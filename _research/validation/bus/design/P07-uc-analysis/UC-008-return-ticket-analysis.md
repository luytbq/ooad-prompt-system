# P07 - Phân tích use case UC-008 Trả vé - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P04-uc-specs/UC-008-return-ticket.md 1.0; P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P02-usecases.md 1.1; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0 (sổ đăng ký AC). UC-008 không có use case được include hoặc extend nên không cần đặc tả P04 nào khác |
| Phạm vi | UC-008 |

Quy ước trích nguồn: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md; "Dữ liệu vào n", "Dữ liệu ra n" chỉ bảng dữ liệu của P04 UC-008. Tham số bước: LUONG_CAN_VE = Không có (vẽ mọi luồng); YEU_CAU_BO_SUNG = Không có.

## 1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-008 Trả vé (Return Ticket) |
| Tác nhân chính (ACT, loại) | ACT-01 Hành khách (Người), tác nhân của vé mua trực tuyến; ACT-02 Nhân viên bán vé (Người), tác nhân của vé mua tại quầy (RL-11, RL-12) |
| Tác nhân phụ (ACT, loại) | ACT-06 Cổng thanh toán (Hệ thống ngoài), tương tác trực tiếp ở bước 8, 9 (RL-13) |
| Include (UC) | Không có |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2 không có điểm mở rộng của UC-008) |
| Tác nhân thời gian | ACT-10 Bộ định thời không kích hoạt UC-008 và không tương tác với UC-008. Xem Vấn đề còn mở về mốc thời gian phụ thuộc dữ liệu (A2) |
| File P07 đã có được dùng làm sổ đăng ký AC | UC-002-book-ticket-online-analysis.md. Sổ AC: AC-B-BookTicketForm (boundary), AC-B-SmsGateway (boundary), AC-C-BookTicketOnlineController (control), AC-C-PayTicketOnlineController (control, tạm chờ UC-003), AC-E-Trip, AC-E-Route, AC-E-Seat, AC-E-Booking, AC-E-Ticket, AC-E-BaseFare, AC-E-HolidaySurcharge (entity). UC-008 tái dùng AC-E-Trip, AC-E-Seat, AC-E-Ticket |

## 2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Hành khách / Nhân viên bán vé | Yêu cầu trả vé và cung cấp thông tin nhận diện vé (xem Dữ liệu vào 1). | Không đổi | Dữ liệu vào 1; REQ-29 |
| 2 | Hệ thống | Kiểm tra có vé khớp thông tin đã cung cấp (ASM-18) và vé chưa bị huỷ (ASM-20). | Hệ thống tìm vé có mã vé đã cung cấp và, khi hành khách yêu cầu, có số điện thoại người đi trùng số điện thoại người đi ghi trên vé (ASM-18). Vé tìm được được kiểm tra trạng thái: vé ở trạng thái đã huỷ không được trả (ASM-20). | ASM-18, ASM-20; GL-22, GL-37, GL-39; REQ-18 |
| 2a | Hệ thống | Điều kiện: không có vé nào khớp thông tin đã cung cấp (ASM-18). Thông báo không tìm thấy vé khớp thông tin đã cung cấp. Quay lại bước 1. | Hệ thống xác định không có vé nào khớp mã vé (và số điện thoại người đi khi hành khách yêu cầu) và thông báo cho tác nhân để cung cấp lại thông tin. | ASM-18; GL-22 |
| 2b | Hệ thống | Điều kiện: có vé khớp và vé đã bị huỷ (ASM-20). Từ chối yêu cầu trả vé và thông báo vé đã bị huỷ. Kết thúc use case (thất bại). | Hệ thống xác định vé khớp đang ở trạng thái đã huỷ, từ chối yêu cầu và thông báo vé đã bị huỷ; vé và chỗ của vé giữ nguyên. | ASM-20; GL-39 |
| 3 | Hệ thống | Kiểm tra vé được trả qua đúng kênh đã mua (BR-11) và thời gian còn lại trước giờ xuất bến của chuyến từ 4 giờ trở lên (BR-12, ASM-23). | Hệ thống so sánh kênh mua của vé với kênh yêu cầu trả, suy ra từ tác nhân thực hiện: hành khách là Trực tuyến, nhân viên bán vé là Tại quầy (BR-11, ASM-45). Hệ thống lấy từ chuyến của vé thời gian còn lại từ thời điểm trả tới giờ xuất bến và so với 4 giờ (BR-12); thời gian còn lại này được dùng lại ở bước 4 (ASM-23). | BR-11, BR-12; GL-13, GL-34, GL-10; ASM-23, ASM-45; REQ-33 |
| 3a | Hệ thống | Điều kiện: vé được mua qua kênh khác với kênh đang yêu cầu trả (BR-11). Từ chối yêu cầu trả vé và thông báo quy tắc bị vi phạm (BR-11). Kết thúc use case (thất bại). | Hệ thống phát hiện kênh mua của vé khác kênh yêu cầu trả, từ chối yêu cầu và thông báo quy tắc BR-11; vé giữ nguyên. | BR-11; GL-13 |
| 3b | Hệ thống | Điều kiện: vé được trả qua đúng kênh đã mua và thời gian còn lại dưới 4 giờ (BR-12). Từ chối yêu cầu trả vé và thông báo quy tắc bị vi phạm (BR-12). Kết thúc use case (thất bại). | Hệ thống phát hiện thời gian còn lại trước giờ xuất bến của chuyến dưới 4 giờ, từ chối yêu cầu và thông báo quy tắc BR-12; vé giữ nguyên. | BR-12; GL-34 |
| 4 | Hệ thống | Tính số tiền hoàn của vé theo mức hoàn ứng với thời gian còn lại trước giờ xuất bến (BR-13, BR-14, ASM-22). | Từ thời gian còn lại đã xác định ở bước 3, vé xác định mức hoàn 90% khi từ 24 giờ trở lên (BR-13) hoặc 50% khi từ 4 giờ đến dưới 24 giờ (BR-14). Số tiền hoàn bằng giá vé nhân mức hoàn, với giá vé là số tiền đã thanh toán cho vé khi mua (ASM-22). | BR-13, BR-14; GL-08, GL-24; ASM-22, ASM-23; REQ-31, REQ-32 |
| 5 | Hệ thống | Hiển thị thông tin vé, mức hoàn và số tiền hoàn (xem Dữ liệu ra 1) (ASM-19). | Hệ thống lấy mã vé và giá vé từ vé, tuyến và giờ xuất bến từ chuyến của vé, mã chỗ từ chỗ của vé. Hệ thống hiển thị các thông tin đó cùng thời gian còn lại, mức hoàn và số tiền hoàn cho tác nhân (ASM-19). | Dữ liệu ra 1; ASM-19; GL-02, GL-08, GL-22, GL-24; REQ-42 |
| 6 | Hành khách / Nhân viên bán vé | Xác nhận trả vé (ASM-19). | Không đổi | ASM-19 |
| 6a | Hệ thống | Điều kiện: tác nhân không xác nhận trả vé với số tiền hoàn đã hiển thị (ASM-19). Thông báo yêu cầu trả vé đã được huỷ và vé giữ nguyên hiệu lực. Kết thúc use case (thất bại). | Hệ thống kết thúc yêu cầu trả vé khi tác nhân không xác nhận, thông báo yêu cầu đã được huỷ; vé, chỗ của vé không đổi và không có khoản hoàn nào được ghi nhận. | ASM-19, ASM-21 |
| 7 | Hệ thống | Xác định hình thức hoàn theo kênh mua của vé (BR-15, BR-16). | Hệ thống lấy kênh mua của vé: vé mua trực tuyến có hình thức hoàn Qua cổng thanh toán (BR-15), vé mua tại quầy có hình thức hoàn Tiền mặt tại quầy (BR-16). | BR-15, BR-16; GL-13, GL-16 |
| 7a | - | Điều kiện: vé được mua tại quầy, gồm vé đặt qua điện thoại đã thanh toán tại quầy (BR-16). Tiếp tục bước 10. | Hệ thống bỏ qua việc hoàn qua Cổng thanh toán vì hình thức hoàn là Tiền mặt tại quầy, chuyển sang bước 10. | BR-16 |
| 8 | Hệ thống | Gửi yêu cầu hoàn số tiền hoàn của vé tới Cổng thanh toán (BR-15). | Hệ thống gửi mã vé và số tiền hoàn tới Cổng thanh toán qua giao diện hệ thống của cổng; hệ thống không lưu thông tin thẻ (NFR-03). | BR-15; NFR-07; GL-16 |
| 9 | Cổng thanh toán | Trả về kết quả hoàn tiền. | Không đổi | NFR-07 |
| 9a | Hệ thống | Điều kiện: Cổng thanh toán trả về kết quả hoàn tiền không thành công. Thông báo hoàn tiền không thành công và vé chưa được trả (ASM-21). Kết thúc use case (thất bại). | Hệ thống nhận kết quả hoàn tiền không thành công, thông báo cho tác nhân; vé không bị huỷ, chỗ của vé không đổi và không có khoản hoàn nào được ghi nhận (ASM-21). | ASM-21; NFR-07 |
| 10 | Hệ thống | Huỷ vé, trả chỗ của vé về trạng thái còn trống (BR-03, ASM-20) và ghi nhận khoản hoàn tiền của vé. | Vé chuyển sang trạng thái đã huỷ và yêu cầu chỗ của vé trở lại còn trống (BR-03, ASM-20). Vé tạo khoản hoàn tiền gắn với vé, ghi mức hoàn, số tiền hoàn, hình thức hoàn và kết quả hoàn (ASM-46). | BR-03, BR-13, BR-14, BR-15, BR-16; GL-16, GL-39; ASM-20, ASM-46 |
| 11 | Hệ thống | Thông báo trả vé thành công kèm số tiền hoàn và hình thức hoàn (xem Dữ liệu ra 2). | Hệ thống thông báo cho tác nhân mã vé, trạng thái vé là đã huỷ, số tiền hoàn và hình thức hoàn. Với vé mua tại quầy, việc nhân viên bán vé chi tiền mặt diễn ra ngoài hệ thống. | Dữ liệu ra 2; BR-15, BR-16 |

## 3. Tìm lớp phân tích

### 3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-01 Hành khách | Người | ReturnTicketForm (AC-B-ReturnTicketForm) | Giao diện người dùng | Mới | Một boundary cho cặp (ACT-01, UC-008) gom mọi tương tác của hành khách: nhập mã vé và số điện thoại người đi, xem thông tin vé và mức hoàn, xác nhận hoặc không xác nhận, nhận các thông báo. Tên theo hành động của use case với hậu tố Form (HAU_TO_TEN_LOP là Mặc định) |
| ACT-02 Nhân viên bán vé | Người | CounterReturnTicketForm (AC-B-CounterReturnTicketForm) | Giao diện người dùng | Mới | Một boundary cho cặp (ACT-02, UC-008). Tách khỏi ReturnTicketForm vì mỗi cặp tác nhân và use case có một boundary riêng; thông tin nhập chỉ có mã vé (vé giấy), không có số điện thoại người đi (ASM-18). Boundary giao diện người dùng không dùng chung giữa hai tác nhân |
| ACT-06 Cổng thanh toán | Hệ thống ngoài | PaymentGateway (AC-B-PaymentGateway) | Giao diện hệ thống | Mới | Tên theo hệ thống, không hậu tố (HAU_TO_TEN_LOP là Mặc định); không trùng tên entity nào nên không cần hậu tố Gateway bắt buộc. ACT-06 tương tác trực tiếp ở bước 8, 9 của UC-008 nên boundary được đặt mã tại đây; UC-003 Thanh toán vé trực tuyến (chưa có P07) phải tái dùng đúng mã AC-B-PaymentGateway và bổ sung trách nhiệm thanh toán |

ACT-10 Bộ định thời không tham gia UC-008 nên không có boundary. Số boundary là 3, bằng số tác nhân tham gia.

### 3.2 Bảng lọc danh từ


| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Hành khách | Mô tả; bước 1, 6, 6a | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01, có boundary ReturnTicketForm |
| 2 | Nhân viên bán vé | Mô tả; bước 1, 6, 6a; tiền điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | ACT-02, có boundary CounterReturnTicketForm |
| 3 | Cổng thanh toán | Bước 8, 9, 9a | Loại - là tác nhân hoặc ngoài phạm vi | ACT-06, có boundary PaymentGateway |
| 4 | Hệ thống | Mọi bước hệ thống | Loại - mơ hồ | Chỉ là chủ ngữ của bước, không chỉ một khái niệm dữ liệu cụ thể |
| 5 | Khách (khách mang vé mua tại quầy) | Mô tả ngắn; sự kiện kích hoạt EV-12 | Loại - là tác nhân hoặc ngoài phạm vi | GL-15 là bên liên quan SH-07, không là tác nhân; không tự thao tác với hệ thống |
| 6 | Yêu cầu trả vé | Bước 1, 2b, 3a, 3b, 6a | Loại - thao tác hoặc sự kiện | Là hành động của tác nhân (requestReturnTicket), kết quả không lưu quá một lần thực hiện |
| 7 | Thông tin nhận diện vé, thông tin đã cung cấp | Bước 1, 2, 2a; Dữ liệu vào 1 | Loại - trùng hoặc đồng nghĩa với mã vé, số điện thoại người đi | Gọi chung hai trường của Dữ liệu vào 1 |
| 8 | Vé | Bước 1, 2, 2a, 2b, 3, 5, 10; BR-10, BR-11 đến BR-14 | Entity (AC-E-Ticket) | GL-37; hệ thống lưu vé, kiểm tra trạng thái và kênh mua, tính số tiền hoàn, chuyển trạng thái sang đã huỷ; tái dùng mã từ UC-002 |
| 9 | Mã vé | Bước 1, 2a; Dữ liệu vào 1 #1; Dữ liệu ra 1 #1; Dữ liệu ra 2 #1; BR-10 | Loại - thuộc tính của Ticket | ticketCode; GL-22 |
| 10 | Số điện thoại người đi | Bước 1, 2a; Dữ liệu vào 1 #2 | Loại - thuộc tính của Ticket | travelerPhone; ASM-18 |
| 11 | Người đi | Bước 1 (qua số điện thoại người đi) | Loại - là tác nhân hoặc ngoài phạm vi | GL-26 là bên liên quan SH-03, không là tác nhân; chỉ họ tên và số điện thoại là thuộc tính của Ticket |
| 12 | Trạng thái vé (đã huỷ) | Bước 2, 2b, 10; Dữ liệu ra 2 #2; hậu điều kiện | Loại - thuộc tính của Ticket | status; GL-39 Vé đã huỷ là một giá trị |
| 13 | Kênh mua, kênh trả vé, kênh yêu cầu trả | Bước 3, 3a, 7; BR-11, BR-15, BR-16 | Loại - thuộc tính của Ticket | purchaseChannel; GL-13 ghi kênh mua là đặc điểm của một vé với hai giá trị Trực tuyến, Tại quầy; kênh yêu cầu trả suy từ tác nhân (ASM-45) nên chỉ là tham số của message |
| 14 | Website | BR-11 | Loại - trùng hoặc đồng nghĩa với kênh mua giá trị Trực tuyến | Kênh giao diện của chính hệ thống (P01 Mục 4) |
| 15 | Quầy bán vé, quầy | Mô tả; BR-11, BR-16 | Loại - trùng hoặc đồng nghĩa với kênh mua giá trị Tại quầy | GL-29 ứng với giá trị Tại quầy của GL-13 |
| 16 | Vé đặt qua điện thoại đã thanh toán tại quầy | Luồng 7a; BR-11 | Loại - trùng hoặc đồng nghĩa với vé có kênh mua Tại quầy | BR-11 xếp vào kênh mua tại quầy; không còn là đặt chỗ qua điện thoại (GL-07) |
| 17 | Chuyến | Bước 3, 4, 5; Dữ liệu ra 1 #2; BR-12, BR-13, BR-14 | Entity (AC-E-Trip) | GL-04; hệ thống lưu chuyến và Trip tính thời gian còn lại trước giờ xuất bến từ giờ xuất bến của chính nó; tái dùng mã từ UC-002 |
| 18 | Giờ xuất bến | Bước 3, 4; Dữ liệu ra 1 #2, #5; BR-12 đến BR-14 | Loại - thuộc tính của Trip | departureTime; GL-10 |
| 19 | Tuyến, điểm đi, điểm đến | Dữ liệu ra 1 #2 | Loại - không tham gia hành vi của use case này (khái niệm của UC-002) | Tuyến chỉ hiện trong nhãn "Tuyến và giờ xuất bến" do Trip cung cấp (getRouteAndDepartureTime); UC-008 không đọc hay kiểm tra Route |
| 20 | Tuyến và giờ xuất bến | Dữ liệu ra 1 #2 | Loại - trùng hoặc đồng nghĩa với tuyến, giờ xuất bến | Gọi chung hai khái niệm đã xét |
| 21 | Thời gian còn lại trước giờ xuất bến | Bước 3, 3b, 4; Dữ liệu ra 1 #5; BR-12 đến BR-14 | Loại - thuộc tính của Trip | Giá trị suy ra từ departureTime và thời điểm trả (calculateTimeToDeparture); GL-34 |
| 22 | Thời điểm trả vé | Bước 3, 4; ASM-23 | Loại - thao tác hoặc sự kiện | Thời điểm hệ thống kiểm tra ở bước 3, chỉ là tham số của message (Q-39) |
| 23 | 4 giờ, 24 giờ | Bước 3, 3b; BR-12, BR-13, BR-14 | Loại - tham số của quy tắc BR-12, BR-13, BR-14 | Ngưỡng nằm trong quy tắc |
| 24 | Mức hoàn (90%, 50%) | Bước 4, 5; Dữ liệu ra 1 #6; BR-13, BR-14 | Loại - thuộc tính của Refund | refundRate; GL-24. Giá trị 90% và 50% là tham số của BR-13, BR-14 |
| 25 | Giá vé | Bước 4; Dữ liệu ra 1 #4; BR-13, BR-14 | Loại - thuộc tính của Ticket | price; GL-08; là số tiền đã thanh toán khi mua (ASM-22) |
| 26 | Số tiền hoàn | Bước 4, 5, 8; Dữ liệu ra 1 #7; Dữ liệu ra 2 #3 | Loại - thuộc tính của Refund | refundAmount; GL-16 |
| 27 | Khoản hoàn tiền | Bước 10; hậu điều kiện | Entity (AC-E-Refund) | GL-16; hệ thống ghi nhận và lưu khoản hoàn của vé đã trả sau lần thực hiện use case (ASM-46) |
| 28 | Hình thức hoàn | Bước 7, 11; Dữ liệu ra 2 #4 | Loại - thuộc tính của Refund | refundMethod; hai giá trị Qua cổng thanh toán, Tiền mặt tại quầy theo BR-15, BR-16 |
| 29 | Kết quả hoàn tiền, kết quả hoàn | Bước 9, 9a | Loại - thuộc tính của Refund | refundResult; GL-16 ghi kết quả hoàn là thành phần của khoản hoàn |
| 30 | Tiền mặt | Bước 7, 11; BR-16 | Loại - thuộc tính của Refund | Giá trị của hình thức hoàn (Tiền mặt tại quầy) |
| 31 | Yêu cầu hoàn tiền | Bước 8 | Loại - thao tác hoặc sự kiện | Message requestRefund tới PaymentGateway, hệ thống không lưu |
| 32 | Chỗ, chỗ của vé | Bước 10; Dữ liệu ra 1 #3; BR-03 | Entity (AC-E-Seat) | GL-02; có trạng thái đổi trong use case (trả về còn trống) và hành vi release; tái dùng mã từ UC-002 |
| 33 | Mã chỗ | Dữ liệu ra 1 #3 | Loại - thuộc tính của Seat | seatCode |
| 34 | Chỗ còn trống, trạng thái chỗ | Bước 10; BR-03 | Loại - thuộc tính của Seat | status của Seat, suy ra theo BR-03 với "chưa có vé" hiểu là chưa có vé còn hiệu lực (ASM-20) |
| 35 | Sơ đồ xe | Dữ liệu ra 1 #3 ("theo sơ đồ xe") | Loại - không tham gia hành vi của use case này (khái niệm của UC-012) | Chỉ nêu cách đặt mã chỗ; UC-008 không đọc hay ghi xe hay sơ đồ |
| 36 | Tài khoản | Mục 8 của P04 (Q-35) | Loại - không tham gia hành vi của use case này (khái niệm của UC-009, UC-010) | Use case không đọc, ghi hay kiểm tra tài khoản (ASM-18) |
| 37 | Phiên làm việc, xác thực | Tiền điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | Điều kiện đã có trước use case (ASM-09), không có hành vi trong UC-008 |
| 38 | Chuyến bị huỷ, vé của chuyến bị huỷ | Luồng 2b | Loại - thuộc phân tích của UC-013 | UC-013 Huỷ chuyến tạo ra trạng thái đã huỷ và hoàn 100% (BR-17); UC-008 chỉ gặp vé ở trạng thái đã huỷ |
| 39 | Thông báo, quy tắc bị vi phạm | Bước 2a, 2b, 3a, 3b, 6a, 9a, 11 | Loại - thao tác hoặc sự kiện | Là việc hiển thị của boundary (các message show...Notice); nội dung thông điệp thuộc P11a |
| 40 | Quy tắc bị vi phạm (BR-11, BR-12) | Bước 3a, 3b | Loại - mơ hồ | Chỉ mã BR, được ghi ngay trong message tương ứng |


### 3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| ReturnTicketController (AC-C-ReturnTicketController) | UC-008 Trả vé | Mới | Một control cho use case, đặt tên theo tên tiếng Anh của use case (Return Ticket) với hậu tố Controller (HAU_TO_TEN_LOP là Mặc định). Điều phối trình tự 11 bước cho cả hai tác nhân chính, không giữ dữ liệu nghiệp vụ lâu dài |

### 3.4 Bảng lớp phân tích


| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-ReturnTicketForm | boundary | ReturnTicketForm | // requestReturnTicket: nhận yêu cầu trả vé và thông tin nhận diện vé từ tác nhân<br>// confirmReturnTicket: nhận xác nhận trả vé của tác nhân<br>// declineReturnTicket: nhận việc tác nhân không xác nhận trả vé<br>// showReturnInfo: hiển thị thông tin vé, thời gian còn lại, mức hoàn và số tiền hoàn<br>// showTicketNotFoundNotice: thông báo không tìm thấy vé khớp thông tin đã cung cấp<br>// showTicketCancelledNotice: thông báo vé đã bị huỷ<br>// showWrongChannelNotice: thông báo vé mua qua kênh khác kênh yêu cầu trả (BR-11)<br>// showReturnTimeLimitNotice: thông báo còn dưới 4 giờ trước giờ xuất bến (BR-12)<br>// showReturnAbortedNotice: thông báo yêu cầu trả vé đã được huỷ, vé giữ nguyên<br>// showRefundFailedNotice: thông báo hoàn tiền không thành công, vé chưa được trả<br>// showReturnResult: hiển thị kết quả trả vé gồm trạng thái vé, số tiền hoàn, hình thức hoàn | ticketCode, travelerPhone | 1, 2a, 2b, 3a, 3b, 5, 6, 6a, 9a, 11 | Giao diện người dùng | Mới | - |
| AC-B-CounterReturnTicketForm | boundary | CounterReturnTicketForm | // requestReturnTicket: nhận yêu cầu trả vé và thông tin nhận diện vé từ tác nhân<br>// confirmReturnTicket: nhận xác nhận trả vé của tác nhân<br>// declineReturnTicket: nhận việc tác nhân không xác nhận trả vé<br>// showReturnInfo: hiển thị thông tin vé, thời gian còn lại, mức hoàn và số tiền hoàn<br>// showTicketNotFoundNotice: thông báo không tìm thấy vé khớp thông tin đã cung cấp<br>// showTicketCancelledNotice: thông báo vé đã bị huỷ<br>// showWrongChannelNotice: thông báo vé mua qua kênh khác kênh yêu cầu trả (BR-11)<br>// showReturnTimeLimitNotice: thông báo còn dưới 4 giờ trước giờ xuất bến (BR-12)<br>// showReturnAbortedNotice: thông báo yêu cầu trả vé đã được huỷ, vé giữ nguyên<br>// showRefundFailedNotice: thông báo hoàn tiền không thành công, vé chưa được trả<br>// showReturnResult: hiển thị kết quả trả vé gồm trạng thái vé, số tiền hoàn, hình thức hoàn | ticketCode | 1, 2a, 2b, 3a, 3b, 5, 6, 6a, 9a, 11 | Giao diện người dùng | Mới | - |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestRefund: gửi yêu cầu hoàn số tiền hoàn của vé tới Cổng thanh toán<br>// returnRefundResult: nhận kết quả hoàn tiền từ Cổng thanh toán | ticketCode, refundAmount | 8, 9 | Giao diện hệ thống | Mới | GL-16 |
| AC-C-ReturnTicketController | control | ReturnTicketController | // startReturnTicket: điều phối nhận diện vé, kiểm tra điều kiện trả, tính số tiền hoàn và hiển thị cho tác nhân<br>// confirmReturn: điều phối xác định hình thức hoàn, hoàn tiền qua cổng thanh toán khi cần, huỷ vé và thông báo kết quả<br>// cancelReturnRequest: kết thúc yêu cầu trả vé khi tác nhân không xác nhận | - | 1-11, 2a, 2b, 3a, 3b, 6a, 7a, 9a | - | Mới | - |
| AC-E-Ticket | entity | Ticket | // findTicket: tìm vé khớp mã vé và, khi hành khách yêu cầu, khớp số điện thoại người đi<br>// checkNotCancelled: kiểm tra vé chưa ở trạng thái đã huỷ (ASM-20)<br>// checkPurchaseChannel: kiểm tra kênh mua của vé trùng kênh yêu cầu trả (BR-11)<br>// checkReturnTimeLimit: kiểm tra thời gian còn lại trước giờ xuất bến từ 4 giờ trở lên và cho biết thời gian còn lại (BR-12)<br>// calculateRefundAmount: xác định mức hoàn 90% hoặc 50% và tính số tiền hoàn theo giá vé (BR-13, BR-14)<br>// getTicketReturnInfo: cung cấp mã vé, tuyến, giờ xuất bến, chỗ, giá vé để hiển thị<br>// determineRefundMethod: xác định hình thức hoàn theo kênh mua (BR-15, BR-16)<br>// cancelTicket: chuyển vé sang đã huỷ, trả chỗ và tạo khoản hoàn tiền | ticketCode, travelerPhone, price, status, purchaseChannel | 2, 2a, 2b, 3, 3a, 3b, 4, 5, 7, 10 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-13, GL-22, GL-37, GL-39 |
| AC-E-Trip | entity | Trip | // calculateTimeToDeparture: tính thời gian còn lại từ thời điểm trả tới giờ xuất bến của chuyến<br>// getRouteAndDepartureTime: cung cấp tuyến và giờ xuất bến của chuyến | departureTime | 3, 3b, 4, 5 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-04, GL-10, GL-34 |
| AC-E-Seat | entity | Seat | // getSeatCode: cung cấp mã chỗ của vé<br>// release: trả chỗ của vé đã trả về trạng thái còn trống (BR-03, ASM-20) | seatCode, status | 5, 10 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-02, GL-03 |
| AC-E-Refund | entity | Refund | // createRefund: khởi tạo khoản hoàn tiền của vé đã trả, ghi mức hoàn, số tiền hoàn, hình thức hoàn và kết quả hoàn | refundAmount, refundRate, refundMethod, refundResult | 10 | - | Mới | GL-16, GL-24 |


Số lớp: 8 (3 boundary, 1 control, 4 entity), trong đó 3 entity tái dùng từ UC-002. Thuộc tính có kiểu khái niệm: departureTime (Giờ), price và refundAmount (Số tiền), refundRate (Số lượng, đơn vị phần trăm), status (Trạng thái), purchaseChannel (Trạng thái, giá trị Trực tuyến hoặc Tại quầy), refundMethod (Trạng thái, giá trị Qua cổng thanh toán hoặc Tiền mặt tại quầy), refundResult (Trạng thái), các thuộc tính còn lại là Văn bản.

## 4. Phân bổ hành vi


| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc (Giao tiếp tác nhân / Information Expert / Controller / Creator / Lớp mới / Giao cho control) | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestReturnTicket | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 1 | // startReturnTicket | AC-C-ReturnTicketController | Controller | - |
| 2 | // findTicket | AC-E-Ticket | Information Expert | Mã vé và số điện thoại người đi nằm ở Ticket; giao cho control bị loại vì control sẽ phải đọc dữ liệu của vé |
| 2 | // checkNotCancelled | AC-E-Ticket | Information Expert | Trạng thái vé nằm ở Ticket |
| 2a | // showTicketNotFoundNotice | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 2b | // showTicketCancelledNotice | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 3 | // checkPurchaseChannel | AC-E-Ticket | Information Expert | Kênh mua là thuộc tính của vé (GL-13) |
| 3 | // checkReturnTimeLimit | AC-E-Ticket | Information Expert | Dữ liệu nằm ở hai lớp: giờ xuất bến ở Trip, quy tắc BR-12 là quy tắc trả vé của vé. Giao cho Ticket và thêm quan hệ tới Trip; giao cho Trip bị loại vì Trip sẽ phải biết quy tắc trả vé (cohesion thấp); giao cho control bị loại vì thành god control |
| 3 | // calculateTimeToDeparture | AC-E-Trip | Information Expert | Giờ xuất bến nằm ở Trip |
| 3a | // showWrongChannelNotice | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 3b | // showReturnTimeLimitNotice | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 4 | // calculateRefundAmount | AC-E-Ticket | Information Expert | Giá vé nằm ở Ticket nên Ticket tính số tiền hoàn. Giao cho Refund bị loại vì khoản hoàn chỉ được ghi nhận ở bước 10 sau khi hoàn thành công (ASM-21), trước đó chưa có đối tượng Refund |
| 5 | // getTicketReturnInfo | AC-E-Ticket | Information Expert | Vé biết mã vé, giá vé, chuyến và chỗ của mình |
| 5 | // getRouteAndDepartureTime | AC-E-Trip | Information Expert | - |
| 5 | // getSeatCode | AC-E-Seat | Information Expert | - |
| 5 | // showReturnInfo | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 6 | // confirmReturnTicket | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 6 | // confirmReturn | AC-C-ReturnTicketController | Controller | - |
| 6a | // declineReturnTicket | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 6a | // cancelReturnRequest | AC-C-ReturnTicketController | Controller | - |
| 6a | // showReturnAbortedNotice | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 7 | // determineRefundMethod | AC-E-Ticket | Information Expert | Kênh mua nằm ở Ticket |
| 7a | (không có message tới PaymentGateway) | AC-C-ReturnTicketController | Controller | Control bỏ qua nhánh hoàn qua cổng khi hình thức hoàn là Tiền mặt tại quầy (opt trong SD1, ref ở SD5) |
| 8 | // requestRefund | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 9 | // returnRefundResult | AC-B-PaymentGateway | Giao tiếp tác nhân | Kết quả do ACT-06 trả về boundary của nó |
| 9a | // showRefundFailedNotice | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |
| 10 | // cancelTicket | AC-E-Ticket | Information Expert | Dữ liệu nằm ở nhiều lớp (vé, chỗ, khoản hoàn). Giao cho Ticket vì Ticket đổi trạng thái của chính nó và có quan hệ tới Seat và Refund; giao cho control bị loại vì thành god control |
| 10 | // release | AC-E-Seat | Information Expert | Trạng thái chỗ nằm ở Seat |
| 10 | // createRefund | AC-E-Refund | Creator | Ticket có dữ liệu khởi tạo (giá vé, số tiền hoàn, hình thức hoàn) nên Ticket gửi message Tạo; giao cho control bị loại để control không giữ dữ liệu nghiệp vụ |
| 11 | // showReturnResult | AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm | Giao tiếp tác nhân | - |


Bước 7a không có hành động (cột Thực hiện bởi của P04 ghi "-"), nên chỉ có dòng ghi nhận việc control bỏ qua nhánh hoàn qua cổng.

## 5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-008.drawio gồm năm trang. SD1 thể hiện luồng chính của ACT-01 (vé mua trực tuyến) cùng nhánh hoàn qua cổng thanh toán bằng fragment opt, là phần luồng 7a bỏ qua khi vé mua tại quầy. SD2 thể hiện luồng 2a, 2b; SD3 thể hiện luồng 3a, 3b; SD4 thể hiện luồng 6a, 9a; SD5 thể hiện luồng chính của ACT-02 (vé mua tại quầy, luồng 7a). Mọi luồng thay thế kết thúc use case dùng fragment break. Message ở SD2, SD3, SD4 mang STT của message cùng điểm rẽ nhánh trong SD1 kèm hậu tố a (ví dụ 1.1.1a là nhánh của message 1.1.1); message ở SD5 mang STT của SD1 kèm hậu tố c. Các luồng thay thế của ACT-02 (2a, 2b, 3a, 3b, 6a) có nội dung giống SD2, SD3, SD4 với boundary CounterReturnTicketForm thay cho ReturnTicketForm nên không vẽ lại.

Bảng message dùng thêm cột ID (ID cell trong file .drawio). Lifeline Refund có đỉnh đặt ngang message Tạo 2.1.3.2. Trang có fragment bắt đầu message đầu tiên ở y thấp hơn 120 một khoảng bằng 40 để chừa chỗ nhãn của fragment.


### SD1 - Luồng chính của ACT-01 (vé mua trực tuyến), nhánh hoàn qua cổng thanh toán (opt)

a) Tên sơ đồ và luồng thể hiện: luồng chính (bước 1 đến 11) với opt cho bước 8, 9 (phần bị bỏ qua ở luồng 7a).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1-L01 | Actor | Hành khách | ACT-01 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 1260 |
| SD1-L02 | Lifeline | :ReturnTicketForm | boundary | - | Boundary của ACT-01 | 200 | 40 | 120 | 1260 |
| SD1-L03 | Lifeline | :ReturnTicketController | control | - | Control của UC-008 | 360 | 40 | 120 | 1260 |
| SD1-L04 | Lifeline | :Ticket | entity | - | Vé cần trả | 520 | 40 | 120 | 1260 |
| SD1-L05 | Lifeline | :Trip | entity | - | Chuyến của vé | 680 | 40 | 120 | 1260 |
| SD1-L06 | Lifeline | :Seat | entity | - | Chỗ của vé | 840 | 40 | 120 | 1260 |
| SD1-L07 | Lifeline | :Refund | entity | - | Được tạo bởi message 2.1.3.2 | 1000 | 1200 | 120 | 100 |
| SD1-L08 | Lifeline | :PaymentGateway | boundary | - | Boundary của ACT-06 | 1160 | 40 | 120 | 1260 |
| SD1-L09 | Actor | Cổng thanh toán | ACT-06 (Hệ thống ngoài) | - | Tác nhân phụ | 1320 | 40 | 120 | 1260 |
| SD1-FR1 | Fragment | opt [hình thức hoàn là Qua cổng thanh toán (BR-15)] | opt | - | Nhánh bị bỏ qua khi luồng 7a (vé mua tại quầy), tiếp tục bước 10 | 340 | 920 | 1120 | 180 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1-M01 | 1 | SD1-L01 | SD1-L02 | // requestReturnTicket (mã vé, số điện thoại người đi) | Đồng bộ | - | 1 |
| SD1-M02 | 1.1 | SD1-L02 | SD1-L03 | // startReturnTicket (mã vé, số điện thoại người đi, kênh yêu cầu trả) | Đồng bộ | - | 1 |
| SD1-M03 | 1.1.1 | SD1-L03 | SD1-L04 | // findTicket (mã vé, số điện thoại người đi) | Đồng bộ | - | 2 |
| SD1-M04 | 1.1.1 (trả về) | SD1-L04 | SD1-L03 | vé khớp thông tin đã cung cấp | Trả về | - | 2 |
| SD1-M05 | 1.1.2 | SD1-L03 | SD1-L04 | // checkNotCancelled | Đồng bộ | - | 2 |
| SD1-M06 | 1.1.3 | SD1-L03 | SD1-L04 | // checkPurchaseChannel (kênh yêu cầu trả, BR-11) | Đồng bộ | - | 3 |
| SD1-M07 | 1.1.4 | SD1-L03 | SD1-L04 | // checkReturnTimeLimit (thời điểm trả, BR-12) | Đồng bộ | - | 3 |
| SD1-M08 | 1.1.4.1 | SD1-L04 | SD1-L05 | // calculateTimeToDeparture (thời điểm trả) | Đồng bộ | - | 3 |
| SD1-M09 | 1.1.4 (trả về) | SD1-L04 | SD1-L03 | thời gian còn lại trước giờ xuất bến | Trả về | - | 3 |
| SD1-M10 | 1.1.5 | SD1-L03 | SD1-L04 | // calculateRefundAmount (thời gian còn lại) | Đồng bộ | - | 4 |
| SD1-M11 | 1.1.5 (trả về) | SD1-L04 | SD1-L03 | mức hoàn và số tiền hoàn | Trả về | - | 4 |
| SD1-M12 | 1.1.6 | SD1-L03 | SD1-L04 | // getTicketReturnInfo | Đồng bộ | - | 5 |
| SD1-M13 | 1.1.6.1 | SD1-L04 | SD1-L05 | // getRouteAndDepartureTime | Đồng bộ | - | 5 |
| SD1-M14 | 1.1.6.2 | SD1-L04 | SD1-L06 | // getSeatCode | Đồng bộ | - | 5 |
| SD1-M15 | 1.1.6 (trả về) | SD1-L04 | SD1-L03 | mã vé, tuyến, giờ xuất bến, chỗ, giá vé | Trả về | - | 5 |
| SD1-M16 | 1.1.7 | SD1-L03 | SD1-L02 | // showReturnInfo (thông tin vé, thời gian còn lại, mức hoàn, số tiền hoàn) | Đồng bộ | - | 5 |
| SD1-M17 | 2 | SD1-L01 | SD1-L02 | // confirmReturnTicket | Đồng bộ | - | 6 |
| SD1-M18 | 2.1 | SD1-L02 | SD1-L03 | // confirmReturn | Đồng bộ | - | 6 |
| SD1-M19 | 2.1.1 | SD1-L03 | SD1-L04 | // determineRefundMethod | Đồng bộ | - | 7 |
| SD1-M20 | 2.1.1 (trả về) | SD1-L04 | SD1-L03 | hình thức hoàn theo kênh mua | Trả về | - | 7 |
| SD1-M21 | 2.1.2 | SD1-L03 | SD1-L08 | // requestRefund (mã vé, số tiền hoàn) | Đồng bộ | SD1-FR1 | 8 |
| SD1-M22 | 2.1.2.1 | SD1-L08 | SD1-L09 | // submitRefundRequest (mã vé, số tiền hoàn) | Đồng bộ | SD1-FR1 | 8 |
| SD1-M23 | 2.1.2.2 | SD1-L09 | SD1-L08 | // returnRefundResult (kết quả hoàn tiền) | Đồng bộ | SD1-FR1 | 9 |
| SD1-M24 | 2.1.2 (trả về) | SD1-L08 | SD1-L03 | kết quả hoàn tiền | Trả về | SD1-FR1 | 9 |
| SD1-M25 | 2.1.3 | SD1-L03 | SD1-L04 | // cancelTicket (số tiền hoàn, hình thức hoàn) | Đồng bộ | - | 10 |
| SD1-M26 | 2.1.3.1 | SD1-L04 | SD1-L06 | // release | Đồng bộ | - | 10 |
| SD1-M27 | 2.1.3.2 | SD1-L04 | SD1-L07 | // createRefund (vé, mức hoàn, số tiền hoàn, hình thức hoàn) | Tạo | - | 10 |
| SD1-M28 | 2.1.4 | SD1-L03 | SD1-L02 | // showReturnResult (mã vé, trạng thái vé, số tiền hoàn, hình thức hoàn) | Đồng bộ | - | 11 |

SD1 có 28 dòng message, trong đó 6 message trả về. Ngưỡng F5 đạt (không quá khoảng 30 message, 1 fragment ngoài cùng). Nhánh opt FR1 là nhánh hoàn qua cổng thanh toán; bước 9a vẽ ở SD4.


### SD2 - Luồng 2a, 2b

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 2a (quay lại bước 1, alt) và 2b (kết thúc use case, break).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD2-L01 | Lifeline | :ReturnTicketForm | boundary | - | Boundary của ACT-01 | 40 | 40 | 120 | 360 |
| SD2-L02 | Lifeline | :ReturnTicketController | control | - | Control của UC-008 | 200 | 40 | 120 | 360 |
| SD2-L03 | Lifeline | :Ticket | entity | - | Vé cần trả | 360 | 40 | 120 | 360 |
| SD2-FR1 | Fragment | alt [không có vé nào khớp thông tin đã cung cấp (ASM-18)] | alt | - | Điểm rẽ nhánh: sau 1.1.1 (trả về) của SD1. Luồng 2a quay lại bước 1. Toán hạng 1 | 20 | 120 | 480 | 160 |
| SD2-FR1-O2 | Fragment | [có vé khớp thông tin đã cung cấp] | alt | SD2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SD2-FR1-O2-SEP | 30 | 200 | 460 | 20 |
| SD2-FR2 | Fragment | break [vé khớp thông tin và đã bị huỷ (ASM-20)] | break | - | Điểm rẽ nhánh: sau 1.1.2 của SD1. Luồng 2b kết thúc use case (thất bại) | 20 | 300 | 480 | 60 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2-M01 | 1.1.1a | SD2-L02 | SD2-L01 | // showTicketNotFoundNotice | Đồng bộ | SD2-FR1 | 2a |
| SD2-M02 | 1.1.2 | SD2-L02 | SD2-L03 | // checkNotCancelled | Đồng bộ | SD2-FR1 | 2 |
| SD2-M03 | 1.1.2a | SD2-L02 | SD2-L01 | // showTicketCancelledNotice | Đồng bộ | SD2-FR2 | 2b |

SD2 có 3 dòng message, trong đó 0 message trả về. Hai toán hạng của alt loại trừ nhau. Toán hạng 2 lặp lại message 1.1.2 của luồng chính để guard có đủ hai toán hạng; khoảng cách giữa hai message liền nhau lớn hơn 40 ở chỗ có fragment hoặc đường ngăn toán hạng.


### SD3 - Luồng 3a, 3b

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 3a và 3b (kết thúc use case, break).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD3-L01 | Lifeline | :ReturnTicketForm | boundary | - | Boundary của ACT-01 | 40 | 40 | 120 | 260 |
| SD3-L02 | Lifeline | :ReturnTicketController | control | - | Control của UC-008 | 200 | 40 | 120 | 260 |
| SD3-FR1 | Fragment | break [vé được mua qua kênh khác với kênh yêu cầu trả (BR-11)] | break | - | Điểm rẽ nhánh: sau 1.1.3 của SD1. Luồng 3a kết thúc use case (thất bại) | 20 | 120 | 320 | 60 |
| SD3-FR2 | Fragment | break [đúng kênh mua và thời gian còn lại dưới 4 giờ (BR-12)] | break | - | Điểm rẽ nhánh: sau 1.1.4 (trả về) của SD1. Luồng 3b kết thúc use case (thất bại) | 20 | 200 | 320 | 60 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD3-M01 | 1.1.3a | SD3-L02 | SD3-L01 | // showWrongChannelNotice (BR-11) | Đồng bộ | SD3-FR1 | 3a |
| SD3-M02 | 1.1.4a | SD3-L02 | SD3-L01 | // showReturnTimeLimitNotice (BR-12) | Đồng bộ | SD3-FR2 | 3b |

SD3 có 2 dòng message, trong đó 0 message trả về.


### SD4 - Luồng 6a, 9a

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 6a và 9a (kết thúc use case, break).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD4-L01 | Actor | Hành khách | ACT-01 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 340 |
| SD4-L02 | Lifeline | :ReturnTicketForm | boundary | - | Boundary của ACT-01 | 200 | 40 | 120 | 340 |
| SD4-L03 | Lifeline | :ReturnTicketController | control | - | Control của UC-008 | 360 | 40 | 120 | 340 |
| SD4-FR1 | Fragment | break [tác nhân không xác nhận trả vé (ASM-19)] | break | - | Điểm rẽ nhánh: sau 1.1.7 của SD1, thay cho message 2. Luồng 6a kết thúc use case (thất bại) | 20 | 120 | 480 | 140 |
| SD4-FR2 | Fragment | break [kết quả hoàn tiền không thành công (ASM-21)] | break | - | Điểm rẽ nhánh: sau 2.1.2 (trả về) của SD1, trước message 2.1.3. Luồng 9a kết thúc use case (thất bại), vé không bị huỷ | 180 | 280 | 320 | 60 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD4-M01 | 2a | SD4-L01 | SD4-L02 | // declineReturnTicket | Đồng bộ | SD4-FR1 | 6a |
| SD4-M02 | 2a.1 | SD4-L02 | SD4-L03 | // cancelReturnRequest | Đồng bộ | SD4-FR1 | 6a |
| SD4-M03 | 2a.1.1 | SD4-L03 | SD4-L02 | // showReturnAbortedNotice | Đồng bộ | SD4-FR1 | 6a |
| SD4-M04 | 2.1.3a | SD4-L03 | SD4-L02 | // showRefundFailedNotice | Đồng bộ | SD4-FR2 | 9a |

SD4 có 4 dòng message, trong đó 0 message trả về.


### SD5 - Luồng chính của ACT-02 (vé mua tại quầy), luồng 7a

a) Tên sơ đồ và luồng thể hiện: luồng chính của nhân viên bán vé kèm luồng 7a; nội bộ bước 2 đến 5 và bước 10 giống SD1 nên dùng fragment ref.

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD5-L01 | Actor | Nhân viên bán vé | ACT-02 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 620 |
| SD5-L02 | Lifeline | :CounterReturnTicketForm | boundary | - | Boundary của ACT-02 | 200 | 40 | 120 | 620 |
| SD5-L03 | Lifeline | :ReturnTicketController | control | - | Control của UC-008, dùng chung với SD1 | 360 | 40 | 120 | 620 |
| SD5-L04 | Lifeline | :Ticket | entity | - | Vé mua tại quầy cần trả | 520 | 40 | 120 | 620 |
| SD5-REF1 | Fragment | ref SD1: bước 2 đến 5 (message 1.1.1 đến 1.1.6) | ref | - | Nội bộ giống SD1; kênh yêu cầu trả là Tại quầy | 340 | 180 | 320 | 60 |
| SD5-REF2 | Fragment | ref SD1: bước 10 (message 2.1.3 đến 2.1.3.2) | ref | - | Huỷ vé, trả chỗ, ghi nhận khoản hoàn tiền mặt tại quầy | 340 | 480 | 320 | 60 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD5-M01 | 1c | SD5-L01 | SD5-L02 | // requestReturnTicket (mã vé) | Đồng bộ | - | 1 |
| SD5-M02 | 1c.1 | SD5-L02 | SD5-L03 | // startReturnTicket (mã vé, kênh yêu cầu trả) | Đồng bộ | - | 1 |
| SD5-M03 | 1c.2 | SD5-L03 | SD5-L02 | // showReturnInfo (thông tin vé, thời gian còn lại, mức hoàn, số tiền hoàn) | Đồng bộ | - | 5 |
| SD5-M04 | 2c | SD5-L01 | SD5-L02 | // confirmReturnTicket | Đồng bộ | - | 6 |
| SD5-M05 | 2c.1 | SD5-L02 | SD5-L03 | // confirmReturn | Đồng bộ | - | 6 |
| SD5-M06 | 2c.1.1 | SD5-L03 | SD5-L04 | // determineRefundMethod | Đồng bộ | - | 7 |
| SD5-M07 | 2c.1.1 (trả về) | SD5-L04 | SD5-L03 | hình thức hoàn là Tiền mặt tại quầy (luồng 7a: không gửi yêu cầu tới PaymentGateway) | Trả về | - | 7a |
| SD5-M08 | 2c.2 | SD5-L03 | SD5-L02 | // showReturnResult (mã vé, trạng thái vé, số tiền hoàn, hình thức hoàn) | Đồng bộ | - | 11 |

SD5 có 8 dòng message, trong đó 1 message trả về. Hai fragment ref thay cho các message nội bộ của SD1 (1.1.1 đến 1.1.6 và 2.1.3 đến 2.1.3.2); luồng 7a không có message tới PaymentGateway.


## 6. Quy tắc tương tác giữa các lớp phân tích

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

Đã kiểm tra mọi message của SD1 đến SD5 và mọi link của communication diagram theo bảng F6: actor chỉ gửi message tới boundary của mình (ACT-01 --> ReturnTicketForm, ACT-02 --> CounterReturnTicketForm, ACT-06 --> PaymentGateway); boundary chỉ trao đổi với actor của nó và control; control gọi boundary, entity; entity chỉ gọi entity có quan hệ cấu trúc (Ticket --> Trip, Ticket --> Seat, Ticket --> Refund). Message 2.1.2.2 từ ACT-06 tới PaymentGateway và 2.1.2.1 từ PaymentGateway tới ACT-06 là trao đổi giữa actor phụ và boundary của nó.

## 7. Communication diagram

File diagrams/P07-communication-UC-008.drawio, phạm vi là luồng chính của SD1 (MUC_CHI_TIET là DAY_DU). Luồng thay thế đã gộp vào SD1 là nhánh opt hoàn qua cổng thanh toán (phần luồng 7a bỏ qua). Luồng thay thế ở SD2, SD3, SD4 nằm trên trang riêng và SD5 là biến thể của tác nhân ACT-02 nên không gộp vào communication diagram. Nhãn link dùng STT của SD1; message trả về không vẽ.

a) Bảng Node:


| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| CO-01 | Actor | Hành khách | - | - | Tác nhân chính | 40 | 200 | 40 | 80 |
| CO-02 | Object | :ReturnTicketForm | boundary | - | Boundary của ACT-01 | 200 | 220 | 160 | 40 |
| CO-03 | Object | :ReturnTicketController | control | - | Control của UC-008 | 640 | 220 | 160 | 40 |
| CO-04 | Object | :Ticket | entity | - | Vé cần trả | 640 | 560 | 160 | 40 |
| CO-05 | Object | :Trip | entity | - | Chuyến của vé | 200 | 560 | 160 | 40 |
| CO-06 | Object | :Seat | entity | - | Chỗ của vé | 1080 | 560 | 160 | 40 |
| CO-07 | Object | :Refund | entity | - | Được tạo bởi message 2.1.3.2 | 640 | 760 | 160 | 40 |
| CO-08 | Object | :PaymentGateway | boundary | - | Boundary của ACT-06 | 1080 | 220 | 160 | 40 |
| CO-09 | Actor | Cổng thanh toán | - | - | Tác nhân phụ | 1440 | 200 | 40 | 80 |

b) Bảng Edge (link):

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message |
|---|---|---|---|---|---|
| LK-01 | CO-01 | CO-02 | Link | 1: // requestReturnTicket (mã vé, số điện thoại người đi) (-->)<br>2: // confirmReturnTicket (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-02 | CO-02 | CO-03 | Link | 1.1: // startReturnTicket (mã vé, số điện thoại người đi, kênh yêu cầu trả) (-->)<br>1.1.7: // showReturnInfo (thông tin vé, thời gian còn lại, mức hoàn, số tiền hoàn) (<--)<br>2.1: // confirmReturn (-->)<br>2.1.4: // showReturnResult (mã vé, trạng thái vé, số tiền hoàn, hình thức hoàn) (<--) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-03 | CO-03 | CO-04 | Link | 1.1.1: // findTicket (mã vé, số điện thoại người đi) (-->)<br>1.1.2: // checkNotCancelled (-->)<br>1.1.3: // checkPurchaseChannel (kênh yêu cầu trả, BR-11) (-->)<br>1.1.4: // checkReturnTimeLimit (thời điểm trả, BR-12) (-->)<br>1.1.5: // calculateRefundAmount (thời gian còn lại) (-->)<br>1.1.6: // getTicketReturnInfo (-->)<br>2.1.1: // determineRefundMethod (-->)<br>2.1.3: // cancelTicket (số tiền hoàn, hình thức hoàn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-04 | CO-04 | CO-05 | Link | 1.1.4.1: // calculateTimeToDeparture (thời điểm trả) (-->)<br>1.1.6.1: // getRouteAndDepartureTime (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-05 | CO-04 | CO-06 | Link | 1.1.6.2: // getSeatCode (-->)<br>2.1.3.1: // release (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-06 | CO-03 | CO-08 | Link | 2.1.2: // requestRefund (mã vé, số tiền hoàn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-07 | CO-08 | CO-09 | Link | 2.1.2.1: // submitRefundRequest (mã vé, số tiền hoàn) (-->)<br>2.1.2.2: // returnRefundResult (kết quả hoàn tiền) (<--) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-08 | CO-04 | CO-07 | Link | 2.1.3.2: // createRefund (vé, mức hoàn, số tiền hoàn, hình thức hoàn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |


Tổng số message trên các link: 22 (bằng số message không phải trả về của SD1: 22). Không có link tự gọi.

## 8. VOPC

File diagrams/P07-class-UC-008.drawio.

a) Bảng Node (lớp):


| ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-B-CounterReturnTicketForm | Class | CounterReturnTicketForm | «boundary» | - | ticketCode | // requestReturnTicket<br>// confirmReturnTicket<br>// declineReturnTicket<br>// showReturnInfo<br>// showTicketNotFoundNotice<br>// showTicketCancelledNotice<br>// showWrongChannelNotice<br>// showReturnTimeLimitNotice<br>// showReturnAbortedNotice<br>// showRefundFailedNotice<br>// showReturnResult | 40 | 40 | 240 | 300 |
| AC-B-ReturnTicketForm | Class | ReturnTicketForm | «boundary» | - | ticketCode<br>travelerPhone | // requestReturnTicket<br>// confirmReturnTicket<br>// declineReturnTicket<br>// showReturnInfo<br>// showTicketNotFoundNotice<br>// showTicketCancelledNotice<br>// showWrongChannelNotice<br>// showReturnTimeLimitNotice<br>// showReturnAbortedNotice<br>// showRefundFailedNotice<br>// showReturnResult | 360 | 40 | 240 | 320 |
| AC-B-PaymentGateway | Class | PaymentGateway | «boundary» | - | ticketCode<br>refundAmount | // requestRefund<br>// returnRefundResult | 680 | 40 | 240 | 140 |
| AC-C-ReturnTicketController | Class | ReturnTicketController | «control» | - | - | // startReturnTicket<br>// confirmReturn<br>// cancelReturnRequest | 360 | 460 | 240 | 120 |
| AC-E-Trip | Class | Trip | «entity» | - | departureTime | // calculateTimeToDeparture<br>// getRouteAndDepartureTime | 40 | 680 | 240 | 120 |
| AC-E-Ticket | Class | Ticket | «entity» | - | ticketCode<br>travelerPhone<br>price<br>status<br>purchaseChannel | // findTicket<br>// checkNotCancelled<br>// checkPurchaseChannel<br>// checkReturnTimeLimit<br>// calculateRefundAmount<br>// getTicketReturnInfo<br>// determineRefundMethod<br>// cancelTicket | 360 | 680 | 240 | 320 |
| AC-E-Seat | Class | Seat | «entity» | - | seatCode<br>status | // getSeatCode<br>// release | 680 | 680 | 240 | 140 |
| AC-E-Refund | Class | Refund | «entity» | - | refundAmount<br>refundRate<br>refundMethod<br>refundResult | // createRefund | 360 | 1100 | 240 | 160 |


b) Bảng quan hệ (bảng Edge):

| ID | Lớp A | Lớp B | Loại (Association / Aggregation / Composition / Generalization / Dependency) | Multiplicity | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC008-01 | AC-B-ReturnTicketForm | AC-C-ReturnTicketController | Association | - | tạm thời | LK-02 |
| R-UC008-02 | AC-B-CounterReturnTicketForm | AC-C-ReturnTicketController | Association | - | tạm thời | Bước 1, 5, 6, 11 và SD5 (message 1c.1, 1c.2, 2c.1, 2c.2); không có link trong F7 vì SD5 không gộp vào SD1 |
| R-UC008-03 | AC-C-ReturnTicketController | AC-B-PaymentGateway | Association | - | tạm thời | LK-06 |
| R-UC008-04 | AC-C-ReturnTicketController | AC-E-Ticket | Association | - | tạm thời | LK-03 |
| R-UC008-05 | AC-E-Ticket | AC-E-Trip | Association | A 0..* - B 1 | vé thuộc một chuyến | LK-04; R-UC002-14; GL-37 |
| R-UC008-06 | AC-E-Ticket | AC-E-Seat | Association | A - B 1 | vé của một chỗ | LK-05; R-UC002-15; BR-10; chờ Q-36 cho phía A |
| R-UC008-07 | AC-E-Ticket | AC-E-Refund | Association | A 1 - B 0..1 | khoản hoàn của vé đã trả | LK-08; ASM-46; bước 2b |

Link actor-boundary (LK-01, LK-07) không vào VOPC. Mỗi link còn lại giữa hai lớp khác nhau của F7 sinh một quan hệ (LK-02 --> R-UC008-01, LK-03 --> R-UC008-04, LK-04 --> R-UC008-05, LK-05 --> R-UC008-06, LK-06 --> R-UC008-03, LK-08 --> R-UC008-07); R-UC008-02 dựa trên bằng chứng bước UC và SD5. Multiplicity "-" nghĩa là đặc tả chưa nêu rõ nên để trống. Hai quan hệ R-UC008-05, R-UC008-06 trùng với R-UC002-14, R-UC002-15 của UC-002; P08 sẽ gộp. Quan hệ cuối cùng chốt ở P08.

## 9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) và tác nhân |
|---|---|---|
| 1 | 1 (SD1), 1.1 (SD1), 1c, 1c.1 (SD5) | ACT-01, ACT-02, AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm, AC-C-ReturnTicketController |
| 2 | 1.1.1 (SD1), 1.1.1 (trả về) (SD1), 1.1.2 (SD1), 1.1.2 (SD2) | AC-C-ReturnTicketController, AC-E-Ticket |
| 2a | 1.1.1a (SD2) | AC-C-ReturnTicketController, AC-B-ReturnTicketForm |
| 2b | 1.1.2a (SD2) | AC-C-ReturnTicketController, AC-B-ReturnTicketForm |
| 3 | 1.1.3 (SD1), 1.1.4 (SD1), 1.1.4.1 (SD1), 1.1.4 (trả về) (SD1) | AC-C-ReturnTicketController, AC-E-Ticket, AC-E-Trip |
| 3a | 1.1.3a (SD3) | AC-C-ReturnTicketController, AC-B-ReturnTicketForm |
| 3b | 1.1.4a (SD3) | AC-C-ReturnTicketController, AC-B-ReturnTicketForm |
| 4 | 1.1.5 (SD1), 1.1.5 (trả về) (SD1) | AC-C-ReturnTicketController, AC-E-Ticket |
| 5 | 1.1.6 (SD1), 1.1.6.1 (SD1), 1.1.6.2 (SD1), 1.1.6 (trả về) (SD1), 1.1.7 (SD1), 1c.2 (SD5) | AC-C-ReturnTicketController, AC-E-Ticket, AC-E-Trip, AC-E-Seat, AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm |
| 6 | 2 (SD1), 2.1 (SD1), 2c, 2c.1 (SD5) | ACT-01, ACT-02, AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm, AC-C-ReturnTicketController |
| 6a | 2a, 2a.1, 2a.1.1 (SD4) | ACT-01, AC-B-ReturnTicketForm, AC-C-ReturnTicketController |
| 7 | 2.1.1 (SD1), 2.1.1 (trả về) (SD1), 2c.1.1 (SD5) | AC-C-ReturnTicketController, AC-E-Ticket |
| 7a | 2c.1.1 (trả về) (SD5); fragment opt FR1 (SD1) | AC-C-ReturnTicketController, AC-E-Ticket |
| 8 | 2.1.2 (SD1), 2.1.2.1 (SD1) | AC-C-ReturnTicketController, AC-B-PaymentGateway, ACT-06 |
| 9 | 2.1.2.2 (SD1), 2.1.2 (trả về) (SD1) | ACT-06, AC-B-PaymentGateway, AC-C-ReturnTicketController |
| 9a | 2.1.3a (SD4) | AC-C-ReturnTicketController, AC-B-ReturnTicketForm |
| 10 | 2.1.3 (SD1), 2.1.3.1 (SD1), 2.1.3.2 (SD1) | AC-C-ReturnTicketController, AC-E-Ticket, AC-E-Seat, AC-E-Refund |
| 11 | 2.1.4 (SD1), 2c.2 (SD5) | AC-C-ReturnTicketController, AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm |

## 10. File .drawio

| File | Trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-008.drawio | SD1, SD2, SD3, SD4, SD5 | Bảng F5; ID cell là ID trong bảng lifeline, fragment, message |
| diagrams/P07-communication-UC-008.drawio | COMM1 | Bảng F7; ID cell là ID trong bảng Node và Edge |
| diagrams/P07-class-UC-008.drawio | VOPC1 | Bảng F8; ID cell của lớp là mã AC, của cạnh là ID quan hệ, nhãn multiplicity là cell con của cạnh |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-70 | Kênh yêu cầu trả vé (Trực tuyến hoặc Tại quầy) do hệ thống suy ra từ tác nhân thực hiện, hay do tác nhân chọn hoặc nhập? (Suy từ tác nhân / Tác nhân nhập) | Bước 3, luồng 3a; BR-11; message 1.1 (SD1), 1c.1 (SD5); ASM-45 | P04 UC-008 bước 3 và BR-11 nói "kênh đang yêu cầu trả" nhưng Dữ liệu vào 1 không có trường kênh |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-45 | Kênh yêu cầu trả vé được suy ra từ tác nhân thực hiện: hành khách (ACT-01) là kênh Trực tuyến, nhân viên bán vé (ACT-02) là kênh Tại quầy. Control truyền kênh này cho Ticket kiểm tra BR-11 và gửi kết quả về boundary của đúng tác nhân. | P04 không nêu cách xác định kênh đang yêu cầu trả, trong khi BR-11 và luồng 3a cần so sánh với kênh mua của vé. Chờ Q-70 | AC-E-Ticket (checkPurchaseChannel); AC-C-ReturnTicketController; message 1.1, 1.1.3; luồng 3a |
| ASM-46 | Khoản hoàn tiền (Refund) là entity chỉ được tạo ở bước 10 sau khi việc hoàn tiền thành công (hoặc ngay khi hình thức hoàn là tiền mặt), gắn với đúng một vé; mỗi vé có tối đa một khoản hoàn. | GL-16 coi khoản hoàn là khái niệm có hình thức hoàn và kết quả hoàn; ASM-21 buộc không có khoản hoàn nào được ghi nhận khi hoàn không thành công; luồng 2b không cho trả lại vé đã huỷ nên một vé không có hai khoản hoàn | AC-E-Refund; R-UC008-07; message 2.1.3.2; bước 10 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-008 Dữ liệu vào 1, bước 3, BR-11 | BR-11 và bước 3 so sánh kênh mua với "kênh đang yêu cầu trả" nhưng bảng Dữ liệu vào 1 không có trường kênh, nên không biết kênh lấy từ đâu khi phân bổ cho lớp | Ghi vào bước 1 hoặc Mục 8 của P04 rằng kênh yêu cầu trả suy từ tác nhân (ASM-45), hoặc thêm trường vào Dữ liệu vào 1 sau khi Q-70 được trả lời |
| P04 | UC-008 bước 7, 7a | BR-11 đã buộc kênh trả trùng kênh mua ở bước 3, nên hình thức hoàn ở bước 7 luôn suy ra được từ tác nhân; bước 7 chỉ lặp lại thông tin đã có | Giữ bước 7 nếu cần để thể hiện BR-15, BR-16; nếu Q-02 được trả lời (c), bước 7 mới có lựa chọn thật |
| P01 | ACT-01, ACT-02 | P04 UC-008 Mục 8 ghi hai tác nhân chính chung một cột vì P01 không có tác nhân cha; P07 phải dùng hai boundary cho hai tác nhân dù hành vi của hai tác nhân gần như giống nhau | Cân nhắc thêm tác nhân cha tổng quát hoá cho ACT-01, ACT-02 ở các use case dùng chung, hoặc chấp nhận hai boundary |
| P04 | UC-003 (chưa có đặc tả) | AC-B-PaymentGateway được đặt mã tại UC-008 vì ACT-06 tương tác trực tiếp ở UC-008; UC-002 đã ghi boundary của ACT-06 thuộc P07 của UC-003 | Khi chạy P07 UC-003 phải tái dùng đúng mã AC-B-PaymentGateway (Tái dùng từ UC-008) và bổ sung trách nhiệm thanh toán |

## Vấn đề còn mở

- Target 14 đạt một phần: C7.3 yêu cầu cạnh không cắt qua node và không có hai node chồng nhau, nhưng trong sequence diagram message đi qua các lifeline ở giữa và fragment phủ lên lifeline theo ký pháp UML (F10). Các file communication và VOPC thoả C7.3 về toạ độ bội số 10, khoảng cách giữa node từ 40, nhưng nhãn của link trong communication diagram dài nên có thể chồng lên hình của node kề khi mở bằng draw.io; cần chỉnh tay.
- Target 9 đạt một phần: Refund chỉ có trách nhiệm createRefund, đặc tả UC-008 không nêu hành vi nào khác trên khoản hoàn (tính số tiền hoàn được giao cho Ticket vì Refund chưa tồn tại ở bước 4, ASM-21). Seat chỉ có getSeatCode và release. P08 sẽ gộp thêm trách nhiệm từ UC-013 (hoàn 100%, BR-17) cho Refund.
- Target 1: bước 7a không có hành động (P04 ghi "-") nên không có message riêng, thể hiện bằng nhánh opt bị bỏ qua ở SD1 và ghi chú ở SD5. Bước 9 do ACT-06 thực hiện có message 2.1.2.2 từ ACT-06 tới PaymentGateway. Với ACT-02, nội bộ bước 2 đến 5 và bước 10 thể hiện bằng fragment ref tới SD1 chứ không vẽ lại message.
- Chọn giữa hai quy tắc (C9): F3.1 quy định một boundary cho mỗi cặp tác nhân và use case, còn P04 gộp hai tác nhân chính chung một cột "Hành khách / Nhân viên bán vé". Đã chọn hai boundary (ReturnTicketForm, CounterReturnTicketForm), kéo theo SD5 riêng cho ACT-02 và VOPC có quan hệ R-UC008-02 không có link trong F7.
- Chọn giữa hai quy tắc (C9): F5 yêu cầu message đầu tiên ở y=120 và cách nhau 40 (F10), nhưng nhãn fragment và đường ngăn toán hạng cần chỗ; các trang SD2, SD3, SD4 bắt đầu message đầu tiên ở y=160 hoặc cao hơn và có khoảng cách 80 hoặc 60 quanh fragment.
- Chọn giữa hai quy tắc (C9): F7 yêu cầu communication diagram tương đương với phần sequence diagram nó thể hiện; luồng 7a (ACT-02) vẽ ở SD5 nên không có trong communication diagram, chỉ có opt của SD1.
- Chạy sau UC-002 nhưng trước UC-003: AC-B-PaymentGateway do UC-008 đặt mã (xem Đề xuất sửa artifact trước). Trách nhiệm AC-E-Seat // release dùng lại tên của UC-002 nhưng ý nghĩa khác (UC-002: trả chỗ đang giữ khi hết thời hạn giữ chỗ, BR-08; UC-008: trả chỗ của vé đã trả, BR-03 với ASM-20); P08 quyết định có gộp thành một trách nhiệm hay tách tên. Thuộc tính purchaseChannel của AC-E-Ticket là thuộc tính mới so với UC-002 (GL-13).
- Mốc thời gian phụ thuộc dữ liệu (A2): UC-006 (huỷ đặt chỗ qua điện thoại quá hạn, 60 phút trước giờ xuất bến) tính trên đặt chỗ qua điện thoại chưa thanh toán, UC-008 không tạo hay đổi mốc này. UC-014 (gửi danh sách hành khách của chuyến, 15 phút trước giờ xuất bến) tính theo giờ xuất bến của chuyến chứ không theo dữ liệu của từng vé, danh sách được lập từ vé còn hiệu lực lúc kích hoạt, và BR-12 chặn trả vé từ 4 giờ trước giờ xuất bến nên UC-008 không làm thay đổi vé sau mốc 15 phút (P04 Mục 8). Do đó UC-008 không có message hẹn, hẹn lại hoặc huỷ mốc.
- Chạy với giả định: thời điểm trả vé (Q-39), giá vé dùng tính hoàn (Q-38), kết quả hoàn không thành công (Q-37), trạng thái chỗ sau khi trả (Q-36) và cách xác nhận người yêu cầu (Q-35) vẫn là câu hỏi mở của P04; P07 dùng ASM-18 đến ASM-23 của P04. Bước 8 phụ thuộc API hoàn tiền chưa có tài liệu (Q-24, NFR-07), nên message requestRefund và returnRefundResult chỉ ở mức phân tích.

