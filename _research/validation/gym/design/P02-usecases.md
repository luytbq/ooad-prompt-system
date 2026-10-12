# P02 - Xác định use case - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02 |
| Phiên bản | 1.1 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0); P01-actors.md (phiên bản 1.0); yeu-cau-phong-tap.md; P02-usecases.md (phiên bản 1.0, bản được cập nhật); P02R-review.md (phiên bản 1.0). PHAM_VI_LAN_CHAY, QUY_UOC_DA_CHOT: Không có. YEU_CAU_BO_SUNG: Áp dụng UCR-01, UCR-02, UCR-03 của P02R-review.md phiên bản 1.0 |
| Phạm vi | Toàn hệ thống |
| Mã Q, ASM cuối đã cấp | Q-49; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Danh sách mục tiêu tác nhân

| ACT | Mục tiêu | Mức mục tiêu dự kiến | REQ | CAND |
|---|---|---|---|---|
| ACT-01 | Xem giá các gói tập | User-goal | REQ-06 | CAND-01 |
| ACT-01 | Xem lịch lớp nhóm | User-goal | REQ-07 | CAND-02 |
| ACT-01 | Đăng ký tài khoản hội viên | User-goal | REQ-08 | CAND-03 |
| ACT-02 | Xác thực để dùng các chức năng dành cho người có tài khoản | Subfunction | REQ-06, REQ-07, REQ-08 | CAND-04 |
| ACT-02 | Mua hoặc gia hạn gói tập | User-goal | REQ-11, REQ-12, REQ-13, REQ-14, REQ-15, REQ-16, REQ-17 | CAND-05, CAND-06, CAND-08, CAND-09, CAND-12 |
| ACT-02 | Đặt chỗ lớp nhóm, huỷ chỗ, vào danh sách chờ và nhận chỗ khi có người huỷ | Summary | REQ-22 đến REQ-33 | CAND-70 |
| ACT-02 | Đặt chỗ lớp nhóm (kể cả vào danh sách chờ khi lớp đã đủ chỗ) | User-goal | REQ-22, REQ-23, REQ-24, REQ-25, REQ-26, REQ-93, REQ-95 | CAND-19, CAND-20, CAND-21, CAND-22, CAND-31 |
| ACT-02 | Huỷ chỗ lớp nhóm đã đặt | User-goal | REQ-27, REQ-32, REQ-33 | CAND-25, CAND-26 |
| ACT-02 | Nhận chỗ lớp khi được thông báo từ danh sách chờ | User-goal | REQ-28, REQ-29 | CAND-27 |
| ACT-02 | Vào chi nhánh bằng mã QR | User-goal | REQ-39, REQ-40, REQ-41 | CAND-32, CAND-34, CAND-35 |
| ACT-02 | Bảo lưu gói tập | User-goal | REQ-46, REQ-47, REQ-48, REQ-49, REQ-50, REQ-51 | CAND-36, CAND-37 |
| ACT-02 | Mua gói buổi tập cá nhân, đặt và huỷ buổi tập | Summary | REQ-56 đến REQ-64 | CAND-71 |
| ACT-02 | Mua gói buổi tập cá nhân với một huấn luyện viên | User-goal | REQ-56, REQ-57, REQ-58 | CAND-38 |
| ACT-02 | Đặt buổi tập cá nhân | User-goal | REQ-59 | CAND-39, CAND-40 |
| ACT-02 | Huỷ buổi tập cá nhân đã đặt | User-goal | REQ-63, REQ-64 | CAND-41 |
| ACT-02 | Xem chỉ số cơ thể của mình | User-goal | REQ-68 | CAND-42 |
| ACT-03 | Vào chi nhánh trong ngày bằng mã QR trên vé tập một ngày | User-goal | REQ-44, REQ-45 | CAND-33 |
| ACT-04 | Xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân | User-goal | REQ-60, REQ-61 | CAND-43 |
| ACT-04 | Ghi nhận buổi tập cá nhân và chỉ số cơ thể của hội viên | User-goal | REQ-65, REQ-66, REQ-67 | CAND-45, CAND-46 |
| ACT-04 | Xem chỉ số cơ thể của hội viên mình phụ trách | User-goal | REQ-68 | CAND-47 |
| ACT-05 | Bán gói tập tại quầy (thu tiền mặt hoặc nhập mã giao dịch POS) | User-goal | REQ-18, REQ-19, REQ-20, REQ-21 | CAND-07, CAND-10, CAND-11 |
| ACT-05 | Chuyển nhượng gói tập tại quầy và thu phí chuyển nhượng | User-goal | REQ-52, REQ-53, REQ-54, REQ-55 | CAND-48, CAND-49 |
| ACT-05 | Bán vé tập một ngày có mã QR cho khách vãng lai | User-goal | REQ-42, REQ-43, REQ-44, REQ-45 | CAND-50, CAND-51 |
| ACT-06 | Lập lịch lớp nhóm hằng tuần | User-goal | REQ-69, REQ-70, REQ-71, REQ-72 | CAND-52 |
| ACT-06 | Huỷ lớp nhóm vì sự cố | User-goal | REQ-76, REQ-77 | CAND-53, CAND-54 |
| ACT-07 | Đặt giá các gói | User-goal | REQ-78 | CAND-57 |
| ACT-07 | Đặt chương trình khuyến mãi theo khoảng ngày | User-goal | REQ-79, REQ-80 | CAND-58 |
| ACT-07 | Xem báo cáo doanh thu, tỉ lệ lấp đầy lớp nhóm và số buổi tập cá nhân của huấn luyện viên | User-goal | REQ-81, REQ-82, REQ-83 | CAND-59, CAND-60, CAND-61 |
| ACT-13 | Nhắc gia hạn cho hội viên có gói hết hạn trong 7 ngày tới | User-goal | REQ-84, REQ-85, REQ-86 | CAND-63, CAND-64, CAND-65 |
| ACT-14 | Chuyển chỗ cho người kế tiếp khi hội viên không xác nhận nhận chỗ trong 30 phút | User-goal | REQ-30, REQ-31 | CAND-28 |
| ACT-14 | Ghi nhận vắng mặt của hội viên đặt chỗ mà không vào lớp, khoá quyền đặt lớp khi đạt ngưỡng | User-goal | REQ-34, REQ-35, REQ-36, REQ-37, REQ-38 | CAND-29, CAND-30 |
| ACT-14 | Huỷ lớp nhóm có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học | User-goal | REQ-73, REQ-74, REQ-75 | CAND-55, CAND-56 |
| ACT-14 | Huỷ yêu cầu đặt buổi tập cá nhân quá hạn 12 giờ chưa được huấn luyện viên phản hồi | User-goal | REQ-61, REQ-62 | CAND-44 |
| ACT-08 | Gửi kết quả thanh toán về hệ thống vào thời điểm cổng quyết định (chỉ khi cổng tự gửi, chờ Q-45) | User-goal | REQ-14 | CAND-13 |
| Chưa xác định | Tạo tài khoản hội viên cho người mua tại quầy (chờ Q-01) | User-goal | REQ-08, REQ-18 | CAND-14 |
| Chưa xác định | Quản lý thông tin hội viên (chờ Q-02) | User-goal | REQ-02 | CAND-15 |
| Chưa xác định | Mở đặt chỗ lớp cho tuần mới lúc 6 giờ sáng thứ Hai (chờ Q-11) | User-goal | REQ-93 | CAND-24 |
| Chưa xác định | Quản lý danh mục chi nhánh, phòng tập và sức chứa (chờ Q-03) | User-goal | REQ-01, REQ-25, REQ-69, REQ-71 | CAND-66 |
| Chưa xác định | Quản lý danh mục loại lớp (chờ Q-04) | User-goal | REQ-05, REQ-69, REQ-70 | CAND-67 |
| Chưa xác định | Quản lý tài khoản nhân viên và hồ sơ huấn luyện viên (chờ Q-05) | User-goal | REQ-03, REQ-60, REQ-69, REQ-78 | CAND-68 |
| Chưa xác định | Lập lịch làm việc của huấn luyện viên (chờ Q-06) | User-goal | REQ-59 | CAND-69 |

## 2. Danh sách sự kiện

| EV | Sự kiện | Loại | Nguồn phát (ACT) | Phản hồi mong đợi của hệ thống | REQ | CAND |
|---|---|---|---|---|---|---|
| EV-01 | Người quan tâm muốn biết giá các gói tập | Nghiệp vụ | ACT-01 | Cho xem giá các gói tập mà không cần tài khoản | REQ-06 | CAND-01 |
| EV-02 | Người quan tâm muốn biết lịch các lớp nhóm | Nghiệp vụ | ACT-01 | Cho xem lịch lớp nhóm mà không cần tài khoản | REQ-07 | CAND-02 |
| EV-03 | Người quan tâm muốn trở thành hội viên | Nghiệp vụ | ACT-01 | Tạo tài khoản hội viên bằng số điện thoại và họ tên | REQ-08 | CAND-03 |
| EV-04 | Hội viên muốn dùng các chức năng chỉ dành cho người có tài khoản | Nghiệp vụ | ACT-02 | Xác thực hội viên | REQ-06, REQ-07, REQ-08 | CAND-04 |
| EV-05 | Hội viên muốn mua hoặc gia hạn gói tập | Nghiệp vụ | ACT-02 | Tạo đơn mua, thu tiền qua cổng thanh toán, kích hoạt gói | REQ-11, REQ-12, REQ-13, REQ-14 | CAND-05, CAND-06 |
| EV-06 | Khách đến quầy muốn mua gói tập | Nghiệp vụ | ACT-05 | Bán gói, ghi nhận thu tiền mặt hoặc mã giao dịch POS | REQ-18, REQ-19, REQ-20, REQ-21 | CAND-07 |
| EV-07 | Đơn mua chưa thanh toán thành công sau 15 phút | Thời gian | - | Huỷ đơn; luồng thay thế của UC-005 | REQ-15, REQ-16 | CAND-09 |
| EV-08 | Hội viên muốn đặt chỗ một lớp nhóm | Nghiệp vụ | ACT-02 | Giữ chỗ trong lớp, hoặc đưa vào danh sách chờ khi lớp đã đủ chỗ | REQ-22, REQ-23, REQ-24, REQ-25, REQ-26 | CAND-19, CAND-20 |
| EV-09 | Hội viên muốn huỷ chỗ lớp đã đặt | Nghiệp vụ | ACT-02 | Huỷ chỗ, giải phóng chỗ, thông báo cho hội viên đứng đầu danh sách chờ | REQ-27, REQ-32, REQ-33 | CAND-25 |
| EV-10 | Hội viên đứng đầu danh sách chờ muốn nhận chỗ trong 30 phút sau thông báo | Nghiệp vụ | ACT-02 | Xác nhận nhận chỗ cho hội viên | REQ-28, REQ-29 | CAND-27 |
| EV-11 | Hết 30 phút kể từ thông báo nhận chỗ mà hội viên chưa xác nhận | Thời gian | ACT-14 | Chuyển chỗ cho người kế tiếp; không chuyển khi còn dưới 1 giờ trước giờ học | REQ-30, REQ-31 | CAND-28 |
| EV-12 | Hết 10 phút sau giờ bắt đầu lớp mà hội viên đặt chỗ chưa quẹt vào cửa | Thời gian | ACT-14 | Tính một lần vắng mặt; khoá quyền đặt lớp khi đạt ngưỡng | REQ-34, REQ-35, REQ-36, REQ-37, REQ-38 | CAND-29 |
| EV-13 | Hội viên quét mã QR trên ứng dụng tại cửa quay | Nghiệp vụ | ACT-02 | Kiểm tra gói, trả kết quả cho cửa quay mở cửa | REQ-39, REQ-40, REQ-41 | CAND-32 |
| EV-14 | Khách vãng lai quét mã QR trên vé tại cửa quay | Nghiệp vụ | ACT-03 | Kiểm tra vé, trả kết quả cho cửa quay mở cửa | REQ-44, REQ-45 | CAND-33 |
| EV-15 | Hội viên muốn bảo lưu gói tập | Nghiệp vụ | ACT-02 | Ghi nhận bảo lưu, lùi ngày hết hạn gói | REQ-46, REQ-47, REQ-48, REQ-49, REQ-50, REQ-51 | CAND-36 |
| EV-16 | Hội viên và người nhận đến quầy muốn chuyển nhượng gói | Nghiệp vụ | ACT-05 | Chuyển gói sang người nhận, thu phí chuyển nhượng | REQ-52, REQ-53, REQ-54, REQ-55 | CAND-48 |
| EV-17 | Khách vãng lai đến quầy muốn mua vé tập một ngày | Nghiệp vụ | ACT-05 | Bán vé, in vé có mã QR | REQ-42, REQ-43, REQ-44, REQ-45 | CAND-50 |
| EV-18 | Hội viên muốn mua gói buổi tập cá nhân | Nghiệp vụ | ACT-02 | Tạo gói buổi tập cá nhân gắn với một huấn luyện viên | REQ-56, REQ-57, REQ-58 | CAND-38 |
| EV-19 | Hội viên muốn đặt buổi tập cá nhân | Nghiệp vụ | ACT-02 | Ghi nhận yêu cầu đặt buổi vào khung giờ trống đã chọn | REQ-59 | CAND-39 |
| EV-20 | Huấn luyện viên muốn phản hồi yêu cầu đặt buổi tập cá nhân trong 12 giờ | Nghiệp vụ | ACT-04 | Ghi nhận xác nhận hoặc từ chối | REQ-60, REQ-61 | CAND-43 |
| EV-21 | Hết 12 giờ mà huấn luyện viên chưa xác nhận hoặc từ chối | Thời gian | ACT-14 | Huỷ yêu cầu đặt buổi | REQ-61, REQ-62 | CAND-44 |
| EV-22 | Hội viên muốn huỷ buổi tập cá nhân đã đặt | Nghiệp vụ | ACT-02 | Huỷ buổi; không trừ buổi khi huỷ trước 12 giờ | REQ-63, REQ-64 | CAND-41 |
| EV-23 | Buổi tập cá nhân đã diễn ra, huấn luyện viên muốn ghi nhận | Nghiệp vụ | ACT-04 | Ghi nhận buổi tập và chỉ số cơ thể | REQ-65, REQ-66, REQ-67 | CAND-45, CAND-46 |
| EV-24 | Hội viên hoặc huấn luyện viên phụ trách muốn xem chỉ số cơ thể | Nghiệp vụ | ACT-02, ACT-04 | Cho xem chỉ số cơ thể, chỉ với hai vai trò này | REQ-68 | CAND-42, CAND-47 |
| EV-25 | Quản lý chi nhánh muốn lập lịch lớp nhóm cho tuần | Nghiệp vụ | ACT-06 | Ghi nhận lịch lớp, không cho trùng giờ phòng hoặc huấn luyện viên | REQ-69, REQ-70, REQ-71, REQ-72 | CAND-52 |
| EV-26 | Sự cố khiến quản lý chi nhánh phải huỷ lớp | Nghiệp vụ | ACT-06 | Huỷ lớp, thông báo cho người đã đặt và người trong danh sách chờ | REQ-76, REQ-77 | CAND-53 |
| EV-27 | Đến 2 giờ trước giờ học, lớp có dưới 3 người đặt chỗ | Thời gian | ACT-14 | Tự huỷ lớp, thông báo cho người đã đặt | REQ-73, REQ-74, REQ-75 | CAND-55 |
| EV-28 | Giám đốc chuỗi muốn đặt giá các gói | Nghiệp vụ | ACT-07 | Ghi nhận giá gói | REQ-78 | CAND-57 |
| EV-29 | Giám đốc chuỗi muốn đặt chương trình khuyến mãi | Nghiệp vụ | ACT-07 | Ghi nhận khuyến mãi theo khoảng ngày, giảm tối đa 20% | REQ-79, REQ-80 | CAND-58 |
| EV-30 | Giám đốc chuỗi muốn xem báo cáo | Nghiệp vụ | ACT-07 | Cho xem báo cáo doanh thu, tỉ lệ lấp đầy, số buổi tập cá nhân | REQ-81, REQ-82, REQ-83 | CAND-59, CAND-60, CAND-61 |
| EV-31 | Đến 8 giờ sáng mỗi ngày | Thời gian | ACT-13 | Gửi nhắc gia hạn cho hội viên có gói hết hạn trong 7 ngày tới | REQ-84, REQ-85, REQ-86 | CAND-63 |

## 3. Bảng ứng viên use case

| CAND | Ứng viên | Kết luận | Phép thử không đạt | Lý do | REQ | Nguồn phát hiện |
|---|---|---|---|---|---|---|
| CAND-01 | Xem giá các gói tập | Giữ thành UC-001 | - | U-R05, U-R17: mục tiêu thông tin độc lập của người chưa có tài khoản; miễn U-T4. Khác loại thông tin với CAND-02 nên không gộp | REQ-06 | Mục tiêu (EV-01) |
| CAND-02 | Xem lịch lớp nhóm | Giữ thành UC-002 | - | U-R05, U-R17: mục tiêu thông tin độc lập; miễn U-T4. Ai được xem độc lập chờ Q-46 | REQ-07 | Mục tiêu (EV-02) |
| CAND-03 | Đăng ký tài khoản hội viên | Giữ thành UC-003 | - | U-R03: tác nhân chưa có tài khoản (ACT-01), kết quả là có tài khoản để mua gói và đặt lớp | REQ-08 | Mục tiêu (EV-03) |
| CAND-04 | Đăng nhập | Giữ thành UC-004 | U-T3, U-T4 | U-R01: nguồn ngụ ý xác thực ("tài khoản hội viên" ở Mục 1 câu 2; chức năng "không cần tài khoản" ở Mục 1 câu 1); chỉ nối ACT-02; các vai trò còn lại chờ Q-47; mức Subfunction | REQ-06, REQ-07, REQ-08 | Sự kiện (EV-04) |
| CAND-05 | Mua gói tập | Giữ thành UC-005 | - | Gộp CAND-06 và CAND-07 theo U-R12; nối ACT-02 và ACT-05 theo U-R10 b | REQ-11, REQ-13 | Mục tiêu (EV-05) |
| CAND-06 | Gia hạn gói tập | Gộp vào UC-005 | U-T11, U-AP15 | Cùng tác nhân, cùng mục tiêu có gói; khác mốc bắt đầu của gói mới (REQ-17) là luồng thay thế (U-R12) | REQ-12, REQ-17 | Mục tiêu (EV-05) |
| CAND-07 | Bán gói tập tại quầy | Gộp vào UC-005 | U-T11, U-AP15 | U-R10 b: lễ tân làm hộ khách, không có đoạn tương tác riêng từ 2 bước (thu tiền mặt, nhập mã POS tương ứng bước thanh toán của hội viên), kết quả như nhau (gói được kích hoạt); kênh thu tiền khác nhau là luồng thay thế (U-R12). Q-01 trả lời lễ tân tạo tài khoản tại quầy thì xét lại theo U-R10 a | REQ-18, REQ-19, REQ-20, REQ-21 | Mục tiêu (EV-06) |
| CAND-08 | Thanh toán đơn mua gói qua cổng thanh toán | Là bước của UC-005 | U-T1, U-T4 | Q4 d không thoả: vế "thanh toán thất bại thì thanh toán lại, không huỷ đơn" chưa có căn cứ (Q-13). U-R08: ACT-08 là tác nhân phụ, phản hồi trong cùng phiên | REQ-13, REQ-14 | Động từ |
| CAND-09 | Huỷ đơn mua chưa thanh toán thành công sau 15 phút | Là bước của UC-005 | U-T8, U-AP11 | U-R07 hết giờ trong phiên: luồng thay thế của UC-005 (theo P01 Mục 4) | REQ-15, REQ-16 | Sự kiện (EV-07) |
| CAND-10 | Thu tiền mặt khi bán gói tại quầy | Là bước của UC-005 | U-T1, U-T4, U-AP01 | Luồng thay thế thu tiền mặt (U-R12) | REQ-19 | Động từ |
| CAND-11 | Nhập mã giao dịch POS | Là bước của UC-005 | U-T1, U-T4, U-AP01 | Luồng thay thế thu tiền bằng thẻ (U-R12); máy POS không phải tác nhân (P01 Mục 4) | REQ-20, REQ-21 | Động từ |
| CAND-12 | Tính ngày bắt đầu của gói gia hạn | Là bước của UC-005 | U-T9, U-AP03 | Quy tắc tính, không có tác nhân trao đổi | REQ-17 | Động từ |
| CAND-13 | Ghi nhận kết quả thanh toán do cổng thanh toán gửi về | Chờ Q-45 | - | U-R08: Q-45 trả lời "Tự gửi kết quả về phần mềm" thì là UC của ACT-08 (Chính); trả lời "Chỉ trả khi được gọi hoặc tra cứu" thì là bước của UC-005 | REQ-14 | Mục tiêu (ACT-08) |
| CAND-14 | Tạo tài khoản hội viên cho người mua tại quầy | Chờ Q-01 | - | Q-01 trả lời "Lễ tân tạo tài khoản cho người mua tại quầy" thì thành đoạn tương tác riêng, xét U-R10 a để tách UC-005 và xét UC riêng của ACT-05 (U-R03); trả lời "Phải có tài khoản" thì loại | REQ-08, REQ-18 | Mục tiêu |
| CAND-15 | Quản lý thông tin hội viên | Chờ Q-02 | - | Q-02 trả lời "Có, nêu thao tác" thì thành UC "Quản lý <dữ liệu hội viên>" của nhân viên (U-R04) với đúng thao tác nguồn nêu; trả lời "Không" thì loại | REQ-02 | Mục tiêu (Đoạn mở đầu câu 3) |
| CAND-16 | Xuất hoá đơn điện tử cho giao dịch thu tiền | Là bước của UC-005, UC-007, UC-017, UC-019 | U-T9, U-AP03 | U-R08: ACT-11 là tác nhân phụ của các UC có thu tiền; Q4 a không thoả vì đoạn trao đổi dưới 3 bước và chưa có tài liệu API (Q-39). Phạm vi giao dịch chờ Q-37 | REQ-91, REQ-92 | Động từ |
| CAND-17 | Lập, điều chỉnh, huỷ hoá đơn điện tử | Loại | U-T10 | U-R16: "Nghiệp vụ hoá đơn điện tử nằm ngoài phạm vi: phần mềm chỉ gửi dữ liệu giao dịch thu tiền" (project-profile.md mục 4) | REQ-91, REQ-92 | Mục tiêu |
| CAND-18 | Quẹt thẻ ngân hàng trên máy POS | Loại | U-T10 | U-R16: "máy POS không kết nối với phần mềm" (Mục 2 câu 4); phần mềm chỉ nhận mã giao dịch (CAND-11) | REQ-20 | Động từ |
| CAND-19 | Đặt chỗ lớp nhóm | Giữ thành UC-010 | - | Gộp CAND-20 theo U-R12; CAND-21, CAND-22 là bước | REQ-22, REQ-23, REQ-24, REQ-25 | Mục tiêu (EV-08) |
| CAND-20 | Vào danh sách chờ của lớp đã đủ chỗ | Gộp vào UC-010 | U-T4, U-AP01 | U-R12: luồng thay thế khi lớp đủ chỗ, cùng mục tiêu có chỗ trong lớp; việc nhận chỗ sau đó là phiên khác (CAND-27, U-R13) | REQ-26 | Mục tiêu (EV-08) |
| CAND-21 | Xem lịch lớp để chọn lớp khi đặt chỗ | Là bước của UC-010 | U-T4, U-AP01 | U-R05: việc xem chỉ phục vụ một bước của mục tiêu đặt chỗ; Q4 a không thoả vì nguồn không mô tả đoạn xem từ 3 bước và UC-002 chỉ có tác nhân chính ACT-01 | REQ-22 | Động từ |
| CAND-22 | Kiểm tra quy tắc đặt chỗ (đặt trước tối đa 7 ngày, tối đa 2 lớp một ngày, sức chứa, quyền đặt lớp) | Là bước của UC-010 | U-T9, U-AP03 | Kiểm tra nội bộ trong phiên đặt chỗ | REQ-23, REQ-24, REQ-25, REQ-38, REQ-95 | Động từ |
| CAND-23 | Phục vụ 1.500 lượt đặt chỗ cùng lúc | Loại | U-T9 | Yêu cầu phi chức năng (REQ-94), chuyển P06 | REQ-94 | Động từ |
| CAND-24 | Mở đặt chỗ lớp cho tuần mới lúc 6 giờ sáng thứ Hai | Chờ Q-11 | - | Q-11 trả lời "Cả tuần mới mở lúc 6 giờ sáng thứ Hai" và việc mở do hệ thống thực hiện theo lịch thì là UC của tác nhân thời gian (U-R07), P01 chưa có tác nhân này; trả lời khác thì là quy tắc thời điểm, bước của UC-010 | REQ-93, REQ-23 | Động từ |
| CAND-25 | Huỷ chỗ lớp nhóm | Giữ thành UC-011 | - | U-R04 b: giao dịch nghiệp vụ có quy tắc thời hạn huỷ; không gộp vào đặt chỗ | REQ-32, REQ-33 | Mục tiêu (EV-09) |
| CAND-26 | Gửi thông báo cho hội viên đứng đầu danh sách chờ khi có người huỷ chỗ | Là bước của UC-011 | U-T9, U-AP03 | U-R06: hệ quả của huỷ chỗ; ACT-09, ACT-10 là tác nhân phụ | REQ-27 | Động từ |
| CAND-27 | Xác nhận nhận chỗ từ danh sách chờ | Giữ thành UC-012 | - | U-R13: phiên riêng, thời điểm khác UC-011 (hội viên được thông báo rồi mới thao tác) | REQ-28, REQ-29 | Mục tiêu (EV-10) |
| CAND-28 | Chuyển chỗ cho người kế tiếp khi quá 30 phút | Giữ thành UC-013 | - | U-R07: mốc 30 phút sau thông báo, lúc đó không còn phiên nào của tác nhân đang mở (P01 ACT-14); Q-43 chưa trả lời không đổi việc UC tồn tại | REQ-30, REQ-31 | Sự kiện (EV-11) |
| CAND-29 | Ghi nhận vắng mặt lớp nhóm | Giữ thành UC-016 | - | U-R07: mốc 10 phút sau giờ bắt đầu lớp; kết quả có giá trị nghiệp vụ cho VietFit và hội viên | REQ-34, REQ-35 | Sự kiện (EV-12) |
| CAND-30 | Khoá quyền đặt lớp 7 ngày khi đạt 3 lần vắng mặt trong 30 ngày | Là bước của UC-016 | U-T9, U-AP11 | U-R09: hệ quả của việc ghi nhận vắng mặt | REQ-36, REQ-37, REQ-38 | Động từ |
| CAND-31 | Mở lại quyền đặt lớp sau 7 ngày | Là bước của UC-010 | U-T9, U-AP11 | Điều kiện kiểm tra khi hội viên đặt chỗ; P01 xếp mốc này là điều kiện tính theo ngày (A-T4), nguồn không nêu chức năng | REQ-38 | Động từ |
| CAND-32 | Vào chi nhánh bằng mã QR hiển thị trên ứng dụng | Giữ thành UC-018 | - | U-R18: người quét mã có mục tiêu nên là tác nhân chính, cửa quay (ACT-12) là tác nhân phụ; U-R11: nối cả ACT-02 và ACT-03 | REQ-39, REQ-40, REQ-41 | Mục tiêu (EV-13) |
| CAND-33 | Vào chi nhánh bằng mã QR trên vé tập một ngày | Gộp vào UC-018 | U-T11, U-AP15 | U-R11, U-R12: cùng mục tiêu và luồng, khác loại mã và điều kiện kiểm tra; khác biệt là luồng thay thế | REQ-44, REQ-45 | Mục tiêu (EV-14) |
| CAND-34 | Hiển thị mã QR trên ứng dụng | Là bước của UC-018 | U-T12, U-AP02 | Giao diện phục vụ mục tiêu vào chi nhánh | REQ-39 | Động từ |
| CAND-35 | Kiểm tra gói tập còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh khi cửa quay hỏi | Là bước của UC-018 | U-T9, U-AP03 | Kiểm tra nội bộ trong UC-018 | REQ-41 | Động từ |
| CAND-36 | Bảo lưu gói tập | Giữ thành UC-006 | - | U-R04 b: giao dịch nghiệp vụ có quy tắc riêng; kênh thực hiện chờ Q-48 | REQ-46, REQ-47, REQ-48, REQ-49, REQ-50 | Mục tiêu (EV-15) |
| CAND-37 | Lùi ngày hết hạn gói theo số ngày bảo lưu | Là bước của UC-006 | U-T9, U-AP03 | Hệ quả của bảo lưu | REQ-51 | Động từ |
| CAND-38 | Mua gói buổi tập cá nhân | Giữ thành UC-019 | - | U-R12: tách khỏi UC-005 vì quy tắc riêng nguồn mô tả (10 hoặc 20 buổi, 90 ngày, gắn một huấn luyện viên); kênh mua chờ Q-07 | REQ-56, REQ-57, REQ-58 | Mục tiêu (EV-18) |
| CAND-39 | Đặt buổi tập cá nhân | Giữ thành UC-020 | - | U-R13: phiên riêng, huấn luyện viên phản hồi ở phiên khác (CAND-43) | REQ-59 | Mục tiêu (EV-19) |
| CAND-40 | Chọn khung giờ trống trong lịch làm việc của huấn luyện viên | Là bước của UC-020 | U-T1, U-AP01 | Bước chọn của UC-020 | REQ-59 | Động từ |
| CAND-41 | Huỷ buổi tập cá nhân | Giữ thành UC-023 | - | U-R04 b: giao dịch nghiệp vụ có quy tắc huỷ trước 12 giờ | REQ-63, REQ-64 | Mục tiêu (EV-22) |
| CAND-42 | Xem chỉ số cơ thể của mình | Giữ thành UC-025 | - | U-R05, U-R11: mục tiêu thông tin độc lập của hội viên; gộp CAND-47; miễn U-T4 | REQ-68 | Mục tiêu (EV-24) |
| CAND-43 | Xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân | Giữ thành UC-021 | - | U-R13: phiên của huấn luyện viên, khác thời điểm với CAND-39; xác nhận và từ chối là hai kết cục của cùng mục tiêu phản hồi yêu cầu (U-R12) | REQ-60, REQ-61 | Mục tiêu (EV-20) |
| CAND-44 | Huỷ yêu cầu đặt buổi tập cá nhân quá hạn 12 giờ chưa được phản hồi | Giữ thành UC-022 | - | U-R07: hạn 12 giờ của huấn luyện viên, lúc hết hạn không còn phiên nào của tác nhân chính đang mở (P01 ACT-14) | REQ-61, REQ-62 | Sự kiện (EV-21) |
| CAND-45 | Ghi nhận buổi tập cá nhân | Giữ thành UC-024 | - | Gộp CAND-46 (mục 7.1) | REQ-65 | Mục tiêu (EV-23) |
| CAND-46 | Ghi nhận chỉ số cơ thể của hội viên | Gộp vào UC-024 | U-T11, U-AP12 | Cùng tác nhân, cùng thời điểm (sau mỗi buổi), cùng mục tiêu; chỉ khác dữ liệu ghi nhận | REQ-66, REQ-67 | Mục tiêu (EV-23) |
| CAND-47 | Xem chỉ số cơ thể của hội viên mình phụ trách | Gộp vào UC-025 | U-T11, U-AP12 | U-R11: cùng thông tin, hai tác nhân được phép xem | REQ-68 | Mục tiêu (EV-24) |
| CAND-48 | Chuyển nhượng gói tập tại quầy | Giữ thành UC-007 | - | U-R10: lễ tân thao tác trực tiếp nên là tác nhân chính; hội viên chuyển và người nhận là bên liên quan | REQ-52, REQ-53 | Mục tiêu (EV-16) |
| CAND-49 | Thu phí chuyển nhượng 200.000 đồng | Là bước của UC-007 | U-T1, U-T4, U-AP01 | Q4 d không thoả: nguồn không mô tả như phần tách bạch; hình thức thu chờ Q-38 | REQ-54, REQ-55 | Động từ |
| CAND-50 | Bán vé tập một ngày | Giữ thành UC-017 | - | U-R10: lễ tân thao tác trực tiếp nên là tác nhân chính; khách vãng lai là bên liên quan | REQ-42, REQ-44, REQ-45 | Mục tiêu (EV-17) |
| CAND-51 | In vé tập một ngày có mã QR | Là bước của UC-017 | U-T1, U-AP01 | Bước của UC-017; cách in chờ Q-44 | REQ-43 | Động từ |
| CAND-52 | Lập lịch lớp nhóm hằng tuần | Giữ thành UC-009 | - | Danh mục đầu vào (phòng, loại lớp, huấn luyện viên) chờ Q-03, Q-04, Q-05 | REQ-69, REQ-70, REQ-71, REQ-72 | Mục tiêu (EV-25) |
| CAND-53 | Huỷ lớp nhóm vì sự cố | Giữ thành UC-014 | - | Tác nhân chính ACT-06, tách khỏi CAND-55 vì tác nhân chính và sự kiện khác (U-R07) | REQ-76 | Mục tiêu (EV-26) |
| CAND-54 | Gửi thông báo huỷ lớp cho người đã đặt và người trong danh sách chờ | Là bước của UC-014 | U-T9, U-AP03 | U-R06: hệ quả của huỷ lớp; ACT-09, ACT-10 là tác nhân phụ | REQ-77 | Động từ |
| CAND-55 | Huỷ lớp nhóm có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học | Giữ thành UC-015 | - | U-R07: mốc 2 giờ trước giờ học; Q-43 chưa trả lời không đổi việc UC tồn tại | REQ-73, REQ-74 | Sự kiện (EV-27) |
| CAND-56 | Gửi thông báo cho người đã đặt khi lớp bị tự huỷ | Là bước của UC-015 | U-T9, U-AP03 | U-R06: hệ quả của huỷ lớp; ACT-09, ACT-10 là tác nhân phụ | REQ-75 | Động từ |
| CAND-57 | Đặt giá gói tập | Giữ thành UC-026 | - | U-R15: tham số nghiệp vụ do giám đốc chuỗi đặt; nguồn chỉ nêu "đặt" nên không dùng "Quản lý" (U-R04). Phạm vi gói chờ Q-08, Q-10 | REQ-78 | Mục tiêu (EV-28) |
| CAND-58 | Đặt chương trình khuyến mãi | Giữ thành UC-027 | - | U-R04, U-R15: khuyến mãi là loại dữ liệu khác giá gói (khoảng ngày, mức giảm), mỗi loại một UC. Cách áp dụng chờ Q-09 | REQ-79, REQ-80 | Mục tiêu (EV-29) |
| CAND-59 | Xem báo cáo doanh thu theo chi nhánh và theo tháng | Giữ thành UC-028 | - | U-R05: gộp CAND-60, CAND-61 vì cùng tác nhân, cùng cách thao tác (chọn kỳ, tiêu chí, xem kết quả), chỉ khác nội dung dữ liệu | REQ-81 | Mục tiêu (EV-30) |
| CAND-60 | Xem báo cáo tỉ lệ lấp đầy lớp nhóm | Gộp vào UC-028 | U-T11, U-AP12 | U-R05: cùng tác nhân, chỉ khác nội dung báo cáo; công thức chờ Q-33 | REQ-82 | Mục tiêu (EV-30) |
| CAND-61 | Xem báo cáo số buổi tập cá nhân của huấn luyện viên | Gộp vào UC-028 | U-T11, U-AP12 | U-R05: cùng tác nhân, chỉ khác nội dung báo cáo; cách tính chờ Q-34 | REQ-83 | Mục tiêu (EV-30) |
| CAND-62 | Tính thù lao huấn luyện viên | Loại | U-T10 | U-R16: "Việc tính thù lao huấn luyện viên làm ngoài phần mềm" (project-profile.md mục 4) | REQ-83 | Mục tiêu |
| CAND-63 | Nhắc gia hạn gói tập | Giữ thành UC-008 | - | U-R06, U-R07: nhắc theo lịch, tác nhân chính ACT-13, kênh gửi là tác nhân phụ; hội viên nhận nhắc là bên hưởng lợi. Tần suất chờ Q-35 | REQ-84, REQ-85, REQ-86 | Sự kiện (EV-31) |
| CAND-64 | Gửi thông báo qua thông báo đẩy | Là bước của UC-008, UC-011, UC-014, UC-015 | U-T9, U-AP03 | U-R06: kênh gửi dùng chung của các UC phát sinh thông báo; ACT-10 là tác nhân phụ | REQ-87, REQ-89 | Động từ |
| CAND-65 | Gửi SMS cho hội viên chưa cài ứng dụng | Là bước của UC-008, UC-011, UC-014, UC-015 | U-T9, U-AP03 | U-R06: kênh gửi dùng chung của các UC phát sinh thông báo; ACT-09 là tác nhân phụ. Cách xác định "chưa cài ứng dụng" chờ Q-36 | REQ-88, REQ-90 | Động từ |
| CAND-66 | Quản lý danh mục chi nhánh, phòng tập và sức chứa | Chờ Q-03 | - | Q-03 nêu được người tạo thì thành UC "Quản lý <danh mục phòng tập>" (U-R04) của người đó; chưa nêu thì không tự thêm | REQ-01, REQ-25, REQ-69, REQ-71 | Mục tiêu |
| CAND-67 | Quản lý danh mục loại lớp | Chờ Q-04 | - | Q-04 trả lời "Mở rộng được" và nêu người quản lý thì thành UC (U-R04); trả lời "Cố định ba loại" thì loại | REQ-05, REQ-69, REQ-70 | Mục tiêu |
| CAND-68 | Quản lý tài khoản nhân viên và hồ sơ huấn luyện viên | Chờ Q-05 | - | Q-05 nêu được người quản lý thì thành UC (U-R15) của người đó, cần tác nhân tương ứng ở P01 | REQ-03, REQ-60, REQ-69, REQ-78 | Mục tiêu |
| CAND-69 | Lập lịch làm việc của huấn luyện viên | Chờ Q-06 | - | Q-06 nêu được người lập lịch thì thành UC của người đó; lịch này là đầu vào của UC-020 | REQ-59 | Mục tiêu |
| CAND-70 | Đặt chỗ lớp nhóm, huỷ chỗ, vào danh sách chờ và nhận chỗ khi có người huỷ | Tách thành CAND-19, CAND-20, CAND-25, CAND-27 | U-T1, U-T6, U-AP04, U-AP05 | Mức Summary: nhiều phiên, nhiều thời điểm, có chờ thông báo; dùng làm khung | REQ-22, REQ-26, REQ-27, REQ-28, REQ-32 | Mục tiêu (P01 ACT-02) |
| CAND-71 | Mua gói buổi tập cá nhân, đặt và huỷ buổi tập | Tách thành CAND-38, CAND-39, CAND-41 | U-T1, U-T6, U-AP04, U-AP05 | Mức Summary: ba mục tiêu ở ba thời điểm, huấn luyện viên phản hồi ở phiên khác; dùng làm khung | REQ-56, REQ-59, REQ-63 | Mục tiêu (P01 ACT-02) |

## 4. Bảng use case

### Bảng 4a. Bảng lõi

| UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mức | Nhóm chức năng |
|---|---|---|---|---|---|---|
| UC-001 | Xem giá gói tập | View Package Prices | ACT-01 Người quan tâm | - | User-goal | Tiếp cận và tài khoản |
| UC-002 | Xem lịch lớp nhóm | View Class Schedule | ACT-01 | - | User-goal | Tiếp cận và tài khoản |
| UC-003 | Đăng ký tài khoản hội viên | Register Member Account | ACT-01 | - | User-goal | Tiếp cận và tài khoản |
| UC-004 | Đăng nhập | Log In | ACT-02 Hội viên | - | Subfunction | Tiếp cận và tài khoản |
| UC-005 | Mua hoặc gia hạn gói tập | Purchase Or Renew Membership Package | ACT-02, ACT-05 Lễ tân | ACT-08 Cổng thanh toán, ACT-11 Hệ thống hoá đơn điện tử | User-goal | Gói tập |
| UC-006 | Bảo lưu gói tập | Freeze Membership Package | ACT-02 | - | User-goal | Gói tập |
| UC-007 | Chuyển nhượng gói tập | Transfer Membership Package | ACT-05 | ACT-11 | User-goal | Gói tập |
| UC-008 | Nhắc gia hạn gói tập | Remind Package Renewal | ACT-13 Bộ định thời hằng ngày | ACT-09 Cổng SMS, ACT-10 Dịch vụ thông báo đẩy | User-goal | Gói tập |
| UC-009 | Lập lịch lớp nhóm | Schedule Group Classes | ACT-06 Quản lý chi nhánh | - | User-goal | Lớp nhóm |
| UC-010 | Đặt chỗ lớp nhóm | Book Class Spot | ACT-02 | - | User-goal | Lớp nhóm |
| UC-011 | Huỷ chỗ lớp nhóm | Cancel Class Booking | ACT-02 | ACT-09, ACT-10 | User-goal | Lớp nhóm |
| UC-012 | Nhận chỗ từ danh sách chờ | Claim Waitlist Spot | ACT-02 | - | User-goal | Lớp nhóm |
| UC-013 | Chuyển chỗ cho người kế tiếp | Pass Spot To Next Person | ACT-14 Bộ định thời theo hạn | - | User-goal | Lớp nhóm |
| UC-014 | Huỷ lớp nhóm vì sự cố | Cancel Class Due To Incident | ACT-06 | ACT-09, ACT-10 | User-goal | Lớp nhóm |
| UC-015 | Huỷ lớp nhóm ít người đặt | Cancel Under-Booked Class | ACT-14 | ACT-09, ACT-10 | User-goal | Lớp nhóm |
| UC-016 | Ghi nhận vắng mặt lớp nhóm | Record Class Absence | ACT-14 | - | User-goal | Lớp nhóm |
| UC-017 | Bán vé tập một ngày | Sell Day Pass | ACT-05 | ACT-11 | User-goal | Ra vào chi nhánh |
| UC-018 | Vào chi nhánh | Enter Branch | ACT-02, ACT-03 Khách vãng lai | ACT-12 Cửa quay | User-goal | Ra vào chi nhánh |
| UC-019 | Mua gói buổi tập cá nhân | Purchase Personal Training Package | ACT-02 | ACT-11 | User-goal | Huấn luyện cá nhân |
| UC-020 | Đặt buổi tập cá nhân | Book Personal Training Session | ACT-02 | - | User-goal | Huấn luyện cá nhân |
| UC-021 | Phản hồi yêu cầu đặt buổi tập | Respond To Training Session Request | ACT-04 Huấn luyện viên | - | User-goal | Huấn luyện cá nhân |
| UC-022 | Huỷ yêu cầu đặt buổi quá hạn | Cancel Expired Session Request | ACT-14 | - | User-goal | Huấn luyện cá nhân |
| UC-023 | Huỷ buổi tập cá nhân | Cancel Personal Training Session | ACT-02 | - | User-goal | Huấn luyện cá nhân |
| UC-024 | Ghi nhận buổi tập cá nhân | Record Training Session | ACT-04 | - | User-goal | Huấn luyện cá nhân |
| UC-025 | Xem chỉ số cơ thể | View Body Metrics | ACT-02, ACT-04 | - | User-goal | Huấn luyện cá nhân |
| UC-026 | Đặt giá gói tập | Set Package Prices | ACT-07 Giám đốc chuỗi | - | User-goal | Giá và báo cáo |
| UC-027 | Đặt chương trình khuyến mãi | Set Promotion | ACT-07 | - | User-goal | Giá và báo cáo |
| UC-028 | Xem báo cáo chuỗi | View Chain Reports | ACT-07 | - | User-goal | Giá và báo cáo |

### Bảng 4b. Bảng mô tả

| UC | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | REQ | CAND nguồn |
|---|---|---|---|---|---|
| UC-001 | Người quan tâm biết được giá và quy cách các gói tập để quyết định có đăng ký hay không. | Người quan tâm xem giá các gói tập (thời hạn 1, 3, 6 hoặc 12 tháng, loại một chi nhánh hoặc toàn chuỗi) mà không cần tài khoản. Hội viên xem giá khi mua gói là bước của UC-005; hội viên có xem độc lập hay không chờ Q-46. | Người quan tâm muốn biết giá các gói tập (EV-01) | REQ-06, REQ-09, REQ-10 | CAND-01 |
| UC-002 | Người quan tâm biết được các lớp nhóm đang mở để quyết định có đăng ký hay không. | Người quan tâm xem lịch các lớp nhóm mà không cần tài khoản. Hội viên xem lịch khi đặt chỗ là bước của UC-010; hội viên có xem độc lập hay không chờ Q-46. | Người quan tâm muốn biết lịch các lớp nhóm (EV-02) | REQ-07 | CAND-02 |
| UC-003 | Người quan tâm có tài khoản hội viên để mua gói và đặt lớp. | Người quan tâm đăng ký tài khoản hội viên bằng số điện thoại và họ tên. | Người quan tâm muốn trở thành hội viên (EV-03) | REQ-08 | CAND-03 |
| UC-004 | Hội viên được xác nhận danh tính để dùng các chức năng của tài khoản mình. | Hội viên xác thực để dùng các chức năng dành cho người có tài khoản. Mức Subfunction giữ theo U-R01: là điều kiện để dùng các UC mà ACT-02 là tác nhân chính, không nối include. Huấn luyện viên, lễ tân, quản lý chi nhánh, giám đốc chuỗi chưa nối, chờ Q-47. | Hội viên muốn dùng các chức năng chỉ dành cho người có tài khoản (EV-04) | REQ-06, REQ-07, REQ-08 | CAND-04 |
| UC-005 | Hội viên có gói tập đã thanh toán và được kích hoạt; khi mua tại quầy, khách có gói tập đã thu tiền. | Hội viên mua gói tập mới hoặc gia hạn gói đang có và thanh toán qua cổng thanh toán trực tuyến (đơn chưa thanh toán thành công trong 15 phút thì bị huỷ, đó là luồng thay thế theo U-R07), hoặc lễ tân bán gói tại quầy và thu tiền mặt hoặc nhập mã giao dịch POS. Gia hạn khi gói cũ còn hiệu lực thì gói mới bắt đầu sau ngày hết hạn gói cũ. Giao dịch thu tiền được gửi sang hệ thống hoá đơn điện tử (Q-37). | Hội viên muốn mua hoặc gia hạn gói tập (EV-05); khách đến quầy muốn mua gói tập (EV-06) | REQ-09, REQ-10, REQ-11, REQ-12, REQ-13, REQ-14, REQ-15, REQ-16, REQ-17, REQ-18, REQ-19, REQ-20, REQ-21, REQ-91, REQ-92 | CAND-05, CAND-06, CAND-07, CAND-08, CAND-09, CAND-10, CAND-11, CAND-12, CAND-16 |
| UC-006 | Hội viên có gói được tạm dừng trong thời gian đã đăng ký và ngày hết hạn lùi tương ứng. | Hội viên có gói từ 3 tháng trở lên đăng ký bảo lưu gói một lần cho mỗi gói, từ 7 đến 30 ngày, trước ngày bắt đầu ít nhất 1 ngày; ngày hết hạn của gói lùi thêm đúng số ngày bảo lưu. Kênh thực hiện chờ Q-48; quan hệ với gói buổi tập cá nhân chờ Q-17, Q-19. | Hội viên muốn bảo lưu gói tập (EV-15) | REQ-46, REQ-47, REQ-48, REQ-49, REQ-50, REQ-51 | CAND-36, CAND-37 |
| UC-007 | Người nhận có gói tập chuyển nhượng và VietFit thu phí chuyển nhượng. | Lễ tân chuyển gói còn ít nhất 30 ngày của một hội viên cho người khác đã có tài khoản, khi có mặt cả hai người tại quầy, và thu phí chuyển nhượng 200.000 đồng. Hội viên chuyển và người nhận là bên liên quan (P01 SH-02), không tương tác trực tiếp. Hình thức thu phí chờ Q-38; phạm vi gói chờ Q-17. | Hội viên và người nhận đến quầy muốn chuyển nhượng gói (EV-16) | REQ-52, REQ-53, REQ-54, REQ-55, REQ-91, REQ-92 | CAND-16, CAND-48, CAND-49 |
| UC-008 | Hội viên có gói hết hạn trong 7 ngày tới nhận được lời nhắc gia hạn. | Mỗi ngày lúc 8 giờ sáng, bộ định thời kích hoạt việc gửi nhắc gia hạn qua thông báo đẩy, hoặc SMS cho hội viên chưa cài ứng dụng, tới hội viên có gói hết hạn trong 7 ngày tới. Hội viên nhận nhắc là bên hưởng lợi (U-R06). Tần suất và đối tượng đã gia hạn chờ Q-35. | Đến 8 giờ sáng mỗi ngày (EV-31) | REQ-84, REQ-85, REQ-86, REQ-87, REQ-88, REQ-89, REQ-90 | CAND-63, CAND-64, CAND-65 |
| UC-009 | Quản lý chi nhánh có lịch lớp nhóm của tuần đã xếp đủ loại lớp, phòng, huấn luyện viên và giờ, không trùng. | Quản lý chi nhánh lập lịch lớp nhóm hằng tuần: chọn loại lớp, phòng, huấn luyện viên và giờ; một phòng hoặc một huấn luyện viên không được xếp hai lớp trùng giờ. Danh mục phòng, loại lớp, huấn luyện viên chờ Q-03, Q-04, Q-05; lập từng tuần hay lịch mẫu chờ Q-16; trùng giờ chờ Q-32. | Quản lý chi nhánh muốn lập lịch lớp nhóm cho tuần (EV-25) | REQ-05, REQ-25, REQ-69, REQ-70, REQ-71, REQ-72 | CAND-52 |
| UC-010 | Hội viên có chỗ trong lớp nhóm mong muốn, hoặc có vị trí trong danh sách chờ khi lớp đã đủ chỗ. | Hội viên chọn lớp nhóm và đặt chỗ, sớm nhất 7 ngày trước giờ học, tối đa 2 lớp một ngày; lớp đã đủ chỗ thì hội viên vào danh sách chờ (luồng thay thế). Số chỗ đã đặt của lớp không vượt sức chứa kể cả khi nhiều hội viên đặt cùng lúc. Cách mở đặt chỗ chờ Q-11; điều kiện về gói chờ Q-12. | Hội viên muốn đặt chỗ một lớp nhóm (EV-08) | REQ-22, REQ-23, REQ-24, REQ-25, REQ-26, REQ-38, REQ-93, REQ-94, REQ-95 | CAND-19, CAND-20, CAND-21, CAND-22, CAND-31 |
| UC-011 | Hội viên không còn giữ chỗ trong lớp đã huỷ; hội viên đứng đầu danh sách chờ (nếu có) được thông báo có chỗ trống. | Hội viên huỷ chỗ lớp nhóm đã đặt, chậm nhất 2 giờ trước giờ học; hệ thống thông báo cho hội viên đứng đầu danh sách chờ qua thông báo đẩy hoặc SMS. | Hội viên muốn huỷ chỗ lớp đã đặt (EV-09) | REQ-27, REQ-32, REQ-33, REQ-87, REQ-88, REQ-89, REQ-90 | CAND-25, CAND-26, CAND-64, CAND-65 |
| UC-012 | Hội viên đứng đầu danh sách chờ có chỗ trong lớp vốn đã đủ chỗ. | Hội viên được thông báo có chỗ xem lại lớp và xác nhận nhận chỗ trong 30 phút. Chỗ trống có được giữ riêng hay không chờ Q-22. | Hội viên đứng đầu danh sách chờ muốn nhận chỗ trong 30 phút sau thông báo (EV-10) | REQ-28, REQ-29 | CAND-27 |
| UC-013 | Hội viên kế tiếp trong danh sách chờ có cơ hội nhận chỗ khi hội viên trước không xác nhận kịp. | Quá 30 phút kể từ thông báo mà hội viên chưa xác nhận thì chỗ chuyển cho người kế tiếp trong danh sách chờ; không chuyển khi còn dưới 1 giờ trước giờ học. Số phận hội viên không xác nhận chờ Q-23; người kế tiếp có được thông báo như người đứng đầu chờ Q-49 (nếu có thì thêm tác nhân phụ ACT-09, ACT-10); nhân viên can thiệp được không chờ Q-43. | Hết 30 phút kể từ thông báo nhận chỗ mà hội viên chưa xác nhận (EV-11) | REQ-30, REQ-31 | CAND-28 |
| UC-014 | Mọi người đã đặt chỗ và người trong danh sách chờ của lớp bị huỷ biết lớp đã huỷ. | Quản lý chi nhánh huỷ lớp nhóm vì sự cố; hệ thống thông báo cho mọi người đã đặt chỗ và người trong danh sách chờ qua thông báo đẩy hoặc SMS. | Sự cố khiến quản lý chi nhánh phải huỷ lớp (EV-26) | REQ-76, REQ-77, REQ-87, REQ-88, REQ-89, REQ-90 | CAND-53, CAND-54, CAND-64, CAND-65 |
| UC-015 | Những hội viên đã đặt chỗ trong lớp có dưới 3 người đặt biết lớp đã bị huỷ. | Lúc 2 giờ trước giờ học, lớp có dưới 3 người đặt chỗ thì hệ thống tự huỷ lớp và thông báo cho những người đã đặt. Có bước nhân viên duyệt hoặc gỡ hay không chờ Q-43. | Đến 2 giờ trước giờ học, lớp có dưới 3 người đặt chỗ (EV-27) | REQ-73, REQ-74, REQ-75, REQ-87, REQ-88, REQ-89, REQ-90 | CAND-55, CAND-56, CAND-64, CAND-65 |
| UC-016 | Hội viên đặt chỗ mà không vào lớp bị tính vắng mặt, và bị khoá quyền đặt lớp khi đạt ngưỡng. | Mười phút sau giờ bắt đầu lớp, hệ thống tính một lần vắng mặt cho hội viên đã đặt chỗ mà không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu; đạt 3 lần vắng mặt trong 30 ngày thì khoá quyền đặt lớp 7 ngày. Chỗ đã đặt khi bị khoá chờ Q-20; cách đếm sau khi khoá chờ Q-21. | Hết 10 phút sau giờ bắt đầu lớp mà hội viên đặt chỗ chưa quẹt vào cửa (EV-12) | REQ-34, REQ-35, REQ-36, REQ-37, REQ-38 | CAND-29, CAND-30 |
| UC-017 | Khách vãng lai có vé tập một ngày có mã QR dùng được trong ngày tại chi nhánh đã mua. | Lễ tân bán vé tập một ngày cho khách vãng lai tại quầy và in vé có mã QR. Hình thức thu tiền chờ Q-38; cách in chờ Q-44; người đặt giá vé chờ Q-08. | Khách vãng lai đến quầy muốn mua vé tập một ngày (EV-17) | REQ-42, REQ-43, REQ-44, REQ-45, REQ-91, REQ-92 | CAND-16, CAND-50, CAND-51 |
| UC-018 | Hội viên hoặc khách vãng lai hợp lệ đi qua cửa quay vào chi nhánh. | Hội viên quét mã QR hiển thị trên ứng dụng, khách vãng lai quét mã QR trên vé, tại cửa quay; cửa quay hỏi phần mềm và chỉ mở khi hợp lệ (hội viên: gói còn hiệu lực, không đang bảo lưu, áp dụng cho chi nhánh; khách vãng lai: vé dùng trong ngày tại chi nhánh đã mua). Lượt quẹt vào cửa là căn cứ xác định vắng mặt (UC-016); số lần dùng vé trong ngày chờ Q-40. | Hội viên quét mã QR tại cửa quay (EV-13); khách vãng lai quét mã QR trên vé tại cửa quay (EV-14) | REQ-35, REQ-39, REQ-40, REQ-41, REQ-44, REQ-45, REQ-96 | CAND-32, CAND-33, CAND-34, CAND-35 |
| UC-019 | Hội viên có gói buổi tập cá nhân với một huấn luyện viên. | Hội viên mua gói 10 hoặc 20 buổi tập cá nhân dùng trong 90 ngày với một huấn luyện viên. Kênh mua và hình thức thanh toán chờ Q-07; mốc tính 90 ngày chờ Q-26; bảo lưu, chuyển nhượng chờ Q-17. | Hội viên muốn mua gói buổi tập cá nhân (EV-18) | REQ-56, REQ-57, REQ-58, REQ-91, REQ-92 | CAND-16, CAND-38 |
| UC-020 | Hội viên có yêu cầu đặt buổi tập cá nhân vào khung giờ đã chọn, chờ huấn luyện viên phản hồi. | Hội viên chọn khung giờ trống trong lịch làm việc của huấn luyện viên để đặt buổi tập. Người lập lịch làm việc chờ Q-06; thời lượng khung giờ chờ Q-32. | Hội viên muốn đặt buổi tập cá nhân (EV-19) | REQ-59 | CAND-39, CAND-40 |
| UC-021 | Yêu cầu đặt buổi tập cá nhân được huấn luyện viên xác nhận hoặc từ chối. | Huấn luyện viên xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân trong 12 giờ. Cách huấn luyện viên được báo có yêu cầu chờ Q-15; xử lý khi từ chối chờ Q-30. | Huấn luyện viên muốn phản hồi yêu cầu đặt buổi tập cá nhân trong 12 giờ (EV-20) | REQ-60, REQ-61 | CAND-43 |
| UC-022 | Yêu cầu đặt buổi chưa được huấn luyện viên xác nhận hoặc từ chối trong 12 giờ bị huỷ. | Hết 12 giờ mà huấn luyện viên chưa xác nhận hoặc từ chối thì yêu cầu đặt buổi tự huỷ. Mốc bắt đầu 12 giờ nguồn chưa nêu; hội viên có được báo hay không chờ Q-15; nhân viên gỡ được không chờ Q-43. | Hết 12 giờ mà huấn luyện viên chưa xác nhận hoặc từ chối (EV-21) | REQ-61, REQ-62 | CAND-44 |
| UC-023 | Hội viên huỷ được buổi tập đã đặt và không bị trừ buổi khi huỷ sớm. | Hội viên huỷ buổi tập cá nhân đã đặt; huỷ trước 12 giờ thì không bị trừ buổi. Nghĩa của "trước 12 giờ" chờ Q-27; huỷ muộn hơn chờ Q-28. | Hội viên muốn huỷ buổi tập cá nhân đã đặt (EV-22) | REQ-63, REQ-64 | CAND-41 |
| UC-024 | Buổi tập cá nhân và chỉ số cơ thể của hội viên được ghi nhận. | Sau mỗi buổi, huấn luyện viên ghi nhận buổi tập cá nhân đã diễn ra và chỉ số cơ thể của hội viên (cân nặng, tỉ lệ mỡ). Nội dung ghi nhận ngoài chỉ số chờ Q-31; thời điểm trừ buổi chờ Q-29. | Buổi tập cá nhân đã diễn ra, huấn luyện viên muốn ghi nhận (EV-23) | REQ-65, REQ-66, REQ-67 | CAND-45, CAND-46 |
| UC-025 | Hội viên và huấn luyện viên phụ trách xem được chỉ số cơ thể, không ai khác xem được. | Hội viên xem chỉ số cơ thể của chính mình; huấn luyện viên phụ trách xem chỉ số của hội viên mình phụ trách. | Hội viên hoặc huấn luyện viên phụ trách muốn xem chỉ số cơ thể (EV-24) | REQ-67, REQ-68 | CAND-42, CAND-47 |
| UC-026 | Giám đốc chuỗi có giá các gói được áp dụng trong chuỗi. | Giám đốc chuỗi đặt giá các gói. Loại gói thuộc phạm vi chờ Q-08; hiệu lực theo khoảng ngày chờ Q-10. | Giám đốc chuỗi muốn đặt giá các gói (EV-28) | REQ-09, REQ-10, REQ-78 | CAND-57 |
| UC-027 | Giám đốc chuỗi có chương trình khuyến mãi áp dụng trong khoảng ngày đã chọn. | Giám đốc chuỗi đặt chương trình khuyến mãi theo khoảng ngày, giảm tối đa 20% giá gói. Cách áp dụng cho người mua chờ Q-09; loại gói thuộc phạm vi chờ Q-08. | Giám đốc chuỗi muốn đặt chương trình khuyến mãi (EV-29) | REQ-79, REQ-80 | CAND-58 |
| UC-028 | Giám đốc chuỗi nắm được doanh thu, mức lấp đầy lớp nhóm và số buổi tập cá nhân của từng huấn luyện viên. | Giám đốc chuỗi xem báo cáo doanh thu theo chi nhánh và theo tháng, tỉ lệ lấp đầy lớp nhóm, số buổi tập cá nhân của từng huấn luyện viên. Công thức và kỳ chờ Q-33, Q-34; việc tính thù lao nằm ngoài phạm vi. | Giám đốc chuỗi muốn xem báo cáo (EV-30) | REQ-81, REQ-82, REQ-83 | CAND-59, CAND-60, CAND-61 |

## 5. Ma trận truy vết REQ --> UC

| REQ | Nội dung tóm tắt | UC phủ | Ghi chú (lý do nếu không phủ) |
|---|---|---|---|
| REQ-01 | Hệ thống quản lý 4 chi nhánh trong thành phố. | - | Chuyển P06 (số liệu quy mô). CAND-66 chờ Q-03 |
| REQ-02 | Hệ thống quản lý khoảng 6.000 hội viên. | - | Chuyển P06 (số liệu quy mô). CAND-15 chờ Q-02 |
| REQ-03 | Hệ thống quản lý 40 huấn luyện viên. | - | Chuyển P06 (số liệu quy mô). CAND-68 chờ Q-05 |
| REQ-04 | Mỗi chi nhánh mở khoảng 25 lớp tập nhóm mỗi ngày. | - | Chuyển P06 (số liệu quy mô) |
| REQ-05 | Lớp tập nhóm gồm các loại yoga, aerobic, đạp xe trong nhà. | UC-009 | CAND-67 chờ Q-04 về người quản lý danh mục loại lớp |
| REQ-06 | Người quan tâm có thể xem bảng giá gói tập trên ứng dụng di động mà không cần tài khoản. | UC-001, UC-004 | UC-004: căn cứ xác thực (U-R01) |
| REQ-07 | Người quan tâm có thể xem lịch lớp nhóm trên ứng dụng di động mà không cần tài khoản. | UC-002, UC-004 | UC-004: căn cứ xác thực (U-R01) |
| REQ-08 | Người quan tâm có thể đăng ký tài khoản hội viên bằng số điện thoại và họ tên. | UC-003, UC-004 | UC-004: căn cứ xác thực (U-R01). CAND-14 chờ Q-01 |
| REQ-09 | Gói tập có thời hạn 1, 3, 6 hoặc 12 tháng. | UC-001, UC-005, UC-026 | - |
| REQ-10 | Gói tập thuộc một trong hai loại: áp dụng cho một chi nhánh, hoặc áp dụng cho toàn chuỗi. | UC-001, UC-005, UC-026 | - |
| REQ-11 | Hội viên có thể mua gói tập trên ứng dụng. | UC-005 | - |
| REQ-12 | Hội viên có thể gia hạn gói tập trên ứng dụng. | UC-005 | - |
| REQ-13 | Hội viên có thể thanh toán đơn mua hoặc đơn gia hạn gói tập qua cổng thanh toán trực tuyến của đối tác. | UC-005 | - |
| REQ-14 | Hệ thống trao đổi thông tin đơn mua và kết quả thanh toán với cổng thanh toán trực tuyến của đối tác để thu tiền đơn mua gói tập. | UC-005 | CAND-13 chờ Q-45 về chiều gửi kết quả thanh toán |
| REQ-15 | Hệ thống huỷ đơn mua gói tập chưa thanh toán thành công. | UC-005 | - |
| REQ-16 | Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ. | UC-005 | - |
| REQ-17 | Khi hội viên gia hạn lúc gói cũ còn hiệu lực, gói mới bắt đầu ngay sau ngày hết hạn của gói cũ. | UC-005 | - |
| REQ-18 | Lễ tân có thể bán gói tập tại quầy. | UC-005 | - |
| REQ-19 | Lễ tân có thể thu tiền mặt khi bán gói tập tại quầy. | UC-005 | - |
| REQ-20 | Lễ tân có thể nhập mã giao dịch in trên hoá đơn POS vào hệ thống khi bán gói tập tại quầy và thu tiền bằng thẻ ngân hàng qua máy POS của ngân hàng. | UC-005 | Máy POS ngoài phạm vi (CAND-18) |
| REQ-21 | Hệ thống nhận mã giao dịch của máy POS ngân hàng do lễ tân nhập tay, không có kết nối trực tiếp với máy POS. | UC-005 | Giao tiếp ngoài không có thiết bị kết nối; lễ tân nhập mã (UC-005) |
| REQ-22 | Hội viên có thể đặt chỗ lớp nhóm trên ứng dụng. | UC-010 | - |
| REQ-23 | Hội viên được đặt chỗ lớp nhóm sớm nhất 7 ngày trước giờ học. | UC-010 | Mâu thuẫn với REQ-93, chờ Q-11 |
| REQ-24 | Hội viên được đặt chỗ tối đa 2 lớp trong một ngày. | UC-010 | - |
| REQ-25 | Sức chứa của mỗi lớp nhóm được xác định theo phòng. | UC-009, UC-010 | CAND-66 chờ Q-03 về người tạo danh mục phòng và sức chứa |
| REQ-26 | Hội viên có thể vào danh sách chờ của lớp nhóm đã đủ chỗ. | UC-010 | - |
| REQ-27 | Hệ thống gửi thông báo cho hội viên đứng đầu danh sách chờ của lớp nhóm khi có người huỷ chỗ. | UC-011 | - |
| REQ-28 | Hội viên được thông báo có thể xem lại lớp và xác nhận nhận chỗ trên ứng dụng. | UC-012 | - |
| REQ-29 | Hội viên đứng đầu danh sách chờ được thông báo có 30 phút để xác nhận nhận chỗ. | UC-012 | - |
| REQ-30 | Hệ thống chuyển chỗ cho hội viên kế tiếp trong danh sách chờ khi hội viên được thông báo không xác nhận nhận chỗ đúng thời hạn. | UC-013 | - |
| REQ-31 | Hệ thống không chuyển chỗ từ danh sách chờ khi còn dưới 1 giờ trước giờ học. | UC-013 | - |
| REQ-32 | Hội viên có thể huỷ chỗ lớp nhóm đã đặt. | UC-011 | - |
| REQ-33 | Hội viên huỷ chỗ đã đặt chậm nhất 2 giờ trước giờ học. | UC-011 | - |
| REQ-34 | Hệ thống tính một lần vắng mặt cho hội viên đã đặt chỗ mà không vào lớp. | UC-016 | - |
| REQ-35 | Hội viên đặt chỗ được xem là không vào lớp khi không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu. | UC-016, UC-018 | - |
| REQ-36 | Hệ thống khoá quyền đặt lớp của hội viên khi số lần vắng mặt của hội viên đạt ngưỡng. | UC-016 | - |
| REQ-37 | Ngưỡng vắng mặt dẫn tới khoá quyền đặt lớp là 3 lần trong 30 ngày. | UC-016 | - |
| REQ-38 | Quyền đặt lớp của hội viên bị khoá trong 7 ngày. | UC-010, UC-016 | - |
| REQ-39 | Hội viên có thể vào chi nhánh qua cửa quay bằng mã QR hiển thị trên ứng dụng. | UC-018 | - |
| REQ-40 | Hệ thống trao đổi mã QR đọc được và kết quả cho phép vào với cửa quay có đầu đọc mã QR tại mỗi chi nhánh để mở cửa. | UC-018 | - |
| REQ-41 | Hệ thống cho phép cửa quay mở cho hội viên chỉ khi gói tập của hội viên còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh đó. | UC-018 | - |
| REQ-42 | Khách vãng lai có thể mua vé tập một ngày tại quầy. | UC-017 | - |
| REQ-43 | Lễ tân có thể in vé tập một ngày có mã QR cho khách vãng lai. | UC-017 | - |
| REQ-44 | Mã QR trên vé tập một ngày dùng được trong ngày mua vé. | UC-017, UC-018 | - |
| REQ-45 | Mã QR trên vé tập một ngày dùng được tại chi nhánh đã mua vé. | UC-017, UC-018 | - |
| REQ-46 | Hội viên có thể bảo lưu gói tập. | UC-006 | - |
| REQ-47 | Hội viên có gói từ 3 tháng trở lên được bảo lưu gói. | UC-006 | - |
| REQ-48 | Mỗi gói được bảo lưu một lần. | UC-006 | - |
| REQ-49 | Thời gian bảo lưu của một lần bảo lưu từ 7 đến 30 ngày. | UC-006 | - |
| REQ-50 | Hội viên đăng ký bảo lưu trước ngày bắt đầu bảo lưu ít nhất 1 ngày. | UC-006 | - |
| REQ-51 | Ngày hết hạn của gói được lùi thêm đúng số ngày bảo lưu. | UC-006 | - |
| REQ-52 | Lễ tân có thể chuyển nhượng gói tập của hội viên cho người khác đã có tài khoản tại quầy khi có mặt cả hai người. | UC-007 | - |
| REQ-53 | Gói được chuyển nhượng khi còn ít nhất 30 ngày. | UC-007 | - |
| REQ-54 | Lễ tân thu phí chuyển nhượng khi thực hiện chuyển nhượng gói tập. | UC-007 | - |
| REQ-55 | Phí chuyển nhượng gói tập là 200.000 đồng. | UC-007 | - |
| REQ-56 | Hội viên có thể mua gói buổi tập cá nhân với một huấn luyện viên. | UC-019 | - |
| REQ-57 | Gói buổi tập cá nhân có 10 buổi hoặc 20 buổi. | UC-019 | - |
| REQ-58 | Gói buổi tập cá nhân dùng trong 90 ngày. | UC-019 | - |
| REQ-59 | Hội viên có thể đặt buổi tập cá nhân bằng cách chọn khung giờ trống trong lịch làm việc của huấn luyện viên. | UC-020 | CAND-69 chờ Q-06 về người lập lịch làm việc |
| REQ-60 | Huấn luyện viên có thể xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân. | UC-021 | - |
| REQ-61 | Huấn luyện viên xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân trong 12 giờ. | UC-021, UC-022 | - |
| REQ-62 | Hệ thống tự huỷ yêu cầu đặt buổi tập cá nhân mà huấn luyện viên chưa xác nhận hoặc từ chối khi quá hạn. | UC-022 | - |
| REQ-63 | Hội viên có thể huỷ buổi tập cá nhân đã đặt. | UC-023 | - |
| REQ-64 | Hội viên huỷ buổi tập cá nhân trước 12 giờ thì không bị trừ buổi. | UC-023 | - |
| REQ-65 | Huấn luyện viên có thể ghi nhận buổi tập cá nhân sau mỗi buổi. | UC-024 | - |
| REQ-66 | Huấn luyện viên có thể ghi nhận chỉ số cơ thể của hội viên sau mỗi buổi tập cá nhân. | UC-024 | - |
| REQ-67 | Chỉ số cơ thể của hội viên gồm cân nặng và tỉ lệ mỡ. | UC-024, UC-025 | - |
| REQ-68 | Chỉ hội viên đó và huấn luyện viên phụ trách có thể xem chỉ số cơ thể của hội viên. | UC-025 | - |
| REQ-69 | Quản lý chi nhánh có thể lập lịch lớp nhóm hằng tuần. | UC-009 | - |
| REQ-70 | Lịch lớp nhóm gồm loại lớp, phòng, huấn luyện viên và giờ. | UC-009 | - |
| REQ-71 | Một phòng không được xếp hai lớp trùng giờ. | UC-009 | - |
| REQ-72 | Một huấn luyện viên không được xếp hai lớp trùng giờ. | UC-009 | - |
| REQ-73 | Hệ thống tự huỷ lớp nhóm khi số người đặt chỗ thấp hơn ngưỡng quy định. | UC-015 | - |
| REQ-74 | Lớp nhóm có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học thì bị huỷ. | UC-015 | - |
| REQ-75 | Hệ thống gửi thông báo cho những người đã đặt chỗ của lớp nhóm bị tự huỷ. | UC-015 | - |
| REQ-76 | Quản lý chi nhánh có thể huỷ lớp nhóm vì sự cố. | UC-014 | - |
| REQ-77 | Hệ thống gửi thông báo cho những người đã đặt chỗ và những người trong danh sách chờ khi quản lý chi nhánh huỷ lớp nhóm. | UC-014 | - |
| REQ-78 | Giám đốc chuỗi có thể đặt giá các gói. | UC-026 | - |
| REQ-79 | Giám đốc chuỗi có thể đặt chương trình khuyến mãi theo khoảng ngày. | UC-027 | - |
| REQ-80 | Chương trình khuyến mãi giảm tối đa 20% giá gói. | UC-027 | - |
| REQ-81 | Giám đốc chuỗi có thể xem báo cáo doanh thu theo chi nhánh và theo tháng. | UC-028 | - |
| REQ-82 | Giám đốc chuỗi có thể xem báo cáo tỉ lệ lấp đầy lớp nhóm. | UC-028 | - |
| REQ-83 | Giám đốc chuỗi có thể xem báo cáo số buổi tập cá nhân của từng huấn luyện viên. | UC-028 | Việc tính thù lao ngoài phạm vi (CAND-62) |
| REQ-84 | Hệ thống gửi thông báo nhắc gia hạn cho hội viên có gói sắp hết hạn. | UC-008 | - |
| REQ-85 | Thông báo nhắc gia hạn được gửi cho hội viên có gói hết hạn trong 7 ngày tới. | UC-008 | - |
| REQ-86 | Thông báo nhắc gia hạn được gửi mỗi ngày lúc 8 giờ sáng. | UC-008 | - |
| REQ-87 | Hệ thống gửi thông báo cho hội viên qua thông báo đẩy của ứng dụng. | UC-008, UC-011, UC-014, UC-015 | Kênh gửi qua tác nhân phụ ACT-10 |
| REQ-88 | Hệ thống gửi thông báo cho hội viên chưa cài ứng dụng qua SMS. | UC-008, UC-011, UC-014, UC-015 | Kênh gửi qua tác nhân phụ ACT-09 |
| REQ-89 | Hệ thống trao đổi nội dung thông báo với dịch vụ thông báo đẩy của nền tảng di động để gửi thông báo đẩy tới ứng dụng của hội viên. | UC-008, UC-011, UC-014, UC-015 | Giao tiếp ngoài với ACT-10 |
| REQ-90 | Hệ thống trao đổi nội dung tin nhắn với cổng SMS của nhà mạng để gửi SMS tới hội viên. | UC-008, UC-011, UC-014, UC-015 | Giao tiếp ngoài với ACT-09 |
| REQ-91 | Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử. | UC-005, UC-007, UC-017, UC-019 | Chờ Q-37 về phạm vi giao dịch thu tiền |
| REQ-92 | Hệ thống trao đổi dữ liệu giao dịch thu tiền với hệ thống hoá đơn điện tử của đơn vị cung cấp để xuất hoá đơn điện tử. | UC-005, UC-007, UC-017, UC-019 | Giao tiếp ngoài với ACT-11; chưa có tài liệu API (Q-39) |
| REQ-93 | Đặt chỗ lớp nhóm cho tuần mới mở lúc 6 giờ sáng thứ Hai. | UC-010 | Mâu thuẫn với REQ-23, chờ Q-11; CAND-24 chờ Q-11 |
| REQ-94 | Hệ thống phục vụ tới 1.500 hội viên đặt chỗ lớp nhóm cùng lúc khi mở đặt lớp cho tuần mới lúc 6 giờ sáng thứ Hai. | UC-010 | Phi chức năng gắn UC-010, chuyển P06 (Q-42) |
| REQ-95 | Số chỗ đã đặt của một lớp nhóm không được vượt sức chứa. | UC-010 | - |
| REQ-96 | Cửa quay phải phản hồi trong vòng 1 giây. | UC-018 | Phi chức năng gắn UC-018, chuyển P06 (Q-41) |

REQ loại Chức năng và Giao tiếp ngoài đều có UC phủ. Không phủ: REQ-01 đến REQ-04 (loại Dữ liệu, số liệu quy mô, chuyển P06).

## 6. Thống kê và nhận xét ngưỡng

| ACT | Số UC là tác nhân chính | Số UC là tác nhân phụ | Nhận xét |
|---|---|---|---|
| ACT-01 Người quan tâm | 3 | 0 | Trong mức 2-12. Hai UC xem thông tin ngắn, giữ theo U-R05 |
| ACT-02 Hội viên | 11 (10 User-goal, 1 Subfunction) | 0 | Trong mức 2-12. Tăng so với 6 mục tiêu ở P01 vì tách theo phiên và theo thời điểm (U-R13) |
| ACT-03 Khách vãng lai | 1 | 0 | Một UC dùng chung với ACT-02 (UC-018); việc mua vé do lễ tân thao tác (UC-017) |
| ACT-04 Huấn luyện viên | 3 | 0 | Trong mức 2-12 |
| ACT-05 Lễ tân | 3 | 0 | Trong mức 2-12. UC-005 dùng chung với ACT-02 theo U-R10 b |
| ACT-06 Quản lý chi nhánh | 2 | 0 | Trong mức 2-12. Có thể tăng khi Q-03, Q-04, Q-06 được trả lời |
| ACT-07 Giám đốc chuỗi | 3 | 0 | Trong mức 2-12. Ba báo cáo gộp một UC theo U-R05 |
| ACT-08 Cổng thanh toán | 0 | 1 | Có thể thêm 1 UC chính nếu Q-45 trả lời cổng tự gửi kết quả |
| ACT-09 Cổng SMS | 0 | 4 | UC-008, UC-011, UC-014, UC-015 |
| ACT-10 Dịch vụ thông báo đẩy | 0 | 4 | UC-008, UC-011, UC-014, UC-015 |
| ACT-11 Hệ thống hoá đơn điện tử | 0 | 4 | UC-005, UC-007, UC-017, UC-019 |
| ACT-12 Cửa quay | 0 | 1 | UC-018 |
| ACT-13 Bộ định thời hằng ngày | 1 | 0 | Một UC là bình thường với tác nhân thời gian |
| ACT-14 Bộ định thời theo hạn | 4 | 0 | Cao hơn mức một UC thường thấy với tác nhân thời gian, có căn cứ: bốn mốc hạn khác nhau trong nguồn (30 phút, 10 phút sau giờ học, 2 giờ trước giờ học, 12 giờ) với kết quả nghiệp vụ khác nhau; giữ nguyên theo Conventions Phần E |

Tổng số UC: 28 (27 User-goal, 1 Subfunction). Số UC mỗi nhóm: Tiếp cận và tài khoản 4; Gói tập 4; Lớp nhóm 8; Ra vào chi nhánh 2; Huấn luyện cá nhân 7; Giá và báo cáo 3. Số UC Subfunction: 1 (3,6% tổng số, dưới ngưỡng 20%). Tổng số UC nằm trong mức 10-40. Nhóm Ra vào chi nhánh có 2 UC, ít hơn mức 3-12, giữ riêng vì khác lĩnh vực với các nhóm gần nhất (vé và cửa quay). Nhóm Lớp nhóm có 8 UC, trong mức 3-12. Danh sách chưa gồm các UC quản lý danh mục, tài khoản nhân viên, lịch làm việc huấn luyện viên (CAND-14, CAND-15, CAND-66 đến CAND-69) vì đang chờ câu hỏi mở; khi được trả lời, số UC và số UC của các tác nhân quản lý chi nhánh, giám đốc chuỗi sẽ tăng.

## 7. Các mục kiểm soát

### Thay đổi so với phiên bản trước

| UCR | Phần tử đã đổi (UC, CAND, dòng REQ) | Thay đổi |
|---|---|---|
| UCR-01 | UC-005 (Bảng 4a: Tên VI, Tên EN) | Đổi tên từ "Mua gói tập" (Purchase Membership Package) thành "Mua hoặc gia hạn gói tập" (Purchase Or Renew Membership Package). Giữ nguyên tác nhân, mức, nhóm, mục tiêu, REQ và CAND nguồn |
| UCR-02 | UC-011 (Bảng 4b: Mục tiêu) | Từ "Hội viên không còn chỗ trong lớp đã huỷ và chỗ được trả lại cho hội viên đứng đầu danh sách chờ." thành "Hội viên không còn giữ chỗ trong lớp đã huỷ; hội viên đứng đầu danh sách chờ (nếu có) được thông báo có chỗ trống." |
| UCR-02 | UC-015 (Bảng 4b: Mục tiêu) | Bỏ vế "chỗ phòng được giải phóng" (nguồn không nêu). Mục tiêu mới: "Những hội viên đã đặt chỗ trong lớp có dưới 3 người đặt biết lớp đã bị huỷ." |
| UCR-02 | UC-021 (Bảng 4b: Mục tiêu) | Viết lại từ góc nhìn tác nhân chính ACT-04: "Yêu cầu đặt buổi tập cá nhân được huấn luyện viên xác nhận hoặc từ chối." |
| UCR-02 | UC-022 (Bảng 4b: Mục tiêu) | Bỏ vế "hội viên không bị giữ khung giờ vô thời hạn" (nguồn không nêu). Mục tiêu mới: "Yêu cầu đặt buổi chưa được huấn luyện viên xác nhận hoặc từ chối trong 12 giờ bị huỷ." |
| UCR-03 | UC-021 (Bảng 4a: Tên VI, Tên EN) | Đổi tên từ "Duyệt yêu cầu đặt buổi tập" (Review Training Session Request) thành "Phản hồi yêu cầu đặt buổi tập" (Respond To Training Session Request) cho khớp thuật ngữ "xác nhận hoặc từ chối" của nguồn. Giữ nguyên tác nhân chính ACT-04 và mức User-goal |
| Hệ quả của UCR-01, UCR-03 | Mã phiên bản | Tăng phiên bản từ 1.0 lên 1.1; cập nhật hàng Đầu vào đã dùng. Không đổi mã UC, CAND, EV, Q; không đổi Mục 1, 2, 3, 5, 6 |

### Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-46 | Hội viên đã có tài khoản có xem giá gói tập và lịch lớp nhóm độc lập (ngoài việc xem khi mua gói, khi đặt chỗ) không? (Có, hội viên cũng là tác nhân chính của hai UC xem / Không, chỉ người quan tâm xem độc lập) | Tác nhân chính của UC-001, UC-002 (P02, P03) | Mục 1 câu 1: "Người quan tâm xem bảng giá gói tập và lịch lớp nhóm trên ứng dụng di động mà không cần tài khoản"; nguồn không nêu hội viên có xem độc lập hay không |
| Q-47 | Huấn luyện viên, lễ tân, quản lý chi nhánh, giám đốc chuỗi có phải đăng nhập trước khi dùng các chức năng của mình không? (Có, cả bốn vai trò / Chỉ một số vai trò - nêu rõ / Không) | Tác nhân chính của UC-004 (P02, P03); tiền điều kiện của các UC của bốn vai trò (P04) | Mục 1 câu 2 và Mục 6 câu 3 chỉ nhắc "tài khoản hội viên" và "người khác đã có tài khoản"; nguồn không nhắc tài khoản hoặc đăng nhập của bốn vai trò (U-R01) |
| Q-48 | Hội viên đăng ký bảo lưu gói qua kênh nào? (Tự làm trên ứng dụng / Qua lễ tân tại quầy / Cả hai) | Tác nhân chính của UC-006 (ACT-02, hoặc thêm hoặc thay bằng ACT-05); P03, P04 | Mục 6 câu 1: "Hội viên có gói từ 3 tháng trở lên được bảo lưu gói..." không nêu kênh, trong khi Mục 6 câu 3 nêu rõ lễ tân thực hiện chuyển nhượng tại quầy |
| Q-49 | Khi chỗ chuyển cho người kế tiếp trong danh sách chờ (quá 30 phút), người đó có được thông báo và có 30 phút xác nhận như người đứng đầu không? (Có, lặp lại cách xử lý / Không - nêu cách khác) | UC-013 (tác nhân phụ ACT-09, ACT-10), quan hệ giữa UC-012 và UC-013 (P03); luồng ngoại lệ (P04) | Mục 3 câu 4: "quá 30 phút thì chỗ chuyển cho người kế tiếp" không nêu người kế tiếp có được thông báo và có hạn 30 phút không |

Các ứng viên đang chờ câu hỏi đã cấp ở bước trước: Q-01, Q-02, Q-03, Q-04, Q-05, Q-06, Q-11 (nội dung ở P00-problem-brief.md) và Q-45 (nội dung ở P01-actors.md). Nội dung các câu hỏi này không chép lại để mỗi mã chỉ trỏ tới một câu hỏi.

### Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

### Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P01 | Tác nhân thời gian (chưa có mã) | Mốc 6 giờ sáng thứ Hai mở đặt lớp cho tuần mới (REQ-93) chưa có tác nhân thời gian; CAND-24 chờ Q-11. Nếu Q-11 trả lời cả tuần mở lúc 6 giờ sáng thứ Hai do hệ thống thực hiện theo lịch thì cần tác nhân thời gian theo tuần (U-R07) | Chưa sửa. Chỉ thêm tác nhân thời gian theo tuần ở P01 khi Q-11 được trả lời theo hướng này, rồi chạy lại P02 |

### Vấn đề còn mở

Mọi mục Target đạt, với các điểm cần người dùng lưu ý:

- Lần chạy lại sau review áp dụng cả ba UCR (UCR-01, UCR-02, UCR-03); không có UCR nào bị bỏ qua. P02R phiên bản 1.0 không cấp Q-nn, ASM-nn mới nên không có mục nào để chép vào Câu hỏi mở, Giả định.

- Mục 3 của Target: kết luận "Chờ Q-nn" của CAND-13 (Q-45), CAND-14 (Q-01), CAND-15 (Q-02), CAND-24 (Q-11), CAND-66 (Q-03), CAND-67 (Q-04), CAND-68 (Q-05), CAND-69 (Q-06) trỏ tới câu hỏi nằm ở P00 hoặc P01, không chép lại vào mục Câu hỏi mở của P02 để mã Q chỉ trỏ tới một câu hỏi duy nhất (Conventions C3). Các ứng viên này không vào Mục 4; P03 bỏ qua.
- UC-005 hợp nhất việc bán gói của lễ tân với việc mua gói của hội viên theo U-R10 b và U-R12 (kênh thu tiền khác nhau chỉ là luồng thay thế). Nếu Q-01 trả lời lễ tân tạo tài khoản cho người mua tại quầy thì đoạn tạo tài khoản có thể thoả U-R10 a và cần tách thành hai UC; khi đó chạy lại P02.
- Hết giờ chờ 15 phút của đơn mua được xử lý là luồng thay thế của UC-005 (CAND-09), theo P01 Mục 4. Hạn 30 phút của danh sách chờ (UC-013) và hạn 12 giờ của huấn luyện viên (UC-022) là UC của ACT-14, theo P01. Nếu người dùng coi hai hạn này là luồng thay thế thì bỏ UC-013 và UC-022, chuyển vào UC-012 và UC-020.
- Q-43 chưa trả lời: UC-013, UC-015, UC-016, UC-022 là hành động hệ thống tự thực hiện theo câu bị động của nguồn; nếu có bước nhân viên duyệt hoặc gỡ thì ACT-14 và các UC này phải xét lại.
- UC-028 gộp ba báo cáo theo U-R05 vì nguồn không nêu cách thao tác khác nhau; nếu Q-33, Q-34 cho thấy kỳ và tiêu chí khác nhau đáng kể, tách theo từng báo cáo.
- UC-010 còn mang mâu thuẫn REQ-23 và REQ-93 chờ Q-11; REQ-94 (phi chức năng) và REQ-96 (phi chức năng) gắn với UC-010, UC-018 và chuyển P06.
- Kết luận của CAND-16, CAND-64, CAND-65 trỏ tới nhiều UC vì cùng một việc (xuất hoá đơn điện tử, gửi thông báo đẩy, gửi SMS) xảy ra trong nhiều UC; mỗi UC liệt kê đủ ở cột CAND nguồn.
- UC-022 có tên 7 từ, vượt mức 2-6 từ của U-N7 vì cần nêu cả đối tượng (yêu cầu đặt buổi) và điều kiện (quá hạn); không có từ cấm.
- UC-005 sau khi đổi tên có 6 từ, trong mức 2-6 của U-N7; từ "hoặc" nối hai cách đạt cùng một mục tiêu (mua, gia hạn) trong cùng một phiên, không phải hai mục tiêu ở hai thời điểm (U-AP05 không áp dụng).
- Tên UC-001 dùng "giá gói tập" thay cho "bảng giá" của nguồn để tránh từ cấm "bảng" của U-N5.
