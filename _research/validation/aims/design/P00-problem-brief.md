# P00 - Chuẩn hoá yêu cầu - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P00 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; AIMS-ProblemStatement-VI.md |
| Phạm vi | Toàn hệ thống |

## 1. Bối cảnh và mục tiêu nghiệp vụ

AIMS Project là một hệ thống thương mại điện tử chuyên mua bán sản phẩm phương tiện truyền thông (L10-11). Đề bài nêu động cơ là giúp sản phẩm sáng tạo của văn nghệ sĩ, trí thức đến được với mọi người trong thời đại Internet (L5-10). Hệ thống hiện chỉ bán sản phẩm vật lý gồm sách, CD, đĩa than LP và DVD (L51-55). Trọng tâm được đề bài chỉ định là đặt hàng và thanh toán đơn hàng của khách hàng (L13-15). Thanh toán được thực hiện qua thẻ tín dụng giả lập bằng các API liên ngân hàng có sẵn (L193-212).

Mục tiêu nghiệp vụ:
- Cho phép khách hàng đặt hàng và thanh toán đơn hàng sản phẩm phương tiện truyền thông (nguồn: "tập trung vào các tính năng liên quan tới đặt hàng và thanh toán đơn đặt hàng của khách hàng", L14-15).
- Cho phép quản trị viên quản lý sản phẩm bán và phê duyệt đơn hàng (nguồn: L23-27, L174-181).

## 2. Phạm vi

Trong phạm vi:
- Khách hàng tìm kiếm, xem sản phẩm, quản lý giỏ hàng (REQ-31 đến REQ-40).
- Đặt hàng, giao hàng nhanh, tính phí giao hàng, đơn hàng tạm thời (REQ-42 đến REQ-73).
- Thanh toán đơn hàng qua liên ngân hàng (REQ-74 đến REQ-83, REQ-95 đến REQ-99, REQ-101).
- Quản trị viên phê duyệt hoặc từ chối đơn hàng (REQ-84 đến REQ-89).
- Khách hàng huỷ đơn hàng đã thanh toán và được hoàn tiền (REQ-90, REQ-91).
- Quản trị viên quản lý sản phẩm (REQ-08 đến REQ-28).
- Yêu cầu phi chức năng toàn hệ thống (REQ-01 đến REQ-07).

Ngoài phạm vi:
- Xác thực tài khoản, đăng ký, đăng nhập của khách hàng (nguồn: "thay vì các tính năng liên quan tới xác thực tài khoản hay quản lý người dùng", L13; "Hệ thống cũng sẽ không có chức năng cho phép khách hàng đăng ký, đăng nhập", L188-189). REQ-94.
- Quản lý người dùng (nguồn: L13, câu trên). Mâu thuẫn với đoạn L66-69 mô tả chi tiết chức năng này, xem mục 5 dòng 1 và Q-01. REQ-29, REQ-30 được ghi nhận với trạng thái chờ Q-01.
- API reset của thẻ tín dụng ảo: chỉ phục vụ kiểm thử khi phát triển (nguồn: "API này được tạo ra giúp thuận tiện cho việc test khi dev", L209-210). REQ-100.

## 3. Các bên liên quan và người dùng

| SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống | REQ |
|---|---|---|---|---|---|
| SH-01 | Khách hàng | Người dùng trực tiếp | Tìm và mua sản phẩm, thanh toán, huỷ đơn và nhận lại tiền | Có | REQ-31 đến REQ-83, REQ-90 đến REQ-93 |
| SH-02 | Quản trị viên | Người vận hành, quản trị | Quản lý sản phẩm, phê duyệt đơn hàng | Có | REQ-08 đến REQ-30, REQ-84 đến REQ-89 |
| SH-03 | Liên ngân hàng | Hệ thống hoặc thiết bị ngoài | Xử lý giao dịch thẻ tín dụng (trừ tiền, cộng tiền, xem số dư) | Có | REQ-77, REQ-97 đến REQ-101 |
| SH-04 | Người dùng được quản trị viên quản lý | Người hưởng lợi gián tiếp | Nhận email thông báo về hành động quản trị | Chưa rõ | REQ-29, REQ-30 |
| SH-05 | Văn nghệ sĩ, trí thức (tác giả sản phẩm) | Người hưởng lợi gián tiếp | Sản phẩm sáng tạo đến được với người mua | Không | Không có (bối cảnh L5-9) |
| SH-06 | Người nhận hàng | Người hưởng lợi gián tiếp | Nhận hàng theo thông tin giao hàng | Không | REQ-45 |

## 4. Danh sách yêu cầu

| REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |
|---|---|---|---|---|
| REQ-01 | Hệ thống phải hoạt động "đa nền tảng". | Ràng buộc | "AIMS Project là một hệ thống đa nền tảng" (L17) | Q-15 |
| REQ-02 | Hệ thống hoạt động 24/7. | Phi chức năng | "hoạt động 24/7" (L17) | Không có |
| REQ-03 | Người dùng mới làm quen với hệ thống "dễ dàng". | Phi chức năng | "cho phép người dùng mới có thể làm quen dễ dàng" (L17-18) | Q-15 |
| REQ-04 | Hệ thống phục vụ 1000 khách hàng cùng lúc mà hiệu suất không bị giảm "đáng kể". | Phi chức năng | "phục vụ 1000 khách hàng cùng lúc mà hiệu suất không bị giảm đáng kể" (L18-19) | Q-15 |
| REQ-05 | Hệ thống hoạt động 300 giờ liên tục không hỏng hóc. | Phi chức năng | "có thể hoạt động 300 giờ liên tục không hỏng hóc" (L19) | Không có |
| REQ-06 | Hệ thống hoạt động trở lại bình thường trong vòng 1 giờ sau khi xảy ra lỗi. | Phi chức năng | "hoạt động trở lại bình thường trong vòng 1 giờ sau khi xảy ra lỗi" (L20) | Không có |
| REQ-07 | Thời gian đáp ứng của hệ thống tối đa 1 giây khi bình thường và 2 giây lúc "cao điểm". | Phi chức năng | "Thời gian đáp ứng của hệ thống tối đa là 1 giây khi bình thường hoặc 2 giây lúc cao điểm" (L20-21) | Q-15 |
| REQ-08 | Quản trị viên có thể thêm sản phẩm. | Chức năng | "quản trị viên có thể thêm, xem, sửa, xóa bất kỳ sản phẩm nào" (L23-24) | Tách vì nguồn có quy định riêng cho từng thao tác |
| REQ-09 | Quản trị viên có thể xem sản phẩm. | Chức năng | như REQ-08 (L23-24) | Tách từ cùng câu với REQ-08 |
| REQ-10 | Quản trị viên có thể sửa sản phẩm, kể cả cập nhật giá. | Chức năng | như REQ-08 (L23-24); "quản trị viên có thể cập nhật giá cả của một sản phẩm" (L57-58) | Tách từ cùng câu với REQ-08 |
| REQ-11 | Quản trị viên có thể xoá sản phẩm. | Chức năng | như REQ-08 (L23-24) | Tách từ cùng câu với REQ-08 |
| REQ-12 | Mỗi lần thêm hoặc sửa, quản trị viên chỉ thao tác với một sản phẩm. | Quy tắc nghiệp vụ | "chỉ có thể thêm hoặc sửa với một sản phẩm tại một thời điểm" (L24-25) | Không có |
| REQ-13 | Mỗi lần xoá, quản trị viên xoá tối đa 10 sản phẩm. | Quy tắc nghiệp vụ | "có thể xóa tới 10 sản phẩm cùng một lúc" (L25) | Không có |
| REQ-14 | Quản trị viên không thể xoá hoặc cập nhật quá 30 sản phẩm. | Quy tắc nghiệp vụ | "không thể xóa hoặc cập nhật quá 30 sản phẩm ví lý do bảo mật" (L25-26) | Q-11 (giới hạn tính theo ngày hay không) |
| REQ-15 | Quản trị viên có thể thêm không giới hạn số sản phẩm trong một ngày. | Quy tắc nghiệp vụ | "có thể thêm không giới hạn số sản phẩm trong một ngày" (L26-27) | Không có |
| REQ-16 | Sản phẩm phương tiện truyền thông gồm tên sản phẩm (title), loại hình (category), giá trị (value) và giá hiện tại (price). | Dữ liệu | "cần cung cấp tên sản phẩm(title), loại hình (category), giá trị (value), và giá cả hiện tại (price)" (L30-31) | Không có |
| REQ-17 | Giá trị và giá của sản phẩm chưa bao gồm thuế VAT 10%. | Quy tắc nghiệp vụ | "Giá trị và giá cả của sản phẩm chưa bao gồm thuế giá trị gia tăng (VAT) 10%" (L31-32) | Không có |
| REQ-18 | Sách gồm tác giả, loại bìa (bìa mềm hoặc bìa cứng), nhà xuất bản, ngày xuất bản (bắt buộc) và số trang, ngôn ngữ, thể loại (không bắt buộc). | Dữ liệu | L35-38 | Không có |
| REQ-19 | Đĩa CD gồm nghệ sĩ, hãng ghi âm, danh sách bài hát, thể loại (bắt buộc) và ngày phát hành (không bắt buộc). | Dữ liệu | L40-42 | Không có |
| REQ-20 | Đĩa than LP gồm các thông tin giống đĩa CD. | Dữ liệu | "Đĩa than LP (long-play record) yêu cầu cần có các thông tin giống với đĩa CD" (L46) | Không có |
| REQ-21 | Đĩa DVD gồm loại đĩa (Blu-ray, HD-DVD), đạo diễn, thời lượng, hãng sản xuất, ngôn ngữ, phụ đề (bắt buộc) và ngày phát hành, thể loại (không bắt buộc). | Dữ liệu | L47-49 | Không có |
| REQ-22 | Hệ thống chỉ cho phép mua bán sản phẩm phương tiện truyền thông vật lý. | Quy tắc nghiệp vụ | "Hiện tại, hệ thống chỉ cho phép mua bán sản phẩm phương tiện truyền thông vật lý" (L51) | Không có |
| REQ-23 | Sản phẩm vật lý gồm mã vạch, mô tả, số lượng, ngày nhập kho, kích thước và khối lượng. | Dữ liệu | L52-54 | Không có |
| REQ-24 | Giá của một sản phẩm được cập nhật tối đa 02 lần trong một ngày. | Quy tắc nghiệp vụ | "cập nhật giá cả của một sản phẩm tối đa 02 lần trong một ngày" (L57-58) | Không có |
| REQ-25 | Giá của sản phẩm nằm trong khoảng từ 30% đến 150% giá trị sản phẩm. | Quy tắc nghiệp vụ | "giá cả của sản phẩm luôn cần nằm trong khoảng từ 30% đến 150% giá trị sản phẩm" (L58-60) | Không có |
| REQ-26 | Hệ thống lưu lịch sử các thao tác thêm, sửa, xoá sản phẩm. | Dữ liệu | "Hệ thống sẽ lưu trữ lịch sử các thao tác thêm, sửa, xóa sản phẩm" (L62) | Không có |
| REQ-27 | Hệ thống thông báo cho quản trị viên khi thao tác thêm, sửa, xoá sản phẩm không hợp lệ. | Chức năng | "sẽ thông báo cho quản trị viên nếu thao tác nào không hợp lệ" (L62-64) | Không có |
| REQ-28 | Ngày tháng nhập cho sản phẩm phải đúng định dạng. | Quy tắc nghiệp vụ | "hoặc sai định dạng ngày tháng" (L64) | Định dạng chưa nêu, Q-11 |
| REQ-29 | Quản trị viên có thể quản lý người dùng (chặn, bỏ chặn, tạo mới, xem, cập nhật, xoá, đổi mật khẩu). | Chức năng | L66-68 | Chưa tách vì nguồn không phân biệt; mâu thuẫn với phạm vi L13; Q-01 |
| REQ-30 | Hệ thống tự động gửi email tới người dùng để thông báo các hành động quản trị người dùng. | Chức năng | L68-69 | Q-01, Q-07 |
| REQ-31 | Hệ thống hiển thị danh sách sản phẩm bất kỳ khi khởi động. | Chức năng | "khi khởi động, hệ thống sẽ hiện ra danh sách của 20 sản phẩm bất kỳ ở mỗi trang" (L71-72) | Không có |
| REQ-32 | Mỗi trang danh sách sản phẩm và mỗi trang kết quả tìm kiếm hiển thị 20 sản phẩm. | Quy tắc nghiệp vụ | L71-72; "hiện ra 20 sản phẩm liên quan trong mỗi trang tìm kiếm" (L72-73) | Tách từ REQ-31, REQ-33 |
| REQ-33 | Khách hàng có thể tìm kiếm sản phẩm theo các đặc tính của sản phẩm. | Chức năng | "khách hàng sử dụng các đặc tính của sản phẩm để tìm kiếm" (L72) | Q-12 |
| REQ-34 | Khách hàng có thể sắp xếp sản phẩm theo giá. | Chức năng | "khách hàng có thể sắp xếp sản phẩm theo giá cả" (L73-74) | Không có |
| REQ-35 | Khách hàng có thể thêm sản phẩm với số lượng tương ứng vào giỏ hàng hiện tại. | Chức năng | L74-75 | Không có |
| REQ-36 | Khách hàng có thể xem giỏ hàng. | Chức năng | "Khi xem giỏ hàng, hệ thống sẽ hiện ra thông tin giỏ hàng" (L77) | Không có |
| REQ-37 | Thông tin giỏ hàng gồm tổng giá sản phẩm chưa gồm VAT, tổng giá sản phẩm đã gồm VAT và danh sách sản phẩm (tên, số lượng, giá). | Dữ liệu | L77-79 | Không có |
| REQ-38 | Hệ thống thông báo cho khách hàng khi hàng tồn kho của sản phẩm trong giỏ không đủ, kèm số lượng của từng sản phẩm bị thiếu. | Chức năng | L79-81 | Q-13 |
| REQ-39 | Khách hàng có thể bỏ sản phẩm khỏi giỏ hàng. | Chức năng | "khách hàng cũng có thể bỏ sản phẩm khỏi giỏ hàng" (L81) | Không có |
| REQ-40 | Mỗi phiên bản chạy của hệ thống chỉ có 1 giỏ hàng. | Quy tắc nghiệp vụ | "chỉ có 1 giỏ hàng trong mỗi phiên bản chạy của hệ thống" (L82) | Không có |
| REQ-41 | Hệ thống làm trống giỏ hàng khi thanh toán đơn hàng thành công. | Chức năng | "giỏ hàng sẽ được làm trống sau khi thanh toán đơn hàng thành công" (L82-83) | Không có |
| REQ-42 | Quá trình đặt hàng gồm 5 bước: đặt hàng, thanh toán, duyệt đơn hàng, vận chuyển, hỗ trợ sau đặt hàng. | Quy tắc nghiệp vụ | L85-87 | Q-03 |
| REQ-43 | Đặt hàng thành công khi khách hàng hoàn tất hai bước đặt hàng và thanh toán. | Quy tắc nghiệp vụ | "Để đặt hàng thành công, khách hàng cần thực hiện 2 bước đầu tiên: đặt hàng và thanh toán" (L89) | Không có |
| REQ-44 | Hệ thống tự động lưu và lấy thông tin giao hàng mặc định, thông tin thẻ và sản phẩm trong giỏ hàng: vào tài khoản với khách hàng đăng nhập, vào bộ nhớ thiết bị với khách hàng không đăng nhập. | Chức năng | L90-99 | Mâu thuẫn với REQ-94; Q-02 |
| REQ-45 | Thông tin giao hàng gồm tên người nhận, số điện thoại, tỉnh/thành phố nhận hàng và địa chỉ nhận hàng. | Dữ liệu | L94-95 | Không có |
| REQ-46 | Thông tin thẻ gồm tên chủ thẻ, mã thẻ, ngân hàng phát hành, ngày hết hạn và mã bảo mật. | Dữ liệu | L96-97 | Không có |
| REQ-47 | Khách hàng yêu cầu đặt hàng từ giỏ hàng đang xem. | Chức năng | "khách hàng phải xem giỏ hàng trước tiên, và từ giao diện này, khách hàng có thể yêu cầu đặt hàng" (L101-102) | Không có |
| REQ-48 | Mỗi khi khách hàng yêu cầu đặt hàng, hệ thống kiểm tra lượng hàng tồn kho có đủ cung cấp. | Chức năng | L102-103 | Không có |
| REQ-49 | Khi tồn kho không đủ, hệ thống yêu cầu khách hàng cập nhật lại giỏ hàng và hiển thị số lượng tồn kho của mỗi sản phẩm không đáp ứng. | Chức năng | L103-105 | Q-19 |
| REQ-50 | Sau khi cập nhật giỏ hàng, khách hàng phải yêu cầu đặt hàng lại để tiếp tục. | Quy tắc nghiệp vụ | L105-106 | Không có |
| REQ-51 | Hệ thống yêu cầu khách hàng cập nhật thông tin giao hàng và chỉ dẫn giao hàng (không bắt buộc). | Chức năng | "hệ thống sẽ yêu cầu khách hàng cập nhật thông tin giao hàng (delivery info) và chỉ dẫn giao hàng (delivery instructions) nếu có" (L108-109) | Không có |
| REQ-52 | Khách hàng có thể chọn phương thức giao hàng nhanh. | Chức năng | "Khách hàng có thể chọn phương thức giao hàng nhanh (rush order)" (L109-110) | Không có |
| REQ-53 | Giao hàng nhanh cho phép khách hàng nhận hàng vào thời gian hẹn trước. | Quy tắc nghiệp vụ | L110 | Không có |
| REQ-54 | Chỉ địa chỉ nhận hàng ở Hà Nội được hỗ trợ giao hàng nhanh. | Quy tắc nghiệp vụ | "Hiện tại, chỉ những địa chỉ nhận hàng ở Hà Nội được hỗ trợ" (L110-111) | Q-09 |
| REQ-55 | Hệ thống kiểm tra thông tin giao hàng và yêu cầu khách hàng cập nhật lại khi có trường bắt buộc bị bỏ trống hoặc thông tin không hợp lệ. | Chức năng | L111-113 | Q-10 |
| REQ-56 | Hệ thống kiểm tra khách hàng có chọn giao hàng nhanh. | Chức năng | L113-114 | Không có |
| REQ-57 | Khi khách hàng chọn giao hàng nhanh, hệ thống kiểm tra có sản phẩm nào và địa chỉ nhận hàng có hỗ trợ giao hàng nhanh. | Chức năng | L116-117 | Q-08 |
| REQ-58 | Khi không có sản phẩm nào hỗ trợ hoặc địa chỉ không hỗ trợ giao hàng nhanh, hệ thống yêu cầu khách hàng cập nhật lại thông tin giao hàng. | Chức năng | L117-118 | Không có |
| REQ-59 | Khi có sản phẩm và địa chỉ hỗ trợ giao hàng nhanh, hệ thống yêu cầu khách hàng cập nhật thông tin giao hàng nhanh (thông tin giao hàng, chỉ dẫn giao hàng, thời gian nhận hàng). | Chức năng | L118-121 | Không có |
| REQ-60 | Sản phẩm hỗ trợ giao hàng nhanh được giao cùng nhau tới địa điểm nhận hàng nhanh vào thời điểm đã hẹn; sản phẩm không hỗ trợ được giao như bình thường. | Quy tắc nghiệp vụ | L123-128 | Không có |
| REQ-61 | Hệ thống tính phí giao hàng sau khi thông tin giao hàng (và thông tin giao hàng nhanh khi có) được xác nhận. | Chức năng | "Sau đó hệ thống sẽ cập nhật cách tính phí giao hàng và sẽ bắt đầu tính phí giao hàng" (L130); "hệ thống sẽ bắt đầu tính phí giao hàng luôn" (L132-133) | Không có |
| REQ-62 | Phí giao hàng phụ thuộc vào khối lượng sản phẩm và địa điểm nhận hàng. | Quy tắc nghiệp vụ | L135 | Không có |
| REQ-63 | Phí giao hàng không bị tính thuế. | Quy tắc nghiệp vụ | L137 | Không có |
| REQ-64 | Đơn hàng có tổng giá sản phẩm trên 100.000 VNĐ được miễn phí vận chuyển. | Quy tắc nghiệp vụ | "Đơn hàng có tổng giá cả các sản phẩm đạt trên 100.000VNĐ sẽ được miễn phí vận chuyển" (L138) | Q-06 |
| REQ-65 | Chỉ tính phí giao hàng với sản phẩm có khối lượng lớn nhất. | Quy tắc nghiệp vụ | L142 | Q-05 |
| REQ-66 | Địa chỉ nhận hàng ở nội thành TP. Hà Nội hoặc nội thành TP.HCM có giá khởi điểm 22.000 VNĐ cho 3 kg đầu. | Quy tắc nghiệp vụ | L143-145 | Không có |
| REQ-67 | Địa chỉ nhận hàng ở vị trí khác trong lãnh thổ Việt Nam có giá khởi điểm 30.000 VNĐ cho 0,5 kg đầu. | Quy tắc nghiệp vụ | L147-149 | Không có |
| REQ-68 | Mỗi 0,5 kg tiếp theo tính thêm 2.500 VNĐ. | Quy tắc nghiệp vụ | L151 | Không có |
| REQ-69 | Khách hàng chọn giao hàng nhanh trả thêm 10.000 VNĐ cho mỗi sản phẩm giao hàng nhanh. | Quy tắc nghiệp vụ | L152-154 | Q-06 |
| REQ-70 | Sau khi tính phí giao hàng, hệ thống hiển thị và lưu thông tin đơn hàng tạm thời (invoice). | Chức năng | L156 | Không có |
| REQ-71 | Đơn hàng tạm thời gồm danh sách sản phẩm trong giỏ hàng, số lượng, giá sản phẩm, tổng giá chưa gồm VAT, tổng giá đã gồm VAT, phí giao hàng và tổng số tiền phải trả. | Dữ liệu | L156-159 | Không có |
| REQ-72 | Tổng số tiền phải trả bằng tổng giá sản phẩm đã gồm VAT cộng phí giao hàng. | Quy tắc nghiệp vụ | L159-160 | Không có |
| REQ-73 | Hệ thống cho phép khách hàng thanh toán đơn hàng sau khi hiển thị đơn hàng tạm thời. | Chức năng | "Sau đó, hệ thống sẽ cho phép khách hàng thanh toán đơn hàng" (L160) | Q-20 |
| REQ-74 | Khách hàng chọn phương thức thanh toán. | Chức năng | "khách hàng cần chọn phương thức thanh toán" (L162) | Không có |
| REQ-75 | Khách hàng chỉ thanh toán bằng nội tệ (VND) bằng "thẻ tín dụng trả trước" liên kết với liên ngân hàng. | Quy tắc nghiệp vụ | L162-164 | Q-16 |
| REQ-76 | Hệ thống yêu cầu khách hàng cung cấp thông tin giao dịch gồm thông tin thẻ và nội dung giao dịch. | Chức năng | L164-165 | Không có |
| REQ-77 | Hệ thống trao đổi thông tin giao dịch thẻ với liên ngân hàng để thanh toán đơn hàng. | Giao tiếp ngoài | "bằng cách liên kết với liên ngân hàng" (L163-164); L204-207 | Không có |
| REQ-78 | Thời gian đáp ứng cho mọi giao dịch không quá 2 giây. | Phi chức năng | "Thời gian đáp ứng cho mọi giao dịch không được phép quá 2 giây" (L165-166) | Không có |
| REQ-79 | Sau khi thanh toán thành công, hệ thống hiển thị mã giao dịch, tên chủ thẻ, số tiền bị trừ, nội dung giao dịch, số dư và ngày giờ giao dịch. | Chức năng | L168-169 | Không có |
| REQ-80 | Hệ thống lưu thông tin giao dịch và đơn hàng sau khi thanh toán thành công. | Dữ liệu | "hệ thống ghi lại thông tin giao dịch và đơn hàng" (L169-170) | Không có |
| REQ-81 | Khách hàng có thể xem lại lịch sử mua hàng. | Chức năng | "để khách hàng có thể xem lại lịch sử mua hàng" (L170) | Không có |
| REQ-82 | Hệ thống chuyển đơn hàng sang trạng thái chờ xử lý sau khi thanh toán thành công. | Chức năng | "Đơn hàng sẽ vào trạng thái chờ xử lý" (L170-171) | Q-18 |
| REQ-83 | Hệ thống gửi thông tin đơn hàng và thông tin giao dịch tới hòm thư điện tử của khách hàng. | Chức năng | L171-172 | Q-04, Q-07 |
| REQ-84 | Quản trị viên có thể phê duyệt hoặc từ chối đơn hàng đang chờ xử lý. | Chức năng | L174-175 | Không có |
| REQ-85 | Quản trị viên có thể xem danh sách đơn hàng đang chờ xử lý. | Chức năng | L175-177 | Không có |
| REQ-86 | Mỗi trang danh sách đơn hàng chờ xử lý hiển thị 30 đơn. | Quy tắc nghiệp vụ | "thấy 30 đơn đặt hàng đang chờ xử lý trên mỗi trang" (L176-177) | Tách từ REQ-85 |
| REQ-87 | Quản trị viên có thể xem chi tiết đơn hàng bằng cách chọn ID đơn. | Chức năng | L177-178 | Không có |
| REQ-88 | Quản trị viên được từ chối đơn hàng kể cả khi đủ sản phẩm trong kho. | Quy tắc nghiệp vụ | L178-180 | Không có |
| REQ-89 | Hệ thống từ chối việc chấp nhận đơn hàng khi không đủ sản phẩm trong kho. | Quy tắc nghiệp vụ | L180-181 | Không có |
| REQ-90 | Khách hàng có thể huỷ đơn hàng sau khi thanh toán. | Chức năng | "hệ thống cũng cho phép khách hàng hủy đơn hàng sau khi thanh toán" (L183) | Q-14 |
| REQ-91 | Khi đơn hàng bị huỷ, toàn bộ số tiền được hoàn trả vào thẻ tín dụng đã dùng để thanh toán đơn hàng đó. | Quy tắc nghiệp vụ | L183-184 | Q-21 |
| REQ-92 | Khách hàng có thể trở về bất kỳ bước nào khi đặt hàng. | Chức năng | L186 | Không có |
| REQ-93 | Khách hàng không cần tạo tài khoản để đặt hàng và thanh toán. | Ràng buộc | L188 | Mâu thuẫn với REQ-44; Q-02 |
| REQ-94 | Hệ thống không có chức năng đăng ký, đăng nhập cho khách hàng. | Ràng buộc | L188-189 | Ngoài phạm vi |
| REQ-95 | Hệ thống thanh toán qua thẻ tín dụng giả lập. | Ràng buộc | L193-194 | Không có |
| REQ-96 | Thẻ tín dụng ảo có số tiền mặc định 1.000.000 VNĐ. | Dữ liệu | L197 | Không có |
| REQ-97 | Hệ thống dùng private token của thẻ tín dụng ảo khi thao tác với thẻ qua liên ngân hàng. | Giao tiếp ngoài | L198-200 | Không có |
| REQ-98 | Liên ngân hàng cung cấp API trừ tiền để thanh toán. | Giao tiếp ngoài | "API trừ tiền (sử dụng để đặt cọc tiền khi thuê xe và thanh toán số tiền của một lần thuê)" (L207) | Q-17 |
| REQ-99 | Liên ngân hàng cung cấp API cộng tiền để hoàn trả tiền. | Giao tiếp ngoài | "API cộng tiền (sử dụng để thực hoàn trả lại tiền cọc cho khách hàng)" (L208) | Q-17 |
| REQ-100 | Liên ngân hàng cung cấp API reset số dư thẻ về mặc định để kiểm thử. | Giao tiếp ngoài | L209-210 | Ngoài phạm vi (chỉ phục vụ kiểm thử) |
| REQ-101 | Liên ngân hàng cung cấp API xem số dư thẻ. | Giao tiếp ngoài | L212 | Không có |

## 5. Vấn đề chất lượng của tài liệu nguồn

| STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
|---|---|---|---|---|---|
| 1 | Mâu thuẫn | REQ-29, REQ-30 | L13: "thay vì các tính năng liên quan tới xác thực tài khoản hay quản lý người dùng, chúng ta sẽ tập trung vào..."; L66-69 mô tả chi tiết quản lý người dùng | L13 được đọc là câu loại trừ; ghi Ngoài phạm vi, chờ xác nhận | Q-01 |
| 2 | Mâu thuẫn | REQ-44, REQ-93, REQ-94 | L90-99: "khách hàng có đăng nhập tài khoản"; L188-189: "không có chức năng cho phép khách hàng đăng ký, đăng nhập" | Giữ cả hai REQ, chờ xác nhận | Q-02 |
| 3 | Thiếu | REQ-42 | L85-87 nêu bước vận chuyển và hỗ trợ sau đặt hàng nhưng không mô tả hành vi nào | Không tạo REQ chức năng | Q-03 |
| 4 | Thiếu | REQ-83 | L171-172 gửi tới "hòm thư điện tử của khách hàng" nhưng thông tin giao hàng (L94-95) không có địa chỉ email | Chờ trả lời | Q-04 |
| 5 | Mơ hồ | REQ-65 | L142: "Chỉ tính phí giao hàng với sản phẩm có khối lượng lớn nhất" | Giữ nguyên câu | Q-05 |
| 6 | Mơ hồ | REQ-64, REQ-69 | L138: "tổng giá cả các sản phẩm" không nói trước hay sau VAT; không nói phụ phí giao nhanh có được miễn | Giữ nguyên câu | Q-06 |
| 7 | Thiếu | REQ-30, REQ-83 | "hệ thống sẽ tự động gửi email" (L68), "gửi ... tới hòm thư điện tử" (L171) không nêu hệ thống gửi email là bên ngoài hay bên trong | Chờ trả lời | Q-07 |
| 8 | Thiếu | REQ-57 | L116: "kiểm tra xem có sản phẩm nào ... hỗ trợ giao hàng nhanh" nhưng dữ liệu sản phẩm (REQ-16 đến REQ-23) không có thuộc tính hỗ trợ giao nhanh | Chờ trả lời | Q-08 |
| 9 | Mơ hồ | REQ-54 | L111 "ở Hà Nội" trong khi L143 phân biệt "nội thành TP. Hà Nội" | Giữ nguyên câu | Q-09 |
| 10 | Thiếu | REQ-55 | L112-113 "trường bắt buộc", "thông tin không hợp lệ" không nêu trường nào bắt buộc, điều kiện hợp lệ | Chờ trả lời | Q-10 |
| 11 | Mơ hồ | REQ-14, REQ-28 | L25-26 "không thể xóa hoặc cập nhật quá 30 sản phẩm" không có đơn vị thời gian; L64 "định dạng ngày tháng" không nêu định dạng | Giữ nguyên câu | Q-11 |
| 12 | Mơ hồ | REQ-33 | L72 "các đặc tính của sản phẩm" không nêu đặc tính nào | Giữ nguyên câu | Q-12 |
| 13 | Mơ hồ | REQ-38 | L80-81 "hiện ra số lượng này của từng sản phẩm bị thiếu": số lượng tồn hay số lượng thiếu | L104 ghi "số lượng hàng tồn kho", có thể hoà giải | Q-13 |
| 14 | Thiếu | REQ-90 | L183 không nêu huỷ được tới thời điểm nào (trước hay sau khi duyệt, giao) và khách hàng chỉ định đơn cần huỷ bằng cách nào | Chờ trả lời | Q-14 |
| 15 | Không kiểm chứng được | REQ-01, REQ-03, REQ-04, REQ-07 | "đa nền tảng", "dễ dàng", "đáng kể", "cao điểm" | Giữ nguyên câu | Q-15 |
| 16 | Mơ hồ | REQ-75 | L163 "thẻ tín dụng trả trước" ghép hai loại thẻ khác nhau | Giữ nguyên câu | Q-16 |
| 17 | Mâu thuẫn | REQ-98, REQ-99 | L207 "đặt cọc tiền khi thuê xe", L208 "hoàn trả lại tiền cọc" không thuộc miền bán hàng | Giữ chức năng API, bỏ mô tả mục đích | Q-17 |
| 18 | Thiếu | REQ-82 | Chỉ nêu trạng thái "chờ xử lý"; không nêu trạng thái sau phê duyệt, từ chối, huỷ | Chờ trả lời | Q-18 |
| 19 | Thiếu | REQ-49 | L105 "Sau khi cập nhật giỏ hàng" gợi ý khách hàng cập nhật số lượng trong giỏ, trong khi L81 chỉ nêu bỏ sản phẩm | Chờ trả lời | Q-19 |
| 20 | Thiếu | REQ-73 | Không nêu đơn hàng tạm thời chưa thanh toán có được thanh toán sau không, và điều gì xảy ra khi thanh toán thất bại | Chờ trả lời | Q-20 |
| 21 | Thiếu | REQ-91 | Không nêu xử lý khi hoàn tiền qua liên ngân hàng thất bại | Chờ trả lời | Q-21 |

## 6. Ma trận phủ nguồn

| Vị trí trong nguồn | Tóm tắt nội dung | Kết luận |
|---|---|---|
| L1-11 | Tên dự án, động cơ, loại hệ thống | Bối cảnh |
| L13-15 | Trọng tâm đặt hàng, thanh toán; loại trừ xác thực, quản lý người dùng | Ngoài phạm vi (xác thực, quản lý người dùng); Q-01 |
| L17-21 | Đa nền tảng, 24/7, dễ làm quen, 1000 khách, 300 giờ, phục hồi 1 giờ, đáp ứng 1-2 giây | REQ-01 đến REQ-07 |
| L23-27 | Quản trị viên thêm, xem, sửa, xoá sản phẩm và giới hạn số lượng | REQ-08 đến REQ-15 |
| L29-33 | Thông tin chung của sản phẩm, VAT | REQ-16, REQ-17 |
| L35-49 | Thông tin riêng của sách, CD, LP, DVD | REQ-18 đến REQ-21 |
| L51-55 | Chỉ bán sản phẩm vật lý, thông tin sản phẩm vật lý | REQ-22, REQ-23 |
| L57-60 | Cập nhật giá 2 lần/ngày, khoảng giá 30%-150% | REQ-10, REQ-24, REQ-25 |
| L62-64 | Lưu lịch sử thao tác, thông báo thao tác không hợp lệ | REQ-26, REQ-27, REQ-28 |
| L66-69 | Quản lý người dùng, email thông báo | REQ-29, REQ-30 (chờ Q-01) |
| L71-75 | Danh sách khởi động, tìm kiếm, sắp xếp, thêm vào giỏ | REQ-31 đến REQ-35 |
| L77-83 | Xem giỏ, thông báo thiếu hàng, bỏ sản phẩm, 1 giỏ, làm trống giỏ | REQ-36 đến REQ-41 |
| L85-87 | 5 bước của quá trình đặt hàng | REQ-42 |
| L89-99 | Đặt hàng thành công gồm 2 bước; lưu thông tin mặc định; dữ liệu giao hàng, thẻ | REQ-43 đến REQ-46 |
| L101-106 | Yêu cầu đặt hàng từ giỏ, kiểm tra tồn kho, cập nhật giỏ | REQ-47 đến REQ-50 |
| L108-114 | Cập nhật thông tin giao hàng, chọn giao nhanh, kiểm tra thông tin | REQ-51 đến REQ-56 |
| L116-133 | Giao hàng nhanh, cập nhật cách tính phí | REQ-57 đến REQ-61 |
| L135-154 | Quy tắc phí giao hàng | REQ-62 đến REQ-69 |
| L156-160 | Đơn hàng tạm thời, tổng tiền, cho phép thanh toán | REQ-70 đến REQ-73 |
| L162-166 | Chọn phương thức, thẻ tín dụng, thông tin giao dịch, 2 giây | REQ-74 đến REQ-78 |
| L168-172 | Kết quả giao dịch, lưu, lịch sử mua hàng, chờ xử lý, email | REQ-79 đến REQ-83 |
| L174-181 | Phê duyệt, danh sách 30 đơn, chi tiết, quy tắc chấp nhận | REQ-84 đến REQ-89 |
| L183-184 | Huỷ đơn, hoàn tiền | REQ-90, REQ-91 |
| L186 | Trở về bất kỳ bước nào khi đặt hàng | REQ-92 |
| L188-189 | Không cần tài khoản, không có đăng ký, đăng nhập | REQ-93, REQ-94 |
| L193-202 | Thẻ tín dụng giả lập, thông tin thẻ ảo cấp cho nhóm | REQ-95, REQ-96, REQ-97; phần "Mỗi nhóm sẽ được cấp", "Các thông tin khác" là Bối cảnh |
| L204-212 | Các API liên ngân hàng | REQ-98 đến REQ-101 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-01 | Chức năng quản lý người dùng (L66-69) có thuộc phạm vi xây dựng không? (Có / Không) | REQ-29, REQ-30; danh sách use case ở P02 | L13 và L66-69 |
| Q-02 | Hệ thống có phân biệt khách hàng đăng nhập và không đăng nhập không? (Có / Không; nếu Không thì thông tin mặc định chỉ lưu ở bộ nhớ thiết bị) | REQ-44, REQ-93; tác nhân ở P01 | L90-99 và L188-189 |
| Q-03 | Bước vận chuyển và hỗ trợ sau đặt hàng có thuộc phạm vi không? (Có / Không) | REQ-42; danh sách use case | L85-87 |
| Q-04 | Địa chỉ email của khách hàng được lấy từ đâu? (Khách hàng nhập khi đặt hàng / Khác) | REQ-83; dữ liệu vào của đặt hàng, thanh toán | L171-172 |
| Q-05 | "Chỉ tính phí giao hàng với sản phẩm có khối lượng lớn nhất" nghĩa là phí tính theo khối lượng của riêng sản phẩm nặng nhất, hay theo cách khác? | REQ-65; BR phí giao hàng | L142 |
| Q-06 | Ngưỡng 100.000 VNĐ miễn phí vận chuyển tính trên tổng giá trước hay sau VAT, và có miễn phụ phí giao nhanh 10.000 VNĐ/sản phẩm không? | REQ-64, REQ-69 | L138, L152 |
| Q-07 | Việc gửi email do AIMS tự thực hiện hay qua một hệ thống gửi email bên ngoài? | REQ-30, REQ-83; tác nhân ở P01 | L68, L171 |
| Q-08 | Hệ thống biết sản phẩm nào hỗ trợ giao hàng nhanh dựa trên thông tin nào? | REQ-57; dữ liệu sản phẩm | L116 |
| Q-09 | Giao hàng nhanh hỗ trợ toàn TP. Hà Nội hay chỉ nội thành? | REQ-54 | L111, L143 |
| Q-10 | Trường nào của thông tin giao hàng là bắt buộc, và điều kiện hợp lệ của từng trường là gì? | REQ-55; dữ liệu vào của đặt hàng | L112-113 |
| Q-11 | Giới hạn 30 sản phẩm xoá hoặc cập nhật có tính theo ngày không, và định dạng ngày tháng là gì? | REQ-14, REQ-28 | L25-26, L64 |
| Q-12 | Khách hàng tìm kiếm theo những đặc tính nào của sản phẩm? | REQ-33 | L72 |
| Q-13 | Khi thiếu hàng, hệ thống hiển thị số lượng tồn kho hay số lượng còn thiếu? | REQ-38, REQ-49 | L80-81, L104 |
| Q-14 | Khách hàng được huỷ đơn hàng đã thanh toán tới thời điểm nào (khi đơn còn chờ xử lý / khi đã phê duyệt / bất kỳ lúc nào), và chỉ định đơn cần huỷ bằng cách nào? | REQ-90; đặc tả huỷ đơn | L183 |
| Q-15 | Ngưỡng cụ thể của "đa nền tảng", "dễ dàng", "không giảm đáng kể", "cao điểm" là gì? | REQ-01, REQ-03, REQ-04, REQ-07 | L17-21 |
| Q-16 | Thẻ dùng để thanh toán là thẻ tín dụng hay thẻ trả trước? | REQ-75 | L163 |
| Q-17 | Mô tả mục đích API trừ tiền, cộng tiền ("thuê xe", "tiền cọc") có phải chép nhầm từ đề khác không? | REQ-98, REQ-99 | L207-208 |
| Q-18 | Đơn hàng có những trạng thái nào ngoài "chờ xử lý" (đã phê duyệt, bị từ chối, đã huỷ...)? | REQ-82, REQ-84, REQ-90 | L170-171 |
| Q-19 | Khách hàng có được thay đổi số lượng sản phẩm trong giỏ không? (Có / Không) | REQ-49; use case giỏ hàng | L81, L105 |
| Q-20 | Khi thanh toán thất bại, đơn hàng tạm thời được giữ để thanh toán sau hay bị huỷ? | REQ-73; đặc tả đặt hàng, thanh toán | L156-166 |
| Q-21 | Khi liên ngân hàng hoàn tiền thất bại, đơn hàng có bị huỷ không và khách hàng được thông báo thế nào? | REQ-91; đặc tả huỷ đơn | L183-184 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 7: các từ "dễ dàng", "đáng kể", "cao điểm", "đa nền tảng" đã có Q-15; từ "mọi giao dịch" (REQ-78) là tổng thể tuyệt đối nhưng không có dấu hiệu ngoại lệ trong nguồn, không tạo câu hỏi riêng.
- REQ-44 chứa hai nhánh (có đăng nhập, không đăng nhập) trong một câu vì cả hai phụ thuộc cùng câu hỏi Q-02; tách khi Q-02 được trả lời.
