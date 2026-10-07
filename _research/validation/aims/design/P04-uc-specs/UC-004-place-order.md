# P04 - Đặc tả use case UC-004 Đặt hàng - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; AIMS-ProblemStatement-VI.md; P00 1.0; P01 1.0; P02 1.0; P03 1.0 |
| Phạm vi | UC-004 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-004 |
| Tên use case | Đặt hàng (Place Order) |
| Tác nhân chính | ACT-01 Khách hàng |
| Tác nhân phụ | Không có |
| Mô tả ngắn | Use case này mô tả tương tác giữa khách hàng và hệ thống khi khách hàng muốn đặt mua các sản phẩm trong giỏ hàng. Kết quả là một đơn hàng đã được thanh toán ở trạng thái chờ xử lý. |
| Sự kiện kích hoạt | Khách hàng muốn đặt mua các sản phẩm trong giỏ (EV-04) |
| Tiền điều kiện | Hệ thống đang hiển thị giỏ hàng cho khách hàng. |
| Hậu điều kiện (thành công) | Thông tin giao hàng mặc định bằng thông tin giao hàng khách hàng đã gửi.<br>Đơn hàng tạm thời được lưu với phí giao hàng và tổng số tiền phải trả.<br>Đơn hàng đã được thanh toán theo UC-006 và ở trạng thái chờ xử lý. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc ở luồng 2a, không có thay đổi dữ liệu nào được lưu. Trạng thái dữ liệu khi thanh toán không thành công chưa được quy định (Q-20). |
| Quan hệ | «include» UC-006 Thanh toán đơn hàng (tại bước 10)<br>Được mở rộng bởi UC-005 Đặt hàng giao nhanh tại điểm mở rộng 'Chọn giao hàng nhanh' |
| Điểm mở rộng | Chọn giao hàng nhanh: tại bước 7 |
| REQ | REQ-17, REQ-43, REQ-44, REQ-45, REQ-47 đến REQ-51, REQ-55, REQ-56, REQ-61 đến REQ-68, REQ-70 đến REQ-73, REQ-92 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Khách hàng | Yêu cầu đặt hàng các sản phẩm trong giỏ hàng. |
| 2 | Hệ thống | Kiểm tra lượng hàng tồn kho đủ cung cấp cho mọi sản phẩm trong giỏ hàng (BR-01). |
| 3 | Hệ thống | Hiển thị thông tin giao hàng mặc định đã lưu (xem Dữ liệu ra 2) và yêu cầu khách hàng cập nhật thông tin giao hàng, chỉ dẫn giao hàng. |
| 4 | Khách hàng | Nhập và gửi thông tin giao hàng, chỉ dẫn giao hàng và lựa chọn phương thức giao hàng (xem Dữ liệu vào 1). |
| 5 | Hệ thống | Kiểm tra thông tin giao hàng đủ trường bắt buộc và hợp lệ. |
| 6 | Hệ thống | Lưu thông tin giao hàng làm thông tin giao hàng mặc định. |
| 7 | Hệ thống | Kiểm tra lựa chọn giao hàng nhanh của khách hàng. |
| 8 | Hệ thống | Tính phí giao hàng theo khối lượng sản phẩm và địa điểm nhận hàng (BR-03 đến BR-09). |
| 9 | Hệ thống | Hiển thị và lưu đơn hàng tạm thời (xem Dữ liệu ra 3), với tổng giá đã gồm VAT và tổng số tiền phải trả (BR-10, BR-11). |
| 10 | Hệ thống | Gọi use case UC-006 Thanh toán đơn hàng để khách hàng thanh toán đơn hàng. |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Lượng tồn kho không đủ cho ít nhất một sản phẩm trong giỏ hàng | Hệ thống | Yêu cầu khách hàng cập nhật lại giỏ hàng và hiển thị số lượng tồn kho của mỗi sản phẩm không đáp ứng (xem Dữ liệu ra 1, BR-02). | Kết thúc use case (thất bại) |
| 5a | Có trường bắt buộc bị bỏ trống | Hệ thống | Yêu cầu khách hàng cập nhật lại thông tin giao hàng. | Quay lại bước 4 |
| 5b | Đủ trường bắt buộc và có thông tin không hợp lệ | Hệ thống | Yêu cầu khách hàng cập nhật lại thông tin giao hàng. | Quay lại bước 4 |
| 7a | Khách hàng chọn giao hàng nhanh | Hệ thống | Chèn use case UC-005 Đặt hàng giao nhanh tại điểm mở rộng 'Chọn giao hàng nhanh'. | Tiếp tục bước 8 |
| *a | Tại bất kỳ bước nào trước bước 10, khách hàng yêu cầu trở về một bước trước | Hệ thống | Đưa khách hàng trở về bước đã chọn. | Quay lại bước khách hàng chọn (một trong các bước 1 đến bước hiện tại) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 4)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Tên người nhận | Người nhận hàng | Chưa quy định (Q-10) | Chưa quy định (Q-10) | Nguyễn Văn An |
| 2 | Số điện thoại | Số điện thoại người nhận | Chưa quy định (Q-10) | Chưa quy định (Q-10) | 0912345678 |
| 3 | Tỉnh/thành phố nhận hàng | Tỉnh hoặc thành phố của địa chỉ nhận hàng | Chưa quy định (Q-10) | Chưa quy định (Q-10) | Hà Nội |
| 4 | Địa chỉ nhận hàng | Địa chỉ cụ thể trong tỉnh/thành phố | Chưa quy định (Q-10) | Chưa quy định (Q-10) | Số 1 Đại Cồ Việt, quận Hai Bà Trưng |
| 5 | Chỉ dẫn giao hàng | Ghi chú của khách hàng cho việc giao hàng | Không | Chưa quy định (Q-10) | Gọi trước khi giao |
| 6 | Lựa chọn giao hàng nhanh | Khách hàng có chọn giao hàng nhanh hay không | Không | Có hoặc Không | Không |

Dữ liệu ra 1 (bước 2a)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tên sản phẩm | Sản phẩm không đủ tồn kho | Văn bản | Mắt biếc |
| 2 | Số lượng tồn kho | Số lượng hiện có trong kho của sản phẩm (Q-13) | Số nguyên | 1 |

Dữ liệu ra 2 (bước 3)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tên người nhận | Theo thông tin giao hàng mặc định đã lưu | Văn bản | Nguyễn Văn An |
| 2 | Số điện thoại | Như trên | Văn bản | 0912345678 |
| 3 | Tỉnh/thành phố nhận hàng | Như trên | Văn bản | Hà Nội |
| 4 | Địa chỉ nhận hàng | Như trên | Văn bản | Số 1 Đại Cồ Việt, quận Hai Bà Trưng |

Dữ liệu ra 3 (bước 9)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Danh sách sản phẩm | Mỗi dòng gồm sản phẩm, số lượng, giá sản phẩm | Chưa quy định (Q-22) | Mắt biếc, 1, 60.000 VNĐ; Album Hoa, 1, 30.000 VNĐ |
| 2 | Tổng giá sản phẩm chưa gồm VAT | Tổng giá các dòng | Chưa quy định (Q-22) | 90.000 VNĐ |
| 3 | Tổng giá sản phẩm đã gồm VAT | Tổng giá chưa VAT cộng VAT 10% (BR-10) | Chưa quy định (Q-22) | 99.000 VNĐ |
| 4 | Phí giao hàng | Theo BR-03 đến BR-09 | Chưa quy định (Q-22) | 22.000 VNĐ (nội thành Hà Nội, sản phẩm nặng nhất 0,5 kg; tổng giá dưới 100.000 VNĐ nên không miễn phí) |
| 5 | Tổng số tiền phải trả | BR-11 | Chưa quy định (Q-22) | 121.000 VNĐ |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-01 | Mỗi khi khách hàng yêu cầu đặt hàng, lượng tồn kho phải đủ cho số lượng của mọi sản phẩm trong giỏ hàng. | Ràng buộc | 2 | REQ-48 | Mới |
| BR-02 | Sau khi cập nhật giỏ hàng vì thiếu tồn kho, khách hàng phải yêu cầu đặt hàng lại để tiếp tục. | Ràng buộc | 2a | REQ-50 | Mới |
| BR-03 | Phí giao hàng phụ thuộc vào khối lượng sản phẩm và địa điểm nhận hàng. | Tính toán | 8 | REQ-62 | Mới |
| BR-04 | Phí giao hàng không bị tính thuế. | Sự kiện | 8 | REQ-63 | Mới |
| BR-05 | Đơn hàng có tổng giá sản phẩm trên 100.000 VNĐ được miễn phí vận chuyển. | Suy luận | 8 | REQ-64 | Mới |
| BR-06 | Chỉ tính phí giao hàng với sản phẩm có khối lượng lớn nhất. | Tính toán | 8 | REQ-65 | Mới |
| BR-07 | Địa chỉ nhận hàng ở nội thành TP. Hà Nội hoặc nội thành TP.HCM có giá khởi điểm 22.000 VNĐ cho 3 kg đầu. | Tính toán | 8 | REQ-66 | Mới |
| BR-08 | Địa chỉ nhận hàng ở vị trí khác trong lãnh thổ Việt Nam có giá khởi điểm 30.000 VNĐ cho 0,5 kg đầu. | Tính toán | 8 | REQ-67 | Mới |
| BR-09 | Mỗi 0,5 kg tiếp theo tính thêm 2.500 VNĐ. | Tính toán | 8 | REQ-68 | Mới |
| BR-10 | Giá sản phẩm chưa gồm VAT; tổng giá đã gồm VAT bằng tổng giá chưa gồm VAT cộng 10%. | Tính toán | 9, Dữ liệu ra 3 | REQ-17 | Mới |
| BR-11 | Tổng số tiền phải trả bằng tổng giá sản phẩm đã gồm VAT cộng phí giao hàng. | Tính toán | 9, Dữ liệu ra 3 | REQ-72 | Mới |

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Thông tin giao hàng mặc định được lấy và lưu ở tài khoản hoặc bộ nhớ thiết bị tuỳ khách hàng có đăng nhập (REQ-44); cách phân biệt chờ Q-02.
- Khi UC-005 phát hiện không có sản phẩm hoặc địa chỉ hỗ trợ giao hàng nhanh, nguồn yêu cầu khách hàng cập nhật lại thông tin giao hàng (REQ-58); điểm quay về bước 4 của use case này được ghi trong đặc tả UC-005, không ghi ở luồng 7a.

## 9. Activity diagram

File: diagrams/P04-activity-UC-004.drawio

<!--GEN:P04-UC-004-->
#### Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Khách hàng | - | - | - | - | 0 | 0 | 300 | 1460 |
| P-SYS | Partition | Hệ thống | - | - | - | - | 300 | 0 | 540 | 1460 |
| INIT | Initial | - | - | P-ACT-01 | - | - | 140 | 60 | 30 | 30 |
| A-1 | Action | Yêu cầu đặt hàng | - | P-ACT-01 | 1 | - | 60 | 110 | 180 | 60 |
| A-2 | Action | Kiểm tra tồn kho đủ | - | P-SYS | 2 | - | 60 | 200 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | - | - | 130 | 290 | 40 | 40 |
| A-2a | Action | Yêu cầu cập nhật giỏ, hiển thị tồn kho | - | P-SYS | 2a | - | 300 | 280 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - | 380 | 380 | 30 | 30 |
| A-3 | Action | Hiển thị thông tin giao hàng mặc định | - | P-SYS | 3 | - | 60 | 370 | 180 | 60 |
| M-4 | Merge | - | - | P-ACT-01 | - | - | 130 | 420 | 40 | 40 |
| A-4 | Action | Nhập và gửi thông tin giao hàng | - | P-ACT-01 | 4 | - | 60 | 480 | 180 | 60 |
| A-5 | Action | Kiểm tra thông tin giao hàng | - | P-SYS | 5 | - | 60 | 560 | 180 | 60 |
| D-5 | Decision | - | - | P-SYS | - | - | 130 | 650 | 40 | 40 |
| A-5a | Action | Yêu cầu cập nhật lại thông tin giao hàng | - | P-SYS | 5a | - | 300 | 640 | 180 | 60 |
| A-5b | Action | Yêu cầu cập nhật lại thông tin giao hàng | - | P-SYS | 5b | - | 300 | 740 | 180 | 60 |
| A-6 | Action | Lưu thông tin giao hàng mặc định | - | P-SYS | 6 | - | 60 | 760 | 180 | 60 |
| A-7 | Action | Kiểm tra lựa chọn giao hàng nhanh | - | P-SYS | 7 | - | 60 | 850 | 180 | 60 |
| D-7 | Decision | - | - | P-SYS | - | - | 130 | 940 | 40 | 40 |
| A-7a | CallBehaviorAction | UC-005 Đặt hàng giao nhanh | - | P-SYS | 7a | - | 300 | 930 | 180 | 60 |
| M-8 | Merge | - | - | P-SYS | - | - | 130 | 1020 | 40 | 40 |
| A-8 | Action | Tính phí giao hàng | - | P-SYS | 8 | - | 60 | 1090 | 180 | 60 |
| A-9 | Action | Hiển thị và lưu đơn hàng tạm thời | - | P-SYS | 9 | - | 60 | 1180 | 180 | 60 |
| A-10 | CallBehaviorAction | UC-006 Thanh toán đơn hàng | - | P-SYS | 10 | - | 60 | 1270 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | - | 140 | 1370 | 30 | 30 |
| N-*a | Note | *a: tại bất kỳ bước nào trước bước 10, khách hàng yêu cầu trở về một bước trước; hệ thống đưa khách hàng về bước đã chọn | - | P-ACT-01 | *a | - | 40 | 900 | 220 | 100 |

Toạ độ của node con tính tương đối trong partition chứa nó.

#### Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - |
| E-03 | A-2 | D-2 | ControlFlow | - | - |
| E-04 | D-2 | A-3 | ControlFlow | [tồn kho đủ] | - |
| E-05 | D-2 | A-2a | ControlFlow | [tồn kho không đủ] | - |
| E-06 | A-2a | FINAL-1 | ControlFlow | - | - |
| E-07 | A-3 | M-4 | ControlFlow | - | - |
| E-08 | M-4 | A-4 | ControlFlow | - | - |
| E-09 | A-4 | A-5 | ControlFlow | - | - |
| E-10 | A-5 | D-5 | ControlFlow | - | - |
| E-11 | D-5 | A-6 | ControlFlow | [đủ trường bắt buộc và hợp lệ] | - |
| E-12 | D-5 | A-5a | ControlFlow | [trường bắt buộc bị bỏ trống] | - |
| E-13 | D-5 | A-5b | ControlFlow | [đủ trường bắt buộc, có thông tin không hợp lệ] | - |
| E-14 | A-5a | M-4 | ControlFlow | - | - |
| E-15 | A-5b | M-4 | ControlFlow | - | - |
| E-16 | A-6 | A-7 | ControlFlow | - | - |
| E-17 | A-7 | D-7 | ControlFlow | - | - |
| E-18 | D-7 | M-8 | ControlFlow | [không chọn giao hàng nhanh] | - |
| E-19 | D-7 | A-7a | ControlFlow | [chọn giao hàng nhanh] | - |
| E-20 | A-7a | M-8 | ControlFlow | - | - |
| E-21 | M-8 | A-8 | ControlFlow | - | - |
| E-22 | A-8 | A-9 | ControlFlow | - | - |
| E-23 | A-9 | A-10 | ControlFlow | - | - |
| E-24 | A-10 | FINAL-2 | ControlFlow | - | - |

#### Đối chiếu bước và node

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a | A-2a |
| 3 | A-3 |
| 4 | A-4 |
| 5 | A-5 |
| 5a | A-5a |
| 5b | A-5b |
| 6 | A-6 |
| 7 | A-7 |
| 7a | A-7a |
| 8 | A-8 |
| 9 | A-9 |
| 10 | A-10 |
| *a | N-*a |
<!--/GEN:P04-UC-004-->

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-22 | Số tiền hiển thị theo định dạng nào (phân cách hàng nghìn, ký hiệu tiền tệ, căn lề)? | Dữ liệu ra 3 của UC-004 | Nguồn chỉ viết "100.000VNĐ" (L138) như cách ghi con số, không quy định hiển thị |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 7 và 10: UC-006 trả kết quả thất bại chưa có luồng thay thế tại bước 10 vì nguồn không nêu xử lý khi thanh toán thất bại (Q-20).
- Target 8: luồng *a có điểm quay lại là bước do khách hàng chọn (REQ-92), không phải một bước K cố định như F5.4 yêu cầu.
- Target 10: cột Bắt buộc của Dữ liệu vào 1 ghi "Chưa quy định (Q-10)" vì nguồn nói có "trường bắt buộc" nhưng không nêu trường nào; F6.1 chỉ quy định cách ghi này cho cột Điều kiện hợp lệ.
