# P07 - Phân tích use case UC-007 Huỷ đơn hàng - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; P01 1.0; P02 1.0; P03 1.0; P04-uc-specs/UC-007-cancel-order.md 1.0; P04-uc-specs/_BR-register.md; P07-uc-analysis/UC-004-place-order-analysis.md 1.0. Không có P05, P06 |
| Phạm vi | UC-007 |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-007 Huỷ đơn hàng |
| Tác nhân chính | ACT-01 Khách hàng (Người) |
| Tác nhân phụ | ACT-03 Liên ngân hàng (Hệ thống ngoài) |
| Include | Không có |
| Được include bởi | Không có |
| Extend | Không có |
| Được extend bởi | Không có |
| File P07 đã có được dùng làm sổ đăng ký AC | UC-004-place-order-analysis.md (AC-B-PlaceOrderForm, AC-C-PlaceOrderController, AC-E-Cart, AC-E-Media, AC-E-DeliveryInfo, AC-E-Invoice, AC-C-PlaceRushOrderController tạm, AC-C-PayOrderController tạm) |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Khách hàng | Yêu cầu huỷ một đơn hàng đã thanh toán. | Không đổi | REQ-90 |
| 2 | Hệ thống | Yêu cầu Liên ngân hàng cộng toàn bộ số tiền đã thanh toán của đơn hàng vào thẻ tín dụng đã dùng. | Hệ thống lấy số tiền đã thanh toán của đơn hàng và thông tin thẻ đã dùng để thanh toán đơn đó, rồi gửi yêu cầu cộng tiền tới Liên ngân hàng (API cộng tiền). | BR-12, REQ-91, REQ-99 |
| 3 | Liên ngân hàng | Trả về kết quả hoàn tiền. | Không đổi | REQ-99 |
| 3a | Hệ thống | Giữ nguyên trạng thái đơn hàng. | Hệ thống kết thúc yêu cầu huỷ, không đổi trạng thái đơn hàng; cách báo cho khách hàng chờ Q-21. | Q-21 |
| 4 | Hệ thống | Ghi nhận đơn hàng đã bị huỷ. | Hệ thống chuyển trạng thái của đơn hàng sang đã huỷ (tên trạng thái chờ Q-18). | REQ-90, Q-18 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng | Lý do |
|---|---|---|---|---|---|
| ACT-01 Khách hàng | Người | CancelOrderForm | Giao diện người dùng | Mới | Một boundary cho cặp Khách hàng - UC-007 |
| ACT-03 Liên ngân hàng | Hệ thống ngoài | InterbankBoundary | Giao diện hệ thống | Mới | Chưa có trong sổ AC; UC-006 khi phân tích phải tái dùng mã này |

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | khách hàng | Bước 1 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01 |
| 2 | Liên ngân hàng | Bước 2, 3 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-03 |
| 3 | hệ thống | Bước 2, 4 | Loại - mơ hồ | Chính hệ thống |
| 4 | đơn hàng | Bước 1, 2, 4 | Entity (AC-E-Order) | Được lưu sau thanh toán (REQ-80), có trạng thái (REQ-82) |
| 5 | số tiền đã thanh toán | Bước 2 | Loại - thuộc tính của Order | Tổng số tiền của đơn |
| 6 | thẻ tín dụng đã dùng | Bước 2, BR-12 | Entity (AC-E-Card) | Thông tin thẻ được lưu (REQ-44, REQ-46) và dùng lại để hoàn tiền |
| 7 | kết quả hoàn tiền | Bước 3 | Loại - thao tác hoặc sự kiện | Kết quả của lời gọi |
| 8 | trạng thái đơn hàng | Bước 3a, 4 | Loại - thuộc tính của Order | REQ-82 |

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do |
|---|---|---|---|
| CancelOrderController | UC-007 | Mới | Một control cho mỗi use case |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-CancelOrderForm | boundary | CancelOrderForm | // requestToCancelOrder: nhận yêu cầu huỷ đơn hàng | - | 1 | Giao diện người dùng | Mới | - |
| AC-C-CancelOrderController | control | CancelOrderController | // cancelOrder: điều phối hoàn tiền và ghi nhận huỷ<br>// abortCancellation: kết thúc yêu cầu huỷ khi hoàn tiền không thành công | - | 1-4, 3a | - | Mới | - |
| AC-E-Order | entity | Order | // getRefundInfo: cung cấp số tiền đã thanh toán và thẻ đã dùng<br>// markCancelled: chuyển trạng thái sang đã huỷ | totalAmount: Số tiền<br>status: Trạng thái | 2, 4 | - | Mới | - |
| AC-E-Card | entity | Card | // getCardInfo: cung cấp thông tin thẻ để hoàn tiền | cardholderName: Văn bản<br>cardNumber: Văn bản<br>issuingBank: Văn bản<br>expirationDate: Ngày<br>securityCode: Văn bản | 2 | - | Mới | - |
| AC-B-InterbankBoundary | boundary | InterbankBoundary | // refund: yêu cầu Liên ngân hàng cộng tiền vào thẻ | - | 2, 3 | Giao diện hệ thống | Mới | - |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | Nhận yêu cầu huỷ | AC-B-CancelOrderForm | Giao tiếp tác nhân | - |
| 1 | Điều phối huỷ đơn | AC-C-CancelOrderController | Controller | - |
| 2 | Cung cấp số tiền và thẻ đã dùng | AC-E-Order | Information Expert | Order hỏi Card vì đơn gắn với thẻ đã dùng (BR-12) |
| 2 | Gửi yêu cầu cộng tiền | AC-B-InterbankBoundary | Giao tiếp tác nhân | - |
| 3a | Kết thúc yêu cầu huỷ | AC-C-CancelOrderController | Controller | - |
| 4 | Chuyển trạng thái đã huỷ | AC-E-Order | Information Expert | - |

## F5. Sequence diagram phân tích

SD1 - Luồng chính và 3a. File diagrams/P07-sequence-UC-007.drawio.

<!--GEN:SEQ-->
#### Bảng lifeline (Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-ACT-01 | Actor | Khách hàng | - | - | ACT-01 |
| L-FORM | Lifeline | :CancelOrderForm | «boundary» | - | AC-B-CancelOrderForm |
| L-CTRL | Lifeline | :CancelOrderController | «control» | - | AC-C-CancelOrderController |
| L-ORDER | Lifeline | :Order | «entity» | - | AC-E-Order |
| L-CARD | Lifeline | :Card | «entity» | - | AC-E-Card |
| L-IB | Lifeline | :InterbankBoundary | «boundary» | - | AC-B-InterbankBoundary |
| L-ACT-03 | Actor | Liên ngân hàng | «system» | - | ACT-03 |
| F1 | Fragment | alt [hoàn tiền thành công] / [hoàn tiền không thành công] | - | - | - |

#### Bảng message (Edge)

| STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | L-ACT-01 | L-FORM | // requestToCancelOrder (đơn hàng) | Đồng bộ | - | 1 |
| 1.1 | L-FORM | L-CTRL | // cancelOrder (đơn hàng) | Đồng bộ | - | 1 |
| 1.1.1 | L-CTRL | L-ORDER | // getRefundInfo | Đồng bộ | - | 2 |
| 1.1.1.1 | L-ORDER | L-CARD | // getCardInfo | Đồng bộ | - | 2 |
| 1.1.1 (trả về) | L-ORDER | L-CTRL | số tiền đã thanh toán, thẻ đã dùng | Trả về | - | 2 |
| 1.1.2 | L-CTRL | L-IB | // refund (thẻ, số tiền) | Đồng bộ | - | 2 |
| 1.1.2.1 | L-IB | L-ACT-03 | // requestAddFunds (thẻ, số tiền) | Đồng bộ | - | 2 |
| 1.1.2.1 (trả về) | L-ACT-03 | L-IB | kết quả hoàn tiền | Trả về | - | 3 |
| 1.1.2 (trả về) | L-IB | L-CTRL | kết quả hoàn tiền | Trả về | - | 3 |
| 1.1.3 | L-CTRL | L-ORDER | // markCancelled | Đồng bộ | F1 | 4 |
| 1.1.4 | L-CTRL | L-CTRL | // abortCancellation | Tự gọi | F1 | 3a |
<!--/GEN:SEQ-->

## F6. Quy tắc tương tác

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-007.drawio.

<!--GEN:COMM-->
#### Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| L-ACT-01 | Actor | Khách hàng | - | - | - | 40 | 200 | 30 | 60 |
| L-FORM | Object | :CancelOrderForm | «boundary» | - | - | 160 | 200 | 200 | 50 |
| L-CTRL | Object | :CancelOrderController | «control» | - | - | 480 | 200 | 200 | 50 |
| L-IB | Object | :InterbankBoundary | «boundary» | - | - | 800 | 200 | 200 | 50 |
| L-ACT-03 | Actor | Liên ngân hàng | «system» | - | - | 1080 | 200 | 30 | 60 |
| L-ORDER | Object | :Order | «entity» | - | - | 480 | 400 | 200 | 50 |
| L-CARD | Object | :Card | «entity» | - | - | 800 | 400 | 200 | 50 |

#### Bảng Edge (link)

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message |
|---|---|---|---|---|---|
| K-01 | L-ACT-01 | L-FORM | Link | 1: // requestToCancelOrder (-->) | 1: Khách hàng-->CancelOrderForm |
| K-02 | L-CTRL | L-FORM | Link | 1.1: // cancelOrder (<--) | 1.1: CancelOrderForm-->CancelOrderController |
| K-03 | L-CTRL | L-ORDER | Link | 1.1.1: // getRefundInfo (-->)<br>1.1.3: // markCancelled (-->) | 1.1.1: CancelOrderController-->Order<br>1.1.3: CancelOrderController-->Order |
| K-04 | L-CARD | L-ORDER | Link | 1.1.1.1: // getCardInfo (<--) | 1.1.1.1: Order-->Card |
| K-05 | L-CTRL | L-IB | Link | 1.1.2: // refund (-->) | 1.1.2: CancelOrderController-->InterbankBoundary |
| K-06 | L-ACT-03 | L-IB | Link | 1.1.2.1: // requestAddFunds (<--) | 1.1.2.1: InterbankBoundary-->Liên ngân hàng |
| K-07 | L-CTRL | L-CTRL | Link | 1.1.4: // abortCancellation | 1.1.4: tự gọi |

Trong nhãn link, "(-->)" nghĩa là message đi từ Nguồn tới Đích, "(<--)" là chiều ngược lại.
<!--/GEN:COMM-->

## F8. VOPC

File diagrams/P07-class-UC-007.drawio.

<!--GEN:VOPC-->
#### Bảng Node (lớp)

| ID (mã AC) | Loại | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-CancelOrderForm | Class | CancelOrderForm | «boundary» | - | - | // requestToCancelOrder |
| AC-B-InterbankBoundary | Class | InterbankBoundary | «boundary» | - | - | // refund |
| AC-C-CancelOrderController | Class | CancelOrderController | «control» | - | - | // cancelOrder<br>// abortCancellation |
| AC-E-Order | Class | Order | «entity» | - | totalAmount: Số tiền<br>status: Trạng thái | // getRefundInfo<br>// markCancelled |
| AC-E-Card | Class | Card | «entity» | - | cardholderName: Văn bản<br>cardNumber: Văn bản<br>issuingBank: Văn bản<br>expirationDate: Ngày<br>securityCode: Văn bản | // getCardInfo |

#### Bảng quan hệ (Edge)

| ID | Lớp A | Lớp B | Loại | Multiplicity (A..B) | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC007-01 | AC-B-CancelOrderForm | AC-C-CancelOrderController | Association | - | - | Link K-02 (1.1); tạm thời |
| R-UC007-02 | AC-C-CancelOrderController | AC-E-Order | Association | - | - | Link K-03 (1.1.1, 1.1.3); tạm thời |
| R-UC007-03 | AC-E-Order | AC-E-Card | Association | Chưa xác định (Q-23) | paymentCard | Link K-04 (1.1.1.1); BR-12 "thẻ tín dụng đã dùng để thanh toán đơn hàng" |
| R-UC007-04 | AC-C-CancelOrderController | AC-B-InterbankBoundary | Association | - | - | Link K-05 (1.1.2); tạm thời |
<!--/GEN:VOPC-->

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1, 1.1 | AC-B-CancelOrderForm, AC-C-CancelOrderController |
| 2 | 1.1.1, 1.1.1.1, 1.1.2, 1.1.2.1 | AC-C-CancelOrderController, AC-E-Order, AC-E-Card, AC-B-InterbankBoundary |
| 3 | 1.1.2.1 (trả về), 1.1.2 (trả về) | AC-B-InterbankBoundary, AC-C-CancelOrderController |
| 3a | 1.1.4 | AC-C-CancelOrderController |
| 4 | 1.1.3 | AC-C-CancelOrderController, AC-E-Order |

## Câu hỏi mở

Không có câu hỏi mới. Liên quan: Q-18, Q-21, Q-23.

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Số lớp của use case là 5, trong khoảng 4-12.
- AC-E-Card chỉ có trách nhiệm cung cấp dữ liệu (entity thiếu trách nhiệm hành vi); đặc tả UC-007 không có hành vi nào khác trên dữ liệu thẻ.
- Luồng 3a không có message tới boundary của khách hàng vì cách thông báo chờ Q-21; bước này được thể hiện bằng message tự gọi của control.
- Không có P05 nên chưa kiểm tra được "đơn hàng" (Order) ở đây và "đơn hàng tạm thời" (Invoice) ở UC-004 có phải một khái niệm; để P08 xét.
