# P02 - Danh sách use case - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02 |
| Phiên bản | 1.1 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; yeu-cau-xe-khach.md (bản hiện có); P02-usecases.md 1.0; P02R-review.md 1.0 (áp dụng UCR-01, UCR-02, UCR-03, UCR-04) |
| Phạm vi | Toàn hệ thống |

## 1. Danh sách mục tiêu tác nhân

| ACT | Mục tiêu | Mức mục tiêu dự kiến (Summary / User-goal / Subfunction) | REQ | CAND |
|---|---|---|---|---|
| ACT-01 Hành khách | Tìm chuyến và xem chỗ trống của chuyến | User-goal | REQ-05, REQ-06 | CAND-01 |
| ACT-01 | Đặt và thanh toán vé trực tuyến cho người đi | User-goal | REQ-03, REQ-07, REQ-08, REQ-09, REQ-12, REQ-13, REQ-14, REQ-16, REQ-17, REQ-19 | CAND-02 |
| ACT-01 | Có tài khoản và xem lại lịch sử vé | Summary | REQ-10, REQ-11 | CAND-03 |
| ACT-01 | Đăng ký tài khoản bằng số điện thoại | User-goal | REQ-10 | CAND-04 |
| ACT-01 | Xem lại lịch sử vé | User-goal | REQ-11 | CAND-05 |
| ACT-01 | Đăng nhập vào tài khoản | Subfunction | REQ-10, REQ-11 | CAND-06 |
| ACT-01 | Đổi vé đã mua trực tuyến, trả chênh lệch qua cổng thanh toán khi vé mới đắt hơn (ASM-02, ASM-10) | User-goal | REQ-30, REQ-37, REQ-38, REQ-39, REQ-40 | CAND-07 |
| ACT-01 | Trả vé đã mua trực tuyến và nhận tiền hoàn (ASM-02) | User-goal | REQ-29, REQ-31, REQ-32, REQ-33, REQ-34 | CAND-08 |
| ACT-02 Nhân viên bán vé | Bán vé cho khách mua trực tiếp, thu tiền mặt, in vé giấy | User-goal | REQ-21, REQ-22, REQ-23 | CAND-09 |
| ACT-02 | Nhận đặt chỗ qua điện thoại | User-goal | REQ-25 | CAND-10 |
| ACT-02 | Thu tiền tại quầy cho đặt chỗ qua điện thoại | User-goal | REQ-26, REQ-27 | CAND-11 |
| ACT-02 | Đổi vé mua tại quầy cho khách (ASM-02) | User-goal | REQ-30, REQ-37, REQ-38, REQ-39, REQ-40 | CAND-12 |
| ACT-02 | Trả vé mua tại quầy và chi tiền hoàn cho khách (ASM-02) | User-goal | REQ-29, REQ-31, REQ-32, REQ-33, REQ-36 | CAND-13 |
| ACT-03 Nhân viên điều hành | Quản lý chuyến của nhà xe | Summary | REQ-41, REQ-47 | CAND-14 |
| ACT-03 | Xếp các chuyến vào lịch chạy của tuần | User-goal | REQ-41, REQ-42, REQ-43, REQ-44, REQ-45, REQ-46 | CAND-15 |
| ACT-03 | Huỷ chuyến không chạy được | User-goal | REQ-47, REQ-48, REQ-49, REQ-50 | CAND-16 |
| ACT-04 Quản lý nhà xe | Đặt giá vé theo tuyến và loại xe | User-goal | REQ-51, REQ-52 | CAND-17 |
| ACT-04 | Đặt mức tăng giá cho dịp lễ, Tết | User-goal | REQ-53, REQ-54 | CAND-18 |
| ACT-04 | Xem doanh thu theo ngày, theo tuyến | User-goal | REQ-63, REQ-64 | CAND-19 |
| ACT-04 | Xem tỉ lệ lấp đầy chỗ của từng chuyến | User-goal | REQ-65 | CAND-20 |
| ACT-05 Phụ xe | Soát vé hành khách lên xe | User-goal | REQ-55, REQ-57, REQ-58, REQ-59, REQ-60 | CAND-21 |
| ACT-10 Bộ định thời | Kích hoạt huỷ đặt chỗ qua điện thoại chưa thanh toán khi đến 60 phút trước giờ xuất bến | User-goal | REQ-27, REQ-28 | CAND-22 |
| ACT-10 | Kích hoạt gửi danh sách hành khách của chuyến về máy soát vé khi đến 15 phút trước giờ xuất bến | User-goal | REQ-61, REQ-62 | CAND-23 |

## 2. Danh sách sự kiện

| EV | Sự kiện | Loại (Nghiệp vụ / Thời gian / Hệ thống ngoài / Thiết bị) | Nguồn phát (ACT) | Phản hồi mong đợi của hệ thống | REQ | CAND |
|---|---|---|---|---|---|---|
| EV-01 | Hành khách muốn biết có chuyến nào và chỗ nào còn trống | Nghiệp vụ | ACT-01 | Cho biết các chuyến khớp điểm đi, điểm đến, ngày đi và sơ đồ chỗ còn trống của chuyến | REQ-05, REQ-06 | CAND-01 |
| EV-02 | Hành khách muốn đặt vé cho một chuyến | Nghiệp vụ | ACT-01 | Giữ chỗ đã chọn, thu tiền qua cổng thanh toán, phát hành vé và gửi vé qua SMS | REQ-03, REQ-07, REQ-08, REQ-09, REQ-12, REQ-14, REQ-17, REQ-19 | CAND-02 |
| EV-03 | Hết 10 phút giữ chỗ mà chưa thanh toán thành công | Thời gian | - | Trả các chỗ đang giữ cho người khác chọn | REQ-13, REQ-16 | CAND-24 |
| EV-04 | Cổng thanh toán trả kết quả thanh toán | Hệ thống ngoài | ACT-06 | Ghi nhận kết quả; thành công thì phát hành vé, không thành công thì báo cho hành khách | REQ-14, REQ-15, REQ-17 | CAND-25 |
| EV-05 | Khách gọi điện tới quầy để đặt chỗ | Nghiệp vụ | ACT-02 | Ghi nhận đặt chỗ, giữ chỗ tới hạn thanh toán (ASM-05) | REQ-25 | CAND-10 |
| EV-06 | Khách tới quầy mua vé trực tiếp | Nghiệp vụ | ACT-02 | Bán vé, ghi nhận tiền mặt, in vé giấy có mã vạch | REQ-21, REQ-22, REQ-23, REQ-24 | CAND-09 |
| EV-07 | Khách đã đặt chỗ qua điện thoại tới quầy thanh toán | Nghiệp vụ | ACT-02 | Ghi nhận thanh toán nếu còn trong hạn, phát hành vé | REQ-26, REQ-27 | CAND-11 |
| EV-08 | Đến 60 phút trước giờ xuất bến của một chuyến | Thời gian | ACT-10 | Huỷ đặt chỗ qua điện thoại chưa thanh toán của chuyến, trả chỗ về trạng thái còn trống | REQ-27, REQ-28 | CAND-22 |
| EV-09 | Hành khách muốn đổi vé đã mua trực tuyến | Nghiệp vụ | ACT-01 | Đổi vé sang chuyến khác cùng tuyến, thu phần chênh lệch qua cổng thanh toán nếu vé mới đắt hơn (ASM-10) | REQ-30, REQ-37, REQ-38, REQ-39, REQ-40 | CAND-07 |
| EV-10 | Khách mang vé mua tại quầy tới quầy để đổi | Nghiệp vụ | ACT-02 | Đổi vé sang chuyến khác cùng tuyến, thu phần chênh lệch nếu vé mới đắt hơn | REQ-30, REQ-37, REQ-38, REQ-39, REQ-40 | CAND-12 |
| EV-11 | Hành khách muốn trả vé đã mua trực tuyến | Nghiệp vụ | ACT-01 | Huỷ vé, tính mức hoàn, hoàn tiền qua cổng thanh toán | REQ-29, REQ-31, REQ-32, REQ-33, REQ-34, REQ-35 | CAND-08 |
| EV-12 | Khách mang vé mua tại quầy tới quầy để trả | Nghiệp vụ | ACT-02 | Huỷ vé, tính mức hoàn để nhân viên chi tiền mặt | REQ-29, REQ-31, REQ-32, REQ-33, REQ-36 | CAND-13 |
| EV-13 | Hành khách muốn có tài khoản để xem lại lịch sử vé | Nghiệp vụ | ACT-01 | Tạo tài khoản gắn với số điện thoại | REQ-10 | CAND-04 |
| EV-14 | Hành khách có tài khoản muốn dùng chức năng cần tài khoản | Nghiệp vụ | ACT-01 | Xác thực và nhận diện chủ tài khoản | REQ-10, REQ-11 | CAND-06 |
| EV-15 | Hành khách muốn xem lại các vé đã mua | Nghiệp vụ | ACT-01 | Cho xem lịch sử vé của tài khoản | REQ-11 | CAND-05 |
| EV-16 | Nhà xe cần xếp chuyến vào lịch chạy của tuần | Nghiệp vụ | ACT-03 | Ghi nhận các chuyến đã xếp vào lịch chạy của tuần, từ chối xếp vi phạm chồng chuyến hoặc giờ lái | REQ-41, REQ-42, REQ-43, REQ-44, REQ-45 | CAND-15 |
| EV-17 | Chuyến không chạy được do xe hỏng hoặc thời tiết | Nghiệp vụ | ACT-03 | Huỷ chuyến, gửi SMS và hoàn 100% giá vé cho mọi hành khách đã có vé | REQ-47, REQ-48, REQ-49, REQ-50 | CAND-16 |
| EV-18 | Đến 15 phút trước giờ xuất bến của một chuyến | Thời gian | ACT-10 | Gửi danh sách hành khách của chuyến về máy soát vé | REQ-61, REQ-62 | CAND-23 |
| EV-19 | Hành khách lên xe xuất trình vé, phụ xe quét mã vé | Nghiệp vụ | ACT-05 | Báo vé hợp lệ hoặc không hợp lệ, ghi nhận vé đã soát | REQ-55, REQ-57, REQ-58 | CAND-21 |
| EV-20 | Quản lý nhà xe quyết định giá vé cho tuyến và loại xe | Nghiệp vụ | ACT-04 | Ghi nhận giá vé áp dụng | REQ-51, REQ-52 | CAND-17 |
| EV-21 | Sắp tới dịp lễ, Tết | Nghiệp vụ | ACT-04 | Ghi nhận mức tăng giá theo phần trăm cho khoảng ngày | REQ-53, REQ-54 | CAND-18 |
| EV-22 | Quản lý nhà xe cần theo dõi doanh thu và mức lấp đầy | Nghiệp vụ | ACT-04 | Lập báo cáo doanh thu và tỉ lệ lấp đầy | REQ-63, REQ-64, REQ-65 | CAND-19, CAND-20 |

## 3. Bảng ứng viên use case

| CAND | Ứng viên | Kết luận | Phép thử không đạt | Lý do | REQ | Nguồn phát hiện |
|---|---|---|---|---|---|---|
| CAND-01 | Tìm chuyến và xem chỗ trống của chuyến | Giữ thành UC-001 | - | U-R05 và U-R17: mục tiêu thông tin độc lập của hành khách, nguồn nêu riêng việc "tìm chuyến và xem chỗ trống không cần tài khoản" (Mục 1, câu 3), giữ theo ASM-08. | REQ-05, REQ-06 | Mục tiêu; Sự kiện EV-01 |
| CAND-02 | Đặt và thanh toán vé trực tuyến | Giữ thành UC-002 | - | Mục tiêu trọn vẹn trong một phiên (chỗ giữ 10 phút để thanh toán), U-R10 a so với CAND-09 và CAND-10 vì kết quả khác (vé phát hành và gửi qua SMS). | REQ-03, REQ-07, REQ-08, REQ-09, REQ-12, REQ-13, REQ-16, REQ-17, REQ-18, REQ-19 | Mục tiêu; Sự kiện EV-02; Động từ ("đặt vé", Mục 1, câu 1) |
| CAND-03 | Đăng ký tài khoản và xem lại lịch sử vé | Tách thành CAND-04, CAND-05 | U-T1, U-T6, U-AP05 | Hai việc ở hai thời điểm khác nhau: đăng ký một lần, xem lịch sử vé nhiều lần về sau. | REQ-10, REQ-11 | Mục tiêu |
| CAND-04 | Đăng ký tài khoản bằng số điện thoại | Giữ thành UC-009 | - | U-R03: UC User-goal của hành khách chưa có tài khoản. | REQ-10 | Mục tiêu; Sự kiện EV-13 |
| CAND-05 | Xem lại lịch sử vé | Giữ thành UC-011 | - | U-R05: hành khách tự tìm tới hệ thống để lấy thông tin các vé đã mua. | REQ-11 | Mục tiêu; Sự kiện EV-15 |
| CAND-06 | Đăng nhập | Giữ thành UC-010 | - | U-R01: nguồn nhắc "tài khoản" của hành khách (Mục 2, câu 2) nên chỉ nối ACT-01; nhân viên nhà xe ghi ASM-09, chưa nối. | REQ-10, REQ-11 | Mục tiêu; Sự kiện EV-14 |
| CAND-07 | Đổi vé mua trực tuyến | Giữ thành UC-007 | - | U-R10 b với CAND-12: cùng mục tiêu, khác biệt chỉ ở bước tìm vé của khách và cách thu chênh lệch, một UC cho ACT-01 và ACT-02 (ASM-02, ASM-10); nhánh trả chênh lệch của vé mua trực tuyến dùng UC-003 (UCR-01). | REQ-30, REQ-37, REQ-38, REQ-39, REQ-40 | Mục tiêu; Sự kiện EV-09 |
| CAND-08 | Trả vé mua trực tuyến | Giữ thành UC-008 | - | U-R10 b với CAND-13: cùng mục tiêu và cùng quy tắc mức hoàn, khác biệt chỉ ở kênh hoàn tiền (một bước), một UC cho ACT-01 và ACT-02 (ASM-02). | REQ-29, REQ-31, REQ-32, REQ-33, REQ-34, REQ-35 | Mục tiêu; Sự kiện EV-11 |
| CAND-09 | Bán vé tại quầy và in vé giấy | Giữ thành UC-005 | - | U-R10 a so với CAND-02: luồng của nhân viên bán vé có đoạn tương tác riêng thu tiền mặt và in vé giấy có mã vạch, kết quả là vé giấy đã thanh toán ngay. | REQ-21, REQ-22, REQ-23, REQ-24 | Mục tiêu; Sự kiện EV-06; Động từ |
| CAND-10 | Nhận đặt chỗ qua điện thoại | Giữ thành UC-004 | - | U-R10 a so với CAND-02: kết quả khác, chỗ được giữ chưa thanh toán tới hạn 60 phút trước giờ xuất bến (ASM-05) thay vì vé đã phát hành. | REQ-25 | Mục tiêu; Sự kiện EV-05; Động từ |
| CAND-11 | Thu tiền tại quầy cho đặt chỗ qua điện thoại | Gộp vào UC-005 | U-T11, U-AP15 | U-R12: cùng tác nhân, cùng kết quả vé đã thanh toán tại quầy như bán vé tại quầy, chỉ khác là có đặt chỗ trước (như "nhận phòng có đặt trước hay khách vãng lai"), thành luồng thay thế. | REQ-26, REQ-27 | Mục tiêu; Sự kiện EV-07 |
| CAND-12 | Đổi vé mua tại quầy cho khách | Gộp vào UC-007 | U-T11, U-AP12 | U-R10 b: nhân viên bán vé làm thay khách cùng mục tiêu đổi vé, khác biệt thành luồng thay thế ở P04. | REQ-30, REQ-37, REQ-38, REQ-39, REQ-40 | Mục tiêu; Sự kiện EV-10 |
| CAND-13 | Trả vé mua tại quầy cho khách | Gộp vào UC-008 | U-T11, U-AP12 | U-R10 b: nhân viên bán vé làm thay khách cùng mục tiêu trả vé, hoàn tiền mặt tại quầy là luồng thay thế. | REQ-29, REQ-31, REQ-32, REQ-33, REQ-36 | Mục tiêu; Sự kiện EV-12 |
| CAND-14 | Quản lý chuyến | Tách thành CAND-15, CAND-16 | U-T1, U-T6, U-AP04 | Tên cả một mảng nghiệp vụ ("quản lý chuyến", Đoạn mở đầu, câu 4) gồm lập lịch và huỷ chuyến ở các thời điểm khác nhau. | REQ-41, REQ-47 | Mục tiêu; Động từ |
| CAND-15 | Lập lịch chạy theo tuần | Giữ thành UC-012 | - | U-R14: chọn tuyến, giờ xuất bến, xe, tài xế cho từng chuyến là vòng lặp trong một UC; mỗi lần làm việc là một lần thực hiện theo ASM-11, nên tên và mục tiêu nêu kết quả của một lần làm việc (U-N3, UCR-03). | REQ-41, REQ-42, REQ-43, REQ-44, REQ-45, REQ-46 | Mục tiêu; Sự kiện EV-16 |
| CAND-16 | Huỷ chuyến | Giữ thành UC-013 | - | Giao dịch nghiệp vụ của nhân viên điều hành phản hồi sự kiện xe hỏng, thời tiết; gửi SMS và hoàn tiền là bước của UC (U-R06, U-R08). | REQ-47, REQ-48, REQ-49, REQ-50 | Mục tiêu; Sự kiện EV-17 |
| CAND-17 | Đặt giá vé theo tuyến và loại xe | Giữ thành UC-016 | - | U-R15: tham số nghiệp vụ do quản lý nhà xe thiết lập; U-R04: nguồn chỉ nêu thao tác "đặt" nên không dùng tên "Quản lý". | REQ-51, REQ-52 | Mục tiêu; Sự kiện EV-20 |
| CAND-18 | Đặt mức tăng giá ngày lễ, Tết | Giữ thành UC-017 | - | U-R04 d và U-R15: dữ liệu khác bảng giá, có quy tắc riêng (tối đa 30%) và thời điểm riêng (trước dịp lễ, Tết), không gộp với CAND-17. | REQ-53, REQ-54 | Mục tiêu; Sự kiện EV-21 |
| CAND-19 | Xem báo cáo doanh thu | Giữ thành UC-018 | - | U-R05: báo cáo doanh thu theo ngày, theo tuyến và tỉ lệ lấp đầy cùng tác nhân, cùng cách thao tác, gộp thành một UC. | REQ-63, REQ-64 | Mục tiêu; Sự kiện EV-22 |
| CAND-20 | Xem tỉ lệ lấp đầy chỗ của chuyến | Gộp vào UC-018 | U-T11, U-AP12 | U-R05: cùng tác nhân và cách thao tác với CAND-19, chỉ khác nội dung dữ liệu. | REQ-65 | Mục tiêu; Sự kiện EV-22 |
| CAND-21 | Soát vé khi hành khách lên xe | Giữ thành UC-015 | - | U-R18: phụ xe là tác nhân chính, ACT-09 Đầu quét mã vạch là tác nhân phụ; U-R14: quét từng vé là vòng lặp trong phiên soát vé của một chuyến. | REQ-55, REQ-57, REQ-58, REQ-59, REQ-60 | Mục tiêu; Sự kiện EV-19; Động từ |
| CAND-22 | Huỷ đặt chỗ qua điện thoại chưa thanh toán khi tới hạn | Giữ thành UC-006 | - | U-R07: nguồn nêu mốc 60 phút trước giờ xuất bến, không người ra lệnh ("tự động bị huỷ"), giải phóng chỗ cho khách khác, không phiên nào đang mở; tên dùng thuật ngữ "đặt chỗ" như UC-004 (U-N4, UCR-02). | REQ-27, REQ-28 | Mục tiêu; Sự kiện EV-08; Động từ |
| CAND-23 | Gửi danh sách hành khách của chuyến về máy soát vé | Giữ thành UC-014 | - | U-R07 (ưu tiên hơn Q1): mốc 15 phút trước giờ xuất bến, không người ra lệnh, giá trị cho phụ xe là soát được vé cả khi mất sóng; tên dùng thuật ngữ nguồn "danh sách hành khách của chuyến" (U-N4, UCR-04); xem Vấn đề còn mở về U-T9. | REQ-61, REQ-62 | Mục tiêu; Sự kiện EV-18; Động từ |
| CAND-24 | Trả lại chỗ đang giữ khi hết 10 phút chưa thanh toán | Là bước của UC-002 | U-T8, U-AP11 | U-R07 hết giờ trong phiên: hành khách vẫn đang ở phiên đặt vé chờ thanh toán. | REQ-13, REQ-16 | Sự kiện EV-03; Động từ |
| CAND-25 | Ghi nhận kết quả thanh toán do cổng thanh toán trả về | Là bước của UC-003 | U-T1, U-T9 | U-R08: phản hồi trong cùng phiên thanh toán (ASM-07); trường hợp kết quả đến sau khi hết thời hạn giữ chỗ chờ Q-10. | REQ-14, REQ-15, REQ-17 | Sự kiện EV-04 |
| CAND-26 | Xem sơ đồ chỗ của chuyến | Gộp vào UC-001 | U-T1, U-AP01 | U-R05: tìm kiếm rồi xem chi tiết là một UC, không tách "Tìm" và "Xem chi tiết". | REQ-06 | Động từ |
| CAND-27 | Chọn chỗ, tối đa 5 chỗ một lần đặt | Là bước của UC-002 | U-T1, U-T4, U-AP01 | Thao tác đơn trong luồng đặt vé, không có kết quả trọn vẹn; giới hạn 5 chỗ là quy tắc của UC-002. | REQ-07, REQ-08 | Động từ |
| CAND-28 | Nhập họ tên và số điện thoại người đi | Là bước của UC-002 | U-T1, U-T4, U-AP01 | Dữ liệu cho bước sau, không có kết quả riêng. | REQ-09 | Động từ |
| CAND-29 | Giữ các chỗ đã chọn | Là bước của UC-002 | U-T9, U-AP03 | U-R09: hệ thống tự làm như hệ quả của việc đặt vé. | REQ-12, REQ-13 | Động từ |
| CAND-30 | Thanh toán vé qua cổng thanh toán trực tuyến | Giữ thành UC-003 | - | Subfunction giữ theo Q4 d: kết quả riêng là khoản tiền được cổng xác nhận; nguồn mô tả tách bạch (cổng của đối tác, trường hợp "chưa thanh toán thành công"); thất bại trong thời hạn giữ chỗ không huỷ lần đặt. Thêm Q4 a: dùng lại ở UC-002 và nhánh trả chênh lệch vé mua trực tuyến của UC-007 (ASM-10, UCR-01). | REQ-13, REQ-14, REQ-15, REQ-40 | Động từ |
| CAND-31 | Phát hành vé, mỗi chỗ một mã vé | Là bước của UC-002 | U-T9, U-AP03 | U-R09: hệ thống phát hành vé như hệ quả của thanh toán thành công. | REQ-17, REQ-18 | Động từ |
| CAND-32 | Gửi vé qua SMS tới số điện thoại người đi | Là bước của UC-002 | U-T9, U-AP03 | U-R06: thông báo là hệ quả của đặt vé, ACT-07 Cổng SMS là tác nhân phụ. | REQ-19, REQ-20 | Động từ |
| CAND-33 | Thu tiền mặt | Là bước của UC-005 | U-T1, U-T4, U-AP01 | Một bước trong luồng bán vé tại quầy. | REQ-22 | Động từ |
| CAND-34 | In vé giấy có mã vạch | Là bước của UC-005 | U-T1, U-T4, U-AP01 | Một bước trong luồng bán vé tại quầy, ACT-08 Máy in vé là tác nhân phụ. | REQ-23, REQ-24 | Động từ |
| CAND-35 | Đổi hoặc trả vé | Tách thành CAND-07, CAND-08 | U-T1, U-T2 | Hai mục tiêu khác nhau, mỗi mục tiêu có quy tắc nghiệp vụ riêng lớn (REQ-31 đến REQ-36; REQ-37 đến REQ-40), tách theo Bước 7.2. | REQ-29, REQ-30 | Động từ |
| CAND-36 | Hoàn tiền vé mua trực tuyến qua cổng thanh toán | Là bước của UC-008 | U-T9, U-AP03 | U-R08: lời gọi tới ACT-06 để hoàn tất việc trả vé. | REQ-34, REQ-35 | Động từ |
| CAND-37 | Hoàn tiền mặt tại quầy | Là bước của UC-008 | U-T1, U-T4, U-AP01 | Bước của luồng nhân viên bán vé nhận trả vé mua tại quầy (U-R10 b). | REQ-36 | Động từ |
| CAND-38 | Trả thêm phần chênh lệch khi đổi vé | Là bước của UC-007 | U-T1, U-T4, U-AP01 | Bước có điều kiện của đổi vé; kênh thanh toán theo ASM-10: vé mua trực tuyến trả qua UC-003 (UCR-01), vé mua tại quầy trả tiền mặt tại quầy. | REQ-40 | Động từ |
| CAND-39 | Chọn tuyến, giờ xuất bến, xe và tài xế cho chuyến | Là bước của UC-012 | U-T1, U-AP01 | U-R14: bước lặp cho từng chuyến khi lập lịch. | REQ-42 | Động từ |
| CAND-40 | Kiểm tra xe, tài xế chồng chuyến và giới hạn 10 giờ lái | Là bước của UC-012 | U-T9, U-AP03 | Kiểm tra hợp lệ nội bộ khi xếp chuyến (ASM-03); quy tắc chuyển P06. | REQ-43, REQ-44, REQ-45, REQ-46 | Động từ |
| CAND-41 | Gửi SMS cho hành khách của chuyến bị huỷ | Là bước của UC-013 | U-T9, U-AP03 | U-R06: hệ quả của huỷ chuyến, ACT-07 là tác nhân phụ, người đi là bên hưởng lợi. | REQ-20, REQ-48 | Động từ |
| CAND-42 | Hoàn 100% giá vé cho hành khách của chuyến bị huỷ | Là bước của UC-013 | U-T9, U-AP03 | U-R08 và U-R09: hệ quả của huỷ chuyến, vé mua trực tuyến hoàn qua ACT-06. | REQ-49, REQ-50 | Động từ |
| CAND-43 | Hoàn tiền mặt tại quầy cho vé mua tại quầy của chuyến bị huỷ | Chờ Q-14 | U-T10 | Q-14 trả lời "Có" thì có hành vi chi tiền mặt tại quầy của ACT-02, xét lại thành luồng thay thế của UC-008 hoặc UC riêng; "Không" thì Loại. | REQ-36, REQ-49 | Động từ |
| CAND-44 | Báo vé hợp lệ hoặc không hợp lệ khi soát | Là bước của UC-015 | U-T9, U-AP03 | Phản hồi của ứng dụng soát vé sau mỗi lần quét. | REQ-57, REQ-58 | Động từ |
| CAND-45 | Soát vé khi xe ở vùng mất sóng | Là bước của UC-015 | U-T9 | Cách hoạt động khi mất sóng là luồng thay thế của soát vé; phần ràng buộc chất lượng chuyển P06. | REQ-59 | Động từ |
| CAND-46 | Gửi lại kết quả soát vé khi có sóng | Là bước của UC-015 | U-T8, U-T9, U-AP11 | U-R09: đồng bộ nội bộ giữa ứng dụng soát vé và hệ thống (ASM-01), hệ quả của soát vé, không có tác nhân hay mốc thời gian. | REQ-60 | Động từ |
| CAND-47 | Cập nhật danh mục tuyến (kể cả thời gian chạy dự kiến) | Chờ Q-03 | U-T10 | U-R16: P00 để chức năng này chờ Q-03; trả lời (a) hoặc (b) thì thành UC "Quản lý danh mục tuyến" của tác nhân tương ứng theo U-R04, (c) thì Loại. | REQ-42, REQ-46 | Động từ |
| CAND-48 | Cập nhật danh mục xe | Chờ Q-03 | U-T10 | U-R16: P00 để chức năng này chờ Q-03; trả lời (a) hoặc (b) thì thành UC "Quản lý danh mục xe" theo U-R04, (c) thì Loại. | REQ-42, REQ-43 | Động từ |
| CAND-49 | Cập nhật danh mục tài xế | Chờ Q-03 | U-T10 | U-R16: P00 để chức năng này chờ Q-03; trả lời (a) hoặc (b) thì thành UC "Quản lý danh mục tài xế" theo U-R04, (c) thì Loại. | REQ-42, REQ-44, REQ-45 | Động từ |

## 4. Bảng use case

### Bảng 4a. Bảng lõi

| UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mức | Nhóm chức năng |
|---|---|---|---|---|---|---|
| UC-001 | Tra cứu chuyến xe | Search Trips | ACT-01 Hành khách | - | User-goal | Bán vé |
| UC-002 | Đặt vé trực tuyến | Book Ticket Online | ACT-01 | ACT-07 Cổng SMS | User-goal | Bán vé |
| UC-003 | Thanh toán vé trực tuyến | Pay Ticket Online | ACT-01 (qua UC-002, UC-007) | ACT-06 Cổng thanh toán | Subfunction | Bán vé |
| UC-004 | Nhận đặt chỗ qua điện thoại | Take Phone Reservation | ACT-02 Nhân viên bán vé | - | User-goal | Bán vé |
| UC-005 | Bán vé tại quầy | Sell Ticket At Counter | ACT-02 | ACT-08 Máy in vé | User-goal | Bán vé |
| UC-006 | Huỷ đặt chỗ qua điện thoại quá hạn | Cancel Overdue Phone Reservation | ACT-10 Bộ định thời | - | User-goal | Bán vé |
| UC-007 | Đổi vé | Exchange Ticket | ACT-01, ACT-02 | - | User-goal | Bán vé |
| UC-008 | Trả vé | Return Ticket | ACT-01, ACT-02 | ACT-06 | User-goal | Bán vé |
| UC-009 | Đăng ký tài khoản | Register Account | ACT-01 | - | User-goal | Tài khoản hành khách |
| UC-010 | Đăng nhập | Log In | ACT-01 | - | Subfunction | Tài khoản hành khách |
| UC-011 | Xem lịch sử vé | View Ticket History | ACT-01 | - | User-goal | Tài khoản hành khách |
| UC-012 | Xếp chuyến vào lịch chạy tuần | Schedule Weekly Trips | ACT-03 Nhân viên điều hành | - | User-goal | Vận hành chuyến |
| UC-013 | Huỷ chuyến | Cancel Trip | ACT-03 | ACT-06, ACT-07 | User-goal | Vận hành chuyến |
| UC-014 | Chuẩn bị danh sách hành khách của chuyến | Prepare Trip Passenger List | ACT-10 | - | User-goal | Vận hành chuyến |
| UC-015 | Soát vé lên xe | Check Boarding Ticket | ACT-05 Phụ xe | ACT-09 Đầu quét mã vạch | User-goal | Vận hành chuyến |
| UC-016 | Đặt giá vé | Set Ticket Fare | ACT-04 Quản lý nhà xe | - | User-goal | Giá vé và báo cáo |
| UC-017 | Đặt mức tăng giá lễ Tết | Set Holiday Price Increase | ACT-04 | - | User-goal | Giá vé và báo cáo |
| UC-018 | Xem báo cáo kinh doanh | View Business Reports | ACT-04 | - | User-goal | Giá vé và báo cáo |

### Bảng 4b. Bảng mô tả

| UC | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | REQ | CAND nguồn |
|---|---|---|---|---|---|
| UC-001 | Hành khách biết các chuyến khớp điểm đi, điểm đến, ngày đi và các chỗ còn trống của chuyến đã chọn. | Hành khách tìm chuyến theo điểm đi, điểm đến và ngày đi rồi xem sơ đồ chỗ của một chuyến với các chỗ còn trống, không cần tài khoản. UC được giữ như mục tiêu thông tin độc lập (ASM-08); phần tìm chuyến cũng là đoạn mở đầu của UC-002. | Hành khách muốn biết có chuyến nào và chỗ nào còn trống (EV-01) | REQ-04, REQ-05, REQ-06 | CAND-01, CAND-26 |
| UC-002 | Hành khách có vé đã phát hành cho các chỗ đã chọn, mỗi chỗ một mã vé, và người đi nhận được vé qua SMS. | Hành khách chọn chuyến và tối đa 5 chỗ, nhập họ tên và số điện thoại người đi, được giữ chỗ 10 phút để thanh toán (UC-003); thanh toán thành công thì vé được phát hành và gửi qua SMS. Không bắt buộc có tài khoản. Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại (luồng thay thế, U-R07 hết giờ trong phiên). | Hành khách muốn đặt vé cho một chuyến (EV-02) | REQ-03, REQ-04, REQ-05, REQ-06, REQ-07, REQ-08, REQ-09, REQ-12, REQ-13, REQ-16, REQ-17, REQ-18, REQ-19, REQ-20, REQ-67 | CAND-02 |
| UC-003 | Hành khách có khoản thanh toán trực tuyến được cổng thanh toán xác nhận. | Hành khách thanh toán một khoản tiền qua cổng thanh toán trực tuyến của đối tác: tiền vé các chỗ đang giữ trong UC-002, hoặc phần chênh lệch khi đổi vé mua trực tuyến sang vé đắt hơn trong UC-007 (ASM-10). Thanh toán không thành công thì UC gọi chưa bị huỷ; thời hạn giữ chỗ 10 phút thuộc UC-002. Giữ theo Q4 d (kết quả riêng là khoản tiền được cổng xác nhận, nguồn mô tả tách bạch cổng của đối tác và trường hợp chưa thanh toán thành công, thất bại không huỷ ngay mục tiêu cha) và Q4 a (dùng lại ở UC-002 và UC-007). | Được gọi từ UC-002 khi các chỗ đã được giữ (EV-02); được gọi từ UC-007 khi vé mới của vé mua trực tuyến đắt hơn vé cũ (EV-09) | REQ-14, REQ-15, REQ-40, REQ-68 | CAND-30 |
| UC-004 | Nhân viên bán vé có chỗ được giữ trên chuyến cho khách gọi điện, chờ khách thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến. | Nhân viên bán vé tìm chuyến, chọn chỗ theo yêu cầu của khách gọi điện và ghi nhận đặt chỗ; chỗ được giữ tới khi được thanh toán hoặc bị tự động huỷ (ASM-05). Tách khỏi UC-002 theo U-R10 a vì kết quả khác (chỗ giữ chưa thanh toán thay vì vé đã phát hành). | Khách gọi điện tới quầy để đặt chỗ (EV-05) | REQ-25, REQ-27, REQ-67 | CAND-10 |
| UC-005 | Nhân viên bán vé hoàn tất việc bán vé: vé đã được thanh toán tại quầy và in thành vé giấy có mã vạch cho khách. | Nhân viên bán vé chọn chuyến và chỗ cho khách mua trực tiếp, thu tiền mặt và in vé giấy có mã vạch. Biến thể theo U-R12: khách đã đặt chỗ qua điện thoại (UC-004) tới quầy thanh toán trước hạn 60 phút trước giờ xuất bến, nhân viên tìm đặt chỗ đó thay vì chọn chuyến và chỗ. | Khách tới quầy mua vé trực tiếp (EV-06); khách đã đặt chỗ qua điện thoại tới quầy thanh toán (EV-07) | REQ-18, REQ-21, REQ-22, REQ-23, REQ-24, REQ-26, REQ-27, REQ-67 | CAND-09, CAND-11 |
| UC-006 | Chỗ của đặt chỗ qua điện thoại chưa thanh toán trở lại còn trống để bán cho khách khác khi đến 60 phút trước giờ xuất bến. | Đến 60 phút trước giờ xuất bến của mỗi chuyến, các đặt chỗ qua điện thoại chưa được thanh toán bị huỷ và chỗ trở lại còn trống (ASM-05). Khách đặt chỗ qua điện thoại là bên hưởng lợi gián tiếp, không tương tác với UC. | Đến 60 phút trước giờ xuất bến của một chuyến (EV-08) | REQ-27, REQ-28 | CAND-22 |
| UC-007 | Khách có vé trên chuyến khác cùng tuyến thay cho vé cũ, đã trả phần chênh lệch nếu vé mới đắt hơn. | Hành khách tự đổi vé mua trực tuyến, nhân viên bán vé đổi vé mua tại quầy cho khách (ASM-02); vé chỉ đổi sang chuyến khác cùng tuyến, một lần, chậm nhất 4 giờ trước giờ xuất bến. Phần chênh lệch thanh toán theo kênh mua (ASM-10): vé mua trực tuyến qua UC-003 Thanh toán vé trực tuyến, vé mua tại quầy bằng tiền mặt tại quầy. Một UC cho hai tác nhân chính theo U-R10 b; cách giao vé mới chờ Q-30. | Hành khách muốn đổi vé đã mua trực tuyến (EV-09); khách mang vé mua tại quầy tới quầy để đổi (EV-10) | REQ-30, REQ-37, REQ-38, REQ-39, REQ-40, REQ-67 | CAND-07, CAND-12 |
| UC-008 | Khách đã trả vé và nhận lại 90% hoặc 50% giá vé tuỳ thời điểm trả. | Hành khách tự trả vé mua trực tuyến và được hoàn qua cổng thanh toán; nhân viên bán vé nhận trả vé mua tại quầy và hoàn tiền mặt (ASM-02). Mức hoàn theo thời gian còn lại trước giờ xuất bến, dưới 4 giờ không được trả. Một UC cho hai tác nhân chính theo U-R10 b. | Hành khách muốn trả vé đã mua trực tuyến (EV-11); khách mang vé mua tại quầy tới quầy để trả (EV-12) | REQ-29, REQ-31, REQ-32, REQ-33, REQ-34, REQ-35, REQ-36 | CAND-08, CAND-13 |
| UC-009 | Hành khách có tài khoản gắn với số điện thoại để xem lại lịch sử vé. | Hành khách chưa có tài khoản đăng ký tài khoản bằng số điện thoại (U-R03). Cách xác thực khi dùng tài khoản chờ Q-07. | Hành khách muốn có tài khoản để xem lại lịch sử vé (EV-13) | REQ-10 | CAND-04 |
| UC-010 | Hành khách được nhận diện là chủ tài khoản để dùng các chức năng cần tài khoản. | Hành khách có tài khoản xác thực để dùng UC-011 Xem lịch sử vé; đây là điều kiện để dùng UC khác, ghi ở tiền điều kiện, không nối include (U-R01). Cách xác thực chờ Q-07; nhân viên nhà xe chưa nối theo ASM-09. | Hành khách có tài khoản muốn dùng chức năng cần tài khoản (EV-14) | REQ-10, REQ-11 | CAND-06 |
| UC-011 | Hành khách thấy lại các vé đã mua gắn với tài khoản của mình. | Hành khách đã đăng nhập xem lại lịch sử vé của tài khoản. Phạm vi các vé có trong lịch sử chờ Q-06. | Hành khách muốn xem lại các vé đã mua (EV-15) | REQ-11 | CAND-05 |
| UC-012 | Các chuyến xếp trong lần làm việc có tuyến, giờ xuất bến, xe và tài xế, được ghi vào lịch chạy của tuần và không vi phạm quy tắc chồng chuyến và giờ lái. | Nhân viên điều hành xếp một hoặc nhiều chuyến vào lịch chạy của tuần, chọn tuyến, giờ xuất bến, xe và tài xế (U-R14); xếp làm xe hoặc tài xế chồng thời gian chạy, hoặc làm tài xế lái quá 10 giờ một ngày, bị từ chối (ASM-03). Mỗi lần làm việc là một lần thực hiện UC (ASM-11). | Nhà xe cần xếp chuyến vào lịch chạy của tuần (EV-16) | REQ-41, REQ-42, REQ-43, REQ-44, REQ-45, REQ-46 | CAND-15 |
| UC-013 | Nhân viên điều hành có chuyến đã huỷ, mọi hành khách đã có vé được báo qua SMS và được hoàn 100% giá vé. | Nhân viên điều hành huỷ một chuyến không chạy được (xe hỏng, thời tiết); hệ thống gửi SMS cho mọi hành khách đã có vé và hoàn 100% giá vé, vé mua trực tuyến hoàn qua cổng thanh toán. Hoàn tiền vé mua tại quầy chờ Q-14 (CAND-43); phạm vi "mọi hành khách" chờ Q-15. | Chuyến không chạy được do xe hỏng hoặc thời tiết (EV-17) | REQ-20, REQ-35, REQ-47, REQ-48, REQ-49, REQ-50 | CAND-16 |
| UC-014 | Máy soát vé của chuyến có danh sách hành khách để phụ xe soát vé, kể cả khi mất sóng. | Đến 15 phút trước giờ xuất bến của mỗi chuyến, danh sách hành khách của chuyến được gửi về ứng dụng soát vé trên máy soát vé cầm tay (ASM-01). Phụ xe là bên hưởng lợi. Thay đổi vé sau mốc này chờ Q-11. | Đến 15 phút trước giờ xuất bến của một chuyến (EV-18) | REQ-61, REQ-62 | CAND-23 |
| UC-015 | Phụ xe biết từng vé hành khách xuất trình là hợp lệ hay không hợp lệ, và kết quả soát được ghi nhận. | Phụ xe quét mã vé của từng hành khách lên xe bằng máy soát vé cầm tay (U-R14, U-R18); ứng dụng soát vé báo hợp lệ hoặc không hợp lệ (sai chuyến, vé đã huỷ, vé đã soát). Khi mất sóng vẫn soát được và gửi lại kết quả khi có sóng. Cách đọc vé mua trực tuyến chờ Q-04. | Hành khách lên xe xuất trình vé, phụ xe quét mã vé (EV-19) | REQ-55, REQ-56, REQ-57, REQ-58, REQ-59, REQ-60 | CAND-21 |
| UC-016 | Quản lý nhà xe có giá vé áp dụng cho từng tuyến và loại xe. | Quản lý nhà xe đặt giá vé theo tuyến và loại xe (U-R15). Chỉ gồm thao tác "đặt" mà nguồn nêu (U-R04). | Quản lý nhà xe quyết định giá vé cho tuyến và loại xe (EV-20) | REQ-51, REQ-52 | CAND-17 |
| UC-017 | Quản lý nhà xe có mức tăng giá theo phần trăm, tối đa 30%, áp dụng cho một khoảng ngày lễ, Tết. | Quản lý nhà xe đặt mức tăng giá theo phần trăm cho một khoảng ngày dịp lễ, Tết, tối đa 30%. Tách khỏi UC-016 theo U-R04 d vì khác dữ liệu, quy tắc và thời điểm. Ngày áp dụng và phạm vi tuyến, loại xe chờ Q-19, Q-20. | Sắp tới dịp lễ, Tết (EV-21) | REQ-53, REQ-54 | CAND-18 |
| UC-018 | Quản lý nhà xe nắm được doanh thu theo ngày, theo tuyến và tỉ lệ lấp đầy chỗ của từng chuyến. | Quản lý nhà xe chọn báo cáo doanh thu theo ngày, doanh thu theo tuyến hoặc tỉ lệ lấp đầy chỗ của từng chuyến rồi xem kết quả. Gộp theo U-R05 vì cùng tác nhân, cùng cách thao tác, chỉ khác nội dung dữ liệu. Cách tính doanh thu chờ Q-23. | Quản lý nhà xe cần theo dõi doanh thu và mức lấp đầy (EV-22) | REQ-63, REQ-64, REQ-65 | CAND-19, CAND-20 |

## 5. Ma trận truy vết REQ --> UC

| REQ | Nội dung tóm tắt | UC phủ | Ghi chú (lý do nếu không phủ) |
|---|---|---|---|
| REQ-01 | Quy mô 12 tuyến, 3 bến, khoảng 80 chuyến mỗi ngày (Dữ liệu) | - | Chuyển P06 (điều kiện dung lượng) |
| REQ-02 | Đội xe khoảng 50 xe giường nằm, 20 xe ghế ngồi (Dữ liệu) | - | Chuyển P06 (điều kiện dung lượng) |
| REQ-03 | Hành khách đặt vé qua website, không bắt buộc tài khoản | UC-002 | Không có |
| REQ-04 | Đặt vé được cung cấp trên website (Ràng buộc) | UC-001, UC-002 | Ràng buộc kênh; chuyển P06 |
| REQ-05 | Tìm chuyến theo điểm đi, điểm đến, ngày đi, không cần tài khoản | UC-001, UC-002 | Không có |
| REQ-06 | Xem sơ đồ chỗ còn trống, không cần tài khoản | UC-001, UC-002 | Không có |
| REQ-07 | Chọn chỗ khi đặt vé | UC-002 | Không có |
| REQ-08 | Tối đa 5 chỗ một lần đặt (Quy tắc nghiệp vụ) | UC-002 | Áp dụng cho UC-004, UC-005 chờ Q-09 |
| REQ-09 | Thông tin đặt vé gồm họ tên, số điện thoại người đi (Dữ liệu) | UC-002 | Q-08 |
| REQ-10 | Đăng ký tài khoản bằng số điện thoại | UC-009, UC-010 | Không có |
| REQ-11 | Xem lại lịch sử vé | UC-011, UC-010 | Không có |
| REQ-12 | Giữ chỗ đã chọn để thanh toán | UC-002 | Không có |
| REQ-13 | Giữ chỗ 10 phút (Quy tắc nghiệp vụ) | UC-002 | Không có |
| REQ-14 | Thanh toán qua cổng thanh toán trực tuyến | UC-003 | Không có |
| REQ-15 | Trao đổi thông tin thanh toán với cổng thanh toán (Giao tiếp ngoài) | UC-003 | Q-24 |
| REQ-16 | Trả chỗ khi hết hạn giữ mà chưa thanh toán | UC-002 | Luồng thay thế hết giờ trong phiên (CAND-24) |
| REQ-17 | Phát hành vé khi thanh toán thành công | UC-002 | Q-10 |
| REQ-18 | Mỗi chỗ một vé, một mã vé (Quy tắc nghiệp vụ) | UC-002, UC-005 | Không có |
| REQ-19 | Gửi vé qua SMS tới người đi | UC-002 | Không có |
| REQ-20 | Trao đổi tin nhắn với cổng SMS (Giao tiếp ngoài) | UC-002, UC-013 | Không có |
| REQ-21 | Bán vé tại quầy cho khách mua trực tiếp | UC-005 | Không có |
| REQ-22 | Vé bán tại quầy thanh toán bằng tiền mặt (Quy tắc nghiệp vụ) | UC-005 | Không có |
| REQ-23 | In vé giấy có mã vạch | UC-005 | Không có |
| REQ-24 | Trao đổi dữ liệu vé với máy in vé nhiệt (Giao tiếp ngoài) | UC-005 | Không có |
| REQ-25 | Nhận đặt chỗ qua điện thoại | UC-004 | ASM-05 |
| REQ-26 | Nhận thanh toán tại quầy cho đặt chỗ qua điện thoại | UC-005 | Luồng thay thế (CAND-11) |
| REQ-27 | Hạn thanh toán đặt chỗ qua điện thoại 60 phút trước giờ xuất bến (Quy tắc nghiệp vụ) | UC-004, UC-005, UC-006 | Không có |
| REQ-28 | Tự động huỷ đặt chỗ qua điện thoại quá hạn | UC-006 | Không có |
| REQ-29 | Hành khách trả vé | UC-008 | ASM-02 |
| REQ-30 | Hành khách đổi vé | UC-007 | ASM-02 |
| REQ-31 | Trả từ 24 giờ trở lên hoàn 90% (Quy tắc nghiệp vụ) | UC-008 | Không có |
| REQ-32 | Trả từ 4 đến dưới 24 giờ hoàn 50% (Quy tắc nghiệp vụ) | UC-008 | Không có |
| REQ-33 | Dưới 4 giờ không được trả (Quy tắc nghiệp vụ) | UC-008 | Không có |
| REQ-34 | Vé trực tuyến hoàn qua cổng thanh toán (Quy tắc nghiệp vụ) | UC-008 | Không có |
| REQ-35 | Trao đổi yêu cầu hoàn tiền với cổng thanh toán (Giao tiếp ngoài) | UC-008, UC-013 | Q-24 |
| REQ-36 | Vé mua tại quầy hoàn tiền mặt tại quầy (Quy tắc nghiệp vụ) | UC-008 | Phần hoàn tiền khi huỷ chuyến chờ Q-14 (CAND-43) |
| REQ-37 | Chỉ đổi sang chuyến khác cùng tuyến (Quy tắc nghiệp vụ) | UC-007 | Không có |
| REQ-38 | Mỗi vé chỉ đổi một lần (Quy tắc nghiệp vụ) | UC-007 | Không có |
| REQ-39 | Đổi chậm nhất 4 giờ trước giờ xuất bến (Quy tắc nghiệp vụ) | UC-007 | Q-13 |
| REQ-40 | Trả thêm chênh lệch khi vé mới đắt hơn (Quy tắc nghiệp vụ) | UC-007, UC-003 | ASM-10; Q-12; UC-003 phủ nhánh vé mua trực tuyến |
| REQ-41 | Lập lịch chạy theo tuần | UC-012 | Không có |
| REQ-42 | Chuyến gồm tuyến, giờ xuất bến, xe, tài xế (Dữ liệu) | UC-012 | Danh mục tuyến, xe, tài xế chờ Q-03 (CAND-47 đến CAND-49) |
| REQ-43 | Xe không chạy hai chuyến chồng nhau (Quy tắc nghiệp vụ) | UC-012 | Không có |
| REQ-44 | Tài xế không chạy hai chuyến chồng nhau (Quy tắc nghiệp vụ) | UC-012 | Không có |
| REQ-45 | Tài xế lái tối đa 10 giờ một ngày (Quy tắc nghiệp vụ) | UC-012 | Q-18 |
| REQ-46 | Tuyến có thời gian chạy dự kiến (Dữ liệu, ASM-03) | UC-012 | Không có |
| REQ-47 | Nhân viên điều hành huỷ chuyến | UC-013 | Không có |
| REQ-48 | Gửi SMS cho mọi hành khách có vé khi huỷ chuyến | UC-013 | Q-15 |
| REQ-49 | Hoàn tiền cho mọi hành khách có vé khi huỷ chuyến | UC-013 | Kênh hoàn vé mua tại quầy chờ Q-14 (CAND-43) |
| REQ-50 | Vé của chuyến bị huỷ hoàn 100% (Quy tắc nghiệp vụ) | UC-013 | Không có |
| REQ-51 | Quản lý nhà xe đặt giá vé | UC-016 | Không có |
| REQ-52 | Giá vé theo tuyến và loại xe (Quy tắc nghiệp vụ) | UC-016 | Không có |
| REQ-53 | Đặt mức tăng giá theo phần trăm cho khoảng ngày lễ, Tết | UC-017 | Q-19, Q-20 |
| REQ-54 | Mức tăng giá tối đa 30% (Quy tắc nghiệp vụ) | UC-017 | Không có |
| REQ-55 | Phụ xe quét mã vé bằng máy soát vé cầm tay | UC-015 | Q-04 |
| REQ-56 | Soát vé chạy trên máy Android có đầu quét (Ràng buộc) | UC-015 | Ràng buộc nền tảng; chuyển P06 |
| REQ-57 | Máy báo vé hợp lệ hoặc không hợp lệ | UC-015 | Không có |
| REQ-58 | Vé không hợp lệ khi sai chuyến, đã huỷ, đã soát (Quy tắc nghiệp vụ) | UC-015 | Q-21 |
| REQ-59 | Soát được khi mất sóng (Phi chức năng) | UC-015 | Ràng buộc chất lượng; chuyển P06 |
| REQ-60 | Gửi lại kết quả soát khi có sóng | UC-015 | Không có |
| REQ-61 | Gửi danh sách hành khách về máy soát vé | UC-014 | Q-11 |
| REQ-62 | Gửi danh sách 15 phút trước giờ xuất bến (Quy tắc nghiệp vụ) | UC-014 | Không có |
| REQ-63 | Báo cáo doanh thu theo ngày | UC-018 | Q-23 |
| REQ-64 | Báo cáo doanh thu theo tuyến | UC-018 | Q-23 |
| REQ-65 | Báo cáo tỉ lệ lấp đầy chỗ của từng chuyến | UC-018 | Không có |
| REQ-66 | Chịu được khoảng 2.000 người truy cập cùng lúc (Phi chức năng) | - | Chuyển P06 |
| REQ-67 | Không hai vé cùng một chỗ trên một chuyến (Quy tắc nghiệp vụ) | UC-002, UC-004, UC-005, UC-007 | Quy tắc chung; chuyển P06 |
| REQ-68 | Không lưu thông tin thẻ (Ràng buộc) | UC-003 | Ngoài phạm vi theo P00; chuyển P06 |

## 6. Thống kê và nhận xét ngưỡng

| ACT | Số UC là tác nhân chính | Số UC là tác nhân phụ | Nhận xét |
|---|---|---|---|
| ACT-01 Hành khách | 7 (UC-001, UC-002, UC-007, UC-008, UC-009, UC-010, UC-011), thêm UC-003 qua UC-002, UC-007 | 0 | Trong khoảng 2-12 |
| ACT-02 Nhân viên bán vé | 4 (UC-004, UC-005, UC-007, UC-008) | 0 | Trong khoảng 2-12 |
| ACT-03 Nhân viên điều hành | 2 (UC-012, UC-013) | 0 | Ở cận dưới; có thể tăng khi Q-03 được trả lời (a) (CAND-47 đến CAND-49) |
| ACT-04 Quản lý nhà xe | 3 (UC-016, UC-017, UC-018) | 0 | Trong khoảng 2-12; có thể tăng khi Q-03 được trả lời (b) |
| ACT-05 Phụ xe | 1 (UC-015) | 0 | Dưới mức thường gặp với tác nhân người. Đã rà lại: nguồn chỉ nêu phụ xe soát vé (Mục 8, câu 1), không có mục tiêu nào bị gộp; giữ nguyên |
| ACT-06 Cổng thanh toán | 0 | 3 (UC-003, UC-008, UC-013) | Tác nhân phụ (ASM-07) |
| ACT-07 Cổng SMS | 0 | 2 (UC-002, UC-013) | Tác nhân phụ |
| ACT-08 Máy in vé | 0 | 1 (UC-005) | Tác nhân phụ |
| ACT-09 Đầu quét mã vạch | 0 | 1 (UC-015) | Tác nhân phụ |
| ACT-10 Bộ định thời | 2 (UC-006, UC-014) | 0 | Bình thường với tác nhân thời gian |

Tổng số UC: 18 (16 User-goal, 2 Subfunction).

Số UC mỗi nhóm: Bán vé 8 (UC-001 đến UC-008); Tài khoản hành khách 3 (UC-009 đến UC-011); Vận hành chuyến 4 (UC-012 đến UC-015); Giá vé và báo cáo 3 (UC-016 đến UC-018).

Số UC mức Subfunction: 2 (UC-003 theo Q4 d và Q4 a, UC-010 theo U-R01), khoảng 11% tổng số, dưới ngưỡng 20%.

Nhận xét: tổng 18 UC nằm trong khoảng 10-40 của hệ thống cỡ vừa. Lệch ngưỡng duy nhất là ACT-05 Phụ xe chỉ có 1 UC, có căn cứ trong nguồn nên giữ nguyên. Ba ứng viên chờ Q-03 và một ứng viên chờ Q-14 có thể làm tổng số UC tăng tới 22 sau khi câu hỏi được trả lời.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-26 | Hành khách có tìm chuyến và xem chỗ trống như một việc riêng, không nhằm đặt vé ngay (ví dụ xem trước lịch chạy và chỗ trống), không? (Có / Không) | UC-001 giữ thành UC riêng hay là bước của UC-002; ASM-08 | Mục 1, câu 2-3: "tìm chuyến ..., xem sơ đồ chỗ ..., rồi chọn tối đa 5 chỗ"; "Việc tìm chuyến và xem chỗ trống không cần tài khoản" |
| Q-27 | Nhân viên bán vé, nhân viên điều hành, quản lý nhà xe và phụ xe có phải đăng nhập trước khi dùng hệ thống không? (Có / Không) | UC-010 (tác nhân nối với Đăng nhập); P03; ASM-09 | Nguồn chỉ nhắc tài khoản của hành khách (Mục 2, câu 2) |
| Q-28 | Khi đổi vé, phần chênh lệch được thanh toán qua kênh nào? (a) Theo kênh mua: vé mua trực tuyến qua cổng thanh toán, vé mua tại quầy bằng tiền mặt tại quầy; (b) Mọi vé thanh toán chênh lệch tại quầy | UC-007 (tác nhân phụ, luồng thay thế); ASM-10 | Mục 5, câu 4: "trả thêm phần chênh lệch nếu vé mới đắt hơn" |
| Q-29 | Nhân viên điều hành lập lịch chạy của một tuần trong một lần làm việc hay có thể xếp dần các chuyến qua nhiều lần làm việc? (Một lần / Nhiều lần) | UC-012 (U-T6, U-T7; trả lời "Một lần" thì trả lại tên "Lập lịch chạy tuần" và mục tiêu cả tuần theo UCR-03); P04 | Mục 6, câu 1: "lập lịch chạy theo tuần"; Đoạn mở đầu, câu 1: "mỗi ngày khoảng 80 chuyến" |
| Q-30 | Khi đổi vé, vé mới được giao cho khách thế nào? (a) Theo kênh mua: vé mua trực tuyến gửi mã vé mới qua SMS, vé mua tại quầy in vé giấy mới có mã vạch tại quầy; (b) Giữ mã vé cũ, chỉ đổi chuyến, không giao vé mới. Câu hỏi nêu ở P02R-review.md 1.0, ghi lại ở đây để P03, P04 đọc được | UC-007 (tác nhân phụ ACT-07, ACT-08; gộp theo U-R10 b hay tách theo U-R10 a); P04 UC-007 | Mục 5, câu 4: "Mỗi vé chỉ được đổi sang chuyến khác cùng tuyến một lần ... và trả thêm phần chênh lệch nếu vé mới đắt hơn"; Mục 3, câu 3 và Mục 4, câu 1 nêu cách giao vé theo kênh mua nhưng không nhắc tới vé đổi |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-08 | Hành khách có thể tìm chuyến và xem chỗ trống như một mục tiêu thông tin riêng, không bắt buộc đặt vé ngay sau đó. | Mục 1, câu 3 nêu riêng quyền dùng việc "tìm chuyến và xem chỗ trống" không cần tài khoản, tách khỏi câu về đặt vé. Chờ Q-26 | UC-001; CAND-01 |
| ASM-09 | Nhân viên bán vé, nhân viên điều hành, quản lý nhà xe và phụ xe phải đăng nhập trước khi dùng chức năng của mình, dùng chung UC-010. Theo U-R01, P02 chưa nối các tác nhân này với UC-010 cho tới khi giả định được xác nhận. | Nguồn không nhắc tài khoản của nhân viên, nhưng các chức năng như đặt giá, huỷ chuyến, bán vé chỉ dành cho vai trò nội bộ của nhà xe. Chờ Q-27 | UC-010; CAND-06 |
| ASM-10 | Phần chênh lệch khi đổi vé được thanh toán theo kênh mua: vé mua trực tuyến qua cổng thanh toán, vé mua tại quầy bằng tiền mặt tại quầy. | Mục 5, câu 3 phân kênh hoàn tiền theo kênh mua; ASM-02 phân kênh đổi vé theo kênh mua. Chờ Q-28 | UC-007 (nhánh trả chênh lệch qua UC-003); UC-003 (tác nhân chính ACT-01 qua UC-007, REQ-40); CAND-30; CAND-38 |
| ASM-11 | Lịch chạy tuần có thể được xếp qua nhiều lần làm việc; mỗi lần thêm một hoặc nhiều chuyến vào lịch tuần và kết thúc ở trạng thái nhất quán (mọi chuyến đã xếp đều thoả quy tắc chồng chuyến và giờ lái). | Khoảng 80 chuyến mỗi ngày (REQ-01) tức khoảng 560 chuyến mỗi tuần, khó hoàn tất trong một phiên; nguồn không nêu. Chờ Q-29 | UC-012; CAND-15 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P01 | ACT-01, ACT-02 | Hai tác nhân cùng khởi xướng UC-007 Đổi vé và UC-008 Trả vé (U-R10 b, U-R11). | Xem xét tác nhân cha cho ACT-01 và ACT-02 ở hai UC này. Nếu P01 thấy tổng quát hoá không có nghĩa nghiệp vụ (một bên là khách, một bên là nhân viên nhà xe, không chung UC nào khác), giữ hai association và ghi lý do. |
| P01 | ACT-01 | Mục tiêu "Đăng ký tài khoản và xem lại lịch sử vé" gộp hai việc ở hai thời điểm (U-AP05). | Tách thành hai mục tiêu "Đăng ký tài khoản" và "Xem lại lịch sử vé". |
| P01 | ACT-02, ACT-10 | Mục tiêu "Thu tiền tại quầy cho vé đặt qua điện thoại" (ACT-02) và "huỷ vé đặt qua điện thoại chưa thanh toán" (ACT-10) gọi đặt chỗ chưa thanh toán là "vé", lệch với tên UC-006 Huỷ đặt chỗ qua điện thoại quá hạn và UC-004 Nhận đặt chỗ qua điện thoại (U-N4, UCR-02 của P02R-review.md 1.0, ASM-05). | Đổi "vé đặt qua điện thoại" thành "đặt chỗ qua điện thoại" trong cột Mục tiêu của ACT-02 và ACT-10. |

## Vấn đề còn mở

- Chọn giữa hai quy tắc (C9): UC-014 Chuẩn bị danh sách hành khách của chuyến là việc chuyển dữ liệu giữa hai phần nội bộ của hệ thống theo ASM-01, khớp dấu hiệu "đồng bộ nội bộ" của Q1 (U-T9). U-R07 lại cho tác vụ có mốc thời gian nguồn nêu rõ, không người ra lệnh, có giá trị cho phụ xe thành UC của tác nhân thời gian, và Bước 5 cho quy tắc U-R ưu tiên hơn cây quyết định. Đã áp dụng U-R07, đồng thời khớp với mục tiêu của ACT-10 đã chốt ở P01. Nếu Q-01 được trả lời là máy soát vé có phần mềm sẵn, máy soát vé trở thành tác nhân phụ của UC-014.
- U-R01 và ASM-09: quy tắc cho chế độ CO_NHAN ghi ASM về việc nhân viên có phải đăng nhập không nhưng vẫn "chưa nối". Đã ghi ASM-09 và chưa nối ACT-02 đến ACT-05 với UC-010; P03 cần chờ Q-27 hoặc xác nhận ASM-09 trước khi vẽ association.
- Bước 9.1 cần "tác nhân đặt trên cùng theo P03 L-02" nhưng P03 chưa chạy. Đã coi ACT-01 Hành khách là tác nhân chính quan trọng nhất (P00 mục 1: mục tiêu đặt và thanh toán vé trực tuyến). Lập lịch chạy và đặt giá vé không được coi là "điều kiện tiên quyết" theo nghĩa của Bước 9.1 (các ví dụ chỉ nêu đăng ký tài khoản của chính tác nhân), nên nhóm Vận hành chuyến và Giá vé và báo cáo đánh số theo thứ tự xuất hiện trong nguồn. Đăng ký tài khoản không bắt buộc để đặt vé (REQ-03) nên nhóm Tài khoản hành khách cũng không đánh số trước nhóm Bán vé.
- UC-003 giữ theo Q4 d: vế "thất bại độc lập mà không huỷ toàn bộ mục tiêu cha" suy từ câu "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại" (Mục 3, câu 2), tức trong 10 phút lần đặt chưa bị huỷ dù thanh toán chưa thành công. Nguồn không nói tường minh hành khách được thanh toán lại; P04 cần xác nhận.
- Đặt tên UC-016 Đặt giá vé: U-R15 gợi ý tên "Cấu hình <nhóm tham số>" hoặc "Quản lý <dữ liệu>", còn U-R04 chỉ cho đưa vào "Quản lý X" những thao tác nguồn nêu. Nguồn chỉ nêu "đặt", nên đã dùng động từ nghiệp vụ của nguồn theo U-N1, U-N4.
- Target 4 với UC-012: U-T6 (một phiên) đạt dựa trên ASM-11; nếu Q-29 trả lời "Một lần" thì UC vẫn đạt, nếu nhiều lần làm việc mà mỗi lần không kết thúc nhất quán thì cần xét lại U-T7.
- Lần chạy 1.1 áp dụng UCR-01 đến UCR-04 của P02R-review.md 1.0 theo yêu cầu bổ sung; không có UCR nào bị từ chối. Mã UC, CAND, EV, ASM, Q giữ nguyên; tổng số UC không đổi (18). Thay đổi: UC-003 (mục tiêu, tác nhân chính, REQ, sự kiện kích hoạt, thêm điều kiện Q4 a), UC-007 (tác nhân phụ, mô tả ngắn), UC-006, UC-012, UC-014 (tên, mục tiêu theo UCR-02, UCR-03, UCR-04), cùng các dòng liên quan ở Mục 1, Mục 2, Mục 3, Mục 5, Mục 6, ASM-10, ASM-11.
- UCR-01 phụ thuộc ASM-10: nếu Q-28 được trả lời (b) (mọi chênh lệch trả tại quầy), UC-007 không dùng UC-003, bỏ REQ-40 và "qua UC-007" khỏi UC-003, bỏ điều kiện Q4 a của UC-003 và trả mục tiêu UC-003 về dạng "thanh toán cho các chỗ đang giữ".
- UC-003 với Q4 d khi được gọi từ UC-007: vế "thất bại không huỷ toàn bộ mục tiêu cha" được suy từ nhánh UC-002 (Mục 3, câu 2); nguồn không nêu UC-007 xử lý thế nào khi thanh toán chênh lệch thất bại. UC-003 vẫn giữ được nhờ Q4 a (dùng lại ở hai UC User-goal); P04 UC-007 cần nêu luồng thất bại.
- UCR-03 phụ thuộc ASM-11: nếu Q-29 được trả lời "Một lần", trả UC-012 về tên "Lập lịch chạy tuần" (Create Weekly Schedule) và mục tiêu cả tuần.
- UCR-01 chuyển thời hạn giữ chỗ 10 phút về UC-002: đã bỏ REQ-13 khỏi cột REQ của UC-003 và khỏi dòng REQ-13 ở Mục 5. Cũng đã bỏ UC-003 khỏi dòng REQ-17 ở Mục 5 để khớp Bảng 4b (phát hành vé là bước của UC-002, CAND-31); bản 1.0 ghi UC-003 ở Mục 5 nhưng không ghi REQ-17 ở Bảng 4b.
- Q-30 (cách giao vé mới khi đổi vé) do P02R nêu, chưa có trả lời và chưa có ASM; UC-007 giữ một UC cho hai tác nhân theo U-R10 b và chưa có tác nhân phụ ACT-07, ACT-08. Nếu Q-30 được trả lời (a), xét lại U-R10 a cho luồng in vé giấy của ACT-02 và thêm tác nhân phụ tương ứng.
- Target 3 với CAND-43 (Chờ Q-14) và CAND-47 đến CAND-49 (Chờ Q-03): Q-14 và Q-03 nằm ở mục Câu hỏi mở của P00-problem-brief.md 1.0, không chép lại vào artifact này; mã Q liên tục toàn dự án nên tham chiếu vẫn trỏ tới một câu hỏi duy nhất.
