# P11a - screen-transition.md - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (Giai đoạn 1) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | screen-list.md 1.0; ui-standards.md 1.0; P04, P07 của UC-005, UC-013 |
| Phạm vi | SCR-01 đến SCR-04 |

File diagrams/P11a-screen-transition.drawio.

## a) Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| START-R | Start | Mở ứng dụng | - | ACT-01 | Tiền điều kiện UC-005: đã xác thực (UC-003 chưa phân tích) |
| SCR-01 | Screen | Màn hình chính người thuê xe | Độc lập | ACT-01 | Điều hướng |
| SCR-02 | Screen | Quét mã QR ụ khoá | Độc lập | ACT-01 | - |
| START-S | Start | Mở StaffWeb | - | ACT-04 | Tiền điều kiện UC-013: đã xác thực |
| SCR-03 | Screen | Màn hình chính nhân viên điều phối | Độc lập | ACT-04 | Điều hướng |
| SCR-04 | Screen | Lập lệnh điều chuyển | Độc lập | ACT-04 | - |

## b) Bảng Edge

| ID | Nguồn | Đích | Mẫu dịch chuyển | Sự kiện kích hoạt | Điều kiện | Dữ liệu truyền | UC bước |
|---|---|---|---|---|---|---|---|
| T-01 | START-R | SCR-01 | 1 Đơn giản | Mở ứng dụng | Đã xác thực | - | UC-005 tiền điều kiện |
| T-02 | SCR-01 | SCR-02 | 1 Đơn giản | Nhấn "Thuê xe" | - | - | UC-005 bước 1 |
| T-03 | SCR-02 | SCR-01 | 1 Đơn giản | Nhấn "Quay lại" | - | - | Chuẩn mục 4 (nút Quay lại trên thanh tiêu đề) |
| T-04 | START-S | SCR-03 | 1 Đơn giản | Mở StaffWeb | Đã xác thực | - | UC-013 tiền điều kiện |
| T-05 | SCR-03 | SCR-04 | 1 Đơn giản | Chọn "Lập lệnh điều chuyển" | - | - | UC-013 bước 1 |
| T-06 | SCR-04 | SCR-03 | 1 Đơn giản | Nhấn "Quay lại" | - | - | Chuẩn mục 5 |

Hộp thông điệp MSG-01 đến MSG-05 dùng hộp thoại chuẩn, không có mã SCR và không vẽ trên sơ đồ.

## Câu hỏi mở

Không có câu hỏi mới. Liên quan: Q-37 (màn hình sau khi quét thành công).

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Sau khi quét mã thành công, người thuê xe ở lại SCR-02 vì đặc tả không có phản hồi thành công (Q-37). Nếu Q-37 trả lời Có, cần màn hình "Chuyến đi đang diễn ra" và dịch chuyển mẫu 4 từ SCR-02.
- Sơ đồ chỉ có mẫu 1 vì 4 use case đã phân tích không có pop-up hoặc màn hình phụ thuộc dữ liệu.
