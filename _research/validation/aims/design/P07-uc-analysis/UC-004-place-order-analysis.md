# P07 - Phân tích use case UC-004 Đặt hàng - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; P01 1.0; P02 1.0; P03 1.0; P04-uc-specs/UC-004-place-order.md 1.0; P04-uc-specs/_BR-register.md. Không có P05, P06 (chưa chạy) |
| Phạm vi | UC-004 |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-004 Đặt hàng |
| Tác nhân chính | ACT-01 Khách hàng (Người) |
| Tác nhân phụ | Không có |
| Include | UC-006 Thanh toán đơn hàng (tại bước 10) |
| Được include bởi | Không có |
| Extend | Không có |
| Được extend bởi | UC-005 Đặt hàng giao nhanh, điểm mở rộng "Chọn giao hàng nhanh", điều kiện {khách hàng chọn giao hàng nhanh} |
| File P07 đã có được dùng làm sổ đăng ký AC | Không có (đây là use case phân tích đầu tiên). Đặt trước: AC-C-PlaceRushOrderController (Tạm - chờ P07 của UC-005), AC-C-PayOrderController (Tạm - chờ P07 của UC-006) |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Khách hàng | Yêu cầu đặt hàng các sản phẩm trong giỏ hàng. | Không đổi | REQ-47 |
| 2 | Hệ thống | Kiểm tra lượng hàng tồn kho đủ cung cấp cho mọi sản phẩm trong giỏ hàng. | Với mỗi sản phẩm trong giỏ hàng, hệ thống so số lượng trong giỏ với số lượng tồn kho của sản phẩm đó; ghi nhận các sản phẩm không đủ kèm số lượng tồn kho. | BR-01, REQ-48 |
| 2a | Hệ thống | Yêu cầu khách hàng cập nhật lại giỏ hàng và hiển thị số lượng tồn kho của mỗi sản phẩm không đáp ứng. | Hệ thống gửi cho khách hàng danh sách sản phẩm không đủ và số lượng tồn kho của từng sản phẩm, không lưu thay đổi nào. | BR-02, REQ-49 |
| 3 | Hệ thống | Hiển thị thông tin giao hàng mặc định đã lưu và yêu cầu khách hàng cập nhật. | Hệ thống lấy thông tin giao hàng mặc định đã lưu (tên người nhận, số điện thoại, tỉnh/thành phố, địa chỉ) và gửi cho khách hàng để cập nhật. | REQ-44, REQ-45, REQ-51 |
| 4 | Khách hàng | Nhập và gửi thông tin giao hàng, chỉ dẫn giao hàng và lựa chọn phương thức giao hàng. | Không đổi | REQ-51, REQ-52 |
| 5 | Hệ thống | Kiểm tra thông tin giao hàng đủ trường bắt buộc và hợp lệ. | Hệ thống kiểm tra thông tin giao hàng vừa nhận: các trường bắt buộc có giá trị và từng trường thoả điều kiện hợp lệ (trường bắt buộc và điều kiện chờ Q-10). | REQ-55 |
| 5a, 5b | Hệ thống | Yêu cầu khách hàng cập nhật lại thông tin giao hàng. | Hệ thống gửi yêu cầu cập nhật lại, không lưu thông tin giao hàng. | REQ-55 |
| 6 | Hệ thống | Lưu thông tin giao hàng làm thông tin giao hàng mặc định. | Hệ thống ghi thông tin giao hàng vừa kiểm tra thành thông tin giao hàng mặc định. | REQ-44 |
| 7 | Hệ thống | Kiểm tra lựa chọn giao hàng nhanh của khách hàng. | Hệ thống đọc lựa chọn giao hàng nhanh trong thông tin khách hàng vừa gửi. | REQ-56 |
| 7a | Hệ thống | Chèn use case UC-005. | Hệ thống chuyển điều phối cho UC-005 Đặt hàng giao nhanh; nội bộ UC-005 thuộc phân tích của UC-005. | REQ-52, P03 RL-12 |
| 8 | Hệ thống | Tính phí giao hàng theo khối lượng sản phẩm và địa điểm nhận hàng. | Hệ thống lấy tổng giá sản phẩm và khối lượng của sản phẩm nặng nhất trong giỏ, rồi tính phí theo tỉnh/thành phố và địa chỉ nhận hàng: miễn phí khi tổng giá trên 100.000 VNĐ; ngược lại giá khởi điểm theo nội thành Hà Nội, TP.HCM hay nơi khác cộng 2.500 VNĐ mỗi 0,5 kg tiếp theo. | BR-03 đến BR-09 |
| 9 | Hệ thống | Hiển thị và lưu đơn hàng tạm thời. | Hệ thống tạo đơn hàng tạm thời từ các sản phẩm trong giỏ (sản phẩm, số lượng, giá) và phí giao hàng, tính tổng giá chưa VAT, đã gồm VAT và tổng số tiền phải trả, lưu lại và gửi cho khách hàng. | BR-10, BR-11, REQ-70, REQ-71 |
| 10 | Hệ thống | Gọi use case UC-006 Thanh toán đơn hàng. | Hệ thống chuyển đơn hàng tạm thời cho điều phối của UC-006; nội bộ UC-006 thuộc phân tích của UC-006. | REQ-43, REQ-73, P03 RL-11 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng | Lý do |
|---|---|---|---|---|---|
| ACT-01 Khách hàng | Người | PlaceOrderForm | Giao diện người dùng | Mới | Một boundary cho cặp Khách hàng - UC-004 |

ACT-03 Liên ngân hàng chỉ tương tác trong UC-006 (được include), nên không tạo boundary ở đây (A3).

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | khách hàng | Bước 1, 3, 4 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01 |
| 2 | hệ thống | Mọi bước hệ thống | Loại - mơ hồ | Chính hệ thống |
| 3 | giỏ hàng | Bước 1, 2, 2a | Entity (AC-E-Cart) | Được lưu vào tài khoản hoặc bộ nhớ thiết bị qua nhiều phiên (REQ-44), có hành vi kiểm tra tồn kho, tính tổng giá |
| 4 | sản phẩm | Bước 1, 2, 2a, Dữ liệu ra 1, 3 | Entity (AC-E-Media) | Thông tin sản phẩm được quản lý lâu dài; nguồn gọi là "media" (L30) |
| 5 | lượng hàng tồn kho, số lượng tồn kho | Bước 2, 2a, Dữ liệu ra 1 | Loại - thuộc tính của Media | Số lượng sản phẩm (REQ-23) |
| 6 | số lượng (trong giỏ) | Bước 2 | Loại - thuộc tính của Cart | Số lượng của từng sản phẩm trong giỏ (REQ-35) |
| 7 | thông tin giao hàng, thông tin giao hàng mặc định | Bước 3, 4, 5, 6 | Entity (AC-E-DeliveryInfo) | Được lưu và lấy lại qua các lần đặt hàng (REQ-44), có hành vi kiểm tra hợp lệ và tính phí theo địa điểm |
| 8 | tên người nhận, số điện thoại, tỉnh/thành phố nhận hàng, địa chỉ nhận hàng | Dữ liệu vào 1, Dữ liệu ra 2 | Loại - thuộc tính của DeliveryInfo | REQ-45 |
| 9 | chỉ dẫn giao hàng | Bước 3, 4 | Loại - thuộc tính của DeliveryInfo | Gửi cùng thông tin giao hàng |
| 10 | lựa chọn giao hàng nhanh, phương thức giao hàng | Bước 4, 7 | Loại - thuộc tính của DeliveryInfo | Gửi cùng thông tin giao hàng ở bước 4 |
| 11 | trường bắt buộc | Bước 5 | Loại - cấu trúc cài đặt | Mô tả cách nhập liệu |
| 12 | phí giao hàng | Bước 8, Dữ liệu ra 3 | Loại - thuộc tính của Invoice | Là một dòng của đơn hàng tạm thời (REQ-71) |
| 13 | khối lượng sản phẩm | Bước 8 | Loại - thuộc tính của Media | REQ-23 |
| 14 | địa điểm nhận hàng | Bước 8 | Loại - trùng hoặc đồng nghĩa với tỉnh/thành phố và địa chỉ nhận hàng | Thuộc tính của DeliveryInfo |
| 15 | đơn hàng tạm thời (invoice) | Bước 9, Dữ liệu ra 3 | Entity (AC-E-Invoice) | Được lưu (REQ-70), có hành vi tính tổng |
| 16 | danh sách sản phẩm | Dữ liệu ra 3 | Loại - cấu trúc cài đặt | Thành phần lines của Invoice |
| 17 | giá sản phẩm | Dữ liệu ra 3 | Loại - thuộc tính của Media | REQ-16 |
| 18 | tổng giá chưa gồm VAT, tổng giá đã gồm VAT, tổng số tiền phải trả | Bước 9, Dữ liệu ra 3 | Loại - thuộc tính của Invoice | REQ-71 |
| 19 | VAT, giá khởi điểm, kg, nội thành | BR-03 đến BR-10 | Loại - thuộc tính của Invoice | Tham số của quy tắc tính, không phải khái niệm lưu riêng |
| 20 | use case UC-005, UC-006 | Bước 7a, 10 | Loại - là tác nhân hoặc ngoài phạm vi | Thuộc phân tích của use case khác |
| 21 | đơn hàng | Hậu điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | Đơn hàng đã thanh toán được tạo trong UC-006 |
| 22 | tài khoản, bộ nhớ thiết bị | Thông tin bổ sung | Loại - cấu trúc cài đặt | Nơi lưu trữ (REQ-44) |

Ghi chú: hàng 19 xếp "thuộc tính của Invoice" vì F3.2 không có giá trị kết luận cho hằng số của quy tắc nghiệp vụ.

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do |
|---|---|---|---|
| PlaceOrderController | UC-004 | Mới | Một control cho mỗi use case |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-PlaceOrderForm | boundary | PlaceOrderForm | // requestToPlaceOrder: nhận yêu cầu đặt hàng<br>// submitDeliveryInfo: nhận thông tin giao hàng, chỉ dẫn, lựa chọn giao nhanh<br>// displayInsufficientStock: hiển thị sản phẩm thiếu và số lượng tồn kho<br>// requestDeliveryInfo: hiển thị thông tin giao hàng mặc định để cập nhật<br>// requestUpdateDeliveryInfo: yêu cầu cập nhật lại thông tin giao hàng<br>// displayInvoice: hiển thị đơn hàng tạm thời | - | 1, 2a, 3, 4, 5a, 5b, 9 | Giao diện người dùng | Mới | - |
| AC-C-PlaceOrderController | control | PlaceOrderController | // placeOrder: điều phối từ yêu cầu đặt hàng tới hiển thị thông tin giao hàng<br>// submitDeliveryInfo: điều phối kiểm tra, lưu thông tin giao hàng, tính phí, lập đơn hàng tạm thời, gọi thanh toán<br>// checkRushOrderSelected: xác định có chèn UC-005 | - | 1-10 | - | Mới | - |
| AC-E-Cart | entity | Cart | // checkMediaAvailability: kiểm tra tồn kho cho mọi sản phẩm trong giỏ<br>// calculateSubtotal: tính tổng giá sản phẩm<br>// getHeaviestMediaWeight: cho biết khối lượng sản phẩm nặng nhất | items: sản phẩm và số lượng | 2, 8 | - | Mới | - |
| AC-E-Media | entity | Media | // checkAvailableQuantity: so số lượng yêu cầu với số lượng tồn kho | title: Văn bản<br>price: Số tiền<br>quantity: Số lượng<br>weight: Khối lượng | 2, 8 | - | Mới | - |
| AC-E-DeliveryInfo | entity | DeliveryInfo | // getDefaultDeliveryInfo: cung cấp thông tin giao hàng mặc định<br>// checkDeliveryInfoValidity: kiểm tra trường bắt buộc và tính hợp lệ<br>// saveAsDefault: lưu làm thông tin mặc định<br>// calculateShippingFee: tính phí theo địa điểm, khối lượng, tổng giá (BR-03 đến BR-09) | receiverName: Văn bản<br>phoneNumber: Văn bản<br>province: Văn bản<br>address: Văn bản<br>deliveryInstructions: Văn bản<br>rushOrderSelected: Có/Không | 3, 5, 6, 8 | - | Mới | - |
| AC-E-Invoice | entity | Invoice | // calculateTotals: tính tổng chưa VAT, đã gồm VAT, tổng số tiền phải trả (BR-10, BR-11)<br>// saveInvoice: ghi nhận đơn hàng tạm thời | lines: sản phẩm, số lượng, giá<br>subtotal: Số tiền<br>totalWithVat: Số tiền<br>shippingFee: Số tiền<br>totalAmount: Số tiền | 9 | - | Mới | - |
| AC-C-PlaceRushOrderController | control | PlaceRushOrderController | // placeRushOrder: điều phối UC-005 khi được chèn | - | 7a | - | Mới (Tạm - chờ P07 của UC-005) | - |
| AC-C-PayOrderController | control | PayOrderController | // payOrder: điều phối UC-006 khi được gọi | - | 10 | - | Mới (Tạm - chờ P07 của UC-006) | - |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | Nhận yêu cầu đặt hàng | AC-B-PlaceOrderForm | Giao tiếp tác nhân | - |
| 1 | Điều phối đặt hàng | AC-C-PlaceOrderController | Controller | - |
| 2 | Kiểm tra tồn kho cho mọi sản phẩm trong giỏ | AC-E-Cart | Information Expert | Giỏ nắm danh sách sản phẩm và số lượng; mỗi Media nắm tồn kho của nó |
| 2 | So số lượng yêu cầu với tồn kho | AC-E-Media | Information Expert | - |
| 2a | Hiển thị sản phẩm thiếu, số lượng tồn kho | AC-B-PlaceOrderForm | Giao tiếp tác nhân | - |
| 3 | Cung cấp thông tin giao hàng mặc định | AC-E-DeliveryInfo | Information Expert | - |
| 3 | Hiển thị thông tin giao hàng để cập nhật | AC-B-PlaceOrderForm | Giao tiếp tác nhân | - |
| 5 | Kiểm tra thông tin giao hàng | AC-E-DeliveryInfo | Information Expert | - |
| 5a, 5b | Yêu cầu cập nhật lại | AC-B-PlaceOrderForm | Giao tiếp tác nhân | - |
| 6 | Lưu thông tin mặc định | AC-E-DeliveryInfo | Information Expert | - |
| 7 | Xác định có chèn UC-005 | AC-C-PlaceOrderController | Controller | - |
| 7a | Điều phối UC-005 | AC-C-PlaceRushOrderController | Controller | - |
| 8 | Tính tổng giá, khối lượng nặng nhất | AC-E-Cart | Information Expert | - |
| 8 | Tính phí giao hàng | AC-E-DeliveryInfo | Information Expert | Dữ liệu nằm ở Cart (khối lượng, tổng giá) và DeliveryInfo (địa điểm). Giao cho DeliveryInfo vì quy tắc phân theo địa điểm, khối lượng và tổng giá truyền vào làm tham số, không cần quan hệ Cart - DeliveryInfo; phương án giao cho control làm control nắm quy tắc tính toán |
| 9 | Tạo đơn hàng tạm thời | AC-C-PlaceOrderController | Creator | Control có dữ liệu khởi tạo (giỏ, phí giao hàng) |
| 9 | Tính các tổng, lưu | AC-E-Invoice | Information Expert | - |
| 9 | Hiển thị đơn hàng tạm thời | AC-B-PlaceOrderForm | Giao tiếp tác nhân | - |
| 10 | Chuyển sang thanh toán | AC-C-PayOrderController | Controller | - |

## F5. Sequence diagram phân tích

SD1 - Luồng chính và 2a, 5a, 5b, 7a. File diagrams/P07-sequence-UC-004.drawio (một trang).

<!--GEN:SEQ-->
#### Bảng lifeline (Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| L-ACT-01 | Actor | Khách hàng | - | - | ACT-01 |
| L-FORM | Lifeline | :PlaceOrderForm | «boundary» | - | AC-B-PlaceOrderForm |
| L-CTRL | Lifeline | :PlaceOrderController | «control» | - | AC-C-PlaceOrderController |
| L-CART | Lifeline | :Cart | «entity» | - | AC-E-Cart |
| L-MEDIA | Lifeline | :Media | «entity» | - | AC-E-Media |
| L-DINFO | Lifeline | :DeliveryInfo | «entity» | - | AC-E-DeliveryInfo |
| L-INV | Lifeline | :Invoice | «entity» | - | AC-E-Invoice |
| L-RUSH | Lifeline | :PlaceRushOrderController | «control» | - | AC-C-PlaceRushOrderController (tạm, chờ P07 của UC-005) |
| L-PAY | Lifeline | :PayOrderController | «control» | - | AC-C-PayOrderController (tạm, chờ P07 của UC-006) |
| F1 | Fragment | alt [tồn kho không đủ] / [tồn kho đủ] | - | - | - |
| F2 | Fragment | alt [thiếu trường bắt buộc hoặc thông tin không hợp lệ] / [đủ và hợp lệ] | - | - | - |
| F3 | Fragment | opt [khách hàng chọn giao hàng nhanh] ref UC-005 Đặt hàng giao nhanh | - | - | - |

#### Bảng message (Edge)

| STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | L-ACT-01 | L-FORM | // requestToPlaceOrder | Đồng bộ | - | 1 |
| 1.1 | L-FORM | L-CTRL | // placeOrder | Đồng bộ | - | 1 |
| 1.1.1 | L-CTRL | L-CART | // checkMediaAvailability | Đồng bộ | - | 2 |
| 1.1.1.1 | L-CART | L-MEDIA | // checkAvailableQuantity (số lượng trong giỏ, với mỗi sản phẩm) | Đồng bộ | - | 2 |
| 1.1.1 (trả về) | L-CART | L-CTRL | kết quả kiểm tra, sản phẩm thiếu và số lượng tồn kho | Trả về | - | 2 |
| 1.1.2 | L-CTRL | L-FORM | // displayInsufficientStock (sản phẩm thiếu, số lượng tồn kho) | Đồng bộ | F1 | 2a |
| 1.1.3 | L-CTRL | L-DINFO | // getDefaultDeliveryInfo | Đồng bộ | F1 | 3 |
| 1.1.4 | L-CTRL | L-FORM | // requestDeliveryInfo (thông tin giao hàng mặc định) | Đồng bộ | F1 | 3 |
| 2 | L-ACT-01 | L-FORM | // submitDeliveryInfo (thông tin giao hàng, chỉ dẫn, lựa chọn giao nhanh) | Đồng bộ | - | 4 |
| 2.1 | L-FORM | L-CTRL | // submitDeliveryInfo (thông tin giao hàng, chỉ dẫn, lựa chọn giao nhanh) | Đồng bộ | - | 4 |
| 2.1.1 | L-CTRL | L-DINFO | // checkDeliveryInfoValidity | Đồng bộ | - | 5 |
| 2.1.1 (trả về) | L-DINFO | L-CTRL | kết quả kiểm tra | Trả về | - | 5 |
| 2.1.2 | L-CTRL | L-FORM | // requestUpdateDeliveryInfo | Đồng bộ | F2 | 5a, 5b |
| 2.1.3 | L-CTRL | L-DINFO | // saveAsDefault | Đồng bộ | F2 | 6 |
| 2.1.4 | L-CTRL | L-CTRL | // checkRushOrderSelected | Tự gọi | F2 | 7 |
| 2.1.5 | L-CTRL | L-RUSH | // placeRushOrder (ref UC-005 Đặt hàng giao nhanh) | Đồng bộ | F3 | 7a |
| 2.1.6 | L-CTRL | L-CART | // calculateSubtotal | Đồng bộ | F2 | 8 |
| 2.1.7 | L-CTRL | L-CART | // getHeaviestMediaWeight | Đồng bộ | F2 | 8 |
| 2.1.8 | L-CTRL | L-DINFO | // calculateShippingFee (khối lượng lớn nhất, tổng giá) | Đồng bộ | F2 | 8 |
| 2.1.8 (trả về) | L-DINFO | L-CTRL | phí giao hàng | Trả về | F2 | 8 |
| 2.1.9 | L-CTRL | L-INV | // createInvoice (sản phẩm trong giỏ, phí giao hàng) | Tạo | F2 | 9 |
| 2.1.9.1 | L-INV | L-INV | // calculateTotals | Tự gọi | F2 | 9 |
| 2.1.10 | L-CTRL | L-INV | // saveInvoice | Đồng bộ | F2 | 9 |
| 2.1.11 | L-CTRL | L-FORM | // displayInvoice (đơn hàng tạm thời) | Đồng bộ | F2 | 9 |
| 2.1.12 | L-CTRL | L-PAY | // payOrder (đơn hàng tạm thời) | Đồng bộ | F2 | 10 |
<!--/GEN:SEQ-->

## F6. Quy tắc tương tác

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-004.drawio, cùng phạm vi với SD1.

<!--GEN:COMM-->
#### Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| L-ACT-01 | Actor | Khách hàng | - | - | - | 40 | 200 | 30 | 60 |
| L-FORM | Object | :PlaceOrderForm | «boundary» | - | - | 160 | 200 | 200 | 50 |
| L-CTRL | Object | :PlaceOrderController | «control» | - | - | 480 | 200 | 200 | 50 |
| L-RUSH | Object | :PlaceRushOrderController | «control» | - | - | 480 | 40 | 200 | 50 |
| L-PAY | Object | :PayOrderController | «control» | - | - | 820 | 40 | 200 | 50 |
| L-CART | Object | :Cart | «entity» | - | - | 160 | 440 | 200 | 50 |
| L-MEDIA | Object | :Media | «entity» | - | - | 160 | 600 | 200 | 50 |
| L-DINFO | Object | :DeliveryInfo | «entity» | - | - | 480 | 440 | 200 | 50 |
| L-INV | Object | :Invoice | «entity» | - | - | 820 | 440 | 200 | 50 |

#### Bảng Edge (link)

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message |
|---|---|---|---|---|---|
| K-01 | L-ACT-01 | L-FORM | Link | 1: // requestToPlaceOrder (-->)<br>2: // submitDeliveryInfo (-->) | 1: Khách hàng-->PlaceOrderForm<br>2: Khách hàng-->PlaceOrderForm |
| K-02 | L-CTRL | L-FORM | Link | 1.1: // placeOrder (<--)<br>1.1.2: // displayInsufficientStock (-->)<br>1.1.4: // requestDeliveryInfo (-->)<br>2.1: // submitDeliveryInfo (<--)<br>2.1.2: // requestUpdateDeliveryInfo (-->)<br>2.1.11: // displayInvoice (-->) | 1.1: PlaceOrderForm-->PlaceOrderController<br>1.1.2: PlaceOrderController-->PlaceOrderForm<br>1.1.4: PlaceOrderController-->PlaceOrderForm<br>2.1: PlaceOrderForm-->PlaceOrderController<br>2.1.2: PlaceOrderController-->PlaceOrderForm<br>2.1.11: PlaceOrderController-->PlaceOrderForm |
| K-03 | L-CART | L-CTRL | Link | 1.1.1: // checkMediaAvailability (<--)<br>2.1.6: // calculateSubtotal (<--)<br>2.1.7: // getHeaviestMediaWeight (<--) | 1.1.1: PlaceOrderController-->Cart<br>2.1.6: PlaceOrderController-->Cart<br>2.1.7: PlaceOrderController-->Cart |
| K-04 | L-CART | L-MEDIA | Link | 1.1.1.1: // checkAvailableQuantity (-->) | 1.1.1.1: Cart-->Media |
| K-05 | L-CTRL | L-DINFO | Link | 1.1.3: // getDefaultDeliveryInfo (-->)<br>2.1.1: // checkDeliveryInfoValidity (-->)<br>2.1.3: // saveAsDefault (-->)<br>2.1.8: // calculateShippingFee (-->) | 1.1.3: PlaceOrderController-->DeliveryInfo<br>2.1.1: PlaceOrderController-->DeliveryInfo<br>2.1.3: PlaceOrderController-->DeliveryInfo<br>2.1.8: PlaceOrderController-->DeliveryInfo |
| K-06 | L-CTRL | L-CTRL | Link | 2.1.4: // checkRushOrderSelected | 2.1.4: tự gọi |
| K-07 | L-CTRL | L-RUSH | Link | 2.1.5: // placeRushOrder (-->) | 2.1.5: PlaceOrderController-->PlaceRushOrderController |
| K-08 | L-CTRL | L-INV | Link | 2.1.9: // createInvoice (-->)<br>2.1.10: // saveInvoice (-->) | 2.1.9: PlaceOrderController-->Invoice<br>2.1.10: PlaceOrderController-->Invoice |
| K-09 | L-INV | L-INV | Link | 2.1.9.1: // calculateTotals | 2.1.9.1: tự gọi |
| K-10 | L-CTRL | L-PAY | Link | 2.1.12: // payOrder (-->) | 2.1.12: PlaceOrderController-->PayOrderController |

Trong nhãn link, "(-->)" nghĩa là message đi từ Nguồn tới Đích, "(<--)" là chiều ngược lại.
<!--/GEN:COMM-->

## F8. VOPC

File diagrams/P07-class-UC-004.drawio.

<!--GEN:VOPC-->
#### Bảng Node (lớp)

| ID (mã AC) | Loại | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-PlaceOrderForm | Class | PlaceOrderForm | «boundary» | - | - | // requestToPlaceOrder<br>// submitDeliveryInfo<br>// displayInsufficientStock<br>// requestDeliveryInfo<br>// requestUpdateDeliveryInfo<br>// displayInvoice |
| AC-C-PlaceOrderController | Class | PlaceOrderController | «control» | - | - | // placeOrder<br>// submitDeliveryInfo<br>// checkRushOrderSelected |
| AC-C-PlaceRushOrderController | Class | PlaceRushOrderController | «control» | - | - | // placeRushOrder |
| AC-C-PayOrderController | Class | PayOrderController | «control» | - | - | // payOrder |
| AC-E-Cart | Class | Cart | «entity» | - | items: sản phẩm và số lượng | // checkMediaAvailability<br>// calculateSubtotal<br>// getHeaviestMediaWeight |
| AC-E-Media | Class | Media | «entity» | - | title: Văn bản<br>price: Số tiền<br>quantity: Số lượng<br>weight: Khối lượng | // checkAvailableQuantity |
| AC-E-DeliveryInfo | Class | DeliveryInfo | «entity» | - | receiverName: Văn bản<br>phoneNumber: Văn bản<br>province: Văn bản<br>address: Văn bản<br>deliveryInstructions: Văn bản<br>rushOrderSelected: Có/Không | // getDefaultDeliveryInfo<br>// checkDeliveryInfoValidity<br>// saveAsDefault<br>// calculateShippingFee |
| AC-E-Invoice | Class | Invoice | «entity» | - | lines: sản phẩm, số lượng, giá<br>subtotal: Số tiền<br>totalWithVat: Số tiền<br>shippingFee: Số tiền<br>totalAmount: Số tiền | // calculateTotals<br>// saveInvoice |

#### Bảng quan hệ (Edge)

| ID | Lớp A | Lớp B | Loại | Multiplicity (A..B) | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
|---|---|---|---|---|---|---|
| R-UC004-01 | AC-B-PlaceOrderForm | AC-C-PlaceOrderController | Association | - | - | Link K-02 (1.1, 1.1.2, 1.1.4, 2.1, 2.1.2, 2.1.11); tạm thời |
| R-UC004-02 | AC-C-PlaceOrderController | AC-E-Cart | Association | - | - | Link K-03 (1.1.1, 2.1.6, 2.1.7); tạm thời |
| R-UC004-03 | AC-E-Cart | AC-E-Media | Association | Chưa xác định (Q-23) | items | Link K-04 (1.1.1.1); REQ-35, REQ-37 giỏ hàng chứa sản phẩm với số lượng |
| R-UC004-04 | AC-C-PlaceOrderController | AC-E-DeliveryInfo | Association | - | - | Link K-05 (1.1.3, 2.1.1, 2.1.3, 2.1.8); tạm thời |
| R-UC004-05 | AC-C-PlaceOrderController | AC-C-PlaceRushOrderController | Association | - | - | Link K-07 (2.1.5); tạm thời; bước 7a |
| R-UC004-06 | AC-C-PlaceOrderController | AC-E-Invoice | Association | - | - | Link K-08 (2.1.9, 2.1.10); tạm thời |
| R-UC004-07 | AC-C-PlaceOrderController | AC-C-PayOrderController | Association | - | - | Link K-10 (2.1.12); tạm thời; bước 10 |
| R-UC004-08 | AC-E-Invoice | AC-E-Media | Association | Chưa xác định (Q-23) | lines | Dữ liệu ra 3: đơn hàng tạm thời gồm danh sách sản phẩm, số lượng, giá (REQ-71) |
<!--/GEN:VOPC-->

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1, 1.1 | AC-B-PlaceOrderForm, AC-C-PlaceOrderController |
| 2 | 1.1.1, 1.1.1.1 | AC-C-PlaceOrderController, AC-E-Cart, AC-E-Media |
| 2a | 1.1.2 | AC-C-PlaceOrderController, AC-B-PlaceOrderForm |
| 3 | 1.1.3, 1.1.4 | AC-C-PlaceOrderController, AC-E-DeliveryInfo, AC-B-PlaceOrderForm |
| 4 | 2, 2.1 | AC-B-PlaceOrderForm, AC-C-PlaceOrderController |
| 5 | 2.1.1 | AC-C-PlaceOrderController, AC-E-DeliveryInfo |
| 5a, 5b | 2.1.2 | AC-C-PlaceOrderController, AC-B-PlaceOrderForm |
| 6 | 2.1.3 | AC-C-PlaceOrderController, AC-E-DeliveryInfo |
| 7 | 2.1.4 | AC-C-PlaceOrderController |
| 7a | 2.1.5 | AC-C-PlaceOrderController, AC-C-PlaceRushOrderController |
| 8 | 2.1.6, 2.1.7, 2.1.8 | AC-C-PlaceOrderController, AC-E-Cart, AC-E-DeliveryInfo |
| 9 | 2.1.9, 2.1.9.1, 2.1.10, 2.1.11 | AC-C-PlaceOrderController, AC-E-Invoice, AC-B-PlaceOrderForm |
| 10 | 2.1.12 | AC-C-PlaceOrderController, AC-C-PayOrderController |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-23 | Một sản phẩm có thể nằm trong bao nhiêu giỏ hàng, đơn hàng tạm thời; một đơn hàng dùng bao nhiêu thẻ? | Multiplicity R-UC004-03, R-UC004-08, R-UC007-03 | Nguồn không nêu (REQ-35, REQ-40, REQ-71, REQ-91) |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 6 và đặt tên entity: P05-glossary.md chưa có (bước P05 không chạy trong lần kiểm chứng này) nên tên entity (Media, DeliveryInfo, Invoice) lấy từ thuật ngữ tiếng Anh trong nguồn, cột GL để "-". P07 mục 2 ghi P05, P06 là đầu vào bắt buộc nhưng không nêu cách chạy khi thiếu.
- AC-B-PlaceOrderForm có 6 trách nhiệm do gom cả message từ tác nhân (A7).
- Communication diagram thể hiện chiều message bằng ký hiệu "(-->)", "(<--)" trong nhãn thay cho mũi tên nhỏ đặt cạnh nhãn (F7), để bảng và file .drawio khớp nhau.
