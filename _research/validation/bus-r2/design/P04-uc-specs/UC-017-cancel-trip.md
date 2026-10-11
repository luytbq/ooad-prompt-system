# P04 - Đặc tả use case UC-017 Huỷ chuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-khach.md; P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09; các dòng REQ liên quan, mục Câu hỏi mở và Giả định); P01-actors.md (phiên bản 1.0, Q-39, ASM-11; Mục 2); P02-usecases.md (phiên bản 1.1, Q-42, ASM-16); P02R-review.md (phiên bản 1.0, Q-42, ASM-16; mục Câu hỏi mở và Giả định); P03-usecase-model.md (phiên bản 1.0, Q-43, ASM-17; Mục 1 và Mục 2); P04-uc-specs/_BR-register.md (BR-01 đến BR-06); P04-uc-specs/UC-009-book-ticket-online.md (Q-45, ASM-24; mục Câu hỏi mở, Giả định và dữ liệu vé, giá vé, mã vé). Placeholder UC_ID = UC-017; TEN_HE_THONG_TRONG_LUONG, YEU_CAU_BO_SUNG: Không có (chủ ngữ hệ thống là "Hệ thống"). Mã Q, ASM cấp tiếp từ Q-45, ASM-24; mã BR cấp tiếp từ BR-06 |
| Phạm vi | UC-017 |
| Mã Q, ASM cuối đã cấp | Q-50, ASM-33 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-017 |
| Tên use case | Huỷ chuyến (Cancel Trip) |
| Tác nhân chính | ACT-03 Nhân viên điều hành |
| Tác nhân phụ | ACT-06 Cổng thanh toán<br>ACT-07 Cổng SMS |
| Mô tả ngắn | Use case này mô tả tương tác giữa nhân viên điều hành và hệ thống khi nhân viên điều hành phải huỷ một chuyến vì xe hỏng hoặc thời tiết. Kết quả là chuyến được ghi nhận đã huỷ, hành khách đã có vé được báo qua SMS và vé mua trực tuyến được hoàn 100% giá vé; vé mua tại quầy chờ hoàn tiền mặt tại quầy. |
| Sự kiện kích hoạt | Chuyến phải huỷ (EV-16) |
| Tiền điều kiện | Nhân viên điều hành đã được xác thực và đang có phiên làm việc. |
| Hậu điều kiện (thành công) | Chuyến đã chọn ở trạng thái "Đã huỷ" kèm lý do huỷ chuyến (ASM-25); mốc 60 phút và mốc 15 phút trước giờ xuất bến của chuyến này không còn được hẹn (ASM-28).<br>Mọi vé đang có hiệu lực của chuyến ở trạng thái "Đã huỷ"; mỗi vé đã thanh toán có trạng thái hoàn tiền "Chưa hoàn" hoặc "Đã hoàn" (ASM-29).<br>Mỗi vé mua trực tuyến mà Cổng thanh toán xác nhận đã hoàn có trạng thái hoàn tiền "Đã hoàn" với số tiền hoàn bằng 100% giá vé (BR-07); mỗi vé mua tại quầy đã thanh toán giữ trạng thái "Chưa hoàn" để UC-018 hoàn tiền mặt tại quầy (BR-08).<br>Yêu cầu gửi SMS thông báo huỷ chuyến đã được chuyển cho Cổng SMS cho từng số điện thoại người đi của chuyến; số điện thoại chưa gửi được (luồng 9a) và vé mua trực tuyến chưa hoàn được (luồng 12a) được ghi nhận. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công (luồng *a), chuyến và các vé không thay đổi, không có SMS nào được gửi và không có yêu cầu hoàn tiền nào được chuyển cho Cổng thanh toán. |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-55, REQ-56, REQ-57, REQ-58, REQ-59, REQ-16, REQ-21 (theo P02); REQ-23 (tiền điều kiện), REQ-46, REQ-47 (chuyến trong lịch chạy ở bước 2 và 3), REQ-31, REQ-32 (mốc của UC-007 ở bước 6), REQ-69, REQ-70 (mốc của UC-025 ở bước 6), REQ-66 (trạng thái vé đã huỷ ở bước 7), REQ-09, REQ-19 (số điện thoại người đi, mã vé ở bước 8), REQ-25, REQ-28, REQ-30 (phân loại vé mua tại quầy, vé đặt qua điện thoại ở bước 7 và 8), REQ-15 (giao dịch thanh toán được hoàn ở bước 11), REQ-60, REQ-61 (giá vé ở bước 11) thêm theo [Action] 1c, xem Đề xuất sửa artifact trước |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Nhân viên điều hành | Yêu cầu huỷ chuyến. |
| 2 | Hệ thống | Hiển thị các chuyến trong lịch chạy (xem Dữ liệu ra 1). |
| 3 | Nhân viên điều hành | Chọn chuyến cần huỷ và lý do huỷ chuyến (xem Dữ liệu vào 1, ASM-25). |
| 4 | Hệ thống | Kiểm tra chuyến đã chọn chưa bị huỷ (BR-09) và chưa đến giờ xuất bến (BR-10). |
| 5 | Hệ thống | Lưu chuyến ở trạng thái "Đã huỷ" kèm lý do huỷ chuyến. |
| 6 | Hệ thống | Huỷ mốc 60 phút trước giờ xuất bến của UC-007 Huỷ vé đặt chỗ quá hạn và mốc 15 phút trước giờ xuất bến của UC-025 Gửi danh sách hành khách cho phụ xe, cho chuyến đã huỷ (ASM-28). |
| 7 | Hệ thống | Chuyển các vé đang có hiệu lực của chuyến sang trạng thái "Đã huỷ" và ghi nhận các vé đã thanh toán chưa được hoàn tiền (ASM-29). |
| 8 | Hệ thống | Gửi SMS thông báo huỷ chuyến tới một số điện thoại người đi qua Cổng SMS (BR-11, ASM-30, xem Dữ liệu ra 2). |
| 9 | Cổng SMS | Trả kết quả gửi SMS. |
| 10 | Hệ thống | Lặp lại bước 8-9 cho đến khi đã gửi SMS cho mọi số điện thoại người đi của chuyến. |
| 11 | Hệ thống | Yêu cầu Cổng thanh toán hoàn tiền cho một vé mua trực tuyến chưa hoàn, bằng 100% giá vé (BR-07, BR-08, ASM-32, xem Dữ liệu ra 3). |
| 12 | Cổng thanh toán | Trả kết quả hoàn tiền. |
| 13 | Hệ thống | Lặp lại bước 11-12 cho đến khi đã yêu cầu hoàn tiền cho mọi vé mua trực tuyến của chuyến. |
| 14 | Hệ thống | Hiển thị kết quả huỷ chuyến cho nhân viên điều hành (xem Dữ liệu ra 4). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 4a | Chuyến đã chọn đã bị huỷ (BR-09) | Hệ thống | Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã bị huỷ (BR-09). | Quay lại bước 3 |
| 4b | Chuyến đã chọn chưa bị huỷ và đã đến giờ xuất bến (BR-10, ASM-26) | Hệ thống | Từ chối yêu cầu huỷ chuyến và thông báo chuyến đã đến giờ xuất bến (BR-10). | Quay lại bước 3 |
| 7a | Chuyến không có vé nào đang có hiệu lực | - | - | Tiếp tục bước 14 |
| 9a | Cổng SMS báo lỗi hoặc không trả kết quả cho SMS gửi tới số điện thoại này | Hệ thống | Ghi nhận số điện thoại và mã các vé chưa được báo qua SMS (ASM-31). | Tiếp tục bước 10 (thành công một phần) |
| 10a | Đã gửi SMS cho mọi số điện thoại người đi và chuyến không có vé mua trực tuyến cần hoàn tiền | - | - | Tiếp tục bước 14 |
| 12a | Cổng thanh toán báo hoàn tiền không thành công hoặc không trả kết quả cho vé này | Hệ thống | Ghi nhận vé chưa được hoàn tiền và giữ trạng thái hoàn tiền "Chưa hoàn" của vé (ASM-33). | Tiếp tục bước 13 (thành công một phần) |
| *a | Tại bất kỳ bước nào trước bước 5, nhân viên điều hành bỏ yêu cầu huỷ chuyến (ASM-27) | Hệ thống | Bỏ yêu cầu huỷ chuyến, không thay đổi dữ liệu và thông báo đã bỏ yêu cầu. | Kết thúc use case (thất bại) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 3)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Chuyến cần huỷ | Chuyến trong lịch chạy mà nhân viên điều hành chọn để huỷ | Có | Là chuyến có trong lịch chạy, chưa bị huỷ (BR-09) và chưa đến giờ xuất bến (BR-10) | Hà Nội - Vinh, 15/12/2026 20:30 |
| 2 | Lý do huỷ chuyến | Lý do nhân viên điều hành phải huỷ chuyến (ASM-25) | Có | Một trong hai giá trị: Xe hỏng, Thời tiết (ASM-25, Q-36) | Xe hỏng |

Dữ liệu ra 1 (bước 2)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Tuyến | Tuyến của chuyến (REQ-47) | Chuỗi ký tự, điểm đi - điểm đến | Hà Nội - Vinh |
| 2 | Giờ xuất bến | Ngày giờ xuất bến của chuyến (REQ-47) | Ngày giờ dạng dd/MM/yyyy HH:mm | 15/12/2026 20:30 |
| 3 | Xe | Xe được xếp vào chuyến (REQ-47) | Chuỗi ký tự | Xe giường nằm 40 chỗ |
| 4 | Tài xế | Tài xế được xếp vào chuyến (REQ-47) | Chuỗi ký tự | Trần Văn Bình |
| 5 | Trạng thái chuyến | Chuyến đã huỷ hay chưa (BR-09) | Chuỗi ký tự | Chưa huỷ |

Dữ liệu ra 2 (bước 8)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Số điện thoại nhận | Số điện thoại người đi của các vé trên chuyến (REQ-09) | Chuỗi chữ số (định dạng theo Q-44) | 0912345678 |
| 2 | Nội dung thông báo | Thông báo chuyến bị huỷ, nêu tuyến và giờ xuất bến của chuyến (ASM-30) | Văn bản, ngày giờ dạng dd/MM/yyyy HH:mm | Chuyến Hà Nội - Vinh 15/12/2026 20:30 đã bị huỷ |
| 3 | Mã vé | Mã các vé của số điện thoại đó trên chuyến, mỗi chỗ một mã vé (BR-04, REQ-19) | Danh sách mã vé ngăn bằng dấu phẩy | SV0001, SV0002 |

Dữ liệu ra 3 (bước 11)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Giao dịch thanh toán của vé | Giao dịch đã thu tiền vé qua Cổng thanh toán (kết quả của UC-010) mà khoản hoàn gắn vào | Chuỗi ký tự do Cổng thanh toán cấp | GD0042 |
| 2 | Mã vé | Mã của vé được hoàn tiền | Chuỗi ký tự | SV0001 |
| 3 | Số tiền hoàn | 100% giá vé của vé (BR-07) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 250.000 đ |

Dữ liệu ra 4 (bước 14)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Chuyến đã huỷ | Tuyến và giờ xuất bến của chuyến đã huỷ | Như Dữ liệu ra 1, dòng 1 và 2 | Hà Nội - Vinh, 15/12/2026 20:30 |
| 2 | Số vé đã huỷ | Số vé đang có hiệu lực đã chuyển sang trạng thái "Đã huỷ" | Số nguyên | 5 |
| 3 | Số điện thoại đã báo qua SMS | Số số điện thoại có SMS đã chuyển cho Cổng SMS | Số nguyên | 4 |
| 4 | Số điện thoại chưa báo được | Số điện thoại và mã các vé chưa gửi được SMS (ASM-31) | Danh sách, mỗi số một dòng; "Không có" khi trống | Không có |
| 5 | Vé mua trực tuyến đã hoàn | Số vé và tổng số tiền đã hoàn | Số vé, rồi tổng tiền dạng số nguyên phân cách hàng nghìn bằng dấu chấm, kèm "đ" | 3 vé, 750.000 đ |
| 6 | Vé mua trực tuyến chưa hoàn được | Mã các vé Cổng thanh toán chưa hoàn được tiền (ASM-33) | Danh sách mã vé; "Không có" khi trống | Không có |
| 7 | Số vé mua tại quầy chờ hoàn tiền mặt | Số vé đã thanh toán tại quầy chờ UC-018 hoàn tiền mặt (BR-08) | Số nguyên | 1 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-04 | Mỗi chỗ có một mã vé. | Ràng buộc | 8, Dữ liệu ra 2 | REQ-19 | Đã có |
| BR-07 | Số tiền hoàn cho mỗi vé của chuyến bị huỷ bằng 100% giá vé của vé đó. | Tính toán | 11, Dữ liệu ra 3 | REQ-58 | Mới |
| BR-08 | Vé của chuyến bị huỷ được hoàn tiền qua cùng kênh với kênh mua vé: vé mua trực tuyến hoàn qua cổng thanh toán, vé mua tại quầy hoàn tiền mặt tại quầy (ASM-08). | Ràng buộc | 7, 11, Dữ liệu ra 4 | REQ-57, REQ-59 | Mới |
| BR-09 | Chuyến đã bị huỷ không được huỷ lại (ASM-26). | Ràng buộc | 4, 4a, Dữ liệu vào 1, Dữ liệu ra 1 | REQ-55 | Mới |
| BR-10 | Chuyến từ giờ xuất bến trở đi không được huỷ (ASM-26). | Ràng buộc | 4, 4b, Dữ liệu vào 1 | REQ-55 | Mới |
| BR-11 | Khi một chuyến bị huỷ, mọi hành khách đã có vé của chuyến phải được thông báo qua SMS (phạm vi "đã có vé" theo ASM-30). | Kích hoạt hành động | 8, 9, 10 | REQ-56 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Chỉ nhân viên điều hành được huỷ chuyến. | Security | REQ-55 |
| 2 | Mỗi vé mua trực tuyến của chuyến bị huỷ được yêu cầu hoàn tiền đúng một lần với số tiền bằng 100% giá vé, không hoàn quá số đã thu. | Reliability | REQ-58 |

## 8. Thông tin bổ sung

- Vé đang có hiệu lực là vé chưa bị huỷ, chưa được trả và chưa được đổi sang chuyến khác (ASM-29). Vé mua tại quầy gồm vé bán tại quầy và vé đặt qua điện thoại đã thanh toán tại quầy. Vé đặt qua điện thoại chưa thanh toán chưa có khoản tiền nào đã thu, nên được huỷ cùng chuyến, nhận SMS (ASM-30) và không có hoàn tiền.
- Ví dụ tính số SMS: chuyến có 5 vé đang có hiệu lực, gồm SV0001, SV0002 (số 0912345678), SV0003 (số 0987654321) mua trực tuyến, SV0004 (số 0933222111) mua tại quầy, SV0005 (số 0944555666) đặt qua điện thoại chưa thanh toán. Có 4 số điện thoại khác nhau nên gửi 4 SMS (ASM-30); số 0912345678 nhận một SMS nêu hai mã vé SV0001, SV0002.
- Ví dụ tính số tiền hoàn (BR-07): mỗi vé mua trực tuyến giá 250.000 đ thì số tiền hoàn của một vé là 100% x 250.000 = 250.000 đ; 3 vé mua trực tuyến thì tổng tiền hoàn là 3 x 250.000 = 750.000 đ. Vé SV0004 chờ UC-018 hoàn 250.000 đ tiền mặt; vé SV0005 không có hoàn tiền.
- Giá vé dùng để hoàn là giá vé của từng vé đã ghi khi bán (dữ liệu của UC-009, giá do UC-023 Đặt giá vé và UC-024 Đặt mức tăng giá ngày lễ cung cấp, REQ-60, REQ-61); giá vé hiện hành sau này không ảnh hưởng số tiền hoàn.
- Kết cục cần khớp khi đặc tả UC-007 và UC-025: mốc theo giờ xuất bến của chuyến đã huỷ bị huỷ (ASM-28, chờ Q-47), nên hai use case này không kích hoạt cho chuyến đó.
- Kết cục cần khớp khi đặc tả UC-018: UC-018 nhận các vé mua tại quầy đã thanh toán của chuyến "Đã huỷ" có trạng thái hoàn tiền "Chưa hoàn" và chuyển sang "Đã hoàn" sau khi hoàn tiền mặt (BR-07, BR-08).
- Luồng 9a và 12a ghi nhận số điện thoại chưa gửi được SMS và vé chưa hoàn được tiền để xử lý lại sau; cơ chế xử lý lại (người thực hiện, thời điểm, số lần thử) chờ Q-49, Q-50 và do P06 đặc tả.
- API hoàn tiền của Cổng thanh toán chưa có tài liệu (project-profile.md, HE_THONG_NGOAI); việc hoàn một phần số tiền của giao dịch chờ Q-20 (ASM-32).
- P03 không có quan hệ include, extend hay generalization cho UC-017; UC-017 chỉ nối với ACT-03, ACT-06, ACT-07 bằng association (RL-28, RL-29, RL-30).
- Chuyến bị huỷ sau mốc 15 phút trước giờ xuất bến thì danh sách hành khách đã được UC-025 gửi về máy soát vé; việc cập nhật máy soát vé khi vé bị huỷ sau thời điểm gửi danh sách chờ Q-29 (UC-025, UC-026).
- Dữ liệu dùng chung: chuyến lấy từ lịch chạy do UC-016 lập; vé do UC-009 và các use case bán vé tạo; vé chuyển sang "Đã huỷ" làm UC-026 báo mã vé không hợp lệ (REQ-66) và UC-011 hiển thị vé đã huỷ theo Q-26.

## 8a. Kịch bản chính

- KB1: Luồng chính --> huỷ chuyến thành công, mọi số điện thoại được báo qua SMS và mọi vé mua trực tuyến được hoàn 100% giá vé.
- KB2: Luồng chính đến bước 4 + 4a, quay lại bước 3, rồi luồng chính --> chọn lại chuyến và huỷ chuyến thành công.
- KB3: Luồng chính đến bước 10 + 10a --> huỷ chuyến chỉ có vé mua tại quầy hoặc vé đặt chưa thanh toán, SMS đã gửi, không có hoàn tiền qua cổng.
- KB4: Luồng chính + 9a + 12a --> huỷ chuyến thành công một phần, số điện thoại chưa báo được và vé chưa hoàn được tiền được ghi nhận.
- KB5: Luồng chính đến bước 3 + *a --> nhân viên điều hành bỏ yêu cầu, không có dữ liệu nào thay đổi.

## 9. Activity diagram

File: diagrams/P04-activity-UC-017.drawio (một trang, tên trang "UC-017"). Bảng Node và bảng Edge dưới đây là nguồn chuẩn. Toạ độ x của node trong bảng Node tính trong partition chứa nó; toạ độ trong cột Điểm uốn là toạ độ tuyệt đối. Cổng ra, cổng vào của mỗi cạnh (exitX, exitY, entryX, entryY) suy ra từ hướng của điểm uốn đầu và điểm uốn cuối (hoặc từ node đối diện khi không có điểm uốn). Bước 10 và bước 13 là bước "Lặp lại" nên ánh xạ sang decision D-10, D-13 (F10.2); luồng 7a và 10a không có hành động nên là cạnh mang guard tới merge node M-14. Luồng *a thể hiện bằng note N-*a, không vẽ cạnh.

Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-03 | Partition | Nhân viên điều hành | - | - | - | Cao 2620 | 0 | 0 | 300 | 2620 |
| P-SYS | Partition | Hệ thống | - | - | - | Cao 2620 | 300 | 0 | 800 | 2620 |
| P-ACT-07 | Partition | Cổng SMS | - | - | - | Cao 2620 | 1100 | 0 | 300 | 2620 |
| P-ACT-06 | Partition | Cổng thanh toán | - | - | - | Cao 2620 | 1400 | 0 | 300 | 2620 |
| INIT | Initial | - | - | P-ACT-03 | 1 | Nút khởi đầu | 130 | 60 | 40 | 40 |
| A-1 | Action | Yêu cầu huỷ chuyến | - | P-ACT-03 | 1 | - | 60 | 140 | 180 | 60 |
| A-2 | Action | Hiển thị các chuyến trong lịch chạy | - | P-SYS | 2 | - | 140 | 260 | 180 | 60 |
| M-3 | Merge | - | - | P-ACT-03 | 3 | Nhận luồng từ A-2 và từ A-4a, A-4b (quay lại bước 3) | 130 | 380 | 40 | 40 |
| A-3 | Action | Chọn chuyến và lý do huỷ | - | P-ACT-03 | 3 | - | 60 | 460 | 180 | 60 |
| A-4 | Action | Kiểm tra trạng thái chuyến | - | P-SYS | 4 | - | 140 | 600 | 180 | 60 |
| D-4 | Decision | - | - | P-SYS | 4 | Ưu tiên 4a, 4b theo ASM-26 | 210 | 700 | 40 | 40 |
| A-4a | Action | Từ chối, báo chuyến đã bị huỷ | - | P-SYS | 4a | - | 440 | 690 | 180 | 60 |
| A-4b | Action | Từ chối, báo chuyến đã xuất bến | - | P-SYS | 4b | - | 440 | 790 | 180 | 60 |
| A-5 | Action | Lưu chuyến ở trạng thái Đã huỷ | - | P-SYS | 5 | - | 140 | 800 | 180 | 60 |
| A-6 | Action | Huỷ mốc theo giờ xuất bến của chuyến | - | P-SYS | 6 | Mốc của UC-007 và UC-025 (ASM-28) | 140 | 900 | 180 | 60 |
| A-7 | Action | Chuyển các vé của chuyến sang Đã huỷ | - | P-SYS | 7 | - | 140 | 1000 | 180 | 60 |
| D-7 | Decision | - | - | P-SYS | 7 | Luồng 7a | 210 | 1100 | 40 | 40 |
| M-8 | Merge | - | - | P-SYS | 8 | Nhận luồng từ D-7 và từ D-10 (lặp lại bước 8-9) | 210 | 1200 | 40 | 40 |
| A-8 | Action | Gửi SMS huỷ chuyến cho một số điện thoại | - | P-SYS | 8 | Gửi qua Cổng SMS | 140 | 1280 | 180 | 60 |
| A-9 | Action | Trả kết quả gửi SMS | - | P-ACT-07 | 9 | - | 60 | 1380 | 180 | 60 |
| D-9 | Decision | - | - | P-SYS | 9 | Hệ thống đánh giá kết quả do Cổng SMS trả về | 210 | 1480 | 40 | 40 |
| A-9a | Action | Ghi nhận số điện thoại chưa báo được | - | P-SYS | 9a | - | 440 | 1470 | 180 | 60 |
| M-10 | Merge | - | - | P-SYS | 10 | Nhận luồng từ D-9 và từ A-9a | 210 | 1580 | 40 | 40 |
| D-10 | Decision | - | - | P-SYS | 10 | Bước "Lặp lại" bước 8-9; có thêm nhánh 10a | 210 | 1660 | 40 | 40 |
| M-11 | Merge | - | - | P-SYS | 11 | Nhận luồng từ D-10 và từ D-13 (lặp lại bước 11-12) | 210 | 1760 | 40 | 40 |
| A-11 | Action | Yêu cầu hoàn 100% giá vé cho một vé | - | P-SYS | 11 | Gọi Cổng thanh toán | 140 | 1840 | 180 | 60 |
| A-12 | Action | Trả kết quả hoàn tiền | - | P-ACT-06 | 12 | - | 60 | 1940 | 180 | 60 |
| D-12 | Decision | - | - | P-SYS | 12 | Hệ thống đánh giá kết quả do Cổng thanh toán trả về | 210 | 2040 | 40 | 40 |
| A-12a | Action | Ghi nhận vé chưa hoàn được tiền | - | P-SYS | 12a | - | 440 | 2030 | 180 | 60 |
| M-13 | Merge | - | - | P-SYS | 13 | Nhận luồng từ D-12 và từ A-12a | 210 | 2140 | 40 | 40 |
| D-13 | Decision | - | - | P-SYS | 13 | Bước "Lặp lại" bước 11-12 | 210 | 2220 | 40 | 40 |
| M-14 | Merge | - | - | P-SYS | 14 | Nhận luồng từ D-7 (7a), D-10 (10a) và D-13 | 210 | 2320 | 40 | 40 |
| A-14 | Action | Hiển thị kết quả huỷ chuyến | - | P-SYS | 14 | - | 140 | 2400 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | 14 | Kết thúc thành công | 210 | 2500 | 40 | 40 |
| N-*a | Note | *a: Tại bất kỳ bước nào trước bước 5, nhân viên điều hành bỏ yêu cầu huỷ chuyến. Hệ thống bỏ yêu cầu, không thay đổi dữ liệu và thông báo đã bỏ yêu cầu. Kết thúc use case (thất bại). | - | P-ACT-03 | *a | Thể hiện bằng note theo F10.2, không vẽ cạnh | 30 | 600 | 240 | 160 |

Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | - | (530,170) |
| E-03 | A-2 | M-3 | ControlFlow | - | - | (530,350); (150,350) |
| E-04 | M-3 | A-3 | ControlFlow | - | - | - |
| E-05 | A-3 | A-4 | ControlFlow | - | - | (530,490) |
| E-06 | A-4 | D-4 | ControlFlow | - | - | - |
| E-07 | D-4 | A-4a | ControlFlow | [chuyến đã bị huỷ] | Luồng 4a | - |
| E-08 | D-4 | A-4b | ControlFlow | [chuyến chưa bị huỷ, đã xuất bến] | Luồng 4b | (700,720); (700,820) |
| E-09 | D-4 | A-5 | ControlFlow | [khác] | - | - |
| E-10 | A-4a | M-3 | ControlFlow | - | Quay lại bước 3 | (980,720); (980,400) |
| E-11 | A-4b | M-3 | ControlFlow | - | Quay lại bước 3 | (980,820); (980,400) |
| E-12 | A-5 | A-6 | ControlFlow | - | - | - |
| E-13 | A-6 | A-7 | ControlFlow | - | - | - |
| E-14 | A-7 | D-7 | ControlFlow | - | - | - |
| E-15 | D-7 | M-8 | ControlFlow | [khác] | - | - |
| E-16 | D-7 | M-14 | ControlFlow | [chuyến không có vé nào đang có hiệu lực] | Luồng 7a: Tiếp tục bước 14 | (320,1120); (320,2340) |
| E-17 | M-8 | A-8 | ControlFlow | - | - | - |
| E-18 | A-8 | A-9 | ControlFlow | - | - | (1250,1310) |
| E-19 | A-9 | D-9 | ControlFlow | - | - | (530,1410) |
| E-20 | D-9 | A-9a | ControlFlow | [Cổng SMS báo lỗi hoặc không trả kết quả] | Luồng 9a | - |
| E-21 | D-9 | M-10 | ControlFlow | [khác] | - | - |
| E-22 | A-9a | M-10 | ControlFlow | - | Tiếp tục bước 10 | (830,1600) |
| E-23 | M-10 | D-10 | ControlFlow | - | - | - |
| E-24 | D-10 | M-8 | ControlFlow | [còn số điện thoại chưa gửi SMS] | Lặp lại bước 8-9 | (380,1680); (380,1220) |
| E-25 | D-10 | M-14 | ControlFlow | [hết số điện thoại, không có vé mua trực tuyến cần hoàn] | Luồng 10a: Tiếp tục bước 14 | (320,1680); (320,2340) |
| E-26 | D-10 | M-11 | ControlFlow | [hết số điện thoại, còn vé mua trực tuyến cần hoàn] | - | - |
| E-27 | M-11 | A-11 | ControlFlow | - | - | - |
| E-28 | A-11 | A-12 | ControlFlow | - | - | (1550,1870) |
| E-29 | A-12 | D-12 | ControlFlow | - | - | (530,1970) |
| E-30 | D-12 | A-12a | ControlFlow | [Cổng thanh toán báo lỗi hoặc không trả kết quả] | Luồng 12a | - |
| E-31 | D-12 | M-13 | ControlFlow | [khác] | - | - |
| E-32 | A-12a | M-13 | ControlFlow | - | Tiếp tục bước 13 | (830,2160) |
| E-33 | M-13 | D-13 | ControlFlow | - | - | - |
| E-34 | D-13 | M-11 | ControlFlow | [còn vé mua trực tuyến chưa yêu cầu hoàn] | Lặp lại bước 11-12 | (380,2240); (380,1780) |
| E-35 | D-13 | M-14 | ControlFlow | [hết vé mua trực tuyến cần hoàn] | - | - |
| E-36 | M-14 | A-14 | ControlFlow | - | - | - |
| E-37 | A-14 | FINAL-1 | ControlFlow | - | - | - |

Bảng đối chiếu

| Bước UC | Node |
|---|---|
| 1 | INIT, A-1 |
| 2 | A-2 |
| 3 | M-3, A-3 |
| 4 | A-4, D-4 |
| 4a | A-4a |
| 4b | A-4b |
| 5 | A-5 |
| 6 | A-6 |
| 7 | A-7, D-7 |
| 7a | E-16 (không có action) |
| 8 | M-8, A-8 |
| 9 | A-9, D-9 |
| 9a | A-9a |
| 10 | D-10, M-8, M-10 (decision lặp, không có action) |
| 10a | E-25 (không có action) |
| 11 | M-11, A-11 |
| 12 | A-12, D-12 |
| 12a | A-12a |
| 13 | D-13, M-11, M-13 (decision lặp, không có action) |
| 14 | M-14, A-14, FINAL-1 |
| *a | N-*a |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-46 | Chuyến ở trạng thái nào thì được huỷ: chỉ chuyến chưa bị huỷ và chưa đến giờ xuất bến, hay còn huỷ được chuyến đã đến giờ xuất bến (ví dụ xe hỏng khi đang chạy)? (Chỉ chuyến chưa huỷ và chưa đến giờ xuất bến / Cả chuyến đã đến giờ xuất bến) | Bước 4, luồng 4a, 4b; BR-09, BR-10; ASM-26; REQ-55 | Mục 6, câu 4: "Khi phải huỷ chuyến (xe hỏng, thời tiết), nhân viên điều hành huỷ chuyến" không nêu trạng thái chuyến được phép huỷ |
| Q-47 | Khi chuyến bị huỷ, các việc hệ thống tự làm theo giờ xuất bến của chuyến (huỷ vé đặt qua điện thoại chưa thanh toán, gửi danh sách hành khách về máy soát vé) có bị bỏ cho chuyến đó không? (Bỏ cho chuyến đã huỷ / Vẫn chạy bình thường) | Bước 6; UC-007, UC-025; ASM-28; REQ-31, REQ-32, REQ-69, REQ-70 | Mục 4, câu 2 và Mục 8, câu 4 nêu các mốc theo giờ xuất bến; Mục 6, câu 4 không nêu ảnh hưởng của huỷ chuyến lên các mốc đó |
| Q-48 | Khi chuyến bị huỷ, mọi vé đang có hiệu lực của chuyến, kể cả vé đặt qua điện thoại chưa thanh toán, có chuyển sang trạng thái "Đã huỷ" ngay không? (Chuyển ngay, kèm trạng thái hoàn tiền riêng / Giữ trạng thái cũ đến khi hoàn tiền xong) | Bước 7, 11; UC-018, UC-026; ASM-29; REQ-57, REQ-58, REQ-66 | Mục 6, câu 4 nêu hoàn tiền nhưng không nêu trạng thái vé; Mục 8, câu 2 nêu "vé đã huỷ" là vé không hợp lệ khi soát |
| Q-49 | Khi SMS thông báo huỷ chuyến không gửi được tới một số điện thoại, hệ thống xử lý thế nào? (Ghi nhận và báo nhân viên điều hành / Tự thử gửi lại / Chỉ ghi nhận lỗi) | Luồng 9a, bước 14; ASM-31; REQ-56 | Mục 6, câu 4: "hệ thống gửi SMS cho mọi hành khách đã có vé" không nêu trường hợp gửi không thành công |
| Q-50 | Khi Cổng thanh toán không hoàn được tiền cho một vé của chuyến bị huỷ, hệ thống xử lý thế nào? (Ghi nhận và báo nhân viên điều hành xử lý / Tự thử hoàn lại / Chuyển sang hoàn tiền mặt tại quầy) | Luồng 12a, bước 14; ASM-33; REQ-57, REQ-16 | Mục 6, câu 4: "hoàn 100% giá vé" và Mục 5, câu 3: "được hoàn qua cổng thanh toán" không nêu hoàn tiền thất bại; project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-25 | Khi huỷ chuyến, nhân viên điều hành chọn lý do huỷ chuyến là Xe hỏng hoặc Thời tiết, và hệ thống lưu lý do cùng chuyến bị huỷ. | Chờ Q-36. Nguồn nêu "Khi phải huỷ chuyến (xe hỏng, thời tiết)" (Mục 6, câu 4) nhưng không nêu việc chọn hay lưu lý do, và Q-36 hỏi lý do có chỉ hai loại không; chọn phương án lý do là dữ liệu của lần huỷ, giới hạn ở hai lý do nguồn nêu | Bước 3, 5; Dữ liệu vào 1; REQ-55 |
| ASM-26 | Chỉ chuyến chưa bị huỷ và chưa đến giờ xuất bến mới được huỷ. Khi chuyến đã chọn vi phạm cả hai điều kiện, hệ thống phản hồi trước điều kiện chuyến đã bị huỷ (4a), rồi mới đến điều kiện đã đến giờ xuất bến (4b). | Chờ Q-46. Nguồn không nêu trạng thái chuyến được phép huỷ; huỷ lại chuyến đã huỷ làm hoàn tiền hai lần, còn hoàn 100% cho chuyến đã đến giờ xuất bến không có căn cứ trong nguồn. Thứ tự phản hồi là lựa chọn mặc định theo thứ tự nêu trong giả định này | Bước 4; luồng 4a, 4b; BR-09, BR-10 |
| ASM-27 | Nhân viên điều hành có thể bỏ yêu cầu huỷ chuyến ở bất kỳ bước nào trước khi chuyến được lưu ở trạng thái "Đã huỷ" (bước 5); khi bỏ, không có dữ liệu nào thay đổi. | Chọn lối thoát mặc định của tác nhân. Nguồn không nêu việc bỏ yêu cầu; trước bước 5 hệ thống chưa lưu gì nên không cần Q | Luồng *a |
| ASM-28 | Khi chuyến bị huỷ, mốc 60 phút trước giờ xuất bến của UC-007 và mốc 15 phút trước giờ xuất bến của UC-025 cho chuyến đó bị huỷ, nên hệ thống không tự huỷ vé đặt qua điện thoại và không gửi danh sách hành khách cho chuyến đã huỷ. | Chờ Q-47. Nguồn nêu các mốc theo giờ xuất bến (Mục 4, câu 2; Mục 8, câu 4) nhưng không nêu ảnh hưởng của huỷ chuyến; chuyến đã huỷ không còn chuyến chạy để tính mốc | Bước 6; UC-007, UC-025; REQ-31, REQ-32, REQ-69, REQ-70 |
| ASM-29 | Khi chuyến bị huỷ, mọi vé đang có hiệu lực của chuyến chuyển ngay sang trạng thái "Đã huỷ", không chờ hoàn tiền xong. Vé đã thanh toán có thêm trạng thái hoàn tiền: "Chưa hoàn" khi vừa huỷ, "Đã hoàn" khi tiền đã được hoàn. Vé đặt qua điện thoại chưa thanh toán chuyển "Đã huỷ" và không có hoàn tiền vì chưa thu tiền. | Chờ Q-48. Nguồn nêu "vé đã huỷ" là trường hợp vé không hợp lệ khi soát (Mục 8, câu 2) nhưng không nêu vé của chuyến bị huỷ đổi trạng thái thế nào; cần trạng thái hoàn tiền để UC-018 biết vé nào còn phải hoàn và để không hoàn hai lần | Bước 7, 11; luồng 7a, 12a; UC-018, UC-026; REQ-57, REQ-58, REQ-66 |
| ASM-30 | Hành khách đã có vé của chuyến bị huỷ là người đi của mọi vé đang có hiệu lực của chuyến, kể cả vé đặt qua điện thoại chưa thanh toán. Hệ thống gửi một SMS cho mỗi số điện thoại người đi, nêu tuyến, giờ xuất bến của chuyến bị huỷ và mã các vé của số điện thoại đó. | Chờ Q-25. Nguồn nêu "gửi SMS cho mọi hành khách đã có vé" (Mục 6, câu 4) và gọi vé đặt qua điện thoại là "vé" (Mục 4, câu 2); nguồn không nêu nội dung SMS, chọn nội dung tối thiểu để người nhận biết chuyến và vé bị ảnh hưởng | Bước 8, 9, 10; Dữ liệu ra 2; BR-11; REQ-56, REQ-09, REQ-19 |
| ASM-31 | Khi SMS gửi tới một số điện thoại không thành công, hệ thống ghi nhận số điện thoại đó chưa được báo kèm mã các vé, tiếp tục gửi cho các số còn lại và nêu số điện thoại chưa báo được trong kết quả ở bước 14; việc huỷ chuyến không bị dừng. | Chờ Q-49. Nguồn không nêu trường hợp gửi SMS không thành công; chuyến đã được lưu huỷ ở bước 5 nên không đảo ngược | Luồng 9a; bước 14; Dữ liệu ra 4; REQ-56 |
| ASM-32 | API hoàn tiền của Cổng thanh toán hỗ trợ hoàn một phần số tiền của giao dịch, nên hệ thống yêu cầu hoàn từng vé mua trực tuyến theo đúng giá vé của vé đó. | Chờ Q-20. Một giao dịch có thể thu tiền nhiều vé, trong đó có vé đã được trả trước khi chuyến bị huỷ; hoàn từng vé cần hoàn một phần. Hồ sơ dự án ghi "chưa có tài liệu API" | Bước 11, 12, 13; Dữ liệu ra 3; BR-07; REQ-16 |
| ASM-33 | Khi Cổng thanh toán báo hoàn tiền không thành công hoặc không trả kết quả cho một vé, hệ thống giữ trạng thái hoàn tiền "Chưa hoàn" của vé, ghi nhận vé đó, tiếp tục hoàn các vé còn lại và nêu vé chưa hoàn được trong kết quả ở bước 14; việc huỷ chuyến không bị đảo ngược. | Chờ Q-50. Nguồn không nêu hoàn tiền thất bại; chuyến đã được lưu huỷ ở bước 5 và SMS đã gửi nên không đảo ngược | Luồng 12a; bước 14; Dữ liệu ra 4; REQ-57, REQ-16 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-017 (bảng 4b cột REQ; Mục 5) | UC-017 dùng REQ-09, REQ-15, REQ-19, REQ-23, REQ-25, REQ-28, REQ-30, REQ-31, REQ-32, REQ-46, REQ-47, REQ-60, REQ-61, REQ-66, REQ-69, REQ-70 nhưng cột REQ của UC-017 không có các REQ này | Thêm các REQ này vào cột REQ của UC-017 ở bảng 4b và thêm UC-017 vào các dòng REQ tương ứng ở Mục 5 |

## Vấn đề còn mở

- F10.3 yêu cầu mọi node đạt được từ INIT, nhưng F10.2 yêu cầu luồng *a chỉ thể hiện bằng note N-*a. Theo C9 chọn quy tắc riêng của bước (F10.2), nên N-*a không đạt được từ INIT bằng cạnh. F10.2 yêu cầu mỗi hàng hành động luồng thay thế có một action nhưng với luồng *a lại chỉ dùng note; chọn F10.2, hàng *a không có action riêng.
- F10.6 đặt trục dọc của các cạnh ra từ decision cách decision 30 về bên phải, nhưng action của luồng chính rộng 180 nằm ngay dưới decision nên trục đó cắt qua action. Dùng trục x=700 (cách mép phải action luồng chính 80) cho D-4 và x=980 cho các cạnh quay lại bước 3.
- F5.4 cho phép "Tiếp tục bước K" nhưng luồng 9a, 12a tiếp tục tại bước 10, 13 là bước "Lặp lại" không có action; ánh xạ sang decision D-10, D-13 qua merge node M-10, M-13 (decision chỉ có một luồng vào, F10.3). Luồng 7a và 10a nhập lại ở bước 14 qua merge node M-14.
- F4.2 mục 17 viết "Hẹn / hẹn lại / huỷ mốc <tên mốc> của UC-xxx" cho một mốc; bước 6 huỷ hai mốc của hai use case (UC-007, UC-025) trong một bước vì cùng gắn với giờ xuất bến của một chuyến.
- F10.4 nêu thứ tự partition theo nhóm (tác nhân chính, hệ thống, các tác nhân phụ) nhưng không nêu thứ tự giữa hai tác nhân phụ. Đặt Cổng SMS trước Cổng thanh toán theo thứ tự xuất hiện trong luồng chính để cạnh giữa hệ thống và hai cổng không cắt qua partition khác.
- Số bước luồng chính là 14, sát cận trên 15 của F4.4 vì mỗi bước "Lặp lại" tính một bước; hai bước "Lặp lại" không có action trong sơ đồ.
- Các mục Target còn lại đạt.
