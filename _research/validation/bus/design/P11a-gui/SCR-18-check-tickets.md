# P11a - SCR-18 Soát vé - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md; 00-Conventions.md; P01-actors.md 1.0; P02-usecases.md 1.1; P04-uc-specs/UC-015-check-boarding-ticket.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-015-check-boarding-ticket-analysis.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11a-gui/ui-standards.md 1.0; P11a-gui/screen-list.md 1.0; P11a-gui/screen-transition.md 1.0. Tham số: CHE_DO_CHAY = Giai đoạn 2 (các màn hình của UC-002, UC-015); NHAN_DIEN_THUONG_HIEU = Không có; MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không có; THONG_TIN_TAI_LIEU = Không có |
| Phạm vi | SCR-18, UC-015 |

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống bán vé xe khách SaoViet Bus | SCR-18 Soát vé (Check tickets) |  |  |  |  |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-18 Soát vé (Check tickets) |
| UC | UC-015 Soát vé lên xe (Check Boarding Ticket) |
| Bước UC | 2-9, 3a, 5a, 5b, 5c (vòng lặp bước 3-7 và bước 8; bước 9 yêu cầu kết thúc) |
| Tác nhân | ACT-05 Phụ xe (tác nhân phụ ACT-09 Đầu quét mã vạch đưa mã vé vào ô mã vé) |
| Boundary AC | AC-B-CheckBoardingTicketForm (showCheckSessionInfo, enterTicketCode, showValidTicketResult, showInvalidTicketResult, requestEndCheck); AC-B-BarcodeScanner (readBarcode) cung cấp mã vé |
| Lớp thiết kế (DC) | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-17 (E-19, mẫu 4, dữ liệu "Chuyến cần soát") |
| Đi tới | SCR-19 (E-20, mẫu 4, dữ liệu "Kết quả soát vé") |

## c) Hình ảnh màn hình

Khung dây ở màn hình ứng dụng soát vé, hướng dọc 360 x 640 dp, sau khi vé thứ nhất được báo hợp lệ. Dữ liệu mẫu theo P04 UC-015 mục 5.

```text
+----------------------------------------+
| Soát vé                                |
|----------------------------------------|
| [Dấu tích] HỢP LỆ                      |
| Vé SV0000123, chỗ A05                  |
| Nguyễn Văn An                          |
|----------------------------------------|
| Chuyến: Hà Nội - Lào Cai,              |
|         21:00 03/02/2027               |
| Số vé còn hiệu lực: 36                 |
| Số vé đã soát: 1                       |
|                                        |
| Mã vé (bắt buộc)                       |
| Ví dụ: SV0000123                       |
| [                                  ]   |
|                                        |
|----------------------------------------|
| [Kết thúc soát vé]  [Kiểm tra mã vé]   |
+----------------------------------------+
```

Ba kết quả không hợp lệ thay vùng kết quả (nền #B3261E, chữ trắng, biểu tượng dấu chéo, chữ "KHÔNG HỢP LỆ" kèm lý do):

```text
+----------------------------------------+
| [Dấu chéo] KHÔNG HỢP LỆ: vé đã soát    |
| Vé SV0000123, chỗ A05                  |
| Đã soát lúc 20:42 03/02/2027           |
+----------------------------------------+
```

Trạng thái ban đầu của vùng kết quả (chưa quét vé nào): nền #E8EDF3, chữ #1F4E79, dòng "Sẵn sàng quét. Quét mã vạch trên vé hoặc nhập mã vé.". Tệp mockup HTML: không có (XUAT_HTML là Không có).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | "Soát vé" (tiêu đề cấp 1, 20 sp) | Trên cùng, cao 56 dp | STT 10, 14 |
| Kết quả quét | Kết quả lần quét gần nhất: Hợp lệ (nền #1B6E3C) hoặc Không hợp lệ kèm lý do (nền #B3261E), mã vé, chỗ, họ tên người đi hoặc thời điểm soát trước; giữ đến lần quét kế tiếp | Ngay dưới thanh tiêu đề, rộng hết màn hình, cao tối thiểu 160 dp | STT 66; MSG-33 đến MSG-36 |
| Thông điệp | Lỗi tại trường MSG-40; chỉ báo MSG-01; MSG-02 | Dưới vùng kết quả quét | STT 10, 13 |
| Nội dung - thông tin chuyến | Chuyến đang soát, số vé còn hiệu lực, số vé đã soát | Dưới vùng kết quả | UC-015 Dữ liệu ra 1 |
| Nội dung - ô mã vé | Nhãn "Mã vé (bắt buộc)", gợi ý, ô nhập mã vé; luôn giữ tiêu điểm | Cuối vùng nội dung, khoảng đệm đáy 88 dp | STT 23, 53, 67 |
| Hành động | Nút phụ "Kết thúc soát vé" (trái) và nút chính "Kiểm tra mã vé" (phải), mỗi nút cao 48 dp | Vùng hành động cố định ở đáy cao 72 dp | STT 10, 11, 69 |

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
|---|---|---|---|---|---|
| 1 | Màn hình | vùng hiển thị | Khởi tạo | Hiển thị tuyến và giờ xuất bến của chuyến đang soát, số vé còn hiệu lực, số vé đã soát; vùng kết quả quét ở trạng thái sẵn sàng; ô mã vé giữ tiêu điểm, bàn phím ảo không hiện; màn hình không tự tắt trong phiên soát vé | UC-015 bước 2, Dữ liệu ra 1 STT 1-3; showCheckSessionInfo; ASM-33; quy định STT 67, 68 |
| 2 | Ô "Mã vé" | ô nhập | Nhập | Nhận mã vé do đầu quét đưa vào (qua SDK hoặc ký tự bàn phím kèm Enter, tự gửi đi kiểm tra) hoặc do phụ xe gõ tay khi chạm vào ô (vé mua trực tuyến không có mã vạch). Không báo lỗi khi đang gõ | UC-015 bước 3, 4, 3a; Dữ liệu vào 2 STT 1; enterTicketCode, readBarcode; ASM-34; quy định STT 67 |
| 3 | Ô "Mã vé" | ô nhập | Rời trường | Không kiểm tra khi rời trường (ô luôn giữ tiêu điểm cho lần quét kế tiếp); việc kiểm tra thực hiện khi gửi mã | Quy định STT 67; xem Vấn đề còn mở |
| 4 | Ô "Mã vé" | ô nhập | Nhập | Phím Enter gửi mã đang nhập đi kiểm tra như nút "Kiểm tra mã vé" | Quy định STT 41, 67 |
| 5 | Nút chính "Kiểm tra mã vé" | nút chính | Nhấn | Bỏ khoảng trắng, dấu chấm, dấu gạch nối trong mã; mã trống thì MSG-40 dưới ô (không gửi). Mã có nội dung: vô hiệu nút trong lúc kiểm tra, hệ thống kiểm tra vé theo danh sách trên máy (không cần sóng). Vé hợp lệ: ghi nhận đã soát kèm thời điểm soát, vùng kết quả hiển thị MSG-33 nền xanh, tăng "Số vé đã soát" thêm 1, giảm số vé chưa soát tương ứng, máy rung 1 lần ngắn. Vé không hợp lệ: vùng kết quả hiển thị MSG-34 (sai chuyến), MSG-35 (vé đã huỷ) hoặc MSG-36 (vé đã soát) nền đỏ, số liệu không đổi, máy rung 2 lần ngắn. Sau mỗi lần ô mã vé được xoá và lấy lại tiêu điểm; phụ xe quét tiếp (bước 8) | UC-015 bước 5, 6, 7, 8, 3a, 5a, 5b, 5c; checkTicket (qua control), showValidTicketResult, showInvalidTicketResult; BR-20, BR-21, BR-22; ASM-33, ASM-35, ASM-64; MSG-33, MSG-34, MSG-35, MSG-36, MSG-40; quy định STT 66, 67, 68 |
| 6 | Vùng kết quả quét | vùng hiển thị | Khởi tạo | Giữ nguyên kết quả của lần quét gần nhất tới lần quét kế tiếp; kết quả có chữ, biểu tượng có nhãn chữ và màu nền (không chỉ màu) | UC-015 Dữ liệu ra 2 STT 1-6; quy định STT 19, 66 |
| 7 | Nút phụ "Kết thúc soát vé" | nút | Nhấn | Vô hiệu nút, hiển thị MSG-39, gửi kết quả soát vé của chuyến. Gửi được: mở SCR-19 theo E-20 truyền "Kết quả soát vé" với trạng thái "Đã gửi" (bước 10, 11). Máy đang mất sóng: lưu kết quả trên máy chờ tự gửi, mở SCR-19 với trạng thái "Chờ gửi khi có sóng" (10a). Lỗi hệ thống: MSG-02 | UC-015 bước 9, 10, 11, 10a; requestEndCheck, showCheckSummary; REQ-60; MSG-02, MSG-39; ASM-35 |
| 8 | Nút Back của hệ điều hành | nút | Nhấn | Không làm gì; phiên soát vé chỉ kết thúc bằng nút "Kết thúc soát vé" | Quy định STT 69; Q-87 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
|---|---|---|---|---|---|---|
| Mã vé (ô nhập) | - (không đặt giới hạn, chờ Q-90) | Chữ | Nhập, bắt buộc, mặc định trống, căn trái, tiêu điểm tự động | Mã vé hệ thống cấp, chuỗi chữ và số, mỗi chỗ một mã (BR-10); việc mã thuộc chuyến đang soát do hệ thống kiểm tra ở bước 5 | Đầu quét đưa mã vào ô; gợi ý "Ví dụ: SV0000123"; mã không có trong danh sách được báo "Sai chuyến" (Q-45) | P04 UC-015 mục 5 Dữ liệu vào 2 STT 1; BR-10, REQ-23, REQ-19, ASM-34; Q-90 |
| Tuyến và giờ xuất bến | - (theo giá trị) | Chữ | Hiển thị, căn trái | "<Điểm đi> - <Điểm đến>, HH:mm dd/MM/yyyy" | Chuyến đang soát | P04 UC-015 mục 5 Dữ liệu ra 1 STT 1; REQ-42 |
| Số vé còn hiệu lực | 2 | Số | Hiển thị, căn phải | Số nguyên từ 0 đến 40 (xe lớn nhất 40 chỗ, REQ-02, BR-10) | Dữ liệu mẫu: 36 = 38 vé đã phát hành trừ 2 vé đã huỷ | P04 UC-015 mục 5 Dữ liệu ra 1 STT 2; ASM-33; GL-38 |
| Số vé đã soát | 2 | Số | Hiển thị, căn phải | Số nguyên từ 0 đến số vé còn hiệu lực; chỉ tăng khi có vé được báo hợp lệ | Tăng sau mỗi lần quét hợp lệ (ASM-64); lần quét không hợp lệ không đổi (ASM-35) | P04 UC-015 mục 5 Dữ liệu ra 1 STT 3; ASM-35, ASM-64 |
| Kết quả soát | - (một trong hai giá trị) | Lựa chọn | Hiển thị, chữ 28 sp đậm; Hợp lệ nền #1B6E3C, Không hợp lệ nền #B3261E | "Hợp lệ" hoặc "Không hợp lệ" | Kèm biểu tượng dấu tích hoặc dấu chéo có nhãn chữ (STT 66) | P04 UC-015 mục 5 Dữ liệu ra 2 STT 1; REQ-57 |
| Lý do không hợp lệ | - (một trong ba giá trị) | Lựa chọn | Hiển thị, chỉ khi không hợp lệ | "Sai chuyến", "Vé đã huỷ" hoặc "Vé đã soát" | Hiển thị trong nội dung MSG-34, MSG-35, MSG-36 | P04 UC-015 mục 5 Dữ liệu ra 2 STT 2; BR-20, BR-21, BR-22 |
| Mã vé (kết quả) | - (như ô nhập) | Chữ | Hiển thị, căn trái | Mã vé đã nhận ở bước 4 hoặc 3a | - | P04 UC-015 mục 5 Dữ liệu ra 2 STT 3; BR-10 |
| Chỗ | - (theo sơ đồ xe) | Chữ | Hiển thị, căn trái | Mã chỗ của vé; không có khi sai chuyến (5a) | - | P04 UC-015 mục 5 Dữ liệu ra 2 STT 4; ASM-33 |
| Họ tên người đi | 100 | Chữ | Hiển thị, căn trái | Chỉ có ở vé hợp lệ (bước 7) | Giới hạn hiển thị cùng SCR-03 (Q-32); chữ dài tự xuống dòng | P04 UC-015 mục 5 Dữ liệu ra 2 STT 5; ASM-33 |
| Thời điểm soát trước đó | 16 (HH:mm dd/MM/yyyy) | Ngày, Giờ | Hiển thị, căn trái | Chỉ có ở luồng 5c | Ví dụ 20:42 03/02/2027 | P04 UC-015 mục 5 Dữ liệu ra 2 STT 6; ASM-35 |

Dữ liệu mẫu trên hình: số vé còn hiệu lực 36 và số vé đã soát 1 sau lần quét hợp lệ đầu tiên (0 trước lần quét, theo ví dụ P04 UC-015 mục 5); 36 không vượt 40 chỗ của xe giường nằm.

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Mã vé | Khi nhấn Kiểm tra mã vé, nhấn Enter hoặc đầu quét gửi mã (không kiểm tra khi rời trường) | 1. Bắt buộc: không trống sau khi bỏ khoảng trắng, dấu chấm, dấu gạch nối. 2. Định dạng: không kiểm tra ở giao diện vì mã không do hệ thống cấp được báo "Sai chuyến" (Q-45). 3. Miền giá trị: không có. 4. Quy tắc nghiệp vụ do hệ thống kiểm tra: thuộc chuyến, chưa huỷ, chưa soát (BR-20, BR-21, BR-22) | 1: MSG-40 (Chưa nhập mã vé. Vui lòng nhập mã vé.); 4: MSG-34, MSG-35, MSG-36 |

## g) Đánh giá chuẩn (F7)

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-18 | Nielsen: 1 Hiển thị trạng thái hệ thống | Đạt | STT 44, 46, 66: MSG-01 khi xử lý từ 1 giây, kết quả quét chiếm vùng riêng cao tối thiểu 160 dp | Không có |
| SCR-18 | Nielsen: 2 Khớp giữa hệ thống và thế giới thực | Đạt | STT 6, 15, 17: tiếng Việt, định dạng tuyến, giờ, thuật ngữ Chuyến, Mã vé, Phiên soát vé theo P05 | Không có |
| SCR-18 | Nielsen: 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | STT 69: Back của hệ điều hành không có tác dụng; lần quét hợp lệ đã ghi nhận không có hoàn tác theo P04 | Q-87; không tự thêm chức năng |
| SCR-18 | Nielsen: 4 Nhất quán và theo chuẩn | Đạt | STT 10, 11, 12: bố cục vùng, thứ tự nút (phụ trái, chính phải), tên nút là động từ kèm đối tượng | Không có |
| SCR-18 | Nielsen: 5 Ngăn lỗi | Đạt | STT 20, 66, 67: nút vô hiệu khi kiểm tra, kết quả đỏ rõ cho vé sai, ô tự xoá sau mỗi lần gửi tránh gửi trùng | Kết thúc soát vé không có xác nhận theo P04 (STT 62), nút nằm xa ô mã vé (STT 69) |
| SCR-18 | Nielsen: 6 Nhận biết thay vì nhớ lại | Đạt | STT 53, 67: gợi ý định dạng tại trường, tiêu điểm tự về ô mã vé | Không có |
| SCR-18 | Nielsen: 7 Linh hoạt và hiệu quả | Đạt | STT 41, 67: Enter và đầu quét gửi mã, không cần chạm thêm | Không có |
| SCR-18 | Nielsen: 8 Thẩm mỹ và tối giản | Vi phạm đã sửa | Bản nháp thêm danh sách các vé đã soát và nút Xoá lần quét; P04 không có chức năng này | Sửa: bỏ danh sách và nút, chỉ giữ kết quả lần quét gần nhất và hai bộ đếm |
| SCR-18 | Nielsen: 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | STT 48 đến 52, 66: thông điệp theo mẫu điều gì sai --> làm gì tiếp | Không có |
| SCR-18 | Nielsen: 10 Trợ giúp và tài liệu | Vi phạm còn mở | STT 53, 54: chỉ có gợi ý tại trường; chưa có trang trợ giúp | Q-86 (đã mở ở ui-standards.md) |
| SCR-18 | Shneiderman: Nhất quán | Đạt | STT 10, 11, 12 áp dụng nguyên văn | Không có |
| SCR-18 | Shneiderman: Khả dụng cho mọi người dùng | Đạt | STT 55 đến 60, 66: tương phản, nhãn, sp, kết quả có chữ và biểu tượng | Không có |
| SCR-18 | Shneiderman: Phản hồi đầy đủ | Đạt | STT 44, 46, 66, 68: phản hồi bằng chữ, màu, biểu tượng và rung | Không có |
| SCR-18 | Shneiderman: Hội thoại có điểm kết thúc rõ | Không áp dụng | Màn hình trung gian của UC-015; hội thoại kết thúc ở SCR-19 | Không có |
| SCR-18 | Shneiderman: Ngăn lỗi | Đạt | STT 66, 67, 69: ô tự xoá và lấy lại tiêu điểm, Back vô hiệu để không thoát nhầm phiên | Không có |
| SCR-18 | Shneiderman: Hoàn tác dễ dàng | Vi phạm còn mở | Không có hoàn tác cho vé đã ghi nhận đã soát và cho kết thúc soát vé | Q-87; không tự thêm chức năng |
| SCR-18 | Shneiderman: Người dùng làm chủ | Vi phạm còn mở | Back của hệ điều hành bị vô hiệu ở SCR-18 (điểm lệch khỏi hướng dẫn nền tảng) | Q-87 |
| SCR-18 | Shneiderman: Giảm tải trí nhớ ngắn hạn | Đạt | Thông tin chuyến và hai bộ đếm luôn hiện cùng màn hình | Không có |
| SCR-18 | WCAG 1.1.1 Nội dung không phải chữ | Đạt | STT 58, 66: biểu tượng dấu tích và dấu chéo kèm chữ Hợp lệ hoặc Không hợp lệ | Không có |
| SCR-18 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | STT 57: ô mã vé có nhãn nhìn thấy gắn với ô | Không có |
| SCR-18 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | STT 19, 66: kết quả phân biệt bằng chữ Hợp lệ hoặc Không hợp lệ và biểu tượng, không chỉ màu | Không có |
| SCR-18 | WCAG 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1) | Đạt | STT 18, 66: chữ #FFFFFF trên #1B6E3C đạt 6,28:1; trên #B3261E đạt 6,54:1; chữ 28 sp đậm là chữ lớn | Không có |
| SCR-18 | WCAG 1.4.4 Phóng to chữ 200% | Đạt | STT 60: dùng sp, hỗ trợ cỡ chữ hệ thống tới 200% | Xác minh trên máy thật khi có bản dựng |
| SCR-18 | WCAG 1.4.10 Reflow | Không áp dụng | Ứng dụng Android, không phải nội dung web | Dùng sp và cuộn dọc (STT 60) |
| SCR-18 | WCAG 1.4.11 Tương phản thành phần 3:1 | Đạt | STT 56: viền ô nhập #767676 (4,54:1) | Không có |
| SCR-18 | WCAG 2.1.1 Bàn phím | Đạt | STT 41, 67: Enter và đầu quét gửi mã; mọi nút dùng được bằng chạm | Máy chỉ có chạm và đầu quét, không có bàn phím cứng |
| SCR-18 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | STT 33, 67: ô mã vé giữ tiêu điểm khi mở màn hình và sau mỗi lần quét | Không có |
| SCR-18 | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | STT 12, 14, 57: tiêu đề màn hình ở thanh tiêu đề, nút có tên bằng chữ | Không có |
| SCR-18 | WCAG 2.4.7 Tiêu điểm nhìn thấy | Không áp dụng | Thiết bị chỉ dùng cảm ứng và đầu quét; tiêu điểm ô mã vé theo STT 67 | Không có |
| SCR-18 | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | STT 10: khoảng đệm đáy 88 dp để vùng hành động cố định không che ô đang giữ tiêu điểm | Không có |
| SCR-18 | WCAG 2.5.7 Thay thế thao tác kéo | Đạt | STT 59: không thao tác nào cần kéo thả | Không có |
| SCR-18 | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | STT 30: vùng bấm 48 x 48 dp | Không có |
| SCR-18 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | STT 10, 11: vị trí thanh tiêu đề và vùng hành động giống nhau ở ba màn hình | Không có |
| SCR-18 | WCAG 3.2.4 Định danh nhất quán | Đạt | STT 12, 17: cùng thuật ngữ và tên nút | Không có |
| SCR-18 | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | STT 54: chưa có cơ chế trợ giúp | Q-86 |
| SCR-18 | WCAG 3.3.1 Nhận biết lỗi | Đạt | STT 66: không hợp lệ hiển thị bằng chữ, biểu tượng và lý do cụ thể | Không có |
| SCR-18 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | STT 23, 24, 53, 57: nhãn nhìn thấy, (bắt buộc), gợi ý định dạng | Không có |
| SCR-18 | WCAG 3.3.3 Gợi ý sửa lỗi | Đạt | STT 51: thông điệp lỗi nêu việc cần làm tiếp | Không có |
| SCR-18 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Không áp dụng | Không có thao tác tài chính hoặc pháp lý | Không có |
| SCR-18 | WCAG 3.3.7 Không bắt nhập lại | Đạt | STT 52: dữ liệu giữ khi báo lỗi | Không có |
| SCR-18 | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Chưa có use case xác thực trong phạm vi (Q-27 của P02) | Xét lại khi có UC-010 |
| SCR-18 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | STT 46: thông điệp trạng thái không cướp tiêu điểm, lỗi đọc ngay | Không có |
| SCR-18 | Nền tảng: Material Design (vùng chạm 48 dp, một hành động chính, điều hướng Back) | Đạt | STT 10, 11, 20, 30: vùng chạm 48 dp, một nút chính | Không có |
| SCR-18 | Nền tảng: Apple HIG (vùng chạm 44 pt) | Đạt | STT 30: vùng chạm 48 dp lớn hơn 44 pt | Không có |
| SCR-18 | Baymard: Form một cột, nhãn trên ô, không dùng placeholder thay nhãn | Đạt | STT 23: nhãn trên ô, form một trường | Không có |
| SCR-18 | Baymard: Đánh dấu rõ trường bắt buộc và tuỳ chọn | Đạt | STT 24: nhãn có (bắt buộc) | Không có |
| SCR-18 | Baymard: Kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ | Vi phạm còn mở | Ô mã vé không kiểm tra khi rời trường mà kiểm tra khi gửi (STT 67: ô luôn giữ tiêu điểm, đầu quét gửi liên tục) | Ngoại lệ có chủ đích của STT 32 cho ô mã vé; đề nghị ghi ngoại lệ vào STT 32 |
| SCR-18 | Baymard: Giữ dữ liệu đã nhập khi báo lỗi; lỗi đặt cạnh trường và cụ thể | Đạt | STT 48, 52: lỗi dưới ô; mã đã nhập giữ lại khi mã trống thì không có gì để giữ | Không có |
| SCR-18 | Baymard: Chấp nhận nhiều định dạng nhập hợp lý | Đạt | STT 32: bỏ khoảng trắng, dấu chấm, dấu gạch nối trước khi kiểm tra | Không có |
| SCR-18 | Baymard: Giảm số trường tới mức đặc tả yêu cầu | Đạt | STT 24: một trường theo Dữ liệu vào 2 | Không có |
| SCR-18 | Baymard: Hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Không áp dụng | Màn hình không phải bước thanh toán | Không có |

## h) Thông điệp mới

Màn hình dùng MSG-01, MSG-02, MSG-33 đến MSG-36, MSG-39 của ui-standards.md và MSG-40 do SCR-02 đề xuất. Không đề xuất thông điệp mới khác.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-90 | Mã vé do hệ thống cấp có định dạng và độ dài tối đa là bao nhiêu? (đã nêu đầy đủ ở SCR-05) | Ô Mã vé của SCR-18; SCR-05 | P04 UC-015 mục 5 Dữ liệu vào 2 STT 1: chuỗi chữ và số do hệ thống cấp, không nêu độ dài |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-64 | Số vé đã soát trên SCR-18 tăng thêm 1 sau mỗi lần quét được báo hợp lệ (và số vé chưa soát giảm tương ứng); lần quét không hợp lệ không đổi số liệu | P04 chỉ cho hiển thị Số vé đã soát ở bước 2 (giá trị khi bắt đầu) và ở bước 11; nếu số liệu đứng yên suốt phiên thì phụ xe không thấy tiến độ (Nielsen #1). Số liệu cập nhật cùng nguồn Dữ liệu ra 1 STT 3 và ASM-35 | SCR-18 bộ đếm Số vé đã soát; Dữ liệu ra 1 STT 3 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P11a (ui-standards.md) | STT 32 | Ô mã vé của ứng dụng soát vé không kiểm tra khi rời trường | Thêm ngoại lệ cho ô mã vé vào STT 32 khi chạy lại giai đoạn 1 |
| P04 | UC-015 bước 2, Dữ liệu ra 1 | Số vé đã soát chỉ có ở bước 2 và 11, không nêu cập nhật sau mỗi lần quét | Nêu rõ số vé đã soát hiển thị cập nhật sau mỗi vé hợp lệ nếu ASM-64 được chấp nhận |

## Vấn đề còn mở

- Q-90 (độ dài mã vé) ảnh hưởng ô Mã vé; Q-45 quyết định có phân biệt "mã không do hệ thống cấp" khỏi "sai chuyến".
- Mất sóng khi soát không có thông điệp riêng vì kiểm tra dùng danh sách trên máy (UC-015 mục 8); mất sóng chỉ ảnh hưởng bước 10 (MSG-37 ở SCR-19).
- Nielsen #3, Shneiderman hoàn tác và người dùng làm chủ còn mở theo Q-87 (Back bị vô hiệu, không hoàn tác). Nielsen #10 còn mở theo Q-86. Baymard (kiểm tra khi rời trường) ghi còn mở vì ô mã vé là ngoại lệ có chủ đích.
