# P11a - ui-standards.md - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (Giai đoạn 1) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE sau P09); P01, P02, P04 (UC-005, UC-007, UC-009, UC-013), P05, P06, P07 (4 UC), P08, P09, P10 1.0 |
| Phạm vi | Toàn hệ thống (RiderApp và StaffWeb) |

Placeholder: CHE_DO_CHAY = "Giai đoạn 1"; THIET_BI_HIEN_THI = "RiderApp: điện thoại Android, iOS từ 360 x 640 dp, dọc, cảm ứng, có camera. StaffWeb: máy tính từ 1366 x 768, chuột và bàn phím"; NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = "Có"; THONG_TIN_TAI_LIEU = Không có; YEU_CAU_BO_SUNG = Không có.

## a) Bảng chuẩn hoá

| STT | Nhóm | Hạng mục | Quy định | Căn cứ |
|---|---|---|---|---|
| 1 | Display | Kích thước mục tiêu | RiderApp: 360 x 640 dp dọc, không xoay ngang. StaffWeb: 1366 x 768, bố cục co giãn tới 1920 x 1080 | THIET_BI_HIEN_THI; NFR-05 |
| 2 | Display | Chế độ màu | Chỉ chế độ sáng; nền #FFFFFF, chữ chính #1A1A1A (tương phản 17.4:1) | Quyết định thiết kế (NHAN_DIEN_THUONG_HIEU = Không có); WCAG 1.4.3 |
| 3 | Display | Điểm ngắt (StaffWeb) | Một điểm ngắt 1280 px: dưới 1280 menu trái thu thành biểu tượng | WCAG 1.4.10 |
| 4 | Screen | Bố cục vùng RiderApp | Thanh tiêu đề cao 56 dp (nút Quay lại bên trái, tiêu đề giữa); vùng nội dung; vùng hành động cố định đáy cao 72 dp | Material Design (top app bar); Nielsen 4 |
| 5 | Screen | Bố cục vùng StaffWeb | Thanh trên 56 px (tên hệ thống trái, tên nhân viên phải); menu trái rộng 240 px; nội dung; vùng hành động cuối form | Nielsen 4; Shneiderman nhất quán |
| 6 | Screen | Vị trí nút | Nút chính bên phải vùng hành động (StaffWeb), toàn chiều rộng ở đáy (RiderApp); nút phụ bên trái nút chính; tối đa một nút chính mỗi màn hình | Material Design (mức nhấn mạnh); Nielsen 4 |
| 7 | Screen | Vị trí thông điệp | Lỗi tại trường: ngay dưới trường. Lỗi nghiệp vụ, lỗi hệ thống: hộp thoại giữa màn hình (RiderApp) hoặc thanh thông báo đầu vùng nội dung (StaffWeb) | Nielsen 9; Baymard (lỗi cạnh trường) |
| 8 | Screen | Chữ, số, tiền, ngày giờ | Tiền: "10.000 đ" (dấu chấm phân cách nghìn, ký hiệu đ sau số); ngày "dd/mm/yyyy"; giờ "HH:mm" 24 giờ; thời lượng "x giờ y phút" | Nielsen 2; GL-05 (đơn vị đồng) |
| 9 | Screen | Văn phong, thuật ngữ | Câu ngắn, xưng "bạn"; viết hoa chữ đầu câu; dùng đúng thuật ngữ P05 (Chuyến đi, Ụ khoá, Khoản tạm giữ, Lệnh điều chuyển), không dùng từ đồng nghĩa không dùng | P05; Nielsen 2, 4 |
| 10 | Screen | Phối màu | Màu chủ đạo #0B5FA5 (tương phản với trắng 6.6:1); lỗi #B3261E kèm biểu tượng và chữ; thành công #1E7B34 kèm biểu tượng; không dùng màu là tín hiệu duy nhất | WCAG 1.4.1, 1.4.3 |
| 11 | Control | Nút chính | Nền #0B5FA5, chữ trắng 16 sp đậm, cao 48 dp (RiderApp) hoặc 40 px (StaffWeb), bo góc 8 | Material Design; WCAG 2.5.8 |
| 12 | Control | Nút phụ | Viền 1 px #0B5FA5, nền trắng, chữ #0B5FA5, cùng kích thước nút chính | Material Design |
| 13 | Control | Ô nhập, danh sách chọn | Cao 48 dp hoặc 40 px; nhãn đặt trên ô; dấu "*" và chữ "(bắt buộc)" cho trường bắt buộc; không dùng placeholder thay nhãn | Baymard; WCAG 3.3.2 |
| 14 | Control | Vùng bấm tối thiểu | 48 x 48 dp (RiderApp); 24 x 24 px (StaffWeb) | Material Design; WCAG 2.5.8 |
| 15 | Control | Kiểm tra dữ liệu nhập | Kiểm tra khi rời trường và khi nhấn nút chính; thứ tự: bắt buộc --> định dạng --> miền giá trị --> quy tắc nghiệp vụ (quy tắc nghiệp vụ do máy chủ trả về); không báo lỗi khi đang gõ; giữ dữ liệu đã nhập | Baymard; WCAG 3.3.1, 3.3.3, 3.3.7 |
| 16 | Control | Tiêu điểm | Thứ tự tiêu điểm theo thứ tự đọc trên xuống, trái sang phải; viền tiêu điểm 2 px #0B5FA5 không bị che | WCAG 2.4.3, 2.4.7, 2.4.11 |
| 17 | Menu | Cấu trúc theo tác nhân | RiderApp: màn hình chính chứa lối vào use case của ACT-01. StaffWeb: menu trái chỉ hiện nhóm chức năng của vai trò đăng nhập (ACT-02 đến ACT-06), thứ tự theo P02 | P02; Nielsen 4 |
| 18 | Menu | Mục đang chọn | Nền #E3EEF8 và vạch trái 4 px màu chủ đạo, kèm aria-current | WCAG 1.4.1, 4.1.2 |
| 19 | Bàn phím | Phím tắt | Không định nghĩa phím tắt riêng. Enter kích hoạt nút chính của form; Esc đóng hộp thoại (StaffWeb) | Nielsen 7; tránh trùng phím trình duyệt |
| 20 | Messages | Chỉ báo bận | Thao tác gọi máy chủ quá 0,5 giây hiện chỉ báo bận có chữ mô tả; không cho nhấn lại nút chính khi đang xử lý; không có nút huỷ khi đặc tả không cho | Nielsen 1; NFR-02 |
| 21 | Messages | Thông báo trạng thái | Thông báo trạng thái được đọc bởi trình đọc màn hình (vùng live) | WCAG 4.1.3 |
| 22 | Error | Lỗi nhập | Tại trường, chữ đỏ kèm biểu tượng, nói cụ thể điều sai và cách sửa | Nielsen 9; Baymard |
| 23 | Error | Lỗi nghiệp vụ | Hộp thoại có tiêu đề, nội dung theo mẫu điều gì sai --> vì sao --> làm gì tiếp, một nút đóng đặt tên theo hành động tiếp theo | Nielsen 9; MSG |
| 24 | Error | Lỗi hệ thống, hệ thống ngoài | Hộp thoại MSG-05, không hiện mã kỹ thuật, giữ nguyên màn hình và dữ liệu | Nielsen 9; NFR-06 |
| 25 | Help | Trợ giúp | Biểu tượng "?" góc phải thanh tiêu đề mở trang hướng dẫn của màn hình; thuật ngữ theo P05 | Nielsen 10; WCAG 3.2.6 |
| 26 | Khả năng tiếp cận | Tương phản, nhãn, phóng to | Chữ 4.5:1, thành phần 3:1; mọi trường có nhãn gắn; hình có văn bản thay thế; hỗ trợ cỡ chữ hệ thống tới 200% không cắt chữ | WCAG 1.1.1, 1.4.3, 1.4.4, 1.4.11 |
| 27 | Xác nhận | Thao tác cần xác nhận | Thao tác tài chính khởi phát từ người dùng: hộp xác nhận với nút đặt tên theo hành động. Thuê xe không có bước xác nhận riêng vì đặc tả UC-005 không có (Q-38) | WCAG 3.3.4; C1 |

## b) Danh mục thông điệp

| MSG | Loại | Nội dung hiển thị | Nút và hành động | Nguồn |
|---|---|---|---|---|
| MSG-01 | Đang xử lý | Đang kiểm tra và mở khoá ụ... | Không có nút | UC-005 bước 2 đến 6; mục 20 |
| MSG-02 | Lỗi | Không thể thuê xe tại ụ này. (Lý do cụ thể chờ Q-22) | "Đóng" --> đóng hộp, quay về SCR-02 | UC-005 bước 2a, 2b, 2c, 3a |
| MSG-03 | Lỗi | Không tạm giữ được tiền trên thẻ của bạn nên chưa thể thuê xe. Vui lòng kiểm tra thẻ rồi thử lại. (Nội dung chờ Q-08) | "Đóng" --> đóng hộp, quay về SCR-02 | UC-005 bước 5a |
| MSG-04 | Lỗi | Mã vừa quét không phải mã QR của ụ khoá CityBike. Hãy quét mã dán trên ụ khoá. | "Quét lại" --> đóng hộp, bật lại camera | UC-005 bước 1 (kiểm tra định dạng tại boundary) |
| MSG-05 | Lỗi | Không kết nối được với hệ thống. Vui lòng thử lại sau ít phút. | "Đóng" --> đóng hộp, giữ màn hình hiện tại | Chuẩn mục 24 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-37 | Ứng dụng có thông báo cho người thuê xe khi ụ đã mở khoá, khi chuyến đi bắt đầu, khi hết 60 giây mà chưa rút xe, và khi chuyến kết thúc không? (Có / Không cho từng sự kiện) | SCR-02, MSG, P04 UC-005, UC-007 | P04 UC-005 không có bước phản hồi thành công; Mục 3 |
| Q-38 | Trước khi tạm giữ 200.000 đồng, người thuê xe có cần xác nhận không? (Có / Không) | SCR-02, WCAG 3.3.4 | Mục 3 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Màu chủ đạo, phông chữ là quyết định thiết kế vì không có nhận diện thương hiệu.
