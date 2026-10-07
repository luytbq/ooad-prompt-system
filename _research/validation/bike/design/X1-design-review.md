# X1 - Review thiết kế - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | X1 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P12-class-design/PKG-09-15-16-rental-core.md 1.0; P13-data-model.md 1.0; P11b 1.0; P10 1.0; P09 1.0; P07 (4 UC); P06 1.0 |
| Phạm vi | PKG-09, PKG-15, PKG-16 trong P12 và TBL-01 đến TBL-08 trong P13 |

Placeholder: PHAM_VI_REVIEW = "PKG-09, PKG-15, PKG-16 trong P12 và các bảng liên quan trong P13; P11b SS-01, SS-02 ở phần chữ ký interface"; NHOM_TIEU_CHI = Không có; THIET_KE_DOC_LAP = Không có; MA_RV_BAT_DAU = Không có; YEU_CAU_BO_SUNG = Không có.

## F1. Phạm vi và phương pháp

| Hạng mục | Nội dung |
|---|---|
| Artifact | P12 (PKG-09, PKG-15, PKG-16) 1.0; P13 1.0; P11b 1.0 (chữ ký IF-01, IF-02, IF-03); P10 1.0; P09 1.0 |
| Phần tử | 3 package; 20 lớp và value object, 7 enumeration, 8 interface kho dữ liệu, 6 interface ngoài (tham chiếu); 8 bảng |
| Nhóm tiêu chí | MOD, CPL, COH, SOLID, GRASP, PRN, PKP, SML, CNS, DAT |
| Không review được | Lớp bên trong SS-01, SS-02 (không có đặc tả method); PKG-05, PKG-11, PKG-17 đến PKG-23 (chưa có P12); DDL chưa chạy trên PostgreSQL |
| Phép thử continuity | (1) Đổi mức cước theo bảng giá cước (REQ-55, Q-15): sửa DC-FareCalculator và hằng của nó, thêm nguồn dữ liệu bảng giá --> 1 lớp + P13 thêm bảng. (2) Đổi ngân hàng đối tác: chỉ SS-01 bên trong --> 0 lớp ngoài PKG-18, nhưng Money, CardReference, HoldReference nằm ở PKG-15 (RV-05). (3) Đổi thời hạn chờ 60 giây: DC-RentalRequest.REMOVAL_TIMEOUT --> 1 lớp |

## F2. Bảng phát hiện

| RV | Nguyên lý / tiêu chí vi phạm | Phần tử | Bằng chứng | Mức độ | Đề xuất sửa | Bước cần sửa | Nhóm | Độ tin cậy | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| RV-01 | CNS Thiết kế không hiện thực hậu điều kiện tối thiểu; MOD protection | DC-RentBikeService.requestRental; DC-ReturnBikeService.handleBikeReturned; DC-RecordLostBikeService.handleTripDurationReached | P12 F3 requestRental: bước 6 placeHold rồi bước 7 mới ghi PaymentHold, bước 8 sendUnlockCommand; P12 F1 "Lời gọi IF-01, IF-02 nằm ngoài giao dịch". Nếu bước 7 hoặc 8 lỗi, khoản tạm giữ trên thẻ không có bản ghi và không bị huỷ. P04 UC-005 hậu điều kiện tối thiểu: "không còn khoản tạm giữ nào của lượt thuê này". Tương tự handleBikeReturned bước 2 ghi Trip COMPLETED trước khi capture; capture lỗi thì Trip đã kết thúc mà tiền chưa thu, không trạng thái nào cho biết cần thu lại | Nghiêm trọng | Ghi RentalRequest ở trạng thái mới PENDING_HOLD trước khi gọi placeHold (requestId đã có), cập nhật sau khi cổng trả kết quả; thêm bước bù trừ cancelHold khi bước sau lỗi; với trả xe, thêm trạng thái Trip hoặc PaymentHold "CAPTURE_PENDING" để tác vụ đối soát thu lại. Cần câu trả lời Q-23, Q-42, Q-44 | P04 (luồng lỗi), P12 | CNS | Chắc chắn | Mở |
| RV-02 | DAT mất toàn vẹn khi xử lý đồng thời; SML Temporal coupling ẩn | DC-RentBikeService.handleBikeRemoved, handleRemovalTimeout; TBL-07 | P12 F3: handleBikeRemoved "requests.findAwaitingByDock ... request.complete()"; handleRemovalTimeout "Không còn AwaitingRemoval thì kết thúc ... cancelHold ... request.expire()". Hai sự kiện tới gần mốc 60 giây trên hai tiến trình (P09: máy chủ nhân bản) cùng đọc AWAITING_REMOVAL; kết quả có thể là chuyến bắt đầu và khoản tạm giữ bị huỷ. P13 TBL-07 không có cột phiên bản | Nghiêm trọng | Thêm cột version (optimistic lock) hoặc cập nhật có điều kiện "UPDATE rental_request SET status = ... WHERE id = ? AND status = 'AWAITING_REMOVAL'" và chỉ tiếp tục khi 1 dòng bị cập nhật; gọi cancelHold chỉ sau khi chuyển EXPIRED thành công | P12, P13 | DAT | Chắc chắn | Mở |
| RV-03 | CNS BR-02 không được bảo đảm trong khoảng chờ; DAT | DC-RentBikeService.requestRental; ux_rental_request_rider_awaiting | P12 F3 bước 2 kiểm tra trips.existsInProgressByRider nhưng không kiểm tra lượt thuê đang chờ; P13 thêm ux_rental_request_rider_awaiting, vi phạm được phát hiện ở bước 7 (sau khi đã placeHold ở bước 6) | Cao | Kiểm tra lượt AWAITING_REMOVAL của tài khoản ở bước 2 (thêm IF-14.existsAwaitingByRider) và ghi RentalRequest trước placeHold theo RV-01 để index chặn sớm | P12 | CNS | Chắc chắn | Mở |
| RV-04 | GRASP Protected Variations; SOLID OCP | DC-FareCalculator (FREE_PERIOD, BLOCK, BLOCK_PRICE) | P12 F7: ba hằng "{readOnly}, Classifier" theo BR-07; P02 UC-023 "Quản lý bảng giá cước"; GL-01 "Tập mức giá do quản trị viên quản lý, dùng để tính cước" | Cao (nâng một mức: REQ-55 cho biết giá dễ đổi) | Khi Q-15 trả lời Có: đổi hằng thành tham số của một đối tượng FarePolicy nạp từ bảng giá cước, FareCalculator.calculate(duration, policy); thêm bảng fare_policy ở P13. Khi Q-15 trả lời Không: chấp nhận có lý do | P12, P13 | GRASP | Cần xác nhận (Q-15) | Mở |
| RV-05 | PKP phụ thuộc ngược layer | PKG-18, PKG-19 --> PKG-15, PKG-16 | P11b F3: "placeHold(cardRef: CardReference, amount: Money, requestId: UUID)"; P12 F1: DC-Money, DC-CardReference, DC-HoldReference thuộc PKG-15; P12 F9 dòng PKG-18, PKG-19 "Không: layer dưới phụ thuộc layer trên" | Cao | Move Class: chuyển Money, CardReference, HoldReference, DockEvent sang một package kiểu dữ liệu dùng chung ở layer thấp nhất (đề xuất P10 cấp PKG mới trong PKG-04), hoặc để interface IF-01, IF-02 thuộc PKG-09 (DIP: interface thuộc phía mức cao) | P10, P11b, P12 | PKP | Chắc chắn | Mở |
| RV-06 | PRN Law of Demeter; SML Message chains | DC-ReturnBikeService.handleBikeReturned; DC-RecordLostBikeService.handleTripDurationReached | P12 F3: "invoiceSender.sendInvoice(trip.getRider().getEmail(), trip.composeInvoice())"; "trip.getBike().markLost()"; "trip.getRider().lock()"; "hold = trip.getPaymentHold(); paymentGateway.capture(hold.holdReference, ...)" | Trung bình | Hide Delegate: Trip.markBikeLost(), Trip.lockRider(); ReturnBikeService nhận email qua TripInvoice (composeInvoice điền recipientEmail) | P12 | PRN | Chắc chắn | Mở |
| RV-07 | SOLID SRP; COH communicational | DC-Trip.composeInvoice | P12 F2: "Lập nội dung hoá đơn từ chuyến đã kết thúc (thành phần chờ Q-24)"; hoá đơn là định dạng trình bày cho email (P10 SS-03), khác lý do thay đổi với vòng đời chuyến | Trung bình | Extract Class: InvoiceComposer ở PKG-09 dựng TripInvoice từ Trip; Trip chỉ lộ dữ liệu cần qua operation truy vấn | P12 | SOLID | Chắc chắn | Mở |
| RV-08 | CNS Interface không có chữ ký chốt ở P11b | IF-04, IF-05, IF-06 | P12 F2 "Chữ ký tạm cho interface ngoài phạm vi P11b"; P11b phạm vi chỉ SS-01, SS-02 | Trung bình | Chạy P11b cho SS-03, SS-04 rồi chạy lại P12 PKG-09 | P11b | CNS | Chắc chắn | Mở |
| RV-09 | CNS Kiểu định danh lệch giữa artifact | IF-02 (DockId) và DC-Dock.id (UUID) | P11b F3: "sendUnlockCommand(dockId: DockId, requestId: UUID)"; P12 F7: "DC-Dock id UUID ... dùng làm DockId của IF-02 (Q-36)" | Thấp | Thống nhất: DockId là value object bọc UUID, hoặc mã thiết bị riêng của nhà cung cấp lưu thành cột dock.device_code khi Q-36 trả lời | P12, P13 | CNS | Cần xác nhận (Q-36) | Mở |
| RV-10 | CNS Multiplicity lệch P12 - P13 | R-50; TBL-07 | P12 F5 R-50 "A 0..1 - B 1"; P13 F4.2 "0..1 chỉ áp dụng cho lượt đang chờ" | Thấp | Đổi R-50 thành "A 0..* - B 1" với ràng buộc {tối đa một AWAITING_REMOVAL mỗi ụ} (đã có ở Đề xuất sửa của P13) | P12 | CNS | Chắc chắn | Mở |
| RV-11 | SML Data class; CNS thuộc tính không có operation ghi | DC-RiderAccount.outstandingFare | P12 F7 "Khoản nợ cước (phát sinh chờ Q-02)"; không operation nào trong P12 làm tăng outstandingFare; checkRentalEligibility chỉ đọc | Thấp | Giữ, ghi rõ chờ Q-02; khi có luồng 4a của UC-007 thêm RiderAccount.addOutstandingFare(amount) | P04, P12 | CNS | Chắc chắn | Chấp nhận có lý do |
| RV-12 | CPL Control coupling | DC-RentalTimerHandler.onTimerFired | P12 F2: "REMOVAL_TIMEOUT --> RentBikeService.handleRemovalTimeout; TRIP_MAX_DURATION --> RecordLostBikeService..." | Thấp | Chấp nhận: lớp là bộ chuyển (dispatcher) theo loại mốc của IF-06; nếu số loại mốc tăng, thay bằng đăng ký listener theo loại | - | CPL | Chắc chắn | Chấp nhận có lý do |
| RV-13 | DAT CHECK không phủ BR-05 | TBL-05.amount | P13 F6.1 "CHECK (amount > 0)"; BR-05 "Số tiền tạm giữ cho mỗi lần thuê xe là 200.000 đồng" | Thấp | Để CHECK (amount > 0) (BR-05 có thể đổi); ghi hằng HOLD_AMOUNT ở DC-PaymentHold (P12 Vấn đề còn mở) | P12 | DAT | Chắc chắn | Chấp nhận có lý do |

## F3. Đánh giá coupling

| Phần tử A | Phần tử B | Kênh | Mức | Bằng chứng | Chấp nhận |
|---|---|---|---|---|---|
| DC-RentBikeService | IF-01, IF-02, IF-05, IF-07, IF-08, IF-09, IF-11, IF-14 | thuộc tính | Data | R-06, R-08, R-33 đến R-38; tham số nguyên tố hoặc value object | Có |
| DC-RentBikeService | DC-RiderAccount, DC-Dock, DC-Bike, DC-PaymentHold, DC-Trip, DC-RentalRequest | biến cục bộ | Data | R-02, R-04, R-05, R-07, R-09; gọi operation, không đọc dữ liệu nội bộ | Có |
| DC-ReturnBikeService | IF-01, IF-04, IF-05, IF-08, IF-09, IF-11, DC-FareCalculator | thuộc tính | Data | R-14, R-19, R-39 đến R-41, R-53, R-54 | Có |
| DC-ReturnBikeService | DC-Trip, DC-Dock, DC-PaymentHold, DC-RiderAccount | biến cục bộ | Stamp qua chuỗi lời gọi | trip.getRider().getEmail() | Không: RV-06 |
| DC-RecordLostBikeService | IF-01, IF-07, IF-08, IF-09, IF-12 | thuộc tính | Data | R-24, R-42, R-55 đến R-57 | Có |
| DC-RecordLostBikeService | DC-Trip, DC-Bike, DC-RiderAccount, DC-PaymentHold | biến cục bộ | Data, có message chain | trip.getBike().markLost() | Không: RV-06 |
| DC-DockEventHandler | DC-RentBikeService, DC-ReturnBikeService | thuộc tính | Data | R-15, R-45 | Có |
| DC-RentalTimerHandler | DC-RentBikeService, DC-RecordLostBikeService | thuộc tính | Control (theo loại mốc) | onTimerFired rẽ nhánh theo timer.type | Có (RV-12 chấp nhận) |
| DC-Trip | DC-RiderAccount, DC-Bike, DC-Dock, DC-PaymentHold | thuộc tính | Data | R-03, R-11, R-12, R-13, R-21 | Có |
| DC-Trip | DC-FareCalculator | tham số | Data | R-48 | Có |
| DC-RentalRequest | DC-RiderAccount, DC-Dock, DC-Bike, DC-PaymentHold | thuộc tính | Data | R-49 đến R-52 | Có |
| DC-Dock | DC-Bike, DC-Station | thuộc tính | Data | R-10, R-32 | Có |
| DC-TransferOrder | DC-Station | thuộc tính | Data | R-30, R-31 | Có |
| SS-01, SS-02 (qua chữ ký IF) | DC-Money, DC-CardReference, DC-HoldReference | tham số | Data nhưng ngược layer | P11b F3 | Không: RV-05 |

## F4. Đánh giá cohesion

| Phần tử | Mức | Lý do | Chấp nhận |
|---|---|---|---|
| DC-RentBikeService | Sequential | Ba operation của cùng UC-005, đầu ra bước trước là đầu vào bước sau | Có |
| DC-ReturnBikeService | Sequential | Một operation điều phối UC-007 | Có |
| DC-RecordLostBikeService | Functional | Một trách nhiệm | Có |
| DC-DockEventHandler, DC-RentalTimerHandler | Functional | Chuyển sự kiện | Có |
| DC-RiderAccount | Functional | Điều kiện thuê và trạng thái tài khoản | Có |
| DC-Trip | Communicational | Vòng đời chuyến, tính cước qua tham số, và lập hoá đơn cùng dùng dữ liệu chuyến | Không: RV-07 |
| DC-FareCalculator | Functional | Chỉ BR-07 | Có |
| DC-PaymentHold | Functional | Vòng đời khoản tạm giữ | Có |
| DC-RentalRequest | Functional | Vòng đời lượt chờ | Có |
| DC-Station | Functional (Data class trong phạm vi) | Không có hành vi vì UC-012 chưa phân tích | Có |
| DC-Dock, DC-Bike, DC-TransferOrder | Functional | - | Có |
| DC-Money, DC-CardReference, DC-HoldReference, DC-TripInvoice, DC-RentalOutcome | Functional | Value object | Có |
| PKG-09 | CCP đạt | Cùng thay đổi khi luồng thuê trả xe đổi | Có |
| PKG-15 | CCP một phần | Chứa cả value object dùng bởi PKG-18, PKG-19 | Không: RV-05 |

## F5. Danh mục nguyên lý

| Nguyên lý | Phần tử đã xét | Kết luận |
|---|---|---|
| SRP | Mọi lớp | Vi phạm: RV-07 |
| OCP | DC-FareCalculator, DC-RentalTimerHandler | Vi phạm: RV-04; RV-12 chấp nhận |
| LSP | Không có kế thừa | Không phát hiện vi phạm |
| ISP | IF-01 (4 operation, 3 client dùng khác nhau), IF-08 | Không phát hiện vi phạm (mỗi client dùng 1-2 operation nhưng interface nhỏ) |
| DIP | Dịch vụ --> IF; IF-01, IF-02 thuộc package của subsystem | Vi phạm: RV-05 |
| Information Expert, Creator | DC-RiderAccount.checkRentalEligibility (tham số hasTripInProgress), Trip.start | Đạt; lựa chọn truyền hasTripInProgress đổi Information Expert lấy Low Coupling (P12 R-03), chấp nhận |
| Controller | Dịch vụ | Đạt |
| Pure Fabrication, Indirection | Repository, handler | Đạt |
| Protected Variations | FareCalculator | Vi phạm: RV-04 |
| Encapsulation, Law of Demeter | Getter của Trip | Vi phạm: RV-06 |
| DRY | BR-02 ở requestRental và ux_trip_rider_in_progress | Đạt (index là lưới an toàn, không phải cách viết khác của quy tắc) |
| KISS, YAGNI | RentalRequest, handler | Đạt: RentalRequest có lý do NFR-03 |
| Design smell | Toàn phạm vi | RV-06 Message chains; RV-11 Data class; RV-02 Temporal coupling ẩn |
| PKP | PKG-09, PKG-15, PKG-16, PKG-18, PKG-19 | Vi phạm: RV-05 |
| CNS | P07 - P12, P11b - P12, P12 - P13 | Vi phạm: RV-01, RV-03, RV-08, RV-09, RV-10 |
| DAT | TBL-01 đến TBL-08 | Vi phạm: RV-02; RV-13 chấp nhận |
| MOD | PKG-09, SS-01, SS-02 | Vi phạm protection: RV-01 |

## F6. Phụ thuộc package

### F6.1

| PKG nguồn | PKG đích | Quan hệ lớp | Hợp lệ theo layer |
|---|---|---|---|
| PKG-09 | PKG-15 | R-02, R-07, R-09, R-18, R-20, R-22, R-25, R-26, R-33, R-34, R-36, R-37, R-39, R-42, R-53 đến R-56 | Có |
| PKG-09 | PKG-16 | R-04, R-05, R-16, R-17, R-23, R-35, R-40, R-57 | Có |
| PKG-09 | PKG-18, PKG-19, PKG-20, PKG-21 | R-06, R-08, R-14, R-19, R-24, R-38, R-41, R-43, R-44 | Có (nới lỏng) |
| PKG-15 | PKG-16 | R-11, R-12, R-21, R-50, R-51 | Có |
| PKG-18, PKG-19 | PKG-15, PKG-16 | Chữ ký IF-01, IF-02, IF-03 | Không (RV-05) |

### F6.2 Vòng phụ thuộc

PKG-09 --> PKG-19 (IF-02) và PKG-19 --> PKG-09 không có (IF-03 do PKG-19 sở hữu). PKG-15 --> PKG-18 không có. Không có vòng. PKG-18 --> PKG-15 --> (không tới PKG-18): không vòng, nhưng ngược layer.

### F6.3 Chỉ số

| PKG | Ca | Ce | I | A | D | Nhận xét |
|---|---|---|---|---|---|---|
| PKG-09 | 2 (endpoint PKG-22; SS-02, SS-04 gọi qua IF) | 18 | 0,90 | 0 | 0,10 | Không ổn định, cụ thể: phù hợp |
| PKG-15 | 8 | 3 | 0,27 | 4/18 = 0,22 | 0,51 | Ổn định nhưng cụ thể; do value object dùng chung (RV-05) |
| PKG-16 | 8 | 0 | 0 | 4/10 = 0,40 | 0,60 | Ổn định, cụ thể: entity miền, chấp nhận |

## F7. Tổng hợp

| Mức độ | Số phát hiện | Mã RV |
|---|---|---|
| Nghiêm trọng | 2 | RV-01, RV-02 |
| Cao | 3 | RV-03, RV-04, RV-05 |
| Trung bình | 3 | RV-06, RV-07, RV-08 |
| Thấp | 5 | RV-09 đến RV-13 |

Thứ tự chạy lại: 1. P04: RV-01 (luồng lỗi cổng thanh toán, lệnh mở khoá), RV-11. 2. P10: RV-05. 3. P11b: RV-05, RV-08. 4. P12: RV-01, RV-02, RV-03, RV-04, RV-06, RV-07, RV-09, RV-10. 5. P13: RV-02, RV-04.

## Câu hỏi mở

Không có câu hỏi mới. Liên quan: Q-15, Q-23, Q-36, Q-42, Q-44.

## Đề xuất sửa artifact trước

Xem bảng phát hiện F2.

## Vấn đề còn mở

- Target 2: F3 gộp nhiều cặp cùng phần tử A và cùng kênh vào một dòng; tách từng cặp sẽ có khoảng 55 dòng.
- DDL của P13 chưa được chạy trên PostgreSQL; review DAT dựa trên văn bản.
