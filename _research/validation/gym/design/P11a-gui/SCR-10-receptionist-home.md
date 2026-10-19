# P11a - SCR-10 Trang chủ Lễ tân - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện: bước 1, bước kết thúc); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3); P07-uc-analysis/UC-005 (phiên bản 1.0; Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); mục h) của SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14 (đều ghi Không có thông điệp mới). Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-104; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-105. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-010 và các màn hình điều hướng (SCR-01, SCR-02, SCR-06, SCR-07, SCR-08, SCR-09, SCR-10, SCR-15, SCR-16); đây là lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Có. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-10 (UC-005, UC-007, UC-017, ACT-05 Lễ tân, ứng dụng web) |
| Mã Q, ASM cuối đã cấp | Q-105; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-10 Trang chủ Lễ tân (Receptionist home) |
| UC | UC-005, UC-007, UC-017 (use case được mở từ màn hình điều hướng) |
| Bước UC | - (màn hình điều hướng không phục vụ bước nào của use case; bước 1 của use case có màn hình đích là người dùng nhấn thẻ lối vào ở đây) |
| Tác nhân | ACT-05 Lễ tân |
| Boundary AC | Điều hướng (UC-005, UC-007, UC-017) |
| DC | Chưa có (điều hướng) |
| Loại màn hình | Độc lập |
| Đến từ | START-ACT-05 (TR-11, mẫu 1, sau khi có phiên làm việc, lễ tân đã xác thực; Q-47); mọi màn hình khác của ACT-05 qua menu trái (mẫu 1, ghi ở node START-ACT-05) |
| Đi tới | SCR-11 (TR-12, mẫu 1, lối vào UC-005); chưa có màn hình đích: UC-007, UC-017 |

## c) Hình ảnh màn hình

Mockup HTML: mockups/SCR-10-receptionist-home.html.

Nội dung vừa một màn hình. Các thẻ lối vào chưa có màn hình đích vẫn hiển thị (UI-STT 44).

```text
+-------------------------------------------------------------------------------------------------------------------+
| [VietFit]                                                                                                         |
+--------------------------------+----------------------------------------------------------------------------------+
| > Trang chủ                    | Trang chủ Lễ tân                                                                 |
|   Mua hoặc gia hạn gói tập     |                                                                                  |
|   Chuyển nhượng gói tập        | +------------------------------------+                                           |
|   Bán vé tập một ngày          | | [i] Mua hoặc gia hạn gói tập       |                                           |
|                                | +------------------------------------+                                           |
|                                | +------------------------------------+                                           |
|                                | | [i] Chuyển nhượng gói tập          |                                           |
|                                | +------------------------------------+                                           |
|                                | +------------------------------------+                                           |
|                                | | [i] Bán vé tập một ngày            |                                           |
|                                | +------------------------------------+                                           |
+--------------------------------+----------------------------------------------------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit | Trên cùng, cao 56 px; logo trái cách mép 24 px, cao 32 px | UI-STT 11, 12 |
| Menu | Trang chủ và 3 lối vào use case; mục Trang chủ đang chọn | Trái, rộng 240 px, nền #F4F5F9, mỗi mục cao 44 px | UI-STT 44, 46, 47, 48 |
| Dải thông báo | Không dùng ở màn hình này | - | Thông điệp của use case: xem dòng cuối mục d) |
| Tiêu đề màn hình | Trang chủ Lễ tân | Đầu vùng nội dung, 24 px Bold | UI-STT 13 |
| Nội dung | 3 thẻ lối vào use case: biểu tượng 24 px bên trái, tên use case 16 px Medium | Lề 24 px, thẻ rộng 320 px, cao 64 px, cách nhau 8 px | UI-STT 11, 28, 44 |
| Hành động | Không có nút hành động | - | Màn hình điều hướng chỉ chứa lối vào use case |
| Thông điệp | Không có hộp thông điệp | - | Màn hình không gọi máy chủ |

Dữ liệu mẫu: tên 3 use case lấy đúng cột Tên (VI) của P02 bảng 4a, xếp theo mã UC tăng dần.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Menu trái | Liên kết | Khởi tạo | Hiển thị các mục theo thứ tự: Trang chủ, Mua hoặc gia hạn gói tập (UC-005), Chuyển nhượng gói tập (UC-007), Bán vé tập một ngày (UC-017); đánh dấu mục Trang chủ đang chọn | UI-STT 44, 46, 47, 48; P02 bảng 4a |
| 3 | Mục menu Trang chủ | Liên kết | Nhấn | Ở lại SCR-10, không đổi gì (mục đang chọn) | UI-STT 47 |
| 4 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Trang chủ Lễ tân | UI-STT 13 |
| 5 | Danh sách lối vào use case | Vùng hiển thị | Khởi tạo | Hiển thị mỗi use case của lễ tân một thẻ theo thứ tự mã UC tăng dần (UC-005, UC-007, UC-017), tên use case tiếng Việt. Màn hình chỉ chứa lối vào các use case, không có trường nhập, nút hành động hay dải thông báo | P02 bảng 4a; P11a mục A2; UI-STT 28, 44 |
| 6 | Thẻ lối vào Mua hoặc gia hạn gói tập (UC-005) | Liên kết | Nhấn | Rời màn hình và mở SCR-11 (mẫu 1, TR-12). Nhấn mục menu cùng use case cho kết quả như nhau | UC-005 bước 1; screen-transition.md TR-12 |
| 7 | Thẻ lối vào Chuyển nhượng gói tập (UC-007) | Liên kết | Nhấn | Chưa có màn hình đích (UC-007); ở lại SCR-10. Nhấn mục menu cùng use case cho kết quả như nhau | UI-STT 44; screen-transition.md node SCR-10 |
| 8 | Thẻ lối vào Bán vé tập một ngày (UC-017) | Liên kết | Nhấn | Chưa có màn hình đích (UC-017); ở lại SCR-10. Nhấn mục menu cùng use case cho kết quả như nhau | UI-STT 44; screen-transition.md node SCR-10 |
| 9 | Thông điệp của use case | Vùng hiển thị | Khởi tạo | Không có thông điệp của use case hiển thị khi mở màn hình: UC-005 (bán tại quầy) kết thúc ở bước 13 tại SCR-14; lễ tân rời SCR-14 bằng menu trái, không kèm thông điệp | UC-005 bước 13 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Tên lối vào use case | - | Chữ | Hiển thị trong thẻ; căn trái; chữ #1C1F2A Medium 500 16 px | Tên tiếng Việt của use case theo P02 bảng 4a; mỗi use case của tác nhân một thẻ; thứ tự mã UC tăng dần | Màn hình không có dữ liệu nghiệp vụ khác và không có trường nhập | P02 bảng 4a; UI-STT 28, 44 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình chỉ chứa lối vào use case, không có trường nhập và không có nút hành động | - |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-10 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-007, UC-017 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-10 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ | - |
| SCR-10 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-10 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Menu trái là vùng điều hướng (nav) có aria-current ở mục Trang chủ; các thẻ lối vào là danh sách các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-10 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao 64 px, rộng 320 px; mục menu cao 44 px | - |
| SCR-10 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu trái có cùng thứ tự các mục với SCR-11, SCR-12, SCR-13, SCR-14 (UI-STT 46, 48) | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình điều hướng không hiển thị thông điệp trong danh mục ở ui-standards.md.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-47 (lễ tân có phải đăng nhập không), Q-95 (trợ giúp).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3, F4 (PKG-07) | Màn hình điều hướng SCR-10 của ACT-05 chưa có lớp thiết kế giao diện tương ứng trong P10 (đề xuất đã ghi ở screen-list.md) | Thêm phần tử View điều hướng của ACT-05 vào package giao diện PKG-07 ReceptionWebUI. Chỉ đổi cấu trúc thiết kế nên P10 không chạy lại. Chưa áp dụng |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 9: có 1 dòng Vi phạm còn mở (Nielsen 1) vì lối vào UC-007, UC-017 chưa có màn hình đích; đây là hệ quả của phạm vi dự án chỉ có đặc tả bốn use case, không phải chỗ đặc tả thiếu, nên không có mã Q. Không có vi phạm WCAG AA chưa xử lý.
- Cách hiển thị và phản hồi khi nhấn lối vào chưa có màn hình đích không được ui-standards.md quy định; màn hình hiển thị đầy đủ như lối vào có đích và không phản hồi, theo UI-STT 44 và cách đã dùng ở SCR-11.
- Màn hình không có thông tin về người đang đăng nhập hay nút đăng xuất vì đặc tả không có (Q-47, Q-99).
