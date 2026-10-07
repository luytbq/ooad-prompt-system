# P02R - Review danh sách use case - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02R |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, P00-problem-brief.md 1.0, P01-actors.md 1.0, P02-usecases.md 1.0, yeu-cau-phong-kham.md |
| Phạm vi | TAC_NHAN, DANH_SACH_UC |

## 1. Tóm tắt

- Đối tượng: bảng tác nhân P01-actors.md (7 tác nhân) và bảng use case P02-usecases.md (21 use case). Có tài liệu nguồn và P00. Không chấm sơ đồ (P03 chưa chạy).
- Số phát hiện: Nghiêm trọng 0; Trung bình 2; Nhỏ 4.
- Kết luận: Đạt.
- Điểm làm tốt:
  - UC-008 Nhắc lịch khám có tác nhân chính ACT-07 Bộ định thời, tác nhân phụ ACT-06 Cổng SMS, bệnh nhân chỉ là bên hưởng lợi, đúng U-R06, U-R07.
  - UC-004 Đặt lịch khám và UC-005 Đặt lịch khám cho bệnh nhân tách theo U-R10 b với căn cứ cụ thể (tạo hồ sơ, xác nhận ngay).
  - CAND-12, CAND-33, CAND-35 (thông báo, khoá, báo lễ tân) đều thành bước của UC gây ra, không có UC "hệ thống tự làm".

## 2. Bảng kiểm kê

Không có (đối tượng đã có mã ACT, UC).

## 3. Bảng phát hiện

| Mã | Phần tử | Vấn đề | Quy tắc vi phạm | Mức độ (Nghiêm trọng / Trung bình / Nhỏ) | Đề xuất sửa |
|---|---|---|---|---|---|
| UCR-01 | UC-009 Hủy lịch hẹn; UC-010 Hủy lịch hẹn cho bệnh nhân | Hai UC cùng mục tiêu, cùng kết quả (lịch hẹn bị hủy, khung giờ giải phóng). Khác biệt chỉ là bước tìm lịch hẹn của bệnh nhân và điều kiện 4 tiếng ("Sau thời điểm đó chỉ lễ tân mới hủy được", mục 5). Theo U-R10 a, đây là một UC nối hai tác nhân, điều kiện 4 tiếng là luồng thay thế | U-R10, U-AP12 | Trung bình | Gộp UC-010 vào UC-009 "Hủy lịch hẹn", tác nhân chính ACT-01, ACT-02; bước tìm lịch hẹn của lễ tân và ngoại lệ "còn dưới 4 tiếng" thành luồng thay thế ở P04 |
| UCR-02 | UC-017 Xem kết luận khám | Căn cứ duy nhất là REQ-45, một yêu cầu phi chức năng về quyền xem ("chỉ bác sĩ khám và chính bệnh nhân được xem"). Nguồn không có câu chức năng nào nói bệnh nhân xem kết luận; P00 đã đặt Q-02 | U-T10 | Trung bình | Giữ UC-017 với trạng thái "Chờ Q-02"; nếu Q-02 trả lời Không thì loại UC-017 và chuyển REQ-45 sang P06 |
| UCR-03 | UC-006 Chọn khung giờ khám | Subfunction dùng qua include cho UC-004, UC-005 là hợp lệ, nhưng "Chọn khung giờ" là ví dụ điển hình của UC quá nhỏ. Rủi ro ở P03 là include bị hiểu như phân rã chức năng | U-AP01 (nguy cơ), D-AP01 (nguy cơ) | Nhỏ | Giữ; ở P03 chỉ vẽ include từ UC-004, UC-005 tới UC-006, không nối UC-006 với tác nhân |
| UCR-04 | UC-003 Đăng nhập nối với ACT-04, ACT-05 | Nguồn nêu tài khoản của bệnh nhân (mục 2) và của bác sĩ, lễ tân (mục 11), không nêu tài khoản của quản trị viên và quản lý phòng khám | U-T10, U-R01 | Nhỏ | Giữ nối ACT-04, ACT-05 với UC-003, thêm câu hỏi mở "Quản trị viên và quản lý phòng khám có đăng nhập bằng tài khoản không?" |
| UCR-05 | UC-011 Tiếp nhận bệnh nhân đến khám | Luồng chính dự kiến chỉ 2-3 bước (tìm lịch hẹn, ghi nhận đến) | U-T4 | Nhỏ | Giữ: sự kiện nghiệp vụ riêng (EV-09) và kết quả riêng; ghi nhận xét ở P04 nếu luồng dưới 3 bước |
| UCR-06 | UC-019 Quản lý tài khoản nhân viên | Từ "nhân viên" không có trong nguồn; nguồn dùng "tài khoản bác sĩ và lễ tân" | U-N4 | Nhỏ | Đổi tên thành "Quản lý tài khoản bác sĩ và lễ tân" hoặc giữ và định nghĩa "nhân viên" ở P05 |

## 4. Danh sách use case đề xuất sau sửa

| UC | Tên (VI) | Tên (EN) | Tác nhân chính | Tác nhân phụ | Mục tiêu (kết quả có giá trị) | Thay đổi | Mã phát hiện |
|---|---|---|---|---|---|---|---|
| UC-001 | Tra cứu lịch trống của bác sĩ | Browse Doctor Availability | ACT-01 | - | Bệnh nhân biết bác sĩ nào còn khung giờ trống | Giữ | - |
| UC-002 | Đăng ký tài khoản | Register Account | ACT-01 | ACT-06 | Bệnh nhân có tài khoản với số điện thoại đã xác thực | Giữ | - |
| UC-003 | Đăng nhập | Log In | ACT-01 đến ACT-05 | - | Người dùng được nhận diện theo vai trò | Giữ | UCR-04 |
| UC-004 | Đặt lịch khám | Book Appointment | ACT-01 | - | Bệnh nhân có lịch hẹn "Chờ xác nhận" | Giữ | - |
| UC-005 | Đặt lịch khám cho bệnh nhân | Book Appointment for Patient | ACT-02 | - | Bệnh nhân gọi điện có lịch hẹn đã xác nhận | Giữ | - |
| UC-006 | Chọn khung giờ khám | Select Appointment Slot | - | - | Khung giờ trống được chọn | Giữ | UCR-03 |
| UC-007 | Duyệt lịch hẹn | Review Pending Appointment | ACT-02 | ACT-06 | Lịch chờ được xác nhận hoặc từ chối, bệnh nhân được báo | Giữ | - |
| UC-008 | Nhắc lịch khám | Send Appointment Reminders | ACT-07 | ACT-06 | Bệnh nhân nhận SMS nhắc lịch ngày hôm sau | Giữ | - |
| UC-009 | Hủy lịch hẹn | Cancel Appointment | ACT-01, ACT-02 | - | Lịch hẹn bị hủy, khung giờ được giải phóng | Gộp từ UC-009, UC-010 | UCR-01 |
| UC-010 | Hủy lịch hẹn cho bệnh nhân | Cancel Appointment for Patient | ACT-02 | - | - | Loại (gộp vào UC-009) | UCR-01 |
| UC-011 | Tiếp nhận bệnh nhân đến khám | Check In Patient | ACT-02 | - | Lịch hẹn ghi nhận bệnh nhân đã đến | Giữ | UCR-05 |
| UC-012 | Đánh dấu bệnh nhân không đến | Mark No-Show | ACT-02 | - | Lịch hẹn ghi "Không đến", khoá khi đủ số lần | Giữ | - |
| UC-013 | Đăng ký lịch làm việc tuần | Register Weekly Schedule | ACT-03 | - | Bác sĩ có lịch làm việc tuần | Giữ | - |
| UC-014 | Khoá khung giờ đột xuất | Block Time Slot | ACT-03 | - | Khung giờ bị khoá, lễ tân được báo | Giữ | - |
| UC-015 | Xem lịch hẹn trong ngày | View Daily Appointments | ACT-03 | - | Bác sĩ biết lịch hẹn trong ngày | Giữ | - |
| UC-016 | Ghi kết luận khám | Record Examination Result | ACT-03 | - | Lịch hẹn có kết luận, "Đã khám" | Giữ | - |
| UC-017 | Xem kết luận khám | View Examination Result | ACT-01 | - | Bệnh nhân đọc kết luận khám của mình | Giữ (chờ Q-02) | UCR-02 |
| UC-018 | Quản lý chuyên khoa | Manage Specialties | ACT-04 | - | Danh mục chuyên khoa đúng thực tế | Giữ | - |
| UC-019 | Quản lý tài khoản nhân viên | Manage Staff Accounts | ACT-04 | - | Bác sĩ, lễ tân có tài khoản đúng vai trò | Giữ | UCR-06 |
| UC-020 | Cấu hình tham số nghiệp vụ | Configure Business Parameters | ACT-04 | - | Tham số hủy lịch, không đến có giá trị mới | Giữ | - |
| UC-021 | Xem báo cáo lịch hẹn tháng | View Monthly Appointment Report | ACT-05 | - | Quản lý có số liệu lịch hẹn tháng | Giữ | - |

## 5. Quan hệ đề xuất sau sửa

Không có (phạm vi không gồm SO_DO).

## 6. Giới hạn của review

- UCR-01 dựa trên cách đọc U-R10 a. U-R10 b cũng nêu "áp dụng quy tắc khác" là lý do tách, nên P02 có căn cứ khi tách. Người viết cần chốt một cách hiểu trong QUY_UOC_DA_CHOT.
- Câu hỏi cần người viết trả lời: quản trị viên và quản lý phòng khám có đăng nhập bằng tài khoản không (UCR-04).
