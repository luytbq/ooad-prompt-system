# P11b - Giao diện hệ thống và thiết bị - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI; CONG_NGHE sau P09); P04 UC-005, UC-007, UC-009; P06; P07 UC-005, UC-007, UC-009; P08; P09; P10 1.0 |
| Phạm vi | SS-01 PaymentGatewaySubsystem, SS-02 DockCommunicationSubsystem |

Placeholder: PHAM_VI_SUBSYSTEM = "SS-01 PaymentGatewaySubsystem, SS-02 DockCommunicationSubsystem"; TAI_LIEU_GIAO_TIEP = Không có; CHINH_SACH_LOI = Không có; YEU_CAU_BO_SUNG = Không có.

## SS-01 PaymentGatewaySubsystem

### F1. Bối cảnh sử dụng

| UC | Control gọi | Message trong P07 | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-005 | DC-RentBikeService (AC-C-RentBikeController) | 1.1.6 // requestHold; 3.2 // requestCancelHold | 200.000 đồng, mã tham chiếu thẻ; mã khoản tạm giữ | 5a tạm giữ không thành công; không có luồng cho cổng không phản hồi (Q-08) |
| UC-007 | DC-ReturnBikeService | 1.1.5 // requestCapture; 1.1.7 // requestReleaseRemainder | Cước, khoản tạm giữ; phần dư | Không có (Q-23) |
| UC-009 | DC-RecordLostBikeService | 1.3 // requestCapture | Toàn bộ số tiền tạm giữ | Không có (Q-23) |

### F2. Interface

| IF | Tên | Vai trò | Subsystem hiện thực | Client | Package chứa |
|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Cho phép hệ thống tạm giữ, huỷ, thu và trả lại tiền trên thẻ đã liên kết. | SS-01 | DC-RentBikeService, DC-ReturnBikeService, DC-RecordLostBikeService (PKG-09) | PKG-18 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Cổng thanh toán | placeHold(cardRef: CardReference, amount: Money, requestId: UUID): HoldResult | cardRef: CardReference - mã do cổng cấp (GL-12)<br>amount: Money - 200.000 đồng (BR-05)<br>requestId: UUID - sinh một lần cho mỗi lượt quét | HoldResult: status (Approved / Declined), holdRef: HoldReference (Q-30) | Declined trong kết quả (Nghiệp vụ); PaymentGatewayUnavailableException (Kỹ thuật tạm thời); PaymentOutcomeUnknownException (Không rõ kết quả) | UC-005 | Tài khoản có cardRef | Approved: có khoản tạm giữ trên thẻ | Có | Có với khoá requestId nếu cổng hỗ trợ (Q-42) | Chưa quy định (Q-41); phải nhỏ hơn phần còn lại của 2 giây NFR-02 nếu Q-13 = Có |
| IF-01 | IPaymentGateway | Cổng thanh toán | cancelHold(holdRef: HoldReference): void | holdRef: HoldReference | - | PaymentGatewayUnavailableException (Kỹ thuật tạm thời); PaymentOutcomeUnknownException (Không rõ kết quả) | UC-005 | Khoản tạm giữ chưa thu | Khoản tạm giữ bị huỷ | Có | Có (huỷ lại một khoản đã huỷ không đổi trạng thái; cần xác nhận Q-42) | Chưa quy định (Q-41) |
| IF-01 | IPaymentGateway | Cổng thanh toán | capture(holdRef: HoldReference, amount: Money): CaptureResult | holdRef: HoldReference<br>amount: Money - từ 0 tới số tiền tạm giữ (Q-02, Q-31) | CaptureResult: status (Captured / Rejected), captureRef | Rejected trong kết quả (Nghiệp vụ); PaymentGatewayUnavailableException; PaymentOutcomeUnknownException | UC-007, UC-009 | Khoản tạm giữ còn hiệu lực | Số tiền đã được thu | Có | Không (trừ khi cổng hỗ trợ khoá, Q-42) | Chưa quy định (Q-41) |
| IF-01 | IPaymentGateway | Cổng thanh toán | releaseRemainder(holdRef: HoldReference, amount: Money): ReleaseResult | holdRef: HoldReference<br>amount: Money - 200.000 đồng trừ cước | ReleaseResult: status (Released / Rejected) | Như capture | UC-007 | Đã capture | Phần dư được trả lại | Có | Không (Q-42) | Chưa quy định (Q-41) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-01.drawio, trang 1-7.

#### Hộp đen - UC-005

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-RBS | Lifeline | :RentBikeService | - | - | DC-RentBikeService |
| L-IF1 | Lifeline | :IPaymentGateway | «interface» | - | IF-01 |
| F1 | Fragment | alt [Approved] ...(tiếp UC-005 bước 6) | - | - | Bao S1 đến M4 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | L-RBS | L-IF1 | placeHold(cardRef, Money(200000), rentalRequestId) | Đồng bộ | - | UC-005 bước 4 |
| 1 (trả về) | L-IF1 | L-RBS | HoldResult(status, holdRef) | Trả về | - | UC-005 bước 5 |
| 2 | L-RBS | L-IF1 | cancelHold(holdRef) | Đồng bộ | F1 | UC-005 bước 6a2 |
| 2 (trả về) | L-IF1 | L-RBS | void | Trả về | F1 | UC-005 bước 6a2 |

#### Hộp đen - UC-007

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-RTS | Lifeline | :ReturnBikeService | - | - |  |
| L-IF1 | Lifeline | :IPaymentGateway | «interface» | - | IF-01 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | L-RTS | L-IF1 | capture(holdRef, fare) | Đồng bộ | - | UC-007 bước 5 |
| 1 (trả về) | L-IF1 | L-RTS | CaptureResult(status, captureRef) | Trả về | - | UC-007 bước 5 |
| 2 | L-RTS | L-IF1 | releaseRemainder(holdRef, Money(200000) - fare) | Đồng bộ | - | UC-007 bước 6 (Q-26) |
| 2 (trả về) | L-IF1 | L-RTS | ReleaseResult(status) | Trả về | - | UC-007 bước 6 |

#### Hộp đen - UC-009

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-LBS | Lifeline | :RecordLostBikeService | - | - |  |
| L-IF1 | Lifeline | :IPaymentGateway | «interface» | - | IF-01 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | L-LBS | L-IF1 | capture(holdRef, hold.amount) | Đồng bộ | - | UC-009 bước 3 |
| 1 (trả về) | L-IF1 | L-LBS | CaptureResult(status, captureRef) | Trả về | - | UC-009 bước 3 |

#### Hộp trắng - placeHold

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| G1 | Lifeline | placeHold | - | - | Gate |
| L-FAC | Lifeline | :PaymentGatewayFacade | - | - | DC-PaymentGatewayFacade |
| L-MAP | Lifeline | :PaymentMessageMapper | - | - | DC-PaymentMessageMapper |
| L-CLI | Lifeline | :BankApiClient | - | - | DC-BankApiClient |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |
| F1 | Fragment | alt [có phản hồi] | - | - | Bao M4 đến M5 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | G1 | L-FAC | placeHold(cardRef, amount, rentalRequestId) | Đồng bộ | - | placeHold |
| 1.1 | L-FAC | L-MAP | toHoldRequest(cardRef, amount, rentalRequestId) | Đồng bộ | - | placeHold |
| 1.2 | L-FAC | L-CLI | post(holdRequest) [timeout Q-41] | Đồng bộ | - | placeHold |
| 1.2.1 | L-CLI | A-07 | tạm giữ tiền (API ngân hàng, chưa có tài liệu) | Đồng bộ | - | placeHold |
| 1.2 (trả về) | L-CLI | L-FAC | phản hồi ngân hàng | Trả về | - | placeHold |
| 1.3 | L-FAC | L-FAC | throw PaymentOutcomeUnknownException(rentalRequestId) | Tự gọi | F1 | placeHold |
| 1.4 | L-FAC | L-MAP | toHoldResult(response) | Đồng bộ | - | placeHold |

#### Hộp trắng - cancelHold

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| G1 | Lifeline | cancelHold | - | - | Gate |
| L-FAC | Lifeline | :PaymentGatewayFacade | - | - | DC-PaymentGatewayFacade |
| L-MAP | Lifeline | :PaymentMessageMapper | - | - | DC-PaymentMessageMapper |
| L-CLI | Lifeline | :BankApiClient | - | - | DC-BankApiClient |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | G1 | L-FAC | cancelHold(holdRef) | Đồng bộ | - | cancelHold |
| 1.1 | L-FAC | L-CLI | post(cancelRequest(holdRef)) | Đồng bộ | - | cancelHold |
| 1.1.1 | L-CLI | A-07 | huỷ tạm giữ (API ngân hàng) | Đồng bộ | - | cancelHold |
| 1.1 (trả về) | L-CLI | L-FAC | phản hồi ngân hàng | Trả về | - | cancelHold |

#### Hộp trắng - capture

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| G1 | Lifeline | capture | - | - | Gate |
| L-FAC | Lifeline | :PaymentGatewayFacade | - | - | DC-PaymentGatewayFacade |
| L-MAP | Lifeline | :PaymentMessageMapper | - | - | DC-PaymentMessageMapper |
| L-CLI | Lifeline | :BankApiClient | - | - | DC-BankApiClient |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | G1 | L-FAC | capture(holdRef, amount) | Đồng bộ | - | capture |
| 1.1 | L-FAC | L-MAP | toCaptureRequest(holdRef, amount) | Đồng bộ | - | capture |
| 1.2 | L-FAC | L-CLI | post(captureRequest) | Đồng bộ | - | capture |
| 1.2.1 | L-CLI | A-07 | thu tiền từ khoản tạm giữ (API ngân hàng) | Đồng bộ | - | capture |
| 1.2 (trả về) | L-CLI | L-FAC | phản hồi ngân hàng | Trả về | - | capture |
| 1.3 | L-FAC | L-MAP | toCaptureResult(response) | Đồng bộ | - | capture |

#### Hộp trắng - releaseRemainder

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| G1 | Lifeline | releaseRemainder | - | - | Gate |
| L-FAC | Lifeline | :PaymentGatewayFacade | - | - | DC-PaymentGatewayFacade |
| L-MAP | Lifeline | :PaymentMessageMapper | - | - | DC-PaymentMessageMapper |
| L-CLI | Lifeline | :BankApiClient | - | - | DC-BankApiClient |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | G1 | L-FAC | releaseRemainder(holdRef, amount) | Đồng bộ | - | releaseRemainder |
| 1.1 | L-FAC | L-CLI | post(releaseRequest(holdRef, amount)) [API hoàn tiền hay huỷ một phần: Q-26] | Đồng bộ | - | releaseRemainder |
| 1.1.1 | L-CLI | A-07 | hoàn tiền hoặc huỷ phần tạm giữ còn lại | Đồng bộ | - | releaseRemainder |
| 1.1 (trả về) | L-CLI | L-FAC | phản hồi ngân hàng | Trả về | - | releaseRemainder |

### F5. Phần tử của subsystem

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-PaymentGatewayFacade | PaymentGatewayFacade | Điều phối | Nhận lời gọi IF-01, gọi mapper và client, chuyển lỗi giao thức thành ngoại lệ của interface | package-private | IF-01 |
| DC-PaymentMessageMapper | PaymentMessageMapper | Chuyển đổi dữ liệu | Chuyển CardReference, Money, HoldReference sang định dạng API ngân hàng và ngược lại | package-private | - |
| DC-BankApiClient | BankApiClient | Giao tiếp ngoài | Gửi yêu cầu tới cổng, áp timeout, xác thực với cổng | package-private | - |
| DC-HoldResult, DC-CaptureResult, DC-ReleaseResult | HoldResult, CaptureResult, ReleaseResult | Kiểu dữ liệu | Kết quả operation | public (đi cùng IF-01) | - |
| DC-PaymentGatewayUnavailableException, DC-PaymentOutcomeUnknownException | - | Ngoại lệ | Lỗi kỹ thuật tạm thời; kết quả không rõ | public (đi cùng IF-01) | - |

Class diagram: trang "Phần tử".

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| SS-01 | Subsystem | PaymentGatewaySubsystem | «subsystem» | - | Khung |
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-18 | 4 operation |
| DC-PaymentGatewayFacade, DC-PaymentMessageMapper, DC-BankApiClient | Class | - | - | SS-01 | - |
| DC-HoldResult | Class | HoldResult | «datatype» | SS-01 | - |
| DC-PaymentOutcomeUnknownException, DC-PaymentGatewayUnavailableException | Class | - | «exception» | SS-01 | - |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú |
|---|---|---|---|---|---|
| R1 | DC-PaymentGatewayFacade | IF-01 | Realization | - | - |
| R2 | DC-PaymentGatewayFacade | DC-PaymentMessageMapper | Dependency | - | - |
| R3 | DC-PaymentGatewayFacade | DC-BankApiClient | Dependency | - | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào | Loại | Lý do | Đánh giá |
|---|---|---|---|---|
| SS-01 | PKG-15 RentalDomain (Money, CardReference, HoldReference) | Vào package | Kiểu giá trị của mô hình dùng trong chữ ký IF-01 | Dùng thận trọng: PKG-18 ở layer dưới phụ thuộc PKG-15 ở layer trên (xem Vấn đề còn mở) |

### F7. Xử lý lỗi và điểm kiểm tra

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| placeHold | Cổng từ chối | Nghiệp vụ | Phản hồi Declined | Không thử lại | HoldResult(Declined) | UC-005 5a | Q-08 |
| placeHold | Không kết nối được | Kỹ thuật tạm thời | Lỗi kết nối trước khi gửi | Không thử lại (ngân sách 2 giây) | PaymentGatewayUnavailableException | Không có | Đề xuất sửa P04; Q-08 |
| placeHold | Hết thời gian chờ sau khi gửi | Không rõ kết quả | Timeout | Không thử lại; không có operation tra cứu vì chưa biết cổng hỗ trợ | PaymentOutcomeUnknownException | Không có. Tiền có thể đã bị giữ mà chuyến không bắt đầu | Q-42; đề xuất sửa P04 |
| cancelHold | Không kết nối, timeout | Kỹ thuật tạm thời / Không rõ | Lỗi, timeout | Được thử lại nếu Q-42 xác nhận huỷ là idempotent; tối đa: chưa quy định | Ngoại lệ tương ứng | Không có | Q-41, Q-42 |
| capture | Cổng từ chối, lỗi, timeout | Nghiệp vụ / Kỹ thuật / Không rõ | Phản hồi, timeout | Không thử lại (tác dụng tài chính, không idempotent) | CaptureResult(Rejected) hoặc ngoại lệ | Không có | Q-23 |
| releaseRemainder | Như capture | - | - | Không thử lại | Như capture | Không có | Q-23, Q-26 |

| Điểm kiểm tra | SS-01 |
|---|---|
| Interface cung cấp có realization | Đạt |
| Interface dùng có phụ thuộc | Không áp dụng |
| Không phần tử bên trong public | Đạt (trừ kiểu dữ liệu và ngoại lệ đi cùng interface) |
| Mỗi operation có hộp trắng | Đạt |

## SS-02 DockCommunicationSubsystem

### F1. Bối cảnh sử dụng

| UC | Control gọi | Message trong P07 | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-005 | DC-RentBikeService | 1.1.9 // sendUnlockCommand; 3.1 // sendLockCommand; 2 // reportBikeRemoved (thiết bị --> hệ thống) | Ụ khoá; ụ, xe | 6a hết 60 giây; không có luồng mất kết nối ụ |
| UC-007 | DC-ReturnBikeService (qua DC-DockEventHandler) | 1 // reportBikeReturned | Ụ, xe | Không có |

### F2. Interface

| IF | Tên | Vai trò | Subsystem hiện thực | Client | Package chứa |
|---|---|---|---|---|---|
| IF-02 | IDockCommandSender | Gửi lệnh mở khoá, khoá lại tới một ụ khoá. | SS-02 | DC-RentBikeService (PKG-09) | PKG-19 |
| IF-03 | IDockEventListener | Nhận sự kiện xe được rút ra, xe được đưa vào từ ụ khoá. Do phía hệ thống cung cấp (DC-DockEventHandler, PKG-09 hiện thực), SS-02 gọi vào. | Không (Application hiện thực) | SS-02 | PKG-19 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-02 | IDockCommandSender | Ụ khoá | sendUnlockCommand(dockId: DockId, requestId: UUID): void | dockId: DockId - định danh ụ (Q-36)<br>requestId: UUID - lượt thuê | - (không có xác nhận từ ụ; Q-36) | DockCommunicationException (Kỹ thuật tạm thời: broker không nhận) | UC-005 | Khoản tạm giữ Approved | Lệnh đã giao cho broker | Không (bất đồng bộ) | Có với khoá requestId nếu ụ bỏ qua lệnh trùng (Q-36) | Giao cho broker: chưa quy định (Q-41) |
| IF-02 | IDockCommandSender | Ụ khoá | sendLockCommand(dockId: DockId): void | dockId: DockId | - | DockCommunicationException | UC-005 | Hết 60 giây (BR-06) | Lệnh đã giao cho broker | Không | Có (khoá lại ụ đã khoá không đổi trạng thái) | Chưa quy định (Q-41) |
| IF-03 | IDockEventListener | Ụ khoá | onBikeRemoved(event: DockEvent): void | event: DockEvent - type, dockId, bikeId, occurredAt, eventId (Q-43) | - | Không (lỗi xử lý thuộc bên hiện thực) | UC-005 | Có lượt thuê đang chờ rút xe ở ụ (không kiểm tra trong SS-02) | - | Không | Bên hiện thực phải bỏ qua eventId đã xử lý | - |
| IF-03 | IDockEventListener | Ụ khoá | onBikeReturned(event: DockEvent): void | event: DockEvent | - | Không | UC-007 | - | - | Không | Như trên | - |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-02.drawio, trang 1-5.

#### Hộp đen - UC-005

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-RBS | Lifeline | :RentBikeService | - | - |  |
| L-IF2 | Lifeline | :IDockCommandSender | «interface» | - | IF-02 |
| L-SS2 | Lifeline | :DockCommunicationSubsystem | «subsystem» | - | SS-02, gọi ngược |
| L-IF3 | Lifeline | :IDockEventListener | «interface» | - | IF-03 (DockEventHandler hiện thực) |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | L-RBS | L-IF2 | sendUnlockCommand(dockId, rentalRequestId) | Bất đồng bộ | - | UC-005 bước 6 |
| 2 | L-SS2 | L-IF3 | onBikeRemoved(DockEvent(dockId, bikeId, occurredAt, eventId)) | Bất đồng bộ | - | UC-005 bước 7 |
| 3 | L-RBS | L-IF2 | sendLockCommand(dockId) | Bất đồng bộ | - | UC-005 bước 6a1 |

#### Hộp đen - UC-007

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-SS2 | Lifeline | :DockCommunicationSubsystem | «subsystem» | - | SS-02 |
| L-IF3 | Lifeline | :IDockEventListener | «interface» | - | IF-03 (DockEventHandler hiện thực) |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | L-SS2 | L-IF3 | onBikeReturned(DockEvent(dockId, bikeId, occurredAt, eventId)) | Bất đồng bộ | - | UC-007 bước 2 |

#### Hộp trắng - sendUnlockCommand

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| G1 | Lifeline | sendUnlockCommand | - | - | Gate |
| L-DGS | Lifeline | :DockGatewayService | - | - |  |
| L-COD | Lifeline | :DockMessageCodec | - | - |  |
| L-MQ | Lifeline | :MqttConnection | - | - |  |
| A-08 | Actor | Ụ khoá (qua MQTT broker) | - | - | ACT-08 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | G1 | L-DGS | sendUnlockCommand(dockId, rentalRequestId) | Bất đồng bộ | - | sendUnlockCommand |
| 1.1 | L-DGS | L-COD | encodeUnlock(dockId, rentalRequestId) | Đồng bộ | - | sendUnlockCommand |
| 1.2 | L-DGS | L-MQ | publish(topic(dockId), payload) [topic, QoS: Q-36] | Đồng bộ | - | sendUnlockCommand |
| 1.2.1 | L-MQ | A-08 | lệnh mở khoá | Bất đồng bộ | - | sendUnlockCommand |

#### Hộp trắng - sendLockCommand

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| G1 | Lifeline | sendLockCommand | - | - | Gate |
| L-DGS | Lifeline | :DockGatewayService | - | - |  |
| L-COD | Lifeline | :DockMessageCodec | - | - |  |
| L-MQ | Lifeline | :MqttConnection | - | - |  |
| A-08 | Actor | Ụ khoá (qua MQTT broker) | - | - | ACT-08 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | G1 | L-DGS | sendLockCommand(dockId) | Bất đồng bộ | - | sendLockCommand |
| 1.1 | L-DGS | L-COD | encodeLock(dockId) | Đồng bộ | - | sendLockCommand |
| 1.2 | L-DGS | L-MQ | publish(topic(dockId), payload) | Đồng bộ | - | sendLockCommand |
| 1.2.1 | L-MQ | A-08 | lệnh khoá lại | Bất đồng bộ | - | sendLockCommand |

#### Hộp trắng - onBikeRemoved, onBikeReturned (chiều thiết bị --> hệ thống)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| A-08 | Actor | Ụ khoá (qua MQTT broker) | - | - | ACT-08 |
| L-MQ | Lifeline | :MqttConnection | - | - |  |
| L-DSP | Lifeline | :DockEventDispatcher | - | - |  |
| L-COD | Lifeline | :DockMessageCodec | - | - |  |
| L-IF3 | Lifeline | :IDockEventListener | «interface» | - | IF-03 |
| F1 | Fragment | alt [không trùng] [type = BIKE_REMOVED] | - | - | Bao M5 đến M6 |

| STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | A-08 | L-MQ | thông điệp sự kiện ụ | Bất đồng bộ | - | onBikeRemoved, onBikeReturned |
| 1.1 | L-MQ | L-DSP | onMessage(topic, payload) | Bất đồng bộ | - | - |
| 1.1.1 | L-DSP | L-COD | decode(payload) | Đồng bộ | - | - |
| 1.1.1 (trả về) | L-COD | L-DSP | DockEvent(type, dockId, bikeId, occurredAt, eventId) | Trả về | - | - |
| 1.1.2 | L-DSP | L-DSP | isDuplicate(eventId) [eventId: Q-43] | Tự gọi | - | - |
| 1.1.3 | L-DSP | L-IF3 | onBikeRemoved(event) | Bất đồng bộ | F1 | UC-005 bước 7 |
| 1.1.4 | L-DSP | L-IF3 | onBikeReturned(event) | Bất đồng bộ | F1 | UC-007 bước 2 |

### F5. Phần tử của subsystem

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-DockGatewayService | DockGatewayService | Điều phối | Nhận lệnh IF-02, mã hoá, publish | package-private | IF-02 |
| DC-DockMessageCodec | DockMessageCodec | Chuyển đổi dữ liệu | Mã hoá lệnh, giải mã sự kiện theo định dạng nhà cung cấp (Q-36) | package-private | - |
| DC-MqttConnection | MqttConnection | Giao tiếp ngoài | Kết nối broker, publish, subscribe, kết nối lại | package-private | - |
| DC-DockEventDispatcher | DockEventDispatcher | Điều phối | Nhận thông điệp, lọc eventId trùng, gọi IF-03 theo loại sự kiện | package-private | - |
| DC-DockEvent | DockEvent | Kiểu dữ liệu | Sự kiện ụ đã giải mã | public (đi cùng IF-03) | - |
| DC-DockCommunicationException | - | Ngoại lệ | Broker không nhận lệnh | public | - |

Class diagram: trang "Phần tử" (IF-02, IF-03, 5 lớp; R1 realization DockGatewayService --> IF-02; R2-R5 dependency).

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào | Loại | Lý do | Đánh giá |
|---|---|---|---|---|
| SS-02 | IF-03 IDockEventListener | Qua interface | Gọi ngược sự kiện thiết bị lên Application | Ưu tiên |

### F7. Xử lý lỗi và điểm kiểm tra

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| sendUnlockCommand | Broker không nhận | Kỹ thuật tạm thời | Lỗi publish | Không thử lại (ngân sách 2 giây) | DockCommunicationException | Không có; khoản tạm giữ đã tạo sẽ ra sao | Đề xuất sửa P04; Q-44 |
| sendUnlockCommand | Ụ mất kết nối, không thực hiện | Thiết bị | Không phát hiện được (không có xác nhận) | - | - | Rơi vào 6a sau 60 giây | Q-36 |
| sendLockCommand | Broker không nhận | Kỹ thuật tạm thời | Lỗi publish | Thử lại (idempotent), số lần chưa quy định | DockCommunicationException sau khi hết lượt | Không có | Q-41 |
| onBikeRemoved, onBikeReturned | Thông điệp trùng | Thiết bị | eventId đã xử lý | Bỏ qua | - | - | Q-43 |
| onBikeRemoved, onBikeReturned | Thông điệp hỏng | Thiết bị | Giải mã lỗi | Ghi nhận, bỏ qua | - | Không có | Q-36 |
| onBikeRemoved | Báo rút xe đến sau khi đã hết 60 giây | Thiết bị | Bên hiện thực IF-03 thấy lượt thuê đã huỷ | Không thuộc SS-02 | - | Không có | Q-45 |

| Điểm kiểm tra | SS-02 |
|---|---|
| Interface cung cấp có realization | Đạt |
| Interface dùng có phụ thuộc | Đạt (IF-03) |
| Không phần tử bên trong public | Đạt |
| Mỗi operation có hộp trắng | Đạt (onBikeRemoved, onBikeReturned chung một sơ đồ) |

## F8. Tổng hợp toàn hệ thống

| SS | IF | Số operation | UC dùng | Rủi ro chính |
|---|---|---|---|---|
| SS-01 | IF-01 | 4 | UC-005, UC-007, UC-009 | Kết quả không rõ khi tạm giữ; không có tài liệu API |
| SS-02 | IF-02, IF-03 | 2 + 2 | UC-005, UC-007 | Không có xác nhận từ ụ; giao thức chưa có tài liệu |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-41 | Thời gian chờ tối đa khi gọi cổng thanh toán và khi giao lệnh cho MQTT broker là bao nhiêu, và số lần thử lại cho thao tác idempotent? | IF-01, IF-02 | Mục 13, 14; CHINH_SACH_LOI = Không có |
| Q-42 | Cổng thanh toán có hỗ trợ khoá idempotency và API tra cứu trạng thái giao dịch không? | placeHold, capture, releaseRemainder | Hồ sơ dự án "chưa có tài liệu API" |
| Q-43 | Thông điệp sự kiện của ụ có định danh duy nhất để phát hiện trùng không? | DockEvent, IF-03 | Hồ sơ dự án "chưa có tài liệu giao thức" |
| Q-44 | Khi không gửi được lệnh mở khoá (broker không nhận), hệ thống có huỷ khoản tạm giữ ngay và báo người thuê xe không? (Có / Không) | UC-005, SS-02 | Mục 3 chỉ nêu trường hợp hết 60 giây |
| Q-45 | Khi ụ báo xe được rút ra sau khi hệ thống đã khoá lại ụ và huỷ tạm giữ (hết 60 giây), hệ thống xử lý thế nào? | UC-005, IF-03 | Mục 3 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-005 | Không có luồng cho cổng thanh toán không phản hồi hoặc kết quả không rõ ở bước 4-5 | Thêm luồng 5b sau khi trả lời Q-08, Q-42 |
| P04 | UC-005 | Không có luồng khi không gửi được lệnh mở khoá | Thêm luồng 6b sau khi trả lời Q-44 |
| P04 | UC-007, UC-009 | Không có luồng khi thu tiền thất bại | Thêm luồng sau khi trả lời Q-23 |

## Vấn đề còn mở

- F6 SS-01: chữ ký IF-01 dùng kiểu giá trị Money, CardReference, HoldReference của PKG-15, làm PKG-18 (layer dưới) phụ thuộc PKG-15 (layer trên). Phương án khác là đặt các kiểu giá trị này trong PKG-18; chưa sửa P10.
- Operation linkCard (UC-002) và onStaffCardOperation (UC-014) có trong P10 nhưng không thiết kế vì các use case này chưa có P07 (Target 2).
- Timeout của mọi operation chờ Q-41 (chế độ NGHIEM_NGAT không cho giả định).
