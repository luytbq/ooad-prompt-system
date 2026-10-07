# P04 - Đặc tả use case UC-013 Huỷ chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.1; P03-usecase-model.md 1.0 (Mục 1, Mục 2, Câu hỏi mở, Giả định); P04-uc-specs/_BR-register.md (BR-01 đến BR-16); P04-uc-specs/UC-002-book-ticket-online.md 1.0 (Câu hỏi mở, Giả định; Mục 5 để dùng chung ví dụ vé); P04-uc-specs/UC-008-return-ticket.md 1.0 (Câu hỏi mở, Giả định; Mục 6, Mục 8 vì dùng chung BR-15, BR-16 và trạng thái vé đã huỷ) |
| Phạm vi | UC-013 |

Quy ước trích nguồn theo P00: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-013 |
| Tên use case | Huỷ chuyến (Cancel Trip) |
| Tác nhân chính | ACT-03 Nhân viên điều hành |
| Tác nhân phụ | ACT-06 Cổng thanh toán, ACT-07 Cổng SMS |
| Mô tả ngắn | Use case này mô tả tương tác giữa nhân viên điều hành và hệ thống khi nhân viên điều hành muốn huỷ một chuyến không chạy được do xe hỏng hoặc thời tiết. Kết quả là chuyến và các vé của chuyến bị huỷ, hành khách đã có vé được báo qua SMS và được hoàn 100% giá vé. |
| Sự kiện kích hoạt | Chuyến không chạy được do xe hỏng hoặc thời tiết (EV-17) |
| Tiền điều kiện | Nhân viên điều hành đã được xác thực và đang có phiên làm việc (ASM-09). |
| Hậu điều kiện (thành công) | Chuyến ở trạng thái đã huỷ (ASM-26).<br>Mọi vé còn hiệu lực của chuyến ở trạng thái đã huỷ; mọi đặt chỗ qua điện thoại chưa thanh toán của chuyến đã bị huỷ (ASM-26, ASM-27).<br>Mỗi vé đã huỷ có khoản hoàn bằng 100% giá vé (BR-17, BR-19): với vé mua trực tuyến, khoản hoàn đã được Cổng thanh toán xác nhận (BR-15) hoặc được ghi nhận là chưa thành công (ASM-31); với vé mua tại quầy, khoản hoàn được ghi nhận là chờ chi tiền mặt tại quầy (BR-16, ASM-28).<br>Tin nhắn báo huỷ chuyến của từng vé đã huỷ đã được gửi tới Cổng SMS để chuyển tới số điện thoại người đi của vé (BR-18, ASM-29, ASM-30). |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công, chuyến, các vé và các đặt chỗ của chuyến không thay đổi (mọi luồng kết thúc thất bại đều kết thúc trước bước 5). |
| Quan hệ | Không có quan hệ include, extend, generalization (P03 chỉ có association RL-18 ACT-03, RL-19 ACT-06, RL-20 ACT-07 với UC-013) |
| Điểm mở rộng | Không có |
| REQ | REQ-09, REQ-20, REQ-25, REQ-34, REQ-35, REQ-36, REQ-42, REQ-47, REQ-48, REQ-49, REQ-50, REQ-58 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Nhân viên điều hành | Yêu cầu huỷ chuyến và chỉ định chuyến cần huỷ (xem Dữ liệu vào 1). |
| 2 | Hệ thống | Kiểm tra chuyến đã chỉ định có trong lịch chạy, chưa bị huỷ và chưa tới giờ xuất bến (ASM-24). |
| 3 | Hệ thống | Hiển thị thông tin chuyến, số vé còn hiệu lực theo kênh mua, số đặt chỗ qua điện thoại chưa thanh toán và tổng số tiền hoàn (xem Dữ liệu ra 1) (BR-17, ASM-25). |
| 4 | Nhân viên điều hành | Xác nhận huỷ chuyến (ASM-25). |
| 5 | Hệ thống | Ghi nhận chuyến ở trạng thái đã huỷ, huỷ mọi vé còn hiệu lực và mọi đặt chỗ qua điện thoại chưa thanh toán của chuyến (ASM-26, ASM-27). |
| 6 | Hệ thống | Tính số tiền hoàn bằng 100% giá vé (BR-17, BR-19, ASM-22) và xác định hình thức hoàn theo kênh mua (BR-15, BR-16, ASM-28) cho từng vé đã huỷ. |
| 7 | Hệ thống | Gửi yêu cầu hoàn số tiền hoàn của từng vé mua trực tuyến tới Cổng thanh toán (BR-15). |
| 8 | Cổng thanh toán | Trả về kết quả hoàn tiền của từng vé. |
| 9 | Hệ thống | Ghi nhận khoản hoàn của từng vé đã huỷ: vé mua trực tuyến đã được Cổng thanh toán xác nhận hoàn, vé mua tại quầy chờ chi tiền mặt tại quầy (BR-15, BR-16, ASM-28). |
| 10 | Hệ thống | Gửi tin nhắn báo huỷ chuyến kèm số tiền hoàn và hình thức hoàn tới số điện thoại người đi của từng vé đã huỷ qua Cổng SMS (xem Dữ liệu ra 2) (BR-18, ASM-29, ASM-30). |
| 11 | Hệ thống | Hiển thị kết quả huỷ chuyến cho nhân viên điều hành (xem Dữ liệu ra 3) (ASM-31). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Không có chuyến nào trong lịch chạy khớp tuyến, ngày và giờ xuất bến đã chỉ định (ASM-24) | Hệ thống | Thông báo không có chuyến khớp thông tin đã chỉ định. | Quay lại bước 1 |
| 2b | Có chuyến khớp và chuyến đã bị huỷ trước đó (ASM-26) | Hệ thống | Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã bị huỷ. | Kết thúc use case (thất bại) |
| 2c | Có chuyến khớp, chuyến chưa bị huỷ và đã tới hoặc đã qua giờ xuất bến (ASM-24) | Hệ thống | Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã tới giờ xuất bến (ASM-24). | Kết thúc use case (thất bại) |
| 4a | Nhân viên điều hành không xác nhận huỷ chuyến (ASM-25) | Hệ thống | Thông báo yêu cầu huỷ chuyến đã được bỏ và chuyến giữ nguyên. | Kết thúc use case (thất bại) |
| 5a | Chuyến không có vé còn hiệu lực nào | - | - | Tiếp tục bước 11 |
| 6a | Chuyến có vé còn hiệu lực và không vé nào được mua trực tuyến | - | - | Tiếp tục bước 9 |
| 8a | Cổng thanh toán trả về kết quả hoàn tiền không thành công cho ít nhất một vé | Hệ thống | Ghi nhận khoản hoàn của các vé đó là chưa thành công để nhà xe xử lý lại (ASM-31). | Tiếp tục bước 9 |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 1)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Tuyến | Tuyến của chuyến cần huỷ, gồm điểm đi và điểm đến | Có | Là một tuyến nhà xe đang khai thác (REQ-01, REQ-42) | Hà Nội - Lào Cai |
| 2 | Ngày xuất bến | Ngày chuyến cần huỷ xuất bến | Có | Có chuyến của tuyến đã chỉ định xuất bến vào ngày này trong lịch chạy (ASM-24) | 03/02/2027 |
| 3 | Giờ xuất bến | Giờ xuất bến của chuyến cần huỷ (REQ-42) | Có | Cùng với tuyến và ngày xuất bến, khớp đúng một chuyến trong lịch chạy (ASM-24) | 21:00 |

Dữ liệu ra 1 (bước 3)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tuyến và giờ xuất bến | Chuyến sắp bị huỷ (REQ-42) | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Hà Nội - Lào Cai, 21:00 03/02/2027 |
| 2 | Số vé mua trực tuyến | Số vé còn hiệu lực của chuyến được mua trực tuyến (ASM-25) | Số nguyên, căn phải | 3 |
| 3 | Số vé mua tại quầy | Số vé còn hiệu lực của chuyến được mua tại quầy, gồm vé đặt qua điện thoại đã thanh toán tại quầy (ASM-25) | Số nguyên, căn phải | 2 |
| 4 | Số đặt chỗ qua điện thoại chưa thanh toán | Số đặt chỗ của chuyến sẽ bị huỷ cùng chuyến, không hoàn tiền (ASM-27) | Số nguyên, căn phải | 1 |
| 5 | Tổng số tiền hoàn | Tổng số tiền hoàn của mọi vé còn hiệu lực của chuyến (BR-17) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 1.800.000 đ |

Dữ liệu ra 2 (bước 10), nội dung tin nhắn báo huỷ chuyến của một vé

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Mã vé | Mã của vé đã huỷ (BR-10) | Chuỗi chữ và số do hệ thống cấp | SV0000123 |
| 2 | Tuyến và giờ xuất bến | Chuyến đã bị huỷ (ASM-29) | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Hà Nội - Lào Cai, 21:00 03/02/2027 |
| 3 | Thông báo huỷ chuyến | Câu báo chuyến đã bị nhà xe huỷ (BR-18) | Chữ | Chuyến đã bị huỷ |
| 4 | Số tiền hoàn | 100% giá vé (BR-17) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ" | 360.000 đ |
| 5 | Hình thức hoàn | Kênh hoàn theo kênh mua (BR-15, BR-16, ASM-28) | Một trong hai giá trị "Qua cổng thanh toán" / "Tiền mặt tại quầy" | Qua cổng thanh toán |

Dữ liệu ra 3 (bước 11)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tuyến và giờ xuất bến | Chuyến đã huỷ | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Hà Nội - Lào Cai, 21:00 03/02/2027 |
| 2 | Số vé đã huỷ | Số vé còn hiệu lực đã chuyển sang trạng thái đã huỷ ở bước 5 (ASM-26) | Số nguyên, căn phải | 5 |
| 3 | Số vé đã hoàn qua cổng thanh toán | Số vé mua trực tuyến có khoản hoàn được Cổng thanh toán xác nhận (BR-15) | Số nguyên, căn phải | 3 |
| 4 | Số vé hoàn qua cổng thanh toán không thành công | Số vé mua trực tuyến có khoản hoàn chưa thành công (ASM-31) | Số nguyên, căn phải | 0 |
| 5 | Số vé chờ hoàn tiền mặt tại quầy | Số vé mua tại quầy có khoản hoàn chờ chi tiền mặt (BR-16, ASM-28) | Số nguyên, căn phải | 2 |
| 6 | Tổng số tiền hoàn | Tổng khoản hoàn của mọi vé đã huỷ, kể cả khoản chưa thành công (BR-17) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 1.800.000 đ |
| 7 | Số đặt chỗ qua điện thoại đã huỷ | Số đặt chỗ chưa thanh toán bị huỷ cùng chuyến (ASM-27) | Số nguyên, căn phải | 1 |
| 8 | Số tin nhắn đã gửi | Số tin nhắn báo huỷ chuyến đã gửi tới Cổng SMS, mỗi vé đã huỷ một tin (BR-18, ASM-29) | Số nguyên, căn phải | 5 |
| 9 | Mã vé hoàn không thành công | Danh sách mã vé có khoản hoàn chưa thành công, để nhà xe xử lý lại (ASM-31) | Các mã vé ngăn cách bằng dấu phẩy, hoặc "Không có" | Không có |

Ví dụ tính số tiền hoàn (BR-17, BR-19), dùng chuyến của ví dụ UC-002 và UC-008: chuyến Hà Nội - Lào Cai xuất bến 21:00 03/02/2027, giá vé đã thanh toán của mỗi vé 360.000 đ (300.000 x (1 + 20/100) = 360.000 đ theo BR-05 ở UC-002; giá vé dùng tính hoàn theo ASM-22). Chuyến có 3 vé mua trực tuyến, 2 vé mua tại quầy và 1 đặt chỗ qua điện thoại chưa thanh toán.

- Số tiền hoàn mỗi vé = 360.000 x 100/100 = 360.000 đ.
- Hoàn qua cổng thanh toán = 3 x 360.000 = 1.080.000 đ; chờ chi tiền mặt tại quầy = 2 x 360.000 = 720.000 đ; tổng số tiền hoàn = 1.080.000 + 720.000 = 1.800.000 đ (bằng 5 x 360.000).
- Đặt chỗ qua điện thoại chưa thanh toán không được hoàn tiền và không được tính vào tổng (ASM-27); số tin nhắn gửi đi = số vé đã huỷ = 3 + 2 = 5.
- Huỷ lúc 19:00 03/02/2027, còn 21:00 - 19:00 = 2 giờ trước giờ xuất bến: mỗi vé vẫn được hoàn 360.000 đ, vì mốc 4 giờ (BR-12) và mức 90%, 50% (BR-13, BR-14) chỉ áp dụng cho trả vé (P00 mục 5 dòng 28).
- Luồng 8a với 1 vé mua trực tuyến hoàn không thành công: số vé đã hoàn qua cổng thanh toán = 3 - 1 = 2, số vé hoàn không thành công = 1, tổng số tiền hoàn vẫn là 1.800.000 đ.
- Mức lớn nhất cho một chuyến: xe giường nằm 40 chỗ (REQ-02) có tối đa 40 vé, tổng số tiền hoàn tối đa = 40 x 360.000 = 14.400.000 đ và 40 tin nhắn.

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-10 | Mỗi chỗ được phát hành thành đúng một vé có một mã vé. | Ràng buộc | Dữ liệu ra 2 | REQ-18 | Đã có |
| BR-15 | Vé mua trực tuyến được hoàn tiền qua cổng thanh toán trực tuyến của đối tác. | Ràng buộc | 6, 7, 9, Dữ liệu ra 2, Dữ liệu ra 3 (áp dụng cho huỷ chuyến theo ASM-28) | REQ-34 | Đã có |
| BR-16 | Vé mua tại quầy được hoàn bằng tiền mặt tại quầy. | Ràng buộc | 6, 6a, 9, Dữ liệu ra 2, Dữ liệu ra 3 (áp dụng cho huỷ chuyến theo ASM-28) | REQ-36 | Đã có |
| BR-17 | Số tiền hoàn của một vé thuộc chuyến bị nhà xe huỷ bằng 100% giá vé. | Tính toán | 3, 6, Dữ liệu ra 1, Dữ liệu ra 2, Dữ liệu ra 3 | REQ-50 | Mới |
| BR-18 | Khi chuyến bị huỷ, mọi hành khách đã có vé còn hiệu lực của chuyến được báo việc huỷ chuyến qua SMS (ASM-27). | Kích hoạt hành động | 10, Dữ liệu ra 2 | REQ-48 | Mới |
| BR-19 | Khi chuyến bị huỷ, mọi hành khách đã có vé còn hiệu lực của chuyến được hoàn tiền theo BR-17 (ASM-27). | Kích hoạt hành động | 6 | REQ-49 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Yêu cầu hoàn tiền vé mua trực tuyến của chuyến bị huỷ được trao đổi với cổng thanh toán trực tuyến của đối tác qua API hoàn tiền; tài liệu API chưa có (Q-24). | Giao tiếp (+) | REQ-35 |
| 2 | Tin nhắn báo huỷ chuyến được gửi qua API REST của cổng SMS của nhà mạng. | Giao tiếp (+) | REQ-20 |

## 8. Thông tin bổ sung

- Mốc 4 giờ (BR-12) và mức hoàn 90%, 50% (BR-13, BR-14) của UC-008 Trả vé không áp dụng cho vé của chuyến bị huỷ: P00 mục 5 dòng 28 tách hành khách tự trả vé khác với nhà xe huỷ chuyến.
- "Vé còn hiệu lực" là vé đã phát hành chưa bị huỷ (ASM-26): không gồm vé đã trả qua UC-008 (ASM-20) và vé cũ đã đổi sang chuyến khác qua UC-007 Đổi vé (chờ Q-21). Vé mới đổi vào chuyến này là vé còn hiệu lực; giá vé dùng tính hoàn của vé đã đổi chờ Q-38.
- Vé của chuyến bị huỷ ở trạng thái đã huỷ, nên UC-008 từ chối trả các vé này (luồng 2b của UC-008) và ứng dụng soát vé báo "vé đã huỷ" khi quét (REQ-58, UC-015 Soát vé lên xe).
- Với vé mua tại quầy, use case này chỉ ghi nhận khoản hoàn chờ chi tiền mặt; việc nhân viên bán vé chi tiền mặt cho khách tới quầy là CAND-43 của P02 (chờ Q-14), hiện chưa có use case nào thực hiện (xem Đề xuất sửa artifact trước).
- Tin nhắn báo huỷ chuyến cần số điện thoại người đi của mọi vé (ASM-30). Khi đặc tả UC-004 Nhận đặt chỗ qua điện thoại và UC-005 Bán vé tại quầy, cần thu số điện thoại người đi cho vé bán tại quầy, hoặc trả lời Q-42 theo hướng khác.
- Chuyến có thể bị huỷ sau mốc gửi danh sách hành khách về máy soát vé 15 phút trước giờ xuất bến (REQ-62) vì ASM-24 cho huỷ tới trước giờ xuất bến. Chuyến không chạy nên không có lượt soát vé nào; Q-11 không làm thay đổi luồng của UC-013.
- Lần đặt trực tuyến đang giữ chỗ của chuyến (BR-07) tại thời điểm huỷ không phải là vé, không được hoàn tiền hay báo SMS trong use case này; cách UC-002 Đặt vé trực tuyến kết thúc lần đặt đó theo ASM-26 (chờ Q-44).
- Tần suất: nguồn không nêu số chuyến bị huỷ; lý do huỷ nguồn nêu làm ví dụ là xe hỏng và thời tiết (Mục 6, câu 4).

## 8a. Kịch bản chính

- KB1: Luồng chính --> chuyến có vé mua trực tuyến và vé mua tại quầy bị huỷ, mọi vé mua trực tuyến được Cổng thanh toán hoàn thành công, mọi người đi nhận tin nhắn báo huỷ chuyến.
- KB2: Luồng chính + 6a --> chuyến chỉ có vé mua tại quầy, khoản hoàn được ghi nhận chờ chi tiền mặt tại quầy.
- KB3: Luồng chính + 5a --> chuyến chưa có vé nào, chuyến và các đặt chỗ chưa thanh toán bị huỷ, không có hoàn tiền và tin nhắn.
- KB4: Luồng chính + 8a --> Cổng thanh toán hoàn không thành công cho một vé, chuyến vẫn bị huỷ và vé đó được liệt kê để xử lý lại.
- KB5: Luồng chính + 2c --> chuyến đã tới giờ xuất bến, không huỷ được.

## 9. Activity diagram

File: diagrams/P04-activity-UC-013.drawio (trang "UC-013").

Bảng Node (x, y là toạ độ tương đối trong partition; partition dùng toạ độ tuyệt đối):

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-03 | Partition | Nhân viên điều hành | - | - | - | ACT-03, tác nhân chính | 0 | 0 | 320 | 2040 |
| P-SYS | Partition | Hệ thống | - | - | - | Chủ ngữ hệ thống mặc định | 320 | 0 | 680 | 2040 |
| P-ACT-06 | Partition | Cổng thanh toán | - | - | - | ACT-06, tác nhân phụ trả về kết quả hoàn tiền; ACT-07 chỉ nhận tin nhắn nên không có partition | 1000 | 0 | 320 | 2040 |
| INIT | Initial | - | - | P-ACT-03 | - | - | 140 | 60 | 40 | 40 |
| M-1 | Merge | - | - | P-ACT-03 | - | Nhận luồng quay lại từ 2a | 140 | 140 | 40 | 40 |
| A-1 | Action | Yêu cầu huỷ chuyến, chỉ định chuyến | - | P-ACT-03 | 1 | - | 70 | 220 | 180 | 60 |
| A-2 | Action | Kiểm tra chuyến còn huỷ được | - | P-SYS | 2 | ASM-24 | 70 | 330 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | - | - | 140 | 430 | 40 | 40 |
| A-2a | Action | Thông báo không có chuyến khớp | - | P-SYS | 2a | ASM-24 | 330 | 420 | 180 | 60 |
| A-2b | Action | Từ chối: chuyến đã bị huỷ | - | P-SYS | 2b | ASM-26 | 330 | 520 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 530 | 40 | 40 |
| A-2c | Action | Từ chối: chuyến đã tới giờ xuất bến | - | P-SYS | 2c | ASM-24 | 330 | 620 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 630 | 40 | 40 |
| A-3 | Action | Hiển thị chuyến, số vé, tổng tiền hoàn | - | P-SYS | 3 | BR-17, ASM-25 | 70 | 520 | 180 | 60 |
| A-4 | Action | Xác nhận huỷ chuyến | - | P-ACT-03 | 4 | ASM-25 | 70 | 640 | 180 | 60 |
| D-4 | Decision | - | - | P-ACT-03 | - | Lựa chọn của tác nhân, đặt trong partition tác nhân | 140 | 740 | 40 | 40 |
| A-4a | Action | Thông báo bỏ yêu cầu, chuyến giữ nguyên | - | P-SYS | 4a | ASM-25 | 330 | 730 | 180 | 60 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 550 | 740 | 40 | 40 |
| A-5 | Action | Huỷ chuyến, vé và đặt chỗ chưa thanh toán | - | P-SYS | 5 | ASM-26, ASM-27 | 70 | 830 | 180 | 60 |
| D-5 | Decision | - | - | P-SYS | - | Luồng 5a không có hành động | 140 | 930 | 40 | 40 |
| A-6 | Action | Tính tiền hoàn 100%, xác định hình thức hoàn | - | P-SYS | 6 | BR-15, BR-16, BR-17, BR-19, ASM-22, ASM-28 | 70 | 1010 | 180 | 60 |
| D-6 | Decision | - | - | P-SYS | - | Luồng 6a không có hành động | 140 | 1110 | 40 | 40 |
| A-7 | Action | Gửi yêu cầu hoàn tới Cổng thanh toán | - | P-SYS | 7 | BR-15 | 70 | 1190 | 180 | 60 |
| A-8 | Action | Trả về kết quả hoàn tiền từng vé | - | P-ACT-06 | 8 | - | 70 | 1300 | 180 | 60 |
| D-8 | Decision | - | - | P-SYS | - | Hệ thống đánh giá kết quả do ACT-06 trả về | 140 | 1410 | 40 | 40 |
| A-8a | Action | Ghi nhận khoản hoàn chưa thành công | - | P-SYS | 8a | ASM-31 | 330 | 1400 | 180 | 60 |
| M-9 | Merge | - | - | P-SYS | - | Nhận luồng từ D-8, A-8a và luồng 6a | 140 | 1500 | 40 | 40 |
| A-9 | Action | Ghi nhận khoản hoàn của từng vé | - | P-SYS | 9 | BR-15, BR-16, ASM-28 | 70 | 1580 | 180 | 60 |
| A-10 | Action | Gửi tin nhắn báo huỷ qua Cổng SMS | - | P-SYS | 10 | BR-18, ASM-29, ASM-30 | 70 | 1680 | 180 | 60 |
| M-11 | Merge | - | - | P-SYS | - | Nhận luồng từ A-10 và luồng 5a | 140 | 1780 | 40 | 40 |
| A-11 | Action | Hiển thị kết quả huỷ chuyến | - | P-SYS | 11 | ASM-31 | 70 | 1860 | 180 | 60 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thành công) | 140 | 1960 | 40 | 40 |

Bảng Edge (Điểm uốn là toạ độ tuyệt đối):

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | M-1 | ControlFlow | - | - | - |
| E-02 | M-1 | A-1 | ControlFlow | - | - | - |
| E-03 | A-1 | A-2 | ControlFlow | - | Sang partition hệ thống | (160,300); (480,300) |
| E-04 | A-2 | D-2 | ControlFlow | - | - | - |
| E-05 | D-2 | A-2a | ControlFlow | [không có chuyến khớp] | Luồng 2a | - |
| E-06 | D-2 | A-2b | ControlFlow | [chuyến đã bị huỷ] | Luồng 2b | (600,450); (600,550) |
| E-07 | D-2 | A-2c | ControlFlow | [chưa huỷ, đã tới giờ xuất bến] | Luồng 2c | (600,450); (600,650) |
| E-08 | D-2 | A-3 | ControlFlow | [chuyến chưa huỷ, chưa tới giờ xuất bến] | Luồng chính | - |
| E-09 | A-2a | M-1 | ControlFlow | - | Quay lại bước 1 | (960,450); (960,160) |
| E-10 | A-2b | FINAL-1 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-11 | A-2c | FINAL-2 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-12 | A-3 | A-4 | ControlFlow | - | Sang partition tác nhân | (480,610); (160,610) |
| E-13 | A-4 | D-4 | ControlFlow | - | - | - |
| E-14 | D-4 | A-4a | ControlFlow | [không xác nhận huỷ] | Luồng 4a; sang partition hệ thống, đi thẳng ở y = 760 | (320,760) |
| E-15 | D-4 | A-5 | ControlFlow | [xác nhận huỷ] | Luồng chính; sang partition hệ thống | (160,800); (480,800) |
| E-16 | A-4a | FINAL-3 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-17 | A-5 | D-5 | ControlFlow | - | - | - |
| E-18 | D-5 | M-11 | ControlFlow | [không có vé còn hiệu lực] | Luồng 5a, tiếp tục bước 11; đi vòng bên trái trục chính | (340,950); (340,1800) |
| E-19 | D-5 | A-6 | ControlFlow | [có vé còn hiệu lực] | Luồng chính | - |
| E-20 | A-6 | D-6 | ControlFlow | - | - | - |
| E-21 | D-6 | M-9 | ControlFlow | [không có vé mua trực tuyến] | Luồng 6a, tiếp tục bước 9; đi vòng bên trái trục chính | (360,1130); (360,1520) |
| E-22 | D-6 | A-7 | ControlFlow | [có vé mua trực tuyến] | Luồng chính | - |
| E-23 | A-7 | A-8 | ControlFlow | - | Sang partition Cổng thanh toán | (480,1270); (1160,1270) |
| E-24 | A-8 | D-8 | ControlFlow | - | Về partition hệ thống | (1160,1380); (480,1380) |
| E-25 | D-8 | A-8a | ControlFlow | [có vé hoàn không thành công] | Luồng 8a | - |
| E-26 | D-8 | M-9 | ControlFlow | [mọi vé hoàn thành công] | Luồng chính | - |
| E-27 | A-8a | M-9 | ControlFlow | - | Tiếp tục bước 9 | (740,1520) |
| E-28 | M-9 | A-9 | ControlFlow | - | - | - |
| E-29 | A-9 | A-10 | ControlFlow | - | - | - |
| E-30 | A-10 | M-11 | ControlFlow | - | - | - |
| E-31 | M-11 | A-11 | ControlFlow | - | - | - |
| E-32 | A-11 | FINAL-4 | ControlFlow | - | Kết thúc use case (thành công) | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a | D-2, A-2a, M-1 |
| 2b | D-2, A-2b, FINAL-1 |
| 2c | D-2, A-2c, FINAL-2 |
| 3 | A-3 |
| 4 | A-4 |
| 4a | D-4, A-4a, FINAL-3 |
| 5 | A-5 |
| 5a | D-5, E-18 (guard [không có vé còn hiệu lực], không có action), M-11 |
| 6 | A-6 |
| 6a | D-6, E-21 (guard [không có vé mua trực tuyến], không có action), M-9 |
| 7 | A-7 |
| 8 | A-8 |
| 8a | D-8, A-8a, M-9 |
| 9 | A-9 |
| 10 | A-10 |
| 11 | A-11, FINAL-4 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-40 | Nhân viên điều hành có được huỷ chuyến đã tới hoặc đã qua giờ xuất bến (ví dụ xe hỏng giữa đường) không? (a) Không, chỉ huỷ chuyến chưa tới giờ xuất bến; (b) Có, hành khách vẫn được hoàn 100% giá vé; (c) Có, với mức hoàn khác | Bước 2; luồng 2c; ASM-24; BR-17 | Mục 6, câu 4: "Khi phải huỷ chuyến (xe hỏng, thời tiết), nhân viên điều hành huỷ chuyến" (không nêu thời điểm được huỷ) |
| Q-41 | Tin nhắn SMS báo huỷ chuyến gồm những thông tin nào? Có nêu lý do huỷ (xe hỏng, thời tiết) không; nếu có, nhân viên điều hành có phải nhập lý do huỷ khi huỷ chuyến không? | Bước 1, 10; Dữ liệu vào 1; Dữ liệu ra 2; ASM-29; liên quan Q-33 | Mục 6, câu 4: "hệ thống gửi SMS cho mọi hành khách đã có vé" (không nêu nội dung) |
| Q-42 | Vé bán tại quầy và vé đặt qua điện thoại đã thanh toán tại quầy có ghi số điện thoại người đi không? Nếu không, hành khách của các vé này được báo huỷ chuyến bằng cách nào? (Có ghi, gửi SMS như vé mua trực tuyến / Không ghi, nhà xe báo bằng cách khác ngoài hệ thống) | Bước 10; Dữ liệu ra 2; ASM-30; BR-18; UC-004, UC-005 (dữ liệu vé) | Mục 6, câu 4: "gửi SMS cho mọi hành khách đã có vé"; Mục 2, câu 1 chỉ nêu số điện thoại người đi khi đặt vé trên website; Mục 4 không nêu dữ liệu vé bán tại quầy |
| Q-43 | Khi huỷ chuyến mà cổng thanh toán hoàn tiền không thành công cho một vé mua trực tuyến, khoản hoàn đó được xử lý tiếp thế nào? (a) Hệ thống tự gửi lại yêu cầu hoàn sau; (b) Nhân viên nhà xe gửi lại yêu cầu hoàn; (c) Khách tới quầy nhận tiền mặt | Luồng 8a; Dữ liệu ra 3; ASM-31; liên quan Q-37 | Mục 5, câu 3: "Vé mua trực tuyến được hoàn qua cổng thanh toán"; project-profile.md, HE_THONG_NGOAI: "API thanh toán và hoàn tiền, chưa có tài liệu API" |
| Q-44 | Lần đặt trực tuyến đang giữ chỗ chờ thanh toán (10 phút) trên một chuyến vào lúc chuyến bị huỷ được xử lý thế nào? (a) Kết thúc ngay, trả chỗ, không cho thanh toán; (b) Vẫn cho thanh toán, vé phát hành rồi được hoàn 100% như vé khác của chuyến | ASM-26; UC-002 (luồng thay thế khi chuyến bị huỷ trong thời hạn giữ chỗ) | Mục 3, câu 1: "Các chỗ đã chọn được giữ trong 10 phút để hành khách thanh toán"; Mục 6, câu 4 chỉ nêu "hành khách đã có vé" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-24 | Nhân viên điều hành chỉ định chuyến cần huỷ bằng tuyến, ngày và giờ xuất bến; chỉ huỷ được chuyến có trong lịch chạy, chưa bị huỷ và chưa tới giờ xuất bến. | Nguồn chỉ nêu "huỷ chuyến (xe hỏng, thời tiết)", không nêu thời điểm được huỷ; chuyến đã xuất bến thì hành khách đã đi một phần hành trình, mức hoàn 100% có thể không còn đúng. Chuyến được xác định bằng tuyến và giờ xuất bến theo REQ-42. Chờ Q-40 | Bước 1, 2; luồng 2a, 2c; Dữ liệu vào 1 |
| ASM-25 | Trước khi huỷ, hệ thống hiển thị thông tin chuyến, số vé còn hiệu lực theo kênh mua, số đặt chỗ qua điện thoại chưa thanh toán và tổng số tiền hoàn để nhân viên điều hành xác nhận; không xác nhận thì chuyến giữ nguyên. | Nguồn không nêu bước xác nhận. Huỷ chuyến không đảo ngược được và kéo theo hoàn tiền cho mọi vé của chuyến; cách làm nhất quán với ASM-19 của UC-008 | Bước 3, 4; luồng 4a; Dữ liệu ra 1 |
| ASM-26 | Chuyến bị huỷ chuyển sang trạng thái đã huỷ và không còn được đặt vé, đặt chỗ hay bán vé. Mọi vé còn hiệu lực (vé đã phát hành chưa bị huỷ) của chuyến chuyển sang trạng thái đã huỷ như vé đã trả (ASM-20). Lần đặt trực tuyến đang giữ chỗ của chuyến kết thúc, chỗ giữ được trả lại và không thể thanh toán tiếp. | EV-17 của P02 ghi phản hồi của hệ thống là "Huỷ chuyến"; nguồn không nêu trạng thái của chuyến, vé và lần đặt đang giữ chỗ sau khi huỷ. Vé đã huỷ khớp quy tắc "vé đã huỷ" khi soát (REQ-58). Chờ Q-44 (lần đặt đang giữ chỗ) | Bước 5; luồng 2b; hậu điều kiện thành công; UC-002 (lần đặt đang giữ chỗ) |
| ASM-27 | "Mọi hành khách đã có vé" (REQ-48, REQ-49) chỉ gồm người đi của các vé còn hiệu lực. Đặt chỗ qua điện thoại chưa thanh toán của chuyến bị huỷ cùng chuyến, không được hoàn tiền và không được gửi tin nhắn. | P02 phân biệt đặt chỗ qua điện thoại với vé (UC-004, UC-006); đặt chỗ chưa thanh toán thì chưa có tiền để hoàn; nguồn không nêu đặt chỗ qua điện thoại ghi số điện thoại nhận tin. Chờ Q-15 | Bước 3, 5; Dữ liệu ra 1, Dữ liệu ra 3; BR-18, BR-19 |
| ASM-28 | Tiền hoàn 100% khi huỷ chuyến được trả theo kênh mua như Mục 5 câu 3: vé mua trực tuyến hoàn qua Cổng thanh toán (BR-15); vé mua tại quầy, gồm vé đặt qua điện thoại đã thanh toán tại quầy, được ghi nhận khoản hoàn chờ chi tiền mặt tại quầy (BR-16). Việc chi tiền mặt diễn ra khi khách tới quầy, ngoài use case này. | Mục 6, câu 4 chỉ nêu "hoàn 100% giá vé", không nêu kênh hoàn; Mục 5 câu 3 là quy định kênh hoàn duy nhất của nguồn. Khách mua tại quầy không có giao dịch nào qua cổng thanh toán để hoàn. Chờ Q-14 | Bước 6, 9; luồng 6a; Dữ liệu ra 2, Dữ liệu ra 3; BR-15, BR-16 áp dụng cho UC-013 |
| ASM-29 | Mỗi vé đã huỷ có một tin nhắn báo huỷ chuyến gửi tới số điện thoại người đi của vé, gồm mã vé, tuyến, giờ xuất bến, câu báo chuyến đã bị huỷ, số tiền hoàn và hình thức hoàn; tin nhắn không nêu lý do huỷ, nên nhân viên điều hành không phải nhập lý do. | Nguồn chỉ nêu "gửi SMS cho mọi hành khách đã có vé" (Mục 6, câu 4). Người đi cần biết vé nào bị ảnh hưởng và được hoàn bao nhiêu, qua kênh nào; mỗi vé gắn một người đi theo ASM-13. Chờ Q-41 | Bước 10; Dữ liệu ra 2, Dữ liệu ra 3 |
| ASM-30 | Mọi vé, kể cả vé bán tại quầy và vé đặt qua điện thoại đã thanh toán tại quầy, có số điện thoại người đi để nhận tin nhắn báo huỷ chuyến. | REQ-48 đòi gửi SMS cho mọi hành khách đã có vé, việc này cần số điện thoại của người đi trên từng vé; REQ-09 chỉ nêu số điện thoại người đi khi đặt vé trên website. Chờ Q-42 | Bước 10; BR-18; UC-004, UC-005 (dữ liệu vé) |
| ASM-31 | Khi Cổng thanh toán trả về kết quả hoàn tiền không thành công cho một vé, chuyến và vé vẫn ở trạng thái đã huỷ; khoản hoàn của vé được ghi nhận là chưa thành công và mã vé được liệt kê trong kết quả huỷ chuyến để nhà xe xử lý lại. Tin nhắn của vé đó vẫn nêu số tiền hoàn và hình thức hoàn qua cổng thanh toán. | Nguồn không nêu trường hợp hoàn không thành công. Khác UC-008 (ASM-21), chuyến không chạy nên không thể giữ vé còn hiệu lực chờ hoàn lại. Chờ Q-43 | Luồng 8a; bước 11; Dữ liệu ra 3; hậu điều kiện thành công |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-013 | Cột REQ của UC-013 ở Bảng 4b chưa có REQ-09 (số điện thoại người đi nhận tin nhắn), REQ-25 (đặt chỗ qua điện thoại bị huỷ cùng chuyến), REQ-34 và REQ-36 (kênh hoàn tiền theo ASM-28), REQ-42 (chuyến xác định bằng tuyến và giờ xuất bến), REQ-58 (vé của chuyến bị huỷ báo "vé đã huỷ" khi soát). | Thêm REQ-09, REQ-25, REQ-34, REQ-36, REQ-42, REQ-58 vào cột REQ của UC-013 ở Bảng 4b và thêm UC-013 vào các dòng tương ứng ở Mục 5. |
| P02 | CAND-43 | Theo ASM-28, vé mua tại quầy của chuyến bị huỷ có khoản hoàn chờ chi tiền mặt tại quầy, nhưng chưa use case nào cho nhân viên bán vé chi khoản này: UC-008 từ chối vé đã huỷ (luồng 2b). | Khi Q-14 được trả lời "Có" hoặc ASM-28 được chấp nhận, xét CAND-43 thành use case của ACT-02 Nhân viên bán vé hoặc luồng thay thế của UC-008, rồi chạy lại P03 và P04 cho use case đó. |
| P04 (UC-002) | UC-002 | UC-002 chưa có luồng khi chuyến bị huỷ trong thời hạn giữ chỗ (ASM-26, Q-44): sau khi UC-013 huỷ chuyến, thanh toán thành công của lần đặt đang giữ chỗ có thể phát hành vé cho chuyến đã huỷ. | Khi chạy lại P04 UC-002, thêm luồng thay thế "chuyến đã bị huỷ" tại bước thanh toán, kết thúc lần đặt và trả chỗ theo ASM-26, sau khi Q-44 được trả lời. |

## Vấn đề còn mở

- Chọn giữa hai quy tắc (C9): F4.2 mục 9 cho viết lặp bằng một bước "Lặp lại bước K-L cho đến khi ...", còn F10.2 đòi mỗi bước luồng chính có đúng một action. Bước lặp không có action tương ứng. Đã dùng dạng "với từng vé" trong bước 6, 7, 8, 9, 10 (F4.2 mục 9 vế sau) để giữ ánh xạ 1-1; sơ đồ không có vòng lặp, kết quả hoàn từng phần (một số vé thành công, một số không) thể hiện bằng luồng 8a với điều kiện "ít nhất một vé".
- Luồng 8a không kết thúc use case: chuyến đã huỷ ở bước 5 nên use case vẫn đi tiếp tới bước 11, mục tiêu chỉ đạt một phần với các vé hoàn không thành công. F5.4 chỉ có "Kết thúc use case (thành công)" hoặc "(thất bại)"; đã dùng "Tiếp tục bước 9" và ghi trạng thái chưa thành công vào hậu điều kiện thành công.
- Luồng 5a và 6a: điều kiện (không có vé, không có vé mua trực tuyến) đã biết từ bước 3 (Dữ liệu ra 1), nhưng nhánh phải tách sau bước 5 và bước 6 vì chuyến vẫn phải được huỷ và hình thức hoàn vẫn phải được xác định. Đã đánh số theo bước tách nhánh (5a, 6a).
- Chọn giữa hai quy tắc (C9): F10.5 bắt buộc điền Điểm uốn cho cạnh vượt qua partition khác, còn Conventions C7.1 ghi "-" cho cạnh đi thẳng. E-14 (D-4 --> A-4a) đi thẳng ở y = 760; đã ghi một điểm nằm trên đường thẳng tại ranh giới partition (320,760) để thoả cả hai.
- Chọn giữa hai quy tắc (C9): F10.6 đặt trục rẽ nhánh cách decision 30 về bên phải, nhưng trục đó nằm trong bề ngang action luồng chính kế tiếp (A-3 rộng 180, cùng trục với D-2). Đã đặt trục ở x = 600 (cách mép phải action luồng chính 30) cho E-06, E-07 để giữ quy tắc "cạnh không cắt qua node" (C7.3).
- BR-15, BR-16 dùng lại mã vì nội dung trong sổ không giới hạn ở trả vé, nhưng việc áp dụng cho huỷ chuyến dựa trên ASM-28. Nếu Q-14 được trả lời "Không", bỏ UC-013 khỏi cột UC áp dụng của BR-15, BR-16 trong sổ BR và sửa bước 6, 9, luồng 6a.
- BR-18, BR-19 tách từ REQ-48, REQ-49 mà P00 xếp loại Chức năng, theo tiền lệ BR-09 (từ REQ-17). Phép thử F7.1 thoả: không có phần mềm, nhà xe vẫn phải báo và hoàn tiền cho mọi hành khách có vé của chuyến bị huỷ; kênh SMS là cách thực hiện.
- Cạnh E-06, E-07 dùng chung đoạn dọc x = 600 từ y = 450 tới y = 550; không cạnh nào cắt qua node.
