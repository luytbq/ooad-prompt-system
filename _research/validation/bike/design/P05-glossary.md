# P05 - Từ điển thuật ngữ - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P05 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-dap.md; P00 1.0; P01 1.0; P02 1.0 (Mục 4, Mục 5); P04 UC-005, UC-007, UC-009, UC-013 1.0; _BR-register.md (BR-01 đến BR-10) |
| Phạm vi | Toàn hệ thống |

Placeholder: NGUON_THUAT_NGU_CHUAN = Không có; YEU_CAU_BO_SUNG = Không có.

## 1. Giới thiệu

Từ điển này thống nhất cách gọi các khái niệm nghiệp vụ của Hệ thống cho thuê xe đạp công cộng CityBike. Mọi artifact dùng cột Thuật ngữ làm cách gọi chính thức và cột Tiếng Anh làm gốc đặt tên lớp, thuộc tính, bảng. Từ ở cột "Từ đồng nghĩa không dùng" không được dùng trong artifact mới.

## 2. Thuật ngữ

| GL | Thuật ngữ | Tiếng Anh | Định nghĩa | Từ đồng nghĩa không dùng | Nguồn (REQ / UC) | Ghi chú |
|---|---|---|---|---|---|---|
| GL-01 | Bảng giá cước | Fare Table | Tập mức giá do quản trị viên quản lý, dùng để tính cước chuyến đi. | Không có | REQ-55, UC-023 | Quan hệ với BR-07 chờ Q-15 |
| GL-02 | Báo cáo hằng tuần | Weekly Report | Báo cáo tổng hợp hoạt động thuê xe của một tuần dành cho ban giám đốc. | Không có | REQ-56, REQ-57, UC-024 | Gồm: số chuyến theo trạm, thời lượng trung bình, doanh thu, số xe hỏng. Cách tính chờ Q-17 |
| GL-03 | Báo hỏng | Damage Report | Thông báo của người thuê xe rằng xe vừa trả bị hỏng, kèm loại hỏng hóc và mô tả. | Không có | REQ-33, REQ-35, UC-008 | Loại hỏng hóc: phanh, xích, lốp, khác. Thời hạn báo hỏng theo REQ-34 |
| GL-04 | Chuyến đi | Trip | Khoảng sử dụng một xe của một người thuê xe, từ khi xe được rút khỏi ụ khoá tới khi xe được trả vào ụ khoá. | Chuyến | REQ-13, REQ-19, UC-005, UC-007 | Trạng thái đã thấy trong nguồn: đang diễn ra, đã kết thúc. Kết thúc khi xe thất lạc chờ Q-04 |
| GL-05 | Cước | Fare | Số tiền người thuê xe phải trả cho một chuyến đi, tính theo thời lượng chuyến. | Không có | REQ-20, REQ-21, UC-007 | Đơn vị: đồng. Công thức ở BR-07 |
| GL-06 | Hoá đơn | Invoice | Chứng từ gửi cho người thuê xe qua email sau khi chuyến đi kết thúc và cước đã được thu. | Không có | REQ-24, UC-007 | Thành phần chờ Q-24 |
| GL-07 | Hoàn tiền | Refund | Việc trả lại cho người thuê xe một khoản đã thu qua cổng thanh toán. | Không có | REQ-48, REQ-62, UC-017 | "Hoàn lại phần dư" ở REQ-23 là hoàn tiền hay huỷ phần tạm giữ còn lại chờ Q-26 |
| GL-08 | Khoản tạm giữ | Payment Hold | Số tiền được giữ trên thẻ thanh toán của người thuê xe qua cổng thanh toán trong suốt một chuyến đi, dùng để thu cước. | Số tiền tạm giữ, lệnh tạm giữ | REQ-10, REQ-11, REQ-22, REQ-30, UC-005, UC-007, UC-009 | Số tiền ở BR-05 |
| GL-09 | Lệnh điều chuyển | Transfer Order | Chỉ thị do nhân viên điều phối lập để chuyển xe từ một trạm tới trạm khác, được theo dõi tới khi hoàn tất. | Không có | REQ-44, REQ-45, REQ-46, UC-013, UC-014, UC-015 | Trạng thái: chưa hoàn tất, hoàn tất (điều kiện chờ Q-09). Thành phần chờ Q-25 |
| GL-10 | Lệnh mở khoá | Unlock Command | Thông điệp hệ thống gửi tới một ụ khoá để nhả xe cho người thuê xe. | Không có | REQ-12, REQ-58, UC-005 | Khác với việc mở khoá tài khoản (UC-018) |
| GL-11 | Mã QR của ụ khoá | Dock QR Code | Mã dán trên ụ khoá, người thuê xe quét bằng ứng dụng để yêu cầu thuê xe ở ụ đó. | Không có | REQ-07, UC-005 | Không có |
| GL-12 | Mã tham chiếu thẻ | Card Reference | Mã do cổng thanh toán cấp để đại diện cho thẻ thanh toán đã liên kết, là dữ liệu thẻ duy nhất hệ thống lưu. | Không có | REQ-60, REQ-61, UC-002 | Không có |
| GL-13 | Người thuê xe | Rider | Người dùng ứng dụng di động của CityBike để thuê và trả xe, phân biệt với các vai trò nhân viên. | Người dùng | REQ-02 đến REQ-33, ACT-01 | Xem Vấn đề còn mở về cách chọn tên |
| GL-14 | Nợ cước | Outstanding Fare | Khoản cước mà tài khoản chưa thanh toán đủ. | Không có | REQ-09, BR-03, UC-005 | Nguồn phát sinh và cách trả chờ Q-02 |
| GL-15 | Tài khoản bị khoá | Locked Account | Tài khoản người thuê xe đang bị chặn sử dụng dịch vụ cho tới khi nhân viên chăm sóc khách hàng mở khoá. | Không có | REQ-31, REQ-50, UC-009, UC-018 | Phạm vi chặn chờ Q-21 |
| GL-16 | Thẻ nhân viên | Staff Card | Thẻ nhân viên dùng tại ụ khoá khi lấy xe ra hoặc đưa xe vào để thực hiện lệnh điều chuyển. | Không có | REQ-46, UC-014 | Thiết bị đọc thẻ và vai trò dùng thẻ chờ Q-07 |
| GL-17 | Thẻ thanh toán | Payment Card | Thẻ của người thuê xe được liên kết với tài khoản qua cổng thanh toán, là nơi tạm giữ và thu tiền. | Thẻ | REQ-03, REQ-04, UC-002 | Mỗi tài khoản liên kết một thẻ (REQ-03). Số thẻ không được lưu (REQ-60) |
| GL-18 | Thời gian miễn phí cộng thêm | Extra Free Time | Khoảng thời gian không tính cước được cộng vào chuyến đi khi người thuê xe tới trạm không còn ụ trống. | Không có | REQ-25, REQ-26, REQ-27, UC-006 | 15 phút, một lần mỗi chuyến (REQ-26, REQ-27). Cách cộng vào cước chờ Q-05 |
| GL-19 | Trạm | Station | Địa điểm đặt một nhóm ụ khoá, nơi người thuê xe lấy và trả xe. | Không có | REQ-05, REQ-17, UC-004, UC-019 | Khoảng 10-20 ụ khoá mỗi trạm (đoạn mở đầu) |
| GL-20 | Trạm sắp đầy | Near-full Station | Trạm có tỉ lệ ụ có xe vượt ngưỡng sắp đầy. | Không có | REQ-41, REQ-43, UC-012 | Ngưỡng "trên 90%" ở REQ-43, đại lượng chờ Q-11 |
| GL-21 | Trạm sắp hết xe | Low Station | Trạm có tỉ lệ ụ có xe dưới ngưỡng sắp hết xe. | Không có | REQ-41, REQ-42, UC-012 | Ngưỡng 20% ở REQ-42 |
| GL-22 | Trạng thái xe | Bike Status | Tình trạng của một xe quyết định xe có được cho thuê hay không. | Không có | REQ-36, REQ-37, REQ-40, UC-008, UC-011 | Giá trị đã thấy: Sẵn sàng, Chờ kiểm tra; "thu hồi về xưởng" và "thất lạc" có phải giá trị trạng thái không chờ Q-27. BR-04 |
| GL-23 | Ụ khoá | Dock | Thiết bị tại trạm giữ một xe, có đầu đọc mã QR và khoá điện, trao đổi với máy chủ qua MQTT. | Ụ, dock | REQ-12, REQ-18, REQ-63, ACT-08, UC-005, UC-007 | Là tác nhân ACT-08 |
| GL-24 | Ụ trống | Empty Dock | Ụ khoá đang không giữ xe nào, sẵn sàng nhận xe trả. | Không có | REQ-05, REQ-17, REQ-25, UC-004, UC-007 | Không có |
| GL-25 | Xe | Bike | Xe đạp công cộng của CityBike được cho thuê tại các trạm. | Xe đạp | REQ-05, REQ-07, REQ-53, UC-005, UC-021 | Trạng thái theo GL-22 |
| GL-26 | Xe thất lạc | Lost Bike | Xe thuộc một chuyến đi kéo dài quá thời hạn tối đa của chuyến. | Không có | REQ-28, UC-009 | Thời hạn ở BR-09 |

## 3. Ứng viên không đưa vào

| Ứng viên | Lý do không đưa vào | Nơi xuất hiện |
|---|---|---|
| Tài khoản, tài khoản nhân viên | Thuật ngữ kỹ thuật dùng đúng nghĩa thông thường | REQ-02, REQ-54 |
| Đăng nhập, đăng ký | Thuật ngữ kỹ thuật phần mềm | REQ-02, REQ-05 |
| Bản đồ trạm | Tên use case UC-004 | REQ-05 |
| Lịch sử chuyến đi | Tên use case UC-016; là danh sách Chuyến đi | REQ-47 |
| Điều chỉnh cước | Tên use case UC-017 | REQ-48 |
| Xưởng | Từ phổ thông, nơi sửa xe, không có tương tác với hệ thống | REQ-40 |
| Kết quả sửa chữa | Nguồn không nêu thành phần; ghi nhận ở UC-011 | REQ-39 |
| Doanh thu, thời lượng trung bình, số xe hỏng | Thành phần của GL-02 | REQ-57 |
| Loại hỏng hóc | Thành phần của GL-03 | REQ-35 |
| Chuyến, xe đạp, ụ, dock, số tiền tạm giữ, lệnh tạm giữ, người dùng | Đồng nghĩa của GL-04, GL-25, GL-23, GL-08, GL-13 | Nguồn |
| Cổng thanh toán, ngân hàng đối tác | Tên tác nhân ACT-07, không cần định nghĩa phân biệt | REQ-03, REQ-62 |
| MQTT | Giao thức kỹ thuật (Giao tiếp ngoài, P06) | REQ-63 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-26 | "Hoàn lại phần dư" sau khi thu cước là (a) hoàn tiền qua API hoàn tiền, hay (b) huỷ phần tạm giữ còn lại qua API huỷ tạm giữ? | GL-07, GL-08, UC-007 bước 6 | Mục 4 "hoàn lại phần dư"; Mục 14 liệt kê cả "huỷ tạm giữ" và "hoàn tiền" |
| Q-27 | Xe có những trạng thái nào? "Thu hồi về xưởng" và "thất lạc" có phải là trạng thái của xe không? (Có / Không cho từng giá trị) | GL-22, GL-26, UC-011, UC-009 | Mục 6, Mục 7, Mục 8 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-005 luồng 6a2 | Dùng "lệnh tạm giữ tiền", đồng nghĩa không dùng của GL-08 | Đổi thành "Yêu cầu Cổng thanh toán huỷ khoản tạm giữ." |
| P04 | UC-005 activity A-6a2 | Nhãn "Yêu cầu huỷ lệnh tạm giữ" | Đổi thành "Yêu cầu huỷ khoản tạm giữ" |

## Vấn đề còn mở

- GL-13: nguồn gọi vai trò này là "người dùng" ở mọi mục; theo F4 mục 2 và 3 thuật ngữ chính thức phải là "Người dùng". P01 đã chốt tên tác nhân "Người thuê xe" vì quy tắc đặt tên của P01 coi "Người dùng" là tên quá chung khi hệ thống có nhiều vai trò. Đã chọn "Người thuê xe" (F4 mục 5) để không mâu thuẫn với P01; thứ tự ưu tiên của F4 không cho phép lựa chọn này.
- Số thuật ngữ (26) trong khoảng 15-50 của F2.
