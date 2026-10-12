# P01 - Xác định tác nhân - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P01 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0); yeu-cau-phong-tap.md |
| Phạm vi | Toàn hệ thống |
| Mã Q, ASM cuối đã cấp | Q-45; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Ranh giới hệ thống

Hệ thống cần xây dựng là Hệ thống quản lý chuỗi phòng tập VietFit, gồm ứng dụng di động (Android, iOS) cho hội viên và huấn luyện viên, ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi, cùng phần xử lý nghiệp vụ phía sau và kho dữ liệu của chính hệ thống.

| Thành phần | Trong / Ngoài / Chờ Q-nn | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
|---|---|---|---|
| Ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (kể cả mã QR hiển thị trên ứng dụng) | Trong | Hồ sơ dự án: NEN_TANG; "trên ứng dụng di động" (Mục 1 câu 1); REQ-06, REQ-11, REQ-39 | Là thành phần nội bộ, không phải tác nhân |
| Ứng dụng web trên trình duyệt máy tính cho lễ tân, quản lý chi nhánh và giám đốc chuỗi | Trong | Hồ sơ dự án: NEN_TANG; REQ-18, REQ-69, REQ-78 | Là thành phần nội bộ, không phải tác nhân |
| Phần mềm quản lý hội viên, lớp tập và ra vào (phần xử lý nghiệp vụ phía sau) | Trong | "VietFit cần phần mềm quản lý hội viên, lớp tập và ra vào" (Đoạn mở đầu, câu 3); REQ-02 | Là thành phần nội bộ, không phải tác nhân |
| Kho dữ liệu của hệ thống (hội viên, gói tập, lớp, đặt chỗ, ra vào) | Trong | Kho dữ liệu của chính hệ thống (Bước 1.3), thay bảng tính hiện tại; REQ-02, REQ-04 | Là thành phần nội bộ, không phải tác nhân |
| Cổng thanh toán trực tuyến của đối tác | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-14 | Là tác nhân ACT-08 |
| Cổng SMS của nhà mạng | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-90 | Là tác nhân ACT-09 |
| Dịch vụ thông báo đẩy của nền tảng di động | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-89 | Là tác nhân ACT-10 |
| Hệ thống hoá đơn điện tử của đơn vị cung cấp | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI; REQ-92 | Là tác nhân ACT-11 |
| Cửa quay có đầu đọc mã QR tại mỗi chi nhánh | Ngoài | Hồ sơ dự án: HE_THONG_NGOAI ("do nhà cung cấp thiết bị lắp đặt, gửi mã QR đọc được tới phần mềm qua API"); "Cửa quay hỏi phần mềm" (Mục 5 câu 2); REQ-40 | Là tác nhân ACT-12 |
| Máy POS của ngân hàng | Ngoài | "máy POS không kết nối với phần mềm, lễ tân nhập mã giao dịch in trên hoá đơn POS" (Mục 2 câu 4); REQ-21; P00 SH-07 | Ngoài, không phải tác nhân (đường truyền: không kết nối, thông tin đi qua mã giao dịch do ACT-05 nhập tay) kèm dòng ở Mục 4 |
| Máy in vé (ngụ ý từ "lễ tân in vé có mã QR") | Chờ Q-44 | "lễ tân in vé có mã QR" (Mục 5 câu 3); REQ-43; hồ sơ dự án không ghi máy in trong HE_THONG_NGOAI | Chờ trả lời Q-44 |
| Bảng tính ghi bán gói tập | Ngoài | "việc bán gói tập ghi bằng bảng tính" (Đoạn mở đầu, câu 1) | Ngoài, không phải tác nhân (cách làm cũ được thay thế) kèm dòng ở Mục 4 |
| Nhóm chat đặt chỗ lớp nhóm | Ngoài | "đặt chỗ lớp nhóm qua nhóm chat" (Đoạn mở đầu, câu 1) | Ngoài, không phải tác nhân (cách làm cũ được thay thế) kèm dòng ở Mục 4 |
| Sổ giấy dò tên hội viên khi vào cửa | Ngoài | "lễ tân phải dò tên hội viên trên giấy khi vào cửa" (Đoạn mở đầu, câu 1) | Ngoài, không phải tác nhân (cách làm cũ được thay thế) kèm dòng ở Mục 4 |

## 2. Bảng tác nhân

| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |
|---|---|---|---|---|---|---|---|---|
| ACT-01 | Người quan tâm | Prospect | Người | Chính | Người chưa có tài khoản, dùng ứng dụng di động để xem thông tin; đăng ký tài khoản để trở thành hội viên. Cách gọi của nguồn: "Người quan tâm", "người đó". | Xem bảng giá gói tập<br>Xem lịch lớp nhóm<br>Đăng ký tài khoản hội viên | - | REQ-06, REQ-07, REQ-08 |
| ACT-02 | Hội viên | Member | Người | Chính | Người đã có tài khoản hội viên, dùng ứng dụng di động. Gồm cả người đứng đầu danh sách chờ, người đã đặt chỗ, hội viên chưa cài ứng dụng (nhận SMS) và người nhận chuyển nhượng gói ("người khác đã có tài khoản"); khi chuyển nhượng, hội viên chỉ làm việc qua Lễ tân (ACT-05). | Mua hoặc gia hạn gói tập<br>Đặt chỗ lớp nhóm, huỷ chỗ, vào danh sách chờ và nhận chỗ khi có người huỷ<br>Vào chi nhánh bằng mã QR<br>Bảo lưu gói tập<br>Mua gói buổi tập cá nhân, đặt và huỷ buổi tập<br>Xem chỉ số cơ thể của mình | - | REQ-11, REQ-12, REQ-13, REQ-15, REQ-16, REQ-17, REQ-22, REQ-26, REQ-27, REQ-28, REQ-29, REQ-32, REQ-39, REQ-46, REQ-56, REQ-59, REQ-63, REQ-68 |
| ACT-03 | Khách vãng lai | Walk-in Guest | Người | Chính | Người không có gói hội viên, mua vé tập một ngày tại quầy qua Lễ tân (ACT-05) và dùng mã QR trên vé quét tại cửa quay của chi nhánh đã mua trong ngày. | Vào chi nhánh trong ngày bằng mã QR trên vé tập một ngày | - | REQ-42, REQ-44, REQ-45 |
| ACT-04 | Huấn luyện viên | Trainer | Người | Chính | Huấn luyện viên dùng ứng dụng di động để xử lý yêu cầu đặt buổi tập cá nhân và ghi nhận buổi tập. "Huấn luyện viên phụ trách" của một hội viên là cùng vai trò này. | Xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân<br>Ghi nhận buổi tập cá nhân và chỉ số cơ thể của hội viên<br>Xem chỉ số cơ thể của hội viên mình phụ trách | - | REQ-60, REQ-61, REQ-65, REQ-66, REQ-68 |
| ACT-05 | Lễ tân | Receptionist | Người | Chính | Nhân viên tại quầy chi nhánh, dùng ứng dụng web. Bán gói và chuyển nhượng gói trực tiếp với khách tại quầy, thu tiền mặt hoặc nhập mã giao dịch POS. | Bán gói tập tại quầy (thu tiền mặt hoặc nhập mã giao dịch POS)<br>Chuyển nhượng gói tập tại quầy và thu phí chuyển nhượng<br>In vé tập một ngày có mã QR cho khách vãng lai | - | REQ-18, REQ-19, REQ-20, REQ-21, REQ-43, REQ-52, REQ-54 |
| ACT-06 | Quản lý chi nhánh | Branch Manager | Người | Chính | Người phụ trách lịch lớp nhóm của một chi nhánh, dùng ứng dụng web. | Lập lịch lớp nhóm hằng tuần<br>Huỷ lớp nhóm vì sự cố | - | REQ-69, REQ-70, REQ-71, REQ-72, REQ-76, REQ-77 |
| ACT-07 | Giám đốc chuỗi | Chain Director | Người | Chính | Người điều hành toàn chuỗi, dùng ứng dụng web. Đặt giá, khuyến mãi và xem báo cáo toàn chuỗi. | Đặt giá các gói<br>Đặt chương trình khuyến mãi theo khoảng ngày<br>Xem báo cáo doanh thu, tỉ lệ lấp đầy lớp nhóm và số buổi tập cá nhân của huấn luyện viên | - | REQ-78, REQ-79, REQ-80, REQ-81, REQ-82, REQ-83 |
| ACT-08 | Cổng thanh toán | Payment Gateway | Hệ thống ngoài | Phụ | Cổng thanh toán trực tuyến của đối tác (API REST, có tài liệu API thanh toán và tra cứu giao dịch). Tính chất Phụ theo nguồn; chờ Q-45 xác nhận cổng có tự gửi kết quả về hay không. | Cung cấp: thu tiền thanh toán trực tuyến cho đơn mua và đơn gia hạn gói tập, trả kết quả thanh toán | - | REQ-13, REQ-14 |
| ACT-09 | Cổng SMS | SMS Gateway | Hệ thống ngoài | Phụ | Cổng SMS của nhà mạng (API REST). Hội viên nhận SMS là bên nhận thụ động, xem Mục 3. | Cung cấp: gửi tin nhắn SMS tới hội viên chưa cài ứng dụng | - | REQ-27, REQ-75, REQ-77, REQ-84, REQ-88, REQ-90 |
| ACT-10 | Dịch vụ thông báo đẩy | Push Notification Service | Hệ thống ngoài | Phụ | Dịch vụ thông báo đẩy của nền tảng di động. Hội viên nhận thông báo là bên nhận thụ động, xem Mục 3. | Cung cấp: gửi thông báo đẩy tới ứng dụng của hội viên | - | REQ-27, REQ-75, REQ-77, REQ-84, REQ-87, REQ-89 |
| ACT-11 | Hệ thống hoá đơn điện tử | E-Invoice System | Hệ thống ngoài | Phụ | Hệ thống hoá đơn điện tử của đơn vị cung cấp (API REST, chưa có tài liệu API). Việc lập, điều chỉnh, huỷ hoá đơn nằm ngoài phạm vi. | Cung cấp: nhận dữ liệu giao dịch thu tiền để xuất hoá đơn điện tử | - | REQ-91, REQ-92 |
| ACT-12 | Cửa quay | Turnstile | Thiết bị | Phụ | Cửa quay có đầu đọc mã QR tại mỗi chi nhánh, do nhà cung cấp thiết bị lắp đặt; đầu đọc mã QR là bộ phận của thiết bị này. Hội viên hoặc khách vãng lai quét mã tại cửa quay; cửa quay hỏi phần mềm và mở cửa theo kết quả. | Cung cấp: gửi mã QR đọc được tới phần mềm, nhận kết quả cho phép vào và mở cửa | - | REQ-35, REQ-39, REQ-40, REQ-41, REQ-96 |
| ACT-13 | Bộ định thời hằng ngày | Daily Timer | Thời gian | Chính | Sự kiện theo lịch mỗi ngày, không có người hay hệ thống nào ra lệnh. | Kích hoạt: mỗi ngày lúc 8 giờ sáng (nhắc gia hạn cho hội viên có gói hết hạn trong 7 ngày tới) | - | REQ-84, REQ-85, REQ-86 |
| ACT-14 | Bộ định thời theo hạn | Deadline Timer | Thời gian | Chính | Sự kiện theo mốc hạn của từng lớp, từng thông báo, từng yêu cầu; mốc rơi vào lúc không còn phiên nào của tác nhân đang mở. Các hành động do hệ thống tự thực hiện chờ Q-43 xác nhận. | Kích hoạt: 2 giờ trước giờ học của mỗi lớp nhóm (kiểm tra số người đặt chỗ, tự huỷ lớp dưới 3 người)<br>Kích hoạt: 10 phút sau giờ bắt đầu của mỗi lớp nhóm (tính vắng mặt cho hội viên đặt chỗ mà không quẹt vào cửa)<br>Kích hoạt: 30 phút sau khi thông báo nhận chỗ cho hội viên đứng đầu danh sách chờ<br>Kích hoạt: hạn 12 giờ của huấn luyện viên với yêu cầu đặt buổi tập cá nhân (mốc bắt đầu nguồn chưa nêu) | - | REQ-30, REQ-34, REQ-35, REQ-36, REQ-62, REQ-61, REQ-73, REQ-74, REQ-75 |

## 3. Bên liên quan không phải tác nhân

| SH | Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
|---|---|---|---|---|
| SH-01 | Chuỗi phòng tập VietFit (tổ chức, chủ sở hữu) | Thay bảng tính, nhóm chat và sổ giấy bằng phần mềm quản lý hội viên, lớp tập và ra vào; không để đặt chỗ vượt sức chứa | Báo cáo do ACT-07 Giám đốc chuỗi xem | REQ-01, REQ-02, REQ-81 |
| SH-02 | Hội viên (khi chỉ nhận thông báo, hoặc khi là người nhận chuyển nhượng do lễ tân thao tác) | Biết lớp đã đặt bị huỷ, có chỗ trống, gói sắp hết hạn; nhận gói chuyển nhượng | ACT-10 Dịch vụ thông báo đẩy, ACT-09 Cổng SMS (thông báo); ACT-05 Lễ tân (chuyển nhượng) | REQ-27, REQ-52, REQ-75, REQ-77, REQ-84, REQ-88 |
| SH-03 | Huấn luyện viên (khi là đối tượng của báo cáo số buổi tập cá nhân) | Số buổi tập cá nhân được ghi nhận đúng để tính thù lao | Báo cáo do ACT-07 Giám đốc chuỗi xem | REQ-83 |

## 4. Ứng viên tác nhân bị loại

| Ứng viên | Lý do loại | REQ |
|---|---|---|
| Hệ thống, phần mềm VietFit, máy chủ | A-T1: chính hệ thống cần xây dựng, hạ tầng của hệ thống | REQ-02 |
| Ứng dụng di động, ứng dụng web, mã QR hiển thị trên ứng dụng | A-T1: giao diện của chính hệ thống | REQ-06, REQ-39 |
| Kho dữ liệu của hệ thống | A-T1: thành phần nội bộ của hệ thống | REQ-02, REQ-04 |
| Máy POS của ngân hàng (P00 SH-07) | A-T2: không kết nối với phần mềm; lễ tân quẹt thẻ trên máy POS rồi nhập mã giao dịch vào hệ thống | REQ-20, REQ-21 |
| Ngân hàng (chủ máy POS, phát hành thẻ) | A-T2: không trao đổi trực tiếp với hệ thống; mã giao dịch đến hệ thống qua ACT-05 | REQ-20, REQ-21 |
| Đối tác (chủ cổng thanh toán) | A-T2: chỉ trao đổi qua Cổng thanh toán ACT-08 | REQ-14 |
| Nhà mạng (chủ cổng SMS) | A-T2: chỉ trao đổi qua Cổng SMS ACT-09 | REQ-90 |
| Nền tảng di động (chủ dịch vụ thông báo đẩy) | A-T2: chỉ trao đổi qua Dịch vụ thông báo đẩy ACT-10 | REQ-89 |
| Đơn vị cung cấp hệ thống hoá đơn điện tử | A-T2: chỉ trao đổi qua Hệ thống hoá đơn điện tử ACT-11 | REQ-92 |
| Nhà cung cấp thiết bị cửa quay | A-T2: chỉ lắp đặt thiết bị, không trao đổi với hệ thống; thiết bị là ACT-12 | REQ-40 |
| Đầu đọc mã QR của cửa quay | Gộp vào ACT-12 Cửa quay: bộ phận của thiết bị | REQ-40 |
| Bảng tính ghi bán gói tập | A-T2: cách làm cũ được hệ thống thay thế, không trao đổi với hệ thống | - |
| Nhóm chat đặt chỗ | A-T2: cách làm cũ được hệ thống thay thế, không trao đổi với hệ thống | - |
| Sổ giấy dò tên hội viên | A-T2: cách làm cũ được hệ thống thay thế, không trao đổi với hệ thống | - |
| Người đứng đầu danh sách chờ, người trong danh sách chờ, người đã đặt chỗ | Gộp vào ACT-02 Hội viên: cùng mục tiêu và cùng quyền | REQ-26, REQ-27, REQ-75, REQ-77 |
| Người nhận chuyển nhượng, "người khác đã có tài khoản" | Gộp vào ACT-02 Hội viên: cùng vai trò; trong chuyển nhượng chỉ làm việc qua Lễ tân nên không phải tác nhân của tương tác đó (A-T2) | REQ-52 |
| Hội viên chưa cài ứng dụng | Gộp vào ACT-02 Hội viên: nhận SMS thụ động, không khác vai trò (xem Q-36 của P00) | REQ-88 |
| Người đăng ký tài khoản ("người đó") | Gộp vào ACT-01 Người quan tâm | REQ-08 |
| Huấn luyện viên phụ trách | Gộp vào ACT-04 Huấn luyện viên | REQ-68 |
| Người mua vé tại quầy | Gộp vào ACT-03 Khách vãng lai | REQ-42 |
| Nhân viên (cách gọi chung của lễ tân, quản lý chi nhánh, giám đốc chuỗi) | A-T3 và A-T5: tên chung che mất khác biệt mục tiêu giữa ba vai trò, đã tách thành ACT-05, ACT-06, ACT-07 | - |
| Người quản trị hệ thống (quản lý danh mục phòng, loại lớp, tài khoản nhân viên, lịch làm việc huấn luyện viên) | A-T6: nguồn không nêu vai trò quản trị; chờ P00 Q-02, Q-03, Q-04, Q-05, Q-06 | - |
| Hết giờ chờ 15 phút của đơn mua chưa thanh toán | Bước 2.3: hết giờ chờ trong phiên, là luồng thay thế của use case | REQ-15, REQ-16 |
| Mốc 6 giờ sáng thứ Hai mở đặt lớp cho tuần mới | A-T4: là quy tắc thời điểm được phép đặt chỗ, nguồn không nêu chức năng nào được kích hoạt vào mốc này; mâu thuẫn với REQ-23 chờ P00 Q-11 | REQ-93 |
| Mốc ngày hết hạn gói, ngày bắt đầu và kết thúc bảo lưu, hết 7 ngày khoá quyền đặt lớp, hết hạn gói buổi tập cá nhân 90 ngày, hết ngày dùng vé | A-T4: là điều kiện tính theo ngày khi kiểm tra trạng thái, nguồn không nêu chức năng nào được kích hoạt vào các mốc này | REQ-38, REQ-44, REQ-51, REQ-58 |

## 5. Các mục kiểm soát

### Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-44 | Vé tập một ngày có mã QR do lễ tân in bằng cách nào? (In từ trình duyệt qua máy in thông thường, phần mềm không giao tiếp riêng với máy in / Máy in nối riêng nhận lệnh in từ phần mềm theo giao thức riêng) | Ranh giới (Mục 1, dòng Máy in vé); có thêm tác nhân Thiết bị "Máy in vé" hay không (P01); giao diện thiết bị (P11b); REQ-43 | Mục 5 câu 3: "lễ tân in vé có mã QR"; HE_THONG_NGOAI của hồ sơ dự án không ghi máy in |
| Q-45 | Cổng thanh toán chỉ trả kết quả thanh toán khi phần mềm gọi hoặc tra cứu, hay còn tự gửi kết quả về phần mềm vào thời điểm phần mềm không yêu cầu? (Chỉ trả khi được gọi hoặc tra cứu / Tự gửi kết quả về phần mềm) | Tính chất của ACT-08 (Phụ, hoặc Chính và phụ); REQ-14; luồng ngoại lệ thanh toán (P04, cùng Q-14 của P00) | Mục 2 câu 1: "thanh toán qua cổng thanh toán trực tuyến của đối tác"; HE_THONG_NGOAI: "có tài liệu API thanh toán và tra cứu giao dịch" không nói chiều khởi xướng của kết quả |

### Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

### Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P00 | SH-09 | Cột "Tương tác trực tiếp" ghi "Chưa rõ" cho Khách vãng lai. Khách vãng lai quét mã QR trên vé tại cửa quay, thiết bị chuyển thao tác đó vào hệ thống (A-T2 thoả) | Đổi thành "Có (qua cửa quay)"; nếu giữ "Chưa rõ" thì P01 vẫn xử lý Khách vãng lai là tác nhân Chính ACT-03 |
| P00 | REQ-21 | Loại "Giao tiếp ngoài" nhưng nội dung nêu "không có kết nối trực tiếp với máy POS": không có giao diện máy nào để mô tả, chỉ là việc lễ tân nhập mã giao dịch | Đổi loại thành Chức năng hoặc Dữ liệu (gộp vào REQ-20); nếu giữ loại Giao tiếp ngoài thì P01 mục 8 vẫn đạt nhờ lý do ghi ở Vấn đề còn mở |

### Vấn đề còn mở

Mọi mục Target đạt, với các điểm cần người dùng lưu ý:

- Mục 8: REQ-21 (loại Giao tiếp ngoài) không có tác nhân hệ thống ngoài hoặc thiết bị vì máy POS không kết nối với phần mềm. REQ-21 gắn với ACT-05 Lễ tân (người nhập mã giao dịch).
- Danh sách tác nhân phụ thuộc các câu hỏi mở của P00 chưa được trả lời. Q-01, Q-02, Q-03, Q-04, Q-05, Q-06 có thể thêm vai trò quản trị hoặc mục tiêu quản lý danh mục, tài khoản, lịch làm việc cho Lễ tân, Quản lý chi nhánh, Giám đốc chuỗi; Q-15 có thể thêm mục tiêu nhận thông báo cho Huấn luyện viên; Q-43 có thể thêm bước duyệt hoặc gỡ của nhân viên cho các hành động hệ thống tự thực hiện (ACT-14), và nếu có thì ACT-14 phải xét lại. P01 không tự thêm các tác nhân hoặc mục tiêu này.
- Lựa chọn giữa hai quy tắc ở Bước 2.3 (C9): hết giờ chờ 15 phút của đơn mua được loại vì là chờ thanh toán trong phiên mua gói. Hạn 30 phút của danh sách chờ và hạn 12 giờ của huấn luyện viên được giữ làm kích hoạt của ACT-14 vì lúc hết hạn không còn phiên nào của tác nhân đang mở, giống ví dụ lịch đặt phòng chưa đặt cọc sau 24 giờ. Nếu người dùng coi hai hạn này là luồng thay thế của use case thì bỏ hai dòng tương ứng của ACT-14.
- Tính chất của Cửa quay (ACT-12): nguồn nêu cửa quay là bên hỏi phần mềm, nhưng người quét mã mới có mục tiêu nên Hội viên và Khách vãng lai là Chính, Cửa quay là Phụ theo quy tắc thiết bị ngoài ranh giới ở cột Tính chất.
- Huấn luyện viên (ACT-04) xếp Chính vì việc xử lý yêu cầu đặt buổi nằm ngoài phiên của hội viên (hạn 12 giờ), không phải bước xác nhận trong cùng phiên.
- Số mục tiêu của Hội viên (ACT-02) là 6, vượt mức hợp lý 1-5 do nguồn giao nhiều mục tiêu khác nhau cho một vai trò; không có cơ sở tách vai trò.
- Không tạo quan hệ tổng quát hoá: không có nhóm từ hai tác nhân con trở lên thoả đồng thời tiêu chí a, b, c của Bước 5 (Hội viên và Huấn luyện viên chỉ chung một mục tiêu xem chỉ số cơ thể và không thoả phép thử "là một").
