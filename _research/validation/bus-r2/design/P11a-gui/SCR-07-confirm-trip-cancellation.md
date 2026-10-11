# P11a - SCR-07 Xác nhận huỷ chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0); P04-uc-specs/UC-017-cancel-trip.md (luồng sự kiện, bảng dữ liệu vào ra, BR, Câu hỏi mở, Giả định); P05-glossary.md (GL-04, GL-07, GL-10); P06-supplementary-spec.md (NFR-03, NFR-05, BR-07 đến BR-11); P07-uc-analysis/UC-017 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng AC-B-CancelTripForm); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4). Placeholder: CHE_DO_CHAY = Giai đoạn 2: các màn hình của UC-009, UC-017; THIET_BI_HIEN_THI, NHAN_DIEN_THUONG_HIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có, XUAT_HTML = Không, THONG_TIN_TAI_LIEU = Không có, YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét trước lần chạy: Q-69, ASM-51 |
| Phạm vi | SCR-07 (UC-017 bước 3, 4, 4a, 4b) |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 |

## a) Thông tin tài liệu

Không có (THONG_TIN_TAI_LIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có; dùng mẫu F5).

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-07 Xác nhận huỷ chuyến (Confirm trip cancellation) |
| UC | UC-017 Huỷ chuyến |
| Bước UC | 3 (gửi chuyến và lý do), 4, 4a, 4b |
| Tác nhân | ACT-03 Nhân viên điều hành |
| Boundary AC | AC-B-CancelTripForm |
| DC | DC-CancelTripView (tiếp nhận thao tác: DC-CancelTripRequestHandler) |
| Loại màn hình | Con phụ thuộc (pop-up modal, SCR-06 bị khoá) |
| Đến từ | SCR-06 (E-10, mẫu 2, nút "Tiếp tục huỷ chuyến") |
| Đi tới | SCR-08 (E-11, mẫu 4, "Kết quả huỷ chuyến"). Nút "Không huỷ" và Esc đóng pop-up, quay về SCR-06 ngầm định, không vẽ cạnh. Luồng 4a, 4b: pop-up đóng và SCR-06 hiển thị MSG-10, MSG-11 |
| Nền tảng | Phần mềm web cho nhân viên nhà xe, máy tính bàn từ 1280 x 720 px, chuột và bàn phím (UI-STT 2) |

## c) Hình ảnh màn hình

```text
          (nền SCR-06 bị phủ #1F2933 độ mờ 60%, không thao tác được)
        +--------------------------------------------------------+
        | Cảnh báo: Xác nhận huỷ chuyến                           |
        |--------------------------------------------------------|
        | Chuyến                                                  |
        | Hà Nội - Vinh, 15/12/2026 20:30                         |
        | Lý do huỷ chuyến                                        |
        | Xe hỏng                                                 |
        |                                                         |
        | Khi xác nhận, chuyến chuyển sang Đã huỷ.                |
        | Mọi vé đang có hiệu lực của chuyến bị huỷ.              |
        | Hành khách được báo qua SMS.                            |
        | Vé mua trực tuyến được hoàn 100% giá vé qua Cổng        |
        | thanh toán. Vé mua tại quầy chờ hoàn tiền mặt tại quầy. |
        | Thao tác này không hoàn tác được.                       |
        |--------------------------------------------------------|
        |             [ Không huỷ ]   [ Xác nhận huỷ chuyến ]     |
        +--------------------------------------------------------+
```

Nút "Xác nhận huỷ chuyến" là nút nguy hiểm (nền #B3261E, UI-STT 20); tiêu điểm đầu ở "Không huỷ" (UI-STT 47, 66).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Tiêu đề hộp | Biểu tượng và tiền tố "Cảnh báo:" kèm "Xác nhận huỷ chuyến" | Đầu hộp, rộng tối đa 480 px, giữa màn hình | UI-STT 12, 47, 66 |
| Nội dung - đối tượng | Tuyến, giờ xuất bến, lý do huỷ chuyến đã chọn ở SCR-06 | Dưới tiêu đề hộp | UI-STT 66; mục chi tiết chỉ đọc theo UI-STT 14 |
| Nội dung - hệ quả | Năm câu nêu hệ quả của việc huỷ, lấy từ BR-07, BR-08, BR-11 | Dưới đối tượng | UI-STT 66 |
| Hành động | "Không huỷ" (nút phụ, nút an toàn), "Xác nhận huỷ chuyến" (nút nguy hiểm) | Cuối hộp, căn phải, nút phụ bên trái | UI-STT 8, 20, 47, 67 |
| Thông điệp xử lý | MSG-13 cạnh nút vừa nhấn | Trong hộp, cạnh nút | UI-STT 43 |

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Hộp xác nhận | Vùng hiển thị | Khởi tạo | Mở pop-up modal, khoá SCR-06; hiển thị tuyến, giờ xuất bến, lý do huỷ chuyến đã chọn và các câu hệ quả; tiêu điểm vào nút "Không huỷ"; tiêu điểm được giữ trong hộp | UC-017 bước 3; BR-07, BR-08, BR-11; UI-STT 47, 66 |
| 2 | Nút "Không huỷ" | Nút phụ | Nhấn | Đóng pop-up, quay về SCR-06 với chuyến và lý do vẫn được chọn; không gửi gì cho hệ thống (luồng *a ở mức màn hình xác nhận) | UC-017 bước *a; ASM-27; UI-STT 66 |
| 3 | Phím Esc | Nút phụ | Nhấn | Như "Không huỷ"; không có tác dụng khi đang xử lý | UI-STT 40, 44, 66 |
| 4 | Nút "Xác nhận huỷ chuyến" | Nút nguy hiểm | Nhấn | Vô hiệu cả hai nút, hiện MSG-13 sau 1 giây (không có nút huỷ khi đang xử lý). Hệ thống kiểm tra chuyến chưa bị huỷ (BR-09), rồi chưa đến giờ xuất bến (BR-10). Đã huỷ --> đóng pop-up, hiển thị MSG-10 tại SCR-06 (luồng 4a). Đã đến giờ xuất bến --> đóng pop-up, hiển thị MSG-11 tại SCR-06 (luồng 4b). Hợp lệ --> hệ thống lưu chuyến Đã huỷ, huỷ vé, gửi SMS, hoàn tiền (bước 5 đến 13) rồi mở SCR-08 kèm kết quả (E-11). Lỗi hệ thống --> đóng pop-up, hiển thị MSG-14 tại SCR-06 | UC-017 bước 3 đến 14, 4a, 4b; ASM-26; BR-09, BR-10; MSG-10, MSG-11, MSG-13, MSG-14; UI-STT 44, 53 |

## e) Định nghĩa thuộc tính trường

| Mục | Số ký tự tối đa | Kiểu | Thuộc tính trường | Ràng buộc dữ liệu | Ghi chú | Nguồn |
|---|---|---|---|---|---|---|
| Tuyến của chuyến cần huỷ | - | Chữ | Hiển thị; căn trái | Dạng "Điểm đi - Điểm đến" | Nhận từ SCR-06 | P04 UC-017 Dữ liệu vào 1 STT 1, Dữ liệu ra 1 STT 1; GL-22 |
| Giờ xuất bến của chuyến cần huỷ | 16 | Ngày | Hiển thị; căn trái | Định dạng dd/MM/yyyy HH:mm | Độ dài của định dạng hiển thị | P04 UC-017 Dữ liệu vào 1 STT 1, Dữ liệu ra 1 STT 2; GL-07 |
| Lý do huỷ chuyến | - | Lựa chọn | Hiển thị; căn trái | Một trong hai giá trị: Xe hỏng, Thời tiết | Nhận từ SCR-06; không sửa được ở đây | P04 UC-017 Dữ liệu vào 1 STT 2; ASM-25 |
| Câu hệ quả | - | Chữ | Hiển thị; căn trái; chữ #1F2933 16 px | Nội dung cố định lấy từ BR-07, BR-08, BR-11 | Không có số liệu động (không nêu số vé vì P04 chưa có dữ liệu này trước bước 14) | P04 UC-017 BR-07, BR-08, BR-11; UI-STT 66 |

## f) Kiểm tra dữ liệu nhập

Không có trường nhập chữ. Chuyến và lý do đã được kiểm tra bắt buộc ở SCR-06.

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Chuyến cần huỷ | Khi nhấn "Xác nhận huỷ chuyến" (hệ thống, ASM-26) | Chưa bị huỷ (BR-09), rồi chưa đến giờ xuất bến (BR-10) | MSG-10; MSG-11 |
| Chuyến cần huỷ | Khi nhấn "Xác nhận huỷ chuyến" | Lỗi hệ thống | MSG-14 |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-07 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | MSG-13 khi xử lý; không đóng hộp cho tới khi có kết quả | - |
| SCR-07 | Nielsen 2 Khớp giữa hệ thống và thế giới thực | Đạt | Nhãn nút đặt theo hành động: "Xác nhận huỷ chuyến", "Không huỷ" | - |
| SCR-07 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | "Không huỷ" và Esc đóng hộp không thay đổi dữ liệu | - |
| SCR-07 | Nielsen 4 Nhất quán và theo chuẩn | Vi phạm đã sửa | Bản đầu cho MSG-14 hiện chồng lên hộp xác nhận (hai hộp modal lồng nhau) | Đóng SCR-07 trước, hiển thị MSG-14 tại SCR-06 (chức năng 4) |
| SCR-07 | Nielsen 5 Ngăn lỗi | Đạt | Thao tác không hoàn tác có hộp xác nhận riêng nêu lại chuyến, lý do, hệ quả; tiêu điểm đầu ở nút an toàn; Enter không kích hoạt nút nguy hiểm | - |
| SCR-07 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Tiêu đề hộp có biểu tượng và tiền tố "Cảnh báo:"; nút nguy hiểm khác nút phụ bằng nhãn | - |
| SCR-07 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ trắng trên #B3261E 6,54:1; cảnh báo #7A4A00 trên #FFF4D6 6,83:1 | - |
| SCR-07 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Tiêu điểm vào "Không huỷ", giữ trong hộp, trả về nút "Tiếp tục huỷ chuyến" khi đóng | - |
| SCR-07 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Việc huỷ gây hoàn tiền phải xác nhận trước khi gửi, hệ quả nêu bằng chữ | - |
| SCR-07 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Hộp khai báo role alertdialog; MSG-13 khai báo role status | - |
| SCR-07 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 2, 4 đến 17, 18, 19, 20, 27, 32, 33, 39, 40, 43 đến 45, 47, 53, 57 đến 68 | - |

## h) Thông điệp mới

Không có

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | - | - | - |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | ASM-26, ASM-27 (P04 UC-017) được dẫn ở d) |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Không có | - | - | - |

## Vấn đề còn mở

- Hộp xác nhận là bước trình bày thêm giữa bước 3 và bước 4 của P04 theo UI-STT 65, không phải chức năng mới của đặc tả; nếu người dùng không muốn thêm bước này, bỏ SCR-07 và sửa E-10, E-11 ở screen-transition.md.
- Nếu lỗi hệ thống (MSG-14) xảy ra sau khi chuyến đã được lưu Đã huỷ ở bước 5, thử lại sẽ nhận MSG-10 (chuyến đã bị huỷ); kết quả đầy đủ của lần huỷ đó không xem lại được trên màn hình nào.
