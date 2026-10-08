# P11a - SCR-03 Chọn chỗ và nhập thông tin người đi - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-002-book-ticket-online.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-03, UC-002 |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-03 Chọn chỗ và nhập thông tin người đi (Select seats and enter traveler info) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-03 Chọn chỗ và nhập thông tin người đi (Select seats and enter traveler info) |
| UC | UC-002 Đặt vé trực tuyến (Book Ticket Online) |
| Bước UC | 4-9, 6a, 6b, 7a, 7b (hiển thị sơ đồ chỗ và nhập ở bước 4-5; kết quả kiểm tra, tính tiền, giữ chỗ ở bước 6-9) |
| Tác nhân | ACT-01 Hành khách |
| Boundary AC | AC-B-BookTicketForm (selectSeatsAndEnterTravelerInfo, showSeatMap, showSeatLimitExceededNotice, showSeatsUnavailableNotice, showMissingTravelerInfoNotice, showInvalidPhoneNotice) |
| Lớp thiết kế (DC) | DC-BookTicketView, DC-BookTicketStore |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-02 (E-03, mẫu 4, dữ liệu "Chuyến đã chọn") |
| Đi tới | SCR-04 (E-04, mẫu 4, dữ liệu "Lần đặt đã giữ chỗ") |

## c) Hình ảnh màn hình

Khung dây ở cửa sổ máy tính (từ 1024 px), đã chọn hai chỗ A05, A06. Chỗ còn trống [ A05 ], không còn trống [xA02x], đã chọn [*A05*]. Dữ liệu mẫu theo P04 UC-002 mục 5. Bố cục lưới chỗ chỉ để minh hoạ (ASM-61, Q-88).

```text
+--------------------------------------------------------------------------------------------------+
| [SaoViet Bus]                                             Đặt vé trực tuyến    Trả vé            |
|--------------------------------------------------------------------------------------------------|
| Chọn chỗ và nhập thông tin người đi                                                              |
|                                                                                                  |
| Chuyến: Hà Nội - Lào Cai, 21:00 03/02/2027, Giường nằm 40 chỗ, giá vé 360.000 đ                  |
|                                                                                                  |
| Sơ đồ chỗ - Còn 12 chỗ trống                                                                     |
| Chú giải: [ A05 ] còn trống   [xA02x] không còn trống   [*A05*] đã chọn                          |
|                                                                                                  |
|   [xA01x] [xA02x] [xA03x] [xA04x] [*A05*]      [xB01x] [xB02x] [ B03 ] [ B04 ] [xB05x]           |
|   [*A06*] [ A07 ] [xA08x] [xA09x] [xA10x]      [xB06x] [xB07x] [ B08 ] [ B09 ] [xB10x]           |
|   [xA11x] [ A12 ] [ A13 ] [xA14x] [xA15x]      [xB11x] [xB12x] [xB13x] [ B14 ] [xB15x]           |
|   [xA16x] [ A17 ] [xA18x] [xA19x] [xA20x]      [xB16x] [xB17x] [ B18 ] [xB19x] [xB20x]           |
|                                                                                                  |
| Đã chọn 2 chỗ. Tối đa 5 chỗ mỗi lần đặt.                                                         |
|--------------------------------------------------------------------------------------------------|
| Người đi - chỗ A05                                                                               |
| Họ tên người đi (bắt buộc)                  Số điện thoại người đi (bắt buộc)                    |
|                                             Ví dụ: 0912345678                                    |
| [ Nguyễn Văn An                         ]   [ 0912345678                      ]                  |
| Người đi - chỗ A06                                                                               |
| Họ tên người đi (bắt buộc)                  Số điện thoại người đi (bắt buộc)                    |
|                                             Ví dụ: 0912345678                                    |
| [ Trần Thị Bình                         ]   [ 0987654321                      ]                  |
|--------------------------------------------------------------------------------------------------|
|                                                               [ Tiếp tục thanh toán ]            |
+--------------------------------------------------------------------------------------------------+
```

Dưới 600 px: lưới chỗ co theo chiều ngang (mỗi nút 44 x 44 px, cách nhau 8 px, có thể cuộn ngang trong vùng sơ đồ chỗ, ngoại lệ STT 60), các khối người đi xếp một cột, họ tên rồi số điện thoại, nút "Tiếp tục thanh toán" rộng 100% cao 48 px.

Thông điệp: MSG-06, MSG-07 hiển thị banner ở vùng thông điệp; MSG-08, MSG-09, MSG-40 hiển thị tại trường; MSG-13 là chỉ báo xử lý. Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Header | Tên hệ thống và menu ACT-01, mục "Đặt vé trực tuyến" đang chọn | Trên cùng, cao 56 px | STT 8, 35, 36, 37 |
| Tiêu đề màn hình | "Chọn chỗ và nhập thông tin người đi" (tiêu đề cấp 1) | Dưới header | STT 14 |
| Thông điệp | Banner MSG-06, MSG-07, MSG-02, MSG-03; chỉ báo MSG-13 và MSG-01 | Dưới tiêu đề | STT 13, 44, 46, 47 |
| Nội dung - chuyến | Tuyến, giờ xuất bến, loại xe, giá vé của chuyến đã chọn (dòng chữ, không nhập) | Đầu vùng nội dung | UC-002 Dữ liệu ra 1 |
| Nội dung - sơ đồ chỗ | Lưới nút chỗ với ba trạng thái, chú giải bằng chữ, dòng "Còn <n> chỗ trống", bộ đếm chỗ đã chọn | Dưới khối chuyến | STT 29; UC-002 Dữ liệu ra 2; GL-31 |
| Nội dung - người đi | Với mỗi chỗ đã chọn một khối "Người đi - chỗ <mã chỗ>" có hai trường họ tên, số điện thoại; form một cột (nhãn trên ô) | Dưới sơ đồ chỗ, theo thứ tự mã chỗ | STT 23, 24, 53; UC-002 Dữ liệu vào 2 |
| Hành động | Nút chính "Tiếp tục thanh toán", căn phải | Cuối vùng nội dung (STT 11) | Không có nút phụ vì P04 không có dịch chuyển quay lại |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị thông tin chuyến đã chọn, sơ đồ chỗ của chuyến với trạng thái từng chỗ, dòng "Còn <n> chỗ trống", bộ đếm "Đã chọn 0 chỗ. Tối đa 5 chỗ mỗi lần đặt."; chưa có khối người đi; tiêu điểm vào tiêu đề màn hình | UC-002 bước 4; showSeatMap; Dữ liệu ra 2; quy định STT 33 |
| 2 | Liên kết "SaoViet Bus" ở header | liên kết | Nhấn | Mở SCR-01 (điều hướng chung, STT 39); lần đặt chưa giữ chỗ nên không có chỗ nào bị giữ | Quy định STT 8, 39 |
| 3 | Mục menu "Đặt vé trực tuyến" (đang chọn) và "Trả vé" | liên kết | Nhấn | Mở màn hình đầu của use case được chọn (SCR-02 hoặc SCR-06) theo mẫu 1 như E-02, E-07; dữ liệu đã nhập trên màn hình hiện tại không được giữ. Mục "Đặt vé trực tuyến" có nền, vạch dưới và thuộc tính trang hiện hành (STT 37) | Quy định STT 35, 36, 37, 38; xem Q-89 |
| 4 | Chỗ còn trống (mỗi chỗ) | nút chọn | Chọn | Bật hoặc bỏ chọn chỗ (dùng chuột, chạm, Space hoặc Enter). Chọn: chỗ đổi sang trạng thái đã chọn, thêm khối "Người đi - chỗ <mã chỗ>" rỗng, tăng bộ đếm. Bỏ chọn: bỏ khối của chỗ đó cùng dữ liệu đã nhập ở khối, giảm bộ đếm. Không chặn chọn chỗ thứ 6, việc từ chối thuộc bước 6 (MSG-06) | UC-002 bước 5, Dữ liệu vào 2 STT 1; BR-01; selectSeatsAndEnterTravelerInfo |
| 5 | Chỗ không còn trống (mỗi chỗ) | nút chọn | Nhấn | Không bấm được (vô hiệu, gạch chéo, nhãn truy cập "<mã chỗ>, không còn trống") | UC-002 bước 4, Dữ liệu ra 2 STT 2; BR-03; quy định STT 29 |
| 6 | Bộ đếm chỗ đã chọn | vùng hiển thị | Chọn | Cập nhật "Đã chọn <n> chỗ. Tối đa 5 chỗ mỗi lần đặt."; khi n lớn hơn 5 chữ chuyển #B3261E kèm biểu tượng lỗi có nhãn chữ, không chặn thao tác | BR-01; quy định STT 19, 53 |
| 7 | Ô "Họ tên người đi" (mỗi chỗ) | ô nhập | Nhập | Nhận họ tên, không báo lỗi khi đang gõ | UC-002 bước 5, Dữ liệu vào 2 STT 2; ASM-13 |
| 8 | Ô "Họ tên người đi" (mỗi chỗ) | ô nhập | Rời trường | Kiểm tra bắt buộc; để trống thì hiển thị MSG-08 (họ tên) dưới ô | Dữ liệu vào 2 STT 2, ASM-15; MSG-08 |
| 9 | Ô "Số điện thoại người đi" (mỗi chỗ) | ô nhập | Nhập | Nhận số điện thoại; trước khi kiểm tra bỏ khoảng trắng, dấu chấm, dấu gạch nối | UC-002 bước 5, Dữ liệu vào 2 STT 3; quy định STT 32 |
| 10 | Ô "Số điện thoại người đi" (mỗi chỗ) | ô nhập | Rời trường | Kiểm tra theo thứ tự: bắt buộc (MSG-08, số điện thoại) --> định dạng 10 chữ số bắt đầu bằng 0 (MSG-09); lỗi hiển thị dưới ô | Dữ liệu vào 2 STT 3, ASM-15; MSG-08, MSG-09 |
| 11 | Nút chính "Tiếp tục thanh toán" | nút chính | Nhấn | Kiểm tra lại mọi trường theo STT 32: chưa chọn chỗ thì MSG-40 ở vùng sơ đồ chỗ; thiếu hoặc sai thông tin người đi thì MSG-08, MSG-09 tại trường, tiêu điểm vào trường lỗi đầu tiên, không gửi. Hợp lệ thì vô hiệu nút, hiển thị MSG-13 và gửi chỗ đã chọn cùng thông tin người đi. Kết quả của hệ thống: quá 5 chỗ thì banner MSG-06 giữ các chỗ đã chọn, ở lại màn hình (6a); có chỗ không còn trống thì banner MSG-07, bỏ chọn các chỗ đó, làm mới sơ đồ chỗ, giữ thông tin người đi của chỗ còn lại (6b); thiếu hoặc sai định dạng thông tin người đi thì MSG-08, MSG-09 (7a, 7b); hợp lệ thì tính giá, tổng tiền, giữ chỗ và mở SCR-04 theo E-04 truyền lần đặt đã giữ chỗ (bước 8, 9). Lỗi hệ thống: MSG-02; mất kết nối: MSG-03 | UC-002 bước 5-9, 6a, 6b, 7a, 7b; selectSeatsAndEnterTravelerInfo, showSeatLimitExceededNotice, showSeatsUnavailableNotice, showMissingTravelerInfoNotice, showInvalidPhoneNotice; BR-01, BR-02, BR-03, BR-06, BR-07; MSG-02, MSG-03, MSG-06, MSG-07, MSG-08, MSG-09, MSG-13, MSG-40 |
| 12 | Phím Enter trong form | ô nhập | Nhập | Enter ở ô họ tên hoặc số điện thoại kích hoạt nút "Tiếp tục thanh toán" | Quy định STT 41 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Tuyến, Giờ xuất bến, Loại xe, Giá vé của chuyến đã chọn | Như SCR-02 mục e | Chữ, Ngày giờ, Lựa chọn, Tiền | Hiển thị, căn trái (giá vé căn phải) | Như SCR-02 mục e; dữ liệu đến từ chuyến đã chọn ở SCR-02 | Không nhập | P04 UC-002 mục 5 Dữ liệu ra 1 STT 1-5 |
| Chỗ (mã chỗ) | - (theo sơ đồ xe) | Chữ | Chọn, căn giữa trong nút, chữ là mã chỗ | Chuỗi mã chỗ theo sơ đồ xe, ví dụ A05; mỗi chỗ thuộc chuyến đã chọn | Độ dài mã không đặt vì nguồn không nêu; nút 44 x 44 px chứa được mã 3 ký tự ở cỡ chữ 16 px | P04 UC-002 mục 5 Dữ liệu ra 2 STT 1; Dữ liệu vào 2 STT 1 |
| Trạng thái chỗ | - (một trong hai giá trị) | Lựa chọn | Hiển thị: còn trống (viền xám, nền trắng), không còn trống (nền #E0E0E0, gạch chéo), thêm trạng thái đã chọn của giao diện (nền #1F4E79, dấu tích) | "Còn trống" hoặc "Không còn trống"; chỉ chỗ còn trống chọn được | Trạng thái đã chọn là trạng thái cục bộ của màn hình, chưa phải trạng thái giữ chỗ | P04 UC-002 mục 5 Dữ liệu ra 2 STT 2; BR-03; GL-03 |
| Chỗ đã chọn | - (từ 1 đến 5 chỗ) | Lựa chọn | Chọn nhiều, bắt buộc, mặc định không chọn chỗ nào | Từ 1 đến 5 chỗ trong một lần đặt; mỗi chỗ thuộc chuyến và còn trống | Hiển thị bằng bộ đếm "Đã chọn <n> chỗ" | P04 UC-002 mục 5 Dữ liệu vào 2 STT 1; BR-01, BR-02, BR-03 |
| Họ tên người đi | 100 | Chữ | Nhập, bắt buộc cho từng chỗ, mặc định trống, căn trái | Không để trống (ASM-15) | Giới hạn 100 ký tự là quyết định thiết kế (C1.7: đủ cho họ tên tiếng Việt thông thường); giới hạn nghiệp vụ chờ Q-32 | P04 UC-002 mục 5 Dữ liệu vào 2 STT 2; ASM-13, ASM-15, Q-32; GL-26 |
| Số điện thoại người đi | 10 | Chữ (chuỗi chữ số) | Nhập, bắt buộc cho từng chỗ, mặc định trống, căn trái, gợi ý "Ví dụ: 0912345678" | Số thuê bao di động Việt Nam gồm 10 chữ số, bắt đầu bằng 0 (ASM-15) | Kiểu chữ vì chữ số 0 đầu phải giữ; chấp nhận nhập kèm khoảng trắng, dấu chấm, dấu gạch nối rồi bỏ đi (STT 32); hiển thị 10 chữ số liền (STT 15) | P04 UC-002 mục 5 Dữ liệu vào 2 STT 3; ASM-13, ASM-15, Q-32 |
| Số chỗ còn trống (dòng tóm tắt) | 2 | Số | Hiển thị, căn trái trong dòng "Còn <n> chỗ trống" | Số nguyên từ 0 đến 40 (REQ-02) | Dùng làm văn bản thay thế của sơ đồ chỗ (STT 29, 58) | P04 UC-002 mục 5 Dữ liệu ra 1 STT 4; BR-03 |

Dữ liệu mẫu trên hình: chuyến Hà Nội - Lào Cai 21:00 03/02/2027, giá vé 360.000 đ; còn 12 chỗ trống trong tổng 40 chỗ (A01 đến A20, B01 đến B20) và đã chọn A05, A06 là hai chỗ còn trống; hai người đi theo P04 UC-002 mục 5 Dữ liệu vào 2. Tổng tiền không hiển thị ở màn hình này vì tổng tiền là kết quả của bước 8 và được hiển thị ở SCR-04.

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Chỗ đã chọn | Nhấn Tiếp tục thanh toán | 1. Bắt buộc: ít nhất một chỗ. 2. Định dạng: không có. 3. Miền giá trị: không quá 5 chỗ (BR-01, hệ thống kiểm tra). 4. Quy tắc nghiệp vụ: mọi chỗ còn trống (BR-02, BR-03, hệ thống kiểm tra) | 1: MSG-40 (Chưa chọn chỗ. Vui lòng chọn chỗ.); 3: MSG-06; 4: MSG-07 |
| Họ tên người đi (mỗi chỗ) | Rời trường; nhấn Tiếp tục thanh toán | 1. Bắt buộc: không để trống. 2-4. Không có | MSG-08 (họ tên) |
| Số điện thoại người đi (mỗi chỗ) | Rời trường; nhấn Tiếp tục thanh toán | 1. Bắt buộc: không để trống. 2. Định dạng: 10 chữ số, bắt đầu bằng 0 sau khi bỏ khoảng trắng, dấu chấm, dấu gạch nối. 3. Miền giá trị: số thuê bao di động Việt Nam theo ASM-15 (không có danh sách đầu số nên chỉ kiểm tra 10 chữ số bắt đầu bằng 0). 4. Không có | 1: MSG-08 (số điện thoại); 2, 3: MSG-09 |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-03 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 44, 46: MSG-13 khi kiểm tra và giữ chỗ; bộ đếm chỗ đã chọn và dòng Còn n chỗ trống cập nhật ngay | Không có |
| SCR-03 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng hiển thị theo P04 mục 5, thuật ngữ theo P05 | Không có |
| SCR-03 | Nielsen: 3 Người dùng kiểm soát và tự do | Đạt | STT 39, 65: Quay lại của trình duyệt về SCR-02; bỏ chọn chỗ bất cứ lúc nào trước khi nhấn Tiếp tục thanh toán | Không có |
| SCR-03 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 11, 12, 35, 38: vị trí nút, tên nút, menu giống các màn hình web khác | Không có |
| SCR-03 | Nielsen: 5 Ngăn lỗi | Đạt | STT 20, 29: chỗ không còn trống không bấm được, nút chính vô hiệu khi xử lý; bộ đếm cảnh báo trước khi gửi | Việc không chặn chọn chỗ thứ 6 là có chủ đích, BR-01 do hệ thống từ chối (MSG-06) |
| SCR-03 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | STT 29, 53: chú giải ba trạng thái, tiêu đề khối nêu mã chỗ, gợi ý số điện thoại | Không có |
| SCR-03 | Nielsen: 7 Linh hoạt và hiệu quả | Đạt | STT 41, 27: Enter kích hoạt nút chính, ô ngày nhận gõ tay | Không dùng phím tắt tuỳ biến (STT 40) |
| SCR-03 | Nielsen: 8 Thẩm mỹ và tối giản | Vi phạm đã sửa | Bản nháp hiển thị tạm tính tổng tiền ngay trên màn hình này; tổng tiền thuộc kết quả bước 8, không có trong Dữ liệu ra của bước 4-5 | Sửa: bỏ tạm tính, tổng tiền chỉ hiển thị ở SCR-04 |
| SCR-03 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | STT 48 đến 52: lỗi đặt cạnh trường hoặc banner, theo mẫu điều gì sai --> làm gì tiếp | Không có |
| SCR-03 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 53, 54: chỉ có gợi ý tại trường; chưa có trang trợ giúp vì nguồn không có tài liệu hướng dẫn | Q-86 (đã mở ở ui-standards.md) |
| SCR-03 | Shneiderman: Nhất quán | Đạt | STT 9, 10, 11, 38 áp dụng nguyên văn | Không có |
| SCR-03 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60: tương phản, nhãn, bàn phím, phóng chữ | Không có |
| SCR-03 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46: mọi thao tác gửi hệ thống đều có phản hồi trạng thái hoặc kết quả | Không có |
| SCR-03 | Shneiderman: Hội thoại có điểm kết thúc rõ | Không áp dụng | Màn hình trung gian, hội thoại kết thúc ở SCR-05 | Không có |
| SCR-03 | Shneiderman: Ngăn lỗi | Đạt | STT 25, 29, 32: chỉ chọn được chỗ còn trống, kiểm tra khi rời trường | Không có |
| SCR-03 | Shneiderman: Hoàn tác dễ dàng | Đạt | Bỏ chọn chỗ hoặc sửa trường trước khi gửi; chưa có thao tác không hoàn tác ở màn hình này | Không có |
| SCR-03 | Shneiderman: Người dùng làm chủ | Đạt | STT 39, 65; người dùng tự chọn và bỏ chọn chỗ, sửa thông tin | Không có |
| SCR-03 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | STT 29, 45, 52: sơ đồ chỗ, thông tin chuyến luôn hiện ở đầu màn hình | Không có |
| SCR-03 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58: mỗi chỗ có tên truy cập nêu mã chỗ và trạng thái, sơ đồ chỗ có dòng tóm tắt bằng chữ | Không có |
| SCR-03 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 28, 57: mỗi khối người đi là một nhóm có tiêu đề nhóm, nhãn gắn với ô | Không có |
| SCR-03 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19, 29: chỗ khác nhau bằng viền, gạch chéo, dấu tích và chú giải bằng chữ | Không có |
| SCR-03 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 55: mọi cặp màu từ 5,53:1 | Không có |
| SCR-03 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 7, 60: đơn vị rem, chiều cao hộp chứa chữ không cố định | Xác minh trên trang thật khi có bản dựng |
| SCR-03 | WCAG 1.4.10 Reflow | Đạt | STT 1, 5, 60: một cột dưới 1024 px; sơ đồ chỗ là ngoại lệ cho phép cuộn ngang | Không có |
| SCR-03 | WCAG 1.4.11 Tương phản thành phần 3:1 | Đạt | STT 56: viền điều khiển #767676 (4,54:1), viền tiêu điểm 8,66:1 | Không có |
| SCR-03 | WCAG 2.1.1 Bàn phím | Đạt | STT 41 đến 43, 59: mọi điều khiển dùng được bằng bàn phím | Không có |
| SCR-03 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33: thứ tự Tab trùng thứ tự đọc, không dùng tabindex dương | Không có |
| SCR-03 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề cấp 1, nút có tên bằng chữ | Không có |
| SCR-03 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Đạt | STT 34: viền tiêu điểm 3 px #1F4E79, không tắt | Không có |
| SCR-03 | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | STT 9: header và vùng hành động không cố định khi cuộn | Không có |
| SCR-03 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 29, 59: chọn chỗ bằng bấm hoặc chạm, không kéo thả | Không có |
| SCR-03 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | STT 30: vùng bấm 44 x 44 px (48 px trên điện thoại) | Không có |
| SCR-03 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 9, 36, 38, 39: header, menu, vị trí điều hướng giống nhau ở mọi màn hình web của ACT-01 | Không có |
| SCR-03 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng một chức năng dùng cùng tên nút và thuật ngữ | Không có |
| SCR-03 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp lặp lại ở nhiều màn hình | Q-86 |
| SCR-03 | WCAG 3.3.1 Nhận biết lỗi | Đạt | STT 48, 49: lỗi nhập đặt tại trường, lỗi nghiệp vụ ở banner | Không có |
| SCR-03 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | STT 23, 24, 53, 57: nhãn nhìn thấy gắn với ô, đánh dấu (bắt buộc) hoặc (tuỳ chọn), gợi ý định dạng | Không có |
| SCR-03 | WCAG 3.3.3 Gợi ý sửa lỗi | Đạt | STT 51: mọi thông điệp lỗi nêu việc cần làm tiếp | Không có |
| SCR-03 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Không áp dụng | Màn hình chưa thực hiện thao tác tài chính; giữ chỗ chưa thu tiền, tổng tiền được xem lại ở SCR-04 | Không có |
| SCR-03 | WCAG 3.3.7 Không bắt nhập lại | Đạt | STT 52: MSG-07 chỉ bỏ chọn chỗ không còn trống, giữ các chỗ còn lại và thông tin người đi | Không có |
| SCR-03 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-03 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 46: thông điệp trạng thái không cướp tiêu điểm, lỗi đọc ngay | Không có |
| SCR-03 | Nền tảng: Material Design (mức nhấn mạnh nút, một hành động chính) | Đạt | STT 11, 20, 21: một nút chính, nút phụ dạng viền | Không có |
| SCR-03 | Nền tảng: Apple HIG (vùng chạm 44 pt, điều hướng quay lại theo nền tảng) | Đạt | STT 20, 30, 65: nút cao 44 px (điện thoại 48 px), Quay lại theo trình duyệt | Không có |
| SCR-03 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Đạt | STT 23: form một cột, nhãn trên ô, placeholder chỉ ví dụ | Không có |
| SCR-03 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Đạt | STT 24: cả hai trường đều có (bắt buộc) | Không có |
| SCR-03 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Đạt | STT 32: kiểm tra khi rời trường (hàng 8, 10 của bảng chức năng) | Không có |
| SCR-03 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Đạt | STT 48, 52: lỗi dưới ô, thông tin người đi được giữ | Không có |
| SCR-03 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Đạt | STT 32: số điện thoại chấp nhận khoảng trắng, dấu chấm, gạch nối | Không có |
| SCR-03 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Đạt | STT 24: chỉ họ tên và số điện thoại cho từng chỗ, đúng Dữ liệu vào 2 | Không có |
| SCR-03 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Không áp dụng | Chưa phải bước thanh toán; tóm tắt đơn và tổng tiền ở SCR-04 | Không có |

## h) Thông điệp mới

Màn hình dùng MSG-40 do SCR-02 đề xuất (chưa chỉnh vào ui-standards.md). Không đề xuất thông điệp mới khác.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-88 | Sơ đồ chỗ của xe có bố cục không gian (tầng, dãy, cột, vị trí cạnh cửa sổ hay lối đi) cần hiển thị, hay chỉ là danh sách mã chỗ kèm trạng thái? (Có bố cục không gian, cần nguồn mô tả bố cục / Chỉ danh sách mã chỗ) | SCR-03 sơ đồ chỗ; ASM-61; P13 (dữ liệu sơ đồ xe) | P04 UC-002 mục 5 Dữ liệu ra 2: chỉ có hai trường "Chỗ" (mã chỗ theo sơ đồ xe) và "Trạng thái chỗ"; GL-31 "Bố trí các chỗ trên xe của một chuyến" không nêu cách bố trí |
| Q-89 | Khi hành khách rời SCR-03 hoặc SCR-04 (dùng menu, tên hệ thống, đóng trang) trong lúc các chỗ đang được giữ, lần đặt có kết thúc và trả chỗ ngay, hay các chỗ vẫn được giữ tới hết 10 phút? (Trả chỗ ngay / Giữ tới hết 10 phút) | SCR-03, SCR-04 (hành vi của menu, liên kết tên hệ thống); BR-07, BR-08; Nielsen #3 | P04 UC-002 luồng 9a chỉ nêu hết thời hạn; hậu điều kiện tối thiểu không nêu trường hợp hành khách bỏ đi giữa chừng |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-61 | Sơ đồ chỗ hiển thị các chỗ của chuyến dạng lưới nút xếp theo thứ tự mã chỗ, nhóm theo chữ cái đầu của mã (ví dụ nhóm A và nhóm B), mỗi chỗ một nút; bố trí vật lý theo sơ đồ xe chờ Q-88 | Nguồn chỉ có mã chỗ và trạng thái; cần một cách hiển thị chọn được, đủ cho 40 chỗ và 29 chỗ của hai loại xe (REQ-02) | SCR-03 vùng sơ đồ chỗ; quy định STT 29 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P11a (ui-standards.md) | Mục 2 Danh mục thông điệp | MSG-40 dùng ở SCR-03 chưa có trong danh mục | Như đề nghị ở SCR-02 mục Đề xuất sửa artifact trước |
| P04 | UC-002 bước 5-6 | Bước 5 cho chọn chỗ và nhập thông tin cùng lúc nhưng P04 không nêu hành vi khi hành khách không chọn chỗ nào mà nhấn tiếp tục | Thêm luồng thay thế hoặc ghi điều kiện chỗ đã chọn tối thiểu 1; trước mắt dùng MSG-40 |

## Vấn đề còn mở

- Q-34 (thứ tự báo lỗi khi nhiều vi phạm): theo STT 32 giao diện kiểm tra bắt buộc và định dạng của từng trường rồi mới gửi hệ thống, nên khi vừa thiếu thông tin người đi vừa chọn quá 5 chỗ thì lỗi thông tin người đi hiện trước MSG-06, khác thứ tự P04 (6a trước 7a); chờ Q-34 để thống nhất.
- Bộ đếm báo vượt 5 chỗ chỉ là cảnh báo; việc từ chối là của hệ thống ở bước 6 (MSG-06). Không chặn chọn chỗ thứ 6 để giữ đúng luồng 6a của P04.
- Hành vi menu và đồng hồ giữ chỗ khi rời màn hình chờ Q-89. Nielsen #10 còn mở theo Q-86.
