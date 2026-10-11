# P11b - Giao diện hệ thống và thiết bị - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI; CONG_NGHE đã chốt: Java 17, Spring Boot, Thymeleaf, PostgreSQL; Kotlin, Android, SQLite); P10-design-elements.md phiên bản 1.0 (F2 và bảng Interface gọi ngược, F4, F5, Câu hỏi mở, Giả định, Vấn đề còn mở); P08-analysis-model.md phiên bản 1.0 (F3 dòng AC-B-SmsGateway, AC-B-PaymentGateway, Vấn đề còn mở); P07-uc-analysis/UC-009-book-ticket-online-analysis.md phiên bản 1.0 (message 3.1.9, Câu hỏi mở, Giả định) và UC-017-cancel-trip-analysis.md phiên bản 1.0 (message 2.1.10, 2.1.14, Câu hỏi mở, Giả định); P04-uc-specs/UC-009-book-ticket-online.md và UC-017-cancel-trip.md phiên bản 1.0 (luồng 11a, 9a, 12a); P06-supplementary-spec.md phiên bản 1.0 (NFR-01, NFR-05, NFR-06, NFR-08, NFR-10, NFR-11, NFR-12 và các Q, ASM liên quan); P09-architecture.md phiên bản 1.0 (F4, F6, F7). Placeholder: PHAM_VI_SUBSYSTEM = Tất cả; TAI_LIEU_GIAO_TIEP = Không có; CHINH_SACH_LOI = Không có; YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-68, ASM-50 (P11a); lần chạy này cấp Q-69, ASM-51. Mã SS, IF giữ từ P10; mã DC cấp mới theo C3 |
| Phạm vi | Toàn hệ thống: 2 subsystem của bảng F2 trong P10 (SS-01 OnlinePayment, SS-02 SmsNotification). Máy in vé nhiệt và máy soát vé chưa là subsystem (P10 F1) nên không thuộc lần chạy này |
| Mã Q, ASM cuối đã cấp | Q-69, ASM-51 |

Chính sách lỗi áp dụng chung (CHINH_SACH_LOI = Không có; TAI_LIEU_GIAO_TIEP = Không có nên thiết kế ở mức interface, chưa ánh xạ chi tiết lời gọi ngoài):

- Timeout: suy từ vị trí lời gọi trong luồng, ghi "Thiết kế: <lý do>" ở cột Timeout của F3 (C1 mục 7). Không có NFR đặt thời gian chờ cổng.
- Thử lại: subsystem không tự thử lại operation nào. Hoàn tiền không idempotent, có tác dụng phụ tài chính (NFR-05). Gửi SMS: P04 chọn ghi nhận rồi tiếp tục (ASM-20, ASM-31), thử gửi lại chờ Q-35, Q-49.
- Kết quả không rõ: trả giá trị OutcomeUnknown riêng, tách khỏi từ chối nghiệp vụ, để nơi gọi và việc đối soát sau này phân biệt được. Chưa biết cổng thanh toán có tra cứu trạng thái hoàn tiền hay không (Q-69, ASM-51).
- Cô lập lỗi: ngoại lệ, mã HTTP, chuỗi JSON của giao thức ngoài không ra khỏi subsystem; mọi lỗi của hệ thống ngoài trả bằng kết quả của interface.
- Dữ liệu nhạy cảm: không có dữ liệu thẻ qua interface (NFR-01); số điện thoại và mã vé truyền qua HTTPS, nhật ký che bớt số điện thoại (P09 F7).

## SS-01 OnlinePayment

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-017 Huỷ chuyến | DC-CancelTripService (AC-C-CancelTripController) | SD1: 2.1.14 // requestTicketRefund (giao dịch, mã vé, số tiền hoàn) và 2.1.14 (trả về) kết quả hoàn tiền; bước 11, 12 (lặp ở bước 13) | Vào: mã giao dịch thanh toán, mã vé, số tiền hoàn (100% giá vé, BR-07). Ra: kết quả hoàn tiền thành công hoặc không thành công | 12a: Cổng thanh toán báo hoàn tiền không thành công hoặc không trả kết quả cho vé này (ASM-33) |
| UC-009 Đặt vé trực tuyến, UC-010 Thanh toán vé trực tuyến, UC-014 Đổi vé | - | Chờ P07 UC-010, UC-014: thu tiền vé qua Cổng thanh toán (NFR-10) chưa có message nào ở P07 | Chờ P07 | Chờ P04 UC-010, UC-014 |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Cho phép phần ứng dụng yêu cầu Cổng thanh toán hoàn tiền một vé và nhận kết quả mà không biết giao thức của cổng. Phần thu tiền vé: Chờ P07 UC-010 | SS-01 OnlinePayment (lớp hiện thực DC-OnlinePaymentManager) | DC-CancelTripService (PKG-16); dự kiến DC-PayTicketOnlineService (PKG-13) và PKG-15 khi có P07 UC-010, UC-014 (P10 F5) | PKG-21 PaymentIntegration (Services) |

Phân tích interface (A2): P10 giữ một interface IF-01 cho Cổng thanh toán. Không tách thêm vì chỉ có một nhóm client (Application) dùng cùng vai trò thanh toán với cổng; không gộp với IF-02 vì khác hệ thống ngoài, khác lý do thay đổi. IF-01 có 1 operation hoạt động và 1 operation chờ P07 UC-010, nằm trong mức hợp lý 1-7. Tên không mang tên nhà cung cấp hay công nghệ. Package PKG-21 thuộc Services, không cao hơn layer của control dùng nó (Application) nên realization không đi lên (P09 A5). Hệ thống ngoài không đẩy sự kiện vào hệ thống (P10 bảng Interface gọi ngược: Không có), nên không có interface chiều ngược.

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-06) | refundTicket(transactionCode: PaymentTransactionCode, ticketCode: TicketCode, refundAmount: Money): RefundResult | transactionCode: PaymentTransactionCode - giao dịch đã thu tiền vé, khác rỗng<br>ticketCode: TicketCode - vé mua trực tuyến thuộc giao dịch đó<br>refundAmount: Money - lớn hơn 0 và không vượt số tiền đã thu của vé (NFR-06, BR-07; nơi gọi bảo đảm) | RefundResult: status (Refunded / NotRefunded), failureKind (Declined / Unavailable / OutcomeUnknown; rỗng khi status là Refunded) | Declined (Nghiệp vụ: cổng từ chối hoàn tiền)<br>Unavailable (Kỹ thuật tạm thời: chưa thiết lập được kết nối nên cổng chưa nhận yêu cầu)<br>OutcomeUnknown (Không rõ kết quả: quá thời gian chờ sau khi đã gửi, hoặc phản hồi không phân loại được)<br>Cả ba trả bằng RefundResult. Tham số vi phạm ràng buộc --> IllegalArgumentException (lỗi lập trình, không gọi cổng) | UC-017 (bước 11, 12; luồng 12a) | Vé thuộc chuyến Đã huỷ, trạng thái hoàn tiền Chưa hoàn; nơi gọi đã ghi nhận lần gọi này trước khi gọi để mỗi vé chỉ bị gửi một yêu cầu (P09 F7) | Tối đa một yêu cầu hoàn tiền cho ticketCode đã gửi tới cổng; Refunded nghĩa là cổng xác nhận đã hoàn refundAmount; subsystem không đổi dữ liệu của hệ thống (nơi gọi ghi kết quả) | Đồng bộ | Không (khoá idempotency do hệ thống sinh được gửi kèm nhưng chưa biết cổng có hỗ trợ: Q-69, ASM-51) | 30 giây tổng, 5 giây cho kết nối (Thiết kế: hoàn tiền là giao dịch tài chính nên chờ lâu hơn gửi tin; 30 giây là mức chờ thông dụng của lời gọi cổng thanh toán khi chưa có tài liệu API; P06 không có NFR thời gian phản hồi cho UC-017, NFR-08 chỉ áp dụng UC-008, UC-009) |
| IF-01 | IPaymentGateway | Cổng thanh toán (ACT-06) | // thu tiền vé qua Cổng thanh toán (NFR-10; P10 F2 Ghi chú): Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 | UC-009, UC-010, UC-014 (Chờ P07 UC-010, UC-014) | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 |

Ánh xạ trách nhiệm của boundary nguồn: // requestTicketRefund (AC-B-PaymentGateway, P08 F3) --> refundTicket. Trách nhiệm thu tiền chưa có trong lớp phân tích nguồn nên chưa có chữ ký.

Kiểm tra layer của chữ ký: PaymentTransactionCode, TicketCode, Money nằm ở PKG-31 ValueTypes (Domain, layer thấp nhất, P09 A4); RefundResult nằm cùng package với IF-01 (PKG-21). Chữ ký không dùng kiểu của layer cao hơn Services và không lộ kiểu giao thức ngoài (chuỗi JSON, mã HTTP).

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-01.drawio gồm 4 trang. Bảng Node, bảng message là nguồn chuẩn (C7.1). STT đánh số phẳng theo trục thời gian trong mỗi trang. Message ở mức thiết kế ghi chữ ký kèm đối số; client chỉ gọi interface. Ở trang Phần tử, toạ độ x, y của lớp nằm trong khung subsystem là toạ độ tương đối so với khung.

#### Trang "Hộp đen - UC-017 refundTicket"

Bảng Node:

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S1BB1-L1 | Lifeline | :DC-CancelTripService | - | - | Control của UC-017 (AC-C-CancelTripController) | 40 | 40 | 120 | 260 |
| S1BB1-L2 | Lifeline | :IF-01 IPaymentGateway | «interface» | - | Interface do SS-01 OnlinePayment cung cấp | 200 | 40 | 120 | 260 |
| S1BB1-F1 | Fragment | loop [mỗi vé mua trực tuyến chưa hoàn (bước 13)] | - | - | Toán tử loop | 50 | 80 | 260 | 150 |
| S1BB1-F2 | Fragment | alt [cổng xác nhận đã hoàn (bước 12)] | - | - | Toán tử alt | 60 | 130 | 240 | 90 |
| S1BB1-F2-O2 | Fragment | [không hoàn được hoặc không rõ kết quả (12a)] | - | S1BB1-F2 | Toán hạng 2, nhãn đặt ngay trên đường ngăn S1BB1-F2-O2-SEP; các message dưới đường ngăn thuộc toán hạng này | 70 | 160 | 220 | 20 |

Bảng message:

| STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | S1BB1-L1 | S1BB1-L2 | refundTicket(transactionCode, ticketCode, refundAmount) | Đồng bộ | S1BB1-F1 | UC-017 bước 11 |
| 2 | S1BB1-L2 | S1BB1-L1 | RefundResult(status = Refunded) | Trả về | S1BB1-F2 | UC-017 bước 12 |
| 3 | S1BB1-L2 | S1BB1-L1 | RefundResult(status = NotRefunded, failureKind) | Trả về | S1BB1-F2-O2 | UC-017 luồng 12a |

#### Trang "Hộp trắng - refundTicket"

Bảng Node:

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S1WB1-F | Fragment | sd refundTicket | sd | - | Khung sd của operation | 40 | 0 | 800 | 760 |
| S1WB1-L1 | Lifeline | :DC-OnlinePaymentManager | - | S1WB1-F | Lớp điều phối, hiện thực IF-01 | 200 | 40 | 120 | 700 |
| S1WB1-L2 | Lifeline | :DC-PaymentMessageConverter | - | S1WB1-F | Chuyển đổi dữ liệu | 360 | 40 | 120 | 700 |
| S1WB1-L3 | Lifeline | :DC-PaymentGatewayAdapter | - | S1WB1-F | Giao tiếp ngoài (HTTPS) | 520 | 40 | 120 | 700 |
| S1WB1-L4 | Actor | ACT-06 Cổng thanh toán | - | S1WB1-F | Hệ thống ngoài (tác nhân phụ của UC-017) | 680 | 40 | 120 | 700 |
| S1WB1-F1 | Fragment | alt [kết nối được và cổng phản hồi trong 30 giây] | - | S1WB1-F | Toán tử alt | 220 | 250 | 560 | 250 |
| S1WB1-F1-O2 | Fragment | [không thiết lập được kết nối trong 5 giây, yêu cầu chưa tới cổng] | - | S1WB1-F1 | Toán hạng 2, nhãn đặt ngay trên đường ngăn S1WB1-F1-O2-SEP; các message dưới đường ngăn thuộc toán hạng này | 230 | 360 | 360 | 20 |
| S1WB1-F1-O3 | Fragment | [đã gửi, quá 30 giây không có phản hồi (kết quả không rõ)] | - | S1WB1-F1 | Toán hạng 3, nhãn đặt ngay trên đường ngăn S1WB1-F1-O3-SEP; các message dưới đường ngăn thuộc toán hạng này | 230 | 400 | 360 | 20 |
| S1WB1-F-G1 | Gate | refundTicket | - | S1WB1-F | Gate nhận message 1; tên gate là tên message đi qua | 35 | 115 | 10 | 10 |
| S1WB1-F-G14 | Gate | RefundResult | - | S1WB1-F | Gate trả message 14 ra ngoài khung; tên gate là tên message đi qua | 35 | 635 | 10 | 10 |

Bảng message:

| STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | S1WB1-F-G1 | S1WB1-L1 | refundTicket(transactionCode, ticketCode, refundAmount) | Đồng bộ | - | IF-01 refundTicket; UC-017 bước 11 |
| 2 | S1WB1-L1 | S1WB1-L2 | toRefundRequest(transactionCode, ticketCode, refundAmount) | Đồng bộ | - | Dựng yêu cầu của cổng |
| 3 | S1WB1-L2 | S1WB1-L1 | gatewayRefundRequest (kèm khoá idempotency) | Trả về | - | Dựng yêu cầu của cổng |
| 4 | S1WB1-L1 | S1WB1-L3 | call(gatewayRefundRequest, 30 giây) | Đồng bộ | - | Gọi cổng với timeout 30 giây |
| 5 | S1WB1-L3 | S1WB1-L4 | submitRefund(gatewayRefundRequest) | Đồng bộ | S1WB1-F1 | UC-017 bước 11 |
| 6 | S1WB1-L4 | S1WB1-L3 | gatewayRefundResponse | Trả về | S1WB1-F1 | UC-017 bước 12 |
| 7 | S1WB1-L3 | S1WB1-L1 | CallOutcome(Responded, gatewayRefundResponse) | Trả về | S1WB1-F1 | UC-017 bước 12 |
| 8 | S1WB1-L3 | S1WB1-L1 | CallOutcome(ConnectFailed) | Trả về | S1WB1-F1-O2 | UC-017 luồng 12a (không kết nối) |
| 9 | S1WB1-L3 | S1WB1-L4 | submitRefund(gatewayRefundRequest) | Đồng bộ | S1WB1-F1-O3 | UC-017 luồng 12a (không trả kết quả) |
| 10 | S1WB1-L3 | S1WB1-L1 | CallOutcome(TimedOut) | Trả về | S1WB1-F1-O3 | UC-017 luồng 12a (không trả kết quả) |
| 11 | S1WB1-L1 | S1WB1-L2 | toRefundResult(outcome) | Đồng bộ | - | Phân loại kết quả (F7) |
| 12 | S1WB1-L2 | S1WB1-L1 | RefundResult | Trả về | - | Phân loại kết quả (F7) |
| 13 | S1WB1-L1 | S1WB1-L1 | logOutcome(ticketCode, status, failureKind) | Tự gọi | - | Cơ chế ghi nhật ký |
| 14 | S1WB1-L1 | S1WB1-F-G14 | RefundResult | Trả về | - | UC-017 bước 12 |

#### Trang "Phần tử"

Bảng Node:

| ID | Loại (Class / Interface / Subsystem / Package) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S1EL-IF | Interface | «interface» IF-01 IPaymentGateway | «interface» | PKG-21 | public; do DC-OnlinePaymentManager hiện thực | 400 | 40 | 240 | 80 |
| S1EL-SS | Subsystem | «subsystem» SS-01 OnlinePayment | «subsystem» | PKG-21 | Khung subsystem; mọi lớp bên trong là package-private trừ kiểu dữ liệu trong chữ ký | 40 | 200 | 960 | 340 |
| S1EL-CONV | Class | DC-PaymentMessageConverter | - | SS-01 | Chuyển đổi dữ liệu | 40 | 60 | 240 | 80 |
| S1EL-MGR | Class | DC-OnlinePaymentManager | - | SS-01 | Điều phối; hiện thực IF-01 | 360 | 60 | 240 | 80 |
| S1EL-ADP | Class | DC-PaymentGatewayAdapter | - | SS-01 | Giao tiếp ngoài | 680 | 60 | 240 | 80 |
| S1EL-RES | Class | DC-RefundResult | - | SS-01 | Kiểu dữ liệu, public (chữ ký IF-01) | 40 | 220 | 240 | 80 |
| S1EL-FK | Class | «enumeration» DC-RefundFailureKind | «enumeration» | SS-01 | Kiểu dữ liệu, public (chữ ký IF-01) | 360 | 220 | 240 | 80 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| S1EL-E1 | S1EL-MGR | S1EL-IF | Realization | - | Lớp điều phối hiện thực IF-01; đồng thời là realization của SS-01 | - |
| S1EL-E2 | S1EL-MGR | S1EL-CONV | Dependency | - | Điều phối gọi chuyển đổi | - |
| S1EL-E3 | S1EL-MGR | S1EL-ADP | Dependency | - | Điều phối gọi lớp giao tiếp | - |
| S1EL-E4 | S1EL-CONV | S1EL-RES | Dependency | «create» | Chuyển đổi tạo kết quả | - |
| S1EL-E5 | S1EL-RES | S1EL-FK | Association | 1 - 0..1 | failureKind có giá trị khi status là kết quả lỗi | - |

#### Trang "Phụ thuộc"

Bảng Node:

| ID | Loại (Class / Interface / Subsystem / Package) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S1DP-IF | Interface | «interface» IF-01 IPaymentGateway | «interface» | PKG-21 | public | 160 | 200 | 240 | 60 |
| S1DP-SS | Subsystem | «subsystem» SS-01 OnlinePayment | «subsystem» | PKG-21 | Hiện thực IF-01 | 160 | 360 | 240 | 60 |
| S1DP-VT | Package | PKG-31 ValueTypes | - | PKG-04 | Kiểu giá trị trong chữ ký IF-01 | 520 | 360 | 240 | 60 |
| S1DP-C1 | Package | PKG-13 Booking | - | PKG-02 | Client dự kiến của thu tiền (UC-010) | 40 | 40 | 200 | 60 |
| S1DP-C2 | Package | PKG-16 TripManagement | - | PKG-02 | Client của refundTicket (UC-017) | 320 | 40 | 200 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| S1DP-D3 | S1DP-SS | S1DP-IF | Realization | - | Subsystem hiện thực interface | - |
| S1DP-D4 | S1DP-SS | S1DP-VT | Dependency | - | Vào package, dùng thận trọng (F6) | - |
| S1DP-D1 | S1DP-C1 | S1DP-IF | Dependency | - | Client phụ thuộc interface | (140,150); (220,150) |
| S1DP-D2 | S1DP-C2 | S1DP-IF | Dependency | - | Client phụ thuộc interface | (420,150); (340,150) |

### F5. Phần tử của subsystem

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-OnlinePaymentManager | OnlinePaymentManager | Điều phối | Nhận refundTicket; kiểm tra tham số; nhờ DC-PaymentMessageConverter dựng yêu cầu và phân loại kết quả; nhờ DC-PaymentGatewayAdapter gọi cổng; ghi nhật ký kết quả (mã vé, trạng thái, loại lỗi; không ghi dữ liệu thẻ, NFR-01); không để ngoại lệ giao thức lọt ra khỏi subsystem | package-private | IF-01 |
| DC-PaymentGatewayAdapter | PaymentGatewayAdapter | Giao tiếp ngoài | Gửi yêu cầu qua HTTPS tới API thanh toán và hoàn tiền của cổng; áp timeout kết nối 5 giây và tổng 30 giây; không thử lại; trả kết quả lời gọi thô (Responded / ConnectFailed / TimedOut); giữ địa chỉ và thông tin xác thực với cổng từ cấu hình ngoài mã nguồn | package-private | - |
| DC-PaymentMessageConverter | PaymentMessageConverter | Chuyển đổi dữ liệu | Chuyển kiểu mô hình (mã giao dịch, mã vé, số tiền) thành yêu cầu hoàn tiền của cổng và sinh khoá idempotency từ mã vé; chuyển phản hồi hoặc kết quả lời gọi thành RefundResult; mã phản hồi chưa biết hoặc phản hồi không đọc được --> OutcomeUnknown; bảng ánh xạ mã phản hồi của cổng để trống tới khi có tài liệu API | package-private | - |
| DC-RefundResult | RefundResult | Kiểu dữ liệu | Kết quả của refundTicket: status, failureKind; xuất hiện trong chữ ký IF-01 | public | - |
| DC-RefundFailureKind | RefundFailureKind | Kiểu dữ liệu | Phân loại lỗi hoàn tiền: Declined, Unavailable, OutcomeUnknown; xuất hiện trong chữ ký IF-01 qua RefundResult | public | - |

Mã DC cấp theo C3; P12 thiết kế chi tiết thuộc tính, phương thức. IF-01 giữ mã IF của P10, không cấp DC. Cơ chế kiến trúc tích hợp: ghi nhật ký (DC-OnlinePaymentManager ghi kết quả mỗi lần gọi, không ghi dữ liệu thẻ), bảo mật (HTTPS, thông tin xác thực với cổng nằm trong cấu hình ngoài mã nguồn, không lưu dữ liệu thẻ, NFR-01), cấu hình (địa chỉ cổng, timeout đọc từ cấu hình của nền tảng Spring Boot).

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-01 OnlinePayment | PKG-31 ValueTypes (DC-Money, DC-TicketCode, DC-PaymentTransactionCode) | Vào package | Chữ ký IF-01 dùng kiểu tiền, mã vé, mã giao dịch; PKG-31 nằm ở layer thấp nhất nên Services không kéo layer dưới phụ thuộc layer trên (P10 F4). Không có interface của subsystem khác phù hợp | Dùng thận trọng |

Phụ thuộc của client vào interface của subsystem (trang Phụ thuộc):

| Client (PKG) | IF | Nguồn |
|---|---|---|
| PKG-16 TripManagement (DC-CancelTripService) | IF-01 | UC-017; P10 F5, P09 QT-6 |
| PKG-13 Booking (dự kiến DC-PayTicketOnlineService) | IF-01 | UC-010 chưa có P07; P10 F5 |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| refundTicket | Cổng từ chối hoàn tiền | Nghiệp vụ | Phản hồi của cổng báo từ chối | Không thử lại; ghi nhật ký (mã vé, trạng thái, loại lỗi) | RefundResult(NotRefunded, Declined) | UC-017 12a | ASM-33, Q-50 |
| refundTicket | Không thiết lập được kết nối, yêu cầu chưa tới cổng | Kỹ thuật tạm thời | Từ chối kết nối, quá 5 giây, lỗi phân giải tên | Không thử lại trong subsystem: thử hoàn lại vé chưa hoàn là quyết định của nơi gọi theo Q-50 và phải giữ NFR-05 (Thiết kế: số lần thử lại trong subsystem bằng 0); ghi nhật ký | RefundResult(NotRefunded, Unavailable) | UC-017 12a | ASM-33, Q-50 |
| refundTicket | Đã gửi nhưng quá 30 giây không có phản hồi | Không rõ kết quả | Hết thời gian chờ đọc | Không thử lại (operation không idempotent có tác dụng phụ tài chính, NFR-05); không tra cứu trạng thái vì chưa biết cổng có hỗ trợ (ASM-51); ghi nhật ký kèm khoá idempotency để đối soát thủ công | RefundResult(NotRefunded, OutcomeUnknown) | UC-017 12a ("không trả kết quả"); P04 chưa tách khỏi "báo không thành công" | ASM-33, Q-50, Q-69, ASM-51 |
| refundTicket | Phản hồi không đọc được hoặc mã phản hồi ngoài các giá trị đã biết | Không rõ kết quả | DC-PaymentMessageConverter không phân loại được | Như dòng trước | RefundResult(NotRefunded, OutcomeUnknown) | UC-017 12a | Q-69, ASM-51 |
| refundTicket | Tham số vi phạm ràng buộc (mã rỗng, số tiền không dương) | Lỗi lập trình | Kiểm tra tiền điều kiện ở DC-OnlinePaymentManager | Không gọi cổng | IllegalArgumentException | Không có (không phải luồng nghiệp vụ) | - |

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | SS-01: DC-OnlinePaymentManager hiện thực IF-01 (trang Phần tử, cạnh E1; trang Phụ thuộc, cạnh D3) |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt | SS-01 không dùng interface của subsystem khác; chỉ phụ thuộc package PKG-31 (F6) |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Public chỉ có kiểu kết quả và kiểu phân loại lỗi trong chữ ký IF-01 (F5) |
| Mỗi operation có sơ đồ hộp trắng, hoặc hiện thực 1-1 bởi một lớp duy nhất | Đạt | 1 operation (refundTicket) đều có trang Hộp trắng; không dùng ngoại lệ ánh xạ 1-1 |

## SS-02 SmsNotification

### F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-009 Đặt vé trực tuyến | DC-BookTicketOnlineService (AC-C-BookTicketOnlineController) | SD1c: 3.1.9 // sendTicketCodesBySms (số điện thoại người đi, mã vé) và 3.1.9 (trả về) kết quả gửi SMS; bước 10, 11 | Vào: số điện thoại người đi, mã các vé vừa phát hành. Ra: kết quả của lời gọi gửi SMS | 11a: SMS mã vé không gửi được (Cổng SMS báo lỗi hoặc không trả kết quả); mã vé vẫn hiển thị (ASM-20) |
| UC-017 Huỷ chuyến | DC-CancelTripService (AC-C-CancelTripController) | SD1: 2.1.10 // sendTripCancellationBySms (số điện thoại, tuyến, giờ xuất bến, mã vé) và 2.1.10 (trả về) kết quả gửi SMS; bước 8, 9 (lặp ở bước 10) | Vào: một số điện thoại người đi, tuyến, giờ xuất bến, mã các vé của số điện thoại đó trên chuyến (ASM-30). Ra: kết quả của lời gọi gửi SMS | 9a: Cổng SMS báo lỗi hoặc không trả kết quả cho số điện thoại này (ASM-31) |
| UC-003 Đăng nhập, UC-014 Đổi vé | - | Chờ P07 UC-003, UC-014: SMS mã xác thực và SMS mã vé khi đổi vé (NFR-12) chưa có message nào ở P07 | Chờ P07 | Chờ P04 UC-003, UC-014 |

### F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-02 | ISmsGateway | Cho phép phần ứng dụng yêu cầu gửi một tin nhắn SMS tới một số điện thoại và nhận kết quả của lời gọi mà không biết giao thức của Cổng SMS. Phần SMS mã xác thực: Chờ P07 UC-003 | SS-02 SmsNotification (lớp hiện thực DC-SmsNotificationManager) | DC-BookTicketOnlineService (PKG-13), DC-CancelTripService (PKG-16); dự kiến PKG-12, PKG-15 khi có P07 UC-003, UC-014 (P10 F5) | PKG-22 SmsIntegration (Services) |

Phân tích interface (A2): P10 giữ một interface IF-02 cho Cổng SMS. Hai operation cùng vai trò (gửi một tin tới một số điện thoại), cùng nhóm client là Application, nên giữ một interface; không tách vì không có nhóm client nào chỉ dùng một operation. IF-02 có 2 operation hoạt động và 1 operation chờ P07 UC-003, nằm trong mức hợp lý 1-7. Package PKG-22 thuộc Services, không cao hơn layer của control dùng nó nên realization không đi lên (P09 A5). Cổng SMS là kênh một chiều từ hệ thống tới cổng (NFR-12), nên không có interface chiều ngược.

### F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-02 | ISmsGateway | Cổng SMS (ACT-07) | sendTicketCodes(recipient: PhoneNumber, ticketCodes: List<TicketCode>): SmsSendResult | recipient: PhoneNumber - số điện thoại người đi của lần đặt vé<br>ticketCodes: List<TicketCode> - mã các vé vừa phát hành của lần đặt, có ít nhất 1 mã | SmsSendResult: status (Sent / NotSent), failureKind (Rejected / Unavailable / OutcomeUnknown; rỗng khi status là Sent) | Rejected (Nghiệp vụ: cổng từ chối số điện thoại hoặc nội dung)<br>Unavailable (Kỹ thuật tạm thời: không kết nối được, cổng quá tải hoặc vượt hạn mức)<br>OutcomeUnknown (Không rõ kết quả: quá thời gian chờ sau khi đã gửi, hoặc phản hồi không phân loại được)<br>Cả ba trả bằng SmsSendResult. Tham số vi phạm ràng buộc --> IllegalArgumentException | UC-009 (bước 10, 11; luồng 11a) | Các vé trong ticketCodes đã phát hành; recipient là số điện thoại người đi của lần đặt | Tối đa một yêu cầu gửi tin đã chuyển cho cổng; Sent nghĩa là cổng xác nhận đã nhận gửi; vé và lần đặt không bị đổi dù gửi lỗi (NFR-12) | Đồng bộ | Không (gửi hai lần là hai tin; subsystem không tự thử lại nên không cần khoá, ASM-20) | 10 giây tổng, 3 giây cho kết nối (Thiết kế: lời gọi chặn hành khách giữa lúc phát hành vé và lúc xem mã vé, UC-009 bước 10 đến 12, nên chọn ngắn; NFR-08 không tính thời gian chờ Cổng SMS; chưa có tài liệu API) |
| IF-02 | ISmsGateway | Cổng SMS (ACT-07) | sendTripCancellationNotice(recipient: PhoneNumber, routeName: String, departureTime: LocalDateTime, ticketCodes: List<TicketCode>): SmsSendResult | recipient: PhoneNumber - một số điện thoại người đi của chuyến đã huỷ<br>routeName: String - tên tuyến xe của chuyến, khác rỗng<br>departureTime: LocalDateTime - giờ xuất bến của chuyến, giờ địa phương<br>ticketCodes: List<TicketCode> - mã các vé của số điện thoại đó trên chuyến, có ít nhất 1 mã | SmsSendResult: status (Sent / NotSent), failureKind (Rejected / Unavailable / OutcomeUnknown; rỗng khi status là Sent) | Như sendTicketCodes: Rejected (Nghiệp vụ); Unavailable (Kỹ thuật tạm thời); OutcomeUnknown (Không rõ kết quả); trả bằng SmsSendResult. Tham số vi phạm ràng buộc --> IllegalArgumentException | UC-017 (bước 8, 9; luồng 9a) | Chuyến ở trạng thái Đã huỷ, các vé trong ticketCodes đã Đã huỷ (ASM-29); nơi gọi gọi một lần cho mỗi số điện thoại (ASM-30) | Tối đa một yêu cầu gửi tin đã chuyển cho cổng; chuyến và vé không bị đổi dù gửi lỗi (NFR-12, ASM-31) | Đồng bộ | Không (gửi hai lần là hai tin; subsystem không tự thử lại nên không cần khoá, ASM-31) | 10 giây tổng, 3 giây cho kết nối (Thiết kế: cùng giá trị với sendTicketCodes để cấu hình một chỗ; lời gọi chạy tuần tự từng số điện thoại trong lúc nhân viên điều hành chờ kết quả huỷ chuyến) |
| IF-02 | ISmsGateway | Cổng SMS (ACT-07) | // gửi SMS mã xác thực đăng nhập (NFR-12; P10 F2 Ghi chú): Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 | UC-003 (Chờ P07 UC-003); UC-014 dự kiến dùng lại sendTicketCodes (Chờ P07 UC-014) | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 |

Ánh xạ trách nhiệm của boundary nguồn: // sendTicketCodesBySms --> sendTicketCodes; // sendTripCancellationBySms --> sendTripCancellationNotice (AC-B-SmsGateway, P08 F3). Hai operation tách vì mỗi UC cần dữ liệu khác nhau (UC-017 thêm tuyến, giờ xuất bến) và nội dung tin khác nhau.

Kiểm tra layer của chữ ký: PhoneNumber, TicketCode nằm ở PKG-31 ValueTypes (Domain); SmsSendResult nằm cùng package với IF-02 (PKG-22); String, LocalDateTime, List là kiểu chuẩn của Java 17. Tuyến xe truyền bằng tên (String) để PKG-22 không phụ thuộc DC-Trip ở PKG-27 (P10 F4 chỉ cho PKG-22 phụ thuộc PKG-31).

### F4. Sequence diagram

File diagrams/P11b-subsystem-SS-02.drawio gồm 6 trang. Bảng Node, bảng message là nguồn chuẩn (C7.1). STT đánh số phẳng theo trục thời gian trong mỗi trang. Message ở mức thiết kế ghi chữ ký kèm đối số; client chỉ gọi interface. Ở trang Phần tử, toạ độ x, y của lớp nằm trong khung subsystem là toạ độ tương đối so với khung.

#### Trang "Hộp đen - UC-009 sendTicketCodes"

Bảng Node:

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S2BB1-L1 | Lifeline | :DC-BookTicketOnlineService | - | - | Control của UC-009 (AC-C-BookTicketOnlineController) | 40 | 40 | 120 | 260 |
| S2BB1-L2 | Lifeline | :IF-02 ISmsGateway | «interface» | - | Interface do SS-02 SmsNotification cung cấp | 200 | 40 | 120 | 260 |
| S2BB1-F2 | Fragment | alt [cổng xác nhận đã nhận tin (bước 11)] | - | - | Toán tử alt | 60 | 130 | 240 | 90 |
| S2BB1-F2-O2 | Fragment | [không gửi được (11a)] | - | S2BB1-F2 | Toán hạng 2, nhãn đặt ngay trên đường ngăn S2BB1-F2-O2-SEP; các message dưới đường ngăn thuộc toán hạng này | 70 | 160 | 220 | 20 |

Bảng message:

| STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | S2BB1-L1 | S2BB1-L2 | sendTicketCodes(recipient, ticketCodes) | Đồng bộ | - | UC-009 bước 10 |
| 2 | S2BB1-L2 | S2BB1-L1 | SmsSendResult(status = Sent) | Trả về | S2BB1-F2 | UC-009 bước 11 |
| 3 | S2BB1-L2 | S2BB1-L1 | SmsSendResult(status = NotSent, failureKind) | Trả về | S2BB1-F2-O2 | UC-009 luồng 11a |

#### Trang "Hộp đen - UC-017 sendTripCancellationNotice"

Bảng Node:

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S2BB2-L1 | Lifeline | :DC-CancelTripService | - | - | Control của UC-017 (AC-C-CancelTripController) | 40 | 40 | 120 | 260 |
| S2BB2-L2 | Lifeline | :IF-02 ISmsGateway | «interface» | - | Interface do SS-02 SmsNotification cung cấp | 200 | 40 | 120 | 260 |
| S2BB2-F1 | Fragment | loop [mỗi số điện thoại người đi của chuyến (bước 10)] | - | - | Toán tử loop | 50 | 80 | 260 | 150 |
| S2BB2-F2 | Fragment | alt [cổng xác nhận đã nhận tin (bước 9)] | - | - | Toán tử alt | 60 | 130 | 240 | 90 |
| S2BB2-F2-O2 | Fragment | [không gửi được (9a)] | - | S2BB2-F2 | Toán hạng 2, nhãn đặt ngay trên đường ngăn S2BB2-F2-O2-SEP; các message dưới đường ngăn thuộc toán hạng này | 70 | 160 | 220 | 20 |

Bảng message:

| STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | S2BB2-L1 | S2BB2-L2 | sendTripCancellationNotice(recipient, routeName, departureTime, ticketCodes) | Đồng bộ | S2BB2-F1 | UC-017 bước 8 |
| 2 | S2BB2-L2 | S2BB2-L1 | SmsSendResult(status = Sent) | Trả về | S2BB2-F2 | UC-017 bước 9 |
| 3 | S2BB2-L2 | S2BB2-L1 | SmsSendResult(status = NotSent, failureKind) | Trả về | S2BB2-F2-O2 | UC-017 luồng 9a |

#### Trang "Hộp trắng - sendTicketCodes"

Bảng Node:

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S2WB1-F | Fragment | sd sendTicketCodes | sd | - | Khung sd của operation | 40 | 0 | 800 | 760 |
| S2WB1-L1 | Lifeline | :DC-SmsNotificationManager | - | S2WB1-F | Lớp điều phối, hiện thực IF-02 | 200 | 40 | 120 | 700 |
| S2WB1-L2 | Lifeline | :DC-SmsMessageConverter | - | S2WB1-F | Chuyển đổi dữ liệu | 360 | 40 | 120 | 700 |
| S2WB1-L3 | Lifeline | :DC-SmsGatewayAdapter | - | S2WB1-F | Giao tiếp ngoài (HTTPS, REST) | 520 | 40 | 120 | 700 |
| S2WB1-L4 | Actor | ACT-07 Cổng SMS | - | S2WB1-F | Hệ thống ngoài (tác nhân phụ của UC-009, UC-017) | 680 | 40 | 120 | 700 |
| S2WB1-F1 | Fragment | alt [kết nối được và cổng phản hồi trong 10 giây] | - | S2WB1-F | Toán tử alt | 220 | 250 | 560 | 250 |
| S2WB1-F1-O2 | Fragment | [không thiết lập được kết nối trong 3 giây, yêu cầu chưa tới cổng] | - | S2WB1-F1 | Toán hạng 2, nhãn đặt ngay trên đường ngăn S2WB1-F1-O2-SEP; các message dưới đường ngăn thuộc toán hạng này | 230 | 360 | 360 | 20 |
| S2WB1-F1-O3 | Fragment | [đã gửi, quá 10 giây không có phản hồi (kết quả không rõ)] | - | S2WB1-F1 | Toán hạng 3, nhãn đặt ngay trên đường ngăn S2WB1-F1-O3-SEP; các message dưới đường ngăn thuộc toán hạng này | 230 | 400 | 360 | 20 |
| S2WB1-F-G1 | Gate | sendTicketCodes | - | S2WB1-F | Gate nhận message 1; tên gate là tên message đi qua | 35 | 115 | 10 | 10 |
| S2WB1-F-G14 | Gate | SmsSendResult | - | S2WB1-F | Gate trả message 14 ra ngoài khung; tên gate là tên message đi qua | 35 | 635 | 10 | 10 |

Bảng message:

| STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | S2WB1-F-G1 | S2WB1-L1 | sendTicketCodes(recipient, ticketCodes) | Đồng bộ | - | IF-02 sendTicketCodes; UC-009 bước 10 |
| 2 | S2WB1-L1 | S2WB1-L2 | composeTicketCodesRequest(recipient, ticketCodes) | Đồng bộ | - | Dựng yêu cầu của cổng |
| 3 | S2WB1-L2 | S2WB1-L1 | gatewaySmsRequest | Trả về | - | Dựng yêu cầu của cổng |
| 4 | S2WB1-L1 | S2WB1-L3 | call(gatewaySmsRequest, 10 giây) | Đồng bộ | - | Gọi cổng với timeout 10 giây |
| 5 | S2WB1-L3 | S2WB1-L4 | postSms(gatewaySmsRequest) | Đồng bộ | S2WB1-F1 | UC-009 bước 10 |
| 6 | S2WB1-L4 | S2WB1-L3 | gatewaySmsResponse | Trả về | S2WB1-F1 | UC-009 bước 11 |
| 7 | S2WB1-L3 | S2WB1-L1 | CallOutcome(Responded, gatewaySmsResponse) | Trả về | S2WB1-F1 | UC-009 bước 11 |
| 8 | S2WB1-L3 | S2WB1-L1 | CallOutcome(ConnectFailed) | Trả về | S2WB1-F1-O2 | UC-009 luồng 11a (không kết nối) |
| 9 | S2WB1-L3 | S2WB1-L4 | postSms(gatewaySmsRequest) | Đồng bộ | S2WB1-F1-O3 | UC-009 luồng 11a (không trả kết quả) |
| 10 | S2WB1-L3 | S2WB1-L1 | CallOutcome(TimedOut) | Trả về | S2WB1-F1-O3 | UC-009 luồng 11a (không trả kết quả) |
| 11 | S2WB1-L1 | S2WB1-L2 | toSmsSendResult(outcome) | Đồng bộ | - | Phân loại kết quả (F7) |
| 12 | S2WB1-L2 | S2WB1-L1 | SmsSendResult | Trả về | - | Phân loại kết quả (F7) |
| 13 | S2WB1-L1 | S2WB1-L1 | logOutcome(maskedRecipient, status, failureKind) | Tự gọi | - | Cơ chế ghi nhật ký |
| 14 | S2WB1-L1 | S2WB1-F-G14 | SmsSendResult | Trả về | - | UC-009 bước 11 |

#### Trang "Hộp trắng - sendTripCancellationNotice"

Bảng Node:

| ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S2WB2-F | Fragment | sd sendTripCancellationNotice | sd | - | Khung sd của operation | 40 | 0 | 800 | 760 |
| S2WB2-L1 | Lifeline | :DC-SmsNotificationManager | - | S2WB2-F | Lớp điều phối, hiện thực IF-02 | 200 | 40 | 120 | 700 |
| S2WB2-L2 | Lifeline | :DC-SmsMessageConverter | - | S2WB2-F | Chuyển đổi dữ liệu | 360 | 40 | 120 | 700 |
| S2WB2-L3 | Lifeline | :DC-SmsGatewayAdapter | - | S2WB2-F | Giao tiếp ngoài (HTTPS, REST) | 520 | 40 | 120 | 700 |
| S2WB2-L4 | Actor | ACT-07 Cổng SMS | - | S2WB2-F | Hệ thống ngoài (tác nhân phụ của UC-009, UC-017) | 680 | 40 | 120 | 700 |
| S2WB2-F1 | Fragment | alt [kết nối được và cổng phản hồi trong 10 giây] | - | S2WB2-F | Toán tử alt | 220 | 250 | 560 | 250 |
| S2WB2-F1-O2 | Fragment | [không thiết lập được kết nối trong 3 giây, yêu cầu chưa tới cổng] | - | S2WB2-F1 | Toán hạng 2, nhãn đặt ngay trên đường ngăn S2WB2-F1-O2-SEP; các message dưới đường ngăn thuộc toán hạng này | 230 | 360 | 360 | 20 |
| S2WB2-F1-O3 | Fragment | [đã gửi, quá 10 giây không có phản hồi (kết quả không rõ)] | - | S2WB2-F1 | Toán hạng 3, nhãn đặt ngay trên đường ngăn S2WB2-F1-O3-SEP; các message dưới đường ngăn thuộc toán hạng này | 230 | 400 | 360 | 20 |
| S2WB2-F-G1 | Gate | sendTripCancellationNotice | - | S2WB2-F | Gate nhận message 1; tên gate là tên message đi qua | 35 | 115 | 10 | 10 |
| S2WB2-F-G14 | Gate | SmsSendResult | - | S2WB2-F | Gate trả message 14 ra ngoài khung; tên gate là tên message đi qua | 35 | 635 | 10 | 10 |

Bảng message:

| STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|
| 1 | S2WB2-F-G1 | S2WB2-L1 | sendTripCancellationNotice(recipient, routeName, departureTime, ticketCodes) | Đồng bộ | - | IF-02 sendTripCancellationNotice; UC-017 bước 8 |
| 2 | S2WB2-L1 | S2WB2-L2 | composeCancellationRequest(recipient, routeName, departureTime, ticketCodes) | Đồng bộ | - | Dựng yêu cầu của cổng |
| 3 | S2WB2-L2 | S2WB2-L1 | gatewaySmsRequest | Trả về | - | Dựng yêu cầu của cổng |
| 4 | S2WB2-L1 | S2WB2-L3 | call(gatewaySmsRequest, 10 giây) | Đồng bộ | - | Gọi cổng với timeout 10 giây |
| 5 | S2WB2-L3 | S2WB2-L4 | postSms(gatewaySmsRequest) | Đồng bộ | S2WB2-F1 | UC-017 bước 8 |
| 6 | S2WB2-L4 | S2WB2-L3 | gatewaySmsResponse | Trả về | S2WB2-F1 | UC-017 bước 9 |
| 7 | S2WB2-L3 | S2WB2-L1 | CallOutcome(Responded, gatewaySmsResponse) | Trả về | S2WB2-F1 | UC-017 bước 9 |
| 8 | S2WB2-L3 | S2WB2-L1 | CallOutcome(ConnectFailed) | Trả về | S2WB2-F1-O2 | UC-017 luồng 9a (không kết nối) |
| 9 | S2WB2-L3 | S2WB2-L4 | postSms(gatewaySmsRequest) | Đồng bộ | S2WB2-F1-O3 | UC-017 luồng 9a (không trả kết quả) |
| 10 | S2WB2-L3 | S2WB2-L1 | CallOutcome(TimedOut) | Trả về | S2WB2-F1-O3 | UC-017 luồng 9a (không trả kết quả) |
| 11 | S2WB2-L1 | S2WB2-L2 | toSmsSendResult(outcome) | Đồng bộ | - | Phân loại kết quả (F7) |
| 12 | S2WB2-L2 | S2WB2-L1 | SmsSendResult | Trả về | - | Phân loại kết quả (F7) |
| 13 | S2WB2-L1 | S2WB2-L1 | logOutcome(maskedRecipient, status, failureKind) | Tự gọi | - | Cơ chế ghi nhật ký |
| 14 | S2WB2-L1 | S2WB2-F-G14 | SmsSendResult | Trả về | - | UC-017 bước 9 |

#### Trang "Phần tử"

Bảng Node:

| ID | Loại (Class / Interface / Subsystem / Package) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S2EL-IF | Interface | «interface» IF-02 ISmsGateway | «interface» | PKG-22 | public; do DC-SmsNotificationManager hiện thực | 400 | 40 | 240 | 120 |
| S2EL-SS | Subsystem | «subsystem» SS-02 SmsNotification | «subsystem» | PKG-22 | Khung subsystem; mọi lớp bên trong là package-private trừ kiểu dữ liệu trong chữ ký | 40 | 200 | 960 | 340 |
| S2EL-CONV | Class | DC-SmsMessageConverter | - | SS-02 | Chuyển đổi dữ liệu | 40 | 60 | 240 | 80 |
| S2EL-MGR | Class | DC-SmsNotificationManager | - | SS-02 | Điều phối; hiện thực IF-02 | 360 | 60 | 240 | 80 |
| S2EL-ADP | Class | DC-SmsGatewayAdapter | - | SS-02 | Giao tiếp ngoài | 680 | 60 | 240 | 80 |
| S2EL-RES | Class | DC-SmsSendResult | - | SS-02 | Kiểu dữ liệu, public (chữ ký IF-02) | 40 | 220 | 240 | 80 |
| S2EL-FK | Class | «enumeration» DC-SmsFailureKind | «enumeration» | SS-02 | Kiểu dữ liệu, public (chữ ký IF-02) | 360 | 220 | 240 | 80 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| S2EL-E1 | S2EL-MGR | S2EL-IF | Realization | - | Lớp điều phối hiện thực IF-02; đồng thời là realization của SS-02 | - |
| S2EL-E2 | S2EL-MGR | S2EL-CONV | Dependency | - | Điều phối gọi chuyển đổi | - |
| S2EL-E3 | S2EL-MGR | S2EL-ADP | Dependency | - | Điều phối gọi lớp giao tiếp | - |
| S2EL-E4 | S2EL-CONV | S2EL-RES | Dependency | «create» | Chuyển đổi tạo kết quả | - |
| S2EL-E5 | S2EL-RES | S2EL-FK | Association | 1 - 0..1 | failureKind có giá trị khi status là kết quả lỗi | - |

#### Trang "Phụ thuộc"

Bảng Node:

| ID | Loại (Class / Interface / Subsystem / Package) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| S2DP-IF | Interface | «interface» IF-02 ISmsGateway | «interface» | PKG-22 | public | 160 | 200 | 240 | 60 |
| S2DP-SS | Subsystem | «subsystem» SS-02 SmsNotification | «subsystem» | PKG-22 | Hiện thực IF-02 | 160 | 360 | 240 | 60 |
| S2DP-VT | Package | PKG-31 ValueTypes | - | PKG-04 | Kiểu giá trị trong chữ ký IF-02 | 520 | 360 | 240 | 60 |
| S2DP-C1 | Package | PKG-13 Booking | - | PKG-02 | Client của sendTicketCodes (UC-009) | 40 | 40 | 200 | 60 |
| S2DP-C2 | Package | PKG-16 TripManagement | - | PKG-02 | Client của sendTripCancellationNotice (UC-017) | 320 | 40 | 200 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| S2DP-D3 | S2DP-SS | S2DP-IF | Realization | - | Subsystem hiện thực interface | - |
| S2DP-D4 | S2DP-SS | S2DP-VT | Dependency | - | Vào package, dùng thận trọng (F6) | - |
| S2DP-D1 | S2DP-C1 | S2DP-IF | Dependency | - | Client phụ thuộc interface | (140,150); (220,150) |
| S2DP-D2 | S2DP-C2 | S2DP-IF | Dependency | - | Client phụ thuộc interface | (420,150); (340,150) |

### F5. Phần tử của subsystem

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-SmsNotificationManager | SmsNotificationManager | Điều phối | Nhận sendTicketCodes, sendTripCancellationNotice; kiểm tra tham số; nhờ DC-SmsMessageConverter dựng yêu cầu và phân loại kết quả; nhờ DC-SmsGatewayAdapter gọi cổng; ghi nhật ký kết quả với số điện thoại đã che bớt chữ số (P09 F7: giảm thiểu dữ liệu cá nhân); không để ngoại lệ giao thức lọt ra khỏi subsystem | package-private | IF-02 |
| DC-SmsGatewayAdapter | SmsGatewayAdapter | Giao tiếp ngoài | Gọi API REST của Cổng SMS qua HTTPS; áp timeout kết nối 3 giây và tổng 10 giây; không thử lại; trả kết quả lời gọi thô (Responded / ConnectFailed / TimedOut); giữ địa chỉ và thông tin xác thực với cổng từ cấu hình ngoài mã nguồn | package-private | - |
| DC-SmsMessageConverter | SmsMessageConverter | Chuyển đổi dữ liệu | Dựng nội dung tin từ mẫu nằm trong cấu hình (mã vé; tuyến, giờ xuất bến định dạng dd/MM/yyyy HH:mm, P04 UC-017 Dữ liệu ra 2) và chuyển thành yêu cầu REST của cổng; chuyển phản hồi hoặc kết quả lời gọi thành SmsSendResult; phản hồi không đọc được --> OutcomeUnknown; bảng ánh xạ mã phản hồi của cổng để trống tới khi có tài liệu API | package-private | - |
| DC-SmsSendResult | SmsSendResult | Kiểu dữ liệu | Kết quả của sendTicketCodes, sendTripCancellationNotice: status, failureKind; xuất hiện trong chữ ký IF-02 | public | - |
| DC-SmsFailureKind | SmsFailureKind | Kiểu dữ liệu | Phân loại lỗi gửi tin: Rejected, Unavailable, OutcomeUnknown; xuất hiện trong chữ ký IF-02 qua SmsSendResult | public | - |

Mã DC cấp theo C3; P12 thiết kế chi tiết thuộc tính, phương thức. IF-02 giữ mã IF của P10, không cấp DC. Cơ chế kiến trúc tích hợp: ghi nhật ký (kết quả mỗi lần gọi, số điện thoại che bớt), bảo mật (HTTPS, thông tin xác thực với cổng nằm trong cấu hình ngoài mã nguồn, số điện thoại và mã vé truyền qua HTTPS theo P09 F7), cấu hình (địa chỉ cổng, timeout, mẫu nội dung tin đọc từ cấu hình của nền tảng Spring Boot).

### F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-02 SmsNotification | PKG-31 ValueTypes (DC-PhoneNumber, DC-TicketCode) | Vào package | Chữ ký IF-02 dùng kiểu số điện thoại, mã vé; PKG-31 nằm ở layer thấp nhất (P10 F4). Không có interface của subsystem khác phù hợp | Dùng thận trọng |

Phụ thuộc của client vào interface của subsystem (trang Phụ thuộc):

| Client (PKG) | IF | Nguồn |
|---|---|---|
| PKG-13 Booking (DC-BookTicketOnlineService) | IF-02 | UC-009; P10 F5, P09 QT-6 |
| PKG-16 TripManagement (DC-CancelTripService) | IF-02 | UC-017; P10 F5, P09 QT-6 |

### F7. Thiết kế xử lý lỗi và điểm kiểm tra

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| sendTicketCodes, sendTripCancellationNotice | Cổng từ chối số điện thoại hoặc nội dung | Nghiệp vụ | Phản hồi của cổng báo từ chối | Không thử lại; ghi nhật ký (số điện thoại đã che, trạng thái, loại lỗi) | SmsSendResult(NotSent, Rejected) | UC-009 11a; UC-017 9a | ASM-20, ASM-31 |
| sendTicketCodes, sendTripCancellationNotice | Không thiết lập được kết nối, cổng quá tải hoặc vượt hạn mức | Kỹ thuật tạm thời | Từ chối kết nối, quá 3 giây, mã phản hồi quá tải | Không thử lại (ASM-20, ASM-31 chọn ghi nhận rồi tiếp tục; thử gửi lại chờ Q-35, Q-49) (Thiết kế: số lần thử lại trong subsystem bằng 0); ghi nhật ký | SmsSendResult(NotSent, Unavailable) | UC-009 11a; UC-017 9a | Q-35, Q-49, ASM-20, ASM-31 |
| sendTicketCodes, sendTripCancellationNotice | Đã gửi nhưng quá 10 giây không có phản hồi | Không rõ kết quả | Hết thời gian chờ đọc | Không thử lại; tin có thể đã được gửi, P04 coi là chưa gửi được nên chấp nhận khả năng người nhận có thể nhận tin dù hệ thống ghi chưa gửi được; ghi nhật ký | SmsSendResult(NotSent, OutcomeUnknown) | UC-009 11a ("không trả kết quả"); UC-017 9a | Q-35, Q-49, ASM-20, ASM-31 |
| sendTicketCodes, sendTripCancellationNotice | Phản hồi không đọc được hoặc mã phản hồi ngoài các giá trị đã biết | Không rõ kết quả | DC-SmsMessageConverter không phân loại được | Như dòng trước | SmsSendResult(NotSent, OutcomeUnknown) | UC-009 11a; UC-017 9a | Q-35, Q-49 |
| sendTicketCodes, sendTripCancellationNotice | Tham số vi phạm ràng buộc (danh sách mã vé rỗng, tên tuyến rỗng) | Lỗi lập trình | Kiểm tra tiền điều kiện ở DC-SmsNotificationManager | Không gọi cổng | IllegalArgumentException | Không có (không phải luồng nghiệp vụ) | - |

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | SS-02: DC-SmsNotificationManager hiện thực IF-02 (trang Phần tử, cạnh E1; trang Phụ thuộc, cạnh D3) |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt | SS-02 không dùng interface của subsystem khác; chỉ phụ thuộc package PKG-31 (F6) |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Public chỉ có kiểu kết quả và kiểu phân loại lỗi trong chữ ký IF-02 (F5) |
| Mỗi operation có sơ đồ hộp trắng, hoặc hiện thực 1-1 bởi một lớp duy nhất | Đạt | 2 operation (sendTicketCodes, sendTripCancellationNotice) đều có trang Hộp trắng; không dùng ngoại lệ ánh xạ 1-1 |

## F8. Tổng hợp toàn hệ thống

| SS | IF | Số operation | UC dùng | Rủi ro chính |
|---|---|---|---|---|
| SS-01 OnlinePayment | IF-01 IPaymentGateway | 1 (thêm 1 chờ P07 UC-010) | UC-017 (UC-009, UC-010, UC-014 chờ P07) | API chưa có tài liệu; hoàn tiền quá thời gian chờ là kết quả không rõ, nơi gọi tự hoàn lại có thể hoàn trùng (NFR-05) khi chưa biết cổng có chống trùng hay tra cứu được (Q-69); UC-017 gọi tuần tự từng vé, mỗi vé tối đa 30 giây |
| SS-02 SmsNotification | IF-02 ISmsGateway | 2 (thêm 1 chờ P07 UC-003) | UC-009, UC-017 (UC-003, UC-014 chờ P07) | API chưa có tài liệu; UC-009 gọi đồng bộ nên hành khách chờ tối đa 10 giây trước khi xem mã vé; tin có thể đã gửi nhưng bị coi là chưa gửi được khi quá thời gian chờ; UC-017 gọi tuần tự từng số điện thoại |

Mục kiểm soát theo C5 nằm ngay dưới đây.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-69 | Cổng thanh toán của đối tác có hỗ trợ (a) khoá idempotency cho yêu cầu hoàn tiền và (b) tra cứu trạng thái một yêu cầu hoàn tiền đã gửi không? (Hỗ trợ cả hai / Chỉ hỗ trợ một trong hai / Không hỗ trợ) | SS-01 IF-01 refundTicket (cột Idempotent, F7), khả năng thêm operation tra cứu trạng thái hoàn tiền; UC-017 luồng 12a; NFR-05; liên quan Q-50, Q-20 | project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API"; P04 UC-017 luồng 12a gộp "báo không thành công" và "không trả kết quả" nên không phân biệt được hoàn tiền bị từ chối với hoàn tiền chưa rõ kết quả |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-51 | Cổng thanh toán không được giả định hỗ trợ khoá idempotency và tra cứu trạng thái hoàn tiền: SS-01 coi refundTicket là không idempotent, không tự thử lại, không có operation tra cứu trạng thái; kết quả không rõ (quá thời gian chờ sau khi đã gửi, hoặc phản hồi không phân loại được) trả RefundResult(NotRefunded, OutcomeUnknown) để nơi gọi phân biệt với từ chối nghiệp vụ. | Chờ Q-69. Hồ sơ dự án ghi chưa có tài liệu API; chọn phương án an toàn nhất cho NFR-05 (mỗi vé được yêu cầu hoàn đúng một lần) khi không biết cổng có chống trùng | IF-01 refundTicket; F7 SS-01 dòng 3, 4; DC-PaymentMessageConverter, DC-RefundFailureKind |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-017 (luồng 12a) | Luồng 12a gộp "báo không thành công" và "không trả kết quả". Với hoàn tiền, không trả kết quả là kết quả không rõ: cổng có thể đã hoàn tiền, nên hoàn lại vé đó có nguy cơ hoàn hai lần (NFR-05). ASM-33 chỉ giữ trạng thái "Chưa hoàn" | Tách trường hợp không rõ kết quả khỏi trường hợp cổng từ chối; nêu vé ở trạng thái không rõ kết quả không được hoàn lại trước khi đối soát với cổng (theo câu trả lời Q-50, Q-69) |
| P10 | F4 (PKG-21, PKG-22), F5 | Chữ ký IF-01, IF-02 dùng kiểu kết quả và kiểu phân loại lỗi (DC-RefundResult, DC-RefundFailureKind, DC-SmsSendResult, DC-SmsFailureKind) do subsystem định nghĩa; F5 ghi mọi phần tử trong PKG-21, PKG-22 là package-private và cột Được dùng bởi chỉ có IF | Thêm bốn kiểu này vào cột Phần tử chứa của PKG-21, PKG-22 ở F4 và vào F5 với visibility public, được dùng bởi PKG-13, PKG-16 (PKG-12, PKG-15 dự kiến) |
| P04, P07 | UC-010, UC-003, UC-014 (thu tiền qua cổng, SMS mã xác thực, SMS mã vé khi đổi vé) | Các use case này dùng IF-01, IF-02 nhưng chưa có P04, P07 nên P11b chưa định nghĩa chữ ký (A1) | Chạy P04, P07 cho các use case này, rồi P08, P10 và chạy lại P11b cho SS-01, SS-02 |

## Vấn đề còn mở

- Độ phủ: chỉ UC-009 và UC-017 có P04, P07 nên mỗi subsystem chỉ có operation của hai use case này. Thu tiền vé (IF-01), SMS mã xác thực (IF-02) ở trạng thái "Chờ P07" (F3). Target 1 và Target 2 đạt cho phạm vi hai use case.
- Máy in vé nhiệt (ACT-08) và máy soát vé chưa là subsystem (P10 F1), nên chưa có interface chiều ngược cho thiết bị đẩy sự kiện; Target 9 chưa áp dụng. Khi P07 của UC-004, UC-006, UC-015, UC-025, UC-026 có và P10 tạo subsystem, chạy lại P11b.
- TAI_LIEU_GIAO_TIEP = Không có: phần ánh xạ lời gọi ngoài (đường dẫn, định dạng thông điệp, bảng mã phản hồi, hạn mức tốc độ) để trống trong DC-PaymentMessageConverter, DC-SmsMessageConverter. Khi có tài liệu, chạy lại chỉ để bổ sung bên trong subsystem, interface không đổi trừ khi Q-69 có câu trả lời thêm operation tra cứu.
- ASM-37 (P10 F2 SS-01, "coi không có phản hồi là không thành công") áp dụng cho lời gọi thu tiền; P11b thiết kế hoàn tiền theo ASM-33 và tách OutcomeUnknown. Khi có P07 UC-010, xét kết quả không rõ của thu tiền theo Q-53 và Q-69.
- Mẫu nội dung tin SMS (lời văn, ngôn ngữ, giới hạn độ dài khi một số điện thoại có nhiều mã vé) nằm trong cấu hình của DC-SmsMessageConverter. Nguồn chỉ nêu nội dung tối thiểu (ASM-30; P04 UC-017 Dữ liệu ra 2), lời văn cụ thể chưa chốt.
- UC-017 gọi cổng tuần tự: mỗi số điện thoại tối đa 10 giây, mỗi vé hoàn tiền tối đa 30 giây. Chuyến nhiều vé có thể chạy lâu; việc chạy nền hay đồng bộ với nhân viên điều hành do P12 và X1 xét, hiện không có NFR thời gian cho UC-017.
- Lựa chọn khi hai quy tắc xung đột: C7.3 yêu cầu toạ độ bội số của 10, trong khi gate 10 x 10 phải có tâm trên cạnh khung sd và message ở y bội số của 10; gate đặt với x, y lệch 5 đơn vị so với bội số của 10 (x = 35, y = y message - 5). Các node khác đều là bội số của 10.
- Lựa chọn khi hai quy tắc xung đột: khoảng cách hai message cố định 40 nên nhãn toán hạng thứ hai trở đi của alt đặt ngay trên đường ngăn, thay vì dưới đường ngăn, để không đè nhãn message. Message của toán hạng nằm dưới đường ngăn.
- File .drawio sinh bằng chương trình từ cùng dữ liệu với các bảng ở F4 và đã kiểm tự động (XML hợp lệ, toạ độ bội số của 10 trừ gate, khoảng cách tối thiểu 40 giữa các node cùng cấp, không trùng ID). Chưa mở bằng draw.io để xem bằng mắt. Ở các trang Hộp trắng, message từ lớp điều phối tới lớp giao tiếp đi qua đường lifeline của lớp chuyển đổi dữ liệu, và message vào ra qua gate đi qua lifeline của lớp điều phối; các đường này không đè lên hộp lifeline nhưng cắt đường nét đứt của lifeline.
