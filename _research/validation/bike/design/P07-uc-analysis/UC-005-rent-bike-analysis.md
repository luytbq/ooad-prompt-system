# P07 - Phân tích use case UC-005 Thuê xe - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-005-rent-bike.md 1.0; P04-uc-specs/_BR-register.md; P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P02-usecases.md 1.0 (đối chiếu) |
| Phạm vi | UC-005 |

Placeholder: UC_ID = "UC-005 Thuê xe"; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có.

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-005 Thuê xe (Rent Bike) |
| Tác nhân chính | ACT-01 Người thuê xe (Người) |
| Tác nhân phụ | ACT-07 Cổng thanh toán (Hệ thống ngoài); ACT-08 Ụ khoá (Thiết bị) |
| Include | Không có |
| Được include bởi | Không có |
| Extend | Không có |
| Được extend bởi | Không có |
| File P07 đã có được dùng làm sổ đăng ký AC | Không có (UC-005 là lần chạy P07 đầu tiên; sổ rỗng) |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Người thuê xe | Quét mã QR dán trên ụ khoá để yêu cầu thuê xe. | Không đổi | GL-11, REQ-07 |
| 2 | Hệ thống | Kiểm tra tài khoản đã liên kết thẻ thanh toán (BR-01), không có chuyến đi đang diễn ra (BR-02) và không nợ cước (BR-03). | Hệ thống lấy tài khoản của người thuê xe đã xác thực. Tài khoản kiểm tra mình có mã tham chiếu thẻ, có khoản nợ cước hay không, và hỏi các chuyến đi của mình xem có chuyến nào đang diễn ra. Kết quả là đủ điều kiện hoặc lý do không đủ. | BR-01, BR-02, BR-03, GL-12, GL-14, GL-04 |
| 2a, 2b, 2c | Hệ thống | Từ chối yêu cầu thuê xe (Q-22). | Hệ thống kết thúc yêu cầu, không tạo khoản tạm giữ, không gửi lệnh mở khoá, báo từ chối cho người thuê xe; nội dung báo chờ Q-22. | BR-01, BR-02, BR-03 |
| 3 | Hệ thống | Kiểm tra xe tại ụ khoá được phép cho thuê (BR-04). | Hệ thống tìm ụ khoá theo mã QR và lấy xe ụ đang giữ. Xe kiểm tra trạng thái của mình khác "Chờ kiểm tra". Trường hợp ụ không giữ xe chờ Q-20. | BR-04, GL-22, GL-23, GL-11 |
| 3a | Hệ thống | Từ chối yêu cầu thuê xe (Q-22). | Như 2a. | BR-04 |
| 4 | Hệ thống | Yêu cầu Cổng thanh toán tạm giữ tiền trên thẻ đã liên kết (BR-05). | Hệ thống gửi tới Cổng thanh toán yêu cầu tạm giữ 200.000 đồng kèm mã tham chiếu thẻ lấy từ tài khoản. | BR-05, GL-08, GL-12, NFR-06 |
| 5 | Cổng thanh toán | Trả về kết quả tạm giữ. | Khi thành công, hệ thống ghi nhận một khoản tạm giữ gồm số tiền và mã do cổng cấp để huỷ hoặc thu về sau (Q-30). | GL-08 |
| 5a | Hệ thống | Từ chối yêu cầu thuê xe (Q-08). | Như 2a; không có khoản tạm giữ nào được ghi nhận. | Q-08 |
| 6 | Hệ thống | Gửi lệnh mở khoá tới ụ khoá. | Hệ thống gửi lệnh mở khoá tới ụ khoá đã tìm ở bước 3 và bắt đầu đếm thời hạn chờ rút xe 60 giây (mốc tính chờ Q-10). | GL-10, BR-06, NFR-02, NFR-07 |
| 6a | - | Hết thời hạn chờ rút xe mà ụ khoá chưa báo xe được rút ra (BR-06). | Hệ thống phát hiện thời hạn chờ của lượt thuê đã hết mà chưa nhận báo rút xe. | BR-06 |
| 6a1 | Hệ thống | Gửi lệnh khoá lại ụ khoá. | Hệ thống gửi lệnh khoá lại tới cùng ụ khoá. | BR-06, NFR-07 |
| 6a2 | Hệ thống | Yêu cầu Cổng thanh toán huỷ lệnh tạm giữ tiền. | Hệ thống gửi yêu cầu huỷ khoản tạm giữ theo mã đã ghi ở bước 5 và ghi khoản tạm giữ ở trạng thái đã huỷ. | BR-06, GL-08 |
| 7 | Ụ khoá | Báo xe đã được rút ra. | Không đổi | REQ-13 |
| 8 | Hệ thống | Bắt đầu chuyến đi. | Hệ thống dừng đếm thời hạn chờ, ghi nhận ụ khoá không còn giữ xe, tạo chuyến đi gắn tài khoản, xe, ụ khoá lấy xe và khoản tạm giữ, trạng thái đang diễn ra, thời điểm bắt đầu là lúc nhận báo rút xe. | GL-04, GL-24, REQ-13 |

## F3. Tìm lớp phân tích

### F3.1 Boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-01 Người thuê xe | Người | RentBikeForm | Giao diện người dùng | Mới (AC-B-RentBikeForm) | Cặp ACT-01 - UC-005; hậu tố Form vì HAU_TO_TEN_LOP = Mặc định |
| ACT-07 Cổng thanh toán | Hệ thống ngoài | PaymentGateway | Giao diện hệ thống | Mới (AC-B-PaymentGateway) | Tên theo hệ thống ngoài, không hậu tố |
| ACT-08 Ụ khoá | Thiết bị | DockDevice | Giao diện thiết bị | Mới (AC-B-DockDevice) | Tên theo thiết bị là "Dock", trùng tên entity Dock (GL-23) cần cho dữ liệu ụ; thêm "Device" để phân biệt (xem Vấn đề còn mở) |

### F3.2 Lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Người thuê xe | Bước 1, tác nhân chính | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01 |
| 2 | Mã QR (dán trên ụ khoá) | Bước 1 | Loại - thuộc tính của Dock | GL-11: mã gắn với một ụ khoá |
| 3 | Ụ khoá | Bước 1, 3, 6, 7 | Entity (AC-E-Dock) | Hệ thống phải biết ụ nào giữ xe nào, mã QR của ụ, qua nhiều lần thuê (GL-23, GL-24); đồng thời là tác nhân ACT-08 (boundary DockDevice) |
| 4 | Yêu cầu thuê xe | Bước 1, 2a | Loại - thao tác hoặc sự kiện | Hành động quét mã |
| 5 | Tài khoản | Bước 2 | Entity (AC-E-RiderAccount) | Hồ sơ của người thuê xe, giữ mã tham chiếu thẻ, nợ cước, lịch sử chuyến; biểu diễn thông tin về tác nhân, không phải tác nhân |
| 6 | Thẻ thanh toán | Bước 2, 4 | Loại - thuộc tính của RiderAccount | Hệ thống chỉ lưu mã tham chiếu thẻ (GL-12, NFR-04); giữ cardReference |
| 7 | Chuyến đi | Bước 2, 8 | Entity (AC-E-Trip) | GL-04; tồn tại qua nhiều use case (UC-007, UC-009) |
| 8 | Nợ cước | Bước 2 | Loại - thuộc tính của RiderAccount | GL-14; cách phát sinh chờ Q-02 |
| 9 | Xe | Bước 3 | Entity (AC-E-Bike) | GL-25; có trạng thái quyết định cho thuê (GL-22) |
| 10 | Trạng thái "Chờ kiểm tra" | Bước 3a | Loại - thuộc tính của Bike | GL-22 |
| 11 | Cổng thanh toán | Bước 4, 5 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-07 |
| 12 | Tiền tạm giữ, khoản tạm giữ, lệnh tạm giữ tiền | Bước 4, 6a2 | Entity (AC-E-PaymentHold) | GL-08; phải lưu để thu (UC-007, UC-009) hoặc huỷ (6a2). "Lệnh tạm giữ" là từ đồng nghĩa không dùng của GL-08 |
| 13 | 200.000 đồng | BR-05 | Loại - tham số của quy tắc BR-05 | Hằng số của quy tắc |
| 14 | Kết quả tạm giữ | Bước 5 | Loại - thao tác hoặc sự kiện | Phản hồi của cổng, không lưu riêng |
| 15 | Lệnh mở khoá | Bước 6 | Loại - thao tác hoặc sự kiện | GL-10: thông điệp gửi tới ụ |
| 16 | Thời hạn chờ rút xe, 60 giây | Bước 6a, BR-06 | Loại - tham số của quy tắc BR-06 | Hằng số của quy tắc |
| 17 | Lệnh khoá lại | Bước 6a1 | Loại - thao tác hoặc sự kiện | Thông điệp gửi tới ụ |
| 18 | Hệ thống | Mọi bước | Loại - mơ hồ | Chủ thể chung |
| 19 | Trạm | Sự kiện kích hoạt EV-04 "tại trạm" | Loại - là tác nhân hoặc ngoài phạm vi | Trạm là khái niệm của hệ thống (GL-19) nhưng không tham gia hành vi của UC-005; bảng kết luận không có giá trị phù hợp hơn (xem Vấn đề còn mở) |
| 20 | Thời điểm bắt đầu | Bước 8 (bổ sung) | Loại - thuộc tính của Trip | Cần cho tính cước ở UC-007 (BR-07) |

### F3.3 Control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do |
|---|---|---|---|
| RentBikeController | UC-005 | Mới (AC-C-RentBikeController) | Một control cho mỗi use case; điều phối kiểm tra, tạm giữ, mở khoá, chờ rút xe |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-RentBikeForm | boundary | RentBikeForm | // scanDockQrCode: nhận mã QR người thuê xe quét<br>// showRentalRejected: báo từ chối thuê xe | dockQrCode | 1, 2a, 2b, 2c, 3a, 5a | Giao diện người dùng | Mới | - |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestHold: gửi yêu cầu tạm giữ tiền tới cổng thanh toán<br>// requestCancelHold: gửi yêu cầu huỷ khoản tạm giữ | - | 4, 5, 6a2 | Giao diện hệ thống | Mới | - |
| AC-B-DockDevice | boundary | DockDevice | // sendUnlockCommand: gửi lệnh mở khoá tới ụ<br>// sendLockCommand: gửi lệnh khoá lại ụ<br>// reportBikeRemoved: nhận báo xe được rút ra | - | 6, 6a1, 7 | Giao diện thiết bị | Mới | GL-23 |
| AC-C-RentBikeController | control | RentBikeController | // requestRental: điều phối kiểm tra điều kiện, tạm giữ, mở khoá<br>// rejectRental: kết thúc yêu cầu không thành công<br>// startRemovalWait: bắt đầu đếm thời hạn chờ rút xe<br>// handleBikeRemoved: điều phối bắt đầu chuyến khi xe được rút<br>// handleRemovalTimeout: điều phối khoá lại ụ và huỷ tạm giữ khi hết thời hạn | - | 2 đến 8, 6a | - | Mới | - |
| AC-E-RiderAccount | entity | RiderAccount | // checkRentalEligibility: kiểm tra BR-01, BR-02, BR-03 trên dữ liệu của tài khoản | cardReference: Văn bản<br>outstandingFare: Số tiền | 2 | - | Mới | GL-12, GL-14 |
| AC-E-Trip | entity | Trip | // isOngoing: cho biết chuyến có đang diễn ra<br>// startTrip: khởi tạo chuyến đang diễn ra | startTime: Giờ<br>status: Trạng thái | 2, 8 | - | Mới | GL-04 |
| AC-E-Dock | entity | Dock | // findDockByQrCode: xác định ụ theo mã QR<br>// releaseBike: ghi nhận ụ không còn giữ xe | qrCode: Văn bản | 3, 8 | - | Mới | GL-23, GL-11 |
| AC-E-Bike | entity | Bike | // checkRentable: kiểm tra BR-04 trên trạng thái xe | status: Trạng thái | 3 | - | Mới | GL-25, GL-22 |
| AC-E-PaymentHold | entity | PaymentHold | // recordHold: ghi nhận khoản tạm giữ thành công<br>// markCancelled: ghi khoản tạm giữ đã huỷ | holdReference: Văn bản<br>amount: Số tiền<br>status: Trạng thái | 5, 6a2 | - | Mới | GL-08 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // scanDockQrCode | AC-B-RentBikeForm | Giao tiếp tác nhân | - |
| 2 | // requestRental | AC-C-RentBikeController | Controller | - |
| 2 | // checkRentalEligibility | AC-E-RiderAccount | Information Expert | BR-02 cần dữ liệu chuyến đi. Chọn giao cho RiderAccount và để nó hỏi Trip qua quan hệ R-UC005-03, vì tài khoản giữ hai trong ba điều kiện; giao cho control sẽ làm control giữ quy tắc thuộc dữ liệu entity |
| 2 | // isOngoing | AC-E-Trip | Information Expert | - |
| 2a, 2b, 2c, 3a, 5a | // rejectRental | AC-C-RentBikeController | Controller | - |
| 2a, 2b, 2c, 3a, 5a | // showRentalRejected | AC-B-RentBikeForm | Giao tiếp tác nhân | - |
| 3 | // findDockByQrCode | AC-E-Dock | Information Expert | - |
| 3 | // checkRentable | AC-E-Bike | Information Expert | - |
| 4 | // requestHold | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 5 | // recordHold | AC-E-PaymentHold | Creator | Control tạo vì dữ liệu khởi tạo (mã khoản tạm giữ) chỉ có ở control sau bước 5; không entity nào đang chứa khoản tạm giữ lúc này (Trip chưa tồn tại) |
| 6 | // sendUnlockCommand | AC-B-DockDevice | Giao tiếp tác nhân | - |
| 6 | // startRemovalWait | AC-C-RentBikeController | Controller | Thời hạn chờ gắn với một lượt thuê chưa thành chuyến, không entity nào giữ |
| 6a | // handleRemovalTimeout | AC-C-RentBikeController | Controller | - |
| 6a1 | // sendLockCommand | AC-B-DockDevice | Giao tiếp tác nhân | - |
| 6a2 | // requestCancelHold | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 6a2 | // markCancelled | AC-E-PaymentHold | Information Expert | - |
| 7 | // reportBikeRemoved | AC-B-DockDevice | Giao tiếp tác nhân | - |
| 7 | // handleBikeRemoved | AC-C-RentBikeController | Controller | - |
| 8 | // releaseBike | AC-E-Dock | Information Expert | - |
| 8 | // startTrip | AC-E-Trip | Creator | Dữ liệu khởi tạo nằm ở bốn lớp (RiderAccount, Bike, Dock, PaymentHold); giao cho control tạo để RiderAccount không phải biết Dock, PaymentHold |

## F5. Sequence diagram phân tích

### SD1 - Luồng chính và 2a, 2b, 2c, 3a, 5a

File diagrams/P07-sequence-UC-005.drawio, trang 1. Ba luồng từ chối dùng toán tử break (UML 2.5.1): khi guard đúng thì kết thúc tương tác, không quay lại luồng chính.

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| A-01 | Actor | Người thuê xe | - | - | ACT-01 |
| L-RBF | Lifeline | :RentBikeForm | «boundary» | - | AC-B-RentBikeForm |
| L-RBC | Lifeline | :RentBikeController | «control» | - | AC-C-RentBikeController |
| L-RA | Lifeline | :RiderAccount | «entity» | - | AC-E-RiderAccount |
| L-TO | Lifeline | ongoing:Trip | «entity» | - | AC-E-Trip, chuyến đang diễn ra (nếu có) của tài khoản |
| L-DK | Lifeline | :Dock | «entity» | - | AC-E-Dock |
| L-BK | Lifeline | :Bike | «entity» | - | AC-E-Bike |
| L-PH | Lifeline | :PaymentHold | «entity» | - | AC-E-PaymentHold |
| L-TN | Lifeline | trip:Trip | «entity» | - | AC-E-Trip, chuyến mới |
| L-PG | Lifeline | :PaymentGateway | «boundary» | - | AC-B-PaymentGateway |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |
| L-DD | Lifeline | :DockDevice | «boundary» | - | AC-B-DockDevice |
| A-08 | Actor | Ụ khoá | - | - | ACT-08 |
| F1 | Fragment | break [không đủ điều kiện: 2a, 2b, 2c] | - | - | Bao M06 đến M07 |
| F2 | Fragment | break [xe Chờ kiểm tra: 3a] | - | - | Bao M11 đến M12 |
| F3 | Fragment | break [tạm giữ không thành công: 5a] | - | - | Bao M17 đến M18 |

| STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | A-01 | L-RBF | // scanDockQrCode (mã QR của ụ khoá) | Đồng bộ | - | 1 |
| 1.1 | L-RBF | L-RBC | // requestRental (mã QR, tài khoản) | Đồng bộ | - | 2 |
| 1.1.1 | L-RBC | L-RA | // checkRentalEligibility | Đồng bộ | - | 2 |
| 1.1.1.1 | L-RA | L-TO | // isOngoing | Đồng bộ | - | 2 |
| 1.1.1 (trả về) | L-RA | L-RBC | đủ điều kiện hoặc lý do không đủ (BR-01, BR-02, BR-03) | Trả về | - | 2 |
| 1.1.2 | L-RBC | L-RBF | // rejectRental (lý do, Q-22) | Đồng bộ | F1 | 2a, 2b, 2c |
| 1.1.2.1 | L-RBF | A-01 | // showRentalRejected | Đồng bộ | F1 | 2a, 2b, 2c |
| 1.1.3 | L-RBC | L-DK | // findDockByQrCode (mã QR) | Đồng bộ | - | 3 |
| 1.1.3 (trả về) | L-DK | L-RBC | ụ khoá và xe ụ đang giữ | Trả về | - | 3 |
| 1.1.4 | L-RBC | L-BK | // checkRentable | Đồng bộ | - | 3 |
| 1.1.5 | L-RBC | L-RBF | // rejectRental (lý do, Q-22) | Đồng bộ | F2 | 3a |
| 1.1.5.1 | L-RBF | A-01 | // showRentalRejected | Đồng bộ | F2 | 3a |
| 1.1.6 | L-RBC | L-PG | // requestHold (200.000 đồng, mã tham chiếu thẻ) | Đồng bộ | - | 4 |
| 1.1.6.1 | L-PG | A-07 | // placeHold | Đồng bộ | - | 4 |
| 1.1.6.1 (trả về) | A-07 | L-PG | kết quả tạm giữ | Trả về | - | 5 |
| 1.1.6 (trả về) | L-PG | L-RBC | kết quả tạm giữ, mã khoản tạm giữ (Q-30) | Trả về | - | 5 |
| 1.1.7 | L-RBC | L-RBF | // rejectRental (lý do, Q-08) | Đồng bộ | F3 | 5a |
| 1.1.7.1 | L-RBF | A-01 | // showRentalRejected | Đồng bộ | F3 | 5a |
| 1.1.8 | L-RBC | L-PH | // recordHold (mã khoản tạm giữ, số tiền) | Tạo | - | 5 |
| 1.1.9 | L-RBC | L-DD | // sendUnlockCommand (ụ khoá) | Đồng bộ | - | 6 |
| 1.1.9.1 | L-DD | A-08 | // unlock | Bất đồng bộ | - | 6 |
| 1.1.10 | L-RBC | L-RBC | // startRemovalWait (60 giây, BR-06) | Tự gọi | - | 6 |
| 2 | A-08 | L-DD | // reportBikeRemoved | Bất đồng bộ | - | 7 |
| 2.1 | L-DD | L-RBC | // handleBikeRemoved (ụ khoá) | Đồng bộ | - | 7 |
| 2.1.1 | L-RBC | L-DK | // releaseBike | Đồng bộ | - | 7 |
| 2.1.2 | L-RBC | L-TN | // startTrip (tài khoản, xe, ụ khoá, khoản tạm giữ) | Tạo | - | 8 |

### SD2 - Luồng 6a (hết thời hạn chờ rút xe)

File diagrams/P07-sequence-UC-005.drawio, trang 2. Tách trang vì SD1 đã có 3 fragment ngoài cùng (ngưỡng F5). Bắt đầu bằng ref tới SD1 tại 1.1.10.

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-RBC | Lifeline | :RentBikeController | «control» | - | AC-C-RentBikeController |
| L-PH | Lifeline | :PaymentHold | «entity» | - | AC-E-PaymentHold |
| L-PG | Lifeline | :PaymentGateway | «boundary» | - | AC-B-PaymentGateway |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |
| L-DD | Lifeline | :DockDevice | «boundary» | - | AC-B-DockDevice |
| A-08 | Actor | Ụ khoá | - | - | ACT-08 |
| R1 | Fragment | ref SD1 - Luồng chính tới 1.1.10 | - | - | Bao G1 đến G2 |

| STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 3 | L-RBC | L-RBC | // handleRemovalTimeout | Tự gọi | - | 6a |
| 3.1 | L-RBC | L-DD | // sendLockCommand (ụ khoá) | Đồng bộ | - | 6a1 |
| 3.1.1 | L-DD | A-08 | // lock | Bất đồng bộ | - | 6a1 |
| 3.2 | L-RBC | L-PG | // requestCancelHold (mã khoản tạm giữ) | Đồng bộ | - | 6a2 |
| 3.2.1 | L-PG | A-07 | // cancelHold | Đồng bộ | - | 6a2 |
| 3.3 | L-RBC | L-PH | // markCancelled | Đồng bộ | - | 6a2 |

## F6. Quy tắc tương tác

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-005.drawio. Phạm vi: SD1 (luồng chính và các luồng thay thế đã gộp, MUC_CHI_TIET = DAY_DU).

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| A-01 | Actor | Người thuê xe | - | - | - |
| L-RBF | Object | :RentBikeForm | «boundary» | - | - |
| L-RBC | Object | :RentBikeController | «control» | - | - |
| L-RA | Object | :RiderAccount | «entity» | - | - |
| L-TO | Object | ongoing:Trip | «entity» | - | - |
| L-DK | Object | :Dock | «entity» | - | - |
| L-BK | Object | :Bike | «entity» | - | - |
| L-PH | Object | :PaymentHold | «entity» | - | - |
| L-TN | Object | trip:Trip | «entity» | - | - |
| L-PG | Object | :PaymentGateway | «boundary» | - | - |
| A-07 | Actor | Cổng thanh toán | - | - | - |
| L-DD | Object | :DockDevice | «boundary» | - | - |
| A-08 | Actor | Ụ khoá | - | - | - |

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message |
|---|---|---|---|---|---|
| K01 | A-01 | L-RBF | Link | 1: // scanDockQrCode (-->)<br>1.1.2.1, 1.1.5.1, 1.1.7.1: // showRentalRejected (<--) | 1 Nguồn-->Đích; 1.1.2.1, 1.1.5.1, 1.1.7.1 Đích-->Nguồn |
| K02 | L-RBF | L-RBC | Link | 1.1: // requestRental (-->)<br>1.1.2, 1.1.5, 1.1.7: // rejectRental (<--) | 1.1 Nguồn-->Đích; còn lại Đích-->Nguồn |
| K03 | L-RBC | L-RA | Link | 1.1.1: // checkRentalEligibility (-->) | Nguồn-->Đích |
| K04 | L-RA | L-TO | Link | 1.1.1.1: // isOngoing (-->) | Nguồn-->Đích |
| K05 | L-RBC | L-DK | Link | 1.1.3: // findDockByQrCode (-->)<br>2.1.1: // releaseBike (-->) | Nguồn-->Đích |
| K06 | L-RBC | L-BK | Link | 1.1.4: // checkRentable (-->) | Nguồn-->Đích |
| K07 | L-RBC | L-PG | Link | 1.1.6: // requestHold (-->) | Nguồn-->Đích |
| K08 | L-PG | A-07 | Link | 1.1.6.1: // placeHold (-->) | Nguồn-->Đích |
| K09 | L-RBC | L-PH | Link | 1.1.8: // recordHold (-->) | Nguồn-->Đích |
| K10 | L-RBC | L-DD | Link | 1.1.9: // sendUnlockCommand (-->)<br>2.1: // handleBikeRemoved (<--) | 1.1.9 Nguồn-->Đích; 2.1 Đích-->Nguồn |
| K11 | L-DD | A-08 | Link | 1.1.9.1: // unlock (-->)<br>2: // reportBikeRemoved (<--) | 1.1.9.1 Nguồn-->Đích; 2 Đích-->Nguồn |
| K12 | L-RBC | L-RBC | Link | 1.1.10: // startRemovalWait | Tự gọi |
| K13 | L-RBC | L-TN | Link | 2.1.2: // startTrip (-->) | Nguồn-->Đích |

## F8. VOPC

File diagrams/P07-class-UC-005.drawio.

| ID (mã AC) | Loại | Nhãn | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-RentBikeForm | Class | RentBikeForm | boundary | - | dockQrCode | // scanDockQrCode<br>// showRentalRejected |
| AC-B-PaymentGateway | Class | PaymentGateway | boundary | - | - | // requestHold<br>// requestCancelHold |
| AC-B-DockDevice | Class | DockDevice | boundary | - | - | // sendUnlockCommand<br>// sendLockCommand<br>// reportBikeRemoved |
| AC-C-RentBikeController | Class | RentBikeController | control | - | - | // requestRental<br>// rejectRental<br>// startRemovalWait<br>// handleBikeRemoved<br>// handleRemovalTimeout |
| AC-E-RiderAccount | Class | RiderAccount | entity | - | cardReference: Văn bản<br>outstandingFare: Số tiền | // checkRentalEligibility |
| AC-E-Trip | Class | Trip | entity | - | startTime: Giờ<br>status: Trạng thái | // isOngoing<br>// startTrip |
| AC-E-Dock | Class | Dock | entity | - | qrCode: Văn bản | // findDockByQrCode<br>// releaseBike |
| AC-E-Bike | Class | Bike | entity | - | status: Trạng thái | // checkRentable |
| AC-E-PaymentHold | Class | PaymentHold | entity | - | holdReference: Văn bản<br>amount: Số tiền<br>status: Trạng thái | // recordHold<br>// markCancelled |

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC005-01 | AC-B-RentBikeForm | AC-C-RentBikeController | Association | - | - | K02; tạm thời |
| R-UC005-02 | AC-C-RentBikeController | AC-E-RiderAccount | Association | - | - | K03; tạm thời |
| R-UC005-03 | AC-E-RiderAccount | AC-E-Trip | Association | A 1 - B 0..* | rider / trips | K04; GL-04 "của một người thuê xe"; BR-02 |
| R-UC005-04 | AC-C-RentBikeController | AC-E-Dock | Association | - | - | K05; tạm thời |
| R-UC005-05 | AC-C-RentBikeController | AC-E-Bike | Association | - | - | K06; tạm thời |
| R-UC005-06 | AC-C-RentBikeController | AC-B-PaymentGateway | Association | - | - | K07; tạm thời |
| R-UC005-07 | AC-C-RentBikeController | AC-E-PaymentHold | Association | - | - | K09; tạm thời |
| R-UC005-08 | AC-C-RentBikeController | AC-B-DockDevice | Association | - | - | K10; tạm thời |
| R-UC005-09 | AC-C-RentBikeController | AC-E-Trip | Association | - | - | K13; tạm thời |
| R-UC005-10 | AC-E-Dock | AC-E-Bike | Association | A 0..1 - B 0..1 | dock / dockedBike | Trả về của 1.1.3; GL-23 "giữ một xe"; GL-24 |
| R-UC005-11 | AC-E-Trip | AC-E-Bike | Association | A 0..* - B 1 | - | Bước 8; GL-04 "sử dụng một xe" |
| R-UC005-12 | AC-E-Trip | AC-E-Dock | Association | A 0..* - B 1 | - / startDock | Bước 8; GL-04 "từ khi xe được rút khỏi ụ khoá" |
| R-UC005-13 | AC-E-Trip | AC-E-PaymentHold | Association | A 0..1 - B 1 | - | Bước 8; GL-08 "trong suốt một chuyến đi"; 6a2 khoản tạm giữ tồn tại khi không có chuyến |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1 | AC-B-RentBikeForm |
| 2 | 1.1, 1.1.1, 1.1.1.1 | AC-B-RentBikeForm, AC-C-RentBikeController, AC-E-RiderAccount, AC-E-Trip |
| 2a, 2b, 2c | 1.1.2, 1.1.2.1 | AC-C-RentBikeController, AC-B-RentBikeForm |
| 3 | 1.1.3, 1.1.4 | AC-E-Dock, AC-E-Bike |
| 3a | 1.1.5, 1.1.5.1 | AC-C-RentBikeController, AC-B-RentBikeForm |
| 4 | 1.1.6, 1.1.6.1 | AC-B-PaymentGateway |
| 5 | 1.1.6 (trả về), 1.1.8 | AC-B-PaymentGateway, AC-E-PaymentHold |
| 5a | 1.1.7, 1.1.7.1 | AC-C-RentBikeController, AC-B-RentBikeForm |
| 6 | 1.1.9, 1.1.9.1, 1.1.10 | AC-B-DockDevice, AC-C-RentBikeController |
| 6a | 3 | AC-C-RentBikeController |
| 6a1 | 3.1, 3.1.1 | AC-B-DockDevice |
| 6a2 | 3.2, 3.2.1, 3.3 | AC-B-PaymentGateway, AC-E-PaymentHold |
| 7 | 2, 2.1 | AC-B-DockDevice, AC-C-RentBikeController |
| 8 | 2.1.1, 2.1.2 | AC-E-Dock, AC-E-Trip |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-30 | Cổng thanh toán trả về gì để hệ thống thu hoặc huỷ đúng khoản tạm giữ về sau (mã khoản tạm giữ riêng, hay dùng mã tham chiếu thẻ kèm số tiền)? | AC-E-PaymentHold.holdReference; UC-005 bước 5, 6a2; UC-007; UC-009 | Mục 14; hồ sơ dự án "chưa có tài liệu API" |

Liên quan từ bước trước: Q-08, Q-10, Q-13, Q-20, Q-21, Q-22.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-005 bước 8 | Bước 8 chỉ ghi "Bắt đầu chuyến đi"; không nêu ụ khoá trở thành ụ trống, trong khi UC-004 cần số ụ trống (REQ-05) | Bổ sung vào bước 8: "Hệ thống ghi nhận ụ khoá không còn giữ xe và bắt đầu chuyến đi." |

## Vấn đề còn mở

- Boundary thiết bị đặt tên DockDevice thay vì Dock theo F3.1 (không hậu tố khi HAU_TO_TEN_LOP = Mặc định), vì cùng khái niệm ụ khoá còn là entity Dock. F3.1 không có quy tắc cho trường hợp thiết bị vừa là tác nhân vừa là dữ liệu hệ thống quản lý.
- Thời hạn chờ 60 giây không có tác nhân thời gian (P01 đã loại, mục 4); control tự phát hiện hết hạn (message 3 tự gọi ở SD2). Prompt không có mẫu cho sự kiện thời gian nội bộ không phải tác nhân.
- Dùng toán tử break cho các luồng từ chối; F5 chỉ liệt kê alt, opt, loop, ref.
- Danh từ "Trạm" xếp "Loại - là tác nhân hoặc ngoài phạm vi" dù trạm nằm trong phạm vi hệ thống; danh sách kết luận của F3.2 không có giá trị "không tham gia use case này".
- Target 9: RentBikeController có 5 trách nhiệm, Đạt. Target 14: file .drawio sinh từ bảng; cạnh tự gọi dùng điểm uốn.
