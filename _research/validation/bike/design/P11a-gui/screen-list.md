# P11a - screen-list.md - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (Giai đoạn 1) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | Như ui-standards.md |
| Phạm vi | Boundary giao diện người dùng trong P08 (3 boundary) |

| SCR | Tên | Boundary AC nguồn | UC | Tác nhân | Loại | Lớp thiết kế (DC) | Mục đích | Bước UC phục vụ |
|---|---|---|---|---|---|---|---|---|
| SCR-01 | Màn hình chính người thuê xe (Rider home) | Điều hướng: UC-005 (các UC khác của ACT-01 chưa phân tích) | UC-005 | ACT-01 | Độc lập | - | Chọn use case | - |
| SCR-02 | Quét mã QR ụ khoá (Scan dock QR) | AC-B-RentBikeForm | UC-005 | ACT-01 | Độc lập | DC-RentBikeScreen, DC-RentBikeViewModel | Quét mã QR để thuê xe; nhận báo từ chối | 1, 2a, 2b, 2c, 3a, 5a |
| SCR-03 | Màn hình chính nhân viên điều phối (Dispatcher home) | Điều hướng: UC-013 | UC-013 | ACT-04 | Độc lập | - | Chọn use case | - |
| SCR-04 | Lập lệnh điều chuyển (Create transfer order) | AC-B-CreateTransferOrderForm | UC-013 | ACT-04 | Độc lập | DC-CreateTransferOrderPage | Chỉ định trạm lấy, trạm nhận, xe | 1, 2 |

AC-B-ReturnBikeForm (UC-007) không có màn hình: P10 ánh xạ boundary này sang SS-03 EmailSubsystem, kênh là email (Q-19). Hoá đơn là nội dung email, không phải màn hình.

## Tổng hợp đánh giá (F7)

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-02 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Sau khi quét, người thuê xe không biết ụ đã mở, chuyến đã bắt đầu hay hết 60 giây | Q-37; không tự thêm thông báo |
| SCR-02 | WCAG 3.3.4 Ngăn lỗi với dữ liệu tài chính | Vi phạm còn mở | Quét mã dẫn tới tạm giữ 200.000 đồng không qua xác nhận | Q-38 |
| SCR-02 | WCAG 2.5.7, 1.1.1 (camera không dùng được) | Vi phạm đã sửa | Người dùng không dùng được camera | Thêm "Nhập mã ụ" không được vì ngoài đặc tả; ghi Q-39; hiện hướng dẫn bằng chữ và văn bản thay thế cho khung camera |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-39 | Khi không quét được mã QR (camera hỏng, mã mờ, người dùng khiếm thị), người thuê xe có cách nhập mã ụ khoá thay thế không? (Có / Không) | SCR-02, WCAG | Mục 3 chỉ nêu quét mã QR |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 2 không đạt cho AC-B-ReturnBikeForm: P11a A2 lấy boundary người dùng từ P08, còn P10 đã ánh xạ boundary này sang subsystem email.
- SCR-01, SCR-03 chỉ có một lối vào vì chỉ UC-005, UC-013 đã phân tích.
