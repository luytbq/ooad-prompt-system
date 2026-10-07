# P03 - Mô hình use case - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P03 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.0 |
| Phạm vi | Toàn hệ thống |

## 1. Bảng quan hệ

| ID | Nguồn | Đích | Loại | Điều kiện extend / điểm mở rộng | Lý do | REQ | Sơ đồ |
|---|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | Tác nhân chính | REQ-33 | Tổng quát |
| RL-02 | ACT-01 | UC-002 | Association | - | Tác nhân chính | REQ-35 | Tổng quát |
| RL-03 | ACT-01 | UC-003 | Association | - | Tác nhân chính | REQ-36 | Tổng quát |
| RL-04 | ACT-01 | UC-004 | Association | - | Tác nhân chính | REQ-47 | Tổng quát |
| RL-05 | ACT-03 | UC-006 | Association | - | Tác nhân phụ: trừ tiền trên thẻ. Tác nhân phụ chỉ tham gia phần hành vi được include (Bước 2.2a) | REQ-77, REQ-98 | Tổng quát |
| RL-06 | ACT-01 | UC-007 | Association | - | Tác nhân chính | REQ-90 | Tổng quát |
| RL-07 | ACT-03 | UC-007 | Association | - | Tác nhân phụ: cộng tiền hoàn trả vào thẻ | REQ-99 | Tổng quát |
| RL-08 | ACT-01 | UC-008 | Association | - | Tác nhân chính | REQ-81 | Tổng quát |
| RL-09 | ACT-02 | UC-009 | Association | - | Tác nhân chính | REQ-08 | Tổng quát |
| RL-10 | ACT-02 | UC-010 | Association | - | Tác nhân chính | REQ-84 | Tổng quát |
| RL-11 | UC-004 | UC-006 | Include | - | UC-006 được P02 giữ theo Q4c (Bước 3a); thanh toán bắt buộc trong mọi kịch bản đặt hàng thành công, "Để đặt hàng thành công, khách hàng cần thực hiện 2 bước đầu tiên: đặt hàng và thanh toán" (Bước 3b); có căn cứ nguồn (Bước 3c) | REQ-43, REQ-73 | Tổng quát |
| RL-12 | UC-005 | UC-004 | Extend | {khách hàng chọn giao hàng nhanh} tại Chọn giao hàng nhanh | UC-005 được P02 giữ theo Q4b (Bước 4a); đặt hàng đạt mục tiêu khi không chọn giao nhanh, "Trong trường hợp khách hàng không muốn đặt hàng nhanh, hệ thống sẽ bắt đầu tính phí giao hàng luôn" (Bước 4b); điều kiện và điểm mở rộng xác định được (Bước 4c) | REQ-52, REQ-56 | Tổng quát |

## 2. Điểm mở rộng

| UC gốc | Điểm mở rộng | Vị trí trong luồng (mô tả nghiệp vụ) | UC mở rộng | Điều kiện |
|---|---|---|---|---|
| UC-004 Đặt hàng | Chọn giao hàng nhanh | Sau khi thông tin giao hàng được xác nhận hợp lệ, trước khi tính phí giao hàng | UC-005 Đặt hàng giao nhanh | Khách hàng chọn giao hàng nhanh |

## 3. UC đề xuất bổ sung

Không có

## 4. Danh sách sơ đồ

| Sơ đồ | Phạm vi | Tác nhân | Use case | File |
|---|---|---|---|---|
| Tổng quát | Toàn hệ thống, đủ mọi quan hệ (N = 8 UC User-goal, M = 3 tác nhân, dưới ngưỡng 20 và 8) | ACT-01, ACT-02, ACT-03 | 10 (8 User-goal, 2 Subfunction) | diagrams/P03-usecase-overview.drawio |

## 5. Bảng mô hình của từng sơ đồ

### Tổng quát

<!--GEN:P03-overview-->
#### Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống thương mại điện tử AIMS | - | - | Subject | 200 | 40 | 600 | 1080 |
| ACT-01 | Actor | Khách hàng | - | - | Tác nhân chính | 60 | 410 | 30 | 60 |
| ACT-02 | Actor | Quản trị viên | - | - | Tác nhân chính | 60 | 950 | 30 | 60 |
| ACT-03 | Actor | Liên ngân hàng | «system» | - | Tác nhân phụ | 880 | 620 | 30 | 60 |
| UC-001 | UseCase | Tìm kiếm sản phẩm | - | SYS | - | 260 | 80 | 160 | 70 |
| UC-002 | UseCase | Thêm sản phẩm vào giỏ hàng | - | SYS | - | 260 | 190 | 160 | 70 |
| UC-003 | UseCase | Xem giỏ hàng | - | SYS | - | 260 | 300 | 160 | 70 |
| UC-004 | UseCase | Đặt hàng; extension points: Chọn giao hàng nhanh | - | SYS | UC gốc của RL-11, RL-12 | 260 | 410 | 200 | 90 |
| UC-005 | UseCase | Đặt hàng giao nhanh | - | SYS | Subfunction, UC mở rộng | 300 | 540 | 160 | 70 |
| UC-006 | UseCase | Thanh toán đơn hàng | - | SYS | Subfunction, UC được include | 560 | 420 | 160 | 70 |
| UC-007 | UseCase | Huỷ đơn hàng | - | SYS | - | 260 | 650 | 160 | 70 |
| UC-008 | UseCase | Xem lịch sử mua hàng | - | SYS | - | 260 | 760 | 160 | 70 |
| UC-009 | UseCase | Quản lý sản phẩm | - | SYS | - | 260 | 900 | 160 | 70 |
| UC-010 | UseCase | Duyệt đơn hàng | - | SYS | - | 260 | 1010 | 160 | 70 |
| N-01 | Note | Condition: {khách hàng chọn giao hàng nhanh}; extension point: Chọn giao hàng nhanh | - | - | Gắn vào RL-12 | 540 | 540 | 200 | 60 |

#### Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | - |
| RL-02 | ACT-01 | UC-002 | Association | - | - |
| RL-03 | ACT-01 | UC-003 | Association | - | - |
| RL-04 | ACT-01 | UC-004 | Association | - | - |
| RL-05 | ACT-03 | UC-006 | Association | - | - |
| RL-06 | ACT-01 | UC-007 | Association | - | - |
| RL-07 | ACT-03 | UC-007 | Association | - | - |
| RL-08 | ACT-01 | UC-008 | Association | - | - |
| RL-09 | ACT-02 | UC-009 | Association | - | - |
| RL-10 | ACT-02 | UC-010 | Association | - | - |
| RL-11 | UC-004 | UC-006 | Include | «include» | - |
| RL-12 | UC-005 | UC-004 | Extend | «extend» | - |
| RL-12-N | N-01 | RL-12 | NoteLink | - | Nối note N-01 vào đường «extend» |
<!--/GEN:P03-overview-->

## 6. Nội dung file .drawio

File diagrams/P03-usecase-overview.drawio được ghi trực tiếp (chạy bằng agent có quyền ghi file), sinh từ bảng Node và Edge ở mục 5.

## Câu hỏi mở

Không có

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- RL-11: Bước 3 cấm include cho "các bước tuần tự của một quy trình (phân rã chức năng)" và D-AP01 cấm "chuỗi UC nối nhau bằng include theo thứ tự thời gian". Thanh toán là bước thứ hai trong quy trình 5 bước của nguồn (REQ-42). Quan hệ vẫn được tạo vì UC-006 thoả Bước 3a theo điều kiện Q4c (tách phần rất lớn), là điều kiện Bước 3a cho phép tường minh; đây là chỗ hai quy tắc của Bước 3 cùng áp dụng được và cho kết luận ngược nhau.
- Phép thử che phủ (Bước 6): che UC-005, UC-006 vẫn còn các mục tiêu chính tìm sản phẩm, giỏ hàng, đặt hàng, huỷ đơn, lịch sử, quản lý sản phẩm, duyệt đơn. Đạt.
- Tỷ lệ UC Subfunction 2/10 = 20%, ở ngưỡng trên; không có dấu hiệu D-AP17 vì mỗi quan hệ có căn cứ riêng.
