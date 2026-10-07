# P01 - Xác định tác nhân - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P01 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md 1.0; yeu-cau-xe-dap.md |
| Phạm vi | Toàn hệ thống |

## Mục 1. Ranh giới hệ thống

Hệ thống cần xây dựng là phần mềm CityBike quản lý việc thuê và trả xe, gồm máy chủ trung tâm và ứng dụng di động cho người dùng.

| Thành phần | Trong / Ngoài / Chờ Q-nn | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
|---|---|---|---|
| Ứng dụng di động của người dùng | Trong | REQ-01; "Công ty cần phần mềm quản lý việc thuê và trả xe" (đoạn mở đầu) | Là thành phần nội bộ, không phải tác nhân |
| Máy chủ trung tâm | Trong | "kết nối về máy chủ trung tâm" (đoạn mở đầu); REQ-63 | Là thành phần nội bộ, không phải tác nhân |
| Dữ liệu tài khoản, chuyến đi, xe, trạm, lệnh điều chuyển | Trong | REQ-02, REQ-13, REQ-44, REQ-51 đến REQ-55 | Là thành phần nội bộ, không phải tác nhân |
| Ụ khoá (đầu đọc mã QR, khoá điện) | Ngoài | REQ-18, REQ-63: thiết bị có giao thức do nhà cung cấp quy định | Là tác nhân ACT-08 |
| Cổng thanh toán của ngân hàng đối tác | Ngoài | REQ-03, REQ-62 | Là tác nhân ACT-07 |
| Kênh gửi email hoá đơn | Chờ Q-19 | REQ-24: nguồn chỉ nói "gửi hoá đơn qua email", không nêu đây là hệ thống bên ngoài | Chờ trả lời Q-19 |
| Thiết bị đọc thẻ nhân viên | Chờ Q-07 | REQ-46: nguồn không nói ụ đọc thẻ nhân viên bằng thiết bị nào | Chờ trả lời Q-07 |

## Mục 2. Bảng tác nhân

| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |
|---|---|---|---|---|---|---|---|---|
| ACT-01 | Người thuê xe | Rider | Người | Chính | Người dùng ứng dụng di động của CityBike để thuê và trả xe; nguồn gọi là "người dùng". Gồm cả người chưa đăng nhập khi xem bản đồ trạm. | Đăng ký tài khoản và liên kết thẻ thanh toán<br>Xem bản đồ trạm<br>Thuê xe và trả xe<br>Xin thêm thời gian miễn phí khi trạm đến đầy<br>Báo xe hỏng | - | REQ-01 đến REQ-05, REQ-07, REQ-17, REQ-25, REQ-33 |
| ACT-02 | Nhân viên chăm sóc khách hàng | Customer Support Agent | Người | Chính | Nhân viên CityBike hỗ trợ người thuê xe qua hệ thống. | Tra cứu lịch sử chuyến đi<br>Điều chỉnh cước<br>Mở khoá tài khoản<br>Xử lý xe thất lạc | - | REQ-32, REQ-47 đến REQ-50 |
| ACT-03 | Nhân viên bảo trì | Maintenance Technician | Người | Chính | Nhân viên CityBike kiểm tra và sửa chữa xe bị báo hỏng. | Xem xe chờ kiểm tra<br>Ghi nhận kết quả sửa chữa và trạng thái xe | - | REQ-38, REQ-39, REQ-40 |
| ACT-04 | Nhân viên điều phối | Dispatcher | Người | Chính | Nhân viên CityBike cân bằng số xe giữa các trạm. | Xem trạm sắp hết xe, sắp đầy<br>Lập lệnh điều chuyển<br>Theo dõi lệnh điều chuyển | - | REQ-41, REQ-44, REQ-45 |
| ACT-05 | Quản trị viên | Administrator | Người | Chính | Người quản trị dữ liệu danh mục của hệ thống. | Quản lý trạm, ụ khoá, xe<br>Quản lý tài khoản nhân viên<br>Quản lý bảng giá cước | - | REQ-51 đến REQ-55 |
| ACT-06 | Ban giám đốc | Management Board | Người | Chính | Lãnh đạo CityBike xem báo cáo vận hành. | Xem báo cáo hằng tuần | - | REQ-56, REQ-57 |
| ACT-07 | Cổng thanh toán | Payment Gateway | Hệ thống ngoài | Phụ | Cổng thanh toán của ngân hàng đối tác, cung cấp API; gộp tên "ngân hàng đối tác". | Cung cấp: liên kết thẻ và cấp mã tham chiếu thẻ<br>Cung cấp: tạm giữ tiền, thu tiền từ khoản tạm giữ, huỷ tạm giữ, hoàn tiền | - | REQ-03, REQ-10, REQ-15, REQ-22, REQ-23, REQ-30, REQ-48, REQ-61, REQ-62 |
| ACT-08 | Ụ khoá | Dock | Thiết bị | Chính và phụ | Thiết bị tại trạm có đầu đọc mã QR và khoá điện, giao tiếp với máy chủ qua MQTT theo quy định của nhà cung cấp. | Báo: xe được rút ra, xe được đưa vào (kể cả khi nhân viên dùng thẻ nhân viên)<br>Cung cấp: mở khoá, khoá lại ụ | - | REQ-12, REQ-13, REQ-14, REQ-18, REQ-46, REQ-63 |
| ACT-09 | Bộ định thời | Timer | Thời gian | Chính | Đại diện sự kiện theo thời gian không có người khởi xướng. | Kích hoạt: khi một chuyến đi đạt thời hạn tối đa 24 giờ | - | REQ-28, REQ-29 |

## Mục 3. Bên liên quan không phải tác nhân

| SH | Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
|---|---|---|---|---|
| SH-01 | Công ty CityBike | Quản lý việc thuê và trả xe tại các trạm | Báo cáo do ACT-06 xem; các vai trò nhân viên | Đoạn mở đầu |
| SH-11 | Nhà cung cấp thiết bị ụ khoá | Giao thức MQTT được tuân thủ | ACT-08 Ụ khoá | REQ-63 |
| SH-08 | Nhân viên lấy, đưa xe bằng thẻ nhân viên | Lệnh điều chuyển được cập nhật khi lấy, đưa xe | ACT-08 Ụ khoá (quẹt thẻ nhân viên) | REQ-46 |
| SH-03 | Người thuê xe khi nhận hoá đơn | Nhận hoá đơn chuyến đi | Kênh email (Q-19) | REQ-24 |

## Mục 4. Ứng viên tác nhân bị loại

| Ứng viên | Lý do loại | REQ |
|---|---|---|
| Người dùng chưa đăng nhập | Gộp vào ACT-01 Người thuê xe: chỉ có mục tiêu xem bản đồ, là tập con mục tiêu của ACT-01 | REQ-05 |
| Ngân hàng đối tác | Gộp vào ACT-07 Cổng thanh toán: nguồn chỉ nêu tương tác qua cổng thanh toán | REQ-03, REQ-62 |
| Nhân viên lấy, đưa xe bằng thẻ nhân viên | A-T2: chỉ thao tác trên ụ khoá; hệ thống nhận sự kiện từ ACT-08; vai trò cụ thể chờ Q-07 (xếp vào Mục 3) | REQ-46 |
| Nhà cung cấp thiết bị | A-T2: không tương tác với hệ thống, chỉ quy định giao thức (xếp vào Mục 3) | REQ-63 |
| Máy chủ trung tâm | A-T1: thành phần nội bộ | Đoạn mở đầu |
| Ứng dụng di động | A-T1: thành phần nội bộ | REQ-01 |
| Xưởng | A-T2, A-T6: là nơi đưa xe về, không có tương tác với hệ thống | REQ-40 |
| Bộ định thời 60 giây chờ rút xe | A-T4: thời hạn chờ là một phần của chuyến thuê đang diễn ra, không phải sự kiện độc lập có mục tiêu riêng | REQ-14, REQ-15, REQ-16 |
| Bộ định thời báo cáo hằng tuần | A-T6: nguồn chỉ nói Ban giám đốc xem báo cáo hằng tuần, không nói hệ thống tự lập báo cáo theo lịch | REQ-56 |
| Công ty CityBike | A-T2: không thao tác trên hệ thống (xếp vào Mục 3) | Đoạn mở đầu |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-19 | Hoá đơn được gửi qua một dịch vụ email bên ngoài (tác nhân phụ) hay do hệ thống tự gửi? (Dịch vụ ngoài / Tự gửi) | Ranh giới, tác nhân phụ của UC trả xe | "gửi hoá đơn qua email" (Mục 4) |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Trả xe: người thuê xe là người muốn trả xe, nhưng thông tin tới hệ thống do ACT-08 Ụ khoá gửi (REQ-18). Phép thử A-T2 và phép thử "Ai muốn điều này xảy ra và bắt đầu nó?" cho hai câu trả lời khác nhau (người thuê xe muốn, ụ khoá bắt đầu). ACT-01 vẫn giữ mục tiêu "Thuê xe và trả xe"; tác nhân chính của use case trả xe quyết định ở P02.
- ACT-02 có mục tiêu "Xử lý xe thất lạc" dựa trên REQ-32, nội dung chờ Q-03.
