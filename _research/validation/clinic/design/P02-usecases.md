# P02 - Xác định use case - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, P00-problem-brief.md 1.0, P01-actors.md 1.0, yeu-cau-phong-kham.md |
| Phạm vi | Toàn hệ thống |

## 1. Danh sách mục tiêu tác nhân

| ACT | Mục tiêu | Mức mục tiêu dự kiến (Summary / User-goal / Subfunction) | REQ | CAND |
|---|---|---|---|---|
| ACT-01 Bệnh nhân | Tìm bác sĩ còn lịch trống trước khi quyết định đặt | User-goal | REQ-02, REQ-03, REQ-04, REQ-05 | CAND-01 |
| ACT-01 | Có tài khoản để đặt lịch trực tuyến | User-goal | REQ-06, REQ-07, REQ-08 | CAND-02 |
| ACT-01 | Đăng nhập để dùng chức năng cần tài khoản | Subfunction | REQ-06, REQ-02 | CAND-03 |
| ACT-01 | Đặt được lịch khám với bác sĩ và khung giờ mong muốn | User-goal | REQ-09 đến REQ-13 | CAND-04 |
| ACT-01 | Hủy lịch hẹn không thể đến | User-goal | REQ-19, REQ-20 | CAND-05 |
| ACT-01 | Xem kết luận khám của mình | User-goal | REQ-45 | CAND-06 |
| ACT-02 Lễ tân | Xác nhận hoặc từ chối các lịch hẹn chờ | User-goal | REQ-14 đến REQ-18 | CAND-07 |
| ACT-02 | Đặt lịch cho bệnh nhân gọi điện | User-goal | REQ-22 đến REQ-25 | CAND-08 |
| ACT-02 | Hủy lịch hẹn cho bệnh nhân khi đã sát giờ khám | User-goal | REQ-21 | CAND-09 |
| ACT-02 | Ghi nhận bệnh nhân đã đến | User-goal | REQ-27 | CAND-10 |
| ACT-02 | Ghi nhận bệnh nhân không đến | User-goal | REQ-28, REQ-29, REQ-30 | CAND-11 |
| ACT-02 | Biết các lịch hẹn bị ảnh hưởng khi bác sĩ khoá khung giờ | User-goal | REQ-37 | CAND-12 |
| ACT-02 | Điều phối lịch khám của phòng khám | Summary | REQ-14 đến REQ-30 | CAND-13 |
| ACT-03 Bác sĩ | Nắm danh sách bệnh nhân hẹn khám trong ngày | User-goal | REQ-31 | CAND-14 |
| ACT-03 | Ghi kết luận sau khi khám | User-goal | REQ-32, REQ-33, REQ-34 | CAND-15 |
| ACT-03 | Đăng ký các buổi làm việc trong tuần | User-goal | REQ-35 | CAND-16 |
| ACT-03 | Khoá khung giờ khi có việc đột xuất | User-goal | REQ-36, REQ-37 | CAND-17 |
| ACT-04 Quản trị viên | Duy trì danh mục chuyên khoa | User-goal | REQ-38 | CAND-18 |
| ACT-04 | Duy trì tài khoản bác sĩ và lễ tân | User-goal | REQ-39, REQ-40 | CAND-19 |
| ACT-04 | Điều chỉnh tham số hủy lịch và không đến | User-goal | REQ-41 | CAND-20 |
| ACT-05 Quản lý phòng khám | Xem số liệu lịch hẹn hằng tháng | User-goal | REQ-42 | CAND-21 |
| ACT-07 Bộ định thời | Nhắc bệnh nhân lịch khám ngày hôm sau | User-goal | REQ-26 | CAND-22 |

## 2. Danh sách sự kiện

| EV | Sự kiện | Loại (Nghiệp vụ / Thời gian / Hệ thống ngoài) | Nguồn phát (ACT) | Phản hồi mong đợi của hệ thống | REQ | CAND |
|---|---|---|---|---|---|---|
| EV-01 | Bệnh nhân muốn biết bác sĩ nào còn lịch trống | Nghiệp vụ | ACT-01 | Hiển thị chuyên khoa, bác sĩ, lịch trống 14 ngày tới | REQ-02 đến REQ-05 | CAND-01 |
| EV-02 | Người chưa có tài khoản muốn đặt lịch trực tuyến | Nghiệp vụ | ACT-01 | Tạo tài khoản sau khi xác thực số điện thoại | REQ-07, REQ-08 | CAND-02 |
| EV-03 | Bệnh nhân muốn đặt lịch khám | Nghiệp vụ | ACT-01 | Tạo lịch hẹn "Chờ xác nhận" | REQ-09 đến REQ-13 | CAND-04 |
| EV-04 | Bệnh nhân không thể đến theo lịch hẹn | Nghiệp vụ | ACT-01 | Hủy lịch hẹn, giải phóng khung giờ | REQ-19, REQ-20 | CAND-05 |
| EV-05 | Bệnh nhân muốn xem kết luận khám | Nghiệp vụ | ACT-01 | Hiển thị kết luận khám của chính bệnh nhân | REQ-45 | CAND-06 |
| EV-06 | Có lịch hẹn mới ở trạng thái "Chờ xác nhận" | Nghiệp vụ | ACT-02 | Ghi nhận xác nhận hoặc từ chối, gửi SMS | REQ-14 đến REQ-18 | CAND-07 |
| EV-07 | Bệnh nhân gọi điện tới phòng khám để đặt lịch | Nghiệp vụ | ACT-02 | Tạo lịch hẹn đã xác nhận, tạo hồ sơ nếu cần | REQ-22 đến REQ-25 | CAND-08 |
| EV-08 | Bệnh nhân báo hủy lịch khi còn dưới 4 tiếng tới giờ khám | Nghiệp vụ | ACT-02 | Hủy lịch hẹn | REQ-21 | CAND-09 |
| EV-09 | Bệnh nhân tới phòng khám | Nghiệp vụ | ACT-02 | Ghi nhận bệnh nhân đã đến | REQ-27 | CAND-10 |
| EV-10 | Quá giờ hẹn 30 phút mà bệnh nhân chưa đến | Nghiệp vụ | ACT-02 | Đánh dấu "Không đến", khoá tự đặt lịch nếu đủ 3 lần trong 6 tháng | REQ-28, REQ-29, REQ-30 | CAND-11 |
| EV-11 | Bác sĩ cần biết lịch khám trong ngày | Nghiệp vụ | ACT-03 | Hiển thị lịch hẹn theo ngày | REQ-31 | CAND-14 |
| EV-12 | Bác sĩ khám xong một bệnh nhân | Nghiệp vụ | ACT-03 | Lưu kết luận, chuyển lịch hẹn sang "Đã khám" | REQ-32, REQ-33, REQ-34 | CAND-15 |
| EV-13 | Bác sĩ cần đăng ký lịch làm việc cho tuần | Nghiệp vụ | ACT-03 | Ghi nhận các buổi làm việc | REQ-35 | CAND-16 |
| EV-14 | Bác sĩ có việc đột xuất | Nghiệp vụ | ACT-03 | Khoá khung giờ, báo lễ tân nếu đã có lịch hẹn | REQ-36, REQ-37 | CAND-17 |
| EV-15 | Phòng khám thay đổi chuyên khoa | Nghiệp vụ | ACT-04 | Cập nhật danh mục chuyên khoa | REQ-38 | CAND-18 |
| EV-16 | Phòng khám có bác sĩ hoặc lễ tân mới, hoặc thay đổi nhân sự | Nghiệp vụ | ACT-04 | Cập nhật tài khoản nhân viên | REQ-39, REQ-40 | CAND-19 |
| EV-17 | Phòng khám thay đổi quy định hủy lịch hoặc không đến | Nghiệp vụ | ACT-04 | Cập nhật tham số | REQ-41 | CAND-20 |
| EV-18 | Quản lý cần số liệu lịch hẹn của tháng | Nghiệp vụ | ACT-05 | Hiển thị báo cáo tháng | REQ-42 | CAND-21 |
| EV-19 | Đến 18 giờ mỗi ngày | Thời gian | ACT-07 | Gửi SMS nhắc lịch cho lịch hẹn đã xác nhận của ngày hôm sau | REQ-26 | CAND-22 |

## 3. Bảng ứng viên use case

| CAND | Ứng viên | Kết luận | Phép thử không đạt | Lý do | REQ | Nguồn phát hiện |
|---|---|---|---|---|---|---|
| CAND-01 | Tra cứu lịch trống của bác sĩ | Giữ thành UC-001 | - | Mục tiêu thông tin độc lập, không cần đăng nhập (U-R05) | REQ-02 đến REQ-05 | Mục tiêu, EV-01 |
| CAND-02 | Đăng ký tài khoản | Giữ thành UC-002 | - | U-R03 | REQ-07, REQ-08 | Mục tiêu, EV-02 |
| CAND-03 | Đăng nhập | Giữ thành UC-003 | - | U-R01: nguồn nêu đăng nhập và tài khoản (mục 1, mục 2, mục 11) | REQ-06, REQ-02, REQ-39, REQ-40 | Mục tiêu |
| CAND-04 | Đặt lịch khám | Giữ thành UC-004 | - | Giao dịch nghiệp vụ (U-R04 b) | REQ-09 đến REQ-13 | Mục tiêu, EV-03 |
| CAND-05 | Hủy lịch hẹn | Giữ thành UC-009 | - | Giao dịch nghiệp vụ có quy tắc thời hạn (U-R04 b) | REQ-19, REQ-20 | Mục tiêu, EV-04 |
| CAND-06 | Xem kết luận khám | Giữ thành UC-017 | - | Mục tiêu thông tin độc lập (U-R05); căn cứ câu nguồn mục 13, chờ xác nhận ở Q-02 | REQ-45 | Mục tiêu, EV-05 |
| CAND-07 | Xác nhận hoặc từ chối lịch hẹn chờ | Giữ thành UC-007 | - | Cùng tác nhân, cùng đối tượng, cùng phiên; từ chối là luồng thay thế (Bước 7.1) | REQ-14 đến REQ-18 | Mục tiêu, EV-06 |
| CAND-08 | Đặt lịch khám cho bệnh nhân gọi điện | Giữ thành UC-005 | - | U-R10 b: lễ tân phải tìm hoặc tạo hồ sơ, lịch xác nhận ngay (quy tắc khác) | REQ-22 đến REQ-25 | Mục tiêu, EV-07 |
| CAND-09 | Hủy lịch hẹn cho bệnh nhân | Giữ thành UC-010 | - | U-R10 b: lễ tân tìm lịch hẹn của bệnh nhân, không bị giới hạn 4 tiếng | REQ-21 | Mục tiêu, EV-08 |
| CAND-10 | Ghi nhận bệnh nhân đến khám | Giữ thành UC-011 | - | Phản hồi sự kiện nghiệp vụ, kết quả rõ ràng | REQ-27 | Mục tiêu, EV-09 |
| CAND-11 | Đánh dấu bệnh nhân không đến | Giữ thành UC-012 | - | Phản hồi sự kiện nghiệp vụ, có quy tắc riêng | REQ-28, REQ-29, REQ-30 | Mục tiêu, EV-10 |
| CAND-12 | Xem lịch hẹn bị ảnh hưởng do khoá khung giờ | Là bước của UC-014 | U-T9, U-AP03 | Thông báo là hệ quả của UC-014 (U-R06); cách lễ tân nhận chờ Q-05, Q-20 | REQ-37 | Mục tiêu |
| CAND-13 | Điều phối lịch khám | Tách thành CAND-07, CAND-08, CAND-09, CAND-10, CAND-11 | U-T1, U-T6, U-AP04 | Mức Summary | REQ-14 đến REQ-30 | Mục tiêu |
| CAND-14 | Xem lịch hẹn trong ngày | Giữ thành UC-015 | - | Mục tiêu thông tin độc lập của bác sĩ (U-R05) | REQ-31 | Mục tiêu, EV-11 |
| CAND-15 | Ghi kết luận khám | Giữ thành UC-016 | - | Giao dịch nghiệp vụ, đổi trạng thái lịch hẹn | REQ-32, REQ-33, REQ-34 | Mục tiêu, EV-12 |
| CAND-16 | Đăng ký lịch làm việc tuần | Giữ thành UC-013 | - | Giao dịch nghiệp vụ của bác sĩ | REQ-35 | Mục tiêu, EV-13 |
| CAND-17 | Khoá khung giờ đột xuất | Giữ thành UC-014 | - | Giao dịch nghiệp vụ có hệ quả báo lễ tân | REQ-36, REQ-37 | Mục tiêu, EV-14 |
| CAND-18 | Quản lý chuyên khoa | Giữ thành UC-018 | - | U-R04: CRUD danh mục, nguồn chỉ nêu "quản lý" | REQ-38 | Mục tiêu, EV-15 |
| CAND-19 | Quản lý tài khoản bác sĩ và lễ tân | Giữ thành UC-019 | - | U-R15, U-R04: cùng tác nhân, cùng loại dữ liệu tài khoản | REQ-39, REQ-40 | Mục tiêu, EV-16 |
| CAND-20 | Cấu hình tham số | Giữ thành UC-020 | - | U-R15 | REQ-41 | Mục tiêu, EV-17 |
| CAND-21 | Xem báo cáo tháng | Giữ thành UC-021 | - | U-R05: một tác nhân, cùng cách thao tác, gộp các chỉ số | REQ-42 | Mục tiêu, EV-18 |
| CAND-22 | Gửi SMS nhắc lịch hằng ngày | Giữ thành UC-008 | - | U-R06, U-R07: có thời điểm rõ, tác nhân chính ACT-07 | REQ-26 | Mục tiêu, EV-19 |
| CAND-23 | Xem danh sách chuyên khoa | Gộp vào UC-001 | U-T1, U-AP01 | Bước của mục tiêu tra cứu lịch trống (U-R05) | REQ-02 | Động từ |
| CAND-24 | Xem danh sách bác sĩ theo chuyên khoa | Gộp vào UC-001 | U-T1, U-AP01 | Bước của mục tiêu tra cứu lịch trống (U-R05) | REQ-03 | Động từ |
| CAND-25 | Gửi mã OTP xác thực số điện thoại | Là bước của UC-002 | U-T9, U-AP03 | Lời gọi tới ACT-06 trong phiên đăng ký (U-R08) | REQ-08 | Động từ |
| CAND-26 | Chọn chuyên khoa, bác sĩ, ngày, khung giờ còn trống | Giữ thành UC-006 | - | Q4 a: đoạn tương tác từ 3 bước trở lên dùng lại trong UC-004 và UC-005 | REQ-09, REQ-10, REQ-11, REQ-22 | Động từ |
| CAND-27 | Để phòng khám tự phân bác sĩ | Là bước của UC-006 | U-T1, U-AP15 | Biến thể lựa chọn bác sĩ (U-R12); cách phân chờ Q-01 | REQ-10 | Động từ |
| CAND-28 | Xem lịch hẹn chờ xác nhận | Là bước của UC-007 | U-T1 | Việc xem phục vụ xác nhận, từ chối (U-R05) | REQ-14 | Động từ |
| CAND-29 | Xác nhận lịch hẹn | Gộp vào UC-007 | U-AP12 | Trùng nghĩa với CAND-07 | REQ-15 | Động từ |
| CAND-30 | Từ chối lịch hẹn | Gộp vào UC-007 | U-AP15 | Luồng thay thế của UC-007 | REQ-16, REQ-17 | Động từ |
| CAND-31 | Gửi SMS thông báo xác nhận hoặc từ chối | Là bước của UC-007 | U-T9, U-AP03 | U-R06 | REQ-18 | Động từ |
| CAND-32 | Tạo hồ sơ bệnh nhân | Là bước của UC-005 | U-T1, U-T3 | Nguồn chỉ nêu tạo hồ sơ khi đặt lịch hộ (mục 6) | REQ-23, REQ-24 | Động từ |
| CAND-33 | Khoá chức năng tự đặt lịch của bệnh nhân | Là bước của UC-012 | U-T9, U-AP11 | Hệ quả của lần đánh dấu "Không đến" thứ 3 (U-R09) | REQ-30 | Động từ |
| CAND-34 | Chuyển lịch hẹn sang "Đã khám" | Là bước của UC-016 | U-T9, U-AP03 | Hệ quả của ghi kết luận (U-R09) | REQ-34 | Động từ |
| CAND-35 | Báo lễ tân khi khung giờ bị khoá đã có lịch hẹn | Là bước của UC-014 | U-T9, U-AP03 | U-R06 | REQ-37 | Động từ |
| CAND-36 | Đổi lịch hẹn cho bệnh nhân | Loại | U-T10 | Nguồn chỉ nói "liên hệ bệnh nhân đổi lịch", không nêu chức năng đổi lịch trên hệ thống; chờ Q-03 | REQ-37 | Động từ |
| CAND-37 | Mở khoá tự đặt lịch cho bệnh nhân | Loại | U-T10 | Nguồn không nêu; chờ Q-04 | REQ-30 | Động từ |
| CAND-38 | Tạo lịch hẹn "Chờ xác nhận" | Là bước của UC-004 | U-T9, U-AP03 | Hệ quả của đặt lịch | REQ-13 | Động từ |

## 4. Bảng use case

| UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | Nhóm chức năng | REQ | Mức | CAND nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UC-001 | Tra cứu lịch trống của bác sĩ | Browse Doctor Availability | ACT-01 Bệnh nhân | - | Bệnh nhân biết bác sĩ nào của chuyên khoa nào còn khung giờ trống trong 14 ngày tới. | Bệnh nhân, chưa cần đăng nhập, xem danh sách chuyên khoa, bác sĩ theo chuyên khoa và lịch trống của từng bác sĩ. | EV-01 | Tra cứu và tài khoản | REQ-02, REQ-03, REQ-04, REQ-05 | User-goal | CAND-01, CAND-23, CAND-24 |
| UC-002 | Đăng ký tài khoản | Register Account | ACT-01 | ACT-06 Cổng SMS | Bệnh nhân có tài khoản gắn với số điện thoại đã xác thực. | Bệnh nhân tự đăng ký bằng số điện thoại và xác thực số điện thoại bằng mã OTP nhận qua SMS. | EV-02 | Tra cứu và tài khoản | REQ-06, REQ-07, REQ-08 | User-goal | CAND-02, CAND-25 |
| UC-003 | Đăng nhập | Log In | ACT-01, ACT-02 Lễ tân, ACT-03 Bác sĩ, ACT-04 Quản trị viên, ACT-05 Quản lý phòng khám | - | Người dùng được hệ thống nhận diện và dùng được các chức năng theo vai trò. | Điều kiện để dùng các UC cần tài khoản (U-R01). | Người dùng cần dùng chức năng cần tài khoản | Tra cứu và tài khoản | REQ-06, REQ-02, REQ-39, REQ-40 | Subfunction | CAND-03 |
| UC-004 | Đặt lịch khám | Book Appointment | ACT-01 | - | Bệnh nhân có một lịch hẹn "Chờ xác nhận" với bác sĩ và khung giờ mong muốn. | Bệnh nhân chọn chuyên khoa, bác sĩ hoặc để phòng khám tự phân, ngày, khung giờ trống và nhập lý do khám; hệ thống kiểm tra giới hạn 2 lịch hẹn chưa diễn ra và trạng thái khoá. | EV-03 | Đặt lịch | REQ-09 đến REQ-13, REQ-30 | User-goal | CAND-04, CAND-38 |
| UC-005 | Đặt lịch khám cho bệnh nhân | Book Appointment for Patient | ACT-02 | - | Bệnh nhân gọi điện có một lịch hẹn đã xác nhận do lễ tân đặt. | Lễ tân tìm bệnh nhân hoặc tạo hồ sơ bệnh nhân mới (họ tên, ngày sinh, số điện thoại), rồi đặt lịch; lịch được xác nhận ngay. Có gửi SMS hay không chờ Q-10. | EV-07 | Đặt lịch | REQ-22 đến REQ-25 | User-goal | CAND-08, CAND-32 |
| UC-006 | Chọn khung giờ khám | Select Appointment Slot | - (Được gọi từ UC-004, UC-005) | - | Một khung giờ trống của một bác sĩ được chọn cho lịch hẹn. | Đoạn chọn chuyên khoa, bác sĩ (hoặc tự phân), ngày và khung giờ 30 phút còn trống, dùng chung cho UC-004 và UC-005 (Q4 a). | Được gọi từ UC-004, UC-005 | Đặt lịch | REQ-09, REQ-10, REQ-11 | Subfunction | CAND-26, CAND-27 |
| UC-007 | Duyệt lịch hẹn | Review Pending Appointment | ACT-02 | ACT-06 | Lịch hẹn chờ được xác nhận hoặc từ chối có lý do, bệnh nhân được báo qua SMS. | Lễ tân xem các lịch hẹn "Chờ xác nhận", xác nhận hoặc từ chối kèm lý do; hệ thống gửi SMS thông báo cho bệnh nhân. | EV-06 | Đặt lịch | REQ-14 đến REQ-18 | User-goal | CAND-07, CAND-28 đến CAND-31 |
| UC-008 | Nhắc lịch khám | Send Appointment Reminders | ACT-07 Bộ định thời | ACT-06 | Bệnh nhân có lịch hẹn đã xác nhận vào ngày hôm sau nhận được SMS nhắc lịch. | Vào 18 giờ mỗi ngày, hệ thống gửi SMS nhắc lịch cho mọi lịch hẹn đã xác nhận của ngày hôm sau. Bệnh nhân là bên hưởng lợi. | EV-19 | Đặt lịch | REQ-26, REQ-46 | User-goal | CAND-22 |
| UC-009 | Hủy lịch hẹn | Cancel Appointment | ACT-01 | - | Lịch hẹn của bệnh nhân bị hủy và khung giờ được giải phóng. | Bệnh nhân hủy lịch hẹn của mình khi còn ít nhất 4 tiếng trước giờ khám. | EV-04 | Đặt lịch | REQ-19, REQ-20 | User-goal | CAND-05 |
| UC-010 | Hủy lịch hẹn cho bệnh nhân | Cancel Appointment for Patient | ACT-02 | - | Lịch hẹn của bệnh nhân bị hủy theo yêu cầu, kể cả khi còn dưới 4 tiếng trước giờ khám. | Lễ tân tìm lịch hẹn của bệnh nhân và hủy. Phạm vi thời gian được phép chờ Q-09. | EV-08 | Đặt lịch | REQ-21 | User-goal | CAND-09 |
| UC-011 | Tiếp nhận bệnh nhân đến khám | Check In Patient | ACT-02 | - | Lịch hẹn được ghi nhận là bệnh nhân đã đến. | Lễ tân tìm lịch hẹn của bệnh nhân vừa tới và ghi nhận đã đến (check-in). | EV-09 | Tiếp đón | REQ-27 | User-goal | CAND-10 |
| UC-012 | Đánh dấu bệnh nhân không đến | Mark No-Show | ACT-02 | - | Lịch hẹn quá giờ 30 phút được ghi "Không đến"; bệnh nhân vi phạm đủ số lần bị khoá tự đặt lịch. | Lễ tân đánh dấu "Không đến" cho lịch hẹn quá giờ 30 phút; hệ thống khoá tự đặt lịch trực tuyến khi đủ 3 lần trong 6 tháng. | EV-10 | Tiếp đón | REQ-28, REQ-29, REQ-30 | User-goal | CAND-11, CAND-33 |
| UC-013 | Đăng ký lịch làm việc tuần | Register Weekly Schedule | ACT-03 Bác sĩ | - | Bác sĩ có lịch làm việc tuần làm cơ sở cho khung giờ trống. | Bác sĩ chọn các buổi sáng, chiều làm việc trong tuần. | EV-13 | Khám bệnh và lịch làm việc | REQ-35 | User-goal | CAND-16 |
| UC-014 | Khoá khung giờ đột xuất | Block Time Slot | ACT-03 | - | Các khung giờ bác sĩ không làm được không còn nhận lịch mới, lễ tân được báo các lịch hẹn bị ảnh hưởng. | Bác sĩ khoá một số khung giờ; nếu khung giờ đã có lịch hẹn, hệ thống báo cho lễ tân để liên hệ bệnh nhân đổi lịch. | EV-14 | Khám bệnh và lịch làm việc | REQ-36, REQ-37 | User-goal | CAND-17, CAND-12, CAND-35 |
| UC-015 | Xem lịch hẹn trong ngày | View Daily Appointments | ACT-03 | - | Bác sĩ biết danh sách bệnh nhân hẹn khám của mình trong một ngày. | Bác sĩ chọn ngày và xem danh sách lịch hẹn của mình. | EV-11 | Khám bệnh và lịch làm việc | REQ-31 | User-goal | CAND-14 |
| UC-016 | Ghi kết luận khám | Record Examination Result | ACT-03 | - | Lịch hẹn có kết luận khám và ở trạng thái "Đã khám". | Bác sĩ ghi chẩn đoán và lời dặn vào lịch hẹn sau khi khám. | EV-12 | Khám bệnh và lịch làm việc | REQ-32, REQ-33, REQ-34, REQ-45 | User-goal | CAND-15, CAND-34 |
| UC-017 | Xem kết luận khám | View Examination Result | ACT-01 | - | Bệnh nhân đọc được kết luận khám của chính mình. | Bệnh nhân xem chẩn đoán và lời dặn của các lần khám của mình. Phạm vi chờ Q-02. | EV-05 | Khám bệnh và lịch làm việc | REQ-45 | User-goal | CAND-06 |
| UC-018 | Quản lý chuyên khoa | Manage Specialties | ACT-04 Quản trị viên | - | Danh mục chuyên khoa phản ánh đúng các chuyên khoa của phòng khám. | Quản trị viên quản lý danh mục chuyên khoa (nguồn không nêu chi tiết thao tác). | EV-15 | Quản trị và báo cáo | REQ-38 | User-goal | CAND-18 |
| UC-019 | Quản lý tài khoản nhân viên | Manage Staff Accounts | ACT-04 | - | Bác sĩ và lễ tân có tài khoản đúng vai trò. | Quản trị viên quản lý tài khoản bác sĩ và tài khoản lễ tân (nguồn không nêu chi tiết thao tác). | EV-16 | Quản trị và báo cáo | REQ-39, REQ-40 | User-goal | CAND-19 |
| UC-020 | Cấu hình tham số nghiệp vụ | Configure Business Parameters | ACT-04 | - | Hệ thống áp dụng giá trị mới của số giờ tối thiểu được hủy và số lần không đến tối đa. | Quản trị viên đặt giá trị các tham số nguồn nêu. | EV-17 | Quản trị và báo cáo | REQ-41, REQ-20, REQ-30 | User-goal | CAND-20 |
| UC-021 | Xem báo cáo lịch hẹn tháng | View Monthly Appointment Report | ACT-05 Quản lý phòng khám | - | Quản lý có số lịch hẹn theo chuyên khoa, theo bác sĩ và tỷ lệ không đến của một tháng. | Quản lý chọn tháng và xem báo cáo. | EV-18 | Quản trị và báo cáo | REQ-42 | User-goal | CAND-21 |

## 5. Ma trận truy vết REQ --> UC

| REQ | Nội dung tóm tắt | UC phủ | Ghi chú (lý do nếu không phủ) |
|---|---|---|---|
| REQ-01 | Phần mềm web | - | Ràng buộc, chuyển P06 |
| REQ-02 | Xem chuyên khoa | UC-001 | Không có |
| REQ-03 | Xem bác sĩ theo chuyên khoa | UC-001 | Không có |
| REQ-04 | Xem lịch trống | UC-001 | Không có |
| REQ-05 | Phạm vi 14 ngày | UC-001 | Quy tắc gắn UC-001; Q-06 |
| REQ-06 | Phải có tài khoản để đặt lịch | UC-003, UC-004 | Quy tắc gắn UC-004 |
| REQ-07 | Tự đăng ký bằng SĐT | UC-002 | Không có |
| REQ-08 | OTP qua SMS | UC-002 | Không có |
| REQ-09 | Đặt lịch khám | UC-004, UC-006 | Không có |
| REQ-10 | Tự phân bác sĩ | UC-006 | Q-01 |
| REQ-11 | Khung 30 phút | UC-006 | Quy tắc gắn UC-006 |
| REQ-12 | Tối đa 2 lịch chưa diễn ra | UC-004 | Quy tắc gắn UC-004; Q-07 |
| REQ-13 | Trạng thái Chờ xác nhận | UC-004 | Quy tắc gắn UC-004 |
| REQ-14 | Xem lịch chờ | UC-007 | Không có |
| REQ-15 | Xác nhận | UC-007 | Không có |
| REQ-16 | Từ chối | UC-007 | Không có |
| REQ-17 | Lý do từ chối | UC-007 | Quy tắc gắn UC-007 |
| REQ-18 | SMS kết quả duyệt | UC-007 | Q-10 cho UC-005 |
| REQ-19 | Bệnh nhân hủy | UC-009 | Không có |
| REQ-20 | Hạn hủy 4 tiếng | UC-009 | Quy tắc gắn UC-009 |
| REQ-21 | Lễ tân hủy sát giờ | UC-010 | Q-09 |
| REQ-22 | Lễ tân đặt hộ | UC-005 | Không có |
| REQ-23 | Tạo hồ sơ bệnh nhân | UC-005 | Q-11 |
| REQ-24 | Thành phần hồ sơ | UC-005 | Dữ liệu gắn UC-005 |
| REQ-25 | Xác nhận ngay | UC-005 | Quy tắc gắn UC-005 |
| REQ-26 | Nhắc lịch 18 giờ | UC-008 | Không có |
| REQ-27 | Check-in | UC-011 | Không có |
| REQ-28 | Đánh dấu Không đến | UC-012 | Không có |
| REQ-29 | Quá giờ 30 phút | UC-012 | Quy tắc gắn UC-012 |
| REQ-30 | Khoá sau 3 lần/6 tháng | UC-012, UC-004 | Quy tắc gắn UC-012; Q-04, Q-08 |
| REQ-31 | Bác sĩ xem lịch theo ngày | UC-015 | Không có |
| REQ-32 | Ghi kết luận | UC-016 | Không có |
| REQ-33 | Thành phần kết luận | UC-016 | Dữ liệu gắn UC-016 |
| REQ-34 | Chuyển Đã khám | UC-016 | Quy tắc gắn UC-016 |
| REQ-35 | Lịch làm việc tuần | UC-013 | Q-14 |
| REQ-36 | Khoá khung giờ | UC-014 | Không có |
| REQ-37 | Báo lễ tân | UC-014 | Q-03, Q-05 |
| REQ-38 | Quản lý chuyên khoa | UC-018 | Không có |
| REQ-39 | Tài khoản bác sĩ | UC-019 | Không có |
| REQ-40 | Tài khoản lễ tân | UC-019 | Không có |
| REQ-41 | Cấu hình tham số | UC-020 | Q-12 |
| REQ-42 | Báo cáo tháng | UC-021 | Q-15 |
| REQ-43 | 3 giây / 200 người dùng | - | Phi chức năng, chuyển P06 |
| REQ-44 | Dùng được trên điện thoại | - | Ràng buộc, chuyển P06 |
| REQ-45 | Quyền xem kết luận | UC-016, UC-017 | Phi chức năng gắn UC-017; phần còn lại chuyển P06 |
| REQ-46 | SMS Gateway qua API | UC-002, UC-007, UC-008 | Giao tiếp ngoài |

## 6. Thống kê và nhận xét ngưỡng

| ACT | Số UC là tác nhân chính | Số UC là tác nhân phụ | Nhận xét |
|---|---|---|---|
| ACT-01 Bệnh nhân | 6 (UC-001, 002, 003, 004, 009, 017) | 0 | Trong mức 2-12 |
| ACT-02 Lễ tân | 6 (UC-003, 005, 007, 010, 011, 012) | 0 | Trong mức 2-12 |
| ACT-03 Bác sĩ | 5 (UC-003, 013, 014, 015, 016) | 0 | Trong mức 2-12 |
| ACT-04 Quản trị viên | 4 (UC-003, 018, 019, 020) | 0 | Trong mức 2-12 |
| ACT-05 Quản lý phòng khám | 2 (UC-003, 021) | 0 | Chỉ 1 UC nghiệp vụ; đúng với nguồn (mục 12 là câu duy nhất về vai trò này) |
| ACT-06 Cổng SMS | 0 | 3 (UC-002, 007, 008) | Có thể thêm UC-005, UC-009, UC-010 tuỳ Q-09, Q-10 |
| ACT-07 Bộ định thời | 1 (UC-008) | 0 | Bình thường với tác nhân thời gian |

Tổng số UC: 21, trong đó 19 User-goal và 2 Subfunction (UC-003, UC-006; khoảng 10%). Số UC theo nhóm: Tra cứu và tài khoản 3; Đặt lịch 7; Tiếp đón 2; Khám bệnh và lịch làm việc 5; Quản trị và báo cáo 4. Nhóm Tiếp đón chỉ 2 UC nhưng tách riêng vì là nghiệp vụ tại quầy trong ngày khám, khác hẳn nhóm Đặt lịch.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-21 | Có cần UC "Đổi lịch hẹn" cho lễ tân khi bác sĩ khoá khung giờ không, hay lễ tân dùng UC-010 rồi UC-005? (tổng hợp từ Q-03) | CAND-36; danh sách UC | REQ-37 |
| Q-22 | Có cần UC mở khoá tự đặt lịch cho bệnh nhân không, và tác nhân nào làm? (tổng hợp từ Q-04) | CAND-37; danh sách UC | REQ-30 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- CAND-36, CAND-37 kết luận "Loại" vì chưa truy vết được, nhưng thực chất đang chờ Q-21, Q-22. Bảng kết luận không có giá trị "Chờ Q"; đã ghi rõ trong cột Lý do.
- UC-006 Chọn khung giờ khám được giữ theo Q4 a, dù "Chọn khung giờ" xuất hiện trong ví dụ Subfunction quá nhỏ ở phần định nghĩa. Lý do giữ: đoạn này gồm chọn chuyên khoa, bác sĩ hoặc tự phân, ngày, khung giờ (từ 3 bước) và dùng lại trong UC-004, UC-005.
- UC-017 Xem kết luận khám chỉ có căn cứ gián tiếp (REQ-45 là yêu cầu phi chức năng về quyền xem). Giữ theo U-T10 (truy vết được về câu nguồn), chờ xác nhận ở Q-02.
