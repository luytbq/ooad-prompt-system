# P04 - Đặc tả use case UC-007 Trả xe - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-dap.md; P00 1.0; P01 1.0; P02 1.0; P03 1.0 (Mục 1, Mục 2); _BR-register.md (sau UC-005); UC-005-rent-bike.md (Câu hỏi mở) |
| Phạm vi | UC-007 |

Placeholder: UC_ID = UC-007; TEN_HE_THONG_TRONG_LUONG = Không có; YEU_CAU_BO_SUNG = Không có.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-007 |
| Tên use case | Trả xe (Return Bike) |
| Tác nhân chính | ACT-01 Người thuê xe |
| Tác nhân phụ | ACT-08 Ụ khoá; ACT-07 Cổng thanh toán |
| Mô tả ngắn | Use case này mô tả tương tác giữa người thuê xe và hệ thống khi người thuê xe muốn kết thúc chuyến đi bằng cách trả xe vào một ụ khoá. Kết quả là cước được thu từ tiền tạm giữ, phần dư được hoàn và hoá đơn được gửi. |
| Sự kiện kích hoạt | Ụ khoá báo đã nhận xe (EV-07) |
| Tiền điều kiện | Xe thuộc một chuyến đi đang diễn ra của người thuê xe.<br>Chuyến đi có khoản tạm giữ còn hiệu lực. |
| Hậu điều kiện (thành công) | Chuyến đi ở trạng thái đã kết thúc, có thời điểm kết thúc và ụ khoá trả.<br>Cước của chuyến được thu từ khoản tạm giữ; phần tạm giữ còn dư được hoàn.<br>Hoá đơn chuyến đi đã được gửi qua email. |
| Hậu điều kiện tối thiểu | Chưa quy định (Q-23) |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-17, REQ-18, REQ-19, REQ-20, REQ-21, REQ-22, REQ-23, REQ-24, REQ-11, REQ-62, REQ-63 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Người thuê xe | Đẩy xe vào một ụ khoá trống ở trạm bất kỳ (BR-08). |
| 2 | Ụ khoá | Nhận diện xe và báo đã nhận xe. |
| 3 | Hệ thống | Kết thúc chuyến đi của xe. |
| 4 | Hệ thống | Tính cước chuyến đi theo thời lượng (BR-07). |
| 5 | Hệ thống | Yêu cầu Cổng thanh toán thu cước từ khoản tạm giữ. |
| 6 | Hệ thống | Yêu cầu Cổng thanh toán hoàn lại phần tạm giữ còn dư. |
| 7 | Hệ thống | Gửi hoá đơn chuyến đi cho người thuê xe qua email (Q-19). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 4a | Cước lớn hơn số tiền tạm giữ (BR-05, BR-07) | - | Chưa quy định (Q-02) | Chưa quy định (Q-02) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu ra 1 (bước 7): Hoá đơn chuyến đi.

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Chưa quy định (Q-24) | Nguồn chỉ nêu "gửi hoá đơn qua email" | Chưa quy định (Q-24) | - |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-05 | Số tiền tạm giữ cho mỗi lần thuê xe là 200.000 đồng. | Sự kiện | 4a | REQ-11 | Đã có |
| BR-07 | Cước chuyến đi miễn phí 30 phút đầu, sau đó 5.000 đồng cho mỗi 15 phút hoặc phần lẻ của 15 phút. | Tính toán | 4 | REQ-21 | Mới |
| BR-08 | Người thuê xe được trả xe vào một ụ trống bất kỳ ở bất kỳ trạm nào. | Sự kiện | 1 | REQ-17 | Mới |

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Thời gian miễn phí cộng thêm của UC-006 (REQ-26) có thể ảnh hưởng BR-07; cách cộng chờ Q-05.
- Người thuê xe có thể báo xe hỏng ngay khi trả xe (UC-008, REQ-33); P03 không có quan hệ giữa hai UC.
- Ví dụ áp dụng BR-07: chuyến 47 phút có 17 phút tính cước, tức 2 đơn vị 15 phút (15 phút và phần lẻ 2 phút), cước 10.000 đồng.

## 8a. Kịch bản chính

- KB1: Luồng chính --> chuyến kết thúc, thu cước, hoàn dư, gửi hoá đơn.
- KB2: Luồng chính + 4a --> chưa quy định (Q-02).

## 9. Activity diagram

File: diagrams/P04-activity-UC-007.drawio

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú |
|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Người thuê xe | - | - | - | x=0, w=280, h=880 |
| P-SYS | Partition | Hệ thống | - | - | - | x=280, w=520, h=880 |
| P-ACT-08 | Partition | Ụ khoá | - | - | - | x=800, w=280, h=880 |
| INIT | Initial | - | - | P-ACT-01 | - | - |
| A-1 | Action | Đẩy xe vào ụ khoá trống | - | P-ACT-01 | 1 | - |
| A-2 | Action | Nhận diện xe, báo đã nhận xe | - | P-ACT-08 | 2 | - |
| A-3 | Action | Kết thúc chuyến đi | - | P-SYS | 3 | - |
| A-4 | Action | Tính cước chuyến đi | - | P-SYS | 4 | - |
| N-4a | Note | 4a: cước lớn hơn tiền tạm giữ: chưa quy định (Q-02) | - | P-SYS | 4a | - |
| A-5 | Action | Thu cước từ khoản tạm giữ | - | P-SYS | 5 | - |
| A-6 | Action | Hoàn phần tạm giữ còn dư | - | P-SYS | 6 | - |
| A-7 | Action | Gửi hoá đơn qua email | - | P-SYS | 7 | - |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | Vượt partition | (140,200); (940,200) |
| E-03 | A-2 | A-3 | ControlFlow | - | Vượt partition | (940,300); (410,300) |
| E-04 | A-3 | A-4 | ControlFlow | - | - | - |
| E-05 | A-4 | A-5 | ControlFlow | - | - | - |
| E-06 | A-5 | A-6 | ControlFlow | - | - | - |
| E-07 | A-6 | A-7 | ControlFlow | - | - | - |
| E-08 | A-7 | FINAL-1 | ControlFlow | - | - | - |
| E-09 | N-4a | A-4 | NoteLink | - | - | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 3 | A-3 |
| 4 | A-4 |
| 4a | N-4a |
| 5 | A-5 |
| 6 | A-6 |
| 7 | A-7 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-23 | Khi cổng thanh toán không thu được cước, không hoàn được phần dư hoặc không thu được tạm giữ, hệ thống xử lý thế nào: (a) ghi nợ cước cho tài khoản; (b) thử lại; (c) chuyển nhân viên chăm sóc khách hàng? | UC-007 bước 5, 6, hậu điều kiện tối thiểu; UC-009 bước 3 | Mục 4, Mục 14 không nêu |
| Q-24 | Hoá đơn chuyến đi gồm những thông tin nào (ví dụ thời điểm thuê, trả, trạm, thời lượng, cước)? | UC-007 Dữ liệu ra 1 | "gửi hoá đơn qua email" (Mục 4) |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Luồng 4a có điều kiện suy ra trực tiếp từ BR-05 và BR-07 (chuyến dài hơn khoảng 8 giờ 45 phút có cước vượt 200.000 đồng) nhưng cách xử lý chờ Q-02. F5 không có mẫu cho luồng thay thế có điều kiện nhưng chưa có hành động và điểm kết thúc; đã ghi "Chưa quy định (Q-02)" ở hai cột. Activity diagram không vẽ decision cho 4a (không có đích hợp lệ), chỉ gắn note N-4a vào A-4; vì vậy Target mục 13 (mỗi luồng thay thế là một nhánh từ decision) không đạt.
- Không có luồng cho trường hợp xe thuộc chuyến đã bị coi là thất lạc được trả vào ụ (Q-04).
- Bước 1 là thao tác của người thuê xe trên ụ khoá, không phải trên hệ thống; bước 2 do ụ khoá thực hiện. Tác nhân chính theo P02 (xem P02 Vấn đề còn mở).
