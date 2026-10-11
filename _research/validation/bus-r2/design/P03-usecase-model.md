# P03 - Mô hình và sơ đồ use case - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P03 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09); P01-actors.md (phiên bản 1.0, Q-39, ASM-11); P02-usecases.md (phiên bản 1.1, Q-42, ASM-16); yeu-cau-xe-khach.md; P02R-review.md (phiên bản 1.0). Đối chiếu P02R 1.0: UCR-01, UCR-02, UCR-03, UCR-04 đã áp dụng ở P02 1.1, không có UCR nào không áp dụng. Placeholder KIEU_DUONG_ASSOCIATION, CACH_PHAN_RA_SO_DO, YEU_CAU_BO_SUNG: Không có (dùng KHONG_MUI_TEN, THEO_NHOM). Mã Q, ASM cấp tiếp từ Q-42, ASM-16 |
| Phạm vi | Toàn hệ thống: 9 tác nhân (ACT-01 đến ACT-09), 27 use case hiệu lực (UC-013 trạng thái Loại, không vẽ) |
| Mã Q, ASM cuối đã cấp | Q-43, ASM-17 |

## 1. Bảng quan hệ

| ID | Nguồn | Đích | Loại | Điều kiện extend / điểm mở rộng | Lý do | REQ | Sơ đồ |
|---|---|---|---|---|---|---|---|
| RL-01 | ACT-01 Hành khách | UC-001 Đăng ký tài khoản | Association | - | Tác nhân chính | REQ-10 | Tổng quát |
| RL-02 | ACT-04 Quản lý nhà xe | UC-002 Quản lý tài khoản nhân viên | Association | - | Tác nhân chính | REQ-24 | Tổng quát |
| RL-03 | ACT-01 Hành khách | UC-003 Đăng nhập | Association | - | Tác nhân chính (U-R01 của P02: nối mọi tác nhân phải đăng nhập) | REQ-12 | Tổng quát |
| RL-04 | ACT-02 Nhân viên bán vé | UC-003 Đăng nhập | Association | - | Tác nhân chính (U-R01 của P02: nối mọi tác nhân phải đăng nhập) | REQ-23 | Tổng quát |
| RL-05 | ACT-03 Nhân viên điều hành | UC-003 Đăng nhập | Association | - | Tác nhân chính (U-R01 của P02: nối mọi tác nhân phải đăng nhập) | REQ-23 | Tổng quát |
| RL-06 | ACT-04 Quản lý nhà xe | UC-003 Đăng nhập | Association | - | Tác nhân chính (U-R01 của P02: nối mọi tác nhân phải đăng nhập) | REQ-23 | Tổng quát |
| RL-07 | ACT-05 Phụ xe | UC-003 Đăng nhập | Association | - | Tác nhân chính (U-R01 của P02: nối mọi tác nhân phải đăng nhập) | REQ-23 | Tổng quát |
| RL-08 | ACT-07 Cổng SMS | UC-003 Đăng nhập | Association | - | Tác nhân phụ: gửi mã xác thực đăng nhập qua SMS (ASM-01) | REQ-12, REQ-21 | Tổng quát |
| RL-09 | ACT-02 Nhân viên bán vé | UC-004 Bán vé tại quầy | Association | - | Tác nhân chính | REQ-22, REQ-25, REQ-26, REQ-29 | Tổng quát; Bán vé tại quầy |
| RL-10 | ACT-08 Máy in vé | UC-004 Bán vé tại quầy | Association | - | Tác nhân phụ: in vé giấy có mã vạch | REQ-26, REQ-27 | Tổng quát; Bán vé tại quầy |
| RL-11 | ACT-02 Nhân viên bán vé | UC-005 Nhận đặt chỗ qua điện thoại | Association | - | Tác nhân chính | REQ-28, REQ-29 | Tổng quát; Bán vé tại quầy |
| RL-12 | ACT-02 Nhân viên bán vé | UC-006 Thu tiền vé đặt qua điện thoại | Association | - | Tác nhân chính | REQ-30 | Tổng quát; Bán vé tại quầy |
| RL-13 | ACT-08 Máy in vé | UC-006 Thu tiền vé đặt qua điện thoại | Association | - | Tác nhân phụ: in vé giấy có mã vạch (ASM-14, chờ Q-40) | REQ-26, REQ-27 | Tổng quát; Bán vé tại quầy |
| RL-14 | ACT-09 Bộ định thời | UC-007 Huỷ vé đặt chỗ quá hạn | Association | - | Tác nhân chính | REQ-31, REQ-32 | Tổng quát; Bán vé tại quầy |
| RL-15 | ACT-01 Hành khách | UC-008 Tra cứu chuyến xe | Association | - | Tác nhân chính; UC-008 cũng là UC được include nên áp dụng Bước 2.2b: P02 ghi ACT-01 là tác nhân chính, có sự kiện kích hoạt riêng EV-01 | REQ-05, REQ-06 | Tổng quát; Đặt vé trực tuyến |
| RL-16 | ACT-01 Hành khách | UC-009 Đặt vé trực tuyến | Association | - | Tác nhân chính | REQ-04, REQ-07, REQ-08, REQ-09, REQ-13 | Tổng quát; Đặt vé trực tuyến |
| RL-17 | ACT-07 Cổng SMS | UC-009 Đặt vé trực tuyến | Association | - | Tác nhân phụ: gửi mã vé qua SMS tới số điện thoại người đi | REQ-20, REQ-21 | Tổng quát; Đặt vé trực tuyến |
| RL-18 | ACT-06 Cổng thanh toán | UC-010 Thanh toán vé trực tuyến | Association | - | Tác nhân phụ: thu tiền vé qua cổng thanh toán | REQ-15, REQ-16 | Tổng quát; Đặt vé trực tuyến |
| RL-19 | ACT-01 Hành khách | UC-011 Xem lịch sử vé | Association | - | Tác nhân chính | REQ-11 | Tổng quát; Đặt vé trực tuyến |
| RL-20 | ACT-01 Hành khách | UC-012 Trả vé | Association | - | Tác nhân chính | REQ-33 | Tổng quát; Trả vé và đổi vé |
| RL-21 | ACT-02 Nhân viên bán vé | UC-012 Trả vé | Association | - | Tác nhân chính (vé mua tại quầy, ASM-04, ASM-15) | REQ-35 | Tổng quát; Trả vé và đổi vé |
| RL-22 | ACT-06 Cổng thanh toán | UC-012 Trả vé | Association | - | Tác nhân phụ: hoàn tiền vé mua trực tuyến qua cổng (nhánh hoàn qua cổng thanh toán) | REQ-16, REQ-40 | Tổng quát; Trả vé và đổi vé |
| RL-23 | ACT-01 Hành khách | UC-014 Đổi vé trực tuyến | Association | - | Tác nhân chính | REQ-34 | Tổng quát; Trả vé và đổi vé |
| RL-24 | ACT-07 Cổng SMS | UC-014 Đổi vé trực tuyến | Association | - | Tác nhân phụ: gửi mã vé mới qua SMS (ASM-16, chờ Q-42) | REQ-20, REQ-21 | Tổng quát; Trả vé và đổi vé |
| RL-25 | ACT-02 Nhân viên bán vé | UC-015 Đổi vé tại quầy | Association | - | Tác nhân chính | REQ-36 | Tổng quát; Trả vé và đổi vé |
| RL-26 | ACT-08 Máy in vé | UC-015 Đổi vé tại quầy | Association | - | Tác nhân phụ: in vé giấy mới (ASM-14, chờ Q-40) | REQ-26, REQ-27 | Tổng quát; Trả vé và đổi vé |
| RL-27 | ACT-03 Nhân viên điều hành | UC-016 Lập lịch chạy tuần | Association | - | Tác nhân chính | REQ-46, REQ-51 | Tổng quát |
| RL-28 | ACT-03 Nhân viên điều hành | UC-017 Huỷ chuyến | Association | - | Tác nhân chính | REQ-55 | Tổng quát |
| RL-29 | ACT-06 Cổng thanh toán | UC-017 Huỷ chuyến | Association | - | Tác nhân phụ: hoàn 100% vé mua trực tuyến qua cổng | REQ-16, REQ-57 | Tổng quát |
| RL-30 | ACT-07 Cổng SMS | UC-017 Huỷ chuyến | Association | - | Tác nhân phụ: gửi SMS thông báo huỷ chuyến cho hành khách đã có vé | REQ-21, REQ-56 | Tổng quát |
| RL-31 | ACT-02 Nhân viên bán vé | UC-018 Hoàn tiền mặt chuyến bị huỷ | Association | - | Tác nhân chính | REQ-57, REQ-58, REQ-59 | Tổng quát |
| RL-32 | ACT-03 Nhân viên điều hành | UC-019 Quản lý danh mục bến xe | Association | - | Tác nhân chính | REQ-48 | Tổng quát |
| RL-33 | ACT-03 Nhân viên điều hành | UC-020 Quản lý danh mục tuyến xe | Association | - | Tác nhân chính | REQ-48 | Tổng quát |
| RL-34 | ACT-03 Nhân viên điều hành | UC-021 Quản lý danh mục xe | Association | - | Tác nhân chính | REQ-49 | Tổng quát |
| RL-35 | ACT-03 Nhân viên điều hành | UC-022 Quản lý danh mục tài xế | Association | - | Tác nhân chính | REQ-50 | Tổng quát |
| RL-36 | ACT-04 Quản lý nhà xe | UC-023 Đặt giá vé | Association | - | Tác nhân chính | REQ-60 | Tổng quát |
| RL-37 | ACT-04 Quản lý nhà xe | UC-024 Đặt mức tăng giá ngày lễ | Association | - | Tác nhân chính | REQ-61 | Tổng quát |
| RL-38 | ACT-09 Bộ định thời | UC-025 Gửi danh sách hành khách cho phụ xe | Association | - | Tác nhân chính | REQ-69, REQ-70 | Tổng quát |
| RL-39 | ACT-05 Phụ xe | UC-026 Soát vé hành khách lên xe | Association | - | Tác nhân chính | REQ-63 | Tổng quát |
| RL-40 | ACT-04 Quản lý nhà xe | UC-027 Xem báo cáo doanh thu | Association | - | Tác nhân chính | REQ-71, REQ-72 | Tổng quát |
| RL-41 | ACT-04 Quản lý nhà xe | UC-028 Xem báo cáo tỉ lệ lấp đầy | Association | - | Tác nhân chính | REQ-73 | Tổng quát |
| RL-42 | UC-004 Bán vé tại quầy | UC-008 Tra cứu chuyến xe | Include | - | Bước 3a (UC-008 là UC User-goal mà luồng chọn chuyến và chỗ của UC-004 luôn cần, ASM-03), 3b (bán vé cho chỗ cụ thể thì luôn phải chọn chuyến), 3c (ASM-03). Dùng chung với UC-005, UC-009, UC-014, UC-015 | REQ-29, REQ-05, REQ-06 | Bán vé tại quầy |
| RL-43 | UC-005 Nhận đặt chỗ qua điện thoại | UC-008 Tra cứu chuyến xe | Include | - | Bước 3a (như UC-004), 3b (nhận đặt chỗ luôn phải chọn chuyến và chỗ), 3c (ASM-03) | REQ-29, REQ-05, REQ-06 | Bán vé tại quầy |
| RL-44 | UC-009 Đặt vé trực tuyến | UC-008 Tra cứu chuyến xe | Include | - | Bước 3a (nguồn nêu hành khách tìm chuyến, xem sơ đồ chỗ rồi chọn chỗ, Mục 1 câu 2), 3b (không chọn được chỗ nếu chưa tìm chuyến), 3c (Mục 1 câu 2) | REQ-05, REQ-06, REQ-07 | Đặt vé trực tuyến |
| RL-45 | UC-009 Đặt vé trực tuyến | UC-010 Thanh toán vé trực tuyến | Include | - | Bước 3a (UC-010 là Subfunction giữ theo Q4 d của P02), 3b (vé chỉ được phát hành khi thanh toán thành công), 3c (Mục 3 câu 1 và câu 3) | REQ-15, REQ-18 | Đặt vé trực tuyến |
| RL-46 | UC-014 Đổi vé trực tuyến | UC-008 Tra cứu chuyến xe | Include | - | Bước 3a (UC-008 là UC User-goal mà luồng chọn chuyến mới cùng tuyến luôn cần, ASM-17), 3b (đổi sang chuyến khác thì luôn phải chọn chuyến mới), 3c (Mục 5 câu 4, ASM-17 chờ Q-43) | REQ-34, REQ-05, REQ-06 | Trả vé và đổi vé |
| RL-47 | UC-015 Đổi vé tại quầy | UC-008 Tra cứu chuyến xe | Include | - | Bước 3a (như UC-014, ASM-17), 3b (đổi vé tại quầy luôn phải chọn chuyến mới), 3c (Mục 5 câu 4, ASM-17 chờ Q-43) | REQ-36, REQ-05, REQ-06 | Trả vé và đổi vé |
| RL-48 | UC-010 Thanh toán vé trực tuyến | UC-014 Đổi vé trực tuyến | Extend | {vé mới đắt hơn vé cũ} tại Thu phần chênh lệch | Bước 4a (UC-010 là Subfunction đã được UC-009 include, UC-014 chỉ dùng khi điều kiện đúng, P02 ghi Q4 b), 4b (đổi sang vé rẻ hơn hoặc bằng giá vẫn đạt mục tiêu của UC-014, ASM-05), 4c (có điều kiện và điểm mở rộng) | REQ-44, REQ-45 | Trả vé và đổi vé |

## 2. Điểm mở rộng

| UC gốc | Điểm mở rộng | Vị trí trong luồng (mô tả nghiệp vụ) | UC mở rộng | Điều kiện |
|---|---|---|---|---|
| UC-014 Đổi vé trực tuyến | Thu phần chênh lệch | Bước thu thêm phần chênh lệch sau khi hành khách đã chọn vé mới ở chuyến khác cùng tuyến | UC-010 Thanh toán vé trực tuyến | Vé mới đắt hơn vé cũ |

## 3. UC đề xuất bổ sung

Không có

## 4. Danh sách sơ đồ

| Sơ đồ | Phạm vi | Tác nhân | Use case | File |
|---|---|---|---|---|
| Tổng quát | Toàn hệ thống, không vẽ quan hệ giữa UC; mọi association | ACT-01..ACT-09 (9 tác nhân) | 27 UC (gồm Đăng nhập UC-003; 2 UC Subfunction: UC-003, UC-010) | diagrams/P03-usecase-overview.drawio |
| Đặt vé trực tuyến | UC-008..UC-011, 2 include (UC-009 --> UC-008, UC-009 --> UC-010) | ACT-01, ACT-06, ACT-07 | 4 | diagrams/P03-usecase-online-booking.drawio |
| Bán vé tại quầy | UC-004..UC-007, 2 include (UC-004, UC-005 --> UC-008) | ACT-02, ACT-08, ACT-09 | 4 + UC-008 của nhóm Đặt vé trực tuyến | diagrams/P03-usecase-counter-sales.drawio |
| Trả vé và đổi vé | UC-012, UC-014, UC-015, 2 include (UC-014, UC-015 --> UC-008), 1 extend (UC-010 --> UC-014) | ACT-01, ACT-02, ACT-06, ACT-07, ACT-08 | 3 + UC-008, UC-010 của nhóm Đặt vé trực tuyến | diagrams/P03-usecase-return-exchange.drawio |

Nhóm không có sơ đồ phân rã vì không có quan hệ include, extend, generalization giữa UC: Tài khoản (3 UC), Lịch chạy và chuyến (3), Danh mục (4), Giá vé (2), Soát vé (2), Báo cáo (2).

## 5. Bảng mô hình của từng sơ đồ

### Tổng quát

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống bán vé xe khách SaoViet Bus | - | - | Subject; chứa 27 use case | 200 | 40 | 1000 | 1970 |
| ACT-01 | Actor | Hành khách | - | - | Chính | 60 | 210 | 30 | 60 |
| ACT-02 | Actor | Nhân viên bán vé | - | - | Chính | 60 | 650 | 30 | 60 |
| ACT-03 | Actor | Nhân viên điều hành | - | - | Chính | 60 | 1050 | 30 | 60 |
| ACT-04 | Actor | Quản lý nhà xe | - | - | Chính | 60 | 1450 | 30 | 60 |
| ACT-05 | Actor | Phụ xe | - | - | Chính | 60 | 1700 | 30 | 60 |
| ACT-06 | Actor | Cổng thanh toán | «system» | - | Phụ | 1280 | 750 | 30 | 60 |
| ACT-07 | Actor | Cổng SMS | «system» | - | Phụ | 1280 | 350 | 30 | 60 |
| ACT-08 | Actor | Máy in vé | «device» | - | Phụ | 1280 | 600 | 30 | 60 |
| ACT-09 | Actor | Bộ định thời | - | - | Chính; tác nhân thời gian | 60 | 1880 | 30 | 60 |
| UC-001 | UseCase | Đăng ký tài khoản | - | SYS | - | 280 | 100 | 160 | 70 |
| UC-002 | UseCase | Quản lý tài khoản nhân viên | - | SYS | - | 280 | 1330 | 160 | 70 |
| UC-003 | UseCase | Đăng nhập | - | SYS | Subfunction; nối mọi tác nhân chính theo U-R01 | 760 | 1050 | 160 | 70 |
| UC-004 | UseCase | Bán vé tại quầy | - | SYS | (quan hệ ở sơ đồ Bán vé tại quầy) | 280 | 540 | 160 | 70 |
| UC-005 | UseCase | Nhận đặt chỗ qua điện thoại | - | SYS | (quan hệ ở sơ đồ Bán vé tại quầy) | 520 | 590 | 160 | 70 |
| UC-006 | UseCase | Thu tiền vé đặt qua điện thoại | - | SYS | - | 280 | 650 | 160 | 70 |
| UC-007 | UseCase | Huỷ vé đặt chỗ quá hạn | - | SYS | - | 280 | 1850 | 160 | 70 |
| UC-008 | UseCase | Tra cứu chuyến xe | - | SYS | (quan hệ ở sơ đồ Đặt vé trực tuyến, Bán vé tại quầy, Trả vé và đổi vé) | 520 | 150 | 160 | 70 |
| UC-009 | UseCase | Đặt vé trực tuyến | - | SYS | (quan hệ ở sơ đồ Đặt vé trực tuyến) | 280 | 210 | 160 | 70 |
| UC-010 | UseCase | Thanh toán vé trực tuyến | - | SYS | Subfunction; (quan hệ ở sơ đồ Đặt vé trực tuyến, Trả vé và đổi vé) | 1000 | 840 | 160 | 70 |
| UC-011 | UseCase | Xem lịch sử vé | - | SYS | - | 520 | 260 | 160 | 70 |
| UC-012 | UseCase | Trả vé | - | SYS | - | 280 | 430 | 160 | 70 |
| UC-014 | UseCase | Đổi vé trực tuyến | - | SYS | (quan hệ ở sơ đồ Trả vé và đổi vé) | 280 | 320 | 160 | 70 |
| UC-015 | UseCase | Đổi vé tại quầy | - | SYS | (quan hệ ở sơ đồ Trả vé và đổi vé) | 520 | 700 | 160 | 70 |
| UC-016 | UseCase | Lập lịch chạy tuần | - | SYS | - | 280 | 910 | 160 | 70 |
| UC-017 | UseCase | Huỷ chuyến | - | SYS | - | 520 | 960 | 160 | 70 |
| UC-018 | UseCase | Hoàn tiền mặt chuyến bị huỷ | - | SYS | - | 280 | 760 | 160 | 70 |
| UC-019 | UseCase | Quản lý danh mục bến xe | - | SYS | - | 280 | 1020 | 160 | 70 |
| UC-020 | UseCase | Quản lý danh mục tuyến xe | - | SYS | - | 520 | 1070 | 160 | 70 |
| UC-021 | UseCase | Quản lý danh mục xe | - | SYS | - | 280 | 1130 | 160 | 70 |
| UC-022 | UseCase | Quản lý danh mục tài xế | - | SYS | - | 520 | 1180 | 160 | 70 |
| UC-023 | UseCase | Đặt giá vé | - | SYS | - | 520 | 1380 | 160 | 70 |
| UC-024 | UseCase | Đặt mức tăng giá ngày lễ | - | SYS | - | 280 | 1440 | 160 | 70 |
| UC-025 | UseCase | Gửi danh sách hành khách cho phụ xe | - | SYS | - | 520 | 1900 | 160 | 70 |
| UC-026 | UseCase | Soát vé hành khách lên xe | - | SYS | - | 280 | 1700 | 160 | 70 |
| UC-027 | UseCase | Xem báo cáo doanh thu | - | SYS | - | 520 | 1490 | 160 | 70 |
| UC-028 | UseCase | Xem báo cáo tỉ lệ lấp đầy | - | SYS | - | 280 | 1550 | 160 | 70 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | - | - |
| RL-02 | ACT-04 | UC-002 | Association | - | - | - |
| RL-03 | ACT-01 | UC-003 | Association | - | - | (220,410); (880,410) |
| RL-04 | ACT-02 | UC-003 | Association | - | - | (220,850); (850,850) |
| RL-05 | ACT-03 | UC-003 | Association | - | - | (220,880); (820,880) |
| RL-06 | ACT-04 | UC-003 | Association | - | - | (220,1290); (850,1290) |
| RL-07 | ACT-05 | UC-003 | Association | - | - | (220,1660); (900,1660) |
| RL-08 | ACT-07 | UC-003 | Association | - | - | (1180,1080) |
| RL-09 | ACT-02 | UC-004 | Association | - | - | - |
| RL-10 | ACT-08 | UC-004 | Association | - | - | (1180,570) |
| RL-11 | ACT-02 | UC-005 | Association | - | - | (240,630) |
| RL-12 | ACT-02 | UC-006 | Association | - | - | - |
| RL-13 | ACT-08 | UC-006 | Association | - | - | (1180,680) |
| RL-14 | ACT-09 | UC-007 | Association | - | - | - |
| RL-15 | ACT-01 | UC-008 | Association | - | - | (240,190) |
| RL-16 | ACT-01 | UC-009 | Association | - | - | - |
| RL-17 | ACT-07 | UC-009 | Association | - | - | (1180,240) |
| RL-18 | ACT-06 | UC-010 | Association | - | - | - |
| RL-19 | ACT-01 | UC-011 | Association | - | - | (240,300) |
| RL-20 | ACT-01 | UC-012 | Association | - | - | (220,445) |
| RL-21 | ACT-02 | UC-012 | Association | - | - | (220,485) |
| RL-22 | ACT-06 | UC-012 | Association | - | - | (1180,460) |
| RL-23 | ACT-01 | UC-014 | Association | - | - | - |
| RL-24 | ACT-07 | UC-014 | Association | - | - | (1180,350) |
| RL-25 | ACT-02 | UC-015 | Association | - | - | (240,740) |
| RL-26 | ACT-08 | UC-015 | Association | - | - | (1180,740) |
| RL-27 | ACT-03 | UC-016 | Association | - | - | - |
| RL-28 | ACT-03 | UC-017 | Association | - | - | (240,1000) |
| RL-29 | ACT-06 | UC-017 | Association | - | - | (1180,1000) |
| RL-30 | ACT-07 | UC-017 | Association | - | - | (1180,1000) |
| RL-31 | ACT-02 | UC-018 | Association | - | - | - |
| RL-32 | ACT-03 | UC-019 | Association | - | - | - |
| RL-33 | ACT-03 | UC-020 | Association | - | - | (240,1110) |
| RL-34 | ACT-03 | UC-021 | Association | - | - | - |
| RL-35 | ACT-03 | UC-022 | Association | - | - | (240,1220) |
| RL-36 | ACT-04 | UC-023 | Association | - | - | (240,1420) |
| RL-37 | ACT-04 | UC-024 | Association | - | - | - |
| RL-38 | ACT-09 | UC-025 | Association | - | - | (240,1940) |
| RL-39 | ACT-05 | UC-026 | Association | - | - | - |
| RL-40 | ACT-04 | UC-027 | Association | - | - | (240,1530) |
| RL-41 | ACT-04 | UC-028 | Association | - | - | - |

### Đặt vé trực tuyến

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống bán vé xe khách SaoViet Bus | - | - | Subject | 200 | 40 | 520 | 390 |
| ACT-01 | Actor | Hành khách | - | - | Chính | 60 | 210 | 30 | 60 |
| ACT-06 | Actor | Cổng thanh toán | «system» | - | Phụ | 800 | 320 | 30 | 60 |
| ACT-07 | Actor | Cổng SMS | «system» | - | Phụ | 800 | 210 | 30 | 60 |
| UC-008 | UseCase | Tra cứu chuyến xe | - | SYS | UC được include | 520 | 100 | 160 | 70 |
| UC-009 | UseCase | Đặt vé trực tuyến | - | SYS | UC gốc của hai include | 280 | 210 | 160 | 70 |
| UC-010 | UseCase | Thanh toán vé trực tuyến | - | SYS | Subfunction; UC được include | 520 | 320 | 160 | 70 |
| UC-011 | UseCase | Xem lịch sử vé | - | SYS | - | 280 | 320 | 160 | 70 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-15 | ACT-01 | UC-008 | Association | - | - | (240,140) |
| RL-16 | ACT-01 | UC-009 | Association | - | - | - |
| RL-17 | ACT-07 | UC-009 | Association | - | - | - |
| RL-18 | ACT-06 | UC-010 | Association | - | - | - |
| RL-19 | ACT-01 | UC-011 | Association | - | - | - |
| RL-44 | UC-009 | UC-008 | Include | «include» | - | - |
| RL-45 | UC-009 | UC-010 | Include | «include» | - | - |

### Bán vé tại quầy

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống bán vé xe khách SaoViet Bus | - | - | Subject | 200 | 40 | 520 | 620 |
| ACT-02 | Actor | Nhân viên bán vé | - | - | Chính | 60 | 250 | 30 | 60 |
| ACT-08 | Actor | Máy in vé | «device» | - | Phụ | 800 | 250 | 30 | 60 |
| ACT-09 | Actor | Bộ định thời | - | - | Chính; tác nhân thời gian | 60 | 550 | 30 | 60 |
| UC-004 | UseCase | Bán vé tại quầy | - | SYS | UC gốc của include | 280 | 100 | 160 | 70 |
| UC-005 | UseCase | Nhận đặt chỗ qua điện thoại | - | SYS | UC gốc của include | 280 | 250 | 160 | 70 |
| UC-006 | UseCase | Thu tiền vé đặt qua điện thoại | - | SYS | - | 280 | 400 | 160 | 70 |
| UC-007 | UseCase | Huỷ vé đặt chỗ quá hạn | - | SYS | - | 280 | 550 | 160 | 70 |
| UC-008 | UseCase | Tra cứu chuyến xe | - | SYS | (nhóm Đặt vé trực tuyến); UC được include; association ở sơ đồ Đặt vé trực tuyến | 520 | 170 | 160 | 70 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-09 | ACT-02 | UC-004 | Association | - | - | - |
| RL-10 | ACT-08 | UC-004 | Association | - | - | (700,140) |
| RL-11 | ACT-02 | UC-005 | Association | - | - | - |
| RL-12 | ACT-02 | UC-006 | Association | - | - | - |
| RL-13 | ACT-08 | UC-006 | Association | - | - | (700,440) |
| RL-14 | ACT-09 | UC-007 | Association | - | - | - |
| RL-42 | UC-004 | UC-008 | Include | «include» | - | - |
| RL-43 | UC-005 | UC-008 | Include | «include» | - | - |

### Trả vé và đổi vé

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống bán vé xe khách SaoViet Bus | - | - | Subject | 200 | 40 | 600 | 580 |
| ACT-01 | Actor | Hành khách | - | - | Chính | 60 | 160 | 30 | 60 |
| ACT-02 | Actor | Nhân viên bán vé | - | - | Chính | 60 | 310 | 30 | 60 |
| ACT-06 | Actor | Cổng thanh toán | «system» | - | Phụ | 880 | 60 | 30 | 60 |
| ACT-07 | Actor | Cổng SMS | «system» | - | Phụ | 880 | 160 | 30 | 60 |
| ACT-08 | Actor | Máy in vé | «device» | - | Phụ | 880 | 510 | 30 | 60 |
| UC-008 | UseCase | Tra cứu chuyến xe | - | SYS | (nhóm Đặt vé trực tuyến); UC được include; association ở sơ đồ Đặt vé trực tuyến | 600 | 440 | 160 | 70 |
| UC-010 | UseCase | Thanh toán vé trực tuyến | - | SYS | (nhóm Đặt vé trực tuyến); Subfunction; UC mở rộng; association ở sơ đồ Đặt vé trực tuyến | 320 | 400 | 160 | 70 |
| UC-012 | UseCase | Trả vé | - | SYS | - | 280 | 100 | 160 | 70 |
| UC-014 | UseCase | Đổi vé trực tuyến<br>extension points<br>Thu phần chênh lệch | - | SYS | UC gốc của extend và include; điểm mở rộng: Thu phần chênh lệch | 280 | 210 | 200 | 90 |
| UC-015 | UseCase | Đổi vé tại quầy | - | SYS | UC gốc của include | 280 | 510 | 160 | 70 |
| N-01 | Note | Condition: {vé mới đắt hơn vé cũ}<br>extension point: Thu phần chênh lệch | - | SYS | Điều kiện extend của RL-48 | 520 | 260 | 200 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-20 | ACT-01 | UC-012 | Association | - | - | - |
| RL-21 | ACT-02 | UC-012 | Association | - | - | - |
| RL-22 | ACT-06 | UC-012 | Association | - | - | - |
| RL-23 | ACT-01 | UC-014 | Association | - | - | - |
| RL-24 | ACT-07 | UC-014 | Association | - | - | - |
| RL-25 | ACT-02 | UC-015 | Association | - | - | - |
| RL-26 | ACT-08 | UC-015 | Association | - | - | - |
| RL-46 | UC-014 | UC-008 | Include | «include» | - | - |
| RL-47 | UC-015 | UC-008 | Include | «include» | - | - |
| RL-48 | UC-010 | UC-014 | Extend | «extend» | - | - |
| RL-48-N | N-01 | RL-48 | NoteLink | - | Đường nối note tới đường extend | - |

## 6. Nội dung file .drawio

Các file đã ghi, không chép lại XML:

- bus-r2/design/diagrams/P03-usecase-overview.drawio
- bus-r2/design/diagrams/P03-usecase-online-booking.drawio
- bus-r2/design/diagrams/P03-usecase-counter-sales.drawio
- bus-r2/design/diagrams/P03-usecase-return-exchange.drawio

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-43 | Khi đổi vé (UC-014, UC-015), người đổi có tìm chuyến mới cùng tuyến và xem sơ đồ chỗ của chuyến mới bằng đoạn tương tác tìm chuyến như khi đặt vé không? (Có, dùng chung đoạn tìm chuyến và xem chỗ của UC-008 / Không, chuyến mới được chọn theo cách khác) | RL include UC-014 --> UC-008, UC-015 --> UC-008; ASM-17 | Mục 5, câu 4 "đổi sang chuyến khác cùng tuyến" không nêu cách chọn chuyến mới; Mục 1, câu 2 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-17 | Khi đổi vé, người đổi (hành khách ở UC-014, nhân viên bán vé ở UC-015) chọn chuyến mới cùng tuyến và chỗ mới bằng đoạn tìm chuyến và xem sơ đồ chỗ của UC-008, nên UC-014 và UC-015 cùng include UC-008. | Chờ Q-43. Nguồn nêu đổi sang chuyến khác cùng tuyến nhưng không nêu cách chọn chuyến; chọn phương án dùng chung đoạn tìm chuyến đã có để có căn cứ cho include theo Bước 3c | Include UC-014 --> UC-008, UC-015 --> UC-008; REQ-34, REQ-36 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Mục Target 8 (D-AP15) chưa đạt hẳn: sơ đồ Tổng quát có 24 giao điểm giữa các đường nối (đã kiểm bằng toạ độ: không đường nào cắt qua elip hay tác nhân). Trong đó 10 giao điểm do đường từ ACT-01, ACT-02, ACT-03 tới UC-003 (RL-03, RL-04, RL-05) cắt các đường đi sang tác nhân phụ bên phải, 6 giao điểm của RL-08 (UC-003 tới Cổng SMS), 8 giao điểm giữa các đường đi sang ba tác nhân phụ. Không tác nhân nào nối quá 7 UC. Thử đổi vị trí ba tác nhân phụ (lưới 60) không giảm được số giao điểm dưới 24. Sơ đồ Trả vé và đổi vé có 1 giao điểm (RL-21 cắt RL-23 phía tác nhân chính).
- Các mục Target còn lại đạt.
- Kế hoạch sơ đồ (Bước 8): N = 27 UC (kể cả UC-003 Đăng nhập và UC-010 Subfunction) và M = 9 tác nhân, M trên 8 nên chọn phương án sơ đồ tổng quát chỉ vẽ association. Ba nhóm có include hoặc extend giữa UC có sơ đồ phân rã; sáu nhóm còn lại không có sơ đồ phân rã.
- Lựa chọn khi prompt không nói rõ: quan hệ giữa UC khác nhóm (UC-004, UC-005, UC-014, UC-015 include UC-008; UC-010 extend UC-014) được vẽ ở sơ đồ phân rã của nhóm chứa UC gốc. UC của nhóm khác chỉ vẽ làm đầu mút quan hệ, ghi chú "(nhóm <tên>)", không vẽ association của nó. Vì vậy sơ đồ Đặt vé trực tuyến không vẽ bốn include đi tới UC-008 từ nhóm khác; các include này ghi ở Mục 1 và ở cột Ghi chú của UC-008.
- Lựa chọn khi hai quy tắc xung đột (Conventions C9): L-12 đặt cột hai lệch 55 so với cột một, trong khi L-10 và Conventions C7.1, C7.3 đòi mọi toạ độ là bội số của 10. Dùng độ lệch 50. Điểm uốn lấy bội số của 10 nên đoạn cuối tới elip lệch tối đa 5 so với tâm elip.
- Nhãn UC-014 trên sơ đồ Tổng quát không có ngăn extension points vì extend không vẽ ở sơ đồ này; ngăn extension points chỉ có ở sơ đồ Trả vé và đổi vé, nơi vẽ RL-48.
- UC-010 vừa được UC-009 include vừa là UC mở rộng của UC-014: không tạo chu trình, include chỉ một tầng.
- Số quan hệ include cộng extend là 7, không vượt khoảng một phần ba của 25 UC User-goal (8,3). Tỷ lệ UC Subfunction là 2 trên 27 UC, khoảng 7%, dưới 20%.
- Quan hệ phụ thuộc câu hỏi mở của bước trước: RL-13 và RL-26 (Máy in vé nối UC-006, UC-015) chờ Q-40; RL-21 (UC-012 nối Nhân viên bán vé) và việc khôi phục UC-013 chờ Q-41; RL-24 (Cổng SMS nối UC-014) chờ Q-42; RL-48 (extend UC-010 --> UC-014) chờ Q-22 qua ASM-13; hai include tới UC-008 từ UC-014, UC-015 chờ Q-43.
