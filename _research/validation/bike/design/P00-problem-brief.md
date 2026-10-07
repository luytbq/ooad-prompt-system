# P00 - Chuẩn hoá yêu cầu - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P00 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-dap.md |
| Phạm vi | Toàn hệ thống |

## 1. Bối cảnh và mục tiêu nghiệp vụ

Công ty CityBike vận hành khoảng 60 trạm xe đạp công cộng trong nội thành, mỗi trạm có từ 10 đến 20 ụ khoá. Mỗi ụ khoá có đầu đọc mã QR và khoá điện, kết nối về máy chủ trung tâm. Công ty cần phần mềm quản lý việc thuê và trả xe, phục vụ người dùng thuê xe qua ứng dụng di động và các nhóm nhân viên vận hành (bảo trì, điều phối, chăm sóc khách hàng, quản trị) cùng ban giám đốc.

Mục tiêu nghiệp vụ:
- Quản lý việc thuê và trả xe tại các trạm (nguồn: "Công ty cần phần mềm quản lý việc thuê và trả xe", đoạn mở đầu).

## 2. Phạm vi

Trong phạm vi:
- Đăng ký tài khoản và liên kết thẻ thanh toán (REQ-02, REQ-03, REQ-04).
- Xem bản đồ trạm (REQ-05, REQ-06).
- Thuê xe, trả xe, tính và thu cước (REQ-07 đến REQ-24).
- Thêm thời gian miễn phí khi trạm đến đầy (REQ-25 đến REQ-27).
- Xử lý chuyến đi quá thời hạn tối đa (REQ-28 đến REQ-32).
- Báo xe hỏng và xử lý xe chờ kiểm tra (REQ-33 đến REQ-40).
- Điều chuyển xe giữa các trạm (REQ-41 đến REQ-46).
- Chăm sóc khách hàng: tra cứu chuyến, điều chỉnh cước, mở khoá tài khoản (REQ-47 đến REQ-50).
- Quản trị danh mục trạm, ụ khoá, xe, tài khoản nhân viên, bảng giá cước (REQ-51 đến REQ-55).
- Báo cáo hằng tuần (REQ-56, REQ-57).

Ngoài phạm vi:
- Cổng thanh toán của ngân hàng đối tác: hệ thống khác, hệ thống này chỉ gọi API (REQ-62, "Cổng thanh toán của ngân hàng đối tác cung cấp API...", Mục 14).
- Phần cứng và phần mềm nhúng của ụ khoá: do nhà cung cấp thiết bị quy định giao thức, hệ thống này chỉ trao đổi qua MQTT (REQ-63, Mục 14).

Chờ Q-nn: Không có.

## 3. Các bên liên quan và người dùng

| SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống (Có / Không / Chưa rõ) | REQ |
|---|---|---|---|---|---|
| SH-01 | Công ty CityBike | Chủ sở hữu, người đặt hàng | Quản lý việc thuê và trả xe tại các trạm | Không | Đoạn mở đầu |
| SH-02 | Ụ khoá (đầu đọc mã QR, khoá điện) | Hệ thống hoặc thiết bị ngoài | Nhận lệnh mở khoá, báo xe được rút ra hoặc đưa vào | Có | REQ-12, REQ-13, REQ-18, REQ-46, REQ-63 |
| SH-03 | Người dùng (người thuê xe) | Người dùng trực tiếp | Thuê, trả xe thuận tiện; cước đúng | Có | REQ-01 đến REQ-33 |
| SH-04 | Cổng thanh toán của ngân hàng đối tác | Hệ thống hoặc thiết bị ngoài | Tạm giữ, thu, huỷ tạm giữ, hoàn tiền | Có | REQ-03, REQ-10, REQ-62 |
| SH-05 | Nhân viên chăm sóc khách hàng | Người vận hành, quản trị | Xử lý chuyến thất lạc, điều chỉnh cước, mở khoá tài khoản | Có | REQ-32, REQ-47 đến REQ-50 |
| SH-06 | Nhân viên bảo trì | Người vận hành, quản trị | Kiểm tra, sửa chữa xe bị báo hỏng | Có | REQ-38 đến REQ-40 |
| SH-07 | Nhân viên điều phối | Người vận hành, quản trị | Cân bằng số xe giữa các trạm | Có | REQ-41 đến REQ-45 |
| SH-08 | Nhân viên lấy, đưa xe bằng thẻ nhân viên | Người vận hành, quản trị | Thực hiện điều chuyển xe tại trạm | Chưa rõ (Q-07) | REQ-46 |
| SH-09 | Quản trị viên | Người vận hành, quản trị | Duy trì danh mục trạm, ụ khoá, xe, tài khoản nhân viên, bảng giá cước | Có | REQ-51 đến REQ-55 |
| SH-10 | Ban giám đốc | Chủ sở hữu, người đặt hàng | Theo dõi số chuyến, thời lượng, doanh thu, xe hỏng | Có | REQ-56, REQ-57 |
| SH-11 | Nhà cung cấp thiết bị ụ khoá | Hệ thống hoặc thiết bị ngoài | Quy định giao thức MQTT của ụ khoá | Không | REQ-63 |

## 4. Danh sách yêu cầu

| REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |
|---|---|---|---|---|
| REQ-01 | Người dùng sử dụng hệ thống qua ứng dụng di động. | Ràng buộc | "Người dùng cài ứng dụng di động" (Mục 1) | Không có |
| REQ-02 | Người dùng có thể đăng ký tài khoản bằng email và số điện thoại. | Chức năng | "đăng ký tài khoản bằng email và số điện thoại" (Mục 1) | Không có |
| REQ-03 | Người dùng có thể liên kết một thẻ thanh toán với tài khoản qua cổng thanh toán của ngân hàng đối tác. | Chức năng | "liên kết một thẻ thanh toán qua cổng thanh toán của ngân hàng đối tác" (Mục 1) | Kênh: cổng thanh toán (REQ-62) |
| REQ-04 | Tài khoản chỉ được thuê xe sau khi đã liên kết một thẻ thanh toán. | Quy tắc nghiệp vụ | "Tài khoản chỉ được thuê xe sau khi liên kết một thẻ thanh toán" (Mục 1) | Tách từ cùng câu với REQ-03 |
| REQ-05 | Người dùng, kể cả khi chưa đăng nhập, có thể xem bản đồ các trạm kèm số xe sẵn sàng và số ụ trống của từng trạm. | Chức năng | "xem bản đồ các trạm, số xe sẵn sàng và số ụ trống ở từng trạm" (Mục 2)<br>"Việc xem bản đồ không cần đăng nhập" (Mục 2) | Q-01 |
| REQ-06 | Số xe sẵn sàng và số ụ trống trên bản đồ được cập nhật "theo thời gian thực". | Phi chức năng | "cập nhật theo thời gian thực" (Mục 2) | Q-12 |
| REQ-07 | Người dùng có thể thuê xe bằng cách dùng ứng dụng quét mã QR dán trên ụ khoá khi đứng tại trạm. | Chức năng | "người dùng đứng tại trạm, dùng ứng dụng quét mã QR dán trên ụ khoá" (Mục 3) | Không có |
| REQ-08 | Tài khoản chỉ được thuê xe khi không có chuyến đi đang diễn ra. | Quy tắc nghiệp vụ | "kiểm tra tài khoản không có chuyến đang diễn ra" (Mục 3) | Không có |
| REQ-09 | Tài khoản chỉ được thuê xe khi không nợ cước. | Quy tắc nghiệp vụ | "và không nợ cước" (Mục 3) | Q-02 |
| REQ-10 | Hệ thống tạm giữ tiền trên thẻ đã liên kết qua cổng thanh toán khi người dùng thuê xe. | Chức năng | "tạm giữ 200.000 đồng trên thẻ qua cổng thanh toán" (Mục 3) | Kênh: cổng thanh toán; Q-08 |
| REQ-11 | Số tiền tạm giữ cho mỗi lần thuê xe là 200.000 đồng. | Quy tắc nghiệp vụ | "tạm giữ 200.000 đồng" (Mục 3) | Tách từ cùng câu với REQ-10 |
| REQ-12 | Hệ thống gửi lệnh mở khoá tới ụ khoá sau khi tạm giữ tiền. | Chức năng | "rồi gửi lệnh mở khoá tới ụ" (Mục 3) | Kênh: ụ khoá (REQ-63) |
| REQ-13 | Hệ thống bắt đầu chuyến đi khi ụ khoá báo xe đã được rút ra. | Chức năng | "Chuyến đi bắt đầu khi ụ báo xe đã được rút ra" (Mục 3) | Không có |
| REQ-14 | Hệ thống khoá lại ụ khoá khi ụ không báo xe được rút ra trong thời hạn chờ rút xe. | Chức năng | "Nếu sau 60 giây ụ không báo xe được rút, hệ thống khoá lại ụ" (Mục 3) | Không có |
| REQ-15 | Hệ thống huỷ lệnh tạm giữ tiền khi ụ không báo xe được rút ra trong thời hạn chờ rút xe. | Chức năng | "và huỷ lệnh tạm giữ tiền" (Mục 3) | Tách từ cùng câu với REQ-14 |
| REQ-16 | Thời hạn chờ rút xe là 60 giây. | Quy tắc nghiệp vụ | "Nếu sau 60 giây ụ không báo xe được rút" (Mục 3) | Q-10 |
| REQ-17 | Người dùng có thể trả xe bằng cách đẩy xe vào một ụ trống bất kỳ ở bất kỳ trạm nào. | Chức năng | "trả xe bằng cách đẩy xe vào một ụ trống bất kỳ ở bất kỳ trạm nào" (Mục 4) | Không có |
| REQ-18 | Hệ thống nhận thông báo từ ụ khoá khi ụ tự nhận diện được xe vừa được đẩy vào. | Giao tiếp ngoài | "Ụ khoá tự nhận diện xe và báo về hệ thống" (Mục 4) | Không có |
| REQ-19 | Hệ thống kết thúc chuyến đi khi ụ khoá báo đã nhận xe. | Chức năng | "Hệ thống kết thúc chuyến" (Mục 4) | Q-04 |
| REQ-20 | Hệ thống tính cước chuyến đi khi kết thúc chuyến. | Chức năng | "tính cước" (Mục 4) | Không có |
| REQ-21 | Cước chuyến đi miễn phí 30 phút đầu, sau đó 5.000 đồng cho mỗi 15 phút hoặc phần lẻ của 15 phút. | Quy tắc nghiệp vụ | "miễn phí 30 phút đầu, sau đó 5.000 đồng cho mỗi 15 phút hoặc phần lẻ" (Mục 4) | Q-15 |
| REQ-22 | Hệ thống thu cước từ số tiền tạm giữ. | Chức năng | "thu cước từ số tiền tạm giữ" (Mục 4) | Kênh: cổng thanh toán (REQ-62); Q-02 |
| REQ-23 | Hệ thống hoàn lại cho người dùng phần tiền tạm giữ còn dư sau khi thu cước. | Chức năng | "hoàn lại phần dư" (Mục 4) | Không có |
| REQ-24 | Hệ thống gửi hoá đơn chuyến đi cho người dùng qua email. | Chức năng | "gửi hoá đơn qua email" (Mục 4) | Kênh: email |
| REQ-25 | Người dùng có thể yêu cầu thêm thời gian miễn phí để đi tới trạm khác khi trạm đến không còn ụ trống. | Chức năng | "Nếu trạm đến không còn ụ trống, người dùng có thể yêu cầu thêm 15 phút miễn phí để đi tới trạm khác" (Mục 5) | Q-05 |
| REQ-26 | Thời gian miễn phí cộng thêm cho một yêu cầu là 15 phút. | Quy tắc nghiệp vụ | "thêm 15 phút miễn phí" (Mục 5) | Tách từ cùng câu với REQ-25 |
| REQ-27 | Mỗi chuyến đi chỉ được yêu cầu thêm thời gian miễn phí một lần. | Quy tắc nghiệp vụ | "mỗi chuyến chỉ được yêu cầu một lần" (Mục 5) | Không có |
| REQ-28 | Hệ thống tự động coi xe là thất lạc khi chuyến đi kéo dài quá thời hạn tối đa của chuyến. | Chức năng | "Nếu chuyến đi kéo dài quá 24 giờ, hệ thống tự động coi xe là thất lạc" (Mục 6) | Q-04 |
| REQ-29 | Thời hạn tối đa của một chuyến đi là 24 giờ. | Quy tắc nghiệp vụ | "kéo dài quá 24 giờ" (Mục 6) | Tách từ cùng câu với REQ-28 |
| REQ-30 | Hệ thống thu toàn bộ số tiền tạm giữ khi xe bị coi là thất lạc. | Chức năng | "thu toàn bộ số tiền tạm giữ" (Mục 6) | Kênh: cổng thanh toán |
| REQ-31 | Hệ thống khoá tài khoản của người dùng khi xe bị coi là thất lạc. | Chức năng | "và khoá tài khoản" (Mục 6) | Không có |
| REQ-32 | Nhân viên chăm sóc khách hàng "xử lý tiếp" trường hợp xe bị coi là thất lạc. | Chức năng | "nhân viên chăm sóc khách hàng sẽ xử lý tiếp" (Mục 6) | Q-03 |
| REQ-33 | Người dùng có thể báo xe hỏng ngay khi trả xe hoặc trong thời hạn báo hỏng sau khi trả xe. | Chức năng | "Người dùng có thể báo xe hỏng ngay khi trả xe hoặc trong vòng 10 phút sau khi trả" (Mục 7) | Q-06 |
| REQ-34 | Thời hạn báo hỏng là 10 phút sau khi trả xe. | Quy tắc nghiệp vụ | "trong vòng 10 phút sau khi trả" (Mục 7) | Tách từ cùng câu với REQ-33 |
| REQ-35 | Báo hỏng gồm loại hỏng hóc (phanh, xích, lốp, khác) và mô tả. | Dữ liệu | "chọn loại hỏng hóc (phanh, xích, lốp, khác) và mô tả" (Mục 7) | Không có |
| REQ-36 | Hệ thống đánh dấu xe bị báo hỏng ở trạng thái "Chờ kiểm tra". | Chức năng | "Xe bị báo hỏng được đánh dấu 'Chờ kiểm tra'" (Mục 7) | Không có |
| REQ-37 | Xe ở trạng thái "Chờ kiểm tra" không được cho thuê. | Quy tắc nghiệp vụ | "và không cho thuê" (Mục 7) | Không có |
| REQ-38 | Nhân viên bảo trì có thể xem danh sách xe chờ kiểm tra theo trạm. | Chức năng | "Nhân viên bảo trì xem danh sách xe chờ kiểm tra theo trạm" (Mục 8) | Không có |
| REQ-39 | Nhân viên bảo trì có thể ghi nhận kết quả sửa chữa xe. | Chức năng | "ghi nhận kết quả sửa chữa" (Mục 8) | Không có |
| REQ-40 | Nhân viên bảo trì có thể chuyển xe về trạng thái sẵn sàng hoặc thu hồi xe về xưởng. | Chức năng | "chuyển xe về trạng thái sẵn sàng hoặc thu hồi về xưởng" (Mục 8) | Chưa tách vì hai kết quả là hai lựa chọn của cùng một quyết định sau kiểm tra; Q-18 |
| REQ-41 | Nhân viên điều phối có thể xem các trạm sắp hết xe hoặc sắp đầy. | Chức năng | "Nhân viên điều phối xem các trạm sắp hết xe ... hoặc sắp đầy" (Mục 9) | Không có |
| REQ-42 | Trạm sắp hết xe là trạm có dưới 20% số ụ có xe. | Quy tắc nghiệp vụ | "sắp hết xe (dưới 20% số ụ có xe)" (Mục 9) | Không có |
| REQ-43 | Trạm sắp đầy là trạm có "trên 90%" số ụ có xe. | Quy tắc nghiệp vụ | "hoặc sắp đầy (trên 90%)" (Mục 9) | Q-11 |
| REQ-44 | Nhân viên điều phối có thể lập lệnh điều chuyển xe giữa các trạm. | Chức năng | "lập lệnh điều chuyển xe giữa các trạm" (Mục 9) | Không có |
| REQ-45 | Nhân viên điều phối có thể theo dõi lệnh điều chuyển cho tới khi hoàn tất. | Chức năng | "theo dõi lệnh điều chuyển cho tới khi hoàn tất" (Mục 9) | Q-09 |
| REQ-46 | Hệ thống tự động cập nhật lệnh điều chuyển khi nhân viên lấy xe ra hoặc đưa xe vào ụ khoá bằng thẻ nhân viên. | Chức năng | "Khi nhân viên lấy xe ra hoặc đưa xe vào ụ bằng thẻ nhân viên, lệnh điều chuyển được cập nhật tự động" (Mục 9) | Q-07 |
| REQ-47 | Nhân viên chăm sóc khách hàng có thể tra cứu lịch sử chuyến đi của người dùng. | Chức năng | "tra cứu lịch sử chuyến đi của người dùng" (Mục 10) | Không có |
| REQ-48 | Nhân viên chăm sóc khách hàng có thể điều chỉnh cước bằng cách hoàn tiền một phần hoặc toàn bộ. | Chức năng | "điều chỉnh cước (hoàn tiền một phần hoặc toàn bộ ...)" (Mục 10) | Kênh: cổng thanh toán (REQ-62) |
| REQ-49 | Mỗi lần điều chỉnh cước phải ghi lý do. | Quy tắc nghiệp vụ | "phải ghi lý do" (Mục 10) | Tách từ cùng câu với REQ-48 |
| REQ-50 | Nhân viên chăm sóc khách hàng có thể mở khoá tài khoản người dùng. | Chức năng | "và mở khoá tài khoản" (Mục 10) | Không có |
| REQ-51 | Quản trị viên có thể quản lý trạm. | Chức năng | "Quản trị viên quản lý trạm" (Mục 11) | Chưa tách thao tác vì nguồn không phân biệt; Q-16 |
| REQ-52 | Quản trị viên có thể quản lý ụ khoá. | Chức năng | "quản lý ... ụ khoá" (Mục 11) | Chưa tách thao tác vì nguồn không phân biệt; Q-16 |
| REQ-53 | Quản trị viên có thể quản lý xe. | Chức năng | "quản lý ... xe" (Mục 11) | Chưa tách thao tác vì nguồn không phân biệt; Q-16 |
| REQ-54 | Quản trị viên có thể quản lý tài khoản nhân viên. | Chức năng | "quản lý ... tài khoản nhân viên" (Mục 11) | Chưa tách thao tác vì nguồn không phân biệt; Q-16 |
| REQ-55 | Quản trị viên có thể quản lý bảng giá cước. | Chức năng | "quản lý ... bảng giá cước" (Mục 11) | Q-15, Q-16 |
| REQ-56 | Ban giám đốc có thể xem báo cáo hằng tuần. | Chức năng | "Ban giám đốc xem báo cáo hằng tuần" (Mục 12) | Không có |
| REQ-57 | Báo cáo hằng tuần gồm số chuyến theo trạm, thời lượng trung bình, doanh thu, số xe hỏng. | Dữ liệu | "số chuyến theo trạm, thời lượng trung bình, doanh thu, số xe hỏng" (Mục 12) | Q-17 |
| REQ-58 | Lệnh mở khoá tới ụ khoá trong không quá 2 giây kể từ khi người dùng quét mã. | Phi chức năng | "Lệnh mở khoá phải tới ụ trong không quá 2 giây kể từ khi quét mã" (Mục 13) | Q-13 |
| REQ-59 | Hệ thống phục vụ được 1.500 chuyến đi đồng thời. | Phi chức năng | "Hệ thống phải phục vụ được 1.500 chuyến đi đồng thời" (Mục 13) | Q-14 |
| REQ-60 | Hệ thống không được lưu số thẻ thanh toán. | Phi chức năng | "Số thẻ thanh toán không được lưu trong hệ thống" (Mục 13) | Bảo mật |
| REQ-61 | Hệ thống chỉ lưu mã tham chiếu thẻ do cổng thanh toán cấp. | Dữ liệu | "chỉ lưu mã tham chiếu do cổng thanh toán cấp" (Mục 13) | Tách từ cùng câu với REQ-60 |
| REQ-62 | Hệ thống trao đổi với cổng thanh toán của ngân hàng đối tác qua API để tạm giữ tiền, thu tiền từ khoản tạm giữ, huỷ tạm giữ và hoàn tiền. | Giao tiếp ngoài | "cung cấp API tạm giữ tiền, thu tiền từ khoản tạm giữ, huỷ tạm giữ và hoàn tiền" (Mục 14) | Chưa tách vì cùng một giao diện ngoài |
| REQ-63 | Hệ thống giao tiếp với ụ khoá qua giao thức MQTT do nhà cung cấp thiết bị quy định. | Giao tiếp ngoài | "Ụ khoá giao tiếp với máy chủ qua giao thức MQTT do nhà cung cấp thiết bị quy định" (Mục 14) | Không có |

## 5. Vấn đề chất lượng của tài liệu nguồn

| STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
|---|---|---|---|---|---|
| 1 | Thiếu | REQ-05 | "Việc xem bản đồ không cần đăng nhập" (Mục 2) | Nguồn ngụ ý có đăng nhập cho các chức năng khác nhưng không mô tả | Q-01 |
| 2 | Thiếu | REQ-09, REQ-22 | "không nợ cước" (Mục 3); "thu cước từ số tiền tạm giữ" (Mục 4) | Nguồn nhắc nợ cước nhưng không nói nợ phát sinh khi nào (ví dụ cước vượt 200.000 đồng) và trả nợ thế nào | Q-02 |
| 3 | Mơ hồ | REQ-32 | "nhân viên chăm sóc khách hàng sẽ xử lý tiếp" (Mục 6) | Không rõ "xử lý tiếp" gồm việc gì trong hệ thống | Q-03 |
| 4 | Thiếu | REQ-19, REQ-28 | "hệ thống tự động coi xe là thất lạc" (Mục 6) | Không rõ chuyến có kết thúc không, và xử lý thế nào khi xe thất lạc được trả vào ụ | Q-04 |
| 5 | Thiếu | REQ-25 | "Nếu trạm đến không còn ụ trống" (Mục 5) | Không rõ hệ thống xác định trạm đến và tình trạng không còn ụ trống thế nào | Q-05 |
| 6 | Mơ hồ | REQ-33 | "báo xe hỏng ngay khi trả xe" (Mục 7) | Trả xe là thao tác đẩy xe vào ụ; không rõ báo hỏng qua kênh nào | Q-06 |
| 7 | Mơ hồ | REQ-46 | "nhân viên lấy xe ra hoặc đưa xe vào ụ bằng thẻ nhân viên" (Mục 9) | "Nhân viên" không rõ vai trò; nguồn chỉ nêu ụ có đầu đọc mã QR | Q-07 |
| 8 | Thiếu | REQ-10 | "tạm giữ 200.000 đồng trên thẻ qua cổng thanh toán" (Mục 3) | Không nói khi tạm giữ thất bại thì xử lý thế nào | Q-08 |
| 9 | Mơ hồ | REQ-45 | "cho tới khi hoàn tất" (Mục 9) | Không rõ điều kiện lệnh điều chuyển hoàn tất | Q-09 |
| 10 | Mơ hồ | REQ-16 | "Nếu sau 60 giây" (Mục 3) | Không rõ mốc bắt đầu tính 60 giây | Q-10 |
| 11 | Mơ hồ | REQ-43 | "sắp đầy (trên 90%)" (Mục 9) | Không nêu 90% của đại lượng nào | Q-11 |
| 12 | Không kiểm chứng được | REQ-06 | "cập nhật theo thời gian thực" (Mục 2) | Không có ngưỡng độ trễ | Q-12 |
| 13 | Không khả thi | REQ-58 | "không quá 2 giây kể từ khi quét mã" (Mục 13) | Khoảng 2 giây bao gồm bước tạm giữ tiền qua cổng thanh toán ngoài (REQ-10), thời gian của cổng không do hệ thống kiểm soát | Q-13 |
| 14 | Không kiểm chứng được | REQ-59 | "phục vụ được 1.500 chuyến đi đồng thời" (Mục 13) | Không nêu tiêu chí "phục vụ được" | Q-14 |
| 15 | Mơ hồ | REQ-21, REQ-55 | "5.000 đồng cho mỗi 15 phút" (Mục 4); "quản lý ... bảng giá cước" (Mục 11) | Không rõ mức cước ở Mục 4 có thay đổi được qua bảng giá cước không | Q-15 |
| 16 | Mơ hồ | REQ-51 đến REQ-55 | "Quản trị viên quản lý trạm, ụ khoá, xe, tài khoản nhân viên và bảng giá cước" (Mục 11) | "Quản lý" không nêu thao tác | Q-16 |
| 17 | Mơ hồ | REQ-57 | "số chuyến theo trạm ... doanh thu" (Mục 12) | Không rõ trạm tính theo trạm thuê hay trạm trả; doanh thu tính gồm khoản nào | Q-17 |
| 18 | Thiếu | REQ-40 | "thu hồi về xưởng" (Mục 8) | Không nói xe thu hồi về xưởng quay lại hoạt động thế nào | Q-18 |

## 6. Ma trận phủ nguồn

| Vị trí trong nguồn | Tóm tắt nội dung | Kết luận |
|---|---|---|
| Đoạn mở đầu, câu 1 | Khoảng 60 trạm, mỗi trạm 10-20 ụ khoá | Bối cảnh |
| Đoạn mở đầu, câu 2 | Ụ khoá có đầu đọc QR, khoá điện, kết nối máy chủ | Bối cảnh (chi tiết giao tiếp ở REQ-18, REQ-63) |
| Đoạn mở đầu, câu 3 | Cần phần mềm quản lý thuê và trả xe | Bối cảnh, mục tiêu nghiệp vụ |
| Mục 1 | Ứng dụng di động, đăng ký, liên kết thẻ, điều kiện thuê | REQ-01, REQ-02, REQ-03, REQ-04 |
| Mục 2 | Xem bản đồ, thời gian thực, không cần đăng nhập | REQ-05, REQ-06 |
| Mục 3 | Thuê xe, kiểm tra, tạm giữ, mở khoá, bắt đầu chuyến, hết 60 giây | REQ-07 đến REQ-16 |
| Mục 4 | Trả xe, kết thúc chuyến, tính cước, thu, hoàn, hoá đơn | REQ-17 đến REQ-24 |
| Mục 5 | Thêm 15 phút miễn phí | REQ-25, REQ-26, REQ-27 |
| Mục 6 | Chuyến quá 24 giờ | REQ-28 đến REQ-32 |
| Mục 7 | Báo xe hỏng | REQ-33 đến REQ-37 |
| Mục 8 | Nhân viên bảo trì | REQ-38, REQ-39, REQ-40 |
| Mục 9 | Nhân viên điều phối, lệnh điều chuyển | REQ-41 đến REQ-46 |
| Mục 10 | Chăm sóc khách hàng | REQ-47 đến REQ-50 |
| Mục 11 | Quản trị viên | REQ-51 đến REQ-55 |
| Mục 12 | Báo cáo hằng tuần | REQ-56, REQ-57 |
| Mục 13 | 2 giây, 1.500 chuyến, không lưu số thẻ | REQ-58 đến REQ-61 |
| Mục 14 | API cổng thanh toán, MQTT | REQ-62, REQ-63 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-01 | Người dùng và nhân viên có phải đăng nhập để dùng các chức năng ngoài xem bản đồ không, và đăng nhập có thuộc phạm vi phân tích không? (Có / Không) | REQ-05, danh sách use case (P02) | "Việc xem bản đồ không cần đăng nhập" (Mục 2) |
| Q-02 | Nợ cước phát sinh khi nào (ví dụ cước vượt 200.000 đồng tạm giữ) và người dùng trả nợ bằng cách nào? (a) Hệ thống tự thu thêm từ thẻ qua cổng thanh toán; (b) Người dùng tự thanh toán nợ trong ứng dụng; (c) Chỉ nhân viên chăm sóc khách hàng xử lý | REQ-09, REQ-22, danh sách use case | "không nợ cước" (Mục 3) |
| Q-03 | "Xử lý tiếp" của nhân viên chăm sóc khách hàng với xe thất lạc gồm: (a) chỉ các chức năng ở Mục 10; (b) thêm chức năng riêng (ví dụ ghi nhận thu hồi xe, đóng vụ việc)? | REQ-32, danh sách use case | "sẽ xử lý tiếp" (Mục 6) |
| Q-04 | Khi xe bị coi là thất lạc, chuyến đi có kết thúc không, và nếu sau đó xe được đẩy vào ụ thì hệ thống có kết thúc chuyến và tính cước như thường không? (Có / Không) | REQ-19, REQ-28, luồng ngoại lệ UC trả xe | Mục 6 |
| Q-05 | Hệ thống xác định "trạm đến không còn ụ trống" thế nào: (a) người dùng chọn trạm đến trong ứng dụng và hệ thống kiểm tra số ụ trống; (b) người dùng tự khai báo? 15 phút được cộng vào thời gian miễn phí của chuyến? (Có / Không) | REQ-25, REQ-26, REQ-21 | Mục 5 |
| Q-06 | Người dùng báo xe hỏng qua ứng dụng sau khi ụ ghi nhận xe đã trả? (Có / Không) | REQ-33 | "ngay khi trả xe" (Mục 7) |
| Q-07 | Người lấy xe ra, đưa xe vào ụ bằng thẻ nhân viên là nhân viên điều phối hay vai trò khác, và ụ đọc thẻ nhân viên bằng thiết bị nào? | REQ-46, tác nhân (P01) | Mục 9 |
| Q-08 | Khi tạm giữ tiền qua cổng thanh toán thất bại, hệ thống từ chối thuê và báo lỗi cho người dùng? (Có / Không) | REQ-10, luồng ngoại lệ UC thuê xe | Mục 3 |
| Q-09 | Lệnh điều chuyển hoàn tất khi đủ số xe đã được đưa vào các ụ ở trạm đích? (Có / Không) | REQ-45 | "cho tới khi hoàn tất" (Mục 9) |
| Q-10 | 60 giây được tính từ lúc hệ thống gửi lệnh mở khoá? (Có / Không) | REQ-16 | Mục 3 |
| Q-11 | "Trên 90%" là tỉ lệ số ụ có xe trên tổng số ụ của trạm? (Có / Không) | REQ-43 | Mục 9 |
| Q-12 | "Thời gian thực" của bản đồ là độ trễ tối đa bao nhiêu giây? | REQ-06 | Mục 2 |
| Q-13 | Ngưỡng 2 giây có bao gồm thời gian cổng thanh toán xử lý tạm giữ tiền không? (Có / Không) | REQ-58, REQ-10 | Mục 13 |
| Q-14 | "Phục vụ được 1.500 chuyến đi đồng thời" đo bằng tiêu chí nào (ví dụ vẫn đạt REQ-58 khi có 1.500 chuyến đang diễn ra)? | REQ-59 | Mục 13 |
| Q-15 | Mức cước ở Mục 4 có thay đổi được qua bảng giá cước do quản trị viên quản lý không? (Có / Không) | REQ-21, REQ-55 | Mục 4, Mục 11 |
| Q-16 | "Quản lý" trạm, ụ khoá, xe, tài khoản nhân viên, bảng giá cước gồm các thao tác nào (thêm, sửa, xoá, xem, khoá)? | REQ-51 đến REQ-55 | Mục 11 |
| Q-17 | Số chuyến theo trạm tính theo trạm thuê hay trạm trả, và doanh thu có trừ các khoản hoàn tiền không? | REQ-57 | Mục 12 |
| Q-18 | Xe thu hồi về xưởng quay lại trạng thái sẵn sàng bằng cách nào và do ai cập nhật? | REQ-40 | Mục 8 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Mục tiêu nghiệp vụ chỉ có một dòng vì nguồn không nêu mục tiêu nào khác; không tự thêm.
- Số REQ (63) vượt mức tham khảo 15-40 của F2 cho tài liệu nguồn một trang. Nguyên nhân: nguồn dày đặc ngưỡng định lượng và quy tắc F2 số 5 buộc tách mọi ngưỡng thành REQ Quy tắc nghiệp vụ.
