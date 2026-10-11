# X1 - Review thiết kế - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | X1 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (CHE_DO_GIA_DINH = CO_NHAN; MUC_CHI_TIET = DAY_DU); 00-Conventions.md; P12-class-design/PKG-09-PKG-22-PKG-23-ticket-sales-catalog-ticketing.md 1.0; P13-data-model.md 1.0; P09-architecture.md 1.0; P10-design-elements.md 1.0; P11b-system-interfaces.md 1.0 (phần SS-07, IF-10, IF-11 và các IF mà phạm vi dùng); P07-uc-analysis/UC-002, UC-008, UC-013, UC-015 (1.0); P08-analysis-model.md 1.0; P06-supplementary-spec.md 1.0. Chưa có file X1 cũ. Tham số: PHAM_VI_REVIEW = PKG-09, PKG-22, PKG-23 (P12) và P13 của các package đó; NHOM_TIEU_CHI = Không có; THIET_KE_DOC_LAP = Không có; MA_RV_BAT_DAU = Không có; YEU_CAU_BO_SUNG = cấp mã Q mới từ Q-150 và ASM mới từ ASM-150 vì X2 chạy song song |
| Phạm vi | PKG-09 TicketSalesService, PKG-22 TripCatalog, PKG-23 Ticketing (45 phần tử thiết kế) và mô hình dữ liệu TBL-01 đến TBL-10 của PKG-22, PKG-23 |

## F1. Phạm vi và phương pháp

| Hạng mục | Nội dung |
|---|---|
| Artifact và phiên bản đã review | P12 (một file, 3 package) 1.0; P13 1.0. Đối chiếu với P09 1.0, P10 1.0, P11b 1.0, P07 của UC-002, UC-008, UC-013, UC-015, P08 1.0, P06 1.0 |
| Kiểm tra placeholder (C6) | Đủ. NHOM_TIEU_CHI, THIET_KE_DOC_LAP, MA_RV_BAT_DAU là Không có (áp dụng mặc định: mọi nhóm tiêu chí, review artifact pipeline, bắt đầu RV-01). Không còn khối {{PH:...}} nào chưa thay |
| Phần tử trong phạm vi | 3 package; 45 phần tử thiết kế (3 control, 12 entity, 3 interface, 12 value object, 12 enumeration, 3 exception); 103 operation; 89 thuộc tính; 50 quan hệ R-02 đến R-67; 3 state machine ST-01 đến ST-03; 9 lớp persistent thành 10 bảng TBL-01 đến TBL-10; 13 quan hệ khái niệm ER-01 đến ER-13 |
| Nhóm tiêu chí đã áp dụng | Tất cả: MOD, CPL, COH, SOLID, GRASP, PRN, PKP, SML, CNS, DAT. Chỉ số Ca, Ce, I, A, D ở F6.3 vì MUC_CHI_TIET = DAY_DU |
| Phép thử continuity (MOD) | Ba thay đổi dễ xảy ra: (1) Q-75 trả lời theo hướng trạng thái chỗ suy ra từ vé và đặt chỗ thay vì lưu thành cột; (2) BR-13, BR-14 đổi mức hoàn hoặc thêm bậc thời gian; (3) đổi cổng thanh toán (NFR-06, API chưa có tài liệu, Q-24). Kết quả ở F5 mục MOD |
| Phần không review được | (a) Hai file sơ đồ class và ERD (.drawio) không mở; lấy bảng Node, Edge trong P12 F8 làm nguồn chuẩn (ASM-153). (b) Thân method của DC-TripCatalogRepositoryImpl, DC-TicketingRepositoryImpl (PKG-14) ngoài phạm vi; cách SS-07 gộp hoặc tách câu lệnh ghi dựa trên ASM-151. (c) Hiệu năng thực đo của NFR-01 (chưa có mức đạt, Q-22). (d) Lớp PKG-28 (Money, TicketCode, PhoneNumber, PaymentReference, ngoại lệ kỹ thuật) chưa có P12, chỉ xét qua giao ước ở P12. (e) Glossary P05 và đặc tả P04 không nằm trong đầu vào của X1, nên tiêu chí "Tên dùng đúng glossary" chỉ kiểm qua trích dẫn GL-nn trong P12. (f) Ca của package ngoài phạm vi tính ước lượng (ASM-150) |

## F2. Bảng phát hiện

| RV | Nguyên lý / tiêu chí vi phạm | Phần tử | Bằng chứng | Mức độ | Đề xuất sửa | Bước cần sửa | Nhóm | Độ tin cậy | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| RV-01 | SOLID DIP; PKP ADP cấp lớp; SML Inappropriate intimacy; SML Large class (constructor 8 tham số); GRASP Controller (phình) | DC-BookTicketOnlineService, DC-PayTicketOnlineService, R-03, R-47 | P12 F2, constructor DC-BookTicketOnlineService: "BookTicketOnlineService(tripCatalog: ITripCatalogRepository, ticketing: ITicketingRepository, scheduler: ITriggerScheduler, smsSender: ISmsSender, idGenerator: ITicketingIdGenerator, smsContent: TicketSmsContent, payService: PayTicketOnlineService, clock: Clock)"; constructor DC-PayTicketOnlineService: "PayTicketOnlineService(paymentGateway: IPaymentGateway, ticketing: ITicketingRepository, bookingCompletion: BookTicketOnlineService)". P12 F5: R-47 "cùng R-03 tạo phụ thuộc hai chiều giữa hai control cùng package". Hai constructor đòi nhau nên không dựng được bằng tiêm qua constructor (P12 F5 R-03: "được tiêm qua constructor"). P12 Vấn đề còn mở chấp nhận tạm vì UC-003 chưa phân tích | Cao | Extract Class DC-BookingCompletionService trong PKG-09, nhận completeBooking cùng phần phát hành vé và gửi SMS (smsSender, smsContent, idGenerator, tripCatalog, ticketing). DC-PayTicketOnlineService phụ thuộc DC-BookingCompletionService thay cho DC-BookTicketOnlineService; DC-BookTicketOnlineService chỉ còn phụ thuộc payService, tripCatalog, ticketing, scheduler, idGenerator, clock (6 tham số) và không còn bị DC-PayTicketOnlineService gọi ngược. Bỏ R-47, thêm quan hệ mới tới DC-BookingCompletionService | P12 | DIP | Chắc chắn | Mở |
| RV-02 | CNS Hành vi không bảo vệ trạng thái chuyến đã huỷ (ASM-26, Q-44) | DC-BookTicketOnlineService.searchTrips, getSeatMap, submitBooking, completeBooking; IF-10.findTrips; DC-TripCancellation.cancelTrip | P12 F3: searchTrips lấy "trips = IF-10.findTrips(...)" rồi dựng TripOffer không lọc theo trạng thái; submitBooking bước 1 đến 5 chỉ kiểm TRIP_NOT_FOUND, SEAT_LIMIT_EXCEEDED, SEATS_UNAVAILABLE, thông tin người đi; DC-Trip.areSeatsAvailable chỉ hỏi Seat.isAvailable. P12 F2 DC-TripCancellation.cancelTrip chỉ đổi Trip, Ticket, PhoneReservation; Seat của chuyến đã huỷ giữ AVAILABLE hoặc HELD. P12 F7a TicketSalesRule không có giá trị cho chuyến đã huỷ. P07 UC-013 mục loại lớp, dòng 40: lần đặt giữ chỗ "chờ Q-44". Hệ quả: chuyến CANCELLED vẫn hiện trong kết quả tìm và vẫn nhận lần đặt, thanh toán, phát hành vé | Cao | Thêm Trip.isCancelled vào ba điểm: searchTrips bỏ chuyến CANCELLED, getSeatMap và submitBooking ném giá trị mới TicketSalesRule.TRIP_CANCELLED; completeBooking với chuyến đã huỷ xử lý theo Q-44 (không phát hành vé, ghi nhật ký đối soát như HOLD_EXPIRED). Thêm giá trị TRIP_CANCELLED vào DC-TicketSalesRule | P12 | CNS | Cần xác nhận (thiếu: câu trả lời Q-44 và nội dung ASM-26 về việc chuyến đã huỷ có còn nhận đặt vé; Q-150) | Mở |
| RV-03 | DAT Thiếu cơ chế nhất quán cho cập nhật có điều kiện; CNS cột có nguồn | DC-Trip, DC-Booking, IF-10.saveTrip, IF-11.saveBooking, TBL-04, TBL-05 | P12 F3 handleTrigger bước 4: "Cập nhật có điều kiện theo phiên bản: nếu thanh toán thành công commit trước thì bên này thua". P11b SS07-WB1-M04: "cập nhật có điều kiện từng chỗ và phiên bản chuyến". P12 F7 không có thuộc tính phiên bản ở DC-Trip, DC-Booking; P13 F6.1 TBL-04 chỉ có id, route_id, bus_type, departure_time, status; TBL-05 không có cột phiên bản. Kịch bản: retryPayment đọc Booking HELD rồi gọi payTickets --> IF-11.saveBooking(booking) trong khi handleTrigger đã commit EXPIRED; bản ghi đầy đủ ghi đè status về HELD trong khi các Seat đã được trả | Cao | Introduce khoá lạc quan: thêm thuộc tính version (Long, readOnly) vào DC-Trip và DC-Booking ở P12 F7; thêm cột version INTEGER NOT NULL DEFAULT 0 vào TBL-04, TBL-05 ở P13; IF-10.saveTrip, IF-11.saveBooking ghi kèm điều kiện version và ném PersistenceUnavailableException hoặc ngoại lệ xung đột đã có khi lệch phiên bản | P12 | DAT | Cần xác nhận (thiếu: cách SS-07 hiện thực "cập nhật có điều kiện"; nếu chỉ điều kiện theo status của từng Seat thì bản ghi Booking vẫn chưa được bảo vệ; Q-151) | Mở |
| RV-04 | PRN Law of Demeter; PRN Encapsulation; GRASP Information Expert; SML Shotgun surgery; SML Hidden dependencies (temporal coupling ẩn) | DC-Booking.holdSeats, releaseSeats, issueTickets; DC-Ticket.cancelTicket; DC-Trip.findSeats; DC-Seat; R-23, R-27, R-30; DC-BookTicketOnlineService.handleTrigger, completeBooking; DC-ReturnTicketService.confirmReturn | P12 F3 DC-Booking.holdSeats: "seats = trip.findSeats(mã chỗ của travelerInfos). 3. Với mỗi Seat: seat.hold()"; releaseSeats: "Với mỗi Seat trong seats: seat.release()"; issueTickets: "seat.markSold()"; DC-Ticket.cancelTicket: "3. seat.release()". P12 F5 R-23: Seat là Composition của Trip ("Seat không tồn tại ngoài chuyến"), nhưng Booking (R-27) và Ticket (R-30) điều khiển trực tiếp trạng thái Seat qua đối tượng trả về từ Trip.findSeats. Dịch vụ phải nhớ ghi hai nơi: handleTrigger bước 4 "IF-10.saveTrip(booking.getTrip()); IF-11.saveBooking(booking)", completeBooking bước 4, confirmReturn bước 5 "IF-10.saveTrip(ticket.getTrip())". Continuity (1): nếu Q-75 trả lời trạng thái chỗ suy ra thì phải sửa Seat, Trip, Booking, Ticket, IF-10 và TBL-08 (4 lớp, 1 interface, 1 bảng). Mức gốc Trung bình, nâng một mức vì Q-75 còn mở | Cao | Hide Delegate và Move Method: Trip thành chủ duy nhất của ST-03 với Trip.holdSeats(seatCodes: List<String>, bookingId: String, now: LocalDateTime), Trip.releaseSeats(seatCodes: List<String>), Trip.markSeatsSold(seatCodes: List<String>); Booking giữ danh sách mã chỗ và gọi các operation này qua R-26; Ticket.cancelTicket gọi Trip.releaseSeats với mã chỗ của vé qua R-29; bỏ Trip.findSeats khỏi public; các operation của Seat đổi sang package-private. Bỏ điều hướng Booking --> Seat (R-27) và Ticket --> Seat (R-30) khỏi lớp, giữ mã chỗ làm thuộc tính | P12 | PRN | Chắc chắn | Mở |
| RV-05 | CPL Common coupling (bảng dùng chung hai chủ ghi); DAT Ràng buộc kiểm tra không thoả khi ghi từng phần | IF-10.saveTrip, IF-11.saveBooking, IF-11.saveTripCancellation, TBL-04, TBL-08.status, TBL-08.holding_booking_id, ck_seat_hold | P13 F2: DC-TripCancellation "việc ghi do IF-11.saveTripCancellation thực hiện trên TBL-04, TBL-09, TBL-07" trong khi P11b mô tả IF-10.saveTrip ghi "chuyến cùng trạng thái các chỗ đã đổi ... hoặc trạng thái chuyến": TBL-04 có hai chủ ghi. P13 F6.1 TBL-08: "ck_seat_hold: (status = 'HELD') = (holding_booking_id IS NOT NULL)" và holding_booking_id lấy từ R-27 (Booking --> Seat), trong khi P12 F7 DC-Seat chỉ có seatCode, status. P12 F3 submitBooking bước 7: "IF-10.saveTrip(trip) ... rồi IF-11.saveBooking(booking)": cột status do IF-10 ghi, cột holding_booking_id do IF-11 ghi, CHECK của PostgreSQL kiểm sau từng câu lệnh nên lần ghi trước vi phạm ck_seat_hold. Tương tự completeBooking (SOLD còn holding_booking_id) và handleTrigger (AVAILABLE còn holding_booking_id) | Cao | Một chủ ghi cho mỗi bảng: thêm thuộc tính holdingBookingId (String, 0..1) vào DC-Seat, đặt bởi hold(bookingId) và xoá bởi release, markSold, để IF-10.saveTrip ghi status và holding_booking_id trong cùng một UPDATE có điều kiện (kết hợp RV-04). Sửa mô tả IF-11.saveTripCancellation chỉ ghi vé và đặt chỗ (TBL-09, TBL-07); DC-CancelTripService gọi IF-10.saveTrip(trip) và IF-11.saveTripCancellation trong cùng giao dịch của nó | P11b | CPL | Cần xác nhận (thiếu: thứ tự và số câu lệnh SQL mà DC-TripCatalogRepositoryImpl, DC-TicketingRepositoryImpl thực hiện, ASM-151; Q-152) | Mở |
| RV-06 | CPL Control coupling (giá trị null làm cờ); SML Primitive obsession | DC-ReturnTicketService.startReturnTicket, confirmReturn; IF-11.findTicket | P12 F2 startReturnTicket: "travelerPhone là null khi nhân viên bán vé trả vé tại quầy (ASM-18)"; IF-11.findTicket: "khi travelerPhone khác null, khớp số điện thoại người đi". Không có tiền điều kiện buộc travelerPhone khác null khi requestChannel là ONLINE, nên yêu cầu trực tuyến truyền null sẽ tra vé chỉ bằng mã vé, bỏ bước đối chiếu số điện thoại. requestChannel và null của travelerPhone cùng mang một ý (quầy) | Trung bình | Replace Parameter with Explicit Methods: IF-11.findTicket(ticketCode, travelerPhone) bỏ nghĩa null và thêm IF-11.findTicketByCode(ticketCode); DC-ReturnTicketService tách startReturnTicketOnline(ticketCode, travelerPhone) và startReturnTicketAtCounter(ticketCode) (confirmReturn tương tự), bỏ tham số requestChannel khỏi chữ ký công khai (kênh suy từ operation) | P11b | CPL | Chắc chắn | Mở |
| RV-07 | CPL Control coupling (refundMethod rẽ nhánh trong entity); PRN DRY | DC-Ticket.cancelTicket, DC-Ticket.recordRefund | P12 F3 DC-Ticket.cancelTicket: "4. outcome = refundMethod là VIA_GATEWAY ? REFUNDED : AWAITING_CASH_PAYOUT"; cùng lúc DC-Ticket.recordRefund(refundRatePercent, refundAmount, refundMethod, refundOutcome) nhận outcome do dịch vụ xác định (P12 F2: "với kết quả hoàn do dịch vụ xác định (ASM-48)"). Hai cách xác định refundOutcome ở hai operation của cùng một lớp | Trung bình | Thêm tham số refundOutcome vào DC-Ticket.cancelTicket(refundRatePercent, refundAmount, refundMethod, refundOutcome); DC-ReturnTicketService truyền REFUNDED (cổng xác nhận) hoặc AWAITING_CASH_PAYOUT (tiền mặt), bỏ nhánh theo refundMethod trong Ticket. Cập nhật F3, F4 dòng UC-008 msg 2.1.3 | P12 | CPL | Chắc chắn | Mở |
| RV-08 | SML Feature envy; SML Message chains; SML Middle man; CPL Stamp coupling; PRN Law of Demeter | DC-TicketReturnPolicy (matchesPurchaseChannel, getTimeToDeparture, calculateRefundAmount), DC-TicketSmsContent.getTicketSmsContent, DC-Ticket (7 getter), R-62, R-63 | P12 F3 DC-TicketReturnPolicy: getTimeToDeparture "trả ticket.getTrip().calculateTimeToDeparture(requestTime)"; calculateRefundAmount "amount = ticket.getPrice().percent(rate)" (chỉ dùng giá); matchesPurchaseChannel(ticket, requestChannel) chỉ dùng kênh mua; DC-TicketSmsContent.getTicketSmsContent "schedule = ticket.getTrip().getRouteAndDepartureTime()". P12 F2 DC-Ticket có getTicketCode, getTravelerName, getTravelerPhone, getPrice, getPurchaseChannel, getSeatCode, getTrip với nguồn "Bổ sung: DC-TicketReturnPolicy, DC-TicketSmsContent". Đánh đổi: Information Expert muốn đặt logic vào Ticket, High Cohesion/SRP (P10 F3) tách quy tắc trả vé và nội dung SMS ra. Giữ phương án tách | Trung bình | Giữ ba lớp Ticket, TicketReturnPolicy, TicketSmsContent; thu hẹp kênh phụ thuộc: Hide Delegate thêm DC-Ticket.calculateTimeToDeparture(requestTime) và DC-Ticket.getRouteAndDepartureTime(); DC-TicketReturnPolicy.calculateRefundAmount(price: Money, timeToDeparture: Duration) và matchesPurchaseChannel(ticketChannel: PurchaseChannel, requestChannel: PurchaseChannel); Remove Middle Man bỏ DC-TicketReturnPolicy.getTimeToDeparture (dịch vụ gọi Ticket.calculateTimeToDeparture). Bỏ getTrip khỏi bề mặt công khai của Ticket nếu không còn bên gọi ngoài PKG-09 | P12 | PRN | Chắc chắn | Mở |
| RV-09 | PRN DRY; SML Primitive obsession; CPL External coupling (định dạng chuỗi requestKey) | DC-Booking.startPaymentAttempt, DC-PayTicketOnlineService.receivePaymentResult, IF-01.requestPayment, IF-02.receivePaymentResult | P12 F2 DC-Booking.startPaymentAttempt: "trả khoá yêu cầu <bookingId>-<số lần>"; P12 F3 receivePaymentResult bước 2: "bookingId = phần của requestKey trước dấu gạch nối cuối". Tri thức về định dạng khoá nằm ở hai lớp; P12 Đề xuất sửa P11b cũng chỉ ghi định dạng ở dạng văn bản. P13 TBL-05.id VARCHAR(36) "dự phòng cho UUID" nên mã có thể chứa dấu gạch nối. Continuity (3): đổi cổng thanh toán hoặc định dạng khoá phải sửa Booking và PayTicketOnlineService | Trung bình | Introduce Value Object DC-PaymentRequestKey trong PKG-28 với PaymentRequestKey.of(bookingId, attempt), parse(raw: String) và bookingId(); Booking.startPaymentAttempt trả PaymentRequestKey; DC-PayTicketOnlineService dùng PaymentRequestKey.parse(requestKey).bookingId(); chữ ký IF-01, IF-02 giữ String ở biên (toString) | P10 | PRN | Chắc chắn | Mở |
| RV-10 | SML Primitive obsession; CPL External coupling (định dạng nhãn tuyến) | IF-10.findTrip, DC-Route.getDisplayName | P12 F1, ghi chú IF-10: "Tham số route của findTrip là nhãn <Điểm đi> - <Điểm đến> (Đề xuất sửa P11b)"; P12 F2 DC-Route.getDisplayName tạo nhãn đó; P13 ASM-108 phải giả định "Mỗi cặp (điểm đi, điểm đến) là đúng một tuyến" để nhãn xác định một tuyến. Bên gọi (PKG-10, PKG-11) và repository phải cùng hiểu định dạng ghép, tên điểm chứa " - " sẽ tách sai | Trung bình | Đổi IF-10.findTrip(departurePoint: String, arrivalPoint: String, departureDateTime: DateTime): Trip (hoặc nhận routeId) ở P11b F3; cập nhật sequence UC-013, UC-015 của SS-07; DC-Route.getDisplayName chỉ còn dùng để hiển thị | P11b | SML | Chắc chắn | Mở |
| RV-11 | SOLID OCP; CPL Control coupling (kind của TriggerReference) | DC-BookTicketOnlineService.handleTrigger, IF-08 | P12 F2 handleTrigger: ném "IllegalArgumentException (kind khác HOLD_EXPIRY)"; P12 F2a: "kind khác HOLD_EXPIRY thì ném IllegalArgumentException (chờ Đề xuất sửa P10 về bộ định tuyến theo kind)" và "SS-05 coi là lỗi xử lý, giao lại"; P12 F2a dòng 2 nêu mốc UC-006 (60 phút), UC-014 (15 phút) sẽ thêm. Một bên hiện thực IF-08 phải biết mọi kind; mốc có kind lạ bị giao lại mãi. Không nâng mức vì P12 đã có đề xuất P10 | Trung bình | Replace Conditional with Polymorphism: SS-05 giữ ánh xạ TriggerKind --> ITriggerHandler, mỗi dịch vụ đăng ký handler cho kind của mình; DC-BookTicketOnlineService chỉ hiện thực handler cho HOLD_EXPIRY và bỏ nhánh kiểm kind; kind chưa có handler thì SS-05 ghi nhật ký và đánh dấu đã xử lý thay vì giao lại | P10 | SOLID | Chắc chắn | Mở |
| RV-12 | SML Long parameter list (7); SML Data clumps; CNS Bất biến quan hệ không được kiểm | DC-Trip constructor, DC-BaseFare constructor, R-22, R-24, R-31 | P12 F2 DC-Trip: "Trip(tripId: String, route: Route, departureTime: LocalDateTime, busType: BusType, baseFare: BaseFare, holidaySurcharge: HolidaySurcharge, seatCodes: List<String>)" với Tiền: "seatCodes không rỗng, mã không trùng"; DC-BaseFare: "BaseFare(baseFareId, busType, amount, route)". Chuyến mang route, busType và baseFare, trong khi baseFare đã mang route (R-31) và busType, nên có thể truyền cặp không khớp và giá vé sai (BR-04, BR-05). P13 F4.2 R-24 chỉ chặn ở CSDL bằng khoá ngoại ghép | Trung bình | Bỏ tham số busType (Trip.busType lấy từ baseFare.busType); thêm kiểm tra trong constructor: baseFare.route phải trùng route, nếu không ném IllegalArgumentException; thêm vào Tiền điều kiện. Giữ tập chỗ tạo từ seatCodes | P12 | SML | Chắc chắn | Mở |
| RV-13 | CNS Ranh giới giao dịch của việc hoàn tiền | DC-ReturnTicketService.confirmReturn, IF-01.requestRefund | P12 F3 confirmReturn bước 4, 5: hoàn qua cổng trước, sau đó "Giao dịch T1: ticket.cancelTicket ...; commit"; "Nếu bước 5 lỗi sau khi cổng đã hoàn thì ghi nhật ký requestKey để đối soát bằng IF-01.queryRefundStatus (Q-55, Q-104)"; requestKey cố định "'refund-' + mã vé". P06 NFR-07 ghi API hoàn tiền "chưa có tài liệu (Q-24)". Nếu T1 lỗi, vé vẫn ISSUED dù tiền đã hoàn; lần gọi confirmReturn kế tiếp chỉ an toàn khi cổng coi cùng requestKey là cùng yêu cầu | Trung bình | Ghi vào thiết kế yêu cầu bắt buộc: confirmReturn gọi lặp với cùng ticketCode phải an toàn; SS-01 (IF-01.requestRefund) trả kết quả của lần hoàn trước khi nhận lại cùng requestKey (cập nhật mô tả IF-01 ở P11b); thêm vào F3 bước 5 việc thử lại giao dịch T1 có giới hạn trước khi ghi nhật ký đối soát | P12 | CNS | Cần xác nhận (thiếu: cổng thanh toán có trả kết quả cũ khi gọi lại cùng requestKey hay không; Q-154) | Mở |
| RV-14 | CNS Dữ liệu cần bảo vệ (P09 F7) chưa có biện pháp ở operation đọc | DC-BookTicketOnlineService.getBookingStatus, getIssuedTickets, IF-15.nextBookingId | P12 F2 getIssuedTickets(bookingId: String): BookingSummary trả "các vé đã phát hành" (DC-BookingSummary.tickets gồm họ tên, số điện thoại, mã vé theo F7); không có tham số nào chứng minh quyền. P13 TBL-05.id: "mã do IF-15 cấp bằng dãy số của CSDL, dạng chuỗi" nên bookingId đoán được. P09 F7 "Dữ liệu cần bảo vệ: Họ tên và số điện thoại người đi, mã vé". Mã vé lấy được dùng tiếp ở trả vé cùng số điện thoại | Trung bình | Đổi hiện thực IF-15.nextBookingId thành mã ngẫu nhiên khó đoán (UUID, VARCHAR(36) của TBL-05.id đã đủ) và ghi thành bất biến trong mô tả IF-15; getBookingStatus, getIssuedTickets chỉ chấp nhận mã đó | P12 | CNS | Cần xác nhận (thiếu: PKG-08 có xác thực hoặc phiên cho hành khách khách vãng lai hay không; Q-153) | Mở |
| RV-15 | CNS Ràng buộc liên bảng P13 mâu thuẫn hành vi P12 | P13 F4.2 (ràng buộc seat.status), DC-Ticket.cancelWithTrip, DC-TripCancellation.cancelTrip | P13 F4.2: "seat.status = 'SOLD' khi và chỉ khi chỗ có vé ISSUED". P12 F2 DC-Ticket.cancelWithTrip: "chỉ đổi status, không đụng chỗ (ASM-26, Q-44)" và F3 DC-TripCancellation.cancelTrip không gọi Seat. Sau khi huỷ chuyến, vé CANCELLED nhưng Seat vẫn SOLD, trái ràng buộc đã ghi | Trung bình | Sửa P13 F4.2: "seat.status = 'SOLD' khi và chỉ khi chỗ có vé ISSUED, áp dụng cho chuyến ACTIVE"; ghi rõ chuyến CANCELLED không ràng buộc trạng thái chỗ | P13 | CNS | Chắc chắn | Mở |
| RV-16 | PRN DRY | DC-BaseFare.calculateTicketPrice, DC-HolidaySurcharge constructor, DC-RefundQuote.ratePercent, DC-ReturnQuote.refundRatePercent, DC-TicketReturnPolicy | P12 F2 DC-BaseFare.calculateTicketPrice Tiền: "surchargeRatePercent trong 0..30 (BR-32)" và DC-HolidaySurcharge constructor ném lỗi khi "ratePercent ngoài 0..30" (BR-32). P12 F7: DC-RefundQuote.ratePercent {50 hoặc 90}, DC-ReturnQuote.refundRatePercent {50 hoặc 90} trong khi mức hoàn nằm ở hằng HIGH_RATE_PERCENT, LOW_RATE_PERCENT của DC-TicketReturnPolicy (BR-13, BR-14). Continuity (2): đổi mức hoàn phải sửa ba nơi | Thấp | Introduce Value Object DC-SurchargeRate (PKG-22) kiểm 0..30 một lần, BaseFare.calculateTicketPrice nhận DC-SurchargeRate; bỏ ràng buộc {50 hoặc 90} khỏi hai value object và để DC-TicketReturnPolicy là nơi duy nhất biểu diễn mức hoàn | P12 | PRN | Chắc chắn | Mở |
| RV-17 | PKP CRP/CCP (lớp dùng chung đặt sai package) | DC-InvalidStateException | P12 F1: "Đặt ở PKG-22 vì PKG-23 đã phụ thuộc PKG-22 (P09 R8)"; mô tả "bộ ngoại lệ chung cho các state machine ST-01 đến ST-03". PKG-23 và sau này PKG-24 phụ thuộc PKG-22 để dùng một ngoại lệ không liên quan tuyến, chuyến, giá. P11b F5 đặt DC-PersistenceUnavailableException (cũng dùng chung) ở PKG-28 | Thấp | Move Class DC-InvalidStateException sang PKG-28 SharedValueTypes; cập nhật P10 F4 | P10 | PKP | Chắc chắn | Mở |
| RV-18 | CNS Stereotype không khớp vai trò | DC-TicketReturnPolicy, DC-TicketSmsContent, DC-TripCancellation | P12 F1: ba lớp ghi «entity» với Persistent "Không"; ghi chú "dịch vụ miền không có trạng thái"; DC-TripCancellation "Không có thuộc tính". P13 F2 xếp cả ba là không persistent | Thấp | Đổi stereotype thành «domain service» (ghi vào quy ước stereotype của P12) cho ba lớp | P12 | CNS | Chắc chắn | Mở |
| RV-19 | PRN Program to an interface (entity gọi hạ tầng); CNS Ngoại lệ khai báo thiếu | DC-Booking.issueTickets, IF-15, R-64 | P12 F2 DC-Booking.issueTickets(paymentReference, idGenerator: ITicketingIdGenerator) có cột Ngoại lệ chỉ "InvalidStateException"; IF-15.nextTicketCode có Ngoại lệ "PersistenceUnavailableException". F3: Booking gọi "IF-15.nextTicketCode" trong vòng lặp nên một entity miền chạm tới dãy số CSDL và có thể ném lỗi kỹ thuật không khai báo | Thấp | Replace Parameter: DC-BookTicketOnlineService gọi IF-15.nextTicketCode() theo số chỗ rồi truyền List<TicketCode> vào DC-Booking.issueTickets(paymentReference, ticketCodes); bỏ R-64 | P12 | PRN | Chắc chắn | Mở |
| RV-20 | CNS State machine (trạng thái cụt) | DC-Refund, DC-RefundOutcome.FAILED, AWAITING_CASH_PAYOUT | P12 F1 DC-Refund: "Không có state machine: ... xử lý lại hoàn chưa thành công thuộc use case chưa có"; P12 F7a RefundOutcome có FAILED, AWAITING_CASH_PAYOUT; P12 F2 DC-Refund chỉ có createRefund. Khoản hoàn FAILED hoặc chờ chi tiền mặt không có operation chuyển sang REFUNDED | Thấp | Khi use case xử lý lại được phân tích: thêm DC-Refund.markRefunded(): void (FAILED hoặc AWAITING_CASH_PAYOUT --> REFUNDED) và state machine ST-04; trước đó thêm ràng buộc {readOnly} cho refundOutcome để không để ngỏ | P12 | CNS | Cần xác nhận (thiếu: use case nào chi tiền mặt và xử lý lại hoàn thất bại; Q-155) | Mở |
| RV-21 | DAT Truy vấn thường xuyên theo NFR (nạp dư dữ liệu) | IF-10.findTrips, DC-Trip.countAvailableSeats, TBL-08 | P12 F3 searchTrips: "Với mỗi chuyến dựng TripOffer(... countAvailableSeats() ...)"; DC-Trip.countAvailableSeats "đếm Seat có isAvailable()": phải nạp cả tập Seat (40 chỗ theo GL-21) của mỗi chuyến chỉ để lấy một số đếm. P06 NFR-01: "khoảng 2.000 người truy cập cùng lúc vào dịp Tết", chưa có mức đạt (Q-22). P12 F1 chủ động không tách nạp muộn "vì chưa có NFR đo được" | Thấp | Nếu đo tải (ASM-40) không đạt: thêm IF-10.countAvailableSeats(tripIds: List<String>): Map<String, Integer> thực hiện một truy vấn COUNT theo pk_seat (trip_id), searchTrips dùng cho TripOffer và Trip.countAvailableSeats vẫn dùng ở miền | P11b | DAT | Cần xác nhận (thiếu: mức đạt thời gian phản hồi của NFR-01; Q-156) | Mở |

## F3. Đánh giá coupling

| Phần tử A (phụ thuộc) | Phần tử B (được dùng) | Kênh phụ thuộc | Mức coupling | Bằng chứng | Chấp nhận (Có / Không: RV) |
|---|---|---|---|---|---|
| DC-BookTicketOnlineService | DC-PayTicketOnlineService | thuộc tính payService (R-03); tham số payTickets(booking: Booking) | Stamp | P12 F2: payTickets chỉ dùng Booking.startPaymentAttempt, getTotalAmount trong 15 operation của Booking | Không: RV-01 |
| DC-PayTicketOnlineService | DC-BookTicketOnlineService | thuộc tính bookingCompletion (R-47) | Data (tạo vòng phụ thuộc lớp) | P12 F2 constructor; F5 R-47 | Không: RV-01 |
| DC-PayTicketOnlineService | DC-Booking | tham số booking (R-67); chuỗi requestKey | External coupling (định dạng requestKey) | P12 F3 receivePaymentResult bước 2 | Không: RV-09 |
| DC-ReturnTicketService | IF-11 | tham số travelerPhone (null nghĩa là không lọc) | Control | P12 F2 startReturnTicket, IF-11.findTicket | Không: RV-06 |
| DC-ReturnTicketService | DC-Ticket | tham số refundMethod của cancelTicket (R-10) | Control | P12 F3 cancelTicket bước 4 | Không: RV-07 |
| SS-05 (qua IF-08, R-43) | DC-BookTicketOnlineService | tham số reference.kind của handleTrigger | Control | P12 F2a, F2 handleTrigger | Không: RV-11 |
| DC-TicketReturnPolicy | DC-Ticket | tham số ticket (R-62) | Stamp | calculateRefundAmount chỉ dùng giá; matchesPurchaseChannel chỉ dùng kênh mua | Không: RV-08 |
| DC-TicketReturnPolicy<br>DC-TicketSmsContent | DC-Trip | giá trị trả về của Ticket.getTrip() | Data (vi phạm Law of Demeter) | P12 F3: "ticket.getTrip().calculateTimeToDeparture(requestTime)", "ticket.getTrip().getRouteAndDepartureTime()" | Không: RV-08 |
| DC-Booking | DC-Seat | thuộc tính seats (R-27); giá trị trả về của Trip.findSeats | Data (vi phạm Law of Demeter, vượt qua Trip) | P12 F3 holdSeats, releaseSeats, issueTickets | Không: RV-04 |
| DC-Ticket | DC-Seat | thuộc tính seat (R-30) | Data (điều khiển phần của Trip) | P12 F3 cancelTicket bước 3 | Không: RV-04 |
| DC-Trip | DC-Route<br>DC-BaseFare | thuộc tính route, baseFare (R-22, R-24); constructor | Data (bất biến baseFare.route = route chưa kiểm) | P12 F2 constructor DC-Trip | Không: RV-12 |
| DC-Booking | IF-15 | tham số idGenerator của issueTickets (R-64) | Data (entity gọi hạ tầng) | P12 F2 DC-Booking.issueTickets | Không: RV-19 |
| IF-11 (SS-07 hiện thực) | TBL-04 trip | dữ liệu dùng chung: saveTripCancellation ghi chuyến đã huỷ | Common | P13 F2 DC-TripCancellation; P11b IF-10.saveTrip cũng ghi trạng thái chuyến | Không: RV-05 |
| IF-10, IF-11 (SS-07 hiện thực) | TBL-08 seat | dữ liệu dùng chung: status do IF-10, holding_booking_id do IF-11 (R-27) | Common | P13 F6.1 TBL-08 ck_seat_hold | Không: RV-05 |
| DC-CancelTripService (PKG-10)<br>DC-CheckBoardingTicketService (PKG-11) | IF-10 | tham số route của findTrip (nhãn chuỗi) | External coupling (định dạng nhãn tuyến) | P12 F1 ghi chú IF-10 | Không: RV-10 |
| DC-BookTicketOnlineService | IF-10<br>IF-11<br>IF-07<br>IF-15<br>IF-03<br>DC-TicketSmsContent<br>java.time.Clock | thuộc tính qua constructor (R-38, R-39, R-40, R-41, R-02, R-42, R-51) | Data | scheduleTrigger(kind, targetId, groupId, dueAt); sendSms(recipient, content, messageKey): chỉ truyền dữ liệu nguyên tố hoặc đối tượng dùng trọn | Có |
| DC-BookTicketOnlineService | DC-Trip<br>DC-Booking<br>DC-Ticket | biến cục bộ (R-04, R-05, R-06) | Data | P12 F5: nạp từ IF-10, IF-11 hoặc tạo bằng Booking.createBooking trong từng method | Có |
| DC-PayTicketOnlineService | IF-01<br>IF-11 | thuộc tính (R-44, R-45) | Data | requestPayment(requestKey, totalAmount) | Có |
| DC-PayTicketOnlineService | IF-02 | Realization (R-46) | Data | receivePaymentResult(requestKey, outcome, paymentReference, amount): bốn dữ liệu nguyên tố | Có |
| DC-ReturnTicketService | IF-01<br>IF-10<br>IF-11<br>DC-TicketReturnPolicy<br>java.time.Clock | thuộc tính (R-09, R-49, R-48, R-50, R-52) | Data | requestRefund(ticketCode, amount, requestKey) | Có |
| DC-Trip | DC-Seat<br>DC-HolidaySurcharge | thuộc tính (R-23, R-25) | Data | Seat.isAvailable(); getSurchargeRate(departureDate) | Có |
| DC-BaseFare | DC-Route | thuộc tính (R-31) | Data | khoá tuyến của mức giá | Có |
| DC-Booking | DC-Trip<br>DC-Ticket | thuộc tính (R-26, R-28) | Data | Trip.determineTicketPrice(); Ticket.createTicket(...) | Có |
| DC-Ticket | DC-Trip<br>DC-Refund | thuộc tính (R-29, R-32) | Data | Trip.calculateTimeToDeparture(requestTime) qua Ticket; Refund.createRefund(...) | Có |
| DC-PhoneReservation | DC-Trip<br>DC-Seat | thuộc tính (R-33 điều hướng B --> A, R-37) | Data | P12 F5; R-37 chờ Q-76 | Có |
| DC-TripCancellation | DC-Trip<br>DC-Ticket<br>DC-PhoneReservation<br>DC-TicketReturnPolicy | thuộc tính (R-58, R-59, R-60, R-61) | Data | markCancelled(); cancelWithTrip(); isUnpaid(); getCancelImpactInfo(ticket) | Có |
| IF-10 | DC-Trip<br>DC-SeatAlreadyHeldException | tham số, kiểu trả về, ném ngoại lệ (R-53, R-66) | Data | saveTrip(trip: Trip): void; Trip là khái niệm trọn vẹn mà kho lưu hết | Có |
| IF-11 | DC-Booking<br>DC-Ticket<br>DC-PhoneReservation<br>DC-TripCancellation | tham số, kiểu trả về (R-54, R-55, R-56, R-57) | Data | đối tượng trọn vẹn do kho lưu; stamp chấp nhận được | Có |
| DC-TicketSmsContent | DC-Ticket | tham số (R-63) | Data | dùng mã vé, mã chỗ, họ tên, chuyến của vé (phần lớn); chuỗi getTrip xem RV-08 | Có |
| DC-Seat | DC-SeatAlreadyHeldException | ném ngoại lệ (R-65) | Data | Seat.hold() | Có |

## F4. Đánh giá cohesion

| Phần tử (PKG / DC / DC.operation) | Mức cohesion | Lý do (nhóm phần tử và lý do đặt cùng nhau) | Chấp nhận (Có / Không: RV) |
|---|---|---|---|
| PKG-09 TicketSalesService | Functional | Ba dịch vụ của UC-002, UC-003, UC-008 cùng value object và ngoại lệ của chúng; thay đổi cùng nhóm chức năng bán vé (CCP đạt) | Có |
| PKG-22 TripCatalog | Communicational | Hai nhóm đổi theo hai lý do: lịch chạy và chỗ (Trip, Route, Seat) với giá vé (BaseFare, HolidaySurcharge, UC-016, UC-017); PKG-11 chỉ dùng Trip nhưng phụ thuộc cả package. Chấp nhận vì 5 lớp nhỏ và có quan hệ R-22 đến R-25 | Có |
| PKG-23 Ticketing | Communicational | Booking, Ticket, Refund, PhoneReservation cùng vòng đời vé; TripCancellation, TicketReturnPolicy, TicketSmsContent là dịch vụ miền kèm theo | Có |
| DC-BookTicketOnlineService | Procedural | Gom theo thứ tự use case UC-002 (tìm chuyến, giữ chỗ, hết hạn, hoàn tất) trên dữ liệu khác nhau; phần hoàn tất lần đặt và SMS là trách nhiệm tách được | Không: RV-01 |
| DC-PayTicketOnlineService | Functional | Gửi yêu cầu thanh toán và nhận kết quả: một trách nhiệm về thanh toán lần đặt | Có (vòng phụ thuộc: RV-01) |
| DC-ReturnTicketService | Sequential | UC-008: nhận diện, kiểm tra, hoàn tiền, huỷ vé; đầu ra bước trước là đầu vào bước sau | Có |
| DC-BookTicketOnlineService.submitBooking | Sequential | Mười bước nối tiếp từ lập lần đặt tới gửi yêu cầu thanh toán, mỗi bước dùng kết quả bước trước; ranh giới giao dịch T1 rõ | Có |
| DC-ReturnTicketService.confirmReturn | Sequential | Kiểm tra lại, tính tiền, hoàn tiền, huỷ vé theo chuỗi | Có |
| DC-TripOffer | Functional | Gói một chuyến khớp tiêu chí để hiển thị | Có |
| DC-BookingHold | Functional | Gói kết quả giữ chỗ | Có |
| DC-ReturnQuote | Functional | Gói báo giá trả vé | Có |
| DC-ReturnReceipt | Functional | Gói kết quả trả vé | Có |
| DC-TicketSalesRuleException | Functional | Báo từ chối nghiệp vụ kèm lý do | Có |
| DC-TicketSalesRule | Logical | 13 lý do của hai use case khác nhau (UC-002 và UC-008) trong một enumeration, bên gọi chọn bằng giá trị. Là bộ mã lỗi chung chấp nhận được; theo dõi khi UC-003, UC-007 thêm lý do | Có |
| DC-Trip | Communicational | Bốn nhóm operation trên các thuộc tính rời nhau: chỗ (seats), giá (baseFare, holidaySurcharge), thời gian (departureTime), trạng thái (status). Mỗi nhóm mỏng (1 đến 4 operation) và chỉ ủy quyền, nên không tách; khi RV-04 thêm thao tác chỗ cần xem lại | Có |
| DC-Route | Functional | Dữ liệu và tên hiển thị của tuyến | Có |
| DC-Seat | Functional | Vòng đời trạng thái một chỗ (ST-03) | Có |
| DC-BaseFare | Functional | Mức giá và cách tính giá một vé | Có |
| DC-HolidaySurcharge | Functional | Khoảng ngày và mức tăng | Có |
| DC-TripSchedule | Functional | Tuyến và giờ xuất bến | Có |
| DC-TripStatus | Functional | Tập giá trị trạng thái chuyến | Có |
| DC-SeatStatus | Functional | Tập giá trị trạng thái chỗ | Có |
| DC-BusType | Functional | Tập giá trị loại xe | Có |
| IF-10 ITripCatalogRepository | Functional | Bốn operation tìm và ghi chuyến | Có |
| DC-SeatAlreadyHeldException | Functional | Báo chỗ đã bị giữ | Có |
| DC-InvalidStateException | Functional | Ngoại lệ trạng thái; vị trí package xem RV-17 | Không: RV-17 |
| DC-Booking | Sequential | Vòng đời lần đặt DRAFT --> HELD --> TICKETED, EXPIRED; phần payment (paymentAttemptCount, startPaymentAttempt) nhỏ và Tạm theo ASM-100 | Có |
| DC-Ticket | Sequential | Vòng đời vé ISSUED, Checked, CANCELLED cùng kết quả soát; mọi operation đọc hoặc đổi status, checkedTime | Có |
| DC-TicketReturnPolicy | Communicational | Hai nhóm hằng rời nhau: MIN_RETURN_TIME, FULL_RATE_TIME, HIGH_RATE_PERCENT, LOW_RATE_PERCENT (trả vé, BR-12 đến BR-14) và TRIP_CANCEL_RATE_PERCENT (huỷ chuyến, BR-17); cùng chủ đề hoàn tiền của vé. Chấp nhận, xem RV-08 về kênh phụ thuộc | Có |
| DC-TicketSmsContent | Functional | Lập nội dung và khoá chống gửi trùng của SMS | Có |
| DC-TripCancellation | Sequential | Tổng hợp rồi huỷ chuyến, vé, đặt chỗ | Có |
| DC-Refund | Functional | Dữ liệu một khoản hoàn bất biến | Có (trạng thái cụt: RV-20) |
| DC-PhoneReservation | Functional | Đặt chỗ qua điện thoại; mới có 3 operation vì UC-004 đến UC-006 chưa phân tích (theo dõi Lazy class khi các UC đó có P07) | Có |
| IF-11 ITicketingRepository | Communicational | Bảy operation trên ba khái niệm (lần đặt, vé, đặt chỗ) cùng một đơn vị huỷ chuyến; mỗi bên gọi dùng 2 đến 4 operation | Có |
| IF-15 ITicketingIdGenerator | Functional | Cấp mã lần đặt và mã vé | Có |
| DC-TravelerInfo | Functional | Gói thông tin một người đi | Có |
| DC-BookingSummary | Functional | Gói vé đã phát hành và tổng tiền | Có |
| DC-TicketCheckResult | Functional | Gói kết luận soát vé | Có |
| DC-RefundQuote | Functional | Gói mức hoàn và số tiền hoàn | Có |
| DC-TicketReturnInfo | Functional | Gói thông tin vé khi trả | Có |
| DC-CancelImpactInfo | Functional | Gói kênh mua và số tiền hoàn | Có |
| DC-CancellationSummary | Functional | Gói số liệu trước khi huỷ chuyến | Có |
| DC-BookingStatus | Functional | Tập giá trị trạng thái lần đặt | Có |
| DC-TicketStatus | Functional | Tập giá trị trạng thái vé | Có |
| DC-PurchaseChannel | Functional | Tập giá trị kênh mua | Có |
| DC-RefundMethod | Functional | Tập giá trị hình thức hoàn | Có |
| DC-RefundOutcome | Functional | Tập giá trị kết quả hoàn | Có |
| DC-PhoneReservationStatus | Functional | Tập giá trị trạng thái đặt chỗ | Có |
| DC-TravelerInfoProblem | Functional | Tập giá trị kết quả kiểm tra thông tin người đi | Có |
| DC-CheckOutcome | Functional | Tập giá trị kết luận soát vé; WRONG_TRIP do lớp điều phối soát vé của PKG-11 gán (P12 F1), chấp nhận vì là tập kết luận trọn vẹn của UC-015 | Có |

## F5. Danh mục nguyên lý, design smell, nhất quán, dữ liệu

| Nguyên lý | Phần tử đã xét | Kết luận (Đạt / Vi phạm: RV) |
|---|---|---|
| MOD Decomposable, Composable, Understandable | PKG-09, PKG-22, PKG-23; IF-10, IF-11, IF-15 | Đạt: ba package có trách nhiệm đơn, ghép qua ba interface kho dữ liệu, hiểu được khi xem riêng |
| MOD Continuity | Ba phép thử ở F1 | Vi phạm: RV-04 (thay đổi 1: 4 lớp, 1 interface, 1 bảng), RV-09 (thay đổi 3: 2 lớp). Thay đổi 2 (BR-13, BR-14): 1 lớp chính cộng 2 value object, ghi ở RV-16 |
| MOD Protection | Lỗi kho dữ liệu, SMS, cổng thanh toán | Vi phạm: RV-03 (lỗi ghi đè đồng thời lan sang trạng thái chỗ). Còn lại Đạt: PersistenceUnavailableException cô lập lỗi kho, lỗi SMS không huỷ vé |
| SOLID SRP | 3 control, DC-Booking, DC-Trip, DC-Ticket, DC-TicketReturnPolicy | Vi phạm: RV-01 (DC-BookTicketOnlineService). Các lớp còn lại Đạt theo F4 |
| SOLID OCP | confirmReturn (VIA_GATEWAY, CASH_AT_COUNTER), handleTrigger, TicketSalesRule | Vi phạm: RV-11. confirmReturn rẽ nhánh hai giá trị cố định theo BR-15, BR-16: chấp nhận, thêm hình thức hoàn mới là thay đổi chưa có căn cứ trong nguồn |
| SOLID LSP | Ba exception kế thừa RuntimeException; không có cây kế thừa nghiệp vụ | Không phát hiện vi phạm |
| SOLID ISP | IF-10 (4 operation), IF-11 (7), IF-15 (2) | Đạt: mỗi bên gọi dùng 2 đến 4 operation, interface chưa đủ lớn để tách; theo dõi khi PKG-10, PKG-11 thêm operation vào IF-11 |
| SOLID DIP | Ba control và các interface IF-01, IF-02, IF-03, IF-07, IF-08, IF-10, IF-11, IF-15 | Vi phạm: RV-01 (Pay phụ thuộc lớp cụ thể Book). Các phụ thuộc còn lại đi qua interface đặt đúng layer theo P09 R5, R6 |
| GRASP Information Expert | Policy, SmsContent, Booking, Trip | Vi phạm: RV-08, RV-04 |
| GRASP Creator | Booking tạo Ticket, Ticket tạo Refund, Trip tạo Seat | Đạt |
| GRASP Controller | DC-BookTicketOnlineService, DC-ReturnTicketService, DC-PayTicketOnlineService | Vi phạm: RV-01 (phình do kiêm hoàn tất lần đặt, SMS). Hai control còn lại Đạt |
| GRASP Low Coupling, High Cohesion | Xem F3, F4 | Vi phạm: các RV ghi ở F3 và F4 |
| GRASP Polymorphism | Rẽ nhánh theo loại | Vi phạm: RV-07 (rẽ nhánh theo refundMethod), RV-11 |
| GRASP Pure Fabrication | IF-10, IF-11, IF-15, Clock | Vi phạm: RV-19 (entity gọi bộ sinh mã). Entity không tự lưu hay gửi SMS |
| GRASP Indirection | IF-01, IF-02, IF-03, IF-07 | Đạt |
| GRASP Protected Variations | Cổng thanh toán, cổng SMS, bộ định thời, mức hoàn BR-13, BR-14 | Vi phạm: RV-09, RV-10 (định dạng chuỗi chưa được bọc). Hằng mức hoàn trong DC-TicketReturnPolicy: chấp nhận (một hiện thực, YAGNI) |
| PRN Encapsulation | DC-Ticket (7 getter), Trip.findSeats | Vi phạm: RV-04, RV-08 |
| PRN Composition over inheritance | Toàn phạm vi | Đạt: không có kế thừa nghiệp vụ |
| PRN Program to an interface | Thuộc tính và tham số ở ranh giới | Vi phạm: RV-01, RV-19 |
| PRN Law of Demeter | Method của Policy, SmsContent, Booking, Ticket | Vi phạm: RV-04, RV-08 |
| PRN DRY | Định dạng requestKey, BR-32, tập {50, 90}, refundOutcome | Vi phạm: RV-07, RV-09, RV-16 |
| PRN KISS | Không dùng State pattern, không thêm lớp trừu tượng không biến thể | Đạt |
| PRN YAGNI | IF-15 (một hiện thực, có lý do BR-10 và nhiều bản back-end), DC-TripSchedule | Đạt |
| SML God class / Large class | DC-BookTicketOnlineService (9 operation, 8 phụ thuộc); DC-Booking (15 operation); DC-Trip (13) | Vi phạm: RV-01. Booking, Trip: Đạt (xem F4) |
| SML Data class | DC-PhoneReservation (2 thuộc tính, 3 operation) | Không phát hiện vi phạm; theo dõi khi UC-004 đến UC-006 có P07 |
| SML Feature envy | DC-TicketReturnPolicy, DC-TicketSmsContent | Vi phạm: RV-08 |
| SML Shotgun surgery / Divergent change | Thay đổi trạng thái chỗ | Vi phạm: RV-04 |
| SML Long parameter list / Data clumps / Primitive obsession | Trip constructor (7), requestKey, nhãn tuyến | Vi phạm: RV-06, RV-09, RV-10, RV-12 |
| SML Switch statements theo mã loại | confirmReturn, handleTrigger | Vi phạm: RV-11. confirmReturn: chấp nhận (hai giá trị) |
| SML Message chains / Middle man / Inappropriate intimacy | Policy, SmsContent, Book và Pay | Vi phạm: RV-01, RV-08 |
| SML Refused bequest / Lazy class / Speculative generality | Toàn phạm vi | Không phát hiện vi phạm |
| SML Hidden dependencies / Temporal coupling ẩn | Dịch vụ phải gọi IF-10.saveTrip và IF-11.save... đủ cặp | Vi phạm: RV-04, RV-05 |
| PKP ADP (không phụ thuộc vòng) | Đồ thị F6 | Đạt ở cấp package; vòng cấp lớp: RV-01 |
| PKP Chiều layer và nhảy layer | PKG-09 (Application), PKG-22, PKG-23 (Domain) | Đạt: không phụ thuộc đi lên; nhảy layer Application --> Domain được P09 R1 cho phép |
| PKP Chỉ lớp public được tham chiếu từ ngoài | DC-PayTicketOnlineService package-private; phần còn lại public theo P10 F5 | Đạt |
| PKP REP, CCP, CRP | Ba package | Vi phạm: RV-17 (lớp dùng chung đặt sai package). Còn lại Đạt (F4) |
| PKP SDP, SAP | Chỉ số F6.3 | Đạt cho PKG-09; PKG-22 có D = 0,82 và PKG-23 có D = 0,52, ghi nhận xét, không tự động là vi phạm |
| CNS Message P07 --> operation P12 | 109 dòng F4 của P12, đối chiếu UC-002 SD1 (46 message) | Đạt cho message có lớp nhận hoặc gửi trong phạm vi |
| CNS AC P10 có DC; IF P11b có lớp | 18 phần tử P10, P11b trong phạm vi | Đạt: DC-TripCancellation, ba lớp tách của Ticket đều có nguồn; IF-10, IF-11 hiện thực bởi lớp ngoài phạm vi |
| CNS State machine khớp operation và BR | ST-01 đến ST-03 | Vi phạm: RV-02 (trạng thái chuyến), RV-15, RV-20 |
| CNS Multiplicity P12 khớp P13; mọi lớp persistent có bảng; mọi cột có nguồn | 9 lớp persistent, TBL-01 đến TBL-10 | Vi phạm: RV-03 (thiếu cột phiên bản), RV-05 (cột holding_booking_id không có thuộc tính nguồn), RV-15. Còn lại Đạt: R-25 (0..1) và R-37 (Q-76) đã ghi chú |
| CNS Class diagram khớp bảng | F8 và F5 của P12 | Đạt: các cạnh bị lược khỏi sơ đồ PKG-09 đều được giải thích ở F8 |
| CNS Tên đúng glossary | Qua trích dẫn GL-nn | Không review được (xem F1) |
| CNS Dữ liệu cần bảo vệ | P09 F7 | Vi phạm: RV-14 |
| DAT 3NF, phi chuẩn hoá có lý do | TBL-01 đến TBL-10 | Đạt: P13 F5.1 và F5.3 có FD và cơ chế nhất quán cho total_amount, price, traveler_name, refund_amount |
| DAT CASCADE cho composition, FK đúng phía, bảng trung gian, UNIQUE khoá nghiệp vụ | R-23, R-32, booking_traveler, uq_* | Đạt: CASCADE cho seat và refund và booking_traveler; booking_traveler.seat_code không có FK do ứng dụng giữ (P13 F4.2), chấp nhận có lý do |
| DAT Kiểu tiền, CHECK miền giá trị | DECIMAL(12,0), ck_* | Đạt |
| DAT Index theo truy vấn | F6.3 của P13 | Đạt về index; nạp dư dữ liệu khi tìm chuyến: RV-21 |
| DAT Nhất quán khi ghi đồng thời, chủ ghi bảng | TBL-04, TBL-05, TBL-08 | Vi phạm: RV-03, RV-05 |

## F6. Phụ thuộc package

### F6.1. Bảng phụ thuộc

| PKG nguồn | PKG đích | Quan hệ lớp tạo ra phụ thuộc (R-nn) | Hợp lệ theo layer (Có / Không) |
|---|---|---|---|
| PKG-09 | PKG-15 | R-09, R-44, R-46 (Realization IF-02); kiểu PaymentRequestResult, RefundResult, PaymentOutcome trong chữ ký | Có (P09 R1, R5, R7) |
| PKG-09 | PKG-16 | R-02; kiểu SmsResult | Có (R7) |
| PKG-09 | PKG-19 | R-40, R-43 (Realization IF-08); kiểu TriggerReference, TriggerKind | Có (R5, R7) |
| PKG-09 | PKG-22 | R-04, R-38, R-49; kiểu BusType, TripSchedule, SeatAlreadyHeldException | Có (R1, nhảy layer được phép) |
| PKG-09 | PKG-23 | R-05, R-06, R-10, R-39, R-41, R-42, R-45, R-48, R-50, R-67 | Có (R1, nhảy layer được phép) |
| PKG-09 | PKG-28 | Không có R-nn; kiểu Money, TicketCode, PhoneNumber, PaymentReference, PersistenceUnavailableException trong chữ ký | Có (R1); chưa có trong P10 F4 (đã nêu ở P12 Đề xuất sửa P10) |
| PKG-22 | PKG-28 | Không có R-nn; DC-BaseFare.amount là Money, IF-10 ném PersistenceUnavailableException | Có |
| PKG-22 | PKG-23 | Không có (R-33 điều hướng từ PhoneReservation sang Trip) | Không phụ thuộc, đúng P09 R8 |
| PKG-23 | PKG-22 | R-26, R-27, R-29, R-30, R-37, R-58 (và R-33 theo chiều ngược); kiểu TripSchedule, SeatAlreadyHeldException, InvalidStateException | Có (R8, một chiều) |
| PKG-23 | PKG-28 | Không có R-nn; kiểu Money, TicketCode, PhoneNumber, PaymentReference, PersistenceUnavailableException | Có |
| PKG-08 | PKG-09 | R-01, R-07, R-08 (P10 F6; ngoài phạm vi) | Có |
| PKG-10, PKG-11, PKG-24 | PKG-22, PKG-23 | P10 F6; ngoài phạm vi | Có |
| PKG-14 | PKG-22, PKG-23 | SS-07 hiện thực IF-10, IF-11 (P10 F6; ngoài phạm vi) | Có (Services --> Domain) |
| PKG-17 | PKG-23 | Dữ liệu vé cần in (P10 F6; ngoài phạm vi) | Có |

### F6.2. Vòng phụ thuộc

Không có vòng giữa các package PKG-09, PKG-22, PKG-23, PKG-28 và các package Services mà PKG-09 dùng. Có một vòng cấp lớp trong PKG-09: DC-BookTicketOnlineService --> DC-PayTicketOnlineService --> DC-BookTicketOnlineService (R-03, R-47), ghi ở RV-01.

### F6.3. Chỉ số

Cách đếm: Ca và Ce đếm lớp, interface, value object, enumeration, ngoại lệ ngoài package xuất hiện trong quan hệ R-nn, chữ ký, thuộc tính hoặc F3 của các lớp trong package (bỏ kiểu nền tảng Java). Lớp ngoài phạm vi chỉ đếm theo cột "Được dùng bởi" của P10 F5 và P10 F6 (ASM-150).

| PKG | Ca | Ce | I = Ce / (Ca + Ce) | A | D = abs(A + I - 1) | Nhận xét |
|---|---|---|---|---|---|---|
| PKG-09 | 3 (ba REST controller của PKG-08) | 39 (PKG-15: 6, PKG-16: 3, PKG-19: 5, PKG-22: 5, PKG-23: 15, PKG-28: 5) | 0,93 | 0 (0/9) | 0,07 | Không ổn định và cụ thể, đúng với package Application điều phối; D thấp |
| PKG-22 | 18 (PKG-09: 3, PKG-23: 8, PKG-10: 1, PKG-11: 1, PKG-14: 3, PKG-24: 2) | 2 (Money, PersistenceUnavailableException) | 0,10 | 0,08 (1/12) | 0,82 | Rất ổn định nhưng cụ thể (entity có hành vi): vùng đau theo SAP. Chấp nhận với package miền; hệ quả là mọi thay đổi PKG-22 lan ra 18 lớp (liên quan RV-04) |
| PKG-23 | 15 (PKG-09: 5, PKG-08: 3, PKG-10: 1, PKG-11: 1, PKG-14: 2, PKG-17: 1, PKG-24: 2) | 10 (PKG-22: 5, PKG-28: 5) | 0,40 | 0,08 (2/24) | 0,52 | Trung gian, hơi lệch về ổn định và cụ thể; 15 value object, enumeration làm tăng Ca. Ghi nhận xét |

## F7. Tổng hợp

| Mức độ | Số phát hiện | Mã RV |
|---|---|---|
| Nghiêm trọng | 0 | Không có |
| Cao | 5 | RV-01, RV-02, RV-03, RV-04, RV-05 |
| Trung bình | 10 | RV-06, RV-07, RV-08, RV-09, RV-10, RV-11, RV-12, RV-13, RV-14, RV-15 |
| Thấp | 6 | RV-16, RV-17, RV-18, RV-19, RV-20, RV-21 |

Thứ tự chạy lại đề xuất:

1. P10: RV-09, RV-11, RV-17.
2. P11b: RV-05, RV-06, RV-10, RV-21.
3. P12: RV-01, RV-02, RV-03, RV-04, RV-07, RV-08, RV-12, RV-13, RV-14, RV-16, RV-18, RV-19, RV-20.
4. P13: RV-15; chạy lại tiếp P13 sau P12 để thêm cột version (RV-03) và cột holding_booking_id có nguồn thuộc tính (RV-05).

Phát hiện theo độ tin cậy: Chắc chắn 14 (RV-01, RV-04, RV-06 đến RV-12, RV-15 đến RV-19); Cần xác nhận 7 (RV-02, RV-03, RV-05, RV-13, RV-14, RV-20, RV-21).

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-150 | Chuyến đã ở trạng thái CANCELLED có còn xuất hiện trong kết quả tìm chuyến và sơ đồ chỗ, và lần đặt đang giữ chỗ của chuyến đó có còn được thanh toán, phát hành vé không? (Loại khỏi tìm kiếm và từ chối đặt, thanh toán / Chỉ từ chối đặt mới, lần đặt đang giữ vẫn thanh toán và được hoàn 100%) | RV-02; DC-BookTicketOnlineService; IF-10.findTrips; DC-TicketSalesRule | P12 trích ASM-26 và Q-44 nhưng F3 của searchTrips, submitBooking không có bước kiểm; P07 UC-013 để lần đặt giữ chỗ "chờ Q-44" |
| Q-151 | SS-07 bảo đảm "cập nhật có điều kiện" cho chuyến và lần đặt bằng cột phiên bản hay bằng điều kiện theo trạng thái của từng chỗ và lần đặt? (Cột version cho trip và booking / Điều kiện trạng thái trong câu lệnh UPDATE) | RV-03; TBL-04, TBL-05; DC-Trip, DC-Booking | P12 F3 handleTrigger nói "theo phiên bản"; P11b SS07-WB1-M04 nói "phiên bản chuyến"; P13 không có cột phiên bản |
| Q-152 | DC-TripCatalogRepositoryImpl và DC-TicketingRepositoryImpl ghi status và holding_booking_id của TBL-08 trong một câu lệnh hay hai câu lệnh ở hai interface? (Một UPDATE do IF-10 / Hai lệnh do IF-10 và IF-11) | RV-05; ck_seat_hold; TBL-08 | P11b F4 chỉ có hộp trắng của saveTrip; P13 F6.1 ghi ck_seat_hold không nói bên ghi holding_booking_id |
| Q-153 | PKG-08 xác thực hành khách bằng cách nào khi gọi getBookingStatus, getIssuedTickets, và bookingId do IF-15 cấp có khó đoán không? (Mã ngẫu nhiên / Mã tuần tự kèm phiên đăng nhập / Mã tuần tự không xác thực) | RV-14; IF-15; TBL-05.id | P09 F7 nêu dữ liệu cần bảo vệ nhưng P12 F2 không có tham số chứng minh quyền; P13 TBL-05.id "dãy số của CSDL" |
| Q-154 | Khi gọi lại IF-01.requestRefund với cùng requestKey, cổng thanh toán trả kết quả của lần hoàn trước hay thực hiện hoàn lần hai? (Trả kết quả cũ / Hoàn lần hai / Chưa biết) | RV-13; DC-ReturnTicketService.confirmReturn | P06 NFR-07 và Q-24: API hoàn tiền chưa có tài liệu |
| Q-155 | Use case nào ghi nhận việc chi tiền mặt tại quầy và xử lý lại khoản hoàn FAILED để chuyển DC-Refund sang REFUNDED? (UC hiện có UC-008, UC-013 mở rộng / Use case mới / Làm ngoài hệ thống) | RV-20; DC-Refund; DC-RefundOutcome | P12 F1 DC-Refund: "xử lý lại hoàn chưa thành công thuộc use case chưa có" |
| Q-156 | Thời gian phản hồi tối đa của tìm chuyến và sơ đồ chỗ khi 2.000 phiên đồng thời dịp Tết là bao nhiêu? | RV-21; IF-10.findTrips; NFR-01 | P06 NFR-01 chưa có mức đạt (Q-22) |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-150 | Ca của PKG-09, PKG-22, PKG-23 đếm lớp ngoài phạm vi (PKG-08, PKG-10, PKG-11, PKG-14, PKG-17, PKG-24) theo cột "Được dùng bởi" của P10 F5 và P10 F6, mỗi lớp ngoài phạm vi tính một lần. | Các package đó chưa có P12 nên không có danh sách lớp chi tiết; ước lượng đủ để nhận xét I và D | F6.3 |
| ASM-151 | DC-TripCatalogRepositoryImpl và DC-TicketingRepositoryImpl ánh xạ mỗi operation IF-10, IF-11 thành một lượt ghi riêng, không gộp hai operation thành một câu lệnh SQL. | P11b F4 nói các operation ngoài saveTrip "ánh xạ 1-1" và chỉ có hộp trắng cho saveTrip | RV-05, Q-152 |
| ASM-152 | Các thay đổi dễ xảy ra dùng làm phép thử continuity là Q-75 (cách xác định trạng thái chỗ), BR-13 và BR-14 (mức hoàn), đổi cổng thanh toán (NFR-06, Q-24). | Là các điểm mà P06 và P12 ghi là còn mở hoặc phụ thuộc hệ thống ngoài chưa có tài liệu | MOD Continuity, RV-04, RV-09, RV-16 |
| ASM-153 | Bảng Node, Edge trong P12 F8 và F6.4 là nguồn chuẩn của sơ đồ; hai file .drawio không được mở khi review. | C7.1: bảng mô hình là nguồn chuẩn, file .drawio sinh từ bảng | CNS Class diagram khớp bảng |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Nhiều bước | Xem bảng phát hiện F2 | Toàn bộ đề xuất nằm ở F2 | Xem bảng phát hiện F2 |

## Vấn đề còn mở

- Target 7: RV-04, RV-05 và RV-03 cùng chạm tới trạng thái chỗ nhưng ở ba nguyên nhân gốc khác nhau (điều khiển Seat ngoài Trip; hai chủ ghi một bảng; thiếu khoá lạc quan). Ba đề xuất sửa tương thích nhau (Trip điều khiển ST-03, Seat có holdingBookingId do IF-10 ghi, thêm version); nếu người chạy lại P12 coi là một nguyên nhân thì gộp thành một dòng.
- Target 8: bảy phát hiện "Cần xác nhận" đều nêu thông tin còn thiếu ở cột Độ tin cậy và có Q-150 đến Q-156 tương ứng.
- Target 1, 2, 3: đạt. F3 phủ đủ 50 quan hệ R-02 đến R-67, F4 phủ 45 phần tử, ba package và hai operation dài. Hai file .drawio không được mở nên bảng F8 của P12 và sơ đồ không được đối chiếu hình vẽ (ASM-153).
- Chỉ số F6.3 của PKG-22 và PKG-23 là ước lượng vì Ca phụ thuộc lớp ngoài phạm vi (ASM-150); chạy lại X1 sau khi có P12 của PKG-08, PKG-10, PKG-11, PKG-14, PKG-24 để chốt số.
- Chọn giữa hai quy tắc (C9): YEU_CAU_BO_SUNG yêu cầu cấp Q và ASM từ 150, còn C3 yêu cầu cấp tiếp từ số lớn nhất đã thấy (Q-109, ASM-110 trong các đầu vào); đã theo YEU_CAU_BO_SUNG vì ưu tiên cao hơn quy tắc của bước, nên dãy Q-110 đến Q-149 và ASM-111 đến ASM-149 để trống cho các lần chạy khác.
- Chọn giữa hai quy tắc (nguyên lý): RV-08 giữ phương án tách Ticket thành ba lớp của P10 F3 (High Cohesion, SRP) thay vì gộp lại để thoả Information Expert; chỉ thu hẹp kênh phụ thuộc.
- Chưa có phát hiện nào ở mức Nghiêm trọng: RV-03 và RV-05 là ứng viên nếu Q-151, Q-152 được trả lời theo hướng xấu (mất toàn vẹn dữ liệu hoặc thao tác ghi luôn thất bại); cần nâng mức khi đó.
