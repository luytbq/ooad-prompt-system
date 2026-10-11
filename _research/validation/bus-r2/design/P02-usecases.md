# P02 - Xác định use case - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02 |
| Phiên bản | 1.1 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09); P01-actors.md (phiên bản 1.0, Q-39, ASM-11); P02-usecases.md (phiên bản 1.0, Q-40, ASM-14); P02R-review.md (phiên bản 1.0, Q-42, ASM-16); yeu-cau-xe-khach.md. Placeholder PHAM_VI_LAN_CHAY, QUY_UOC_DA_CHOT: Không có. YEU_CAU_BO_SUNG: áp dụng UCR-01, UCR-02, UCR-03, UCR-04 của P02R-review.md phiên bản 1.0. Q-41, Q-42, ASM-15, ASM-16 do P02R cấp, chép nguyên mã; không cấp mã Q, ASM mới |
| Phạm vi | Toàn hệ thống |
| Mã Q, ASM cuối đã cấp | Q-42, ASM-16 |

## 1. Danh sách mục tiêu tác nhân

| ACT | Mục tiêu | Mức mục tiêu dự kiến | REQ | CAND |
|---|---|---|---|---|
| ACT-01, ACT-02 | Bán vé cho hành khách (đặt trực tuyến, bán tại quầy, đặt chỗ qua điện thoại) | Summary | REQ-04, REQ-22, REQ-28 | CAND-30 |
| ACT-01 Hành khách | Tìm chuyến và xem các chỗ còn trống | User-goal | REQ-05, REQ-06 | CAND-01, CAND-33 |
| ACT-01 | Đặt vé trực tuyến cho chuyến đã chọn và nhận mã vé | User-goal | REQ-04, REQ-07, REQ-08, REQ-09, REQ-13, REQ-14, REQ-17 đến REQ-21 | CAND-02 |
| ACT-01 | Thanh toán các chỗ đang giữ qua cổng thanh toán | Subfunction | REQ-15, REQ-16 | CAND-39 |
| ACT-01 | Đăng ký tài khoản bằng số điện thoại | User-goal | REQ-10 | CAND-03 |
| ACT-01 | Đăng nhập để xem lại lịch sử vé | Subfunction | REQ-12 | CAND-05 |
| ACT-01 | Xem lại lịch sử vé | User-goal | REQ-11 | CAND-04 |
| ACT-01 | Trả vé mua trực tuyến và nhận hoàn tiền | User-goal | REQ-33, REQ-37 đến REQ-40 | CAND-06, CAND-31 |
| ACT-01 | Đổi vé mua trực tuyến sang chuyến khác cùng tuyến và nhận mã vé mới | User-goal | REQ-20, REQ-21, REQ-34, REQ-42 đến REQ-45 | CAND-07, CAND-32 |
| ACT-02 Nhân viên bán vé | Bán vé tại quầy cho khách mua trực tiếp, thu tiền mặt, in vé giấy | User-goal | REQ-22, REQ-25, REQ-26, REQ-27, REQ-29 | CAND-08 |
| ACT-02 | Nhận đặt chỗ qua điện thoại cho khách | User-goal | REQ-28, REQ-29, REQ-31 | CAND-09 |
| ACT-02 | Thu tiền vé đặt qua điện thoại khi khách đến quầy | User-goal | REQ-30, REQ-31 | CAND-10 |
| ACT-02 | Tìm chuyến và xem chỗ trống cho khách khi bán vé, nhận đặt chỗ, đổi vé tại quầy (đoạn dùng chung với UC-008, qua UC-004, UC-005, UC-015) | User-goal | REQ-05, REQ-06, REQ-29 | CAND-01, CAND-34 |
| ACT-02 | Trả vé tại quầy cho vé mua tại quầy và hoàn tiền mặt (cùng UC với trả vé mua trực tuyến, UCR-02) | User-goal | REQ-35, REQ-37 đến REQ-39, REQ-41 | CAND-11 |
| ACT-02 | Đổi vé tại quầy cho vé mua tại quầy | User-goal | REQ-36, REQ-42 đến REQ-45 | CAND-12 |
| ACT-02 | Hoàn tiền mặt tại quầy cho vé mua tại quầy của chuyến bị huỷ | User-goal | REQ-57, REQ-58, REQ-59 | CAND-13 |
| ACT-02 | Đăng nhập để dùng phần mềm nhà xe | Subfunction | REQ-23 | CAND-05 |
| ACT-03 Nhân viên điều hành | Lập lịch chạy theo tuần: chọn tuyến, giờ xuất bến, xe, tài xế, phụ xe | User-goal | REQ-46, REQ-47, REQ-51 đến REQ-54 | CAND-14, CAND-53, CAND-54 |
| ACT-03 | Huỷ chuyến phải huỷ và báo, hoàn tiền cho hành khách đã có vé | User-goal | REQ-55 đến REQ-59 | CAND-15, CAND-56 |
| ACT-03 | Duy trì danh mục tuyến xe và bến xe | User-goal | REQ-48 | CAND-16 |
| ACT-03 | Duy trì danh mục xe (loại xe, số chỗ, sơ đồ chỗ) | User-goal | REQ-49 | CAND-19 |
| ACT-03 | Duy trì danh mục tài xế | User-goal | REQ-50 | CAND-20 |
| ACT-03 | Đăng nhập để dùng phần mềm nhà xe | Subfunction | REQ-23 | CAND-05 |
| ACT-04 Quản lý nhà xe | Đặt giá vé theo tuyến và loại xe | User-goal | REQ-60 | CAND-21 |
| ACT-04 | Đặt mức tăng giá theo phần trăm cho khoảng ngày lễ, Tết | User-goal | REQ-61, REQ-62 | CAND-22 |
| ACT-04 | Xem báo cáo doanh thu theo ngày, theo tuyến | User-goal | REQ-71, REQ-72 | CAND-23, CAND-60, CAND-61 |
| ACT-04 | Xem báo cáo tỉ lệ lấp đầy chỗ của từng chuyến | User-goal | REQ-73 | CAND-24 |
| ACT-04 | Quản lý tài khoản của nhân viên nhà xe | User-goal | REQ-24 | CAND-25 |
| ACT-04 | Đăng nhập để dùng phần mềm nhà xe | Subfunction | REQ-23 | CAND-05 |
| ACT-05 Phụ xe | Soát vé hành khách lên xe | User-goal | REQ-63, REQ-65, REQ-66 | CAND-26 |
| ACT-05 | Soát vé khi xe ở vùng mất sóng và gửi lại kết quả khi có sóng | User-goal | REQ-67, REQ-68 | CAND-27 |
| ACT-05 | Đăng nhập để dùng máy soát vé | Subfunction | REQ-23 | CAND-05 |
| ACT-09 Bộ định thời | Huỷ vé đặt qua điện thoại chưa thanh toán tại quầy đúng hạn, trả chỗ cho người khác | User-goal | REQ-31, REQ-32 | CAND-28 |
| ACT-09 | Đưa danh sách hành khách của chuyến về máy soát vé trước giờ xuất bến | User-goal | REQ-69, REQ-70 | CAND-29 |

## 2. Danh sách sự kiện

| EV | Sự kiện | Loại | Nguồn phát (ACT) | Phản hồi mong đợi của hệ thống | REQ | CAND |
|---|---|---|---|---|---|---|
| EV-01 | Hành khách muốn tìm chuyến và xem chỗ trống | Nghiệp vụ | ACT-01 | Cho xem danh sách chuyến theo điểm đi, điểm đến, ngày đi và sơ đồ chỗ còn trống | REQ-05, REQ-06 | CAND-01, CAND-33 |
| EV-02 | Hành khách muốn mua vé xe trực tuyến | Nghiệp vụ | ACT-01 | Giữ chỗ, thu tiền qua cổng thanh toán, phát hành vé, gửi mã vé qua SMS | REQ-04, REQ-07, REQ-08, REQ-09, REQ-13, REQ-14, REQ-18, REQ-19, REQ-20 | CAND-02 |
| EV-03 | Đủ 10 phút giữ chỗ mà hành khách chưa thanh toán thành công (trong phiên đặt vé) | Thời gian | - | Trả các chỗ đang giữ cho người khác | REQ-14, REQ-17 | CAND-41 |
| EV-04 | Hành khách muốn có tài khoản để xem lại lịch sử vé | Nghiệp vụ | ACT-01 | Tạo tài khoản gắn với số điện thoại | REQ-10 | CAND-03 |
| EV-05 | Hành khách có tài khoản hoặc nhân viên nhà xe muốn vào hệ thống bằng tài khoản | Nghiệp vụ | ACT-01, ACT-02, ACT-03, ACT-04, ACT-05 | Xác thực người dùng, mở phiên làm việc | REQ-12, REQ-23 | CAND-05, CAND-37 |
| EV-06 | Hành khách muốn xem lại các vé đã đặt | Nghiệp vụ | ACT-01 | Cho xem lịch sử vé | REQ-11 | CAND-04 |
| EV-07 | Hành khách muốn trả vé đã mua trực tuyến | Nghiệp vụ | ACT-01 | Trả vé, hoàn tiền theo mức hoàn qua cổng thanh toán | REQ-33, REQ-37, REQ-38, REQ-39, REQ-40 | CAND-06, CAND-31 |
| EV-08 | Hành khách muốn đổi vé đã mua trực tuyến sang chuyến khác cùng tuyến | Nghiệp vụ | ACT-01 | Đổi vé, thu thêm chênh lệch nếu vé mới đắt hơn, gửi mã vé mới qua SMS (ASM-16) | REQ-20, REQ-21, REQ-34, REQ-42, REQ-43, REQ-44, REQ-45 | CAND-07, CAND-32 |
| EV-09 | Khách đến quầy muốn mua vé trực tiếp | Nghiệp vụ | ACT-02 | Bán vé, thu tiền mặt, in vé giấy có mã vạch | REQ-22, REQ-25, REQ-26, REQ-29 | CAND-08 |
| EV-10 | Khách gọi điện muốn đặt chỗ | Nghiệp vụ | ACT-02 | Ghi nhận đặt chỗ và giữ chỗ đến hạn thanh toán | REQ-28, REQ-29, REQ-31 | CAND-09 |
| EV-11 | Khách đã đặt chỗ qua điện thoại đến quầy thanh toán | Nghiệp vụ | ACT-02 | Thu tiền, xác nhận vé đã thanh toán | REQ-30, REQ-31 | CAND-10 |
| EV-12 | Đến 60 phút trước giờ xuất bến mà vé đặt qua điện thoại chưa thanh toán tại quầy | Thời gian | ACT-09 | Huỷ vé đặt chỗ quá hạn, trả chỗ cho người khác | REQ-31, REQ-32 | CAND-28 |
| EV-13 | Khách có vé mua tại quầy muốn trả vé | Nghiệp vụ | ACT-02 | Trả vé, hoàn tiền mặt theo mức hoàn | REQ-35, REQ-37, REQ-38, REQ-39, REQ-41 | CAND-11, CAND-31 |
| EV-14 | Khách có vé mua tại quầy muốn đổi vé | Nghiệp vụ | ACT-02 | Đổi vé, thu thêm chênh lệch nếu vé mới đắt hơn | REQ-36, REQ-42, REQ-43, REQ-44, REQ-45 | CAND-12, CAND-32 |
| EV-15 | Nhà xe cần lịch chạy của tuần | Nghiệp vụ | ACT-03 | Lập lịch chạy đúng ràng buộc xe, tài xế | REQ-46, REQ-47, REQ-51, REQ-52, REQ-53, REQ-54 | CAND-14, CAND-53, CAND-54 |
| EV-16 | Chuyến phải huỷ (xe hỏng, thời tiết) | Nghiệp vụ | ACT-03 | Huỷ chuyến, báo SMS và hoàn tiền cho hành khách đã có vé | REQ-55, REQ-56, REQ-57, REQ-58, REQ-59 | CAND-15, CAND-55, CAND-56, CAND-57 |
| EV-17 | Khách có vé mua tại quầy của chuyến bị huỷ đến quầy nhận hoàn tiền | Nghiệp vụ | ACT-02 | Hoàn tiền mặt đủ 100% giá vé | REQ-57, REQ-58, REQ-59 | CAND-13 |
| EV-18 | Nhà xe cần thêm hoặc đổi dữ liệu bến xe | Nghiệp vụ | ACT-03 | Duy trì danh mục bến xe | REQ-48 | CAND-18 |
| EV-19 | Nhà xe cần thêm hoặc đổi dữ liệu tuyến xe | Nghiệp vụ | ACT-03 | Duy trì danh mục tuyến xe | REQ-48 | CAND-17 |
| EV-20 | Nhà xe cần thêm hoặc đổi dữ liệu xe, loại xe, sơ đồ chỗ | Nghiệp vụ | ACT-03 | Duy trì danh mục xe | REQ-49 | CAND-19 |
| EV-21 | Nhà xe cần thêm hoặc đổi dữ liệu tài xế | Nghiệp vụ | ACT-03 | Duy trì danh mục tài xế | REQ-50 | CAND-20 |
| EV-22 | Quản lý cần đặt hoặc đổi giá vé | Nghiệp vụ | ACT-04 | Ghi nhận giá vé theo tuyến và loại xe | REQ-60 | CAND-21 |
| EV-23 | Đến dịp lễ, Tết quản lý cần tăng giá vé cho một khoảng ngày | Nghiệp vụ | ACT-04 | Ghi nhận mức tăng giá theo phần trăm, tối đa 30% | REQ-61, REQ-62 | CAND-22 |
| EV-24 | Quản lý cần biết doanh thu | Nghiệp vụ | ACT-04 | Cho xem báo cáo doanh thu theo ngày, theo tuyến | REQ-71, REQ-72 | CAND-23, CAND-60, CAND-61 |
| EV-25 | Quản lý cần biết mức lấp đầy chỗ của các chuyến | Nghiệp vụ | ACT-04 | Cho xem báo cáo tỉ lệ lấp đầy chỗ của từng chuyến | REQ-73 | CAND-24 |
| EV-26 | Nhà xe cần cấp hoặc thay đổi tài khoản của nhân viên | Nghiệp vụ | ACT-04 | Quản lý tài khoản nhân viên nhà xe | REQ-23, REQ-24 | CAND-25 |
| EV-27 | Hành khách lên xe, phụ xe cần soát vé | Nghiệp vụ | ACT-05 | Báo hợp lệ hoặc không hợp lệ cho mã vé đã quét, kể cả khi mất sóng | REQ-63, REQ-65, REQ-66, REQ-67 | CAND-26, CAND-27, CAND-58 |
| EV-28 | Đến 15 phút trước giờ xuất bến | Thời gian | ACT-09 | Gửi danh sách hành khách của chuyến về máy soát vé | REQ-69, REQ-70 | CAND-29 |
| EV-29 | Máy soát vé có sóng trở lại sau khi soát vé lúc mất sóng | Thiết bị | - | Gửi lại kết quả soát vé cho hệ thống | REQ-68 | CAND-59 |

## 3. Bảng ứng viên use case

| CAND | Ứng viên | Kết luận | Phép thử không đạt | Lý do | REQ | Nguồn phát hiện |
|---|---|---|---|---|---|---|
| CAND-01 | Tìm chuyến và xem chỗ trống | Giữ thành UC-008 | - | U-R05, U-R17: hành khách có mục tiêu thông tin độc lập, nguồn nêu "không cần tài khoản" (Mục 1, câu 3); tìm rồi xem sơ đồ chỗ là một UC; phần đầu của các UC đặt, bán, đổi vé; nhân viên bán vé dùng đoạn này qua UC-004, UC-005, UC-015 (ASM-03) nên ACT-02 là tác nhân chính ghi "(qua ...)" | REQ-05, REQ-06 | Mục tiêu; Sự kiện EV-01; Động từ |
| CAND-02 | Đặt vé trực tuyến (từ chọn chỗ đến nhận mã vé) | Giữ thành UC-009 | - | Một phiên, kết quả là vé đã phát hành; thanh toán là UC Subfunction CAND-39 được UC này include | REQ-04, REQ-07, REQ-08, REQ-09, REQ-13 đến REQ-21 | Mục tiêu; Sự kiện EV-02; Động từ |
| CAND-03 | Đăng ký tài khoản bằng số điện thoại | Giữ thành UC-001 | - | U-R03: tác nhân chưa có tài khoản, kết quả là có tài khoản | REQ-10 | Mục tiêu; Sự kiện EV-04; Động từ |
| CAND-04 | Xem lại lịch sử vé | Giữ thành UC-011 | - | U-R05: mục tiêu thông tin độc lập của hành khách có tài khoản; nội dung lịch sử chờ Q-26 | REQ-11 | Mục tiêu; Sự kiện EV-06; Động từ |
| CAND-05 | Đăng nhập (hành khách có tài khoản và bốn vai trò nhân viên nhà xe) | Giữ thành UC-003 | U-T3 (Subfunction, giữ theo U-R01) | U-R01: nguồn nhắc tài khoản của hành khách (ASM-01) và ngụ ý tài khoản nhân viên (ASM-02); nối ACT-01 đến ACT-05; không include vào các UC khác | REQ-12, REQ-23 | Mục tiêu; Sự kiện EV-05; Động từ |
| CAND-06 | Trả vé mua trực tuyến | Giữ thành UC-012 | - | U-R10 b, U-R12, U-AP15: cùng mục tiêu và quy tắc hoàn với CAND-11, chỉ khác người thao tác và kênh hoàn (cổng thanh toán hoặc tiền mặt) nên là một UC hai tác nhân chính; đoạn xác thực quyền trả vé (Q-37) thuộc luồng hành khách, không thuộc người đại diện; theo ASM-04, ASM-15 (Chờ Q-41) | REQ-33, REQ-37 đến REQ-40 | Mục tiêu; Sự kiện EV-07; Động từ |
| CAND-07 | Đổi vé mua trực tuyến sang chuyến khác cùng tuyến | Giữ thành UC-014 | - | U-R10 a, U-R12: tách khỏi đổi vé tại quầy vì thu chênh lệch qua cổng thanh toán (ASM-13) và hành khách tự chọn chuyến mới; vé mới có mã riêng gửi qua SMS (ASM-16, Chờ Q-42), Cổng SMS là tác nhân phụ (U-R06); theo ASM-04 | REQ-34, REQ-42 đến REQ-45 | Mục tiêu; Sự kiện EV-08; Động từ |
| CAND-08 | Bán vé tại quầy cho khách mua trực tiếp | Giữ thành UC-004 | - | U-R10 a: nhân viên bán vé thao tác thay khách, kết quả khác đặt trực tuyến (vé phát hành ngay, tiền mặt, in vé giấy qua máy in, không giữ chỗ chờ thanh toán); chọn chuyến và chỗ theo ASM-03; máy in là tác nhân phụ theo U-R18 | REQ-22, REQ-25, REQ-26, REQ-27, REQ-29 | Mục tiêu; Sự kiện EV-09; Động từ |
| CAND-09 | Nhận đặt chỗ qua điện thoại | Giữ thành UC-005 | - | U-R13: tách khỏi thu tiền (khách đến quầy vào lúc khác); chọn chuyến và chỗ theo ASM-03; kết quả là chỗ được giữ đến hạn thanh toán | REQ-28, REQ-29, REQ-31 | Mục tiêu; Sự kiện EV-10; Động từ |
| CAND-10 | Thu tiền vé đặt qua điện thoại tại quầy | Giữ thành UC-006 | - | U-R13: phiên riêng của nhân viên bán vé khi khách đến quầy; in vé giấy theo ASM-14 | REQ-30, REQ-31 | Mục tiêu; Sự kiện EV-11; Động từ |
| CAND-11 | Trả vé tại quầy cho vé mua tại quầy | Gộp vào UC-012 | U-T11, U-AP15 | U-R10 b: nhân viên bán vé làm thay khách, luồng không có đoạn tương tác riêng từ 2 bước (tra vé và trao tiền mặt đều có bước tương ứng ở luồng trực tuyến), kết quả giống nhau; hoàn tiền mặt tại quầy là luồng thay thế; theo ASM-04, ASM-15 (Chờ Q-41); UC-013 chuyển trạng thái Loại | REQ-35, REQ-37 đến REQ-39, REQ-41 | Mục tiêu; Sự kiện EV-13; Động từ |
| CAND-12 | Đổi vé tại quầy cho vé mua tại quầy | Giữ thành UC-015 | - | U-R10 a, U-R12: nhân viên bán vé làm thay khách; chênh lệch thu tiền mặt theo ASM-13; in vé giấy theo ASM-14; theo ASM-04 | REQ-36, REQ-42 đến REQ-45 | Mục tiêu; Sự kiện EV-14; Động từ |
| CAND-13 | Hoàn tiền mặt tại quầy cho vé mua tại quầy của chuyến bị huỷ | Giữ thành UC-018 | - | U-R13: phiên riêng của nhân viên bán vé khi khách đến quầy, tách khỏi Huỷ chuyến của nhân viên điều hành; kênh hoàn theo ASM-08 | REQ-57, REQ-58, REQ-59 | Mục tiêu; Sự kiện EV-17; Động từ |
| CAND-14 | Lập lịch chạy theo tuần | Giữ thành UC-016 | - | Một phiên của nhân viên điều hành, kết quả là lịch chạy của tuần; chọn cả phụ xe theo ASM-07 | REQ-46, REQ-47, REQ-51 đến REQ-54 | Mục tiêu; Sự kiện EV-15; Động từ |
| CAND-15 | Huỷ chuyến | Giữ thành UC-017 | - | U-R13: phiên riêng của nhân viên điều hành; SMS (U-R06) và hoàn tiền vé trực tuyến qua cổng là bước của UC này | REQ-55 đến REQ-59 | Mục tiêu; Sự kiện EV-16; Động từ |
| CAND-16 | Quản lý danh mục tuyến xe và bến xe | Tách thành CAND-17, CAND-18 | U-T11 | U-R04: mỗi loại dữ liệu danh mục một UC; bến xe được nguồn đếm riêng ("3 bến xe") và tuyến là dữ liệu khác | REQ-48 | Mục tiêu; Động từ |
| CAND-17 | Quản lý danh mục tuyến xe | Giữ thành UC-020 | - | U-R04, U-R15, ASM-06: danh mục do nhân viên điều hành duy trì | REQ-48, REQ-01 | Mục tiêu; Sự kiện EV-19 |
| CAND-18 | Quản lý danh mục bến xe | Giữ thành UC-019 | - | U-R04, U-R15, ASM-06 | REQ-48, REQ-01 | Mục tiêu; Sự kiện EV-18 |
| CAND-19 | Quản lý danh mục xe (loại xe, số chỗ, sơ đồ chỗ) | Giữ thành UC-021 | - | U-R04, U-R15, ASM-06: loại xe, số chỗ, sơ đồ chỗ là thuộc tính phụ của xe, nguồn mô tả theo "xe giường nằm 40 chỗ" | REQ-49, REQ-03, REQ-06 | Mục tiêu; Sự kiện EV-20 |
| CAND-20 | Quản lý danh mục tài xế | Giữ thành UC-022 | - | U-R04, U-R15, ASM-06 | REQ-50 | Mục tiêu; Sự kiện EV-21 |
| CAND-21 | Đặt giá vé theo tuyến và loại xe | Giữ thành UC-023 | - | U-R15: tham số nghiệp vụ do quản lý nhà xe đặt, nguồn nêu rõ; tách khỏi mức tăng giá ngày lễ theo U-R04 d (thời điểm và quy tắc tối đa 30% riêng) | REQ-60 | Mục tiêu; Sự kiện EV-22; Động từ |
| CAND-22 | Đặt mức tăng giá ngày lễ, Tết | Giữ thành UC-024 | - | U-R15, U-R04 d: nguồn nêu câu riêng với quy tắc riêng (phần trăm, khoảng ngày, tối đa 30%) | REQ-61, REQ-62 | Mục tiêu; Sự kiện EV-23; Động từ |
| CAND-23 | Xem báo cáo doanh thu | Giữ thành UC-027 | - | U-R05: gộp báo cáo theo ngày và theo tuyến, cùng tác nhân, cùng cách thao tác (chọn kỳ, chọn tiêu chí, xem) | REQ-71, REQ-72 | Mục tiêu; Sự kiện EV-24; Động từ |
| CAND-24 | Xem báo cáo tỉ lệ lấp đầy chỗ của từng chuyến | Giữ thành UC-028 | - | U-R05: tách khỏi báo cáo doanh thu vì mục đích khác (khai thác chỗ, không phải tài chính) | REQ-73 | Mục tiêu; Sự kiện EV-25; Động từ |
| CAND-25 | Quản lý tài khoản nhân viên nhà xe | Giữ thành UC-002 | - | U-R03, U-R15, ASM-02: quản lý nhà xe quản lý tài khoản; thao tác cụ thể nguồn chỉ nêu "quản lý" | REQ-24 | Mục tiêu; Sự kiện EV-26; Động từ |
| CAND-26 | Soát vé hành khách lên xe | Giữ thành UC-026 | - | U-R14: một phiên soát nhiều vé trên một chuyến; U-R18: người thao tác là phụ xe, máy là nền tảng chạy ứng dụng nội bộ (ASM-10) nên không ghi tác nhân phụ | REQ-63, REQ-65, REQ-66 | Mục tiêu; Sự kiện EV-27; Động từ |
| CAND-27 | Soát vé khi xe ở vùng mất sóng | Gộp vào UC-026 | U-AP12 | Trùng nghĩa với CAND-26, cùng tác nhân và kết quả; khác biệt là luồng thay thế (lưu cục bộ, gửi lại khi có sóng) | REQ-67, REQ-68 | Mục tiêu; Sự kiện EV-27 |
| CAND-28 | Tự huỷ vé đặt qua điện thoại chưa thanh toán đúng hạn | Giữ thành UC-007 | U-T3, U-T5 (ghi đè bởi U-R07) | U-R07: nguồn nêu mốc 60 phút trước giờ xuất bến, không có người ra lệnh, kết quả có giá trị (trả chỗ), mốc rơi vào lúc không còn phiên mở; tác nhân chính ACT-09 | REQ-31, REQ-32 | Sự kiện EV-12; Mục tiêu; Động từ |
| CAND-29 | Gửi danh sách hành khách của chuyến về máy soát vé | Giữ thành UC-025 | U-T3, U-T4 (ghi đè bởi U-R07) | U-R07 (tác vụ chuyển dữ liệu giữa hai thành phần Trong ranh giới theo mốc 15 phút nguồn nêu); bên hưởng lợi là phụ xe; ASM-10 | REQ-69, REQ-70 | Sự kiện EV-28; Mục tiêu; Động từ |
| CAND-30 | Bán vé cho hành khách | Tách thành CAND-02, CAND-08, CAND-09 | U-T1, U-T6, U-AP04 | Summary gom ba kênh với tác nhân chính khác nhau và nhiều phiên; việc thu tiền vé đặt qua điện thoại tách ra thành CAND-10 | REQ-04, REQ-22, REQ-28 | Mục tiêu |
| CAND-31 | Trả vé | Tách thành CAND-06, CAND-11 | U-T8, U-AP05 | Nguồn nêu "đổi hoặc trả vé" chung (Mục 5, câu 1); ASM-04 chia theo kênh mua vé, hai tác nhân chính khác nhau; hai ứng viên sau tách được gộp lại thành UC-012 theo U-R10 b (ASM-15) | REQ-33, REQ-35 | Động từ; Sự kiện EV-07, EV-13 |
| CAND-32 | Đổi vé | Tách thành CAND-07, CAND-12 | U-T8, U-AP05 | Như CAND-31; theo ASM-04 | REQ-34, REQ-36 | Động từ; Sự kiện EV-08, EV-14 |
| CAND-33 | Xem sơ đồ chỗ của chuyến | Gộp vào UC-008 | U-T1, U-AP12 | U-R17, U-R05: tìm rồi xem sơ đồ chỗ là một UC; trùng nghĩa với CAND-01 | REQ-06 | Động từ; Sự kiện EV-01 |
| CAND-34 | Chọn chuyến và chỗ cho vé (dùng ở đặt vé, bán vé, đổi vé) | Tách thành CAND-01, CAND-35 | U-T1, U-T4 | Phần tìm chuyến và xem sơ đồ đã là UC-008 (đoạn dùng chung, ứng viên include ở P03 cho UC-009, UC-004, UC-005, UC-014, UC-015); phần còn lại là CAND-35 | REQ-07, REQ-29 | Động từ |
| CAND-35 | Chọn chỗ trên sơ đồ chỗ | Là bước của UC-009 | U-T1, U-T4, U-AP01 | Dưới 3 bước, không thoả Q4; đồng thời là bước của UC-004, UC-005, UC-014, UC-015; giới hạn tối đa 5 chỗ ở REQ-08 (Q-12 cho luồng quầy) | REQ-07, REQ-08, REQ-29 | Động từ |
| CAND-36 | Nhập họ tên và số điện thoại người đi | Là bước của UC-009 | U-T1, U-AP01 | Một thao tác nhập dữ liệu; đồng thời là bước của UC-004, UC-005 (Q-11) | REQ-09 | Động từ |
| CAND-37 | Gửi mã xác thực đăng nhập qua SMS | Là bước của UC-003 | U-T9, U-AP03 | U-R06: hệ quả của đăng nhập, Cổng SMS là tác nhân phụ; theo ASM-01 | REQ-12 | Động từ |
| CAND-38 | Giữ các chỗ đã chọn trong 10 phút | Là bước của UC-009 | U-T9, U-AP03 | Hành vi của hệ thống trong phiên đặt vé; thời điểm bắt đầu tính chờ Q-18 | REQ-13, REQ-14 | Động từ |
| CAND-39 | Thanh toán vé trực tuyến qua cổng thanh toán | Giữ thành UC-010 | U-T1, U-T3 (Subfunction giữ theo Q4 d) | Q4 d: kết quả riêng (tiền đã được cổng xác nhận); nguồn mô tả tách bạch (cổng, REQ-16 riêng, giữ chỗ 10 phút); thanh toán lại độc lập theo ASM-12 (Chờ Q-17) mà không huỷ việc đặt. UC-014 dùng khi thu chênh lệch (Q4 b, ASM-13) | REQ-15, REQ-16, REQ-17 | Mục tiêu; Động từ |
| CAND-40 | Trao đổi thông tin thanh toán và hoàn tiền với cổng thanh toán | Là bước của UC-010 | U-T9, U-AP03 | U-R08: cổng là tác nhân phụ, phản hồi tức thời trong phiên (ASM-11); phần hoàn tiền thuộc CAND-49, CAND-57 | REQ-16 | Động từ |
| CAND-41 | Trả chỗ cho người khác khi hết 10 phút chưa thanh toán thành công | Là bước của UC-009 | U-T9, U-AP11 | U-R07 hết giờ trong phiên: luồng thay thế của UC-009; không tạo UC riêng, không tạo tác nhân thời gian | REQ-14, REQ-17 | Sự kiện EV-03; Động từ |
| CAND-42 | Phát hành vé khi thanh toán thành công | Là bước của UC-009 | U-T9, U-AP03 | Hệ quả của thanh toán thành công, mỗi chỗ một mã vé (REQ-19) | REQ-18, REQ-19 | Động từ |
| CAND-43 | Gửi mã vé qua SMS tới số điện thoại người đi | Là bước của UC-009 | U-T9, U-AP03 | U-R06: Cổng SMS là tác nhân phụ của UC-009; đồng thời là bước của UC-014 với mã vé mới (ASM-16); SMS thất bại chờ Q-35 | REQ-20 | Động từ |
| CAND-44 | Trao đổi nội dung SMS với cổng SMS | Là bước của UC-009 | U-T9, U-AP03 | U-R06, U-R08: cổng là tác nhân phụ; đồng thời dùng ở UC-003, UC-014, UC-017 | REQ-21 | Động từ |
| CAND-45 | Thu tiền mặt khi bán vé tại quầy | Là bước của UC-004 | U-T1, U-AP01 | Bước của bán vé tại quầy | REQ-25 | Động từ |
| CAND-46 | In vé giấy có mã vạch | Là bước của UC-004 | U-T1, U-AP06 | Bước của bán vé tại quầy; đồng thời là bước của UC-006, UC-015 theo ASM-14 | REQ-26 | Động từ |
| CAND-47 | Trao đổi dữ liệu vé với máy in vé nhiệt | Là bước của UC-004 | U-T9, U-AP03 | U-R18: máy in nằm ngoài ranh giới (P01), là tác nhân phụ | REQ-27 | Động từ |
| CAND-48 | Tính mức hoàn tiền khi trả vé (90%, 50%, không được trả) | Là bước của UC-012 | U-T9, U-AP03 | Tính toán nội bộ; áp dụng cho cả vé mua trực tuyến và vé mua tại quầy | REQ-37, REQ-38, REQ-39 | Động từ |
| CAND-49 | Hoàn tiền vé mua trực tuyến qua cổng thanh toán | Là bước của UC-012 | U-T1 (Subfunction không đạt Q4) | Q4 a: chỉ UC-012 bắt buộc có đoạn này (UC-017 có thể không có vé trực tuyến); Q4 d: nguồn không nêu việc hoàn tiền thất bại độc lập; Q-20 | REQ-40, REQ-16 | Động từ |
| CAND-50 | Hoàn tiền mặt tại quầy khi trả vé | Là bước của UC-012 | U-T1, U-AP01 | Luồng thay thế của trả vé cho vé mua tại quầy; người thực hiện là nhân viên bán vé (ASM-04, ASM-15) | REQ-41 | Động từ |
| CAND-51 | Thu phần chênh lệch khi đổi sang vé đắt hơn | Là bước của UC-014 | U-T1, U-AP01 | Trực tuyến: qua UC-010 (Q4 b, ASM-13); tại quầy: tiền mặt, bước của UC-015 | REQ-44 | Động từ |
| CAND-52 | Hoàn phần chênh lệch khi đổi sang vé rẻ hơn | Là bước của UC-014 | U-T9 | ASM-05 (Chờ Q-08): không hoàn, chỉ là nhánh của luồng đổi vé, không có hành vi riêng; đồng thời áp dụng cho UC-015 | REQ-45 | Động từ |
| CAND-53 | Chọn tuyến, giờ xuất bến, xe, tài xế, phụ xe cho chuyến | Là bước của UC-016 | U-T1, U-AP01 | Bước của lập lịch chạy; phụ xe theo ASM-07 | REQ-47, REQ-51 | Động từ |
| CAND-54 | Kiểm tra chồng lịch của xe, tài xế và giới hạn 10 giờ lái trong ngày | Là bước của UC-016 | U-T9, U-AP03 | Kiểm tra hợp lệ nội bộ khi lập lịch; Q-15, Q-16 | REQ-52, REQ-53, REQ-54 | Động từ |
| CAND-55 | Gửi SMS thông báo huỷ chuyến cho hành khách đã có vé | Là bước của UC-017 | U-T9, U-AP03 | U-R06: hệ quả của huỷ chuyến, Cổng SMS là tác nhân phụ; Q-25 | REQ-56 | Động từ; Sự kiện EV-16 |
| CAND-56 | Hoàn tiền vé của chuyến bị huỷ | Tách thành CAND-13, CAND-57 | U-T8, U-AP05 | Hai người thực hiện vào hai thời điểm: hoàn qua cổng khi huỷ chuyến (CAND-57), hoàn tiền mặt tại quầy khi khách đến (CAND-13), theo ASM-08 | REQ-57, REQ-58, REQ-59 | Động từ; Sự kiện EV-16 |
| CAND-57 | Hoàn tiền vé mua trực tuyến của chuyến bị huỷ qua cổng thanh toán | Là bước của UC-017 | U-T1 (Subfunction không đạt Q4) | Cùng lý do Q4 như CAND-49; cổng thanh toán là tác nhân phụ của UC-017 | REQ-57, REQ-58, REQ-59, REQ-16 | Động từ; Sự kiện EV-16 |
| CAND-58 | Báo hợp lệ hoặc không hợp lệ cho mã vé đã quét | Là bước của UC-026 | U-T1, U-AP01 | Bước của soát vé; ba trường hợp không hợp lệ chờ Q-28 | REQ-65, REQ-66 | Động từ; Sự kiện EV-27 |
| CAND-59 | Gửi lại kết quả soát vé cho hệ thống khi có sóng | Là bước của UC-026 | U-T9, U-AP11 | U-R09: hệ quả của việc soát vé khi mất sóng; ứng viên là phần của ứng dụng nội bộ (ASM-10) | REQ-68 | Sự kiện EV-29; Động từ |
| CAND-60 | Xem báo cáo doanh thu theo ngày | Gộp vào UC-027 | U-T11, U-AP12 | U-R05: cùng tác nhân, cùng cách thao tác với CAND-23, chỉ khác tiêu chí | REQ-71 | Động từ |
| CAND-61 | Xem báo cáo doanh thu theo tuyến | Gộp vào UC-027 | U-T11, U-AP12 | U-R05 như CAND-60 | REQ-72 | Động từ |
| CAND-62 | Không để hai vé cùng một chỗ trên một chuyến | Là bước của UC-009 | U-T9, U-AP03 | Quy tắc kiểm soát nội bộ khi giữ chỗ và phát hành vé; đồng thời áp dụng cho UC-004, UC-005, UC-014, UC-015 | REQ-75 | Động từ |
| CAND-63 | Xử lý thanh toán thẻ và lưu thông tin thẻ của hành khách | Loại | U-T10, U-AP13 | U-R16: ngoài phạm vi theo P00, trích "Hệ thống không lưu thông tin thẻ của hành khách" (Mục 10, câu 3) | REQ-76 | Động từ |
| CAND-64 | Truyền SMS qua mạng viễn thông | Loại | U-T10, U-AP13 | U-R16: ngoài phạm vi theo P00, do cổng SMS của nhà mạng đảm nhiệm (project-profile.md, HE_THONG_NGOAI) | REQ-21 | Động từ |
| CAND-65 | Cung cấp phần cứng máy soát vé cầm tay và máy in vé nhiệt | Loại | U-T10, U-AP13 | U-R16: ngoài phạm vi theo P00, máy soát vé "do nhà xe tự trang bị" (project-profile.md, HE_THONG_NGOAI) | REQ-27, REQ-77 | Động từ |
| CAND-66 | Chịu được khoảng 2.000 người truy cập cùng lúc vào dịp Tết | Loại | U-T9, U-AP16 | Yêu cầu phi chức năng, chuyển P06 | REQ-74 | Động từ |

## 4. Bảng use case

Bảng 4a. Bảng lõi

| UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mức | Nhóm chức năng |
|---|---|---|---|---|---|---|
| UC-001 | Đăng ký tài khoản | Register Account | ACT-01 Hành khách | - | User-goal | Tài khoản |
| UC-002 | Quản lý tài khoản nhân viên | Manage Staff Accounts | ACT-04 Quản lý nhà xe | - | User-goal | Tài khoản |
| UC-003 | Đăng nhập | Log In | ACT-01, ACT-02 Nhân viên bán vé, ACT-03 Nhân viên điều hành, ACT-04, ACT-05 Phụ xe | ACT-07 Cổng SMS | Subfunction | Tài khoản |
| UC-004 | Bán vé tại quầy | Sell Ticket At Counter | ACT-02 | ACT-08 Máy in vé | User-goal | Bán vé tại quầy |
| UC-005 | Nhận đặt chỗ qua điện thoại | Take Phone Reservation | ACT-02 | - | User-goal | Bán vé tại quầy |
| UC-006 | Thu tiền vé đặt qua điện thoại | Collect Payment For Phone Reservation | ACT-02 | ACT-08 | User-goal | Bán vé tại quầy |
| UC-007 | Huỷ vé đặt chỗ quá hạn | Cancel Overdue Reservation | ACT-09 Bộ định thời | - | User-goal | Bán vé tại quầy |
| UC-008 | Tra cứu chuyến xe | Search Trips | ACT-01; ACT-02 Nhân viên bán vé (qua UC-004, UC-005, UC-015) | - | User-goal | Đặt vé trực tuyến |
| UC-009 | Đặt vé trực tuyến | Book Ticket Online | ACT-01 | ACT-07 | User-goal | Đặt vé trực tuyến |
| UC-010 | Thanh toán vé trực tuyến | Pay Ticket Online | ACT-01 (qua UC-009, UC-014) | ACT-06 Cổng thanh toán | Subfunction | Đặt vé trực tuyến |
| UC-011 | Xem lịch sử vé | View Ticket History | ACT-01 | - | User-goal | Đặt vé trực tuyến |
| UC-012 | Trả vé | Return Ticket | ACT-01, ACT-02 | ACT-06 (nhánh hoàn qua cổng thanh toán) | User-goal | Trả vé và đổi vé |
| UC-013 | Trả vé tại quầy | Return Ticket At Counter | - | - | Loại (gộp vào UC-012) | Trả vé và đổi vé |
| UC-014 | Đổi vé trực tuyến | Exchange Ticket Online | ACT-01 | ACT-07 Cổng SMS | User-goal | Trả vé và đổi vé |
| UC-015 | Đổi vé tại quầy | Exchange Ticket At Counter | ACT-02 | ACT-08 | User-goal | Trả vé và đổi vé |
| UC-016 | Lập lịch chạy tuần | Create Weekly Schedule | ACT-03 | - | User-goal | Lịch chạy và chuyến |
| UC-017 | Huỷ chuyến | Cancel Trip | ACT-03 | ACT-06, ACT-07 | User-goal | Lịch chạy và chuyến |
| UC-018 | Hoàn tiền mặt chuyến bị huỷ | Refund Cash For Cancelled Trip | ACT-02 | - | User-goal | Lịch chạy và chuyến |
| UC-019 | Quản lý danh mục bến xe | Manage Station Catalog | ACT-03 | - | User-goal | Danh mục |
| UC-020 | Quản lý danh mục tuyến xe | Manage Route Catalog | ACT-03 | - | User-goal | Danh mục |
| UC-021 | Quản lý danh mục xe | Manage Vehicle Catalog | ACT-03 | - | User-goal | Danh mục |
| UC-022 | Quản lý danh mục tài xế | Manage Driver Catalog | ACT-03 | - | User-goal | Danh mục |
| UC-023 | Đặt giá vé | Set Ticket Fare | ACT-04 | - | User-goal | Giá vé |
| UC-024 | Đặt mức tăng giá ngày lễ | Set Holiday Surcharge | ACT-04 | - | User-goal | Giá vé |
| UC-025 | Gửi danh sách hành khách cho phụ xe | Send Passenger List To Attendant | ACT-09 | - | User-goal | Soát vé |
| UC-026 | Soát vé hành khách lên xe | Check Ticket At Boarding | ACT-05 | - | User-goal | Soát vé |
| UC-027 | Xem báo cáo doanh thu | View Revenue Report | ACT-04 | - | User-goal | Báo cáo |
| UC-028 | Xem báo cáo tỉ lệ lấp đầy | View Occupancy Report | ACT-04 | - | User-goal | Báo cáo |

Bảng 4b. Bảng mô tả

| UC | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | REQ | CAND nguồn |
|---|---|---|---|---|---|
| UC-001 | Hành khách có tài khoản gắn với số điện thoại để xem lại lịch sử vé. | Hành khách chưa có tài khoản đăng ký tài khoản bằng số điện thoại. Đặt vé không bắt buộc có tài khoản. | Hành khách muốn có tài khoản (EV-04) | REQ-10 | CAND-03 |
| UC-002 | Quản lý nhà xe có danh sách tài khoản nhân viên đúng với các vai trò đang làm việc. | Quản lý nhà xe quản lý tài khoản của nhân viên bán vé, nhân viên điều hành, quản lý nhà xe và phụ xe (ASM-02). Nguồn không nêu thao tác cụ thể nên P04 chốt thao tác theo câu trả lời Q-01. | Nhà xe cần cấp hoặc đổi tài khoản nhân viên (EV-26) | REQ-24 | CAND-25 |
| UC-003 | Người dùng vào được hệ thống với đúng vai trò của mình. | Điều kiện để dùng các UC cần tài khoản (xem lịch sử vé, mọi UC của nhân viên nhà xe); các UC này ghi việc đã đăng nhập là tiền điều kiện ở P04. Hành khách đăng nhập bằng mã xác thực gửi qua SMS (ASM-01); nhân viên nhà xe đăng nhập bằng tài khoản riêng theo vai trò (ASM-02). Subfunction giữ theo U-R01. | Người dùng muốn vào hệ thống bằng tài khoản (EV-05) | REQ-12, REQ-23, REQ-21 | CAND-05, CAND-37 |
| UC-004 | Khách mua trực tiếp nhận được vé giấy có mã vạch cho chỗ đã chọn trên chuyến, sau khi trả tiền mặt. | Nhân viên bán vé chọn chuyến và chỗ còn trống cho khách (ASM-03), nhập họ tên và số điện thoại người đi, thu tiền mặt rồi in vé giấy qua máy in vé. Có thể bán nhiều chỗ trong một lần; giới hạn số chỗ chờ Q-12. | Khách đến quầy muốn mua vé trực tiếp (EV-09) | REQ-07, REQ-09, REQ-19, REQ-22, REQ-25, REQ-26, REQ-27, REQ-29, REQ-75 | CAND-08, CAND-45, CAND-46, CAND-47 |
| UC-005 | Khách gọi điện có chỗ được giữ trên chuyến đến hạn thanh toán tại quầy. | Nhân viên bán vé nhận cuộc gọi, chọn chuyến và chỗ còn trống cho khách (ASM-03), nhập họ tên và số điện thoại người đi, giữ chỗ đến hạn chậm nhất 60 phút trước giờ xuất bến. Trường hợp đặt khi còn dưới 60 phút chờ Q-14. | Khách gọi điện muốn đặt chỗ (EV-10) | REQ-07, REQ-09, REQ-28, REQ-29, REQ-31, REQ-75 | CAND-09 |
| UC-006 | Khách đã đặt chỗ qua điện thoại có vé đã thanh toán tại quầy. | Nhân viên bán vé tìm vé đặt qua điện thoại của khách, thu tiền mặt và xác nhận đã thanh toán; in vé giấy theo ASM-14 (Chờ Q-40). | Khách đã đặt chỗ đến quầy thanh toán (EV-11) | REQ-26, REQ-27, REQ-30, REQ-31 | CAND-10 |
| UC-007 | Chỗ của vé đặt qua điện thoại quá hạn thanh toán được trả lại để người khác đặt. | Đến 60 phút trước giờ xuất bến, hệ thống huỷ các vé đặt qua điện thoại chưa thanh toán tại quầy và trả chỗ. Bên hưởng lợi là hành khách khác và nhà xe. | Đến 60 phút trước giờ xuất bến mà vé chưa thanh toán (EV-12) | REQ-31, REQ-32 | CAND-28 |
| UC-008 | Hành khách biết các chuyến phù hợp và các chỗ còn trống mà không cần tài khoản. | Hành khách tìm chuyến theo điểm đi, điểm đến, ngày đi và xem sơ đồ chỗ của chuyến. Đoạn tương tác này cũng là phần đầu của các UC đặt, bán, đổi vé (ứng viên include ở P03 cho UC-009, UC-004, UC-005, UC-014, UC-015); nhân viên bán vé thao tác đoạn này trong UC-004, UC-005, UC-015 (ASM-03) nên ACT-02 ghi "(qua ...)". Điểm đi, điểm đến là bến xe hay tỉnh chờ Q-10. | Hành khách muốn tìm chuyến và xem chỗ trống (EV-01) | REQ-05, REQ-06 | CAND-01, CAND-33, CAND-34 |
| UC-009 | Hành khách có vé đã phát hành, mỗi chỗ một mã vé, và nhận mã vé qua SMS. | Hành khách chọn chỗ (tối đa 5 chỗ), nhập họ tên và số điện thoại người đi, các chỗ được giữ 10 phút để thanh toán qua UC-010; thanh toán thành công thì vé được phát hành và mã vé gửi qua SMS. Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại (luồng thay thế, U-R07). Không bắt buộc có tài khoản. | Hành khách muốn mua vé xe trực tuyến (EV-02); đến 10 phút giữ chỗ (EV-03) | REQ-04, REQ-07, REQ-08, REQ-09, REQ-13, REQ-14, REQ-17, REQ-18, REQ-19, REQ-20, REQ-21, REQ-75 | CAND-02, CAND-35, CAND-36, CAND-38, CAND-41, CAND-42, CAND-43, CAND-44, CAND-62 |
| UC-010 | Hành khách có khoản tiền vé đã được cổng thanh toán xác nhận. | Hành khách thanh toán các chỗ đang giữ qua cổng thanh toán của đối tác; thanh toán không thành công thì được thanh toán lại đến hết thời gian giữ chỗ (ASM-12, Chờ Q-17). Điều kiện Q4: Q4 d với UC-009; Q4 b với UC-014 (chỉ khi vé mới đắt hơn, ASM-13). Hệ thống không lưu thông tin thẻ. | Hành khách chuyển sang thanh toán trong UC-009 hoặc UC-014 | REQ-15, REQ-16, REQ-17, REQ-44, REQ-76 | CAND-39, CAND-40 |
| UC-011 | Hành khách có tài khoản xem được các vé đã đặt. | Hành khách đã đăng nhập xem lại lịch sử vé. Vé nào được tính vào lịch sử chờ Q-26. | Hành khách muốn xem lại các vé đã đặt (EV-06) | REQ-11 | CAND-04 |
| UC-012 | Khách có vé đã trả và nhận lại tiền theo mức hoàn: qua cổng thanh toán với vé mua trực tuyến, bằng tiền mặt tại quầy với vé mua tại quầy. | Hành khách trả vé mua trực tuyến, hoặc nhân viên bán vé trả vé tại quầy cho vé mua tại quầy (ASM-04, ASM-15, Chờ Q-41), trước giờ xuất bến: từ 24 giờ trở lên hoàn 90%, từ 4 giờ đến dưới 24 giờ hoàn 50%, dưới 4 giờ không được trả. Vé mua trực tuyến được hoàn qua cổng thanh toán; vé mua tại quầy được hoàn tiền mặt tại quầy (luồng thay thế). Cách xác thực quyền trả vé của hành khách không có tài khoản chờ Q-37; hoàn một phần chờ Q-20. | Hành khách muốn trả vé mua trực tuyến (EV-07); khách có vé mua tại quầy muốn trả vé (EV-13) | REQ-16, REQ-33, REQ-35, REQ-37, REQ-38, REQ-39, REQ-40, REQ-41 | CAND-06, CAND-11, CAND-31, CAND-48, CAND-49, CAND-50 |
| UC-013 | Loại: gộp vào UC-012 (UCR-02, ASM-15, Chờ Q-41). | Mã giữ lại, không còn là use case; phần việc trả vé tại quầy cho vé mua tại quầy nằm trong UC-012. Q-41 trả lời "Có, ghi rõ đoạn đó" thì khôi phục UC-013 thành User-goal của ACT-02. | - | - | CAND-11 |
| UC-014 | Hành khách có vé mới ở chuyến khác cùng tuyến thay cho vé cũ. | Hành khách đổi vé mua trực tuyến một lần, chậm nhất 4 giờ trước giờ xuất bến (mốc tính theo chuyến nào chờ Q-21), trả thêm chênh lệch qua UC-010 nếu vé mới đắt hơn (ASM-13); vé mới rẻ hơn không hoàn chênh lệch (ASM-05). Vé mới có mã vé riêng, mã vé mới gửi qua SMS tới số điện thoại người đi (ASM-16, Chờ Q-42). | Hành khách muốn đổi vé mua trực tuyến (EV-08) | REQ-20, REQ-21, REQ-34, REQ-42, REQ-43, REQ-44, REQ-45, REQ-75 | CAND-07, CAND-32, CAND-51, CAND-52 |
| UC-015 | Khách có vé mua tại quầy có vé mới ở chuyến khác cùng tuyến thay cho vé cũ. | Nhân viên bán vé đổi vé tại quầy cho vé mua tại quầy (ASM-04) với các điều kiện như UC-014, thu thêm chênh lệch bằng tiền mặt (ASM-13), in vé giấy mới (ASM-14, Chờ Q-40). | Khách có vé mua tại quầy muốn đổi vé (EV-14) | REQ-26, REQ-27, REQ-36, REQ-42, REQ-43, REQ-44, REQ-45, REQ-75 | CAND-12, CAND-32, CAND-51, CAND-52 |
| UC-016 | Nhân viên điều hành có lịch chạy của tuần, mỗi chuyến có đủ tuyến, giờ xuất bến, xe, tài xế và phụ xe, không vi phạm ràng buộc. | Nhân viên điều hành chọn cho mỗi chuyến tuyến, giờ xuất bến, xe, tài xế và phụ xe (ASM-07). Xe, tài xế không được xếp vào hai chuyến chồng thời gian; tài xế không lái quá 10 giờ một ngày. | Nhà xe cần lịch chạy của tuần (EV-15) | REQ-02, REQ-46, REQ-47, REQ-51, REQ-52, REQ-53, REQ-54 | CAND-14, CAND-53, CAND-54 |
| UC-017 | Chuyến bị huỷ, hành khách đã có vé được báo và vé trực tuyến được hoàn 100% giá vé. | Nhân viên điều hành huỷ chuyến khi xe hỏng, thời tiết; hệ thống gửi SMS cho hành khách đã có vé và hoàn 100% vé mua trực tuyến qua cổng thanh toán. Vé mua tại quầy hoàn tiền mặt tại quầy qua UC-018 (ASM-08). | Chuyến phải huỷ (EV-16) | REQ-55, REQ-56, REQ-57, REQ-58, REQ-59, REQ-16, REQ-21 | CAND-15, CAND-55, CAND-56, CAND-57 |
| UC-018 | Khách có vé mua tại quầy của chuyến bị huỷ nhận lại 100% giá vé bằng tiền mặt. | Nhân viên bán vé hoàn tiền mặt tại quầy cho khách có vé mua tại quầy của chuyến đã bị huỷ (ASM-08). | Khách có vé quầy của chuyến bị huỷ đến quầy nhận hoàn tiền (EV-17) | REQ-57, REQ-58, REQ-59 | CAND-13, CAND-56 |
| UC-019 | Danh mục bến xe đúng với các bến nhà xe đang khai thác. | Nhân viên điều hành duy trì danh mục bến xe (ASM-06). Nguồn chỉ nêu "quản lý" nên thao tác cụ thể do P04 chốt. | Nhà xe cần thêm hoặc đổi dữ liệu bến xe (EV-18) | REQ-48, REQ-01 | CAND-18 |
| UC-020 | Danh mục tuyến xe đúng với các tuyến nhà xe đang khai thác. | Nhân viên điều hành duy trì danh mục tuyến xe (ASM-06). Thao tác cụ thể do P04 chốt. | Nhà xe cần thêm hoặc đổi dữ liệu tuyến xe (EV-19) | REQ-48, REQ-01 | CAND-17 |
| UC-021 | Danh mục xe đúng với đội xe, mỗi xe có loại xe, số chỗ và sơ đồ chỗ. | Nhân viên điều hành duy trì danh mục xe gồm loại xe, số chỗ, sơ đồ chỗ của từng loại xe (ASM-06). Thao tác cụ thể do P04 chốt. | Nhà xe cần thêm hoặc đổi dữ liệu xe (EV-20) | REQ-49, REQ-03, REQ-06 | CAND-19 |
| UC-022 | Danh mục tài xế đúng với các tài xế nhà xe đang có. | Nhân viên điều hành duy trì danh mục tài xế (ASM-06). Thao tác cụ thể do P04 chốt. | Nhà xe cần thêm hoặc đổi dữ liệu tài xế (EV-21) | REQ-50 | CAND-20 |
| UC-023 | Giá vé theo từng tuyến và loại xe do quản lý nhà xe đặt. | Quản lý nhà xe đặt giá vé theo tuyến và loại xe. | Quản lý cần đặt hoặc đổi giá vé (EV-22) | REQ-60 | CAND-21 |
| UC-024 | Giá vé trong khoảng ngày lễ, Tết được tăng đúng mức quản lý đặt. | Quản lý nhà xe đặt mức tăng giá theo phần trăm cho một khoảng ngày, tối đa 30%. Chỉ ngày lễ, Tết hay bất kỳ khoảng ngày chờ Q-23; áp dụng theo ngày xuất bến hay ngày mua chờ Q-24. | Đến dịp lễ, Tết quản lý cần tăng giá (EV-23) | REQ-61, REQ-62 | CAND-22 |
| UC-025 | Phụ xe của chuyến có sẵn danh sách hành khách trên máy soát vé trước giờ xuất bến. | Đến 15 phút trước giờ xuất bến, hệ thống gửi danh sách hành khách của chuyến cho ứng dụng soát vé của phụ xe (ASM-10); bên hưởng lợi là phụ xe. Nội dung danh sách chờ Q-30. | Đến 15 phút trước giờ xuất bến (EV-28) | REQ-69, REQ-70 | CAND-29 |
| UC-026 | Phụ xe biết mã vé quét được hợp lệ hay không hợp lệ và vé hợp lệ được ghi nhận đã soát. | Phụ xe quét mã vé của từng hành khách lên xe và nhận kết quả hợp lệ hay không hợp lệ (sai chuyến, vé đã huỷ, vé đã soát). Khi xe ở vùng mất sóng vẫn soát được, kết quả lưu cục bộ và gửi lại hệ thống khi có sóng (EV-29). | Hành khách lên xe, phụ xe cần soát vé (EV-27) | REQ-63, REQ-64, REQ-65, REQ-66, REQ-67, REQ-68, REQ-77 | CAND-26, CAND-27, CAND-58, CAND-59 |
| UC-027 | Quản lý nhà xe biết doanh thu theo ngày hoặc theo tuyến. | Quản lý nhà xe chọn kỳ hoặc tuyến và xem báo cáo doanh thu theo ngày, theo tuyến. Doanh thu có trừ tiền hoàn hay không chờ Q-32. | Quản lý cần biết doanh thu (EV-24) | REQ-71, REQ-72 | CAND-23, CAND-60, CAND-61 |
| UC-028 | Quản lý nhà xe biết tỉ lệ lấp đầy chỗ của từng chuyến. | Quản lý nhà xe xem báo cáo tỉ lệ lấp đầy chỗ của từng chuyến. Chỗ đang giữ chưa thanh toán có tính hay không chờ Q-33. | Quản lý cần biết mức lấp đầy chỗ (EV-25) | REQ-73 | CAND-24 |

## 5. Ma trận truy vết REQ --> UC

| REQ | Nội dung tóm tắt | UC phủ | Ghi chú (lý do nếu không phủ) |
|---|---|---|---|
| REQ-01 | 12 tuyến, 3 bến xe | UC-019, UC-020 | Dữ liệu quy mô; Chuyển P06 phần số liệu |
| REQ-02 | Khoảng 80 chuyến mỗi ngày | UC-016 | Dữ liệu quy mô; Chuyển P06 phần số liệu |
| REQ-03 | Đội xe 50 xe giường nằm, 20 xe ghế ngồi | UC-021 | Dữ liệu quy mô; Chuyển P06 phần số liệu |
| REQ-04 | Hành khách đặt vé qua website, không bắt buộc tài khoản | UC-009 | - |
| REQ-05 | Tìm chuyến theo điểm đi, điểm đến, ngày đi | UC-008 | - |
| REQ-06 | Xem sơ đồ chỗ, chỗ còn trống | UC-008, UC-021 | UC-021 giữ dữ liệu sơ đồ chỗ |
| REQ-07 | Chọn chỗ còn trống khi đặt vé | UC-009, UC-004, UC-005 | Bước chọn chỗ |
| REQ-08 | Tối đa 5 chỗ một lần đặt | UC-009 | Quy tắc nghiệp vụ; luồng quầy chờ Q-12 |
| REQ-09 | Họ tên và số điện thoại người đi | UC-009, UC-004, UC-005 | Dữ liệu; Q-11 |
| REQ-10 | Đăng ký tài khoản bằng số điện thoại | UC-001 | - |
| REQ-11 | Xem lịch sử vé | UC-011 | - |
| REQ-12 | Đăng nhập bằng mã xác thực qua SMS | UC-003 | ASM-01 |
| REQ-13 | Giữ chỗ để thanh toán | UC-009 | - |
| REQ-14 | Giữ chỗ 10 phút | UC-009 | Quy tắc nghiệp vụ gắn UC-009 |
| REQ-15 | Thanh toán qua cổng thanh toán | UC-010 | Include trong UC-009 |
| REQ-16 | Trao đổi với cổng thanh toán | UC-010, UC-012, UC-017 | Giao tiếp ngoài |
| REQ-17 | Trả chỗ khi hết 10 phút | UC-009, UC-010 | U-R07 hết giờ trong phiên |
| REQ-18 | Phát hành vé khi thanh toán thành công | UC-009 | - |
| REQ-19 | Mỗi chỗ một mã vé | UC-009, UC-004 | Quy tắc nghiệp vụ |
| REQ-20 | Gửi mã vé qua SMS | UC-009, UC-014 | UC-014 theo ASM-16 |
| REQ-21 | Trao đổi với cổng SMS | UC-009, UC-003, UC-014, UC-017 | Giao tiếp ngoài; UC-014 theo ASM-16 |
| REQ-22 | Bán vé tại quầy | UC-004 | - |
| REQ-23 | Nhân viên nhà xe đăng nhập theo vai trò | UC-003 | ASM-02 |
| REQ-24 | Quản lý nhà xe quản lý tài khoản nhân viên | UC-002 | ASM-02 |
| REQ-25 | Thu tiền mặt | UC-004 | - |
| REQ-26 | In vé giấy có mã vạch | UC-004, UC-006, UC-015 | UC-006, UC-015 theo ASM-14 |
| REQ-27 | Trao đổi dữ liệu với máy in | UC-004, UC-006, UC-015 | Giao tiếp ngoài |
| REQ-28 | Nhận đặt chỗ qua điện thoại | UC-005 | - |
| REQ-29 | Nhân viên bán vé chọn chuyến và chỗ | UC-004, UC-005 | ASM-03 |
| REQ-30 | Thanh toán vé đặt qua điện thoại tại quầy | UC-006 | - |
| REQ-31 | Thanh toán chậm nhất 60 phút trước giờ xuất bến | UC-005, UC-006, UC-007 | Quy tắc nghiệp vụ |
| REQ-32 | Tự động huỷ vé quá hạn | UC-007 | - |
| REQ-33 | Hành khách trả vé | UC-012 | Kênh trực tuyến theo ASM-04 |
| REQ-34 | Hành khách đổi vé cùng tuyến | UC-014 | Kênh trực tuyến theo ASM-04 |
| REQ-35 | Nhân viên bán vé trả vé tại quầy | UC-012 | ASM-04; gộp vào UC-012 theo ASM-15 (UCR-02) |
| REQ-36 | Nhân viên bán vé đổi vé tại quầy | UC-015 | ASM-04 |
| REQ-37 | Hoàn 90% khi trả từ 24 giờ trở lên | UC-012 | Quy tắc nghiệp vụ |
| REQ-38 | Hoàn 50% khi trả từ 4 đến dưới 24 giờ | UC-012 | Quy tắc nghiệp vụ |
| REQ-39 | Không được trả khi dưới 4 giờ | UC-012 | Quy tắc nghiệp vụ |
| REQ-40 | Hoàn tiền vé trực tuyến qua cổng | UC-012 | - |
| REQ-41 | Hoàn tiền mặt tại quầy cho vé mua tại quầy | UC-012 | Chủ thể theo ASM-04; luồng thay thế của UC-012 (ASM-15) |
| REQ-42 | Mỗi vé đổi một lần | UC-014, UC-015 | Quy tắc nghiệp vụ |
| REQ-43 | Đổi chậm nhất 4 giờ trước giờ xuất bến | UC-014, UC-015 | Quy tắc nghiệp vụ; Q-21 |
| REQ-44 | Trả thêm chênh lệch khi vé mới đắt hơn | UC-014, UC-015, UC-010 | Q-22, ASM-13 |
| REQ-45 | Không hoàn chênh lệch khi vé mới rẻ hơn | UC-014, UC-015 | ASM-05 |
| REQ-46 | Lập lịch chạy theo tuần | UC-016 | - |
| REQ-47 | Chuyến gồm tuyến, giờ xuất bến, xe, tài xế | UC-016 | Dữ liệu |
| REQ-48 | Quản lý danh mục tuyến và bến | UC-019, UC-020 | ASM-06 |
| REQ-49 | Quản lý danh mục xe | UC-021 | ASM-06 |
| REQ-50 | Quản lý danh mục tài xế | UC-022 | ASM-06 |
| REQ-51 | Phụ xe của chuyến do điều hành chọn | UC-016 | ASM-07 |
| REQ-52 | Xe không xếp hai chuyến chồng nhau | UC-016 | Quy tắc nghiệp vụ |
| REQ-53 | Tài xế không xếp hai chuyến chồng nhau | UC-016 | Quy tắc nghiệp vụ |
| REQ-54 | Tài xế không lái quá 10 giờ một ngày | UC-016 | Quy tắc nghiệp vụ |
| REQ-55 | Nhân viên điều hành huỷ chuyến | UC-017 | - |
| REQ-56 | Gửi SMS cho hành khách đã có vé của chuyến bị huỷ | UC-017 | - |
| REQ-57 | Hoàn tiền vé của chuyến bị huỷ | UC-017, UC-018 | - |
| REQ-58 | Hoàn 100% giá vé | UC-017, UC-018 | Quy tắc nghiệp vụ |
| REQ-59 | Hoàn cùng kênh mua vé | UC-017, UC-018 | ASM-08 |
| REQ-60 | Quản lý đặt giá vé theo tuyến và loại xe | UC-023 | - |
| REQ-61 | Quản lý đặt mức tăng giá ngày lễ, Tết | UC-024 | - |
| REQ-62 | Mức tăng tối đa 30% | UC-024 | Quy tắc nghiệp vụ |
| REQ-63 | Phụ xe quét mã vé | UC-026 | - |
| REQ-64 | Trao đổi dữ liệu vé với máy soát vé | UC-026 | Giao tiếp ngoài; ASM-10 |
| REQ-65 | Máy báo hợp lệ hoặc không hợp lệ | UC-026 | - |
| REQ-66 | Ba trường hợp vé không hợp lệ | UC-026 | Quy tắc nghiệp vụ; Q-28 |
| REQ-67 | Soát được khi mất sóng | UC-026 | Phi chức năng gắn UC-026; Chuyển P06 phần ràng buộc |
| REQ-68 | Gửi lại kết quả khi có sóng | UC-026 | - |
| REQ-69 | Gửi danh sách hành khách về máy soát vé | UC-025 | - |
| REQ-70 | Gửi vào 15 phút trước giờ xuất bến | UC-025 | Quy tắc nghiệp vụ |
| REQ-71 | Báo cáo doanh thu theo ngày | UC-027 | - |
| REQ-72 | Báo cáo doanh thu theo tuyến | UC-027 | - |
| REQ-73 | Báo cáo tỉ lệ lấp đầy từng chuyến | UC-028 | - |
| REQ-74 | Chịu 2.000 người truy cập cùng lúc | - | Chuyển P06 (phi chức năng, CAND-66) |
| REQ-75 | Không hai vé cùng một chỗ trên một chuyến | UC-009, UC-004, UC-005, UC-014, UC-015 | Quy tắc nghiệp vụ xuyên các UC cấp chỗ |
| REQ-76 | Không lưu thông tin thẻ | UC-010 | Ràng buộc; Chuyển P06 |
| REQ-77 | Máy soát vé là thiết bị Android có đầu quét mã vạch | UC-026 | Ràng buộc; Chuyển P06 |

## 6. Thống kê và nhận xét ngưỡng

| ACT | Số UC là tác nhân chính | Số UC là tác nhân phụ | Nhận xét |
|---|---|---|---|
| ACT-01 Hành khách | 8 (6 User-goal, 2 Subfunction: UC-003, UC-010) | 0 | Trong khoảng 2-12 |
| ACT-02 Nhân viên bán vé | 8 (7 User-goal, 1 Subfunction: UC-003) | 0 | Trong khoảng 2-12; UC-008 tính theo "(qua UC-004, UC-005, UC-015)", UC-012 dùng chung với ACT-01 |
| ACT-03 Nhân viên điều hành | 7 (6 User-goal, 1 Subfunction: UC-003) | 0 | Trong khoảng 2-12; bốn UC là danh mục tách theo U-R04 |
| ACT-04 Quản lý nhà xe | 6 (5 User-goal, 1 Subfunction: UC-003) | 0 | Trong khoảng 2-12 |
| ACT-05 Phụ xe | 2 (1 User-goal, 1 Subfunction: UC-003) | 0 | Một User-goal đã gom soát vé thường và soát vé khi mất sóng; không gộp quá mức vì nguồn chỉ có một mục tiêu |
| ACT-06 Cổng thanh toán | 0 | 3 (UC-010, UC-012, UC-017) | - |
| ACT-07 Cổng SMS | 0 | 4 (UC-003, UC-009, UC-014, UC-017) | UC-014 theo ASM-16 |
| ACT-08 Máy in vé | 0 | 3 (UC-004, UC-006, UC-015) | UC-006, UC-015 theo ASM-14 |
| ACT-09 Bộ định thời | 2 (UC-007, UC-025) | 0 | Trong khoảng bình thường của tác nhân thời gian |

Tổng số UC: 27 hiệu lực (25 User-goal, 2 Subfunction) trên 28 mã UC; UC-013 trạng thái Loại, giữ mã.
Số UC mỗi nhóm: Tài khoản 3; Bán vé tại quầy 4; Đặt vé trực tuyến 4; Trả vé và đổi vé 3 (UC-012, UC-014, UC-015; UC-013 Loại); Lịch chạy và chuyến 3; Danh mục 4; Giá vé 2; Soát vé 2; Báo cáo 2.
Số UC mức Subfunction: 2 (UC-003, UC-010), chiếm khoảng 7% của 27 UC hiệu lực, dưới ngưỡng 20%.
Nhận xét: tổng số UC nằm trong khoảng 10-40 của hệ thống cỡ vừa. Ba nhóm Giá vé, Soát vé, Báo cáo chỉ có 2 UC, dưới ngưỡng 3 UC mỗi nhóm; giữ nguyên vì mỗi nhóm là một lĩnh vực nghiệp vụ riêng trong nguồn (Mục 7, Mục 8, Mục 9) và nhập vào nhóm khác làm sai ranh giới nghiệp vụ.

## Thay đổi so với phiên bản trước

| UCR | Phần tử đã đổi (UC, CAND, dòng REQ) | Thay đổi |
|---|---|---|
| UCR-01 | UC-008 (Bảng 4a, 4b); Mục 1 (thêm dòng ACT-02); CAND-01; Mục 6 dòng ACT-02 | Tác nhân chính của UC-008 thành "ACT-01; ACT-02 Nhân viên bán vé (qua UC-004, UC-005, UC-015)"; Mô tả ngắn nêu ACT-02 thao tác đoạn dùng chung; Mục 1 thêm mục tiêu tìm chuyến của ACT-02 (CAND-01, CAND-34); Lý do của CAND-01 nêu ACT-02; số UC của ACT-02 từ 7 thành 8. UC-008 giữ mức User-goal |
| UCR-02 | UC-012, UC-013 (Bảng 4a, 4b); CAND-06, CAND-11, CAND-31, CAND-48, CAND-50; Mục 5 dòng REQ-35, REQ-37, REQ-38, REQ-39, REQ-41; Mục 6; ASM-15; Q-41 | UC-013 chuyển Loại, giữ mã, gộp vào UC-012. UC-012 đổi tên "Trả vé" (Return Ticket), tác nhân chính ACT-01, ACT-02, tác nhân phụ ACT-06 (nhánh hoàn qua cổng thanh toán), REQ thêm REQ-35, REQ-41, CAND nguồn thêm CAND-11, CAND-50, sự kiện kích hoạt thêm EV-13. CAND-11 từ "Giữ thành UC-013" thành "Gộp vào UC-012"; CAND-06 đổi lý do sang U-R10 b; CAND-48, CAND-50, CAND-31 trỏ về UC-012. Mục 5 chuyển các REQ của UC-013 sang UC-012. Tổng UC hiệu lực 28 thành 27, nhóm "Trả vé và đổi vé" 4 thành 3. Chép ASM-15, Q-41 từ P02R |
| UCR-03 | UC-004, UC-005, UC-006, UC-015 (Bảng 4b cột REQ); Mục 5 dòng REQ-17 | UC-004 thêm REQ-07, REQ-09, REQ-19; UC-005 thêm REQ-07, REQ-09; UC-006 thêm REQ-26; UC-015 thêm REQ-26. Mục 5 dòng REQ-17 thêm UC-010 (giữ REQ-17 ở cột REQ của UC-010). Đã đối chiếu: tập REQ của mỗi UC ở Bảng 4b khớp Mục 5 |
| UCR-04 | UC-014 (Bảng 4a, 4b); EV-08; Mục 1 dòng ACT-01 đổi vé; CAND-07, CAND-43, CAND-44; Mục 5 dòng REQ-20, REQ-21; Mục 6 dòng ACT-07; ASM-16; Q-42 | Tác nhân phụ của UC-014 thành ACT-07 Cổng SMS; UC-014 thêm REQ-20, REQ-21; Mô tả ngắn nêu mã vé mới gửi qua SMS (ASM-16). Hệ quả: EV-08 thêm phản hồi gửi mã vé mới và REQ-20, REQ-21; Mục 1 thêm REQ-20, REQ-21; lý do CAND-07, CAND-43, CAND-44 nêu UC-014; Mục 5 thêm UC-014 vào REQ-20, REQ-21; Cổng SMS có 4 UC phụ. Chép ASM-16, Q-42 từ P02R |
| Hệ quả của UCR-02 và UCR-04 | Đầu vào đã dùng, phiên bản, Mã Q, ASM cuối | Phiên bản 1.0 thành 1.1; thêm P02-usecases.md phiên bản 1.0 và P02R-review.md vào đầu vào; mã Q, ASM cuối thành Q-42, ASM-16 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-40 | Khi nhân viên bán vé thu tiền vé đặt qua điện thoại tại quầy hoặc đổi vé tại quầy, hệ thống có in vé giấy có mã vạch cho khách không? (Có, in như khi bán vé tại quầy / Không in, khách chỉ nhận mã vé) | UC-006, UC-015; tác nhân phụ ACT-08 | Mục 4, câu 1 nêu in vé giấy cho bán tại quầy; Mục 4 câu 2 và Mục 5 câu 4 không nêu |
| Q-41 | Khi nhân viên bán vé trả vé tại quầy cho vé mua tại quầy, luồng có đoạn tương tác riêng từ 2 bước trở lên mà luồng hành khách tự trả vé trực tuyến không có không? (Không có, chỉ khác kênh hoàn tiền / Có, ghi rõ đoạn đó) | UC-012, UC-013; UCR-02 | P02R: Mục 5, câu 1 và câu 3; ASM-04 |
| Q-42 | Khi đổi vé trực tuyến, hệ thống có phát hành vé mới với mã vé mới và gửi mã vé mới qua SMS cho người đi không? (Có, gửi SMS như khi đặt vé / Không, giữ mã vé cũ) | UC-014, tác nhân phụ ACT-07; UCR-04 | P02R: Mục 5, câu 4 ("vé mới"); Mục 3, câu 3 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-12 | Khi thanh toán không thành công trong thời gian giữ chỗ, hành khách được thanh toán lại với các chỗ đang giữ đến hết thời gian giữ chỗ. | Chờ Q-17. Nguồn nêu chỗ chỉ được trả lại khi "Hết 10 phút chưa thanh toán thành công" (Mục 3, câu 2); giả định này làm thanh toán có thể thực hiện lại độc lập, thoả Q4 d để giữ UC-010 | UC-010, UC-009; CAND-39 |
| ASM-13 | Phần chênh lệch khi đổi sang vé đắt hơn được thanh toán cùng kênh mua vé cũ: vé mua trực tuyến thanh toán qua cổng thanh toán, vé mua tại quầy thanh toán tiền mặt tại quầy. | Chờ Q-22. Nguồn nêu "trả thêm phần chênh lệch" (Mục 5, câu 4) nhưng không nêu kênh; chọn cùng kênh mua vé cũ, nhất quán với ASM-08 | UC-014, UC-015, UC-010; REQ-44 |
| ASM-14 | Khi thu tiền vé đặt qua điện thoại tại quầy và khi đổi vé tại quầy, nhân viên bán vé in vé giấy có mã vạch qua máy in vé như khi bán vé tại quầy. | Chờ Q-40. Nguồn chỉ nêu in vé giấy cho bán tại quầy (Mục 4, câu 1); vé mua tại quầy dùng vé giấy để soát | UC-006, UC-015; ACT-08; REQ-26, REQ-27 |
| ASM-15 | Luồng trả vé tại quầy chỉ khác luồng trả vé trực tuyến ở người thao tác và kênh hoàn tiền, không có đoạn tương tác riêng từ 2 bước trở lên; trả vé là một use case có hai tác nhân chính. | Chờ Q-41. Nguồn không mô tả luồng trả vé tại quầy ngoài việc hoàn tiền mặt tại quầy (Mục 5, câu 3); chọn phương án gộp theo U-R10 nhánh b | UC-012, UC-013; UCR-02 |
| ASM-16 | Đổi vé trực tuyến thành công phát hành vé mới có mã vé riêng, mã vé mới được gửi qua SMS tới số điện thoại người đi; Cổng SMS là tác nhân phụ của UC-014. | Chờ Q-42. Nguồn nêu "vé mới" khi đổi và việc gửi mã vé qua SMS khi phát hành vé trực tuyến nhưng không nói rõ cho trường hợp đổi vé | UC-014; ACT-07; REQ-19, REQ-20; UCR-04 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Không có mục Target nào ở trạng thái Không đạt.
- Lựa chọn khi hai quy tắc xung đột (Conventions C9): quy trình nghiệp vụ chính ở Bước 9.1 hoà ba tác nhân người (ACT-01, ACT-02, ACT-03 đều có 6 UC User-goal). Chọn ACT-02 theo mục tiêu nghiệp vụ đầu tiên ở P00 mục 1 ("thay cho cách bán qua điện thoại và quầy"), nên nhóm Bán vé tại quầy được đánh số ngay sau nhóm Tài khoản (điều kiện tiên quyết là Đăng nhập của chính ACT-02).
- Lựa chọn khi hai quy tắc xung đột: U-R10 b chỉ cho một UC khi không thoả U-R10 a, nhưng U-R12 cho tách khi tác nhân phụ khác nhau. Trả vé gộp thành một UC (UC-012) theo U-R10 b, U-R12 và U-AP15 vì tác nhân phụ khác nhau không phải điều kiện của U-R10 a và đoạn xác thực Q-37 thuộc luồng hành khách (UCR-02, ASM-15). Đổi vé giữ tách UC-014 và UC-015 theo U-R10 a vì UC-015 có đoạn riêng thu chênh lệch tiền mặt và in vé giấy mới qua máy in (ASM-13, ASM-14); kết luận này phụ thuộc Q-40, nếu Q-40 trả lời "Không in" thì đoạn riêng chỉ còn một bước và phải xét gộp như UC-012.
- Lựa chọn khi hai quy tắc xung đột: đoạn chọn chuyến và chỗ dùng chung ở năm UC thoả Q4 a về hình thức, nhưng phần tìm chuyến và xem sơ đồ đã là UC User-goal UC-008 (U-T11 cấm trùng), phần còn lại dưới 3 bước. Không tạo Subfunction riêng; UC-008 là đoạn dùng chung (ứng viên include ở P03).
- Ứng viên mà bước thuộc nhiều UC (CAND-35, 36, 44, 46, 48, 51, 52, 62) ghi một UC chính ở cột Kết luận và các UC còn lại ở cột Lý do, vì định dạng kết luận chỉ cho một mã UC.
- UC-025 có tên 7 từ, dài hơn khoảng 2-6 từ của U-N7; giữ vì tên ngắn hơn ("Cấp danh sách soát vé") mất kết quả nghiệp vụ.
- EV-29 xếp Loại Thiết bị với Nguồn phát "-" vì máy soát vé không là tác nhân (P01, ASM-10); không có loại sự kiện nào khớp đúng.
