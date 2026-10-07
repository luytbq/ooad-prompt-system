# P04 - Đặc tả use case UC-009 Ghi nhận xe thất lạc - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-dap.md; P00 1.0; P01 1.0; P02 1.0; P03 1.0 (Mục 1, Mục 2); _BR-register.md (sau UC-007); Câu hỏi mở của UC-005, UC-007 |
| Phạm vi | UC-009 |

Placeholder: UC_ID = UC-009; TEN_HE_THONG_TRONG_LUONG = Không có; YEU_CAU_BO_SUNG = Không có.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-009 |
| Tên use case | Ghi nhận xe thất lạc (Record Lost Bike) |
| Tác nhân chính | ACT-09 Bộ định thời |
| Tác nhân phụ | ACT-07 Cổng thanh toán |
| Mô tả ngắn | Use case này mô tả việc hệ thống xử lý một chuyến đi kéo dài quá 24 giờ. Kết quả là xe được coi là thất lạc, toàn bộ tiền tạm giữ được thu và tài khoản người thuê xe bị khoá. |
| Sự kiện kích hoạt | Chuyến đi đạt 24 giờ (EV-09) |
| Tiền điều kiện | Chuyến đi đang diễn ra và có khoản tạm giữ còn hiệu lực. |
| Hậu điều kiện (thành công) | Xe của chuyến đi được đánh dấu thất lạc.<br>Toàn bộ khoản tạm giữ của chuyến đã được thu.<br>Tài khoản của người thuê xe ở trạng thái bị khoá. |
| Hậu điều kiện tối thiểu | Chưa quy định (Q-23) |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-28, REQ-29, REQ-30, REQ-31, REQ-32, REQ-62 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Hệ thống | Tới thời điểm một chuyến đi kéo dài quá 24 giờ (BR-09). |
| 2 | Hệ thống | Đánh dấu xe của chuyến đi là thất lạc. |
| 3 | Hệ thống | Yêu cầu Cổng thanh toán thu toàn bộ số tiền tạm giữ của chuyến đi (BR-10). |
| 4 | Hệ thống | Khoá tài khoản của người thuê xe (BR-10). |

## 3. Luồng sự kiện thay thế và ngoại lệ

Không có (lỗi thu tạm giữ chờ Q-23).

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Không có

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-09 | Chuyến đi kéo dài quá 24 giờ thì xe của chuyến bị coi là thất lạc. | Suy luận | 1 | REQ-28, REQ-29 | Mới |
| BR-10 | Khi xe bị coi là thất lạc, toàn bộ số tiền tạm giữ của chuyến bị thu và tài khoản của người thuê xe bị khoá. | Kích hoạt hành động | 3, 4 | REQ-30, REQ-31 | Mới |

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Sau use case này nhân viên chăm sóc khách hàng "xử lý tiếp" (REQ-32); nội dung chờ Q-03. Mở khoá tài khoản thuộc UC-018.
- Chuyến đi có kết thúc ở bước nào không chờ Q-04.

## 8a. Kịch bản chính

- KB1: Luồng chính --> xe thất lạc, thu toàn bộ tạm giữ, khoá tài khoản.

## 9. Activity diagram

File: diagrams/P04-activity-UC-009.drawio

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú |
|---|---|---|---|---|---|---|
| P-SYS | Partition | Hệ thống | - | - | - | x=0, w=400, h=580 |
| INIT | Initial | - | - | P-SYS | - | - |
| A-1 | AcceptTimeEvent | Tới khi chuyến đi quá 24 giờ | - | P-SYS | 1 | - |
| A-2 | Action | Đánh dấu xe thất lạc | - | P-SYS | 2 | - |
| A-3 | Action | Yêu cầu thu toàn bộ tiền tạm giữ | - | P-SYS | 3 | - |
| A-4 | Action | Khoá tài khoản người thuê xe | - | P-SYS | 4 | - |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - | - |
| E-03 | A-2 | A-3 | ControlFlow | - | - | - |
| E-04 | A-3 | A-4 | ControlFlow | - | - | - |
| E-05 | A-4 | FINAL-1 | ControlFlow | - | - | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 3 | A-3 |
| 4 | A-4 |

## Câu hỏi mở

Không có câu hỏi mới. Liên quan: Q-03, Q-04, Q-23.

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Luồng chính có 4 bước, mọi bước do hệ thống thực hiện; không có luồng thay thế nào có căn cứ trong nguồn.
