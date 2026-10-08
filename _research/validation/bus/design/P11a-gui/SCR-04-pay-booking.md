# P11a - SCR-04 Thanh toán lần đặt - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-002-book-ticket-online.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-04, UC-002 (phần gọi UC-003 chờ Q-84) |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-04 Thanh toán lần đặt (Pay booking) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-04 Thanh toán lần đặt (Pay booking) |
| UC | UC-002 Đặt vé trực tuyến (phần gọi UC-003 Thanh toán vé trực tuyến, UC-003 chưa có P04 nên chờ Q-84) |
| Bước UC | 9, 10, 9a, 9a2, 10a |
| Tác nhân | ACT-01 Hành khách |
| Boundary AC | AC-B-BookTicketForm (showPaymentFailedNotice, showHoldExpiredNotice) |
| Lớp thiết kế (DC) | DC-BookTicketView, DC-BookTicketStore |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-03 (E-04, mẫu 4, dữ liệu "Lần đặt đã giữ chỗ") |
| Đi tới | SCR-05 (E-05, mẫu 4, dữ liệu "Vé đã phát hành"); SCR-02 (E-06, mẫu 1, sau MSG-10 hết thời hạn giữ chỗ) |

## c) Hình ảnh màn hình

Khung dây ở cửa sổ máy tính (từ 1024 px). Nội dung phần thanh toán chờ Q-84, màn hình chỉ có tóm tắt lần đặt, đồng hồ và nút Thanh toán. Dữ liệu mẫu theo P04 UC-002 mục 5.

```text
+--------------------------------------------------------------------------------------------------+
| [SaoViet Bus]                                             Đặt vé trực tuyến    Trả vé            |
|--------------------------------------------------------------------------------------------------|
| Thanh toán lần đặt                                                                               |
| [i] Thời gian giữ chỗ còn lại: 09:12                                                             |
|--------------------------------------------------------------------------------------------------|
| Chuyến: Hà Nội - Lào Cai, 21:00 03/02/2027                                                       |
| Các chỗ đã giữ cho lần đặt                                                                       |
| | Chỗ   | Họ tên người đi      | Số điện thoại người đi |      Giá vé |                          |
| |-------|----------------------|------------------------|-------------|                          |
| | A05   | Nguyễn Văn An        | 0912345678             |   360.000 đ |                          |
| | A06   | Trần Thị Bình        | 0987654321             |   360.000 đ |                          |
|                                                                                                  |
| Tổng tiền: 720.000 đ                                                                             |
|--------------------------------------------------------------------------------------------------|
|                                                                           [ Thanh toán ]         |
+--------------------------------------------------------------------------------------------------+
```

Khi hết thời hạn giữ chỗ, hộp thông điệp MSG-10 phủ lên màn hình:

```text
+------------------------------------------------------------------------------------+
| Hết thời hạn giữ chỗ                                                               |
| [!] Đã hết 10 phút giữ chỗ nên các chỗ được trả lại và lần đặt vé chưa thành công. |
|     Vui lòng đặt lại nếu vẫn muốn đi.                                              |
|                                                                                    |
|                                                          [ Tìm chuyến khác ]       |
+------------------------------------------------------------------------------------+
```

Dưới 600 px: bảng chỗ chuyển thành danh sách thẻ, mỗi chỗ một thẻ có nhãn cột lặp lại; nút "Thanh toán" rộng 100% cao 48 px; hộp MSG-10 rộng tối đa 480 px. Dòng đồng hồ dưới 1:00 chuyển #B3261E kèm dòng "Sắp hết thời hạn giữ chỗ" (STT 45). Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Header | Tên hệ thống và menu ACT-01, mục "Đặt vé trực tuyến" đang chọn | Trên cùng, cao 56 px | STT 8, 35, 36, 37 |
| Tiêu đề màn hình | "Thanh toán lần đặt" (tiêu đề cấp 1) | Dưới header | STT 14 |
| Thông điệp | Đồng hồ "Thời gian giữ chỗ còn lại: mm:ss"; banner MSG-11; chỉ báo MSG-14; MSG-02, MSG-03 | Dưới tiêu đề | STT 13, 45, 46, 47; MSG-14 thay MSG-01 vì có thông điệp riêng |
| Nội dung - chuyến và chỗ | Tuyến và giờ xuất bến; bảng chỗ đã giữ gồm Chỗ, Họ tên người đi, Số điện thoại người đi, Giá vé | Đầu vùng nội dung | STT 28; ASM-62 |
| Nội dung - tổng tiền | Dòng "Tổng tiền: <số tiền>" căn phải | Dưới bảng chỗ | BR-06; Baymard: tóm tắt đơn và tổng tiền |
| Hành động | Nút chính "Thanh toán", căn phải | Cuối vùng nội dung (STT 11) | Nội dung thanh toán thêm (chuyển trang cổng hay form nhúng) chờ Q-84 |
| Hộp thoại | Hộp thông điệp MSG-10 với nút "Tìm chuyến khác" | Giữa cửa sổ, rộng tối đa 480 px, nền mờ phủ phần còn lại | STT 13, 47 |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị chuyến, bảng chỗ đã giữ kèm họ tên, số điện thoại người đi và giá vé từng chỗ, tổng tiền, đồng hồ giữ chỗ bắt đầu từ thời điểm giữ chỗ (10:00 tại lúc giữ); tiêu điểm vào tiêu đề màn hình | UC-002 bước 8, 9; BR-05, BR-06, BR-07; ASM-62; quy định STT 33, 45 |
| 2 | Liên kết "SaoViet Bus" ở header | liên kết | Nhấn | Mở SCR-01 (điều hướng chung, STT 39) | Quy định STT 8, 39 |
| 3 | Mục menu "Đặt vé trực tuyến" (đang chọn) và "Trả vé" | liên kết | Nhấn | Mở màn hình đầu của use case được chọn (SCR-02 hoặc SCR-06) theo mẫu 1 như E-02, E-07; dữ liệu đã nhập trên màn hình hiện tại không được giữ. Mục "Đặt vé trực tuyến" có nền, vạch dưới và thuộc tính trang hiện hành (STT 37) | Quy định STT 35, 36, 37, 38; xem Q-89 |
| 4 | Đồng hồ giữ chỗ | vùng hiển thị | Khởi tạo | Đếm ngược từ 10:00 mỗi giây; trình đọc màn hình chỉ báo lại ở các mốc 5:00, 2:00, 1:00, 0:30; dưới 1:00 đổi màu chữ #B3261E kèm dòng "Sắp hết thời hạn giữ chỗ". Khi về 00:00 mà thanh toán chưa thành công thì mở hộp thông điệp MSG-10 | UC-002 bước 9, 9a, 9a2; BR-07, BR-08; quy định STT 45; MSG-10 |
| 5 | Bảng chỗ đã giữ | bảng | Khởi tạo | Mỗi hàng một chỗ: Chỗ, Họ tên người đi, Số điện thoại người đi, Giá vé; sắp theo mã chỗ; có chú thích bảng "Các chỗ đã giữ cho lần đặt" | UC-002 bước 5, 8; Dữ liệu vào 2; BR-05; ASM-62 |
| 6 | Dòng Tổng tiền | vùng hiển thị | Khởi tạo | Hiển thị tổng giá vé của các chỗ (BR-06), định dạng tiền STT 15 | UC-002 bước 8; BR-06; ASM-62 |
| 7 | Nút chính "Thanh toán" | nút chính | Nhấn | Vô hiệu nút, hiển thị MSG-14 và thực hiện thanh toán tổng tiền của lần đặt qua UC-003 (cách hiển thị chuyển trang cổng hay form nhúng chờ Q-84). Thanh toán thành công trong thời hạn giữ chỗ: hệ thống phát hành vé, gửi SMS và mở SCR-05 theo E-05 truyền "Vé đã phát hành", thay thế mục lịch sử trình duyệt (bước 11-13). Không thành công khi chưa hết thời hạn: banner MSG-11, nút Thanh toán bật lại, ở lại màn hình, đồng hồ tiếp tục (10a). Hết thời hạn giữ chỗ khi thanh toán chưa thành công: mở hộp MSG-10 (9a). Lỗi hệ thống: MSG-02; mất kết nối: MSG-03 | UC-002 bước 10, 11-13, 10a, 9a; showPaymentFailedNotice, showHoldExpiredNotice; MSG-02, MSG-03, MSG-10, MSG-11, MSG-14; BR-07; ASM-14, Q-31, Q-84 |
| 8 | Hộp thông điệp MSG-10 | vùng hiển thị | Khởi tạo | Mở khi hết thời hạn giữ chỗ: tiêu đề "Hết thời hạn giữ chỗ", nội dung MSG-10, nền mờ phủ màn hình, tiêu điểm vào nút "Tìm chuyến khác"; Tab không ra ngoài hộp. Esc không có tác dụng vì hộp chỉ có một lối ra | UC-002 bước 9a1, 9a2; BR-08; MSG-10; quy định STT 13, 33, 42, 47 |
| 9 | Nút "Tìm chuyến khác" trong hộp MSG-10 | nút chính | Nhấn | Đóng hộp, mở SCR-02 theo E-06 (mẫu 1) với tiêu chí tìm đã nhập được giữ lại | UC-002 bước 9a2; MSG-10; quy định STT 47 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Tuyến và giờ xuất bến | - (theo giá trị) | Chữ | Hiển thị, căn trái | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Ví dụ Hà Nội - Lào Cai, 21:00 03/02/2027 | P04 UC-002 mục 5 Dữ liệu ra 4 STT 6; ASM-17 |
| Chỗ | - (theo sơ đồ xe) | Chữ | Hiển thị, căn trái | Mã chỗ theo sơ đồ xe, ví dụ A05 | Số hàng bằng số chỗ đã chọn, từ 1 đến 5 (BR-01) | P04 UC-002 mục 5 Dữ liệu vào 2 STT 1; Dữ liệu ra 4 STT 2; BR-01 |
| Họ tên người đi | 100 | Chữ | Hiển thị, căn trái | Họ tên đã nhập ở SCR-03 | Giới hạn 100 ký tự cùng SCR-03 (quyết định thiết kế C1.7, giới hạn nghiệp vụ chờ Q-32) | P04 UC-002 mục 5 Dữ liệu vào 2 STT 2; Dữ liệu ra 4 STT 3; Q-32 |
| Số điện thoại người đi | 10 | Chữ (chuỗi chữ số) | Hiển thị, căn trái | 10 chữ số liền, không dấu phân cách, bắt đầu bằng 0 | - | P04 UC-002 mục 5 Dữ liệu ra 4 STT 4; ASM-15 |
| Giá vé | - (theo giá trị tính ở BR-05) | Tiền | Hiển thị, căn phải | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", ví dụ 360.000 đ | Mỗi chỗ một giá vé bằng giá theo tuyến và loại xe x (1 + mức tăng giá lễ Tết) | P04 UC-002 mục 5 Dữ liệu ra 4 STT 5; BR-04, BR-05 |
| Tổng tiền | - (theo giá trị tính ở BR-06) | Tiền | Hiển thị, căn phải, chữ đậm | Bằng tổng giá vé của các chỗ trong lần đặt; ví dụ 2 x 360.000 = 720.000 đ | Tính ở bước 8, hiển thị trước khi thanh toán (ASM-62) | P04 UC-002 mục 5 Dữ liệu ra 4 STT 7; BR-06 |
| Thời gian giữ chỗ còn lại | 5 (mm:ss) | Giờ | Hiển thị, căn trái, chữ đậm 16 px, màu #212121 (dưới 1:00 là #B3261E) | Từ 10:00 giảm tới 00:00 (BR-07) | Thời hạn 10 phút là giá trị nghiệp vụ của BR-07 | BR-07; quy định STT 45 |

Dữ liệu mẫu trên hình: hai chỗ A05, A06 giống SCR-03; giá vé 360.000 đ mỗi chỗ nên tổng tiền 2 x 360.000 = 720.000 đ khớp P04 UC-002 mục 5; đồng hồ 09:12 nằm trong 10:00.

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình không có trường nhập (nội dung thanh toán chờ Q-84) | - |
| Thời hạn giữ chỗ (kiểm tra của hệ thống khi nhấn Thanh toán) | Nhấn Thanh toán; khi đồng hồ về 00:00 | Quy tắc nghiệp vụ: chưa quá 10 phút kể từ lúc giữ chỗ (BR-07) | MSG-10 |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-04 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 44, 45, 46: đồng hồ giữ chỗ, MSG-14 khi chờ kết quả thanh toán, banner MSG-11 | Không có |
| SCR-04 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng hiển thị theo P04 mục 5, thuật ngữ theo P05 | Không có |
| SCR-04 | Nielsen: 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | Màn hình không có điều khiển huỷ lần đặt hay trả chỗ sớm; STT 39, 65 cho phép rời màn hình nhưng hành vi giữ chỗ khi rời chưa đặc tả | Q-89; Q-87 (không tự thêm chức năng huỷ lần đặt) |
| SCR-04 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 11, 12, 35, 38: vị trí nút, tên nút, menu giống các màn hình web khác | Không có |
| SCR-04 | Nielsen: 5 Ngăn lỗi | Đạt | STT 20, 62: nút Thanh toán vô hiệu khi xử lý, màn hình xem lại chỗ và tổng tiền trước khi thanh toán | Không có |
| SCR-04 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | STT 62: toàn bộ chỗ, người đi, tổng tiền hiển thị lại để quyết định | Không có |
| SCR-04 | Nielsen: 7 Linh hoạt và hiệu quả | Đạt | STT 41: Enter kích hoạt nút đang giữ tiêu điểm | Không có |
| SCR-04 | Nielsen: 8 Thẩm mỹ và tối giản | Đạt | STT 9: chỉ có tóm tắt, đồng hồ và một nút chính | Không có |
| SCR-04 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | STT 49, 51: MSG-10, MSG-11 nêu điều gì sai và làm gì tiếp | Không có |
| SCR-04 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 54: chưa có trang trợ giúp; màn hình không có trường khó | Q-86 |
| SCR-04 | Shneiderman: Nhất quán | Đạt | STT 9, 10, 11, 38 áp dụng nguyên văn | Không có |
| SCR-04 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60: tương phản, nhãn, bàn phím, phóng chữ | Không có |
| SCR-04 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46: mọi thao tác gửi hệ thống đều có phản hồi trạng thái hoặc kết quả | Không có |
| SCR-04 | Shneiderman: Hội thoại có điểm kết thúc rõ | Đạt | MSG-10 kết thúc lần đặt thất bại bằng hộp có lối ra duy nhất về SCR-02; thành công sang SCR-05 | Không có |
| SCR-04 | Shneiderman: Ngăn lỗi | Đạt | STT 62: xem lại tổng tiền trước khi thanh toán (WCAG 3.3.4) | Không có |
| SCR-04 | Shneiderman: Hoàn tác dễ dàng | Vi phạm còn mở | Thanh toán và việc hết thời hạn giữ chỗ không có hoàn tác theo P04; chưa có gia hạn | Q-87; không tự thêm chức năng |
| SCR-04 | Shneiderman: Người dùng làm chủ | Vi phạm còn mở | Hành khách không điều khiển được thời hạn 10 phút (BR-07) | Q-87; bù bằng đồng hồ STT 45 |
| SCR-04 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | STT 45, 62: thông tin cần để thanh toán luôn hiện cùng màn hình | Không có |
| SCR-04 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58: biểu tượng thông điệp kèm chữ; màn hình không có hình khác | Không có |
| SCR-04 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 28: bảng có chú thích và tiêu đề cột | Không có |
| SCR-04 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19, 45: đồng hồ dưới 1:00 đổi màu và kèm dòng chữ Sắp hết thời hạn giữ chỗ | Không có |
| SCR-04 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 55: mọi cặp màu từ 5,53:1 | Không có |
| SCR-04 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 7, 60: đơn vị rem, chiều cao hộp chứa chữ không cố định | Xác minh trên trang thật khi có bản dựng |
| SCR-04 | WCAG 1.4.10 Reflow | Đạt | STT 1, 5, 60: một cột dưới 1024 px, bảng chuyển thành thẻ dưới 600 px | Không có |
| SCR-04 | WCAG 1.4.11 Tương phản thành phần 3:1 | Đạt | STT 56: viền điều khiển #767676 (4,54:1), viền tiêu điểm 8,66:1 | Không có |
| SCR-04 | WCAG 2.1.1 Bàn phím | Đạt | STT 41 đến 43, 59: mọi điều khiển dùng được bằng bàn phím | Không có |
| SCR-04 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33: thứ tự Tab trùng thứ tự đọc, không dùng tabindex dương | Không có |
| SCR-04 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề cấp 1, nút có tên bằng chữ | Không có |
| SCR-04 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Đạt | STT 34: viền tiêu điểm 3 px; trong hộp MSG-10 tiêu điểm ban đầu ở nút Tìm chuyến khác | Không có |
| SCR-04 | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | STT 9, 33: hộp thoại nhốt tiêu điểm, header và vùng hành động không cố định | Không có |
| SCR-04 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 59: không thao tác nào cần kéo thả | Không có |
| SCR-04 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | STT 30: vùng bấm 44 x 44 px (48 px trên điện thoại) | Không có |
| SCR-04 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 9, 36, 38, 39: header, menu, vị trí điều hướng giống nhau ở mọi màn hình web của ACT-01 | Không có |
| SCR-04 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng một chức năng dùng cùng tên nút và thuật ngữ | Không có |
| SCR-04 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp | Q-86 |
| SCR-04 | WCAG 3.3.1 Nhận biết lỗi | Đạt | STT 49: MSG-11 ở banner; MSG-10 ở hộp thông điệp | Không có |
| SCR-04 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Không áp dụng | Không có trường nhập | Không có |
| SCR-04 | WCAG 3.3.3 Gợi ý sửa lỗi | Đạt | STT 51: mọi thông điệp lỗi nêu việc cần làm tiếp | Không có |
| SCR-04 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | STT 62, 63: xem lại chỗ, người đi và tổng tiền trước khi nhấn Thanh toán | Chờ Q-84 cho nội dung thanh toán thêm |
| SCR-04 | WCAG 3.3.7 Không bắt nhập lại | Đạt | Không bắt nhập lại họ tên, số điện thoại đã nhập ở SCR-03 (STT 52) | Không có |
| SCR-04 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-04 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 45, 46: đồng hồ chỉ báo lại ở mốc 5:00, 2:00, 1:00, 0:30; MSG-14 dạng trạng thái, MSG-11 dạng cảnh báo | Không có |
| SCR-04 | Nền tảng: Material Design (mức nhấn mạnh nút, một hành động chính) | Đạt | STT 11, 20, 21: một nút chính, nút phụ dạng viền | Không có |
| SCR-04 | Nền tảng: Apple HIG (vùng chạm 44 pt, điều hướng quay lại theo nền tảng) | Đạt | STT 20, 30, 65: nút cao 44 px (điện thoại 48 px), Quay lại theo trình duyệt | Không có |
| SCR-04 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-04 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-04 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-04 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-04 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-04 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Không áp dụng | Màn hình không có form nhập, giỏ hàng hay thanh toán | Không có |
| SCR-04 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Đạt | Bảng chỗ, giá vé từng chỗ và Tổng tiền hiển thị ở màn hình thanh toán (BR-06) | Chờ Q-84 cho phần thông tin thanh toán |

## h) Thông điệp mới

Không có. Màn hình dùng MSG-02, MSG-03, MSG-10, MSG-11, MSG-14 của ui-standards.md.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-84 | Việc thanh toán của UC-003 diễn ra thế nào trên giao diện, hành khách có phải nhập thêm thông tin thanh toán ngay trên website không? (đã mở ở screen-list.md) | SCR-04 nút Thanh toán, MSG-14; cạnh E-04, E-05 | P04 UC-002 bước 10; UC-003 chưa có P04 |
| Q-89 | Khi hành khách rời màn hình bằng menu, tên hệ thống hoặc đóng trang trong lúc các chỗ đang được giữ (SCR-03, SCR-04), lần đặt có kết thúc và trả chỗ ngay không? (đã nêu đầy đủ ở SCR-03) | Hành vi của mục menu và liên kết tên hệ thống ở màn hình này; BR-07, BR-08 | P04 UC-002 luồng 9a chỉ nêu hết thời hạn giữ chỗ |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-62 | Trước khi thanh toán, SCR-04 cho hành khách xem lại chuyến, từng chỗ kèm họ tên, số điện thoại người đi và giá vé, tổng tiền và thời gian giữ chỗ còn lại; thông tin lấy từ kết quả bước 6-9 vì P04 không có bảng Dữ liệu ra cho các bước này | P04 UC-002 chỉ có Dữ liệu ra 4 ở bước 13; ui-standards.md STT 62 và WCAG 3.3.4 cần xem lại tổng tiền trước khi thanh toán; thông tin này là dữ liệu của chính lần đặt nên không thêm chức năng | SCR-04 mục d, e; BR-05, BR-06 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-002 bước 8-10 | Không có bảng Dữ liệu ra cho nội dung hiển thị trước khi thanh toán (tổng tiền, thời gian giữ chỗ còn lại), nên SCR-04 phải dựa vào ASM-62 | Thêm Dữ liệu ra 2a (hoặc mở rộng bước 9) cho chuyến, chỗ, người đi, giá vé, tổng tiền trước khi thanh toán, và nói rõ thời gian giữ chỗ còn lại có hiển thị không |
| P04 | UC-003 | UC-003 chưa có đặc tả nên phần thanh toán của SCR-04 chưa có căn cứ | Chạy P04, P07 cho UC-003 rồi chạy lại SCR-04 |

## Vấn đề còn mở

- Phần thanh toán thực sự (nhập thông tin, chuyển trang cổng) chưa thiết kế do Q-84; SCR-04 chỉ mô tả phần của UC-002.
- Chọn giữa hai quy tắc (C9): STT 42 của ui-standards.md cho Esc đóng hộp bằng nút phụ, nhưng hộp MSG-10 chỉ có một nút dẫn tới SCR-02 (cạnh E-06 phải xảy ra theo luồng 9a2). Đã cho Esc không tác dụng ở hộp MSG-10 để Esc không kích hoạt nút chính; đề nghị bổ sung ngoại lệ vào STT 42.
- Nielsen #3, Shneiderman hoàn tác, Shneiderman người dùng làm chủ còn mở theo Q-87 và Q-89 (không có huỷ lần đặt, thời hạn 10 phút không gia hạn).
- Nielsen #10 còn mở theo Q-86.
