# P11a - Danh sách màn hình (screen-list) - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-002, UC-008, UC-013, UC-015 (1.0); P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-002, UC-008, UC-013, UC-015 (qua P08 và các bảng message); P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0 (F3, F4); P11a-gui/ui-standards.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 1; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | Toàn hệ thống, giai đoạn 1. Phân tích mới phủ 4 trong 18 use case (UC-002, UC-008, UC-013, UC-015), nên màn hình chỉ phủ 4 use case đó cùng 3 màn hình điều hướng; use case còn lại mới có trong P02 |

Quy ước: boundary giao diện người dùng cần màn hình được xác định từ P10 F3 (dòng có phần tử thiết kế View, Store hoặc ViewModel) và P10 F4 (package PKG-05, PKG-26, PKG-27, PKG-07 thuộc layer Presentation PKG-01). Tên màn hình ghi tiếng Việt trước, tiếng Anh trong ngoặc để làm slug cho SCR-nn-slug.md ở giai đoạn 2.

## 1. Danh sách màn hình

| SCR | Tên | Boundary AC nguồn | UC | Tác nhân | Loại | Lớp thiết kế (DC) | Mục đích | Bước UC phục vụ |
|---|---|---|---|---|---|---|---|---|
| SCR-01 | Trang chủ hành khách (Passenger home) | Điều hướng: mở UC-002, UC-008; lối vào UC-001, UC-007, UC-009, UC-011 chờ P04 | UC-002, UC-008 (UC-001, UC-007, UC-009, UC-011 chưa có màn hình đích) | ACT-01 | Độc lập | - | Chọn use case cần làm | - |
| SCR-02 | Tìm và chọn chuyến (Search and select trip) | AC-B-BookTicketForm | UC-002 | ACT-01 | Độc lập | DC-BookTicketView, DC-BookTicketStore | Nhập điểm đi, điểm đến, ngày đi; xem danh sách chuyến khớp và chọn một chuyến | 1-3, 2a, 4a |
| SCR-03 | Chọn chỗ và nhập thông tin người đi (Select seats and enter traveler info) | AC-B-BookTicketForm | UC-002 | ACT-01 | Phụ thuộc có dữ liệu | DC-BookTicketView, DC-BookTicketStore | Xem sơ đồ chỗ của chuyến, chọn tối đa 5 chỗ, nhập họ tên và số điện thoại người đi cho từng chỗ | 4-9, 6a, 6b, 7a, 7b |
| SCR-04 | Thanh toán lần đặt (Pay booking) | AC-B-BookTicketForm | UC-002 (phần gọi UC-003 chờ Q-84) | ACT-01 | Phụ thuộc có dữ liệu | DC-BookTicketView, DC-BookTicketStore | Xem lại chỗ, người đi, tổng tiền và thời gian giữ chỗ còn lại; thanh toán trước khi hết thời hạn giữ chỗ | 9, 10, 9a, 9a2, 10a |
| SCR-05 | Vé đã phát hành (Issued tickets) | AC-B-BookTicketForm | UC-002 | ACT-01 | Phụ thuộc có dữ liệu | DC-BookTicketView, DC-BookTicketStore | Xem các vé đã phát hành kèm tổng tiền; màn hình kết thúc của UC-002 | 11-13 |
| SCR-06 | Nhập vé cần trả (Enter ticket to return) | AC-B-ReturnTicketForm | UC-008 | ACT-01 | Độc lập | DC-ReturnTicketView, DC-ReturnTicketStore | Nhập mã vé và số điện thoại người đi để tìm vé cần trả | 1-3, 2a, 2b, 3a, 3b |
| SCR-07 | Xác nhận trả vé (Confirm ticket return) | AC-B-ReturnTicketForm | UC-008 | ACT-01 | Con phụ thuộc | DC-ReturnTicketView, DC-ReturnTicketStore | Xem thông tin vé, mức hoàn, số tiền hoàn và xác nhận hoặc không trả vé; thao tác tài chính không hoàn tác | 4-6, 6a, 7-9, 9a |
| SCR-08 | Kết quả trả vé (Ticket return result) | AC-B-ReturnTicketForm | UC-008 | ACT-01 | Phụ thuộc có dữ liệu | DC-ReturnTicketView, DC-ReturnTicketStore | Xem trạng thái vé sau trả, số tiền hoàn và hình thức hoàn; màn hình kết thúc | 10, 11 |
| SCR-09 | Trang chủ nhân viên bán vé (Ticket clerk home) | Điều hướng: mở UC-008; lối vào UC-004, UC-005, UC-007 chờ P04 | UC-008 (UC-004, UC-005, UC-007 chưa có màn hình đích) | ACT-02 | Độc lập | - | Chọn use case cần làm | - |
| SCR-10 | Nhập vé cần trả tại quầy (Enter ticket to return at counter) | AC-B-CounterReturnTicketForm | UC-008 | ACT-02 | Độc lập | DC-CounterReturnTicketView, DC-CounterReturnTicketStore | Nhập mã vé in trên vé giấy để tìm vé khách trả tại quầy | 1-3, 2a, 2b, 3a, 3b |
| SCR-11 | Xác nhận trả vé tại quầy (Confirm ticket return at counter) | AC-B-CounterReturnTicketForm | UC-008 | ACT-02 | Con phụ thuộc | DC-CounterReturnTicketView, DC-CounterReturnTicketStore | Xem thông tin vé, mức hoàn, số tiền hoàn và xác nhận hoặc không trả vé; hoàn tiền mặt tại quầy | 4-6, 6a, 7, 7a, 10 |
| SCR-12 | Kết quả trả vé tại quầy (Counter ticket return result) | AC-B-CounterReturnTicketForm | UC-008 | ACT-02 | Phụ thuộc có dữ liệu | DC-CounterReturnTicketView, DC-CounterReturnTicketStore | Xem trạng thái vé sau trả, số tiền hoàn và hình thức hoàn để chi tiền mặt; màn hình kết thúc | 10, 11 |
| SCR-13 | Trang chủ nhân viên điều hành (Dispatcher home) | Điều hướng: mở UC-013; lối vào UC-012 chờ P04 | UC-013 (UC-012 chưa có màn hình đích) | ACT-03 | Độc lập | - | Chọn use case cần làm | - |
| SCR-14 | Chỉ định chuyến cần huỷ (Specify trip to cancel) | AC-B-CancelTripForm | UC-013 | ACT-03 | Độc lập | DC-CancelTripView, DC-CancelTripStore | Nhập tuyến, ngày xuất bến, giờ xuất bến của chuyến cần huỷ | 1-3, 2a, 2b, 2c |
| SCR-15 | Xác nhận huỷ chuyến (Confirm trip cancellation) | AC-B-CancelTripForm | UC-013 | ACT-03 | Con phụ thuộc | DC-CancelTripView, DC-CancelTripStore | Xem số vé theo kênh mua, số đặt chỗ chưa thanh toán, tổng số tiền hoàn và xác nhận hoặc không huỷ chuyến | 3, 4, 4a, 5-10 |
| SCR-16 | Kết quả huỷ chuyến (Trip cancellation result) | AC-B-CancelTripForm | UC-013 | ACT-03 | Phụ thuộc có dữ liệu | DC-CancelTripView, DC-CancelTripStore | Xem số vé đã huỷ, kết quả hoàn tiền, số tin nhắn đã gửi, mã vé hoàn không thành công; màn hình kết thúc | 11, 8a |
| SCR-17 | Chọn chuyến soát vé (Select trip to check) | AC-B-CheckBoardingTicketForm | UC-015 | ACT-05 | Độc lập | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel | Chọn chuyến đã có danh sách hành khách trên máy để bắt đầu phiên soát vé | 1 |
| SCR-18 | Soát vé (Check tickets) | AC-B-CheckBoardingTicketForm | UC-015 | ACT-05 | Phụ thuộc có dữ liệu | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel | Xem thông tin chuyến và số vé; quét hoặc nhập mã vé, xem kết quả hợp lệ hay không hợp lệ; kết thúc soát vé | 2-9, 3a, 5a, 5b, 5c |
| SCR-19 | Kết quả soát vé của chuyến (Trip check summary) | AC-B-CheckBoardingTicketForm | UC-015 | ACT-05 | Phụ thuộc có dữ liệu | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel | Xem số vé đã soát, số vé còn hiệu lực chưa soát, trạng thái gửi kết quả; màn hình kết thúc | 10, 11, 10a |

Thống kê: 19 màn hình; 3 màn hình điều hướng; 16 màn hình có boundary nguồn. Số màn hình mỗi use case: UC-002 có 4; UC-008 có 3 cho ACT-01 và 3 cho ACT-02; UC-013 có 3; UC-015 có 3 (đều không quá 6). Phân loại theo mẫu dịch chuyển dẫn tới màn hình: Độc lập 8 (SCR-01, 02, 06, 09, 10, 13, 14, 17); Con phụ thuộc 3 (SCR-07, 11, 15); Con độc lập 0; Phụ thuộc có dữ liệu 8 (SCR-03, 04, 05, 08, 12, 16, 18, 19).

Mô tả cách nhóm: mỗi hộp xác nhận của trả vé và huỷ chuyến là một màn hình con phụ thuộc vì có nội dung và điều khiển riêng (thông tin vé, số tiền hoàn, hai nút theo hành động) ngoài mẫu hộp thông điệp chuẩn. Thông điệp lỗi và thông điệp kết quả ngắn dùng hộp thông điệp chuẩn và mã MSG ở ui-standards.md, không có mã SCR. Thanh toán của UC-003 chưa có P04 nên SCR-04 chỉ gồm phần của UC-002 (Q-84).

## 2. Boundary không có màn hình

| AC | Loại boundary | Ánh xạ ở P10 (SS, DC) | Lý do |
|---|---|---|---|
| AC-B-SmsGateway | Giao diện hệ thống (kênh thông báo SMS, ACT-07) | SS-02 SmsDelivery (PKG-16, IF-03) | Là kênh gửi tin nhắn tới điện thoại người đi, không hiển thị trong hệ thống; thông báo gửi SMS cho người dùng hiển thị bằng MSG-12, MSG-31 |
| AC-B-PaymentGateway | Giao diện hệ thống (hệ thống ngoài, ACT-06) | SS-01 OnlinePayment (PKG-15, IF-01, IF-02) | Là giao diện với cổng thanh toán của đối tác, đã ánh xạ sang subsystem; phần hiển thị phía hệ thống nằm ở SCR-04 và SCR-07 |
| AC-B-BarcodeScanner | Giao diện thiết bị (đầu quét mã vạch, ACT-09) | SS-03 BarcodeReading (PKG-18, IF-04, IF-05) | Là thiết bị, đã ánh xạ sang subsystem; kết quả quét hiển thị ở SCR-18 |

Ghi chú: DC-BookTicketRestController, DC-ReturnTicketRestController, DC-CounterReturnTicketRestController, DC-CancelTripRestController và DC-BoardingSyncRestController (PKG-08) là thành phần layer Application theo P09 F5, không phải boundary giao diện người dùng nên không có màn hình. SS-04 TicketPrinting (máy in vé, ACT-08) không có boundary AC ở P08 và thuộc UC-005 chưa phân tích.

## 3. Đánh giá theo chuẩn (F7), giai đoạn 1

Giai đoạn 1 đánh giá chuẩn hoá (ui-standards.md) và cách nhóm màn hình. Đánh giá trên hình ảnh, bảng điều khiển và bảng thuộc tính trường của từng SCR-nn thực hiện ở giai đoạn 2 trong mục g của mỗi đặc tả. Dòng có nhiều SCR nghĩa là kết quả như nhau cho các màn hình đó.

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-01 đến SCR-19 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Quy định STT 44, 45, 46; MSG-01, 13, 14, 25, 30, 39; đồng hồ giữ chỗ ở SCR-04 | Không có |
| SCR-01 đến SCR-19 | Nielsen 2 Khớp hệ thống và thế giới thực | Đạt | STT 6, 15, 17 (tiếng Việt, định dạng của P04, thuật ngữ P05) | Không có |
| SCR-01 đến SCR-06, SCR-08 đến SCR-10, SCR-12 đến SCR-14, SCR-16, SCR-17 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | STT 39, 42, 65 (về trang chủ, Esc, Quay lại trình duyệt) | Không có |
| SCR-07, SCR-11, SCR-15, SCR-18, SCR-19 | Nielsen 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | Thao tác trả vé, huỷ chuyến, kết thúc soát vé không có hoàn tác theo P04; Back của hệ điều hành ở SCR-18 vô hiệu (STT 69) | Giữ hộp xác nhận (STT 63); câu hỏi Q-87 |
| SCR-01 đến SCR-19 | Nielsen 4 Nhất quán và theo chuẩn | Đạt | STT 11, 12, 35, 38 | Không có |
| SCR-01 đến SCR-19 | Nielsen 5 Ngăn lỗi | Đạt | STT 20 (vô hiệu nút khi xử lý), 25, 27, 62, 63 | Không có |
| SCR-01 đến SCR-19 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | STT 25, 29, 53 (chọn từ danh sách, sơ đồ chỗ, gợi ý định dạng) | Không có |
| SCR-02, SCR-03, SCR-06, SCR-10, SCR-14, SCR-18 | Nielsen 7 Linh hoạt và hiệu quả | Đạt | STT 41 (Enter), 27 (gõ ngày), 67 (đầu quét tự đưa mã vào ô) | Không dùng phím tắt tuỳ biến (STT 40) |
| SCR-01 đến SCR-19 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | STT 9, 10, 39 (mỗi thẻ điều hướng chỉ có tên use case) | Không có |
| SCR-01 đến SCR-19 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | STT 48 đến 52; mọi MSG lỗi theo mẫu điều gì sai --> làm gì tiếp | Không có |
| SCR-01 đến SCR-19 | Nielsen 10 Trợ giúp và tài liệu | Vi phạm còn mở | Chỉ có gợi ý tại trường (STT 53); chưa có trang trợ giúp vì nguồn không có tài liệu hướng dẫn | Q-86 |
| SCR-01 đến SCR-19 | Shneiderman nhất quán | Đạt | STT 9, 10, 11, 38 | Không có |
| SCR-01 đến SCR-19 | Shneiderman khả dụng cho mọi người dùng | Đạt | STT 55 đến 60 | Không có |
| SCR-01 đến SCR-19 | Shneiderman phản hồi đầy đủ | Đạt | STT 44, 46, 66, 68 | Không có |
| SCR-04, SCR-05, SCR-08, SCR-12, SCR-16, SCR-19 | Shneiderman hội thoại có điểm kết thúc rõ | Đạt | Màn hình kết quả có thông điệp thành công (MSG-12, 23, 24, 31, 38); SCR-04 thất bại kết thúc bằng MSG-10 rồi về SCR-02 | Không có |
| SCR-07, SCR-11, SCR-15 | Shneiderman ngăn lỗi | Đạt | STT 62, 63 (xác nhận, tiêu điểm đầu ở nút phụ) | Không có |
| SCR-07, SCR-11, SCR-15, SCR-18, SCR-19 | Shneiderman hoàn tác dễ dàng | Vi phạm còn mở | Không có hoàn tác trong P04 | Q-87; không tự thêm chức năng |
| SCR-18 | Shneiderman người dùng làm chủ | Vi phạm còn mở | Back của hệ điều hành không có tác dụng ở SCR-18 (STT 69) | Q-87 |
| SCR-01 đến SCR-19 | Shneiderman giảm tải trí nhớ ngắn hạn | Đạt | STT 25, 29, 45; SCR-04 hiển thị lại chỗ, người đi, tổng tiền | Không có |
| SCR-01 đến SCR-19 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58 | Xác minh trên hình ảnh ở giai đoạn 2 |
| SCR-01 đến SCR-19 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 28, 57 | Xác minh ở giai đoạn 2 |
| SCR-01 đến SCR-19 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19, 29, 37, 66 | Không có |
| SCR-01 đến SCR-19 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | STT 18, 55 (mọi cặp màu từ 5,53:1) | Không có |
| SCR-01 đến SCR-19 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 7, 60 | Xác minh ở giai đoạn 2 |
| SCR-01 đến SCR-16 | WCAG 1.4.10 Reflow | Đạt | STT 1, 2, 5, 60; ngoại lệ bảng rộng và sơ đồ chỗ | Không có |
| SCR-17 đến SCR-19 | WCAG 1.4.10 Reflow | Không áp dụng | Ứng dụng Android, không phải nội dung web | Dùng sp và cuộn dọc (STT 60) |
| SCR-01 đến SCR-19 | WCAG 1.4.11 Tương phản thành phần | Đạt | STT 56 | Không có |
| SCR-01 đến SCR-19 | WCAG 2.1.1 Bàn phím | Đạt | STT 41 đến 43, 59 | Không có |
| SCR-01 đến SCR-19 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33 | Không có |
| SCR-01 đến SCR-19 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57 | Không có |
| SCR-01 đến SCR-16 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Đạt | STT 34 | Không có |
| SCR-17 đến SCR-19 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Không áp dụng | Thiết bị chỉ dùng cảm ứng và đầu quét; tiêu điểm ô mã vé theo STT 67 | Không có |
| SCR-01 đến SCR-19 | WCAG 2.4.11 Tiêu điểm không bị che | Vi phạm đã sửa | Bản nháp đầu đặt header và vùng hành động cố định khi cuộn, có thể che ô đang giữ tiêu điểm | Sửa: STT 9 (không cố định), STT 10 (khoảng đệm đáy 88 dp), STT 34 |
| SCR-03 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 29, 59 (chọn chỗ bằng bấm) | Không có |
| SCR-01 đến SCR-19 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | STT 30 (44, 40, 48 px; không dưới 24 px) | Không có |
| SCR-01 đến SCR-19 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 9, 38, 39 | Không có |
| SCR-01 đến SCR-19 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17 | Không có |
| SCR-01 đến SCR-19 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | Chưa có cơ chế trợ giúp lặp lại ở nhiều màn hình (STT 54) | Q-86 |
| SCR-01 đến SCR-19 | WCAG 3.3.1 Nhận biết lỗi | Đạt | STT 48, 49 | Không có |
| SCR-02, SCR-03, SCR-06, SCR-10, SCR-14, SCR-18 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | STT 23, 24, 53, 57 | Không có |
| SCR-01 đến SCR-19 | WCAG 3.3.3 Gợi ý sửa lỗi | Đạt | STT 51; mọi MSG lỗi nêu việc cần làm tiếp | Không có |
| SCR-04, SCR-07, SCR-11, SCR-15 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | STT 62, 63; SCR-04 xem lại tổng tiền trước khi thanh toán | Không có |
| SCR-03, SCR-04, SCR-06, SCR-10, SCR-14 | WCAG 3.3.7 Không bắt nhập lại | Đạt | STT 52 | Không có |
| SCR-01 đến SCR-19 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-01 đến SCR-19 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 46, 45 | Không có |
| SCR-17 đến SCR-19 | Material Design (vùng chạm 48 dp, một hành động chính) | Đạt | STT 20, 30, 11 | Không có |
| SCR-01 đến SCR-16 | Material Design (mức nhấn mạnh nút, một hành động chính) | Đạt | STT 11, 20, 21 | Không có |
| SCR-01 đến SCR-16 | Apple HIG (vùng chạm 44 pt, điều hướng quay lại theo nền tảng) | Vi phạm đã sửa | Bản nháp đầu đặt nút web hành khách cao 40 px theo ví dụ F1, thấp hơn 44 pt trong khi website nhận cả cảm ứng | Sửa: STT 20, 23, 30 (44 px, điện thoại 48 px); STT 65 cho Quay lại |
| SCR-02, SCR-03, SCR-06, SCR-10, SCR-14, SCR-18 | Baymard: form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Đạt | STT 23 | Không có |
| SCR-02, SCR-03, SCR-06, SCR-10, SCR-14, SCR-18 | Baymard: đánh dấu bắt buộc và tuỳ chọn; giảm số trường | Đạt | STT 24 | Không có |
| SCR-02, SCR-03, SCR-06, SCR-10, SCR-14, SCR-18 | Baymard: kiểm tra khi rời trường; chấp nhận nhiều định dạng nhập | Đạt | STT 27, 32 | Không có |
| SCR-02, SCR-03, SCR-06, SCR-10, SCR-14, SCR-18 | Baymard: giữ dữ liệu, lỗi đặt cạnh trường và cụ thể | Đạt | STT 48, 51, 52 | Không có |
| SCR-04 | Baymard: hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Đạt | SCR-04 hiển thị chỗ, người đi, tổng tiền (BR-06); nội dung thanh toán của UC-003 chờ Q-84 | Không có |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-84 | Việc thanh toán của UC-003 diễn ra thế nào trên giao diện: hành khách được chuyển sang trang của cổng thanh toán rồi quay lại, hay nhập thông tin thanh toán ngay trên website? SCR-04 cần hiển thị và có điều khiển nào ngoài tổng tiền, thời gian giữ chỗ và nút Thanh toán? (Chuyển hướng sang cổng / Form nhúng / Khác) | SCR-04; MSG-11, MSG-14; cạnh E-04, E-05 ở screen-transition.md; UC-003 | P04 UC-002 bước 10 "Gọi use case UC-003 Thanh toán vé trực tuyến"; UC-003 chưa có P04, P07; P06 NFR-06 "chưa có tài liệu API" (Q-24) |
| Q-85 | Khi phụ xe mở ứng dụng soát vé mà máy chưa có danh sách hành khách của chuyến nào (chưa tới mốc 15 phút hoặc gửi danh sách lỗi), SCR-17 hiển thị gì và phụ xe làm gì tiếp? | SCR-17; cạnh E-19 | P04 UC-015 tiền điều kiện (REQ-61) và Dữ liệu vào 1 "Là một chuyến đã có danh sách hành khách trên máy" không nêu trường hợp chưa có danh sách |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-60 | Điểm khởi đầu của ACT-01 là việc mở website; của ACT-02 và ACT-03 là sau khi nhân viên đã có phiên làm việc (ASM-09); của ACT-05 là khi mở ứng dụng soát vé có phiên làm việc (ASM-09). Màn hình đầu tiên của ACT-01, ACT-02, ACT-03 là màn hình điều hướng liệt kê use case user-goal của tác nhân trong P02 (quy định STT 35); màn hình đầu tiên của ACT-05 là SCR-17 vì ACT-05 chỉ có UC-015. Màn hình đăng nhập không thuộc phạm vi vì chưa có use case xác thực nhân viên (Q-27 của P02). | Nguồn và P04 không nêu màn hình đầu tiên; cần một điểm khởi đầu để mọi màn hình truy được từ node Start, và chỉ có tác nhân cần chọn giữa nhiều use case mới có màn hình điều hướng | SCR-01, SCR-09, SCR-13, SCR-17; node START-ACT-01, START-ACT-02, START-ACT-03, START-ACT-05 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3, F4 (PKG-05, PKG-26, PKG-27) | Ba màn hình điều hướng (SCR-01, SCR-09, SCR-13) không có boundary ở P08 nên không có View ở P10 | Khi chạy lại P10, thêm phần tử View điều hướng cho mỗi package PKG-05, PKG-26, PKG-27 (hoặc thành phần điều hướng dùng chung); P12 thiết kế |
| P10 | DC-BookTicketView, DC-ReturnTicketView, DC-CounterReturnTicketView, DC-CancelTripView, DC-CheckBoardingTicketView | Mỗi boundary có một View nhưng sinh 3 đến 4 màn hình (SCR-02 đến SCR-05 cùng DC-BookTicketView) | Giữ cột DC theo View hiện có; P12 cân nhắc tách thành phần giao diện theo màn hình |
| P10 | F3 | Bảng F3 không có cột layer, phải đối chiếu F4 để biết phần tử nào ở layer giao diện | Thêm cột Layer vào F3 khi chạy lại P10 |
| P04 | UC-003 | UC-003 chưa có đặc tả nên SCR-04 không có căn cứ cho phần thanh toán (Q-84) | Chạy P04 và P07 cho UC-003 trước giai đoạn 2 của SCR-04 |

## Vấn đề còn mở

- Phạm vi: P02 có 18 use case, P04 và P07 mới phủ 4. Màn hình điều hướng SCR-01, SCR-09, SCR-13 liệt kê lối vào cho UC-001, UC-004, UC-005, UC-007, UC-009, UC-011, UC-012 chưa có màn hình đích; cần chạy lại P11a khi các use case này có P04, P07. Quản lý nhà xe (ACT-04: UC-016 đến UC-018) chưa có màn hình nào và chưa có package giao diện ở P10.
- Target 9: giai đoạn 1 chỉ đánh giá được chuẩn hoá và cách nhóm màn hình (mục 3); đánh giá trên hình ảnh từng màn hình chưa làm vì chưa có SCR-nn-slug.md. Còn 3 nhóm vi phạm còn mở (Nielsen 3, Nielsen 10, Shneiderman hoàn tác) đều có câu hỏi Q-86, Q-87.
- Target 2: mọi boundary giao diện người dùng của P10 (5 boundary) đều có ít nhất một màn hình; ba boundary còn lại có dòng ở mục 2.
- Chọn giữa hai quy tắc (C9): prompt yêu cầu bảng F7 phủ mọi tiêu chí cho mỗi SCR (MUC_CHI_TIET là DAY_DU), nhưng giai đoạn 1 chưa có hình ảnh. Đã ghi mỗi tiêu chí một dòng với cột SCR nhóm theo phạm vi áp dụng thay vì 19 nhân 55 dòng; bảng đầy đủ từng màn hình ở giai đoạn 2.
- Màn hình con phụ thuộc SCR-07, SCR-11, SCR-15 chọn dạng hộp thoại modal thay cho màn hình riêng; nếu nhà xe muốn màn hình xác nhận riêng, đổi loại sang Phụ thuộc có dữ liệu và cạnh E-08, E-12, E-16 sang mẫu 4.
