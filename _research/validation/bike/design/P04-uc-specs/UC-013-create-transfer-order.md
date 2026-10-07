# P04 - Đặc tả use case UC-013 Lập lệnh điều chuyển - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-dap.md; P00 1.0; P01 1.0; P02 1.0; P03 1.0 (Mục 1, Mục 2); _BR-register.md (sau UC-009); Câu hỏi mở của UC-005, UC-007, UC-009 |
| Phạm vi | UC-013 |

Placeholder: UC_ID = UC-013; TEN_HE_THONG_TRONG_LUONG = Không có; YEU_CAU_BO_SUNG = Không có.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-013 |
| Tên use case | Lập lệnh điều chuyển (Create Transfer Order) |
| Tác nhân chính | ACT-04 Nhân viên điều phối |
| Tác nhân phụ | Không có |
| Mô tả ngắn | Use case này mô tả tương tác giữa nhân viên điều phối và hệ thống khi nhân viên điều phối muốn chuyển xe giữa các trạm. Kết quả là một lệnh điều chuyển được ghi nhận để theo dõi tới khi hoàn tất. |
| Sự kiện kích hoạt | Nhân viên điều phối quyết định chuyển xe giữa hai trạm (EV-14) |
| Tiền điều kiện | Nhân viên điều phối đã được xác thực. |
| Hậu điều kiện (thành công) | Có một lệnh điều chuyển mới ở trạng thái chưa hoàn tất, ghi trạm lấy xe và trạm nhận xe. |
| Hậu điều kiện tối thiểu | Không có thay đổi dữ liệu nào được lưu. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-44, REQ-45, REQ-46 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Nhân viên điều phối | Yêu cầu lập lệnh điều chuyển. |
| 2 | Nhân viên điều phối | Chỉ định trạm lấy xe, trạm nhận xe và xe cần điều chuyển (xem Dữ liệu vào 1). |
| 3 | Hệ thống | Tạo lệnh điều chuyển ở trạng thái chưa hoàn tất. |

## 3. Luồng sự kiện thay thế và ngoại lệ

Không có

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 2)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Trạm lấy xe | Trạm có xe cần chuyển đi | Chưa quy định (Q-25) | Chưa quy định (Q-25) | Trạm Kim Mã |
| 2 | Trạm nhận xe | Trạm cần nhận thêm xe | Chưa quy định (Q-25) | Chưa quy định (Q-25) | Trạm Hồ Gươm |
| 3 | Xe cần điều chuyển | Số lượng xe hoặc danh sách xe cụ thể | Chưa quy định (Q-25) | Chưa quy định (Q-25) | 5 xe |

## 6. Quy tắc nghiệp vụ

Không có

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Lệnh điều chuyển được cập nhật tự động khi nhân viên lấy, đưa xe bằng thẻ nhân viên (UC-014, REQ-46) và được theo dõi ở UC-015; điều kiện hoàn tất chờ Q-09.
- Trạm sắp hết xe, sắp đầy (UC-012) là căn cứ để lập lệnh nhưng nguồn không nói lệnh phải chọn trong các trạm đó.

## 8a. Kịch bản chính

- KB1: Luồng chính --> lệnh điều chuyển được tạo.

## 9. Activity diagram

File: diagrams/P04-activity-UC-013.drawio

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú |
|---|---|---|---|---|---|---|
| P-ACT-04 | Partition | Nhân viên điều phối | - | - | - | x=0, w=280, h=480 |
| P-SYS | Partition | Hệ thống | - | - | - | x=280, w=280, h=480 |
| INIT | Initial | - | - | P-ACT-04 | - | - |
| A-1 | Action | Yêu cầu lập lệnh điều chuyển | - | P-ACT-04 | 1 | - |
| A-2 | Action | Chỉ định trạm lấy xe, trạm nhận xe, xe | - | P-ACT-04 | 2 | - |
| A-3 | Action | Tạo lệnh điều chuyển chưa hoàn tất | - | P-SYS | 3 | - |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - | - |
| E-03 | A-2 | A-3 | ControlFlow | - | Vượt partition | (140,300); (420,300) |
| E-04 | A-3 | FINAL-1 | ControlFlow | - | - | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 3 | A-3 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-25 | Lệnh điều chuyển gồm những thông tin nào: trạm lấy xe, trạm nhận xe, số lượng xe hay danh sách xe cụ thể, nhân viên thực hiện? Trường nào bắt buộc? | UC-013 Dữ liệu vào 1, UC-014, UC-015 | "lập lệnh điều chuyển xe giữa các trạm" (Mục 9) |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-013 | Luồng chính chỉ có 3 bước vì nguồn chỉ có một câu về việc lập lệnh; UC có thể quá nhỏ (F4.4) | Giữ UC-013; xét lại sau khi Q-25 được trả lời |

## Vấn đề còn mở

- Ví dụ trong Dữ liệu vào 1 là tên trạm và số xe minh hoạ, không lấy từ nguồn.
