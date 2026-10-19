# P11b - SS-01 OnlinePayment - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | SS-01 OnlinePayment (package PKG-23 PaymentIntegration); lần chạy đầu cho mọi subsystem của P10 F2 |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102, ghi ở file chung P11b-system-interfaces.md); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-005 Mua hoặc gia hạn gói tập | AC-C-PurchaseOrRenewPackageHandler (DC-PurchaseOrRenewPackageHandler) | SD1b STT 3.1.2 requestPayment (đơn mua), bước 9; SD2 (biến thể Lễ tân) dùng lại SD1b cho bước 9, 10 | Đơn mua: người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả | 9a (hết thời hạn BR-04 mà đơn mua chưa thanh toán thành công); 10a (giao dịch không thành công); cổng không phản hồi: P04 chưa có luồng (Q-77) |
| UC-005 Mua hoặc gia hạn gói tập | Cổng thanh toán --> AC-C-PurchaseOrRenewPackageHandler (DC-PurchaseOrRenewPackageHandler) | SD1b STT 4 returnPaymentResult (kết quả giao dịch) và 4.1 handlePaymentResult, bước 10 | Kết quả giao dịch: thành công, không thành công | 10a (thanh toán lại hay tạo đơn mới: Q-13); kết quả đến sau khi đơn bị huỷ: Q-14; cổng tự gửi kết quả về hay phần mềm tra cứu: Q-45 |

- UC-010, UC-015, UC-018 không có message tới boundary AC-B-PaymentGateway. Biến thể Lễ tân của UC-005 có toán hạng cổng thanh toán trong alt; lễ tân có thanh toán qua cổng hay không chờ Q-98.
- Giao diện hiển thị cho người trả tiền (trang của cổng, biểu mẫu trong ứng dụng) chờ Q-96; interface ở mức dưới không mang chi tiết đó.

## F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Gửi yêu cầu thu tiền cho một đơn mua tới cổng thanh toán và tra cứu trạng thái giao dịch. | SS-01 OnlinePayment | DC-PurchaseOrRenewPackageHandler (PKG-14) | PKG-23 PaymentIntegration |
| IF-08 | IPaymentResultReceiver | Nhận kết quả giao dịch từ SS-01 để control xử lý tiếp. | DC-PurchaseOrRenewPackageHandler (PKG-14); interface gọi ngược do SS-01 gọi | SS-01 OnlinePayment | PKG-23 PaymentIntegration |

- Số operation: IF-01 có 2, IF-08 có 1 (trong khoảng 1-7).
- Layer: IF-01, IF-08 ở PKG-23 (Services), cùng layer với SS-01. DC-PurchaseOrRenewPackageHandler ở PKG-14 (Application) hiện thực IF-08, realization đi xuống PKG-23 (P09 F6 V4).
- Kiểu trong chữ ký: DC-PackageOrder (PKG-27), DC-Money và DC-TransactionReference (PKG-32) đều ở Domain, layer thấp nhất (P09 A4); DC-PaymentRequestResult, DC-PaymentResult ở PKG-23.

## F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-08) | requestPayment(order: PackageOrder): PaymentRequestResult | order: PackageOrder - trạng thái chờ thanh toán, số tiền phải trả lớn hơn 0 | PaymentRequestResult: status (Accepted / Rejected), transactionRef: TransactionReference (mã tham chiếu do phần mềm sinh trước khi gửi, dùng để tra cứu) | Rejected (Nghiệp vụ, nằm trong kết quả); PaymentGatewayUnavailable (Kỹ thuật tạm thời, yêu cầu chưa gửi); PaymentOutcomeUnknown (Không rõ kết quả, kèm transactionRef) | UC-005 (bước 9) | Đơn mua đã tạo ở trạng thái chờ thanh toán (bước 8) | Accepted: cổng đã có giao dịch cho đơn, chưa có kết luận thanh toán; Rejected: cổng không tạo giao dịch | Đồng bộ | Không (không tự thử lại yêu cầu thanh toán) | 10 giây (CHINH_SACH_LOI) |
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-08) | queryPaymentStatus(transactionRef: TransactionReference): PaymentResult | transactionRef: TransactionReference - do requestPayment trả về | PaymentResult: status (Succeeded / Failed / Pending / NotFound), transactionRef, paidAmount: Money (khi Succeeded) | PaymentGatewayUnavailable (Kỹ thuật tạm thời) | UC-005 (bước 10; kỹ thuật) | Đã gọi requestPayment cho đơn | Không đổi dữ liệu ở cổng và ở phần mềm | Đồng bộ | Có | 10 giây (CHINH_SACH_LOI) |
| IF-08 | IPaymentResultReceiver | Cổng thanh toán (ACT-08) | returnPaymentResult(result: PaymentResult): void | result: PaymentResult - status là Succeeded hoặc Failed | - | - (lỗi xử lý ở bên hiện thực không đi ngược vào SS-01) | UC-005 (bước 10, luồng 10a) | Đơn mua đã gửi cho cổng (requestPayment trả Accepted hoặc PaymentOutcomeUnknown) | Bên hiện thực đã nhận kết quả để xử lý tiếp bước 11 đến 13 hoặc luồng 10a | Bất đồng bộ (SS-01 không chờ xử lý xong) | Có (cổng hoặc tra cứu có thể đưa cùng một kết quả hai lần, P09 F7; bên hiện thực xử lý lặp lại được) | - |

- Ánh xạ trách nhiệm P08 của AC-B-PaymentGateway: // requestPayment --> IF-01.requestPayment; // returnPaymentResult --> IF-08.returnPaymentResult.
- queryPaymentStatus là operation kỹ thuật cần cho chính sách lỗi: CHINH_SACH_LOI yêu cầu tra cứu giao dịch qua API tra cứu của cổng khi chưa biết giao dịch đã thành công hay chưa; operation này cũng cho Application cách nhận kết quả bằng tra cứu nếu Q-45 chọn phần mềm tra cứu.
- Mã tham chiếu giao dịch do phần mềm sinh trước khi gửi (Thiết kế: có mã trước khi gửi thì tra cứu được cả khi không nhận được phản hồi). Việc API tra cứu của cổng nhận mã này hay mã do cổng cấp cần tài liệu API, hiện chưa có (TAI_LIEU_GIAO_TIEP: Không có).
- requestPayment không idempotent vì chưa biết cổng có loại trùng theo mã tham chiếu; chính sách là không tự thử lại nên không cần khoá.

## F4. Sequence diagram

File diagrams/P11b-subsystem-SS-01.drawio gồm 6 trang: "Hộp đen - UC-005 thanh toán qua cổng"; "Hộp trắng - requestPayment"; "Hộp trắng - queryPaymentStatus"; "Hộp trắng - returnPaymentResult"; "Phần tử"; "Phụ thuộc". STT đánh số phẳng theo trục thời gian trong mỗi trang; tọa độ bảng Node là tuyệt đối. Gate nằm trên cạnh trái khung sd, tâm gate ở y của message nên x, y của gate lệch 5 so với bội số của 10 (xem Vấn đề còn mở).

### Trang "Hộp đen - UC-005 thanh toán qua cổng" (SS01-BB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-BB1-FR | Fragment | sd Hộp đen UC-005 cổng thanh toán | - | - | Khung sd của trang | 20 | 0 | 580 | 520 |
| SS01-BB1-L1 | Lifeline | :PurchaseOrRenewPackageHandler | «control» | - | DC-PurchaseOrRenewPackageHandler (PKG-14); lớp phân tích AC-C-PurchaseOrRenewPackageHandler | 100 | 40 | 120 | 460 |
| SS01-BB1-L2 | Lifeline | :IF-01 IPaymentGateway | «interface» | - | Subsystem SS-01 hiện thực | 260 | 40 | 120 | 460 |
| SS01-BB1-L3 | Lifeline | :IF-08 IPaymentResultReceiver | «interface» | - | DC-PurchaseOrRenewPackageHandler hiện thực; SS-01 gọi | 420 | 40 | 120 | 460 |
| SS01-BB1-F1 | Fragment | alt [yêu cầu được cổng nhận hoặc từ chối] | - | - | đường ngăn SS01-BB1-F1-O2-SEP nét đứt tại y=180; đường ngăn SS01-BB1-F1-O3-SEP nét đứt tại y=220 | 80 | 140 | 320 | 110 |
| SS01-BB1-F2 | Fragment | alt [phần mềm tra cứu kết quả (Q-45)] | - | - | đường ngăn SS01-BB1-F2-O2-SEP nét đứt tại y=380 | 80 | 300 | 480 | 150 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS01-BB1-F1 toán hạng 2: [không gửi được yêu cầu]; SS01-BB1-F1 toán hạng 3: [không rõ kết quả sau khi đã gửi]; SS01-BB1-F2 toán hạng 2: [kết quả được đẩy tới IF-08 (Q-45)].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-BB1-M01 | 1 | SS01-BB1-L1 | SS01-BB1-L2 | requestPayment(order) | Đồng bộ | - | UC-005 bước 9; requestPayment |
| SS01-BB1-M02 | 2 | SS01-BB1-L2 | SS01-BB1-L1 | PaymentRequestResult (Accepted / Rejected) | Trả về | SS01-BB1-F1 (toán hạng 1) | UC-005 bước 9; luồng 10a khi Rejected |
| SS01-BB1-M03 | 3 | SS01-BB1-L2 | SS01-BB1-L1 | PaymentGatewayUnavailable | Trả về | SS01-BB1-F1 (toán hạng 2) | UC-005 bước 9; Q-77 |
| SS01-BB1-M04 | 4 | SS01-BB1-L2 | SS01-BB1-L1 | PaymentOutcomeUnknown(transactionRef) | Trả về | SS01-BB1-F1 (toán hạng 3) | UC-005 bước 9; Q-77, Q-14 |
| SS01-BB1-M05 | 5 | SS01-BB1-L1 | SS01-BB1-L1 | awaitPaymentResult() | Tự gọi | - | UC-005 bước 9 (chờ trong thời hạn BR-04) |
| SS01-BB1-M06 | 6 | SS01-BB1-L1 | SS01-BB1-L2 | queryPaymentStatus(transactionRef) | Đồng bộ | SS01-BB1-F2 (toán hạng 1) | UC-005 bước 10; queryPaymentStatus (Q-45) |
| SS01-BB1-M07 | 7 | SS01-BB1-L2 | SS01-BB1-L1 | PaymentResult | Trả về | SS01-BB1-F2 (toán hạng 1) | UC-005 bước 10; queryPaymentStatus |
| SS01-BB1-M08 | 8 | SS01-BB1-L2 | SS01-BB1-L3 | returnPaymentResult(result) | Bất đồng bộ | SS01-BB1-F2 (toán hạng 2) | UC-005 bước 10, 10a; returnPaymentResult |
| SS01-BB1-M09 | 9 | SS01-BB1-L3 | SS01-BB1-L1 | handlePaymentResult(result) | Đồng bộ | SS01-BB1-F2 (toán hạng 2) | UC-005 bước 10 đến 13, 10a |

### Trang "Hộp trắng - requestPayment" (SS01-WB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-WB1-FR | Fragment | sd requestPayment | - | - | Khung sd của trang | 20 | 0 | 740 | 960 |
| SS01-WB1-L1 | Lifeline | :PaymentGatewayFacade | «facade» | SS-01 | DC-PaymentGatewayFacade; hiện thực IF-01 | 100 | 40 | 120 | 900 |
| SS01-WB1-L2 | Lifeline | :PaymentMessageMapper | «mapper» | SS-01 | DC-PaymentMessageMapper | 260 | 40 | 120 | 900 |
| SS01-WB1-L3 | Lifeline | :PaymentGatewayClient | «adapter» | SS-01 | DC-PaymentGatewayClient | 420 | 40 | 120 | 900 |
| SS01-WB1-L4 | Actor | Cổng thanh toán (ACT-08) | «actor» | - | Tác nhân hệ thống ngoài | 580 | 40 | 120 | 900 |
| SS01-WB1-FR-G1 | Gate | requestPayment | - | SS01-WB1-FR | Gate vào khung, message STT 1 | 15 | 115 | 10 | 10 |
| SS01-WB1-FR-G11 | Gate | PaymentRequestResult (Accepted / Rejected) | - | SS01-WB1-FR | Gate ra khung, message STT 11 | 15 | 515 | 10 | 10 |
| SS01-WB1-FR-G13 | Gate | PaymentGatewayUnavailable | - | SS01-WB1-FR | Gate ra khung, message STT 13 | 15 | 595 | 10 | 10 |
| SS01-WB1-FR-G19 | Gate | PaymentRequestResult (Accepted) | - | SS01-WB1-FR | Gate ra khung, message STT 19 | 15 | 835 | 10 | 10 |
| SS01-WB1-FR-G20 | Gate | PaymentOutcomeUnknown(ref) | - | SS01-WB1-FR | Gate ra khung, message STT 20 | 15 | 875 | 10 | 10 |
| SS01-WB1-F1 | Fragment | alt [cổng phản hồi trong 10 giây] | - | - | đường ngăn SS01-WB1-F1-O2-SEP nét đứt tại y=540; đường ngăn SS01-WB1-F1-O3-SEP nét đứt tại y=620 | 70 | 330 | 660 | 570 |
| SS01-WB1-F2 | Fragment | alt [tìm thấy giao dịch ở cổng] | - | SS01-WB1-F1 | đường ngăn SS01-WB1-F2-O2-SEP nét đứt tại y=860 | 80 | 820 | 160 | 70 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS01-WB1-F1 toán hạng 2: [không kết nối được, yêu cầu chưa gửi]; SS01-WB1-F1 toán hạng 3: [quá 10 giây sau khi đã gửi]; SS01-WB1-F2 toán hạng 2: [không thấy giao dịch hoặc tra cứu lỗi].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-WB1-M01 | 1 | SS01-WB1-FR-G1 | SS01-WB1-L1 | requestPayment(order) | Đồng bộ | - | requestPayment; UC-005 bước 9 |
| SS01-WB1-M02 | 2 | SS01-WB1-L1 | SS01-WB1-L1 | generateTransactionRef(order) | Tự gọi | - | Mã tham chiếu sinh trước khi gửi để tra cứu được khi mất phản hồi |
| SS01-WB1-M03 | 3 | SS01-WB1-L1 | SS01-WB1-L2 | toGatewayRequest(order, ref) | Đồng bộ | - | requestPayment |
| SS01-WB1-M04 | 4 | SS01-WB1-L2 | SS01-WB1-L1 | gatewayRequest | Trả về | - | requestPayment |
| SS01-WB1-M05 | 5 | SS01-WB1-L1 | SS01-WB1-L3 | send(gatewayRequest) | Đồng bộ | - | requestPayment; timeout 10 giây |
| SS01-WB1-M06 | 6 | SS01-WB1-L3 | SS01-WB1-L4 | createTransaction(gatewayRequest) | Đồng bộ | - | UC-005 bước 9 |
| SS01-WB1-M07 | 7 | SS01-WB1-L4 | SS01-WB1-L3 | phản hồi tạo giao dịch | Trả về | SS01-WB1-F1 (toán hạng 1) | UC-005 bước 9 |
| SS01-WB1-M08 | 8 | SS01-WB1-L3 | SS01-WB1-L1 | gatewayResponse | Trả về | SS01-WB1-F1 (toán hạng 1) | requestPayment |
| SS01-WB1-M09 | 9 | SS01-WB1-L1 | SS01-WB1-L2 | toPaymentRequestResult(response, ref) | Đồng bộ | SS01-WB1-F1 (toán hạng 1) | requestPayment |
| SS01-WB1-M10 | 10 | SS01-WB1-L2 | SS01-WB1-L1 | PaymentRequestResult | Trả về | SS01-WB1-F1 (toán hạng 1) | requestPayment |
| SS01-WB1-M11 | 11 | SS01-WB1-L1 | SS01-WB1-FR-G11 | PaymentRequestResult (Accepted / Rejected) | Trả về | SS01-WB1-F1 (toán hạng 1) | requestPayment; luồng 10a khi Rejected |
| SS01-WB1-M12 | 12 | SS01-WB1-L3 | SS01-WB1-L1 | ConnectionFailed | Trả về | SS01-WB1-F1 (toán hạng 2) | requestPayment; yêu cầu chưa được gửi |
| SS01-WB1-M13 | 13 | SS01-WB1-L1 | SS01-WB1-FR-G13 | PaymentGatewayUnavailable | Trả về | SS01-WB1-F1 (toán hạng 2) | requestPayment; Q-77 |
| SS01-WB1-M14 | 14 | SS01-WB1-L3 | SS01-WB1-L1 | ResponseTimeout | Trả về | SS01-WB1-F1 (toán hạng 3) | requestPayment; kết quả không rõ |
| SS01-WB1-M15 | 15 | SS01-WB1-L1 | SS01-WB1-L3 | lookup(ref) | Đồng bộ | SS01-WB1-F1 (toán hạng 3) | Tra cứu một lần, không gửi lại yêu cầu thanh toán |
| SS01-WB1-M16 | 16 | SS01-WB1-L3 | SS01-WB1-L4 | queryTransaction(ref) | Đồng bộ | SS01-WB1-F1 (toán hạng 3) | API tra cứu giao dịch của cổng |
| SS01-WB1-M17 | 17 | SS01-WB1-L4 | SS01-WB1-L3 | trạng thái giao dịch | Trả về | SS01-WB1-F1 (toán hạng 3) | requestPayment |
| SS01-WB1-M18 | 18 | SS01-WB1-L3 | SS01-WB1-L1 | lookupResult | Trả về | SS01-WB1-F1 (toán hạng 3) | requestPayment |
| SS01-WB1-M19 | 19 | SS01-WB1-L1 | SS01-WB1-FR-G19 | PaymentRequestResult (Accepted) | Trả về | SS01-WB1-F2 (toán hạng 1) | requestPayment; giao dịch đã tồn tại ở cổng |
| SS01-WB1-M20 | 20 | SS01-WB1-L1 | SS01-WB1-FR-G20 | PaymentOutcomeUnknown(ref) | Trả về | SS01-WB1-F2 (toán hạng 2) | requestPayment; Q-77, Q-14 |

### Trang "Hộp trắng - queryPaymentStatus" (SS01-WB2)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-WB2-FR | Fragment | sd queryPaymentStatus | - | - | Khung sd của trang | 20 | 0 | 740 | 640 |
| SS01-WB2-L1 | Lifeline | :PaymentGatewayFacade | «facade» | SS-01 | DC-PaymentGatewayFacade; hiện thực IF-01 | 100 | 40 | 120 | 580 |
| SS01-WB2-L2 | Lifeline | :PaymentMessageMapper | «mapper» | SS-01 | DC-PaymentMessageMapper | 260 | 40 | 120 | 580 |
| SS01-WB2-L3 | Lifeline | :PaymentGatewayClient | «adapter» | SS-01 | DC-PaymentGatewayClient | 420 | 40 | 120 | 580 |
| SS01-WB2-L4 | Actor | Cổng thanh toán (ACT-08) | «actor» | - | Tác nhân hệ thống ngoài | 580 | 40 | 120 | 580 |
| SS01-WB2-FR-G1 | Gate | queryPaymentStatus | - | SS01-WB2-FR | Gate vào khung, message STT 1 | 15 | 115 | 10 | 10 |
| SS01-WB2-FR-G10 | Gate | PaymentResult | - | SS01-WB2-FR | Gate ra khung, message STT 10 | 15 | 475 | 10 | 10 |
| SS01-WB2-FR-G12 | Gate | PaymentGatewayUnavailable | - | SS01-WB2-FR | Gate ra khung, message STT 12 | 15 | 555 | 10 | 10 |
| SS01-WB2-F1 | Fragment | alt [cổng phản hồi trong 10 giây] | - | - | đường ngăn SS01-WB2-F1-O2-SEP nét đứt tại y=500 | 80 | 300 | 640 | 270 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS01-WB2-F1 toán hạng 2: [không kết nối được hoặc quá 10 giây].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-WB2-M01 | 1 | SS01-WB2-FR-G1 | SS01-WB2-L1 | queryPaymentStatus(ref) | Đồng bộ | - | queryPaymentStatus; UC-005 bước 10 (Q-45) |
| SS01-WB2-M02 | 2 | SS01-WB2-L1 | SS01-WB2-L2 | toLookupRequest(ref) | Đồng bộ | - | queryPaymentStatus |
| SS01-WB2-M03 | 3 | SS01-WB2-L2 | SS01-WB2-L1 | lookupRequest | Trả về | - | queryPaymentStatus |
| SS01-WB2-M04 | 4 | SS01-WB2-L1 | SS01-WB2-L3 | lookup(lookupRequest) | Đồng bộ | - | queryPaymentStatus; timeout 10 giây |
| SS01-WB2-M05 | 5 | SS01-WB2-L3 | SS01-WB2-L4 | queryTransaction(lookupRequest) | Đồng bộ | - | API tra cứu giao dịch của cổng |
| SS01-WB2-M06 | 6 | SS01-WB2-L4 | SS01-WB2-L3 | trạng thái giao dịch | Trả về | SS01-WB2-F1 (toán hạng 1) | queryPaymentStatus |
| SS01-WB2-M07 | 7 | SS01-WB2-L3 | SS01-WB2-L1 | lookupResponse | Trả về | SS01-WB2-F1 (toán hạng 1) | queryPaymentStatus |
| SS01-WB2-M08 | 8 | SS01-WB2-L1 | SS01-WB2-L2 | toPaymentResult(response) | Đồng bộ | SS01-WB2-F1 (toán hạng 1) | queryPaymentStatus |
| SS01-WB2-M09 | 9 | SS01-WB2-L2 | SS01-WB2-L1 | PaymentResult | Trả về | SS01-WB2-F1 (toán hạng 1) | queryPaymentStatus |
| SS01-WB2-M10 | 10 | SS01-WB2-L1 | SS01-WB2-FR-G10 | PaymentResult | Trả về | SS01-WB2-F1 (toán hạng 1) | queryPaymentStatus |
| SS01-WB2-M11 | 11 | SS01-WB2-L3 | SS01-WB2-L1 | CommunicationFailed | Trả về | SS01-WB2-F1 (toán hạng 2) | queryPaymentStatus |
| SS01-WB2-M12 | 12 | SS01-WB2-L1 | SS01-WB2-FR-G12 | PaymentGatewayUnavailable | Trả về | SS01-WB2-F1 (toán hạng 2) | queryPaymentStatus; Q-77 |

### Trang "Hộp trắng - returnPaymentResult" (SS01-WB3)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS01-WB3-FR | Fragment | sd returnPaymentResult | - | - | Khung sd của trang | 20 | 0 | 740 | 400 |
| SS01-WB3-L1 | Lifeline | :PaymentGatewayFacade | «facade» | SS-01 | DC-PaymentGatewayFacade; hiện thực IF-01 | 100 | 40 | 120 | 340 |
| SS01-WB3-L2 | Lifeline | :PaymentMessageMapper | «mapper» | SS-01 | DC-PaymentMessageMapper | 260 | 40 | 120 | 340 |
| SS01-WB3-L3 | Lifeline | :PaymentGatewayClient | «adapter» | SS-01 | DC-PaymentGatewayClient | 420 | 40 | 120 | 340 |
| SS01-WB3-L4 | Actor | Cổng thanh toán (ACT-08) | «actor» | - | Tác nhân hệ thống ngoài | 580 | 40 | 120 | 340 |
| SS01-WB3-FR-G5 | Gate | returnPaymentResult | - | SS01-WB3-FR | Gate ra khung, message STT 5 | 15 | 275 | 10 | 10 |
| SS01-WB3-F1 | Fragment | alt [thông điệp hợp lệ, khớp một giao dịch đã gửi] | - | - | đường ngăn SS01-WB3-F1-O2-SEP nét đứt tại y=300 | 80 | 260 | 160 | 70 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS01-WB3-F1 toán hạng 2: [sai định dạng hoặc không khớp giao dịch nào].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS01-WB3-M01 | 1 | SS01-WB3-L4 | SS01-WB3-L3 | thông điệp kết quả giao dịch | Bất đồng bộ | - | UC-005 bước 10 (kênh nhận: Q-45) |
| SS01-WB3-M02 | 2 | SS01-WB3-L3 | SS01-WB3-L1 | onGatewayResult(message) | Đồng bộ | - | returnPaymentResult |
| SS01-WB3-M03 | 3 | SS01-WB3-L1 | SS01-WB3-L2 | toPaymentResult(message) | Đồng bộ | - | returnPaymentResult |
| SS01-WB3-M04 | 4 | SS01-WB3-L2 | SS01-WB3-L1 | PaymentResult | Trả về | - | returnPaymentResult |
| SS01-WB3-M05 | 5 | SS01-WB3-L1 | SS01-WB3-FR-G5 | returnPaymentResult(result) | Bất đồng bộ | SS01-WB3-F1 (toán hạng 1) | returnPaymentResult (IF-08); UC-005 bước 10, 10a |
| SS01-WB3-M06 | 6 | SS01-WB3-L1 | SS01-WB3-L1 | discardAndLog(message) | Tự gọi | SS01-WB3-F1 (toán hạng 2) | returnPaymentResult; thông điệp không dùng được |

Quy tắc ngữ nghĩa đã áp dụng: message mức thiết kế ghi chữ ký với đối số; message bất đồng bộ đầu mũi tên mở, nét liền (endArrow=open;endFill=0;html=1;); client chỉ gọi interface; không có message từ subsystem tới lớp giao diện người dùng; mỗi message đi qua khung sd có một gate riêng.

## F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-PaymentGatewayFacade | PaymentGatewayFacade | Điều phối | Hiện thực IF-01: sinh mã tham chiếu, gọi Mapper và Client, áp timeout 10 giây, không gửi lại yêu cầu thanh toán, tra cứu đúng một lần khi không rõ kết quả, đổi lỗi giao thức thành ngoại lệ của interface, gọi IF-08 khi có kết quả | package-private | IF-01 |
| DC-PaymentMessageMapper | PaymentMessageMapper | Chuyển đổi dữ liệu | Đổi PackageOrder, TransactionReference, Money sang thông điệp của cổng và thông điệp kết quả sang PaymentResult | package-private | - |
| DC-PaymentGatewayClient | PaymentGatewayClient | Giao tiếp ngoài | Proxy gọi API REST thanh toán và tra cứu của đối tác; phân biệt lỗi kết nối (chưa gửi) với hết thời gian chờ (đã gửi) | package-private | - |
| DC-PaymentGatewayConfig | PaymentGatewayConfig | Lưu trữ trong subsystem | Giữ địa chỉ và thông tin xác thực của cổng lấy từ cấu hình môi trường | package-private | - |
| DC-PaymentRequestResult | PaymentRequestResult (PKG-23) | Kiểu dữ liệu | status (Accepted / Rejected), transactionRef | public | - |
| DC-PaymentResult | PaymentResult (PKG-23) | Kiểu dữ liệu | status (Succeeded / Failed / Pending / NotFound), transactionRef, paidAmount | public | - |
| DC-PaymentGatewayUnavailable | PaymentGatewayUnavailable (PKG-23) | Ngoại lệ | Lỗi kỹ thuật tạm thời: yêu cầu hoặc tra cứu không tới được cổng | public | - |
| DC-PaymentOutcomeUnknown | PaymentOutcomeUnknown (PKG-23) | Ngoại lệ | Không rõ kết quả sau khi đã gửi; mang transactionRef | public | - |

b) Class diagram phần tử: trang "Phần tử" (SS01-EL). Tọa độ bảng Node là tuyệt đối trên trang; file .drawio ghi tọa độ của phần tử con tương đối theo khung subsystem. Kiểu dữ liệu và ngoại lệ ở F5 a không vẽ lại ở sơ đồ.

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-01 | Subsystem | SS-01 OnlinePayment | «subsystem» | - | Khung subsystem | 40 | 180 | 1060 | 200 |
| IF-08 | Interface | IF-08 IPaymentResultReceiver | «interface» | PKG-23 | Interface gọi ngược; DC-PurchaseOrRenewPackageHandler hiện thực | 40 | 40 | 240 | 60 |
| IF-01 | Interface | IF-01 IPaymentGateway | «interface» | PKG-23 | Interface subsystem cung cấp | 320 | 40 | 240 | 60 |
| DC-PaymentMessageMapper | Class | PaymentMessageMapper | «mapper» | SS-01 | Chuyển đổi dữ liệu | 80 | 260 | 200 | 60 |
| DC-PaymentGatewayFacade | Class | PaymentGatewayFacade | «facade» | SS-01 | Điều phối; hiện thực IF-01 | 340 | 260 | 200 | 60 |
| DC-PaymentGatewayClient | Class | PaymentGatewayClient | «adapter» | SS-01 | Giao tiếp ngoài | 600 | 260 | 200 | 60 |
| DC-PaymentGatewayConfig | Class | PaymentGatewayConfig | «config» | SS-01 | Cấu hình địa chỉ và thông tin xác thực | 860 | 260 | 200 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS01-EL-E1 | DC-PaymentGatewayFacade | IF-01 | Realization | - | Facade hiện thực IF-01 | - |
| SS01-EL-E2 | DC-PaymentGatewayFacade | IF-08 | Dependency | «use» | Facade gọi IF-08 khi có kết quả giao dịch | (380,130); (160,130) |
| SS01-EL-E3 | DC-PaymentGatewayFacade | DC-PaymentMessageMapper | Dependency | «use» | Chuyển đổi kiểu mô hình và thông điệp của cổng | - |
| SS01-EL-E4 | DC-PaymentGatewayFacade | DC-PaymentGatewayClient | Dependency | «use» | Gửi yêu cầu và tra cứu qua client | - |
| SS01-EL-E5 | DC-PaymentGatewayClient | DC-PaymentGatewayConfig | Dependency | «use» | Đọc địa chỉ và thông tin xác thực | - |

c) Cơ chế kiến trúc áp dụng

| Cơ chế | Nguồn | Cách tích hợp |
|---|---|---|
| Bảo mật dữ liệu | P09 F7 (giao dịch thu tiền là dữ liệu cần bảo vệ, truyền qua kênh mã hoá) | Mọi lời gọi tới cổng qua kênh mã hoá. SS-01 không nhận và không lưu dữ liệu thẻ (người trả tiền nhập ở phía cổng, giao diện chờ Q-96); nhật ký không ghi thông tin xác thực. |
| Giao dịch và xử lý lặp lại | P09 F7 (kết quả ngoài có thể đến hai lần) | IF-08 có thể được gọi lặp cho cùng giao dịch; bên hiện thực xử lý lặp lại được. SS-01 không giữ trạng thái đơn mua. |
| Ghi nhật ký | Thiết kế: P09 F7 không nêu | Ghi mỗi lần gọi cổng gồm transactionRef, loại lời gọi, kết quả, thời gian; lý do: đối soát khi kết quả không rõ. |
| Cấu hình địa chỉ và thông tin xác thực | Thiết kế: P09 F7 không nêu | DC-PaymentGatewayConfig đọc từ cấu hình môi trường; lý do: đổi nhà cung cấp hoặc môi trường kiểm thử không phải sửa mã (cổng có thể đổi nhà cung cấp theo KHA_NANG_THAY_DOI_GIAO_DIEN ở P10). |

## F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-01 | IF-08 | Qua interface | Báo kết quả giao dịch cho Application mà không phụ thuộc lớp bên trong Application | Ưu tiên |
| SS-01 | PKG-27 (DC-PackageOrder) | Vào package | Chữ ký requestPayment nhận đơn mua; entity ở Domain, layer thấp nhất, dùng trực tiếp trong chữ ký (P09 A4, P11b A3) | Dùng thận trọng |
| SS-01 | PKG-32 (DC-Money, DC-TransactionReference) | Vào package | Kiểu giá trị trong chữ ký đặt ở Domain để Services không phụ thuộc layer trên (P10 PKG-32) | Dùng thận trọng |

Trang "Phụ thuộc" (SS01-DP)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-01 | SubsystemBox | SS-01 OnlinePayment | «subsystem» | - | Subsystem đang xét | 40 | 40 | 240 | 260 |
| IF-08 | Interface | IF-08 IPaymentResultReceiver | «interface» | PKG-23 | Interface gọi ngược | 420 | 40 | 240 | 60 |
| PKG-27 | Package | PKG-27 Membership | - | PKG-04 Domain | Chứa DC-PackageOrder | 420 | 140 | 240 | 60 |
| PKG-32 | Package | PKG-32 ValueTypes | - | PKG-04 Domain | Chứa DC-Money, DC-TransactionReference | 420 | 240 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS01-DP-E1 | SS-01 | IF-08 | Dependency | «use» | Qua interface: chuyển kết quả giao dịch cho Application | - |
| SS01-DP-E2 | SS-01 | PKG-27 | Dependency | «use» | Vào package: chữ ký IF-01 dùng DC-PackageOrder | - |
| SS01-DP-E3 | SS-01 | PKG-32 | Dependency | «use» | Vào package: chữ ký IF-01, IF-08 dùng DC-Money, DC-TransactionReference | - |

## F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| requestPayment | Cổng từ chối tạo giao dịch cho đơn | Nghiệp vụ | Phản hồi của cổng báo từ chối | Không thử lại | PaymentRequestResult.status = Rejected | 10a (giao dịch không thành công) | Q-13 |
| requestPayment | Không kết nối được tới cổng, yêu cầu chưa gửi | Kỹ thuật tạm thời | Lỗi kết nối trước khi gửi (ConnectionFailed) | Không tự thử lại (CHINH_SACH_LOI) | PaymentGatewayUnavailable | Không có luồng tương ứng trong P04 UC-005 (cổng không phản hồi); ghi Đề xuất sửa P04 | Q-77 |
| requestPayment | Quá 10 giây sau khi đã gửi | Không rõ kết quả | Hết thời gian chờ (ResponseTimeout) | Không thử lại; tra cứu giao dịch bằng mã tham chiếu đúng một lần; thấy giao dịch --> Accepted; không thấy hoặc tra cứu lỗi --> PaymentOutcomeUnknown | PaymentRequestResult.status = Accepted, hoặc PaymentOutcomeUnknown(transactionRef) | 9a khi hết thời hạn BR-04 mà chưa có kết quả; P04 chưa có luồng "chờ xác nhận thanh toán", ghi Đề xuất sửa P04 | Q-77, Q-14 |
| queryPaymentStatus | Không kết nối được hoặc quá 10 giây | Kỹ thuật tạm thời | CommunicationFailed | Không thử lại trong subsystem; client quyết định gọi lại (operation idempotent) | PaymentGatewayUnavailable | 9a (đơn chờ tới hết thời hạn BR-04) | Q-77 |
| queryPaymentStatus | Cổng không có giao dịch với mã tham chiếu | Nghiệp vụ | Phản hồi của cổng | Không | PaymentResult.status = NotFound | 9a (Q-77 chưa chọn cách xử lý) | Q-77 |
| returnPaymentResult | Thông điệp kết quả sai định dạng hoặc không khớp giao dịch nào | Không rõ kết quả | Mapper không đọc được hoặc không đối chiếu được mã tham chiếu | Bỏ thông điệp, ghi nhật ký; kết quả vẫn lấy được bằng queryPaymentStatus | Không gọi IF-08 | 10a, 9a | Q-45 |
| returnPaymentResult | Kết quả đến sau khi đơn đã bị huỷ | Nghiệp vụ | Bên hiện thực IF-08 nhận kết quả của đơn đã huỷ | SS-01 vẫn chuyển qua IF-08; bên hiện thực quyết định | returnPaymentResult như bình thường | Không có luồng tương ứng trong P04 UC-005 (đã nêu ở Q-14) | Q-14 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | IF-01: SS01-EL-E1 (DC-PaymentGatewayFacade --> IF-01) |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt | IF-08: SS01-EL-E2 và trang Phụ thuộc |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Xem F5 a |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt | requestPayment: SS01-WB1; queryPaymentStatus: SS01-WB2; returnPaymentResult (IF-08, phía SS-01 gọi): SS01-WB3 |

## Câu hỏi mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Vấn đề còn mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).
