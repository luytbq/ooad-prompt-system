# P00 - Chuẩn hoá yêu cầu - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P00 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-khach.md (tài liệu nguồn duy nhất); trường HE_THONG_NGOAI của project-profile.md |
| Phạm vi | Toàn hệ thống |
| Mã Q, ASM cuối đã cấp | Q-37, ASM-09 |

## 1. Bối cảnh và mục tiêu nghiệp vụ

Nhà xe SaoViet khai thác 12 tuyến xe khách liên tỉnh xuất phát từ 3 bến xe, mỗi ngày khoảng 80 chuyến, với đội xe gồm xe giường nằm và xe ghế ngồi. Hiện vé được bán qua điện thoại và quầy tại bến, ghi sổ tay, và thường xuyên bị trùng chỗ. Nhà xe cần phần mềm bán vé và quản lý chuyến để hành khách đặt và thanh toán vé trực tuyến, nhân viên bán vé, lập lịch chạy và soát vé, quản lý xem báo cáo.

Mục tiêu nghiệp vụ:

- Có phần mềm bán vé và quản lý chuyến thay cho cách bán qua điện thoại và quầy ghi sổ tay (nguồn: Đoạn mở đầu, câu 3 và câu 4).
- Chấm dứt tình trạng trùng chỗ: "Không được để hai vé cùng một chỗ trên một chuyến" (nguồn: Mục 10, câu 2; Đoạn mở đầu, câu 3 "thường xuyên bị trùng chỗ").
- Cho hành khách đặt và thanh toán vé qua website (nguồn: Mục 1, câu 1; Mục 3, câu 1).

## 2. Phạm vi

Trong phạm vi:

- Tìm chuyến, xem sơ đồ chỗ, chọn chỗ, đặt vé qua website, không bắt buộc có tài khoản: REQ-04 đến REQ-09.
- Tài khoản hành khách và lịch sử vé: REQ-10, REQ-11, REQ-12 (ASM-01).
- Giữ chỗ, thanh toán trực tuyến, phát hành vé, gửi mã vé qua SMS: REQ-13 đến REQ-21.
- Bán vé tại quầy, in vé giấy, nhận đặt chỗ qua điện thoại, thanh toán và tự huỷ vé đặt qua điện thoại: REQ-22, REQ-25 đến REQ-28, REQ-30 đến REQ-32; đăng nhập và quản lý tài khoản nhân viên nhà xe: REQ-23, REQ-24 (ASM-02); chọn chuyến và chỗ cho khách: REQ-29 (ASM-03).
- Trả vé, đổi vé, hoàn tiền: REQ-33, REQ-34, REQ-37 đến REQ-44; trả vé, đổi vé tại quầy: REQ-35, REQ-36 (ASM-04); đổi sang vé rẻ hơn: REQ-45 (ASM-05).
- Lập lịch chạy theo tuần, ràng buộc xe và tài xế, huỷ chuyến, SMS và hoàn tiền khi huỷ chuyến: REQ-46, REQ-47, REQ-52 đến REQ-58; quản lý danh mục tuyến, bến xe, xe, tài xế: REQ-48 đến REQ-50 (ASM-06); phụ xe của chuyến: REQ-51 (ASM-07); kênh hoàn tiền khi huỷ chuyến: REQ-59 (ASM-08).
- Giá vé và mức tăng giá ngày lễ, Tết: REQ-60 đến REQ-62.
- Soát vé bằng máy soát vé cầm tay, gồm soát khi mất sóng và gửi danh sách hành khách về máy: REQ-63 đến REQ-70, REQ-77.
- Báo cáo doanh thu và tỉ lệ lấp đầy: REQ-71 đến REQ-73 (ASM-09).
- Quy mô và chất lượng: REQ-01 đến REQ-03, REQ-74 đến REQ-76.

Ngoài phạm vi (hệ thống, thiết bị khác mà hệ thống này chỉ trao đổi dữ liệu):

- Xử lý thanh toán trực tuyến và thông tin thẻ do cổng thanh toán trực tuyến của đối tác đảm nhiệm (nguồn: "qua cổng thanh toán trực tuyến của đối tác", Mục 3, câu 1; "Hệ thống không lưu thông tin thẻ của hành khách", Mục 10, câu 3).
- Truyền tin nhắn SMS qua mạng viễn thông do cổng SMS của nhà mạng đảm nhiệm (nguồn: project-profile.md, HE_THONG_NGOAI).
- Cung cấp phần cứng máy soát vé cầm tay Android: "do nhà xe tự trang bị" (nguồn: project-profile.md, HE_THONG_NGOAI).
- Cung cấp phần cứng máy in vé nhiệt tại quầy (nguồn: project-profile.md, HE_THONG_NGOAI).

Chờ Q-nn: Không có. Nguồn không có câu phạm vi nào mâu thuẫn với mô tả chi tiết.

## 3. Các bên liên quan và người dùng

| SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống | REQ |
|---|---|---|---|---|---|
| SH-01 | Nhà xe SaoViet (tổ chức khai thác tuyến, đặt hàng phần mềm) | Chủ sở hữu, người đặt hàng | Hết trùng chỗ, bán vé và quản lý chuyến bằng phần mềm | Chưa rõ | REQ-01, REQ-02, REQ-03, REQ-75 |
| SH-02 | Hành khách (gồm người đi nhận SMS) | Người dùng trực tiếp | Tìm chuyến, đặt, thanh toán, trả, đổi vé thuận tiện, có vé đúng chỗ | Có | REQ-04 đến REQ-21, REQ-33 đến REQ-45 |
| SH-03 | Cổng thanh toán trực tuyến của đối tác | Hệ thống hoặc thiết bị ngoài | Nhận yêu cầu thu tiền và hoàn tiền từ hệ thống | Có | REQ-15, REQ-16, REQ-40, REQ-76 |
| SH-04 | Cổng SMS của nhà mạng | Hệ thống hoặc thiết bị ngoài | Nhận nội dung SMS cần gửi tới hành khách | Có | REQ-12, REQ-20, REQ-21, REQ-56 |
| SH-05 | Nhân viên bán vé | Người dùng trực tiếp | Bán vé tại quầy, nhận đặt chỗ qua điện thoại, thu và hoàn tiền mặt | Có | REQ-22 đến REQ-32, REQ-35, REQ-36, REQ-41 |
| SH-06 | Máy in vé nhiệt tại quầy | Hệ thống hoặc thiết bị ngoài | Nhận dữ liệu vé để in vé giấy có mã vạch | Có | REQ-26, REQ-27 |
| SH-07 | Nhân viên điều hành | Người dùng trực tiếp | Lập lịch chạy đúng ràng buộc xe, tài xế; huỷ chuyến khi cần | Có | REQ-46 đến REQ-59 |
| SH-08 | Tài xế | Người hưởng lợi gián tiếp | Lịch lái không chồng nhau, không quá 10 giờ một ngày | Chưa rõ | REQ-47, REQ-50, REQ-53, REQ-54 |
| SH-09 | Quản lý nhà xe | Người vận hành, quản trị | Đặt giá vé, mức tăng giá, xem báo cáo doanh thu và tỉ lệ lấp đầy | Có | REQ-24, REQ-60 đến REQ-62, REQ-71 đến REQ-73 |
| SH-10 | Phụ xe | Người dùng trực tiếp | Soát vé nhanh, kể cả khi mất sóng | Có | REQ-51, REQ-63, REQ-65 đến REQ-70 |
| SH-11 | Máy soát vé cầm tay Android | Hệ thống hoặc thiết bị ngoài | Nhận danh sách hành khách, gửi lại kết quả soát vé | Có | REQ-64, REQ-67 đến REQ-70, REQ-77 |

## 4. Danh sách yêu cầu

| REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |
|---|---|---|---|---|
| REQ-01 | Hệ thống quản lý 12 tuyến xe khách liên tỉnh xuất phát từ 3 bến xe. | Dữ liệu | "Nhà xe SaoViet khai thác 12 tuyến xe khách liên tỉnh xuất phát từ 3 bến xe" (Đoạn mở đầu, câu 1) | Số liệu quy mô. Ai quản lý danh mục: ASM-06 |
| REQ-02 | Hệ thống quản lý khoảng 80 chuyến xe mỗi ngày. | Dữ liệu | "mỗi ngày khoảng 80 chuyến" (Đoạn mở đầu, câu 1) | Số liệu quy mô. Tách từ cùng câu với REQ-01 |
| REQ-03 | Hệ thống quản lý đội xe gồm khoảng 50 xe giường nằm 40 chỗ và 20 xe ghế ngồi 29 chỗ. | Dữ liệu | "Đội xe gồm khoảng 50 xe giường nằm 40 chỗ và 20 xe ghế ngồi 29 chỗ" (Đoạn mở đầu, câu 2) | Số liệu quy mô. Chưa tách theo loại xe vì nguồn không phân biệt. Xem ASM-06 |
| REQ-04 | Hành khách có thể đặt vé chuyến xe qua website, không bắt buộc có tài khoản. | Chức năng | "Hành khách đặt vé qua website." (Mục 1, câu 1)<br>"đặt vé không bắt buộc có tài khoản" (Mục 2, câu 2) | Kênh: website. Điều kiện vai trò gộp theo F3. Xem Q-13 |
| REQ-05 | Hành khách có thể tìm chuyến theo điểm đi, điểm đến và ngày đi mà không cần tài khoản. | Chức năng | "Hành khách tìm chuyến theo điểm đi, điểm đến và ngày đi" (Mục 1, câu 2)<br>"Việc tìm chuyến và xem chỗ trống không cần tài khoản." (Mục 1, câu 3) | Xem Q-10 |
| REQ-06 | Hành khách có thể xem sơ đồ chỗ của chuyến, trong đó thể hiện các chỗ còn trống, mà không cần tài khoản. | Chức năng | "xem sơ đồ chỗ của chuyến với các chỗ còn trống" (Mục 1, câu 2)<br>"Việc tìm chuyến và xem chỗ trống không cần tài khoản." (Mục 1, câu 3) | Sơ đồ chỗ theo loại xe: xem ASM-06 |
| REQ-07 | Hành khách có thể chọn chỗ còn trống trên sơ đồ chỗ của chuyến khi đặt vé. | Chức năng | "rồi chọn tối đa 5 chỗ trong một lần đặt" (Mục 1, câu 2) | Tách từ cùng câu với REQ-08 |
| REQ-08 | Hành khách chọn tối đa 5 chỗ trong một lần đặt. | Quy tắc nghiệp vụ | "rồi chọn tối đa 5 chỗ trong một lần đặt" (Mục 1, câu 2) | Tách từ cùng câu với REQ-07. Xem Q-12 |
| REQ-09 | Thông tin người đi khi đặt vé gồm họ tên và số điện thoại. | Dữ liệu | "Khi đặt vé, hành khách nhập họ tên và số điện thoại của người đi." (Mục 2, câu 1) | Xem Q-11 |
| REQ-10 | Hành khách có thể đăng ký tài khoản bằng số điện thoại. | Chức năng | "Hành khách có thể đăng ký tài khoản bằng số điện thoại" (Mục 2, câu 2) | Xem Q-04 |
| REQ-11 | Hành khách có tài khoản có thể xem lại lịch sử vé. | Chức năng | "để xem lại lịch sử vé" (Mục 2, câu 2) | Tách từ cùng câu với REQ-10. Xem Q-26 |
| REQ-12 | Hành khách có thể đăng nhập bằng mã xác thực gửi qua SMS tới số điện thoại đã đăng ký tài khoản. | Chức năng | Giả định ASM-01 | Chờ Q-04. Kênh: cổng SMS (REQ-21) |
| REQ-13 | Hệ thống giữ các chỗ hành khách đã chọn để hành khách thanh toán. | Chức năng | "Các chỗ đã chọn được giữ trong 10 phút để hành khách thanh toán" (Mục 3, câu 1) | Tách từ cùng câu với REQ-14, REQ-15. Xem Q-18 |
| REQ-14 | Thời gian giữ các chỗ đã chọn là 10 phút. | Quy tắc nghiệp vụ | "Các chỗ đã chọn được giữ trong 10 phút" (Mục 3, câu 1) | Tách từ cùng câu với REQ-13. Xem Q-18 |
| REQ-15 | Hành khách có thể thanh toán vé trực tuyến qua cổng thanh toán trực tuyến của đối tác. | Chức năng | "thanh toán qua cổng thanh toán trực tuyến của đối tác" (Mục 3, câu 1) | Kênh: cổng thanh toán (REQ-16). Xem Q-17, Q-19 |
| REQ-16 | Hệ thống trao đổi thông tin thanh toán và hoàn tiền với cổng thanh toán trực tuyến của đối tác để thu tiền vé và hoàn tiền vé. | Giao tiếp ngoài | "qua cổng thanh toán trực tuyến của đối tác" (Mục 3, câu 1)<br>"Vé mua trực tuyến được hoàn qua cổng thanh toán" (Mục 5, câu 3)<br>project-profile.md, HE_THONG_NGOAI | Hồ sơ ghi "API thanh toán và hoàn tiền, chưa có tài liệu API". Xem Q-20 |
| REQ-17 | Hệ thống trả các chỗ đang giữ cho người khác khi hết thời gian giữ chỗ mà hành khách chưa thanh toán thành công. | Chức năng | "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại cho người khác" (Mục 3, câu 2) | Thời gian giữ theo REQ-14. Xem Q-19 |
| REQ-18 | Hệ thống phát hành vé khi thanh toán thành công. | Chức năng | "Thanh toán thành công thì hệ thống phát hành vé" (Mục 3, câu 3) | Tách từ cùng câu với REQ-19, REQ-20 |
| REQ-19 | Mỗi chỗ có một mã vé. | Quy tắc nghiệp vụ | "mỗi chỗ một mã vé" (Mục 3, câu 3) | Tách từ cùng câu với REQ-18 |
| REQ-20 | Hệ thống gửi mã vé qua SMS tới số điện thoại người đi khi phát hành vé. | Chức năng | "gửi qua SMS tới số điện thoại người đi" (Mục 3, câu 3) | Kênh: cổng SMS (REQ-21). Xem Q-11, Q-35 |
| REQ-21 | Hệ thống trao đổi nội dung tin nhắn SMS với cổng SMS của nhà mạng qua API REST để gửi SMS tới hành khách. | Giao tiếp ngoài | "gửi qua SMS tới số điện thoại người đi" (Mục 3, câu 3)<br>"hệ thống gửi SMS cho mọi hành khách đã có vé" (Mục 6, câu 4)<br>project-profile.md, HE_THONG_NGOAI | Hồ sơ ghi "Cổng SMS của nhà mạng (API REST)" |
| REQ-22 | Nhân viên bán vé có thể bán vé tại quầy cho khách mua trực tiếp. | Chức năng | "Nhân viên bán vé tại quầy bán vé cho khách mua trực tiếp" (Mục 4, câu 1) | Xem Q-13 |
| REQ-23 | Nhân viên nhà xe (nhân viên bán vé, nhân viên điều hành, quản lý nhà xe, phụ xe) có thể đăng nhập vào hệ thống bằng tài khoản riêng theo vai trò. | Chức năng | Giả định ASM-02 | Chờ Q-01 |
| REQ-24 | Quản lý nhà xe có thể quản lý tài khoản của nhân viên nhà xe. | Chức năng | Giả định ASM-02 | Chờ Q-01 |
| REQ-25 | Nhân viên bán vé thu tiền mặt của khách khi bán vé tại quầy. | Chức năng | "thu tiền mặt" (Mục 4, câu 1) | Tách từ cùng câu với REQ-22 |
| REQ-26 | Nhân viên bán vé in vé giấy có mã vạch cho khách mua tại quầy. | Chức năng | "in vé giấy có mã vạch" (Mục 4, câu 1) | Kênh: máy in vé nhiệt (REQ-27). Xem Q-27 |
| REQ-27 | Hệ thống trao đổi dữ liệu vé với máy in vé nhiệt tại quầy để in vé giấy có mã vạch. | Giao tiếp ngoài | "in vé giấy có mã vạch" (Mục 4, câu 1)<br>project-profile.md, HE_THONG_NGOAI | Hồ sơ ghi "Máy in vé nhiệt tại quầy" |
| REQ-28 | Nhân viên bán vé có thể nhận đặt chỗ qua điện thoại. | Chức năng | "Nhân viên bán vé cũng nhận đặt chỗ qua điện thoại" (Mục 4, câu 2) | Xem Q-14 |
| REQ-29 | Nhân viên bán vé có thể chọn chuyến và chỗ còn trống trên sơ đồ chỗ cho khách khi bán vé tại quầy hoặc khi nhận đặt chỗ qua điện thoại. | Chức năng | Giả định ASM-03 | Chờ Q-05. Xem Q-12 |
| REQ-30 | Hành khách có thể thanh toán vé đặt qua điện thoại tại quầy. | Chức năng | "vé đặt qua điện thoại phải được thanh toán tại quầy" (Mục 4, câu 2) | Tách từ cùng câu với REQ-31, REQ-32 |
| REQ-31 | Vé đặt qua điện thoại phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến. | Quy tắc nghiệp vụ | "phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến" (Mục 4, câu 2) | Xem Q-14 |
| REQ-32 | Hệ thống tự động huỷ vé đặt qua điện thoại khi vé chưa được thanh toán tại quầy đúng hạn. | Chức năng | "nếu không sẽ tự động bị huỷ" (Mục 4, câu 2) | Hạn thanh toán theo REQ-31 |
| REQ-33 | Hành khách có thể trả vé. | Chức năng | "Hành khách được đổi hoặc trả vé." (Mục 5, câu 1) | Tách từ cùng câu với REQ-34. Kênh với vé mua trực tuyến: website theo ASM-04. Xem Q-03, Q-37 |
| REQ-34 | Hành khách có thể đổi vé sang chuyến khác cùng tuyến. | Chức năng | "Hành khách được đổi hoặc trả vé." (Mục 5, câu 1)<br>"Mỗi vé chỉ được đổi sang chuyến khác cùng tuyến một lần" (Mục 5, câu 4) | Kênh với vé mua trực tuyến: website theo ASM-04. Xem Q-03, Q-37 |
| REQ-35 | Nhân viên bán vé có thể thực hiện trả vé tại quầy cho hành khách có vé mua tại quầy. | Chức năng | Giả định ASM-04 | Chờ Q-03 |
| REQ-36 | Nhân viên bán vé có thể thực hiện đổi vé tại quầy cho hành khách có vé mua tại quầy. | Chức năng | Giả định ASM-04 | Chờ Q-03 |
| REQ-37 | Hành khách trả vé trước giờ xuất bến từ 24 giờ trở lên được hoàn 90% giá vé. | Quy tắc nghiệp vụ | "Trả vé trước giờ xuất bến từ 24 giờ trở lên được hoàn 90% giá vé" (Mục 5, câu 2) | Tách từ cùng câu với REQ-38, REQ-39 |
| REQ-38 | Hành khách trả vé trước giờ xuất bến từ 4 giờ đến dưới 24 giờ được hoàn 50% giá vé. | Quy tắc nghiệp vụ | "từ 4 giờ đến dưới 24 giờ hoàn 50%" (Mục 5, câu 2) | Tách từ cùng câu với REQ-37 |
| REQ-39 | Vé không được trả khi còn dưới 4 giờ trước giờ xuất bến. | Quy tắc nghiệp vụ | "dưới 4 giờ không được trả" (Mục 5, câu 2) | Tách từ cùng câu với REQ-37 |
| REQ-40 | Hệ thống hoàn tiền vé mua trực tuyến qua cổng thanh toán. | Chức năng | "Vé mua trực tuyến được hoàn qua cổng thanh toán" (Mục 5, câu 3) | Kênh: cổng thanh toán (REQ-16). Xem Q-20 |
| REQ-41 | Vé mua tại quầy được hoàn tiền mặt tại quầy. | Quy tắc nghiệp vụ | "vé mua tại quầy được hoàn tiền mặt tại quầy" (Mục 5, câu 3) | Câu bị động không nêu chủ thể thực hiện. Xem Q-03, ASM-04 |
| REQ-42 | Mỗi vé chỉ được đổi một lần. | Quy tắc nghiệp vụ | "Mỗi vé chỉ được đổi sang chuyến khác cùng tuyến một lần" (Mục 5, câu 4) | Tách từ cùng câu với REQ-34 |
| REQ-43 | Vé chỉ được đổi chậm nhất 4 giờ trước giờ xuất bến. | Quy tắc nghiệp vụ | "chậm nhất 4 giờ trước giờ xuất bến" (Mục 5, câu 4) | Xem Q-21 |
| REQ-44 | Hành khách trả thêm phần chênh lệch khi vé mới đắt hơn vé cũ. | Quy tắc nghiệp vụ | "trả thêm phần chênh lệch nếu vé mới đắt hơn" (Mục 5, câu 4) | Xem Q-22 |
| REQ-45 | Hành khách không được hoàn phần chênh lệch khi vé mới rẻ hơn vé cũ. | Quy tắc nghiệp vụ | Giả định ASM-05 | Chờ Q-08 |
| REQ-46 | Nhân viên điều hành có thể lập lịch chạy theo tuần. | Chức năng | "Nhân viên điều hành lập lịch chạy theo tuần" (Mục 6, câu 1) | Xem Q-01 |
| REQ-47 | Mỗi chuyến trong lịch chạy gồm tuyến, giờ xuất bến, xe và tài xế. | Dữ liệu | "với mỗi chuyến, chọn tuyến, giờ xuất bến, xe và tài xế" (Mục 6, câu 1) | Tách từ cùng câu với REQ-46 |
| REQ-48 | Nhân viên điều hành có thể quản lý danh mục tuyến xe và bến xe. | Chức năng | Giả định ASM-06 | Chờ Q-02 |
| REQ-49 | Nhân viên điều hành có thể quản lý danh mục xe, gồm loại xe, số chỗ và sơ đồ chỗ của từng loại xe. | Chức năng | Giả định ASM-06 | Chờ Q-02 |
| REQ-50 | Nhân viên điều hành có thể quản lý danh mục tài xế. | Chức năng | Giả định ASM-06 | Chờ Q-02 |
| REQ-51 | Mỗi chuyến trong lịch chạy có một phụ xe phụ trách soát vé, do nhân viên điều hành chọn. | Dữ liệu | Giả định ASM-07 | Chờ Q-06 |
| REQ-52 | Một xe không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Quy tắc nghiệp vụ | "Một xe hoặc một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau." (Mục 6, câu 2) | Tách từ cùng câu với REQ-53. Xem Q-15 |
| REQ-53 | Một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Quy tắc nghiệp vụ | "Một xe hoặc một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau." (Mục 6, câu 2) | Tách từ cùng câu với REQ-52. Xem Q-15 |
| REQ-54 | Một tài xế không được lái quá 10 giờ trong một ngày. | Quy tắc nghiệp vụ | "Tài xế không được lái quá 10 giờ trong một ngày." (Mục 6, câu 3) | Xem Q-15, Q-16 |
| REQ-55 | Nhân viên điều hành có thể huỷ một chuyến trong trường hợp phải huỷ chuyến (xe hỏng, thời tiết). | Chức năng | "Khi phải huỷ chuyến (xe hỏng, thời tiết), nhân viên điều hành huỷ chuyến" (Mục 6, câu 4) | Xem Q-36 |
| REQ-56 | Hệ thống gửi SMS cho mọi hành khách đã có vé của chuyến bị huỷ. | Chức năng | "hệ thống gửi SMS cho mọi hành khách đã có vé" (Mục 6, câu 4) | Kênh: cổng SMS (REQ-21). Xem Q-25 |
| REQ-57 | Hệ thống hoàn tiền vé cho hành khách của chuyến bị huỷ. | Chức năng | "hoàn 100% giá vé" (Mục 6, câu 4) | Tách từ cùng câu với REQ-58. Xem Q-07 |
| REQ-58 | Chuyến bị huỷ được hoàn 100% giá vé. | Quy tắc nghiệp vụ | "hoàn 100% giá vé" (Mục 6, câu 4) | Tách từ cùng câu với REQ-57 |
| REQ-59 | Vé của chuyến bị huỷ được hoàn tiền qua cùng kênh với kênh mua vé. | Quy tắc nghiệp vụ | Giả định ASM-08 | Chờ Q-07 |
| REQ-60 | Quản lý nhà xe có thể đặt giá vé theo tuyến và loại xe. | Chức năng | "Giá vé do quản lý nhà xe đặt theo tuyến và loại xe." (Mục 7, câu 1) | Xem Q-01 |
| REQ-61 | Quản lý nhà xe có thể đặt mức tăng giá vé theo phần trăm cho một khoảng ngày lễ, Tết. | Chức năng | "Ngày lễ, Tết, quản lý có thể đặt mức tăng giá theo phần trăm cho một khoảng ngày" (Mục 7, câu 2) | Tách từ cùng câu với REQ-62. "quản lý" hiểu là Quản lý nhà xe theo ASM-09. Xem Q-23, Q-24 |
| REQ-62 | Mức tăng giá vé cho một khoảng ngày tối đa 30%. | Quy tắc nghiệp vụ | "tối đa 30%" (Mục 7, câu 2) | Tách từ cùng câu với REQ-61 |
| REQ-63 | Phụ xe của chuyến có thể quét mã vé bằng máy soát vé cầm tay khi hành khách lên xe. | Chức năng | "Phụ xe mỗi chuyến dùng máy soát vé cầm tay quét mã vé khi hành khách lên xe." (Mục 8, câu 1) | Kênh: máy soát vé (REQ-64). Xem Q-27 |
| REQ-64 | Hệ thống trao đổi dữ liệu vé với máy soát vé cầm tay để soát vé hành khách lên xe. | Giao tiếp ngoài | "máy soát vé cầm tay quét mã vé" (Mục 8, câu 1)<br>project-profile.md, HE_THONG_NGOAI | Hồ sơ ghi "Máy soát vé cầm tay Android có đầu quét mã vạch, do nhà xe tự trang bị". Nền tảng: REQ-77 |
| REQ-65 | Máy soát vé báo kết quả hợp lệ hoặc không hợp lệ cho mã vé đã quét. | Chức năng | "Máy báo hợp lệ hay không hợp lệ" (Mục 8, câu 2) | Tách từ cùng câu với REQ-66 |
| REQ-66 | Mã vé không hợp lệ khi sai chuyến, vé đã huỷ hoặc vé đã soát. | Quy tắc nghiệp vụ | "(sai chuyến, vé đã huỷ, vé đã soát)" (Mục 8, câu 2) | Xem Q-28 |
| REQ-67 | Máy soát vé soát được vé khi xe ở vùng mất sóng. | Phi chức năng | "Máy cần soát được cả khi xe ở vùng mất sóng" (Mục 8, câu 3) | Tách từ cùng câu với REQ-68. Xem Q-31 |
| REQ-68 | Máy soát vé gửi lại kết quả soát vé cho hệ thống khi có sóng. | Chức năng | "gửi lại kết quả khi có sóng" (Mục 8, câu 3) | Tách từ cùng câu với REQ-67 |
| REQ-69 | Hệ thống gửi danh sách hành khách của chuyến về máy soát vé trước giờ xuất bến. | Chức năng | "hệ thống gửi danh sách hành khách của chuyến về máy soát vé" (Mục 8, câu 4) | Tách từ cùng câu với REQ-70. Xem Q-29, Q-30 |
| REQ-70 | Danh sách hành khách của chuyến được gửi về máy soát vé vào thời điểm 15 phút trước giờ xuất bến. | Quy tắc nghiệp vụ | "15 phút trước giờ xuất bến" (Mục 8, câu 4) | Tách từ cùng câu với REQ-69 |
| REQ-71 | Quản lý nhà xe có thể xem báo cáo doanh thu theo ngày. | Chức năng | "Quản lý xem báo cáo doanh thu theo ngày" (Mục 9) | "Quản lý" hiểu là Quản lý nhà xe theo ASM-09. Xem Q-32 |
| REQ-72 | Quản lý nhà xe có thể xem báo cáo doanh thu theo tuyến. | Chức năng | "báo cáo doanh thu theo ngày, theo tuyến" (Mục 9) | Tách từ cùng câu với REQ-71. Xem Q-09, Q-32 |
| REQ-73 | Quản lý nhà xe có thể xem báo cáo tỉ lệ lấp đầy chỗ của từng chuyến. | Chức năng | "tỉ lệ lấp đầy chỗ của từng chuyến" (Mục 9) | Tách từ cùng câu với REQ-71. Xem Q-09, Q-33 |
| REQ-74 | Hệ thống chịu được khoảng 2.000 người truy cập cùng lúc vào dịp Tết. | Phi chức năng | "Hệ thống phải chịu được khoảng 2.000 người truy cập cùng lúc vào dịp Tết." (Mục 10, câu 1) | Xem Q-34 |
| REQ-75 | Không được có hai vé cùng một chỗ trên một chuyến. | Quy tắc nghiệp vụ | "Không được để hai vé cùng một chỗ trên một chuyến." (Mục 10, câu 2) | Không có |
| REQ-76 | Hệ thống không lưu thông tin thẻ của hành khách. | Ràng buộc | "Hệ thống không lưu thông tin thẻ của hành khách." (Mục 10, câu 3) | Không có |
| REQ-77 | Máy soát vé cầm tay mà hệ thống giao tiếp là thiết bị Android có đầu quét mã vạch. | Ràng buộc | project-profile.md, HE_THONG_NGOAI | Chỉ có nguồn là hồ sơ nên đặt sau mọi REQ lấy từ tài liệu nguồn. Hồ sơ ghi thêm thiết bị do nhà xe tự trang bị (xem mục 2, Ngoài phạm vi) |

## 5. Vấn đề chất lượng của tài liệu nguồn

Mâu thuẫn giữa hai câu của nguồn: không phát hiện. Trùng lặp: không phát hiện.

| STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
|---|---|---|---|---|---|
| 1 | Thiếu | REQ-23, REQ-24 | Mục 4 đến Mục 9 nêu nhân viên bán vé, nhân viên điều hành, quản lý, phụ xe dùng hệ thống nhưng không nêu đăng nhập, ai cấp tài khoản | Hỏi Q-01; giả định ASM-02 | Q-01, ASM-02 |
| 2 | Thiếu | REQ-48, REQ-49, REQ-50, REQ-06 | "chọn tuyến, giờ xuất bến, xe và tài xế" (Mục 6, câu 1) cần danh mục tuyến, xe, tài xế nhưng nguồn không nói ai tạo và duy trì; "sơ đồ chỗ" (Mục 1, câu 2) không nói ai định nghĩa | Hỏi Q-02; giả định ASM-06 | Q-02, ASM-06 |
| 3 | Thiếu | REQ-33, REQ-34, REQ-35, REQ-36, REQ-41 | "Hành khách được đổi hoặc trả vé." (Mục 5, câu 1) không nêu kênh; "vé mua tại quầy được hoàn tiền mặt tại quầy" (Mục 5, câu 3) là câu bị động không nêu chủ thể | Hỏi Q-03; giả định ASM-04 | Q-03, ASM-04 |
| 4 | Thiếu | REQ-10, REQ-11, REQ-12 | "đăng ký tài khoản bằng số điện thoại để xem lại lịch sử vé" (Mục 2, câu 2) không nêu cách đăng nhập | Hỏi Q-04; giả định ASM-01 | Q-04, ASM-01 |
| 5 | Thiếu | REQ-22, REQ-28, REQ-29 | "Nhân viên bán vé ... bán vé cho khách mua trực tiếp" (Mục 4, câu 1) và "nhận đặt chỗ qua điện thoại" (Mục 4, câu 2) không nói ai chọn chuyến và chỗ | Hỏi Q-05; giả định ASM-03 | Q-05, ASM-03 |
| 6 | Thiếu | REQ-47, REQ-51, REQ-63 | "Phụ xe mỗi chuyến" (Mục 8, câu 1) nhưng lịch chạy chỉ gồm "tuyến, giờ xuất bến, xe và tài xế" (Mục 6, câu 1) | Hỏi Q-06; giả định ASM-07 | Q-06, ASM-07 |
| 7 | Thiếu | REQ-57, REQ-58, REQ-59 | "hoàn 100% giá vé" (Mục 6, câu 4) không nêu kênh hoàn; kênh chỉ nêu cho nhánh trả vé (Mục 5, câu 3) | Hỏi Q-07; giả định ASM-08 | Q-07, ASM-08 |
| 8 | Thiếu | REQ-44, REQ-45 | "trả thêm phần chênh lệch nếu vé mới đắt hơn" (Mục 5, câu 4) chỉ nêu nhánh vé mới đắt hơn | Hỏi Q-08; giả định ASM-05 | Q-08, ASM-05 |
| 9 | Mơ hồ | REQ-61, REQ-71, REQ-72, REQ-73 | "quản lý nhà xe đặt" (Mục 7, câu 1); "quản lý có thể đặt" (Mục 7, câu 2); "Quản lý xem báo cáo" (Mục 9): không rõ cùng một vai trò | Hỏi Q-09; giả định ASM-09 | Q-09, ASM-09 |
| 10 | Mơ hồ | REQ-05 | "tìm chuyến theo điểm đi, điểm đến và ngày đi" (Mục 1, câu 2): điểm đi, điểm đến là bến xe hay tỉnh, thành | Hỏi Q-10 | Q-10 |
| 11 | Mơ hồ | REQ-09, REQ-20 | "nhập họ tên và số điện thoại của người đi" (Mục 2, câu 1) với "chọn tối đa 5 chỗ" (Mục 1, câu 2): một người đi hay mỗi chỗ một người đi | Hỏi Q-11 | Q-11 |
| 12 | Thiếu | REQ-08, REQ-29 | "tối đa 5 chỗ trong một lần đặt" (Mục 1, câu 2) chỉ nêu ở luồng hành khách đặt qua website | Hỏi Q-12 | Q-12 |
| 13 | Thiếu | REQ-04, REQ-22 | Nguồn không nêu thời điểm ngừng bán vé trước giờ xuất bến | Hỏi Q-13 | Q-13 |
| 14 | Thiếu | REQ-28, REQ-31 | "nhận đặt chỗ qua điện thoại" (Mục 4, câu 2) và "chậm nhất 60 phút trước giờ xuất bến": không nêu trường hợp đặt khi còn dưới 60 phút | Hỏi Q-14 | Q-14 |
| 15 | Thiếu | REQ-52, REQ-53, REQ-54 | "thời gian chạy chồng nhau" (Mục 6, câu 2): nguồn không nêu thời gian chạy của chuyến lấy từ đâu | Hỏi Q-15 | Q-15 |
| 16 | Mơ hồ | REQ-54 | "không được lái quá 10 giờ trong một ngày" (Mục 6, câu 3): không rõ ngày tính thế nào, chuyến qua nửa đêm | Hỏi Q-16 | Q-16 |
| 17 | Thiếu | REQ-15 | "thanh toán thành công" (Mục 3, câu 2, câu 3): không nêu thanh toán thất bại trong 10 phút thì hành khách thử lại được không | Hỏi Q-17 | Q-17 |
| 18 | Mơ hồ | REQ-13, REQ-14 | "giữ trong 10 phút" (Mục 3, câu 1): không nêu mốc bắt đầu tính | Hỏi Q-18 | Q-18 |
| 19 | Thiếu | REQ-15, REQ-17 | "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại" (Mục 3, câu 2): không nêu trường hợp cổng báo thành công sau khi hết 10 phút | Hỏi Q-19 | Q-19 |
| 20 | Thiếu | REQ-16, REQ-37, REQ-38 | "chưa có tài liệu API" (project-profile.md, HE_THONG_NGOAI); hoàn 90% và 50% đòi hỏi hoàn một phần | Hỏi Q-20 | Q-20 |
| 21 | Mơ hồ | REQ-43 | "chậm nhất 4 giờ trước giờ xuất bến" (Mục 5, câu 4): giờ xuất bến của chuyến cũ hay chuyến mới | Hỏi Q-21 | Q-21 |
| 22 | Thiếu | REQ-44 | "trả thêm phần chênh lệch" (Mục 5, câu 4): không nêu kênh thanh toán phần chênh lệch | Hỏi Q-22 | Q-22 |
| 23 | Mơ hồ | REQ-61 | "Ngày lễ, Tết, quản lý có thể đặt mức tăng giá ... cho một khoảng ngày" (Mục 7, câu 2): chỉ khoảng ngày lễ, Tết hay bất kỳ khoảng ngày | Hỏi Q-23 | Q-23 |
| 24 | Thiếu | REQ-61 | Nguồn không nêu mức tăng áp dụng theo ngày xuất bến hay ngày mua vé | Hỏi Q-24 | Q-24 |
| 25 | Mơ hồ (từ "mọi") | REQ-56 | "gửi SMS cho mọi hành khách đã có vé" (Mục 6, câu 4): cần xác nhận ngoại lệ, ví dụ vé đặt qua điện thoại chưa thanh toán | Hỏi Q-25 | Q-25 |
| 26 | Thiếu | REQ-11 | "xem lại lịch sử vé" (Mục 2, câu 2): không nêu gồm vé nào, vé đặt khi chưa đăng nhập có hiện không | Hỏi Q-26 | Q-26 |
| 27 | Thiếu | REQ-26, REQ-63 | "quét mã vé" (Mục 8, câu 1); vé trực tuyến chỉ nhận "mã vé" qua SMS (Mục 3, câu 3); vé giấy có "mã vạch" (Mục 4, câu 1): không nêu cách xuất trình mã vé trực tuyến | Hỏi Q-27 | Q-27 |
| 28 | Mơ hồ | REQ-66 | "Máy báo hợp lệ hay không hợp lệ (sai chuyến, vé đã huỷ, vé đã soát)" (Mục 8, câu 2): danh sách trong ngoặc là đầy đủ hay ví dụ | Hỏi Q-28 | Q-28 |
| 29 | Thiếu | REQ-67, REQ-69 | "soát được cả khi xe ở vùng mất sóng" (Mục 8, câu 3) với "15 phút trước giờ xuất bến, hệ thống gửi danh sách" (Mục 8, câu 4): vé bán, đổi, huỷ sau thời điểm gửi danh sách | Hỏi Q-29 | Q-29 |
| 30 | Thiếu | REQ-69 | "danh sách hành khách của chuyến" (Mục 8, câu 4): không nêu danh sách gồm thông tin nào | Hỏi Q-30 | Q-30 |
| 31 | Không kiểm chứng được | REQ-67 | "soát được cả khi xe ở vùng mất sóng" (Mục 8, câu 3): không nêu thời gian mất sóng tối đa | Hỏi Q-31 | Q-31 |
| 32 | Mơ hồ | REQ-71, REQ-72 | "báo cáo doanh thu theo ngày, theo tuyến" (Mục 9): doanh thu có trừ tiền hoàn không | Hỏi Q-32 | Q-32 |
| 33 | Mơ hồ | REQ-73 | "tỉ lệ lấp đầy chỗ của từng chuyến" (Mục 9): chỗ đang giữ chưa thanh toán có tính là đã lấp đầy không | Hỏi Q-33 | Q-33 |
| 34 | Không kiểm chứng được | REQ-74 | "chịu được khoảng 2.000 người truy cập cùng lúc vào dịp Tết" (Mục 10, câu 1): không nêu thời gian phản hồi chấp nhận được, không nêu khoảng thời gian "dịp Tết" | Hỏi Q-34 | Q-34 |
| 35 | Thiếu | REQ-20 | "gửi qua SMS tới số điện thoại người đi" (Mục 3, câu 3): không nêu khi gửi SMS thất bại | Hỏi Q-35 | Q-35 |
| 36 | Mơ hồ | REQ-55 | "(xe hỏng, thời tiết)" (Mục 6, câu 4): danh sách lý do mở hay đóng | Hỏi Q-36 | Q-36 |
| 37 | Thiếu | REQ-33, REQ-34 | "Hành khách được đổi hoặc trả vé." (Mục 5, câu 1) và "đặt vé không bắt buộc có tài khoản" (Mục 2, câu 2): hành khách không có tài khoản xác thực quyền trả, đổi vé bằng gì | Hỏi Q-37 | Q-37 |

## 6. Ma trận phủ nguồn

| Vị trí trong nguồn | Tóm tắt nội dung | Kết luận |
|---|---|---|
| Đoạn mở đầu, câu 1 | 12 tuyến, 3 bến xe, khoảng 80 chuyến mỗi ngày | REQ-01, REQ-02 |
| Đoạn mở đầu, câu 2 | Đội xe khoảng 50 xe giường nằm 40 chỗ, 20 xe ghế ngồi 29 chỗ | REQ-03 |
| Đoạn mở đầu, câu 3 | Hiện bán vé qua điện thoại, quầy, ghi sổ tay, thường trùng chỗ | Bối cảnh (mục 1) |
| Đoạn mở đầu, câu 4 | Nhà xe cần phần mềm bán vé và quản lý chuyến | Bối cảnh (mục 1) |
| Mục 1, câu 1 | Hành khách đặt vé qua website | REQ-04 |
| Mục 1, câu 2 | Tìm chuyến, xem sơ đồ chỗ, chọn tối đa 5 chỗ | REQ-05, REQ-06, REQ-07, REQ-08 |
| Mục 1, câu 3 | Tìm chuyến và xem chỗ trống không cần tài khoản | REQ-05, REQ-06 |
| Mục 2, câu 1 | Nhập họ tên và số điện thoại của người đi | REQ-09 |
| Mục 2, câu 2 | Đăng ký tài khoản bằng số điện thoại, xem lịch sử vé, đặt vé không bắt buộc tài khoản | REQ-10, REQ-11, REQ-04; REQ-12 (ASM-01) |
| Mục 3, câu 1 | Giữ chỗ 10 phút, thanh toán qua cổng thanh toán của đối tác | REQ-13, REQ-14, REQ-15, REQ-16 |
| Mục 3, câu 2 | Hết 10 phút chưa thanh toán thì trả chỗ | REQ-17 |
| Mục 3, câu 3 | Phát hành vé, mỗi chỗ một mã vé, gửi SMS | REQ-18, REQ-19, REQ-20, REQ-21 |
| Mục 4, câu 1 | Bán vé tại quầy, thu tiền mặt, in vé giấy có mã vạch | REQ-22, REQ-25, REQ-26, REQ-27; REQ-23, REQ-24 (ASM-02) |
| Mục 4, câu 2 | Nhận đặt chỗ qua điện thoại, thanh toán tại quầy chậm nhất 60 phút, tự huỷ | REQ-28, REQ-30, REQ-31, REQ-32; REQ-29 (ASM-03) |
| Mục 5, câu 1 | Đổi hoặc trả vé | REQ-33, REQ-34; REQ-35, REQ-36 (ASM-04) |
| Mục 5, câu 2 | Mức hoàn khi trả vé theo ba khoảng thời gian | REQ-37, REQ-38, REQ-39 |
| Mục 5, câu 3 | Hoàn vé trực tuyến qua cổng thanh toán, vé quầy hoàn tiền mặt tại quầy | REQ-40, REQ-41, REQ-16 |
| Mục 5, câu 4 | Đổi một lần, cùng tuyến, chậm nhất 4 giờ, trả thêm chênh lệch | REQ-34, REQ-42, REQ-43, REQ-44; REQ-45 (ASM-05) |
| Mục 6, câu 1 | Lập lịch chạy theo tuần, chọn tuyến, giờ xuất bến, xe, tài xế | REQ-46, REQ-47; REQ-48, REQ-49, REQ-50 (ASM-06); REQ-51 (ASM-07) |
| Mục 6, câu 2 | Xe, tài xế không xếp vào hai chuyến chồng nhau | REQ-52, REQ-53 |
| Mục 6, câu 3 | Tài xế không lái quá 10 giờ một ngày | REQ-54 |
| Mục 6, câu 4 | Huỷ chuyến, gửi SMS, hoàn 100% giá vé | REQ-55, REQ-56, REQ-57, REQ-58; REQ-59 (ASM-08) |
| Mục 7, câu 1 | Quản lý nhà xe đặt giá vé theo tuyến và loại xe | REQ-60 |
| Mục 7, câu 2 | Mức tăng giá theo phần trăm cho khoảng ngày lễ, Tết, tối đa 30% | REQ-61, REQ-62 |
| Mục 8, câu 1 | Phụ xe quét mã vé bằng máy soát vé cầm tay | REQ-63, REQ-64 |
| Mục 8, câu 2 | Máy báo hợp lệ hoặc không hợp lệ | REQ-65, REQ-66 |
| Mục 8, câu 3 | Soát khi mất sóng, gửi lại kết quả khi có sóng | REQ-67, REQ-68 |
| Mục 8, câu 4 | 15 phút trước giờ xuất bến gửi danh sách hành khách về máy | REQ-69, REQ-70 |
| Mục 9 | Báo cáo doanh thu theo ngày, theo tuyến, tỉ lệ lấp đầy từng chuyến | REQ-71, REQ-72, REQ-73 |
| Mục 10, câu 1 | Chịu khoảng 2.000 người truy cập cùng lúc dịp Tết | REQ-74 |
| Mục 10, câu 2 | Không hai vé cùng một chỗ trên một chuyến | REQ-75 |
| Mục 10, câu 3 | Không lưu thông tin thẻ | REQ-76; Ngoài phạm vi (xử lý thông tin thẻ) |
| project-profile.md, HE_THONG_NGOAI: Cổng thanh toán trực tuyến của đối tác | API thanh toán và hoàn tiền, chưa có tài liệu API | REQ-16 |
| project-profile.md, HE_THONG_NGOAI: Cổng SMS của nhà mạng | API REST | REQ-21 |
| project-profile.md, HE_THONG_NGOAI: Máy soát vé cầm tay Android | Có đầu quét mã vạch, do nhà xe tự trang bị | REQ-64, REQ-77; Ngoài phạm vi (cung cấp phần cứng) |
| project-profile.md, HE_THONG_NGOAI: Máy in vé nhiệt tại quầy | Máy in tại quầy | REQ-27 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-01 | Nhân viên nhà xe (bán vé, điều hành, quản lý, phụ xe) có phải đăng nhập bằng tài khoản riêng theo vai trò không, và ai cấp tài khoản? (Có, quản lý nhà xe cấp / Có, người quản trị hệ thống riêng cấp / Không đăng nhập) | REQ-23, REQ-24; tác nhân và phân quyền ở P01; mọi UC của nhân viên | Mục 4 đến Mục 9: nhân viên dùng hệ thống nhưng không nêu đăng nhập |
| Q-02 | Ai quản lý danh mục tuyến, bến xe, xe (gồm loại xe và sơ đồ chỗ) và tài xế? (Nhân viên điều hành / Quản lý nhà xe / Người quản trị hệ thống riêng) | REQ-48, REQ-49, REQ-50, REQ-06, REQ-47; danh sách UC ở P02 | Mục 6, câu 1; Mục 1, câu 2 |
| Q-03 | Việc trả vé, đổi vé thực hiện qua kênh nào? (Hành khách tự thực hiện trên website với vé mua trực tuyến, nhân viên bán vé thực hiện với vé mua tại quầy / Mọi vé đều qua nhân viên bán vé tại quầy) | REQ-33, REQ-34, REQ-35, REQ-36, REQ-41; tác nhân và UC trả, đổi vé | Mục 5, câu 1 và câu 3 |
| Q-04 | Hành khách đã đăng ký tài khoản bằng số điện thoại thì đăng nhập bằng cách nào? (Mật khẩu / Mã xác thực gửi qua SMS) | REQ-10, REQ-11, REQ-12; UC đăng ký, đăng nhập | Mục 2, câu 2 |
| Q-05 | Khi bán vé tại quầy hoặc nhận đặt chỗ qua điện thoại, nhân viên bán vé có chọn chuyến và chỗ cho khách trên sơ đồ chỗ không? (Có / Không, hệ thống tự gán chỗ) | REQ-22, REQ-28, REQ-29; luồng chính của UC bán vé tại quầy | Mục 4, câu 1 và câu 2 |
| Q-06 | Phụ xe của mỗi chuyến do ai xác định? (Nhân viên điều hành chọn khi lập lịch / Phụ xe tự chọn chuyến trên máy soát vé) | REQ-47, REQ-51, REQ-63; UC lập lịch chạy, soát vé | Mục 6, câu 1; Mục 8, câu 1 |
| Q-07 | Vé của chuyến bị huỷ được hoàn tiền qua kênh nào? (Cùng kênh mua vé: vé trực tuyến hoàn qua cổng thanh toán, vé mua tại quầy hoàn tiền mặt tại quầy / Mọi vé hoàn qua cổng thanh toán) | REQ-57, REQ-58, REQ-59; UC huỷ chuyến | Mục 6, câu 4 |
| Q-08 | Khi đổi sang vé mới rẻ hơn vé cũ, hành khách có được hoàn phần chênh lệch không? (Hoàn / Không hoàn) | REQ-44, REQ-45; UC đổi vé | Mục 5, câu 4 |
| Q-09 | Chữ "quản lý" ở Mục 7 câu 2 và Mục 9 có cùng là vai trò quản lý nhà xe ở Mục 7 câu 1 không? (Cùng vai trò / Khác vai trò) | REQ-61, REQ-71, REQ-72, REQ-73; tác nhân ở P01 | Mục 7, câu 1 và câu 2; Mục 9 |
| Q-10 | Điểm đi và điểm đến khi tìm chuyến là bến xe hay tỉnh, thành phố? (Bến xe / Tỉnh, thành phố) | REQ-05, REQ-01; dữ liệu tuyến | Mục 1, câu 2 |
| Q-11 | Mỗi lần đặt nhiều chỗ thì nhập một họ tên, số điện thoại chung hay riêng cho từng chỗ? (Một người đi chung cho cả lần đặt / Riêng cho từng chỗ) | REQ-09, REQ-20; luồng đặt vé và gửi SMS | Mục 2, câu 1; Mục 3, câu 3 |
| Q-12 | Giới hạn tối đa 5 chỗ trong một lần đặt có áp dụng khi nhân viên bán vé bán tại quầy hoặc nhận đặt chỗ qua điện thoại không? (Áp dụng / Không giới hạn) | REQ-08, REQ-29; luồng bán vé tại quầy | Mục 1, câu 2 |
| Q-13 | Vé ngừng được bán (website và quầy) vào thời điểm nào trước giờ xuất bến? (Đến giờ xuất bến / Trước giờ xuất bến một số phút do nhà xe quy định) | REQ-04, REQ-22; điều kiện đầu của UC đặt vé, bán vé | Không có câu nào trong nguồn nêu thời điểm ngừng bán |
| Q-14 | Khi nhận đặt chỗ qua điện thoại lúc còn dưới 60 phút trước giờ xuất bến thì xử lý thế nào? (Không nhận đặt qua điện thoại / Vẫn nhận, phải thanh toán ngay tại quầy) | REQ-28, REQ-31, REQ-32; luồng ngoại lệ của UC đặt chỗ qua điện thoại | Mục 4, câu 2 |
| Q-15 | Thời gian chạy của một chuyến (dùng để kiểm tra chồng lịch và giới hạn lái xe) lấy từ đâu? (Thời lượng cố định theo tuyến / Nhân viên điều hành nhập giờ đến cho từng chuyến) | REQ-47, REQ-52, REQ-53, REQ-54; kiểm tra ràng buộc khi lập lịch | Mục 6, câu 2 và câu 3 |
| Q-16 | Giới hạn 10 giờ lái tính theo ngày dương lịch hay theo mọi khoảng 24 giờ liên tục? (Ngày dương lịch / Mọi khoảng 24 giờ liên tục) | REQ-54 | Mục 6, câu 3 |
| Q-17 | Khi thanh toán không thành công trong thời gian giữ chỗ, hành khách có được thanh toán lại với các chỗ đang giữ không? (Có, đến hết thời gian giữ chỗ / Không, phải chọn lại chỗ) | REQ-15, REQ-17; luồng ngoại lệ của UC thanh toán | Mục 3, câu 2 |
| Q-18 | Thời gian giữ chỗ 10 phút bắt đầu tính từ lúc nào? (Lúc hành khách chọn chỗ / Lúc hành khách bắt đầu thanh toán) | REQ-13, REQ-14, REQ-17 | Mục 3, câu 1 |
| Q-19 | Nếu cổng thanh toán báo thành công sau khi đã hết 10 phút và chỗ đã trả lại, xử lý thế nào? (Hoàn tiền cho hành khách / Phát hành vé nếu chỗ còn trống, ngược lại hoàn tiền) | REQ-15, REQ-17, REQ-40; luồng ngoại lệ của UC thanh toán | Mục 3, câu 2 |
| Q-20 | API hoàn tiền của cổng thanh toán đối tác có hỗ trợ hoàn một phần số tiền không? (Có / Không) | REQ-16, REQ-37, REQ-38, REQ-40; P06, P09 | project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" |
| Q-21 | Hạn đổi vé chậm nhất 4 giờ trước giờ xuất bến tính theo chuyến cũ hay chuyến mới? (Chuyến cũ / Chuyến mới / Cả hai) | REQ-43; điều kiện của UC đổi vé | Mục 5, câu 4 |
| Q-22 | Phần chênh lệch khi đổi sang vé đắt hơn được thanh toán qua kênh nào? (Cùng kênh mua vé cũ / Hành khách chọn lại) | REQ-44; luồng chính của UC đổi vé | Mục 5, câu 4 |
| Q-23 | Quản lý nhà xe có được đặt mức tăng giá cho khoảng ngày không phải ngày lễ, Tết không? (Chỉ ngày lễ, Tết / Bất kỳ khoảng ngày) | REQ-61 | Mục 7, câu 2 |
| Q-24 | Mức tăng giá áp dụng theo ngày xuất bến hay ngày mua vé? (Ngày xuất bến / Ngày mua vé) | REQ-61, REQ-62; BR tính giá | Mục 7, câu 2 |
| Q-25 | Vé đặt qua điện thoại chưa thanh toán của chuyến bị huỷ có nhận SMS thông báo huỷ chuyến không? (Có / Không) | REQ-56, REQ-57 | Mục 6, câu 4 |
| Q-26 | Lịch sử vé của hành khách gồm những vé nào? (Chỉ vé đặt khi đã đăng nhập / Cả vé đặt không đăng nhập có cùng số điện thoại) | REQ-11 | Mục 2, câu 2 |
| Q-27 | Hành khách có vé trực tuyến xuất trình mã vé để soát bằng cách nào? (Mã trong SMS quét được bằng máy soát vé / Phụ xe nhập mã vé bằng tay) | REQ-26, REQ-63; UC soát vé | Mục 3, câu 3; Mục 8, câu 1 |
| Q-28 | Ba trường hợp vé không hợp lệ (sai chuyến, vé đã huỷ, vé đã soát) là đầy đủ không? (Đầy đủ / Còn trường hợp khác) | REQ-66 | Mục 8, câu 2 |
| Q-29 | Vé bán, đổi, huỷ sau thời điểm gửi danh sách (15 phút trước giờ xuất bến) cập nhật vào máy soát vé thế nào? (Gửi bổ sung khi máy có sóng / Không cập nhật, máy dùng danh sách đã gửi) | REQ-67, REQ-68, REQ-69, REQ-70; luồng ngoại lệ của UC soát vé | Mục 8, câu 3 và câu 4 |
| Q-30 | Danh sách hành khách gửi về máy soát vé gồm thông tin nào? (Mã vé và chỗ / Mã vé, chỗ, họ tên, số điện thoại) | REQ-69; P05, P13 | Mục 8, câu 4 |
| Q-31 | Máy soát vé phải hoạt động độc lập khi mất sóng liên tục tối đa bao lâu? (Trong phạm vi một chuyến / Số giờ cụ thể do nhà xe quy định) | REQ-67; NFR ở P06 | Mục 8, câu 3 |
| Q-32 | Doanh thu trong báo cáo có trừ tiền hoàn trả vé và huỷ chuyến không? (Trừ / Không trừ) | REQ-71, REQ-72 | Mục 9 |
| Q-33 | Tỉ lệ lấp đầy chỗ có tính chỗ đang giữ chưa thanh toán không? (Chỉ chỗ đã có vé / Gồm cả chỗ đang giữ) | REQ-73 | Mục 9 |
| Q-34 | Khi có khoảng 2.000 người truy cập cùng lúc, thời gian phản hồi tối đa chấp nhận được là bao nhiêu giây, và "dịp Tết" gồm những ngày nào? (Nhập số giây và khoảng ngày) | REQ-74; NFR ở P06 | Mục 10, câu 1 |
| Q-35 | Khi gửi SMS mã vé không thành công, hệ thống xử lý thế nào? (Thử gửi lại / Hiển thị mã vé trên website / Chỉ ghi nhận lỗi) | REQ-20; luồng ngoại lệ của UC phát hành vé | Mục 3, câu 3 |
| Q-36 | Lý do huỷ chuyến chỉ gồm xe hỏng và thời tiết hay còn lý do khác? (Chỉ hai lý do / Còn lý do khác) | REQ-55 | Mục 6, câu 4 |
| Q-37 | Hành khách không có tài khoản xác thực quyền trả vé, đổi vé bằng gì? (Mã vé và số điện thoại người đi / Chỉ mã vé) | REQ-33, REQ-34; UC trả vé, đổi vé | Mục 5, câu 1; Mục 2, câu 2 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-01 | Hành khách đã đăng ký tài khoản đăng nhập bằng mã xác thực gửi qua SMS tới số điện thoại đã đăng ký. | Chờ Q-04. Nguồn cho phép đăng ký bằng số điện thoại và xem lại lịch sử vé nhưng không nêu cách đăng nhập; chọn mã SMS vì tài khoản định danh bằng số điện thoại và hệ thống đã có kênh SMS | REQ-12, REQ-11 |
| ASM-02 | Nhân viên nhà xe đăng nhập bằng tài khoản riêng theo vai trò; quản lý nhà xe quản lý các tài khoản đó. | Chờ Q-01. Nguồn nêu bốn vai trò nhân viên dùng hệ thống nhưng không nêu đăng nhập, cấp tài khoản | REQ-23, REQ-24 |
| ASM-03 | Nhân viên bán vé chọn chuyến và chỗ còn trống trên sơ đồ chỗ cho khách khi bán vé tại quầy và khi nhận đặt chỗ qua điện thoại. | Chờ Q-05. Bán vé và giữ chỗ cần xác định chuyến và chỗ mà nguồn không nói ai chọn | REQ-29, REQ-22, REQ-28 |
| ASM-04 | Nhân viên bán vé thực hiện trả vé và đổi vé tại quầy cho hành khách có vé mua tại quầy; hành khách tự trả vé, đổi vé mua trực tuyến trên website. | Chờ Q-03. Nguồn nêu hoàn tiền mặt tại quầy cho vé mua tại quầy nên phải có người thực hiện trả vé tại quầy | REQ-35, REQ-36, REQ-33, REQ-34, REQ-41 |
| ASM-05 | Khi vé mới rẻ hơn vé cũ, hành khách không được hoàn phần chênh lệch. | Chờ Q-08. Nguồn chỉ nêu nhánh vé mới đắt hơn; chọn phương án không thêm khoản hoàn mà nguồn không nêu | REQ-45 |
| ASM-06 | Nhân viên điều hành quản lý danh mục tuyến, bến xe, xe (loại xe, số chỗ, sơ đồ chỗ) và tài xế. | Chờ Q-02. Lập lịch chạy phải chọn tuyến, xe, tài xế từ danh mục mà nguồn không nói ai tạo | REQ-48, REQ-49, REQ-50, REQ-01, REQ-03, REQ-06 |
| ASM-07 | Mỗi chuyến có một phụ xe do nhân viên điều hành chọn khi lập lịch chạy. | Chờ Q-06. Nguồn nêu "Phụ xe mỗi chuyến" nhưng lịch chạy không có phụ xe | REQ-51, REQ-63 |
| ASM-08 | Vé của chuyến bị huỷ được hoàn tiền qua cùng kênh với kênh mua vé. | Chờ Q-07. Nguồn chỉ nêu kênh hoàn cho nhánh trả vé | REQ-59, REQ-57 |
| ASM-09 | Chữ "quản lý" ở Mục 7 câu 2 và Mục 9 chỉ cùng vai trò Quản lý nhà xe ở Mục 7 câu 1. | Chờ Q-09. Ba chỗ dùng ba cách gọi khác nhau cho vai trò đặt giá và xem báo cáo | REQ-61, REQ-71, REQ-72, REQ-73 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Không có mục Target nào ở trạng thái Không đạt.
- Lựa chọn khi hai quy tắc xung đột (Conventions C9): ngưỡng thời gian của hệ thống (REQ-14 giữ chỗ 10 phút, REQ-70 gửi danh sách 15 phút) được tách thành Quy tắc nghiệp vụ theo F2 quy tắc 5, dù F3 câu 4 ("vẫn đúng kể cả khi làm bằng tay") không chắc áp dụng cho các ngưỡng này.
- Lựa chọn khi hai quy tắc xung đột: REQ-03 giữ một REQ Dữ liệu cho đội xe hai loại theo F2 quy tắc 6, không tách theo loại xe.
- Lựa chọn khi hai quy tắc xung đột: "qua website" ở REQ-04 giữ trong REQ Chức năng như kênh, không tách thành Ràng buộc, vì NEN_TANG trong hồ sơ là "Chưa chốt" và F3 câu 2 chỉ coi câu bắt buộc nền tảng là Ràng buộc.
- Số REQ là 77, vượt khoảng 60-70 ở F2 vì 21 REQ là Quy tắc nghiệp vụ tách theo ngưỡng và quy tắc, 12 REQ dựa trên giả định (CO_NHAN) và 5 REQ gắn với hệ thống, thiết bị ngoài.
- REQ-23 và REQ-29 mỗi REQ nêu một năng lực cho nhiều vai trò hoặc nhiều ngữ cảnh (đăng nhập cho bốn vai trò; chọn chuyến và chỗ cho hai luồng bán). Giữ một REQ vì nguồn không phân biệt quy tắc riêng.
