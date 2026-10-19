# P11a - SCR-05 Gói tập đã kích hoạt - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, Mục 4, BR-01 đến BR-05, BR-38); P07-uc-analysis/UC-005 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); chưa có SCR nào trước lần chạy này nên không có mục h) của SCR khác. Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-102, P11b đã chạy; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-103, Q-104. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-005 (SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14; màn hình điều hướng SCR-02, SCR-10 để lần chạy sau); lần chạy này không phải lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a giai đoạn 1, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-05 (UC-005, ACT-02 Hội viên, ứng dụng di động) |
| Mã Q, ASM cuối đã cấp | Q-104; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-05 Gói tập đã kích hoạt (Activated membership package) |
| UC | UC-005 Mua hoặc gia hạn gói tập |
| Bước UC | 13 |
| Tác nhân | ACT-02 Hội viên |
| Boundary AC | AC-B-PurchaseOrRenewPackageUI |
| DC | DC-PurchaseOrRenewPackageView (đi cùng DC-PurchaseOrRenewPackageStore) |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-04 (TR-06, mẫu 4, dữ liệu Đơn mua đã thanh toán) |
| Đi tới | SCR-02 (nút Trang chủ và nút quay lại của hệ thống, mẫu 1, ghi ở node START-ACT-02). Màn hình kết thúc của UC-005 (hội viên) |

## c) Hình ảnh màn hình

```text
+--------------------------------------+
| [VietFit]                  [Trang chủ]|
|--------------------------------------|
| (v) Gói tập đã được kích hoạt.       |
|                                      |
| Gói tập đã kích hoạt                 |
|                                      |
| Gói tập        6 tháng, Toàn chuỗi   |
| Ngày bắt đầu              01/12/2026 |
| Trạng thái gói          Đã kích hoạt |
+--------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit, nút Trang chủ | Trên cùng, cao 56 dp, logo trái, Trang chủ phải | UI-STT 10, 12, 45 |
| Dải thông báo | MSG-13 kèm biểu tượng dấu tích | Đầu vùng nội dung, nền #E8F5EC, viền #1B6E3C, ở lại cho tới khi rời màn hình | UI-STT 22, 25, 57 |
| Tiêu đề màn hình | Gói tập đã kích hoạt | Ngay dưới dải thông báo, 20 sp Bold | UI-STT 13, 25 |
| Nội dung | Ba dòng thông tin gói tập: nhãn bên trái, giá trị bên phải | Lề 16 dp, khoảng cách giữa hai dòng 16 dp | UI-STT 10, 25 |
| Hành động | Không có nút hành động | - | UI-STT 25: rời màn hình bằng nút Trang chủ |
| Thông điệp | MSG-13 ở dải thông báo | - | Màn hình kết quả không có hộp thông điệp |

Dữ liệu mẫu nhất quán với SCR-04: gói 6 tháng Toàn chuỗi, ngày bắt đầu 01/12/2026, trạng thái Đã kích hoạt (ví dụ Dữ liệu ra 3 của P04).

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Nút Trang chủ | Nút | Nhấn | Rời màn hình và mở SCR-02 (mẫu 1). UC-005 đã kết thúc, không có dữ liệu cần giữ | UI-STT 25, 45; screen-transition.md node START-ACT-02 |
| 3 | Nút quay lại của hệ thống (Android) hoặc cử chỉ quay lại (iOS) | Nút | Nhấn | Mở SCR-02; không đưa về SCR-04 vì dữ liệu đã được ghi | UI-STT 15 |
| 4 | Dải thông báo thành công | Vùng hiển thị | Khởi tạo | Hiển thị MSG-13 (Gói tập đã được kích hoạt.) ở đầu vùng nội dung, trình đọc màn hình đọc không chuyển tiêu điểm | UC-005 bước 13, Dữ liệu ra 3 STT 3; MSG-13; UI-STT 25, 57 |
| 5 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Gói tập đã kích hoạt | UI-STT 13 |
| 6 | Dòng Gói tập | Vùng hiển thị | Khởi tạo | Hiển thị thời hạn và loại của gói tập vừa kích hoạt | UC-005 bước 13, Dữ liệu ra 3 STT 1 |
| 7 | Dòng Ngày bắt đầu | Vùng hiển thị | Khởi tạo | Hiển thị ngày bắt đầu của gói tập | UC-005 bước 13, Dữ liệu ra 3 STT 2 |
| 8 | Dòng Trạng thái gói | Vùng hiển thị | Khởi tạo | Hiển thị trạng thái của gói sau khi kích hoạt (Đã kích hoạt) | UC-005 bước 13, Dữ liệu ra 3 STT 3 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Gói tập | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Regular 16 sp | Dạng "{n} tháng, {loại}"; thời hạn thuộc 1, 3, 6, 12 tháng (BR-01), loại thuộc Một chi nhánh hoặc Toàn chuỗi (BR-02) | Chi nhánh áp dụng của gói loại Một chi nhánh: Q-50 | P04 UC-005 Dữ liệu ra 3 STT 1; BR-01, BR-02 |
| Ngày bắt đầu | 10 | Ngày | Hiển thị; căn phải; chữ #1C1F2A Regular 16 sp | Định dạng dd/MM/yyyy | Cùng giá trị đã hiển thị ở SCR-04 | P04 UC-005 Dữ liệu ra 3 STT 2 |
| Trạng thái gói | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Bold 16 sp | Sau bước 11 luôn là Đã kích hoạt. Quan hệ với các trạng thái khác của gói (còn hiệu lực, đang bảo lưu, sắp hết hạn): Q-75 | - | P04 UC-005 Dữ liệu ra 3 STT 3; GL-16; Q-75 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình chỉ hiển thị kết quả, không có trường nhập và không có nút hành động | - |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-05 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Dải thông báo thành công MSG-13 và dòng Trạng thái gói Đã kích hoạt cho biết kết quả ngay khi mở màn hình | - |
| SCR-05 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ ba dòng thông tin của Dữ liệu ra 3 và dải thông báo; không thêm nút hay thông tin ngoài đặc tả | - |
| SCR-05 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Rời màn hình bằng nút Trang chủ hoặc nút quay lại của hệ thống, đều về SCR-02 | - |
| SCR-05 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Dải thông báo có biểu tượng dấu tích và chữ, không chỉ màu xanh | - |
| SCR-05 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Dải thông báo có vai trò status, được đọc khi mở màn hình mà không chuyển tiêu điểm | - |
| SCR-05 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ dải thông báo #1C1F2A trên nền #E8F5EC đo 14,63:1; biểu tượng và viền #1B6E3C trên nền #E8F5EC đo 5,60:1 (cặp màu này nền #E8F5EC chưa được đo ở ui-standards.md, UI-STT 22 chỉ đo #1B6E3C trên trắng) | - |
| SCR-05 | Material Design (Android): một hành động chính | Không áp dụng | Màn hình kết quả không có nút hành động theo UI-STT 25 | - |
| SCR-05 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Cử chỉ quay lại về SCR-02, không về màn hình xác nhận đã ghi dữ liệu | - |

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

- Target 9: không có vi phạm còn mở; WCAG 1.4.3 của dải thông báo tính theo công thức WCAG, nên đo lại bằng công cụ khi có bản thiết kế thật.
- Màn hình hiển thị đúng ba trường của Dữ liệu ra 3; số tiền đã thanh toán và mã đơn không hiển thị vì đặc tả không có.
- Thứ tự bước 11 (kích hoạt gói) và bước 12 (gửi hoá đơn điện tử) chờ Q-54; màn hình chỉ hiển thị sau bước 13 nên không đổi theo Q-54.
