# P07 - Phân tích use case UC-002 Đặt vé trực tuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P04-uc-specs/UC-002-book-ticket-online.md 1.0; P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P02-usecases.md 1.1. Chưa có file P07 nào trước lần chạy này; chưa có đặc tả P04 của UC-003 (use case được include) |
| Phạm vi | UC-002 |

Quy ước trích nguồn: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md; "Dữ liệu vào n", "Dữ liệu ra n" chỉ bảng dữ liệu của P04 UC-002. Tham số bước: LUONG_CAN_VE = Không có (vẽ mọi luồng); YEU_CAU_BO_SUNG = Không có.

## 1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-002 Đặt vé trực tuyến (Book Ticket Online) |
| Tác nhân chính (ACT, loại) | ACT-01 Hành khách (Người) |
| Tác nhân phụ (ACT, loại) | ACT-07 Cổng SMS (Hệ thống ngoài). ACT-06 Cổng thanh toán (Hệ thống ngoài) chỉ tham gia trong UC-003 (RL-04), không tương tác trực tiếp với UC-002 |
| Include (UC) | UC-003 Thanh toán vé trực tuyến, tại bước 10 (RL-27) |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2 không có điểm mở rộng của UC-002) |
| Tác nhân thời gian | ACT-10 Bộ định thời không kích hoạt UC-002. Hết thời hạn giữ chỗ 10 phút (EV-03, BR-07) là thời hạn nội bộ của UC-002, không là tác nhân |
| File P07 đã có được dùng làm sổ đăng ký AC | Không có file nào, sổ AC rỗng. Mã tạm đặt trước cho use case được include: AC-C-PayTicketOnlineController, trạng thái "Tạm - chờ P07 của UC-003" |

## 2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Hành khách | Yêu cầu đặt vé và cung cấp điểm đi, điểm đến, ngày đi (xem Dữ liệu vào 1). | Không đổi | Dữ liệu vào 1; REQ-05 |
| 2 | Hệ thống | Hiển thị các chuyến khớp điểm đi, điểm đến và ngày đi (xem Dữ liệu ra 1). | Hệ thống lấy các chuyến có tuyến khớp điểm đi, điểm đến và có ngày xuất bến là ngày đi đã cung cấp. Mỗi chuyến kèm số chỗ còn trống theo BR-03 và giá một vé tính từ giá theo tuyến và loại xe cùng mức tăng giá lễ Tết áp dụng cho ngày xuất bến (BR-04, BR-05). Hệ thống hiển thị danh sách chuyến cho hành khách. | BR-03, BR-04, BR-05; GL-04, GL-09, GL-25, GL-36; REQ-05 |
| 2a | Hệ thống | Điều kiện: không có chuyến nào khớp điểm đi, điểm đến và ngày đi. Thông báo không có chuyến phù hợp với tiêu chí đã cung cấp (ASM-16). Quay lại bước 1. | Hệ thống xác định không có chuyến nào khớp tiêu chí và thông báo cho hành khách để cung cấp lại tiêu chí. | ASM-16 |
| 3 | Hành khách | Chọn một chuyến. | Không đổi | - |
| 4 | Hệ thống | Hiển thị sơ đồ chỗ của chuyến với các chỗ còn trống (BR-03) (xem Dữ liệu ra 2). | Hệ thống lấy các chỗ của chuyến đã chọn theo sơ đồ xe của chuyến và xác định từng chỗ còn trống hay không còn trống theo BR-03. Hệ thống hiển thị sơ đồ chỗ với trạng thái từng chỗ. | BR-03; GL-02, GL-03, GL-31 |
| 4a | Hệ thống | Điều kiện: chuyến đã chọn không còn chỗ trống nào (BR-03). Thông báo chuyến đã hết chỗ trống. Quay lại bước 3. | Hệ thống xác định mọi chỗ của chuyến đều không còn trống và thông báo cho hành khách chọn chuyến khác. | BR-03 |
| 5 | Hành khách | Chọn các chỗ muốn đặt và cung cấp họ tên, số điện thoại của người đi cho từng chỗ (xem Dữ liệu vào 2). | Không đổi | Dữ liệu vào 2; ASM-13 |
| 6 | Hệ thống | Kiểm tra số chỗ đã chọn không vượt quá giới hạn của một lần đặt (BR-01) và mọi chỗ đã chọn còn trống (BR-02, BR-03). | Hệ thống lập lần đặt gồm các chỗ đã chọn của chuyến và thông tin người đi, rồi kiểm tra số chỗ của lần đặt không quá 5 (BR-01). Hệ thống kiểm tra từng chỗ đã chọn của chuyến còn trống theo BR-03 để không có hai vé cùng một chỗ (BR-02). | BR-01, BR-02, BR-03; GL-18 |
| 6a | Hệ thống | Điều kiện: số chỗ đã chọn lớn hơn 5 (BR-01). Từ chối yêu cầu đặt vé và thông báo quy tắc bị vi phạm (BR-01). Quay lại bước 5. | Hệ thống phát hiện số chỗ của lần đặt vượt giới hạn, từ chối yêu cầu và thông báo quy tắc BR-01. | BR-01 |
| 6b | Hệ thống | Điều kiện: số chỗ không lớn hơn 5 và có ít nhất một chỗ không còn trống (BR-03). Từ chối yêu cầu đặt vé và thông báo các chỗ không còn trống (BR-02). Quay lại bước 4. | Hệ thống phát hiện ít nhất một chỗ đã chọn không còn trống, từ chối yêu cầu và thông báo các chỗ không còn trống. | BR-02, BR-03 |
| 7 | Hệ thống | Kiểm tra họ tên và số điện thoại người đi đã được cung cấp cho mọi chỗ đã chọn và số điện thoại đúng định dạng (ASM-15). | Hệ thống kiểm tra từng chỗ của lần đặt có họ tên người đi không để trống và số điện thoại người đi có 10 chữ số, bắt đầu bằng 0 (ASM-15). Việc kiểm tra thực hiện sau bước 6 để giữ thứ tự báo lỗi hiện dùng (Q-34). | ASM-13, ASM-15; GL-26; Q-34 |
| 7a | Hệ thống | Điều kiện: thiếu họ tên hoặc số điện thoại người đi của ít nhất một chỗ đã chọn. Từ chối yêu cầu đặt vé và nhắc hành khách cung cấp đủ họ tên, số điện thoại người đi cho từng chỗ. Quay lại bước 5. | Hệ thống phát hiện ít nhất một chỗ thiếu họ tên hoặc số điện thoại người đi, từ chối yêu cầu và nhắc cung cấp đủ. | ASM-13 |
| 7b | Hệ thống | Điều kiện: thông tin người đi đủ cho mọi chỗ và có ít nhất một số điện thoại không đúng định dạng (ASM-15). Từ chối yêu cầu đặt vé và thông báo số điện thoại không đúng định dạng. Quay lại bước 5. | Hệ thống phát hiện ít nhất một số điện thoại người đi không đúng định dạng, từ chối yêu cầu và thông báo. | ASM-15 |
| 8 | Hệ thống | Tính giá vé của từng chỗ đã chọn (BR-04, BR-05) và tổng tiền của lần đặt (BR-06). | Với mỗi chỗ, hệ thống tính giá một vé bằng giá theo tuyến và loại xe của chuyến nhân với (1 + mức tăng giá lễ Tết áp dụng cho ngày xuất bến) (BR-05). Lần đặt giữ tổng tiền bằng tổng giá vé của các chỗ (BR-06). | BR-04, BR-05, BR-06; GL-08, GL-09, GL-25 |
| 9 | Hệ thống | Giữ các chỗ đã chọn cho lần đặt và chờ hành khách thanh toán thành công trong thời hạn giữ chỗ (BR-07). | Hệ thống chuyển từng chỗ của lần đặt sang trạng thái đang giữ cho lần đặt đó và ghi nhận thời điểm bắt đầu giữ. Control bắt đầu chờ thanh toán trong 10 phút (BR-07); chỗ đang giữ không còn trống với người khác (BR-03). | BR-03, BR-07; GL-11 |
| 9a | Hệ thống | Điều kiện: hết thời hạn giữ chỗ (BR-07) mà thanh toán chưa thành công. Hết thời hạn giữ chỗ. | Control nhận sự kiện hết thời hạn giữ chỗ 10 phút bằng message tự gọi after(BR-07) khi thanh toán chưa thành công, rồi tiến hành trả chỗ và thông báo. | BR-07; EV-03 |
| 9a1 | Hệ thống | Trả các chỗ đang giữ của lần đặt về trạng thái còn trống cho hành khách khác chọn (BR-08). | Lần đặt yêu cầu từng chỗ đang giữ của nó chuyển về trạng thái còn trống để người khác chọn (BR-08). | BR-08 |
| 9a2 | Hệ thống | Thông báo hành khách đã hết thời hạn giữ chỗ và lần đặt vé không thành công. Kết thúc use case (thất bại). | Hệ thống thông báo cho hành khách hết thời hạn giữ chỗ và lần đặt không thành công, rồi kết thúc use case; không vé nào được phát hành. | BR-07, BR-08 |
| 10 | Hệ thống | Gọi use case UC-003 Thanh toán vé trực tuyến để hành khách thanh toán tổng tiền của lần đặt. | Control chuyển tổng tiền của lần đặt cho control của UC-003 Thanh toán vé trực tuyến và nhận kết quả thanh toán thành công hoặc không thành công. Việc làm việc với cổng thanh toán thuộc phân tích của UC-003. | BR-06; RL-27; GL-17 |
| 10a | Hệ thống | Điều kiện: UC-003 trả kết quả thanh toán không thành công trong thời hạn giữ chỗ (BR-07). Thông báo thanh toán không thành công và các chỗ vẫn được giữ tới hết thời hạn giữ chỗ (BR-07, ASM-14). Quay lại bước 10. | Hệ thống nhận kết quả không thành công khi chưa hết thời hạn giữ chỗ, thông báo cho hành khách và giữ nguyên các chỗ. Control gọi lại UC-003 cho tới khi thanh toán thành công hoặc hết thời hạn giữ chỗ. | BR-07, ASM-14; Q-31 |
| 11 | Hệ thống | Phát hành vé cho các chỗ đang giữ, mỗi chỗ một vé có một mã vé (BR-09, BR-10). | Khi thanh toán thành công, lần đặt tạo một vé cho mỗi chỗ đang giữ, mỗi vé có mã vé duy nhất trên toàn hệ thống (BR-10). Mỗi vé ghi họ tên, số điện thoại người đi, giá vé của chỗ và ở trạng thái đã phát hành (BR-09). | BR-09, BR-10; GL-22, GL-37 |
| 12 | Hệ thống | Gửi vé của từng chỗ qua SMS tới số điện thoại người đi của chỗ đó qua Cổng SMS (xem Dữ liệu ra 3). | Với mỗi vé, hệ thống lập nội dung gồm mã vé, tuyến, giờ xuất bến, chỗ, họ tên người đi (ASM-17), lấy tuyến và giờ xuất bến từ chuyến của vé. Hệ thống gửi nội dung đó cùng số điện thoại người đi của vé tới Cổng SMS (ASM-13). | ASM-13, ASM-17; GL-30; REQ-19, REQ-20 |
| 13 | Hệ thống | Hiển thị các vé đã phát hành cho hành khách (xem Dữ liệu ra 4). | Hệ thống lấy các vé vừa phát hành của lần đặt kèm giá từng vé và tổng tiền, rồi hiển thị cho hành khách (ASM-17). | ASM-17; BR-06; Dữ liệu ra 4 |

## 3. Tìm lớp phân tích

### 3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-01 Hành khách | Người | BookTicketForm (AC-B-BookTicketForm) | Giao diện người dùng | Mới | Một boundary cho cặp (ACT-01, UC-002) gom mọi tương tác của hành khách: nhập tiêu chí, chọn chuyến, chọn chỗ và nhập thông tin người đi, nhận thông báo và vé hiển thị. Tên theo hành động của use case với hậu tố Form (HAU_TO_TEN_LOP là Mặc định) |
| ACT-07 Cổng SMS | Hệ thống ngoài | SmsGateway (AC-B-SmsGateway) | Giao diện hệ thống | Mới | Boundary đặt tên theo hệ thống, không hậu tố (HAU_TO_TEN_LOP là Mặc định); không trùng tên entity nào nên không cần hậu tố Gateway bắt buộc. Tái dùng được ở UC-013 (gửi SMS báo huỷ chuyến) với cùng mã |

Tác nhân ACT-06 Cổng thanh toán chỉ xuất hiện trong phần hành vi của UC-003 được include nên boundary của nó thuộc P07 của UC-003. Tác nhân thời gian ACT-10 không tham gia UC-002.

### 3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Hành khách | Bước 1, 3, 5, 13; mô tả | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01, có boundary BookTicketForm |
| 2 | Hệ thống | Mọi bước hệ thống | Loại - mơ hồ | Chỉ là chủ ngữ của bước, không chỉ một khái niệm dữ liệu cụ thể |
| 3 | Yêu cầu đặt vé | Bước 1, 6a, 7a, 7b | Loại - thao tác hoặc sự kiện | Là hành động của hành khách (requestBooking) |
| 4 | Điểm đi | Bước 1; Dữ liệu vào 1 #1 | Loại - thuộc tính của Route | GL-36 ghi điểm đi là thành phần dữ liệu của Tuyến |
| 5 | Điểm đến | Bước 1; Dữ liệu vào 1 #2 | Loại - thuộc tính của Route | GL-36 ghi điểm đến là thành phần dữ liệu của Tuyến |
| 6 | Ngày đi (ngày xuất bến) | Bước 1, 2; Dữ liệu vào 1 #3; BR-05 | Loại - thuộc tính của Trip | Thành phần ngày của GL-10 Giờ xuất bến (departureTime) |
| 7 | Tiêu chí | Bước 2a | Loại - trùng hoặc đồng nghĩa với điểm đi, điểm đến, ngày đi | Gọi chung ba trường của Dữ liệu vào 1 |
| 8 | Tuyến | Bước 2; Dữ liệu ra 1 #1; BR-04, BR-05 | Entity (AC-E-Route) | GL-36; hệ thống quản lý 12 tuyến vượt quá một lần thực hiện và Route có hành vi kiểm tra khớp điểm đi, điểm đến |
| 9 | Chuyến (chuyến đang mở bán) | Bước 2, 3, 4, 6, 8; BR-02..BR-06; Tiền điều kiện | Entity (AC-E-Trip) | GL-04; hệ thống lưu chuyến, tìm chuyến khớp, cung cấp chỗ và tính giá vé |
| 10 | Danh sách chuyến (các chuyến khớp) | Bước 2; Dữ liệu ra 1 | Loại - cấu trúc cài đặt | Là tập kết quả của việc tìm trên Trip theo tiêu chí |
| 11 | Giờ xuất bến | Dữ liệu ra 1 #2; Dữ liệu ra 3 #3 | Loại - thuộc tính của Trip | GL-10 |
| 12 | Loại xe | Dữ liệu ra 1 #3; BR-04 | Loại - thuộc tính của Trip | GL-21 là giá trị Giường nằm 40 chỗ, Ghế ngồi 29 chỗ, không có hành vi riêng; BaseFare tra theo giá trị này |
| 13 | Xe | Dữ liệu ra 2 #1 ("sơ đồ chỗ của xe") | Loại - không tham gia hành vi của use case này (khái niệm của UC-012) | Xe chỉ được nhắc để xác định sơ đồ chỗ và loại xe; UC-002 không đọc hay ghi xe (ASM-42); UC-012 xếp xe vào chuyến |
| 14 | Sơ đồ chỗ | Bước 4; Dữ liệu ra 2 | Loại - cấu trúc cài đặt | GL-31 là kết quả hiển thị các chỗ của chuyến kèm trạng thái, lấy từ Seat |
| 15 | Chỗ | Bước 4, 5, 6, 9, 11; BR-02, BR-03 | Entity (AC-E-Seat) | GL-02; có trạng thái đổi trong use case (giữ, trả) và hành vi xác định còn trống theo BR-03 |
| 16 | Mã chỗ | Dữ liệu vào 2 #1; Dữ liệu ra 2 #1; Dữ liệu ra 3 #4 | Loại - thuộc tính của Seat | seatCode |
| 17 | Chỗ còn trống, trạng thái chỗ | Bước 4, 4a, 6; BR-03; Dữ liệu ra 2 #2 | Loại - thuộc tính của Seat | status của Seat, suy ra theo BR-03 |
| 18 | Số chỗ còn trống | Dữ liệu ra 1 #4 | Loại - thuộc tính của Trip | availableSeatCount, giá trị suy ra từ trạng thái các chỗ của chuyến |
| 19 | Số chỗ đã chọn, giới hạn 5 chỗ | Bước 6, 6a; BR-01; Dữ liệu vào 2 #1 | Loại - tham số của quy tắc BR-01 | Hằng số 5 nằm trong quy tắc |
| 20 | Giữ chỗ, chỗ đang giữ | Bước 9, 9a1; BR-03, BR-07, BR-08 | Loại - thuộc tính của Seat | GL-11 là trạng thái tạm thời của chỗ (status của Seat); thời điểm bắt đầu giữ là thuộc tính của Booking |
| 21 | Thời hạn giữ chỗ (10 phút) | Bước 9, 9a; BR-07 | Loại - tham số của quy tắc BR-07 | Hằng số 10 phút nằm trong quy tắc |
| 22 | Lần đặt | Bước 6, 8, 9, 11; BR-01, BR-06, BR-07, BR-08; Dữ liệu ra 4 | Entity (AC-E-Booking) | GL-18; hệ thống lưu lần đặt cùng chỗ, tổng tiền, thời điểm giữ và có hành vi kiểm tra, tính tổng, giữ, trả chỗ, phát hành vé |
| 23 | Tổng tiền | Bước 8; BR-06; Dữ liệu ra 4 #7 | Loại - thuộc tính của Booking | totalAmount; GL-18 ghi tổng tiền là thành phần của Lần đặt |
| 24 | Thời điểm bắt đầu giữ | Bước 9; BR-07 | Loại - thuộc tính của Booking | holdStartTime |
| 25 | Họ tên người đi | Bước 5, 7; Dữ liệu vào 2 #2; Dữ liệu ra 3 #5; Dữ liệu ra 4 #3 | Loại - thuộc tính của Ticket | travelerName; trước khi có vé, Booking giữ theo ASM-43 |
| 26 | Số điện thoại người đi | Bước 5, 7, 12; Dữ liệu vào 2 #3; Dữ liệu ra 4 #4 | Loại - thuộc tính của Ticket | travelerPhone; trước khi có vé, Booking giữ theo ASM-43 |
| 27 | Thông tin người đi | Bước 7, 7a | Loại - trùng hoặc đồng nghĩa với họ tên người đi, số điện thoại người đi | Gọi chung hai trường của Dữ liệu vào 2 |
| 28 | Người đi | Bước 5, 12; Dữ liệu vào 2 | Loại - là tác nhân hoặc ngoài phạm vi | GL-26 là bên liên quan SH-03, không là tác nhân; thông tin về người đi chỉ gồm họ tên, số điện thoại là thuộc tính của Ticket, không có hồ sơ riêng |
| 29 | Định dạng số điện thoại, điều kiện hợp lệ | Bước 7, 7b; Dữ liệu vào 2 #3 | Loại - tham số của quy tắc ASM-15 | 10 chữ số, bắt đầu bằng 0 nằm trong giả định ASM-15, không có BR |
| 30 | Giá vé (giá một vé) | Bước 8; BR-05; Dữ liệu ra 1 #5; Dữ liệu ra 4 #5 | Loại - thuộc tính của Ticket | price; GL-08; giá do Trip xác định từ BaseFare và HolidaySurcharge |
| 31 | Giá vé theo tuyến và loại xe | Bước 8; BR-04, BR-05; Tiền điều kiện | Entity (AC-E-BaseFare) | GL-09; dữ liệu do quản lý đặt (UC-016), hệ thống lưu vượt một lần thực hiện và BaseFare tính giá một vé theo BR-05 |
| 32 | Mức tăng giá lễ Tết, khoảng ngày tăng giá | Bước 8; BR-05 | Entity (AC-E-HolidaySurcharge) | GL-25; dữ liệu do quản lý đặt (UC-017), hệ thống lưu vượt một lần thực hiện và HolidaySurcharge xác định mức tăng theo ngày xuất bến |
| 33 | Ngày hiện tại | Dữ liệu vào 1 #3 | Loại - tham số của quy tắc ASM-15 | Mốc so sánh của điều kiện ngày đi; không có bước hay luồng kiểm tra (xem Đề xuất sửa artifact trước) |
| 34 | Vé | Bước 11, 12, 13; BR-02, BR-09, BR-10 | Entity (AC-E-Ticket) | GL-37; hệ thống lưu vé, cấp mã duy nhất, lập nội dung SMS |
| 35 | Mã vé | Bước 11, 12; BR-10; Dữ liệu ra 3 #1; Dữ liệu ra 4 #1 | Loại - thuộc tính của Ticket | ticketCode; GL-22 |
| 36 | Trạng thái vé (đã phát hành) | Hậu điều kiện | Loại - thuộc tính của Ticket | status |
| 37 | Tuyến và giờ xuất bến | Dữ liệu ra 4 #6 | Loại - trùng hoặc đồng nghĩa với tuyến, giờ xuất bến | Gọi chung hai khái niệm đã xét |
| 38 | Khoản thanh toán, thanh toán, kết quả thanh toán | Bước 10, 10a; Hậu điều kiện | Loại - thuộc phân tích của UC-003 | GL-17 do UC-003 tạo và xử lý; UC-002 chỉ nhận kết quả thành công hoặc không thành công |
| 39 | Cổng thanh toán | Hậu điều kiện | Loại - thuộc phân tích của UC-003 | ACT-06 chỉ tương tác trong UC-003 (RL-04) |
| 40 | Cổng SMS | Bước 12 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-07, có boundary SmsGateway |
| 41 | SMS, tin nhắn, nội dung SMS | Bước 12; Dữ liệu ra 3 | Loại - thao tác hoặc sự kiện | GL-30; nội dung được lập khi gửi từ dữ liệu của Ticket và Trip rồi chuyển cho SmsGateway, hệ thống không lưu; là tham số của sendTicketSms (xử lý khi gửi lỗi chờ Q-56) |
| 42 | Tài khoản | Mô tả ngắn ("không bắt buộc có tài khoản") | Loại - không tham gia hành vi của use case này (khái niệm của UC-009, UC-010) | Use case không đọc, ghi hay kiểm tra tài khoản |
| 43 | Thông báo | Bước 2a, 4a, 6a, 6b, 7a, 7b, 9a2, 10a | Loại - thao tác hoặc sự kiện | Là việc hiển thị của boundary (các message show...Notice); nội dung thông điệp thuộc P11a |
| 44 | Quy tắc bị vi phạm | Bước 6a | Loại - mơ hồ | Chỉ BR-01, được ghi ngay trong message tương ứng |

### 3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| BookTicketOnlineController (AC-C-BookTicketOnlineController) | UC-002 Đặt vé trực tuyến | Mới | Một control cho use case, đặt tên theo tên tiếng Anh của use case (Book Ticket Online) với hậu tố Controller (HAU_TO_TEN_LOP là Mặc định). Điều phối trình tự 13 bước, nhận sự kiện hết thời hạn giữ chỗ, không giữ dữ liệu nghiệp vụ lâu dài |
| PayTicketOnlineController (AC-C-PayTicketOnlineController) | UC-003 Thanh toán vé trực tuyến (được include) | Tạm - chờ P07 của UC-003 | Mã và tên đặt trước theo quy tắc F3.3 từ tên Pay Ticket Online của UC-003 trong P02. UC-002 chỉ gửi message tới control này tại bước 10; nội bộ thuộc P07 của UC-003 |

### 3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-BookTicketForm | boundary | BookTicketForm | // requestBooking: nhận yêu cầu đặt vé và tiêu chí tìm chuyến từ hành khách<br>// selectTrip: nhận chuyến hành khách chọn<br>// selectSeatsAndEnterTravelerInfo: nhận chỗ đã chọn và họ tên, số điện thoại người đi của từng chỗ<br>// showTrips: hiển thị các chuyến khớp kèm số chỗ còn trống và giá vé<br>// showSeatMap: hiển thị sơ đồ chỗ với trạng thái từng chỗ<br>// showNoTripFoundNotice: thông báo không có chuyến phù hợp<br>// showNoSeatLeftNotice: thông báo chuyến đã hết chỗ trống<br>// showSeatLimitExceededNotice: thông báo số chỗ vượt giới hạn một lần đặt<br>// showSeatsUnavailableNotice: thông báo các chỗ không còn trống<br>// showMissingTravelerInfoNotice: nhắc cung cấp đủ họ tên, số điện thoại người đi<br>// showInvalidPhoneNotice: thông báo số điện thoại không đúng định dạng<br>// showHoldExpiredNotice: thông báo hết thời hạn giữ chỗ, lần đặt không thành công<br>// showPaymentFailedNotice: thông báo thanh toán không thành công<br>// showIssuedTickets: hiển thị các vé đã phát hành và tổng tiền | departurePoint, arrivalPoint, travelDate, selectedSeats, travelerNames, travelerPhones | 1, 2, 2a, 3, 4, 4a, 5, 6a, 6b, 7a, 7b, 9a2, 10a, 13 | Giao diện người dùng | Mới | - |
| AC-B-SmsGateway | boundary | SmsGateway | // sendTicketSms: gửi nội dung vé tới số điện thoại người đi qua Cổng SMS | recipientPhone, smsContent | 12 | Giao diện hệ thống | Mới | GL-30 |
| AC-C-BookTicketOnlineController | control | BookTicketOnlineController | // searchTrips: điều phối tìm các chuyến khớp tiêu chí<br>// getSeatMap: điều phối lấy sơ đồ chỗ của chuyến đã chọn<br>// submitBooking: điều phối kiểm tra, tính tiền, giữ chỗ, thanh toán, phát hành và gửi vé<br>// startWaitingForPayment: bắt đầu chờ thanh toán trong thời hạn giữ chỗ (BR-07)<br>// handleSeatHoldExpired: xử lý sự kiện hết thời hạn giữ chỗ | - | 1-13, 2a, 4a, 6a, 6b, 7a, 7b, 9a, 9a1, 9a2, 10a | - | Mới | - |
| AC-C-PayTicketOnlineController | control | PayTicketOnlineController | // payTickets: nhận yêu cầu thanh toán tổng tiền của lần đặt từ UC-002 | - | 10 | - | Tạm - chờ P07 của UC-003 | - |
| AC-E-Trip | entity | Trip | // findMatchingTrips: tìm các chuyến có tuyến và ngày xuất bến khớp tiêu chí<br>// getSeatMap: cung cấp các chỗ của chuyến kèm trạng thái<br>// checkSeatsAvailable: kiểm tra mọi chỗ đã chọn của chuyến còn trống<br>// determineTicketPrice: xác định giá một vé của chuyến<br>// getRouteAndDepartureTime: cung cấp tuyến và giờ xuất bến của chuyến | departureTime, busType, availableSeatCount | 2, 4, 6, 8, 12 | - | Mới | GL-04 |
| AC-E-Route | entity | Route | // checkRouteMatches: kiểm tra điểm đi, điểm đến của tuyến khớp tiêu chí | departurePoint, arrivalPoint | 2 | - | Mới | GL-36 |
| AC-E-Seat | entity | Seat | // checkAvailable: xác định chỗ còn trống theo BR-03<br>// hold: chuyển chỗ sang trạng thái đang giữ cho một lần đặt<br>// release: trả chỗ đang giữ về trạng thái còn trống (BR-08) | seatCode, status | 2, 4, 6, 9, 9a1 | - | Mới | GL-02 |
| AC-E-Booking | entity | Booking | // createBooking: khởi tạo lần đặt từ các chỗ đã chọn và thông tin người đi<br>// checkMaxSeats: kiểm tra số chỗ của lần đặt không quá 5 (BR-01)<br>// validateTravelerInfo: kiểm tra họ tên và số điện thoại người đi của mọi chỗ (ASM-15)<br>// calculateTotal: tính tổng tiền bằng tổng giá vé các chỗ (BR-06)<br>// holdSeats: giữ các chỗ của lần đặt và ghi nhận thời điểm bắt đầu giữ<br>// releaseSeats: trả các chỗ đang giữ khi hết thời hạn (BR-08)<br>// issueTickets: phát hành vé cho các chỗ đang giữ (BR-09, BR-10)<br>// getBookingSummary: cung cấp các vé đã phát hành và tổng tiền | totalAmount, holdStartTime, status, travelerInfos | 6, 7, 8, 9, 9a1, 11, 13 | - | Mới | GL-18 |
| AC-E-Ticket | entity | Ticket | // createTicket: khởi tạo vé với mã vé duy nhất cho một chỗ (BR-10)<br>// getTicketSmsContent: lập nội dung SMS gồm mã vé, tuyến, giờ xuất bến, chỗ, họ tên người đi | ticketCode, travelerName, travelerPhone, price, status | 11, 12 | - | Mới | GL-37 |
| AC-E-BaseFare | entity | BaseFare | // calculateTicketPrice: tính giá một vé từ giá theo tuyến và loại xe và mức tăng giá (BR-05) | busType, amount | 2, 8 | - | Mới | GL-09 |
| AC-E-HolidaySurcharge | entity | HolidaySurcharge | // getSurchargeRate: xác định mức tăng áp dụng cho ngày xuất bến, 0% nếu ngoài khoảng ngày (BR-05) | startDate, endDate, ratePercent | 2, 8 | - | Mới | GL-25 |

Số lớp: 11 (2 boundary, 2 control trong đó 1 control tạm của UC-003, 7 entity). Thuộc tính có kiểu khái niệm: departureTime (Giờ), availableSeatCount (Số lượng), status (Trạng thái), totalAmount và price và amount (Số tiền), holdStartTime (Giờ), ratePercent (Số lượng, đơn vị phần trăm), startDate và endDate (Ngày), các thuộc tính còn lại là Văn bản. travelerInfos của Booking là danh sách họ tên và số điện thoại người đi theo từng chỗ (ASM-43).

## 4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestBooking | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 1 | // searchTrips | AC-C-BookTicketOnlineController | Controller | - |
| 2 | // findMatchingTrips | AC-E-Trip | Information Expert | Dữ liệu tuyến và ngày xuất bến nằm ở Trip và Route. Giao cho Trip và thêm quan hệ tới Route; giao cho control bị loại vì control sẽ phải đọc dữ liệu của hai entity |
| 2 | // checkRouteMatches | AC-E-Route | Information Expert | - |
| 2 | // checkAvailable | AC-E-Seat | Information Expert | - |
| 2 | // getSurchargeRate | AC-E-HolidaySurcharge | Information Expert | Giá một vé cần dữ liệu ở BaseFare và HolidaySurcharge. Trip điều phối vì Trip biết tuyến, loại xe, ngày xuất bến; đưa vào control bị loại vì thành god control; gộp hai lớp bị loại vì phạm vi tuyến và loại xe của mức tăng chờ Q-20 |
| 2 | // calculateTicketPrice | AC-E-BaseFare | Information Expert | BaseFare giữ giá nền nên tính giá một vé theo BR-05 |
| 2 | // showTrips | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 2a | // showNoTripFoundNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 3 | // selectTrip | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 3 | // getSeatMap (Controller) | AC-C-BookTicketOnlineController | Controller | - |
| 4 | // getSeatMap (Trip) | AC-E-Trip | Information Expert | Trip biết các chỗ của chuyến |
| 4 | // checkAvailable | AC-E-Seat | Information Expert | - |
| 4 | // showSeatMap | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 4a | // showNoSeatLeftNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 5 | // selectSeatsAndEnterTravelerInfo | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 5 | // submitBooking | AC-C-BookTicketOnlineController | Controller | - |
| 6 | // createBooking | AC-E-Booking | Creator | Control có dữ liệu khởi tạo (chuyến, chỗ, thông tin người đi) và Booking là lớp ghi nhận chúng |
| 6 | // checkMaxSeats | AC-E-Booking | Information Expert | Booking biết số chỗ của chính nó |
| 6 | // checkSeatsAvailable | AC-E-Trip | Information Expert | Dữ liệu chỗ nằm ở Seat, danh sách chỗ nằm ở Booking và Trip. Giao cho Trip hỏi Seat vì trạng thái còn trống của chỗ phụ thuộc chuyến; giao cho Booking bị loại vì Booking sẽ phải truy cập Seat của chuyến ngoài lần đặt |
| 6 | // checkAvailable | AC-E-Seat | Information Expert | - |
| 6a | // showSeatLimitExceededNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 6b | // showSeatsUnavailableNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 7 | // validateTravelerInfo | AC-E-Booking | Information Expert | Dữ liệu người đi nằm ở Form (nhập) và Booking (ASM-43). Giao cho Booking vì ASM-15 là quy tắc dữ liệu và để giữ thứ tự báo lỗi bước 6 trước bước 7 (Q-34); boundary chỉ kiểm tra hình thức nhập nên bị loại |
| 7a | // showMissingTravelerInfoNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 7b | // showInvalidPhoneNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 8 | // calculateTotal | AC-E-Booking | Information Expert | BR-06 tính trên các chỗ của chính lần đặt |
| 8 | // determineTicketPrice | AC-E-Trip | Information Expert | Như bước 2 |
| 8 | // getSurchargeRate | AC-E-HolidaySurcharge | Information Expert | - |
| 8 | // calculateTicketPrice | AC-E-BaseFare | Information Expert | - |
| 9 | // holdSeats | AC-E-Booking | Information Expert | Booking biết các chỗ của mình và ghi thời điểm bắt đầu giữ |
| 9 | // hold | AC-E-Seat | Information Expert | - |
| 9 | // startWaitingForPayment | AC-C-BookTicketOnlineController | Controller | Điều phối riêng của use case, không là quy tắc dữ liệu |
| 9a | // handleSeatHoldExpired | AC-C-BookTicketOnlineController | Controller | - |
| 9a1 | // releaseSeats | AC-E-Booking | Information Expert | - |
| 9a1 | // release | AC-E-Seat | Information Expert | - |
| 9a2 | // showHoldExpiredNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 10 | // payTickets | AC-C-PayTicketOnlineController | Controller (include) | - |
| 10a | // showPaymentFailedNotice | AC-B-BookTicketForm | Giao tiếp tác nhân | - |
| 11 | // issueTickets | AC-E-Booking | Creator | Booking chứa các chỗ được phát hành vé |
| 11 | // createTicket | AC-E-Ticket | Creator | Ticket tự cấp mã vé duy nhất (BR-10) |
| 12 | // getTicketSmsContent | AC-E-Ticket | Information Expert | - |
| 12 | // getRouteAndDepartureTime | AC-E-Trip | Information Expert | - |
| 12 | // sendTicketSms | AC-B-SmsGateway | Giao tiếp tác nhân | - |
| 13 | // getBookingSummary | AC-E-Booking | Information Expert | - |
| 13 | // showIssuedTickets | AC-B-BookTicketForm | Giao tiếp tác nhân | - |

## 5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-002.drawio gồm ba trang. SD1 thể hiện luồng chính cùng luồng 9a (break) và 10a (loop, opt); SD2 và SD3 thể hiện các luồng thay thế quay lại bước trước. Message ở SD2, SD3 mang STT của message cùng điểm rẽ nhánh trong SD1 kèm hậu tố a hoặc b (ví dụ 3.1.4a là nhánh của message 3.1.4).

Bảng message dùng thêm cột ID (ID cell trong file .drawio). Lifeline Booking và Ticket có đỉnh đặt ngang message Tạo tương ứng (3.1.1 và 3.1.11.1).

### SD1 - Luồng chính, 9a, 10a

a) Tên sơ đồ và luồng thể hiện: luồng chính (bước 1 đến 13), luồng 9a (break) và luồng 10a (loop, opt).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1-L01 | Actor | Hành khách | ACT-01 (Người) | - | Tác nhân chính | 40 | 40 | 120 | 1940 |
| SD1-L02 | Lifeline | :BookTicketForm | boundary | - | Boundary của ACT-01 | 200 | 40 | 120 | 1940 |
| SD1-L03 | Lifeline | :BookTicketOnlineController | control | - | Control của UC-002 | 360 | 40 | 120 | 1940 |
| SD1-L04 | Lifeline | :PayTicketOnlineController | control | - | Control của UC-003, mã tạm chờ P07 của UC-003 | 520 | 40 | 120 | 1940 |
| SD1-L05 | Lifeline | :Trip | entity | - | - | 680 | 40 | 120 | 1940 |
| SD1-L06 | Lifeline | :Route | entity | - | - | 840 | 40 | 120 | 1940 |
| SD1-L07 | Lifeline | :Seat | entity | - | - | 1000 | 40 | 120 | 1940 |
| SD1-L08 | Lifeline | :Booking | entity | - | Được tạo bởi message 3.1.1 | 1160 | 800 | 120 | 1180 |
| SD1-L09 | Lifeline | :BaseFare | entity | - | - | 1320 | 40 | 120 | 1940 |
| SD1-L10 | Lifeline | :HolidaySurcharge | entity | - | - | 1480 | 40 | 120 | 1940 |
| SD1-L11 | Lifeline | :Ticket | entity | - | Được tạo bởi message 3.1.11.1, một đối tượng cho mỗi chỗ đang giữ | 1640 | 1600 | 120 | 380 |
| SD1-L12 | Lifeline | :SmsGateway | boundary | - | Boundary của ACT-07 | 1800 | 40 | 120 | 1940 |
| SD1-L13 | Actor | Cổng SMS | ACT-07 (Hệ thống ngoài) | - | Tác nhân phụ | 1960 | 40 | 120 | 1940 |
| SD1-FR1 | Fragment | break [hết thời hạn giữ chỗ (BR-07) mà thanh toán chưa thành công] | break | - | Luồng 9a, kết thúc use case (thất bại) | 180 | 1260 | 1120 | 150 |
| SD1-FR2 | Fragment | loop [thanh toán chưa thành công và chưa hết thời hạn giữ chỗ (BR-07, ASM-14)] | loop | - | Quay lại bước 10 (luồng 10a); gọi UC-003 bằng message tới control, không vẽ nội bộ UC-003 | 170 | 1420 | 490 | 120 |
| SD1-FR3 | Fragment | opt [UC-003 trả kết quả không thành công] | opt | SD1-FR2 | Luồng 10a | 180 | 1500 | 470 | 30 |
| SD1-FR4 | Fragment | loop [với mỗi vé đã phát hành] | loop | - | Bước 12, mỗi vé một SMS (ASM-13) | 340 | 1620 | 1760 | 190 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1-M01 | 1 | SD1-L01 | SD1-L02 | // requestBooking (điểm đi, điểm đến, ngày đi) | Đồng bộ | - | 1 |
| SD1-M02 | 1.1 | SD1-L02 | SD1-L03 | // searchTrips (điểm đi, điểm đến, ngày đi) | Đồng bộ | - | 1 |
| SD1-M03 | 1.1.1 | SD1-L03 | SD1-L05 | // findMatchingTrips (điểm đi, điểm đến, ngày đi) | Đồng bộ | - | 2 |
| SD1-M04 | 1.1.1.1 | SD1-L05 | SD1-L06 | // checkRouteMatches (điểm đi, điểm đến) | Đồng bộ | - | 2 |
| SD1-M05 | 1.1.1.2 | SD1-L05 | SD1-L07 | // checkAvailable (chỗ của chuyến) | Đồng bộ | - | 2 |
| SD1-M06 | 1.1.1.3 | SD1-L05 | SD1-L10 | // getSurchargeRate (ngày xuất bến) | Đồng bộ | - | 2 |
| SD1-M07 | 1.1.1.4 | SD1-L05 | SD1-L09 | // calculateTicketPrice (loại xe, mức tăng) | Đồng bộ | - | 2 |
| SD1-M08 | 1.1.1 (trả về) | SD1-L05 | SD1-L03 | danh sách chuyến kèm số chỗ còn trống và giá vé | Trả về | - | 2 |
| SD1-M09 | 1.1.2 | SD1-L03 | SD1-L02 | // showTrips (danh sách chuyến) | Đồng bộ | - | 2 |
| SD1-M10 | 2 | SD1-L01 | SD1-L02 | // selectTrip | Đồng bộ | - | 3 |
| SD1-M11 | 2.1 | SD1-L02 | SD1-L03 | // getSeatMap (chuyến đã chọn) | Đồng bộ | - | 3 |
| SD1-M12 | 2.1.1 | SD1-L03 | SD1-L05 | // getSeatMap | Đồng bộ | - | 4 |
| SD1-M13 | 2.1.1.1 | SD1-L05 | SD1-L07 | // checkAvailable (từng chỗ của chuyến) | Đồng bộ | - | 4 |
| SD1-M14 | 2.1.1 (trả về) | SD1-L05 | SD1-L03 | sơ đồ chỗ kèm trạng thái từng chỗ | Trả về | - | 4 |
| SD1-M15 | 2.1.2 | SD1-L03 | SD1-L02 | // showSeatMap (sơ đồ chỗ) | Đồng bộ | - | 4 |
| SD1-M16 | 3 | SD1-L01 | SD1-L02 | // selectSeatsAndEnterTravelerInfo (chỗ, họ tên, số điện thoại) | Đồng bộ | - | 5 |
| SD1-M17 | 3.1 | SD1-L02 | SD1-L03 | // submitBooking (chỗ, họ tên, số điện thoại) | Đồng bộ | - | 5 |
| SD1-M18 | 3.1.1 | SD1-L03 | SD1-L08 | // createBooking (chuyến, chỗ đã chọn, thông tin người đi) | Tạo | - | 6 |
| SD1-M19 | 3.1.2 | SD1-L03 | SD1-L08 | // checkMaxSeats | Đồng bộ | - | 6 |
| SD1-M20 | 3.1.3 | SD1-L03 | SD1-L05 | // checkSeatsAvailable (chỗ đã chọn) | Đồng bộ | - | 6 |
| SD1-M21 | 3.1.3.1 | SD1-L05 | SD1-L07 | // checkAvailable (từng chỗ đã chọn) | Đồng bộ | - | 6 |
| SD1-M22 | 3.1.4 | SD1-L03 | SD1-L08 | // validateTravelerInfo | Đồng bộ | - | 7 |
| SD1-M23 | 3.1.5 | SD1-L03 | SD1-L08 | // calculateTotal | Đồng bộ | - | 8 |
| SD1-M24 | 3.1.5.1 | SD1-L08 | SD1-L05 | // determineTicketPrice (từng chỗ) | Đồng bộ | - | 8 |
| SD1-M25 | 3.1.5.1.1 | SD1-L05 | SD1-L10 | // getSurchargeRate (ngày xuất bến) | Đồng bộ | - | 8 |
| SD1-M26 | 3.1.5.1.2 | SD1-L05 | SD1-L09 | // calculateTicketPrice (loại xe, mức tăng) | Đồng bộ | - | 8 |
| SD1-M27 | 3.1.6 | SD1-L03 | SD1-L08 | // holdSeats | Đồng bộ | - | 9 |
| SD1-M28 | 3.1.6.1 | SD1-L08 | SD1-L07 | // hold (từng chỗ của lần đặt) | Đồng bộ | - | 9 |
| SD1-M29 | 3.1.7 | SD1-L03 | SD1-L03 | // startWaitingForPayment (BR-07) | Tự gọi | - | 9 |
| SD1-M30 | 3.1.8 | SD1-L03 | SD1-L03 | // after(BR-07) handleSeatHoldExpired | Tự gọi | SD1-FR1 | 9a |
| SD1-M31 | 3.1.8.1 | SD1-L03 | SD1-L08 | // releaseSeats | Đồng bộ | SD1-FR1 | 9a1 |
| SD1-M32 | 3.1.8.1.1 | SD1-L08 | SD1-L07 | // release (từng chỗ đang giữ) | Đồng bộ | SD1-FR1 | 9a1 |
| SD1-M33 | 3.1.8.2 | SD1-L03 | SD1-L02 | // showHoldExpiredNotice | Đồng bộ | SD1-FR1 | 9a2 |
| SD1-M34 | 3.1.9 | SD1-L03 | SD1-L04 | // payTickets (tổng tiền của lần đặt) | Đồng bộ | SD1-FR2 | 10 |
| SD1-M35 | 3.1.9 (trả về) | SD1-L04 | SD1-L03 | kết quả thanh toán (thành công hoặc không thành công) | Trả về | SD1-FR2 | 10 |
| SD1-M36 | 3.1.10 | SD1-L03 | SD1-L02 | // showPaymentFailedNotice | Đồng bộ | SD1-FR3 | 10a |
| SD1-M37 | 3.1.11 | SD1-L03 | SD1-L08 | // issueTickets | Đồng bộ | - | 11 |
| SD1-M38 | 3.1.11.1 | SD1-L08 | SD1-L11 | // createTicket (chỗ, họ tên, số điện thoại, giá vé) | Tạo | - | 11 |
| SD1-M39 | 3.1.12 | SD1-L03 | SD1-L11 | // getTicketSmsContent | Đồng bộ | SD1-FR4 | 12 |
| SD1-M40 | 3.1.12.1 | SD1-L11 | SD1-L05 | // getRouteAndDepartureTime | Đồng bộ | SD1-FR4 | 12 |
| SD1-M41 | 3.1.12 (trả về) | SD1-L11 | SD1-L03 | nội dung SMS của vé và số điện thoại người đi | Trả về | SD1-FR4 | 12 |
| SD1-M42 | 3.1.13 | SD1-L03 | SD1-L12 | // sendTicketSms (nội dung SMS, số điện thoại người đi) | Đồng bộ | SD1-FR4 | 12 |
| SD1-M43 | 3.1.13.1 | SD1-L12 | SD1-L13 | // deliverSms (nội dung SMS, số điện thoại người đi) | Đồng bộ | SD1-FR4 | 12 |
| SD1-M44 | 3.1.14 | SD1-L03 | SD1-L08 | // getBookingSummary | Đồng bộ | - | 13 |
| SD1-M45 | 3.1.14 (trả về) | SD1-L08 | SD1-L03 | các vé đã phát hành và tổng tiền | Trả về | - | 13 |
| SD1-M46 | 3.1.15 | SD1-L03 | SD1-L02 | // showIssuedTickets (vé, tổng tiền) | Đồng bộ | - | 13 |

SD1 có 46 dòng message, trong đó 5 message trả về; 3 fragment ngoài cùng (FR1, FR2, FR4) và 1 fragment lồng (FR3). Bước 10 gửi message tới control của UC-003 (3.1.9), nội bộ UC-003 không vẽ lại. Hết thời hạn giữ chỗ vẽ bằng message tự gọi 3.1.8 trong break FR1; luồng 10a vẽ bằng loop FR2 chứa opt FR3.

### SD2 - Luồng 2a, 4a

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 2a (quay lại bước 1) và 4a (quay lại bước 3).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD2-L01 | Lifeline | :BookTicketForm | boundary | - | Boundary của ACT-01 | 40 | 40 | 120 | 260 |
| SD2-L02 | Lifeline | :BookTicketOnlineController | control | - | Control của UC-002 | 200 | 40 | 120 | 260 |
| SD2-FR1 | Fragment | alt [không có chuyến nào khớp tiêu chí (ASM-16)] | alt | - | Điểm rẽ nhánh: sau 1.1.1 (trả về) của SD1. Luồng 2a quay lại bước 1. Toán hạng 1 | 20 | 100 | 320 | 70 |
| SD2-FR1-O2 | Fragment | [có chuyến khớp tiêu chí] | alt | SD2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SD2-FR1-SEP | 30 | 140 | 300 | 20 |
| SD2-FR2 | Fragment | alt [chuyến đã chọn không còn chỗ trống nào (BR-03)] | alt | - | Điểm rẽ nhánh: sau 2.1.1 (trả về) của SD1. Luồng 4a quay lại bước 3. Toán hạng 1 | 20 | 180 | 320 | 70 |
| SD2-FR2-O2 | Fragment | [chuyến còn chỗ trống] | alt | SD2-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SD2-FR2-SEP | 30 | 220 | 300 | 20 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2-M01 | 1.1.2a | SD2-L02 | SD2-L01 | // showNoTripFoundNotice (tiêu chí đã cung cấp) | Đồng bộ | SD2-FR1 | 2a |
| SD2-M02 | 1.1.2 | SD2-L02 | SD2-L01 | // showTrips (danh sách chuyến) | Đồng bộ | SD2-FR1 | 2 |
| SD2-M03 | 2.1.2a | SD2-L02 | SD2-L01 | // showNoSeatLeftNotice | Đồng bộ | SD2-FR2 | 4a |
| SD2-M04 | 2.1.2 | SD2-L02 | SD2-L01 | // showSeatMap (sơ đồ chỗ) | Đồng bộ | SD2-FR2 | 4 |

Trang không vẽ lại các message của luồng chính dẫn tới điểm rẽ nhánh; điểm rẽ nhánh ghi ở cột Ghi chú của fragment. Toán hạng else của mỗi alt lặp lại message của luồng chính (1.1.2, 2.1.2) để guard có đủ hai toán hạng.

### SD3 - Luồng 6a, 6b, 7a, 7b

a) Tên sơ đồ và luồng thể hiện: luồng thay thế 6a (quay lại bước 5), 6b (quay lại bước 4), 7a và 7b (quay lại bước 5).

b) Bảng lifeline và fragment (bảng Node):

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD3-L01 | Lifeline | :BookTicketForm | boundary | - | Boundary của ACT-01 | 40 | 40 | 120 | 260 |
| SD3-L02 | Lifeline | :BookTicketOnlineController | control | - | Control của UC-002 | 200 | 40 | 120 | 260 |
| SD3-FR1 | Fragment | alt [số chỗ đã chọn lớn hơn 5 (BR-01)] | alt | - | Điểm rẽ nhánh: sau 3.1.2 và 3.1.3 của SD1. Luồng 6a quay lại bước 5, luồng 6b quay lại bước 4. Toán hạng 1 | 20 | 100 | 320 | 70 |
| SD3-FR1-O2 | Fragment | [số chỗ không lớn hơn 5 và có chỗ không còn trống (BR-03)] | alt | SD3-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SD3-FR1-SEP | 30 | 140 | 300 | 20 |
| SD3-FR2 | Fragment | alt [thiếu họ tên hoặc số điện thoại người đi của ít nhất một chỗ] | alt | - | Điểm rẽ nhánh: sau 3.1.4 của SD1. Luồng 7a, 7b quay lại bước 5. Toán hạng 1 | 20 | 180 | 320 | 70 |
| SD3-FR2-O2 | Fragment | [thông tin người đi đủ và có số điện thoại sai định dạng (ASM-15)] | alt | SD3-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SD3-FR2-SEP | 30 | 220 | 300 | 20 |

c) Bảng message (bảng Edge):

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD3-M01 | 3.1.2a | SD3-L02 | SD3-L01 | // showSeatLimitExceededNotice (BR-01) | Đồng bộ | SD3-FR1 | 6a |
| SD3-M02 | 3.1.3a | SD3-L02 | SD3-L01 | // showSeatsUnavailableNotice (các chỗ không còn trống) | Đồng bộ | SD3-FR1 | 6b |
| SD3-M03 | 3.1.4a | SD3-L02 | SD3-L01 | // showMissingTravelerInfoNotice | Đồng bộ | SD3-FR2 | 7a |
| SD3-M04 | 3.1.4b | SD3-L02 | SD3-L01 | // showInvalidPhoneNotice | Đồng bộ | SD3-FR2 | 7b |

Mỗi alt có hai toán hạng, mỗi toán hạng có guard theo điều kiện của đặc tả. Hai luồng ở mỗi alt loại trừ nhau theo điều kiện P04 (6b chỉ khi số chỗ không lớn hơn 5; 7b chỉ khi thông tin đủ).

## 6. Quy tắc tương tác giữa các lớp phân tích

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

Đã kiểm tra mọi message của SD1, SD2, SD3 và mọi link của communication diagram theo bảng F6: actor chỉ gửi message tới boundary (ACT-01 --> BookTicketForm), boundary chỉ trao đổi với actor của nó và control (SmsGateway --> ACT-07), control gọi boundary, entity và control của UC-003, entity gọi entity khi có quan hệ cấu trúc (Trip, Booking, Ticket tới Seat, Trip, Route, BaseFare, HolidaySurcharge).

## 7. Communication diagram

File diagrams/P07-communication-UC-002.drawio, phạm vi là luồng chính của SD1 cùng luồng thay thế đã gộp vào SD1 (9a, 10a). MUC_CHI_TIET là DAY_DU. Luồng thay thế ở SD2, SD3 nằm trên trang riêng nên không gộp vào communication diagram. Nhãn link dùng STT của SD1; message trả về không xuất hiện.

a) Bảng Node:

| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| CO-01 | Actor | Hành khách | - | - | Tác nhân chính | 40 | 200 | 40 | 80 |
| CO-02 | Object | :BookTicketForm | boundary | - | Boundary của ACT-01 | 200 | 220 | 160 | 40 |
| CO-03 | Object | :BookTicketOnlineController | control | - | Control của UC-002 | 480 | 220 | 160 | 40 |
| CO-04 | Object | :PayTicketOnlineController | control | - | Control của UC-003, mã tạm | 480 | 60 | 160 | 40 |
| CO-05 | Object | :SmsGateway | boundary | - | Boundary của ACT-07 | 840 | 220 | 160 | 40 |
| CO-06 | Actor | Cổng SMS | - | - | Tác nhân phụ | 1080 | 200 | 40 | 80 |
| CO-07 | Object | :Trip | entity | - | - | 200 | 420 | 160 | 40 |
| CO-08 | Object | :Booking | entity | - | - | 480 | 420 | 160 | 40 |
| CO-09 | Object | :Ticket | entity | - | - | 760 | 520 | 160 | 40 |
| CO-10 | Object | :Route | entity | - | - | 40 | 620 | 160 | 40 |
| CO-11 | Object | :Seat | entity | - | - | 280 | 620 | 160 | 40 |
| CO-12 | Object | :BaseFare | entity | - | - | 520 | 620 | 160 | 40 |
| CO-13 | Object | :HolidaySurcharge | entity | - | - | 760 | 620 | 160 | 40 |

b) Bảng Edge (link):

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message |
|---|---|---|---|---|---|
| LK-01 | CO-01 | CO-02 | Link | 1: // requestBooking (điểm đi, điểm đến, ngày đi) (-->)<br>2: // selectTrip (-->)<br>3: // selectSeatsAndEnterTravelerInfo (chỗ, họ tên, số điện thoại) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-02 | CO-02 | CO-03 | Link | 1.1: // searchTrips (điểm đi, điểm đến, ngày đi) (-->)<br>1.1.2: // showTrips (danh sách chuyến) (<--)<br>2.1: // getSeatMap (chuyến đã chọn) (-->)<br>2.1.2: // showSeatMap (sơ đồ chỗ) (<--)<br>3.1: // submitBooking (chỗ, họ tên, số điện thoại) (-->)<br>3.1.8.2: // showHoldExpiredNotice (<--)<br>3.1.10: // showPaymentFailedNotice (<--)<br>3.1.15: // showIssuedTickets (vé, tổng tiền) (<--) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-03 | CO-03 | CO-07 | Link | 1.1.1: // findMatchingTrips (điểm đi, điểm đến, ngày đi) (-->)<br>2.1.1: // getSeatMap (-->)<br>3.1.3: // checkSeatsAvailable (chỗ đã chọn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-04 | CO-07 | CO-10 | Link | 1.1.1.1: // checkRouteMatches (điểm đi, điểm đến) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-05 | CO-07 | CO-11 | Link | 1.1.1.2: // checkAvailable (chỗ của chuyến) (-->)<br>2.1.1.1: // checkAvailable (từng chỗ của chuyến) (-->)<br>3.1.3.1: // checkAvailable (từng chỗ đã chọn) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-06 | CO-07 | CO-13 | Link | 1.1.1.3: // getSurchargeRate (ngày xuất bến) (-->)<br>3.1.5.1.1: // getSurchargeRate (ngày xuất bến) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-07 | CO-07 | CO-12 | Link | 1.1.1.4: // calculateTicketPrice (loại xe, mức tăng) (-->)<br>3.1.5.1.2: // calculateTicketPrice (loại xe, mức tăng) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-08 | CO-03 | CO-08 | Link | 3.1.1: // createBooking (chuyến, chỗ đã chọn, thông tin người đi) (-->)<br>3.1.2: // checkMaxSeats (-->)<br>3.1.4: // validateTravelerInfo (-->)<br>3.1.5: // calculateTotal (-->)<br>3.1.6: // holdSeats (-->)<br>3.1.8.1: // releaseSeats (-->)<br>3.1.11: // issueTickets (-->)<br>3.1.14: // getBookingSummary (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-09 | CO-08 | CO-07 | Link | 3.1.5.1: // determineTicketPrice (từng chỗ) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-10 | CO-08 | CO-11 | Link | 3.1.6.1: // hold (từng chỗ của lần đặt) (-->)<br>3.1.8.1.1: // release (từng chỗ đang giữ) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-11 | CO-03 | CO-03 | Link | 3.1.7: // startWaitingForPayment (BR-07) (-->)<br>3.1.8: // after(BR-07) handleSeatHoldExpired (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-12 | CO-03 | CO-04 | Link | 3.1.9: // payTickets (tổng tiền của lần đặt) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-13 | CO-08 | CO-09 | Link | 3.1.11.1: // createTicket (chỗ, họ tên, số điện thoại, giá vé) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-14 | CO-03 | CO-09 | Link | 3.1.12: // getTicketSmsContent (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-15 | CO-09 | CO-07 | Link | 3.1.12.1: // getRouteAndDepartureTime (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-16 | CO-03 | CO-05 | Link | 3.1.13: // sendTicketSms (nội dung SMS, số điện thoại người đi) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |
| LK-17 | CO-05 | CO-06 | Link | 3.1.13.1: // deliverSms (nội dung SMS, số điện thoại người đi) (-->) | Nguồn-->Đích hoặc Đích-->Nguồn theo từng message trong nhãn |

Tổng số message trên các link: 41 (bằng số message không phải trả về của SD1: 41). Link LK-11 là link tự gọi của control (message 3.1.7, 3.1.8).

## 8. VOPC

File diagrams/P07-class-UC-002.drawio.

a) Bảng Node (lớp):

| ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-B-BookTicketForm | Class | BookTicketForm | «boundary» | - | departurePoint<br>arrivalPoint<br>travelDate<br>selectedSeats<br>travelerNames<br>travelerPhones | // requestBooking<br>// selectTrip<br>// selectSeatsAndEnterTravelerInfo<br>// showTrips<br>// showSeatMap<br>// showNoTripFoundNotice<br>// showNoSeatLeftNotice<br>// showSeatLimitExceededNotice<br>// showSeatsUnavailableNotice<br>// showMissingTravelerInfoNotice<br>// showInvalidPhoneNotice<br>// showHoldExpiredNotice<br>// showPaymentFailedNotice<br>// showIssuedTickets | 360 | 40 | 240 | 440 |
| AC-B-SmsGateway | Class | SmsGateway | «boundary» | - | recipientPhone<br>smsContent | // sendTicketSms | 1000 | 40 | 240 | 100 |
| AC-C-BookTicketOnlineController | Class | BookTicketOnlineController | «control» | - | - | // searchTrips<br>// getSeatMap<br>// submitBooking<br>// startWaitingForPayment<br>// handleSeatHoldExpired | 680 | 560 | 240 | 160 |
| AC-C-PayTicketOnlineController | Class | PayTicketOnlineController | «control» | - | - | // payTickets | 360 | 560 | 240 | 80 |
| AC-E-Trip | Class | Trip | «entity» | - | departureTime<br>busType<br>availableSeatCount | // findMatchingTrips<br>// getSeatMap<br>// checkSeatsAvailable<br>// determineTicketPrice<br>// getRouteAndDepartureTime | 680 | 820 | 240 | 200 |
| AC-E-Route | Class | Route | «entity» | - | departurePoint<br>arrivalPoint | // checkRouteMatches | 40 | 1260 | 240 | 100 |
| AC-E-Seat | Class | Seat | «entity» | - | seatCode<br>status | // checkAvailable<br>// hold<br>// release | 680 | 1260 | 240 | 140 |
| AC-E-Booking | Class | Booking | «entity» | - | totalAmount<br>holdStartTime<br>status<br>travelerInfos | // createBooking<br>// checkMaxSeats<br>// validateTravelerInfo<br>// calculateTotal<br>// holdSeats<br>// releaseSeats<br>// issueTickets<br>// getBookingSummary | 360 | 820 | 240 | 280 |
| AC-E-Ticket | Class | Ticket | «entity» | - | ticketCode<br>travelerName<br>travelerPhone<br>price<br>status | // createTicket<br>// getTicketSmsContent | 1000 | 820 | 240 | 180 |
| AC-E-BaseFare | Class | BaseFare | «entity» | - | busType<br>amount | // calculateTicketPrice | 360 | 1260 | 240 | 100 |
| AC-E-HolidaySurcharge | Class | HolidaySurcharge | «entity» | - | startDate<br>endDate<br>ratePercent | // getSurchargeRate | 1000 | 1260 | 240 | 120 |

b) Bảng quan hệ (bảng Edge):

| ID | Lớp A | Lớp B | Loại (Association / Aggregation / Composition / Generalization / Dependency) | Multiplicity | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC002-01 | AC-B-BookTicketForm | AC-C-BookTicketOnlineController | Association | - | tạm thời | LK-02 |
| R-UC002-02 | AC-C-BookTicketOnlineController | AC-B-SmsGateway | Association | - | tạm thời | LK-16 |
| R-UC002-03 | AC-C-BookTicketOnlineController | AC-C-PayTicketOnlineController | Dependency | - | tạm thời; «include» RL-27 | LK-12, RL-27 |
| R-UC002-04 | AC-C-BookTicketOnlineController | AC-E-Trip | Association | - | tạm thời | LK-03 |
| R-UC002-05 | AC-C-BookTicketOnlineController | AC-E-Booking | Association | - | tạm thời | LK-08 |
| R-UC002-06 | AC-C-BookTicketOnlineController | AC-E-Ticket | Association | - | tạm thời | LK-14 |
| R-UC002-07 | AC-E-Trip | AC-E-Route | Association | A 0..* - B 1 | chuyến thuộc một tuyến | LK-04; GL-04 "Một lần chạy của một tuyến" |
| R-UC002-08 | AC-E-Trip | AC-E-Seat | Association | A 1 - B 1..* | chuyến gồm các chỗ | LK-05; ASM-42 |
| R-UC002-09 | AC-E-Trip | AC-E-BaseFare | Association | - | tạm thời; tra giá theo tuyến và loại xe của chuyến | LK-07; BR-04 |
| R-UC002-10 | AC-E-Trip | AC-E-HolidaySurcharge | Association | - | tạm thời; phạm vi tuyến, loại xe chờ Q-20 | LK-06; BR-05 |
| R-UC002-11 | AC-E-Booking | AC-E-Trip | Association | A 0..* - B 1 | lần đặt cho một chuyến | LK-09; GL-18 "cùng một chuyến" |
| R-UC002-12 | AC-E-Booking | AC-E-Seat | Association | A - B 1..5 | chỗ của lần đặt | LK-10; BR-01 |
| R-UC002-13 | AC-E-Booking | AC-E-Ticket | Association | A 1 - B 0..5 | vé phát hành cho lần đặt | LK-13; BR-01, BR-10 |
| R-UC002-14 | AC-E-Ticket | AC-E-Trip | Association | A 0..* - B 1 | vé thuộc một chuyến | LK-15; GL-37 |
| R-UC002-15 | AC-E-Ticket | AC-E-Seat | Association | A - B 1 | vé của một chỗ | BR-10; chờ Q-36 cho phía A |
| R-UC002-16 | AC-E-BaseFare | AC-E-Route | Association | A - B 1 | giá đặt theo tuyến | BR-04 |

Link actor-boundary (LK-01, LK-17) và link tự gọi (LK-11) không vào VOPC. Mỗi link còn lại giữa hai lớp khác nhau của F7 sinh một quan hệ (R-UC002-01 đến R-UC002-14); R-UC002-15 và R-UC002-16 dựa trên bằng chứng của đặc tả (BR-10, BR-04). Multiplicity "-" nghĩa là đặc tả chưa nêu rõ nên để trống (A, B ghi "-" ở phía chưa rõ). Quan hệ cuối cùng chốt ở P08.

## 9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) và tác nhân |
|---|---|---|
| 1 | 1 (SD1), 1.1 (SD1) | ACT-01, AC-B-BookTicketForm, AC-C-BookTicketOnlineController |
| 2 | 1.1.1 (SD1), 1.1.1.1 (SD1), 1.1.1.2 (SD1), 1.1.1.3 (SD1), 1.1.1.4 (SD1), 1.1.1 (trả về) (SD1), 1.1.2 (SD1), 1.1.2 (SD2) | AC-C-BookTicketOnlineController, AC-E-Trip, AC-E-Route, AC-E-Seat, AC-E-HolidaySurcharge, AC-E-BaseFare, AC-B-BookTicketForm |
| 2a | 1.1.2a (SD2) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 3 | 2 (SD1), 2.1 (SD1) | ACT-01, AC-B-BookTicketForm, AC-C-BookTicketOnlineController |
| 4 | 2.1.1 (SD1), 2.1.1.1 (SD1), 2.1.1 (trả về) (SD1), 2.1.2 (SD1), 2.1.2 (SD2) | AC-C-BookTicketOnlineController, AC-E-Trip, AC-E-Seat, AC-B-BookTicketForm |
| 4a | 2.1.2a (SD2) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 5 | 3 (SD1), 3.1 (SD1) | ACT-01, AC-B-BookTicketForm, AC-C-BookTicketOnlineController |
| 6 | 3.1.1 (SD1), 3.1.2 (SD1), 3.1.3 (SD1), 3.1.3.1 (SD1) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Trip, AC-E-Seat |
| 6a | 3.1.2a (SD3) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 6b | 3.1.3a (SD3) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 7 | 3.1.4 (SD1) | AC-C-BookTicketOnlineController, AC-E-Booking |
| 7a | 3.1.4a (SD3) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 7b | 3.1.4b (SD3) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 8 | 3.1.5 (SD1), 3.1.5.1 (SD1), 3.1.5.1.1 (SD1), 3.1.5.1.2 (SD1) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Trip, AC-E-HolidaySurcharge, AC-E-BaseFare |
| 9 | 3.1.6 (SD1), 3.1.6.1 (SD1), 3.1.7 (SD1) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Seat |
| 9a | 3.1.8 (SD1) | AC-C-BookTicketOnlineController |
| 9a1 | 3.1.8.1 (SD1), 3.1.8.1.1 (SD1) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Seat |
| 9a2 | 3.1.8.2 (SD1) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 10 | 3.1.9 (SD1), 3.1.9 (trả về) (SD1) | AC-C-BookTicketOnlineController, AC-C-PayTicketOnlineController |
| 10a | 3.1.10 (SD1) | AC-C-BookTicketOnlineController, AC-B-BookTicketForm |
| 11 | 3.1.11 (SD1), 3.1.11.1 (SD1) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-E-Ticket |
| 12 | 3.1.12 (SD1), 3.1.12.1 (SD1), 3.1.12 (trả về) (SD1), 3.1.13 (SD1), 3.1.13.1 (SD1) | AC-C-BookTicketOnlineController, AC-E-Ticket, AC-E-Trip, AC-B-SmsGateway, ACT-07 |
| 13 | 3.1.14 (SD1), 3.1.14 (trả về) (SD1), 3.1.15 (SD1) | AC-C-BookTicketOnlineController, AC-E-Booking, AC-B-BookTicketForm |

## 10. File .drawio

| File | Trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-002.drawio | SD1, SD2, SD3 | Bảng F5; ID cell là ID trong bảng lifeline, fragment, message |
| diagrams/P07-communication-UC-002.drawio | COMM1 | Bảng F7; ID cell là ID trong bảng Node và Edge |
| diagrams/P07-class-UC-002.drawio | VOPC1 | Bảng F8; ID cell của lớp là mã AC, của cạnh là ID quan hệ, nhãn multiplicity là cell con của cạnh |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-69 | Chỗ trên sơ đồ chỗ thuộc về xe (bố trí cố định theo xe, trạng thái ghi theo chuyến) hay thuộc về chuyến (mỗi chuyến có tập chỗ riêng)? (Thuộc chuyến / Thuộc xe, trạng thái theo chuyến lưu riêng) | AC-E-Seat, AC-E-Trip; R-UC002-08; ASM-42; P08, P13 | Dữ liệu ra 2 #1: "Mã chỗ trên sơ đồ chỗ của xe của chuyến"; BR-02, BR-03: "chỗ của chuyến" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-42 | Mỗi chuyến có tập chỗ riêng theo sơ đồ xe được xếp; chỗ và trạng thái (còn trống, đang giữ, đã có vé) được quản lý theo chuyến, xe không tham gia hành vi của UC-002. | Dữ liệu ra 2 mô tả sơ đồ chỗ "của xe của chuyến" còn BR-02, BR-03 nói "chỗ của chuyến"; việc giữ và trả chỗ cần một đối tượng có định danh chỗ trên một chuyến. Chờ Q-69 | AC-E-Seat, AC-E-Trip; R-UC002-08; F2 bước 4, 9; loại danh từ Xe ở F3.2 |
| ASM-43 | Lần đặt giữ họ tên và số điện thoại người đi của từng chỗ từ bước 6 tới khi vé được phát hành; khi phát hành, thông tin đó được ghi vào vé của chỗ. | P04 không nêu nơi giữ thông tin người đi trước khi có vé, trong khi bước 7 phải kiểm tra thông tin này khi chưa có vé nào | AC-E-Booking (travelerInfos), AC-E-Ticket; bước 6, 7, 11 |
| ASM-44 | Lần đặt được khởi tạo khi hệ thống nhận yêu cầu ở bước 6 để kiểm tra BR-01 và thông tin người đi; yêu cầu bị từ chối ở 6a, 6b, 7a, 7b không để lại lần đặt nào được lưu. | P04 không nêu thời điểm bắt đầu có lần đặt; hậu điều kiện tối thiểu chỉ nói không có vé nào được phát hành và chỗ trở lại còn trống khi không thành công | AC-E-Booking; message 3.1.1; bước 6, 6a, 6b, 7a, 7b |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-002 Dữ liệu vào 1 #1, #2, #3 (ASM-15) | Điều kiện hợp lệ của điểm đi, điểm đến và ngày đi (ngày không trước ngày hiện tại) được nêu ở Dữ liệu vào 1 nhưng luồng sự kiện không có bước và luồng thay thế nào kiểm tra, nên không phân bổ được cho lớp nào | Thêm bước kiểm tra tiêu chí tìm chuyến và luồng thay thế cho tiêu chí không hợp lệ, hoặc bỏ cột điều kiện hợp lệ khỏi Dữ liệu vào 1 |
| P04 | UC-002 luồng 9a, Mục 8 ("Thời hạn giữ chỗ (BR-07) tiếp tục chạy trong khi UC-003 đang thực hiện") | Luồng 9a gắn với bước 9 nhưng hết thời hạn giữ chỗ có thể xảy ra khi bước 10 hoặc 10a đang thực hiện. Sơ đồ phân tích đặt 9a trước bước 10 theo thứ tự bước nên không thể hiện việc UC-003 bị ngắt khi hết thời hạn | Ghi điều kiện của 9a áp dụng cho các bước 9 đến 10a và nêu UC-003 đang chạy bị ngắt thế nào khi hết thời hạn (liên quan Q-10, Q-55) |
| P04 | UC-002 bước 12 | Đặc tả thiếu luồng ngoại lệ cho lỗi của hệ thống ngoài khi Cổng SMS không nhận hoặc báo lỗi, nên SD1 không có nhánh xử lý (Q-56) | Thêm luồng ngoại lệ gửi SMS lỗi sau khi Q-56 được trả lời |
| P04 | UC-003 (chưa có đặc tả) | P07 UC-002 dùng kết quả "thành công hoặc không thành công" và tổng tiền theo P04 UC-002, P02, P03 để đặt message payTickets (3.1.9) tới control tạm AC-C-PayTicketOnlineController | Chạy P04 UC-003, rồi P07 UC-003 với đúng mã AC-C-PayTicketOnlineController; rà lại message 3.1.9 và luồng 10a |

## Vấn đề còn mở

- Target (ngưỡng F5) không đạt cho SD1: luồng chính một mình đã có 46 dòng message (41 không tính trả về), vượt ngưỡng khoảng 30 của một trang. Prompt chỉ cho tách luồng thay thế sang trang riêng, không nêu cách tách chính luồng chính; giữ nguyên một trang để communication diagram cùng phạm vi với SD1.
- Chạy khi chưa có P04 và P07 của UC-003: AC-C-PayTicketOnlineController là mã tạm; kết quả trả về của message 3.1.9 lấy theo P04 UC-002 bước 10, 10a. Cần chạy P07 của UC-003 với đúng mã này.
- Chọn giữa hai quy tắc (C9): F3.2 chỉ cho các giá trị Kết luận đã liệt kê; điều kiện định dạng số điện thoại và ngày hiện tại (ASM-15) không thuộc BR nên ghi "Loại - tham số của quy tắc ASM-15", ngoài danh sách giá trị.
- Chọn giữa hai quy tắc (C9): F5 cho vẽ luồng thay thế ngắn cùng sơ đồ bằng fragment nhưng chỉ cho tối đa 3 fragment ngoài cùng mỗi trang. Đã gộp 9a, 10a vào SD1 (3 fragment ngoài cùng), tách 2a, 4a sang SD2 và 6a, 6b, 7a, 7b sang SD3; communication diagram chỉ gồm SD1.
- Chọn giữa hai quy tắc (C9): boundary được kiểm tra hình thức dữ liệu nhập (bắt buộc, định dạng) nhưng đặc tả đặt bước 7 sau bước 6 và Q-34 xác định thứ tự báo lỗi, nên việc kiểm tra thông tin người đi (validateTravelerInfo) giao cho Booking thay vì BookTicketForm.
- Luồng 9a vẽ bằng fragment break đặt trước message gọi UC-003 theo thứ tự bước của P04, trong khi thời hạn giữ chỗ chạy cả khi UC-003 đang thực hiện (P04 Mục 8). Sơ đồ chưa thể hiện việc ngắt UC-003; đã ghi đề xuất sửa P04.
- Mốc thời gian phụ thuộc dữ liệu (A2): UC-006 Huỷ đặt chỗ qua điện thoại quá hạn tính từ giờ xuất bến và đặt chỗ qua điện thoại do UC-004 tạo; UC-014 Chuẩn bị danh sách hành khách của chuyến tính từ giờ xuất bến của chuyến do UC-012 xếp. UC-002 không tạo hay đổi mốc của hai use case này nên không có message hẹn mốc. Vé UC-002 phát hành sau mốc 15 phút của UC-014 chờ Q-11.
- Target 14 đạt một phần: C7.3 yêu cầu không có hai node chồng nhau và cạnh không cắt qua node, nhưng trong sequence diagram message đi qua các lifeline ở giữa và fragment phủ lên lifeline theo ký pháp UML (F10). Các file communication và VOPC thoả C7.3 (đã kiểm tra khoảng cách tối thiểu 40, cạnh không cắt node, toạ độ bội số 10).
- Route, BaseFare, HolidaySurcharge mỗi lớp chỉ có một trách nhiệm hành vi trong use case này (kiểm tra khớp, tính giá, xác định mức tăng). P08 sẽ gộp thêm trách nhiệm từ UC-001, UC-016, UC-017 khi các use case đó được phân tích.

