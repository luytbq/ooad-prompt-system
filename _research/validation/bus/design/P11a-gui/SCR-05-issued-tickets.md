# P11a - SCR-05 Vé đã phát hành - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-002-book-ticket-online.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-05, UC-002 |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-05 Vé đã phát hành (Issued tickets) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-05 Vé đã phát hành (Issued tickets) |
| UC | UC-002 Đặt vé trực tuyến (Book Ticket Online) |
| Bước UC | 11-13 (hiển thị kết quả của bước 13; phát hành vé bước 11 và gửi SMS bước 12 do hệ thống thực hiện) |
| Tác nhân | ACT-01 Hành khách |
| Boundary AC | AC-B-BookTicketForm (showIssuedTickets) |
| Lớp thiết kế (DC) | DC-BookTicketView, DC-BookTicketStore |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-04 (E-05, mẫu 4, dữ liệu "Vé đã phát hành") |
| Đi tới | Không có (màn hình kết thúc của UC-002); người dùng rời màn hình bằng tên hệ thống ở header về SCR-01 (STT 39) hoặc menu |

## c) Hình ảnh màn hình

Khung dây ở cửa sổ máy tính (từ 1024 px). Dữ liệu mẫu theo P04 UC-002 mục 5 (Dữ liệu ra 4).

```text
+--------------------------------------------------------------------------------------------------+
| [SaoViet Bus]                                             Đặt vé trực tuyến    Trả vé            |
|--------------------------------------------------------------------------------------------------|
| Vé đã phát hành                                                                                  |
| [v] Đặt vé thành công. Vé của từng chỗ đã được gửi qua SMS tới số điện thoại người đi.           |
|--------------------------------------------------------------------------------------------------|
| Chuyến: Hà Nội - Lào Cai, 21:00 03/02/2027                                                       |
| Các vé đã phát hành                                                                              |
| | Mã vé      | Chỗ  | Họ tên người đi  | Số điện thoại  |    Giá vé |                            |
| |------------|------|------------------|----------------|-----------|                            |
| | SV0000123  | A05  | Nguyễn Văn An    | 0912345678     | 360.000 đ |                            |
| | SV0000124  | A06  | Trần Thị Bình    | 0987654321     | 360.000 đ |                            |
|                                                                                                  |
| Tổng tiền: 720.000 đ                                                                             |
+--------------------------------------------------------------------------------------------------+
```

Dưới 600 px: bảng vé chuyển thành danh sách thẻ, mỗi vé một thẻ có nhãn cột lặp lại. Màn hình không có nút hành động. Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Header | Tên hệ thống và menu ACT-01, mục "Đặt vé trực tuyến" đang chọn | Trên cùng, cao 56 px | STT 8, 35, 36, 37 |
| Tiêu đề màn hình | "Vé đã phát hành" (tiêu đề cấp 1) | Dưới header | STT 14 |
| Thông điệp | Banner thành công MSG-12 (biểu tượng thành công kèm chữ) | Dưới tiêu đề | STT 46, 47 |
| Nội dung | Tuyến và giờ xuất bến; bảng vé (Mã vé, Chỗ, Họ tên người đi, Số điện thoại người đi, Giá vé); dòng Tổng tiền | Vùng nội dung | STT 28; UC-002 Dữ liệu ra 4 |
| Hành động | Không có nút | - | Màn hình kết thúc; P04 không có bước tiếp theo |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị banner thành công MSG-12; hiển thị tuyến, giờ xuất bến, bảng các vé đã phát hành của lần đặt và tổng tiền đã thanh toán; tiêu điểm vào tiêu đề màn hình; lịch sử trình duyệt của SCR-04 được thay bằng màn hình này để Quay lại không gửi lại thanh toán | UC-002 bước 11-13; showIssuedTickets; MSG-12; quy định STT 33, 65 |
| 2 | Liên kết "SaoViet Bus" ở header | liên kết | Nhấn | Mở SCR-01 (điều hướng chung, STT 39) | Quy định STT 8, 39 |
| 3 | Mục menu "Đặt vé trực tuyến" (đang chọn) và "Trả vé" | liên kết | Nhấn | Mở màn hình đầu của use case được chọn (SCR-02 hoặc SCR-06) theo mẫu 1 như E-02, E-07; dữ liệu đã nhập trên màn hình hiện tại không được giữ. Mục "Đặt vé trực tuyến" có nền, vạch dưới và thuộc tính trang hiện hành (STT 37) | Quy định STT 35, 36, 37, 38; xem Q-89 |
| 4 | Bảng vé đã phát hành | bảng | Khởi tạo | Mỗi hàng một vé: Mã vé, Chỗ, Họ tên người đi, Số điện thoại người đi, Giá vé; sắp theo mã chỗ; chú thích bảng "Các vé đã phát hành" | UC-002 bước 13, Dữ liệu ra 4 STT 1-5; BR-10 |
| 5 | Dòng Tổng tiền | vùng hiển thị | Khởi tạo | Hiển thị tổng tiền đã thanh toán của lần đặt | UC-002 bước 13, Dữ liệu ra 4 STT 7; BR-06 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Tuyến và giờ xuất bến | - (theo giá trị) | Chữ | Hiển thị, căn trái | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | - | P04 UC-002 mục 5 Dữ liệu ra 4 STT 6; ASM-17 |
| Mã vé | - (do hệ thống cấp) | Chữ | Hiển thị, căn trái | Chuỗi chữ và số do hệ thống cấp, duy nhất toàn hệ thống, ví dụ SV0000123 | Độ dài mã vé chờ Q-90 nên không đặt giới hạn ở giao diện; mỗi chỗ một mã (BR-10) | P04 UC-002 mục 5 Dữ liệu ra 4 STT 1; BR-10; GL-22; Q-90 |
| Chỗ | - (theo sơ đồ xe) | Chữ | Hiển thị, căn trái | Mã chỗ theo sơ đồ xe, ví dụ A05 | - | P04 UC-002 mục 5 Dữ liệu ra 4 STT 2 |
| Họ tên người đi | 100 | Chữ | Hiển thị, căn trái | Họ tên người đi của chỗ | Giới hạn như SCR-03 (Q-32) | P04 UC-002 mục 5 Dữ liệu ra 4 STT 3; Q-32 |
| Số điện thoại người đi | 10 | Chữ (chuỗi chữ số) | Hiển thị, căn trái | 10 chữ số liền, không dấu phân cách | Số đã nhận vé qua SMS | P04 UC-002 mục 5 Dữ liệu ra 4 STT 4; ASM-15 |
| Giá vé | - (theo giá trị tính ở BR-05) | Tiền | Hiển thị, căn phải | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ" | - | P04 UC-002 mục 5 Dữ liệu ra 4 STT 5; BR-05 |
| Tổng tiền | - (theo giá trị tính ở BR-06) | Tiền | Hiển thị, căn phải, chữ đậm | Bằng tổng giá vé các vé trong bảng | Dữ liệu mẫu: 360.000 + 360.000 = 720.000 đ | P04 UC-002 mục 5 Dữ liệu ra 4 STT 7; BR-06 |

Dữ liệu mẫu trên hình: mã vé SV0000123 lấy từ ví dụ P04; mã vé SV0000124 của chỗ A06 theo cùng dạng chuỗi do hệ thống cấp (giá trị minh hoạ). Tổng tiền bằng tổng các dòng, cùng đơn vị đồng.

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có | - | Màn hình không có trường nhập | - |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-05 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 46: banner MSG-12 cho biết đặt vé và gửi SMS đã thành công | Không có |
| SCR-05 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng hiển thị theo P04 mục 5, thuật ngữ theo P05 | Không có |
| SCR-05 | Nielsen: 3 Người dùng kiểm soát và tự do | Đạt | STT 39, 65: tên hệ thống và menu dẫn đi tiếp; Quay lại của trình duyệt không đưa vào lại bước đã thanh toán | Không có |
| SCR-05 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 11, 12, 35, 38: vị trí nút, tên nút, menu giống các màn hình web khác | Không có |
| SCR-05 | Nielsen: 5 Ngăn lỗi | Đạt | STT 65: lịch sử được thay thế nên không gửi lại thao tác thanh toán | Không có |
| SCR-05 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | Toàn bộ thông tin vé hiển thị cùng màn hình | Không có |
| SCR-05 | Nielsen: 7 Linh hoạt và hiệu quả | Không áp dụng | Màn hình kết quả chỉ xem | Không có |
| SCR-05 | Nielsen: 8 Thẩm mỹ và tối giản | Đạt | STT 9, 10: mỗi màn hình chỉ có điều khiển truy được về P04 hoặc trách nhiệm boundary | Không có |
| SCR-05 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Không áp dụng | Màn hình không sinh lỗi | Không có |
| SCR-05 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 53, 54: chỉ có gợi ý tại trường; chưa có trang trợ giúp vì nguồn không có tài liệu hướng dẫn | Q-86 (đã mở ở ui-standards.md) |
| SCR-05 | Shneiderman: Nhất quán | Đạt | STT 9, 10, 11, 38 áp dụng nguyên văn | Không có |
| SCR-05 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60: tương phản, nhãn, bàn phím, phóng chữ | Không có |
| SCR-05 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46: mọi thao tác gửi hệ thống đều có phản hồi trạng thái hoặc kết quả | Không có |
| SCR-05 | Shneiderman: Hội thoại có điểm kết thúc rõ | Đạt | Màn hình kết thúc của UC-002 có thông điệp thành công MSG-12 | Không có |
| SCR-05 | Shneiderman: Ngăn lỗi | Không áp dụng | Không có dữ liệu nhập | Không có |
| SCR-05 | Shneiderman: Hoàn tác dễ dàng | Vi phạm còn mở | Vé đã phát hành; việc trả vé là UC-008, màn hình không có hoàn tác | Q-87 (đã mở); không tự thêm chức năng |
| SCR-05 | Shneiderman: Người dùng làm chủ | Đạt | Không có bước bắt buộc nào tiếp theo | Không có |
| SCR-05 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | Thông tin vé hiển thị đủ để ghi lại, không bắt nhớ | Không có |
| SCR-05 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58: không có hình mang nghĩa ngoài biểu tượng trạng thái đã kèm chữ | Không có |
| SCR-05 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 28, 57: bảng có chú thích và tiêu đề cột, nhóm trường có tiêu đề nhóm, tiêu đề cấp 1 duy nhất | Không có |
| SCR-05 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19: mọi trạng thái kèm chữ hoặc biểu tượng có nhãn chữ | Không có |
| SCR-05 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 55: mọi cặp màu từ 5,53:1 | Không có |
| SCR-05 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 7, 60: đơn vị rem, chiều cao hộp chứa chữ không cố định | Xác minh trên trang thật khi có bản dựng |
| SCR-05 | WCAG 1.4.10 Reflow | Đạt | STT 1, 5, 60: một cột dưới 1024 px, bảng chuyển thành thẻ dưới 600 px | Không có |
| SCR-05 | WCAG 1.4.11 Tương phản thành phần 3:1 | Đạt | STT 56: viền điều khiển #767676 (4,54:1), viền tiêu điểm 8,66:1 | Không có |
| SCR-05 | WCAG 2.1.1 Bàn phím | Đạt | STT 41 đến 43, 59: mọi điều khiển dùng được bằng bàn phím | Không có |
| SCR-05 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33: thứ tự Tab trùng thứ tự đọc, không dùng tabindex dương | Không có |
| SCR-05 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề cấp 1, nút có tên bằng chữ | Không có |
| SCR-05 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Đạt | STT 34: viền tiêu điểm 3 px #1F4E79, không tắt | Không có |
| SCR-05 | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | STT 9: header và vùng hành động không cố định khi cuộn | Không có |
| SCR-05 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 59: không thao tác nào cần kéo thả | Không có |
| SCR-05 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | STT 30: vùng bấm 44 x 44 px (48 px trên điện thoại) | Không có |
| SCR-05 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 9, 36, 38, 39: header, menu, vị trí điều hướng giống nhau ở mọi màn hình web của ACT-01 | Không có |
| SCR-05 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng một chức năng dùng cùng tên nút và thuật ngữ | Không có |
| SCR-05 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp lặp lại ở nhiều màn hình | Q-86 |
| SCR-05 | WCAG 3.3.1 Nhận biết lỗi | Không áp dụng | Màn hình không sinh lỗi | Không có |
| SCR-05 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Không áp dụng | Không có trường nhập | Không có |
| SCR-05 | WCAG 3.3.3 Gợi ý sửa lỗi | Không áp dụng | Không có thông điệp lỗi | Không có |
| SCR-05 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Không áp dụng | Thanh toán đã xong ở SCR-04 | Không có |
| SCR-05 | WCAG 3.3.7 Không bắt nhập lại | Không áp dụng | Không có trường nhập | Không có |
| SCR-05 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-05 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 46: thông điệp trạng thái không cướp tiêu điểm, lỗi đọc ngay | Không có |
| SCR-05 | Nền tảng: Material Design (mức nhấn mạnh nút, một hành động chính) | Đạt | STT 11, 20, 21: một nút chính, nút phụ dạng viền | Không có |
| SCR-05 | Nền tảng: Apple HIG (vùng chạm 44 pt, điều hướng quay lại theo nền tảng) | Đạt | STT 20, 30, 65: nút cao 44 px (điện thoại 48 px), Quay lại theo trình duyệt | Không có |
| SCR-05 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-05 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-05 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-05 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-05 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-05 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-05 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |

## h) Thông điệp mới

Không có. Màn hình dùng MSG-12 của ui-standards.md.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-90 | Mã vé do hệ thống cấp có định dạng và độ dài tối đa là bao nhiêu (ví dụ chữ SV và 7 chữ số)? (Theo ví dụ SV + 7 chữ số / Khác) | SCR-05, SCR-18 trường Mã vé; Q-45; P13 (cột mã vé) | P04 UC-002 Dữ liệu ra 3 STT 1: "Chuỗi chữ và số do hệ thống cấp", ví dụ SV0000123, không nêu độ dài |
| Q-89 | Khi hành khách rời màn hình bằng menu, tên hệ thống hoặc đóng trang trong lúc các chỗ đang được giữ (SCR-03, SCR-04), lần đặt có kết thúc và trả chỗ ngay không? (đã nêu đầy đủ ở SCR-03) | Hành vi của mục menu và liên kết tên hệ thống ở màn hình này; BR-07, BR-08 | P04 UC-002 luồng 9a chỉ nêu hết thời hạn giữ chỗ |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-002 bước 12 | Lỗi gửi SMS của Cổng SMS chưa có luồng (Q-56) nên SCR-05 hiển thị MSG-12 khẳng định vé đã gửi SMS trong mọi trường hợp | Thêm luồng ngoại lệ gửi SMS lỗi sau khi Q-56 được trả lời; khi đó thêm MSG tương ứng thay cho MSG-12 |

## Vấn đề còn mở

- MSG-12 khẳng định SMS đã gửi trong khi hành vi khi Cổng SMS lỗi chưa đặc tả (Q-56).
- Màn hình không có nút; việc rời màn hình dùng liên kết tên hệ thống và menu (điều hướng chung). Đây là màn hình kết thúc của UC-002, đủ lối ra theo screen-transition.md mục 3.
- Nielsen #10 còn mở theo Q-86; Shneiderman hoàn tác còn mở theo Q-87.
