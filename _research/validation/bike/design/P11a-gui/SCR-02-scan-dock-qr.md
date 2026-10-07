# P11a - SCR-02-scan-dock-qr.md - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (Giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | ui-standards.md, screen-list.md, screen-transition.md 1.0; P04 UC-005; P07 UC-005; P05; P06; P10 |
| Phạm vi | SCR-02 |

Placeholder: CHE_DO_CHAY = "Giai đoạn 2: các màn hình của UC-005, UC-007"; XUAT_HTML = "Có".

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống cho thuê xe đạp công cộng CityBike | SCR-02 Quét mã QR ụ khoá | | | | |

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-02 |
| UC, bước | UC-005 bước 1, 2a, 2b, 2c, 3a, 5a |
| Tác nhân | ACT-01 Người thuê xe |
| Boundary AC | AC-B-RentBikeForm |
| DC | DC-RentBikeScreen, DC-RentBikeViewModel |
| Loại | Độc lập |
| Đến từ | SCR-01 (T-02) |
| Đi tới | SCR-01 (T-03) |

## c) Hình ảnh màn hình

```text
+------------------------------------+
| [<]   Thuê xe                 [?]  |
|------------------------------------|
|  Hướng camera vào mã QR dán        |
|  trên ụ khoá.                      |
|  +------------------------------+  |
|  |                              |  |
|  |     [ khung camera ]         |  |
|  |       +----------+           |  |
|  |       |  vùng QR |           |  |
|  |       +----------+           |  |
|  |                              |  |
|  +------------------------------+  |
|  Khi quét, hệ thống tạm giữ        |
|  200.000 đ trên thẻ đã liên kết.   |
+------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Tiêu đề | Nút Quay lại, "Thuê xe", Trợ giúp | Trên | Chuẩn mục 4 |
| Hướng dẫn | Câu hướng dẫn quét | Dưới tiêu đề | Nielsen 10 |
| Nội dung | Khung camera có vùng ngắm | Giữa | Văn bản thay thế "Khung camera quét mã QR ụ khoá" |
| Thông tin | Số tiền tạm giữ | Đáy | BR-05; Nielsen 1 (báo trước hệ quả tài chính, không thêm bước xác nhận: Q-38) |

Mockup: P11a-gui/mockups/SCR-02-scan-dock-qr.html

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Màn hình | - | Khởi tạo | Xin quyền camera nếu chưa có, bật khung camera, hiển thị câu hướng dẫn và số tiền tạm giữ 200.000 đ | UC-005 bước 1; BR-05 |
| 2 | Khung camera | Vùng hiển thị | Quét được mã | Kiểm tra định dạng mã QR của ụ; sai định dạng thì hiện MSG-04. Đúng định dạng thì gửi yêu cầu thuê xe (mã QR) và hiện MSG-01 tới khi có kết quả | UC-005 bước 1, 2; // scanDockQrCode; MSG-01, MSG-04 |
| 3 | Khung camera | Vùng hiển thị | Nhận kết quả từ chối điều kiện tài khoản hoặc xe | Hiện MSG-02; đóng hộp thì bật lại camera | UC-005 bước 2a, 2b, 2c, 3a; // showRentalRejected |
| 4 | Khung camera | Vùng hiển thị | Nhận kết quả tạm giữ không thành công | Hiện MSG-03 | UC-005 bước 5a |
| 5 | Khung camera | Vùng hiển thị | Lỗi kết nối | Hiện MSG-05, giữ màn hình | Chuẩn mục 24 |
| 6 | Khung camera | Vùng hiển thị | Nhận kết quả thành công | Chưa quy định (Q-37); tắt MSG-01 | UC-005 bước 6 đến 8 |
| 7 | Nút "<" Quay lại | Nút | Nhấn | Mở SCR-01; không cho nhấn khi MSG-01 đang hiện | T-03; chuẩn mục 20 |
| 8 | Nút "?" | Nút | Nhấn | Mở trang hướng dẫn quét mã | Chuẩn mục 25 |

## e) Định nghĩa thuộc tính trường

| Mục | Số ký tự tối đa | Kiểu | Thuộc tính trường | Ràng buộc dữ liệu | Ghi chú | Nguồn |
|---|---|---|---|---|---|---|
| Mã QR ụ khoá (dockQrCode) | Chưa quy định (Q-40) | Chữ | Nhập qua camera; bắt buộc; không hiển thị | Định dạng mã QR của ụ: chưa quy định (Q-40) | Người dùng không nhìn thấy giá trị | GL-11; P04 UC-005 mục 5 (không có bảng dữ liệu) |
| Số tiền tạm giữ | 9 | Tiền | Hiển thị; căn trái | 200.000 đ | Hiển thị "200.000 đ" | BR-05 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Mã QR ụ khoá | Ngay khi quét được | 1 Bắt buộc: có mã. 2 Định dạng: là mã ụ khoá CityBike (Q-40). 3 Quy tắc nghiệp vụ (BR-01 đến BR-04, tạm giữ): máy chủ trả về | MSG-04; MSG-02; MSG-03 |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-02 | Nielsen 1 Hiển thị trạng thái | Vi phạm còn mở | Không có phản hồi khi ụ mở, khi chuyến bắt đầu | Q-37 |
| SCR-02 | Nielsen 9 Khắc phục lỗi | Vi phạm còn mở | MSG-02 không nói lý do từ chối | Q-22 |
| SCR-02 | WCAG 3.3.4 Ngăn lỗi tài chính | Vi phạm đã sửa một phần | Thêm dòng báo trước số tiền tạm giữ; không thêm bước xác nhận | Q-38 |
| SCR-02 | WCAG 1.1.1, 2.5.7 | Vi phạm còn mở | Chỉ có cách nhập bằng camera | Q-39 |
| SCR-02 | WCAG 4.1.3 Thông báo trạng thái | Đạt | MSG-01 trong vùng live | - |
| SCR-02 | Material 48 dp | Đạt | Nút Quay lại, Trợ giúp 48 x 48 dp | - |
| SCR-02 | NFR-02 (2 giây) | Không áp dụng cho giao diện | Thời gian đo từ quét tới ụ nhận lệnh | P09 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-40 | Mã QR dán trên ụ khoá có định dạng và độ dài nào (ví dụ URL, mã ụ)? | SCR-02 mục e, P11b | Mục 3; hồ sơ dự án "chưa có tài liệu giao thức" |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-005 | Không có bước phản hồi cho người thuê xe khi thành công | Sau khi có câu trả lời Q-37, bổ sung bước "Hệ thống thông báo ụ đã mở khoá" và "Hệ thống thông báo chuyến đi đã bắt đầu" |

## Vấn đề còn mở

- Target 6: bảng dữ liệu vào ra P04 UC-005 là "Không có"; thuộc tính mã QR lấy từ GL-11 và trách nhiệm boundary.
