# P11a - SCR-01 Trang chủ Người quan tâm - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3); các use case của màn hình này chưa có đặc tả P04 và phân tích P07 trong phạm vi dự án; P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); mục h) của SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14 (đều ghi Không có thông điệp mới). Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-104; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-105. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-010 và các màn hình điều hướng (SCR-01, SCR-02, SCR-06, SCR-07, SCR-08, SCR-09, SCR-10, SCR-15, SCR-16); đây là lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Có. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-01 (UC-001, UC-002, UC-003, ACT-01 Người quan tâm, ứng dụng di động) |
| Mã Q, ASM cuối đã cấp | Q-105; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-01 Trang chủ Người quan tâm (Prospect home) |
| UC | UC-001, UC-002, UC-003 (use case được mở từ màn hình điều hướng) |
| Bước UC | - (màn hình điều hướng không phục vụ bước nào của use case; bước 1 của use case có màn hình đích là người dùng nhấn thẻ lối vào ở đây) |
| Tác nhân | ACT-01 Người quan tâm |
| Boundary AC | Điều hướng (UC-001, UC-002, UC-003) |
| DC | Chưa có (điều hướng) |
| Loại màn hình | Độc lập |
| Đến từ | START-ACT-01 (TR-01, mẫu 1, mở ứng dụng khi chưa có phiên làm việc; Q-99); chưa có màn hình nào khác của ACT-01 dẫn về màn hình này |
| Đi tới | Chưa có màn hình đích cho UC-001, UC-002, UC-003. Màn hình kết thúc của sơ đồ cho tới khi các use case này có màn hình |

## c) Hình ảnh màn hình

Mockup HTML: mockups/SCR-01-prospect-home.html.

Nội dung vừa một màn hình. Các thẻ lối vào chưa có màn hình đích vẫn hiển thị (UI-STT 44).

```text
+----------------------------------------+
| [VietFit]                              |
|----------------------------------------|
|                                        |
| Trang chủ Người quan tâm               |
|                                        |
| +-----------------------------------+  |
| | [i] Xem giá gói tập               |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Xem lịch lớp nhóm             |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Đăng ký tài khoản hội viên    |  |
| +-----------------------------------+  |
|                                        |
+----------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit | Trên cùng, cao 56 dp; logo bên trái cách mép 16 dp, cao 28 dp. Không có nút Trang chủ | UI-STT 10, 12, 45 |
| Dải thông báo | Không dùng ở màn hình này | - | Thông điệp của use case: xem dòng cuối mục d) |
| Tiêu đề màn hình | Trang chủ Người quan tâm | Đầu vùng nội dung, 20 sp Bold | UI-STT 13 |
| Nội dung | 3 thẻ lối vào use case: biểu tượng 24 dp bên trái, tên use case 16 sp Medium | Cuộn dọc, lề trái phải 16 dp, thẻ rộng hết vùng nội dung, cao tối thiểu 64 dp, cách nhau 8 dp | UI-STT 10, 28, 44 |
| Hành động | Không có nút hành động | - | Màn hình điều hướng chỉ chứa lối vào use case |
| Thông điệp | Không có hộp thông điệp | - | Màn hình không gọi máy chủ |

Dữ liệu mẫu: tên 3 use case lấy đúng cột Tên (VI) của P02 bảng 4a, xếp theo mã UC tăng dần.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Nút quay lại của hệ thống (Android) hoặc cử chỉ quay lại (iOS) | Nút | Nhấn | Không mở màn hình nào của phần mềm: màn hình điều hướng là màn hình mở đầu của tác nhân. Android đưa ứng dụng xuống nền theo hành vi chuẩn của nền tảng; iOS không có cử chỉ quay lại ở màn hình gốc. Màn hình không có nút Trang chủ | UI-STT 15, 45; Material Design, Apple HIG (điều hướng quay lại theo nền tảng) |
| 3 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Trang chủ Người quan tâm | UI-STT 13 |
| 4 | Danh sách lối vào use case | Vùng hiển thị | Khởi tạo | Hiển thị mỗi use case của người quan tâm một thẻ theo thứ tự mã UC tăng dần (UC-001, UC-002, UC-003), tên use case tiếng Việt. Màn hình chỉ chứa lối vào các use case, không có trường nhập, nút hành động hay dải thông báo | P02 bảng 4a; P11a mục A2; UI-STT 28, 44 |
| 5 | Thẻ lối vào Xem giá gói tập (UC-001) | Liên kết | Nhấn | Chưa có màn hình đích (UC-001); ở lại SCR-01 | UI-STT 44; screen-transition.md node SCR-01 |
| 6 | Thẻ lối vào Xem lịch lớp nhóm (UC-002) | Liên kết | Nhấn | Chưa có màn hình đích (UC-002); ở lại SCR-01 | UI-STT 44; screen-transition.md node SCR-01 |
| 7 | Thẻ lối vào Đăng ký tài khoản hội viên (UC-003) | Liên kết | Nhấn | Chưa có màn hình đích (UC-003); ở lại SCR-01 | UI-STT 44; screen-transition.md node SCR-01 |
| 8 | Thông điệp của use case | Vùng hiển thị | Khởi tạo | Không có: các use case UC-001, UC-002, UC-003 chưa có đặc tả P04 trong phạm vi dự án nên chưa có thông điệp kết thúc hay huỷ use case hiển thị trên màn hình điều hướng | P02 bảng 4a; UI-STT 44 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Tên lối vào use case | - | Chữ | Hiển thị trong thẻ; căn trái; chữ #1C1F2A Medium 500 16 sp | Tên tiếng Việt của use case theo P02 bảng 4a; mỗi use case của tác nhân một thẻ; thứ tự mã UC tăng dần | Màn hình không có dữ liệu nghiệp vụ khác và không có trường nhập | P02 bảng 4a; UI-STT 28, 44 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình chỉ chứa lối vào use case, không có trường nhập và không có nút hành động | - |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-01 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-001, UC-002, UC-003 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-01 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ | - |
| SCR-01 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-01 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Các thẻ lối vào là danh sách (list) các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-01 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 64 dp, rộng hết vùng nội dung, khoảng cách 8 dp | - |
| SCR-01 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Màn hình gốc của tác nhân không có nút Quay lại và không có cử chỉ quay lại về màn hình khác của phần mềm, đúng hành vi iOS | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình điều hướng không hiển thị thông điệp trong danh mục ở ui-standards.md.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-99 (điểm khởi đầu của ứng dụng, lối vào Đăng nhập), Q-46 (hội viên xem giá gói tập và lịch lớp nhóm độc lập), Q-95 (trợ giúp).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3, F4 (PKG-05) | Màn hình điều hướng SCR-01 của ACT-01 chưa có lớp thiết kế giao diện tương ứng trong P10 (đề xuất đã ghi ở screen-list.md) | Thêm phần tử View điều hướng của ACT-01 vào package giao diện PKG-05 MemberMobileUI. Chỉ đổi cấu trúc thiết kế nên P10 không chạy lại. Chưa áp dụng |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 9: có 1 dòng Vi phạm còn mở (Nielsen 1) vì lối vào UC-001, UC-002, UC-003 chưa có màn hình đích; đây là hệ quả của phạm vi dự án chỉ có đặc tả bốn use case, không phải chỗ đặc tả thiếu, nên không có mã Q. Không có vi phạm WCAG AA chưa xử lý.
- Cách hiển thị và phản hồi khi nhấn lối vào chưa có màn hình đích không được ui-standards.md quy định; màn hình hiển thị đầy đủ như lối vào có đích và không phản hồi, theo UI-STT 44 và cách đã dùng ở SCR-11.
- Màn hình không có thông tin về người đang đăng nhập hay nút đăng xuất vì đặc tả không có (Q-47, Q-99).
