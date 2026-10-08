# P11a - SCR-02 Tìm và chọn chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-002-book-ticket-online.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-02, UC-002 |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-02 Tìm và chọn chuyến (Search and select trip) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-02 Tìm và chọn chuyến (Search and select trip) |
| UC | UC-002 Đặt vé trực tuyến (Book Ticket Online) |
| Bước UC | 1-3, 2a, 4a (một phần bước 4: kiểm tra chuyến còn chỗ trước khi sang SCR-03) |
| Tác nhân | ACT-01 Hành khách |
| Boundary AC | AC-B-BookTicketForm (requestBooking, selectTrip, showTrips, showNoTripFoundNotice, showNoSeatLeftNotice) |
| Lớp thiết kế (DC) | DC-BookTicketView, DC-BookTicketStore |
| Loại màn hình | Độc lập |
| Đến từ | SCR-01 (E-02, mẫu 1); SCR-04 (E-06, mẫu 1, sau MSG-10 hết thời hạn giữ chỗ, tiêu chí tìm được giữ lại) |
| Đi tới | SCR-03 (E-03, mẫu 4, dữ liệu "Chuyến đã chọn") |

## c) Hình ảnh màn hình

Khung dây ở cửa sổ máy tính (từ 1024 px), sau khi tìm có kết quả. Dữ liệu mẫu theo P04 UC-002 mục 5.

```text
+--------------------------------------------------------------------------------------------------------------+
| [SaoViet Bus]                                             Đặt vé trực tuyến    Trả vé                        |
|--------------------------------------------------------------------------------------------------------------|
| Tìm và chọn chuyến                                                                                           |
|                                                                                                              |
| Điểm đi (bắt buộc)                 Điểm đến (bắt buộc)                Ngày đi (bắt buộc)                     |
| Ví dụ: Hà Nội                      Ví dụ: Lào Cai                     Ví dụ: 03/02/2027                      |
| [ Hà Nội                      v]    [ Lào Cai                     v]    [ 03/02/2027       ] [Chọn ngày]     |
|                                                                                                              |
|                                                                               [ Tìm chuyến ]                 |
|--------------------------------------------------------------------------------------------------------------|
| Các chuyến khớp tiêu chí tìm                                                                                 |
| | Tuyến             | Giờ xuất bến     | Loại xe           | Số chỗ còn trống |    Giá vé |               |  |
| |-------------------|------------------|-------------------|------------------|-----------|---------------|  |
| | Hà Nội - Lào Cai  | 21:00 03/02/2027 | Giường nằm 40 chỗ |               12 | 360.000 đ | [Chọn chuyến] |  |
| | Hà Nội - Lào Cai  | 22:30 03/02/2027 | Giường nằm 40 chỗ |                5 | 360.000 đ | [Chọn chuyến] |  |
+--------------------------------------------------------------------------------------------------------------+
```

Dưới 600 px: ba trường xếp một cột, nút "Tìm chuyến" và nút "Chọn chuyến" rộng 100% (cao 48 px), bảng chuyến chuyển thành danh sách thẻ, mỗi chuyến một thẻ có nhãn cột lặp lại. Trước khi tìm, vùng bảng chuyến không hiển thị. Thông điệp (MSG-04, MSG-05) hiển thị ở vùng thông điệp ngay dưới tiêu đề.

Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Header | Tên hệ thống (liên kết) và menu ACT-01; mục "Đặt vé trực tuyến" đang chọn | Trên cùng, cao 56 px | STT 8, 35, 36, 37 |
| Tiêu đề màn hình | "Tìm và chọn chuyến" (tiêu đề cấp 1) | Dưới header | STT 14 |
| Thông điệp | Banner MSG-04 (không có chuyến), MSG-05 (chuyến hết chỗ), MSG-02, MSG-03; chỉ báo MSG-01 khi xử lý từ 1 giây | Dưới tiêu đề, rộng bằng vùng nội dung | STT 13, 44, 46, 47 |
| Nội dung - tiêu chí tìm | Ba trường Điểm đi, Điểm đến, Ngày đi, một cột trên điện thoại, ba cột từ 1024 px (trường độc lập, không phải form dài nên không vi phạm form một cột) | Đầu vùng nội dung | STT 23, 24, 25, 27, 53 |
| Nội dung - danh sách chuyến | Bảng chuyến khớp (Tuyến, Giờ xuất bến, Loại xe, Số chỗ còn trống, Giá vé) kèm nút "Chọn chuyến" mỗi hàng, sắp theo giờ xuất bến tăng dần | Dưới khối tiêu chí; chỉ hiện sau khi tìm có kết quả | STT 28; UC-002 Dữ liệu ra 1 |
| Hành động | Nút chính "Tìm chuyến" ở cuối khối tiêu chí, căn phải | Cuối khối tiêu chí (STT 12) | Nút "Chọn chuyến" mỗi hàng là nút phụ nằm trong bảng, không phải nút chính |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị ba trường tiêu chí rỗng, ô Điểm đến vô hiệu đến khi chọn điểm đi, ô Ngày đi có gợi ý dd/MM/yyyy; chưa hiển thị danh sách chuyến. Khi đến từ SCR-04 sau MSG-10 thì ba trường mang giá trị tiêu chí đã nhập và tiêu điểm vào Điểm đi | UC-002 bước 1, 9a2; MSG-10; quy định STT 33 |
| 2 | Liên kết "SaoViet Bus" ở header | liên kết | Nhấn | Mở SCR-01 (điều hướng chung, STT 39) | Quy định STT 8, 39 |
| 3 | Mục menu "Đặt vé trực tuyến" (đang chọn) và "Trả vé" | liên kết | Nhấn | Mở màn hình đầu của use case được chọn (SCR-02 hoặc SCR-06) theo mẫu 1 như E-02, E-07; dữ liệu đã nhập trên màn hình hiện tại không được giữ. Mục "Đặt vé trực tuyến" có nền, vạch dưới và thuộc tính trang hiện hành (STT 37) | Quy định STT 35, 36, 37, 38; xem Q-89 |
| 4 | Danh sách "Điểm đi" | danh sách chọn | Chọn | Nạp danh sách Điểm đến gồm các điểm đến của những tuyến có điểm đi đã chọn và bật ô Điểm đến; nếu Điểm đến đang chọn không thuộc danh sách mới thì xoá giá trị đó | UC-002 bước 1, Dữ liệu vào 1 STT 1, 2; BookTicketForm.requestBooking |
| 5 | Danh sách "Điểm đi" | danh sách chọn | Rời trường | Kiểm tra bắt buộc; thiếu thì hiển thị MSG-40 dưới ô | Dữ liệu vào 1 STT 1; MSG-40 |
| 6 | Danh sách "Điểm đến" | danh sách chọn | Chọn | Ghi nhận điểm đến; nếu danh sách chuyến đang hiển thị thì giữ nguyên cho tới khi nhấn Tìm chuyến lần kế tiếp | Dữ liệu vào 1 STT 2 |
| 7 | Danh sách "Điểm đến" | danh sách chọn | Rời trường | Kiểm tra bắt buộc; thiếu thì hiển thị MSG-40 dưới ô | Dữ liệu vào 1 STT 2; MSG-40 |
| 8 | Ô "Ngày đi" | ô nhập | Nhập | Nhận ngày gõ tay theo dd/MM/yyyy, không báo lỗi khi đang gõ | Dữ liệu vào 1 STT 3; quy định STT 27, 32 |
| 9 | Ô "Ngày đi" | ô nhập | Rời trường | Kiểm tra theo thứ tự: bắt buộc (MSG-40) --> định dạng ngày hợp lệ theo lịch (MSG-41) --> không trước ngày hiện tại (MSG-42); hiển thị lỗi đầu tiên dưới ô | Dữ liệu vào 1 STT 3, ASM-15; MSG-40, MSG-41, MSG-42 |
| 10 | Nút "Chọn ngày" | nút | Nhấn | Mở bộ chọn ngày dùng được bằng bàn phím, vô hiệu hoá các ngày trước ngày hiện tại; chọn một ngày thì điền vào ô Ngày đi dạng dd/MM/yyyy | Dữ liệu vào 1 STT 3, ASM-15; quy định STT 27 |
| 11 | Nút chính "Tìm chuyến" | nút chính | Nhấn | Kiểm tra lại cả ba trường theo STT 32; còn lỗi thì hiển thị lỗi tại trường, tiêu điểm vào trường lỗi đầu tiên, không gửi (MSG-40, MSG-41, MSG-42). Hợp lệ thì vô hiệu nút, hiển thị MSG-01 nếu quá 1 giây và gửi yêu cầu đặt vé với tiêu chí. Có chuyến khớp: hiển thị bảng chuyến (bước 2). Không có chuyến khớp: banner MSG-04, giữ tiêu chí, tiêu điểm vào Điểm đi, ở lại màn hình (2a). Lỗi hệ thống: MSG-02; mất kết nối: MSG-03 | UC-002 bước 1, 2, 2a; requestBooking, showTrips, showNoTripFoundNotice; MSG-01, MSG-02, MSG-03, MSG-04, MSG-40, MSG-41, MSG-42 |
| 12 | Phím Enter trong form | ô nhập | Nhập | Enter ở ô Ngày đi kích hoạt nút "Tìm chuyến" | Quy định STT 41 |
| 13 | Bảng chuyến | bảng | Khởi tạo | Sau khi tìm có kết quả: mỗi hàng một chuyến gồm Tuyến, Giờ xuất bến, Loại xe, Số chỗ còn trống, Giá vé; sắp theo giờ xuất bến tăng dần (Thiết kế: dễ so sánh giờ đi); có chú thích bảng "Các chuyến khớp tiêu chí tìm" | UC-002 bước 2, Dữ liệu ra 1 STT 1-5; BR-03, BR-04, BR-05; showTrips |
| 14 | Nút "Chọn chuyến" mỗi hàng | nút (phụ) | Nhấn | Vô hiệu nút, hiển thị MSG-01 nếu quá 1 giây, gửi chuyến đã chọn để lấy sơ đồ chỗ. Chuyến còn chỗ trống: mở SCR-03 theo E-03 truyền "Chuyến đã chọn" (tuyến, giờ xuất bến) và sơ đồ chỗ (bước 4). Chuyến không còn chỗ trống: banner MSG-05, giữ nguyên bảng chuyến, ở lại màn hình (4a). Lỗi hệ thống: MSG-02; mất kết nối: MSG-03 | UC-002 bước 3, 4, 4a; selectTrip, showNoSeatLeftNotice; MSG-01, MSG-02, MSG-03, MSG-05; BR-03 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Điểm đi | - (chọn từ danh sách) | Lựa chọn | Chọn, bắt buộc, mặc định trống, căn trái, chữ #212121 | Là điểm đi của ít nhất một tuyến nhà xe đang khai thác | Từ 12 giá trị trở xuống dùng điều khiển chọn gốc, trên 12 giá trị dùng ô nhập có gợi ý (STT 25); gợi ý "Ví dụ: Hà Nội" | P04 UC-002 mục 5 Dữ liệu vào 1 STT 1; REQ-01, REQ-05 |
| Điểm đến | - (chọn từ danh sách) | Lựa chọn | Chọn, bắt buộc, mặc định trống, vô hiệu đến khi có điểm đi, căn trái | Là điểm đến của ít nhất một tuyến có điểm đi đã chọn | Danh sách phụ thuộc Điểm đi; gợi ý "Ví dụ: Lào Cai" | P04 UC-002 mục 5 Dữ liệu vào 1 STT 2; REQ-05 |
| Ngày đi | 10 (dd/MM/yyyy) | Ngày | Nhập hoặc chọn, bắt buộc, mặc định trống, căn trái | Ngày theo lịch, không trước ngày hiện tại (ASM-15) | Định dạng hiển thị dd/MM/yyyy (STT 15); gợi ý "Ví dụ: 03/02/2027"; bộ chọn ngày vô hiệu ngày đã qua | P04 UC-002 mục 5 Dữ liệu vào 1 STT 3; ASM-15, Q-32 |
| Tuyến (cột bảng) | - (theo tên điểm đi, điểm đến) | Chữ | Hiển thị, căn trái | "<Điểm đi> - <Điểm đến>" | Không đặt giới hạn độ dài, bảng tự xuống dòng | P04 UC-002 mục 5 Dữ liệu ra 1 STT 1; GL-36 |
| Giờ xuất bến (cột bảng) | 16 (HH:mm dd/MM/yyyy) | Ngày, Giờ | Hiển thị, căn trái | Giờ phút HH:mm kèm ngày dd/MM/yyyy | Ví dụ 21:00 03/02/2027 | P04 UC-002 mục 5 Dữ liệu ra 1 STT 2; GL-10, REQ-42 |
| Loại xe (cột bảng) | 17 ("Giường nằm 40 chỗ") | Lựa chọn | Hiển thị, căn trái | Một trong "Giường nằm 40 chỗ" hoặc "Ghế ngồi 29 chỗ" | - | P04 UC-002 mục 5 Dữ liệu ra 1 STT 3; REQ-02 |
| Số chỗ còn trống (cột bảng) | 2 | Số | Hiển thị, căn phải | Số nguyên từ 0 đến số chỗ của loại xe (tối đa 40, REQ-02); bằng 0 thì chuyến hết chỗ | Hiển thị số, không đơn vị thừa (STT 15) | P04 UC-002 mục 5 Dữ liệu ra 1 STT 4; BR-03, ASM-17 |
| Giá vé (cột bảng) | - (theo giá trị tính ở BR-05) | Tiền | Hiển thị, căn phải | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", ví dụ 360.000 đ; giá một vé = giá theo tuyến và loại xe x (1 + mức tăng giá lễ Tết) | Không đặt giới hạn độ dài (nguồn không nêu) | P04 UC-002 mục 5 Dữ liệu ra 1 STT 5; BR-04, BR-05, ASM-12, ASM-17 |

Dữ liệu mẫu trên hình: giá vé 360.000 đ = 300.000 x (1 + 20/100) theo ví dụ tính tiền của P04 UC-002 mục 5 (xe giường nằm 40 chỗ, ngày 03/02/2027 trong khoảng tăng giá Tết); số chỗ còn trống 12 và 5 không vượt 40 chỗ của loại xe.

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Điểm đi | Rời trường; nhấn Tìm chuyến | Bắt buộc: đã chọn một điểm đi. Định dạng, miền giá trị: giá trị lấy từ danh sách nên luôn thuộc tuyến đang khai thác | MSG-40 (Chưa chọn điểm đi. Vui lòng chọn điểm đi.) |
| Điểm đến | Rời trường; nhấn Tìm chuyến | Bắt buộc: đã chọn một điểm đến. Miền giá trị: giá trị lấy từ danh sách theo điểm đi | MSG-40 (Chưa chọn điểm đến. Vui lòng chọn điểm đến.) |
| Ngày đi | Rời trường; nhấn Tìm chuyến | 1. Bắt buộc. 2. Định dạng: đúng dd/MM/yyyy và là ngày có trong lịch. 3. Miền giá trị: không trước ngày hiện tại (ASM-15). 4. Quy tắc nghiệp vụ: không có (chuyến có khớp hay không do hệ thống xác định ở bước 2, MSG-04) | 1: MSG-40; 2: MSG-41; 3: MSG-42; 4: MSG-04 |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-02 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 44, 46: MSG-01 khi tìm hoặc chọn chuyến quá 1 giây; số lượng chuyến khớp thấy ngay trong bảng | Không có |
| SCR-02 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng hiển thị theo P04 mục 5, thuật ngữ theo P05 | Không có |
| SCR-02 | Nielsen: 3 Người dùng kiểm soát và tự do | Đạt | STT 39, 42, 65: Quay lại của trình duyệt, tên hệ thống về điều hướng; thao tác tìm không đổi dữ liệu | Không có |
| SCR-02 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 11, 12, 35, 38: vị trí nút, tên nút, menu giống các màn hình web khác | Không có |
| SCR-02 | Nielsen: 5 Ngăn lỗi | Vi phạm đã sửa | Bản nháp để ô Điểm đến nhập tự do và nút Chọn chuyến mỗi hàng là nút chính; điểm đến sai tuyến và nhiều nút chính cùng màn hình | Sửa: Điểm đến chọn từ danh sách phụ thuộc điểm đi (STT 25), nút Chọn chuyến là nút phụ (STT 20, 21) |
| SCR-02 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | STT 25, 29, 53: chọn thay cho gõ, sơ đồ chỗ có chú giải, gợi ý định dạng tại trường | Không có |
| SCR-02 | Nielsen: 7 Linh hoạt và hiệu quả | Đạt | STT 41, 27: Enter kích hoạt nút chính, ô ngày nhận gõ tay | Không dùng phím tắt tuỳ biến (STT 40) |
| SCR-02 | Nielsen: 8 Thẩm mỹ và tối giản | Đạt | STT 9, 10: mỗi màn hình chỉ có điều khiển truy được về P04 hoặc trách nhiệm boundary | Không có |
| SCR-02 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | STT 48 đến 52: lỗi đặt cạnh trường hoặc banner, theo mẫu điều gì sai --> làm gì tiếp | Không có |
| SCR-02 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 53, 54: chỉ có gợi ý tại trường; chưa có trang trợ giúp vì nguồn không có tài liệu hướng dẫn | Q-86 (đã mở ở ui-standards.md) |
| SCR-02 | Shneiderman: Nhất quán | Đạt | STT 9, 10, 11, 38 áp dụng nguyên văn | Không có |
| SCR-02 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60: tương phản, nhãn, bàn phím, phóng chữ | Không có |
| SCR-02 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46: mọi thao tác gửi hệ thống đều có phản hồi trạng thái hoặc kết quả | Không có |
| SCR-02 | Shneiderman: Hội thoại có điểm kết thúc rõ | Không áp dụng | Màn hình trung gian của UC-002, hội thoại kết thúc ở SCR-05 | Không có |
| SCR-02 | Shneiderman: Ngăn lỗi | Đạt | STT 25, 27: chọn từ danh sách, bộ chọn ngày vô hiệu ngày đã qua | Không có |
| SCR-02 | Shneiderman: Hoàn tác dễ dàng | Đạt | Thao tác tìm và chọn chuyến chưa thay đổi dữ liệu nên không cần hoàn tác | Không có |
| SCR-02 | Shneiderman: Người dùng làm chủ | Đạt | STT 39, 65: người dùng đổi tiêu chí và tìm lại, quay về điều hướng bất cứ lúc nào | Không có |
| SCR-02 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | STT 25, 53: điểm đến chỉ hiện giá trị hợp lệ, gợi ý định dạng ngày ngay dưới nhãn | Không có |
| SCR-02 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58: màn hình không có hình mang nghĩa; biểu tượng lỗi kèm chữ | Không có |
| SCR-02 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 28, 57: bảng chuyến có chú thích và tiêu đề cột; mỗi trường có nhãn gắn với ô | Không có |
| SCR-02 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19: mọi trạng thái kèm chữ hoặc biểu tượng có nhãn chữ | Không có |
| SCR-02 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 55: mọi cặp màu từ 5,53:1 | Không có |
| SCR-02 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 7, 60: đơn vị rem, chiều cao hộp chứa chữ không cố định | Xác minh trên trang thật khi có bản dựng |
| SCR-02 | WCAG 1.4.10 Reflow | Đạt | STT 1, 5, 60: một cột dưới 1024 px, bảng chuyển thành thẻ dưới 600 px | Không có |
| SCR-02 | WCAG 1.4.11 Tương phản thành phần 3:1 | Đạt | STT 56: viền điều khiển #767676 (4,54:1), viền tiêu điểm 8,66:1 | Không có |
| SCR-02 | WCAG 2.1.1 Bàn phím | Đạt | STT 41 đến 43, 59: mọi điều khiển dùng được bằng bàn phím | Không có |
| SCR-02 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33: thứ tự Tab trùng thứ tự đọc, không dùng tabindex dương | Không có |
| SCR-02 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề cấp 1, nút có tên bằng chữ | Không có |
| SCR-02 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Đạt | STT 34: viền tiêu điểm 3 px #1F4E79 trên ô nhập, danh sách chọn, nút | Không có |
| SCR-02 | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | STT 9: header và vùng hành động không cố định, không che trường đang giữ tiêu điểm | Không có |
| SCR-02 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 59: không thao tác nào cần kéo thả | Không có |
| SCR-02 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | STT 30: vùng bấm 44 x 44 px (48 px trên điện thoại) | Không có |
| SCR-02 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 9, 36, 38, 39: header, menu, vị trí điều hướng giống nhau ở mọi màn hình web của ACT-01 | Không có |
| SCR-02 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng một chức năng dùng cùng tên nút và thuật ngữ | Không có |
| SCR-02 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp lặp lại ở nhiều màn hình | Q-86 |
| SCR-02 | WCAG 3.3.1 Nhận biết lỗi | Đạt | STT 48, 49: lỗi nhập đặt tại trường, lỗi nghiệp vụ ở banner | Không có |
| SCR-02 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | STT 23, 24, 53, 57: nhãn nhìn thấy gắn với ô, đánh dấu (bắt buộc) hoặc (tuỳ chọn), gợi ý định dạng | Không có |
| SCR-02 | WCAG 3.3.3 Gợi ý sửa lỗi | Đạt | STT 51: mọi thông điệp lỗi nêu việc cần làm tiếp | Không có |
| SCR-02 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Không áp dụng | Chưa có thao tác pháp lý hoặc tài chính; thanh toán nằm ở SCR-04 | Không có |
| SCR-02 | WCAG 3.3.7 Không bắt nhập lại | Đạt | STT 52: tiêu chí tìm được giữ khi báo MSG-04, MSG-05 và khi quay lại từ SCR-04 | Không có |
| SCR-02 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-02 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 46: thông điệp trạng thái không cướp tiêu điểm, lỗi đọc ngay | Không có |
| SCR-02 | Nền tảng: Material Design (mức nhấn mạnh nút, một hành động chính) | Đạt | STT 11, 20, 21: một nút chính, nút phụ dạng viền | Không có |
| SCR-02 | Nền tảng: Apple HIG (vùng chạm 44 pt, điều hướng quay lại theo nền tảng) | Đạt | STT 20, 30, 65: nút cao 44 px (điện thoại 48 px), Quay lại theo trình duyệt | Không có |
| SCR-02 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Đạt | STT 23: nhãn đặt trên ô; ba trường độc lập đặt cùng hàng từ 1024 px nhưng dưới 600 px là một cột, placeholder chỉ làm ví dụ định dạng | Không có |
| SCR-02 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Đạt | STT 24: nhãn kết thúc bằng (bắt buộc); cả ba trường đều bắt buộc theo Dữ liệu vào 1 | Không có |
| SCR-02 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Đạt | STT 32: kiểm tra khi rời trường (hàng 5, 7, 9 của bảng chức năng) | Không có |
| SCR-02 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Đạt | STT 48, 52: lỗi dưới ô, MSG-04 và MSG-05 giữ tiêu chí và danh sách | Không có |
| SCR-02 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Đạt | STT 27, 32: ngày gõ tay hoặc chọn bằng bộ chọn | Không có |
| SCR-02 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Đạt | STT 24: chỉ ba trường của Dữ liệu vào 1 | Không có |
| SCR-02 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Không áp dụng | Màn hình không phải bước thanh toán | Không có |

## h) Thông điệp mới cần bổ sung vào danh mục MSG

| MSG | Loại (Lỗi / Cảnh báo / Xác nhận / Thành công / Đang xử lý) | Nội dung hiển thị | Nút và hành động | Nguồn (UC bước, BR) |
|---|---|---|---|---|
| MSG-40 | Lỗi | Chưa {chọn hoặc nhập} {tên trường}. Vui lòng {chọn hoặc nhập} {tên trường}. Ví dụ: Chưa chọn điểm đi. Vui lòng chọn điểm đi. | Đóng thông điệp (dạng lỗi tại trường: hiển thị dưới ô, tiêu điểm vào trường lỗi đầu tiên) | P04 mục 5 cột Bắt buộc là Có; quy định STT 32, 48, 51 |
| MSG-41 | Lỗi | Ngày đi chưa đúng định dạng. Vui lòng nhập ngày theo dạng dd/MM/yyyy, ví dụ 03/02/2027. | Đóng thông điệp, giữ giá trị đã nhập, tiêu điểm vào ô Ngày đi | UC-002 Dữ liệu vào 1 STT 3 (ngày theo lịch), ASM-15 |
| MSG-42 | Lỗi | Ngày đi {dd/MM/yyyy} đã qua. Vui lòng chọn từ ngày {dd/MM/yyyy của ngày hiện tại} trở đi. | Đóng thông điệp, giữ giá trị đã nhập, tiêu điểm vào ô Ngày đi | UC-002 Dữ liệu vào 1 STT 3 (không trước ngày hiện tại), ASM-15 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-89 | Khi hành khách rời màn hình bằng menu, tên hệ thống hoặc đóng trang trong lúc các chỗ đang được giữ (SCR-03, SCR-04), lần đặt có kết thúc và trả chỗ ngay không? (đã nêu đầy đủ ở SCR-03) | Hành vi của mục menu và liên kết tên hệ thống ở màn hình này; BR-07, BR-08 | P04 UC-002 luồng 9a chỉ nêu hết thời hạn giữ chỗ |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P11a (ui-standards.md) | Mục 2 Danh mục thông điệp | Danh mục dừng ở MSG-39; kiểm tra bắt buộc, định dạng ngày, miền ngày đi của P04 Dữ liệu vào 1 chưa có thông điệp | Bổ sung MSG-40, MSG-41, MSG-42 ở mục h) khi chạy lại giai đoạn 1; các SCR khác dùng MSG-40 |
| P04 | UC-002 Dữ liệu vào 1 | Điều kiện hợp lệ của Điểm đi, Điểm đến, Ngày đi có trong bảng nhưng luồng sự kiện không có bước hay luồng thay thế kiểm tra chúng (đã nêu ở P07 UC-002) | Thêm luồng thay thế cho tiêu chí không hợp lệ ở bước 1 hoặc bỏ cột điều kiện hợp lệ; trước mắt giao diện kiểm tra tại trường theo STT 32 để phản hồi nhanh, kết luận thuộc hệ thống |

## Vấn đề còn mở

- Thông điệp MSG-40 đến MSG-42 mới được đề xuất ở file này vì giai đoạn 1 chưa có thông điệp cho kiểm tra tiêu chí tìm chuyến; mã MSG nối tiếp từ MSG-40 theo ghi chú cuối ui-standards.md. Cần hợp nhất vào ui-standards.md mục 2 khi chạy lại giai đoạn 1.
- Danh sách chuyến và hành vi chọn chuyến phụ thuộc Q-34 (thứ tự báo lỗi khi nhiều vi phạm) chỉ ở SCR-03; ở SCR-02 mỗi trường chỉ hiện một lỗi theo STT 32.
- Nielsen #10 còn mở theo Q-86; Q-89 về việc rời màn hình khi đang giữ chỗ không ảnh hưởng SCR-02 nhưng ảnh hưởng điều hướng menu ở các màn hình sau.
