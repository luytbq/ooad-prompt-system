# P11a - SCR-03 Nhập thông tin người đi - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0); P04-uc-specs/UC-009-book-ticket-online.md (luồng sự kiện, bảng dữ liệu vào ra, BR, Câu hỏi mở, Giả định); P05-glossary.md (GL-08, GL-17, GL-20, GL-21); P06-supplementary-spec.md (NFR-01, NFR-02, BR-03); P07-uc-analysis/UC-009 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng AC-B-BookTicketOnlineForm); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4). Placeholder: CHE_DO_CHAY = Giai đoạn 2: các màn hình của UC-009, UC-017; THIET_BI_HIEN_THI, NHAN_DIEN_THUONG_HIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có, XUAT_HTML = Không, THONG_TIN_TAI_LIEU = Không có, YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét trước lần chạy: Q-69, ASM-51; lần chạy giai đoạn 2 này cấp Q-70 đến Q-72, ASM-52 đến ASM-54 |
| Phạm vi | SCR-03 (UC-009 bước 5, 6, 7, 7a, 5a, 8, 8a, *a) |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 |

## a) Thông tin tài liệu

Không có (THONG_TIN_TAI_LIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có; dùng mẫu F5).

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-03 Nhập thông tin người đi (Enter traveler info) |
| UC | UC-009 Đặt vé trực tuyến |
| Bước UC | 5 (hiển thị kết quả giữ chỗ), 6, 7, 7a, 5a, 8, 8a, *a |
| Tác nhân | ACT-01 Hành khách (không cần tài khoản, NFR-02) |
| Boundary AC | AC-B-BookTicketOnlineForm |
| DC | DC-BookTicketOnlineView (tiếp nhận thao tác: DC-BookTicketOnlineRequestHandler) |
| Loại màn hình | Phụ thuộc có dữ liệu (nhận "Các chỗ đang giữ" từ SCR-02, E-03) |
| Đến từ | SCR-02 (E-03, mẫu 4, "Các chỗ đang giữ") |
| Đi tới | SCR-04 (E-04, mẫu 4, "Các vé đã phát hành", sau khi UC-010 trả thanh toán thành công); SCR-01 (E-06, mẫu 1: đóng MSG-07 hoặc MSG-08, "Huỷ yêu cầu mua vé", menu "Trang chủ"). UC-010 chưa có màn hình nên bước thanh toán nằm trong cạnh E-04 (ASM-49) |
| Hành vi khi rời bằng menu | Mục "Trang chủ" coi là hành khách huỷ yêu cầu mua vé (luồng *a): hệ thống trả lại ngay các chỗ đang giữ (ASM-24) và mở SCR-01 kèm MSG-09 (ASM-53, chờ Q-71) |
| Nền tảng | Website cho hành khách, máy tính từ 1280 x 720 px và điện thoại từ 360 x 640 px (UI-STT 1) |

## c) Hình ảnh màn hình

```text
+------------------------------------------------------------------------+
| SaoViet Bus                                              [ Trang chủ ] |
|------------------------------------------------------------------------|
| Nhập thông tin người đi                                                |
| [ vùng thông điệp: trống; MSG-15 hiện ở đây ]                          |
|                                                                        |
| Chuyến                          Chỗ đang giữ                           |
| Hà Nội - Vinh, 15/12/2026 20:30 A05, A06 (2 chỗ)                       |
|                                                                        |
| Chỗ được giữ đến 20:10 - còn 07:42                                     |
|                                                                        |
| Họ tên người đi (bắt buộc)                                             |
| [ Nguyễn Văn An                                      ]                 |
| Lỗi: Vui lòng nhập họ tên người đi.   (chỉ hiện khi sai, MSG-05)       |
|                                                                        |
| Số điện thoại người đi (bắt buộc)                                      |
| Mã vé sẽ được gửi qua SMS tới số này. Ví dụ: 0912345678                |
| [ 0912345678                         ]                                 |
| Lỗi: Vui lòng nhập số điện thoại người đi. (chỉ hiện khi sai, MSG-06)   |
|------------------------------------------------------------------------|
|              [ Huỷ yêu cầu mua vé ]   [ Tiếp tục thanh toán ]          |
+------------------------------------------------------------------------+
```

Trên điện thoại (dưới 600 px) các nút xếp dọc, "Tiếp tục thanh toán" ở trên (UI-STT 9). Màn hình không có trường thông tin thẻ (NFR-01).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh trên | Tên hệ thống "SaoViet Bus", mục "Trang chủ" | Trên cùng, cao 56 px | UI-STT 7, 34, 35 |
| Tiêu đề | "Nhập thông tin người đi" (tiêu đề cấp 1) | Dưới thanh trên | UI-STT 12 |
| Thông điệp | Banner MSG-15; hộp modal MSG-07, MSG-08, MSG-14 | Banner dưới tiêu đề; hộp modal ở giữa màn hình | UI-STT 11, 47, 48 |
| Nội dung - tóm tắt | Chuyến, chỗ đang giữ, thời hạn giữ chỗ và thời gian còn lại | Đầu vùng nội dung | UI-STT 46; mục chi tiết chỉ đọc theo UI-STT 14 |
| Nội dung - form | Hai ô nhập một cột: họ tên, số điện thoại; nhãn trên ô; gợi ý dưới nhãn; lỗi dưới ô | Dưới tóm tắt | UI-STT 22, 30, 55 |
| Hành động | "Huỷ yêu cầu mua vé" (nút phụ), "Tiếp tục thanh toán" (nút chính) | Cuối nội dung, căn phải, ngăn bằng đường kẻ 1 px | UI-STT 7, 8, 18, 19 |

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Màn hình | Vùng hiển thị | Khởi tạo | Hiển thị tiêu đề cấp 1, vùng tóm tắt và form; tiêu điểm đặt ở ô "Họ tên người đi" (UI-STT 32). Tiêu đề trang trình duyệt là "Nhập thông tin người đi - SaoViet Bus" | UC-009 bước 5, 6; UI-STT 12, 32 |
| 2 | Vùng "Chuyến" và "Chỗ đang giữ" | Vùng hiển thị | Khởi tạo | Hiển thị tuyến, giờ xuất bến và mã các chỗ đang giữ (nhận từ SCR-02), cùng số chỗ | UC-009 bước 5, Dữ liệu vào 1, Dữ liệu ra 1 dòng 2 |
| 3 | Vùng "Thời hạn giữ chỗ" | Vùng hiển thị | Khởi tạo | Hiển thị "Chỗ được giữ đến HH:mm - còn mm:ss"; thời gian còn lại cập nhật mỗi giây cho mắt nhìn | BR-03; GL-21; UI-STT 46 |
| 4 | Vùng "Thời hạn giữ chỗ" | Vùng hiển thị | Hết thời gian | Tại các mốc còn 5 phút, 1 phút, 30 giây: thông báo MSG-16 bằng role status cho trình đọc màn hình, không chiếm tiêu điểm | BR-03; UI-STT 46; MSG-16 |
| 5 | Vùng "Thời hạn giữ chỗ" | Vùng hiển thị | Hết thời gian | Hết thời hạn giữ chỗ mà thanh toán chưa thành công: hệ thống đã trả lại các chỗ (luồng 5a); hiển thị hộp modal MSG-08 (hết hạn có thể xảy ra ở bước 6 đến 8, kể cả lúc đang xử lý thanh toán) | UC-009 luồng 5a; BR-03; MSG-08 |
| 6 | Ô "Họ tên người đi" | Ô nhập | Nhập | Nhận họ tên, tối đa 100 ký tự (ASM-52); không báo lỗi khi đang gõ | UC-009 bước 6, Dữ liệu vào 2 STT 1; ASM-52; UI-STT 28 |
| 7 | Ô "Họ tên người đi" | Ô nhập | Rời trường | Kiểm tra bắt buộc: để trống thì hiển thị MSG-05 ngay dưới ô, viền ô đỏ; hợp lệ thì xoá lỗi. Điều kiện hợp lệ khác chưa quy định (Q-44) | UC-009 bước 7, 7a; MSG-05; Q-44; UI-STT 28, 30 |
| 8 | Ô "Số điện thoại người đi" | Ô nhập | Nhập | Nhận số điện thoại, tối đa 20 ký tự gồm cả khoảng trắng, dấu chấm, dấu gạch ngang; gợi bàn phím số trên điện thoại | UC-009 bước 6, Dữ liệu vào 2 STT 2; ASM-52; UI-STT 22, 31 |
| 9 | Ô "Số điện thoại người đi" | Ô nhập | Rời trường | Bỏ khoảng trắng, dấu chấm, dấu gạch ngang trước khi kiểm tra; để trống thì hiển thị MSG-06 ngay dưới ô; điều kiện hợp lệ khác chưa quy định (Q-44) | UC-009 bước 7, 7a; MSG-06; Q-44; UI-STT 28, 31 |
| 10 | Nút "Tiếp tục thanh toán" | Nút chính | Nhấn | Kiểm tra lại cả hai ô. Một ô lỗi: hiển thị MSG-05 hoặc MSG-06 tại ô và đưa tiêu điểm tới ô đó. Cả hai ô lỗi: hiển thị banner MSG-15 và đưa tiêu điểm tới ô lỗi đầu tiên. Hợp lệ: vô hiệu cả hai nút, hiện MSG-13 sau 1 giây, hệ thống ghi thông tin người đi (bước 7) rồi gọi UC-010 (chưa có màn hình, ASM-49). Thanh toán thành công --> phát hành vé, gửi SMS và mở SCR-04 (E-04). Thanh toán thất bại --> hộp modal MSG-07 (luồng 8a). Hết thời hạn giữ chỗ --> hộp modal MSG-08 (luồng 5a). Lỗi hệ thống --> hộp modal MSG-14, ở lại SCR-03 | UC-009 bước 6 đến 12, 5a, 7a, 8a; MSG-05, MSG-06, MSG-07, MSG-08, MSG-13, MSG-14, MSG-15; UI-STT 21, 44, 53, 54 |
| 11 | Nút "Huỷ yêu cầu mua vé" | Nút phụ | Nhấn | Huỷ yêu cầu mua vé (luồng *a): hệ thống trả lại ngay các chỗ đang giữ (ASM-24), mở SCR-01 và hiển thị MSG-09 (E-06). Nút bị vô hiệu từ khi hợp lệ và bắt đầu thanh toán, vì luồng *a chỉ áp dụng trước bước 8 | UC-009 bước *a; ASM-24; MSG-09; UI-STT 44 |
| 12 | Mục "Trang chủ" ở thanh trên | Liên kết | Nhấn | Xử lý như "Huỷ yêu cầu mua vé" (mục 11): trả lại ngay các chỗ đang giữ, mở SCR-01 kèm MSG-09 (ASM-53, chờ Q-71). Mục bị vô hiệu khi đang xử lý thanh toán | ASM-53; UC-009 bước *a; UI-STT 34, 37 |
| 13 | Hộp thông điệp MSG-07 | Nút | Nhấn | Nút "Về trang chủ" (cũng là Esc): đóng hộp và mở SCR-01 (E-06); use case kết thúc thất bại, các chỗ đã được trả lại | UC-009 bước 8a; MSG-07; UI-STT 49 |
| 14 | Hộp thông điệp MSG-08 | Nút | Nhấn | Nút "Về trang chủ" (cũng là Esc): đóng hộp và mở SCR-01 (E-06) | UC-009 bước 5a; MSG-08; UI-STT 49 |
| 15 | Hộp thông điệp MSG-14 | Nút | Nhấn | Nút "Đóng": đóng hộp, ở lại SCR-03, giữ nguyên họ tên, số điện thoại và thời hạn giữ chỗ vẫn tiếp tục đếm | UI-STT 52, 53; MSG-14 |
| 16 | Banner MSG-15 | Nút | Nhấn | Nút đóng "x": đóng banner; banner cũng mất khi hành khách sửa xong và gửi lại | UI-STT 48, 54 |

## e) Định nghĩa thuộc tính trường

| Mục | Số ký tự tối đa | Kiểu | Thuộc tính trường | Ràng buộc dữ liệu | Ghi chú | Nguồn |
|---|---|---|---|---|---|---|
| Họ tên người đi | 100 | Chữ | Nhập; bắt buộc; mặc định trống; căn trái; chữ #1F2933 16 px, viền #6B7280 | Chỉ cần đã nhập; điều kiện hợp lệ khác chưa quy định (Q-44). Một họ tên chung cho cả lần đặt (ASM-19) | Gợi ý "Ví dụ: Nguyễn Văn An". Độ dài tối đa 100 là giả định ASM-52 | P04 UC-009 Dữ liệu vào 2 STT 1, bước 7, 7a; GL-17; ASM-19, ASM-52; Q-44 |
| Số điện thoại người đi | 20 | Chữ | Nhập; bắt buộc; mặc định trống; căn trái; chữ #1F2933 16 px, viền #6B7280 | Chỉ cần đã nhập sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang; định dạng và miền giá trị chưa quy định (Q-44) | Kiểu Chữ vì chuỗi chữ số có thể bắt đầu bằng số 0. Gợi ý "Mã vé sẽ được gửi qua SMS tới số này. Ví dụ: 0912345678". Độ dài tối đa 20 gồm cả ký tự phân cách là giả định ASM-52 | P04 UC-009 Dữ liệu vào 2 STT 2, bước 7, 7a; GL-17; ASM-52; Q-44; UI-STT 31 |
| Tuyến của chuyến | - | Chữ | Hiển thị; căn trái | Dạng "Điểm đi - Điểm đến" | Nhận từ SCR-02 | P04 UC-009 Dữ liệu ra 1 STT 2; UI-STT 13 |
| Giờ xuất bến của chuyến | 16 | Ngày | Hiển thị; căn trái | Định dạng dd/MM/yyyy HH:mm | Độ dài của định dạng hiển thị | P04 UC-009 Dữ liệu ra 1 STT 2; GL-07; UI-STT 13 |
| Chỗ đang giữ | - | Chữ | Hiển thị; căn trái | Danh sách mã chỗ, từ 1 đến 5 chỗ, ngăn bằng dấu phẩy | Nhận từ SCR-02 | P04 UC-009 Dữ liệu vào 1 STT 1, BR-01; GL-01 |
| Số chỗ đang giữ | - | Số | Hiển thị; căn trái | Số nguyên từ 1 đến 5, bằng số mã chỗ trong danh sách | Giá trị tính từ danh sách | P04 UC-009 BR-01 |
| Thời hạn giữ chỗ | 5 | Giờ | Hiển thị; căn trái | Dạng HH:mm; bằng thời điểm giữ chỗ cộng 10 phút | Hệ thống cấp, độ dài là của định dạng hiển thị | P04 UC-009 BR-03, mục 8; GL-21; UI-STT 13, 46 |
| Thời gian còn lại | 5 | Giờ | Hiển thị; căn trái; cập nhật mỗi giây | Dạng mm:ss, từ 10:00 giảm về 00:00 | Hệ thống tính từ thời hạn giữ chỗ | BR-03; GL-20; UI-STT 46 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Họ tên người đi | Khi rời trường; khi nhấn "Tiếp tục thanh toán" | 1. Bắt buộc: đã nhập (không chỉ khoảng trắng). 2. Định dạng, miền giá trị, quy tắc nghiệp vụ: chưa quy định (Q-44), chưa kiểm tra | MSG-05 |
| Số điện thoại người đi | Khi rời trường; khi nhấn "Tiếp tục thanh toán" | 1. Bỏ khoảng trắng, dấu chấm, dấu gạch ngang. 2. Bắt buộc: còn ít nhất một ký tự. 3. Định dạng, miền giá trị, quy tắc nghiệp vụ: chưa quy định (Q-44), chưa kiểm tra | MSG-06 |
| Cả hai trường | Khi nhấn "Tiếp tục thanh toán" | Hai trường cùng lỗi: tóm tắt lỗi, đưa tiêu điểm tới trường lỗi đầu tiên | MSG-15 |
| Thời hạn giữ chỗ | Liên tục từ bước 6 đến bước 8 | Còn trong 10 phút kể từ lúc giữ chỗ (BR-03) | MSG-08 |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-03 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Thời hạn giữ chỗ và thời gian còn lại luôn hiển thị; MSG-13 khi xử lý thanh toán | - |
| SCR-03 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Có "Huỷ yêu cầu mua vé" và mục "Trang chủ" trả chỗ ngay; không có nút "Quay lại" SCR-02 vì đặc tả không có dịch chuyển lùi từ bước 6 | - |
| SCR-03 | Nielsen 5 Ngăn lỗi | Vi phạm còn mở | Mục "Trang chủ" và "Huỷ yêu cầu mua vé" trả chỗ ngay không qua xác nhận, hành khách bấm nhầm sẽ mất chỗ đã giữ | Q-71; chưa thêm hộp xác nhận vì đặc tả không có |
| SCR-03 | Nielsen 6 Nhận biết thay vì nhớ lại | Vi phạm còn mở | Tóm tắt có tuyến, giờ xuất bến, chỗ nhưng không có giá vé và tổng tiền vì P04 chưa có dữ liệu này trước bước 12 | Q-70 |
| SCR-03 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | MSG-05, MSG-06 ngay dưới ô, nói rõ việc cần làm; MSG-15 nêu số trường cần sửa | - |
| SCR-03 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Lỗi có biểu tượng và tiền tố "Lỗi:"; trường bắt buộc ghi "(bắt buộc)" bằng chữ | - |
| SCR-03 | WCAG 2.2.1 Điều chỉnh thời gian | Đạt | Thời hạn 10 phút do BR-03 quy định nên không cho kéo dài (ngoại lệ thiết yếu); thời gian còn lại hiển thị, trình đọc màn hình được báo ở ba mốc (MSG-16) | - |
| SCR-03 | WCAG 3.3.1 Nhận biết lỗi | Đạt | Lỗi hiện bằng chữ cạnh ô, gắn aria-describedby, kèm banner MSG-15 khi có từ hai lỗi | - |
| SCR-03 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhãn luôn hiển thị, gắn for; gợi ý ví dụ nằm dưới nhãn, không dùng placeholder thay nhãn | - |
| SCR-03 | WCAG 3.3.4 Ngăn lỗi với dữ liệu tài chính | Vi phạm còn mở | Hành khách sang bước thanh toán mà chưa thấy tổng tiền trên màn hình này | Q-70; tổng tiền được xác nhận ở màn hình thanh toán của UC-010 |
| SCR-03 | WCAG 3.3.7 Không bắt nhập lại | Đạt | Họ tên và số điện thoại chỉ nhập một lần cho cả lần đặt (ASM-19); MSG-14 giữ dữ liệu | - |
| SCR-03 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Mốc còn 5 phút, 1 phút, 30 giây thông báo bằng role status; MSG-15 và lỗi trường khai báo role alert | - |
| SCR-03 | Baymard: form một cột, nhãn trên ô, đánh dấu bắt buộc | Đạt | Hai ô một cột, nhãn trên ô, ghi "(bắt buộc)" | - |
| SCR-03 | Baymard: giảm số trường tới mức đặc tả yêu cầu | Đạt | Chỉ có hai ô của Dữ liệu vào 2; không có tài khoản, không có trường thẻ | - |
| SCR-03 | Baymard: hiển thị tóm tắt đơn và tổng tiền | Vi phạm còn mở | Chỉ có tóm tắt chuyến và chỗ, chưa có giá vé và tổng tiền | Q-70 |
| SCR-03 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 1 đến 17, 18, 19, 22, 27 đến 33, 34 đến 37, 39, 40, 43 đến 45, 47 đến 55, 57 đến 64, 69 | - |

## h) Thông điệp mới

| MSG | Loại | Nội dung hiển thị | Nút và hành động | Nguồn |
|---|---|---|---|---|
| MSG-15 | Lỗi | Có <n> trường cần sửa. Vui lòng kiểm tra các trường được đánh dấu lỗi. | Banner tại SCR-03 khi nhấn nút chính mà có từ hai trường lỗi; tiêu điểm vào trường lỗi đầu tiên; nút đóng "x" | UC-009 bước 7a; UI-STT 54 |
| MSG-16 | Cảnh báo | Chỗ của bạn chỉ còn được giữ <5 phút / 1 phút / 30 giây>. Vui lòng hoàn tất thanh toán. | Thông báo role status cho trình đọc màn hình tại ba mốc; không có nút và không chiếm tiêu điểm | BR-03; UC-009 bước 5; UI-STT 46 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-70 | Màn hình nhập thông tin người đi, bước ngay trước khi sang thanh toán, có hiển thị giá vé từng chỗ và tổng tiền của lần đặt không? (Không, tổng tiền chỉ hiển thị ở màn hình thanh toán của UC-010 / Có, hiển thị giá vé từng chỗ và tổng tiền ở SCR-03) | SCR-03 vùng tóm tắt; UI-STT 69; F7 Nielsen 6, WCAG 3.3.4, Baymard | P04 UC-009 bước 6 chỉ có Dữ liệu vào 2, không có dữ liệu ra; giá vé và tổng tiền chỉ nằm ở Dữ liệu ra 1 của bước 12; P07 UC-009 bước 8 tính tổng tiền rồi chuyển cho UC-010 |
| Q-71 | Khi hành khách nhấn mục "Trang chủ" (hoặc đóng trang) lúc đang mua vé (SCR-02, SCR-03), hệ thống xử lý thế nào? (Coi như huỷ yêu cầu mua vé, trả chỗ ngay / Hỏi xác nhận rồi mới huỷ / Chỉ rời màn hình, các chỗ vẫn giữ đến hết 10 phút) | SCR-02, SCR-03 mục "Trang chủ"; UC-009 luồng *a; ASM-24, ASM-53; F7 Nielsen 5 | P04 UC-009 luồng *a chỉ nêu "hành khách huỷ yêu cầu mua vé", không nêu rời màn hình bằng menu; UI-STT 37 yêu cầu ghi hành vi này ở đặc tả màn hình |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-52 | Họ tên người đi nhập tối đa 100 ký tự; số điện thoại người đi nhập tối đa 20 ký tự, gồm cả khoảng trắng, dấu chấm, dấu gạch ngang. | Chờ Q-44. Nguồn không nêu độ dài tối đa của hai trường người đi nhập (độ dài là giá trị nghiệp vụ); chọn giới hạn rộng để không từ chối họ tên dài hoặc số có ký tự phân cách, trong khi điều kiện hợp lệ chờ Q-44 | SCR-03 trường "Họ tên người đi", "Số điện thoại người đi"; UC-009 Dữ liệu vào 2 |
| ASM-53 | Nhấn mục "Trang chủ" khi đang ở SCR-02 hoặc SCR-03 được coi là hành khách huỷ yêu cầu mua vé (luồng *a): hệ thống trả lại ngay các chỗ đang giữ (nếu đã giữ) và hiển thị MSG-09 ở SCR-01. | Chờ Q-71. Đặc tả không nêu rời màn hình bằng menu; chọn đồng nhất với luồng *a và ASM-24 để chỗ không bị giữ vô ích trong 10 phút | SCR-02, SCR-03 mục "Trang chủ"; E-05, E-06; UC-009 luồng *a |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-009 bước 5, bước 6 | Đặc tả không nêu hệ thống hiển thị cho hành khách các chỗ đang giữ và thời hạn giữ chỗ trước khi nhập thông tin người đi; SCR-03 hiển thị hai thông tin này dựa vào BR-03, GL-21 và UI-STT 46 | Thêm vào bước 5 hoặc bước 6 việc hiển thị chỗ đang giữ và thời hạn giữ chỗ cho hành khách |

## Vấn đề còn mở

- Q-44 chưa có trả lời nên hai ô chỉ kiểm tra bắt buộc; khi có điều kiện hợp lệ cần thêm kiểm tra định dạng và MSG tương ứng.
- Bước thanh toán (UC-010) chưa có màn hình nên SCR-03 hiển thị MSG-14 khi lỗi hệ thống xảy ra lúc đang thanh toán; kết quả giao dịch trong trường hợp đó do UC-010 và BR-06 xử lý.
- MSG-16 chỉ là thông báo cho trình đọc màn hình; cảnh báo bằng hình ảnh là dòng thời gian còn lại luôn hiển thị.
