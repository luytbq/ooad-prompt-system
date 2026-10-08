# P11a - SCR-17 Chọn chuyến soát vé - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-015-check-boarding-ticket.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-015-check-boarding-ticket-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-17, UC-015 |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-17 Chọn chuyến soát vé (Select trip to check) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-17 Chọn chuyến soát vé (Select trip to check) |
| UC | UC-015 Soát vé lên xe (Check Boarding Ticket) |
| Bước UC | 1 |
| Tác nhân | ACT-05 Phụ xe |
| Boundary AC | AC-B-CheckBoardingTicketForm (requestStartCheck) |
| Lớp thiết kế (DC) | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel |
| Loại màn hình | Độc lập |
| Đến từ | START-ACT-05 (E-18, mẫu 1, mở ứng dụng soát vé khi có phiên làm việc, ASM-60) |
| Đi tới | SCR-18 (E-19, mẫu 4, dữ liệu "Chuyến cần soát") |

## c) Hình ảnh màn hình

Khung dây ở màn hình ứng dụng soát vé, hướng dọc 360 x 640 dp (720 x 1280 px). Dữ liệu mẫu theo P04 UC-015 mục 5.

```text
+----------------------------------------+
| SaoViet Bus                            |
| Chọn chuyến soát vé                    |
|----------------------------------------|
|                                        |
| Chuyến cần soát (bắt buộc)             |
| Chọn một trong các chuyến đã có danh   |
| sách hành khách trên máy.              |
| [ Hà Nội - Lào Cai, 21:00 03/02/2027 v]|
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|----------------------------------------|
|                     [ Bắt đầu soát vé ]|
+----------------------------------------+
```

Khi máy chưa có danh sách của chuyến nào (ASM-63), vùng thông điệp dưới thanh tiêu đề hiển thị cảnh báo MSG-43, danh sách chọn rỗng và nút "Bắt đầu soát vé" vô hiệu. Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Tên hệ thống "SaoViet Bus" (14 sp) và tiêu đề "Chọn chuyến soát vé" (20 sp) | Trên cùng, cao 56 dp | STT 8, 10, 14: màn hình đầu tiên của ứng dụng hiển thị tên hệ thống ở thanh tiêu đề |
| Thông điệp | Cảnh báo MSG-43 (khi máy chưa có danh sách); lỗi tại trường MSG-40; MSG-01 khi xử lý | Ngay dưới thanh tiêu đề | STT 10, 13, 46 |
| Nội dung | Nhãn "Chuyến cần soát (bắt buộc)", dòng gợi ý, danh sách chọn các chuyến đã có danh sách hành khách trên máy | Vùng nội dung cuộn dọc | STT 23, 24, 25, 53; ASM-32 |
| Hành động | Nút chính "Bắt đầu soát vé" cao 48 dp | Vùng hành động đáy cao 72 dp, nút ở bên phải | STT 10, 11 |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị thanh tiêu đề có tên hệ thống, danh sách các chuyến đã có danh sách hành khách trên máy (mỗi chuyến "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy", sắp theo giờ xuất bến tăng dần), chưa chọn sẵn chuyến nào. Máy chưa có danh sách của chuyến nào thì hiển thị MSG-43, vô hiệu nút Bắt đầu soát vé | UC-015 bước 1, Dữ liệu vào 1; ASM-32, ASM-63; MSG-43; quy định STT 8 |
| 2 | Danh sách "Chuyến cần soát" | danh sách chọn | Chọn | Ghi nhận chuyến được chọn và xoá lỗi tại trường nếu có | UC-015 bước 1, Dữ liệu vào 1 STT 1; requestStartCheck |
| 3 | Danh sách "Chuyến cần soát" | danh sách chọn | Rời trường | Kiểm tra bắt buộc; chưa chọn thì hiển thị MSG-40 dưới ô | Dữ liệu vào 1 STT 1; MSG-40 |
| 4 | Nút chính "Bắt đầu soát vé" | nút chính | Nhấn | Kiểm tra đã chọn chuyến (chưa chọn thì MSG-40 và không gửi). Hợp lệ thì vô hiệu nút, hiển thị MSG-01 nếu quá 1 giây, gửi chuyến để mở phiên soát vé; thành công thì mở SCR-18 theo E-19 truyền "Chuyến cần soát" cùng số vé còn hiệu lực và số vé đã soát (bước 2). Lỗi hệ thống: MSG-02 | UC-015 bước 1, 2; requestStartCheck; MSG-01, MSG-02, MSG-40; ASM-32, ASM-33 |
| 5 | Nút Back của hệ điều hành | nút | Nhấn | Thoát ứng dụng theo hệ điều hành (đây là màn hình đầu tiên); không có thao tác nghiệp vụ | Quy định STT 69 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Chuyến cần soát | - (chọn từ danh sách) | Lựa chọn | Chọn, bắt buộc, mặc định không chọn sẵn, căn trái | Là một chuyến đã có danh sách hành khách trên máy soát vé (ASM-32); mỗi giá trị dạng "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Chuyến xác định bằng tuyến và giờ xuất bến (REQ-42); từ 12 giá trị trở xuống dùng điều khiển chọn gốc (STT 25); sắp theo giờ xuất bến tăng dần (Thiết kế: chuyến sắp đi hiện trước); gợi ý "Chọn một trong các chuyến đã có danh sách hành khách trên máy" | P04 UC-015 mục 5 Dữ liệu vào 1 STT 1; REQ-42, ASM-32; GL-05, GL-04 |

Dữ liệu mẫu trên hình: chuyến Hà Nội - Lào Cai xuất bến 21:00 03/02/2027, cùng chuyến với ví dụ P04 UC-015 mục 5.

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Chuyến cần soát | Rời trường; nhấn Bắt đầu soát vé | 1. Bắt buộc: đã chọn một chuyến. 2. Định dạng: không có. 3. Miền giá trị: chỉ chọn trong danh sách các chuyến đã có danh sách hành khách trên máy. 4. Quy tắc nghiệp vụ: không có ở giao diện | 1: MSG-40 (Chưa chọn chuyến cần soát. Vui lòng chọn chuyến cần soát.) |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-17 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 44, 46, 66: MSG-01 khi xử lý từ 1 giây, kết quả quét chiếm vùng riêng cao tối thiểu 160 dp | Không có |
| SCR-17 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng tuyến, giờ, thuật ngữ Chuyến, Mã vé, Phiên soát vé theo P05 | Không có |
| SCR-17 | Nielsen: 3 Người dùng kiểm soát và tự do | Đạt | STT 69: Back thoát ứng dụng theo hệ điều hành; chưa có thao tác không hoàn tác | Không có |
| SCR-17 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 10, 11, 12: bố cục vùng, thứ tự nút (phụ trái, chính phải), tên nút là động từ kèm đối tượng | Không có |
| SCR-17 | Nielsen: 5 Ngăn lỗi | Vi phạm đã sửa | Bản nháp chọn sẵn chuyến đầu tiên của danh sách, dễ soát nhầm chuyến (BR-20) | Sửa: không chọn sẵn, nút Bắt đầu soát vé chỉ hợp lệ khi đã chọn chuyến |
| SCR-17 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | STT 53, 67: gợi ý định dạng tại trường, tiêu điểm tự về ô mã vé | Không có |
| SCR-17 | Nielsen: 7 Linh hoạt và hiệu quả | Đạt | STT 41, 67: Enter và đầu quét gửi mã, không cần chạm thêm | Không có |
| SCR-17 | Nielsen: 8 Thẩm mỹ và tối giản | Đạt | STT 10: chỉ có điều khiển truy được về P04 hoặc trách nhiệm boundary | Không có |
| SCR-17 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | STT 48 đến 52, 66: thông điệp theo mẫu điều gì sai --> làm gì tiếp | Không có |
| SCR-17 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 53, 54: chỉ có gợi ý tại trường; chưa có trang trợ giúp | Q-86 (đã mở ở ui-standards.md) |
| SCR-17 | Shneiderman: Nhất quán | Đạt | STT 10, 11, 12 áp dụng nguyên văn | Không có |
| SCR-17 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60, 66: tương phản, nhãn, sp, kết quả có chữ và biểu tượng | Không có |
| SCR-17 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46, 66, 68: phản hồi bằng chữ, màu, biểu tượng và rung | Không có |
| SCR-17 | Shneiderman: Hội thoại có điểm kết thúc rõ | Không áp dụng | Màn hình khởi đầu, hội thoại kết thúc ở SCR-19 | Không có |
| SCR-17 | Shneiderman: Ngăn lỗi | Đạt | Không chọn sẵn chuyến; chỉ chọn trong danh sách | Không có |
| SCR-17 | Shneiderman: Hoàn tác dễ dàng | Đạt | Chọn chuyến chưa thay đổi dữ liệu | Không có |
| SCR-17 | Shneiderman: Người dùng làm chủ | Đạt | Phụ xe tự chọn chuyến và bắt đầu | Không có |
| SCR-17 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | Gợi ý nêu rõ danh sách là các chuyến đã có danh sách hành khách trên máy | Không có |
| SCR-17 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58: biểu tượng kết quả luôn kèm chữ | Không có |
| SCR-17 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 57: ô mã vé có nhãn nhìn thấy gắn với ô | Không có |
| SCR-17 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19, 66: kết quả phân biệt bằng chữ Hợp lệ hoặc Không hợp lệ và biểu tượng, không chỉ màu | Không có |
| SCR-17 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 55, 66: #FFFFFF trên #1B6E3C 6,28; #FFFFFF trên #B3261E 6,54 | Không có |
| SCR-17 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 60: dùng sp, hỗ trợ cỡ chữ hệ thống tới 200% | Xác minh trên máy thật khi có bản dựng |
| SCR-17 | WCAG 1.4.10 Reflow | Không áp dụng | Ứng dụng Android, không phải nội dung web | Dùng sp và cuộn dọc (STT 60) |
| SCR-17 | WCAG 1.4.11 Tương phản thành phần 3:1 | Đạt | STT 56: viền ô nhập #767676 (4,54:1) | Không có |
| SCR-17 | WCAG 2.1.1 Bàn phím | Đạt | STT 41, 67: Enter và đầu quét gửi mã; mọi nút dùng được bằng chạm | Máy chỉ có chạm và đầu quét, không có bàn phím cứng |
| SCR-17 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33, 67: ô mã vé giữ tiêu điểm khi mở màn hình và sau mỗi lần quét | Không có |
| SCR-17 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề màn hình ở thanh tiêu đề, nút có tên bằng chữ | Không có |
| SCR-17 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Không áp dụng | Thiết bị chỉ dùng cảm ứng và đầu quét; tiêu điểm ô mã vé theo STT 67 | Không có |
| SCR-17 | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | STT 10: khoảng đệm đáy 88 dp để vùng hành động cố định không che ô đang giữ tiêu điểm | Không có |
| SCR-17 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 59: không thao tác nào cần kéo thả | Không có |
| SCR-17 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | STT 30: vùng bấm 48 x 48 dp | Không có |
| SCR-17 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 10, 11: vị trí thanh tiêu đề và vùng hành động giống nhau ở ba màn hình | Không có |
| SCR-17 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng thuật ngữ và tên nút | Không có |
| SCR-17 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp | Q-86 |
| SCR-17 | WCAG 3.3.1 Nhận biết lỗi | Đạt | STT 48, 66: lỗi nhập đặt dưới ô, kết quả không hợp lệ có chữ và biểu tượng | Không có |
| SCR-17 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | STT 23, 24, 53, 57: nhãn nhìn thấy, (bắt buộc), gợi ý định dạng | Không có |
| SCR-17 | WCAG 3.3.3 Gợi ý sửa lỗi | Đạt | STT 51: thông điệp lỗi nêu việc cần làm tiếp | Không có |
| SCR-17 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Không áp dụng | Không có thao tác tài chính hoặc pháp lý | Không có |
| SCR-17 | WCAG 3.3.7 Không bắt nhập lại | Đạt | STT 52: dữ liệu giữ khi báo lỗi | Không có |
| SCR-17 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-17 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 46: thông điệp trạng thái không cướp tiêu điểm, lỗi đọc ngay | Không có |
| SCR-17 | Nền tảng: Material Design (vùng chạm 48 dp, một hành động chính, điều hướng Back) | Đạt | STT 10, 11, 20, 30: vùng chạm 48 dp, một nút chính | Không có |
| SCR-17 | Nền tảng: Apple HIG (vùng chạm 44 pt) | Đạt | STT 30: vùng chạm 48 dp lớn hơn 44 pt | Không có |
| SCR-17 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Đạt | STT 23: nhãn trên ô, một cột (một trường duy nhất) | Không có |
| SCR-17 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Đạt | STT 24: nhãn có (bắt buộc) | Không có |
| SCR-17 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Đạt | STT 32: kiểm tra khi rời trường | Không có |
| SCR-17 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Đạt | STT 48, 52: lỗi dưới ô | Không có |
| SCR-17 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Không áp dụng | Trường chỉ chọn từ danh sách, không nhập định dạng tự do | Không có |
| SCR-17 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Đạt | STT 24: một trường theo Dữ liệu vào 1 | Không có |
| SCR-17 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Không áp dụng | Màn hình không phải bước thanh toán | Không có |

## h) Thông điệp mới cần bổ sung vào danh mục MSG

| MSG | Loại (Lỗi / Cảnh báo / Xác nhận / Thành công / Đang xử lý) | Nội dung hiển thị | Nút và hành động | Nguồn (UC bước, BR) |
|---|---|---|---|---|
| MSG-43 | Cảnh báo | Máy chưa có danh sách hành khách của chuyến nào. Vui lòng thử lại sau khi danh sách được gửi về máy. | Đóng thông điệp; nút Bắt đầu soát vé vô hiệu | UC-015 tiền điều kiện (REQ-61), ASM-63, Q-85 |

MSG-40 dùng ở màn hình này do SCR-02 đề xuất (xem Đề xuất sửa artifact trước).


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-91 | Khi máy có danh sách của chuyến mới sau khi SCR-17 đã mở (danh sách tới lúc 15 phút trước giờ xuất bến), danh sách chọn có tự cập nhật hay phụ xe phải mở lại màn hình? (Tự cập nhật / Mở lại màn hình) | SCR-17; ASM-63; Q-85 | P04 UC-015 tiền điều kiện (REQ-61); nguồn không nêu cách ứng dụng nhận danh sách mới (UC-014 chưa có P04) |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-63 | Khi máy chưa có danh sách hành khách của chuyến nào, SCR-17 hiển thị cảnh báo MSG-43, danh sách chọn rỗng và nút Bắt đầu soát vé bị vô hiệu | Q-85 chưa có câu trả lời, tiền điều kiện của UC-015 không nêu trường hợp này; cần một hành vi hiển thị để màn hình không để trống; không thêm chức năng | SCR-17 mục d, f; MSG-43; cạnh E-19 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P11a (ui-standards.md) | Mục 2 Danh mục thông điệp | MSG-40 (từ SCR-02) và MSG-43 chưa có trong danh mục | Bổ sung MSG-40, MSG-41, MSG-42 (SCR-02) và MSG-43 (SCR-17) khi chạy lại giai đoạn 1 |
| P04 | UC-015 mục 5 Dữ liệu vào 1 | Không nêu trường hợp máy chưa có danh sách của chuyến nào (Q-85) | Thêm luồng thay thế ở bước 1 hoặc tiền điều kiện cho trường hợp này |

## Vấn đề còn mở

- Hành vi khi máy chưa có danh sách là giả định ASM-63, chờ Q-85 và Q-91.
- Nielsen #10 còn mở theo Q-86.
