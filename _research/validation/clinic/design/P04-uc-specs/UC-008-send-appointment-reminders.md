# P04 - Đặc tả use case UC-008 Nhắc lịch khám - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, yeu-cau-phong-kham.md, P00 1.0, P01 1.0, P02 1.0, P03 1.0, P04-uc-specs/_BR-register.md (sau UC-005) |
| Phạm vi | UC-008 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-008 |
| Tên use case | Nhắc lịch khám (Send Appointment Reminders) |
| Tác nhân chính | ACT-07 Bộ định thời |
| Tác nhân phụ | ACT-06 Cổng SMS |
| Mô tả ngắn | Use case này mô tả việc hệ thống, khi tới 18 giờ mỗi ngày, gửi SMS nhắc lịch cho bệnh nhân có lịch hẹn đã xác nhận vào ngày hôm sau. Kết quả là các bệnh nhân này nhận được tin nhắc lịch. |
| Sự kiện kích hoạt | Đến 18 giờ mỗi ngày (EV-19) |
| Tiền điều kiện | Không có |
| Hậu điều kiện (thành công) | Với mỗi lịch hẹn ở trạng thái "Đã xác nhận" có ngày khám là ngày hôm sau, một yêu cầu gửi SMS nhắc lịch đã được gửi tới Cổng SMS cho số điện thoại của bệnh nhân. |
| Hậu điều kiện tối thiểu | Không có thay đổi dữ liệu lịch hẹn. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-26, REQ-46 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Bộ định thời | Tới 18 giờ hằng ngày. |
| 2 | Hệ thống | Xác định các lịch hẹn ở trạng thái "Đã xác nhận" có ngày khám là ngày hôm sau (BR-06). |
| 3 | Hệ thống | Với mỗi lịch hẹn đã xác định, gửi SMS nhắc lịch tới số điện thoại của bệnh nhân qua Cổng SMS. |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Không có lịch hẹn nào ở trạng thái "Đã xác nhận" vào ngày hôm sau | Hệ thống | Kết thúc lượt nhắc lịch, không gửi SMS. | Kết thúc use case (thành công) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Không có (nội dung tin nhắc lịch chưa được nguồn quy định, xem Q-28).

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-06 | Lúc 18 giờ mỗi ngày, mỗi lịch hẹn ở trạng thái "Đã xác nhận" có ngày khám là ngày hôm sau được nhắc lịch bằng SMS. | Kích hoạt hành động | 1, 2, 3 | REQ-26 | Mới |

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Bệnh nhân là bên hưởng lợi, không phải tác nhân của use case này (P01 Mục 3).

## 9. Activity diagram

File: diagrams/P04-activity-UC-008.drawio

Theo F10.2, bước 1 là AcceptTimeEvent trong partition hệ thống, không có partition cho ACT-07. ACT-06 chỉ nhận yêu cầu nên không có partition (F10.4).

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-SYS | Partition | Hệ thống | - | - | - | - | 0 | 0 | 560 | 820 |
| INIT | Initial | - | - | P-SYS | - | - | 140 | 80 | 30 | 30 |
| A-1 | AcceptTimeEvent | Tới 18 giờ hằng ngày | - | P-SYS | 1 | - | 70 | 150 | 180 | 60 |
| A-2 | Action | Xác định lịch hẹn đã xác nhận của ngày hôm sau | - | P-SYS | 2 | - | 70 | 240 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | - | - | 140 | 340 | 40 | 40 |
| A-2a | Action | Kết thúc lượt nhắc, không gửi SMS | - | P-SYS | 2a | - | 330 | 330 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | - | 400 | 440 | 30 | 30 |
| M-3 | Merge | - | - | P-SYS | - | - | 140 | 430 | 40 | 40 |
| A-3 | Action | Gửi SMS nhắc lịch cho một lịch hẹn qua Cổng SMS | - | P-SYS | 3 | - | 70 | 510 | 180 | 60 |
| D-3 | Decision | - | - | P-SYS | - | - | 140 | 610 | 40 | 40 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - | 140 | 700 | 30 | 30 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - |
| E-03 | A-2 | D-2 | ControlFlow | - | - |
| E-04 | D-2 | A-2a | ControlFlow | [không có lịch hẹn cần nhắc] | - |
| E-05 | A-2a | FINAL-2 | ControlFlow | - | - |
| E-06 | D-2 | M-3 | ControlFlow | [có lịch hẹn cần nhắc] | - |
| E-07 | M-3 | A-3 | ControlFlow | - | - |
| E-08 | A-3 | D-3 | ControlFlow | - | - |
| E-09 | D-3 | M-3 | ControlFlow | [còn] | - |
| E-10 | D-3 | FINAL-1 | ControlFlow | [hết] | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a | A-2a |
| 3 | A-3 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-28 | Tin nhắc lịch gồm những thông tin nào (ngày giờ, bác sĩ, chuyên khoa, địa chỉ)? | Dữ liệu ra | REQ-26 |
| Q-29 | Khi Cổng SMS không nhận yêu cầu gửi cho một lịch hẹn, hệ thống có gửi lại hoặc báo cho lễ tân không? | Luồng thay thế tại bước 3 | REQ-26, REQ-46 |
| Q-30 | Hệ thống có cần ghi lại lịch hẹn nào đã được nhắc không? | Hậu điều kiện | REQ-26 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Luồng chính có 3 bước, ở ngưỡng dưới của F4.4; không đề xuất sửa P02 vì mục tiêu nghiệp vụ trọn vẹn.
- F4.2 mục 2 yêu cầu cột "Thực hiện bởi" ghi tên tác nhân (bước 1 ghi Bộ định thời), còn F10.4 yêu cầu mỗi chủ thể trong cột này có một partition. Theo F10.2, không tạo partition cho tác nhân thời gian; đã chọn F10.2 vì quy tắc riêng hơn.
- Luồng 2a có hành động "không gửi SMS" chỉ để giữ ánh xạ 1-1 giữa hàng luồng thay thế và action.
