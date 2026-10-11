# P11a - SCR-02 Chọn chỗ - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0); P04-uc-specs/UC-009-book-ticket-online.md (luồng sự kiện, bảng dữ liệu vào ra, BR); P05-glossary.md (GL-01, GL-02, GL-19); P06-supplementary-spec.md (NFR-04, NFR-08, BR-01, BR-02, BR-05); P07-uc-analysis/UC-009 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng AC-B-BookTicketOnlineForm); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4). Placeholder: CHE_DO_CHAY = Giai đoạn 2: các màn hình của UC-009, UC-017; THIET_BI_HIEN_THI, NHAN_DIEN_THUONG_HIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có, XUAT_HTML = Không, THONG_TIN_TAI_LIEU = Không có, YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét trước lần chạy: Q-69, ASM-51 |
| Phạm vi | SCR-02 (UC-009 bước 3, 4, 4a, 4b, 4c, *a) |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 |

## a) Thông tin tài liệu

Không có (THONG_TIN_TAI_LIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có; dùng mẫu F5).

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-02 Chọn chỗ (Select seats) |
| UC | UC-009 Đặt vé trực tuyến |
| Bước UC | 3, 4, 4a, 4b, 4c, *a (bước 2 thuộc UC-008, bước 5 giữ chỗ do hệ thống thực hiện sau khi hành khách nhấn "Tiếp tục") |
| Tác nhân | ACT-01 Hành khách (không cần tài khoản, NFR-02) |
| Boundary AC | AC-B-BookTicketOnlineForm |
| DC | DC-BookTicketOnlineView (tiếp nhận thao tác: DC-BookTicketOnlineRequestHandler) |
| Loại màn hình | Phụ thuộc có dữ liệu (nhận "Chuyến đã chọn" từ UC-008 qua SCR-01, E-02, ASM-49) |
| Đến từ | SCR-01 (E-02, mẫu 4, "Chuyến đã chọn"); menu "Trang chủ" của mọi màn hình không vẽ cạnh |
| Đi tới | SCR-03 (E-03, mẫu 4, "Các chỗ đang giữ"); SCR-01 (E-05, mẫu 1: "Tìm lại chuyến" ở MSG-02, "Về trang chủ" ở MSG-04, "Huỷ yêu cầu mua vé", menu "Trang chủ") |
| Nền tảng | Website cho hành khách, máy tính từ 1280 x 720 px và điện thoại từ 360 x 640 px (UI-STT 1) |

## c) Hình ảnh màn hình

```text
+------------------------------------------------------------------------+
| SaoViet Bus                                              [ Trang chủ ] |
|------------------------------------------------------------------------|
| Chọn chỗ                                                               |
| [ vùng thông điệp: trống; MSG-03 hiện ở đây ]                          |
|                                                                        |
| Chuyến                                                                 |
| Hà Nội - Vinh, 15/12/2026 20:30                                        |
|                                                                        |
| Sơ đồ chỗ - chọn tối đa 5 chỗ                                          |
|  [ A01 ] [ A02 ] [ A03 ] [A04 x] [ A05 v] [ A06 v] [ A07 ] [ A08 ]     |
|  [ A09 ] [A10 x] [ A11 ] [ A12 ] ...   (minh hoạ một phần sơ đồ)       |
|  Chú giải:  [ A ] Trống   [ v ] Đã chọn   [ x ] Không chọn được        |
|                                                                        |
| Đã chọn: A05, A06 (2 chỗ)                                              |
|------------------------------------------------------------------------|
|                     [ Huỷ yêu cầu mua vé ]   [ Tiếp tục ]              |
+------------------------------------------------------------------------+
```

Trên điện thoại (dưới 600 px) các nút xếp dọc, "Tiếp tục" ở trên, "Huỷ yêu cầu mua vé" ở dưới (UI-STT 9); sơ đồ chỗ được phép cuộn ngang (UI-STT 62).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh trên | Tên hệ thống "SaoViet Bus" bên trái, mục "Trang chủ" bên phải | Trên cùng, cao 56 px | UI-STT 7, 34, 35 |
| Tiêu đề | "Chọn chỗ" (tiêu đề cấp 1) | Dưới thanh trên | UI-STT 12 |
| Thông điệp | Banner MSG-03; hộp modal MSG-02, MSG-04, MSG-14 | Banner dưới tiêu đề; hộp modal ở giữa màn hình | UI-STT 11, 47, 48 |
| Nội dung - chuyến | Tuyến và giờ xuất bến của chuyến đã chọn | Đầu vùng nội dung | Mục chi tiết chỉ đọc: nhãn 14 px đậm trên, giá trị 16 px dưới (UI-STT 14) |
| Nội dung - sơ đồ chỗ | Lưới chỗ theo sơ đồ chỗ của loại xe, chú giải ba trạng thái, dòng gợi ý "Chọn tối đa 5 chỗ" | Giữa vùng nội dung | UI-STT 26, 55; bố cục lưới theo loại xe (GL-19) |
| Nội dung - chỗ đã chọn | Danh sách mã chỗ đã chọn và số chỗ | Dưới sơ đồ chỗ | role status, không chiếm tiêu điểm (UI-STT 45) |
| Hành động | "Huỷ yêu cầu mua vé" (nút phụ), "Tiếp tục" (nút chính) | Cuối nội dung, căn phải, ngăn bằng đường kẻ 1 px | UI-STT 7, 8, 18, 19 |

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Tiêu đề "Chọn chỗ" | Vùng hiển thị | Khởi tạo | Hiển thị tiêu đề cấp 1; tiêu điểm đặt ở tiêu đề vì màn hình không có ô nhập chữ (UI-STT 32). Tiêu đề trang trình duyệt là "Chọn chỗ - SaoViet Bus" | UC-009 bước 3; UI-STT 12, 32 |
| 2 | Vùng "Chuyến" | Vùng hiển thị | Khởi tạo | Hiển thị tuyến và giờ xuất bến của chuyến đã chọn ở UC-008, dạng "Hà Nội - Vinh, 15/12/2026 20:30" | UC-009 bước 3, Dữ liệu ra 1 dòng 2; ASM-49 |
| 3 | Lưới sơ đồ chỗ | Vùng hiển thị | Khởi tạo | Hiển thị sơ đồ chỗ của loại xe của chuyến; mỗi chỗ ở trạng thái Trống hoặc Không chọn được (chỗ đã có vé hoặc đang được giữ cho lần đặt khác); chưa chọn chỗ nào | UC-009 bước 3, Dữ liệu vào 1, BR-02; GL-02, GL-19 |
| 4 | Ô chỗ trống (mỗi chỗ một ô) | Ô chọn | Chọn | Đổi qua lại giữa Trống và Đã chọn; cập nhật vùng "Đã chọn" và trạng thái nút "Tiếp tục". Giao diện không chặn khi chọn quá 5 chỗ để việc từ chối theo luồng 4b do hệ thống thực hiện | UC-009 bước 3, Dữ liệu vào 1; UI-STT 26, 41 |
| 5 | Ô chỗ không chọn được | Ô chọn | Nhấn | Không đổi gì; ô khai báo aria-disabled, tên đọc được "Chỗ A04, không chọn được" | UC-009 Dữ liệu vào 1, BR-02; UI-STT 26 |
| 6 | Vùng "Đã chọn" | Vùng hiển thị | Chọn | Cập nhật danh sách mã chỗ đã chọn theo thứ tự mã chỗ và số chỗ; khi chưa chọn chỗ nào ghi "Chưa chọn chỗ" | UC-009 Dữ liệu vào 1; UI-STT 45 |
| 7 | Nút "Tiếp tục" | Nút chính | Khởi tạo | Vô hiệu (aria-disabled) khi chưa chọn chỗ nào, bật khi có ít nhất một chỗ được chọn | UC-009 Dữ liệu vào 1 (bắt buộc: Có); UI-STT 21 |
| 8 | Nút "Tiếp tục" | Nút chính | Nhấn | Vô hiệu nút; quá 1 giây thì hiện MSG-13 cạnh nút. Hệ thống kiểm tra theo thứ tự (ASM-23): có chỗ không còn trống --> hộp modal MSG-02 (luồng 4a); quá 5 chỗ --> banner MSG-03 tại SCR-02, giữ nguyên các chỗ đã chọn, bật lại nút (luồng 4b); chuyến đã đến giờ xuất bến --> hộp modal MSG-04 (luồng 4c); lỗi hệ thống --> MSG-14. Hợp lệ --> hệ thống giữ các chỗ và mở SCR-03 kèm các chỗ đang giữ (bước 5, E-03) | UC-009 bước 4, 4a, 4b, 4c, 5; BR-01, BR-02, BR-05; ASM-23; MSG-02, MSG-03, MSG-04, MSG-13, MSG-14 |
| 9 | Nút "Huỷ yêu cầu mua vé" | Nút phụ | Nhấn | Huỷ yêu cầu mua vé (luồng *a); chưa có chỗ nào được giữ nên không có chỗ cần trả; mở SCR-01 và hiển thị MSG-09 (E-05). Nút bị vô hiệu khi đang xử lý "Tiếp tục" | UC-009 bước *a; ASM-24; MSG-09; UI-STT 44 |
| 10 | Mục "Trang chủ" ở thanh trên | Liên kết | Nhấn | Xử lý như "Huỷ yêu cầu mua vé" (mục 9): về SCR-01 kèm MSG-09 (ASM-53, chờ Q-71) | ASM-53; UI-STT 34, 37 |
| 11 | Hộp thông điệp MSG-02 | Nút | Nhấn | Nút "Tìm lại chuyến" (cũng là Esc): đóng hộp và mở SCR-01 để tìm lại chuyến (E-05); các chỗ chưa được giữ | UC-009 bước 4a; MSG-02; UI-STT 40 |
| 12 | Hộp thông điệp MSG-04 | Nút | Nhấn | Nút "Về trang chủ" (cũng là Esc): đóng hộp và mở SCR-01 (E-05); use case kết thúc thất bại | UC-009 bước 4c; MSG-04; UI-STT 49 |
| 13 | Banner MSG-03 | Nút | Nhấn | Nút đóng "x": đóng banner, giữ nguyên các chỗ đã chọn để hành khách bỏ bớt chỗ (quay lại bước 3) | UC-009 bước 4b; MSG-03; UI-STT 48 |
| 14 | Hộp thông điệp MSG-14 | Nút | Nhấn | Nút "Đóng": đóng hộp, ở lại SCR-02, giữ nguyên các chỗ đã chọn | UI-STT 53; MSG-14 |
| 15 | Vùng thông điệp MSG-13 | Vùng hiển thị | Hết thời gian | Quá 1 giây từ khi nhấn "Tiếp tục": hiện chỉ báo xoay và MSG-13; quá 10 giây thêm câu "Việc này mất lâu hơn thường lệ" | NFR-08; UI-STT 43; MSG-13 |

## e) Định nghĩa thuộc tính trường

| Mục | Số ký tự tối đa | Kiểu | Thuộc tính trường | Ràng buộc dữ liệu | Ghi chú | Nguồn |
|---|---|---|---|---|---|---|
| Tuyến của chuyến | - | Chữ | Hiển thị; căn trái; chữ #1F2933 | Dạng "Điểm đi - Điểm đến" | Nhận từ UC-008 | P04 UC-009 Dữ liệu ra 1 STT 2; GL-22; UI-STT 13 |
| Giờ xuất bến của chuyến | 16 | Ngày | Hiển thị; căn trái; chữ #1F2933 | Định dạng dd/MM/yyyy HH:mm | Độ dài là của định dạng hiển thị | P04 UC-009 Dữ liệu ra 1 STT 2; GL-07; UI-STT 13 |
| Mã chỗ (nhãn của mỗi ô) | 5 | Chữ | Hiển thị; căn giữa trong ô 44 x 44 px; màu theo trạng thái (UI-STT 26) | Mã chỗ theo sơ đồ chỗ của loại xe, ví dụ A05 | Thiết kế: 5 ký tự đủ cho mã dạng chữ và hai chữ số (ví dụ A05) có dư, vì độ dài mã chỗ do danh mục xe (UC-021) quyết định | P04 UC-009 Dữ liệu vào 1 STT 1, Ví dụ; GL-01; C1 mục 7 |
| Trạng thái của chỗ | - | Lựa chọn | Hiển thị / Chọn; ba giá trị: Trống, Đã chọn, Không chọn được; mặc định Trống hoặc Không chọn được theo dữ liệu chuyến | Chỉ chỗ trống mới chọn được (BR-02) | Biểu diễn bằng màu, biểu tượng và tên đọc được (UI-STT 26) | P04 UC-009 Dữ liệu vào 1 STT 1, BR-02; GL-02 |
| Chỗ đã chọn | - | Lựa chọn | Chọn; bắt buộc; mặc định chưa chọn; danh sách mã chỗ căn trái | Từ 1 đến 5 chỗ (BR-01); mỗi chỗ còn trống, chưa có vé, chưa bị giữ cho yêu cầu khác (BR-02) | Kiểm tra số chỗ do hệ thống thực hiện sau khi gửi (MSG-03); giao diện chỉ bắt buộc chọn ít nhất một chỗ | P04 UC-009 Dữ liệu vào 1 STT 1, BR-01, BR-02 |
| Số chỗ đã chọn | - | Số | Hiển thị; căn trái | Số nguyên bằng số chỗ trong "Chỗ đã chọn" | Giá trị tính từ lựa chọn, không do hành khách nhập | P04 UC-009 Dữ liệu vào 1 STT 1 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Chỗ đã chọn | Khi chọn hoặc bỏ chọn một chỗ | Bắt buộc: có ít nhất một chỗ; chưa có chỗ thì nút "Tiếp tục" vô hiệu, không hiện lỗi | Không có (ngăn lỗi bằng nút vô hiệu, UI-STT 21) |
| Chỗ đã chọn | Khi nhấn "Tiếp tục" (hệ thống kiểm tra, ASM-23) | Quy tắc nghiệp vụ theo thứ tự: mọi chỗ còn trống (BR-02); số chỗ không quá 5 (BR-01); chuyến chưa đến giờ xuất bến (BR-05) | MSG-02; MSG-03; MSG-04 |
| Chỗ đã chọn | Khi nhấn "Tiếp tục" | Lỗi hệ thống | MSG-14 |

Không có trường nhập chữ nên không có kiểm tra định dạng hay miền giá trị.

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-02 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Vùng "Đã chọn" cập nhật ngay khi chọn; MSG-13 sau 1 giây khi kiểm tra và giữ chỗ | - |
| SCR-02 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Có "Huỷ yêu cầu mua vé" và mục "Trang chủ"; không có nút "Quay lại" vì SCR-02 là bước đầu sau UC-008 và đặc tả không có dịch chuyển lùi | - |
| SCR-02 | Nielsen 5 Ngăn lỗi | Đạt | Nút "Tiếp tục" vô hiệu khi chưa chọn chỗ; gợi ý "Chọn tối đa 5 chỗ"; chỗ không chọn được không bấm được | Giao diện không chặn chọn chỗ thứ 6 để luồng 4b còn đến được; hệ thống chặn bằng MSG-03 |
| SCR-02 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | MSG-02, MSG-03, MSG-04 nêu điều sai và việc cần làm; MSG-03 giữ các chỗ đã chọn | - |
| SCR-02 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Ba trạng thái chỗ khác nhau bằng viền, biểu tượng (dấu tick, gạch chéo) và chú giải chữ | - |
| SCR-02 | WCAG 1.4.11 Tương phản thành phần | Đạt | Viền chỗ trống #1F4E8C 2 px trên trắng 8,31:1; viền chỗ không chọn được #6B7280 trên nền ô #D5DAE0 là 3,44:1; chữ mã chỗ #52606D trên #D5DAE0 là 4,59:1 | - |
| SCR-02 | WCAG 2.1.1 Bàn phím | Đạt | Lưới chỗ một điểm dừng Tab, mũi tên di chuyển, Space chọn (UI-STT 41) | - |
| SCR-02 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Ô chỗ 44 x 44 px, khoảng cách 8 px | - |
| SCR-02 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | "Đã chọn" và MSG-03 khai báo role; MSG-02, MSG-04, MSG-14 là hộp modal giữ tiêu điểm | - |
| SCR-02 | Baymard: giữ nguyên dữ liệu đã nhập khi báo lỗi | Đạt | MSG-03 và MSG-14 giữ nguyên các chỗ đã chọn | - |
| SCR-02 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 1 đến 17, 18, 19, 27, 32, 34 đến 37, 39, 40, 43 đến 45, 47 đến 49, 53, 57 đến 64 | - |

## h) Thông điệp mới

Không có

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | - | - | Q-66 (cách nối UC-008 và luồng 4a) và Q-71 (nhấn "Trang chủ" khi đang mua vé) được nêu ở screen-transition.md và SCR-03 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | ASM-49 (screen-transition.md) và ASM-53 (SCR-03) được dẫn ở d) |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Không có | - | - | - |

## Vấn đề còn mở

- Bố cục lưới chỗ chỉ là minh hoạ một phần; số hàng, số cột và tầng của xe giường nằm 40 chỗ và xe ghế ngồi 29 chỗ do sơ đồ chỗ của loại xe quyết định (GL-19, UC-021 chưa có đặc tả).
- Cặp màu #6B7280 trên #D5DAE0 (3,44:1) và #52606D trên #D5DAE0 (4,59:1) gần ngưỡng, nên đo lại bằng công cụ khi dựng giao diện.
