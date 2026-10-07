# P04 - Đặc tả use case UC-004 Đặt lịch khám - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, yeu-cau-phong-kham.md, P00 1.0, P01 1.0, P02 1.0, P03 1.0 |
| Phạm vi | UC-004 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-004 |
| Tên use case | Đặt lịch khám (Book Appointment) |
| Tác nhân chính | ACT-01 Bệnh nhân |
| Tác nhân phụ | Không có |
| Mô tả ngắn | Use case này mô tả tương tác giữa bệnh nhân và hệ thống khi bệnh nhân muốn tự đặt một lịch khám trực tuyến. Kết quả là bệnh nhân có một lịch hẹn ở trạng thái "Chờ xác nhận" với bác sĩ và khung giờ đã chọn. |
| Sự kiện kích hoạt | Bệnh nhân muốn đặt lịch khám (EV-03) |
| Tiền điều kiện | Bệnh nhân có tài khoản đã được xác thực và đang có phiên làm việc (BR-01). |
| Hậu điều kiện (thành công) | Có một lịch hẹn mới của bệnh nhân với chuyên khoa, bác sĩ, ngày, khung giờ và lý do khám đã chọn, ở trạng thái "Chờ xác nhận" (BR-03).<br>Khung giờ đã chọn không còn trống. |
| Hậu điều kiện tối thiểu | Không có thay đổi dữ liệu nào được lưu. |
| Quan hệ | «include» UC-006 Chọn khung giờ khám (tại bước 3) |
| Điểm mở rộng | Không có |
| REQ | REQ-06, REQ-09, REQ-10, REQ-11, REQ-12, REQ-13, REQ-30, REQ-43 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Bệnh nhân | Yêu cầu đặt lịch khám. |
| 2 | Hệ thống | Kiểm tra bệnh nhân không bị khoá chức năng tự đặt lịch trực tuyến (BR-04) và số lịch hẹn chưa diễn ra của bệnh nhân dưới 2 (BR-02). |
| 3 | Hệ thống | Gọi use case UC-006 Chọn khung giờ khám để bệnh nhân chọn chuyên khoa, bác sĩ (hoặc để phòng khám tự phân), ngày và khung giờ còn trống. |
| 4 | Bệnh nhân | Nhập và gửi lý do khám (xem Dữ liệu vào 1). |
| 5 | Hệ thống | Kiểm tra khung giờ đã chọn vẫn còn trống. |
| 6 | Hệ thống | Tạo lịch hẹn ở trạng thái "Chờ xác nhận" (BR-03). |
| 7 | Hệ thống | Hiển thị thông tin lịch hẹn vừa tạo (xem Dữ liệu ra 1). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Bệnh nhân đang bị khoá chức năng tự đặt lịch trực tuyến (BR-04) | Hệ thống | Thông báo bệnh nhân đang bị khoá chức năng tự đặt lịch trực tuyến. | Kết thúc use case (thất bại) |
| 2b | Bệnh nhân không bị khoá và đã có 2 lịch hẹn chưa diễn ra (BR-02) | Hệ thống | Thông báo bệnh nhân đã có đủ 2 lịch hẹn chưa diễn ra. | Kết thúc use case (thất bại) |
| 3a | UC-006 trả kết quả thất bại (không chọn được khung giờ) | Hệ thống | Thông báo chưa chọn được khung giờ khám. | Kết thúc use case (thất bại) |
| 5a | Khung giờ đã chọn không còn trống | Hệ thống | Thông báo khung giờ không còn trống. | Quay lại bước 3 |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 4)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Lý do khám | Lý do bệnh nhân muốn khám | Chưa quy định (Q-23) | Chưa quy định (Q-23) | Nổi mẩn đỏ ở tay 3 ngày |

Dữ liệu ra 1 (bước 7)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Chuyên khoa | Chuyên khoa đã chọn | Văn bản | Da liễu |
| 2 | Bác sĩ | Bác sĩ đã chọn hoặc được phân | Văn bản; cách hiển thị khi phòng khám tự phân chờ Q-01 | BS. Trần Văn B |
| 3 | Ngày khám | Ngày của lịch hẹn | dd/mm/yyyy | 05/10/2026 |
| 4 | Khung giờ | Khung giờ 30 phút | hh:mm - hh:mm | 09:00 - 09:30 |
| 5 | Lý do khám | Lý do đã nhập | Văn bản | Nổi mẩn đỏ ở tay 3 ngày |
| 6 | Trạng thái | Trạng thái lịch hẹn | Văn bản | Chờ xác nhận |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-01 | Bệnh nhân phải có tài khoản để tự đặt lịch khám. | Ràng buộc | Tiền điều kiện | REQ-06 | Mới |
| BR-02 | Mỗi bệnh nhân không được có quá 2 lịch hẹn chưa diễn ra cùng lúc. | Ràng buộc | 2, 2b | REQ-12 | Mới |
| BR-03 | Lịch hẹn do bệnh nhân tự đặt có trạng thái ban đầu "Chờ xác nhận". | Kích hoạt hành động | 6 | REQ-13 | Mới |
| BR-04 | Bệnh nhân bị đánh dấu "Không đến" 3 lần trong 6 tháng bị khoá chức năng tự đặt lịch trực tuyến. | Suy luận | 2, 2a | REQ-30 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Thao tác đặt lịch phản hồi trong không quá 3 giây khi có 200 người dùng đồng thời | Performance | REQ-43 |

## 8. Thông tin bổ sung

Không có

## 9. Activity diagram

File: diagrams/P04-activity-UC-004.drawio

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Bệnh nhân | - | - | - | - | 0 | 0 | 280 | 1360 |
| P-SYS | Partition | Hệ thống | - | - | - | - | 280 | 0 | 640 | 1360 |
| INIT | Initial | - | - | P-ACT-01 | - | - | 120 | 80 | 30 | 30 |
| A-1 | Action | Yêu cầu đặt lịch khám | - | P-ACT-01 | 1 | - | 50 | 150 | 180 | 60 |
| A-2 | Action | Kiểm tra trạng thái khoá và số lịch hẹn chưa diễn ra | - | P-SYS | 2 | - | 70 | 240 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | - | - | 140 | 340 | 40 | 40 |
| A-2a | Action | Thông báo bị khoá tự đặt lịch | - | P-SYS | 2a | - | 330 | 330 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | - | 560 | 340 | 30 | 30 |
| A-2b | Action | Thông báo đã có đủ 2 lịch hẹn chưa diễn ra | - | P-SYS | 2b | - | 330 | 420 | 180 | 60 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | - | - | 560 | 440 | 30 | 30 |
| M-3 | Merge | - | - | P-SYS | - | - | 140 | 520 | 40 | 40 |
| A-3 | CallBehaviorAction | UC-006 Chọn khung giờ khám | - | P-SYS | 3 | - | 70 | 600 | 180 | 60 |
| D-3 | Decision | - | - | P-SYS | - | - | 140 | 700 | 40 | 40 |
| A-3a | Action | Thông báo chưa chọn được khung giờ | - | P-SYS | 3a | - | 330 | 690 | 180 | 60 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | - | - | 560 | 700 | 30 | 30 |
| A-4 | Action | Nhập và gửi lý do khám | - | P-ACT-01 | 4 | - | 50 | 780 | 180 | 60 |
| A-5 | Action | Kiểm tra khung giờ còn trống | - | P-SYS | 5 | - | 70 | 870 | 180 | 60 |
| D-5 | Decision | - | - | P-SYS | - | - | 140 | 970 | 40 | 40 |
| A-5a | Action | Thông báo khung giờ không còn trống | - | P-SYS | 5a | - | 330 | 960 | 180 | 60 |
| A-6 | Action | Tạo lịch hẹn "Chờ xác nhận" | - | P-SYS | 6 | - | 70 | 1050 | 180 | 60 |
| A-7 | Action | Hiển thị thông tin lịch hẹn | - | P-SYS | 7 | - | 70 | 1140 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - | 140 | 1240 | 30 | 30 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - |
| E-03 | A-2 | D-2 | ControlFlow | - | - |
| E-04 | D-2 | A-2a | ControlFlow | [bị khoá tự đặt lịch] | - |
| E-05 | A-2a | FINAL-2 | ControlFlow | - | - |
| E-06 | D-2 | A-2b | ControlFlow | [không khoá, đủ 2 lịch] | - |
| E-07 | A-2b | FINAL-3 | ControlFlow | - | - |
| E-08 | D-2 | M-3 | ControlFlow | [khác] | - |
| E-09 | M-3 | A-3 | ControlFlow | - | - |
| E-10 | A-3 | D-3 | ControlFlow | - | - |
| E-11 | D-3 | A-3a | ControlFlow | [UC-006 thất bại] | - |
| E-12 | A-3a | FINAL-4 | ControlFlow | - | - |
| E-13 | D-3 | A-4 | ControlFlow | [đã chọn khung giờ] | - |
| E-14 | A-4 | A-5 | ControlFlow | - | - |
| E-15 | A-5 | D-5 | ControlFlow | - | - |
| E-16 | D-5 | A-5a | ControlFlow | [khung giờ không còn trống] | - |
| E-17 | A-5a | M-3 | ControlFlow | - | - |
| E-18 | D-5 | A-6 | ControlFlow | [khung giờ còn trống] | - |
| E-19 | A-6 | A-7 | ControlFlow | - | - |
| E-20 | A-7 | FINAL-1 | ControlFlow | - | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a | A-2a |
| 2b | A-2b |
| 3 | A-3 |
| 3a | A-3a |
| 4 | A-4 |
| 5 | A-5 |
| 5a | A-5a |
| 6 | A-6 |
| 7 | A-7 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-23 | Lý do khám có bắt buộc không, có giới hạn độ dài không? | Dữ liệu vào 1, bước 4 | REQ-09 |

Các câu hỏi đã có ở P00 và ảnh hưởng tới use case này: Q-01 (cách phân bác sĩ, trong UC-006), Q-06 (giới hạn 14 ngày), Q-07 (lịch "Chờ xác nhận" có tính vào BR-02 không), Q-19 (số bệnh nhân mỗi khung giờ, ảnh hưởng bước 5).

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Bước 5 kiểm tra khung giờ còn trống suy ra từ "khung giờ 30 phút còn trống" (REQ-09). Nghĩa của "còn trống" phụ thuộc Q-19.
