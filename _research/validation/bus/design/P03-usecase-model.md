# P03 - Mô hình use case - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P03 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.1; P02R-review.md 1.0 (đối chiếu: UCR-01 đến UCR-04 đã được P02 1.1 áp dụng); yeu-cau-xe-khach.md (bản hiện có) |
| Phạm vi | Toàn hệ thống |

## 1. Bảng quan hệ

| ID | Nguồn | Đích | Loại | Điều kiện extend / điểm mở rộng | Lý do | REQ | Sơ đồ |
|---|---|---|---|---|---|---|---|
| RL-01 | ACT-01 Hành khách | UC-001 Tra cứu chuyến xe | Association | - | Tác nhân chính | REQ-05, REQ-06 | Tổng quát; Nhóm Bán vé |
| RL-02 | ACT-01 | UC-002 Đặt vé trực tuyến | Association | - | Tác nhân chính | REQ-03, REQ-07, REQ-09 | Tổng quát; Nhóm Bán vé |
| RL-03 | ACT-07 Cổng SMS | UC-002 | Association | - | Tác nhân phụ: gửi vé qua SMS tới số điện thoại người đi | REQ-19, REQ-20 | Tổng quát; Nhóm Bán vé |
| RL-04 | ACT-06 Cổng thanh toán | UC-003 Thanh toán vé trực tuyến | Association | - | Tác nhân phụ: thu tiền thanh toán trực tuyến và trả kết quả thanh toán (Bước 2.2a: chỉ tham gia trong phần hành vi của UC được include, UC mở rộng) | REQ-14, REQ-15 | Tổng quát; Nhóm Bán vé |
| RL-05 | ACT-02 Nhân viên bán vé | UC-004 Nhận đặt chỗ qua điện thoại | Association | - | Tác nhân chính | REQ-25 | Tổng quát; Nhóm Bán vé |
| RL-06 | ACT-02 | UC-005 Bán vé tại quầy | Association | - | Tác nhân chính | REQ-21, REQ-22, REQ-26 | Tổng quát; Nhóm Bán vé |
| RL-07 | ACT-08 Máy in vé | UC-005 | Association | - | Tác nhân phụ: in vé giấy có mã vạch | REQ-23, REQ-24 | Tổng quát; Nhóm Bán vé |
| RL-08 | ACT-10 Bộ định thời | UC-006 Huỷ đặt chỗ qua điện thoại quá hạn | Association | - | Tác nhân chính | REQ-27, REQ-28 | Tổng quát; Nhóm Bán vé |
| RL-09 | ACT-01 | UC-007 Đổi vé | Association | - | Tác nhân chính (vé mua trực tuyến, ASM-02) | REQ-30 | Tổng quát; Nhóm Bán vé |
| RL-10 | ACT-02 | UC-007 | Association | - | Tác nhân chính (vé mua tại quầy, ASM-02) | REQ-30 | Tổng quát; Nhóm Bán vé |
| RL-11 | ACT-01 | UC-008 Trả vé | Association | - | Tác nhân chính (vé mua trực tuyến, ASM-02) | REQ-29, REQ-34 | Tổng quát; Nhóm Bán vé |
| RL-12 | ACT-02 | UC-008 | Association | - | Tác nhân chính (vé mua tại quầy, ASM-02) | REQ-29, REQ-36 | Tổng quát; Nhóm Bán vé |
| RL-13 | ACT-06 | UC-008 | Association | - | Tác nhân phụ: hoàn tiền vé mua trực tuyến | REQ-34, REQ-35 | Tổng quát; Nhóm Bán vé |
| RL-14 | ACT-01 | UC-009 Đăng ký tài khoản | Association | - | Tác nhân chính | REQ-10 | Tổng quát |
| RL-15 | ACT-01 | UC-010 Đăng nhập | Association | - | Tác nhân chính | REQ-10, REQ-11 | Tổng quát |
| RL-16 | ACT-01 | UC-011 Xem lịch sử vé | Association | - | Tác nhân chính | REQ-11 | Tổng quát |
| RL-17 | ACT-03 Nhân viên điều hành | UC-012 Xếp chuyến vào lịch chạy tuần | Association | - | Tác nhân chính | REQ-41, REQ-42 | Tổng quát |
| RL-18 | ACT-03 | UC-013 Huỷ chuyến | Association | - | Tác nhân chính | REQ-47 | Tổng quát |
| RL-19 | ACT-06 | UC-013 | Association | - | Tác nhân phụ: hoàn 100% giá vé mua trực tuyến của chuyến bị huỷ | REQ-35, REQ-49 | Tổng quát |
| RL-20 | ACT-07 | UC-013 | Association | - | Tác nhân phụ: gửi SMS báo huỷ chuyến cho hành khách đã có vé | REQ-20, REQ-48 | Tổng quát |
| RL-21 | ACT-10 | UC-014 Chuẩn bị danh sách hành khách của chuyến | Association | - | Tác nhân chính | REQ-61, REQ-62 | Tổng quát |
| RL-22 | ACT-05 Phụ xe | UC-015 Soát vé lên xe | Association | - | Tác nhân chính | REQ-55 | Tổng quát |
| RL-23 | ACT-09 Đầu quét mã vạch | UC-015 | Association | - | Tác nhân phụ: đọc mã vạch trên vé và chuyển mã vé cho ứng dụng soát vé | REQ-55, REQ-56 | Tổng quát |
| RL-24 | ACT-04 Quản lý nhà xe | UC-016 Đặt giá vé | Association | - | Tác nhân chính | REQ-51, REQ-52 | Tổng quát |
| RL-25 | ACT-04 | UC-017 Đặt mức tăng giá lễ Tết | Association | - | Tác nhân chính | REQ-53, REQ-54 | Tổng quát |
| RL-26 | ACT-04 | UC-018 Xem báo cáo kinh doanh | Association | - | Tác nhân chính | REQ-63, REQ-64, REQ-65 | Tổng quát |
| RL-27 | UC-002 | UC-003 | Include | - | Bước 3a: UC-003 được P02 giữ mức Subfunction theo Q4 d (kết quả riêng là khoản tiền được cổng thanh toán xác nhận) và Q4 a. Bước 3b: mọi kịch bản thành công của UC-002 đều qua UC-003, vì vé chỉ được phát hành khi thanh toán thành công. Bước 3c: "Các chỗ đã chọn được giữ trong 10 phút để hành khách thanh toán qua cổng thanh toán trực tuyến của đối tác" (Mục 3, câu 1); "Thanh toán thành công thì hệ thống phát hành vé" (Mục 3, câu 3) | REQ-12, REQ-14, REQ-17 | Nhóm Bán vé |
| RL-28 | UC-003 | UC-007 | Extend | {vé mua trực tuyến và vé mới đắt hơn vé cũ} tại Thu chênh lệch giá vé | Bước 4a: nguồn mô tả việc trả chênh lệch là phần thêm có điều kiện khi đổi vé ("trả thêm phần chênh lệch nếu vé mới đắt hơn", Mục 5, câu 4), vé mua trực tuyến trả qua cổng thanh toán theo ASM-10 (xem Vấn đề còn mở về Q4 b). Bước 4b: UC-007 đạt mục tiêu khi vé mới không đắt hơn vé cũ hoặc khi đổi vé mua tại quầy. Bước 4c: điều kiện và điểm mở rộng ở Mục 2. Không dùng include vì Bước 3b không thoả (D-AP04) | REQ-40 | Nhóm Bán vé |

## 2. Điểm mở rộng

| UC gốc | Điểm mở rộng | Vị trí trong luồng (mô tả nghiệp vụ) | UC mở rộng | Điều kiện |
|---|---|---|---|---|
| UC-007 Đổi vé | Thu chênh lệch giá vé | Sau khi khách chọn chuyến mới cùng tuyến và hệ thống xác định giá vé mới so với giá vé cũ, trước khi ghi nhận vé mới thay cho vé cũ | UC-003 Thanh toán vé trực tuyến | {vé mua trực tuyến và vé mới đắt hơn vé cũ} (ASM-10) |

## 3. UC đề xuất bổ sung

Không có

## 4. Danh sách sơ đồ

| Sơ đồ | Phạm vi | Tác nhân | Use case | File |
|---|---|---|---|---|
| Tổng quát | Toàn hệ thống, không vẽ quan hệ giữa UC (Bước 8 phương án hai vì M = 10 tác nhân, trên 8) | ACT-01..ACT-10 | 18 UC (gồm Đăng nhập UC-010) | diagrams/P03-usecase-overview.drawio |
| Nhóm Bán vé | UC-001..UC-008, có 1 include, 1 extend | ACT-01, ACT-02, ACT-06, ACT-07, ACT-08, ACT-10 | 8 | diagrams/P03-usecase-ticket-sales.drawio |

Nhóm Tài khoản hành khách (UC-009 đến UC-011), Vận hành chuyến (UC-012 đến UC-015) và Giá vé và báo cáo (UC-016 đến UC-018) không có quan hệ include, extend, generalization giữa UC, nên không có sơ đồ phân rã; nội dung của ba nhóm nằm đủ trên sơ đồ Tổng quát.

## 5. Bảng mô hình của từng sơ đồ

### Tổng quát

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống bán vé xe khách SaoViet Bus | - | - | - | 200 | 40 | 1000 | 1430 |
| ACT-01 | Actor | Hành khách | - | - | - | 60 | 220 | 30 | 60 |
| ACT-02 | Actor | Nhân viên bán vé | - | - | - | 60 | 510 | 30 | 60 |
| ACT-03 | Actor | Nhân viên điều hành | - | - | - | 60 | 710 | 30 | 60 |
| ACT-10 | Actor | Bộ định thời | - | - | - | 60 | 920 | 30 | 60 |
| ACT-05 | Actor | Phụ xe | - | - | - | 60 | 1100 | 30 | 60 |
| ACT-04 | Actor | Quản lý nhà xe | - | - | - | 60 | 1310 | 30 | 60 |
| ACT-07 | Actor | Cổng SMS | «system» | - | - | 1280 | 300 | 30 | 60 |
| ACT-08 | Actor | Máy in vé | «device» | - | - | 1280 | 530 | 30 | 60 |
| ACT-06 | Actor | Cổng thanh toán | «system» | - | - | 1280 | 640 | 30 | 60 |
| ACT-09 | Actor | Đầu quét mã vạch | «device» | - | - | 1280 | 1100 | 30 | 60 |
| UC-001 | UseCase | Tra cứu chuyến xe | - | SYS | - | 240 | 100 | 160 | 70 |
| UC-002 | UseCase | Đặt vé trực tuyến | - | SYS | - | 480 | 160 | 160 | 70 |
| UC-009 | UseCase | Đăng ký tài khoản | - | SYS | - | 240 | 210 | 160 | 70 |
| UC-010 | UseCase | Đăng nhập | - | SYS | - | 480 | 270 | 160 | 70 |
| UC-011 | UseCase | Xem lịch sử vé | - | SYS | - | 240 | 320 | 160 | 70 |
| UC-004 | UseCase | Nhận đặt chỗ qua điện thoại | - | SYS | - | 240 | 470 | 160 | 70 |
| UC-005 | UseCase | Bán vé tại quầy | - | SYS | - | 480 | 530 | 160 | 70 |
| UC-012 | UseCase | Xếp chuyến vào lịch chạy tuần | - | SYS | - | 240 | 680 | 160 | 70 |
| UC-013 | UseCase | Huỷ chuyến | - | SYS | - | 480 | 740 | 160 | 70 |
| UC-006 | UseCase | Huỷ đặt chỗ qua điện thoại quá hạn | - | SYS | - | 240 | 890 | 160 | 70 |
| UC-014 | UseCase | Chuẩn bị danh sách hành khách của chuyến | - | SYS | - | 480 | 950 | 160 | 70 |
| UC-015 | UseCase | Soát vé lên xe | - | SYS | - | 240 | 1100 | 160 | 70 |
| UC-016 | UseCase | Đặt giá vé | - | SYS | - | 240 | 1250 | 160 | 70 |
| UC-017 | UseCase | Đặt mức tăng giá lễ Tết | - | SYS | - | 480 | 1310 | 160 | 70 |
| UC-018 | UseCase | Xem báo cáo kinh doanh | - | SYS | - | 240 | 1360 | 160 | 70 |
| UC-008 | UseCase | Trả vé | - | SYS | - | 740 | 470 | 160 | 70 |
| UC-003 | UseCase | Thanh toán vé trực tuyến | - | SYS | Quan hệ ở sơ đồ Nhóm Bán vé | 1000 | 600 | 160 | 70 |
| UC-007 | UseCase | Đổi vé<br>extension points<br>Thu chênh lệch giá vé | - | SYS | Ngăn extension points; quan hệ ở sơ đồ Nhóm Bán vé | 720 | 300 | 200 | 90 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | Tác nhân chính | - |
| RL-02 | ACT-01 | UC-002 | Association | - | Tác nhân chính | (240,190) |
| RL-03 | ACT-07 | UC-002 | Association | - | Tác nhân phụ | (1180,190) |
| RL-04 | ACT-06 | UC-003 | Association | - | Tác nhân phụ | - |
| RL-05 | ACT-02 | UC-004 | Association | - | Tác nhân chính | - |
| RL-06 | ACT-02 | UC-005 | Association | - | Tác nhân chính | (240,560) |
| RL-07 | ACT-08 | UC-005 | Association | - | Tác nhân phụ | - |
| RL-08 | ACT-10 | UC-006 | Association | - | Tác nhân chính | - |
| RL-09 | ACT-01 | UC-007 | Association | - | Tác nhân chính | (220,410); (800,410) |
| RL-10 | ACT-02 | UC-007 | Association | - | Tác nhân chính | (220,440); (840,440) |
| RL-11 | ACT-01 | UC-008 | Association | - | Tác nhân chính | (220,420); (780,420) |
| RL-12 | ACT-02 | UC-008 | Association | - | Tác nhân chính | (220,450); (820,450) |
| RL-13 | ACT-06 | UC-008 | Association | - | Tác nhân phụ | (1180,500) |
| RL-14 | ACT-01 | UC-009 | Association | - | Tác nhân chính | - |
| RL-15 | ACT-01 | UC-010 | Association | - | Tác nhân chính | (240,300) |
| RL-16 | ACT-01 | UC-011 | Association | - | Tác nhân chính | - |
| RL-17 | ACT-03 | UC-012 | Association | - | Tác nhân chính | - |
| RL-18 | ACT-03 | UC-013 | Association | - | Tác nhân chính | (240,770) |
| RL-19 | ACT-06 | UC-013 | Association | - | Tác nhân phụ | (1170,770) |
| RL-20 | ACT-07 | UC-013 | Association | - | Tác nhân phụ | (1190,780) |
| RL-21 | ACT-10 | UC-014 | Association | - | Tác nhân chính | (240,980) |
| RL-22 | ACT-05 | UC-015 | Association | - | Tác nhân chính | - |
| RL-23 | ACT-09 | UC-015 | Association | - | Tác nhân phụ | - |
| RL-24 | ACT-04 | UC-016 | Association | - | Tác nhân chính | - |
| RL-25 | ACT-04 | UC-017 | Association | - | Tác nhân chính | (240,1340) |
| RL-26 | ACT-04 | UC-018 | Association | - | Tác nhân chính | - |

### Nhóm Bán vé

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SYS | Boundary | Hệ thống bán vé xe khách SaoViet Bus | - | - | - | 200 | 40 | 520 | 850 |
| ACT-01 | Actor | Hành khách | - | - | - | 60 | 220 | 30 | 60 |
| ACT-02 | Actor | Nhân viên bán vé | - | - | - | 60 | 520 | 30 | 60 |
| ACT-10 | Actor | Bộ định thời | - | - | - | 60 | 790 | 30 | 60 |
| ACT-07 | Actor | Cổng SMS | «system» | - | - | 800 | 210 | 30 | 60 |
| ACT-06 | Actor | Cổng thanh toán | «system» | - | - | 800 | 370 | 30 | 60 |
| ACT-08 | Actor | Máy in vé | «device» | - | - | 800 | 670 | 30 | 60 |
| UC-001 | UseCase | Tra cứu chuyến xe | - | SYS | - | 240 | 100 | 160 | 70 |
| UC-002 | UseCase | Đặt vé trực tuyến | - | SYS | - | 240 | 210 | 160 | 70 |
| UC-008 | UseCase | Trả vé | - | SYS | - | 240 | 450 | 160 | 70 |
| UC-004 | UseCase | Nhận đặt chỗ qua điện thoại | - | SYS | - | 240 | 560 | 160 | 70 |
| UC-005 | UseCase | Bán vé tại quầy | - | SYS | - | 240 | 670 | 160 | 70 |
| UC-006 | UseCase | Huỷ đặt chỗ qua điện thoại quá hạn | - | SYS | - | 240 | 780 | 160 | 70 |
| UC-003 | UseCase | Thanh toán vé trực tuyến | - | SYS | - | 500 | 270 | 160 | 70 |
| UC-007 | UseCase | Đổi vé<br>extension points<br>Thu chênh lệch giá vé | - | SYS | Ngăn extension points | 240 | 320 | 200 | 90 |
| N-01 | Note | Condition: {vé mua trực tuyến và vé mới đắt hơn vé cũ}<br>extension point: Thu chênh lệch giá vé | - | - | Điều kiện của RL-28 | 480 | 380 | 200 | 60 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| RL-01 | ACT-01 | UC-001 | Association | - | Tác nhân chính | - |
| RL-02 | ACT-01 | UC-002 | Association | - | Tác nhân chính | - |
| RL-03 | ACT-07 | UC-002 | Association | - | Tác nhân phụ | - |
| RL-04 | ACT-06 | UC-003 | Association | - | Tác nhân phụ | - |
| RL-05 | ACT-02 | UC-004 | Association | - | Tác nhân chính | - |
| RL-06 | ACT-02 | UC-005 | Association | - | Tác nhân chính | - |
| RL-07 | ACT-08 | UC-005 | Association | - | Tác nhân phụ | - |
| RL-08 | ACT-10 | UC-006 | Association | - | Tác nhân chính | - |
| RL-09 | ACT-01 | UC-007 | Association | - | Tác nhân chính | - |
| RL-10 | ACT-02 | UC-007 | Association | - | Tác nhân chính | - |
| RL-11 | ACT-01 | UC-008 | Association | - | Tác nhân chính | (220,480) |
| RL-12 | ACT-02 | UC-008 | Association | - | Tác nhân chính | - |
| RL-13 | ACT-06 | UC-008 | Association | - | Tác nhân phụ | (700,480) |
| RL-27 | UC-002 | UC-003 | Include | «include» | - | - |
| RL-28 | UC-003 | UC-007 | Extend | «extend» | Điểm mở rộng: Thu chênh lệch giá vé | - |
| RL-28-N | N-01 | RL-28 | Note | - | Gắn note điều kiện vào RL-28 | - |

## 6. Nội dung file .drawio

- diagrams/P03-usecase-overview.drawio (sơ đồ Tổng quát)
- diagrams/P03-usecase-ticket-sales.drawio (sơ đồ Nhóm Bán vé)

## Câu hỏi mở

Không có

## Giả định

Không có

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-003 Thanh toán vé trực tuyến; UC-007 Đổi vé | P02 1.1 giữ UC-003 theo Q4 d và Q4 a và ghi UC-007 "dùng UC-003". Với UC-007, thanh toán chênh lệch chỉ xảy ra khi vé mua trực tuyến và vé mới đắt hơn (ASM-10), không có trong mọi kịch bản thành công, nên P03 nối bằng «extend» (RL-28). Bước 4a của P03 đòi UC mở rộng được giữ theo Q4 b. | Bổ sung Q4 b vào lý do giữ CAND-30 và UC-003 cho nhánh của UC-007 (hành vi có điều kiện khi đổi vé). Trong Bảng 4b, mô tả ngắn của UC-007 ghi "được UC-003 mở rộng tại điểm Thu chênh lệch giá vé" thay cho "qua UC-003". |

## Vấn đề còn mở

- Bước 8: N = 18 không quá 20 nhưng M = 10 trên 8, nên dùng phương án hai. Sơ đồ Tổng quát chỉ vẽ association. Chỉ nhóm Bán vé có quan hệ giữa UC nên chỉ có một sơ đồ phân rã.
- Chọn giữa hai quy tắc (C9): Bước 8 yêu cầu UC-010 Đăng nhập "nối mọi tác nhân phải xác thực", còn [Context] cấm đổi tác nhân của UC đã chốt. P02 1.1 chỉ ghi ACT-01 cho UC-010 và chưa nối ACT-02 đến ACT-05 cho tới khi ASM-09 được xác nhận (Q-27). Đã giữ theo P02: UC-010 chỉ nối ACT-01 (RL-15). Nếu Q-27 được trả lời "Có", thêm association ACT-02, ACT-03, ACT-04, ACT-05 --> UC-010 và đưa UC-010 sang cột giữa theo L-12.
- RL-28 (UC-003 «extend» UC-007): vế đầu của Bước 4a chưa thoả theo nghĩa chữ vì UC-003 được giữ theo Q4 d và Q4 a, không theo Q4 b. Vế hai ("lựa chọn thêm") thoả một phần: chênh lệch phát sinh theo điều kiện, khách không tự chọn. Không dùng include vì Bước 3b không thoả (D-AP04). Bỏ quan hệ thì UC-007 không còn liên hệ với cổng thanh toán, trái với ASM-10. Đã ghi đề xuất sửa P02. RL-28 phụ thuộc ASM-10: nếu Q-28 được trả lời (b) (mọi chênh lệch trả tại quầy), bỏ RL-28 và điểm mở rộng Thu chênh lệch giá vé.
- UC-003 vừa được UC-002 include (RL-27) vừa mở rộng UC-007 (RL-28). P04 UC-007 chỉ đặt điểm mở rộng Thu chênh lệch giá vé, không gọi UC-003 trong luồng chính, vì UC gốc không biết tới UC mở rộng.
- Target 10 không đạt với RL-28 trên sơ đồ Nhóm Bán vé. L-05 đặt UC-002 trên UC-007, L-06 đặt UC-003 bên phải UC-002 (cùng hàng hoặc giữa các UC gốc), L-07 đặt UC-003 bên dưới UC-007; không đồng thời thoả được cả ba. Đã chọn L-05 và L-06: UC-003 ở cột hai, giữa UC-002 và UC-007, nên nằm trên UC-007 và đường «extend» đi chéo xuống.
- Chọn giữa hai quy tắc (C9): L-12 lệch cột hai xuống 55 so với cột một, còn L-10 và Conventions C7.3 đòi toạ độ là bội số của 10. Đã dùng độ lệch 60. Điểm uốn tới UC cột hai đặt ở y = đỉnh hàng cột một + 90 (giữa khe của cột một), lệch 5 so với tâm dọc của UC đích.
- Sơ đồ Tổng quát: UC-007 và UC-008 nối hai tác nhân chính ở hai dải kề nhau (ACT-01, ACT-02). L-12 cho đặt các UC này ở cột một giữa hai dải, nhưng hành lang 150 chỉ chứa một UC, nên đã đặt cả hai ở cột giữa. Đường RL-11 cắt RL-10 và RL-12 trong hành lang; khi hai tác nhân cùng nối hai UC thì không tránh được một chỗ cắt. Phía phải, RL-20 (ACT-07 --> UC-013) cắt các đường tới ACT-08, ACT-06 vì ACT-07 nối UC ở dải trên cùng và dải giữa. Không đường nào cắt qua node.
- Sơ đồ Tổng quát: ghi chú "Quan hệ ở sơ đồ Nhóm Bán vé" đặt cho UC-003 và UC-007 dù hai UC này có association, để người đọc biết quan hệ giữa UC nằm ở sơ đồ phân rã.
- Không tạo include UC-002 --> UC-001. P02 ghi phần tìm chuyến là đoạn mở đầu của UC-002, nhưng UC-001 là User-goal không tách theo Q4, và nguồn chỉ mô tả trình tự ("tìm chuyến ..., xem sơ đồ chỗ ..., rồi chọn tối đa 5 chỗ", Mục 1, câu 2). Vẽ include sẽ thành D-AP01, D-AP19.
- Không có generalization tác nhân: P01 1.0 không có tác nhân nào ở cột Tổng quát hoá từ. Đề xuất của P02 về tác nhân cha cho ACT-01, ACT-02 chưa được P01 áp dụng; theo Bước 5.2, P03 không tạo mới.
- Nhãn phần tử dùng tên tiếng Việt: NGON_NGU_TEN_PHAN_TU của hồ sơ dự án chỉ quy định tên lớp, thuộc tính, phương thức, bảng, cột. Tác nhân hệ thống ngoài ghi «system», thiết bị ghi «device»; ACT-10 Bộ định thời không có stereotype vì Phần A không nêu stereotype cho tác nhân thời gian.
- Sơ đồ Tổng quát có 6 dải tác nhân chính nên cao 1430, vượt khổ A4; pageWidth, pageHeight của file đặt theo kích thước sơ đồ.
