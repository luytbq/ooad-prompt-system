# P04 - Đặc tả use case UC-005 Đặt lịch khám cho bệnh nhân - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, yeu-cau-phong-kham.md, P00 1.0, P01 1.0, P02 1.0, P03 1.0, P04-uc-specs/_BR-register.md (sau UC-004), P04-uc-specs/UC-004-book-appointment.md |
| Phạm vi | UC-005 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-005 |
| Tên use case | Đặt lịch khám cho bệnh nhân (Book Appointment for Patient) |
| Tác nhân chính | ACT-02 Lễ tân |
| Tác nhân phụ | Không có |
| Mô tả ngắn | Use case này mô tả tương tác giữa lễ tân và hệ thống khi lễ tân muốn đặt lịch khám thay cho bệnh nhân gọi điện tới phòng khám. Kết quả là bệnh nhân có một lịch hẹn đã được xác nhận. |
| Sự kiện kích hoạt | Bệnh nhân gọi điện tới phòng khám để đặt lịch (EV-07) |
| Tiền điều kiện | Lễ tân đã được xác thực và đang có phiên làm việc. |
| Hậu điều kiện (thành công) | Có một lịch hẹn mới của bệnh nhân với chuyên khoa, bác sĩ, ngày, khung giờ và lý do khám đã chọn, ở trạng thái "Đã xác nhận" (BR-05).<br>Nếu bệnh nhân chưa có tài khoản hoặc hồ sơ, có một hồ sơ bệnh nhân mới gồm họ tên, ngày sinh, số điện thoại. |
| Hậu điều kiện tối thiểu | Không có lịch hẹn nào được tạo. Hồ sơ bệnh nhân tạo ở luồng 2a (nếu có) vẫn được giữ (Q-27). |
| Quan hệ | «include» UC-006 Chọn khung giờ khám (tại bước 4) |
| Điểm mở rộng | Không có |
| REQ | REQ-09, REQ-22, REQ-23, REQ-24, REQ-25 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Lễ tân | Yêu cầu đặt lịch khám cho bệnh nhân và cung cấp số điện thoại của bệnh nhân (Q-24). |
| 2 | Hệ thống | Tìm và hiển thị bệnh nhân có tài khoản hoặc hồ sơ ứng với số điện thoại đã cung cấp. |
| 3 | Lễ tân | Xác nhận bệnh nhân cần đặt lịch. |
| 4 | Hệ thống | Gọi use case UC-006 Chọn khung giờ khám để lễ tân chọn chuyên khoa, bác sĩ (hoặc để phòng khám tự phân), ngày và khung giờ còn trống. |
| 5 | Lễ tân | Nhập và gửi lý do khám (xem Dữ liệu vào 2). |
| 6 | Hệ thống | Kiểm tra khung giờ đã chọn vẫn còn trống. |
| 7 | Hệ thống | Tạo lịch hẹn ở trạng thái "Đã xác nhận" (BR-05). |
| 8 | Hệ thống | Hiển thị thông tin lịch hẹn vừa tạo. |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Không tìm thấy bệnh nhân ứng với số điện thoại | - | Tạo hồ sơ bệnh nhân mới | - |
| 2a1 | | Lễ tân | Nhập và gửi họ tên, ngày sinh, số điện thoại của bệnh nhân (xem Dữ liệu vào 1). | |
| 2a2 | | Hệ thống | Tạo hồ sơ bệnh nhân. | Tiếp tục bước 4 |
| 4a | UC-006 trả kết quả thất bại (không chọn được khung giờ) | Hệ thống | Thông báo chưa chọn được khung giờ khám. | Kết thúc use case (thất bại) |
| 6a | Khung giờ đã chọn không còn trống | Hệ thống | Thông báo khung giờ không còn trống. | Quay lại bước 4 |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 2a1)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Họ tên | Họ tên bệnh nhân | Chưa quy định (Q-26) | Chưa quy định (Q-26) | Nguyễn Thị Lan |
| 2 | Ngày sinh | Ngày sinh bệnh nhân | Chưa quy định (Q-26) | Chưa quy định (Q-26) | 12/03/1950 |
| 3 | Số điện thoại | Số điện thoại liên lạc, dùng nhận SMS | Chưa quy định (Q-26) | Chưa quy định (Q-26) | 0912345678 |

Dữ liệu vào 2 (bước 5)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Lý do khám | Lý do bệnh nhân muốn khám, do lễ tân ghi theo lời bệnh nhân | Chưa quy định (Q-25) | Chưa quy định (Q-23) | Ho kéo dài 2 tuần |

Dữ liệu ra: như Dữ liệu ra 1 của UC-004, trạng thái là "Đã xác nhận".

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-05 | Lịch hẹn do lễ tân đặt có trạng thái ban đầu "Đã xác nhận". | Kích hoạt hành động | 7 | REQ-25 | Mới |

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Nguồn gọi người dùng của use case này là "bệnh nhân gọi điện" và cho biết "nhiều người lớn tuổi vẫn gọi điện thoại" (mục 6).

## 9. Activity diagram

File: diagrams/P04-activity-UC-005.drawio

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-02 | Partition | Lễ tân | - | - | - | - | 0 | 0 | 520 | 1540 |
| P-SYS | Partition | Hệ thống | - | - | - | - | 520 | 0 | 640 | 1540 |
| INIT | Initial | - | - | P-ACT-02 | - | - | 120 | 80 | 30 | 30 |
| A-1 | Action | Yêu cầu đặt lịch hộ, cung cấp số điện thoại bệnh nhân | - | P-ACT-02 | 1 | - | 50 | 150 | 180 | 60 |
| A-2 | Action | Tìm bệnh nhân theo số điện thoại | - | P-SYS | 2 | - | 70 | 240 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | - | - | 140 | 340 | 40 | 40 |
| A-2a1 | Action | Nhập họ tên, ngày sinh, số điện thoại | - | P-ACT-02 | 2a1 | - | 310 | 420 | 180 | 60 |
| A-2a2 | Action | Tạo hồ sơ bệnh nhân | - | P-SYS | 2a2 | - | 330 | 510 | 180 | 60 |
| A-3 | Action | Xác nhận bệnh nhân cần đặt lịch | - | P-ACT-02 | 3 | - | 50 | 600 | 180 | 60 |
| M-4 | Merge | - | - | P-SYS | - | - | 140 | 700 | 40 | 40 |
| A-4 | CallBehaviorAction | UC-006 Chọn khung giờ khám | - | P-SYS | 4 | - | 70 | 780 | 180 | 60 |
| D-4 | Decision | - | - | P-SYS | - | - | 140 | 880 | 40 | 40 |
| A-4a | Action | Thông báo chưa chọn được khung giờ | - | P-SYS | 4a | - | 330 | 870 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | - | 560 | 880 | 30 | 30 |
| A-5 | Action | Nhập và gửi lý do khám | - | P-ACT-02 | 5 | - | 50 | 960 | 180 | 60 |
| A-6 | Action | Kiểm tra khung giờ còn trống | - | P-SYS | 6 | - | 70 | 1050 | 180 | 60 |
| D-6 | Decision | - | - | P-SYS | - | - | 140 | 1150 | 40 | 40 |
| A-6a | Action | Thông báo khung giờ không còn trống | - | P-SYS | 6a | - | 330 | 1140 | 180 | 60 |
| A-7 | Action | Tạo lịch hẹn "Đã xác nhận" | - | P-SYS | 7 | - | 70 | 1230 | 180 | 60 |
| A-8 | Action | Hiển thị thông tin lịch hẹn | - | P-SYS | 8 | - | 70 | 1320 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - | 140 | 1420 | 30 | 30 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - |
| E-03 | A-2 | D-2 | ControlFlow | - | - |
| E-04 | D-2 | A-3 | ControlFlow | [tìm thấy bệnh nhân] | - |
| E-05 | D-2 | A-2a1 | ControlFlow | [không tìm thấy bệnh nhân] | - |
| E-06 | A-2a1 | A-2a2 | ControlFlow | - | - |
| E-07 | A-2a2 | M-4 | ControlFlow | - | - |
| E-08 | A-3 | M-4 | ControlFlow | - | - |
| E-09 | M-4 | A-4 | ControlFlow | - | - |
| E-10 | A-4 | D-4 | ControlFlow | - | - |
| E-11 | D-4 | A-4a | ControlFlow | [UC-006 thất bại] | - |
| E-12 | A-4a | FINAL-2 | ControlFlow | - | - |
| E-13 | D-4 | A-5 | ControlFlow | [đã chọn khung giờ] | - |
| E-14 | A-5 | A-6 | ControlFlow | - | - |
| E-15 | A-6 | D-6 | ControlFlow | - | - |
| E-16 | D-6 | A-6a | ControlFlow | [khung giờ không còn trống] | - |
| E-17 | A-6a | M-4 | ControlFlow | - | - |
| E-18 | D-6 | A-7 | ControlFlow | [khung giờ còn trống] | - |
| E-19 | A-7 | A-8 | ControlFlow | - | - |
| E-20 | A-8 | FINAL-1 | ControlFlow | - | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a1 | A-2a1 |
| 2a2 | A-2a2 |
| 3 | A-3 |
| 4 | A-4 |
| 4a | A-4a |
| 5 | A-5 |
| 6 | A-6 |
| 6a | A-6a |
| 7 | A-7 |
| 8 | A-8 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-24 | Lễ tân tìm bệnh nhân bằng thông tin nào (số điện thoại / họ tên và ngày sinh)? | Bước 1, 2 | REQ-22, REQ-23 |
| Q-25 | Lịch do lễ tân đặt có bắt buộc lý do khám không? | Dữ liệu vào 2 | REQ-09, REQ-22 |
| Q-26 | Ba trường của hồ sơ bệnh nhân có bắt buộc không, định dạng số điện thoại và ngày sinh thế nào, số điện thoại có phải duy nhất không? | Dữ liệu vào 1 | REQ-24 |
| Q-27 | Khi lễ tân đã tạo hồ sơ nhưng không đặt được lịch (luồng 4a), hồ sơ có được giữ không? | Hậu điều kiện tối thiểu | REQ-23 |

Các câu hỏi đã có ở P00 và ảnh hưởng tới use case này: Q-06 (giới hạn 14 ngày), Q-07 (BR-02 có áp dụng khi lễ tân đặt không), Q-08 (bệnh nhân bị khoá có được đặt hộ không), Q-10 (có gửi SMS xác nhận không), Q-11 (quan hệ hồ sơ và tài khoản). Vì Q-07, Q-08 chưa có câu trả lời, luồng chính chưa kiểm tra BR-02 và BR-04.

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Bước 1 gộp yêu cầu và cung cấp số điện thoại theo F4.2 mục 4; cách tìm bệnh nhân chờ Q-24.
