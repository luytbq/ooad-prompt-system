# P11b - SS-04 SmsMessaging - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | SS-04 SmsMessaging (package PKG-24 NotificationChannels); lần chạy đầu cho mọi subsystem của P10 F2 |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102, ghi ở file chung P11b-system-interfaces.md); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-015 Huỷ lớp nhóm ít người đặt | AC-C-CancelUnderBookedClassHandler (DC-CancelUnderBookedClassHandler) | SD1b STT 1.9 sendSms (hội viên, lớp nhóm bị huỷ), bước 6, 7 | Số điện thoại của hội viên chưa cài ứng dụng; nội dung thông báo lớp bị huỷ (Q-66) | 6a (cổng SMS không gửi được), chờ Q-65 và Q-79 |

- UC-005 (luồng 9a2, 10a) có thể dùng IF-04 nếu Q-53 chọn SMS; UC-008, UC-011, UC-014 chưa có P04, P07. Khi có, chạy lại P11b cho SS-04.

## F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-04 | ISmsGateway | Nhận yêu cầu gửi SMS tới một số điện thoại và chuyển cho cổng SMS. | SS-04 SmsMessaging | DC-CancelUnderBookedClassHandler (PKG-15) | PKG-24 NotificationChannels |

- Số operation: IF-04 có 1.
- Layer: IF-04 ở PKG-24 (Services); DC-PhoneNumber ở PKG-32 (Domain); DC-NotificationContent, DC-NotificationReceipt, DC-InvalidNotificationContent dùng chung với SS-03 trong PKG-24.

## F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-04 | ISmsGateway | Cổng SMS (ACT-09) | sendSms(phone: PhoneNumber, content: NotificationContent): NotificationReceipt | phone: PhoneNumber - số điện thoại của hội viên chưa cài ứng dụng (BR-14)<br>content: NotificationContent - đã soạn, không rỗng (nội dung: Q-66) | NotificationReceipt: status (Accepted), notificationKey: string (khoá do phần mềm sinh) | InvalidPhoneNumber (Nghiệp vụ, kiểm tra đầu vào); InvalidNotificationContent (Nghiệp vụ); lỗi gửi xảy ra ở nền và chỉ ghi nhật ký | UC-015 (bước 6, 7) | Control đã xác định kênh của hội viên là SMS | Yêu cầu nằm trong hàng chờ gửi nền; đã thử gửi tới 4 lần (1 lần đầu, tối đa 3 lần thử lại) khi cần | Bất đồng bộ (P09 F7: gửi qua tiến trình nền) | Có với khoá idempotency do hệ thống sinh (notificationKey); cổng chưa có tài liệu nên nhận trùng được chấp nhận vì không có tác dụng phụ tài chính đáng kể | 5 giây mỗi lần gửi (CHINH_SACH_LOI) |

- Ánh xạ trách nhiệm P08 của AC-B-SmsGateway: // sendSms --> IF-04.sendSms.
- Chữ ký nhận DC-PhoneNumber theo P10 PKG-32; control lấy số điện thoại từ hội viên (thuộc tính định danh theo GL-19, P12 bổ sung vào DC-Member).
- Xử lý khi cổng không gửi được chờ Q-65, Q-79; SS-04 chỉ thử lại cùng kênh theo CHINH_SACH_LOI rồi ghi nhật ký.

## F4. Sequence diagram

File diagrams/P11b-subsystem-SS-04.drawio gồm 4 trang: "Hộp đen - UC-015 gửi thông báo lớp bị huỷ"; "Hộp trắng - sendSms"; "Phần tử"; "Phụ thuộc". STT đánh số phẳng theo trục thời gian trong mỗi trang; tọa độ bảng Node là tuyệt đối. Gate nằm trên cạnh trái khung sd, tâm gate ở y của message nên x, y của gate lệch 5 so với bội số của 10 (xem Vấn đề còn mở).

### Trang "Hộp đen - UC-015 gửi thông báo lớp bị huỷ" (SS04-BB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS04-BB1-FR | Fragment | sd Hộp đen UC-015 SMS | - | - | Khung sd của trang | 20 | 0 | 420 | 320 |
| SS04-BB1-L1 | Lifeline | :CancelUnderBookedClassHandler | «control» | - | DC-CancelUnderBookedClassHandler (PKG-15) | 100 | 40 | 120 | 260 |
| SS04-BB1-L2 | Lifeline | :IF-04 ISmsGateway | «interface» | - | Subsystem SS-04 hiện thực | 260 | 40 | 120 | 260 |
| SS04-BB1-F1 | Fragment | loop [mỗi hội viên có kênh là SMS (BR-14)] | - | - | - | 70 | 90 | 340 | 170 |
| SS04-BB1-F2 | Fragment | alt [yêu cầu được nhận vào hàng chờ gửi] | - | SS04-BB1-F1 | đường ngăn SS04-BB1-F2-O2-SEP nét đứt tại y=180; đường ngăn SS04-BB1-F2-O3-SEP nét đứt tại y=220 | 80 | 140 | 320 | 110 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS04-BB1-F2 toán hạng 2: [số điện thoại không hợp lệ]; SS04-BB1-F2 toán hạng 3: [nội dung không hợp lệ].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS04-BB1-M01 | 1 | SS04-BB1-L1 | SS04-BB1-L2 | sendSms(phone, content) | Đồng bộ | SS04-BB1-F1 | UC-015 bước 6, 7; sendSms |
| SS04-BB1-M02 | 2 | SS04-BB1-L2 | SS04-BB1-L1 | NotificationReceipt | Trả về | SS04-BB1-F2 (toán hạng 1) | UC-015 bước 6, 7 |
| SS04-BB1-M03 | 3 | SS04-BB1-L2 | SS04-BB1-L1 | InvalidPhoneNumber | Trả về | SS04-BB1-F2 (toán hạng 2) | UC-015 bước 6; Q-36 |
| SS04-BB1-M04 | 4 | SS04-BB1-L2 | SS04-BB1-L1 | InvalidNotificationContent | Trả về | SS04-BB1-F2 (toán hạng 3) | UC-015 bước 6; Q-66 |

### Trang "Hộp trắng - sendSms" (SS04-WB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS04-WB1-FR | Fragment | sd sendSms | - | - | Khung sd của trang | 20 | 0 | 740 | 680 |
| SS04-WB1-L1 | Lifeline | :SmsFacade | «facade» | SS-04 | DC-SmsFacade; hiện thực IF-04 | 100 | 40 | 120 | 620 |
| SS04-WB1-L2 | Lifeline | :SmsMessageMapper | «mapper» | SS-04 | DC-SmsMessageMapper | 260 | 40 | 120 | 620 |
| SS04-WB1-L3 | Lifeline | :SmsClient | «adapter» | SS-04 | DC-SmsClient | 420 | 40 | 120 | 620 |
| SS04-WB1-L4 | Actor | Cổng SMS (ACT-09) | «actor» | - | Tác nhân hệ thống ngoài | 580 | 40 | 120 | 620 |
| SS04-WB1-FR-G1 | Gate | sendSms | - | SS04-WB1-FR | Gate vào khung, message STT 1 | 15 | 115 | 10 | 10 |
| SS04-WB1-FR-G2 | Gate | InvalidPhoneNumber | - | SS04-WB1-FR | Gate ra khung, message STT 2 | 15 | 155 | 10 | 10 |
| SS04-WB1-FR-G3 | Gate | InvalidNotificationContent | - | SS04-WB1-FR | Gate ra khung, message STT 3 | 15 | 195 | 10 | 10 |
| SS04-WB1-FR-G5 | Gate | NotificationReceipt | - | SS04-WB1-FR | Gate ra khung, message STT 5 | 15 | 275 | 10 | 10 |
| SS04-WB1-F1 | Fragment | alt [số điện thoại không hợp lệ] | - | - | đường ngăn SS04-WB1-F1-O2-SEP nét đứt tại y=180; đường ngăn SS04-WB1-F1-O3-SEP nét đứt tại y=220 | 80 | 140 | 160 | 150 |
| SS04-WB1-F2 | Fragment | loop [lần đầu và tối đa 3 lần thử lại, dừng khi dịch vụ phản hồi] | - | - | - | 70 | 370 | 660 | 210 |
| SS04-WB1-F3 | Fragment | opt [lỗi tạm thời hoặc quá 5 giây] | - | SS04-WB1-F2 | - | 80 | 540 | 160 | 30 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS04-WB1-F1 toán hạng 2: [nội dung rỗng]; SS04-WB1-F1 toán hạng 3: [yêu cầu hợp lệ].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS04-WB1-M01 | 1 | SS04-WB1-FR-G1 | SS04-WB1-L1 | sendSms(phone, content) | Đồng bộ | - | sendSms; UC-015 bước 6, 7 |
| SS04-WB1-M02 | 2 | SS04-WB1-L1 | SS04-WB1-FR-G2 | InvalidPhoneNumber | Trả về | SS04-WB1-F1 (toán hạng 1) | sendSms; Q-36 |
| SS04-WB1-M03 | 3 | SS04-WB1-L1 | SS04-WB1-FR-G3 | InvalidNotificationContent | Trả về | SS04-WB1-F1 (toán hạng 2) | sendSms; Q-66 |
| SS04-WB1-M04 | 4 | SS04-WB1-L1 | SS04-WB1-L1 | enqueue(phone, content) | Tự gọi | SS04-WB1-F1 (toán hạng 3) | sendSms |
| SS04-WB1-M05 | 5 | SS04-WB1-L1 | SS04-WB1-FR-G5 | NotificationReceipt | Trả về | SS04-WB1-F1 (toán hạng 3) | sendSms |
| SS04-WB1-M06 | 6 | SS04-WB1-L1 | SS04-WB1-L2 | toSmsMessage(phone, content, notificationKey) | Đồng bộ | - | Gửi ở nền |
| SS04-WB1-M07 | 7 | SS04-WB1-L2 | SS04-WB1-L1 | providerMessage | Trả về | - | Gửi ở nền |
| SS04-WB1-M08 | 8 | SS04-WB1-L1 | SS04-WB1-L3 | send(providerMessage) | Đồng bộ | SS04-WB1-F2 | Gửi ở nền; timeout 5 giây |
| SS04-WB1-M09 | 9 | SS04-WB1-L3 | SS04-WB1-L4 | deliver(providerMessage) | Đồng bộ | SS04-WB1-F2 | UC-015 bước 6, 7 |
| SS04-WB1-M10 | 10 | SS04-WB1-L4 | SS04-WB1-L3 | phản hồi hoặc lỗi | Trả về | SS04-WB1-F2 | UC-015 bước 6, 7 |
| SS04-WB1-M11 | 11 | SS04-WB1-L3 | SS04-WB1-L1 | sendResult | Trả về | SS04-WB1-F2 | Gửi ở nền |
| SS04-WB1-M12 | 12 | SS04-WB1-L1 | SS04-WB1-L1 | waitBeforeRetry(1 phút) | Tự gọi | SS04-WB1-F3 | Thử lại tối đa 3 lần |
| SS04-WB1-M13 | 13 | SS04-WB1-L1 | SS04-WB1-L1 | recordOutcome(sendResult) | Tự gọi | - | Ghi nhật ký; luồng 6a (Q-65) |

Quy tắc ngữ nghĩa đã áp dụng: message mức thiết kế ghi chữ ký với đối số; message bất đồng bộ đầu mũi tên mở, nét liền (endArrow=open;endFill=0;html=1;); client chỉ gọi interface; không có message từ subsystem tới lớp giao diện người dùng; mỗi message đi qua khung sd có một gate riêng.

## F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-SmsGatewayFacade | SmsGatewayFacade | Điều phối | Hiện thực IF-04: kiểm tra số điện thoại và nội dung, sinh notificationKey, giữ hàng chờ gửi nền, gọi Mapper và Client, thử lại tối đa 3 lần cách 1 phút, ghi nhật ký kết quả cuối | package-private | IF-04 |
| DC-SmsMessageMapper | SmsMessageMapper | Chuyển đổi dữ liệu | Đổi PhoneNumber và NotificationContent thành thông điệp của cổng SMS | package-private | - |
| DC-SmsGatewayClient | SmsGatewayClient | Giao tiếp ngoài | Proxy gọi API REST của cổng SMS; timeout 5 giây; phân loại phản hồi | package-private | - |
| DC-SmsGatewayConfig | SmsGatewayConfig | Lưu trữ trong subsystem | Giữ địa chỉ cổng và thông tin xác thực lấy từ cấu hình môi trường | package-private | - |
| DC-InvalidPhoneNumber | InvalidPhoneNumber (PKG-24) | Ngoại lệ | Số điện thoại không đúng định dạng | public | - |

b) Class diagram phần tử: trang "Phần tử" (SS04-EL). Tọa độ bảng Node là tuyệt đối trên trang; file .drawio ghi tọa độ của phần tử con tương đối theo khung subsystem. Kiểu dữ liệu và ngoại lệ ở F5 a không vẽ lại ở sơ đồ.

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-04 | Subsystem | SS-04 SmsMessaging | «subsystem» | - | Khung subsystem | 40 | 180 | 1060 | 200 |
| IF-04 | Interface | IF-04 ISmsGateway | «interface» | PKG-24 | Interface subsystem cung cấp | 320 | 40 | 240 | 60 |
| DC-SmsMessageMapper | Class | SmsMessageMapper | «mapper» | SS-04 | Chuyển đổi dữ liệu | 80 | 260 | 200 | 60 |
| DC-SmsGatewayFacade | Class | SmsGatewayFacade | «facade» | SS-04 | Điều phối; hiện thực IF-04 | 340 | 260 | 200 | 60 |
| DC-SmsGatewayClient | Class | SmsGatewayClient | «adapter» | SS-04 | Giao tiếp ngoài | 600 | 260 | 200 | 60 |
| DC-SmsGatewayConfig | Class | SmsGatewayConfig | «config» | SS-04 | Cấu hình địa chỉ và thông tin xác thực | 860 | 260 | 200 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS04-EL-E1 | DC-SmsGatewayFacade | IF-04 | Realization | - | Facade hiện thực IF-04 | - |
| SS04-EL-E2 | DC-SmsGatewayFacade | DC-SmsMessageMapper | Dependency | «use» | Chuyển đổi nội dung và số điện thoại | - |
| SS04-EL-E3 | DC-SmsGatewayFacade | DC-SmsGatewayClient | Dependency | «use» | Gửi qua client | - |
| SS04-EL-E4 | DC-SmsGatewayClient | DC-SmsGatewayConfig | Dependency | «use» | Đọc địa chỉ và thông tin xác thực | - |

c) Cơ chế kiến trúc áp dụng

| Cơ chế | Nguồn | Cách tích hợp |
|---|---|---|
| Bảo mật dữ liệu | P09 F7 (số điện thoại là dữ liệu cần bảo vệ, truyền qua kênh mã hoá) | Lời gọi qua kênh mã hoá; nhật ký ghi notificationKey và số điện thoại đã che bớt chữ số. |
| Giao dịch và xử lý lặp lại | P09 F7 | notificationKey giữ nguyên ở mọi lần thử lại. |
| Ghi nhật ký | Thiết kế: P09 F7 không nêu | Ghi mỗi lần gửi và kết quả cuối; lý do: chưa chốt xử lý khi gửi không được (Q-65). |
| Cấu hình địa chỉ và thông tin xác thực | Thiết kế: P09 F7 không nêu | DC-SmsGatewayConfig đọc từ cấu hình môi trường; lý do: cổng SMS có thể đổi nhà cung cấp (KHA_NANG_THAY_DOI_GIAO_DIEN ở P10). |
| Gửi ở nền | P09 F7 (Thiết kế: gửi thông báo qua tiến trình nền, NFR-01) | Hàng chờ gửi nền nằm trong DC-SmsGatewayFacade; mất khi tiến trình dừng (Q-88). |

## F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-04 | PKG-32 (DC-PhoneNumber) | Vào package | Chữ ký sendSms dùng DC-PhoneNumber (P10 PKG-32) | Dùng thận trọng |

Trang "Phụ thuộc" (SS04-DP)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-04 | SubsystemBox | SS-04 SmsMessaging | «subsystem» | - | Subsystem đang xét | 40 | 40 | 240 | 60 |
| PKG-32 | Package | PKG-32 ValueTypes | - | PKG-04 Domain | Chứa DC-PhoneNumber | 420 | 40 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS04-DP-E1 | SS-04 | PKG-32 | Dependency | «use» | Vào package: chữ ký IF-04 dùng DC-PhoneNumber | - |

## F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| sendSms | Số điện thoại không đúng định dạng | Nghiệp vụ | Kiểm tra đầu vào | Từ chối ngay | InvalidPhoneNumber | 6a (không gửi được thông báo) | Q-36, Q-65 |
| sendSms | Nội dung thông báo rỗng | Nghiệp vụ | Kiểm tra đầu vào | Từ chối ngay | InvalidNotificationContent | Dữ liệu ra 1 của UC-015 (nội dung thông báo); lỗi lập nội dung của control, không là luồng nghiệp vụ | Q-66 |
| sendSms | Cổng từ chối số điện thoại (số không tồn tại, bị chặn) | Nghiệp vụ | Phản hồi từ chối của cổng | Không thử lại, ghi nhật ký | Không trả (bất đồng bộ) | 6a | Q-65 |
| sendSms | Mất kết nối hoặc cổng quá tải | Kỹ thuật tạm thời | Lỗi kết nối hoặc mã báo tạm thời | Thử lại tối đa 3 lần cách 1 phút (CHINH_SACH_LOI) | Không trả | 6a | Q-65, Q-79 |
| sendSms | Quá 5 giây sau khi đã gửi | Không rõ kết quả | Hết thời gian chờ | Như dòng trên; có thể gửi trùng một SMS, chấp nhận vì chỉ tốn một tin nhắn | Không trả | 6a | Q-65 |
| sendSms | Hết 3 lần thử lại vẫn thất bại | Kỹ thuật tạm thời | Bộ đếm lần thử lại | Dừng thử, ghi nhật ký SMS chưa tới | Không trả | 6a | Q-65, Q-79 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | IF-04: SS04-EL-E1 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Không áp dụng | SS-04 không dùng interface nào |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Xem F5 a |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt | sendSms: SS04-WB1 |

## Câu hỏi mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Vấn đề còn mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).
