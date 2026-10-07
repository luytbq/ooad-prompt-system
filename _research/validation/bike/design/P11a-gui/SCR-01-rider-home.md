# P11a - SCR-01-rider-home.md - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (Giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | ui-standards.md, screen-list.md, screen-transition.md 1.0; P02; P04 UC-005 |
| Phạm vi | SCR-01 |

Placeholder: CHE_DO_CHAY = "Giai đoạn 2: các màn hình của UC-005, UC-007"; các placeholder khác như Giai đoạn 1.

## a) Bảng đầu trang

| Tên hệ thống | Mã và tên màn hình | Ngày tạo | Người duyệt | Người kiểm tra | Người phụ trách |
|---|---|---|---|---|---|
| Hệ thống cho thuê xe đạp công cộng CityBike | SCR-01 Màn hình chính người thuê xe | | | | |

## b) Thông tin chung

| Mục | Giá trị |
|---|---|
| SCR | SCR-01 |
| UC | Điều hướng: UC-005 |
| Tác nhân | ACT-01 |
| Boundary AC | Điều hướng |
| DC | - |
| Loại | Độc lập |
| Đến từ | START-R (T-01), SCR-02 (T-03) |
| Đi tới | SCR-02 (T-02) |

## c) Hình ảnh màn hình

```text
+------------------------------------+
|        CityBike               [?]  |
|------------------------------------|
|                                    |
|   Lối vào các chức năng            |
|                                    |
|   +----------------------------+   |
|   |  [icon QR]  Thuê xe        |   |
|   +----------------------------+   |
|                                    |
|   (Lối vào UC-001 đến UC-008       |
|    khác bổ sung khi có P07)        |
|                                    |
+------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Tiêu đề | "CityBike", nút Trợ giúp | Trên, cao 56 dp | Chuẩn mục 4, 25 |
| Nội dung | Thẻ lối vào "Thuê xe" | Giữa | Thẻ cao 72 dp, vùng bấm toàn thẻ |

## d) Danh sách chức năng

| STT | Điều khiển | Loại | Thao tác | Chức năng | Nguồn |
|---|---|---|---|---|---|
| 1 | Màn hình | - | Khởi tạo | Hiển thị lối vào các use case của ACT-01 đã phân tích | P02 (ACT-01) |
| 2 | Thẻ "Thuê xe" | Liên kết | Nhấn | Mở SCR-02 | UC-005 bước 1; T-02 |
| 3 | Nút "?" | Nút | Nhấn | Mở trang hướng dẫn của màn hình | Chuẩn mục 25 |

## e) Định nghĩa thuộc tính trường

Không có trường dữ liệu nghiệp vụ.

## f) Kiểm tra dữ liệu nhập

Không có trường nhập.

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-01 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Lối vào có biểu tượng và chữ | - |
| SCR-01 | WCAG 2.5.8 Vùng bấm | Đạt | Thẻ 72 dp | - |
| SCR-01 | WCAG 1.1.1 | Đạt | Biểu tượng QR có văn bản thay thế "Thuê xe" | - |

## Câu hỏi mở

Không có

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Màn hình điều hướng chỉ có một lối vào vì chỉ UC-005 của ACT-01 có dịch chuyển trong phạm vi; UC-007 không có màn hình.
