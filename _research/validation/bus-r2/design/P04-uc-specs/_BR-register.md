# Sổ đăng ký quy tắc nghiệp vụ - Hệ thống bán vé xe khách SaoViet Bus

| BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
| BR-01 | Mỗi lần đặt vé, hành khách chọn tối đa 5 chỗ. | Ràng buộc | UC-009 | REQ-08 | P04 UC-009 | Hiệu lực | Luồng bán tại quầy chờ Q-12 |
| BR-02 | Không được có hai vé cùng một chỗ trên một chuyến. | Ràng buộc | UC-004, UC-005, UC-009, UC-014, UC-015 | REQ-75 | P04 UC-009 | Hiệu lực | UC-004, UC-005, UC-014, UC-015 theo P02 Mục 5 (REQ-75). Tính chất xử lý đồng thời xem NFR-04 |
| BR-03 | Các chỗ hành khách đã chọn được giữ trong 10 phút để thanh toán, tính từ lúc hệ thống giữ các chỗ đó (ASM-18); hết 10 phút mà chưa thanh toán thành công thì chỗ được trả lại cho người khác. | Ràng buộc | UC-009, UC-010 | REQ-13, REQ-14, REQ-17 | P04 UC-009 | Hiệu lực | UC-009 theo ASM-18 (chờ Q-18); UC-010 theo P02 Mục 5 (REQ-17) |
| BR-04 | Mỗi chỗ có một mã vé. | Ràng buộc | UC-004, UC-009, UC-017 | REQ-19 | P04 UC-009 | Hiệu lực | UC-004 theo P02 Mục 5 (REQ-19) |
| BR-05 | Vé của một chuyến chỉ bán trực tuyến cho đến giờ xuất bến; từ giờ xuất bến trở đi không giữ chỗ để bán (ASM-21). | Ràng buộc | UC-009 | REQ-04 | P04 UC-009 | Hiệu lực | UC-009 theo ASM-21 (chờ Q-13); luồng bán tại quầy cũng chờ Q-13 |
| BR-06 | Giao dịch thanh toán thành công đến sau khi hết thời hạn giữ chỗ và chỗ đã trả lại cho người khác thì không phát hành vé và khoản tiền được hoàn cho hành khách (ASM-22). | Kích hoạt hành động | UC-009, UC-010 | REQ-15, REQ-17 | P04 UC-009 | Hiệu lực | UC-009 theo ASM-22 (chờ Q-19); phần xử lý giao dịch đến sau thuộc UC-010 (UC-010 theo P02 Mục 5, REQ-15, REQ-17) |
| BR-07 | Số tiền hoàn cho mỗi vé của chuyến bị huỷ bằng 100% giá vé của vé đó. | Tính toán | UC-017, UC-018 | REQ-58 | P04 UC-017 | Hiệu lực | UC-018 theo P02 Mục 5 (REQ-58) |
| BR-08 | Vé của chuyến bị huỷ được hoàn tiền qua cùng kênh với kênh mua vé: vé mua trực tuyến hoàn qua cổng thanh toán, vé mua tại quầy hoàn tiền mặt tại quầy (ASM-08). | Ràng buộc | UC-017, UC-018 | REQ-57, REQ-59 | P04 UC-017 | Hiệu lực | UC-018 theo P02 Mục 5 (REQ-57, REQ-59); theo ASM-08 (chờ Q-07) |
| BR-09 | Chuyến đã bị huỷ không được huỷ lại (ASM-26). | Ràng buộc | UC-017 | REQ-55 | P04 UC-017 | Hiệu lực | UC-017 theo ASM-26 (chờ Q-46) |
| BR-10 | Chuyến từ giờ xuất bến trở đi không được huỷ (ASM-26). | Ràng buộc | UC-017 | REQ-55 | P04 UC-017 | Hiệu lực | UC-017 theo ASM-26 (chờ Q-46) |
| BR-11 | Khi một chuyến bị huỷ, mọi hành khách đã có vé của chuyến phải được thông báo qua SMS (phạm vi "đã có vé" theo ASM-30). | Kích hoạt hành động | UC-017 | REQ-56 | P04 UC-017 | Hiệu lực | UC-017 theo ASM-30 (chờ Q-25) |
| BR-12 | Vé đặt qua điện thoại phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến. | Ràng buộc | UC-005, UC-006, UC-007 | REQ-31 | P06 | Hiệu lực | Chờ Q-14 (đặt khi còn dưới 60 phút). UC-005, UC-006, UC-007 theo P02 Mục 5 (REQ-31). Mốc của chuyến đã huỷ bị bỏ theo ASM-28 (chờ Q-47) |
| BR-13 | Trả vé trước giờ xuất bến từ 24 giờ trở lên được hoàn 90% giá vé. | Tính toán | UC-012 | REQ-37 | P06 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-37). Hoàn một phần số tiền của giao dịch chờ Q-20 (ASM-32) |
| BR-14 | Trả vé trước giờ xuất bến từ 4 giờ đến dưới 24 giờ được hoàn 50% giá vé. | Tính toán | UC-012 | REQ-38 | P06 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-38). Hoàn một phần số tiền của giao dịch chờ Q-20 (ASM-32) |
| BR-15 | Vé không được trả khi còn dưới 4 giờ trước giờ xuất bến. | Ràng buộc | UC-012 | REQ-39 | P06 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-39) |
| BR-16 | Vé mua tại quầy được hoàn tiền mặt tại quầy. | Ràng buộc | UC-012 | REQ-41 | P06 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-41). Câu nguồn bị động, chủ thể thực hiện theo ASM-04 (chờ Q-03). Hoàn tiền của chuyến bị huỷ xem BR-08 |
| BR-17 | Mỗi vé chỉ được đổi một lần. | Ràng buộc | UC-014, UC-015 | REQ-42 | P06 | Hiệu lực | UC-014, UC-015 theo P02 Mục 5 (REQ-42) |
| BR-18 | Vé chỉ được đổi chậm nhất 4 giờ trước giờ xuất bến. | Ràng buộc | UC-014, UC-015 | REQ-43 | P06 | Hiệu lực | Giờ xuất bến của chuyến cũ hay chuyến mới chờ Q-21. UC-014, UC-015 theo P02 Mục 5 (REQ-43) |
| BR-19 | Hành khách trả thêm phần chênh lệch khi vé mới đắt hơn vé cũ. | Tính toán | UC-010, UC-014, UC-015 | REQ-44 | P06 | Hiệu lực | Kênh thanh toán phần chênh lệch chờ Q-22 (ASM-13). UC-010, UC-014, UC-015 theo P02 Mục 5 (REQ-44) |
| BR-20 | Hành khách không được hoàn phần chênh lệch khi vé mới rẻ hơn vé cũ (ASM-05). | Ràng buộc | UC-014, UC-015 | REQ-45 | P06 | Hiệu lực | Theo ASM-05 (chờ Q-08). UC-014, UC-015 theo P02 Mục 5 (REQ-45) |
| BR-21 | Một xe không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-016 | REQ-52 | P06 | Hiệu lực | Thời gian chạy của chuyến lấy từ đâu chờ Q-15. UC-016 theo P02 Mục 5 (REQ-52) |
| BR-22 | Một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-016 | REQ-53 | P06 | Hiệu lực | Tách khỏi BR-21 vì đối tượng khác (xe, tài xế) theo hai REQ riêng. Chờ Q-15. UC-016 theo P02 Mục 5 (REQ-53) |
| BR-23 | Một tài xế không được lái quá 10 giờ trong một ngày. | Ràng buộc | UC-016 | REQ-54 | P06 | Hiệu lực | Cách tính ngày chờ Q-16; thời gian chạy chờ Q-15. UC-016 theo P02 Mục 5 (REQ-54) |
| BR-24 | Mức tăng giá vé cho một khoảng ngày tối đa 30%. | Ràng buộc | UC-024 | REQ-62 | P06 | Hiệu lực | Phạm vi khoảng ngày chờ Q-23; ngày áp dụng chờ Q-24. UC-024 theo P02 Mục 5 (REQ-62) |
| BR-25 | Mã vé không hợp lệ khi sai chuyến, vé đã huỷ hoặc vé đã soát. | Suy luận | UC-026 | REQ-66 | P06 | Hiệu lực | Ba trường hợp đầy đủ hay còn trường hợp khác chờ Q-28. UC-026 theo P02 Mục 5 (REQ-66) |
| BR-26 | Danh sách hành khách của chuyến được gửi về máy soát vé vào thời điểm 15 phút trước giờ xuất bến. | Kích hoạt hành động | UC-025 | REQ-70 | P06 | Hiệu lực | Nội dung danh sách chờ Q-30; vé phát sinh sau thời điểm gửi chờ Q-29. Mốc của chuyến đã huỷ bị bỏ theo ASM-28 (chờ Q-47). UC-025 theo P02 Mục 5 (REQ-70) |
