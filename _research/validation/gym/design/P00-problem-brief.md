# P00 - Chuẩn hoá yêu cầu - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P00 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-phong-tap.md |
| Phạm vi | Toàn hệ thống (TRONG_TAM_PHAN_TICH: Không có) |
| Mã Q, ASM cuối đã cấp | Q-43; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Bối cảnh và mục tiêu nghiệp vụ

VietFit là chuỗi phòng tập có 4 chi nhánh trong thành phố, khoảng 6.000 hội viên và 40 huấn luyện viên; mỗi chi nhánh mở khoảng 25 lớp tập nhóm mỗi ngày (yoga, aerobic, đạp xe trong nhà). Hiện việc bán gói tập được ghi bằng bảng tính và việc đặt chỗ lớp nhóm qua nhóm chat. Đặt chỗ qua nhóm chat thường quá sức chứa phòng. Lễ tân phải dò tên hội viên trên giấy khi hội viên vào cửa. VietFit cần phần mềm để thay các cách làm này.

Mục tiêu nghiệp vụ nêu trong nguồn:

- Có phần mềm quản lý hội viên, lớp tập và ra vào (nguồn: Đoạn mở đầu, câu 3). Xem Q-02 về nghĩa của "quản lý hội viên".

## 2. Phạm vi

### Trong phạm vi

- Xem bảng giá và lịch lớp không cần tài khoản; đăng ký tài khoản hội viên (REQ-06 đến REQ-08)
- Quy cách gói tập: thời hạn, loại một chi nhánh hoặc toàn chuỗi (REQ-09, REQ-10)
- Mua và gia hạn gói tập trên ứng dụng, thanh toán qua cổng thanh toán, huỷ đơn chưa thanh toán (REQ-11 đến REQ-17)
- Bán gói tại quầy: bán, thu tiền mặt, nhập mã giao dịch POS (REQ-18 đến REQ-21)
- Đặt chỗ lớp nhóm, danh sách chờ, huỷ chỗ, vắng mặt và khoá quyền đặt lớp (REQ-22 đến REQ-38)
- Vào chi nhánh qua cửa quay bằng mã QR; vé tập một ngày cho khách vãng lai (REQ-39 đến REQ-45)
- Bảo lưu gói, chuyển nhượng gói và phí chuyển nhượng (REQ-46 đến REQ-55)
- Gói buổi tập cá nhân: mua, đặt buổi, xác nhận, huỷ, ghi nhận buổi và chỉ số cơ thể, quyền xem chỉ số (REQ-56 đến REQ-68)
- Lập lịch lớp nhóm, huỷ lớp, thông báo huỷ lớp (REQ-69 đến REQ-77)
- Giá gói, khuyến mãi, báo cáo cho giám đốc chuỗi (REQ-78 đến REQ-83)
- Thông báo nhắc gia hạn; gửi thông báo qua thông báo đẩy và SMS (REQ-84 đến REQ-88)
- Trao đổi dữ liệu với cổng thanh toán, cửa quay, dịch vụ thông báo đẩy, cổng SMS, hệ thống hoá đơn điện tử (REQ-14, REQ-40, REQ-89, REQ-90, REQ-92)
- Quy mô, mở đặt chỗ và yêu cầu hiệu năng (REQ-01 đến REQ-05, REQ-93, REQ-94, REQ-95, REQ-96)

### Ngoài phạm vi

- Nghiệp vụ lập, điều chỉnh, huỷ hoá đơn điện tử (nguồn: project-profile.md, mục 4: "phần mềm chỉ gửi dữ liệu giao dịch thu tiền sang hệ thống hoá đơn điện tử")
- Việc tính thù lao huấn luyện viên (nguồn: project-profile.md, mục 4: "Việc tính thù lao huấn luyện viên làm ngoài phần mềm"; yeu-cau-phong-tap.md, Mục 9 câu 2: "để tính thù lao")
- Thao tác quẹt thẻ trên máy POS của ngân hàng (nguồn: Mục 2 câu 4: "máy POS không kết nối với phần mềm"); phần mềm chỉ nhận mã giao dịch do lễ tân nhập (REQ-21)
- Hoạt động bên trong của cổng thanh toán, cổng SMS, dịch vụ thông báo đẩy, cửa quay và hệ thống hoá đơn điện tử: là hệ thống khác, phần mềm chỉ trao đổi dữ liệu (REQ-14, REQ-90, REQ-89, REQ-40, REQ-92)

### Chờ Q-nn

Không có (không có câu nêu phạm vi mâu thuẫn với mô tả chi tiết).

## 3. Các bên liên quan và người dùng

| SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống (Có / Không / Chưa rõ) | REQ |
|---|---|---|---|---|---|
| SH-01 | Chuỗi phòng tập VietFit (tổ chức) | Chủ sở hữu, người đặt hàng | Thay cách ghi bán gói bằng bảng tính, đặt chỗ qua nhóm chat và dò tên hội viên trên giấy bằng phần mềm quản lý hội viên, lớp tập và ra vào | Không | REQ-01, REQ-02 |
| SH-02 | Hội viên (kể cả người đứng đầu danh sách chờ, người nhận chuyển nhượng gói) | Người dùng trực tiếp | Mua và gia hạn gói, đặt chỗ lớp, vào chi nhánh bằng mã QR, bảo lưu gói, mua gói buổi tập cá nhân, xem chỉ số cơ thể của mình; nhận thông báo | Có | REQ-11, REQ-22, REQ-39, REQ-46, REQ-56, REQ-68 |
| SH-03 | Huấn luyện viên | Người dùng trực tiếp | Xác nhận hoặc từ chối yêu cầu đặt buổi tập, ghi nhận buổi tập và chỉ số cơ thể; được tính thù lao qua báo cáo số buổi | Có | REQ-60, REQ-65, REQ-68, REQ-83 |
| SH-04 | Lễ tân | Người dùng trực tiếp | Bán gói, thu tiền mặt hoặc thẻ, nhập mã giao dịch POS, chuyển nhượng gói, in vé một ngày | Có | REQ-18, REQ-52, REQ-43 |
| SH-05 | Người quan tâm (người chưa có tài khoản) | Người dùng trực tiếp | Xem bảng giá và lịch lớp không cần tài khoản; đăng ký tài khoản hội viên | Có | REQ-06, REQ-07, REQ-08 |
| SH-06 | Cổng thanh toán trực tuyến của đối tác | Hệ thống hoặc thiết bị ngoài | Nhận thông tin đơn mua và trả kết quả thanh toán | Có | REQ-14 |
| SH-07 | Máy POS của ngân hàng | Hệ thống hoặc thiết bị ngoài | In hoá đơn POS có mã giao dịch; không kết nối với phần mềm | Không | REQ-21 |
| SH-08 | Cửa quay có đầu đọc mã QR (nhà cung cấp thiết bị lắp đặt) | Hệ thống hoặc thiết bị ngoài | Gửi mã QR đọc được tới phần mềm và mở cửa theo kết quả trả về, phản hồi trong 1 giây | Có | REQ-40, REQ-96 |
| SH-09 | Khách vãng lai | Người dùng trực tiếp | Mua vé tập một ngày tại quầy, dùng mã QR trên vé trong ngày tại chi nhánh đã mua | Chưa rõ | REQ-42, REQ-44, REQ-45 |
| SH-10 | Quản lý chi nhánh | Người dùng trực tiếp | Lập lịch lớp nhóm, huỷ lớp vì sự cố | Có | REQ-69, REQ-76 |
| SH-11 | Giám đốc chuỗi | Người dùng trực tiếp | Đặt giá gói và khuyến mãi, xem báo cáo doanh thu, tỉ lệ lấp đầy, số buổi tập cá nhân | Có | REQ-78, REQ-79, REQ-81 |
| SH-12 | Dịch vụ thông báo đẩy của nền tảng di động | Hệ thống hoặc thiết bị ngoài | Chuyển thông báo đẩy tới ứng dụng của hội viên | Có | REQ-89 |
| SH-13 | Cổng SMS của nhà mạng | Hệ thống hoặc thiết bị ngoài | Chuyển SMS tới hội viên chưa cài ứng dụng | Có | REQ-90 |
| SH-14 | Hệ thống hoá đơn điện tử của đơn vị cung cấp | Hệ thống hoặc thiết bị ngoài | Nhận dữ liệu giao dịch thu tiền để xuất hoá đơn điện tử | Có | REQ-92 |

## 4. Danh sách yêu cầu

| REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |
|---|---|---|---|---|
| REQ-01 | Hệ thống quản lý 4 chi nhánh trong thành phố. | Dữ liệu | "Chuỗi phòng tập VietFit có 4 chi nhánh trong thành phố" (Đoạn mở đầu, câu 1) | Số liệu quy mô. Q: Q-03 |
| REQ-02 | Hệ thống quản lý khoảng 6.000 hội viên. | Dữ liệu | "khoảng 6.000 hội viên" (Đoạn mở đầu, câu 1) | Số liệu quy mô, tách từ cùng câu với REQ-01 |
| REQ-03 | Hệ thống quản lý 40 huấn luyện viên. | Dữ liệu | "40 huấn luyện viên" (Đoạn mở đầu, câu 1) | Số liệu quy mô, tách từ cùng câu với REQ-01. Q: Q-05 |
| REQ-04 | Mỗi chi nhánh mở khoảng 25 lớp tập nhóm mỗi ngày. | Dữ liệu | "mỗi chi nhánh mở khoảng 25 lớp tập nhóm mỗi ngày" (Đoạn mở đầu, câu 1) | Số liệu quy mô, tách từ cùng câu với REQ-01 |
| REQ-05 | Lớp tập nhóm gồm các loại yoga, aerobic, đạp xe trong nhà. | Dữ liệu | "(yoga, aerobic, đạp xe trong nhà)" (Đoạn mở đầu, câu 1) | Nguồn đặt trong ngoặc đơn, chưa rõ là danh sách đóng. Q: Q-04 |
| REQ-06 | Người quan tâm có thể xem bảng giá gói tập trên ứng dụng di động mà không cần tài khoản. | Chức năng | "Người quan tâm xem bảng giá gói tập và lịch lớp nhóm trên ứng dụng di động mà không cần tài khoản." (Mục 1, câu 1) | Tách từ cùng câu với REQ-07 vì hai đối tượng xem độc lập |
| REQ-07 | Người quan tâm có thể xem lịch lớp nhóm trên ứng dụng di động mà không cần tài khoản. | Chức năng | "Người quan tâm xem bảng giá gói tập và lịch lớp nhóm trên ứng dụng di động mà không cần tài khoản." (Mục 1, câu 1) | Tách từ cùng câu với REQ-06 |
| REQ-08 | Người quan tâm có thể đăng ký tài khoản hội viên bằng số điện thoại và họ tên. | Chức năng | "Để mua gói hoặc đặt lớp, người đó đăng ký tài khoản hội viên bằng số điện thoại và họ tên." (Mục 1, câu 2) | Vai trò có tài khoản hội viên là điều kiện để mua gói và đặt lớp, đã ghi vào chủ thể "Hội viên" của REQ-11, REQ-12, REQ-22. Q: Q-01, Q-36 |
| REQ-09 | Gói tập có thời hạn 1, 3, 6 hoặc 12 tháng. | Quy tắc nghiệp vụ | "Gói tập có thời hạn 1, 3, 6 hoặc 12 tháng, loại một chi nhánh hoặc toàn chuỗi." (Mục 1, câu 3) | Tách từ cùng câu với REQ-10 |
| REQ-10 | Gói tập thuộc một trong hai loại: áp dụng cho một chi nhánh, hoặc áp dụng cho toàn chuỗi. | Quy tắc nghiệp vụ | "Gói tập có thời hạn 1, 3, 6 hoặc 12 tháng, loại một chi nhánh hoặc toàn chuỗi." (Mục 1, câu 3) | Tách từ cùng câu với REQ-09 |
| REQ-11 | Hội viên có thể mua gói tập trên ứng dụng. | Chức năng | "Hội viên mua hoặc gia hạn gói tập trên ứng dụng và thanh toán qua cổng thanh toán trực tuyến của đối tác." (Mục 2, câu 1) | Tách từ cùng câu với REQ-12, REQ-13. Q: Q-13 |
| REQ-12 | Hội viên có thể gia hạn gói tập trên ứng dụng. | Chức năng | "Hội viên mua hoặc gia hạn gói tập trên ứng dụng và thanh toán qua cổng thanh toán trực tuyến của đối tác." (Mục 2, câu 1) | Tách từ cùng câu với REQ-11. Quy tắc ngày bắt đầu gói mới ở REQ-17 |
| REQ-13 | Hội viên có thể thanh toán đơn mua hoặc đơn gia hạn gói tập qua cổng thanh toán trực tuyến của đối tác. | Chức năng | "Hội viên mua hoặc gia hạn gói tập trên ứng dụng và thanh toán qua cổng thanh toán trực tuyến của đối tác." (Mục 2, câu 1) | Kênh: cổng thanh toán (REQ-14). Tách từ cùng câu với REQ-11. Xem Q-13, Q-14 về thanh toán thất bại |
| REQ-14 | Hệ thống trao đổi thông tin đơn mua và kết quả thanh toán với cổng thanh toán trực tuyến của đối tác để thu tiền đơn mua gói tập. | Giao tiếp ngoài | "thanh toán qua cổng thanh toán trực tuyến của đối tác" (Mục 2, câu 1)<br>"Cổng thanh toán trực tuyến của đối tác (API REST, có tài liệu API thanh toán và tra cứu giao dịch)" (project-profile.md, HE_THONG_NGOAI) | Tách từ cùng câu với REQ-13. Hồ sơ ghi có tài liệu API thanh toán và tra cứu giao dịch |
| REQ-15 | Hệ thống huỷ đơn mua gói tập chưa thanh toán thành công. | Chức năng | "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ." (Mục 2, câu 2) | Chủ thể "Hệ thống" suy từ việc nguồn dùng câu bị động và không có thao tác của người. Ngưỡng ở REQ-16. Q: Q-43 |
| REQ-16 | Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ. | Quy tắc nghiệp vụ | "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ." (Mục 2, câu 2) | Tách từ cùng câu với REQ-15. Q: Q-25, Q-13, Q-14 |
| REQ-17 | Khi hội viên gia hạn lúc gói cũ còn hiệu lực, gói mới bắt đầu ngay sau ngày hết hạn của gói cũ. | Quy tắc nghiệp vụ | "Gia hạn khi gói cũ còn hiệu lực thì gói mới bắt đầu ngay sau ngày hết hạn của gói cũ." (Mục 2, câu 3) | Nguồn chỉ nêu nhánh gói cũ còn hiệu lực. Q: Q-24 |
| REQ-18 | Lễ tân có thể bán gói tập tại quầy. | Chức năng | "Lễ tân cũng bán gói tại quầy, thu tiền mặt hoặc quẹt thẻ ngân hàng qua máy POS của ngân hàng (...)" (Mục 2, câu 4) | Tách từ cùng câu với REQ-19, REQ-20, REQ-21. Q: Q-01 |
| REQ-19 | Lễ tân có thể thu tiền mặt khi bán gói tập tại quầy. | Chức năng | "Lễ tân cũng bán gói tại quầy, thu tiền mặt hoặc quẹt thẻ ngân hàng qua máy POS của ngân hàng (...)" (Mục 2, câu 4) | Tách từ cùng câu với REQ-18 |
| REQ-20 | Lễ tân có thể nhập mã giao dịch in trên hoá đơn POS vào hệ thống khi bán gói tập tại quầy và thu tiền bằng thẻ ngân hàng qua máy POS của ngân hàng. | Chức năng | "... quẹt thẻ ngân hàng qua máy POS của ngân hàng (máy POS không kết nối với phần mềm, lễ tân nhập mã giao dịch in trên hoá đơn POS)" (Mục 2, câu 4) | Kênh: máy POS (REQ-21). Việc quẹt thẻ diễn ra trên máy POS, ngoài hệ thống. Tách từ cùng câu với REQ-18 |
| REQ-21 | Hệ thống nhận mã giao dịch của máy POS ngân hàng do lễ tân nhập tay, không có kết nối trực tiếp với máy POS. | Giao tiếp ngoài | "máy POS không kết nối với phần mềm, lễ tân nhập mã giao dịch in trên hoá đơn POS" (Mục 2, câu 4) | Máy POS không có trong HE_THONG_NGOAI của hồ sơ. Tách từ cùng câu với REQ-20 |
| REQ-22 | Hội viên có thể đặt chỗ lớp nhóm trên ứng dụng. | Chức năng | "Hội viên đặt chỗ lớp nhóm trên ứng dụng, sớm nhất 7 ngày trước giờ học, tối đa 2 lớp trong một ngày." (Mục 3, câu 1) | Tách từ cùng câu với REQ-23, REQ-24. Q: Q-12, Q-11 |
| REQ-23 | Hội viên được đặt chỗ lớp nhóm sớm nhất 7 ngày trước giờ học. | Quy tắc nghiệp vụ | "Hội viên đặt chỗ lớp nhóm trên ứng dụng, sớm nhất 7 ngày trước giờ học, tối đa 2 lớp trong một ngày." (Mục 3, câu 1) | Mâu thuẫn với REQ-93. Q: Q-11 |
| REQ-24 | Hội viên được đặt chỗ tối đa 2 lớp trong một ngày. | Quy tắc nghiệp vụ | "Hội viên đặt chỗ lớp nhóm trên ứng dụng, sớm nhất 7 ngày trước giờ học, tối đa 2 lớp trong một ngày." (Mục 3, câu 1) | Tách từ cùng câu với REQ-22 |
| REQ-25 | Sức chứa của mỗi lớp nhóm được xác định theo phòng. | Quy tắc nghiệp vụ | "Mỗi lớp có sức chứa theo phòng." (Mục 3, câu 2) | Chưa rõ sức chứa lớp bằng hay thấp hơn sức chứa phòng. Q: Q-03 |
| REQ-26 | Hội viên có thể vào danh sách chờ của lớp nhóm đã đủ chỗ. | Chức năng | "Lớp đã đủ chỗ thì hội viên được vào danh sách chờ." (Mục 3, câu 3) | Không có |
| REQ-27 | Hệ thống gửi thông báo cho hội viên đứng đầu danh sách chờ của lớp nhóm khi có người huỷ chỗ. | Chức năng | "Khi có người huỷ, hệ thống gửi thông báo cho người đứng đầu danh sách chờ" (Mục 3, câu 4) | Kênh: thông báo đẩy và SMS (REQ-87, REQ-88). Tách từ cùng câu với REQ-28, REQ-29, REQ-30 |
| REQ-28 | Hội viên được thông báo có thể xem lại lớp và xác nhận nhận chỗ trên ứng dụng. | Chức năng | "người đó có 30 phút để mở ứng dụng, xem lại lớp và xác nhận nhận chỗ" (Mục 3, câu 4) | Không tách các bước mở ứng dụng, xem lớp vì từng bước không có giá trị nghiệp vụ riêng. Q: Q-22 |
| REQ-29 | Hội viên đứng đầu danh sách chờ được thông báo có 30 phút để xác nhận nhận chỗ. | Quy tắc nghiệp vụ | "người đó có 30 phút để mở ứng dụng, xem lại lớp và xác nhận nhận chỗ" (Mục 3, câu 4) | Tách từ cùng câu với REQ-28 |
| REQ-30 | Hệ thống chuyển chỗ cho hội viên kế tiếp trong danh sách chờ khi hội viên được thông báo không xác nhận nhận chỗ đúng thời hạn. | Chức năng | "quá 30 phút thì chỗ chuyển cho người kế tiếp" (Mục 3, câu 4) | Chủ thể "Hệ thống" suy từ câu bị động. Q: Q-23, Q-43 |
| REQ-31 | Hệ thống không chuyển chỗ từ danh sách chờ khi còn dưới 1 giờ trước giờ học. | Quy tắc nghiệp vụ | "Không chuyển chỗ từ danh sách chờ khi còn dưới 1 giờ trước giờ học." (Mục 3, câu 5) | Không có |
| REQ-32 | Hội viên có thể huỷ chỗ lớp nhóm đã đặt. | Chức năng | "Hội viên huỷ chỗ đã đặt chậm nhất 2 giờ trước giờ học." (Mục 4, câu 1) | Tách từ cùng câu với REQ-33 |
| REQ-33 | Hội viên huỷ chỗ đã đặt chậm nhất 2 giờ trước giờ học. | Quy tắc nghiệp vụ | "Hội viên huỷ chỗ đã đặt chậm nhất 2 giờ trước giờ học." (Mục 4, câu 1) | Tách từ cùng câu với REQ-32 |
| REQ-34 | Hệ thống tính một lần vắng mặt cho hội viên đã đặt chỗ mà không vào lớp. | Chức năng | "Hội viên đặt chỗ mà không vào lớp (...) bị tính một lần vắng mặt" (Mục 4, câu 2) | Điều kiện "không vào lớp" ở REQ-35. Chủ thể "Hệ thống" suy từ câu bị động. Q: Q-43 |
| REQ-35 | Hội viên đặt chỗ được xem là không vào lớp khi không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu. | Quy tắc nghiệp vụ | "(không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu)" (Mục 4, câu 2) | Tách từ cùng câu với REQ-34. Cửa quay: REQ-40 |
| REQ-36 | Hệ thống khoá quyền đặt lớp của hội viên khi số lần vắng mặt của hội viên đạt ngưỡng. | Chức năng | "3 lần vắng mặt trong 30 ngày thì bị khoá quyền đặt lớp 7 ngày." (Mục 4, câu 2) | Ngưỡng ở REQ-37, thời gian khoá ở REQ-38. Chủ thể "Hệ thống" suy từ câu bị động. Q: Q-20, Q-21, Q-43 |
| REQ-37 | Ngưỡng vắng mặt dẫn tới khoá quyền đặt lớp là 3 lần trong 30 ngày. | Quy tắc nghiệp vụ | "3 lần vắng mặt trong 30 ngày thì bị khoá quyền đặt lớp 7 ngày." (Mục 4, câu 2) | Tách từ cùng câu với REQ-36, REQ-38 |
| REQ-38 | Quyền đặt lớp của hội viên bị khoá trong 7 ngày. | Quy tắc nghiệp vụ | "3 lần vắng mặt trong 30 ngày thì bị khoá quyền đặt lớp 7 ngày." (Mục 4, câu 2) | Tách từ cùng câu với REQ-36, REQ-37 |
| REQ-39 | Hội viên có thể vào chi nhánh qua cửa quay bằng mã QR hiển thị trên ứng dụng. | Chức năng | "Hội viên vào chi nhánh qua cửa quay bằng mã QR hiển thị trên ứng dụng." (Mục 5, câu 1) | Kênh: cửa quay (REQ-40) |
| REQ-40 | Hệ thống trao đổi mã QR đọc được và kết quả cho phép vào với cửa quay có đầu đọc mã QR tại mỗi chi nhánh để mở cửa. | Giao tiếp ngoài | "Cửa quay hỏi phần mềm" (Mục 5, câu 2)<br>"Cửa quay có đầu đọc mã QR tại mỗi chi nhánh, do nhà cung cấp thiết bị lắp đặt, gửi mã QR đọc được tới phần mềm qua API và mở cửa theo kết quả trả về" (project-profile.md, HE_THONG_NGOAI) | Hồ sơ không ghi tài liệu API của cửa quay. Q: Q-41 |
| REQ-41 | Hệ thống cho phép cửa quay mở cho hội viên chỉ khi gói tập của hội viên còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh đó. | Chức năng | "Cửa quay hỏi phần mềm và chỉ mở khi gói tập còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh đó." (Mục 5, câu 2) | Kênh: cửa quay (REQ-40). Điều kiện trạng thái giữ chung với hành động. Q: Q-18, Q-40 |
| REQ-42 | Khách vãng lai có thể mua vé tập một ngày tại quầy. | Chức năng | "Khách vãng lai mua vé tập một ngày tại quầy; lễ tân in vé có mã QR dùng được trong ngày tại chi nhánh đã mua." (Mục 5, câu 3) | Q: Q-08, Q-38 |
| REQ-43 | Lễ tân có thể in vé tập một ngày có mã QR cho khách vãng lai. | Chức năng | "Khách vãng lai mua vé tập một ngày tại quầy; lễ tân in vé có mã QR dùng được trong ngày tại chi nhánh đã mua." (Mục 5, câu 3) | Tách từ cùng câu với REQ-42 |
| REQ-44 | Mã QR trên vé tập một ngày dùng được trong ngày mua vé. | Quy tắc nghiệp vụ | "lễ tân in vé có mã QR dùng được trong ngày tại chi nhánh đã mua" (Mục 5, câu 3) | Tách từ cùng câu với REQ-45. Q: Q-40 |
| REQ-45 | Mã QR trên vé tập một ngày dùng được tại chi nhánh đã mua vé. | Quy tắc nghiệp vụ | "lễ tân in vé có mã QR dùng được trong ngày tại chi nhánh đã mua" (Mục 5, câu 3) | Tách từ cùng câu với REQ-44 |
| REQ-46 | Hội viên có thể bảo lưu gói tập. | Chức năng | "Hội viên có gói từ 3 tháng trở lên được bảo lưu gói một lần cho mỗi gói, từ 7 đến 30 ngày, đăng ký trước ngày bắt đầu bảo lưu ít nhất 1 ngày." (Mục 6, câu 1) | Điều kiện định lượng tách thành REQ-47 đến REQ-50. Q: Q-17, Q-19 |
| REQ-47 | Hội viên có gói từ 3 tháng trở lên được bảo lưu gói. | Quy tắc nghiệp vụ | "Hội viên có gói từ 3 tháng trở lên được bảo lưu gói" (Mục 6, câu 1) | Tách từ cùng câu với REQ-46. Q: Q-17 |
| REQ-48 | Mỗi gói được bảo lưu một lần. | Quy tắc nghiệp vụ | "được bảo lưu gói một lần cho mỗi gói" (Mục 6, câu 1) | Tách từ cùng câu với REQ-46 |
| REQ-49 | Thời gian bảo lưu của một lần bảo lưu từ 7 đến 30 ngày. | Quy tắc nghiệp vụ | "từ 7 đến 30 ngày" (Mục 6, câu 1) | Tách từ cùng câu với REQ-46 |
| REQ-50 | Hội viên đăng ký bảo lưu trước ngày bắt đầu bảo lưu ít nhất 1 ngày. | Quy tắc nghiệp vụ | "đăng ký trước ngày bắt đầu bảo lưu ít nhất 1 ngày" (Mục 6, câu 1) | Tách từ cùng câu với REQ-46 |
| REQ-51 | Ngày hết hạn của gói được lùi thêm đúng số ngày bảo lưu. | Quy tắc nghiệp vụ | "Ngày hết hạn của gói được lùi thêm đúng số ngày bảo lưu." (Mục 6, câu 2) | Không có |
| REQ-52 | Lễ tân có thể chuyển nhượng gói tập của hội viên cho người khác đã có tài khoản tại quầy khi có mặt cả hai người. | Chức năng | "Hội viên được chuyển nhượng gói còn ít nhất 30 ngày cho người khác đã có tài khoản; lễ tân thực hiện chuyển nhượng tại quầy khi có mặt cả hai người" (Mục 6, câu 3) | Gộp hai vế của nguồn (hội viên chuyển nhượng, lễ tân thực hiện) thành một chức năng vì cùng một hành vi. Chủ thể là lễ tân vì nguồn nêu lễ tân thực hiện. Điều kiện "đã có tài khoản" giữ chung với hành động. Q: Q-17 |
| REQ-53 | Gói được chuyển nhượng khi còn ít nhất 30 ngày. | Quy tắc nghiệp vụ | "Hội viên được chuyển nhượng gói còn ít nhất 30 ngày" (Mục 6, câu 3) | Tách từ cùng câu với REQ-52 |
| REQ-54 | Lễ tân thu phí chuyển nhượng khi thực hiện chuyển nhượng gói tập. | Chức năng | "... và thu phí chuyển nhượng 200.000 đồng." (Mục 6, câu 3) | Q: Q-38 |
| REQ-55 | Phí chuyển nhượng gói tập là 200.000 đồng. | Quy tắc nghiệp vụ | "thu phí chuyển nhượng 200.000 đồng" (Mục 6, câu 3) | Tách từ cùng câu với REQ-54 |
| REQ-56 | Hội viên có thể mua gói buổi tập cá nhân với một huấn luyện viên. | Chức năng | "Hội viên mua gói buổi tập cá nhân (10 hoặc 20 buổi, dùng trong 90 ngày) với một huấn luyện viên." (Mục 7, câu 1) | Q: Q-07, Q-08 |
| REQ-57 | Gói buổi tập cá nhân có 10 buổi hoặc 20 buổi. | Quy tắc nghiệp vụ | "(10 hoặc 20 buổi, dùng trong 90 ngày)" (Mục 7, câu 1) | Tách từ cùng câu với REQ-56 |
| REQ-58 | Gói buổi tập cá nhân dùng trong 90 ngày. | Quy tắc nghiệp vụ | "(10 hoặc 20 buổi, dùng trong 90 ngày)" (Mục 7, câu 1) | Tách từ cùng câu với REQ-56. Q: Q-26 |
| REQ-59 | Hội viên có thể đặt buổi tập cá nhân bằng cách chọn khung giờ trống trong lịch làm việc của huấn luyện viên. | Chức năng | "Hội viên chọn khung giờ trống trong lịch làm việc của huấn luyện viên để đặt buổi tập" (Mục 7, câu 2) | Q: Q-06, Q-32 |
| REQ-60 | Huấn luyện viên có thể xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân. | Chức năng | "huấn luyện viên xác nhận hoặc từ chối trong 12 giờ" (Mục 7, câu 2) | Chưa tách xác nhận và từ chối vì nguồn không phân biệt. Q: Q-15, Q-30 |
| REQ-61 | Huấn luyện viên xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân trong 12 giờ. | Quy tắc nghiệp vụ | "huấn luyện viên xác nhận hoặc từ chối trong 12 giờ" (Mục 7, câu 2) | Tách từ cùng câu với REQ-60. Nguồn không nêu mốc bắt đầu 12 giờ |
| REQ-62 | Hệ thống tự huỷ yêu cầu đặt buổi tập cá nhân mà huấn luyện viên chưa xác nhận hoặc từ chối khi quá hạn. | Chức năng | "quá hạn thì yêu cầu tự huỷ" (Mục 7, câu 2) | Hạn là REQ-61. Q: Q-30, Q-15 |
| REQ-63 | Hội viên có thể huỷ buổi tập cá nhân đã đặt. | Chức năng | "Hội viên huỷ buổi trước 12 giờ thì không bị trừ buổi." (Mục 7, câu 3) | Nguồn không nêu riêng chức năng huỷ buổi; chức năng này là hành động mà câu quy tắc áp dụng. Q: Q-28, Q-19 |
| REQ-64 | Hội viên huỷ buổi tập cá nhân trước 12 giờ thì không bị trừ buổi. | Quy tắc nghiệp vụ | "Hội viên huỷ buổi trước 12 giờ thì không bị trừ buổi." (Mục 7, câu 3) | Giữ nguyên "trước 12 giờ" của nguồn. Q: Q-27, Q-28, Q-29 |
| REQ-65 | Huấn luyện viên có thể ghi nhận buổi tập cá nhân sau mỗi buổi. | Chức năng | "Sau mỗi buổi, huấn luyện viên ghi nhận buổi tập và chỉ số cơ thể của hội viên (cân nặng, tỉ lệ mỡ)" (Mục 7, câu 4) | Tách từ cùng câu với REQ-66. Q: Q-31, Q-29 |
| REQ-66 | Huấn luyện viên có thể ghi nhận chỉ số cơ thể của hội viên sau mỗi buổi tập cá nhân. | Chức năng | "Sau mỗi buổi, huấn luyện viên ghi nhận buổi tập và chỉ số cơ thể của hội viên (cân nặng, tỉ lệ mỡ)" (Mục 7, câu 4) | Tách từ cùng câu với REQ-65 |
| REQ-67 | Chỉ số cơ thể của hội viên gồm cân nặng và tỉ lệ mỡ. | Dữ liệu | "chỉ số cơ thể của hội viên (cân nặng, tỉ lệ mỡ)" (Mục 7, câu 4) | Tách từ cùng câu với REQ-66 |
| REQ-68 | Chỉ hội viên đó và huấn luyện viên phụ trách có thể xem chỉ số cơ thể của hội viên. | Chức năng | "chỉ hội viên đó và huấn luyện viên phụ trách được xem các chỉ số này." (Mục 7, câu 4) | Vai trò được xem ghi vào chủ thể theo F3, không tách REQ Phi chức năng riêng. Nếu coi là yêu cầu bảo mật thì chuyển loại Phi chức năng |
| REQ-69 | Quản lý chi nhánh có thể lập lịch lớp nhóm hằng tuần. | Chức năng | "Quản lý chi nhánh lập lịch lớp nhóm hằng tuần: chọn loại lớp, phòng, huấn luyện viên và giờ." (Mục 8, câu 1) | Tách từ cùng câu với REQ-70. Q: Q-16, Q-03, Q-04 |
| REQ-70 | Lịch lớp nhóm gồm loại lớp, phòng, huấn luyện viên và giờ. | Dữ liệu | "chọn loại lớp, phòng, huấn luyện viên và giờ" (Mục 8, câu 1) | Tách từ cùng câu với REQ-69. Q: Q-32 |
| REQ-71 | Một phòng không được xếp hai lớp trùng giờ. | Quy tắc nghiệp vụ | "Một phòng hoặc một huấn luyện viên không được xếp hai lớp trùng giờ." (Mục 8, câu 2) | Tách từ cùng câu với REQ-72. Q: Q-32 |
| REQ-72 | Một huấn luyện viên không được xếp hai lớp trùng giờ. | Quy tắc nghiệp vụ | "Một phòng hoặc một huấn luyện viên không được xếp hai lớp trùng giờ." (Mục 8, câu 2) | Tách từ cùng câu với REQ-71. Q: Q-32 |
| REQ-73 | Hệ thống tự huỷ lớp nhóm khi số người đặt chỗ thấp hơn ngưỡng quy định. | Chức năng | "Lớp có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học thì hệ thống tự huỷ lớp và gửi thông báo cho những người đã đặt." (Mục 8, câu 3) | Ngưỡng ở REQ-74. Tách từ cùng câu với REQ-75 |
| REQ-74 | Lớp nhóm có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học thì bị huỷ. | Quy tắc nghiệp vụ | "Lớp có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học thì hệ thống tự huỷ lớp" (Mục 8, câu 3) | Tách từ cùng câu với REQ-73 |
| REQ-75 | Hệ thống gửi thông báo cho những người đã đặt chỗ của lớp nhóm bị tự huỷ. | Chức năng | "gửi thông báo cho những người đã đặt" (Mục 8, câu 3) | Kênh: thông báo đẩy và SMS (REQ-87, REQ-88). Tách từ cùng câu với REQ-73 |
| REQ-76 | Quản lý chi nhánh có thể huỷ lớp nhóm vì sự cố. | Chức năng | "Quản lý chi nhánh cũng có thể huỷ lớp vì sự cố" (Mục 8, câu 4) | Tách từ cùng câu với REQ-77 |
| REQ-77 | Hệ thống gửi thông báo cho những người đã đặt chỗ và những người trong danh sách chờ khi quản lý chi nhánh huỷ lớp nhóm. | Chức năng | "khi đó hệ thống gửi thông báo cho mọi người đã đặt và người trong danh sách chờ" (Mục 8, câu 4) | Kênh: thông báo đẩy và SMS (REQ-87, REQ-88). Tách từ cùng câu với REQ-76. "Mọi" của nguồn chỉ tập người nhận, không phải khẳng định độ tin cậy |
| REQ-78 | Giám đốc chuỗi có thể đặt giá các gói. | Chức năng | "Giám đốc chuỗi đặt giá các gói và chương trình khuyến mãi theo khoảng ngày, giảm tối đa 20% giá gói." (Mục 9, câu 1) | Tách từ cùng câu với REQ-79. Q: Q-08, Q-10 |
| REQ-79 | Giám đốc chuỗi có thể đặt chương trình khuyến mãi theo khoảng ngày. | Chức năng | "Giám đốc chuỗi đặt giá các gói và chương trình khuyến mãi theo khoảng ngày, giảm tối đa 20% giá gói." (Mục 9, câu 1) | Tách từ cùng câu với REQ-78. Q: Q-09, Q-10, Q-08 |
| REQ-80 | Chương trình khuyến mãi giảm tối đa 20% giá gói. | Quy tắc nghiệp vụ | "giảm tối đa 20% giá gói" (Mục 9, câu 1) | Tách từ cùng câu với REQ-79 |
| REQ-81 | Giám đốc chuỗi có thể xem báo cáo doanh thu theo chi nhánh và theo tháng. | Chức năng | "Giám đốc chuỗi xem báo cáo doanh thu theo chi nhánh và theo tháng, tỉ lệ lấp đầy lớp nhóm, và số buổi tập cá nhân của từng huấn luyện viên để tính thù lao." (Mục 9, câu 2) | Chưa tách theo chi nhánh và theo tháng vì nguồn không phân biệt. Tách từ cùng câu với REQ-82, REQ-83 |
| REQ-82 | Giám đốc chuỗi có thể xem báo cáo tỉ lệ lấp đầy lớp nhóm. | Chức năng | "... tỉ lệ lấp đầy lớp nhóm ..." (Mục 9, câu 2) | Tách từ cùng câu với REQ-81. Q: Q-33 |
| REQ-83 | Giám đốc chuỗi có thể xem báo cáo số buổi tập cá nhân của từng huấn luyện viên. | Chức năng | "... số buổi tập cá nhân của từng huấn luyện viên để tính thù lao." (Mục 9, câu 2) | Việc tính thù lao ngoài phạm vi (project-profile.md, mục 4). Tách từ cùng câu với REQ-81. Q: Q-34 |
| REQ-84 | Hệ thống gửi thông báo nhắc gia hạn cho hội viên có gói sắp hết hạn. | Chức năng | "Mỗi ngày lúc 8 giờ sáng, hệ thống gửi thông báo nhắc gia hạn cho hội viên có gói hết hạn trong 7 ngày tới." (Mục 9, câu 3) | Kênh: thông báo đẩy và SMS (REQ-87, REQ-88). "Sắp hết hạn" được định nghĩa bởi REQ-85. Q: Q-35 |
| REQ-85 | Thông báo nhắc gia hạn được gửi cho hội viên có gói hết hạn trong 7 ngày tới. | Quy tắc nghiệp vụ | "hội viên có gói hết hạn trong 7 ngày tới" (Mục 9, câu 3) | Tách từ cùng câu với REQ-84 |
| REQ-86 | Thông báo nhắc gia hạn được gửi mỗi ngày lúc 8 giờ sáng. | Quy tắc nghiệp vụ | "Mỗi ngày lúc 8 giờ sáng" (Mục 9, câu 3) | Tách từ cùng câu với REQ-84 |
| REQ-87 | Hệ thống gửi thông báo cho hội viên qua thông báo đẩy của ứng dụng. | Chức năng | "Thông báo cho hội viên gửi qua thông báo đẩy của ứng dụng" (Mục 10, câu 1) | Kênh: dịch vụ thông báo đẩy (REQ-89). Nội dung thông báo ở các REQ REQ-27, REQ-75, REQ-77, REQ-84. Q: Q-15 |
| REQ-88 | Hệ thống gửi thông báo cho hội viên chưa cài ứng dụng qua SMS. | Chức năng | "hội viên chưa cài ứng dụng thì nhận SMS qua cổng SMS của nhà mạng" (Mục 10, câu 1) | Kênh: cổng SMS (REQ-90). Q: Q-36 |
| REQ-89 | Hệ thống trao đổi nội dung thông báo với dịch vụ thông báo đẩy của nền tảng di động để gửi thông báo đẩy tới ứng dụng của hội viên. | Giao tiếp ngoài | "gửi qua thông báo đẩy của ứng dụng" (Mục 10, câu 1)<br>"Dịch vụ thông báo đẩy của nền tảng di động" (project-profile.md, HE_THONG_NGOAI) | Không có |
| REQ-90 | Hệ thống trao đổi nội dung tin nhắn với cổng SMS của nhà mạng để gửi SMS tới hội viên. | Giao tiếp ngoài | "nhận SMS qua cổng SMS của nhà mạng" (Mục 10, câu 1)<br>"Cổng SMS của nhà mạng (API REST)" (project-profile.md, HE_THONG_NGOAI) | Không có |
| REQ-91 | Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử. | Quy tắc nghiệp vụ | "Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử qua hệ thống hoá đơn điện tử của đơn vị cung cấp." (Mục 10, câu 2) | Từ "Mọi" thuộc F6. Kênh: hệ thống hoá đơn điện tử (REQ-92). Q: Q-37 |
| REQ-92 | Hệ thống trao đổi dữ liệu giao dịch thu tiền với hệ thống hoá đơn điện tử của đơn vị cung cấp để xuất hoá đơn điện tử. | Giao tiếp ngoài | "qua hệ thống hoá đơn điện tử của đơn vị cung cấp" (Mục 10, câu 2)<br>"Hệ thống hoá đơn điện tử của đơn vị cung cấp (API REST, chưa có tài liệu API)" (project-profile.md, HE_THONG_NGOAI) | Phạm vi phần mềm chỉ gửi dữ liệu giao dịch; lập, điều chỉnh, huỷ hoá đơn ngoài phạm vi (project-profile.md, mục 4). Chưa có tài liệu API. Q: Q-39 |
| REQ-93 | Đặt chỗ lớp nhóm cho tuần mới mở lúc 6 giờ sáng thứ Hai. | Quy tắc nghiệp vụ | "Lúc 6 giờ sáng thứ Hai, khi mở đặt lớp cho tuần mới" (Mục 10, câu 3) | Mâu thuẫn với REQ-23. Q: Q-11 |
| REQ-94 | Hệ thống phục vụ tới 1.500 hội viên đặt chỗ lớp nhóm cùng lúc khi mở đặt lớp cho tuần mới lúc 6 giờ sáng thứ Hai. | Phi chức năng | "có thể có tới 1.500 hội viên đặt chỗ cùng lúc" (Mục 10, câu 3) | Q: Q-42 |
| REQ-95 | Số chỗ đã đặt của một lớp nhóm không được vượt sức chứa. | Quy tắc nghiệp vụ | "không được để số chỗ đã đặt của một lớp vượt sức chứa." (Mục 10, câu 3) | Áp dụng cả khi có REQ-94 đặt chỗ cùng lúc |
| REQ-96 | Cửa quay phải phản hồi trong vòng 1 giây. | Phi chức năng | "Cửa quay phải phản hồi trong vòng 1 giây." (Mục 10, câu 4) | Giữ nguyên chủ thể "Cửa quay" của nguồn. Kênh: REQ-40. Q: Q-41 |

## 5. Vấn đề chất lượng của tài liệu nguồn

| STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
|---|---|---|---|---|---|
| 1 | Mâu thuẫn | REQ-23, REQ-93 | Mục 3 câu 1: "sớm nhất 7 ngày trước giờ học"; Mục 10 câu 3: "Lúc 6 giờ sáng thứ Hai, khi mở đặt lớp cho tuần mới" | Giữ cả hai REQ, không tự chọn. Cả hai nằm trong cùng tài liệu nguồn nên không có ưu tiên | Q-11 |
| 2 | Mâu thuẫn | REQ-41, REQ-44, REQ-45 | Mục 5 câu 2: "chỉ mở khi gói tập còn hiệu lực ..."; Mục 5 câu 3: "vé có mã QR dùng được trong ngày tại chi nhánh đã mua" | Không mâu thuẫn, tách thành hai REQ theo đối tượng (hội viên có gói, khách vãng lai có vé). Không tạo Q cho cặp này | Không có |
| 3 | Mơ hồ | REQ-96 | "Cửa quay phải phản hồi trong vòng 1 giây." | Giữ nguyên chủ thể của nguồn; hỏi mốc đo | Q-41 |
| 4 | Không kiểm chứng được | REQ-94 | "có thể có tới 1.500 hội viên đặt chỗ cùng lúc" | Giữ nguyên; thiếu ngưỡng đo thời gian phản hồi và nghĩa của "cùng lúc" | Q-42 |
| 5 | Mơ hồ | REQ-91 | "Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử" (từ "Mọi" thuộc nhóm tổng thể tuyệt đối) | Giữ nguyên từ "Mọi"; hỏi phạm vi giao dịch và ngoại lệ | Q-37 |
| 6 | Mơ hồ | REQ-15, REQ-30, REQ-34, REQ-36 | "bị huỷ" (Mục 2 câu 2); "chỗ chuyển cho người kế tiếp" (Mục 3 câu 4); "bị tính một lần vắng mặt", "bị khoá quyền đặt lớp" (Mục 4 câu 2): câu bị động không có chủ thể | Ghi chủ thể "Hệ thống" ở Nội dung chuẩn hoá vì không có thao tác của người; hỏi xác nhận | Q-43 |
| 7 | Mơ hồ | REQ-16 | "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ." | Giữ nguyên; không nêu mốc bắt đầu và phạm vi đơn | Q-25 |
| 8 | Thiếu | REQ-13, REQ-16 | "thanh toán qua cổng thanh toán trực tuyến của đối tác" (Mục 2 câu 1); nguồn không nêu thanh toán thất bại hoặc kết quả đến muộn | Không tự điền; hỏi để bước sau viết luồng ngoại lệ | Q-13, Q-14 |
| 9 | Thiếu | REQ-17 | "Gia hạn khi gói cũ còn hiệu lực thì gói mới bắt đầu ngay sau ngày hết hạn của gói cũ." (quy tắc chỉ nêu cho một nhánh) | Không tự điền nhánh gói cũ đã hết hạn | Q-24 |
| 10 | Mơ hồ | REQ-58 | "dùng trong 90 ngày" | Giữ nguyên; không nêu mốc bắt đầu | Q-26 |
| 11 | Mơ hồ | REQ-64 | "Hội viên huỷ buổi trước 12 giờ thì không bị trừ buổi." | Giữ nguyên "trước 12 giờ"; có thể hiểu là 12 giờ trước giờ tập hoặc 12 giờ trưa | Q-27 |
| 12 | Thiếu | REQ-64, REQ-63 | "Hội viên huỷ buổi trước 12 giờ thì không bị trừ buổi." (không nêu trường hợp huỷ muộn hơn) | Không tự điền | Q-28 |
| 13 | Thiếu | REQ-57, REQ-60, REQ-62, REQ-64, REQ-65 | "không bị trừ buổi" (Mục 7 câu 3); "ghi nhận buổi tập" (Mục 7 câu 4); nguồn không nêu thời điểm trừ buổi, trường hợp bị từ chối, quá hạn, không đến, và nội dung ghi nhận | Không tự điền | Q-29, Q-30, Q-31 |
| 14 | Thiếu | REQ-60, REQ-62, REQ-87 | "Thông báo cho hội viên gửi qua thông báo đẩy của ứng dụng" (Mục 10 câu 1); nguồn không nêu cách huấn luyện viên được báo yêu cầu đặt buổi | Không tự điền | Q-15 |
| 15 | Thiếu | REQ-59 | "khung giờ trống trong lịch làm việc của huấn luyện viên" (Mục 7 câu 2); không nêu ai lập lịch làm việc và khung giờ dài bao lâu | Không tự điền | Q-06, Q-32 |
| 16 | Mơ hồ | REQ-78, REQ-79 | "đặt giá các gói và chương trình khuyến mãi theo khoảng ngày" (Mục 9 câu 1) | Giữ nguyên; không rõ "theo khoảng ngày" gắn với giá hay khuyến mãi, "các gói" gồm loại nào, và khuyến mãi áp dụng ra sao | Q-10, Q-08, Q-09 |
| 17 | Mơ hồ | REQ-82 | "tỉ lệ lấp đầy lớp nhóm" | Giữ nguyên; thiếu công thức và kỳ báo cáo | Q-33 |
| 18 | Mơ hồ | REQ-83 | "số buổi tập cá nhân của từng huấn luyện viên" | Giữ nguyên; thiếu cách tính và kỳ báo cáo | Q-34 |
| 19 | Mơ hồ | REQ-84, REQ-85, REQ-86 | "Mỗi ngày lúc 8 giờ sáng, hệ thống gửi thông báo nhắc gia hạn cho hội viên có gói hết hạn trong 7 ngày tới." | Giữ nguyên; chưa rõ nhắc lặp mỗi ngày hay một lần | Q-35 |
| 20 | Mơ hồ | REQ-88, REQ-08 | "hội viên chưa cài ứng dụng thì nhận SMS" (Mục 10 câu 1) và "đăng ký tài khoản hội viên" trên ứng dụng di động (Mục 1) | Giữ nguyên; trường hợp "chưa cài ứng dụng" khó xảy ra nếu tài khoản đăng ký trên ứng dụng | Q-36 |
| 21 | Thiếu | REQ-18, REQ-08 | "Lễ tân cũng bán gói tại quầy" (Mục 2 câu 4); nguồn không nêu người mua tại quầy có tài khoản không | Không tự điền | Q-01 |
| 22 | Mơ hồ | REQ-02 | "phần mềm quản lý hội viên, lớp tập và ra vào" (Đoạn mở đầu câu 3) | Giữ ở mức bối cảnh; "quản lý" không nêu thao tác nên không tạo REQ chức năng | Q-02 |
| 23 | Thiếu | REQ-01, REQ-25, REQ-69, REQ-05 | Mục 3 câu 2 ("sức chứa theo phòng"), Mục 8 câu 1 ("chọn loại lớp, phòng, ..."); nguồn dùng chi nhánh, phòng, loại lớp nhưng không nêu ai tạo | Không tự điền | Q-03, Q-04 |
| 24 | Thiếu | REQ-03, REQ-60, REQ-69 | Nguồn có lễ tân, quản lý chi nhánh, giám đốc chuỗi, huấn luyện viên dùng hệ thống nhưng chỉ nêu hội viên tự đăng ký (Mục 1 câu 2) | Không tự điền | Q-05 |
| 25 | Thiếu | REQ-56 | "Hội viên mua gói buổi tập cá nhân ..." (Mục 7 câu 1); không nêu kênh mua và hình thức thanh toán | Không tự điền | Q-07 |
| 26 | Thiếu | REQ-42, REQ-54 | "Khách vãng lai mua vé tập một ngày tại quầy" (Mục 5 câu 3), "thu phí chuyển nhượng 200.000 đồng" (Mục 6 câu 3); không nêu hình thức thu tiền | Không tự điền | Q-38 |
| 27 | Thiếu | REQ-22 | "Hội viên đặt chỗ lớp nhóm trên ứng dụng" (Mục 3 câu 1); không nêu điều kiện về gói tập | Không tự điền | Q-12 |
| 28 | Thiếu | REQ-28, REQ-30 | "người đó có 30 phút ... quá 30 phút thì chỗ chuyển cho người kế tiếp" (Mục 3 câu 4); không nêu chỗ trống có được giữ riêng và số phận người không xác nhận | Không tự điền | Q-22, Q-23 |
| 29 | Thiếu | REQ-36, REQ-37 | "3 lần vắng mặt trong 30 ngày thì bị khoá quyền đặt lớp 7 ngày." (Mục 4 câu 2); không nêu ảnh hưởng tới chỗ đã đặt và cách đếm sau khi khoá | Không tự điền | Q-20, Q-21 |
| 30 | Thiếu | REQ-46, REQ-52, REQ-41, REQ-63 | "Hội viên có gói từ 3 tháng trở lên được bảo lưu gói" (Mục 6 câu 1); "gói buổi tập cá nhân ... 90 ngày" (Mục 7 câu 1); "không đang bảo lưu" (Mục 5 câu 2); không nêu quan hệ giữa bảo lưu và gói buổi tập cá nhân, chỗ đã đặt, cửa quay | Không tự điền | Q-17, Q-18, Q-19 |
| 31 | Mơ hồ | REQ-69 | "lập lịch lớp nhóm hằng tuần" (Mục 8 câu 1) | Giữ nguyên; chưa rõ lập từng tuần hay lịch mẫu lặp lại | Q-16 |
| 32 | Mơ hồ | REQ-71, REQ-72 | "không được xếp hai lớp trùng giờ" (Mục 8 câu 2) | Giữ nguyên; thiếu thời lượng lớp nên chưa rõ trùng giờ bắt đầu hay chồng khoảng thời gian | Q-32 |
| 33 | Mơ hồ | REQ-44, REQ-45 | "mã QR dùng được trong ngày tại chi nhánh đã mua" (Mục 5 câu 3) | Giữ nguyên; chưa rõ số lần dùng trong ngày | Q-40 |
| 34 | Thiếu | REQ-92 | project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" | Không tự điền trường dữ liệu | Q-39 |

## 6. Ma trận phủ nguồn

| Vị trí trong nguồn | Tóm tắt nội dung | Kết luận (REQ-xx / Ngoài phạm vi / Bối cảnh) |
|---|---|---|
| Đoạn mở đầu, câu 1 | Chuỗi có 4 chi nhánh, khoảng 6.000 hội viên, 40 huấn luyện viên, mỗi chi nhánh khoảng 25 lớp mỗi ngày, loại lớp yoga, aerobic, đạp xe trong nhà | REQ-01 đến REQ-05 |
| Đoạn mở đầu, câu 2 | Hiện bán gói ghi bảng tính, đặt chỗ qua nhóm chat thường quá sức chứa, lễ tân dò tên trên giấy | Bối cảnh |
| Đoạn mở đầu, câu 3 | VietFit cần phần mềm quản lý hội viên, lớp tập và ra vào | Bối cảnh (mục tiêu nghiệp vụ). Xem Q-02 |
| Mục 1, câu 1 | Người quan tâm xem bảng giá gói tập và lịch lớp nhóm không cần tài khoản | REQ-06, REQ-07 |
| Mục 1, câu 2 | Đăng ký tài khoản hội viên bằng số điện thoại và họ tên để mua gói hoặc đặt lớp | REQ-08 |
| Mục 1, câu 3 | Gói tập thời hạn 1, 3, 6, 12 tháng; loại một chi nhánh hoặc toàn chuỗi | REQ-09, REQ-10 |
| Mục 2, câu 1 | Hội viên mua hoặc gia hạn gói trên ứng dụng và thanh toán qua cổng thanh toán | REQ-11 đến REQ-14 |
| Mục 2, câu 2 | Đơn chưa thanh toán thành công trong 15 phút thì bị huỷ | REQ-15, REQ-16 |
| Mục 2, câu 3 | Gia hạn khi gói cũ còn hiệu lực thì gói mới bắt đầu sau ngày hết hạn gói cũ | REQ-17 |
| Mục 2, câu 4 | Lễ tân bán gói tại quầy, thu tiền mặt hoặc thẻ qua máy POS không kết nối, nhập mã giao dịch POS | REQ-18 đến REQ-21 |
| Mục 3, câu 1 | Đặt chỗ lớp trên ứng dụng, sớm nhất 7 ngày, tối đa 2 lớp một ngày | REQ-22, REQ-23, REQ-24 |
| Mục 3, câu 2 | Mỗi lớp có sức chứa theo phòng | REQ-25 |
| Mục 3, câu 3 | Lớp đủ chỗ thì vào danh sách chờ | REQ-26 |
| Mục 3, câu 4 | Thông báo cho người đứng đầu danh sách chờ, 30 phút xác nhận, quá hạn chuyển người kế tiếp | REQ-27 đến REQ-30 |
| Mục 3, câu 5 | Không chuyển chỗ từ danh sách chờ khi còn dưới 1 giờ | REQ-31 |
| Mục 4, câu 1 | Hội viên huỷ chỗ chậm nhất 2 giờ trước giờ học | REQ-32, REQ-33 |
| Mục 4, câu 2 (vế 1) | Đặt chỗ mà không quẹt vào cửa trong khoảng quy định thì bị tính một lần vắng mặt | REQ-34, REQ-35 |
| Mục 4, câu 2 (vế 2) | 3 lần vắng mặt trong 30 ngày thì bị khoá quyền đặt lớp 7 ngày | REQ-36 đến REQ-38 |
| Mục 5, câu 1 | Hội viên vào chi nhánh qua cửa quay bằng mã QR trên ứng dụng | REQ-39 |
| Mục 5, câu 2 | Cửa quay hỏi phần mềm, chỉ mở khi gói còn hiệu lực, không bảo lưu, áp dụng cho chi nhánh | REQ-40, REQ-41 |
| Mục 5, câu 3 | Khách vãng lai mua vé một ngày tại quầy; lễ tân in vé có mã QR dùng trong ngày tại chi nhánh đã mua | REQ-42 đến REQ-45 |
| Mục 6, câu 1 | Gói từ 3 tháng được bảo lưu một lần mỗi gói, 7 đến 30 ngày, đăng ký trước ít nhất 1 ngày | REQ-46 đến REQ-50 |
| Mục 6, câu 2 | Ngày hết hạn lùi thêm đúng số ngày bảo lưu | REQ-51 |
| Mục 6, câu 3 | Chuyển nhượng gói còn ít nhất 30 ngày cho người có tài khoản, lễ tân thực hiện tại quầy, phí 200.000 đồng | REQ-52 đến REQ-55 |
| Mục 7, câu 1 | Mua gói buổi tập cá nhân 10 hoặc 20 buổi, 90 ngày, với một huấn luyện viên | REQ-56 đến REQ-58 |
| Mục 7, câu 2 | Chọn khung giờ trống để đặt buổi; huấn luyện viên xác nhận hoặc từ chối trong 12 giờ, quá hạn tự huỷ | REQ-59 đến REQ-62 |
| Mục 7, câu 3 | Hội viên huỷ buổi trước 12 giờ thì không bị trừ buổi | REQ-63, REQ-64 |
| Mục 7, câu 4 | Huấn luyện viên ghi nhận buổi tập và chỉ số cơ thể (cân nặng, tỉ lệ mỡ); chỉ hội viên đó và huấn luyện viên phụ trách được xem | REQ-65 đến REQ-68 |
| Mục 8, câu 1 | Quản lý chi nhánh lập lịch lớp hằng tuần: loại lớp, phòng, huấn luyện viên, giờ | REQ-69, REQ-70 |
| Mục 8, câu 2 | Phòng, huấn luyện viên không xếp hai lớp trùng giờ | REQ-71, REQ-72 |
| Mục 8, câu 3 | Dưới 3 người đặt lúc 2 giờ trước giờ học thì tự huỷ lớp và thông báo | REQ-73 đến REQ-75 |
| Mục 8, câu 4 | Quản lý chi nhánh huỷ lớp vì sự cố, thông báo cho người đã đặt và người trong danh sách chờ | REQ-76, REQ-77 |
| Mục 9, câu 1 | Giám đốc chuỗi đặt giá gói và khuyến mãi theo khoảng ngày, giảm tối đa 20% | REQ-78 đến REQ-80 |
| Mục 9, câu 2 | Giám đốc chuỗi xem báo cáo doanh thu, tỉ lệ lấp đầy, số buổi tập cá nhân của huấn luyện viên để tính thù lao | REQ-81 đến REQ-83; việc tính thù lao: Ngoài phạm vi |
| Mục 9, câu 3 | 8 giờ sáng mỗi ngày gửi nhắc gia hạn cho hội viên có gói hết hạn trong 7 ngày tới | REQ-84 đến REQ-86 |
| Mục 10, câu 1 | Thông báo qua thông báo đẩy; hội viên chưa cài ứng dụng nhận SMS | REQ-87 đến REQ-90 |
| Mục 10, câu 2 | Mọi giao dịch thu tiền phải xuất hoá đơn điện tử qua hệ thống hoá đơn điện tử | REQ-91, REQ-92 |
| Mục 10, câu 3 (vế 1) | 6 giờ sáng thứ Hai mở đặt lớp tuần mới, tới 1.500 hội viên đặt cùng lúc | REQ-93, REQ-94 |
| Mục 10, câu 3 (vế 2) | Không để số chỗ đã đặt vượt sức chứa | REQ-95 |
| Mục 10, câu 4 | Cửa quay phản hồi trong vòng 1 giây | REQ-96 |
| project-profile.md, HE_THONG_NGOAI: cổng thanh toán | Cổng thanh toán trực tuyến của đối tác (API REST, có tài liệu API thanh toán và tra cứu giao dịch) | REQ-14 |
| project-profile.md, HE_THONG_NGOAI: cổng SMS | Cổng SMS của nhà mạng (API REST) | REQ-90 |
| project-profile.md, HE_THONG_NGOAI: thông báo đẩy | Dịch vụ thông báo đẩy của nền tảng di động | REQ-89 |
| project-profile.md, HE_THONG_NGOAI: hoá đơn điện tử | Hệ thống hoá đơn điện tử của đơn vị cung cấp (API REST, chưa có tài liệu API) | REQ-92 |
| project-profile.md, HE_THONG_NGOAI: cửa quay | Cửa quay có đầu đọc mã QR tại mỗi chi nhánh, gửi mã QR tới phần mềm qua API và mở cửa theo kết quả trả về | REQ-40 |
| project-profile.md, mục 4, gạch 1 | Nghiệp vụ hoá đơn điện tử nằm ngoài phạm vi; phần mềm chỉ gửi dữ liệu giao dịch thu tiền | Ngoài phạm vi (lập, điều chỉnh, huỷ hoá đơn); phần gửi dữ liệu: REQ-92 |
| project-profile.md, mục 4, gạch 2 | Tính thù lao huấn luyện viên làm ngoài phần mềm; phần mềm chỉ cung cấp báo cáo số buổi tập cá nhân | Ngoài phạm vi (tính thù lao); báo cáo: REQ-83 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-01 | Khi lễ tân bán gói tại quầy, người mua có phải đã có tài khoản hội viên không? (Phải có tài khoản / Lễ tân tạo tài khoản cho người mua tại quầy) | REQ-08, REQ-18, REQ-20; chức năng của lễ tân (P01, P02) | Mục 1 câu 2 ("Để mua gói hoặc đặt lớp, người đó đăng ký tài khoản hội viên...") và Mục 2 câu 4 ("Lễ tân cũng bán gói tại quầy"): nguồn không nói người mua tại quầy có tài khoản không |
| Q-02 | Ngoài đăng ký tài khoản, nhân viên (lễ tân, quản lý chi nhánh, giám đốc chuỗi) có thao tác xem, tra cứu hoặc sửa thông tin hội viên không? (Có, nêu thao tác / Không) | REQ-02, REQ-08; danh sách chức năng của nhân viên (P01, P02) | Đoạn mở đầu câu 3: "VietFit cần phần mềm quản lý hội viên, lớp tập và ra vào"; "quản lý hội viên" không nêu thao tác |
| Q-03 | Ai tạo và cập nhật danh mục chi nhánh, phòng tập và sức chứa của từng phòng? (Giám đốc chuỗi / Quản lý chi nhánh / Người khác - nêu rõ) | REQ-01, REQ-25, REQ-69, REQ-71; use case quản lý danh mục (P02) | Mục 3 câu 2 ("Mỗi lớp có sức chứa theo phòng") và Mục 8 câu 1 ("chọn loại lớp, phòng, ..."): nguồn dùng phòng nhưng không nói ai tạo |
| Q-04 | Danh mục loại lớp chỉ gồm yoga, aerobic, đạp xe trong nhà hay mở rộng được, và ai quản lý danh mục này? (Cố định ba loại / Mở rộng được - nêu ai quản lý) | REQ-05, REQ-69, REQ-70; use case quản lý danh mục (P02) | Đoạn mở đầu câu 1 ("(yoga, aerobic, đạp xe trong nhà)") và Mục 8 câu 1 ("chọn loại lớp") |
| Q-05 | Ai tạo và quản lý tài khoản của nhân viên (lễ tân, quản lý chi nhánh, giám đốc chuỗi) và hồ sơ huấn luyện viên? (Giám đốc chuỗi / Quản lý chi nhánh / Người khác - nêu rõ) | REQ-03, REQ-60, REQ-69, REQ-78; tác nhân và use case quản lý người dùng (P01, P02) | Mục 1 câu 2 chỉ nêu người quan tâm tự đăng ký tài khoản hội viên; các vai trò nhân viên và huấn luyện viên dùng hệ thống nhưng nguồn không nêu cách có tài khoản |
| Q-06 | Ai lập và cập nhật lịch làm việc của huấn luyện viên (nguồn cho khung giờ trống để đặt buổi tập cá nhân)? (Huấn luyện viên / Quản lý chi nhánh / Người khác - nêu rõ) | REQ-59; use case lập lịch làm việc huấn luyện viên (P02) | Mục 7 câu 2: "khung giờ trống trong lịch làm việc của huấn luyện viên" |
| Q-07 | Gói buổi tập cá nhân được mua qua kênh nào và thanh toán bằng hình thức nào? (Ứng dụng, thanh toán qua cổng thanh toán / Quầy, qua lễ tân / Cả hai) | REQ-56; luồng mua gói buổi tập cá nhân (P02, P04) | Mục 7 câu 1: "Hội viên mua gói buổi tập cá nhân ... với một huấn luyện viên" không nêu kênh và hình thức thanh toán |
| Q-08 | Giá và chương trình khuyến mãi do giám đốc chuỗi đặt áp dụng cho những loại nào? (Chỉ gói tập / Gói tập và gói buổi tập cá nhân / Gồm cả vé tập một ngày) | REQ-78, REQ-79, REQ-56, REQ-42 | Mục 9 câu 1: "đặt giá các gói và chương trình khuyến mãi"; Mục 5 câu 3 (vé tập một ngày) và Mục 7 câu 1 (gói buổi tập cá nhân) không nêu giá do ai đặt |
| Q-09 | Chương trình khuyến mãi được áp dụng tự động cho đơn nằm trong khoảng ngày, hay người mua phải nhập mã? (Tự động / Nhập mã) | REQ-79, REQ-80; luồng mua gói (P04) | Mục 9 câu 1: "chương trình khuyến mãi theo khoảng ngày" không nêu cách áp dụng cho người mua |
| Q-10 | Cụm "theo khoảng ngày" áp dụng cho cả giá gói và chương trình khuyến mãi, hay chỉ cho chương trình khuyến mãi? (Cả hai / Chỉ khuyến mãi) | REQ-78, REQ-79 | Mục 9 câu 1: "đặt giá các gói và chương trình khuyến mãi theo khoảng ngày" |
| Q-11 | Đặt chỗ lớp nhóm mở theo cách nào? (Mỗi lớp mở đặt từ 7 ngày trước giờ học / Cả tuần mới mở lúc 6 giờ sáng thứ Hai / Kết hợp - nêu rõ) | REQ-22, REQ-23, REQ-93, REQ-94; luồng đặt chỗ (P04, P06) | Mâu thuẫn: Mục 3 câu 1 ("sớm nhất 7 ngày trước giờ học") và Mục 10 câu 3 ("Lúc 6 giờ sáng thứ Hai, khi mở đặt lớp cho tuần mới") |
| Q-12 | Hội viên có cần gói tập còn hiệu lực, và gói đó có phải áp dụng cho chi nhánh của lớp, mới được đặt chỗ lớp nhóm không? (Cần gói còn hiệu lực và áp dụng cho chi nhánh của lớp / Chỉ cần gói còn hiệu lực / Không cần gói) | REQ-22, REQ-10; điều kiện tiên quyết của UC đặt chỗ (P04) | Mục 3 câu 1 và Mục 5 câu 2: nguồn nêu điều kiện gói cho cửa quay nhưng không nêu điều kiện gói cho đặt chỗ lớp |
| Q-13 | Khi thanh toán trực tuyến thất bại và đơn còn trong 15 phút, hội viên có được thanh toán lại trên cùng đơn không? (Có / Không, phải tạo đơn mới) | REQ-13, REQ-16; luồng ngoại lệ của UC mua gói (P04) | Mục 2 câu 1 và câu 2: nguồn không nêu điều gì xảy ra khi thanh toán thất bại |
| Q-14 | Khi cổng thanh toán báo thanh toán thành công sau khi đơn đã bị huỷ, hệ thống xử lý thế nào? (Hoàn tiền / Kích hoạt gói / Khác - nêu rõ) | REQ-14, REQ-16; luồng ngoại lệ của UC mua gói (P04) | Mục 2 câu 2: "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ" không nêu trường hợp kết quả thanh toán đến sau khi huỷ |
| Q-15 | Huấn luyện viên được báo có yêu cầu đặt buổi tập cá nhân bằng cách nào, và hội viên có được thông báo khi yêu cầu được xác nhận, bị từ chối hoặc bị tự huỷ không? (Có, qua kênh thông báo của hệ thống / Không) | REQ-60, REQ-62, REQ-87; luồng đặt buổi tập (P04) | Mục 7 câu 2 và Mục 10 câu 1: nguồn chỉ nêu thông báo cho hội viên và không nêu thông báo cho huấn luyện viên |
| Q-16 | Quản lý chi nhánh lập lịch riêng cho từng tuần, hay lập một lịch mẫu lặp lại hằng tuần? (Từng tuần / Lịch mẫu lặp lại) | REQ-69, REQ-70; luồng lập lịch (P04) | Mục 8 câu 1: "lập lịch lớp nhóm hằng tuần" |
| Q-17 | Quy tắc bảo lưu và chuyển nhượng gói có áp dụng cho gói buổi tập cá nhân không? (Có / Không) | REQ-46, REQ-47, REQ-52, REQ-58 | Mục 6 câu 1 và câu 3 dùng từ "gói"; Mục 7 câu 1 có "gói buổi tập cá nhân" dùng trong 90 ngày (gần 3 tháng) |
| Q-18 | Hội viên chỉ có gói buổi tập cá nhân (không có gói tập) có được vào chi nhánh qua cửa quay không? (Có / Không) | REQ-41, REQ-39 | Mục 5 câu 2 ("chỉ mở khi gói tập còn hiệu lực") và Mục 7 câu 1 (gói buổi tập cá nhân) |
| Q-19 | Khi hội viên bảo lưu gói, các chỗ lớp nhóm và buổi tập cá nhân đã đặt trong thời gian bảo lưu có bị huỷ không, và hội viên đang bảo lưu có được đặt thêm không? (Huỷ và không cho đặt / Giữ nguyên và cho đặt) | REQ-46, REQ-41, REQ-34; luồng bảo lưu (P04) | Mục 5 câu 2 ("không đang bảo lưu" mới được mở cửa) và Mục 4 câu 2 (vắng mặt): nguồn không nêu quan hệ giữa bảo lưu và chỗ đã đặt |
| Q-20 | Khi hội viên bị khoá quyền đặt lớp, các chỗ đã đặt và vị trí trong danh sách chờ của hội viên đó có giữ nguyên không? (Giữ nguyên / Huỷ) | REQ-36; luồng khoá quyền đặt lớp (P04) | Mục 4 câu 2: "bị khoá quyền đặt lớp 7 ngày" |
| Q-21 | Sau khi hội viên bị khoá quyền đặt lớp, số lần vắng mặt đã tính có được xoá để đếm lại không? (Xoá và đếm lại / Giữ và đếm tiếp trong cửa sổ 30 ngày) | REQ-37, REQ-36 | Mục 4 câu 2: "3 lần vắng mặt trong 30 ngày" |
| Q-22 | Trong 30 phút chờ xác nhận, chỗ trống có được giữ riêng cho hội viên đứng đầu danh sách chờ không? (Giữ riêng / Không giữ, hội viên khác đặt trực tiếp được) | REQ-28, REQ-29, REQ-95; luồng danh sách chờ (P04) | Mục 3 câu 4: "người đó có 30 phút để mở ứng dụng, xem lại lớp và xác nhận nhận chỗ"; Mục 10 câu 3: không vượt sức chứa |
| Q-23 | Hội viên được thông báo nhưng không xác nhận trong 30 phút thì còn trong danh sách chờ không? (Còn, giữ vị trí cuối / Bị loại khỏi danh sách chờ) | REQ-30; luồng danh sách chờ (P04) | Mục 3 câu 4: "quá 30 phút thì chỗ chuyển cho người kế tiếp" |
| Q-24 | Khi hội viên gia hạn lúc gói cũ đã hết hạn, gói mới bắt đầu vào ngày nào? (Ngày thanh toán thành công / Ngày hội viên chọn / Khác - nêu rõ) | REQ-17, REQ-12; luồng gia hạn (P04) | Mục 2 câu 3: nguồn chỉ nêu trường hợp gói cũ còn hiệu lực |
| Q-25 | Thời hạn 15 phút của đơn mua tính từ lúc tạo đơn hay từ lúc bắt đầu thanh toán, và áp dụng cho đơn mua qua ứng dụng, đơn gia hạn hay cả đơn bán tại quầy? (Từ lúc tạo đơn / Từ lúc bắt đầu thanh toán; áp dụng cho - nêu rõ) | REQ-16, REQ-15; luồng mua gói (P04) | Mục 2 câu 2: "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ" |
| Q-26 | Thời hạn 90 ngày của gói buổi tập cá nhân tính từ ngày mua hay từ buổi tập đầu tiên? (Ngày mua / Buổi tập đầu tiên) | REQ-58, REQ-56 | Mục 7 câu 1: "dùng trong 90 ngày" |
| Q-27 | "Huỷ buổi trước 12 giờ" nghĩa là huỷ trước giờ tập ít nhất 12 giờ, hay trước 12 giờ trưa của ngày tập? (Trước giờ tập ít nhất 12 giờ / Trước 12 giờ trưa) | REQ-64, REQ-63 | Mục 7 câu 3: "Hội viên huỷ buổi trước 12 giờ thì không bị trừ buổi" |
| Q-28 | Hội viên huỷ buổi tập cá nhân muộn hơn mốc nói trên thì bị trừ buổi hay không được huỷ? (Bị trừ buổi / Không được huỷ) | REQ-64, REQ-63; luồng huỷ buổi (P04) | Mục 7 câu 3: nguồn chỉ nêu trường hợp huỷ sớm |
| Q-29 | Buổi trong gói bị trừ vào lúc nào? (Khi huấn luyện viên xác nhận / Khi huấn luyện viên ghi nhận buổi đã diễn ra / Khác - nêu rõ) | REQ-64, REQ-65, REQ-57 | Mục 7 câu 3 ("không bị trừ buổi") và câu 4 ("ghi nhận buổi tập"): nguồn không nêu thời điểm trừ buổi |
| Q-30 | Yêu cầu đặt buổi bị huấn luyện viên từ chối, bị tự huỷ do quá hạn, hoặc buổi đã xác nhận mà hội viên không đến thì có bị trừ buổi không? (Từng trường hợp: Có / Không) | REQ-60, REQ-62, REQ-64 | Mục 7 câu 2 và câu 3 |
| Q-31 | Ghi nhận buổi tập chỉ là đánh dấu buổi đã diễn ra, hay gồm thêm thông tin khác? (Chỉ đánh dấu buổi đã diễn ra / Có thêm thông tin - nêu rõ) | REQ-65; luồng ghi nhận buổi tập (P04), dữ liệu (P13) | Mục 7 câu 4: "huấn luyện viên ghi nhận buổi tập" |
| Q-32 | Mỗi lớp nhóm và mỗi khung giờ buổi tập cá nhân dài bao lâu? (Cố định - nêu số phút / Do người lập lịch chọn) | REQ-71, REQ-72, REQ-59, REQ-70 | Mục 8 câu 1 ("giờ"), câu 2 ("trùng giờ") và Mục 7 câu 2 ("khung giờ trống"): nguồn không nêu thời lượng, nên chưa rõ trùng giờ là trùng giờ bắt đầu hay chồng khoảng thời gian |
| Q-33 | Tỉ lệ lấp đầy lớp nhóm tính thế nào và theo kỳ nào? (Số chỗ đã đặt chia sức chứa / Số hội viên vào lớp chia sức chứa; theo ngày / tuần / tháng) | REQ-82; báo cáo (P06) | Mục 9 câu 2: "tỉ lệ lấp đầy lớp nhóm" |
| Q-34 | Số buổi tập cá nhân của từng huấn luyện viên trong báo cáo tính theo buổi đã ghi nhận hay buổi đã xác nhận, và theo kỳ nào? (Buổi đã ghi nhận / Buổi đã xác nhận; theo tháng / Khác) | REQ-83; báo cáo (P06) | Mục 9 câu 2: "số buổi tập cá nhân của từng huấn luyện viên" |
| Q-35 | Hội viên có gói hết hạn trong 7 ngày tới nhận nhắc gia hạn mỗi ngày hay chỉ một lần, và đã gia hạn thì còn nhận nhắc không? (Mỗi ngày đến khi gia hạn hoặc hết hạn / Mỗi ngày trong 7 ngày bất kể đã gia hạn / Một lần) | REQ-84, REQ-85, REQ-86 | Mục 9 câu 3: "Mỗi ngày lúc 8 giờ sáng, ... hội viên có gói hết hạn trong 7 ngày tới" |
| Q-36 | Hệ thống xác định hội viên "chưa cài ứng dụng" bằng cách nào, khi hội viên đăng ký tài khoản trên ứng dụng? (Đăng ký tại quầy / Đã gỡ ứng dụng / Không có thiết bị nhận thông báo đẩy / Khác - nêu rõ) | REQ-88, REQ-08, REQ-87 | Mục 10 câu 1: "hội viên chưa cài ứng dụng thì nhận SMS" và Mục 1 câu 2: tài khoản hội viên đăng ký trên ứng dụng di động |
| Q-37 | "Giao dịch thu tiền" gồm những khoản nào, và có khoản nào không cần xuất hoá đơn điện tử không? (Gói tập, gia hạn, gói buổi tập cá nhân, vé một ngày, phí chuyển nhượng; ngoại lệ - nêu rõ hoặc Không có) | REQ-91, REQ-92 | Mục 10 câu 2: "Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử" |
| Q-38 | Vé tập một ngày và phí chuyển nhượng được thu bằng hình thức nào? (Tiền mặt / Thẻ qua máy POS / Cả hai) | REQ-42, REQ-54, REQ-20 | Mục 5 câu 3 và Mục 6 câu 3: nguồn chỉ nêu hình thức thu tiền cho việc bán gói (Mục 2 câu 4) |
| Q-39 | Dữ liệu giao dịch thu tiền gửi sang hệ thống hoá đơn điện tử gồm những trường nào? (Danh sách trường theo tài liệu API của đơn vị cung cấp, khi có) | REQ-92; giao diện hệ thống ngoài (P11b) | project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" |
| Q-40 | Mã QR trên vé tập một ngày mở cửa quay một lần hay nhiều lần trong ngày? (Một lần / Nhiều lần) | REQ-44, REQ-45, REQ-41; luồng vào chi nhánh (P04) | Mục 5 câu 3: "mã QR dùng được trong ngày tại chi nhánh đã mua" |
| Q-41 | Ngưỡng 1 giây tính từ lúc nào đến lúc nào? (Từ lúc đầu đọc quét mã đến lúc cửa mở / Từ lúc phần mềm nhận yêu cầu đến lúc trả kết quả) | REQ-96, REQ-40; NFR (P06) | Mục 10 câu 4: "Cửa quay phải phản hồi trong vòng 1 giây" (chủ thể là cửa quay, không phải phần mềm) |
| Q-42 | Khi 1.500 hội viên đặt chỗ cùng lúc, thời gian phản hồi tối đa cho một lần đặt chỗ là bao nhiêu giây, và "cùng lúc" là trong khoảng bao nhiêu giây? (Nêu số giây) | REQ-94; NFR (P06) | Mục 10 câu 3: "có thể có tới 1.500 hội viên đặt chỗ cùng lúc" không nêu ngưỡng đo |
| Q-43 | Các hành động nguồn viết ở dạng bị động (huỷ đơn quá 15 phút, chuyển chỗ trong danh sách chờ, tính vắng mặt, khoá quyền đặt lớp) do hệ thống tự thực hiện, hay có bước nhân viên duyệt hoặc gỡ? (Hệ thống tự thực hiện, không ngoại lệ / Nhân viên được duyệt hoặc gỡ - nêu rõ) | REQ-15, REQ-30, REQ-34, REQ-36; tác nhân (P01), luồng ngoại lệ (P04) | Mục 2 câu 2, Mục 3 câu 4, Mục 4 câu 2: câu bị động không nêu chủ thể |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

Không có mục Target nào ở trạng thái Không đạt. Các điểm cần người dùng lưu ý:

- REQ-23 và REQ-93 là cặp REQ mâu thuẫn chưa giải quyết được (xem Q-11); các bước sau không được chọn một bên khi chưa có câu trả lời.
- Các Q về danh mục và tài khoản (Q-01, Q-02, Q-03, Q-04, Q-05, Q-06) làm đổi danh sách chức năng; chưa có câu trả lời thì P01, P02 không được tự thêm chức năng quản lý các danh mục này.
- REQ-68 phân loại Chức năng theo quy ước F3 (vai trò được xem ghi vào chủ thể); nếu người dùng coi đây là yêu cầu bảo mật thì chuyển sang Phi chức năng.
- Các cặp REQ chức năng và quy tắc nghiệp vụ tách theo F2 quy tắc 5 (REQ-15 và REQ-16, REQ-73 và REQ-74, REQ-36 đến REQ-38, REQ-84 đến REQ-86) có nội dung chức năng tham chiếu ngưỡng ở REQ quy tắc nghiệp vụ đi kèm.
