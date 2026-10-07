# P01 - Xác định tác nhân - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P01 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, P00-problem-brief.md 1.0, yeu-cau-phong-kham.md |
| Phạm vi | Toàn hệ thống |

## 1. Ranh giới hệ thống

Hệ thống cần xây dựng là Hệ thống đặt lịch khám ClinicBook, một phần mềm web (REQ-01) dùng cho bệnh nhân, lễ tân, bác sĩ, quản trị viên và quản lý phòng khám.

| Thành phần | Trong / Ngoài | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
|---|---|---|---|
| Phần mềm web ClinicBook (giao diện dùng trên máy tính và điện thoại) | Trong | REQ-01, REQ-44 | Là thành phần nội bộ, không phải tác nhân |
| Dữ liệu lịch hẹn, hồ sơ bệnh nhân, lịch làm việc do ClinicBook lưu | Trong | REQ-09, REQ-24, REQ-35 | Là thành phần nội bộ, không phải tác nhân |
| SMS Gateway của nhà mạng | Ngoài | REQ-46; quyết định ranh giới đã chốt | Là tác nhân ACT-06 |
| Điện thoại di động của người dùng | Ngoài | REQ-44, REQ-08 | Thiết bị người dùng dùng để thao tác và nhận SMS; không phải tác nhân |
| Sổ ghi lịch của lễ tân (cách làm hiện tại) | Ngoài | Đoạn mở đầu: "lễ tân ghi sổ" | Cách làm được thay thế, không trao đổi dữ liệu với hệ thống; không phải tác nhân |
| Cuộc gọi điện thoại của bệnh nhân tới lễ tân | Ngoài | REQ-22 | Kênh giữa hai người, không qua hệ thống; không phải tác nhân |

## 2. Bảng tác nhân

| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |
|---|---|---|---|---|---|---|---|---|
| ACT-01 | Bệnh nhân | Patient | Người | Chính | Người có nhu cầu khám tại phòng khám, tự thao tác trên hệ thống qua trình duyệt. Gồm cả người chưa có tài khoản (chỉ xem thông tin, đăng ký tài khoản) và người đã có tài khoản | Xem chuyên khoa, bác sĩ, lịch trống<br>Đăng ký tài khoản<br>Đặt lịch khám<br>Hủy lịch hẹn | - | REQ-02 đến REQ-12, REQ-19, REQ-20, REQ-45 |
| ACT-02 | Lễ tân | Receptionist | Người | Chính | Nhân viên tiếp đón của phòng khám, xử lý lịch hẹn và tiếp nhận bệnh nhân gọi điện | Xác nhận hoặc từ chối lịch hẹn chờ<br>Đặt lịch hộ bệnh nhân gọi điện<br>Hủy lịch hẹn sát giờ khám<br>Ghi nhận bệnh nhân đến hoặc không đến<br>Nắm các lịch hẹn bị ảnh hưởng khi bác sĩ khoá khung giờ | - | REQ-14 đến REQ-17, REQ-21 đến REQ-25, REQ-27 đến REQ-29, REQ-37 |
| ACT-03 | Bác sĩ | Doctor | Người | Chính | Bác sĩ thuộc một chuyên khoa của phòng khám | Xem lịch hẹn của mình theo ngày<br>Ghi kết luận khám<br>Đăng ký lịch làm việc tuần<br>Khoá khung giờ đột xuất | - | REQ-31 đến REQ-36, REQ-45 |
| ACT-04 | Quản trị viên | Administrator | Người | Chính | Người quản trị hệ thống của phòng khám | Quản lý chuyên khoa<br>Quản lý tài khoản bác sĩ và lễ tân<br>Cấu hình tham số nghiệp vụ | - | REQ-38 đến REQ-41 |
| ACT-05 | Quản lý phòng khám | Clinic Manager | Người | Chính | Người quản lý điều hành phòng khám | Xem báo cáo lịch hẹn hằng tháng | - | REQ-42 |
| ACT-06 | Cổng SMS | SMS Gateway | Hệ thống ngoài | Phụ | Dịch vụ SMS Gateway của nhà mạng, hệ thống gọi qua API có sẵn | Cung cấp: gửi tin nhắn SMS tới số điện thoại của bệnh nhân | - | REQ-08, REQ-18, REQ-26, REQ-46 |
| ACT-07 | Bộ định thời | Timer | Thời gian | Chính | Sự kiện theo lịch hằng ngày | Kích hoạt: 18 giờ mỗi ngày (nhắc lịch hẹn ngày hôm sau) | - | REQ-26 |

## 3. Bên liên quan không phải tác nhân

| Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
|---|---|---|---|
| SH-01 Phòng khám (ban điều hành) | Giảm trùng lịch, giảm bệnh nhân không đến | Báo cáo do ACT-05 xem | REQ-01, REQ-42 |
| SH-06 Bệnh nhân đặt lịch qua điện thoại | Có lịch khám mà không tự thao tác trên hệ thống | ACT-02 Lễ tân | REQ-22, REQ-23 |
| Bệnh nhân (khi nhận SMS thông báo, nhắc lịch) | Biết kết quả xác nhận, nhớ lịch khám | ACT-06 Cổng SMS | REQ-18, REQ-26 |

## 4. Ứng viên tác nhân bị loại

| Ứng viên | Lý do loại | REQ |
|---|---|---|
| Phòng khám đa khoa Minh An | A-T2: tổ chức sở hữu, không thao tác trên hệ thống (xếp vào Mục 3) | REQ-01 |
| Người lớn tuổi gọi điện | A-T2: chỉ tương tác qua lễ tân (xếp vào Mục 3 dưới tên SH-06) | REQ-22 |
| Nhà mạng | A-T2: tổ chức cung cấp dịch vụ; dịch vụ của họ là ACT-06 | REQ-46 |
| Hệ thống (ClinicBook) | A-T1: chính hệ thống cần xây dựng | - |
| Sổ ghi lịch | A-T1, A-T4: cách làm cũ được thay thế, không có vai trò trong chức năng nào | - |
| Điện thoại di động | A-T4: thiết bị người dùng dùng để thao tác, người thao tác mới là tác nhân | REQ-44 |
| Người dùng chưa đăng nhập | Gộp vào ACT-01 Bệnh nhân: nguồn gọi là "bệnh nhân" ở mục 1 và mục 2; không có vai trò riêng được nêu | REQ-02 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-20 | Lễ tân nhận thông báo khung giờ bị khoá trong phiên làm việc của bác sĩ (tác nhân phụ) hay xem sau trong hệ thống (tác nhân chính của một mục tiêu xem)? Phụ thuộc câu trả lời Q-05 của P00 | Tính chất của ACT-02; P02 | REQ-37 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Không tạo tác nhân cha cho các tác nhân người: phần chung duy nhất có thể là đăng nhập, không đủ hai mục tiêu chung theo điều kiện Bước 5a.
