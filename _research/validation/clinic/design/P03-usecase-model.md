# P03 - Mô hình và sơ đồ use case - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P03 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, P00-problem-brief.md 1.0, P01-actors.md 1.0, P02-usecases.md 1.0 |
| Phạm vi | Toàn hệ thống |

## 1. Bảng quan hệ

| ID | Nguồn | Đích | Loại | Điều kiện extend / điểm mở rộng | Lý do | REQ | Sơ đồ |
|---|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | Tác nhân chính | REQ-02..05 | Tổng quát |
| RL-02 | ACT-01 | UC-002 | Association | - | Tác nhân chính | REQ-07, REQ-08 | Tổng quát |
| RL-03 | ACT-06 | UC-002 | Association | - | Tác nhân phụ: gửi SMS | REQ-07, REQ-08, REQ-46 | Tổng quát |
| RL-04 | ACT-01 | UC-003 | Association | - | Tác nhân chính | REQ-06 | Tổng quát |
| RL-05 | ACT-02 | UC-003 | Association | - | Tác nhân chính | REQ-06 | Tổng quát |
| RL-06 | ACT-03 | UC-003 | Association | - | Tác nhân chính | REQ-06 | Tổng quát |
| RL-07 | ACT-04 | UC-003 | Association | - | Tác nhân chính | REQ-06 | Tổng quát |
| RL-08 | ACT-05 | UC-003 | Association | - | Tác nhân chính | REQ-06 | Tổng quát |
| RL-09 | ACT-01 | UC-004 | Association | - | Tác nhân chính | REQ-09 | Tổng quát |
| RL-10 | ACT-02 | UC-005 | Association | - | Tác nhân chính | REQ-22 | Tổng quát |
| RL-11 | ACT-02 | UC-007 | Association | - | Tác nhân chính | REQ-14..18 | Tổng quát |
| RL-12 | ACT-06 | UC-007 | Association | - | Tác nhân phụ: gửi SMS | REQ-14..18, REQ-46 | Tổng quát |
| RL-13 | ACT-07 | UC-008 | Association | - | Tác nhân chính | REQ-26 | Tổng quát |
| RL-14 | ACT-06 | UC-008 | Association | - | Tác nhân phụ: gửi SMS | REQ-26, REQ-46 | Tổng quát |
| RL-15 | ACT-01 | UC-009 | Association | - | Tác nhân chính | REQ-19 | Tổng quát |
| RL-16 | ACT-02 | UC-010 | Association | - | Tác nhân chính | REQ-21 | Tổng quát |
| RL-17 | ACT-02 | UC-011 | Association | - | Tác nhân chính | REQ-27 | Tổng quát |
| RL-18 | ACT-02 | UC-012 | Association | - | Tác nhân chính | REQ-28 | Tổng quát |
| RL-19 | ACT-03 | UC-013 | Association | - | Tác nhân chính | REQ-35 | Tổng quát |
| RL-20 | ACT-03 | UC-014 | Association | - | Tác nhân chính | REQ-36 | Tổng quát |
| RL-21 | ACT-03 | UC-015 | Association | - | Tác nhân chính | REQ-31 | Tổng quát |
| RL-22 | ACT-03 | UC-016 | Association | - | Tác nhân chính | REQ-32 | Tổng quát |
| RL-23 | ACT-01 | UC-017 | Association | - | Tác nhân chính | REQ-45 | Tổng quát |
| RL-24 | ACT-04 | UC-018 | Association | - | Tác nhân chính | REQ-38 | Tổng quát |
| RL-25 | ACT-04 | UC-019 | Association | - | Tác nhân chính | REQ-39, REQ-40 | Tổng quát |
| RL-26 | ACT-04 | UC-020 | Association | - | Tác nhân chính | REQ-41 | Tổng quát |
| RL-27 | ACT-05 | UC-021 | Association | - | Tác nhân chính | REQ-42 | Tổng quát |
| RL-28 | UC-004 | UC-006 | Include | - | Dùng chung cho UC-004, UC-005 (Bước 3a); bắt buộc trong mọi kịch bản thành công (Bước 3b) | REQ-09, REQ-22 | Tổng quát |
| RL-29 | UC-005 | UC-006 | Include | - | Dùng chung cho UC-004, UC-005 (Bước 3a); bắt buộc trong mọi kịch bản thành công (Bước 3b) | REQ-09, REQ-22 | Tổng quát |

## 2. Điểm mở rộng

Không có

## 3. UC đề xuất bổ sung

Không có

## 4. Danh sách sơ đồ

| Sơ đồ | Phạm vi | Tác nhân | Use case | File |
|---|---|---|---|---|
| Tổng quát | Toàn hệ thống, đủ quan hệ (N = 19 UC User-goal, M = 7 tác nhân, thuộc phương án một sơ đồ ở Bước 8) | ACT-01..ACT-07 | 21 UC (19 User-goal, 2 Subfunction) | diagrams/P03-usecase-overview.drawio |

## 5. Bảng mô hình của từng sơ đồ

### Tổng quát

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống đặt lịch khám ClinicBook | - | - | - | 200 | 40 | 980 | 2370 |
| ACT-01 | Actor | Bệnh nhân | - | - | Tác nhân chính | 60 | 440 | 30 | 60 |
| ACT-02 | Actor | Lễ tân | - | - | Tác nhân chính | 60 | 1100 | 30 | 60 |
| ACT-03 | Actor | Bác sĩ | - | - | Tác nhân chính | 60 | 1700 | 30 | 60 |
| ACT-04 | Actor | Quản trị viên | - | - | Tác nhân chính | 60 | 2080 | 30 | 60 |
| ACT-05 | Actor | Quản lý phòng khám | - | - | Tác nhân chính | 60 | 2300 | 30 | 60 |
| ACT-06 | Actor | Cổng SMS | «system» | - | Tác nhân phụ | 1260 | 930 | 30 | 60 |
| ACT-07 | Actor | Bộ định thời | - | - | Tác nhân chính | 60 | 1420 | 30 | 60 |
| UC-001 | UseCase | Tra cứu lịch trống của bác sĩ | - | SYS | - | 460 | 210 | 160 | 70 |
| UC-002 | UseCase | Đăng ký tài khoản | - | SYS | - | 460 | 320 | 160 | 70 |
| UC-003 | UseCase | Đăng nhập | - | SYS | Subfunction | 240 | 1480 | 160 | 70 |
| UC-004 | UseCase | Đặt lịch khám | - | SYS | - | 460 | 650 | 160 | 70 |
| UC-005 | UseCase | Đặt lịch khám cho bệnh nhân | - | SYS | - | 460 | 870 | 160 | 70 |
| UC-006 | UseCase | Chọn khung giờ khám | - | SYS | Subfunction | 540 | 760 | 160 | 70 |
| UC-007 | UseCase | Duyệt lịch hẹn | - | SYS | - | 460 | 980 | 160 | 70 |
| UC-008 | UseCase | Nhắc lịch khám | - | SYS | - | 460 | 1420 | 160 | 70 |
| UC-009 | UseCase | Hủy lịch hẹn | - | SYS | - | 460 | 540 | 160 | 70 |
| UC-010 | UseCase | Hủy lịch hẹn cho bệnh nhân | - | SYS | - | 460 | 1090 | 160 | 70 |
| UC-011 | UseCase | Tiếp nhận bệnh nhân đến khám | - | SYS | - | 460 | 1200 | 160 | 70 |
| UC-012 | UseCase | Đánh dấu bệnh nhân không đến | - | SYS | - | 460 | 1310 | 160 | 70 |
| UC-013 | UseCase | Đăng ký lịch làm việc tuần | - | SYS | - | 460 | 1530 | 160 | 70 |
| UC-014 | UseCase | Khoá khung giờ đột xuất | - | SYS | - | 460 | 1640 | 160 | 70 |
| UC-015 | UseCase | Xem lịch hẹn trong ngày | - | SYS | - | 460 | 1750 | 160 | 70 |
| UC-016 | UseCase | Ghi kết luận khám | - | SYS | - | 460 | 1860 | 160 | 70 |
| UC-017 | UseCase | Xem kết luận khám | - | SYS | - | 460 | 430 | 160 | 70 |
| UC-018 | UseCase | Quản lý chuyên khoa | - | SYS | - | 460 | 1970 | 160 | 70 |
| UC-019 | UseCase | Quản lý tài khoản nhân viên | - | SYS | - | 460 | 2080 | 160 | 70 |
| UC-020 | UseCase | Cấu hình tham số nghiệp vụ | - | SYS | - | 460 | 2190 | 160 | 70 |
| UC-021 | UseCase | Xem báo cáo lịch hẹn tháng | - | SYS | - | 460 | 2300 | 160 | 70 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | - |
| RL-02 | ACT-01 | UC-002 | Association | - | - |
| RL-03 | ACT-06 | UC-002 | Association | - | - |
| RL-04 | ACT-01 | UC-003 | Association | - | - |
| RL-05 | ACT-02 | UC-003 | Association | - | - |
| RL-06 | ACT-03 | UC-003 | Association | - | - |
| RL-07 | ACT-04 | UC-003 | Association | - | - |
| RL-08 | ACT-05 | UC-003 | Association | - | - |
| RL-09 | ACT-01 | UC-004 | Association | - | - |
| RL-10 | ACT-02 | UC-005 | Association | - | - |
| RL-11 | ACT-02 | UC-007 | Association | - | - |
| RL-12 | ACT-06 | UC-007 | Association | - | - |
| RL-13 | ACT-07 | UC-008 | Association | - | - |
| RL-14 | ACT-06 | UC-008 | Association | - | - |
| RL-15 | ACT-01 | UC-009 | Association | - | - |
| RL-16 | ACT-02 | UC-010 | Association | - | - |
| RL-17 | ACT-02 | UC-011 | Association | - | - |
| RL-18 | ACT-02 | UC-012 | Association | - | - |
| RL-19 | ACT-03 | UC-013 | Association | - | - |
| RL-20 | ACT-03 | UC-014 | Association | - | - |
| RL-21 | ACT-03 | UC-015 | Association | - | - |
| RL-22 | ACT-03 | UC-016 | Association | - | - |
| RL-23 | ACT-01 | UC-017 | Association | - | - |
| RL-24 | ACT-04 | UC-018 | Association | - | - |
| RL-25 | ACT-04 | UC-019 | Association | - | - |
| RL-26 | ACT-04 | UC-020 | Association | - | - |
| RL-27 | ACT-05 | UC-021 | Association | - | - |
| RL-28 | UC-004 | UC-006 | Include | «include» | - |
| RL-29 | UC-005 | UC-006 | Include | «include» | - |

## 6. Nội dung file .drawio

Đã ghi thẳng ra diagrams/P03-usecase-overview.drawio (chạy bằng agent có quyền ghi file), không chép lại XML vào đây.

## Câu hỏi mở

Không có

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-009, UC-010 | P02R UCR-01 đề nghị gộp; P03 vẽ theo P02 1.0 | Chốt cách hiểu U-R10 rồi chạy lại P02 nếu gộp |

## Vấn đề còn mở

- Target 10 (UC sắp theo trình tự thời gian từ trên xuống): Không đạt một phần. Trong nhóm của ACT-01, UC-017 và UC-009 đặt trên UC-004 để UC-004 nằm sát UC-005 và UC-006 (include); theo L-09 ưu tiên tránh đường cắt qua node.
- UC-003 Đăng nhập nối với 5 tác nhân. Đặt UC-003 ở cột trái, giữa nhóm ACT-07 và ACT-03, để 5 đường nối không cắt qua node nào; vẫn còn đường cắt đường (cắt các đường của ACT-02, ACT-07, ACT-03).
- Sơ đồ cao khoảng 2400 px (một cột 20 UC) vì quy tắc bố cục L-05, L-09 chỉ hướng dẫn một cột UC cho mỗi nhóm tác nhân. Boundary được nới rộng sang phải (x tới 1180) để đường nối tới ACT-06 Cổng SMS đủ thoải, không cắt UC-006 và UC-012.
- Tổng số UC trên sơ đồ là 21, vượt nhẹ mức "khoảng 20 UC" ở Phần C, trong khi Bước 8 chỉ đếm UC User-goal (19). Giữ một sơ đồ theo Bước 8.
