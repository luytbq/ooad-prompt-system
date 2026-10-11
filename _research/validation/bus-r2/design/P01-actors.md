# P01 - Xác định tác nhân - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P01 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09); yeu-cau-xe-khach.md |
| Phạm vi | Toàn hệ thống |
| Mã Q, ASM cuối đã cấp | Q-39, ASM-11 |

## 1. Ranh giới hệ thống

Hệ thống cần xây dựng là Hệ thống bán vé xe khách SaoViet Bus: phần mềm bán vé và quản lý chuyến gồm website đặt vé, phần mềm cho nhân viên nhà xe và ứng dụng soát vé chạy trên máy soát vé cầm tay (ASM-10).

| Thành phần | Trong / Ngoài / Chờ Q-nn | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
|---|---|---|---|
| Website đặt vé cho hành khách | Trong | REQ-04; "Hành khách đặt vé qua website." (Mục 1, câu 1) | Là thành phần nội bộ, không phải tác nhân |
| Phần mềm cho nhân viên nhà xe (bán vé tại quầy, lập lịch chạy, đặt giá, xem báo cáo) | Trong | REQ-22, REQ-46, REQ-60, REQ-71; "Nhà xe cần phần mềm bán vé và quản lý chuyến." (Đoạn mở đầu, câu 4) | Là thành phần nội bộ, không phải tác nhân |
| Ứng dụng soát vé chạy trên máy soát vé cầm tay | Trong | REQ-63, REQ-65, REQ-67, REQ-68; nguồn giao cho máy hành vi nghiệp vụ: "Máy báo hợp lệ hay không hợp lệ", "Máy cần soát được cả khi xe ở vùng mất sóng" (Mục 8, câu 2 và câu 3); ASM-10 | Là thành phần nội bộ, không phải tác nhân |
| Bộ nhớ cục bộ của ứng dụng soát vé (lưu danh sách hành khách và kết quả soát khi mất sóng) | Trong | REQ-67, REQ-68, REQ-69; ASM-10 | Là thành phần nội bộ, không phải tác nhân |
| Kho dữ liệu của hệ thống (vé, chuyến, lịch chạy, danh mục, tài khoản) | Trong | REQ-11, REQ-47, REQ-48 | Là thành phần nội bộ, không phải tác nhân |
| Máy soát vé cầm tay Android có đầu quét mã vạch | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; "do nhà xe tự trang bị"; REQ-64, REQ-77; ASM-10 | Ngoài, không phải tác nhân (nền tảng chạy thành phần nội bộ); đầu quét tích hợp trên máy là kênh nhập, không ghi dòng riêng; người thao tác là ACT-05 |
| Cổng thanh toán trực tuyến của đối tác | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-15, REQ-16 | Là tác nhân ACT-06 |
| Cổng SMS của nhà mạng | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-20, REQ-21 | Là tác nhân ACT-07 |
| Máy in vé nhiệt tại quầy | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-26, REQ-27 | Là tác nhân ACT-08 |
| Điện thoại (đường dây đặt chỗ của nhà xe) | Ngoài | REQ-28; "Nhân viên bán vé cũng nhận đặt chỗ qua điện thoại" (Mục 4, câu 2) | Ngoài, không phải tác nhân (đường truyền giữa hành khách và Nhân viên bán vé) kèm dòng ở Mục 4 |
| Đường truyền dữ liệu giữa máy soát vé và hệ thống ("sóng") | Ngoài | REQ-67, REQ-68; "vùng mất sóng" (Mục 8, câu 3) | Ngoài, không phải tác nhân (đường truyền) kèm dòng ở Mục 4 |
| Sổ tay ghi vé tại quầy và qua điện thoại | Ngoài | "ghi sổ tay, thường xuyên bị trùng chỗ" (Đoạn mở đầu, câu 3) | Ngoài, không phải tác nhân (cách làm cũ được thay thế) kèm dòng ở Mục 4 |

## 2. Bảng tác nhân

| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |
|---|---|---|---|---|---|---|---|---|
| ACT-01 | Hành khách | Passenger | Người | Chính | Người mua vé xe khách qua website, có hoặc không có tài khoản. Gộp "người truy cập" (Mục 10) và hành khách đã đăng ký tài khoản. Hành khách mua trực tiếp tại quầy hoặc đặt qua điện thoại không phải tác nhân của các luồng đó (xem Mục 3). | Tìm chuyến và xem chỗ trống<br>Đặt vé và thanh toán trực tuyến<br>Đăng ký tài khoản và xem lại lịch sử vé (ASM-01: đăng nhập bằng mã xác thực qua SMS)<br>Trả vé mua trực tuyến và nhận hoàn tiền (ASM-04)<br>Đổi vé mua trực tuyến sang chuyến khác cùng tuyến (ASM-04, ASM-05) | - | REQ-04, REQ-05, REQ-06, REQ-07, REQ-08, REQ-09, REQ-10, REQ-11, REQ-12, REQ-13, REQ-14, REQ-15, REQ-17, REQ-18, REQ-33, REQ-34, REQ-37, REQ-38, REQ-39, REQ-40, REQ-42, REQ-43, REQ-44, REQ-45, REQ-74 |
| ACT-02 | Nhân viên bán vé | Ticket Seller | Người | Chính | Nhân viên nhà xe làm việc tại quầy bán vé, dùng phần mềm nhà xe. Phục vụ khách mua trực tiếp và khách gọi điện đặt chỗ. | Bán vé tại quầy, thu tiền mặt và in vé giấy (ASM-03: chọn chuyến và chỗ cho khách)<br>Nhận đặt chỗ qua điện thoại (ASM-03)<br>Thu tiền vé đặt qua điện thoại tại quầy<br>Trả vé và đổi vé tại quầy cho vé mua tại quầy (ASM-04, ASM-05)<br>Hoàn tiền mặt tại quầy cho vé mua tại quầy (trả vé; chuyến bị huỷ theo ASM-08) | - | REQ-22, REQ-23, REQ-25, REQ-26, REQ-28, REQ-29, REQ-30, REQ-31, REQ-35, REQ-36, REQ-41, REQ-59 |
| ACT-03 | Nhân viên điều hành | Dispatcher | Người | Chính | Nhân viên nhà xe lập lịch chạy, huỷ chuyến và duy trì danh mục tuyến, bến, xe, tài xế (ASM-06). | Lập lịch chạy theo tuần: chọn tuyến, giờ xuất bến, xe, tài xế (ASM-07: chọn cả phụ xe)<br>Huỷ chuyến khi xe hỏng, thời tiết<br>Quản lý danh mục tuyến xe và bến xe (ASM-06)<br>Quản lý danh mục xe, loại xe, số chỗ và sơ đồ chỗ (ASM-06)<br>Quản lý danh mục tài xế (ASM-06) | - | REQ-01, REQ-03, REQ-23, REQ-46, REQ-47, REQ-48, REQ-49, REQ-50, REQ-51, REQ-52, REQ-53, REQ-54, REQ-55, REQ-56, REQ-57, REQ-58, REQ-59 |
| ACT-04 | Quản lý nhà xe | Bus Company Manager | Người | Chính | Người quản lý nhà xe, đặt giá, xem báo cáo và quản lý tài khoản nhân viên. Nguồn gọi là "quản lý nhà xe", "quản lý" (Mục 7, Mục 9); các cách gọi này được hiểu là một vai trò theo ASM-09. | Đặt giá vé theo tuyến và loại xe<br>Đặt mức tăng giá theo phần trăm cho khoảng ngày lễ, Tết (tối đa 30%)<br>Xem báo cáo doanh thu theo ngày, theo tuyến (ASM-09)<br>Xem báo cáo tỉ lệ lấp đầy chỗ của từng chuyến (ASM-09)<br>Quản lý tài khoản nhân viên nhà xe (ASM-02) | - | REQ-23, REQ-24, REQ-60, REQ-61, REQ-62, REQ-71, REQ-72, REQ-73 |
| ACT-05 | Phụ xe | Bus Attendant | Người | Chính | Người đi cùng chuyến, quét mã vé khi hành khách lên xe bằng máy soát vé cầm tay (đầu quét tích hợp là kênh nhập). Do nhân viên điều hành chọn cho từng chuyến (ASM-07). | Soát vé hành khách lên xe<br>Soát vé khi xe ở vùng mất sóng và gửi lại kết quả khi có sóng | - | REQ-23, REQ-51, REQ-63, REQ-64, REQ-65, REQ-66, REQ-67, REQ-68, REQ-77 |
| ACT-06 | Cổng thanh toán | Payment Gateway | Hệ thống ngoài | Phụ | Cổng thanh toán trực tuyến của đối tác, giao tiếp qua API thanh toán và hoàn tiền (chưa có tài liệu API). Hệ thống gọi cổng; cổng không tự khởi xướng (ASM-11). | Cung cấp: thu tiền vé thanh toán trực tuyến<br>Cung cấp: hoàn tiền vé mua trực tuyến (trả vé; chuyến bị huỷ theo ASM-08) | - | REQ-15, REQ-16, REQ-40, REQ-57, REQ-59, REQ-76 |
| ACT-07 | Cổng SMS | SMS Gateway | Hệ thống ngoài | Phụ | Cổng SMS của nhà mạng, giao tiếp qua API REST. | Cung cấp: gửi SMS mã vé tới số điện thoại người đi<br>Cung cấp: gửi SMS thông báo huỷ chuyến cho hành khách đã có vé<br>Cung cấp: gửi mã xác thực đăng nhập tới số điện thoại đã đăng ký (ASM-01) | - | REQ-12, REQ-20, REQ-21, REQ-56 |
| ACT-08 | Máy in vé | Ticket Printer | Thiết bị | Phụ | Máy in vé nhiệt đặt tại quầy bán vé, nhận dữ liệu vé từ hệ thống để in vé giấy có mã vạch. | Cung cấp: in vé giấy có mã vạch | - | REQ-26, REQ-27 |
| ACT-09 | Bộ định thời | Timer | Thời gian | Chính | Tác nhân đại diện cho các mốc thời gian tính theo giờ xuất bến của từng chuyến, khi không còn phiên nào của tác nhân đang mở. | Kích hoạt: 60 phút trước giờ xuất bến, tự huỷ vé đặt qua điện thoại chưa thanh toán tại quầy<br>Kích hoạt: 15 phút trước giờ xuất bến, gửi danh sách hành khách của chuyến về máy soát vé | - | REQ-31, REQ-32, REQ-69, REQ-70 |

## 3. Bên liên quan không phải tác nhân

| SH | Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
|---|---|---|---|---|
| SH-01 | Nhà xe SaoViet (tổ chức khai thác tuyến, đặt hàng phần mềm) | Hết trùng chỗ, bán vé và quản lý chuyến bằng phần mềm | ACT-04 Quản lý nhà xe (đại diện nhà xe khi đặt giá, xem báo cáo) | REQ-01, REQ-02, REQ-03, REQ-75 |
| SH-02 | Hành khách khi mua trực tiếp tại quầy hoặc đặt chỗ qua điện thoại; người đi chỉ nhận SMS mã vé | Có vé đúng chỗ, đúng chuyến; nhận được mã vé | ACT-02 Nhân viên bán vé (quầy, điện thoại); ACT-07 Cổng SMS (nhận SMS) | REQ-09, REQ-20, REQ-22, REQ-28, REQ-30, REQ-56 |
| SH-08 | Tài xế | Lịch lái không chồng nhau, không quá 10 giờ một ngày | ACT-03 Nhân viên điều hành (lập lịch chạy) | REQ-47, REQ-50, REQ-53, REQ-54 |

## 4. Ứng viên tác nhân bị loại

| Ứng viên | Lý do loại | REQ |
|---|---|---|
| Khách mua trực tiếp tại quầy | A-T2: chỉ tương tác qua Nhân viên bán vé, không thao tác trên hệ thống (xếp vào Mục 3, SH-02) | REQ-22 |
| Hành khách gọi điện đặt chỗ, thanh toán vé đặt qua điện thoại tại quầy | A-T2: tương tác qua điện thoại và quầy với Nhân viên bán vé, không thao tác trên hệ thống (xếp vào Mục 3, SH-02) | REQ-28, REQ-30 |
| Người đi (người nhận SMS mã vé) | A-T2: nhận kết quả thụ động qua kênh SMS; kênh gửi là ACT-07 (xếp vào Mục 3, SH-02) | REQ-09, REQ-20 |
| Hành khách có tài khoản, hành khách không có tài khoản, người truy cập | Gộp vào ACT-01 Hành khách: cùng một vai trò, tài khoản chỉ là điều kiện tuỳ chọn | REQ-04, REQ-10, REQ-74 |
| Quản lý (cách gọi ở Mục 7 câu 2 và Mục 9) | Gộp vào ACT-04 Quản lý nhà xe theo ASM-09 | REQ-61, REQ-71, REQ-72, REQ-73 |
| Nhà mạng, đối tác thanh toán | Gộp vào ACT-07 Cổng SMS, ACT-06 Cổng thanh toán: tổ chức sở hữu cổng, hệ thống giao tiếp qua cổng | REQ-16, REQ-21 |
| Nhân viên nhà xe (cách gọi chung ở REQ-23, REQ-24) | A-T3: nhóm gồm bốn vai trò có mục tiêu khác nhau; không tạo tác nhân cha vì chỉ chung một mục tiêu đăng nhập (Bước 5a) | REQ-23, REQ-24 |
| Người quản trị hệ thống (phương án của Q-01) | A-T6: nguồn không nhắc; ASM-02 giao quản lý tài khoản cho ACT-04 | REQ-24 |
| Tài xế | A-T2: chỉ được xếp lịch, không tương tác với hệ thống; A-T4: không có mục tiêu với hệ thống (xếp vào Mục 3, SH-08) | REQ-47, REQ-50, REQ-53, REQ-54 |
| Nhà xe SaoViet (tổ chức) | A-T3: tổ chức, không phải vai trò thao tác; đại diện bằng ACT-04 (xếp vào Mục 3, SH-01) | REQ-01, REQ-75 |
| Hệ thống (chủ thể của "hệ thống gửi", "hệ thống phát hành", "hệ thống hoàn tiền") | A-T1: chính hệ thống cần xây dựng | REQ-18, REQ-20, REQ-56, REQ-69 |
| Website đặt vé | A-T1: giao diện của chính hệ thống | REQ-04 |
| Ứng dụng soát vé và máy soát vé cầm tay | A-T1: ứng dụng là thành phần nội bộ, máy là nền tảng chạy ứng dụng (ASM-10) | REQ-64, REQ-77 |
| Đầu quét mã vạch tích hợp trên máy soát vé | A-T1: bộ phận nhập liệu gắn liền thiết bị chạy phần mềm của hệ thống, là kênh nhập của ACT-05 | REQ-63 |
| Điện thoại | A-T2: đường truyền giữa hành khách và Nhân viên bán vé, không trao đổi thông tin với hệ thống | REQ-28 |
| Đường truyền dữ liệu giữa máy soát vé và hệ thống ("sóng") | A-T2: đường truyền, không phải bên trao đổi thông tin | REQ-67, REQ-68 |
| Sổ tay ghi vé | A-T2: cách làm cũ được thay thế bởi hệ thống, không tương tác với hệ thống | - |
| Xe khách (xe giường nằm, xe ghế ngồi) | A-T2: đối tượng dữ liệu của danh mục xe, không trao đổi thông tin với hệ thống | REQ-03, REQ-49 |
| Bộ định thời hết thời gian giữ chỗ 10 phút | Bước 2.3: hết giờ chờ trong phiên, là luồng thay thế của use case | REQ-14, REQ-17 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-38 | Ứng dụng soát vé chạy trên máy soát vé cầm tay do dự án này xây dựng, hay máy đã có phần mềm riêng và hệ thống chỉ trao đổi dữ liệu với máy qua giao diện? (Dự án xây dựng ứng dụng / Máy có phần mềm riêng, hệ thống giao tiếp qua giao diện) | Ranh giới ở Mục 1; có thể thêm tác nhân Thiết bị Máy soát vé; ACT-05 và các UC soát vé ở P02 | Mục 8, câu 1 đến câu 4; project-profile.md, HE_THONG_NGOAI: "do nhà xe tự trang bị"; REQ-64 |
| Q-39 | Cổng thanh toán có tự gửi thông báo kết quả thanh toán về hệ thống vào thời điểm không xác định (khởi động một xử lý riêng), hay chỉ trả kết quả cho lời gọi của hệ thống? (Tự gửi thông báo / Chỉ trả kết quả cho lời gọi) | Tính chất của ACT-06 (Phụ hay Chính và phụ); sự kiện kích hoạt ở P02 | Mục 3, câu 2 và câu 3; project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API"; liên quan Q-19 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-10 | Ứng dụng soát vé chạy trên máy soát vé cầm tay do dự án xây dựng; ứng dụng là thành phần Trong, máy là nền tảng Ngoài, người thao tác là Phụ xe. | Chờ Q-38. Nguồn giao cho máy hành vi nghiệp vụ (báo hợp lệ, soát khi mất sóng, gửi lại kết quả) nhưng không nói ai xây dựng phần mềm trên máy | Mục 1; ACT-05; REQ-63, REQ-64, REQ-65, REQ-67, REQ-68, REQ-77 |
| ASM-11 | Cổng thanh toán chỉ là tác nhân Phụ: hệ thống gọi cổng và nhận kết quả như phản hồi của lời gọi; cổng không tự gửi thông báo khởi động xử lý riêng. | Chờ Q-39. Nguồn không nêu cơ chế báo kết quả của cổng; chọn phương án không tạo thêm sự kiện từ hệ thống ngoài mà nguồn không nêu | ACT-06; REQ-15, REQ-16 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Không có mục Target nào ở trạng thái Không đạt.
- Lựa chọn khi hai quy tắc xung đột (Conventions C9): ACT-09 gộp hai mốc 60 phút và 15 phút trước giờ xuất bến thành một Bộ định thời có hai dòng Kích hoạt, vì cùng neo vào giờ xuất bến của chuyến; quy tắc đặt tên cho phép tách thành hai tác nhân khi nhịp độc lập nhưng Bước 4.1 ưu tiên gộp vai trò. P02 quyết định tách thành hai sự kiện EV.
- Lựa chọn khi hai quy tắc xung đột: "Hành khách có tài khoản" không tách khỏi ACT-01 dù có thêm mục tiêu xem lịch sử vé (A-T5), vì Bước 5 đòi từ hai tác nhân con và nguồn mô tả tài khoản là tuỳ chọn của cùng một vai trò.
- Không tạo tác nhân cha "Nhân viên nhà xe": ACT-02, ACT-03, ACT-04, ACT-05 chỉ chung mục tiêu đăng nhập (REQ-23), không đạt Bước 5a (thường từ hai mục tiêu chung trở lên). Đăng nhập được xét riêng ở P02.
- REQ-17 (trả chỗ khi hết 10 phút) gắn với ACT-01 và không tạo tác nhân thời gian: hết giờ chờ thanh toán thuộc phiên của Hành khách theo Bước 2.3.
- REQ-64 và REQ-77 (loại Giao tiếp ngoài, Ràng buộc) gắn với ACT-05 thay vì một tác nhân Thiết bị, vì máy soát vé là nền tảng chạy ứng dụng nội bộ (ASM-10, chờ Q-38).
- REQ-02 (số liệu quy mô) và REQ-19 (mỗi chỗ một mã vé) là Dữ liệu hoặc Quy tắc nghiệp vụ đi kèm REQ chức năng; không cần tác nhân riêng. REQ-74, REQ-75, REQ-76 là phi chức năng, quy tắc, ràng buộc: chỉ REQ-74 và REQ-76 được gắn vào ACT-01 và ACT-06.
