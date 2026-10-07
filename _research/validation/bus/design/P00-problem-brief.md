# P00 - Chuẩn hoá yêu cầu - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P00 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có) |
| Phạm vi | Toàn hệ thống |

Quy ước vị trí trích dẫn: tài liệu nguồn duy nhất là yeu-cau-xe-khach.md, nên trích nguồn không ghi tên tài liệu. "Đoạn mở đầu" là đoạn văn ngay dưới tiêu đề; "Mục n" là mục đánh số n; "câu k" là câu thứ k trong đoạn hoặc mục đó. Trích từ hồ sơ dự án ghi "project-profile.md, <tên trường>".

## 1. Bối cảnh và mục tiêu nghiệp vụ

Nhà xe SaoViet khai thác 12 tuyến xe khách liên tỉnh xuất phát từ 3 bến xe, khoảng 80 chuyến mỗi ngày, với đội xe giường nằm và xe ghế ngồi. Hiện vé được bán qua điện thoại và tại quầy ở bến, ghi bằng sổ tay, và thường xuyên bị trùng chỗ. Nhà xe cần một phần mềm bán vé và quản lý chuyến. Hệ thống phục vụ hành khách đặt vé trực tuyến, nhân viên bán vé tại quầy, nhân viên điều hành lập lịch chạy, phụ xe soát vé và quản lý nhà xe đặt giá, xem báo cáo.

Mục tiêu nghiệp vụ:

- Bán vé và quản lý chuyến bằng phần mềm thay cho bán qua điện thoại, quầy và ghi sổ tay (nguồn: Đoạn mở đầu, câu 3 và câu 4).
- Chấm dứt tình trạng trùng chỗ (nguồn: Đoạn mở đầu, câu 3 "thường xuyên bị trùng chỗ"; Mục 10, câu 2 "Không được để hai vé cùng một chỗ trên một chuyến").
- Cho phép hành khách đặt và thanh toán vé xe khách liên tỉnh trực tuyến (nguồn: Mục 1, câu 1; Mục 3, câu 1; project-profile.md, MO_TA_MOT_CAU).

## 2. Phạm vi

Trong phạm vi:

- Tìm chuyến, xem sơ đồ chỗ và đặt vé qua website, có hoặc không có tài khoản: REQ-03 đến REQ-09.
- Tài khoản hành khách và lịch sử vé: REQ-10, REQ-11.
- Giữ chỗ, thanh toán trực tuyến, phát hành vé và gửi vé qua SMS: REQ-12 đến REQ-20.
- Bán vé tại quầy, in vé giấy, nhận đặt chỗ qua điện thoại và tự động huỷ vé đặt qua điện thoại quá hạn thanh toán: REQ-21 đến REQ-28.
- Đổi vé, trả vé và hoàn tiền: REQ-29 đến REQ-40.
- Lập lịch chạy, huỷ chuyến và xử lý hành khách của chuyến bị huỷ: REQ-41 đến REQ-50.
- Đặt giá vé và mức tăng giá ngày lễ, Tết: REQ-51 đến REQ-54.
- Soát vé bằng máy soát vé cầm tay, kể cả khi mất sóng (phần mềm soát vé thuộc phạm vi theo ASM-01): REQ-55 đến REQ-62.
- Báo cáo doanh thu và tỉ lệ lấp đầy: REQ-63 đến REQ-65.
- Quy mô, chất lượng và ràng buộc chung: REQ-01, REQ-02, REQ-04, REQ-66, REQ-67, REQ-68.

Ngoài phạm vi:

- Xử lý giao dịch thanh toán và hoàn tiền trực tuyến: do cổng thanh toán trực tuyến của đối tác đảm nhiệm, hệ thống chỉ trao đổi dữ liệu (nguồn: Mục 3, câu 1 "cổng thanh toán trực tuyến của đối tác"; project-profile.md, HE_THONG_NGOAI). Xem REQ-15, REQ-35.
- Lưu thông tin thẻ của hành khách (nguồn: Mục 10, câu 3 "Hệ thống không lưu thông tin thẻ của hành khách"). Xem REQ-68.
- Chuyển tin nhắn SMS tới thuê bao: do cổng SMS của nhà mạng đảm nhiệm, hệ thống chỉ gửi nội dung tin nhắn qua API (nguồn: project-profile.md, HE_THONG_NGOAI "Cổng SMS của nhà mạng (API REST)"). Xem REQ-20.
- Trang bị phần cứng máy soát vé cầm tay (nguồn: project-profile.md, HE_THONG_NGOAI "do nhà xe tự trang bị"). Xem REQ-56, ASM-01.
- Máy in vé nhiệt tại quầy là thiết bị ngoài, hệ thống chỉ gửi dữ liệu in (nguồn: project-profile.md, HE_THONG_NGOAI "Máy in vé nhiệt tại quầy"). Xem REQ-24.

Chưa xếp vào danh sách nào vì nguồn không nói: chức năng cập nhật danh mục tuyến, xe, tài xế mà Mục 6 câu 1 cần dùng khi lập lịch; chờ trả lời Q-03.

## 3. Các bên liên quan và người dùng

| SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống (Có / Không / Chưa rõ) | REQ |
|---|---|---|---|---|---|
| SH-01 | Nhà xe SaoViet | Chủ sở hữu, người đặt hàng | Bán vé và quản lý chuyến bằng phần mềm, chấm dứt trùng chỗ | Không | REQ-01, REQ-02, REQ-67 |
| SH-02 | Hành khách | Người dùng trực tiếp | Tìm chuyến, đặt và thanh toán vé trực tuyến, đổi, trả vé, xem lịch sử vé | Có | REQ-03, REQ-05 đến REQ-14, REQ-29, REQ-30, REQ-40 |
| SH-03 | Người đi | Người hưởng lợi gián tiếp | Nhận vé qua SMS, được soát vé khi lên xe, nhận SMS khi chuyến bị huỷ | Không | REQ-09, REQ-19, REQ-48, REQ-55 |
| SH-04 | Cổng thanh toán trực tuyến của đối tác | Hệ thống hoặc thiết bị ngoài | Nhận yêu cầu thanh toán và hoàn tiền vé mua trực tuyến | Có | REQ-14, REQ-15, REQ-34, REQ-35 |
| SH-05 | Cổng SMS của nhà mạng | Hệ thống hoặc thiết bị ngoài | Nhận nội dung tin nhắn để gửi vé và thông báo cho hành khách | Có | REQ-19, REQ-20, REQ-48 |
| SH-06 | Nhân viên bán vé | Người dùng trực tiếp | Bán vé tại quầy, nhận đặt chỗ qua điện thoại, thu tiền, in vé | Có | REQ-21 đến REQ-28, REQ-36 |
| SH-07 | Khách mua vé trực tiếp tại quầy | Người hưởng lợi gián tiếp | Mua vé bằng tiền mặt, nhận vé giấy có mã vạch | Không | REQ-21, REQ-22, REQ-23, REQ-36 |
| SH-08 | Máy in vé nhiệt tại quầy | Hệ thống hoặc thiết bị ngoài | Nhận dữ liệu vé để in vé giấy có mã vạch | Có | REQ-23, REQ-24 |
| SH-09 | Khách đặt chỗ qua điện thoại | Người hưởng lợi gián tiếp | Được giữ chỗ qua điện thoại và thanh toán tại quầy trước hạn | Không | REQ-25 đến REQ-28 |
| SH-10 | Nhân viên điều hành | Người dùng trực tiếp | Lập lịch chạy theo tuần, huỷ chuyến | Có | REQ-41 đến REQ-47 |
| SH-11 | Tài xế | Người hưởng lợi gián tiếp | Được xếp lịch không chồng chuyến, không lái quá 10 giờ một ngày | Không (nguồn không nêu tài xế thao tác với hệ thống) | REQ-42, REQ-44, REQ-45 |
| SH-12 | Quản lý nhà xe | Người dùng trực tiếp | Đặt giá vé, mức tăng giá ngày lễ, Tết, xem báo cáo doanh thu và tỉ lệ lấp đầy | Có | REQ-51 đến REQ-54, REQ-63 đến REQ-65 |
| SH-13 | Phụ xe | Người dùng trực tiếp | Soát vé khi hành khách lên xe | Có | REQ-55 |
| SH-14 | Máy soát vé cầm tay | Hệ thống hoặc thiết bị ngoài | Thiết bị quét mã vé, báo kết quả, soát khi mất sóng | Chưa rõ (Q-01, ASM-01) | REQ-55 đến REQ-62 |

## 4. Danh sách yêu cầu

| REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |
|---|---|---|---|---|
| REQ-01 | Hệ thống quản lý 12 tuyến xe khách liên tỉnh xuất phát từ 3 bến xe, với khoảng 80 chuyến mỗi ngày. | Dữ liệu | "Nhà xe SaoViet khai thác 12 tuyến xe khách liên tỉnh xuất phát từ 3 bến xe, mỗi ngày khoảng 80 chuyến." (Đoạn mở đầu, câu 1) | Số liệu quy mô trong câu bối cảnh, dùng làm điều kiện dung lượng ở P06 |
| REQ-02 | Đội xe gồm khoảng 50 xe giường nằm 40 chỗ và 20 xe ghế ngồi 29 chỗ. | Dữ liệu | "Đội xe gồm khoảng 50 xe giường nằm 40 chỗ và 20 xe ghế ngồi 29 chỗ." (Đoạn mở đầu, câu 2) | Số liệu quy mô; hai loại xe dùng ở REQ-52 |
| REQ-03 | Hành khách có thể đặt vé qua website mà không bắt buộc có tài khoản. | Chức năng | "Hành khách đặt vé qua website." (Mục 1, câu 1)<br>"đặt vé không bắt buộc có tài khoản" (Mục 2, câu 2) | Ràng buộc kênh website tách thành REQ-04; Q-09 |
| REQ-04 | Hệ thống phải cung cấp chức năng đặt vé cho hành khách trên website. | Ràng buộc | "Hành khách đặt vé qua website." (Mục 1, câu 1) | Tách từ cùng câu với REQ-03 |
| REQ-05 | Hành khách có thể tìm chuyến theo điểm đi, điểm đến và ngày đi mà không cần tài khoản. | Chức năng | "Hành khách tìm chuyến theo điểm đi, điểm đến và ngày đi" (Mục 1, câu 2)<br>"Việc tìm chuyến và xem chỗ trống không cần tài khoản." (Mục 1, câu 3) | Không có |
| REQ-06 | Hành khách có thể xem sơ đồ chỗ của chuyến với các chỗ còn trống mà không cần tài khoản. | Chức năng | "xem sơ đồ chỗ của chuyến với các chỗ còn trống" (Mục 1, câu 2)<br>"Việc tìm chuyến và xem chỗ trống không cần tài khoản." (Mục 1, câu 3) | Tách từ cùng câu với REQ-05 |
| REQ-07 | Hành khách có thể chọn chỗ của chuyến khi đặt vé. | Chức năng | "rồi chọn tối đa 5 chỗ trong một lần đặt" (Mục 1, câu 2) | Tách từ cùng câu với REQ-05, REQ-08 |
| REQ-08 | Mỗi lần đặt vé được chọn tối đa 5 chỗ. | Quy tắc nghiệp vụ | "rồi chọn tối đa 5 chỗ trong một lần đặt" (Mục 1, câu 2) | Tách từ cùng câu với REQ-07; Q-09 |
| REQ-09 | Thông tin đặt vé gồm họ tên và số điện thoại của người đi. | Dữ liệu | "Khi đặt vé, hành khách nhập họ tên và số điện thoại của người đi." (Mục 2, câu 1) | Q-08 |
| REQ-10 | Hành khách có thể đăng ký tài khoản bằng số điện thoại. | Chức năng | "Hành khách có thể đăng ký tài khoản bằng số điện thoại" (Mục 2, câu 2) | Q-07 |
| REQ-11 | Hành khách có tài khoản có thể xem lại lịch sử vé. | Chức năng | "để xem lại lịch sử vé" (Mục 2, câu 2) | Tách từ cùng câu với REQ-10; Q-06, Q-07 |
| REQ-12 | Hệ thống giữ các chỗ hành khách đã chọn để hành khách thanh toán. | Chức năng | "Các chỗ đã chọn được giữ trong 10 phút để hành khách thanh toán" (Mục 3, câu 1) | Thời hạn giữ chỗ ở REQ-13 |
| REQ-13 | Các chỗ đã chọn được giữ chờ thanh toán trong 10 phút. | Quy tắc nghiệp vụ | "Các chỗ đã chọn được giữ trong 10 phút" (Mục 3, câu 1)<br>"Hết 10 phút chưa thanh toán thành công" (Mục 3, câu 2) | Tách từ cùng câu với REQ-12; Q-10 |
| REQ-14 | Hành khách có thể thanh toán các chỗ đang giữ qua cổng thanh toán trực tuyến của đối tác. | Chức năng | "để hành khách thanh toán qua cổng thanh toán trực tuyến của đối tác" (Mục 3, câu 1) | Tách từ cùng câu với REQ-12; Kênh: cổng thanh toán trực tuyến của đối tác (SH-04, REQ-15) |
| REQ-15 | Hệ thống trao đổi thông tin thanh toán với cổng thanh toán trực tuyến của đối tác qua API để thu tiền vé. | Giao tiếp ngoài | "thanh toán qua cổng thanh toán trực tuyến của đối tác" (Mục 3, câu 1)<br>"Cổng thanh toán trực tuyến của đối tác (API thanh toán và hoàn tiền, chưa có tài liệu API)" (project-profile.md, HE_THONG_NGOAI) | Cùng hệ thống ngoài với REQ-35; Q-24 |
| REQ-16 | Hệ thống trả các chỗ đang giữ cho người khác chọn khi hết thời hạn giữ chỗ mà chưa thanh toán thành công. | Chức năng | "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại cho người khác." (Mục 3, câu 2) | Thời hạn ở REQ-13; Q-10 |
| REQ-17 | Hệ thống phát hành vé khi hành khách thanh toán trực tuyến thành công. | Chức năng | "Thanh toán thành công thì hệ thống phát hành vé" (Mục 3, câu 3) | Q-10 |
| REQ-18 | Mỗi chỗ được phát hành thành một vé có một mã vé. | Quy tắc nghiệp vụ | "mỗi chỗ một mã vé" (Mục 3, câu 3) | Tách từ cùng câu với REQ-17 |
| REQ-19 | Hệ thống gửi vé qua SMS tới số điện thoại người đi khi phát hành vé trực tuyến. | Chức năng | "gửi qua SMS tới số điện thoại người đi" (Mục 3, câu 3) | Tách từ cùng câu với REQ-17; Kênh: cổng SMS của nhà mạng (SH-05, REQ-20); Q-04, Q-08 |
| REQ-20 | Hệ thống trao đổi nội dung tin nhắn với cổng SMS của nhà mạng qua API REST để gửi SMS cho hành khách. | Giao tiếp ngoài | "gửi qua SMS tới số điện thoại người đi" (Mục 3, câu 3)<br>"hệ thống gửi SMS cho mọi hành khách đã có vé" (Mục 6, câu 4)<br>"Cổng SMS của nhà mạng (API REST)" (project-profile.md, HE_THONG_NGOAI) | Không có |
| REQ-21 | Nhân viên bán vé có thể bán vé tại quầy cho khách mua trực tiếp. | Chức năng | "Nhân viên bán vé tại quầy bán vé cho khách mua trực tiếp" (Mục 4, câu 1) | Q-09, Q-11 |
| REQ-22 | Vé bán tại quầy cho khách mua trực tiếp được thanh toán bằng tiền mặt. | Quy tắc nghiệp vụ | "thu tiền mặt" (Mục 4, câu 1) | Tách từ cùng câu với REQ-21 |
| REQ-23 | Nhân viên bán vé có thể in vé giấy có mã vạch cho vé bán tại quầy. | Chức năng | "in vé giấy có mã vạch" (Mục 4, câu 1) | Tách từ cùng câu với REQ-21; Thiết bị: máy in vé nhiệt tại quầy (SH-08, REQ-24) |
| REQ-24 | Hệ thống trao đổi dữ liệu vé với máy in vé nhiệt tại quầy để in vé giấy có mã vạch. | Giao tiếp ngoài | "in vé giấy có mã vạch" (Mục 4, câu 1)<br>"Máy in vé nhiệt tại quầy" (project-profile.md, HE_THONG_NGOAI) | Không có |
| REQ-25 | Nhân viên bán vé có thể nhận đặt chỗ qua điện thoại. | Chức năng | "Nhân viên bán vé cũng nhận đặt chỗ qua điện thoại" (Mục 4, câu 2) | ASM-05; Q-05, Q-09 |
| REQ-26 | Nhân viên bán vé có thể nhận thanh toán tại quầy cho vé đặt qua điện thoại. | Chức năng | "vé đặt qua điện thoại phải được thanh toán tại quầy" (Mục 4, câu 2) | Chủ thể suy từ "tại quầy" vì Mục 4 chỉ nêu nhân viên bán vé làm việc tại quầy, xem mục 5 dòng 26 |
| REQ-27 | Vé đặt qua điện thoại phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến. | Quy tắc nghiệp vụ | "vé đặt qua điện thoại phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến" (Mục 4, câu 2) | Tách từ cùng câu với REQ-26 |
| REQ-28 | Hệ thống tự động huỷ vé đặt qua điện thoại chưa được thanh toán khi quá thời hạn thanh toán. | Chức năng | "nếu không sẽ tự động bị huỷ" (Mục 4, câu 2) | Thời hạn ở REQ-27; ASM-05; Q-05 |
| REQ-29 | Hành khách có thể trả vé. | Chức năng | "Hành khách được đổi hoặc trả vé." (Mục 5, câu 1) | ASM-02; Q-02 |
| REQ-30 | Hành khách có thể đổi vé. | Chức năng | "Hành khách được đổi hoặc trả vé." (Mục 5, câu 1) | Tách từ cùng câu với REQ-29; ASM-02; Q-02 |
| REQ-31 | Vé được trả trước giờ xuất bến từ 24 giờ trở lên được hoàn 90% giá vé. | Quy tắc nghiệp vụ | "Trả vé trước giờ xuất bến từ 24 giờ trở lên được hoàn 90% giá vé" (Mục 5, câu 2) | Không mâu thuẫn với REQ-50, xem mục 5 dòng 28 |
| REQ-32 | Vé được trả trước giờ xuất bến từ 4 giờ đến dưới 24 giờ được hoàn 50% giá vé. | Quy tắc nghiệp vụ | "từ 4 giờ đến dưới 24 giờ hoàn 50%" (Mục 5, câu 2) | Tách từ cùng câu với REQ-31 |
| REQ-33 | Vé không được trả khi còn dưới 4 giờ trước giờ xuất bến. | Quy tắc nghiệp vụ | "dưới 4 giờ không được trả" (Mục 5, câu 2) | Tách từ cùng câu với REQ-31; không mâu thuẫn với REQ-50, xem mục 5 dòng 28 |
| REQ-34 | Vé mua trực tuyến được hoàn tiền qua cổng thanh toán trực tuyến của đối tác. | Quy tắc nghiệp vụ | "Vé mua trực tuyến được hoàn qua cổng thanh toán" (Mục 5, câu 3) | Kênh: REQ-35; Q-14 |
| REQ-35 | Hệ thống trao đổi yêu cầu hoàn tiền với cổng thanh toán trực tuyến của đối tác qua API để hoàn tiền vé mua trực tuyến. | Giao tiếp ngoài | "Vé mua trực tuyến được hoàn qua cổng thanh toán" (Mục 5, câu 3)<br>"API thanh toán và hoàn tiền, chưa có tài liệu API" (project-profile.md, HE_THONG_NGOAI) | Cùng hệ thống ngoài với REQ-15; Q-24 |
| REQ-36 | Vé mua tại quầy được hoàn tiền mặt tại quầy. | Quy tắc nghiệp vụ | "vé mua tại quầy được hoàn tiền mặt tại quầy" (Mục 5, câu 3) | Tách từ cùng câu với REQ-34; ASM-02; Q-02, Q-14 |
| REQ-37 | Vé chỉ được đổi sang chuyến khác cùng tuyến. | Quy tắc nghiệp vụ | "Mỗi vé chỉ được đổi sang chuyến khác cùng tuyến một lần" (Mục 5, câu 4) | Không có |
| REQ-38 | Mỗi vé chỉ được đổi một lần. | Quy tắc nghiệp vụ | "Mỗi vé chỉ được đổi sang chuyến khác cùng tuyến một lần" (Mục 5, câu 4) | Tách từ cùng câu với REQ-37; Q-21 |
| REQ-39 | Vé chỉ được đổi chậm nhất 4 giờ trước giờ xuất bến. | Quy tắc nghiệp vụ | "chậm nhất 4 giờ trước giờ xuất bến" (Mục 5, câu 4) | Tách từ cùng câu với REQ-37; Q-13 |
| REQ-40 | Hành khách trả thêm phần chênh lệch khi vé mới sau khi đổi đắt hơn vé cũ. | Quy tắc nghiệp vụ | "và trả thêm phần chênh lệch nếu vé mới đắt hơn" (Mục 5, câu 4) | Tách từ cùng câu với REQ-37; Q-02, Q-12 |
| REQ-41 | Nhân viên điều hành có thể lập lịch chạy theo tuần. | Chức năng | "Nhân viên điều hành lập lịch chạy theo tuần" (Mục 6, câu 1) | Q-03 |
| REQ-42 | Mỗi chuyến trong lịch chạy gồm tuyến, giờ xuất bến, xe và tài xế. | Dữ liệu | "với mỗi chuyến, chọn tuyến, giờ xuất bến, xe và tài xế" (Mục 6, câu 1) | Tách từ cùng câu với REQ-41; Q-03, Q-16 |
| REQ-43 | Một xe không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Quy tắc nghiệp vụ | "Một xe hoặc một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau." (Mục 6, câu 2) | ASM-03; Q-17 |
| REQ-44 | Một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Quy tắc nghiệp vụ | "Một xe hoặc một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau." (Mục 6, câu 2) | Tách từ cùng câu với REQ-43; ASM-03; Q-16, Q-17 |
| REQ-45 | Tài xế không được lái quá 10 giờ trong một ngày. | Quy tắc nghiệp vụ | "Tài xế không được lái quá 10 giờ trong một ngày." (Mục 6, câu 3) | ASM-03; Q-16, Q-17, Q-18 |
| REQ-46 | Mỗi tuyến có thời gian chạy dự kiến dùng để xác định thời gian chạy của chuyến. | Dữ liệu | Giả định ASM-03 | Phục vụ REQ-43, REQ-44, REQ-45; Q-03, Q-17 |
| REQ-47 | Nhân viên điều hành có thể huỷ chuyến. | Chức năng | "Khi phải huỷ chuyến (xe hỏng, thời tiết), nhân viên điều hành huỷ chuyến" (Mục 6, câu 4) | Lý do huỷ nguồn nêu làm ví dụ: xe hỏng, thời tiết |
| REQ-48 | Hệ thống gửi SMS cho "mọi" hành khách đã có vé của chuyến khi chuyến bị huỷ. | Chức năng | "hệ thống gửi SMS cho mọi hành khách đã có vé" (Mục 6, câu 4) | Tách từ cùng câu với REQ-47; Kênh: cổng SMS của nhà mạng (REQ-20); Q-15 |
| REQ-49 | Hệ thống hoàn tiền cho "mọi" hành khách đã có vé của chuyến khi chuyến bị huỷ. | Chức năng | "hệ thống gửi SMS cho mọi hành khách đã có vé và hoàn 100% giá vé" (Mục 6, câu 4) | Tách từ cùng câu với REQ-47; Q-14, Q-15 |
| REQ-50 | Vé của chuyến bị huỷ được hoàn 100% giá vé. | Quy tắc nghiệp vụ | "và hoàn 100% giá vé" (Mục 6, câu 4) | Tách từ cùng câu với REQ-49; Q-14 |
| REQ-51 | Quản lý nhà xe có thể đặt giá vé. | Chức năng | "Giá vé do quản lý nhà xe đặt theo tuyến và loại xe." (Mục 7, câu 1) | Không có |
| REQ-52 | Giá vé được đặt theo tuyến và loại xe. | Quy tắc nghiệp vụ | "Giá vé do quản lý nhà xe đặt theo tuyến và loại xe." (Mục 7, câu 1) | Tách từ cùng câu với REQ-51 |
| REQ-53 | Quản lý nhà xe có thể đặt mức tăng giá theo phần trăm cho một khoảng ngày vào dịp lễ, Tết. | Chức năng | "Ngày lễ, Tết, quản lý có thể đặt mức tăng giá theo phần trăm cho một khoảng ngày" (Mục 7, câu 2) | ASM-04; Q-19, Q-20, Q-25 |
| REQ-54 | Mức tăng giá ngày lễ, Tết tối đa 30%. | Quy tắc nghiệp vụ | "tối đa 30%" (Mục 7, câu 2) | Tách từ cùng câu với REQ-53 |
| REQ-55 | Phụ xe có thể quét mã vé bằng máy soát vé cầm tay khi hành khách lên xe. | Chức năng | "Phụ xe mỗi chuyến dùng máy soát vé cầm tay quét mã vé khi hành khách lên xe." (Mục 8, câu 1) | ASM-01; Q-01, Q-04 |
| REQ-56 | Chức năng soát vé phải chạy trên máy soát vé cầm tay Android có đầu quét mã vạch do nhà xe tự trang bị. | Ràng buộc | "dùng máy soát vé cầm tay" (Mục 8, câu 1)<br>"Máy soát vé cầm tay Android có đầu quét mã vạch, do nhà xe tự trang bị" (project-profile.md, HE_THONG_NGOAI) | ASM-01; Q-01 |
| REQ-57 | Máy soát vé báo vé được quét là hợp lệ hoặc không hợp lệ. | Chức năng | "Máy báo hợp lệ hay không hợp lệ" (Mục 8, câu 2) | ASM-01 |
| REQ-58 | Vé không hợp lệ khi soát nếu vé sai chuyến, vé đã huỷ hoặc vé đã soát. | Quy tắc nghiệp vụ | "(sai chuyến, vé đã huỷ, vé đã soát)" (Mục 8, câu 2) | Tách từ cùng câu với REQ-57; chưa tách ba trường hợp vì nguồn nêu chung một quy tắc kiểm tra; Q-21 |
| REQ-59 | Máy soát vé soát được vé khi xe ở vùng mất sóng. | Phi chức năng | "Máy cần soát được cả khi xe ở vùng mất sóng" (Mục 8, câu 3) | ASM-01; Q-11 |
| REQ-60 | Máy soát vé gửi lại kết quả soát vé khi có sóng. | Chức năng | "và gửi lại kết quả khi có sóng" (Mục 8, câu 3) | Tách từ cùng câu với REQ-59; ASM-01 |
| REQ-61 | Hệ thống gửi danh sách hành khách của chuyến về máy soát vé trước giờ xuất bến. | Chức năng | "15 phút trước giờ xuất bến, hệ thống gửi danh sách hành khách của chuyến về máy soát vé." (Mục 8, câu 4) | Thời điểm gửi ở REQ-62; Q-11 |
| REQ-62 | Danh sách hành khách của chuyến được gửi về máy soát vé 15 phút trước giờ xuất bến. | Quy tắc nghiệp vụ | "15 phút trước giờ xuất bến, hệ thống gửi danh sách hành khách của chuyến về máy soát vé." (Mục 8, câu 4) | Tách từ cùng câu với REQ-61; Q-11 |
| REQ-63 | Quản lý nhà xe có thể xem báo cáo doanh thu theo ngày. | Chức năng | "Quản lý xem báo cáo doanh thu theo ngày, theo tuyến, và tỉ lệ lấp đầy chỗ của từng chuyến." (Mục 9, câu 1) | ASM-04; Q-23, Q-25 |
| REQ-64 | Quản lý nhà xe có thể xem báo cáo doanh thu theo tuyến. | Chức năng | "Quản lý xem báo cáo doanh thu theo ngày, theo tuyến, và tỉ lệ lấp đầy chỗ của từng chuyến." (Mục 9, câu 1) | Tách từ cùng câu với REQ-63; ASM-04; Q-23 |
| REQ-65 | Quản lý nhà xe có thể xem báo cáo tỉ lệ lấp đầy chỗ của từng chuyến. | Chức năng | "Quản lý xem báo cáo doanh thu theo ngày, theo tuyến, và tỉ lệ lấp đầy chỗ của từng chuyến." (Mục 9, câu 1) | Tách từ cùng câu với REQ-63; ASM-04 |
| REQ-66 | Hệ thống "chịu được" khoảng 2.000 người truy cập cùng lúc vào dịp Tết. | Phi chức năng | "Hệ thống phải chịu được khoảng 2.000 người truy cập cùng lúc vào dịp Tết." (Mục 10, câu 1) | Q-22 |
| REQ-67 | Hai vé không được cùng một chỗ trên một chuyến. | Quy tắc nghiệp vụ | "Không được để hai vé cùng một chỗ trên một chuyến." (Mục 10, câu 2) | Gắn với mục tiêu chấm dứt trùng chỗ (mục 1); ASM-05 |
| REQ-68 | Hệ thống không được lưu thông tin thẻ của hành khách. | Ràng buộc | "Hệ thống không lưu thông tin thẻ của hành khách." (Mục 10, câu 3) | Không có |

## 5. Vấn đề chất lượng của tài liệu nguồn

| STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
|---|---|---|---|---|---|
| 1 | Mơ hồ | REQ-55 đến REQ-62 | Mục 8, câu 2-3: "Máy báo hợp lệ hay không hợp lệ ... Máy cần soát được cả khi xe ở vùng mất sóng và gửi lại kết quả khi có sóng"; project-profile.md, HE_THONG_NGOAI liệt kê "Máy soát vé cầm tay Android" là hệ thống ngoài | Nguồn giao hành vi nghiệp vụ cho máy nhưng hồ sơ xếp máy vào hệ thống ngoài; chưa rõ phần mềm soát vé có thuộc phạm vi. Tạm coi phần mềm thuộc phạm vi, phần cứng là thiết bị ngoài | Q-01, ASM-01 |
| 2 | Thiếu | REQ-29, REQ-30, REQ-40 | Mục 5, câu 1: "Hành khách được đổi hoặc trả vé."; Mục 5, câu 3: "Vé mua trực tuyến được hoàn qua cổng thanh toán; vé mua tại quầy được hoàn tiền mặt tại quầy" | Không nêu đổi, trả thực hiện ở kênh nào và ai thao tác; tạm theo kênh mua | Q-02, ASM-02 |
| 3 | Thiếu | REQ-41, REQ-42, REQ-46, REQ-51 | Mục 6, câu 1: "với mỗi chuyến, chọn tuyến, giờ xuất bến, xe và tài xế" | Lập lịch cần danh mục tuyến, xe, tài xế có sẵn nhưng nguồn không nêu ai cập nhật danh mục. Không tự thêm chức năng | Q-03 |
| 4 | Thiếu | REQ-19, REQ-55, REQ-57 | Mục 3, câu 3: "mỗi chỗ một mã vé, gửi qua SMS"; Mục 4, câu 1: "in vé giấy có mã vạch"; Mục 8, câu 1: "quét mã vé" | Vé giấy có mã vạch để quét, còn vé trực tuyến chỉ nêu mã vé gửi qua SMS; chưa rõ máy soát vé đọc vé trực tuyến thế nào | Q-04 |
| 5 | Mơ hồ | REQ-25, REQ-27, REQ-28, REQ-67 | Mục 4, câu 2: "nhận đặt chỗ qua điện thoại; vé đặt qua điện thoại phải được thanh toán tại quầy ... nếu không sẽ tự động bị huỷ" | Nguồn dùng lẫn "đặt chỗ" và "vé"; chưa rõ đặt chỗ qua điện thoại có giữ chỗ trên chuyến không. Tạm coi có giữ chỗ để thoả REQ-67 | Q-05, ASM-05 |
| 6 | Mơ hồ | REQ-11 | Mục 2, câu 2: "đăng ký tài khoản bằng số điện thoại để xem lại lịch sử vé; đặt vé không bắt buộc có tài khoản" | Vé đặt không cần tài khoản có vào lịch sử vé của tài khoản cùng số điện thoại không | Q-06 |
| 7 | Thiếu | REQ-10, REQ-11 | Mục 2, câu 2: "đăng ký tài khoản bằng số điện thoại" | Có tài khoản nhưng không nêu cách xác thực khi dùng tài khoản | Q-07 |
| 8 | Mơ hồ | REQ-09, REQ-19 | Mục 2, câu 1: "hành khách nhập họ tên và số điện thoại của người đi"; Mục 1, câu 2: "chọn tối đa 5 chỗ trong một lần đặt" | Một lần đặt nhiều chỗ: nhập thông tin cho từng người đi hay một người; SMS gửi tới số nào | Q-08 |
| 9 | Mơ hồ | REQ-08, REQ-21, REQ-25 | Mục 1, câu 2: "chọn tối đa 5 chỗ trong một lần đặt" | Câu nằm trong mục đặt vé qua website; chưa rõ giới hạn có áp dụng cho quầy và điện thoại | Q-09 |
| 10 | Thiếu | REQ-13, REQ-16, REQ-17 | Mục 3, câu 2-3: "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại ... Thanh toán thành công thì hệ thống phát hành vé" | Không nêu trường hợp cổng thanh toán báo thành công sau khi chỗ đã được trả lại | Q-10 |
| 11 | Thiếu | REQ-21, REQ-59, REQ-61, REQ-62 | Mục 8, câu 4: "15 phút trước giờ xuất bến, hệ thống gửi danh sách hành khách của chuyến về máy soát vé"; Mục 8, câu 3: "soát được cả khi xe ở vùng mất sóng" | Không nêu xử lý vé bán, đổi, huỷ sau mốc gửi danh sách, trong khi máy có thể soát khi mất sóng chỉ với danh sách đã nhận | Q-11 |
| 12 | Thiếu | REQ-40 | Mục 5, câu 4: "trả thêm phần chênh lệch nếu vé mới đắt hơn" | Chỉ nêu chiều vé mới đắt hơn, không nêu chiều vé mới rẻ hơn | Q-12 |
| 13 | Mơ hồ | REQ-39 | Mục 5, câu 4: "chậm nhất 4 giờ trước giờ xuất bến" | Không rõ giờ xuất bến của chuyến cũ hay chuyến mới | Q-13 |
| 14 | Thiếu | REQ-34, REQ-36, REQ-49, REQ-50 | Mục 6, câu 4: "hoàn 100% giá vé"; Mục 5, câu 3: kênh hoàn theo kênh mua | Không nêu kênh hoàn tiền khi huỷ chuyến | Q-14 |
| 15 | Mơ hồ | REQ-48, REQ-49 | Mục 6, câu 4: "gửi SMS cho mọi hành khách đã có vé" | Từ tổng thể tuyệt đối "mọi" (F6); chưa rõ có gồm khách đặt chỗ qua điện thoại chưa thanh toán | Q-15 |
| 16 | Mơ hồ | REQ-42, REQ-44, REQ-45 | Mục 6, câu 1: "chọn tuyến, giờ xuất bến, xe và tài xế" | Không rõ một chuyến có một hay nhiều tài xế | Q-16 |
| 17 | Thiếu | REQ-43, REQ-44, REQ-45, REQ-46 | Mục 6, câu 2-3: "thời gian chạy chồng nhau"; "không được lái quá 10 giờ trong một ngày" | Hai quy tắc cần thời điểm kết thúc chuyến, nguồn chỉ nêu giờ xuất bến | Q-17, ASM-03 |
| 18 | Mơ hồ | REQ-45 | Mục 6, câu 3: "trong một ngày" | Không rõ ngày theo lịch hay 24 giờ liên tục; chuyến qua nửa đêm tính thế nào | Q-18 |
| 19 | Mơ hồ | REQ-53 | Mục 7, câu 2: "cho một khoảng ngày" | Không rõ khoảng ngày áp dụng theo ngày xuất bến hay ngày mua vé | Q-19 |
| 20 | Mơ hồ | REQ-52, REQ-53 | Mục 7, câu 2: "đặt mức tăng giá theo phần trăm cho một khoảng ngày" | Không rõ mức tăng áp dụng cho mọi tuyến, loại xe hay từng tuyến, loại xe | Q-20 |
| 21 | Mơ hồ | REQ-38, REQ-58 | Mục 8, câu 2: "(sai chuyến, vé đã huỷ, vé đã soát)"; Mục 5, câu 4: "đổi sang chuyến khác" | Không rõ vé cũ sau khi đổi được coi là "vé đã huỷ" khi soát | Q-21 |
| 22 | Không kiểm chứng được | REQ-66 | Mục 10, câu 1: "phải chịu được khoảng 2.000 người truy cập cùng lúc" | "Chịu được" không có tiêu chí đo (thời gian phản hồi); "khoảng" không cho ngưỡng chính xác. Giữ nguyên ý nguồn, không tự thêm ngưỡng | Q-22 |
| 23 | Mơ hồ | REQ-63, REQ-64 | Mục 9, câu 1: "báo cáo doanh thu" | Không rõ doanh thu tính trước hay sau khi trừ tiền hoàn vé | Q-23 |
| 24 | Thiếu | REQ-15, REQ-35 | project-profile.md, HE_THONG_NGOAI: "API thanh toán và hoàn tiền, chưa có tài liệu API" | Thiếu tài liệu giao tiếp với cổng thanh toán; cần trước khi thiết kế giao diện hệ thống | Q-24 |
| 25 | Mơ hồ | REQ-53, REQ-63, REQ-64, REQ-65 | Mục 7, câu 1: "quản lý nhà xe"; Mục 7, câu 2 và Mục 9, câu 1: "quản lý" | Tham chiếu vai trò rút gọn; tạm coi là cùng vai trò quản lý nhà xe | Q-25, ASM-04 |
| 26 | Mơ hồ | REQ-26, REQ-36 | Mục 4, câu 2: "phải được thanh toán tại quầy"; Mục 5, câu 3: "được hoàn tiền mặt tại quầy" | Câu bị động không nêu chủ thể (F6). Ghi chủ thể là nhân viên bán vé vì Mục 4 chỉ nêu vai trò này làm việc tại quầy; ai thực hiện đổi, trả gắn với Q-02 | Q-02, ASM-02 |
| 27 | Mơ hồ | REQ-50 | Mục 6, câu 4: "hoàn 100% giá vé" | Đã rà theo F6 (nhóm "100%"): đây là tỉ lệ hoàn tiền xác định, không phải tuyên bố tuyệt đối về hành vi hệ thống. Giữ nguyên; câu hỏi còn lại về kênh hoàn đã ở Q-14 | Q-14 |
| 28 | Mâu thuẫn | REQ-31, REQ-33, REQ-50 | Mục 5, câu 2: "dưới 4 giờ không được trả"; Mục 6, câu 4: "hệ thống gửi SMS cho mọi hành khách đã có vé và hoàn 100% giá vé" | Không mâu thuẫn, tách thành hai REQ có điều kiện: hành khách tự trả vé (REQ-31 đến REQ-33) khác với nhà xe huỷ chuyến (REQ-50) | Không có |

## 6. Ma trận phủ nguồn

| Vị trí trong nguồn | Tóm tắt nội dung | Kết luận (REQ-xx / Ngoài phạm vi / Bối cảnh) |
|---|---|---|
| Tiêu đề | Tên hệ thống bán vé xe khách liên tỉnh SaoViet Bus | Bối cảnh |
| Đoạn mở đầu, câu 1 | 12 tuyến, 3 bến xe, khoảng 80 chuyến mỗi ngày | REQ-01 |
| Đoạn mở đầu, câu 2 | Đội xe khoảng 50 xe giường nằm 40 chỗ, 20 xe ghế ngồi 29 chỗ | REQ-02 |
| Đoạn mở đầu, câu 3 | Cách làm hiện tại: bán qua điện thoại, quầy, ghi sổ tay, thường trùng chỗ | Bối cảnh (mục tiêu ở mục 1) |
| Đoạn mở đầu, câu 4 | Nhà xe cần phần mềm bán vé và quản lý chuyến | Bối cảnh (mục tiêu ở mục 1) |
| Mục 1, câu 1 | Hành khách đặt vé qua website | REQ-03, REQ-04 |
| Mục 1, câu 2 | Tìm chuyến theo điểm đi, điểm đến, ngày đi; xem sơ đồ chỗ trống; chọn tối đa 5 chỗ một lần đặt | REQ-05, REQ-06, REQ-07, REQ-08 |
| Mục 1, câu 3 | Tìm chuyến, xem chỗ trống không cần tài khoản | REQ-05, REQ-06 |
| Mục 2, câu 1 | Nhập họ tên, số điện thoại người đi khi đặt vé | REQ-09 |
| Mục 2, câu 2 | Đăng ký tài khoản bằng số điện thoại để xem lịch sử vé; đặt vé không bắt buộc tài khoản | REQ-10, REQ-11, REQ-03 |
| Mục 3, câu 1 | Giữ chỗ 10 phút để thanh toán qua cổng thanh toán trực tuyến của đối tác | REQ-12, REQ-13, REQ-14, REQ-15 |
| Mục 3, câu 2 | Hết 10 phút chưa thanh toán thì trả chỗ | REQ-16, REQ-13 |
| Mục 3, câu 3 | Thanh toán thành công thì phát hành vé, mỗi chỗ một mã vé, gửi SMS tới người đi | REQ-17, REQ-18, REQ-19, REQ-20 |
| Mục 4, câu 1 | Nhân viên bán vé bán tại quầy, thu tiền mặt, in vé giấy có mã vạch | REQ-21, REQ-22, REQ-23, REQ-24 |
| Mục 4, câu 2 | Nhận đặt chỗ qua điện thoại; thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến; quá hạn tự động huỷ | REQ-25, REQ-26, REQ-27, REQ-28 |
| Mục 5, câu 1 | Hành khách được đổi hoặc trả vé | REQ-29, REQ-30 |
| Mục 5, câu 2 | Mức hoàn khi trả vé: từ 24 giờ 90%, từ 4 đến dưới 24 giờ 50%, dưới 4 giờ không được trả | REQ-31, REQ-32, REQ-33 |
| Mục 5, câu 3 | Vé trực tuyến hoàn qua cổng thanh toán; vé tại quầy hoàn tiền mặt tại quầy | REQ-34, REQ-35, REQ-36 |
| Mục 5, câu 4 | Đổi sang chuyến khác cùng tuyến, một lần, chậm nhất 4 giờ trước giờ xuất bến, trả chênh lệch nếu vé mới đắt hơn | REQ-37, REQ-38, REQ-39, REQ-40 |
| Mục 6, câu 1 | Nhân viên điều hành lập lịch theo tuần, mỗi chuyến chọn tuyến, giờ xuất bến, xe, tài xế | REQ-41, REQ-42 |
| Mục 6, câu 2 | Xe, tài xế không xếp vào hai chuyến chồng thời gian | REQ-43, REQ-44 |
| Mục 6, câu 3 | Tài xế không lái quá 10 giờ một ngày | REQ-45 |
| Mục 6, câu 4 | Nhân viên điều hành huỷ chuyến; hệ thống gửi SMS và hoàn 100% giá vé cho hành khách đã có vé | REQ-47, REQ-48, REQ-49, REQ-50, REQ-20 |
| Mục 7, câu 1 | Quản lý nhà xe đặt giá vé theo tuyến và loại xe | REQ-51, REQ-52 |
| Mục 7, câu 2 | Mức tăng giá ngày lễ, Tết theo phần trăm cho một khoảng ngày, tối đa 30% | REQ-53, REQ-54 |
| Mục 8, câu 1 | Phụ xe dùng máy soát vé cầm tay quét mã vé khi lên xe | REQ-55, REQ-56 |
| Mục 8, câu 2 | Máy báo hợp lệ, không hợp lệ (sai chuyến, đã huỷ, đã soát) | REQ-57, REQ-58 |
| Mục 8, câu 3 | Soát được khi mất sóng, gửi lại kết quả khi có sóng | REQ-59, REQ-60 |
| Mục 8, câu 4 | 15 phút trước giờ xuất bến gửi danh sách hành khách về máy soát vé | REQ-61, REQ-62 |
| Mục 9, câu 1 | Quản lý xem báo cáo doanh thu theo ngày, theo tuyến, tỉ lệ lấp đầy từng chuyến | REQ-63, REQ-64, REQ-65 |
| Mục 10, câu 1 | Chịu được khoảng 2.000 người truy cập cùng lúc dịp Tết | REQ-66 |
| Mục 10, câu 2 | Không để hai vé cùng một chỗ trên một chuyến | REQ-67 |
| Mục 10, câu 3 | Không lưu thông tin thẻ của hành khách | REQ-68; Ngoài phạm vi (lưu thông tin thẻ) |
| project-profile.md, MO_TA_MOT_CAU | Mô tả một câu về hệ thống | Bối cảnh (mục tiêu ở mục 1) |
| project-profile.md, HE_THONG_NGOAI: cổng thanh toán | API thanh toán và hoàn tiền, chưa có tài liệu API | REQ-15, REQ-35; Ngoài phạm vi (xử lý giao dịch thanh toán) |
| project-profile.md, HE_THONG_NGOAI: cổng SMS | Cổng SMS của nhà mạng, API REST | REQ-20; Ngoài phạm vi (chuyển tin nhắn tới thuê bao) |
| project-profile.md, HE_THONG_NGOAI: máy soát vé | Máy cầm tay Android có đầu quét mã vạch, do nhà xe tự trang bị | REQ-56; Ngoài phạm vi (trang bị phần cứng) |
| project-profile.md, HE_THONG_NGOAI: máy in | Máy in vé nhiệt tại quầy | REQ-24; Ngoài phạm vi (thiết bị in) |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-01 | Phần mềm soát vé chạy trên máy soát vé cầm tay có thuộc phạm vi hệ thống cần xây dựng không, hay máy đã có phần mềm riêng và hệ thống chỉ trao đổi dữ liệu với máy? (Thuộc phạm vi / Thiết bị ngoài có phần mềm sẵn) | Phạm vi; REQ-55 đến REQ-62; P01 (máy soát vé là tác nhân hay không); P09 | Mục 8, câu 2-3; project-profile.md, HE_THONG_NGOAI |
| Q-02 | Hành khách đổi, trả vé qua kênh nào? (a) Vé mua trực tuyến tự đổi, trả trên website, vé mua tại quầy đổi, trả tại quầy; (b) Mọi vé chỉ đổi, trả tại quầy qua nhân viên bán vé; (c) Mọi vé đổi, trả được ở cả website và quầy | REQ-29, REQ-30, REQ-36, REQ-40; P01, P02 (danh sách use case đổi, trả vé) | Mục 5, câu 1 và câu 3 |
| Q-03 | Danh mục tuyến, xe, tài xế (và thời gian chạy của tuyến nếu có) được cập nhật vào hệ thống bởi ai? (a) Nhân viên điều hành; (b) Quản lý nhà xe; (c) Nhập một lần khi triển khai, không phải chức năng của hệ thống | Phạm vi; REQ-41, REQ-42, REQ-46, REQ-51; P02 (danh sách use case) | Mục 6, câu 1 |
| Q-04 | Phụ xe soát vé mua trực tuyến (mã vé gửi qua SMS) bằng cách nào? (a) Quét mã vạch hoặc mã QR mà SMS cung cấp; (b) Nhập tay mã vé vào máy soát vé | REQ-19, REQ-55, REQ-57; P02, P04 UC soát vé; P11b | Mục 3, câu 3; Mục 4, câu 1; Mục 8, câu 1 |
| Q-05 | Đặt chỗ qua điện thoại có giữ chỗ trên chuyến (chỗ không còn trống với khách khác) ngay khi nhân viên bán vé ghi nhận không? (Có / Không) | REQ-25, REQ-27, REQ-28, REQ-67; luồng chính và ngoại lệ của UC đặt chỗ qua điện thoại | Mục 4, câu 2 |
| Q-06 | Lịch sử vé của một tài khoản gồm những vé nào? (a) Chỉ vé đặt khi đã dùng tài khoản đó; (b) Mọi vé có số điện thoại người đi trùng số điện thoại của tài khoản | REQ-11; P04 UC xem lịch sử vé | Mục 2, câu 2 |
| Q-07 | Hành khách xác thực khi dùng tài khoản bằng cách nào? (a) Số điện thoại và mật khẩu; (b) Mã xác thực một lần gửi qua SMS | REQ-10, REQ-11; P02, P06 | Mục 2, câu 2 |
| Q-08 | Khi một lần đặt có nhiều chỗ, hành khách nhập họ tên và số điện thoại cho từng người đi hay cho một người đi đại diện cả lần đặt? (Từng người / Một người đại diện) | REQ-09, REQ-19; P04 UC đặt vé; P13 | Mục 2, câu 1; Mục 1, câu 2 |
| Q-09 | Giới hạn tối đa 5 chỗ trong một lần đặt có áp dụng cho bán vé tại quầy và đặt chỗ qua điện thoại không? (Có / Không) | REQ-08, REQ-21, REQ-25; P06 (BR) | Mục 1, câu 2 |
| Q-10 | Khi cổng thanh toán báo thành công sau khi đã hết 10 phút giữ chỗ, hệ thống xử lý thế nào? (a) Phát hành vé nếu chỗ còn trống, nếu không thì hoàn tiền; (b) Luôn hoàn tiền, không phát hành vé | REQ-13, REQ-16, REQ-17; luồng ngoại lệ của UC đặt vé | Mục 3, câu 2-3 |
| Q-11 | Vé bán, đổi, huỷ sau mốc gửi danh sách hành khách (15 phút trước giờ xuất bến) được xử lý thế nào? (a) Hệ thống gửi bổ sung thay đổi về máy soát vé khi có sóng; (b) Hệ thống ngừng bán, đổi, huỷ vé của chuyến từ mốc đó | REQ-21, REQ-59, REQ-61, REQ-62; P04 UC soát vé, UC bán vé tại quầy | Mục 8, câu 3-4 |
| Q-12 | Khi đổi sang vé mới rẻ hơn vé cũ, hành khách có được hoàn phần chênh lệch không? (Có / Không) | REQ-40; luồng thay thế của UC đổi vé | Mục 5, câu 4 |
| Q-13 | Mốc "chậm nhất 4 giờ trước giờ xuất bến" khi đổi vé tính theo giờ xuất bến của chuyến nào? (Chuyến cũ / Chuyến mới / Cả hai) | REQ-39; P06 (BR) | Mục 5, câu 4 |
| Q-14 | Khi huỷ chuyến, tiền hoàn 100% có được trả theo kênh mua như Mục 5 không (vé trực tuyến qua cổng thanh toán, vé mua tại quầy bằng tiền mặt tại quầy)? (Có / Không) | REQ-34, REQ-36, REQ-49, REQ-50; P04 UC huỷ chuyến | Mục 6, câu 4; Mục 5, câu 3 |
| Q-15 | "Mọi hành khách đã có vé" khi huỷ chuyến có gồm khách đặt chỗ qua điện thoại chưa thanh toán không? (Có / Không) | REQ-48, REQ-49; P04 UC huỷ chuyến | Mục 6, câu 4 |
| Q-16 | Một chuyến được xếp một tài xế hay có thể nhiều tài xế? (Một / Nhiều) | REQ-42, REQ-44, REQ-45; P13 | Mục 6, câu 1 |
| Q-17 | Thời gian chạy của một chuyến được xác định thế nào để kiểm tra chồng chuyến và giới hạn 10 giờ lái? (a) Giờ xuất bến cộng thời gian chạy dự kiến của tuyến; (b) Nhân viên điều hành nhập giờ đến cho từng chuyến | REQ-43, REQ-44, REQ-45, REQ-46; P04 UC lập lịch chạy | Mục 6, câu 2-3 |
| Q-18 | "Một ngày" trong giới hạn 10 giờ lái là gì? (a) Ngày theo lịch 00:00-24:00, chuyến qua nửa đêm chia giờ lái cho hai ngày; (b) 24 giờ liên tục bất kỳ | REQ-45; P06 (BR) | Mục 6, câu 3 |
| Q-19 | Mức tăng giá ngày lễ, Tết áp dụng theo ngày xuất bến của chuyến hay theo ngày mua vé? (Ngày xuất bến / Ngày mua) | REQ-53; P06 (BR) | Mục 7, câu 2 |
| Q-20 | Mức tăng giá ngày lễ, Tết áp dụng cho mọi tuyến và loại xe hay quản lý chọn từng tuyến, loại xe? (Mọi tuyến / Chọn từng tuyến, loại xe) | REQ-52, REQ-53; P04 UC đặt mức tăng giá | Mục 7, câu 2 |
| Q-21 | Vé cũ sau khi đổi sang chuyến khác, nếu bị quét, có được máy soát vé báo là "vé đã huỷ" không? (Có / Không) | REQ-38, REQ-58; P04 UC soát vé | Mục 8, câu 2; Mục 5, câu 4 |
| Q-22 | Khi có khoảng 2.000 người truy cập cùng lúc vào dịp Tết, thời gian phản hồi tối đa chấp nhận được của tìm chuyến và đặt vé là bao nhiêu giây? | REQ-66; P06 (NFR), P09 | Mục 10, câu 1 |
| Q-23 | Báo cáo doanh thu tính trước hay sau khi trừ tiền hoàn vé? (Trước / Sau) | REQ-63, REQ-64; P04 UC xem báo cáo | Mục 9, câu 1 |
| Q-24 | Tài liệu API thanh toán và hoàn tiền của cổng thanh toán đối tác có được cung cấp trước bước thiết kế giao diện hệ thống (P11b) không? (Có / Không) | REQ-15, REQ-35; P11b | project-profile.md, HE_THONG_NGOAI |
| Q-25 | "Quản lý" ở Mục 7 câu 2 và Mục 9 có phải là "quản lý nhà xe" ở Mục 7 câu 1 không? (Có / Không) | REQ-53, REQ-63, REQ-64, REQ-65; P01 | Mục 7, câu 1-2; Mục 9, câu 1 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-01 | Phần mềm soát vé chạy trên máy soát vé cầm tay thuộc phạm vi hệ thống; phần cứng máy (Android, đầu quét mã vạch) là thiết bị ngoài do nhà xe trang bị. | Mục 8 giao cho máy các hành vi nghiệp vụ (báo hợp lệ, soát khi mất sóng, gửi lại kết quả) cần dữ liệu vé của hệ thống; hồ sơ dự án chỉ nói máy "do nhà xe tự trang bị". Chờ Q-01 | Phạm vi; SH-14; REQ-55 đến REQ-60 |
| ASM-02 | Kênh đổi, trả vé theo kênh mua: vé mua trực tuyến do hành khách tự đổi, trả trên website; vé mua tại quầy (gồm vé đặt qua điện thoại đã thanh toán tại quầy) đổi, trả tại quầy do nhân viên bán vé thực hiện. | Mục 5 câu 3 phân kênh hoàn tiền theo kênh mua. Chờ Q-02 | REQ-29, REQ-30, REQ-36, REQ-40 |
| ASM-03 | Thời gian chạy của một chuyến tính từ giờ xuất bến tới giờ xuất bến cộng thời gian chạy dự kiến của tuyến. | Mục 6 câu 2-3 cần thời điểm kết thúc chuyến để kiểm tra chồng chuyến và giới hạn 10 giờ lái, nguồn chỉ nêu giờ xuất bến. Chờ Q-17 | REQ-43, REQ-44, REQ-45, REQ-46 |
| ASM-04 | "Quản lý" ở Mục 7 câu 2 và Mục 9 là vai trò quản lý nhà xe ở Mục 7 câu 1. | Cùng đoạn văn dùng dạng đầy đủ rồi rút gọn; nguồn không nêu vai trò quản lý nào khác. Chờ Q-25 | SH-12; REQ-53, REQ-63, REQ-64, REQ-65 |
| ASM-05 | Đặt chỗ qua điện thoại giữ chỗ trên chuyến từ khi nhân viên bán vé ghi nhận tới khi được thanh toán hoặc bị tự động huỷ; khi bị huỷ, chỗ trở lại còn trống. | Mục 4 câu 2 gọi đặt chỗ qua điện thoại là "vé" và cho tự động huỷ khi quá hạn; Mục 10 câu 2 cấm hai vé cùng một chỗ. Chờ Q-05 | REQ-25, REQ-28, REQ-67 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Chọn giữa hai quy tắc (C9): F3 câu 1 xếp câu nêu hành vi nghiệp vụ có nhắc hệ thống ngoài làm kênh vào Chức năng, trong khi ví dụ REQ-14 ở F2 xếp câu tương tự vào Giao tiếp ngoài. Đã áp dụng F3: hành vi (thanh toán, gửi vé qua SMS, hoàn tiền) là REQ Chức năng hoặc Quy tắc nghiệp vụ có ghi kênh ở cột Ghi chú; việc trao đổi dữ liệu với từng hệ thống, thiết bị ngoài là REQ Giao tiếp ngoài riêng (REQ-15, REQ-20, REQ-24, REQ-35). Lý do: cây quyết định F3 là quy tắc, ví dụ chỉ minh hoạ.
- Dùng trường HE_THONG_NGOAI của hồ sơ dự án làm nguồn (C1.1 xếp trường này sau mọi tài liệu nguồn) cho REQ-15, REQ-20, REQ-24, REQ-35, REQ-56 và cho mục Ngoài phạm vi, dù mục 2 của P00 chỉ nêu tài liệu trong TAI_LIEU_NGUON. Các REQ này đều có câu trích tài liệu nguồn đi kèm, nên thứ tự mã vẫn theo vị trí trong tài liệu nguồn.
- Mục 2 Phạm vi có thêm một dòng "Chưa xếp vào danh sách nào" cho chức năng cập nhật danh mục tuyến, xe, tài xế (Q-03). F4 chỉ cho danh sách thứ ba "Chờ Q-nn" khi câu phạm vi mâu thuẫn với mô tả chi tiết; trường hợp này là chỗ thiếu, không phải mâu thuẫn, nên không dùng danh sách "Chờ Q-nn" và không tạo ASM để tránh tự thêm chức năng.
- Target 7 (từ F6 trong REQ có Q): REQ-50 chứa "100%", thuộc nhóm "Tổng thể tuyệt đối" của F6, nhưng ở đây là tỉ lệ hoàn tiền xác định. Đã ghi dòng 27 ở mục 5 và gắn Q-14 (câu hỏi có sẵn về cùng REQ) thay vì tạo câu hỏi riêng không có nội dung cần hỏi.
