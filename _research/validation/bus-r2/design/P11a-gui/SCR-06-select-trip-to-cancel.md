# P11a - SCR-06 Chọn chuyến cần huỷ - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0); P04-uc-specs/UC-017-cancel-trip.md (luồng sự kiện, bảng dữ liệu vào ra, BR, Câu hỏi mở, Giả định); P05-glossary.md (GL-03, GL-04, GL-07, GL-13, GL-14, GL-22); P06-supplementary-spec.md (NFR-03, BR-09, BR-10); P07-uc-analysis/UC-017 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng AC-B-CancelTripForm); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4). Placeholder: CHE_DO_CHAY = Giai đoạn 2: các màn hình của UC-009, UC-017; THIET_BI_HIEN_THI, NHAN_DIEN_THUONG_HIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có, XUAT_HTML = Không, THONG_TIN_TAI_LIEU = Không có, YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét trước lần chạy: Q-69, ASM-51; lần chạy giai đoạn 2 này cấp Q-70 đến Q-72, ASM-52 đến ASM-54 |
| Phạm vi | SCR-06 (UC-017 bước 2, 3, 4a, 4b, *a) |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 |

## a) Thông tin tài liệu

Không có (THONG_TIN_TAI_LIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có; dùng mẫu F5).

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-06 Chọn chuyến cần huỷ (Select trip to cancel) |
| UC | UC-017 Huỷ chuyến |
| Bước UC | 2, 3, 4a, 4b, *a (bước 4 kiểm tra do hệ thống thực hiện sau khi xác nhận ở SCR-07) |
| Tác nhân | ACT-03 Nhân viên điều hành (chỉ vai trò này huỷ được chuyến, NFR-03, ASM-34) |
| Boundary AC | AC-B-CancelTripForm |
| DC | DC-CancelTripView (tiếp nhận thao tác: DC-CancelTripRequestHandler) |
| Loại màn hình | Độc lập (đến từ SCR-05 bằng dịch chuyển đơn giản) |
| Đến từ | SCR-05 (E-09, mẫu 1, "chọn Huỷ chuyến"); SCR-07 khi pop-up đóng ngầm định (không vẽ cạnh) |
| Đi tới | SCR-07 (E-10, mẫu 2, pop-up modal); SCR-05 (E-12, mẫu 1: "Bỏ yêu cầu huỷ chuyến", menu "Trang chủ") |
| Hành vi khi rời bằng menu | Mục "Trang chủ" coi là bỏ yêu cầu huỷ chuyến (luồng *a): không dữ liệu nào thay đổi, mở SCR-05 kèm MSG-12 (ASM-54, chờ Q-71) |
| Nền tảng | Phần mềm web cho nhân viên nhà xe, máy tính bàn từ 1280 x 720 px, chuột và bàn phím (UI-STT 2) |

## c) Hình ảnh màn hình

```text
+----------------------------------------------------------------------------------+
| SaoViet Bus                                                        [ Trang chủ ] |
|----------------------------------------------------------------------------------|
| Chọn chuyến cần huỷ                                                              |
| [ vùng thông điệp: trống; MSG-10, MSG-11 hiện ở đây ]                            |
|                                                                                  |
| Chuyến trong lịch chạy (chọn một chuyến)                                         |
| +---+----------------+------------------+------------------+--------------+      |
| |   | Tuyến          | Giờ xuất bến     | Xe               | Tài xế       | Trạng thái |
| +---+----------------+------------------+------------------+--------------+      |
| |( )| Hà Nội - Hải Phòng | 15/12/2026 18:00 | Xe ghế ngồi 29 chỗ | Lê Quang Huy | Chưa huỷ |
| |(x)| Hà Nội - Vinh  | 15/12/2026 20:30 | Xe giường nằm 40 chỗ | Trần Văn Bình | Chưa huỷ |
| |( )| Hà Nội - Vinh  | 15/12/2026 22:00 | Xe giường nằm 40 chỗ | Phạm Minh Đức | Đã huỷ   |
| +---+----------------+------------------+------------------+--------------+      |
|                                                                                  |
| Lý do huỷ chuyến (bắt buộc)                                                      |
|   (x) Xe hỏng      ( ) Thời tiết                                                 |
|----------------------------------------------------------------------------------|
|                     [ Bỏ yêu cầu huỷ chuyến ]   [ Tiếp tục huỷ chuyến ]          |
+----------------------------------------------------------------------------------+
```

Bảng chỉ hiển thị 3 dòng minh hoạ; từ 21 chuyến trở lên bảng phân trang 20 dòng mỗi trang (UI-STT 25). Khi phóng to chữ 400% (độ rộng 320 px) bảng chuyển thành thẻ (UI-STT 25, 62).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh trên | Tên hệ thống "SaoViet Bus", mục "Trang chủ" | Trên cùng, cao 56 px | UI-STT 7, 34, 35 |
| Tiêu đề | "Chọn chuyến cần huỷ" (tiêu đề cấp 1) | Dưới thanh trên | UI-STT 12 |
| Thông điệp | Banner MSG-10, MSG-11; hộp modal MSG-14 | Banner dưới tiêu đề | UI-STT 11, 48 |
| Nội dung - bảng chuyến | Cột chọn (nút chọn), tuyến, giờ xuất bến, xe, tài xế, trạng thái chuyến; sắp theo giờ xuất bến tăng dần; phân trang khi từ 21 dòng | Đầu vùng nội dung | UI-STT 25 |
| Nội dung - lý do | Nhóm nút chọn "Lý do huỷ chuyến" với hai lựa chọn | Dưới bảng | UI-STT 23, 59 (fieldset, legend) |
| Hành động | "Bỏ yêu cầu huỷ chuyến" (nút phụ), "Tiếp tục huỷ chuyến" (nút chính) | Cuối nội dung, căn phải, ngăn bằng đường kẻ 1 px | UI-STT 7, 8, 18, 19 |

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Màn hình | Vùng hiển thị | Khởi tạo | Hiển thị tiêu đề cấp 1, bảng chuyến và nhóm lý do; chưa chọn chuyến và chưa chọn lý do; tiêu điểm đặt ở nút chọn đầu tiên của bảng (UI-STT 32). Tiêu đề trang trình duyệt là "Chọn chuyến cần huỷ - SaoViet Bus" | UC-017 bước 2; UI-STT 12, 32 |
| 2 | Bảng chuyến | Bảng | Khởi tạo | Hiển thị các chuyến trong lịch chạy, mỗi chuyến một dòng gồm tuyến, giờ xuất bến, xe, tài xế, trạng thái chuyến (Chưa huỷ hoặc Đã huỷ), sắp theo giờ xuất bến tăng dần | UC-017 bước 2, Dữ liệu ra 1; GL-13 |
| 3 | Nút chọn ở đầu mỗi dòng | Nút chọn | Chọn | Chọn một chuyến cần huỷ (chỉ một chuyến); dòng đã chọn có nút chọn được đánh dấu, không chỉ tô màu. Chuyến Đã huỷ hoặc đã đến giờ xuất bến vẫn chọn được để hệ thống từ chối theo luồng 4a, 4b | UC-017 bước 3, Dữ liệu vào 1 STT 1; UI-STT 25 |
| 4 | Liên kết phân trang | Liên kết | Nhấn | Chuyển trang danh sách (từ 21 chuyến trở lên, 20 dòng mỗi trang), giữ nguyên chuyến và lý do đã chọn | UC-017 bước 2; UI-STT 25; Q-72 |
| 5 | Nhóm nút chọn "Lý do huỷ chuyến" | Nút chọn | Chọn | Chọn một trong hai lý do: Xe hỏng, Thời tiết; không chọn sẵn | UC-017 bước 3, Dữ liệu vào 1 STT 2; ASM-25; UI-STT 23 |
| 6 | Nút "Tiếp tục huỷ chuyến" | Nút chính | Khởi tạo | Vô hiệu (aria-disabled) cho tới khi đã chọn cả chuyến và lý do | UC-017 Dữ liệu vào 1 (bắt buộc: Có); UI-STT 21 |
| 7 | Nút "Tiếp tục huỷ chuyến" | Nút chính | Nhấn | Mở pop-up SCR-07 (khoá SCR-06) kèm chuyến và lý do đã chọn (E-10); chưa gửi gì cho hệ thống | UC-017 bước 3; UI-STT 65, 66 |
| 8 | Nút "Bỏ yêu cầu huỷ chuyến" | Nút phụ | Nhấn | Bỏ yêu cầu huỷ chuyến (luồng *a), không dữ liệu nào thay đổi; mở SCR-05 và hiển thị MSG-12 (E-12) | UC-017 bước *a; ASM-27; MSG-12 |
| 9 | Mục "Trang chủ" ở thanh trên | Liên kết | Nhấn | Xử lý như "Bỏ yêu cầu huỷ chuyến" (mục 8): mở SCR-05 kèm MSG-12 (ASM-54, chờ Q-71) | ASM-54; UC-017 bước *a; UI-STT 34, 37 |
| 10 | Banner MSG-10 | Vùng hiển thị | Nhận kết quả | Hệ thống báo chuyến đã chọn đã bị huỷ (luồng 4a, BR-09): hiển thị banner, làm mới bảng chuyến, giữ nguyên lý do đã chọn, bỏ chọn chuyến, tiêu điểm vào banner rồi nút chọn đầu tiên | UC-017 bước 4a; BR-09; MSG-10; UI-STT 52 |
| 11 | Banner MSG-11 | Vùng hiển thị | Nhận kết quả | Hệ thống báo chuyến đã đến giờ xuất bến (luồng 4b, BR-10): hiển thị banner, làm mới bảng chuyến, giữ nguyên lý do đã chọn, bỏ chọn chuyến | UC-017 bước 4b; BR-10; MSG-11; UI-STT 52 |
| 12 | Nút đóng "x" của banner | Nút | Nhấn | Đóng banner MSG-10 hoặc MSG-11; hành vi tương ứng cho MSG-14 xem mục 13 | UI-STT 48 |
| 13 | Hộp thông điệp MSG-14 | Nút | Nhấn | Nút "Đóng": đóng hộp, ở lại SCR-06, giữ nguyên chuyến và lý do đã chọn (hộp này cũng hiển thị khi lỗi hệ thống xảy ra sau SCR-07) | UI-STT 52, 53; MSG-14 |

## e) Định nghĩa thuộc tính trường

| Mục | Số ký tự tối đa | Kiểu | Thuộc tính trường | Ràng buộc dữ liệu | Ghi chú | Nguồn |
|---|---|---|---|---|---|---|
| Chuyến cần huỷ | - | Lựa chọn | Chọn; bắt buộc; mặc định chưa chọn; một chuyến | Là chuyến có trong lịch chạy, chưa bị huỷ (BR-09) và chưa đến giờ xuất bến (BR-10); hai điều kiện sau do hệ thống kiểm tra | Chuyến đã huỷ vẫn chọn được để luồng 4a đến được | P04 UC-017 Dữ liệu vào 1 STT 1, BR-09, BR-10 |
| Lý do huỷ chuyến | - | Lựa chọn | Chọn; bắt buộc; mặc định chưa chọn; hai giá trị | Một trong hai giá trị: Xe hỏng, Thời tiết (ASM-25, Q-36) | Nhóm nút chọn, nhãn nhóm "Lý do huỷ chuyến" | P04 UC-017 Dữ liệu vào 1 STT 2; ASM-25; GL-04 |
| Tuyến | - | Chữ | Hiển thị; căn trái | Dạng "Điểm đi - Điểm đến" | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 1 STT 1; GL-22; UI-STT 13 |
| Giờ xuất bến | 16 | Ngày | Hiển thị; căn trái | Định dạng dd/MM/yyyy HH:mm | Độ dài của định dạng hiển thị | P04 UC-017 Dữ liệu ra 1 STT 2; GL-07; UI-STT 13 |
| Xe | - | Chữ | Hiển thị; căn trái | Xe được xếp vào chuyến, ví dụ "Xe giường nằm 40 chỗ" | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 1 STT 3; GL-14 |
| Tài xế | - | Chữ | Hiển thị; căn trái | Tài xế được xếp vào chuyến | Độ dài theo giá trị | P04 UC-017 Dữ liệu ra 1 STT 4 |
| Trạng thái chuyến | - | Lựa chọn | Hiển thị; căn trái; kèm biểu tượng khi Đã huỷ | Hai giá trị: Chưa huỷ, Đã huỷ | Không chỉ dùng màu để phân biệt (UI-STT 17) | P04 UC-017 Dữ liệu ra 1 STT 5; BR-09 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Chuyến cần huỷ | Khi chọn | 1. Bắt buộc: chưa chọn thì nút "Tiếp tục huỷ chuyến" vô hiệu, không hiện lỗi | Không có (UI-STT 21) |
| Lý do huỷ chuyến | Khi chọn | 1. Bắt buộc: chưa chọn thì nút "Tiếp tục huỷ chuyến" vô hiệu. 2. Miền giá trị: chỉ hai lựa chọn có sẵn nên không nhập sai được | Không có (UI-STT 21) |
| Chuyến cần huỷ | Sau khi xác nhận ở SCR-07 (hệ thống kiểm tra theo ASM-26) | Quy tắc nghiệp vụ theo thứ tự: chuyến chưa bị huỷ (BR-09); chuyến chưa đến giờ xuất bến (BR-10) | MSG-10; MSG-11 |
| Chuyến cần huỷ | Sau khi xác nhận ở SCR-07 | Lỗi hệ thống | MSG-14 |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-06 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Cột "Trạng thái" cho biết chuyến Chưa huỷ hay Đã huỷ ngay trên danh sách | - |
| SCR-06 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | "Bỏ yêu cầu huỷ chuyến" và "Trang chủ" thoát không thay đổi dữ liệu; xác nhận ở SCR-07 có "Không huỷ" | - |
| SCR-06 | Nielsen 5 Ngăn lỗi | Đạt | Nút "Tiếp tục huỷ chuyến" vô hiệu tới khi chọn đủ chuyến và lý do; lý do không chọn sẵn; thao tác huỷ phải qua SCR-07 | Chuyến đã huỷ hoặc đã xuất bến vẫn chọn được vì luồng 4a, 4b của đặc tả |
| SCR-06 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mỗi dòng hiển thị đủ tuyến, giờ, xe, tài xế, trạng thái để nhận biết chuyến | - |
| SCR-06 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Khoảng 80 chuyến mỗi ngày (nguồn mục mở đầu) nên lịch chạy một tuần có hàng trăm dòng, chỉ có phân trang 20 dòng, không có lọc theo ngày hoặc tuyến | Q-72; chưa thêm bộ lọc vì đặc tả không có |
| SCR-06 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | MSG-10, MSG-11 nêu chuyến nào, vì sao không huỷ được và việc cần làm; làm mới danh sách | - |
| SCR-06 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Bảng dùng th có scope; nhóm lý do dùng fieldset và legend | - |
| SCR-06 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Trạng thái "Đã huỷ" có chữ và biểu tượng; dòng được chọn có nút chọn đánh dấu | - |
| SCR-06 | WCAG 1.4.10 Reflow | Đạt | Bảng chuyển thành thẻ dưới 600 px, kể cả khi phóng to 400% trên máy tính bàn | - |
| SCR-06 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Thứ tự Tab: thanh trên, banner, bảng, nhóm lý do, nút hành động (UI-STT 32) | - |
| SCR-06 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhóm lý do có nhãn "(bắt buộc)"; mỗi nút chọn có nhãn đọc được | - |
| SCR-06 | WCAG 3.3.7 Không bắt nhập lại | Đạt | MSG-10, MSG-11, MSG-14 giữ nguyên lý do đã chọn | - |
| SCR-06 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 2, 4 đến 17, 18, 19, 23, 27, 28, 32 đến 37, 39, 40, 43 đến 45, 47 đến 55, 57 đến 64 | - |

## h) Thông điệp mới

Không có

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-72 | Danh sách "các chuyến trong lịch chạy" ở bước 2 có cần tìm hoặc lọc theo ngày, tuyến để nhân viên điều hành chọn chuyến không, hay chỉ hiển thị phân trang? (Chỉ phân trang, không lọc / Có lọc theo ngày và tuyến / Chỉ hiển thị các chuyến chưa huỷ và chưa xuất bến) | SCR-06 bảng chuyến; UC-017 bước 2, Dữ liệu ra 1; F7 Nielsen 7 | P04 UC-017 bước 2: "Hiển thị các chuyến trong lịch chạy" không nêu phạm vi (cả tuần, chỉ chuyến sắp chạy) hay cách tìm chuyến; nguồn nêu khoảng 80 chuyến mỗi ngày |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-54 | Nhấn mục "Trang chủ" khi đang ở SCR-06 được coi là nhân viên điều hành bỏ yêu cầu huỷ chuyến (luồng *a): không thay đổi dữ liệu và hiển thị MSG-12 ở SCR-05. | Chờ Q-71. Đặc tả không nêu rời màn hình bằng menu; chọn đồng nhất với luồng *a và ASM-27 | SCR-06 mục "Trang chủ"; E-12; UC-017 luồng *a |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-017 bước 2 | Phạm vi và cách tìm chuyến trong "các chuyến trong lịch chạy" không nêu (Q-72) | Nêu phạm vi danh sách (ví dụ chuyến chưa huỷ và chưa xuất bến) hoặc bộ lọc theo câu trả lời Q-72 |

## Vấn đề còn mở

- Q-72 chưa có trả lời nên F7 Nielsen 7 là Vi phạm còn mở.
- Q-71 áp dụng cho cả mục "Trang chủ" ở SCR-02, SCR-03 (ASM-53) và SCR-06 (ASM-54); câu hỏi nằm ở SCR-03.
- Bảng minh hoạ có 3 dòng; dữ liệu thật có thể trên 20 dòng nên phân trang đã được quy định ở UI-STT 25.
