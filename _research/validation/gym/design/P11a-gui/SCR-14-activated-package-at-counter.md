# P11a - SCR-14 Gói tập đã kích hoạt tại quầy - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, Mục 4, BR-01 đến BR-05, BR-38); P07-uc-analysis/UC-005 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); chưa có SCR nào trước lần chạy này nên không có mục h) của SCR khác. Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-102, P11b đã chạy; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-103, Q-104. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-005 (SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14; màn hình điều hướng SCR-02, SCR-10 để lần chạy sau); lần chạy này không phải lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a giai đoạn 1, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-14 (UC-005, ACT-05 Lễ tân, ứng dụng web) |
| Mã Q, ASM cuối đã cấp | Q-104; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-14 Gói tập đã kích hoạt tại quầy (Activated package at counter) |
| UC | UC-005 Mua hoặc gia hạn gói tập |
| Bước UC | 13 |
| Tác nhân | ACT-05 Lễ tân |
| Boundary AC | AC-B-SellPackageUI |
| DC | DC-SellPackageView (đi cùng DC-SellPackageStore) |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-13 (TR-16, mẫu 4, dữ liệu Đơn mua đã thanh toán) |
| Đi tới | SCR-10, SCR-11 và các màn hình khác qua menu trái (mẫu 1, ghi ở node START-ACT-05). Màn hình kết thúc của UC-005 (lễ tân) |

## c) Hình ảnh màn hình

```text
+---------------------------------------------------------------------------------------------------------------------+
| [VietFit]                                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------+
| Trang chủ                  | (v) Gói tập đã được kích hoạt.                                                         |
| > Mua hoặc gia hạn gói tập |                                                                                        |
| Chuyển nhượng gói tập      | Gói tập đã kích hoạt tại quầy                                                          |
| Bán vé tập một ngày        |                                                                                        |
|                            | Gói tập                  6 tháng, Toàn chuỗi                                           |
|                            | Ngày bắt đầu             01/12/2026                                                    |
|                            | Trạng thái gói           Đã kích hoạt                                                  |
+----------------------------+----------------------------------------------------------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit | Trên cùng, cao 56 px, logo trái cách mép 24 px, cao 32 px | UI-STT 11, 12 |
| Menu | Trang chủ, Mua hoặc gia hạn gói tập, Chuyển nhượng gói tập, Bán vé tập một ngày; mục Mua hoặc gia hạn gói tập đang chọn | Trái, rộng 240 px, nền #F4F5F9, mỗi mục cao 44 px | UI-STT 44, 46, 47, 48 |
| Dải thông báo | MSG-13 kèm biểu tượng dấu tích | Đầu vùng nội dung, nền #E8F5EC, viền #1B6E3C, ở lại cho tới khi rời màn hình | UI-STT 22, 25, 57 |
| Tiêu đề màn hình | Gói tập đã kích hoạt tại quầy | Ngay dưới dải thông báo, 24 px Bold | UI-STT 13, 25 |
| Nội dung | Ba dòng thông tin gói tập: nhãn bên trái, giá trị bên phải | Lề 24 px, khoảng cách giữa hai dòng 16 px | UI-STT 11, 25 |
| Hành động | Không có nút hành động | - | UI-STT 25: rời màn hình bằng menu |
| Thông điệp | MSG-13 ở dải thông báo | - | Màn hình kết quả không có hộp thông điệp |

Dữ liệu mẫu nhất quán với SCR-12, SCR-13: gói 6 tháng Toàn chuỗi, ngày bắt đầu 01/12/2026, trạng thái Đã kích hoạt (ví dụ Dữ liệu ra 3 của P04).

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Menu trái | Liên kết | Khởi tạo | Hiển thị các mục theo thứ tự: Trang chủ, Mua hoặc gia hạn gói tập (UC-005), Chuyển nhượng gói tập (UC-007), Bán vé tập một ngày (UC-017); đánh dấu mục Mua hoặc gia hạn gói tập đang chọn | UI-STT 25, 44, 46, 47, 48; P02 bảng 4a |
| 3 | Mục menu Trang chủ | Liên kết | Nhấn | Rời màn hình và mở SCR-10 (mẫu 1). UC-005 đã kết thúc, không có dữ liệu cần giữ | UI-STT 25, 46; screen-transition.md node START-ACT-05 |
| 4 | Mục menu Mua hoặc gia hạn gói tập | Liên kết | Nhấn | Rời màn hình và mở SCR-11 trống để bắt đầu lần bán mới (mẫu 1) | UI-STT 46; screen-transition.md node START-ACT-05 |
| 5 | Mục menu Chuyển nhượng gói tập, Bán vé tập một ngày | Liên kết | Nhấn | Chưa có màn hình đích (UC-007), Chưa có màn hình đích (UC-017); ở lại SCR-14 | UI-STT 44; screen-transition.md node SCR-10 |
| 6 | Dải thông báo thành công | Vùng hiển thị | Khởi tạo | Hiển thị MSG-13 (Gói tập đã được kích hoạt.) ở đầu vùng nội dung, trình đọc màn hình đọc không chuyển tiêu điểm | UC-005 bước 13, Dữ liệu ra 3 STT 3; MSG-13; UI-STT 25, 57 |
| 7 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Gói tập đã kích hoạt tại quầy | UI-STT 13 |
| 8 | Dòng Gói tập | Vùng hiển thị | Khởi tạo | Hiển thị thời hạn và loại của gói tập vừa kích hoạt cho khách | UC-005 bước 13, Dữ liệu ra 3 STT 1 |
| 9 | Dòng Ngày bắt đầu | Vùng hiển thị | Khởi tạo | Hiển thị ngày bắt đầu của gói tập | UC-005 bước 13, Dữ liệu ra 3 STT 2 |
| 10 | Dòng Trạng thái gói | Vùng hiển thị | Khởi tạo | Hiển thị trạng thái của gói sau khi kích hoạt (Đã kích hoạt) | UC-005 bước 13, Dữ liệu ra 3 STT 3 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Gói tập | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Regular 14 px | Dạng "{n} tháng, {loại}"; thời hạn thuộc 1, 3, 6, 12 tháng (BR-01), loại thuộc Một chi nhánh hoặc Toàn chuỗi (BR-02) | Chi nhánh áp dụng của gói loại Một chi nhánh: Q-50 | P04 UC-005 Dữ liệu ra 3 STT 1; BR-01, BR-02 |
| Ngày bắt đầu | 10 | Ngày | Hiển thị; căn phải; chữ #1C1F2A Regular 14 px | Định dạng dd/MM/yyyy | Cùng giá trị đã hiển thị ở SCR-12 | P04 UC-005 Dữ liệu ra 3 STT 2 |
| Trạng thái gói | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Bold 14 px | Sau bước 11 luôn là Đã kích hoạt. Quan hệ với các trạng thái khác của gói: Q-75 | - | P04 UC-005 Dữ liệu ra 3 STT 3; GL-16; Q-75 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình chỉ hiển thị kết quả, không có trường nhập và không có nút hành động | - |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-14 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Dải thông báo thành công MSG-13 và dòng Trạng thái gói Đã kích hoạt cho lễ tân biết kết quả để báo khách ngay khi mở màn hình | - |
| SCR-14 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ ba dòng thông tin của Dữ liệu ra 3 và dải thông báo; không thêm nút hay thông tin ngoài đặc tả | - |
| SCR-14 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Rời màn hình bằng menu về SCR-10 hoặc SCR-11 bất cứ lúc nào | - |
| SCR-14 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Dải thông báo có biểu tượng dấu tích và chữ, không chỉ màu xanh | - |
| SCR-14 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ dải thông báo #1C1F2A trên nền #E8F5EC đo 14,63:1; biểu tượng và viền #1B6E3C trên nền #E8F5EC đo 5,60:1 (cặp màu này nền #E8F5EC chưa được đo ở ui-standards.md, UI-STT 22 chỉ đo #1B6E3C trên trắng) | - |
| SCR-14 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Dải thông báo có vai trò status, được đọc khi mở màn hình mà không chuyển tiêu điểm | - |
| SCR-14 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu cùng thứ tự các mục với SCR-10, SCR-11, SCR-12, SCR-13 (UI-STT 46, 48) | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-13 của ui-standards.md.

## Câu hỏi mở

Không có câu hỏi mới. Câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-75 (quan hệ giữa các trạng thái của gói), Q-50 (chi nhánh áp dụng), Q-54 (hệ thống hoá đơn điện tử không nhận dữ liệu: màn hình kết quả không báo kết cục này vì đặc tả chưa quy định).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 9: không có vi phạm còn mở; các tỉ lệ tương phản tính theo công thức WCAG, nên đo lại bằng công cụ khi có bản thiết kế thật.
- Màn hình hiển thị đúng ba trường của Dữ liệu ra 3; số tiền đã thu, hình thức thu và người mua không hiển thị lại vì đặc tả không có.
- Thứ tự bước 11 (kích hoạt gói) và bước 12 (gửi hoá đơn điện tử) chờ Q-54; màn hình chỉ hiển thị sau bước 13 nên không đổi theo Q-54.
