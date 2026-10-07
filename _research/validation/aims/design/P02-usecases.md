# P02 - Xác định use case - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; P00-problem-brief.md 1.0; P01-actors.md 1.0; AIMS-ProblemStatement-VI.md |
| Phạm vi | Toàn hệ thống |

## 1. Danh sách mục tiêu tác nhân

| ACT | Mục tiêu | Mức mục tiêu dự kiến | REQ | CAND |
|---|---|---|---|---|
| ACT-01 | Mua sản phẩm (từ đặt hàng tới khi được hỗ trợ sau đặt hàng) | Summary | REQ-42, REQ-43 | CAND-20 |
| ACT-01 | Tìm sản phẩm muốn mua | User-goal | REQ-31 đến REQ-34 | CAND-01, CAND-02, CAND-03 |
| ACT-01 | Đưa sản phẩm vào giỏ hàng | User-goal | REQ-35, REQ-40, REQ-44 | CAND-04 |
| ACT-01 | Xem và điều chỉnh giỏ hàng | User-goal | REQ-36 đến REQ-39 | CAND-05, CAND-06, CAND-07 |
| ACT-01 | Đặt hàng các sản phẩm trong giỏ | User-goal | REQ-43, REQ-47 đến REQ-73, REQ-92 | CAND-09 |
| ACT-01 | Nhận hàng nhanh vào thời gian hẹn trước | Subfunction | REQ-52 đến REQ-60, REQ-69 | CAND-12 |
| ACT-01 | Thanh toán đơn hàng | Subfunction | REQ-73 đến REQ-83 | CAND-15 |
| ACT-01 | Huỷ đơn hàng đã thanh toán và nhận lại tiền | User-goal | REQ-90, REQ-91 | CAND-17, CAND-18 |
| ACT-01 | Xem lại lịch sử mua hàng | User-goal | REQ-81 | CAND-19 |
| ACT-02 | Quản lý sản phẩm bán | User-goal | REQ-08 đến REQ-28 | CAND-21 đến CAND-27 |
| ACT-02 | Quản lý người dùng | User-goal | REQ-29, REQ-30 | CAND-28, CAND-29 |
| ACT-02 | Xử lý đơn hàng chờ duyệt | User-goal | REQ-84 đến REQ-89 | CAND-30 đến CAND-33 |

## 2. Danh sách sự kiện

| EV | Sự kiện | Loại | Nguồn phát (ACT) | Phản hồi mong đợi của hệ thống | REQ | CAND |
|---|---|---|---|---|---|---|
| EV-01 | Khách hàng muốn tìm sản phẩm để mua | Nghiệp vụ | ACT-01 | Hiển thị sản phẩm phù hợp, 20 sản phẩm mỗi trang | REQ-31 đến REQ-34 | CAND-01, CAND-02 |
| EV-02 | Khách hàng quyết định mua một sản phẩm với số lượng nhất định | Nghiệp vụ | ACT-01 | Thêm sản phẩm vào giỏ hàng hiện tại | REQ-35 | CAND-04 |
| EV-03 | Khách hàng muốn kiểm tra giỏ hàng | Nghiệp vụ | ACT-01 | Hiển thị thông tin giỏ hàng và cảnh báo thiếu hàng | REQ-36 đến REQ-38 | CAND-05 |
| EV-04 | Khách hàng muốn đặt mua các sản phẩm trong giỏ | Nghiệp vụ | ACT-01 | Kiểm tra tồn kho, nhận thông tin giao hàng, tính phí, lập đơn hàng tạm thời, cho thanh toán | REQ-47 đến REQ-73 | CAND-09 |
| EV-05 | Khách hàng muốn huỷ đơn hàng đã thanh toán | Nghiệp vụ | ACT-01 | Huỷ đơn, hoàn toàn bộ tiền vào thẻ | REQ-90, REQ-91 | CAND-17 |
| EV-06 | Khách hàng muốn xem lại các lần mua | Nghiệp vụ | ACT-01 | Hiển thị lịch sử mua hàng | REQ-81 | CAND-19 |
| EV-07 | Cửa hàng có sản phẩm mới, thay đổi hoặc ngừng bán sản phẩm, giá thị trường thay đổi | Nghiệp vụ | ACT-02 | Thêm, sửa, xoá sản phẩm, cập nhật giá | REQ-08 đến REQ-28 | CAND-21 đến CAND-26 |
| EV-08 | Có đơn hàng ở trạng thái chờ xử lý | Nghiệp vụ | ACT-02 | Cho quản trị viên xem, phê duyệt hoặc từ chối đơn | REQ-84 đến REQ-89 | CAND-30 |
| EV-09 | Quản trị viên cần thay đổi người dùng | Nghiệp vụ | ACT-02 | Chặn, bỏ chặn, tạo, xem, cập nhật, xoá người dùng, đổi mật khẩu | REQ-29, REQ-30 | CAND-28 |

## 3. Bảng ứng viên use case

| CAND | Ứng viên | Kết luận | Phép thử không đạt | Lý do | REQ | Nguồn phát hiện |
|---|---|---|---|---|---|---|
| CAND-01 | Xem danh sách sản phẩm | Gộp vào UC-001 | U-T11, U-AP12 | Cùng tác nhân, cùng kết quả (thấy sản phẩm để chọn mua), cùng cách hiển thị 20 sản phẩm mỗi trang và sắp xếp theo giá như tìm kiếm; khác biệt là có hay không có tiêu chí tìm kiếm, thành luồng thay thế (U-R05, U-R12) | REQ-31, REQ-32 | Sự kiện EV-01 |
| CAND-02 | Tìm kiếm sản phẩm | Giữ thành UC-001 | - | Mục tiêu thông tin độc lập của khách hàng (U-R05) | REQ-32, REQ-33 | Mục tiêu |
| CAND-03 | Sắp xếp sản phẩm theo giá | Là bước của UC-001 | U-T4, U-AP01 | Sắp xếp là tuỳ chọn trên danh sách (U-R05) | REQ-34 | Động từ |
| CAND-04 | Thêm sản phẩm vào giỏ hàng | Giữ thành UC-002 | - | Giỏ hàng được lưu vào tài khoản hoặc bộ nhớ thiết bị (REQ-44) nên tồn tại qua nhiều phiên và khách hàng có mục tiêu riêng với nó (U-R14) | REQ-35, REQ-40, REQ-44 | Mục tiêu |
| CAND-05 | Xem giỏ hàng | Giữ thành UC-003 | - | Mục tiêu riêng: biết giỏ có gì, tổng tiền, sản phẩm nào thiếu hàng (U-R05) | REQ-36, REQ-37, REQ-38 | Mục tiêu |
| CAND-06 | Bỏ sản phẩm khỏi giỏ hàng | Là bước của UC-003 | U-T4, U-AP01 | Một thao tác đơn trong khi xem giỏ hàng | REQ-39 | Động từ |
| CAND-07 | Cập nhật giỏ hàng | Là bước của UC-003 | U-T4, U-AP01 | Thao tác trong khi xem giỏ; phạm vi cập nhật chờ Q-19 | REQ-49 | Động từ |
| CAND-08 | Làm trống giỏ hàng | Là bước của UC-006 | U-T9, U-AP03 | Hệ quả của thanh toán thành công, không có tác nhân chủ động | REQ-41 | Động từ |
| CAND-09 | Đặt hàng | Giữ thành UC-004 | - | Mục tiêu User-goal của khách hàng, hoàn tất trong một phiên | REQ-43, REQ-47 đến REQ-73, REQ-92 | Mục tiêu |
| CAND-10 | Kiểm tra tồn kho | Là bước của UC-004 | U-T9, U-AP03 | Xử lý nội bộ khi đặt hàng | REQ-48 | Động từ |
| CAND-11 | Cập nhật thông tin giao hàng | Là bước của UC-004 | U-T1, U-AP01 | Một bước trong đặt hàng | REQ-51 | Động từ |
| CAND-12 | Đặt hàng giao nhanh | Giữ thành UC-005 | - | Subfunction giữ theo Q4b: hành vi tuỳ chọn có điều kiện (khách hàng chọn giao nhanh), đủ lớn (kiểm tra hỗ trợ, nhận thông tin giao nhanh, cập nhật cách tính phí) | REQ-52 đến REQ-60, REQ-69 | Mục tiêu |
| CAND-13 | Tính phí giao hàng | Là bước của UC-004 | U-T9, U-AP03 | Xử lý nội bộ; quy tắc phí thành BR ở P04 | REQ-61 đến REQ-69 | Động từ |
| CAND-14 | Lưu và lấy thông tin giao hàng, thông tin thẻ mặc định | Là bước của UC-004 | U-T9, U-AP03 | Xử lý nội bộ về lưu trữ, dùng trong đặt hàng và thanh toán (U-R09) | REQ-44 | Động từ |
| CAND-15 | Thanh toán đơn hàng | Giữ thành UC-006 | - | Subfunction giữ theo Q4c: đặt hàng cộng thanh toán vượt khoảng 15 bước (đặt hàng khoảng 10 bước, thanh toán khoảng 8 bước), có tác nhân phụ riêng; nguồn nêu là bước bắt buộc để đặt hàng thành công (REQ-43) | REQ-43, REQ-73 đến REQ-83 | Mục tiêu |
| CAND-16 | Gửi email thông tin đơn hàng và giao dịch | Là bước của UC-006 | U-T9, U-AP03 | Hệ quả của thanh toán (U-R06); kênh gửi chờ Q-07 | REQ-83 | Động từ |
| CAND-17 | Huỷ đơn hàng | Giữ thành UC-007 | - | Giao dịch nghiệp vụ của khách hàng, kết quả là đơn bị huỷ và tiền được hoàn | REQ-90, REQ-91 | Mục tiêu |
| CAND-18 | Hoàn tiền vào thẻ tín dụng | Là bước của UC-007 | U-T8, U-T9, U-AP03 | Lời gọi tác nhân phụ trong huỷ đơn (U-R08); Q4 không thoả: chỉ một UC dùng, không tuỳ chọn, nhỏ | REQ-91, REQ-99 | Động từ |
| CAND-19 | Xem lịch sử mua hàng | Giữ thành UC-008 | - | Mục tiêu thông tin độc lập (U-R05) | REQ-80, REQ-81 | Mục tiêu |
| CAND-20 | Mua sản phẩm (quy trình 5 bước) | Tách thành CAND-09, CAND-15, CAND-30 | U-T1, U-T6, U-AP04 | Gồm nhiều phiên và nhiều tác nhân (khách hàng, quản trị viên); vận chuyển và hỗ trợ sau đặt hàng chờ Q-03 | REQ-42 | Mục tiêu |
| CAND-21 | Quản lý sản phẩm | Giữ thành UC-009 | - | CRUD dữ liệu danh mục sản phẩm của cùng tác nhân (U-R04); các giới hạn số lượng, số lần cập nhật giá, khoảng giá là quy tắc kiểm tra, không làm luồng khác hẳn (U-R04c không thoả) | REQ-08 đến REQ-28 | Mục tiêu |
| CAND-22 | Thêm sản phẩm | Gộp vào UC-009 | U-AP07 | CRUD vụn (U-R04) | REQ-08 | Động từ |
| CAND-23 | Xem sản phẩm (quản trị viên) | Gộp vào UC-009 | U-AP07 | CRUD vụn (U-R04) | REQ-09 | Động từ |
| CAND-24 | Sửa sản phẩm | Gộp vào UC-009 | U-AP07 | CRUD vụn (U-R04) | REQ-10 | Động từ |
| CAND-25 | Xoá sản phẩm | Gộp vào UC-009 | U-AP07 | CRUD vụn (U-R04) | REQ-11 | Động từ |
| CAND-26 | Cập nhật giá sản phẩm | Gộp vào UC-009 | U-AP07, U-AP15 | Là một trường hợp của sửa sản phẩm; quy tắc riêng (REQ-24, REQ-25) là BR của UC-009 | REQ-10, REQ-24, REQ-25 | Động từ |
| CAND-27 | Lưu lịch sử thao tác sản phẩm | Là bước của UC-009 | U-T9, U-AP03 | Xử lý nội bộ | REQ-26 | Động từ |
| CAND-28 | Quản lý người dùng | Loại | U-T10 | Thuộc mục Ngoài phạm vi của P00 theo câu loại trừ "thay vì ... quản lý người dùng" (L13), U-R16; chờ Q-01 | REQ-29 | Mục tiêu |
| CAND-29 | Gửi email thông báo hành động quản trị người dùng | Loại | U-T9, U-AP03 | Hệ quả của CAND-28 đã bị loại (U-R06, U-R16) | REQ-30 | Động từ |
| CAND-30 | Duyệt đơn hàng | Giữ thành UC-010 | - | Giao dịch nghiệp vụ của quản trị viên, phản hồi sự kiện EV-08, có quy tắc riêng (REQ-88, REQ-89) (U-R13) | REQ-84 đến REQ-89 | Sự kiện EV-08 |
| CAND-31 | Từ chối đơn hàng | Gộp vào UC-010 | U-AP12 | Cùng tác nhân, cùng sự kiện, là kết quả khác của cùng quyết định duyệt | REQ-84, REQ-88 | Động từ |
| CAND-32 | Xem danh sách đơn hàng chờ xử lý | Là bước của UC-010 | U-T5 | Việc xem phục vụ bước chọn đơn để duyệt (U-R05) | REQ-85, REQ-86, REQ-87 | Động từ |
| CAND-33 | Quản lý đơn hàng | Gộp vào UC-010 | U-AP02, U-AP08 | "chế độ xem quản lý đơn đặt hàng" là giao diện; "Quản lý X" che giấu giao dịch duyệt đơn (U-R04b) | REQ-84, REQ-85 | Động từ |
| CAND-34 | Đăng ký, đăng nhập | Loại | U-T10 | Nguồn loại trừ tường minh (REQ-94), U-R16, U-R01 | REQ-94 | Động từ |
| CAND-35 | Reset số dư thẻ | Loại | U-AP16 | Chỉ phục vụ kiểm thử, không có tác nhân nghiệp vụ | REQ-100 | Động từ |
| CAND-36 | Xem số dư thẻ | Là bước của UC-006 | U-T8, U-AP03 | Số dư được hiển thị trong kết quả thanh toán (REQ-79); không có tác nhân chủ động xem số dư | REQ-79, REQ-101 | Động từ |
| CAND-37 | Vận chuyển, hỗ trợ sau đặt hàng | Loại | U-T10 | Nguồn chỉ nêu tên bước, không mô tả tương tác; chờ Q-03 | REQ-42 | Mục tiêu |
| CAND-38 | Trở về bước trước khi đặt hàng | Là bước của UC-004 | U-T4, U-AP01 | Biến thể trong đặt hàng (luồng *a ở P04) | REQ-92 | Động từ |

## 4. Bảng use case

| UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | Nhóm chức năng | REQ | Mức | CAND nguồn |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UC-001 | Tìm kiếm sản phẩm | Search Media | ACT-01 Khách hàng | - | Khách hàng thấy các sản phẩm phù hợp để chọn mua. | Khách hàng xem danh sách sản phẩm hoặc tìm sản phẩm theo đặc tính, xem 20 sản phẩm mỗi trang và có thể sắp xếp theo giá. | Khách hàng muốn tìm sản phẩm để mua (EV-01) | Mua hàng | REQ-31 đến REQ-34 | User-goal | CAND-01, CAND-02, CAND-03 |
| UC-002 | Thêm sản phẩm vào giỏ hàng | Add Media To Cart | ACT-01 Khách hàng | - | Giỏ hàng hiện tại có sản phẩm khách hàng chọn với số lượng mong muốn. | Khách hàng chọn một sản phẩm và số lượng để đưa vào giỏ hàng hiện tại. | Khách hàng quyết định mua một sản phẩm (EV-02) | Mua hàng | REQ-35, REQ-40, REQ-44 | User-goal | CAND-04 |
| UC-003 | Xem giỏ hàng | View Cart | ACT-01 Khách hàng | - | Khách hàng biết giỏ hàng có gì, tổng tiền và sản phẩm nào thiếu hàng, và giỏ hàng chỉ còn sản phẩm khách hàng muốn mua. | Khách hàng xem sản phẩm, tổng giá trước và sau VAT trong giỏ, được cảnh báo sản phẩm thiếu hàng tồn kho và có thể bỏ sản phẩm khỏi giỏ. | Khách hàng muốn kiểm tra giỏ hàng (EV-03) | Mua hàng | REQ-36 đến REQ-39 | User-goal | CAND-05, CAND-06, CAND-07 |
| UC-004 | Đặt hàng | Place Order | ACT-01 Khách hàng | - | Khách hàng có một đơn hàng đã thanh toán đang chờ xử lý. | Khách hàng yêu cầu đặt hàng từ giỏ hàng, cung cấp thông tin giao hàng; hệ thống kiểm tra tồn kho và thông tin giao hàng, tính phí giao hàng, lập đơn hàng tạm thời rồi cho khách hàng thanh toán. | Khách hàng muốn đặt mua các sản phẩm trong giỏ (EV-04) | Mua hàng | REQ-43, REQ-47 đến REQ-73, REQ-92 | User-goal | CAND-09, CAND-10, CAND-11, CAND-13, CAND-14, CAND-38 |
| UC-005 | Đặt hàng giao nhanh | Place Rush Order | - (Được gọi từ UC-004) | - | Khách hàng có đơn hàng được giao nhanh vào thời gian hẹn trước. | Hành vi tuỳ chọn trong đặt hàng (Q4b): hệ thống kiểm tra sản phẩm và địa chỉ hỗ trợ giao nhanh, nhận thông tin giao hàng nhanh và cập nhật cách tính phí giao hàng. | Khách hàng chọn giao hàng nhanh khi đặt hàng | Mua hàng | REQ-52 đến REQ-60, REQ-69 | Subfunction | CAND-12 |
| UC-006 | Thanh toán đơn hàng | Pay Order | - (Được gọi từ UC-004) | ACT-03 Liên ngân hàng | Khách hàng đã trả tiền cho đơn hàng bằng thẻ và nhận thông tin giao dịch. | Phần rất lớn của đặt hàng được tách ra (Q4c): khách hàng chọn phương thức, cung cấp thông tin thẻ và nội dung giao dịch; hệ thống trừ tiền qua liên ngân hàng, hiển thị kết quả, lưu giao dịch, chuyển đơn sang chờ xử lý, làm trống giỏ và gửi email. | Hệ thống cho phép thanh toán sau khi hiển thị đơn hàng tạm thời | Mua hàng | REQ-41, REQ-43, REQ-73 đến REQ-83, REQ-95 đến REQ-98, REQ-101 | Subfunction | CAND-08, CAND-15, CAND-16, CAND-36 |
| UC-007 | Huỷ đơn hàng | Cancel Order | ACT-01 Khách hàng | ACT-03 Liên ngân hàng | Đơn hàng đã thanh toán bị huỷ và khách hàng nhận lại toàn bộ số tiền vào thẻ đã dùng. | Khách hàng huỷ một đơn hàng đã thanh toán; hệ thống hoàn toàn bộ số tiền vào thẻ tín dụng đã dùng qua liên ngân hàng. | Khách hàng muốn huỷ đơn hàng đã thanh toán (EV-05) | Mua hàng | REQ-90, REQ-91, REQ-97, REQ-99 | User-goal | CAND-17, CAND-18 |
| UC-008 | Xem lịch sử mua hàng | View Purchase History | ACT-01 Khách hàng | - | Khách hàng biết các đơn hàng và giao dịch đã thực hiện. | Khách hàng xem lại các đơn hàng và thông tin giao dịch đã được hệ thống ghi lại. | Khách hàng muốn xem lại các lần mua (EV-06) | Mua hàng | REQ-80, REQ-81 | User-goal | CAND-19 |
| UC-009 | Quản lý sản phẩm | Manage Media | ACT-02 Quản trị viên | - | Quản trị viên có danh mục sản phẩm bán đúng với thực tế cửa hàng. | Quản trị viên thêm, xem, sửa (kể cả cập nhật giá), xoá sản phẩm theo các giới hạn về số lượng, số lần cập nhật giá và khoảng giá; hệ thống lưu lịch sử thao tác và thông báo thao tác không hợp lệ. | Cửa hàng có sản phẩm mới, thay đổi hoặc ngừng bán sản phẩm (EV-07) | Quản trị | REQ-08 đến REQ-28 | User-goal | CAND-21 đến CAND-27 |
| UC-010 | Duyệt đơn hàng | Review Order | ACT-02 Quản trị viên | - | Đơn hàng chờ xử lý được phê duyệt hoặc từ chối. | Quản trị viên xem danh sách đơn chờ xử lý, xem chi tiết một đơn và phê duyệt hoặc từ chối; hệ thống không cho phê duyệt khi kho không đủ sản phẩm. | Có đơn hàng ở trạng thái chờ xử lý (EV-08) | Quản trị | REQ-84 đến REQ-89 | User-goal | CAND-30 đến CAND-33 |

## 5. Ma trận truy vết REQ --> UC

| REQ | Nội dung tóm tắt | UC phủ | Ghi chú |
|---|---|---|---|
| REQ-08 đến REQ-11 | Thêm, xem, sửa, xoá sản phẩm | UC-009 | Không có |
| REQ-12 đến REQ-15, REQ-17, REQ-24, REQ-25, REQ-28 | Quy tắc sản phẩm | UC-009 | BR ở P04 của UC-009 |
| REQ-16, REQ-18 đến REQ-23 | Dữ liệu sản phẩm | UC-009 | Không có |
| REQ-26, REQ-27 | Lịch sử thao tác, thông báo không hợp lệ | UC-009 | Không có |
| REQ-29, REQ-30 | Quản lý người dùng | Không có | Ngoài phạm vi, chờ Q-01 |
| REQ-31 đến REQ-34 | Danh sách, tìm kiếm, sắp xếp | UC-001 | Không có |
| REQ-35 | Thêm vào giỏ | UC-002 | Không có |
| REQ-36 đến REQ-39 | Xem giỏ, cảnh báo thiếu hàng, bỏ sản phẩm | UC-003 | Không có |
| REQ-40 | Một giỏ hàng | UC-002 | BR |
| REQ-41 | Làm trống giỏ | UC-006 | Không có |
| REQ-42 | Quy trình 5 bước | UC-004, UC-006, UC-010 | Vận chuyển, hỗ trợ sau đặt hàng chờ Q-03 |
| REQ-43 | Đặt hàng thành công gồm đặt hàng và thanh toán | UC-004, UC-006 | Căn cứ quan hệ include ở P03 |
| REQ-44 | Lưu, lấy thông tin mặc định | UC-002, UC-004, UC-006 | Chờ Q-02 |
| REQ-45, REQ-46 | Dữ liệu giao hàng, thẻ | UC-004, UC-006 | Không có |
| REQ-47 đến REQ-51, REQ-55, REQ-56, REQ-61 đến REQ-68, REQ-70 đến REQ-72 | Đặt hàng, tồn kho, thông tin giao hàng, phí, đơn tạm thời | UC-004 | Không có |
| REQ-52 đến REQ-54, REQ-57 đến REQ-60, REQ-69 | Giao hàng nhanh | UC-005 | REQ-52, REQ-56 cũng phủ bởi UC-004 (điểm mở rộng) |
| REQ-73 đến REQ-80, REQ-82, REQ-83 | Thanh toán | UC-006 | Không có |
| REQ-81 | Xem lịch sử mua hàng | UC-008 | Không có |
| REQ-84 đến REQ-89 | Duyệt đơn | UC-010 | Không có |
| REQ-90, REQ-91 | Huỷ đơn, hoàn tiền | UC-007 | Không có |
| REQ-92 | Trở về bước bất kỳ | UC-004 | Không có |
| REQ-93, REQ-94 | Không tài khoản, không đăng nhập | Không có | Ràng buộc, chuyển P06 |
| REQ-95 đến REQ-98, REQ-101 | Thẻ giả lập, token, API trừ tiền, xem số dư | UC-006 | Không có |
| REQ-99 | API cộng tiền | UC-007 | Không có |
| REQ-100 | API reset | Không có | Ngoài phạm vi |
| REQ-01 đến REQ-07 | Phi chức năng toàn hệ thống | Không có | Chuyển P06 |

## 6. Thống kê và nhận xét ngưỡng

| ACT | Số UC là tác nhân chính | Số UC là tác nhân phụ | Nhận xét |
|---|---|---|---|
| ACT-01 Khách hàng | 6 (UC-001, UC-002, UC-003, UC-004, UC-007, UC-008) | 0 | Trong khoảng 2-12. Tương tác trong UC-005, UC-006 qua UC-004 |
| ACT-02 Quản trị viên | 2 (UC-009, UC-010) | 0 | Trong khoảng 2-12 |
| ACT-03 Liên ngân hàng | 0 | 2 (UC-006, UC-007) | Tác nhân phụ |

Tổng số UC: 10. Nhóm Mua hàng: 8 UC; nhóm Quản trị: 2 UC (hệ thống dưới 15 UC nên giữ 2 nhóm). Số UC mức Subfunction: 2 (20%), ở ngưỡng trên của mức hợp lý.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi ảnh hưởng tới danh sách use case: Q-01 (CAND-28), Q-03 (CAND-37), Q-19 (CAND-07), Q-20 (UC-006).

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- UC-002 Thêm sản phẩm vào giỏ hàng có luồng dự kiến 2-3 bước, dưới ngưỡng U-T4. Giữ theo U-R14 vì giỏ hàng tồn tại qua nhiều phiên (REQ-44); quy tắc U-R14 được ưu tiên hơn cây quyết định (Bước 5, ngoại lệ ưu tiên).
- UC-006 được giữ theo Q4c dựa trên ước lượng số bước (đặt hàng cộng thanh toán vượt 15 bước). Nếu ước lượng thấp hơn, cây quyết định cho kết luận "Là bước của UC-004"; kết luận này phụ thuộc ước lượng, chưa có căn cứ trực tiếp khác ngoài REQ-43.
