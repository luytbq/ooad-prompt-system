# X2 - Thiết kế unit test - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | X2 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (Java 17, JUnit 5, Mockito); P12-class-design/PKG-09-15-16-rental-core.md 1.0; P06 1.0; P04 UC-005, UC-007 1.0; P13 1.0 |
| Phạm vi | DC-FareCalculator.calculate, DC-RentBikeService.requestRental |

Placeholder: PHAM_VI_TEST = "DC-FareCalculator.calculate(Duration), DC-RentBikeService.requestRental(UUID, String)"; MUC_TIEU_PHU = "C1 100%"; SINH_MA_TEST = "Có, JUnit 5 và Mockito"; MA_TC_BAT_DAU = Không có; YEU_CAU_BO_SUNG = Không có.

## F1. Bảng chọn operation

| DC.operation | Tiêu chí | Ưu tiên | Chọn |
|---|---|---|---|
| DC-FareCalculator.calculate | BR-07; tính toán; rẽ nhánh | Cao | Có |
| DC-RentBikeService.requestRental | Điều phối UC-005; 5 luồng thay thế; gọi hệ thống ngoài | Cao | Có |
| Các operation khác của hai lớp | - | - | Không: FareCalculator chỉ có một operation; handleBikeRemoved, handleRemovalTimeout ngoài PHAM_VI_TEST |

## F2.1 DC-FareCalculator.calculate

### F2.1.1 Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | + calculate(duration: Duration): Money | P12 F2 |
| Tiền điều kiện | duration >= 0 | P12 F2 |
| Hậu điều kiện | Không đổi trạng thái | P12 F2 |
| Ngoại lệ | IllegalArgumentException khi duration âm | P12 F2 |
| BR | BR-07: miễn phí 30 phút đầu, sau đó 5.000 đồng cho mỗi 15 phút hoặc phần lẻ của 15 phút | P06 |
| Ví dụ trong đặc tả | Chuyến 47 phút có cước 10.000 đồng | P04 UC-007 mục 8 |
| Luồng thay thế | 4a cước lớn hơn 200.000 đồng tạm giữ (Q-02): thuộc bên gọi, không thuộc calculate | P04 UC-007 |

### F2.1.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-01 | duration | duration < 0 | Không hợp lệ | -5 phút | P12 tiền điều kiện |
| EC-02 | duration | 0 <= duration <= 30 phút | Hợp lệ (cước 0) | 10 phút | BR-07 |
| EC-03 | duration | duration > 30 phút | Hợp lệ (cước > 0) | 47 phút | BR-07 |
| EC-04 | duration | null | Không hợp lệ | null | Kết quả chưa quy định (Q-49) |
| EC-05 | phần tính cước (duration - 30 phút) | chia hết cho 15 phút | Hợp lệ | 45 phút | BR-07 |
| EC-06 | phần tính cước | có phần lẻ | Hợp lệ | 47 phút | BR-07 "hoặc phần lẻ" |

### F2.1.3 Giá trị biên

| BV | Biên | Giá trị | Thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-01 | min EC-02 | -1 giây | EC-01 | IllegalArgumentException |
| BV-02 | min EC-02 | 0 | EC-02 | 0 đồng |
| BV-03 | max EC-02 | 30 phút 0 giây | EC-02 | 0 đồng |
| BV-04 | min EC-03 | 30 phút 1 giây | EC-03, EC-06 | 5.000 đồng (tính theo giây; chờ Q-46) |
| BV-05 | biên khối thứ nhất | 45 phút 0 giây | EC-05 | 5.000 đồng |
| BV-06 | biên khối thứ nhất + 1 | 45 phút 1 giây | EC-06 | 10.000 đồng |
| BV-07 | biên đầu ra bằng tiền tạm giữ | 10 giờ 30 phút | EC-05 | 200.000 đồng (40 khối) |
| BV-08 | ngay trên tiền tạm giữ | 10 giờ 30 phút 1 giây | EC-06 | 205.000 đồng (41 khối) |
| BV-09 | thời hạn tối đa của chuyến (BR-09) | 24 giờ | EC-05 | 470.000 đồng (94 khối) |

### F2.1.4 Bảng quyết định

Không áp dụng (một điều kiện đầu vào; các nhánh theo thứ tự).

### F2.1.5 Chuyển trạng thái

Không áp dụng (lớp không trạng thái).

### F2.1.6 Hộp trắng

File diagrams/X2-cfg-DC-FareCalculator-calculate.drawio (theo P12 F3 method).

| N | Nội dung | Loại |
|---|---|---|
| N1 | Bắt đầu | bắt đầu |
| N2 | duration < 0 | quyết định |
| N3 | throw IllegalArgumentException | khối lệnh |
| N4 | duration <= FREE_PERIOD | quyết định |
| N5 | return Money.ZERO | khối lệnh |
| N6 | billable = duration - FREE_PERIOD; blocks = billable / BLOCK | khối lệnh |
| N7 | billable % BLOCK > 0 | quyết định |
| N8 | blocks = blocks + 1 | khối lệnh |
| N9 | return BLOCK_PRICE.times(blocks) | khối lệnh |
| N10 | Kết thúc | kết thúc |

| CE | Từ | Tới | Nhãn |
|---|---|---|---|
| CE1 | N1 | N2 | - |
| CE2 | N2 | N3 | Đúng |
| CE3 | N2 | N4 | Sai |
| CE4 | N4 | N5 | Đúng |
| CE5 | N4 | N6 | Sai |
| CE6 | N6 | N7 | - |
| CE7 | N7 | N8 | Đúng |
| CE8 | N7 | N9 | Sai |
| CE9 | N8 | N9 | - |
| CE10 | N9 | N10 | - |
| CE11 | N3 | N10 | - |
| CE12 | N5 | N10 | - |

V(G) = E - N + 2 = 12 - 10 + 2 = 4 (ba điểm quyết định + 1). Đường đi cơ sở: P1 N1-N2-N3-N10; P2 N1-N2-N4-N5-N10; P3 N1-N2-N4-N6-N7-N8-N9-N10; P4 N1-N2-N4-N6-N7-N9-N10.

| Nhánh | TC phủ |
|---|---|
| CE2 | TC-001 |
| CE3, CE4 | TC-002, TC-003 |
| CE5, CE7, CE9 | TC-004, TC-006, TC-007, TC-009 |
| CE8 | TC-005, TC-008, TC-010 |

C0 = 100%, C1 = 100%. Không có vòng lặp.

### F2.1.7 Test double

Không cần (hàm thuần tính toán, không phụ thuộc).

## F2.2 DC-RentBikeService.requestRental

### F2.2.1 Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | + requestRental(riderId: UUID, dockQrCode: String): RentalOutcome | P12 F2 |
| Tiền điều kiện | Người thuê đã xác thực | P12 F2, P04 UC-005 |
| Hậu điều kiện (thành công) | PaymentHold ACTIVE, RentalRequest AWAITING_REMOVAL, lệnh mở khoá đã giao, mốc 60 giây đã hẹn | P12 F2, F3 |
| Ngoại lệ | UnknownDockException; PaymentOutcomeUnknownException; DockCommunicationException | P12 F2 |
| BR | BR-01, BR-02, BR-03 (qua RiderAccount), BR-04, BR-05, BR-06 | P06 |
| Luồng thay thế | 2a, 2b, 2c, 3a, 5a; 6a thuộc handleRemovalTimeout | P04 UC-005 |
| Kịch bản chính | KB1 đến KB5 | P04 UC-005 mục 8a |
| Thứ tự kiểm tra | tài khoản --> ụ --> xe --> tạm giữ | P12 F3 |

### F2.2.2 Phân vùng tương đương

| EC | Điều kiện | Lớp | Hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-07 | Điều kiện tài khoản | ELIGIBLE | Hợp lệ | có cardReference, không chuyến, nợ 0 | BR-01 đến BR-03 |
| EC-08 | Điều kiện tài khoản | NO_CARD_LINKED | Không hợp lệ | cardReference rỗng | BR-01, 2a |
| EC-09 | Điều kiện tài khoản | TRIP_IN_PROGRESS | Không hợp lệ | existsInProgressByRider = true | BR-02, 2b |
| EC-10 | Điều kiện tài khoản | OUTSTANDING_FARE | Không hợp lệ | outstandingFare = 1 đồng | BR-03, 2c |
| EC-11 | dockQrCode | có ụ | Hợp lệ | "QR-A01" | GL-11 |
| EC-12 | dockQrCode | không có ụ | Không hợp lệ | "QR-XXX" | P12 ngoại lệ |
| EC-13 | Ụ | đang giữ xe | Hợp lệ | dockedBike có | - |
| EC-14 | Ụ | trống | Không hợp lệ | dockedBike rỗng | Q-20 |
| EC-15 | Trạng thái xe | AVAILABLE | Hợp lệ | AVAILABLE | BR-04 |
| EC-16 | Trạng thái xe | AWAITING_INSPECTION | Không hợp lệ | AWAITING_INSPECTION | BR-04, 3a |
| EC-17 | Kết quả tạm giữ | Approved | Hợp lệ | holdRef "H-1" | - |
| EC-18 | Kết quả tạm giữ | Declined | Không hợp lệ | - | 5a |
| EC-19 | Kết quả tạm giữ | Không rõ (ngoại lệ) | Không hợp lệ | PaymentOutcomeUnknownException | P11b F7 |
| EC-20 | Gửi lệnh mở khoá | Lỗi | Không hợp lệ | DockCommunicationException | Q-44 |

Giá trị biên: BV-10 outstandingFare = 0 (ELIGIBLE) và BV-11 outstandingFare = 1 đồng (OUTSTANDING_FARE), theo BR-03 "không nợ cước".

### F2.2.4 Bảng quyết định

```text
| Điều kiện / Hành động              | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
| C1: tài khoản ELIGIBLE             | N  | Y  | Y  | Y  | Y  | Y  |
| C2: tìm thấy ụ theo mã QR          | -  | N  | Y  | Y  | Y  | Y  |
| C3: ụ đang giữ xe                  | -  | -  | N  | Y  | Y  | Y  |
| C4: xe isRentable                  | -  | -  | -  | N  | Y  | Y  |
| C5: tạm giữ Approved               | -  | -  | -  | -  | N  | Y  |
| A1: REJECTED(lý do tài khoản)       | X  | -  | -  | -  | -  | -  |
| A2: ném UnknownDockException       | -  | X  | -  | -  | -  | -  |
| A3: REJECTED (Q-20)                | -  | -  | X  | -  | -  | -  |
| A4: REJECTED(BIKE_NOT_RENTABLE)    | -  | -  | -  | X  | -  | -  |
| A5: REJECTED(HOLD_DECLINED)        | -  | -  | -  | -  | X  | -  |
| A6: gọi placeHold                  | -  | -  | -  | -  | X  | X  |
| A7: lưu hold, request; mở khoá; hẹn 60 giây; UNLOCK_SENT | - | - | - | - | - | X |
```

Gộp bằng "-" có căn cứ: thứ tự kiểm tra ở P12 F3. P04 không nói khi nhiều điều kiện cùng sai thì báo lý do nào (Q-22); thứ tự của P12 được dùng làm oracle, ghi ở Vấn đề còn mở.

### F2.2.6 Hộp trắng

File diagrams/X2-cfg-DC-RentBikeService-requestRental.drawio. Node N1-N16, cạnh CE1-CE20 (bảng trong file drawio có ID trùng). Năm điểm quyết định (N3, N5, N7, N9, N12): V(G) = 6; E - N + 2 = 20 - 16 + 2 = 6. Sáu đường đi cơ sở tương ứng Q1-Q6; TC-011 đến TC-017 phủ C1 = 100%. Lỗi ném từ placeHold, sendUnlockCommand không có trong CFG vì method P12 không xử lý (lan ra ngoài).

### F2.2.7 Test double

| Phụ thuộc | Loại | Hành vi giả lập / xác minh | Lý do |
|---|---|---|---|
| IF-07 IRiderAccountRepository | stub | findById trả RiderAccount dựng sẵn | CSDL |
| IF-08 ITripRepository | stub | existsInProgressByRider trả true/false | CSDL |
| IF-11 IDockRepository | stub | findByQrCode trả Optional | CSDL |
| IF-01 IPaymentGateway | mock | trả HoldResult hoặc ném; xác minh amount = 200.000 và số lần gọi | Hệ thống ngoài |
| IF-09, IF-14 | mock | xác minh save được gọi hay không | CSDL |
| IF-02 IDockCommandSender | mock | xác minh sendUnlockCommand(dock.id, requestId) | Thiết bị |
| IF-05 IScheduler | mock | xác minh schedule(REMOVAL_TIMEOUT, requestId, now + 60 giây) | Thời gian |
| Đồng hồ | stub (Clock.fixed 2026-09-27T01:00:00Z) | Cố định now | P12 chưa có phụ thuộc đồng hồ (Đề xuất sửa P12) |

## F3. Bảng test case

| TC | DC.operation | Kỹ thuật | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn | Phủ | Test double | Ưu tiên |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | FareCalculator.calculate | giá trị biên | - | -1 giây | Ném IllegalArgumentException | P12 tiền điều kiện | BV-01, EC-01, CE2 | - | Cao |
| TC-002 | FareCalculator.calculate | giá trị biên | - | 0 | Money 0 | BR-07 | BV-02, EC-02, CE4 | - | Cao |
| TC-003 | FareCalculator.calculate | giá trị biên | - | 30 phút | Money 0 | BR-07 | BV-03, EC-02 | - | Cao |
| TC-004 | FareCalculator.calculate | giá trị biên | - | 30 phút 1 giây | Money 5.000 (chờ Q-46) | BR-07 | BV-04, EC-03, EC-06, CE7 | - | Cao |
| TC-005 | FareCalculator.calculate | giá trị biên | - | 45 phút | Money 5.000 | BR-07 | BV-05, EC-05, CE8 | - | Cao |
| TC-006 | FareCalculator.calculate | giá trị biên | - | 45 phút 1 giây | Money 10.000 | BR-07 | BV-06, EC-06 | - | Cao |
| TC-007 | FareCalculator.calculate | phân vùng tương đương | - | 47 phút | Money 10.000 | P04 UC-007 mục 8 | EC-03, EC-06 | - | Cao |
| TC-008 | FareCalculator.calculate | giá trị biên | - | 10 giờ 30 phút | Money 200.000 | BR-07, BR-05 | BV-07 | - | Trung bình |
| TC-009 | FareCalculator.calculate | giá trị biên | - | 10 giờ 30 phút 1 giây | Money 205.000 | BR-07; 4a (Q-02) ở bên gọi | BV-08 | - | Trung bình |
| TC-010 | FareCalculator.calculate | giá trị biên | - | 24 giờ | Money 470.000 | BR-07, BR-09 | BV-09 | - | Trung bình |
| TC-011 | RentBikeService.requestRental | bảng quyết định | Tài khoản không có cardReference | riderId R1, "QR-A01" | REJECTED(NO_CARD_LINKED); không gọi docks, placeHold, save, sendUnlockCommand | BR-01, UC-005 2a | EC-08, DT1-Q1, CE3 | stub, mock | Cao |
| TC-012 | RentBikeService.requestRental | phân vùng tương đương | existsInProgressByRider = true | R1, "QR-A01" | REJECTED(TRIP_IN_PROGRESS); không gọi placeHold | BR-02, 2b | EC-09, DT1-Q1 | stub, mock | Cao |
| TC-013 | RentBikeService.requestRental | giá trị biên | outstandingFare = 1 đồng | R1, "QR-A01" | REJECTED(OUTSTANDING_FARE); không gọi placeHold | BR-03, 2c, KB2 | EC-10, BV-11, DT1-Q1 | stub, mock | Cao |
| TC-014 | RentBikeService.requestRental | bảng quyết định | Tài khoản ELIGIBLE; findByQrCode rỗng | R1, "QR-XXX" | Ném UnknownDockException; không gọi placeHold | P12 ngoại lệ | EC-12, DT1-Q2, CE6 | stub, mock | Cao |
| TC-015 | RentBikeService.requestRental | bảng quyết định | Ụ trống | R1, "QR-A01" | REJECTED; lý do chờ Q-20; không gọi placeHold | Q-20 | EC-14, DT1-Q3, CE8 | stub, mock | Trung bình |
| TC-016 | RentBikeService.requestRental | bảng quyết định | Xe AWAITING_INSPECTION | R1, "QR-A01" | REJECTED(BIKE_NOT_RENTABLE); không gọi placeHold | BR-04, 3a, KB3 | EC-16, DT1-Q4, CE10 | stub, mock | Cao |
| TC-017 | RentBikeService.requestRental | use case | placeHold trả Declined | R1, "QR-A01" | REJECTED(HOLD_DECLINED); placeHold gọi 1 lần với 200.000; không save; không sendUnlockCommand | 5a, KB4 | EC-18, DT1-Q5, CE12 | mock | Cao |
| TC-018 | RentBikeService.requestRental | use case | Mọi điều kiện đạt; outstandingFare = 0; now = 2026-09-27T01:00:00Z | R1, "QR-A01" | UNLOCK_SENT; placeHold(cardRef C1, 200.000, requestId); holds.save 1 lần (ACTIVE, H-1); requests.save 1 lần (AWAITING_REMOVAL, createdAt = now); sendUnlockCommand(dockId, requestId) cùng requestId; schedule(REMOVAL_TIMEOUT, requestId, now + 60 giây) | KB1, BR-05, BR-06 | EC-07, EC-11, EC-13, EC-15, EC-17, BV-10, DT1-Q6, CE13 | mock | Cao |
| TC-019 | RentBikeService.requestRental | use case | placeHold ném PaymentOutcomeUnknownException | R1, "QR-A01" | Ngoại lệ lan ra; không save; không sendUnlockCommand. Hậu điều kiện tối thiểu UC-005 (không còn khoản tạm giữ) không kiểm được (X1 RV-01, Q-42) | P11b F7 | EC-19 | mock | Cao |
| TC-020 | RentBikeService.requestRental | use case | sendUnlockCommand ném DockCommunicationException | R1, "QR-A01" | Chưa quy định (Q-44): có huỷ tạm giữ hay không; test bị bỏ qua | Q-44 | EC-20 | mock | Trung bình |

## F4. Ma trận phủ

| Mục cần phủ | TC phủ | Đạt |
|---|---|---|
| EC-01 đến EC-03, EC-05, EC-06 | TC-001 đến TC-010 | Có |
| EC-04 (null) | - | Không: Q-49 |
| BV-01 đến BV-09 | TC-001 đến TC-010 | Có (TC-004 phụ thuộc Q-46) |
| EC-07 đến EC-20, BV-10, BV-11 | TC-011 đến TC-020 | Có (TC-015, TC-020 chờ Q-20, Q-44) |
| DT1-Q1 đến DT1-Q6 | TC-011 đến TC-018 | Có |
| BR-01, BR-02, BR-03 | TC-011, TC-012, TC-013 | Có (qua RiderAccount thật) |
| BR-04 | TC-016 | Có |
| BR-05 | TC-017, TC-018 | Có |
| BR-06 | TC-018 (hẹn giờ) | Một phần: hết 60 giây (6a, KB5) thuộc handleRemovalTimeout, ngoài phạm vi |
| BR-07 | TC-002 đến TC-010 | Có |
| UC-005 2a, 2b, 2c, 3a, 5a | TC-011 đến TC-013, TC-016, TC-017 | Có |
| UC-005 6a (KB5) | - | Không: ngoài phạm vi (handleRemovalTimeout) |
| NFR-02 (2 giây) | - | Không: kiểm thử hiệu năng, không phải unit test |
| C1 calculate | TC-001 đến TC-010 | 100% |
| C1 requestRental | TC-011 đến TC-018 | 100% |

## F5. Khung mã test

```java
class FareCalculatorTest {
    private final FareCalculator calculator = new FareCalculator();

    @Test
    @DisplayName("TC-001 calculate: thời lượng âm thì ném IllegalArgumentException")
    void calculate_negativeDuration_throwsIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> calculator.calculate(Duration.ofSeconds(-1)));
    }

    @ParameterizedTest(name = "TC-002..TC-010: calculate({0} giây) = {1} đồng")
    @CsvSource({
        "0, 0",          // TC-002
        "1800, 0",       // TC-003
        "1801, 5000",    // TC-004 (Q-46)
        "2700, 5000",    // TC-005
        "2701, 10000",   // TC-006
        "2820, 10000",   // TC-007
        "37800, 200000", // TC-008
        "37801, 205000", // TC-009
        "86400, 470000"  // TC-010
    })
    void calculate_validDuration_returnsFarePerBr07(long seconds, long expectedFare) {
        assertEquals(Money.of(expectedFare), calculator.calculate(Duration.ofSeconds(seconds)));
    }
}

@ExtendWith(MockitoExtension.class)
class RentBikeServiceTest {
    private static final Instant NOW = Instant.parse("2026-09-27T01:00:00Z");
    @Mock IRiderAccountRepository accounts;
    @Mock ITripRepository trips;
    @Mock IDockRepository docks;
    @Mock IPaymentHoldRepository holds;
    @Mock IRentalRequestRepository requests;
    @Mock IPaymentGateway paymentGateway;
    @Mock IDockCommandSender dockCommands;
    @Mock IScheduler scheduler;
    private RentBikeService service;
    private final UUID riderId = UUID.randomUUID();

    @BeforeEach
    void setUp() {
        // Clock chưa có trong P12 (Đề xuất sửa P12)
        service = new RentBikeService(accounts, trips, docks, holds, requests, paymentGateway, dockCommands, scheduler,
                Clock.fixed(NOW, ZoneOffset.UTC));
    }

    @Test
    @DisplayName("TC-011 requestRental: chưa liên kết thẻ thì từ chối NO_CARD_LINKED và không tạm giữ")
    void requestRental_noCardLinked_rejectedWithoutHold() {
        // Arrange: tài khoản không có cardReference
        // Act: service.requestRental(riderId, "QR-A01")
        // Assert: REJECTED(NO_CARD_LINKED); verifyNoInteractions(paymentGateway, dockCommands, holds, requests)
    }

    @Test
    @DisplayName("TC-017 requestRental: tạm giữ bị từ chối thì trả HOLD_DECLINED và không mở khoá")
    void requestRental_holdDeclined_rejectedWithoutUnlock() {
        // Assert: verify(paymentGateway).placeHold(any(), eq(Money.of(200000)), any()); verifyNoInteractions(dockCommands, holds, requests)
    }

    @Test
    @DisplayName("TC-018 requestRental: đủ điều kiện thì tạm giữ, lưu lượt chờ, mở khoá, hẹn 60 giây")
    void requestRental_allConditionsMet_unlockSentAndTimeoutScheduled() {
        // Assert: UNLOCK_SENT; ArgumentCaptor<UUID> requestId từ placeHold;
        // verify(dockCommands).sendUnlockCommand(dockId, requestId); verify(scheduler).schedule(REMOVAL_TIMEOUT, requestId, NOW.plusSeconds(60))
    }

    @Test
    @Disabled("Q-44: chưa quy định xử lý khi không gửi được lệnh mở khoá")
    void requestRental_unlockCommandFails_behaviourUndefined() {
    }

    // TC-012 đến TC-016, TC-019 theo bảng F3, cùng cấu trúc
}
```

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-49 | FareCalculator.calculate nhận null thì phải làm gì (ném IllegalArgumentException hay NullPointerException)? | TC cho EC-04 | P12 F2 không nêu |

Liên quan: Q-20, Q-22, Q-42, Q-44, Q-46.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P12 | DC-RentBikeService | Method dùng "now" (RentalRequest.open, schedule) nhưng lớp không có phụ thuộc đồng hồ; không test lặp lại được | Thêm association tới java.time.Clock (tiêm qua constructor) |
| P12 | DC-FareCalculator.calculate | Không nêu hành vi với null | Thêm ngoại lệ hoặc ghi rõ tiền điều kiện duration khác null |
| P04 | UC-007 mục Vấn đề còn mở | Ghi "chuyến dài hơn khoảng 8 giờ 45 phút có cước vượt 200.000 đồng"; theo BR-07 cước bằng 200.000 đồng ở 10 giờ 30 phút và vượt từ 10 giờ 30 phút 1 giây (TC-008, TC-009) | Sửa thành "dài hơn 10 giờ 30 phút" |

## Vấn đề còn mở

- Oracle của TC-011 đến TC-016 khi nhiều điều kiện cùng sai dựa trên thứ tự kiểm tra của P12 F3, không có trong P04 (Q-22).
- Khung mã chỉ viết đầy đủ thân cho FareCalculatorTest; RentBikeServiceTest có Arrange - Act - Assert ở dạng chú thích vì DC-RentBikeService chưa có constructor chốt (thiếu Clock).
