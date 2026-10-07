# Sổ đăng ký quy tắc nghiệp vụ - Hệ thống bán vé xe khách SaoViet Bus

| BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái |
|---|---|---|---|---|---|---|
| BR-01 | Mỗi lần đặt vé trực tuyến được chọn tối đa 5 chỗ. | Ràng buộc | UC-002 | REQ-08 | P04 UC-002 | Hiệu lực |
| BR-02 | Trên một chuyến, hai vé không được cùng một chỗ. | Ràng buộc | UC-002 | REQ-67 | P04 UC-002 | Hiệu lực |
| BR-03 | Một chỗ của chuyến là còn trống khi chỗ đó chưa có vé và không đang được giữ cho một lần đặt chưa hết thời hạn giữ chỗ. | Suy luận | UC-002, UC-008 | REQ-12, REQ-16, REQ-67 | P04 UC-002 | Hiệu lực |
| BR-04 | Giá vé được đặt theo tuyến và loại xe. | Sự kiện | UC-002 | REQ-52 | P04 UC-002 | Hiệu lực |
| BR-05 | Giá một vé bằng giá vé theo tuyến và loại xe của chuyến nhân với (1 + mức tăng giá lễ Tết theo phần trăm) khi ngày xuất bến của chuyến thuộc khoảng ngày có mức tăng giá áp dụng cho chuyến (ASM-12); ngoài khoảng ngày đó, mức tăng bằng 0%. | Tính toán | UC-002 | REQ-52, REQ-53 | P04 UC-002 | Hiệu lực |
| BR-06 | Tổng tiền của một lần đặt vé bằng tổng giá vé của các chỗ đã chọn trong lần đặt đó. | Tính toán | UC-002 | REQ-12, REQ-14 | P04 UC-002 | Hiệu lực |
| BR-07 | Các chỗ đã chọn được giữ chờ thanh toán trực tuyến trong 10 phút kể từ khi bắt đầu giữ. | Ràng buộc | UC-002 | REQ-13 | P04 UC-002 | Hiệu lực |
| BR-08 | Khi hết thời hạn giữ chỗ (BR-07) mà chưa thanh toán thành công, các chỗ đang giữ của lần đặt được trả lại trạng thái còn trống cho người khác chọn. | Kích hoạt hành động | UC-002 | REQ-16 | P04 UC-002 | Hiệu lực |
| BR-09 | Khi thanh toán trực tuyến cho các chỗ đang giữ thành công, hệ thống phát hành vé cho các chỗ đó. | Kích hoạt hành động | UC-002 | REQ-17 | P04 UC-002 | Hiệu lực |
| BR-10 | Mỗi chỗ được phát hành thành đúng một vé có một mã vé. | Ràng buộc | UC-002, UC-008, UC-013, UC-015 | REQ-18 | P04 UC-002 | Hiệu lực |
| BR-11 | Vé chỉ được trả qua kênh đã mua vé: vé mua trực tuyến do hành khách trả trên website, vé mua tại quầy (gồm vé đặt qua điện thoại đã thanh toán tại quầy) do nhân viên bán vé trả tại quầy (ASM-02). | Ràng buộc | UC-008 | REQ-29, REQ-34, REQ-36 | P04 UC-008 | Hiệu lực |
| BR-12 | Vé không được trả khi thời gian còn lại trước giờ xuất bến của chuyến dưới 4 giờ. | Ràng buộc | UC-008 | REQ-33 | P04 UC-008 | Hiệu lực |
| BR-13 | Vé được trả khi thời gian còn lại trước giờ xuất bến của chuyến từ 24 giờ trở lên được hoàn 90% giá vé. | Tính toán | UC-008 | REQ-31 | P04 UC-008 | Hiệu lực |
| BR-14 | Vé được trả khi thời gian còn lại trước giờ xuất bến của chuyến từ 4 giờ đến dưới 24 giờ được hoàn 50% giá vé. | Tính toán | UC-008 | REQ-32 | P04 UC-008 | Hiệu lực |
| BR-15 | Vé mua trực tuyến được hoàn tiền qua cổng thanh toán trực tuyến của đối tác. | Ràng buộc | UC-008, UC-013 (ASM-28) | REQ-34 | P04 UC-008 | Hiệu lực |
| BR-16 | Vé mua tại quầy được hoàn bằng tiền mặt tại quầy. | Ràng buộc | UC-008, UC-013 (ASM-28) | REQ-36 | P04 UC-008 | Hiệu lực |
| BR-17 | Số tiền hoàn của một vé thuộc chuyến bị nhà xe huỷ bằng 100% giá vé. | Tính toán | UC-013 | REQ-50 | P04 UC-013 | Hiệu lực |
| BR-18 | Khi chuyến bị huỷ, mọi hành khách đã có vé còn hiệu lực của chuyến được báo việc huỷ chuyến qua SMS (ASM-27). | Kích hoạt hành động | UC-013 | REQ-48 | P04 UC-013 | Hiệu lực |
| BR-19 | Khi chuyến bị huỷ, mọi hành khách đã có vé còn hiệu lực của chuyến được hoàn tiền theo BR-17 (ASM-27). | Kích hoạt hành động | UC-013 | REQ-49 | P04 UC-013 | Hiệu lực |
| BR-20 | Khi soát vé lên xe, vé không thuộc chuyến đang soát là vé không hợp lệ với lý do sai chuyến. | Suy luận | UC-015 | REQ-58 | P04 UC-015 | Hiệu lực |
| BR-21 | Khi soát vé lên xe, vé đã bị huỷ là vé không hợp lệ với lý do vé đã huỷ. | Suy luận | UC-015 | REQ-58 | P04 UC-015 | Hiệu lực |
| BR-22 | Khi soát vé lên xe, vé đã được soát trước đó là vé không hợp lệ với lý do vé đã soát. | Suy luận | UC-015 | REQ-58 | P04 UC-015 | Hiệu lực |
| BR-23 | Vé bán tại quầy cho khách mua trực tiếp được thanh toán bằng tiền mặt. | Sự kiện | UC-005 | REQ-22 | P06 | Hiệu lực |
| BR-24 | Đặt chỗ qua điện thoại phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến của chuyến. | Ràng buộc | UC-004, UC-005, UC-006 | REQ-27 | P06 | Hiệu lực |
| BR-25 | Vé chỉ được đổi sang chuyến khác cùng tuyến. | Ràng buộc | UC-007 | REQ-37 | P06 | Hiệu lực |
| BR-26 | Mỗi vé chỉ được đổi một lần. | Ràng buộc | UC-007 | REQ-38 | P06 | Hiệu lực |
| BR-27 | Vé chỉ được đổi chậm nhất 4 giờ trước giờ xuất bến. | Ràng buộc | UC-007 | REQ-39 | P06 | Hiệu lực |
| BR-28 | Khi vé mới đắt hơn vé cũ, hành khách trả thêm phần chênh lệch giữa giá vé mới và giá vé cũ. | Tính toán | UC-007, UC-003 | REQ-40 | P06 | Hiệu lực |
| BR-29 | Một xe không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-012 | REQ-43 | P06 | Hiệu lực |
| BR-30 | Một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-012 | REQ-44 | P06 | Hiệu lực |
| BR-31 | Tài xế không được lái quá 10 giờ trong một ngày. | Ràng buộc | UC-012 | REQ-45 | P06 | Hiệu lực |
| BR-32 | Mức tăng giá lễ Tết theo phần trăm tối đa là 30%. | Ràng buộc | UC-017 | REQ-54 | P06 | Hiệu lực |
| BR-33 | Danh sách hành khách của chuyến được gửi về máy soát vé cầm tay vào thời điểm 15 phút trước giờ xuất bến của chuyến. | Kích hoạt hành động | UC-014 | REQ-62 | P06 | Hiệu lực |
