# P04 - Đặc tả use case UC-009 Đặt vé trực tuyến - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-khach.md; P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09); P01-actors.md (phiên bản 1.0, Q-39, ASM-11); P02-usecases.md (phiên bản 1.1, Q-42, ASM-16); P02R-review.md (phiên bản 1.0, Q-42, ASM-16); P03-usecase-model.md (phiên bản 1.0, Q-43, ASM-17; Mục 1 và Mục 2). Chưa có sổ BR và chưa có đặc tả P04 nào; sổ BR bắt đầu từ BR-01. Placeholder UC_ID = UC-009; TEN_HE_THONG_TRONG_LUONG, YEU_CAU_BO_SUNG: Không có (chủ ngữ hệ thống là "Hệ thống"). Mã Q, ASM cấp tiếp từ Q-43, ASM-17 |
| Phạm vi | UC-009 |
| Mã Q, ASM cuối đã cấp | Q-45, ASM-24 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-009 |
| Tên use case | Đặt vé trực tuyến (Book Ticket Online) |
| Tác nhân chính | ACT-01 Hành khách |
| Tác nhân phụ | ACT-07 Cổng SMS |
| Mô tả ngắn | Use case này mô tả tương tác giữa hành khách và hệ thống khi hành khách muốn mua vé xe trực tuyến cho một chuyến mà không cần tài khoản. Kết quả là mỗi chỗ đã chọn có một vé đã phát hành với mã vé riêng, và mã vé được gửi qua SMS tới số điện thoại người đi. |
| Sự kiện kích hoạt | Hành khách muốn mua vé xe trực tuyến (EV-02); đến 10 phút giữ chỗ (EV-03) |
| Tiền điều kiện | Không có |
| Hậu điều kiện (thành công) | Mỗi chỗ đã chọn có một vé đã phát hành với mã vé riêng, gắn với chuyến, chỗ, họ tên và số điện thoại người đi.<br>Các chỗ đó không còn trống cho người khác.<br>Khoản tiền vé đã được cổng thanh toán xác nhận (kết quả của UC-010).<br>Yêu cầu gửi SMS mã vé tới số điện thoại người đi đã được chuyển cho Cổng SMS; khi kết thúc ở luồng 11a, việc mã vé chưa gửi được qua SMS được ghi nhận. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công, không có vé nào được phát hành và các chỗ đã chọn không còn bị giữ cho yêu cầu này. |
| Quan hệ | «include» UC-008 Tra cứu chuyến xe (tại bước 2)<br>«include» UC-010 Thanh toán vé trực tuyến (tại bước 8) |
| Điểm mở rộng | Không có |
| REQ | REQ-04, REQ-07, REQ-08, REQ-09, REQ-13, REQ-14, REQ-17, REQ-18, REQ-19, REQ-20, REQ-21, REQ-75 (theo P02); REQ-05, REQ-06 (bước 2), REQ-15 (bước 8), REQ-60, REQ-61 (giá vé ở bước 8 và bước 12) thêm theo [Action] 1c, xem Đề xuất sửa artifact trước |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Hành khách | Yêu cầu mua vé xe trực tuyến. |
| 2 | Hệ thống | Gọi use case UC-008 Tra cứu chuyến xe để hành khách tìm chuyến theo điểm đi, điểm đến, ngày đi và xem sơ đồ chỗ của chuyến. |
| 3 | Hành khách | Chọn các chỗ còn trống trên chuyến để mua vé (xem Dữ liệu vào 1). |
| 4 | Hệ thống | Kiểm tra các chỗ đã chọn còn trống (BR-02), số chỗ đã chọn không vượt giới hạn (BR-01) và chuyến chưa đến giờ xuất bến (BR-05). |
| 5 | Hệ thống | Giữ tạm các chỗ đã chọn cho hành khách trong thời hạn (BR-03, ASM-18). |
| 6 | Hành khách | Nhập và gửi họ tên và số điện thoại của người đi cho cả lần đặt (xem Dữ liệu vào 2, ASM-19). |
| 7 | Hệ thống | Kiểm tra họ tên và số điện thoại của người đi đã được cung cấp. |
| 8 | Hệ thống | Gọi use case UC-010 Thanh toán vé trực tuyến để hành khách thanh toán tiền vé của các chỗ đang giữ. |
| 9 | Hệ thống | Phát hành vé cho các chỗ đang giữ, mỗi chỗ một mã vé (BR-04). |
| 10 | Hệ thống | Gửi mã vé của các vé đã phát hành tới số điện thoại người đi qua Cổng SMS (xem Dữ liệu ra 2). |
| 11 | Cổng SMS | Trả kết quả gửi SMS. |
| 12 | Hệ thống | Hiển thị các vé đã phát hành và mã vé cho hành khách (xem Dữ liệu ra 1, ASM-20). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 2a | UC-008 kết thúc mà hành khách chưa chọn chuyến nào | Hệ thống | Thông báo chưa chọn được chuyến để mua vé. | Kết thúc use case (thất bại) |
| 4a | Có chỗ đã chọn không còn trống (BR-02) | Hệ thống | Từ chối yêu cầu chọn chỗ và thông báo chỗ không còn trống (BR-02). | Quay lại bước 2 |
| 4b | Các chỗ đã chọn còn trống và số chỗ đã chọn lớn hơn 5 (BR-01) | Hệ thống | Từ chối yêu cầu chọn chỗ và thông báo giới hạn tối đa 5 chỗ mỗi lần đặt (BR-01). | Quay lại bước 3 |
| 4c | Các chỗ đã chọn còn trống, số chỗ đã chọn không quá 5 và chuyến đã đến giờ xuất bến (BR-05, ASM-21) | Hệ thống | Từ chối yêu cầu chọn chỗ và thông báo chuyến đã đến giờ xuất bến (BR-05). | Kết thúc use case (thất bại) |
| 5a | Hết thời hạn giữ chỗ (BR-03) tại bất kỳ bước nào từ bước 6 đến bước 8 mà thanh toán chưa thành công | Hệ thống | Trả lại các chỗ đang giữ cho người khác và thông báo hết thời hạn giữ chỗ cho hành khách. | Kết thúc use case (thất bại) |
| 7a | Hành khách chưa cung cấp họ tên hoặc số điện thoại của người đi | Hệ thống | Từ chối thông tin và thông báo thông tin còn thiếu. | Quay lại bước 6 |
| 8a | UC-010 trả kết quả thất bại cho UC-009 | Hệ thống | Trả lại ngay các chỗ đang giữ cho người khác và thông báo thanh toán không thành công (ASM-24). | Kết thúc use case (thất bại) |
| 11a | SMS mã vé không gửi được (Cổng SMS báo lỗi hoặc không trả kết quả) | Hệ thống | Ghi nhận mã vé chưa gửi được qua SMS; mã vé vẫn được hiển thị cho hành khách ở bước 12 (ASM-20). | Tiếp tục bước 12 (thành công một phần) |
| *a | Tại bất kỳ bước nào trước bước 8, hành khách huỷ yêu cầu mua vé | Hệ thống | Huỷ yêu cầu mua vé, trả lại ngay các chỗ đang giữ và thông báo đã huỷ (ASM-24). | Kết thúc use case (thất bại) |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

Dữ liệu vào 1 (bước 3)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Chỗ đã chọn | Danh sách mã chỗ trên sơ đồ chỗ của chuyến mà hành khách muốn mua vé | Có | Từ 1 đến 5 chỗ (BR-01), mỗi chỗ gắn một vé (BR-04); mỗi chỗ còn trống, chưa có vé và chưa bị giữ cho yêu cầu khác (BR-02) | A05, A06 |

Dữ liệu vào 2 (bước 6)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Họ tên người đi | Họ tên của người đi, một người chung cho cả lần đặt (ASM-19) | Có | Chưa quy định (Q-44) | Nguyễn Văn An |
| 2 | Số điện thoại người đi | Số điện thoại nhận mã vé qua SMS (REQ-20) | Có | Chưa quy định (Q-44) | 0912345678 |

Dữ liệu ra 1 (bước 12)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Mã vé | Mã của từng vé đã phát hành, mỗi chỗ một mã (BR-04) | Chuỗi ký tự, mỗi vé một dòng | SV0001<br>SV0002 |
| 2 | Chuyến | Tuyến, điểm đi, điểm đến và giờ xuất bến của chuyến | Ngày giờ dạng dd/MM/yyyy HH:mm | Hà Nội - Vinh, 15/06/2026 20:30 |
| 3 | Chỗ | Mã chỗ của từng vé | Chuỗi ký tự, cùng thứ tự với mã vé | A05<br>A06 |
| 4 | Họ tên người đi | Họ tên đã nhập ở bước 6 | Chuỗi ký tự | Nguyễn Văn An |
| 5 | Giá vé | Giá của từng vé (REQ-60, REQ-61) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 250.000 đ<br>250.000 đ |
| 6 | Tổng tiền | Tổng giá vé của các vé trong lần đặt | Như Giá vé | 500.000 đ |

Dữ liệu ra 2 (bước 10)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Số điện thoại nhận | Số điện thoại người đi đã nhập ở bước 6 | Chuỗi chữ số (định dạng theo Q-44) | 0912345678 |
| 2 | Mã vé | Mã của các vé đã phát hành, mỗi chỗ một mã (BR-04) | Danh sách mã vé ngăn bằng dấu phẩy | SV0001, SV0002 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-01 | Mỗi lần đặt vé, hành khách chọn tối đa 5 chỗ. | Ràng buộc | 4, 4b, Dữ liệu vào 1 | REQ-08 | Mới |
| BR-02 | Không được có hai vé cùng một chỗ trên một chuyến. | Ràng buộc | 4, 4a, 5, Dữ liệu vào 1 | REQ-75 | Mới |
| BR-03 | Các chỗ hành khách đã chọn được giữ trong 10 phút để thanh toán, tính từ lúc hệ thống giữ các chỗ đó (ASM-18); hết 10 phút mà chưa thanh toán thành công thì chỗ được trả lại cho người khác. | Ràng buộc | 5, 5a | REQ-13, REQ-14, REQ-17 | Mới |
| BR-04 | Mỗi chỗ có một mã vé. | Ràng buộc | 9, 10, 12, Dữ liệu ra 1, Dữ liệu ra 2 | REQ-19 | Mới |
| BR-05 | Vé của một chuyến chỉ bán trực tuyến cho đến giờ xuất bến; từ giờ xuất bến trở đi không giữ chỗ để bán (ASM-21). | Ràng buộc | 4, 4c | REQ-04 | Mới |
| BR-06 | Giao dịch thanh toán thành công đến sau khi hết thời hạn giữ chỗ và chỗ đã trả lại cho người khác thì không phát hành vé và khoản tiền được hoàn cho hành khách (ASM-22). | Kích hoạt hành động | 5a (phần xử lý giao dịch đến sau thuộc UC-010, xem mục 8) | REQ-15, REQ-17 | Mới |

## 7. Yêu cầu đặc biệt

| STT | Yêu cầu | Nhóm (FURPS+) | REQ |
|---|---|---|---|
| 1 | Hành khách thực hiện use case này không cần có tài khoản. | Security | REQ-04 |
| 2 | Khi nhiều hành khách cùng chọn một chỗ trên một chuyến tại cùng thời điểm, chỉ một yêu cầu giữ được chỗ đó; không bao giờ có hai vé cùng một chỗ trên một chuyến. | Reliability | REQ-75 |

## 8. Thông tin bổ sung

- Thời hạn giữ chỗ: chỗ được giữ lúc 20:00 thì hết thời hạn lúc 20:10 (20:00 + 10 phút, BR-03). Thời hạn này chạy qua các bước 6, 7 và cả bước 8 (thời gian hành khách ở trong UC-010).
- Tổng tiền: ví dụ 2 chỗ, mỗi chỗ 250.000 đ, tổng tiền là 2 x 250.000 = 500.000 đ. Giá vé do UC-023 Đặt giá vé và UC-024 Đặt mức tăng giá ngày lễ cung cấp (REQ-60, REQ-61); ngày áp dụng mức tăng giá chờ Q-24.
- Kết cục của UC-010 cần khớp khi đặc tả UC-010: kết quả thành công --> tiếp tục bước 9; kết quả thất bại (hành khách không thanh toán tiếp) --> luồng 8a. Theo ASM-12, thanh toán lại nhiều lần xảy ra bên trong UC-010 cho đến hết thời hạn giữ chỗ, không quay về UC-009.
- Kết cục của UC-008 cần khớp khi đặc tả UC-008: đã chọn chuyến --> tiếp tục bước 3; chưa chọn chuyến --> luồng 2a.
- Giao dịch thanh toán thành công đến sau khi hết thời hạn giữ chỗ (Q-19, ASM-22, BR-06) xảy ra sau khi UC-009 đã kết thúc ở luồng 5a; việc không phát hành vé và hoàn tiền cho giao dịch đó do UC-010 và P06 đặc tả.
- UC-009 tạo vé, là dữ liệu mốc cho UC-025 (gửi danh sách hành khách 15 phút trước giờ xuất bến) nhưng không tạo, đổi hay huỷ mốc thời gian nào, nên không có bước hẹn mốc (F4.2 mục 17). Vé phát hành sau thời điểm gửi danh sách chờ Q-29 ở UC-025.
- Vé đã phát hành là dữ liệu dùng chung với UC-011 (lịch sử vé, Q-26), UC-012 (trả vé), UC-014 (đổi vé), UC-026 (soát vé).

## 8a. Kịch bản chính

- KB1: Luồng chính --> mua vé thành công, mã vé gửi qua SMS và hiển thị cho hành khách.
- KB2: Luồng chính + 11a --> mua vé thành công một phần, SMS không gửi được, mã vé vẫn hiển thị.
- KB3: Luồng chính đến bước 4 + 4a, quay lại bước 2, rồi luồng chính --> chọn lại chỗ và mua vé thành công.
- KB4: Luồng chính đến bước 7 + 5a --> hết thời hạn giữ chỗ, không có vé.
- KB5: Luồng chính đến bước 8 + 8a --> thanh toán không thành công, không có vé.

## 9. Activity diagram

File: diagrams/P04-activity-UC-009.drawio (một trang, tên trang "UC-009"). Bảng Node và bảng Edge dưới đây là nguồn chuẩn. Toạ độ x của node trong bảng Node tính trong partition chứa nó; toạ độ trong cột Điểm uốn là toạ độ tuyệt đối. Cổng ra, cổng vào của mỗi cạnh (exitX, exitY, entryX, entryY) suy ra từ hướng của điểm uốn đầu và điểm uốn cuối (hoặc từ node đối diện khi không có điểm uốn). Luồng chờ thời hạn giữ chỗ (5a) thể hiện bằng note N-5a theo F10.2 vì bước bắt đầu chờ (5) và bước sự kiện tới (8) cách nhau bởi các bước khác.

Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Hành khách | - | - | - | Cao 2240 | 0 | 0 | 300 | 2240 |
| P-SYS | Partition | Hệ thống | - | - | - | Cao 2240 | 300 | 0 | 960 | 2240 |
| P-ACT-07 | Partition | Cổng SMS | - | - | - | Cao 2240 | 1260 | 0 | 300 | 2240 |
| INIT | Initial | - | - | P-ACT-01 | 1 | Nút khởi đầu | 130 | 60 | 40 | 40 |
| A-1 | Action | Yêu cầu mua vé xe trực tuyến | - | P-ACT-01 | 1 | - | 60 | 140 | 180 | 60 |
| M-2 | Merge | - | - | P-SYS | 2 | Nhận luồng từ A-1 và từ A-4a (quay lại bước 2) | 130 | 230 | 40 | 40 |
| A-2 | CallBehaviorAction | UC-008 Tra cứu chuyến xe | - | P-SYS | 2 | Include UC-008 | 60 | 310 | 180 | 60 |
| D-2 | Decision | - | - | P-SYS | 2 | Kết cục của UC-008 | 130 | 410 | 40 | 40 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | 2a | Kết thúc thất bại sau 2a | 390 | 320 | 40 | 40 |
| A-2a | Action | Thông báo chưa chọn được chuyến | - | P-SYS | 2a | - | 320 | 400 | 180 | 60 |
| M-3 | Merge | - | - | P-ACT-01 | 3 | Nhận luồng từ D-2 và từ A-4b (quay lại bước 3) | 130 | 490 | 40 | 40 |
| A-3 | Action | Chọn các chỗ còn trống | - | P-ACT-01 | 3 | - | 60 | 570 | 180 | 60 |
| A-4 | Action | Kiểm tra chuyến, số chỗ, chỗ trống | - | P-SYS | 4 | - | 60 | 670 | 180 | 60 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | 4c | Kết thúc thất bại sau 4c | 390 | 680 | 40 | 40 |
| D-4 | Decision | - | - | P-SYS | 4 | Ưu tiên 4a, 4b, 4c theo ASM-23 | 130 | 770 | 40 | 40 |
| A-4c | Action | Từ chối, báo chuyến đã đến giờ xuất bến | - | P-SYS | 4c | - | 320 | 760 | 180 | 60 |
| A-4b | Action | Từ chối, báo tối đa 5 chỗ | - | P-SYS | 4b | - | 320 | 860 | 180 | 60 |
| A-4a | Action | Từ chối, báo chỗ không còn trống | - | P-SYS | 4a | - | 320 | 960 | 180 | 60 |
| A-5 | Action | Giữ tạm các chỗ đã chọn | - | P-SYS | 5 | Bước bắt đầu chờ (BR-03) | 60 | 850 | 180 | 60 |
| M-6 | Merge | - | - | P-ACT-01 | 6 | Nhận luồng từ A-5 và từ A-7a (quay lại bước 6) | 130 | 1030 | 40 | 40 |
| A-6 | Action | Nhập và gửi họ tên, số điện thoại | - | P-ACT-01 | 6 | - | 60 | 1110 | 180 | 60 |
| A-7 | Action | Kiểm tra thông tin người đi | - | P-SYS | 7 | - | 60 | 1210 | 180 | 60 |
| D-7 | Decision | - | - | P-SYS | 7 | - | 130 | 1310 | 40 | 40 |
| A-7a | Action | Từ chối, báo thông tin còn thiếu | - | P-SYS | 7a | - | 320 | 1300 | 180 | 60 |
| A-8 | CallBehaviorAction | UC-010 Thanh toán vé trực tuyến | - | P-SYS | 8 | Include UC-010; bước sự kiện tới của thời hạn chờ | 60 | 1390 | 180 | 60 |
| D-8 | Decision | - | - | P-SYS | 8 | Kết cục của UC-010 | 130 | 1490 | 40 | 40 |
| A-8a | Action | Trả lại chỗ, báo thanh toán không thành công | - | P-SYS | 8a | - | 320 | 1480 | 180 | 60 |
| FINAL-5 | ActivityFinal | - | - | P-SYS | 8a | Kết thúc thất bại sau 8a | 390 | 1580 | 40 | 40 |
| A-9 | Action | Phát hành vé, mỗi chỗ một mã vé | - | P-SYS | 9 | - | 60 | 1570 | 180 | 60 |
| A-10 | Action | Gửi mã vé qua Cổng SMS | - | P-SYS | 10 | - | 60 | 1670 | 180 | 60 |
| A-11 | Action | Trả kết quả gửi SMS | - | P-ACT-07 | 11 | - | 60 | 1770 | 180 | 60 |
| D-11 | Decision | - | - | P-SYS | 11 | Hệ thống đánh giá kết quả do Cổng SMS trả về | 130 | 1870 | 40 | 40 |
| A-11a | Action | Ghi nhận mã vé chưa gửi được qua SMS | - | P-SYS | 11a | - | 320 | 1860 | 180 | 60 |
| M-12 | Merge | - | - | P-SYS | 12 | Nhận luồng từ D-11 và từ A-11a (tiếp tục bước 12) | 130 | 1970 | 40 | 40 |
| A-12 | Action | Hiển thị các vé và mã vé | - | P-SYS | 12 | - | 60 | 2050 | 180 | 60 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | 12 | Kết thúc thành công | 130 | 2150 | 40 | 40 |
| N-5a | Note | 5a: Hết thời hạn giữ chỗ (BR-03) tại bất kỳ bước nào từ bước 6 đến bước 8 mà thanh toán chưa thành công | - | P-SYS | 5a | Nhánh 5a bắt đầu từ note, không có cạnh vào từ luồng chính | 680 | 300 | 240 | 120 |
| A-5a | Action | Trả lại chỗ đang giữ, báo hết thời hạn | - | P-SYS | 5a | - | 710 | 480 | 180 | 60 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | 5a | Kết thúc thất bại sau 5a | 780 | 580 | 40 | 40 |
| N-*a | Note | *a: Tại bất kỳ bước nào trước bước 8, hành khách huỷ yêu cầu mua vé. Hệ thống huỷ yêu cầu, trả lại ngay các chỗ đang giữ và thông báo đã huỷ. Kết thúc use case (thất bại). | - | P-ACT-01 | *a | Thể hiện bằng note theo F10.2, không vẽ cạnh | 30 | 1250 | 240 | 140 |

Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | M-2 | ControlFlow | - | - | (450,170) |
| E-03 | M-2 | A-2 | ControlFlow | - | - | - |
| E-04 | A-2 | D-2 | ControlFlow | - | - | - |
| E-05 | D-2 | A-2a | ControlFlow | [chưa chọn chuyến] | Luồng 2a | - |
| E-06 | A-2a | FINAL-1 | ControlFlow | - | Luồng 2a | - |
| E-07 | D-2 | M-3 | ControlFlow | [đã chọn chuyến] | - | (150,430) |
| E-08 | M-3 | A-3 | ControlFlow | - | - | - |
| E-09 | A-3 | A-4 | ControlFlow | - | - | (450,600) |
| E-10 | A-4 | D-4 | ControlFlow | - | - | - |
| E-11 | D-4 | A-4c | ControlFlow | [chỗ còn trống, không quá 5 chỗ, chuyến đã xuất bến] | Luồng 4c | - |
| E-12 | D-4 | A-4b | ControlFlow | [chỗ còn trống, quá 5 chỗ] | Luồng 4b | (580,790); (580,890) |
| E-13 | D-4 | A-4a | ControlFlow | [có chỗ không còn trống] | Luồng 4a | (580,790); (580,990) |
| E-14 | D-4 | A-5 | ControlFlow | [khác] | - | - |
| E-15 | A-4c | FINAL-3 | ControlFlow | - | Luồng 4c | - |
| E-16 | A-4b | M-3 | ControlFlow | - | Quay lại bước 3 | (860,890); (860,510) |
| E-17 | A-4a | M-2 | ControlFlow | - | Quay lại bước 2 | (900,990); (900,250) |
| E-18 | A-5 | M-6 | ControlFlow | - | - | (150,880) |
| E-19 | M-6 | A-6 | ControlFlow | - | - | - |
| E-20 | A-6 | A-7 | ControlFlow | - | - | (450,1140) |
| E-21 | A-7 | D-7 | ControlFlow | - | - | - |
| E-22 | D-7 | A-7a | ControlFlow | [thiếu họ tên hoặc số điện thoại] | Luồng 7a | - |
| E-23 | D-7 | A-8 | ControlFlow | [đủ họ tên và số điện thoại] | - | - |
| E-24 | A-7a | M-6 | ControlFlow | - | Quay lại bước 6 | (860,1330); (860,1050) |
| E-25 | A-8 | D-8 | ControlFlow | - | - | - |
| E-26 | D-8 | A-8a | ControlFlow | [UC-010 thất bại] | Luồng 8a | - |
| E-27 | D-8 | A-9 | ControlFlow | [thanh toán thành công] | - | - |
| E-28 | A-8a | FINAL-5 | ControlFlow | - | Luồng 8a | - |
| E-29 | A-9 | A-10 | ControlFlow | - | - | - |
| E-30 | A-10 | A-11 | ControlFlow | - | - | (1410,1700) |
| E-31 | A-11 | D-11 | ControlFlow | - | - | (450,1800) |
| E-32 | D-11 | A-11a | ControlFlow | [SMS không gửi được] | Luồng 11a | - |
| E-33 | D-11 | M-12 | ControlFlow | [SMS gửi được] | - | - |
| E-34 | A-11a | M-12 | ControlFlow | - | Tiếp tục bước 12 | (710,1990) |
| E-35 | M-12 | A-12 | ControlFlow | - | - | - |
| E-36 | A-12 | FINAL-2 | ControlFlow | - | - | - |
| E-37 | N-5a | A-5a | ControlFlow | - | Nhánh 5a bắt đầu từ note | - |
| E-38 | A-5a | FINAL-4 | ControlFlow | - | Luồng 5a | - |

Bảng đối chiếu

| Bước UC | Node |
|---|---|
| 1 | A-1 (INIT là nút khởi đầu) |
| 2 | M-2, A-2, D-2 |
| 2a | A-2a, FINAL-1 |
| 3 | M-3, A-3 |
| 4 | A-4, D-4 |
| 4a | A-4a (quay lại M-2) |
| 4b | A-4b (quay lại M-3) |
| 4c | A-4c, FINAL-3 |
| 5 | A-5 |
| 5a | N-5a, A-5a, FINAL-4 |
| 6 | M-6, A-6 |
| 7 | A-7, D-7 |
| 7a | A-7a (quay lại M-6) |
| 8 | A-8, D-8 |
| 8a | A-8a, FINAL-5 |
| 9 | A-9 |
| 10 | A-10 |
| 11 | A-11, D-11 |
| 11a | A-11a (tiếp tục M-12) |
| 12 | M-12, A-12, FINAL-2 |
| *a | N-*a |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-44 | Họ tên và số điện thoại của người đi phải thoả điều kiện hợp lệ nào (độ dài họ tên, định dạng số điện thoại trong nước hay quốc tế, có xác minh số điện thoại không)? (Chỉ cần đã nhập / Số điện thoại di động đúng định dạng trong nước / Xác minh số điện thoại bằng mã gửi qua SMS) | Dữ liệu vào 2, Dữ liệu ra 2, luồng 7a; REQ-09, REQ-20 | Mục 2, câu 1: "hành khách nhập họ tên và số điện thoại của người đi" không nêu điều kiện hợp lệ |
| Q-45 | Khi hành khách từ bỏ trước khi thanh toán thành công (huỷ yêu cầu, hoặc UC-010 trả kết quả thất bại), các chỗ đang giữ được trả lại ngay hay vẫn giữ đến hết 10 phút? (Trả lại ngay / Giữ đến hết 10 phút) | Luồng *a, 8a; BR-03, ASM-24; REQ-13, REQ-14, REQ-17 | Mục 3, câu 2: "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại cho người khác" chỉ nêu trả chỗ khi hết 10 phút |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-18 | Thời gian giữ chỗ 10 phút tính từ lúc hệ thống giữ các chỗ hành khách vừa chọn (bước 5), không tính từ lúc hành khách bắt đầu thanh toán. | Chờ Q-18. Nguồn nêu "Các chỗ đã chọn được giữ trong 10 phút để hành khách thanh toán" (Mục 3, câu 1) nhưng không nêu mốc bắt đầu; chọn mốc lúc chọn chỗ để chỗ không bị người khác lấy trong khi hành khách nhập thông tin người đi | Bước 5, 5a; BR-03; REQ-13, REQ-14 |
| ASM-19 | Một lần đặt có một người đi chung: hành khách nhập một họ tên và một số điện thoại cho tất cả các chỗ trong lần đặt, và mã vé của mọi chỗ được gửi tới số điện thoại đó. | Chờ Q-11. Nguồn nêu "hành khách nhập họ tên và số điện thoại của người đi" (Mục 2, câu 1) và "chọn tối đa 5 chỗ trong một lần đặt" (Mục 1, câu 2) nhưng không nêu một hay nhiều người đi | Bước 6, 10; Dữ liệu vào 2; REQ-09, REQ-20 |
| ASM-20 | Khi SMS mã vé không gửi được, vé đã phát hành vẫn giữ nguyên; hệ thống hiển thị mã vé cho hành khách ngay sau khi phát hành (bước 12) và ghi nhận SMS chưa gửi được. | Chờ Q-35. Nguồn nêu "gửi qua SMS tới số điện thoại người đi" (Mục 3, câu 3) nhưng không nêu khi gửi SMS thất bại; chọn phương án hiển thị mã vé để hành khách luôn nhận được mã vé | Bước 12, 11a; REQ-20 |
| ASM-21 | Vé trực tuyến được bán cho đến giờ xuất bến của chuyến; từ giờ xuất bến trở đi hệ thống không giữ chỗ để bán. | Chờ Q-13. Nguồn không nêu thời điểm ngừng bán vé trước giờ xuất bến; chọn phương án ngừng bán tại giờ xuất bến, là thời điểm muộn nhất còn có nghĩa | Bước 4, 4c; BR-05; REQ-04 |
| ASM-22 | Giao dịch thanh toán thành công đến sau khi hết thời hạn giữ chỗ và chỗ đã trả lại cho người khác thì không phát hành vé; khoản tiền được hoàn cho hành khách. | Chờ Q-19. Nguồn nêu chỗ được trả lại khi "Hết 10 phút chưa thanh toán thành công" (Mục 3, câu 2) nhưng không nêu giao dịch thành công đến muộn; chọn phương án hoàn tiền vì chỗ có thể đã thuộc người khác | Luồng 5a; BR-06; REQ-15, REQ-17 |
| ASM-23 | Khi một yêu cầu chọn chỗ vi phạm nhiều điều kiện cùng lúc ở bước 4, hệ thống phản hồi điều kiện đầu tiên theo thứ tự: chỗ không còn trống (4a), số chỗ vượt giới hạn (4b), chuyến đã đến giờ xuất bến (4c). | Chọn thứ tự phản hồi mặc định, không cần Q. Nguồn không nêu thứ tự ưu tiên; hai điều kiện đầu theo thứ tự xuất hiện trong nguồn (Mục 1, câu 2: "các chỗ còn trống, rồi chọn tối đa 5 chỗ"), điều kiện giờ xuất bến đến từ ASM-21 nên xếp cuối | Bước 4; luồng 4a, 4b, 4c |
| ASM-24 | Hành khách có thể huỷ yêu cầu mua vé trước khi thanh toán thành công; khi huỷ, hoặc khi UC-010 trả kết quả thất bại, các chỗ đang giữ được trả lại ngay, không chờ hết 10 phút. | Chờ Q-45. Nguồn không nêu việc huỷ hay từ bỏ; use case kết thúc thì không còn phiên nào để chờ hết thời hạn, nên chọn phương án trả chỗ ngay | Luồng *a, 8a; BR-03 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-009 (bảng 4b cột REQ; Mục 5) | UC-009 dùng REQ-05, REQ-06 (bước 2 gọi UC-008), REQ-15 (bước 8 gọi UC-010), REQ-60, REQ-61 (giá vé ở bước 8 và bước 12) nhưng cột REQ của UC-009 không có các REQ này | Thêm REQ-05, REQ-06, REQ-15, REQ-60, REQ-61 vào cột REQ của UC-009 ở bảng 4b và thêm UC-009 vào các dòng REQ tương ứng ở Mục 5 |

## Vấn đề còn mở

- F10.3 yêu cầu mọi node đạt được từ INIT, nhưng F10.2 yêu cầu nhánh 5a bắt đầu từ note N-5a (action A-5a không có cạnh vào từ luồng chính) và luồng *a chỉ thể hiện bằng note N-*a. Theo C9 chọn quy tắc riêng của bước (F10.2), nên N-5a, A-5a, FINAL-4 và N-*a không đạt được từ INIT bằng cạnh.
- F10.2 yêu cầu mỗi hàng hành động của luồng thay thế có một action, nhưng với luồng *a lại yêu cầu chỉ dùng note. Theo C9 chọn F10.2 cho luồng *a: hàng *a không có action riêng (N-*a mô tả điều kiện và hành động).
- F10.6 đặt trục dọc của các cạnh từ decision cách decision 30 về bên phải, nhưng action của luồng chính nằm ngay dưới decision rộng 180 nên trục cách decision 30 cắt qua action đó. Dùng trục x=580 (cách mép phải của action luồng chính 40) cho decision D-4.
- Q-44: điều kiện hợp lệ của họ tên và số điện thoại ghi "Chưa quy định (Q-44)" ở chế độ CO_NHAN, vì F6.1 chỉ nói ghi như vậy ở chế độ NGHIEM_NGAT và không cho phép tự đặt điều kiện.
- Target 5a (báo kết quả cho hành khách) đạt cho mọi luồng kết thúc use case: 2a, 4c, 5a, 8a, *a có bước hệ thống thông báo; luồng chính và 11a kết thúc bằng bước 12 hiển thị vé.
