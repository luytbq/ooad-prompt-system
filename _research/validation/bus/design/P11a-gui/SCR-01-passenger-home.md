# P11a - SCR-01 Trang chủ hành khách - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-002-book-ticket-online.md, UC-008-return-ticket.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-002-book-ticket-online-analysis.md, UC-008-return-ticket-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-01, phục vụ UC-002 (cùng lối vào UC-008) |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-01 Trang chủ hành khách (Passenger home) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-01 Trang chủ hành khách (Passenger home) |
| UC | UC-002 Đặt vé trực tuyến (lối vào); UC-008 Trả vé (lối vào, ngoài phạm vi chạy này). UC-001, UC-007, UC-009, UC-011 chưa có màn hình đích nên chưa có thẻ (quy định STT 35) |
| Bước UC | UC-002 bước 1 (yêu cầu đặt vé) được thực hiện bằng việc chọn thẻ; màn hình không phục vụ bước nào khác |
| Tác nhân | ACT-01 Hành khách |
| Boundary AC | Điều hướng: mở UC-002, UC-008 (không có boundary nguồn theo A2) |
| Lớp thiết kế (DC) | Không có (P10 chưa có View điều hướng, xem Đề xuất sửa artifact trước của screen-list.md) |
| Loại màn hình | Độc lập |
| Đến từ | START-ACT-01 (E-01, mẫu 1, sự kiện mở website) |
| Đi tới | SCR-02 (E-02, mẫu 1, chọn lối vào Đặt vé trực tuyến); SCR-06 (E-07, mẫu 1, chọn lối vào Trả vé) |

## c) Hình ảnh màn hình

Khung dây ở cửa sổ máy tính (từ 1024 px):

```text
+--------------------------------------------------------------------------------------------------------+
| [SaoViet Bus]                                             Đặt vé trực tuyến    Trả vé                  |
|--------------------------------------------------------------------------------------------------------|
| Trang chủ hành khách                                                                                   |
|                                                                                                        |
| +-------------------------------------------+  +-------------------------------------------+           |
| | Đặt vé trực tuyến                         |  | Trả vé                                    |           |
| +-------------------------------------------+  +-------------------------------------------+           |
+--------------------------------------------------------------------------------------------------------+
```

Dưới 600 px: header gồm "SaoViet Bus" và nút "Menu" (cao 48 px); hai thẻ xếp một cột, mỗi thẻ rộng 100% và cao 72 px.

Thông điệp: không có thông điệp hiển thị ở màn hình này. Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Header | Tên hệ thống "SaoViet Bus" (liên kết); menu các use case của ACT-01 đã có màn hình đích: Đặt vé trực tuyến, Trả vé | Trên cùng, cao 56 px; tên bên trái, menu bên phải | STT 8, 9, 35, 36; chưa có mục menu đang chọn vì đang ở trang chủ |
| Tiêu đề màn hình | "Trang chủ hành khách" (tiêu đề cấp 1) | Ngay dưới header | STT 14; tiêu đề tab "Trang chủ hành khách - SaoViet Bus" |
| Thông điệp | Không dùng | Dưới tiêu đề | Không có thông điệp ở màn hình này |
| Nội dung | Hai thẻ lối vào: "Đặt vé trực tuyến", "Trả vé"; mỗi thẻ cao 72 px, chỉ có tên use case | Dưới vùng thông điệp, hai cột từ 1024 px, một cột dưới 1024 px | STT 39; thứ tự theo P02: Đặt vé trực tuyến (UC-002), Trả vé (UC-008) |
| Hành động | Không có nút hành động | - | Màn hình chỉ điều hướng (A2) |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị header, tiêu đề và danh sách thẻ lối vào. Thẻ của use case chưa có đặc tả màn hình (UC-001, UC-007, UC-009, UC-011) chưa hiển thị | Quy định STT 35, 39; ASM-60 |
| 2 | Liên kết "SaoViet Bus" ở header | liên kết | Nhấn | Tải lại SCR-01 | Quy định STT 8, 39 |
| 3 | Mục menu "Đặt vé trực tuyến" | liên kết | Nhấn | Mở SCR-02 theo dịch chuyển E-02 (mẫu 1). Menu cũng có ở mọi màn hình web của ACT-01 (quy định STT 38) | UC-002 bước 1; quy định STT 35, 36 |
| 4 | Mục menu "Trả vé" | liên kết | Nhấn | Mở SCR-06 theo dịch chuyển E-07 (mẫu 1) | UC-008 bước 1; quy định STT 35 |
| 5 | Nút "Menu" (chỉ dưới 600 px) | nút | Nhấn | Mở hoặc đóng danh sách dọc các mục menu, mỗi mục cao 48 px | Quy định STT 36 |
| 6 | Thẻ "Đặt vé trực tuyến" | liên kết | Nhấn | Mở SCR-02 theo dịch chuyển E-02 (mẫu 1); không truyền dữ liệu | UC-002 bước 1 |
| 7 | Thẻ "Trả vé" | liên kết | Nhấn | Mở SCR-06 theo dịch chuyển E-07 (mẫu 1); không truyền dữ liệu | UC-008 bước 1 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Không có | - | - | - | - | Màn hình điều hướng không có trường nhập hay trường hiển thị dữ liệu nghiệp vụ; tên thẻ là nhãn cố định | Quy định STT 39 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có | - | Màn hình không có trường nhập | - |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-01 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 44, 45, 46: chỉ báo bận từ 1 giây, thông điệp trạng thái trong vùng thông điệp (MSG-01) | Không có |
| SCR-01 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng hiển thị theo P04 mục 5, thuật ngữ theo P05 | Không có |
| SCR-01 | Nielsen: 3 Người dùng kiểm soát và tự do | Đạt | STT 36, 39, 65: mọi thẻ và mục menu dẫn đi tiếp; Quay lại của trình duyệt dùng được | Không có |
| SCR-01 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 11, 12, 35, 38: vị trí nút, tên nút, menu giống các màn hình web khác | Không có |
| SCR-01 | Nielsen: 5 Ngăn lỗi | Đạt | Màn hình chỉ chọn lối vào, không có dữ liệu nhập để sinh lỗi | Không có |
| SCR-01 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | STT 35, 39: thẻ nêu tên use case bằng thuật ngữ P02, hành khách nhận ra thay vì nhớ | Không có |
| SCR-01 | Nielsen: 7 Linh hoạt và hiệu quả | Đạt | STT 36, 39: lối vào có cả ở menu header và thẻ | Không có |
| SCR-01 | Nielsen: 8 Thẩm mỹ và tối giản | Đạt | STT 39: thẻ chỉ có tên use case | Không có |
| SCR-01 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Không áp dụng | Không có thao tác sinh lỗi ở màn hình này | Không có |
| SCR-01 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 53, 54: chỉ có gợi ý tại trường; chưa có trang trợ giúp vì nguồn không có tài liệu hướng dẫn | Q-86 (đã mở ở ui-standards.md) |
| SCR-01 | Shneiderman: Nhất quán | Đạt | STT 9, 10, 11, 38 áp dụng nguyên văn | Không có |
| SCR-01 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60: tương phản, nhãn, bàn phím, phóng chữ | Không có |
| SCR-01 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46: mọi thao tác gửi hệ thống đều có phản hồi trạng thái hoặc kết quả | Không có |
| SCR-01 | Shneiderman: Hội thoại có điểm kết thúc rõ | Không áp dụng | Màn hình điều hướng, không kết thúc hội thoại | Không có |
| SCR-01 | Shneiderman: Ngăn lỗi | Không áp dụng | Không có dữ liệu nhập | Không có |
| SCR-01 | Shneiderman: Hoàn tác dễ dàng | Không áp dụng | Không có thao tác thay đổi dữ liệu | Không có |
| SCR-01 | Shneiderman: Người dùng làm chủ | Đạt | STT 39, 65: người dùng chọn use case và quay lại bằng trình duyệt | Không có |
| SCR-01 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | STT 35: chỉ hiển thị lối vào, không bắt nhớ mã hay tên màn hình | Không có |
| SCR-01 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58: màn hình không có hình mang nghĩa | Không có |
| SCR-01 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 28, 57: bảng có chú thích và tiêu đề cột, nhóm trường có tiêu đề nhóm, tiêu đề cấp 1 duy nhất | Không có |
| SCR-01 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19, 37: thẻ phân biệt bằng chữ, không dựa vào màu | Không có |
| SCR-01 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 55: mọi cặp màu từ 5,53:1 | Không có |
| SCR-01 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 7, 60: đơn vị rem, chiều cao hộp chứa chữ không cố định | Xác minh trên trang thật khi có bản dựng |
| SCR-01 | WCAG 1.4.10 Reflow | Đạt | STT 1, 5, 60: một cột dưới 1024 px, bảng chuyển thành thẻ dưới 600 px | Không có |
| SCR-01 | WCAG 1.4.11 Tương phản thành phần 3:1 | Đạt | STT 56: viền điều khiển #767676 (4,54:1), viền tiêu điểm 8,66:1 | Không có |
| SCR-01 | WCAG 2.1.1 Bàn phím | Đạt | STT 41 đến 43, 59: mọi điều khiển dùng được bằng bàn phím | Không có |
| SCR-01 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33: thứ tự Tab trùng thứ tự đọc, không dùng tabindex dương | Không có |
| SCR-01 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề cấp 1, nút có tên bằng chữ | Không có |
| SCR-01 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Đạt | STT 34: viền tiêu điểm 3 px #1F4E79, không tắt | Không có |
| SCR-01 | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | STT 9: header và vùng hành động không cố định khi cuộn | Không có |
| SCR-01 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 59: không thao tác nào cần kéo thả | Không có |
| SCR-01 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | STT 30: vùng bấm 44 x 44 px (48 px trên điện thoại) | Không có |
| SCR-01 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 9, 36, 38, 39: header, menu, vị trí điều hướng giống nhau ở mọi màn hình web của ACT-01 | Không có |
| SCR-01 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng một chức năng dùng cùng tên nút và thuật ngữ | Không có |
| SCR-01 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp lặp lại ở nhiều màn hình | Q-86 |
| SCR-01 | WCAG 3.3.1 Nhận biết lỗi | Không áp dụng | Không có trường nhập hoặc thao tác sinh lỗi | Không có |
| SCR-01 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Không áp dụng | Không có trường nhập | Không có |
| SCR-01 | WCAG 3.3.3 Gợi ý sửa lỗi | Không áp dụng | Không có thông điệp lỗi | Không có |
| SCR-01 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Không áp dụng | Màn hình không thực hiện thao tác pháp lý hoặc tài chính | Không có |
| SCR-01 | WCAG 3.3.7 Không bắt nhập lại | Không áp dụng | Không có trường nhập | Không có |
| SCR-01 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-01 | WCAG 4.1.3 Thông điệp trạng thái | Không áp dụng | Không có thông điệp trạng thái ở màn hình này | Không có |
| SCR-01 | Nền tảng: Material Design (mức nhấn mạnh nút, một hành động chính) | Đạt | STT 11, 20, 21: một nút chính, nút phụ dạng viền | Không có |
| SCR-01 | Nền tảng: Apple HIG (vùng chạm 44 pt, điều hướng quay lại theo nền tảng) | Đạt | STT 20, 30, 65: nút cao 44 px (điện thoại 48 px), Quay lại theo trình duyệt | Không có |
| SCR-01 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-01 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-01 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-01 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-01 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-01 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-01 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3, F4 | Màn hình điều hướng SCR-01 chưa có phần tử View ở P10 (đã nêu ở screen-list.md) | Như đề nghị đã ghi ở screen-list.md; không phát sinh đề nghị mới |

## Vấn đề còn mở

- Màn hình điều hướng chỉ có thẻ cho UC-002 và UC-008; thẻ của UC-001, UC-007, UC-009, UC-011 thêm khi các use case đó có P04 và đặc tả màn hình (STT 35). Cần chạy lại SCR-01 khi đó.
- Mục menu của header dẫn tới màn hình đầu của use case từ mọi màn hình web của ACT-01 được xem là điều hướng chung như liên kết tên hệ thống (STT 39), không vẽ cạnh dịch chuyển từ mọi màn hình; tiêu chí Nielsen #10 còn mở theo Q-86.
