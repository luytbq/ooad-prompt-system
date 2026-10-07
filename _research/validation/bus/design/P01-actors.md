# P01 - Danh sách tác nhân - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P01 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); P00-problem-brief.md 1.0; yeu-cau-xe-khach.md (bản hiện có) |
| Phạm vi | Toàn hệ thống |

Quy ước trích nguồn theo P00: "Đoạn mở đầu", "Mục n", "câu k" chỉ vị trí trong yeu-cau-xe-khach.md.

## 1. Ranh giới hệ thống

Hệ thống cần xây dựng là Hệ thống bán vé xe khách SaoViet Bus: phần mềm bán vé và quản lý chuyến của nhà xe SaoViet, gồm website đặt vé cho hành khách, phần dành cho nhân viên nhà xe (bán vé, điều hành, quản lý) và ứng dụng soát vé chạy trên máy soát vé cầm tay (ASM-01).

| Thành phần | Trong / Ngoài / Chờ Q-nn | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
|---|---|---|---|
| Website đặt vé cho hành khách | Trong | REQ-03, REQ-04 ("Hành khách đặt vé qua website.", Mục 1, câu 1) | Là thành phần nội bộ, không phải tác nhân |
| Ứng dụng soát vé chạy trên máy soát vé cầm tay (phần "Máy báo hợp lệ hay không hợp lệ", "gửi lại kết quả khi có sóng") | Trong | ASM-01; REQ-57, REQ-59, REQ-60 | Là thành phần nội bộ, không phải tác nhân |
| Dữ liệu lưu trên máy soát vé (danh sách hành khách của chuyến, kết quả soát khi mất sóng) | Trong | Bộ nhớ thiết bị của ứng dụng thuộc hệ thống (ASM-01); REQ-59, REQ-60, REQ-61 | Là thành phần nội bộ, không phải tác nhân |
| Đầu quét mã vạch của máy soát vé cầm tay Android | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI ("Máy soát vé cầm tay Android có đầu quét mã vạch, do nhà xe tự trang bị"); ASM-01; ASM-06; REQ-55, REQ-56 | Là tác nhân ACT-09 |
| Phần cứng còn lại của máy soát vé cầm tay Android (hệ điều hành, màn hình, kết nối mạng) | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; ASM-06; REQ-56 | Là nền tảng chạy ứng dụng soát vé, không phải tác nhân (xem Mục 4) |
| Cổng thanh toán trực tuyến của đối tác | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-14, REQ-15, REQ-34, REQ-35 | Là tác nhân ACT-06 |
| Cổng SMS của nhà mạng | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-19, REQ-20, REQ-48 | Là tác nhân ACT-07 |
| Máy in vé nhiệt tại quầy | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-23, REQ-24 | Là tác nhân ACT-08 |
| Mạng di động ("vùng mất sóng", "khi có sóng", Mục 8, câu 3) | Ngoài | REQ-59, REQ-60 | Là đường truyền, không phải tác nhân (xem Mục 4) |
| Điện thoại (khách gọi tới nhân viên bán vé để đặt chỗ; điện thoại của người đi nhận SMS) | Ngoài | "nhận đặt chỗ qua điện thoại" (Mục 4, câu 2); "gửi qua SMS tới số điện thoại người đi" (Mục 3, câu 3); REQ-19, REQ-25 | Không tương tác trực tiếp với hệ thống, không phải tác nhân (xem Mục 4) |
| Sổ tay ghi vé (cách làm hiện tại) | Ngoài | "Hiện vé được bán qua điện thoại và quầy tại bến, ghi sổ tay" (Đoạn mở đầu, câu 3) | Bị hệ thống thay thế, không trao đổi dữ liệu với hệ thống, không phải tác nhân |

## 2. Bảng tác nhân

| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |
|---|---|---|---|---|---|---|---|---|
| ACT-01 | Hành khách | Passenger | Người | Chính | Người đặt vé xe khách liên tỉnh qua website của nhà xe, có hoặc không có tài khoản. Gộp các cách gọi "người khác" (Mục 3, câu 2) và "người truy cập" (Mục 10, câu 1). Có thể khác với người đi ghi trên vé (Mục 3). | Tìm chuyến và xem chỗ trống<br>Đặt và thanh toán vé trực tuyến<br>Đăng ký tài khoản và xem lại lịch sử vé<br>Đổi vé mua trực tuyến (ASM-02)<br>Trả vé mua trực tuyến (ASM-02) | - | REQ-03, REQ-05, REQ-06, REQ-07, REQ-08, REQ-09, REQ-10, REQ-11, REQ-12, REQ-13, REQ-14, REQ-16, REQ-17, REQ-19, REQ-29, REQ-30, REQ-34, REQ-40, REQ-66 |
| ACT-02 | Nhân viên bán vé | Ticket Clerk | Người | Chính | Nhân viên nhà xe làm việc tại quầy bán vé ở bến, phục vụ khách mua trực tiếp và khách gọi điện đặt chỗ. | Bán vé tại quầy và in vé giấy<br>Nhận đặt chỗ qua điện thoại<br>Thu tiền tại quầy cho vé đặt qua điện thoại<br>Đổi, trả vé mua tại quầy cho khách (ASM-02) | - | REQ-21, REQ-22, REQ-23, REQ-25, REQ-26, REQ-27, REQ-29, REQ-30, REQ-36, REQ-40 |
| ACT-03 | Nhân viên điều hành | Dispatcher | Người | Chính | Nhân viên nhà xe lập lịch chạy và xử lý khi phải huỷ chuyến (xe hỏng, thời tiết). | Lập lịch chạy theo tuần<br>Huỷ chuyến | - | REQ-41, REQ-42, REQ-43, REQ-44, REQ-45, REQ-46, REQ-47, REQ-48, REQ-49, REQ-50 |
| ACT-04 | Quản lý nhà xe | Manager | Người | Chính | Người quản lý của nhà xe SaoViet, quyết định giá vé và theo dõi kết quả kinh doanh. Nguồn gọi tắt là "quản lý" ở Mục 7 câu 2 và Mục 9 (ASM-04). | Đặt giá vé theo tuyến và loại xe<br>Đặt mức tăng giá ngày lễ, Tết<br>Xem báo cáo doanh thu<br>Xem tỉ lệ lấp đầy chỗ của chuyến | - | REQ-51, REQ-52, REQ-53, REQ-54, REQ-63, REQ-64, REQ-65 |
| ACT-05 | Phụ xe | Bus Attendant | Người | Chính | Nhân viên đi theo mỗi chuyến, soát vé khi hành khách lên xe bằng ứng dụng soát vé trên máy soát vé cầm tay. | Soát vé khi hành khách lên xe | - | REQ-55, REQ-57, REQ-58, REQ-59, REQ-60 |
| ACT-06 | Cổng thanh toán | Payment Gateway | Hệ thống ngoài | Phụ (ASM-07) | Cổng thanh toán trực tuyến của đối tác, trao đổi với hệ thống qua API thanh toán và hoàn tiền, chưa có tài liệu API (Q-24). Hệ thống không lưu thông tin thẻ, việc xử lý thẻ do cổng đảm nhận. | Cung cấp: thu tiền vé mua trực tuyến<br>Cung cấp: hoàn tiền vé mua trực tuyến | - | REQ-14, REQ-15, REQ-17, REQ-34, REQ-35, REQ-49, REQ-68 |
| ACT-07 | Cổng SMS | SMS Gateway | Hệ thống ngoài | Phụ | Cổng SMS của nhà mạng, nhận nội dung tin nhắn qua API REST và chuyển tới thuê bao. | Cung cấp: gửi tin nhắn SMS tới số điện thoại người đi (vé, thông báo huỷ chuyến) | - | REQ-19, REQ-20, REQ-48 |
| ACT-08 | Máy in vé | Ticket Printer | Thiết bị | Phụ | Máy in vé nhiệt đặt tại quầy, nhận dữ liệu vé từ hệ thống để in. | Cung cấp: in vé giấy có mã vạch | - | REQ-23, REQ-24 |
| ACT-09 | Đầu quét mã vạch | Barcode Scanner | Thiết bị | Phụ | Đầu quét gắn trên máy soát vé cầm tay Android do nhà xe tự trang bị. Đọc mã trên vé và chuyển mã cho ứng dụng soát vé của hệ thống (ASM-01, ASM-06). | Cung cấp: đọc mã vạch trên vé và chuyển mã vé cho ứng dụng soát vé | - | REQ-55, REQ-56 |
| ACT-10 | Bộ định thời | Timer | Thời gian | Chính | Sự kiện theo giờ xuất bến của từng chuyến, khởi xướng các xử lý tự động mà nguồn nêu. | Kích hoạt: 60 phút trước giờ xuất bến của mỗi chuyến (huỷ vé đặt qua điện thoại chưa thanh toán)<br>Kích hoạt: 15 phút trước giờ xuất bến của mỗi chuyến (gửi danh sách hành khách của chuyến về máy soát vé) | - | REQ-27, REQ-28, REQ-61, REQ-62 |

## 3. Bên liên quan không phải tác nhân

| SH | Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
|---|---|---|---|---|
| SH-01 | Nhà xe SaoViet | Bán vé và quản lý chuyến bằng phần mềm, chấm dứt trùng chỗ | Báo cáo do ACT-04 Quản lý nhà xe xem; vận hành qua ACT-02, ACT-03, ACT-05 | REQ-01, REQ-02, REQ-67 |
| SH-03 | Người đi | Nhận vé qua SMS, được soát vé khi lên xe, nhận SMS khi chuyến bị huỷ | ACT-07 Cổng SMS (nhận tin nhắn); ACT-05 Phụ xe (soát vé) | REQ-09, REQ-19, REQ-48, REQ-55 |
| SH-07 | Khách mua vé trực tiếp tại quầy | Mua vé bằng tiền mặt, nhận vé giấy có mã vạch, đổi, trả vé tại quầy | ACT-02 Nhân viên bán vé | REQ-21, REQ-22, REQ-23, REQ-36 |
| SH-09 | Khách đặt chỗ qua điện thoại | Được giữ chỗ qua điện thoại và thanh toán tại quầy trước hạn | ACT-02 Nhân viên bán vé | REQ-25, REQ-26, REQ-27, REQ-28 |
| SH-11 | Tài xế | Được xếp lịch không chồng chuyến, không lái quá 10 giờ một ngày | Lịch chạy do ACT-03 Nhân viên điều hành lập | REQ-42, REQ-44, REQ-45 |

## 4. Ứng viên tác nhân bị loại

| Ứng viên | Lý do loại | REQ |
|---|---|---|
| Hệ thống ("hệ thống phát hành vé", "hệ thống gửi SMS") | A-T1: chính hệ thống cần xây dựng | REQ-17, REQ-48, REQ-61 |
| Website | A-T1: kênh giao diện của chính hệ thống | REQ-03, REQ-04 |
| Máy soát vé cầm tay ở vai trò chủ thể ("Máy báo hợp lệ", "Máy ... gửi lại kết quả") | A-T1: phần mềm thực hiện các hành vi này là ứng dụng soát vé thuộc hệ thống (ASM-01) | REQ-57, REQ-59, REQ-60 |
| Phần cứng máy soát vé cầm tay ngoài đầu quét (hệ điều hành, màn hình, kết nối mạng) | A-T2: là nền tảng chạy ứng dụng soát vé, không tự trao đổi thông tin nghiệp vụ với hệ thống; phần có giao tiếp riêng là đầu quét, đã thành ACT-09 (ASM-06) | REQ-56 |
| Hành khách có tài khoản | Gộp vào ACT-01 Hành khách: cùng vai trò, tài khoản chỉ là điều kiện để xem lịch sử vé; không đủ hai tác nhân con để lập tổng quát hoá | REQ-10, REQ-11 |
| Người khác (được trả lại chỗ, Mục 3, câu 2) | Gộp vào ACT-01 Hành khách: chỉ các hành khách khác đặt vé trên website | REQ-16 |
| Người truy cập ("2.000 người truy cập cùng lúc", Mục 10, câu 1) | Gộp vào ACT-01 Hành khách: người dùng website trong câu yêu cầu tải | REQ-66 |
| Quản lý (Mục 7, câu 2; Mục 9, câu 1) | Gộp vào ACT-04 Quản lý nhà xe: cách gọi tắt của cùng vai trò (ASM-04) | REQ-53, REQ-63, REQ-64, REQ-65 |
| Đối tác (chủ sở hữu cổng thanh toán) | A-T2: tổ chức không tự thao tác với hệ thống; hệ thống của đối tác là ACT-06 Cổng thanh toán | REQ-14, REQ-15 |
| Nhà mạng | A-T2: tổ chức không tự thao tác với hệ thống; hệ thống của nhà mạng là ACT-07 Cổng SMS | REQ-20 |
| Xe | A-T2: phương tiện là đối tượng được xếp vào chuyến, không trao đổi thông tin với hệ thống | REQ-42, REQ-43 |
| Xe hỏng, thời tiết (lý do huỷ chuyến) | A-T2: sự kiện bên ngoài do ACT-03 Nhân viên điều hành nhận biết rồi ra lệnh huỷ chuyến, không tự báo cho hệ thống | REQ-47 |
| Mạng di động ("sóng") | A-T2: chỉ là đường truyền, không tự trao đổi thông tin nghiệp vụ với hệ thống | REQ-59, REQ-60 |
| Điện thoại | A-T2: khách gọi tới ACT-02 Nhân viên bán vé, không tới hệ thống; điện thoại của người đi nhận SMS từ ACT-07 Cổng SMS | REQ-19, REQ-25 |
| Bộ định thời hết hạn giữ chỗ 10 phút | Không thành ứng viên theo Bước 2.3: hết giờ chờ thanh toán trong phiên đặt vé đang mở của ACT-01 Hành khách, là luồng thay thế của use case đặt vé | REQ-13, REQ-16 |
| Sự kiện có sóng trở lại (gửi lại kết quả soát vé) | A-T1: hành vi nội bộ của ứng dụng soát vé thuộc hệ thống (ASM-01), không phải mốc thời gian và không có tác nhân ngoài khởi xướng | REQ-60 |

## Câu hỏi mở

Không có

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-06 | Trên máy soát vé cầm tay, chỉ đầu quét mã vạch được xét là thiết bị ngoài có giao tiếp riêng với ứng dụng soát vé (tác nhân phụ). Phần còn lại của máy là nền tảng chạy ứng dụng soát vé, không phải tác nhân. | Hồ sơ dự án xếp máy soát vé vào HE_THONG_NGOAI, trong khi ASM-01 đưa phần mềm soát vé vào phạm vi; nguồn không nêu cách ứng dụng nhận mã từ đầu quét. Chờ Q-01, Q-04 | ACT-09; Mục 1 (hai dòng máy soát vé); REQ-55, REQ-56 |
| ASM-07 | Cổng thanh toán là tác nhân phụ: hệ thống gọi tới cổng để thu tiền và hoàn tiền, kết quả thanh toán trả về trong phiên đặt vé. Nếu tài liệu API cho thấy cổng tự gửi kết quả thanh toán vào thời điểm không xác định và việc đó khởi động một xử lý riêng, đổi Tính chất thành "Chính và phụ". | Nguồn chỉ nêu "thanh toán qua cổng thanh toán" và "hoàn qua cổng thanh toán"; chưa có tài liệu API. Chờ Q-24, Q-10 | ACT-06; REQ-14, REQ-15, REQ-17, REQ-35 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Chọn giữa hai quy tắc (C9): cột Hệ quả của Mục 1 chỉ cho ba giá trị ("Là tác nhân ACT-nn", "Là thành phần nội bộ, không phải tác nhân", "Chờ trả lời Q-nn"), nhưng Target 1 yêu cầu liệt kê mọi thành phần nguồn nhắc tới. Phần cứng máy soát vé ngoài đầu quét, mạng di động, điện thoại và sổ tay nằm ngoài ranh giới nhưng không phải tác nhân. Đã giữ các dòng này để thoả Target 1 và ghi Hệ quả mô tả riêng, trỏ sang Mục 4.
- Mục 4 yêu cầu lý do loại nêu phép thử A-T1 đến A-T6. Ứng viên "Bộ định thời hết hạn giữ chỗ 10 phút" bị loại theo quy tắc Bước 2.3 (không thành ứng viên), không ứng với phép thử nào; đã ghi lý do theo Bước 2.3.
- REQ-60 (gửi lại kết quả soát khi có sóng) và REQ-61 (gửi danh sách hành khách về máy soát vé) là trao đổi giữa hai phần nội bộ của hệ thống theo ASM-01. REQ-60 gắn với ACT-05 Phụ xe vì kết quả soát do phụ xe tạo ra; REQ-61 gắn với ACT-10 Bộ định thời. Nếu Q-01 được trả lời là máy soát vé có phần mềm sẵn, máy soát vé trở thành tác nhân thiết bị ngoài (Chính với REQ-60, Phụ với REQ-61) và cần chạy lại P01.
- Q-03 (ai cập nhật danh mục tuyến, xe, tài xế) chưa có trả lời: chưa thêm mục tiêu nào cho ACT-03 hoặc ACT-04 về danh mục này. Khi Q-03 được trả lời, bổ sung mục tiêu cho tác nhân tương ứng.
- Q-14 (kênh hoàn tiền khi huỷ chuyến): REQ-49 gắn với ACT-03 (khởi xướng huỷ chuyến) và ACT-06 (hoàn tiền vé trực tuyến). Nếu vé mua tại quầy được hoàn tiền mặt tại quầy, ACT-02 Nhân viên bán vé có thêm vai trò trong REQ-49.
- Mục tiêu đổi, trả vé của ACT-01 và ACT-02 dựa trên ASM-02 (chờ Q-02). Nếu mọi vé chỉ đổi, trả tại quầy, bỏ hai mục tiêu này khỏi ACT-01.
