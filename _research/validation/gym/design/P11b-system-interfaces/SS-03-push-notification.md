# P11b - SS-03 PushNotification - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | SS-03 PushNotification (package PKG-24 NotificationChannels); lần chạy đầu cho mọi subsystem của P10 F2 |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102, ghi ở file chung P11b-system-interfaces.md); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-015 Huỷ lớp nhóm ít người đặt | AC-C-CancelUnderBookedClassHandler (DC-CancelUnderBookedClassHandler) | SD1b STT 1.8 sendPushNotification (hội viên, lớp nhóm bị huỷ), bước 6, 7 | Hội viên nhận thông báo; nội dung thông báo lớp bị huỷ (loại lớp, giờ học; nội dung đầy đủ: Q-66) | 6a (dịch vụ thông báo đẩy không gửi được), chờ Q-65 và Q-79 |

- UC-005 (luồng 9a2, 10a) có thể dùng IF-03 nếu Q-53 chọn thông báo đẩy; UC-008, UC-011, UC-014 chưa có P04, P07. Khi có, chạy lại P11b cho SS-03 để thêm UC dùng IF-03.

## F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-03 | IPushNotificationGateway | Nhận yêu cầu gửi thông báo đẩy tới một hội viên và chuyển cho dịch vụ thông báo đẩy. | SS-03 PushNotification | DC-CancelUnderBookedClassHandler (PKG-15) | PKG-24 NotificationChannels |

- Số operation: IF-03 có 1. Tên interface theo vai trò, không theo nhà cung cấp.
- Layer: IF-03 ở PKG-24 (Services); DC-Member ở PKG-26 (Domain); DC-NotificationContent, DC-NotificationReceipt ở PKG-24.

## F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-03 | IPushNotificationGateway | Dịch vụ thông báo đẩy (ACT-10) | sendPushNotification(recipient: Member, content: NotificationContent): NotificationReceipt | recipient: Member - hội viên có kênh thông báo là thông báo đẩy (BR-14)<br>content: NotificationContent - đã soạn, không rỗng (nội dung: Q-66) | NotificationReceipt: status (Accepted), notificationKey: string (khoá do phần mềm sinh) | InvalidNotificationContent (Nghiệp vụ, kiểm tra đầu vào); lỗi gửi xảy ra ở nền và chỉ ghi nhật ký (Kỹ thuật tạm thời, Không rõ kết quả) | UC-015 (bước 6, 7) | Control đã xác định kênh của hội viên là thông báo đẩy | Yêu cầu nằm trong hàng chờ gửi nền; đã thử gửi tới 4 lần (1 lần đầu, tối đa 3 lần thử lại) khi cần | Bất đồng bộ (P09 F7: gửi qua tiến trình nền) | Có với khoá idempotency do hệ thống sinh (notificationKey); dịch vụ chưa có tài liệu nên nhận trùng được chấp nhận vì không có tác dụng phụ tài chính | 5 giây mỗi lần gửi (CHINH_SACH_LOI) |

- Ánh xạ trách nhiệm P08 của AC-B-PushNotificationGateway: // sendPushNotification --> IF-03.sendPushNotification.
- Địa chỉ thiết bị nhận thông báo đẩy của hội viên chưa có trong mô hình (AC-E-Member không có thuộc tính này); nguồn lấy địa chỉ chờ Q-101. Chữ ký nhận DC-Member để SS-03 tự tra địa chỉ, tránh để lộ địa chỉ thiết bị ra control.
- Xử lý khi gửi không được (gửi lại sau, thử kênh còn lại, bỏ qua) là giá trị nghiệp vụ chờ Q-65, Q-79; SS-03 chỉ thử lại cùng kênh theo CHINH_SACH_LOI rồi ghi nhật ký.

## F4. Sequence diagram

File diagrams/P11b-subsystem-SS-03.drawio gồm 4 trang: "Hộp đen - UC-015 gửi thông báo lớp bị huỷ"; "Hộp trắng - sendPushNotification"; "Phần tử"; "Phụ thuộc". STT đánh số phẳng theo trục thời gian trong mỗi trang; tọa độ bảng Node là tuyệt đối. Gate nằm trên cạnh trái khung sd, tâm gate ở y của message nên x, y của gate lệch 5 so với bội số của 10 (xem Vấn đề còn mở).

### Trang "Hộp đen - UC-015 gửi thông báo lớp bị huỷ" (SS03-BB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS03-BB1-FR | Fragment | sd Hộp đen UC-015 thông báo đẩy | - | - | Khung sd của trang | 20 | 0 | 420 | 280 |
| SS03-BB1-L1 | Lifeline | :CancelUnderBookedClassHandler | «control» | - | DC-CancelUnderBookedClassHandler (PKG-15) | 100 | 40 | 120 | 220 |
| SS03-BB1-L2 | Lifeline | :IF-03 IPushNotificationGateway | «interface» | - | Subsystem SS-03 hiện thực | 260 | 40 | 120 | 220 |
| SS03-BB1-F1 | Fragment | loop [mỗi hội viên có kênh là thông báo đẩy (BR-14)] | - | - | - | 70 | 90 | 340 | 130 |
| SS03-BB1-F2 | Fragment | alt [yêu cầu được nhận vào hàng chờ gửi] | - | SS03-BB1-F1 | đường ngăn SS03-BB1-F2-O2-SEP nét đứt tại y=180 | 80 | 140 | 320 | 70 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS03-BB1-F2 toán hạng 2: [nội dung không hợp lệ].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS03-BB1-M01 | 1 | SS03-BB1-L1 | SS03-BB1-L2 | sendPushNotification(recipient, content) | Đồng bộ | SS03-BB1-F1 | UC-015 bước 6, 7; sendPushNotification |
| SS03-BB1-M02 | 2 | SS03-BB1-L2 | SS03-BB1-L1 | NotificationReceipt | Trả về | SS03-BB1-F2 (toán hạng 1) | UC-015 bước 6, 7 |
| SS03-BB1-M03 | 3 | SS03-BB1-L2 | SS03-BB1-L1 | InvalidNotificationContent | Trả về | SS03-BB1-F2 (toán hạng 2) | UC-015 bước 6; Q-66 |

### Trang "Hộp trắng - sendPushNotification" (SS03-WB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS03-WB1-FR | Fragment | sd sendPushNotification | - | - | Khung sd của trang | 20 | 0 | 740 | 640 |
| SS03-WB1-L1 | Lifeline | :PushFacade | «facade» | SS-03 | DC-PushFacade; hiện thực IF-03 | 100 | 40 | 120 | 580 |
| SS03-WB1-L2 | Lifeline | :PushMessageMapper | «mapper» | SS-03 | DC-PushMessageMapper | 260 | 40 | 120 | 580 |
| SS03-WB1-L3 | Lifeline | :PushClient | «adapter» | SS-03 | DC-PushClient | 420 | 40 | 120 | 580 |
| SS03-WB1-L4 | Actor | Dịch vụ thông báo đẩy (ACT-10) | «actor» | - | Tác nhân hệ thống ngoài | 580 | 40 | 120 | 580 |
| SS03-WB1-FR-G1 | Gate | sendPushNotification | - | SS03-WB1-FR | Gate vào khung, message STT 1 | 15 | 115 | 10 | 10 |
| SS03-WB1-FR-G2 | Gate | InvalidNotificationContent | - | SS03-WB1-FR | Gate ra khung, message STT 2 | 15 | 155 | 10 | 10 |
| SS03-WB1-FR-G4 | Gate | NotificationReceipt | - | SS03-WB1-FR | Gate ra khung, message STT 4 | 15 | 235 | 10 | 10 |
| SS03-WB1-F1 | Fragment | alt [nội dung rỗng] | - | - | đường ngăn SS03-WB1-F1-O2-SEP nét đứt tại y=180 | 80 | 140 | 160 | 110 |
| SS03-WB1-F2 | Fragment | loop [lần đầu và tối đa 3 lần thử lại, dừng khi dịch vụ phản hồi] | - | - | - | 70 | 330 | 660 | 210 |
| SS03-WB1-F3 | Fragment | opt [lỗi tạm thời hoặc quá 5 giây] | - | SS03-WB1-F2 | - | 80 | 500 | 160 | 30 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS03-WB1-F1 toán hạng 2: [yêu cầu hợp lệ].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS03-WB1-M01 | 1 | SS03-WB1-FR-G1 | SS03-WB1-L1 | sendPushNotification(recipient, content) | Đồng bộ | - | sendPushNotification; UC-015 bước 6, 7 |
| SS03-WB1-M02 | 2 | SS03-WB1-L1 | SS03-WB1-FR-G2 | InvalidNotificationContent | Trả về | SS03-WB1-F1 (toán hạng 1) | sendPushNotification; Q-66 |
| SS03-WB1-M03 | 3 | SS03-WB1-L1 | SS03-WB1-L1 | enqueue(recipient, content) | Tự gọi | SS03-WB1-F1 (toán hạng 2) | sendPushNotification |
| SS03-WB1-M04 | 4 | SS03-WB1-L1 | SS03-WB1-FR-G4 | NotificationReceipt | Trả về | SS03-WB1-F1 (toán hạng 2) | sendPushNotification |
| SS03-WB1-M05 | 5 | SS03-WB1-L1 | SS03-WB1-L2 | toPushMessage(recipient, content, notificationKey) | Đồng bộ | - | Gửi ở nền |
| SS03-WB1-M06 | 6 | SS03-WB1-L2 | SS03-WB1-L1 | providerMessage | Trả về | - | Gửi ở nền |
| SS03-WB1-M07 | 7 | SS03-WB1-L1 | SS03-WB1-L3 | send(providerMessage) | Đồng bộ | SS03-WB1-F2 | Gửi ở nền; timeout 5 giây |
| SS03-WB1-M08 | 8 | SS03-WB1-L3 | SS03-WB1-L4 | deliver(providerMessage) | Đồng bộ | SS03-WB1-F2 | UC-015 bước 6, 7 |
| SS03-WB1-M09 | 9 | SS03-WB1-L4 | SS03-WB1-L3 | phản hồi hoặc lỗi | Trả về | SS03-WB1-F2 | UC-015 bước 6, 7 |
| SS03-WB1-M10 | 10 | SS03-WB1-L3 | SS03-WB1-L1 | sendResult | Trả về | SS03-WB1-F2 | Gửi ở nền |
| SS03-WB1-M11 | 11 | SS03-WB1-L1 | SS03-WB1-L1 | waitBeforeRetry(1 phút) | Tự gọi | SS03-WB1-F3 | Thử lại tối đa 3 lần |
| SS03-WB1-M12 | 12 | SS03-WB1-L1 | SS03-WB1-L1 | recordOutcome(sendResult) | Tự gọi | - | Ghi nhật ký; luồng 6a (Q-65) |

Quy tắc ngữ nghĩa đã áp dụng: message mức thiết kế ghi chữ ký với đối số; message bất đồng bộ đầu mũi tên mở, nét liền (endArrow=open;endFill=0;html=1;); client chỉ gọi interface; không có message từ subsystem tới lớp giao diện người dùng; mỗi message đi qua khung sd có một gate riêng.

## F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-PushNotificationFacade | PushNotificationFacade | Điều phối | Hiện thực IF-03: kiểm tra nội dung, sinh notificationKey, giữ hàng chờ gửi nền, gọi Mapper và Client, thử lại tối đa 3 lần cách 1 phút, ghi nhật ký kết quả cuối | package-private | IF-03 |
| DC-PushMessageMapper | PushMessageMapper | Chuyển đổi dữ liệu | Đổi NotificationContent và hội viên nhận thành thông điệp của dịch vụ thông báo đẩy | package-private | - |
| DC-PushServiceClient | PushServiceClient | Giao tiếp ngoài | Proxy gọi dịch vụ thông báo đẩy của nền tảng; timeout 5 giây; phân loại phản hồi | package-private | - |
| DC-PushServiceConfig | PushServiceConfig | Lưu trữ trong subsystem | Giữ địa chỉ dịch vụ và thông tin xác thực lấy từ cấu hình môi trường | package-private | - |
| DC-NotificationContent | NotificationContent (PKG-24) | Kiểu dữ liệu | Nội dung thông báo đã soạn (tiêu đề, nội dung; thông tin cần có: Q-66); dùng chung với SS-04 | public | - |
| DC-NotificationReceipt | NotificationReceipt (PKG-24) | Kiểu dữ liệu | status, notificationKey; dùng chung với SS-04 | public | - |
| DC-InvalidNotificationContent | InvalidNotificationContent (PKG-24) | Ngoại lệ | Nội dung rỗng; dùng chung với SS-04 | public | - |

b) Class diagram phần tử: trang "Phần tử" (SS03-EL). Tọa độ bảng Node là tuyệt đối trên trang; file .drawio ghi tọa độ của phần tử con tương đối theo khung subsystem. Kiểu dữ liệu và ngoại lệ ở F5 a không vẽ lại ở sơ đồ.

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-03 | Subsystem | SS-03 PushNotification | «subsystem» | - | Khung subsystem | 40 | 180 | 1060 | 200 |
| IF-03 | Interface | IF-03 IPushNotificationGateway | «interface» | PKG-24 | Interface subsystem cung cấp | 320 | 40 | 240 | 60 |
| DC-PushMessageMapper | Class | PushMessageMapper | «mapper» | SS-03 | Chuyển đổi dữ liệu | 80 | 260 | 200 | 60 |
| DC-PushNotificationFacade | Class | PushNotificationFacade | «facade» | SS-03 | Điều phối; hiện thực IF-03 | 340 | 260 | 200 | 60 |
| DC-PushServiceClient | Class | PushServiceClient | «adapter» | SS-03 | Giao tiếp ngoài | 600 | 260 | 200 | 60 |
| DC-PushServiceConfig | Class | PushServiceConfig | «config» | SS-03 | Cấu hình địa chỉ và thông tin xác thực | 860 | 260 | 200 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS03-EL-E1 | DC-PushNotificationFacade | IF-03 | Realization | - | Facade hiện thực IF-03 | - |
| SS03-EL-E2 | DC-PushNotificationFacade | DC-PushMessageMapper | Dependency | «use» | Chuyển đổi nội dung thông báo | - |
| SS03-EL-E3 | DC-PushNotificationFacade | DC-PushServiceClient | Dependency | «use» | Gửi qua client | - |
| SS03-EL-E4 | DC-PushServiceClient | DC-PushServiceConfig | Dependency | «use» | Đọc địa chỉ và thông tin xác thực | - |

c) Cơ chế kiến trúc áp dụng

| Cơ chế | Nguồn | Cách tích hợp |
|---|---|---|
| Bảo mật dữ liệu | P09 F7 (họ tên, số điện thoại là dữ liệu cần bảo vệ, truyền qua kênh mã hoá) | Lời gọi qua kênh mã hoá; nội dung gửi đi chỉ gồm thông tin cần cho thông báo; nhật ký ghi notificationKey, không ghi nội dung. |
| Giao dịch và xử lý lặp lại | P09 F7 | notificationKey giữ nguyên ở mọi lần thử lại để dịch vụ (nếu hỗ trợ) loại trùng. |
| Ghi nhật ký | Thiết kế: P09 F7 không nêu | Ghi mỗi lần gửi và kết quả cuối; lý do: chưa chốt cách xử lý khi gửi không được (Q-65), cần dấu vết thông báo chưa tới. |
| Cấu hình địa chỉ và thông tin xác thực | Thiết kế: P09 F7 không nêu | DC-PushServiceConfig đọc từ cấu hình môi trường; lý do: giao thức dịch vụ chưa có tài liệu (NFR-10). |
| Gửi ở nền | P09 F7 (Thiết kế: gửi thông báo qua tiến trình nền để không làm chậm đường đặt chỗ, NFR-01) | Hàng chờ gửi nền nằm trong DC-PushNotificationFacade; mất khi tiến trình dừng (Q-88). |

## F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-03 | PKG-26 (DC-Member) | Vào package | Chữ ký sendPushNotification nhận hội viên để SS-03 tra địa chỉ thiết bị (Q-101); entity ở Domain dùng trực tiếp trong chữ ký | Dùng thận trọng |

Trang "Phụ thuộc" (SS03-DP)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-03 | SubsystemBox | SS-03 PushNotification | «subsystem» | - | Subsystem đang xét | 40 | 40 | 240 | 60 |
| PKG-26 | Package | PKG-26 Account | - | PKG-04 Domain | Chứa DC-Member | 420 | 40 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS03-DP-E1 | SS-03 | PKG-26 | Dependency | «use» | Vào package: chữ ký IF-03 dùng DC-Member | - |

## F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| sendPushNotification | Nội dung thông báo rỗng | Nghiệp vụ | Kiểm tra đầu vào | Từ chối ngay, không đưa vào hàng chờ | InvalidNotificationContent | Dữ liệu ra 1 của UC-015 (nội dung thông báo); nội dung rỗng là lỗi lập nội dung của control, không là luồng nghiệp vụ | Q-66 |
| sendPushNotification | Hội viên chưa có địa chỉ thiết bị nhận thông báo đẩy | Nghiệp vụ | Tra địa chỉ trước khi gửi ở nền | Không thử lại, ghi nhật ký | Không trả (bất đồng bộ) | 6a | Q-101, Q-36, Q-65 |
| sendPushNotification | Dịch vụ từ chối thông báo (địa chỉ thiết bị hết hạn) | Nghiệp vụ | Phản hồi từ chối của dịch vụ | Không thử lại, ghi nhật ký | Không trả | 6a | Q-65 |
| sendPushNotification | Mất kết nối hoặc dịch vụ quá tải | Kỹ thuật tạm thời | Lỗi kết nối hoặc mã báo tạm thời | Thử lại tối đa 3 lần cách 1 phút (CHINH_SACH_LOI) | Không trả | 6a | Q-65, Q-79 |
| sendPushNotification | Quá 5 giây sau khi đã gửi | Không rõ kết quả | Hết thời gian chờ | Như dòng trên; thông báo không có tác dụng phụ tài chính nên nhận trùng được chấp nhận | Không trả | 6a | Q-65 |
| sendPushNotification | Hết 3 lần thử lại vẫn thất bại | Kỹ thuật tạm thời | Bộ đếm lần thử lại | Dừng thử, ghi nhật ký thông báo chưa tới | Không trả | 6a | Q-65, Q-79 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | IF-03: SS03-EL-E1 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Không áp dụng | SS-03 không dùng interface nào |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Xem F5 a |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt | sendPushNotification: SS03-WB1 |

## Câu hỏi mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Vấn đề còn mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).
