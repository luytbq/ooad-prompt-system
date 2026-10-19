# P04 - Đặc tả use case UC-010 Đặt chỗ lớp nhóm - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-phong-tap.md; P00-problem-brief.md (phiên bản 1.0; các dòng REQ của UC-010 và REQ-69, REQ-70, REQ-73, REQ-76; mục Câu hỏi mở); P01-actors.md (phiên bản 1.0; Mục 2, mục Câu hỏi mở, Giả định); P02-usecases.md (phiên bản 1.1; dòng UC-010 ở bảng 4a, 4b; dòng EV-08; mục Câu hỏi mở, Giả định); P02R-review.md (phiên bản 1.0; mục Câu hỏi mở, Giả định); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2, mục Câu hỏi mở, Giả định); P04-uc-specs/_BR-register.md (BR-01 đến BR-05); mục Câu hỏi mở, Giả định của P04-uc-specs/UC-005-purchase-or-renew-membership-package.md (Q-50 đến Q-57). P05, P06: chưa có. UC_ID: UC-010. TEN_HE_THONG_TRONG_LUONG: Phần mềm VietFit. YEU_CAU_BO_SUNG: Không có |
| Phạm vi | UC-010 |
| Mã Q, ASM cuối đã cấp | Q-62; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-010 |
| Tên use case | Đặt chỗ lớp nhóm (Book Class Spot) |
| Tác nhân chính | ACT-02 Hội viên |
| Tác nhân phụ | Không có |
| Mô tả ngắn | Use case này mô tả tương tác giữa hội viên và Phần mềm VietFit khi hội viên muốn đặt chỗ một lớp nhóm. Kết quả là hội viên có chỗ trong lớp, hoặc có vị trí trong danh sách chờ khi lớp đã đủ chỗ. |
| Sự kiện kích hoạt | Hội viên muốn đặt chỗ một lớp nhóm (EV-08) |
| Tiền điều kiện | Hội viên đã được xác thực và đang có phiên làm việc. |
| Hậu điều kiện (thành công) | Hội viên có một chỗ đã đặt trong lớp nhóm đã chọn; số chỗ đã đặt của lớp tăng 1 và không vượt sức chứa (BR-11); số lớp hội viên đã đặt trong ngày tăng 1.<br>Khi use case kết thúc ở luồng 7a: hội viên có vị trí trong danh sách chờ của lớp nhóm và không có chỗ đã đặt trong lớp đó. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công, chỗ đã đặt và danh sách chờ của lớp nhóm không thay đổi. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-22, REQ-23, REQ-24, REQ-25, REQ-26, REQ-38, REQ-93, REQ-94, REQ-95 (theo P02); thêm REQ-69, REQ-70, REQ-73, REQ-76 (xem Đề xuất sửa artifact trước) |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Hội viên | Yêu cầu đặt chỗ lớp nhóm. |
| 2 | Phần mềm VietFit | Hiển thị lịch các lớp nhóm để hội viên chọn lớp (xem Dữ liệu ra 1). |
| 3 | Hội viên | Chọn lớp nhóm cần đặt chỗ trong lịch lớp nhóm. |
| 4 | Phần mềm VietFit | Kiểm tra quyền đặt lớp của hội viên không đang bị khoá (BR-09). |
| 5 | Phần mềm VietFit | Kiểm tra lớp nhóm đã chọn chưa bị huỷ và giờ học nằm trong thời hạn cho phép đặt chỗ (BR-06, BR-07). |
| 6 | Phần mềm VietFit | Kiểm tra số lớp hội viên đã đặt trong ngày chưa đạt mức tối đa (BR-08). |
| 7 | Phần mềm VietFit | Kiểm tra số chỗ đã đặt của lớp nhóm còn dưới sức chứa (BR-10, BR-11). |
| 8 | Phần mềm VietFit | Lưu chỗ đã đặt của hội viên trong lớp nhóm (BR-11). |
| 9 | Phần mềm VietFit | Hiển thị thông tin chỗ đã đặt cho hội viên (xem Dữ liệu ra 2). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 4a | Quyền đặt lớp của hội viên đang bị khoá (BR-09) | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo quyền đặt lớp đang bị khoá (BR-09). | Kết thúc use case (thất bại) |
| 5a | Lớp nhóm đã chọn đã bị huỷ | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo lớp nhóm đã bị huỷ. | Quay lại bước 2 |
| 5b | Lớp nhóm đã chọn chưa bị huỷ và giờ học nằm ngoài thời hạn cho phép đặt chỗ (BR-06, BR-07) | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo quy tắc bị vi phạm (BR-06, BR-07). | Quay lại bước 2 |
| 6a | Hội viên đã đặt đủ số lớp tối đa trong ngày (BR-08) | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo quy tắc bị vi phạm (BR-08). | Quay lại bước 2 |
| 7a | Lớp nhóm đã đủ chỗ: số chỗ đã đặt bằng sức chứa (BR-11, BR-12) | - | Vào danh sách chờ | - |
| 7a1 | | Phần mềm VietFit | Thông báo lớp nhóm đã đủ chỗ và đề nghị hội viên vào danh sách chờ (BR-12). | |
| 7a2 | | Hội viên | Yêu cầu vào danh sách chờ của lớp nhóm. | |
| 7a2a | Hội viên không yêu cầu vào danh sách chờ | - | - | Kết thúc use case (thất bại) |
| 7a3 | | Phần mềm VietFit | Thêm hội viên vào danh sách chờ của lớp nhóm (thứ tự xếp chờ Q-61). | |
| 7a4 | | Phần mềm VietFit | Hiển thị vị trí của hội viên trong danh sách chờ (xem Dữ liệu ra 3). | Kết thúc use case (thành công) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào: Không có. Ở bước 3 hội viên chỉ chọn một lớp trong danh sách ở Dữ liệu ra 1.

### Dữ liệu ra 1 (bước 2)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Loại lớp | Loại của lớp nhóm | Văn bản | Yoga |
| 2 | Phòng | Phòng tập diễn ra lớp | Văn bản | Phòng 2 |
| 3 | Huấn luyện viên | Huấn luyện viên phụ trách lớp | Văn bản (họ tên) | Nguyễn Thị Lan |
| 4 | Giờ học | Ngày và giờ bắt đầu của lớp | Ngày/tháng/năm giờ:phút, giờ 24 | 26/10/2026 18:00 |

### Dữ liệu ra 2 (bước 9)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Loại lớp | Loại của lớp nhóm đã đặt chỗ | Văn bản | Yoga |
| 2 | Phòng | Phòng tập diễn ra lớp | Văn bản | Phòng 2 |
| 3 | Huấn luyện viên | Huấn luyện viên phụ trách lớp | Văn bản (họ tên) | Nguyễn Thị Lan |
| 4 | Giờ học | Ngày và giờ bắt đầu của lớp | Ngày/tháng/năm giờ:phút, giờ 24 | 26/10/2026 18:00 |

### Dữ liệu ra 3 (bước 7a4)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Loại lớp | Loại của lớp nhóm đã đủ chỗ | Văn bản | Yoga |
| 2 | Giờ học | Ngày và giờ bắt đầu của lớp | Ngày/tháng/năm giờ:phút, giờ 24 | 26/10/2026 18:00 |
| 3 | Vị trí trong danh sách chờ | Thứ tự của hội viên trong danh sách chờ của lớp, 1 là đứng đầu (cách xếp thứ tự chờ Q-61) | Số nguyên dương | 3 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-06 | Hội viên chỉ được đặt chỗ lớp nhóm sớm nhất 7 ngày trước giờ học. | Ràng buộc | 5, 5b | REQ-23 | Mới |
| BR-07 | Đặt chỗ lớp nhóm cho tuần mới mở lúc 6 giờ sáng thứ Hai. | Ràng buộc | 5, 5b | REQ-93 | Mới |
| BR-08 | Mỗi hội viên được đặt chỗ tối đa 2 lớp nhóm trong một ngày. | Ràng buộc | 6, 6a | REQ-24 | Mới |
| BR-09 | Hội viên bị khoá quyền đặt lớp trong 7 ngày thì không đặt được chỗ lớp nhóm trong thời gian khoá. | Ràng buộc | 4, 4a | REQ-38 | Mới |
| BR-10 | Sức chứa của mỗi lớp nhóm được xác định theo phòng. | Sự kiện | 7, 7a | REQ-25 | Mới |
| BR-11 | Số chỗ đã đặt của một lớp nhóm không được vượt sức chứa, kể cả khi nhiều hội viên đặt chỗ cùng lúc. | Ràng buộc | 7, 7a, 8 | REQ-95, REQ-94 | Mới |
| BR-12 | Lớp nhóm đã đủ chỗ thì hội viên được vào danh sách chờ của lớp. | Kích hoạt hành động | 7a, 7a1 | REQ-26 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Phục vụ tới 1.500 hội viên đặt chỗ lớp nhóm cùng lúc khi mở đặt lớp cho tuần mới lúc 6 giờ sáng thứ Hai; ngưỡng thời gian phản hồi cho một lần đặt chỗ chờ Q-42 | Performance | REQ-94 |

## 8. Thông tin bổ sung

- Chỗ đã đặt và danh sách chờ do use case này tạo là dữ liệu mà UC-011, UC-012, UC-013, UC-015 và UC-016 đọc hoặc đổi.
- Giờ học của lớp là mốc tính hạn của UC-015 và UC-016 và do lịch lớp đặt (REQ-70). Use case này chỉ tạo chỗ đã đặt, không tạo, đổi hay huỷ mốc nào nên không có bước hẹn mốc.
- Ở bước 7 và bước 8, kết quả kiểm tra chỗ trống phải còn đúng tại lúc lưu chỗ đã đặt (BR-11). Khi hai hội viên cùng đặt chỗ cuối cùng của một lớp, hội viên đến sau đi theo luồng 7a.
- Thứ tự các bước kiểm tra 4, 5, 6, 7 là thứ tự trình bày của đặc tả này; nguồn không nêu thứ tự ưu tiên giữa các điều kiện.
- Mục 8a Kịch bản chính không lập vì MUC_CHI_TIET của hồ sơ dự án là GON.

## 9. Activity diagram

File: diagrams/P04-activity-UC-010.drawio (một trang, tên trang UC-010).

### Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-02 | Partition | Hội viên | - | - | - | Partition của ACT-02 | 0 | 0 | 520 | 1700 |
| P-SYS | Partition | Phần mềm VietFit | - | - | - | Partition của chủ ngữ hệ thống | 520 | 0 | 660 | 1700 |
| INIT | Initial | - | - | P-ACT-02 | 1 | Nút khởi đầu | 130 | 60 | 40 | 40 |
| A-1 | Action | Yêu cầu đặt chỗ lớp nhóm | - | P-ACT-02 | 1 | Sự kiện kích hoạt EV-08 | 60 | 140 | 180 | 60 |
| M-2 | Merge | - | - | P-SYS | 2 | Hợp các luồng: từ A-1 và quay lại từ 5a, 5b, 6a | 130 | 150 | 40 | 40 |
| A-2 | Action | Hiển thị lịch các lớp nhóm | - | P-SYS | 2 | Dữ liệu ra 1 | 60 | 230 | 180 | 60 |
| A-3 | Action | Chọn lớp nhóm cần đặt chỗ | - | P-ACT-02 | 3 | - | 60 | 230 | 180 | 60 |
| A-4 | Action | Kiểm tra quyền đặt lớp không bị khoá | - | P-SYS | 4 | BR-09 | 60 | 330 | 180 | 60 |
| D-4 | Decision | - | - | P-SYS | 4 | Rẽ nhánh luồng 4a | 130 | 430 | 40 | 40 |
| A-4a | Action | Thông báo quyền đặt lớp bị khoá | - | P-SYS | 4a | BR-09 | 380 | 420 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | 4a | Kết thúc use case (thất bại) | 450 | 520 | 40 | 40 |
| A-5 | Action | Kiểm tra lớp chưa huỷ và thời hạn đặt chỗ | - | P-SYS | 5 | BR-06, BR-07 | 60 | 510 | 180 | 60 |
| D-5 | Decision | - | - | P-SYS | 5 | Rẽ nhánh luồng 5a, 5b | 130 | 610 | 40 | 40 |
| A-5a | Action | Thông báo lớp nhóm đã bị huỷ | - | P-SYS | 5a | - | 380 | 600 | 180 | 60 |
| A-5b | Action | Thông báo quy tắc thời hạn đặt chỗ bị vi phạm | - | P-SYS | 5b | BR-06, BR-07 | 380 | 700 | 180 | 60 |
| A-6 | Action | Kiểm tra số lớp đã đặt trong ngày | - | P-SYS | 6 | BR-08 | 60 | 690 | 180 | 60 |
| D-6 | Decision | - | - | P-SYS | 6 | Rẽ nhánh luồng 6a | 130 | 810 | 40 | 40 |
| A-6a | Action | Thông báo quy tắc số lớp mỗi ngày bị vi phạm | - | P-SYS | 6a | BR-08 | 380 | 800 | 180 | 60 |
| A-7 | Action | Kiểm tra lớp còn chỗ trống | - | P-SYS | 7 | BR-10, BR-11 | 60 | 890 | 180 | 60 |
| D-7 | Decision | - | - | P-SYS | 7 | Rẽ nhánh luồng 7a | 130 | 990 | 40 | 40 |
| A-7a1 | Action | Thông báo lớp đủ chỗ, đề nghị vào danh sách chờ | - | P-SYS | 7a1 | BR-12 | 380 | 980 | 180 | 60 |
| D-7a2 | Decision | - | - | P-ACT-02 | 7a2 | Lựa chọn của hội viên, đặt ngay trước A-7a2 | 130 | 1090 | 40 | 40 |
| A-7a2 | Action | Yêu cầu vào danh sách chờ | - | P-ACT-02 | 7a2 | - | 300 | 1080 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-ACT-02 | 7a2a | Kết thúc use case (thất bại) | 130 | 1190 | 40 | 40 |
| A-7a3 | Action | Thêm hội viên vào danh sách chờ | - | P-SYS | 7a3 | - | 60 | 1400 | 180 | 60 |
| A-7a4 | Action | Hiển thị vị trí trong danh sách chờ | - | P-SYS | 7a4 | Dữ liệu ra 3 | 60 | 1500 | 180 | 60 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | 7a4 | Kết thúc use case (thành công) | 130 | 1600 | 40 | 40 |
| A-8 | Action | Lưu chỗ đã đặt của hội viên | - | P-SYS | 8 | BR-11 | 60 | 1090 | 180 | 60 |
| A-9 | Action | Hiển thị thông tin chỗ đã đặt | - | P-SYS | 9 | Dữ liệu ra 2 | 60 | 1190 | 180 | 60 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | 9 | Kết thúc use case (thành công) | 130 | 1290 | 40 | 40 |

### Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | M-2 | ControlFlow | - | Vượt qua partition | (460,170) |
| E-03 | M-2 | A-2 | ControlFlow | - | - | - |
| E-04 | A-2 | A-3 | ControlFlow | - | Vượt qua partition | (410,260) |
| E-05 | A-3 | A-4 | ControlFlow | - | Vượt qua partition | (150,360) |
| E-06 | A-4 | D-4 | ControlFlow | - | - | - |
| E-07 | D-4 | A-4a | ControlFlow | [bị khoá quyền đặt lớp] | Luồng 4a | - |
| E-08 | A-4a | FINAL-1 | ControlFlow | - | - | - |
| E-09 | D-4 | A-5 | ControlFlow | [không bị khoá] | Nhánh luồng chính | - |
| E-10 | A-5 | D-5 | ControlFlow | - | - | - |
| E-11 | D-5 | A-5a | ControlFlow | [lớp đã bị huỷ] | Luồng 5a | - |
| E-12 | D-5 | A-5b | ControlFlow | [lớp chưa huỷ, ngoài thời hạn đặt chỗ] | Luồng 5b | (780,630); (780,730) |
| E-13 | D-5 | A-6 | ControlFlow | [lớp chưa huỷ, trong thời hạn đặt chỗ] | Nhánh luồng chính | - |
| E-14 | A-5a | M-2 | ControlFlow | - | Quay lại bước 2 (M-2) | (1110,630); (1110,90); (670,90) |
| E-15 | A-5b | M-2 | ControlFlow | - | Quay lại bước 2 (M-2) | (1130,730); (1130,80); (670,80) |
| E-16 | A-6 | D-6 | ControlFlow | - | - | - |
| E-17 | D-6 | A-6a | ControlFlow | [đã đủ 2 lớp trong ngày] | Luồng 6a | - |
| E-18 | A-6a | M-2 | ControlFlow | - | Quay lại bước 2 (M-2) | (1150,830); (1150,70); (670,70) |
| E-19 | D-6 | A-7 | ControlFlow | [chưa đủ 2 lớp trong ngày] | Nhánh luồng chính | - |
| E-20 | A-7 | D-7 | ControlFlow | - | - | - |
| E-21 | D-7 | A-8 | ControlFlow | [còn chỗ] | Nhánh luồng chính | - |
| E-22 | D-7 | A-7a1 | ControlFlow | [đã đủ chỗ] | Luồng 7a | - |
| E-23 | A-7a1 | D-7a2 | ControlFlow | - | Vượt qua partition | (990,1060); (150,1060) |
| E-24 | D-7a2 | A-7a2 | ControlFlow | [vào danh sách chờ] | - | - |
| E-25 | D-7a2 | FINAL-2 | ControlFlow | [không vào danh sách chờ] | Luồng 7a2a, không có hành động | - |
| E-26 | A-7a2 | A-7a3 | ControlFlow | - | Vượt qua partition | (390,1430) |
| E-27 | A-7a3 | A-7a4 | ControlFlow | - | - | - |
| E-28 | A-7a4 | FINAL-3 | ControlFlow | - | - | - |
| E-29 | A-8 | A-9 | ControlFlow | - | - | - |
| E-30 | A-9 | FINAL-4 | ControlFlow | - | - | - |

### Bảng đối chiếu

| Bước UC | Node |
|---|---|
| 1 | INIT, A-1 |
| 2 | M-2, A-2 |
| 3 | A-3 |
| 4 | A-4, D-4 |
| 4a | A-4a, FINAL-1 |
| 5 | A-5, D-5 |
| 5a | A-5a (về M-2) |
| 5b | A-5b (về M-2) |
| 6 | A-6, D-6 |
| 6a | A-6a (về M-2) |
| 7 | A-7, D-7 |
| 7a1 | A-7a1 |
| 7a2 | D-7a2, A-7a2 |
| 7a2a | FINAL-2 |
| 7a3 | A-7a3 |
| 7a4 | A-7a4, FINAL-3 |
| 8 | A-8 |
| 9 | A-9, FINAL-4 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-58 | Hội viên được đặt chỗ hoặc vào danh sách chờ muộn nhất vào lúc nào trước giờ học, và lớp đã bắt đầu thì còn đặt được không? (Đến lúc lớp bắt đầu / Đến một mốc trước giờ học - nêu rõ / Không giới hạn) | Bước 5, luồng 5b; BR-06 | Mục 3 câu 1: "sớm nhất 7 ngày trước giờ học" chỉ nêu mốc sớm nhất; mốc "dưới 1 giờ" (Mục 3 câu 5) và "2 giờ" (Mục 4 câu 1, Mục 8 câu 3) nêu cho các việc khác |
| Q-59 | Hội viên đã có chỗ đặt hoặc đang đứng trong danh sách chờ của một lớp có được yêu cầu đặt chỗ lớp đó lần nữa không? (Không - từ chối / Có - nêu cách tính chỗ) | Thêm luồng kiểm tra giữa bước 5 và bước 6; BR-08, BR-11 | Mục 3 câu 1 đến câu 3: nguồn không nêu việc đặt trùng cùng một lớp |
| Q-60 | Mức tối đa 2 lớp "trong một ngày" tính theo ngày diễn ra lớp hay ngày hội viên đặt chỗ, và có tính các lớp mà hội viên đang đứng trong danh sách chờ không? (Ngày diễn ra lớp / Ngày đặt chỗ; có tính hoặc không tính lớp trong danh sách chờ) | Bước 6, luồng 6a, Dữ liệu ra; BR-08 | Mục 3 câu 1: "tối đa 2 lớp trong một ngày" |
| Q-61 | Danh sách chờ của một lớp xếp thứ tự thế nào để xác định người đứng đầu? (Theo thời điểm vào danh sách, vào trước đứng trước / Khác - nêu rõ) | Luồng 7a3, Dữ liệu ra 3; UC-012, UC-013 | Mục 3 câu 3, câu 4: nguồn dùng "người đứng đầu danh sách chờ" và "người kế tiếp" nhưng không nêu quy tắc xếp thứ tự |
| Q-62 | Khi lớp đã đủ chỗ, hệ thống tự đưa hội viên vào danh sách chờ hay hội viên phải chọn vào danh sách chờ? (Tự đưa vào / Hội viên chọn) | Luồng 7a, 7a1, 7a2, 7a2a; BR-12 | Mục 3 câu 3: "Lớp đã đủ chỗ thì hội viên được vào danh sách chờ" |

Các câu hỏi đã cấp ở bước trước và làm đổi use case này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-03 (người tạo danh mục phòng và sức chứa, cách hiểu sức chứa lớp), Q-11 (cách mở đặt chỗ, mâu thuẫn BR-06 và BR-07), Q-12 (điều kiện về gói tập khi đặt chỗ), Q-19 (hội viên đang bảo lưu gói có được đặt chỗ không), Q-20 (chỗ đã đặt và vị trí chờ của hội viên bị khoá quyền đặt lớp), Q-22 (chỗ trống được giữ riêng trong 30 phút có tính vào số chỗ đã đặt không), Q-23 (vị trí trong danh sách chờ của hội viên không xác nhận nhận chỗ), Q-32 (thời lượng lớp), Q-42 (ngưỡng phản hồi khi 1.500 hội viên đặt chỗ cùng lúc), Q-43 (lớp tự huỷ do hệ thống thực hiện).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-010 (bảng 4b cột REQ; Mục 5) | Đặc tả dùng REQ-69 và REQ-70 (lịch lớp nhóm gồm loại lớp, phòng, huấn luyện viên và giờ, làm dữ liệu cho bước 2, bước 9 và bước 7a4) và REQ-73, REQ-76 (lớp nhóm bị huỷ, làm căn cứ cho luồng 5a), nhưng bốn REQ này chưa nằm ở cột REQ của UC-010 | Thêm REQ-69, REQ-70, REQ-73, REQ-76 vào cột REQ của UC-010 ở bảng 4b và vào Mục 5 (ma trận REQ --> UC) |

## Vấn đề còn mở

Các mục Target đạt, trừ các điểm sau cần người dùng lưu ý:

- Target 5a (đạt một phần): luồng 7a2a (hội viên không yêu cầu vào danh sách chờ) không có bước hệ thống báo kết quả riêng, vì bước 7a1 đã báo cho hội viên là lớp đã đủ chỗ và đây là lựa chọn của chính hội viên. Mọi luồng thay thế khác kết thúc use case đều có bước hệ thống báo kết quả. Cách báo là hiển thị trên ứng dụng (REQ-22 "trên ứng dụng"); nguồn không nêu gửi thêm thông báo đẩy hoặc SMS khi đặt chỗ nên không có Q riêng.
- Target 12 (đạt một phần): bước 2 (hiển thị lịch lớp để chọn) lấy từ CAND-21, bước 9 và các thông báo của luồng 4a, 5a, 5b, 6a cần có để hội viên biết kết quả. Luồng 7a theo hướng hội viên chọn vào danh sách chờ (REQ-26 "có thể vào danh sách chờ") là một trong hai cách đọc của nguồn; nếu Q-62 trả lời "Tự đưa vào" thì bỏ 7a1, 7a2, 7a2a và sửa D-7a2 trong sơ đồ.
- Target 12a: BR-06 và BR-07 mâu thuẫn nhau (Q-11). Ví dụ lớp bắt đầu lúc 18:00 thứ Hai 26/10/2026: theo BR-06 sớm nhất đặt được từ 18:00 ngày 19/10/2026 (26 - 7 = 19); nếu hiểu BR-07 là tuần của lớp mở đặt lúc 6:00 thứ Hai 26/10/2026 thì sớm nhất đặt từ 6:00 ngày 26/10/2026, muộn hơn BR-06 đúng 7 ngày trừ 12 giờ (18:00 ngày 19/10 đến 6:00 ngày 26/10). Vì vậy bước 5 và luồng 5b dẫn cả hai BR mà không chọn bên nào; hai BR không thể cùng là điều kiện đúng cho mọi lớp.
- Q-12 chưa trả lời nên đặc tả không có kiểm tra hội viên phải có gói tập (còn hiệu lực, áp dụng cho chi nhánh của lớp) trước khi đặt chỗ. Nếu Q-12 trả lời cần gói thì thêm bước kiểm tra và luồng thay thế, và thêm tiền điều kiện hoặc BR tương ứng.
- Luồng 4a chặn cả việc vào danh sách chờ của hội viên bị khoá, vì P02 gộp việc vào danh sách chờ vào mục tiêu đặt chỗ (CAND-20); nguồn không nêu riêng điều này.
- REQ-93 cần một tác nhân thời gian theo tuần nếu Q-11 trả lời cả tuần mở lúc 6 giờ sáng thứ Hai (đã có đề xuất ở P02); đặc tả này không có bước hẹn mốc mở đặt chỗ.
- Các giá trị ở cột Ví dụ (loại lớp, phòng, tên huấn luyện viên, giờ học) là giá trị minh hoạ, không phải dữ liệu của nguồn.
