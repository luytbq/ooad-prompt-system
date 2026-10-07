# P04 - Đặc tả use case UC-002 Đặt vé trực tuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.1; P03-usecase-model.md 1.0 (Mục 1, Mục 2, Câu hỏi mở, Giả định). Chưa có sổ BR và đặc tả P04 nào trước lần chạy này |
| Phạm vi | UC-002 |

Quy ước trích nguồn theo P00: "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-002 |
| Tên use case | Đặt vé trực tuyến (Book Ticket Online) |
| Tác nhân chính | ACT-01 Hành khách |
| Tác nhân phụ | ACT-07 Cổng SMS |
| Mô tả ngắn | Use case này mô tả tương tác giữa hành khách và hệ thống khi hành khách muốn đặt và thanh toán trực tuyến vé cho một hoặc nhiều chỗ trên một chuyến xe khách, không bắt buộc có tài khoản. Kết quả là mỗi chỗ đã chọn có một vé được phát hành với mã vé riêng và người đi nhận được vé qua SMS. |
| Sự kiện kích hoạt | Hành khách muốn đặt vé cho một chuyến (EV-02) |
| Tiền điều kiện | Mỗi tuyến và loại xe của các chuyến đang mở bán đã có giá vé (BR-04). |
| Hậu điều kiện (thành công) | Mỗi chỗ đã chọn có một vé ở trạng thái đã phát hành, mang một mã vé riêng và họ tên, số điện thoại của người đi (BR-10, ASM-13).<br>Các chỗ đã có vé không còn trống trên chuyến (BR-02, BR-03).<br>Khoản thanh toán tổng tiền của lần đặt đã được cổng thanh toán xác nhận (qua UC-003).<br>Vé của từng chỗ đã được gửi tới Cổng SMS để chuyển tới số điện thoại người đi của chỗ đó. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công, không có vé nào được phát hành cho lần đặt và mọi chỗ đã giữ cho lần đặt trở lại trạng thái còn trống (BR-08). |
| Quan hệ | «include» UC-003 Thanh toán vé trực tuyến (tại bước 10) |
| Điểm mở rộng | Không có |
| REQ | REQ-01, REQ-02, REQ-03, REQ-04, REQ-05, REQ-06, REQ-07, REQ-08, REQ-09, REQ-12, REQ-13, REQ-14, REQ-16, REQ-17, REQ-18, REQ-19, REQ-20, REQ-42, REQ-52, REQ-53, REQ-67 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Hành khách | Yêu cầu đặt vé và cung cấp điểm đi, điểm đến, ngày đi (xem Dữ liệu vào 1). |
| 2 | Hệ thống | Hiển thị các chuyến khớp điểm đi, điểm đến và ngày đi (xem Dữ liệu ra 1). |
| 3 | Hành khách | Chọn một chuyến. |
| 4 | Hệ thống | Hiển thị sơ đồ chỗ của chuyến với các chỗ còn trống (BR-03) (xem Dữ liệu ra 2). |
| 5 | Hành khách | Chọn các chỗ muốn đặt và cung cấp họ tên, số điện thoại của người đi cho từng chỗ (xem Dữ liệu vào 2). |
| 6 | Hệ thống | Kiểm tra số chỗ đã chọn không vượt quá giới hạn của một lần đặt (BR-01) và mọi chỗ đã chọn còn trống (BR-02, BR-03). |
| 7 | Hệ thống | Kiểm tra họ tên và số điện thoại người đi đã được cung cấp cho mọi chỗ đã chọn và số điện thoại đúng định dạng (ASM-15). |
| 8 | Hệ thống | Tính giá vé của từng chỗ đã chọn (BR-04, BR-05) và tổng tiền của lần đặt (BR-06). |
| 9 | Hệ thống | Giữ các chỗ đã chọn cho lần đặt và chờ hành khách thanh toán thành công trong thời hạn giữ chỗ (BR-07). |
| 10 | Hệ thống | Gọi use case UC-003 Thanh toán vé trực tuyến để hành khách thanh toán tổng tiền của lần đặt. |
| 11 | Hệ thống | Phát hành vé cho các chỗ đang giữ, mỗi chỗ một vé có một mã vé (BR-09, BR-10). |
| 12 | Hệ thống | Gửi vé của từng chỗ qua SMS tới số điện thoại người đi của chỗ đó qua Cổng SMS (xem Dữ liệu ra 3). |
| 13 | Hệ thống | Hiển thị các vé đã phát hành cho hành khách (xem Dữ liệu ra 4). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Không có chuyến nào khớp điểm đi, điểm đến và ngày đi | Hệ thống | Thông báo không có chuyến phù hợp với tiêu chí đã cung cấp (ASM-16). | Quay lại bước 1 |
| 4a | Chuyến đã chọn không còn chỗ trống nào (BR-03) | Hệ thống | Thông báo chuyến đã hết chỗ trống. | Quay lại bước 3 |
| 6a | Số chỗ đã chọn lớn hơn 5 (BR-01) | Hệ thống | Từ chối yêu cầu đặt vé và thông báo quy tắc bị vi phạm (BR-01). | Quay lại bước 5 |
| 6b | Số chỗ đã chọn không lớn hơn 5 và có ít nhất một chỗ đã chọn không còn trống (BR-03) | Hệ thống | Từ chối yêu cầu đặt vé và thông báo các chỗ không còn trống (BR-02). | Quay lại bước 4 |
| 7a | Thiếu họ tên hoặc số điện thoại người đi của ít nhất một chỗ đã chọn | Hệ thống | Từ chối yêu cầu đặt vé và nhắc hành khách cung cấp đủ họ tên, số điện thoại người đi cho từng chỗ. | Quay lại bước 5 |
| 7b | Thông tin người đi đủ cho mọi chỗ và có ít nhất một số điện thoại không đúng định dạng (ASM-15) | Hệ thống | Từ chối yêu cầu đặt vé và thông báo số điện thoại không đúng định dạng. | Quay lại bước 5 |
| 9a | Hết thời hạn giữ chỗ (BR-07) mà thanh toán chưa thành công | - | Hết thời hạn giữ chỗ | - |
| 9a1 | | Hệ thống | Trả các chỗ đang giữ của lần đặt về trạng thái còn trống cho hành khách khác chọn (BR-08). | |
| 9a2 | | Hệ thống | Thông báo hành khách đã hết thời hạn giữ chỗ và lần đặt vé không thành công. | Kết thúc use case (thất bại) |
| 10a | UC-003 trả kết quả thanh toán không thành công trong thời hạn giữ chỗ (BR-07) | Hệ thống | Thông báo thanh toán không thành công và các chỗ vẫn được giữ tới hết thời hạn giữ chỗ (BR-07, ASM-14). | Quay lại bước 10 |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 1)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Điểm đi | Nơi người đi bắt đầu hành trình | Có | Là điểm đi của ít nhất một tuyến nhà xe đang khai thác (REQ-01, REQ-05) | Hà Nội |
| 2 | Điểm đến | Nơi người đi kết thúc hành trình | Có | Là điểm đến của ít nhất một tuyến có điểm đi đã cung cấp (REQ-05) | Lào Cai |
| 3 | Ngày đi | Ngày xuất bến mong muốn | Có | Ngày theo lịch, không trước ngày hiện tại (ASM-15) | 03/02/2027 |

Dữ liệu vào 2 (bước 5)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Chỗ đã chọn | Các chỗ trên sơ đồ chỗ của chuyến mà hành khách muốn đặt | Có | Từ 1 đến 5 chỗ trong một lần đặt (BR-01); mỗi chỗ thuộc chuyến đã chọn và còn trống (BR-02, BR-03) | A05, A06 |
| 2 | Họ tên người đi | Họ tên của người sẽ đi ở chỗ tương ứng | Có, cho từng chỗ (ASM-13) | Không để trống (ASM-15) | Chỗ A05: Nguyễn Văn An; chỗ A06: Trần Thị Bình |
| 3 | Số điện thoại người đi | Số điện thoại nhận vé qua SMS của người đi ở chỗ tương ứng | Có, cho từng chỗ (ASM-13) | Số thuê bao di động Việt Nam gồm 10 chữ số, bắt đầu bằng 0 (ASM-15) | Chỗ A05: 0912345678; chỗ A06: 0987654321 |

Dữ liệu ra 1 (bước 2)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tuyến | Điểm đi và điểm đến của tuyến của chuyến | "<Điểm đi> - <Điểm đến>" | Hà Nội - Lào Cai |
| 2 | Giờ xuất bến | Thời điểm chuyến rời bến (REQ-42) | Giờ phút dạng HH:mm kèm ngày dạng dd/MM/yyyy | 21:00 03/02/2027 |
| 3 | Loại xe | Loại xe của chuyến (REQ-02) | Chữ: "Giường nằm 40 chỗ" hoặc "Ghế ngồi 29 chỗ" | Giường nằm 40 chỗ |
| 4 | Số chỗ còn trống | Số chỗ của chuyến còn trống (BR-03) (ASM-17) | Số nguyên, căn phải | 12 |
| 5 | Giá vé | Giá một vé của chuyến (BR-04, BR-05) (ASM-17) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 360.000 đ |

Dữ liệu ra 2 (bước 4)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Chỗ | Mã chỗ trên sơ đồ chỗ của xe của chuyến (REQ-02, REQ-06) | Chuỗi mã chỗ theo sơ đồ xe | A05 |
| 2 | Trạng thái chỗ | Chỗ còn trống hay không còn trống (BR-03) | Một trong hai giá trị "Còn trống" / "Không còn trống" | Còn trống |

Dữ liệu ra 3 (bước 12, nội dung SMS gửi cho mỗi chỗ)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Mã vé | Mã của vé đã phát hành cho chỗ (BR-10) | Chuỗi chữ và số do hệ thống cấp, duy nhất trên toàn hệ thống | SV0000123 |
| 2 | Tuyến | Điểm đi và điểm đến (ASM-17) | "<Điểm đi> - <Điểm đến>" | Hà Nội - Lào Cai |
| 3 | Giờ xuất bến | Thời điểm chuyến rời bến (ASM-17) | HH:mm dd/MM/yyyy | 21:00 03/02/2027 |
| 4 | Chỗ | Mã chỗ của vé (ASM-17) | Chuỗi mã chỗ theo sơ đồ xe | A05 |
| 5 | Họ tên người đi | Họ tên ghi trên vé (ASM-17) | Chữ | Nguyễn Văn An |

Dữ liệu ra 4 (bước 13, mỗi vé một dòng, kèm tổng tiền)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Mã vé | Mã của vé đã phát hành (BR-10) | Chuỗi chữ và số do hệ thống cấp | SV0000123 |
| 2 | Chỗ | Mã chỗ của vé | Chuỗi mã chỗ theo sơ đồ xe | A05 |
| 3 | Họ tên người đi | Họ tên người đi của chỗ | Chữ | Nguyễn Văn An |
| 4 | Số điện thoại người đi | Số đã nhận vé qua SMS | 10 chữ số, không dấu phân cách | 0912345678 |
| 5 | Giá vé | Giá vé của chỗ (BR-05) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 360.000 đ |
| 6 | Tuyến và giờ xuất bến | Chuyến của các vé (ASM-17) | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Hà Nội - Lào Cai, 21:00 03/02/2027 |
| 7 | Tổng tiền | Tổng tiền đã thanh toán của lần đặt (BR-06) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 720.000 đ |

Ví dụ tính tiền dùng trong các bảng trên (BR-04, BR-05, BR-06): giá vé tuyến Hà Nội - Lào Cai, xe giường nằm 40 chỗ là 300.000 đ; ngày xuất bến 03/02/2027 nằm trong khoảng ngày tăng giá Tết với mức tăng 20%. Giá một vé = 300.000 x (1 + 20/100) = 360.000 đ. Tổng tiền cho 2 chỗ A05, A06 = 2 x 360.000 = 720.000 đ.

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-01 | Mỗi lần đặt vé trực tuyến được chọn tối đa 5 chỗ. | Ràng buộc | 6, 6a, Dữ liệu vào 2 | REQ-08 | Mới |
| BR-02 | Trên một chuyến, hai vé không được cùng một chỗ. | Ràng buộc | 6, 6b, Dữ liệu vào 2 | REQ-67 | Mới |
| BR-03 | Một chỗ của chuyến là còn trống khi chỗ đó chưa có vé và không đang được giữ cho một lần đặt chưa hết thời hạn giữ chỗ. | Suy luận | 4, 4a, 6, 6b, Dữ liệu ra 1, Dữ liệu ra 2 | REQ-12, REQ-16, REQ-67 | Mới |
| BR-04 | Giá vé được đặt theo tuyến và loại xe. | Sự kiện | Tiền điều kiện, 8, Dữ liệu ra 1 | REQ-52 | Mới |
| BR-05 | Giá một vé bằng giá vé theo tuyến và loại xe của chuyến nhân với (1 + mức tăng giá lễ Tết theo phần trăm) khi ngày xuất bến của chuyến thuộc khoảng ngày có mức tăng giá áp dụng cho chuyến (ASM-12); ngoài khoảng ngày đó, mức tăng bằng 0%. | Tính toán | 8, Dữ liệu ra 1, Dữ liệu ra 4 | REQ-52, REQ-53 | Mới |
| BR-06 | Tổng tiền của một lần đặt vé bằng tổng giá vé của các chỗ đã chọn trong lần đặt đó. | Tính toán | 8, 10, Dữ liệu ra 4 | REQ-12, REQ-14 | Mới |
| BR-07 | Các chỗ đã chọn được giữ chờ thanh toán trực tuyến trong 10 phút kể từ khi bắt đầu giữ. | Ràng buộc | 9, 9a, 10a | REQ-13 | Mới |
| BR-08 | Khi hết thời hạn giữ chỗ (BR-07) mà chưa thanh toán thành công, các chỗ đang giữ của lần đặt được trả lại trạng thái còn trống cho người khác chọn. | Kích hoạt hành động | 9a1 | REQ-16 | Mới |
| BR-09 | Khi thanh toán trực tuyến cho các chỗ đang giữ thành công, hệ thống phát hành vé cho các chỗ đó. | Kích hoạt hành động | 11 | REQ-17 | Mới |
| BR-10 | Mỗi chỗ được phát hành thành đúng một vé có một mã vé. | Ràng buộc | 11, Dữ liệu ra 3, Dữ liệu ra 4 | REQ-18 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Chức năng đặt vé được cung cấp cho hành khách trên website. | Ràng buộc thiết kế (+) | REQ-04 |
| 2 | Vé gửi cho người đi được chuyển tới cổng SMS của nhà mạng qua API REST. | Giao tiếp (+) | REQ-20 |

## 8. Thông tin bổ sung

- Bước 1 đến bước 4 trùng nội dung với UC-001 Tra cứu chuyến xe. P03 không nối include UC-002 --> UC-001 (UC-001 là User-goal, nguồn chỉ mô tả trình tự); khi đặc tả UC-001, các bước tìm chuyến và hiển thị sơ đồ chỗ cần dùng cùng Dữ liệu vào 1, Dữ liệu ra 1, Dữ liệu ra 2 và BR-03.
- UC-003 Thanh toán vé trực tuyến được gọi tại bước 10, khi các chỗ đã được giữ (bước 9) và tổng tiền đã được tính (bước 8, BR-06). Đặc tả UC-003 cần ghi tiền điều kiện là trạng thái này, kết quả thành công dẫn tới bước 11, kết quả thất bại dẫn tới luồng 10a.
- Thời hạn giữ chỗ (BR-07) tiếp tục chạy trong khi UC-003 đang thực hiện; luồng 9a có thể xảy ra khi hành khách đang thanh toán. Trường hợp cổng thanh toán báo thành công sau khi chỗ đã được trả lại chờ Q-10.
- Vé đặt khi hành khách không đăng nhập có xuất hiện trong lịch sử vé của tài khoản cùng số điện thoại hay không chờ Q-06 (UC-011 Xem lịch sử vé).
- Có tiếp tục bán vé trực tuyến cho chuyến sau mốc gửi danh sách hành khách 15 phút trước giờ xuất bến hay không chờ Q-11. Nếu Q-11 được trả lời (b), thêm luồng thay thế tại bước 3 cho chuyến đã qua mốc này.
- Cách phụ xe đọc vé mua trực tuyến (mã vạch, mã QR hay nhập tay mã vé) chờ Q-04; câu trả lời có thể thêm trường vào Dữ liệu ra 3.
- UC-002 là chức năng chịu tải chính của yêu cầu REQ-66 (khoảng 2.000 người truy cập cùng lúc dịp Tết, Q-22); yêu cầu này áp dụng toàn hệ thống nên thuộc P06.

## 8a. Kịch bản chính

- KB1: Luồng chính --> vé được phát hành cho các chỗ đã chọn và gửi qua SMS.
- KB2: Luồng chính + 6b --> chọn lại chỗ còn trống, vé được phát hành.
- KB3: Luồng chính + 10a --> thanh toán lại trong thời hạn giữ chỗ thành công, vé được phát hành.
- KB4: Luồng chính + 9a --> hết thời hạn giữ chỗ, chỗ được trả lại, không có vé nào được phát hành.
- KB5: Luồng chính + 6a + 7b --> sửa số chỗ và số điện thoại, vé được phát hành.

## 9. Activity diagram

File: diagrams/P04-activity-UC-002.drawio (trang "UC-002").

Bảng Node (x, y là toạ độ tương đối trong partition; partition dùng toạ độ tuyệt đối):

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Hành khách | - | - | - | ACT-01 | 0 | 0 | 320 | 2480 |
| P-SYS | Partition | Hệ thống | - | - | - | Chủ ngữ hệ thống mặc định | 320 | 0 | 680 | 2480 |
| INIT | Initial | - | - | P-ACT-01 | - | - | 140 | 60 | 40 | 40 |
| M-1 | Merge | - | - | P-ACT-01 | - | Nhận luồng quay lại từ 2a | 140 | 150 | 40 | 40 |
| A-1 | Action | Yêu cầu đặt vé với tiêu chí tìm chuyến | - | P-ACT-01 | 1 | - | 70 | 230 | 180 | 60 |
| A-2 | Action | Hiển thị các chuyến khớp tiêu chí | - | P-SYS | 2 | - | 70 | 340 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | - | - | 140 | 440 | 40 | 40 |
| A-2a | Action | Thông báo không có chuyến phù hợp | - | P-SYS | 2a | ASM-16 | 330 | 430 | 180 | 60 |
| M-3 | Merge | - | - | P-ACT-01 | - | Nhận luồng quay lại từ 4a | 140 | 520 | 40 | 40 |
| A-3 | Action | Chọn một chuyến | - | P-ACT-01 | 3 | - | 70 | 600 | 180 | 60 |
| M-4 | Merge | - | - | P-SYS | - | Nhận luồng quay lại từ 6b | 140 | 700 | 40 | 40 |
| A-4 | Action | Hiển thị sơ đồ chỗ còn trống | - | P-SYS | 4 | - | 70 | 780 | 180 | 60 |
| D-4 | Decision | - | - | P-SYS | - | - | 140 | 880 | 40 | 40 |
| A-4a | Action | Thông báo chuyến đã hết chỗ trống | - | P-SYS | 4a | - | 330 | 870 | 180 | 60 |
| M-5 | Merge | - | - | P-ACT-01 | - | Nhận luồng quay lại từ 6a, 7a, 7b | 140 | 960 | 40 | 40 |
| A-5 | Action | Chọn chỗ và nhập thông tin người đi | - | P-ACT-01 | 5 | - | 70 | 1040 | 180 | 60 |
| A-6 | Action | Kiểm tra số chỗ và chỗ còn trống | - | P-SYS | 6 | BR-01, BR-02, BR-03 | 70 | 1150 | 180 | 60 |
| D-6 | Decision | - | - | P-SYS | - | - | 140 | 1250 | 40 | 40 |
| A-6a | Action | Từ chối: vượt quá 5 chỗ (BR-01) | - | P-SYS | 6a | - | 330 | 1240 | 180 | 60 |
| A-6b | Action | Từ chối: có chỗ không còn trống (BR-02) | - | P-SYS | 6b | - | 330 | 1340 | 180 | 60 |
| A-7 | Action | Kiểm tra thông tin người đi | - | P-SYS | 7 | ASM-15 | 70 | 1350 | 180 | 60 |
| D-7 | Decision | - | - | P-SYS | - | - | 140 | 1450 | 40 | 40 |
| A-7a | Action | Nhắc cung cấp đủ thông tin người đi | - | P-SYS | 7a | - | 330 | 1440 | 180 | 60 |
| A-7b | Action | Từ chối: số điện thoại sai định dạng | - | P-SYS | 7b | ASM-15 | 330 | 1540 | 180 | 60 |
| A-8 | Action | Tính giá vé và tổng tiền | - | P-SYS | 8 | BR-04, BR-05, BR-06 | 70 | 1530 | 180 | 60 |
| A-9 | Action | Giữ chỗ và chờ thanh toán trong 10 phút | - | P-SYS | 9 | Bắt đầu chờ có hạn giờ (BR-07) | 70 | 1630 | 180 | 60 |
| D-9 | Decision | - | - | P-SYS | - | Hết thời hạn chờ theo F4.2 mục 15 | 140 | 1730 | 40 | 40 |
| A-9a1 | Action | Trả các chỗ đang giữ (BR-08) | - | P-SYS | 9a1 | - | 330 | 1720 | 180 | 60 |
| A-9a2 | Action | Thông báo hết thời hạn giữ chỗ | - | P-SYS | 9a2 | - | 330 | 1820 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thất bại) | 400 | 1920 | 40 | 40 |
| M-10 | Merge | - | - | P-SYS | - | Nhận luồng quay lại từ 10a | 140 | 1810 | 40 | 40 |
| A-10 | CallBehaviorAction | UC-003 Thanh toán vé trực tuyến | - | P-SYS | 10 | «include» RL-27 | 70 | 1890 | 180 | 60 |
| D-10 | Decision | - | - | P-SYS | - | - | 140 | 2010 | 40 | 40 |
| A-10a | Action | Thông báo thanh toán không thành công | - | P-SYS | 10a | ASM-14 | 330 | 2000 | 180 | 60 |
| A-11 | Action | Phát hành vé, mỗi chỗ một mã vé | - | P-SYS | 11 | BR-09, BR-10 | 70 | 2100 | 180 | 60 |
| A-12 | Action | Gửi vé qua SMS qua Cổng SMS | - | P-SYS | 12 | ACT-07 nhận, không có partition | 70 | 2200 | 180 | 60 |
| A-13 | Action | Hiển thị các vé đã phát hành | - | P-SYS | 13 | - | 70 | 2300 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | Kết thúc use case (thành công) | 140 | 2400 | 40 | 40 |

Bảng Edge (Điểm uốn là toạ độ tuyệt đối):

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | M-1 | ControlFlow | - | - | - |
| E-02 | M-1 | A-1 | ControlFlow | - | - | - |
| E-03 | A-1 | A-2 | ControlFlow | - | Sang partition hệ thống | (160,310); (480,310) |
| E-04 | A-2 | D-2 | ControlFlow | - | - | - |
| E-05 | D-2 | A-2a | ControlFlow | [không có chuyến khớp] | Luồng 2a | - |
| E-06 | A-2a | M-1 | ControlFlow | - | Quay lại bước 1 | (860,460); (860,170) |
| E-07 | D-2 | M-3 | ControlFlow | [có chuyến khớp] | Luồng chính | (480,500); (160,500) |
| E-08 | M-3 | A-3 | ControlFlow | - | - | - |
| E-09 | A-3 | M-4 | ControlFlow | - | Sang partition hệ thống | (160,680); (480,680) |
| E-10 | M-4 | A-4 | ControlFlow | - | - | - |
| E-11 | A-4 | D-4 | ControlFlow | - | - | - |
| E-12 | D-4 | A-4a | ControlFlow | [chuyến hết chỗ trống] | Luồng 4a | - |
| E-13 | A-4a | M-3 | ControlFlow | - | Quay lại bước 3 | (880,900); (880,540) |
| E-14 | D-4 | M-5 | ControlFlow | [còn chỗ trống] | Luồng chính | (480,940); (160,940) |
| E-15 | M-5 | A-5 | ControlFlow | - | - | - |
| E-16 | A-5 | A-6 | ControlFlow | - | Sang partition hệ thống | (160,1120); (480,1120) |
| E-17 | A-6 | D-6 | ControlFlow | - | - | - |
| E-18 | D-6 | A-6a | ControlFlow | [quá 5 chỗ] | Luồng 6a | - |
| E-19 | D-6 | A-6b | ControlFlow | [không quá 5 chỗ, có chỗ không còn trống] | Luồng 6b | (600,1270); (600,1370) |
| E-20 | D-6 | A-7 | ControlFlow | [không quá 5 chỗ, mọi chỗ còn trống] | Luồng chính | - |
| E-21 | A-6a | M-5 | ControlFlow | - | Quay lại bước 5 | (900,1270); (900,980) |
| E-22 | A-6b | M-4 | ControlFlow | - | Quay lại bước 4 | (920,1370); (920,720) |
| E-23 | A-7 | D-7 | ControlFlow | - | - | - |
| E-24 | D-7 | A-7a | ControlFlow | [thiếu thông tin người đi] | Luồng 7a | - |
| E-25 | D-7 | A-7b | ControlFlow | [đủ thông tin, số điện thoại sai định dạng] | Luồng 7b | (600,1470); (600,1570) |
| E-26 | D-7 | A-8 | ControlFlow | [thông tin người đi hợp lệ] | Luồng chính | - |
| E-27 | A-7a | M-5 | ControlFlow | - | Quay lại bước 5 | (940,1470); (940,980) |
| E-28 | A-7b | M-5 | ControlFlow | - | Quay lại bước 5 | (960,1570); (960,980) |
| E-29 | A-8 | A-9 | ControlFlow | - | - | - |
| E-30 | A-9 | D-9 | ControlFlow | - | - | - |
| E-31 | D-9 | A-9a1 | ControlFlow | [hết 10 phút giữ chỗ] | Luồng 9a | - |
| E-32 | D-9 | M-10 | ControlFlow | [thanh toán trong 10 phút] | Luồng chính | - |
| E-33 | A-9a1 | A-9a2 | ControlFlow | - | - | - |
| E-34 | A-9a2 | FINAL-1 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-35 | M-10 | A-10 | ControlFlow | - | - | - |
| E-36 | A-10 | D-10 | ControlFlow | - | - | - |
| E-37 | D-10 | A-10a | ControlFlow | [UC-003 không thành công] | Luồng 10a | - |
| E-38 | D-10 | A-11 | ControlFlow | [UC-003 thành công] | Luồng chính | - |
| E-39 | A-10a | M-10 | ControlFlow | - | Quay lại bước 10; đi vòng bên trái trục chính để không cắt A-9a2 | (740,2080); (350,2080); (350,1830) |
| E-40 | A-11 | A-12 | ControlFlow | - | - | - |
| E-41 | A-12 | A-13 | ControlFlow | - | - | - |
| E-42 | A-13 | FINAL-2 | ControlFlow | - | Kết thúc use case (thành công) | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a | D-2, A-2a, M-1 |
| 3 | A-3 |
| 4 | A-4 |
| 4a | D-4, A-4a, M-3 |
| 5 | A-5 |
| 6 | A-6 |
| 6a | D-6, A-6a, M-5 |
| 6b | D-6, A-6b, M-4 |
| 7 | A-7 |
| 7a | D-7, A-7a, M-5 |
| 7b | D-7, A-7b, M-5 |
| 8 | A-8 |
| 9 | A-9 |
| 9a | D-9 (guard [hết 10 phút giữ chỗ]) |
| 9a1 | A-9a1 |
| 9a2 | A-9a2, FINAL-1 |
| 10 | A-10 (CallBehaviorAction) |
| 10a | D-10, A-10a, M-10 |
| 11 | A-11 |
| 12 | A-12 |
| 13 | A-13, FINAL-2 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-31 | Khi thanh toán qua cổng thanh toán không thành công mà thời hạn giữ chỗ 10 phút chưa hết, hành khách có được thanh toán lại cho cùng các chỗ đang giữ không? (Có, thanh toán lại tới hết thời hạn / Không, lần đặt kết thúc và trả chỗ ngay) | Luồng 10a; ASM-14; UC-003 (kết quả thất bại trả về UC gọi) | Mục 3, câu 2: "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại cho người khác." (không nói tường minh về thanh toán lại) |
| Q-32 | Điều kiện hợp lệ của dữ liệu đặt vé là gì: số điện thoại người đi chỉ nhận số di động Việt Nam 10 chữ số hay nhận cả số khác; họ tên người đi có giới hạn độ dài, ký tự không; ngày đi được chọn tối đa bao xa so với ngày hiện tại? | Bước 7, luồng 7b; Dữ liệu vào 1, Dữ liệu vào 2; ASM-15 | Mục 2, câu 1: "hành khách nhập họ tên và số điện thoại của người đi" (không nêu điều kiện hợp lệ) |
| Q-33 | Tin nhắn SMS gửi vé và thông tin vé hiển thị cho hành khách sau khi đặt gồm những thông tin nào ngoài mã vé (tuyến, giờ xuất bến, chỗ, họ tên người đi, giá vé)? | Dữ liệu ra 1, Dữ liệu ra 3, Dữ liệu ra 4; ASM-17; liên quan Q-04 | Mục 3, câu 3: "mỗi chỗ một mã vé, gửi qua SMS tới số điện thoại người đi" |
| Q-34 | Khi một yêu cầu đặt vé vi phạm nhiều điều kiện cùng lúc (vừa chọn quá 5 chỗ vừa có chỗ không còn trống; vừa thiếu thông tin người đi vừa có số điện thoại sai định dạng), hệ thống báo điều kiện nào trước, hay báo tất cả cùng lúc? (Theo thứ tự đang dùng: số chỗ trước chỗ trống, thiếu thông tin trước sai định dạng / Báo tất cả cùng lúc) | Luồng 6a, 6b, 7a, 7b | Nguồn không nêu thứ tự ưu tiên; thứ tự đang dùng theo vị trí xuất hiện: Mục 1, câu 2 ("tối đa 5 chỗ") trước Mục 10, câu 2 ("Không được để hai vé cùng một chỗ") |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-12 | Mức tăng giá lễ Tết áp dụng cho một chuyến khi ngày xuất bến của chuyến thuộc khoảng ngày tăng giá; giá sau khi tăng lấy đúng theo công thức của BR-05, không làm tròn. | Mục 7, câu 2 nêu mức tăng "cho một khoảng ngày" nhưng không nói ngày xuất bến hay ngày mua, cũng không nêu cách làm tròn. Chờ Q-19 | BR-05; bước 8; Dữ liệu ra 1, Dữ liệu ra 4 |
| ASM-13 | Mỗi chỗ trong một lần đặt có họ tên và số điện thoại người đi riêng; vé của mỗi chỗ được gửi qua SMS tới số điện thoại người đi của chỗ đó. | Mục 2, câu 1 và Mục 3, câu 3 nói "người đi" mà không nói một hay nhiều người khi đặt nhiều chỗ; "mỗi chỗ một mã vé, gửi qua SMS tới số điện thoại người đi" gợi ý mỗi vé gắn với một người đi. Chờ Q-08 | Bước 5, 7, 12; luồng 7a; Dữ liệu vào 2; hậu điều kiện thành công |
| ASM-14 | Khi UC-003 trả kết quả thanh toán không thành công trong thời hạn giữ chỗ, các chỗ vẫn được giữ và hành khách được thanh toán lại tới hết thời hạn. | Mục 3, câu 2 chỉ trả chỗ khi "hết 10 phút chưa thanh toán thành công", tức trước mốc đó lần đặt chưa bị huỷ dù thanh toán chưa thành công (P02, mô tả UC-003). Chờ Q-31 | Luồng 10a; M-10, E-39 trên activity diagram |
| ASM-15 | Họ tên người đi không để trống; số điện thoại người đi là số thuê bao di động Việt Nam gồm 10 chữ số, bắt đầu bằng 0; ngày đi không trước ngày hiện tại. | Nguồn không nêu điều kiện hợp lệ của các trường; vé được gửi qua SMS nên số điện thoại phải nhận được tin nhắn. Chờ Q-32 | Bước 7; luồng 7b; Dữ liệu vào 1, Dữ liệu vào 2 |
| ASM-16 | Khi không có chuyến nào khớp điểm đi, điểm đến và ngày đi, hệ thống thông báo và hành khách cung cấp lại tiêu chí. | Nguồn không nêu trường hợp tìm không thấy chuyến; luồng cần điểm quay lại để không dừng ở bước 2 | Luồng 2a |
| ASM-17 | Danh sách chuyến hiển thị số chỗ còn trống và giá vé; SMS gửi vé và thông tin vé hiển thị sau khi đặt gồm mã vé, tuyến, giờ xuất bến, chỗ, họ tên người đi (thông tin hiển thị có thêm giá vé và tổng tiền). | Nguồn chỉ nêu mã vé gửi qua SMS (Mục 3, câu 3) và sơ đồ chỗ còn trống (Mục 1, câu 2); hành khách cần giá để quyết định đặt và cần chuyến, chỗ để đi đúng xe. Chờ Q-33 | Dữ liệu ra 1, Dữ liệu ra 3, Dữ liệu ra 4 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-002 | Bảng 4b cột REQ của UC-002 chưa có REQ-52, REQ-53, trong khi bước 8 phải tính giá vé theo tuyến, loại xe và mức tăng giá lễ Tết để có số tiền thanh toán (BR-04, BR-05). | Thêm REQ-52, REQ-53 vào cột REQ của UC-002 ở Bảng 4b và thêm UC-002 vào hai dòng tương ứng ở Mục 5. |

## Vấn đề còn mở

- Luồng 9a chỉ xử lý hết thời hạn giữ chỗ khi thanh toán chưa thành công. Trường hợp cổng thanh toán báo thành công sau khi chỗ đã được trả lại (Q-10) chưa có luồng: hai phương án của Q-10 đều có thể cần hoàn tiền qua ACT-06 Cổng thanh toán, là tác nhân P02 chưa gán cho UC-002. Không tự đặt giả định để tránh thêm tác nhân; hậu điều kiện tối thiểu chưa nói gì về khoản tiền đã bị trừ trong trường hợp này.
- Activity diagram dùng decision D-9 cho chờ có hạn giờ theo F10.2. Ở UC-002, sự kiện được chờ là kết quả thành công của UC-003 (bước 10), nên D-9 thể hiện lựa chọn trước khi thanh toán diễn ra; luồng quay lại 10a --> M-10 không đi qua D-9 nên sơ đồ không thể hiện việc hết thời hạn trong vòng thanh toán lại. Ngữ nghĩa đầy đủ cần interruptible activity region bao A-10, A-10a, chỉ dùng khi YEU_CAU_BO_SUNG yêu cầu.
- Chọn giữa hai quy tắc (C9): F10.6 đặt trục rẽ nhánh cách decision 30 về bên phải, nhưng với decision 40 rộng và action 180 rộng cùng trục, trục đó nằm trong bề ngang action luồng chính kế tiếp (A-7, A-8) và cạnh tới nhánh thứ hai (6b, 7b) sẽ cắt qua action. Đã đặt trục ở x = 600 (cách mép phải action luồng chính 30) để giữ quy tắc "cạnh không cắt qua node" (C7.3).
- Cạnh E-21, E-27, E-28 cùng vào M-5 từ bên phải nên trùng đoạn ngang cuối ở y = 980. Các cạnh quay lại cắt nhau ở vài điểm (ví dụ E-13 với E-22); không cạnh nào cắt qua node.
