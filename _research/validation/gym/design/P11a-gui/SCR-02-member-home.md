# P11a - SCR-02 Trang chủ Hội viên - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005, UC-010 (phiên bản 1.0; luồng sự kiện: bước 1, bước kết thúc); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3); P07-uc-analysis/UC-005, UC-010 (phiên bản 1.0; Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); mục h) của SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14 (đều ghi Không có thông điệp mới). Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-104; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-105. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-010 và các màn hình điều hướng (SCR-01, SCR-02, SCR-06, SCR-07, SCR-08, SCR-09, SCR-10, SCR-15, SCR-16); đây là lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Có. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-02 (UC-005, UC-006, UC-010, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025, ACT-02 Hội viên, ứng dụng di động) |
| Mã Q, ASM cuối đã cấp | Q-105; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-02 Trang chủ Hội viên (Member home) |
| UC | UC-005, UC-006, UC-010, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025 (use case được mở từ màn hình điều hướng) |
| Bước UC | - (màn hình điều hướng không phục vụ bước nào của use case; bước 1 của use case có màn hình đích là người dùng nhấn thẻ lối vào ở đây) |
| Tác nhân | ACT-02 Hội viên |
| Boundary AC | Điều hướng (UC-005, UC-006, UC-010, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025) |
| DC | Chưa có (điều hướng) |
| Loại màn hình | Độc lập |
| Đến từ | START-ACT-02 (TR-02, mẫu 1, sau khi có phiên làm việc, hội viên đã xác thực; Q-99); mọi màn hình khác của ACT-02 qua nút Trang chủ (mẫu 1, ghi ở node START-ACT-02) |
| Đi tới | SCR-03 (TR-03, mẫu 1, lối vào UC-005); SCR-06 (TR-07, mẫu 1, lối vào UC-010); chưa có màn hình đích: UC-006, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025 |

## c) Hình ảnh màn hình

Mockup HTML: mockups/SCR-02-member-home.html.

Nội dung dài hơn một màn hình nên cuộn dọc. Các thẻ lối vào chưa có màn hình đích vẫn hiển thị (UI-STT 44).

```text
+----------------------------------------+
| [VietFit]                              |
|----------------------------------------|
|                                        |
| Trang chủ Hội viên                     |
|                                        |
| +-----------------------------------+  |
| | [i] Mua hoặc gia hạn gói tập      |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Bảo lưu gói tập               |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Đặt chỗ lớp nhóm              |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Huỷ chỗ lớp nhóm              |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Nhận chỗ từ danh sách chờ     |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Vào chi nhánh                 |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Mua gói buổi tập cá nhân      |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Đặt buổi tập cá nhân          |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Huỷ buổi tập cá nhân          |  |
| +-----------------------------------+  |
| +-----------------------------------+  |
| | [i] Xem chỉ số cơ thể             |  |
| +-----------------------------------+  |
|                                        |
+----------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit | Trên cùng, cao 56 dp; logo bên trái cách mép 16 dp, cao 28 dp. Không có nút Trang chủ | UI-STT 10, 12, 45 |
| Dải thông báo | Không dùng ở màn hình này | - | Thông điệp của use case: xem dòng cuối mục d) |
| Tiêu đề màn hình | Trang chủ Hội viên | Đầu vùng nội dung, 20 sp Bold | UI-STT 13 |
| Nội dung | 10 thẻ lối vào use case: biểu tượng 24 dp bên trái, tên use case 16 sp Medium | Cuộn dọc, lề trái phải 16 dp, thẻ rộng hết vùng nội dung, cao tối thiểu 64 dp, cách nhau 8 dp | UI-STT 10, 28, 44 |
| Hành động | Không có nút hành động | - | Màn hình điều hướng chỉ chứa lối vào use case |
| Thông điệp | Không có hộp thông điệp | - | Màn hình không gọi máy chủ |

Dữ liệu mẫu: tên 10 use case lấy đúng cột Tên (VI) của P02 bảng 4a, xếp theo mã UC tăng dần.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Nút quay lại của hệ thống (Android) hoặc cử chỉ quay lại (iOS) | Nút | Nhấn | Không mở màn hình nào của phần mềm: màn hình điều hướng là màn hình mở đầu của tác nhân. Android đưa ứng dụng xuống nền theo hành vi chuẩn của nền tảng; iOS không có cử chỉ quay lại ở màn hình gốc. Màn hình không có nút Trang chủ | UI-STT 15, 45; Material Design, Apple HIG (điều hướng quay lại theo nền tảng) |
| 3 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Trang chủ Hội viên | UI-STT 13 |
| 4 | Danh sách lối vào use case | Vùng hiển thị | Khởi tạo | Hiển thị mỗi use case của hội viên một thẻ theo thứ tự mã UC tăng dần (UC-005, UC-006, UC-010, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025), tên use case tiếng Việt. Màn hình chỉ chứa lối vào các use case, không có trường nhập, nút hành động hay dải thông báo | P02 bảng 4a; P11a mục A2; UI-STT 28, 44 |
| 5 | Thẻ lối vào Mua hoặc gia hạn gói tập (UC-005) | Liên kết | Nhấn | Rời màn hình và mở SCR-03 (mẫu 1, TR-03) | UC-005 bước 1; screen-transition.md TR-03 |
| 6 | Thẻ lối vào Bảo lưu gói tập (UC-006) | Liên kết | Nhấn | Chưa có màn hình đích (UC-006); ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02 |
| 7 | Thẻ lối vào Đặt chỗ lớp nhóm (UC-010) | Liên kết | Nhấn | Rời màn hình và mở SCR-06 (mẫu 1, TR-07) | UC-010 bước 1; screen-transition.md TR-07 |
| 8 | Thẻ lối vào Huỷ chỗ lớp nhóm (UC-011) | Liên kết | Nhấn | Chưa có màn hình đích (UC-011); ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02 |
| 9 | Thẻ lối vào Nhận chỗ từ danh sách chờ (UC-012) | Liên kết | Nhấn | Chưa có màn hình đích (UC-012); ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02 |
| 10 | Thẻ lối vào Vào chi nhánh (UC-018) | Liên kết | Nhấn | Chưa có màn hình đích (UC-018); hiển thị mã QR của hội viên: Q-97; ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02; Q-97 |
| 11 | Thẻ lối vào Mua gói buổi tập cá nhân (UC-019) | Liên kết | Nhấn | Chưa có màn hình đích (UC-019); ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02 |
| 12 | Thẻ lối vào Đặt buổi tập cá nhân (UC-020) | Liên kết | Nhấn | Chưa có màn hình đích (UC-020); ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02 |
| 13 | Thẻ lối vào Huỷ buổi tập cá nhân (UC-023) | Liên kết | Nhấn | Chưa có màn hình đích (UC-023); ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02 |
| 14 | Thẻ lối vào Xem chỉ số cơ thể (UC-025) | Liên kết | Nhấn | Chưa có màn hình đích (UC-025); ở lại SCR-02 | UI-STT 44; screen-transition.md node SCR-02 |
| 15 | Thông điệp của use case | Vùng hiển thị | Khởi tạo | Không có thông điệp của use case hiển thị khi mở màn hình: UC-005 kết thúc ở bước 13 tại SCR-05 và UC-010 kết thúc ở bước 9 tại SCR-07, ở luồng 7a4 tại SCR-08, hoặc ở lại SCR-06 khi thất bại (luồng 4a, 7a2a); hội viên về màn hình này bằng nút Trang chủ, không kèm thông điệp | UC-005 bước 13; UC-010 bước 9, luồng 4a, 7a2a, 7a4 |

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
| SCR-02 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-006, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-02 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ (cuộn dọc khi dài hơn màn hình) | - |
| SCR-02 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-02 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Các thẻ lối vào là danh sách (list) các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-02 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 64 dp, rộng hết vùng nội dung, khoảng cách 8 dp | - |
| SCR-02 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Thứ tự lối vào theo mã UC tăng dần (UI-STT 44) như thứ tự các use case của hội viên trong P02; nút Trang chủ ở mọi màn hình khác của ACT-02 đều dẫn về màn hình này | - |
| SCR-02 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Màn hình gốc của tác nhân không có nút Quay lại và không có cử chỉ quay lại về màn hình khác của phần mềm, đúng hành vi iOS | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình điều hướng không hiển thị thông điệp trong danh mục ở ui-standards.md.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-99 (điểm khởi đầu, lối vào Đăng nhập UC-004), Q-97 (màn hình mã QR của UC-018), Q-46 (hội viên xem giá gói tập và lịch lớp nhóm độc lập: UC-001, UC-002 chưa là lối vào ở đây), Q-92 (hội viên và huấn luyện viên chung một ứng dụng), Q-95 (trợ giúp).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3, F4 (PKG-05) | Màn hình điều hướng SCR-02 của ACT-02 chưa có lớp thiết kế giao diện tương ứng trong P10 (đề xuất đã ghi ở screen-list.md) | Thêm phần tử View điều hướng của ACT-02 vào package giao diện PKG-05 MemberMobileUI. Chỉ đổi cấu trúc thiết kế nên P10 không chạy lại. Chưa áp dụng |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 9: có 1 dòng Vi phạm còn mở (Nielsen 1) vì lối vào UC-006, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025 chưa có màn hình đích; đây là hệ quả của phạm vi dự án chỉ có đặc tả bốn use case, không phải chỗ đặc tả thiếu, nên không có mã Q. Không có vi phạm WCAG AA chưa xử lý.
- Cách hiển thị và phản hồi khi nhấn lối vào chưa có màn hình đích không được ui-standards.md quy định; màn hình hiển thị đầy đủ như lối vào có đích và không phản hồi, theo UI-STT 44 và cách đã dùng ở SCR-11.
- Màn hình không có thông tin về người đang đăng nhập hay nút đăng xuất vì đặc tả không có (Q-47, Q-99).
