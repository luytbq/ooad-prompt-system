# P04 - Đặc tả use case UC-018 Vào chi nhánh - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-phong-tap.md; P00-problem-brief.md (phiên bản 1.0; các dòng REQ-35, REQ-39, REQ-40, REQ-41, REQ-44, REQ-45, REQ-96 của UC-018 và REQ-10, REQ-42, REQ-43, REQ-46, REQ-51; mục Câu hỏi mở); P01-actors.md (phiên bản 1.0; Mục 2, mục Câu hỏi mở, Giả định); P02-usecases.md (phiên bản 1.1; dòng UC-018 ở bảng 4a, 4b; dòng EV-13, EV-14; mục Câu hỏi mở, Giả định); P02R-review.md (phiên bản 1.0; mục Câu hỏi mở, Giả định); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2, mục Câu hỏi mở, Giả định); P04-uc-specs/_BR-register.md (BR-01 đến BR-14); mục Câu hỏi mở và Giả định của UC-005, UC-010, UC-015 (Q-50 đến Q-66). TEN_HE_THONG_TRONG_LUONG: Phần mềm VietFit. YEU_CAU_BO_SUNG: Không có |
| Phạm vi | UC-018 |
| Mã Q, ASM cuối đã cấp | Q-72; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-018 |
| Tên use case | Vào chi nhánh (Enter Branch) |
| Tác nhân chính | ACT-02 Hội viên<br>ACT-03 Khách vãng lai |
| Tác nhân phụ | ACT-12 Cửa quay |
| Mô tả ngắn | Use case này mô tả tương tác giữa hội viên hoặc khách vãng lai, Phần mềm VietFit và cửa quay khi hội viên hoặc khách vãng lai muốn vào chi nhánh. Kết quả là cửa quay mở cho người có mã QR hợp lệ và lượt quẹt vào cửa của hội viên được ghi nhận. |
| Sự kiện kích hoạt | Hội viên quét mã QR tại cửa quay (EV-13); khách vãng lai quét mã QR trên vé tại cửa quay (EV-14) |
| Tiền điều kiện | Hội viên đã được xác thực và mã QR của hội viên đang hiển thị trên ứng dụng (khi người vào là hội viên; cách tạo mã chờ Q-68).<br>Khách vãng lai đang giữ vé tập một ngày có mã QR do lễ tân in (khi người vào là khách vãng lai). |
| Hậu điều kiện (thành công) | Cửa quay đã nhận kết quả cho phép vào và đã mở cửa.<br>Khi người vào là hội viên: lượt quẹt vào cửa của hội viên đã được ghi nhận kèm chi nhánh và thời điểm quẹt.<br>Khi người vào là khách vãng lai bằng vé (luồng 3a): không có lượt quẹt nào được ghi nhận theo bước 5; việc ghi nhận lượt dùng vé chờ Q-71, Q-40. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công, cửa quay không mở; gói tập của hội viên và vé tập một ngày không thay đổi. Việc lượt quẹt bị từ chối có được ghi nhận hay không chờ Q-71. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-35, REQ-39, REQ-40, REQ-41, REQ-44, REQ-45, REQ-96 (theo P02); REQ-10, REQ-43, REQ-46, REQ-51 (thêm, xem Đề xuất sửa artifact trước) |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Hội viên / Khách vãng lai | Quét mã QR tại đầu đọc của cửa quay. |
| 2 | Cửa quay | Gửi mã QR đọc được và chi nhánh của cửa quay tới phần mềm (xem Dữ liệu vào 1). |
| 3 | Phần mềm VietFit | Kiểm tra mã QR là mã của một hội viên. |
| 4 | Phần mềm VietFit | Kiểm tra gói tập của hội viên còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh của cửa quay (BR-15, BR-16, BR-17). |
| 5 | Phần mềm VietFit | Ghi nhận lượt quẹt vào cửa của hội viên tại chi nhánh (BR-20). |
| 6 | Phần mềm VietFit | Trả kết quả cho phép vào cho cửa quay (xem Dữ liệu ra 1). |
| 7 | Cửa quay | Mở cửa. |
| 8 | Hội viên / Khách vãng lai | Đi qua cửa quay vào chi nhánh. |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 3a | Mã QR là mã trên vé tập một ngày, không phải mã của hội viên | - | Khách vãng lai vào bằng vé tập một ngày | - |
| 3a1 | | Phần mềm VietFit | Kiểm tra vé dùng được trong ngày mua vé và tại chi nhánh đã mua (BR-18, BR-19). | Tiếp tục bước 6 |
| 3a1a | Hôm nay không phải ngày mua vé (BR-18) | Phần mềm VietFit | Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-18) cho cửa quay; cách báo cho người quét chờ Q-70. | Kết thúc use case (thất bại) |
| 3a1b | Hôm nay là ngày mua vé và vé được mua ở chi nhánh khác chi nhánh của cửa quay (BR-19) | Phần mềm VietFit | Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-19) cho cửa quay; cách báo cho người quét chờ Q-70. | Kết thúc use case (thất bại) |
| 3a1c | Vé đúng ngày, đúng chi nhánh và đã được dùng để vào chi nhánh trước đó trong ngày | - | - | Chờ Q-40 |
| 3b | Mã QR không phải mã của hội viên và không phải mã trên vé tập một ngày | Phần mềm VietFit | Từ chối cho vào và thông báo mã QR không hợp lệ (BR-15, BR-18) cho cửa quay; cách báo cho người quét chờ Q-70. | Kết thúc use case (thất bại) |
| 4a | Hội viên không có gói tập còn hiệu lực (BR-15); hội viên chỉ có gói buổi tập cá nhân chờ Q-18, nhiều gói cùng lúc chờ Q-69 | Phần mềm VietFit | Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-15) cho cửa quay; cách báo cho người quét chờ Q-70. | Kết thúc use case (thất bại) |
| 4b | Hội viên có gói còn hiệu lực và gói đó đang bảo lưu (BR-16) | Phần mềm VietFit | Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-16) cho cửa quay; cách báo cho người quét chờ Q-70. | Kết thúc use case (thất bại) |
| 4c | Gói còn hiệu lực, không đang bảo lưu và không áp dụng cho chi nhánh của cửa quay (BR-17) | Phần mềm VietFit | Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-17) cho cửa quay; cách báo cho người quét chờ Q-70. | Kết thúc use case (thất bại) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

### Dữ liệu vào 1 (bước 2)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Mã QR đọc được | Chuỗi mã mà đầu đọc của cửa quay đọc từ mã QR hiển thị trên ứng dụng của hội viên hoặc in trên vé tập một ngày | Có | Chưa quy định (Q-68) | VF-M-004217 (ví dụ minh hoạ, định dạng chưa quy định) |
| 2 | Chi nhánh của cửa quay | Chi nhánh nơi cửa quay đặt, dùng để kiểm tra gói tập áp dụng cho chi nhánh và vé dùng tại chi nhánh đã mua (BR-17, BR-19) | Chưa quy định (Q-67) | Là một chi nhánh của VietFit; cách cửa quay cho biết chi nhánh chờ Q-67 | Chi nhánh số 2 |
| 3 | Thời điểm quẹt | Thời điểm hội viên quét mã tại cửa quay, dùng làm căn cứ xác định vắng mặt (BR-20) | Chưa quy định (Q-67) | Chưa quy định (Q-67) | 17:45 ngày 19/10/2026 |

### Dữ liệu ra 1 (bước 6)

Dùng chung cho kết quả không cho phép vào ở các luồng 3a1a, 3a1b, 3b, 4a, 4b, 4c.

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Kết quả cho phép vào | Cửa quay có được mở cho người vừa quét mã hay không | Một trong hai giá trị "Cho phép", "Không cho phép" | Cho phép |
| 2 | Lý do không cho phép | Quy tắc bị vi phạm khi kết quả là "Không cho phép"; để trống khi cho phép | Một câu văn bản ngắn; nội dung và cách báo cho người quét chờ Q-70 | Gói tập đang bảo lưu |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-15 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên còn hiệu lực. | Ràng buộc | 4, 4a, 3b | REQ-41 | Mới |
| BR-16 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên không đang bảo lưu. | Ràng buộc | 4, 4b | REQ-41 | Mới |
| BR-17 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên áp dụng cho chi nhánh có cửa quay đó. | Ràng buộc | 4, 4c, Dữ liệu vào 1 | REQ-41, REQ-10 | Mới |
| BR-18 | Mã QR trên vé tập một ngày chỉ dùng được trong ngày mua vé. | Ràng buộc | 3a1, 3a1a, 3b | REQ-44 | Mới |
| BR-19 | Mã QR trên vé tập một ngày chỉ dùng được tại chi nhánh đã mua vé. | Ràng buộc | 3a1, 3a1b, Dữ liệu vào 1 | REQ-45 | Mới |
| BR-20 | Hội viên đặt chỗ lớp nhóm được xem là không vào lớp khi không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu lớp. | Suy luận | 5, Dữ liệu vào 1 | REQ-35 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Cửa quay phản hồi trong vòng 1 giây; thời điểm bắt đầu và kết thúc phép đo chờ Q-41 | Performance | REQ-96 |
| 2 | Phần mềm trao đổi mã QR đọc được và kết quả cho phép vào với cửa quay có đầu đọc mã QR tại mỗi chi nhánh qua API; hồ sơ dự án chưa ghi tài liệu API của cửa quay | Interface | REQ-40 |

## 8. Thông tin bổ sung

- Lượt quẹt vào cửa ghi ở bước 5 là dữ liệu đầu vào của UC-016 Ghi nhận vắng mặt lớp nhóm; UC-016 dùng lại BR-20 khi được đặc tả (P02 mô tả UC-018: "Lượt quẹt vào cửa là căn cứ xác định vắng mặt (UC-016)").
- Dữ liệu dùng chung với use case khác: gói tập do UC-005 tạo và do UC-006 đặt trạng thái bảo lưu; vé tập một ngày và mã QR trên vé do UC-017 tạo (REQ-43).
- Hiển thị mã QR trên ứng dụng (CAND-34) được xử lý là tiền điều kiện của hội viên vì sự kiện kích hoạt của P02 là lúc hội viên quét mã tại cửa quay (EV-13); xem Đề xuất sửa artifact trước.
- Số lần dùng vé trong ngày chờ Q-40: trả lời "một lần" thì cần ghi nhận lượt dùng vé ở luồng 3a1 và luồng 3a1c có hành động từ chối; trả lời "nhiều lần" thì luồng 3a1c bỏ.
- Hai tác nhân chính dùng chung partition vì P01 không có quan hệ tổng quát hoá giữa ACT-02 và ACT-03; khác biệt hành vi giữa hội viên và khách vãng lai được thể hiện ở luồng 3a.

## 9. Activity diagram

File: diagrams/P04-activity-UC-018.drawio (một trang, tên trang UC-018). Toạ độ x, y, w, h trong bảng Node là toạ độ tương đối trong partition cha.

Bảng Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-02-03 | Partition | Hội viên / Khách vãng lai | - | - | - | Tác nhân hoặc chủ thể thực hiện bước | 0 | 0 | 280 | 1260 |
| P-SYS | Partition | Phần mềm VietFit | - | - | - | Tác nhân hoặc chủ thể thực hiện bước | 280 | 0 | 1200 | 1260 |
| P-ACT-12 | Partition | Cửa quay | - | - | - | Tác nhân hoặc chủ thể thực hiện bước | 1480 | 0 | 280 | 1260 |
| INIT | Initial | - | - | P-ACT-02-03 | 1 | Điểm bắt đầu, trong partition của chủ thể bước 1 | 120 | 60 | 40 | 40 |
| A-1 | Action | Quét mã QR tại cửa quay | - | P-ACT-02-03 | 1 | Sự kiện kích hoạt EV-13, EV-14 | 50 | 140 | 180 | 60 |
| A-2 | Action | Gửi mã QR đọc được tới phần mềm | - | P-ACT-12 | 2 | - | 50 | 240 | 180 | 60 |
| A-3 | Action | Kiểm tra mã QR là của hội viên | - | P-SYS | 3 | - | 410 | 340 | 180 | 60 |
| D-3 | Decision | - | - | P-SYS | 3 | Rẽ nhánh 3a, 3b | 480 | 440 | 40 | 40 |
| A-3a1 | Action | Kiểm tra vé tập một ngày | - | P-SYS | 3a1 | Luồng 3a (hàng tiêu đề 3a không có action) | 650 | 430 | 180 | 60 |
| D-3a1 | Decision | - | - | P-SYS | 3a1 | Rẽ nhánh 3a1a, 3a1b, 3a1c | 720 | 540 | 40 | 40 |
| A-3a1a | Action | Từ chối cho vào, báo BR-18 | - | P-SYS | 3a1a | - | 890 | 530 | 180 | 60 |
| A-3a1b | Action | Từ chối cho vào, báo BR-19 | - | P-SYS | 3a1b | - | 890 | 650 | 180 | 60 |
| N-3a1c | Note | Chờ Q-40 | - | P-SYS | 3a1c | Luồng 3a1c không có hành động | 970 | 770 | 160 | 60 |
| A-3b | Action | Từ chối cho vào, báo mã không hợp lệ | - | P-SYS | 3b | - | 650 | 330 | 180 | 60 |
| A-4 | Action | Kiểm tra gói tập của hội viên | - | P-SYS | 4 | - | 410 | 520 | 180 | 60 |
| D-4 | Decision | - | - | P-SYS | 4 | Rẽ nhánh 4a, 4b, 4c | 480 | 620 | 40 | 40 |
| A-4a | Action | Từ chối cho vào, báo BR-15 | - | P-SYS | 4a | - | 150 | 610 | 180 | 60 |
| A-4b | Action | Từ chối cho vào, báo BR-16 | - | P-SYS | 4b | - | 150 | 710 | 180 | 60 |
| A-4c | Action | Từ chối cho vào, báo BR-17 | - | P-SYS | 4c | - | 150 | 810 | 180 | 60 |
| A-5 | Action | Ghi nhận lượt quẹt vào cửa | - | P-SYS | 5 | - | 410 | 700 | 180 | 60 |
| M-6 | Merge | - | - | P-SYS | 6 | Nhận luồng chính và luồng 3a1 (Tiếp tục bước 6) | 480 | 800 | 40 | 40 |
| A-6 | Action | Trả kết quả cho phép vào | - | P-SYS | 6 | - | 410 | 880 | 180 | 60 |
| A-7 | Action | Mở cửa | - | P-ACT-12 | 7 | - | 50 | 980 | 180 | 60 |
| A-8 | Action | Đi qua cửa quay vào chi nhánh | - | P-ACT-02-03 | 8 | - | 50 | 1080 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-ACT-02-03 | 8 | Kết thúc thành công | 120 | 1180 | 40 | 40 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | 3a1a | Kết thúc thất bại | 1130 | 540 | 40 | 40 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | 3a1b | Kết thúc thất bại | 1130 | 660 | 40 | 40 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | 3a1c | Chờ Q-40 | 890 | 780 | 40 | 40 |
| FINAL-5 | ActivityFinal | - | - | P-SYS | 3b | Kết thúc thất bại | 890 | 340 | 40 | 40 |
| FINAL-6 | ActivityFinal | - | - | P-SYS | 4a | Kết thúc thất bại | 60 | 630 | 40 | 40 |
| FINAL-7 | ActivityFinal | - | - | P-SYS | 4b | Kết thúc thất bại | 60 | 730 | 40 | 40 |
| FINAL-8 | ActivityFinal | - | - | P-SYS | 4c | Kết thúc thất bại | 60 | 830 | 40 | 40 |

Bảng Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | Vượt partition Phần mềm VietFit | (140,220); (1620,220) |
| E-03 | A-2 | A-3 | ControlFlow | - | Vượt partition Phần mềm VietFit | (780,270) |
| E-04 | A-3 | D-3 | ControlFlow | - | - | - |
| E-05 | D-3 | A-4 | ControlFlow | [mã QR là mã của hội viên] | - | - |
| E-06 | D-3 | A-3a1 | ControlFlow | [mã QR là mã trên vé tập một ngày] | Luồng 3a | - |
| E-07 | D-3 | A-3b | ControlFlow | [mã QR không phải mã hội viên hay mã vé] | Luồng 3b | (900,460); (900,360) |
| E-08 | A-3a1 | D-3a1 | ControlFlow | - | - | - |
| E-09 | D-3a1 | M-6 | ControlFlow | [vé dùng được] | Tiếp tục bước 6 | (1020,820) |
| E-10 | D-3a1 | A-3a1a | ControlFlow | [hôm nay không phải ngày mua vé] | Luồng 3a1a | - |
| E-11 | D-3a1 | A-3a1b | ControlFlow | [đúng ngày, vé thuộc chi nhánh khác] | Luồng 3a1b | (1100,560); (1100,680) |
| E-12 | D-3a1 | FINAL-4 | ControlFlow | [đúng ngày, đúng chi nhánh, vé đã dùng trước đó] | Luồng 3a1c, chờ Q-40 | (1100,560); (1100,800) |
| E-13 | A-3a1a | FINAL-2 | ControlFlow | - | - | - |
| E-14 | A-3a1b | FINAL-3 | ControlFlow | - | - | - |
| E-15 | N-3a1c | FINAL-4 | NoteLink | - | Ghi chú Chờ Q-40 | - |
| E-16 | A-3b | FINAL-5 | ControlFlow | - | - | - |
| E-17 | A-4 | D-4 | ControlFlow | - | - | - |
| E-18 | D-4 | A-5 | ControlFlow | [gói đủ điều kiện] | - | - |
| E-19 | D-4 | A-4a | ControlFlow | [không có gói còn hiệu lực] | Luồng 4a | - |
| E-20 | D-4 | A-4b | ControlFlow | [gói còn hiệu lực và đang bảo lưu] | Luồng 4b | (650,640); (650,740) |
| E-21 | D-4 | A-4c | ControlFlow | [gói còn hiệu lực, không bảo lưu, không áp dụng cho chi nhánh] | Luồng 4c | (650,640); (650,840) |
| E-22 | A-4a | FINAL-6 | ControlFlow | - | - | - |
| E-23 | A-4b | FINAL-7 | ControlFlow | - | - | - |
| E-24 | A-4c | FINAL-8 | ControlFlow | - | - | - |
| E-25 | A-5 | M-6 | ControlFlow | - | - | - |
| E-26 | M-6 | A-6 | ControlFlow | - | - | - |
| E-27 | A-6 | A-7 | ControlFlow | - | Vượt partition Phần mềm VietFit | (780,960); (1620,960) |
| E-28 | A-7 | A-8 | ControlFlow | - | Vượt partition Phần mềm VietFit | (1620,1060); (140,1060) |
| E-29 | A-8 | FINAL-1 | ControlFlow | - | - | - |

Bảng đối chiếu bước luồng với node:

| Bước UC | Node |
|---|---|
| 1 | INIT, A-1 |
| 2 | A-2 |
| 3 | A-3, D-3 |
| 3a | Guard của E-06 (hàng tiêu đề, không có action) |
| 3a1 | A-3a1, D-3a1 |
| 3a1a | A-3a1a, FINAL-2 |
| 3a1b | A-3a1b, FINAL-3 |
| 3a1c | Guard của E-12, FINAL-4, N-3a1c (không có action) |
| 3b | A-3b, FINAL-5 |
| 4 | A-4, D-4 |
| 4a | A-4a, FINAL-6 |
| 4b | A-4b, FINAL-7 |
| 4c | A-4c, FINAL-8 |
| 5 | A-5 |
| 6 | M-6, A-6 |
| 7 | A-7 |
| 8 | A-8, FINAL-1 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-67 | Cửa quay gửi tới phần mềm những thông tin nào ngoài mã QR đọc được (mã cửa quay hoặc chi nhánh, thời điểm quẹt), và kết quả phần mềm trả về gồm những gì (chỉ cho phép hoặc không cho phép, hay kèm lý do)? (Cửa quay gửi mã QR, chi nhánh và thời điểm quẹt; phần mềm trả cho phép hoặc không cho phép kèm lý do / Khác - nêu rõ) | Bước 2, bước 6; Dữ liệu vào 1, Dữ liệu ra 1; BR-17, BR-19, BR-20; REQ-40; giao diện thiết bị (P11b) | Mục 5 câu 2: "Cửa quay hỏi phần mềm"; HE_THONG_NGOAI: cửa quay "gửi mã QR đọc được tới phần mềm qua API và mở cửa theo kết quả trả về" không nêu nội dung trao đổi và cách phần mềm biết chi nhánh của cửa quay |
| Q-68 | Mã QR hiển thị trên ứng dụng của hội viên là một mã cố định cho mỗi hội viên hay đổi theo thời gian, và mã cũ hoặc mã đã được chụp lại có bị từ chối không? (Cố định cho mỗi hội viên / Đổi theo thời gian - nêu thời hạn hiệu lực của mỗi mã) | Tiền điều kiện; bước 3; có thêm luồng mã QR hết hiệu lực hay không; Dữ liệu vào 1 | Mục 5 câu 1: "bằng mã QR hiển thị trên ứng dụng" không nêu cách tạo mã hoặc thời hạn của mã |
| Q-69 | Hội viên có nhiều gói tập cùng lúc (gói gia hạn nối tiếp, gói một chi nhánh và gói toàn chuỗi) thì ba điều kiện "còn hiệu lực, không đang bảo lưu, áp dụng cho chi nhánh" phải cùng đúng ở một gói hay mỗi điều kiện xét riêng trên mọi gói, và gói gia hạn chưa tới ngày bắt đầu có tính là còn hiệu lực không? (Cùng đúng ở ít nhất một gói / Xét riêng từng điều kiện trên mọi gói) | Bước 4, luồng 4a, 4b, 4c; BR-15, BR-16, BR-17 | Mục 5 câu 2: "gói tập còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh đó" dùng số ít; Mục 2 câu 3: gói gia hạn bắt đầu sau ngày hết hạn của gói cũ nên một hội viên có thể có nhiều gói |
| Q-70 | Khi cửa quay không mở, người quét được báo lý do bằng cách nào (màn hình hoặc âm báo của cửa quay, thông báo trên ứng dụng), nội dung báo gồm những gì, và khi một lần quét vi phạm nhiều điều kiện cùng lúc (ví dụ gói hết hạn và gói không áp dụng cho chi nhánh; vé sai ngày và sai chi nhánh) thì báo lý do nào? (Cửa quay báo, nêu cách / Ứng dụng báo / Không báo lý do; thứ tự ưu tiên của lý do - nêu rõ) | Luồng 3a1a, 3a1b, 3b, 4a, 4b, 4c; Dữ liệu ra 1; thứ tự loại trừ giữa các điều kiện cùng bước | Mục 5 câu 2: "chỉ mở khi gói tập còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh đó" không nêu phản hồi cho người quét khi cửa không mở; HE_THONG_NGOAI: cửa quay mở cửa "theo kết quả trả về" |
| Q-71 | Lượt quẹt bị từ chối có được ghi nhận không và có tính là "quẹt vào cửa" để xác định vắng mặt không; lượt vào của khách vãng lai bằng vé có được ghi nhận không? (Chỉ ghi lượt được cho phép vào / Ghi cả lượt bị từ chối, nêu cách tính cho việc xác định vắng mặt; ghi hoặc không ghi lượt dùng vé) | Bước 5; hậu điều kiện thành công và tối thiểu; luồng 3a, 3a1c; BR-20; UC-016 | Mục 4 câu 2: "không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu" không nêu lượt quẹt bị từ chối có được tính; Mục 5 câu 2: cửa quay chỉ mở khi hợp lệ |
| Q-72 | Khi cửa quay không nhận được kết quả từ phần mềm trong 1 giây hoặc không liên lạc được với phần mềm, cửa quay giữ đóng hay mở, và lượt quẹt đó có phải được ghi nhận bù sau không? (Giữ đóng / Mở / Khác - nêu rõ) | Có thêm luồng thay thế tại bước 2 hoặc bước 6 hay không; hậu điều kiện tối thiểu; REQ-96 | Mục 10 câu 4: "Cửa quay phải phản hồi trong vòng 1 giây" không nêu việc xảy ra khi quá ngưỡng |

Các câu hỏi đã cấp ở bước trước và làm đổi use case này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-18 (hội viên chỉ có gói buổi tập cá nhân có được vào chi nhánh không), Q-40 (mã QR trên vé mở cửa một lần hay nhiều lần), Q-41 (ngưỡng 1 giây tính từ lúc nào đến lúc nào), Q-03 (ai tạo danh mục chi nhánh mà cửa quay thuộc về).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-018 (bảng 4b cột REQ, Mục 5) | Đặc tả dùng thêm bốn REQ ngoài danh sách của P02: REQ-10 (gói tập loại một chi nhánh hoặc toàn chuỗi, dùng ở BR-17), REQ-43 (lễ tân in vé có mã QR, nguồn của mã QR ở luồng 3a), REQ-46 (bảo lưu gói, nguồn của trạng thái "đang bảo lưu" ở BR-16), REQ-51 (ngày hết hạn lùi theo số ngày bảo lưu, ảnh hưởng điều kiện "còn hiệu lực" ở BR-15) | Thêm REQ-10, REQ-43, REQ-46, REQ-51 vào cột REQ của UC-018 ở bảng 4b và vào Mục 5 |
| P02 | CAND-34, EV-13, UC-018 | CAND-34 "Hiển thị mã QR trên ứng dụng" được xếp "Là bước của UC-018", nhưng sự kiện kích hoạt EV-13 là lúc hội viên quét mã tại cửa quay, nên bước hiển thị mã không thể là bước của luồng chính (bước 1 phải là sự kiện kích hoạt) | Chọn một trong hai: (a) đổi disposition CAND-34 thành tiền điều kiện của UC-018; (b) đổi sự kiện kích hoạt EV-13 thành lúc hội viên mở mã QR để vào chi nhánh rồi chạy lại P04 cho UC-018 để có bước hiển thị mã |

## Vấn đề còn mở

- Mọi mục Target đạt, với các điểm cần người dùng lưu ý:
  - Mục 5a (Target): mọi luồng thất bại chỉ có bước hệ thống báo kết quả cho cửa quay (thiết bị); nguồn không nêu cách người quét được báo, nên ghi Q-70 thay vì bước báo trực tiếp cho người.
  - Mục 12 (Target): bước 5 (ghi nhận lượt quẹt) và BR-20 suy ra từ REQ-35 và câu "Lượt quẹt vào cửa là căn cứ xác định vắng mặt (UC-016)" của P02; tài liệu nguồn không có câu nào nêu rõ phần mềm ghi lượt quẹt, nên Q-71 hỏi phạm vi ghi nhận.
  - Mục 8 (Target): luồng 3a1c dùng "Chờ Q-40" cho điều kiện "vé đã được dùng trước đó"; điều kiện này chỉ có nghĩa khi Q-40 trả lời "một lần", luồng sẽ bỏ nếu trả lời "nhiều lần".
  - Mục 8 (Target) và F5.3: các điều kiện cùng bước có thể cùng đúng (3a1a và 3a1b; 4a, 4b, 4c); điều kiện đã viết loại trừ nhau theo thứ tự xuất hiện trong nguồn, thứ tự ưu tiên lý do báo cho người quét chờ Q-70.
  - Bố cục (F10.6): activity diagram đặt nhánh thay thế của bước 4 ở bên trái trục chính và nhánh của bước 3 ở bên phải, vì hai chuỗi nhánh (có decision lồng 3a1) cùng cần cột riêng mà không cắt cạnh; trục dọc của các cạnh ra từ decision đặt ở khoảng trống giữa trục chính và cột nhánh (cách decision hơn 30) để không đi qua action rộng 180.
  - Mục 8a (khung Format) Kịch bản chính không có vì MUC_CHI_TIET trong project-profile.md là GON.
