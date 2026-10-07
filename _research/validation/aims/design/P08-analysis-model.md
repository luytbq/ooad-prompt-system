# P08 - Mô hình phân tích hợp nhất - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P08 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; P01 1.0; P02 1.0; P04-uc-specs (UC-004, UC-007, sổ BR); P07-uc-analysis/UC-004-place-order-analysis.md 1.0; P07-uc-analysis/UC-007-cancel-order-analysis.md 1.0. Không có P05, P06 |
| Phạm vi | Toàn hệ thống (phần đã phân tích: UC-004, UC-007) |

## F1. Độ phủ use case

| UC | Tên | File P07 | Trạng thái |
|---|---|---|---|
| UC-001 | Tìm kiếm sản phẩm | - | Chưa phân tích |
| UC-002 | Thêm sản phẩm vào giỏ hàng | - | Chưa phân tích |
| UC-003 | Xem giỏ hàng | - | Chưa phân tích |
| UC-004 | Đặt hàng | P07-uc-analysis/UC-004-place-order-analysis.md | Đã phân tích |
| UC-005 | Đặt hàng giao nhanh | - | Chưa phân tích |
| UC-006 | Thanh toán đơn hàng | - | Chưa phân tích |
| UC-007 | Huỷ đơn hàng | P07-uc-analysis/UC-007-cancel-order-analysis.md | Đã phân tích |
| UC-008 | Xem lịch sử mua hàng | - | Chưa phân tích |
| UC-009 | Quản lý sản phẩm | - | Chưa phân tích |
| UC-010 | Duyệt đơn hàng | - | Chưa phân tích |

## F2. Nhật ký hợp nhất

| STT | Lớp gốc (AC, tên) | UC nguồn | Tình huống | Kết quả | Bằng chứng |
|---|---|---|---|---|---|
| 1 | AC-B-PlaceOrderForm | UC-004 | Giữ nguyên | Giữ | Một boundary cho cặp Khách hàng - UC-004 |
| 2 | AC-C-PlaceOrderController | UC-004 | Giữ nguyên | Giữ | Control của UC-004 |
| 3 | AC-E-Cart | UC-004 | Giữ nguyên | Giữ | REQ-35, REQ-40 |
| 4 | AC-E-Media | UC-004 | Giữ nguyên | Giữ | REQ-16, REQ-23 |
| 5 | AC-E-DeliveryInfo | UC-004 | Giữ nguyên | Giữ | REQ-44, REQ-45; có hành vi riêng (kiểm tra hợp lệ, tính phí) nên không phải thuộc tính trá hình |
| 6 | AC-E-Invoice | UC-004 | Giữ nguyên | Giữ | Xét đồng nghĩa với AC-E-Order (dòng 11): nguồn gọi là "thông tin đơn hàng tạm thời (invoice)" (L156) và sau thanh toán "Đơn hàng sẽ vào trạng thái chờ xử lý" (L170). Phép thử "một đối tượng lớp này luôn là một đối tượng lớp kia" không chứng minh được vì đơn hàng tạm thời có thể không được thanh toán (Q-20). Không có glossary để phân định; Q-24 |
| 7 | AC-C-PlaceRushOrderController | UC-004 (đặt trước cho UC-005) | Giữ nguyên | Giữ | Tạm, chờ P07 của UC-005 |
| 8 | AC-C-PayOrderController | UC-004 (đặt trước cho UC-006) | Giữ nguyên | Giữ | Tạm, chờ P07 của UC-006 |
| 9 | AC-B-CancelOrderForm | UC-007 | Giữ nguyên | Giữ | Một boundary cho cặp Khách hàng - UC-007 |
| 10 | AC-C-CancelOrderController | UC-007 | Giữ nguyên | Giữ | Control của UC-007 |
| 11 | AC-E-Order | UC-007 | Giữ nguyên | Giữ | Xem dòng 6; Q-24 |
| 12 | AC-E-Card | UC-007 | Giữ nguyên | Giữ | REQ-46 có định danh (mã thẻ) và được lưu (REQ-44) |
| 13 | AC-B-InterbankBoundary | UC-007 | Giữ nguyên | Giữ | Boundary hệ thống duy nhất cho ACT-03; UC-006 phải tái dùng |

## F3. Bảng lớp hợp nhất

| AC | Stereotype | Tên | Trách nhiệm (gộp) | Thuộc tính | Dùng trong UC | Loại boundary | Trạng thái |
|---|---|---|---|---|---|---|---|
| AC-B-PlaceOrderForm | boundary | PlaceOrderForm | // requestToPlaceOrder: nhận yêu cầu đặt hàng (UC-004)<br>// submitDeliveryInfo: nhận thông tin giao hàng (UC-004)<br>// displayInsufficientStock: hiển thị sản phẩm thiếu (UC-004)<br>// requestDeliveryInfo: hiển thị thông tin giao hàng mặc định (UC-004)<br>// requestUpdateDeliveryInfo: yêu cầu cập nhật lại (UC-004)<br>// displayInvoice: hiển thị đơn hàng tạm thời (UC-004) | - | UC-004 | Giao diện người dùng | Hoạt động |
| AC-B-CancelOrderForm | boundary | CancelOrderForm | // requestToCancelOrder: nhận yêu cầu huỷ đơn (UC-007) | - | UC-007 | Giao diện người dùng | Hoạt động |
| AC-B-InterbankBoundary | boundary | InterbankBoundary | // refund: yêu cầu cộng tiền vào thẻ (UC-007) | - | UC-007 | Giao diện hệ thống | Hoạt động |
| AC-C-PlaceOrderController | control | PlaceOrderController | // placeOrder: điều phối tới bước nhập thông tin giao hàng (UC-004)<br>// submitDeliveryInfo: điều phối kiểm tra, lưu, tính phí, lập đơn tạm thời, gọi thanh toán (UC-004)<br>// checkRushOrderSelected: xác định chèn UC-005 (UC-004) | - | UC-004 | - | Hoạt động |
| AC-C-PlaceRushOrderController | control | PlaceRushOrderController | // placeRushOrder: điều phối UC-005 (UC-004) | - | UC-004 (UC-005 chưa phân tích) | - | Hoạt động |
| AC-C-PayOrderController | control | PayOrderController | // payOrder: điều phối UC-006 (UC-004) | - | UC-004 (UC-006 chưa phân tích) | - | Hoạt động |
| AC-C-CancelOrderController | control | CancelOrderController | // cancelOrder: điều phối hoàn tiền và ghi nhận huỷ (UC-007)<br>// abortCancellation: kết thúc khi hoàn tiền thất bại (UC-007) | - | UC-007 | - | Hoạt động |
| AC-E-Cart | entity | Cart | // checkMediaAvailability: kiểm tra tồn kho (UC-004)<br>// calculateSubtotal: tính tổng giá (UC-004)<br>// getHeaviestMediaWeight: khối lượng nặng nhất (UC-004) | items: sản phẩm và số lượng | UC-004 | - | Hoạt động |
| AC-E-Media | entity | Media | // checkAvailableQuantity: so số lượng yêu cầu với tồn kho (UC-004) | title: Văn bản<br>price: Số tiền<br>quantity: Số lượng<br>weight: Khối lượng | UC-004 | - | Hoạt động |
| AC-E-DeliveryInfo | entity | DeliveryInfo | // getDefaultDeliveryInfo (UC-004)<br>// checkDeliveryInfoValidity (UC-004)<br>// saveAsDefault (UC-004)<br>// calculateShippingFee: tính phí theo BR-03 đến BR-09 (UC-004) | receiverName, phoneNumber, province, address, deliveryInstructions: Văn bản<br>rushOrderSelected: Có/Không | UC-004 | - | Hoạt động |
| AC-E-Invoice | entity | Invoice | // calculateTotals: tính các tổng (UC-004)<br>// saveInvoice: ghi nhận đơn hàng tạm thời (UC-004) | lines: sản phẩm, số lượng, giá<br>subtotal, totalWithVat, shippingFee, totalAmount: Số tiền | UC-004 | - | Hoạt động |
| AC-E-Order | entity | Order | // getRefundInfo: số tiền và thẻ đã dùng (UC-007)<br>// markCancelled: chuyển sang đã huỷ (UC-007) | totalAmount: Số tiền<br>status: Trạng thái | UC-007 | - | Hoạt động |
| AC-E-Card | entity | Card | // getCardInfo: cung cấp thông tin thẻ (UC-007) | cardholderName, cardNumber, issuingBank, securityCode: Văn bản<br>expirationDate: Ngày | UC-007 | - | Hoạt động |

## F4. Bảng quan hệ

<!--GEN:P08REL-->
| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn UC | Bằng chứng | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| R-01 | AC-B-PlaceOrderForm | AC-C-PlaceOrderController | Association | - | - | UC-004 | Link K-02 của UC-004 | Tạm thời; R-UC004-01 |
| R-02 | AC-C-PlaceOrderController | AC-E-Cart | Association | - | - | UC-004 | Link K-03 của UC-004 | Tạm thời; R-UC004-02 |
| R-03 | AC-E-Cart | AC-E-Media | Association | Chưa xác định (Q-23) | items | UC-004 | REQ-35, REQ-37: giỏ hàng chứa sản phẩm với số lượng; sản phẩm tồn tại độc lập với giỏ nên không là composition | R-UC004-03 |
| R-04 | AC-C-PlaceOrderController | AC-E-DeliveryInfo | Association | - | - | UC-004 | Link K-05 của UC-004 | Tạm thời; R-UC004-04 |
| R-05 | AC-C-PlaceOrderController | AC-C-PlaceRushOrderController | Association | - | - | UC-004 | Bước 7a, P03 RL-12 | Tạm thời; R-UC004-05 |
| R-06 | AC-C-PlaceOrderController | AC-E-Invoice | Association | - | - | UC-004 | Link K-08 của UC-004 | Tạm thời; R-UC004-06 |
| R-07 | AC-C-PlaceOrderController | AC-C-PayOrderController | Association | - | - | UC-004 | Bước 10, P03 RL-11 | Tạm thời; R-UC004-07 |
| R-08 | AC-E-Invoice | AC-E-Media | Association | Chưa xác định (Q-23) | lines | UC-004 | REQ-71: đơn hàng tạm thời gồm danh sách sản phẩm, số lượng, giá | R-UC004-08 |
| R-09 | AC-B-CancelOrderForm | AC-C-CancelOrderController | Association | - | - | UC-007 | Link K-02 của UC-007 | Tạm thời; R-UC007-01 |
| R-10 | AC-C-CancelOrderController | AC-E-Order | Association | - | - | UC-007 | Link K-03 của UC-007 | Tạm thời; R-UC007-02 |
| R-11 | AC-E-Order | AC-E-Card | Association | Chưa xác định (Q-23) | paymentCard | UC-007 | BR-12: thẻ tín dụng đã dùng để thanh toán đơn hàng | R-UC007-03 |
| R-12 | AC-C-CancelOrderController | AC-B-InterbankBoundary | Association | - | - | UC-007 | Link K-05 của UC-007 | Tạm thời; R-UC007-04 |
<!--/GEN:P08REL-->

Không có generalization, aggregation, composition: đặc tả UC-004, UC-007 và sổ BR không có câu về quan hệ "là một loại" hay vòng đời phụ thuộc giữa các entity đã có. Sách, CD, LP, DVD là các loại sản phẩm (REQ-18 đến REQ-21) nhưng chưa xuất hiện trong luồng của hai use case đã phân tích nên chưa thành lớp.

## F5. Analysis class diagram tổng thể

File diagrams/P08-class-analysis.drawio, một trang "Tổng thể" (13 lớp, dưới ngưỡng 20).

<!--GEN:P08-->
#### Bảng Node (lớp)

| ID (mã AC) | Loại | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-PlaceOrderForm | Class | PlaceOrderForm | «boundary» | - | - | // requestToPlaceOrder<br>// submitDeliveryInfo<br>// displayInsufficientStock<br>// requestDeliveryInfo<br>// requestUpdateDeliveryInfo<br>// displayInvoice |
| AC-B-CancelOrderForm | Class | CancelOrderForm | «boundary» | - | - | // requestToCancelOrder |
| AC-B-InterbankBoundary | Class | InterbankBoundary | «boundary» | - | - | // refund |
| AC-C-PlaceRushOrderController | Class | PlaceRushOrderController | «control» | - | - | // placeRushOrder |
| AC-C-PlaceOrderController | Class | PlaceOrderController | «control» | - | - | // placeOrder<br>// submitDeliveryInfo<br>// checkRushOrderSelected |
| AC-C-PayOrderController | Class | PayOrderController | «control» | - | - | // payOrder |
| AC-C-CancelOrderController | Class | CancelOrderController | «control» | - | - | // cancelOrder<br>// abortCancellation |
| AC-E-Cart | Class | Cart | «entity» | - | items: sản phẩm và số lượng | // checkMediaAvailability<br>// calculateSubtotal<br>// getHeaviestMediaWeight |
| AC-E-DeliveryInfo | Class | DeliveryInfo | «entity» | - | receiverName: Văn bản<br>phoneNumber: Văn bản<br>province: Văn bản<br>address: Văn bản<br>deliveryInstructions: Văn bản<br>rushOrderSelected: Có/Không | // getDefaultDeliveryInfo<br>// checkDeliveryInfoValidity<br>// saveAsDefault<br>// calculateShippingFee |
| AC-E-Invoice | Class | Invoice | «entity» | - | lines: sản phẩm, số lượng, giá<br>subtotal: Số tiền<br>totalWithVat: Số tiền<br>shippingFee: Số tiền<br>totalAmount: Số tiền | // calculateTotals<br>// saveInvoice |
| AC-E-Order | Class | Order | «entity» | - | totalAmount: Số tiền<br>status: Trạng thái | // getRefundInfo<br>// markCancelled |
| AC-E-Card | Class | Card | «entity» | - | cardholderName: Văn bản<br>cardNumber: Văn bản<br>issuingBank: Văn bản<br>expirationDate: Ngày<br>securityCode: Văn bản | // getCardInfo |
| AC-E-Media | Class | Media | «entity» | - | title: Văn bản<br>price: Số tiền<br>quantity: Số lượng<br>weight: Khối lượng | // checkAvailableQuantity |

#### Bảng quan hệ (Edge)

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Thuộc về (view) |
|---|---|---|---|---|---|
| R-01 | AC-B-PlaceOrderForm | AC-C-PlaceOrderController | Association | - | Tổng thể |
| R-02 | AC-C-PlaceOrderController | AC-E-Cart | Association | - | Tổng thể |
| R-03 | AC-E-Cart | AC-E-Media | Association | Chưa xác định (Q-23) | Tổng thể |
| R-04 | AC-C-PlaceOrderController | AC-E-DeliveryInfo | Association | - | Tổng thể |
| R-05 | AC-C-PlaceOrderController | AC-C-PlaceRushOrderController | Association | - | Tổng thể |
| R-06 | AC-C-PlaceOrderController | AC-E-Invoice | Association | - | Tổng thể |
| R-07 | AC-C-PlaceOrderController | AC-C-PayOrderController | Association | - | Tổng thể |
| R-08 | AC-E-Invoice | AC-E-Media | Association | Chưa xác định (Q-23) | Tổng thể |
| R-09 | AC-B-CancelOrderForm | AC-C-CancelOrderController | Association | - | Tổng thể |
| R-10 | AC-C-CancelOrderController | AC-E-Order | Association | - | Tổng thể |
| R-11 | AC-E-Order | AC-E-Card | Association | Chưa xác định (Q-23) | Tổng thể |
| R-12 | AC-C-CancelOrderController | AC-B-InterbankBoundary | Association | - | Tổng thể |
<!--/GEN:P08-->

## F6. Rà soát lớp phân tích

| AC | Tên phản ánh đúng vai trò | Một khái niệm duy nhất | Trách nhiệm gắn kết | Cung cấp đủ hành vi cần | Yêu cầu đặc thù (BR, NFR) đã gắn | Ghi chú |
|---|---|---|---|---|---|---|
| AC-B-PlaceOrderForm | Đạt | Đạt | Đạt | Đạt | Đạt | - |
| AC-B-CancelOrderForm | Đạt | Đạt | Đạt | Đạt | Không đạt | Luồng 3a chưa có thông báo cho khách hàng (Q-21) |
| AC-B-InterbankBoundary | Đạt | Đạt | Đạt | Không đạt | Không đạt | Chưa có trách nhiệm trừ tiền, xem số dư vì UC-006 chưa phân tích; NFR 2 giây (REQ-78) chưa gắn vì P06 chưa có |
| AC-C-PlaceOrderController | Đạt | Đạt | Đạt | Đạt | Đạt | - |
| AC-C-PlaceRushOrderController | Đạt | Đạt | Đạt | Không đạt | Không đạt | Tạm, chờ P07 của UC-005 |
| AC-C-PayOrderController | Đạt | Đạt | Đạt | Không đạt | Không đạt | Tạm, chờ P07 của UC-006 |
| AC-C-CancelOrderController | Đạt | Đạt | Đạt | Đạt | Đạt | - |
| AC-E-Cart | Đạt | Đạt | Đạt | Đạt | Đạt | BR-01 |
| AC-E-Media | Đạt | Đạt | Đạt | Đạt | Không đạt | Quy tắc giá (REQ-24, REQ-25) thuộc UC-009 chưa phân tích |
| AC-E-DeliveryInfo | Đạt | Đạt | Không đạt | Đạt | Đạt | Vừa giữ thông tin người nhận vừa tính phí giao hàng; xem Vấn đề còn mở |
| AC-E-Invoice | Không đạt | Không đạt | Đạt | Đạt | Đạt | Có thể trùng khái niệm với Order (Q-24) |
| AC-E-Order | Không đạt | Không đạt | Đạt | Đạt | Đạt | Như trên |
| AC-E-Card | Đạt | Đạt | Đạt | Không đạt | Đạt | Chỉ cung cấp dữ liệu (entity thiếu trách nhiệm hành vi) |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-24 | "Đơn hàng tạm thời (invoice)" và "đơn hàng" có phải cùng một khái niệm ở hai trạng thái (tạm thời, chờ xử lý) không? | AC-E-Invoice, AC-E-Order; quan hệ giữa hai lớp | L156, L169-171 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 1: 8/10 use case chưa có P07 (lần chạy kiểm chứng chỉ phân tích UC-004, UC-007).
- Target 3: AC-E-Invoice và AC-E-Order có thể là một khái niệm; chưa gộp vì thiếu glossary (P05 chưa chạy) và Q-24.
- Target 6: multiplicity của R-03, R-08, R-11 để trống, chờ Q-23.
- AC-E-DeliveryInfo nhận trách nhiệm tính phí giao hàng do P07 chọn phương án Information Expert theo địa điểm; khi phân tích UC-005 (phụ phí giao nhanh theo sản phẩm, REQ-69) cần xét lại có tách lớp mới giữ quy tắc phí hay không.
