# P11a - Sơ đồ dịch chuyển màn hình (screen-transition) - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md (C7); P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-002, UC-008, UC-013, UC-015 (1.0); P08-analysis-model.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 1 |
| Phạm vi | Toàn hệ thống, giai đoạn 1: 19 màn hình (SCR-01 đến SCR-19) của 4 tác nhân người và 4 node Start. File sơ đồ: diagrams/P11a-screen-transition.drawio (một trang, mỗi tác nhân một partition ngang) |

Sơ đồ có 19 màn hình, không quá 20 nên giữ một trang; bốn tác nhân là bốn thành phần liên thông riêng nên mỗi tác nhân một partition. Màn hình rộng 160, cao 60; node Start 40 x 40. Toạ độ x, y ở bảng Node là toạ độ tuyệt đối trên trang; trong file .drawio toạ độ của node con được ghi tương đối theo partition (y trừ đi y của partition, x của partition bằng 0). ID của mxCell trùng ID ở các bảng.

## 1. Bảng Node

| ID (SCR) | Loại (Screen / Start) | Nhãn (tên màn hình) | Stereotype (Loại màn hình ở F2) | Thuộc về (tác nhân) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| START-ACT-01 | Start | Điểm khởi đầu | - | ACT-01 Hành khách | Mở website (ASM-60) | 60 | 70 | 40 | 40 |
| SCR-01 | Screen | Trang chủ hành khách | Độc lập | ACT-01 Hành khách | Điều hướng; lối vào UC-001, UC-007, UC-009, UC-011 chưa có màn hình đích | 200 | 60 | 160 | 60 |
| SCR-02 | Screen | Tìm và chọn chuyến | Độc lập | ACT-01 Hành khách | UC-002 bước 1-3 | 500 | 60 | 160 | 60 |
| SCR-03 | Screen | Chọn chỗ và nhập thông tin người đi | Phụ thuộc có dữ liệu | ACT-01 Hành khách | UC-002 bước 4-9 | 800 | 60 | 160 | 60 |
| SCR-04 | Screen | Thanh toán lần đặt | Phụ thuộc có dữ liệu | ACT-01 Hành khách | UC-002 bước 9-10; chờ Q-84 | 1100 | 60 | 160 | 60 |
| SCR-05 | Screen | Vé đã phát hành | Phụ thuộc có dữ liệu | ACT-01 Hành khách | Màn hình kết thúc của UC-002 (bước 13) | 1400 | 60 | 160 | 60 |
| SCR-06 | Screen | Nhập vé cần trả | Độc lập | ACT-01 Hành khách | UC-008 bước 1-3 | 500 | 220 | 160 | 60 |
| SCR-07 | Screen | Xác nhận trả vé | Con phụ thuộc | ACT-01 Hành khách | Pop-up modal trên SCR-06 | 800 | 220 | 160 | 60 |
| SCR-08 | Screen | Kết quả trả vé | Phụ thuộc có dữ liệu | ACT-01 Hành khách | Màn hình kết thúc của UC-008 (bước 11) | 1100 | 220 | 160 | 60 |
| START-ACT-02 | Start | Điểm khởi đầu | - | ACT-02 Nhân viên bán vé | Sau khi có phiên làm việc (ASM-09, ASM-60) | 60 | 470 | 40 | 40 |
| SCR-09 | Screen | Trang chủ nhân viên bán vé | Độc lập | ACT-02 Nhân viên bán vé | Điều hướng; lối vào UC-004, UC-005, UC-007 chưa có màn hình đích | 200 | 460 | 160 | 60 |
| SCR-10 | Screen | Nhập vé cần trả tại quầy | Độc lập | ACT-02 Nhân viên bán vé | UC-008 bước 1-3 | 500 | 460 | 160 | 60 |
| SCR-11 | Screen | Xác nhận trả vé tại quầy | Con phụ thuộc | ACT-02 Nhân viên bán vé | Pop-up modal trên SCR-10 | 800 | 460 | 160 | 60 |
| SCR-12 | Screen | Kết quả trả vé tại quầy | Phụ thuộc có dữ liệu | ACT-02 Nhân viên bán vé | Màn hình kết thúc của UC-008 (bước 11) | 1100 | 460 | 160 | 60 |
| START-ACT-03 | Start | Điểm khởi đầu | - | ACT-03 Nhân viên điều hành | Sau khi có phiên làm việc (ASM-09, ASM-60) | 60 | 710 | 40 | 40 |
| SCR-13 | Screen | Trang chủ nhân viên điều hành | Độc lập | ACT-03 Nhân viên điều hành | Điều hướng; lối vào UC-012 chưa có màn hình đích | 200 | 700 | 160 | 60 |
| SCR-14 | Screen | Chỉ định chuyến cần huỷ | Độc lập | ACT-03 Nhân viên điều hành | UC-013 bước 1-3 | 500 | 700 | 160 | 60 |
| SCR-15 | Screen | Xác nhận huỷ chuyến | Con phụ thuộc | ACT-03 Nhân viên điều hành | Pop-up modal trên SCR-14 | 800 | 700 | 160 | 60 |
| SCR-16 | Screen | Kết quả huỷ chuyến | Phụ thuộc có dữ liệu | ACT-03 Nhân viên điều hành | Màn hình kết thúc của UC-013 (bước 11) | 1100 | 700 | 160 | 60 |
| START-ACT-05 | Start | Điểm khởi đầu | - | ACT-05 Phụ xe | Mở ứng dụng khi có phiên làm việc (ASM-09, ASM-60) | 60 | 950 | 40 | 40 |
| SCR-17 | Screen | Chọn chuyến soát vé | Độc lập | ACT-05 Phụ xe | UC-015 bước 1 | 200 | 940 | 160 | 60 |
| SCR-18 | Screen | Soát vé | Phụ thuộc có dữ liệu | ACT-05 Phụ xe | UC-015 bước 2-9 | 500 | 940 | 160 | 60 |
| SCR-19 | Screen | Kết quả soát vé của chuyến | Phụ thuộc có dữ liệu | ACT-05 Phụ xe | Màn hình kết thúc của UC-015 (bước 11) | 800 | 940 | 160 | 60 |

Bảng Partition (container của node theo tác nhân):

| ID | Loại | Nhãn | x | y | w | h |
|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Hành khách (ACT-01) | 0 | 0 | 1700 | 360 |
| P-ACT-02 | Partition | Nhân viên bán vé (ACT-02) | 0 | 400 | 1700 | 200 |
| P-ACT-03 | Partition | Nhân viên điều hành (ACT-03) | 0 | 640 | 1700 | 200 |
| P-ACT-05 | Partition | Phụ xe (ACT-05) | 0 | 880 | 1700 | 200 |

## 2. Bảng Edge

Dữ liệu truyền chỉ ghi giá trị khác "Không có" ở mẫu 4 (dữ liệu của màn hình trước mà màn hình đích làm việc trên đó) và ở mẫu 2 (dữ liệu pop-up hiển thị). Cột Nhãn trên sơ đồ là bản rút gọn: mẫu 4 ghi dữ liệu truyền, các mẫu khác ghi "sự kiện [điều kiện]". Cột Điểm uốn là toạ độ tuyệt đối theo thứ tự từ nguồn tới đích, "-" là cạnh đi thẳng.

| ID | Nguồn | Đích | Mẫu dịch chuyển | Sự kiện kích hoạt | Điều kiện | Dữ liệu truyền | UC bước | Nhãn trên sơ đồ | Điểm uốn |
|---|---|---|---|---|---|---|---|---|---|
| E-01 | START-ACT-01 | SCR-01 | Mẫu 1 (đơn giản) | Mở website | Không có | Không có | - | mở website | - |
| E-02 | SCR-01 | SCR-02 | Mẫu 1 (đơn giản) | Chọn lối vào Đặt vé trực tuyến | Không có | Không có | UC-002 bước 1 | chọn Đặt vé | - |
| E-03 | SCR-02 | SCR-03 | Mẫu 4 (phụ thuộc có dữ liệu) | Chọn một chuyến trong danh sách | Chuyến còn chỗ trống (BR-03); không còn thì hiển thị MSG-05 và ở lại SCR-02 | Chuyến đã chọn (tuyến, giờ xuất bến) | UC-002 bước 3, 4, 4a | Chuyến đã chọn | - |
| E-04 | SCR-03 | SCR-04 | Mẫu 4 (phụ thuộc có dữ liệu) | Nhấn Tiếp tục thanh toán | Từ 1 đến 5 chỗ, mọi chỗ còn trống, đủ và đúng định dạng thông tin người đi (BR-01, BR-02, BR-03, ASM-15); không thì MSG-06 đến MSG-09 và ở lại SCR-03 | Lần đặt đã giữ chỗ: chuyến, chỗ, họ tên và số điện thoại người đi, tổng tiền (BR-06) | UC-002 bước 5-9, 6a, 6b, 7a, 7b | Lần đặt đã giữ chỗ | - |
| E-05 | SCR-04 | SCR-05 | Mẫu 4 (phụ thuộc có dữ liệu) | Thanh toán thành công (UC-003 trả kết quả thành công) | Chưa hết thời hạn giữ chỗ (BR-07); thanh toán không thành công thì MSG-11 và ở lại SCR-04 | Các vé đã phát hành: mã vé, chỗ, người đi, giá vé, tổng tiền | UC-002 bước 10-13, 10a; chờ Q-84 | Vé đã phát hành | - |
| E-06 | SCR-04 | SCR-02 | Mẫu 1 (đơn giản) | Nhấn Tìm chuyến khác trong MSG-10 | Hết thời hạn giữ chỗ mà thanh toán chưa thành công (BR-07) | Không có (tiêu chí tìm được giữ lại theo MSG-10) | UC-002 bước 9a, 9a1, 9a2 | đóng MSG-10 [hết hạn giữ chỗ] | (1180,170); (580,170) |
| E-07 | SCR-01 | SCR-06 | Mẫu 1 (đơn giản) | Chọn lối vào Trả vé | Không có | Không có | UC-008 bước 1 | chọn Trả vé | (280,250) |
| E-08 | SCR-06 | SCR-07 | Mẫu 2 (con phụ thuộc) | Nhấn Xem thông tin trả vé | Có vé khớp, chưa huỷ, đúng kênh mua, còn từ 4 giờ trở lên (BR-11, BR-12); không thì MSG-15, MSG-17, MSG-18, MSG-20 và ở lại SCR-06 | Thông tin vé, mức hoàn, số tiền hoàn (bước 5) | UC-008 bước 1-5, 2a, 2b, 3a, 3b | xem thông tin [hợp lệ] | - |
| E-09 | SCR-07 | SCR-08 | Mẫu 4 (phụ thuộc có dữ liệu) | Nhấn Xác nhận trả vé | Cổng thanh toán hoàn tiền thành công (bước 9); không thì MSG-22 và pop-up đóng về SCR-06 | Vé đã trả: mã vé, trạng thái, số tiền hoàn, hình thức hoàn | UC-008 bước 6-11, 9a | Kết quả trả vé | - |
| E-10 | START-ACT-02 | SCR-09 | Mẫu 1 (đơn giản) | Có phiên làm việc (ASM-09) | Không có | Không có | - | có phiên làm việc | - |
| E-11 | SCR-09 | SCR-10 | Mẫu 1 (đơn giản) | Chọn lối vào Trả vé | Không có | Không có | UC-008 bước 1 | chọn Trả vé | - |
| E-12 | SCR-10 | SCR-11 | Mẫu 2 (con phụ thuộc) | Nhấn Xem thông tin trả vé | Có vé khớp, chưa huỷ, đúng kênh mua, còn từ 4 giờ trở lên (BR-11, BR-12); không thì MSG-16, MSG-17, MSG-19, MSG-20 và ở lại SCR-10 | Thông tin vé, mức hoàn, số tiền hoàn (bước 5) | UC-008 bước 1-5, 2a, 2b, 3a, 3b | xem thông tin [hợp lệ] | - |
| E-13 | SCR-11 | SCR-12 | Mẫu 4 (phụ thuộc có dữ liệu) | Nhấn Xác nhận trả vé | Vé mua tại quầy, hoàn bằng tiền mặt (BR-16) | Vé đã trả: mã vé, trạng thái, số tiền hoàn, hình thức hoàn | UC-008 bước 6, 7, 7a, 10, 11 | Kết quả trả vé | - |
| E-14 | START-ACT-03 | SCR-13 | Mẫu 1 (đơn giản) | Có phiên làm việc (ASM-09) | Không có | Không có | - | có phiên làm việc | - |
| E-15 | SCR-13 | SCR-14 | Mẫu 1 (đơn giản) | Chọn lối vào Huỷ chuyến | Không có | Không có | UC-013 bước 1 | chọn Huỷ chuyến | - |
| E-16 | SCR-14 | SCR-15 | Mẫu 2 (con phụ thuộc) | Nhấn Xem thông tin huỷ chuyến | Có chuyến khớp trong lịch chạy, chưa huỷ, chưa tới giờ xuất bến (ASM-24); không thì MSG-26 đến MSG-28 và ở lại SCR-14 | Thông tin chuyến, số vé theo kênh mua, số đặt chỗ chưa thanh toán, tổng số tiền hoàn (bước 3) | UC-013 bước 1-3, 2a, 2b, 2c | xem thông tin [hợp lệ] | - |
| E-17 | SCR-15 | SCR-16 | Mẫu 4 (phụ thuộc có dữ liệu) | Nhấn Xác nhận huỷ chuyến | Không có | Kết quả huỷ chuyến: số vé đã huỷ, kết quả hoàn tiền, số tin nhắn đã gửi, mã vé hoàn không thành công | UC-013 bước 4-11, 5a, 6a, 8a | Kết quả huỷ chuyến | - |
| E-18 | START-ACT-05 | SCR-17 | Mẫu 1 (đơn giản) | Mở ứng dụng soát vé khi có phiên làm việc (ASM-09) | Không có | Không có | - | mở ứng dụng | - |
| E-19 | SCR-17 | SCR-18 | Mẫu 4 (phụ thuộc có dữ liệu) | Chọn chuyến và nhấn Bắt đầu soát vé | Chuyến đã có danh sách hành khách trên máy (ASM-32); chưa có danh sách chờ Q-85 | Chuyến cần soát (tuyến, giờ xuất bến) | UC-015 bước 1, 2 | Chuyến cần soát | - |
| E-20 | SCR-18 | SCR-19 | Mẫu 4 (phụ thuộc có dữ liệu) | Nhấn Kết thúc soát vé | Không có | Kết quả soát vé của chuyến: số vé đã soát, số vé còn hiệu lực chưa soát, trạng thái gửi | UC-015 bước 9-11, 10a | Kết quả soát vé | - |

Style theo bốn mẫu: mẫu 1 là dashed=1;endArrow=open;endFill=0;html=1; (E-01, E-02, E-06, E-07, E-10, E-11, E-14, E-15, E-18); mẫu 2 là dashed=0;startArrow=diamondThin;startFill=0;endArrow=open;endFill=0;html=1; (E-08, E-12, E-16); mẫu 4 là dashed=0;endArrow=open;endFill=0;html=1; (E-03, E-04, E-05, E-09, E-13, E-17, E-19, E-20). Mẫu 3 không dùng vì giai đoạn này không có pop-up không khoá màn hình cha. File .drawio thêm vào style các thuộc tính trình bày fontSize, labelBackgroundColor và điểm neo exit, entry.

## 3. Kiểm tra

- Khả năng đến được: ACT-01 có START-ACT-01 --> SCR-01, từ đó tới SCR-02 đến SCR-05 (E-02 đến E-05) và SCR-06 đến SCR-08 (E-07 đến E-09). ACT-02 có SCR-09 đến SCR-12 (E-10 đến E-13). ACT-03 có SCR-13 đến SCR-16 (E-14 đến E-17). ACT-05 có SCR-17 đến SCR-19 (E-18 đến E-20). Cả 19 màn hình đến được từ node Start của tác nhân.
- Lối ra: SCR-01 đến SCR-04, SCR-06, SCR-09, SCR-10, SCR-13, SCR-14, SCR-17, SCR-18 có cạnh đi. SCR-07, SCR-11, SCR-15 là pop-up, lối ra là đóng về màn hình cha (ngầm định của mẫu 2). SCR-05, SCR-08, SCR-12, SCR-16, SCR-19 là màn hình kết thúc của use case (ghi ở cột Ghi chú); người dùng rời bằng tên hệ thống ở header trở về màn hình điều hướng (quy định STT 39 của ui-standards.md), còn ở ứng dụng soát vé thì bắt đầu phiên mới từ SCR-17.
- Không vẽ cạnh đóng pop-up: việc đóng SCR-07 bằng "Không trả vé" (MSG-21) hoặc sau MSG-22, đóng SCR-11 bằng "Không trả vé", đóng SCR-15 bằng "Không huỷ chuyến" (MSG-29) đều quay về màn hình cha theo mẫu 2.
- Không vẽ cạnh quay lại: P04 không có dịch chuyển quay lại màn hình trước; các luồng "Quay lại bước n" của P04 (2a, 4a, 6a, 6b, 7a, 7b, 10a của UC-002; 2a, 2b, 3a, 3b của UC-008; 2a, 2b, 2c của UC-013; luồng 5a, 5b, 5c của UC-015) xảy ra trong cùng một màn hình bằng thông điệp (quy định STT 47), không có dịch chuyển.
- Cạnh E-06 (SCR-04 --> SCR-02) là dịch chuyển duy nhất sau khi use case kết thúc thất bại; được quy định ở MSG-10 theo luồng 9a2, chọn mẫu 1 vì SCR-04 không còn là ngữ cảnh làm việc.
- Liên kết tên hệ thống ở header của mọi màn hình web về màn hình điều hướng (quy định STT 39) và nút Quay lại của trình duyệt (quy định STT 65) là hành vi chung của nền tảng, không vẽ thành cạnh để sơ đồ không có thêm một cạnh trùng lặp ở mỗi màn hình web.
- Lối vào chưa có màn hình đích: SCR-01 (UC-001, UC-007, UC-009, UC-011), SCR-09 (UC-004, UC-005, UC-007), SCR-13 (UC-012) có lối vào use case chưa phân tích nên chưa có cạnh; ACT-04 chưa có node nào. Cần chạy lại khi các use case này có P04, P07.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | Không có câu hỏi mới ở file này. Q-84 (thanh toán UC-003, cạnh E-04, E-05) và Q-85 (chưa có danh sách trên máy, cạnh E-19) được nêu ở screen-list.md | Không có | Không có |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | Không có giả định mới ở file này. ASM-60 (điểm khởi đầu và màn hình đầu tiên của mỗi tác nhân) được nêu ở screen-list.md | Không có | START-ACT-01, START-ACT-02, START-ACT-03, START-ACT-05 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Vấn đề còn mở

- Target 5: mọi dịch chuyển dùng một trong bốn mẫu; mẫu 3 chưa có trường hợp sử dụng. Mọi màn hình đến được từ Start và có lối ra theo mục 3.
- Target 11: bố cục .drawio được kiểm bằng tính toán (toạ độ node là bội số của 10, khoảng cách tối thiểu giữa hai node từ 40, đoạn thẳng của cạnh không cắt qua node nào); chưa mở bằng draw.io để xem nhãn cạnh và chữ trong node, nên nhãn dài ở khe 140 giữa hai node có thể chồng lên node và cần chỉnh tay.
- Chọn giữa hai quy tắc (C9): C7.3 dùng edgeStyle=orthogonalEdgeStyle cho sơ đồ lớp, package, ERD, còn F3 của P11a quy định nguyên chuỗi style của bốn mẫu. Đã giữ nguyên chuỗi style của F3 và vẽ cạnh gấp khúc bằng điểm uốn tường minh (E-06, E-07).
- Chọn giữa hai quy tắc (C9): F3 chỉ cho cột Loại là Screen hoặc Start, còn C7.3 và việc gom theo tác nhân cần container. Đã thêm bảng Partition riêng và giữ bảng Node đúng hai giá trị Loại.
- Chọn giữa hai quy tắc (C9): stereotype «Loại màn hình» và tên màn hình trong node nhiều dòng làm chữ tràn node cao 60 ở cỡ chữ 10; chấp nhận vì chiều cao 60 là quy định bắt buộc của F3.
