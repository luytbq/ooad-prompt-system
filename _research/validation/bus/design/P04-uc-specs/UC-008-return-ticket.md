# P04 - Đặc tả use case UC-008 Trả vé - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.1; P03-usecase-model.md 1.0 (Mục 1, Mục 2, Câu hỏi mở, Giả định); P04-uc-specs/_BR-register.md (BR-01 đến BR-10); P04-uc-specs/UC-002-book-ticket-online.md 1.0 (Câu hỏi mở, Giả định; Mục 5, Mục 6 để dùng chung ví dụ vé và mã BR) |
| Phạm vi | UC-008 |

Quy ước trích nguồn theo P00: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-008 |
| Tên use case | Trả vé (Return Ticket) |
| Tác nhân chính | ACT-01 Hành khách, ACT-02 Nhân viên bán vé |
| Tác nhân phụ | ACT-06 Cổng thanh toán |
| Mô tả ngắn | Use case này mô tả tương tác giữa hành khách hoặc nhân viên bán vé và hệ thống khi hành khách muốn trả vé đã mua trực tuyến, hoặc khi nhân viên bán vé nhận trả vé mua tại quầy cho khách. Kết quả là vé bị huỷ và khách được hoàn 90% hoặc 50% giá vé tuỳ thời gian còn lại trước giờ xuất bến, qua cổng thanh toán hoặc bằng tiền mặt tại quầy theo kênh mua. |
| Sự kiện kích hoạt | Hành khách muốn trả vé đã mua trực tuyến (EV-11); khách mang vé mua tại quầy tới quầy để trả (EV-12) |
| Tiền điều kiện | Khi tác nhân là nhân viên bán vé: nhân viên bán vé đã được xác thực và đang có phiên làm việc (ASM-09). |
| Hậu điều kiện (thành công) | Vé đã trả ở trạng thái đã huỷ và chỗ của vé trở lại còn trống trên chuyến (BR-03, ASM-20).<br>Khoản hoàn tiền của vé được ghi nhận với số tiền bằng 90% giá vé (BR-13) hoặc 50% giá vé (BR-14) theo thời gian còn lại trước giờ xuất bến tại thời điểm trả (ASM-23).<br>Với vé mua trực tuyến, khoản hoàn đã được Cổng thanh toán xác nhận (BR-15); với vé mua tại quầy, khoản hoàn được ghi nhận là hoàn bằng tiền mặt tại quầy (BR-16). |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công, vé giữ nguyên trạng thái, chỗ của vé không thay đổi và không có khoản hoàn tiền nào được ghi nhận (ASM-21). |
| Quan hệ | Không có quan hệ include, extend, generalization (P03 chỉ có association RL-11 ACT-01, RL-12 ACT-02, RL-13 ACT-06 với UC-008) |
| Điểm mở rộng | Không có |
| REQ | REQ-18, REQ-29, REQ-31, REQ-32, REQ-33, REQ-34, REQ-35, REQ-36, REQ-42 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Hành khách / Nhân viên bán vé | Yêu cầu trả vé và cung cấp thông tin nhận diện vé (xem Dữ liệu vào 1). |
| 2 | Hệ thống | Kiểm tra có vé khớp thông tin đã cung cấp (ASM-18) và vé chưa bị huỷ (ASM-20). |
| 3 | Hệ thống | Kiểm tra vé được trả qua đúng kênh đã mua (BR-11) và thời gian còn lại trước giờ xuất bến của chuyến từ 4 giờ trở lên (BR-12, ASM-23). |
| 4 | Hệ thống | Tính số tiền hoàn của vé theo mức hoàn ứng với thời gian còn lại trước giờ xuất bến (BR-13, BR-14, ASM-22). |
| 5 | Hệ thống | Hiển thị thông tin vé, mức hoàn và số tiền hoàn (xem Dữ liệu ra 1) (ASM-19). |
| 6 | Hành khách / Nhân viên bán vé | Xác nhận trả vé (ASM-19). |
| 7 | Hệ thống | Xác định hình thức hoàn theo kênh mua của vé (BR-15, BR-16). |
| 8 | Hệ thống | Gửi yêu cầu hoàn số tiền hoàn của vé tới Cổng thanh toán (BR-15). |
| 9 | Cổng thanh toán | Trả về kết quả hoàn tiền. |
| 10 | Hệ thống | Huỷ vé, trả chỗ của vé về trạng thái còn trống (BR-03, ASM-20) và ghi nhận khoản hoàn tiền của vé. |
| 11 | Hệ thống | Thông báo trả vé thành công kèm số tiền hoàn và hình thức hoàn (xem Dữ liệu ra 2). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Không có vé nào khớp thông tin đã cung cấp (mã vé không tồn tại, hoặc số điện thoại người đi không khớp vé, ASM-18) | Hệ thống | Thông báo không tìm thấy vé khớp thông tin đã cung cấp. | Quay lại bước 1 |
| 2b | Có vé khớp thông tin và vé đã bị huỷ (đã được trả trước đó hoặc thuộc chuyến bị huỷ) (ASM-20) | Hệ thống | Từ chối yêu cầu trả vé và thông báo vé đã bị huỷ. | Kết thúc use case (thất bại) |
| 3a | Vé được mua qua kênh khác với kênh đang yêu cầu trả (BR-11) | Hệ thống | Từ chối yêu cầu trả vé và thông báo quy tắc bị vi phạm (BR-11). | Kết thúc use case (thất bại) |
| 3b | Vé được trả qua đúng kênh đã mua và thời gian còn lại trước giờ xuất bến dưới 4 giờ (BR-12) | Hệ thống | Từ chối yêu cầu trả vé và thông báo quy tắc bị vi phạm (BR-12). | Kết thúc use case (thất bại) |
| 6a | Hành khách / Nhân viên bán vé không xác nhận trả vé với số tiền hoàn đã hiển thị (ASM-19) | Hệ thống | Thông báo yêu cầu trả vé đã được huỷ và vé giữ nguyên hiệu lực. | Kết thúc use case (thất bại) |
| 7a | Vé được mua tại quầy, gồm vé đặt qua điện thoại đã thanh toán tại quầy (BR-16) | - | - | Tiếp tục bước 10 |
| 9a | Cổng thanh toán trả về kết quả hoàn tiền không thành công | Hệ thống | Thông báo hoàn tiền không thành công và vé chưa được trả (ASM-21). | Kết thúc use case (thất bại) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 1)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Mã vé | Mã của vé cần trả: mã vé gửi qua SMS với vé mua trực tuyến, mã trên vé giấy với vé mua tại quầy | Có | Là mã vé đã được hệ thống cấp, mỗi mã ứng với đúng một vé (BR-10) | SV0000123 |
| 2 | Số điện thoại người đi | Số điện thoại người đi của vé, dùng để xác nhận người yêu cầu trả vé mua trực tuyến | Có khi hành khách yêu cầu trả vé (ASM-18) | Trùng số điện thoại người đi đã ghi cho vé (ASM-18) | 0912345678 |

Dữ liệu ra 1 (bước 5)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Mã vé | Mã của vé đang yêu cầu trả (BR-10) | Chuỗi chữ và số do hệ thống cấp | SV0000123 |
| 2 | Tuyến và giờ xuất bến | Chuyến của vé (REQ-42) (ASM-19) | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Hà Nội - Lào Cai, 21:00 03/02/2027 |
| 3 | Chỗ | Mã chỗ của vé (ASM-19) | Chuỗi mã chỗ theo sơ đồ xe | A05 |
| 4 | Giá vé | Số tiền đã thanh toán cho vé khi mua (ASM-22) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 360.000 đ |
| 5 | Thời gian còn lại trước giờ xuất bến | Từ thời điểm trả vé tới giờ xuất bến của chuyến (ASM-23) | "<số giờ> giờ <số phút> phút" | 49 giờ 0 phút |
| 6 | Mức hoàn | Tỉ lệ hoàn trên giá vé (BR-13, BR-14) | Số nguyên kèm "%" | 90% |
| 7 | Số tiền hoàn | Giá vé nhân mức hoàn (BR-13, BR-14) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 324.000 đ |

Dữ liệu ra 2 (bước 11)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Mã vé | Mã của vé đã trả | Chuỗi chữ và số do hệ thống cấp | SV0000123 |
| 2 | Trạng thái vé | Trạng thái của vé sau khi trả (ASM-20) | Chữ | Đã huỷ |
| 3 | Số tiền hoàn | Số tiền khách được hoàn (BR-13, BR-14) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 324.000 đ |
| 4 | Hình thức hoàn | Kênh hoàn tiền theo kênh mua (BR-15, BR-16) | Một trong hai giá trị "Qua cổng thanh toán" / "Tiền mặt tại quầy" | Qua cổng thanh toán |

Ví dụ tính số tiền hoàn (BR-12, BR-13, BR-14), dùng vé SV0000123 của ví dụ UC-002: chuyến Hà Nội - Lào Cai xuất bến 21:00 03/02/2027, giá vé đã thanh toán 360.000 đ (ASM-22).

- Trả lúc 20:00 01/02/2027: thời gian còn lại = 21:00 03/02/2027 - 20:00 01/02/2027 = 49 giờ, từ 24 giờ trở lên nên hoàn 90%: 360.000 x 90/100 = 324.000 đ.
- Trả lúc 09:00 03/02/2027: thời gian còn lại = 21:00 - 09:00 = 12 giờ, từ 4 giờ đến dưới 24 giờ nên hoàn 50%: 360.000 x 50/100 = 180.000 đ.
- Trả lúc 18:00 03/02/2027: thời gian còn lại = 21:00 - 18:00 = 3 giờ, dưới 4 giờ nên không được trả (luồng 3b).
- Hai mốc biên: trả lúc 21:00 02/02/2027 còn đúng 24 giờ, hoàn 90% (324.000 đ); trả lúc 17:00 03/02/2027 còn đúng 4 giờ, hoàn 50% (180.000 đ).

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-03 | Một chỗ của chuyến là còn trống khi chỗ đó chưa có vé và không đang được giữ cho một lần đặt chưa hết thời hạn giữ chỗ. | Suy luận | 10 | REQ-12, REQ-16, REQ-67 | Đã có |
| BR-10 | Mỗi chỗ được phát hành thành đúng một vé có một mã vé. | Ràng buộc | Dữ liệu vào 1, Dữ liệu ra 1 | REQ-18 | Đã có |
| BR-11 | Vé chỉ được trả qua kênh đã mua vé: vé mua trực tuyến do hành khách trả trên website, vé mua tại quầy (gồm vé đặt qua điện thoại đã thanh toán tại quầy) do nhân viên bán vé trả tại quầy (ASM-02). | Ràng buộc | 3, 3a | REQ-29, REQ-34, REQ-36 | Mới |
| BR-12 | Vé không được trả khi thời gian còn lại trước giờ xuất bến của chuyến dưới 4 giờ. | Ràng buộc | 3, 3b | REQ-33 | Mới |
| BR-13 | Vé được trả khi thời gian còn lại trước giờ xuất bến của chuyến từ 24 giờ trở lên được hoàn 90% giá vé. | Tính toán | 4, Dữ liệu ra 1, Dữ liệu ra 2 | REQ-31 | Mới |
| BR-14 | Vé được trả khi thời gian còn lại trước giờ xuất bến của chuyến từ 4 giờ đến dưới 24 giờ được hoàn 50% giá vé. | Tính toán | 4, Dữ liệu ra 1, Dữ liệu ra 2 | REQ-32 | Mới |
| BR-15 | Vé mua trực tuyến được hoàn tiền qua cổng thanh toán trực tuyến của đối tác. | Ràng buộc | 7, 8, Dữ liệu ra 2 | REQ-34 | Mới |
| BR-16 | Vé mua tại quầy được hoàn bằng tiền mặt tại quầy. | Ràng buộc | 7, 7a, Dữ liệu ra 2 | REQ-36 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Yêu cầu hoàn tiền vé mua trực tuyến được trao đổi với cổng thanh toán trực tuyến của đối tác qua API hoàn tiền; tài liệu API chưa có (Q-24). | Giao tiếp (+) | REQ-35 |

## 8. Thông tin bổ sung

- Hai tác nhân chính được ghi chung "Hành khách / Nhân viên bán vé" theo F4.2 mục 12 vì P01 1.0 không có tác nhân cha cho ACT-01 và ACT-02 (đề xuất của P02 chưa được P01 áp dụng). Khác biệt hành vi giữa hai tác nhân nằm ở luồng 3a (kênh trả vé) và luồng 7a (hình thức hoàn). Luồng chính mô tả vé mua trực tuyến do hành khách trả.
- Phân kênh trả vé theo kênh mua dựa trên ASM-02 (chờ Q-02). Nếu Q-02 được trả lời (c) (đổi, trả ở cả website và quầy), bỏ phần kênh của bước 3 và luồng 3a, hình thức hoàn vẫn theo kênh mua (BR-15, BR-16); nếu trả lời (b) (chỉ tại quầy), ACT-01 không còn là tác nhân chính của UC-008.
- Với vé mua tại quầy, sau bước 11 nhân viên bán vé chi tiền mặt cho khách theo số tiền hoàn đã thông báo. Việc chi tiền diễn ra ngoài hệ thống; nguồn không nêu hệ thống ghi nhận xác nhận đã chi.
- Hoàn 100% giá vé khi huỷ chuyến (REQ-50) thuộc UC-013 Huỷ chuyến, không qua UC-008; vé của chuyến bị huỷ rơi vào luồng 2b. Hoàn tiền mặt tại quầy cho vé mua tại quầy của chuyến bị huỷ chờ Q-14 (CAND-43 của P02) và có thể thành luồng thay thế của UC-008.
- Theo ASM-20, vé đã trả được ứng dụng soát vé báo là "vé đã huỷ" khi quét (REQ-58, UC-015 Soát vé lên xe).
- Mốc chậm nhất để trả vé là 4 giờ trước giờ xuất bến (BR-12), sớm hơn mốc gửi danh sách hành khách 15 phút trước giờ xuất bến (REQ-62), nên UC-008 không làm thay đổi vé sau mốc đó; Q-11 không ảnh hưởng UC-008.
- Vé cũ sau khi đổi (UC-007 Đổi vé) có bị coi là đã huỷ (luồng 2b) hay không chờ Q-21; giá vé dùng tính hoàn của vé đã đổi chờ Q-38.
- Cách hành khách xác nhận quyền trả vé (ASM-18, Q-35) liên quan tới cách xác thực tài khoản (Q-07) và phạm vi lịch sử vé (Q-06): nếu chọn bắt buộc đăng nhập, tiền điều kiện của hành khách đổi thành trạng thái đã xác thực và Dữ liệu vào 1 bỏ số điện thoại người đi.

## 8a. Kịch bản chính

- KB1: Luồng chính --> hành khách trả vé mua trực tuyến khi còn từ 24 giờ trở lên, được hoàn 90% giá vé qua Cổng thanh toán.
- KB2: Luồng chính + 7a --> nhân viên bán vé nhận trả vé mua tại quầy, khách được hoàn bằng tiền mặt tại quầy.
- KB3: Luồng chính + 3b --> còn dưới 4 giờ trước giờ xuất bến, vé không được trả.
- KB4: Luồng chính + 9a --> Cổng thanh toán hoàn tiền không thành công, vé giữ nguyên.
- KB5: Luồng chính + 2a --> nhập sai số điện thoại người đi, nhập lại đúng, vé được trả và hoàn tiền.

## 9. Activity diagram

File: diagrams/P04-activity-UC-008.drawio (trang "UC-008").

Bảng Node (x, y là toạ độ tương đối trong partition; partition dùng toạ độ tuyệt đối):

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01-02 | Partition | Hành khách / Nhân viên bán vé | - | - | - | ACT-01, ACT-02 ghi chung (F4.2 mục 12) | 0 | 0 | 320 | 2000 |
| P-SYS | Partition | Hệ thống | - | - | - | Chủ ngữ hệ thống mặc định | 320 | 0 | 680 | 2000 |
| P-ACT-06 | Partition | Cổng thanh toán | - | - | - | ACT-06, tác nhân phụ trả về kết quả hoàn tiền | 1000 | 0 | 320 | 2000 |
| INIT | Initial | - | - | P-ACT-01-02 | - | - | 140 | 60 | 40 | 40 |
| M-1 | Merge | - | - | P-ACT-01-02 | - | Nhận luồng quay lại từ 2a | 140 | 140 | 40 | 40 |
| A-1 | Action | Yêu cầu trả vé, cung cấp thông tin vé | - | P-ACT-01-02 | 1 | - | 70 | 220 | 180 | 60 |
| A-2 | Action | Kiểm tra vé khớp và chưa bị huỷ | - | P-SYS | 2 | ASM-18, ASM-20 | 70 | 330 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | - | - | 140 | 430 | 40 | 40 |
| A-2a | Action | Thông báo không tìm thấy vé khớp | - | P-SYS | 2a | ASM-18 | 330 | 420 | 180 | 60 |
| A-2b | Action | Từ chối: vé đã bị huỷ | - | P-SYS | 2b | ASM-20 | 330 | 520 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 530 | 40 | 40 |
| A-3 | Action | Kiểm tra kênh trả và mốc 4 giờ | - | P-SYS | 3 | BR-11, BR-12, ASM-23 | 70 | 520 | 180 | 60 |
| D-3 | Decision | - | - | P-SYS | - | - | 140 | 630 | 40 | 40 |
| A-3a | Action | Từ chối: sai kênh mua (BR-11) | - | P-SYS | 3a | - | 330 | 620 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 630 | 40 | 40 |
| A-3b | Action | Từ chối: còn dưới 4 giờ (BR-12) | - | P-SYS | 3b | - | 330 | 720 | 180 | 60 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 730 | 40 | 40 |
| A-4 | Action | Tính số tiền hoàn theo mức hoàn | - | P-SYS | 4 | BR-13, BR-14, ASM-22 | 70 | 720 | 180 | 60 |
| A-5 | Action | Hiển thị thông tin vé và số tiền hoàn | - | P-SYS | 5 | ASM-19 | 70 | 830 | 180 | 60 |
| A-6 | Action | Xác nhận trả vé | - | P-ACT-01-02 | 6 | ASM-19 | 70 | 940 | 180 | 60 |
| D-6 | Decision | - | - | P-ACT-01-02 | - | Lựa chọn của tác nhân, đặt trong partition tác nhân | 140 | 1040 | 40 | 40 |
| A-6a | Action | Thông báo đã huỷ yêu cầu, vé giữ nguyên | - | P-SYS | 6a | ASM-19 | 330 | 1030 | 180 | 60 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 1040 | 40 | 40 |
| A-7 | Action | Xác định hình thức hoàn theo kênh mua | - | P-SYS | 7 | BR-15, BR-16 | 70 | 1130 | 180 | 60 |
| D-7 | Decision | - | - | P-SYS | - | Luồng 7a không có hành động | 140 | 1230 | 40 | 40 |
| A-8 | Action | Gửi yêu cầu hoàn tiền tới Cổng thanh toán | - | P-SYS | 8 | BR-15 | 70 | 1320 | 180 | 60 |
| A-9 | Action | Trả về kết quả hoàn tiền | - | P-ACT-06 | 9 | - | 70 | 1420 | 180 | 60 |
| D-9 | Decision | - | - | P-SYS | - | Hệ thống đánh giá kết quả do ACT-06 trả về | 140 | 1540 | 40 | 40 |
| A-9a | Action | Thông báo hoàn tiền không thành công | - | P-SYS | 9a | ASM-21 | 330 | 1530 | 180 | 60 |
| FINAL-5 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 1540 | 40 | 40 |
| M-10 | Merge | - | - | P-SYS | - | Nhận luồng từ D-9 và luồng 7a | 140 | 1620 | 40 | 40 |
| A-10 | Action | Huỷ vé, trả chỗ, ghi nhận khoản hoàn | - | P-SYS | 10 | BR-03, ASM-20 | 70 | 1700 | 180 | 60 |
| A-11 | Action | Thông báo trả vé thành công | - | P-SYS | 11 | - | 70 | 1810 | 180 | 60 |
| FINAL-6 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thành công) | 140 | 1920 | 40 | 40 |

Bảng Edge (Điểm uốn là toạ độ tuyệt đối):

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | M-1 | ControlFlow | - | - | - |
| E-02 | M-1 | A-1 | ControlFlow | - | - | - |
| E-03 | A-1 | A-2 | ControlFlow | - | Sang partition hệ thống | (160,300); (480,300) |
| E-04 | A-2 | D-2 | ControlFlow | - | - | - |
| E-05 | D-2 | A-2a | ControlFlow | [không có vé khớp thông tin] | Luồng 2a | - |
| E-06 | D-2 | A-2b | ControlFlow | [vé khớp, đã bị huỷ] | Luồng 2b | (600,450); (600,550) |
| E-07 | D-2 | A-3 | ControlFlow | [vé khớp, chưa bị huỷ] | Luồng chính | - |
| E-08 | A-2a | M-1 | ControlFlow | - | Quay lại bước 1 | (960,450); (960,160) |
| E-09 | A-2b | FINAL-1 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-10 | A-3 | D-3 | ControlFlow | - | - | - |
| E-11 | D-3 | A-3a | ControlFlow | [sai kênh mua] | Luồng 3a | - |
| E-12 | D-3 | A-3b | ControlFlow | [đúng kênh, còn dưới 4 giờ] | Luồng 3b | (600,650); (600,750) |
| E-13 | D-3 | A-4 | ControlFlow | [đúng kênh, còn từ 4 giờ trở lên] | Luồng chính | - |
| E-14 | A-3a | FINAL-2 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-15 | A-3b | FINAL-3 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-16 | A-4 | A-5 | ControlFlow | - | - | - |
| E-17 | A-5 | A-6 | ControlFlow | - | Sang partition tác nhân | (480,910); (160,910) |
| E-18 | A-6 | D-6 | ControlFlow | - | - | - |
| E-19 | D-6 | A-6a | ControlFlow | [không xác nhận trả vé] | Luồng 6a; sang partition hệ thống, đi thẳng ở y = 1060 | - |
| E-20 | D-6 | A-7 | ControlFlow | [xác nhận trả vé] | Luồng chính; sang partition hệ thống | (160,1100); (480,1100) |
| E-21 | A-6a | FINAL-4 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-22 | A-7 | D-7 | ControlFlow | - | - | - |
| E-23 | D-7 | M-10 | ControlFlow | [vé mua tại quầy] | Luồng 7a, tiếp tục bước 10; đi vòng bên trái trục chính | (350,1250); (350,1640) |
| E-24 | D-7 | A-8 | ControlFlow | [vé mua trực tuyến] | Luồng chính | - |
| E-25 | A-8 | A-9 | ControlFlow | - | Sang partition Cổng thanh toán | (480,1400); (1160,1400) |
| E-26 | A-9 | D-9 | ControlFlow | - | Về partition hệ thống | (1160,1500); (480,1500) |
| E-27 | D-9 | A-9a | ControlFlow | [hoàn tiền không thành công] | Luồng 9a | - |
| E-28 | D-9 | M-10 | ControlFlow | [hoàn tiền thành công] | Luồng chính | - |
| E-29 | A-9a | FINAL-5 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-30 | M-10 | A-10 | ControlFlow | - | - | - |
| E-31 | A-10 | A-11 | ControlFlow | - | - | - |
| E-32 | A-11 | FINAL-6 | ControlFlow | - | Kết thúc use case (thành công) | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a | D-2, A-2a, M-1 |
| 2b | D-2, A-2b, FINAL-1 |
| 3 | A-3 |
| 3a | D-3, A-3a, FINAL-2 |
| 3b | D-3, A-3b, FINAL-3 |
| 4 | A-4 |
| 5 | A-5 |
| 6 | A-6 |
| 6a | D-6, A-6a, FINAL-4 |
| 7 | A-7 |
| 7a | D-7, E-23 (guard [vé mua tại quầy], không có action), M-10 |
| 8 | A-8 |
| 9 | A-9 |
| 9a | D-9, A-9a, FINAL-5 |
| 10 | A-10 |
| 11 | A-11, FINAL-6 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-35 | Khi hành khách trả vé mua trực tuyến trên website, hệ thống xác nhận người yêu cầu có quyền trả vé bằng cách nào? (a) Chỉ cần mã vé; (b) Mã vé và số điện thoại người đi của vé; (c) Hành khách phải đăng nhập tài khoản và vé thuộc lịch sử vé của tài khoản | Bước 1, 2; luồng 2a; Dữ liệu vào 1; tiền điều kiện; ASM-18; liên quan Q-06, Q-07 | Mục 5, câu 1: "Hành khách được đổi hoặc trả vé."; Mục 2, câu 2: "đặt vé không bắt buộc có tài khoản" |
| Q-36 | Sau khi vé được trả, chỗ của vé có trở lại còn trống để bán cho khách khác không, và vé đã trả có được coi là "vé đã huỷ" khi soát vé không? (Có / Không) | Bước 2, 10; luồng 2b; hậu điều kiện thành công; ASM-20; BR-02, BR-03; UC-015 (REQ-58) | Mục 5, câu 2 không nêu chỗ của vé sau khi trả; Mục 8, câu 2: "vé đã huỷ" |
| Q-37 | Khi cổng thanh toán trả về kết quả hoàn tiền không thành công, hệ thống xử lý thế nào? (a) Vé chưa được trả, hành khách yêu cầu trả lại sau; (b) Vé vẫn được trả, khoản hoàn được gửi lại cổng thanh toán sau; (c) Khách tới quầy nhận tiền mặt | Luồng 9a; thứ tự bước 8 đến 10; hậu điều kiện tối thiểu; ASM-21 | Mục 5, câu 3: "Vé mua trực tuyến được hoàn qua cổng thanh toán"; project-profile.md, HE_THONG_NGOAI: "API thanh toán và hoàn tiền, chưa có tài liệu API" |
| Q-38 | "Giá vé" dùng để tính mức hoàn 90%, 50% là giá nào? (a) Số tiền đã thanh toán cho vé khi mua, gồm mức tăng giá lễ Tết nếu có; (b) Giá vé theo tuyến và loại xe hiện hành tại thời điểm trả. Với vé đã đổi (UC-007), giá vé là giá của vé mới hay tổng số tiền khách đã trả (vé cũ cộng chênh lệch)? | Bước 4; BR-13, BR-14; Dữ liệu ra 1; ASM-22; UC-007 | Mục 5, câu 2: "hoàn 90% giá vé"; Mục 7, câu 2 (mức tăng giá lễ Tết); Mục 5, câu 4 (đổi vé, trả thêm chênh lệch) |
| Q-39 | Thời điểm trả vé dùng để tính thời gian còn lại trước giờ xuất bến là thời điểm nào? (Lúc tác nhân yêu cầu trả vé / Lúc hệ thống ghi nhận vé đã trả) | Bước 3, 4; BR-12, BR-13, BR-14; ASM-23 | Mục 5, câu 2: "Trả vé trước giờ xuất bến từ 24 giờ trở lên được hoàn 90% giá vé" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-18 | Hành khách nhận diện vé mua trực tuyến cần trả bằng mã vé và số điện thoại người đi của vé, không cần tài khoản; nhân viên bán vé nhận diện vé mua tại quầy bằng mã vé trên vé giấy. | Nguồn không nêu cách xác nhận người yêu cầu trả vé. Đặt vé không bắt buộc có tài khoản (REQ-03) và vé được gửi tới số điện thoại người đi (REQ-19), nên mã vé kèm số điện thoại người đi là thông tin người nhận vé có. Chờ Q-35 | Bước 1, 2; luồng 2a; Dữ liệu vào 1 |
| ASM-19 | Trước khi vé bị huỷ, hệ thống hiển thị thông tin vé (mã vé, tuyến, giờ xuất bến, chỗ, giá vé), mức hoàn và số tiền hoàn để tác nhân xác nhận; tác nhân không xác nhận thì vé giữ nguyên. | Nguồn không nêu bước xác nhận. Mức hoàn phụ thuộc thời điểm trả, có thể chỉ 50% giá vé, và vé đã trả không dùng lại được, nên khách cần biết số tiền hoàn trước khi quyết định | Bước 5, 6; luồng 6a; Dữ liệu ra 1 |
| ASM-20 | Vé đã trả chuyển sang trạng thái đã huỷ; chỗ của vé trở lại còn trống cho khách khác chọn, với "chưa có vé" trong BR-03 hiểu là chưa có vé còn hiệu lực. | EV-11, EV-12 của P02 ghi phản hồi của hệ thống là "Huỷ vé"; nguồn không nêu chỗ của vé sau khi trả. Chờ Q-36 | Bước 2, 10; luồng 2b; hậu điều kiện thành công; Dữ liệu ra 2 |
| ASM-21 | Khi Cổng thanh toán trả về kết quả hoàn tiền không thành công, vé không bị huỷ, không có khoản hoàn nào được ghi nhận và hành khách được thông báo để yêu cầu trả lại sau. | Nguồn chỉ nêu kênh hoàn (Mục 5, câu 3), không nêu trường hợp hoàn không thành công. Huỷ vé sau khi cổng xác nhận hoàn tránh trường hợp vé đã bị huỷ mà khách chưa nhận tiền. Chờ Q-37 | Luồng 9a; thứ tự bước 8 đến 10; hậu điều kiện tối thiểu |
| ASM-22 | Giá vé dùng để tính số tiền hoàn là số tiền đã thanh toán cho vé đó khi mua (với vé mua trực tuyến là giá tính theo BR-05 tại lần đặt). | Mục 5, câu 2 nói "giá vé" mà không nói giá lúc mua hay giá hiện hành; giá vé và mức tăng giá có thể thay đổi sau khi mua (UC-016, UC-017). Chờ Q-38 | Bước 4; BR-13, BR-14; Dữ liệu ra 1 |
| ASM-23 | Thời điểm trả vé là thời điểm hệ thống kiểm tra thời gian còn lại ở bước 3; mức hoàn tính ở bước 4 áp dụng cho lần trả vé đó dù tác nhân xác nhận ở bước 6 sau một mốc 24 giờ hoặc 4 giờ. | Nguồn nêu mốc theo "trả vé trước giờ xuất bến" mà không nêu thời điểm trả là lúc yêu cầu hay lúc hoàn tất. Chờ Q-39 | Bước 3, 4; BR-12, BR-13, BR-14; Dữ liệu ra 1 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 (UC-002), P06 | BR-02, BR-03 | Sau khi vé được trả (UC-008) hoặc chuyến bị huỷ, chỗ có một vé ở trạng thái đã huỷ. Hiểu theo nghĩa chữ, BR-02 "hai vé không được cùng một chỗ" và BR-03 "chỗ chưa có vé" chặn việc bán lại chỗ đã trả. | Khi hợp nhất BR ở P06 (hoặc chạy lại P04 UC-002), diễn đạt BR-02 là "hai vé còn hiệu lực không được cùng một chỗ" và BR-03 là "chỗ chưa có vé còn hiệu lực", sau khi Q-36 được trả lời. |
| P02 | UC-008 | Cột REQ của UC-008 ở Bảng 4b chưa có REQ-18 (mã vé dùng nhận diện vé cần trả) và REQ-42 (giờ xuất bến dùng tính thời gian còn lại và mức hoàn). | Thêm REQ-18, REQ-42 vào cột REQ của UC-008 ở Bảng 4b và thêm UC-008 vào hai dòng tương ứng ở Mục 5. |

## Vấn đề còn mở

- Chọn giữa hai quy tắc (C9): F10.5 bắt buộc điền Điểm uốn cho cạnh vượt qua partition khác, còn Conventions C7.1 ghi "-" cho cạnh đi thẳng. E-19 (D-6 --> A-6a) đi thẳng một đoạn ngang ở y = 1060 từ partition tác nhân sang partition hệ thống, không cắt node nào; đã ghi "-" theo C7.1 và nêu đường đi ở cột Ghi chú.
- Chọn giữa hai quy tắc (C9): F10.6 đặt trục rẽ nhánh cách decision 30 về bên phải, nhưng trục đó nằm trong bề ngang action luồng chính kế tiếp (A-3, A-4 rộng 180, cùng trục với decision). Đã đặt trục ở x = 600 (cách mép phải action luồng chính 30) cho E-06 và E-12 để giữ quy tắc "cạnh không cắt qua node" (C7.3).
- F10.4 đòi decision đặt "ngay dưới action phát sinh điều kiện" và trong partition của chủ thể đánh giá điều kiện. Với bước 9, action A-9 thuộc partition Cổng thanh toán còn hệ thống đánh giá kết quả, nên D-9 đặt trong P-SYS, thấp hơn A-9 nhưng không thẳng dưới A-9; cạnh E-26 đi từ A-9 về D-9 có điểm uốn.
- F10.5 chỉ quy định ID partition "P-ACT-nn" cho một tác nhân. Partition chung của hai tác nhân chính (F10.4) dùng ID P-ACT-01-02, ghép hai mã ACT.
- Target 1 với hàng Quan hệ: P03 chỉ có association cho UC-008; hàng Quan hệ ghi "Không có" quan hệ include, extend, generalization kèm mã association để đối chiếu được với P03.
