# P11a - SCR-08 Vị trí trong danh sách chờ - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-010 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, BR-06 đến BR-12); P07-uc-analysis/UC-010 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); mục h) của SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14 (đều ghi Không có thông điệp mới). Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-104; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-105. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-010 và các màn hình điều hướng (SCR-01, SCR-02, SCR-06, SCR-07, SCR-08, SCR-09, SCR-10, SCR-15, SCR-16); đây là lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Có. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-08 (UC-010, ACT-02 Hội viên, ứng dụng di động) |
| Mã Q, ASM cuối đã cấp | Q-105; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-08 Vị trí trong danh sách chờ (Waitlist position) |
| UC | UC-010 Đặt chỗ lớp nhóm |
| Bước UC | 7a4 (bước 7a3 do máy chủ thêm hội viên vào danh sách chờ trước khi mở màn hình) |
| Tác nhân | ACT-02 Hội viên |
| Boundary AC | AC-B-BookClassSpotUI |
| DC | DC-BookClassSpotView (đi cùng DC-BookClassSpotStore) |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-06 (TR-09, mẫu 4, dữ liệu Lớp nhóm đã chọn, qua nút Vào danh sách chờ của hộp MSG-09) |
| Đi tới | SCR-02 (nút Trang chủ và nút quay lại của hệ thống, mẫu 1, ghi ở node START-ACT-02). Màn hình kết thúc của UC-010 (vào danh sách chờ) |

## c) Hình ảnh màn hình

Mockup HTML: mockups/SCR-08-waitlist-position.html.

```text
+--------------------------------------+
| [VietFit]                [Trang chủ] |
|--------------------------------------|
| (v) Bạn đã vào danh sách chờ của     |
|     lớp này.                         |
|                                      |
| Vị trí trong danh sách chờ           |
|                                      |
| Loại lớp            Đạp xe trong nhà |
| Giờ học             27/10/2026 06:30 |
| Vị trí trong danh sách chờ         3 |
|                                      |
+--------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit, nút Trang chủ | Trên cùng, cao 56 dp, logo trái, Trang chủ phải | UI-STT 10, 12, 45 |
| Dải thông báo | MSG-15 kèm biểu tượng dấu tích | Đầu vùng nội dung, nền #E8F5EC, viền #1B6E3C, ở lại cho tới khi rời màn hình | UI-STT 22, 25, 57 |
| Tiêu đề màn hình | Vị trí trong danh sách chờ | Ngay dưới dải thông báo, 20 sp Bold | UI-STT 13, 25 |
| Nội dung | Ba dòng thông tin: nhãn bên trái, giá trị bên phải | Lề 16 dp, khoảng cách giữa hai dòng 16 dp | UI-STT 10, 25 |
| Hành động | Không có nút hành động | - | UI-STT 25: rời màn hình bằng nút Trang chủ |
| Thông điệp | MSG-15 ở dải thông báo | - | Màn hình kết quả không có hộp thông điệp |

Dữ liệu mẫu nhất quán với SCR-06: lớp Đạp xe trong nhà, 27/10/2026 06:30 là lớp đã đủ chỗ trong hộp MSG-09; vị trí 3 theo ví dụ Dữ liệu ra 3 của P04.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Nút Trang chủ | Nút | Nhấn | Rời màn hình và mở SCR-02 (mẫu 1). UC-010 đã kết thúc, không có dữ liệu cần giữ | UI-STT 25, 45; screen-transition.md node START-ACT-02 |
| 3 | Nút quay lại của hệ thống (Android) hoặc cử chỉ quay lại (iOS) | Nút | Nhấn | Mở SCR-02; không đưa về SCR-06 vì hội viên đã được thêm vào danh sách chờ | UI-STT 15 |
| 4 | Dải thông báo thành công | Vùng hiển thị | Khởi tạo | Hiển thị MSG-15 (Bạn đã vào danh sách chờ của lớp này.) ở đầu vùng nội dung, trình đọc màn hình đọc không chuyển tiêu điểm | UC-010 luồng 7a4; MSG-15; UI-STT 25, 57 |
| 5 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Vị trí trong danh sách chờ | UI-STT 13 |
| 6 | Dòng Loại lớp | Vùng hiển thị | Khởi tạo | Hiển thị loại của lớp nhóm đã đủ chỗ | UC-010 luồng 7a4, Dữ liệu ra 3 STT 1 |
| 7 | Dòng Giờ học | Vùng hiển thị | Khởi tạo | Hiển thị ngày và giờ bắt đầu của lớp | UC-010 luồng 7a4, Dữ liệu ra 3 STT 2 |
| 8 | Dòng Vị trí trong danh sách chờ | Vùng hiển thị | Khởi tạo | Hiển thị thứ tự của hội viên trong danh sách chờ của lớp, 1 là đứng đầu; cách xếp thứ tự chờ: Q-61 | UC-010 luồng 7a4, Dữ liệu ra 3 STT 3; Q-61 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Loại lớp | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Regular 16 sp | Văn bản; giá trị nguồn nêu: yoga, aerobic, đạp xe trong nhà (GL-27) | Cùng giá trị đã hiển thị ở SCR-06 | P04 UC-010 Dữ liệu ra 3 STT 1; GL-27 |
| Giờ học | 16 | Ngày, Giờ | Hiển thị; căn phải; chữ #1C1F2A Bold 16 sp | Định dạng dd/MM/yyyy HH:mm, giờ 24 (UI-STT 18) | Thiết kế: 16 là độ dài của định dạng hiển thị. Cùng giá trị đã hiển thị ở SCR-06 | P04 UC-010 Dữ liệu ra 3 STT 2; GL-13; UI-STT 18 |
| Vị trí trong danh sách chờ | - | Số | Hiển thị; căn phải; chữ #1C1F2A Bold 16 sp | Số nguyên dương, 1 là đứng đầu (UI-STT 20). Quy tắc xếp thứ tự: Q-61 | Độ dài theo giá trị, không có giá trị tối đa nguồn nêu | P04 UC-010 Dữ liệu ra 3 STT 3; GL-08; Q-61 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình chỉ hiển thị kết quả, không có trường nhập và không có nút hành động | - |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-08 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Dải thông báo thành công MSG-15 và ba dòng thông tin (lớp, giờ học, vị trí) cho biết hội viên đã vào danh sách chờ và đang đứng thứ mấy | - |
| SCR-08 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ ba dòng thông tin của Dữ liệu ra 3 và dải thông báo; không thêm nút hay thông tin ngoài đặc tả | - |
| SCR-08 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Rời màn hình bằng nút Trang chủ hoặc nút quay lại của hệ thống, đều về SCR-02. Muốn rút khỏi danh sách chờ thì dùng chức năng huỷ của use case khác nếu có; màn hình không thêm nút vì đặc tả UC-010 không có (UI-STT 77) | - |
| SCR-08 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Dải thông báo có biểu tượng dấu tích và chữ, không chỉ màu xanh | - |
| SCR-08 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Cùng cặp màu dải thông báo đã đo ở SCR-07: chữ #1C1F2A trên nền #E8F5EC 14,63:1; biểu tượng và viền #1B6E3C trên nền #E8F5EC 5,60:1 | - |
| SCR-08 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Dải thông báo có vai trò status, được đọc khi mở màn hình mà không chuyển tiêu điểm | - |
| SCR-08 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Cử chỉ quay lại về SCR-02, không về SCR-06 vì hội viên đã vào danh sách chờ | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-15 của ui-standards.md.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-61 (thứ tự xếp chờ), Q-62 (tự vào hay chọn vào danh sách chờ), Q-23 (vị trí chờ của hội viên không xác nhận nhận chỗ), Q-20 (vị trí chờ của hội viên bị khoá quyền đặt lớp), Q-73 (giờ học và giờ bắt đầu).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 9: không có vi phạm còn mở; các tỉ lệ tương phản dùng lại cặp màu đã đo ở SCR-07, nên đo lại bằng công cụ khi có bản thiết kế thật.
- Màn hình hiển thị đúng ba trường của Dữ liệu ra 3; phòng, huấn luyện viên, tổng số người chờ và hạn xác nhận nhận chỗ không hiển thị vì đặc tả không có.
- Hội viên đã vào danh sách chờ thì không thấy lại vị trí này ở màn hình nào khác trong phạm vi hiện có; use case xem hoặc huỷ vị trí chờ chưa có đặc tả.
