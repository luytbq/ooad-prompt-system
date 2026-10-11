# P11a - SCR-04 Vé đã phát hành - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0); P04-uc-specs/UC-009-book-ticket-online.md (luồng sự kiện, bảng dữ liệu vào ra, BR, Câu hỏi mở, Giả định); P05-glossary.md (GL-05, GL-15, GL-23); P06-supplementary-spec.md (BR-04); P07-uc-analysis/UC-009 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng AC-B-BookTicketOnlineForm); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4). Placeholder: CHE_DO_CHAY = Giai đoạn 2: các màn hình của UC-009, UC-017; THIET_BI_HIEN_THI, NHAN_DIEN_THUONG_HIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có, XUAT_HTML = Không, THONG_TIN_TAI_LIEU = Không có, YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét trước lần chạy: Q-69, ASM-51 |
| Phạm vi | SCR-04 (UC-009 bước 12, kết quả của bước 9 đến 11) |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 |

## a) Thông tin tài liệu

Không có (THONG_TIN_TAI_LIEU = Không có, MAU_DAC_TA_MAN_HINH = Không có; dùng mẫu F5).

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-04 Vé đã phát hành (Issued tickets) |
| UC | UC-009 Đặt vé trực tuyến |
| Bước UC | 12 (kết quả của bước 9 đến 11, kể cả luồng 11a) |
| Tác nhân | ACT-01 Hành khách |
| Boundary AC | AC-B-BookTicketOnlineForm |
| DC | DC-BookTicketOnlineView (tiếp nhận thao tác: DC-BookTicketOnlineRequestHandler) |
| Loại màn hình | Phụ thuộc có dữ liệu (nhận "Các vé đã phát hành" từ SCR-03, E-04) |
| Đến từ | SCR-03 (E-04, mẫu 4, "Các vé đã phát hành") |
| Đi tới | SCR-01 (E-07, mẫu 1: "Về trang chủ", menu "Trang chủ"). Đây là màn hình kết thúc thành công của UC-009 |
| Nền tảng | Website cho hành khách, máy tính từ 1280 x 720 px và điện thoại từ 360 x 640 px (UI-STT 1) |

## c) Hình ảnh màn hình

```text
+------------------------------------------------------------------------+
| SaoViet Bus                                              [ Trang chủ ] |
|------------------------------------------------------------------------|
| Vé đã phát hành                                                        |
| [ vùng thông điệp: trống ]                                             |
|                                                                        |
| Chuyến                          Người đi                               |
| Hà Nội - Vinh, 15/12/2026 20:30 Nguyễn Văn An                          |
|                                                                        |
| +-----------+--------+--------------+                                  |
| | Mã vé     | Chỗ    |      Giá vé  |                                  |
| +-----------+--------+--------------+                                  |
| | SV0001    | A05    |    250.000 đ |                                  |
| | SV0002    | A06    |    250.000 đ |                                  |
| +-----------+--------+--------------+                                  |
|                         Tổng tiền:      500.000 đ                      |
|------------------------------------------------------------------------|
|                                              [ Về trang chủ ]          |
+------------------------------------------------------------------------+
```

Trên điện thoại (dưới 600 px) mỗi vé thành một thẻ có nhãn cột đứng trước giá trị (UI-STT 25); nút "Về trang chủ" rộng toàn chiều ngang (UI-STT 9).

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh trên | Tên hệ thống "SaoViet Bus", mục "Trang chủ" | Trên cùng, cao 56 px | UI-STT 7, 34, 35 |
| Tiêu đề | "Vé đã phát hành" (tiêu đề cấp 1) | Dưới thanh trên | UI-STT 12 |
| Thông điệp | Hộp modal MSG-14 (nếu có lỗi hệ thống) | Giữa màn hình | UI-STT 47, 53 |
| Nội dung - chuyến và người đi | Tuyến, giờ xuất bến, họ tên người đi | Đầu vùng nội dung | Mục chi tiết chỉ đọc (UI-STT 14) |
| Nội dung - bảng vé | Mỗi vé một dòng: mã vé, chỗ, giá vé; dòng tổng tiền | Giữa vùng nội dung | Giá vé căn phải (UI-STT 13, 25) |
| Hành động | "Về trang chủ" (nút chính) | Cuối nội dung, căn phải | UI-STT 8, 18, 49 |

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Màn hình | Vùng hiển thị | Khởi tạo | Hiển thị tiêu đề cấp 1 "Vé đã phát hành"; tiêu điểm đặt ở tiêu đề (UI-STT 32). Tiêu đề trang trình duyệt là "Vé đã phát hành - SaoViet Bus" | UC-009 bước 12; UI-STT 12, 32 |
| 2 | Vùng "Chuyến" | Vùng hiển thị | Khởi tạo | Hiển thị tuyến và giờ xuất bến của chuyến, dạng "Hà Nội - Vinh, 15/12/2026 20:30" | UC-009 bước 12, Dữ liệu ra 1 STT 2 |
| 3 | Vùng "Người đi" | Vùng hiển thị | Khởi tạo | Hiển thị họ tên người đi đã nhập ở bước 6 | UC-009 Dữ liệu ra 1 STT 4 |
| 4 | Bảng vé | Bảng | Khởi tạo | Hiển thị mỗi vé đã phát hành một dòng gồm mã vé, chỗ, giá vé theo cùng thứ tự mã vé và chỗ. Hiển thị cả khi SMS mã vé không gửi được (luồng 11a, ASM-20); màn hình không báo việc SMS chưa gửi được (Q-67) | UC-009 bước 12, 11a, Dữ liệu ra 1 STT 1, 3, 5; BR-04; ASM-20; Q-67 |
| 5 | Dòng "Tổng tiền" | Vùng hiển thị | Khởi tạo | Hiển thị tổng giá vé của các vé trong lần đặt, bằng tổng các dòng giá vé, dạng "500.000 đ" | UC-009 bước 12, Dữ liệu ra 1 STT 6; UI-STT 13 |
| 6 | Nút "Về trang chủ" | Nút chính | Nhấn | Mở SCR-01; use case UC-009 kết thúc thành công (E-07) | UC-009 bước 12; UI-STT 49 |
| 7 | Mục "Trang chủ" ở thanh trên | Liên kết | Nhấn | Mở SCR-01, như nút "Về trang chủ" (E-07). Các vé đã phát hành, nên không có chỗ nào cần trả lại | UI-STT 34, 37 |
| 8 | Hộp thông điệp MSG-14 | Nút | Nhấn | Nút "Đóng": đóng hộp, ở lại SCR-04 (xuất hiện khi lỗi hệ thống xảy ra lúc tải màn hình) | UI-STT 53; MSG-14 |

## e) Định nghĩa thuộc tính trường

| Mục | Số ký tự tối đa | Kiểu | Thuộc tính trường | Ràng buộc dữ liệu | Ghi chú | Nguồn |
|---|---|---|---|---|---|---|
| Mã vé | 10 | Chữ | Hiển thị; căn trái; chữ #1F2933; mỗi vé một dòng | Mỗi chỗ một mã vé (BR-04); hiển thị đúng như hệ thống cấp, ví dụ SV0001 | Thiết kế: 10 ký tự đủ cho tiền tố và dãy số của ví dụ SV0001 có dư để dãy số mở rộng (C3 cho phép mở rộng); phạm vi duy nhất của mã vé do P12 quyết định | P04 UC-009 Dữ liệu ra 1 STT 1, BR-04; GL-15; C1 mục 7 |
| Chỗ | 5 | Chữ | Hiển thị; căn trái; cùng thứ tự với mã vé | Mã chỗ của từng vé, ví dụ A05 | Thiết kế: cùng độ dài với mã chỗ ở SCR-02 | P04 UC-009 Dữ liệu ra 1 STT 3 |
| Tuyến của chuyến | - | Chữ | Hiển thị; căn trái | Dạng "Điểm đi - Điểm đến" | Độ dài theo giá trị | P04 UC-009 Dữ liệu ra 1 STT 2; GL-22; UI-STT 13 |
| Giờ xuất bến của chuyến | 16 | Ngày | Hiển thị; căn trái | Định dạng dd/MM/yyyy HH:mm | Độ dài của định dạng hiển thị | P04 UC-009 Dữ liệu ra 1 STT 2; GL-07; UI-STT 13 |
| Họ tên người đi | 100 | Chữ | Hiển thị; căn trái | Họ tên đã nhập ở bước 6 | Cùng độ dài với ô nhập ở SCR-03 (ASM-52) | P04 UC-009 Dữ liệu ra 1 STT 4; ASM-52 |
| Giá vé | 13 | Tiền | Hiển thị; căn phải; mỗi vé một dòng | Số nguyên đồng, phân cách hàng nghìn bằng dấu chấm, kèm " đ" | Thiết kế: 13 ký tự đủ cho "999.999.999 đ"; giá vé do UC-023, UC-024 cung cấp | P04 UC-009 Dữ liệu ra 1 STT 5; GL-05; UI-STT 13 |
| Tổng tiền | 13 | Tiền | Hiển thị; căn phải; chữ đậm | Bằng tổng giá vé các vé trong lần đặt (ví dụ 2 x 250.000 = 500.000 đ); chỉ cộng các khoản đồng | Thiết kế: cùng độ dài với Giá vé | P04 UC-009 Dữ liệu ra 1 STT 6, mục 8; UI-STT 13 |

## f) Kiểm tra dữ liệu nhập

Không có trường nhập. Màn hình chỉ hiển thị kết quả.

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có | - | - | MSG-14 khi lỗi hệ thống lúc tải màn hình |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-04 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Tiêu đề "Vé đã phát hành" và bảng mã vé cho hành khách biết kết quả | - |
| SCR-04 | Nielsen 2 Khớp giữa hệ thống và thế giới thực | Đạt | Dùng "vé", "mã vé", "chỗ", "người đi" theo glossary; tiền ghi "250.000 đ" | - |
| SCR-04 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | Khi SMS mã vé không gửi được (luồng 11a), màn hình không báo cho hành khách nên hành khách có thể chờ SMS không bao giờ đến | Q-67; chưa thêm dòng thông tin vì đặc tả không nêu |
| SCR-04 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Bảng vé dùng th có scope; dòng tổng tiền có nhãn "Tổng tiền" | - |
| SCR-04 | WCAG 3.2.4 Định danh nhất quán | Đạt | Nút "Về trang chủ" cùng nhãn và cùng đích với mục "Trang chủ" | - |
| SCR-04 | WCAG 1.4.10 Reflow | Đạt | Bảng chuyển thành thẻ dưới 600 px (UI-STT 25) | - |
| SCR-04 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 1 đến 17, 18, 27, 32, 33 đến 37, 45, 47, 49, 53, 57 đến 64 | - |

## h) Thông điệp mới

Không có

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | - | - | Q-67 (báo SMS chưa gửi được trên SCR-04) đã có ở screen-list.md |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | ASM-20, ASM-52 được dẫn ở d), e) |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Không có | - | - | - |

## Vấn đề còn mở

- Q-67 chưa có trả lời nên F7 Nielsen 9 là Vi phạm còn mở.
- Mã vé hiển thị cho từng vé nhưng chuyến và người đi hiển thị một lần vì P04 ASM-19 quy định một người đi chung cho cả lần đặt.
