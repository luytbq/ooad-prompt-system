# P07 - Phân tích use case UC-013 Huỷ chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P04-uc-specs/UC-013-cancel-trip.md 1.0; P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P02-usecases.md 1.1; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0 và P07-uc-analysis/UC-008-return-ticket-analysis.md 1.0 (sổ đăng ký AC). UC-013 không có use case được include hoặc extend nên không cần đặc tả P04 nào khác |
| Phạm vi | UC-013 |

Quy ước trích nguồn: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md; "Dữ liệu vào n", "Dữ liệu ra n" chỉ bảng dữ liệu của P04 UC-013. Tham số bước: LUONG_CAN_VE = Không có (vẽ mọi luồng); YEU_CAU_BO_SUNG = Không có.

## 1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-013 Huỷ chuyến (Cancel Trip) |
| Tác nhân chính (ACT, loại) | ACT-03 Nhân viên điều hành (Người) |
| Tác nhân phụ (ACT, loại) | ACT-06 Cổng thanh toán (Hệ thống ngoài), tương tác trực tiếp ở bước 7, 8 (RL-19); ACT-07 Cổng SMS (Hệ thống ngoài), tương tác trực tiếp ở bước 10 (RL-20) |
| Include (UC) | Không có |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2 không có điểm mở rộng của UC-013) |
| Tác nhân thời gian | ACT-10 Bộ định thời không kích hoạt UC-013 và không tương tác với UC-013. Hai use case do ACT-10 kích hoạt tính mốc từ giờ xuất bến của chuyến mà UC-013 làm mất hiệu lực: UC-006 Huỷ đặt chỗ qua điện thoại quá hạn (EV-08, 60 phút trước giờ xuất bến) và UC-014 Chuẩn bị danh sách hành khách của chuyến (EV-18, 15 phút trước giờ xuất bến). UC-013 có trách nhiệm huỷ hai mốc này (A2, ASM-47, Q-71) |
| File P07 đã có được dùng làm sổ đăng ký AC | UC-002-book-ticket-online-analysis.md và UC-008-return-ticket-analysis.md. Sổ AC: AC-B-BookTicketForm, AC-B-SmsGateway, AC-B-ReturnTicketForm, AC-B-CounterReturnTicketForm, AC-B-PaymentGateway (boundary); AC-C-BookTicketOnlineController, AC-C-PayTicketOnlineController (tạm chờ UC-003), AC-C-ReturnTicketController (control); AC-E-Trip, AC-E-Route, AC-E-Seat, AC-E-Booking, AC-E-Ticket, AC-E-BaseFare, AC-E-HolidaySurcharge, AC-E-Refund (entity). UC-013 tái dùng AC-B-PaymentGateway, AC-B-SmsGateway, AC-E-Trip, AC-E-Route, AC-E-Ticket, AC-E-Refund |

## 2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Nhân viên điều hành | Yêu cầu huỷ chuyến và chỉ định chuyến cần huỷ (xem Dữ liệu vào 1). | Không đổi | Dữ liệu vào 1; REQ-47, REQ-42 |
| 2 | Hệ thống | Kiểm tra chuyến đã chỉ định có trong lịch chạy, chưa bị huỷ và chưa tới giờ xuất bến (ASM-24). | Hệ thống tìm trong các chuyến của lịch chạy chuyến có tuyến, ngày xuất bến và giờ xuất bến trùng thông tin đã chỉ định. Chuyến tìm được được kiểm tra trạng thái: chuyến đã ở trạng thái đã huỷ thì không huỷ lại (ASM-26). Giờ xuất bến của chuyến được so với thời điểm hiện tại: chỉ huỷ được chuyến chưa tới giờ xuất bến (ASM-24, ASM-49). | ASM-24, ASM-26, ASM-49; GL-04, GL-10, GL-19, GL-36; REQ-42 |
| 2a | Hệ thống | Điều kiện: không có chuyến nào trong lịch chạy khớp tuyến, ngày và giờ xuất bến đã chỉ định (ASM-24). Thông báo không có chuyến khớp thông tin đã chỉ định. Quay lại bước 1. | Hệ thống xác định không có chuyến nào khớp tuyến, ngày và giờ xuất bến đã chỉ định và thông báo cho nhân viên điều hành để chỉ định lại. | ASM-24; GL-19 |
| 2b | Hệ thống | Điều kiện: có chuyến khớp và chuyến đã bị huỷ trước đó (ASM-26). Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã bị huỷ. Kết thúc use case (thất bại). | Hệ thống xác định chuyến khớp đang ở trạng thái đã huỷ, từ chối yêu cầu và thông báo chuyến đã bị huỷ; chuyến, vé và đặt chỗ giữ nguyên. | ASM-26; GL-04 |
| 2c | Hệ thống | Điều kiện: có chuyến khớp, chuyến chưa bị huỷ và đã tới hoặc đã qua giờ xuất bến (ASM-24). Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã tới giờ xuất bến (ASM-24). Kết thúc use case (thất bại). | Hệ thống xác định giờ xuất bến của chuyến chưa huỷ không sau thời điểm hiện tại, từ chối yêu cầu và thông báo chuyến đã tới giờ xuất bến; chuyến, vé và đặt chỗ giữ nguyên. | ASM-24; GL-10; Q-40 |
| 3 | Hệ thống | Hiển thị thông tin chuyến, số vé còn hiệu lực theo kênh mua, số đặt chỗ qua điện thoại chưa thanh toán và tổng số tiền hoàn (xem Dữ liệu ra 1) (BR-17, ASM-25). | Hệ thống lấy tuyến và giờ xuất bến từ chuyến. Từ các vé còn hiệu lực của chuyến, hệ thống lấy kênh mua và số tiền hoàn bằng 100% giá vé (BR-17) để đếm số vé theo kênh mua và cộng tổng số tiền hoàn; từ đặt chỗ qua điện thoại của chuyến, hệ thống đếm các đặt chỗ chưa thanh toán. Hệ thống hiển thị các số liệu đó cho nhân viên điều hành (ASM-25). | Dữ liệu ra 1; BR-17; GL-07, GL-13, GL-38; ASM-25, ASM-27; REQ-42 |
| 4 | Nhân viên điều hành | Xác nhận huỷ chuyến (ASM-25). | Không đổi | ASM-25 |
| 4a | Hệ thống | Điều kiện: nhân viên điều hành không xác nhận huỷ chuyến (ASM-25). Thông báo yêu cầu huỷ chuyến đã được bỏ và chuyến giữ nguyên. Kết thúc use case (thất bại). | Hệ thống kết thúc yêu cầu huỷ chuyến khi nhân viên điều hành không xác nhận và thông báo yêu cầu đã được bỏ; chuyến, vé và đặt chỗ không đổi. | ASM-25 |
| 5 | Hệ thống | Ghi nhận chuyến ở trạng thái đã huỷ, huỷ mọi vé còn hiệu lực và mọi đặt chỗ qua điện thoại chưa thanh toán của chuyến (ASM-26, ASM-27). | Chuyến chuyển sang trạng thái đã huỷ; từng vé còn hiệu lực và từng đặt chỗ qua điện thoại chưa thanh toán của chuyến cùng chuyển sang trạng thái đã huỷ (ASM-26, ASM-27). Hệ thống huỷ các mốc kích hoạt tự động tính từ giờ xuất bến của chuyến: UC-006 (60 phút) và UC-014 (15 phút) (ASM-47). Danh sách vé đã huỷ được giữ tạm trong lần thực hiện để dùng ở bước 6 đến 10. | ASM-26, ASM-27, ASM-47; GL-37, GL-38, GL-39, GL-07; BR-18, BR-19; EV-08, EV-18 |
| 5a | - | Điều kiện: chuyến không có vé còn hiệu lực nào. Tiếp tục bước 11. | Hệ thống bỏ qua bước 6 đến 10 vì không có vé đã huỷ, chuyển sang bước 11. | GL-38 |
| 6 | Hệ thống | Tính số tiền hoàn bằng 100% giá vé (BR-17, BR-19, ASM-22) và xác định hình thức hoàn theo kênh mua (BR-15, BR-16, ASM-28) cho từng vé đã huỷ. | Với từng vé đã huỷ, vé tính số tiền hoàn bằng 100% giá vé đã thanh toán (BR-17, ASM-22), không phụ thuộc thời gian còn lại trước giờ xuất bến. Vé xác định hình thức hoàn theo kênh mua: Qua cổng thanh toán cho vé mua trực tuyến (BR-15), Tiền mặt tại quầy cho vé mua tại quầy (BR-16, ASM-28). | BR-15, BR-16, BR-17, BR-19; GL-08, GL-13, GL-16, GL-24; ASM-22, ASM-28; REQ-49, REQ-50 |
| 6a | - | Điều kiện: chuyến có vé còn hiệu lực và không vé nào được mua trực tuyến. Tiếp tục bước 9. | Hệ thống bỏ qua bước 7, 8 vì không vé nào có hình thức hoàn Qua cổng thanh toán, chuyển sang bước 9. | BR-16; GL-13 |
| 7 | Hệ thống | Gửi yêu cầu hoàn số tiền hoàn của từng vé mua trực tuyến tới Cổng thanh toán (BR-15). | Với từng vé có hình thức hoàn Qua cổng thanh toán, hệ thống gửi mã vé và số tiền hoàn tới Cổng thanh toán qua giao diện hệ thống của cổng. Hệ thống không lưu thông tin thẻ (NFR-03). | BR-15; NFR-03, NFR-07; GL-16, GL-22 |
| 8 | Cổng thanh toán | Trả về kết quả hoàn tiền của từng vé. | Không đổi | NFR-07 |
| 8a | Hệ thống | Điều kiện: Cổng thanh toán trả về kết quả hoàn tiền không thành công cho ít nhất một vé. Ghi nhận khoản hoàn của các vé đó là chưa thành công để nhà xe xử lý lại (ASM-31). Tiếp tục bước 9. | Với từng vé có kết quả hoàn không thành công, vé tạo khoản hoàn với kết quả hoàn chưa thành công; chuyến và vé vẫn ở trạng thái đã huỷ (ASM-31, ASM-48). | ASM-31, ASM-48; GL-16; NFR-07 |
| 9 | Hệ thống | Ghi nhận khoản hoàn của từng vé đã huỷ: vé mua trực tuyến đã được Cổng thanh toán xác nhận hoàn, vé mua tại quầy chờ chi tiền mặt tại quầy (BR-15, BR-16, ASM-28). | Với từng vé đã huỷ chưa được ghi nhận ở 8a, vé tạo khoản hoàn gắn với vé, ghi mức hoàn 100%, số tiền hoàn, hình thức hoàn và kết quả hoàn: đã hoàn khi cổng xác nhận, chờ chi tiền mặt khi hình thức là Tiền mặt tại quầy (ASM-48). Việc chi tiền mặt diễn ra ngoài use case (ASM-28). | BR-15, BR-16, BR-17; GL-16, GL-24; ASM-28, ASM-48 |
| 10 | Hệ thống | Gửi tin nhắn báo huỷ chuyến kèm số tiền hoàn và hình thức hoàn tới số điện thoại người đi của từng vé đã huỷ qua Cổng SMS (xem Dữ liệu ra 2) (BR-18, ASM-29, ASM-30). | Với từng vé đã huỷ, vé lập nội dung tin nhắn gồm mã vé, tuyến và giờ xuất bến lấy từ chuyến, câu báo chuyến đã bị huỷ, số tiền hoàn và hình thức hoàn (ASM-29). Hệ thống gửi nội dung đó tới số điện thoại người đi ghi trên vé qua Cổng SMS, mỗi vé một tin (ASM-30). Đặt chỗ qua điện thoại chưa thanh toán không được nhắn (ASM-27). | Dữ liệu ra 2; BR-18; GL-22, GL-26, GL-30; ASM-27, ASM-29, ASM-30; REQ-48 |
| 11 | Hệ thống | Hiển thị kết quả huỷ chuyến cho nhân viên điều hành (xem Dữ liệu ra 3) (ASM-31). | Hệ thống hiển thị tuyến, giờ xuất bến, số vé đã huỷ, số vé theo kết quả hoàn, tổng số tiền hoàn, số đặt chỗ đã huỷ, số tin nhắn đã gửi và mã vé hoàn không thành công. Các số liệu được tổng hợp tạm thời từ kết quả các bước trước của lần thực hiện và không lưu (ASM-31). | Dữ liệu ra 3; ASM-31; GL-16 |

## 3. Tìm lớp phân tích

### 3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-03 Nhân viên điều hành | Người | CancelTripForm (AC-B-CancelTripForm) | Giao diện người dùng | Mới | Một boundary cho cặp (ACT-03, UC-013) gom mọi tương tác của nhân viên điều hành: chỉ định chuyến, xem thông tin huỷ, xác nhận hoặc không xác nhận, nhận các thông báo và kết quả. Tên theo hành động của use case với hậu tố Form (HAU_TO_TEN_LOP là Mặc định) |
| ACT-06 Cổng thanh toán | Hệ thống ngoài | PaymentGateway (AC-B-PaymentGateway) | Giao diện hệ thống | Tái dùng từ UC-008 (AC-B-PaymentGateway) | ACT-06 tương tác trực tiếp ở bước 7, 8 của UC-013 giống bước 8, 9 của UC-008. Dùng lại đúng mã và tên; trách nhiệm requestRefund, returnRefundResult dùng nguyên |
| ACT-07 Cổng SMS | Hệ thống ngoài | SmsGateway (AC-B-SmsGateway) | Giao diện hệ thống | Tái dùng từ UC-002 (AC-B-SmsGateway) | ACT-07 tương tác trực tiếp ở bước 10. UC-002 đã ghi boundary này tái dùng được ở UC-013; bổ sung trách nhiệm gửi tin nhắn báo huỷ chuyến |

ACT-10 Bộ định thời không tham gia UC-013 nên không có boundary. Số boundary là 3, bằng số tác nhân tham gia.

### 3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Nhân viên điều hành | Mô tả; bước 1, 4, 4a; tiền điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | ACT-03, có boundary CancelTripForm |
| 2 | Cổng thanh toán | Bước 7, 8, 8a | Loại - là tác nhân hoặc ngoài phạm vi | ACT-06, có boundary PaymentGateway |
| 3 | Cổng SMS | Bước 10 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-07, có boundary SmsGateway |
| 4 | Hệ thống | Mọi bước hệ thống | Loại - mơ hồ | Chỉ là chủ ngữ của bước, không chỉ một khái niệm dữ liệu cụ thể |
| 5 | Bộ định thời, mốc kích hoạt tự động | Không có trong luồng; A2 (UC-006, UC-014) | Loại - là tác nhân hoặc ngoài phạm vi | ACT-10 không tham gia UC-013; hành vi huỷ mốc là message cancelTripTriggers của control (ASM-47) |
| 6 | Chuyến, chuyến khớp | Mô tả; bước 1, 2, 3, 5; Dữ liệu vào 1; Dữ liệu ra 1 #1; Dữ liệu ra 3 #1 | Entity (AC-E-Trip) | GL-04; hệ thống lưu chuyến, Trip kiểm tra trạng thái và giờ xuất bến, chuyển sang đã huỷ và nắm tập vé, đặt chỗ của chuyến; tái dùng mã từ UC-002 |
| 7 | Lịch chạy | Bước 2, 2a; Dữ liệu vào 1 #2 | Loại - không tham gia hành vi của use case này (khái niệm của UC-012) | GL-19 là tập các chuyến do UC-012 xếp; UC-013 chỉ tìm chuyến trong tập đó qua Trip.findTrip, không đọc hay ghi lịch chạy như một đối tượng riêng |
| 8 | Tuyến | Bước 1, 2; Dữ liệu vào 1 #1; Dữ liệu ra 1 #1 | Entity (AC-E-Route) | GL-36; Trip dùng Route để kiểm tra tuyến khớp tuyến đã chỉ định (checkRouteMatches), như UC-002; tái dùng mã từ UC-002 |
| 9 | Điểm đi, điểm đến | Dữ liệu vào 1 #1; Dữ liệu ra 1 #1 | Loại - thuộc tính của Route | departurePoint, arrivalPoint |
| 10 | Ngày xuất bến, giờ xuất bến, thời điểm hiện tại | Bước 2; Dữ liệu vào 1 #2, #3; Dữ liệu ra 1 #1 | Loại - thuộc tính của Trip | departureTime; GL-10 (phần ngày gọi là ngày xuất bến). Thời điểm hiện tại chỉ là tham số của message checkBeforeDeparture |
| 11 | Tuyến và giờ xuất bến | Dữ liệu ra 1 #1; Dữ liệu ra 2 #2; Dữ liệu ra 3 #1 | Loại - trùng hoặc đồng nghĩa với tuyến, giờ xuất bến | Gọi chung hai khái niệm đã xét |
| 12 | Trạng thái chuyến (đã huỷ) | Bước 2, 2b, 5; hậu điều kiện | Loại - thuộc tính của Trip | status; ASM-26 |
| 13 | Vé, vé còn hiệu lực | Bước 3, 5, 5a, 6, 10; BR-10, BR-17, BR-18, BR-19 | Entity (AC-E-Ticket) | GL-37, GL-38; hệ thống lưu vé, Ticket chuyển sang đã huỷ, tính số tiền hoàn 100%, xác định hình thức hoàn; tái dùng mã từ UC-002 |
| 14 | Mã vé | Dữ liệu ra 2 #1; Dữ liệu ra 3 #9; BR-10 | Loại - thuộc tính của Ticket | ticketCode; GL-22 |
| 15 | Trạng thái vé (đã huỷ) | Bước 5; Dữ liệu ra 3 #2; hậu điều kiện | Loại - thuộc tính của Ticket | status; GL-39 Vé đã huỷ là một giá trị |
| 16 | Kênh mua (vé mua trực tuyến, vé mua tại quầy) | Bước 3, 6; Dữ liệu ra 1 #2, #3; BR-15, BR-16 | Loại - thuộc tính của Ticket | purchaseChannel; GL-13 |
| 17 | Quầy bán vé, quầy | Bước 6, 9; BR-16 | Loại - trùng hoặc đồng nghĩa với kênh mua giá trị Tại quầy | GL-29 ứng với giá trị Tại quầy của GL-13 |
| 18 | Website, trực tuyến | BR-15 | Loại - trùng hoặc đồng nghĩa với kênh mua giá trị Trực tuyến | Kênh giao diện của chính hệ thống (P01 Mục 4) |
| 19 | Giá vé | Bước 6; Dữ liệu ra 2 #4; BR-17 | Loại - thuộc tính của Ticket | price; GL-08; là số tiền đã thanh toán khi mua (ASM-22) |
| 20 | 100% | Bước 6; BR-17, BR-19 | Loại - tham số của quy tắc BR-17 | Mức hoàn cố định nằm trong quy tắc |
| 21 | Mức hoàn | Bước 9; Dữ liệu ra 2 #4 | Loại - thuộc tính của Refund | refundRate; GL-24 |
| 22 | Số tiền hoàn, tổng số tiền hoàn | Bước 3, 6, 7, 10; Dữ liệu ra 1 #5; Dữ liệu ra 2 #4; Dữ liệu ra 3 #6 | Loại - thuộc tính của Refund | refundAmount; GL-16. Tổng số tiền hoàn là số liệu tổng hợp hiển thị, không lưu |
| 23 | Khoản hoàn tiền | Bước 8a, 9; hậu điều kiện | Entity (AC-E-Refund) | GL-16; hệ thống ghi nhận và lưu khoản hoàn của mỗi vé đã huỷ sau lần thực hiện use case (ASM-48); tái dùng mã từ UC-008 |
| 24 | Hình thức hoàn | Bước 6, 10; Dữ liệu ra 2 #5 | Loại - thuộc tính của Refund | refundMethod; hai giá trị Qua cổng thanh toán, Tiền mặt tại quầy theo BR-15, BR-16 |
| 25 | Kết quả hoàn tiền, khoản hoàn chưa thành công | Bước 8, 8a, 9; Dữ liệu ra 3 #4, #9 | Loại - thuộc tính của Refund | refundResult; ba giá trị đã hoàn, chưa thành công, chờ chi tiền mặt (ASM-48) |
| 26 | Tiền mặt | Bước 9; BR-16 | Loại - thuộc tính của Refund | Giá trị của hình thức hoàn (Tiền mặt tại quầy) |
| 27 | Yêu cầu hoàn tiền | Bước 7 | Loại - thao tác hoặc sự kiện | Message requestRefund tới PaymentGateway, hệ thống không lưu |
| 28 | Đặt chỗ qua điện thoại (chưa thanh toán) | Bước 3, 5; Dữ liệu ra 1 #4; Dữ liệu ra 3 #7 | Entity (AC-E-PhoneReservation) | GL-07; hệ thống lưu đặt chỗ, PhoneReservation xác định chưa thanh toán và chuyển sang đã huỷ cùng chuyến (ASM-27); chưa có mã trong sổ AC vì UC-004, UC-005, UC-006 chưa có P07 |
| 29 | Số điện thoại người đi | Bước 10; ASM-30 | Loại - thuộc tính của Ticket | travelerPhone |
| 30 | Người đi, hành khách đã có vé, mọi hành khách | Bước 10; BR-18, BR-19 | Loại - là tác nhân hoặc ngoài phạm vi | GL-26 là bên liên quan SH-03, không là tác nhân; chỉ số điện thoại là thuộc tính của Ticket |
| 31 | Tin nhắn báo huỷ chuyến, nội dung tin nhắn | Bước 10; Dữ liệu ra 2; BR-18 | Loại - thao tác hoặc sự kiện | GL-30; nội dung dựng từ dữ liệu vé khi gửi (getTripCancelSmsContent), hệ thống không lưu |
| 32 | Câu báo chuyến đã bị huỷ, thông báo | Bước 2a, 2b, 2c, 4a; Dữ liệu ra 2 #3 | Loại - thao tác hoặc sự kiện | Là việc hiển thị của boundary (các message show...Notice); nội dung thông điệp thuộc P11a |
| 33 | Số vé, số đặt chỗ, số tin nhắn, số vé theo kết quả hoàn | Bước 3, 11; Dữ liệu ra 1 #2 đến #4; Dữ liệu ra 3 #2 đến #5, #7, #8 | Loại - thao tác hoặc sự kiện | Số liệu tổng hợp hiển thị của một lần thực hiện, không lưu |
| 34 | Danh sách mã vé hoàn không thành công, danh sách vé đã huỷ | Bước 5; Dữ liệu ra 3 #9 | Loại - cấu trúc cài đặt | Danh sách là kết quả tạm của lần thực hiện, không là khái niệm nghiệp vụ |
| 35 | Kết quả huỷ chuyến | Bước 11; Dữ liệu ra 3 | Loại - thao tác hoặc sự kiện | Là nội dung hiển thị của showCancelTripResult |
| 36 | Định dạng hiển thị (HH:mm dd/MM/yyyy, số nguyên, "đ") | Dữ liệu ra 1, 2, 3 | Loại - cấu trúc cài đặt | Định dạng hiển thị thuộc P11a |
| 37 | Xe hỏng, thời tiết (lý do huỷ chuyến) | Mô tả ngắn; sự kiện kích hoạt EV-17 | Loại - là tác nhân hoặc ngoài phạm vi | P01 Mục 4: sự kiện bên ngoài do nhân viên điều hành nhận biết; hệ thống không ghi lý do (ASM-29) |
| 38 | Nhà xe | BR-17 | Loại - là tác nhân hoặc ngoài phạm vi | SH-01, bên liên quan, không tương tác trực tiếp |
| 39 | Phiên làm việc, xác thực | Tiền điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | Điều kiện đã có trước use case (ASM-09), không có hành vi trong UC-013 |
| 40 | Chỗ, lần đặt trực tuyến đang giữ chỗ | Mục 8 của P04; Dữ liệu ra 3 | Loại - thuộc phân tích của UC-002 | Lần đặt giữ chỗ do UC-002 tạo và xử lý; UC-013 không đọc hay ghi chỗ hay lần đặt (chờ Q-44) |

### 3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| CancelTripController (AC-C-CancelTripController) | UC-013 Huỷ chuyến | Mới | Một control cho use case, đặt tên theo tên tiếng Anh của use case (Cancel Trip) với hậu tố Controller (HAU_TO_TEN_LOP là Mặc định). Điều phối trình tự 11 bước, huỷ mốc kích hoạt tự động của UC-006, UC-014 (A2), không giữ dữ liệu nghiệp vụ lâu dài |

### 3.4 Bảng lớp phân tích
| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-CancelTripForm | boundary | CancelTripForm | // requestCancelTrip: nhận yêu cầu huỷ chuyến và tuyến, ngày xuất bến, giờ xuất bến của chuyến từ tác nhân<br>// confirmCancelTrip: nhận xác nhận huỷ chuyến của tác nhân<br>// declineCancelTrip: nhận việc tác nhân không xác nhận huỷ chuyến<br>// showCancelTripInfo: hiển thị tuyến, giờ xuất bến, số vé theo kênh mua, số đặt chỗ chưa thanh toán và tổng số tiền hoàn<br>// showTripNotFoundNotice: thông báo không có chuyến khớp thông tin đã chỉ định<br>// showTripAlreadyCancelledNotice: thông báo chuyến đã bị huỷ<br>// showTripDepartedNotice: thông báo chuyến đã tới giờ xuất bến<br>// showCancelTripAbortedNotice: thông báo yêu cầu huỷ chuyến đã được bỏ, chuyến giữ nguyên<br>// showCancelTripResult: hiển thị kết quả huỷ chuyến | departurePoint, arrivalPoint, departureDate, departureTime | 1, 2a, 2b, 2c, 3, 4, 4a, 11 | Giao diện người dùng | Mới | - |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestRefund: gửi yêu cầu hoàn số tiền hoàn của vé tới Cổng thanh toán<br>// returnRefundResult: nhận kết quả hoàn tiền từ Cổng thanh toán | ticketCode, refundAmount | 7, 8 | Giao diện hệ thống | Tái dùng từ UC-008 | GL-16 |
| AC-B-SmsGateway | boundary | SmsGateway | // sendTripCancelSms: gửi nội dung tin nhắn báo huỷ chuyến tới số điện thoại người đi qua Cổng SMS | recipientPhone, smsContent | 10 | Giao diện hệ thống | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-30 |
| AC-C-CancelTripController | control | CancelTripController | // startCancelTrip: điều phối tìm chuyến, kiểm tra điều kiện huỷ và hiển thị thông tin huỷ chuyến<br>// confirmCancel: điều phối huỷ chuyến, hoàn tiền, gửi tin nhắn và thông báo kết quả<br>// cancelCancelTripRequest: kết thúc yêu cầu huỷ chuyến khi tác nhân không xác nhận<br>// cancelTripTriggers: huỷ các mốc kích hoạt tự động của UC-006 và UC-014 tính từ giờ xuất bến của chuyến đã huỷ (ASM-47) | - | 1-11, 4a | - | Mới | - |
| AC-E-Trip | entity | Trip | // findTrip: tìm chuyến trong lịch chạy khớp tuyến, ngày xuất bến và giờ xuất bến đã chỉ định<br>// checkNotCancelled: kiểm tra chuyến chưa ở trạng thái đã huỷ (ASM-26)<br>// checkBeforeDeparture: kiểm tra thời điểm hiện tại chưa tới giờ xuất bến (ASM-24)<br>// getCancellationSummary: tổng hợp tuyến, giờ xuất bến, số vé còn hiệu lực theo kênh mua, số đặt chỗ chưa thanh toán và tổng số tiền hoàn (BR-17)<br>// cancelTrip: chuyển chuyến sang đã huỷ và yêu cầu vé còn hiệu lực, đặt chỗ chưa thanh toán của chuyến cùng chuyển sang đã huỷ (ASM-26, ASM-27)<br>// getRouteAndDepartureTime: cung cấp tuyến và giờ xuất bến của chuyến | departureTime, status | 2, 3, 5, 10 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-04, GL-10, GL-19 |
| AC-E-Route | entity | Route | // checkRouteMatches: kiểm tra điểm đi, điểm đến của tuyến khớp tuyến đã chỉ định | departurePoint, arrivalPoint | 2 | - | Tái dùng từ UC-002 | GL-36 |
| AC-E-Ticket | entity | Ticket | // getCancelImpactInfo: cung cấp kênh mua và số tiền hoàn bằng 100% giá vé của vé còn hiệu lực (BR-17)<br>// cancelWithTrip: chuyển vé sang đã huỷ do chuyến bị huỷ (ASM-26)<br>// calculateTripCancelRefundAmount: tính số tiền hoàn bằng 100% giá vé đã thanh toán (BR-17, ASM-22)<br>// determineRefundMethod: xác định hình thức hoàn theo kênh mua (BR-15, BR-16)<br>// recordRefund: ghi nhận khoản hoàn của vé với số tiền hoàn, hình thức hoàn và kết quả hoàn (ASM-48)<br>// getTripCancelSmsContent: lập nội dung tin nhắn báo huỷ chuyến gồm mã vé, tuyến, giờ xuất bến, số tiền hoàn, hình thức hoàn (ASM-29) | ticketCode, travelerPhone, price, status, purchaseChannel | 3, 5, 6, 8a, 9, 10 | - | Tái dùng từ UC-002, bổ sung trách nhiệm | GL-08, GL-13, GL-22, GL-37, GL-38, GL-39 |
| AC-E-PhoneReservation | entity | PhoneReservation | // checkUnpaid: xác định đặt chỗ qua điện thoại chưa thanh toán (ASM-27)<br>// cancelWithTrip: chuyển đặt chỗ chưa thanh toán sang đã huỷ cùng chuyến (ASM-27) | status | 3, 5 | - | Mới | GL-07 |
| AC-E-Refund | entity | Refund | // createRefund: khởi tạo khoản hoàn tiền của vé đã huỷ, ghi mức hoàn, số tiền hoàn, hình thức hoàn và kết quả hoàn | refundAmount, refundRate, refundMethod, refundResult | 8a, 9 | - | Tái dùng từ UC-008 | GL-16, GL-24 |

Số lớp: 9 (3 boundary, 1 control, 5 entity), trong đó 6 lớp tái dùng từ UC-002, UC-008 (PaymentGateway, SmsGateway, Trip, Route, Ticket, Refund) và 3 lớp mới (CancelTripForm, CancelTripController, PhoneReservation). Thuộc tính có kiểu khái niệm: departureDate (Ngày), departureTime (Giờ), status (Trạng thái), purchaseChannel (Trạng thái, giá trị Trực tuyến hoặc Tại quầy), price và refundAmount (Số tiền), refundRate (Số lượng, đơn vị phần trăm), refundMethod (Trạng thái, giá trị Qua cổng thanh toán hoặc Tiền mặt tại quầy), refundResult (Trạng thái, giá trị đã hoàn, chưa thành công, chờ chi tiền mặt), các thuộc tính còn lại là Văn bản. Trách nhiệm getRouteAndDepartureTime của Trip, checkRouteMatches của Route, determineRefundMethod của Ticket, requestRefund và returnRefundResult của PaymentGateway, createRefund của Refund được dùng lại đúng tên của UC-002, UC-008.

## 4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc (Giao tiếp tác nhân / Information Expert / Controller / Creator / Lớp mới / Giao cho control) | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestCancelTrip | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 1 | // startCancelTrip | AC-C-CancelTripController | Controller | - |
| 2 | // findTrip | AC-E-Trip | Information Expert | Tuyến, ngày xuất bến và giờ xuất bến của chuyến nằm ở Trip và Route. Giao cho Trip và thêm quan hệ tới Route (giống UC-002); giao cho control bị loại vì control sẽ phải đọc dữ liệu của chuyến |
| 2 | // checkRouteMatches | AC-E-Route | Information Expert | Điểm đi, điểm đến nằm ở Route |
| 2 | // checkNotCancelled | AC-E-Trip | Information Expert | Trạng thái chuyến nằm ở Trip |
| 2 | // checkBeforeDeparture | AC-E-Trip | Information Expert | Giờ xuất bến nằm ở Trip |
| 2a | // showTripNotFoundNotice | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 2b | // showTripAlreadyCancelledNotice | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 2c | // showTripDepartedNotice | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 3 | // getCancellationSummary | AC-E-Trip | Information Expert | Dữ liệu nằm ở nhiều lớp (chuyến, vé, đặt chỗ). Giao cho Trip vì Trip có quan hệ tới Ticket và PhoneReservation của chuyến; giao cho control bị loại vì control sẽ phải duyệt vé và đặt chỗ của chuyến (god control); tạo lớp mới như TripCancellation bị loại vì số liệu chỉ là tổng hợp tạm của một lần thực hiện, không có định danh và dữ liệu riêng |
| 3 | // getCancelImpactInfo | AC-E-Ticket | Information Expert | Kênh mua và giá vé nằm ở Ticket |
| 3 | // checkUnpaid | AC-E-PhoneReservation | Information Expert | Trạng thái thanh toán của đặt chỗ nằm ở PhoneReservation |
| 3 | // showCancelTripInfo | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 4 | // confirmCancelTrip | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 4 | // confirmCancel | AC-C-CancelTripController | Controller | - |
| 4a | // declineCancelTrip | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 4a | // cancelCancelTripRequest | AC-C-CancelTripController | Controller | - |
| 4a | // showCancelTripAbortedNotice | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 5 | // cancelTrip | AC-E-Trip | Information Expert | Dữ liệu nằm ở nhiều lớp (chuyến, vé, đặt chỗ). Giao cho Trip vì Trip đổi trạng thái của chính nó và nắm tập vé, đặt chỗ của chuyến qua quan hệ; giao cho control bị loại vì control sẽ phải duyệt và đổi trạng thái từng vé, đặt chỗ (god control) |
| 5 | // cancelWithTrip | AC-E-Ticket | Information Expert | Trạng thái vé nằm ở Ticket |
| 5 | // cancelWithTrip | AC-E-PhoneReservation | Information Expert | Trạng thái đặt chỗ nằm ở PhoneReservation |
| 5 | // cancelTripTriggers | AC-C-CancelTripController | Giao cho control | Mốc kích hoạt của UC-006, UC-014 không thuộc dữ liệu của entity nào của use case này (A2). Giao cho Trip bị loại vì Trip sẽ phải biết cơ chế lập lịch mà mức phân tích không chọn (P12 thiết kế) |
| 5a | (không có message riêng) | AC-C-CancelTripController | Controller | Control bỏ qua bước 6 đến 10 khi không có vé còn hiệu lực (fragment opt FR1 trong SD1) |
| 6 | // calculateTripCancelRefundAmount | AC-E-Ticket | Information Expert | Giá vé nằm ở Ticket nên Ticket tính số tiền hoàn. Giao cho Refund bị loại vì khoản hoàn chỉ được tạo ở bước 9 (ASM-48), trước đó chưa có đối tượng Refund |
| 6 | // determineRefundMethod | AC-E-Ticket | Information Expert | Kênh mua nằm ở Ticket |
| 6a | (không có message tới PaymentGateway) | AC-C-CancelTripController | Controller | Control bỏ qua nhánh hoàn qua cổng khi hình thức hoàn là Tiền mặt tại quầy (fragment opt FR3 trong SD1) |
| 7 | // requestRefund | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 8 | // returnRefundResult | AC-B-PaymentGateway | Giao tiếp tác nhân | Kết quả do ACT-06 trả về boundary của nó |
| 8a | // recordRefund | AC-E-Ticket | Information Expert | Xem bước 9; kết quả hoàn chưa thành công cũng được ghi thành khoản hoàn (ASM-31, ASM-48), vẽ ở SD4 |
| 9 | // recordRefund | AC-E-Ticket | Information Expert | Dữ liệu nằm ở nhiều lớp (vé, khoản hoàn). Giao cho Ticket vì Ticket giữ giá vé, kênh mua và có quan hệ tới Refund; giao cho control bị loại để control không giữ dữ liệu nghiệp vụ |
| 9 | // createRefund | AC-E-Refund | Creator | Ticket có dữ liệu khởi tạo (mức hoàn, số tiền hoàn, hình thức hoàn, kết quả hoàn) nên Ticket gửi message Tạo |
| 10 | // getTripCancelSmsContent | AC-E-Ticket | Information Expert | Mã vé và số điện thoại người đi nằm ở Ticket. Số tiền hoàn và hình thức hoàn do control truyền vào vì control đã nhận ở bước 6; giao cho Refund bị loại để Ticket không phải truy cập thêm Refund |
| 10 | // getRouteAndDepartureTime | AC-E-Trip | Information Expert | Tuyến và giờ xuất bến nằm ở Trip |
| 10 | // sendTripCancelSms | AC-B-SmsGateway | Giao tiếp tác nhân | - |
| 11 | // showCancelTripResult | AC-B-CancelTripForm | Giao tiếp tác nhân | Số liệu kết quả do control tổng hợp tạm từ các kết quả trả về trong lần thực hiện, không lưu |

Bước 5a và 6a không có hành động (cột Thực hiện bởi của P04 ghi "-"), nên chỉ có dòng ghi nhận việc control bỏ qua nhánh.

## 5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-013.drawio gồm bốn trang. SD1 thể hiện luồng chính cùng luồng 5a (fragment opt bỏ qua bước 6 đến 10) và 6a (fragment opt bỏ qua bước 7, 8). SD2 thể hiện luồng 2a, 2b, 2c; SD3 thể hiện luồng 4a; SD4 thể hiện luồng 8a. Mọi luồng thay thế kết thúc use case (2b, 2c, 4a) dùng fragment break; luồng 2a quay lại bước 1 dùng alt; luồng 8a tiếp tục bước 9 dùng alt. Message ở SD2, SD3, SD4 mang STT của message cùng điểm rẽ nhánh trong SD1 kèm hậu tố a (ví dụ 1.1.1a là nhánh của message 1.1.1).

Bảng message dùng thêm cột ID (ID cell trong file .drawio). Lifeline Refund có đỉnh đặt ngang message Tạo (SD1: 2.1.6.1; SD4: 2.1.6a.1). Trang có fragment bắt đầu message đầu tiên ở y thấp hơn mức mặc định 40 để chừa chỗ nhãn của fragment. Bước 5a và 6a không có hành động (P04 ghi "-") nên thể hiện bằng fragment opt; bước 8a thể hiện ở SD4.

### SD1 - Luồng chính, 5a, 6a

a) Tên sơ đồ và luồng thể hiện: luồng chính (bước 1 đến 11), luồng 5a (opt bỏ qua bước 6 đến 10) và luồng 6a (opt bỏ qua bước 7, 8).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1-L01 | Actor | Nhân viên điều hành | ACT-03 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 1730 |
| SD1-L02 | Lifeline | :CancelTripForm | boundary | - | Boundary của ACT-03 | 200 | 40 | 120 | 1730 |
| SD1-L03 | Lifeline | :CancelTripController | control | - | Control của UC-013 | 360 | 40 | 120 | 1730 |
| SD1-L04 | Lifeline | :Trip | entity | - | Chuyến cần huỷ | 520 | 40 | 120 | 1730 |
| SD1-L05 | Lifeline | :Route | entity | - | Tuyến của chuyến | 680 | 40 | 120 | 1730 |
| SD1-L06 | Lifeline | :Ticket | entity | - | Một đối tượng cho mỗi vé; ở bước 6 đến 10 là vé đã huỷ | 840 | 40 | 120 | 1730 |
| SD1-L07 | Lifeline | :PhoneReservation | entity | - | Một đối tượng cho mỗi đặt chỗ qua điện thoại của chuyến | 1000 | 40 | 120 | 1730 |
| SD1-L08 | Lifeline | :Refund | entity | - | Được tạo bởi message 2.1.6.1, một đối tượng cho mỗi vé đã huỷ | 1160 | 1380 | 120 | 390 |
| SD1-L09 | Lifeline | :PaymentGateway | boundary | - | Boundary của ACT-06 | 1320 | 40 | 120 | 1730 |
| SD1-L10 | Lifeline | :SmsGateway | boundary | - | Boundary của ACT-07 | 1480 | 40 | 120 | 1730 |
| SD1-L11 | Actor | Cổng thanh toán | ACT-06 (Hệ thống ngoài) | - | Tác nhân phụ | 1640 | 40 | 120 | 1730 |
| SD1-L12 | Actor | Cổng SMS | ACT-07 (Hệ thống ngoài) | - | Tác nhân phụ | 1800 | 40 | 120 | 1730 |
| SD1-FR1 | Fragment | opt [có vé còn hiệu lực (luồng 5a)] | opt | - | Luồng 5a, tiếp tục bước 11 khi không có vé còn hiệu lực | 320 | 880 | 1630 | 800 |
| SD1-FR2 | Fragment | loop [với từng vé đã huỷ (bước 6 đến 9)] | loop | SD1-FR1 | Mỗi vé đã huỷ một lần lặp (ASM-29, P04 "với từng vé") | 330 | 920 | 1460 | 490 |
| SD1-FR3 | Fragment | opt [hình thức hoàn là Qua cổng thanh toán (BR-15)] | opt | SD1-FR2 | Luồng 6a: vé mua tại quầy bỏ qua bước 7, 8, tiếp tục bước 9 | 340 | 1120 | 1440 | 190 |
| SD1-FR4 | Fragment | loop [với từng vé đã huỷ (bước 10)] | loop | SD1-FR1 | Mỗi vé đã huỷ một tin nhắn (BR-18, ASM-29) | 340 | 1440 | 1600 | 230 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1-M01 | 1 | SD1-L01 | SD1-L02 | // requestCancelTrip (tuyến, ngày xuất bến, giờ xuất bến) | Đồng bộ | - | 1 |
| SD1-M02 | 1.1 | SD1-L02 | SD1-L03 | // startCancelTrip (tuyến, ngày xuất bến, giờ xuất bến) | Đồng bộ | - | 1 |
| SD1-M03 | 1.1.1 | SD1-L03 | SD1-L04 | // findTrip (tuyến, ngày xuất bến, giờ xuất bến) | Đồng bộ | - | 2 |
| SD1-M04 | 1.1.1.1 | SD1-L04 | SD1-L05 | // checkRouteMatches (tuyến) | Đồng bộ | - | 2 |
| SD1-M05 | 1.1.1 (trả về) | SD1-L04 | SD1-L03 | chuyến khớp thông tin đã chỉ định | Trả về | - | 2 |
| SD1-M06 | 1.1.2 | SD1-L03 | SD1-L04 | // checkNotCancelled | Đồng bộ | - | 2 |
| SD1-M07 | 1.1.3 | SD1-L03 | SD1-L04 | // checkBeforeDeparture (thời điểm hiện tại) | Đồng bộ | - | 2 |
| SD1-M08 | 1.1.4 | SD1-L03 | SD1-L04 | // getCancellationSummary | Đồng bộ | - | 3 |
| SD1-M09 | 1.1.4.1 | SD1-L04 | SD1-L06 | // getCancelImpactInfo (từng vé còn hiệu lực của chuyến, BR-17) | Đồng bộ | - | 3 |
| SD1-M10 | 1.1.4.2 | SD1-L04 | SD1-L07 | // checkUnpaid (từng đặt chỗ qua điện thoại của chuyến) | Đồng bộ | - | 3 |
| SD1-M11 | 1.1.4 (trả về) | SD1-L04 | SD1-L03 | tuyến, giờ xuất bến, số vé theo kênh mua, số đặt chỗ chưa thanh toán, tổng số tiền hoàn | Trả về | - | 3 |
| SD1-M12 | 1.1.5 | SD1-L03 | SD1-L02 | // showCancelTripInfo (tuyến, giờ xuất bến, số vé theo kênh mua, số đặt chỗ chưa thanh toán, tổng số tiền hoàn) | Đồng bộ | - | 3 |
| SD1-M13 | 2 | SD1-L01 | SD1-L02 | // confirmCancelTrip | Đồng bộ | - | 4 |
| SD1-M14 | 2.1 | SD1-L02 | SD1-L03 | // confirmCancel | Đồng bộ | - | 4 |
| SD1-M15 | 2.1.1 | SD1-L03 | SD1-L04 | // cancelTrip | Đồng bộ | - | 5 |
| SD1-M16 | 2.1.1.1 | SD1-L04 | SD1-L06 | // cancelWithTrip (từng vé còn hiệu lực, ASM-26) | Đồng bộ | - | 5 |
| SD1-M17 | 2.1.1.2 | SD1-L04 | SD1-L07 | // cancelWithTrip (từng đặt chỗ chưa thanh toán, ASM-27) | Đồng bộ | - | 5 |
| SD1-M18 | 2.1.1 (trả về) | SD1-L04 | SD1-L03 | danh sách vé đã huỷ | Trả về | - | 5 |
| SD1-M19 | 2.1.2 | SD1-L03 | SD1-L03 | // cancelTripTriggers (chuyến, mốc của UC-006 và UC-014, ASM-47) | Tự gọi | - | 5 |
| SD1-M20 | 2.1.3 | SD1-L03 | SD1-L06 | // calculateTripCancelRefundAmount (BR-17) | Đồng bộ | SD1-FR2 | 6 |
| SD1-M21 | 2.1.3 (trả về) | SD1-L06 | SD1-L03 | số tiền hoàn bằng 100% giá vé | Trả về | SD1-FR2 | 6 |
| SD1-M22 | 2.1.4 | SD1-L03 | SD1-L06 | // determineRefundMethod | Đồng bộ | SD1-FR2 | 6 |
| SD1-M23 | 2.1.4 (trả về) | SD1-L06 | SD1-L03 | hình thức hoàn theo kênh mua | Trả về | SD1-FR2 | 6 |
| SD1-M24 | 2.1.5 | SD1-L03 | SD1-L09 | // requestRefund (mã vé, số tiền hoàn) | Đồng bộ | SD1-FR3 | 7 |
| SD1-M25 | 2.1.5.1 | SD1-L09 | SD1-L11 | // submitRefundRequest (mã vé, số tiền hoàn) | Đồng bộ | SD1-FR3 | 7 |
| SD1-M26 | 2.1.5.2 | SD1-L11 | SD1-L09 | // returnRefundResult (kết quả hoàn tiền) | Đồng bộ | SD1-FR3 | 8 |
| SD1-M27 | 2.1.5 (trả về) | SD1-L09 | SD1-L03 | kết quả hoàn tiền | Trả về | SD1-FR3 | 8 |
| SD1-M28 | 2.1.6 | SD1-L03 | SD1-L06 | // recordRefund (số tiền hoàn, hình thức hoàn, kết quả hoàn) | Đồng bộ | SD1-FR2 | 9 |
| SD1-M29 | 2.1.6.1 | SD1-L06 | SD1-L08 | // createRefund (vé, mức hoàn 100%, số tiền hoàn, hình thức hoàn, kết quả hoàn) | Tạo | SD1-FR2 | 9 |
| SD1-M30 | 2.1.7 | SD1-L03 | SD1-L06 | // getTripCancelSmsContent (số tiền hoàn, hình thức hoàn) | Đồng bộ | SD1-FR4 | 10 |
| SD1-M31 | 2.1.7.1 | SD1-L06 | SD1-L04 | // getRouteAndDepartureTime | Đồng bộ | SD1-FR4 | 10 |
| SD1-M32 | 2.1.7 (trả về) | SD1-L06 | SD1-L03 | nội dung tin nhắn và số điện thoại người đi | Trả về | SD1-FR4 | 10 |
| SD1-M33 | 2.1.8 | SD1-L03 | SD1-L10 | // sendTripCancelSms (nội dung tin nhắn, số điện thoại người đi) | Đồng bộ | SD1-FR4 | 10 |
| SD1-M34 | 2.1.8.1 | SD1-L10 | SD1-L12 | // deliverSms (nội dung tin nhắn, số điện thoại người đi) | Đồng bộ | SD1-FR4 | 10 |
| SD1-M35 | 2.1.9 | SD1-L03 | SD1-L02 | // showCancelTripResult (tuyến, giờ xuất bến, số vé đã huỷ, số vé theo kết quả hoàn, tổng số tiền hoàn, số đặt chỗ đã huỷ, số tin nhắn đã gửi, mã vé hoàn không thành công) | Đồng bộ | - | 11 |

SD1 có 35 dòng message, trong đó 7 message trả về; 1 fragment ngoài cùng. Ngưỡng F5: 28 message không kể trả về (không quá khoảng 30), 1 fragment ngoài cùng (opt FR1) chứa loop FR2, loop FR4 và opt FR3 lồng bên trong. Message 2.1.2 là message tự gọi của control huỷ mốc kích hoạt của UC-006, UC-014 (A2). Bước 9a của luồng 8a được vẽ ở SD4.

### SD2 - Luồng 2a, 2b, 2c

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 2a (quay lại bước 1, alt) và 2b, 2c (kết thúc use case, break).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD2-L01 | Lifeline | :CancelTripForm | boundary | - | Boundary của ACT-03 | 40 | 40 | 120 | 530 |
| SD2-L02 | Lifeline | :CancelTripController | control | - | Control của UC-013 | 200 | 40 | 120 | 530 |
| SD2-L03 | Lifeline | :Trip | entity | - | Chuyến cần huỷ | 360 | 40 | 120 | 530 |
| SD2-FR1 | Fragment | alt [không có chuyến nào khớp tuyến, ngày và giờ xuất bến đã chỉ định (ASM-24)] | alt | - | Điểm rẽ nhánh: sau 1.1.1 (trả về) của SD1. Luồng 2a quay lại bước 1. Toán hạng 1 | 20 | 120 | 480 | 150 |
| SD2-FR1-O2 | Fragment | [có chuyến khớp thông tin đã chỉ định] | alt | SD2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SD2-FR1-O2-SEP | 30 | 200 | 460 | 20 |
| SD2-FR2 | Fragment | break [chuyến khớp đã bị huỷ trước đó (ASM-26)] | break | - | Điểm rẽ nhánh: sau 1.1.2 của SD1. Luồng 2b kết thúc use case (thất bại) | 20 | 300 | 320 | 70 |
| SD2-FR3 | Fragment | break [chuyến chưa huỷ, đã tới hoặc đã qua giờ xuất bến (ASM-24)] | break | - | Điểm rẽ nhánh: sau 1.1.3 của SD1. Luồng 2c kết thúc use case (thất bại) | 20 | 440 | 320 | 70 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2-M01 | 1.1.1a | SD2-L02 | SD2-L01 | // showTripNotFoundNotice | Đồng bộ | SD2-FR1 | 2a |
| SD2-M02 | 1.1.2 | SD2-L02 | SD2-L03 | // checkNotCancelled | Đồng bộ | SD2-FR1 | 2 |
| SD2-M03 | 1.1.2a | SD2-L02 | SD2-L01 | // showTripAlreadyCancelledNotice | Đồng bộ | SD2-FR2 | 2b |
| SD2-M04 | 1.1.3 | SD2-L02 | SD2-L03 | // checkBeforeDeparture (thời điểm hiện tại) | Đồng bộ | - | 2 |
| SD2-M05 | 1.1.3a | SD2-L02 | SD2-L01 | // showTripDepartedNotice | Đồng bộ | SD2-FR3 | 2c |

SD2 có 5 dòng message, trong đó 0 message trả về; 3 fragment ngoài cùng. Hai toán hạng của alt loại trừ nhau; toán hạng 2 lặp lại message 1.1.2 của luồng chính để guard có đủ hai toán hạng. Message 1.1.3 nằm ngoài fragment để ghi điểm rẽ nhánh của luồng 2c. Luồng 2a quay lại bước 1: sau toán hạng 1 nhân viên điều hành chỉ định lại chuyến (message 1 của SD1).

### SD3 - Luồng 4a

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 4a (kết thúc use case, break).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD3-L01 | Actor | Nhân viên điều hành | ACT-03 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 290 |
| SD3-L02 | Lifeline | :CancelTripForm | boundary | - | Boundary của ACT-03 | 200 | 40 | 120 | 290 |
| SD3-L03 | Lifeline | :CancelTripController | control | - | Control của UC-013 | 360 | 40 | 120 | 290 |
| SD3-FR1 | Fragment | break [tác nhân không xác nhận huỷ chuyến (ASM-25)] | break | - | Điểm rẽ nhánh: sau 1.1.5 của SD1, thay cho message 2. Luồng 4a kết thúc use case (thất bại) | 20 | 120 | 480 | 150 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD3-M01 | 2a | SD3-L01 | SD3-L02 | // declineCancelTrip | Đồng bộ | SD3-FR1 | 4a |
| SD3-M02 | 2a.1 | SD3-L02 | SD3-L03 | // cancelCancelTripRequest | Đồng bộ | SD3-FR1 | 4a |
| SD3-M03 | 2a.1.1 | SD3-L03 | SD3-L02 | // showCancelTripAbortedNotice | Đồng bộ | SD3-FR1 | 4a |

SD3 có 3 dòng message, trong đó 0 message trả về; 1 fragment ngoài cùng.

### SD4 - Luồng 8a

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 8a (alt, tiếp tục bước 9 cho vé kế tiếp), toán hạng 2 tham chiếu SD1.

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD4-L01 | Lifeline | :CancelTripController | control | - | Control của UC-013 | 40 | 40 | 120 | 360 |
| SD4-L02 | Lifeline | :Ticket | entity | - | Vé đã huỷ có khoản hoàn không thành công | 200 | 40 | 120 | 360 |
| SD4-L03 | Lifeline | :Refund | entity | - | Được tạo bởi message 2.1.6a.1 | 360 | 200 | 120 | 200 |
| SD4-FR1 | Fragment | alt [kết quả hoàn tiền không thành công của vé (luồng 8a)] | alt | - | Điểm rẽ nhánh: sau 2.1.5 (trả về) của SD1, trong vòng lặp bước 6 đến 9. Luồng 8a tiếp tục bước 9. Toán hạng 1 | 10 | 120 | 500 | 220 |
| SD4-FR1-O2 | Fragment | [kết quả hoàn tiền thành công hoặc hình thức hoàn là Tiền mặt tại quầy] | alt | SD4-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SD4-FR1-O2-SEP | 20 | 240 | 480 | 20 |
| SD4-FR2 | Fragment | ref SD1: 2.1.6 đến 2.1.6.1 (bước 9) | ref | SD4-FR1 | Tham chiếu message recordRefund, createRefund của SD1 | 20 | 280 | 480 | 50 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD4-M01 | 2.1.6a | SD4-L01 | SD4-L02 | // recordRefund (số tiền hoàn, hình thức hoàn Qua cổng thanh toán, kết quả hoàn chưa thành công) | Đồng bộ | SD4-FR1 | 8a |
| SD4-M02 | 2.1.6a.1 | SD4-L02 | SD4-L03 | // createRefund (vé, mức hoàn 100%, số tiền hoàn, hình thức hoàn, kết quả hoàn chưa thành công) | Tạo | SD4-FR1 | 8a |

SD4 có 2 dòng message, trong đó 0 message trả về; 1 fragment ngoài cùng. Toán hạng 2 là fragment ref tới SD1 (message 2.1.6, 2.1.6.1) nên không có message riêng.

## 6. Quy tắc tương tác giữa các lớp phân tích

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

Đã kiểm tra mọi message của SD1 đến SD4 và mọi link của communication diagram theo bảng F6: actor chỉ gửi message tới boundary của mình (ACT-03 --> CancelTripForm, ACT-06 --> PaymentGateway); boundary chỉ trao đổi với actor của nó và control; control gọi boundary, entity và gọi chính nó (cancelTripTriggers); entity chỉ gọi entity có quan hệ cấu trúc (Trip --> Route, Trip --> Ticket, Trip --> PhoneReservation, Ticket --> Trip, Ticket --> Refund). Message 2.1.5.1 từ PaymentGateway tới ACT-06, 2.1.5.2 từ ACT-06 tới PaymentGateway và 2.1.8.1 từ SmsGateway tới ACT-07 là trao đổi giữa actor phụ và boundary của nó. Không có message giữa hai actor, không có message từ control hoặc entity tới actor.

## 7. Communication diagram

File diagrams/P07-communication-UC-013.drawio, phạm vi là luồng chính của SD1 (MUC_CHI_TIET là DAY_DU). Luồng thay thế đã gộp vào SD1 là fragment opt 5a (bỏ qua bước 6 đến 10) và opt 6a (bỏ qua bước 7, 8); các fragment này không thêm message hay STT mới. Luồng 2a, 2b, 2c, 4a, 8a nằm trên trang riêng SD2, SD3, SD4 nên không gộp vào communication diagram. Nhãn link dùng STT của SD1; message trả về không vẽ.

a) Bảng Node:

| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| CO-01 | Actor | Nhân viên điều hành | - | - | Tác nhân chính | 40 | 300 | 40 | 80 |
| CO-02 | Object | :CancelTripForm | boundary | - | Boundary của ACT-03 | 200 | 320 | 160 | 40 |
| CO-03 | Object | :CancelTripController | control | - | Control của UC-013 | 640 | 320 | 160 | 40 |
| CO-04 | Object | :Trip | entity | - | Chuyến cần huỷ | 640 | 600 | 160 | 40 |
| CO-05 | Object | :Route | entity | - | Tuyến của chuyến | 200 | 600 | 160 | 40 |
| CO-06 | Object | :Ticket | entity | - | Vé của chuyến | 1080 | 600 | 160 | 40 |
| CO-07 | Object | :PhoneReservation | entity | - | Đặt chỗ qua điện thoại của chuyến | 640 | 860 | 160 | 40 |
| CO-08 | Object | :Refund | entity | - | Được tạo bởi message 2.1.6.1 | 1080 | 860 | 160 | 40 |
| CO-09 | Object | :PaymentGateway | boundary | - | Boundary của ACT-06 | 1080 | 320 | 160 | 40 |
| CO-10 | Object | :SmsGateway | boundary | - | Boundary của ACT-07 | 1080 | 140 | 160 | 40 |
| CO-11 | Actor | Cổng thanh toán | - | - | Tác nhân phụ | 1480 | 300 | 40 | 80 |
| CO-12 | Actor | Cổng SMS | - | - | Tác nhân phụ | 1480 | 120 | 40 | 80 |

b) Bảng Edge (link):

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message |
|---|---|---|---|---|---|
| LK-01 | CO-01 | CO-02 | Link | 1: // requestCancelTrip (tuyến, ngày xuất bến, giờ xuất bến) (-->)<br>2: // confirmCancelTrip (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-02 | CO-02 | CO-03 | Link | 1.1: // startCancelTrip (tuyến, ngày xuất bến, giờ xuất bến) (-->)<br>1.1.5: // showCancelTripInfo (tuyến, giờ xuất bến, số vé theo kênh mua, số đặt chỗ chưa thanh toán, tổng số tiền hoàn) (<--)<br>2.1: // confirmCancel (-->)<br>2.1.9: // showCancelTripResult (tuyến, giờ xuất bến, số vé đã huỷ, số vé theo kết quả hoàn, tổng số tiền hoàn, số đặt chỗ đã huỷ, số tin nhắn đã gửi, mã vé hoàn không thành công) (<--) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-03 | CO-03 | CO-04 | Link | 1.1.1: // findTrip (tuyến, ngày xuất bến, giờ xuất bến) (-->)<br>1.1.2: // checkNotCancelled (-->)<br>1.1.3: // checkBeforeDeparture (thời điểm hiện tại) (-->)<br>1.1.4: // getCancellationSummary (-->)<br>2.1.1: // cancelTrip (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-04 | CO-04 | CO-05 | Link | 1.1.1.1: // checkRouteMatches (tuyến) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-05 | CO-04 | CO-06 | Link | 1.1.4.1: // getCancelImpactInfo (từng vé còn hiệu lực của chuyến, BR-17) (-->)<br>2.1.1.1: // cancelWithTrip (từng vé còn hiệu lực, ASM-26) (-->)<br>2.1.7.1: // getRouteAndDepartureTime (<--) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-06 | CO-04 | CO-07 | Link | 1.1.4.2: // checkUnpaid (từng đặt chỗ qua điện thoại của chuyến) (-->)<br>2.1.1.2: // cancelWithTrip (từng đặt chỗ chưa thanh toán, ASM-27) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-07 | CO-03 | CO-03 | Link | 2.1.2: // cancelTripTriggers (chuyến, mốc của UC-006 và UC-014, ASM-47) (-->) | Link tự gọi của control |
| LK-08 | CO-03 | CO-06 | Link | 2.1.3: // calculateTripCancelRefundAmount (BR-17) (-->)<br>2.1.4: // determineRefundMethod (-->)<br>2.1.6: // recordRefund (số tiền hoàn, hình thức hoàn, kết quả hoàn) (-->)<br>2.1.7: // getTripCancelSmsContent (số tiền hoàn, hình thức hoàn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-09 | CO-06 | CO-08 | Link | 2.1.6.1: // createRefund (vé, mức hoàn 100%, số tiền hoàn, hình thức hoàn, kết quả hoàn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-10 | CO-03 | CO-09 | Link | 2.1.5: // requestRefund (mã vé, số tiền hoàn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-11 | CO-09 | CO-11 | Link | 2.1.5.1: // submitRefundRequest (mã vé, số tiền hoàn) (-->)<br>2.1.5.2: // returnRefundResult (kết quả hoàn tiền) (<--) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-12 | CO-03 | CO-10 | Link | 2.1.8: // sendTripCancelSms (nội dung tin nhắn, số điện thoại người đi) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-13 | CO-10 | CO-12 | Link | 2.1.8.1: // deliverSms (nội dung tin nhắn, số điện thoại người đi) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |

Tổng số message trên các link: 28 (bằng số message không phải trả về của SD1: 28). LK-07 là link tự gọi của control (message 2.1.2); không vào VOPC.

## 8. VOPC

File diagrams/P07-class-UC-013.drawio.

a) Bảng Node (lớp):

| ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-B-CancelTripForm | Class | CancelTripForm | «boundary» | - | departurePoint<br>arrivalPoint<br>departureDate<br>departureTime | // requestCancelTrip<br>// confirmCancelTrip<br>// declineCancelTrip<br>// showCancelTripInfo<br>// showTripNotFoundNotice<br>// showTripAlreadyCancelledNotice<br>// showTripDepartedNotice<br>// showCancelTripAbortedNotice<br>// showCancelTripResult | 40 | 40 | 240 | 320 |
| AC-B-PaymentGateway | Class | PaymentGateway | «boundary» | - | ticketCode<br>refundAmount | // requestRefund<br>// returnRefundResult | 360 | 40 | 240 | 140 |
| AC-B-SmsGateway | Class | SmsGateway | «boundary» | - | recipientPhone<br>smsContent | // sendTripCancelSms | 680 | 40 | 240 | 120 |
| AC-C-CancelTripController | Class | CancelTripController | «control» | - | - | // startCancelTrip<br>// confirmCancel<br>// cancelCancelTripRequest<br>// cancelTripTriggers | 360 | 480 | 240 | 130 |
| AC-E-Trip | Class | Trip | «entity» | - | departureTime<br>status | // findTrip<br>// checkNotCancelled<br>// checkBeforeDeparture<br>// getCancellationSummary<br>// cancelTrip<br>// getRouteAndDepartureTime | 360 | 690 | 240 | 220 |
| AC-E-Route | Class | Route | «entity» | - | departurePoint<br>arrivalPoint | // checkRouteMatches | 40 | 690 | 240 | 120 |
| AC-E-Ticket | Class | Ticket | «entity» | - | ticketCode<br>travelerPhone<br>price<br>status<br>purchaseChannel | // getCancelImpactInfo<br>// cancelWithTrip<br>// calculateTripCancelRefundAmount<br>// determineRefundMethod<br>// recordRefund<br>// getTripCancelSmsContent | 680 | 690 | 240 | 280 |
| AC-E-PhoneReservation | Class | PhoneReservation | «entity» | - | status | // checkUnpaid<br>// cancelWithTrip | 360 | 1050 | 240 | 120 |
| AC-E-Refund | Class | Refund | «entity» | - | refundAmount<br>refundRate<br>refundMethod<br>refundResult | // createRefund | 680 | 1050 | 240 | 160 |

b) Bảng quan hệ (bảng Edge):

| ID | Lớp A | Lớp B | Loại (Association / Aggregation / Composition / Generalization / Dependency) | Multiplicity | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC013-01 | AC-B-CancelTripForm | AC-C-CancelTripController | Association | - | tạm thời | LK-02 |
| R-UC013-02 | AC-C-CancelTripController | AC-E-Trip | Association | - | tạm thời | LK-03 |
| R-UC013-03 | AC-C-CancelTripController | AC-E-Ticket | Association | - | tạm thời | LK-08 |
| R-UC013-04 | AC-C-CancelTripController | AC-B-PaymentGateway | Association | - | tạm thời | LK-10 |
| R-UC013-05 | AC-C-CancelTripController | AC-B-SmsGateway | Association | - | tạm thời | LK-12 |
| R-UC013-06 | AC-E-Trip | AC-E-Route | Association | A 0..* - B 1 | chuyến thuộc một tuyến | LK-04; R-UC002-07; GL-04 "Một lần chạy của một tuyến" |
| R-UC013-07 | AC-E-Trip | AC-E-Ticket | Association | A 1 - B 0..* | chuyến có các vé | LK-05; R-UC002-14; GL-37 |
| R-UC013-08 | AC-E-Trip | AC-E-PhoneReservation | Association | A 1 - B 0..* | chuyến có các đặt chỗ qua điện thoại | LK-06; GL-07 "giữ chỗ trên một chuyến" |
| R-UC013-09 | AC-E-Ticket | AC-E-Refund | Association | A 1 - B 0..1 | khoản hoàn của vé đã huỷ | LK-09; R-UC008-07; ASM-48 |

Link actor-boundary (LK-01, LK-11, LK-13) và link tự gọi (LK-07) không vào VOPC. Mỗi link còn lại giữa hai lớp khác nhau của F7 sinh một quan hệ (LK-02 --> R-UC013-01, LK-03 --> R-UC013-02, LK-08 --> R-UC013-03, LK-10 --> R-UC013-04, LK-12 --> R-UC013-05, LK-04 --> R-UC013-06, LK-05 --> R-UC013-07, LK-06 --> R-UC013-08, LK-09 --> R-UC013-09). Multiplicity "-" nghĩa là đặc tả chưa nêu rõ nên để trống; quan hệ giữa boundary, control và entity là quan hệ tạm thời. R-UC013-06 và R-UC013-07 trùng với R-UC002-07, R-UC002-14 của UC-002 và R-UC013-09 trùng với R-UC008-07 của UC-008; P08 sẽ gộp. Multiplicity "A 1 - B 0..*" của R-UC013-08 dựa trên GL-07 (đặt chỗ giữ trên một chuyến). Quan hệ cuối cùng chốt ở P08.

## 9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) và tác nhân |
|---|---|---|
| 1 | SD1: 1, 1.1 | ACT-03, AC-B-CancelTripForm, AC-C-CancelTripController |
| 2 | SD1: 1.1.1, 1.1.1.1, 1.1.1 (trả về), 1.1.2, 1.1.3 | AC-C-CancelTripController, AC-E-Trip, AC-E-Route |
| 2a | SD2: 1.1.1a | AC-C-CancelTripController, AC-B-CancelTripForm |
| 2b | SD2: 1.1.2a | AC-C-CancelTripController, AC-B-CancelTripForm |
| 2c | SD2: 1.1.3a | AC-C-CancelTripController, AC-B-CancelTripForm |
| 3 | SD1: 1.1.4, 1.1.4.1, 1.1.4.2, 1.1.4 (trả về), 1.1.5 | AC-C-CancelTripController, AC-E-Trip, AC-E-Ticket, AC-E-PhoneReservation, AC-B-CancelTripForm |
| 4 | SD1: 2, 2.1 | ACT-03, AC-B-CancelTripForm, AC-C-CancelTripController |
| 4a | SD3: 2a, 2a.1, 2a.1.1 | ACT-03, AC-B-CancelTripForm, AC-C-CancelTripController |
| 5 | SD1: 2.1.1, 2.1.1.1, 2.1.1.2, 2.1.1 (trả về), 2.1.2 | AC-C-CancelTripController, AC-E-Trip, AC-E-Ticket, AC-E-PhoneReservation |
| 5a | SD1: fragment opt FR1 | AC-C-CancelTripController |
| 6 | SD1: 2.1.3, 2.1.3 (trả về), 2.1.4, 2.1.4 (trả về) | AC-C-CancelTripController, AC-E-Ticket |
| 6a | SD1: fragment opt FR3 | AC-C-CancelTripController |
| 7 | SD1: 2.1.5, 2.1.5.1 | AC-C-CancelTripController, AC-B-PaymentGateway, ACT-06 |
| 8 | SD1: 2.1.5.2, 2.1.5 (trả về) | ACT-06, AC-B-PaymentGateway, AC-C-CancelTripController |
| 8a | SD4: 2.1.6a, 2.1.6a.1 | AC-C-CancelTripController, AC-E-Ticket, AC-E-Refund |
| 9 | SD1: 2.1.6, 2.1.6.1 | AC-C-CancelTripController, AC-E-Ticket, AC-E-Refund |
| 10 | SD1: 2.1.7, 2.1.7.1, 2.1.7 (trả về), 2.1.8, 2.1.8.1 | AC-C-CancelTripController, AC-E-Ticket, AC-E-Trip, AC-B-SmsGateway, ACT-07 |
| 11 | SD1: 2.1.9 | AC-C-CancelTripController, AC-B-CancelTripForm |

## 10. File .drawio

| File | Trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-013.drawio | SD1, SD2, SD3, SD4 | Bảng F5; ID cell là ID trong bảng lifeline, fragment, message |
| diagrams/P07-communication-UC-013.drawio | COMM1 | Bảng F7; ID cell là ID trong bảng Node và Edge |
| diagrams/P07-class-UC-013.drawio | VOPC1 | Bảng F8; ID cell của lớp là mã AC, của cạnh là ID quan hệ, nhãn multiplicity là cell con của cạnh |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-71 | Khi chuyến bị huỷ, các mốc kích hoạt tự động tính từ giờ xuất bến của chuyến (60 phút trước giờ xuất bến của UC-006, 15 phút trước giờ xuất bến của UC-014) do UC-013 huỷ, hay UC-006 và UC-014 tự bỏ qua chuyến đã huỷ khi tới mốc? (UC-013 huỷ mốc / UC-006, UC-014 tự bỏ qua chuyến đã huỷ) | Message 2.1.2 (cancelTripTriggers) của SD1; AC-C-CancelTripController; ASM-47; P07 của UC-012, UC-006, UC-014 | Mục 4, câu 2 và Mục 8, câu 4: mốc "60 phút trước giờ xuất bến", "15 phút trước giờ xuất bến"; Mục 6, câu 4 không nêu ảnh hưởng của việc huỷ chuyến tới các mốc này |
| Q-72 | Khi nhân viên điều hành xác nhận ở bước 4, hệ thống có kiểm tra lại điều kiện huỷ được (chuyến chưa huỷ, chưa tới giờ xuất bến) trước khi ghi nhận ở bước 5 không, hay chỉ dùng kết quả kiểm tra ở bước 2? (Kiểm tra lại ở bước 5 / Chỉ kiểm tra ở bước 2) | Bước 2, 5; message 1.1.2, 1.1.3 (SD1); ASM-49; Q-40 | P04 UC-013 bước 2: kiểm tra trước khi hiển thị; bước 5 không nêu kiểm tra lại, trong khi giữa bước 3 và bước 4 thời gian có thể trôi qua giờ xuất bến |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-47 | UC-013 có trách nhiệm huỷ các mốc kích hoạt tự động của UC-006 (EV-08) và UC-014 (EV-18) tính từ giờ xuất bến của chuyến bị huỷ, thể hiện bằng message tự gọi "// cancelTripTriggers" của control ở bước 5. Mức phân tích không chọn cơ chế lập lịch. | Quy tắc A2: use case làm mốc mất hiệu lực có trách nhiệm huỷ mốc. Chuyến đã huỷ không chạy nên danh sách hành khách (UC-014) và hạn thanh toán đặt chỗ (UC-006) không còn ý nghĩa. P04 UC-013 không nêu việc này. Chờ Q-71 | AC-C-CancelTripController (cancelTripTriggers); message 2.1.2 (SD1); bước 5 |
| ASM-48 | Mỗi vé đã huỷ của chuyến có đúng một khoản hoàn tiền (Refund) được tạo ở bước 9 (hoặc 8a), ghi mức hoàn 100%, số tiền hoàn, hình thức hoàn và kết quả hoàn với ba giá trị: đã hoàn, chưa thành công, chờ chi tiền mặt. Khác ASM-46 của UC-008, khoản hoàn vẫn được tạo khi hoàn qua cổng không thành công. | Vé đã huỷ ở bước 5 trước khi hoàn tiền nên khoản hoàn chưa thành công phải được ghi lại để nhà xe xử lý lại (ASM-31); vé mua tại quầy cần khoản hoàn chờ chi tiền mặt (ASM-28); GL-16 coi kết quả hoàn là thành phần của khoản hoàn. Chờ Q-43 | AC-E-Refund; AC-E-Ticket (recordRefund); message 2.1.6, 2.1.6.1 (SD1), 2.1.6a, 2.1.6a.1 (SD4); R-UC013-09 |
| ASM-49 | Điều kiện huỷ được (chuyến có trong lịch chạy, chưa huỷ, chưa tới giờ xuất bến) chỉ kiểm tra ở bước 2 bằng thời điểm hiện tại lúc hệ thống xử lý bước 2; bước 5 không kiểm tra lại. | P04 UC-013 chỉ đặt kiểm tra ở bước 2 và hậu điều kiện tối thiểu nói mọi luồng thất bại kết thúc trước bước 5. Chờ Q-72 | AC-E-Trip (checkNotCancelled, checkBeforeDeparture); message 1.1.2, 1.1.3 (SD1); bước 2, 5 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 (UC-013) | Bước 5, Mục 8 | Chuyến bị huỷ làm mất hiệu lực hai mốc do ACT-10 kích hoạt (UC-006 60 phút, UC-014 15 phút trước giờ xuất bến) nhưng đặc tả không nêu ai huỷ hoặc bỏ qua các mốc này (A2, ASM-47, Q-71). | Thêm vào bước 5 hoặc Mục 8 việc huỷ mốc kích hoạt tự động của chuyến, hoặc ghi rõ UC-006, UC-014 bỏ qua chuyến đã huỷ, sau khi Q-71 được trả lời. |
| P04 (UC-013) | Bước 8a, bước 9 | Luồng 8a ghi nhận khoản hoàn chưa thành công rồi "Tiếp tục bước 9", trong khi bước 9 nêu "ghi nhận khoản hoàn của từng vé đã huỷ" và chỉ mô tả hai trường hợp (đã hoàn, chờ chi tiền mặt); không rõ vé hoàn không thành công có được ghi hai lần hay không. | Sửa bước 9 thành "ghi nhận khoản hoàn của từng vé đã huỷ chưa được ghi nhận ở bước 8a" hoặc gộp 8a vào bước 9 với kết quả chưa thành công là một giá trị. |
| P04 (UC-013) | Bước 10 | Đặc tả thiếu luồng ngoại lệ cho lỗi của hệ thống ngoài khi Cổng SMS không nhận hoặc báo lỗi, nên SD1 không có nhánh xử lý (Q-56). | Thêm luồng ngoại lệ gửi tin nhắn lỗi sau khi Q-56 được trả lời. |
| P04 (UC-013) | Bước 11, Dữ liệu ra 3 | Dữ liệu ra 3 nêu các số liệu tổng hợp (số vé theo kết quả hoàn, mã vé hoàn không thành công) nhưng đặc tả không nêu lớp nào giữ; P07 để control tổng hợp tạm từ kết quả các bước trước. | Giữ nguyên nếu chấp nhận số liệu tạm; nếu cần lưu lịch sử huỷ chuyến thì bổ sung yêu cầu và use case xem lại. |
| P07 (UC-008) | AC-E-Refund, ASM-46 | Refund của UC-008 chỉ tạo khi hoàn thành công, của UC-013 tạo cả khi chưa thành công (ASM-48), nên refundResult có nhiều giá trị hơn UC-008 đã nêu. | P08 gộp Refund với refundResult gồm đã hoàn, chưa thành công, chờ chi tiền mặt và thống nhất thời điểm tạo khoản hoàn. |

## Vấn đề còn mở

- Target 14 đạt một phần: C7.3 yêu cầu cạnh không cắt qua node và không có hai node chồng nhau, nhưng trong sequence diagram message đi qua các lifeline ở giữa và fragment phủ lên lifeline theo ký pháp UML (F10). Communication diagram và VOPC thoả C7.3 về toạ độ bội số 10, khoảng cách giữa node từ 40 và cạnh không cắt qua node; nhãn link dài của communication diagram có thể chồng lên hình node kề khi mở bằng draw.io, cần chỉnh tay.
- Chọn giữa hai quy tắc (C9): A2 ghi "Không thêm chức năng mới" còn quy tắc mốc thời gian phụ thuộc dữ liệu (A2, Target 15) đòi use case làm mốc mất hiệu lực có message huỷ mốc. Đã chọn thêm message tự gọi cancelTripTriggers (ASM-47, Q-71) và đề xuất sửa P04 thay vì bỏ qua mốc.
- Chọn giữa hai quy tắc (C9): F3.2 chỉ cho các giá trị Kết luận đã liệt kê. Dòng "Lịch chạy" dùng "Loại - không tham gia hành vi của use case này (khái niệm của UC-012)" và dòng "Chỗ, lần đặt trực tuyến đang giữ chỗ" dùng "Loại - thuộc phân tích của UC-002" dù UC-002 không là use case được include hoặc extend; đây là giá trị gần nhất trong danh sách.
- Chọn giữa hai quy tắc (C9): F5 nêu ngưỡng khoảng 30 message mỗi trang; SD1 có 35 dòng gồm 7 message trả về, tức 28 message không kể trả về, nên đếm theo message không kể trả về thì đạt. Không tách luồng chính sang trang thứ hai để communication diagram có cùng phạm vi với SD1.
- Chọn giữa hai quy tắc (C9): F5 yêu cầu message đầu tiên ở y=120 và cách nhau 40 (F10), nhưng nhãn fragment và đường ngăn toán hạng cần chỗ; trang có fragment mở ở đầu (SD2, SD3, SD4) bắt đầu message đầu tiên ở y=160, và giữa các message quanh fragment có khoảng cách lớn hơn 40.
- Chọn giữa hai quy tắc (C9): F7 yêu cầu communication diagram tương đương với phần sequence diagram nó thể hiện; luồng 2a, 2b, 2c, 4a, 8a vẽ ở SD2, SD3, SD4 nên không có trong communication diagram, chỉ có opt 5a, 6a của SD1.
- Target 9 đạt một phần: Refund chỉ có trách nhiệm createRefund và Route chỉ có checkRouteMatches; đặc tả UC-013 không nêu hành vi nào khác trên khoản hoàn hay tuyến (số tiền hoàn do Ticket tính vì Refund chưa tồn tại ở bước 6, ASM-48). P08 sẽ gộp thêm trách nhiệm từ các use case khác.
- Chạy khi chưa có P07 của UC-004, UC-005, UC-006, UC-012, UC-014: AC-E-PhoneReservation do UC-013 đặt mã và các thuộc tính, quan hệ của nó (R-UC013-08) suy từ GL-07; UC-004 và UC-006 phải tái dùng đúng mã này. Mốc của UC-006, UC-014 do UC-012 (xếp chuyến) hẹn ban đầu; message huỷ mốc của UC-013 phải khớp với cơ chế hẹn mốc ở P07 của UC-012.
- Trách nhiệm sendTripCancelSms của SmsGateway có cùng ý nghĩa gửi nội dung tới số điện thoại với sendTicketSms của UC-002 (khác nội dung); P08 quyết định gộp thành một trách nhiệm hay giữ hai tên. Tương tự cancelWithTrip của Ticket và PhoneReservation dùng cùng tên ở hai lớp khác nhau, và determineRefundMethod, getRouteAndDepartureTime dùng lại đúng tên của UC-008, UC-002.
- Chạy với giả định: điều kiện huỷ được (Q-40, Q-72), nội dung tin nhắn (Q-41), số điện thoại người đi của vé bán tại quầy (Q-42), hoàn không thành công (Q-43) và lần đặt đang giữ chỗ (Q-44) vẫn là câu hỏi mở của P04; P07 dùng ASM-24 đến ASM-31 của P04. Bước 7, 8 phụ thuộc API hoàn tiền chưa có tài liệu (Q-24, NFR-07), nên message requestRefund và returnRefundResult chỉ ở mức phân tích. Lớp Seat không tham gia vì UC-013 không đọc hay ghi chỗ (ASM-26 nêu trả chỗ của lần đặt đang giữ, chờ Q-44 và UC-002).
- Khoản hoàn của vé mua tại quầy chỉ được ghi nhận "chờ chi tiền mặt"; việc chi tiền mặt chưa có use case (CAND-43, chờ Q-14).
