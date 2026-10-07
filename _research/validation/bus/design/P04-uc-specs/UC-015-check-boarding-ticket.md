# P04 - Đặc tả use case UC-015 Soát vé lên xe - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.1; P03-usecase-model.md 1.0 (Mục 1, Mục 2, Câu hỏi mở, Giả định); P04-uc-specs/_BR-register.md (BR-01 đến BR-19); P04-uc-specs/UC-002-book-ticket-online.md 1.0 (Câu hỏi mở, Giả định; Mục 5 để dùng chung ví dụ vé); P04-uc-specs/UC-008-return-ticket.md 1.0 (Câu hỏi mở, Giả định; Mục 8 vì vé đã trả là vé đã huỷ khi soát); P04-uc-specs/UC-013-cancel-trip.md 1.0 (Câu hỏi mở, Giả định; Mục 8 vì vé của chuyến bị huỷ là vé đã huỷ khi soát) |
| Phạm vi | UC-015 |

Quy ước trích nguồn theo P00: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-015 |
| Tên use case | Soát vé lên xe (Check Boarding Ticket) |
| Tác nhân chính | ACT-05 Phụ xe |
| Tác nhân phụ | ACT-09 Đầu quét mã vạch |
| Mô tả ngắn | Use case này mô tả tương tác giữa phụ xe và hệ thống khi phụ xe muốn soát vé của hành khách lên xe trong một chuyến. Kết quả là phụ xe biết từng vé hành khách xuất trình là hợp lệ hay không hợp lệ, và các vé hợp lệ được ghi nhận là đã soát. |
| Sự kiện kích hoạt | Hành khách lên xe xuất trình vé, phụ xe quét mã vé (EV-19) |
| Tiền điều kiện | Phụ xe đã được xác thực và đang có phiên làm việc trên ứng dụng soát vé (ASM-09).<br>Máy soát vé của phụ xe đã có danh sách hành khách của chuyến cần soát (REQ-61, ASM-33). |
| Hậu điều kiện (thành công) | Mỗi vé được báo hợp lệ trong phiên soát vé được ghi nhận là đã soát, kèm thời điểm soát (ASM-35).<br>Kết quả soát vé của chuyến đã được gửi từ máy soát vé về dữ liệu vé của hệ thống, hoặc đang được lưu trên máy soát vé để tự gửi khi máy có sóng trở lại (REQ-60, ASM-35). |
| Hậu điều kiện tối thiểu | Use case không có luồng kết thúc thất bại. Lần quét bị báo không hợp lệ (luồng 5a, 5b, 5c) không làm thay đổi trạng thái của vé nào. |
| Quan hệ | Không có quan hệ include, extend, generalization (P03 chỉ có association RL-22 ACT-05, RL-23 ACT-09 với UC-015) |
| Điểm mở rộng | Không có |
| REQ | REQ-18, REQ-19, REQ-23, REQ-42, REQ-55, REQ-56, REQ-57, REQ-58, REQ-59, REQ-60, REQ-61 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Phụ xe | Yêu cầu bắt đầu soát vé và chọn chuyến cần soát (xem Dữ liệu vào 1) (ASM-32). |
| 2 | Hệ thống | Hiển thị thông tin chuyến và số vé còn hiệu lực trong danh sách hành khách của chuyến (xem Dữ liệu ra 1) (ASM-33). |
| 3 | Phụ xe | Quét mã vạch trên vé hành khách xuất trình khi lên xe bằng đầu quét mã vạch. |
| 4 | Đầu quét mã vạch | Đọc mã vạch trên vé và chuyển mã vé cho hệ thống (xem Dữ liệu vào 2). |
| 5 | Hệ thống | Kiểm tra vé có mã vé đã nhận thuộc chuyến đang soát, chưa bị huỷ và chưa được soát (BR-20, BR-21, BR-22, ASM-33). |
| 6 | Hệ thống | Ghi nhận vé đã soát kèm thời điểm soát (ASM-35). |
| 7 | Hệ thống | Báo vé hợp lệ kèm chỗ và họ tên người đi của vé (xem Dữ liệu ra 2). |
| 8 | Phụ xe | Lặp lại bước 3-7 cho đến khi không còn hành khách lên xe xuất trình vé. |
| 9 | Phụ xe | Yêu cầu kết thúc soát vé của chuyến. |
| 10 | Hệ thống | Gửi kết quả soát vé của chuyến từ máy soát vé về dữ liệu vé của hệ thống (REQ-60, ASM-35). |
| 11 | Hệ thống | Hiển thị kết quả soát vé của chuyến (xem Dữ liệu ra 3). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 3a | Hành khách xuất trình vé mua trực tuyến bằng mã vé nhận qua SMS, không có mã vạch để quét (ASM-34) | Phụ xe | Nhập mã vé hành khách xuất trình (xem Dữ liệu vào 2). | Tiếp tục bước 5 |
| 5a | Danh sách hành khách của chuyến không có vé nào mang mã vé đã nhận (ASM-33) | Hệ thống | Báo vé không hợp lệ với lý do sai chuyến (BR-20) (xem Dữ liệu ra 2). | Tiếp tục bước 8 |
| 5b | Vé có trong danh sách hành khách của chuyến và đã bị huỷ (ASM-36) | Hệ thống | Báo vé không hợp lệ với lý do vé đã huỷ (BR-21) (xem Dữ liệu ra 2). | Tiếp tục bước 8 |
| 5c | Vé có trong danh sách hành khách của chuyến, chưa bị huỷ và đã được soát | Hệ thống | Báo vé không hợp lệ với lý do vé đã soát, kèm thời điểm soát trước đó (BR-22) (xem Dữ liệu ra 2). | Tiếp tục bước 8 |
| 10a | Máy soát vé đang ở vùng mất sóng | Hệ thống | Lưu kết quả soát vé chưa gửi trên máy soát vé và tự gửi về dữ liệu vé của hệ thống khi máy có sóng trở lại (REQ-60, ASM-35). | Tiếp tục bước 11 |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 1)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Chuyến cần soát | Chuyến phụ xe đi theo, xác định bằng tuyến và giờ xuất bến (REQ-42) | Có | Là một chuyến đã có danh sách hành khách trên máy soát vé (ASM-32) | Hà Nội - Lào Cai, 21:00 03/02/2027 |

Dữ liệu vào 2 (bước 4, luồng 3a)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Mã vé | Mã vé đầu quét đọc từ mã vạch trên vé giấy (bước 4, REQ-23) hoặc phụ xe nhập từ mã vé hành khách nhận qua SMS (luồng 3a, REQ-19, ASM-34) | Có | Là mã vé hệ thống cấp khi phát hành vé, mỗi chỗ một mã (BR-10); việc mã vé thuộc chuyến đang soát được kiểm tra ở bước 5 | SV0000123 |

Dữ liệu ra 1 (bước 2)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tuyến và giờ xuất bến | Chuyến đang soát | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Hà Nội - Lào Cai, 21:00 03/02/2027 |
| 2 | Số vé còn hiệu lực | Số vé chưa bị huỷ trong danh sách hành khách của chuyến (ASM-33) | Số nguyên, căn phải | 36 |
| 3 | Số vé đã soát | Số vé của chuyến đã được ghi nhận là đã soát trên máy (ASM-35) | Số nguyên, căn phải | 0 |

Dữ liệu ra 2 (bước 7; luồng 5a, 5b, 5c)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Kết quả soát | Vé hợp lệ hay không hợp lệ (REQ-57) | Một trong hai giá trị "Hợp lệ" / "Không hợp lệ" | Hợp lệ |
| 2 | Lý do không hợp lệ | Chỉ có khi kết quả là không hợp lệ (BR-20, BR-21, BR-22) | Một trong ba giá trị "Sai chuyến" / "Vé đã huỷ" / "Vé đã soát" | Không có (vé hợp lệ) |
| 3 | Mã vé | Mã vé đã nhận ở bước 4 hoặc luồng 3a (BR-10) | Chuỗi chữ và số do hệ thống cấp | SV0000123 |
| 4 | Chỗ | Mã chỗ của vé trong danh sách hành khách; không có ở luồng 5a (ASM-33) | Chuỗi mã chỗ theo sơ đồ xe | A05 |
| 5 | Họ tên người đi | Họ tên người đi của vé; có ở bước 7 (ASM-33) | Chữ | Nguyễn Văn An |
| 6 | Thời điểm soát trước đó | Chỉ có ở luồng 5c, thời điểm vé đã được ghi nhận là đã soát (ASM-35) | HH:mm dd/MM/yyyy | 20:42 03/02/2027 |

Dữ liệu ra 3 (bước 11)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tuyến và giờ xuất bến | Chuyến đã soát | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Hà Nội - Lào Cai, 21:00 03/02/2027 |
| 2 | Số vé đã soát | Số vé của chuyến được ghi nhận là đã soát (ASM-35) | Số nguyên, căn phải | 35 |
| 3 | Số vé còn hiệu lực chưa soát | Số vé còn hiệu lực trừ số vé đã soát | Số nguyên, căn phải | 1 |
| 4 | Trạng thái gửi kết quả | Kết quả soát vé đã gửi về dữ liệu vé của hệ thống hay đang chờ gửi (bước 10, luồng 10a) | Một trong hai giá trị "Đã gửi" / "Chờ gửi khi có sóng" | Đã gửi |

Ví dụ số liệu, dùng chuyến và vé của ví dụ UC-002: chuyến Hà Nội - Lào Cai xuất bến 21:00 03/02/2027 bằng xe giường nằm 40 chỗ (REQ-02). Danh sách hành khách của chuyến có 38 vé đã phát hành, trong đó 2 vé đã trả qua UC-008 (đã huỷ theo ASM-20).

- Số vé còn hiệu lực ở bước 2 = 38 - 2 = 36; không vượt 40 chỗ của xe (BR-10: mỗi chỗ một vé).
- Phiên soát có 35 vé được báo hợp lệ, 1 lần quét báo "Vé đã huỷ" (luồng 5b, một trong 2 vé đã trả) và 1 lần quét lại vé SV0000123 báo "Vé đã soát" (luồng 5c). Số vé đã soát ở bước 11 = 35, vì lần quét không hợp lệ không được ghi nhận (ASM-35).
- Số vé còn hiệu lực chưa soát = 36 - 35 = 1.

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-10 | Mỗi chỗ được phát hành thành đúng một vé có một mã vé. | Ràng buộc | Dữ liệu vào 2, Dữ liệu ra 2 | REQ-18 | Đã có |
| BR-20 | Khi soát vé lên xe, vé không thuộc chuyến đang soát là vé không hợp lệ với lý do sai chuyến. | Suy luận | 5, 5a, Dữ liệu ra 2 | REQ-58 | Mới |
| BR-21 | Khi soát vé lên xe, vé đã bị huỷ là vé không hợp lệ với lý do vé đã huỷ. | Suy luận | 5, 5b, Dữ liệu ra 2 | REQ-58 | Mới |
| BR-22 | Khi soát vé lên xe, vé đã được soát trước đó là vé không hợp lệ với lý do vé đã soát. | Suy luận | 5, 5c, Dữ liệu ra 2 | REQ-58 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Phụ xe soát vé được (bước 3 đến bước 9) cả khi máy soát vé ở vùng mất sóng. | Reliability | REQ-59 |
| 2 | Chức năng soát vé chạy trên máy soát vé cầm tay Android có đầu quét mã vạch do nhà xe tự trang bị. | Ràng buộc thiết kế (+) | REQ-56 |

## 8. Thông tin bổ sung

- Mỗi lần thực hiện use case là một phiên soát vé của một chuyến; quét từng vé là vòng lặp bước 3-7 (P02, CAND-21, U-R14).
- Vé đã huỷ (BR-21) gồm vé đã trả qua UC-008 Trả vé (ASM-20), vé của chuyến bị huỷ qua UC-013 Huỷ chuyến (ASM-26) và vé cũ đã đổi qua UC-007 Đổi vé (ASM-36). Chuyến bị huỷ không chạy nên thực tế không có phiên soát vé cho chuyến đó.
- Danh sách hành khách trên máy là kết quả của UC-014 Chuẩn bị danh sách hành khách của chuyến, gửi 15 phút trước giờ xuất bến (REQ-61, REQ-62). Khi đặc tả UC-014, danh sách cần gồm mọi vé đã phát hành của chuyến kèm mã vé, chỗ, họ tên người đi và trạng thái vé, để use case này phân biệt "Sai chuyến" với "Vé đã huỷ" (ASM-33).
- Vé bán, đổi, trả sau mốc gửi danh sách (Q-11): theo ASM-33, hệ thống kiểm tra theo danh sách trên máy, nên vé bán sau mốc bị báo "Sai chuyến" và vé trả sau mốc vẫn được báo hợp lệ cho tới khi Q-11 được trả lời.
- Kiểm tra vé ở bước 5 dùng danh sách trên máy nên không cần sóng (ASM-33); vì vậy REQ-59 không tạo luồng thay thế trong vòng lặp, mất sóng chỉ ảnh hưởng bước 10 (luồng 10a).
- Việc tự gửi kết quả khi máy có sóng trở lại (luồng 10a) diễn ra sau khi use case kết thúc và không cần phụ xe thao tác; P02 coi đây là đồng bộ nội bộ của ứng dụng soát vé (CAND-46, ASM-01).
- Tần suất: khoảng 80 chuyến mỗi ngày (REQ-01), mỗi chuyến một phiên soát vé; mỗi phiên có tối đa 40 lần báo hợp lệ vì xe lớn nhất có 40 chỗ (REQ-02, BR-10), tức tối đa khoảng 80 x 40 = 3.200 lượt soát hợp lệ mỗi ngày.

## 8a. Kịch bản chính

- KB1: Luồng chính --> mọi hành khách xuất trình vé giấy hợp lệ, kết quả soát vé gửi được ngay khi kết thúc.
- KB2: Luồng chính + 3a --> hành khách xuất trình mã vé nhận qua SMS, phụ xe nhập mã vé, vé hợp lệ.
- KB3: Luồng chính + 5a --> hành khách xuất trình vé của chuyến khác, vé bị báo không hợp lệ (sai chuyến), phụ xe soát tiếp.
- KB4: Luồng chính + 5b + 5c --> một vé đã trả bị báo "Vé đã huỷ", một vé quét lần hai bị báo "Vé đã soát", phụ xe soát tiếp.
- KB5: Luồng chính + 10a --> xe ở vùng mất sóng khi kết thúc soát vé, kết quả lưu trên máy chờ gửi khi có sóng.

## 9. Activity diagram

File: diagrams/P04-activity-UC-015.drawio (trang "UC-015").

Bảng Node (x, y là toạ độ tương đối trong partition; partition dùng toạ độ tuyệt đối):

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-05 | Partition | Phụ xe | - | - | - | ACT-05, tác nhân chính; rộng 520 vì luồng 3a có hành động của phụ xe | 0 | 0 | 520 | 2000 |
| P-SYS | Partition | Hệ thống | - | - | - | Chủ ngữ hệ thống mặc định; gồm ứng dụng soát vé trên máy soát vé (ASM-01) | 520 | 0 | 680 | 2000 |
| P-ACT-09 | Partition | Đầu quét mã vạch | - | - | - | ACT-09, tác nhân phụ trả về mã vé đọc được (bước 4) | 1200 | 0 | 320 | 2000 |
| INIT | Initial | - | - | P-ACT-05 | - | - | 140 | 60 | 40 | 40 |
| A-1 | Action | Yêu cầu soát vé, chọn chuyến | - | P-ACT-05 | 1 | ASM-32 | 70 | 140 | 180 | 60 |
| A-2 | Action | Hiển thị chuyến và số vé cần soát | - | P-SYS | 2 | ASM-33 | 70 | 250 | 180 | 60 |
| M-3 | Merge | - | - | P-ACT-05 | - | Nhận luồng từ A-2 và luồng lặp từ D-8 | 140 | 360 | 40 | 40 |
| D-3 | Decision | - | - | P-ACT-05 | - | Loại vé hành khách xuất trình; đặt trước A-3 vì luồng 3a thay cho chính bước 3 | 140 | 440 | 40 | 40 |
| A-3a | Action | Nhập mã vé nhận qua SMS | - | P-ACT-05 | 3a | ASM-34 | 300 | 430 | 180 | 60 |
| A-3 | Action | Quét mã vạch trên vé | - | P-ACT-05 | 3 | - | 70 | 520 | 180 | 60 |
| A-4 | Action | Đọc mã vạch, chuyển mã vé | - | P-ACT-09 | 4 | - | 70 | 640 | 180 | 60 |
| M-5 | Merge | - | - | P-SYS | - | Nhận luồng từ A-4 và luồng 3a | 140 | 760 | 40 | 40 |
| A-5 | Action | Kiểm tra vé đúng chuyến, chưa huỷ, chưa soát | - | P-SYS | 5 | BR-20, BR-21, BR-22, ASM-33 | 70 | 840 | 180 | 60 |
| D-5 | Decision | - | - | P-SYS | - | - | 140 | 940 | 40 | 40 |
| A-5a | Action | Báo không hợp lệ: sai chuyến | - | P-SYS | 5a | BR-20 | 330 | 930 | 180 | 60 |
| A-5b | Action | Báo không hợp lệ: vé đã huỷ | - | P-SYS | 5b | BR-21, ASM-36 | 330 | 1030 | 180 | 60 |
| A-6 | Action | Ghi nhận vé đã soát | - | P-SYS | 6 | ASM-35 | 70 | 1030 | 180 | 60 |
| A-5c | Action | Báo không hợp lệ: vé đã soát | - | P-SYS | 5c | BR-22 | 330 | 1130 | 180 | 60 |
| A-7 | Action | Báo vé hợp lệ | - | P-SYS | 7 | - | 70 | 1140 | 180 | 60 |
| M-8 | Merge | - | - | P-ACT-05 | - | Nhận luồng từ A-7 và luồng 5a, 5b, 5c (Tiếp tục bước 8) | 140 | 1250 | 40 | 40 |
| D-8 | Decision | - | - | P-ACT-05 | 8 | Bước 8 (lặp lại bước 3-7) là quyết định lặp của phụ xe, không có action riêng | 140 | 1330 | 40 | 40 |
| A-9 | Action | Yêu cầu kết thúc soát vé | - | P-ACT-05 | 9 | - | 70 | 1410 | 180 | 60 |
| A-10 | Action | Gửi kết quả soát vé của chuyến | - | P-SYS | 10 | REQ-60, ASM-35 | 70 | 1520 | 180 | 60 |
| D-10 | Decision | - | - | P-SYS | - | - | 140 | 1620 | 40 | 40 |
| A-10a | Action | Lưu kết quả trên máy, gửi khi có sóng | - | P-SYS | 10a | REQ-60, ASM-35 | 330 | 1610 | 180 | 60 |
| M-11 | Merge | - | - | P-SYS | - | Nhận luồng từ D-10 và A-10a | 140 | 1710 | 40 | 40 |
| A-11 | Action | Hiển thị kết quả soát vé của chuyến | - | P-SYS | 11 | - | 70 | 1790 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thành công) | 140 | 1900 | 40 | 40 |

Bảng Edge (Điểm uốn là toạ độ tuyệt đối):

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | Sang partition hệ thống | (160,230); (680,230) |
| E-03 | A-2 | M-3 | ControlFlow | - | Về partition phụ xe | (680,340); (160,340) |
| E-04 | M-3 | D-3 | ControlFlow | - | - | - |
| E-05 | D-3 | A-3a | ControlFlow | [mã vé nhận qua SMS] | Luồng 3a | - |
| E-06 | D-3 | A-3 | ControlFlow | [vé giấy có mã vạch] | Luồng chính | - |
| E-07 | A-3a | M-5 | ControlFlow | - | Tiếp tục bước 5; sang partition hệ thống | (390,780) |
| E-08 | A-3 | A-4 | ControlFlow | - | Sang partition Đầu quét mã vạch, vượt qua partition hệ thống ở y = 610 | (160,610); (1360,610) |
| E-09 | A-4 | M-5 | ControlFlow | - | Về partition hệ thống | (1360,730); (680,730) |
| E-10 | M-5 | A-5 | ControlFlow | - | - | - |
| E-11 | A-5 | D-5 | ControlFlow | - | - | - |
| E-12 | D-5 | A-5a | ControlFlow | [không thuộc chuyến] | Luồng 5a | - |
| E-13 | D-5 | A-5b | ControlFlow | [đã huỷ] | Luồng 5b | (800,960); (800,1060) |
| E-14 | D-5 | A-5c | ControlFlow | [chưa huỷ, đã soát] | Luồng 5c | (800,960); (800,1160) |
| E-15 | D-5 | A-6 | ControlFlow | [đúng chuyến, chưa huỷ, chưa soát] | Luồng chính | - |
| E-16 | A-5a | M-8 | ControlFlow | - | Tiếp tục bước 8; về partition phụ xe | (1070,960); (1070,1270) |
| E-17 | A-5b | M-8 | ControlFlow | - | Tiếp tục bước 8; về partition phụ xe | (1070,1060); (1070,1270) |
| E-18 | A-6 | A-7 | ControlFlow | - | - | - |
| E-19 | A-5c | M-8 | ControlFlow | - | Tiếp tục bước 8; về partition phụ xe | (1070,1160); (1070,1270) |
| E-20 | A-7 | M-8 | ControlFlow | - | Về partition phụ xe | (680,1230); (160,1230) |
| E-21 | M-8 | D-8 | ControlFlow | - | - | - |
| E-22 | D-8 | M-3 | ControlFlow | [còn hành khách xuất trình vé] | Lặp lại bước 3-7; đi vòng bên trái trục chính | (40,1350); (40,380) |
| E-23 | D-8 | A-9 | ControlFlow | [hết hành khách lên xe] | Luồng chính | - |
| E-24 | A-9 | A-10 | ControlFlow | - | Sang partition hệ thống | (160,1490); (680,1490) |
| E-25 | A-10 | D-10 | ControlFlow | - | - | - |
| E-26 | D-10 | A-10a | ControlFlow | [máy mất sóng] | Luồng 10a | - |
| E-27 | D-10 | M-11 | ControlFlow | [máy có sóng] | Luồng chính | - |
| E-28 | A-10a | M-11 | ControlFlow | - | Tiếp tục bước 11 | (940,1730) |
| E-29 | M-11 | A-11 | ControlFlow | - | - | - |
| E-30 | A-11 | FINAL-1 | ControlFlow | - | Kết thúc use case (thành công) | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 3 | M-3, D-3, A-3 |
| 3a | D-3, A-3a, M-5 |
| 4 | A-4 |
| 5 | M-5, A-5 |
| 5a | D-5, A-5a, M-8 |
| 5b | D-5, A-5b, M-8 |
| 5c | D-5, A-5c, M-8 |
| 6 | A-6 |
| 7 | A-7 |
| 8 | M-8, D-8 (cạnh E-22 quay về M-3) |
| 9 | A-9 |
| 10 | A-10 |
| 10a | D-10, A-10a, M-11 |
| 11 | M-11, A-11, FINAL-1 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-45 | Danh sách hành khách gửi về máy soát vé gồm những thông tin nào (mã vé, chỗ, họ tên người đi, trạng thái vé), và có gồm vé đã huỷ của chuyến không? Khi mã vé quét được không có trong danh sách, máy báo "sai chuyến" cho mọi trường hợp (vé của chuyến khác, mã không do hệ thống cấp, vé bán sau mốc gửi danh sách) hay phân biệt từng trường hợp? | Bước 2, 5; luồng 5a, 5b; Dữ liệu ra 1, Dữ liệu ra 2; ASM-33; UC-014 (nội dung danh sách); liên quan Q-11 | Mục 8, câu 2: "Máy báo hợp lệ hay không hợp lệ (sai chuyến, vé đã huỷ, vé đã soát)"; Mục 8, câu 4: "hệ thống gửi danh sách hành khách của chuyến về máy soát vé" (không nêu nội dung danh sách) |
| Q-46 | Kết quả soát vé được gửi từ máy soát vé về hệ thống vào lúc nào và gồm những gì? (a) Sau mỗi lần soát khi máy có sóng; (b) Khi phụ xe kết thúc soát vé của chuyến. Lần quét bị báo không hợp lệ có được ghi nhận và gửi về không? (Có / Không) | Bước 6, 10; luồng 10a; Dữ liệu ra 3; hậu điều kiện thành công; ASM-35 | Mục 8, câu 3: "Máy cần soát được cả khi xe ở vùng mất sóng và gửi lại kết quả khi có sóng" (không nêu thời điểm gửi và nội dung kết quả) |
| Q-47 | Khi một vé vừa đã bị huỷ vừa đã được soát (ví dụ vé được soát rồi chuyến bị huỷ trước giờ xuất bến), máy báo lý do nào? (Vé đã huỷ, theo thứ tự đang dùng / Vé đã soát) | Luồng 5b, 5c; BR-21, BR-22 | Nguồn không nêu thứ tự ưu tiên; thứ tự đang dùng theo vị trí xuất hiện trong Mục 8, câu 2: "(sai chuyến, vé đã huỷ, vé đã soát)" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-32 | Mỗi phiên soát vé dành cho một chuyến; phụ xe chọn chuyến cần soát trong các chuyến đã có danh sách hành khách trên máy soát vé. | Mục 8, câu 1 nói "Phụ xe mỗi chuyến dùng máy soát vé cầm tay", Mục 8, câu 4 gửi danh sách hành khách "của chuyến" về máy; nguồn không nêu cách phụ xe chỉ định chuyến đang soát, trong khi quy tắc "sai chuyến" cần biết chuyến đó | Bước 1; Dữ liệu vào 1 |
| ASM-33 | Hệ thống kiểm tra vé ở bước 5 theo danh sách hành khách của chuyến đã có trên máy soát vé và các vé đã ghi nhận đã soát trên máy, cả khi máy có sóng. Danh sách gồm mọi vé đã phát hành của chuyến, kể cả vé đã huỷ, với mã vé, chỗ, họ tên người đi và trạng thái vé. Mã vé không có trong danh sách được báo "Sai chuyến". | Mục 8 cho máy soát được khi mất sóng và gửi danh sách hành khách về máy trước giờ xuất bến, nên danh sách trên máy là dữ liệu duy nhất luôn có khi soát; để báo "vé đã huỷ" khác "sai chuyến", danh sách phải có cả vé đã huỷ. Chờ Q-45, Q-11 | Tiền điều kiện; bước 2, 5; luồng 5a, 5b; Dữ liệu ra 1, Dữ liệu ra 2; UC-014 |
| ASM-34 | Vé giấy (vé bán tại quầy) được soát bằng đầu quét mã vạch; vé mua trực tuyến được soát bằng cách phụ xe nhập mã vé hành khách nhận qua SMS. | Mục 4, câu 1 nêu vé giấy "có mã vạch", còn Mục 3, câu 3 chỉ nêu "mã vé" gửi qua SMS; tin nhắn SMS chỉ chứa văn bản nên không có mã vạch để quét. Chờ Q-04 | Bước 3, 4; luồng 3a; Dữ liệu vào 2 |
| ASM-35 | Mỗi vé được báo hợp lệ được ghi nhận là đã soát trên máy, kèm thời điểm soát; lần quét bị báo không hợp lệ không được ghi nhận. Kết quả soát vé của chuyến được gửi về dữ liệu vé của hệ thống khi phụ xe kết thúc soát vé; khi máy đang mất sóng, kết quả được lưu trên máy và tự gửi khi máy có sóng trở lại. | Mục 8, câu 3 chỉ nêu "gửi lại kết quả khi có sóng", không nêu thời điểm gửi khi có sóng và nội dung kết quả. Gửi một lần khi kết thúc phiên giữ vòng lặp soát vé không phụ thuộc sóng. Chờ Q-46 | Bước 6, 10; luồng 5c, 10a; Dữ liệu ra 1, Dữ liệu ra 2, Dữ liệu ra 3; hậu điều kiện thành công |
| ASM-36 | Vé cũ sau khi đổi sang chuyến khác (UC-007) ở trạng thái đã huỷ; khi bị quét trong phiên soát vé của chuyến cũ, vé được báo "Vé đã huỷ". | Mục 5, câu 4 cho đổi vé sang chuyến khác nhưng không nêu trạng thái vé cũ; cách làm nhất quán với vé đã trả (ASM-20). Nếu mã vé được giữ nguyên khi đổi (Q-30 phương án b), vé quét trên chuyến cũ bị báo "Sai chuyến" theo ASM-33. Chờ Q-21, Q-30 | Luồng 5b; BR-21 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-015 | Cột REQ của UC-015 ở Bảng 4b chưa có REQ-18 (mỗi chỗ một mã vé, dùng nhận diện vé khi soát), REQ-19 (mã vé gửi qua SMS, cách soát vé mua trực tuyến theo ASM-34), REQ-23 (vé giấy có mã vạch để quét), REQ-42 (chuyến xác định bằng tuyến và giờ xuất bến), REQ-61 (danh sách hành khách trên máy là dữ liệu kiểm tra vé). | Thêm REQ-18, REQ-19, REQ-23, REQ-42, REQ-61 vào cột REQ của UC-015 ở Bảng 4b và thêm UC-015 vào các dòng tương ứng ở Mục 5. |
| P02 | UC-015, EV-19 | Sự kiện kích hoạt "Hành khách lên xe xuất trình vé, phụ xe quét mã vé (EV-19)" là sự kiện của từng lần quét, trong khi UC-015 là một phiên soát vé của cả chuyến với quét từng vé là vòng lặp (U-R14). Bước 1 của đặc tả là phụ xe bắt đầu soát vé của chuyến, không khớp nguyên văn sự kiện kích hoạt. | Sửa EV-19 và sự kiện kích hoạt của UC-015 thành sự kiện mở phiên, ví dụ "Hành khách bắt đầu lên xe của chuyến, phụ xe bắt đầu soát vé (EV-19)"; giữ việc quét từng vé trong cột Phản hồi mong đợi. |

## Vấn đề còn mở

- Chọn giữa hai quy tắc (C9): F4.2 mục 9 yêu cầu viết lặp bằng một bước "Lặp lại bước 3-7 cho đến khi ...", còn F10.2 và Target 13 yêu cầu mỗi bước luồng chính có đúng một action. Bước 8 là bước lặp nên không có action; đã ánh xạ bước 8 sang merge M-8 và decision D-8 (trong partition phụ xe vì phụ xe quyết định còn hay hết hành khách) theo mục "Luồng lặp" của F10.2. Target 13 đạt với mọi bước trừ bước 8.
- F10.2 đặt decision D-N ngay sau action A-N. Luồng 3a là lựa chọn của phụ xe thay cho chính bước 3 (không quét được vì vé không có mã vạch), nên D-3 đặt trước A-3, sau merge M-3; đặt sau A-3 sẽ mang nghĩa đã quét rồi mới rẽ nhánh.
- Target 5 (bước 1 là sự kiện kích hoạt): bước 1 là phụ xe bắt đầu phiên soát vé của chuyến, còn sự kiện kích hoạt chép từ P02 là sự kiện của từng lần quét (bước 3). Đã giữ nguyên văn P02 ở bảng thông tin chung theo F1 và ghi đề xuất sửa P02.
- Luồng 10a: việc tự gửi kết quả khi có sóng trở lại diễn ra sau khi use case kết thúc, không có thời hạn và không có tác nhân. F4.2 mục 15 chỉ hướng dẫn chờ sự kiện có hạn giờ trong phiên; F5.4 không có giá trị cho hành động tiếp diễn sau khi use case kết thúc. Đã viết hành động "lưu ... và tự gửi ... khi máy có sóng trở lại" trong một hàng, Quay lại "Tiếp tục bước 11", và ghi trạng thái "đang được lưu ... để tự gửi" vào hậu điều kiện thành công.
- Chọn giữa hai quy tắc (C9): F10.6 đặt trục rẽ nhánh cách decision 30 về bên phải, nhưng trục đó nằm trong bề ngang action luồng chính kế tiếp (A-6 cùng trục với D-5). Đã đặt trục ở x = 800 (cách mép phải A-6 là 30) cho E-13, E-14 để cạnh không cắt qua node (C7.3).
- E-08 (A-3 --> A-4) phải vượt qua partition hệ thống vì F10.4 đặt tác nhân phụ ở bên phải hệ thống; cạnh đi ở y = 610, không cắt node nào nhưng cắt đoạn dọc x = 390 của E-07 (A-3a --> M-5). Ba cạnh quay lại E-16, E-17, E-19 dùng chung trục x = 1070 và làn y = 1270 vào M-8.
- Target 5a: các luồng 5a, 5b, 5c, 10a không kết thúc use case; mọi đường đi đều kết thúc qua bước 11 (hiển thị kết quả soát vé cho phụ xe), nên không có luồng kết thúc nào thiếu bước báo kết quả.
