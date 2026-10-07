# P05 - Từ điển thuật ngữ - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P05 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, yeu-cau-phong-kham.md, P00 1.0, P01 1.0, P02 1.0, P04-uc-specs/UC-004, UC-005, UC-008 (1.0), P04-uc-specs/_BR-register.md |
| Phạm vi | Toàn hệ thống |

## 1. Giới thiệu

Từ điển này là nguồn thuật ngữ duy nhất của Hệ thống đặt lịch khám ClinicBook. Mọi artifact dùng cột Thuật ngữ làm cách gọi chính thức. Từ ở cột "Từ đồng nghĩa không dùng" không được dùng trong artifact mới. Tên tiếng Anh là tên dùng cho lớp, thuộc tính, bảng ở các bước thiết kế.

## 2. Thuật ngữ

| GL | Thuật ngữ | Tiếng Anh | Định nghĩa | Từ đồng nghĩa không dùng | Nguồn (REQ / UC) | Ghi chú |
|---|---|---|---|---|---|---|
| GL-01 | Buổi làm việc | Work Session | Nửa ngày (buổi sáng hoặc buổi chiều) trong tuần mà bác sĩ đăng ký làm việc tại phòng khám. | Ca làm việc | REQ-35, UC-013 | Giá trị: Sáng, Chiều. Giờ bắt đầu, kết thúc của mỗi buổi chưa quy định (Q-14) |
| GL-02 | Check-in | Check-in | Việc lễ tân ghi nhận bệnh nhân có lịch hẹn đã có mặt tại phòng khám. | Tiếp nhận bệnh nhân | REQ-27, UC-011 | Trạng thái lịch hẹn sau check-in chưa quy định (Q-18) |
| GL-03 | Chuyên khoa | Specialty | Lĩnh vực khám chữa bệnh của phòng khám mà mỗi bác sĩ thuộc về, dùng để nhóm bác sĩ khi bệnh nhân tra cứu và đặt lịch. | Khoa | REQ-02, REQ-03, REQ-38, UC-001, UC-018 | Hiện có: Nội, Nhi, Da liễu (đoạn mở đầu) |
| GL-04 | Hồ sơ bệnh nhân | Patient Profile | Tập thông tin nhận diện một bệnh nhân do lễ tân tạo khi bệnh nhân gọi điện chưa có tài khoản. | Không có | REQ-23, REQ-24, UC-005 | Gồm họ tên, ngày sinh, số điện thoại (REQ-24). Quan hệ với Tài khoản bệnh nhân chờ Q-11 |
| GL-05 | Kết luận khám | Examination Result | Nội dung bác sĩ ghi vào một lịch hẹn sau khi khám, gồm chẩn đoán và lời dặn. | Kết quả khám | REQ-32, REQ-33, REQ-45, UC-016, UC-017 | Chỉ bác sĩ khám và chính bệnh nhân được xem (REQ-45) |
| GL-06 | Khoá tự đặt lịch | Self-booking Lock | Trạng thái của một bệnh nhân không được tự đặt lịch khám trực tuyến do vi phạm quy định không đến. | Khoá tài khoản | REQ-30, UC-004, UC-012 | Điều kiện theo BR-04. Cách mở khoá chờ Q-04 |
| GL-07 | Không đến | No-show | Trạng thái của lịch hẹn mà bệnh nhân không có mặt sau giờ hẹn một khoảng thời gian quy định, do lễ tân đánh dấu. | Vắng mặt | REQ-28, REQ-29, UC-012 | Khoảng thời gian 30 phút (REQ-29). Là một giá trị của trạng thái Lịch hẹn |
| GL-08 | Khung giờ | Time Slot | Khoảng thời gian 30 phút trong lịch làm việc của một bác sĩ, là đơn vị để đặt một lịch hẹn. | Khung giờ khám, ca khám | REQ-09, REQ-11, REQ-36, UC-004, UC-005, UC-006, UC-014 | Trạng thái: Trống, Đã có lịch hẹn, Bị khoá (REQ-36). Số lịch hẹn tối đa mỗi khung giờ chờ Q-19. Chọn "Khung giờ" vì nguồn chỉ dùng cách gọi này (F4 mục 2) |
| GL-09 | Lịch hẹn | Appointment | Thoả thuận khám giữa một bệnh nhân và phòng khám tại một khung giờ của một bác sĩ, kèm lý do khám. | Lịch khám, lịch, cuộc hẹn | REQ-09, REQ-13, REQ-25, UC-004, UC-005, UC-007, UC-008 | Thành phần: chuyên khoa, bác sĩ, ngày, khung giờ, lý do khám, lý do từ chối (khi bị từ chối), kết luận khám. Trạng thái nguồn nêu: Chờ xác nhận (BR-03), Đã xác nhận (BR-05, REQ-26), Không đến, Đã khám (REQ-34). Trạng thái sau hủy, từ chối, check-in chờ Q-18 |
| GL-10 | Lịch hẹn chưa diễn ra | Upcoming Appointment | Lịch hẹn của một bệnh nhân có giờ khám chưa tới. | Không có | REQ-12, UC-004 | Dùng trong BR-02. Có tính lịch hẹn "Chờ xác nhận" không chờ Q-07 |
| GL-11 | Lịch làm việc tuần | Weekly Work Schedule | Tập các buổi làm việc trong một tuần mà một bác sĩ đăng ký, làm cơ sở sinh ra các khung giờ. | Lịch trực | REQ-35, UC-013 | Đăng ký từng tuần hay lặp lại chờ Q-14 |
| GL-12 | Lịch trống | Doctor Availability | Tập các khung giờ trống của một bác sĩ trong phạm vi ngày được xem. | Lịch rảnh | REQ-04, REQ-05, UC-001 | Phạm vi 14 ngày tới (REQ-05, Q-06) |
| GL-13 | Nhắc lịch | Appointment Reminder | Tin SMS hệ thống gửi cho bệnh nhân vào buổi tối trước ngày khám để nhắc lịch hẹn đã xác nhận. | Không có | REQ-26, UC-008 | Thời điểm và điều kiện theo BR-06. Nội dung chờ Q-28 |
| GL-14 | OTP | One-Time Password | Mã dùng một lần hệ thống gửi qua SMS để xác thực số điện thoại khi bệnh nhân đăng ký tài khoản. | Mã xác thực | REQ-08, UC-002 | Độ dài, thời hạn hiệu lực chưa quy định |
| GL-15 | Tài khoản bệnh nhân | Patient Account | Tư cách truy cập hệ thống của một bệnh nhân, gắn với một số điện thoại đã xác thực, cho phép tự đặt lịch khám. | Không có | REQ-06, REQ-07, UC-002, UC-004 | Phân biệt với Hồ sơ bệnh nhân (GL-04). Điều kiện đặt lịch theo BR-01 |
| GL-16 | Tham số nghiệp vụ | Business Parameter | Giá trị cấu hình do quản trị viên đặt, dùng làm ngưỡng trong quy tắc nghiệp vụ. | Cấu hình | REQ-41, UC-020 | Gồm: số giờ tối thiểu được hủy, số lần không đến tối đa. Danh sách đầy đủ chờ Q-12 |
| GL-17 | Tự phân bác sĩ | Automatic Doctor Assignment | Lựa chọn khi đặt lịch, trong đó bệnh nhân không chọn bác sĩ và phòng khám chỉ định bác sĩ cho lịch hẹn. | Không có | REQ-10, UC-006 | Ai phân và khi nào chờ Q-01 |
| GL-18 | Tỷ lệ không đến | No-show Rate | Đại lượng trong báo cáo tháng thể hiện mức độ bệnh nhân không đến theo lịch hẹn. | Không có | REQ-42, UC-021 | Công thức chờ Q-15 |

## 3. Ứng viên không đưa vào

| Ứng viên | Lý do không đưa vào | Nơi xuất hiện |
|---|---|---|
| Bệnh nhân, Lễ tân, Bác sĩ, Quản trị viên, Quản lý phòng khám | Tên tác nhân, không cần định nghĩa phân biệt | P01 |
| Cổng SMS, SMS | Tên tác nhân; SMS là từ phổ thông | REQ-46, ACT-06 |
| Lý do khám, lý do từ chối, chẩn đoán, lời dặn | Thuộc tính lẻ, ghi ở Ghi chú của GL-09, GL-05 | REQ-09, REQ-17, REQ-33 |
| Họ tên, ngày sinh, số điện thoại | Từ phổ thông, ghi ở Ghi chú của GL-04 | REQ-24 |
| Chờ xác nhận, Đã xác nhận, Đã khám | Giá trị trạng thái, ghi ở Ghi chú của GL-09 | REQ-13, REQ-25, REQ-34 |
| Báo cáo tháng | Tên use case UC-021 | REQ-42 |
| Đăng nhập, tài khoản bác sĩ, tài khoản lễ tân | Thuật ngữ kỹ thuật dùng đúng nghĩa thông thường | REQ-02, REQ-39, REQ-40 |
| Khung giờ bị khoá | Trạng thái của GL-08, ghi ở Ghi chú | REQ-36 |
| Nhân viên | Đồng nghĩa không có trong nguồn, dùng ở UC-019; nguồn nói "bác sĩ và lễ tân" | P02 UC-019 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-31 | Mã OTP có độ dài và thời hạn hiệu lực bao nhiêu? | GL-14, UC-002 | REQ-08 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-006 | Tên "Chọn khung giờ khám" dùng "khung giờ khám", thuật ngữ chính thức là "Khung giờ" (GL-08) | Giữ tên UC (đã chốt, là cụm động từ); ghi chú đồng nghĩa ở GL-08. Không cần đổi nếu nhóm chấp nhận |
| P02 | UC-011 | Tên "Tiếp nhận bệnh nhân đến khám" dùng "tiếp nhận", thuật ngữ chính thức là "Check-in" (GL-02) | Đổi tên thành "Check-in bệnh nhân" hoặc "Ghi nhận bệnh nhân đến khám" |
| P02 | UC-019 | "Nhân viên" không có trong nguồn | Đổi tên thành "Quản lý tài khoản bác sĩ và lễ tân" (trùng P02R UCR-06) |
| P02 | UC-004, UC-005, UC-008 | Tên dùng "lịch khám"; thuật ngữ chính thức là "Lịch hẹn" (GL-09). "Đặt lịch khám" là cụm động từ của nghiệp vụ nguồn dùng ("đặt lịch khám", đoạn mở đầu) | Giữ UC-004, UC-005. Đổi UC-008 thành "Nhắc lịch hẹn" nếu cần nhất quán |

## Vấn đề còn mở

- Mới có đặc tả P04 của UC-004, UC-005, UC-008. Target 2 (mọi khái niệm trong đặc tả P04 có trong từ điển) chỉ kiểm được trên ba đặc tả này; cần chạy lại P05 khi có đủ đặc tả.
- F4 xếp "cách gọi của tài liệu nguồn" (mục 2) trên "cách gọi cụ thể hơn" (mục 4), nên chọn "Khung giờ" dù "Khung giờ khám" cụ thể hơn.
