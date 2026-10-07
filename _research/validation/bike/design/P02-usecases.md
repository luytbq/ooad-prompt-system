# P02 - Xác định use case - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md 1.0; P01-actors.md 1.0; yeu-cau-xe-dap.md |
| Phạm vi | Toàn hệ thống |

## Mục 1. Danh sách mục tiêu tác nhân

| ACT | Mục tiêu | Mức mục tiêu dự kiến | REQ | CAND |
|---|---|---|---|---|
| ACT-01 Người thuê xe | Đăng ký tài khoản | User-goal | REQ-02 | CAND-01 |
| ACT-01 | Liên kết thẻ thanh toán | User-goal | REQ-03, REQ-04 | CAND-02 |
| ACT-01 | Xem bản đồ trạm để biết trạm nào có xe, có ụ trống | User-goal | REQ-05 | CAND-03 |
| ACT-01 | Thuê xe và trả xe | Summary | REQ-07, REQ-17 | CAND-04 |
| ACT-01 | Thuê xe | User-goal | REQ-07 đến REQ-16 | CAND-05 |
| ACT-01 | Trả xe | User-goal | REQ-17 đến REQ-24 | CAND-06 |
| ACT-01 | Xin thêm thời gian miễn phí khi trạm đến đầy | User-goal | REQ-25, REQ-26, REQ-27 | CAND-07 |
| ACT-01 | Báo xe hỏng | User-goal | REQ-33 đến REQ-37 | CAND-08 |
| ACT-01 | Đăng nhập | Subfunction | REQ-05 (ngụ ý) | CAND-39 |
| ACT-02 Nhân viên chăm sóc khách hàng | Tra cứu lịch sử chuyến đi của người dùng | User-goal | REQ-47 | CAND-09 |
| ACT-02 | Điều chỉnh cước | User-goal | REQ-48, REQ-49 | CAND-10 |
| ACT-02 | Mở khoá tài khoản | User-goal | REQ-50 | CAND-11 |
| ACT-02 | Xử lý xe thất lạc | Chưa rõ (Q-03) | REQ-32 | CAND-12 |
| ACT-03 Nhân viên bảo trì | Xem danh sách xe chờ kiểm tra theo trạm | User-goal | REQ-38 | CAND-13 |
| ACT-03 | Ghi nhận kết quả sửa chữa | User-goal | REQ-39 | CAND-14 |
| ACT-03 | Chuyển xe về sẵn sàng hoặc thu hồi về xưởng | Subfunction | REQ-40 | CAND-15 |
| ACT-04 Nhân viên điều phối | Xem trạm sắp hết xe, sắp đầy | User-goal | REQ-41 | CAND-16 |
| ACT-04 | Lập lệnh điều chuyển | User-goal | REQ-44 | CAND-17 |
| ACT-04 | Theo dõi lệnh điều chuyển | User-goal | REQ-45 | CAND-18 |
| ACT-04 | Điều chuyển xe giữa các trạm | Summary | REQ-44, REQ-45, REQ-46 | CAND-19 |
| ACT-05 Quản trị viên | Quản lý trạm | User-goal | REQ-51 | CAND-20 |
| ACT-05 | Quản lý ụ khoá | User-goal | REQ-52 | CAND-21 |
| ACT-05 | Quản lý xe | User-goal | REQ-53 | CAND-22 |
| ACT-05 | Quản lý tài khoản nhân viên | User-goal | REQ-54 | CAND-23 |
| ACT-05 | Quản lý bảng giá cước | User-goal | REQ-55 | CAND-24 |
| ACT-06 Ban giám đốc | Xem báo cáo hằng tuần | User-goal | REQ-56 | CAND-25 |
| ACT-08 Ụ khoá | Báo xe được rút ra | Subfunction | REQ-13 | CAND-28 |
| ACT-08 | Báo xe được đưa vào | Subfunction | REQ-18 | CAND-30 |
| ACT-08 | Báo xe được lấy ra, đưa vào bằng thẻ nhân viên | User-goal | REQ-46 | CAND-26 |
| ACT-09 Bộ định thời | Coi xe là thất lạc khi chuyến quá 24 giờ | User-goal | REQ-28 đến REQ-31 | CAND-27 |

## Mục 2. Danh sách sự kiện

| EV | Sự kiện | Loại | Nguồn phát (ACT) | Phản hồi mong đợi của hệ thống | REQ | CAND |
|---|---|---|---|---|---|---|
| EV-01 | Người muốn dùng dịch vụ thuê xe chưa có tài khoản | Nghiệp vụ | ACT-01 | Tạo tài khoản | REQ-02 | CAND-01 |
| EV-02 | Người thuê xe muốn đủ điều kiện thuê xe | Nghiệp vụ | ACT-01 | Liên kết thẻ qua cổng thanh toán | REQ-03 | CAND-02 |
| EV-03 | Người muốn biết trạm nào có xe, có ụ trống | Nghiệp vụ | ACT-01 | Hiển thị bản đồ trạm | REQ-05 | CAND-03 |
| EV-04 | Người thuê xe đứng tại trạm muốn lấy xe | Nghiệp vụ | ACT-01 | Kiểm tra, tạm giữ tiền, mở khoá ụ | REQ-07 | CAND-05 |
| EV-05 | Ụ khoá báo xe đã được rút ra | Hệ thống ngoài (thiết bị) | ACT-08 | Bắt đầu chuyến đi | REQ-13 | CAND-28 |
| EV-06 | Hết 60 giây mà ụ chưa báo xe được rút | Thời gian | - | Khoá lại ụ, huỷ tạm giữ | REQ-14, REQ-15, REQ-16 | CAND-29 |
| EV-07 | Ụ khoá báo đã nhận xe được đẩy vào | Hệ thống ngoài (thiết bị) | ACT-08 | Kết thúc chuyến, tính và thu cước, hoàn dư, gửi hoá đơn | REQ-18 đến REQ-24 | CAND-06, CAND-30 |
| EV-08 | Người thuê xe tới trạm không còn ụ trống | Nghiệp vụ | ACT-01 | Cộng thêm 15 phút miễn phí | REQ-25 | CAND-07 |
| EV-09 | Một chuyến đi đạt 24 giờ | Thời gian | ACT-09 | Coi xe thất lạc, thu toàn bộ tạm giữ, khoá tài khoản | REQ-28 | CAND-27 |
| EV-10 | Người thuê xe phát hiện xe hỏng khi trả hoặc trong 10 phút sau khi trả | Nghiệp vụ | ACT-01 | Ghi nhận báo hỏng, đánh dấu xe "Chờ kiểm tra" | REQ-33 | CAND-08 |
| EV-11 | Nhân viên bảo trì cần biết xe nào chờ kiểm tra | Nghiệp vụ | ACT-03 | Danh sách xe chờ kiểm tra theo trạm | REQ-38 | CAND-13 |
| EV-12 | Nhân viên bảo trì kiểm tra, sửa xong một xe | Nghiệp vụ | ACT-03 | Ghi kết quả, đổi trạng thái xe | REQ-39, REQ-40 | CAND-14, CAND-15 |
| EV-13 | Nhân viên điều phối cần biết trạm nào sắp hết xe, sắp đầy | Nghiệp vụ | ACT-04 | Danh sách trạm theo ngưỡng | REQ-41 | CAND-16 |
| EV-14 | Nhân viên điều phối quyết định chuyển xe giữa hai trạm | Nghiệp vụ | ACT-04 | Tạo lệnh điều chuyển | REQ-44 | CAND-17 |
| EV-15 | Ụ khoá báo xe được lấy ra hoặc đưa vào bằng thẻ nhân viên | Hệ thống ngoài (thiết bị) | ACT-08 | Cập nhật lệnh điều chuyển | REQ-46 | CAND-26 |
| EV-16 | Nhân viên điều phối cần biết tiến độ lệnh điều chuyển | Nghiệp vụ | ACT-04 | Trạng thái lệnh điều chuyển | REQ-45 | CAND-18 |
| EV-17 | Nhân viên chăm sóc khách hàng cần thông tin chuyến đi của một người dùng | Nghiệp vụ | ACT-02 | Lịch sử chuyến đi | REQ-47 | CAND-09 |
| EV-18 | Nhân viên chăm sóc khách hàng quyết định hoàn cước | Nghiệp vụ | ACT-02 | Hoàn tiền qua cổng thanh toán, ghi lý do | REQ-48 | CAND-10 |
| EV-19 | Nhân viên chăm sóc khách hàng quyết định mở khoá một tài khoản | Nghiệp vụ | ACT-02 | Tài khoản được mở khoá | REQ-50 | CAND-11 |
| EV-20 | Có thay đổi về trạm, ụ khoá, xe, nhân viên, giá cước | Nghiệp vụ | ACT-05 | Cập nhật danh mục tương ứng | REQ-51 đến REQ-55 | CAND-20 đến CAND-24 |
| EV-21 | Ban giám đốc cần số liệu vận hành trong tuần | Nghiệp vụ | ACT-06 | Báo cáo hằng tuần | REQ-56 | CAND-25 |

## Mục 3. Bảng ứng viên use case

| CAND | Ứng viên | Kết luận | Phép thử không đạt | Lý do | REQ | Nguồn phát hiện |
|---|---|---|---|---|---|---|
| CAND-01 | Đăng ký tài khoản | Giữ thành UC-001 | - | U-R03: UC User-goal của tác nhân sẽ sở hữu tài khoản | REQ-02 | Mục tiêu, EV-01 |
| CAND-02 | Liên kết thẻ thanh toán | Giữ thành UC-002 | - | Kết quả riêng (tài khoản đủ điều kiện thuê), có tác nhân phụ và quy tắc riêng (REQ-04, REQ-61) | REQ-03, REQ-04 | Mục tiêu, EV-02 |
| CAND-03 | Xem bản đồ trạm | Giữ thành UC-004 | - | U-R05: mục tiêu thông tin độc lập, dùng cả khi chưa đăng nhập | REQ-05 | Mục tiêu, EV-03 |
| CAND-04 | Thuê xe và trả xe | Tách thành CAND-05, CAND-06 | U-T1, U-T6, U-AP05 | Hai thời điểm cách nhau cả chuyến đi | REQ-07, REQ-17 | Mục tiêu (P01) |
| CAND-05 | Thuê xe | Giữ thành UC-005 | - | Một phiên tại trạm, kết quả là chuyến đi bắt đầu | REQ-07 đến REQ-16 | Mục tiêu, EV-04 |
| CAND-06 | Trả xe | Giữ thành UC-007 | - | Kết quả là chuyến kết thúc, cước được thu; tác nhân chính xem Vấn đề còn mở | REQ-17 đến REQ-24 | Mục tiêu, EV-07 |
| CAND-07 | Xin thêm thời gian miễn phí | Giữ thành UC-006 | - | Mục tiêu riêng trong lúc đang đi, có quy tắc riêng (REQ-26, REQ-27) | REQ-25, REQ-26, REQ-27 | Mục tiêu, EV-08 |
| CAND-08 | Báo xe hỏng | Giữ thành UC-008 | - | Có thể làm tới 10 phút sau khi trả xe, kết quả riêng là xe bị chặn cho thuê | REQ-33 đến REQ-37 | Mục tiêu, EV-10 |
| CAND-09 | Tra cứu lịch sử chuyến đi | Giữ thành UC-016 | - | U-R05, U-R17 | REQ-47 | Mục tiêu, EV-17 |
| CAND-10 | Điều chỉnh cước | Giữ thành UC-017 | - | Giao dịch có quy tắc riêng (REQ-49) và tác nhân phụ | REQ-48, REQ-49 | Mục tiêu, EV-18 |
| CAND-11 | Mở khoá tài khoản | Giữ thành UC-018 | - | Kết quả riêng: người dùng được dùng dịch vụ trở lại | REQ-50 | Mục tiêu, EV-19 |
| CAND-12 | Xử lý xe thất lạc (nhân viên chăm sóc khách hàng) | Chờ Q-03 | - | Nếu Q-03 trả lời (b), ứng viên thành UC của ACT-02; nếu (a), nội dung đã nằm trong UC-016, UC-017, UC-018 | REQ-32 | Mục tiêu |
| CAND-13 | Xem danh sách xe chờ kiểm tra theo trạm | Giữ thành UC-010 | - | U-R05: phục vụ việc đi kiểm tra xe ngoài hệ thống, không phải bước của UC khác | REQ-38 | Mục tiêu, EV-11 |
| CAND-14 | Ghi nhận kết quả sửa chữa | Giữ thành UC-011 | - | Kết quả: xe có kết quả kiểm tra và trạng thái mới | REQ-39 | Mục tiêu, EV-12 |
| CAND-15 | Chuyển xe về sẵn sàng hoặc thu hồi về xưởng | Gộp vào UC-011 | U-T4, U-AP01 | Cùng tác nhân, cùng phiên với ghi nhận kết quả | REQ-40 | Mục tiêu, EV-12 |
| CAND-16 | Xem trạm sắp hết xe, sắp đầy | Giữ thành UC-012 | - | U-R05: thông tin phục vụ quyết định điều chuyển | REQ-41, REQ-42, REQ-43 | Mục tiêu, EV-13 |
| CAND-17 | Lập lệnh điều chuyển | Giữ thành UC-013 | - | Giao dịch nghiệp vụ | REQ-44 | Mục tiêu, EV-14 |
| CAND-18 | Theo dõi lệnh điều chuyển | Giữ thành UC-015 | - | U-R05 | REQ-45 | Mục tiêu, EV-16 |
| CAND-19 | Điều chuyển xe giữa các trạm | Tách thành CAND-17, CAND-18, CAND-26 | U-T1, U-T6, U-AP04 | Nhiều phiên, nhiều tác nhân | REQ-44, REQ-45, REQ-46 | Mục tiêu |
| CAND-20 | Quản lý trạm | Giữ thành UC-019 | - | U-R04: dữ liệu danh mục, một tác nhân | REQ-51 | Mục tiêu, EV-20 |
| CAND-21 | Quản lý ụ khoá | Giữ thành UC-020 | - | U-R04: mỗi loại dữ liệu một UC | REQ-52 | Mục tiêu, EV-20 |
| CAND-22 | Quản lý xe | Giữ thành UC-021 | - | U-R04 | REQ-53 | Mục tiêu, EV-20 |
| CAND-23 | Quản lý tài khoản nhân viên | Giữ thành UC-022 | - | U-R04, U-R15 | REQ-54 | Mục tiêu, EV-20 |
| CAND-24 | Quản lý bảng giá cước | Giữ thành UC-023 | - | U-R15 | REQ-55 | Mục tiêu, EV-20 |
| CAND-25 | Xem báo cáo hằng tuần | Giữ thành UC-024 | - | U-R05 | REQ-56, REQ-57 | Mục tiêu, EV-21 |
| CAND-26 | Ghi nhận xe điều chuyển tại ụ | Giữ thành UC-014 | U-T4 (bị U-R08 ghi đè) | U-R08: ụ khoá tự gửi sự kiện vào thời điểm nhân viên thao tác, không thuộc phiên của UC nào khác | REQ-46 | Sự kiện EV-15 |
| CAND-27 | Ghi nhận xe thất lạc | Giữ thành UC-009 | - | U-R07: thời điểm nguồn nêu rõ (quá 24 giờ), không có người ra lệnh, kết quả có giá trị cho công ty | REQ-28 đến REQ-31 | Sự kiện EV-09 |
| CAND-28 | Ụ báo xe được rút ra, bắt đầu chuyến | Là bước của UC-005 | U-T4, U-AP03 | U-R08: phản hồi trong cùng phiên thuê xe | REQ-13 | Sự kiện EV-05 |
| CAND-29 | Khoá lại ụ và huỷ tạm giữ khi quá 60 giây | Là bước của UC-005 | U-T6, U-AP11 | U-R09: hệ quả của lượt thuê đang diễn ra trong cùng phiên, người thuê vẫn đứng tại ụ | REQ-14, REQ-15, REQ-16 | Sự kiện EV-06 |
| CAND-30 | Ụ báo nhận xe | Gộp vào UC-007 | U-T4 | Là sự kiện kích hoạt của UC-007 | REQ-18 | Sự kiện EV-07 |
| CAND-31 | Kiểm tra không có chuyến đang diễn ra và không nợ cước | Là bước của UC-005 | U-T9, U-AP03 | Kiểm tra nội bộ | REQ-08, REQ-09 | Động từ |
| CAND-32 | Tạm giữ tiền | Là bước của UC-005 | U-T4, U-AP03 | Q4 d không thoả vế thứ ba: nguồn không nói tạm giữ thất bại thì làm lại được (Q-08) | REQ-10, REQ-11 | Động từ |
| CAND-33 | Gửi lệnh mở khoá tới ụ | Là bước của UC-005 | U-T9, U-AP03 | Việc hệ thống làm trong UC-005 | REQ-12 | Động từ |
| CAND-34 | Tính cước | Là bước của UC-007 | U-T9, U-AP03 | Tính toán nội bộ | REQ-20, REQ-21 | Động từ |
| CAND-35 | Thu cước và hoàn phần dư | Là bước của UC-007 | U-T9, U-AP03 | U-R08: lời gọi cổng thanh toán trong UC-007 | REQ-22, REQ-23 | Động từ |
| CAND-36 | Gửi hoá đơn qua email | Là bước của UC-007 | U-AP03 | U-R06 | REQ-24 | Động từ |
| CAND-37 | Thu toàn bộ tạm giữ và khoá tài khoản | Là bước của UC-009 | U-T9, U-AP03 | Hệ quả của UC-009 | REQ-30, REQ-31 | Động từ |
| CAND-38 | Đánh dấu xe "Chờ kiểm tra" | Là bước của UC-008 | U-T9, U-AP03 | Hệ quả của báo hỏng | REQ-36, REQ-37 | Động từ |
| CAND-39 | Đăng nhập | Giữ thành UC-003 | U-T3 (bị U-R01 ghi đè) | U-R01: nguồn suy ra trực tiếp là có xác thực ("Việc xem bản đồ không cần đăng nhập"; "tài khoản nhân viên"); Q-01 xác nhận phạm vi | REQ-05, REQ-54 | Mục tiêu |
| CAND-40 | Thanh toán nợ cước | Chờ Q-02 | - | Nếu Q-02 trả lời (b), ứng viên thành UC của ACT-01 | REQ-09 | Động từ |
| CAND-41 | Kết thúc chuyến đi | Là bước của UC-007 | U-T9, U-AP03 | Hệ quả của sự kiện ụ nhận xe | REQ-19 | Động từ |

## Mục 4. Bảng use case

| UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | Nhóm chức năng | REQ | Mức | CAND nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UC-001 | Đăng ký tài khoản | Register Account | ACT-01 Người thuê xe | - | Người thuê xe có tài khoản gắn email và số điện thoại. | Người thuê xe tạo tài khoản bằng email và số điện thoại. | Người muốn dùng dịch vụ (EV-01) | Tài khoản | REQ-02 | User-goal | CAND-01 |
| UC-002 | Liên kết thẻ thanh toán | Link Payment Card | ACT-01 | ACT-07 Cổng thanh toán | Tài khoản của người thuê xe có một thẻ thanh toán được liên kết và đủ điều kiện thuê xe. | Người thuê xe liên kết một thẻ qua cổng thanh toán; hệ thống chỉ lưu mã tham chiếu do cổng cấp. | Người thuê xe muốn đủ điều kiện thuê (EV-02) | Tài khoản | REQ-03, REQ-04, REQ-61, REQ-62 | User-goal | CAND-02 |
| UC-003 | Đăng nhập | Log In | ACT-01, ACT-02, ACT-03, ACT-04, ACT-05, ACT-06 | - | Tác nhân được xác thực để dùng các chức năng cần tài khoản. | Điều kiện để dùng các UC khác trừ UC-001, UC-004 (U-R01). | Tác nhân muốn dùng chức năng cần tài khoản | Tài khoản | REQ-05, REQ-54 | Subfunction | CAND-39 |
| UC-004 | Xem bản đồ trạm | View Station Map | ACT-01 | - | Người thuê xe biết số xe sẵn sàng và số ụ trống của từng trạm. | Người thuê xe, kể cả chưa đăng nhập, xem bản đồ các trạm với số xe sẵn sàng và số ụ trống. | Người muốn biết trạm có xe, có ụ trống (EV-03) | Thuê trả xe | REQ-05, REQ-06 | User-goal | CAND-03 |
| UC-005 | Thuê xe | Rent Bike | ACT-01 | ACT-07, ACT-08 Ụ khoá | Người thuê xe lấy được xe ra khỏi ụ và chuyến đi bắt đầu. | Người thuê xe quét mã QR trên ụ; hệ thống kiểm tra điều kiện, tạm giữ tiền, mở khoá ụ; chuyến bắt đầu khi xe được rút, hoặc ụ bị khoá lại và tạm giữ bị huỷ khi quá 60 giây. | Người thuê xe tại trạm muốn lấy xe (EV-04) | Thuê trả xe | REQ-04, REQ-07 đến REQ-16, REQ-58 | User-goal | CAND-05, CAND-28, CAND-29, CAND-31, CAND-32, CAND-33 |
| UC-006 | Xin thêm thời gian miễn phí | Request Extra Free Time | ACT-01 | - | Chuyến đi của người thuê xe được cộng thêm 15 phút miễn phí để tới trạm khác. | Người thuê xe đang đi, tới trạm không còn ụ trống, yêu cầu thêm 15 phút miễn phí; mỗi chuyến một lần. | Trạm đến không còn ụ trống (EV-08) | Thuê trả xe | REQ-25, REQ-26, REQ-27 | User-goal | CAND-07 |
| UC-007 | Trả xe | Return Bike | ACT-01 | ACT-08, ACT-07 | Chuyến đi của người thuê xe kết thúc, cước được thu từ tiền tạm giữ, phần dư được hoàn và hoá đơn được gửi. | Người thuê xe đẩy xe vào một ụ trống ở trạm bất kỳ; ụ báo nhận xe; hệ thống kết thúc chuyến, tính cước, thu cước, hoàn phần dư, gửi hoá đơn qua email. | Ụ khoá báo đã nhận xe (EV-07) | Thuê trả xe | REQ-17 đến REQ-24, REQ-63 | User-goal | CAND-06, CAND-30, CAND-34, CAND-35, CAND-36, CAND-41 |
| UC-008 | Báo xe hỏng | Report Damaged Bike | ACT-01 | - | Xe hỏng được ghi nhận và không còn được cho thuê. | Người thuê xe báo xe hỏng khi trả hoặc trong 10 phút sau khi trả, chọn loại hỏng hóc và mô tả; xe chuyển sang "Chờ kiểm tra". | Phát hiện xe hỏng (EV-10) | Thuê trả xe | REQ-33 đến REQ-37 | User-goal | CAND-08, CAND-38 |
| UC-009 | Ghi nhận xe thất lạc | Record Lost Bike | ACT-09 Bộ định thời | ACT-07 | Công ty thu toàn bộ tiền tạm giữ của chuyến quá 24 giờ và tài khoản người thuê bị khoá chờ xử lý. | Khi một chuyến đi quá 24 giờ, hệ thống coi xe là thất lạc, thu toàn bộ tiền tạm giữ, khoá tài khoản. | Chuyến đi đạt 24 giờ (EV-09) | Thuê trả xe | REQ-28 đến REQ-31 | User-goal | CAND-27, CAND-37 |
| UC-010 | Tra cứu xe chờ kiểm tra | Look Up Bikes Awaiting Inspection | ACT-03 Nhân viên bảo trì | - | Nhân viên bảo trì biết các xe chờ kiểm tra ở từng trạm. | Nhân viên bảo trì xem danh sách xe "Chờ kiểm tra" theo trạm. | Cần biết xe chờ kiểm tra (EV-11) | Bảo trì | REQ-38 | User-goal | CAND-13 |
| UC-011 | Ghi nhận kết quả kiểm tra xe | Record Bike Inspection Result | ACT-03 | - | Xe có kết quả sửa chữa được ghi nhận và ở trạng thái sẵn sàng hoặc thu hồi về xưởng. | Nhân viên bảo trì ghi kết quả sửa chữa và chuyển xe về sẵn sàng hoặc thu hồi về xưởng. | Kiểm tra, sửa xong xe (EV-12) | Bảo trì | REQ-39, REQ-40 | User-goal | CAND-14, CAND-15 |
| UC-012 | Xem trạm sắp hết xe, sắp đầy | View Low And Full Stations | ACT-04 Nhân viên điều phối | - | Nhân viên điều phối biết các trạm cần điều chuyển xe. | Nhân viên điều phối xem các trạm dưới 20% hoặc trên 90% số ụ có xe. | Cần biết trạm mất cân bằng (EV-13) | Điều phối | REQ-41, REQ-42, REQ-43 | User-goal | CAND-16 |
| UC-013 | Lập lệnh điều chuyển | Create Transfer Order | ACT-04 | - | Có lệnh điều chuyển xe giữa hai trạm được ghi nhận. | Nhân viên điều phối lập lệnh điều chuyển xe giữa các trạm. | Quyết định chuyển xe (EV-14) | Điều phối | REQ-44 | User-goal | CAND-17 |
| UC-014 | Ghi nhận xe điều chuyển tại ụ | Record Transfer At Dock | ACT-08 Ụ khoá | - | Lệnh điều chuyển phản ánh đúng xe đã được lấy ra hoặc đưa vào. | Ụ khoá báo xe được lấy ra hoặc đưa vào bằng thẻ nhân viên; hệ thống cập nhật lệnh điều chuyển tương ứng. | Ụ báo thao tác bằng thẻ nhân viên (EV-15) | Điều phối | REQ-46, REQ-63 | User-goal | CAND-26 |
| UC-015 | Theo dõi lệnh điều chuyển | Track Transfer Order | ACT-04 | - | Nhân viên điều phối biết tiến độ của lệnh điều chuyển tới khi hoàn tất. | Nhân viên điều phối xem trạng thái các lệnh điều chuyển. | Cần biết tiến độ (EV-16) | Điều phối | REQ-45 | User-goal | CAND-18 |
| UC-016 | Tra cứu lịch sử chuyến đi | Look Up Trip History | ACT-02 Nhân viên chăm sóc khách hàng | - | Nhân viên chăm sóc khách hàng có thông tin chuyến đi của một người dùng. | Nhân viên chăm sóc khách hàng tìm người dùng và xem lịch sử chuyến đi. | Cần thông tin chuyến đi (EV-17) | Chăm sóc khách hàng | REQ-47 | User-goal | CAND-09 |
| UC-017 | Điều chỉnh cước | Adjust Fare | ACT-02 | ACT-07 | Người dùng được hoàn một phần hoặc toàn bộ cước, có lý do được ghi lại. | Nhân viên chăm sóc khách hàng hoàn tiền một phần hoặc toàn bộ cước của một chuyến, bắt buộc ghi lý do. | Quyết định hoàn cước (EV-18) | Chăm sóc khách hàng | REQ-48, REQ-49, REQ-62 | User-goal | CAND-10 |
| UC-018 | Mở khoá tài khoản | Unlock Account | ACT-02 | - | Tài khoản người dùng được dùng dịch vụ trở lại. | Nhân viên chăm sóc khách hàng mở khoá một tài khoản đang bị khoá. | Quyết định mở khoá (EV-19) | Chăm sóc khách hàng | REQ-50 | User-goal | CAND-11 |
| UC-019 | Quản lý trạm | Manage Stations | ACT-05 Quản trị viên | - | Danh mục trạm đúng với thực tế. | Quản trị viên quản lý thông tin trạm; thao tác cụ thể chờ Q-16. | Thay đổi về trạm (EV-20) | Danh mục | REQ-51 | User-goal | CAND-20 |
| UC-020 | Quản lý ụ khoá | Manage Docks | ACT-05 | - | Danh mục ụ khoá đúng với thực tế. | Quản trị viên quản lý thông tin ụ khoá; thao tác cụ thể chờ Q-16. | Thay đổi về ụ khoá (EV-20) | Danh mục | REQ-52 | User-goal | CAND-21 |
| UC-021 | Quản lý xe | Manage Bikes | ACT-05 | - | Danh mục xe đúng với thực tế. | Quản trị viên quản lý thông tin xe; thao tác cụ thể chờ Q-16. | Thay đổi về xe (EV-20) | Danh mục | REQ-53 | User-goal | CAND-22 |
| UC-022 | Quản lý tài khoản nhân viên | Manage Staff Accounts | ACT-05 | - | Nhân viên có tài khoản đúng vai trò. | Quản trị viên quản lý tài khoản nhân viên; thao tác cụ thể chờ Q-16. | Thay đổi về nhân viên (EV-20) | Danh mục | REQ-54 | User-goal | CAND-23 |
| UC-023 | Quản lý bảng giá cước | Manage Fare Table | ACT-05 | - | Bảng giá cước áp dụng đúng quy định của công ty. | Quản trị viên quản lý bảng giá cước; thao tác cụ thể chờ Q-16, quan hệ với REQ-21 chờ Q-15. | Thay đổi giá cước (EV-20) | Danh mục | REQ-55 | User-goal | CAND-24 |
| UC-024 | Xem báo cáo hằng tuần | View Weekly Report | ACT-06 Ban giám đốc | - | Ban giám đốc có số chuyến theo trạm, thời lượng trung bình, doanh thu, số xe hỏng của tuần. | Ban giám đốc xem báo cáo hằng tuần. | Cần số liệu tuần (EV-21) | Báo cáo | REQ-56, REQ-57 | User-goal | CAND-25 |

## Mục 5. Ma trận truy vết REQ --> UC

| REQ | Nội dung tóm tắt | UC phủ | Ghi chú |
|---|---|---|---|
| REQ-01 | Dùng qua ứng dụng di động | - | Chuyển P06 (Ràng buộc) |
| REQ-02 | Đăng ký tài khoản | UC-001 | Không có |
| REQ-03 | Liên kết thẻ | UC-002 | Không có |
| REQ-04 | Chỉ thuê khi đã liên kết thẻ | UC-005 | Tiền điều kiện của UC-005 |
| REQ-05 | Xem bản đồ không cần đăng nhập | UC-004 | Không có |
| REQ-06 | Bản đồ cập nhật thời gian thực | UC-004 | Chuyển P06 (Phi chức năng) |
| REQ-07 | Thuê xe bằng quét QR | UC-005 | Không có |
| REQ-08, REQ-09 | Không có chuyến đang diễn ra, không nợ cước | UC-005 | Quy tắc nghiệp vụ gắn UC-005 |
| REQ-10, REQ-11 | Tạm giữ 200.000 đồng | UC-005 | Không có |
| REQ-12, REQ-13 | Mở khoá, bắt đầu chuyến | UC-005 | Không có |
| REQ-14, REQ-15, REQ-16 | Quá 60 giây: khoá lại ụ, huỷ tạm giữ | UC-005 | Không có |
| REQ-17, REQ-18, REQ-19 | Trả xe, ụ báo nhận xe, kết thúc chuyến | UC-007 | Không có |
| REQ-20, REQ-21 | Tính cước, công thức cước | UC-007 | Không có |
| REQ-22, REQ-23, REQ-24 | Thu cước, hoàn dư, gửi hoá đơn | UC-007 | Không có |
| REQ-25, REQ-26, REQ-27 | Thêm 15 phút miễn phí, một lần | UC-006 | Không có |
| REQ-28 đến REQ-31 | Quá 24 giờ: thất lạc, thu tạm giữ, khoá tài khoản | UC-009 | Không có |
| REQ-32 | Chăm sóc khách hàng xử lý tiếp | - | Chờ Q-03 (CAND-12) |
| REQ-33 đến REQ-37 | Báo xe hỏng, "Chờ kiểm tra" | UC-008 | REQ-37 cũng là điều kiện của UC-005 |
| REQ-38 | Xem xe chờ kiểm tra | UC-010 | Không có |
| REQ-39, REQ-40 | Ghi kết quả, chuyển trạng thái | UC-011 | Không có |
| REQ-41, REQ-42, REQ-43 | Trạm sắp hết, sắp đầy | UC-012 | Không có |
| REQ-44 | Lập lệnh điều chuyển | UC-013 | Không có |
| REQ-45 | Theo dõi lệnh điều chuyển | UC-015 | Không có |
| REQ-46 | Tự cập nhật lệnh khi dùng thẻ nhân viên | UC-014 | Q-07 |
| REQ-47 | Tra cứu lịch sử chuyến | UC-016 | Không có |
| REQ-48, REQ-49 | Điều chỉnh cước, ghi lý do | UC-017 | Không có |
| REQ-50 | Mở khoá tài khoản | UC-018 | Không có |
| REQ-51 đến REQ-55 | Quản lý danh mục | UC-019 đến UC-023 | Q-16 |
| REQ-56, REQ-57 | Báo cáo hằng tuần | UC-024 | Không có |
| REQ-58 | Mở khoá trong 2 giây | UC-005 | Chuyển P06 (Phi chức năng) |
| REQ-59 | 1.500 chuyến đồng thời | - | Chuyển P06 |
| REQ-60 | Không lưu số thẻ | - | Chuyển P06 |
| REQ-61 | Chỉ lưu mã tham chiếu thẻ | UC-002 | Không có |
| REQ-62 | API cổng thanh toán | UC-002, UC-005, UC-007, UC-009, UC-017 | Không có |
| REQ-63 | MQTT với ụ khoá | UC-005, UC-007, UC-014 | Không có |

## Mục 6. Thống kê và nhận xét ngưỡng

| ACT | Số UC là tác nhân chính | Số UC là tác nhân phụ | Nhận xét |
|---|---|---|---|
| ACT-01 Người thuê xe | 8 (UC-001 đến UC-008) | 0 | Trong khoảng 2-12 |
| ACT-02 Nhân viên chăm sóc khách hàng | 4 (UC-003, UC-016, UC-017, UC-018) | 0 | Không có |
| ACT-03 Nhân viên bảo trì | 3 (UC-003, UC-010, UC-011) | 0 | Không có |
| ACT-04 Nhân viên điều phối | 4 (UC-003, UC-012, UC-013, UC-015) | 0 | Không có |
| ACT-05 Quản trị viên | 6 (UC-003, UC-019 đến UC-023) | 0 | Không có |
| ACT-06 Ban giám đốc | 2 (UC-003, UC-024) | 0 | Không có |
| ACT-07 Cổng thanh toán | 0 | 5 (UC-002, UC-005, UC-007, UC-009, UC-017) | Không có |
| ACT-08 Ụ khoá | 1 (UC-014) | 2 (UC-005, UC-007) | Không có |
| ACT-09 Bộ định thời | 1 (UC-009) | 0 | Bình thường với tác nhân thời gian |

Tổng số UC: 24 (23 User-goal, 1 Subfunction, tỉ lệ Subfunction khoảng 4%). Số UC mỗi nhóm: Tài khoản 3, Thuê trả xe 6, Bảo trì 2, Điều phối 4, Chăm sóc khách hàng 3, Danh mục 5, Báo cáo 1. Nhóm Báo cáo chỉ có 1 UC; giữ riêng vì tác nhân và mục đích khác hẳn các nhóm còn lại.

## Câu hỏi mở

Không có câu hỏi mới. Các ứng viên chờ Q-02 (CAND-40), Q-03 (CAND-12) của P00.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P01 | ACT-08 | Mục tiêu "Báo: xe được rút ra, xe được đưa vào" không thành UC riêng với ụ khoá là tác nhân chính; hai sự kiện này là bước hoặc sự kiện kích hoạt của UC-005, UC-007 | Giữ tính chất "Chính và phụ" (chính ở UC-014); ghi rõ trong Mô tả vai trò |

## Vấn đề còn mở

- UC-007 Trả xe: chọn ACT-01 làm tác nhân chính vì mục tiêu thuộc người thuê xe (P01 Mục 2), ACT-08 làm tác nhân phụ. Tuy vậy U-R10 ghi "Tác nhân chính là người trực tiếp thao tác trên hệ thống" và người thuê xe không thao tác trên hệ thống mà trên ụ khoá; theo câu chữ này tác nhân chính sẽ là ACT-08. Chưa có quy tắc cho người tác động lên hệ thống qua một thiết bị ngoài.
- UC-014: vì vai trò nhân viên dùng thẻ chưa rõ (Q-07), tác nhân chính là ACT-08, không nhất quán với cách chọn ở UC-007. Khi Q-07 được trả lời cần xét lại cả hai UC theo cùng một quy tắc.
- CAND-29 (khoá lại ụ sau 60 giây): U-R07 và ví dụ "tự huỷ lịch hẹn chưa xác nhận sau 15 phút" gợi ý thành UC của tác nhân thời gian; U-R09 gợi ý là bước của UC-005. Đã chọn U-R09 vì người thuê xe vẫn trong phiên thuê.
- UC-003: danh sách tác nhân phải đăng nhập gồm cả ACT-06 dù nguồn không nói ban giám đốc có tài khoản; chờ Q-01.
