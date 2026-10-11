# P12 - Thiết kế lớp PKG-13, PKG-27, PKG-28 - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P12 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CONG_NGHE đã chốt: Java 17, Spring Boot, Thymeleaf, PostgreSQL; máy soát vé Kotlin, Android, SQLite - chỉ phần máy chủ liên quan); P10-design-elements.md phiên bản 1.0 (F3 gồm bảng ánh xạ và bảng phần tử mới do cơ chế kiến trúc, F4, F5, F6, Vấn đề còn mở); P08-analysis-model.md phiên bản 1.0 (F3, F4 R-01 đến R-22, F6, Câu hỏi mở Q-59 đến Q-61, Giả định ASM-43, ASM-44, Vấn đề còn mở); P07-uc-analysis/UC-009-book-ticket-online-analysis.md phiên bản 1.0 (F3.4, F4, F5 trang SD1a, SD1b, SD1c, SD2, F8, Q-55 đến Q-57, ASM-39 đến ASM-41, Vấn đề còn mở); P07-uc-analysis/UC-017-cancel-trip-analysis.md phiên bản 1.0 (F3.4, F5 trang SD1, SD2, Vấn đề còn mở; chỉ các message có lớp nhận Trip, Ticket); P09-architecture.md phiên bản 1.0 (F1 dòng 1, 5, 9, F3, F4, F5, F6, F7); P11b-system-interfaces.md phiên bản 1.0 (SS-01 và SS-02: F2, F3, F5, F7, Câu hỏi mở, Giả định); P11a-gui/screen-list.md, SCR-02-select-seats.md, SCR-03-enter-traveler-info.md, SCR-04-issued-tickets.md (dữ liệu của view model); P04-uc-specs/UC-009-book-ticket-online.md, UC-017-cancel-trip.md phiên bản 1.0 (mục 5, 6, 8, Câu hỏi mở, Giả định); P06-supplementary-spec.md phiên bản 1.0 (Mục 3 đến 5: NFR-01, NFR-02, NFR-04 đến NFR-06, NFR-08, NFR-10 đến NFR-12); P05-glossary.md phiên bản 1.0 (GL-01 đến GL-28). Không dùng P07 của UC khác UC-009, UC-017 và P11b của SS khác SS-01, SS-02. Placeholder: PHAM_VI_THIET_KE = "PKG-13 Booking, PKG-27 Operations, PKG-28 Ticketing (chưa có file P12 nào khác)"; QUY_UOC_KIEU_DU_LIEU = Không có (dùng kiểu của Java); MAU_THIET_KE_DA_CHOT = Không có; YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-72, ASM-54 (P11a); lần chạy này cấp Q-73, Q-74, ASM-55, ASM-56. Mã R-nn lớn nhất trước lần chạy: R-22 (P08); lần chạy này cấp R-23 đến R-45. Mã ST-nn cấp mới từ ST-01 đến ST-04. Mã IF-nn lớn nhất: IF-08 (P10); lần chạy này không cấp IF mới |
| Phạm vi | PKG-13 Booking, PKG-27 Operations, PKG-28 Ticketing; 14 lớp có hành vi (control, entity, lớp dịch vụ miền, interface) và 15 dòng ở F1 kể cả view model; 26 kiểu phụ trợ ở F1b. Dưới ngưỡng khoảng 20 lớp có hành vi nên chạy một lượt, không chia hai lượt |
| Mã Q, ASM cuối đã cấp | Q-74, ASM-56 |

Kiểm tra đầu vào (B0): placeholder đã điền đủ theo C6, hai placeholder tuỳ chọn đã thay bằng "Không có". CONG_NGHE đã chốt Java 17 nên kiểu dữ liệu theo Java (bảng ánh xạ kiểu ở đầu F2). Mẫu kiến trúc theo P09 F3, F5: layered nới lỏng, MVC passive ở Presentation; stereotype control thành lớp dịch vụ ứng dụng (hậu tố Service, giữ tên P10), entity thành lớp miền ở Domain, kho dữ liệu là interface ở Domain do PKG-20 hiện thực.

Danh sách phần tử trong phạm vi: (a) bảng ánh xạ P10 F3: DC-BookTicketOnlineService, DC-SearchTripsService, DC-PayTicketOnlineService (PKG-13), DC-Trip, DC-Fare (PKG-27), DC-Seat, DC-Booking, DC-Ticket (PKG-28); (b) bảng phần tử mới do cơ chế kiến trúc của P10: DC-BookTicketOnlineViewModel (PKG-13), IF-03, IF-04 (PKG-27), IF-05, IF-06, IF-07 (PKG-28); (c) không có lớp bên trong subsystem do P11b cấp mã DC thuộc phạm vi (SS-01, SS-02 chỉ dùng qua IF-01, IF-02); (d) interface IF-01, IF-02, IF-08 được dùng nhưng thuộc package khác nên chỉ liệt kê ở F5. Ngoài phạm vi: DC-HoldExpiryTrigger (PKG-11), DC-Money, DC-TicketCode, DC-PhoneNumber (PKG-31), DC-PaymentTransaction, IF-08 (PKG-29), DC-Relational*Repository (PKG-20), DC-CancelTripService, DC-CancelTripViewModel (PKG-16), View và RequestHandler (PKG-05, PKG-07).

UC có lớp trong phạm vi tham gia (cột Dùng trong UC của P08): UC-009 (P07 đã có), UC-017 (Trip, Ticket; chỉ các message có lớp nhận thuộc phạm vi), UC-008 và UC-010 (control tạm, chưa có P04, P07).

Chữ ký interface tạm (Bước 0): IF-01 và IF-08 được DC-PayTicketOnlineService dùng nhưng chưa có chữ ký (P11b ghi "Chờ P07 UC-010"; PKG-29 chưa chạy P12); các kiểu giá trị ở PKG-31 chưa chạy P12. Chữ ký dưới đây là tạm, dùng ở F2, F3, F4. Đề xuất sửa artifact trước: chạy P07 của UC-010 rồi P11b cho SS-01; khi có chữ ký, chạy lại P12 cho PKG-13.

| IF hoặc lớp | Chữ ký tạm | Lý do | Message P07 nguồn |
|---|---|---|---|
| IF-01 | collectPayment(amount: Money, orderReference: String): PaymentCollectionResult | Thu tiền vé qua Cổng thanh toán (NFR-10); P11b ghi "Chờ P07 UC-010" nên chưa có chữ ký. orderReference là mã lần đặt gửi cho cổng; PaymentCollectionResult gồm status (Collected / NotCollected) và transactionCode: PaymentTransactionCode khi Collected | P07 UC-009 SD1b-M08 (STT 3.1.4) // payTicketOnline (lần đặt vé, tổng tiền); kết quả thành công hoặc thất bại |
| IF-01 | cancelPaymentSession(orderReference: String): void | Dừng phiên thanh toán đang chạy của lần đặt khi hết thời hạn giữ chỗ (ASM-41); không làm gì khi không có phiên | P07 UC-009 SD1b-M17 (STT 4.2) // cancelPayment |
| IF-08 | save(transaction: PaymentTransaction): PaymentTransaction | Lưu giao dịch thu tiền; interface thuộc PKG-29 chưa có chữ ký vì chưa chạy P12 cho PKG-29. Chữ ký theo quy ước chung của interface kho dữ liệu, lần chạy PKG-29 có thể đổi | P09 F6 PKG-13 --> PKG-29; P10 F3 IF-08 (Tạm, chờ P07 UC-010) |
| DC-PaymentTransaction | collected(code: PaymentTransactionCode, amount: Money): PaymentTransaction (classifier) | Tạo giao dịch đã thu tiền; lớp thuộc PKG-29, chữ ký tạm để DC-PayTicketOnlineService.payTicketOnline có chỗ gọi. Lần chạy PKG-29 chốt chữ ký | P07 UC-009 SD1b-M09 (kết quả thanh toán thành công); P08 F3 AC-E-PaymentTransaction |
| DC-Money | multiply(factor: int): Money; scaleBy(factor: BigDecimal): Money (làm tròn về đồng, HALF_UP); toBigDecimal(): BigDecimal | Kiểu giá trị ở PKG-31 chưa chạy P12; chữ ký tạm cho Booking.calculateTotalAmount, Fare.determineFare, view model, TripCancellationSummary | P10 F3 DC-Money; ASM-56 |
| DC-PhoneNumber | of(value: String): PhoneNumber (classifier); value(): String | Kiểu giá trị ở PKG-31; of chuẩn hoá chuỗi số (bỏ khoảng trắng, dấu chấm, dấu gạch ngang theo SCR-03); điều kiện hợp lệ khác chờ Q-44 | P10 F3 DC-PhoneNumber; P11a SCR-03 trường Số điện thoại người đi |
| DC-TicketCode | of(value: String): TicketCode (classifier); value(): String | Kiểu giá trị ở PKG-31; value() dùng khi hiển thị và gửi SMS | P10 F3 DC-TicketCode; GL-15 |

## F1. Bảng lớp thiết kế

| DC | Tên | Stereotype | PKG | Trách nhiệm | Nguồn AC | Loại | Persistent | Ghi chú thiết kế |
|---|---|---|---|---|---|---|---|---|
| DC-BookTicketOnlineService | BookTicketOnlineService | «control» | PKG-13 | Điều phối luồng đặt vé trực tuyến của UC-009 từ chọn chỗ đến phát hành vé | AC-C-BookTicketOnlineController; P10 F3 (tách thành DC-BookTicketOnlineService và DC-HoldExpiryTrigger) | class | Không | Lớp dịch vụ ứng dụng theo P09 F5 (không dùng hậu tố Controller, tránh nhầm với controller của MVC passive). Là ranh giới giao dịch của từng bước (F3). Phân tích control: cần (điều phối 5 lớp miền, 2 control khác, 1 interface); không tách thêm vì cùng một UC, cùng tác nhân ACT-01, cùng lý do thay đổi (luồng UC-009); khởi động lại và nhiều bản sao: không giữ bộ đếm trong bộ nhớ (P09 F5) |
| DC-SearchTripsService | SearchTripsService | «control» | PKG-13 | Điều phối tra cứu chuyến xe và xem sơ đồ chỗ của UC-008 | AC-C-SearchTripsController (Tạm, chờ P07 của UC-008) | class | Không | Tạm: UC-008 chưa có P04, P07; chữ ký ở F2 chỉ đủ cho UC-009. Phân tích control: cần (UC-008 được include bởi UC-009, UC-004, UC-005, UC-014, UC-015, P10 F5); không gộp vào DC-BookTicketOnlineService vì nhiều UC khác cùng dùng |
| DC-PayTicketOnlineService | PayTicketOnlineService | «control» | PKG-13 | Điều phối thanh toán vé trực tuyến của UC-010 qua Cổng thanh toán | AC-C-PayTicketOnlineController (Tạm, chờ P07 của UC-010) | class | Không | Tạm: UC-010 chưa có P04, P07. Phân tích control: cần (che IF-01 và IF-08 khỏi DC-BookTicketOnlineService, UC-014 sẽ dùng lại); ranh giới giao dịch: không bao lời gọi Cổng thanh toán (P09 F7) |
| DC-BookTicketOnlineViewModel | BookTicketOnlineViewModel | «value object» | PKG-13 | Chứa dữ liệu hiển thị của các màn hình đặt vé để Presentation không phụ thuộc Domain | P10 cơ chế MVC passive (P09 F3, QT-4); thuộc tính selectedSeats, issuedTickets, totalAmount của AC-B-BookTicketOnlineForm | value object | Không | Java record, bất biến, accessor do ngôn ngữ sinh nên không liệt kê ở F2. Dùng BigDecimal, String, LocalDateTime thay Money, TicketCode, PhoneNumber vì PKG-05 chỉ được phụ thuộc Application (P09 QT-4). Dữ liệu theo SCR-02, SCR-03, SCR-04 |
| DC-Trip | Trip | «entity» | PKG-27 | Lưu thông tin một chuyến xe và kiểm soát việc huỷ chuyến | AC-E-Trip | class | Có | Có state machine ST-01. route, vehicle, driver kiểu String vì Tuyến xe, Xe, Tài xế chưa có lớp (P08 Vấn đề còn mở); đổi thành association khi UC-020, UC-021, UC-022 có P07. Tạo chuyến thuộc UC-016 (chưa có P07) |
| DC-Fare | Fare | «entity» | PKG-27 | Lưu giá vé theo tuyến xe và loại xe và xác định giá một chỗ của chuyến | AC-E-Fare | class | Có | Một dòng Fare cho mỗi cặp (route, vehicleType). Mức tăng giá chỉ là surchargePercent đang áp dụng; khoảng ngày áp dụng thuộc UC-024 (Q-23, Q-24), xét lại khi có P07 của UC-023, UC-024 |
| IF-03 | ITripRepository | «interface» | PKG-27 | Cung cấp truy cập lưu trữ cho Trip mà không để Application biết cơ sở dữ liệu | P10 cơ chế Persistence (P09 F5, QT-5) | interface | Không | Hiện thực bởi DC-RelationalTripRepository (PKG-20, lần chạy PKG-20) |
| IF-04 | IFareRepository | «interface» | PKG-27 | Cung cấp truy cập lưu trữ cho Fare mà không để Application biết cơ sở dữ liệu | P10 cơ chế Persistence | interface | Không | Hiện thực bởi DC-RelationalFareRepository (PKG-20) |
| DC-Seat | Seat | «entity» | PKG-28 | Lưu trạng thái bán của một chỗ trên một chuyến xe và bảo đảm chỉ một yêu cầu giữ được chỗ | AC-E-Seat | class | Có | Có state machine ST-02. Chỗ của chuyến xe định danh bằng (trip, seatCode) theo ASM-43. Đồng thời (NFR-04): ISeatRepository nạp chỗ bằng khoá ghi theo thứ tự mã chỗ (F3). Tạo chỗ khi lập chuyến thuộc UC-016, UC-021 (chưa có P07) |
| DC-Booking | Booking | «entity» | PKG-28 | Lưu một lần đặt vé và kiểm soát vòng đời giữ chỗ, thanh toán và phát hành vé của nó | AC-E-Booking | class | Có | Có state machine ST-03. trip và seatCodes của P08 thành association R-12 và R-10 (không lặp ở F7). 17 operation public trong đó 8 là getter (F2); các quy tắc BR-01, BR-03, BR-04 nằm ở đây. Booking ở trạng thái SELECTING chỉ tồn tại trong bộ nhớ của một giao dịch, chỉ lưu từ HOLDING |
| DC-Ticket | Ticket | «entity» | PKG-28 | Lưu một vé của một chỗ trên một chuyến xe và kiểm soát việc huỷ và hoàn tiền của vé đó | AC-E-Ticket | class | Có | Có state machine ST-04. Bốn trách nhiệm tác động lên tập vé của chuyến tách sang DC-TripTicketCancellation (P08 F6 không đạt gắn kết; P10 F1 giao P12 quyết định). 20 operation public trong đó 11 là getter; còn 9 operation hành vi và kiểm tra |
| DC-TripTicketCancellation | TripTicketCancellation | «service» | PKG-28 | Thực hiện các thao tác lên tập vé đang có hiệu lực của một chuyến bị huỷ | Thiết kế: tách từ AC-E-Ticket (cancelTicketsOfTrip, groupTicketCodesByTravelerPhone, selectOnlineTicketsToRefund, summarizeTripCancellation; P08 F6 Target 3 không đạt) | class | Không | Dịch vụ miền không trạng thái, nhận ITicketRepository qua constructor. Đặt ở PKG-28 cùng entity Ticket nên PKG-16 chỉ thêm phụ thuộc vào PKG-28 đã có. Đề xuất cập nhật P10 F3, F4 (mục Đề xuất sửa artifact trước) |
| IF-05 | ISeatRepository | «interface» | PKG-28 | Cung cấp truy cập lưu trữ cho Seat, gồm nạp có khoá ghi để giữ chỗ không trùng | P10 cơ chế Persistence; NFR-04 | interface | Không | Hiện thực bởi DC-RelationalSeatRepository (PKG-20) |
| IF-06 | IBookingRepository | «interface» | PKG-28 | Cung cấp truy cập lưu trữ cho Booking, gồm tìm các lần đặt đã hết thời hạn giữ chỗ | P10 cơ chế Persistence | interface | Không | Hiện thực bởi DC-RelationalBookingRepository (PKG-20) |
| IF-07 | ITicketRepository | «interface» | PKG-28 | Cung cấp truy cập lưu trữ cho Ticket, gồm cấp mã vé duy nhất | P10 cơ chế Persistence | interface | Không | Hiện thực bởi DC-RelationalTicketRepository (PKG-20). Ràng buộc duy nhất trên (chuyến, chỗ) cho vé đang có hiệu lực (BR-02, P09 F7) do P13 định nghĩa |

Ghi chú chung: interface giữ mã IF-nn của P10, không cấp DC. Phân tích 4 câu hỏi của Bước 1.4 cho ba control nằm ở cột Ghi chú thiết kế của F1. DC-HoldExpiryTrigger (PKG-11) tách khỏi DC-BookTicketOnlineService theo P10 nên không thuộc lần chạy này; điểm vào cho nó là DC-BookTicketOnlineService.listExpiredHolds và handleHoldExpiry.

### F1b. Kiểu phụ trợ

| DC | Loại | PKG | Thành phần hoặc giá trị | Dùng trong chữ ký (DC.operation, IF.operation) |
|---|---|---|---|---|
| DC-TripOption | value object | PKG-13 | tripId: long; route: String; departureTime: LocalDateTime; vehicleType: String | DC-SearchTripsService.searchTrips |
| DC-SeatCell | value object | PKG-13 | seatCode: String; selectable: boolean (true khi chỗ trống, BR-02) | DC-BookTicketOnlineViewModel.seatMap |
| DC-IssuedTicketLine | value object | PKG-13 | ticketCode: String; seatCode: String; fare: BigDecimal | DC-BookTicketOnlineViewModel.issuedTickets |
| DC-PaymentFailedException | exception | PKG-13 | Không có thành phần; ném khi UC-010 trả kết quả thất bại (luồng 8a) | DC-BookTicketOnlineService.processTravelerInfo |
| DC-VehicleType | enumeration | PKG-27 | SLEEPER_40 (xe giường nằm 40 chỗ); SEATER_29 (xe ghế ngồi 29 chỗ) - GL-14, REQ-03 | DC-Trip.getVehicleType, DC-Fare (constructor), IF-04.findByRouteAndVehicleType |
| DC-TripStatus | enumeration | PKG-27 | SCHEDULED (Chưa huỷ); CANCELLED (Đã huỷ) - GL-03, GL-04 | DC-Trip.getStatus |
| DC-CancelReason | enumeration | PKG-27 | VEHICLE_BREAKDOWN (Xe hỏng); BAD_WEATHER (Thời tiết) - ASM-25 | DC-Trip.cancel, DC-Trip.getCancelReason |
| DC-TripNotFoundException | exception | PKG-27 | Không có thành phần; ném khi không có chuyến ứng với định danh | DC-BookTicketOnlineService.startBookTicketOnline, processSeatSelection, DC-SearchTripsService.viewSeatMap |
| DC-FareNotFoundException | exception | PKG-27 | Không có thành phần; ném khi chưa có giá vé cho cặp (tuyến xe, loại xe) của chuyến | DC-BookTicketOnlineService.processSeatSelection |
| DC-TripDepartedException | exception | PKG-27 | Không có thành phần; ném khi chuyến đã đến giờ xuất bến (BR-05, BR-10; luồng 4c của UC-009, 4b của UC-017) | DC-BookTicketOnlineService.processSeatSelection, DC-Trip.cancel |
| DC-TripAlreadyCancelledException | exception | PKG-27 | Không có thành phần; ném khi chuyến đã bị huỷ (BR-09; luồng 4a của UC-017) | DC-Trip.cancel |
| DC-SeatState | enumeration | PKG-28 | AVAILABLE (Trống); HELD (Đang giữ); SOLD (Đã bán) - P08 Seat.tripState | DC-Seat.getTripState |
| DC-BookingStatus | enumeration | PKG-28 | SELECTING (Đang chọn); HOLDING (Đang giữ chỗ); TICKETS_ISSUED (Đã phát hành vé); SEATS_RELEASED (Đã trả chỗ) - P08 Booking.status | DC-Booking.getStatus |
| DC-TicketStatus | enumeration | PKG-28 | ISSUED (Đã phát hành); CANCELLED (Đã huỷ) - GL-23, GL-24; giá trị đã trả, đã đổi chờ UC-012, UC-014 | DC-Ticket.getStatus |
| DC-PurchaseChannel | enumeration | PKG-28 | ONLINE (Trực tuyến); COUNTER (Tại quầy) - GL-11 | DC-Ticket.createTicket (kênh cố định ONLINE); DC-Ticket.isOnlineRefundPending |
| DC-PaymentStatus | enumeration | PKG-28 | PAID (Đã thanh toán); UNPAID (Chưa thanh toán) - ASM-29 | DC-Ticket.cancelForTrip |
| DC-RefundStatus | enumeration | PKG-28 | NOT_APPLICABLE (không có khoản hoàn); NOT_REFUNDED (Chưa hoàn); REFUNDED (Đã hoàn) - ASM-29, GL-10 | DC-Ticket.getRefundStatus |
| DC-SmsStatus | enumeration | PKG-28 | NO_ISSUE (không ghi nhận lỗi); NOT_SENT (Chưa gửi được) - ASM-39 | DC-Ticket.getSmsStatus |
| DC-CancelNoticeStatus | enumeration | PKG-28 | NO_ISSUE (không ghi nhận lỗi); NOT_NOTIFIED (Chưa báo được) - ASM-42 | DC-Ticket.getCancelNoticeStatus |
| DC-RefundAttemptStatus | enumeration | PKG-28 | NO_ISSUE (không ghi nhận lỗi); FAILED (Hoàn không thành công) - ASM-33, ASM-42 | DC-Ticket.getRefundAttemptStatus |
| DC-TripCancellationSummary | value object | PKG-28 | cancelledTicketCount: int; notifiedPhoneCount: int; unnotified: Map<PhoneNumber, List<TicketCode>>; refundedTicketCount: int; refundedTotal: Money; refundFailedTicketCodes: List<TicketCode>; counterTicketsAwaitingCashRefund: int (P04 UC-017 Dữ liệu ra 4) | DC-TripTicketCancellation.summarizeTripCancellation |
| DC-BookingNotFoundException | exception | PKG-28 | Không có thành phần; ném khi không có lần đặt ứng với định danh | DC-BookTicketOnlineService.processTravelerInfo, requestCancelBooking, handleHoldExpiry |
| DC-SeatsUnavailableException | exception | PKG-28 | Không có thành phần; ném khi có chỗ không còn trống, kể cả khi thua tranh chấp giữ chỗ (BR-02, NFR-04; luồng 4a) | DC-Seat.markHeld, DC-Booking.holdSeats, DC-BookTicketOnlineService.processSeatSelection |
| DC-SeatLimitExceededException | exception | PKG-28 | Không có thành phần; ném khi số chỗ của lần đặt vượt giới hạn (BR-01; luồng 4b) | DC-BookTicketOnlineService.processSeatSelection |
| DC-TravelerInfoMissingException | exception | PKG-28 | Không có thành phần; ném khi thiếu họ tên hoặc số điện thoại người đi (luồng 7a) | DC-Booking.recordTravelerInfo, DC-BookTicketOnlineService.processTravelerInfo |
| DC-HoldExpiredException | exception | PKG-28 | Không có thành phần; ném khi thao tác tới lúc lần đặt đã hết thời hạn giữ chỗ hoặc đã trả chỗ (BR-03; luồng 5a) | DC-Booking.recordTravelerInfo, clearHoldExpiry, issueTickets, DC-BookTicketOnlineService.processTravelerInfo |

Ngoại lệ nghiệp vụ là ngoại lệ không kiểm tra (RuntimeException): Spring hoàn tác giao dịch khi ném, nên giữ chỗ thất bại không để lại Booking; ngoại lệ cần giữ lại thay đổi (trả chỗ rồi báo hết hạn hoặc thanh toán thất bại) được ném sau khi giao dịch đã commit (F3). Enumeration và ngoại lệ đặt ở package của entity sở hữu vì PKG-31 chỉ nhận kiểu giá trị (P10 F4); các kiểu dùng chung giữa PKG-13 và PKG-16 (DC-CancelReason, DC-TripDepartedException, DC-TripAlreadyCancelledException) nằm ở PKG-27, phụ thuộc PKG-16 --> PKG-27 đã có.

## F2. Bảng operation

Bảng ánh xạ kiểu từ kiểu trung lập của P07, P08, P11b sang kiểu Java 17:

| Kiểu trung lập | Kiểu thiết kế |
|---|---|
| Văn bản | String |
| Số tiền | Money (DC-Money, PKG-31); BigDecimal ở view model của Presentation |
| Ngày, Giờ | LocalDateTime (giờ xuất bến, hạn giữ chỗ); LocalDate (ngày đi) |
| Trạng thái | enumeration của F1b (UPPER_SNAKE_CASE) |
| Phần trăm | BigDecimal |
| Định danh | long (Thiết kế: mặc định của Java, C1 mục 7) |
| Số nguyên, giá trị đúng sai | int, boolean |
| Tập hợp | List<T>, Set<T>, Map<K,V> |
| Giá trị tuỳ chọn | Optional<T> cho kiểu trả về; nullable cho thuộc tính multiplicity 0..1 |
| Thời hạn, đồng hồ | Duration; java.time.Clock (đồng hồ do nền tảng cấp, không cấp IF) |
| Không trả về | void (thống nhất cả artifact) |

Visibility mặc định public cho operation có bên gọi ngoài lớp; không có operation private liệt kê vì các bước nội bộ nằm trong method (F3). Operation tạo đối tượng (createBooking, createTicket) là classifier; constructor ghi "Instance" theo quy ước Java.

| DC | Visibility | Chữ ký | Mô tả | Tiền/hậu điều kiện | Nguồn (message P07 / UC bước) | Phạm vi | Ngoại lệ / lỗi |
|---|---|---|---|---|---|---|---|
| DC-BookTicketOnlineService | + | startBookTicketOnline(tripId: long): BookTicketOnlineViewModel | Bắt đầu bước chọn chỗ cho chuyến hành khách đã chọn ở UC-008; tripId là định danh chuyến; trả view model có sơ đồ chỗ của chuyến | Tiền: chuyến tồn tại. Hậu: không đổi dữ liệu | P07 UC-009 SD1a-M02 (STT 1.1) // startBookTicketOnline | Instance | TripNotFoundException |
| DC-BookTicketOnlineService | + | processSeatSelection(tripId: long, seatCodes: Set<String>): BookTicketOnlineViewModel | Kiểm tra các chỗ đã chọn theo thứ tự ASM-23 (còn trống, số chỗ, giờ xuất bến), xác định giá vé và giữ chỗ trong một giao dịch; trả view model có mã lần đặt, các chỗ đang giữ, thời hạn giữ chỗ. seatCodes là mã chỗ hành khách chọn, từ 1 phần tử | Tiền: seatCodes khác rỗng (rỗng --> IllegalArgumentException). Hậu thành công: Booking HOLDING đã lưu, mọi Seat HELD, holdExpiry = giờ giữ + 10 phút (BR-03). Hậu thất bại: không lưu gì (giao dịch hoàn tác, BR-02, NFR-04) | P07 UC-009 SD1a-M07 (STT 2.1) // processSeatSelection | Instance | SeatsUnavailableException (4a), SeatLimitExceededException (4b), TripDepartedException (4c), TripNotFoundException, FareNotFoundException |
| DC-BookTicketOnlineService | + | processTravelerInfo(bookingId: long, travelerName: String, travelerPhone: String): BookTicketOnlineViewModel | Ghi người đi, gọi thanh toán, phát hành vé, gửi mã vé qua SMS và trả view model có các vé đã phát hành và tổng tiền. Hai tham số chuỗi là họ tên và số điện thoại người nhập (ASM-19) | Tiền: lần đặt ở HOLDING và chưa hết thời hạn giữ chỗ. Hậu thành công: Booking TICKETS_ISSUED, mỗi chỗ một Ticket ISSUED, Seat SOLD, SMS đã chuyển cho Cổng SMS hoặc vé ghi smsStatus = NOT_SENT. Hậu thất bại: các lỗi 7a giữ nguyên HOLDING; 8a và 5a trả chỗ (SEATS_RELEASED) | P07 UC-009 SD1b-M02 (STT 3.1) // processTravelerInfo | Instance | BookingNotFoundException, TravelerInfoMissingException (7a), HoldExpiredException (5a), PaymentFailedException (8a) |
| DC-BookTicketOnlineService | + | requestCancelBooking(bookingId: long): void | Huỷ yêu cầu mua vé của hành khách và trả ngay các chỗ đang giữ (ASM-24); chỉ gọi khi đã giữ chỗ | Tiền: lần đặt tồn tại. Hậu: Booking SEATS_RELEASED, Seat AVAILABLE; gọi lại khi đã trả chỗ không đổi gì | P07 UC-009 SD2-M02 (STT 2.1.10*a.1) // requestCancelBooking | Instance | BookingNotFoundException; IllegalStateException khi vé đã phát hành |
| DC-BookTicketOnlineService | + | handleHoldExpiry(bookingId: long): void | Xử lý một lần đặt tới mốc hết thời hạn giữ chỗ: trả các chỗ và yêu cầu UC-010 dừng phiên thanh toán (ASM-41); bỏ qua khi lần đặt đã xử lý | Tiền: không. Hậu: nếu Booking HOLDING và holdExpiry <= giờ hiện tại thì SEATS_RELEASED, Seat AVAILABLE; ngược lại không đổi gì (mỗi mốc xử lý một lần, P09 F7) | P07 UC-009 SD1b-M14 (STT 4) // after(BR-03) handleHoldExpiry; ST-03 sự kiện when(now >= holdExpiry) | Instance | Không (lần đặt không tồn tại cũng bỏ qua) |
| DC-BookTicketOnlineService | + | listExpiredHolds(): List<Long> | Cho bộ định thời biết các lần đặt đã tới mốc hết thời hạn giữ chỗ; trả định danh Booking | Hậu: không đổi dữ liệu; kết quả là Booking HOLDING có holdExpiry <= giờ hiện tại | Bổ sung: cơ chế quét mốc (Bước 1.6a; P09 F1 dòng 9, F7) | Instance | Không |
| DC-SearchTripsService | + | searchTrips(origin: String, destination: String, travelDate: LocalDate): List<TripOption> | Tìm các chuyến chưa xuất bến theo điểm đi, điểm đến và ngày đi (REQ-05); tạm, chờ P07 UC-008 | Tiền: origin, destination khác rỗng. Hậu: không đổi dữ liệu | P07 UC-009 SD1a-M03 (STT 1.1.1) // searchTrips (Tạm) | Instance | Không (không có chuyến --> danh sách rỗng, luồng 2a) |
| DC-SearchTripsService | + | viewSeatMap(tripId: long): BookTicketOnlineViewModel | Trả view model có sơ đồ chỗ của chuyến và chỗ nào chọn được (REQ-06); tạm, chờ P07 UC-008 | Tiền: chuyến tồn tại. Hậu: không đổi dữ liệu | Bổ sung: sơ đồ chỗ cho SCR-02 (P11a ASM-49; P07 UC-009 F2 bước 2 giao UC-008) | Instance | TripNotFoundException |
| DC-PayTicketOnlineService | + | payTicketOnline(booking: Booking, totalAmount: Money): Optional<PaymentTransaction> | Thu tiền vé của lần đặt qua Cổng thanh toán và ghi nhận giao dịch; booking là lần đặt đang giữ chỗ; totalAmount là tổng tiền cần thu (NFR-10); trả giao dịch khi thành công, rỗng khi không thành công; tạm, chờ P07 UC-010 | Tiền: booking HOLDING, totalAmount > 0. Hậu thành công: PaymentTransaction đã lưu và được trả về. Không thành công hoặc cổng không trả kết quả (ASM-37): trả rỗng, không lưu gì | P07 UC-009 SD1b-M08 (STT 3.1.4) // payTicketOnline (Tạm) | Instance | Không (thất bại trả bằng Optional rỗng) |
| DC-PayTicketOnlineService | + | cancelPayment(booking: Booking): void | Yêu cầu dừng phiên thanh toán đang chạy của lần đặt khi hết thời hạn giữ chỗ (ASM-41); tạm, chờ P07 UC-010 | Tiền: không. Hậu: nếu có phiên thanh toán thì đã yêu cầu dừng; không có phiên thì không làm gì | P07 UC-009 SD1b-M17 (STT 4.2) // cancelPayment (Tạm) | Instance | Không |
| DC-Trip | + | Trip(departureTime: LocalDateTime, route: String, vehicleType: VehicleType, vehicle: String, driver: String) | Khởi tạo chuyến ở trạng thái SCHEDULED | Hậu: status = SCHEDULED | Bổ sung: khởi tạo (UC-016 chưa có P07); ST-01 sự kiện create | Instance | IllegalArgumentException khi tham số rỗng |
| DC-Trip | + | isBeforeDeparture(now: LocalDateTime): boolean | Cho biết giờ xuất bến chưa tới; now là thời điểm hiện tại do bên gọi cấp | Hậu: true khi now < departureTime (BR-05, BR-10); không đổi trạng thái | P07 UC-009 SD1a-M13 (STT 2.1.4) và UC-017 STT 2.1.3 // checkDepartureNotReached | Instance | Không |
| DC-Trip | + | isCancelled(): boolean | Cho biết chuyến đã ở trạng thái Đã huỷ | Hậu: true khi status = CANCELLED (BR-09) | P07 UC-017 STT 2.1.1 // checkNotCancelled | Instance | Không |
| DC-Trip | + | cancel(reason: CancelReason, now: LocalDateTime): void | Chuyển chuyến sang Đã huỷ kèm lý do; reason là lý do nhân viên điều hành chọn; now để kiểm tra giờ xuất bến | Tiền: status = SCHEDULED (BR-09) và now < departureTime (BR-10); kiểm tra theo thứ tự này (ASM-26). Hậu: status = CANCELLED, cancelReason = reason | P07 UC-017 STT 2.1.5 // cancelTrip; ST-01 sự kiện cancel | Instance | TripAlreadyCancelledException (4a), TripDepartedException (4b) |
| DC-Trip | + | getId(): long | Trả định danh chuyến | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (TripOption.tripId, view model) | Instance | Không |
| DC-Trip | + | getRoute(): String | Trả tuyến xe của chuyến | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (hiển thị, Fare.determineFare, SMS huỷ chuyến); P07 UC-017 STT 2.1.5 (trả về tuyến) | Instance | Không |
| DC-Trip | + | getDepartureTime(): LocalDateTime | Trả giờ xuất bến | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (hiển thị, SMS huỷ chuyến); P07 UC-017 STT 2.1.5 (trả về giờ xuất bến) | Instance | Không |
| DC-Trip | + | getVehicleType(): VehicleType | Trả loại xe của chuyến | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (tra giá vé theo tuyến và loại xe, REQ-60) | Instance | Không |
| DC-Trip | + | getStatus(): TripStatus | Trả trạng thái chuyến | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của cancel; P07 UC-017 STT 1.1.1 (trả về trạng thái) | Instance | Không |
| DC-Trip | + | getCancelReason(): Optional<CancelReason> | Trả lý do huỷ chuyến nếu có | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của cancel | Instance | Không |
| DC-Trip | + | getVehicle(): String | Trả định danh hiển thị của xe | Hậu: không đổi trạng thái | P07 UC-017 STT 1.1.1 (trả về xe) | Instance | Không |
| DC-Trip | + | getDriver(): String | Trả họ tên tài xế | Hậu: không đổi trạng thái | P07 UC-017 STT 1.1.1 (trả về tài xế) | Instance | Không |
| DC-Fare | + | Fare(route: String, vehicleType: VehicleType, amount: Money, surchargePercent: BigDecimal) | Khởi tạo một dòng giá vé; surchargePercent có thể rỗng | Hậu: các thuộc tính cùng tên được gán | Bổ sung: khởi tạo (UC-023, UC-024 chưa có P07) | Instance | IllegalArgumentException khi amount không dương hoặc surchargePercent âm |
| DC-Fare | + | determineFare(trip: Trip): Money | Xác định giá vé của một chỗ trên chuyến: amount, cộng mức tăng giá nếu có, làm tròn về đồng (ASM-56) | Tiền: trip.route = route và trip.vehicleType = vehicleType. Hậu: không đổi trạng thái; kết quả > 0 | P07 UC-009 SD1a-M18 (STT 2.1.8) // determineFare | Instance | IllegalArgumentException khi chuyến không thuộc tuyến và loại xe của Fare |
| IF-03 | + | findById(tripId: long): Optional<Trip> | Nạp chuyến theo định danh | Hậu: không đổi dữ liệu | Bổ sung: nạp chuyến (P07 UC-009 SD1a-M13) | Instance | Không |
| IF-03 | + | findByIdForUpdate(tripId: long): Optional<Trip> | Nạp chuyến kèm khoá ghi để huỷ chuyến không trùng với giữ chỗ | Hậu: bản ghi bị khoá đến hết giao dịch | Bổ sung: nạp chuyến để huỷ (P07 UC-017 STT 2.1.1 đến 2.1.5) | Instance | Không |
| IF-03 | + | findByRouteAndDate(route: String, date: LocalDate): List<Trip> | Tìm các chuyến của tuyến có giờ xuất bến trong ngày, mọi trạng thái; route ghép từ điểm đi và điểm đến | Hậu: không đổi dữ liệu | P07 UC-009 SD1a-M03 (searchTrips, Tạm) | Instance | Không |
| IF-03 | + | findInSchedule(from: LocalDateTime): List<Trip> | Cung cấp các chuyến trong lịch chạy từ thời điểm from trở đi, gồm cả chuyến đã huỷ (ASM-55) | Hậu: không đổi dữ liệu | P07 UC-017 STT 1.1.1 // listTripsInSchedule | Instance | Không |
| IF-03 | + | save(trip: Trip): Trip | Lưu chuyến mới hoặc thay đổi của chuyến | Hậu: bản ghi phản ánh trạng thái hiện tại của trip | Bổ sung: lưu ST-01 sự kiện cancel; khởi tạo (UC-016 chờ) | Instance | Không |
| IF-04 | + | findByRouteAndVehicleType(route: String, vehicleType: VehicleType): Optional<Fare> | Tìm giá vé của cặp tuyến xe và loại xe | Hậu: không đổi dữ liệu | Bổ sung: nạp Fare cho P07 UC-009 SD1a-M18 | Instance | Không |
| IF-04 | + | save(fare: Fare): Fare | Lưu giá vé | Hậu: bản ghi phản ánh trạng thái hiện tại của fare | Bổ sung: lưu giá vé (UC-023, UC-024 chờ P07) | Instance | Không |
| DC-Seat | + | Seat(trip: Trip, seatCode: String) | Khởi tạo chỗ của chuyến ở trạng thái AVAILABLE | Hậu: tripState = AVAILABLE | Bổ sung: khởi tạo (UC-016, UC-021 chưa có P07); ST-02 sự kiện create | Instance | IllegalArgumentException khi seatCode rỗng |
| DC-Seat | + | isAvailable(): boolean | Cho biết chỗ chưa có vé và chưa bị giữ | Hậu: true khi tripState = AVAILABLE (BR-02) | P07 UC-009 SD1a-M09 (STT 2.1.2) // checkAvailable | Instance | Không |
| DC-Seat | + | markHeld(): void | Chuyển chỗ sang đang giữ; chỉ một yêu cầu giữ được chỗ | Tiền: tripState = AVAILABLE. Hậu: tripState = HELD (NFR-04, BR-02) | P07 UC-009 SD1a-M21 (STT 2.1.9.1) // markHeld; ST-02 sự kiện markHeld | Instance | SeatsUnavailableException khi chỗ không AVAILABLE |
| DC-Seat | + | markSold(): void | Chuyển chỗ sang đã bán khi vé được phát hành | Tiền: tripState = HELD. Hậu: tripState = SOLD | P07 UC-009 SD1c-M04 (STT 3.1.8.2) // markSold; ST-02 sự kiện markSold | Instance | IllegalStateException khi chỗ không HELD |
| DC-Seat | + | markAvailable(): void | Trả chỗ đang giữ về trạng thái trống | Tiền: tripState = HELD. Hậu: tripState = AVAILABLE | P07 UC-009 SD1b-M12, SD1b-M16, SD2-M05 // markAvailable; ST-02 sự kiện markAvailable | Instance | IllegalStateException khi chỗ không HELD |
| DC-Seat | + | getSeatCode(): String | Trả mã chỗ | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model, tìm chỗ theo mã) | Instance | Không |
| DC-Seat | + | getTripState(): SeatState | Trả trạng thái bán của chỗ | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của markHeld, markSold, markAvailable | Instance | Không |
| DC-Seat | + | getTrip(): Trip | Trả chuyến của chỗ | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (Booking.createBooking, Ticket.createTicket kiểm tra chỗ thuộc chuyến) | Instance | Không |
| DC-Booking | + | createBooking(trip: Trip, seats: List<Seat>): Booking | Tạo lần đặt ở trạng thái SELECTING cho chuyến và các chỗ đã chọn; chưa lưu | Tiền: seats khác rỗng và mọi chỗ thuộc trip. Hậu: status = SELECTING | P07 UC-009 SD1a-M08 (STT 2.1.1) «create» // createBooking; ST-03 sự kiện create | Classifier | IllegalArgumentException khi seats rỗng hoặc có chỗ không thuộc trip |
| DC-Booking | + | isSeatCountWithinLimit(): boolean | Cho biết số chỗ của lần đặt không quá giới hạn | Hậu: true khi số chỗ <= MAX_SEATS (BR-01) | P07 UC-009 SD1a-M11 (STT 2.1.3) // checkSeatCountWithinLimit | Instance | Không |
| DC-Booking | + | holdSeats(seatFare: Money, now: LocalDateTime): void | Giữ các chỗ, ghi giá vé mỗi chỗ, đặt thời điểm giữ và thời hạn giữ chỗ; seatFare là giá đã xác định ở bước 5 (ASM-40) | Tiền: status = SELECTING, số chỗ <= MAX_SEATS. Hậu: status = HOLDING; mọi Seat HELD; holdStartedAt = now; holdExpiry = now + HOLD_DURATION (BR-03); seatFare đã ghi | P07 UC-009 SD1a-M20 (STT 2.1.9) // holdSeats; ST-03 sự kiện holdSeats | Instance | SeatsUnavailableException khi có chỗ không còn trống; IllegalStateException khi status khác SELECTING |
| DC-Booking | + | recordTravelerInfo(travelerName: String, travelerPhone: String, now: LocalDateTime): void | Ghi họ tên, số điện thoại người đi và kiểm tra cả hai đã được cung cấp; điều kiện hợp lệ khác chưa quy định (Q-44) | Tiền: status = HOLDING và chưa tới holdExpiry. Hậu: travelerName, travelerPhone đã ghi | P07 UC-009 SD1b-M03 (STT 3.1.1) // recordTravelerInfo; ST-03 sự kiện recordTravelerInfo | Instance | TravelerInfoMissingException (7a), HoldExpiredException (5a), IllegalStateException |
| DC-Booking | + | calculateTotalAmount(): Money | Tính tổng tiền bằng giá vé một chỗ nhân số chỗ | Tiền: status = HOLDING. Hậu: không đổi trạng thái; kết quả = seatFare x số chỗ | P07 UC-009 SD1b-M06 (STT 3.1.3) // calculateTotalAmount | Instance | IllegalStateException khi chưa ghi seatFare |
| DC-Booking | + | clearHoldExpiry(): void | Dừng chờ thời hạn giữ chỗ khi đã có kết quả thanh toán thành công | Tiền: status = HOLDING. Hậu: holdExpiry rỗng nên bộ định thời không còn thấy lần đặt này | P07 UC-009 SD1b-M10 (STT 3.1.5) // stopWaitingForPaymentResult; P10 F3; ST-03 sự kiện clearHoldExpiry | Instance | HoldExpiredException khi đã SEATS_RELEASED; IllegalStateException |
| DC-Booking | + | isHoldExpired(now: LocalDateTime): boolean | Cho biết đã tới thời hạn giữ chỗ | Hậu: true khi holdExpiry có giá trị và now >= holdExpiry (BR-03) | Bổ sung: quan sát hậu điều kiện (Bước 2.4); dùng ở Booking.recordTravelerInfo và DC-BookTicketOnlineService.processTravelerInfo | Instance | Không |
| DC-Booking | + | releaseHeldSeats(): void | Trả các chỗ đang giữ cho người khác và xoá thời hạn giữ chỗ; dùng cho thanh toán thất bại, hết thời hạn, hành khách huỷ (cùng ý nghĩa, ASM-24) | Tiền: status = HOLDING hoặc SEATS_RELEASED. Hậu: status = SEATS_RELEASED; mọi Seat AVAILABLE; holdExpiry rỗng | P07 UC-009 SD1b-M11, SD1b-M15, SD2-M04 // releaseHeldSeats; SD2-M03 // stopWaitingForPaymentResult (gộp); ST-03 sự kiện releaseHeldSeats | Instance | IllegalStateException khi status là SELECTING hoặc TICKETS_ISSUED |
| DC-Booking | + | issueTickets(ticketCodes: List<TicketCode>, transaction: PaymentTransaction): List<Ticket> | Phát hành mỗi chỗ đang giữ một vé kênh trực tuyến, đã thanh toán, mang mã vé riêng và giao dịch thanh toán; ticketCodes là các mã vé đã cấp, đủ số chỗ; chuyển các chỗ sang đã bán | Tiền: status = HOLDING; ticketCodes có số phần tử bằng số chỗ (BR-04). Hậu: status = TICKETS_ISSUED; mọi Seat SOLD; holdExpiry rỗng; kết quả là các Ticket ISSUED, mỗi vé có fare = seatFare | P07 UC-009 SD1c-M01 (STT 3.1.8) // issueTickets; ST-03 sự kiện issueTickets | Instance | HoldExpiredException khi đã SEATS_RELEASED; IllegalArgumentException khi số mã vé khác số chỗ; IllegalStateException |
| DC-Booking | + | getId(): long | Trả định danh lần đặt | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model) | Instance | Không |
| DC-Booking | + | getStatus(): BookingStatus | Trả trạng thái lần đặt | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của sự kiện ST-03 | Instance | Không |
| DC-Booking | + | getTrip(): Trip | Trả chuyến của lần đặt | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model, tạo vé) | Instance | Không |
| DC-Booking | + | getSeats(): List<Seat> | Trả các chỗ của lần đặt | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model, lưu chỗ) | Instance | Không |
| DC-Booking | + | getTravelerName(): Optional<String> | Trả họ tên người đi nếu đã ghi | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model SCR-04) | Instance | Không |
| DC-Booking | + | getTravelerPhone(): Optional<PhoneNumber> | Trả số điện thoại người đi nếu đã ghi | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (gửi SMS mã vé) | Instance | Không |
| DC-Booking | + | getHoldExpiry(): Optional<LocalDateTime> | Trả thời hạn giữ chỗ nếu còn chờ | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model SCR-03) | Instance | Không |
| DC-Booking | + | getSeatFare(): Optional<Money> | Trả giá vé một chỗ đã ghi | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của holdSeats | Instance | Không |
| DC-Ticket | + | createTicket(trip: Trip, seat: Seat, travelerName: String, travelerPhone: PhoneNumber, fare: Money, ticketCode: TicketCode, transaction: PaymentTransaction): Ticket | Khởi tạo vé kênh trực tuyến, đã thanh toán, gắn chuyến, chỗ, người đi, giá vé, mã vé và giao dịch thu tiền | Tiền: seat thuộc trip. Hậu: status = ISSUED; purchaseChannel = ONLINE; paymentStatus = PAID; refundStatus = NOT_APPLICABLE | P07 UC-009 SD1c-M02 (STT 3.1.8.1) «create» // createTicket; ST-04 sự kiện create | Classifier | IllegalArgumentException khi seat không thuộc trip |
| DC-Ticket | + | recordSmsNotSent(): void | Ghi nhận mã vé chưa gửi được qua SMS; vé giữ nguyên (ASM-20, ASM-39) | Hậu: smsStatus = NOT_SENT; các thuộc tính khác không đổi | P07 UC-009 SD1c-M10 (STT 3.1.10) // recordSmsNotSent | Instance | Không |
| DC-Ticket | + | cancelForTrip(): void | Chuyển vé đang có hiệu lực sang Đã huỷ khi chuyến bị huỷ; vé đã thanh toán có thêm hoàn tiền Chưa hoàn (ASM-29) | Tiền: status = ISSUED. Hậu: status = CANCELLED; refundStatus = NOT_REFUNDED khi paymentStatus = PAID, ngược lại giữ NOT_APPLICABLE | P07 UC-017 STT 2.1.8 // cancelTicketsOfTrip (phần của một vé); ST-04 sự kiện cancelForTrip | Instance | IllegalStateException khi vé không ISSUED |
| DC-Ticket | + | isActive(): boolean | Cho biết vé đang có hiệu lực (GL-25) | Hậu: true khi status = ISSUED | Bổ sung: bên gọi cần (kiểm tra tiền điều kiện của cancelForTrip) | Instance | Không |
| DC-Ticket | + | isOnlineRefundPending(): boolean | Cho biết vé mua trực tuyến, đã thanh toán, đã huỷ và còn Chưa hoàn | Hậu: true khi purchaseChannel = ONLINE, paymentStatus = PAID, status = CANCELLED, refundStatus = NOT_REFUNDED (BR-08) | P07 UC-017 STT 2.1.12 // selectOnlineTicketsToRefund (phần của một vé) | Instance | Không |
| DC-Ticket | + | calculateRefundAmount(): Money | Tính số tiền hoàn bằng 100% giá vé đã ghi của vé | Tiền: isOnlineRefundPending. Hậu: không đổi trạng thái; kết quả = fare (BR-07, không vượt số đã thu, NFR-06) | P07 UC-017 STT 2.1.13 // calculateRefundAmount | Instance | IllegalStateException khi vé không cần hoàn tiền |
| DC-Ticket | + | markRefunded(): void | Ghi nhận Cổng thanh toán đã hoàn tiền vé | Tiền: refundStatus = NOT_REFUNDED. Hậu: refundStatus = REFUNDED; refundAttemptStatus = NO_ISSUE (NFR-05: không hoàn lại) | P07 UC-017 STT 2.1.15 // markRefunded; ST-04 sự kiện markRefunded | Instance | IllegalStateException khi refundStatus khác NOT_REFUNDED |
| DC-Ticket | + | recordRefundNotCompleted(): void | Giữ hoàn tiền Chưa hoàn và ghi nhận lần hoàn không thành công (ASM-33) | Tiền: refundStatus = NOT_REFUNDED. Hậu: refundAttemptStatus = FAILED; refundStatus giữ NOT_REFUNDED | P07 UC-017 STT 2.1.17 // recordRefundNotCompleted; ST-04 sự kiện recordRefundNotCompleted | Instance | IllegalStateException khi refundStatus khác NOT_REFUNDED |
| DC-Ticket | + | markCancelNoticeNotSent(): void | Ghi nhận vé chưa được báo huỷ chuyến qua SMS (ASM-31, ASM-42) | Tiền: status = CANCELLED. Hậu: cancelNoticeStatus = NOT_NOTIFIED | P07 UC-017 STT 2.1.11 // recordCancelNoticeNotSent (phần của một vé) | Instance | IllegalStateException khi vé không CANCELLED |
| DC-Ticket | + | getTicketCode(): TicketCode | Trả mã vé | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model, SMS, hoàn tiền) | Instance | Không |
| DC-Ticket | + | getSeat(): Seat | Trả chỗ của vé | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model) | Instance | Không |
| DC-Ticket | + | getTravelerName(): String | Trả họ tên người đi | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model) | Instance | Không |
| DC-Ticket | + | getTravelerPhone(): PhoneNumber | Trả số điện thoại người đi | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (gom SMS huỷ chuyến, UC-017) | Instance | Không |
| DC-Ticket | + | getFare(): Money | Trả giá vé đã ghi | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (view model, tổng tiền hoàn) | Instance | Không |
| DC-Ticket | + | getStatus(): TicketStatus | Trả trạng thái vé | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của cancelForTrip | Instance | Không |
| DC-Ticket | + | getRefundStatus(): RefundStatus | Trả trạng thái hoàn tiền | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của cancelForTrip, markRefunded | Instance | Không |
| DC-Ticket | + | getPaymentTransaction(): Optional<PaymentTransaction> | Trả giao dịch thu tiền của vé nếu có | Hậu: không đổi trạng thái | P07 UC-017 STT 2.1.12 (trả về giao dịch thanh toán); R-20 | Instance | Không |
| DC-Ticket | + | getSmsStatus(): SmsStatus | Trả ghi nhận gửi SMS mã vé | Hậu: không đổi trạng thái | Bổ sung: quan sát hậu điều kiện của recordSmsNotSent | Instance | Không |
| DC-Ticket | + | getCancelNoticeStatus(): CancelNoticeStatus | Trả ghi nhận báo huỷ chuyến | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (tổng hợp kết quả huỷ chuyến) | Instance | Không |
| DC-Ticket | + | getRefundAttemptStatus(): RefundAttemptStatus | Trả ghi nhận lần hoàn tiền gần nhất | Hậu: không đổi trạng thái | Bổ sung: bên gọi cần (tổng hợp kết quả huỷ chuyến) | Instance | Không |
| DC-TripTicketCancellation | + | cancelTicketsOfTrip(trip: Trip): List<Ticket> | Chuyển mọi vé đang có hiệu lực của chuyến sang Đã huỷ và trả các vé vừa huỷ; trip là chuyến đã chuyển sang Đã huỷ | Tiền: trip.isCancelled(). Hậu: mọi vé ISSUED của trip thành CANCELLED và đã lưu; vé đã thanh toán có refundStatus = NOT_REFUNDED (ASM-29) | P07 UC-017 STT 2.1.8 // cancelTicketsOfTrip (tách từ AC-E-Ticket) | Instance | IllegalStateException khi chuyến chưa huỷ |
| DC-TripTicketCancellation | + | groupTicketCodesByTravelerPhone(tickets: List<Ticket>): Map<PhoneNumber, List<Ticket>> | Gom các vé theo số điện thoại người đi để mỗi số nhận một SMS (ASM-30); tickets là các vé đã huỷ | Hậu: không đổi dữ liệu; mỗi vé thuộc đúng một nhóm; khoá gom theo PhoneNumber (BR-04) | P07 UC-017 STT 2.1.9 // groupTicketCodesByTravelerPhone (tách từ AC-E-Ticket) | Instance | Không |
| DC-TripTicketCancellation | + | recordCancelNoticeNotSent(tickets: List<Ticket>): void | Ghi nhận các vé của một số điện thoại chưa được báo huỷ chuyến qua SMS; tickets là nhóm vé của số đó | Hậu: mỗi vé trong tickets có cancelNoticeStatus = NOT_NOTIFIED và đã lưu | P07 UC-017 STT 2.1.11 // recordCancelNoticeNotSent (tách từ AC-E-Ticket) | Instance | Không |
| DC-TripTicketCancellation | + | selectOnlineTicketsToRefund(tickets: List<Ticket>): List<Ticket> | Chọn trong các vé đã huỷ các vé mua trực tuyến đã thanh toán còn Chưa hoàn | Hậu: không đổi dữ liệu; kết quả là các vé có isOnlineRefundPending (BR-08) | P07 UC-017 STT 2.1.12 // selectOnlineTicketsToRefund (tách từ AC-E-Ticket) | Instance | Không |
| DC-TripTicketCancellation | + | summarizeTripCancellation(tickets: List<Ticket>): TripCancellationSummary | Tổng hợp kết quả huỷ chuyến từ các vé đã huỷ để hiển thị ở bước 14 | Tiền: các vé đã qua bước báo SMS và hoàn tiền. Hậu: không đổi dữ liệu; số liệu theo P04 UC-017 Dữ liệu ra 4 | P07 UC-017 STT 2.1.18 // summarizeTripCancellation (tách từ AC-E-Ticket) | Instance | Không |
| IF-05 | + | findByTripAndSeatCodesForUpdate(trip: Trip, seatCodes: Set<String>): List<Seat> | Nạp các chỗ của chuyến theo mã kèm khoá ghi, sắp theo mã chỗ tăng dần để hai yêu cầu cùng chỗ nối đuôi nhau và không khoá chéo | Hậu: kết quả có thể ít hơn seatCodes khi có mã không tồn tại; bản ghi bị khoá đến hết giao dịch (NFR-04) | Bổ sung: nạp chỗ để P07 UC-009 SD1a-M09, SD1a-M21 (NFR-04) | Instance | Không |
| IF-05 | + | findByTrip(trip: Trip): List<Seat> | Nạp mọi chỗ của chuyến cho sơ đồ chỗ | Hậu: không đổi dữ liệu | Bổ sung: sơ đồ chỗ (DC-SearchTripsService.viewSeatMap) | Instance | Không |
| IF-05 | + | saveAll(seats: List<Seat>): void | Lưu thay đổi trạng thái của các chỗ | Hậu: bản ghi phản ánh trạng thái hiện tại | Bổ sung: lưu ST-02 sự kiện markHeld, markSold, markAvailable | Instance | Không |
| IF-06 | + | findById(bookingId: long): Optional<Booking> | Nạp lần đặt theo định danh | Hậu: không đổi dữ liệu | Bổ sung: nạp lần đặt để đọc | Instance | Không |
| IF-06 | + | findByIdForUpdate(bookingId: long): Optional<Booking> | Nạp lần đặt kèm khoá ghi để thanh toán, huỷ và hết hạn không xử lý chồng nhau | Hậu: bản ghi bị khoá đến hết giao dịch | Bổ sung: nạp lần đặt để đổi trạng thái (P09 F7: mỗi mốc xử lý một lần) | Instance | Không |
| IF-06 | + | findIdsHoldExpiredAt(now: LocalDateTime): List<Long> | Tìm định danh các lần đặt HOLDING có holdExpiry <= now | Hậu: không đổi dữ liệu | Bổ sung: cơ chế quét mốc (Bước 1.6a; DC-BookTicketOnlineService.listExpiredHolds) | Instance | Không |
| IF-06 | + | save(booking: Booking): Booking | Lưu lần đặt, kèm liên kết tới chỗ và vé | Hậu: bản ghi phản ánh trạng thái hiện tại | Bổ sung: lưu ST-03 mọi sự kiện đổi dữ liệu | Instance | Không |
| IF-07 | + | nextTicketCodes(count: int): List<TicketCode> | Cấp count mã vé kế tiếp, duy nhất trên mọi vé của mọi chuyến (BR-04) | Hậu: các mã chưa từng cấp; dạng SV + số thứ tự đệm 0 tới 4 chữ số, mở rộng khi vượt (GL-15 ví dụ SV0001) | P07 UC-009 SD1c-M03 (STT 3.1.8.1.1) // generateTicketCode (P07 F4 giao P12 chọn phạm vi duy nhất) | Instance | Không |
| IF-07 | + | saveAll(tickets: List<Ticket>): void | Lưu vé mới hoặc thay đổi của vé | Hậu: bản ghi phản ánh trạng thái hiện tại | Bổ sung: lưu ST-04 mọi sự kiện đổi dữ liệu | Instance | Không |
| IF-07 | + | findActiveByTrip(trip: Trip): List<Ticket> | Tìm các vé đang có hiệu lực của chuyến (chưa huỷ, chưa trả, chưa đổi, GL-25) | Hậu: không đổi dữ liệu | P07 UC-017 STT 2.1.8 (cancelTicketsOfTrip cần tập vé của chuyến) | Instance | Không |

## F3. Bảng thiết kế method

Chỉ liệt kê operation có thuật toán hoặc quy tắc không hiển nhiên; getter, constructor, save, saveAll, findById không có dòng. Mọi chữ ký tham chiếu theo dạng DC.operation(kiểu tham số).

| DC.operation | Thuật toán / các bước chính | Đối tượng và operation khác được dùng | Cách dùng thuộc tính, tham số, quan hệ | Hành vi theo trạng thái (nếu có ST) |
|---|---|---|---|---|
| DC-BookTicketOnlineService.startBookTicketOnline(long) | 1. Gọi searchTripsService.viewSeatMap(tripId). 2. Trả view model đó. | DC-SearchTripsService.viewSeatMap | tripId chuyền nguyên; không có giao dịch ghi (chỉ đọc) | Không có ST |
| DC-BookTicketOnlineService.processSeatSelection(long, Set<String>) | Giao dịch T1 bao trọn các bước, mọi ngoại lệ làm hoàn tác (Thiết kế: một thao tác một giao dịch, P09 F7).<br>1. seatCodes rỗng --> IllegalArgumentException.<br>2. trip = tripRepository.findById(tripId) hoặc TripNotFoundException.<br>3. seats = seatRepository.findByTripAndSeatCodesForUpdate(trip, seatCodes). Có mã không tìm thấy hoặc có seat không isAvailable() --> SeatsUnavailableException (4a, BR-02).<br>4. booking = Booking.createBooking(trip, seats). Không isSeatCountWithinLimit() --> SeatLimitExceededException (4b, BR-01).<br>5. now = LocalDateTime.now(clock). Không trip.isBeforeDeparture(now) --> TripDepartedException (4c, BR-05). Thứ tự bước 3 đến 5 theo ASM-23.<br>6. fare = fareRepository.findByRouteAndVehicleType(trip.getRoute(), trip.getVehicleType()) hoặc FareNotFoundException; seatFare = fare.determineFare(trip).<br>7. booking.holdSeats(seatFare, now); seatRepository.saveAll(seats); bookingRepository.save(booking). Lưu holdExpiry cùng Booking chính là việc bắt đầu chờ thời hạn giữ chỗ (P10 F3).<br>8. Trả view model: bookingId, chuyến, selectedSeats theo mã tăng dần, holdExpiry. | IF-03.findById, IF-05.findByTripAndSeatCodesForUpdate, DC-Booking.createBooking, isSeatCountWithinLimit, holdSeats, DC-Trip.isBeforeDeparture, IF-04.findByRouteAndVehicleType, DC-Fare.determineFare, IF-05.saveAll, IF-06.save | Dùng clock (R-39) cho now. Khoá ghi ở bước 3 làm hai yêu cầu cùng chỗ nối đuôi nhau; yêu cầu sau thấy seat HELD và nhận 4a, thoả NFR-04. Booking SELECTING chỉ sống trong giao dịch, không lưu (P07 Vấn đề còn mở dòng 6) | Seat: AVAILABLE --> HELD (ST-02). Booking: (initial) --> SELECTING --> HOLDING (ST-03) |
| DC-BookTicketOnlineService.processTravelerInfo(long, String, String) | Ba giao dịch ngắn, lời gọi hệ thống ngoài nằm giữa các giao dịch (Thiết kế: không giữ khoá cơ sở dữ liệu lúc gọi cổng, P09 F7).<br>Giao dịch T1: 1. booking = bookingRepository.findByIdForUpdate(bookingId) hoặc BookingNotFoundException. 2. now = LocalDateTime.now(clock). Nếu booking.isHoldExpired(now) thì booking.releaseHeldSeats(), lưu, và ném HoldExpiredException (5a) sau khi T1 đã commit (ném bên trong giao dịch làm hoàn tác việc trả chỗ). 3. booking.recordTravelerInfo(travelerName, travelerPhone, now) (7a nếu thiếu). 4. total = booking.calculateTotalAmount(). 5. Lưu booking.<br>Ngoài giao dịch: 6. payment = payTicketOnlineService.payTicketOnline(booking, total).<br>Giao dịch T2: 7. Nạp lại booking bằng findByIdForUpdate. Nếu payment rỗng (8a): booking.releaseHeldSeats(), lưu, ném PaymentFailedException sau khi T2 đã commit. 8. Nếu payment có giá trị: booking.clearHoldExpiry() (đã SEATS_RELEASED do hết hạn lúc đang thanh toán --> HoldExpiredException, 5a; khoản thu đến muộn xử lý theo BR-06 ở UC-010). 9. codes = ticketRepository.nextTicketCodes(số chỗ); tickets = booking.issueTickets(codes, payment.get()). 10. ticketRepository.saveAll(tickets); seatRepository.saveAll(booking.getSeats()); bookingRepository.save(booking).<br>Ngoài giao dịch: 11. result = smsGateway.sendTicketCodes(booking.getTravelerPhone(), mã các vé). 12. Nếu result.status = NotSent (11a): Giao dịch T3 gọi ticket.recordSmsNotSent() cho từng vé, ticketRepository.saveAll.<br>13. Trả view model: các vé (mã vé, chỗ, giá), tổng tiền, họ tên người đi (bước 12 hiển thị mã vé kể cả khi SMS lỗi, ASM-20). | IF-06.findByIdForUpdate, DC-Booking.isHoldExpired, releaseHeldSeats, recordTravelerInfo, calculateTotalAmount, clearHoldExpiry, issueTickets, DC-PayTicketOnlineService.payTicketOnline, IF-07.nextTicketCodes, IF-07.saveAll, IF-05.saveAll, IF-06.save, IF-02.sendTicketCodes, DC-Ticket.recordSmsNotSent | Booking được nạp lại ở T2 vì có thể bị bộ định thời xử lý trong lúc chờ thanh toán. SMS gửi sau khi vé đã lưu nên lỗi gửi không đảo ngược vé (NFR-12). Lỗi hệ thống bất ngờ ném tiếp, Presentation hiển thị MSG-14 | Booking: HOLDING --> HOLDING (recordTravelerInfo, clearHoldExpiry) --> TICKETS_ISSUED; hoặc HOLDING --> SEATS_RELEASED (8a, 5a). Seat: HELD --> SOLD hoặc HELD --> AVAILABLE |
| DC-BookTicketOnlineService.requestCancelBooking(long) | Giao dịch T1: 1. booking = bookingRepository.findByIdForUpdate(bookingId) hoặc BookingNotFoundException. 2. booking.releaseHeldSeats(). 3. seatRepository.saveAll(booking.getSeats()); bookingRepository.save(booking). | IF-06.findByIdForUpdate, DC-Booking.releaseHeldSeats, IF-05.saveAll, IF-06.save | releaseHeldSeats đã xoá holdExpiry nên message stopWaitingForPaymentResult của luồng *a được gộp vào đây | Booking: HOLDING --> SEATS_RELEASED; đã SEATS_RELEASED --> bỏ qua; TICKETS_ISSUED --> IllegalStateException |
| DC-BookTicketOnlineService.handleHoldExpiry(long) | Giao dịch T1: 1. booking = bookingRepository.findByIdForUpdate(bookingId); không có thì kết thúc. 2. now = LocalDateTime.now(clock). Nếu booking.getStatus() khác HOLDING hoặc không booking.isHoldExpired(now) thì kết thúc (lần đặt đã xử lý hoặc chưa tới mốc). 3. booking.releaseHeldSeats(); seatRepository.saveAll(booking.getSeats()); bookingRepository.save(booking).<br>Sau T1: 4. payTicketOnlineService.cancelPayment(booking) (ASM-41; ngoài giao dịch vì gọi hệ thống ngoài). | IF-06.findByIdForUpdate, DC-Booking.getStatus, isHoldExpired, releaseHeldSeats, IF-05.saveAll, IF-06.save, DC-PayTicketOnlineService.cancelPayment | Guard ở bước 2 thay cho việc huỷ mốc: mốc tới lúc lần đặt đã đổi trạng thái (thanh toán xong, hành khách huỷ, bản sao khác đã xử lý) thì bỏ qua (Bước 1.6a, P09 F7). Thông báo hết hạn cho hành khách đến ở yêu cầu kế tiếp của họ qua HoldExpiredException (F4b) | Booking: HOLDING --> SEATS_RELEASED khi now >= holdExpiry (ST-03 sự kiện thời gian) |
| DC-BookTicketOnlineService.listExpiredHolds() | 1. Trả bookingRepository.findIdsHoldExpiredAt(LocalDateTime.now(clock)). | IF-06.findIdsHoldExpiredAt | Bộ định thời PKG-11 gọi chu kỳ 30 giây (Thiết kế: nhỏ hơn đơn vị phút của mốc, P09 F1 dòng 9) rồi gọi handleHoldExpiry cho từng định danh; mỗi lần gọi một giao dịch riêng để lỗi một lần đặt không chặn các lần khác | Không có ST |
| DC-SearchTripsService.searchTrips(String, String, LocalDate) | 1. route = origin + " - " + destination (Thiết kế tạm: định dạng "Điểm đi - Điểm đến" của P04 UC-009 Dữ liệu ra 1, vì Tuyến xe chưa có lớp). 2. trips = tripRepository.findByRouteAndDate(route, travelDate). 3. Giữ chuyến không isCancelled() và isBeforeDeparture(LocalDateTime.now(clock)). 4. Đổi mỗi chuyến thành TripOption(tripId, route, departureTime, vehicleType.name()). 5. Sắp theo giờ xuất bến tăng dần. | IF-03.findByRouteAndDate, DC-Trip.isCancelled, isBeforeDeparture, getId, getRoute, getDepartureTime, getVehicleType | Chỉ đọc; nhiều bản sao dùng chung kho (NFR-08, bộ nhớ đệm nếu thêm không được làm sai NFR-04, P09 F1 dòng 5) | Không có ST |
| DC-SearchTripsService.viewSeatMap(long) | 1. trip = tripRepository.findById(tripId) hoặc TripNotFoundException. 2. seats = seatRepository.findByTrip(trip). 3. seatMap = mỗi seat thành SeatCell(seat.getSeatCode(), seat.isAvailable()), sắp theo mã chỗ. 4. Trả view model có bookingId rỗng, tripId, route, departureTime, seatMap, các danh sách khác rỗng. | IF-03.findById, IF-05.findByTrip, DC-Seat.getSeatCode, isAvailable | Chỉ đọc. Bố cục lưới (hàng, cột) thuộc UC-021 chưa phân tích, view model chỉ có danh sách chỗ | Không có ST |
| DC-PayTicketOnlineService.payTicketOnline(Booking, Money) | 1. result = paymentGateway.collectPayment(totalAmount, mã lần đặt) (chữ ký tạm). 2. Nếu Collected: transaction = PaymentTransaction.collected(result.transactionCode, totalAmount); paymentTransactionRepository.save(transaction); trả Optional.of(transaction). 3. Ngược lại hoặc cổng không trả kết quả (ASM-37): trả Optional.empty(). | IF-01.collectPayment (tạm), DC-PaymentTransaction.collected (tạm), IF-08.save (tạm) | Không giữ giao dịch cơ sở dữ liệu lúc gọi cổng; lưu giao dịch trong một giao dịch ngắn sau khi có kết quả. Không ghi dữ liệu thẻ (NFR-01). Hoàn thiện khi có P07 của UC-010 | Không có ST |
| DC-PayTicketOnlineService.cancelPayment(Booking) | 1. Gọi paymentGateway.cancelPaymentSession(mã lần đặt). 2. Không làm gì nếu không có phiên. | IF-01.cancelPaymentSession (tạm) | Giao dịch thành công đến sau khi phiên bị dừng xử lý theo BR-06 ở UC-010 | Không có ST |
| DC-Trip.cancel(CancelReason, LocalDateTime) | 1. Nếu status = CANCELLED --> TripAlreadyCancelledException (BR-09). 2. Nếu now >= departureTime --> TripDepartedException (BR-10). 3. status = CANCELLED; cancelReason = reason. | - | Thứ tự kiểm tra 1 rồi 2 theo ASM-26; CancelTripService đã gọi isCancelled, isBeforeDeparture trước để thông báo đúng luồng 4a, 4b, cancel kiểm tra lại để không phụ thuộc bên gọi | Scheduled --> Cancelled; ở Cancelled hoặc quá giờ xuất bến thì từ chối (F6.2, ST-01) |
| DC-Fare.determineFare(Trip) | 1. Nếu trip.getRoute() khác route hoặc trip.getVehicleType() khác vehicleType --> IllegalArgumentException. 2. Nếu surchargePercent rỗng: trả amount. 3. Ngược lại: trả amount.scaleBy(1 + surchargePercent / 100) làm tròn HALF_UP về đồng (ASM-56). | DC-Money.scaleBy (tạm), DC-Trip.getRoute, getVehicleType | Dùng amount, surchargePercent của chính Fare; thời điểm xác định giá theo ASM-40 (một lần lúc giữ chỗ) | Không có ST |
| DC-Booking.createBooking(Trip, List<Seat>) | 1. seats rỗng hoặc có seat.getTrip() khác trip --> IllegalArgumentException. 2. Tạo Booking với status SELECTING, trip, bản sao danh sách seats sắp theo mã chỗ; chưa gán thời điểm, người đi, giá. | DC-Seat.getTrip, getSeatCode | R-12, R-10 | Khởi đầu ST-03: (initial) --> SELECTING |
| DC-Booking.holdSeats(Money, LocalDateTime) | 1. status khác SELECTING --> IllegalStateException. 2. Với mỗi seat theo mã chỗ tăng dần: seat.markHeld(). 3. holdStartedAt = now; holdExpiry = now.plus(HOLD_DURATION); seatFare = seatFare; status = HOLDING. | DC-Seat.markHeld | HOLD_DURATION (BR-03), R-10 | Chỉ SELECTING --> HOLDING; seat không AVAILABLE thì SeatsUnavailableException làm giao dịch hoàn tác |
| DC-Booking.recordTravelerInfo(String, String, LocalDateTime) | 1. status = SEATS_RELEASED --> HoldExpiredException; status khác HOLDING --> IllegalStateException. 2. isHoldExpired(now) --> HoldExpiredException (5a). 3. travelerName rỗng sau cắt khoảng trắng, hoặc travelerPhone rỗng sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang --> TravelerInfoMissingException (7a). 4. Gán travelerName đã cắt khoảng trắng; travelerPhone = PhoneNumber.of(chuỗi đã chuẩn hoá). | DC-PhoneNumber.of (tạm), isHoldExpired | Chuẩn hoá số theo SCR-03; điều kiện hợp lệ khác chưa kiểm tra (Q-44) | Chỉ HOLDING --> HOLDING (tự chuyển) |
| DC-Booking.calculateTotalAmount() | 1. seatFare rỗng --> IllegalStateException. 2. Trả seatFare.multiply(số chỗ). | DC-Money.multiply (tạm) | Dùng seatFare đã ghi (ASM-40) nên không đổi khi giá vé đổi giữa chừng | Không đổi trạng thái |
| DC-Booking.clearHoldExpiry() | 1. status = SEATS_RELEASED --> HoldExpiredException; status khác HOLDING --> IllegalStateException. 2. holdExpiry = rỗng. | - | Sau bước này bộ định thời không tìm thấy lần đặt qua IF-06.findIdsHoldExpiredAt | Chỉ HOLDING --> HOLDING (tự chuyển) |
| DC-Booking.releaseHeldSeats() | 1. status = SEATS_RELEASED: kết thúc, không làm gì. 2. status khác HOLDING --> IllegalStateException. 3. Với mỗi seat: seat.markAvailable(). 4. status = SEATS_RELEASED; holdExpiry = rỗng. | DC-Seat.markAvailable | Một operation cho ba nguyên nhân (thanh toán không thành công, hết hạn, hành khách huỷ) vì hành vi giống nhau (ASM-24); không dùng tham số cờ | HOLDING --> SEATS_RELEASED; SEATS_RELEASED --> bỏ qua |
| DC-Booking.issueTickets(List<TicketCode>, PaymentTransaction) | 1. status = SEATS_RELEASED --> HoldExpiredException; status khác HOLDING --> IllegalStateException. 2. ticketCodes.size() khác số chỗ --> IllegalArgumentException. 3. Với chỗ thứ i theo mã tăng dần: ticket = Ticket.createTicket(trip, seat, travelerName, travelerPhone, seatFare, ticketCodes[i], transaction); seat.markSold(). 4. status = TICKETS_ISSUED; holdExpiry = rỗng. 5. Trả các vé. | DC-Ticket.createTicket, DC-Seat.markSold | Mã vé tăng theo mã chỗ nên vé của A05 có mã nhỏ hơn A06 (P04 UC-009 Dữ liệu ra 1 ví dụ); R-11, R-10, R-36 | HOLDING --> TICKETS_ISSUED |
| DC-Ticket.createTicket(Trip, Seat, String, PhoneNumber, Money, TicketCode, PaymentTransaction) | 1. seat.getTrip() khác trip --> IllegalArgumentException. 2. Tạo Ticket với status ISSUED, purchaseChannel ONLINE, paymentStatus PAID, refundStatus NOT_APPLICABLE, ba cờ ghi nhận NO_ISSUE. | DC-Seat.getTrip | R-19, R-22, R-20 | Khởi đầu ST-04: (initial) --> Issued |
| DC-Ticket.cancelForTrip() | 1. status khác ISSUED --> IllegalStateException. 2. status = CANCELLED. 3. Nếu paymentStatus = PAID: refundStatus = NOT_REFUNDED; ngược lại giữ NOT_APPLICABLE (vé đặt qua điện thoại chưa thanh toán, ASM-29). | - | Vé của chuyến bị huỷ chuyển Đã huỷ ngay, không chờ hoàn tiền xong (ASM-29) | Issued --> CancelledRefundPending hoặc CancelledNoRefundDue |
| DC-Ticket.calculateRefundAmount() | 1. Không isOnlineRefundPending() --> IllegalStateException. 2. Trả fare (100% giá vé đã ghi, BR-07). | - | Dùng fare đã ghi khi bán nên giá hiện hành sau này không ảnh hưởng (P04 UC-017 mục 8); không vượt số đã thu (NFR-06) | Chỉ ở CancelledRefundPending |
| DC-Ticket.markRefunded() | 1. refundStatus khác NOT_REFUNDED --> IllegalStateException. 2. refundStatus = REFUNDED; refundAttemptStatus = NO_ISSUE. | - | Chặn hoàn lần hai cho cùng vé (NFR-05) | CancelledRefundPending --> CancelledRefunded |
| DC-Ticket.recordRefundNotCompleted() | 1. refundStatus khác NOT_REFUNDED --> IllegalStateException. 2. refundAttemptStatus = FAILED; refundStatus giữ NOT_REFUNDED. | - | Không tự thử lại; cơ chế xử lý lại chờ Q-50 (P04 UC-017 mục 8) | CancelledRefundPending --> CancelledRefundPending (tự chuyển) |
| DC-TripTicketCancellation.cancelTicketsOfTrip(Trip) | 1. Không trip.isCancelled() --> IllegalStateException. 2. tickets = ticketRepository.findActiveByTrip(trip). 3. Với mỗi vé: ticket.cancelForTrip(). 4. ticketRepository.saveAll(tickets). 5. Trả tickets (rỗng khi chuyến không có vé, luồng 7a). | DC-Trip.isCancelled, IF-07.findActiveByTrip, DC-Ticket.cancelForTrip, IF-07.saveAll | Giao dịch do DC-CancelTripService (PKG-16) bao cùng bước đổi trạng thái chuyến | Vé: Issued --> Cancelled* (ST-04) |
| DC-TripTicketCancellation.groupTicketCodesByTravelerPhone(List<Ticket>) | 1. Duyệt vé theo thứ tự đầu vào. 2. Thêm vé vào danh sách của khoá ticket.getTravelerPhone() trong LinkedHashMap. 3. Trả map. | DC-Ticket.getTravelerPhone | Khoá gom là PhoneNumber, bằng nhau khi cùng chuỗi số đã chuẩn hoá; mỗi số nhận một SMS (ASM-30) | Không có ST |
| DC-TripTicketCancellation.summarizeTripCancellation(List<Ticket>) | 1. cancelledTicketCount = số vé. 2. Số điện thoại có vé với cancelNoticeStatus NOT_NOTIFIED là chưa báo được, gom mã vé theo số; notifiedPhoneCount = số số điện thoại khác nhau trừ số chưa báo. 3. Vé refundStatus REFUNDED: refundedTicketCount tăng 1, refundedTotal cộng fare. 4. Vé purchaseChannel ONLINE, refundStatus NOT_REFUNDED và refundAttemptStatus FAILED: thêm mã vé vào refundFailedTicketCodes. 5. Vé purchaseChannel COUNTER, paymentStatus PAID, refundStatus NOT_REFUNDED: counterTicketsAwaitingCashRefund tăng 1. | DC-Ticket.getTravelerPhone, getCancelNoticeStatus, getRefundStatus, getFare, getRefundAttemptStatus, getTicketCode, isOnlineRefundPending | Chỉ đọc; vé mua tại quầy do UC-004, UC-006 tạo (chưa có P07) nên nhánh bước 5 chưa chạy được ở phạm vi này | Không có ST |
| IF-05.findByTripAndSeatCodesForUpdate(Trip, Set<String>) | Hiện thực tìm chỗ theo (trip, seatCode) có seatCode trong tập, sắp theo seatCode tăng dần, khoá ghi từng bản ghi (SELECT ... FOR UPDATE). | - | Thứ tự khoá cố định làm hai yêu cầu chọn tập chỗ giao nhau không khoá chéo (Thiết kế: tránh deadlock); là điểm bảo đảm NFR-04 cùng ràng buộc duy nhất của P13 | Không có ST |
| IF-06.findIdsHoldExpiredAt(LocalDateTime) | Hiện thực tìm Booking có status HOLDING và holdExpiry <= now, chỉ lấy định danh. | - | Cần chỉ mục trên (status, holdExpiry) cho P13 để quét 30 giây không đọc toàn bảng | Không có ST |
| IF-07.nextTicketCodes(int) | Hiện thực lấy count giá trị liên tiếp từ dãy số của kho dữ liệu (sequence), định dạng "SV" + số đệm 0 tới 4 chữ số, mở rộng khi vượt 9999. | DC-TicketCode.of (tạm) | Dãy số duy nhất toàn hệ thống nên mã vé không trùng giữa các chuyến và các bản sao ứng dụng (BR-04); khoảng trống trong dãy khi giao dịch hoàn tác được chấp nhận | Không có ST |
| IF-03.findInSchedule(LocalDateTime) | Hiện thực tìm Trip có departureTime >= from, mọi trạng thái, sắp theo giờ xuất bến tăng dần. | - | Phạm vi lịch chạy theo ASM-55 (chờ Q-73) | Không có ST |

## F4. Bảng ánh xạ message --> operation

Phạm vi F4: mọi message của P07 UC-009 và UC-017 có lớp nhận thuộc PKG-13, PKG-27, PKG-28, và message có lớp gửi thuộc phạm vi mà lớp nhận là interface (IF-02). Cột STT ghi mã message của P07 kèm STT trong ngoặc; P07 UC-017 chỉ có STT. Message trả về có dữ liệu không thành dòng riêng mà đi cùng dòng gọi.

| UC | STT message (P07) | Từ (AC/DC) | Đến (AC/DC) | Message phân tích (// tênTráchNhiệm) | Operation thiết kế (chữ ký đầy đủ) |
|---|---|---|---|---|---|
| UC-009 | SD1a-M02 (1.1) | AC-B-BookTicketOnlineForm | AC-C-BookTicketOnlineController | // startBookTicketOnline | DC-BookTicketOnlineService.startBookTicketOnline(tripId: long): BookTicketOnlineViewModel |
| UC-009 | SD1a-M03 (1.1.1), SD1a-M04 | AC-C-BookTicketOnlineController | AC-C-SearchTripsController | // searchTrips | DC-SearchTripsService.searchTrips(origin: String, destination: String, travelDate: LocalDate): List<TripOption>. Khác điểm gọi: web không giữ trạng thái giữa hai yêu cầu nên DC-BookTicketOnlineRequestHandler gọi trước startBookTicketOnline (P10 F6 đã cho PKG-05 --> DC-SearchTripsService); kết quả trả về của M04 là danh sách TripOption (rỗng --> luồng 2a). Tạm |
| UC-009 | SD1a-M07 (2.1) | AC-B-BookTicketOnlineForm | AC-C-BookTicketOnlineController | // processSeatSelection (chuyến, các chỗ đã chọn) | DC-BookTicketOnlineService.processSeatSelection(tripId: long, seatCodes: Set<String>): BookTicketOnlineViewModel |
| UC-009 | SD1a-M08 (2.1.1) | AC-C-BookTicketOnlineController | AC-E-Booking | «create» // createBooking (chuyến, các chỗ đã chọn) | DC-Booking.createBooking(trip: Trip, seats: List<Seat>): Booking |
| UC-009 | SD1a-M09 (2.1.2), SD1a-M10 | AC-C-BookTicketOnlineController | AC-E-Seat | // checkAvailable (chuyến, các chỗ đã chọn) | DC-Seat.isAvailable(): boolean, gọi cho từng chỗ nạp bằng IF-05.findByTripAndSeatCodesForUpdate(trip: Trip, seatCodes: Set<String>): List<Seat> (Bổ sung: nạp chỗ có khoá ghi, NFR-04) |
| UC-009 | SD1a-M11 (2.1.3), SD1a-M12 | AC-C-BookTicketOnlineController | AC-E-Booking | // checkSeatCountWithinLimit | DC-Booking.isSeatCountWithinLimit(): boolean |
| UC-009 | SD1a-M13 (2.1.4), SD1a-M14 | AC-C-BookTicketOnlineController | AC-E-Trip | // checkDepartureNotReached (chuyến) | DC-Trip.isBeforeDeparture(now: LocalDateTime): boolean |
| UC-009 | SD1a-M18 (2.1.8), SD1a-M19 | AC-C-BookTicketOnlineController | AC-E-Fare | // determineFare (chuyến) | DC-Fare.determineFare(trip: Trip): Money, Fare nạp bằng IF-04.findByRouteAndVehicleType(route: String, vehicleType: VehicleType): Optional<Fare> (Bổ sung: nạp Fare) |
| UC-009 | SD1a-M20 (2.1.9) | AC-C-BookTicketOnlineController | AC-E-Booking | // holdSeats (giá vé mỗi chỗ) | DC-Booking.holdSeats(seatFare: Money, now: LocalDateTime): void |
| UC-009 | SD1a-M21 (2.1.9.1) | AC-E-Booking | AC-E-Seat | // markHeld (thời hạn giữ chỗ) | DC-Seat.markHeld(): void. Tham số thời hạn giữ chỗ bỏ vì Seat không lưu thời hạn, Booking giữ holdExpiry |
| UC-009 | SD1a-M22 (2.1.10) | AC-C-BookTicketOnlineController | AC-C-BookTicketOnlineController | // startWaitingForPaymentResult (BR-03) | Khác lớp nhận: P10 F3 (chốt thành thao tác ghi thời hạn giữ chỗ trên Booking): gộp vào DC-Booking.holdSeats (đặt holdExpiry) và IF-06.save(booking: Booking): Booking |
| UC-009 | SD1b-M02 (3.1) | AC-B-BookTicketOnlineForm | AC-C-BookTicketOnlineController | // processTravelerInfo (họ tên, số điện thoại) | DC-BookTicketOnlineService.processTravelerInfo(bookingId: long, travelerName: String, travelerPhone: String): BookTicketOnlineViewModel |
| UC-009 | SD1b-M03 (3.1.1), SD1b-M04 | AC-C-BookTicketOnlineController | AC-E-Booking | // recordTravelerInfo (họ tên, số điện thoại) | DC-Booking.recordTravelerInfo(travelerName: String, travelerPhone: String, now: LocalDateTime): void |
| UC-009 | SD1b-M06 (3.1.3), SD1b-M07 | AC-C-BookTicketOnlineController | AC-E-Booking | // calculateTotalAmount | DC-Booking.calculateTotalAmount(): Money |
| UC-009 | SD1b-M08 (3.1.4), SD1b-M09 | AC-C-BookTicketOnlineController | AC-C-PayTicketOnlineController | // payTicketOnline (lần đặt vé, tổng tiền) | DC-PayTicketOnlineService.payTicketOnline(booking: Booking, totalAmount: Money): Optional<PaymentTransaction>. Kết quả thành công hoặc thất bại của M09 thành Optional có giá trị hoặc rỗng. Tạm |
| UC-009 | SD1b-M10 (3.1.5) | AC-C-BookTicketOnlineController | AC-C-BookTicketOnlineController | // stopWaitingForPaymentResult | Khác lớp nhận: P10 F3 (chốt thành thao tác xoá thời hạn giữ chỗ trên Booking): DC-Booking.clearHoldExpiry(): void |
| UC-009 | SD1b-M11 (3.1.6) | AC-C-BookTicketOnlineController | AC-E-Booking | // releaseHeldSeats (thanh toán không thành công) | DC-Booking.releaseHeldSeats(): void (cùng operation cho SD1b-M15, SD2-M04) |
| UC-009 | SD1b-M12 (3.1.6.1) | AC-E-Booking | AC-E-Seat | // markAvailable | DC-Seat.markAvailable(): void (cùng operation cho SD1b-M16, SD2-M05) |
| UC-009 | SD1b-M14 (4) | AC-C-BookTicketOnlineController | AC-C-BookTicketOnlineController | // after(BR-03) handleHoldExpiry | DC-BookTicketOnlineService.handleHoldExpiry(bookingId: long): void; điểm vào của bộ định thời: listExpiredHolds(): List<Long> (Bổ sung: cơ chế quét mốc, Bước 1.6a) |
| UC-009 | SD1b-M15 (4.1), SD1b-M16 (4.1.1) | AC-C-BookTicketOnlineController | AC-E-Booking | // releaseHeldSeats (hết thời hạn giữ chỗ); AC-E-Booking --> AC-E-Seat // markAvailable | DC-Booking.releaseHeldSeats(): void; DC-Seat.markAvailable(): void |
| UC-009 | SD1b-M17 (4.2) | AC-C-BookTicketOnlineController | AC-C-PayTicketOnlineController | // cancelPayment (nếu UC-010 còn đang chạy) | DC-PayTicketOnlineService.cancelPayment(booking: Booking): void. Tạm |
| UC-009 | SD1c-M01 (3.1.8), SD1c-M05 | AC-C-BookTicketOnlineController | AC-E-Booking | // issueTickets | DC-Booking.issueTickets(ticketCodes: List<TicketCode>, transaction: PaymentTransaction): List<Ticket>. Thêm hai tham số so với message P07: mã vé (từ IF-07) và giao dịch thu tiền (cho R-20); Đề xuất sửa P07 |
| UC-009 | SD1c-M02 (3.1.8.1) | AC-E-Booking | AC-E-Ticket | «create» // createTicket (chuyến, chỗ, họ tên, số điện thoại, giá vé) | DC-Ticket.createTicket(trip: Trip, seat: Seat, travelerName: String, travelerPhone: PhoneNumber, fare: Money, ticketCode: TicketCode, transaction: PaymentTransaction): Ticket |
| UC-009 | SD1c-M03 (3.1.8.1.1) | AC-E-Ticket | AC-E-Ticket | // generateTicketCode (BR-04) | Khác lớp nhận: P07 F4 giao P12 chọn phạm vi duy nhất của mã: IF-07.nextTicketCodes(count: int): List<TicketCode> |
| UC-009 | SD1c-M04 (3.1.8.2) | AC-E-Booking | AC-E-Seat | // markSold | DC-Seat.markSold(): void |
| UC-009 | SD1c-M06 (3.1.9), SD1c-M09 | AC-C-BookTicketOnlineController | AC-B-SmsGateway | // sendTicketCodesBySms (số điện thoại người đi, mã vé) | Khác lớp nhận: P11b F3 (SS-02): IF-02.sendTicketCodes(recipient: PhoneNumber, ticketCodes: List<TicketCode>): SmsSendResult |
| UC-009 | SD1c-M10 (3.1.10) | AC-C-BookTicketOnlineController | AC-E-Ticket | // recordSmsNotSent (mã vé chưa gửi được) | DC-Ticket.recordSmsNotSent(): void |
| UC-009 | SD2-M02 (2.1.10*a.1) | AC-B-BookTicketOnlineForm | AC-C-BookTicketOnlineController | // requestCancelBooking | DC-BookTicketOnlineService.requestCancelBooking(bookingId: long): void |
| UC-009 | SD2-M03 (2.1.10*a.2) | AC-C-BookTicketOnlineController | AC-C-BookTicketOnlineController | // stopWaitingForPaymentResult | Gộp vào DC-Booking.releaseHeldSeats() (đã xoá holdExpiry); không gọi riêng clearHoldExpiry |
| UC-009 | SD2-M04 (2.1.10*a.3), SD2-M05 | AC-C-BookTicketOnlineController | AC-E-Booking | // releaseHeldSeats (hành khách huỷ); AC-E-Booking --> AC-E-Seat // markAvailable | DC-Booking.releaseHeldSeats(): void; DC-Seat.markAvailable(): void |
| UC-017 | 1.1.1 | AC-C-CancelTripController | AC-E-Trip | // listTripsInSchedule | Khác lớp nhận: P12 (truy vấn tập chuyến thuộc kho dữ liệu, không thuộc một Trip): IF-03.findInSchedule(from: LocalDateTime): List<Trip>; mỗi Trip trả tuyến, giờ xuất bến, xe, tài xế, trạng thái qua getRoute, getDepartureTime, getVehicle, getDriver, getStatus |
| UC-017 | 2.1.1 | AC-C-CancelTripController | AC-E-Trip | // checkNotCancelled (BR-09) | DC-Trip.isCancelled(): boolean, chuyến nạp bằng IF-03.findByIdForUpdate(tripId: long): Optional<Trip> (Bổ sung: nạp chuyến) |
| UC-017 | 2.1.3 | AC-C-CancelTripController | AC-E-Trip | // checkDepartureNotReached (BR-10) | DC-Trip.isBeforeDeparture(now: LocalDateTime): boolean |
| UC-017 | 2.1.5 | AC-C-CancelTripController | AC-E-Trip | // cancelTrip (chuyến, lý do huỷ chuyến) | DC-Trip.cancel(reason: CancelReason, now: LocalDateTime): void; tuyến và giờ xuất bến của message trả về lấy bằng getRoute, getDepartureTime; lưu bằng IF-03.save(trip: Trip): Trip |
| UC-017 | 2.1.8 | AC-C-CancelTripController | AC-E-Ticket | // cancelTicketsOfTrip (chuyến) | Khác lớp nhận: P12 tách từ AC-E-Ticket (P10 F1 giao P12 quyết định): DC-TripTicketCancellation.cancelTicketsOfTrip(trip: Trip): List<Ticket>; phần của một vé: DC-Ticket.cancelForTrip(): void |
| UC-017 | 2.1.9 | AC-C-CancelTripController | AC-E-Ticket | // groupTicketCodesByTravelerPhone (các vé đã huỷ) | Khác lớp nhận: P12 tách từ AC-E-Ticket: DC-TripTicketCancellation.groupTicketCodesByTravelerPhone(tickets: List<Ticket>): Map<PhoneNumber, List<Ticket>> |
| UC-017 | 2.1.11 | AC-C-CancelTripController | AC-E-Ticket | // recordCancelNoticeNotSent (số điện thoại, mã vé) | Khác lớp nhận: P12 tách từ AC-E-Ticket: DC-TripTicketCancellation.recordCancelNoticeNotSent(tickets: List<Ticket>): void; phần của một vé: DC-Ticket.markCancelNoticeNotSent(): void |
| UC-017 | 2.1.12 | AC-C-CancelTripController | AC-E-Ticket | // selectOnlineTicketsToRefund (các vé đã huỷ) | Khác lớp nhận: P12 tách từ AC-E-Ticket: DC-TripTicketCancellation.selectOnlineTicketsToRefund(tickets: List<Ticket>): List<Ticket>; điều kiện từng vé: DC-Ticket.isOnlineRefundPending(): boolean; giao dịch thanh toán của vé: DC-Ticket.getPaymentTransaction(): Optional<PaymentTransaction> |
| UC-017 | 2.1.13 | AC-C-CancelTripController | AC-E-Ticket | // calculateRefundAmount (BR-07) | DC-Ticket.calculateRefundAmount(): Money |
| UC-017 | 2.1.15 | AC-C-CancelTripController | AC-E-Ticket | // markRefunded | DC-Ticket.markRefunded(): void |
| UC-017 | 2.1.17 | AC-C-CancelTripController | AC-E-Ticket | // recordRefundNotCompleted | DC-Ticket.recordRefundNotCompleted(): void |
| UC-017 | 2.1.18 | AC-C-CancelTripController | AC-E-Ticket | // summarizeTripCancellation (các vé đã huỷ) | Khác lớp nhận: P12 tách từ AC-E-Ticket: DC-TripTicketCancellation.summarizeTripCancellation(tickets: List<Ticket>): TripCancellationSummary |

F4b. Message có lớp nhận ngoài phạm vi, để lần chạy chứa lớp nhận thiết kế; cột cuối ghi cách DC-BookTicketOnlineService thể hiện kết quả của message để Presentation không phụ thuộc ngược lên (P09 QT-2, QT-4).

| UC | STT message (P07) | Từ | Đến (lớp ngoài, PKG) | Message | Thể hiện ở phạm vi này |
|---|---|---|---|---|---|
| UC-009 | SD1a-M01, SD1a-M06, SD1b-M01, SD2-M01 | ACT-01 | AC-B-BookTicketOnlineForm (PKG-05) | // requestBookTicket, // selectSeats, // enterTravelerInfo, // cancelBooking | Lần chạy PKG-05; View gọi startBookTicketOnline, processSeatSelection, processTravelerInfo, requestCancelBooking ở F2 |
| UC-009 | SD1a-M05 (1.1.2) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifyNoTripSelected | searchTrips trả danh sách rỗng, View hiển thị MSG-01 |
| UC-009 | SD1a-M15 (2.1.5) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifySeatsUnavailable | processSeatSelection ném SeatsUnavailableException, View hiển thị MSG-02 |
| UC-009 | SD1a-M16 (2.1.6) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifySeatLimitExceeded | processSeatSelection ném SeatLimitExceededException, View hiển thị MSG-03 |
| UC-009 | SD1a-M17 (2.1.7) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifyTripDeparted | processSeatSelection ném TripDepartedException, View hiển thị MSG-04 |
| UC-009 | SD1b-M05 (3.1.2) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifyTravelerInfoMissing | processTravelerInfo ném TravelerInfoMissingException, View hiển thị MSG-05, MSG-06 |
| UC-009 | SD1b-M13 (3.1.7) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifyPaymentFailed | processTravelerInfo ném PaymentFailedException, View hiển thị MSG-07 |
| UC-009 | SD1b-M18 (4.3) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifyHoldExpired | Mọi thao tác trên lần đặt đã trả chỗ ném HoldExpiredException ở yêu cầu kế tiếp của hành khách, View hiển thị MSG-08 (web không đẩy sang trình duyệt) |
| UC-009 | SD1c-M07 (3.1.9.1), SD1c-M08 | AC-B-SmsGateway | ACT-07 Cổng SMS | // requestSmsSending (số điện thoại, mã vé); kết quả gửi SMS | Bên trong SS-02 (P11b F4 trang Hộp trắng sendTicketCodes), không thuộc lớp của phạm vi này |
| UC-009 | SD1c-M11 (3.1.11) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // showIssuedTickets (vé đã phát hành, chuyến, tổng tiền) | processTravelerInfo trả BookTicketOnlineViewModel (issuedTickets, totalAmount), View hiển thị SCR-04 |
| UC-009 | SD2-M06 (2.1.10*a.4) | AC-C-BookTicketOnlineController | AC-B-BookTicketOnlineForm (PKG-05) | // notifyBookingCancelled | requestCancelBooking trả void, View hiển thị MSG-09 |
| UC-017 | 1.1.2, 2.1.2, 2.1.4, 2.1.19, 1.1.2*a.1.1 | AC-C-CancelTripController | AC-B-CancelTripForm (PKG-07) | // showScheduledTrips, // notifyTripAlreadyCancelled, // notifyTripDeparted, // showCancellationResult, // notifyCancelTripAborted | Lần chạy PKG-07, PKG-16 |
| UC-017 | 2.1.10, 2.1.14, 2.1.16, 2.1.6, 2.1.7 | AC-C-CancelTripController | SS-02 IF-02 (PKG-22), SS-01 IF-01 (PKG-21), AC-E-PaymentTransaction (PKG-29), chính control | // sendTripCancellationBySms, // requestTicketRefund, // recordRefund, // cancelOverdueReservationMark, // cancelPassengerListMark | Lớp gửi DC-CancelTripService thuộc PKG-16; lần chạy PKG-16, PKG-29 |

## F5. Bảng quan hệ

| ID | Lớp A | Lớp B | Loại | Multiplicity | Điều hướng | Lý do | Vai trò (đầu A / đầu B) | Căn cứ hiển thị |
|---|---|---|---|---|---|---|---|---|
| R-02 | DC-BookTicketOnlineService | DC-SearchTripsService | Association | A 1 - B 1 | A --> B | Giữ mã P08. Đổi từ Dependency thành Association: control giữ DC-SearchTripsService làm field để gọi viewSeatMap ở mọi lần mở bước chọn chỗ (include UC-008). Thiết kế: tiêm phụ thuộc | - / searchTripsService | field |
| R-03 | DC-BookTicketOnlineService | DC-PayTicketOnlineService | Association | A 1 - B 1 | A --> B | Giữ mã P08. Đổi từ Dependency thành Association: control giữ DC-PayTicketOnlineService làm field để gọi payTicketOnline, cancelPayment (include UC-010). Thiết kế: tiêm phụ thuộc | - / payTicketOnlineService | field |
| R-04 | DC-BookTicketOnlineService | DC-Trip | Dependency |  | A --> B | Giữ mã P08. Đổi từ Association thành Dependency: Trip nạp qua IF-03 trong từng method và chuyền cho Booking, Fare làm tham số (cây quyết định bước 3) |  | biến cục bộ |
| R-05 | DC-BookTicketOnlineService | DC-Seat | Dependency |  | A --> B | Giữ mã P08. Đổi từ Association thành Dependency: Seat nạp qua IF-05 trong từng method (cây quyết định bước 3) |  | biến cục bộ |
| R-06 | DC-BookTicketOnlineService | DC-Fare | Dependency |  | A --> B | Giữ mã P08. Đổi từ Association thành Dependency: Fare nạp qua IF-04 trong processSeatSelection (cây quyết định bước 3) |  | biến cục bộ |
| R-07 | DC-BookTicketOnlineService | DC-Booking | Dependency |  | A --> B | Giữ mã P08. Đổi từ Association thành Dependency: Booking nạp qua IF-06 hoặc tạo trong từng method; control không giữ lần đặt giữa hai lời gọi (NFR-08: không giữ trạng thái phiên trong bộ nhớ, P09 F7) |  | biến cục bộ |
| R-08 | DC-BookTicketOnlineService | DC-Ticket | Dependency |  | A --> B | Giữ mã P08. Đổi từ Association thành Dependency: Ticket nhận từ Booking.issueTickets rồi chuyền cho IF-07, DC-Ticket.recordSmsNotSent |  | biến cục bộ |
| R-09 | DC-BookTicketOnlineService | IF-02 | Association | A 1 - B 1 | A --> B | Giữ mã P08 (B là AC-B-SmsGateway thành SS-02 với IF-02, P10 F3). Control chỉ phụ thuộc interface (Bước 1.2, P09 QT-6). Thiết kế: tiêm phụ thuộc | - / smsGateway | field |
| R-10 | DC-Booking | DC-Seat | Association | A 0..* - B 1..5 | A --> B | Giữ mã P08 và loại Association. Thay thuộc tính seatCodes của P08 (Bước 5.3). Chỗ tồn tại độc lập, thuộc nhiều lần đặt theo thời gian (ASM-44) nên không là composition; B 1..5 theo BR-01, A 0..* theo ASM-44 (chờ Q-60). Chỉ giữ chiều Booking --> Seat vì Seat không cần biết lần đặt | bookings / seats | field |
| R-11 | DC-Booking | DC-Ticket | Association | A 0..1 - B 0..5 | A --> B | Giữ mã P08 và loại Association. Vé tồn tại sau khi lần đặt kết thúc (GL-12, GL-24) nên không là composition; B 0..5 theo BR-01, BR-04; A 0..1 theo ASM-44 (chờ Q-60). Chiều Booking --> Ticket vì Booking tạo vé; Ticket không cần biết lần đặt | booking / tickets | field |
| R-12 | DC-Booking | DC-Trip | Association | A 0..* - B 1 | A --> B | Giữ mã P08 và loại Association. Thay thuộc tính trip của P08 (Bước 5.3). Mang ràng buộc mọi chỗ của một lần đặt cùng một chuyến (P08 F4 R-12). Trip không cần biết các lần đặt, tìm qua IF-06 | bookings / trip | field |
| R-19 | DC-Ticket | DC-Trip | Association | A 0..* - B 1 | A --> B | Giữ mã P08 và loại Association. UC-017 truy vấn vé theo chuyến qua IF-07.findActiveByTrip; Trip không cần biết danh sách vé | tickets / trip | field |
| R-20 | DC-Ticket | DC-PaymentTransaction | Association | A 0..* - B 0..1 | A --> B | Giữ mã P08 và loại Association. B 0..1 vì vé mua tại quầy không có giao dịch (BR-08); Booking.issueTickets chuyền giao dịch cho từng vé. Lớp B thuộc PKG-29 (lần chạy PKG-29) | tickets / paymentTransaction | field |
| R-21 | DC-Seat | DC-Trip | Association | A 1..* - B 1 | A --> B | Giữ mã P08 và loại Association (ASM-43, chờ Q-59). Mỗi chỗ thuộc đúng một chuyến; định danh chỗ là (trip, seatCode) | seats / trip | field |
| R-22 | DC-Ticket | DC-Seat | Association | A 0..* - B 1 | A --> B | Giữ mã P08 và loại Association. Vé đã huỷ vẫn được lưu nên một chỗ có 0..* vé theo thời gian (ASM-44); tại một thời điểm một vé đang có hiệu lực cho chỗ (BR-02) | tickets / seat | field |
| R-23 | DC-BookTicketOnlineService | IF-03 | Association | A 1 - B 1 | A --> B | Mới. Nạp và lưu Trip qua interface kho dữ liệu (P09 QT-5). Thiết kế: tiêm phụ thuộc | - / tripRepository | field |
| R-24 | DC-BookTicketOnlineService | IF-04 | Association | A 1 - B 1 | A --> B | Mới. Nạp Fare của chuyến (P07 UC-009 SD1a-M18). Thiết kế: tiêm phụ thuộc | - / fareRepository | field |
| R-25 | DC-BookTicketOnlineService | IF-05 | Association | A 1 - B 1 | A --> B | Mới. Nạp và lưu Seat có khoá ghi (NFR-04). Thiết kế: tiêm phụ thuộc | - / seatRepository | field |
| R-26 | DC-BookTicketOnlineService | IF-06 | Association | A 1 - B 1 | A --> B | Mới. Nạp, lưu Booking và tìm lần đặt hết hạn. Thiết kế: tiêm phụ thuộc | - / bookingRepository | field |
| R-27 | DC-BookTicketOnlineService | IF-07 | Association | A 1 - B 1 | A --> B | Mới. Cấp mã vé và lưu Ticket. Thiết kế: tiêm phụ thuộc | - / ticketRepository | field |
| R-28 | DC-SearchTripsService | IF-03 | Association | A 1 - B 1 | A --> B | Mới. Tìm chuyến theo tuyến và ngày, nạp chuyến (Tạm). Thiết kế: tiêm phụ thuộc | - / tripRepository | field |
| R-29 | DC-SearchTripsService | IF-05 | Association | A 1 - B 1 | A --> B | Mới. Nạp các chỗ của chuyến cho sơ đồ chỗ (Tạm). Thiết kế: tiêm phụ thuộc | - / seatRepository | field |
| R-30 | DC-PayTicketOnlineService | IF-01 | Association | A 1 - B 1 | A --> B | Mới. P10 F6 đã có PKG-13 --> PKG-21 (Tạm, NFR-10); chữ ký thu tiền của IF-01 xem bảng Chữ ký interface tạm. Thiết kế: tiêm phụ thuộc | - / paymentGateway | field |
| R-31 | DC-PayTicketOnlineService | IF-08 | Association | A 1 - B 1 | A --> B | Mới. Lưu PaymentTransaction của lần thu tiền (Tạm, chờ P07 UC-010; P09 F6 PKG-13 --> PKG-29). Thiết kế: tiêm phụ thuộc | - / paymentTransactionRepository | field |
| R-32 | DC-TripTicketCancellation | IF-07 | Association | A 1 - B 1 | A --> B | Mới. Tìm vé đang có hiệu lực của chuyến và lưu vé đã đổi trạng thái. Thiết kế: tiêm phụ thuộc | - / ticketRepository | field |
| R-33 | DC-BookTicketOnlineService | DC-BookTicketOnlineViewModel | Dependency |  | A --> B | Mới. Control dựng view model từ Booking, Ticket để trả cho Presentation (P10 cơ chế MVC passive) |  | biến cục bộ |
| R-34 | DC-SearchTripsService | DC-BookTicketOnlineViewModel | Dependency |  | A --> B | Mới. viewSeatMap dựng view model sơ đồ chỗ |  | biến cục bộ |
| R-35 | DC-Fare | DC-Trip | Dependency |  | A --> B | Mới. determineFare nhận chuyến làm tham số (P07 UC-009 SD1a-M18 // determineFare (chuyến)); trước đây P08 chưa có quan hệ nào của Fare. Fare vẫn không giữ tham chiếu tới Trip (P08 Vấn đề còn mở) |  | tham số |
| R-36 | DC-Booking | DC-PaymentTransaction | Dependency |  | A --> B | Mới. issueTickets nhận giao dịch thu tiền làm tham số rồi chuyền cho từng Ticket (R-20). Lớp B thuộc PKG-29 |  | tham số |
| R-37 | DC-TripTicketCancellation | DC-Ticket | Dependency |  | A --> B | Mới. Mọi operation nhận hoặc trả danh sách Ticket qua tham số, kiểu trả về hoặc biến cục bộ |  | tham số |
| R-38 | DC-TripTicketCancellation | DC-Trip | Dependency |  | A --> B | Mới. cancelTicketsOfTrip nhận chuyến làm tham số |  | tham số |
| R-39 | DC-BookTicketOnlineService | Clock (java.time) | Association | A 1 - B 1 | A --> B | Mới. Nhận đồng hồ qua constructor để so hạn giữ chỗ, giờ xuất bến, X2 kiểm thử được giá trị biên (Bước 2.6). Nền tảng đã có kiểu đồng hồ nên không cấp IF. Thiết kế: tiêm phụ thuộc | - / clock | field |
| R-40 | DC-SearchTripsService | Clock (java.time) | Association | A 1 - B 1 | A --> B | Mới. Lọc chuyến đã xuất bến theo giờ hiện tại (Bước 2.6). Thiết kế: tiêm phụ thuộc | - / clock | field |
| R-41 | IF-03 | DC-Trip | Dependency |  | A --> B | Mới. Interface kho dữ liệu của entity (P10 F3): Trip là tham số và kiểu trả về |  | tham số |
| R-42 | IF-04 | DC-Fare | Dependency |  | A --> B | Mới. Interface kho dữ liệu của entity (P10 F3): Fare là tham số và kiểu trả về |  | tham số |
| R-43 | IF-05 | DC-Seat | Dependency |  | A --> B | Mới. Interface kho dữ liệu của entity (P10 F3): Seat là tham số và kiểu trả về |  | tham số |
| R-44 | IF-06 | DC-Booking | Dependency |  | A --> B | Mới. Interface kho dữ liệu của entity (P10 F3): Booking là tham số và kiểu trả về |  | tham số |
| R-45 | IF-07 | DC-Ticket | Dependency |  | A --> B | Mới. Interface kho dữ liệu của entity (P10 F3): Ticket là tham số và kiểu trả về |  | tham số |

Quan hệ P08 có một đầu ngoài phạm vi, không liệt kê ở đây vì Lớp A thuộc lần chạy khác: R-01 (PKG-05), R-13 (PKG-07), R-14 đến R-18 (PKG-16); xem Vấn đề còn mở. Quan hệ phụ thuộc chỉ xuất hiện trong chữ ký (kiểu giá trị, enumeration, ngoại lệ, kiểu kết quả) không có dòng riêng. Không có Generalization, Realization trong phạm vi: Realization của IF-03 đến IF-07 do DC-Relational*Repository (PKG-20) thực hiện, thuộc lần chạy PKG-20. Dòng R-39, R-40 liên quan kiểu java.time.Clock của nền tảng, không vẽ.

## F6. State machine

Bốn lớp có state machine: DC-Trip (ST-01), DC-Seat (ST-02), DC-Booking (ST-03), DC-Ticket (ST-04). DC-Fare không có (chỉ tạo và sửa, một trạng thái). Lớp control và kho dữ liệu không có.

### ST-01 DC-Trip

F6.1. Bảng trạng thái

| ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết | entry | do | exit |
|---|---|---|---|---|---|---|
| ST-01 | DC-Trip | Scheduled | status = SCHEDULED; chuyến chưa huỷ (GL-03 Chưa huỷ) | - | - | - |
| ST-01 | DC-Trip | Cancelled | status = CANCELLED và cancelReason có giá trị (GL-04 Đã huỷ) | cancelReason = reason | - | - |

F6.2. Bảng chuyển trạng thái

| ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích | STT | Operation tương ứng (DC.operation) | Nguồn (BR / UC bước) |
|---|---|---|---|---|---|---|---|---|---|
| ST-01 | DC-Trip | (initial) | create |  | / status = SCHEDULED | Scheduled | 1 | DC-Trip.Trip(...) | Bổ sung: khởi tạo (UC-016 chờ P07); GL-03 |
| ST-01 | DC-Trip | Scheduled | cancel(reason, now) | [now < departureTime] | / status = CANCELLED; cancelReason = reason | Cancelled | 2 | DC-Trip.cancel | BR-09, BR-10; UC-017 bước 4, 5; ASM-26 |

Sự kiện bị từ chối:

| ST | Trạng thái | Sự kiện | Xử lý (bỏ qua / ngoại lệ <tên>) |
|---|---|---|---|
| ST-01 | Scheduled | cancel(reason, now) [now >= departureTime] | ngoại lệ TripDepartedException (BR-10, luồng 4b) |
| ST-01 | Cancelled | cancel(reason, now) | ngoại lệ TripAlreadyCancelledException (BR-09, luồng 4a); kiểm tra trước giờ xuất bến theo ASM-26 |

F6.3. Ánh xạ về mô hình lớp

| ST | Thuộc tính biểu diễn trạng thái | Kiểu (enumeration) | Operation được thêm/sửa |
|---|---|---|---|
| ST-01 | status | TripStatus | cancel (đã có), isCancelled (đã có), getStatus |

Ghi chú: Không có sự kiện kết thúc vòng đời (lưu trữ, xoá) trong nguồn nên không vẽ final. Hai trạng thái, giữ state machine vì BR-09, BR-10 dạng "chỉ được huỷ khi chưa huỷ và chưa tới giờ xuất bến" (Target 18).

F6.4. Sơ đồ state machine: file diagrams/P12-state-DC-Trip.drawio

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-01-I | Initial | - | - | - | initial | 60 | 100 | 40 | 40 |
| ST-01-S1 | State | Scheduled | - | - | status = SCHEDULED; chuyến chưa huỷ (GL-03 Chưa huỷ) | 200 | 90 | 240 | 60 |
| ST-01-S2 | State | Cancelled; entry / cancelReason = reason | - | - | status = CANCELLED và cancelReason có giá trị (GL-04 Đã huỷ) | 680 | 90 | 240 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn (su_kien [guard] / hanh_dong) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-01-T1 | ST-01-I | ST-01-S1 | Transition | create / status = SCHEDULED | - | - |
| ST-01-T2 | ST-01-S1 | ST-01-S2 | Transition | cancel(reason, now) [now < departureTime] / status = CANCELLED; cancelReason = reason | - | - |

### ST-02 DC-Seat

F6.1. Bảng trạng thái

| ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết | entry | do | exit |
|---|---|---|---|---|---|---|
| ST-02 | DC-Seat | Available | tripState = AVAILABLE; chưa có vé và chưa bị giữ (GL-02) | - | - | - |
| ST-02 | DC-Seat | Held | tripState = HELD; được giữ cho một lần đặt HOLDING (GL-08) | - | - | - |
| ST-02 | DC-Seat | Sold | tripState = SOLD; có vé đang có hiệu lực (BR-02) | - | - | - |

F6.2. Bảng chuyển trạng thái

| ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích | STT | Operation tương ứng (DC.operation) | Nguồn (BR / UC bước) |
|---|---|---|---|---|---|---|---|---|---|
| ST-02 | DC-Seat | (initial) | create |  | / tripState = AVAILABLE | Available | 1 | DC-Seat.Seat(...) | Bổ sung: khởi tạo (UC-016, UC-021 chờ P07) |
| ST-02 | DC-Seat | Available | markHeld |  | / tripState = HELD | Held | 2 | DC-Seat.markHeld | BR-02, NFR-04; UC-009 bước 5 |
| ST-02 | DC-Seat | Held | markSold |  | / tripState = SOLD | Sold | 3 | DC-Seat.markSold | BR-04; UC-009 bước 9 |
| ST-02 | DC-Seat | Held | markAvailable |  | / tripState = AVAILABLE | Available | 4 | DC-Seat.markAvailable | BR-03, ASM-24; UC-009 luồng 5a, 8a, *a |

Sự kiện bị từ chối:

| ST | Trạng thái | Sự kiện | Xử lý (bỏ qua / ngoại lệ <tên>) |
|---|---|---|---|
| ST-02 | Held | markHeld | ngoại lệ SeatsUnavailableException (BR-02, NFR-04) |
| ST-02 | Sold | markHeld | ngoại lệ SeatsUnavailableException (BR-02) |
| ST-02 | Available | markSold | ngoại lệ IllegalStateException |
| ST-02 | Available | markAvailable | ngoại lệ IllegalStateException |
| ST-02 | Sold | markSold | ngoại lệ IllegalStateException |
| ST-02 | Sold | markAvailable | ngoại lệ IllegalStateException; trả chỗ của vé đã bán (trả vé, đổi vé) chờ P07 của UC-012, UC-014 |

F6.3. Ánh xạ về mô hình lớp

| ST | Thuộc tính biểu diễn trạng thái | Kiểu (enumeration) | Operation được thêm/sửa |
|---|---|---|---|
| ST-02 | tripState | SeatState | isAvailable, getTripState (đã có) |

Ghi chú: Không có sự kiện lưu trữ, xoá nên không vẽ final. Chuyển Sold --> Available chưa có vì UC-012, UC-014 chưa có P07.

F6.4. Sơ đồ state machine: file diagrams/P12-state-DC-Seat.drawio

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-02-I | Initial | - | - | - | initial | 60 | 100 | 40 | 40 |
| ST-02-S1 | State | Available | - | - | tripState = AVAILABLE; chưa có vé và chưa bị giữ (GL-02) | 200 | 90 | 220 | 60 |
| ST-02-S2 | State | Held | - | - | tripState = HELD; được giữ cho một lần đặt HOLDING (GL-08) | 680 | 90 | 220 | 60 |
| ST-02-S3 | State | Sold | - | - | tripState = SOLD; có vé đang có hiệu lực (BR-02) | 1160 | 90 | 220 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn (su_kien [guard] / hanh_dong) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-02-T1 | ST-02-I | ST-02-S1 | Transition | create / tripState = AVAILABLE | - | - |
| ST-02-T2 | ST-02-S1 | ST-02-S2 | Transition | markHeld / tripState = HELD | - | - |
| ST-02-T3 | ST-02-S2 | ST-02-S3 | Transition | markSold / tripState = SOLD | - | - |
| ST-02-T4 | ST-02-S2 | ST-02-S1 | Transition | markAvailable / tripState = AVAILABLE | - | (790,220); (310,220) |

### ST-03 DC-Booking

F6.1. Bảng trạng thái

| ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết | entry | do | exit |
|---|---|---|---|---|---|---|
| ST-03 | DC-Booking | Selecting | status = SELECTING; chỉ tồn tại trong bộ nhớ của giao dịch chọn chỗ, chưa lưu | - | - | - |
| ST-03 | DC-Booking | Holding | status = HOLDING; các chỗ đang giữ, holdExpiry có giá trị hoặc rỗng sau khi dừng chờ | - | do / chờ tới holdExpiry (bộ định thời PKG-11 quét) | - |
| ST-03 | DC-Booking | TicketsIssued | status = TICKETS_ISSUED; mỗi chỗ một vé đã phát hành | - | - | - |
| ST-03 | DC-Booking | SeatsReleased | status = SEATS_RELEASED; các chỗ đã trả cho người khác | - | - | - |

F6.2. Bảng chuyển trạng thái

| ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích | STT | Operation tương ứng (DC.operation) | Nguồn (BR / UC bước) |
|---|---|---|---|---|---|---|---|---|---|
| ST-03 | DC-Booking | (initial) | create(trip, seats) |  | / status = SELECTING | Selecting | 1 | DC-Booking.createBooking | UC-009 bước 4 |
| ST-03 | DC-Booking | Selecting | holdSeats(seatFare, now) | [mọi chỗ AVAILABLE] | / chỗ HELD; holdStartedAt = now; holdExpiry = now + 10 phút; seatFare | Holding | 2 | DC-Booking.holdSeats | BR-03, BR-02; UC-009 bước 5 |
| ST-03 | DC-Booking | Holding | recordTravelerInfo(name, phone, now) | [now < holdExpiry và đã có họ tên, số điện thoại] | / travelerName, travelerPhone | Holding | 3 | DC-Booking.recordTravelerInfo | UC-009 bước 7 |
| ST-03 | DC-Booking | Holding | clearHoldExpiry |  | / holdExpiry = rỗng | Holding | 4 | DC-Booking.clearHoldExpiry | UC-009 bước 8; P10 F3 |
| ST-03 | DC-Booking | Holding | issueTickets(codes, transaction) | [số mã vé = số chỗ] | / tạo Ticket; chỗ SOLD; holdExpiry = rỗng | TicketsIssued | 5 | DC-Booking.issueTickets | BR-04; UC-009 bước 9 |
| ST-03 | DC-Booking | Holding | releaseHeldSeats |  | / chỗ AVAILABLE; holdExpiry = rỗng | SeatsReleased | 6 | DC-Booking.releaseHeldSeats | BR-03, ASM-24; UC-009 luồng 8a, *a |
| ST-03 | DC-Booking | Holding | when(now >= holdExpiry) | [holdExpiry có giá trị] | / releaseHeldSeats (qua DC-BookTicketOnlineService.handleHoldExpiry) | SeatsReleased | 7 | DC-BookTicketOnlineService.handleHoldExpiry; DC-Booking.releaseHeldSeats | BR-03; UC-009 luồng 5a |
| ST-03 | DC-Booking | SeatsReleased | releaseHeldSeats |  | / bỏ qua | SeatsReleased | 8 | DC-Booking.releaseHeldSeats | Thiết kế: hành khách huỷ và bộ định thời có thể xử lý cùng lần đặt, thao tác thứ hai không đổi gì |

Sự kiện bị từ chối:

| ST | Trạng thái | Sự kiện | Xử lý (bỏ qua / ngoại lệ <tên>) |
|---|---|---|---|
| ST-03 | Holding | recordTravelerInfo [now >= holdExpiry] | ngoại lệ HoldExpiredException (luồng 5a) |
| ST-03 | Holding | recordTravelerInfo [thiếu họ tên hoặc số điện thoại] | ngoại lệ TravelerInfoMissingException (luồng 7a) |
| ST-03 | Holding | holdSeats | ngoại lệ IllegalStateException |
| ST-03 | Selecting | holdSeats [có chỗ không AVAILABLE] | ngoại lệ SeatsUnavailableException, giao dịch hoàn tác nên lần đặt bị bỏ (luồng 4a) |
| ST-03 | Selecting | recordTravelerInfo, clearHoldExpiry, issueTickets, releaseHeldSeats | ngoại lệ IllegalStateException |
| ST-03 | SeatsReleased | recordTravelerInfo, clearHoldExpiry, issueTickets | ngoại lệ HoldExpiredException (chỗ đã trả, hết hạn trong lúc thanh toán, BR-06) |
| ST-03 | SeatsReleased | holdSeats | ngoại lệ IllegalStateException |
| ST-03 | TicketsIssued | holdSeats, recordTravelerInfo, clearHoldExpiry, issueTickets, releaseHeldSeats | ngoại lệ IllegalStateException |

F6.3. Ánh xạ về mô hình lớp

| ST | Thuộc tính biểu diễn trạng thái | Kiểu (enumeration) | Operation được thêm/sửa |
|---|---|---|---|
| ST-03 | status | BookingStatus | isHoldExpired, getStatus, getHoldExpiry (đã có) |

Ghi chú: Không có sự kiện lưu trữ, xoá nên không vẽ final. Lần đặt Selecting bị bỏ khi một kiểm tra thất bại (luồng 4a, 4b, 4c) không là chuyển trạng thái: đối tượng chưa lưu và bị thu hồi cùng giao dịch.

F6.4. Sơ đồ state machine: file diagrams/P12-state-DC-Booking.drawio

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-03-I | Initial | - | - | - | initial | 60 | 100 | 40 | 40 |
| ST-03-S1 | State | Selecting | - | - | status = SELECTING; chỉ tồn tại trong bộ nhớ của giao dịch chọn chỗ, chưa lưu | 200 | 90 | 220 | 60 |
| ST-03-S2 | State | Holding; do / chờ tới holdExpiry (bộ định thời PKG-11 quét) | - | - | status = HOLDING; các chỗ đang giữ, holdExpiry có giá trị hoặc rỗng sau khi dừng chờ | 660 | 80 | 300 | 100 |
| ST-03-S3 | State | TicketsIssued | - | - | status = TICKETS_ISSUED; mỗi chỗ một vé đã phát hành | 1200 | 90 | 240 | 60 |
| ST-03-S4 | State | SeatsReleased | - | - | status = SEATS_RELEASED; các chỗ đã trả cho người khác | 660 | 420 | 300 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn (su_kien [guard] / hanh_dong) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-03-T1 | ST-03-I | ST-03-S1 | Transition | create(trip, seats) / status = SELECTING | - | - |
| ST-03-T2 | ST-03-S1 | ST-03-S2 | Transition | holdSeats(seatFare, now) [mọi chỗ AVAILABLE] / chỗ HELD; holdStartedAt = now; holdExpiry = now + 10 phút; seatFare | - | - |
| ST-03-T3 | ST-03-S2 | ST-03-S2 | Transition | recordTravelerInfo(name, phone, now) [now < holdExpiry và đã có họ tên, số điện thoại] / travelerName, travelerPhone | - | (680,40); (740,40) |
| ST-03-T4 | ST-03-S2 | ST-03-S2 | Transition | clearHoldExpiry / holdExpiry = rỗng | - | (880,40); (940,40) |
| ST-03-T5 | ST-03-S2 | ST-03-S3 | Transition | issueTickets(codes, transaction) [số mã vé = số chỗ] / tạo Ticket; chỗ SOLD; holdExpiry = rỗng | - | - |
| ST-03-T6 | ST-03-S2 | ST-03-S4 | Transition | releaseHeldSeats / chỗ AVAILABLE; holdExpiry = rỗng | - | - |
| ST-03-T7 | ST-03-S2 | ST-03-S4 | Transition | when(now >= holdExpiry) [holdExpiry có giá trị] / releaseHeldSeats (qua DC-BookTicketOnlineService.handleHoldExpiry) | - | - |
| ST-03-T8 | ST-03-S4 | ST-03-S4 | Transition | releaseHeldSeats / bỏ qua | - | (760,540); (840,540) |

### ST-04 DC-Ticket

F6.1. Bảng trạng thái

| ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết | entry | do | exit |
|---|---|---|---|---|---|---|
| ST-04 | DC-Ticket | Issued | status = ISSUED; refundStatus = NOT_APPLICABLE (GL-25 vé đang có hiệu lực) | - | - | - |
| ST-04 | DC-Ticket | CancelledRefundPending | status = CANCELLED; refundStatus = NOT_REFUNDED (vé đã thanh toán, chờ hoàn tiền) | - | - | - |
| ST-04 | DC-Ticket | CancelledRefunded | status = CANCELLED; refundStatus = REFUNDED | - | - | - |
| ST-04 | DC-Ticket | CancelledNoRefundDue | status = CANCELLED; refundStatus = NOT_APPLICABLE (vé chưa thanh toán, không có khoản hoàn) | - | - | - |

F6.2. Bảng chuyển trạng thái

| ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích | STT | Operation tương ứng (DC.operation) | Nguồn (BR / UC bước) |
|---|---|---|---|---|---|---|---|---|---|
| ST-04 | DC-Ticket | (initial) | create |  | / status = ISSUED; purchaseChannel = ONLINE; paymentStatus = PAID; refundStatus = NOT_APPLICABLE | Issued | 1 | DC-Ticket.createTicket | UC-009 bước 9; BR-04 |
| ST-04 | DC-Ticket | Issued | cancelForTrip | [paymentStatus = PAID] | / status = CANCELLED; refundStatus = NOT_REFUNDED | CancelledRefundPending | 2 | DC-Ticket.cancelForTrip | UC-017 bước 7; ASM-29 |
| ST-04 | DC-Ticket | Issued | cancelForTrip | [paymentStatus = UNPAID] | / status = CANCELLED | CancelledNoRefundDue | 3 | DC-Ticket.cancelForTrip | UC-017 bước 7; ASM-29 |
| ST-04 | DC-Ticket | CancelledRefundPending | markRefunded |  | / refundStatus = REFUNDED; refundAttemptStatus = NO_ISSUE | CancelledRefunded | 4 | DC-Ticket.markRefunded | UC-017 bước 13; NFR-05 |
| ST-04 | DC-Ticket | CancelledRefundPending | recordRefundNotCompleted |  | / refundAttemptStatus = FAILED | CancelledRefundPending | 5 | DC-Ticket.recordRefundNotCompleted | UC-017 luồng 12a; ASM-33 |
| ST-04 | DC-Ticket | Issued | recordSmsNotSent |  | / smsStatus = NOT_SENT | Issued | 6 | DC-Ticket.recordSmsNotSent | UC-009 luồng 11a; ASM-39 (không vẽ: chỉ đặt cờ ghi nhận) |
| ST-04 | DC-Ticket | CancelledRefundPending, CancelledRefunded, CancelledNoRefundDue | markCancelNoticeNotSent |  | / cancelNoticeStatus = NOT_NOTIFIED | (cùng trạng thái nguồn) | 7 | DC-Ticket.markCancelNoticeNotSent | UC-017 luồng 9a; ASM-42 (không vẽ: chỉ đặt cờ ghi nhận) |

Sự kiện bị từ chối:

| ST | Trạng thái | Sự kiện | Xử lý (bỏ qua / ngoại lệ <tên>) |
|---|---|---|---|
| ST-04 | Issued | markRefunded, recordRefundNotCompleted, calculateRefundAmount, markCancelNoticeNotSent | ngoại lệ IllegalStateException |
| ST-04 | CancelledRefundPending | cancelForTrip, recordSmsNotSent | cancelForTrip: ngoại lệ IllegalStateException (control chỉ gọi cho vé do findActiveByTrip trả); recordSmsNotSent: không áp dụng sau khi huỷ, ngoại lệ IllegalStateException |
| ST-04 | CancelledRefunded | cancelForTrip, markRefunded, recordRefundNotCompleted, calculateRefundAmount | ngoại lệ IllegalStateException (NFR-05: không hoàn lần hai) |
| ST-04 | CancelledNoRefundDue | cancelForTrip, markRefunded, recordRefundNotCompleted, calculateRefundAmount | ngoại lệ IllegalStateException |

F6.3. Ánh xạ về mô hình lớp

| ST | Thuộc tính biểu diễn trạng thái | Kiểu (enumeration) | Operation được thêm/sửa |
|---|---|---|---|
| ST-04 | status, refundStatus | TicketStatus, RefundStatus | isActive, isOnlineRefundPending, getStatus, getRefundStatus (đã có) |

Ghi chú: Trạng thái là cặp (status, refundStatus) nên đặt tên trạng thái ghép; hai thuộc tính trực giao smsStatus, cancelNoticeStatus, refundAttemptStatus chỉ là cờ ghi nhận lỗi nên chuyển 6, 7 là tự chuyển không đổi trạng thái và không vẽ. Không có sự kiện lưu trữ, xoá nên không vẽ final. Trạng thái "Đã trả", "Đã đổi" chờ P07 của UC-012, UC-014.

F6.4. Sơ đồ state machine: file diagrams/P12-state-DC-Ticket.drawio

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-04-I | Initial | - | - | - | initial | 60 | 100 | 40 | 40 |
| ST-04-S1 | State | Issued | - | - | status = ISSUED; refundStatus = NOT_APPLICABLE (GL-25 vé đang có hiệu lực) | 200 | 90 | 220 | 60 |
| ST-04-S2 | State | CancelledRefundPending | - | - | status = CANCELLED; refundStatus = NOT_REFUNDED (vé đã thanh toán, chờ hoàn tiền) | 740 | 90 | 280 | 60 |
| ST-04-S3 | State | CancelledRefunded | - | - | status = CANCELLED; refundStatus = REFUNDED | 1280 | 90 | 260 | 60 |
| ST-04-S4 | State | CancelledNoRefundDue | - | - | status = CANCELLED; refundStatus = NOT_APPLICABLE (vé chưa thanh toán, không có khoản hoàn) | 740 | 380 | 280 | 60 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn (su_kien [guard] / hanh_dong) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-04-T1 | ST-04-I | ST-04-S1 | Transition | create / status = ISSUED; purchaseChannel = ONLINE; paymentStatus = PAID; refundStatus = NOT_APPLICABLE | - | - |
| ST-04-T2 | ST-04-S1 | ST-04-S2 | Transition | cancelForTrip [paymentStatus = PAID] / status = CANCELLED; refundStatus = NOT_REFUNDED | - | - |
| ST-04-T3 | ST-04-S1 | ST-04-S4 | Transition | cancelForTrip [paymentStatus = UNPAID] / status = CANCELLED | - | (310,410) |
| ST-04-T4 | ST-04-S2 | ST-04-S3 | Transition | markRefunded / refundStatus = REFUNDED; refundAttemptStatus = NO_ISSUE | - | - |
| ST-04-T5 | ST-04-S2 | ST-04-S2 | Transition | recordRefundNotCompleted / refundAttemptStatus = FAILED | - | (800,40); (880,40) |

## F7. Bảng thuộc tính

Lớp không có dòng ở bảng này: ba lớp dịch vụ (DC-BookTicketOnlineService, DC-SearchTripsService, DC-PayTicketOnlineService), DC-TripTicketCancellation và các interface không có thuộc tính; phụ thuộc của chúng là association tới interface ở F5. Thuộc tính trỏ tới lớp đã có association không lặp lại: Booking.trip, Booking.seats (R-12, R-10), Booking.tickets (R-11), Seat.trip (R-21), Ticket.trip, seat, paymentTransaction (R-19, R-22, R-20).

| DC | Visibility | Tên | Kiểu | Multiplicity | Mặc định | Ràng buộc | Phạm vi | Derived | Nguồn | Mô tả |
|---|---|---|---|---|---|---|---|---|---|---|
| DC-Trip | - | id | long | 1 |  | {readOnly} | Instance | Không | Thiết kế: định danh nội bộ (kiểu Long mặc định, C1 mục 7) | Định danh nội bộ của chuyến |
| DC-Trip | - | departureTime | LocalDateTime | 1 |  | giờ địa phương | Instance | Không | AC-E-Trip; GL-07; BR-05, BR-10 | Giờ xuất bến, mốc ngừng bán vé trực tuyến và mốc không huỷ được chuyến |
| DC-Trip | - | route | String | 1 |  | khác rỗng; dạng "Điểm đi - Điểm đến" | Instance | Không | AC-E-Trip; GL-22; P04 UC-009 Dữ liệu ra 1 | Tuyến xe của chuyến; tạm kiểu String vì Tuyến xe chưa có lớp |
| DC-Trip | - | vehicleType | VehicleType | 1 |  |  | Instance | Không | AC-E-Trip; GL-14; REQ-60 | Loại xe, cùng route xác định giá vé |
| DC-Trip | - | status | TripStatus | 1 | SCHEDULED |  | Instance | Không | ST-01; GL-03, GL-04 | Trạng thái chuyến, chỉ đổi qua cancel |
| DC-Trip | - | cancelReason | CancelReason | 0..1 |  | khác rỗng khi status = CANCELLED | Instance | Không | AC-E-Trip; ASM-25 | Lý do huỷ chuyến |
| DC-Trip | - | vehicle | String | 1 |  | khác rỗng | Instance | Không | AC-E-Trip; REQ-47 | Định danh hiển thị của xe đảm nhiệm; tạm kiểu String vì Xe chưa có lớp |
| DC-Trip | - | driver | String | 1 |  | khác rỗng | Instance | Không | AC-E-Trip; REQ-47 | Họ tên tài xế đảm nhiệm; tạm kiểu String vì Tài xế chưa có lớp |
| DC-Fare | - | id | long | 1 |  | {readOnly} | Instance | Không | Thiết kế: định danh nội bộ | Định danh nội bộ của dòng giá vé |
| DC-Fare | - | route | String | 1 |  | khác rỗng; {unique} cùng vehicleType | Instance | Không | AC-E-Fare; GL-05; REQ-60 | Tuyến xe áp dụng giá |
| DC-Fare | - | vehicleType | VehicleType | 1 |  | {unique} cùng route | Instance | Không | AC-E-Fare; REQ-60 | Loại xe áp dụng giá |
| DC-Fare | - | amount | Money | 1 |  | lớn hơn 0 | Instance | Không | AC-E-Fare; GL-05 | Giá vé cơ bản của một chỗ, đơn vị đồng |
| DC-Fare | - | surchargePercent | BigDecimal | 0..1 |  | >= 0; mức tối đa do UC-024 kiểm tra (REQ-62) | Instance | Không | AC-E-Fare; GL-16; REQ-61 | Mức tăng giá đang áp dụng, đơn vị phần trăm |
| DC-Seat | - | id | long | 1 |  | {readOnly} | Instance | Không | Thiết kế: định danh nội bộ | Định danh nội bộ của chỗ |
| DC-Seat | - | seatCode | String | 1 |  | {readOnly}; khác rỗng; tối đa 5 ký tự (Thiết kế: SCR-02); {unique} trong cùng trip | Instance | Không | AC-E-Seat; GL-01 | Mã chỗ trên sơ đồ chỗ, ví dụ A05 |
| DC-Seat | - | tripState | SeatState | 1 | AVAILABLE |  | Instance | Không | ST-02; AC-E-Seat; BR-02 | Trạng thái bán của chỗ trên chuyến, chỉ đổi qua markHeld, markSold, markAvailable |
| DC-Booking | + | MAX_SEATS | int | 1 | 5 | {readOnly} | Classifier | Không | BR-01 | Số chỗ tối đa mỗi lần đặt |
| DC-Booking | + | HOLD_DURATION | Duration | 1 | PT10M | {readOnly} | Classifier | Không | BR-03; GL-20 | Thời gian giữ chỗ 10 phút |
| DC-Booking | - | id | long | 1 |  | {readOnly} | Instance | Không | Thiết kế: định danh nội bộ; hành khách giữ định danh này trong phiên (NFR-02, P09 F7) | Định danh nội bộ của lần đặt |
| DC-Booking | - | status | BookingStatus | 1 | SELECTING |  | Instance | Không | ST-03; AC-E-Booking | Trạng thái lần đặt, chỉ đổi qua sự kiện của ST-03 |
| DC-Booking | - | holdStartedAt | LocalDateTime | 0..1 |  | có khi status khác SELECTING | Instance | Không | AC-E-Booking; GL-20, ASM-18 | Thời điểm giữ chỗ, mốc tính thời hạn |
| DC-Booking | - | holdExpiry | LocalDateTime | 0..1 |  | = holdStartedAt + HOLD_DURATION khi có; rỗng sau khi dừng chờ hoặc trả chỗ | Instance | Không | AC-E-Booking; GL-21; BR-03 | Thời hạn giữ chỗ; PKG-11 quét giá trị này để xử lý hết hạn |
| DC-Booking | - | travelerName | String | 0..1 |  | khác rỗng khi đã ghi (Q-44: điều kiện khác chưa quy định); tối đa 100 ký tự (ASM-52) | Instance | Không | AC-E-Booking; GL-17; ASM-19 | Họ tên người đi chung của lần đặt |
| DC-Booking | - | travelerPhone | PhoneNumber | 0..1 |  | khác rỗng khi đã ghi (Q-44) | Instance | Không | AC-E-Booking; GL-17; ASM-19 | Số điện thoại nhận mã vé |
| DC-Booking | - | seatFare | Money | 0..1 |  | lớn hơn 0 khi đã ghi | Instance | Không | AC-E-Booking; ASM-40 | Giá vé của mỗi chỗ, ghi khi giữ chỗ |
| DC-Ticket | - | id | long | 1 |  | {readOnly} | Instance | Không | Thiết kế: định danh nội bộ | Định danh nội bộ của vé |
| DC-Ticket | - | ticketCode | TicketCode | 1 |  | {unique} trên mọi vé; {readOnly} | Instance | Không | AC-E-Ticket; GL-15; BR-04 | Mã vé, ví dụ SV0001 |
| DC-Ticket | - | travelerName | String | 1 |  | {readOnly}; khác rỗng | Instance | Không | AC-E-Ticket; GL-17 | Họ tên người đi, chép từ lần đặt |
| DC-Ticket | - | travelerPhone | PhoneNumber | 1 |  | {readOnly} | Instance | Không | AC-E-Ticket; GL-17; BR-11 | Số điện thoại người đi, chép từ lần đặt, khoá gom SMS của UC-017 |
| DC-Ticket | - | fare | Money | 1 |  | {readOnly}; lớn hơn 0 | Instance | Không | AC-E-Ticket; ASM-40; BR-07 | Giá vé đã ghi khi bán, cơ sở tính số tiền hoàn |
| DC-Ticket | - | purchaseChannel | PurchaseChannel | 1 |  | {readOnly} | Instance | Không | AC-E-Ticket; GL-11; BR-08 | Kênh mua vé; vé tạo ở UC-009 luôn là ONLINE |
| DC-Ticket | - | status | TicketStatus | 1 | ISSUED |  | Instance | Không | ST-04; AC-E-Ticket; ASM-29 | Trạng thái vé |
| DC-Ticket | - | smsStatus | SmsStatus | 1 | NO_ISSUE |  | Instance | Không | AC-E-Ticket; ASM-39 | Ghi nhận mã vé chưa gửi được qua SMS |
| DC-Ticket | - | paymentStatus | PaymentStatus | 1 |  | {readOnly} | Instance | Không | AC-E-Ticket; ASM-29 | Vé đã thanh toán hay chưa |
| DC-Ticket | - | refundStatus | RefundStatus | 1 | NOT_APPLICABLE |  | Instance | Không | ST-04; AC-E-Ticket; ASM-29; BR-08 | Trạng thái hoàn tiền, chỉ đổi qua cancelForTrip, markRefunded |
| DC-Ticket | - | cancelNoticeStatus | CancelNoticeStatus | 1 | NO_ISSUE |  | Instance | Không | AC-E-Ticket; ASM-31, ASM-42 | Ghi nhận vé chưa được báo huỷ chuyến qua SMS |
| DC-Ticket | - | refundAttemptStatus | RefundAttemptStatus | 1 | NO_ISSUE |  | Instance | Không | AC-E-Ticket; ASM-33, ASM-42 | Ghi nhận lần hoàn tiền gần nhất không thành công |
| DC-BookTicketOnlineViewModel | - | bookingId | Long | 0..1 |  | {readOnly}; rỗng khi chưa giữ chỗ | Instance | Không | Thiết kế: định danh lần đặt trong phiên | Định danh lần đặt để Presentation gửi lại ở bước sau |
| DC-BookTicketOnlineViewModel | - | tripId | long | 1 |  | {readOnly} | Instance | Không | SCR-02; UC-009 Dữ liệu ra 1 STT 2 | Chuyến đã chọn |
| DC-BookTicketOnlineViewModel | - | route | String | 1 |  | {readOnly} | Instance | Không | SCR-02, SCR-03, SCR-04 | Tuyến của chuyến, hiển thị "Điểm đi - Điểm đến" |
| DC-BookTicketOnlineViewModel | - | departureTime | LocalDateTime | 1 |  | {readOnly} | Instance | Không | SCR-02, SCR-03, SCR-04 | Giờ xuất bến, hiển thị dd/MM/yyyy HH:mm |
| DC-BookTicketOnlineViewModel | - | seatMap | List<SeatCell> | 0..* |  | {readOnly} | Instance | Không | SCR-02 lưới sơ đồ chỗ; GL-19 | Các chỗ của chuyến kèm chọn được hay không |
| DC-BookTicketOnlineViewModel | - | selectedSeats | List<String> | 0..* |  | {readOnly}; từ 1 đến 5 mã chỗ | Instance | Không | AC-B-BookTicketOnlineForm.selectedSeats; SCR-03 "Chỗ đang giữ" | Mã các chỗ đang giữ của lần đặt |
| DC-BookTicketOnlineViewModel | - | holdExpiry | LocalDateTime | 0..1 |  | {readOnly} | Instance | Không | SCR-03 vùng thời hạn giữ chỗ; BR-03 | Thời hạn giữ chỗ để màn hình đếm ngược |
| DC-BookTicketOnlineViewModel | - | travelerName | String | 0..1 |  | {readOnly} | Instance | Không | SCR-04 vùng người đi | Họ tên người đi hiển thị ở SCR-04 |
| DC-BookTicketOnlineViewModel | - | issuedTickets | List<IssuedTicketLine> | 0..* |  | {readOnly} | Instance | Không | AC-B-BookTicketOnlineForm.issuedTickets; SCR-04 bảng vé | Các vé đã phát hành |
| DC-BookTicketOnlineViewModel | - | totalAmount | BigDecimal | 0..1 |  | {readOnly}; bằng tổng fare của issuedTickets khi có vé | Instance | Không | AC-B-BookTicketOnlineForm.totalAmount; SCR-04 dòng Tổng tiền | Tổng tiền của lần đặt, đơn vị đồng |

## F8. Class diagram

| Sơ đồ | Phạm vi (PKG / UC) | File .drawio | Số lớp |
|---|---|---|---|
| Class diagram PKG-13 | PKG-13 | diagrams/P12-class-PKG-13.drawio | 4 (kèm 8 interface tham chiếu) |
| Class diagram PKG-27 | PKG-27 | diagrams/P12-class-PKG-27.drawio | 4 (kèm 4 lớp tham chiếu) |
| Class diagram PKG-28 | PKG-28 | diagrams/P12-class-PKG-28.drawio | 7 (kèm 2 lớp tham chiếu) |
| Class diagram tham gia UC-009 | UC-009 | diagrams/P12-class-UC-009.drawio | 8 (kèm 1 interface tham chiếu) |

Không vẽ class diagram theo UC-017: UC-017 chỉ có 2 lớp trong phạm vi (Trip, Ticket cùng DC-TripTicketCancellation) và control DC-CancelTripService thuộc PKG-16 (ngưỡng 3 lớp và có control trong phạm vi chưa thoả). Sơ đồ PKG-13 chỉ vẽ interface của lớp ngoài package; dependency từ control tới Trip, Seat, Fare, Booking, Ticket (R-04 đến R-08) liệt kê ở F5, vẽ ở sơ đồ UC-009. Sơ đồ PKG-27 và PKG-28 không vẽ dependency từ control của PKG-13 tới entity (R-04 đến R-08, R-33). Sơ đồ UC-009 ẩn operation không thuộc UC-009, ghi "..." cuối ngăn; nội dung các sơ đồ còn lại lấy đúng F7, F2.

### Sơ đồ PKG-13 (P12-class-PKG-13.drawio)

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-SearchTripsService | Class | SearchTripsService | «control» | PKG-13 | - | 40 | 90 | 520 | 140 |
| DC-BookTicketOnlineViewModel | Class | BookTicketOnlineViewModel | «value object» | PKG-13 | - | 640 | 90 | 380 | 270 |
| DC-BookTicketOnlineService | Class | BookTicketOnlineService | «control» | PKG-13 | - | 1100 | 90 | 520 | 220 |
| DC-PayTicketOnlineService | Class | PayTicketOnlineService | «control» | PKG-13 | - | 1700 | 90 | 520 | 140 |
| IF-03 | Interface | ITripRepository | «interface» | PKG-27 | tham chiếu (lớp ngoài package) | 40 | 540 | 200 | 50 |
| IF-05 | Interface | ISeatRepository | «interface» | PKG-28 | tham chiếu (lớp ngoài package) | 300 | 540 | 200 | 50 |
| IF-04 | Interface | IFareRepository | «interface» | PKG-27 | tham chiếu (lớp ngoài package) | 560 | 540 | 200 | 50 |
| IF-06 | Interface | IBookingRepository | «interface» | PKG-28 | tham chiếu (lớp ngoài package) | 820 | 540 | 200 | 50 |
| IF-07 | Interface | ITicketRepository | «interface» | PKG-28 | tham chiếu (lớp ngoài package) | 1080 | 540 | 200 | 50 |
| IF-02 | Interface | ISmsGateway | «interface» | PKG-22 | tham chiếu (lớp ngoài package) | 1340 | 540 | 200 | 50 |
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-21 | tham chiếu (lớp ngoài package) | 1600 | 540 | 200 | 50 |
| IF-08 | Interface | IPaymentTransactionRepository | «interface» | PKG-29 | tham chiếu (lớp ngoài package) | 1860 | 540 | 250 | 50 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-34 | DC-SearchTripsService | DC-BookTicketOnlineViewModel | Dependency | - | Dependency; biến cục bộ | - |
| R-33 | DC-BookTicketOnlineService | DC-BookTicketOnlineViewModel | Dependency | - | Dependency; biến cục bộ | - |
| R-03 | DC-BookTicketOnlineService | DC-PayTicketOnlineService | Association | đầu nguồn 1; đầu đích 1 payTicketOnlineService | Association; field | - |
| R-02 | DC-BookTicketOnlineService | DC-SearchTripsService | Association | đầu nguồn 1; đầu đích 1 searchTripsService | Association; field | (1160,50); (100,50) |
| R-09 | DC-BookTicketOnlineService | IF-02 | Association | đầu nguồn 1; đầu đích 1 smsGateway | Association; field | (1550,470); (1440,470) |
| R-23 | DC-BookTicketOnlineService | IF-03 | Association | đầu nguồn 1; đầu đích 1 tripRepository | Association; field | (1170,420); (170,420) |
| R-24 | DC-BookTicketOnlineService | IF-04 | Association | đầu nguồn 1; đầu đích 1 fareRepository | Association; field | (1320,440); (660,440) |
| R-25 | DC-BookTicketOnlineService | IF-05 | Association | đầu nguồn 1; đầu đích 1 seatRepository | Association; field | (1250,430); (430,430) |
| R-26 | DC-BookTicketOnlineService | IF-06 | Association | đầu nguồn 1; đầu đích 1 bookingRepository | Association; field | (1400,450); (920,450) |
| R-27 | DC-BookTicketOnlineService | IF-07 | Association | đầu nguồn 1; đầu đích 1 ticketRepository | Association; field | (1470,460); (1180,460) |
| R-28 | DC-SearchTripsService | IF-03 | Association | đầu nguồn 1; đầu đích 1 tripRepository | Association; field | (210,400); (110,400) |
| R-29 | DC-SearchTripsService | IF-05 | Association | đầu nguồn 1; đầu đích 1 seatRepository | Association; field | (390,410); (370,410) |
| R-30 | DC-PayTicketOnlineService | IF-01 | Association | đầu nguồn 1; đầu đích 1 paymentGateway | Association; field | (1870,480); (1700,480) |
| R-31 | DC-PayTicketOnlineService | IF-08 | Association | đầu nguồn 1; đầu đích 1 paymentTransactionRepository | Association; field | (2050,490); (1980,490) |

### Sơ đồ PKG-27 (P12-class-PKG-27.drawio)

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-Trip | Class | Trip | «entity» | PKG-27 | - | 40 | 210 | 520 | 410 |
| DC-Fare | Class | Fare | «entity» | PKG-27 | - | 660 | 210 | 520 | 200 |
| IF-03 | Interface | ITripRepository | «interface» | PKG-27 | - | 40 | 680 | 430 | 190 |
| IF-04 | Interface | IFareRepository | «interface» | PKG-27 | - | 660 | 680 | 520 | 140 |
| DC-Seat | Class | Seat | «entity» | PKG-28 | tham chiếu (lớp ngoài package) | 40 | 40 | 200 | 50 |
| DC-Booking | Class | Booking | «entity» | PKG-28 | tham chiếu (lớp ngoài package) | 340 | 40 | 200 | 50 |
| DC-Ticket | Class | Ticket | «entity» | PKG-28 | tham chiếu (lớp ngoài package) | 640 | 40 | 200 | 50 |
| DC-TripTicketCancellation | Class | TripTicketCancellation | «service» | PKG-28 | tham chiếu (lớp ngoài package) | 940 | 40 | 200 | 50 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-21 | DC-Seat | DC-Trip | Association | đầu nguồn 1..* seats; đầu đích 1 trip | Association; field | - |
| R-12 | DC-Booking | DC-Trip | Association | đầu nguồn 0..* bookings; đầu đích 1 trip | Association; field | (440,130); (250,130) |
| R-19 | DC-Ticket | DC-Trip | Association | đầu nguồn 0..* tickets; đầu đích 1 trip | Association; field | (740,140); (350,140) |
| R-38 | DC-TripTicketCancellation | DC-Trip | Dependency | - | Dependency; tham số | (1040,150); (460,150) |
| R-35 | DC-Fare | DC-Trip | Dependency | - | Dependency; tham số | - |
| R-41 | IF-03 | DC-Trip | Dependency | - | Dependency; tham số | - |
| R-42 | IF-04 | DC-Fare | Dependency | - | Dependency; tham số | - |

### Sơ đồ PKG-28 (P12-class-PKG-28.drawio)

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| IF-05 | Interface | ISeatRepository | «interface» | PKG-28 | - | 40 | 40 | 520 | 160 |
| IF-06 | Interface | IBookingRepository | «interface» | PKG-28 | - | 640 | 40 | 380 | 190 |
| IF-07 | Interface | ITicketRepository | «interface» | PKG-28 | - | 1280 | 40 | 330 | 160 |
| DC-TripTicketCancellation | Class | TripTicketCancellation | «service» | PKG-28 | - | 1900 | 40 | 520 | 200 |
| DC-Seat | Class | Seat | «entity» | PKG-28 | - | 40 | 380 | 260 | 290 |
| DC-Booking | Class | Booking | «entity» | PKG-28 | - | 640 | 380 | 520 | 530 |
| DC-Ticket | Class | Ticket | «entity» | PKG-28 | - | 1280 | 380 | 520 | 610 |
| DC-Trip | Class | Trip | «entity» | PKG-27 | tham chiếu (lớp ngoài package) | 140 | 1130 | 200 | 50 |
| DC-PaymentTransaction | Class | PaymentTransaction | «entity» | PKG-29 | tham chiếu (lớp ngoài package) | 1380 | 1130 | 200 | 50 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-43 | IF-05 | DC-Seat | Dependency | - | Dependency; tham số | - |
| R-44 | IF-06 | DC-Booking | Dependency | - | Dependency; tham số | - |
| R-45 | IF-07 | DC-Ticket | Dependency | - | Dependency; tham số | - |
| R-32 | DC-TripTicketCancellation | IF-07 | Association | đầu nguồn 1; đầu đích 1 ticketRepository | Association; field | - |
| R-10 | DC-Booking | DC-Seat | Association | đầu nguồn 0..* bookings; đầu đích 1..5 seats | Association; field | - |
| R-11 | DC-Booking | DC-Ticket | Association | đầu nguồn 0..1 booking; đầu đích 0..5 tickets | Association; field | - |
| R-22 | DC-Ticket | DC-Seat | Association | đầu nguồn 0..* tickets; đầu đích 1 seat | Association; field | (1380,360); (140,360) |
| R-37 | DC-TripTicketCancellation | DC-Ticket | Dependency | - | Dependency; tham số | (1940,340); (1760,340) |
| R-21 | DC-Seat | DC-Trip | Association | đầu nguồn 1..* seats; đầu đích 1 trip | Association; field | (170,1040); (190,1040) |
| R-12 | DC-Booking | DC-Trip | Association | đầu nguồn 0..* bookings; đầu đích 1 trip | Association; field | (810,1050); (240,1050) |
| R-19 | DC-Ticket | DC-Trip | Association | đầu nguồn 0..* tickets; đầu đích 1 trip | Association; field | (1450,1060); (290,1060) |
| R-20 | DC-Ticket | DC-PaymentTransaction | Association | đầu nguồn 0..* tickets; đầu đích 0..1 paymentTransaction | Association; field | (1630,1070); (1510,1070) |
| R-36 | DC-Booking | DC-PaymentTransaction | Dependency | - | Dependency; tham số | (990,1030); (1450,1030) |
| R-38 | DC-TripTicketCancellation | DC-Trip | Dependency | - | Dependency; tham số | (2380,1080); (310,1080) |

### Sơ đồ UC-009 (P12-class-UC-009.drawio)

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-SearchTripsService | Class | SearchTripsService | «control» | PKG-13 | ẩn operation không thuộc UC-009 | 40 | 90 | 520 | 140 |
| DC-BookTicketOnlineService | Class | BookTicketOnlineService | «control» | PKG-13 | ẩn operation không thuộc UC-009 | 640 | 90 | 520 | 220 |
| DC-PayTicketOnlineService | Class | PayTicketOnlineService | «control» | PKG-13 | ẩn operation không thuộc UC-009 | 1240 | 90 | 520 | 140 |
| DC-Fare | Class | Fare | «entity» | PKG-27 | ẩn operation không thuộc UC-009 | 40 | 440 | 260 | 200 |
| DC-Trip | Class | Trip | «entity» | PKG-27 | ẩn operation không thuộc UC-009 | 400 | 440 | 330 | 250 |
| DC-Seat | Class | Seat | «entity» | PKG-28 | ẩn operation không thuộc UC-009 | 830 | 440 | 260 | 220 |
| DC-Ticket | Class | Ticket | «entity» | PKG-28 | ẩn operation không thuộc UC-009 | 1190 | 440 | 520 | 340 |
| DC-Booking | Class | Booking | «entity» | PKG-28 | ẩn operation không thuộc UC-009 | 1810 | 440 | 520 | 400 |
| IF-02 | Interface | ISmsGateway | «interface» | PKG-22 | tham chiếu (lớp ngoài package) | 1840 | 90 | 200 | 50 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-02 | DC-BookTicketOnlineService | DC-SearchTripsService | Association | đầu nguồn 1; đầu đích 1 searchTripsService | Association; field | - |
| R-03 | DC-BookTicketOnlineService | DC-PayTicketOnlineService | Association | đầu nguồn 1; đầu đích 1 payTicketOnlineService | Association; field | - |
| R-09 | DC-BookTicketOnlineService | IF-02 | Association | đầu nguồn 1; đầu đích 1 smsGateway | Association; field | (740,50); (1900,50) |
| R-04 | DC-BookTicketOnlineService | DC-Trip | Dependency | - | Dependency; biến cục bộ | (810,390); (560,390) |
| R-05 | DC-BookTicketOnlineService | DC-Seat | Dependency | - | Dependency; biến cục bộ | (900,370); (960,370) |
| R-06 | DC-BookTicketOnlineService | DC-Fare | Dependency | - | Dependency; biến cục bộ | (730,380); (170,380) |
| R-07 | DC-BookTicketOnlineService | DC-Booking | Dependency | - | Dependency; biến cục bộ | (1070,350); (2070,350) |
| R-08 | DC-BookTicketOnlineService | DC-Ticket | Dependency | - | Dependency; biến cục bộ | (990,360); (1450,360) |
| R-35 | DC-Fare | DC-Trip | Dependency | - | Dependency; tham số | - |
| R-21 | DC-Seat | DC-Trip | Association | đầu nguồn 1..* seats; đầu đích 1 trip | Association; field | - |
| R-22 | DC-Ticket | DC-Seat | Association | đầu nguồn 0..* tickets; đầu đích 1 seat | Association; field | - |
| R-11 | DC-Booking | DC-Ticket | Association | đầu nguồn 0..1 booking; đầu đích 0..5 tickets | Association; field | - |
| R-10 | DC-Booking | DC-Seat | Association | đầu nguồn 0..* bookings; đầu đích 1..5 seats | Association; field | (1870,880); (890,880) |
| R-12 | DC-Booking | DC-Trip | Association | đầu nguồn 0..* bookings; đầu đích 1 trip | Association; field | (1910,890); (500,890) |
| R-19 | DC-Ticket | DC-Trip | Association | đầu nguồn 0..* tickets; đầu đích 1 trip | Association; field | (1250,900); (460,900) |

## F9. Gán package và kiểm tra phụ thuộc package

| PKG | Lớp (DC) | Phụ thuộc vào PKG (suy từ F5) | Hợp lệ theo P09 (Có / Không: lý do) |
|---|---|---|---|
| PKG-13 | DC-BookTicketOnlineService, DC-SearchTripsService, DC-PayTicketOnlineService, DC-BookTicketOnlineViewModel (+ kiểu phụ trợ F1b) | PKG-21 (R-30 --> IF-01); PKG-22 (R-09 --> IF-02, kiểu DC-SmsSendResult trong chữ ký); PKG-27 (R-04, R-06, R-23, R-24, R-28); PKG-28 (R-05, R-07, R-08, R-25, R-26, R-27, R-29); PKG-29 (R-31 --> IF-08; kiểu Optional<DC-PaymentTransaction> trong chữ ký payTicketOnline); PKG-31 (kiểu Money, PhoneNumber, TicketCode trong chữ ký) | Có: khớp P10 F6 (PKG-13 --> PKG-21, PKG-22, PKG-27, PKG-28, PKG-29, PKG-31); Application phụ thuộc Services và Domain, không phụ thuộc ngược; Presentation (PKG-05, PKG-11) gọi vào PKG-13, PKG-13 không gọi lên (QT-2, QT-4) |
| PKG-27 | DC-Trip, DC-Fare, IF-03, IF-04 (+ kiểu phụ trợ F1b) | PKG-31 (kiểu Money của Fare.amount) | Có: khớp P10 F6 (PKG-27 --> PKG-31); không phụ thuộc PKG-28 dù Seat, Booking, Ticket tham chiếu Trip (một chiều từ PKG-28 tới PKG-27, không vòng, QT-3) |
| PKG-28 | DC-Seat, DC-Booking, DC-Ticket, DC-TripTicketCancellation, IF-05, IF-06, IF-07 (+ kiểu phụ trợ F1b) | PKG-27 (R-12, R-19, R-21, R-38); PKG-29 (R-20, R-36 --> DC-PaymentTransaction); PKG-31 (kiểu Money, PhoneNumber, TicketCode) | Có: khớp P10 F6 (PKG-28 --> PKG-27, PKG-29, PKG-31); cùng layer Domain, một chiều, không vòng (PKG-29 không phụ thuộc PKG-28) |

- Gán package theo cột PKG của P10 F3; lớp mới (DC-TripTicketCancellation, kiểu phụ trợ) vào package của entity mà nó phục vụ. DC-TripTicketCancellation chỉ dùng cho UC-017 nhưng đặt ở PKG-28 vì thao tác trên tập Ticket đổi cùng quy tắc trạng thái của Ticket và để PKG-16 không thêm phụ thuộc mới; không đặt ở PKG-16 (Application) vì quy tắc hoàn tiền BR-07, BR-08 là quy tắc miền.
- Boundary giao diện của hai tác nhân khác nhau không cùng package: không có boundary trong phạm vi lần chạy này.
- Visibility theo P10 F5: lớp và interface của PKG-13, PKG-27, PKG-28 public vì có bên dùng ngoài package; kiểu phụ trợ public khi xuất hiện trong chữ ký công khai, exception public. Không có lớp chỉ dùng nội bộ package.
- Không có phụ thuộc vòng, không có realization đi lên layer trên trong phạm vi; realization của IF-03 đến IF-07 do PKG-20 (Services) đặt xuống Domain, thuộc lần chạy PKG-20.

## F10. Design pattern đã áp dụng

| Pattern | Vấn đề trong thiết kế này | Lớp tham gia (vai trò trong pattern) | Lý do chọn | Phương án đơn giản hơn đã xét |
|---|---|---|---|---|
| Repository | Tách truy cập dữ liệu khỏi logic nghiệp vụ của Application và Domain (P09 QT-5); NFR-04 cần nạp có khoá ghi, NFR-05, NFR-06 cần lưu bền cùng kho | IF-03, IF-04, IF-05, IF-06, IF-07 (Repository); DC-Relational*Repository của PKG-20 (hiện thực, lần chạy PKG-20) | P10 đã chốt mỗi entity một interface kho dữ liệu; MAU_THIET_KE_DA_CHOT không có; mẫu này là cơ chế kiến trúc P09, không do P12 chọn thêm | Gọi thẳng EntityManager từ control: không đạt vì Application phụ thuộc công nghệ lưu trữ, vi phạm QT-5 |
| Không áp dụng: State | Booking, Seat, Ticket, Trip có 2 đến 4 trạng thái và mỗi trạng thái chỉ chặn vài operation bằng guard đơn giản | - | Không đủ dấu hiệu ở F10 (nhiều trạng thái và nhiều operation phải kiểm tra trạng thái) | Enumeration kèm guard trong method và ST-01 đến ST-04 là đủ; tách lớp trạng thái thêm 10 lớp mà không đổi hành vi |
| Không áp dụng: Strategy cho Fare | Giá vé hiện chỉ có một công thức (giá cơ bản cộng mức tăng giá nếu có) | - | Chưa có biến thể thuật toán trong yêu cầu; áp dụng là dự phòng cho yêu cầu chưa có (vi phạm YAGNI) | Một operation Fare.determineFare; xét lại khi UC-023, UC-024 có P07 |

Dịch vụ miền DC-TripTicketCancellation là Pure Fabrication (GRASP) chứ không phải pattern của Gamma; lý do tách ghi ở F1. Adapter cho Cổng SMS, Cổng thanh toán nằm trong SS-01, SS-02 (P11b), không áp dụng thêm ở lần chạy này.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-73 | Màn hình bước 2 của UC-017 hiển thị những chuyến nào của lịch chạy? (Mọi chuyến có giờ xuất bến từ thời điểm hiện tại trở đi, gồm cả chuyến đã huỷ / Chỉ các chuyến của tuần hiện tại / Khoảng ngày khác do nhân viên điều hành chọn) | IF-03.findInSchedule; UC-017 bước 2, Dữ liệu ra 1; GL-13 | P04 UC-017 bước 2 "Hiển thị các chuyến trong lịch chạy" và GL-13 "Danh sách các chuyến xe của một tuần" không nêu phạm vi chuyến hiển thị |
| Q-74 | Giá vé sau khi cộng mức tăng giá không chia hết cho đồng thì làm tròn thế nào? (Làm tròn gần nhất về đồng / Làm tròn lên / Làm tròn xuống) | DC-Fare.determineFare, DC-Booking.seatFare, DC-Ticket.fare, số tiền hoàn của UC-017 (BR-07); REQ-61 | REQ-61 nêu mức tăng giá theo phần trăm; P04 UC-009 Dữ liệu ra 1 nêu giá vé là số nguyên đồng nhưng không nêu cách làm tròn |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-55 | Bước 2 của UC-017 hiển thị mọi chuyến có giờ xuất bến từ thời điểm hiện tại trở đi, gồm cả chuyến đã huỷ để nhân viên điều hành thấy trạng thái (BR-09); chuyến đã xuất bến không hiển thị vì không huỷ được (BR-10). | Chờ Q-73. Nguồn không nêu phạm vi chuyến hiển thị; chọn phạm vi rộng nhất còn có nghĩa với hai BR huỷ chuyến | IF-03.findInSchedule; DC-Trip |
| ASM-56 | Giá vé có mức tăng giá được làm tròn gần nhất về đồng (nửa đồng làm tròn lên); giá vé, tổng tiền, số tiền hoàn đều là số nguyên đồng. | Chờ Q-74. Nguồn không nêu cách làm tròn; chọn cách làm tròn phổ biến nhất và khớp định dạng số nguyên đồng của P04 UC-009 Dữ liệu ra 1 | DC-Fare.determineFare; DC-Money.scaleBy |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P07 | UC-009 SD1c-M01 (STT 3.1.8) // issueTickets, SD1c-M02 // createTicket, SD1c-M03 // generateTicketCode | Message không mang giao dịch thanh toán và mã vé, trong khi R-20 (P08) gắn vé với giao dịch để UC-017 hoàn tiền; generateTicketCode là self-message của Ticket nhưng tính duy nhất của mã cần kho dữ liệu | Thêm giao dịch thanh toán vào issueTickets, createTicket; chuyển generateTicketCode thành message tới kho vé (IF-07.nextTicketCodes) |
| P07 | UC-010 (chưa có), UC-009 SD1b-M08 // payTicketOnline | Kết quả UC-010 trả về chỉ là thành công hoặc thất bại; Booking.issueTickets cần giao dịch thu tiền thành công để gắn vào vé (R-20) | Khi viết P07 của UC-010, trả giao dịch thanh toán khi thành công và rỗng khi thất bại |
| P10 | F3, F4, F5 (PKG-28) | P12 cấp DC-TripTicketCancellation (PKG-28) để tách bốn trách nhiệm tác động lên tập vé của chuyến khỏi DC-Ticket (P08 F6 không đạt gắn kết, P10 giao P12 quyết định); P10 chưa có phần tử này | Khi chạy lại P10, thêm DC-TripTicketCancellation vào bảng phần tử mới do thiết kế, vào PKG-28 ở F4, visibility public ở F5, được dùng bởi PKG-16 |
| P11b | SS-01 IF-01 (thu tiền vé, dừng phiên thanh toán) | DC-PayTicketOnlineService (PKG-13) dùng IF-01 nhưng P11b chưa có chữ ký thu tiền và dừng phiên (Chờ P07 UC-010); P12 đặt chữ ký tạm | Chạy P04, P07 của UC-010, rồi P11b cho SS-01; khi có chữ ký, chạy lại P12 cho PKG-13 |
| P08 | F3 AC-E-Trip, AC-E-Fare (thuộc tính route, vehicle, driver) | Tuyến xe, Xe, Tài xế chưa có lớp nên Trip.route, Fare.route, Trip.vehicle, Trip.driver kiểu String; tra cứu theo điểm đi, điểm đến (REQ-05) phải ghép và tách chuỗi route | Khi UC-020, UC-021, UC-022 có P07, thêm lớp Tuyến xe (điểm đi, điểm đến), Xe, Tài xế và đổi các thuộc tính này thành association |
| P04 | UC-009 (bước 5, Mục 8) | Đặc tả không nêu cách xử lý khi chuyến chưa có giá vé cho cặp (tuyến xe, loại xe); P12 ném FareNotFoundException | Thêm luồng thay thế hoặc ghi UC-023 bảo đảm mọi cặp tuyến xe và loại xe đều có giá trước khi bán |

## Vấn đề còn mở

- Target 24 (khớp bảng Node/Edge và file .drawio): XML hợp lệ, toạ độ và điểm uốn là bội số của 10, khoảng cách giữa hai node tối thiểu 40, cạnh không cắt qua node đều đã kiểm bằng chương trình; chưa mở bằng draw.io để xem bằng mắt, nhãn multiplicity và vai trò ở các cạnh ngắn, nhãn chuyển trạng thái dài có thể cần chỉnh.
- Target 6 (vòng đời đầy đủ của lớp persistent): vòng đời đầy đủ chỉ có ở Booking và Ticket trong phạm vi UC-009, UC-017. Tạo, sửa Trip, Seat, Fare thuộc UC-016, UC-021, UC-023, UC-024; chuyển Seat từ SOLD về AVAILABLE và các trạng thái đã trả, đã đổi của Ticket thuộc UC-012, UC-014; tất cả chưa có P07. Không lớp nào có thao tác xoá hay lưu trữ vì nguồn không nêu. Làm khi có P07 của các use case đó.
- Target 12 (lập lịch): UC-009 không có message hẹn hay huỷ mốc; mốc hết thời hạn giữ chỗ dùng cơ chế quét định kỳ của P09 (listExpiredHolds, handleHoldExpiry, F3). Hai trách nhiệm cancelOverdueReservationMark, cancelPassengerListMark của UC-017 thuộc DC-CancelTripService (PKG-16) nên do lần chạy PKG-16 xác định là thao tác hay hệ quả của trạng thái CANCELLED của Trip (ST-01).
- Operation tạm: DC-SearchTripsService (searchTrips, viewSeatMap) và DC-PayTicketOnlineService (payTicketOnline, cancelPayment) chờ P04, P07 của UC-008, UC-010; chữ ký IF-01.collectPayment, cancelPaymentSession, IF-08.save, DC-PaymentTransaction.collected và các kiểu PKG-31 là tạm (bảng Chữ ký interface tạm). Chạy lại P12 cho PKG-13 khi các artifact này có.
- Giao dịch thanh toán thành công đến sau khi hết thời hạn giữ chỗ (BR-06, ASM-22): processTravelerInfo ném HoldExpiredException khi Booking đã SEATS_RELEASED, nhưng việc hoàn tiền khoản thu đến muộn thuộc UC-010 và chưa có operation; xét ở P07 của UC-010.
- Operation public vượt ngưỡng khoảng 15-20: DC-Booking 17 (8 getter) và DC-Ticket 20 (11 getter); đã kiểm tra lại mục đích lớp, giữ vì mỗi getter có bên gọi hoặc để quan sát hậu điều kiện (Bước 2.4). Một số operation chưa có bên gọi trong UC-009, UC-017 nhưng có nguồn Bổ sung: constructor, IF-03.save, IF-04.save, IF-04.findByRouteAndVehicleType dùng cho UC-016, UC-023, UC-024 chờ P07.
- Quan hệ P08 có Lớp A ngoài phạm vi, chưa thiết kế ở lần chạy này: R-01 (PKG-05), R-13 (PKG-07), R-14, R-15, R-16, R-17, R-18 (PKG-16, DC-CancelTripService).
- Các thành phần thuộc package khác dùng ở đây nhưng chưa có thiết kế chi tiết: DC-Money, DC-TicketCode, DC-PhoneNumber (PKG-31), DC-PaymentTransaction, IF-08 (PKG-29), DC-SmsSendResult (PKG-22, P11b). Hợp đồng ở bảng Chữ ký interface tạm.
- Kiểu của view model dùng BigDecimal, String thay vì Money, TicketCode, PhoneNumber vì P09 QT-4 cấm Presentation phụ thuộc Domain; việc đổi Money --> BigDecimal xảy ra ở DC-BookTicketOnlineService khi dựng view model (R-33).
- Chọn nơi lưu trạng thái khi nhiều bản sao ứng dụng: Seat.tripState, Booking.status, Ticket.status cùng thể hiện một sự thật (chỗ đã bán khi có vé hiệu lực, P08 Vấn đề còn mở). P12 chọn Seat.tripState là nguồn cho BR-02 (ràng buộc duy nhất trên (chuyến, chỗ) khi tripState = HELD hoặc SOLD, P13 định nghĩa); Ticket.status là nguồn cho vé; hai nguồn được đổi trong cùng giao dịch ở Booking.issueTickets.
- R-12 (Booking-Trip) và R-19 (Ticket-Trip) suy được qua Seat nhưng được giữ (P08 Vấn đề còn mở): R-12 mang ràng buộc mọi chỗ cùng chuyến (Booking.createBooking kiểm tra), R-19 phục vụ IF-07.findActiveByTrip.
- Booking ở trạng thái SELECTING không được lưu (P07 Vấn đề còn mở dòng 6): quyết định thời điểm lưu là sau holdSeats cùng giao dịch; P13 không cần cột cho SELECTING nhưng enumeration vẫn có giá trị này.
- Số tham số: DC-Ticket.createTicket có 7 tham số và constructor của DC-Trip có 5 (mức khoảng 4 trở lên cần xem xét gom). Đã xét: mọi tham số đều được dùng nên không có stamp coupling; gom thành đối tượng tham số buộc Ticket phụ thuộc Booking, tạo vòng phụ thuộc Booking-Ticket (R-11), hoặc thêm một kiểu trung gian chỉ để chuyền dữ liệu. Giữ nguyên; gom thành đối tượng tham số khi thêm kênh mua vé tại quầy (UC-004, UC-006).
- DC-Booking.holdStartedAt được lưu theo UC-009 bước 5 (ASM-18, GL-20) làm gốc tính thời hạn nhưng không operation nào đọc; holdExpiry là giá trị bộ định thời dùng.
- Tên lớp: DC-TripTicketCancellation đặt theo nghiệp vụ UC-017; nếu UC-012, UC-014 (trả vé, đổi vé) cũng cần thao tác lên tập vé thì đổi tên thành lớp chung khi có P07.
