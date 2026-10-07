# P03 - Mô hình và sơ đồ use case - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P03 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.0; P02R-review.md 1.0 (đối chiếu) |
| Phạm vi | Toàn hệ thống |

Placeholder: KIEU_DUONG_ASSOCIATION = Không có (mặc định KHONG_MUI_TEN); CACH_PHAN_RA_SO_DO = Không có (mặc định THEO_NHOM); YEU_CAU_BO_SUNG = Không có.

## Mục 1. Bảng quan hệ

| ID | Nguồn | Đích | Loại | Điều kiện extend / điểm mở rộng | Lý do | REQ | Sơ đồ |
|---|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | Tác nhân chính | REQ-02 | P03-usecase-overview, P03-usecase-account |
| RL-02 | ACT-01 | UC-002 | Association | - | Tác nhân chính | REQ-03, REQ-62 | P03-usecase-overview, P03-usecase-account |
| RL-03 | ACT-07 | UC-002 | Association | - | Tác nhân phụ: tạm giữ, thu, huỷ tạm giữ, hoàn tiền, liên kết thẻ | REQ-03, REQ-62 | P03-usecase-overview, P03-usecase-account |
| RL-04 | ACT-01 | UC-003 | Association | - | Tác nhân chính | REQ-05, REQ-54 | P03-usecase-account |
| RL-05 | ACT-02 | UC-003 | Association | - | Tác nhân chính | REQ-05, REQ-54 | P03-usecase-account |
| RL-06 | ACT-03 | UC-003 | Association | - | Tác nhân chính | REQ-05, REQ-54 | P03-usecase-account |
| RL-07 | ACT-04 | UC-003 | Association | - | Tác nhân chính | REQ-05, REQ-54 | P03-usecase-account |
| RL-08 | ACT-05 | UC-003 | Association | - | Tác nhân chính | REQ-05, REQ-54 | P03-usecase-account |
| RL-09 | ACT-06 | UC-003 | Association | - | Tác nhân chính | REQ-05, REQ-54 | P03-usecase-account |
| RL-10 | ACT-01 | UC-004 | Association | - | Tác nhân chính | REQ-05 | P03-usecase-overview, P03-usecase-rental |
| RL-11 | ACT-01 | UC-005 | Association | - | Tác nhân chính | REQ-07, REQ-10, REQ-12 | P03-usecase-overview, P03-usecase-rental |
| RL-12 | ACT-07 | UC-005 | Association | - | Tác nhân phụ: tạm giữ, thu, huỷ tạm giữ, hoàn tiền, liên kết thẻ | REQ-07, REQ-10, REQ-12 | P03-usecase-overview, P03-usecase-rental |
| RL-13 | ACT-08 | UC-005 | Association | - | Tác nhân phụ: mở khoá, báo xe được rút, đưa vào | REQ-07, REQ-10, REQ-12 | P03-usecase-overview, P03-usecase-rental |
| RL-14 | ACT-01 | UC-006 | Association | - | Tác nhân chính | REQ-25 | P03-usecase-overview, P03-usecase-rental |
| RL-15 | ACT-01 | UC-007 | Association | - | Tác nhân chính | REQ-17, REQ-18, REQ-22 | P03-usecase-overview, P03-usecase-rental |
| RL-16 | ACT-08 | UC-007 | Association | - | Tác nhân phụ: mở khoá, báo xe được rút, đưa vào | REQ-17, REQ-18, REQ-22 | P03-usecase-overview, P03-usecase-rental |
| RL-17 | ACT-07 | UC-007 | Association | - | Tác nhân phụ: tạm giữ, thu, huỷ tạm giữ, hoàn tiền, liên kết thẻ | REQ-17, REQ-18, REQ-22 | P03-usecase-overview, P03-usecase-rental |
| RL-18 | ACT-01 | UC-008 | Association | - | Tác nhân chính | REQ-33 | P03-usecase-overview, P03-usecase-rental |
| RL-19 | ACT-09 | UC-009 | Association | - | Tác nhân chính | REQ-28, REQ-30 | P03-usecase-overview, P03-usecase-rental |
| RL-20 | ACT-07 | UC-009 | Association | - | Tác nhân phụ: tạm giữ, thu, huỷ tạm giữ, hoàn tiền, liên kết thẻ | REQ-28, REQ-30 | P03-usecase-overview, P03-usecase-rental |
| RL-21 | ACT-03 | UC-010 | Association | - | Tác nhân chính | REQ-38 | P03-usecase-overview, P03-usecase-maintenance |
| RL-22 | ACT-03 | UC-011 | Association | - | Tác nhân chính | REQ-39 | P03-usecase-overview, P03-usecase-maintenance |
| RL-23 | ACT-04 | UC-012 | Association | - | Tác nhân chính | REQ-41 | P03-usecase-overview, P03-usecase-dispatch |
| RL-24 | ACT-04 | UC-013 | Association | - | Tác nhân chính | REQ-44 | P03-usecase-overview, P03-usecase-dispatch |
| RL-25 | ACT-08 | UC-014 | Association | - | Tác nhân chính | REQ-46 | P03-usecase-overview, P03-usecase-dispatch |
| RL-26 | ACT-04 | UC-015 | Association | - | Tác nhân chính | REQ-45 | P03-usecase-overview, P03-usecase-dispatch |
| RL-27 | ACT-02 | UC-016 | Association | - | Tác nhân chính | REQ-47 | P03-usecase-overview, P03-usecase-customer-care |
| RL-28 | ACT-02 | UC-017 | Association | - | Tác nhân chính | REQ-48, REQ-62 | P03-usecase-overview, P03-usecase-customer-care |
| RL-29 | ACT-07 | UC-017 | Association | - | Tác nhân phụ: tạm giữ, thu, huỷ tạm giữ, hoàn tiền, liên kết thẻ | REQ-48, REQ-62 | P03-usecase-overview, P03-usecase-customer-care |
| RL-30 | ACT-02 | UC-018 | Association | - | Tác nhân chính | REQ-50 | P03-usecase-overview, P03-usecase-customer-care |
| RL-31 | ACT-05 | UC-019 | Association | - | Tác nhân chính | REQ-51 | P03-usecase-overview, P03-usecase-catalog |
| RL-32 | ACT-05 | UC-020 | Association | - | Tác nhân chính | REQ-52 | P03-usecase-overview, P03-usecase-catalog |
| RL-33 | ACT-05 | UC-021 | Association | - | Tác nhân chính | REQ-53 | P03-usecase-overview, P03-usecase-catalog |
| RL-34 | ACT-05 | UC-022 | Association | - | Tác nhân chính | REQ-54 | P03-usecase-overview, P03-usecase-catalog |
| RL-35 | ACT-05 | UC-023 | Association | - | Tác nhân chính | REQ-55 | P03-usecase-overview, P03-usecase-catalog |
| RL-36 | ACT-06 | UC-024 | Association | - | Tác nhân chính | REQ-56 | P03-usecase-overview, P03-usecase-reporting |

Không có quan hệ include, extend, generalization. Lý do: P02 không giữ UC Subfunction nào theo Q4 (UC-003 Đăng nhập giữ theo U-R01, dùng tiền điều kiện, không include); không UC nào được P02 giữ theo Q4b; P01 không có tổng quát hoá tác nhân.

## Mục 2. Điểm mở rộng

Không có

## Mục 3. UC đề xuất bổ sung

Không có

## Mục 4. Danh sách sơ đồ

| Sơ đồ | Phạm vi | Tác nhân | Use case | File |
|---|---|---|---|---|
| Tổng quát | Toàn hệ thống, UC User-goal, không vẽ quan hệ giữa UC | ACT-01 đến ACT-09 | 23 UC User-goal (trừ UC-003) | diagrams/P03-usecase-overview.drawio |
| Nhóm Tài khoản | UC-001 đến UC-003 | ACT-01 đến ACT-07 | 3 | diagrams/P03-usecase-account.drawio |
| Nhóm Thuê trả xe | UC-004 đến UC-009 | ACT-01, ACT-07, ACT-08, ACT-09 | 6 | diagrams/P03-usecase-rental.drawio |
| Nhóm Bảo trì | UC-010, UC-011 | ACT-03 | 2 | diagrams/P03-usecase-maintenance.drawio |
| Nhóm Điều phối | UC-012 đến UC-015 | ACT-04, ACT-08 | 4 | diagrams/P03-usecase-dispatch.drawio |
| Nhóm Chăm sóc khách hàng | UC-016 đến UC-018 | ACT-02, ACT-07 | 3 | diagrams/P03-usecase-customer-care.drawio |
| Nhóm Danh mục | UC-019 đến UC-023 | ACT-05 | 5 | diagrams/P03-usecase-catalog.drawio |
| Nhóm Báo cáo | UC-024 | ACT-06 | 1 | diagrams/P03-usecase-reporting.drawio |

## Mục 5. Bảng mô hình của từng sơ đồ

### Tổng quát

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| UC-001 | UseCase | Đăng ký tài khoản | - | SYS | - | 260 | 100 | 160 | 70 |
| UC-002 | UseCase | Liên kết thẻ thanh toán | - | SYS | - | 500 | 160 | 160 | 70 |
| UC-004 | UseCase | Xem bản đồ trạm | - | SYS | - | 260 | 220 | 160 | 70 |
| UC-005 | UseCase | Thuê xe | - | SYS | - | 500 | 280 | 160 | 70 |
| UC-006 | UseCase | Xin thêm thời gian miễn phí | - | SYS | - | 260 | 340 | 160 | 70 |
| UC-007 | UseCase | Trả xe | - | SYS | - | 500 | 400 | 160 | 70 |
| UC-008 | UseCase | Báo xe hỏng | - | SYS | - | 260 | 460 | 160 | 70 |
| UC-009 | UseCase | Ghi nhận xe thất lạc | - | SYS | - | 260 | 580 | 160 | 70 |
| UC-016 | UseCase | Tra cứu lịch sử chuyến đi | - | SYS | - | 260 | 700 | 160 | 70 |
| UC-017 | UseCase | Điều chỉnh cước | - | SYS | - | 500 | 760 | 160 | 70 |
| UC-018 | UseCase | Mở khoá tài khoản | - | SYS | - | 260 | 820 | 160 | 70 |
| UC-010 | UseCase | Tra cứu xe chờ kiểm tra | - | SYS | - | 260 | 940 | 160 | 70 |
| UC-011 | UseCase | Ghi nhận kết quả kiểm tra xe | - | SYS | - | 500 | 1000 | 160 | 70 |
| UC-012 | UseCase | Xem trạm sắp hết xe, sắp đầy | - | SYS | - | 260 | 1060 | 160 | 70 |
| UC-013 | UseCase | Lập lệnh điều chuyển | - | SYS | - | 500 | 1120 | 160 | 70 |
| UC-015 | UseCase | Theo dõi lệnh điều chuyển | - | SYS | - | 260 | 1180 | 160 | 70 |
| UC-014 | UseCase | Ghi nhận xe điều chuyển tại ụ | - | SYS | - | 500 | 1240 | 160 | 70 |
| UC-019 | UseCase | Quản lý trạm | - | SYS | - | 260 | 1300 | 160 | 70 |
| UC-020 | UseCase | Quản lý ụ khoá | - | SYS | - | 500 | 1360 | 160 | 70 |
| UC-021 | UseCase | Quản lý xe | - | SYS | - | 260 | 1420 | 160 | 70 |
| UC-022 | UseCase | Quản lý tài khoản nhân viên | - | SYS | - | 500 | 1480 | 160 | 70 |
| UC-023 | UseCase | Quản lý bảng giá cước | - | SYS | - | 260 | 1540 | 160 | 70 |
| UC-024 | UseCase | Xem báo cáo hằng tuần | - | SYS | - | 260 | 1660 | 160 | 70 |
| ACT-01 | Actor | Người thuê xe | - | - | - | 60 | 280 | 30 | 60 |
| ACT-09 | Actor | Bộ định thời | - | - | - | 60 | 580 | 30 | 60 |
| ACT-02 | Actor | Nhân viên chăm sóc khách hàng | - | - | - | 60 | 760 | 30 | 60 |
| ACT-03 | Actor | Nhân viên bảo trì | - | - | - | 60 | 980 | 30 | 60 |
| ACT-04 | Actor | Nhân viên điều phối | - | - | - | 60 | 1160 | 30 | 60 |
| ACT-05 | Actor | Quản trị viên | - | - | - | 60 | 1420 | 30 | 60 |
| ACT-06 | Actor | Ban giám đốc | - | - | - | 60 | 1660 | 30 | 60 |
| ACT-07 | Actor | Cổng thanh toán | «system» | - | - | 800 | 220 | 30 | 60 |
| ACT-08 | Actor | Ụ khoá | «device» | - | - | 800 | 580 | 30 | 60 |
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 520 | 1730 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | - | - |
| RL-02 | ACT-01 | UC-002 | Association | - | - | (240,195) |
| RL-03 | ACT-07 | UC-002 | Association | - | - | - |
| RL-10 | ACT-01 | UC-004 | Association | - | - | - |
| RL-11 | ACT-01 | UC-005 | Association | - | - | (240,315) |
| RL-12 | ACT-07 | UC-005 | Association | - | - | - |
| RL-13 | ACT-08 | UC-005 | Association | - | - | - |
| RL-14 | ACT-01 | UC-006 | Association | - | - | - |
| RL-15 | ACT-01 | UC-007 | Association | - | - | (240,435) |
| RL-16 | ACT-08 | UC-007 | Association | - | - | - |
| RL-17 | ACT-07 | UC-007 | Association | - | - | - |
| RL-18 | ACT-01 | UC-008 | Association | - | - | - |
| RL-19 | ACT-09 | UC-009 | Association | - | - | - |
| RL-20 | ACT-07 | UC-009 | Association | - | - | (750,620) |
| RL-21 | ACT-03 | UC-010 | Association | - | - | - |
| RL-22 | ACT-03 | UC-011 | Association | - | - | (240,1035) |
| RL-23 | ACT-04 | UC-012 | Association | - | - | - |
| RL-24 | ACT-04 | UC-013 | Association | - | - | (240,1155) |
| RL-25 | ACT-08 | UC-014 | Association | - | - | (760,1270) |
| RL-26 | ACT-04 | UC-015 | Association | - | - | - |
| RL-27 | ACT-02 | UC-016 | Association | - | - | - |
| RL-28 | ACT-02 | UC-017 | Association | - | - | (240,795) |
| RL-29 | ACT-07 | UC-017 | Association | - | - | - |
| RL-30 | ACT-02 | UC-018 | Association | - | - | - |
| RL-31 | ACT-05 | UC-019 | Association | - | - | - |
| RL-32 | ACT-05 | UC-020 | Association | - | - | (240,1395) |
| RL-33 | ACT-05 | UC-021 | Association | - | - | - |
| RL-34 | ACT-05 | UC-022 | Association | - | - | (240,1515) |
| RL-35 | ACT-05 | UC-023 | Association | - | - | - |
| RL-36 | ACT-06 | UC-024 | Association | - | - | - |

### Nhóm Tài khoản

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 280 | 880 |
| UC-001 | UseCase | Đăng ký tài khoản | - | SYS | - | 260 | 100 | 160 | 70 |
| UC-002 | UseCase | Liên kết thẻ thanh toán | - | SYS | - | 260 | 220 | 160 | 70 |
| UC-003 | UseCase | Đăng nhập | - | SYS | - | 260 | 520 | 160 | 70 |
| ACT-01 | Actor | Người thuê xe | - | - | - | 60 | 160 | 30 | 60 |
| ACT-02 | Actor | Nhân viên chăm sóc khách hàng | - | - | - | 60 | 340 | 30 | 60 |
| ACT-03 | Actor | Nhân viên bảo trì | - | - | - | 60 | 460 | 30 | 60 |
| ACT-04 | Actor | Nhân viên điều phối | - | - | - | 60 | 580 | 30 | 60 |
| ACT-05 | Actor | Quản trị viên | - | - | - | 60 | 700 | 30 | 60 |
| ACT-06 | Actor | Ban giám đốc | - | - | - | 60 | 820 | 30 | 60 |
| ACT-07 | Actor | Cổng thanh toán | «system» | - | - | 560 | 220 | 30 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | - | - |
| RL-02 | ACT-01 | UC-002 | Association | - | - | - |
| RL-03 | ACT-07 | UC-002 | Association | - | - | - |
| RL-04 | ACT-01 | UC-003 | Association | - | - | (180,190); (240,555) |
| RL-05 | ACT-02 | UC-003 | Association | - | - | - |
| RL-06 | ACT-03 | UC-003 | Association | - | - | - |
| RL-07 | ACT-04 | UC-003 | Association | - | - | - |
| RL-08 | ACT-05 | UC-003 | Association | - | - | - |
| RL-09 | ACT-06 | UC-003 | Association | - | - | - |

### Nhóm Thuê trả xe

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 280 | 770 |
| UC-004 | UseCase | Xem bản đồ trạm | - | SYS | - | 260 | 100 | 160 | 70 |
| UC-005 | UseCase | Thuê xe | - | SYS | - | 260 | 220 | 160 | 70 |
| UC-006 | UseCase | Xin thêm thời gian miễn phí | - | SYS | - | 260 | 340 | 160 | 70 |
| UC-007 | UseCase | Trả xe | - | SYS | - | 260 | 460 | 160 | 70 |
| UC-008 | UseCase | Báo xe hỏng | - | SYS | - | 260 | 580 | 160 | 70 |
| UC-009 | UseCase | Ghi nhận xe thất lạc | - | SYS | - | 260 | 700 | 160 | 70 |
| ACT-01 | Actor | Người thuê xe | - | - | - | 60 | 340 | 30 | 60 |
| ACT-09 | Actor | Bộ định thời | - | - | - | 60 | 700 | 30 | 60 |
| ACT-07 | Actor | Cổng thanh toán | «system» | - | - | 560 | 140 | 30 | 60 |
| ACT-08 | Actor | Ụ khoá | «device» | - | - | 560 | 400 | 30 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-10 | ACT-01 | UC-004 | Association | - | - | - |
| RL-11 | ACT-01 | UC-005 | Association | - | - | - |
| RL-12 | ACT-07 | UC-005 | Association | - | - | - |
| RL-13 | ACT-08 | UC-005 | Association | - | - | - |
| RL-14 | ACT-01 | UC-006 | Association | - | - | - |
| RL-15 | ACT-01 | UC-007 | Association | - | - | - |
| RL-16 | ACT-08 | UC-007 | Association | - | - | - |
| RL-17 | ACT-07 | UC-007 | Association | - | - | - |
| RL-18 | ACT-01 | UC-008 | Association | - | - | - |
| RL-19 | ACT-09 | UC-009 | Association | - | - | - |
| RL-20 | ACT-07 | UC-009 | Association | - | - | (500,740) |

### Nhóm Bảo trì

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 280 | 290 |
| UC-010 | UseCase | Tra cứu xe chờ kiểm tra | - | SYS | - | 260 | 100 | 160 | 70 |
| UC-011 | UseCase | Ghi nhận kết quả kiểm tra xe | - | SYS | - | 260 | 220 | 160 | 70 |
| ACT-03 | Actor | Nhân viên bảo trì | - | - | - | 60 | 160 | 30 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-21 | ACT-03 | UC-010 | Association | - | - | - |
| RL-22 | ACT-03 | UC-011 | Association | - | - | - |

### Nhóm Điều phối

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 280 | 530 |
| UC-012 | UseCase | Xem trạm sắp hết xe, sắp đầy | - | SYS | - | 260 | 100 | 160 | 70 |
| UC-013 | UseCase | Lập lệnh điều chuyển | - | SYS | - | 260 | 220 | 160 | 70 |
| UC-014 | UseCase | Ghi nhận xe điều chuyển tại ụ | - | SYS | - | 260 | 340 | 160 | 70 |
| UC-015 | UseCase | Theo dõi lệnh điều chuyển | - | SYS | - | 260 | 460 | 160 | 70 |
| ACT-04 | Actor | Nhân viên điều phối | - | - | - | 60 | 260 | 30 | 60 |
| ACT-08 | Actor | Ụ khoá | «device» | - | - | 560 | 340 | 30 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-23 | ACT-04 | UC-012 | Association | - | - | - |
| RL-24 | ACT-04 | UC-013 | Association | - | - | - |
| RL-25 | ACT-08 | UC-014 | Association | - | - | - |
| RL-26 | ACT-04 | UC-015 | Association | - | - | - |

### Nhóm Chăm sóc khách hàng

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 280 | 410 |
| UC-016 | UseCase | Tra cứu lịch sử chuyến đi | - | SYS | - | 260 | 100 | 160 | 70 |
| UC-017 | UseCase | Điều chỉnh cước | - | SYS | - | 260 | 220 | 160 | 70 |
| UC-018 | UseCase | Mở khoá tài khoản | - | SYS | - | 260 | 340 | 160 | 70 |
| ACT-02 | Actor | Nhân viên chăm sóc khách hàng | - | - | - | 60 | 220 | 30 | 60 |
| ACT-07 | Actor | Cổng thanh toán | «system» | - | - | 560 | 220 | 30 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-27 | ACT-02 | UC-016 | Association | - | - | - |
| RL-28 | ACT-02 | UC-017 | Association | - | - | - |
| RL-29 | ACT-07 | UC-017 | Association | - | - | - |
| RL-30 | ACT-02 | UC-018 | Association | - | - | - |

### Nhóm Danh mục

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 280 | 650 |
| UC-019 | UseCase | Quản lý trạm | - | SYS | - | 260 | 100 | 160 | 70 |
| UC-020 | UseCase | Quản lý ụ khoá | - | SYS | - | 260 | 220 | 160 | 70 |
| UC-021 | UseCase | Quản lý xe | - | SYS | - | 260 | 340 | 160 | 70 |
| UC-022 | UseCase | Quản lý tài khoản nhân viên | - | SYS | - | 260 | 460 | 160 | 70 |
| UC-023 | UseCase | Quản lý bảng giá cước | - | SYS | - | 260 | 580 | 160 | 70 |
| ACT-05 | Actor | Quản trị viên | - | - | - | 60 | 340 | 30 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-31 | ACT-05 | UC-019 | Association | - | - | - |
| RL-32 | ACT-05 | UC-020 | Association | - | - | - |
| RL-33 | ACT-05 | UC-021 | Association | - | - | - |
| RL-34 | ACT-05 | UC-022 | Association | - | - | - |
| RL-35 | ACT-05 | UC-023 | Association | - | - | - |

### Nhóm Báo cáo

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống cho thuê xe đạp công cộng CityBike | - | - | - | 200 | 40 | 280 | 170 |
| UC-024 | UseCase | Xem báo cáo hằng tuần | - | SYS | - | 260 | 100 | 160 | 70 |
| ACT-06 | Actor | Ban giám đốc | - | - | - | 60 | 100 | 30 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-36 | ACT-06 | UC-024 | Association | - | - | - |

## Mục 6. Nội dung file .drawio

Đã ghi file: diagrams/P03-usecase-overview.drawio, diagrams/P03-usecase-account.drawio, diagrams/P03-usecase-rental.drawio, diagrams/P03-usecase-maintenance.drawio, diagrams/P03-usecase-dispatch.drawio, diagrams/P03-usecase-customer-care.drawio, diagrams/P03-usecase-catalog.drawio, diagrams/P03-usecase-reporting.drawio.

## Câu hỏi mở

Không có

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Sơ đồ tổng quát có 23 UC và 9 tác nhân, vượt ngưỡng Phần C (khoảng 20 UC, 8 tác nhân mỗi sơ đồ) dù Bước 8 (N từ 21 đến 40 hoặc M trên 8) yêu cầu sơ đồ tổng quát gồm mọi UC User-goal và mọi tác nhân. Chọn theo Bước 8.
- L-12 yêu cầu mỗi nhóm chức năng một cột. Bản bố cục theo đúng câu chữ (7 cột, hai tầng) có 11 đường cắt qua elip vì các nhóm nhân viên đều nối với tác nhân chính ở bên trái. Bố cục đã dùng: hai cột, mỗi tác nhân chính một dải ngang, UC của cùng dải đặt xen hai cột lệch nửa hàng; đường tới cột hai đi qua điểm uốn ở lề trái boundary. Không có đường cắt qua node; còn vài đường cắt nhau ở phía tác nhân phụ.
- ACT-08 Ụ khoá là tác nhân chính ở UC-014 và phụ ở UC-005, UC-007; đặt bên phải theo L-03 (vai trò chiếm đa số). Association RL-25 từ ACT-08 tới UC-014 vì vậy đi từ bên phải.
- Bảy sơ đồ phân rã theo nhóm được sinh theo Bước 8 dù không có quan hệ include, extend nào; sáu sơ đồ trùng nội dung với sơ đồ tổng quát, chỉ sơ đồ Nhóm Tài khoản có thêm UC-003.
- Không vẽ extend giữa UC-008 Báo xe hỏng và UC-007 Trả xe: UC-008 được P02 giữ ở mức User-goal (không theo Q4b) và có thể thực hiện tới 10 phút sau khi trả xe, nên không thoả Bước 4a.
- P02R UCR-04 (đổi tên UC-012) không được áp dụng vì P02 không chạy lại (P02R kết luận Đạt); sơ đồ dùng tên theo P02 1.0.
