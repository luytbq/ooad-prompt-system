# P07 - Phân tích use case UC-013 Lập lệnh điều chuyển - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-013-create-transfer-order.md 1.0; _BR-register.md; P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07 UC-005, UC-007, UC-009 1.0 (sổ đăng ký AC) |
| Phạm vi | UC-013 |

Placeholder: UC_ID = "UC-013 Lập lệnh điều chuyển"; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có.

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-013 Lập lệnh điều chuyển (Create Transfer Order) |
| Tác nhân chính | ACT-04 Nhân viên điều phối (Người) |
| Tác nhân phụ | Không có |
| Include, Được include bởi, Extend, Được extend bởi | Không có |
| File P07 đã có được dùng làm sổ đăng ký AC | UC-005, UC-007, UC-009 (12 mã AC; không mã nào trùng khái niệm của UC-013) |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Nhân viên điều phối | Yêu cầu lập lệnh điều chuyển. | Không đổi | REQ-44 |
| 2 | Nhân viên điều phối | Chỉ định trạm lấy xe, trạm nhận xe và xe cần điều chuyển. | Không đổi | REQ-44, Q-25 |
| 3 | Hệ thống | Tạo lệnh điều chuyển ở trạng thái chưa hoàn tất. | Hệ thống xác định hai trạm đã chỉ định, tạo lệnh điều chuyển gắn trạm lấy xe, trạm nhận xe và xe cần điều chuyển (số lượng hay danh sách chờ Q-25), trạng thái chưa hoàn tất. Hai trạm có được trùng nhau không chờ Q-33. | GL-09, GL-19 |

## F3. Tìm lớp phân tích

### F3.1 Boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-04 Nhân viên điều phối | Người | CreateTransferOrderForm | Giao diện người dùng | Mới (AC-B-CreateTransferOrderForm) | Cặp ACT-04 - UC-013 |

### F3.2 Lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Nhân viên điều phối | Bước 1 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-04 |
| 2 | Lệnh điều chuyển | Bước 1, 3 | Entity (AC-E-TransferOrder) | GL-09; được theo dõi ở UC-015, cập nhật ở UC-014 |
| 3 | Trạm lấy xe, trạm nhận xe | Bước 2 | Entity (AC-E-Station) | GL-19; hai vai trò của cùng khái niệm Trạm |
| 4 | Xe cần điều chuyển | Bước 2 | Loại - thuộc tính của TransferOrder | Số lượng hay danh sách chưa rõ (Q-25); nếu là danh sách xe cụ thể thì thành quan hệ tới AC-E-Bike |
| 5 | Trạng thái chưa hoàn tất | Bước 3 | Loại - thuộc tính của TransferOrder | GL-09 |
| 6 | Hệ thống | Bước 3 | Loại - mơ hồ | - |

### F3.3 Control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do |
|---|---|---|---|
| CreateTransferOrderController | UC-013 | Mới (AC-C-CreateTransferOrderController) | Use case ghi đơn giản một entity; A5 mặc định vẫn giữ control tối giản |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-CreateTransferOrderForm | boundary | CreateTransferOrderForm | // requestCreateTransferOrder: nhận yêu cầu lập lệnh<br>// specifyTransfer: nhận trạm lấy, trạm nhận, xe cần điều chuyển | fromStation<br>toStation<br>requestedBikes | 1, 2 | Giao diện người dùng | Mới | - |
| AC-C-CreateTransferOrderController | control | CreateTransferOrderController | // createTransferOrder: điều phối tạo lệnh | - | 3 | - | Mới | - |
| AC-E-Station | entity | Station | // findStation: xác định trạm theo chỉ định | name: Văn bản | 3 | - | Mới | GL-19 |
| AC-E-TransferOrder | entity | TransferOrder | // createTransferOrder: khởi tạo lệnh ở trạng thái chưa hoàn tất | status: Trạng thái<br>requestedBikes (Q-25) | 3 | - | Mới | GL-09 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestCreateTransferOrder | AC-B-CreateTransferOrderForm | Giao tiếp tác nhân | - |
| 2 | // specifyTransfer | AC-B-CreateTransferOrderForm | Giao tiếp tác nhân | - |
| 3 | // createTransferOrder | AC-C-CreateTransferOrderController | Controller | - |
| 3 | // findStation | AC-E-Station | Information Expert | - |
| 3 | // createTransferOrder | AC-E-TransferOrder | Creator | Control tạo vì có dữ liệu khởi tạo; không entity nào chứa lệnh điều chuyển |

## F5. Sequence diagram phân tích

### SD1 - Luồng chính

File diagrams/P07-sequence-UC-013.drawio.

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| A-04 | Actor | Nhân viên điều phối | - | - | ACT-04 |
| L-CTF | Lifeline | :CreateTransferOrderForm | «boundary» | - | AC-B-CreateTransferOrderForm |
| L-CTC | Lifeline | :CreateTransferOrderController | «control» | - | AC-C-CreateTransferOrderController |
| L-FS | Lifeline | from:Station | «entity» | - | AC-E-Station, trạm lấy xe |
| L-TS | Lifeline | to:Station | «entity» | - | AC-E-Station, trạm nhận xe |
| L-TO | Lifeline | :TransferOrder | «entity» | - | AC-E-TransferOrder |

| STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | A-04 | L-CTF | // requestCreateTransferOrder | Đồng bộ | - | 1 |
| 2 | A-04 | L-CTF | // specifyTransfer (trạm lấy xe, trạm nhận xe, xe cần điều chuyển) | Đồng bộ | - | 2 |
| 2.1 | L-CTF | L-CTC | // createTransferOrder (trạm lấy xe, trạm nhận xe, xe cần điều chuyển) | Đồng bộ | - | 3 |
| 2.1.1 | L-CTC | L-FS | // findStation (trạm lấy xe) | Đồng bộ | - | 3 |
| 2.1.2 | L-CTC | L-TS | // findStation (trạm nhận xe) | Đồng bộ | - | 3 |
| 2.1.3 | L-CTC | L-TO | // createTransferOrder (trạm lấy xe, trạm nhận xe, xe cần điều chuyển) | Tạo | - | 3 |

## F6. Quy tắc tương tác

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-013.drawio.

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| A-04 | Actor | Nhân viên điều phối | - | - | - |
| L-CTF | Object | :CreateTransferOrderForm | «boundary» | - | - |
| L-CTC | Object | :CreateTransferOrderController | «control» | - | - |
| L-FS | Object | from:Station | «entity» | - | - |
| L-TS | Object | to:Station | «entity» | - | - |
| L-TO | Object | :TransferOrder | «entity» | - | - |

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message |
|---|---|---|---|---|---|
| K01 | A-04 | L-CTF | Link | 1: // requestCreateTransferOrder (-->)<br>2: // specifyTransfer (-->) | Nguồn-->Đích |
| K02 | L-CTF | L-CTC | Link | 2.1: // createTransferOrder (-->) | Nguồn-->Đích |
| K03 | L-CTC | L-FS | Link | 2.1.1: // findStation (-->) | Nguồn-->Đích |
| K04 | L-CTC | L-TS | Link | 2.1.2: // findStation (-->) | Nguồn-->Đích |
| K05 | L-CTC | L-TO | Link | 2.1.3: // createTransferOrder (-->) | Nguồn-->Đích |

## F8. VOPC

File diagrams/P07-class-UC-013.drawio.

| ID (mã AC) | Loại | Nhãn | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-CreateTransferOrderForm | Class | CreateTransferOrderForm | boundary | - | fromStation<br>toStation<br>requestedBikes | // requestCreateTransferOrder<br>// specifyTransfer |
| AC-C-CreateTransferOrderController | Class | CreateTransferOrderController | control | - | - | // createTransferOrder |
| AC-E-Station | Class | Station | entity | - | name: Văn bản | // findStation |
| AC-E-TransferOrder | Class | TransferOrder | entity | - | status: Trạng thái<br>requestedBikes (Q-25) | // createTransferOrder |

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC013-01 | AC-B-CreateTransferOrderForm | AC-C-CreateTransferOrderController | Association | - | - | K02; tạm thời |
| R-UC013-02 | AC-C-CreateTransferOrderController | AC-E-Station | Association | - | - | K03, K04; tạm thời |
| R-UC013-03 | AC-C-CreateTransferOrderController | AC-E-TransferOrder | Association | - | - | K05; tạm thời |
| R-UC013-04 | AC-E-TransferOrder | AC-E-Station | Association | A 0..* - B 1 | - / fromStation | Bước 3; GL-09 "từ một trạm" |
| R-UC013-05 | AC-E-TransferOrder | AC-E-Station | Association | A 0..* - B 1 | - / toStation | Bước 3; GL-09 "tới trạm khác" |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1 | AC-B-CreateTransferOrderForm |
| 2 | 2 | AC-B-CreateTransferOrderForm |
| 3 | 2.1, 2.1.1, 2.1.2, 2.1.3 | AC-C-CreateTransferOrderController, AC-E-Station, AC-E-TransferOrder |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-33 | Trạm lấy xe và trạm nhận xe của một lệnh điều chuyển có được trùng nhau không? (Có / Không) | AC-E-TransferOrder, UC-013 bước 3 | Mục 9 "điều chuyển xe giữa các trạm" |

Liên quan: Q-09, Q-25.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-013 bước 3 | Không có bước hệ thống báo kết quả cho nhân viên điều phối sau khi tạo lệnh | Xét bổ sung "Hệ thống thông báo lệnh điều chuyển đã được tạo." nếu nguồn cho phép |

## Vấn đề còn mở

- AC-E-Station chỉ có trách nhiệm // findStation (truy vấn), thiếu trách nhiệm hành vi; UC-013 không có quy tắc nào trên dữ liệu trạm. Trách nhiệm hành vi của trạm (tỉ lệ ụ có xe, BR-14, BR-15) thuộc UC-012 chưa phân tích.
- Trách nhiệm // createTransferOrder cùng tên ở control và entity; giữ để truy vết message, P08 xử lý khi gộp.
