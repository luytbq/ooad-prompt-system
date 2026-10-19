# P11a - SCR-12 Xác nhận đơn bán tại quầy - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, Mục 4, BR-01 đến BR-05, BR-38); P07-uc-analysis/UC-005 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); chưa có SCR nào trước lần chạy này nên không có mục h) của SCR khác. Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-102, P11b đã chạy; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-103, Q-104. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-005 (SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14; màn hình điều hướng SCR-02, SCR-10 để lần chạy sau); lần chạy này không phải lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a giai đoạn 1, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-12 (UC-005, ACT-05 Lễ tân, ứng dụng web) |
| Mã Q, ASM cuối đã cấp | Q-104; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-12 Xác nhận đơn bán tại quầy (Confirm counter sale order) |
| UC | UC-005 Mua hoặc gia hạn gói tập |
| Bước UC | 6-7 (bước 8 tạo đơn chờ thanh toán do máy chủ xử lý sau khi nhấn Xác nhận bán) |
| Tác nhân | ACT-05 Lễ tân |
| Boundary AC | AC-B-SellPackageUI |
| DC | DC-SellPackageView (đi cùng DC-SellPackageStore) |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-11 (TR-13, mẫu 4, dữ liệu Gói tập và người mua đã chọn) |
| Đi tới | SCR-13 (TR-15, mẫu 4, dữ liệu Đơn mua chờ thu tiền); SCR-11 (TR-14, mẫu 1: nút Quay lại); SCR-10 và các màn hình khác qua menu trái (mẫu 1, ghi ở node START-ACT-05) |

## c) Hình ảnh màn hình

```text
+---------------------------------------------------------------------------------------------------------------------+
| [VietFit]                                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------+
| Trang chủ                  | Xác nhận đơn bán tại quầy                                                              |
| > Mua hoặc gia hạn gói tập |                                                                                        |
| Chuyển nhượng gói tập      | Gói tập                  6 tháng, Toàn chuỗi                                           |
| Bán vé tập một ngày        | Người mua gói            Nguyễn Văn An                                                 |
|                            | Ngày bắt đầu             01/12/2026                                                    |
|                            | Số tiền phải trả         1.080.000 đ                                                   |
|                            |                                                                                        |
|                            |                                                                                        |
|                            |                                         [ Quay lại ]  [ Xác nhận bán ]                 |
+----------------------------+----------------------------------------------------------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit | Trên cùng, cao 56 px, logo trái cách mép 24 px, cao 32 px | UI-STT 11, 12 |
| Menu | Trang chủ, Mua hoặc gia hạn gói tập, Chuyển nhượng gói tập, Bán vé tập một ngày; mục Mua hoặc gia hạn gói tập đang chọn | Trái, rộng 240 px, nền #F4F5F9, mỗi mục cao 44 px | UI-STT 44, 46, 47, 48 |
| Dải thông báo | Không dùng ở màn hình này | - | - |
| Tiêu đề màn hình | Xác nhận đơn bán tại quầy | Đầu vùng nội dung, 24 px Bold | UI-STT 13 |
| Nội dung | Bốn dòng tóm tắt: nhãn bên trái, giá trị bên phải | Lề 24 px, khoảng cách giữa hai dòng 16 px | UI-STT 11, 76 |
| Hành động | Nút phụ Quay lại bên trái, nút chính Xác nhận bán bên phải | Cuối nội dung, canh phải, cao 44 px, cách nhau 12 px | UI-STT 14, 26, 27 |
| Thông điệp | Hộp MSG-10, MSG-11, MSG-12 là lớp phủ modal rộng 480 px | - | UI-STT 54 |

Dữ liệu mẫu nhất quán với SCR-11: gói 6 tháng Toàn chuỗi (giá 1.200.000 đ), người mua Nguyễn Văn An, ngày bắt đầu 01/12/2026, số tiền phải trả 1.080.000 đ theo ví dụ Dữ liệu ra 2 của P04 (giá gói trừ khuyến mãi 10%, trong giới hạn 20% của BR-38).

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Menu trái | Liên kết | Khởi tạo | Hiển thị các mục theo thứ tự: Trang chủ, Mua hoặc gia hạn gói tập (UC-005), Chuyển nhượng gói tập (UC-007), Bán vé tập một ngày (UC-017); đánh dấu mục Mua hoặc gia hạn gói tập đang chọn | UI-STT 44, 46, 47, 48; P02 bảng 4a |
| 3 | Mục menu Trang chủ | Liên kết | Nhấn | Rời màn hình, bỏ dữ liệu đã chọn (đơn chưa tạo), mở SCR-10 (mẫu 1) | UI-STT 46; screen-transition.md node START-ACT-05 |
| 4 | Mục menu Mua hoặc gia hạn gói tập | Liên kết | Nhấn | Rời màn hình, bỏ dữ liệu đã chọn (đơn chưa tạo), mở SCR-11 trống để bắt đầu lần bán mới (mẫu 1) | UI-STT 46; screen-transition.md node START-ACT-05 |
| 5 | Mục menu Chuyển nhượng gói tập, Bán vé tập một ngày | Liên kết | Nhấn | Chưa có màn hình đích (UC-007), Chưa có màn hình đích (UC-017); ở lại SCR-12 | UI-STT 44; screen-transition.md node SCR-10 |
| 6 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Xác nhận đơn bán tại quầy | UI-STT 13 |
| 7 | Dòng Gói tập | Vùng hiển thị | Khởi tạo | Hiển thị thời hạn và loại của gói đã chọn ở SCR-11 | UC-005 bước 6, Dữ liệu ra 2 STT 1 |
| 8 | Dòng Người mua gói | Vùng hiển thị | Khởi tạo | Hiển thị lại người mua đã nhập ở SCR-11 để lễ tân kiểm tra trước khi tạo đơn | UC-005 Dữ liệu vào 1 STT 5; UI-STT 76; Q-01, Q-104 |
| 9 | Dòng Ngày bắt đầu | Vùng hiển thị | Khởi tạo | Hiển thị ngày bắt đầu của gói mới do máy chủ xác định ở bước 4 (BR-03). Ngày bắt đầu khi mua gói mới, gia hạn gói đã hết hạn, gia hạn gói đang bảo lưu: chưa quy định (Q-51, Q-24, Q-52) | UC-005 bước 4, 6, Dữ liệu ra 2 STT 2; BR-03; Q-51, Q-24, Q-52 |
| 10 | Dòng Số tiền phải trả | Vùng hiển thị | Khởi tạo | Hiển thị số tiền phải trả do máy chủ tính ở bước 5 (giá gói trừ mức giảm khuyến mãi áp dụng, cách áp dụng: Q-09) | UC-005 bước 5, 6, Dữ liệu ra 2 STT 3; GL-37; Q-09 |
| 11 | Nút Xác nhận bán | Nút chính | Nhấn | Nhãn chuyển thành Đang xử lý và khoá nhấn lại (UI-STT 41); từ giây thứ 1 hiển thị MSG-10. Máy chủ tạo đơn mua ở trạng thái chờ thanh toán (bước 8) rồi mở SCR-13 với Đơn mua chờ thu tiền (TR-15, mẫu 4). Sự cố hệ thống thì hiển thị MSG-11, mất kết nối thì MSG-12, ở lại SCR-12 | UC-005 bước 7, 8; TR-15; UI-STT 41, 56; MSG-10, MSG-11, MSG-12 |
| 12 | Nút Quay lại | Nút phụ | Nhấn | Mở SCR-11 và giữ gói và người mua đã chọn (TR-14, mẫu 1). Chỉ có khi đơn chưa tạo | UC-005 bước 7; UI-STT 15, 62; TR-14 |
| 13 | Hộp MSG-11, MSG-12: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-12, giữ nguyên dữ liệu đã chọn | UI-STT 60, 62; MSG-11, MSG-12 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Gói tập | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Regular 14 px | Dạng "{n} tháng, {loại}"; thời hạn thuộc 1, 3, 6, 12 tháng (BR-01), loại thuộc Một chi nhánh hoặc Toàn chuỗi (BR-02) | Gói loại Một chi nhánh thêm tên chi nhánh áp dụng trong ngoặc (UI-STT 76; nguồn chi nhánh: Q-50) | P04 UC-005 Dữ liệu ra 2 STT 1; BR-01, BR-02; UI-STT 76 |
| Người mua gói | Chưa quy định (Q-104) | Chữ | Hiển thị; căn phải; chữ #1C1F2A Regular 14 px | Giá trị đã nhập ở SCR-11; định dạng chưa quy định (Q-104) | Không thuộc Dữ liệu ra 2; hiển thị lại Dữ liệu vào 1 STT 5 theo UI-STT 76 | P04 UC-005 Dữ liệu vào 1 STT 5; UI-STT 76 |
| Ngày bắt đầu | 10 | Ngày | Hiển thị; căn phải; chữ #1C1F2A Regular 14 px | Định dạng dd/MM/yyyy. Gia hạn khi gói cũ còn hiệu lực: ngay sau ngày hết hạn của gói cũ (BR-03); các nhánh khác chưa quy định (Q-51, Q-24, Q-52) | - | P04 UC-005 Dữ liệu ra 2 STT 2; BR-03 |
| Số tiền phải trả | 13 | Tiền | Hiển thị; căn phải; chữ #1C1F2A Bold 14 px | Số nguyên đồng, phân cách hàng nghìn bằng dấu chấm, kèm dấu cách và chữ đ | Thiết kế: 13 là độ rộng vùng hiển thị tiền (999.999.999 đ), không phải miền giá trị. Số tiền = giá gói trừ mức giảm khuyến mãi (GL-37), cách áp dụng chờ Q-09 | P04 UC-005 Dữ liệu ra 2 STT 3; GL-37; UI-STT 19 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình chỉ hiển thị tóm tắt đơn mua và hai nút; dữ liệu đã được kiểm tra ở SCR-11. Quy tắc nghiệp vụ liên quan đơn mua do máy chủ kiểm tra khi nhấn Xác nhận bán | Sự cố hệ thống MSG-11; mất kết nối MSG-12 |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-12 | Nielsen 5 Ngăn lỗi | Đạt | Màn hình xác nhận riêng cho dữ liệu tài chính (UI-STT 74): tóm tắt, nút Quay lại sửa, nút Xác nhận bán; nút khoá nhấn lại khi đang xử lý để không tạo hai đơn cho một lần bán | - |
| SCR-12 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Nút Quay lại về SCR-11 giữ nguyên dữ liệu khi đơn chưa tạo; menu cho phép rời bất cứ lúc nào | - |
| SCR-12 | Nielsen 1 Hiển thị trạng thái hệ thống (tóm tắt đơn) | Vi phạm còn mở | Giá gói ở SCR-11 là 1.200.000 đ còn số tiền phải trả là 1.080.000 đ; Dữ liệu ra 2 không có mức giảm khuyến mãi nên chênh lệch không được giải thích trên màn hình | Q-09; đề xuất sửa P04 Dữ liệu ra 2 đã ghi ở SCR-04; không tự thêm trường |
| SCR-12 | Baymard: hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Đạt | Bốn dòng tóm tắt gồm gói tập, người mua gói, ngày bắt đầu, số tiền phải trả, kèm nút Quay lại sửa | - |
| SCR-12 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Có tóm tắt để kiểm tra, sửa được bằng Quay lại, xác nhận bằng nút đặt tên theo hành động Xác nhận bán (UI-STT 75) | - |
| SCR-12 | WCAG 3.3.7 Không bắt nhập lại | Đạt | Gói và người mua đã chọn ở SCR-11 được chuyển sang và được giữ khi dùng Quay lại | - |
| SCR-12 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Thứ tự Tab: logo, menu, nút Quay lại rồi nút Xác nhận bán (nút phụ rồi nút chính, UI-STT 42) | - |
| SCR-12 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu cùng thứ tự các mục với SCR-10, SCR-11, SCR-13, SCR-14 (UI-STT 46, 48) | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-10, MSG-11, MSG-12 của ui-standards.md.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-01, Q-104 (người mua gói), Q-09 (cách áp dụng khuyến mãi), Q-50 (chi nhánh áp dụng), Q-51, Q-24, Q-52 (ngày bắt đầu các nhánh), Q-25 (15 phút có áp dụng cho đơn bán tại quầy không), Q-47 (xác thực của lễ tân).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Không có. Đề xuất sửa P04 UC-005 Dữ liệu ra 2 (mức giảm khuyến mãi, Người mua gói) đã ghi ở SCR-04 và áp dụng cả cho SCR-12.

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 3: dòng Người mua gói không thuộc Dữ liệu ra 2 mà là hiển thị lại Dữ liệu vào 1 STT 5 theo UI-STT 76 để lễ tân kiểm tra đơn tài chính; truy được về Dữ liệu vào và quy định chuẩn, cần người dùng xác nhận khi Q-01, Q-104 có trả lời.
- Target 9: 1 dòng Vi phạm còn mở (Nielsen 1 gắn Q-09) do đặc tả chưa quy định; không có vi phạm WCAG AA chưa xử lý.
- Đơn bán tại quầy có chịu thời hạn 15 phút của BR-04 hay không chờ Q-25; màn hình này không hiển thị thời hạn.
- Nút Xác nhận bán tạo đơn rồi chuyển sang SCR-13 thu tiền; nếu Q-98 trả lời lễ tân cũng bán qua cổng thanh toán thì cần thêm đích sau Xác nhận bán (chưa thiết kế).
