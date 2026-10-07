# P04 - Đặc tả use case UC-005 Thuê xe - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-dap.md; P00 1.0; P01 1.0; P02 1.0; P03 1.0 (Mục 1, Mục 2) |
| Phạm vi | UC-005 |

Placeholder: UC_ID = UC-005; TEN_HE_THONG_TRONG_LUONG = Không có (dùng "Hệ thống"); YEU_CAU_BO_SUNG = Không có.

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-005 |
| Tên use case | Thuê xe (Rent Bike) |
| Tác nhân chính | ACT-01 Người thuê xe |
| Tác nhân phụ | ACT-07 Cổng thanh toán; ACT-08 Ụ khoá |
| Mô tả ngắn | Use case này mô tả tương tác giữa người thuê xe và hệ thống khi người thuê xe muốn lấy một xe tại trạm. Kết quả là chuyến đi bắt đầu với 200.000 đồng được tạm giữ trên thẻ. |
| Sự kiện kích hoạt | Người thuê xe tại trạm muốn lấy xe (EV-04) |
| Tiền điều kiện | Người thuê xe đã được xác thực. |
| Hậu điều kiện (thành công) | Có một chuyến đi đang diễn ra gắn với tài khoản của người thuê xe và xe vừa được rút khỏi ụ khoá.<br>Khoản tạm giữ 200.000 đồng trên thẻ đã liên kết còn hiệu lực cho chuyến đi. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công, không có chuyến đi nào được tạo, không còn khoản tạm giữ nào của lượt thuê này và ụ khoá ở trạng thái khoá. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-04, REQ-07, REQ-08, REQ-09, REQ-10, REQ-11, REQ-12, REQ-13, REQ-14, REQ-15, REQ-16, REQ-37, REQ-58, REQ-62, REQ-63 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Người thuê xe | Quét mã QR dán trên ụ khoá để yêu cầu thuê xe. |
| 2 | Hệ thống | Kiểm tra tài khoản đã liên kết thẻ thanh toán (BR-01), không có chuyến đi đang diễn ra (BR-02) và không nợ cước (BR-03). |
| 3 | Hệ thống | Kiểm tra xe tại ụ khoá được phép cho thuê (BR-04). |
| 4 | Hệ thống | Yêu cầu Cổng thanh toán tạm giữ tiền trên thẻ đã liên kết (BR-05). |
| 5 | Cổng thanh toán | Trả về kết quả tạm giữ. |
| 6 | Hệ thống | Gửi lệnh mở khoá tới ụ khoá. |
| 7 | Ụ khoá | Báo xe đã được rút ra. |
| 8 | Hệ thống | Bắt đầu chuyến đi. |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Tài khoản chưa liên kết thẻ thanh toán (BR-01) | Hệ thống | Từ chối yêu cầu thuê xe (Q-22). | Kết thúc use case (thất bại) |
| 2b | Tài khoản đã liên kết thẻ và đang có chuyến đi đang diễn ra (BR-02) | Hệ thống | Từ chối yêu cầu thuê xe (Q-22). | Kết thúc use case (thất bại) |
| 2c | Tài khoản đã liên kết thẻ, không có chuyến đi đang diễn ra và đang nợ cước (BR-03) | Hệ thống | Từ chối yêu cầu thuê xe (Q-22). | Kết thúc use case (thất bại) |
| 3a | Xe tại ụ khoá ở trạng thái "Chờ kiểm tra" (BR-04) | Hệ thống | Từ chối yêu cầu thuê xe (Q-22). | Kết thúc use case (thất bại) |
| 5a | Cổng thanh toán trả về tạm giữ không thành công | Hệ thống | Từ chối yêu cầu thuê xe (Q-08). | Kết thúc use case (thất bại) |
| 6a | Hết thời hạn chờ rút xe mà ụ khoá chưa báo xe được rút ra (BR-06) | - | Hết thời hạn chờ rút xe | - |
| 6a1 | | Hệ thống | Gửi lệnh khoá lại ụ khoá. | |
| 6a2 | | Hệ thống | Yêu cầu Cổng thanh toán huỷ lệnh tạm giữ tiền. | Kết thúc use case (thất bại) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Không có (người thuê xe chỉ cung cấp một mục là mã QR của ụ khoá; hệ thống không trả về bộ thông tin có cấu trúc).

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-01 | Tài khoản chỉ được thuê xe sau khi đã liên kết một thẻ thanh toán. | Ràng buộc | 2, 2a | REQ-04 | Mới |
| BR-02 | Tài khoản chỉ được thuê xe khi không có chuyến đi đang diễn ra. | Ràng buộc | 2, 2b | REQ-08 | Mới |
| BR-03 | Tài khoản chỉ được thuê xe khi không nợ cước. | Ràng buộc | 2, 2c | REQ-09 | Mới |
| BR-04 | Xe ở trạng thái "Chờ kiểm tra" không được cho thuê. | Ràng buộc | 3, 3a | REQ-37 | Mới |
| BR-05 | Số tiền tạm giữ cho mỗi lần thuê xe là 200.000 đồng. | Sự kiện | 4 | REQ-11 | Mới |
| BR-06 | Thời hạn chờ rút xe là 60 giây; quá thời hạn mà xe chưa được rút thì ụ khoá bị khoá lại và lệnh tạm giữ bị huỷ. | Kích hoạt hành động | 6a | REQ-14, REQ-15, REQ-16 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Lệnh mở khoá tới ụ khoá trong không quá 2 giây kể từ khi người thuê xe quét mã (từ bước 1 tới bước 6); phạm vi có gồm bước 4, 5 hay không chờ Q-13 | Performance | REQ-58 |

## 8. Thông tin bổ sung

- Kênh tới ụ khoá theo REQ-63 (MQTT); kênh tới cổng thanh toán theo REQ-62.
- Mốc bắt đầu tính 60 giây ở BR-06 chờ Q-10.

## 8a. Kịch bản chính

- KB1: Luồng chính --> chuyến đi bắt đầu.
- KB2: Luồng chính + 2c --> từ chối vì đang nợ cước.
- KB3: Luồng chính + 3a --> từ chối vì xe "Chờ kiểm tra".
- KB4: Luồng chính + 5a --> tạm giữ không thành công, từ chối.
- KB5: Luồng chính + 6a --> hết 60 giây, ụ bị khoá lại, huỷ tạm giữ.

## 9. Activity diagram

File: diagrams/P04-activity-UC-005.drawio

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú |
|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Người thuê xe | - | - | - | x=0, w=280, h=1540 |
| P-SYS | Partition | Hệ thống | - | - | - | x=280, w=800, h=1540 |
| P-ACT-07 | Partition | Cổng thanh toán | - | - | - | x=1080, w=280, h=1540 |
| P-ACT-08 | Partition | Ụ khoá | - | - | - | x=1360, w=280, h=1540 |
| INIT | Initial | - | - | P-ACT-01 | - | - |
| A-1 | Action | Quét mã QR trên ụ khoá | - | P-ACT-01 | 1 | - |
| A-2 | Action | Kiểm tra liên kết thẻ, chuyến đang diễn ra, nợ cước | - | P-SYS | 2 | - |
| D-2 | Decision | - | - | P-SYS | - | - |
| A-2a | Action | Từ chối thuê xe | - | P-SYS | 2a | - |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - |
| A-2b | Action | Từ chối thuê xe | - | P-SYS | 2b | - |
| FINAL-2 | ActivityFinal | - | - | P-SYS | - | - |
| A-2c | Action | Từ chối thuê xe | - | P-SYS | 2c | - |
| FINAL-3 | ActivityFinal | - | - | P-SYS | - | - |
| A-3 | Action | Kiểm tra xe tại ụ được phép cho thuê | - | P-SYS | 3 | - |
| D-3 | Decision | - | - | P-SYS | - | - |
| A-3a | Action | Từ chối thuê xe | - | P-SYS | 3a | - |
| FINAL-4 | ActivityFinal | - | - | P-SYS | - | - |
| A-4 | Action | Yêu cầu tạm giữ 200.000 đồng | - | P-SYS | 4 | - |
| A-5 | Action | Trả kết quả tạm giữ | - | P-ACT-07 | 5 | - |
| D-5 | Decision | - | - | P-ACT-07 | - | - |
| A-5a | Action | Từ chối thuê xe | - | P-SYS | 5a | - |
| FINAL-5 | ActivityFinal | - | - | P-SYS | - | - |
| A-6 | Action | Gửi lệnh mở khoá tới ụ khoá | - | P-SYS | 6 | - |
| D-6 | Decision | - | - | P-SYS | - | - |
| A-6a1 | Action | Gửi lệnh khoá lại ụ khoá | - | P-SYS | 6a1 | - |
| A-6a2 | Action | Yêu cầu huỷ lệnh tạm giữ | - | P-SYS | 6a2 | - |
| FINAL-6 | ActivityFinal | - | - | P-SYS | - | - |
| A-7 | Action | Báo xe đã được rút ra | - | P-ACT-08 | 7 | - |
| A-8 | Action | Bắt đầu chuyến đi | - | P-SYS | 8 | - |
| FINAL-7 | ActivityFinal | - | - | P-SYS | - | - |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | Vượt partition | (140,200); (410,200) |
| E-03 | A-2 | D-2 | ControlFlow | - | - | - |
| E-04 | D-2 | A-3 | ControlFlow | [đủ điều kiện] | - | - |
| E-05 | D-2 | A-2a | ControlFlow | [chưa liên kết thẻ] | - | - |
| E-06 | D-2 | A-2b | ControlFlow | [đang có chuyến đi] | - | (460,340); (460,440) |
| E-07 | D-2 | A-2c | ControlFlow | [đang nợ cước] | - | (460,340); (460,540) |
| E-08 | A-2a | FINAL-1 | ControlFlow | - | - | - |
| E-09 | A-2b | FINAL-2 | ControlFlow | - | - | - |
| E-10 | A-2c | FINAL-3 | ControlFlow | - | - | - |
| E-11 | A-3 | D-3 | ControlFlow | - | - | - |
| E-12 | D-3 | A-4 | ControlFlow | [được phép cho thuê] | - | - |
| E-13 | D-3 | A-3a | ControlFlow | [xe Chờ kiểm tra] | - | - |
| E-14 | A-3a | FINAL-4 | ControlFlow | - | - | - |
| E-15 | A-4 | A-5 | ControlFlow | - | Vượt partition | (410,840); (1220,840) |
| E-16 | A-5 | D-5 | ControlFlow | - | - | - |
| E-17 | D-5 | A-6 | ControlFlow | [tạm giữ thành công] | Vượt partition | (1220,1030); (410,1030) |
| E-18 | D-5 | A-5a | ControlFlow | [tạm giữ không thành công] | - | - |
| E-19 | A-5a | FINAL-5 | ControlFlow | - | - | - |
| E-20 | A-6 | D-6 | ControlFlow | - | - | - |
| E-21 | D-6 | A-7 | ControlFlow | [xe được rút trong 60 giây] | Vượt partition | (410,1230); (1500,1230) |
| E-22 | D-6 | A-6a1 | ControlFlow | [hết 60 giây] | - | - |
| E-23 | A-6a1 | A-6a2 | ControlFlow | - | - | - |
| E-24 | A-6a2 | FINAL-6 | ControlFlow | - | - | - |
| E-25 | A-7 | A-8 | ControlFlow | - | Vượt partition | (1500,1340); (410,1340) |
| E-26 | A-8 | FINAL-7 | ControlFlow | - | - | - |

Bảng đối chiếu:

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2 |
| 2a | A-2a |
| 2b | A-2b |
| 2c | A-2c |
| 3 | A-3 |
| 3a | A-3a |
| 4 | A-4 |
| 5 | A-5 |
| 5a | A-5a |
| 6 | A-6 |
| 6a1 | A-6a1 |
| 6a2 | A-6a2 |
| 7 | A-7 |
| 8 | A-8 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-20 | Khi ụ khoá được quét không có xe thì hệ thống từ chối yêu cầu thuê? (Có / Không) | UC-005 bước 3 | Mục 3 không nêu |
| Q-21 | Tài khoản đang bị khoá (REQ-31) có được thuê xe không, và có đăng nhập được không? (Có / Không) | UC-005 bước 2, tiền điều kiện | Mục 6, Mục 10 |
| Q-22 | Khi từ chối yêu cầu thuê xe, hệ thống có thông báo lý do cho người thuê xe không? (Có / Không) | UC-005 luồng 2a, 2b, 2c, 3a | Mục 3 chỉ nêu điều kiện, không nêu phản hồi |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Luồng 6a (hết 60 giây) đặt tại bước 6 là bước hệ thống bắt đầu chờ; F5.2 gắn luồng thay thế vào "bước mà tại đó điều kiện được phát hiện", nhưng điều kiện hết giờ chờ không gắn với một hành động nào. Nếu gắn vào bước 7 thì decision D-7 nằm sau action "Báo xe đã được rút ra", tức là action đã xảy ra rồi mới rẽ nhánh "chưa báo", sai nghĩa.
- Luồng 2a, 2b, 2c, 3a chỉ ghi "Từ chối yêu cầu thuê xe" vì nguồn không nêu phản hồi (Q-22).
- Nút khởi đầu và nút kết thúc 30 x 30 không căn giữa được với action 180 x 60 khi mọi toạ độ là bội số của 10; cạnh vào, ra các nút này lệch 5.
