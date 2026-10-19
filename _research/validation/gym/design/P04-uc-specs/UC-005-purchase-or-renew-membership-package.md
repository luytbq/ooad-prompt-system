# P04 - Đặc tả use case UC-005 Mua hoặc gia hạn gói tập - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P04 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-phong-tap.md; P00-problem-brief.md (phiên bản 1.0; các dòng REQ của UC-005 và REQ-78, REQ-79; mục Câu hỏi mở); P01-actors.md (phiên bản 1.0; Mục 2, mục Câu hỏi mở, Giả định); P02-usecases.md (phiên bản 1.1; dòng UC-005 ở bảng 4a, 4b; dòng EV-05, EV-06, EV-07; mục Câu hỏi mở, Giả định); P02R-review.md (phiên bản 1.0; mục Câu hỏi mở, Giả định); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2, mục Câu hỏi mở, Giả định). Sổ BR, đặc tả P04 khác, P05, P06: chưa có. UC_ID: UC-005. TEN_HE_THONG_TRONG_LUONG: Phần mềm VietFit. YEU_CAU_BO_SUNG: Không có |
| Phạm vi | UC-005 |
| Mã Q, ASM cuối đã cấp | Q-57; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Mã use case | UC-005 |
| Tên use case | Mua hoặc gia hạn gói tập (Purchase Or Renew Membership Package) |
| Tác nhân chính | ACT-02 Hội viên, ACT-05 Lễ tân |
| Tác nhân phụ | ACT-08 Cổng thanh toán, ACT-11 Hệ thống hoá đơn điện tử |
| Mô tả ngắn | Use case này mô tả tương tác giữa hội viên hoặc lễ tân và Phần mềm VietFit khi hội viên muốn mua hoặc gia hạn gói tập, hoặc khách đến quầy muốn mua gói tập. Kết quả là gói tập đã thanh toán và được kích hoạt. |
| Sự kiện kích hoạt | Hội viên muốn mua hoặc gia hạn gói tập (EV-05); khách đến quầy muốn mua gói tập (EV-06) |
| Tiền điều kiện | Hội viên, khi tự mua hoặc gia hạn trên ứng dụng, đã được xác thực và đang có phiên làm việc. |
| Hậu điều kiện (thành công) | Đơn mua ở trạng thái đã thanh toán.<br>Gói tập mới ở trạng thái đã kích hoạt, có thời hạn và loại theo gói đã chọn, bắt đầu vào ngày xác định theo BR-03.<br>Dữ liệu giao dịch thu tiền đã được gửi sang hệ thống hoá đơn điện tử. |
| Hậu điều kiện tối thiểu | Nếu use case kết thúc không thành công vì hết thời hạn thanh toán (luồng 9a), đơn mua ở trạng thái đã huỷ và không có gói tập nào được kích hoạt cho đơn đó. Kết cục dữ liệu của các luồng chờ câu hỏi mở (4a, 4b, 4c, 10a, 12a) chưa quy định (Q-51, Q-24, Q-52, Q-13, Q-54). |
| Quan hệ | Không có |
| Điểm mở rộng | Không có |
| REQ | REQ-09, REQ-10, REQ-11, REQ-12, REQ-13, REQ-14, REQ-15, REQ-16, REQ-17, REQ-18, REQ-19, REQ-20, REQ-21, REQ-91, REQ-92 (theo P02); REQ-78, REQ-79 (thêm theo [Action] 1c, xem Đề xuất sửa artifact trước) |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Hội viên / Lễ tân | Yêu cầu mua hoặc gia hạn gói tập. |
| 2 | Phần mềm VietFit | Hiển thị các gói tập kèm thời hạn, loại và giá hiện hành (xem Dữ liệu ra 1). |
| 3 | Hội viên / Lễ tân | Chọn gói tập cần mua hoặc gia hạn (xem Dữ liệu vào 1). |
| 4 | Phần mềm VietFit | Xác định ngày bắt đầu của gói mới (BR-03). |
| 5 | Phần mềm VietFit | Tính số tiền phải trả theo giá gói và chương trình khuyến mãi áp dụng (cách áp dụng khuyến mãi: Q-09). |
| 6 | Phần mềm VietFit | Hiển thị tóm tắt đơn mua (xem Dữ liệu ra 2). |
| 7 | Hội viên / Lễ tân | Xác nhận mua gói tập. |
| 8 | Phần mềm VietFit | Tạo đơn mua ở trạng thái chờ thanh toán. |
| 9 | Phần mềm VietFit | Gửi thông tin đơn mua cho cổng thanh toán và chờ kết quả thanh toán trong thời hạn (BR-04). |
| 10 | Cổng thanh toán | Thu tiền thanh toán của hội viên và trả về kết quả giao dịch. |
| 11 | Phần mềm VietFit | Ghi nhận đơn mua đã thanh toán và kích hoạt gói tập. |
| 12 | Phần mềm VietFit | Gửi dữ liệu giao dịch thu tiền cho hệ thống hoá đơn điện tử (BR-05). |
| 13 | Phần mềm VietFit | Hiển thị gói tập đã kích hoạt cho hội viên hoặc lễ tân thực hiện giao dịch (xem Dữ liệu ra 3). |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
|---|---|---|---|---|
| 4a | Hội viên mua gói mới, không gia hạn gói nào | - | - | Chờ Q-51 |
| 4b | Hội viên gia hạn khi gói cũ đã hết hạn | - | - | Chờ Q-24 |
| 4c | Hội viên gia hạn khi gói cũ đang trong thời gian bảo lưu | - | - | Chờ Q-52 |
| 8a | Lễ tân bán gói tại quầy và khách trả bằng tiền mặt | Lễ tân | Thu tiền mặt của khách và xác nhận đã thu đủ số tiền phải trả. | Tiếp tục bước 11 |
| 8b | Lễ tân bán gói tại quầy và khách quẹt thẻ ngân hàng qua máy POS | Lễ tân | Nhập mã giao dịch in trên hoá đơn POS (xem Dữ liệu vào 2). | Tiếp tục bước 11 |
| 9a | Hết thời hạn (BR-04) mà đơn mua chưa thanh toán thành công | - | Huỷ đơn do hết thời hạn thanh toán | - |
| 9a1 | | Phần mềm VietFit | Huỷ đơn mua chưa thanh toán thành công. | |
| 9a2 | | Phần mềm VietFit | Thông báo cho hội viên đơn mua đã bị huỷ do hết thời hạn thanh toán (kênh thông báo: Q-53). | Kết thúc use case (thất bại) |
| 10a | Cổng thanh toán trả về giao dịch không thành công | Phần mềm VietFit | Thông báo cho hội viên giao dịch thanh toán không thành công (kênh thông báo: Q-53). | Chờ Q-13 |
| 12a | Hệ thống hoá đơn điện tử không nhận hoặc từ chối dữ liệu giao dịch | - | - | Chờ Q-54 |

## 4. Luồng con

Không có

## 5. Dữ liệu vào và dữ liệu ra

### Dữ liệu vào 1 (bước 3)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Thời hạn gói | Số tháng của gói tập cần mua hoặc gia hạn | Có | 1, 3, 6 hoặc 12 tháng (BR-01) | 6 tháng |
| 2 | Loại gói | Gói áp dụng cho một chi nhánh hoặc cho toàn chuỗi | Có | Một chi nhánh hoặc toàn chuỗi (BR-02) | Toàn chuỗi |
| 3 | Chi nhánh áp dụng | Chi nhánh mà gói loại một chi nhánh áp dụng | Chưa quy định (Q-50) | Chưa quy định (Q-50) | Chi nhánh 2 |
| 4 | Gói đang có cần gia hạn | Gói tập hiện có của hội viên mà hội viên muốn gia hạn | Chưa quy định (Q-56) | Chưa quy định (Q-56) | Gói 3 tháng toàn chuỗi, hết hạn ngày 30/11/2026 |
| 5 | Người mua gói | Người sở hữu gói khi lễ tân bán gói tại quầy | Chưa quy định (Q-01) | Chưa quy định (Q-01) | Hội viên Nguyễn Văn An |

### Dữ liệu vào 2 (bước 8b)

| STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
|---|---|---|---|---|---|
| 1 | Mã giao dịch POS | Mã giao dịch in trên hoá đơn của máy POS ngân hàng khi khách quẹt thẻ | Có | Chưa quy định (Q-55) | 004217 |

### Dữ liệu ra 1 (bước 2)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Thời hạn gói | Số tháng của gói tập | Số nguyên kèm "tháng" | 6 tháng |
| 2 | Loại gói | Gói áp dụng cho một chi nhánh hoặc cho toàn chuỗi | Văn bản: "Một chi nhánh" hoặc "Toàn chuỗi" | Toàn chuỗi |
| 3 | Chi nhánh áp dụng | Chi nhánh mà gói loại một chi nhánh áp dụng | Tên chi nhánh; chỉ gói loại một chi nhánh có giá trị này (Q-50) | Chi nhánh 2 |
| 4 | Giá gói | Giá hiện hành của gói do giám đốc chuỗi đặt (khuyến mãi: Q-09) | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 1.200.000 đ |

### Dữ liệu ra 2 (bước 6)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Gói tập | Thời hạn và loại của gói đã chọn | Văn bản, thời hạn kèm "tháng" | 6 tháng, toàn chuỗi |
| 2 | Ngày bắt đầu | Ngày bắt đầu của gói mới theo bước 4 | dd/MM/yyyy | 01/12/2026 |
| 3 | Số tiền phải trả | Số tiền hội viên phải thanh toán cho đơn | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 1.080.000 đ |

### Dữ liệu ra 3 (bước 13)

| STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
|---|---|---|---|---|
| 1 | Gói tập | Thời hạn và loại của gói đã kích hoạt | Văn bản, thời hạn kèm "tháng" | 6 tháng, toàn chuỗi |
| 2 | Ngày bắt đầu | Ngày bắt đầu của gói | dd/MM/yyyy | 01/12/2026 |
| 3 | Trạng thái gói | Trạng thái của gói sau khi kích hoạt | Văn bản | Đã kích hoạt |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-01 | Mỗi gói tập có thời hạn là 1, 3, 6 hoặc 12 tháng. | Ràng buộc | 2, Dữ liệu vào 1 | REQ-09 | Mới |
| BR-02 | Mỗi gói tập thuộc một trong hai loại: áp dụng cho một chi nhánh, hoặc áp dụng cho toàn chuỗi. | Ràng buộc | 2, Dữ liệu vào 1 | REQ-10 | Mới |
| BR-03 | Khi hội viên gia hạn lúc gói cũ còn hiệu lực, gói mới bắt đầu ngay sau ngày hết hạn của gói cũ. | Tính toán | 4 | REQ-17 | Mới |
| BR-04 | Đơn mua gói tập chưa thanh toán thành công trong 15 phút thì bị huỷ. | Kích hoạt hành động | 9, 9a | REQ-15, REQ-16 | Mới |
| BR-05 | Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử. | Ràng buộc | 12 | REQ-91 | Mới |

## 7. Yêu cầu đặc biệt

Không có

## 8. Thông tin bổ sung

- Luồng chính đi qua nhánh gia hạn khi gói cũ còn hiệu lực vì đây là trường hợp duy nhất nguồn nêu ngày bắt đầu của gói mới (REQ-17). Mua gói mới, gia hạn khi gói cũ đã hết hạn và gia hạn khi gói cũ đang bảo lưu rẽ ở bước 4 (4a, 4b, 4c) và chờ câu trả lời; các bước 5 đến 13 dùng chung cho mọi nhánh.
- Dữ liệu dùng chung: giá gói do UC-026 Đặt giá gói tập cung cấp (REQ-78); chương trình khuyến mãi do UC-027 Đặt chương trình khuyến mãi cung cấp (REQ-79). Cách áp dụng khuyến mãi cho đơn chờ Q-09; loại hàng mà giá và khuyến mãi áp dụng chờ Q-08, Q-10.
- Bước 11 tạo ra trạng thái gói mà UC-018 Vào chi nhánh đọc (REQ-41: còn hiệu lực, không đang bảo lưu, áp dụng cho chi nhánh) và ngày hết hạn mà UC-008 Nhắc gia hạn gói tập đọc (REQ-85). UC-008 do tác nhân thời gian khởi động hằng ngày lúc 8 giờ sáng theo lịch cố định nên UC này không hẹn hoặc huỷ mốc riêng cho UC-008 (F4.2 mục 17 không áp dụng). Hội viên đã gia hạn còn nhận nhắc hay không chờ Q-35. Ngày hết hạn của gói bị UC-006 Bảo lưu gói tập lùi thêm đúng số ngày bảo lưu (REQ-51).
- Thời hạn BR-04 được đặt ở bước 9 (đơn gửi cho cổng thanh toán). Thời điểm bắt đầu tính 15 phút, và việc thời hạn có áp dụng cho đơn bán tại quầy (luồng 8a, 8b) hay không, chờ Q-25.
- Đơn mua bị huỷ ở luồng 9a là trạng thái cuối. Thao tác dở dang trên đơn: giao dịch đang xử lý tại cổng thanh toán, hoặc kết quả thanh toán thành công đến sau khi đơn đã bị huỷ, chờ Q-14. Việc cổng thanh toán tự gửi kết quả về phần mềm vào thời điểm phần mềm không yêu cầu chờ Q-45. Việc huỷ đơn do hệ thống tự thực hiện hay có bước nhân viên duyệt hoặc gỡ chờ Q-43. Việc hội viên hoặc lễ tân tự huỷ đơn chưa thanh toán chờ Q-57.
- Hội viên thanh toán thất bại khi đơn còn trong thời hạn (luồng 10a): thanh toán lại trên cùng đơn hay phải tạo đơn mới chờ Q-13.
- Bán tại quầy: người mua tại quầy phải có tài khoản hay lễ tân tạo tài khoản cho người mua chờ Q-01 (nếu lễ tân tạo tài khoản thì đoạn đó thuộc use case khác, xem P02 mục Vấn đề còn mở). Xác thực của lễ tân chờ Q-47. Máy POS không kết nối với phần mềm; phần mềm chỉ nhận mã giao dịch do lễ tân nhập (REQ-21).
- Hoá đơn điện tử: phạm vi giao dịch thu tiền chờ Q-37; các trường dữ liệu gửi sang chờ Q-39; thứ tự giữa bước 11 và bước 12, và cách xử lý khi hệ thống hoá đơn điện tử không nhận dữ liệu, chờ Q-54. Việc lập, điều chỉnh, huỷ hoá đơn nằm ngoài phạm vi (project-profile.md, mục 4).
- Báo kết quả cho tác nhân: bước 13 và các luồng 9a2, 10a báo kết quả cho hội viên hoặc lễ tân. Kênh báo kết quả không thành công cho hội viên (thông báo đẩy, SMS hay chỉ hiển thị trên ứng dụng) chờ Q-53.
- Kết cục của các luồng 4a, 4b, 4c, 10a, 12a chưa quy định cách đi tiếp; sơ đồ kết thúc các luồng này ở node kết thúc kèm ghi chú "Chờ Q-nn".

## 9. Activity diagram

File: diagrams/P04-activity-UC-005.drawio (một trang, tên trang UC-005). Chủ thể hệ thống: Phần mềm VietFit. Tọa độ x, y của node trong bảng Node là tọa độ tương đối trong partition chứa nó; điểm uốn của cạnh là tọa độ tuyệt đối.

### Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| P-ACT-02-05 | Partition | Hội viên / Lễ tân | - | - | - | Chủ thể thực hiện | 0 | 0 | 300 | 2000 |
| P-ACT-05 | Partition | Lễ tân | - | - | - | Chủ thể thực hiện | 300 | 0 | 540 | 2000 |
| P-SYS | Partition | Phần mềm VietFit | - | - | - | Chủ thể thực hiện | 840 | 0 | 740 | 2000 |
| P-ACT-08 | Partition | Cổng thanh toán | - | - | - | Chủ thể thực hiện | 1580 | 0 | 300 | 2000 |
| INIT | Initial | - | - | P-ACT-02-05 | 1 | Điểm bắt đầu | 130 | 60 | 40 | 40 |
| A-1 | Action | Yêu cầu mua hoặc gia hạn gói tập | - | P-ACT-02-05 | 1 | - | 60 | 140 | 180 | 60 |
| A-2 | Action | Hiển thị gói tập, thời hạn, loại và giá | - | P-SYS | 2 | - | 270 | 240 | 180 | 60 |
| A-3 | Action | Chọn gói tập cần mua hoặc gia hạn | - | P-ACT-02-05 | 3 | - | 60 | 340 | 180 | 60 |
| A-4 | Action | Xác định ngày bắt đầu gói mới | - | P-SYS | 4 | - | 270 | 440 | 180 | 60 |
| D-4 | Decision | - | - | P-SYS | 4a, 4b, 4c | Rẽ nhánh theo tình trạng gói cũ | 340 | 540 | 40 | 40 |
| FINAL-2 | ActivityFinal | - | - | P-SYS | 4a | Chờ Q-51 | 580 | 540 | 40 | 40 |
| N-4a | Note | Chờ Q-51 | - | P-SYS | 4a | - | 660 | 540 | 70 | 40 |
| FINAL-3 | ActivityFinal | - | - | P-SYS | 4b | Chờ Q-24 | 580 | 640 | 40 | 40 |
| N-4b | Note | Chờ Q-24 | - | P-SYS | 4b | - | 660 | 640 | 70 | 40 |
| FINAL-4 | ActivityFinal | - | - | P-SYS | 4c | Chờ Q-52 | 580 | 740 | 40 | 40 |
| N-4c | Note | Chờ Q-52 | - | P-SYS | 4c | - | 660 | 740 | 70 | 40 |
| A-5 | Action | Tính số tiền phải trả | - | P-SYS | 5 | - | 270 | 620 | 180 | 60 |
| A-6 | Action | Hiển thị tóm tắt đơn mua | - | P-SYS | 6 | - | 270 | 720 | 180 | 60 |
| A-7 | Action | Xác nhận mua gói tập | - | P-ACT-02-05 | 7 | - | 60 | 820 | 180 | 60 |
| A-8 | Action | Tạo đơn mua chờ thanh toán | - | P-SYS | 8 | - | 270 | 920 | 180 | 60 |
| D-8 | Decision | - | - | P-SYS | 8a, 8b | Rẽ nhánh theo cách thu tiền | 340 | 1020 | 40 | 40 |
| A-8a | Action | Thu tiền mặt và xác nhận đã thu | - | P-ACT-05 | 8a | - | 20 | 1100 | 180 | 60 |
| A-8b1 | Action | Nhập mã giao dịch POS | - | P-ACT-05 | 8b | - | 300 | 1100 | 180 | 60 |
| A-9 | Action | Gửi đơn cho cổng thanh toán và chờ kết quả | - | P-SYS | 9 | Bắt đầu chờ theo BR-04 | 270 | 1100 | 180 | 60 |
| D-9 | Decision | - | - | P-SYS | 9a | Kết quả trong thời hạn hay hết thời hạn | 340 | 1200 | 40 | 40 |
| A-9a1 | Action | Huỷ đơn mua | - | P-SYS | 9a1 | - | 30 | 1190 | 180 | 60 |
| A-9a2 | Action | Thông báo đơn bị huỷ do quá hạn | - | P-SYS | 9a2 | - | 30 | 1290 | 180 | 60 |
| FINAL-5 | ActivityFinal | - | - | P-SYS | 9a2 | Kết thúc use case (thất bại) | 100 | 1390 | 40 | 40 |
| A-10 | Action | Thu tiền và trả kết quả giao dịch | - | P-ACT-08 | 10 | - | 60 | 1190 | 180 | 60 |
| D-10 | Decision | - | - | P-SYS | 10a | Giao dịch thành công hay không | 340 | 1380 | 40 | 40 |
| A-10a | Action | Thông báo giao dịch không thành công | - | P-SYS | 10a | - | 510 | 1470 | 180 | 60 |
| FINAL-6 | ActivityFinal | - | - | P-SYS | 10a | Chờ Q-13 | 580 | 1570 | 40 | 40 |
| N-10a | Note | Chờ Q-13 | - | P-SYS | 10a | - | 660 | 1570 | 70 | 40 |
| M-11 | Merge | - | - | P-SYS | 11 | Nhập luồng chính, 8a và 8b | 340 | 1460 | 40 | 40 |
| A-11 | Action | Ghi nhận đã thanh toán, kích hoạt gói | - | P-SYS | 11 | - | 270 | 1540 | 180 | 60 |
| A-12 | Action | Gửi dữ liệu thu tiền sang hoá đơn điện tử | - | P-SYS | 12 | - | 270 | 1640 | 180 | 60 |
| D-12 | Decision | - | - | P-SYS | 12a | Hệ thống hoá đơn điện tử nhận hay không | 340 | 1740 | 40 | 40 |
| FINAL-7 | ActivityFinal | - | - | P-SYS | 12a | Chờ Q-54 | 580 | 1740 | 40 | 40 |
| N-12a | Note | Chờ Q-54 | - | P-SYS | 12a | - | 660 | 1740 | 70 | 40 |
| A-13 | Action | Hiển thị gói tập đã kích hoạt | - | P-SYS | 13 | - | 270 | 1820 | 180 | 60 |
| FINAL-1 | ActivityFinal | - | - | P-SYS | 13 | Kết thúc thành công | 340 | 1920 | 40 | 40 |

### Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | A-2 | ControlFlow | - | Vượt partition | (150,220); (1200,220) |
| E-03 | A-2 | A-3 | ControlFlow | - | Vượt partition | (1200,320); (150,320) |
| E-04 | A-3 | A-4 | ControlFlow | - | Vượt partition | (150,420); (1200,420) |
| E-05 | A-4 | D-4 | ControlFlow | - | - | - |
| E-06 | D-4 | A-5 | ControlFlow | [gia hạn, gói cũ còn hiệu lực] | Nhánh luồng chính | - |
| E-07 | D-4 | FINAL-2 | ControlFlow | [mua gói mới, không gia hạn] | Luồng 4a | - |
| E-08 | D-4 | FINAL-3 | ControlFlow | [gia hạn, gói cũ đã hết hạn] | Luồng 4b | (1330,560); (1330,660) |
| E-09 | D-4 | FINAL-4 | ControlFlow | [gia hạn, gói cũ đang bảo lưu] | Luồng 4c | (1330,560); (1330,760) |
| E-10 | A-5 | A-6 | ControlFlow | - | - | - |
| E-11 | A-6 | A-7 | ControlFlow | - | Vượt partition | (1200,800); (150,800) |
| E-12 | A-7 | A-8 | ControlFlow | - | Vượt partition | (150,900); (1200,900) |
| E-13 | A-8 | D-8 | ControlFlow | - | - | - |
| E-14 | D-8 | A-9 | ControlFlow | [hội viên thanh toán qua cổng thanh toán] | Nhánh luồng chính | - |
| E-15 | D-8 | A-8a | ControlFlow | [khách trả tiền mặt tại quầy] | Luồng 8a | (410,1040) |
| E-16 | D-8 | A-8b1 | ControlFlow | [khách quẹt thẻ qua máy POS] | Luồng 8b | (690,1040) |
| E-17 | A-9 | D-9 | ControlFlow | - | - | - |
| E-18 | D-9 | A-10 | ControlFlow | [kết quả trong thời hạn (BR-04)] | Nhánh luồng chính | - |
| E-19 | D-9 | A-9a1 | ControlFlow | [hết thời hạn (BR-04)] | Luồng 9a | - |
| E-20 | A-9a1 | A-9a2 | ControlFlow | - | - | - |
| E-21 | A-9a2 | FINAL-5 | ControlFlow | - | Kết thúc use case (thất bại) | - |
| E-22 | A-10 | D-10 | ControlFlow | - | Vượt partition | (1730,1320); (1200,1320) |
| E-23 | D-10 | M-11 | ControlFlow | [giao dịch thành công] | Nhánh luồng chính | - |
| E-24 | D-10 | A-10a | ControlFlow | [giao dịch không thành công] | Luồng 10a | (1330,1400); (1330,1500) |
| E-25 | A-10a | FINAL-6 | ControlFlow | - | Chờ Q-13 | - |
| E-26 | A-8a | M-11 | ControlFlow | - | Tiếp tục bước 11 | (410,1480) |
| E-27 | A-8b1 | M-11 | ControlFlow | - | Tiếp tục bước 11 | (690,1480) |
| E-28 | M-11 | A-11 | ControlFlow | - | - | - |
| E-29 | A-11 | A-12 | ControlFlow | - | - | - |
| E-30 | A-12 | D-12 | ControlFlow | - | - | - |
| E-31 | D-12 | A-13 | ControlFlow | [hệ thống hoá đơn điện tử nhận dữ liệu] | Nhánh luồng chính | - |
| E-32 | D-12 | FINAL-7 | ControlFlow | [hệ thống hoá đơn điện tử không nhận hoặc từ chối] | Luồng 12a | - |
| E-33 | A-13 | FINAL-1 | ControlFlow | - | Mục tiêu đạt được | - |
| E-34 | N-4a | FINAL-2 | NoteLink | - | - | - |
| E-35 | N-4b | FINAL-3 | NoteLink | - | - | - |
| E-36 | N-4c | FINAL-4 | NoteLink | - | - | - |
| E-37 | N-10a | FINAL-6 | NoteLink | - | - | - |
| E-38 | N-12a | FINAL-7 | NoteLink | - | - | - |

### Bảng đối chiếu bước và node

| Bước UC | Node |
|---|---|
| 1 | INIT, A-1 |
| 2 | A-2 |
| 3 | A-3 |
| 4 | A-4, D-4 |
| 4a | D-4, FINAL-2, N-4a (không có action) |
| 4b | D-4, FINAL-3, N-4b (không có action) |
| 4c | D-4, FINAL-4, N-4c (không có action) |
| 5 | A-5 |
| 6 | A-6 |
| 7 | A-7 |
| 8 | A-8, D-8 |
| 8a | A-8a (nhập lại luồng chính tại M-11) |
| 8b | A-8b1 (nhập lại luồng chính tại M-11) |
| 9 | A-9, D-9 |
| 9a | D-9 (hàng tiêu đề, không có action riêng) |
| 9a1 | A-9a1 |
| 9a2 | A-9a2, FINAL-5 |
| 10 | A-10 |
| 10a | D-10, A-10a, FINAL-6, N-10a |
| 11 | M-11, A-11 |
| 12 | A-12, D-12 |
| 12a | D-12, FINAL-7, N-12a (không có action) |
| 13 | A-13, FINAL-1 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-50 | Gói tập loại một chi nhánh áp dụng cho chi nhánh nào, và ai xác định chi nhánh đó khi mua? (Hội viên chọn chi nhánh khi mua / Gói được đặt giá sẵn theo từng chi nhánh / Chi nhánh của quầy khi lễ tân bán / Khác - nêu rõ) | Bước 2, bước 3 (Dữ liệu vào 1 trường 3, Dữ liệu ra 1 trường 3); REQ-10; UC-026 | Mục 1 câu 3: "loại một chi nhánh hoặc toàn chuỗi" không nêu chi nhánh nào và ai chọn |
| Q-51 | Khi hội viên mua gói mới (không gia hạn gói nào), gói bắt đầu vào ngày nào? (Ngày thanh toán thành công / Ngày hội viên chọn / Khác - nêu rõ) | Bước 4, luồng 4a; hậu điều kiện (BR-03) | Mục 2 câu 1 và câu 3: nguồn chỉ nêu ngày bắt đầu cho trường hợp gia hạn khi gói cũ còn hiệu lực |
| Q-52 | Gói đang trong thời gian bảo lưu có được tính là còn hiệu lực khi hội viên gia hạn không, và nếu có thì ngày hết hạn của gói cũ dùng để tính ngày bắt đầu là ngày hết hạn đã lùi theo thời gian bảo lưu? (Tính là còn hiệu lực, dùng ngày hết hạn đã lùi / Không tính, xử lý như gói cũ đã hết hạn / Khác - nêu rõ) | Bước 4, luồng 4c; BR-03 | Mục 2 câu 3 ("gói cũ còn hiệu lực"), Mục 5 câu 2 ("còn hiệu lực, không đang bảo lưu") và Mục 6 câu 2 ("Ngày hết hạn của gói được lùi thêm đúng số ngày bảo lưu") |
| Q-53 | Hội viên được báo bằng kênh nào khi đơn mua bị huỷ do quá 15 phút và khi giao dịch thanh toán không thành công? (Thông báo đẩy, hoặc SMS khi chưa cài ứng dụng / Chỉ hiển thị trên ứng dụng khi hội viên đang dùng / Khác - nêu rõ) | Luồng 9a2, 10a; REQ-87, REQ-88 | Mục 2 câu 2: "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ" không nêu việc báo cho hội viên; Mục 10 câu 1 nêu kênh thông báo nhưng không nói thông báo này có thuộc phạm vi đó không |
| Q-54 | Khi hệ thống hoá đơn điện tử không nhận hoặc từ chối dữ liệu giao dịch thu tiền, gói tập vẫn được kích hoạt và dữ liệu được gửi lại sau, hay giao dịch phải dừng? (Gói vẫn kích hoạt, gửi lại sau / Không kích hoạt gói - nêu rõ) | Thứ tự bước 11 và bước 12; luồng 12a; hậu điều kiện | Mục 10 câu 2: "Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử" không nêu xử lý khi xuất không được; hồ sơ dự án ghi chưa có tài liệu API |
| Q-55 | Mã giao dịch POS do lễ tân nhập có quy tắc về định dạng, độ dài hoặc kiểm tra trùng với mã đã nhập không? (Nêu quy tắc / Không kiểm tra) | Luồng 8b, Dữ liệu vào 2 | Mục 2 câu 4: "lễ tân nhập mã giao dịch in trên hoá đơn POS" không nêu điều kiện hợp lệ của mã |
| Q-56 | Khi gia hạn, hội viên chỉ định gói đang có nào để gia hạn, và gói đó phải thoả điều kiện gì (cùng loại, cùng thời hạn với gói mới; chưa chuyển nhượng cho người khác)? (Hội viên chọn gói đang có, không ràng buộc thêm / Hệ thống tự xác định gói đang có / Có ràng buộc - nêu rõ) | Bước 3 (Dữ liệu vào 1 trường 4), bước 4; REQ-12, REQ-17 | Mục 2 câu 1 và câu 3: "gia hạn gói tập", "gói cũ" không nêu cách xác định gói cũ |
| Q-57 | Hội viên hoặc lễ tân có được huỷ đơn mua chưa thanh toán trước khi hết 15 phút không? (Có - nêu ai huỷ và đến lúc nào / Không, chỉ hệ thống huỷ khi hết thời hạn) | Thêm luồng huỷ đơn trong phiên mua (luồng *a); BR-04 | Mục 2 câu 2: nguồn chỉ nêu việc đơn bị huỷ khi hết 15 phút, không nêu tác nhân huỷ đơn |

Các câu hỏi đã cấp ở bước trước và làm đổi use case này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-01 (người mua tại quầy có tài khoản không), Q-08, Q-09, Q-10 (phạm vi và cách áp dụng giá, khuyến mãi), Q-13 (thanh toán lại khi thất bại), Q-14 (kết quả thanh toán đến sau khi đơn bị huỷ), Q-24 (gia hạn khi gói cũ đã hết hạn), Q-25 (cách tính 15 phút), Q-35 (nhắc gia hạn sau khi đã gia hạn), Q-37, Q-39 (phạm vi và dữ liệu hoá đơn điện tử), Q-43 (hệ thống tự huỷ đơn), Q-45 (cổng thanh toán tự gửi kết quả), Q-47 (xác thực của lễ tân), Q-36 (hội viên chưa cài ứng dụng nhận SMS).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-005 (bảng 4b cột REQ; Mục 5) | Đặc tả dùng REQ-78 (giá gói) ở bước 2 và bước 5 và REQ-79 (chương trình khuyến mãi) ở bước 5, nhưng hai REQ này chưa nằm ở cột REQ của UC-005 | Thêm REQ-78, REQ-79 vào cột REQ của UC-005 ở bảng 4b và vào Mục 5 (ma trận REQ --> UC) |

## Vấn đề còn mở

Các mục Target đạt, trừ mục 8 và mục 12 (đạt một phần), với các điểm cần người dùng lưu ý:

- Target 12: ở chế độ NGHIEM_NGAT, một số bước không có câu gốc trực tiếp trong nguồn. Bước 6 và bước 7 (hiển thị tóm tắt đơn rồi hội viên hoặc lễ tân xác nhận mua) là cặp yêu cầu - phản hồi cần để lễ tân biết số tiền phải thu (luồng 8a) và để đơn chỉ được tạo sau khi người mua đồng ý; bước 2 cần để người mua có giá mà chọn gói (REQ-78). Bước thông báo cho hội viên ở luồng 9a2 và 10a được viết để thoả Target 5a (luồng kết thúc có tác nhân người phải được báo kết quả), kênh báo được hỏi ở Q-53.
- Target 8: các luồng 4b, 10a chờ Q-24, Q-13 là câu hỏi đã cấp ở P00, không chép lại vào mục Câu hỏi mở của đặc tả này để mỗi mã chỉ trỏ tới một câu hỏi duy nhất (Conventions C3); các mã được liệt kê ngay dưới bảng Câu hỏi mở.
- Vị trí bước bắt đầu chờ 15 phút (bước 9) là lựa chọn trong hai cách tính của Q-25; nếu Q-25 trả lời tính từ lúc tạo đơn thì bước bắt đầu chờ chuyển về bước 8 và khoảng bước của luồng 9a đổi theo.
- Luồng 4a, 4b, 4c, 10a, 12a kết thúc bằng "Chờ Q-nn", nên hậu điều kiện tối thiểu của các luồng này chưa xác định (ghi ở mục 1).
- Partition "Lễ tân" tách riêng khỏi partition "Hội viên / Lễ tân" vì hai luồng 8a, 8b chỉ do lễ tân thực hiện; sơ đồ vì vậy có 4 partition.
- Các giá trị ở cột Ví dụ (số tiền, ngày, tên chi nhánh, mã giao dịch POS, tên hội viên) là giá trị minh hoạ, không phải dữ liệu của nguồn.
- Mục 8a Kịch bản chính không lập vì MUC_CHI_TIET của hồ sơ dự án là GON.
