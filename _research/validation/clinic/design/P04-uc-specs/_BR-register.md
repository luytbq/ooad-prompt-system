# Sổ đăng ký quy tắc nghiệp vụ - Hệ thống đặt lịch khám ClinicBook

| BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái |
|---|---|---|---|---|---|---|
| BR-01 | Bệnh nhân phải có tài khoản để tự đặt lịch khám. | Ràng buộc | UC-004 | REQ-06 | P04 UC-004 | Hiệu lực |
| BR-02 | Mỗi bệnh nhân không được có quá 2 lịch hẹn chưa diễn ra cùng lúc. | Ràng buộc | UC-004 | REQ-12 | P04 UC-004 | Hiệu lực |
| BR-03 | Lịch hẹn do bệnh nhân tự đặt có trạng thái ban đầu "Chờ xác nhận". | Kích hoạt hành động | UC-004 | REQ-13 | P04 UC-004 | Hiệu lực |
| BR-04 | Bệnh nhân bị đánh dấu "Không đến" 3 lần trong 6 tháng bị khoá chức năng tự đặt lịch trực tuyến. | Suy luận | UC-004 | REQ-30 | P04 UC-004 | Hiệu lực |
| BR-05 | Lịch hẹn do lễ tân đặt có trạng thái ban đầu "Đã xác nhận". | Kích hoạt hành động | UC-005 | REQ-25 | P04 UC-005 | Hiệu lực |
| BR-06 | Lúc 18 giờ mỗi ngày, mỗi lịch hẹn ở trạng thái "Đã xác nhận" có ngày khám là ngày hôm sau được nhắc lịch bằng SMS. | Kích hoạt hành động | UC-008 | REQ-26 | P04 UC-008 | Hiệu lực |
| BR-07 | Lịch trống của bác sĩ được xem trong phạm vi 14 ngày tới. | Ràng buộc | Chưa gắn UC | REQ-05 | P06 | Hiệu lực |
| BR-08 | Mỗi khung giờ dài 30 phút. | Sự kiện | Chưa gắn UC | REQ-11 | P06 | Hiệu lực |
| BR-09 | Lễ tân phải ghi lý do khi từ chối lịch hẹn. | Ràng buộc | Chưa gắn UC | REQ-17 | P06 | Hiệu lực |
| BR-10 | Bệnh nhân chỉ được tự hủy lịch hẹn khi còn ít nhất 4 tiếng trước giờ khám. | Ràng buộc | Chưa gắn UC | REQ-20 | P06 | Hiệu lực |
| BR-11 | Lịch hẹn chỉ được đánh dấu "Không đến" khi đã quá giờ hẹn 30 phút mà bệnh nhân chưa đến. | Ràng buộc | Chưa gắn UC | REQ-29 | P06 | Hiệu lực |
| BR-12 | Khi bác sĩ ghi kết luận khám, lịch hẹn chuyển sang trạng thái "Đã khám". | Kích hoạt hành động | Chưa gắn UC | REQ-34 | P06 | Hiệu lực |
