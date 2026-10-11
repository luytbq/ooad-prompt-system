# P07 - Phân tích use case UC-009 Đặt vé trực tuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-009-book-ticket-online.md (phiên bản 1.0, toàn bộ, Q-45, ASM-24); P01-actors.md (phiên bản 1.0, Mục 2); P02-usecases.md (phiên bản 1.1, dòng UC-009 ở Mục 4, các dòng UC có tác nhân thời gian UC-007, UC-025); P03-usecase-model.md (phiên bản 1.0, các dòng có UC-009 ở Mục 1, Mục 2); P05-glossary.md (phiên bản 1.0, các thuật ngữ đặc tả dùng); P06-supplementary-spec.md (phiên bản 1.0, các BR, NFR có UC-009). Chưa có đặc tả P04 của UC-008, UC-010; chưa có file P07 nào. Q, ASM lớn nhất đã có trước lần chạy: Q-54, ASM-38 (P06); cấp tiếp từ Q-55, ASM-39 |
| Phạm vi | UC-009 |
| Mã Q, ASM cuối đã cấp | Q-57, ASM-41 |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-009 Đặt vé trực tuyến (Book Ticket Online) |
| Tác nhân chính (ACT, loại) | ACT-01 Hành khách (Người) |
| Tác nhân phụ (ACT, loại) | ACT-07 Cổng SMS (Hệ thống ngoài) |
| Include (UC) | UC-008 Tra cứu chuyến xe (tại bước 2), chưa có P07: control tạm AC-C-SearchTripsController, trạng thái "Tạm - chờ P07 của UC-008"<br>UC-010 Thanh toán vé trực tuyến (tại bước 8), chưa có P07: control tạm AC-C-PayTicketOnlineController, trạng thái "Tạm - chờ P07 của UC-010". ACT-06 Cổng thanh toán là tác nhân phụ của UC-010, không tương tác trực tiếp trong UC-009 |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có (UC-009 không là use case extend) |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2: UC-009 không có điểm mở rộng) |
| File P07 đã có được dùng làm sổ đăng ký AC | Không có (đây là file P07 đầu tiên của dự án; sổ đăng ký AC rỗng) |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Hành khách | Yêu cầu mua vé xe trực tuyến. | Không đổi | REQ-04 |
| 2 | Hệ thống | Gọi use case UC-008 Tra cứu chuyến xe để hành khách tìm chuyến theo điểm đi, điểm đến, ngày đi và xem sơ đồ chỗ của chuyến. | Control của UC-009 giao cho control của UC-008 để hành khách tìm chuyến và xem sơ đồ chỗ, rồi nhận lại chuyến hành khách đã chọn hoặc kết quả chưa chọn chuyến. Hiển thị sơ đồ chỗ và chỗ trống thuộc phân tích của UC-008. | REQ-05, REQ-06; GL-03, GL-19; RL-44 |
| 2a | Hệ thống | Thông báo chưa chọn được chuyến để mua vé. | Hệ thống thông báo cho hành khách chưa chọn được chuyến. Chưa có chỗ nào được giữ nên không có chỗ cần trả lại. | REQ-05 |
| 3 | Hành khách | Chọn các chỗ còn trống trên chuyến để mua vé (xem Dữ liệu vào 1). | Không đổi | REQ-07, REQ-08; GL-01, GL-02 |
| 4 | Hệ thống | Kiểm tra các chỗ đã chọn còn trống (BR-02), số chỗ đã chọn không vượt giới hạn (BR-01) và chuyến chưa đến giờ xuất bến (BR-05). | Hệ thống tạo lần đặt vé ở trạng thái đang chọn cho chuyến và các chỗ đã chọn, rồi kiểm tra theo thứ tự: mọi chỗ chưa có vé và chưa bị giữ cho yêu cầu khác (BR-02), số chỗ của lần đặt không quá 5 (BR-01), giờ xuất bến của chuyến chưa tới (BR-05). Khi vi phạm nhiều điều kiện, phản hồi điều kiện đầu tiên theo ASM-23. | BR-01, BR-02, BR-05; GL-01, GL-02, GL-07, GL-12; ASM-23 |
| 4a | Hệ thống | Từ chối yêu cầu chọn chỗ và thông báo chỗ không còn trống (BR-02). | Hệ thống thông báo có chỗ không còn trống rồi hành khách tìm lại chuyến ở bước 2. Lần đặt vé đang chọn bị bỏ, chưa có chỗ nào bị giữ. | BR-02 |
| 4b | Hệ thống | Từ chối yêu cầu chọn chỗ và thông báo giới hạn tối đa 5 chỗ mỗi lần đặt (BR-01). | Hệ thống thông báo giới hạn số chỗ mỗi lần đặt rồi hành khách chọn lại chỗ ở bước 3. Lần đặt vé đang chọn bị bỏ, chưa có chỗ nào bị giữ. | BR-01 |
| 4c | Hệ thống | Từ chối yêu cầu chọn chỗ và thông báo chuyến đã đến giờ xuất bến (BR-05). | Hệ thống thông báo chuyến đã đến giờ xuất bến và kết thúc use case. Lần đặt vé đang chọn bị bỏ, chưa có chỗ nào bị giữ. | BR-05, ASM-21 |
| 5 | Hệ thống | Giữ tạm các chỗ đã chọn cho hành khách trong thời hạn (BR-03, ASM-18). | Hệ thống xác định giá vé của một chỗ theo tuyến xe, loại xe và mức tăng giá của chuyến rồi ghi vào lần đặt (ASM-40), chuyển từng chỗ sang đang giữ và đặt thời hạn giữ chỗ bằng thời điểm giữ cộng 10 phút (BR-03). Control bắt đầu chờ thời hạn giữ chỗ. Hết hạn có thể xảy ra ở mọi bước từ bước 6 đến bước 8 (luồng 5a). | BR-03; REQ-60, REQ-61; GL-05, GL-08, GL-21; ASM-18, ASM-40 |
| 5a | Hệ thống | Trả lại các chỗ đang giữ cho người khác và thông báo hết thời hạn giữ chỗ cho hành khách. | Hết 10 phút kể từ lúc giữ chỗ (BR-03) mà thanh toán chưa thành công: hệ thống chuyển các chỗ đang giữ về trạng thái trống, yêu cầu UC-010 dừng phiên thanh toán nếu còn đang chạy (ASM-41) và thông báo hết thời hạn giữ chỗ. Hết hạn có thể xảy ra ở mọi bước từ bước 6 đến bước 8. | BR-03, BR-06; GL-21; ASM-41 |
| 6 | Hành khách | Nhập và gửi họ tên và số điện thoại của người đi cho cả lần đặt (xem Dữ liệu vào 2, ASM-19). | Không đổi | REQ-09; GL-17; ASM-19 |
| 7 | Hệ thống | Kiểm tra họ tên và số điện thoại của người đi đã được cung cấp. | Hệ thống ghi họ tên và số điện thoại người đi vào lần đặt vé và kiểm tra cả hai đã được cung cấp. Điều kiện hợp lệ khác của hai trường chưa quy định (Q-44). | GL-17; ASM-19; Q-44 |
| 7a | Hệ thống | Từ chối thông tin và thông báo thông tin còn thiếu. | Hệ thống thông báo thông tin người đi còn thiếu rồi hành khách nhập lại ở bước 6. | GL-17 |
| 8 | Hệ thống | Gọi use case UC-010 Thanh toán vé trực tuyến để hành khách thanh toán tiền vé của các chỗ đang giữ. | Hệ thống tính tổng tiền bằng tổng giá vé các chỗ của lần đặt, rồi gọi UC-010 kèm lần đặt vé và tổng tiền và nhận lại kết quả thành công hoặc thất bại. Khi đã có kết quả, hệ thống dừng chờ thời hạn giữ chỗ. | REQ-15, REQ-17; GL-05, GL-12; BR-03; ASM-40 |
| 8a | Hệ thống | Trả lại ngay các chỗ đang giữ cho người khác và thông báo thanh toán không thành công (ASM-24). | Hệ thống chuyển ngay các chỗ đang giữ về trạng thái trống (ASM-24) rồi thông báo thanh toán không thành công. | BR-03; ASM-24 |
| 9 | Hệ thống | Phát hành vé cho các chỗ đang giữ, mỗi chỗ một mã vé (BR-04). | Hệ thống tạo một vé cho mỗi chỗ đang giữ, gắn chuyến, chỗ, họ tên và số điện thoại người đi, giá vé, kênh mua vé trực tuyến và một mã vé riêng (BR-04); các chỗ đó chuyển sang đã bán. UC-009 chỉ thêm vé vào chuyến, không tạo, đổi hay huỷ mốc thời gian tính từ giờ xuất bến (UC-007, UC-025) nên không có message hẹn mốc (P04 mục 8). | BR-04; GL-15, GL-23, GL-28; REQ-18, REQ-19 |
| 10 | Hệ thống | Gửi mã vé của các vé đã phát hành tới số điện thoại người đi qua Cổng SMS (xem Dữ liệu ra 2). | Hệ thống gửi một yêu cầu gửi SMS chứa các mã vé vừa phát hành tới số điện thoại người đi qua Cổng SMS và nhận kết quả của lời gọi. | REQ-20; NFR-12; ASM-19 |
| 11 | Cổng SMS | Trả kết quả gửi SMS. | Không đổi | REQ-20, REQ-21 |
| 11a | Hệ thống | Ghi nhận mã vé chưa gửi được qua SMS; mã vé vẫn được hiển thị cho hành khách ở bước 12 (ASM-20). | Hệ thống ghi nhận trên từng vé liên quan là mã vé chưa gửi được qua SMS (ASM-39). Vé giữ nguyên và mã vé vẫn được hiển thị ở bước 12 (ASM-20). | NFR-12; ASM-20, ASM-39 |
| 12 | Hệ thống | Hiển thị các vé đã phát hành và mã vé cho hành khách (xem Dữ liệu ra 1, ASM-20). | Hệ thống hiển thị cho hành khách từng vé với mã vé, chuyến, chỗ, họ tên người đi và giá vé, cùng tổng tiền của lần đặt (xem Dữ liệu ra 1). | BR-04; GL-15; REQ-18 |
| *a | Hệ thống | Huỷ yêu cầu mua vé, trả lại ngay các chỗ đang giữ và thông báo đã huỷ (ASM-24). Điều kiện: tại bất kỳ bước nào trước bước 8, hành khách huỷ yêu cầu mua vé. | Hệ thống dừng chờ thời hạn giữ chỗ và chuyển các chỗ đang giữ về trạng thái trống (ASM-24) nếu đã giữ chỗ, rồi thông báo đã huỷ. Nếu chưa giữ chỗ thì chỉ thông báo đã huỷ. | BR-03; ASM-24 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-01 Hành khách | Người | BookTicketOnlineForm | Giao diện người dùng | Mới (AC-B-BookTicketOnlineForm, UC-009) | Một boundary cho cặp ACT-01 và UC-009: nhận yêu cầu mua vé, các chỗ đã chọn, họ tên và số điện thoại người đi, yêu cầu huỷ; hiển thị thông báo và các vé đã phát hành. Phần hành khách tương tác trong UC-008 (bước 2) và UC-010 (bước 8) thuộc boundary của hai use case đó |
| ACT-07 Cổng SMS | Hệ thống ngoài | SmsGateway | Giao diện hệ thống | Mới (AC-B-SmsGateway, UC-009) | Cổng SMS chỉ nhận lời gọi gửi SMS từ hệ thống và trả kết quả (NFR-12). Đặt tên theo hệ thống, không hậu tố vì HAU_TO_TEN_LOP là Mặc định; Cổng SMS không trùng tên entity nào. UC-003, UC-014, UC-017 cũng dùng, chưa có P07 nên UC-009 là nơi cấp mã đầu tiên |

ACT-06 Cổng thanh toán chỉ tương tác trong phần hành vi của UC-010 được include nên boundary của nó thuộc P07 của UC-010; không cấp mã ở đây.

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Hành khách | Bước 1, 3, 6, 12; mô tả ngắn | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01, tác nhân chính (GL-09); thông tin về người đi được giữ ở Booking và Ticket |
| 2 | Hệ thống | Mọi bước hệ thống | Loại - mơ hồ | Chủ ngữ chung của bước, không chỉ một khái niệm |
| 3 | Yêu cầu mua vé | Bước 1, luồng *a | Loại - thao tác hoặc sự kiện | Là hành động của hành khách tới boundary, không có dữ liệu lưu riêng |
| 4 | Yêu cầu chọn chỗ | Luồng 4a, 4b, 4c | Loại - thao tác hoặc sự kiện | Là thông điệp chọn chỗ ở bước 3; dữ liệu nằm ở Booking (các chỗ đã chọn) |
| 5 | Use case UC-008 Tra cứu chuyến xe | Bước 2, 2a | Loại - thuộc phân tích của UC-008 | Use case được include; chỉ gọi qua control, không vẽ nội bộ |
| 6 | Điểm đi, điểm đến, ngày đi | Bước 2 | Loại - thuộc phân tích của UC-008 | Dữ liệu hành khách nhập để tìm chuyến, thuộc phần hành vi của UC-008 (Tuyến xe GL-22 giữ điểm đi, điểm đến) |
| 7 | Sơ đồ chỗ | Bước 2 | Loại - thuộc phân tích của UC-008 | Việc xem sơ đồ chỗ thuộc UC-008; UC-009 chỉ dùng mã chỗ qua Seat |
| 8 | Chuyến, chuyến xe | Bước 2, 4, 4c; mô tả ngắn | Entity AC-E-Trip | GL-03; có giờ xuất bến để kiểm tra BR-05 |
| 9 | Tuyến xe | Dữ liệu ra 1 (Chuyến); mục 8 | Loại - khái niệm do UC-020 tạo, use case này chỉ đọc hoặc đổi trạng thái qua entity Trip | GL-22; UC-009 chỉ đọc tuyến của chuyến để hiển thị và xác định giá vé |
| 10 | Loại xe | Mục 8 (giá vé theo loại xe) | Loại - khái niệm do UC-021 tạo, use case này chỉ đọc hoặc đổi trạng thái qua entity Fare | GL-14; chỉ dùng để xác định giá vé |
| 11 | Chỗ (mã chỗ, chỗ đã chọn, chỗ trống) | Bước 3, 4, Dữ liệu vào 1; BR-02 | Entity AC-E-Seat | GL-01; có trạng thái trên chuyến và hành vi kiểm tra, đổi trạng thái |
| 12 | Mã chỗ | Dữ liệu vào 1, Dữ liệu ra 1 | Loại - thuộc tính của Seat | seatCode |
| 13 | Chỗ trống, chỗ còn trống | Bước 3, 4; BR-02 | Loại - thuộc tính của Seat | GL-02; là trạng thái Trống của Seat trên chuyến |
| 14 | Giới hạn tối đa 5 chỗ, số chỗ đã chọn | Bước 4, 4b; BR-01 | Loại - tham số của quy tắc BR-01 | Ngưỡng 5 nằm trong BR-01; số chỗ đã chọn đếm từ Booking |
| 15 | Giờ xuất bến | Bước 4, 4c; BR-05; Dữ liệu ra 1 | Loại - thuộc tính của Trip | GL-07; departureTime |
| 16 | Giữ chỗ, chỗ đang giữ | Bước 5, 5a, 8a, *a; BR-03 | Loại - thao tác hoặc sự kiện | GL-08; là thao tác holdSeats của Booking, trạng thái Đang giữ thuộc Seat và Booking |
| 17 | Thời hạn giữ chỗ | Bước 5, 5a; mục 8; BR-03 | Loại - thuộc tính của Booking | GL-21; holdExpiry |
| 18 | Thời gian giữ chỗ (10 phút) | BR-03 | Loại - tham số của quy tắc BR-03 | GL-20; hằng số 10 phút nằm trong BR-03 |
| 19 | Lần đặt (lần đặt vé) | Bước 6; BR-01; mô tả ngắn | Entity AC-E-Booking | GL-12; nhóm các chỗ của một chuyến, giữ chỗ, thời hạn giữ chỗ và người đi chung, có hành vi riêng |
| 20 | Họ tên người đi | Bước 6, 7; Dữ liệu vào 2, Dữ liệu ra 1 | Loại - thuộc tính của Booking | travelerName; chép sang Ticket khi phát hành vé |
| 21 | Số điện thoại người đi, số điện thoại nhận | Bước 6, 7, 10; Dữ liệu vào 2, Dữ liệu ra 2 | Loại - thuộc tính của Booking | travelerPhone; chép sang Ticket khi phát hành vé |
| 22 | Người đi | Bước 6, 7; hậu điều kiện | Loại - thuộc tính của Ticket | GL-17; họ tên và số điện thoại, không có định danh và vòng đời riêng (ASM-19, một người đi chung cho cả lần đặt) |
| 23 | Điều kiện hợp lệ (của họ tên, số điện thoại) | Dữ liệu vào 2 | Loại - mơ hồ | Chưa quy định (Q-44); P04 ghi "Chưa quy định (Q-44)", không đủ để đặt thành kiểm tra nghiệp vụ |
| 24 | Thông tin (còn thiếu) | Bước 7a | Loại - mơ hồ | Cụ thể là họ tên và số điện thoại người đi |
| 25 | Giá vé (của từng vé) | Dữ liệu ra 1; mục 8 | Loại - thuộc tính của Ticket | fare; giá ghi lại khi bán (GL-05) |
| 26 | Giá vé (mức giá theo tuyến, loại xe) | Mục 8; REQ-60, REQ-61 | Entity AC-E-Fare | GL-05; có quy tắc xác định giá riêng, do UC-023 đặt, UC-009 chỉ đọc (ASM-40) |
| 27 | Mức tăng giá | Mục 8; REQ-61 | Loại - khái niệm do UC-024 tạo, use case này chỉ đọc hoặc đổi trạng thái qua entity Fare | GL-16; Fare áp mức tăng giá nếu có |
| 28 | Tổng tiền | Bước 8; Dữ liệu ra 1 | Loại - giá trị suy ra từ Booking | Tổng giá vé các chỗ của lần đặt, tính khi cần, không lưu |
| 29 | Vé, vé xe, vé đã phát hành | Bước 9, 10, 12; hậu điều kiện | Entity AC-E-Ticket | GL-23; được lưu sau use case, có mã vé, trạng thái và hành vi riêng |
| 30 | Vé mua trực tuyến, kênh mua vé | Tên use case; mô tả ngắn | Loại - thuộc tính của Ticket | GL-11, GL-28; purchaseChannel có giá trị Trực tuyến |
| 31 | Mã vé | Bước 9, 10, 12; BR-04 | Loại - thuộc tính của Ticket | GL-15; ticketCode, mỗi chỗ một mã |
| 32 | Danh sách mã vé, danh sách mã chỗ | Dữ liệu vào 1, Dữ liệu ra 1, Dữ liệu ra 2 | Loại - cấu trúc cài đặt | Danh sách là kết quả hiển thị hoặc truyền đi của các Ticket, Seat đã chọn |
| 33 | SMS (tin nhắn mã vé) | Bước 10, 11; hậu điều kiện | Loại - dữ liệu trao đổi qua boundary SmsGateway | Nội dung gửi đi, không lưu |
| 34 | Kết quả gửi SMS | Bước 11, 11a | Loại - dữ liệu trao đổi qua boundary SmsGateway | Trả về từ Cổng SMS, không lưu; riêng trạng thái chưa gửi được ghi trên Ticket (ASM-39) |
| 35 | Mã vé chưa gửi được qua SMS | Bước 11a; hậu điều kiện | Loại - thuộc tính của Ticket | smsStatus; nơi ghi nhận chọn theo ASM-39 (chờ Q-55) |
| 36 | Cổng SMS | Bước 10, 11; mô tả ngắn | Loại - là tác nhân hoặc ngoài phạm vi | ACT-07, tác nhân phụ; boundary SmsGateway |
| 37 | Cổng thanh toán | Hậu điều kiện; mục 8 | Loại - thuộc phân tích của UC-010 | ACT-06 chỉ xuất hiện trong UC-010; boundary thuộc P07 của UC-010 |
| 38 | Thanh toán, kết quả thanh toán | Bước 8, 8a; BR-03 | Loại - thuộc phân tích của UC-010 | Hành vi và dữ liệu thanh toán thuộc use case được include; UC-009 chỉ nhận kết quả thành công hoặc thất bại |
| 39 | Khoản tiền vé, giao dịch thanh toán | Hậu điều kiện; BR-06; mục 8 | Loại - thuộc phân tích của UC-010 | GL-06; do UC-010 tạo và xử lý (xem Vấn đề còn mở về liên kết với vé) |
| 40 | Use case UC-010 Thanh toán vé trực tuyến | Bước 8, 8a | Loại - thuộc phân tích của UC-010 | Use case được include; chỉ gọi qua control, không vẽ nội bộ |
| 41 | Kết cục của UC-008, UC-010 | Mục 8; bước 2a, 8a | Loại - thao tác hoặc sự kiện | Là kết quả trả về giữa các control, không lưu |
| 42 | Thông báo (chưa chọn chuyến, chỗ không còn trống, hết thời hạn...) | Bước 2a, 4a, 4b, 4c, 5a, 7a, 8a, *a | Loại - dữ liệu trao đổi qua boundary BookTicketOnlineForm | Nội dung hiển thị cho hành khách, không lưu |
| 43 | Định dạng hiển thị (dd/MM/yyyy HH:mm, số có dấu chấm, đ) | Dữ liệu ra 1 | Loại - dữ liệu trao đổi qua boundary BookTicketOnlineForm | Cách trình bày, thuộc boundary |
| 44 | Người khác (nhận lại chỗ) | Bước 5a, 8a, *a; BR-03 | Loại - là tác nhân hoặc ngoài phạm vi | Hành khách khác của lần đặt khác, là ACT-01 |
| 45 | Tài khoản | Yêu cầu đặc biệt 1 | Loại - không tham gia hành vi của use case này (khái niệm của UC-001) | UC-009 không cần tài khoản (NFR-02) |
| 46 | Giao dịch thanh toán thành công đến muộn | BR-06; mục 8 | Loại - thuộc phân tích của UC-010 | Phần xử lý thuộc UC-010 (P04 mục 6, BR-06) |

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| AC-C-BookTicketOnlineController | UC-009 | Mới | Điều phối trình tự đặt vé: gọi UC-008, kiểm tra chỗ đã chọn, giữ chỗ, chờ thời hạn giữ chỗ, gọi UC-010, phát hành vé, gửi mã vé. Không giữ dữ liệu nghiệp vụ lâu dài |
| AC-C-SearchTripsController | UC-008 (include tại bước 2) | Mới - Tạm - chờ P07 của UC-008 | Đặt trước tên và mã theo F3.3 để UC-009 gọi; P07 của UC-008 phải dùng đúng mã này |
| AC-C-PayTicketOnlineController | UC-010 (include tại bước 8) | Mới - Tạm - chờ P07 của UC-010 | Đặt trước tên và mã theo F3.3 để UC-009 gọi; P07 của UC-010 phải dùng đúng mã này |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-BookTicketOnlineForm | boundary | BookTicketOnlineForm | // requestBookTicket: nhận yêu cầu mua vé của hành khách<br>// selectSeats: nhận các chỗ hành khách chọn<br>// enterTravelerInfo: nhận họ tên và số điện thoại người đi<br>// cancelBooking: nhận yêu cầu huỷ mua vé của hành khách<br>// notifyNoTripSelected: thông báo chưa chọn được chuyến<br>// notifySeatsUnavailable: thông báo chỗ không còn trống (BR-02)<br>// notifySeatLimitExceeded: thông báo giới hạn số chỗ mỗi lần đặt (BR-01)<br>// notifyTripDeparted: thông báo chuyến đã đến giờ xuất bến (BR-05)<br>// notifyTravelerInfoMissing: thông báo thông tin người đi còn thiếu<br>// notifyPaymentFailed: thông báo thanh toán không thành công<br>// notifyHoldExpired: thông báo hết thời hạn giữ chỗ (BR-03)<br>// notifyBookingCancelled: thông báo đã huỷ yêu cầu mua vé<br>// showIssuedTickets: hiển thị các vé đã phát hành, mã vé và tổng tiền | selectedSeats (chỗ đã chọn), travelerName (Văn bản), travelerPhone (Văn bản), issuedTickets (mã vé, chuyến, chỗ, giá vé), totalAmount (Số tiền) | 1, 2a, 3, 4a, 4b, 4c, 5a, 6, 7a, 8a, 12, *a | Giao diện người dùng | Mới | - |
| AC-B-SmsGateway | boundary | SmsGateway | // sendTicketCodesBySms: chuyển yêu cầu gửi SMS mã vé cho Cổng SMS và nhận kết quả của lời gọi (NFR-12) | recipientPhone (Văn bản), ticketCodes (Văn bản) | 10, 11 | Giao diện hệ thống | Mới | - |
| AC-C-BookTicketOnlineController | control | BookTicketOnlineController | // startBookTicketOnline: điều phối đặt vé trực tuyến, gọi UC-008 để hành khách tìm chuyến<br>// processSeatSelection: điều phối kiểm tra các chỗ đã chọn, xác định giá vé và giữ chỗ<br>// processTravelerInfo: điều phối ghi người đi, gọi UC-010, phát hành vé, gửi mã vé và hiển thị kết quả<br>// requestCancelBooking: điều phối huỷ yêu cầu mua vé của hành khách<br>// startWaitingForPaymentResult: bắt đầu chờ kết quả thanh toán trong thời hạn giữ chỗ (BR-03)<br>// stopWaitingForPaymentResult: dừng chờ khi đã có kết quả thanh toán hoặc use case kết thúc<br>// handleHoldExpiry: xử lý khi hết thời hạn giữ chỗ (after(BR-03)) | - | 1, 2, 2a, 3, 4, 4a, 4b, 4c, 5, 5a, 6, 7, 7a, 8, 8a, 9, 10, 11, 11a, 12, *a | - | Mới | - |
| AC-C-SearchTripsController | control | SearchTripsController | // searchTrips: điều phối tra cứu chuyến xe của UC-008 (tạm, chờ P07 của UC-008) | - | 2 | - | Mới - Tạm - chờ P07 của UC-008 | - |
| AC-C-PayTicketOnlineController | control | PayTicketOnlineController | // payTicketOnline: điều phối thanh toán vé trực tuyến của UC-010 (tạm, chờ P07 của UC-010)<br>// cancelPayment: dừng phiên thanh toán của lần đặt vé khi hết thời hạn giữ chỗ (ASM-41, tạm) | - | 5a, 8 | - | Mới - Tạm - chờ P07 của UC-010 | - |
| AC-E-Trip | entity | Trip | // checkDepartureNotReached: kiểm tra giờ xuất bến chưa tới (BR-05) | departureTime (Ngày, Giờ), route (Tuyến xe), vehicleType (Loại xe) | 4 | - | Mới - chủ sở hữu UC-016 | GL-03 |
| AC-E-Seat | entity | Seat | // checkAvailable: kiểm tra chỗ chưa có vé và chưa bị giữ (BR-02)<br>// markHeld: chuyển chỗ sang đang giữ, chỉ một yêu cầu giữ được chỗ (NFR-04)<br>// markSold: chuyển chỗ sang đã bán khi vé được phát hành<br>// markAvailable: trả chỗ về trạng thái trống | seatCode (Văn bản), tripState (Trạng thái: Trống, Đang giữ, Đã bán) | 4, 5, 5a, 8a, 9, *a | - | Mới - chủ sở hữu UC-021 | GL-01 |
| AC-E-Fare | entity | Fare | // determineFare: xác định giá vé một chỗ theo tuyến xe, loại xe và mức tăng giá (REQ-60, REQ-61, ASM-40) | route (Tuyến xe), vehicleType (Loại xe), amount (Số tiền), surchargePercent (Phần trăm, nếu có) | 5 | - | Mới - chủ sở hữu UC-023 | GL-05 |
| AC-E-Booking | entity | Booking | // createBooking: tạo lần đặt vé ở trạng thái đang chọn cho chuyến và các chỗ đã chọn<br>// checkSeatCountWithinLimit: kiểm tra số chỗ không quá giới hạn mỗi lần đặt (BR-01)<br>// holdSeats: giữ các chỗ, ghi giá vé, đặt thời điểm bắt đầu và thời hạn giữ chỗ (BR-03)<br>// recordTravelerInfo: ghi họ tên, số điện thoại người đi và kiểm tra đã được cung cấp<br>// calculateTotalAmount: tính tổng tiền bằng tổng giá vé các chỗ<br>// releaseHeldSeats: trả lại các chỗ đang giữ cho người khác (BR-03, ASM-24)<br>// issueTickets: phát hành vé cho các chỗ đang giữ, mỗi chỗ một vé (BR-04) | trip (Chuyến xe), seatCodes (Văn bản), status (Trạng thái: Đang chọn, Đang giữ chỗ, Đã phát hành vé, Đã trả chỗ), holdStartedAt (Giờ), holdExpiry (Giờ), travelerName (Văn bản), travelerPhone (Văn bản), seatFare (Số tiền) | 4, 5, 5a, 7, 8, 8a, 9, *a | - | Mới | GL-12 |
| AC-E-Ticket | entity | Ticket | // createTicket: khởi tạo vé gắn chuyến, chỗ, người đi, giá vé, kênh mua vé trực tuyến<br>// generateTicketCode: gán mã vé riêng cho vé (BR-04)<br>// recordSmsNotSent: ghi nhận mã vé chưa gửi được qua SMS (ASM-39) | ticketCode (Văn bản), travelerName (Văn bản), travelerPhone (Văn bản), fare (Số tiền), purchaseChannel (Trạng thái: Trực tuyến), status (Trạng thái: Đã phát hành), smsStatus (Trạng thái: Chưa gửi được) | 9, 11a | - | Mới | GL-23 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestBookTicket | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 1 | // startBookTicketOnline | AC-C-BookTicketOnlineController | Controller | - |
| 2 | // searchTrips | AC-C-SearchTripsController | Controller | Include UC-008: control gọi control của use case được include, không vẽ lại nội bộ (F5) |
| 2a | // notifyNoTripSelected | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 3 | // selectSeats | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 3 | // processSeatSelection | AC-C-BookTicketOnlineController | Controller | - |
| 4 | // createBooking | AC-E-Booking | Creator | Booking là lớp ghi nhận các chỗ đã chọn của một chuyến (GL-12) và là nơi giữ BR-01 nên là lớp tạo. Phương án khác: control tự giữ danh sách chỗ rồi đếm; bị loại vì quy tắc BR-01 thuộc dữ liệu của lần đặt, đưa vào control là god control |
| 4 | // checkAvailable | AC-E-Seat | Information Expert | Trạng thái chỗ trên chuyến nằm ở Seat. Phương án khác: Booking hỏi từng Seat hoặc control lọc; bị loại vì tăng coupling và đẩy BR-02 sang control |
| 4 | // checkSeatCountWithinLimit | AC-E-Booking | Information Expert | Số chỗ của lần đặt nằm ở Booking. Phương án khác: control đếm; bị loại như trên |
| 4 | // checkDepartureNotReached | AC-E-Trip | Information Expert | Giờ xuất bến nằm ở Trip. Phương án khác: control so giờ; bị loại vì giờ xuất bến là dữ liệu của Trip |
| 4a | // notifySeatsUnavailable | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 4b | // notifySeatLimitExceeded | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 4c | // notifyTripDeparted | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 5 | // determineFare | AC-E-Fare | Information Expert | Quy tắc xác định giá theo tuyến, loại xe, mức tăng giá nằm ở Fare (REQ-60, REQ-61). Phương án khác: Trip hỏi Fare; bị loại vì P04 chưa có bằng chứng về quan hệ Trip và Fare. Thời điểm xác định giá theo ASM-40 |
| 5 | // holdSeats | AC-E-Booking | Information Expert | Booking giữ thời điểm bắt đầu, thời hạn giữ chỗ (GL-21) và danh sách chỗ; Seat giữ trạng thái từng chỗ. Chọn Booking điều phối và Seat đổi trạng thái; phương án control gọi từng Seat bị loại vì tăng coupling |
| 5 | // markHeld | AC-E-Seat | Information Expert | Trạng thái của chỗ do Seat nắm; việc chỉ một yêu cầu giữ được chỗ (NFR-04) kiểm tra tại đây, thất bại coi như luồng 4a |
| 5 | // startWaitingForPaymentResult | AC-C-BookTicketOnlineController | Controller | Thời hạn nội bộ BR-03 không là tác nhân, control ghi nhận bắt đầu chờ (A2) |
| 5a | // handleHoldExpiry | AC-C-BookTicketOnlineController | Controller | Nhận sự kiện hết hạn after(BR-03) và điều phối xử lý (A2) |
| 5a | // releaseHeldSeats | AC-E-Booking | Information Expert | Booking biết các chỗ đang giữ. Dùng cho 5a, 8a, *a vì cùng ý nghĩa; lý do nằm trong tham số message |
| 5a | // markAvailable | AC-E-Seat | Information Expert | Seat đổi trạng thái chỗ về Trống |
| 5a | // cancelPayment | AC-C-PayTicketOnlineController | Controller | Control gọi control của UC-010 (ASM-41, chờ Q-57) |
| 5a | // notifyHoldExpired | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 6 | // enterTravelerInfo | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 6 | // processTravelerInfo | AC-C-BookTicketOnlineController | Controller | - |
| 7 | // recordTravelerInfo | AC-E-Booking | Information Expert | Họ tên và số điện thoại thuộc lần đặt (ASM-19) nên Booking ghi và kiểm tra đã cung cấp. Phương án khác: boundary kiểm tra bắt buộc; bị loại vì điều kiện hợp lệ còn chờ Q-44 và có thể thành quy tắc nghiệp vụ |
| 7a | // notifyTravelerInfoMissing | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 8 | // calculateTotalAmount | AC-E-Booking | Information Expert | Booking giữ giá vé các chỗ. Phương án khác: control cộng; bị loại vì là quy tắc tính toán thuộc dữ liệu của entity |
| 8 | // payTicketOnline | AC-C-PayTicketOnlineController | Controller | Include UC-010: control gọi control của use case được include |
| 8 | // stopWaitingForPaymentResult | AC-C-BookTicketOnlineController | Controller | Có kết quả thanh toán thì dừng chờ (A2) |
| 8a | // releaseHeldSeats, // markAvailable | AC-E-Booking, AC-E-Seat | Information Expert | Như bước 5a, trả chỗ ngay theo ASM-24 |
| 8a | // notifyPaymentFailed | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| 9 | // issueTickets | AC-E-Booking | Creator | Booking chứa chuyến, chỗ, người đi và giá vé nên tạo Ticket. Phương án khác: control tạo Ticket; bị loại vì control không giữ dữ liệu nghiệp vụ |
| 9 | // createTicket, // generateTicketCode | AC-E-Ticket | Information Expert | Vé nắm mã vé của chính nó (BR-04); phạm vi duy nhất của mã trên mọi vé do P12 quyết định |
| 9 | // markSold | AC-E-Seat | Information Expert | Seat đổi trạng thái chỗ sang Đã bán |
| 10 | // sendTicketCodesBySms | AC-B-SmsGateway | Giao tiếp tác nhân | Boundary hệ thống ngoài chuyển yêu cầu cho ACT-07 qua message // requestSmsSending (message tới tác nhân, không phải trách nhiệm của lớp) |
| 11 | Kết quả gửi SMS (message trả về) | AC-B-SmsGateway | Giao tiếp tác nhân | ACT-07 trả kết quả cho boundary, boundary trả cho control |
| 11a | // recordSmsNotSent | AC-E-Ticket | Information Expert | Mã vé thuộc Ticket nên trạng thái gửi SMS ghi trên vé (ASM-39). Phương án khác: Booking giữ; bị loại vì một lần đặt có thể có nhiều vé, mỗi vé một mã |
| 12 | // showIssuedTickets | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| *a | // cancelBooking | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |
| *a | // requestCancelBooking, // stopWaitingForPaymentResult | AC-C-BookTicketOnlineController | Controller | - |
| *a | // releaseHeldSeats, // markAvailable | AC-E-Booking, AC-E-Seat | Information Expert | Như bước 5a; chỉ thực hiện khi đã giữ chỗ |
| *a | // notifyBookingCancelled | AC-B-BookTicketOnlineForm | Giao tiếp tác nhân | - |

## F5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-009.drawio gồm bốn trang. Message gửi tới boundary của tác nhân người thể hiện việc boundary hiển thị hoặc thông báo cho tác nhân; không vẽ thêm message riêng từ boundary tới tác nhân. Lifeline Seat và Ticket đại diện cho từng chỗ, từng vé của lần đặt.

**SD1a - Luồng chính bước 1 đến 5 và các luồng 2a, 4a, 4b, 4c**

Bảng lifeline (bảng Node)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L01 | Actor | Hành khách | - | - | Tác nhân chính ACT-01 Hành khách (Người) |
| L02 | Lifeline | :BookTicketOnlineForm | boundary | - | AC-B-BookTicketOnlineForm; Boundary giao diện người dùng của ACT-01 trong UC-009 |
| L03 | Lifeline | :BookTicketOnlineController | control | - | AC-C-BookTicketOnlineController; Control của UC-009 |
| L04 | Lifeline | :SearchTripsController | control | - | AC-C-SearchTripsController; Control của UC-008 (include, bước 2), đặt tạm, chờ P07 của UC-008 |
| L06 | Lifeline | :Trip | entity | - | AC-E-Trip; Chuyến xe đã chọn ở bước 2 |
| L07 | Lifeline | :Seat | entity | - | AC-E-Seat; Đại diện cho từng chỗ đã chọn của lần đặt |
| L08 | Lifeline | :Fare | entity | - | AC-E-Fare; Giá vé theo tuyến xe, loại xe, mức tăng giá của chuyến |
| L09 | Lifeline | :Booking | entity | - | AC-E-Booking; Lần đặt vé; tạo ở bước 4; đỉnh lifeline đặt tại message tạo |
| SD1a-FR1 | Fragment | break [UC-008 kết thúc mà chưa chọn chuyến (2a)] | - | - | Toán tử break |
| SD1a-FR2 | Fragment | alt [có chỗ không còn trống (4a)] | - | - | Toán tử alt |
| SD1a-FR2-O2 | Fragment | [các chỗ còn trống, quá 5 chỗ (4b)] | - | SD1a-FR2 | Toán hạng 2; đường ngăn SD1a-FR2-O2-SEP |
| SD1a-FR2-O3 | Fragment | [các chỗ còn trống, không quá 5 chỗ] | - | SD1a-FR2 | Toán hạng 3; đường ngăn SD1a-FR2-O3-SEP |
| SD1a-FR3 | Fragment | break [chuyến đã đến giờ xuất bến (4c)] | - | SD1a-FR2-O3 | Toán tử break |
| SD1a-N1 | Note | quay lại bước 2 | - | - | Chú thích |
| SD1a-N2 | Note | quay lại bước 3 | - | - | Chú thích |
| SD1a-N3 | Note | tiếp tục luồng chính | - | - | Chú thích |

Bảng message (bảng Edge)

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1a-M01 | 1 | Hành khách | :BookTicketOnlineForm | // requestBookTicket | Đồng bộ | - | 1 |
| SD1a-M02 | 1.1 | :BookTicketOnlineForm | :BookTicketOnlineController | // startBookTicketOnline | Đồng bộ | - | 1 |
| SD1a-M03 | 1.1.1 | :BookTicketOnlineController | :SearchTripsController | // searchTrips | Đồng bộ | - | 2 |
| SD1a-M04 | 1.1.1 (trả về) | :SearchTripsController | :BookTicketOnlineController | chuyến đã chọn hoặc chưa chọn chuyến | Trả về | - | 2 |
| SD1a-M05 | 1.1.2 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifyNoTripSelected | Đồng bộ | SD1a-FR1 | 2a |
| SD1a-M06 | 2 | Hành khách | :BookTicketOnlineForm | // selectSeats (các chỗ đã chọn) | Đồng bộ | - | 3 |
| SD1a-M07 | 2.1 | :BookTicketOnlineForm | :BookTicketOnlineController | // processSeatSelection (chuyến, các chỗ đã chọn) | Đồng bộ | - | 3 |
| SD1a-M08 | 2.1.1 | :BookTicketOnlineController | :Booking | «create» // createBooking (chuyến, các chỗ đã chọn) | Tạo | - | 4 |
| SD1a-M09 | 2.1.2 | :BookTicketOnlineController | :Seat | // checkAvailable (chuyến, các chỗ đã chọn) | Đồng bộ | - | 4 |
| SD1a-M10 | 2.1.2 (trả về) | :Seat | :BookTicketOnlineController | mọi chỗ còn trống hoặc có chỗ không còn trống | Trả về | - | 4 |
| SD1a-M11 | 2.1.3 | :BookTicketOnlineController | :Booking | // checkSeatCountWithinLimit | Đồng bộ | - | 4 |
| SD1a-M12 | 2.1.3 (trả về) | :Booking | :BookTicketOnlineController | số chỗ trong giới hạn hoặc vượt giới hạn | Trả về | - | 4 |
| SD1a-M13 | 2.1.4 | :BookTicketOnlineController | :Trip | // checkDepartureNotReached (chuyến) | Đồng bộ | - | 4 |
| SD1a-M14 | 2.1.4 (trả về) | :Trip | :BookTicketOnlineController | chuyến chưa đến hoặc đã đến giờ xuất bến | Trả về | - | 4 |
| SD1a-M15 | 2.1.5 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifySeatsUnavailable | Đồng bộ | SD1a-FR2 | 4a |
| SD1a-M16 | 2.1.6 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifySeatLimitExceeded | Đồng bộ | SD1a-FR2-O2 | 4b |
| SD1a-M17 | 2.1.7 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifyTripDeparted | Đồng bộ | SD1a-FR3 | 4c |
| SD1a-M18 | 2.1.8 | :BookTicketOnlineController | :Fare | // determineFare (chuyến) | Đồng bộ | - | 5 |
| SD1a-M19 | 2.1.8 (trả về) | :Fare | :BookTicketOnlineController | giá vé mỗi chỗ | Trả về | - | 5 |
| SD1a-M20 | 2.1.9 | :BookTicketOnlineController | :Booking | // holdSeats (giá vé mỗi chỗ) | Đồng bộ | - | 5 |
| SD1a-M21 | 2.1.9.1 | :Booking | :Seat | // markHeld (thời hạn giữ chỗ) | Đồng bộ | - | 5 |
| SD1a-M22 | 2.1.10 | :BookTicketOnlineController | :BookTicketOnlineController | // startWaitingForPaymentResult (BR-03) | Tự gọi | - | 5 |

**SD1b - Luồng chính bước 6 đến 8 và các luồng 5a, 7a, 8a**

Bảng lifeline (bảng Node)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L01 | Actor | Hành khách | - | - | Tác nhân chính ACT-01 Hành khách (Người) |
| L02 | Lifeline | :BookTicketOnlineForm | boundary | - | AC-B-BookTicketOnlineForm; Boundary giao diện người dùng của ACT-01 trong UC-009 |
| L03 | Lifeline | :BookTicketOnlineController | control | - | AC-C-BookTicketOnlineController; Control của UC-009 |
| L05 | Lifeline | :PayTicketOnlineController | control | - | AC-C-PayTicketOnlineController; Control của UC-010 (include, bước 8), đặt tạm, chờ P07 của UC-010 |
| L07 | Lifeline | :Seat | entity | - | AC-E-Seat; Đại diện cho từng chỗ đã chọn của lần đặt |
| L09 | Lifeline | :Booking | entity | - | AC-E-Booking; Lần đặt vé; tạo ở bước 4 |
| SD1b-REF1 | Fragment | ref SD1a - Luồng chính bước 1 đến 5 | - | - | Fragment ref |
| SD1b-FR1 | Fragment | par | - | - | Toán tử par |
| SD1b-FR1-O2 | Fragment | [theo dõi thời hạn giữ chỗ] | - | SD1b-FR1 | Toán hạng 2; đường ngăn SD1b-FR1-O2-SEP |
| SD1b-FR2 | Fragment | alt [thiếu họ tên hoặc số điện thoại (7a)] | - | SD1b-FR1 | Toán tử alt |
| SD1b-FR2-O2 | Fragment | [đủ họ tên và số điện thoại] | - | SD1b-FR2 | Toán hạng 2; đường ngăn SD1b-FR2-O2-SEP |
| SD1b-FR3 | Fragment | break [UC-010 trả kết quả thất bại (8a)] | - | SD1b-FR1 | Toán tử break |
| SD1b-FR4 | Fragment | break [hết 10 phút (BR-03) mà thanh toán chưa thành công (5a)] | - | SD1b-FR1-O2 | Toán tử break |
| SD1b-N1 | Note | quay lại bước 6 | - | - | Chú thích |
| SD1b-N2 | Note | tiếp tục luồng chính | - | - | Chú thích |

Bảng message (bảng Edge)

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1b-M01 | 3 | Hành khách | :BookTicketOnlineForm | // enterTravelerInfo (họ tên, số điện thoại) | Đồng bộ | SD1b-FR1 | 6 |
| SD1b-M02 | 3.1 | :BookTicketOnlineForm | :BookTicketOnlineController | // processTravelerInfo (họ tên, số điện thoại) | Đồng bộ | SD1b-FR1 | 6 |
| SD1b-M03 | 3.1.1 | :BookTicketOnlineController | :Booking | // recordTravelerInfo (họ tên, số điện thoại) | Đồng bộ | SD1b-FR1 | 7 |
| SD1b-M04 | 3.1.1 (trả về) | :Booking | :BookTicketOnlineController | đã đủ hoặc còn thiếu họ tên, số điện thoại | Trả về | SD1b-FR1 | 7 |
| SD1b-M05 | 3.1.2 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifyTravelerInfoMissing | Đồng bộ | SD1b-FR2 | 7a |
| SD1b-M06 | 3.1.3 | :BookTicketOnlineController | :Booking | // calculateTotalAmount | Đồng bộ | SD1b-FR1 | 8 |
| SD1b-M07 | 3.1.3 (trả về) | :Booking | :BookTicketOnlineController | tổng tiền | Trả về | SD1b-FR1 | 8 |
| SD1b-M08 | 3.1.4 | :BookTicketOnlineController | :PayTicketOnlineController | // payTicketOnline (lần đặt vé, tổng tiền) | Đồng bộ | SD1b-FR1 | 8 |
| SD1b-M09 | 3.1.4 (trả về) | :PayTicketOnlineController | :BookTicketOnlineController | kết quả thanh toán thành công hoặc thất bại | Trả về | SD1b-FR1 | 8 |
| SD1b-M10 | 3.1.5 | :BookTicketOnlineController | :BookTicketOnlineController | // stopWaitingForPaymentResult | Tự gọi | SD1b-FR1 | 8 |
| SD1b-M11 | 3.1.6 | :BookTicketOnlineController | :Booking | // releaseHeldSeats (thanh toán không thành công) | Đồng bộ | SD1b-FR3 | 8a |
| SD1b-M12 | 3.1.6.1 | :Booking | :Seat | // markAvailable | Đồng bộ | SD1b-FR3 | 8a |
| SD1b-M13 | 3.1.7 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifyPaymentFailed | Đồng bộ | SD1b-FR3 | 8a |
| SD1b-M14 | 4 | :BookTicketOnlineController | :BookTicketOnlineController | // after(BR-03) handleHoldExpiry | Tự gọi | SD1b-FR4 | 5a |
| SD1b-M15 | 4.1 | :BookTicketOnlineController | :Booking | // releaseHeldSeats (hết thời hạn giữ chỗ) | Đồng bộ | SD1b-FR4 | 5a |
| SD1b-M16 | 4.1.1 | :Booking | :Seat | // markAvailable | Đồng bộ | SD1b-FR4 | 5a |
| SD1b-M17 | 4.2 | :BookTicketOnlineController | :PayTicketOnlineController | // cancelPayment (nếu UC-010 còn đang chạy) | Đồng bộ | SD1b-FR4 | 5a |
| SD1b-M18 | 4.3 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifyHoldExpired | Đồng bộ | SD1b-FR4 | 5a |

**SD1c - Luồng chính bước 9 đến 12 và luồng 11a**

Bảng lifeline (bảng Node)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L02 | Lifeline | :BookTicketOnlineForm | boundary | - | AC-B-BookTicketOnlineForm; Boundary giao diện người dùng của ACT-01 trong UC-009 |
| L03 | Lifeline | :BookTicketOnlineController | control | - | AC-C-BookTicketOnlineController; Control của UC-009 |
| L07 | Lifeline | :Seat | entity | - | AC-E-Seat; Đại diện cho từng chỗ đã chọn của lần đặt |
| L09 | Lifeline | :Booking | entity | - | AC-E-Booking; Lần đặt vé; tạo ở bước 4 |
| L10 | Lifeline | :Ticket | entity | - | AC-E-Ticket; Đại diện cho từng vé; tạo ở bước 9; đỉnh lifeline đặt tại message tạo |
| L11 | Lifeline | :SmsGateway | boundary | - | AC-B-SmsGateway; Boundary giao diện hệ thống của ACT-07 |
| L12 | Actor | Cổng SMS | - | - | Tác nhân phụ ACT-07 Cổng SMS (Hệ thống ngoài) |
| SD1c-REF1 | Fragment | ref SD1b - Luồng chính bước 6 đến 8 | - | - | Fragment ref |
| SD1c-FR1 | Fragment | loop [mỗi chỗ đang giữ] | - | - | Toán tử loop |
| SD1c-FR2 | Fragment | alt [SMS không gửi được (11a)] | - | - | Toán tử alt |
| SD1c-FR2-O2 | Fragment | [SMS gửi được] | - | SD1c-FR2 | Toán hạng 2; đường ngăn SD1c-FR2-O2-SEP |
| SD1c-N1 | Note | tiếp tục bước 12 | - | - | Chú thích |
| SD1c-N2 | Note | tiếp tục luồng chính | - | - | Chú thích |

Bảng message (bảng Edge)

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1c-M01 | 3.1.8 | :BookTicketOnlineController | :Booking | // issueTickets | Đồng bộ | - | 9 |
| SD1c-M02 | 3.1.8.1 | :Booking | :Ticket | «create» // createTicket (chuyến, chỗ, họ tên, số điện thoại, giá vé) | Tạo | SD1c-FR1 | 9 |
| SD1c-M03 | 3.1.8.1.1 | :Ticket | :Ticket | // generateTicketCode (BR-04) | Tự gọi | SD1c-FR1 | 9 |
| SD1c-M04 | 3.1.8.2 | :Booking | :Seat | // markSold | Đồng bộ | SD1c-FR1 | 9 |
| SD1c-M05 | 3.1.8 (trả về) | :Booking | :BookTicketOnlineController | các vé đã phát hành (mã vé, chỗ, giá vé) | Trả về | - | 9 |
| SD1c-M06 | 3.1.9 | :BookTicketOnlineController | :SmsGateway | // sendTicketCodesBySms (số điện thoại người đi, mã vé) | Đồng bộ | - | 10 |
| SD1c-M07 | 3.1.9.1 | :SmsGateway | Cổng SMS | // requestSmsSending (số điện thoại, mã vé) | Đồng bộ | - | 10 |
| SD1c-M08 | 3.1.9.1 (trả về) | Cổng SMS | :SmsGateway | kết quả gửi SMS | Trả về | - | 11 |
| SD1c-M09 | 3.1.9 (trả về) | :SmsGateway | :BookTicketOnlineController | kết quả gửi SMS | Trả về | - | 11 |
| SD1c-M10 | 3.1.10 | :BookTicketOnlineController | :Ticket | // recordSmsNotSent (mã vé chưa gửi được) | Đồng bộ | SD1c-FR2 | 11a |
| SD1c-M11 | 3.1.11 | :BookTicketOnlineController | :BookTicketOnlineForm | // showIssuedTickets (vé đã phát hành, chuyến, tổng tiền) | Đồng bộ | - | 12 |

**SD2 - Luồng *a (hành khách huỷ yêu cầu mua vé trước bước 8)**

Bảng lifeline (bảng Node)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L01 | Actor | Hành khách | - | - | Tác nhân chính ACT-01 Hành khách (Người) |
| L02 | Lifeline | :BookTicketOnlineForm | boundary | - | AC-B-BookTicketOnlineForm; Boundary giao diện người dùng của ACT-01 trong UC-009 |
| L03 | Lifeline | :BookTicketOnlineController | control | - | AC-C-BookTicketOnlineController; Control của UC-009 |
| L07 | Lifeline | :Seat | entity | - | AC-E-Seat; Đại diện cho từng chỗ đã chọn của lần đặt |
| L09 | Lifeline | :Booking | entity | - | AC-E-Booking; Lần đặt vé; tạo ở bước 4 |
| SD2-REF1 | Fragment | ref SD1a - rẽ nhánh sau message 2.1.10 (luồng *a có thể xảy ra ở bất kỳ bước nào trước bước 8) | - | - | Fragment ref |
| SD2-FR1 | Fragment | break [hành khách huỷ yêu cầu mua vé trước bước 8 (*a)] | - | - | Toán tử break |
| SD2-FR2 | Fragment | opt [đã giữ chỗ] | - | SD2-FR1 | Toán tử opt |

Bảng message (bảng Edge)

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2-M01 | 2.1.10*a | Hành khách | :BookTicketOnlineForm | // cancelBooking | Đồng bộ | SD2-FR1 | *a |
| SD2-M02 | 2.1.10*a.1 | :BookTicketOnlineForm | :BookTicketOnlineController | // requestCancelBooking | Đồng bộ | SD2-FR1 | *a |
| SD2-M03 | 2.1.10*a.2 | :BookTicketOnlineController | :BookTicketOnlineController | // stopWaitingForPaymentResult | Tự gọi | SD2-FR2 | *a |
| SD2-M04 | 2.1.10*a.3 | :BookTicketOnlineController | :Booking | // releaseHeldSeats (hành khách huỷ) | Đồng bộ | SD2-FR2 | *a |
| SD2-M05 | 2.1.10*a.3.1 | :Booking | :Seat | // markAvailable | Đồng bộ | SD2-FR2 | *a |
| SD2-M06 | 2.1.10*a.4 | :BookTicketOnlineController | :BookTicketOnlineForm | // notifyBookingCancelled | Đồng bộ | SD2-FR1 | *a |

## F6. Vi phạm quy tắc tương tác

Không có

## F7. Communication diagram

File diagrams/P07-communication-UC-009.drawio (một trang), gồm mọi message không phải trả về của SD1a, SD1b, SD1c và luồng thay thế SD2 (MUC_CHI_TIET là DAY_DU), giữ nguyên STT của trang chứa message.

a) Bảng Node

| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| O01 | Actor | Hành khách | - | - | Tác nhân chính ACT-01 Hành khách (Người) |
| O02 | Object | :BookTicketOnlineForm | boundary | - | AC-B-BookTicketOnlineForm |
| O03 | Object | :BookTicketOnlineController | control | - | AC-C-BookTicketOnlineController |
| O04 | Object | :SearchTripsController | control | - | AC-C-SearchTripsController |
| O05 | Object | :PayTicketOnlineController | control | - | AC-C-PayTicketOnlineController |
| O06 | Object | :Trip | entity | - | AC-E-Trip |
| O07 | Object | :Seat | entity | - | AC-E-Seat |
| O08 | Object | :Fare | entity | - | AC-E-Fare |
| O09 | Object | :Booking | entity | - | AC-E-Booking |
| O10 | Object | :Ticket | entity | - | AC-E-Ticket |
| O11 | Object | :SmsGateway | boundary | - | AC-B-SmsGateway |
| O12 | Actor | Cổng SMS | - | - | Tác nhân phụ ACT-07 Cổng SMS (Hệ thống ngoài) |

b) Bảng Edge (link)

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message (Nguồn-->Đích hoặc Đích-->Nguồn) |
|---|---|---|---|---|---|
| CL01 | O01 | O02 | Link | 1: // requestBookTicket (-->)<br>2: // selectSeats (các chỗ đã chọn) (-->)<br>2.1.10*a: // cancelBooking (-->)<br>3: // enterTravelerInfo (họ tên, số điện thoại) (-->) | Nguồn-->Đích |
| CL02 | O02 | O03 | Link | 1.1: // startBookTicketOnline (-->)<br>1.1.2: // notifyNoTripSelected (<--)<br>2.1: // processSeatSelection (chuyến, các chỗ đã chọn) (-->)<br>2.1.5: // notifySeatsUnavailable (<--)<br>2.1.6: // notifySeatLimitExceeded (<--)<br>2.1.7: // notifyTripDeparted (<--)<br>2.1.10*a.1: // requestCancelBooking (-->)<br>2.1.10*a.4: // notifyBookingCancelled (<--)<br>3.1: // processTravelerInfo (họ tên, số điện thoại) (-->)<br>3.1.2: // notifyTravelerInfoMissing (<--)<br>3.1.7: // notifyPaymentFailed (<--)<br>3.1.11: // showIssuedTickets (vé đã phát hành, chuyến, tổng tiền) (<--)<br>4.3: // notifyHoldExpired (<--) | Cả hai chiều theo nhãn từng message |
| CL03 | O03 | O04 | Link | 1.1.1: // searchTrips (-->) | Nguồn-->Đích |
| CL04 | O03 | O05 | Link | 3.1.4: // payTicketOnline (lần đặt vé, tổng tiền) (-->)<br>4.2: // cancelPayment (nếu UC-010 còn đang chạy) (-->) | Nguồn-->Đích |
| CL05 | O03 | O06 | Link | 2.1.4: // checkDepartureNotReached (chuyến) (-->) | Nguồn-->Đích |
| CL06 | O03 | O07 | Link | 2.1.2: // checkAvailable (chuyến, các chỗ đã chọn) (-->) | Nguồn-->Đích |
| CL07 | O03 | O08 | Link | 2.1.8: // determineFare (chuyến) (-->) | Nguồn-->Đích |
| CL08 | O03 | O09 | Link | 2.1.1: «create» // createBooking (chuyến, các chỗ đã chọn) (-->)<br>2.1.3: // checkSeatCountWithinLimit (-->)<br>2.1.9: // holdSeats (giá vé mỗi chỗ) (-->)<br>2.1.10*a.3: // releaseHeldSeats (hành khách huỷ) (-->)<br>3.1.1: // recordTravelerInfo (họ tên, số điện thoại) (-->)<br>3.1.3: // calculateTotalAmount (-->)<br>3.1.6: // releaseHeldSeats (thanh toán không thành công) (-->)<br>3.1.8: // issueTickets (-->)<br>4.1: // releaseHeldSeats (hết thời hạn giữ chỗ) (-->) | Nguồn-->Đích |
| CL09 | O03 | O10 | Link | 3.1.10: // recordSmsNotSent (mã vé chưa gửi được) (-->) | Nguồn-->Đích |
| CL10 | O03 | O11 | Link | 3.1.9: // sendTicketCodesBySms (số điện thoại người đi, mã vé) (-->) | Nguồn-->Đích |
| CL11 | O09 | O07 | Link | 2.1.9.1: // markHeld (thời hạn giữ chỗ) (-->)<br>2.1.10*a.3.1: // markAvailable (-->)<br>3.1.6.1: // markAvailable (-->)<br>3.1.8.2: // markSold (-->)<br>4.1.1: // markAvailable (-->) | Nguồn-->Đích |
| CL12 | O09 | O10 | Link | 3.1.8.1: «create» // createTicket (chuyến, chỗ, họ tên, số điện thoại, giá vé) (-->) | Nguồn-->Đích |
| CL13 | O11 | O12 | Link | 3.1.9.1: // requestSmsSending (số điện thoại, mã vé) (-->) | Nguồn-->Đích |
| CL14 | O03 | O03 | Link | 2.1.10: // startWaitingForPaymentResult (BR-03)<br>2.1.10*a.2: // stopWaitingForPaymentResult<br>3.1.5: // stopWaitingForPaymentResult<br>4: // after(BR-03) handleHoldExpiry | Tự gọi |
| CL15 | O10 | O10 | Link | 3.1.8.1.1: // generateTicketCode (BR-04) | Tự gọi |

## F8. VOPC (View Of Participating Classes)

File diagrams/P07-class-UC-009.drawio (một trang).

a) Bảng Node (lớp)

| ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-BookTicketOnlineForm | Class | BookTicketOnlineForm | boundary | - | selectedSeats<br>travelerName<br>travelerPhone<br>issuedTickets<br>totalAmount | // requestBookTicket<br>// selectSeats<br>// enterTravelerInfo<br>// cancelBooking<br>// notifyNoTripSelected<br>// notifySeatsUnavailable<br>// notifySeatLimitExceeded<br>// notifyTripDeparted<br>// notifyTravelerInfoMissing<br>// notifyPaymentFailed<br>// notifyHoldExpired<br>// notifyBookingCancelled<br>// showIssuedTickets |
| AC-B-SmsGateway | Class | SmsGateway | boundary | - | recipientPhone<br>ticketCodes | // sendTicketCodesBySms |
| AC-C-BookTicketOnlineController | Class | BookTicketOnlineController | control | - | - | // startBookTicketOnline<br>// processSeatSelection<br>// processTravelerInfo<br>// requestCancelBooking<br>// startWaitingForPaymentResult<br>// stopWaitingForPaymentResult<br>// handleHoldExpiry |
| AC-C-SearchTripsController | Class | SearchTripsController | control | - | - | // searchTrips |
| AC-C-PayTicketOnlineController | Class | PayTicketOnlineController | control | - | - | // payTicketOnline<br>// cancelPayment |
| AC-E-Trip | Class | Trip | entity | - | departureTime<br>route<br>vehicleType | // checkDepartureNotReached |
| AC-E-Seat | Class | Seat | entity | - | seatCode<br>tripState | // checkAvailable<br>// markHeld<br>// markSold<br>// markAvailable |
| AC-E-Fare | Class | Fare | entity | - | route<br>vehicleType<br>amount<br>surchargePercent | // determineFare |
| AC-E-Booking | Class | Booking | entity | - | trip<br>seatCodes<br>status<br>holdStartedAt<br>holdExpiry<br>travelerName<br>travelerPhone<br>seatFare | // createBooking<br>// checkSeatCountWithinLimit<br>// holdSeats<br>// recordTravelerInfo<br>// calculateTotalAmount<br>// releaseHeldSeats<br>// issueTickets |
| AC-E-Ticket | Class | Ticket | entity | - | ticketCode<br>travelerName<br>travelerPhone<br>fare<br>purchaseChannel<br>status<br>smsStatus | // createTicket<br>// generateTicketCode<br>// recordSmsNotSent |

b) Bảng quan hệ (bảng Edge)

| ID | Lớp A | Lớp B | Loại (Association / Aggregation / Composition / Generalization / Dependency) | Multiplicity | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC009-01 | BookTicketOnlineForm | BookTicketOnlineController | Association | - | - | Link CL02 (1.1, 2.1, 3.1 và các message hiển thị); tạm thời |
| R-UC009-02 | BookTicketOnlineController | SearchTripsController | Dependency | - | - | Link CL03 (1.1.1, bước 2, include UC-008); tạm thời |
| R-UC009-03 | BookTicketOnlineController | PayTicketOnlineController | Dependency | - | - | Link CL04 (3.1.4, 4.2, bước 8, include UC-010); tạm thời |
| R-UC009-04 | BookTicketOnlineController | Trip | Association | - | - | Link CL05 (2.1.4, bước 4); tạm thời |
| R-UC009-05 | BookTicketOnlineController | Seat | Association | - | - | Link CL06 (2.1.2, bước 4); tạm thời |
| R-UC009-06 | BookTicketOnlineController | Fare | Association | - | - | Link CL07 (2.1.8, bước 5, ASM-40); tạm thời |
| R-UC009-07 | BookTicketOnlineController | Booking | Association | - | - | Link CL08 (2.1.1, 2.1.3, 2.1.9, 3.1.1, 3.1.3, 3.1.6, 3.1.8, 4.1, 2.1.10*a.3); tạm thời |
| R-UC009-08 | BookTicketOnlineController | Ticket | Association | - | - | Link CL09 (3.1.10, bước 11a, ASM-39); tạm thời |
| R-UC009-09 | BookTicketOnlineController | SmsGateway | Association | - | - | Link CL10 (3.1.9, bước 10); tạm thời |
| R-UC009-10 | Booking | Seat | Association | A ? - B 1..5 | - | Link CL11 (2.1.9.1, 3.1.6.1, 3.1.8.2, 4.1.1, 2.1.10*a.3.1); GL-12 "Nhóm các chỗ", BR-01 (tối đa 5 chỗ mỗi lần đặt) |
| R-UC009-11 | Booking | Ticket | Association | A ? - B 0..5 | - | Link CL12 (3.1.8.1, bước 9); BR-01, BR-04 (mỗi chỗ một vé, tối đa 5 chỗ); lần đặt chưa thanh toán thành công không có vé |
| R-UC009-12 | Booking | Trip | Association | A 0..* - B 1 | - | Bằng chứng từ đặc tả: GL-12 "Nhóm các chỗ của một chuyến xe", bước 3 và bước 4 (không có link trong F7) |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1, 1.1 | ACT-01, AC-B-BookTicketOnlineForm, AC-C-BookTicketOnlineController |
| 2 | 1.1.1, 1.1.1 (trả về) | AC-C-BookTicketOnlineController, AC-C-SearchTripsController |
| 2a | 1.1.2 | AC-C-BookTicketOnlineController, AC-B-BookTicketOnlineForm |
| 3 | 2, 2.1 | ACT-01, AC-B-BookTicketOnlineForm, AC-C-BookTicketOnlineController |
| 4 | 2.1.1, 2.1.2, 2.1.2 (trả về), 2.1.3, 2.1.3 (trả về), 2.1.4, 2.1.4 (trả về) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Seat, AC-E-Trip |
| 4a | 2.1.5 | AC-C-BookTicketOnlineController, AC-B-BookTicketOnlineForm |
| 4b | 2.1.6 | AC-C-BookTicketOnlineController, AC-B-BookTicketOnlineForm |
| 4c | 2.1.7 | AC-C-BookTicketOnlineController, AC-B-BookTicketOnlineForm |
| 5 | 2.1.8, 2.1.8 (trả về), 2.1.9, 2.1.9.1, 2.1.10 | AC-C-BookTicketOnlineController, AC-E-Fare, AC-E-Booking, AC-E-Seat |
| 5a | 4, 4.1, 4.1.1, 4.2, 4.3 | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Seat, AC-C-PayTicketOnlineController, AC-B-BookTicketOnlineForm |
| 6 | 3, 3.1 | ACT-01, AC-B-BookTicketOnlineForm, AC-C-BookTicketOnlineController |
| 7 | 3.1.1, 3.1.1 (trả về) | AC-C-BookTicketOnlineController, AC-E-Booking |
| 7a | 3.1.2 | AC-C-BookTicketOnlineController, AC-B-BookTicketOnlineForm |
| 8 | 3.1.3, 3.1.3 (trả về), 3.1.4, 3.1.4 (trả về), 3.1.5 | AC-C-BookTicketOnlineController, AC-E-Booking, AC-C-PayTicketOnlineController |
| 8a | 3.1.6, 3.1.6.1, 3.1.7 | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Seat, AC-B-BookTicketOnlineForm |
| 9 | 3.1.8, 3.1.8.1, 3.1.8.1.1, 3.1.8.2, 3.1.8 (trả về) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Ticket, AC-E-Seat |
| 10 | 3.1.9, 3.1.9.1 | AC-C-BookTicketOnlineController, AC-B-SmsGateway, ACT-07 |
| 11 | 3.1.9.1 (trả về), 3.1.9 (trả về) | ACT-07, AC-B-SmsGateway, AC-C-BookTicketOnlineController |
| 11a | 3.1.10 | AC-C-BookTicketOnlineController, AC-E-Ticket |
| 12 | 3.1.11 | AC-C-BookTicketOnlineController, AC-B-BookTicketOnlineForm |
| *a | 2.1.10*a, 2.1.10*a.1, 2.1.10*a.2, 2.1.10*a.3, 2.1.10*a.3.1, 2.1.10*a.4 | ACT-01, AC-B-BookTicketOnlineForm, AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Seat |

## F10. File .drawio

Ba file trong diagrams/: P07-sequence-UC-009.drawio (bốn trang SD1a, SD1b, SD1c, SD2), P07-communication-UC-009.drawio (một trang), P07-class-UC-009.drawio (một trang). ID cell trùng ID trong các bảng ở F5, F7, F8; toạ độ là bội số của 10.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-55 | Việc ghi nhận "mã vé chưa gửi được qua SMS" lưu những gì và để ai dùng xử lý tiếp? (Chỉ đánh dấu trạng thái gửi SMS trên từng vé / Lưu thêm bản ghi riêng cho từng lần gửi thất bại để nhân viên xử lý gửi lại) | AC-E-Ticket (smsStatus, recordSmsNotSent), luồng 11a, hậu điều kiện thành công, ASM-39 | UC-009 luồng 11a: "Ghi nhận mã vé chưa gửi được qua SMS" không nêu ghi nhận ở đâu và dùng vào việc gì |
| Q-56 | Giá vé của lần đặt được xác định tại thời điểm nào và có đổi không khi giá vé hoặc mức tăng giá thay đổi giữa lúc giữ chỗ và lúc thanh toán? (Cố định từ lúc giữ chỗ / Tính lại lúc thanh toán / Tính lúc phát hành vé) | AC-E-Fare (determineFare), AC-E-Booking (calculateTotalAmount), AC-E-Ticket (fare), bước 5, 8, 9, ASM-40 | UC-009 mục 8: "Giá vé do UC-023 ... và UC-024 ... cung cấp" không nêu thời điểm lấy giá |
| Q-57 | Khi thời hạn giữ chỗ hết trong lúc hành khách đang thanh toán ở UC-010 (bước 8), UC-009 có yêu cầu UC-010 dừng phiên thanh toán đó không? (Có, dừng phiên thanh toán ngay / Không, để UC-010 tự kết thúc rồi xử lý giao dịch đến muộn theo BR-06) | AC-C-PayTicketOnlineController (cancelPayment), luồng 5a, message 4.2, ASM-41 | UC-009 luồng 5a: hết thời hạn "tại bất kỳ bước nào từ bước 6 đến bước 8" không nêu hành vi của UC-010 đang chạy; mục 8 chỉ nêu giao dịch đến sau khi UC-009 đã kết thúc |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-39 | Mã vé chưa gửi được qua SMS được ghi nhận bằng thuộc tính trạng thái gửi SMS (Chưa gửi được) trên từng vé liên quan; không có bản ghi riêng. | Chờ Q-55. Luồng 11a chỉ nêu ghi nhận mà không nêu nơi ghi; chọn dấu trên vé vì mã vé thuộc về vé và không thêm khái niệm ngoài P05 | AC-E-Ticket (smsStatus, recordSmsNotSent); message 3.1.10; luồng 11a |
| ASM-40 | Giá vé của từng chỗ được xác định một lần tại bước 5 khi giữ chỗ và ghi vào lần đặt; tổng tiền ở bước 8, giá trên vé ở bước 9 và giá hiển thị ở bước 12 dùng giá đã ghi này. | Chờ Q-56. P04 không nêu thời điểm lấy giá vé; chọn lúc giữ chỗ để số tiền hành khách thanh toán không đổi trong thời hạn giữ chỗ | AC-E-Fare (determineFare), AC-E-Booking (seatFare, calculateTotalAmount); message 2.1.8, 3.1.3, 3.1.8.1 |
| ASM-41 | Khi hết thời hạn giữ chỗ (luồng 5a) mà UC-010 còn đang chạy, control của UC-009 yêu cầu control của UC-010 dừng phiên thanh toán của lần đặt này; giao dịch thanh toán thành công đến sau xử lý theo BR-06. | Chờ Q-57. Luồng 5a vẽ hết hạn ở bất kỳ bước nào từ 6 đến 8 nhưng không nêu hành vi của UC-010 đang chạy; chọn dừng phiên để phiên thanh toán không còn chạy khi chỗ đã trả cho người khác | AC-C-PayTicketOnlineController (cancelPayment); message 4.2; luồng 5a |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-009 (luồng 5a, Mục 8) | Luồng 5a hết hạn ở bước 6 đến 8 không nêu hành vi với UC-010 đang chạy (Q-57, ASM-41) | Thêm vào hành động của luồng 5a việc yêu cầu UC-010 dừng phiên thanh toán nếu còn đang chạy, hoặc ghi rõ không cần theo câu trả lời Q-57 |
| P04 | UC-009 (luồng 11a, hậu điều kiện thành công) | Nơi ghi nhận "mã vé chưa gửi được qua SMS" không nêu (Q-55, ASM-39) | Nêu dữ liệu ghi nhận ở luồng 11a (trạng thái gửi SMS của vé) theo câu trả lời Q-55 |
| P04 | UC-009 (bước 5, bước 8, Mục 8) | Không nêu thời điểm xác định giá vé và bước tính tổng tiền trước khi gọi UC-010 (Q-56, ASM-40) | Thêm việc xác định giá vé của từng chỗ vào bước 5 (hoặc bước 8) và nêu tổng tiền chuyển cho UC-010 ở bước 8 |

## Vấn đề còn mở

- UC-008 và UC-010 chưa có đặc tả P04 và chưa có P07. Đã đặt trước control tạm AC-C-SearchTripsController (trách nhiệm // searchTrips) và AC-C-PayTicketOnlineController (// payTicketOnline, // cancelPayment); P07 của hai use case phải dùng đúng mã và tên này. Kết cục của hai use case (chọn được hay chưa chọn chuyến; thanh toán thành công hay thất bại) lấy theo P04 UC-009 mục 8, cần khớp khi đặc tả hai use case đó.
- Khái niệm do use case khác quản lý và chưa có P07 (A1): AC-E-Trip (chủ sở hữu UC-016 Lập lịch chạy tuần), AC-E-Seat (UC-021 Quản lý danh mục xe, sơ đồ chỗ), AC-E-Fare (UC-023 Đặt giá vé, UC-024 Đặt mức tăng giá ngày lễ). P07 của các use case đó phải dùng lại các mã này. AC-B-SmsGateway cũng được UC-003, UC-014, UC-017 dùng.
- Trạng thái của chỗ trên một chuyến (Trống, Đang giữ, Đã bán) được đặt làm thuộc tính tripState của Seat. P05 GL-01 định nghĩa Chỗ là vị trí trên sơ đồ chỗ của loại xe, còn trạng thái theo từng chuyến chưa có thuật ngữ riêng; P08 xét có tách "chỗ của chuyến" khỏi vị trí trên sơ đồ chỗ hay không.
- NFR-04 (chỉ một yêu cầu giữ được chỗ): việc kiểm tra ở bước 4 và giữ chỗ ở bước 5 là hai message; thất bại của Seat // markHeld do tranh chấp được coi như luồng 4a (NFR-04, BR-02) và không vẽ nhánh riêng. Cách bảo đảm không trùng chỗ là quyết định thiết kế của P12.
- Liên kết giữa vé và giao dịch thanh toán (GL-06) không có trong P04 UC-009 và GL-23 không liệt kê giao dịch trong thành phần của vé. UC-009 chỉ nhận kết quả thành công hoặc thất bại từ UC-010 nên Ticket không có thuộc tính giao dịch. Các use case hoàn tiền (UC-012, UC-017) cần biết giao dịch của vé; P07 của UC-010 và P08 xét quan hệ này.
- Booking được tạo ở bước 4 (trạng thái Đang chọn) trước khi kiểm tra để Booking kiểm tra BR-01; ở các luồng 4a, 4b, 4c lần đặt bị bỏ và chỉ lưu từ bước 5 (khi giữ chỗ). P08 và P12 quyết định thời điểm lưu.
- Mốc thời gian (A2): UC-007 (60 phút trước giờ xuất bến, trên vé đặt qua điện thoại) và UC-025 (15 phút trước giờ xuất bến, danh sách hành khách) tính mốc từ giờ xuất bến của Trip. UC-009 chỉ thêm Ticket vào chuyến, không tạo, đổi hay huỷ Trip nên không có message hẹn mốc; vé phát hành sau mốc của UC-025 chờ Q-29 ở UC-025.
- Luồng *a (hành khách huỷ ở bất kỳ bước nào trước bước 8) vẽ ở trang SD2 tại một điểm rẽ đại diện sau message 2.1.10 (sau khi giữ chỗ), với opt [đã giữ chỗ] cho trường hợp huỷ trước khi giữ chỗ. Huỷ khi đang ở bên trong UC-008 (bước 2) thuộc boundary của UC-008.
- Trách nhiệm // stopWaitingForPaymentResult dùng cho hai sự kiện kết thúc chờ (có kết quả thanh toán ở bước 8; use case kết thúc do huỷ ở *a) vì cùng ý nghĩa dừng bộ đếm thời hạn giữ chỗ.
- Bố cục ba file .drawio sinh từ bảng mô hình và đã kiểm tra tự động (XML hợp lệ, toạ độ bội số của 10, node không chồng nhau, khoảng cách tối thiểu 40, link communication và cạnh VOPC không cắt node). Chưa mở bằng draw.io để xem bằng mắt; nhãn dài trên link CL02, CL08 của communication diagram có thể cần chỉnh vị trí.
