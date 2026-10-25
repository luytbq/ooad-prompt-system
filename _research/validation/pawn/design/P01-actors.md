# P01 - Xác định tác nhân - Hệ thống quản lý chuỗi cầm đồ Phúc An

| Thuộc tính | Giá trị |
|---|---|
| Bước | P01 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (1.0); P00-problem-brief.md (1.0); yeu-cau-cam-do.md; bien-ban-hop-bo-sung.md |
| Phạm vi | Toàn hệ thống, trừ nghiệp vụ chốt ca và cảnh báo định mức tiền mặt trong két (Ngoài trọng tâm phân tích theo P00) |
| Mã Q, ASM cuối đã cấp | Q-36, ASM-11 |

## 1. Ranh giới hệ thống

Hệ thống cần xây dựng là Hệ thống quản lý chuỗi cầm đồ Phúc An, gồm phần mềm dùng tại quầy của 6 cửa hàng, ứng dụng di động cho khách, và kho dữ liệu của chính hệ thống.

| Thành phần | Trong / Ngoài / Chờ Q-nn | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
|---|---|---|---|
| Phần mềm quản lý hợp đồng, tài sản cầm cố và tiền mặt tại quầy | Trong | REQ-01; "Phúc An cần phần mềm quản lý hợp đồng cầm đồ, tài sản cầm cố và tiền mặt tại quầy" (yeu-cau-cam-do.md, đoạn mở đầu) | Là thành phần nội bộ, không phải tác nhân |
| Ứng dụng di động của Phúc An cho khách | Trong | REQ-42, REQ-75 đến REQ-80; QUYET_DINH_RANH_GIOI: "Ứng dụng di động cho khách: Trong" | Là thành phần nội bộ, không phải tác nhân. Khách là tác nhân ACT-01 |
| Điện thoại của khách (nền tảng chạy ứng dụng di động) | Ngoài | REQ-75; thiết bị của khách, hệ thống chỉ cài ứng dụng lên | Ngoài, không phải tác nhân (nền tảng chạy thành phần nội bộ) |
| Cơ sở dữ liệu hợp đồng, hồ sơ khách, ảnh tài sản, nhật ký thay đổi hợp đồng | Trong | REQ-07, REQ-08, REQ-88, REQ-89, REQ-93 | Là thành phần nội bộ, không phải tác nhân |
| Bảng giá thị trường | Trong | REQ-14, REQ-15; dữ liệu của hệ thống do ACT-06 cập nhật | Là thành phần nội bộ, không phải tác nhân |
| Máy trạm tại quầy (nền tảng chạy phần mềm tại quầy) | Ngoài | Chỉ ngụ ý qua "tại quầy"; nguồn không nêu thiết bị cụ thể, chỉ kể thiết bị rời ở các dòng dưới | Ngoài, không phải tác nhân (nền tảng chạy thành phần nội bộ) |
| Đầu đọc căn cước gắn chip tại quầy | Ngoài | REQ-06; Hồ sơ dự án: HE_THONG_NGOAI (kết nối USB, bộ thư viện nhà sản xuất) | Là tác nhân ACT-14 |
| Máy quét mã vạch tại quầy | Ngoài | REQ-58; Hồ sơ dự án: HE_THONG_NGOAI | Là tác nhân ACT-15 |
| Máy in nhãn mã vạch tại quầy | Ngoài | REQ-105; Hồ sơ dự án: HE_THONG_NGOAI; QUYET_DINH_RANH_GIOI: "Máy in nhãn mã vạch: Ngoài"; ASM-03 | Là tác nhân ACT-16 |
| Máy in dùng để in hợp đồng và biên nhận chuộc đồ | Ngoài | REQ-33, REQ-61; nguồn chỉ nói "in hợp đồng", không liệt kê thiết bị in này trong HE_THONG_NGOAI; ASM-11, Chờ Q-36 | Ngoài, không phải tác nhân (đầu ra in qua chức năng in thông thường của máy trạm, không có giao tiếp riêng với hệ thống) |
| Cổng chi hộ của ngân hàng đối tác | Ngoài | REQ-32; Hồ sơ dự án: HE_THONG_NGOAI | Là tác nhân ACT-09 |
| Cổng thanh toán trực tuyến | Ngoài | REQ-43; Hồ sơ dự án: HE_THONG_NGOAI | Là tác nhân ACT-10 |
| Cổng SMS của nhà mạng | Ngoài | REQ-90; Hồ sơ dự án: HE_THONG_NGOAI | Là tác nhân ACT-11 |
| Dịch vụ thông báo đẩy của nền tảng di động | Ngoài | REQ-99; Hồ sơ dự án: HE_THONG_NGOAI | Là tác nhân ACT-12 |
| Hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an | Ngoài | REQ-24; Hồ sơ dự án: HE_THONG_NGOAI (chưa có tài liệu API, xem Q-21 của P00) | Là tác nhân ACT-13 |
| Bộ phận thanh lý của chuỗi (nơi bán tài sản ngoài phần mềm) | Ngoài | "Việc bán tài sản ở bộ phận thanh lý của chuỗi làm ngoài phần mềm" (bien-ban-hop-bo-sung.md, mục 5); REQ-72, REQ-102 | Ngoài, không phải tác nhân (không kết nối, dữ liệu do ACT-08 nhập tay) |
| Két của cửa hàng | Ngoài | REQ-38, REQ-57; vật chứa tài sản, không có giao tiếp với hệ thống (Q-23 của P00) | Ngoài, không phải tác nhân (không kết nối, việc cất và lấy tài sản do con người thực hiện) |
| Hợp đồng viết tay hai liên và bảng tính theo dõi hạn | Ngoài | "Hiện hợp đồng viết tay hai liên, hạn hợp đồng theo dõi bằng bảng tính" (yeu-cau-cam-do.md, đoạn mở đầu) | Ngoài, không phải tác nhân (cách làm cũ được thay thế) |
| Thẻ căn cước của khách | Ngoài | REQ-05, REQ-06 | Ngoài, không phải tác nhân (vật mang dữ liệu, đọc qua ACT-14) |

## 2. Bảng tác nhân

| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |
|---|---|---|---|---|---|---|---|---|
| ACT-01 | Khách | Customer | Người | Chính | Người cầm đồ, chủ hợp đồng cầm đồ, dùng ứng dụng di động của Phúc An sau khi đăng ký bằng số điện thoại đã khai trong hợp đồng. Nguồn gọi là "khách". Tại quầy khách giao dịch qua nhân viên nên ở đó không phải tác nhân (xem Mục 3). | Đăng ký ứng dụng di động bằng số điện thoại<br>Xem các hợp đồng đang có<br>Xem lịch sử đóng lãi<br>Xem số tiền phải trả nếu chuộc trong ngày<br>Đóng lãi gia hạn hợp đồng trực tuyến | - | REQ-42, REQ-75, REQ-77, REQ-78, REQ-79, REQ-80 |
| ACT-02 | Nhân viên giao dịch | Transaction Clerk | Người | Chính | Nhân viên tại quầy tiếp khách, đọc thẻ căn cước, lập và in hợp đồng, in nhãn mã vạch, làm thủ tục lấy tài sản khi chuộc. Ở cửa hàng nhỏ cùng một người có thể kiêm Nhân viên định giá (REQ-96), nhưng là hai vai trò khác nhau. Nguồn cũng gọi "nhân viên tại quầy" khi tra cứu hợp đồng (ASM-09). | Tiếp nhận khách, lấy thông tin từ thẻ căn cước, tạo hoặc mở hồ sơ khách (ASM-06 chụp ảnh thẻ)<br>Lập, in hợp đồng cầm đồ (ASM-01)<br>In nhãn mã vạch cho tài sản cầm cố (ASM-03)<br>Làm thủ tục chuộc đồ: đọc thẻ người chuộc, quét mã vạch lấy tài sản, in biên nhận (ASM-04)<br>Tra cứu hợp đồng bằng mã vạch tại quầy (ASM-09) | - | REQ-05, REQ-07, REQ-08, REQ-33, REQ-34, REQ-35, REQ-37, REQ-55, REQ-57, REQ-61, REQ-92, REQ-94, REQ-96 |
| ACT-03 | Nhân viên định giá | Appraiser | Người | Chính | Nhân viên kiểm tra tài sản cầm cố và định giá. Nhận gợi ý giá tham khảo từ hệ thống với điện thoại và máy tính xách tay. Không được duyệt khoản vay của hợp đồng mình định giá (REQ-97). | Chụp ảnh tài sản cầm cố<br>Ghi đặc điểm tài sản, gồm số máy của xe máy (ASM-05)<br>Nhập giá định giá | - | REQ-10, REQ-11, REQ-13, REQ-14, REQ-23, REQ-96, REQ-97 |
| ACT-04 | Thủ quỹ | Cashier | Người | Chính | Nhân viên quản lý tiền mặt tại quầy: giải ngân, thu tiền lãi, thu tiền chuộc, ghi nhận trả tiền thừa. Việc nhập giao dịch đóng lãi tại quầy gán cho Thủ quỹ vì nguồn nêu "tại quầy (thủ quỹ thu tiền mặt)". Nghiệp vụ chốt ca và định mức két nằm Ngoài trọng tâm phân tích. | Giải ngân khoản vay bằng tiền mặt<br>Giải ngân khoản vay bằng chuyển khoản, nhập tài khoản ngân hàng của khách (ASM-02)<br>Thu tiền lãi gia hạn và tiền gốc trả bớt tại quầy<br>Thu tiền chuộc đồ<br>Ghi nhận trả lại tiền thừa cho khách (ASM-08) | - | REQ-29, REQ-30, REQ-31, REQ-39, REQ-41, REQ-45, REQ-56, REQ-74 |
| ACT-05 | Quản lý cửa hàng | Store Manager | Người | Chính | Người phụ trách một cửa hàng, duyệt khoản vay lớn và quyết định thanh lý. Nhận báo hợp đồng chờ thanh lý trên phần mềm (ASM-10). | Duyệt khoản vay từ 5 triệu đồng trở lên<br>Nhận báo hợp đồng chuyển sang chờ thanh lý (ASM-10)<br>Quyết định thanh lý: bán tại quầy hoặc chuyển về bộ phận thanh lý<br>Nhập số tiền bán được khi bán tài sản tại quầy (ASM-07) | - | REQ-19, REQ-20, REQ-68, REQ-69, REQ-70, REQ-71, REQ-72, REQ-97 |
| ACT-06 | Quản lý chuỗi | Chain Manager | Người | Chính | Người điều hành toàn chuỗi, đặt tham số tài chính và xem báo cáo toàn chuỗi. | Đặt lãi suất cho từng loại tài sản<br>Đặt tỉ lệ cho vay theo loại tài sản<br>Cập nhật bảng giá thị trường<br>Xem báo cáo dư nợ, tỉ lệ hợp đồng quá hạn, doanh thu lãi theo tháng | - | REQ-15, REQ-16, REQ-28, REQ-81, REQ-82, REQ-83, REQ-84 |
| ACT-07 | Kiểm toán viên nội bộ | Internal Auditor | Người | Chính | Người kiểm tra nội bộ, chỉ xem, không sửa dữ liệu. | Xem mọi hợp đồng<br>Xem nhật ký thao tác | - | REQ-85, REQ-86, REQ-87 |
| ACT-08 | Kế toán chuỗi | Chain Accountant | Người | Chính | Nhân viên kế toán của chuỗi, nhập vào phần mềm số tiền bán được của tài sản bán ở bộ phận thanh lý để phần mềm tính tiền thừa. | Nhập số tiền bán được của tài sản bán ở bộ phận thanh lý | - | REQ-102, REQ-103 |
| ACT-09 | Cổng chi hộ | Disbursement Gateway | Hệ thống ngoài | Phụ | Cổng chi hộ của ngân hàng đối tác (API REST), thực hiện lệnh chuyển khoản giải ngân vào tài khoản ngân hàng của khách. | Cung cấp: thực hiện lệnh chi chuyển khoản và trả kết quả chi | - | REQ-30, REQ-32 |
| ACT-10 | Cổng thanh toán trực tuyến | Online Payment Gateway | Hệ thống ngoài | Phụ | Dịch vụ thanh toán trực tuyến (API REST) xử lý khoản đóng lãi của khách trên ứng dụng di động. | Cung cấp: xử lý thanh toán đóng lãi và trả kết quả giao dịch | - | REQ-42, REQ-43, REQ-46 |
| ACT-11 | Cổng SMS | SMS Gateway | Hệ thống ngoài | Phụ | Cổng SMS của nhà mạng (API REST), gửi tin nhắn tới số điện thoại của khách. | Cung cấp: gửi tin nhắn và mã OTP tới số điện thoại của khách | - | REQ-62, REQ-63, REQ-77, REQ-90 |
| ACT-12 | Dịch vụ thông báo đẩy | Push Notification Service | Hệ thống ngoài | Phụ | Dịch vụ thông báo đẩy của nền tảng di động, chuyển tin nhắc tới ứng dụng di động của khách đã cài ứng dụng. | Cung cấp: gửi thông báo đẩy tới ứng dụng di động của khách | - | REQ-98, REQ-99 |
| ACT-13 | Hệ thống tra cứu phương tiện bị mất cắp | Stolen Vehicle Lookup System | Hệ thống ngoài | Phụ | Hệ thống của cơ quan công an, nhận số khung và số máy xe máy và trả kết quả có hay không có trong danh sách mất cắp. | Cung cấp: tra cứu số khung, số máy xe máy trong danh sách phương tiện bị mất cắp | - | REQ-22, REQ-24, REQ-25, REQ-104 |
| ACT-14 | Đầu đọc căn cước | ID Card Reader | Thiết bị | Phụ | Đầu đọc căn cước gắn chip đặt tại mỗi quầy, kết nối USB, có bộ thư viện của nhà sản xuất. Là thiết bị rời có giao tiếp riêng với hệ thống. | Cung cấp: họ tên, số căn cước, ngày sinh, địa chỉ đọc từ thẻ căn cước | - | REQ-05, REQ-06, REQ-55 |
| ACT-15 | Máy quét mã vạch | Barcode Scanner | Thiết bị | Phụ | Máy quét mã vạch đặt tại mỗi quầy, thiết bị rời nằm ngoài ranh giới. Nhân viên giao dịch thao tác trên máy, người có mục tiêu là ACT-02. | Cung cấp: mã vạch đọc từ nhãn tài sản | - | REQ-57, REQ-58, REQ-94 |
| ACT-16 | Máy in nhãn mã vạch | Barcode Label Printer | Thiết bị | Phụ | Máy in nhãn mã vạch đặt tại mỗi quầy, thiết bị rời nằm ngoài ranh giới, nhận dữ liệu nhãn từ hệ thống. | Cung cấp: in nhãn mã vạch theo mã hợp đồng để dán lên tài sản cầm cố | - | REQ-37, REQ-105 |
| ACT-17 | Bộ định thời 9 giờ sáng | Morning Timer | Thời gian | Chính | Nhịp 9 giờ sáng mỗi ngày, khởi xướng việc gửi tin nhắc cho khách có hợp đồng sắp đến hạn hoặc đã quá hạn, không có người nào ra lệnh. | Kích hoạt: 9 giờ sáng mỗi ngày, nhắc khách có hợp đồng đến hạn sau 3 ngày<br>Kích hoạt: 9 giờ sáng mỗi ngày, nhắc khách có hợp đồng quá hạn đúng 7 ngày | - | REQ-62, REQ-63, REQ-64, REQ-65, REQ-98 |
| ACT-18 | Bộ định thời 0 giờ | Midnight Timer | Thời gian | Chính | Nhịp 0 giờ mỗi ngày, khởi xướng việc chuyển hợp đồng quá hạn sang trạng thái chờ thanh lý, không có người nào ra lệnh. | Kích hoạt: 0 giờ mỗi ngày, chuyển hợp đồng quá hạn 15 ngày chưa đóng lãi hay chuộc sang chờ thanh lý | - | REQ-66, REQ-67 |

## 3. Bên liên quan không phải tác nhân

| SH | Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
|---|---|---|---|---|
| SH-01 | Chuỗi cầm đồ Phúc An (chủ sở hữu) | Quản lý hợp đồng, tài sản cầm cố và tiền mặt tại quầy; báo khách khi hợp đồng quá hạn | Báo cáo do ACT-06 Quản lý chuỗi xem | REQ-01, REQ-02, REQ-03, REQ-82 |
| SH-02 | Khách (khi giao dịch tại quầy) | Cầm đồ, đóng lãi, chuộc đồ qua nhân viên; nhận lại tài sản đúng hợp đồng | ACT-02 Nhân viên giao dịch, ACT-04 Thủ quỹ | REQ-39, REQ-41, REQ-50, REQ-56, REQ-59, REQ-60 |
| SH-02 | Khách (khi nhận tin nhắc và mã OTP) | Biết hợp đồng sắp đến hạn hoặc đã quá hạn; xác nhận đăng ký | ACT-11 Cổng SMS, ACT-12 Dịch vụ thông báo đẩy | REQ-62, REQ-63, REQ-77, REQ-98 |
| SH-13 | Người được chủ hợp đồng uỷ quyền chuộc đồ | Chuộc đồ thay chủ hợp đồng bằng giấy uỷ quyền có công chứng | ACT-02 Nhân viên giao dịch (đọc thẻ căn cước người chuộc) | REQ-54, REQ-55 |
| SH-16 | Người mua tài sản thanh lý tại quầy | Mua tài sản thanh lý | ACT-05 Quản lý cửa hàng | REQ-69, REQ-70 |
| SH-17 | Bộ phận thanh lý của chuỗi | Nhận tài sản chuyển về và bán ngoài phần mềm | ACT-05 Quản lý cửa hàng (chuyển tài sản), ACT-08 Kế toán chuỗi (nhập số tiền bán được) | REQ-72, REQ-102 |

## 4. Ứng viên tác nhân bị loại

| Ứng viên | Lý do loại | REQ |
|---|---|---|
| Cơ sở dữ liệu | A-T1: kho dữ liệu của chính hệ thống, thành phần nội bộ | REQ-88, REQ-89, REQ-93 |
| Ứng dụng di động của Phúc An | A-T1: thành phần nội bộ theo QUYET_DINH_RANH_GIOI; Khách là tác nhân, ứng dụng là giao diện của hệ thống | REQ-42, REQ-75 |
| Phần mềm, hệ thống (chủ thể "phần mềm", "hệ thống" trong nguồn) | A-T1: chính hệ thống cần xây dựng | REQ-07, REQ-14, REQ-22 |
| Bảng giá thị trường | A-T1: dữ liệu của hệ thống, do ACT-06 cập nhật | REQ-14, REQ-15 |
| Chủ hợp đồng | Gộp vào ACT-01 Khách: cùng một vai trò, cùng mục tiêu và cùng quyền | REQ-54 |
| Người cầm đồ, khách mới, khách cũ | Gộp vào ACT-01 Khách: tên đồng nghĩa, cùng mục tiêu và cùng quyền | REQ-07, REQ-08 |
| Khách (khi giao dịch tại quầy) | A-T2: chỉ tương tác qua nhân viên quầy, không thao tác trực tiếp trên hệ thống; xếp vào Mục 3 | REQ-39, REQ-50 |
| Người chuộc | A-T2: tại quầy chỉ tương tác qua Nhân viên giao dịch; là chủ hợp đồng (gộp vào Khách) hoặc người được uỷ quyền (Mục 3) | REQ-54, REQ-55 |
| Nhân viên tại quầy | Gộp vào ACT-02 Nhân viên giao dịch (ASM-09, Chờ Q-31) | REQ-94 |
| Nhân viên (cách gọi chung, kiêm hai vai trò ở cửa hàng nhỏ) | A-T3: một cá nhân có thể đóng hai vai trò; mô hình hoá theo ACT-02 và ACT-03, không tạo vai trò kiêm | REQ-96 |
| Người định giá | Gộp vào ACT-03 Nhân viên định giá: tên đồng nghĩa | REQ-97 |
| Người mua tài sản | A-T2: giao dịch bằng tiền với quản lý cửa hàng, không tương tác với hệ thống; xếp vào Mục 3 | REQ-69 |
| Bộ phận thanh lý của chuỗi | A-T2: bán ngoài phần mềm, không giao tiếp với hệ thống; xếp vào Mục 3 | REQ-72, REQ-102 |
| Ngân hàng đối tác | Gộp vào ACT-09 Cổng chi hộ: hệ thống chỉ giao tiếp qua cổng | REQ-30, REQ-32 |
| Nhà mạng | Gộp vào ACT-11 Cổng SMS: hệ thống chỉ giao tiếp qua cổng | REQ-90 |
| Nền tảng di động | Gộp vào ACT-12 Dịch vụ thông báo đẩy | REQ-99 |
| Cơ quan công an | Gộp vào ACT-13: hệ thống chỉ giao tiếp qua hệ thống tra cứu, không có cán bộ nào thao tác trên hệ thống Phúc An | REQ-24 |
| Thiết bị chụp ảnh tài sản | A-T1 và A-T4: nguồn chỉ nói nhân viên định giá "chụp ảnh", thiết bị chụp là kênh nhập của người thao tác, không có giao tiếp riêng nêu trong nguồn | REQ-10 |
| Máy in dùng in hợp đồng, biên nhận | A-T2 và A-T6: nguồn không nêu giao tiếp riêng và không liệt kê trong HE_THONG_NGOAI (ASM-11, Chờ Q-36) | REQ-33, REQ-61 |
| Két của cửa hàng | A-T2: vật chứa, không giao tiếp với hệ thống | REQ-38, REQ-57 |
| Thẻ căn cước | A-T3 và A-T2: vật mang dữ liệu, không phải vai trò; dữ liệu đến qua ACT-14 | REQ-05 |
| Nhóm phát triển phần mềm, hai quản lý cửa hàng dự họp (biên bản, đoạn "Thành phần") | A-T2: người dự họp làm rõ yêu cầu, không tương tác với hệ thống trong vai trò này; quản lý cửa hàng là ACT-05 | - |
| Quản lý cửa hàng xác nhận chênh lệch chốt ca, thủ quỹ chốt ca, nộp tiền về ngân hàng | Ngoài phạm vi lần chạy theo P00 (mục 8 của yeu-cau-cam-do.md, Ngoài trọng tâm phân tích); vai trò vẫn là ACT-04, ACT-05, mục tiêu chốt ca không tính | - |
| Bộ định thời hết hạn giao dịch thanh toán 10 phút | Bước 2.3: hết giờ chờ trong phiên, là luồng thay thế của use case | REQ-46, REQ-47 |
| Bộ định thời hiệu lực mã OTP | Bước 2.3: hết giờ chờ trong phiên đăng ký đang mở, là luồng thay thế của use case | REQ-77 |
| Bộ định thời hạn 30 ngày trả tiền thừa | A-T4: nguồn chỉ nêu thời hạn nghiệp vụ, không nêu hành vi hệ thống tự chạy theo mốc này | REQ-73 |
| Bộ định thời lưu ảnh tài sản 5 năm | A-T4: yêu cầu lưu trữ phi chức năng, nguồn không nêu hành vi tự chạy | REQ-93 |
| Hãng sản xuất đầu đọc căn cước | A-T4: chỉ cung cấp bộ thư viện lúc phát triển, không tương tác lúc vận hành | REQ-06 |
| Người nhận tin nhắn (khách nhận SMS, thông báo đẩy) | Là chủ thể nhận kết quả thụ động qua kênh ngoài; xếp vào Mục 3 | REQ-62, REQ-63 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-36 | Việc in hợp đồng và biên nhận chuộc đồ dùng loại máy in nào, và máy in đó có giao tiếp riêng với hệ thống (cần coi là thiết bị ngoài) hay chỉ là máy in văn phòng thông thường? (Máy in văn phòng thông thường, không phải tác nhân / Thiết bị riêng, nêu rõ) | Danh sách tác nhân thiết bị; REQ-33, REQ-61 | "Nhân viên giao dịch in hợp đồng để khách ký" (yeu-cau-cam-do.md, Mục 3); HE_THONG_NGOAI chỉ liệt kê máy in nhãn mã vạch |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-09 | Người tra cứu hợp đồng bằng mã vạch tại quầy là Nhân viên giao dịch. | Nguồn chỉ nêu "Nhân viên tại quầy" qua REQ-94, không nói vai trò nào; Nhân viên giao dịch là người quét mã vạch trên nhãn ở luồng chuộc đồ (REQ-57). Chờ Q-31 | ACT-02, REQ-94 |
| ASM-10 | Hệ thống báo cho Quản lý cửa hàng về hợp đồng chờ thanh lý trên chính phần mềm, không qua kênh ngoài. | Nguồn nói "báo cho quản lý cửa hàng" nhưng không nêu kênh; chọn kênh không cần thêm tác nhân hệ thống ngoài. Chờ Q-22 | ACT-05, REQ-68 |
| ASM-11 | Máy in hợp đồng và biên nhận chuộc đồ là đầu ra in thông thường của máy trạm, không là tác nhân thiết bị. | Nguồn không liệt kê thiết bị in này trong HE_THONG_NGOAI và không nêu giao thức riêng. Chờ Q-36 | Mục 1 (dòng máy in hợp đồng), REQ-33, REQ-61 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P00 | REQ-94 | Nội dung ghi "Nhân viên tại quầy" làm chủ thể; P01 phải chọn vai trò cụ thể (ASM-09) nên REQ này chưa đọc riêng ra được tác nhân | Sau khi Q-31 được trả lời, cập nhật chủ thể của REQ-94 thành vai trò đã chốt |

## Vấn đề còn mở

- Bộ định thời tách thành hai tác nhân (ACT-17 nhịp 9 giờ sáng, ACT-18 nhịp 0 giờ) vì hai nhịp độc lập có mục tiêu khác nhau theo quy tắc đặt tên của prompt. Nếu người dùng muốn một Bộ định thời duy nhất thì gộp hai dòng, mã ACT-18 chuyển trạng thái Loại.
- Chủ thể thao tác đóng lãi tại quầy (REQ-39, REQ-45) được gán cho Thủ quỹ chỉ do suy từ câu "tại quầy (thủ quỹ thu tiền mặt)"; nguồn không nói rõ ai nhập giao dịch trên phần mềm. Chưa tạo Q mới vì suy ra trực tiếp từ một chức năng nguồn nêu.
- Chủ thể thao tác chuộc đồ (REQ-50, ghi nhận chuộc trên phần mềm) được chia giữa Nhân viên giao dịch (đọc thẻ, quét mã, in biên nhận) và Thủ quỹ (thu tiền) theo đúng các câu nguồn; không có tác nhân nào "ghi nhận chuộc xong" riêng.
- REQ-88 (hệ thống ghi nhật ký thay đổi hợp đồng) không gắn tác nhân riêng: là hành vi nội bộ của hệ thống, tác nhân liên quan duy nhất là ACT-07 xem nhật ký (REQ-86).
- REQ-14 (gợi ý giá tham khảo) gắn ACT-03 là người nhận gợi ý; nguồn không nói ai xem gợi ý, suy từ vị trí câu trong Mục 2.
- Mục Target 1 đạt, trừ ghi chú: thành phần "Máy trạm tại quầy" chỉ ngụ ý qua cụm "tại quầy", ghi để đủ ranh giới nền tảng.
