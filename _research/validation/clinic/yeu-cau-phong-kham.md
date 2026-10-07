# Mô tả yêu cầu: Hệ thống đặt lịch khám ClinicBook

Phòng khám đa khoa tư nhân Minh An có 3 chuyên khoa (Nội, Nhi, Da liễu) với khoảng 12 bác sĩ. Hiện nay bệnh nhân đặt lịch qua điện thoại, lễ tân ghi sổ, thường xuyên trùng lịch và bệnh nhân không đến mà không báo. Phòng khám cần một phần mềm web để quản lý việc đặt lịch khám.

1. Bệnh nhân có thể xem danh sách chuyên khoa, danh sách bác sĩ theo chuyên khoa và lịch trống của từng bác sĩ trong 14 ngày tới mà không cần đăng nhập.
2. Để đặt lịch, bệnh nhân phải có tài khoản. Bệnh nhân tự đăng ký tài khoản bằng số điện thoại; hệ thống gửi mã OTP qua SMS để xác thực số điện thoại.
3. Khi đặt lịch, bệnh nhân chọn chuyên khoa, bác sĩ (hoặc để phòng khám tự phân bác sĩ), ngày và khung giờ 30 phút còn trống, nhập lý do khám. Mỗi bệnh nhân không được có quá 2 lịch hẹn chưa diễn ra cùng lúc.
4. Lịch hẹn vừa đặt ở trạng thái "Chờ xác nhận". Lễ tân xem các lịch chờ và xác nhận hoặc từ chối (phải ghi lý do từ chối). Khi lịch được xác nhận hoặc bị từ chối, hệ thống gửi SMS thông báo cho bệnh nhân.
5. Bệnh nhân có thể hủy lịch hẹn của mình trước giờ khám ít nhất 4 tiếng. Sau thời điểm đó chỉ lễ tân mới hủy được.
6. Nhiều người lớn tuổi vẫn gọi điện thoại. Lễ tân có thể đặt lịch thay cho bệnh nhân gọi điện; nếu bệnh nhân chưa có tài khoản, lễ tân tạo hồ sơ bệnh nhân với họ tên, ngày sinh, số điện thoại. Lịch do lễ tân đặt được xác nhận ngay.
7. Vào 18 giờ mỗi ngày, hệ thống tự động gửi SMS nhắc lịch cho các bệnh nhân có lịch hẹn đã xác nhận vào ngày hôm sau.
8. Khi bệnh nhân đến phòng khám, lễ tân ghi nhận bệnh nhân đã đến (check-in). Nếu quá giờ hẹn 30 phút mà bệnh nhân không đến, lễ tân đánh dấu "Không đến". Bệnh nhân bị đánh dấu "Không đến" 3 lần trong 6 tháng sẽ bị khoá chức năng tự đặt lịch trực tuyến.
9. Bác sĩ xem danh sách lịch hẹn của mình theo ngày. Sau khi khám, bác sĩ ghi kết luận khám ngắn (chẩn đoán, lời dặn) vào lịch hẹn; lịch hẹn chuyển sang "Đã khám".
10. Bác sĩ đăng ký lịch làm việc theo tuần (các buổi sáng/chiều trong tuần). Bác sĩ có thể khoá một số khung giờ đột xuất; nếu khung giờ đó đã có lịch hẹn, hệ thống báo cho lễ tân để liên hệ bệnh nhân đổi lịch.
11. Quản trị viên quản lý chuyên khoa, tài khoản bác sĩ và lễ tân, và cấu hình các tham số (số giờ tối thiểu được hủy, số lần không đến tối đa).
12. Quản lý phòng khám xem báo cáo hàng tháng: số lịch hẹn theo chuyên khoa, theo bác sĩ, tỷ lệ không đến.
13. Hệ thống phải phản hồi thao tác đặt lịch trong không quá 3 giây với 200 người dùng đồng thời. Giao diện phải dùng được trên điện thoại. Dữ liệu kết luận khám chỉ bác sĩ khám và chính bệnh nhân được xem.
14. Việc gửi SMS dùng dịch vụ SMS Gateway của nhà mạng qua API có sẵn.
