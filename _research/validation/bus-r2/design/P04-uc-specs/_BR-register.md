# Sổ đăng ký quy tắc nghiệp vụ - Hệ thống bán vé xe khách SaoViet Bus

| BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
| BR-01 | Mỗi lần đặt vé, hành khách chọn tối đa 5 chỗ. | Ràng buộc | UC-009 | REQ-08 | P04 UC-009 | Hiệu lực | Luồng bán tại quầy chờ Q-12 |
| BR-02 | Không được có hai vé cùng một chỗ trên một chuyến. | Ràng buộc | UC-009 | REQ-75 | P04 UC-009 | Hiệu lực | P02 còn gán REQ-75 cho UC-004, UC-005, UC-014, UC-015; các UC đó thêm mã vào cột UC áp dụng khi được đặc tả |
| BR-03 | Các chỗ hành khách đã chọn được giữ trong 10 phút để thanh toán, tính từ lúc hệ thống giữ các chỗ đó (ASM-18); hết 10 phút mà chưa thanh toán thành công thì chỗ được trả lại cho người khác. | Ràng buộc | UC-009 | REQ-13, REQ-14, REQ-17 | P04 UC-009 | Hiệu lực | UC-009 theo ASM-18 (chờ Q-18) |
| BR-04 | Mỗi chỗ có một mã vé. | Ràng buộc | UC-009, UC-017 | REQ-19 | P04 UC-009 | Hiệu lực | P02 còn gán REQ-19 cho UC-004 |
| BR-05 | Vé của một chuyến chỉ bán trực tuyến cho đến giờ xuất bến; từ giờ xuất bến trở đi không giữ chỗ để bán (ASM-21). | Ràng buộc | UC-009 | REQ-04 | P04 UC-009 | Hiệu lực | UC-009 theo ASM-21 (chờ Q-13); luồng bán tại quầy cũng chờ Q-13 |
| BR-06 | Giao dịch thanh toán thành công đến sau khi hết thời hạn giữ chỗ và chỗ đã trả lại cho người khác thì không phát hành vé và khoản tiền được hoàn cho hành khách (ASM-22). | Kích hoạt hành động | UC-009 | REQ-15, REQ-17 | P04 UC-009 | Hiệu lực | UC-009 theo ASM-22 (chờ Q-19); phần xử lý giao dịch đến sau thuộc UC-010 |
| BR-07 | Số tiền hoàn cho mỗi vé của chuyến bị huỷ bằng 100% giá vé của vé đó. | Tính toán | UC-017 | REQ-58 | P04 UC-017 | Hiệu lực | UC-018 áp dụng khi được đặc tả |
| BR-08 | Vé của chuyến bị huỷ được hoàn tiền qua cùng kênh với kênh mua vé: vé mua trực tuyến hoàn qua cổng thanh toán, vé mua tại quầy hoàn tiền mặt tại quầy (ASM-08). | Ràng buộc | UC-017 | REQ-57, REQ-59 | P04 UC-017 | Hiệu lực | UC-018 áp dụng khi được đặc tả; theo ASM-08 (chờ Q-07) |
| BR-09 | Chuyến đã bị huỷ không được huỷ lại (ASM-26). | Ràng buộc | UC-017 | REQ-55 | P04 UC-017 | Hiệu lực | UC-017 theo ASM-26 (chờ Q-46) |
| BR-10 | Chuyến từ giờ xuất bến trở đi không được huỷ (ASM-26). | Ràng buộc | UC-017 | REQ-55 | P04 UC-017 | Hiệu lực | UC-017 theo ASM-26 (chờ Q-46) |
| BR-11 | Khi một chuyến bị huỷ, mọi hành khách đã có vé của chuyến phải được thông báo qua SMS (phạm vi "đã có vé" theo ASM-30). | Kích hoạt hành động | UC-017 | REQ-56 | P04 UC-017 | Hiệu lực | UC-017 theo ASM-30 (chờ Q-25) |
