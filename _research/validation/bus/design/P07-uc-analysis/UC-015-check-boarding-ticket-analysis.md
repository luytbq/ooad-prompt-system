# P07 - Phân tích use case UC-015 Soát vé lên xe - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P04-uc-specs/UC-015-check-boarding-ticket.md 1.0; P04-uc-specs/_BR-register.md (BR-10, BR-20 đến BR-22); P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P02-usecases.md 1.1; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0, P07-uc-analysis/UC-008-return-ticket-analysis.md 1.0 và P07-uc-analysis/UC-013-cancel-trip-analysis.md 1.0 (sổ đăng ký AC). UC-015 không có use case được include hoặc extend nên không cần đặc tả P04 nào khác |
| Phạm vi | UC-015 |

Quy ước trích nguồn: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md; "Dữ liệu vào n", "Dữ liệu ra n" chỉ bảng dữ liệu của P04 UC-015. Tham số bước: LUONG_CAN_VE = Không có (vẽ mọi luồng); YEU_CAU_BO_SUNG = Không có. Chế độ giả định CO_NHAN, mức chi tiết DAY_DU, hậu tố tên lớp Mặc định.

## 1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-015 Soát vé lên xe (Check Boarding Ticket) |
| Tác nhân chính (ACT, loại) | ACT-05 Phụ xe (Người) |
| Tác nhân phụ (ACT, loại) | ACT-09 Đầu quét mã vạch (Thiết bị), tương tác trực tiếp ở bước 4 (RL-23) |
| Include (UC) | Không có |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2 không có điểm mở rộng của UC-015) |
| Tác nhân thời gian | ACT-10 Bộ định thời không kích hoạt UC-015 và không tương tác với UC-015. UC-014 Chuẩn bị danh sách hành khách của chuyến (EV-18, 15 phút trước giờ xuất bến) tạo danh sách hành khách mà UC-015 đọc (GL-05). UC-015 chỉ đọc danh sách và ghi trạng thái đã soát của vé; UC-015 không tạo, đổi hay làm mất hiệu lực mốc nào của UC-006, UC-014 nên không có message hẹn, hẹn lại hoặc huỷ mốc (A2) |
| File P07 đã có được dùng làm sổ đăng ký AC | UC-002-book-ticket-online-analysis.md, UC-008-return-ticket-analysis.md, UC-013-cancel-trip-analysis.md. Sổ AC: AC-B-BookTicketForm, AC-B-SmsGateway, AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm, AC-B-PaymentGateway, AC-B-CancelTripForm (boundary); AC-C-BookTicketOnlineController, AC-C-PayTicketOnlineController (tạm chờ UC-003), AC-C-ReturnTicketController, AC-C-CancelTripController (control); AC-E-Trip, AC-E-Route, AC-E-Seat, AC-E-Booking, AC-E-Ticket, AC-E-BaseFare, AC-E-HolidaySurcharge, AC-E-Refund, AC-E-PhoneReservation (entity). UC-015 tái dùng AC-E-Trip, AC-E-Route, AC-E-Seat, AC-E-Ticket |

## 2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Phụ xe | Yêu cầu bắt đầu soát vé và chọn chuyến cần soát (xem Dữ liệu vào 1) (ASM-32). | Không đổi | Dữ liệu vào 1; ASM-32; REQ-42, REQ-55 |
| 2 | Hệ thống | Hiển thị thông tin chuyến và số vé còn hiệu lực trong danh sách hành khách của chuyến (xem Dữ liệu ra 1) (ASM-33). | Hệ thống tìm chuyến có tuyến và giờ xuất bến trùng thông tin phụ xe đã chọn, rồi mở một phiên soát vé cho chuyến đó (ASM-32, ASM-51). Hệ thống lấy tuyến và giờ xuất bến từ chuyến, lấy từ danh sách hành khách của chuyến số vé chưa bị huỷ và số vé đã được ghi nhận là đã soát. Hệ thống hiển thị các thông tin đó cho phụ xe. | Dữ liệu ra 1; ASM-32, ASM-33, ASM-51; GL-04, GL-05, GL-28, GL-36, GL-38; REQ-42, REQ-61 |
| 3 | Phụ xe | Quét mã vạch trên vé hành khách xuất trình khi lên xe bằng đầu quét mã vạch. | Không đổi | REQ-23, REQ-55 |
| 3a | Phụ xe | Điều kiện: hành khách xuất trình vé mua trực tuyến bằng mã vé nhận qua SMS, không có mã vạch để quét (ASM-34). Nhập mã vé hành khách xuất trình (xem Dữ liệu vào 2). Tiếp tục bước 5. | Không đổi | Dữ liệu vào 2; ASM-34; REQ-19 |
| 4 | Đầu quét mã vạch | Đọc mã vạch trên vé và chuyển mã vé cho hệ thống (xem Dữ liệu vào 2). | Không đổi | Dữ liệu vào 2; REQ-23, REQ-55, REQ-56 |
| 5 | Hệ thống | Kiểm tra vé có mã vé đã nhận thuộc chuyến đang soát, chưa bị huỷ và chưa được soát (BR-20, BR-21, BR-22, ASM-33). | Hệ thống tìm trong danh sách hành khách của chuyến vé có mã vé đã nhận (BR-20). Với vé tìm được, hệ thống kiểm tra trạng thái vé: đã huỷ thì không hợp lệ (BR-21), chưa huỷ nhưng đã có thời điểm soát thì không hợp lệ (BR-22); thứ tự kiểm tra đã huỷ trước, đã soát sau (Q-47). Hệ thống lấy mã chỗ từ chỗ của vé, họ tên người đi và thời điểm soát trước từ vé để dùng ở bước 7 và luồng 5b, 5c. | BR-10, BR-20, BR-21, BR-22; GL-05, GL-14, GL-22, GL-38, GL-39; ASM-33, ASM-36; Q-47; REQ-57, REQ-58 |
| 5a | Hệ thống | Điều kiện: danh sách hành khách của chuyến không có vé nào mang mã vé đã nhận (ASM-33). Báo vé không hợp lệ với lý do sai chuyến (BR-20) (xem Dữ liệu ra 2). Tiếp tục bước 8. | Hệ thống xác định danh sách hành khách của chuyến không có vé mang mã vé đã nhận và kết luận vé không hợp lệ với lý do Sai chuyến. Hệ thống hiển thị kết quả cùng mã vé đã nhận, không có chỗ và họ tên; lần quét không được ghi nhận. | BR-20; GL-05, GL-14; ASM-33, ASM-35; Q-45; REQ-58 |
| 5b | Hệ thống | Điều kiện: vé có trong danh sách hành khách của chuyến và đã bị huỷ (ASM-36). Báo vé không hợp lệ với lý do vé đã huỷ (BR-21) (xem Dữ liệu ra 2). Tiếp tục bước 8. | Hệ thống xác định vé tìm được đang ở trạng thái đã huỷ và kết luận vé không hợp lệ với lý do Vé đã huỷ. Hệ thống hiển thị kết quả cùng mã vé và mã chỗ của vé; trạng thái vé không đổi và lần quét không được ghi nhận. | BR-21; GL-14, GL-39; ASM-35, ASM-36; REQ-58 |
| 5c | Hệ thống | Điều kiện: vé có trong danh sách hành khách của chuyến, chưa bị huỷ và đã được soát. Báo vé không hợp lệ với lý do vé đã soát, kèm thời điểm soát trước đó (BR-22) (xem Dữ liệu ra 2). Tiếp tục bước 8. | Hệ thống xác định vé tìm được chưa huỷ và đã có thời điểm soát, kết luận vé không hợp lệ với lý do Vé đã soát. Hệ thống hiển thị kết quả cùng mã vé, mã chỗ và thời điểm soát trước lấy từ vé; trạng thái vé không đổi. | BR-22; GL-14; ASM-35; REQ-58 |
| 6 | Hệ thống | Ghi nhận vé đã soát kèm thời điểm soát (ASM-35). | Hệ thống ghi thời điểm soát hiện tại vào vé đã được kết luận hợp lệ ở bước 5, nhờ đó vé được tính là đã soát. Chỉ vé được báo hợp lệ mới được ghi nhận (ASM-35). | ASM-35; GL-37; REQ-57 |
| 7 | Hệ thống | Báo vé hợp lệ kèm chỗ và họ tên người đi của vé (xem Dữ liệu ra 2). | Hệ thống lấy mã chỗ từ chỗ của vé và họ tên người đi từ vé. Hệ thống hiển thị kết quả Hợp lệ cùng mã vé, chỗ và họ tên người đi. | Dữ liệu ra 2; GL-02, GL-14, GL-26; ASM-33; REQ-57 |
| 8 | Phụ xe | Lặp lại bước 3-7 cho đến khi không còn hành khách lên xe xuất trình vé. | Không đổi | P02 CAND-21, U-R14 |
| 9 | Phụ xe | Yêu cầu kết thúc soát vé của chuyến. | Không đổi | REQ-55 |
| 10 | Hệ thống | Gửi kết quả soát vé của chuyến từ máy soát vé về dữ liệu vé của hệ thống (REQ-60, ASM-35). | Hệ thống lấy kết quả soát vé của phiên, gồm các vé đã được ghi nhận là đã soát, và gửi về dữ liệu vé của hệ thống. Khi gửi được, phiên ghi trạng thái gửi là Đã gửi (ASM-35, Q-74). | REQ-60; GL-28; ASM-35, ASM-51; Q-46, Q-74 |
| 10a | Hệ thống | Điều kiện: máy soát vé đang ở vùng mất sóng. Lưu kết quả soát vé chưa gửi trên máy soát vé và tự gửi về dữ liệu vé của hệ thống khi máy có sóng trở lại (REQ-60, ASM-35). Tiếp tục bước 11. | Phiên giữ kết quả soát vé chưa gửi trên máy với trạng thái gửi là Chờ gửi khi có sóng. Việc tự gửi khi máy có sóng trở lại diễn ra sau khi use case kết thúc, không có thao tác của phụ xe và không có message trong sơ đồ (ASM-52). | REQ-59, REQ-60; GL-28; ASM-35, ASM-52; Q-46 |
| 11 | Hệ thống | Hiển thị kết quả soát vé của chuyến (xem Dữ liệu ra 3). | Hệ thống lấy tuyến và giờ xuất bến từ chuyến, lấy từ danh sách hành khách của chuyến số vé đã soát và số vé còn hiệu lực chưa soát (số vé còn hiệu lực trừ số vé đã soát). Hệ thống lấy trạng thái gửi kết quả từ phiên và hiển thị các thông tin đó cho phụ xe. | Dữ liệu ra 3; GL-05, GL-28; ASM-35; REQ-60 |

## 3. Tìm lớp phân tích

### 3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-05 Phụ xe | Người | CheckBoardingTicketForm (AC-B-CheckBoardingTicketForm) | Giao diện người dùng | Mới | Một boundary cho cặp (ACT-05, UC-015) gom mọi tương tác của phụ xe: chọn chuyến, nhập mã vé, yêu cầu kết thúc, nhận thông tin chuyến, kết quả từng vé và kết quả soát vé của chuyến. Tên theo hành động của use case với hậu tố Form (HAU_TO_TEN_LOP là Mặc định) |
| ACT-09 Đầu quét mã vạch | Thiết bị | BarcodeScanner (AC-B-BarcodeScanner) | Giao diện thiết bị | Mới | ACT-09 tương tác trực tiếp ở bước 4: đọc mã vạch trên vé và chuyển mã vé cho hệ thống. Tên theo thiết bị, không hậu tố (HAU_TO_TEN_LOP là Mặc định); không trùng tên entity nào nên không cần hậu tố Device bắt buộc. Boundary đặt mã tại đây để UC-014 và UC-005 (nếu cần) tái dùng đúng mã |

ACT-10 Bộ định thời không tham gia UC-015 nên không có boundary. Số boundary là 2, bằng số tác nhân tham gia (ACT-05, ACT-09).

### 3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Phụ xe | Mô tả; bước 1, 3, 3a, 8, 9; tiền điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | ACT-05, có boundary CheckBoardingTicketForm |
| 2 | Đầu quét mã vạch | Bước 3, 4 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-09, thiết bị, có boundary BarcodeScanner |
| 3 | Hệ thống | Mọi bước hệ thống | Loại - mơ hồ | Chỉ là chủ ngữ của bước, không chỉ một khái niệm dữ liệu cụ thể |
| 4 | Hành khách | Mô tả; bước 3; sự kiện kích hoạt | Loại - là tác nhân hoặc ngoài phạm vi | Là người đi (GL-26, SH-03) chỉ xuất trình vé, không tương tác trực tiếp với hệ thống (P01 Mục 3) |
| 5 | Máy soát vé, ứng dụng soát vé | Tiền điều kiện; bước 10, 10a; Yêu cầu đặc biệt 2 | Loại - là tác nhân hoặc ngoài phạm vi | Là nền tảng chạy chức năng soát vé thuộc hệ thống; phần có giao tiếp riêng là đầu quét (ASM-01, ASM-06, GL-23) |
| 6 | Vùng mất sóng, sóng | Luồng 10a; Yêu cầu đặc biệt 1 | Loại - là tác nhân hoặc ngoài phạm vi | Là đường truyền, không phải tác nhân (P01 Mục 4) |
| 7 | Phiên làm việc, xác thực của phụ xe | Tiền điều kiện (ASM-09) | Loại - không tham gia hành vi của use case này (khái niệm của UC-010) | Chỉ là tiền điều kiện; UC-015 không đọc hay ghi phiên đăng nhập |
| 8 | Chuyến, chuyến cần soát, chuyến đang soát | Mô tả; bước 1, 2, 5, 11; Dữ liệu vào 1; Dữ liệu ra 1 #1; Dữ liệu ra 3 #1; BR-20 | Entity (AC-E-Trip) | GL-04; hệ thống lưu chuyến, Trip tìm chuyến theo tuyến và giờ xuất bến, cung cấp tuyến và giờ xuất bến; tái dùng mã từ UC-002 |
| 9 | Tuyến | Dữ liệu vào 1 #1; Dữ liệu ra 1 #1; Dữ liệu ra 3 #1 | Entity (AC-E-Route) | GL-36; Trip dùng Route để kiểm tra tuyến khớp tuyến phụ xe chọn (checkRouteMatches), như UC-013; tái dùng mã từ UC-002 |
| 10 | Điểm đi, điểm đến | Dữ liệu vào 1 #1; Dữ liệu ra 1 #1 | Loại - thuộc tính của Route | departurePoint, arrivalPoint |
| 11 | Giờ xuất bến, thời điểm hiện tại | Dữ liệu vào 1 #1; Dữ liệu ra 1 #1; bước 6 | Loại - thuộc tính của Trip | departureTime; GL-10. Thời điểm hiện tại chỉ là tham số của message markChecked |
| 12 | Tuyến và giờ xuất bến | Dữ liệu ra 1 #1; Dữ liệu ra 3 #1 | Loại - trùng hoặc đồng nghĩa với tuyến, giờ xuất bến | Gọi chung hai khái niệm đã xét |
| 13 | Phiên soát vé | Mục 8 của P04; hậu điều kiện; Dữ liệu ra 3 | Entity (AC-E-TicketCheckSession) | GL-28; phiên gắn một chuyến (ASM-32), giữ trạng thái gửi kết quả và kết quả chưa gửi khi mất sóng nên tồn tại lâu hơn một lần thực hiện use case (ASM-51) |
| 14 | Danh sách hành khách của chuyến | Tiền điều kiện; bước 2, 5, 5a, 5b; Dữ liệu vào 1 #1; ASM-33 | Entity (AC-E-TripPassengerList) | GL-05; nắm tập vé của một chuyến trên máy, trả lời vé có thuộc chuyến không và đếm vé (ASM-50). Chờ Q-73 |
| 15 | Vé, vé còn hiệu lực | Mô tả; bước 2, 5, 6, 7; Dữ liệu ra 1 #2; Dữ liệu ra 3 #3; BR-10, BR-20 đến BR-22 | Entity (AC-E-Ticket) | GL-37, GL-38; Ticket kết luận hợp lệ hay không và ghi nhận đã soát; tái dùng mã từ UC-002 |
| 16 | Vé đã huỷ | Bước 5, 5b; Dữ liệu ra 2 #2; BR-21; Mục 8 của P04 | Loại - thuộc tính của Ticket | status, GL-39 ghi một giá trị trạng thái của vé; nguyên nhân huỷ (trả vé, huỷ chuyến, đổi vé) thuộc UC-008, UC-013, UC-007 |
| 17 | Vé giấy | Bước 3; Dữ liệu vào 2 #1 | Loại - không tham gia hành vi của use case này (khái niệm của UC-005) | GL-40; UC-015 chỉ đọc mã vé thể hiện trên vé giấy, không in hay đọc vé giấy như một đối tượng riêng |
| 18 | Mã vạch | Bước 3, 4; Dữ liệu vào 2 #1 | Loại - trùng hoặc đồng nghĩa với mã vé | Là cách thể hiện mã vé trên vé giấy (GL-40); đầu quét chuyển mã vạch thành mã vé |
| 19 | Mã vé | Bước 4, 5; Dữ liệu vào 2; Dữ liệu ra 2 #3; BR-10 | Loại - thuộc tính của Ticket | ticketCode; GL-22 |
| 20 | SMS, mã vé nhận qua SMS | Luồng 3a; Dữ liệu vào 2 #1 | Loại - không tham gia hành vi của use case này (khái niệm của UC-002) | UC-015 không gửi SMS; mã vé nhận qua SMS chỉ là nguồn của mã vé phụ xe nhập |
| 21 | Chỗ, mã chỗ | Bước 7; luồng 5b, 5c; Dữ liệu ra 2 #4 | Entity (AC-E-Seat) | GL-02; Ticket lấy mã chỗ từ Seat qua getSeatCode như UC-008; tái dùng mã từ UC-002 |
| 22 | Họ tên người đi, người đi | Bước 7; Dữ liệu ra 2 #5 | Loại - thuộc tính của Ticket | travelerName; GL-26 |
| 23 | Thời điểm soát, thời điểm soát trước đó | Bước 6; luồng 5c; Dữ liệu ra 2 #6; hậu điều kiện | Loại - thuộc tính của Ticket | checkedTime; ASM-35; vé có checkedTime là vé đã soát |
| 24 | Kết quả soát vé (Hợp lệ, Không hợp lệ) | Bước 5, 7; Dữ liệu ra 2 #1; GL-14 | Loại - thao tác hoặc sự kiện | Kết luận của phép kiểm tra ở bước 5, là giá trị trả về của determineCheckResult; lần quét không hợp lệ không được lưu (ASM-35) |
| 25 | Lý do không hợp lệ (Sai chuyến, Vé đã huỷ, Vé đã soát) | Luồng 5a, 5b, 5c; Dữ liệu ra 2 #2; BR-20 đến BR-22 | Loại - thuộc tính của kết quả soát vé | Giá trị đi kèm kết quả Không hợp lệ, không lưu; thứ tự khi vé thoả hai lý do chờ Q-47 |
| 26 | Kết quả soát vé của chuyến | Bước 10, 11; hậu điều kiện | Loại - trùng hoặc đồng nghĩa với phiên soát vé | Là tập vé đã được ghi nhận đã soát trong phiên (ASM-35) cùng trạng thái gửi của phiên (GL-28) |
| 27 | Số vé còn hiệu lực, số vé đã soát, số vé còn hiệu lực chưa soát | Bước 2, 11; Dữ liệu ra 1 #2, #3; Dữ liệu ra 3 #2, #3 | Loại - thuộc tính của TripPassengerList | Giá trị tính từ các vé trong danh sách, không lưu; do summarizeTicketCounts trả về |
| 28 | Trạng thái gửi kết quả (Đã gửi, Chờ gửi khi có sóng) | Bước 10, 10a; Dữ liệu ra 3 #4 | Loại - thuộc tính của TicketCheckSession | sendStatus |
| 29 | Dữ liệu vé của hệ thống | Bước 10; luồng 10a | Loại - mơ hồ | Chưa rõ hệ thống làm gì với kết quả khi nhận (Q-74); không đủ cơ sở tạo lớp riêng ở mức phân tích |
| 30 | Thông tin chuyến | Bước 2 | Loại - mơ hồ | Gọi chung các thông tin đã xét ở dòng 8 đến 12 |
| 31 | Xe giường nằm 40 chỗ | Mục 8 của P04 (ví dụ số liệu) | Loại - không tham gia hành vi của use case này (khái niệm của UC-012) | Chỉ dùng để minh hoạ số vé tối đa của một phiên (BR-10); UC-015 không đọc hay ghi xe |

### 3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| CheckBoardingTicketController (AC-C-CheckBoardingTicketController) | UC-015 Soát vé lên xe | Mới | Một control cho use case, đặt tên theo tên tiếng Anh của use case (Check Boarding Ticket) với hậu tố Controller (HAU_TO_TEN_LOP là Mặc định). Điều phối trình tự mở phiên, kiểm tra từng lần quét, kết thúc và gửi kết quả; không giữ dữ liệu nghiệp vụ lâu dài |

### 3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-CheckBoardingTicketForm | boundary | CheckBoardingTicketForm | // requestStartCheck: nhận yêu cầu bắt đầu soát vé và tuyến, giờ xuất bến của chuyến cần soát từ phụ xe<br>// enterTicketCode: nhận mã vé phụ xe nhập khi vé không có mã vạch<br>// requestEndCheck: nhận yêu cầu kết thúc soát vé của chuyến<br>// showCheckSessionInfo: hiển thị tuyến, giờ xuất bến, số vé còn hiệu lực, số vé đã soát<br>// showValidTicketResult: hiển thị kết quả Hợp lệ kèm mã vé, chỗ, họ tên người đi<br>// showInvalidTicketResult: hiển thị kết quả Không hợp lệ kèm lý do, mã vé và, khi có, chỗ, thời điểm soát trước<br>// showCheckSummary: hiển thị tuyến, giờ xuất bến, số vé đã soát, số vé còn hiệu lực chưa soát, trạng thái gửi kết quả | departurePoint, arrivalPoint, departureTime, ticketCode | 1, 2, 3a, 5a, 5b, 5c, 7, 9, 11 | Giao diện người dùng | Mới | - |
| AC-B-BarcodeScanner | boundary | BarcodeScanner | // readBarcode: nhận mã vạch do đầu quét đọc từ vé và chuyển mã vé cho control | ticketCode | 3, 4 | Giao diện thiết bị | Mới | GL-22, GL-23, GL-40 |
| AC-C-CheckBoardingTicketController | control | CheckBoardingTicketController | // startCheck: điều phối tìm chuyến, mở phiên soát vé và hiển thị thông tin chuyến<br>// checkTicket: điều phối kiểm tra mã vé, ghi nhận vé đã soát và báo kết quả của một lần quét<br>// endCheck: điều phối gửi kết quả soát vé của phiên và hiển thị kết quả soát vé của chuyến | - | 1-11, 3a, 5a, 5b, 5c, 10a | - | Mới | - |
| AC-E-TicketCheckSession | entity | TicketCheckSession | // startSession: khởi tạo phiên soát vé cho một chuyến<br>// sendResult: gửi kết quả soát vé của chuyến về dữ liệu vé của hệ thống và cho biết trạng thái gửi<br>// markResultSent: ghi nhận kết quả soát vé đã gửi<br>// keepResultPending: giữ kết quả soát vé chưa gửi để tự gửi khi máy có sóng trở lại | sendStatus | 2, 10, 10a | - | Mới | GL-28 |
| AC-E-Trip | entity | Trip | // findTrip: tìm chuyến khớp tuyến và giờ xuất bến phụ xe đã chọn<br>// getRouteAndDepartureTime: cung cấp tuyến và giờ xuất bến của chuyến | departureTime | 2, 11 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-04, GL-10 |
| AC-E-Route | entity | Route | // checkRouteMatches: kiểm tra điểm đi, điểm đến của tuyến khớp tuyến phụ xe đã chọn | departurePoint, arrivalPoint | 2 | - | Tái dùng từ UC-002 | GL-36 |
| AC-E-TripPassengerList | entity | TripPassengerList | // findTicket: tìm trong danh sách vé có mã vé đã nhận; không có vé thì vé không thuộc chuyến (BR-20)<br>// summarizeTicketCounts: tính số vé còn hiệu lực, số vé đã soát, số vé còn hiệu lực chưa soát của chuyến | - | 2, 5, 5a, 11 | - | Mới | GL-05 |
| AC-E-Ticket | entity | Ticket | // determineCheckResult: kết luận vé hợp lệ hay không hợp lệ theo trạng thái huỷ và thời điểm soát, kèm lý do, mã chỗ, họ tên người đi, thời điểm soát trước (BR-21, BR-22)<br>// markChecked: ghi nhận vé đã soát kèm thời điểm soát (ASM-35) | ticketCode, travelerName, status, checkedTime | 5, 5b, 5c, 6, 7 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-14, GL-22, GL-26, GL-37, GL-38, GL-39 |
| AC-E-Seat | entity | Seat | // getSeatCode: cung cấp mã chỗ của vé | seatCode | 5, 7 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-02 |

Số lớp: 9 (2 boundary, 1 control, 6 entity), trong đó 4 lớp tái dùng từ UC-002, UC-008, UC-013 (Trip, Route, Ticket, Seat) và 5 lớp mới (CheckBoardingTicketForm, BarcodeScanner, CheckBoardingTicketController, TicketCheckSession, TripPassengerList). Thuộc tính có kiểu khái niệm: departureTime (Giờ), checkedTime (Giờ), sendStatus (Trạng thái, giá trị Đã gửi hoặc Chờ gửi khi có sóng), status (Trạng thái), các thuộc tính còn lại là Văn bản. Trách nhiệm findTrip của Trip dùng lại đúng tên của UC-013, getRouteAndDepartureTime của Trip và checkRouteMatches của Route dùng lại đúng tên của UC-002, UC-013, getSeatCode của Seat dùng lại đúng tên của UC-008. Một vé có checkedTime là vé đã soát; Ticket.status vẫn chỉ ghi vé đã phát hành hay đã huỷ.

## 4. Phân bổ hành vi


| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc (Giao tiếp tác nhân / Information Expert / Controller / Creator / Lớp mới / Giao cho control) | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestStartCheck | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | - |
| 1 | // startCheck | AC-C-CheckBoardingTicketController | Controller | - |
| 2 | // findTrip | AC-E-Trip | Information Expert | Tuyến và giờ xuất bến nằm ở Trip và Route. Giao cho Trip và dùng Route (giống UC-013); giao cho control bị loại vì control sẽ phải đọc dữ liệu của chuyến |
| 2 | // checkRouteMatches | AC-E-Route | Information Expert | Điểm đi, điểm đến nằm ở Route |
| 2 | // startSession | AC-E-TicketCheckSession | Creator | Phiên không nằm trong đối tượng nào của use case; control nhận chuyến vừa tìm được là dữ liệu khởi tạo phiên nên control gửi message Tạo (ASM-51). Gộp phiên vào Trip bị loại vì Trip không biết phiên soát vé trên máy |
| 2 | // getRouteAndDepartureTime | AC-E-Trip | Information Expert | Tuyến và giờ xuất bến nằm ở Trip |
| 2 | // summarizeTicketCounts | AC-E-TripPassengerList | Information Expert | Dữ liệu nằm ở nhiều lớp (danh sách và các vé trong danh sách). Giao cho TripPassengerList vì danh sách nắm tập vé của chuyến trên máy (ASM-50); giao cho control bị loại vì control sẽ phải duyệt trạng thái từng vé (god control); giao cho Ticket bị loại vì một vé không biết các vé còn lại |
| 2 | // showCheckSessionInfo | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | - |
| 3, 4 | // readBarcode | AC-B-BarcodeScanner | Giao tiếp tác nhân | Bước 3 (phụ xe quét) và bước 4 (đầu quét đọc) là một thao tác đi vào hệ thống qua boundary thiết bị; message đến từ ACT-09, không vẽ message từ ACT-05 tới BarcodeScanner vì ACT-05 không là actor của boundary này (F6, ASM-53) |
| 3a | // enterTicketCode | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | - |
| 4, 3a | // checkTicket | AC-C-CheckBoardingTicketController | Controller | Hai boundary (BarcodeScanner, CheckBoardingTicketForm) cùng gọi một trách nhiệm của control vì bước 5 trở đi giống nhau cho cả hai nguồn mã vé |
| 5 | // findTicket | AC-E-TripPassengerList | Information Expert | Mã vé của các vé thuộc chuyến nằm ở danh sách hành khách của chuyến (ASM-33). Giao cho Ticket bị loại vì từng vé không biết mã vé còn lại; giao cho Trip bị loại vì danh sách trên máy là phạm vi riêng (ASM-50, Q-73) |
| 5 | // determineCheckResult | AC-E-Ticket | Information Expert | Trạng thái huỷ và thời điểm soát nằm ở Ticket. Giao cho control bị loại vì control sẽ phải đọc trạng thái vé để áp BR-21, BR-22 |
| 5 | // getSeatCode | AC-E-Seat | Information Expert | Mã chỗ nằm ở Seat (giống UC-008) |
| 5a | // showInvalidTicketResult | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | Lý do Sai chuyến do control truyền vào sau khi findTicket không tìm thấy vé (BR-20) |
| 5b | // showInvalidTicketResult | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | Lý do Vé đã huỷ lấy từ kết quả của determineCheckResult (BR-21) |
| 5c | // showInvalidTicketResult | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | Lý do Vé đã soát và thời điểm soát trước lấy từ kết quả của determineCheckResult (BR-22) |
| 6 | // markChecked | AC-E-Ticket | Information Expert | Thời điểm soát là dữ liệu của vé (ASM-35). Giao cho TicketCheckSession bị loại vì phiên chỉ gửi kết quả, không giữ trạng thái từng vé; giao cho TripPassengerList bị loại vì danh sách không đổi trạng thái vé |
| 7 | // showValidTicketResult | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | - |
| 9 | // requestEndCheck | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | - |
| 9 | // endCheck | AC-C-CheckBoardingTicketController | Controller | - |
| 10 | // sendResult | AC-E-TicketCheckSession | Information Expert | Kết quả cần gửi và trạng thái gửi nằm ở phiên (ASM-51). Giao cho control bị loại vì control sẽ giữ kết quả chờ gửi vượt quá một lần thực hiện use case |
| 10 | // markResultSent | AC-E-TicketCheckSession | Information Expert | Trạng thái gửi nằm ở phiên |
| 10a | // keepResultPending | AC-E-TicketCheckSession | Information Expert | Phiên giữ kết quả chưa gửi và trạng thái Chờ gửi khi có sóng; việc tự gửi lại sau khi use case kết thúc không có message (ASM-52) |
| 11 | // getRouteAndDepartureTime | AC-E-Trip | Information Expert | Tuyến và giờ xuất bến nằm ở Trip |
| 11 | // summarizeTicketCounts | AC-E-TripPassengerList | Information Expert | Xem bước 2 |
| 11 | // showCheckSummary | AC-B-CheckBoardingTicketForm | Giao tiếp tác nhân | Số liệu do control tổng hợp tạm từ các kết quả trả về trong lần thực hiện, không lưu |

Bước 8 do phụ xe thực hiện (vòng lặp), được thể hiện bằng fragment loop SD1-FR1 của SD1, không có trách nhiệm riêng. Bước 5a, 5b, 5c không kết thúc use case nên dùng alt, luồng tiếp tục ở bước 8.

## 5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-015.drawio gồm hai trang. SD1 thể hiện luồng chính cùng luồng 10a (fragment alt máy có sóng hay mất sóng); vòng lặp bước 3 đến 8 là fragment loop và chỉ vẽ nhánh vé hợp lệ. SD2 thể hiện luồng 3a (alt) và luồng 5a, 5b, 5c (alt lồng nhau) của một lần lặp trong vòng lặp. Không luồng nào kết thúc use case (cột Quay lại / Kết thúc của P04 không có "Kết thúc") nên không dùng break. Bảng message dùng thêm cột ID (ID cell trong file .drawio). Lifeline TicketCheckSession của SD1 có đỉnh đặt ngang message Tạo 1.1.2. Bước 3 (phụ xe quét) và bước 4 (đầu quét đọc) thể hiện bằng một message readBarcode từ ACT-09 (ASM-53). Message tự gọi 3.1.1.1 và 3.1.1.2 là xử lý nội bộ của TicketCheckSession khi nhận sendResult.

### SD1 - Luồng chính và 10a

a) Tên sơ đồ và luồng thể hiện: luồng chính (bước 1 đến 11, vòng lặp bước 3 đến 8 chỉ vẽ nhánh vé hợp lệ) và luồng 10a (alt máy có sóng hay mất sóng).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1-L01 | Actor | Phụ xe | ACT-05 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 1600 |
| SD1-L02 | Lifeline | :CheckBoardingTicketForm | boundary | - | Boundary của ACT-05 | 200 | 40 | 120 | 1600 |
| SD1-L03 | Lifeline | :CheckBoardingTicketController | control | - | Control của UC-015 | 360 | 40 | 120 | 1600 |
| SD1-L04 | Lifeline | :TicketCheckSession | entity | - | Phiên soát vé của chuyến; được tạo bởi message 1.1.2 | 520 | 320 | 120 | 1320 |
| SD1-L05 | Lifeline | :Trip | entity | - | Chuyến cần soát | 680 | 40 | 120 | 1600 |
| SD1-L06 | Lifeline | :Route | entity | - | Tuyến của chuyến | 840 | 40 | 120 | 1600 |
| SD1-L07 | Lifeline | :TripPassengerList | entity | - | Danh sách hành khách của chuyến trên máy soát vé | 1000 | 40 | 120 | 1600 |
| SD1-L08 | Lifeline | :Ticket | entity | - | Vé đang được soát; một đối tượng cho mỗi lần quét | 1160 | 40 | 120 | 1600 |
| SD1-L09 | Lifeline | :Seat | entity | - | Chỗ của vé đang được soát | 1320 | 40 | 120 | 1600 |
| SD1-L10 | Lifeline | :BarcodeScanner | boundary | - | Boundary của ACT-09 | 1480 | 40 | 120 | 1600 |
| SD1-L11 | Actor | Đầu quét mã vạch | ACT-09 (Thiết bị) | - | Tác nhân phụ | 1640 | 40 | 120 | 1600 |
| SD1-FR1 | Fragment | loop [còn hành khách lên xe xuất trình vé (bước 8)] | loop | - | Vòng lặp bước 8: mỗi lần lặp là một lần quét một vé hợp lệ (bước 3 đến 7). Các nhánh 3a, 5a, 5b, 5c nằm trên SD2 | 180 | 560 | 1600 | 450 |
| SD1-FR2 | Fragment | alt [máy có sóng] | alt | - | Luồng 10a: máy mất sóng thì kết quả được giữ lại chờ gửi; máy có sóng thì kết quả được ghi nhận đã gửi; toán hạng 2: [máy đang ở vùng mất sóng (luồng 10a)] | 500 | 1170 | 320 | 170 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1-M01 | 1 | SD1-L01 | SD1-L02 | // requestStartCheck (tuyến, giờ xuất bến của chuyến cần soát) | Đồng bộ | - | 1 |
| SD1-M02 | 1.1 | SD1-L02 | SD1-L03 | // startCheck (tuyến, giờ xuất bến) | Đồng bộ | - | 1 |
| SD1-M03 | 1.1.1 | SD1-L03 | SD1-L05 | // findTrip (tuyến, giờ xuất bến) | Đồng bộ | - | 2 |
| SD1-M04 | 1.1.1.1 | SD1-L05 | SD1-L06 | // checkRouteMatches (tuyến) | Đồng bộ | - | 2 |
| SD1-M05 | 1.1.1 (trả về) | SD1-L05 | SD1-L03 | chuyến cần soát | Trả về | - | 2 |
| SD1-M06 | 1.1.2 | SD1-L03 | SD1-L04 | // startSession (chuyến) | Tạo | - | 2 |
| SD1-M07 | 1.1.3 | SD1-L03 | SD1-L05 | // getRouteAndDepartureTime | Đồng bộ | - | 2 |
| SD1-M08 | 1.1.3 (trả về) | SD1-L05 | SD1-L03 | tuyến, giờ xuất bến | Trả về | - | 2 |
| SD1-M09 | 1.1.4 | SD1-L03 | SD1-L07 | // summarizeTicketCounts (chuyến) | Đồng bộ | - | 2 |
| SD1-M10 | 1.1.4 (trả về) | SD1-L07 | SD1-L03 | số vé còn hiệu lực, số vé đã soát, số vé còn hiệu lực chưa soát | Trả về | - | 2 |
| SD1-M11 | 1.1.5 | SD1-L03 | SD1-L02 | // showCheckSessionInfo (tuyến, giờ xuất bến, số vé còn hiệu lực, số vé đã soát) | Đồng bộ | - | 2 |
| SD1-M12 | 2 | SD1-L11 | SD1-L10 | // readBarcode (mã vạch) | Đồng bộ | SD1-FR1 | 3, 4 |
| SD1-M13 | 2.1 | SD1-L10 | SD1-L03 | // checkTicket (mã vé) | Đồng bộ | SD1-FR1 | 4 |
| SD1-M14 | 2.1.1 | SD1-L03 | SD1-L07 | // findTicket (mã vé) | Đồng bộ | SD1-FR1 | 5 |
| SD1-M15 | 2.1.1 (trả về) | SD1-L07 | SD1-L03 | vé mang mã vé đã nhận trong danh sách | Trả về | SD1-FR1 | 5 |
| SD1-M16 | 2.1.2 | SD1-L03 | SD1-L08 | // determineCheckResult | Đồng bộ | SD1-FR1 | 5 |
| SD1-M17 | 2.1.2.1 | SD1-L08 | SD1-L09 | // getSeatCode | Đồng bộ | SD1-FR1 | 5 |
| SD1-M18 | 2.1.2.1 (trả về) | SD1-L09 | SD1-L08 | mã chỗ | Trả về | SD1-FR1 | 5 |
| SD1-M19 | 2.1.2 (trả về) | SD1-L08 | SD1-L03 | kết quả Hợp lệ, mã chỗ, họ tên người đi | Trả về | SD1-FR1 | 5 |
| SD1-M20 | 2.1.3 | SD1-L03 | SD1-L08 | // markChecked (thời điểm soát) | Đồng bộ | SD1-FR1 | 6 |
| SD1-M21 | 2.1.4 | SD1-L03 | SD1-L02 | // showValidTicketResult (mã vé, chỗ, họ tên người đi) | Đồng bộ | SD1-FR1 | 7 |
| SD1-M22 | 3 | SD1-L01 | SD1-L02 | // requestEndCheck | Đồng bộ | - | 9 |
| SD1-M23 | 3.1 | SD1-L02 | SD1-L03 | // endCheck | Đồng bộ | - | 9 |
| SD1-M24 | 3.1.1 | SD1-L03 | SD1-L04 | // sendResult | Đồng bộ | - | 10 |
| SD1-M25 | 3.1.1.1 | SD1-L04 | SD1-L04 | // markResultSent | Tự gọi | SD1-FR2 | 10 |
| SD1-M26 | 3.1.1.2 | SD1-L04 | SD1-L04 | // keepResultPending (kết quả soát vé chưa gửi, tự gửi khi máy có sóng trở lại, ASM-52) | Tự gọi | SD1-FR2 | 10a |
| SD1-M27 | 3.1.1 (trả về) | SD1-L04 | SD1-L03 | trạng thái gửi kết quả (Đã gửi hoặc Chờ gửi khi có sóng) | Trả về | - | 10 |
| SD1-M28 | 3.1.2 | SD1-L03 | SD1-L05 | // getRouteAndDepartureTime | Đồng bộ | - | 11 |
| SD1-M29 | 3.1.2 (trả về) | SD1-L05 | SD1-L03 | tuyến, giờ xuất bến | Trả về | - | 11 |
| SD1-M30 | 3.1.3 | SD1-L03 | SD1-L07 | // summarizeTicketCounts (chuyến) | Đồng bộ | - | 11 |
| SD1-M31 | 3.1.3 (trả về) | SD1-L07 | SD1-L03 | số vé còn hiệu lực, số vé đã soát, số vé còn hiệu lực chưa soát | Trả về | - | 11 |
| SD1-M32 | 3.1.4 | SD1-L03 | SD1-L02 | // showCheckSummary (tuyến, giờ xuất bến, số vé đã soát, số vé còn hiệu lực chưa soát, trạng thái gửi kết quả) | Đồng bộ | - | 11 |

SD1 có 32 dòng message, trong đó 9 message trả về; 23 message không kể trả về, 2 fragment ngoài cùng (loop SD1-FR1, alt SD1-FR2). Ngưỡng F5: không quá khoảng 30 message không kể trả về và tối đa 3 fragment ngoài cùng, đạt. Message 2 (readBarcode) đến từ ACT-09; message 3.1.1.1 và 3.1.1.2 là message tự gọi của TicketCheckSession.

### SD2 - Luồng 3a, 5a, 5b, 5c

a) Tên sơ đồ và luồng thể hiện: luồng 3a (phụ xe nhập mã vé nhận qua SMS thay cho bước 3, 4) và luồng 5a, 5b, 5c (vé không hợp lệ) của một lần lặp trong vòng lặp bước 3 đến 8. Sơ đồ bắt đầu tại vị trí bước 3 của vòng lặp SD1; nhánh vé giấy và nhánh vé hợp lệ tham chiếu SD1 bằng fragment ref.

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD2-L01 | Actor | Phụ xe | ACT-05 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 1170 |
| SD2-L02 | Lifeline | :CheckBoardingTicketForm | boundary | - | Boundary của ACT-05 | 200 | 40 | 120 | 1170 |
| SD2-L03 | Lifeline | :CheckBoardingTicketController | control | - | Control của UC-015 | 360 | 40 | 120 | 1170 |
| SD2-L04 | Lifeline | :TripPassengerList | entity | - | Danh sách hành khách của chuyến trên máy soát vé | 520 | 40 | 120 | 1170 |
| SD2-L05 | Lifeline | :Ticket | entity | - | Vé tìm được trong danh sách | 680 | 40 | 120 | 1170 |
| SD2-L06 | Lifeline | :Seat | entity | - | Chỗ của vé | 840 | 40 | 120 | 1170 |
| SD2-L07 | Lifeline | :BarcodeScanner | boundary | - | Boundary của ACT-09 | 1000 | 40 | 120 | 1170 |
| SD2-L08 | Actor | Đầu quét mã vạch | ACT-09 (Thiết bị) | - | Tác nhân phụ | 1160 | 40 | 120 | 1170 |
| SD2-FR1 | Fragment | alt [phụ xe nhập mã vé nhận qua SMS (luồng 3a)] | alt | - | Luồng 3a thay cho bước 3, 4; sau đó tiếp tục bước 5; toán hạng 2: [vé giấy có mã vạch] | 10 | 160 | 1300 | 250 |
| SD2-FR2 | Fragment | ref SD1: 2, 2.1 (readBarcode, checkTicket) | ref | SD2-FR1 | Nhánh vé giấy: tham chiếu message 2, 2.1 của SD1 | 340 | 330 | 960 | 50 |
| SD2-FR3 | Fragment | alt [danh sách không có vé mang mã vé đã nhận (luồng 5a)] | alt | - | Luồng 5a: mã vé không có trong danh sách; tiếp tục bước 8 (vòng lặp); toán hạng 2: [danh sách có vé mang mã vé đã nhận] | 160 | 530 | 840 | 620 |
| SD2-FR4 | Fragment | alt [vé đã huỷ (luồng 5b)] | alt | SD2-FR3 | Luồng 5b, 5c: vé có trong danh sách nhưng không hợp lệ; tiếp tục bước 8 (vòng lặp); toán hạng 2: [vé đã soát (luồng 5c)]; toán hạng 3: [vé hợp lệ] | 170 | 820 | 660 | 290 |
| SD2-FR5 | Fragment | ref SD1: 2.1.3, 2.1.4 (markChecked, showValidTicketResult) | ref | SD2-FR4 | Nhánh vé hợp lệ: tham chiếu message 2.1.3, 2.1.4 của SD1 | 180 | 1030 | 640 | 50 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2-M01 | 2a | SD2-L01 | SD2-L02 | // enterTicketCode (mã vé) | Đồng bộ | SD2-FR1 | 3a |
| SD2-M02 | 2a.1 | SD2-L02 | SD2-L03 | // checkTicket (mã vé) | Đồng bộ | SD2-FR1 | 3a |
| SD2-M03 | 2.1.1 | SD2-L03 | SD2-L04 | // findTicket (mã vé) | Đồng bộ | - | 5 |
| SD2-M04 | 2.1.1 (trả về) | SD2-L04 | SD2-L03 | vé mang mã vé đã nhận trong danh sách, hoặc không có | Trả về | - | 5 |
| SD2-M05 | 2.1.2a | SD2-L03 | SD2-L02 | // showInvalidTicketResult (không hợp lệ, lý do Sai chuyến, mã vé) | Đồng bộ | SD2-FR3 | 5a |
| SD2-M06 | 2.1.2 | SD2-L03 | SD2-L05 | // determineCheckResult | Đồng bộ | SD2-FR3 | 5 |
| SD2-M07 | 2.1.2.1 | SD2-L05 | SD2-L06 | // getSeatCode | Đồng bộ | SD2-FR3 | 5 |
| SD2-M08 | 2.1.2.1 (trả về) | SD2-L06 | SD2-L05 | mã chỗ | Trả về | SD2-FR3 | 5 |
| SD2-M09 | 2.1.2 (trả về) | SD2-L05 | SD2-L03 | kết quả Hợp lệ, Vé đã huỷ hoặc Vé đã soát, mã chỗ, họ tên người đi, thời điểm soát trước nếu có | Trả về | SD2-FR3 | 5 |
| SD2-M10 | 2.1.3b | SD2-L03 | SD2-L02 | // showInvalidTicketResult (không hợp lệ, lý do Vé đã huỷ, mã vé, chỗ) | Đồng bộ | SD2-FR4 | 5b |
| SD2-M11 | 2.1.3c | SD2-L03 | SD2-L02 | // showInvalidTicketResult (không hợp lệ, lý do Vé đã soát, mã vé, chỗ, thời điểm soát trước) | Đồng bộ | SD2-FR4 | 5c |

SD2 có 11 dòng message, trong đó 3 message trả về; 8 message không kể trả về, 2 fragment ngoài cùng (alt SD2-FR1, alt SD2-FR3; SD2-FR4 lồng trong SD2-FR3; SD2-FR2 và SD2-FR5 là ref). Ngưỡng F5: đạt. Sau mỗi nhánh luồng tiếp tục ở bước 8, tức vòng lặp SD1-FR1.

## 6. Quy tắc tương tác giữa các lớp phân tích

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

Đã kiểm tra mọi message của SD1, SD2 và mọi link của communication diagram theo bảng F6: ACT-05 chỉ gửi message tới CheckBoardingTicketForm (1, 3, 2a), ACT-09 chỉ gửi message tới BarcodeScanner (2); boundary chỉ gọi control (CheckBoardingTicketForm --> controller: 1.1, 3.1, 2a.1; BarcodeScanner --> controller: 2.1); control gọi boundary (showCheckSessionInfo, showValidTicketResult, showInvalidTicketResult, showCheckSummary) và entity (Trip, TicketCheckSession, TripPassengerList, Ticket); entity chỉ gọi entity có quan hệ cấu trúc (Trip --> Route, Ticket --> Seat) và gọi chính nó (TicketCheckSession). Không có message giữa hai actor và không có message từ control hoặc entity tới actor. Thao tác quét của ACT-05 không vẽ thành message tới BarcodeScanner vì ACT-05 không là actor của boundary này (ASM-53).

## 7. Communication diagram

File diagrams/P07-communication-UC-015.drawio, phạm vi là luồng chính của SD1 (MUC_CHI_TIET là DAY_DU). Luồng thay thế đã gộp vào SD1 là fragment alt 10a (hai message tự gọi 3.1.1.1, 3.1.1.2 của TicketCheckSession, vẽ thành link tự gọi LK-06). Luồng 3a, 5a, 5b, 5c nằm trên trang SD2 nên không gộp vào communication diagram. Nhãn link dùng STT của SD1; message trả về không vẽ.

a) Bảng Node:

| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| CO-01 | Actor | Phụ xe | - | - | Tác nhân chính | 40 | 300 | 40 | 80 |
| CO-02 | Object | :CheckBoardingTicketForm | boundary | - | Boundary của ACT-05 | 200 | 320 | 200 | 40 |
| CO-03 | Object | :CheckBoardingTicketController | control | - | Control của UC-015 | 640 | 320 | 200 | 40 |
| CO-04 | Object | :TicketCheckSession | entity | - | Được tạo bởi message 1.1.2 | 200 | 580 | 200 | 40 |
| CO-05 | Object | :TripPassengerList | entity | - | Danh sách hành khách của chuyến | 640 | 580 | 200 | 40 |
| CO-06 | Object | :Ticket | entity | - | Vé đang được soát | 1080 | 580 | 200 | 40 |
| CO-07 | Object | :Trip | entity | - | Chuyến cần soát | 200 | 840 | 200 | 40 |
| CO-08 | Object | :Route | entity | - | Tuyến của chuyến | 640 | 840 | 200 | 40 |
| CO-09 | Object | :Seat | entity | - | Chỗ của vé | 1080 | 840 | 200 | 40 |
| CO-10 | Object | :BarcodeScanner | boundary | - | Boundary của ACT-09 | 1080 | 320 | 200 | 40 |
| CO-11 | Actor | Đầu quét mã vạch | - | - | Tác nhân phụ | 1480 | 300 | 40 | 80 |

b) Bảng Edge (link):

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message |
|---|---|---|---|---|---|
| LK-01 | CO-01 | CO-02 | Link | 1: // requestStartCheck (tuyến, giờ xuất bến của chuyến cần soát) (-->)<br>3: // requestEndCheck (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-02 | CO-02 | CO-03 | Link | 1.1: // startCheck (tuyến, giờ xuất bến) (-->)<br>1.1.5: // showCheckSessionInfo (tuyến, giờ xuất bến, số vé còn hiệu lực, số vé đã soát) (<--)<br>2.1.4: // showValidTicketResult (mã vé, chỗ, họ tên người đi) (<--)<br>3.1: // endCheck (-->)<br>3.1.4: // showCheckSummary (tuyến, giờ xuất bến, số vé đã soát, số vé còn hiệu lực chưa soát, trạng thái gửi kết quả) (<--) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-03 | CO-03 | CO-07 | Link | 1.1.1: // findTrip (tuyến, giờ xuất bến) (-->)<br>1.1.3: // getRouteAndDepartureTime (-->)<br>3.1.2: // getRouteAndDepartureTime (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-04 | CO-07 | CO-08 | Link | 1.1.1.1: // checkRouteMatches (tuyến) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-05 | CO-03 | CO-04 | Link | 1.1.2: // startSession (chuyến) (-->)<br>3.1.1: // sendResult (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-06 | CO-04 | CO-04 | Link | 3.1.1.1: // markResultSent (-->)<br>3.1.1.2: // keepResultPending (kết quả soát vé chưa gửi, tự gửi khi máy có sóng trở lại, ASM-52) (-->) | Link tự gọi của TicketCheckSession |
| LK-07 | CO-03 | CO-05 | Link | 1.1.4: // summarizeTicketCounts (chuyến) (-->)<br>2.1.1: // findTicket (mã vé) (-->)<br>3.1.3: // summarizeTicketCounts (chuyến) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-08 | CO-03 | CO-06 | Link | 2.1.2: // determineCheckResult (-->)<br>2.1.3: // markChecked (thời điểm soát) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-09 | CO-06 | CO-09 | Link | 2.1.2.1: // getSeatCode (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-10 | CO-10 | CO-03 | Link | 2.1: // checkTicket (mã vé) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-11 | CO-11 | CO-10 | Link | 2: // readBarcode (mã vạch) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |

Tổng số message trên các link: 23 (bằng số message không phải trả về của SD1: 23). LK-06 là link tự gọi của TicketCheckSession (message 3.1.1.1, 3.1.1.2); không vào VOPC.

## 8. VOPC

File diagrams/P07-class-UC-015.drawio.

a) Bảng Node (lớp):

| ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-B-CheckBoardingTicketForm | Class | CheckBoardingTicketForm | «boundary» | - | departurePoint<br>arrivalPoint<br>departureTime<br>ticketCode | // requestStartCheck<br>// enterTicketCode<br>// requestEndCheck<br>// showCheckSessionInfo<br>// showValidTicketResult<br>// showInvalidTicketResult<br>// showCheckSummary | 40 | 40 | 240 | 280 |
| AC-B-BarcodeScanner | Class | BarcodeScanner | «boundary» | - | ticketCode | // readBarcode | 680 | 40 | 240 | 100 |
| AC-C-CheckBoardingTicketController | Class | CheckBoardingTicketController | «control» | - | - | // startCheck<br>// checkTicket<br>// endCheck | 360 | 420 | 240 | 140 |
| AC-E-TicketCheckSession | Class | TicketCheckSession | «entity» | - | sendStatus | // startSession<br>// sendResult<br>// markResultSent<br>// keepResultPending | 40 | 680 | 240 | 160 |
| AC-E-Trip | Class | Trip | «entity» | - | departureTime | // findTrip<br>// getRouteAndDepartureTime | 360 | 680 | 240 | 120 |
| AC-E-TripPassengerList | Class | TripPassengerList | «entity» | - | - | // findTicket<br>// summarizeTicketCounts | 680 | 680 | 240 | 120 |
| AC-E-Ticket | Class | Ticket | «entity» | - | ticketCode<br>travelerName<br>status<br>checkedTime | // determineCheckResult<br>// markChecked | 1000 | 680 | 240 | 180 |
| AC-E-Route | Class | Route | «entity» | - | departurePoint<br>arrivalPoint | // checkRouteMatches | 360 | 920 | 240 | 120 |
| AC-E-Seat | Class | Seat | «entity» | - | seatCode | // getSeatCode | 1000 | 920 | 240 | 100 |

b) Bảng quan hệ (bảng Edge):

| ID | Lớp A | Lớp B | Loại (Association / Aggregation / Composition / Generalization / Dependency) | Multiplicity | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC015-01 | AC-B-CheckBoardingTicketForm | AC-C-CheckBoardingTicketController | Association | - | tạm thời | LK-02 |
| R-UC015-02 | AC-B-BarcodeScanner | AC-C-CheckBoardingTicketController | Association | - | tạm thời | LK-10 |
| R-UC015-03 | AC-C-CheckBoardingTicketController | AC-E-TicketCheckSession | Association | - | tạm thời | LK-05 |
| R-UC015-04 | AC-C-CheckBoardingTicketController | AC-E-Trip | Association | - | tạm thời | LK-03 |
| R-UC015-05 | AC-C-CheckBoardingTicketController | AC-E-TripPassengerList | Association | - | tạm thời | LK-07 |
| R-UC015-06 | AC-C-CheckBoardingTicketController | AC-E-Ticket | Association | - | tạm thời | LK-08 |
| R-UC015-07 | AC-E-Trip | AC-E-Route | Association | A 0..* - B 1 | chuyến thuộc một tuyến | LK-04; R-UC002-07; GL-04 "Một lần chạy của một tuyến" |
| R-UC015-08 | AC-E-Ticket | AC-E-Seat | Association | A - B 1 | vé của một chỗ | LK-09; R-UC002-15; BR-10; chờ Q-36 cho phía A |
| R-UC015-09 | AC-E-Trip | AC-E-TripPassengerList | Association | - | danh sách hành khách của chuyến | GL-05 "Tập dữ liệu các vé đã phát hành của một chuyến"; ASM-50; không có link trong F7; chờ Q-73 |
| R-UC015-10 | AC-E-TripPassengerList | AC-E-Ticket | Association | A 1 - B 0..* | danh sách gồm các vé của chuyến | GL-05; ASM-33; ASM-50; không có link trong F7 |
| R-UC015-11 | AC-E-TicketCheckSession | AC-E-Trip | Association | A - B 1 | phiên soát vé dành cho một chuyến | GL-28; ASM-32; không có link trong F7 |

Link actor-boundary (LK-01, LK-11) và link tự gọi (LK-06) không vào VOPC. Mỗi link còn lại giữa hai lớp khác nhau của F7 sinh một quan hệ (LK-02 --> R-UC015-01, LK-10 --> R-UC015-02, LK-05 --> R-UC015-03, LK-03 --> R-UC015-04, LK-07 --> R-UC015-05, LK-08 --> R-UC015-06, LK-04 --> R-UC015-07, LK-09 --> R-UC015-08). Ba quan hệ R-UC015-09, R-UC015-10, R-UC015-11 là quan hệ cấu trúc giữa các entity, không có link trong F7 vì không có message giữa các cặp lớp đó; căn cứ ghi ở cột Nguồn (GL-05, GL-28, ASM-32, ASM-33). Multiplicity "-" nghĩa là đặc tả chưa nêu rõ nên để trống; quan hệ giữa boundary, control và entity là quan hệ tạm thời. R-UC015-07 trùng với R-UC002-07, R-UC013-06 và R-UC015-08 trùng với R-UC002-15, R-UC008-06; P08 sẽ gộp. Phía A của R-UC015-08 và R-UC015-11 để trống vì nguồn chỉ nêu phía B (BR-10, ASM-32). Multiplicity "A 1 - B 0..*" của R-UC015-10 suy từ GL-05 (danh sách là tập các vé của một chuyến).

## 9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) và tác nhân |
|---|---|---|
| 1 | SD1: 1, 1.1 | ACT-05, AC-B-CheckBoardingTicketForm, AC-C-CheckBoardingTicketController |
| 2 | SD1: 1.1.1, 1.1.1.1, 1.1.1 (trả về), 1.1.2, 1.1.3, 1.1.3 (trả về), 1.1.4, 1.1.4 (trả về), 1.1.5 | AC-C-CheckBoardingTicketController, AC-E-Trip, AC-E-Route, AC-E-TicketCheckSession, AC-E-TripPassengerList, AC-B-CheckBoardingTicketForm |
| 3 | SD1: 2; SD2: ref SD2-FR2 | ACT-09, AC-B-BarcodeScanner |
| 3a | SD2: 2a, 2a.1, fragment alt SD2-FR1 | ACT-05, AC-B-CheckBoardingTicketForm, AC-C-CheckBoardingTicketController |
| 4 | SD1: 2, 2.1; SD2: ref SD2-FR2 | ACT-09, AC-B-BarcodeScanner, AC-C-CheckBoardingTicketController |
| 5 | SD1: 2.1.1, 2.1.1 (trả về), 2.1.2, 2.1.2.1, 2.1.2.1 (trả về), 2.1.2 (trả về); SD2: 2.1.1, 2.1.1 (trả về), 2.1.2, 2.1.2.1, 2.1.2.1 (trả về), 2.1.2 (trả về) | AC-C-CheckBoardingTicketController, AC-E-TripPassengerList, AC-E-Ticket, AC-E-Seat |
| 5a | SD2: 2.1.2a, fragment alt SD2-FR3 | AC-C-CheckBoardingTicketController, AC-E-TripPassengerList, AC-B-CheckBoardingTicketForm |
| 5b | SD2: 2.1.3b, fragment alt SD2-FR4 | AC-C-CheckBoardingTicketController, AC-E-TripPassengerList, AC-E-Ticket, AC-E-Seat, AC-B-CheckBoardingTicketForm |
| 5c | SD2: 2.1.3c, fragment alt SD2-FR4 | AC-C-CheckBoardingTicketController, AC-E-TripPassengerList, AC-E-Ticket, AC-E-Seat, AC-B-CheckBoardingTicketForm |
| 6 | SD1: 2.1.3; SD2: ref SD2-FR5 | AC-C-CheckBoardingTicketController, AC-E-Ticket |
| 7 | SD1: 2.1.4; SD2: ref SD2-FR5 | AC-C-CheckBoardingTicketController, AC-B-CheckBoardingTicketForm |
| 8 | SD1: fragment loop SD1-FR1 | AC-C-CheckBoardingTicketController |
| 9 | SD1: 3, 3.1 | ACT-05, AC-B-CheckBoardingTicketForm, AC-C-CheckBoardingTicketController |
| 10 | SD1: 3.1.1, 3.1.1.1, 3.1.1 (trả về) | AC-C-CheckBoardingTicketController, AC-E-TicketCheckSession |
| 10a | SD1: 3.1.1.2, fragment alt SD1-FR2 | AC-E-TicketCheckSession |
| 11 | SD1: 3.1.2, 3.1.2 (trả về), 3.1.3, 3.1.3 (trả về), 3.1.4 | AC-C-CheckBoardingTicketController, AC-E-Trip, AC-E-TripPassengerList, AC-B-CheckBoardingTicketForm |

## 10. File .drawio

| File | Trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-015.drawio | SD1, SD2 | Bảng F5; ID cell là ID trong bảng lifeline, fragment, message |
| diagrams/P07-communication-UC-015.drawio | COMM1 | Bảng F7; ID cell là ID trong bảng Node và Edge |
| diagrams/P07-class-UC-015.drawio | VOPC1 | Bảng F8; ID cell của lớp là mã AC, của cạnh là ID quan hệ, nhãn multiplicity là cell con của cạnh |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-73 | Danh sách hành khách của chuyến trên máy soát vé là bản sao dữ liệu vé tại thời điểm gửi, hay là chính dữ liệu vé của hệ thống được đồng bộ về máy? Trạng thái đã soát ghi trên máy có thuộc cùng đối tượng vé với trạng thái huỷ của vé không? (Bản sao riêng trên máy, đồng bộ về hệ thống khi kết thúc soát vé / Cùng một dữ liệu vé) | AC-E-TripPassengerList, AC-E-Ticket, AC-E-TicketCheckSession; ASM-50; message 1.1.4, 2.1.1, 2.1.3 (SD1); P07 của UC-014; P08 gộp lớp | Mục 8, câu 3: "gửi lại kết quả khi có sóng"; Mục 8, câu 4: "hệ thống gửi danh sách hành khách của chuyến về máy soát vé" (không nêu danh sách là bản sao hay dữ liệu dùng chung) |
| Q-74 | Khi kết quả soát vé của chuyến về tới dữ liệu vé của hệ thống (bước 10), hệ thống dùng kết quả đó vào việc gì? (Đánh dấu vé đã soát trên dữ liệu vé của hệ thống để các use case khác biết, ví dụ vé đã soát còn được trả hay đổi không / Chỉ lưu kết quả để tra cứu) | Bước 10; AC-E-TicketCheckSession (sendResult); message 3.1.1 (SD1); ASM-51; UC-007, UC-008, UC-018 | Mục 8, câu 3: "gửi lại kết quả khi có sóng" (không nêu hệ thống làm gì với kết quả nhận được) |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-50 | Danh sách hành khách của chuyến (GL-05) là một entity AC-E-TripPassengerList, nắm tập vé của một chuyến trên máy soát vé, trả lời vé có mã vé đã nhận có thuộc chuyến không (findTicket) và đếm số vé còn hiệu lực, đã soát, chưa soát (summarizeTicketCounts). Mã vé không có trong danh sách là vé không thuộc chuyến (BR-20). | GL-05 là thuật ngữ riêng; ASM-33 nói kiểm tra theo danh sách trên máy; Trip không biết dữ liệu riêng trên máy. Chờ Q-73, Q-45 | AC-E-TripPassengerList; message 1.1.4, 2.1.1, 3.1.3 (SD1); bước 2, 5, 5a, 11; R-UC015-09, R-UC015-10 |
| ASM-51 | Phiên soát vé (GL-28) là một entity AC-E-TicketCheckSession gắn với một chuyến (ASM-32), được tạo ở bước 2 khi phụ xe chọn chuyến. Phiên giữ trạng thái gửi kết quả (Đã gửi, Chờ gửi khi có sóng) và gửi kết quả soát vé của chuyến về dữ liệu vé của hệ thống ở bước 10. | Kết quả chưa gửi khi máy mất sóng tồn tại lâu hơn một lần thực hiện use case (luồng 10a), nên hệ thống phải quản lý thông tin đó (A4). P04 không nêu thời điểm bắt đầu phiên nên phiên không có thuộc tính thời gian. Chờ Q-46, Q-74 | AC-E-TicketCheckSession; message 1.1.2, 3.1.1 (SD1); bước 2, 10, 10a |
| ASM-52 | Việc tự gửi kết quả soát vé khi máy có sóng trở lại (luồng 10a) là đồng bộ nội bộ của ứng dụng soát vé, diễn ra sau khi use case kết thúc và không có message trong sơ đồ; luồng 10a chỉ thể hiện bằng message tự gọi keepResultPending của TicketCheckSession. Mức phân tích không chọn cơ chế đồng bộ; P12 thiết kế. | P04 Mục 8 và P02 CAND-46 coi đây là đồng bộ nội bộ (ASM-01), không có tác nhân và không có thời hạn. Chờ Q-46 | AC-E-TicketCheckSession (keepResultPending); message 3.1.1.2 (SD1); luồng 10a |
| ASM-53 | Bước 3 (phụ xe quét mã vạch) và bước 4 (đầu quét đọc mã vạch) thể hiện bằng một message readBarcode từ ACT-09 tới BarcodeScanner. Thao tác vật lý của phụ xe trên đầu quét không vẽ thành message ACT-05 --> BarcodeScanner. | F6 chỉ cho boundary trao đổi với actor của nó; ACT-05 có boundary riêng là CheckBoardingTicketForm. Bước 3 và 4 cùng thể hiện một lần đọc mã vạch nên message readBarcode mang cả hai bước | AC-B-BarcodeScanner; message 2 (SD1); bước 3, 4 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 (UC-015) | Dữ liệu vào 1, bước 1, 2 | Điều kiện hợp lệ của Dữ liệu vào 1 là chuyến đã có danh sách hành khách trên máy, nhưng đặc tả không có luồng ngoại lệ khi phụ xe chọn chuyến chưa có danh sách (ví dụ chưa tới mốc 15 phút của UC-014) hoặc không có chuyến khớp tuyến và giờ xuất bến. SD1 không có nhánh xử lý nên phiên không thể mở. | Thêm luồng ngoại lệ ở bước 2 báo không mở được phiên soát vé khi chuyến không có danh sách trên máy, hoặc ghi rõ phụ xe chỉ chọn trong các chuyến đã có danh sách. |
| P04 (UC-015) | Bước 3, 4 | Bước 3 (phụ xe quét) và bước 4 (đầu quét đọc) là hai bước cho một thao tác vật lý, khiến bước 3 phải có tương tác giữa hai tác nhân hoặc giữa phụ xe và boundary thiết bị mà F6 không cho. | Gộp thành một bước do đầu quét thực hiện, hoặc ghi chú bước 3 là thao tác vật lý không có tương tác với hệ thống. |
| P04 (UC-015) | Bước 10, hậu điều kiện | Đặc tả không nêu hệ thống dùng kết quả soát vé nhận được vào việc gì (Q-74) và UC-007, UC-008 không kiểm tra vé đã soát. | Bổ sung tác dụng của kết quả soát vé (ví dụ vé đã soát không được trả, đổi) hoặc ghi rõ chỉ lưu, sau khi Q-74 được trả lời. |

## Vấn đề còn mở


- Target 14 đạt một phần: C7.3 yêu cầu cạnh không cắt qua node và không có hai node chồng nhau, nhưng trong sequence diagram message đi qua các lifeline ở giữa và fragment phủ lên lifeline theo ký pháp UML (F10). Communication diagram và VOPC thoả C7.3 về toạ độ bội số 10 và khoảng cách giữa node từ 40; nhãn link dài của communication diagram có thể chồng lên hình node kề hoặc lên nhau khi mở bằng draw.io, cần chỉnh tay.
- Chọn giữa hai quy tắc (C9): A3 nói thao tác vật lý đi vào hệ thống qua boundary thiết bị, còn F6 nói boundary chỉ trao đổi với actor của nó. ACT-05 vừa có boundary giao diện người dùng vừa quét vé trên đầu quét của ACT-09. Đã chọn một message readBarcode từ ACT-09 cho bước 3 và 4, không vẽ message ACT-05 --> BarcodeScanner (ASM-53) và đề xuất sửa P04.
- Chọn giữa hai quy tắc (C9): F5 yêu cầu vẽ mỗi luồng cần vẽ một trang (mục 2) nhưng A6 cho vẽ luồng ngắn trong cùng sơ đồ bằng fragment. Đã vẽ 10a trong SD1 (alt, 2 message), còn 3a, 5a, 5b, 5c ở SD2 vì thêm vào SD1 sẽ vượt ngưỡng khoảng 30 message mỗi trang. Luồng 3a, 5a, 5b, 5c vì vậy không vào communication diagram (F7 chỉ gộp luồng đã gộp vào SD1).
- Chọn giữa hai quy tắc (C9): F5 nêu ngưỡng khoảng 30 message mỗi trang; SD1 có 32 dòng gồm 9 message trả về, tức 23 message không kể trả về, nên đếm không kể trả về thì đạt (cách đếm như P07 của UC-013).
- Chọn giữa hai quy tắc (C9): F5 yêu cầu message đầu tiên ở y=120 và cách nhau 40 (F10), nhưng nhãn fragment, đường ngăn toán hạng và ref cần chỗ. Trang SD2 bắt đầu message đầu tiên ở y=160, quanh fragment và ref khoảng cách giữa các message lớn hơn 40.
- Target 9 đạt một phần: Seat chỉ có getSeatCode (cung cấp dữ liệu), Trip có findTrip là hành vi nhưng getRouteAndDepartureTime chỉ cung cấp dữ liệu, Route chỉ có checkRouteMatches; đặc tả UC-015 không nêu hành vi nào khác trên chỗ, chuyến, tuyến. P08 sẽ gộp thêm trách nhiệm từ các use case khác.
- Chạy khi chưa có P07 của UC-014: AC-E-TripPassengerList và AC-E-TicketCheckSession do UC-015 đặt mã và thuộc tính; UC-014 (chuẩn bị và gửi danh sách) phải tái dùng đúng mã AC-E-TripPassengerList và đối chiếu với Q-73. Ghi chú: ranh giới giữa máy soát vé và phần còn lại của hệ thống (ASM-01) chưa được chọn ở mức phân tích, nên bước 10 chỉ có message sendResult của TicketCheckSession mà chưa có lớp nhận phía hệ thống (Q-74).
- Chạy với giả định: hậu điều kiện (Q-45, Q-46, Q-47), nội dung danh sách hành khách (ASM-33, Q-11) và cách vé mua trực tuyến được soát (ASM-34, Q-04) vẫn là câu hỏi mở của P04; P07 dùng ASM-32 đến ASM-36 của P04. Thứ tự kiểm tra trong determineCheckResult là đã huỷ trước đã soát theo Q-47. Mã vé sau khi đổi vé (Q-30) ảnh hưởng tới việc Ticket cũ báo Vé đã huỷ hay Sai chuyến (ASM-36). Q-54 (model máy soát vé và loại mã vạch) chưa trả lời nên BarcodeScanner chỉ ở mức phân tích.
- Trách nhiệm checkTicket của CheckBoardingTicketController được gọi từ hai boundary (BarcodeScanner ở message 2.1, CheckBoardingTicketForm ở message 2a.1); P08 giữ một trách nhiệm. showInvalidTicketResult dùng chung cho ba lý do, phân biệt bằng tham số lý do (BR-20, BR-21, BR-22).
- Target 15 không áp dụng: UC-015 không dùng thời hạn nội bộ và không tạo, đổi, kết thúc mốc thời gian mà use case do ACT-10 kích hoạt phụ thuộc vào (xem F1, dòng Tác nhân thời gian).

