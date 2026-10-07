# P07 - Phân tích use case UC-009 Ghi nhận xe thất lạc - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-009-record-lost-bike.md 1.0; _BR-register.md; P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07 UC-005, UC-007 1.0 (sổ đăng ký AC) |
| Phạm vi | UC-009 |

Placeholder: UC_ID = "UC-009 Ghi nhận xe thất lạc"; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có.

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-009 Ghi nhận xe thất lạc (Record Lost Bike) |
| Tác nhân chính | ACT-09 Bộ định thời (Thời gian) |
| Tác nhân phụ | ACT-07 Cổng thanh toán (Hệ thống ngoài) |
| Include, Được include bởi, Extend, Được extend bởi | Không có |
| File P07 đã có được dùng làm sổ đăng ký AC | UC-005, UC-007: AC-B-RentBikeForm, AC-B-ReturnBikeForm, AC-B-PaymentGateway, AC-B-DockDevice, AC-C-RentBikeController, AC-C-ReturnBikeController, AC-E-RiderAccount, AC-E-Trip, AC-E-Dock, AC-E-Bike, AC-E-PaymentHold |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Hệ thống | Tới thời điểm một chuyến đi kéo dài quá 24 giờ (BR-09). | Bộ định thời báo một chuyến đi đã tới mốc; chuyến đi xác nhận mình còn đang diễn ra và thời lượng tính từ thời điểm bắt đầu đã quá 24 giờ. | BR-09, GL-04, GL-26 |
| 2 | Hệ thống | Đánh dấu xe của chuyến đi là thất lạc. | Hệ thống lấy xe của chuyến và ghi xe ở tình trạng thất lạc; "thất lạc" có phải một giá trị trạng thái xe chờ Q-27. Chuyến có kết thúc hay không chờ Q-04. | GL-26, GL-22 |
| 3 | Hệ thống | Yêu cầu Cổng thanh toán thu toàn bộ số tiền tạm giữ của chuyến đi (BR-10). | Hệ thống lấy khoản tạm giữ của chuyến, gửi yêu cầu thu toàn bộ số tiền, ghi số tiền đã thu vào khoản tạm giữ. Lỗi thu chờ Q-23. | BR-10, GL-08 |
| 4 | Hệ thống | Khoá tài khoản của người thuê xe (BR-10). | Hệ thống lấy tài khoản của chuyến và chuyển tài khoản sang trạng thái bị khoá. | BR-10, GL-15 |

## F3. Tìm lớp phân tích

### F3.1 Boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-09 Bộ định thời | Thời gian | Không có | - | - | A3: tác nhân thời gian chỉ kích hoạt use case; control nhận sự kiện là AC-C-RecordLostBikeController |
| ACT-07 Cổng thanh toán | Hệ thống ngoài | PaymentGateway | Giao diện hệ thống | Tái dùng AC-B-PaymentGateway (UC-005) | Cùng hệ thống ngoài |

### F3.2 Lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Chuyến đi | Bước 1 đến 4 | Entity (AC-E-Trip) | Tái dùng |
| 2 | 24 giờ | BR-09 | Loại - tham số của quy tắc BR-09 | Hằng số |
| 3 | Xe, xe thất lạc | Bước 2 | Entity (AC-E-Bike) | Tái dùng; "thất lạc" là trạng thái (GL-26, Q-27) |
| 4 | Cổng thanh toán | Bước 3 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-07 |
| 5 | Số tiền tạm giữ | Bước 3 | Entity (AC-E-PaymentHold) | Tái dùng; "số tiền tạm giữ" là đồng nghĩa không dùng của GL-08 |
| 6 | Tài khoản, tài khoản bị khoá | Bước 4 | Entity (AC-E-RiderAccount) | Tái dùng; "bị khoá" là trạng thái (GL-15) |
| 7 | Người thuê xe | Bước 4 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01 |
| 8 | Hệ thống | Mọi bước | Loại - mơ hồ | - |

### F3.3 Control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do |
|---|---|---|---|
| RecordLostBikeController | UC-009 | Mới (AC-C-RecordLostBikeController) | Một control cho mỗi use case; nhận sự kiện từ ACT-09 |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestCapture: gửi yêu cầu thu tiền từ khoản tạm giữ | - | 3 | Giao diện hệ thống | Tái dùng từ UC-007 | - |
| AC-C-RecordLostBikeController | control | RecordLostBikeController | // notifyTripDurationReached: điều phối xử lý chuyến quá 24 giờ | - | 1 đến 4 | - | Mới | - |
| AC-E-Trip | entity | Trip | // checkExceedsMaxDuration: kiểm tra BR-09 | startTime: Giờ | 1 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-04 |
| AC-E-Bike | entity | Bike | // markLost: ghi xe thất lạc | status: Trạng thái | 2 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-25, GL-26 |
| AC-E-PaymentHold | entity | PaymentHold | // recordCapture: ghi số tiền đã thu | capturedAmount: Số tiền | 3 | - | Tái dùng từ UC-007 | GL-08 |
| AC-E-RiderAccount | entity | RiderAccount | // lock: khoá tài khoản theo BR-10 | accountStatus: Trạng thái | 4 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-15 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // notifyTripDurationReached | AC-C-RecordLostBikeController | Controller | - |
| 1 | // checkExceedsMaxDuration | AC-E-Trip | Information Expert | - |
| 2 | // markLost | AC-E-Bike | Information Expert | - |
| 3 | // requestCapture | AC-B-PaymentGateway | Giao tiếp tác nhân | Dùng lại trách nhiệm của UC-007 với số tiền bằng toàn bộ tạm giữ, không tạo trách nhiệm mới |
| 3 | // recordCapture | AC-E-PaymentHold | Information Expert | - |
| 4 | // lock | AC-E-RiderAccount | Information Expert | - |

## F5. Sequence diagram phân tích

### SD1 - Luồng chính

File diagrams/P07-sequence-UC-009.drawio.

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| A-09 | Actor | Bộ định thời | - | - | ACT-09 |
| L-LBC | Lifeline | :RecordLostBikeController | «control» | - | AC-C-RecordLostBikeController |
| L-TR | Lifeline | :Trip | «entity» | - | AC-E-Trip |
| L-BK | Lifeline | :Bike | «entity» | - | AC-E-Bike |
| L-PH | Lifeline | :PaymentHold | «entity» | - | AC-E-PaymentHold |
| L-RA | Lifeline | :RiderAccount | «entity» | - | AC-E-RiderAccount |
| L-PG | Lifeline | :PaymentGateway | «boundary» | - | AC-B-PaymentGateway |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |

| STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | A-09 | L-LBC | // notifyTripDurationReached (chuyến đi) | Bất đồng bộ | - | 1 |
| 1.1 | L-LBC | L-TR | // checkExceedsMaxDuration (BR-09) | Đồng bộ | - | 1 |
| 1.1 (trả về) | L-TR | L-LBC | quá 24 giờ, xe, khoản tạm giữ, tài khoản của chuyến | Trả về | - | 1 |
| 1.2 | L-LBC | L-BK | // markLost (Q-27) | Đồng bộ | - | 2 |
| 1.3 | L-LBC | L-PG | // requestCapture (toàn bộ số tiền tạm giữ, khoản tạm giữ) | Đồng bộ | - | 3 |
| 1.3.1 | L-PG | A-07 | // captureHold | Đồng bộ | - | 3 |
| 1.4 | L-LBC | L-PH | // recordCapture (toàn bộ số tiền tạm giữ) | Đồng bộ | - | 3 |
| 1.5 | L-LBC | L-RA | // lock (BR-10) | Đồng bộ | - | 4 |

## F6. Quy tắc tương tác

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Actor gửi message tới control (bảng F6: Actor --> Control "Không") | 1: // notifyTripDurationReached (ACT-09 --> RecordLostBikeController), link K01 | Không sửa: A3 cho phép tác nhân thời gian không có boundary và yêu cầu ghi control nhận sự kiện; hai quy tắc mâu thuẫn, chọn A3 (xem Vấn đề còn mở) |

## F7. Communication diagram

File diagrams/P07-communication-UC-009.drawio.

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| A-09 | Actor | Bộ định thời | - | - | - |
| L-LBC | Object | :RecordLostBikeController | «control» | - | - |
| L-TR | Object | :Trip | «entity» | - | - |
| L-BK | Object | :Bike | «entity» | - | - |
| L-PH | Object | :PaymentHold | «entity» | - | - |
| L-RA | Object | :RiderAccount | «entity» | - | - |
| L-PG | Object | :PaymentGateway | «boundary» | - | - |
| A-07 | Actor | Cổng thanh toán | - | - | - |

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message |
|---|---|---|---|---|---|
| K01 | A-09 | L-LBC | Link | 1: // notifyTripDurationReached (-->) | Nguồn-->Đích |
| K02 | L-LBC | L-TR | Link | 1.1: // checkExceedsMaxDuration (-->) | Nguồn-->Đích |
| K03 | L-LBC | L-BK | Link | 1.2: // markLost (-->) | Nguồn-->Đích |
| K04 | L-LBC | L-PG | Link | 1.3: // requestCapture (-->) | Nguồn-->Đích |
| K05 | L-PG | A-07 | Link | 1.3.1: // captureHold (-->) | Nguồn-->Đích |
| K06 | L-LBC | L-PH | Link | 1.4: // recordCapture (-->) | Nguồn-->Đích |
| K07 | L-LBC | L-RA | Link | 1.5: // lock (-->) | Nguồn-->Đích |

## F8. VOPC

File diagrams/P07-class-UC-009.drawio.

| ID (mã AC) | Loại | Nhãn | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-PaymentGateway | Class | PaymentGateway | boundary | - | - | // requestCapture |
| AC-C-RecordLostBikeController | Class | RecordLostBikeController | control | - | - | // notifyTripDurationReached |
| AC-E-Trip | Class | Trip | entity | - | startTime: Giờ | // checkExceedsMaxDuration |
| AC-E-Bike | Class | Bike | entity | - | status: Trạng thái | // markLost |
| AC-E-PaymentHold | Class | PaymentHold | entity | - | capturedAmount: Số tiền | // recordCapture |
| AC-E-RiderAccount | Class | RiderAccount | entity | - | accountStatus: Trạng thái | // lock |

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC009-01 | AC-C-RecordLostBikeController | AC-E-Trip | Association | - | - | K02; tạm thời |
| R-UC009-02 | AC-C-RecordLostBikeController | AC-E-Bike | Association | - | - | K03; tạm thời |
| R-UC009-03 | AC-C-RecordLostBikeController | AC-B-PaymentGateway | Association | - | - | K04; tạm thời |
| R-UC009-04 | AC-C-RecordLostBikeController | AC-E-PaymentHold | Association | - | - | K06; tạm thời |
| R-UC009-05 | AC-C-RecordLostBikeController | AC-E-RiderAccount | Association | - | - | K07; tạm thời |
| R-UC009-06 | AC-E-Trip | AC-E-Bike | Association | A 0..* - B 1 | - | Trả về của 1.1; bước 2 "xe của chuyến đi" |
| R-UC009-07 | AC-E-Trip | AC-E-PaymentHold | Association | A 0..1 - B 1 | - | Bước 3 "tạm giữ của chuyến đi" |
| R-UC009-08 | AC-E-Trip | AC-E-RiderAccount | Association | A 0..* - B 1 | - | Bước 4, BR-10 "tài khoản của người thuê xe" |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1, 1.1 | AC-C-RecordLostBikeController, AC-E-Trip |
| 2 | 1.2 | AC-E-Bike |
| 3 | 1.3, 1.3.1, 1.4 | AC-B-PaymentGateway, AC-E-PaymentHold |
| 4 | 1.5 | AC-E-RiderAccount |

## Câu hỏi mở

Không có câu hỏi mới. Liên quan: Q-03, Q-04, Q-23, Q-27.

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 7 không đạt: message 1 từ tác nhân thời gian tới control vi phạm bảng F6 nhưng đúng theo A3. Đã chọn A3 theo C9 (quy tắc riêng của bước ngang nhau, chọn quy tắc cụ thể hơn).
- Số lớp của UC-009 là 6, trong khoảng 4-12.
- AC-C-RecordLostBikeController có 1 trách nhiệm (dưới mức 2-10 của F3.4) vì cả use case là một chuỗi phản ứng với một sự kiện.
