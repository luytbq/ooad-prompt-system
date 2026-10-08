# P11b - Giao diện hệ thống và thiết bị - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (mục 3 đã cập nhật theo P09); 00-Conventions.md (bản hiện có); P10-design-elements.md 1.0; P08-analysis-model.md 1.0; P07-uc-analysis/UC-002, UC-008, UC-013, UC-015 (bản hiện có); P04-uc-specs/UC-002, UC-008, UC-013, UC-015 (bản hiện có); P06-supplementary-spec.md 1.0; P09-architecture.md 1.0. Tham số: PHAM_VI_SUBSYSTEM = Tất cả; TAI_LIEU_GIAO_TIEP = Không có; CHINH_SACH_LOI = Không có; YEU_CAU_BO_SUNG = đánh số Q mới từ Q-100 và ASM mới từ ASM-100 vì P11a chạy song song |
| Phạm vi | Toàn hệ thống: tám subsystem SS-01 đến SS-08 của P10. P08 mới phủ 4 trong 18 use case (UC-002, UC-008, UC-013, UC-015) nên UC-003, UC-005, UC-006, UC-014 và UC-009 đến UC-011 chỉ có chỗ giữ |

Tóm tắt: tám subsystem, 14 interface (IF-01 đến IF-14, IF-14 mới), 40 dòng operation (IF-12 có 5 operation được hiện thực ở SS-07 và SS-08 nên tính hai lần), 47 trang sơ đồ trong tám file .drawio. Chính sách lỗi (CHINH_SACH_LOI là Không có): operation có tác dụng phụ tài chính (requestPayment, requestRefund) không tự thử lại, kết quả không rõ thì tra cứu một lần bằng khoá do hệ thống sinh rồi trả Unknown; SMS thử lại tối đa 2 lần chỉ với lỗi xảy ra trước khi cổng nhận yêu cầu; kết quả soát vé gửi lại không giới hạn số lần vì idempotent theo tripId; mọi timeout, số lần thử lại là quyết định thiết kế ghi tại chỗ dùng, chỉ thời hạn chờ hoàn tiền của người dùng là giả định (ASM-101). Cổng thanh toán chưa có tài liệu API nên phần ánh xạ lời gọi ngoài để ở mức tên bước (Q-24, Q-100). Mọi interface giữ mã IF-nn của P10; IF-14 là interface mới do P11b cấp.

## SS-01 OnlinePayment

Package chứa: PKG-15. Tác nhân hoặc đối tượng ngoài: ACT-06.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-008 Trả vé | AC-C-ReturnTicketController (DC-ReturnTicketService) | SD1: 2.1.2 // requestRefund; 2.1.2.2 // returnRefundResult; SD4: 2.1.3a // showRefundFailedNotice | ticketCode, refundAmount | 9a (hoàn không thành công, Q-37, ASM-21). Chưa có luồng cho cổng không phản hồi hoặc kết quả không rõ (Q-55) |
| UC-013 Huỷ chuyến | AC-C-CancelTripController (DC-CancelTripService) | SD1: 2.1.5 // requestRefund; 2.1.5.2 // returnRefundResult (trong loop từng vé) | ticketCode, refundAmount của từng vé | 8a (hoàn không thành công, ASM-31, Q-43). Chưa có luồng cho cổng không phản hồi hoặc kết quả không rõ (Q-55) |
| UC-003 Thanh toán vé trực tuyến (chưa có P04, P07) | AC-C-PayTicketOnlineController (DC-PayTicketOnlineService), tạm | UC-002 SD1: 3.1.9 // payTickets, kết quả trả về thành công hoặc không thành công | tổng tiền của lần đặt (BR-06) | UC-002 10a (thanh toán không thành công, ASM-14). Cổng không phản hồi, kết quả đến muộn: Q-55, Q-10 |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Nhận yêu cầu thanh toán, hoàn tiền gửi tới cổng thanh toán của đối tác và trả kết quả | SS-01 | DC-PayTicketOnlineService (PKG-09), DC-ReturnTicketService (PKG-09), DC-CancelTripService (PKG-10) | PKG-15 |
| IF-02 | IPaymentResultListener | Nhận kết quả thanh toán do cổng gửi về (chiều ngược): bên cung cấp DC-PayTicketOnlineService (PKG-09), bên dùng SS-01 | DC-PayTicketOnlineService (PKG-09), hiện thực ở layer trên | SS-01 | PKG-15 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-06) | requestPayment(requestKey: String, amount: Money): PaymentRequestResult | requestKey: String - khoá idempotency do hệ thống sinh, một khoá cho mỗi lần thanh toán của một lần đặt<br>amount: Money - lớn hơn 0, bằng tổng tiền của lần đặt (BR-06) | PaymentRequestResult: status (Accepted / Rejected / Unknown), redirectTarget (có khi cổng yêu cầu chuyển hướng hành khách, Q-83) | PaymentGatewayUnavailableException (Kỹ thuật tạm thời); Rejected (Nghiệp vụ); Unknown (Không rõ kết quả) | UC-003 (gọi từ UC-002 bước 10; Tạm: P04, P07 của UC-003 chưa có, ASM-100) | Các chỗ của lần đặt đang được giữ và còn trong thời hạn giữ chỗ (BR-07) | Cổng đã tiếp nhận yêu cầu thanh toán cho requestKey khi status là Accepted; kết quả thanh toán đến sau qua IF-02 | Đồng bộ (nhận yêu cầu); kết quả thanh toán bất đồng bộ qua IF-02 | Không tự thử lại (chưa biết cổng có hỗ trợ khoá idempotency, Q-100) | Kết nối 5 giây, đọc 30 giây (Thiết kế: mặc định phổ biến của API cổng thanh toán; NFR-01 chưa có thời gian phản hồi, Q-22; thời hạn giữ chỗ 10 phút của BR-07 là giới hạn trên của việc hành khách chờ) |
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-06) | requestRefund(ticketCode: TicketCode, amount: Money, requestKey: String): RefundResult | ticketCode: TicketCode - mã vé mua trực tuyến cần hoàn<br>amount: Money - lớn hơn 0, không vượt giá vé (BR-13 đến BR-17)<br>requestKey: String - khoá do hệ thống sinh, mỗi yêu cầu hoàn một khoá, dùng lại khi tra cứu trạng thái | RefundResult: status (Succeeded / Declined / Unknown), refundReference (mã tham chiếu hoàn của cổng, có khi Succeeded) | PaymentGatewayUnavailableException (Kỹ thuật tạm thời, không gửi được yêu cầu); Declined (Nghiệp vụ); Unknown (Không rõ kết quả) | UC-008 (bước 8, 9); UC-013 (bước 7, 8). Thay cho // requestRefund và // returnRefundResult của AC-B-PaymentGateway: kết quả đi theo giá trị trả về | Vé mua trực tuyến, hình thức hoàn là Qua cổng thanh toán (BR-15); không lưu thông tin thẻ (NFR-03) | Succeeded: cổng xác nhận hoàn. Declined, Unknown: subsystem không ghi nhận gì, client quyết định theo P04 | Đồng bộ | Không (chưa có căn cứ cổng hỗ trợ khoá, Q-100); không tự thử lại | Đọc 30 giây (Thiết kế: như requestPayment, cộng một lần tra cứu 10 giây khi hết thời gian chờ); thời gian tối đa client chờ 45 giây (ASM-101) |
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-06) | queryRefundStatus(requestKey: String): RefundResult | requestKey: String - khoá của yêu cầu hoàn đã gửi | RefundResult: như requestRefund; Unknown khi cổng chưa có kết quả hoặc không hỗ trợ tra cứu (Q-100) | PaymentGatewayUnavailableException (Kỹ thuật tạm thời) | UC-008, UC-013 (operation kỹ thuật của chính sách lỗi A5: tra cứu trước khi báo không rõ; client dùng khi đối soát sau, chờ P04 theo Q-55) | requestKey đã dùng ở một lần requestRefund | Không thay đổi trạng thái | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: tra cứu một bản ghi, ngắn hơn yêu cầu hoàn) |
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-06) | queryPaymentStatus(requestKey: String): PaymentStatusResult | requestKey: String - khoá của yêu cầu thanh toán đã gửi | PaymentStatusResult: status (Succeeded / Failed / Pending / Unknown), paymentReference (PaymentReference, có khi Succeeded) | PaymentGatewayUnavailableException (Kỹ thuật tạm thời) | UC-003 (operation kỹ thuật của chính sách lỗi A5, Tạm theo ASM-100) | requestKey đã dùng ở một lần requestPayment | Không thay đổi trạng thái | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: như queryRefundStatus) |
| IF-02 | IPaymentResultListener | Cổng thanh toán (ACT-06), gọi ngược | receivePaymentResult(requestKey: String, outcome: PaymentOutcome, paymentReference: PaymentReference, amount: Money): void | requestKey: String - khoá của yêu cầu thanh toán<br>outcome: PaymentOutcome - Succeeded / Failed<br>paymentReference: PaymentReference - mã tham chiếu giao dịch của cổng (ASM-41, được lưu)<br>amount: Money - số tiền cổng ghi nhận | void | Không ném ngoại lệ về phía SS-01; bên hiện thực xử lý lỗi của mình (lỗi của bên hiện thực không lọt vào giao thức ngoài) | UC-003 (kết quả thanh toán trả về UC-002 bước 10, 10a); kết quả đến muộn sau hết thời hạn giữ chỗ chờ Q-10 | requestKey tồn tại; thông báo của cổng đã qua kiểm tra chữ ký trong SS-01 | Kết quả thanh toán được ghi nhận đúng một lần cho requestKey | Bất đồng bộ (cổng gọi vào); SS-01 gọi bên hiện thực đồng bộ trong luồng nhận thông báo | Có (khoá requestKey; cổng có thể gửi lặp) | 5 giây để bên hiện thực xác nhận cho cổng (Thiết kế: cổng thường gửi lại thông báo khi không được xác nhận kịp) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-01.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

queryPaymentStatus: ánh xạ 1-1, DC-PaymentGatewayService chuyển thẳng tới DC-PaymentGatewayClient rồi tới cổng, cùng cấu trúc với trang "Hộp trắng - queryRefundStatus", không rẽ nhánh khác.

#### Trang "Hộp đen - UC-008 requestRefund"

UC hoặc operation: UC-008

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-BB1-L01 | Lifeline | :DC-ReturnTicketService | «control» | - | Control của UC-008 (AC-C-ReturnTicketController) | 40 | 40 | 120 | 610 |
| SS01-BB1-L02 | Lifeline | :IF-01 IPaymentGateway | «interface» | - | Interface của SS-01 | 200 | 40 | 120 | 610 |
| SS01-BB1-FR1 | Fragment | alt [status = Succeeded] | alt | - | Mỗi toán hạng là một kết quả của requestRefund | 30 | 160 | 300 | 420 |
| SS01-BB1-FR1-O2 | Fragment | [status = Declined] | alt | SS01-BB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS01-BB1-FR1-SEP2 | 40 | 270 | 280 | 20 |
| SS01-BB1-FR1-O3 | Fragment | [status = Unknown] | alt | SS01-BB1-FR1 | Toán hạng 3, ngăn bởi đường nét đứt SS01-BB1-FR1-SEP3 | 40 | 380 | 280 | 20 |
| SS01-BB1-FR1-O4 | Fragment | [PaymentGatewayUnavailableException] | alt | SS01-BB1-FR1 | Toán hạng 4, ngăn bởi đường nét đứt SS01-BB1-FR1-SEP4 | 40 | 490 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-BB1-M01 | 1 | SS01-BB1-L01 | SS01-BB1-L02 | requestRefund(ticketCode, amount, requestKey) | Đồng bộ | - | UC-008 bước 8 |
| SS01-BB1-M02 | 2 | SS01-BB1-L02 | SS01-BB1-L01 | RefundResult(status = Succeeded) | Trả về | SS01-BB1-FR1 (toán hạng 1) | UC-008 bước 9 |
| SS01-BB1-M03 | 3 | SS01-BB1-L01 | SS01-BB1-L01 | cancelTicket + createRefund | Tự gọi | SS01-BB1-FR1 (toán hạng 1) | UC-008 bước 10 |
| SS01-BB1-M04 | 4 | SS01-BB1-L02 | SS01-BB1-L01 | RefundResult(status = Declined) | Trả về | SS01-BB1-FR1 (toán hạng 2) | UC-008 bước 9 |
| SS01-BB1-M05 | 5 | SS01-BB1-L01 | SS01-BB1-L01 | showRefundFailedNotice, vé giữ nguyên | Tự gọi | SS01-BB1-FR1 (toán hạng 2) | UC-008 luồng 9a |
| SS01-BB1-M06 | 6 | SS01-BB1-L02 | SS01-BB1-L01 | RefundResult(status = Unknown) | Trả về | SS01-BB1-FR1 (toán hạng 3) | UC-008 bước 9 |
| SS01-BB1-M07 | 7 | SS01-BB1-L01 | SS01-BB1-L01 | chưa có luồng P04 (Q-55) | Tự gọi | SS01-BB1-FR1 (toán hạng 3) | Q-55 |
| SS01-BB1-M08 | 8 | SS01-BB1-L02 | SS01-BB1-L01 | PaymentGatewayUnavailableException | Trả về | SS01-BB1-FR1 (toán hạng 4) | UC-008 bước 8 |
| SS01-BB1-M09 | 9 | SS01-BB1-L01 | SS01-BB1-L01 | chưa có luồng P04 (Q-55) | Tự gọi | SS01-BB1-FR1 (toán hạng 4) | Q-55 |

#### Trang "Hộp đen - UC-013 requestRefund"

UC hoặc operation: UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-BB2-L01 | Lifeline | :DC-CancelTripService | «control» | - | Control của UC-013 (AC-C-CancelTripController) | 40 | 40 | 120 | 660 |
| SS01-BB2-L02 | Lifeline | :IF-01 IPaymentGateway | «interface» | - | Interface của SS-01 | 200 | 40 | 120 | 660 |
| SS01-BB2-FR1 | Fragment | loop [với từng vé mua trực tuyến đã huỷ có hình thức hoàn Qua cổng thanh toán] | loop | - | Bước 7, 8 lặp theo từng vé (ASM-29) | 30 | 120 | 300 | 510 |
| SS01-BB2-FR2 | Fragment | alt [status = Succeeded] | alt | - | Mỗi toán hạng là một kết quả của requestRefund | 40 | 190 | 280 | 420 |
| SS01-BB2-FR2-O2 | Fragment | [status = Declined] | alt | SS01-BB2-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS01-BB2-FR2-SEP2 | 50 | 300 | 260 | 20 |
| SS01-BB2-FR2-O3 | Fragment | [status = Unknown] | alt | SS01-BB2-FR2 | Toán hạng 3, ngăn bởi đường nét đứt SS01-BB2-FR2-SEP3 | 50 | 410 | 260 | 20 |
| SS01-BB2-FR2-O4 | Fragment | [PaymentGatewayUnavailableException] | alt | SS01-BB2-FR2 | Toán hạng 4, ngăn bởi đường nét đứt SS01-BB2-FR2-SEP4 | 50 | 520 | 260 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-BB2-M01 | 1 | SS01-BB2-L01 | SS01-BB2-L02 | requestRefund(ticketCode, amount, requestKey) | Đồng bộ | SS01-BB2-FR1 (toán hạng 1) | UC-013 bước 7 |
| SS01-BB2-M02 | 2 | SS01-BB2-L02 | SS01-BB2-L01 | RefundResult(status = Succeeded) | Trả về | SS01-BB2-FR2 (toán hạng 1) | UC-013 bước 8 |
| SS01-BB2-M03 | 3 | SS01-BB2-L01 | SS01-BB2-L01 | recordRefund(thành công) | Tự gọi | SS01-BB2-FR2 (toán hạng 1) | UC-013 bước 9 |
| SS01-BB2-M04 | 4 | SS01-BB2-L02 | SS01-BB2-L01 | RefundResult(status = Declined) | Trả về | SS01-BB2-FR2 (toán hạng 2) | UC-013 bước 8 |
| SS01-BB2-M05 | 5 | SS01-BB2-L01 | SS01-BB2-L01 | recordRefund(chưa thành công) | Tự gọi | SS01-BB2-FR2 (toán hạng 2) | UC-013 luồng 8a |
| SS01-BB2-M06 | 6 | SS01-BB2-L02 | SS01-BB2-L01 | RefundResult(status = Unknown) | Trả về | SS01-BB2-FR2 (toán hạng 3) | UC-013 bước 8 |
| SS01-BB2-M07 | 7 | SS01-BB2-L01 | SS01-BB2-L01 | chưa có luồng P04 (Q-55) | Tự gọi | SS01-BB2-FR2 (toán hạng 3) | Q-55 |
| SS01-BB2-M08 | 8 | SS01-BB2-L02 | SS01-BB2-L01 | PaymentGatewayUnavailableException | Trả về | SS01-BB2-FR2 (toán hạng 4) | UC-013 bước 7 |
| SS01-BB2-M09 | 9 | SS01-BB2-L01 | SS01-BB2-L01 | chưa có luồng P04 (Q-55) | Tự gọi | SS01-BB2-FR2 (toán hạng 4) | Q-55 |

#### Trang "Hộp đen - UC-003 requestPayment và IF-02"

UC hoặc operation: UC-003

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-BB3-L01 | Lifeline | :DC-PayTicketOnlineService | «control» | - | Control tạm của UC-003 (AC-C-PayTicketOnlineController), hiện thực IF-02 | 40 | 40 | 120 | 610 |
| SS01-BB3-L02 | Lifeline | :IF-01 IPaymentGateway | «interface» | - | Interface của SS-01 | 200 | 40 | 120 | 610 |
| SS01-BB3-FR1 | Fragment | alt [status = Accepted] | alt | - | Tạm, theo ASM-100; thông báo kết quả thanh toán đi qua IF-02 | 30 | 160 | 300 | 420 |
| SS01-BB3-FR1-O2 | Fragment | [status = Rejected] | alt | SS01-BB3-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS01-BB3-FR1-SEP2 | 40 | 270 | 280 | 20 |
| SS01-BB3-FR1-O3 | Fragment | [status = Unknown] | alt | SS01-BB3-FR1 | Toán hạng 3, ngăn bởi đường nét đứt SS01-BB3-FR1-SEP3 | 40 | 380 | 280 | 20 |
| SS01-BB3-FR1-O4 | Fragment | [PaymentGatewayUnavailableException] | alt | SS01-BB3-FR1 | Toán hạng 4, ngăn bởi đường nét đứt SS01-BB3-FR1-SEP4 | 40 | 490 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-BB3-M01 | 1 | SS01-BB3-L01 | SS01-BB3-L02 | requestPayment(requestKey, amount) | Đồng bộ | - | UC-002 bước 10 / UC-003 |
| SS01-BB3-M02 | 2 | SS01-BB3-L02 | SS01-BB3-L01 | PaymentRequestResult(status = Accepted) | Trả về | SS01-BB3-FR1 (toán hạng 1) | UC-003 |
| SS01-BB3-M03 | 3 | SS01-BB3-L02 | SS01-BB3-L01 | receivePaymentResult(requestKey, outcome, paymentReference, amount) | Bất đồng bộ | SS01-BB3-FR1 (toán hạng 1) | IF-02, UC-002 bước 11 hoặc luồng 10a |
| SS01-BB3-M04 | 4 | SS01-BB3-L02 | SS01-BB3-L01 | PaymentRequestResult(status = Rejected) | Trả về | SS01-BB3-FR1 (toán hạng 2) | UC-003 |
| SS01-BB3-M05 | 5 | SS01-BB3-L01 | SS01-BB3-L01 | kết quả không thành công cho UC-002 | Tự gọi | SS01-BB3-FR1 (toán hạng 2) | UC-002 luồng 10a |
| SS01-BB3-M06 | 6 | SS01-BB3-L02 | SS01-BB3-L01 | PaymentRequestResult(status = Unknown) | Trả về | SS01-BB3-FR1 (toán hạng 3) | UC-003 |
| SS01-BB3-M07 | 7 | SS01-BB3-L01 | SS01-BB3-L01 | chưa có luồng P04 (Q-55) | Tự gọi | SS01-BB3-FR1 (toán hạng 3) | Q-55 |
| SS01-BB3-M08 | 8 | SS01-BB3-L02 | SS01-BB3-L01 | PaymentGatewayUnavailableException | Trả về | SS01-BB3-FR1 (toán hạng 4) | UC-003 |
| SS01-BB3-M09 | 9 | SS01-BB3-L01 | SS01-BB3-L01 | kết quả không thành công cho UC-002 | Tự gọi | SS01-BB3-FR1 (toán hạng 4) | UC-002 luồng 10a, Q-55 |

#### Trang "Hộp trắng - requestPayment"

UC hoặc operation: UC-003

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-WB1-FRM | Fragment | sd requestPayment | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 1020 |
| SS01-WB1-L01 | Lifeline | :DC-PaymentGatewayService | «control» | - | Lớp điều phối, hiện thực IF-01 | 120 | 40 | 120 | 960 |
| SS01-WB1-L02 | Lifeline | :DC-PaymentDataConverter | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 960 |
| SS01-WB1-L03 | Lifeline | :DC-PaymentGatewayClient | «adapter» | - | Lớp giao tiếp ngoài | 440 | 40 | 120 | 960 |
| SS01-WB1-L04 | Actor | Cổng thanh toán | «ACT-06» | - | Hệ thống ngoài | 600 | 40 | 120 | 960 |
| SS01-WB1-G1 | Gate | requestPayment | - | SS01-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS01-WB1-G1-2 | Gate | requestPayment | - | SS01-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 380 | 20 | 20 |
| SS01-WB1-G1-3 | Gate | requestPayment | - | SS01-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 920 | 20 | 20 |
| SS01-WB1-FR1 | Fragment | break [không kết nối được cổng] | break | - | Kết thúc operation bằng ngoại lệ | 110 | 320 | 460 | 90 |
| SS01-WB1-FR2 | Fragment | alt [có phản hồi trong thời gian chờ] | alt | - | Kết quả không rõ: tra cứu một lần | 110 | 450 | 620 | 320 |
| SS01-WB1-FR2-O2 | Fragment | [hết thời gian chờ sau khi đã gửi] | alt | SS01-WB1-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS01-WB1-FR2-SEP2 | 120 | 560 | 600 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-WB1-M01 | 1 | SS01-WB1-G1 | SS01-WB1-L01 | requestPayment(requestKey, amount) | Đồng bộ | - | UC-003 / UC-002 bước 10 |
| SS01-WB1-M02 | 2 | SS01-WB1-L01 | SS01-WB1-L02 | toPaymentApiRequest(requestKey, amount) | Đồng bộ | - | Chuyển kiểu mô hình sang định dạng ngoài |
| SS01-WB1-M03 | 3 | SS01-WB1-L02 | SS01-WB1-L01 | PaymentApiRequest | Trả về | - | - |
| SS01-WB1-M04 | 4 | SS01-WB1-L01 | SS01-WB1-L03 | sendPayment(paymentApiRequest) | Đồng bộ | - | - |
| SS01-WB1-M05 | 5 | SS01-WB1-L03 | SS01-WB1-L04 | submitPaymentRequest(paymentApiRequest) | Đồng bộ | - | - |
| SS01-WB1-M06 | 6 | SS01-WB1-L03 | SS01-WB1-L01 | ConnectionFailed (không gửi được yêu cầu) | Trả về | SS01-WB1-FR1 (toán hạng 1) | Lỗi kỹ thuật tạm thời |
| SS01-WB1-M07 | 7 | SS01-WB1-L01 | SS01-WB1-G1-2 | PaymentGatewayUnavailableException | Trả về | SS01-WB1-FR1 (toán hạng 1) | Cô lập lỗi giao thức |
| SS01-WB1-M08 | 8 | SS01-WB1-L04 | SS01-WB1-L03 | phản hồi đã tiếp nhận hoặc từ chối | Trả về | SS01-WB1-FR2 (toán hạng 1) | - |
| SS01-WB1-M09 | 9 | SS01-WB1-L03 | SS01-WB1-L01 | PaymentApiResponse | Trả về | SS01-WB1-FR2 (toán hạng 1) | - |
| SS01-WB1-M10 | 10 | SS01-WB1-L03 | SS01-WB1-L01 | ResponseTimeout (đã gửi, chưa có phản hồi) | Trả về | SS01-WB1-FR2 (toán hạng 2) | Kết quả không rõ |
| SS01-WB1-M11 | 11 | SS01-WB1-L01 | SS01-WB1-L03 | getPaymentStatus(requestKey) | Đồng bộ | SS01-WB1-FR2 (toán hạng 2) | Một lần, không gửi lại yêu cầu gốc |
| SS01-WB1-M12 | 12 | SS01-WB1-L03 | SS01-WB1-L04 | queryPaymentStatus(requestKey) | Đồng bộ | SS01-WB1-FR2 (toán hạng 2) | - |
| SS01-WB1-M13 | 13 | SS01-WB1-L04 | SS01-WB1-L03 | kết quả tra cứu hoặc không phản hồi | Trả về | SS01-WB1-FR2 (toán hạng 2) | - |
| SS01-WB1-M14 | 14 | SS01-WB1-L03 | SS01-WB1-L01 | PaymentApiResponse (status hoặc Unknown) | Trả về | SS01-WB1-FR2 (toán hạng 2) | - |
| SS01-WB1-M15 | 15 | SS01-WB1-L01 | SS01-WB1-L02 | toPaymentRequestResult(paymentApiResponse) | Đồng bộ | - | Chuyển định dạng ngoài sang kiểu của interface |
| SS01-WB1-M16 | 16 | SS01-WB1-L02 | SS01-WB1-L01 | PaymentRequestResult | Trả về | - | - |
| SS01-WB1-M17 | 17 | SS01-WB1-L01 | SS01-WB1-L01 | writeAuditLog(requestKey, status) | Tự gọi | - | Cơ chế ghi nhật ký (P09), không ghi dữ liệu thẻ (NFR-03) |
| SS01-WB1-M18 | 18 | SS01-WB1-L01 | SS01-WB1-G1-3 | PaymentRequestResult | Trả về | - | - |

#### Trang "Hộp trắng - requestRefund"

UC hoặc operation: UC-008, UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-WB2-FRM | Fragment | sd requestRefund | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 1020 |
| SS01-WB2-L01 | Lifeline | :DC-PaymentGatewayService | «control» | - | Lớp điều phối, hiện thực IF-01 | 120 | 40 | 120 | 960 |
| SS01-WB2-L02 | Lifeline | :DC-PaymentDataConverter | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 960 |
| SS01-WB2-L03 | Lifeline | :DC-PaymentGatewayClient | «adapter» | - | Lớp giao tiếp ngoài | 440 | 40 | 120 | 960 |
| SS01-WB2-L04 | Actor | Cổng thanh toán | «ACT-06» | - | Hệ thống ngoài | 600 | 40 | 120 | 960 |
| SS01-WB2-G1 | Gate | requestRefund | - | SS01-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS01-WB2-G1-2 | Gate | requestRefund | - | SS01-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 380 | 20 | 20 |
| SS01-WB2-G1-3 | Gate | requestRefund | - | SS01-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 920 | 20 | 20 |
| SS01-WB2-FR1 | Fragment | break [không kết nối được cổng] | break | - | Kết thúc operation bằng ngoại lệ | 110 | 320 | 460 | 90 |
| SS01-WB2-FR2 | Fragment | alt [có phản hồi trong thời gian chờ] | alt | - | Kết quả không rõ: tra cứu một lần | 110 | 450 | 620 | 320 |
| SS01-WB2-FR2-O2 | Fragment | [hết thời gian chờ sau khi đã gửi] | alt | SS01-WB2-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS01-WB2-FR2-SEP2 | 120 | 560 | 600 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-WB2-M01 | 1 | SS01-WB2-G1 | SS01-WB2-L01 | requestRefund(ticketCode, amount, requestKey) | Đồng bộ | - | UC-008 bước 8, 9 / UC-013 bước 7, 8 |
| SS01-WB2-M02 | 2 | SS01-WB2-L01 | SS01-WB2-L02 | toRefundApiRequest(ticketCode, amount, requestKey) | Đồng bộ | - | Chuyển kiểu mô hình sang định dạng ngoài |
| SS01-WB2-M03 | 3 | SS01-WB2-L02 | SS01-WB2-L01 | RefundApiRequest | Trả về | - | - |
| SS01-WB2-M04 | 4 | SS01-WB2-L01 | SS01-WB2-L03 | sendRefund(refundApiRequest) | Đồng bộ | - | - |
| SS01-WB2-M05 | 5 | SS01-WB2-L03 | SS01-WB2-L04 | submitRefundRequest(refundApiRequest) | Đồng bộ | - | - |
| SS01-WB2-M06 | 6 | SS01-WB2-L03 | SS01-WB2-L01 | ConnectionFailed (không gửi được yêu cầu) | Trả về | SS01-WB2-FR1 (toán hạng 1) | Lỗi kỹ thuật tạm thời |
| SS01-WB2-M07 | 7 | SS01-WB2-L01 | SS01-WB2-G1-2 | PaymentGatewayUnavailableException | Trả về | SS01-WB2-FR1 (toán hạng 1) | Cô lập lỗi giao thức |
| SS01-WB2-M08 | 8 | SS01-WB2-L04 | SS01-WB2-L03 | phản hồi hoàn tiền | Trả về | SS01-WB2-FR2 (toán hạng 1) | - |
| SS01-WB2-M09 | 9 | SS01-WB2-L03 | SS01-WB2-L01 | RefundApiResponse | Trả về | SS01-WB2-FR2 (toán hạng 1) | - |
| SS01-WB2-M10 | 10 | SS01-WB2-L03 | SS01-WB2-L01 | ResponseTimeout (đã gửi, chưa có phản hồi) | Trả về | SS01-WB2-FR2 (toán hạng 2) | Kết quả không rõ |
| SS01-WB2-M11 | 11 | SS01-WB2-L01 | SS01-WB2-L03 | getRefundStatus(requestKey) | Đồng bộ | SS01-WB2-FR2 (toán hạng 2) | Một lần, không gửi lại yêu cầu gốc |
| SS01-WB2-M12 | 12 | SS01-WB2-L03 | SS01-WB2-L04 | queryRefundStatus(requestKey) | Đồng bộ | SS01-WB2-FR2 (toán hạng 2) | - |
| SS01-WB2-M13 | 13 | SS01-WB2-L04 | SS01-WB2-L03 | kết quả tra cứu hoặc không phản hồi | Trả về | SS01-WB2-FR2 (toán hạng 2) | - |
| SS01-WB2-M14 | 14 | SS01-WB2-L03 | SS01-WB2-L01 | RefundApiResponse (status hoặc Unknown) | Trả về | SS01-WB2-FR2 (toán hạng 2) | - |
| SS01-WB2-M15 | 15 | SS01-WB2-L01 | SS01-WB2-L02 | toRefundResult(refundApiResponse) | Đồng bộ | - | Chuyển định dạng ngoài sang kiểu của interface |
| SS01-WB2-M16 | 16 | SS01-WB2-L02 | SS01-WB2-L01 | RefundResult | Trả về | - | - |
| SS01-WB2-M17 | 17 | SS01-WB2-L01 | SS01-WB2-L01 | writeAuditLog(requestKey, status) | Tự gọi | - | Cơ chế ghi nhật ký (P09), không ghi dữ liệu thẻ (NFR-03) |
| SS01-WB2-M18 | 18 | SS01-WB2-L01 | SS01-WB2-G1-3 | RefundResult | Trả về | - | - |

#### Trang "Hộp trắng - receivePaymentResult"

UC hoặc operation: UC-003

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-WB3-FRM | Fragment | sd receivePaymentResult | - | - | Khung sơ đồ của operation | 20 | 20 | 580 | 610 |
| SS01-WB3-L01 | Lifeline | :DC-PaymentCallbackReceiver | «adapter» | - | Lớp giao tiếp ngoài, nhận thông báo từ cổng | 120 | 40 | 120 | 550 |
| SS01-WB3-L02 | Lifeline | :DC-PaymentDataConverter | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 550 |
| SS01-WB3-L03 | Actor | Cổng thanh toán | «ACT-06» | - | Hệ thống ngoài | 440 | 40 | 120 | 550 |
| SS01-WB3-G1 | Gate | receivePaymentResult | - | SS01-WB3-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 410 | 20 | 20 |
| SS01-WB3-G1-2 | Gate | receivePaymentResult | - | SS01-WB3-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 450 | 20 | 20 |
| SS01-WB3-FR1 | Fragment | alt [chữ ký không hợp lệ] | alt | - | Thông báo giả mạo bị chặn trong subsystem | 110 | 200 | 460 | 320 |
| SS01-WB3-FR1-O2 | Fragment | [chữ ký hợp lệ] | alt | SS01-WB3-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS01-WB3-FR1-SEP2 | 120 | 310 | 440 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-WB3-M01 | 1 | SS01-WB3-L03 | SS01-WB3-L01 | onPaymentNotification(rawPayload) | Bất đồng bộ | - | Cổng gửi kết quả thanh toán |
| SS01-WB3-M02 | 2 | SS01-WB3-L01 | SS01-WB3-L01 | verifySignature(rawPayload) | Tự gọi | - | Cơ chế bảo mật (P09) |
| SS01-WB3-M03 | 3 | SS01-WB3-L01 | SS01-WB3-L01 | writeAuditLog(từ chối thông báo) | Tự gọi | SS01-WB3-FR1 (toán hạng 1) | Không gọi IF-02 |
| SS01-WB3-M04 | 4 | SS01-WB3-L01 | SS01-WB3-L03 | phản hồi từ chối | Trả về | SS01-WB3-FR1 (toán hạng 1) | Thông báo không tin cậy |
| SS01-WB3-M05 | 5 | SS01-WB3-L01 | SS01-WB3-L02 | toPaymentNotification(rawPayload) | Đồng bộ | SS01-WB3-FR1 (toán hạng 2) | - |
| SS01-WB3-M06 | 6 | SS01-WB3-L02 | SS01-WB3-L01 | PaymentNotification(requestKey, outcome, paymentReference, amount) | Trả về | SS01-WB3-FR1 (toán hạng 2) | - |
| SS01-WB3-M07 | 7 | SS01-WB3-L01 | SS01-WB3-G1 | receivePaymentResult(requestKey, outcome, paymentReference, amount) | Đồng bộ | SS01-WB3-FR1 (toán hạng 2) | IF-02 do DC-PayTicketOnlineService hiện thực |
| SS01-WB3-M08 | 8 | SS01-WB3-G1-2 | SS01-WB3-L01 | xác nhận đã ghi nhận | Trả về | SS01-WB3-FR1 (toán hạng 2) | - |
| SS01-WB3-M09 | 9 | SS01-WB3-L01 | SS01-WB3-L03 | xác nhận đã nhận | Trả về | SS01-WB3-FR1 (toán hạng 2) | - |

#### Trang "Hộp trắng - queryRefundStatus"

UC hoặc operation: UC-008, UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-WB4-FRM | Fragment | sd queryRefundStatus | - | - | Khung sơ đồ của operation | 20 | 20 | 580 | 410 |
| SS01-WB4-L01 | Lifeline | :DC-PaymentGatewayService | «control» | - | Lớp điều phối, hiện thực IF-01 | 120 | 40 | 120 | 350 |
| SS01-WB4-L02 | Lifeline | :DC-PaymentGatewayClient | «adapter» | - | Lớp giao tiếp ngoài | 280 | 40 | 120 | 350 |
| SS01-WB4-L03 | Actor | Cổng thanh toán | «ACT-06» | - | Hệ thống ngoài | 440 | 40 | 120 | 350 |
| SS01-WB4-G1 | Gate | queryRefundStatus | - | SS01-WB4-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS01-WB4-G1-2 | Gate | queryRefundStatus | - | SS01-WB4-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 310 | 20 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-WB4-M01 | 1 | SS01-WB4-G1 | SS01-WB4-L01 | queryRefundStatus(requestKey) | Đồng bộ | - | Tra cứu khi đối soát |
| SS01-WB4-M02 | 2 | SS01-WB4-L01 | SS01-WB4-L02 | getRefundStatus(requestKey) | Đồng bộ | - | - |
| SS01-WB4-M03 | 3 | SS01-WB4-L02 | SS01-WB4-L03 | queryRefundStatus(requestKey) | Đồng bộ | - | - |
| SS01-WB4-M04 | 4 | SS01-WB4-L03 | SS01-WB4-L02 | kết quả tra cứu | Trả về | - | - |
| SS01-WB4-M05 | 5 | SS01-WB4-L02 | SS01-WB4-L01 | RefundApiResponse | Trả về | - | - |
| SS01-WB4-M06 | 6 | SS01-WB4-L01 | SS01-WB4-G1-2 | RefundResult | Trả về | - | Chuyển đổi qua DC-PaymentDataConverter.toRefundResult |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-PaymentGatewayService | PaymentGatewayService | Điều phối | Nhận lời gọi IF-01, điều khiển chuyển đổi, gọi cổng, xử lý timeout và tra cứu một lần, ghi nhật ký | package-private | IF-01 |
| DC-PaymentGatewayClient | PaymentGatewayClient | Giao tiếp ngoài | Nói chuyện với API thanh toán và hoàn tiền của cổng: kết nối, xác thực, timeout, bulkhead 20 kết nối đồng thời và ngắt mạch sau 5 lỗi liên tiếp trong 30 giây (Thiết kế: cô lập lỗi cổng khỏi các luồng khác, NFR-01); cấu hình điểm cuối và khoá lấy từ cơ chế cấu hình (P09) | package-private | - |
| DC-PaymentDataConverter | PaymentDataConverter | Chuyển đổi dữ liệu | Chuyển giữa Money, TicketCode, PaymentReference và định dạng của API cổng; chuyển mã lỗi của cổng sang giá trị của interface | package-private | - |
| DC-PaymentCallbackReceiver | PaymentCallbackReceiver | Giao tiếp ngoài | Nhận thông báo kết quả thanh toán từ cổng, kiểm tra chữ ký, gọi IF-02 | package-private | - |
| DC-PaymentRequestResult | PaymentRequestResult | Kiểu dữ liệu | Kết quả của requestPayment (status, redirectTarget) | public (thuộc chữ ký IF-01) | - |
| DC-PaymentStatusResult | PaymentStatusResult | Kiểu dữ liệu | Kết quả của queryPaymentStatus | public (thuộc chữ ký IF-01) | - |
| DC-RefundResult | RefundResult | Kiểu dữ liệu | Kết quả của requestRefund, queryRefundStatus (status, refundReference) | public (thuộc chữ ký IF-01) | - |
| DC-PaymentOutcome | PaymentOutcome | Kiểu dữ liệu | Giá trị Succeeded / Failed của IF-02 | public (thuộc chữ ký IF-02) | - |
| DC-PaymentGatewayUnavailableException | PaymentGatewayUnavailableException | Ngoại lệ | Lỗi kỹ thuật tạm thời của cổng đã được che giao thức | public (thuộc chữ ký IF-01) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-01 | Subsystem | SS-01 OnlinePayment | «subsystem» | - | - | 160 | 230 | 480 | 280 |
| IF-01 | Interface | IF-01 IPaymentGateway | «interface» | PKG-15 | - | 180 | 40 | 200 | 130 |
| IF-02 | Interface | IF-02 IPaymentResultListener | «interface» | PKG-15 | - | 420 | 40 | 200 | 70 |
| DC-PaymentGatewayService | Class | DC-PaymentGatewayService | «control» | SS-01 | - | 180 | 270 | 200 | 70 |
| DC-PaymentCallbackReceiver | Class | DC-PaymentCallbackReceiver | «adapter» | SS-01 | - | 420 | 270 | 200 | 70 |
| DC-PaymentDataConverter | Class | DC-PaymentDataConverter | «converter» | SS-01 | - | 180 | 420 | 200 | 70 |
| DC-PaymentGatewayClient | Class | DC-PaymentGatewayClient | «adapter» | SS-01 | - | 420 | 420 | 200 | 70 |
| ACT-06 | Actor | Cổng thanh toán (ACT-06) | - | - | - | 680 | 420 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS01-EL-E01 | DC-PaymentGatewayService | IF-01 | Realization | - | Subsystem hiện thực IF-01 qua lớp điều phối | - |
| SS01-EL-E02 | DC-PaymentCallbackReceiver | IF-02 | Dependency | gọi | Gọi ngược lên bên hiện thực IF-02 | - |
| SS01-EL-E03 | DC-PaymentGatewayService | DC-PaymentDataConverter | Association (điều hướng) | dùng | - | - |
| SS01-EL-E04 | DC-PaymentGatewayService | DC-PaymentGatewayClient | Association (điều hướng) | dùng | - | (290,370); (520,370) |
| SS01-EL-E05 | DC-PaymentCallbackReceiver | DC-PaymentDataConverter | Association (điều hướng) | dùng | - | (510,380); (290,380) |
| SS01-EL-E06 | DC-PaymentGatewayClient | ACT-06 | Association | API ngoài | - | - |
| SS01-EL-E07 | ACT-06 | DC-PaymentCallbackReceiver | Association (điều hướng) | thông báo | Cổng gửi kết quả thanh toán vào subsystem | (780,390); (530,390) |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-01 | IF-02 | Qua interface | Gọi ngược kết quả thanh toán lên layer trên theo P09 R5 | Ưu tiên |
| SS-01 | PKG-28 | Vào package | Money, TicketCode, PaymentReference có trong chữ ký IF-01, IF-02; kiểu giá trị bất biến ở layer thấp nhất, không kéo phụ thuộc lên | Dùng thận trọng |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-09 | Package | PKG-09 TicketSalesService | - | - | - | 60 | 40 | 200 | 60 |
| PKG-10 | Package | PKG-10 TripOperationsService | - | - | - | 300 | 40 | 200 | 60 |
| IF-01 | Interface | IF-01 IPaymentGateway | «interface» | - | - | 60 | 170 | 200 | 50 |
| IF-02 | Interface | IF-02 IPaymentResultListener | «interface» | - | - | 300 | 170 | 200 | 50 |
| SS-01 | Subsystem | SS-01 OnlinePayment | - | - | - | 180 | 280 | 200 | 60 |
| PKG-28 | Package | PKG-28 SharedValueTypes | - | - | - | 180 | 390 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS01-DP-E01 | PKG-09 | IF-01 | Dependency | dùng | - | - |
| SS01-DP-E02 | PKG-10 | IF-01 | Dependency | dùng | - | (400,130); (170,130) |
| SS01-DP-E03 | PKG-09 | IF-02 | Realization | DC-PayTicketOnlineService | - | (170,140); (400,140) |
| SS01-DP-E04 | SS-01 | IF-01 | Realization | - | - | (270,240); (160,240) |
| SS01-DP-E05 | SS-01 | IF-02 | Dependency | gọi ngược | - | (290,250); (400,250) |
| SS01-DP-E06 | SS-01 | PKG-28 | Dependency | kiểu giá trị | - | - |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| requestPayment | Không kết nối được cổng (trước khi gửi) | Kỹ thuật tạm thời | Lỗi kết nối hoặc hết thời gian kết nối 5 giây | Không thử lại; ngắt mạch sau 5 lỗi liên tiếp | PaymentGatewayUnavailableException | UC-002 10a (tạm; P04 UC-003 chưa có) | Q-55 |
| requestPayment | Cổng từ chối yêu cầu | Nghiệp vụ | Mã từ chối của cổng | Chuyển thành status Rejected | PaymentRequestResult(Rejected) | UC-002 10a (tạm) | Q-55 |
| requestPayment | Hết thời gian chờ sau khi đã gửi | Không rõ kết quả | Hết thời gian đọc 30 giây | Không gửi lại yêu cầu; tra cứu bằng requestKey tối đa 1 lần nếu cổng hỗ trợ | PaymentRequestResult(Unknown) nếu vẫn chưa rõ | Không có (P04 UC-003 chưa có) | Q-55, Q-100 |
| receivePaymentResult | Chữ ký thông báo không hợp lệ | Kỹ thuật (bảo mật) | verifySignature thất bại | Bỏ qua thông báo, ghi nhật ký, từ chối với cổng, không gọi IF-02 | Không gọi IF-02 | Không có luồng nghiệp vụ | - |
| receivePaymentResult | Thông báo đến muộn sau hết thời hạn giữ chỗ hoặc gửi lặp | Nghiệp vụ | Bên hiện thực IF-02 kiểm tra trạng thái lần đặt | SS-01 chuyển nguyên thông báo, không lọc | Bên hiện thực quyết định, xử lý idempotent theo requestKey | UC-002 9a (kết quả đến sau khi trả chỗ chờ Q-10) | Q-10 |
| requestRefund | Không kết nối được cổng (trước khi gửi) | Kỹ thuật tạm thời | Lỗi kết nối hoặc hết thời gian kết nối 5 giây | Không thử lại tự động (operation có tác dụng phụ tài chính, không idempotent) | PaymentGatewayUnavailableException | UC-008 9a, UC-013 8a (tạm ánh xạ; P04 chưa phân biệt lỗi kỹ thuật) | Q-55 |
| requestRefund | Cổng từ chối hoàn | Nghiệp vụ | Mã từ chối của cổng | Chuyển thành status Declined | RefundResult(Declined) | UC-008 9a, UC-013 8a | Q-37, Q-43 |
| requestRefund | Hết thời gian chờ sau khi đã gửi | Không rõ kết quả | Hết thời gian đọc 30 giây | Không thử lại; gọi queryRefundStatus bằng requestKey tối đa 1 lần; vẫn chưa rõ thì trả Unknown | RefundResult(Unknown) | Không có (UC-008, UC-013 chưa có luồng kết quả không rõ) | Q-55, Q-100; Đề xuất sửa P04 |
| queryRefundStatus, queryPaymentStatus | Cổng không hỗ trợ tra cứu hoặc không phản hồi | Không rõ kết quả | Hết thời gian 10 giây hoặc mã không hỗ trợ | Không thử lại | Status Unknown / PaymentGatewayUnavailableException | Không có | Q-100 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-01 (E01 trang Phần tử) |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: IF-02 (E02 trang Phần tử, E05 trang Phụ thuộc) |
| Không phần tử bên trong subsystem nào public | Đạt: lớp bên trong package-private; kiểu và ngoại lệ public thuộc chữ ký interface, ghi ở F5a |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt: 4 trang hộp trắng, queryPaymentStatus 1-1 |

## SS-02 SmsDelivery

Package chứa: PKG-16. Tác nhân hoặc đối tượng ngoài: ACT-07.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-002 Đặt vé trực tuyến | AC-C-BookTicketOnlineController (DC-BookTicketOnlineService) | SD1: 3.1.13 // sendTicketSms --> P08 // sendSms; 3.1.13.1 // deliverSms (trong loop từng vé) | nội dung SMS của vé, số điện thoại người đi | Chưa có luồng khi cổng không nhận hoặc báo lỗi (Q-56) |
| UC-013 Huỷ chuyến | AC-C-CancelTripController (DC-CancelTripService) | SD1: 2.1.8 // sendTripCancelSms --> P08 // sendSms; 2.1.8.1 // deliverSms (trong loop từng vé) | nội dung tin nhắn báo huỷ chuyến, số điện thoại người đi | Chưa có luồng khi cổng không nhận hoặc báo lỗi (Q-56) |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-03 | ISmsSender | Gửi một tin nhắn tới số điện thoại người đi qua cổng SMS của nhà mạng | SS-02 | DC-BookTicketOnlineService (PKG-09), DC-CancelTripService (PKG-10) | PKG-16 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-03 | ISmsSender | Cổng SMS (ACT-07) | sendSms(recipient: PhoneNumber, content: String, messageKey: String): SmsResult | recipient: PhoneNumber - số di động người đi, đã hợp lệ theo ASM-15<br>content: String - không rỗng, do Ticket lập (DC-TicketSmsContent); độ dài tối đa theo giới hạn của cổng<br>messageKey: String - khoá do hệ thống sinh từ mã vé và loại tin (vé / báo huỷ chuyến), ổn định giữa các lần gửi lại | SmsResult: status (Accepted / Rejected / Unknown), rejectReason (InvalidPhoneNumber / Other, khi Rejected), providerMessageId (khi Accepted) | InvalidPhoneNumber (Nghiệp vụ, qua Rejected); SmsGatewayUnavailableException (Kỹ thuật tạm thời, sau khi hết số lần thử lại); Unknown (Không rõ kết quả, qua status) | UC-002 (bước 12, SD1 3.1.13); UC-013 (bước 10, SD1 2.1.8). Thay cho // sendSms (gộp sendTicketSms và sendTripCancelSms theo P08) | Nội dung tin đã lập; số điện thoại người đi có giá trị | Cổng đã tiếp nhận tin để chuyển tới thuê bao khi status là Accepted (việc chuyển tới thuê bao do cổng đảm nhận, NFR-08) | Đồng bộ (theo P07; khối lượng lớn xem Vấn đề còn mở) | Có với khoá messageKey nếu cổng hỗ trợ (Q-101); thử lại tự động chỉ cho lỗi kỹ thuật tạm thời xảy ra trước khi cổng nhận yêu cầu | 10 giây mỗi lần; tối đa 2 lần thử lại cách nhau 5 giây (Thiết kế: gửi SMS nằm trong luồng đồng bộ của UC-002 và UC-013 nên không chặn người dùng lâu; mặc định phổ biến của API REST nhà mạng; tin trùng có tác hại thấp, khác giao dịch tiền) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-02.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

Mọi operation của IF-03 (một operation) có trang hộp trắng.

#### Trang "Hộp đen - UC-002 sendSms"

UC hoặc operation: UC-002

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS02-BB1-L01 | Lifeline | :DC-BookTicketOnlineService | «control» | - | Control của UC-002 (AC-C-BookTicketOnlineController) | 40 | 40 | 120 | 620 |
| SS02-BB1-L02 | Lifeline | :IF-03 ISmsSender | «interface» | - | Interface của SS-02 | 200 | 40 | 120 | 620 |
| SS02-BB1-FR1 | Fragment | loop [với từng vé đã phát hành (ASM-13)] | loop | - | Mỗi vé một SMS | 30 | 120 | 300 | 470 |
| SS02-BB1-FR2 | Fragment | alt [status = Accepted] | alt | - | Mỗi toán hạng là một kết quả của sendSms | 40 | 190 | 280 | 380 |
| SS02-BB1-FR2-O2 | Fragment | [status = Rejected] | alt | SS02-BB1-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS02-BB1-FR2-SEP2 | 50 | 260 | 260 | 20 |
| SS02-BB1-FR2-O3 | Fragment | [status = Unknown] | alt | SS02-BB1-FR2 | Toán hạng 3, ngăn bởi đường nét đứt SS02-BB1-FR2-SEP3 | 50 | 370 | 260 | 20 |
| SS02-BB1-FR2-O4 | Fragment | [SmsGatewayUnavailableException] | alt | SS02-BB1-FR2 | Toán hạng 4, ngăn bởi đường nét đứt SS02-BB1-FR2-SEP4 | 50 | 480 | 260 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS02-BB1-M01 | 1 | SS02-BB1-L01 | SS02-BB1-L02 | sendSms(recipient, content, messageKey) | Đồng bộ | SS02-BB1-FR1 (toán hạng 1) | UC-002 bước 12 |
| SS02-BB1-M02 | 2 | SS02-BB1-L02 | SS02-BB1-L01 | SmsResult(status = Accepted) | Trả về | SS02-BB1-FR2 (toán hạng 1) | UC-002 bước 12 |
| SS02-BB1-M03 | 3 | SS02-BB1-L02 | SS02-BB1-L01 | SmsResult(status = Rejected, InvalidPhoneNumber) | Trả về | SS02-BB1-FR2 (toán hạng 2) | UC-002 bước 12 |
| SS02-BB1-M04 | 4 | SS02-BB1-L01 | SS02-BB1-L01 | chưa có luồng P04 (Q-56) | Tự gọi | SS02-BB1-FR2 (toán hạng 2) | Q-56 |
| SS02-BB1-M05 | 5 | SS02-BB1-L02 | SS02-BB1-L01 | SmsResult(status = Unknown) | Trả về | SS02-BB1-FR2 (toán hạng 3) | UC-002 bước 12 |
| SS02-BB1-M06 | 6 | SS02-BB1-L01 | SS02-BB1-L01 | chưa có luồng P04 (Q-56) | Tự gọi | SS02-BB1-FR2 (toán hạng 3) | Q-56 |
| SS02-BB1-M07 | 7 | SS02-BB1-L02 | SS02-BB1-L01 | SmsGatewayUnavailableException | Trả về | SS02-BB1-FR2 (toán hạng 4) | UC-002 bước 12 |
| SS02-BB1-M08 | 8 | SS02-BB1-L01 | SS02-BB1-L01 | chưa có luồng P04 (Q-56) | Tự gọi | SS02-BB1-FR2 (toán hạng 4) | Q-56 |

#### Trang "Hộp đen - UC-013 sendSms"

UC hoặc operation: UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS02-BB2-L01 | Lifeline | :DC-CancelTripService | «control» | - | Control của UC-013 (AC-C-CancelTripController) | 40 | 40 | 120 | 510 |
| SS02-BB2-L02 | Lifeline | :IF-03 ISmsSender | «interface» | - | Interface của SS-02 | 200 | 40 | 120 | 510 |
| SS02-BB2-FR1 | Fragment | loop [với từng vé đã huỷ (BR-18, ASM-29)] | loop | - | Mỗi vé một tin nhắn | 30 | 120 | 300 | 360 |
| SS02-BB2-FR2 | Fragment | alt [status = Accepted] | alt | - | Mỗi toán hạng là một kết quả của sendSms | 40 | 190 | 280 | 270 |
| SS02-BB2-FR2-O2 | Fragment | [status = Rejected hoặc Unknown] | alt | SS02-BB2-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS02-BB2-FR2-SEP2 | 50 | 260 | 260 | 20 |
| SS02-BB2-FR2-O3 | Fragment | [SmsGatewayUnavailableException] | alt | SS02-BB2-FR2 | Toán hạng 3, ngăn bởi đường nét đứt SS02-BB2-FR2-SEP3 | 50 | 370 | 260 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS02-BB2-M01 | 1 | SS02-BB2-L01 | SS02-BB2-L02 | sendSms(recipient, content, messageKey) | Đồng bộ | SS02-BB2-FR1 (toán hạng 1) | UC-013 bước 10 |
| SS02-BB2-M02 | 2 | SS02-BB2-L02 | SS02-BB2-L01 | SmsResult(status = Accepted) | Trả về | SS02-BB2-FR2 (toán hạng 1) | UC-013 bước 10 |
| SS02-BB2-M03 | 3 | SS02-BB2-L02 | SS02-BB2-L01 | SmsResult(status = Rejected hoặc Unknown) | Trả về | SS02-BB2-FR2 (toán hạng 2) | UC-013 bước 10 |
| SS02-BB2-M04 | 4 | SS02-BB2-L01 | SS02-BB2-L01 | chưa có luồng P04 (Q-56) | Tự gọi | SS02-BB2-FR2 (toán hạng 2) | Q-56 |
| SS02-BB2-M05 | 5 | SS02-BB2-L02 | SS02-BB2-L01 | SmsGatewayUnavailableException | Trả về | SS02-BB2-FR2 (toán hạng 3) | UC-013 bước 10 |
| SS02-BB2-M06 | 6 | SS02-BB2-L01 | SS02-BB2-L01 | chưa có luồng P04 (Q-56) | Tự gọi | SS02-BB2-FR2 (toán hạng 3) | Q-56 |

#### Trang "Hộp trắng - sendSms"

UC hoặc operation: UC-002, UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS02-WB1-FRM | Fragment | sd sendSms | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 930 |
| SS02-WB1-L01 | Lifeline | :DC-SmsSenderService | «control» | - | Lớp điều phối, hiện thực IF-03 | 120 | 40 | 120 | 870 |
| SS02-WB1-L02 | Lifeline | :DC-SmsPayloadConverter | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 870 |
| SS02-WB1-L03 | Lifeline | :DC-SmsGatewayClient | «adapter» | - | Lớp giao tiếp ngoài | 440 | 40 | 120 | 870 |
| SS02-WB1-L04 | Actor | Cổng SMS | «ACT-07» | - | Hệ thống ngoài | 600 | 40 | 120 | 870 |
| SS02-WB1-G1 | Gate | sendSms | - | SS02-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS02-WB1-G1-2 | Gate | sendSms | - | SS02-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 650 | 20 | 20 |
| SS02-WB1-G1-3 | Gate | sendSms | - | SS02-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 830 | 20 | 20 |
| SS02-WB1-FR1 | Fragment | loop [lỗi kỹ thuật tạm thời, chưa quá 2 lần thử lại] | loop | - | Thử lại có giới hạn | 110 | 360 | 460 | 90 |
| SS02-WB1-FR2 | Fragment | alt [cổng có phản hồi] | alt | - | Phân loại kết quả sau lần thử cuối | 110 | 490 | 460 | 190 |
| SS02-WB1-FR2-O2 | Fragment | [hết thời gian chờ sau khi đã gửi] | alt | SS02-WB1-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS02-WB1-FR2-SEP2 | 120 | 560 | 440 | 20 |
| SS02-WB1-FR2-O3 | Fragment | [hết số lần thử lại] | alt | SS02-WB1-FR2 | Toán hạng 3, ngăn bởi đường nét đứt SS02-WB1-FR2-SEP3 | 120 | 630 | 440 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS02-WB1-M01 | 1 | SS02-WB1-G1 | SS02-WB1-L01 | sendSms(recipient, content, messageKey) | Đồng bộ | - | UC-002 bước 12 / UC-013 bước 10 |
| SS02-WB1-M02 | 2 | SS02-WB1-L01 | SS02-WB1-L02 | toSmsApiRequest(recipient, content, messageKey) | Đồng bộ | - | Chuyển kiểu mô hình sang định dạng REST của cổng |
| SS02-WB1-M03 | 3 | SS02-WB1-L02 | SS02-WB1-L01 | SmsApiRequest | Trả về | - | - |
| SS02-WB1-M04 | 4 | SS02-WB1-L01 | SS02-WB1-L03 | post(smsApiRequest) | Đồng bộ | - | Lần thử 1 |
| SS02-WB1-M05 | 5 | SS02-WB1-L03 | SS02-WB1-L04 | deliverSms(smsApiRequest) | Đồng bộ | - | - |
| SS02-WB1-M06 | 6 | SS02-WB1-L04 | SS02-WB1-L03 | phản hồi của cổng | Trả về | - | - |
| SS02-WB1-M07 | 7 | SS02-WB1-L03 | SS02-WB1-L01 | ConnectionFailed hoặc ServiceBusy (cổng chưa nhận yêu cầu) | Trả về | SS02-WB1-FR1 (toán hạng 1) | Lỗi kỹ thuật tạm thời |
| SS02-WB1-M08 | 8 | SS02-WB1-L01 | SS02-WB1-L03 | post(smsApiRequest) sau 5 giây | Đồng bộ | SS02-WB1-FR1 (toán hạng 1) | Tối đa 2 lần thử lại |
| SS02-WB1-M09 | 9 | SS02-WB1-L03 | SS02-WB1-L01 | SmsApiResponse | Trả về | SS02-WB1-FR2 (toán hạng 1) | - |
| SS02-WB1-M10 | 10 | SS02-WB1-L03 | SS02-WB1-L01 | ResponseTimeout (đã gửi, chưa có phản hồi) | Trả về | SS02-WB1-FR2 (toán hạng 2) | Kết quả không rõ, không thử lại |
| SS02-WB1-M11 | 11 | SS02-WB1-L01 | SS02-WB1-G1-2 | SmsGatewayUnavailableException | Trả về | SS02-WB1-FR2 (toán hạng 3) | Hết số lần thử lại |
| SS02-WB1-M12 | 12 | SS02-WB1-L01 | SS02-WB1-L02 | toSmsResult(smsApiResponse) | Đồng bộ | - | Chuyển mã phản hồi của cổng sang SmsResult |
| SS02-WB1-M13 | 13 | SS02-WB1-L02 | SS02-WB1-L01 | SmsResult | Trả về | - | - |
| SS02-WB1-M14 | 14 | SS02-WB1-L01 | SS02-WB1-L01 | writeAuditLog(messageKey, status) | Tự gọi | - | Cơ chế ghi nhật ký (P09), che bớt số điện thoại |
| SS02-WB1-M15 | 15 | SS02-WB1-L01 | SS02-WB1-G1-3 | SmsResult | Trả về | - | - |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-SmsSenderService | SmsSenderService | Điều phối | Nhận lời gọi IF-03, thử lại có giới hạn lỗi kỹ thuật tạm thời, phân loại kết quả, ghi nhật ký | package-private | IF-03 |
| DC-SmsGatewayClient | SmsGatewayClient | Giao tiếp ngoài | Gọi API REST của cổng SMS: kết nối, xác thực, timeout; bulkhead 10 kết nối đồng thời (Thiết kế: cổng SMS chậm không được chiếm hết luồng của luồng bán vé) | package-private | - |
| DC-SmsPayloadConverter | SmsPayloadConverter | Chuyển đổi dữ liệu | Chuyển PhoneNumber, nội dung, messageKey sang định dạng REST của cổng; chuyển mã phản hồi sang SmsResult | package-private | - |
| DC-SmsResult | SmsResult | Kiểu dữ liệu | Kết quả của sendSms (status, rejectReason, providerMessageId) | public (thuộc chữ ký IF-03) | - |
| DC-SmsGatewayUnavailableException | SmsGatewayUnavailableException | Ngoại lệ | Lỗi kỹ thuật tạm thời của cổng đã che giao thức | public (thuộc chữ ký IF-03) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-02 | Subsystem | SS-02 SmsDelivery | «subsystem» | - | - | 40 | 160 | 480 | 260 |
| IF-03 | Interface | IF-03 ISmsSender | «interface» | PKG-16 | - | 300 | 40 | 200 | 70 |
| DC-SmsSenderService | Class | DC-SmsSenderService | «control» | SS-02 | - | 300 | 200 | 200 | 70 |
| DC-SmsPayloadConverter | Class | DC-SmsPayloadConverter | «converter» | SS-02 | - | 60 | 330 | 200 | 70 |
| DC-SmsGatewayClient | Class | DC-SmsGatewayClient | «adapter» | SS-02 | - | 300 | 330 | 200 | 70 |
| ACT-07 | Actor | Cổng SMS (ACT-07) | - | - | - | 560 | 330 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS02-EL-E01 | DC-SmsSenderService | IF-03 | Realization | - | Subsystem hiện thực IF-03 qua lớp điều phối | - |
| SS02-EL-E02 | DC-SmsSenderService | DC-SmsPayloadConverter | Association (điều hướng) | dùng | - | (390,290); (160,290) |
| SS02-EL-E03 | DC-SmsSenderService | DC-SmsGatewayClient | Association (điều hướng) | dùng | - | (410,300); (400,300) |
| SS02-EL-E04 | DC-SmsGatewayClient | ACT-07 | Association | REST | - | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-02 | PKG-28 | Vào package | PhoneNumber có trong chữ ký IF-03; kiểu giá trị ở layer thấp nhất | Dùng thận trọng |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-09 | Package | PKG-09 TicketSalesService | - | - | - | 60 | 40 | 200 | 60 |
| PKG-10 | Package | PKG-10 TripOperationsService | - | - | - | 300 | 40 | 200 | 60 |
| IF-03 | Interface | IF-03 ISmsSender | «interface» | - | - | 180 | 160 | 200 | 50 |
| SS-02 | Subsystem | SS-02 SmsDelivery | - | - | - | 180 | 260 | 200 | 60 |
| PKG-28 | Package | PKG-28 SharedValueTypes | - | - | - | 180 | 370 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS02-DP-E01 | PKG-09 | IF-03 | Dependency | dùng | - | (160,120); (270,120) |
| SS02-DP-E02 | PKG-10 | IF-03 | Dependency | dùng | - | (400,130); (290,130) |
| SS02-DP-E03 | SS-02 | IF-03 | Realization | - | - | - |
| SS02-DP-E04 | SS-02 | PKG-28 | Dependency | PhoneNumber | - | - |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| sendSms | Số điện thoại bị cổng từ chối | Nghiệp vụ | Mã từ chối của cổng | Không thử lại | SmsResult(Rejected, InvalidPhoneNumber) | Không có (UC-002 bước 12, UC-013 bước 10 chưa có luồng) | Q-56 |
| sendSms | Mất kết nối hoặc cổng quá tải, cổng chưa nhận yêu cầu | Kỹ thuật tạm thời | Lỗi kết nối, mã dịch vụ bận | Thử lại tối đa 2 lần cách nhau 5 giây (an toàn vì cổng chưa nhận yêu cầu); hết lần thì ném ngoại lệ | SmsGatewayUnavailableException | Không có | Q-56 |
| sendSms | Hết thời gian chờ sau khi đã gửi | Không rõ kết quả | Hết thời gian đọc 10 giây | Không thử lại (tránh gửi trùng khi cổng chưa hỗ trợ khoá messageKey) | SmsResult(Unknown) | Không có | Q-56, Q-101 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-03 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: không dùng interface nào |
| Không phần tử bên trong subsystem nào public | Đạt |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt |

## SS-03 BarcodeReading

Package chứa: PKG-18. Tác nhân hoặc đối tượng ngoài: ACT-09.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-015 Soát vé lên xe | AC-C-CheckBoardingTicketController (DC-CheckBoardingTicketService) | SD1: 2 // readBarcode (ACT-09 --> BarcodeScanner), 2.1 // checkTicket (BarcodeScanner --> control); ASM-53 | mã vé đọc từ mã vạch | Bước 5a, 5b, 5c xử lý mã vé hợp lệ về định dạng. Lỗi đọc, mã sai định dạng, đầu quét mất kết nối: P04 chưa có luồng (Q-103) |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-04 | IBarcodeReader | Bật và tắt đầu quét mã vạch của máy soát vé | SS-03 | DC-CheckBoardingTicketService (PKG-11) | PKG-18 |
| IF-05 | IBarcodeReadListener | Nhận mã vé và lỗi đọc do đầu quét đẩy vào (chiều ngược): bên cung cấp DC-CheckBoardingTicketService (PKG-11), bên dùng SS-03 | DC-CheckBoardingTicketService (PKG-11), hiện thực ở layer trên | SS-03 | PKG-18 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-04 | IBarcodeReader | Đầu quét mã vạch (ACT-09) | startScanning(listener: IBarcodeReadListener): void | listener: IBarcodeReadListener - bên nhận mã vé và lỗi đọc, không rỗng | void | ScannerUnavailableException (Thiết bị) | UC-015 (bước 2: mở phiên soát vé; operation kỹ thuật vì đầu quét chỉ đẩy sự kiện sau khi có bộ nhận, P10 F2 "đăng ký bộ nhận") | Phiên soát vé đã mở | Đầu quét sẵn sàng; mã đọc được sẽ gọi listener | Đồng bộ | Có (đăng ký lại cùng bộ nhận không đổi trạng thái) | 5 giây (Thiết kế: khởi tạo SDK hoặc kênh nhập của đầu quét trên máy) |
| IF-04 | IBarcodeReader | Đầu quét mã vạch (ACT-09) | stopScanning(): void | - | void | - | UC-015 (bước 9, 10: kết thúc soát vé; operation kỹ thuật, giải phóng đầu quét) | Đã gọi startScanning | Đầu quét không còn gọi listener | Đồng bộ | Có | 5 giây (Thiết kế: như startScanning) |
| IF-05 | IBarcodeReadListener | Đầu quét mã vạch (ACT-09), gọi ngược | receiveScannedCode(code: TicketCode): void | code: TicketCode - mã vé đã chuẩn hoá từ chuỗi đọc được, đúng định dạng mã vé | void | - | UC-015 (bước 4: đầu quét đọc mã vạch và chuyển mã vé; SD1 message 2 // readBarcode, 2.1 // checkTicket). Thay cho // readBarcode của AC-B-BarcodeScanner | startScanning đã gọi và chưa gọi stopScanning | Bên hiện thực đã nhận mã vé một lần cho mỗi lần quét | Bất đồng bộ (đầu quét đẩy sự kiện; do phía thiết bị gọi vào) | Không (mỗi lần quét là một sự kiện; quét lặp được xử lý bằng BR-22 ở bên hiện thực) | - |
| IF-05 | IBarcodeReadListener | Đầu quét mã vạch (ACT-09), gọi ngược | receiveScanError(error: ScanError): void | error: ScanError - loại lỗi (ReadFailed / InvalidCodeFormat / DeviceDisconnected) | void | - | UC-015 (bước 4; lỗi thiết bị, P04 chưa có luồng, Q-103) | startScanning đã gọi | Bên hiện thực đã nhận lỗi đọc một lần cho mỗi lần lỗi | Bất đồng bộ (do phía thiết bị gọi vào) | Không | - |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-03.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

stopScanning: ánh xạ 1-1, DC-BarcodeReaderService xoá bộ nhận rồi DC-ScannerInputAdapter tắt đầu quét, không rẽ nhánh. receiveScanError nằm trong trang "Hộp trắng - receiveScannedCode" (nhánh lỗi).

#### Trang "Hộp đen - UC-015 quét vé"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS03-BB1-L01 | Lifeline | :DC-CheckBoardingTicketService | «control» | - | Control của UC-015 (AC-C-CheckBoardingTicketController), hiện thực IF-05 | 40 | 40 | 120 | 480 |
| SS03-BB1-L02 | Lifeline | :IF-04 IBarcodeReader | «interface» | - | Interface của SS-03 | 200 | 40 | 120 | 480 |
| SS03-BB1-FR1 | Fragment | loop [còn hành khách xuất trình vé (bước 8)] | loop | - | Vòng lặp bước 3 đến 8 | 30 | 160 | 300 | 250 |
| SS03-BB1-FR2 | Fragment | alt [đọc được mã vé] | alt | - | Hai kết quả của một lần quét | 40 | 190 | 280 | 200 |
| SS03-BB1-FR2-O2 | Fragment | [lỗi đọc hoặc lỗi thiết bị] | alt | SS03-BB1-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS03-BB1-FR2-SEP2 | 50 | 300 | 260 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS03-BB1-M01 | 1 | SS03-BB1-L01 | SS03-BB1-L02 | startScanning(listener) | Đồng bộ | - | UC-015 bước 2 |
| SS03-BB1-M02 | 2 | SS03-BB1-L02 | SS03-BB1-L01 | receiveScannedCode(code) | Bất đồng bộ | SS03-BB1-FR2 (toán hạng 1) | UC-015 bước 4, IF-05 |
| SS03-BB1-M03 | 3 | SS03-BB1-L01 | SS03-BB1-L01 | checkTicket(code) | Tự gọi | SS03-BB1-FR2 (toán hạng 1) | UC-015 bước 5 đến 7 |
| SS03-BB1-M04 | 4 | SS03-BB1-L02 | SS03-BB1-L01 | receiveScanError(error) | Bất đồng bộ | SS03-BB1-FR2 (toán hạng 2) | UC-015 bước 4, IF-05 |
| SS03-BB1-M05 | 5 | SS03-BB1-L01 | SS03-BB1-L01 | chưa có luồng P04 (Q-103) | Tự gọi | SS03-BB1-FR2 (toán hạng 2) | Q-103 |
| SS03-BB1-M06 | 6 | SS03-BB1-L01 | SS03-BB1-L02 | stopScanning() | Đồng bộ | - | UC-015 bước 9, 10 |

#### Trang "Hộp trắng - startScanning"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS03-WB1-FRM | Fragment | sd startScanning | - | - | Khung sơ đồ của operation | 20 | 20 | 580 | 620 |
| SS03-WB1-L01 | Lifeline | :DC-BarcodeReaderService | «control» | - | Lớp điều phối, hiện thực IF-04 | 120 | 40 | 120 | 560 |
| SS03-WB1-L02 | Lifeline | :DC-ScannerInputAdapter | «adapter» | - | Lớp giao tiếp thiết bị | 280 | 40 | 120 | 560 |
| SS03-WB1-L03 | Actor | Đầu quét mã vạch | «ACT-09» | - | Thiết bị | 440 | 40 | 120 | 560 |
| SS03-WB1-G1 | Gate | startScanning | - | SS03-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS03-WB1-G1-2 | Gate | startScanning | - | SS03-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 380 | 20 | 20 |
| SS03-WB1-G1-3 | Gate | startScanning | - | SS03-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 520 | 20 | 20 |
| SS03-WB1-FR1 | Fragment | break [đầu quét không sẵn sàng] | break | - | Kết thúc operation bằng ngoại lệ | 110 | 280 | 460 | 130 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS03-WB1-M01 | 1 | SS03-WB1-G1 | SS03-WB1-L01 | startScanning(listener) | Đồng bộ | - | UC-015 bước 2 |
| SS03-WB1-M02 | 2 | SS03-WB1-L01 | SS03-WB1-L01 | keep(listener) | Tự gọi | - | Lưu bộ nhận |
| SS03-WB1-M03 | 3 | SS03-WB1-L01 | SS03-WB1-L02 | openScanner(onRawInput) | Đồng bộ | - | Đăng ký nhận chuỗi đọc được |
| SS03-WB1-M04 | 4 | SS03-WB1-L02 | SS03-WB1-L03 | enableScanning() | Đồng bộ | - | - |
| SS03-WB1-M05 | 5 | SS03-WB1-L03 | SS03-WB1-L02 | lỗi khởi tạo | Trả về | SS03-WB1-FR1 (toán hạng 1) | Thiết bị không sẵn sàng |
| SS03-WB1-M06 | 6 | SS03-WB1-L02 | SS03-WB1-L01 | ScannerUnavailableException | Trả về | SS03-WB1-FR1 (toán hạng 1) | - |
| SS03-WB1-M07 | 7 | SS03-WB1-L01 | SS03-WB1-G1-2 | ScannerUnavailableException | Trả về | SS03-WB1-FR1 (toán hạng 1) | Cô lập lỗi thiết bị |
| SS03-WB1-M08 | 8 | SS03-WB1-L03 | SS03-WB1-L02 | đầu quét sẵn sàng | Trả về | - | - |
| SS03-WB1-M09 | 9 | SS03-WB1-L02 | SS03-WB1-L01 | mở thành công | Trả về | - | - |
| SS03-WB1-M10 | 10 | SS03-WB1-L01 | SS03-WB1-G1-3 | void | Trả về | - | - |

#### Trang "Hộp trắng - receiveScannedCode"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS03-WB2-FRM | Fragment | sd receiveScannedCode | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 530 |
| SS03-WB2-L01 | Lifeline | :DC-BarcodeReaderService | «control» | - | Lớp điều phối, hiện thực IF-04 | 120 | 40 | 120 | 470 |
| SS03-WB2-L02 | Lifeline | :DC-ScannerInputAdapter | «adapter» | - | Lớp giao tiếp thiết bị | 280 | 40 | 120 | 470 |
| SS03-WB2-L03 | Lifeline | :DC-TicketCodeParser | «converter» | - | Lớp chuyển đổi dữ liệu | 440 | 40 | 120 | 470 |
| SS03-WB2-L04 | Actor | Đầu quét mã vạch | «ACT-09» | - | Thiết bị | 600 | 40 | 120 | 470 |
| SS03-WB2-G1 | Gate | receiveScannedCode | - | SS03-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 300 | 20 | 20 |
| SS03-WB2-G1-2 | Gate | receiveScannedCode | - | SS03-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 410 | 20 | 20 |
| SS03-WB2-FR1 | Fragment | alt [chuỗi đúng định dạng mã vé] | alt | - | Phân loại chuỗi đọc được | 110 | 240 | 460 | 200 |
| SS03-WB2-FR1-O2 | Fragment | [chuỗi sai định dạng hoặc đọc hỏng] | alt | SS03-WB2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS03-WB2-FR1-SEP2 | 120 | 350 | 440 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS03-WB2-M01 | 1 | SS03-WB2-L04 | SS03-WB2-L02 | onRawInput(rawString) | Bất đồng bộ | - | UC-015 bước 4 |
| SS03-WB2-M02 | 2 | SS03-WB2-L02 | SS03-WB2-L01 | handleRawInput(rawString) | Bất đồng bộ | - | - |
| SS03-WB2-M03 | 3 | SS03-WB2-L01 | SS03-WB2-L03 | parseTicketCode(rawString) | Đồng bộ | - | Bỏ ký tự kết thúc Enter, chuẩn hoá |
| SS03-WB2-M04 | 4 | SS03-WB2-L03 | SS03-WB2-L01 | TicketCode | Trả về | SS03-WB2-FR1 (toán hạng 1) | - |
| SS03-WB2-M05 | 5 | SS03-WB2-L01 | SS03-WB2-G1 | receiveScannedCode(code) | Bất đồng bộ | SS03-WB2-FR1 (toán hạng 1) | IF-05 do DC-CheckBoardingTicketService hiện thực |
| SS03-WB2-M06 | 6 | SS03-WB2-L03 | SS03-WB2-L01 | InvalidCodeFormat | Trả về | SS03-WB2-FR1 (toán hạng 2) | Chuỗi không phải mã vé |
| SS03-WB2-M07 | 7 | SS03-WB2-L01 | SS03-WB2-G1-2 | receiveScanError(ScanError) | Bất đồng bộ | SS03-WB2-FR1 (toán hạng 2) | IF-05 |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-BarcodeReaderService | BarcodeReaderService | Điều phối | Nhận lời gọi IF-04, giữ bộ nhận, gọi IF-05 khi có mã vé hoặc lỗi | package-private | IF-04 |
| DC-ScannerInputAdapter | ScannerInputAdapter | Giao tiếp ngoài | Nhận chuỗi đọc được từ đầu quét (SDK của máy hoặc đầu vào giả lập bàn phím gửi kèm phím Enter, chưa biết model, Q-54) và báo lỗi thiết bị | package-private | - |
| DC-TicketCodeParser | TicketCodeParser | Chuyển đổi dữ liệu | Chuẩn hoá chuỗi đọc được thành TicketCode (bỏ ký tự kết thúc, kiểm tra định dạng) | package-private | - |
| DC-ScanError | ScanError | Kiểu dữ liệu | Loại lỗi đọc: ReadFailed / InvalidCodeFormat / DeviceDisconnected | public (thuộc chữ ký IF-05) | - |
| DC-ScannerUnavailableException | ScannerUnavailableException | Ngoại lệ | Đầu quét không sẵn sàng khi bật | public (thuộc chữ ký IF-04) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-03 | Subsystem | SS-03 BarcodeReading | «subsystem» | - | - | 40 | 190 | 480 | 260 |
| IF-04 | Interface | IF-04 IBarcodeReader | «interface» | PKG-18 | - | 180 | 40 | 200 | 90 |
| IF-05 | Interface | IF-05 IBarcodeReadListener | «interface» | PKG-18 | - | 420 | 40 | 200 | 90 |
| DC-BarcodeReaderService | Class | DC-BarcodeReaderService | «control» | SS-03 | - | 300 | 230 | 200 | 70 |
| DC-TicketCodeParser | Class | DC-TicketCodeParser | «converter» | SS-03 | - | 60 | 360 | 200 | 70 |
| DC-ScannerInputAdapter | Class | DC-ScannerInputAdapter | «adapter» | SS-03 | - | 300 | 360 | 200 | 70 |
| ACT-09 | Actor | Đầu quét mã vạch (ACT-09) | - | - | - | 560 | 360 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS03-EL-E01 | DC-BarcodeReaderService | IF-04 | Realization | - | Subsystem hiện thực IF-04 qua lớp điều phối | (390,150); (280,150) |
| SS03-EL-E02 | DC-BarcodeReaderService | IF-05 | Dependency | gọi | Gọi ngược lên bên hiện thực IF-05 | (410,160); (520,160) |
| SS03-EL-E03 | DC-BarcodeReaderService | DC-TicketCodeParser | Association (điều hướng) | dùng | - | (390,320); (160,320) |
| SS03-EL-E04 | DC-BarcodeReaderService | DC-ScannerInputAdapter | Association (điều hướng) | dùng | - | (410,330); (400,330) |
| SS03-EL-E05 | DC-ScannerInputAdapter | ACT-09 | Association | SDK hoặc bàn phím (Q-54) | - | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-03 | IF-05 | Qua interface | Đẩy mã vé lên layer trên theo P09 R5 | Ưu tiên |
| SS-03 | PKG-28 | Vào package | TicketCode có trong chữ ký IF-05 | Dùng thận trọng |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-11 | Package | PKG-11 BoardingCheckService | - | - | - | 180 | 40 | 200 | 60 |
| IF-04 | Interface | IF-04 IBarcodeReader | «interface» | - | - | 60 | 160 | 200 | 50 |
| IF-05 | Interface | IF-05 IBarcodeReadListener | «interface» | - | - | 300 | 160 | 200 | 50 |
| SS-03 | Subsystem | SS-03 BarcodeReading | - | - | - | 180 | 270 | 200 | 60 |
| PKG-28 | Package | PKG-28 SharedValueTypes | - | - | - | 180 | 380 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS03-DP-E01 | PKG-11 | IF-04 | Dependency | dùng | - | (270,120); (160,120) |
| SS03-DP-E02 | PKG-11 | IF-05 | Realization | DC-CheckBoardingTicketService | - | (290,130); (400,130) |
| SS03-DP-E03 | SS-03 | IF-04 | Realization | - | - | (270,230); (160,230) |
| SS03-DP-E04 | SS-03 | IF-05 | Dependency | gọi ngược | - | (290,240); (400,240) |
| SS03-DP-E05 | SS-03 | PKG-28 | Dependency | TicketCode | - | - |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| startScanning | Đầu quét không sẵn sàng khi bật | Thiết bị | Lỗi khởi tạo SDK hoặc kênh nhập | Không thử lại tự động | ScannerUnavailableException | Không có (UC-015 bước 2 chưa có luồng) | Q-103 |
| receiveScanError | Đọc hỏng hoặc dữ liệu đọc không phải mã vé | Thiết bị | TicketCodeParser không phân tích được | Chuyển thành ScanError, không chặn lần quét sau | receiveScanError(InvalidCodeFormat hoặc ReadFailed) | Không có (gần 5a nhưng 5a là mã đúng định dạng không có trong danh sách) | Q-103; Đề xuất sửa P04 |
| receiveScanError | Đầu quét mất kết nối giữa phiên | Thiết bị | Sự kiện ngắt kết nối của SDK | Chuyển thành ScanError(DeviceDisconnected) | receiveScanError(DeviceDisconnected) | Không có | Q-103 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-04 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: IF-05 |
| Không phần tử bên trong subsystem nào public | Đạt |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt: stopScanning 1-1 |

## SS-04 TicketPrinting

Package chứa: PKG-17. Tác nhân hoặc đối tượng ngoài: ACT-08.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-005 Bán vé tại quầy (chưa có P04, P07) | Control của UC-005 (chưa có), PKG-09 | Chưa có message trong P07; nguồn là NFR-09, P09 F7, P10 F2 // printTicket | vé đã phát hành kèm mã vé | Chưa có P04 của UC-005: lỗi in (hết giấy, mất kết nối) chưa có luồng (Q-102) |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-06 | ITicketPrinter | In một vé giấy có mã vạch trên máy in vé nhiệt tại quầy | SS-04 | Control của UC-005 (PKG-09, chưa có DC) | PKG-17 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-06 | ITicketPrinter | Máy in vé nhiệt (ACT-08) | printTicket(ticket: Ticket): PrintResult | ticket: Ticket - vé đã phát hành và đã thanh toán, có mã vé (TicketCode) để tạo mã vạch (ASM-34) | PrintResult: status (Printed / Failed), failureReason (OutOfPaper / PrinterOffline / Other, khi Failed) | PrinterUnavailableException (Thiết bị); Failed (Thiết bị) | UC-005 (P02; P04, P07 chưa có). Nguồn: NFR-09, P10 F2 // printTicket | Vé đã phát hành (UC-005 bước thu tiền mặt xong) | Vé giấy có mã vạch của mã vé được in khi status là Printed | Đồng bộ | Không (mỗi lần gọi in thêm một vé giấy; không tự thử lại; in lại là hành vi nghiệp vụ chưa có) | 15 giây (Thiết kế: máy in nhiệt phản hồi trong vài giây; cộng thời gian qua phần mềm trung gian ở máy trạm, Q-79) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-04.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

Mọi operation của IF-06 (một operation) có trang hộp trắng.

#### Trang "Hộp đen - UC-005 printTicket"

UC hoặc operation: UC-005

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS04-BB1-L01 | Lifeline | :Control của UC-005 (chưa có P07) | «control» | - | Control tạm của UC-005 ở PKG-09 | 40 | 40 | 120 | 460 |
| SS04-BB1-L02 | Lifeline | :IF-06 ITicketPrinter | «interface» | - | Interface của SS-04 | 200 | 40 | 120 | 460 |
| SS04-BB1-FR1 | Fragment | alt [status = Printed] | alt | - | Mỗi toán hạng là một kết quả của printTicket | 30 | 160 | 300 | 270 |
| SS04-BB1-FR1-O2 | Fragment | [status = Failed] | alt | SS04-BB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS04-BB1-FR1-SEP2 | 40 | 230 | 280 | 20 |
| SS04-BB1-FR1-O3 | Fragment | [PrinterUnavailableException] | alt | SS04-BB1-FR1 | Toán hạng 3, ngăn bởi đường nét đứt SS04-BB1-FR1-SEP3 | 40 | 340 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS04-BB1-M01 | 1 | SS04-BB1-L01 | SS04-BB1-L02 | printTicket(ticket) | Đồng bộ | - | UC-005 (in vé giấy, REQ-24) |
| SS04-BB1-M02 | 2 | SS04-BB1-L02 | SS04-BB1-L01 | PrintResult(status = Printed) | Trả về | SS04-BB1-FR1 (toán hạng 1) | UC-005 |
| SS04-BB1-M03 | 3 | SS04-BB1-L02 | SS04-BB1-L01 | PrintResult(status = Failed, failureReason) | Trả về | SS04-BB1-FR1 (toán hạng 2) | UC-005 |
| SS04-BB1-M04 | 4 | SS04-BB1-L01 | SS04-BB1-L01 | chưa có luồng P04 (Q-102) | Tự gọi | SS04-BB1-FR1 (toán hạng 2) | Q-102 |
| SS04-BB1-M05 | 5 | SS04-BB1-L02 | SS04-BB1-L01 | PrinterUnavailableException | Trả về | SS04-BB1-FR1 (toán hạng 3) | UC-005 |
| SS04-BB1-M06 | 6 | SS04-BB1-L01 | SS04-BB1-L01 | chưa có luồng P04 (Q-102) | Tự gọi | SS04-BB1-FR1 (toán hạng 3) | Q-102 |

#### Trang "Hộp trắng - printTicket"

UC hoặc operation: UC-005

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS04-WB1-FRM | Fragment | sd printTicket | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 730 |
| SS04-WB1-L01 | Lifeline | :DC-TicketPrinterService | «control» | - | Lớp điều phối, hiện thực IF-06 | 120 | 40 | 120 | 670 |
| SS04-WB1-L02 | Lifeline | :DC-PrintJobConverter | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 670 |
| SS04-WB1-L03 | Lifeline | :DC-PrinterClient | «adapter» | - | Lớp giao tiếp với phần mềm trung gian ở máy trạm | 440 | 40 | 120 | 670 |
| SS04-WB1-L04 | Actor | Máy in vé nhiệt | «ACT-08» | - | Thiết bị | 600 | 40 | 120 | 670 |
| SS04-WB1-G1 | Gate | printTicket | - | SS04-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS04-WB1-G1-2 | Gate | printTicket | - | SS04-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 490 | 20 | 20 |
| SS04-WB1-G1-3 | Gate | printTicket | - | SS04-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 630 | 20 | 20 |
| SS04-WB1-FR1 | Fragment | alt [nhận được trạng thái từ máy in] | alt | - | Hai kết quả gửi lệnh in | 110 | 320 | 620 | 200 |
| SS04-WB1-FR1-O2 | Fragment | [không kết nối được] | alt | SS04-WB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS04-WB1-FR1-SEP2 | 120 | 430 | 600 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS04-WB1-M01 | 1 | SS04-WB1-G1 | SS04-WB1-L01 | printTicket(ticket) | Đồng bộ | - | UC-005 |
| SS04-WB1-M02 | 2 | SS04-WB1-L01 | SS04-WB1-L02 | toPrintJob(ticket) | Đồng bộ | - | Định dạng lệnh in, tạo mã vạch từ TicketCode |
| SS04-WB1-M03 | 3 | SS04-WB1-L02 | SS04-WB1-L01 | PrintJob | Trả về | - | - |
| SS04-WB1-M04 | 4 | SS04-WB1-L01 | SS04-WB1-L03 | send(printJob) | Đồng bộ | - | - |
| SS04-WB1-M05 | 5 | SS04-WB1-L03 | SS04-WB1-L04 | print(printJob) | Đồng bộ | - | - |
| SS04-WB1-M06 | 6 | SS04-WB1-L04 | SS04-WB1-L03 | trạng thái máy in | Trả về | SS04-WB1-FR1 (toán hạng 1) | - |
| SS04-WB1-M07 | 7 | SS04-WB1-L03 | SS04-WB1-L01 | PrinterStatus | Trả về | SS04-WB1-FR1 (toán hạng 1) | - |
| SS04-WB1-M08 | 8 | SS04-WB1-L03 | SS04-WB1-L01 | ConnectionFailed | Trả về | SS04-WB1-FR1 (toán hạng 2) | Không nối được phần mềm trung gian hoặc máy in |
| SS04-WB1-M09 | 9 | SS04-WB1-L01 | SS04-WB1-G1-2 | PrinterUnavailableException | Trả về | SS04-WB1-FR1 (toán hạng 2) | Cô lập lỗi thiết bị |
| SS04-WB1-M10 | 10 | SS04-WB1-L01 | SS04-WB1-L02 | toPrintResult(printerStatus) | Đồng bộ | - | - |
| SS04-WB1-M11 | 11 | SS04-WB1-L02 | SS04-WB1-L01 | PrintResult | Trả về | - | - |
| SS04-WB1-M12 | 12 | SS04-WB1-L01 | SS04-WB1-G1-3 | PrintResult | Trả về | - | - |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-TicketPrinterService | TicketPrinterService | Điều phối | Nhận lời gọi IF-06, điều khiển tạo lệnh in và gửi lệnh, ghi nhật ký | package-private | IF-06 |
| DC-PrinterClient | PrinterClient | Giao tiếp ngoài | Gửi lệnh in và nhận trạng thái qua phần mềm trung gian ở máy trạm tại quầy (Q-79); timeout, báo mất kết nối | package-private | - |
| DC-PrintJobConverter | PrintJobConverter | Chuyển đổi dữ liệu | Chuyển Ticket sang lệnh in có mã vạch của TicketCode (ASM-34); chuyển trạng thái máy in sang PrintResult | package-private | - |
| DC-PrintResult | PrintResult | Kiểu dữ liệu | Kết quả của printTicket (status, failureReason) | public (thuộc chữ ký IF-06) | - |
| DC-PrinterUnavailableException | PrinterUnavailableException | Ngoại lệ | Không nối được máy in hoặc phần mềm trung gian | public (thuộc chữ ký IF-06) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-04 | Subsystem | SS-04 TicketPrinting | «subsystem» | - | - | 40 | 160 | 480 | 260 |
| IF-06 | Interface | IF-06 ITicketPrinter | «interface» | PKG-17 | - | 300 | 40 | 200 | 70 |
| DC-TicketPrinterService | Class | DC-TicketPrinterService | «control» | SS-04 | - | 300 | 200 | 200 | 70 |
| DC-PrintJobConverter | Class | DC-PrintJobConverter | «converter» | SS-04 | - | 60 | 330 | 200 | 70 |
| DC-PrinterClient | Class | DC-PrinterClient | «adapter» | SS-04 | - | 300 | 330 | 200 | 70 |
| ACT-08 | Actor | Máy in vé nhiệt (ACT-08) | - | - | - | 560 | 330 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS04-EL-E01 | DC-TicketPrinterService | IF-06 | Realization | - | Subsystem hiện thực IF-06 qua lớp điều phối | - |
| SS04-EL-E02 | DC-TicketPrinterService | DC-PrintJobConverter | Association (điều hướng) | dùng | - | (390,290); (160,290) |
| SS04-EL-E03 | DC-TicketPrinterService | DC-PrinterClient | Association (điều hướng) | dùng | - | (410,300); (400,300) |
| SS04-EL-E04 | DC-PrinterClient | ACT-08 | Association | qua phần mềm trung gian (Q-79) | - | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-04 | PKG-23 | Vào package | Ticket có trong chữ ký IF-06 và cần mã vé, chỗ, tuyến để in (P10 F6: PKG-17 --> PKG-23); Domain nằm dưới Services nên không kéo phụ thuộc lên | Dùng thận trọng |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-09 | Package | PKG-09 TicketSalesService | - | - | - | 60 | 40 | 200 | 60 |
| IF-06 | Interface | IF-06 ITicketPrinter | «interface» | - | - | 60 | 150 | 200 | 50 |
| SS-04 | Subsystem | SS-04 TicketPrinting | - | - | - | 60 | 250 | 200 | 60 |
| PKG-23 | Package | PKG-23 Ticketing | - | - | - | 60 | 360 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS04-DP-E01 | PKG-09 | IF-06 | Dependency | dùng | - | - |
| SS04-DP-E02 | SS-04 | IF-06 | Realization | - | - | - |
| SS04-DP-E03 | SS-04 | PKG-23 | Dependency | Ticket | - | - |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| printTicket | Không nối được phần mềm trung gian hoặc máy in | Thiết bị | Lỗi kết nối hoặc hết thời gian kết nối 5 giây | Không thử lại tự động | PrinterUnavailableException | Không có (P04 UC-005 chưa có) | Q-102, Q-57, Q-79 |
| printTicket | Máy in hết giấy hoặc báo lỗi | Thiết bị | Trạng thái máy in | Chuyển thành Failed kèm failureReason | PrintResult(Failed, OutOfPaper hoặc Other) | Không có (P04 UC-005 chưa có) | Q-102 |
| printTicket | Hết thời gian chờ trạng thái sau khi đã gửi lệnh | Không rõ kết quả | Hết thời gian 15 giây | Không tự in lại (tránh in trùng vé giấy); trả Failed(Other) | PrintResult(Failed, Other) | Không có | Q-102 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-06 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: không dùng interface nào |
| Không phần tử bên trong subsystem nào public | Đạt |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt |

## SS-05 TriggerScheduling

Package chứa: PKG-19. Tác nhân hoặc đối tượng ngoài: ACT-10.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-002 Đặt vé trực tuyến | AC-C-BookTicketOnlineController (DC-BookTicketOnlineService) | SD1: 3.1.7 // startWaitingForPayment (tự gọi); 3.1.8 // after(BR-07) handleSeatHoldExpired (tự gọi, trong break 9a) | mã lần đặt, thời điểm bắt đầu giữ chỗ, hạn 10 phút (BR-07) | 9a (hết thời hạn giữ chỗ). Không ghi được mốc: chưa có luồng (Q-104); sai số mốc chưa quy định (Q-82) |
| UC-013 Huỷ chuyến | AC-C-CancelTripController (DC-CancelTripService) | SD1: 2.1.2 // cancelTripTriggers (tự gọi; mốc của UC-006 và UC-014, ASM-47) | mã chuyến, loại mốc cần huỷ | Không huỷ được mốc: chưa có luồng (Q-104) |
| UC-006, UC-014 (chưa có P07) | Chưa có | Chưa có message; P10 F2 ghi mốc của UC-006 (60 phút trước giờ xuất bến), UC-014 (15 phút trước giờ xuất bến) | mã đặt chỗ, mã chuyến, giờ xuất bến | Chưa có P07 |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-07 | ITriggerScheduler | Đăng ký và huỷ mốc kích hoạt tính từ dữ liệu | SS-05 | DC-BookTicketOnlineService (PKG-09), DC-CancelTripService (PKG-10) | PKG-19 |
| IF-08 | ITriggerHandler | Nhận mốc đã đến hạn (chiều ngược): bên cung cấp DC-BookTicketOnlineService (PKG-09), bên dùng SS-05 | DC-BookTicketOnlineService (PKG-09), hiện thực ở layer trên | SS-05 | PKG-19 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-07 | ITriggerScheduler | Bộ định thời (ACT-10) | scheduleTrigger(kind: TriggerKind, targetId: String, groupId: String, dueAt: DateTime): TriggerReference | kind: TriggerKind - loại mốc (HoldExpiry / PhoneReservationExpiry / PassengerListDispatch)<br>targetId: String - định danh đối tượng của mốc (mã lần đặt, mã đặt chỗ, mã chuyến)<br>groupId: String - định danh nhóm để huỷ hàng loạt (mã chuyến)<br>dueAt: DateTime - thời điểm đến hạn, không trước thời điểm hiện tại | TriggerReference: tham chiếu mốc (kind, targetId), dùng làm khoá khi mốc đến hạn | TriggerStoreUnavailableException (Kỹ thuật tạm thời) | UC-002 (bước 9: SD1 3.1.7 // startWaitingForPayment, dueAt = thời điểm bắt đầu giữ cộng 10 phút theo BR-07); UC-006, UC-014 (mốc tính từ giờ xuất bến, chưa có P07) | Lần đặt đã giữ chỗ và có thời điểm bắt đầu giữ (Booking.holdStartTime) | Mốc được ghi bền; đến dueAt bộ định thời gọi IF-08 đúng một lần có hiệu lực | Đồng bộ | Có (khoá kind + targetId; đăng ký lại cùng khoá không tạo mốc thứ hai) | 5 giây (Thiết kế: ghi một dòng trong giao dịch ngắn); sai số của mốc: chưa quy định (Q-82) |
| IF-07 | ITriggerScheduler | Bộ định thời (ACT-10) | cancelTriggers(groupId: String, kinds: List<TriggerKind>): Integer | groupId: String - mã chuyến của các mốc cần huỷ<br>kinds: List<TriggerKind> - loại mốc cần huỷ, không rỗng | Integer: số mốc đã huỷ | TriggerStoreUnavailableException (Kỹ thuật tạm thời) | UC-013 (bước 5: SD1 2.1.2 // cancelTripTriggers, huỷ mốc của UC-006 và UC-014, ASM-47) | Chuyến đã chuyển sang trạng thái huỷ | Các mốc chưa đến hạn thuộc groupId và kinds không còn được kích hoạt; mốc HoldExpiry không bị huỷ vì UC-013 không liệt kê loại này | Đồng bộ | Có (huỷ lại trả 0) | 5 giây (Thiết kế: như scheduleTrigger) |
| IF-08 | ITriggerHandler | Bộ định thời (ACT-10), gọi ngược | handleTrigger(reference: TriggerReference): void | reference: TriggerReference - mốc đã đến hạn (kind, targetId) | void | Bên hiện thực có thể ném ngoại lệ; SS-05 coi là lỗi xử lý, giao lại mốc (xem F7a) | UC-002 (luồng 9a: SD1 3.1.8 // after(BR-07) handleSeatHoldExpired); UC-006, UC-014 khi có P07 | Mốc đã đến hạn và chưa được xử lý | Mốc được xử lý có hiệu lực đúng một lần (kiểm tra trạng thái lần đặt trước khi trả chỗ) | Bất đồng bộ (bộ định thời gọi vào) | Có (giao ít nhất một lần; bên hiện thực kiểm tra trạng thái đối tượng trước khi xử lý) | 60 giây mỗi lần xử lý, sau đó giao lại (Thiết kế: giao dịch trả chỗ ngắn; giới hạn để một bản back-end treo không giữ mốc mãi) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-05.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

Mọi operation của IF-07, IF-08 có trang hộp trắng.

#### Trang "Hộp đen - UC-002 giữ chỗ và hết thời hạn"

UC hoặc operation: UC-002

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS05-BB1-L01 | Lifeline | :DC-BookTicketOnlineService | «control» | - | Control của UC-002, hiện thực IF-08 | 40 | 40 | 120 | 430 |
| SS05-BB1-L02 | Lifeline | :IF-07 ITriggerScheduler | «interface» | - | Interface của SS-05 | 200 | 40 | 120 | 430 |
| SS05-BB1-FR1 | Fragment | alt [ghi mốc thành công] | alt | - | Kết quả của scheduleTrigger | 30 | 160 | 300 | 160 |
| SS05-BB1-FR1-O2 | Fragment | [không ghi được mốc] | alt | SS05-BB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS05-BB1-FR1-SEP2 | 40 | 230 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS05-BB1-M01 | 1 | SS05-BB1-L01 | SS05-BB1-L02 | scheduleTrigger(HoldExpiry, bookingId, tripId, dueAt) | Đồng bộ | - | UC-002 bước 9 |
| SS05-BB1-M02 | 2 | SS05-BB1-L02 | SS05-BB1-L01 | TriggerReference | Trả về | SS05-BB1-FR1 (toán hạng 1) | UC-002 bước 9 |
| SS05-BB1-M03 | 3 | SS05-BB1-L02 | SS05-BB1-L01 | TriggerStoreUnavailableException | Trả về | SS05-BB1-FR1 (toán hạng 2) | UC-002 bước 9 |
| SS05-BB1-M04 | 4 | SS05-BB1-L01 | SS05-BB1-L01 | chưa có luồng P04 (Q-104) | Tự gọi | SS05-BB1-FR1 (toán hạng 2) | Q-104 |
| SS05-BB1-M05 | 5 | SS05-BB1-L02 | SS05-BB1-L01 | handleTrigger(reference) | Bất đồng bộ | - | UC-002 luồng 9a, IF-08 |
| SS05-BB1-M06 | 6 | SS05-BB1-L01 | SS05-BB1-L01 | handleSeatHoldExpired | Tự gọi | - | UC-002 luồng 9a |

#### Trang "Hộp đen - UC-013 cancelTriggers"

UC hoặc operation: UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS05-BB2-L01 | Lifeline | :DC-CancelTripService | «control» | - | Control của UC-013 (AC-C-CancelTripController) | 40 | 40 | 120 | 350 |
| SS05-BB2-L02 | Lifeline | :IF-07 ITriggerScheduler | «interface» | - | Interface của SS-05 | 200 | 40 | 120 | 350 |
| SS05-BB2-FR1 | Fragment | alt [huỷ thành công] | alt | - | Kết quả của cancelTriggers | 30 | 160 | 300 | 160 |
| SS05-BB2-FR1-O2 | Fragment | [không huỷ được] | alt | SS05-BB2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS05-BB2-FR1-SEP2 | 40 | 230 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS05-BB2-M01 | 1 | SS05-BB2-L01 | SS05-BB2-L02 | cancelTriggers(tripId, [PhoneReservationExpiry, PassengerListDispatch]) | Đồng bộ | - | UC-013 bước 5 |
| SS05-BB2-M02 | 2 | SS05-BB2-L02 | SS05-BB2-L01 | Integer (số mốc đã huỷ) | Trả về | SS05-BB2-FR1 (toán hạng 1) | UC-013 bước 5 |
| SS05-BB2-M03 | 3 | SS05-BB2-L02 | SS05-BB2-L01 | TriggerStoreUnavailableException | Trả về | SS05-BB2-FR1 (toán hạng 2) | UC-013 bước 5 |
| SS05-BB2-M04 | 4 | SS05-BB2-L01 | SS05-BB2-L01 | chưa có luồng P04 (Q-104) | Tự gọi | SS05-BB2-FR1 (toán hạng 2) | Q-104 |

#### Trang "Hộp trắng - scheduleTrigger"

UC hoặc operation: UC-002

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS05-WB1-FRM | Fragment | sd scheduleTrigger | - | - | Khung sơ đồ của operation | 20 | 20 | 580 | 540 |
| SS05-WB1-L01 | Lifeline | :DC-TriggerSchedulerService | «control» | - | Lớp điều phối, hiện thực IF-07 | 120 | 40 | 120 | 480 |
| SS05-WB1-L02 | Lifeline | :DC-TriggerStore | «adapter» | - | Lớp giao tiếp: kho mốc bền trong CSDL | 280 | 40 | 120 | 480 |
| SS05-WB1-L03 | Actor | Bộ định thời | «ACT-10» | - | Cơ chế thời gian | 440 | 40 | 120 | 480 |
| SS05-WB1-G1 | Gate | scheduleTrigger | - | SS05-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS05-WB1-G1-2 | Gate | scheduleTrigger | - | SS05-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 300 | 20 | 20 |
| SS05-WB1-G1-3 | Gate | scheduleTrigger | - | SS05-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 440 | 20 | 20 |
| SS05-WB1-FR1 | Fragment | break [không ghi được kho mốc] | break | - | Kết thúc operation bằng ngoại lệ | 110 | 240 | 300 | 90 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS05-WB1-M01 | 1 | SS05-WB1-G1 | SS05-WB1-L01 | scheduleTrigger(kind, targetId, groupId, dueAt) | Đồng bộ | - | UC-002 bước 9 |
| SS05-WB1-M02 | 2 | SS05-WB1-L01 | SS05-WB1-L02 | upsert(kind, targetId, groupId, dueAt) | Đồng bộ | - | Khoá kind + targetId, ghi đè nếu đã có |
| SS05-WB1-M03 | 3 | SS05-WB1-L02 | SS05-WB1-L01 | mốc đã ghi | Trả về | - | - |
| SS05-WB1-M04 | 4 | SS05-WB1-L02 | SS05-WB1-L01 | StoreUnavailable | Trả về | SS05-WB1-FR1 (toán hạng 1) | - |
| SS05-WB1-M05 | 5 | SS05-WB1-L01 | SS05-WB1-G1-2 | TriggerStoreUnavailableException | Trả về | SS05-WB1-FR1 (toán hạng 1) | Cô lập lỗi |
| SS05-WB1-M06 | 6 | SS05-WB1-L01 | SS05-WB1-L03 | arm(reference, dueAt) | Đồng bộ | - | Hẹn lần quét kế tiếp không muộn hơn dueAt |
| SS05-WB1-M07 | 7 | SS05-WB1-L03 | SS05-WB1-L01 | đã hẹn | Trả về | - | - |
| SS05-WB1-M08 | 8 | SS05-WB1-L01 | SS05-WB1-G1-3 | TriggerReference | Trả về | - | - |

#### Trang "Hộp trắng - cancelTriggers"

UC hoặc operation: UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS05-WB2-FRM | Fragment | sd cancelTriggers | - | - | Khung sơ đồ của operation | 20 | 20 | 420 | 490 |
| SS05-WB2-L01 | Lifeline | :DC-TriggerSchedulerService | «control» | - | Lớp điều phối, hiện thực IF-07 | 120 | 40 | 120 | 430 |
| SS05-WB2-L02 | Lifeline | :DC-TriggerStore | «adapter» | - | Lớp giao tiếp: kho mốc bền trong CSDL | 280 | 40 | 120 | 430 |
| SS05-WB2-G1 | Gate | cancelTriggers | - | SS05-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS05-WB2-G1-2 | Gate | cancelTriggers | - | SS05-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 330 | 20 | 20 |
| SS05-WB2-G1-3 | Gate | cancelTriggers | - | SS05-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 390 | 20 | 20 |
| SS05-WB2-FR1 | Fragment | alt [xoá thành công] | alt | - | Kết quả của deleteDue | 110 | 200 | 300 | 160 |
| SS05-WB2-FR1-O2 | Fragment | [kho mốc không sẵn sàng] | alt | SS05-WB2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS05-WB2-FR1-SEP2 | 120 | 270 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS05-WB2-M01 | 1 | SS05-WB2-G1 | SS05-WB2-L01 | cancelTriggers(groupId, kinds) | Đồng bộ | - | UC-013 bước 5 |
| SS05-WB2-M02 | 2 | SS05-WB2-L01 | SS05-WB2-L02 | deleteDue(groupId, kinds) | Đồng bộ | - | Chỉ xoá mốc chưa đến hạn |
| SS05-WB2-M03 | 3 | SS05-WB2-L02 | SS05-WB2-L01 | số dòng đã xoá | Trả về | SS05-WB2-FR1 (toán hạng 1) | - |
| SS05-WB2-M04 | 4 | SS05-WB2-L02 | SS05-WB2-L01 | StoreUnavailable | Trả về | SS05-WB2-FR1 (toán hạng 2) | - |
| SS05-WB2-M05 | 5 | SS05-WB2-L01 | SS05-WB2-G1-2 | TriggerStoreUnavailableException | Trả về | SS05-WB2-FR1 (toán hạng 2) | Cô lập lỗi |
| SS05-WB2-M06 | 6 | SS05-WB2-L01 | SS05-WB2-G1-3 | Integer | Trả về | - | - |

#### Trang "Hộp trắng - handleTrigger"

UC hoặc operation: UC-002

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS05-WB3-FRM | Fragment | sd handleTrigger | - | - | Khung sơ đồ của operation | 20 | 20 | 580 | 620 |
| SS05-WB3-L01 | Lifeline | :DC-TriggerDispatcher | «control» | - | Lớp điều phối mốc đến hạn | 120 | 40 | 120 | 560 |
| SS05-WB3-L02 | Lifeline | :DC-TriggerStore | «adapter» | - | Lớp giao tiếp: kho mốc bền trong CSDL | 280 | 40 | 120 | 560 |
| SS05-WB3-L03 | Actor | Bộ định thời | «ACT-10» | - | Cơ chế thời gian | 440 | 40 | 120 | 560 |
| SS05-WB3-G1 | Gate | handleTrigger | - | SS05-WB3-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 260 | 20 | 20 |
| SS05-WB3-G1-2 | Gate | handleTrigger | - | SS05-WB3-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 330 | 20 | 20 |
| SS05-WB3-G1-3 | Gate | handleTrigger | - | SS05-WB3-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 440 | 20 | 20 |
| SS05-WB3-FR1 | Fragment | loop [với từng mốc đã chiếm] | loop | - | Mỗi mốc một lần gọi IF-08 | 110 | 240 | 300 | 290 |
| SS05-WB3-FR2 | Fragment | alt [xử lý thành công] | alt | - | Kết quả của handleTrigger | 120 | 310 | 280 | 200 |
| SS05-WB3-FR2-O2 | Fragment | [bên xử lý ném ngoại lệ] | alt | SS05-WB3-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS05-WB3-FR2-SEP2 | 130 | 420 | 260 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS05-WB3-M01 | 1 | SS05-WB3-L03 | SS05-WB3-L01 | onTimer() | Bất đồng bộ | - | Mỗi chu kỳ quét 10 giây (Thiết kế: giữ sai số mốc nhỏ; Q-82) |
| SS05-WB3-M02 | 2 | SS05-WB3-L01 | SS05-WB3-L02 | claimDue(now, maxCount) | Đồng bộ | - | Chiếm các mốc đến hạn bằng cập nhật có điều kiện, một bản back-end chiếm được |
| SS05-WB3-M03 | 3 | SS05-WB3-L02 | SS05-WB3-L01 | danh sách TriggerReference đã chiếm | Trả về | - | - |
| SS05-WB3-M04 | 4 | SS05-WB3-L01 | SS05-WB3-G1 | handleTrigger(reference) | Đồng bộ | SS05-WB3-FR1 (toán hạng 1) | IF-08 do DC-BookTicketOnlineService hiện thực |
| SS05-WB3-M05 | 5 | SS05-WB3-G1-2 | SS05-WB3-L01 | xử lý xong | Trả về | SS05-WB3-FR2 (toán hạng 1) | - |
| SS05-WB3-M06 | 6 | SS05-WB3-L01 | SS05-WB3-L02 | markDone(reference) | Đồng bộ | SS05-WB3-FR2 (toán hạng 1) | - |
| SS05-WB3-M07 | 7 | SS05-WB3-G1-3 | SS05-WB3-L01 | ngoại lệ của bên xử lý | Trả về | SS05-WB3-FR2 (toán hạng 2) | - |
| SS05-WB3-M08 | 8 | SS05-WB3-L01 | SS05-WB3-L02 | release(reference, retryAt) | Đồng bộ | SS05-WB3-FR2 (toán hạng 2) | Giao lại sau 1 phút, tối đa 3 lần, sau đó ghi nhật ký cho vận hành |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-TriggerSchedulerService | TriggerSchedulerService | Điều phối | Nhận lời gọi IF-07, ghi và xoá mốc qua kho mốc, hẹn lần quét kế tiếp | package-private | IF-07 |
| DC-TriggerDispatcher | TriggerDispatcher | Điều phối | Mỗi chu kỳ quét chiếm các mốc đến hạn, gọi IF-08, giao lại khi lỗi (tối đa 3 lần cách nhau 1 phút, Thiết kế: lỗi tạm thời của bên xử lý), ghi nhật ký khi hết lần | package-private | - |
| DC-TriggerStore | TriggerStore | Giao tiếp ngoài | Kho mốc bền trong CSDL; chiếm mốc bằng cập nhật có điều kiện để nhiều bản back-end không xử lý trùng một mốc (P09 F1-08) | package-private | - |
| DC-TriggerKind | TriggerKind | Kiểu dữ liệu | Loại mốc: HoldExpiry / PhoneReservationExpiry / PassengerListDispatch | public (thuộc chữ ký IF-07) | - |
| DC-TriggerStoreUnavailableException | TriggerStoreUnavailableException | Ngoại lệ | Kho mốc không sẵn sàng | public (thuộc chữ ký IF-07) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-05 | Subsystem | SS-05 TriggerScheduling | «subsystem» | - | - | 40 | 190 | 480 | 260 |
| IF-07 | Interface | IF-07 ITriggerScheduler | «interface» | PKG-19 | - | 60 | 40 | 200 | 90 |
| IF-08 | Interface | IF-08 ITriggerHandler | «interface» | PKG-19 | - | 300 | 40 | 200 | 70 |
| DC-TriggerSchedulerService | Class | DC-TriggerSchedulerService | «control» | SS-05 | - | 60 | 230 | 200 | 70 |
| DC-TriggerDispatcher | Class | DC-TriggerDispatcher | «control» | SS-05 | - | 300 | 230 | 200 | 70 |
| DC-TriggerStore | Class | DC-TriggerStore | «adapter» | SS-05 | - | 300 | 360 | 200 | 70 |
| ACT-10 | Actor | Bộ định thời (ACT-10) | - | - | - | 560 | 360 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS05-EL-E01 | DC-TriggerSchedulerService | IF-07 | Realization | - | Subsystem hiện thực IF-07 qua lớp điều phối | - |
| SS05-EL-E02 | DC-TriggerDispatcher | IF-08 | Dependency | gọi | Gọi ngược lên bên hiện thực IF-08 | - |
| SS05-EL-E03 | DC-TriggerSchedulerService | DC-TriggerStore | Association (điều hướng) | ghi, xoá | - | (160,320); (390,320) |
| SS05-EL-E04 | DC-TriggerDispatcher | DC-TriggerStore | Association (điều hướng) | chiếm, đánh dấu | - | (400,330); (410,330) |
| SS05-EL-E05 | ACT-10 | DC-TriggerStore | Association | chu kỳ thời gian | Bộ định thời kích hoạt chu kỳ quét; DC-TriggerDispatcher nhận onTimer qua kho | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-05 | IF-08 | Qua interface | Gọi ngược mốc đến hạn lên layer trên theo P09 R5; subsystem không phụ thuộc package nào (P10 F4) | Ưu tiên |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-09 | Package | PKG-09 TicketSalesService | - | - | - | 60 | 40 | 200 | 60 |
| PKG-10 | Package | PKG-10 TripOperationsService | - | - | - | 300 | 40 | 200 | 60 |
| IF-07 | Interface | IF-07 ITriggerScheduler | «interface» | - | - | 60 | 170 | 200 | 50 |
| IF-08 | Interface | IF-08 ITriggerHandler | «interface» | - | - | 300 | 170 | 200 | 50 |
| SS-05 | Subsystem | SS-05 TriggerScheduling | - | - | - | 180 | 280 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS05-DP-E01 | PKG-09 | IF-07 | Dependency | dùng | - | - |
| SS05-DP-E02 | PKG-10 | IF-07 | Dependency | dùng | - | (400,130); (170,130) |
| SS05-DP-E03 | PKG-09 | IF-08 | Realization | DC-BookTicketOnlineService | - | (170,140); (400,140) |
| SS05-DP-E04 | SS-05 | IF-07 | Realization | - | - | (270,240); (160,240) |
| SS05-DP-E05 | SS-05 | IF-08 | Dependency | gọi ngược | - | (290,250); (400,250) |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| scheduleTrigger | Kho mốc không sẵn sàng | Kỹ thuật tạm thời | Lỗi kết nối hoặc hết thời gian 5 giây | Không thử lại trong subsystem (caller chịu giao dịch giữ chỗ) | TriggerStoreUnavailableException | Không có (UC-002 bước 9 chưa có luồng) | Q-104 |
| cancelTriggers | Kho mốc không sẵn sàng | Kỹ thuật tạm thời | Lỗi kết nối hoặc hết thời gian 5 giây | Không thử lại trong subsystem | TriggerStoreUnavailableException | Không có (UC-013 bước 5 chưa có luồng) | Q-104 |
| handleTrigger | Bên xử lý ném ngoại lệ hoặc quá 60 giây | Kỹ thuật tạm thời | Ngoại lệ hoặc hết thời gian | Giao lại sau 1 phút, tối đa 3 lần (an toàn vì handleTrigger idempotent); hết lần thì ghi nhật ký cho vận hành | Không trả cho client | UC-002 9a | Q-82 (sai số mốc) |
| handleTrigger | Hai bản back-end cùng chiếm một mốc | Kỹ thuật | Cập nhật có điều kiện của claimDue | Chỉ bản chiếm được xử lý | Không có | - | - |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-07 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: IF-08 |
| Không phần tử bên trong subsystem nào public | Đạt |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt |

## SS-06 ServerApiAccess

Package chứa: PKG-21. Tác nhân hoặc đối tượng ngoài: Máy chủ.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-015 Soát vé lên xe | AC-C-CheckBoardingTicketController (DC-CheckBoardingTicketService) | SD1: 3.1.1 // sendResult (AC-E-TicketCheckSession, bước 10; P10 giao việc gửi cho DC-CheckBoardingTicketService); 3.1.1.2 // keepResultPending (luồng 10a) | kết quả soát vé của chuyến | 10a (mất sóng, ASM-52). Máy chủ từ chối kết quả: chưa có luồng (Q-105) |
| UC-015 Soát vé lên xe (tiền điều kiện) và UC-014 (chưa có P07) | DC-CheckBoardingTicketService | Không có message trong P07 (ASM-32: danh sách đã có trên máy); nguồn là P09 F7, Q-81 | mã chuyến, danh sách hành khách | Máy mất sóng lúc lấy danh sách: chưa có luồng (Q-81) |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-09 | IServerApiClient | Lấy danh sách hành khách và gửi kết quả soát vé giữa máy soát vé và máy chủ | SS-06 | DC-CheckBoardingTicketService (PKG-11) | PKG-21 |
| IF-14 | IResultDeliveryListener | Báo kết quả soát vé đã gửi được sau khi bị hoãn (chiều ngược): bên cung cấp DC-CheckBoardingTicketService (PKG-11), bên dùng SS-06 | DC-CheckBoardingTicketService (PKG-11), hiện thực ở layer trên | SS-06 | PKG-21 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-09 | IServerApiClient | Máy chủ (đối với máy soát vé) | fetchPassengerList(tripId: String): TripPassengerList | tripId: String - mã chuyến cần lấy danh sách, không rỗng | TripPassengerList: danh sách vé của chuyến (mã vé, chỗ, họ tên người đi, trạng thái vé; nội dung chính xác chờ Q-45) | ServerUnavailableException (Kỹ thuật tạm thời); ServerRejectedException (Nghiệp vụ, chuyến không có danh sách) | UC-015 (tiền điều kiện: chuyến đã có danh sách trên máy, ASM-32); UC-014 (cấp danh sách, chưa có P07). Cách máy lấy danh sách: Q-81 | Máy có kết nối tới máy chủ | Danh sách của chuyến có trên máy sau khi client lưu qua IF-12 | Đồng bộ | Có (chỉ đọc) | Kết nối 5 giây, đọc 30 giây (Thiết kế: mạng di động yếu, danh sách tối đa vài chục vé nên dung lượng nhỏ); không tự thử lại, client thử lại khi có sóng (Q-81) |
| IF-09 | IServerApiClient | Máy chủ (đối với máy soát vé) | submitCheckResult(session: TicketCheckSession): SubmitResult | session: TicketCheckSession - phiên soát vé đã kết thúc, có kết quả soát của chuyến (ASM-51) | SubmitResult: status (Delivered / Deferred) | ServerRejectedException (Nghiệp vụ, máy chủ từ chối kết quả); lỗi kết nối được chuyển thành status Deferred, không phải ngoại lệ | UC-015 (bước 10, luồng 10a: SD1 3.1.1 // sendResult; ASM-52) | Phiên soát vé của chuyến đã kết thúc | Delivered: máy chủ đã nhận kết quả. Deferred: kết quả nằm trong hàng đợi gửi lại, sẽ tự gửi khi có sóng và báo qua IF-14 | Đồng bộ (gửi lần đầu); gửi lại bất đồng bộ trong nền | Có với khoá tripId (máy chủ bỏ qua kết quả đã nhận của cùng chuyến và phiên) | Kết nối 5 giây, đọc 15 giây; gửi lại sau 30 giây, gấp đôi mỗi lần, tối đa cách nhau 5 phút, không giới hạn số lần (Thiết kế: P04 10a yêu cầu tự gửi khi máy có sóng trở lại; khoảng cách tối đa cân bằng pin và độ trễ) |
| IF-14 | IResultDeliveryListener | Máy chủ (đối với máy soát vé), gọi ngược | onResultDelivered(tripId: String): void | tripId: String - mã chuyến có kết quả soát vừa gửi được sau khi bị hoãn | void | - | UC-015 (luồng 10a: kết quả tự gửi sau khi use case kết thúc, ASM-52). Interface mới của P11b, lý do: gửi lại hoàn tất sau use case nên cần báo ngược để đánh dấu Đã gửi (markResultSent) | Kết quả của chuyến đang ở trạng thái Chờ gửi | Bên hiện thực đánh dấu phiên của chuyến là Đã gửi | Bất đồng bộ (SS-06 gọi vào từ luồng nền) | Có (đánh dấu lại phiên đã Đã gửi không đổi) | 5 giây (Thiết kế: ghi một trạng thái cục bộ) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-06.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

Mọi operation của IF-09, IF-14 có trang hộp trắng.

#### Trang "Hộp đen - UC-015 fetchPassengerList và submitCheckResult"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-BB1-L01 | Lifeline | :DC-CheckBoardingTicketService | «control» | - | Control của UC-015, hiện thực IF-14 | 40 | 40 | 120 | 820 |
| SS06-BB1-L02 | Lifeline | :IF-09 IServerApiClient | «interface» | - | Interface của SS-06 | 200 | 40 | 120 | 820 |
| SS06-BB1-FR1 | Fragment | alt [lấy được danh sách] | alt | - | Kết quả của fetchPassengerList | 30 | 160 | 300 | 160 |
| SS06-BB1-FR1-O2 | Fragment | [ServerUnavailableException] | alt | SS06-BB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS06-BB1-FR1-SEP2 | 40 | 230 | 280 | 20 |
| SS06-BB1-FR2 | Fragment | alt [status = Delivered] | alt | - | Kết quả của submitCheckResult | 30 | 400 | 300 | 310 |
| SS06-BB1-FR2-O2 | Fragment | [status = Deferred] | alt | SS06-BB1-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS06-BB1-FR2-SEP2 | 40 | 510 | 280 | 20 |
| SS06-BB1-FR2-O3 | Fragment | [ServerRejectedException] | alt | SS06-BB1-FR2 | Toán hạng 3, ngăn bởi đường nét đứt SS06-BB1-FR2-SEP3 | 40 | 620 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-BB1-M01 | 1 | SS06-BB1-L01 | SS06-BB1-L02 | fetchPassengerList(tripId) | Đồng bộ | - | UC-015 tiền điều kiện (ASM-32) |
| SS06-BB1-M02 | 2 | SS06-BB1-L02 | SS06-BB1-L01 | TripPassengerList | Trả về | SS06-BB1-FR1 (toán hạng 1) | UC-015 |
| SS06-BB1-M03 | 3 | SS06-BB1-L02 | SS06-BB1-L01 | ServerUnavailableException | Trả về | SS06-BB1-FR1 (toán hạng 2) | UC-015 |
| SS06-BB1-M04 | 4 | SS06-BB1-L01 | SS06-BB1-L01 | chưa có luồng P04 (chờ Q-81) | Tự gọi | SS06-BB1-FR1 (toán hạng 2) | Q-81 |
| SS06-BB1-M05 | 5 | SS06-BB1-L01 | SS06-BB1-L02 | submitCheckResult(session) | Đồng bộ | - | UC-015 bước 10 |
| SS06-BB1-M06 | 6 | SS06-BB1-L02 | SS06-BB1-L01 | SubmitResult(status = Delivered) | Trả về | SS06-BB1-FR2 (toán hạng 1) | UC-015 bước 10 |
| SS06-BB1-M07 | 7 | SS06-BB1-L01 | SS06-BB1-L01 | markResultSent | Tự gọi | SS06-BB1-FR2 (toán hạng 1) | UC-015 bước 10 |
| SS06-BB1-M08 | 8 | SS06-BB1-L02 | SS06-BB1-L01 | SubmitResult(status = Deferred) | Trả về | SS06-BB1-FR2 (toán hạng 2) | UC-015 luồng 10a |
| SS06-BB1-M09 | 9 | SS06-BB1-L01 | SS06-BB1-L01 | keepResultPending | Tự gọi | SS06-BB1-FR2 (toán hạng 2) | UC-015 luồng 10a |
| SS06-BB1-M10 | 10 | SS06-BB1-L02 | SS06-BB1-L01 | ServerRejectedException | Trả về | SS06-BB1-FR2 (toán hạng 3) | UC-015 bước 10 |
| SS06-BB1-M11 | 11 | SS06-BB1-L01 | SS06-BB1-L01 | chưa có luồng P04 (Q-105) | Tự gọi | SS06-BB1-FR2 (toán hạng 3) | Q-105 |
| SS06-BB1-M12 | 12 | SS06-BB1-L02 | SS06-BB1-L01 | onResultDelivered(tripId) | Bất đồng bộ | - | UC-015 luồng 10a, IF-14 |
| SS06-BB1-M13 | 13 | SS06-BB1-L01 | SS06-BB1-L01 | markResultSent | Tự gọi | - | UC-015 luồng 10a |

#### Trang "Hộp trắng - fetchPassengerList"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-WB1-FRM | Fragment | sd fetchPassengerList | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 760 |
| SS06-WB1-L01 | Lifeline | :DC-ServerApiClientService | «control» | - | Lớp điều phối, hiện thực IF-09 | 120 | 40 | 120 | 700 |
| SS06-WB1-L02 | Lifeline | :DC-ApiDataConverter | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 700 |
| SS06-WB1-L03 | Lifeline | :DC-ServerHttpClient | «adapter» | - | Lớp giao tiếp ngoài | 440 | 40 | 120 | 700 |
| SS06-WB1-L04 | Actor | Máy chủ | «DC-BoardingSyncRestController» | - | PKG-08, qua REST | 600 | 40 | 120 | 700 |
| SS06-WB1-G1 | Gate | fetchPassengerList | - | SS06-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS06-WB1-G1-2 | Gate | fetchPassengerList | - | SS06-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 410 | 20 | 20 |
| SS06-WB1-G1-3 | Gate | fetchPassengerList | - | SS06-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 520 | 20 | 20 |
| SS06-WB1-G1-4 | Gate | fetchPassengerList | - | SS06-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 660 | 20 | 20 |
| SS06-WB1-FR1 | Fragment | alt [máy chủ trả danh sách] | alt | - | Kết quả của lời gọi máy chủ | 110 | 240 | 620 | 310 |
| SS06-WB1-FR1-O2 | Fragment | [lỗi mạng] | alt | SS06-WB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS06-WB1-FR1-SEP2 | 120 | 350 | 600 | 20 |
| SS06-WB1-FR1-O3 | Fragment | [máy chủ từ chối] | alt | SS06-WB1-FR1 | Toán hạng 3, ngăn bởi đường nét đứt SS06-WB1-FR1-SEP3 | 120 | 460 | 600 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-WB1-M01 | 1 | SS06-WB1-G1 | SS06-WB1-L01 | fetchPassengerList(tripId) | Đồng bộ | - | UC-015 / UC-014 |
| SS06-WB1-M02 | 2 | SS06-WB1-L01 | SS06-WB1-L03 | get(passengerListPath(tripId)) | Đồng bộ | - | Gắn thông tin xác thực của máy |
| SS06-WB1-M03 | 3 | SS06-WB1-L03 | SS06-WB1-L04 | yêu cầu danh sách hành khách của chuyến | Đồng bộ | - | - |
| SS06-WB1-M04 | 4 | SS06-WB1-L04 | SS06-WB1-L03 | dữ liệu danh sách | Trả về | SS06-WB1-FR1 (toán hạng 1) | - |
| SS06-WB1-M05 | 5 | SS06-WB1-L03 | SS06-WB1-L01 | PassengerListDto | Trả về | SS06-WB1-FR1 (toán hạng 1) | - |
| SS06-WB1-M06 | 6 | SS06-WB1-L03 | SS06-WB1-L01 | ConnectionFailed hoặc Timeout | Trả về | SS06-WB1-FR1 (toán hạng 2) | - |
| SS06-WB1-M07 | 7 | SS06-WB1-L01 | SS06-WB1-G1-2 | ServerUnavailableException | Trả về | SS06-WB1-FR1 (toán hạng 2) | Cô lập lỗi mạng |
| SS06-WB1-M08 | 8 | SS06-WB1-L03 | SS06-WB1-L01 | Rejected (mã lỗi nghiệp vụ) | Trả về | SS06-WB1-FR1 (toán hạng 3) | - |
| SS06-WB1-M09 | 9 | SS06-WB1-L01 | SS06-WB1-G1-3 | ServerRejectedException | Trả về | SS06-WB1-FR1 (toán hạng 3) | - |
| SS06-WB1-M10 | 10 | SS06-WB1-L01 | SS06-WB1-L02 | toTripPassengerList(passengerListDto) | Đồng bộ | - | - |
| SS06-WB1-M11 | 11 | SS06-WB1-L02 | SS06-WB1-L01 | TripPassengerList | Trả về | - | - |
| SS06-WB1-M12 | 12 | SS06-WB1-L01 | SS06-WB1-G1-4 | TripPassengerList | Trả về | - | - |

#### Trang "Hộp trắng - submitCheckResult"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-WB2-FRM | Fragment | sd submitCheckResult | - | - | Khung sơ đồ của operation | 20 | 20 | 900 | 800 |
| SS06-WB2-L01 | Lifeline | :DC-ServerApiClientService | «control» | - | Lớp điều phối, hiện thực IF-09 | 120 | 40 | 120 | 740 |
| SS06-WB2-L02 | Lifeline | :DC-ApiDataConverter | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 740 |
| SS06-WB2-L03 | Lifeline | :DC-ServerHttpClient | «adapter» | - | Lớp giao tiếp ngoài | 440 | 40 | 120 | 740 |
| SS06-WB2-L04 | Lifeline | :DC-ResultOutbox | «outbox» | - | Hàng đợi gửi lại bền trên máy | 600 | 40 | 120 | 740 |
| SS06-WB2-L05 | Actor | Máy chủ | «DC-BoardingSyncRestController» | - | PKG-08, qua REST | 760 | 40 | 120 | 740 |
| SS06-WB2-G1 | Gate | submitCheckResult | - | SS06-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS06-WB2-G1-2 | Gate | submitCheckResult | - | SS06-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 420 | 20 | 20 |
| SS06-WB2-G1-3 | Gate | submitCheckResult | - | SS06-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 570 | 20 | 20 |
| SS06-WB2-G1-4 | Gate | submitCheckResult | - | SS06-WB2-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 680 | 20 | 20 |
| SS06-WB2-FR1 | Fragment | alt [máy chủ xác nhận] | alt | - | Kết quả của lần gửi đầu | 110 | 320 | 780 | 390 |
| SS06-WB2-FR1-O2 | Fragment | [mất sóng hoặc hết thời gian] | alt | SS06-WB2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS06-WB2-FR1-SEP2 | 120 | 470 | 760 | 20 |
| SS06-WB2-FR1-O3 | Fragment | [máy chủ từ chối] | alt | SS06-WB2-FR1 | Toán hạng 3, ngăn bởi đường nét đứt SS06-WB2-FR1-SEP3 | 120 | 620 | 760 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-WB2-M01 | 1 | SS06-WB2-G1 | SS06-WB2-L01 | submitCheckResult(session) | Đồng bộ | - | UC-015 bước 10 |
| SS06-WB2-M02 | 2 | SS06-WB2-L01 | SS06-WB2-L02 | toCheckResultDto(session) | Đồng bộ | - | - |
| SS06-WB2-M03 | 3 | SS06-WB2-L02 | SS06-WB2-L01 | CheckResultDto | Trả về | - | - |
| SS06-WB2-M04 | 4 | SS06-WB2-L01 | SS06-WB2-L03 | post(checkResultPath, checkResultDto, idempotencyKey = tripId) | Đồng bộ | - | - |
| SS06-WB2-M05 | 5 | SS06-WB2-L03 | SS06-WB2-L05 | gửi kết quả soát vé của chuyến | Đồng bộ | - | - |
| SS06-WB2-M06 | 6 | SS06-WB2-L05 | SS06-WB2-L03 | xác nhận đã nhận | Trả về | SS06-WB2-FR1 (toán hạng 1) | - |
| SS06-WB2-M07 | 7 | SS06-WB2-L03 | SS06-WB2-L01 | Ok | Trả về | SS06-WB2-FR1 (toán hạng 1) | - |
| SS06-WB2-M08 | 8 | SS06-WB2-L01 | SS06-WB2-G1-2 | SubmitResult(Delivered) | Trả về | SS06-WB2-FR1 (toán hạng 1) | - |
| SS06-WB2-M09 | 9 | SS06-WB2-L03 | SS06-WB2-L01 | ConnectionFailed hoặc Timeout | Trả về | SS06-WB2-FR1 (toán hạng 2) | Mất sóng, luồng 10a |
| SS06-WB2-M10 | 10 | SS06-WB2-L01 | SS06-WB2-L04 | enqueue(tripId, checkResultDto) | Đồng bộ | SS06-WB2-FR1 (toán hạng 2) | Giữ bền để gửi lại |
| SS06-WB2-M11 | 11 | SS06-WB2-L01 | SS06-WB2-G1-3 | SubmitResult(Deferred) | Trả về | SS06-WB2-FR1 (toán hạng 2) | - |
| SS06-WB2-M12 | 12 | SS06-WB2-L03 | SS06-WB2-L01 | Rejected (mã lỗi nghiệp vụ) | Trả về | SS06-WB2-FR1 (toán hạng 3) | - |
| SS06-WB2-M13 | 13 | SS06-WB2-L01 | SS06-WB2-G1-4 | ServerRejectedException | Trả về | SS06-WB2-FR1 (toán hạng 3) | - |

#### Trang "Hộp trắng - gửi lại và onResultDelivered"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-WB3-FRM | Fragment | sd onResultDelivered | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 700 |
| SS06-WB3-L01 | Lifeline | :DC-ResultRedeliveryWorker | «control» | - | Lớp điều phối gửi lại, chạy nền khi có mạng | 120 | 40 | 120 | 640 |
| SS06-WB3-L02 | Lifeline | :DC-ResultOutbox | «outbox» | - | Hàng đợi gửi lại bền trên máy | 280 | 40 | 120 | 640 |
| SS06-WB3-L03 | Lifeline | :DC-ServerHttpClient | «adapter» | - | Lớp giao tiếp ngoài | 440 | 40 | 120 | 640 |
| SS06-WB3-L04 | Actor | Máy chủ | «DC-BoardingSyncRestController» | - | PKG-08, qua REST | 600 | 40 | 120 | 640 |
| SS06-WB3-G1 | Gate | onResultDelivered | - | SS06-WB3-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 450 | 20 | 20 |
| SS06-WB3-FR1 | Fragment | loop [còn mục chờ gửi] | loop | - | Gửi lại tới khi hết hàng đợi | 110 | 120 | 620 | 490 |
| SS06-WB3-FR2 | Fragment | alt [máy chủ xác nhận] | alt | - | Kết quả của lần gửi lại | 120 | 350 | 440 | 240 |
| SS06-WB3-FR2-O2 | Fragment | [chưa gửi được] | alt | SS06-WB3-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS06-WB3-FR2-SEP2 | 130 | 500 | 420 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-WB3-M01 | 1 | SS06-WB3-L01 | SS06-WB3-L02 | peekNext() | Đồng bộ | SS06-WB3-FR1 (toán hạng 1) | Khi có mạng trở lại hoặc đến lượt gửi lại |
| SS06-WB3-M02 | 2 | SS06-WB3-L02 | SS06-WB3-L01 | mục chờ gửi (tripId, checkResultDto) | Trả về | SS06-WB3-FR1 (toán hạng 1) | - |
| SS06-WB3-M03 | 3 | SS06-WB3-L01 | SS06-WB3-L03 | post(checkResultPath, checkResultDto, idempotencyKey = tripId) | Đồng bộ | SS06-WB3-FR1 (toán hạng 1) | - |
| SS06-WB3-M04 | 4 | SS06-WB3-L03 | SS06-WB3-L04 | gửi kết quả soát vé của chuyến | Đồng bộ | SS06-WB3-FR1 (toán hạng 1) | - |
| SS06-WB3-M05 | 5 | SS06-WB3-L04 | SS06-WB3-L03 | xác nhận đã nhận | Trả về | SS06-WB3-FR1 (toán hạng 1) | - |
| SS06-WB3-M06 | 6 | SS06-WB3-L03 | SS06-WB3-L01 | Ok | Trả về | SS06-WB3-FR2 (toán hạng 1) | - |
| SS06-WB3-M07 | 7 | SS06-WB3-L01 | SS06-WB3-L02 | remove(tripId) | Đồng bộ | SS06-WB3-FR2 (toán hạng 1) | - |
| SS06-WB3-M08 | 8 | SS06-WB3-L01 | SS06-WB3-G1 | onResultDelivered(tripId) | Bất đồng bộ | SS06-WB3-FR2 (toán hạng 1) | IF-14 do DC-CheckBoardingTicketService hiện thực |
| SS06-WB3-M09 | 9 | SS06-WB3-L03 | SS06-WB3-L01 | ConnectionFailed hoặc Timeout | Trả về | SS06-WB3-FR2 (toán hạng 2) | - |
| SS06-WB3-M10 | 10 | SS06-WB3-L01 | SS06-WB3-L01 | reschedule(backoff gấp đôi, tối đa 5 phút) | Tự gọi | SS06-WB3-FR2 (toán hạng 2) | Thiết kế: giảm tải pin và mạng |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-ServerApiClientService | ServerApiClientService | Điều phối | Nhận lời gọi IF-09, gọi máy chủ, chuyển lỗi mạng thành Deferred hoặc ngoại lệ | package-private | IF-09 |
| DC-ServerHttpClient | ServerHttpClient | Giao tiếp ngoài | Gọi HTTP tới API máy chủ: xác thực của máy, timeout, kết nối mã hoá cho dữ liệu cá nhân (P09 F7) | package-private | - |
| DC-ApiDataConverter | ApiDataConverter | Chuyển đổi dữ liệu | Chuyển giữa TripPassengerList, TicketCheckSession và dữ liệu truyền | package-private | - |
| DC-ResultOutbox | ResultOutbox | Lưu tạm | Hàng đợi bền trên máy cho kết quả chưa gửi, sống qua khởi động lại ứng dụng | package-private | - |
| DC-ResultRedeliveryWorker | ResultRedeliveryWorker | Điều phối | Chạy nền, gửi lại khi có mạng, gọi IF-14 sau khi gửi được | package-private | - |
| DC-SubmitResult | SubmitResult | Kiểu dữ liệu | Kết quả của submitCheckResult (status) | public (thuộc chữ ký IF-09) | - |
| DC-ServerUnavailableException | ServerUnavailableException | Ngoại lệ | Lỗi mạng hoặc máy chủ tạm thời không sẵn sàng | public (thuộc chữ ký IF-09) | - |
| DC-ServerRejectedException | ServerRejectedException | Ngoại lệ | Máy chủ từ chối yêu cầu vì lý do nghiệp vụ | public (thuộc chữ ký IF-09) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-06 | Subsystem | SS-06 ServerApiAccess | «subsystem» | - | - | 40 | 190 | 720 | 270 |
| IF-09 | Interface | IF-09 IServerApiClient | «interface» | PKG-21 | - | 300 | 40 | 200 | 90 |
| IF-14 | Interface | IF-14 IResultDeliveryListener | «interface» | PKG-21 | - | 540 | 40 | 200 | 70 |
| DC-ServerApiClientService | Class | DC-ServerApiClientService | «control» | SS-06 | - | 300 | 230 | 200 | 70 |
| DC-ResultRedeliveryWorker | Class | DC-ResultRedeliveryWorker | «control» | SS-06 | - | 540 | 230 | 200 | 70 |
| DC-ApiDataConverter | Class | DC-ApiDataConverter | «converter» | SS-06 | - | 60 | 370 | 200 | 70 |
| DC-ResultOutbox | Class | DC-ResultOutbox | «outbox» | SS-06 | - | 300 | 370 | 200 | 70 |
| DC-ServerHttpClient | Class | DC-ServerHttpClient | «adapter» | SS-06 | - | 540 | 370 | 200 | 70 |
| ACT-SRV | Actor | Máy chủ (PKG-08) | - | - | - | 800 | 370 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS06-EL-E01 | DC-ServerApiClientService | IF-09 | Realization | - | Subsystem hiện thực IF-09 qua lớp điều phối | - |
| SS06-EL-E02 | DC-ResultRedeliveryWorker | IF-14 | Dependency | gọi | Gọi ngược lên bên hiện thực IF-14 | - |
| SS06-EL-E03 | DC-ServerApiClientService | DC-ApiDataConverter | Association (điều hướng) | dùng | - | (390,320); (160,320) |
| SS06-EL-E04 | DC-ServerApiClientService | DC-ServerHttpClient | Association (điều hướng) | dùng | - | (410,330); (640,330) |
| SS06-EL-E05 | DC-ResultRedeliveryWorker | DC-ResultOutbox | Association (điều hướng) | đọc, xoá | - | (640,340); (400,340) |
| SS06-EL-E06 | DC-ServerHttpClient | ACT-SRV | Association | REST | - | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-06 | IF-14 | Qua interface | Báo gửi lại xong lên layer trên theo P09 R5 | Ưu tiên |
| SS-06 | PKG-24 | Vào package | TripPassengerList, TicketCheckSession có trong chữ ký IF-09 (P10 F4: PKG-21 --> PKG-24); Domain nằm dưới Services | Dùng thận trọng |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-11 | Package | PKG-11 BoardingCheckService | - | - | - | 180 | 40 | 200 | 60 |
| IF-09 | Interface | IF-09 IServerApiClient | «interface» | - | - | 60 | 160 | 200 | 50 |
| IF-14 | Interface | IF-14 IResultDeliveryListener | «interface» | - | - | 300 | 160 | 200 | 50 |
| SS-06 | Subsystem | SS-06 ServerApiAccess | - | - | - | 180 | 270 | 200 | 60 |
| PKG-24 | Package | PKG-24 BoardingModel | - | - | - | 180 | 380 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS06-DP-E01 | PKG-11 | IF-09 | Dependency | dùng | - | (270,120); (160,120) |
| SS06-DP-E02 | PKG-11 | IF-14 | Realization | DC-CheckBoardingTicketService | - | (290,130); (400,130) |
| SS06-DP-E03 | SS-06 | IF-09 | Realization | - | - | (270,230); (160,230) |
| SS06-DP-E04 | SS-06 | IF-14 | Dependency | gọi ngược | - | (290,240); (400,240) |
| SS06-DP-E05 | SS-06 | PKG-24 | Dependency | TripPassengerList, TicketCheckSession | - | - |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| fetchPassengerList | Mất sóng hoặc hết thời gian | Kỹ thuật tạm thời | Lỗi kết nối hoặc hết thời gian 30 giây | Không thử lại trong subsystem | ServerUnavailableException | Không có | Q-81 |
| fetchPassengerList | Máy chủ báo chuyến không có danh sách | Nghiệp vụ | Mã lỗi của máy chủ | Chuyển thành ngoại lệ | ServerRejectedException | Không có (liên quan đề xuất sửa P04 UC-015 bước 1, 2) | Q-81, Q-105 |
| submitCheckResult | Mất sóng hoặc hết thời gian | Kỹ thuật tạm thời | Lỗi kết nối hoặc hết thời gian 15 giây | Đưa vào ResultOutbox, gửi lại gấp đôi khoảng cách tối đa 5 phút; operation idempotent theo tripId | SubmitResult(Deferred), sau đó IF-14 | UC-015 10a | - |
| submitCheckResult | Máy chủ từ chối kết quả | Nghiệp vụ | Mã lỗi của máy chủ | Không gửi lại (gửi lại vẫn bị từ chối), chuyển thành ngoại lệ | ServerRejectedException | Không có | Q-105 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-09 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: IF-14 |
| Không phần tử bên trong subsystem nào public | Đạt |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt |

## SS-07 ServerPersistence

Package chứa: PKG-14. Tác nhân hoặc đối tượng ngoài: CSDL.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-002 Đặt vé trực tuyến | DC-BookTicketOnlineService | SD1: 1.1.1 // findMatchingTrips (Trip); 3.1.1 // createBooking, 3.1.6 // holdSeats (Booking, Seat); 3.1.11 // issueTickets (Booking, Ticket) - phần lưu của các entity | chuyến, chỗ, lần đặt, vé | 2a (không có chuyến), 6b (chỗ không còn trống). Hai phiên cùng giữ một chỗ ở bước 9: chưa có luồng (Q-106); kho dữ liệu lỗi: Q-104 |
| UC-008 Trả vé | DC-ReturnTicketService | SD1: 1.1.1 // findTicket; 2.1.3 // cancelTicket, 2.1.3.1 // release, 2.1.3.2 // createRefund - phần lưu | vé, chỗ, khoản hoàn | 2a, 2b. Kho dữ liệu lỗi: Q-104 |
| UC-013 Huỷ chuyến | DC-CancelTripService | SD1: 1.1.1 // findTrip; 1.1.4 // getCancellationSummary; 2.1.1 // cancelTrip; 2.1.6 // recordRefund - phần lưu | chuyến, vé, đặt chỗ qua điện thoại, khoản hoàn | 2a, 2b, 2c, 4a. Kho dữ liệu lỗi: Q-104 |
| UC-015 Soát vé lên xe (phía máy chủ) | DC-CheckBoardingTicketService (back-end) | SD1: 3.1.1 // sendResult (phía nhận kết quả); P10 giao DC-BoardingSyncRestController nhận | phiên soát vé, kết quả soát | Kho dữ liệu lỗi: Q-104 |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-10 | ITripCatalogRepository | Lưu và truy xuất tuyến, chuyến, chỗ, giá | SS-07 | DC-BookTicketOnlineService, DC-ReturnTicketService (PKG-09); DC-CancelTripService (PKG-10); DC-CheckBoardingTicketService (PKG-11) | PKG-22 |
| IF-11 | ITicketingRepository | Lưu và truy xuất lần đặt, vé, đặt chỗ qua điện thoại, khoản hoàn | SS-07 | DC-BookTicketOnlineService, DC-ReturnTicketService (PKG-09); DC-CancelTripService (PKG-10); DC-CheckBoardingTicketService (PKG-11) | PKG-23 |
| IF-12 | IBoardingRepository | Lưu và truy xuất danh sách hành khách, phiên soát vé (hiện thực ở máy chủ bởi SS-07 và trên máy soát vé bởi SS-08) | SS-07, SS-08 | DC-CheckBoardingTicketService (PKG-11) | PKG-24 |
| IF-13 | IAccountRepository | Lưu và truy xuất tài khoản hành khách (giữ chỗ) | SS-07 | Chưa có (AccountService chưa có lớp) | PKG-25 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-10 | ITripCatalogRepository | CSDL quan hệ (PostgreSQL) | findTrips(origin: String, destination: String, departureDate: Date): List<Trip> | origin: String - điểm đi<br>destination: String - điểm đến<br>departureDate: Date - ngày đi, không trước ngày hiện tại (ASM-15) | List<Trip>: các chuyến khớp, rỗng khi không có chuyến (luồng 2a) | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-002 (bước 2, SD1 1.1.1 // findMatchingTrips) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-10 | ITripCatalogRepository | CSDL quan hệ (PostgreSQL) | findTrip(route: String, departureDateTime: DateTime): Trip | route: String - tuyến<br>departureDateTime: DateTime - giờ xuất bến | Trip: chuyến khớp, null khi không có chuyến | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-013 (bước 2, SD1 1.1.1 // findTrip); UC-015 (bước 2, SD1 1.1.1 // findTrip) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-10 | ITripCatalogRepository | CSDL quan hệ (PostgreSQL) | findTripById(tripId: String): Trip | tripId: String - mã chuyến, không rỗng | Trip: chuyến, null khi không có | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-002 (bước 3, 4: chọn chuyến, sơ đồ chỗ); UC-008 (bước 5: chuyến của vé) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-10 | ITripCatalogRepository | CSDL quan hệ (PostgreSQL) | saveTrip(trip: Trip): void | trip: Trip - chuyến cùng trạng thái các chỗ đã đổi (giữ, trả) hoặc trạng thái chuyến | void | SeatAlreadyHeldException (Nghiệp vụ); PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-002 (bước 9: giữ chỗ; luồng 9a: trả chỗ); UC-008 (bước 10: trả chỗ của vé) | Trip đã đọc trước đó (mang phiên bản đọc) | Trạng thái chỗ ghi bền bằng cập nhật có điều kiện; hai phiên cùng giữ một chỗ thì một bên thành công (P09 F7, REQ-67) | Đồng bộ | Có (ghi lại cùng trạng thái không đổi dữ liệu) | 10 giây (Thiết kế: như truy vấn; giao dịch ngắn, không giữ qua lời gọi hệ thống ngoài) |
| IF-11 | ITicketingRepository | CSDL quan hệ (PostgreSQL) | saveBooking(booking: Booking): void | booking: Booking - lần đặt cùng các vé đã phát hành và trạng thái | void | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-002 (bước 9: ghi lần đặt đang giữ; bước 11: phát hành vé) | - | Lần đặt và vé ghi bền trong cùng giao dịch của lớp dịch vụ gọi | Đồng bộ | Có (khoá mã lần đặt, ghi lại cùng nội dung không tạo bản ghi mới) | 10 giây (Thiết kế: như truy vấn; giao dịch ngắn, không giữ qua lời gọi hệ thống ngoài) |
| IF-11 | ITicketingRepository | CSDL quan hệ (PostgreSQL) | findBooking(bookingId: String): Booking | bookingId: String - mã lần đặt, không rỗng | Booking: lần đặt, null khi không có | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-002 (luồng 9a: xử lý hết thời hạn giữ chỗ qua IF-08); UC-003 (kiểm tra trạng thái khi nhận kết quả thanh toán, chưa có P07) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-11 | ITicketingRepository | CSDL quan hệ (PostgreSQL) | findTicket(ticketCode: TicketCode, travelerPhone: PhoneNumber): Ticket | ticketCode: TicketCode - mã vé<br>travelerPhone: PhoneNumber - số điện thoại người đi | Ticket: vé khớp cả hai thông tin, null khi không khớp (luồng 2a của UC-008) | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-008 (bước 2, SD1 1.1.1 // findTicket) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-11 | ITicketingRepository | CSDL quan hệ (PostgreSQL) | findTicketsOfTrip(tripId: String): List<Ticket> | tripId: String - mã chuyến | List<Ticket>: các vé của chuyến, kèm trạng thái | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-013 (bước 3, 5, 6); UC-014 (lập danh sách hành khách, chưa có P07) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-11 | ITicketingRepository | CSDL quan hệ (PostgreSQL) | findPhoneReservationsOfTrip(tripId: String): List<PhoneReservation> | tripId: String - mã chuyến | List<PhoneReservation>: các đặt chỗ qua điện thoại của chuyến | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-013 (bước 3, 5, SD1 1.1.4.2 // checkUnpaid, 2.1.1.2 // cancelWithTrip) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-11 | ITicketingRepository | CSDL quan hệ (PostgreSQL) | saveTicket(ticket: Ticket): void | ticket: Ticket - vé cùng trạng thái và khoản hoàn (Refund) nếu có | void | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-008 (bước 10: huỷ vé, tạo khoản hoàn); UC-013 (bước 9: ghi nhận khoản hoàn của từng vé) | - | Vé và khoản hoàn ghi bền trong một giao dịch | Đồng bộ | Có (khoá mã vé) | 10 giây (Thiết kế: như truy vấn; giao dịch ngắn, không giữ qua lời gọi hệ thống ngoài) |
| IF-11 | ITicketingRepository | CSDL quan hệ (PostgreSQL) | saveTripCancellation(cancellation: TripCancellation): void | cancellation: TripCancellation - chuyến đã huỷ cùng các vé còn hiệu lực và đặt chỗ chưa thanh toán đã huỷ | void | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-013 (bước 5: ghi nhận chuyến đã huỷ, huỷ vé và đặt chỗ). Giao dịch này kết thúc trước khi gọi IF-01 ở bước 7 (không giữ giao dịch qua lời gọi hệ thống ngoài) | - | Chuyến, vé, đặt chỗ ghi bền trong một giao dịch | Đồng bộ | Có (khoá mã chuyến) | 10 giây (Thiết kế: như truy vấn; giao dịch ngắn, không giữ qua lời gọi hệ thống ngoài) |
| IF-12 | IBoardingRepository | CSDL quan hệ (PostgreSQL) | findPassengerList(tripId: String): TripPassengerList | tripId: String - mã chuyến | TripPassengerList: danh sách vé của chuyến, null khi chưa lập | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-014 (cấp danh sách cho máy soát vé qua DC-BoardingSyncRestController, chưa có P07); UC-015 (tiền điều kiện) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-12 | IBoardingRepository | CSDL quan hệ (PostgreSQL) | savePassengerList(list: TripPassengerList): void | list: TripPassengerList - danh sách của chuyến | void | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-014 (lập danh sách tại mốc 15 phút, chưa có P07) | - | Danh sách ghi bền | Đồng bộ | Có (khoá mã chuyến) | 10 giây (Thiết kế: như truy vấn; giao dịch ngắn, không giữ qua lời gọi hệ thống ngoài) |
| IF-12 | IBoardingRepository | CSDL quan hệ (PostgreSQL) | findCheckSession(tripId: String): TicketCheckSession | tripId: String - mã chuyến | TicketCheckSession: phiên soát vé của chuyến, null khi chưa có | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-015 (phía máy chủ khi nhận kết quả, bước 10) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-12 | IBoardingRepository | CSDL quan hệ (PostgreSQL) | saveCheckSession(session: TicketCheckSession): void | session: TicketCheckSession - phiên soát vé cùng kết quả soát | void | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-015 (bước 10: máy chủ ghi kết quả soát nhận từ máy soát vé) | - | Phiên và kết quả ghi bền | Đồng bộ | Có (khoá mã chuyến; nhận lặp cùng kết quả không đổi dữ liệu) | 10 giây (Thiết kế: như truy vấn; giao dịch ngắn, không giữ qua lời gọi hệ thống ngoài) |
| IF-12 | IBoardingRepository | CSDL quan hệ (PostgreSQL) | findPendingCheckSessions(): List<TicketCheckSession> | - | List<TicketCheckSession>: các phiên có kết quả chưa gửi | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-015 (luồng 10a; operation kỹ thuật để gửi lại sau khi ứng dụng khởi động lại, dùng ở máy soát vé, SS-08) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-13 | IAccountRepository | CSDL quan hệ (PostgreSQL) | findAccount(accountId: String): Account | accountId: String - mã tài khoản (Tạm: kiểu Account chưa có DC) | Account: tài khoản, null khi không có | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-009 đến UC-011 (chưa có P07; operation giữ chỗ theo P10 F2) | - | Không thay đổi dữ liệu | Đồng bộ | Có (chỉ đọc) | 10 giây (Thiết kế: giới hạn thời gian câu lệnh để một truy vấn chậm không giữ kết nối khi 2.000 phiên đồng thời, NFR-01; kích thước pool 20 kết nối mỗi bản back-end, chỉnh sau kiểm thử tải) |
| IF-13 | IAccountRepository | CSDL quan hệ (PostgreSQL) | saveAccount(account: Account): void | account: Account - tài khoản hành khách (Tạm) | void | PersistenceUnavailableException (Kỹ thuật tạm thời) | UC-009 đến UC-011 (chưa có P07; giữ chỗ theo P10 F2) | - | Tài khoản ghi bền | Đồng bộ | Có (khoá mã tài khoản) | 10 giây (Thiết kế: như truy vấn; giao dịch ngắn, không giữ qua lời gọi hệ thống ngoài) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-07.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

Chỉ saveTrip có trang hộp trắng vì có nhánh cập nhật có điều kiện. Các operation còn lại của IF-10 đến IF-13 ánh xạ 1-1: lớp DC-*RepositoryImpl nhận lời gọi, nhờ DC-OrmMapper ánh xạ và thực hiện một truy vấn hoặc một lần ghi qua CSDL, không rẽ nhánh nghiệp vụ.

#### Trang "Hộp đen - UC-002 kho dữ liệu"

UC hoặc operation: UC-002

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS07-BB1-L01 | Lifeline | :DC-BookTicketOnlineService | «control» | - | Control của UC-002 | 40 | 40 | 120 | 620 |
| SS07-BB1-L02 | Lifeline | :IF-10 ITripCatalogRepository | «interface» | - | Interface của SS-07 | 200 | 40 | 120 | 620 |
| SS07-BB1-L03 | Lifeline | :IF-11 ITicketingRepository | «interface» | - | Interface của SS-07 | 360 | 40 | 120 | 620 |
| SS07-BB1-FR1 | Fragment | alt [giữ chỗ thành công] | alt | - | Kết quả của saveTrip ở bước 9 | 30 | 240 | 460 | 350 |
| SS07-BB1-FR1-O2 | Fragment | [chỗ đã bị phiên khác giữ] | alt | SS07-BB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS07-BB1-FR1-SEP2 | 40 | 390 | 440 | 20 |
| SS07-BB1-FR1-O3 | Fragment | [kho dữ liệu không sẵn sàng] | alt | SS07-BB1-FR1 | Toán hạng 3, ngăn bởi đường nét đứt SS07-BB1-FR1-SEP3 | 40 | 500 | 440 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS07-BB1-M01 | 1 | SS07-BB1-L01 | SS07-BB1-L02 | findTrips(origin, destination, departureDate) | Đồng bộ | - | UC-002 bước 2 |
| SS07-BB1-M02 | 2 | SS07-BB1-L02 | SS07-BB1-L01 | List<Trip> | Trả về | - | UC-002 bước 2, luồng 2a khi rỗng |
| SS07-BB1-M03 | 3 | SS07-BB1-L01 | SS07-BB1-L02 | saveTrip(trip) | Đồng bộ | - | UC-002 bước 9 |
| SS07-BB1-M04 | 4 | SS07-BB1-L02 | SS07-BB1-L01 | void | Trả về | SS07-BB1-FR1 (toán hạng 1) | UC-002 bước 9 |
| SS07-BB1-M05 | 5 | SS07-BB1-L01 | SS07-BB1-L03 | saveBooking(booking) | Đồng bộ | SS07-BB1-FR1 (toán hạng 1) | UC-002 bước 9 |
| SS07-BB1-M06 | 6 | SS07-BB1-L03 | SS07-BB1-L01 | void | Trả về | SS07-BB1-FR1 (toán hạng 1) | UC-002 bước 9 |
| SS07-BB1-M07 | 7 | SS07-BB1-L02 | SS07-BB1-L01 | SeatAlreadyHeldException | Trả về | SS07-BB1-FR1 (toán hạng 2) | UC-002 bước 9 |
| SS07-BB1-M08 | 8 | SS07-BB1-L01 | SS07-BB1-L01 | chưa có luồng P04 (Q-106) | Tự gọi | SS07-BB1-FR1 (toán hạng 2) | Q-106 |
| SS07-BB1-M09 | 9 | SS07-BB1-L02 | SS07-BB1-L01 | PersistenceUnavailableException | Trả về | SS07-BB1-FR1 (toán hạng 3) | UC-002 bước 9 |
| SS07-BB1-M10 | 10 | SS07-BB1-L01 | SS07-BB1-L01 | chưa có luồng P04 (Q-104) | Tự gọi | SS07-BB1-FR1 (toán hạng 3) | Q-104 |

#### Trang "Hộp đen - UC-008 kho dữ liệu"

UC hoặc operation: UC-008

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS07-BB2-L01 | Lifeline | :DC-ReturnTicketService | «control» | - | Control của UC-008 | 40 | 40 | 120 | 510 |
| SS07-BB2-L02 | Lifeline | :IF-11 ITicketingRepository | «interface» | - | Interface của SS-07 | 200 | 40 | 120 | 510 |
| SS07-BB2-L03 | Lifeline | :IF-10 ITripCatalogRepository | «interface» | - | Interface của SS-07 | 360 | 40 | 120 | 510 |
| SS07-BB2-FR1 | Fragment | alt [ghi thành công] | alt | - | Kết quả ghi ở bước 10 | 30 | 200 | 460 | 280 |
| SS07-BB2-FR1-O2 | Fragment | [kho dữ liệu không sẵn sàng] | alt | SS07-BB2-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS07-BB2-FR1-SEP2 | 40 | 390 | 440 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS07-BB2-M01 | 1 | SS07-BB2-L01 | SS07-BB2-L02 | findTicket(ticketCode, travelerPhone) | Đồng bộ | - | UC-008 bước 2 |
| SS07-BB2-M02 | 2 | SS07-BB2-L02 | SS07-BB2-L01 | Ticket (null khi không khớp) | Trả về | - | UC-008 bước 2, luồng 2a |
| SS07-BB2-M03 | 3 | SS07-BB2-L01 | SS07-BB2-L03 | saveTrip(trip) | Đồng bộ | SS07-BB2-FR1 (toán hạng 1) | UC-008 bước 10 (trả chỗ) |
| SS07-BB2-M04 | 4 | SS07-BB2-L03 | SS07-BB2-L01 | void | Trả về | SS07-BB2-FR1 (toán hạng 1) | UC-008 bước 10 |
| SS07-BB2-M05 | 5 | SS07-BB2-L01 | SS07-BB2-L02 | saveTicket(ticket) | Đồng bộ | SS07-BB2-FR1 (toán hạng 1) | UC-008 bước 10 |
| SS07-BB2-M06 | 6 | SS07-BB2-L02 | SS07-BB2-L01 | void | Trả về | SS07-BB2-FR1 (toán hạng 1) | UC-008 bước 10 |
| SS07-BB2-M07 | 7 | SS07-BB2-L02 | SS07-BB2-L01 | PersistenceUnavailableException | Trả về | SS07-BB2-FR1 (toán hạng 2) | UC-008 bước 10 |
| SS07-BB2-M08 | 8 | SS07-BB2-L01 | SS07-BB2-L01 | chưa có luồng P04 (Q-104) | Tự gọi | SS07-BB2-FR1 (toán hạng 2) | Q-104 |

#### Trang "Hộp đen - UC-013 kho dữ liệu"

UC hoặc operation: UC-013

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS07-BB3-L01 | Lifeline | :DC-CancelTripService | «control» | - | Control của UC-013 | 40 | 40 | 120 | 720 |
| SS07-BB3-L02 | Lifeline | :IF-10 ITripCatalogRepository | «interface» | - | Interface của SS-07 | 200 | 40 | 120 | 720 |
| SS07-BB3-L03 | Lifeline | :IF-11 ITicketingRepository | «interface» | - | Interface của SS-07 | 360 | 40 | 120 | 720 |
| SS07-BB3-FR1 | Fragment | loop [với từng vé đã huỷ (bước 6 đến 9)] | loop | - | Ghi khoản hoàn từng vé | 40 | 470 | 440 | 90 |
| SS07-BB3-FR2 | Fragment | alt [ghi thành công] | alt | - | Kết quả ghi | 30 | 360 | 460 | 330 |
| SS07-BB3-FR2-O2 | Fragment | [kho dữ liệu không sẵn sàng] | alt | SS07-BB3-FR2 | Toán hạng 2, ngăn bởi đường nét đứt SS07-BB3-FR2-SEP2 | 40 | 600 | 440 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS07-BB3-M01 | 1 | SS07-BB3-L01 | SS07-BB3-L02 | findTrip(route, departureDateTime) | Đồng bộ | - | UC-013 bước 2 |
| SS07-BB3-M02 | 2 | SS07-BB3-L02 | SS07-BB3-L01 | Trip | Trả về | - | UC-013 bước 2, luồng 2a |
| SS07-BB3-M03 | 3 | SS07-BB3-L01 | SS07-BB3-L03 | findTicketsOfTrip(tripId) | Đồng bộ | - | UC-013 bước 3 |
| SS07-BB3-M04 | 4 | SS07-BB3-L03 | SS07-BB3-L01 | List<Ticket> | Trả về | - | UC-013 bước 3 |
| SS07-BB3-M05 | 5 | SS07-BB3-L01 | SS07-BB3-L03 | findPhoneReservationsOfTrip(tripId) | Đồng bộ | - | UC-013 bước 3 |
| SS07-BB3-M06 | 6 | SS07-BB3-L03 | SS07-BB3-L01 | List<PhoneReservation> | Trả về | - | UC-013 bước 3 |
| SS07-BB3-M07 | 7 | SS07-BB3-L01 | SS07-BB3-L03 | saveTripCancellation(cancellation) | Đồng bộ | SS07-BB3-FR2 (toán hạng 1) | UC-013 bước 5 |
| SS07-BB3-M08 | 8 | SS07-BB3-L03 | SS07-BB3-L01 | void | Trả về | SS07-BB3-FR2 (toán hạng 1) | UC-013 bước 5 |
| SS07-BB3-M09 | 9 | SS07-BB3-L01 | SS07-BB3-L03 | saveTicket(ticket) | Đồng bộ | SS07-BB3-FR2 (toán hạng 1) | UC-013 bước 9 |
| SS07-BB3-M10 | 10 | SS07-BB3-L03 | SS07-BB3-L01 | void | Trả về | SS07-BB3-FR2 (toán hạng 1) | UC-013 bước 9 |
| SS07-BB3-M11 | 11 | SS07-BB3-L03 | SS07-BB3-L01 | PersistenceUnavailableException | Trả về | SS07-BB3-FR2 (toán hạng 2) | UC-013 bước 5 hoặc 9 |
| SS07-BB3-M12 | 12 | SS07-BB3-L01 | SS07-BB3-L01 | chưa có luồng P04 (Q-104) | Tự gọi | SS07-BB3-FR2 (toán hạng 2) | Q-104 |

#### Trang "Hộp đen - UC-015 kho dữ liệu máy chủ"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS07-BB4-L01 | Lifeline | :DC-CheckBoardingTicketService | «control» | - | Control của UC-015 chạy ở back-end khi nhận kết quả | 40 | 40 | 120 | 350 |
| SS07-BB4-L02 | Lifeline | :IF-12 IBoardingRepository | «interface» | - | Interface của SS-07 | 200 | 40 | 120 | 350 |
| SS07-BB4-FR1 | Fragment | alt [ghi thành công] | alt | - | Kết quả của saveCheckSession | 30 | 160 | 300 | 160 |
| SS07-BB4-FR1-O2 | Fragment | [kho dữ liệu không sẵn sàng] | alt | SS07-BB4-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS07-BB4-FR1-SEP2 | 40 | 230 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS07-BB4-M01 | 1 | SS07-BB4-L01 | SS07-BB4-L02 | saveCheckSession(session) | Đồng bộ | - | UC-015 bước 10 |
| SS07-BB4-M02 | 2 | SS07-BB4-L02 | SS07-BB4-L01 | void | Trả về | SS07-BB4-FR1 (toán hạng 1) | UC-015 bước 10 |
| SS07-BB4-M03 | 3 | SS07-BB4-L02 | SS07-BB4-L01 | PersistenceUnavailableException | Trả về | SS07-BB4-FR1 (toán hạng 2) | UC-015 bước 10 |
| SS07-BB4-M04 | 4 | SS07-BB4-L01 | SS07-BB4-L01 | chưa có luồng P04 (Q-104) | Tự gọi | SS07-BB4-FR1 (toán hạng 2) | Q-104 |

#### Trang "Hộp trắng - saveTrip"

UC hoặc operation: UC-002, UC-008

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS07-WB1-FRM | Fragment | sd saveTrip | - | - | Khung sơ đồ của operation | 20 | 20 | 580 | 640 |
| SS07-WB1-L01 | Lifeline | :DC-TripCatalogRepositoryImpl | «control» | - | Lớp điều phối, hiện thực IF-10 | 120 | 40 | 120 | 580 |
| SS07-WB1-L02 | Lifeline | :DC-OrmMapper | «converter» | - | Lớp chuyển đổi đối tượng sang quan hệ | 280 | 40 | 120 | 580 |
| SS07-WB1-L03 | Actor | CSDL quan hệ | «database» | - | PostgreSQL | 440 | 40 | 120 | 580 |
| SS07-WB1-G1 | Gate | saveTrip | - | SS07-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS07-WB1-G1-2 | Gate | saveTrip | - | SS07-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 340 | 20 | 20 |
| SS07-WB1-G1-3 | Gate | saveTrip | - | SS07-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 410 | 20 | 20 |
| SS07-WB1-G1-4 | Gate | saveTrip | - | SS07-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 520 | 20 | 20 |
| SS07-WB1-FR1 | Fragment | alt [số dòng cập nhật khớp số chỗ đổi] | alt | - | Kết quả cập nhật có điều kiện | 110 | 280 | 460 | 270 |
| SS07-WB1-FR1-O2 | Fragment | [số dòng không khớp] | alt | SS07-WB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS07-WB1-FR1-SEP2 | 120 | 390 | 440 | 20 |
| SS07-WB1-FR1-O3 | Fragment | [lỗi kết nối hoặc quá thời gian] | alt | SS07-WB1-FR1 | Toán hạng 3, ngăn bởi đường nét đứt SS07-WB1-FR1-SEP3 | 120 | 460 | 440 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS07-WB1-M01 | 1 | SS07-WB1-G1 | SS07-WB1-L01 | saveTrip(trip) | Đồng bộ | - | UC-002 bước 9 / UC-008 bước 10 |
| SS07-WB1-M02 | 2 | SS07-WB1-L01 | SS07-WB1-L02 | toTripRows(trip) | Đồng bộ | - | - |
| SS07-WB1-M03 | 3 | SS07-WB1-L02 | SS07-WB1-L01 | dòng chuyến và dòng chỗ đã đổi | Trả về | - | - |
| SS07-WB1-M04 | 4 | SS07-WB1-L01 | SS07-WB1-L03 | cập nhật có điều kiện từng chỗ và phiên bản chuyến | Đồng bộ | - | Chống trùng chỗ (REQ-67) |
| SS07-WB1-M05 | 5 | SS07-WB1-L03 | SS07-WB1-L01 | số dòng đã cập nhật | Trả về | SS07-WB1-FR1 (toán hạng 1) | - |
| SS07-WB1-M06 | 6 | SS07-WB1-L01 | SS07-WB1-G1-2 | void | Trả về | SS07-WB1-FR1 (toán hạng 1) | - |
| SS07-WB1-M07 | 7 | SS07-WB1-L01 | SS07-WB1-G1-3 | SeatAlreadyHeldException | Trả về | SS07-WB1-FR1 (toán hạng 2) | Số dòng không khớp: chỗ đã bị phiên khác đổi |
| SS07-WB1-M08 | 8 | SS07-WB1-L03 | SS07-WB1-L01 | lỗi kết nối hoặc hết thời gian câu lệnh | Trả về | SS07-WB1-FR1 (toán hạng 3) | - |
| SS07-WB1-M09 | 9 | SS07-WB1-L01 | SS07-WB1-G1-4 | PersistenceUnavailableException | Trả về | SS07-WB1-FR1 (toán hạng 3) | Cô lập lỗi của kho dữ liệu |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-TripCatalogRepositoryImpl | TripCatalogRepositoryImpl | Điều phối | Hiện thực IF-10, mở và đóng giao dịch ngắn, cập nhật có điều kiện chống trùng chỗ | package-private | IF-10 |
| DC-TicketingRepositoryImpl | TicketingRepositoryImpl | Điều phối | Hiện thực IF-11; ghi lần đặt, vé, khoản hoàn trong giao dịch | package-private | IF-11 |
| DC-BoardingRepositoryImpl | BoardingRepositoryImpl | Điều phối | Hiện thực IF-12 ở máy chủ | package-private | IF-12 |
| DC-AccountRepositoryImpl | AccountRepositoryImpl | Điều phối | Hiện thực IF-13 (giữ chỗ, chờ P07 của UC-009 đến UC-011) | package-private | IF-13 |
| DC-OrmMapper | OrmMapper | Chuyển đổi dữ liệu | Ánh xạ đối tượng miền sang dòng quan hệ và ngược lại (Spring Data JPA, Thiết kế: theo CONG_NGHE của hồ sơ); quản lý kết nối qua pool | package-private | - |
| DC-SeatAlreadyHeldException | SeatAlreadyHeldException | Ngoại lệ | Chỗ đã bị phiên khác giữ hoặc bán (Nghiệp vụ). Đặt ở PKG-22, cạnh IF-10 | public (thuộc chữ ký IF-10; Đề xuất sửa P10) | - |
| DC-PersistenceUnavailableException | PersistenceUnavailableException | Ngoại lệ | Kho dữ liệu không sẵn sàng (Kỹ thuật tạm thời). Đặt ở PKG-28 vì dùng chung bốn interface ở bốn package | public (thuộc chữ ký IF-10 đến IF-13; Đề xuất sửa P10) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-07 | Subsystem | SS-07 ServerPersistence | «subsystem» | - | - | 40 | 310 | 960 | 280 |
| IF-10 | Interface | IF-10 ITripCatalogRepository | «interface» | PKG-22 | - | 60 | 40 | 200 | 130 |
| IF-11 | Interface | IF-11 ITicketingRepository | «interface» | PKG-23 | - | 300 | 40 | 200 | 190 |
| IF-12 | Interface | IF-12 IBoardingRepository | «interface» | PKG-24 | - | 540 | 40 | 200 | 150 |
| IF-13 | Interface | IF-13 IAccountRepository | «interface» | PKG-25 | - | 780 | 40 | 200 | 90 |
| DC-TripCatalogRepositoryImpl | Class | DC-TripCatalogRepositoryImpl | «control» | SS-07 | - | 60 | 350 | 200 | 70 |
| DC-TicketingRepositoryImpl | Class | DC-TicketingRepositoryImpl | «control» | SS-07 | - | 300 | 350 | 200 | 70 |
| DC-BoardingRepositoryImpl | Class | DC-BoardingRepositoryImpl | «control» | SS-07 | - | 540 | 350 | 200 | 70 |
| DC-AccountRepositoryImpl | Class | DC-AccountRepositoryImpl | «control» | SS-07 | - | 780 | 350 | 200 | 70 |
| DC-OrmMapper | Class | DC-OrmMapper | «converter» | SS-07 | - | 780 | 500 | 200 | 70 |
| ACT-DB | Actor | CSDL quan hệ (PostgreSQL) | - | - | - | 1040 | 500 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS07-EL-E01 | DC-TripCatalogRepositoryImpl | IF-10 | Realization | - | Subsystem hiện thực IF-10 qua lớp điều phối | - |
| SS07-EL-E02 | DC-TicketingRepositoryImpl | IF-11 | Realization | - | Subsystem hiện thực IF-11 qua lớp điều phối | - |
| SS07-EL-E03 | DC-BoardingRepositoryImpl | IF-12 | Realization | - | Subsystem hiện thực IF-12 qua lớp điều phối | - |
| SS07-EL-E04 | DC-AccountRepositoryImpl | IF-13 | Realization | - | Subsystem hiện thực IF-13 qua lớp điều phối | - |
| SS07-EL-E05 | DC-TripCatalogRepositoryImpl | DC-OrmMapper | Association (điều hướng) | dùng | - | (160,440); (850,440) |
| SS07-EL-E06 | DC-TicketingRepositoryImpl | DC-OrmMapper | Association (điều hướng) | dùng | - | (400,450); (870,450) |
| SS07-EL-E07 | DC-BoardingRepositoryImpl | DC-OrmMapper | Association (điều hướng) | dùng | - | (640,460); (890,460) |
| SS07-EL-E08 | DC-AccountRepositoryImpl | DC-OrmMapper | Association (điều hướng) | dùng | - | (880,470); (910,470) |
| SS07-EL-E09 | DC-OrmMapper | ACT-DB | Association | truy vấn | - | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-07 | PKG-22, PKG-23, PKG-24, PKG-25 | Vào package | Hiện thực IF-10 đến IF-13 do các package này định nghĩa và ánh xạ mọi lớp miền (P10 F4: PKG-14 --> PKG-22, PKG-23, PKG-24, PKG-25); Domain ở layer thấp nhất nên không đi lên | Dùng thận trọng |
| SS-07 | PKG-28 | Vào package | DC-PersistenceUnavailableException dùng chung bốn interface (Đề xuất sửa P10: thêm phụ thuộc PKG-14 --> PKG-28) | Dùng thận trọng |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-09 | Package | PKG-09 TicketSalesService | - | - | - | 300 | 40 | 200 | 60 |
| PKG-10 | Package | PKG-10 TripOperationsService | - | - | - | 540 | 40 | 200 | 60 |
| PKG-11 | Package | PKG-11 BoardingCheckService | - | - | - | 780 | 40 | 200 | 60 |
| IF-10 | Interface | IF-10 ITripCatalogRepository | «interface» | - | - | 180 | 170 | 200 | 50 |
| IF-11 | Interface | IF-11 ITicketingRepository | «interface» | - | - | 420 | 170 | 200 | 50 |
| IF-12 | Interface | IF-12 IBoardingRepository | «interface» | - | - | 660 | 170 | 200 | 50 |
| IF-13 | Interface | IF-13 IAccountRepository | «interface» | - | - | 900 | 170 | 200 | 50 |
| SS-07 | Subsystem | SS-07 ServerPersistence | - | - | - | 540 | 300 | 200 | 60 |
| PKG-22 | Package | PKG-22 TripCatalog | - | - | - | 60 | 450 | 200 | 60 |
| PKG-23 | Package | PKG-23 Ticketing | - | - | - | 300 | 450 | 200 | 60 |
| PKG-24 | Package | PKG-24 BoardingModel | - | - | - | 540 | 450 | 200 | 60 |
| PKG-25 | Package | PKG-25 AccountModel | - | - | - | 780 | 450 | 200 | 60 |
| PKG-28 | Package | PKG-28 SharedValueTypes | - | - | - | 1020 | 450 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS07-DP-E01 | SS-07 | PKG-22 | Dependency | lớp miền | - | (600,380); (160,380) |
| SS07-DP-E02 | SS-07 | PKG-23 | Dependency | lớp miền | - | (620,390); (400,390) |
| SS07-DP-E03 | SS-07 | PKG-24 | Dependency | lớp miền | - | - |
| SS07-DP-E04 | SS-07 | PKG-25 | Dependency | lớp miền | - | (660,410); (880,410) |
| SS07-DP-E05 | SS-07 | PKG-28 | Dependency | ngoại lệ dùng chung | - | (680,420); (1120,420) |
| SS07-DP-E06 | PKG-09 | IF-10 | Dependency | dùng | - | (400,120); (280,120) |
| SS07-DP-E07 | PKG-10 | IF-11 | Dependency | dùng | - | (640,130); (520,130) |
| SS07-DP-E08 | PKG-11 | IF-12 | Dependency | dùng | - | (880,140); (760,140) |
| SS07-DP-E09 | SS-07 | IF-10 | Realization | - | - | (610,240); (280,240) |
| SS07-DP-E10 | SS-07 | IF-11 | Realization | - | - | (630,250); (520,250) |
| SS07-DP-E11 | SS-07 | IF-12 | Realization | - | - | (650,260); (760,260) |
| SS07-DP-E12 | SS-07 | IF-13 | Realization | - | - | (670,270); (1000,270) |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| saveTrip | Hai phiên cùng giữ một chỗ | Nghiệp vụ | Số dòng cập nhật có điều kiện không khớp | Giao dịch bị huỷ, không thử lại | SeatAlreadyHeldException | UC-002 6b (chỗ không còn trống) gần nghĩa nhưng xảy ra ở bước 9 | Q-106; Đề xuất sửa P04 |
| Mọi operation của IF-10 đến IF-13 | Mất kết nối CSDL hoặc quá 10 giây | Kỹ thuật tạm thời | Lỗi kết nối hoặc hết thời gian câu lệnh | Giao dịch huỷ; không tự thử lại ghi (caller quyết định); đọc không tự thử lại | PersistenceUnavailableException | Không có (P04 chưa có luồng lỗi hệ thống) | Q-104 |
| saveTicket, saveBooking, saveTripCancellation | Ghi lặp cùng khoá | Kỹ thuật | Khoá mã vé, mã lần đặt, mã chuyến | Ghi lại cùng nội dung không tạo bản ghi mới (idempotent) | Không có | - | - |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-10 đến IF-13 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: không dùng interface nào |
| Không phần tử bên trong subsystem nào public | Đạt |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt: saveTrip có trang, còn lại 1-1 |

## SS-08 DeviceLocalPersistence

Package chứa: PKG-20. Tác nhân hoặc đối tượng ngoài: CSDL cục bộ.

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-015 Soát vé lên xe | AC-C-CheckBoardingTicketController (DC-CheckBoardingTicketService) | SD1: 1.1.2 // startSession; 1.1.4 // summarizeTicketCounts; 2.1.1 // findTicket (TripPassengerList); 2.1.3 // markChecked; 3.1.1.2 // keepResultPending - phần lưu cục bộ | danh sách hành khách, phiên soát vé, vé đã soát, trạng thái gửi | 10a (kết quả chờ gửi khi mất sóng). Lỗi ghi dữ liệu cục bộ: chưa có luồng (Q-107) |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Subsystem hiện thực | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-12 | IBoardingRepository | Lưu và truy xuất danh sách hành khách, phiên soát vé trên máy soát vé (cùng interface với SS-07, hiện thực khác) | SS-07, SS-08 | DC-CheckBoardingTicketService (PKG-11) | PKG-24 |

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-12 | IBoardingRepository | CSDL cục bộ (SQLite, Room) | findPassengerList(tripId: String): TripPassengerList | tripId: String - mã chuyến | TripPassengerList: danh sách vé của chuyến trên máy, null khi chưa có (ASM-32) | LocalStoreException (Kỹ thuật tạm thời, ví dụ đầy bộ nhớ hoặc tệp hỏng) | UC-015 (bước 2: mở phiên; bước 5: kiểm tra vé theo danh sách trên máy, NFR-02) | - | Không thay đổi dữ liệu | Đồng bộ (luồng nền) | Có (chỉ đọc) | - (Thiết kế: truy cập SQLite cục bộ không qua mạng, chạy trên luồng nền của ViewModel vì Android cấm truy cập CSDL trên luồng giao diện) |
| IF-12 | IBoardingRepository | CSDL cục bộ (SQLite, Room) | savePassengerList(list: TripPassengerList): void | list: TripPassengerList - danh sách nhận từ máy chủ qua IF-09 | void | LocalStoreException (Kỹ thuật tạm thời, ví dụ đầy bộ nhớ hoặc tệp hỏng) | UC-015 (tiền điều kiện: danh sách có trên máy); UC-014 (chưa có P07) | Danh sách đã lấy qua IF-09.fetchPassengerList | Danh sách ghi bền cục bộ | Đồng bộ (luồng nền) | Có (khoá mã chuyến) | - (Thiết kế: truy cập SQLite cục bộ không qua mạng, chạy trên luồng nền của ViewModel vì Android cấm truy cập CSDL trên luồng giao diện) |
| IF-12 | IBoardingRepository | CSDL cục bộ (SQLite, Room) | findCheckSession(tripId: String): TicketCheckSession | tripId: String - mã chuyến | TicketCheckSession: phiên soát vé của chuyến, null khi chưa có | LocalStoreException (Kỹ thuật tạm thời, ví dụ đầy bộ nhớ hoặc tệp hỏng) | UC-015 (bước 2, 11; mở lại phiên sau khi ứng dụng khởi động lại) | - | Không thay đổi dữ liệu | Đồng bộ (luồng nền) | Có (chỉ đọc) | - (Thiết kế: truy cập SQLite cục bộ không qua mạng, chạy trên luồng nền của ViewModel vì Android cấm truy cập CSDL trên luồng giao diện) |
| IF-12 | IBoardingRepository | CSDL cục bộ (SQLite, Room) | saveCheckSession(session: TicketCheckSession): void | session: TicketCheckSession - phiên cùng các vé đã soát và trạng thái gửi kết quả | void | LocalStoreException (Kỹ thuật tạm thời, ví dụ đầy bộ nhớ hoặc tệp hỏng) | UC-015 (bước 6: ghi nhận vé đã soát; bước 10, luồng 10a: lưu kết quả chưa gửi) | - | Phiên và trạng thái gửi ghi bền, còn sau khi khởi động lại; ghi trong một giao dịch Room | Đồng bộ (luồng nền) | Có (khoá mã chuyến) | - (Thiết kế: truy cập SQLite cục bộ không qua mạng, chạy trên luồng nền của ViewModel vì Android cấm truy cập CSDL trên luồng giao diện) |
| IF-12 | IBoardingRepository | CSDL cục bộ (SQLite, Room) | findPendingCheckSessions(): List<TicketCheckSession> | - | List<TicketCheckSession>: các phiên có kết quả chưa gửi | LocalStoreException (Kỹ thuật tạm thời, ví dụ đầy bộ nhớ hoặc tệp hỏng) | UC-015 (luồng 10a; operation kỹ thuật để khôi phục trạng thái Chờ gửi sau khi ứng dụng khởi động lại) | - | Không thay đổi dữ liệu | Đồng bộ (luồng nền) | Có (chỉ đọc) | - (Thiết kế: truy cập SQLite cục bộ không qua mạng, chạy trên luồng nền của ViewModel vì Android cấm truy cập CSDL trên luồng giao diện) |

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-08.drawio. Các trang "Hộp đen" và "Hộp trắng" cho sequence diagram; trang "Phần tử" và "Phụ thuộc" thuộc F5 và F6.

Chỉ saveCheckSession có trang hộp trắng. Các operation còn lại của IF-12 ánh xạ 1-1: DC-BoardingLocalRepositoryImpl nhờ DC-RoomEntityMapper và DC-BoardingDao đọc hoặc ghi một lần.

#### Trang "Hộp đen - UC-015 kho dữ liệu máy soát vé"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS08-BB1-L01 | Lifeline | :DC-CheckBoardingTicketService | «control» | - | Control của UC-015 trên máy soát vé | 40 | 40 | 120 | 430 |
| SS08-BB1-L02 | Lifeline | :IF-12 IBoardingRepository | «interface» | - | Interface của SS-08 | 200 | 40 | 120 | 430 |
| SS08-BB1-FR1 | Fragment | alt [ghi thành công] | alt | - | Kết quả của saveCheckSession | 30 | 240 | 300 | 160 |
| SS08-BB1-FR1-O2 | Fragment | [LocalStoreException] | alt | SS08-BB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS08-BB1-FR1-SEP2 | 40 | 310 | 280 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS08-BB1-M01 | 1 | SS08-BB1-L01 | SS08-BB1-L02 | findPassengerList(tripId) | Đồng bộ | - | UC-015 bước 2 |
| SS08-BB1-M02 | 2 | SS08-BB1-L02 | SS08-BB1-L01 | TripPassengerList | Trả về | - | UC-015 bước 2 |
| SS08-BB1-M03 | 3 | SS08-BB1-L01 | SS08-BB1-L02 | saveCheckSession(session) | Đồng bộ | - | UC-015 bước 6, 10, 10a |
| SS08-BB1-M04 | 4 | SS08-BB1-L02 | SS08-BB1-L01 | void | Trả về | SS08-BB1-FR1 (toán hạng 1) | UC-015 bước 6 |
| SS08-BB1-M05 | 5 | SS08-BB1-L02 | SS08-BB1-L01 | LocalStoreException | Trả về | SS08-BB1-FR1 (toán hạng 2) | UC-015 bước 6 |
| SS08-BB1-M06 | 6 | SS08-BB1-L01 | SS08-BB1-L01 | chưa có luồng P04 (Q-107) | Tự gọi | SS08-BB1-FR1 (toán hạng 2) | Q-107 |

#### Trang "Hộp trắng - saveCheckSession"

UC hoặc operation: UC-015

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS08-WB1-FRM | Fragment | sd saveCheckSession | - | - | Khung sơ đồ của operation | 20 | 20 | 740 | 690 |
| SS08-WB1-L01 | Lifeline | :DC-BoardingLocalRepositoryImpl | «control» | - | Lớp điều phối, hiện thực IF-12 | 120 | 40 | 120 | 630 |
| SS08-WB1-L02 | Lifeline | :DC-RoomEntityMapper | «converter» | - | Lớp chuyển đổi dữ liệu | 280 | 40 | 120 | 630 |
| SS08-WB1-L03 | Lifeline | :DC-BoardingDao | «adapter» | - | Lớp truy cập Room | 440 | 40 | 120 | 630 |
| SS08-WB1-L04 | Actor | CSDL cục bộ | «database» | - | SQLite | 600 | 40 | 120 | 630 |
| SS08-WB1-G1 | Gate | saveCheckSession | - | SS08-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 110 | 20 | 20 |
| SS08-WB1-G1-2 | Gate | saveCheckSession | - | SS08-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 420 | 20 | 20 |
| SS08-WB1-G1-3 | Gate | saveCheckSession | - | SS08-WB1-FRM | Gate trên khung sd, tên gate là tên message đi qua | 10 | 570 | 20 | 20 |
| SS08-WB1-FR1 | Fragment | alt [ghi thành công] | alt | - | Kết quả ghi | 110 | 320 | 620 | 280 |
| SS08-WB1-FR1-O2 | Fragment | [lỗi ghi] | alt | SS08-WB1-FR1 | Toán hạng 2, ngăn bởi đường nét đứt SS08-WB1-FR1-SEP2 | 120 | 470 | 600 | 20 |

| ID | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS08-WB1-M01 | 1 | SS08-WB1-G1 | SS08-WB1-L01 | saveCheckSession(session) | Đồng bộ | - | UC-015 bước 6, 10 |
| SS08-WB1-M02 | 2 | SS08-WB1-L01 | SS08-WB1-L02 | toSessionEntity(session) | Đồng bộ | - | - |
| SS08-WB1-M03 | 3 | SS08-WB1-L02 | SS08-WB1-L01 | SessionEntity và CheckedTicketEntity | Trả về | - | - |
| SS08-WB1-M04 | 4 | SS08-WB1-L01 | SS08-WB1-L03 | upsertSessionInTransaction(entities) | Đồng bộ | - | Một giao dịch Room |
| SS08-WB1-M05 | 5 | SS08-WB1-L03 | SS08-WB1-L04 | ghi phiên và vé đã soát | Đồng bộ | - | - |
| SS08-WB1-M06 | 6 | SS08-WB1-L04 | SS08-WB1-L03 | đã ghi | Trả về | SS08-WB1-FR1 (toán hạng 1) | - |
| SS08-WB1-M07 | 7 | SS08-WB1-L03 | SS08-WB1-L01 | Ok | Trả về | SS08-WB1-FR1 (toán hạng 1) | - |
| SS08-WB1-M08 | 8 | SS08-WB1-L01 | SS08-WB1-G1-2 | void | Trả về | SS08-WB1-FR1 (toán hạng 1) | - |
| SS08-WB1-M09 | 9 | SS08-WB1-L04 | SS08-WB1-L03 | lỗi ghi | Trả về | SS08-WB1-FR1 (toán hạng 2) | - |
| SS08-WB1-M10 | 10 | SS08-WB1-L03 | SS08-WB1-L01 | StoreError | Trả về | SS08-WB1-FR1 (toán hạng 2) | - |
| SS08-WB1-M11 | 11 | SS08-WB1-L01 | SS08-WB1-G1-3 | LocalStoreException | Trả về | SS08-WB1-FR1 (toán hạng 2) | Cô lập lỗi của Room |

### F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-BoardingLocalRepositoryImpl | BoardingLocalRepositoryImpl | Điều phối | Hiện thực IF-12 trên máy soát vé, mở giao dịch Room cho mỗi ghi | package-private | IF-12 |
| DC-BoardingDao | BoardingDao | Giao tiếp ngoài | Truy cập Room (DAO) tới SQLite cục bộ | package-private | - |
| DC-RoomEntityMapper | RoomEntityMapper | Chuyển đổi dữ liệu | Ánh xạ TripPassengerList, TicketCheckSession sang bảng Room và ngược lại | package-private | - |
| DC-LocalStoreException | LocalStoreException | Ngoại lệ | Lỗi lưu cục bộ đã che lỗi của Room. Đặt ở PKG-28 cạnh DC-PersistenceUnavailableException | public (thuộc chữ ký IF-12; Đề xuất sửa P10) | - |

b) Class diagram phần tử (trang "Phần tử")

#### Trang "Phần tử"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-08 | Subsystem | SS-08 DeviceLocalPersistence | «subsystem» | - | - | 40 | 240 | 480 | 260 |
| IF-12 | Interface | IF-12 IBoardingRepository | «interface» | PKG-24 | - | 300 | 40 | 200 | 150 |
| DC-BoardingLocalRepositoryImpl | Class | DC-BoardingLocalRepositoryImpl | «control» | SS-08 | - | 300 | 280 | 200 | 70 |
| DC-RoomEntityMapper | Class | DC-RoomEntityMapper | «converter» | SS-08 | - | 60 | 410 | 200 | 70 |
| DC-BoardingDao | Class | DC-BoardingDao | «adapter» | SS-08 | - | 300 | 410 | 200 | 70 |
| ACT-SQLITE | Actor | CSDL cục bộ (SQLite) | - | - | - | 560 | 410 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS08-EL-E01 | DC-BoardingLocalRepositoryImpl | IF-12 | Realization | - | Subsystem hiện thực IF-12 qua lớp điều phối | - |
| SS08-EL-E02 | DC-BoardingLocalRepositoryImpl | DC-RoomEntityMapper | Association (điều hướng) | dùng | - | (390,370); (160,370) |
| SS08-EL-E03 | DC-BoardingLocalRepositoryImpl | DC-BoardingDao | Association (điều hướng) | dùng | - | (410,380); (400,380) |
| SS08-EL-E04 | DC-BoardingDao | ACT-SQLITE | Association | Room | - | - |

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-08 | PKG-24 | Vào package | Hiện thực IF-12 và ánh xạ TripPassengerList, TicketCheckSession (P10 F4: PKG-20 --> PKG-24); Domain ở layer thấp nhất | Dùng thận trọng |

#### Trang "Phụ thuộc"

| ID | Loại (Class / Interface / Subsystem / Package / Actor) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-11 | Package | PKG-11 BoardingCheckService | - | - | - | 60 | 40 | 200 | 60 |
| IF-12 | Interface | IF-12 IBoardingRepository | «interface» | - | - | 60 | 150 | 200 | 50 |
| SS-08 | Subsystem | SS-08 DeviceLocalPersistence | - | - | - | 60 | 250 | 200 | 60 |
| PKG-24 | Package | PKG-24 BoardingModel | - | - | - | 60 | 360 | 200 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS08-DP-E01 | PKG-11 | IF-12 | Dependency | dùng | - | - |
| SS08-DP-E02 | SS-08 | IF-12 | Realization | - | - | - |
| SS08-DP-E03 | SS-08 | PKG-24 | Dependency | TripPassengerList, TicketCheckSession | - | - |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| Mọi operation của IF-12 (SS-08) | Đầy bộ nhớ hoặc tệp CSDL hỏng | Kỹ thuật tạm thời | Ngoại lệ của Room | Giao dịch huỷ, không tự thử lại | LocalStoreException | Không có (UC-015 chưa có luồng lỗi lưu cục bộ) | Q-107 |
| saveCheckSession | Ứng dụng bị đóng giữa lúc ghi | Kỹ thuật | Giao dịch Room không hoàn tất | Giao dịch được huỷ nguyên vẹn; lần quét cuối có thể mất và phụ xe quét lại (vé lúc đó chưa hiện là đã soát) | Không có | Không có | Q-107 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả |
|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt: IF-12 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt: không dùng interface nào |
| Không phần tử bên trong subsystem nào public | Đạt |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt: saveCheckSession có trang, còn lại 1-1 |

## F8. Tổng hợp toàn hệ thống

| SS | IF | Số operation | UC dùng | Rủi ro chính |
|---|---|---|---|---|
| SS-01 OnlinePayment | IF-01, IF-02 | 5 | UC-008, UC-013, UC-003 | Cổng chưa có tài liệu API (Q-24, Q-100); kết quả không rõ chưa có luồng P04 (Q-55); thanh toán là Tạm (ASM-100); tiền tệ: không thử lại tự động |
| SS-02 SmsDelivery | IF-03 | 1 | UC-002, UC-013 | Lỗi gửi chưa có luồng P04 (Q-56); gửi đồng bộ trong vòng lặp từng vé nên một chuyến huỷ có nhiều vé kéo dài luồng; trùng tin khi cổng chưa hỗ trợ khoá (Q-101) |
| SS-03 BarcodeReading | IF-04, IF-05 | 4 | UC-015 | Model máy và loại mã vạch chưa biết (Q-54); lỗi đọc chưa có luồng P04 (Q-103); đầu quét giả lập bàn phím có thể lẫn với nhập tay |
| SS-04 TicketPrinting | IF-06 | 1 | UC-005 | Model máy in và cách kết nối chưa biết (Q-57, Q-79); P04 UC-005 chưa có nên lỗi in chưa có luồng (Q-102); in trùng vé giấy khi hết thời gian chờ |
| SS-05 TriggerScheduling | IF-07, IF-08 | 3 | UC-002, UC-013 | Sai số mốc chưa quy định (Q-82); lỗi ghi mốc chưa có luồng (Q-104); P10 F2 ghi subsystem duyệt dữ liệu miền nhưng PKG-19 không phụ thuộc package nào, nên SS-05 giữ kho mốc riêng |
| SS-06 ServerApiAccess | IF-09, IF-14 | 3 | UC-015 | Cách lấy danh sách lúc mất sóng (Q-81); máy chủ cần xử lý idempotent theo tripId (DC-BoardingSyncRestController, P12); IF-14 là interface mới cần ghi vào P10 |
| SS-07 ServerPersistence | IF-10, IF-11, IF-12, IF-13 | 18 | UC-002, UC-008, UC-013, UC-015 (IF-13: chưa có) | Hai phiên cùng giữ chỗ chưa có luồng P04 (Q-106); lỗi hệ thống nội bộ chưa có luồng (Q-104); IF-13 chưa có UC dùng; ranh giới giao dịch: không giữ qua lời gọi hệ thống ngoài |
| SS-08 DeviceLocalPersistence | IF-12 | 5 | UC-015 | Lỗi lưu cục bộ chưa có luồng P04 (Q-107); mất lần quét cuối khi ứng dụng bị đóng giữa giao dịch; danh sách là bản sao (Q-73) |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-100 | Cổng thanh toán của đối tác có hỗ trợ khoá idempotency cho yêu cầu thanh toán và hoàn tiền, có API tra cứu trạng thái giao dịch và hoàn tiền, và gửi thông báo kết quả có chữ ký kiểm tra được không? (Có đủ ba khả năng / Thiếu một hoặc hai / Không có) | IF-01 requestPayment, requestRefund, queryRefundStatus, queryPaymentStatus; IF-02; chính sách không rõ kết quả (F7a của SS-01) | project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API"; liên quan Q-24, Q-55 |
| Q-101 | Cổng SMS của nhà mạng có hỗ trợ khoá chống gửi trùng (cùng messageKey chỉ gửi một tin) và báo cáo trạng thái chuyển tin tới thuê bao không? (Có / Không) | IF-03 sendSms (Idempotent, thử lại); SS-02 | NFR-08: API REST, không nêu khoá chống trùng; liên quan Q-56 |
| Q-102 | Khi máy in vé báo lỗi (hết giấy, mất kết nối, in hỏng) lúc bán vé tại quầy, nhân viên bán vé xử lý thế nào: in lại vé đã phát hành, huỷ vé và bán lại, hay cách khác? (In lại / Huỷ và bán lại / Khác) | IF-06 printTicket (PrintResult Failed, PrinterUnavailableException); UC-005; P04 UC-005 | NFR-09, REQ-24: nêu in vé nhưng không nêu lỗi in; P04 UC-005 chưa có |
| Q-103 | Khi đầu quét không đọc được mã vạch, đọc ra chuỗi không phải mã vé hoặc mất kết nối giữa phiên soát, máy soát vé báo gì cho phụ xe và có tính là vé không hợp lệ không? (Báo lỗi đọc, quét lại / Tính là vé không hợp lệ lý do khác / Chuyển sang nhập tay mã vé) | IF-05 receiveScanError; SS-03; UC-015 (luồng 3a, 5a) | P04 UC-015 chỉ có luồng 3a, 5a, 5b, 5c; NFR-10; liên quan Q-54 |
| Q-104 | Khi hệ thống không ghi được dữ liệu hoặc không đặt được mốc thời gian vì lỗi kỹ thuật nội bộ giữa các bước của một use case (kho dữ liệu, kho mốc không sẵn sàng), use case kết thúc thế nào và hành khách hoặc nhân viên thấy gì? (Báo lỗi hệ thống, hoàn tác thao tác đang làm / Khác) | IF-07 scheduleTrigger, cancelTriggers; IF-10 đến IF-13; UC-002 bước 9, UC-008 bước 10, UC-013 bước 5, UC-015 bước 10 | P04 của UC-002, UC-008, UC-013, UC-015 không có luồng lỗi hệ thống nội bộ |
| Q-105 | Khi máy chủ từ chối kết quả soát vé hoặc báo chuyến chưa có danh sách hành khách, máy soát vé xử lý thế nào? (Giữ kết quả và báo phụ xe / Bỏ kết quả / Khác) | IF-09 submitCheckResult, fetchPassengerList (ServerRejectedException); UC-015 bước 1, 10 | P04 UC-015 bước 10, 10a chỉ có luồng mất sóng; liên quan Q-74, Q-81 |
| Q-106 | Khi hai hành khách cùng giữ một chỗ gần như đồng thời và bước giữ chỗ (bước 9) của một bên thất bại dù bước kiểm tra chỗ (bước 6) đã qua, hành khách bên đó thấy gì và quay lại bước nào? (Báo chỗ không còn trống, quay lại bước 4 / Khác) | IF-10 saveTrip (SeatAlreadyHeldException); UC-002 bước 9; P04 UC-002 | BR-03, REQ-67: không trùng chỗ; P04 UC-002 chỉ có luồng 6b ở bước 6 |
| Q-107 | Khi máy soát vé không ghi được dữ liệu cục bộ (đầy bộ nhớ, tệp hỏng) lúc ghi nhận vé đã soát hoặc kết quả chờ gửi, máy báo gì và phụ xe tiếp tục thế nào? (Báo lỗi, quét lại / Khác) | IF-12 trên SS-08 (LocalStoreException); UC-015 bước 6, 10a; NFR-02 | NFR-02: báo kết quả khi mất sóng; P04 UC-015 không có luồng lỗi lưu cục bộ |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-100 | Thanh toán trực tuyến đi theo hai bước: SS-01 gửi yêu cầu thanh toán (requestPayment, đồng bộ) rồi nhận kết quả bất đồng bộ qua IF-02 receivePaymentResult; hành khách nhập thẻ tại trang của cổng nên hệ thống không nhận dữ liệu thẻ. Các operation requestPayment, queryPaymentStatus và IF-02 ở trạng thái Tạm. | P10 đã có IF-02 (gọi ngược) và P09 F7 nêu kết quả thanh toán trả về qua interface; NFR-06 chỉ nêu gửi thông tin thanh toán và nhận kết quả; UC-003 chưa có P04, P07. Chờ Q-83, Q-24 | IF-01 requestPayment, queryPaymentStatus; IF-02 receivePaymentResult; BB3 và WB1, WB3 của SS-01 |
| ASM-101 | Thời gian tối đa người dùng của UC-008 và UC-013 chờ kết quả hoàn tiền trước khi hệ thống báo chưa rõ kết quả là 45 giây. | Nguồn không nêu thời hạn chờ; thời gian chờ đọc 30 giây cộng một lần tra cứu 10 giây cộng dự phòng 5 giây. Đây là thời hạn người dùng cảm nhận được nên không đặt bằng quyết định thiết kế. Chờ Q-55 | IF-01 requestRefund (cột Timeout); F7a của SS-01 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-008 luồng 9a | Chỉ có luồng cổng trả hoàn không thành công; thiếu luồng cổng không phản hồi hoặc kết quả hoàn không rõ (RefundResult Unknown, PaymentGatewayUnavailableException) | Thêm luồng ngoại lệ ở bước 8, 9 sau khi Q-55 được trả lời; nêu vé còn hiệu lực hay không khi chưa rõ |
| P04 | UC-013 luồng 8a | Như trên cho hoàn tiền từng vé khi huỷ chuyến | Thêm luồng kết quả hoàn không rõ sau khi Q-55 được trả lời |
| P04 | UC-002 bước 9, 12 | Bước 9 thiếu luồng khi hai phiên giữ cùng chỗ (Q-106) và khi kho dữ liệu, kho mốc lỗi (Q-104); bước 12 thiếu luồng gửi SMS lỗi (Q-56) | Thêm luồng ngoại lệ sau khi Q-104, Q-106, Q-56 được trả lời |
| P04 | UC-003 (chưa có), UC-005 (chưa có) | SS-01 requestPayment và SS-04 printTicket dựa vào UC chưa có đặc tả; lỗi in và kết quả thanh toán muộn chưa có luồng (Q-102, Q-10) | Chạy P04 UC-003, UC-005 rồi P07 tương ứng, sau đó chạy lại P11b cho SS-01, SS-04 |
| P04 | UC-015 bước 1, 4, 6, 10 | Thiếu luồng lỗi đọc mã vạch (Q-103), máy chủ từ chối (Q-105), lỗi lưu cục bộ (Q-107) | Thêm luồng ngoại lệ sau khi Q-103, Q-105, Q-107 được trả lời |
| P08 | AC-B-PaymentGateway, AC-E-Refund | // requestRefund và // returnRefundResult được hiện thực bằng một operation requestRefund trả kết quả đồng bộ; khoản hoàn chưa rõ kết quả cần giữ requestKey để đối soát sau, Refund hiện chỉ có kết quả đã biết | P08 ghi hai trách nhiệm là một lời gọi có kết quả trả về; AC-E-Refund có thêm trạng thái chưa rõ kèm khoá yêu cầu khi chạy lại |
| P10 | F2 bảng interface (IF-04, IF-05, IF-07, IF-08, IF-12), F4 (PKG-21) | P11b thêm operation kỹ thuật startScanning, stopScanning, receiveScanError, findTripById, findCheckSession, findPendingCheckSessions...; thêm IF-14 IResultDeliveryListener (chiều ngược, định nghĩa ở PKG-21, DC-CheckBoardingTicketService hiện thực) | Ghi IF-14 vào F2 và F4, ghi PKG-11 hiện thực IF-14; rà lại danh sách operation của các IF trên |
| P10 | F4 PKG-22, PKG-28, PKG-19 | Thiếu phần tử cho ngoại lệ và kiểu của chữ ký interface: DC-SeatAlreadyHeldException (PKG-22), DC-PersistenceUnavailableException và DC-LocalStoreException (PKG-28), DC-TriggerKind (PKG-19); PKG-14, PKG-20 cần phụ thuộc PKG-28 cho ngoại lệ dùng chung | Thêm các phần tử và phụ thuộc này vào F4, F6 |
| P10 | F2 SS-05, P09 F7 | Ghi SS-05 "duyệt dữ liệu tìm mốc đến hạn" nhưng PKG-19 không phụ thuộc package nào, không đọc được Booking; P11b chọn SS-05 giữ kho mốc riêng (DC-TriggerStore) trong CSDL | Sửa lời F2 của P10 và F7 của P09 cho khớp (kho mốc riêng của SS-05, mốc chiếm bằng cập nhật có điều kiện) |

## Vấn đề còn mở

- Target 1 không đạt hoàn toàn: IF-13 IAccountRepository chưa có use case nào dùng (UC-009 đến UC-011 chưa có P07), hai operation giữ chỗ; IF-01 requestPayment, queryPaymentStatus và IF-02 receivePaymentResult gắn với UC-003 chưa có P04, P07 nên ở trạng thái Tạm (ASM-100). Chạy lại P11b cho SS-01 và SS-07 khi có P07 của UC-003 và UC-009 đến UC-011.
- Target 2: trách nhiệm của AC-B-PaymentGateway ngoài hoàn tiền (thanh toán) chờ P07 của UC-003. SS-03 và SS-04 có operation kỹ thuật (startScanning, stopScanning, receiveScanError, printTicket theo NFR-09) ghi lý do ở cột UC.
- Target 3: lỗi của kho dữ liệu, kho mốc, lưu cục bộ dùng kiểu ngoại lệ chung; thời hạn người dùng chờ hoàn tiền (ASM-101) là giá trị nghiệp vụ duy nhất phải dùng ASM. Kiểu Ticket, Trip, Booking, TripPassengerList, TicketCheckSession nằm ở layer Domain là layer thấp nhất theo P09, nên được dùng trong chữ ký interface của layer Services mà không kéo phụ thuộc lên; quy tắc A3 viết cho trường hợp Domain nằm trên, không áp dụng ở đây.
- Target 5: nhiều loại lỗi (kết quả không rõ, lỗi thiết bị, lỗi kỹ thuật nội bộ) không có luồng P04; đã ghi Đề xuất sửa P04 và Q-100 đến Q-107.
- Target 7: SS-07 (trừ saveTrip), SS-08 (trừ saveCheckSession), queryPaymentStatus và stopScanning dùng ánh xạ 1-1 thay cho sơ đồ hộp trắng, đã ghi rõ ở F4 từng subsystem. Hộp đen của UC-003 và UC-005 dùng lifeline control tạm vì chưa có P07.
- Target 10: sequence diagram để fragment phủ lên lifeline và message đi qua lifeline ở giữa theo ký pháp UML, nên không thoả hoàn toàn "không có hai node chồng nhau, cạnh không cắt qua node" của C7.3; các trang Phần tử và Phụ thuộc thoả khoảng cách tối thiểu 40, toạ độ bội 10, cạnh nằm trong dải trống giữa các hàng. Chưa mở bằng draw.io để xem nhãn và nét vẽ.
- Chọn giữa hai quy tắc (C9): prompt yêu cầu "không phần tử bên trong subsystem nào public" nhưng kiểu dữ liệu và ngoại lệ trong chữ ký interface phải public để client dùng; đã coi chúng thuộc interface, ghi "public (thuộc chữ ký IF-nn)" ở F5a và giữ mọi lớp hiện thực package-private.
- Chọn giữa hai quy tắc (C9): prompt F5a chỉ liệt kê năm vai trò (Điều phối, Giao tiếp ngoài, Chuyển đổi dữ liệu, Kiểu dữ liệu, Ngoại lệ); hàng đợi gửi lại của SS-06 cần vai trò lưu tạm nên ghi "Lưu tạm".
- Chọn giữa hai quy tắc (C9): phạm vi "Tất cả" gồm cả SS-07, SS-08 (lưu trữ) dù mục 3 của prompt nói chạy cho subsystem giao tiếp ngoài; đã thiết kế cả tám subsystem để thoả Target 1, riêng SS-07, SS-08 dùng hộp trắng rút gọn.
- SS-02 gửi SMS đồng bộ trong vòng lặp từng vé (theo P07): một chuyến huỷ nhiều vé có thể kéo dài luồng, rủi ro với thời gian phản hồi NFR-01; P12 cân nhắc gửi bất đồng bộ.
- Hợp đồng với phía hiện thực: DC-BoardingSyncRestController phải xử lý idempotent theo tripId cho submitCheckResult; DC-BookTicketOnlineService phải kiểm tra trạng thái lần đặt trước khi trả chỗ khi nhận handleTrigger; P12 thiết kế chi tiết hai chỗ này.
