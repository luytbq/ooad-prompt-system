# P07 - Phân tích use case UC-017 Huỷ chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-017-cancel-trip.md (phiên bản 1.0, toàn bộ, Q-50, ASM-33); P04-uc-specs/_BR-register.md (BR-01 đến BR-26); P01-actors.md (phiên bản 1.0, Mục 2); P02-usecases.md (phiên bản 1.1, dòng UC-017 ở Mục 4, các dòng UC có tác nhân thời gian UC-007, UC-025); P03-usecase-model.md (phiên bản 1.0, các dòng có UC-017 ở Mục 1, Mục 2); P05-glossary.md (phiên bản 1.0, các thuật ngữ đặc tả dùng); P06-supplementary-spec.md (phiên bản 1.0, các BR, NFR có UC-017); P07-uc-analysis/UC-009-book-ticket-online-analysis.md (phiên bản 1.0; F1, F3.4, F8 b), Câu hỏi mở, Giả định, Vấn đề còn mở). Không có include hoặc extend nên không cần đặc tả P04 của use case khác. Q, ASM lớn nhất đã có trước lần chạy: Q-57, ASM-41 (P07 UC-009); cấp tiếp từ Q-58, ASM-42 |
| Phạm vi | UC-017 |
| Mã Q, ASM cuối đã cấp | Q-58, ASM-42 |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-017 Huỷ chuyến (Cancel Trip) |
| Tác nhân chính (ACT, loại) | ACT-03 Nhân viên điều hành (Người) |
| Tác nhân phụ (ACT, loại) | ACT-06 Cổng thanh toán (Hệ thống ngoài)<br>ACT-07 Cổng SMS (Hệ thống ngoài) |
| Include (UC) | Không có (P03 Mục 1: UC-017 chỉ nối với ACT-03, ACT-06, ACT-07 bằng association RL-28, RL-29, RL-30) |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có (UC-017 không là use case extend) |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2: UC-017 không có điểm mở rộng) |
| Use case do tác nhân thời gian kích hoạt trên đối tượng mà UC-017 đổi (A2) | ACT-09 Bộ định thời kích hoạt UC-007 Huỷ vé đặt chỗ quá hạn (60 phút trước giờ xuất bến) và UC-025 Gửi danh sách hành khách cho phụ xe (15 phút trước giờ xuất bến); đối tượng mốc là giờ xuất bến của chuyến (Trip). UC-017 làm chuyến mất hiệu lực nên có trách nhiệm huỷ hai mốc (ASM-28) |
| File P07 đã có được dùng làm sổ đăng ký AC | P07-uc-analysis/UC-009-book-ticket-online-analysis.md. Sổ có 10 mã: AC-B-BookTicketOnlineForm, AC-B-SmsGateway, AC-C-BookTicketOnlineController, AC-C-SearchTripsController (tạm, chờ P07 của UC-008), AC-C-PayTicketOnlineController (tạm, chờ P07 của UC-010), AC-E-Trip, AC-E-Seat, AC-E-Fare, AC-E-Booking, AC-E-Ticket |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Nhân viên điều hành | Yêu cầu huỷ chuyến. | Không đổi | REQ-55 |
| 2 | Hệ thống | Hiển thị các chuyến trong lịch chạy (xem Dữ liệu ra 1). | Hệ thống lấy các chuyến trong lịch chạy, mỗi chuyến kèm tuyến, giờ xuất bến, xe, tài xế và trạng thái chuyến (Chưa huỷ hoặc Đã huỷ), rồi hiển thị cho nhân viên điều hành. | GL-03, GL-13; REQ-46, REQ-47 |
| 3 | Nhân viên điều hành | Chọn chuyến cần huỷ và lý do huỷ chuyến (xem Dữ liệu vào 1, ASM-25). | Không đổi | ASM-25; REQ-55 |
| 4 | Hệ thống | Kiểm tra chuyến đã chọn chưa bị huỷ (BR-09) và chưa đến giờ xuất bến (BR-10). | Hệ thống đọc trạng thái của chuyến đã chọn và kiểm tra chuyến chưa ở trạng thái Đã huỷ (BR-09). Sau đó hệ thống so giờ xuất bến của chuyến với thời điểm hiện tại để kiểm tra chưa đến giờ xuất bến (BR-10), theo thứ tự này (ASM-26). | BR-09, BR-10, ASM-26; GL-04, GL-07 |
| 4a | Hệ thống | Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã bị huỷ (BR-09). | Hệ thống không thay đổi chuyến và vé, hiển thị thông báo chuyến đã bị huỷ để nhân viên điều hành chọn lại ở bước 3. | BR-09; GL-04 |
| 4b | Hệ thống | Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã đến giờ xuất bến (BR-10). | Hệ thống không thay đổi chuyến và vé, hiển thị thông báo chuyến đã đến giờ xuất bến để nhân viên điều hành chọn lại ở bước 3. | BR-10; GL-07 |
| 5 | Hệ thống | Lưu chuyến ở trạng thái "Đã huỷ" kèm lý do huỷ chuyến. | Hệ thống đổi trạng thái của chuyến đã chọn sang Đã huỷ và ghi lý do huỷ chuyến (Xe hỏng hoặc Thời tiết) cùng chuyến. Hệ thống lấy tuyến và giờ xuất bến của chuyến để dùng ở các bước sau. | ASM-25; GL-04; REQ-55 |
| 6 | Hệ thống | Huỷ mốc 60 phút trước giờ xuất bến của UC-007 Huỷ vé đặt chỗ quá hạn và mốc 15 phút trước giờ xuất bến của UC-025 Gửi danh sách hành khách cho phụ xe, cho chuyến đã huỷ (ASM-28). | Chuyến là đối tượng mốc của UC-007 và UC-025 nên hệ thống huỷ hai mốc này cho chuyến vừa chuyển sang Đã huỷ, để hai use case không kích hoạt cho chuyến đó. Mức phân tích không chọn cơ chế lập lịch. | ASM-28, Q-47; BR-12, BR-26; REQ-31, REQ-32, REQ-69, REQ-70 |
| 7 | Hệ thống | Chuyển các vé đang có hiệu lực của chuyến sang trạng thái "Đã huỷ" và ghi nhận các vé đã thanh toán chưa được hoàn tiền (ASM-29). | Hệ thống tìm các vé đang có hiệu lực của chuyến (chưa huỷ, chưa trả, chưa đổi) và chuyển từng vé sang Đã huỷ. Vé đã thanh toán được đặt trạng thái hoàn tiền Chưa hoàn; vé đặt qua điện thoại chưa thanh toán chỉ chuyển sang Đã huỷ vì chưa thu tiền. | ASM-29; GL-23, GL-24, GL-25; REQ-57, REQ-66 |
| 7a | - | - | Không đổi (không có hành động). Chuyến không có vé nào đang có hiệu lực thì bỏ qua bước 8-13 và tiếp tục bước 14. | GL-25 |
| 8 | Hệ thống | Gửi SMS thông báo huỷ chuyến tới một số điện thoại người đi qua Cổng SMS (BR-11, ASM-30, xem Dữ liệu ra 2). | Hệ thống gom mã vé của các vé đã huỷ theo số điện thoại người đi, mỗi số khác nhau một nhóm (BR-04). Với mỗi số, hệ thống soạn nội dung nêu tuyến, giờ xuất bến của chuyến và mã các vé của số đó rồi chuyển cho Cổng SMS. | BR-11, BR-04, ASM-30; GL-15, GL-17; REQ-56 |
| 9 | Cổng SMS | Trả kết quả gửi SMS. | Không đổi | REQ-21 |
| 9a | Hệ thống | Ghi nhận số điện thoại và mã các vé chưa được báo qua SMS (ASM-31). | Hệ thống đánh dấu trên các vé của số điện thoại đó rằng chưa được báo huỷ chuyến qua SMS (ASM-42). Hệ thống tiếp tục với số điện thoại tiếp theo và không đảo ngược việc huỷ chuyến. | ASM-31, ASM-42, Q-49, Q-58; REQ-56 |
| 10 | Hệ thống | Lặp lại bước 8-9 cho đến khi đã gửi SMS cho mọi số điện thoại người đi của chuyến. | Hệ thống lặp theo danh sách số điện thoại đã gom ở bước 8 cho đến khi mọi số đã được xử lý. | ASM-30 |
| 10a | - | - | Không đổi (không có hành động). Đã gửi SMS cho mọi số điện thoại và chuyến không có vé mua trực tuyến chưa hoàn thì bước 11-13 không chạy. | BR-08 |
| 11 | Hệ thống | Yêu cầu Cổng thanh toán hoàn tiền cho một vé mua trực tuyến chưa hoàn, bằng 100% giá vé (BR-07, BR-08, ASM-32, xem Dữ liệu ra 3). | Hệ thống chọn trong số vé đã huỷ các vé mua trực tuyến đã thanh toán còn trạng thái hoàn tiền Chưa hoàn. Với mỗi vé, hệ thống tính số tiền hoàn bằng 100% giá vé đã ghi khi bán (nên không vượt số đã thu cho vé) rồi yêu cầu Cổng thanh toán hoàn số đó vào giao dịch thanh toán đã thu tiền vé. | BR-07, BR-08, ASM-32; GL-05, GL-06, GL-10, GL-18; NFR-05, NFR-06, NFR-11; REQ-57, REQ-58, REQ-16 |
| 12 | Cổng thanh toán | Trả kết quả hoàn tiền. | Không đổi | REQ-16 |
| 12a | Hệ thống | Ghi nhận vé chưa được hoàn tiền và giữ trạng thái hoàn tiền "Chưa hoàn" của vé (ASM-33). | Hệ thống giữ trạng thái hoàn tiền Chưa hoàn của vé và đánh dấu vé đó hoàn tiền không thành công (ASM-42). Hệ thống tiếp tục với vé tiếp theo và không đảo ngược việc huỷ chuyến. | ASM-33, ASM-42, Q-50, Q-58; REQ-57 |
| 13 | Hệ thống | Lặp lại bước 11-12 cho đến khi đã yêu cầu hoàn tiền cho mọi vé mua trực tuyến của chuyến. | Hệ thống lặp theo danh sách vé chọn ở bước 11 cho đến khi mọi vé đã được yêu cầu hoàn tiền. Với mỗi kết quả hoàn tiền thành công, hệ thống chuyển trạng thái hoàn tiền của vé sang Đã hoàn và ghi khoản hoàn vào giao dịch thanh toán của vé (hậu điều kiện thành công). | ASM-29, ASM-32; GL-06, GL-10; NFR-05 |
| 14 | Hệ thống | Hiển thị kết quả huỷ chuyến cho nhân viên điều hành (xem Dữ liệu ra 4). | Hệ thống tổng hợp từ các vé đã huỷ: số vé đã huỷ, số điện thoại đã báo và chưa báo được, số vé mua trực tuyến đã hoàn cùng tổng tiền và vé chưa hoàn được, số vé mua tại quầy chờ hoàn tiền mặt. Hệ thống hiển thị cùng tuyến và giờ xuất bến của chuyến đã huỷ. | BR-08; ASM-31, ASM-33; REQ-57 |
| *a | Hệ thống | Bỏ yêu cầu huỷ chuyến, không thay đổi dữ liệu và thông báo đã bỏ yêu cầu. | Hệ thống không ghi gì vào chuyến và vé, chỉ hiển thị thông báo đã bỏ yêu cầu huỷ chuyến. Luồng áp dụng ở mọi bước trước bước 5. | ASM-27 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-03 Nhân viên điều hành | Người | CancelTripForm | Giao diện người dùng | Mới (AC-B-CancelTripForm, UC-017) | Một boundary cho cặp ACT-03 và UC-017: nhận yêu cầu huỷ chuyến, chuyến và lý do huỷ chuyến được chọn, yêu cầu bỏ; hiển thị các chuyến trong lịch chạy, thông báo từ chối, thông báo đã bỏ và kết quả huỷ chuyến. Boundary giao diện người dùng đặt tên theo tương tác của use case nên không dùng chung với use case khác |
| ACT-07 Cổng SMS | Hệ thống ngoài | SmsGateway | Giao diện hệ thống | Tái dùng (AC-B-SmsGateway, UC-009) | Cổng SMS chỉ nhận lời gọi gửi SMS và trả kết quả (NFR-12), cùng khái niệm với UC-009 nên dùng lại đúng mã và tên; bổ sung trách nhiệm gửi SMS thông báo huỷ chuyến |
| ACT-06 Cổng thanh toán | Hệ thống ngoài | PaymentGateway | Giao diện hệ thống | Mới - chủ sở hữu UC-010 (AC-B-PaymentGateway, UC-017) | Cổng thanh toán chỉ nhận yêu cầu hoàn tiền và trả kết quả (NFR-11). UC-009 chuyển boundary này cho P07 của UC-010 (use case được include), nhưng UC-017 là use case đầu tiên cần boundary này và UC-010 chưa có P07 nên cấp mã tại đây theo A1; P07 của UC-010 phải dùng lại. Đặt tên theo hệ thống, không hậu tố vì HAU_TO_TEN_LOP là Mặc định; không trùng tên entity nào |

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Nhân viên điều hành | Tác nhân chính; bước 1, 3; tiền điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | ACT-03, được phục vụ qua CancelTripForm |
| 2 | Cổng SMS | Tác nhân phụ; bước 8, 9 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-07, được phục vụ qua SmsGateway |
| 3 | Cổng thanh toán | Tác nhân phụ; bước 11, 12 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-06, được phục vụ qua PaymentGateway |
| 4 | Hệ thống | Mọi bước | Loại - mơ hồ | Chủ ngữ chung của các bước, không là khái niệm nghiệp vụ |
| 5 | Phiên làm việc, xác thực | Tiền điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | Thuộc UC-003 Đăng nhập; UC-017 chỉ đòi hỏi phiên đã có |
| 6 | Yêu cầu huỷ chuyến | Bước 1; luồng *a | Loại - thao tác hoặc sự kiện | Thao tác của tác nhân, không lưu |
| 7 | Chuyến, chuyến xe | Bước 2-5; Dữ liệu vào 1; Dữ liệu ra 1, 4; BR-09, BR-10 | Entity (AC-E-Trip) | GL-03: được lưu qua nhiều use case, có trạng thái Chưa huỷ, Đã huỷ và hành vi kiểm tra, huỷ |
| 8 | Chuyến đã huỷ, chuyến bị huỷ, trạng thái "Đã huỷ" | Bước 4a, 5; BR-09; hậu điều kiện | Loại - trùng hoặc đồng nghĩa với Trip | GL-04 là chuyến xe ở trạng thái Đã huỷ, không phải khái niệm riêng |
| 9 | Trạng thái chuyến | Bước 4; Dữ liệu ra 1 dòng 5; BR-09 | Loại - thuộc tính của Trip | Thuộc tính status của Trip |
| 10 | Lịch chạy | Bước 2 | Loại - khái niệm do UC-016 tạo, use case này chỉ đọc qua entity Trip | GL-13 là tập các chuyến của một tuần do UC-016 lập; UC-017 chỉ đọc danh sách chuyến và không đọc hay ghi gì của bản thân lịch (UC-016 không được include hay mở rộng bởi UC-017) |
| 11 | Tuyến | Dữ liệu ra 1 dòng 1; Dữ liệu ra 2 dòng 2; Dữ liệu ra 4 dòng 1 | Loại - thuộc tính của Trip | GL-22, tuyến của chuyến (route); UC-017 không đọc hay ghi danh mục tuyến |
| 12 | Giờ xuất bến | Bước 4, 6; BR-10; Dữ liệu ra 1 dòng 2 | Loại - thuộc tính của Trip | GL-07 (departureTime), là căn cứ của BR-10 và của hai mốc ở bước 6 |
| 13 | Xe | Dữ liệu ra 1 dòng 3 | Loại - khái niệm do UC-021 tạo, use case này chỉ đọc qua entity Trip | UC-017 chỉ hiển thị xe được xếp vào chuyến; Trip giữ tham chiếu vehicle (UC-021 không được include hay mở rộng bởi UC-017) |
| 14 | Tài xế | Dữ liệu ra 1 dòng 4 | Loại - khái niệm do UC-022 tạo, use case này chỉ đọc qua entity Trip | UC-017 chỉ hiển thị tài xế được xếp vào chuyến; Trip giữ tham chiếu driver (UC-022 không được include hay mở rộng bởi UC-017) |
| 15 | Lý do huỷ chuyến (Xe hỏng, Thời tiết) | Bước 3, 5; Dữ liệu vào 1 dòng 2; ASM-25 | Loại - thuộc tính của Trip | cancelReason, dữ liệu của lần huỷ lưu cùng chuyến; hai giá trị là tham số của ASM-25 |
| 16 | Mốc 60 phút và mốc 15 phút trước giờ xuất bến | Bước 6; ASM-28; BR-12, BR-26 | Loại - thao tác hoặc sự kiện | Sự kiện hẹn giờ của UC-007 và UC-025; huỷ mốc là message tự gọi của control (A2); giá trị 60 và 15 là tham số của BR-12, BR-26 |
| 17 | UC-007 Huỷ vé đặt chỗ quá hạn, UC-025 Gửi danh sách hành khách cho phụ xe | Bước 6 | Loại - là tác nhân hoặc ngoài phạm vi | Use case khác, không include hay extend UC-017; chỉ mốc của chúng bị huỷ ở bước 6 |
| 18 | Vé | Bước 7, 8, 11; BR-04; BR-07 | Entity (AC-E-Ticket) | GL-23: lưu qua nhiều use case, đổi trạng thái vé, trạng thái hoàn tiền; tái dùng mã từ UC-009 |
| 19 | Vé đang có hiệu lực | Bước 7, 7a; ASM-29 | Loại - giá trị suy ra từ Ticket | GL-25 là vé chưa huỷ, chưa trả, chưa đổi; suy ra từ status, không lưu riêng |
| 20 | Vé đã huỷ | Bước 7; hậu điều kiện | Loại - trùng hoặc đồng nghĩa với Ticket | GL-24 là Ticket ở trạng thái Đã huỷ |
| 21 | Vé đã thanh toán, vé đặt qua điện thoại chưa thanh toán | Bước 7; mục 8 | Loại - thuộc tính của Ticket | paymentStatus (Đã thanh toán, Chưa thanh toán); vé chưa thanh toán chưa có khoản tiền đã thu nên không hoàn (GL-26) |
| 22 | Vé mua trực tuyến, vé mua tại quầy | Bước 11; BR-08; Dữ liệu ra 4 dòng 5, 7 | Loại - giá trị suy ra từ Ticket | GL-28 và GL-27 là phân loại theo purchaseChannel (GL-11), tính khi cần |
| 23 | Kênh mua vé | BR-08 | Loại - thuộc tính của Ticket | purchaseChannel (GL-11); UC-017 dùng thêm giá trị Tại quầy |
| 24 | Trạng thái hoàn tiền (Chưa hoàn, Đã hoàn) | Bước 7, 12a; hậu điều kiện; ASM-29 | Loại - thuộc tính của Ticket | refundStatus (GL-10, GL-23) |
| 25 | Mã vé | Bước 8; Dữ liệu ra 2 dòng 3; Dữ liệu ra 3 dòng 2; BR-04 | Loại - thuộc tính của Ticket | GL-15, ticketCode |
| 26 | Số điện thoại người đi | Bước 8; Dữ liệu ra 2 dòng 1 | Loại - thuộc tính của Ticket | GL-17, travelerPhone; không có định danh và hành vi riêng |
| 27 | Hành khách đã có vé, hành khách của chuyến, người đi | BR-11; ASM-30 | Loại - trùng hoặc đồng nghĩa với Người đi (GL-17) | ASM-30 hiểu là người đi của các vé đang có hiệu lực; thông tin người đi là thuộc tính của Ticket, không phải tác nhân ACT-01 |
| 28 | Giá vé | Bước 11; BR-07; Dữ liệu ra 3; mục 8 | Loại - thuộc tính của Ticket | GL-05, fare: giá của từng vé đã ghi khi bán; UC-017 không đọc entity Fare vì giá hiện hành không ảnh hưởng số tiền hoàn |
| 29 | 100% | BR-07; bước 11 | Loại - tham số của quy tắc BR-07 | Hằng số của quy tắc tính tiền hoàn |
| 30 | Số tiền hoàn | Bước 11; Dữ liệu ra 3 dòng 3; BR-07 | Loại - giá trị suy ra từ Ticket | GL-18: bằng 100% fare (BR-07), tính khi cần; khoản đã hoàn của giao dịch lưu ở refundedAmount |
| 31 | Hoàn tiền, yêu cầu hoàn tiền | Bước 11, 13; BR-07, BR-08 | Loại - thao tác hoặc sự kiện | GL-10 là việc trả tiền; kết quả lưu qua refundStatus của Ticket và refundedAmount của giao dịch |
| 32 | Giao dịch thanh toán | Dữ liệu ra 3 dòng 1; mục 8; bước 11 | Entity (AC-E-PaymentTransaction) | GL-06: được UC-010 tạo khi thu tiền và UC-017 ghi khoản hoàn gắn vào; một giao dịch có thể thu nhiều vé (ASM-32) nên có vòng đời và định danh riêng do Cổng thanh toán cấp |
| 33 | Mã giao dịch | Dữ liệu ra 3 dòng 1 | Loại - thuộc tính của PaymentTransaction | transactionCode, do Cổng thanh toán cấp |
| 34 | Số đã thu, số đã hoàn của giao dịch | Dữ liệu ra 3; ASM-32; NFR-06 | Loại - thuộc tính của PaymentTransaction | collectedAmount, refundedAmount, để cộng các khoản hoàn gắn vào một giao dịch |
| 35 | SMS, nội dung thông báo, thông báo huỷ chuyến | Bước 8; Dữ liệu ra 2 dòng 2; BR-11 | Loại - dữ liệu trao đổi qua boundary SmsGateway | Nội dung tin nhắn nêu tuyến, giờ xuất bến, mã vé; không lưu (ASM-30) |
| 36 | Kết quả gửi SMS, kết quả hoàn tiền | Bước 9, 12 | Loại - dữ liệu trao đổi qua boundary SmsGateway hoặc PaymentGateway | Kết quả của lời gọi hệ thống ngoài, chỉ dùng để rẽ luồng 9a, 12a |
| 37 | Thông báo từ chối, thông báo đã bỏ yêu cầu | Bước 4a, 4b; luồng *a | Loại - dữ liệu trao đổi qua boundary CancelTripForm | Nội dung hiển thị, không lưu |
| 38 | Kết quả huỷ chuyến | Bước 14; Dữ liệu ra 4 | Loại - dữ liệu trao đổi qua boundary CancelTripForm | Tập các giá trị suy ra từ Ticket và Trip để hiển thị, không lưu |
| 39 | Số vé đã huỷ, số điện thoại đã báo, số điện thoại chưa báo được, số vé và tổng tiền đã hoàn, vé chưa hoàn được, số vé chờ hoàn tiền mặt | Dữ liệu ra 4 dòng 2-7 | Loại - giá trị suy ra từ Ticket | Đếm và cộng khi cần từ status, refundStatus, cancelNoticeStatus, refundAttemptStatus, purchaseChannel của các vé; không lưu |
| 40 | Danh sách (chuyến, số điện thoại, mã vé, vé) | Dữ liệu ra 1, 2, 3, 4 | Loại - cấu trúc cài đặt | Tập hợp hiển thị hoặc kết quả truy vấn, không có định danh nghiệp vụ riêng |

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| AC-C-CancelTripController | UC-017 | Mới | Điều phối trình tự huỷ chuyến: lấy các chuyến, kiểm tra, huỷ chuyến, huỷ mốc, huỷ vé, báo SMS, hoàn tiền, hiển thị kết quả. Không giữ dữ liệu nghiệp vụ lâu dài; quy tắc kiểm tra, đổi trạng thái, tính tiền hoàn nằm ở entity |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-CancelTripForm | boundary | CancelTripForm | // requestCancelTrip: nhận yêu cầu huỷ chuyến của nhân viên điều hành<br>// showScheduledTrips: hiển thị các chuyến trong lịch chạy kèm tuyến, giờ xuất bến, xe, tài xế, trạng thái chuyến<br>// selectTripAndReason: nhận chuyến cần huỷ và lý do huỷ chuyến<br>// notifyTripAlreadyCancelled: thông báo chuyến đã bị huỷ (BR-09)<br>// notifyTripDeparted: thông báo chuyến đã đến giờ xuất bến (BR-10)<br>// abortCancelTrip: nhận yêu cầu bỏ huỷ chuyến của nhân viên điều hành<br>// notifyCancelTripAborted: thông báo đã bỏ yêu cầu huỷ chuyến<br>// showCancellationResult: hiển thị kết quả huỷ chuyến | scheduledTrips (danh sách tuyến, giờ xuất bến, xe, tài xế, trạng thái chuyến), selectedTrip (Chuyến xe), cancelReason (Trạng thái: Xe hỏng, Thời tiết), cancellationResult (kết quả huỷ chuyến theo Dữ liệu ra 4) | 1, 2, 3, 4a, 4b, 14, *a | Giao diện người dùng | Mới | - |
| AC-B-SmsGateway | boundary | SmsGateway | // sendTripCancellationBySms: chuyển yêu cầu gửi SMS thông báo huỷ chuyến (số điện thoại, tuyến, giờ xuất bến, mã vé) cho Cổng SMS và nhận kết quả của lời gọi (NFR-12, ASM-30) | recipientPhone (Văn bản), ticketCodes (Văn bản), noticeContent (Văn bản) (mới ở UC này) | 8, 9 | Giao diện hệ thống | Tái dùng từ UC-009, bổ sung trách nhiệm | - |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestTicketRefund: chuyển yêu cầu hoàn tiền một vé (giao dịch thanh toán, mã vé, số tiền hoàn) cho Cổng thanh toán và nhận kết quả hoàn tiền (NFR-11, ASM-32) | transactionCode (Văn bản), ticketCode (Văn bản), refundAmount (Số tiền), refundResult (Trạng thái: Thành công, Không thành công) | 11, 12 | Giao diện hệ thống | Mới - chủ sở hữu UC-010 | - |
| AC-C-CancelTripController | control | CancelTripController | // startCancelTrip: điều phối bắt đầu huỷ chuyến, lấy các chuyến trong lịch chạy để hiển thị<br>// processTripCancellation: điều phối kiểm tra chuyến, huỷ chuyến, huỷ vé, báo SMS, hoàn tiền và hiển thị kết quả<br>// requestAbortCancelTrip: điều phối bỏ yêu cầu huỷ chuyến, không thay đổi dữ liệu<br>// cancelOverdueReservationMark: huỷ mốc 60 phút trước giờ xuất bến của UC-007 cho chuyến đã huỷ (ASM-28)<br>// cancelPassengerListMark: huỷ mốc 15 phút trước giờ xuất bến của UC-025 cho chuyến đã huỷ (ASM-28) | - | 1, 2, 3, 4, 4a, 4b, 5, 6, 7, 7a, 8, 9a, 10, 11, 12a, 13, 14, *a | - | Mới | - |
| AC-E-Trip | entity | Trip | // listTripsInSchedule: cung cấp các chuyến trong lịch chạy kèm tuyến, giờ xuất bến, xe, tài xế, trạng thái<br>// checkNotCancelled: kiểm tra chuyến chưa ở trạng thái Đã huỷ (BR-09)<br>// checkDepartureNotReached: kiểm tra giờ xuất bến chưa tới (BR-10), cùng ý nghĩa với trách nhiệm cùng tên ở UC-009 (BR-05)<br>// cancelTrip: chuyển chuyến sang Đã huỷ kèm lý do huỷ chuyến và cung cấp tuyến, giờ xuất bến của chuyến đã huỷ | departureTime (Ngày, Giờ), route (Tuyến xe), status (Trạng thái: Chưa huỷ, Đã huỷ) (mới ở UC này), cancelReason (Trạng thái: Xe hỏng, Thời tiết) (mới ở UC này), vehicle (Xe) (mới ở UC này), driver (Tài xế) (mới ở UC này) | 2, 4, 5 | - | Tái dùng từ UC-009, bổ sung trách nhiệm | GL-03, GL-04, GL-07 |
| AC-E-Ticket | entity | Ticket | // cancelTicketsOfTrip: chuyển mọi vé đang có hiệu lực của chuyến sang Đã huỷ, đặt trạng thái hoàn tiền Chưa hoàn cho vé đã thanh toán (ASM-29) và cung cấp các vé đã huỷ<br>// groupTicketCodesByTravelerPhone: gom mã vé của các vé đã huỷ theo số điện thoại người đi để mỗi số nhận một SMS (BR-04, ASM-30)<br>// recordCancelNoticeNotSent: ghi nhận các vé của một số điện thoại chưa được báo huỷ chuyến qua SMS (ASM-31, ASM-42)<br>// selectOnlineTicketsToRefund: chọn các vé mua trực tuyến đã thanh toán trong số vé đã huỷ còn ở trạng thái hoàn tiền Chưa hoàn (BR-08)<br>// calculateRefundAmount: tính số tiền hoàn bằng 100% giá vé đã ghi của vé (BR-07)<br>// markRefunded: chuyển trạng thái hoàn tiền của vé sang Đã hoàn khi Cổng thanh toán xác nhận đã hoàn (ASM-29)<br>// recordRefundNotCompleted: giữ trạng thái hoàn tiền Chưa hoàn và ghi nhận vé hoàn tiền không thành công (ASM-33, ASM-42)<br>// summarizeTripCancellation: tổng hợp số vé đã huỷ, số điện thoại đã báo và chưa báo được, vé mua trực tuyến đã hoàn và chưa hoàn được, số vé mua tại quầy chờ hoàn tiền mặt (BR-08) | ticketCode (Văn bản), travelerPhone (Văn bản), fare (Số tiền), purchaseChannel (Trạng thái: Trực tuyến, Tại quầy; giá trị Tại quầy mới ở UC này), status (Trạng thái; giá trị Đã huỷ mới ở UC này), paymentStatus (Trạng thái: Đã thanh toán, Chưa thanh toán) (mới ở UC này), refundStatus (Trạng thái: Chưa hoàn, Đã hoàn) (mới ở UC này), cancelNoticeStatus (Trạng thái: Chưa báo được) (mới ở UC này), refundAttemptStatus (Trạng thái: Hoàn không thành công) (mới ở UC này) | 7, 8, 9a, 11, 12a, 13, 14 | - | Tái dùng từ UC-009, bổ sung trách nhiệm | GL-23, GL-24, GL-25, GL-10, GL-11 |
| AC-E-PaymentTransaction | entity | PaymentTransaction | // recordRefund: ghi nhận khoản hoàn của một vé vào giao dịch thanh toán đã thu tiền vé, cộng vào số đã hoàn của giao dịch và không để số đã hoàn vượt số đã thu (ASM-32, NFR-06) | transactionCode (Văn bản), collectedAmount (Số tiền), refundedAmount (Số tiền) | 13 | - | Mới - chủ sở hữu UC-010 | GL-06 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestCancelTrip | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 1 | // startCancelTrip | AC-C-CancelTripController | Controller | - |
| 2 | // listTripsInSchedule | AC-E-Trip | Information Expert | Trip nắm tuyến, giờ xuất bến, xe, tài xế, trạng thái. Giao cho control sẽ buộc control giữ dữ liệu chuyến, làm giảm cohesion |
| 2 | // showScheduledTrips | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 3 | // selectTripAndReason | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 3 | // processTripCancellation | AC-C-CancelTripController | Controller | - |
| 4 | // checkNotCancelled | AC-E-Trip | Information Expert | - |
| 4 | // checkDepartureNotReached | AC-E-Trip | Information Expert | - |
| 4a | // notifyTripAlreadyCancelled | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 4b | // notifyTripDeparted | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| 5 | // cancelTrip | AC-E-Trip | Information Expert | - |
| 6 | // cancelOverdueReservationMark | AC-C-CancelTripController | Giao cho control | Dữ liệu nằm ở nhiều lớp: giờ xuất bến là dữ liệu của Trip, còn mốc thuộc UC-007. Giao cho Trip làm Trip phụ thuộc bộ lập lịch mà mức phân tích chưa chọn; giao cho control giữ coupling thấp hơn (A2) |
| 6 | // cancelPassengerListMark | AC-C-CancelTripController | Giao cho control | Như dòng trên, với mốc của UC-025 |
| 7 | // cancelTicketsOfTrip | AC-E-Ticket | Information Expert | Dữ liệu nằm ở nhiều lớp: chuyến giữ giờ và trạng thái, vé giữ trạng thái vé và trạng thái hoàn tiền. Chọn Ticket vì việc đổi trạng thái là dữ liệu của vé; để Trip gọi Ticket thì thêm coupling Trip-Ticket không cần |
| 7a | (fragment F3, toán hạng 1; không có hành động) | AC-C-CancelTripController | Controller | Control rẽ luồng theo danh sách vé đã huỷ trả về ở bước 7 |
| 8 | // groupTicketCodesByTravelerPhone | AC-E-Ticket | Information Expert | Số điện thoại và mã vé đều là dữ liệu của vé; giao cho control sẽ thành quy tắc gom thuộc dữ liệu của entity |
| 8 | // sendTripCancellationBySms | AC-B-SmsGateway | Giao tiếp tác nhân | - |
| 9 | // sendTripCancellationBySms (nhận kết quả từ Cổng SMS) | AC-B-SmsGateway | Giao tiếp tác nhân | - |
| 9a | // recordCancelNoticeNotSent | AC-E-Ticket | Information Expert | Nơi ghi nhận chưa rõ (Q-58); chọn dấu trên vé theo ASM-42, thay cho bản ghi riêng, để không thêm khái niệm ngoài P05 |
| 10 | // processTripCancellation (lặp theo danh sách số điện thoại, fragment F4) | AC-C-CancelTripController | Controller | - |
| 10a | (fragment F6, vòng lặp không chạy; không có hành động) | AC-C-CancelTripController | Controller | Control rẽ luồng theo danh sách vé trực tuyến chưa hoàn trả về ở bước 11 |
| 11 | // selectOnlineTicketsToRefund | AC-E-Ticket | Information Expert | - |
| 11 | // calculateRefundAmount | AC-E-Ticket | Information Expert | Dữ liệu nằm ở nhiều lớp: vé giữ giá vé đã ghi, giao dịch giữ số đã thu của nhiều vé. Chọn Ticket vì BR-07 là 100% giá vé của chính vé đó và giá hiện hành không ảnh hưởng (mục 8); nhờ đó số hoàn không vượt số đã thu cho vé (NFR-06) |
| 11 | // requestTicketRefund | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 12 | // requestTicketRefund (nhận kết quả từ Cổng thanh toán) | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 12a | // recordRefundNotCompleted | AC-E-Ticket | Information Expert | Như bước 9a (Q-58, ASM-42) |
| 13 | // processTripCancellation (lặp theo danh sách vé, fragment F6) | AC-C-CancelTripController | Controller | - |
| 13 | // markRefunded | AC-E-Ticket | Information Expert | - |
| 13 | // recordRefund | AC-E-PaymentTransaction | Information Expert | Dữ liệu nằm ở nhiều lớp: vé giữ trạng thái hoàn tiền, giao dịch thu nhiều vé nên phải cộng số đã hoàn ở giao dịch (ASM-32). Tách thành lớp riêng PaymentTransaction thay vì cộng ở Ticket |
| 14 | // summarizeTripCancellation | AC-E-Ticket | Information Expert | Dữ liệu nằm ở nhiều lớp: tuyến và giờ xuất bến đã có từ // cancelTrip, các số đếm và tổng tiền lấy từ trạng thái của các vé. Giao cho control sẽ làm control giữ quy tắc đếm và cộng thuộc dữ liệu vé (god control) |
| 14 | // showCancellationResult | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| *a | // abortCancelTrip | AC-B-CancelTripForm | Giao tiếp tác nhân | - |
| *a | // requestAbortCancelTrip | AC-C-CancelTripController | Controller | - |
| *a | // notifyCancelTripAborted | AC-B-CancelTripForm | Giao tiếp tác nhân | - |

## F5. Sequence diagram phân tích

### SD1 - Luồng chính và các luồng thay thế 4a, 4b, 7a, 9a, 10a, 12a

a) Trang SD1 của diagrams/P07-sequence-UC-017.drawio. Luồng chính có 27 message không kể message trả về và 3 fragment ở mức ngoài cùng (F1, F2, F3), nằm trong ngưỡng nên không tách đoạn. Luồng 4a, 4b, 9a, 12a dùng alt; luồng 7a dùng alt với toán hạng 1 không có message; luồng 10a là trường hợp vòng lặp F6 không chạy (ghi chú NT7).

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Actor | ACT-03 Nhân viên điều hành | actor | - | Tác nhân chính, loại Người | 40 | 40 | 120 | 2790 |
| L1 | Lifeline | :CancelTripForm | boundary | - | AC-B-CancelTripForm | 200 | 40 | 120 | 2790 |
| L2 | Lifeline | :CancelTripController | control | - | AC-C-CancelTripController | 360 | 40 | 120 | 2790 |
| L3 | Lifeline | :Trip | entity | - | AC-E-Trip | 520 | 40 | 120 | 2790 |
| L4 | Lifeline | :Ticket | entity | - | AC-E-Ticket; đại diện tập vé của chuyến, các trách nhiệm tác động lên nhiều vé được nhận ở mức lớp | 680 | 40 | 120 | 2790 |
| L5 | Lifeline | :PaymentTransaction | entity | - | AC-E-PaymentTransaction | 840 | 40 | 120 | 2790 |
| L6 | Lifeline | :SmsGateway | boundary | - | AC-B-SmsGateway | 1000 | 40 | 120 | 2790 |
| L7 | Lifeline | :PaymentGateway | boundary | - | AC-B-PaymentGateway | 1160 | 40 | 120 | 2790 |
| A2 | Actor | ACT-07 Cổng SMS | actor | - | Tác nhân phụ, loại Hệ thống ngoài | 1320 | 40 | 120 | 2790 |
| A3 | Actor | ACT-06 Cổng thanh toán | actor | - | Tác nhân phụ, loại Hệ thống ngoài | 1480 | 40 | 120 | 2790 |
| F1 | Fragment | alt [chuyến đã bị huỷ (4a)] | - | - | - | 230 | 480 | 340 | 230 |
| F1-O2 | Fragment | [chuyến chưa bị huỷ] | - | F1 | Toán hạng 2 của F1; đường ngăn là edge F1-O2-SEP nét đứt (y=620) | 240 | 630 | 320 | 20 |
| F2 | Fragment | alt [đã đến giờ xuất bến (4b)] | - | - | - | 230 | 820 | 340 | 230 |
| F2-O2 | Fragment | [chưa đến giờ xuất bến] | - | F2 | Toán hạng 2 của F2; đường ngăn là edge F2-O2-SEP nét đứt (y=960) | 240 | 970 | 320 | 20 |
| F3 | Fragment | alt [chuyến không có vé nào đang có hiệu lực (7a)] | - | - | - | 160 | 1320 | 1430 | 1340 |
| F3-O2 | Fragment | [chuyến có vé đang có hiệu lực] | - | F3 | Toán hạng 2 của F3; đường ngăn là edge F3-O2-SEP nét đứt (y=1420) | 170 | 1430 | 1410 | 20 |
| F4 | Fragment | loop [mỗi số điện thoại người đi] | - | F3 | - | 260 | 1550 | 1160 | 410 |
| F5 | Fragment | alt [Cổng SMS báo lỗi hoặc không trả kết quả (9a)] | - | F4 | - | 270 | 1760 | 500 | 180 |
| F5-O2 | Fragment | [đã gửi được] | - | F5 | Toán hạng 2 của F5; đường ngăn là edge F5-O2-SEP nét đứt (y=1850) | 280 | 1860 | 480 | 20 |
| F6 | Fragment | loop [mỗi vé mua trực tuyến chưa hoàn] | - | F3 | - | 380 | 2120 | 1200 | 520 |
| F7 | Fragment | alt [Cổng thanh toán xác nhận đã hoàn] | - | F6 | - | 390 | 2410 | 540 | 210 |
| F7-O2 | Fragment | [báo không thành công hoặc không trả kết quả (12a)] | - | F7 | Toán hạng 2 của F7; đường ngăn là edge F7-O2-SEP nét đứt (y=2540) | 400 | 2550 | 520 | 20 |
| NT1 | Note | quay lại bước 3 | - | F1 | Ghi chú cạnh lifeline L2 | 300 | 570 | 240 | 30 |
| NT2 | Note | tiếp tục luồng chính | - | F1-O2 | Ghi chú cạnh lifeline L2 | 300 | 670 | 240 | 30 |
| NT3 | Note | quay lại bước 3 | - | F2 | Ghi chú cạnh lifeline L2 | 300 | 910 | 240 | 30 |
| NT4 | Note | tiếp tục luồng chính | - | F2-O2 | Ghi chú cạnh lifeline L2 | 300 | 1010 | 240 | 30 |
| NT5 | Note | bỏ qua bước 8-13, tiếp tục bước 14 | - | F3 | Ghi chú cạnh lifeline L2 | 270 | 1370 | 300 | 30 |
| NT6 | Note | tiếp tục vòng lặp | - | F5-O2 | Ghi chú cạnh lifeline L2 | 300 | 1900 | 240 | 30 |
| NT7 | Note | không có vé mua trực tuyến chưa hoàn (10a): vòng lặp không chạy, tiếp tục bước 14 | - | F3-O2 | Ghi chú cạnh lifeline L2 | 200 | 2070 | 440 | 30 |

c) Bảng message (bảng Edge mở rộng)

| STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | A1 | L1 | // requestCancelTrip | Đồng bộ | - | 1 |
| 1.1 | L1 | L2 | // startCancelTrip | Đồng bộ | - | 1 |
| 1.1.1 | L2 | L3 | // listTripsInSchedule | Đồng bộ | - | 2 |
| 1.1.1 (trả về) | L3 | L2 | các chuyến trong lịch chạy kèm tuyến, giờ xuất bến, xe, tài xế, trạng thái | Trả về | - | 2 |
| 1.1.2 | L2 | L1 | // showScheduledTrips (các chuyến trong lịch chạy) | Đồng bộ | - | 2 |
| 2 | A1 | L1 | // selectTripAndReason (chuyến, lý do huỷ chuyến) | Đồng bộ | - | 3 |
| 2.1 | L1 | L2 | // processTripCancellation (chuyến, lý do huỷ chuyến) | Đồng bộ | - | 3 |
| 2.1.1 | L2 | L3 | // checkNotCancelled (BR-09) | Đồng bộ | - | 4 |
| 2.1.1 (trả về) | L3 | L2 | chuyến đã bị huỷ hay chưa | Trả về | - | 4 |
| 2.1.2 | L2 | L1 | // notifyTripAlreadyCancelled | Đồng bộ | F1 | 4a |
| 2.1.3 | L2 | L3 | // checkDepartureNotReached (BR-10) | Đồng bộ | - | 4 |
| 2.1.3 (trả về) | L3 | L2 | đã đến giờ xuất bến hay chưa | Trả về | - | 4 |
| 2.1.4 | L2 | L1 | // notifyTripDeparted | Đồng bộ | F2 | 4b |
| 2.1.5 | L2 | L3 | // cancelTrip (chuyến, lý do huỷ chuyến) | Đồng bộ | - | 5 |
| 2.1.5 (trả về) | L3 | L2 | tuyến và giờ xuất bến của chuyến đã huỷ | Trả về | - | 5 |
| 2.1.6 | L2 | L2 | // cancelOverdueReservationMark (chuyến, mốc 60 phút, UC-007) | Tự gọi | - | 6 |
| 2.1.7 | L2 | L2 | // cancelPassengerListMark (chuyến, mốc 15 phút, UC-025) | Tự gọi | - | 6 |
| 2.1.8 | L2 | L4 | // cancelTicketsOfTrip (chuyến) | Đồng bộ | - | 7 |
| 2.1.8 (trả về) | L4 | L2 | các vé đã huỷ của chuyến | Trả về | - | 7 |
| 2.1.9 | L2 | L4 | // groupTicketCodesByTravelerPhone (các vé đã huỷ) | Đồng bộ | F3-O2 | 8, 10 |
| 2.1.9 (trả về) | L4 | L2 | danh sách số điện thoại người đi kèm mã các vé của số đó | Trả về | F3-O2 | 8, 10 |
| 2.1.10 | L2 | L6 | // sendTripCancellationBySms (số điện thoại, tuyến, giờ xuất bến, mã vé) | Đồng bộ | F4 | 8 |
| 2.1.10.1 | L6 | A2 | // deliverTripCancellationSms (nội dung thông báo) | Đồng bộ | F4 | 8 |
| 2.1.10.1 (trả về) | A2 | L6 | kết quả gửi SMS | Trả về | F4 | 9 |
| 2.1.10 (trả về) | L6 | L2 | kết quả gửi SMS | Trả về | F4 | 9 |
| 2.1.11 | L2 | L4 | // recordCancelNoticeNotSent (số điện thoại, mã vé) | Đồng bộ | F5 | 9a |
| 2.1.12 | L2 | L4 | // selectOnlineTicketsToRefund (các vé đã huỷ) | Đồng bộ | F3-O2 | 11, 13 |
| 2.1.12 (trả về) | L4 | L2 | các vé mua trực tuyến chưa hoàn kèm giao dịch thanh toán và giá vé | Trả về | F3-O2 | 11 |
| 2.1.13 | L2 | L4 | // calculateRefundAmount (BR-07) | Đồng bộ | F6 | 11 |
| 2.1.13 (trả về) | L4 | L2 | số tiền hoàn bằng 100% giá vé | Trả về | F6 | 11 |
| 2.1.14 | L2 | L7 | // requestTicketRefund (giao dịch, mã vé, số tiền hoàn) | Đồng bộ | F6 | 11 |
| 2.1.14.1 | L7 | A3 | // deliverRefundRequest (giao dịch, mã vé, số tiền hoàn) | Đồng bộ | F6 | 11 |
| 2.1.14.1 (trả về) | A3 | L7 | kết quả hoàn tiền | Trả về | F6 | 12 |
| 2.1.14 (trả về) | L7 | L2 | kết quả hoàn tiền | Trả về | F6 | 12 |
| 2.1.15 | L2 | L4 | // markRefunded | Đồng bộ | F7 | 13 |
| 2.1.16 | L2 | L5 | // recordRefund (vé, số tiền hoàn) | Đồng bộ | F7 | 13 |
| 2.1.17 | L2 | L4 | // recordRefundNotCompleted | Đồng bộ | F7-O2 | 12a |
| 2.1.18 | L2 | L4 | // summarizeTripCancellation (các vé đã huỷ) | Đồng bộ | - | 14 |
| 2.1.18 (trả về) | L4 | L2 | số vé đã huỷ; số điện thoại đã báo và chưa báo được; vé mua trực tuyến đã hoàn và chưa hoàn được; số vé mua tại quầy chờ hoàn tiền mặt | Trả về | - | 14 |
| 2.1.19 | L2 | L1 | // showCancellationResult (kết quả huỷ chuyến) | Đồng bộ | - | 14 |

### SD2 - Luồng *a

a) Trang SD2 của diagrams/P07-sequence-UC-017.drawio. Luồng *a (nhân viên điều hành bỏ yêu cầu huỷ chuyến tại bất kỳ bước nào trước bước 5) rẽ tại message 1.1.2 của SD1, sau khi hệ thống hiển thị các chuyến trong lịch chạy. Dùng break vì luồng kết thúc use case. Trang bắt đầu bằng fragment ref tới SD1.

b) Bảng lifeline và fragment (bảng Node; ID lifeline có tiền tố S2- để không trùng với SD1)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S2-A1 | Actor | ACT-03 Nhân viên điều hành | actor | - | Tác nhân chính | 40 | 40 | 120 | 360 |
| S2-L1 | Lifeline | :CancelTripForm | boundary | - | AC-B-CancelTripForm | 200 | 40 | 120 | 360 |
| S2-L2 | Lifeline | :CancelTripController | control | - | AC-C-CancelTripController | 360 | 40 | 120 | 360 |
| R1 | Fragment | ref [SD1 - message 1 đến 1.1.2] | - | - | Điểm rẽ: sau message 1.1.2 của SD1 | 40 | 100 | 440 | 60 |
| F8 | Fragment | break [nhân viên điều hành bỏ yêu cầu huỷ chuyến (*a)] | - | - | - | 70 | 190 | 380 | 160 |

c) Bảng message (bảng Edge mở rộng)

| STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1.1.2*a | S2-A1 | S2-L1 | // abortCancelTrip | Đồng bộ | F8 | *a |
| 1.1.2*a.1 | S2-L1 | S2-L2 | // requestAbortCancelTrip | Đồng bộ | F8 | *a |
| 1.1.2*a.1.1 | S2-L2 | S2-L1 | // notifyCancelTripAborted | Đồng bộ | F8 | *a |

## F6. Vi phạm quy tắc tương tác

Không có

## F7. Communication diagram

File diagrams/P07-communication-UC-017.drawio (một trang COMM1). Phạm vi: luồng chính (SD1) và, vì MUC_CHI_TIET là DAY_DU, mọi luồng thay thế gồm 4a, 4b, 7a, 9a, 10a, 12a (có trong SD1 nên giữ STT của SD1) và *a (giữ STT của SD2). Tổng 30 message, bằng số message không kể trả về của SD1 (27) và SD2 (3).

a) Bảng Node

| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Actor | ACT-03 Nhân viên điều hành | actor | - | Tác nhân chính | 40 | 270 | 40 | 80 |
| L1 | Object | :CancelTripForm | boundary | - | AC-B-CancelTripForm | 240 | 270 | 200 | 60 |
| L2 | Object | :CancelTripController | control | - | AC-C-CancelTripController | 640 | 270 | 240 | 60 |
| L3 | Object | :Trip | entity | - | AC-E-Trip | 480 | 560 | 160 | 60 |
| L4 | Object | :Ticket | entity | - | AC-E-Ticket; đại diện tập vé của chuyến | 720 | 560 | 160 | 60 |
| L5 | Object | :PaymentTransaction | entity | - | AC-E-PaymentTransaction | 960 | 560 | 200 | 60 |
| L6 | Object | :SmsGateway | boundary | - | AC-B-SmsGateway | 1000 | 100 | 200 | 60 |
| L7 | Object | :PaymentGateway | boundary | - | AC-B-PaymentGateway | 1000 | 270 | 200 | 60 |
| A2 | Actor | ACT-07 Cổng SMS | actor | - | Tác nhân phụ | 1320 | 90 | 40 | 80 |
| A3 | Actor | ACT-06 Cổng thanh toán | actor | - | Tác nhân phụ | 1320 | 260 | 40 | 80 |

b) Bảng Edge (link)

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message (Nguồn-->Đích hoặc Đích-->Nguồn) |
|---|---|---|---|---|---|
| CL01 | A1 | L1 | Link | 1: // requestCancelTrip (-->)<br>1.1.2*a: // abortCancelTrip (-->)<br>2: // selectTripAndReason (chuyến, lý do huỷ chuyến) (-->) | A1-->L1: 1, 1.1.2*a, 2 |
| CL02 | L1 | L2 | Link | 1.1: // startCancelTrip (-->)<br>1.1.2: // showScheduledTrips (các chuyến trong lịch chạy) (<--)<br>1.1.2*a.1: // requestAbortCancelTrip (-->)<br>1.1.2*a.1.1: // notifyCancelTripAborted (<--)<br>2.1: // processTripCancellation (chuyến, lý do huỷ chuyến) (-->)<br>2.1.2: // notifyTripAlreadyCancelled (<--)<br>2.1.4: // notifyTripDeparted (<--)<br>2.1.19: // showCancellationResult (kết quả huỷ chuyến) (<--) | L1-->L2: 1.1, 1.1.2*a.1, 2.1; L2-->L1: 1.1.2, 1.1.2*a.1.1, 2.1.2, 2.1.4, 2.1.19 |
| CL03 | L2 | L3 | Link | 1.1.1: // listTripsInSchedule (-->)<br>2.1.1: // checkNotCancelled (BR-09) (-->)<br>2.1.3: // checkDepartureNotReached (BR-10) (-->)<br>2.1.5: // cancelTrip (chuyến, lý do huỷ chuyến) (-->) | L2-->L3: 1.1.1, 2.1.1, 2.1.3, 2.1.5 |
| CL04 | L2 | L4 | Link | 2.1.8: // cancelTicketsOfTrip (chuyến) (-->)<br>2.1.9: // groupTicketCodesByTravelerPhone (các vé đã huỷ) (-->)<br>2.1.11: // recordCancelNoticeNotSent (số điện thoại, mã vé) (-->)<br>2.1.12: // selectOnlineTicketsToRefund (các vé đã huỷ) (-->)<br>2.1.13: // calculateRefundAmount (BR-07) (-->)<br>2.1.15: // markRefunded (-->)<br>2.1.17: // recordRefundNotCompleted (-->)<br>2.1.18: // summarizeTripCancellation (các vé đã huỷ) (-->) | L2-->L4: 2.1.8, 2.1.9, 2.1.11, 2.1.12, 2.1.13, 2.1.15, 2.1.17, 2.1.18 |
| CL05 | L2 | L5 | Link | 2.1.16: // recordRefund (vé, số tiền hoàn) (-->) | L2-->L5: 2.1.16 |
| CL06 | L2 | L6 | Link | 2.1.10: // sendTripCancellationBySms (số điện thoại, tuyến, giờ xuất bến, mã vé) (-->) | L2-->L6: 2.1.10 |
| CL07 | L2 | L7 | Link | 2.1.14: // requestTicketRefund (giao dịch, mã vé, số tiền hoàn) (-->) | L2-->L7: 2.1.14 |
| CL08 | L6 | A2 | Link | 2.1.10.1: // deliverTripCancellationSms (nội dung thông báo) (-->) | L6-->A2: 2.1.10.1 |
| CL09 | L7 | A3 | Link | 2.1.14.1: // deliverRefundRequest (giao dịch, mã vé, số tiền hoàn) (-->) | L7-->A3: 2.1.14.1 |
| CL10 | L2 | L2 | Link | 2.1.6: // cancelOverdueReservationMark (chuyến, mốc 60 phút, UC-007) (-->)<br>2.1.7: // cancelPassengerListMark (chuyến, mốc 15 phút, UC-025) (-->) | Tự gọi: 2.1.6, 2.1.7 |

## F8. VOPC (View Of Participating Classes)

File diagrams/P07-class-UC-017.drawio (một trang VOPC).

a) Bảng Node (lớp)

| ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-CancelTripForm | Class | CancelTripForm | boundary | - | scheduledTrips<br>selectedTrip<br>cancelReason<br>cancellationResult | // requestCancelTrip<br>// showScheduledTrips<br>// selectTripAndReason<br>// notifyTripAlreadyCancelled<br>// notifyTripDeparted<br>// abortCancelTrip<br>// notifyCancelTripAborted<br>// showCancellationResult |
| AC-B-SmsGateway | Class | SmsGateway | boundary | - | recipientPhone<br>ticketCodes<br>noticeContent | // sendTripCancellationBySms |
| AC-B-PaymentGateway | Class | PaymentGateway | boundary | - | transactionCode<br>ticketCode<br>refundAmount<br>refundResult | // requestTicketRefund |
| AC-C-CancelTripController | Class | CancelTripController | control | - | - | // startCancelTrip<br>// processTripCancellation<br>// requestAbortCancelTrip<br>// cancelOverdueReservationMark<br>// cancelPassengerListMark |
| AC-E-Trip | Class | Trip | entity | - | departureTime<br>route<br>status<br>cancelReason<br>vehicle<br>driver | // listTripsInSchedule<br>// checkNotCancelled<br>// checkDepartureNotReached<br>// cancelTrip |
| AC-E-Ticket | Class | Ticket | entity | - | ticketCode<br>travelerPhone<br>fare<br>purchaseChannel<br>status<br>paymentStatus<br>refundStatus<br>cancelNoticeStatus<br>refundAttemptStatus | // cancelTicketsOfTrip<br>// groupTicketCodesByTravelerPhone<br>// recordCancelNoticeNotSent<br>// selectOnlineTicketsToRefund<br>// calculateRefundAmount<br>// markRefunded<br>// recordRefundNotCompleted<br>// summarizeTripCancellation |
| AC-E-PaymentTransaction | Class | PaymentTransaction | entity | - | transactionCode<br>collectedAmount<br>refundedAmount | // recordRefund |

b) Bảng quan hệ (bảng Edge)

| ID | Lớp A | Lớp B | Loại (Association / Aggregation / Composition / Generalization / Dependency) | Multiplicity | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC017-01 | CancelTripForm | CancelTripController | Association | - | - | Link CL02 (1.1, 2.1, 1.1.2*a.1 và các message hiển thị 1.1.2, 2.1.2, 2.1.4, 2.1.19, 1.1.2*a.1.1); tạm thời |
| R-UC017-02 | CancelTripController | Trip | Association | - | - | Link CL03 (1.1.1, 2.1.1, 2.1.3, 2.1.5); tạm thời |
| R-UC017-03 | CancelTripController | Ticket | Association | - | - | Link CL04 (2.1.8, 2.1.9, 2.1.11, 2.1.12, 2.1.13, 2.1.15, 2.1.17, 2.1.18); tạm thời |
| R-UC017-04 | CancelTripController | PaymentTransaction | Association | - | - | Link CL05 (2.1.16); tạm thời |
| R-UC017-05 | CancelTripController | SmsGateway | Association | - | - | Link CL06 (2.1.10); tạm thời |
| R-UC017-06 | CancelTripController | PaymentGateway | Association | - | - | Link CL07 (2.1.14); tạm thời |
| R-UC017-07 | Ticket | Trip | Association | A 0..* - B 1 | - | Bằng chứng từ đặc tả: bước 7 "các vé đang có hiệu lực của chuyến", GL-23 (thành phần chuyến xe), luồng 7a (chuyến có thể không có vé); không có link trong F7 |
| R-UC017-08 | Ticket | PaymentTransaction | Association | A 0..* - B 0..1 | - | Bằng chứng từ đặc tả: Dữ liệu ra 3 dòng 1 "Giao dịch đã thu tiền vé qua Cổng thanh toán ... mà khoản hoàn gắn vào", GL-06 (giao dịch Không thành công không có vé), ASM-32 (một giao dịch thu nhiều vé), BR-08 (vé mua tại quầy không có giao dịch) |

Link CL01, CL08, CL09 nối actor với boundary nên không vào VOPC; link CL10 là link tự nối nên không sinh quan hệ.

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1, 1.1 | AC-B-CancelTripForm, AC-C-CancelTripController |
| 2 | 1.1.1, 1.1.1 (trả về), 1.1.2 | AC-C-CancelTripController, AC-E-Trip, AC-B-CancelTripForm |
| 3 | 2, 2.1 | AC-B-CancelTripForm, AC-C-CancelTripController |
| 4 | 2.1.1, 2.1.1 (trả về), 2.1.3, 2.1.3 (trả về) | AC-C-CancelTripController, AC-E-Trip |
| 4a | 2.1.2 | AC-C-CancelTripController, AC-B-CancelTripForm |
| 4b | 2.1.4 | AC-C-CancelTripController, AC-B-CancelTripForm |
| 5 | 2.1.5, 2.1.5 (trả về) | AC-C-CancelTripController, AC-E-Trip |
| 6 | 2.1.6, 2.1.7 | AC-C-CancelTripController |
| 7 | 2.1.8, 2.1.8 (trả về) | AC-C-CancelTripController, AC-E-Ticket |
| 7a | F3 toán hạng 1 (không có message; ghi chú NT5) | AC-C-CancelTripController, AC-E-Ticket |
| 8 | 2.1.9, 2.1.9 (trả về), 2.1.10, 2.1.10.1 | AC-C-CancelTripController, AC-E-Ticket, AC-B-SmsGateway |
| 9 | 2.1.10.1 (trả về), 2.1.10 (trả về) | AC-B-SmsGateway, AC-C-CancelTripController |
| 9a | 2.1.11 | AC-C-CancelTripController, AC-E-Ticket |
| 10 | 2.1.9, 2.1.9 (trả về), vòng lặp F4 | AC-C-CancelTripController, AC-E-Ticket |
| 10a | 2.1.12 (trả về rỗng), F6 không lặp (ghi chú NT7) | AC-C-CancelTripController, AC-E-Ticket |
| 11 | 2.1.12, 2.1.12 (trả về), 2.1.13, 2.1.13 (trả về), 2.1.14, 2.1.14.1 | AC-C-CancelTripController, AC-E-Ticket, AC-B-PaymentGateway |
| 12 | 2.1.14.1 (trả về), 2.1.14 (trả về) | AC-B-PaymentGateway, AC-C-CancelTripController |
| 12a | 2.1.17 | AC-C-CancelTripController, AC-E-Ticket |
| 13 | 2.1.12, 2.1.15, 2.1.16, vòng lặp F6 | AC-C-CancelTripController, AC-E-Ticket, AC-E-PaymentTransaction |
| 14 | 2.1.18, 2.1.18 (trả về), 2.1.19 | AC-C-CancelTripController, AC-E-Ticket, AC-B-CancelTripForm |
| *a | 1.1.2*a, 1.1.2*a.1, 1.1.2*a.1.1 | AC-B-CancelTripForm, AC-C-CancelTripController |

## F10. File .drawio

Ba file trong diagrams/: P07-sequence-UC-017.drawio (hai trang SD1, SD2), P07-communication-UC-017.drawio (một trang COMM1), P07-class-UC-017.drawio (một trang VOPC). ID cell trùng ID trong các bảng ở F5, F7, F8; toạ độ là bội số của 10. ID cell của message trong sequence diagram suy ra từ STT: "M" cộng STT (ví dụ M2.1.3), message trả về thêm hậu tố "-R" (ví dụ M2.1.3-R).

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-58 | Việc ghi nhận số điện thoại và vé chưa được báo huỷ chuyến qua SMS (luồng 9a) và vé chưa hoàn được tiền (luồng 12a) lưu những gì và để ai dùng xử lý tiếp? (Chỉ đánh dấu trạng thái trên từng vé / Lưu bản ghi riêng cho từng lần thất bại để nhân viên xử lý lại) | AC-E-Ticket (cancelNoticeStatus, refundAttemptStatus, recordCancelNoticeNotSent, recordRefundNotCompleted), message 2.1.11, 2.1.17, bước 14, ASM-42 | UC-017 luồng 9a "Ghi nhận số điện thoại và mã các vé chưa được báo qua SMS" và luồng 12a "Ghi nhận vé chưa được hoàn tiền" không nêu ghi nhận ở đâu và dùng vào việc gì; mục 8 giao cơ chế xử lý lại cho P06 chờ Q-49, Q-50 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-42 | Việc ghi nhận ở luồng 9a và 12a của UC-017 được thể hiện bằng thuộc tính trạng thái trên từng vé liên quan: cancelNoticeStatus (Chưa báo được) cho các vé của số điện thoại chưa báo được, refundAttemptStatus (Hoàn không thành công) cho vé mua trực tuyến chưa hoàn được; không có bản ghi riêng. Số điện thoại chưa báo được lấy từ travelerPhone của các vé đó. | Chờ Q-58. UC-017 nêu ghi nhận nhưng không nêu nơi ghi; chọn dấu trên vé, nhất quán với ASM-39 của UC-009 và không thêm khái niệm ngoài P05 | AC-E-Ticket (cancelNoticeStatus, refundAttemptStatus, recordCancelNoticeNotSent, recordRefundNotCompleted, summarizeTripCancellation); message 2.1.11, 2.1.17, 2.1.18; luồng 9a, 12a |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-017 (bước 12, 13, hậu điều kiện thành công) | Trạng thái hoàn tiền "Đã hoàn" và việc ghi khoản hoàn vào giao dịch thanh toán chỉ có ở hậu điều kiện, không có bước hệ thống nào ghi nhận kết quả hoàn tiền thành công | Thêm vào bước 13 (hoặc thêm một bước sau bước 12) việc hệ thống ghi nhận vé "Đã hoàn" và khoản hoàn vào giao dịch thanh toán khi Cổng thanh toán xác nhận |
| P04 | UC-017 (luồng 9a, 12a) | Nơi ghi nhận số điện thoại và vé chưa báo được, vé chưa hoàn được không nêu (Q-58, ASM-42) | Nêu dữ liệu được ghi nhận ở luồng 9a, 12a theo câu trả lời Q-58 |
| P05 | GL-23 Vé | Thành phần của vé không có giao dịch thanh toán và trạng thái thanh toán, nhưng UC-017 cần giao dịch đã thu tiền vé để hoàn (Dữ liệu ra 3 dòng 1) và cần phân biệt vé đã thanh toán với vé đặt qua điện thoại chưa thanh toán (mục 8) | Thêm "giao dịch thanh toán (vé mua trực tuyến)" và "trạng thái thanh toán" vào thành phần của GL-23 |
| P05 | GL-06 Giao dịch thanh toán | Thành phần của giao dịch không nêu số tiền đã thu và số tiền đã hoàn, trong khi ASM-32 cho phép hoàn một phần số tiền của giao dịch thu nhiều vé | Thêm "số tiền đã thu" và "số tiền đã hoàn" vào thành phần của GL-06 |

## Vấn đề còn mở

- Boundary và entity thuộc use case khác chưa có P07 (A1): AC-B-PaymentGateway và AC-E-PaymentTransaction (chủ sở hữu UC-010 Thanh toán vé trực tuyến, mã cấp tại UC-017); AC-E-Trip (UC-016 Lập lịch chạy tuần, mã cấp tại UC-009); AC-B-SmsGateway (cũng được UC-003, UC-014 dùng, mã cấp tại UC-009). P07 của các use case đó phải dùng lại các mã này. UC-009 giao boundary của ACT-06 cho P07 của UC-010; P07 của UC-010 dùng lại AC-B-PaymentGateway thay vì cấp mã khác.
- Xe và tài xế chỉ được hiển thị ở bước 2 nên là tham chiếu vehicle, driver của Trip; danh mục xe (UC-021) và tài xế (UC-022) chưa có P07, P08 xét có tách thành entity hay không.
- Các giá trị purchaseChannel (Tại quầy), paymentStatus của vé bán tại quầy và vé đặt qua điện thoại do P07 của UC-004, UC-005, UC-006 chốt; UC-017 chỉ cần phân biệt kênh Trực tuyến với Tại quầy và vé đã thanh toán với chưa thanh toán (P04 mục 8, GL-26, GL-27, GL-28).
- Liên kết giữa vé và giao dịch thanh toán mà UC-009 nêu ở Vấn đề còn mở được UC-017 thể hiện bằng quan hệ R-UC017-08 (Ticket - PaymentTransaction); P08 hợp nhất với P07 của UC-010 và UC-012.
- UC-017 không đổi Seat và Booking của UC-009: P04 không nêu việc trả chỗ về trạng thái trống khi chuyến bị huỷ, và chuyến đã huỷ không còn được bán.
- Mốc thời gian (A2): chuyến là đối tượng mốc của UC-007 (60 phút, BR-12) và UC-025 (15 phút, BR-26); UC-017 làm chuyến mất hiệu lực nên có hai message tự gọi 2.1.6, 2.1.7 theo P04 bước 6 và ASM-28 (chờ Q-47). Message hẹn mốc ở use case tạo chuyến (UC-016) và tạo vé đặt qua điện thoại (UC-005) thuộc P07 của các use case đó.
- Lifeline :Ticket ở sequence diagram đại diện tập các vé của chuyến: các trách nhiệm cancelTicketsOfTrip, groupTicketCodesByTravelerPhone, selectOnlineTicketsToRefund, summarizeTripCancellation tác động lên nhiều vé nên được nhận ở mức lớp. P08 và P12 quyết định giao cho lớp nào (ví dụ một lớp tập hợp vé của chuyến).
- Bước 10 và 13 là bước "Lặp lại" không có hành động riêng: được thể hiện bằng fragment loop F4, F6 và gắn với message sinh danh sách lặp (2.1.9, 2.1.12). Bước ghi nhận kết quả hoàn tiền thành công (2.1.15, 2.1.16) không có bước riêng trong P04 nên gắn vào bước 13; xem Đề xuất sửa artifact trước.
- NFR-05 (mỗi vé trực tuyến được yêu cầu hoàn đúng một lần) được bảo đảm ở mức phân tích nhờ chỉ chọn các vé đã huỷ ở lần này còn trạng thái hoàn tiền Chưa hoàn; việc tính lần xử lý lại khi hoàn tiền thất bại chờ Q-50. NFR-06 được bảo đảm nhờ số hoàn là 100% giá vé đã ghi của chính vé đó. NFR-03 (chỉ nhân viên điều hành) dựa vào tiền điều kiện của use case và UC-003, không vẽ message phân quyền ở mức phân tích.
- Luồng *a vẽ ở trang SD2 tại một điểm rẽ đại diện (sau message 1.1.2, khi nhân viên điều hành đã thấy danh sách chuyến); luồng áp dụng ở mọi bước trước bước 5 với cùng ba message. Luồng 4a, 4b quay lại bước 3 nên nhân viên điều hành cũng có thể bỏ yêu cầu sau khi bị từ chối.
- Các file .drawio sinh từ bảng mô hình bằng chương trình và đã kiểm tra tự động (XML hợp lệ, toạ độ bội số của 10, fragment lồng nhau đúng, note không chồng nhau, khoảng cách tối thiểu 40 giữa các lớp của VOPC, link communication không cắt node). Chưa mở bằng draw.io để xem bằng mắt; nhãn dài trên link CL02, CL04 của communication diagram và nhãn message dài của sequence diagram có thể cần chỉnh vị trí.
