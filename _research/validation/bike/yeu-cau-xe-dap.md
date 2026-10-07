# Mô tả yêu cầu: Hệ thống cho thuê xe đạp công cộng CityBike

Công ty CityBike vận hành khoảng 60 trạm xe đạp công cộng trong nội thành, mỗi trạm có từ 10 đến 20 ụ khoá (dock). Mỗi ụ khoá có đầu đọc mã QR và khoá điện, kết nối về máy chủ trung tâm. Công ty cần phần mềm quản lý việc thuê và trả xe.

1. Người dùng cài ứng dụng di động, đăng ký tài khoản bằng email và số điện thoại. Tài khoản chỉ được thuê xe sau khi liên kết một thẻ thanh toán qua cổng thanh toán của ngân hàng đối tác.
2. Người dùng xem bản đồ các trạm, số xe sẵn sàng và số ụ trống ở từng trạm, cập nhật theo thời gian thực. Việc xem bản đồ không cần đăng nhập.
3. Để thuê xe, người dùng đứng tại trạm, dùng ứng dụng quét mã QR dán trên ụ khoá. Hệ thống kiểm tra tài khoản không có chuyến đang diễn ra và không nợ cước, tạm giữ 200.000 đồng trên thẻ qua cổng thanh toán, rồi gửi lệnh mở khoá tới ụ. Chuyến đi bắt đầu khi ụ báo xe đã được rút ra. Nếu sau 60 giây ụ không báo xe được rút, hệ thống khoá lại ụ và huỷ lệnh tạm giữ tiền.
4. Người dùng trả xe bằng cách đẩy xe vào một ụ trống bất kỳ ở bất kỳ trạm nào. Ụ khoá tự nhận diện xe và báo về hệ thống. Hệ thống kết thúc chuyến, tính cước (miễn phí 30 phút đầu, sau đó 5.000 đồng cho mỗi 15 phút hoặc phần lẻ), thu cước từ số tiền tạm giữ, hoàn lại phần dư và gửi hoá đơn qua email.
5. Nếu trạm đến không còn ụ trống, người dùng có thể yêu cầu thêm 15 phút miễn phí để đi tới trạm khác; mỗi chuyến chỉ được yêu cầu một lần.
6. Nếu chuyến đi kéo dài quá 24 giờ, hệ thống tự động coi xe là thất lạc, thu toàn bộ số tiền tạm giữ và khoá tài khoản; nhân viên chăm sóc khách hàng sẽ xử lý tiếp.
7. Người dùng có thể báo xe hỏng ngay khi trả xe hoặc trong vòng 10 phút sau khi trả, chọn loại hỏng hóc (phanh, xích, lốp, khác) và mô tả. Xe bị báo hỏng được đánh dấu "Chờ kiểm tra" và không cho thuê.
8. Nhân viên bảo trì xem danh sách xe chờ kiểm tra theo trạm, ghi nhận kết quả sửa chữa, và chuyển xe về trạng thái sẵn sàng hoặc thu hồi về xưởng.
9. Nhân viên điều phối xem các trạm sắp hết xe (dưới 20% số ụ có xe) hoặc sắp đầy (trên 90%), lập lệnh điều chuyển xe giữa các trạm và theo dõi lệnh điều chuyển cho tới khi hoàn tất. Khi nhân viên lấy xe ra hoặc đưa xe vào ụ bằng thẻ nhân viên, lệnh điều chuyển được cập nhật tự động.
10. Nhân viên chăm sóc khách hàng tra cứu lịch sử chuyến đi của người dùng, điều chỉnh cước (hoàn tiền một phần hoặc toàn bộ, phải ghi lý do) và mở khoá tài khoản.
11. Quản trị viên quản lý trạm, ụ khoá, xe, tài khoản nhân viên và bảng giá cước.
12. Ban giám đốc xem báo cáo hằng tuần: số chuyến theo trạm, thời lượng trung bình, doanh thu, số xe hỏng.
13. Lệnh mở khoá phải tới ụ trong không quá 2 giây kể từ khi quét mã. Hệ thống phải phục vụ được 1.500 chuyến đi đồng thời. Số thẻ thanh toán không được lưu trong hệ thống, chỉ lưu mã tham chiếu do cổng thanh toán cấp.
14. Cổng thanh toán của ngân hàng đối tác cung cấp API tạm giữ tiền, thu tiền từ khoản tạm giữ, huỷ tạm giữ và hoàn tiền. Ụ khoá giao tiếp với máy chủ qua giao thức MQTT do nhà cung cấp thiết bị quy định.
