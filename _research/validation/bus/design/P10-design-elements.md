# P10 - Phần tử thiết kế - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P10 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (mục 3 NEN_TANG, CONG_NGHE đã cập nhật theo khối F11 của P09, phương án CN1); 00-Conventions.md (bản hiện có); P01-actors.md 1.0; P02-usecases.md 1.1; P03-usecase-model.md 1.0; P06-supplementary-spec.md 1.0; P08-analysis-model.md 1.0; P09-architecture.md 1.0; P07-uc-analysis/*.md (không tra thêm: bằng chứng đã có trong P08). Tham số: TIEU_CHI_NHOM_PACKAGE = Không có; KHA_NANG_THAY_DOI_GIAO_DIEN = Không có (suy từ NFR và hồ sơ, không đủ căn cứ thì coi là dễ thay đổi); YEU_CAU_BO_SUNG = Không có |
| Phạm vi | Toàn hệ thống. Mô hình phân tích P08 mới phủ 4 trong 18 use case (UC-002, UC-008, UC-013, UC-015), nên phần tử thiết kế chỉ phủ 24 lớp phân tích của P08 cùng các phần tử cơ chế do P09 yêu cầu; các package của nhóm chưa phân tích được giữ chỗ |

Tóm tắt: 24 lớp phân tích của P08 được ánh xạ như sau: 3 boundary giao diện hệ thống và thiết bị thành subsystem (SS-01 đến SS-03), 7 lớp tách thành nhiều lớp (5 boundary người dùng, Trip, Ticket; tỷ lệ 29%), 14 lớp ánh xạ 1-1. Có thêm 5 subsystem do cơ chế kiến trúc (SS-04 đến SS-08), tổng 8 subsystem, 13 interface (IF-01 đến IF-13) và 39 lớp thiết kế (DC). Ba package mới (PKG-26 đến PKG-28) nối tiếp PKG-25 của P09: hai package con của PKG-06 để tách boundary theo tác nhân, một package kiểu giá trị dùng chung ở layer Domain. Bảng phụ thuộc có 40 dòng, không cross-coupled, không vòng, không phụ thuộc đi lên. Hồ sơ dự án đã chốt CN1 nên mẫu giao diện của P09 F3 (component kết hợp Flux cho web, MVVM cho Android) khớp công nghệ hiện tại.

## F1. Subsystem ứng viên và quyết định

Kiểm tra đầu vào (A0): hồ sơ ghi React, TypeScript, Redux Toolkit cho web và Kotlin, Android cho máy soát vé, khớp mẫu của P09 F3; không có "Chưa chốt" và không có mẫu lệch công nghệ.

| Lớp phân tích (AC) | Tiêu chí thoả | Quyết định | Lý do |
|---|---|---|---|
| AC-B-PaymentGateway | Hệ thống ngoài; Có thể thay thế | Subsystem | ACT-06; NFR-06, NFR-07; API chưa có tài liệu (Q-24), đổi API chỉ được sửa trong một package (P09 F1-06). Thành SS-01 |
| AC-B-SmsGateway | Hệ thống ngoài; Có thể thay thế | Subsystem | ACT-07; NFR-08; chỉ một trách nhiệm một chiều nhưng P09 F1-06 yêu cầu cô lập thay đổi cổng SMS và KHA_NANG_THAY_DOI_GIAO_DIEN mặc định coi là dễ thay đổi. Thành SS-02 |
| AC-B-BarcodeScanner | Thiết bị; Có thể thay thế | Subsystem | ACT-09; NFR-10; model đầu quét và loại mã vạch chưa biết (Q-54). Thành SS-03 |
| AC-B-BookTicketForm | - | Không | Boundary người dùng; 14 trách nhiệm đều là nhận nhập và hiển thị, không phải dịch vụ phức tạp. Tách vai trò theo mẫu giao diện ở F3 |
| AC-B-ReturnTicketForm | - | Không | Như trên; 11 trách nhiệm nhận nhập và hiển thị |
| AC-B-CounterReturnTicketForm | - | Không | Như trên |
| AC-B-CancelTripForm | - | Không | Như trên; 9 trách nhiệm |
| AC-B-CheckBoardingTicketForm | - | Không | Như trên; 7 trách nhiệm, chạy trên máy soát vé |
| AC-C-BookTicketOnlineController | - | Không | Độ dài điều phối không phải tiêu chí subsystem; control không che giấu thành phần nào |
| AC-C-PayTicketOnlineController | - | Không | Như trên; trạng thái tạm chờ P07 của UC-003 |
| AC-C-ReturnTicketController | - | Không | Như trên |
| AC-C-CancelTripController | - | Không | Như trên |
| AC-C-CheckBoardingTicketController | - | Không | Như trên |
| AC-E-Trip | - | Không | Entity miền; 11 trách nhiệm xử lý bằng tách lớp ở F3, không phải subsystem |
| AC-E-Route | - | Không | Entity miền, một trách nhiệm |
| AC-E-Seat | - | Không | Entity miền |
| AC-E-Booking | - | Không | Entity miền |
| AC-E-Ticket | - | Không | 17 trách nhiệm (P08 F6 không đạt) nhưng là khái niệm miền cần lộ rõ; xử lý bằng tách lớp ở F3 |
| AC-E-BaseFare | - | Không | Entity miền |
| AC-E-HolidaySurcharge | - | Không | Entity miền |
| AC-E-Refund | - | Không | Entity miền |
| AC-E-PhoneReservation | - | Không | Entity miền |
| AC-E-TicketCheckSession | - | Không | Entity miền |
| AC-E-TripPassengerList | - | Không | Entity miền |
| - (ACT-08, P09 PKG-17) | Thiết bị; Có thể thay thế | Subsystem | Máy in vé nhiệt không có lớp phân tích (UC-005 chưa có P07); NFR-09; model và kết nối chưa biết (Q-57, Q-79). Thành SS-04 |
| - (ACT-10, P09 PKG-19) | Dịch vụ phức tạp dùng chung; Có thể thay thế | Subsystem | Mốc hết hạn giữ chỗ (UC-002), huỷ mốc khi huỷ chuyến (UC-013), mốc của UC-006, UC-014; cần chống xử lý trùng giữa nhiều bản back-end (P09 F1-08). Thành SS-05 |
| - (P09 PKG-21 ServerApiClient) | Dịch vụ phức tạp dùng chung; Sản phẩm có sẵn | Subsystem | Máy soát vé gọi API máy chủ, giữ kết quả chờ gửi khi mất sóng (NFR-02). Thành SS-06 |
| - (P09 PKG-14 Persistence) | Sản phẩm có sẵn (hỗ trợ truy cập dữ liệu); Bảo mật | Subsystem | Ánh xạ đối tượng sang CSDL quan hệ, giao dịch và ràng buộc duy nhất chống trùng chỗ (REQ-67). Thành SS-07 |
| - (P09 PKG-20 DeviceStore) | Sản phẩm có sẵn (Room) | Subsystem | Lưu cục bộ trên máy soát vé. Thành SS-08 |

## F2. Bảng subsystem

| SS | Tên | Interface (IF) | Trách nhiệm | Che giấu phần tử nào | AC nguồn | ACT liên quan | PKG chứa |
|---|---|---|---|---|---|---|---|
| SS-01 | OnlinePayment | IF-01 IPaymentGateway | // requestRefund: gửi yêu cầu hoàn số tiền hoàn của vé tới cổng thanh toán<br>// returnRefundResult: nhận kết quả hoàn tiền từ cổng thanh toán<br>Trách nhiệm thu tiền thanh toán chờ P07 của UC-003 | Giao thức API của đối tác, xác thực, chuyển đổi dữ liệu thanh toán và hoàn tiền, hết thời gian chờ, lỗi, quản lý kết nối | AC-B-PaymentGateway | ACT-06 | PKG-15 |
| SS-02 | SmsDelivery | IF-03 ISmsSender | // sendSms: gửi nội dung tin nhắn (vé hoặc báo huỷ chuyến) tới số điện thoại người đi | Giao thức REST của cổng SMS, chuyển đổi nội dung, xử lý lỗi và hết thời gian chờ | AC-B-SmsGateway | ACT-07 | PKG-16 |
| SS-03 | BarcodeReading | IF-04 IBarcodeReader | // readBarcode: nhận mã vạch do đầu quét đọc từ vé và chuyển mã vé cho bộ nhận | SDK hoặc đầu vào bàn phím của đầu quét (Q-54), chuẩn hoá mã đọc được thành mã vé, đăng ký bộ nhận | AC-B-BarcodeScanner | ACT-09 | PKG-18 |
| SS-04 | TicketPrinting | IF-06 ITicketPrinter | // printTicket: gửi dữ liệu vé kèm mã vạch tới máy in vé nhiệt (NFR-09) | Định dạng lệnh in, giao tiếp với phần mềm trung gian ở máy trạm (Q-79), tạo mã vạch | Không có (ACT-08, P09 PKG-17) | ACT-08 | PKG-17 |
| SS-05 | TriggerScheduling | IF-07 ITriggerScheduler | // scheduleTrigger: đăng ký mốc kích hoạt tính từ dữ liệu (thời điểm giữ chỗ, giờ xuất bến)<br>// cancelTriggers: huỷ mốc kích hoạt của chuyến đã huỷ | Bộ định thời, duyệt dữ liệu tìm mốc đến hạn, chống xử lý trùng giữa nhiều bản back-end (P09 F1-08) | Không có (nguồn: AC-C-BookTicketOnlineController // startWaitingForPayment, // handleSeatHoldExpired; AC-C-CancelTripController // cancelTripTriggers) | ACT-10 | PKG-19 |
| SS-06 | ServerApiAccess | IF-09 IServerApiClient | // fetchPassengerList: nhận danh sách hành khách của chuyến từ máy chủ<br>// submitCheckResult: gửi kết quả soát vé của phiên về máy chủ, giữ lại khi mất sóng | HTTP client, xác thực, hàng đợi gửi lại, chuyển đổi dữ liệu truyền | Không có (NFR-02, P09 PKG-21; AC-E-TicketCheckSession // sendResult) | ACT-05 | PKG-21 |
| SS-07 | ServerPersistence | IF-10 ITripCatalogRepository<br>IF-11 ITicketingRepository<br>IF-12 IBoardingRepository<br>IF-13 IAccountRepository | // retrieve và // save các đối tượng miền của PKG-22 đến PKG-25 trong CSDL quan hệ; mỗi lần đặt, phát hành vé, trả vé, huỷ chuyến là một giao dịch; ràng buộc duy nhất cho chỗ của chuyến | Ánh xạ đối tượng-quan hệ, giao dịch, ràng buộc duy nhất, quản lý kết nối, câu lệnh truy vấn | Không có (P09 PKG-14, F7) | Không có | PKG-14 |
| SS-08 | DeviceLocalPersistence | IF-12 IBoardingRepository | // retrievePassengerList và // saveCheckSession cục bộ trên máy soát vé: danh sách hành khách, trạng thái phiên, kết quả chờ gửi | Room, DAO, ánh xạ đối tượng sang SQLite | Không có (P09 PKG-20, F7) | ACT-05 | PKG-20 |

Interface của subsystem và interface gọi ngược:

| IF | Tên | Loại | Định nghĩa tại PKG | Hiện thực bởi | Dùng bởi (PKG) | Trách nhiệm (// ...) | Nguồn |
|---|---|---|---|---|---|---|---|
| IF-01 | IPaymentGateway | Cung cấp bởi subsystem | PKG-15 | SS-01 | PKG-09, PKG-10 | // requestRefund, // returnRefundResult | P08 AC-B-PaymentGateway; R-09, R-14 |
| IF-02 | IPaymentResultListener | Gọi ngược | PKG-15 | DC-PayTicketOnlineService (PKG-09) | SS-01 | // receivePaymentResult: nhận kết quả thanh toán, mã tham chiếu giao dịch | P09 R5, F7 |
| IF-03 | ISmsSender | Cung cấp bởi subsystem | PKG-16 | SS-02 | PKG-09, PKG-10 | // sendSms | P08 AC-B-SmsGateway; R-02, R-15 |
| IF-04 | IBarcodeReader | Cung cấp bởi subsystem | PKG-18 | SS-03 | PKG-11 | // readBarcode | P08 AC-B-BarcodeScanner; R-17 |
| IF-05 | IBarcodeReadListener | Gọi ngược | PKG-18 | DC-CheckBoardingTicketService (PKG-11) | SS-03 | // receiveScannedCode: nhận mã vé vừa quét | P09 R5, F7 |
| IF-06 | ITicketPrinter | Cung cấp bởi subsystem | PKG-17 | SS-04 | PKG-09 | // printTicket | NFR-09; P09 F7 |
| IF-07 | ITriggerScheduler | Cung cấp bởi subsystem | PKG-19 | SS-05 | PKG-09, PKG-10 | // scheduleTrigger, // cancelTriggers | P08 // startWaitingForPayment, // cancelTripTriggers |
| IF-08 | ITriggerHandler | Gọi ngược | PKG-19 | DC-BookTicketOnlineService (PKG-09) | SS-05 | // handleTrigger: xử lý mốc đến hạn | P08 // handleSeatHoldExpired; P09 R5 |
| IF-09 | IServerApiClient | Cung cấp bởi subsystem | PKG-21 | SS-06 | PKG-11 | // fetchPassengerList, // submitCheckResult | NFR-02; P09 F7 |
| IF-10 | ITripCatalogRepository | Kho dữ liệu | PKG-22 | SS-07 | PKG-09, PKG-10, PKG-11 | // retrieveTripCatalog, // saveTripCatalog | P09 R6, F5 |
| IF-11 | ITicketingRepository | Kho dữ liệu | PKG-23 | SS-07 | PKG-09, PKG-10, PKG-11 | // retrieveTicketing, // saveTicketing | P09 R6, F5 |
| IF-12 | IBoardingRepository | Kho dữ liệu | PKG-24 | SS-07, SS-08 | PKG-11 | // retrievePassengerList, // saveCheckSession | P09 R6, F5 |
| IF-13 | IAccountRepository | Kho dữ liệu | PKG-25 | SS-07 | Chưa có (AccountService chưa có lớp) | // retrieveAccount, // saveAccount | P09 F7 |

## F3. Bảng ánh xạ lớp phân tích sang phần tử thiết kế

| AC | Kết quả | Phần tử thiết kế | PKG | Lý do |
|---|---|---|---|---|
| AC-B-BookTicketForm | Tách thành nhiều lớp | DC-BookTicketView<br>DC-BookTicketStore<br>DC-BookTicketRestController | PKG-05<br>PKG-05<br>PKG-08 | Bảng ánh xạ P09 F5 (web, component kết hợp Flux): View và Store ở Presentation, phần tiếp nhận yêu cầu là REST controller ở PKG-08. Các // show... thuộc View; // requestBooking, // selectTrip, // selectSeatsAndEnterTravelerInfo thuộc View và Store |
| AC-B-ReturnTicketForm | Tách thành nhiều lớp | DC-ReturnTicketView<br>DC-ReturnTicketStore<br>DC-ReturnTicketRestController | PKG-05<br>PKG-05<br>PKG-08 | Như trên; tác nhân ACT-01 vào PKG-05 |
| AC-B-CounterReturnTicketForm | Tách thành nhiều lớp | DC-CounterReturnTicketView<br>DC-CounterReturnTicketStore<br>DC-CounterReturnTicketRestController | PKG-26<br>PKG-26<br>PKG-08 | Như trên; tác nhân ACT-02 vào PKG-26 (con của PKG-06), tách khỏi boundary của ACT-03 (A3) |
| AC-B-CancelTripForm | Tách thành nhiều lớp | DC-CancelTripView<br>DC-CancelTripStore<br>DC-CancelTripRestController | PKG-27<br>PKG-27<br>PKG-08 | Như trên; tác nhân ACT-03 vào PKG-27 (con của PKG-06) |
| AC-B-CheckBoardingTicketForm | Tách thành nhiều lớp | DC-CheckBoardingTicketView<br>DC-CheckBoardingTicketViewModel | PKG-07<br>PKG-07 | P09 F5 (Android, MVVM): View và ViewModel; không có REST controller vì logic soát vé chạy trên máy qua DC-CheckBoardingTicketService |
| AC-B-BarcodeScanner | Subsystem | SS-03 BarcodeReading | PKG-18 | F1: thiết bị, có thể thay thế |
| AC-B-SmsGateway | Subsystem | SS-02 SmsDelivery | PKG-16 | F1: hệ thống ngoài, có thể thay thế |
| AC-B-PaymentGateway | Subsystem | SS-01 OnlinePayment | PKG-15 | F1: hệ thống ngoài, có thể thay thế |
| AC-C-BookTicketOnlineController | Lớp thiết kế DC | DC-BookTicketOnlineService | PKG-09 | Ánh xạ 1-1 (P09 F5: lớp dịch vụ ứng dụng). Đổi tên: hậu tố Controller đụng REST controller (DC-...RestController) và controller của mẫu MVC trong P09 F5 |
| AC-C-PayTicketOnlineController | Lớp thiết kế DC | DC-PayTicketOnlineService | PKG-09 | Ánh xạ 1-1, trạng thái tạm chờ P07 của UC-003. Đổi tên như trên. Hiện thực IF-02 |
| AC-C-ReturnTicketController | Lớp thiết kế DC | DC-ReturnTicketService | PKG-09 | Ánh xạ 1-1. Đổi tên như trên |
| AC-C-CancelTripController | Lớp thiết kế DC | DC-CancelTripService | PKG-10 | Ánh xạ 1-1. Đổi tên như trên |
| AC-C-CheckBoardingTicketController | Lớp thiết kế DC | DC-CheckBoardingTicketService | PKG-11 | Ánh xạ 1-1. Đổi tên như trên. Nhận mã vé qua IF-05; việc gửi kết quả soát về máy chủ qua IF-09 do lớp này làm (xem AC-E-TicketCheckSession) |
| AC-E-Trip | Tách thành nhiều lớp | DC-Trip<br>DC-TripCancellation | PKG-22<br>PKG-23 | Hai trách nhiệm // getCancellationSummary và // cancelTrip phải truy vấn và yêu cầu Ticket, PhoneReservation (PKG-23) huỷ cùng chuyến; để trong Trip thì PKG-22 phụ thuộc PKG-23 và PKG-23 phụ thuộc PKG-22 (cross-coupled). Tách phần phối hợp sang DC-TripCancellation ở PKG-23 (chuyển lớp, A5). DC-Trip giữ các // findMatchingTrips, // getSeatMap, // checkSeatsAvailable, // determineTicketPrice, // getRouteAndDepartureTime, // calculateTimeToDeparture, // findTrip, // checkNotCancelled, // checkBeforeDeparture và việc đổi trạng thái chuyến sang đã huỷ |
| AC-E-Route | Lớp thiết kế DC | DC-Route | PKG-22 | Lớp đơn giản, một trừu tượng |
| AC-E-Seat | Lớp thiết kế DC | DC-Seat | PKG-22 | Lớp đơn giản, một trừu tượng |
| AC-E-Booking | Lớp thiết kế DC | DC-Booking | PKG-23 | Lớp đơn giản, một trừu tượng |
| AC-E-Ticket | Tách thành nhiều lớp | DC-Ticket<br>DC-TicketReturnPolicy<br>DC-TicketSmsContent | PKG-23<br>PKG-23<br>PKG-23 | P08 F6 ghi trách nhiệm không gắn kết (17 trách nhiệm) và P09 F5 giao P10 cân nhắc tách. DC-Ticket: // createTicket, // findTicket, // checkNotCancelled, // cancelTicket, // cancelWithTrip, // recordRefund, // determineCheckResult, // markChecked. DC-TicketReturnPolicy (quy tắc trả vé và hoàn tiền BR-11 đến BR-17): // checkPurchaseChannel, // checkReturnTimeLimit, // calculateRefundAmount, // getTicketReturnInfo, // determineRefundMethod, // getCancelImpactInfo, // calculateTripCancelRefundAmount. DC-TicketSmsContent: // getTicketSmsContent, // getTripCancelSmsContent |
| AC-E-BaseFare | Lớp thiết kế DC | DC-BaseFare | PKG-22 | Lớp đơn giản, một trừu tượng |
| AC-E-HolidaySurcharge | Lớp thiết kế DC | DC-HolidaySurcharge | PKG-22 | Lớp đơn giản, một trừu tượng |
| AC-E-Refund | Lớp thiết kế DC | DC-Refund | PKG-23 | Lớp đơn giản, một trừu tượng |
| AC-E-PhoneReservation | Lớp thiết kế DC | DC-PhoneReservation | PKG-23 | Lớp đơn giản, một trừu tượng |
| AC-E-TripPassengerList | Lớp thiết kế DC | DC-TripPassengerList | PKG-24 | Lớp đơn giản, một trừu tượng |
| AC-E-TicketCheckSession | Lớp thiết kế DC | DC-TicketCheckSession | PKG-24 | Lớp đơn giản, một trừu tượng. Trách nhiệm // sendResult: phần gửi qua mạng do DC-CheckBoardingTicketService thực hiện qua IF-09 vì Domain không gọi được layer Services; DC-TicketCheckSession giữ // startSession, // markResultSent, // keepResultPending |

Tỷ lệ tách: 7 trên 24 lớp (29%), dưới ngưỡng một nửa. 3 lớp thành subsystem, 14 lớp ánh xạ 1-1.

Phần tử thiết kế mới do cơ chế kiến trúc (không từ lớp phân tích):

| DC hoặc SS | Tên | PKG | Cơ chế | Nguồn nhóm |
|---|---|---|---|---|
| DC-BoardingSyncRestController | BoardingSyncRestController | PKG-08 | Giao tiếp máy soát vé với máy chủ (nhận kết quả soát, cấp danh sách hành khách) | P09 F4 (PKG-08 phụ thuộc PKG-11), F7; NFR-02; AC-C-CheckBoardingTicketController // endCheck |
| SS-04 | TicketPrinting | PKG-17 | Giao tiếp thiết bị | P09 F5, F7; NFR-09; ACT-08 |
| SS-05 | TriggerScheduling | PKG-19 | Định thời tự động | P09 F1-08, F7; ACT-10 |
| SS-06 | ServerApiAccess | PKG-21 | Đồng bộ khi mất sóng | P09 F7; NFR-02 |
| SS-07 | ServerPersistence | PKG-14 | Persistence quan hệ | P09 F5 dòng cuối, F7; REQ-67 |
| SS-08 | DeviceLocalPersistence | PKG-20 | Persistence cục bộ | P09 F5 dòng cuối, F7; NFR-02 |
| IF-02, IF-05, IF-08 | IPaymentResultListener, IBarcodeReadListener, ITriggerHandler | PKG-15, PKG-18, PKG-19 | Gọi ngược lên layer trên | P09 R5, F7 |
| IF-10 đến IF-13 | Interface kho dữ liệu | PKG-22 đến PKG-25 | Persistence | P09 R6, F5 dòng cuối |
| DC-Money | Money | PKG-28 | Kiểu giá trị cho các thuộc tính "Số tiền" trong chữ ký IF-01, IF-02 | A3; P08 totalAmount, price, refundAmount, amount |
| DC-TicketCode | TicketCode | PKG-28 | Kiểu giá trị mã vé trong chữ ký IF-01, IF-05 | A3; P08 ticketCode |
| DC-PhoneNumber | PhoneNumber | PKG-28 | Kiểu giá trị số điện thoại trong chữ ký IF-03 | A3; P08 travelerPhone, recipientPhone |
| DC-PaymentReference | PaymentReference | PKG-28 | Kiểu giá trị mã tham chiếu giao dịch trong chữ ký IF-02 | A3; P09 F7 ("mã tham chiếu giao dịch của cổng được lưu") |
| DC-TriggerReference | TriggerReference | PKG-19 | Kiểu giá trị tham chiếu mốc trong chữ ký IF-07, IF-08 | A3; P09 F7 |

## F4. Bảng package

PKG-01 đến PKG-04 là layer của P09 (không liệt kê lại). Phụ thuộc ghi ở mức package; PKG-12, PKG-13 chưa có phần tử nên không có phụ thuộc vẽ ở F7.

| PKG | Tên | Layer (PKG) | Trách nhiệm | Phần tử chứa (DC, SS, IF) | Tiêu chí nhóm | Phụ thuộc vào (PKG) |
|---|---|---|---|---|---|---|
| PKG-05 | PassengerWeb | PKG-01 | Hiển thị website hành khách, tiếp nhận thao tác | DC-BookTicketView, DC-BookTicketStore, DC-ReturnTicketView, DC-ReturnTicketStore | Cùng tác nhân ACT-01; View trình bày Booking, Ticket; Store thay đổi cùng View | PKG-08 |
| PKG-06 | StaffWeb | PKG-01 | Package cha của giao diện web nhân viên; không chứa phần tử trực tiếp | PKG-26, PKG-27 | Tách theo tác nhân: hai boundary người dùng của hai tác nhân không được cùng package (A3) | PKG-08 (qua PKG-26, PKG-27) |
| PKG-26 | TicketClerkWeb | PKG-01 (con của PKG-06) | Giao diện web của nhân viên bán vé | DC-CounterReturnTicketView, DC-CounterReturnTicketStore | Cùng tác nhân ACT-02; View trình bày Ticket tại quầy | PKG-08 |
| PKG-27 | DispatcherWeb | PKG-01 (con của PKG-06) | Giao diện web của nhân viên điều hành | DC-CancelTripView, DC-CancelTripStore | Cùng tác nhân ACT-03; View trình bày Trip | PKG-08 |
| PKG-07 | CheckerAppUI | PKG-01 | Màn hình soát vé trên máy soát vé | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel | Cùng tác nhân ACT-05; ViewModel và View thay đổi cùng nhau | PKG-11 |
| PKG-08 | RestApi | PKG-02 | Tiếp nhận yêu cầu của client qua REST, chuyển cho dịch vụ ứng dụng | DC-BookTicketRestController, DC-ReturnTicketRestController, DC-CounterReturnTicketRestController, DC-CancelTripRestController, DC-BoardingSyncRestController | Cùng vai trò tiếp nhận yêu cầu (CCP: đổi giao thức API thì đổi cùng lúc); REST controller là thành phần Application, không phải boundary người dùng (P09 F5) nên không vi phạm quy tắc tác nhân | PKG-09, PKG-10, PKG-11 |
| PKG-09 | TicketSalesService | PKG-02 | Điều phối use case bán vé | DC-BookTicketOnlineService, DC-PayTicketOnlineService, DC-ReturnTicketService | Nhóm chức năng Bán vé (UC-002, UC-003, UC-008); trao đổi nhiều message với Booking, Ticket | PKG-15, PKG-16, PKG-17, PKG-19, PKG-22, PKG-23 |
| PKG-10 | TripOperationsService | PKG-02 | Điều phối use case vận hành chuyến | DC-CancelTripService | Nhóm chức năng Vận hành chuyến. Một phần tử: package có lý do thay đổi riêng (nhóm UC-012 đến UC-014), sẽ nhận control của UC-012, UC-014 khi có P07 | PKG-15, PKG-16, PKG-19, PKG-22, PKG-23, PKG-24 |
| PKG-11 | BoardingCheckService | PKG-02 | Điều phối soát vé, chạy trên máy soát vé và ở back-end | DC-CheckBoardingTicketService | UC-015 chạy được khi mất mạng. Một phần tử: package có lý do thay đổi riêng và được triển khai cả trên máy soát vé (P09 F4) | PKG-18, PKG-21, PKG-22, PKG-23, PKG-24 |
| PKG-12 | AccountService | PKG-02 | Điều phối đăng ký, đăng nhập, lịch sử vé | Chưa có (UC-009 đến UC-011 chưa có P07) | Nhóm Tài khoản hành khách; giữ chỗ theo P09 | Giữ như P09: PKG-23, PKG-25 (không vẽ ở F7) |
| PKG-13 | PricingReportService | PKG-02 | Điều phối giá vé, tăng giá lễ Tết, báo cáo | Chưa có (UC-016 đến UC-018 chưa có P07) | Nhóm Giá vé và báo cáo; giữ chỗ theo P09 | Giữ như P09: PKG-22, PKG-23 (không vẽ ở F7) |
| PKG-14 | Persistence | PKG-03 | Lưu, truy xuất đối tượng miền ở máy chủ | SS-07 | Package subsystem; sản phẩm có sẵn (hỗ trợ truy cập dữ liệu) | PKG-22, PKG-23, PKG-24, PKG-25 |
| PKG-15 | PaymentIntegration | PKG-03 | Che cổng thanh toán | SS-01, IF-01, IF-02 | Package subsystem và interface của ACT-06 | PKG-28 |
| PKG-16 | SmsIntegration | PKG-03 | Che cổng SMS | SS-02, IF-03 | Package subsystem và interface của ACT-07 | PKG-28 |
| PKG-17 | PrinterIntegration | PKG-03 | Che máy in vé | SS-04, IF-06 | Package subsystem và interface của ACT-08 | PKG-23 |
| PKG-18 | ScannerIntegration | PKG-03 | Che đầu quét mã vạch | SS-03, IF-04, IF-05 | Package subsystem và interface của ACT-09 | PKG-28 |
| PKG-19 | Scheduling | PKG-03 | Kích hoạt xử lý theo mốc thời gian | SS-05, IF-07, IF-08, DC-TriggerReference | Package subsystem và interface của ACT-10 | Không có |
| PKG-20 | DeviceStore | PKG-03 | Lưu cục bộ trên máy soát vé | SS-08 | Package subsystem; tách khỏi PKG-14 vì chạy trên thiết bị khác | PKG-24 |
| PKG-21 | ServerApiClient | PKG-03 | Gọi API máy chủ từ máy soát vé | SS-06, IF-09 | Package subsystem và interface | PKG-24 |
| PKG-22 | TripCatalog | PKG-04 | Khái niệm tuyến, chuyến, chỗ, giá | DC-Trip, DC-Route, DC-Seat, DC-BaseFare, DC-HolidaySurcharge, IF-10 | Lớp có quan hệ với nhau (R-22 đến R-25); Trip tạo và giữ Seat | PKG-28 |
| PKG-23 | Ticketing | PKG-04 | Khái niệm lần đặt, vé, đặt chỗ qua điện thoại, hoàn tiền | DC-Booking, DC-Ticket, DC-TicketReturnPolicy, DC-TicketSmsContent, DC-TripCancellation, DC-Refund, DC-PhoneReservation, IF-11 | Quan hệ R-28, R-32; Booking tạo Ticket; DC-TripCancellation phối hợp Trip với Ticket, PhoneReservation | PKG-22, PKG-28 |
| PKG-24 | BoardingModel | PKG-04 | Khái niệm danh sách hành khách của chuyến, phiên soát vé | DC-TripPassengerList, DC-TicketCheckSession, IF-12 | Cùng phục vụ UC-015; R-35, R-36 | PKG-22, PKG-23, PKG-28 |
| PKG-25 | AccountModel | PKG-04 | Khái niệm tài khoản hành khách | IF-13 | Một phần tử: package interface, chờ P07 của UC-009 đến UC-011 | Không có |
| PKG-28 | SharedValueTypes | PKG-04 | Kiểu giá trị dùng trong chữ ký interface của layer Services | DC-Money, DC-TicketCode, DC-PhoneNumber, DC-PaymentReference | Cùng loại (kiểu giá trị bất biến), ở layer thấp nhất để interface Services không phụ thuộc lên; không chứa lớp nghiệp vụ | Không có |

## F5. Visibility

Persistence (SS-07) ánh xạ mọi lớp miền của PKG-22 đến PKG-25 nên các lớp miền đều public. Lớp nội bộ của subsystem (che giấu ở F2) không public và chưa được đặt tên cuối cùng.

| PKG | Phần tử | Visibility | Được dùng bởi (PKG) |
|---|---|---|---|
| PKG-05 | DC-BookTicketView, DC-BookTicketStore, DC-ReturnTicketView, DC-ReturnTicketStore | package-private | Không có (dùng trong PKG-05) |
| PKG-26 | DC-CounterReturnTicketView, DC-CounterReturnTicketStore | package-private | Không có (dùng trong PKG-26) |
| PKG-27 | DC-CancelTripView, DC-CancelTripStore | package-private | Không có (dùng trong PKG-27) |
| PKG-07 | DC-CheckBoardingTicketView, DC-CheckBoardingTicketViewModel | package-private | Không có (dùng trong PKG-07) |
| PKG-08 | DC-BookTicketRestController, DC-ReturnTicketRestController | public | PKG-05 (qua REST) |
| PKG-08 | DC-CounterReturnTicketRestController | public | PKG-26 (qua REST) |
| PKG-08 | DC-CancelTripRestController | public | PKG-27 (qua REST) |
| PKG-08 | DC-BoardingSyncRestController | public | PKG-21 (qua REST) |
| PKG-09 | DC-BookTicketOnlineService, DC-ReturnTicketService | public | PKG-08 |
| PKG-09 | DC-PayTicketOnlineService | package-private | Không có (dùng trong PKG-09, và gọi ngược qua IF-02) |
| PKG-10 | DC-CancelTripService | public | PKG-08 |
| PKG-11 | DC-CheckBoardingTicketService | public | PKG-07, PKG-08 |
| PKG-14 | SS-07 | package-private (chỉ IF-10 đến IF-13 public) | Không có (dùng qua interface) |
| PKG-15 | SS-01 | package-private (chỉ IF-01 public) | Không có (dùng qua interface) |
| PKG-15 | IF-01 | public | PKG-09, PKG-10 |
| PKG-15 | IF-02 | public | PKG-09 |
| PKG-16 | SS-02 | package-private | Không có (dùng qua IF-03) |
| PKG-16 | IF-03 | public | PKG-09, PKG-10 |
| PKG-17 | SS-04 | package-private | Không có (dùng qua IF-06) |
| PKG-17 | IF-06 | public | PKG-09 |
| PKG-18 | SS-03 | package-private | Không có (dùng qua IF-04) |
| PKG-18 | IF-04 | public | PKG-11 |
| PKG-18 | IF-05 | public | PKG-11 |
| PKG-19 | SS-05 | package-private | Không có (dùng qua IF-07) |
| PKG-19 | IF-07 | public | PKG-09, PKG-10 |
| PKG-19 | IF-08 | public | PKG-09 |
| PKG-19 | DC-TriggerReference | public | PKG-09, PKG-10 |
| PKG-20 | SS-08 | package-private | Không có (dùng qua IF-12) |
| PKG-21 | SS-06 | package-private | Không có (dùng qua IF-09) |
| PKG-21 | IF-09 | public | PKG-11 |
| PKG-22 | DC-Trip | public | PKG-09, PKG-10, PKG-11, PKG-14, PKG-23, PKG-24 |
| PKG-22 | DC-Seat | public | PKG-14, PKG-23 |
| PKG-22 | DC-Route, DC-BaseFare, DC-HolidaySurcharge | public | PKG-14 |
| PKG-22 | IF-10 | public | PKG-09, PKG-10, PKG-11, PKG-14 |
| PKG-23 | DC-Booking | public | PKG-09, PKG-14 |
| PKG-23 | DC-Refund, DC-PhoneReservation | public | PKG-14 |
| PKG-23 | DC-Ticket | public | PKG-09, PKG-10, PKG-11, PKG-14, PKG-17, PKG-24 |
| PKG-23 | DC-TicketReturnPolicy, DC-TicketSmsContent | public | PKG-09, PKG-10 |
| PKG-23 | DC-TripCancellation | public | PKG-10 |
| PKG-23 | IF-11 | public | PKG-09, PKG-10, PKG-11, PKG-14 |
| PKG-24 | DC-TripPassengerList, DC-TicketCheckSession | public | PKG-11, PKG-14, PKG-21 |
| PKG-24 | IF-12 | public | PKG-11, PKG-14, PKG-20 |
| PKG-25 | IF-13 | public | PKG-14 |
| PKG-28 | DC-Money | public | PKG-15, PKG-22, PKG-23 |
| PKG-28 | DC-TicketCode | public | PKG-15, PKG-18, PKG-23, PKG-24 |
| PKG-28 | DC-PhoneNumber | public | PKG-16, PKG-23 |
| PKG-28 | DC-PaymentReference | public | PKG-15 |

## F6. Kiểm tra coupling giữa package

Layered nới lỏng (P09 R1): nhảy layer được phép. Phụ thuộc Application --> Domain bỏ qua layer Services là hợp lệ theo R1 và được đánh dấu "Có" ở cột Nhảy layer, kèm kết luận.

| Phụ thuộc (PKG --> PKG) | Suy ra từ (quan hệ lớp, message) | Cross-coupled | Lower --> Upper | Nhảy layer | Vòng | Kết luận và cách sửa |
|---|---|---|---|---|---|---|
| PKG-05 --> PKG-08 | Store gọi REST của DC-BookTicketRestController, DC-ReturnTicketRestController (P09 E-01) | Không | Không | Không | Không | Hợp lệ |
| PKG-26 --> PKG-08 | DC-CounterReturnTicketStore gọi DC-CounterReturnTicketRestController | Không | Không | Không | Không | Hợp lệ; thay P09 E-02 |
| PKG-27 --> PKG-08 | DC-CancelTripStore gọi DC-CancelTripRestController | Không | Không | Không | Không | Hợp lệ; thay P09 E-02 |
| PKG-07 --> PKG-11 | R-16: ViewModel gọi DC-CheckBoardingTicketService | Không | Không | Không | Không | Hợp lệ (P09 R4) |
| PKG-08 --> PKG-09 | R-01, R-07, R-08: REST controller gọi DC-BookTicketOnlineService, DC-ReturnTicketService | Không | Không | Không | Không | Hợp lệ, cùng layer một chiều |
| PKG-08 --> PKG-10 | R-11: DC-CancelTripRestController gọi DC-CancelTripService | Không | Không | Không | Không | Hợp lệ |
| PKG-08 --> PKG-11 | DC-BoardingSyncRestController gọi DC-CheckBoardingTicketService (P09 E-06) | Không | Không | Không | Không | Hợp lệ |
| PKG-09 --> PKG-15 | R-09: hoàn tiền qua IF-01; DC-PayTicketOnlineService hiện thực IF-02 (R-03) | Không | Không | Không | Không | Hợp lệ; realization đi xuống |
| PKG-09 --> PKG-16 | R-02: gửi vé qua IF-03 | Không | Không | Không | Không | Hợp lệ |
| PKG-09 --> PKG-17 | P09 E-11; chưa có lớp P08 (UC-005) | Không | Không | Không | Không | Hợp lệ; chờ P07 của UC-005 |
| PKG-09 --> PKG-19 | // startWaitingForPayment, // handleSeatHoldExpired; DC-BookTicketOnlineService hiện thực IF-08 | Không | Không | Không | Không | Hợp lệ; realization đi xuống |
| PKG-09 --> PKG-22 | R-04: dùng Trip; Booking giữ Seat | Không | Không | Có (R1) | Không | Hợp lệ theo P09 R1, không cần sửa |
| PKG-09 --> PKG-23 | R-05, R-06, R-10: dùng Booking, Ticket | Không | Không | Có (R1) | Không | Hợp lệ theo P09 R1, không cần sửa |
| PKG-10 --> PKG-15 | R-14: hoàn tiền qua IF-01 | Không | Không | Không | Không | Hợp lệ |
| PKG-10 --> PKG-16 | R-15: báo huỷ chuyến qua IF-03 | Không | Không | Không | Không | Hợp lệ |
| PKG-10 --> PKG-19 | // cancelTripTriggers qua IF-07 | Không | Không | Không | Không | Hợp lệ |
| PKG-10 --> PKG-22 | R-12: dùng Trip | Không | Không | Có (R1) | Không | Hợp lệ theo P09 R1, không cần sửa |
| PKG-10 --> PKG-23 | R-13: dùng Ticket; gọi DC-TripCancellation | Không | Không | Có (R1) | Không | Hợp lệ theo P09 R1, không cần sửa |
| PKG-10 --> PKG-24 | P09 E-20; chưa có lớp P08 (UC-014) | Không | Không | Có (R1) | Không | Hợp lệ; chờ P07 của UC-014 |
| PKG-11 --> PKG-18 | R-17: đăng ký bộ nhận qua IF-04; hiện thực IF-05 | Không | Không | Không | Không | Hợp lệ; realization đi xuống |
| PKG-11 --> PKG-21 | NFR-02: nhận danh sách, gửi kết quả qua IF-09 (P09 E-22) | Không | Không | Không | Không | Hợp lệ |
| PKG-11 --> PKG-22 | R-19: dùng Trip | Không | Không | Có (R1) | Không | Hợp lệ theo P09 R1, không cần sửa |
| PKG-11 --> PKG-23 | R-21: dùng Ticket | Không | Không | Có (R1) | Không | Hợp lệ theo P09 R1, không cần sửa |
| PKG-11 --> PKG-24 | R-18, R-20: dùng TicketCheckSession, TripPassengerList | Không | Không | Có (R1) | Không | Hợp lệ theo P09 R1, không cần sửa |
| PKG-14 --> PKG-22 | SS-07 hiện thực IF-10 | Không | Không | Không | Không | Hợp lệ; realization đi xuống |
| PKG-14 --> PKG-23 | SS-07 hiện thực IF-11 | Không | Không | Không | Không | Hợp lệ |
| PKG-14 --> PKG-24 | SS-07 hiện thực IF-12 | Không | Không | Không | Không | Hợp lệ |
| PKG-14 --> PKG-25 | SS-07 hiện thực IF-13 | Không | Không | Không | Không | Hợp lệ |
| PKG-20 --> PKG-24 | SS-08 hiện thực IF-12 (P09 E-34) | Không | Không | Không | Không | Hợp lệ |
| PKG-15 --> PKG-28 | Chữ ký IF-01, IF-02 dùng DC-Money, DC-TicketCode, DC-PaymentReference | Không | Không | Không | Không | Hợp lệ; kiểu giá trị ở layer thấp nhất (A3) |
| PKG-16 --> PKG-28 | Chữ ký IF-03 dùng DC-PhoneNumber | Không | Không | Không | Không | Hợp lệ |
| PKG-18 --> PKG-28 | Chữ ký IF-05 dùng DC-TicketCode | Không | Không | Không | Không | Hợp lệ |
| PKG-17 --> PKG-23 | Dữ liệu vé cần in (DC-Ticket) | Không | Không | Không | Không | Hợp lệ |
| PKG-21 --> PKG-24 | Chữ ký IF-09 dùng DC-TripPassengerList, DC-TicketCheckSession | Không | Không | Không | Không | Hợp lệ |
| PKG-22 --> PKG-28 | BaseFare.amount là Số tiền | Không | Không | Không | Không | Hợp lệ |
| PKG-23 --> PKG-28 | Ticket.price, Ticket.ticketCode, travelerPhone | Không | Không | Không | Không | Hợp lệ |
| PKG-24 --> PKG-28 | TripPassengerList tìm vé theo mã vé | Không | Không | Không | Không | Hợp lệ |
| PKG-23 --> PKG-22 | R-26, R-27, R-29, R-30, R-37; R-33 điều hướng từ PhoneReservation sang Trip | Không | Không | Không | Không | Hợp lệ; hướng một chiều (P09 R8) |
| PKG-24 --> PKG-23 | R-35 | Không | Không | Không | Không | Hợp lệ |
| PKG-24 --> PKG-22 | R-34 điều hướng từ TripPassengerList sang Trip; R-36 | Không | Không | Không | Không | Hợp lệ |

Dòng "Có" duy nhất là Nhảy layer của 8 phụ thuộc Application --> Domain; P09 chọn layered nới lỏng (R1) nên đây không phải vi phạm, ghi tại Vấn đề còn mở.

## F7. Package diagram thiết kế

File diagrams/P10-package-design.drawio, một trang. Layer xếp chồng từ trên xuống như P09; layer Application có hai hàng (RestApi trên, các dịch vụ ứng dụng dưới), layer Domain có hai hàng (PKG-28 ở hàng dưới). Package ở layer Presentation, Application phụ thuộc vào interface trong package tích hợp chứ không vào subsystem. PKG-12, PKG-13 chưa có phần tử nên không vẽ. Phụ thuộc tới PKG-22, PKG-23, PKG-24 vẽ tới package vì gồm cả lớp miền và interface kho dữ liệu.

a) Bảng Node. x, y, w, h là toạ độ tuyệt đối trên trang và bằng đúng toạ độ trong file .drawio (mọi cell có parent là lớp gốc của trang). Nhãn hiển thị trong sơ đồ gồm mã và tên (subsystem, interface có thêm dòng stereotype).

| ID (PKG, SS, IF, DC) | Loại (Layer / Package / Subsystem / Interface / Class) | Nhãn | Stereotype | Thuộc về | Ghi chú (visibility) | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-01 | Layer | Presentation | «layer» | - | Layer của P09 | 20 | 30 | 4440 | 200 |
| PKG-02 | Layer | Application | «layer» | - | Layer của P09 | 20 | 290 | 4440 | 380 |
| PKG-03 | Layer | Services | «layer» | - | Layer của P09 | 20 | 890 | 4440 | 190 |
| PKG-04 | Layer | Domain | «layer» | - | Layer của P09 | 20 | 1280 | 4440 | 420 |
| PKG-20 | Package | DeviceStore | - | PKG-03 | Xem F5 | 40 | 940 | 190 | 110 |
| SS-08 | Subsystem | DeviceLocalPersistence | «subsystem» | PKG-20 | package-private; chỉ interface public | 60 | 980 | 150 | 50 |
| PKG-21 | Package | ServerApiClient | - | PKG-03 | Xem F5 | 350 | 940 | 410 | 110 |
| IF-09 | Interface | IServerApiClient | «interface» | PKG-21 | public | 370 | 980 | 180 | 50 |
| SS-06 | Subsystem | ServerApiAccess | «subsystem» | PKG-21 | package-private; chỉ interface public | 590 | 980 | 150 | 50 |
| PKG-18 | Package | ScannerIntegration | - | PKG-03 | Xem F5 | 880 | 940 | 630 | 110 |
| IF-04 | Interface | IBarcodeReader | «interface» | PKG-18 | public | 900 | 980 | 180 | 50 |
| SS-03 | Subsystem | BarcodeReading | «subsystem» | PKG-18 | package-private; chỉ interface public | 1120 | 980 | 150 | 50 |
| IF-05 | Interface | IBarcodeReadListener | «interface» | PKG-18 | public | 1310 | 980 | 180 | 50 |
| PKG-17 | Package | PrinterIntegration | - | PKG-03 | Xem F5 | 1630 | 940 | 410 | 110 |
| IF-06 | Interface | ITicketPrinter | «interface» | PKG-17 | public | 1650 | 980 | 180 | 50 |
| SS-04 | Subsystem | TicketPrinting | «subsystem» | PKG-17 | package-private; chỉ interface public | 1870 | 980 | 150 | 50 |
| PKG-15 | Package | PaymentIntegration | - | PKG-03 | Xem F5 | 2160 | 940 | 630 | 110 |
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-15 | public | 2180 | 980 | 180 | 50 |
| SS-01 | Subsystem | OnlinePayment | «subsystem» | PKG-15 | package-private; chỉ interface public | 2400 | 980 | 150 | 50 |
| IF-02 | Interface | IPaymentResultListener | «interface» | PKG-15 | public | 2590 | 980 | 180 | 50 |
| PKG-16 | Package | SmsIntegration | - | PKG-03 | Xem F5 | 2910 | 940 | 410 | 110 |
| IF-03 | Interface | ISmsSender | «interface» | PKG-16 | public | 2930 | 980 | 180 | 50 |
| SS-02 | Subsystem | SmsDelivery | «subsystem» | PKG-16 | package-private; chỉ interface public | 3150 | 980 | 150 | 50 |
| PKG-19 | Package | Scheduling | - | PKG-03 | Xem F5 | 3440 | 940 | 630 | 110 |
| IF-07 | Interface | ITriggerScheduler | «interface» | PKG-19 | public | 3460 | 980 | 180 | 50 |
| SS-05 | Subsystem | TriggerScheduling | «subsystem» | PKG-19 | package-private; chỉ interface public | 3680 | 980 | 150 | 50 |
| IF-08 | Interface | ITriggerHandler | «interface» | PKG-19 | public | 3870 | 980 | 180 | 50 |
| PKG-14 | Package | Persistence | - | PKG-03 | Xem F5 | 4190 | 940 | 190 | 110 |
| SS-07 | Subsystem | ServerPersistence | «subsystem» | PKG-14 | package-private; chỉ interface public | 4210 | 980 | 150 | 50 |
| PKG-07 | Package | CheckerAppUI | - | PKG-01 | Xem F5 | 640 | 80 | 240 | 60 |
| PKG-05 | Package | PassengerWeb | - | PKG-01 | Xem F5 | 1400 | 80 | 240 | 60 |
| PKG-06 | Package | StaffWeb | - | PKG-01 | Package cha của PKG-26, PKG-27; không chứa phần tử trực tiếp | 1800 | 80 | 560 | 120 |
| PKG-26 | Package | TicketClerkWeb | - | PKG-06 | Xem F5 | 1820 | 120 | 240 | 60 |
| PKG-27 | Package | DispatcherWeb | - | PKG-06 | Xem F5 | 2100 | 120 | 240 | 60 |
| PKG-08 | Package | RestApi | - | PKG-02 | Xem F5 | 1700 | 340 | 260 | 60 |
| PKG-11 | Package | BoardingCheckService | - | PKG-02 | Xem F5 | 640 | 540 | 280 | 100 |
| DC-CheckBoardingTicketService | Class | CheckBoardingTicketService | - | PKG-11 | Xem F5; vẽ vì hiện thực interface callback | 660 | 580 | 240 | 40 |
| PKG-09 | Package | TicketSalesService | - | PKG-02 | Xem F5 | 2000 | 540 | 560 | 100 |
| DC-BookTicketOnlineService | Class | BookTicketOnlineService | - | PKG-09 | Xem F5; vẽ vì hiện thực interface callback | 2020 | 580 | 240 | 40 |
| DC-PayTicketOnlineService | Class | PayTicketOnlineService | - | PKG-09 | Xem F5; vẽ vì hiện thực interface callback | 2300 | 580 | 240 | 40 |
| PKG-10 | Package | TripOperationsService | - | PKG-02 | Xem F5 | 3100 | 540 | 280 | 60 |
| PKG-24 | Package | BoardingModel | - | PKG-04 | Xem F5 | 500 | 1330 | 220 | 110 |
| IF-12 | Interface | IBoardingRepository | «interface» | PKG-24 | public | 520 | 1370 | 180 | 50 |
| PKG-23 | Package | Ticketing | - | PKG-04 | Xem F5 | 1500 | 1330 | 220 | 110 |
| IF-11 | Interface | ITicketingRepository | «interface» | PKG-23 | public | 1520 | 1370 | 180 | 50 |
| PKG-22 | Package | TripCatalog | - | PKG-04 | Xem F5 | 2500 | 1330 | 220 | 110 |
| IF-10 | Interface | ITripCatalogRepository | «interface» | PKG-22 | public | 2520 | 1370 | 180 | 50 |
| PKG-25 | Package | AccountModel | - | PKG-04 | Xem F5 | 3600 | 1330 | 220 | 110 |
| IF-13 | Interface | IAccountRepository | «interface» | PKG-25 | public | 3620 | 1370 | 180 | 50 |
| PKG-28 | Package | SharedValueTypes | - | PKG-04 | Xem F5 | 1500 | 1610 | 300 | 60 |

b) Bảng Edge. Điểm uốn là toạ độ tuyệt đối từ nguồn tới đích; "-" là cạnh đi thẳng giữa hai cổng.

| ID | Nguồn | Đích | Loại quan hệ (Dependency / Realization) | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | PKG-05 | PKG-08 | Dependency | - | Store gọi REST | (1520,240); (1710,240) |
| E-02 | PKG-26 | PKG-08 | Dependency | - | Store gọi REST | (1940,250); (1780,250) |
| E-03 | PKG-27 | PKG-08 | Dependency | - | Store gọi REST | (2220,260); (1850,260) |
| E-04 | PKG-07 | PKG-11 | Dependency | - | ViewModel gọi dịch vụ soát vé trên máy | (760,270); (650,270) |
| E-05 | PKG-08 | PKG-09 | Dependency | - | - | (1830,450); (2080,450) |
| E-06 | PKG-08 | PKG-10 | Dependency | - | - | (1950,460); (3180,460) |
| E-07 | PKG-08 | PKG-11 | Dependency | - | - | (1710,470); (790,470) |
| E-08 | PKG-09 | IF-01 | Dependency | - | Hoàn tiền khi trả vé | (2230,680); (2190,680) |
| E-09 | PKG-09 | IF-03 | Dependency | - | Gửi vé qua SMS | (2430,690); (2940,690) |
| E-10 | PKG-09 | IF-06 | Dependency | - | Giữ từ P09 E-11, chờ P07 UC-005 | (2130,700); (1740,700) |
| E-11 | PKG-09 | IF-07 | Dependency | - | Đăng ký mốc hết hạn giữ chỗ | (2530,710); (3470,710) |
| E-12 | DC-BookTicketOnlineService | IF-08 | Realization | - | Xử lý mốc hết hạn giữ chỗ | (2140,720); (3960,720) |
| E-13 | DC-PayTicketOnlineService | IF-02 | Realization | - | Nhận kết quả thanh toán | (2420,730); (2680,730) |
| E-14 | PKG-10 | IF-01 | Dependency | - | Hoàn tiền khi huỷ chuyến | (3210,740); (2350,740) |
| E-15 | PKG-10 | IF-03 | Dependency | - | Báo huỷ chuyến qua SMS | (3310,750); (3100,750) |
| E-16 | PKG-10 | IF-07 | Dependency | - | Huỷ mốc kích hoạt của chuyến | (3360,760); (3630,760) |
| E-17 | DC-CheckBoardingTicketService | IF-05 | Realization | - | Nhận mã vé vừa quét | (780,770); (1400,770) |
| E-18 | PKG-11 | IF-04 | Dependency | - | Đăng ký bộ nhận mã vé | (780,780); (990,780) |
| E-19 | PKG-11 | IF-09 | Dependency | - | Nhận danh sách, gửi kết quả soát | (660,790); (460,790) |
| E-20 | PKG-09 | PKG-22 | Dependency | - | - | (2330,800); (2130,800); (2130,1090); (2580,1090) |
| E-21 | PKG-09 | PKG-23 | Dependency | - | - | (2030,810); (1600,810) |
| E-22 | PKG-10 | PKG-22 | Dependency | - | - | (3260,820); (2820,820); (2820,1110); (2650,1110) |
| E-23 | PKG-10 | PKG-23 | Dependency | - | - | (3160,830); (2070,830); (2070,1120); (1640,1120) |
| E-24 | PKG-10 | PKG-24 | Dependency | - | Giữ từ P09 E-20, chờ P07 UC-014 | (3110,840); (790,840); (790,1130); (650,1130) |
| E-25 | PKG-11 | PKG-22 | Dependency | - | - | (900,850); (1540,850); (1540,1140); (2510,1140) |
| E-26 | PKG-11 | PKG-23 | Dependency | - | - | (840,1150); (1520,1150) |
| E-27 | PKG-11 | PKG-24 | Dependency | - | - | (720,870); (800,870); (800,1160); (580,1160) |
| E-28 | SS-07 | IF-10 | Realization | - | - | (4300,1170); (2610,1170) |
| E-29 | SS-07 | IF-11 | Realization | - | - | (4260,1180); (1610,1180) |
| E-30 | SS-07 | IF-12 | Realization | - | - | (4220,1190); (690,1190) |
| E-31 | SS-07 | IF-13 | Realization | - | - | (4340,1200); (3710,1200) |
| E-32 | SS-08 | IF-12 | Realization | - | - | (140,1210); (530,1210) |
| E-33 | SS-01 | IF-01 | Realization | - | - | - |
| E-34 | SS-01 | IF-02 | Dependency | - | Trả kết quả thanh toán | - |
| E-35 | SS-02 | IF-03 | Realization | - | - | - |
| E-36 | SS-03 | IF-04 | Realization | - | - | - |
| E-37 | SS-03 | IF-05 | Dependency | - | Báo mã vé vừa quét | - |
| E-38 | SS-04 | IF-06 | Realization | - | - | - |
| E-39 | SS-05 | IF-07 | Realization | - | - | - |
| E-40 | SS-05 | IF-08 | Dependency | - | Báo mốc đến hạn | - |
| E-41 | SS-06 | IF-09 | Realization | - | - | - |
| E-42 | PKG-15 | PKG-28 | Dependency | - | Chữ ký IF-01, IF-02 dùng kiểu giá trị | (2480,1220); (1750,1220); (1750,1480); (1590,1480) |
| E-43 | PKG-16 | PKG-28 | Dependency | - | Chữ ký IF-03 dùng kiểu giá trị | (3120,1230); (1760,1230); (1760,1490); (1630,1490) |
| E-44 | PKG-18 | PKG-28 | Dependency | - | Chữ ký IF-05 dùng kiểu giá trị | (1200,1500); (1550,1500) |
| E-45 | PKG-17 | PKG-23 | Dependency | - | Dữ liệu vé cần in | (1840,1250); (1560,1250) |
| E-46 | PKG-21 | PKG-24 | Dependency | - | Danh sách hành khách, kết quả soát | (560,1260); (510,1260) |
| E-47 | PKG-22 | PKG-28 | Dependency | - | - | (2710,1510); (1610,1510) |
| E-48 | PKG-23 | PKG-28 | Dependency | - | - | (1610,1520); (1570,1520) |
| E-49 | PKG-24 | PKG-28 | Dependency | - | - | (510,1530); (1530,1530) |
| E-50 | PKG-23 | PKG-22 | Dependency | - | - | - |
| E-51 | PKG-24 | PKG-23 | Dependency | - | - | - |
| E-52 | PKG-24 | PKG-22 | Dependency | - | - | (710,1540); (2510,1540) |

## F8. Subsystem context diagram

File diagrams/P10-subsystem-context.drawio, 8 trang, mỗi subsystem một trang. Bố cục từ trái sang phải: lớp thiết kế (hoặc package khi chưa có lớp thiết kế riêng) dùng interface, interface dạng canonical ghi trách nhiệm dạng "// ...", subsystem hiện thực. Mọi cạnh nằm ngang hoặc có đoạn dọc trong dải trống giữa hai cột. Interface gọi ngược (IF-02, IF-05, IF-08) được lớp ở bên trái hiện thực (realization) và được subsystem phụ thuộc vào. Chi tiết operation để P11b làm.

Mỗi subsystem một trang (diagram) trong file; nhãn trang là "SS-nn Tên". x, y, w, h là toạ độ tuyệt đối trên trang. ID cạnh = mã trang + E-nn.

a) Bảng Node

| Trang | ID | Loại (Subsystem / Interface / Class / Package) | Nhãn | Stereotype | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-01 | IF-01 | Interface | IPaymentGateway | «interface» | Trách nhiệm: // requestRefund, // returnRefundResult | 440 | 40 | 320 | 90 |
| SS-01 | IF-02 | Interface | IPaymentResultListener | «interface» | Trách nhiệm: // receivePaymentResult | 440 | 170 | 320 | 70 |
| SS-01 | SS-01 | Subsystem | OnlinePayment | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 200 |
| SS-01 | DC-ReturnTicketService | Class | DC-ReturnTicketService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 40 | 280 | 40 |
| SS-01 | DC-CancelTripService | Class | DC-CancelTripService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 120 | 280 | 40 |
| SS-01 | DC-PayTicketOnlineService | Class | DC-PayTicketOnlineService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 200 | 280 | 40 |
| SS-02 | IF-03 | Interface | ISmsSender | «interface» | Trách nhiệm: // sendSms | 440 | 40 | 320 | 70 |
| SS-02 | SS-02 | Subsystem | SmsDelivery | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 70 |
| SS-02 | DC-BookTicketOnlineService | Class | DC-BookTicketOnlineService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 40 | 280 | 40 |
| SS-02 | DC-CancelTripService | Class | DC-CancelTripService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 120 | 280 | 40 |
| SS-03 | IF-04 | Interface | IBarcodeReader | «interface» | Trách nhiệm: // readBarcode | 440 | 40 | 320 | 70 |
| SS-03 | IF-05 | Interface | IBarcodeReadListener | «interface» | Trách nhiệm: // receiveScannedCode | 440 | 150 | 320 | 70 |
| SS-03 | SS-03 | Subsystem | BarcodeReading | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 180 |
| SS-03 | DC-CheckBoardingTicketService | Class | DC-CheckBoardingTicketService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 100 | 280 | 40 |
| SS-04 | IF-06 | Interface | ITicketPrinter | «interface» | Trách nhiệm: // printTicket | 440 | 40 | 320 | 70 |
| SS-04 | SS-04 | Subsystem | TicketPrinting | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 70 |
| SS-04 | PKG-09 | Package | PKG-09 TicketSalesService | - | Package dùng interface (chưa có lớp thiết kế riêng) | 40 | 40 | 280 | 40 |
| SS-05 | IF-07 | Interface | ITriggerScheduler | «interface» | Trách nhiệm: // scheduleTrigger, // cancelTriggers | 440 | 40 | 320 | 90 |
| SS-05 | IF-08 | Interface | ITriggerHandler | «interface» | Trách nhiệm: // handleTrigger | 440 | 170 | 320 | 70 |
| SS-05 | SS-05 | Subsystem | TriggerScheduling | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 200 |
| SS-05 | DC-CancelTripService | Class | DC-CancelTripService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 50 | 280 | 40 |
| SS-05 | DC-BookTicketOnlineService | Class | DC-BookTicketOnlineService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 130 | 280 | 40 |
| SS-06 | IF-09 | Interface | IServerApiClient | «interface» | Trách nhiệm: // fetchPassengerList, // submitCheckResult | 440 | 40 | 320 | 90 |
| SS-06 | SS-06 | Subsystem | ServerApiAccess | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 90 |
| SS-06 | DC-CheckBoardingTicketService | Class | DC-CheckBoardingTicketService | - | Lớp thiết kế dùng hoặc hiện thực interface | 40 | 40 | 280 | 40 |
| SS-07 | IF-10 | Interface | ITripCatalogRepository | «interface» | Trách nhiệm: // retrieveTripCatalog, // saveTripCatalog | 440 | 40 | 320 | 90 |
| SS-07 | IF-11 | Interface | ITicketingRepository | «interface» | Trách nhiệm: // retrieveTicketing, // saveTicketing | 440 | 170 | 320 | 90 |
| SS-07 | IF-12 | Interface | IBoardingRepository | «interface» | Trách nhiệm: // retrievePassengerList, // saveCheckSession | 440 | 300 | 320 | 90 |
| SS-07 | IF-13 | Interface | IAccountRepository | «interface» | Trách nhiệm: // retrieveAccount, // saveAccount | 440 | 430 | 320 | 90 |
| SS-07 | SS-07 | Subsystem | ServerPersistence | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 480 |
| SS-07 | PKG-09 | Package | PKG-09 TicketSalesService | - | Package dùng interface (chưa có lớp thiết kế riêng) | 40 | 110 | 280 | 40 |
| SS-07 | PKG-10 | Package | PKG-10 TripOperationsService | - | Package dùng interface (chưa có lớp thiết kế riêng) | 40 | 190 | 280 | 40 |
| SS-07 | PKG-11 | Package | PKG-11 BoardingCheckService | - | Package dùng interface (chưa có lớp thiết kế riêng) | 40 | 270 | 280 | 40 |
| SS-08 | IF-12 | Interface | IBoardingRepository | «interface» | Trách nhiệm: // retrievePassengerList, // saveCheckSession | 440 | 40 | 320 | 90 |
| SS-08 | SS-08 | Subsystem | DeviceLocalPersistence | «subsystem» | Hiện thực interface của trang | 900 | 40 | 220 | 90 |
| SS-08 | PKG-11 | Package | PKG-11 BoardingCheckService | - | Package dùng interface (chưa có lớp thiết kế riêng) | 40 | 40 | 280 | 40 |

b) Bảng Edge

| ID | Trang | Nguồn | Đích | Loại quan hệ (Dependency / Realization) | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|---|
| SS-01-E-01 | SS-01 | DC-ReturnTicketService | IF-01 | Dependency | - | - | (350,50); (350,60) |
| SS-01-E-02 | SS-01 | DC-CancelTripService | IF-01 | Dependency | - | - | (360,130); (360,70) |
| SS-01-E-03 | SS-01 | DC-PayTicketOnlineService | IF-02 | Realization | - | - | (370,210); (370,190) |
| SS-01-E-04 | SS-01 | SS-01 | IF-01 | Realization | - | - | - |
| SS-01-E-05 | SS-01 | SS-01 | IF-02 | Dependency | - | - | - |
| SS-02-E-01 | SS-02 | DC-BookTicketOnlineService | IF-03 | Dependency | - | - | (350,50); (350,60) |
| SS-02-E-02 | SS-02 | DC-CancelTripService | IF-03 | Dependency | - | - | (360,130); (360,70) |
| SS-02-E-03 | SS-02 | SS-02 | IF-03 | Realization | - | - | - |
| SS-03-E-01 | SS-03 | DC-CheckBoardingTicketService | IF-04 | Dependency | - | - | (350,110); (350,60) |
| SS-03-E-02 | SS-03 | DC-CheckBoardingTicketService | IF-05 | Realization | - | - | (360,120); (360,170) |
| SS-03-E-03 | SS-03 | SS-03 | IF-04 | Realization | - | - | - |
| SS-03-E-04 | SS-03 | SS-03 | IF-05 | Dependency | - | - | - |
| SS-04-E-01 | SS-04 | PKG-09 | IF-06 | Dependency | - | - | (350,50); (350,60) |
| SS-04-E-02 | SS-04 | SS-04 | IF-06 | Realization | - | - | - |
| SS-05-E-01 | SS-05 | DC-BookTicketOnlineService | IF-07 | Dependency | - | - | (350,140); (350,60) |
| SS-05-E-02 | SS-05 | DC-CancelTripService | IF-07 | Dependency | - | - | (360,60); (360,70) |
| SS-05-E-03 | SS-05 | DC-BookTicketOnlineService | IF-08 | Realization | - | - | (370,150); (370,190) |
| SS-05-E-04 | SS-05 | SS-05 | IF-07 | Realization | - | - | - |
| SS-05-E-05 | SS-05 | SS-05 | IF-08 | Dependency | - | - | - |
| SS-06-E-01 | SS-06 | DC-CheckBoardingTicketService | IF-09 | Dependency | - | - | (350,50); (350,60) |
| SS-06-E-02 | SS-06 | SS-06 | IF-09 | Realization | - | - | - |
| SS-07-E-01 | SS-07 | PKG-09 | IF-10 | Dependency | - | - | (350,120); (350,60) |
| SS-07-E-02 | SS-07 | PKG-09 | IF-11 | Dependency | - | - | (360,130); (360,190) |
| SS-07-E-03 | SS-07 | PKG-10 | IF-10 | Dependency | - | - | (370,200); (370,70) |
| SS-07-E-04 | SS-07 | PKG-10 | IF-11 | Dependency | - | - | (380,210); (380,200) |
| SS-07-E-05 | SS-07 | PKG-11 | IF-10 | Dependency | - | - | (390,280); (390,80) |
| SS-07-E-06 | SS-07 | PKG-11 | IF-11 | Dependency | - | - | (400,290); (400,210) |
| SS-07-E-07 | SS-07 | PKG-11 | IF-12 | Dependency | - | - | (410,300); (410,320) |
| SS-07-E-08 | SS-07 | SS-07 | IF-10 | Realization | - | - | - |
| SS-07-E-09 | SS-07 | SS-07 | IF-11 | Realization | - | - | - |
| SS-07-E-10 | SS-07 | SS-07 | IF-12 | Realization | - | - | - |
| SS-07-E-11 | SS-07 | SS-07 | IF-13 | Realization | - | - | - |
| SS-08-E-01 | SS-08 | PKG-11 | IF-12 | Dependency | - | - | (350,50); (350,60) |
| SS-08-E-02 | SS-08 | SS-08 | IF-12 | Realization | - | - | - |


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | Không có | Không có | Không có |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P09 | PKG-06, E-02 | PKG-06 StaffWeb gồm boundary của ACT-02, ACT-03 (và ACT-04 về sau), vi phạm quy tắc hai boundary người dùng của hai tác nhân không cùng package (P10 A3) | Ghi PKG-06 là package cha; thêm PKG-26 TicketClerkWeb, PKG-27 DispatcherWeb; thay E-02 bằng hai cạnh tới PKG-08 |
| P09 | F8 dòng cuối, E-34 | Văn bản ghi Trip và Ticket cũng lưu cục bộ qua PKG-20 nhưng chỉ có phụ thuộc PKG-20 --> PKG-24 | P10 để SS-08 hiện thực chỉ IF-12 (dữ liệu vé và chuyến lưu cục bộ như một phần danh sách hành khách); sửa lời F8 cho khớp |
| P09 | F4 PKG-08, E-06 | Không có thành phần REST nào nhận kết quả soát vé từ máy soát vé và cấp danh sách hành khách | P10 thêm DC-BoardingSyncRestController vào PKG-08; bổ sung mô tả PKG-08 |
| P09 | E-07, E-08, PKG-12, PKG-13 | Phụ thuộc đặt theo P02, chưa có lớp P08 | Giữ nguyên, rà lại khi P08 phủ UC-009 đến UC-011, UC-016 đến UC-018 |
| P08 | AC-E-Trip // getCancellationSummary, // cancelTrip | Hai trách nhiệm yêu cầu Trip truy vấn Ticket, PhoneReservation, tạo vòng giữa hai package miền | P10 tách DC-TripCancellation (F3); P08 ghi hai trách nhiệm này là phối hợp Trip - Ticket - PhoneReservation khi chạy lại |
| P08 | AC-E-TicketCheckSession // sendResult | Entity ở layer Domain không gọi được layer Services để gửi qua mạng | P10 giao việc gửi cho DC-CheckBoardingTicketService qua IF-09; P08 ghi // sendResult là điều phối khi chạy lại |
| P08 | R-33, R-34 | Quan hệ vẽ từ Trip, P10 cần điều hướng từ PhoneReservation và TripPassengerList sang Trip để không tạo vòng (đã nêu ở P09) | Ghi điều hướng khi chạy lại P08 hoặc ở P12 |

## Vấn đề còn mở

- Phạm vi: P08 mới phủ 4 trong 18 use case. PKG-12 AccountService, PKG-13 PricingReportService chưa có phần tử; PKG-25 AccountModel chỉ có IF-13 giữ chỗ; chưa có package giao diện web cho ACT-04 (Quản lý nhà xe). Cần chạy lại P10 khi P08 và P09 được cập nhật.
- DC-PayTicketOnlineService còn ở trạng thái tạm; IF-01 mới có trách nhiệm hoàn tiền, trách nhiệm thu tiền chờ P07 của UC-003 (P09 F8 đã ghi).
- Target 6: 8 phụ thuộc Application --> Domain (F6) nhảy qua layer Services. P09 chọn layered nới lỏng (R1) nên coi là hợp lệ, không sửa.
- Chọn giữa hai quy tắc (C9): P09 đặt boundary web của ACT-02, ACT-03 chung PKG-06, còn A3 cấm hai boundary hai tác nhân cùng package. Đã chọn A3 (quy tắc không được cùng package ưu tiên hơn gắn kết chức năng và hơn việc giữ nguyên PKG của P09), tách thành PKG-26, PKG-27.
- Chọn giữa hai quy tắc (C9): A3 yêu cầu kiểu giá trị ở package cùng layer hoặc thấp hơn interface; PKG-28 gom bốn kiểu giá trị (khác lỗi thường gặp "Common" vì cùng loại và chỉ phục vụ chữ ký interface). Kiểu giá trị xuất hiện trong chữ ký của lớp ở Application, Persistence, DeviceStore cũng thuộc PKG-28; phụ thuộc này không vẽ riêng vì đã có đường tới PKG-28 qua PKG-22 đến PKG-24, không tạo vòng và không đổi kết luận F6.
- Package một phần tử: PKG-10, PKG-11 (một control), PKG-14, PKG-20 (một subsystem), PKG-25 (một interface giữ chỗ); lý do ghi ở F4.
- PKG-08 chứa REST controller phục vụ nhiều tác nhân (ACT-01, ACT-02, ACT-03, ACT-05). P10 coi REST controller không phải boundary giao diện người dùng (P09 F5) nên giữ chung một package; nếu tổ chức muốn tách theo tác nhân thì chia PKG-08 thành các package con tương tự PKG-26, PKG-27.
- Q-75: nếu trạng thái chỗ được suy ra từ vé và lần đặt thì DC-Seat cần truy vấn Ticketing, tạo phụ thuộc PKG-22 --> PKG-23 và vòng với PKG-23 --> PKG-22; phải chạy lại P09, P10.
- Hai phụ thuộc kế thừa P09 chưa có căn cứ lớp P08: PKG-09 --> PKG-17 (E-10 ở F7, UC-005) và PKG-10 --> PKG-24 (E-24, UC-014); PKG-17 --> PKG-23 do dữ liệu vé cần in là suy luận của P10.
- Target 9: bố cục được kiểm bằng tính toán toạ độ (không node chồng nhau, khoảng cách tối thiểu 40, cạnh trực giao không cắt qua node, mọi toạ độ node là bội số của 10); chưa mở bằng draw.io để xem nhãn và nét vẽ. Sơ đồ F7 rộng khoảng 4.500 đơn vị vì mỗi package tích hợp chứa subsystem và interface xếp ngang.
