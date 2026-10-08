# P11a - SCR-19 Kết quả soát vé của chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-015-check-boarding-ticket.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-015-check-boarding-ticket-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-19, UC-015 |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-19 Kết quả soát vé của chuyến (Trip check summary) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-19 Kết quả soát vé của chuyến (Trip check summary) |
| UC | UC-015 Soát vé lên xe (Check Boarding Ticket) |
| Bước UC | 10, 11, 10a |
| Tác nhân | ACT-05 Phụ xe |
| Boundary AC | AC-B-CheckBoardingTicketForm (showCheckSummary) |
| Lớp thiết kế (DC) | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-18 (E-20, mẫu 4, dữ liệu "Kết quả soát vé") |
| Đi tới | Không có cạnh đi (màn hình kết thúc của UC-015); Back của hệ điều hành quay về SCR-17 để bắt đầu phiên mới (ASM-65) |

## c) Hình ảnh màn hình

Khung dây ở màn hình ứng dụng soát vé, hướng dọc 360 x 640 dp, kết quả gửi thành công. Dữ liệu mẫu theo P04 UC-015 mục 5.

```text
+----------------------------------------+
| Kết quả soát vé của chuyến             |
|----------------------------------------|
| [v] Kết quả soát vé của chuyến đã được |
|     gửi.                               |
|----------------------------------------|
| Chuyến: Hà Nội - Lào Cai,              |
|         21:00 03/02/2027               |
|                                        |
| Số vé đã soát: 35                      |
| Số vé còn hiệu lực chưa soát: 1        |
| Trạng thái gửi kết quả: Đã gửi         |
|                                        |
|                                        |
|                                        |
|                                        |
|----------------------------------------|
|                                        |
+----------------------------------------+
```

Khi máy mất sóng, banner cảnh báo MSG-37 (nền #FFF4D6, chữ #7A4F00, biểu tượng cảnh báo) thay banner thành công và dòng trạng thái là "Chờ gửi khi có sóng". Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | "Kết quả soát vé của chuyến" (tiêu đề cấp 1, 20 sp) | Trên cùng, cao 56 dp | STT 10, 14 |
| Thông điệp | Banner thành công MSG-38 hoặc cảnh báo MSG-37 | Ngay dưới thanh tiêu đề | STT 10, 46, 47 |
| Nội dung | Chuyến đã soát, số vé đã soát, số vé còn hiệu lực chưa soát, trạng thái gửi kết quả | Vùng nội dung cuộn dọc | UC-015 Dữ liệu ra 3 |
| Hành động | Không có nút | Vùng hành động đáy để trống | Màn hình kết thúc; lối ra là Back của hệ điều hành (ASM-65) |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị tuyến và giờ xuất bến, số vé đã soát, số vé còn hiệu lực chưa soát (bằng số vé còn hiệu lực trừ số vé đã soát), trạng thái gửi kết quả. Trạng thái "Đã gửi" kèm banner thành công MSG-38; trạng thái "Chờ gửi khi có sóng" kèm banner cảnh báo MSG-37 (kết quả lưu trên máy, tự gửi khi có sóng, không cần phụ xe thao tác). Mục lịch sử của SCR-18 được thay bằng màn hình này | UC-015 bước 10, 11, 10a, Dữ liệu ra 3 STT 1-4; showCheckSummary; REQ-60; MSG-37, MSG-38; ASM-35, ASM-52, ASM-65 |
| 2 | Vùng thông tin kết quả | vùng hiển thị | Khởi tạo | Bốn dòng nhãn và giá trị, mỗi dòng một thông tin, giá trị số căn phải trên dòng | UC-015 Dữ liệu ra 3 |
| 3 | Nút Back của hệ điều hành | nút | Nhấn | Quay về SCR-17 để phụ xe bắt đầu phiên soát vé mới (SCR-18 không còn trong lịch sử vì phiên đã kết thúc) | Quy định STT 69; ASM-65 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Tuyến và giờ xuất bến | - (theo giá trị) | Chữ | Hiển thị, căn trái | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Chuyến đã soát | P04 UC-015 mục 5 Dữ liệu ra 3 STT 1; REQ-42 |
| Số vé đã soát | 2 | Số | Hiển thị, căn phải | Số nguyên từ 0 đến 40; chỉ gồm vé được báo hợp lệ (ASM-35) | Dữ liệu mẫu: 35 | P04 UC-015 mục 5 Dữ liệu ra 3 STT 2; ASM-35 |
| Số vé còn hiệu lực chưa soát | 2 | Số | Hiển thị, căn phải | Bằng số vé còn hiệu lực trừ số vé đã soát | Dữ liệu mẫu: 36 - 35 = 1 | P04 UC-015 mục 5 Dữ liệu ra 3 STT 3; GL-38 |
| Trạng thái gửi kết quả | - (một trong hai giá trị) | Lựa chọn | Hiển thị, căn trái | "Đã gửi" hoặc "Chờ gửi khi có sóng" | Kèm biểu tượng có nhãn chữ ở banner (STT 19) | P04 UC-015 mục 5 Dữ liệu ra 3 STT 4; REQ-60 |

Dữ liệu mẫu trên hình: khớp ví dụ P04 UC-015 mục 5 (35 vé đã soát, 1 vé còn hiệu lực chưa soát, 36 vé còn hiệu lực; lần quét báo vé đã huỷ và vé đã soát không được tính).

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có | - | Màn hình không có trường nhập | - |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-19 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 46: banner MSG-38 hoặc MSG-37 cho biết kết quả đã gửi hay chờ gửi | Không có |
| SCR-19 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng tuyến, giờ, thuật ngữ Chuyến, Mã vé, Phiên soát vé theo P05 | Không có |
| SCR-19 | Nielsen: 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | Không có hoàn tác kết thúc soát vé theo P04; Back về SCR-17 chỉ bắt đầu phiên mới, không mở lại phiên đã kết thúc | Q-87; không tự thêm chức năng |
| SCR-19 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 10, 11, 12: bố cục vùng, thứ tự nút (phụ trái, chính phải), tên nút là động từ kèm đối tượng | Không có |
| SCR-19 | Nielsen: 5 Ngăn lỗi | Không áp dụng | Màn hình kết quả chỉ xem | Không có |
| SCR-19 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | Toàn bộ kết quả của chuyến hiển thị trên một màn hình | Không có |
| SCR-19 | Nielsen: 7 Linh hoạt và hiệu quả | Không áp dụng | Màn hình kết quả chỉ xem | Không có |
| SCR-19 | Nielsen: 8 Thẩm mỹ và tối giản | Đạt | STT 10: chỉ có điều khiển truy được về P04 hoặc trách nhiệm boundary | Không có |
| SCR-19 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Không áp dụng | Màn hình không sinh lỗi; mất sóng là cảnh báo MSG-37, không phải lỗi | Không có |
| SCR-19 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 53, 54: chỉ có gợi ý tại trường; chưa có trang trợ giúp | Q-86 (đã mở ở ui-standards.md) |
| SCR-19 | Shneiderman: Nhất quán | Đạt | STT 10, 11, 12 áp dụng nguyên văn | Không có |
| SCR-19 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60, 66: tương phản, nhãn, sp, kết quả có chữ và biểu tượng | Không có |
| SCR-19 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46, 66, 68: phản hồi bằng chữ, màu, biểu tượng và rung | Không có |
| SCR-19 | Shneiderman: Hội thoại có điểm kết thúc rõ | Đạt | Màn hình kết thúc của UC-015 có thông điệp thành công hoặc cảnh báo | Không có |
| SCR-19 | Shneiderman: Ngăn lỗi | Không áp dụng | Không có dữ liệu nhập | Không có |
| SCR-19 | Shneiderman: Hoàn tác dễ dàng | Vi phạm còn mở | Không có hoàn tác kết thúc soát vé theo P04 | Q-87 |
| SCR-19 | Shneiderman: Người dùng làm chủ | Đạt | Phụ xe tự bắt đầu phiên mới bằng Back | Không có |
| SCR-19 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | Bốn thông tin hiển thị cùng màn hình | Không có |
| SCR-19 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58: biểu tượng kết quả luôn kèm chữ | Không có |
| SCR-19 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 57: ô mã vé có nhãn nhìn thấy gắn với ô | Không có |
| SCR-19 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19: banner kèm biểu tượng có nhãn chữ và chữ trạng thái | Không có |
| SCR-19 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 55: #7A4F00 trên #FFF4D6 6,51:1; #1B6E3C trên #E6F4EA 5,53:1 | Không có |
| SCR-19 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 60: dùng sp, hỗ trợ cỡ chữ hệ thống tới 200% | Xác minh trên máy thật khi có bản dựng |
| SCR-19 | WCAG 1.4.10 Reflow | Không áp dụng | Ứng dụng Android, không phải nội dung web | Dùng sp và cuộn dọc (STT 60) |
| SCR-19 | WCAG 1.4.11 Tương phản thành phần 3:1 | Không áp dụng | Không có thành phần điều khiển | Không có |
| SCR-19 | WCAG 2.1.1 Bàn phím | Không áp dụng | Màn hình chỉ xem, không có điều khiển | Không có |
| SCR-19 | WCAG 2.4.3 Thứ tự tiêu điểm | Không áp dụng | Không có điều khiển nhận tiêu điểm | Không có |
| SCR-19 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề màn hình ở thanh tiêu đề, nút có tên bằng chữ | Không có |
| SCR-19 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Không áp dụng | Thiết bị chỉ dùng cảm ứng và đầu quét; tiêu điểm ô mã vé theo STT 67 | Không có |
| SCR-19 | WCAG 2.4.11 Tiêu điểm không bị che | Không áp dụng | Không có điều khiển nhận tiêu điểm | Không có |
| SCR-19 | WCAG 2.5.7 Thay thế thao tác kéo | Không áp dụng | Không có thao tác | Không có |
| SCR-19 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Không áp dụng | Không có điều khiển bấm | Không có |
| SCR-19 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 10, 11: vị trí thanh tiêu đề và vùng hành động giống nhau ở ba màn hình | Không có |
| SCR-19 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng thuật ngữ và tên nút | Không có |
| SCR-19 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp | Q-86 |
| SCR-19 | WCAG 3.3.1 Nhận biết lỗi | Không áp dụng | Không có trường nhập hoặc thao tác sinh lỗi | Không có |
| SCR-19 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Không áp dụng | Không có trường nhập | Không có |
| SCR-19 | WCAG 3.3.3 Gợi ý sửa lỗi | Không áp dụng | Không có thông điệp lỗi | Không có |
| SCR-19 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Không áp dụng | Không có thao tác tài chính hoặc pháp lý | Không có |
| SCR-19 | WCAG 3.3.7 Không bắt nhập lại | Không áp dụng | Không có trường nhập | Không có |
| SCR-19 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-19 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 46: thông điệp trạng thái không cướp tiêu điểm, lỗi đọc ngay | Không có |
| SCR-19 | Nền tảng: Material Design (vùng chạm 48 dp, một hành động chính, điều hướng Back) | Không áp dụng | Màn hình không có nút | Không có |
| SCR-19 | Nền tảng: Apple HIG (vùng chạm 44 pt) | Không áp dụng | Màn hình không có điều khiển chạm | Không có |
| SCR-19 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-19 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-19 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-19 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-19 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-19 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-19 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |

## h) Thông điệp mới

Không có. Màn hình dùng MSG-37, MSG-38 của ui-standards.md.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-65 | Sau khi phiên soát vé kết thúc, SCR-19 thay SCR-18 trong lịch sử Back của ứng dụng; Back của hệ điều hành ở SCR-19 đưa phụ xe về SCR-17 để bắt đầu phiên mới | screen-transition.md chỉ nói phụ xe bắt đầu phiên mới từ SCR-17 nhưng không có điều khiển hay cạnh nào; ui-standards.md STT 69 chỉ quy định Back ở SCR-18; cần một lối ra cho màn hình kết thúc mà không thêm nút | SCR-19 mục d; E-20; STT 69 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P11a (ui-standards.md) | STT 65, 69 | Quy tắc thay thế mục lịch sử khi chuyển sang màn hình kết quả chỉ nêu cho web, và STT 69 không nêu Back ở SCR-19 | Mở rộng STT 65 cho Android: chuyển SCR-18 --> SCR-19 thay mục lịch sử; STT 69 nêu Back ở SCR-19 về SCR-17 |
| P11a (screen-transition.md) | Mục 3 Kiểm tra, SCR-19 | Lối ra của SCR-19 chỉ ghi "bắt đầu phiên mới từ SCR-17" mà không có điều khiển | Ghi rõ lối ra là Back của hệ điều hành (ASM-65), không cần cạnh |

## Vấn đề còn mở

- SCR-19 không có nút; lối ra bằng Back là giả định ASM-65. Nếu nhà xe muốn nút "Soát chuyến khác" thì bổ sung vào P04 trước.
- Nielsen #3, Shneiderman hoàn tác còn mở theo Q-87; Nielsen #10 còn mở theo Q-86.
- Tiêu chí điều khiển (2.1.1, 2.4.3, 2.5.8, Material, HIG) ghi Không áp dụng vì màn hình không có điều khiển nào ngoài Back của hệ điều hành.
