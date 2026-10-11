# P11a - SCR-08 Kết quả huỷ chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0); P04-uc-specs/UC-017-cancel-trip.md (luồng sự kiện, bảng dữ liệu vào ra, BR, Câu hỏi mở, Giả định); P05-glossary.md (GL-04, GL-10, GL-15, GL-17, GL-24 đến GL-28); P06-supplementary-spec.md (NFR-05, NFR-06, BR-07, BR-08, BR-11); P07-uc-analysis/UC-017 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng AC-B-CancelTripForm); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4). Placeholder: CHE_DO_CHAY = Giai đoạn 2: các màn hình của UC-009, UC-017; THIET_BI_HIEN_THI, NHAN_DIEN_THUONG_HIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có, XUAT_HTML = Không, THONG_TIN_TAI_LIEU = Không có, YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét trước lần chạy: Q-69, ASM-51 |
| Phạm vi | SCR-08 (UC-017 bước 14, kết quả của bước 5 đến 13, kể cả luồng 7a, 9a, 10a, 12a) |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 |

## a) Thông tin tài liệu

Không có (THONG_TIN_TAI_LIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có; dùng mẫu F5).

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-08 Kết quả huỷ chuyến (Trip cancellation result) |
| UC | UC-017 Huỷ chuyến |
| Bước UC | 14 (kết quả của bước 5 đến 13) |
| Tác nhân | ACT-03 Nhân viên điều hành |
| Boundary AC | AC-B-CancelTripForm |
| DC | DC-CancelTripView (tiếp nhận thao tác: DC-CancelTripRequestHandler) |
| Loại màn hình | Phụ thuộc có dữ liệu (nhận "Kết quả huỷ chuyến" từ SCR-07, E-11) |
| Đến từ | SCR-07 (E-11, mẫu 4, "Kết quả huỷ chuyến") |
| Đi tới | SCR-05 (E-13, mẫu 1: "Về trang chủ", menu "Trang chủ"). Đây là màn hình kết thúc của UC-017 |
| Nền tảng | Phần mềm web cho nhân viên nhà xe, máy tính bàn từ 1280 x 720 px, chuột và bàn phím (UI-STT 2) |

## c) Hình ảnh màn hình

```text
+----------------------------------------------------------------------+
| SaoViet Bus                                            [ Trang chủ ] |
|----------------------------------------------------------------------|
| Kết quả huỷ chuyến                                                   |
| [ vùng thông điệp: trống ]                                           |
|                                                                      |
| Chuyến đã huỷ                                                        |
| Hà Nội - Vinh, 15/12/2026 20:30                                      |
|                                                                      |
| Vé                                                                   |
|   Số vé đã huỷ                                  5                    |
|   Vé mua tại quầy chờ hoàn tiền mặt             1                    |
|                                                                      |
| Thông báo qua SMS                                                    |
|   Số điện thoại đã báo qua SMS                  4                    |
|   Số điện thoại chưa báo được                   Không có             |
|                                                                      |
| Hoàn tiền vé mua trực tuyến                                          |
|   Vé đã hoàn                                    3 vé, 750.000 đ      |
|   Vé chưa hoàn được                             Không có             |
|----------------------------------------------------------------------|
|                                                 [ Về trang chủ ]     |
+----------------------------------------------------------------------+

Khi có số điện thoại hoặc vé chưa xử lý được (ví dụ SV0003 chưa hoàn được thì "Vé đã hoàn" là 2 vé, 500.000 đ), dòng đó đổi thành:
|   (!) Cảnh báo: Số điện thoại chưa báo được                          |
|       0944555666: SV0005                                             |
|   (!) Cảnh báo: Vé chưa hoàn được                                    |
|       SV0003                                                         |
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh trên | Tên hệ thống "SaoViet Bus", mục "Trang chủ" | Trên cùng, cao 56 px | UI-STT 7, 34, 35 |
| Tiêu đề | "Kết quả huỷ chuyến" (tiêu đề cấp 1) | Dưới thanh trên | UI-STT 12 |
| Thông điệp | Hộp modal MSG-14 (nếu lỗi hệ thống khi tải kết quả) | Giữa màn hình | UI-STT 47, 53 |
| Nội dung - chuyến | Tuyến và giờ xuất bến của chuyến đã huỷ | Đầu vùng nội dung | UI-STT 14 |
| Nội dung - nhóm kết quả | Ba nhóm: Vé, Thông báo qua SMS, Hoàn tiền vé mua trực tuyến; mỗi dòng nhãn bên trái, giá trị bên phải | Giữa vùng nội dung | Dòng cần chú ý có biểu tượng và tiền tố "Cảnh báo:" (UI-STT 17) |
| Hành động | "Về trang chủ" (nút chính) | Cuối nội dung, căn phải | UI-STT 8, 18, 49 |

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Màn hình | Vùng hiển thị | Khởi tạo | Hiển thị tiêu đề cấp 1 "Kết quả huỷ chuyến"; tiêu điểm đặt ở tiêu đề (UI-STT 32). Tiêu đề trang trình duyệt là "Kết quả huỷ chuyến - SaoViet Bus" | UC-017 bước 14; UI-STT 12, 32 |
| 2 | Vùng "Chuyến đã huỷ" | Vùng hiển thị | Khởi tạo | Hiển thị tuyến và giờ xuất bến của chuyến đã huỷ | UC-017 bước 14, Dữ liệu ra 4 STT 1 |
| 3 | Dòng "Số vé đã huỷ" | Vùng hiển thị | Khởi tạo | Hiển thị số vé đang có hiệu lực đã chuyển sang Đã huỷ; chuyến không có vé nào đang có hiệu lực (luồng 7a) thì hiển thị 0 | UC-017 Dữ liệu ra 4 STT 2; luồng 7a |
| 4 | Dòng "Số điện thoại đã báo qua SMS" | Vùng hiển thị | Khởi tạo | Hiển thị số số điện thoại có SMS đã chuyển cho Cổng SMS (mỗi số điện thoại khác nhau một SMS) | UC-017 Dữ liệu ra 4 STT 3; BR-11, ASM-30 |
| 5 | Dòng "Số điện thoại chưa báo được" | Vùng hiển thị | Khởi tạo | Hiển thị mỗi số điện thoại chưa gửi được SMS kèm mã các vé của số đó, mỗi số một dòng; không có thì hiển thị "Không có". Khi có số, dòng được đánh dấu biểu tượng và tiền tố "Cảnh báo:" (luồng 9a) | UC-017 Dữ liệu ra 4 STT 4; luồng 9a; ASM-31; Q-49 |
| 6 | Dòng "Vé mua trực tuyến đã hoàn" | Vùng hiển thị | Khởi tạo | Hiển thị số vé và tổng số tiền đã hoàn, dạng "3 vé, 750.000 đ"; tổng bằng 100% giá vé của các vé đó (BR-07) | UC-017 Dữ liệu ra 4 STT 5; BR-07; GL-18 |
| 7 | Dòng "Vé chưa hoàn được" | Vùng hiển thị | Khởi tạo | Hiển thị mã các vé Cổng thanh toán chưa hoàn được tiền; không có thì hiển thị "Không có". Khi có mã, dòng được đánh dấu biểu tượng và tiền tố "Cảnh báo:" (luồng 12a) | UC-017 Dữ liệu ra 4 STT 6; luồng 12a; ASM-33; Q-50 |
| 8 | Dòng "Vé mua tại quầy chờ hoàn tiền mặt" | Vùng hiển thị | Khởi tạo | Hiển thị số vé đã thanh toán tại quầy chờ hoàn tiền mặt tại quầy | UC-017 Dữ liệu ra 4 STT 7; BR-08 |
| 9 | Nút "Về trang chủ" | Nút chính | Nhấn | Mở SCR-05; use case UC-017 kết thúc (E-13) | UC-017 bước 14; UI-STT 49 |
| 10 | Mục "Trang chủ" ở thanh trên | Liên kết | Nhấn | Mở SCR-05, như nút "Về trang chủ" (E-13); việc huỷ chuyến đã hoàn tất nên không có dữ liệu đang giữ | UI-STT 34, 37 |
| 11 | Hộp thông điệp MSG-14 | Nút | Nhấn | Nút "Đóng": đóng hộp, ở lại SCR-08 | UI-STT 53; MSG-14 |

## e) Định nghĩa thuộc tính trường

| Mục | Số ký tự tối đa | Kiểu | Thuộc tính trường | Ràng buộc dữ liệu | Ghi chú | Nguồn |
|---|---|---|---|---|---|---|
| Tuyến của chuyến đã huỷ | - | Chữ | Hiển thị; căn trái | Dạng "Điểm đi - Điểm đến" | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 4 STT 1; GL-22 |
| Giờ xuất bến của chuyến đã huỷ | 16 | Ngày | Hiển thị; căn trái | Định dạng dd/MM/yyyy HH:mm | Độ dài của định dạng hiển thị | P04 UC-017 Dữ liệu ra 4 STT 1, Dữ liệu ra 1 STT 2; GL-07 |
| Số vé đã huỷ | - | Số | Hiển thị; căn phải | Số nguyên không âm | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 4 STT 2 |
| Số điện thoại đã báo qua SMS | - | Số | Hiển thị; căn phải | Số nguyên không âm; bằng số số điện thoại khác nhau của các vé đã huỷ trừ số chưa báo được | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 4 STT 3; ASM-30 |
| Số điện thoại chưa báo được | - | Chữ | Hiển thị; căn trái; mỗi số một dòng; kèm biểu tượng khi có giá trị | Số điện thoại và mã các vé của số đó; "Không có" khi trống | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 4 STT 4; ASM-31; GL-15, GL-17 |
| Số vé mua trực tuyến đã hoàn | - | Số | Hiển thị; căn phải | Số nguyên không âm | Hiển thị liền với tổng tiền, dạng "3 vé, 750.000 đ" | P04 UC-017 Dữ liệu ra 4 STT 5 |
| Tổng tiền đã hoàn | 13 | Tiền | Hiển thị; căn phải | Số nguyên đồng, phân cách hàng nghìn bằng dấu chấm, kèm " đ"; bằng tổng 100% giá vé của các vé đã hoàn (BR-07) | Thiết kế: 13 ký tự đủ cho "999.999.999 đ"; cộng các khoản cùng đơn vị đồng | P04 UC-017 Dữ liệu ra 4 STT 5, BR-07, mục 8; UI-STT 13 |
| Vé mua trực tuyến chưa hoàn được | - | Chữ | Hiển thị; căn trái; kèm biểu tượng khi có giá trị | Danh sách mã vé ngăn bằng dấu phẩy; "Không có" khi trống | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 4 STT 6; ASM-33; GL-15 |
| Số vé mua tại quầy chờ hoàn tiền mặt | - | Số | Hiển thị; căn phải | Số nguyên không âm | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 4 STT 7; BR-08 |

## f) Kiểm tra dữ liệu nhập

Không có trường nhập. Màn hình chỉ hiển thị kết quả.

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có | - | - | MSG-14 khi lỗi hệ thống lúc tải màn hình |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-08 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Màn hình kết quả nêu đủ bảy dữ liệu ra: số vé huỷ, SMS đã và chưa báo, hoàn tiền đã và chưa được, vé chờ hoàn tiền mặt | - |
| SCR-08 | Nielsen 4 Nhất quán và theo chuẩn | Đạt | Cùng bố cục mục chi tiết chỉ đọc (nhãn trên hoặc trái, giá trị đậm) và nút "Về trang chủ" như SCR-04 | - |
| SCR-08 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | Khi có số điện thoại chưa báo được hoặc vé chưa hoàn được, màn hình nêu danh sách nhưng không nêu cách xử lý tiếp vì cơ chế xử lý lại chưa quy định | Q-49, Q-50 (P04 UC-017) |
| SCR-08 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Vi phạm đã sửa | Bản đầu chỉ tô nền vàng cho dòng "Số điện thoại chưa báo được" và "Vé chưa hoàn được" khi có giá trị | Thêm biểu tượng và tiền tố chữ "Cảnh báo:" (UI-STT 17) |
| SCR-08 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ cảnh báo #7A4A00 trên #FFF4D6 6,83:1 | - |
| SCR-08 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Mỗi nhóm kết quả là danh sách mô tả (dt, dd) có tiêu đề nhóm cấp dưới không nhảy cấp | - |
| SCR-08 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Vùng kết quả khai báo role status để trình đọc màn hình đọc kết quả khi mở màn hình, tiêu điểm vẫn ở tiêu đề | - |
| SCR-08 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 2, 4 đến 17, 18, 27, 32 đến 37, 45, 47, 49, 53, 57 đến 64 | - |

## h) Thông điệp mới

Không có

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | - | - | Q-49, Q-50 (xử lý SMS và hoàn tiền không thành công) đã có ở P04 UC-017 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | ASM-30, ASM-31, ASM-33 (P04 UC-017) được dẫn ở d), e) |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Không có | - | - | - |

## Vấn đề còn mở

- Q-49, Q-50 chưa có trả lời nên F7 Nielsen 9 là Vi phạm còn mở; màn hình chưa có điều khiển xử lý lại số điện thoại hoặc vé chưa xử lý được.
- Ví dụ trên hình là kịch bản KB1 của P04 UC-017 (mọi SMS và hoàn tiền thành công); khối "Cảnh báo" minh hoạ định dạng khi có lỗi một phần (KB4).
- Kết quả huỷ chuyến chỉ hiển thị một lần ở màn hình này; P04 không có chức năng xem lại kết quả.
