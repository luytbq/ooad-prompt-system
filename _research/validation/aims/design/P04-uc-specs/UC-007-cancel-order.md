# P04 - Đặc tả use case UC-007 Huỷ đơn hàng - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; AIMS-ProblemStatement-VI.md; P00 1.0; P01 1.0; P02 1.0; P03 1.0; P04-uc-specs/_BR-register.md (sau UC-004) |
| Phạm vi | UC-007 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-007 |
| Tên use case | Huỷ đơn hàng (Cancel Order) |
| Tác nhân chính | ACT-01 Khách hàng |
| Tác nhân phụ | ACT-03 Liên ngân hàng |
| Mô tả ngắn | Use case này mô tả tương tác giữa khách hàng và hệ thống khi khách hàng muốn huỷ một đơn hàng đã thanh toán. Kết quả là đơn hàng bị huỷ và toàn bộ số tiền được hoàn vào thẻ tín dụng đã dùng để thanh toán. |
| Sự kiện kích hoạt | Khách hàng muốn huỷ đơn hàng đã thanh toán (EV-05) |
| Tiền điều kiện | Khách hàng có ít nhất một đơn hàng đã được thanh toán và chưa bị huỷ (BR-13). |
| Hậu điều kiện (thành công) | Đơn hàng được ghi nhận là đã bị huỷ.<br>Toàn bộ số tiền đã thanh toán của đơn hàng được cộng vào thẻ tín dụng đã dùng để thanh toán đơn hàng đó. |
| Hậu điều kiện tối thiểu | Nếu hoàn tiền không thành công, trạng thái đơn hàng không thay đổi. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-90, REQ-91, REQ-97, REQ-99 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Khách hàng | Yêu cầu huỷ một đơn hàng đã thanh toán. |
| 2 | Hệ thống | Yêu cầu Liên ngân hàng cộng toàn bộ số tiền đã thanh toán của đơn hàng vào thẻ tín dụng đã dùng để thanh toán đơn hàng (BR-12). |
| 3 | Liên ngân hàng | Trả về kết quả hoàn tiền. |
| 4 | Hệ thống | Ghi nhận đơn hàng đã bị huỷ. |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 3a | Liên ngân hàng trả về kết quả hoàn tiền không thành công | Hệ thống | Giữ nguyên trạng thái đơn hàng; cách thông báo cho khách hàng chưa quy định (Q-21). | Kết thúc use case (thất bại) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Không có

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-12 | Khi đơn hàng bị huỷ, toàn bộ số tiền của đơn được hoàn trả vào thẻ tín dụng đã dùng để thanh toán đơn hàng đó. | Kích hoạt hành động | 2 | REQ-91 | Mới |
| BR-13 | Khách hàng chỉ được huỷ đơn hàng đã thanh toán. | Ràng buộc | Tiền điều kiện | REQ-90 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Thời gian đáp ứng của giao dịch hoàn tiền không quá 2 giây ("mọi giao dịch") | Performance | REQ-78 |

## 8. Thông tin bổ sung

- Bước ghi nhận huỷ (bước 4) đặt sau khi hoàn tiền thành công để hậu điều kiện tối thiểu được bảo đảm; nguồn không nêu thứ tự hai việc này.
- Cách khách hàng chỉ định đơn cần huỷ và thời hạn được huỷ chưa được quy định (Q-14).

## 9. Activity diagram

File: diagrams/P04-activity-UC-007.drawio

<!--GEN:P04-UC-007-->
#### Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Khách hàng | - | - | - | - | 0 | 0 | 300 | 640 |
| P-SYS | Partition | Hệ thống | - | - | - | - | 300 | 0 | 480 | 640 |
| P-ACT-03 | Partition | Liên ngân hàng | - | - | - | - | 780 | 0 | 300 | 640 |
| INIT | Initial | - | - | P-ACT-01 | - | - | 140 | 60 | 30 | 30 |
| A-1 | Action | Yêu cầu huỷ đơn hàng đã thanh toán | - | P-ACT-01 | 1 | - | 60 | 110 | 180 | 60 |
| A-2 | Action | Yêu cầu Liên ngân hàng hoàn toàn bộ tiền vào thẻ | - | P-SYS | 2 | - | 60 | 200 | 180 | 60 |
| A-3 | Action | Trả về kết quả hoàn tiền | - | P-ACT-03 | 3 | - | 60 | 290 | 180 | 60 |
| D-3 | Decision | - | - | P-ACT-03 | - | - | 130 | 380 | 40 | 40 |
| A-3a | Action | Giữ nguyên trạng thái đơn hàng | - | P-SYS | 3a | - | 260 | 370 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - | 340 | 470 | 30 | 30 |
| A-4 | Action | Ghi nhận đơn hàng đã bị huỷ | - | P-SYS | 4 | - | 30 | 460 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | - | 110 | 560 | 30 | 30 |

Toạ độ của node con tính tương đối trong partition chứa nó.

#### Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - |
| E-03 | A-2 | A-3 | ControlFlow | - | - |
| E-04 | A-3 | D-3 | ControlFlow | - | - |
| E-05 | D-3 | A-4 | ControlFlow | [hoàn tiền thành công] | - |
| E-06 | D-3 | A-3a | ControlFlow | [hoàn tiền không thành công] | - |
| E-07 | A-3a | FINAL-1 | ControlFlow | - | - |
| E-08 | A-4 | FINAL-2 | ControlFlow | - | - |

#### Đối chiếu bước và node

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 3 | A-3 |
| 3a | A-3a |
| 4 | A-4 |
<!--/GEN:P04-UC-007-->

## Câu hỏi mở

Không có câu hỏi mới. Câu hỏi liên quan đã có: Q-14 (thời hạn huỷ, chỉ định đơn), Q-18 (trạng thái đơn hàng), Q-21 (hoàn tiền thất bại).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-007 | Luồng chính 4 bước, gần ngưỡng dưới; nguồn chỉ có hai câu về huỷ đơn (L183-184) | Giữ UC-007; bổ sung khi Q-14 được trả lời |

## Vấn đề còn mở

- Target 9: bước 3 là bước trả kết quả của tác nhân phụ; luồng 3a có hành động phụ thuộc Q-21.
- BR-13 có Bước áp dụng là "Tiền điều kiện" vì hệ thống không kiểm tra lại tiền điều kiện trong luồng (F3); F7.3 chỉ liệt kê bước luồng hoặc bảng dữ liệu.
