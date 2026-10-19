# Sổ đăng ký quy tắc nghiệp vụ - Hệ thống quản lý chuỗi phòng tập VietFit

| BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
| BR-01 | Mỗi gói tập có thời hạn là 1, 3, 6 hoặc 12 tháng. | Ràng buộc | UC-005 | REQ-09 | P04 UC-005 | Hiệu lực | - |
| BR-02 | Mỗi gói tập thuộc một trong hai loại: áp dụng cho một chi nhánh, hoặc áp dụng cho toàn chuỗi. | Ràng buộc | UC-005 | REQ-10 | P04 UC-005 | Hiệu lực | - |
| BR-03 | Khi hội viên gia hạn lúc gói cũ còn hiệu lực, gói mới bắt đầu ngay sau ngày hết hạn của gói cũ. | Tính toán | UC-005 | REQ-17 | P04 UC-005 | Hiệu lực | Trường hợp gói cũ đã hết hạn, đang bảo lưu hoặc mua gói mới chờ Q-24, Q-52, Q-51 |
| BR-04 | Đơn mua gói tập chưa thanh toán thành công trong 15 phút thì bị huỷ. | Kích hoạt hành động | UC-005 | REQ-15, REQ-16 | P04 UC-005 | Hiệu lực | Áp dụng cho đơn bán tại quầy chờ Q-25 |
| BR-05 | Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử. | Ràng buộc | UC-005 | REQ-91 | P04 UC-005 | Hiệu lực | Phạm vi giao dịch thu tiền chờ Q-37 |
| BR-06 | Hội viên chỉ được đặt chỗ lớp nhóm sớm nhất 7 ngày trước giờ học. | Ràng buộc | UC-010 | REQ-23 | P04 UC-010 | Hiệu lực | Mâu thuẫn với BR-07, chờ Q-11; mốc muộn nhất để đặt chờ Q-58 |
| BR-07 | Đặt chỗ lớp nhóm cho tuần mới mở lúc 6 giờ sáng thứ Hai. | Ràng buộc | UC-010 | REQ-93 | P04 UC-010 | Hiệu lực | Mâu thuẫn với BR-06, chờ Q-11 |
| BR-08 | Mỗi hội viên được đặt chỗ tối đa 2 lớp nhóm trong một ngày. | Ràng buộc | UC-010 | REQ-24 | P04 UC-010 | Hiệu lực | Cách tính ngày và có tính lớp trong danh sách chờ chờ Q-60 |
| BR-09 | Hội viên bị khoá quyền đặt lớp trong 7 ngày thì không đặt được chỗ lớp nhóm trong thời gian khoá. | Ràng buộc | UC-010 | REQ-38 | P04 UC-010 | Hiệu lực | Điều kiện dẫn tới khoá thuộc UC-016; chỗ đã đặt của hội viên bị khoá chờ Q-20 |
| BR-10 | Sức chứa của mỗi lớp nhóm được xác định theo phòng. | Sự kiện | UC-010 | REQ-25 | P04 UC-010 | Hiệu lực | Sức chứa lớp so với sức chứa phòng chờ Q-03 |
| BR-11 | Số chỗ đã đặt của một lớp nhóm không được vượt sức chứa, kể cả khi nhiều hội viên đặt chỗ cùng lúc. | Ràng buộc | UC-010 | REQ-95, REQ-94 | P04 UC-010 | Hiệu lực | Chỗ giữ riêng cho người đứng đầu danh sách chờ chờ Q-22 |
| BR-12 | Lớp nhóm đã đủ chỗ thì hội viên được vào danh sách chờ của lớp. | Kích hoạt hành động | UC-010 | REQ-26 | P04 UC-010 | Hiệu lực | Tự vào hay hội viên chọn chờ Q-62 |
| BR-13 | Lớp nhóm có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học thì bị huỷ. | Kích hoạt hành động | UC-015 | REQ-73, REQ-74 | P04 UC-015 | Hiệu lực | Việc nhân viên duyệt hoặc gỡ chờ Q-43; chỗ giữ riêng và chỗ của hội viên bị khoá có tính vào số người đặt chỗ hay không chờ Q-22, Q-20 |
| BR-14 | Thông báo cho hội viên gửi qua thông báo đẩy của ứng dụng; hội viên chưa cài ứng dụng thì nhận SMS qua cổng SMS. | Kích hoạt hành động | UC-015 | REQ-87, REQ-88 | P04 UC-015 | Hiệu lực | Cách xác định hội viên chưa cài ứng dụng chờ Q-36 |
| BR-15 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên còn hiệu lực. | Ràng buộc | UC-018 | REQ-41 | P04 UC-018 | Hiệu lực | Gói buổi tập cá nhân có tính là gói tập chờ Q-18; hội viên có nhiều gói cùng lúc chờ Q-69 |
| BR-16 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên không đang bảo lưu. | Ràng buộc | UC-018 | REQ-41 | P04 UC-018 | Hiệu lực | Hội viên có nhiều gói cùng lúc chờ Q-69 |
| BR-17 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên áp dụng cho chi nhánh có cửa quay đó. | Ràng buộc | UC-018 | REQ-41, REQ-10 | P04 UC-018 | Hiệu lực | Cách cửa quay cho biết chi nhánh chờ Q-67; hội viên có nhiều gói cùng lúc chờ Q-69 |
| BR-18 | Mã QR trên vé tập một ngày chỉ dùng được trong ngày mua vé. | Ràng buộc | UC-018 | REQ-44 | P04 UC-018 | Hiệu lực | Số lần dùng vé trong ngày chờ Q-40 |
| BR-19 | Mã QR trên vé tập một ngày chỉ dùng được tại chi nhánh đã mua vé. | Ràng buộc | UC-018 | REQ-45 | P04 UC-018 | Hiệu lực | Cách cửa quay cho biết chi nhánh chờ Q-67 |
| BR-20 | Hội viên đặt chỗ lớp nhóm được xem là không vào lớp khi không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu lớp. | Suy luận | UC-018 | REQ-35 | P04 UC-018 | Hiệu lực | UC-016 kiểm tra quy tắc này khi được đặc tả; lượt quẹt bị từ chối có tính hay không chờ Q-71 |
