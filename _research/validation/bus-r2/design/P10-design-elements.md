# P10 - Phần tử thiết kế - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P10 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (mục 3 đã thay NEN_TANG, CONG_NGHE bằng khối F11 của P09); P08-analysis-model.md (phiên bản 1.0; F3, F4, Câu hỏi mở, Giả định, Vấn đề còn mở); P09-architecture.md (phiên bản 1.0; F3, F4, F5, F6, F7, F11, Câu hỏi mở, Giả định); P01-actors.md (phiên bản 1.0, Mục 2); P02-usecases.md (phiên bản 1.1, Mục 4); P03-usecase-model.md (phiên bản 1.0, Mục 1 và 2, quan hệ extend); P06-supplementary-spec.md (phiên bản 1.0, Mục 3 đến 5). Không dùng P07-uc-analysis và P04-uc-specs (đầu vào không bắt buộc, quan hệ giữa lớp đã có ở P08 F4). Placeholder: TIEU_CHI_NHOM_PACKAGE = Không có (dùng tiêu chí mặc định ở A3); KHA_NANG_THAY_DOI_GIAO_DIEN = Không có (suy từ NFR và hồ sơ; không đủ căn cứ nên coi giao diện là dễ thay đổi); YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-65, ASM-48; lần chạy này không cấp mã Q, ASM mới. Mã PKG lớn nhất của P09: PKG-30; lần chạy này cấp PKG-31. Mã SS, IF, DC cấp mới từ SS-01, IF-01 |
| Phạm vi | Toàn hệ thống; phần tử thiết kế chỉ có cho 14 lớp phân tích của 2 use case UC-009, UC-017 (P08 phiên bản 1.0), 15 package của P09 còn lại giữ chỗ |
| Mã Q, ASM cuối đã cấp | Q-65, ASM-48 |

Kiểm tra đầu vào (A0): hồ sơ dự án đã chốt NEN_TANG là ứng dụng web dựng phía máy chủ kèm ứng dụng Android gốc, CONG_NGHE là Java 17, Spring Boot, Thymeleaf, PostgreSQL; Kotlin, Android, SQLite. Mẫu phía giao diện của P09 F3 (MVC passive cho web, MVVM cho máy soát vé) khớp công nghệ này, nên không có Đề xuất sửa P09 và không phát sinh Q-nn từ A0. Các Q-38, Q-62 đến Q-65 và ASM-45 đến ASM-48 của P09 vẫn mở; P10 kế thừa và không đổi chúng.

## F1. Subsystem ứng viên và quyết định

| Lớp phân tích (AC) | Tiêu chí thoả | Quyết định | Lý do |
|---|---|---|---|
| AC-B-SmsGateway | Hệ thống ngoài; Dịch vụ phức tạp dùng chung (UC-009, UC-017; UC-003, UC-014 theo NFR-12); Có thể thay thế (đổi nhà mạng; KHA_NANG_THAY_DOI_GIAO_DIEN không có thông tin nên coi là dễ thay đổi) | Subsystem | Boundary giao diện hệ thống ngoài và kênh thông báo đi qua dịch vụ ngoài (P09 F5 dòng boundary kênh thông báo, dòng boundary giao diện hệ thống). Thành SS-02 SmsNotification hiện thực IF-02 ISmsGateway |
| AC-B-PaymentGateway | Hệ thống ngoài; Có thể thay thế (đổi đối tác cổng, API chưa có tài liệu); Bảo mật (NFR-01: thông tin thẻ không đi qua hệ thống, nên chỉ cho lọt dữ liệu cần thiết qua một interface) | Subsystem | Boundary giao diện hệ thống ngoài (P09 F5). Thành SS-01 OnlinePayment hiện thực IF-01 IPaymentGateway; control chỉ thấy kết quả thành công hoặc không thành công (P09 F7) |
| AC-B-BookTicketOnlineForm | - | Không | Boundary giao diện người dùng của ACT-01; thành View và RequestHandler ở Presentation theo P09 F5, không là hệ thống ngoài hay thiết bị |
| AC-B-CancelTripForm | - | Không | Boundary giao diện người dùng của ACT-03; như trên |
| AC-C-BookTicketOnlineController | - | Không | Điều phối luồng đặt vé; độ dài điều phối không là tiêu chí subsystem. Thành lớp dịch vụ ứng dụng ở Application |
| AC-C-SearchTripsController | - | Không | Control tạm của UC-008, như trên |
| AC-C-PayTicketOnlineController | - | Không | Control tạm của UC-010; phần che giấu giao thức cổng thanh toán đã nằm ở SS-01 |
| AC-C-CancelTripController | - | Không | Điều phối luồng huỷ chuyến, như trên |
| AC-E-Trip | - | Không | Entity ở Domain, không che giấu dịch vụ nào |
| AC-E-Seat | - | Không | Entity ở Domain |
| AC-E-Fare | - | Không | Entity ở Domain |
| AC-E-Booking | - | Không | Entity ở Domain |
| AC-E-Ticket | - | Không | Entity ở Domain; nhiều trách nhiệm (P08 F6, Vấn đề còn mở) nhưng là hành vi nghiệp vụ cần dùng chung, không phải dịch vụ có thể thay thế; P12 xét tách phần tập vé của chuyến |
| AC-E-PaymentTransaction | - | Không | Entity ở Domain |
| - (ACT-09, PKG-11 TimerTrigger) | - | Không | Bộ định thời nội bộ, đọc mốc từ dữ liệu bền rồi gọi Application, không có logic nghiệp vụ, không thuộc hệ thống ngoài hay thiết bị và không có NFR đòi thay thế (P09 F7). Thành lớp DC-HoldExpiryTrigger ở PKG-11 (F3) |
| - (PKG-20 Persistence) | Sản phẩm có sẵn (thư viện truy cập dữ liệu của nền tảng) | Không | Phần hiện thực interface kho dữ liệu không thành subsystem; ghi ở bảng phần tử thiết kế mới do cơ chế kiến trúc (F3) |
| - (ACT-08, PKG-23 TicketPrinting) | Thiết bị | Không (giữ chỗ) | Chỉ phục vụ UC-004, UC-006, UC-015 chưa có P07 nên P08 chưa có lớp nguồn. Giữ chỗ PKG-23 ở F4; tạo SS khi P08 phủ các use case này (Vấn đề còn mở) |
| - (ACT-05 Phụ xe, PKG-09 BoardingApi, PKG-25 LocalStore, PKG-26 BoardingSyncClient) | Thiết bị; Có thể thay thế | Không (giữ chỗ) | Máy soát vé là node của chính hệ thống, không là tác nhân (ASM-10); UC-025, UC-026 chưa có P07. Giữ chỗ ở F4 (Vấn đề còn mở) |
| - (PKG-24 Security) | Bảo mật; Sản phẩm có sẵn | Không (giữ chỗ) | Chỉ phục vụ UC-003 chưa có P07. Giữ chỗ ở F4 |

## F2. Bảng subsystem

| SS | Tên | Interface (IF) | Trách nhiệm | Che giấu phần tử nào | AC nguồn | ACT liên quan | PKG chứa |
|---|---|---|---|---|---|---|---|
| SS-01 | OnlinePayment | IF-01 IPaymentGateway | // requestTicketRefund: chuyển yêu cầu hoàn tiền một vé (giao dịch thanh toán, mã vé, số tiền hoàn) cho Cổng thanh toán và trả kết quả thành công hoặc không thành công (UC-017; NFR-11, ASM-32, ASM-33) | Giao thức và định dạng thông điệp của API thanh toán và hoàn tiền (chưa có tài liệu); chuyển đổi giữa kiểu giá trị của hệ thống và dữ liệu của cổng; quản lý kết nối và thời gian chờ, coi không có phản hồi là không thành công (ASM-37); không giữ dữ liệu thẻ (NFR-01) | AC-B-PaymentGateway | ACT-06 Cổng thanh toán | PKG-21 |
| SS-02 | SmsNotification | IF-02 ISmsGateway | // sendTicketCodesBySms: chuyển yêu cầu gửi SMS mã vé cho Cổng SMS và trả kết quả của lời gọi (UC-009; NFR-12)<br>// sendTripCancellationBySms: chuyển yêu cầu gửi SMS thông báo huỷ chuyến (số điện thoại, tuyến, giờ xuất bến, mã vé) cho Cổng SMS và trả kết quả của lời gọi (UC-017; NFR-12, ASM-30) | Giao thức API REST của Cổng SMS; dựng nội dung tin nhắn từ dữ liệu được truyền; quản lý kết nối và phân loại kết quả lời gọi (gửi được hoặc không); không đảo ngược dữ liệu đã lưu khi gửi lỗi (NFR-12) | AC-B-SmsGateway | ACT-07 Cổng SMS | PKG-22 |

Ghi chú: thu tiền vé qua Cổng thanh toán (NFR-10) và SMS mã xác thực đăng nhập (NFR-12, UC-003) là năng lực của hai subsystem này nhưng chưa có trách nhiệm trong lớp phân tích nguồn vì P07 của UC-010, UC-003 chưa có; P11b và P08 chạy lại sẽ bổ sung.

Bảng Interface gọi ngược:

| IF | Tên | Định nghĩa tại PKG | Subsystem gọi | Lớp hiện thực (DC, PKG) | Trách nhiệm | Nguồn (P09 A5, UC) |
|---|---|---|---|---|---|---|
| Không có | - | - | - | - | - | - |

Lý do không có dòng nào: Cổng thanh toán không tự gửi thông báo, hệ thống gọi cổng và nhận kết quả bằng giá trị trả về (ASM-11, P09 F7); Cổng SMS là kênh một chiều từ hệ thống tới cổng (NFR-12); P09 QT-8 ghi hiện không có chỗ nào layer dưới cần gọi ngược lên layer trên. DC-HoldExpiryTrigger ở Presentation gọi xuống DC-BookTicketOnlineService, đây là lời gọi đi xuống nên không cần interface gọi ngược. Máy in vé và máy soát vé chưa có subsystem (F1), nên chưa có sự kiện thiết bị đẩy vào hệ thống; xét lại khi tạo SS cho hai thiết bị này.

## F3. Bảng ánh xạ lớp phân tích sang phần tử thiết kế

| AC | Kết quả (Lớp thiết kế DC / Subsystem SS / Package / Tách thành nhiều lớp) | Phần tử thiết kế | PKG | Lý do |
|---|---|---|---|---|
| AC-B-BookTicketOnlineForm | Tách thành nhiều lớp | DC-BookTicketOnlineView<br>DC-BookTicketOnlineRequestHandler | PKG-05 | P09 F3, F5 chọn MVC passive cho web: bảng ánh xạ stereotype tách View (hiển thị, nhận nhập liệu) và Controller của MVC (tiếp nhận thao tác, chọn view). Đặt tên RequestHandler để không trùng DC-BookTicketOnlineService và thuật ngữ "controller" của lớp control phân tích |
| AC-B-SmsGateway | Subsystem | SS-02 SmsNotification (IF-02 ISmsGateway) | PKG-22 | Xem F1, F2 |
| AC-C-BookTicketOnlineController | Tách thành nhiều lớp | DC-BookTicketOnlineService<br>DC-HoldExpiryTrigger | PKG-13<br>PKG-11 | Hai nhóm trách nhiệm ít liên quan: điều phối luồng đặt vé (startBookTicketOnline, processSeatSelection, processTravelerInfo, requestCancelBooking, handleHoldExpiry) và nhận mốc thời gian hết hạn giữ chỗ. P09 F5: phần chờ hết thời hạn do PKG-11 kích hoạt từ dữ liệu bền, control không giữ bộ đếm trong bộ nhớ; startWaitingForPaymentResult, stopWaitingForPaymentResult do P12 chốt thành thao tác ghi, xoá thời hạn giữ chỗ trên Booking. Lớp Application đổi tên Controller thành Service vì Controller là vai trò của MVC passive ở Presentation (P09 F5 lưu ý) |
| AC-C-SearchTripsController | Lớp thiết kế | DC-SearchTripsService | PKG-13 | Ánh xạ 1-1; đổi tên Controller thành Service như dòng trên. Control tạm chờ P07 của UC-008 (P08 F3) |
| AC-C-PayTicketOnlineController | Lớp thiết kế | DC-PayTicketOnlineService | PKG-13 | Ánh xạ 1-1; đổi tên như dòng trên. Control tạm chờ P07 của UC-010 (P08 F3) |
| AC-E-Trip | Lớp thiết kế | DC-Trip | PKG-27 | Lớp đơn giản, một trừu tượng |
| AC-E-Seat | Lớp thiết kế | DC-Seat | PKG-28 | Lớp đơn giản, một trừu tượng |
| AC-E-Fare | Lớp thiết kế | DC-Fare | PKG-27 | Lớp đơn giản, một trừu tượng |
| AC-E-Booking | Lớp thiết kế | DC-Booking | PKG-28 | Lớp đơn giản, một trừu tượng |
| AC-E-Ticket | Lớp thiết kế | DC-Ticket | PKG-28 | Lớp đơn giản, một trừu tượng; giữ nguyên các trách nhiệm tác động lên tập vé của chuyến theo P08 (Vấn đề còn mở), P12 quyết định tách |
| AC-B-CancelTripForm | Tách thành nhiều lớp | DC-CancelTripView<br>DC-CancelTripRequestHandler | PKG-07 | Như AC-B-BookTicketOnlineForm: P09 tách View và Controller của MVC passive |
| AC-B-PaymentGateway | Subsystem | SS-01 OnlinePayment (IF-01 IPaymentGateway) | PKG-21 | Xem F1, F2 |
| AC-C-CancelTripController | Lớp thiết kế | DC-CancelTripService | PKG-16 | Ánh xạ 1-1; đổi tên Controller thành Service như trên. cancelOverdueReservationMark và cancelPassengerListMark (ASM-28) giữ làm trách nhiệm kế thừa; P09 F7 cho PKG-11 đọc trạng thái chuyến từ dữ liệu bền, P12 xác định hai việc này thành thao tác thật hay chỉ là hệ quả của trạng thái Đã huỷ |
| AC-E-PaymentTransaction | Lớp thiết kế | DC-PaymentTransaction | PKG-29 | Lớp đơn giản, một trừu tượng |

Thống kê: 14 lớp phân tích hoạt động hoặc tạm, mỗi lớp một dòng; 6 ánh xạ 1-1 giữ tên (6 entity), 3 ánh xạ 1-1 đổi tên, 3 dòng tách thành nhiều lớp (21%), 2 subsystem.

Bảng phần tử thiết kế mới do cơ chế kiến trúc (không từ lớp phân tích):

| DC hoặc IF | Tên | PKG | Cơ chế | Nguồn (P09 mục, NFR) |
|---|---|---|---|---|
| DC-BookTicketOnlineViewModel | BookTicketOnlineViewModel | PKG-13 | MVC passive: dữ liệu đưa cho View là view model do Application cấp, Presentation không phụ thuộc Domain | P09 F3 (mẫu phía giao diện), QT-4; thuộc tính selectedSeats, issuedTickets, totalAmount của AC-B-BookTicketOnlineForm |
| DC-CancelTripViewModel | CancelTripViewModel | PKG-16 | Như trên | P09 F3, QT-4; thuộc tính scheduledTrips, cancellationResult của AC-B-CancelTripForm |
| IF-03 | ITripRepository | PKG-27 | Persistence: interface kho dữ liệu ở Domain | P09 F5 (entity phần lưu trữ), QT-5; AC-E-Trip |
| IF-04 | IFareRepository | PKG-27 | Persistence | P09 F5, QT-5; AC-E-Fare |
| IF-05 | ISeatRepository | PKG-28 | Persistence | P09 F5, QT-5; AC-E-Seat; NFR-04 |
| IF-06 | IBookingRepository | PKG-28 | Persistence | P09 F5, QT-5; AC-E-Booking |
| IF-07 | ITicketRepository | PKG-28 | Persistence | P09 F5, QT-5; AC-E-Ticket |
| IF-08 | IPaymentTransactionRepository | PKG-29 | Persistence | P09 F5, QT-5; AC-E-PaymentTransaction; NFR-05, NFR-06 |
| DC-RelationalTripRepository | RelationalTripRepository | PKG-20 | Persistence: hiện thực IF-03 trên cơ sở dữ liệu quan hệ | P09 F7 (loại cơ chế lưu trữ), QT-5 |
| DC-RelationalFareRepository | RelationalFareRepository | PKG-20 | Hiện thực IF-04 | P09 F7, QT-5 |
| DC-RelationalSeatRepository | RelationalSeatRepository | PKG-20 | Hiện thực IF-05 | P09 F7, QT-5; NFR-04 |
| DC-RelationalBookingRepository | RelationalBookingRepository | PKG-20 | Hiện thực IF-06 | P09 F7, QT-5 |
| DC-RelationalTicketRepository | RelationalTicketRepository | PKG-20 | Hiện thực IF-07 | P09 F7, QT-5 |
| DC-RelationalPaymentTransactionRepository | RelationalPaymentTransactionRepository | PKG-20 | Hiện thực IF-08 | P09 F7, QT-5; NFR-05, NFR-06 |
| DC-Money | Money | PKG-31 | Kiểu giá trị dùng trong chữ ký interface ở layer dưới (A3) | Thuộc tính kiểu Số tiền: Fare.amount, Ticket.fare, Booking.seatFare, PaymentTransaction.collectedAmount, refundedAmount, refundAmount của AC-B-PaymentGateway |
| DC-TicketCode | TicketCode | PKG-31 | Như trên | ticketCode của AC-E-Ticket, AC-B-SmsGateway, AC-B-PaymentGateway; BR-04 |
| DC-PaymentTransactionCode | PaymentTransactionCode | PKG-31 | Như trên | transactionCode của AC-E-PaymentTransaction, AC-B-PaymentGateway |
| DC-PhoneNumber | PhoneNumber | PKG-31 | Như trên | travelerPhone của AC-E-Booking, AC-E-Ticket; recipientPhone của AC-B-SmsGateway |

Mỗi entity có một interface kho dữ liệu riêng và một lớp hiện thực riêng; P12 thiết kế operation và có thể gộp theo cụm entity khi lập chi tiết. Không thêm DTO, Mapper cho từng entity vì P09 không yêu cầu.

## F4. Bảng package

Bốn layer PKG-01 đến PKG-04 giữ nguyên như P09 F4. Bảng dưới liệt kê các package PKG-05 đến PKG-30 của P09 (kèm phần tử chứa của P10) và PKG-31 mới. Dòng "Giữ chỗ" là package chưa có lớp phân tích nguồn, trách nhiệm và phụ thuộc giữ nguyên P09 F4, F6.

| PKG | Tên | Layer (PKG) | Trách nhiệm | Phần tử chứa (DC, SS, IF) | Tiêu chí nhóm | Phụ thuộc vào (PKG) |
|---|---|---|---|---|---|---|
| PKG-05 | PassengerWeb | PKG-01 | Hiển thị website đặt vé và tiếp nhận thao tác của hành khách | DC-BookTicketOnlineView, DC-BookTicketOnlineRequestHandler | Cùng tác nhân ACT-01; View trình bày Booking và Ticket; RequestHandler và View trao đổi nhiều message. Boundary tách khỏi lớp nghiệp vụ (giao diện coi là dễ thay đổi) | PKG-13; giữ chỗ P09: PKG-12, PKG-15 |
| PKG-06 | CounterWeb | PKG-01 | Giữ chỗ: giao diện nhân viên bán vé (ACT-02) | Giữ chỗ (UC-003, UC-004, UC-005, UC-006, UC-012, UC-015, UC-018 chưa có P07) | Tác nhân ACT-02 | PKG-12, PKG-14, PKG-15, PKG-16 (P09) |
| PKG-07 | DispatchWeb | PKG-01 | Hiển thị phần mềm huỷ chuyến và tiếp nhận thao tác của nhân viên điều hành | DC-CancelTripView, DC-CancelTripRequestHandler | Cùng tác nhân ACT-03; View trình bày danh sách chuyến và kết quả huỷ; RequestHandler và View trao đổi nhiều message | PKG-16; giữ chỗ P09: PKG-12, PKG-17 |
| PKG-08 | ManagementWeb | PKG-01 | Giữ chỗ: giao diện quản lý nhà xe (ACT-04) | Giữ chỗ (UC-002, UC-023, UC-024, UC-027, UC-028) | Tác nhân ACT-04 | PKG-12, PKG-17, PKG-19 (P09) |
| PKG-09 | BoardingApi | PKG-01 | Giữ chỗ: điểm vào HTTPS cho máy soát vé | Giữ chỗ (UC-025, UC-026) | Tác nhân ACT-05 | PKG-12, PKG-18 (P09) |
| PKG-10 | BoardingApp | PKG-01 | Giữ chỗ: màn hình soát vé trên máy cầm tay | Giữ chỗ (UC-026) | Tác nhân ACT-05 | PKG-18 (P09) |
| PKG-11 | TimerTrigger | PKG-01 | Phát các mốc thời gian sang Application | DC-HoldExpiryTrigger | Cùng tác nhân ACT-09; có lý do thay đổi riêng (cơ chế định thời tách khỏi nghiệp vụ, P09 F7), chỉ 1 phần tử vì mốc của UC-007, UC-025 chưa có lớp nguồn | PKG-13; giữ chỗ P09: PKG-14, PKG-18 |
| PKG-12 | Account | PKG-02 | Giữ chỗ: nhóm chức năng Tài khoản | Giữ chỗ (UC-001, UC-002, UC-003) | Nhóm chức năng Tài khoản | PKG-22, PKG-24, PKG-30 (P09); PKG-31 |
| PKG-13 | Booking | PKG-02 | Điều phối nhóm Đặt vé trực tuyến (tra cứu chuyến, đặt vé, thanh toán) | DC-BookTicketOnlineService, DC-SearchTripsService, DC-PayTicketOnlineService, DC-BookTicketOnlineViewModel | Cùng nhóm chức năng Đặt vé trực tuyến; UC-009 include UC-008 và UC-010 (R-02, R-03); view model đổi cùng service sinh ra nó. UC-010 là include bắt buộc của UC-009 nên không phải lớp tuỳ chọn | PKG-21, PKG-22, PKG-27, PKG-28, PKG-29, PKG-31 |
| PKG-14 | CounterSales | PKG-02 | Giữ chỗ: nhóm Bán vé tại quầy | Giữ chỗ (UC-004 đến UC-007) | Nhóm chức năng Bán vé tại quầy | PKG-13, PKG-23, PKG-27, PKG-28 (P09) |
| PKG-15 | TicketChange | PKG-02 | Giữ chỗ: nhóm Trả vé và đổi vé | Giữ chỗ (UC-012, UC-014, UC-015) | Nhóm chức năng Trả vé và đổi vé | PKG-13, PKG-21, PKG-22, PKG-23, PKG-27, PKG-28, PKG-29 (P09); PKG-31 |
| PKG-16 | TripManagement | PKG-02 | Điều phối nhóm Lịch chạy và chuyến (huỷ chuyến, hoàn tiền) | DC-CancelTripService, DC-CancelTripViewModel | Cùng nhóm chức năng Lịch chạy và chuyến; view model đổi cùng service sinh ra nó | PKG-21, PKG-22, PKG-27, PKG-28, PKG-29, PKG-31 |
| PKG-17 | ReferenceData | PKG-02 | Giữ chỗ: nhóm Danh mục và Giá vé | Giữ chỗ (UC-019 đến UC-024) | Nhóm chức năng Danh mục, Giá vé | PKG-27 (P09) |
| PKG-18 | Boarding | PKG-02 | Giữ chỗ: nhóm Soát vé | Giữ chỗ (UC-025, UC-026) | Nhóm chức năng Soát vé | PKG-25, PKG-26, PKG-27, PKG-28 (P09) |
| PKG-19 | Reporting | PKG-02 | Giữ chỗ: nhóm Báo cáo | Giữ chỗ (UC-027, UC-028) | Nhóm chức năng Báo cáo | PKG-27, PKG-28, PKG-29 (P09) |
| PKG-20 | Persistence | PKG-03 | Hiện thực interface kho dữ liệu của Domain trên cơ sở dữ liệu quan hệ | DC-RelationalTripRepository, DC-RelationalFareRepository, DC-RelationalSeatRepository, DC-RelationalBookingRepository, DC-RelationalTicketRepository, DC-RelationalPaymentTransactionRepository | Cùng cơ chế lưu trữ; thay đổi công nghệ lưu trữ chỉ đổi trong package này | PKG-27, PKG-28, PKG-29; giữ chỗ P09: PKG-30 |
| PKG-21 | PaymentIntegration | PKG-03 | Che Cổng thanh toán sau interface hoàn tiền (và thu tiền khi có P07 của UC-010) | SS-01, IF-01 | Tiêu chí hệ thống ngoài ACT-06; package subsystem và interface, đổi nhà cung cấp chỉ sửa tại đây | PKG-31 |
| PKG-22 | SmsIntegration | PKG-03 | Che Cổng SMS sau interface gửi tin nhắn | SS-02, IF-02 | Tiêu chí hệ thống ngoài ACT-07; package subsystem và interface | PKG-31 |
| PKG-23 | TicketPrinting | PKG-03 | Giữ chỗ: dữ liệu vé in cho máy in vé nhiệt | Giữ chỗ (UC-004, UC-006, UC-015) | Thiết bị ACT-08 | - (P09) |
| PKG-24 | Security | PKG-03 | Giữ chỗ: phiên làm việc và băm thông tin xác thực | Giữ chỗ (UC-003) | NFR-03 | PKG-30 (P09) |
| PKG-25 | LocalStore | PKG-03 | Giữ chỗ: kho cục bộ trên máy soát vé | Giữ chỗ (UC-026) | NFR-07 | - (P09) |
| PKG-26 | BoardingSyncClient | PKG-03 | Giữ chỗ: đồng bộ dữ liệu soát vé qua HTTPS | Giữ chỗ (UC-025, UC-026) | NFR-14 | - (P09) |
| PKG-27 | Operations | PKG-04 | Chứa khái niệm chuyến xe, giá vé và interface kho dữ liệu của chúng | DC-Trip, DC-Fare, IF-03, IF-04 | Cùng khái niệm vận hành: giá vé xác định theo tuyến xe và loại xe của chuyến (Fare dùng giá trị route, vehicleType của Trip); entity cùng interface kho dữ liệu của nó | PKG-31 |
| PKG-28 | Ticketing | PKG-04 | Chứa khái niệm chỗ, lần đặt vé, vé và interface kho dữ liệu của chúng | DC-Seat, DC-Booking, DC-Ticket, IF-05, IF-06, IF-07 | Có quan hệ với nhau (R-10, R-11, R-22) và cùng chịu ảnh hưởng của quy tắc BR-02 (không hai vé cùng chỗ); trạng thái chỗ, lần đặt, vé đổi cùng nhau | PKG-27, PKG-29, PKG-31 |
| PKG-29 | Payment | PKG-04 | Chứa khái niệm giao dịch thanh toán và interface kho dữ liệu của nó | DC-PaymentTransaction, IF-08 | Cùng khái niệm thanh toán và hoàn tiền (NFR-05, NFR-06) | PKG-31 |
| PKG-30 | Accounts | PKG-04 | Giữ chỗ: tài khoản, vai trò | Giữ chỗ (UC-001, UC-002, UC-003) | Khái niệm tài khoản | - (P09) |
| PKG-31 | ValueTypes | PKG-04 | Chứa kiểu giá trị (tiền, mã vé, mã giao dịch, số điện thoại) dùng trong chữ ký interface ở các layer trên | DC-Money, DC-TicketCode, DC-PaymentTransactionCode, DC-PhoneNumber | Kiểu giá trị cùng đổi theo quy tắc biểu diễn; đặt ở layer thấp nhất để chữ ký IF-01, IF-02 không kéo layer dưới phụ thuộc layer trên (A3). Không nhận lớp khác | - |

Lựa chọn khi tiêu chí mâu thuẫn: DC-HoldExpiryTrigger tách khỏi DC-BookTicketOnlineService dù cùng phục vụ UC-009, theo thứ tự ưu tiên quy tắc layer của P09 (PKG-11 ở Presentation, control ở Application) trước gắn kết chức năng.

## F5. Visibility

| PKG | Phần tử | Visibility (public / package-private) | Được dùng bởi (PKG) |
|---|---|---|---|
| PKG-05 | DC-BookTicketOnlineView | package-private | - (chỉ DC-BookTicketOnlineRequestHandler cùng package) |
| PKG-05 | DC-BookTicketOnlineRequestHandler | package-private | - (nền tảng web gọi vào, không package nào của mô hình dùng) |
| PKG-07 | DC-CancelTripView | package-private | - (chỉ DC-CancelTripRequestHandler cùng package) |
| PKG-07 | DC-CancelTripRequestHandler | package-private | - (nền tảng web gọi vào) |
| PKG-11 | DC-HoldExpiryTrigger | package-private | - (bộ định thời của nền tảng kích hoạt) |
| PKG-13 | DC-BookTicketOnlineService | public | PKG-05, PKG-11 |
| PKG-13 | DC-SearchTripsService | public | PKG-05 (UC-008); PKG-14, PKG-15 (dự kiến: UC-004, UC-005, UC-014, UC-015 include UC-008, P03 RL-42 đến RL-47) |
| PKG-13 | DC-PayTicketOnlineService | public | PKG-15 (dự kiến: UC-014 extend, P03 RL-48) |
| PKG-13 | DC-BookTicketOnlineViewModel | public | PKG-05 |
| PKG-16 | DC-CancelTripService | public | PKG-07 |
| PKG-16 | DC-CancelTripViewModel | public | PKG-07 |
| PKG-20 | DC-RelationalTripRepository, DC-RelationalFareRepository, DC-RelationalSeatRepository, DC-RelationalBookingRepository, DC-RelationalTicketRepository, DC-RelationalPaymentTransactionRepository | package-private | - (Application chỉ dùng interface ở Domain, P09 QT-5) |
| PKG-21 | SS-01 và mọi lớp bên trong | package-private | - (truy cập qua IF-01) |
| PKG-21 | IF-01 | public | PKG-13, PKG-16; PKG-15 (dự kiến, P09) |
| PKG-22 | SS-02 và mọi lớp bên trong | package-private | - (truy cập qua IF-02) |
| PKG-22 | IF-02 | public | PKG-13, PKG-16; PKG-12, PKG-15 (dự kiến, P09) |
| PKG-27 | DC-Trip | public | PKG-13, PKG-16, PKG-28, PKG-20 |
| PKG-27 | DC-Fare | public | PKG-13, PKG-20 |
| PKG-27 | IF-03 | public | PKG-13, PKG-16, PKG-20 |
| PKG-27 | IF-04 | public | PKG-13, PKG-20 |
| PKG-28 | DC-Seat | public | PKG-13, PKG-20 |
| PKG-28 | DC-Booking | public | PKG-13, PKG-20 |
| PKG-28 | DC-Ticket | public | PKG-13, PKG-16, PKG-20 |
| PKG-28 | IF-05 | public | PKG-13, PKG-20 |
| PKG-28 | IF-06 | public | PKG-13, PKG-20 |
| PKG-28 | IF-07 | public | PKG-13, PKG-16, PKG-20 |
| PKG-29 | DC-PaymentTransaction | public | PKG-13, PKG-16, PKG-28, PKG-20 |
| PKG-29 | IF-08 | public | PKG-13, PKG-16, PKG-20 |
| PKG-31 | DC-Money | public | PKG-13, PKG-16, PKG-21, PKG-27, PKG-28, PKG-29 |
| PKG-31 | DC-TicketCode | public | PKG-13, PKG-16, PKG-21, PKG-22, PKG-28 |
| PKG-31 | DC-PaymentTransactionCode | public | PKG-13, PKG-16, PKG-21, PKG-29 |
| PKG-31 | DC-PhoneNumber | public | PKG-13, PKG-16, PKG-22, PKG-28 |

## F6. Kiểm tra coupling giữa package

Bảng kiểm tra các phụ thuộc của package có phần tử và các phụ thuộc mới (tới PKG-31). Phụ thuộc giữa các package giữ chỗ không đổi so với P09 F6 (đã kiểm ở P09). P09 chọn layered nới lỏng nên cột Nhảy layer ghi "Không áp dụng".

| Phụ thuộc (PKG --> PKG) | Suy ra từ (quan hệ lớp, message) | Cross-coupled | Lower --> Upper | Nhảy layer | Vòng | Kết luận và cách sửa |
|---|---|---|---|---|---|---|
| PKG-05 PassengerWeb --> PKG-13 Booking | R-01 (BookTicketOnlineForm --> BookTicketOnlineController): DC-BookTicketOnlineRequestHandler gọi DC-BookTicketOnlineService, DC-SearchTripsService và nhận DC-BookTicketOnlineViewModel | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-07 DispatchWeb --> PKG-16 TripManagement | R-13 (CancelTripForm --> CancelTripController): DC-CancelTripRequestHandler gọi DC-CancelTripService và nhận DC-CancelTripViewModel | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-11 TimerTrigger --> PKG-13 Booking | P09 F5, F7: DC-HoldExpiryTrigger gọi DC-BookTicketOnlineService (handleHoldExpiry, after(BR-03)) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-13 Booking --> PKG-21 PaymentIntegration (IF-01) | Tạm: DC-PayTicketOnlineService (payTicketOnline, NFR-10) gọi IF-01; P09 F6 đã có dòng PKG-13 --> PKG-21; P08 chưa có quan hệ vì UC-010 chưa có P07 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-13 Booking --> PKG-22 SmsIntegration (IF-02) | R-09 (BookTicketOnlineController --> SmsGateway) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-13 Booking --> PKG-27 Operations | R-04 (--> Trip), R-06 (--> Fare) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-13 Booking --> PKG-28 Ticketing | R-05 (--> Seat), R-07 (--> Booking), R-08 (--> Ticket) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-13 Booking --> PKG-29 Payment | Tạm: DC-PayTicketOnlineService ghi nhận giao dịch thu tiền của UC-010; P09 F6 đã có dòng này; P08 chưa có quan hệ | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-13 Booking --> PKG-31 ValueTypes | Kiểu DC-Money, DC-TicketCode, DC-PhoneNumber trong lời gọi IF-01, IF-02 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 TripManagement --> PKG-21 PaymentIntegration (IF-01) | R-18 (CancelTripController --> PaymentGateway) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 TripManagement --> PKG-22 SmsIntegration (IF-02) | R-17 (CancelTripController --> SmsGateway) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 TripManagement --> PKG-27 Operations | R-14 (--> Trip) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 TripManagement --> PKG-28 Ticketing | R-15 (--> Ticket) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 TripManagement --> PKG-29 Payment | R-16 (--> PaymentTransaction) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 TripManagement --> PKG-31 ValueTypes | Kiểu DC-Money, DC-TicketCode, DC-PaymentTransactionCode, DC-PhoneNumber trong lời gọi IF-01, IF-02 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-20 Persistence --> PKG-27 Operations (realization IF-03, IF-04) | P09 QT-5: Persistence hiện thực interface kho dữ liệu của Trip, Fare; realization đi xuống | Không | Không | Không áp dụng | Không | Hợp lệ (realization đi xuống) |
| PKG-20 Persistence --> PKG-28 Ticketing (realization IF-05, IF-06, IF-07) | P09 QT-5: kho dữ liệu của Seat, Booking, Ticket | Không | Không | Không áp dụng | Không | Hợp lệ (realization đi xuống) |
| PKG-20 Persistence --> PKG-29 Payment (realization IF-08) | P09 QT-5: kho dữ liệu của PaymentTransaction | Không | Không | Không áp dụng | Không | Hợp lệ (realization đi xuống) |
| PKG-21 PaymentIntegration --> PKG-31 ValueTypes | Chữ ký IF-01 dùng Money, TicketCode, PaymentTransactionCode (A3, kiểu giá trị) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-22 SmsIntegration --> PKG-31 ValueTypes | Chữ ký IF-02 dùng PhoneNumber, TicketCode | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-27 Operations --> PKG-31 ValueTypes | Fare.amount (Số tiền) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-28 Ticketing --> PKG-27 Operations | R-12 (Booking --> Trip), R-19 (Ticket --> Trip), R-21 (Seat --> Trip); cùng layer, một chiều | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-28 Ticketing --> PKG-29 Payment | R-20 (Ticket --> PaymentTransaction); cùng layer, một chiều | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-28 Ticketing --> PKG-31 ValueTypes | Ticket.ticketCode, fare, travelerPhone; Booking.seatFare, travelerPhone | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-29 Payment --> PKG-31 ValueTypes | PaymentTransaction.transactionCode, collectedAmount, refundedAmount | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-12 Account --> PKG-31 ValueTypes (giữ chỗ) | Phụ thuộc PKG-12 --> PKG-22 của P09 (mã xác thực đăng nhập qua IF-02) kéo kiểu PhoneNumber; chưa có P07 của UC-003 | Không | Không | Không áp dụng | Không | Hợp lệ (giữ chỗ, kiểm lại khi có P07) |
| PKG-15 TicketChange --> PKG-31 ValueTypes (giữ chỗ) | Phụ thuộc PKG-15 --> PKG-21, PKG-22 của P09 kéo kiểu Money, TicketCode, PhoneNumber; chưa có P07 của UC-012, UC-014 | Không | Không | Không áp dụng | Không | Hợp lệ (giữ chỗ, kiểm lại khi có P07) |

Kiểm tra toàn đồ thị (27 package PKG-05 đến PKG-31, 67 phụ thuộc gồm 58 của P09 và 9 phụ thuộc tới PKG-31): không có hai package phụ thuộc lẫn nhau, không có vòng, không có phụ thuộc hoặc realization từ layer dưới lên trên, package Presentation chỉ phụ thuộc package Application (P09 QT-4), mọi phụ thuộc tới subsystem đi qua IF-01 hoặc IF-02. Không có dòng nào cần sửa.

## F7. Package diagram thiết kế

File diagrams/P10-package-design.drawio, một trang. Sơ đồ vẽ các package có phần tử cùng SS-01, SS-02, IF-01, IF-02; package giữ chỗ và phụ thuộc giữ chỗ không vẽ (xem P09-package-layers.drawio). Interface kho dữ liệu IF-03 đến IF-08 không vẽ riêng: PKG-20 hiện thực chúng, vẽ bằng realization từ PKG-20 tới package chứa interface, nhãn ghi mã IF. Không có lớp hiện thực interface gọi ngược nên không vẽ Class. Toạ độ x, y ở bảng Node là toạ độ tương đối theo phần tử chứa (theo draw.io).

a) Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú (visibility) | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-01 | Layer | Presentation (layer) | «layer» | - | Layer của P09 | 20 | 40 | 1240 | 150 |
| PKG-02 | Layer | Application (layer) | «layer» | - | Layer của P09 | 20 | 250 | 1240 | 150 |
| PKG-03 | Layer | Services (layer) | «layer» | - | Layer của P09 | 20 | 470 | 1240 | 230 |
| PKG-04 | Layer | Domain (layer) | «layer» | - | Layer của P09 | 20 | 770 | 1240 | 240 |
| PKG-05 | Package | PassengerWeb | - | PKG-01 | DC-BookTicketOnlineView, DC-BookTicketOnlineRequestHandler: package-private | 80 | 60 | 240 | 60 |
| PKG-11 | Package | TimerTrigger | - | PKG-01 | DC-HoldExpiryTrigger: package-private | 380 | 60 | 240 | 60 |
| PKG-07 | Package | DispatchWeb | - | PKG-01 | DC-CancelTripView, DC-CancelTripRequestHandler: package-private | 980 | 60 | 240 | 60 |
| PKG-13 | Package | Booking | - | PKG-02 | Bốn phần tử public | 80 | 60 | 680 | 60 |
| PKG-16 | Package | TripManagement | - | PKG-02 | Hai phần tử public | 820 | 60 | 400 | 60 |
| PKG-21 | Package | PaymentIntegration | - | PKG-03 | Chỉ IF-01 public | 60 | 50 | 300 | 140 |
| SS-01 | Subsystem | OnlinePayment | «subsystem» | PKG-21 | Không public; truy cập qua IF-01 | 20 | 50 | 160 | 60 |
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-21 | public | 240 | 70 | 20 | 20 |
| PKG-22 | Package | SmsIntegration | - | PKG-03 | Chỉ IF-02 public | 420 | 50 | 300 | 140 |
| SS-02 | Subsystem | SmsNotification | «subsystem» | PKG-22 | Không public; truy cập qua IF-02 | 20 | 50 | 160 | 60 |
| IF-02 | Interface | ISmsGateway | «interface» | PKG-22 | public | 240 | 70 | 20 | 20 |
| PKG-20 | Package | Persistence | - | PKG-03 | Sáu lớp hiện thực kho dữ liệu: package-private | 980 | 50 | 240 | 100 |
| PKG-31 | Package | ValueTypes | - | PKG-04 | Bốn kiểu giá trị: public | 80 | 60 | 220 | 100 |
| PKG-27 | Package | Operations | - | PKG-04 | Bốn phần tử public | 340 | 60 | 220 | 100 |
| PKG-28 | Package | Ticketing | - | PKG-04 | Sáu phần tử public | 620 | 60 | 220 | 100 |
| PKG-29 | Package | Payment | - | PKG-04 | Hai phần tử public | 900 | 60 | 220 | 100 |

b) Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ED-01 | PKG-05 | PKG-13 | Dependency | - | R-01 | - |
| ED-02 | PKG-07 | PKG-16 | Dependency | - | R-13 | - |
| ED-03 | PKG-11 | PKG-13 | Dependency | - | P09 F5: PKG-11 kích hoạt handleHoldExpiry | - |
| ED-04 | PKG-13 | IF-01 | Dependency | - | Tạm: DC-PayTicketOnlineService (P09 F6, NFR-10) | - |
| ED-05 | PKG-13 | IF-02 | Dependency | - | R-09 | - |
| ED-06 | PKG-13 | PKG-27 | Dependency | - | R-04, R-06 | - |
| ED-07 | PKG-13 | PKG-28 | Dependency | - | R-05, R-07, R-08 | - |
| ED-08 | PKG-13 | PKG-29 | Dependency | - | Tạm: P09 F6 | (760,420); (960,420) |
| ED-09 | PKG-13 | PKG-31 | Dependency | - | Kiểu giá trị trong chữ ký IF-01, IF-02 | (110,410); (60,410); (60,750); (130,750) |
| ED-10 | PKG-16 | IF-01 | Dependency | - | R-18 | (880,430); (370,430); (370,600) |
| ED-11 | PKG-16 | IF-02 | Dependency | - | R-17 | (900,440); (730,440); (730,600) |
| ED-12 | PKG-16 | PKG-27 | Dependency | - | R-14 | (920,730); (540,730) |
| ED-13 | PKG-16 | PKG-28 | Dependency | - | R-15 | - |
| ED-14 | PKG-16 | PKG-29 | Dependency | - | R-16 | - |
| ED-15 | PKG-16 | PKG-31 | Dependency | - | Kiểu giá trị trong chữ ký IF-01, IF-02 | (870,460); (40,460); (40,760); (170,760) |
| ED-16 | SS-01 | IF-01 | Realization | - | SS-01 hiện thực IF-01 | - |
| ED-17 | SS-02 | IF-02 | Realization | - | SS-02 hiện thực IF-02 | - |
| ED-18 | PKG-21 | PKG-31 | Dependency | - | Kiểu giá trị trong chữ ký IF-01 | - |
| ED-19 | PKG-22 | PKG-31 | Dependency | - | Kiểu giá trị trong chữ ký IF-02 | (560,740); (260,740) |
| ED-20 | PKG-20 | PKG-29 | Realization | IF-08 | Hiện thực IF-08 (kho dữ liệu) | - |
| ED-21 | PKG-20 | PKG-28 | Realization | IF-05, IF-06, IF-07 | Hiện thực kho dữ liệu của Seat, Booking, Ticket | (1020,720); (800,720) |
| ED-22 | PKG-20 | PKG-27 | Realization | IF-03, IF-04 | Hiện thực kho dữ liệu của Trip, Fare | (1040,710); (500,710) |
| ED-23 | PKG-28 | PKG-27 | Dependency | - | R-12, R-19, R-21 | - |
| ED-24 | PKG-28 | PKG-29 | Dependency | - | R-20 | - |
| ED-25 | PKG-27 | PKG-31 | Dependency | - | Kiểu giá trị: Fare.amount | (400,950); (300,950) |
| ED-26 | PKG-28 | PKG-31 | Dependency | - | Kiểu giá trị: Ticket.ticketCode, Ticket.fare, travelerPhone | (700,960); (250,960) |
| ED-27 | PKG-29 | PKG-31 | Dependency | - | Kiểu giá trị: PaymentTransaction.transactionCode, collectedAmount | (1000,970); (200,970) |

## F8. Subsystem context diagram

File diagrams/P10-subsystem-context.drawio, mỗi subsystem một trang (SS-01 OnlinePayment, SS-02 SmsNotification). Lớp DC-PayTicketOnlineService là control tạm của P08, quan hệ với IF-01 lấy từ P09 F6 (CE-02 của trang SS-01).

a) Bảng Node

| Trang | ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| SS-01 OnlinePayment | DC-CancelTripService | Class | DC-CancelTripService | - | - | Lớp thiết kế phụ thuộc vào IF-01 | 80 | 60 | 200 | 40 |
| SS-01 OnlinePayment | DC-PayTicketOnlineService | Class | DC-PayTicketOnlineService | - | - | Lớp thiết kế phụ thuộc vào IF-01 | 360 | 60 | 200 | 40 |
| SS-01 OnlinePayment | IF-01 | Interface | IPaymentGateway | «interface» | - | Interface canonical; trách nhiệm dạng // (operation do P11b) | 160 | 200 | 320 | 70 |
| SS-01 OnlinePayment | SS-01 | Subsystem | OnlinePayment | «subsystem» | - | Hiện thực IF-01 | 200 | 340 | 240 | 60 |
| SS-02 SmsNotification | DC-BookTicketOnlineService | Class | DC-BookTicketOnlineService | - | - | Lớp thiết kế phụ thuộc vào IF-02 | 80 | 60 | 200 | 40 |
| SS-02 SmsNotification | DC-CancelTripService | Class | DC-CancelTripService | - | - | Lớp thiết kế phụ thuộc vào IF-02 | 360 | 60 | 200 | 40 |
| SS-02 SmsNotification | IF-02 | Interface | ISmsGateway | «interface» | - | Interface canonical; trách nhiệm dạng // (operation do P11b) | 160 | 200 | 320 | 90 |
| SS-02 SmsNotification | SS-02 | Subsystem | SmsNotification | «subsystem» | - | Hiện thực IF-02 | 200 | 360 | 240 | 60 |

b) Bảng Edge

| Trang | ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|---|
| SS-01 OnlinePayment | CE-01 | DC-CancelTripService | IF-01 | Dependency | - | Lớp điều phối gọi interface | - |
| SS-01 OnlinePayment | CE-02 | DC-PayTicketOnlineService | IF-01 | Dependency | - | Tạm: chờ P07 của UC-010 (P09 F6, NFR-10) | - |
| SS-01 OnlinePayment | CE-03 | SS-01 | IF-01 | Realization | - | Subsystem hiện thực interface | - |
| SS-02 SmsNotification | CE-01 | DC-BookTicketOnlineService | IF-02 | Dependency | - | Lớp điều phối gọi interface | - |
| SS-02 SmsNotification | CE-02 | DC-CancelTripService | IF-02 | Dependency | - | Lớp điều phối gọi interface | - |
| SS-02 SmsNotification | CE-03 | SS-02 | IF-02 | Realization | - | Subsystem hiện thực interface | - |

## F9. Mục kiểm soát

Các mục Câu hỏi mở, Giả định, Đề xuất sửa artifact trước và Vấn đề còn mở theo C5 nằm ngay dưới đây.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | - | - | - |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | - |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P09 | F4 (PKG-12, PKG-13, PKG-15, PKG-16, PKG-21, PKG-22, PKG-27, PKG-28, PKG-29), F6, F9 | Chữ ký IF-01, IF-02 của subsystem ở Services dùng kiểu tiền, mã vé, mã giao dịch, số điện thoại, nhưng P09 không có package kiểu giá trị ở layer thấp nhất nên P10 cấp PKG-31 ValueTypes (Domain) | Khi chạy lại P09, thêm PKG-31 vào F4 và 9 phụ thuộc tới PKG-31 vào F6, F9; chưa sửa thì P10 là nguồn chuẩn cho PKG-31 |

## Vấn đề còn mở

- Độ phủ: P08 mới phủ UC-009, UC-017 nên 15 package của P09 là giữ chỗ (PKG-06, PKG-08, PKG-09, PKG-10, PKG-12, PKG-14, PKG-15, PKG-17, PKG-18, PKG-19, PKG-23, PKG-24, PKG-25, PKG-26, PKG-30). Chạy lại P10 khi P08, P09 đổi.
- Subsystem chưa tạo: máy in vé nhiệt (PKG-23, UC-004, UC-006, UC-015) và máy soát vé (PKG-09, PKG-25, PKG-26, UC-025, UC-026). Khi P07 của các use case này có, mỗi thiết bị thành subsystem và cần bảng Interface gọi ngược (sự kiện quét, danh sách hành khách); vì vậy P11b hiện chỉ có SS-01, SS-02 để thiết kế.
- Hai control tạm (AC-C-SearchTripsController, AC-C-PayTicketOnlineController, trạng thái "Tạm" ở P08 F3) vẫn được ánh xạ để UC-009 include UC-008, UC-010 có chỗ đặt; trách nhiệm của chúng sẽ đổi khi P07 của UC-008, UC-010 có. Phụ thuộc PKG-13 --> PKG-21, PKG-13 --> PKG-29 chỉ dựa trên P09 F6, chưa có quan hệ ở P08 F4.
- Target 1 và Target 3 đạt cho phạm vi hai use case. Mức hợp lý của F4: PKG-11 có 1 phần tử (có lý do thay đổi riêng), 15 package giữ chỗ chưa có phần tử.
- Tách entity Ticket: P08 F6 ghi bốn trách nhiệm tác động lên tập vé của chuyến lẫn với trách nhiệm một vé; P10 giữ DC-Ticket nguyên khối, P12 quyết định.
- Hai trách nhiệm cancelOverdueReservationMark, cancelPassengerListMark (ASM-28) của DC-CancelTripService và hai trách nhiệm chờ thanh toán của DC-BookTicketOnlineService phụ thuộc cơ chế đọc mốc từ dữ liệu bền của PKG-11 (P09 F7); P12 xác định chúng là thao tác hay hệ quả của trạng thái.
- Interface kho dữ liệu chia theo entity (6 interface, 6 lớp hiện thực); P12 có thể gộp theo cụm entity khi biết ranh giới giao dịch của Trip, Seat, Booking, Ticket.
- File diagrams/P10-package-design.drawio và diagrams/P10-subsystem-context.drawio sinh bằng chương trình từ cùng dữ liệu với F7, F8 và đã kiểm tự động (XML hợp lệ, toạ độ node là bội số của 10, điểm uốn là bội số của 10, khoảng cách giữa hai node cùng container tối thiểu 40, cạnh không cắt qua node). Chưa mở bằng draw.io để xem bằng mắt; định tuyến cạnh dài tới PKG-31 có thể cần chỉnh.
