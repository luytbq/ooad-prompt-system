# P03 - Mô hình và sơ đồ use case - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P03 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0); P01-actors.md (phiên bản 1.0); P02-usecases.md (phiên bản 1.1); yeu-cau-phong-tap.md; P02R-review.md (phiên bản 1.0). P02R 1.0: UCR-01, UCR-02, UCR-03 đã áp dụng ở P02 1.1; không có UCR nào không áp dụng. KIEU_DUONG_ASSOCIATION: MUI_TEN_KHOI_XUONG. CACH_PHAN_RA_SO_DO: THEO_TAC_NHAN. YEU_CAU_BO_SUNG: Không có |
| Phạm vi | Toàn hệ thống |
| Mã Q, ASM cuối đã cấp | Q-49 (P03 không cấp Q mới); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Bảng quan hệ

| ID | Nguồn | Đích | Loại | Điều kiện extend / điểm mở rộng | Lý do | REQ | Sơ đồ |
|---|---|---|---|---|---|---|---|
| RL-01 | ACT-01 Người quan tâm | UC-001 Xem giá gói tập | Association | - | Tác nhân chính | REQ-06 | Tổng quát |
| RL-02 | ACT-01 Người quan tâm | UC-002 Xem lịch lớp nhóm | Association | - | Tác nhân chính | REQ-07 | Tổng quát |
| RL-03 | ACT-01 Người quan tâm | UC-003 Đăng ký tài khoản hội viên | Association | - | Tác nhân chính | REQ-08 | Tổng quát |
| RL-04 | ACT-02 Hội viên | UC-004 Đăng nhập | Association | - | Tác nhân chính | REQ-06, REQ-07, REQ-08 | Tổng quát |
| RL-05 | ACT-02 Hội viên | UC-005 Mua hoặc gia hạn gói tập | Association | - | Tác nhân chính | REQ-11, REQ-12, REQ-13 | Tổng quát |
| RL-06 | ACT-05 Lễ tân | UC-005 Mua hoặc gia hạn gói tập | Association | - | Tác nhân chính | REQ-18, REQ-19, REQ-20, REQ-21 | Tổng quát |
| RL-07 | ACT-08 Cổng thanh toán | UC-005 Mua hoặc gia hạn gói tập | Association | - | Tác nhân phụ: thu tiền thanh toán trực tuyến, trả kết quả thanh toán | REQ-13, REQ-14 | Tổng quát |
| RL-08 | ACT-11 Hệ thống hoá đơn điện tử | UC-005 Mua hoặc gia hạn gói tập | Association | - | Tác nhân phụ: nhận dữ liệu giao dịch thu tiền để xuất hoá đơn điện tử | REQ-91, REQ-92 | Tổng quát |
| RL-09 | ACT-02 Hội viên | UC-006 Bảo lưu gói tập | Association | - | Tác nhân chính | REQ-46 | Tổng quát |
| RL-10 | ACT-05 Lễ tân | UC-007 Chuyển nhượng gói tập | Association | - | Tác nhân chính | REQ-52, REQ-54 | Tổng quát |
| RL-11 | ACT-11 Hệ thống hoá đơn điện tử | UC-007 Chuyển nhượng gói tập | Association | - | Tác nhân phụ: nhận dữ liệu giao dịch thu tiền để xuất hoá đơn điện tử | REQ-91, REQ-92 | Tổng quát |
| RL-12 | ACT-13 Bộ định thời hằng ngày | UC-008 Nhắc gia hạn gói tập | Association | - | Tác nhân chính | REQ-84, REQ-85, REQ-86 | Tổng quát |
| RL-13 | ACT-09 Cổng SMS | UC-008 Nhắc gia hạn gói tập | Association | - | Tác nhân phụ: gửi SMS tới hội viên chưa cài ứng dụng | REQ-88, REQ-90 | Tổng quát |
| RL-14 | ACT-10 Dịch vụ thông báo đẩy | UC-008 Nhắc gia hạn gói tập | Association | - | Tác nhân phụ: gửi thông báo đẩy tới ứng dụng của hội viên | REQ-87, REQ-89 | Tổng quát |
| RL-15 | ACT-06 Quản lý chi nhánh | UC-009 Lập lịch lớp nhóm | Association | - | Tác nhân chính | REQ-69 | Tổng quát |
| RL-16 | ACT-02 Hội viên | UC-010 Đặt chỗ lớp nhóm | Association | - | Tác nhân chính | REQ-22, REQ-26 | Tổng quát |
| RL-17 | ACT-02 Hội viên | UC-011 Huỷ chỗ lớp nhóm | Association | - | Tác nhân chính | REQ-32 | Tổng quát |
| RL-18 | ACT-09 Cổng SMS | UC-011 Huỷ chỗ lớp nhóm | Association | - | Tác nhân phụ: gửi SMS tới hội viên chưa cài ứng dụng | REQ-27, REQ-88, REQ-90 | Tổng quát |
| RL-19 | ACT-10 Dịch vụ thông báo đẩy | UC-011 Huỷ chỗ lớp nhóm | Association | - | Tác nhân phụ: gửi thông báo đẩy tới ứng dụng của hội viên | REQ-27, REQ-87, REQ-89 | Tổng quát |
| RL-20 | ACT-02 Hội viên | UC-012 Nhận chỗ từ danh sách chờ | Association | - | Tác nhân chính | REQ-28, REQ-29 | Tổng quát |
| RL-21 | ACT-14 Bộ định thời theo hạn | UC-013 Chuyển chỗ cho người kế tiếp | Association | - | Tác nhân chính | REQ-30, REQ-31 | Tổng quát |
| RL-22 | ACT-06 Quản lý chi nhánh | UC-014 Huỷ lớp nhóm vì sự cố | Association | - | Tác nhân chính | REQ-76 | Tổng quát |
| RL-23 | ACT-09 Cổng SMS | UC-014 Huỷ lớp nhóm vì sự cố | Association | - | Tác nhân phụ: gửi SMS tới hội viên chưa cài ứng dụng | REQ-77, REQ-88, REQ-90 | Tổng quát |
| RL-24 | ACT-10 Dịch vụ thông báo đẩy | UC-014 Huỷ lớp nhóm vì sự cố | Association | - | Tác nhân phụ: gửi thông báo đẩy tới ứng dụng của hội viên | REQ-77, REQ-87, REQ-89 | Tổng quát |
| RL-25 | ACT-14 Bộ định thời theo hạn | UC-015 Huỷ lớp nhóm ít người đặt | Association | - | Tác nhân chính | REQ-73, REQ-74 | Tổng quát |
| RL-26 | ACT-09 Cổng SMS | UC-015 Huỷ lớp nhóm ít người đặt | Association | - | Tác nhân phụ: gửi SMS tới hội viên chưa cài ứng dụng | REQ-75, REQ-88, REQ-90 | Tổng quát |
| RL-27 | ACT-10 Dịch vụ thông báo đẩy | UC-015 Huỷ lớp nhóm ít người đặt | Association | - | Tác nhân phụ: gửi thông báo đẩy tới ứng dụng của hội viên | REQ-75, REQ-87, REQ-89 | Tổng quát |
| RL-28 | ACT-14 Bộ định thời theo hạn | UC-016 Ghi nhận vắng mặt lớp nhóm | Association | - | Tác nhân chính | REQ-34, REQ-36 | Tổng quát |
| RL-29 | ACT-05 Lễ tân | UC-017 Bán vé tập một ngày | Association | - | Tác nhân chính | REQ-42, REQ-43 | Tổng quát |
| RL-30 | ACT-11 Hệ thống hoá đơn điện tử | UC-017 Bán vé tập một ngày | Association | - | Tác nhân phụ: nhận dữ liệu giao dịch thu tiền để xuất hoá đơn điện tử | REQ-91, REQ-92 | Tổng quát |
| RL-31 | ACT-02 Hội viên | UC-018 Vào chi nhánh | Association | - | Tác nhân chính | REQ-39 | Tổng quát |
| RL-32 | ACT-03 Khách vãng lai | UC-018 Vào chi nhánh | Association | - | Tác nhân chính | REQ-44, REQ-45 | Tổng quát |
| RL-33 | ACT-12 Cửa quay | UC-018 Vào chi nhánh | Association | - | Tác nhân phụ: gửi mã QR đọc được, nhận kết quả cho phép vào và mở cửa | REQ-40, REQ-41 | Tổng quát |
| RL-34 | ACT-02 Hội viên | UC-019 Mua gói buổi tập cá nhân | Association | - | Tác nhân chính | REQ-56 | Tổng quát |
| RL-35 | ACT-11 Hệ thống hoá đơn điện tử | UC-019 Mua gói buổi tập cá nhân | Association | - | Tác nhân phụ: nhận dữ liệu giao dịch thu tiền để xuất hoá đơn điện tử | REQ-91, REQ-92 | Tổng quát |
| RL-36 | ACT-02 Hội viên | UC-020 Đặt buổi tập cá nhân | Association | - | Tác nhân chính | REQ-59 | Tổng quát |
| RL-37 | ACT-04 Huấn luyện viên | UC-021 Phản hồi yêu cầu đặt buổi tập | Association | - | Tác nhân chính | REQ-60, REQ-61 | Tổng quát |
| RL-38 | ACT-14 Bộ định thời theo hạn | UC-022 Huỷ yêu cầu đặt buổi quá hạn | Association | - | Tác nhân chính | REQ-61, REQ-62 | Tổng quát |
| RL-39 | ACT-02 Hội viên | UC-023 Huỷ buổi tập cá nhân | Association | - | Tác nhân chính | REQ-63 | Tổng quát |
| RL-40 | ACT-04 Huấn luyện viên | UC-024 Ghi nhận buổi tập cá nhân | Association | - | Tác nhân chính | REQ-65, REQ-66 | Tổng quát |
| RL-41 | ACT-02 Hội viên | UC-025 Xem chỉ số cơ thể | Association | - | Tác nhân chính | REQ-68 | Tổng quát |
| RL-42 | ACT-04 Huấn luyện viên | UC-025 Xem chỉ số cơ thể | Association | - | Tác nhân chính | REQ-68 | Tổng quát |
| RL-43 | ACT-07 Giám đốc chuỗi | UC-026 Đặt giá gói tập | Association | - | Tác nhân chính | REQ-78 | Tổng quát |
| RL-44 | ACT-07 Giám đốc chuỗi | UC-027 Đặt chương trình khuyến mãi | Association | - | Tác nhân chính | REQ-79 | Tổng quát |
| RL-45 | ACT-07 Giám đốc chuỗi | UC-028 Xem báo cáo chuỗi | Association | - | Tác nhân chính | REQ-81, REQ-82, REQ-83 | Tổng quát |

Không có quan hệ Include, Extend, Generalization giữa use case và không có Generalization giữa tác nhân; căn cứ ở mục Vấn đề còn mở. Mô hình gồm 45 association (RL-01 đến RL-45).

## 2. Điểm mở rộng

| UC gốc | Điểm mở rộng | Vị trí trong luồng (mô tả nghiệp vụ) | UC mở rộng | Điều kiện |
|---|---|---|---|---|
| Không có | - | - | - | - |

## 3. UC đề xuất bổ sung

Không có.

## 4. Danh sách sơ đồ

| Sơ đồ | Phạm vi | Tác nhân | Use case | File |
|---|---|---|---|---|
| Tổng quát | Toàn hệ thống, chỉ vẽ association, không có quan hệ giữa UC | ACT-01..ACT-14 (14 tác nhân) | UC-001..UC-028 (28 UC, gồm UC-004 Đăng nhập) | diagrams/P03-usecase-overview.drawio |

Không có sơ đồ phân rã: không nhóm chức năng hay tác nhân nào có quan hệ Include, Extend hoặc Generalization giữa UC (Bước 8, phương án N từ 21 đến 40).

## 5. Bảng mô hình của từng sơ đồ

### Tổng quát

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống quản lý chuỗi phòng tập VietFit | - | - | Subject; không chứa tác nhân | 200 | 40 | 900 | 2370 |
| ACT-01 | Actor | Người quan tâm | - | - | - | 60 | 180 | 30 | 60 |
| ACT-02 | Actor | Hội viên | - | - | - | 60 | 790 | 30 | 60 |
| ACT-03 | Actor | Khách vãng lai | - | - | Chỉ nối UC-018 (UC cột giữa) | 60 | 1180 | 30 | 60 |
| ACT-04 | Actor | Huấn luyện viên | - | - | - | 60 | 1360 | 30 | 60 |
| ACT-05 | Actor | Lễ tân | - | - | - | 60 | 410 | 30 | 60 |
| ACT-06 | Actor | Quản lý chi nhánh | - | - | - | 60 | 1560 | 30 | 60 |
| ACT-07 | Actor | Giám đốc chuỗi | - | - | - | 60 | 1790 | 30 | 60 |
| ACT-08 | Actor | Cổng thanh toán | «system» | - | - | 1180 | 700 | 30 | 60 |
| ACT-09 | Actor | Cổng SMS | «system» | - | - | 1180 | 2020 | 30 | 60 |
| ACT-10 | Actor | Dịch vụ thông báo đẩy | «system» | - | - | 1180 | 2180 | 30 | 60 |
| ACT-11 | Actor | Hệ thống hoá đơn điện tử | «system» | - | - | 1180 | 580 | 30 | 60 |
| ACT-12 | Actor | Cửa quay | «device» | - | - | 1180 | 1130 | 30 | 60 |
| ACT-13 | Actor | Bộ định thời hằng ngày | - | - | - | 60 | 2000 | 30 | 60 |
| ACT-14 | Actor | Bộ định thời theo hạn | - | - | - | 60 | 2220 | 30 | 60 |
| UC-001 | UseCase | Xem giá gói tập | - | SYS | Nhóm Tiếp cận và tài khoản | 280 | 120 | 160 | 70 |
| UC-002 | UseCase | Xem lịch lớp nhóm | - | SYS | Nhóm Tiếp cận và tài khoản | 520 | 170 | 160 | 70 |
| UC-003 | UseCase | Đăng ký tài khoản hội viên | - | SYS | Nhóm Tiếp cận và tài khoản | 280 | 230 | 160 | 70 |
| UC-004 | UseCase | Đăng nhập | - | SYS | Nhóm Tiếp cận và tài khoản; Subfunction, không include (P02 U-R01) | 280 | 650 | 160 | 70 |
| UC-005 | UseCase | Mua hoặc gia hạn gói tập | - | SYS | Nhóm Gói tập; nối hai tác nhân chính ACT-02, ACT-05, đặt giữa hai dải | 280 | 540 | 160 | 70 |
| UC-006 | UseCase | Bảo lưu gói tập | - | SYS | Nhóm Gói tập | 280 | 870 | 160 | 70 |
| UC-007 | UseCase | Chuyển nhượng gói tập | - | SYS | Nhóm Gói tập | 280 | 380 | 160 | 70 |
| UC-008 | UseCase | Nhắc gia hạn gói tập | - | SYS | Nhóm Gói tập | 280 | 1990 | 160 | 70 |
| UC-009 | UseCase | Lập lịch lớp nhóm | - | SYS | Nhóm Lớp nhóm | 280 | 1530 | 160 | 70 |
| UC-010 | UseCase | Đặt chỗ lớp nhóm | - | SYS | Nhóm Lớp nhóm | 520 | 920 | 160 | 70 |
| UC-011 | UseCase | Huỷ chỗ lớp nhóm | - | SYS | Nhóm Lớp nhóm | 280 | 980 | 160 | 70 |
| UC-012 | UseCase | Nhận chỗ từ danh sách chờ | - | SYS | Nhóm Lớp nhóm | 520 | 1030 | 160 | 70 |
| UC-013 | UseCase | Chuyển chỗ cho người kế tiếp | - | SYS | Nhóm Lớp nhóm | 280 | 2140 | 160 | 70 |
| UC-014 | UseCase | Huỷ lớp nhóm vì sự cố | - | SYS | Nhóm Lớp nhóm | 520 | 1580 | 160 | 70 |
| UC-015 | UseCase | Huỷ lớp nhóm ít người đặt | - | SYS | Nhóm Lớp nhóm | 520 | 2190 | 160 | 70 |
| UC-016 | UseCase | Ghi nhận vắng mặt lớp nhóm | - | SYS | Nhóm Lớp nhóm | 280 | 2250 | 160 | 70 |
| UC-017 | UseCase | Bán vé tập một ngày | - | SYS | Nhóm Ra vào chi nhánh | 520 | 430 | 160 | 70 |
| UC-018 | UseCase | Vào chi nhánh | - | SYS | Nhóm Ra vào chi nhánh; nối hai tác nhân chính ACT-02, ACT-03, đặt ở cột giữa | 760 | 1120 | 160 | 70 |
| UC-019 | UseCase | Mua gói buổi tập cá nhân | - | SYS | Nhóm Huấn luyện cá nhân | 520 | 700 | 160 | 70 |
| UC-020 | UseCase | Đặt buổi tập cá nhân | - | SYS | Nhóm Huấn luyện cá nhân | 280 | 760 | 160 | 70 |
| UC-021 | UseCase | Phản hồi yêu cầu đặt buổi tập | - | SYS | Nhóm Huấn luyện cá nhân | 280 | 1330 | 160 | 70 |
| UC-022 | UseCase | Huỷ yêu cầu đặt buổi quá hạn | - | SYS | Nhóm Huấn luyện cá nhân | 520 | 2300 | 160 | 70 |
| UC-023 | UseCase | Huỷ buổi tập cá nhân | - | SYS | Nhóm Huấn luyện cá nhân | 520 | 810 | 160 | 70 |
| UC-024 | UseCase | Ghi nhận buổi tập cá nhân | - | SYS | Nhóm Huấn luyện cá nhân | 520 | 1380 | 160 | 70 |
| UC-025 | UseCase | Xem chỉ số cơ thể | - | SYS | Nhóm Huấn luyện cá nhân; nối hai tác nhân chính ACT-02, ACT-04, đặt ở cột giữa | 760 | 1270 | 160 | 70 |
| UC-026 | UseCase | Đặt giá gói tập | - | SYS | Nhóm Giá và báo cáo | 280 | 1730 | 160 | 70 |
| UC-027 | UseCase | Đặt chương trình khuyến mãi | - | SYS | Nhóm Giá và báo cáo | 520 | 1780 | 160 | 70 |
| UC-028 | UseCase | Xem báo cáo chuỗi | - | SYS | Nhóm Giá và báo cáo | 280 | 1840 | 160 | 70 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | Tác nhân chính --> use case | (240,210); (240,150) |
| RL-02 | ACT-01 | UC-002 | Association | - | Tác nhân chính --> use case | - |
| RL-03 | ACT-01 | UC-003 | Association | - | Tác nhân chính --> use case | (240,210); (240,260) |
| RL-04 | ACT-02 | UC-004 | Association | - | Tác nhân chính --> use case | (240,820); (240,680) |
| RL-05 | ACT-02 | UC-005 | Association | - | Tác nhân chính --> use case | (240,820); (240,560) |
| RL-06 | ACT-05 | UC-005 | Association | - | Tác nhân chính --> use case | (240,440); (240,580) |
| RL-07 | UC-005 | ACT-08 | Association | - | Use case --> tác nhân phụ | (960,580); (960,730) |
| RL-08 | UC-005 | ACT-11 | Association | - | Use case --> tác nhân phụ | (1040,560); (1040,610) |
| RL-09 | ACT-02 | UC-006 | Association | - | Tác nhân chính --> use case | (240,820); (240,900) |
| RL-10 | ACT-05 | UC-007 | Association | - | Tác nhân chính --> use case | (240,440); (240,410) |
| RL-11 | UC-007 | ACT-11 | Association | - | Use case --> tác nhân phụ | (1040,410); (1040,610) |
| RL-12 | ACT-13 | UC-008 | Association | - | Tác nhân chính --> use case | - |
| RL-13 | UC-008 | ACT-09 | Association | - | Use case --> tác nhân phụ | (1020,2010); (1020,2050) |
| RL-14 | UC-008 | ACT-10 | Association | - | Use case --> tác nhân phụ | (980,2030); (980,2210) |
| RL-15 | ACT-06 | UC-009 | Association | - | Tác nhân chính --> use case | (240,1590); (240,1560) |
| RL-16 | ACT-02 | UC-010 | Association | - | Tác nhân chính --> use case | (240,820); (240,950) |
| RL-17 | ACT-02 | UC-011 | Association | - | Tác nhân chính --> use case | (240,820); (240,1010) |
| RL-18 | UC-011 | ACT-09 | Association | - | Use case --> tác nhân phụ | (1020,1000); (1020,2050) |
| RL-19 | UC-011 | ACT-10 | Association | - | Use case --> tác nhân phụ | (980,1020); (980,2210) |
| RL-20 | ACT-02 | UC-012 | Association | - | Tác nhân chính --> use case | (240,820); (240,1060) |
| RL-21 | ACT-14 | UC-013 | Association | - | Tác nhân chính --> use case | (240,2250); (240,2170) |
| RL-22 | ACT-06 | UC-014 | Association | - | Tác nhân chính --> use case | (240,1590); (240,1610) |
| RL-23 | UC-014 | ACT-09 | Association | - | Use case --> tác nhân phụ | (1020,1600); (1020,2050) |
| RL-24 | UC-014 | ACT-10 | Association | - | Use case --> tác nhân phụ | (980,1620); (980,2210) |
| RL-25 | ACT-14 | UC-015 | Association | - | Tác nhân chính --> use case | (240,2250); (240,2220) |
| RL-26 | UC-015 | ACT-09 | Association | - | Use case --> tác nhân phụ | (1020,2210); (1020,2050) |
| RL-27 | UC-015 | ACT-10 | Association | - | Use case --> tác nhân phụ | (980,2230); (980,2210) |
| RL-28 | ACT-14 | UC-016 | Association | - | Tác nhân chính --> use case | (240,2250); (240,2280) |
| RL-29 | ACT-05 | UC-017 | Association | - | Tác nhân chính --> use case | (240,440); (240,460) |
| RL-30 | UC-017 | ACT-11 | Association | - | Use case --> tác nhân phụ | (1040,460); (1040,610) |
| RL-31 | ACT-02 | UC-018 | Association | - | Tác nhân chính --> use case | (220,820); (220,1150) |
| RL-32 | ACT-03 | UC-018 | Association | - | Tác nhân chính --> use case | (220,1210); (220,1150) |
| RL-33 | UC-018 | ACT-12 | Association | - | Use case --> tác nhân phụ | - |
| RL-34 | ACT-02 | UC-019 | Association | - | Tác nhân chính --> use case | (240,820); (240,730) |
| RL-35 | UC-019 | ACT-11 | Association | - | Use case --> tác nhân phụ | (1040,730); (1040,610) |
| RL-36 | ACT-02 | UC-020 | Association | - | Tác nhân chính --> use case | (240,820); (240,790) |
| RL-37 | ACT-04 | UC-021 | Association | - | Tác nhân chính --> use case | (240,1390); (240,1360) |
| RL-38 | ACT-14 | UC-022 | Association | - | Tác nhân chính --> use case | (240,2250); (240,2330) |
| RL-39 | ACT-02 | UC-023 | Association | - | Tác nhân chính --> use case | (240,820); (240,840) |
| RL-40 | ACT-04 | UC-024 | Association | - | Tác nhân chính --> use case | (240,1390); (240,1410) |
| RL-41 | ACT-02 | UC-025 | Association | - | Tác nhân chính --> use case | (220,820); (220,1290) |
| RL-42 | ACT-04 | UC-025 | Association | - | Tác nhân chính --> use case | (220,1390); (220,1310) |
| RL-43 | ACT-07 | UC-026 | Association | - | Tác nhân chính --> use case | (240,1820); (240,1760) |
| RL-44 | ACT-07 | UC-027 | Association | - | Tác nhân chính --> use case | - |
| RL-45 | ACT-07 | UC-028 | Association | - | Tác nhân chính --> use case | (240,1820); (240,1870) |

## 6. Nội dung file .drawio

- diagrams/P03-usecase-overview.drawio

## 7. Các mục kiểm soát

### Câu hỏi mở

Không có. P03 không cấp Q-nn mới; các câu hỏi làm đổi mô hình này đã có ở P00, P01, P02 và được dẫn ở mục Vấn đề còn mở.

### Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

### Đề xuất sửa artifact trước

Không có.

### Vấn đề còn mở

Mọi mục Target đạt, với các điểm cần người dùng lưu ý:

- Quan hệ giữa use case đã xét và không tạo. (a) UC-004 Đăng nhập không được UC nào include: xác thực đăng nhập của mọi UC dùng tiền điều kiện (Bước 3), P02 giữ Subfunction theo U-R01 và ghi "không nối include"; UC-004 chỉ nối ACT-02, các vai trò khác chờ Q-47. (b) Gửi thông báo đẩy, gửi SMS (UC-008, UC-011, UC-014, UC-015) và xuất hoá đơn điện tử (UC-005, UC-007, UC-017, UC-019) được P02 kết luận là bước của từng UC (CAND-64, CAND-65, CAND-16, không đạt Q4 a); P03 không tạo include và không đề xuất UC mới theo Bước 7, ACT-09, ACT-10, ACT-11 nối trực tiếp với từng UC. (c) Các UC cùng một chuỗi nghiệp vụ nhưng khác phiên và khác tác nhân chính hoặc sự kiện kích hoạt (UC-011, UC-012, UC-013; UC-020, UC-021, UC-022) không phải include vì UC kia vẫn đạt mục tiêu khi không có chúng, và không phải extend vì không có điểm mở rộng nằm trong luồng của UC gốc (P02 U-R07, U-R13). Q-49 trả lời "Có, lặp lại cách xử lý" thì rà lại quan hệ giữa UC-012 và UC-013. (d) UC-014 và UC-015 cùng huỷ lớp nhưng khác tác nhân chính, sự kiện kích hoạt; P02 không có UC cha trừu tượng và nguồn không mô tả khác biệt luồng giữa hai dạng, nên không tạo generalization.
- Bước 8: N = 28 UC, M = 14 tác nhân (M trên 8), theo phương án thứ hai: sơ đồ tổng quát gồm mọi tác nhân, mọi UC và mọi association. Không nhóm chức năng hay tác nhân nào có quan hệ giữa UC nên không tạo sơ đồ phân rã; CACH_PHAN_RA_SO_DO = THEO_TAC_NHAN không có tác dụng ở lần chạy này. Sơ đồ cao 2370 đơn vị vì 14 tác nhân và bố cục dải của L-12.
- Lựa chọn giữa hai quy tắc (Conventions C9): L-12 yêu cầu cột hai lệch xuống 55 so với cột một, trong khi L-10 và Conventions C7.3 yêu cầu mọi toạ độ là bội số của 10; dùng độ lệch 50. Tâm dọc của UC (y + 35) kết thúc bằng 5 nên điểm uốn đặt tại tâm dọc làm tròn xuống 5 đơn vị (ví dụ tâm 155, điểm uốn 150).
- L-12 đặt điểm uốn của đường tới UC cột hai tại cạnh trái boundary + 40, trùng cạnh trái của UC cột một khi lề trong là 40; dùng lề trong 80 (cột một x = 280, điểm uốn x = 240), lề trong vẫn không nhỏ hơn mức tối thiểu 40 của L-01. Đường tới UC cột giữa dùng điểm uốn x = 220 (cạnh trái boundary + 20).
- Hướng đường association ở bảng Edge theo KIEU_DUONG_ASSOCIATION = MUI_TEN_KHOI_XUONG: tác nhân chính là nguồn, UC là nguồn của đường tới tác nhân phụ. Mục 1 ghi nguồn là tác nhân cho mọi association theo Phần B, nên với tác nhân phụ cột Nguồn của Mục 1 và bảng Edge đảo nhau; ID RL-nn giống nhau.
- Thứ tự dải từ trên xuống: ACT-01, ACT-05 (UC-005 nằm giữa hai dải ACT-05 và ACT-02), ACT-02, ACT-03, ACT-04, ACT-06, ACT-07, ACT-13, ACT-14. ACT-01 đặt trên cùng vì gắn với UC khởi đầu quy trình (L-02) dù ACT-02 có nhiều UC nhất; ACT-05 đặt ngay trên ACT-02 và các UC của ACT-02 sắp để UC-019 nằm trước UC-011 nhằm các đường tới ACT-11 và các đường tới ACT-09, ACT-10 không chồng phạm vi dọc (L-09). Còn 8 cặp đường association cắt nhau (chủ yếu ở hành lang bên phải boundary và hành lang UC-018, UC-025), không đường nào cắt qua elip; không thể bỏ hết vì 14 tác nhân và 45 đường trên một sơ đồ (D-AP15).
- Mỗi UC nối hai tác nhân phụ cùng loại kênh (UC-005 với ACT-08, ACT-11; UC-008, UC-011, UC-014, UC-015 với ACT-09, ACT-10) có hai đường rời UC lệch nhau 20 đơn vị theo trục dọc để không chồng lên nhau; UC-005 và UC-025 có hai đường vào từ hai tác nhân chính cũng lệch nhau 20 đơn vị.
- Mô hình phụ thuộc các câu hỏi chưa trả lời ở các bước trước: Q-46 (ACT-02 có nối UC-001, UC-002 không), Q-47 (thêm tác nhân nối UC-004), Q-48 (thêm ACT-05 nối UC-006), Q-45 (thêm UC của ACT-08), Q-49 (thêm ACT-09, ACT-10 nối UC-013), Q-43, Q-01, Q-11 (có thể thêm hoặc đổi UC, tác nhân). Chạy lại P03 khi P01 hoặc P02 thay đổi; giữ nguyên mã RL-nn đã cấp.
- Thứ tự từ trên xuống của các UC do ACT-14 khởi xướng (UC-013, UC-015, UC-016, UC-022) theo mã UC, vì nguồn không cho trình tự thời gian giữa bốn mốc hạn độc lập.
