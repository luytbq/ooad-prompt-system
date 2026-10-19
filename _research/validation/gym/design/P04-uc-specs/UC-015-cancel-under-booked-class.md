# P04 - Đặc tả use case UC-015 Huỷ lớp nhóm ít người đặt - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-phong-tap.md; P00-problem-brief.md (phiên bản 1.0; các dòng REQ của UC-015 và REQ-22, REQ-30, REQ-34, REQ-35, REQ-70, REQ-76; mục Câu hỏi mở); P01-actors.md (phiên bản 1.0; Mục 2, mục Câu hỏi mở, Giả định); P02-usecases.md (phiên bản 1.1; dòng UC-015 ở bảng 4a, 4b; dòng EV-27; mục Câu hỏi mở, Giả định); P02R-review.md (phiên bản 1.0; mục Câu hỏi mở, Giả định); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2; mục Câu hỏi mở, Giả định); P04-uc-specs/_BR-register.md (BR-01 đến BR-12); mục Câu hỏi mở, Giả định của P04-uc-specs/UC-005-purchase-or-renew-membership-package.md và P04-uc-specs/UC-010-book-class-spot.md. UC_ID: UC-015. TEN_HE_THONG_TRONG_LUONG: Phần mềm VietFit. YEU_CAU_BO_SUNG: Không có |
| Phạm vi | UC-015 |
| Mã Q, ASM cuối đã cấp | Q-66; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-015 |
| Tên use case | Huỷ lớp nhóm ít người đặt (Cancel Under-Booked Class) |
| Tác nhân chính | ACT-14 Bộ định thời theo hạn |
| Tác nhân phụ | ACT-09 Cổng SMS<br>ACT-10 Dịch vụ thông báo đẩy |
| Mô tả ngắn | Use case này mô tả tương tác giữa Bộ định thời theo hạn và Phần mềm VietFit khi tới mốc 2 giờ trước giờ học của một lớp nhóm mà lớp có dưới 3 người đặt chỗ. Kết quả là lớp bị huỷ và những hội viên đã đặt chỗ biết lớp đã bị huỷ. |
| Sự kiện kích hoạt | Đến 2 giờ trước giờ học, lớp có dưới 3 người đặt chỗ (EV-27) |
| Tiền điều kiện | Lớp nhóm đã được lập lịch và có giờ học xác định. |
| Hậu điều kiện (thành công) | Lớp nhóm ở trạng thái đã huỷ.<br>Mốc tính vắng mặt của UC-016 và mốc chuyển chỗ từ danh sách chờ của UC-013 gắn với lớp không còn chờ kích hoạt (Q-64).<br>Mỗi hội viên đã đặt chỗ của lớp đã được gửi thông báo lớp bị huỷ qua thông báo đẩy, hoặc qua SMS khi chưa cài ứng dụng (BR-14). |
| Hậu điều kiện tối thiểu | Luồng 2a và 2b kết thúc trước bước lưu: không có thay đổi dữ liệu nào được lưu.<br>Luồng 6a: lớp nhóm đã ở trạng thái đã huỷ (bước 3); trạng thái thông báo của các hội viên còn lại chờ Q-65. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-73, REQ-74, REQ-75, REQ-87, REQ-88, REQ-89, REQ-90 (theo P02).<br>REQ thêm: REQ-22, REQ-30, REQ-34, REQ-35, REQ-70, REQ-76 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Phần mềm VietFit | Tới mốc 2 giờ trước giờ học của một lớp nhóm (BR-13). |
| 2 | Phần mềm VietFit | Kiểm tra lớp nhóm chưa bị huỷ và số người đặt chỗ của lớp dưới 3 (BR-13). |
| 3 | Phần mềm VietFit | Huỷ lớp nhóm (BR-13). |
| 4 | Phần mềm VietFit | Huỷ mốc tính vắng mặt của UC-016 và mốc chuyển chỗ của UC-013 gắn với lớp (Q-64). |
| 5 | Phần mềm VietFit | Xác định các hội viên đã đặt chỗ của lớp. |
| 6 | Phần mềm VietFit | Gửi thông báo lớp bị huỷ (xem Dữ liệu ra 1) cho một hội viên đã đặt chỗ chưa được thông báo, qua dịch vụ thông báo đẩy, hoặc qua cổng SMS khi hội viên chưa cài ứng dụng (BR-14). |
| 7 | Phần mềm VietFit | Lặp lại bước 6 cho đến khi mọi hội viên đã đặt chỗ của lớp được gửi thông báo. |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | Lớp nhóm đã bị huỷ trước mốc 2 giờ (do quản lý chi nhánh huỷ vì sự cố, UC-014) | - | - | Kết thúc use case (thất bại) |
| 2b | Lớp nhóm chưa bị huỷ và có từ 3 người đặt chỗ trở lên (BR-13) | - | - | Kết thúc use case (thất bại) |
| 5a | Lớp nhóm không có hội viên nào đã đặt chỗ | - | - | Kết thúc use case (thành công) |
| 6a | Dịch vụ thông báo đẩy hoặc cổng SMS không gửi được thông báo cho hội viên | - | - | Chờ Q-65 |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào: Không có (use case do tác nhân thời gian kích hoạt, không tác nhân nào cung cấp thông tin).

Dữ liệu ra 1 (bước 6)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Lớp nhóm bị huỷ | Lớp nhóm mà hội viên đã đặt chỗ, nhận diện theo loại lớp và giờ học (REQ-70) | Chưa quy định (Q-66) | Yoga, 18:00 ngày 26/10/2026 |
| 2 | Nội dung khác của thông báo | Thông tin ngoài việc lớp đã bị huỷ mà thông báo gửi cho hội viên có thêm | Chưa quy định (Q-66) | Chưa quy định (Q-66) |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-13 | Lớp nhóm có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học thì bị huỷ. | Kích hoạt hành động | Bước 1, bước 2, bước 3, luồng 2b | REQ-73, REQ-74 | Mới |
| BR-14 | Thông báo cho hội viên gửi qua thông báo đẩy của ứng dụng; hội viên chưa cài ứng dụng thì nhận SMS qua cổng SMS. | Kích hoạt hành động | Bước 6 | REQ-87, REQ-88 | Mới |

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Tần suất: use case chạy một lần cho mỗi lớp nhóm, tại mốc 2 giờ trước giờ học của lớp. Nguồn nêu khoảng 25 lớp mỗi ngày ở mỗi chi nhánh, 4 chi nhánh, tức khoảng 4 x 25 = 100 lần chạy mỗi ngày.
- Ví dụ tính mốc (BR-13): lớp bắt đầu lúc 18:00 thì mốc xét là 18:00 trừ 2 giờ = 16:00 cùng ngày. Lớp có 0, 1 hoặc 2 người đặt chỗ thì bị huỷ; lớp có 3 người đặt chỗ trở lên thì không bị huỷ (luồng 2b).
- Luồng 2a, 2b ghi "Kết thúc use case (thất bại)" vì mục tiêu của use case (hội viên đã đặt chỗ biết lớp bị huỷ) không đạt; đây là các lần xét mà không có việc cần làm, không phải lỗi. Luồng 5a ghi "thành công" vì lớp đã bị huỷ và không còn ai cần được thông báo.
- Hội viên đã đặt chỗ là bên nhận thụ động (P01 Mục 3), không phải tác nhân của use case này; Dịch vụ thông báo đẩy và Cổng SMS chỉ nhận yêu cầu gửi, nguồn không nêu kết quả gửi được dùng tiếp ngoài luồng 6a.
- Mốc 2 giờ trước giờ học của lớp do UC-009 Lập lịch lớp nhóm tạo ra, và UC-014 Huỷ lớp nhóm vì sự cố làm mất hiệu lực; hai use case đó cần có bước hẹn, huỷ mốc của UC-015 khi đặc tả (quy tắc hẹn mốc cho use case do tác nhân thời gian kích hoạt).
- Kết cục cần khớp khi đặc tả các use case khác: UC-010 (luồng chặn đặt chỗ lớp đã huỷ), UC-011 (huỷ chỗ của lớp đã huỷ), UC-016 và UC-013 (không kích hoạt cho lớp đã huỷ, Q-64), UC-014 (cùng lớp đã huỷ, luồng 2a của use case này).
- Q-43 chưa trả lời: use case viết theo hướng hệ thống tự huỷ lớp (câu bị động của nguồn). Nếu có bước nhân viên duyệt hoặc gỡ thì tác nhân chính, luồng chính và sơ đồ phải xét lại.

## 9. Activity diagram

Nguồn chuẩn là hai bảng dưới đây; file diagrams/P04-activity-UC-015.drawio sinh từ hai bảng này.

Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-SYS | Partition | Phần mềm VietFit | - | - | - | Chủ thể duy nhất của cột Thực hiện bởi; ACT-14 là tác nhân thời gian nên không có partition, ACT-09 và ACT-10 không làm chủ thể bước nào | 0 | 0 | 800 | 1380 |
| INIT | Initial | - | - | P-SYS | - | - | 180 | 60 | 40 | 40 |
| A-1 | AcceptTimeEvent | Tới 2 giờ trước giờ học của lớp nhóm | - | P-SYS | 1 | - | 110 | 120 | 180 | 60 |
| A-2 | Action | Kiểm tra lớp và số người đặt chỗ | - | P-SYS | 2 | - | 110 | 230 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | 2 | Luồng 2a, 2b | 180 | 340 | 40 | 40 |
| A-3 | Action | Huỷ lớp nhóm | - | P-SYS | 3 | - | 110 | 470 | 180 | 60 |
| A-4 | Action | Huỷ mốc tính vắng mặt và chuyển chỗ | - | P-SYS | 4 | - | 110 | 580 | 180 | 60 |
| A-5 | Action | Xác định hội viên đã đặt chỗ | - | P-SYS | 5 | - | 110 | 690 | 180 | 60 |
| D-5 | Decision | - | - | P-SYS | 5 | Luồng 5a | 180 | 800 | 40 | 40 |
| M-6 | Merge | - | - | P-SYS | 6 | Nhận luồng từ D-5 và vòng lặp D-7 | 180 | 890 | 40 | 40 |
| A-6 | Action | Gửi thông báo huỷ lớp cho một hội viên | - | P-SYS | 6 | - | 110 | 980 | 180 | 60 |
| D-6 | Decision | - | - | P-SYS | 6 | Luồng 6a | 180 | 1090 | 40 | 40 |
| D-7 | Decision | - | - | P-SYS | 7 | Bước Lặp lại bước 6 | 180 | 1180 | 40 | 40 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | 7 | Kết thúc luồng chính | 180 | 1270 | 40 | 40 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | 2a | - | 500 | 320 | 40 | 40 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | 2b | - | 500 | 400 | 40 | 40 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | 5a | - | 500 | 800 | 40 | 40 |
| FINAL-5 | ActivityFinal | - | - | P-SYS | 6a | - | 500 | 1090 | 40 | 40 |
| N-6a | Note | Chờ Q-65 | - | P-SYS | 6a | Gắn với FINAL-5 | 600 | 1080 | 160 | 60 |

Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - | - |
| E-03 | A-2 | D-2 | ControlFlow | - | - | - |
| E-04 | D-2 | A-3 | ControlFlow | [chưa huỷ, dưới 3 người đặt chỗ] | Nhánh luồng chính | - |
| E-05 | D-2 | FINAL-2 | ControlFlow | [lớp đã bị huỷ] | Luồng 2a | (250,360); (250,340) |
| E-06 | D-2 | FINAL-3 | ControlFlow | [chưa huỷ, từ 3 người đặt chỗ trở lên] | Luồng 2b | (250,360); (250,420) |
| E-07 | A-3 | A-4 | ControlFlow | - | - | - |
| E-08 | A-4 | A-5 | ControlFlow | - | - | - |
| E-09 | A-5 | D-5 | ControlFlow | - | - | - |
| E-10 | D-5 | M-6 | ControlFlow | [có hội viên đã đặt chỗ] | Nhánh luồng chính | - |
| E-11 | D-5 | FINAL-4 | ControlFlow | [không có hội viên đã đặt chỗ] | Luồng 5a | - |
| E-12 | M-6 | A-6 | ControlFlow | - | - | - |
| E-13 | A-6 | D-6 | ControlFlow | - | - | - |
| E-14 | D-6 | D-7 | ControlFlow | [gửi được thông báo] | Nhánh luồng chính | - |
| E-15 | D-6 | FINAL-5 | ControlFlow | [không gửi được thông báo] | Luồng 6a | - |
| E-16 | D-7 | M-6 | ControlFlow | [còn hội viên chưa được thông báo] | Vòng lặp quay lại bước 6 | (60,1200); (60,910) |
| E-17 | D-7 | FINAL-1 | ControlFlow | [hết hội viên chưa được thông báo] | Đi tiếp | - |
| E-18 | N-6a | FINAL-5 | NoteLink | - | - | - |

Đối chiếu bước và node

| Bước UC | Node |
|---|---|
| 1 | A-1 |
| 2 | A-2, D-2 |
| 3 | A-3 |
| 4 | A-4 |
| 5 | A-5, D-5 |
| 6 | A-6, M-6, D-6 |
| 7 | D-7, M-6 |
| 2a | E-05, FINAL-2 |
| 2b | E-06, FINAL-3 |
| 5a | E-11, FINAL-4 |
| 6a | E-15, FINAL-5, N-6a |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-63 | Khi lớp bị tự huỷ, các chỗ đã đặt và danh sách chờ của lớp (kể cả hội viên đang được thông báo nhận chỗ trong 30 phút) được xử lý thế nào, và người trong danh sách chờ có được thông báo lớp bị huỷ không? (Chỗ đã đặt mất hiệu lực, danh sách chờ bị xoá, người trong danh sách chờ được thông báo như người đã đặt / Chỉ người đã đặt được thông báo, danh sách chờ không đổi / Khác - nêu rõ) | Bước 3, bước 5, bước 6; hậu điều kiện; UC-010, UC-011, UC-012, UC-013 | Mục 8 câu 3: "gửi thông báo cho những người đã đặt" chỉ nêu người đã đặt, trong khi câu 4 (huỷ vì sự cố) nêu thêm "người trong danh sách chờ"; Mục 3 câu 3 và câu 4 nêu danh sách chờ và hạn 30 phút nhưng không nêu khi lớp bị huỷ |
| Q-64 | Khi lớp bị tự huỷ, các mốc hạn còn chờ của lớp (tính vắng mặt 10 phút sau giờ bắt đầu của UC-016; chuyển chỗ sau 30 phút của UC-013) có bị huỷ không, hay các use case đó tự bỏ qua lớp đã huỷ? (Hệ thống huỷ các mốc khi huỷ lớp / UC-016 và UC-013 kiểm tra trạng thái lớp khi tới mốc / Khác - nêu rõ) | Bước 4; hậu điều kiện; UC-016, UC-013 | Mục 4 câu 2 ("bị tính một lần vắng mặt") và Mục 3 câu 4 ("quá 30 phút thì chỗ chuyển cho người kế tiếp") không nêu điều gì xảy ra khi lớp đã bị huỷ trước các mốc đó |
| Q-65 | Khi dịch vụ thông báo đẩy hoặc cổng SMS không gửi được thông báo lớp bị huỷ cho một hội viên, hệ thống xử lý thế nào? (Gửi lại sau / Thử kênh còn lại / Bỏ qua hội viên đó và tiếp tục / Khác - nêu rõ) | Bước 6, luồng 6a; hậu điều kiện tối thiểu | Mục 8 câu 3: "gửi thông báo cho những người đã đặt" và Mục 10 câu 1 không nêu xử lý khi gửi không được |
| Q-66 | Thông báo lớp bị huỷ gồm những thông tin nào ngoài việc lớp đã bị huỷ (lý do huỷ, giờ học, chi nhánh, hướng dẫn tiếp theo), và hiển thị theo định dạng nào? (Nêu danh sách thông tin) | Dữ liệu ra 1 (bước 6) | Mục 8 câu 3: "gửi thông báo cho những người đã đặt" không nêu nội dung thông báo |

Các câu hỏi đã cấp ở bước trước và làm đổi use case này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-20 (chỗ đã đặt của hội viên bị khoá quyền đặt lớp, có tính vào số người đặt chỗ), Q-22 (chỗ trống giữ riêng cho người đứng đầu danh sách chờ, có tính vào số người đặt chỗ), Q-23 (vị trí trong danh sách chờ của hội viên không xác nhận), Q-36 (cách xác định hội viên chưa cài ứng dụng), Q-43 (hệ thống tự huỷ lớp hay có bước nhân viên duyệt, gỡ), Q-49 (người kế tiếp trong danh sách chờ có được thông báo).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-015 (bảng 4b cột REQ; Mục 5) | Đặc tả dùng REQ-22 (hội viên đã đặt chỗ, bước 5 và bước 6), REQ-30 và REQ-34, REQ-35 (mốc chuyển chỗ và mốc tính vắng mặt bị huỷ ở bước 4), REQ-70 (loại lớp và giờ học ở Dữ liệu ra 1), REQ-76 (lớp đã bị huỷ vì sự cố, luồng 2a), nhưng sáu REQ này chưa nằm ở cột REQ của UC-015 | Thêm REQ-22, REQ-30, REQ-34, REQ-35, REQ-70, REQ-76 vào cột REQ của UC-015 ở bảng 4b và vào Mục 5 (ma trận REQ --> UC) |

## Vấn đề còn mở

Các mục Target đạt, trừ mục 12 (đạt một phần) và các điểm sau cần người dùng lưu ý:

- Target 5a: use case không có tác nhân người tham gia (tác nhân chính là tác nhân thời gian, hội viên là bên nhận thụ động), nên không có bước báo kết quả cho tác nhân người; bước 6 là bước thông báo cho hội viên theo nguồn.
- Target 12: bước 4 (huỷ mốc của UC-016, UC-013) và bước 5 (xác định hội viên đã đặt chỗ) không có câu gốc trực tiếp trong nguồn. Bước 4 viết theo quy tắc hẹn, huỷ mốc của use case làm mất hiệu lực dữ liệu mốc và kèm Q-64; bước 5 cần để bước 6 có đối tượng gửi. Luồng 2a suy từ việc quản lý chi nhánh huỷ lớp được nêu ở Mục 8 câu 4 (UC-014).
- Target 8: luồng 6a kết thúc bằng "Chờ Q-65", nên hậu điều kiện tối thiểu của luồng này chưa xác định hết; Q-65 ở mục Câu hỏi mở.
- Hai giá trị Kết thúc của luồng 2a, 2b (thất bại) và luồng 5a (thành công) là lựa chọn theo mục tiêu "hội viên đã đặt chỗ biết lớp bị huỷ"; không giá trị nào trong danh sách của F5.4 nêu đúng "không có việc cần làm".
- Sơ đồ chỉ có một partition (Phần mềm VietFit): bước 1 do tác nhân thời gian kích hoạt nên chủ thể ghi là hệ thống, ACT-09 và ACT-10 chỉ nhận yêu cầu gửi nên không có partition.
- BR-14 (kênh gửi thông báo theo trạng thái cài ứng dụng) được tách thành BR vì nguồn nêu như chính sách theo hội viên và nhiều use case dùng chung (UC-008, UC-011, UC-014); nếu người dùng coi đây là quy ước kỹ thuật của kênh thì chuyển sang yêu cầu của P06.
- "Giờ học" của Mục 8 câu 3 được giữ nguyên chữ của nguồn; các chỗ khác của nguồn dùng "giờ bắt đầu", đặc tả này không giải thích hai cụm là một.
- Giá trị ở cột Ví dụ của Dữ liệu ra 1 là giá trị minh hoạ, không phải dữ liệu của nguồn.
