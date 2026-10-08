# P13 - Mô hình hoá dữ liệu - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P13 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (CONG_NGHE: hệ quản trị CSDL PostgreSQL; CHE_DO_GIA_DINH = CO_NHAN; MUC_CHI_TIET = DAY_DU; NGON_NGU_TEN_PHAN_TU: snake_case cho bảng và cột); 00-Conventions.md; P12-class-design/PKG-09-PKG-22-PKG-23-ticket-sales-catalog-ticketing.md 1.0; P06-supplementary-spec.md 1.0; P04-uc-specs/UC-002, UC-008, UC-013, UC-015 (1.0); P09-architecture.md 1.0; P05-glossary.md 1.0. Chưa có bản P13 cũ. Tham số: LOAI_CSDL = Không có; QUY_UOC_CSDL = Không có; KHOI_LUONG_DU_LIEU = Không có; SINH_DDL = Không có; YEU_CAU_BO_SUNG = chỉ phủ các lớp persistent trong phạm vi P12 đã có |
| Phạm vi | Lớp persistent của PKG-22 TripCatalog và PKG-23 Ticketing trong P12 (PKG-09 không có lớp persistent). Các lớp persistent của PKG-24, PKG-25 và lược đồ SQLite cục bộ (Room) của máy soát vé thuộc lần chạy sau |

Tóm tắt: 9 lớp persistent (Trip, Route, Seat, BaseFare, HolidaySurcharge, Booking, Ticket, Refund, PhoneReservation) thành 10 bảng TBL-01 đến TBL-10 (thêm 1 bảng cho thuộc tính đa trị travelerInfos của Booking), 13 mối quan hệ khái niệm ER-01 đến ER-13, 12 khoá ngoại, 7 index bổ sung ngoài khoá chính và UNIQUE, 1 ràng buộc loại trừ (EXCLUDE). Không có cây kế thừa persistent. Không có script DDL (SINH_DDL = Không có).

Kiểm tra placeholder (Conventions C6): đủ; mọi placeholder tuỳ chọn có giá trị "Không có" nên áp dụng mặc định của bước. CONG_NGHE đã chốt PostgreSQL nên không dùng bảng so sánh quan hệ và tài liệu.

## F1. Quyết định loại CSDL

| Hạng mục | Quyết định | Căn cứ (NFR / P09 / CONG_NGHE) |
|---|---|---|
| Loại CSDL | Quan hệ | CONG_NGHE; P09 F7 "Loại cơ chế lưu trữ": dữ liệu có quan hệ chặt giữa chuyến, chỗ, lần đặt, vé; REQ-67 cần ràng buộc và giao dịch |
| Hệ quản trị | PostgreSQL. Phiên bản chưa nêu; chỉ dùng tính năng có từ PostgreSQL 9.2 (index một phần, kiểu khoảng ngày, ràng buộc EXCLUDE kiểu gist, kiểu range) | CONG_NGHE; P09 F2.2 CN1. Thiết kế: chọn tính năng phổ biến để không ràng buộc phiên bản |
| Phạm vi dữ liệu | CSDL PostgreSQL ở máy chủ, một CSDL duy nhất. SQLite cục bộ (Room) trên máy soát vé (PKG-20) và dữ liệu của PKG-24, PKG-25 ngoài phạm vi lần chạy này | P09 F7; YEU_CAU_BO_SUNG |
| Chiến lược khoá chính | Thực thể độc lập: khoá thay thế tên id, kiểu VARCHAR(36) vì định danh trong P12 (tripId, routeId, baseFareId, holidaySurchargeId, bookingId, reservationId) kiểu String. Vé: khoá tự nhiên ticket_code làm khoá chính vì bất biến (readOnly), ngắn, duy nhất toàn hệ thống (BR-10) và là khoá tra cứu của IF-11.findTicket. Bộ phận của composition và bảng của thuộc tính đa trị: khoá ghép chứa khoá ngoại tới bảng cha (seat, booking_traveler, refund) | Conventions mặc định của prompt P13; P12 F7 (kiểu định danh String) |
| Quy ước tên | Bảng số ít, snake_case, tiếng Anh; cột snake_case; khoá ngoại tên theo bảng cha (route_id) hoặc theo vai trò khi có nhiều khoá tới cùng bảng hoặc khi vai trò rõ hơn (holding_booking_id). Tên ràng buộc: pk_<bang>, fk_<bang_con>_<bang_cha>, uq_<bang>_<cot>, ck_<bang>_<noi_dung>, ix_<bang>_<cot>, ex_<bang>_<noi_dung> | NGON_NGU_TEN_PHAN_TU; prompt P13 (Quy ước chung) |
| Kiểu tiền | DECIMAL(12,0), đơn vị đồng, không dùng số thực dấu phẩy động | Thiết kế: tiền Việt Nam không có đơn vị nhỏ hơn đồng (ASM-102); 12 chữ số dự phòng |
| Kiểu thời gian | TIMESTAMP không múi giờ (giờ địa phương Asia/Ho_Chi_Minh, khớp LocalDateTime của P12), DATE cho ngày | Thiết kế: hệ thống một múi giờ; P12 Quy ước áp dụng (Clock cấu hình Asia/Ho_Chi_Minh) |
| Enumeration | Cột VARCHAR kèm CHECK tập giá trị, không tạo bảng danh mục | Các tập giá trị cố định (P12 F7a); không có yêu cầu để người dùng thêm giá trị |
| Giao dịch và chống trùng chỗ | Mỗi lần đặt, phát hành vé, trả vé, huỷ chuyến là một giao dịch ACID; giữ chỗ bằng cập nhật có điều kiện trên seat.status = 'AVAILABLE'; mỗi chỗ có tối đa một vé còn hiệu lực nhờ index UNIQUE một phần uq_ticket_active_seat | P09 F7 "Chiến lược giao dịch mức cao"; BR-02, BR-03 |
| Khối lượng dữ liệu | Khoảng 80 chuyến mỗi ngày, 12 tuyến, xe 40 chỗ hoặc 29 chỗ: khoảng 3.000 dòng seat mỗi ngày (khoảng 1,1 triệu dòng mỗi năm), số dòng ticket tối đa bằng số chỗ bán được. NFR-01 chưa có mức đạt về thời gian phản hồi (Q-22) nên không có phi chuẩn hoá vì hiệu năng, không phân vùng bảng; thời gian lưu dữ liệu chưa được nguồn nêu | ASM-40; NFR-01; Q-22 |
| Dữ liệu cá nhân | Họ tên, số điện thoại người đi (booking_traveler, ticket) đánh dấu ở cột mô tả; không lưu thông tin thẻ, chỉ lưu mã tham chiếu giao dịch của cổng (booking.payment_reference) | NFR-03; ASM-41; P09 F7 |

## F2. Bảng lớp persistent và chiến lược ánh xạ

Cột Persistent theo cột Persistent của P12 F1. Lớp giá trị lưu cùng thực thể chứa nó ghi rõ ở cột Chiến lược.

| DC | Persistent (Có / Không) | Thực thể (E-) | TBL | Chiến lược | Lý do |
|---|---|---|---|---|---|
| DC-BookTicketOnlineService | Không | - | - | - | Lớp control (dịch vụ ứng dụng), không có đối tượng tồn tại sau khi chương trình kết thúc |
| DC-PayTicketOnlineService | Không | - | - | - | Lớp control (dịch vụ ứng dụng), không có đối tượng tồn tại sau khi chương trình kết thúc |
| DC-ReturnTicketService | Không | - | - | - | Lớp control (dịch vụ ứng dụng), không có đối tượng tồn tại sau khi chương trình kết thúc |
| DC-TripOffer | Không | - | - | - | Value object chỉ để hiển thị kết quả tìm chuyến, dữ liệu suy ra từ TBL-04, TBL-01, TBL-02, TBL-08 |
| DC-BookingHold | Không | - | - | - | Value object kết quả giữ chỗ, dữ liệu lấy từ TBL-05 |
| DC-ReturnQuote | Không | - | - | - | Value object báo giá trả vé, tính từ TBL-09 và quy tắc BR-12 đến BR-14 |
| DC-ReturnReceipt | Không | - | - | - | Value object kết quả trả vé, dữ liệu lấy từ TBL-09, TBL-10 |
| DC-TicketSalesRuleException | Không | - | - | - | Ngoại lệ, không lưu |
| DC-TicketSalesRule | Không | - | - | - | Enumeration lý do từ chối của dịch vụ, không lưu |
| DC-Trip | Có | E-Trip | TBL-04 | Một lớp - một bảng | Thực thể độc lập; availableSeatCount là thuộc tính dẫn xuất không lưu (P12 F7, Q-75) |
| DC-Route | Có | E-Route | TBL-01 | Một lớp - một bảng | Thực thể độc lập |
| DC-Seat | Có | E-Seat | TBL-08 | Một lớp - một bảng | Bộ phận của composition R-23, trạng thái chỗ lưu thuộc tính (ASM-42, ST-03) |
| DC-BaseFare | Có | E-BaseFare | TBL-02 | Một lớp - một bảng | Thực thể độc lập |
| DC-HolidaySurcharge | Có | E-HolidaySurcharge | TBL-03 | Một lớp - một bảng | Thực thể độc lập |
| DC-TripSchedule | Không | - | - | - | Value object hiển thị gồm tên tuyến và giờ xuất bến, dữ liệu suy ra từ TBL-01, TBL-04 |
| DC-TripStatus | Không | - | - | CHECK ở TBL-04.status | Enumeration tập giá trị cố định (F7a của P12), không có nhu cầu quản lý danh mục |
| DC-SeatStatus | Không | - | - | CHECK ở TBL-08.status | Như trên |
| DC-BusType | Không | - | - | CHECK ở TBL-02.bus_type, TBL-04.bus_type | Như trên |
| IF-10 | Không | - | - | - | Interface kho dữ liệu, hiện thực ở PKG-14, không phải đối tượng dữ liệu |
| DC-SeatAlreadyHeldException | Không | - | - | - | Ngoại lệ, không lưu |
| DC-InvalidStateException | Không | - | - | - | Ngoại lệ, không lưu |
| DC-Booking | Có | E-Booking | TBL-05 | Một lớp - một bảng | Thực thể độc lập, chỉ lưu từ trạng thái HELD (ASM-44). MAX_SEATS và HOLD_DURATION là hằng của lớp (BR-01, BR-07), không lưu |
| DC-Ticket | Có | E-Ticket | TBL-09 | Một lớp - một bảng | Thực thể độc lập, tồn tại độc lập với lần đặt (R-28) |
| DC-TicketReturnPolicy | Không | - | - | - | Dịch vụ miền không có trạng thái, ngưỡng lấy từ BR-12 đến BR-14, BR-17 |
| DC-TicketSmsContent | Không | - | - | - | Dịch vụ miền không có trạng thái |
| DC-TripCancellation | Không | - | - | - | Đơn vị công việc không có thuộc tính; việc ghi do IF-11.saveTripCancellation thực hiện trên TBL-04, TBL-09, TBL-07 trong một giao dịch |
| DC-Refund | Có | E-Refund | TBL-10 | Một lớp - một bảng | Bộ phận của composition R-32, định danh bằng vé |
| DC-PhoneReservation | Có | E-PhoneReservation | TBL-07 | Một lớp - một bảng | Thực thể độc lập; chỉ có các thuộc tính P12 đã nêu (xem Vấn đề còn mở) |
| IF-11 | Không | - | - | - | Interface kho dữ liệu |
| IF-15 | Không | - | - | - | Interface bộ sinh mã, hiện thực bằng dãy số của CSDL (SS-07), không phải đối tượng dữ liệu |
| DC-TravelerInfo | Không | - | TBL-06 | Nhúng vào TBL-06 (thuộc tính đa trị phức hợp travelerInfos của DC-Booking) | Value object nằm trong danh sách DC-Booking.travelerInfos 1..*; thuộc tính đa trị thành bảng riêng, cần lưu vì dịch vụ không giữ trạng thái giữa hai bước và phải phát hành vé khi thanh toán thành công (P09 F7) |
| DC-BookingSummary | Không | - | - | - | Value object hiển thị, dữ liệu lấy từ TBL-09, TBL-05 |
| DC-TicketCheckResult | Không | - | - | - | Value object kết luận soát vé, không lưu ở phạm vi này |
| DC-RefundQuote | Không | - | - | - | Value object báo giá hoàn, tính từ TBL-09 |
| DC-TicketReturnInfo | Không | - | - | - | Value object hiển thị thông tin vé, dữ liệu lấy từ TBL-09, TBL-04, TBL-01 |
| DC-CancelImpactInfo | Không | - | - | - | Value object hiển thị, dữ liệu lấy từ TBL-09 |
| DC-CancellationSummary | Không | - | - | - | Value object tổng hợp trước khi huỷ chuyến, tính từ TBL-09, TBL-07 |
| DC-BookingStatus | Không | - | - | CHECK ở TBL-05.status | Enumeration tập giá trị cố định |
| DC-TicketStatus | Không | - | - | CHECK ở TBL-09.status | Như trên |
| DC-PurchaseChannel | Không | - | - | CHECK ở TBL-09.purchase_channel | Như trên |
| DC-RefundMethod | Không | - | - | CHECK ở TBL-10.refund_method | Như trên |
| DC-RefundOutcome | Không | - | - | CHECK ở TBL-10.refund_outcome | Như trên |
| DC-PhoneReservationStatus | Không | - | - | CHECK ở TBL-07.status | Như trên |
| DC-TravelerInfoProblem | Không | - | - | - | Enumeration kết quả kiểm tra, không lưu |
| DC-CheckOutcome | Không | - | - | - | Enumeration kết luận soát vé, không lưu ở phạm vi này |

Value object của PKG-28 (Money, TicketCode, PhoneNumber, PaymentReference) không có DC trong phạm vi và không thành bảng: mỗi giá trị nhúng thành một cột (Money --> DECIMAL(12,0), TicketCode --> ticket_code, PhoneNumber --> VARCHAR(10), PaymentReference --> VARCHAR(100)). Thuộc tính không lưu: DC-Trip./availableSeatCount (dẫn xuất từ seat.status), DC-Booking.MAX_SEATS và DC-Booking.HOLD_DURATION (hằng của lớp).

## F3. Mô hình khái niệm (ER)

### F3.1. Thực thể

| E | Tên thực thể | Mô tả | Định danh | Thuộc tính (đánh dấu: định danh, phức hợp, đa trị, dẫn xuất) | Thực thể yếu (Có / Không) | Nguồn DC |
|---|---|---|---|---|---|---|
| E-Route | Tuyến | Đường chạy cố định nối một điểm đi với một điểm đến (GL-36) | routeId | routeId (định danh), departurePoint, arrivalPoint | Không | DC-Route |
| E-BaseFare | Giá vé theo tuyến và loại xe | Mức giá vé của một cặp tuyến và loại xe (GL-09) | baseFareId | baseFareId (định danh), busType, amount | Không | DC-BaseFare |
| E-HolidaySurcharge | Mức tăng giá lễ Tết | Mức tăng theo phần trăm cho một khoảng ngày (GL-25) | holidaySurchargeId | holidaySurchargeId (định danh), startDate, endDate, ratePercent | Không | DC-HolidaySurcharge |
| E-Trip | Chuyến | Một lần chạy của một tuyến tại một giờ xuất bến (GL-04) | tripId | tripId (định danh), departureTime, busType, status, availableSeatCount (dẫn xuất) | Không | DC-Trip |
| E-Seat | Chỗ | Một vị trí trên xe của một chuyến (GL-02) | seatCode (định danh riêng phần, kết hợp với định danh của E-Trip) | seatCode (định danh riêng phần), status | Có (xác định bởi E-Trip qua ER-02) | DC-Seat |
| E-Booking | Lần đặt | Một lần đặt vé trực tuyến (GL-18) | bookingId | bookingId (định danh), ticketPrice, totalAmount, holdStartTime, status, paymentAttemptCount, paymentReference, travelerInfos (đa trị, phức hợp gồm seatCode, travelerName, travelerPhone) | Không | DC-Booking, DC-TravelerInfo |
| E-Ticket | Vé | Vé của một chỗ trên một chuyến (GL-37) | ticketCode | ticketCode (định danh), travelerName, travelerPhone, price, status, purchaseChannel, checkedTime | Không | DC-Ticket |
| E-Refund | Khoản hoàn | Khoản hoàn tiền của một vé đã huỷ | Dùng định danh của E-Ticket (không có định danh riêng) | refundAmount, refundRatePercent, refundMethod, refundOutcome | Có (xác định bởi E-Ticket qua ER-11) | DC-Refund |
| E-PhoneReservation | Đặt chỗ qua điện thoại | Yêu cầu giữ chỗ trên một chuyến do nhân viên bán vé ghi nhận (GL-07) | reservationId | reservationId (định danh), status | Không | DC-PhoneReservation |

Thuộc tính ghi ở mức khái niệm không có kiểu vật lý. Enumeration thành miền giá trị của thuộc tính tương ứng (P12 F7a). Thực thể dùng định danh thay thế: E-Route, E-BaseFare, E-HolidaySurcharge, E-Trip, E-Booking, E-PhoneReservation (mã do hệ thống cấp); E-Ticket dùng mã vé (BR-10).

### F3.2. Mối quan hệ

Cột Tham gia ghi theo thứ tự A, B: bắt buộc khi bản số tối thiểu của đầu kia từ P12 lớn hơn 0.

| ER | Tên mối quan hệ (động từ) | Thực thể A | Thực thể B | Bản số (1:1 / 1:N / M:N) | Tham gia A, B (bắt buộc / tuỳ chọn) | Thuộc tính của mối quan hệ | Nguồn R (P12) |
|---|---|---|---|---|---|---|---|
| ER-01 | chạy theo | E-Trip | E-Route | N:1 | bắt buộc, tuỳ chọn | Không | R-22 |
| ER-02 | gồm | E-Trip | E-Seat | 1:N | bắt buộc, bắt buộc | Không | R-23 |
| ER-03 | áp dụng giá | E-Trip | E-BaseFare | N:1 | bắt buộc, tuỳ chọn | Không | R-24 |
| ER-04 | chịu mức tăng | E-Trip | E-HolidaySurcharge | N:1 | tuỳ chọn, tuỳ chọn | Không | R-25 |
| ER-05 | đặt cho | E-Booking | E-Trip | N:1 | bắt buộc, tuỳ chọn | Không | R-26 |
| ER-06 | giữ | E-Booking | E-Seat | 1:N | bắt buộc, tuỳ chọn | Không | R-27 |
| ER-07 | phát hành | E-Booking | E-Ticket | 1:N | tuỳ chọn, tuỳ chọn | Không | R-28 |
| ER-08 | thuộc chuyến | E-Ticket | E-Trip | N:1 | bắt buộc, tuỳ chọn | Không | R-29 |
| ER-09 | dành cho chỗ | E-Ticket | E-Seat | N:1 | bắt buộc, tuỳ chọn | Không | R-30 |
| ER-10 | định giá cho | E-BaseFare | E-Route | N:1 | bắt buộc, tuỳ chọn | Không | R-31 |
| ER-11 | hoàn tiền cho | E-Ticket | E-Refund | 1:1 | tuỳ chọn, bắt buộc | Không | R-32 |
| ER-12 | giữ chỗ trên | E-PhoneReservation | E-Trip | N:1 | bắt buộc, tuỳ chọn | Không | R-33 |
| ER-13 | đặt giữ | E-PhoneReservation | E-Seat | 1:N | chưa rõ (Q-76), tuỳ chọn | Không | R-37 |

Chiều đọc: ER-01 Chuyến chạy theo Tuyến; ER-02 Chuyến gồm Chỗ; ER-03 Chuyến áp dụng giá của Giá vé theo tuyến và loại xe; ER-04 Chuyến chịu Mức tăng giá lễ Tết (suy ra theo ngày, xem F4.2); ER-05 Lần đặt đặt cho Chuyến; ER-06 Lần đặt giữ Chỗ; ER-07 Lần đặt phát hành Vé; ER-08 Vé thuộc chuyến Chuyến; ER-09 Vé dành cho chỗ Chỗ; ER-10 Giá vé định giá cho Tuyến; ER-11 Vé hoàn tiền cho Khoản hoàn; ER-12 Đặt chỗ qua điện thoại giữ chỗ trên Chuyến; ER-13 Đặt chỗ qua điện thoại đặt giữ Chỗ. Mối quan hệ ER-09 là N:1 vì một chỗ có nhiều vé theo thời gian (ASM-20), tối đa một vé còn hiệu lực (BR-02).

## F4. Mô hình logic (CSDL quan hệ)

### F4.1. Lược đồ quan hệ

| TBL | Tên bảng | Lược đồ (PK ghi trước, đánh dấu PK:, FK:) | Khoá ứng viên khác | Nguồn (E / DC) |
|---|---|---|---|---|
| TBL-01 | route | route(PK: id, departure_point, arrival_point) | (departure_point, arrival_point) | E-Route / DC-Route |
| TBL-02 | base_fare | base_fare(PK: id, route_id FK, bus_type, amount) | (route_id, bus_type) | E-BaseFare / DC-BaseFare |
| TBL-03 | holiday_surcharge | holiday_surcharge(PK: id, start_date, end_date, rate_percent) | Không có khai báo; khoảng ngày không chồng nhau bằng ex_holiday_surcharge_period | E-HolidaySurcharge / DC-HolidaySurcharge |
| TBL-04 | trip | trip(PK: id, route_id FK, bus_type FK, departure_time, status) | (route_id, departure_time) | E-Trip / DC-Trip |
| TBL-05 | booking | booking(PK: id, trip_id FK, ticket_price, total_amount, hold_start_time, status, payment_attempt_count, payment_reference) | Không có | E-Booking / DC-Booking |
| TBL-06 | booking_traveler | booking_traveler(PK: booking_id FK, PK: seat_code, traveler_name, traveler_phone) | Không có | E-Booking (thuộc tính đa trị phức hợp travelerInfos) / DC-Booking.travelerInfos / DC-TravelerInfo |
| TBL-07 | phone_reservation | phone_reservation(PK: id, trip_id FK, status) | Không có | E-PhoneReservation / DC-PhoneReservation |
| TBL-08 | seat | seat(PK: trip_id FK, PK: seat_code, status, holding_booking_id FK, phone_reservation_id FK) | Không có | E-Seat / DC-Seat |
| TBL-09 | ticket | ticket(PK: ticket_code, booking_id FK, trip_id FK, seat_code FK, traveler_name, traveler_phone, price, status, purchase_channel, checked_time) | (trip_id, seat_code) khi status = 'ISSUED' (index UNIQUE một phần) | E-Ticket / DC-Ticket |
| TBL-10 | refund | refund(PK: ticket_code FK, refund_amount, refund_rate_percent, refund_method, refund_outcome) | Không có | E-Refund / DC-Refund |

Khoá ngoại ghép: trip(route_id, bus_type) --> base_fare(route_id, bus_type); ticket(trip_id, seat_code) --> seat(trip_id, seat_code).

### F4.2. Ánh xạ quan hệ giữa lớp

| R (P12) | Loại | Multiplicity | Cách ánh xạ | FK hoặc bảng trung gian | Kiểu quan hệ dữ liệu (phụ thuộc / độc lập) | ON DELETE |
|---|---|---|---|---|---|---|
| R-22 | Association | Trip 0..* - Route 1 | FK ở bảng phía N | trip.route_id NOT NULL (fk_trip_route) | độc lập | RESTRICT |
| R-23 | Composition | Trip 1 - Seat 1..* | FK trong PK bảng bộ phận | seat(PK: trip_id FK, PK: seat_code) (fk_seat_trip) | phụ thuộc | CASCADE |
| R-24 | Association | Trip 0..* - BaseFare 1 | FK ghép ở bảng phía N, trỏ khoá ứng viên (route_id, bus_type) của base_fare | trip(route_id, bus_type) NOT NULL (fk_trip_base_fare); không lưu base_fare_id vì sẽ tạo phụ thuộc bắc cầu (F5) | độc lập | RESTRICT |
| R-25 | Association | Trip 0..* - HolidaySurcharge 0..1 | Không lưu liên kết: mức tăng áp dụng tra theo ngày xuất bến, khoảng ngày chứa date(trip.departure_time) bằng truy vấn trên ex_holiday_surcharge_period; ASM-105 bảo đảm tối đa một kết quả | Không có FK | Không áp dụng | Không áp dụng |
| R-26 | Association | Booking 0..* - Trip 1 | FK ở bảng phía N | booking.trip_id NOT NULL (fk_booking_trip) | độc lập | RESTRICT |
| R-27 | Association | Booking 0..1 - Seat 1..5 | FK ở bảng phía N (seat), tuỳ chọn vì chỗ có thể không bị lần đặt giữ | seat.holding_booking_id NULL (fk_seat_booking) | độc lập | RESTRICT |
| R-28 | Association | Booking 0..1 - Ticket 0..5 | FK ở bảng phía N, tuỳ chọn vì vé bán tại quầy không có lần đặt | ticket.booking_id NULL (fk_ticket_booking) | độc lập | RESTRICT |
| R-29 | Association | Ticket 0..* - Trip 1 | FK ở bảng phía N, dùng chung cột trip_id với khoá ngoại tới chỗ để không có hai cột trip lệch nhau | ticket.trip_id NOT NULL, nằm trong fk_ticket_seat; không khai báo khoá ngoại trực tiếp thứ hai tới trip | độc lập | RESTRICT |
| R-30 | Association | Ticket 0..* - Seat 1 | FK ghép ở bảng phía N | ticket(trip_id, seat_code) NOT NULL (fk_ticket_seat) | độc lập | RESTRICT |
| R-31 | Association | BaseFare 0..* - Route 1 | FK ở bảng phía N | base_fare.route_id NOT NULL (fk_base_fare_route) | độc lập | RESTRICT |
| R-32 | Composition | Ticket 1 - Refund 0..1 | FK trong PK bảng bộ phận (PK của refund đồng thời là FK) | refund.ticket_code (fk_refund_ticket) | phụ thuộc | CASCADE |
| R-33 | Association | Trip 1 - PhoneReservation 0..* | FK ở bảng phía N | phone_reservation.trip_id NOT NULL (fk_phone_reservation_trip) | độc lập | RESTRICT |
| R-37 | Association | PhoneReservation 0..1 - Seat (chờ Q-76) | FK ở bảng phía có bản số 0..1 tới đặt chỗ (seat), dùng được cho cả hai kết quả của Q-76 | seat.phone_reservation_id NULL (fk_seat_phone_reservation) | độc lập | RESTRICT |

Thuộc tính đa trị DC-Booking.travelerInfos (không phải quan hệ P12): booking_traveler(PK: booking_id FK, PK: seat_code), phụ thuộc, ON DELETE CASCADE (fk_booking_traveler_booking).

Quan hệ P12 không ánh xạ: mọi Dependency (R-04, R-05, R-06, R-10, R-53 đến R-57, R-62 đến R-67) và mọi quan hệ có đầu mút là lớp không persistent (R-02, R-03, R-09, R-38 đến R-52, R-58 đến R-61; DC-TripCancellation chỉ phối hợp lúc chạy, việc ghi do IF-11.saveTripCancellation thực hiện).

Ràng buộc liên bảng không khai báo được bằng khoá, do ứng dụng giữ trong giao dịch: seat.status = 'SOLD' khi và chỉ khi chỗ có vé ISSUED; booking_traveler.seat_code là mã chỗ của chuyến booking.trip_id; refund_method khớp ticket.purchase_channel (BR-15, BR-16); số dòng booking_traveler của lần đặt từ 1 đến 5 (BR-01).

### F4.3. Ánh xạ generalization

| Cây kế thừa (lớp cha - các lớp con) | Chiến lược | Bảng | Cột phân biệt loại | Lý do chọn |
|---|---|---|---|---|
| Không có cây kế thừa persistent trong P12 (F5 chỉ có Association, Composition, Dependency, Realization của lớp không persistent) | - | - | - | - |

## F5. Chuẩn hoá (CSDL quan hệ)

### F5.1. Bảng kiểm tra

| TBL | Khoá (chính và ứng viên) | Phụ thuộc hàm (FD) | 1NF | 2NF | 3NF | BCNF | Kết luận |
|---|---|---|---|---|---|---|---|
| TBL-01 | PK id; CK (departure_point, arrival_point) theo ASM-108 | id --> departure_point, arrival_point; (departure_point, arrival_point) --> id | Đạt | Đạt | Đạt | Đạt (cả hai vế trái là khoá) | Đạt BCNF |
| TBL-02 | PK id; CK (route_id, bus_type) theo BR-04 | id --> route_id, bus_type, amount; (route_id, bus_type) --> id, amount | Đạt | Đạt | Đạt | Đạt (hai khoá chồng lấn nhau ở route_id, đã kiểm tra) | Đạt BCNF |
| TBL-03 | PK id; start_date là khoá suy ra từ khoảng ngày không chồng nhau (ASM-105) | id --> start_date, end_date, rate_percent; start_date --> end_date, rate_percent | Đạt | Đạt | Đạt | Đạt (start_date là siêu khoá theo ASM-105) | Đạt BCNF |
| TBL-04 | PK id; CK (route_id, departure_time) theo ASM-109 | id --> route_id, bus_type, departure_time, status; (route_id, departure_time) --> id, bus_type, status | Đạt | Đạt | Đạt: không có cột base_fare_id nên không có phụ thuộc bắc cầu id --> base_fare_id --> (route_id, bus_type) | Đạt (hai khoá chồng lấn ở route_id, đã kiểm tra) | Đạt BCNF |
| TBL-05 | PK id | id --> trip_id, ticket_price, total_amount, hold_start_time, status, payment_attempt_count, payment_reference. total_amount = ticket_price x số dòng booking_traveler là quan hệ giữa hai bảng, không phải FD trong bảng | Đạt | Đạt | Đạt | Đạt | Đạt 3NF; total_amount ghi ở F5.3 |
| TBL-06 | PK (booking_id, seat_code) | (booking_id, seat_code) --> traveler_name, traveler_phone. traveler_phone không xác định traveler_name (một số điện thoại có thể ghi nhiều tên) và ngược lại | Đạt (mỗi chỗ một dòng, không có cột danh sách) | Đạt (không thuộc tính nào phụ thuộc riêng booking_id hay seat_code) | Đạt | Đạt | Đạt BCNF |
| TBL-07 | PK id | id --> trip_id, status | Đạt | Đạt | Đạt | Đạt | Đạt BCNF |
| TBL-08 | PK (trip_id, seat_code) | (trip_id, seat_code) --> status, holding_booking_id, phone_reservation_id. status không phải hàm của holding_booking_id (holding_booking_id rỗng ứng với cả AVAILABLE và SOLD) nên ck_seat_hold là ràng buộc kiểm tra, không phải FD | Đạt | Đạt | Đạt | Đạt | Đạt BCNF |
| TBL-09 | PK ticket_code. (trip_id, seat_code) không phải khoá vì một chỗ có nhiều vé theo thời gian (ASM-20) | ticket_code --> booking_id, trip_id, seat_code, traveler_name, traveler_phone, price, status, purchase_channel, checked_time | Đạt | Đạt | Đạt (traveler_name, traveler_phone và price là sự kiện của vé, không suy ra từ chỗ hay lần đặt) | Đạt | Đạt BCNF |
| TBL-10 | PK ticket_code | ticket_code --> refund_amount, refund_rate_percent, refund_method, refund_outcome. refund_amount là hàm của ticket.price và refund_rate_percent ở hai bảng khác nhau | Đạt | Đạt | Đạt | Đạt | Đạt BCNF; refund_amount ghi ở F5.3 |

### F5.2. Quá trình tách

Không có bảng không đạt. Hai quyết định thiết kế để giữ 3NF: (1) trip không lưu base_fare_id mà dùng khoá ngoại ghép (route_id, bus_type) trỏ khoá ứng viên của base_fare, vì lưu cả base_fare_id lẫn (route_id, bus_type) sẽ tạo phụ thuộc bắc cầu; (2) danh sách DC-Booking.travelerInfos (nhóm lặp) tách thành booking_traveler để đạt 1NF.

### F5.3. Phi chuẩn hoá có chủ đích

| TBL.cột | Dạng phi chuẩn hoá | Lý do (NFR / BR, số liệu) | Cơ chế giữ nhất quán |
|---|---|---|---|
| TBL-05.total_amount | Giá trị dẫn xuất lưu sẵn (ticket_price x số chỗ) | BR-06; P12 F7 ghi tổng tiền giữ lại sau khi giá thay đổi và là số tiền đã gửi cổng thanh toán; lý do ngữ nghĩa (giữ giá trị lịch sử), không phải hiệu năng | Booking.calculateTotal tính một lần khi lập lần đặt, ghi cùng giao dịch với các dòng booking_traveler; không sửa sau khi status khác DRAFT |
| TBL-09.price | Sao chép giá trị lịch sử (cùng giá trị booking.ticket_price của lần đặt trực tuyến tại thời điểm phát hành) | ASM-22: giá khách đã trả là cơ sở tính số tiền hoàn; là sự kiện khác với base_fare.amount vì giá có thể đổi sau khi bán; vé bán tại quầy không có lần đặt nên cột là nguồn duy nhất | Booking.issueTickets ghi price bằng ticket_price của lần đặt trong giao dịch phát hành; cột readOnly (P12 F7) |
| TBL-09.traveler_name, TBL-09.traveler_phone | Sao chép giá trị lịch sử từ booking_traveler lúc phát hành vé | Vé là hồ sơ độc lập, tồn tại cả khi bán tại quầy (không có booking_traveler) và dùng cho gửi SMS, soát vé | Booking.issueTickets sao chép trong giao dịch phát hành; sau đó không đồng bộ hai chiều |
| TBL-10.refund_amount | Giá trị dẫn xuất lưu sẵn (ticket.price x refund_rate_percent / 100, làm tròn đồng HALF_UP theo ASM-102) | Lý do ngữ nghĩa: số tiền thực tế đã ghi nhận lúc hoàn, đối chiếu với kết quả của cổng thanh toán hoặc chi tiền mặt | TicketReturnPolicy tính một lần khi tạo Refund (Ticket.cancelTicket); cột readOnly (P12 F7) |

Kết luận phân biệt: ticket.traveler_name không phải dư thừa của booking_traveler.traveler_name, và ticket.price không phải dư thừa của base_fare.amount (xem quy tắc phân biệt giá trị lịch sử trong prompt P13).

## F6. Mô hình vật lý

### F6.1. Bảng cột

| TBL | Tên bảng | Cột | Kiểu | PK/FK/UNIQUE | NULL | Mặc định | Nguồn DC | Tham chiếu FK (TBL.cột, ON DELETE, ON UPDATE) | CHECK / mô tả |
|---|---|---|---|---|---|---|---|---|---|
| TBL-01 | route | id | VARCHAR(36) | PK | NOT NULL |  | DC-Route.routeId |  | pk_route. Thiết kế: mã chuỗi do ứng dụng cấp, 36 ký tự đủ cho UUID dạng chuỗi nếu đổi cách cấp mã |
| TBL-01 | route | departure_point | VARCHAR(100) | UQ | NOT NULL |  | DC-Route.departurePoint |  | CHECK (btrim(departure_point) <> '') ck_route_departure_point_not_blank. uq_route_points (departure_point, arrival_point) theo ASM-108. Thiết kế: 100 ký tự cho tên điểm đi |
| TBL-01 | route | arrival_point | VARCHAR(100) | UQ | NOT NULL |  | DC-Route.arrivalPoint |  | CHECK (btrim(arrival_point) <> '') ck_route_arrival_point_not_blank. Thuộc uq_route_points. Thiết kế: 100 ký tự cho tên điểm đến |
| TBL-02 | base_fare | id | VARCHAR(36) | PK | NOT NULL |  | DC-BaseFare.baseFareId |  | pk_base_fare. Thiết kế: như TBL-01.id |
| TBL-02 | base_fare | route_id | VARCHAR(36) | FK, UQ | NOT NULL |  | R-31 | TBL-01.id, RESTRICT, NO ACTION (fk_base_fare_route) | uq_base_fare_route_bus_type (route_id, bus_type): BR-04 mỗi cặp tuyến và loại xe có một mức giá |
| TBL-02 | base_fare | bus_type | VARCHAR(20) | UQ | NOT NULL |  | DC-BaseFare.busType |  | CHECK (bus_type IN ('SLEEPER_40','SEATER_29')) ck_base_fare_bus_type (DC-BusType, GL-21). Thuộc uq_base_fare_route_bus_type. Thiết kế: 20 ký tự dự phòng cho giá trị enumeration |
| TBL-02 | base_fare | amount | DECIMAL(12,0) |  | NOT NULL |  | DC-BaseFare.amount |  | CHECK (amount > 0) ck_base_fare_amount. Đơn vị đồng. Thiết kế: DECIMAL(12,0), tiền Việt Nam không có đơn vị nhỏ hơn đồng (ASM-102), 12 chữ số dự phòng |
| TBL-03 | holiday_surcharge | id | VARCHAR(36) | PK | NOT NULL |  | DC-HolidaySurcharge.holidaySurchargeId |  | pk_holiday_surcharge. Thiết kế: như TBL-01.id |
| TBL-03 | holiday_surcharge | start_date | DATE |  | NOT NULL |  | DC-HolidaySurcharge.startDate |  | Tính cả ngày đầu (ASM-105). ex_holiday_surcharge_period: EXCLUDE USING gist (daterange(start_date, end_date, '[]') WITH &&) bảo đảm khoảng ngày không chồng nhau (ASM-105) |
| TBL-03 | holiday_surcharge | end_date | DATE |  | NOT NULL |  | DC-HolidaySurcharge.endDate |  | CHECK (end_date >= start_date) ck_holiday_surcharge_period. Tính cả ngày cuối (ASM-105) |
| TBL-03 | holiday_surcharge | rate_percent | INTEGER |  | NOT NULL |  | DC-HolidaySurcharge.ratePercent |  | CHECK (rate_percent BETWEEN 0 AND 30) ck_holiday_surcharge_rate (BR-32) |
| TBL-04 | trip | id | VARCHAR(36) | PK | NOT NULL |  | DC-Trip.tripId |  | pk_trip. Thiết kế: như TBL-01.id |
| TBL-04 | trip | route_id | VARCHAR(36) | FK, UQ | NOT NULL |  | R-22, R-24 | TBL-01.id, RESTRICT, NO ACTION (fk_trip_route); cùng với bus_type tham chiếu TBL-02.(route_id, bus_type), RESTRICT, NO ACTION (fk_trip_base_fare) | uq_trip_route_departure (route_id, departure_time) theo ASM-109 |
| TBL-04 | trip | bus_type | VARCHAR(20) | FK | NOT NULL |  | DC-Trip.busType; R-24 | TBL-02.bus_type (cùng route_id, fk_trip_base_fare), RESTRICT, NO ACTION | CHECK (bus_type IN ('SLEEPER_40','SEATER_29')) ck_trip_bus_type. Không lưu base_fare_id: mức giá suy ra từ (route_id, bus_type) nên lưu thêm sẽ tạo phụ thuộc bắc cầu |
| TBL-04 | trip | departure_time | TIMESTAMP | UQ | NOT NULL |  | DC-Trip.departureTime |  | Giờ xuất bến gồm ngày, giờ địa phương Asia/Ho_Chi_Minh, không lưu múi giờ (khớp LocalDateTime). Thuộc uq_trip_route_departure |
| TBL-04 | trip | status | VARCHAR(20) |  | NOT NULL | 'ACTIVE' | DC-Trip.status |  | CHECK (status IN ('ACTIVE','CANCELLED')) ck_trip_status (DC-TripStatus) |
| TBL-05 | booking | id | VARCHAR(36) | PK | NOT NULL |  | DC-Booking.bookingId |  | pk_booking. Thiết kế: mã do IF-15 cấp bằng dãy số của CSDL, dạng chuỗi; 36 ký tự dự phòng |
| TBL-05 | booking | trip_id | VARCHAR(36) | FK | NOT NULL |  | R-26 | TBL-04.id, RESTRICT, NO ACTION (fk_booking_trip) |  |
| TBL-05 | booking | ticket_price | DECIMAL(12,0) |  | NULL |  | DC-Booking.ticketPrice |  | CHECK (ticket_price > 0) ck_booking_ticket_price. Giá một vé chốt lúc calculateTotal (ASM-22). NULL chỉ khi status = 'DRAFT' (ck_booking_state) |
| TBL-05 | booking | total_amount | DECIMAL(12,0) |  | NULL |  | DC-Booking.totalAmount |  | CHECK (total_amount > 0) ck_booking_total_amount. Phi chuẩn hoá có chủ đích (F5.3). NULL chỉ khi status = 'DRAFT' (ck_booking_state) |
| TBL-05 | booking | hold_start_time | TIMESTAMP |  | NULL |  | DC-Booking.holdStartTime |  | Giờ địa phương, không múi giờ. Hạn giữ chỗ = hold_start_time + 10 phút (BR-07, HOLD_DURATION), không lưu. ck_booking_state (status <> 'DRAFT' thì ticket_price, total_amount, hold_start_time NOT NULL) |
| TBL-05 | booking | status | VARCHAR(20) |  | NOT NULL | 'DRAFT' | DC-Booking.status |  | CHECK (status IN ('DRAFT','HELD','TICKETED','EXPIRED')) ck_booking_status (DC-BookingStatus, ST-01). Lần đặt DRAFT không được lưu (ASM-44) nhưng giá trị thuộc miền của enumeration |
| TBL-05 | booking | payment_attempt_count | INTEGER |  | NOT NULL | 0 | DC-Booking.paymentAttemptCount |  | CHECK (payment_attempt_count >= 0) ck_booking_payment_attempt_count. |
| TBL-05 | booking | payment_reference | VARCHAR(100) |  | NULL |  | DC-Booking.paymentReference |  | Mã tham chiếu giao dịch do cổng thanh toán cấp, không phải thông tin thẻ (ASM-41, NFR-03). ck_booking_payment_reference: (status = 'TICKETED') = (payment_reference IS NOT NULL). Thiết kế: 100 ký tự dự phòng vì định dạng của cổng chưa có tài liệu (Q-24) |
| TBL-06 | booking_traveler | booking_id | VARCHAR(36) | PK, FK | NOT NULL |  | Thiết kế: khoá ngoại của thuộc tính đa trị DC-Booking.travelerInfos | TBL-05.id, CASCADE, NO ACTION (fk_booking_traveler_booking) | pk_booking_traveler (booking_id, seat_code) |
| TBL-06 | booking_traveler | seat_code | VARCHAR(10) | PK | NOT NULL |  | DC-TravelerInfo.seatCode |  | Mã chỗ của người đi, một dòng cho mỗi chỗ của lần đặt. Khớp một chỗ của chuyến trong TBL-08 do ứng dụng bảo đảm (xem F5.3). Thiết kế: 10 ký tự cho mã chỗ như A05 |
| TBL-06 | booking_traveler | traveler_name | VARCHAR(100) |  | NOT NULL |  | DC-TravelerInfo.travelerName |  | CHECK (btrim(traveler_name) <> '') ck_booking_traveler_name_not_blank (lần đặt chỉ lưu sau validateTravelerInfo). Dữ liệu cá nhân (P09 F7). Thiết kế: 100 ký tự dự phòng cho tên người |
| TBL-06 | booking_traveler | traveler_phone | VARCHAR(10) |  | NOT NULL |  | DC-TravelerInfo.travelerPhone |  | CHECK (traveler_phone ~ '^0[0-9]{9}$') ck_booking_traveler_phone_format (ASM-15). Dữ liệu cá nhân (P09 F7) |
| TBL-07 | phone_reservation | id | VARCHAR(36) | PK | NOT NULL |  | DC-PhoneReservation.reservationId |  | pk_phone_reservation. Thiết kế: như TBL-01.id |
| TBL-07 | phone_reservation | trip_id | VARCHAR(36) | FK | NOT NULL |  | R-33 | TBL-04.id, RESTRICT, NO ACTION (fk_phone_reservation_trip) |  |
| TBL-07 | phone_reservation | status | VARCHAR(20) |  | NOT NULL | 'UNPAID' | DC-PhoneReservation.status |  | CHECK (status IN ('UNPAID','PAID','CANCELLED')) ck_phone_reservation_status (DC-PhoneReservationStatus) |
| TBL-08 | seat | trip_id | VARCHAR(36) | PK, FK | NOT NULL |  | R-23 | TBL-04.id, CASCADE, NO ACTION (fk_seat_trip) | pk_seat (trip_id, seat_code) |
| TBL-08 | seat | seat_code | VARCHAR(10) | PK | NOT NULL |  | DC-Seat.seatCode |  | Duy nhất trong chuyến nhờ khoá chính. Thiết kế: 10 ký tự cho mã chỗ như A05 |
| TBL-08 | seat | status | VARCHAR(20) |  | NOT NULL | 'AVAILABLE' | DC-Seat.status |  | CHECK (status IN ('AVAILABLE','HELD','SOLD')) ck_seat_status (DC-SeatStatus, ST-03). ck_seat_hold: (status = 'HELD') = (holding_booking_id IS NOT NULL) (ASM-55 kết thúc liên kết giữ chỗ khi phát hành vé hoặc trả chỗ). Giữ chỗ bằng cập nhật có điều kiện WHERE status = 'AVAILABLE' (P09 F7) |
| TBL-08 | seat | holding_booking_id | VARCHAR(36) | FK | NULL |  | R-27 | TBL-05.id, RESTRICT, NO ACTION (fk_seat_booking) | Lần đặt đang giữ chỗ; NULL khi chỗ không bị lần đặt giữ. ck_seat_single_holder: không đồng thời có holding_booking_id và phone_reservation_id |
| TBL-08 | seat | phone_reservation_id | VARCHAR(36) | FK | NULL |  | R-37 | TBL-07.id, RESTRICT, NO ACTION (fk_seat_phone_reservation) | Đặt chỗ qua điện thoại gắn với chỗ; số chỗ của một đặt chỗ chờ Q-76; trạng thái chỗ của đặt chỗ này chờ Q-109 |
| TBL-09 | ticket | ticket_code | VARCHAR(20) | PK | NOT NULL |  | DC-Ticket.ticketCode |  | pk_ticket. Khoá tự nhiên được chọn làm khoá chính vì bất biến (readOnly), ngắn, do IF-15 cấp duy nhất toàn hệ thống (BR-10) và là khoá tra cứu của IF-11.findTicket. Thiết kế: 20 ký tự cho mã vé dạng chuỗi, dự phòng định dạng |
| TBL-09 | ticket | booking_id | VARCHAR(36) | FK | NULL |  | R-28 | TBL-05.id, RESTRICT, NO ACTION (fk_ticket_booking) | NULL với vé bán tại quầy (không có lần đặt). ck_ticket_online_has_booking: purchase_channel = 'COUNTER' OR booking_id IS NOT NULL |
| TBL-09 | ticket | trip_id | VARCHAR(36) | FK | NOT NULL |  | R-29, R-30 | TBL-08.(trip_id, seat_code), RESTRICT, NO ACTION (fk_ticket_seat); R-29 thể hiện qua cột này | Chuyến của vé, đồng thời là phần chuyến của khoá ngoại tới chỗ |
| TBL-09 | ticket | seat_code | VARCHAR(10) | FK | NOT NULL |  | R-30 | TBL-08.seat_code (cùng trip_id, fk_ticket_seat), RESTRICT, NO ACTION | uq_ticket_active_seat: UNIQUE (trip_id, seat_code) WHERE status = 'ISSUED' (BR-02, ASM-20): một chỗ có tối đa một vé còn hiệu lực, chỗ được bán lại nên nhiều vé theo thời gian |
| TBL-09 | ticket | traveler_name | VARCHAR(100) |  | NOT NULL |  | DC-Ticket.travelerName |  | CHECK (btrim(traveler_name) <> '') ck_ticket_traveler_name_not_blank. Dữ liệu cá nhân (P09 F7). Thiết kế: 100 ký tự dự phòng cho tên người |
| TBL-09 | ticket | traveler_phone | VARCHAR(10) |  | NOT NULL |  | DC-Ticket.travelerPhone |  | CHECK (traveler_phone ~ '^0[0-9]{9}$') ck_ticket_traveler_phone_format (ASM-15). Dữ liệu cá nhân (P09 F7) |
| TBL-09 | ticket | price | DECIMAL(12,0) |  | NOT NULL |  | DC-Ticket.price |  | CHECK (price > 0) ck_ticket_price. Số tiền khách đã trả cho vé, là cơ sở tính số tiền hoàn (ASM-22); giá tại thời điểm phát hành, không phải dư thừa của base_fare.amount |
| TBL-09 | ticket | status | VARCHAR(20) |  | NOT NULL | 'ISSUED' | DC-Ticket.status |  | CHECK (status IN ('ISSUED','CANCELLED')) ck_ticket_status (DC-TicketStatus, ST-02) |
| TBL-09 | ticket | purchase_channel | VARCHAR(20) |  | NOT NULL |  | DC-Ticket.purchaseChannel |  | CHECK (purchase_channel IN ('ONLINE','COUNTER')) ck_ticket_purchase_channel (DC-PurchaseChannel, GL-13) |
| TBL-09 | ticket | checked_time | TIMESTAMP |  | NULL |  | DC-Ticket.checkedTime |  | Giờ địa phương, không múi giờ. NULL khi vé chưa soát; có giá trị khi trạng thái Checked của ST-02 (ASM-35) |
| TBL-10 | refund | ticket_code | VARCHAR(20) | PK, FK | NOT NULL |  | R-32 | TBL-09.ticket_code, CASCADE, NO ACTION (fk_refund_ticket) | pk_refund. Khoản hoàn định danh bằng vé (P12 F1) |
| TBL-10 | refund | refund_amount | DECIMAL(12,0) |  | NOT NULL |  | DC-Refund.refundAmount |  | CHECK (refund_amount >= 0) ck_refund_amount (BR-13, BR-14, BR-17). Số tiền thực tế ghi nhận lúc hoàn, giữ nguyên sau khi tạo |
| TBL-10 | refund | refund_rate_percent | INTEGER |  | NOT NULL |  | DC-Refund.refundRatePercent |  | CHECK (refund_rate_percent BETWEEN 0 AND 100) ck_refund_rate (GL-24) |
| TBL-10 | refund | refund_method | VARCHAR(20) |  | NOT NULL |  | DC-Refund.refundMethod |  | CHECK (refund_method IN ('VIA_GATEWAY','CASH_AT_COUNTER')) ck_refund_method (DC-RefundMethod, BR-15, BR-16) |
| TBL-10 | refund | refund_outcome | VARCHAR(30) |  | NOT NULL |  | DC-Refund.refundOutcome |  | CHECK (refund_outcome IN ('REFUNDED','FAILED','AWAITING_CASH_PAYOUT')) ck_refund_outcome (DC-RefundOutcome, ASM-54). Thiết kế: 30 ký tự dự phòng cho giá trị enumeration |

Khoá ghép: pk_booking_traveler (booking_id, seat_code), pk_seat (trip_id, seat_code). ON UPDATE của mọi khoá ngoại là NO ACTION vì khoá bất biến (readOnly).

### F6.2. Ánh xạ kiểu dữ liệu

| Kiểu thiết kế | Kiểu vật lý đã dùng (PostgreSQL) |
|---|---|
| String có độ dài tối đa | VARCHAR(n): mã định danh 36 (id), mã vé 20, mã chỗ 10, tên người 100, tên điểm 100, số điện thoại 10, enumeration 20 (30 cho refund_outcome), mã tham chiếu cổng thanh toán 100. Độ dài đều là quyết định thiết kế (C1 mục 7) trừ số điện thoại 10 chữ số theo ASM-15 |
| Integer | INTEGER |
| Decimal (tiền) | DECIMAL(12,0), không dùng FLOAT hoặc REAL |
| Date / DateTime | DATE; TIMESTAMP không múi giờ (giờ địa phương Asia/Ho_Chi_Minh) |
| Enumeration | VARCHAR(n) kèm CHECK tập giá trị (không dùng bảng danh mục) |
| Định danh thay thế | VARCHAR(36) theo kiểu String của định danh trong P12; mã vé làm khoá tự nhiên VARCHAR(20) |
| Khoảng ngày không chồng nhau | Ràng buộc EXCLUDE USING gist trên daterange(start_date, end_date, '[]') |

### F6.3. Index

Khoá chính và UNIQUE (uq_route_points, uq_base_fare_route_bus_type, uq_trip_route_departure) đã có index và phục vụ các truy vấn dưới đây. Bảng chỉ liệt kê index tạo thêm và các index có sẵn được dùng cho truy vấn chính.

| TBL | Tên index | Cột (theo thứ tự) | Loại (UNIQUE / thường / khác) | Phục vụ truy vấn (UC bước / NFR) |
|---|---|---|---|---|
| TBL-01 | uq_route_points (có sẵn) | departure_point, arrival_point | UNIQUE | UC-002 bước 2: IF-10.findTrips nối tuyến theo điểm đi, điểm đến |
| TBL-02 | uq_base_fare_route_bus_type (có sẵn) | route_id, bus_type | UNIQUE | UC-002 bước 8, BR-04: tra giá vé theo tuyến và loại xe; fk_trip_base_fare |
| TBL-03 | ex_holiday_surcharge_period (có sẵn) | daterange(start_date, end_date, '[]') | khác (gist) | BR-05: tra mức tăng giá chứa ngày xuất bến; UC-002 bước 8 |
| TBL-04 | uq_trip_route_departure (có sẵn) | route_id, departure_time | UNIQUE | UC-002 bước 2: IF-10.findTrips lọc chuyến của tuyến theo ngày xuất bến; UC-013 bước 2: IF-10.findTrip theo tuyến và giờ xuất bến; fk_trip_route |
| TBL-05 | ix_booking_held_start | hold_start_time WHERE status = 'HELD' | thường (index một phần) | BR-07, BR-08: Scheduling duyệt các lần đặt HELD đã quá hạn giữ chỗ (P09 F7) |
| TBL-07 | ix_phone_reservation_trip_status | trip_id, status | thường | UC-013 bước 3, 5: IF-11.findPhoneReservationsOfTrip lấy đặt chỗ chưa thanh toán của chuyến; fk_phone_reservation_trip |
| TBL-08 | pk_seat (có sẵn) | trip_id, seat_code | UNIQUE | UC-002 bước 4: nạp sơ đồ chỗ và đếm chỗ trống của chuyến (BR-03) |
| TBL-08 | ix_seat_holding_booking | holding_booking_id WHERE holding_booking_id IS NOT NULL | thường (index một phần) | UC-002: nạp Booking.seats (R-27) khi hết hạn giữ chỗ và phát hành vé; fk_seat_booking |
| TBL-08 | ix_seat_phone_reservation | phone_reservation_id WHERE phone_reservation_id IS NOT NULL | thường (index một phần) | Nạp chỗ của đặt chỗ qua điện thoại (R-37); fk_seat_phone_reservation |
| TBL-09 | ix_ticket_trip_seat | trip_id, seat_code | thường | UC-013 bước 3, 5; UC-015 bước 2, 5: IF-11.findTicketsOfTrip lấy mọi vé của chuyến kèm trạng thái; fk_ticket_seat |
| TBL-09 | uq_ticket_active_seat | trip_id, seat_code WHERE status = 'ISSUED' | UNIQUE (index một phần) | BR-02, ASM-20: mỗi chỗ tối đa một vé còn hiệu lực; UC-015 bước 2: đếm vé còn hiệu lực của chuyến |
| TBL-09 | ix_ticket_booking | booking_id WHERE booking_id IS NOT NULL | thường (index một phần) | UC-002 bước 13: lấy các vé của lần đặt (getBookingSummary); fk_ticket_booking |

Không tạo index cho booking.trip_id: không có truy vấn theo chuyến trên booking trong bốn UC đã phân tích và việc xoá trip không nằm trong UC nào. Không tạo index cho khoá ngoại fk_trip_base_fare ở phía trip vì base_fare hiếm khi bị xoá. Khoá chính của ticket, refund, booking_traveler phục vụ tra theo mã vé (UC-008 bước 2, IF-11.findTicket) và theo lần đặt.

## F7. Mô hình tài liệu

Không áp dụng: CSDL là quan hệ (F1).

## F8. ERD

### F8.1. ERD logic/vật lý

File diagrams/P13-erd-logical.drawio. Danh sách cột của từng bảng lấy từ F6.1 (nhãn dạng "PK tên: KIỂU").

Node (x, y, w, h là toạ độ trong file):

| ID (TBL) | Loại (Table / Collection / Note) | Nhãn (tên bảng) | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| TBL-01 | Table | route | «table» | - | 3 cột | 80 | 40 | 260 | 104 |
| TBL-02 | Table | base_fare | «table» | - | 4 cột | 440 | 40 | 260 | 130 |
| TBL-03 | Table | holiday_surcharge | «table» | - | 4 cột | 1100 | 40 | 260 | 130 |
| TBL-04 | Table | trip | «table» | - | 5 cột | 280 | 280 | 260 | 156 |
| TBL-05 | Table | booking | «table» | - | 8 cột | 80 | 560 | 260 | 234 |
| TBL-06 | Table | booking_traveler | «table» | - | 4 cột | 80 | 900 | 240 | 130 |
| TBL-07 | Table | phone_reservation | «table» | - | 3 cột | 840 | 560 | 260 | 104 |
| TBL-08 | Table | seat | «table» | - | 5 cột | 400 | 900 | 280 | 156 |
| TBL-09 | Table | ticket | «table» | - | 10 cột | 400 | 1200 | 260 | 286 |
| TBL-10 | Table | refund | «table» | - | 5 cột | 400 | 1600 | 260 | 156 |
| NOTE-R25 | Note | R-25 không có khoá ngoại | - | - | Mức tăng giá tra theo ngày xuất bến, xem F4.2 | 1100 | 230 | 300 | 110 |

Edge (nguồn là bảng cha, đích là bảng con chứa FK; đầu cha và đầu con theo ký pháp chân chim):

| ID (tên ràng buộc fk_...) | Nguồn (bảng cha) | Đích (bảng con chứa FK) | Loại quan hệ (Phụ thuộc / Độc lập) | Nhãn / multiplicity (ký pháp chân chim hai đầu) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| fk_base_fare_route | TBL-01 | TBL-02 | Độc lập | ERmandOne (1) --> ERzeroToMany (0..*) | R-31 | - |
| fk_trip_route | TBL-01 | TBL-04 | Độc lập | ERmandOne (1) --> ERzeroToMany (0..*) | R-22 | - |
| fk_trip_base_fare | TBL-02 | TBL-04 | Độc lập | ERmandOne (1) --> ERzeroToMany (0..*) | R-24; khoá ngoại ghép (route_id, bus_type) | - |
| fk_booking_trip | TBL-04 | TBL-05 | Độc lập | ERmandOne (1) --> ERzeroToMany (0..*) | R-26 | - |
| fk_phone_reservation_trip | TBL-04 | TBL-07 | Độc lập | ERmandOne (1) --> ERzeroToMany (0..*) | R-33 | (970,358) |
| fk_seat_trip | TBL-04 | TBL-08 | Phụ thuộc | ERmandOne (1) --> ERoneToMany (1..*) | R-23, composition | - |
| fk_booking_traveler_booking | TBL-05 | TBL-06 | Phụ thuộc | ERmandOne (1) --> ERoneToMany (1..*) | Thuộc tính đa trị travelerInfos của Booking | - |
| fk_seat_booking | TBL-05 | TBL-08 | Độc lập | ERzeroToOne (0..1) --> ERoneToMany (1..5) | R-27 | (370,700); (370,978) |
| fk_seat_phone_reservation | TBL-07 | TBL-08 | Độc lập | ERzeroToOne (0..1) --> ERzeroToMany (0..*) | R-37, số chỗ của đặt chỗ chờ Q-76 | (900,978) |
| fk_ticket_booking | TBL-05 | TBL-09 | Độc lập | ERzeroToOne (0..1) --> ERzeroToMany (0..5) | R-28 | (40,620); (40,1340) |
| fk_ticket_seat | TBL-08 | TBL-09 | Độc lập | ERmandOne (1) --> ERzeroToMany (0..*) | R-29, R-30; khoá ngoại ghép (trip_id, seat_code) | - |
| fk_refund_ticket | TBL-09 | TBL-10 | Phụ thuộc | ERmandOne (1) --> ERzeroToOne (0..1) | R-32, composition | - |

Không có cạnh riêng cho R-29 (cùng khoá ngoại ghép fk_ticket_seat) và R-25 (không có khoá ngoại). Cạnh nét liền là quan hệ phụ thuộc, nét đứt là quan hệ độc lập.

### F8.2. ER khái niệm (Chen)

File diagrams/P13-erd-conceptual.drawio. Thực thể yếu: E-Seat, E-Refund (viền kép). Mối quan hệ xác định thực thể yếu: ER-02, ER-11 (thoi viền kép). Bản số ghi trên đoạn nối giữa thực thể và hình thoi.

Node (toạ độ là góc trên trái; ID thuộc tính AT-<E>-<ten>, mối quan hệ ER-nn, thực thể E-<Ten>):

| ID | Loại | Nhãn | Thuộc về | x | y | w | h |
|---|---|---|---|---|---|---|---|
| E-Route | Entity | Route | - | 590 | 470 | 140 | 60 |
| E-BaseFare | Entity | BaseFare | - | 1590 | 470 | 140 | 60 |
| E-HolidaySurcharge | Entity | HolidaySurcharge | - | 2590 | 470 | 140 | 60 |
| E-Booking | Entity | Booking | - | 590 | 1370 | 140 | 60 |
| E-Trip | Entity | Trip | - | 1590 | 1370 | 140 | 60 |
| E-PhoneReservation | Entity | PhoneReservation | - | 2590 | 1370 | 140 | 60 |
| E-Ticket | Entity | Ticket | - | 590 | 2270 | 140 | 60 |
| E-Seat | Entity (yếu) | Seat | - | 1590 | 2270 | 140 | 60 |
| E-Refund | Entity (yếu) | Refund | - | 590 | 3170 | 140 | 60 |
| ER-01 | Relationship | chạy theo | - | 1095 | 910 | 130 | 80 |
| ER-02 | Relationship (xác định thực thể yếu) | gồm | - | 1595 | 1810 | 130 | 80 |
| ER-03 | Relationship | áp dụng giá | - | 1595 | 910 | 130 | 80 |
| ER-04 | Relationship | chịu mức tăng | - | 2095 | 910 | 130 | 80 |
| ER-05 | Relationship | đặt cho | - | 1095 | 1360 | 130 | 80 |
| ER-06 | Relationship | giữ | - | 895 | 1630 | 130 | 80 |
| ER-07 | Relationship | phát hành | - | 595 | 1810 | 130 | 80 |
| ER-08 | Relationship | thuộc chuyến | - | 895 | 1990 | 130 | 80 |
| ER-09 | Relationship | dành cho chỗ | - | 1095 | 2260 | 130 | 80 |
| ER-10 | Relationship | định giá cho | - | 1095 | 460 | 130 | 80 |
| ER-11 | Relationship (xác định thực thể yếu) | hoàn tiền cho | - | 595 | 2710 | 130 | 80 |
| ER-12 | Relationship | giữ chỗ trên | - | 2095 | 1360 | 130 | 80 |
| ER-13 | Relationship | đặt giữ | - | 2095 | 1810 | 130 | 80 |
| AT-Route-routeId | Attribute (định danh) | routeId | E-Route | 380 | 120 | 150 | 40 |
| AT-Route-departurePoint | Attribute | departurePoint | E-Route | 160 | 480 | 150 | 40 |
| AT-Route-arrivalPoint | Attribute | arrivalPoint | E-Route | 370 | 840 | 150 | 40 |
| AT-BaseFare-baseFareId | Attribute (định danh) | baseFareId | E-BaseFare | 1800 | 120 | 150 | 40 |
| AT-BaseFare-busType | Attribute | busType | E-BaseFare | 1580 | 60 | 150 | 40 |
| AT-BaseFare-amount | Attribute | amount | E-BaseFare | 1380 | 120 | 150 | 40 |
| AT-HolidaySurcharge-holidaySurchargeId | Attribute (định danh) | holidaySurchargeId | E-HolidaySurcharge | 2990 | 330 | 150 | 40 |
| AT-HolidaySurcharge-startDate | Attribute | startDate | E-HolidaySurcharge | 2760 | 90 | 150 | 40 |
| AT-HolidaySurcharge-endDate | Attribute | endDate | E-HolidaySurcharge | 2410 | 90 | 150 | 40 |
| AT-HolidaySurcharge-ratePercent | Attribute | ratePercent | E-HolidaySurcharge | 2180 | 330 | 150 | 40 |
| AT-Booking-bookingId | Attribute (định danh) | bookingId | E-Booking | 330 | 930 | 150 | 40 |
| AT-Booking-ticketPrice | Attribute | ticketPrice | E-Booking | 220 | 1010 | 150 | 40 |
| AT-Booking-totalAmount | Attribute | totalAmount | E-Booking | 130 | 1120 | 150 | 40 |
| AT-Booking-holdStartTime | Attribute | holdStartTime | E-Booking | 70 | 1290 | 150 | 40 |
| AT-Booking-status | Attribute | status | E-Booking | 70 | 1470 | 150 | 40 |
| AT-Booking-paymentAttemptCount | Attribute | paymentAttemptCount | E-Booking | 130 | 1640 | 150 | 40 |
| AT-Booking-paymentReference | Attribute | paymentReference | E-Booking | 250 | 1780 | 150 | 40 |
| AT-Booking-travelerInfos | Attribute (đa trị, phức hợp) | travelerInfos | E-Booking | 800 | 1850 | 150 | 40 |
| AT-Trip-tripId | Attribute (định danh) | tripId | E-Trip | 2090 | 1250 | 150 | 40 |
| AT-Trip-departureTime | Attribute | departureTime | E-Trip | 2050 | 1140 | 150 | 40 |
| AT-Trip-busType | Attribute | busType | E-Trip | 1880 | 950 | 150 | 40 |
| AT-Trip-status | Attribute | status | E-Trip | 1390 | 900 | 150 | 40 |
| AT-Trip-availableSeatCount | Attribute (dẫn xuất) | availableSeatCount | E-Trip | 1690 | 810 | 150 | 40 |
| AT-PhoneReservation-reservationId | Attribute (định danh) | reservationId | E-PhoneReservation | 2910 | 1650 | 150 | 40 |
| AT-PhoneReservation-status | Attribute | status | E-PhoneReservation | 2660 | 970 | 150 | 40 |
| AT-Ticket-ticketCode | Attribute (định danh) | ticketCode | E-Ticket | 250 | 1880 | 150 | 40 |
| AT-Ticket-travelerName | Attribute | travelerName | E-Ticket | 130 | 2020 | 150 | 40 |
| AT-Ticket-travelerPhone | Attribute | travelerPhone | E-Ticket | 70 | 2190 | 150 | 40 |
| AT-Ticket-price | Attribute | price | E-Ticket | 70 | 2370 | 150 | 40 |
| AT-Ticket-status | Attribute | status | E-Ticket | 130 | 2540 | 150 | 40 |
| AT-Ticket-purchaseChannel | Attribute | purchaseChannel | E-Ticket | 250 | 2680 | 150 | 40 |
| AT-Ticket-checkedTime | Attribute | checkedTime | E-Ticket | 800 | 2750 | 150 | 40 |
| AT-Seat-seatCode | Attribute (định danh riêng phần) | seatCode | E-Seat | 1510 | 2700 | 150 | 40 |
| AT-Seat-status | Attribute | status | E-Seat | 1990 | 2430 | 150 | 40 |
| AT-Refund-refundAmount | Attribute | refundAmount | E-Refund | 260 | 2900 | 150 | 40 |
| AT-Refund-refundRatePercent | Attribute | refundRatePercent | E-Refund | 160 | 3180 | 150 | 40 |
| AT-Refund-refundMethod | Attribute | refundMethod | E-Refund | 260 | 3460 | 150 | 40 |
| AT-Refund-refundOutcome | Attribute | refundOutcome | E-Refund | 510 | 3600 | 150 | 40 |

Edge (Chen):

| ID | Nguồn | Đích | Loại | Bản số | Ghi chú |
|---|---|---|---|---|---|
| ED-ER-01-A | E-Trip | ER-01 | Nối | N | R-22 |
| ED-ER-01-B | E-Route | ER-01 | Nối | 1 | R-22 |
| ED-ER-02-A | E-Trip | ER-02 | Nối | 1 | R-23 |
| ED-ER-02-B | E-Seat | ER-02 | Nối | N | R-23 |
| ED-ER-03-A | E-Trip | ER-03 | Nối | N | R-24 |
| ED-ER-03-B | E-BaseFare | ER-03 | Nối | 1 | R-24 |
| ED-ER-04-A | E-Trip | ER-04 | Nối | N | R-25 |
| ED-ER-04-B | E-HolidaySurcharge | ER-04 | Nối | 1 | R-25 |
| ED-ER-05-A | E-Booking | ER-05 | Nối | N | R-26 |
| ED-ER-05-B | E-Trip | ER-05 | Nối | 1 | R-26 |
| ED-ER-06-A | E-Booking | ER-06 | Nối | 1 | R-27 |
| ED-ER-06-B | E-Seat | ER-06 | Nối | N | R-27 |
| ED-ER-07-A | E-Booking | ER-07 | Nối | 1 | R-28 |
| ED-ER-07-B | E-Ticket | ER-07 | Nối | N | R-28 |
| ED-ER-08-A | E-Ticket | ER-08 | Nối | N | R-29 |
| ED-ER-08-B | E-Trip | ER-08 | Nối | 1 | R-29 |
| ED-ER-09-A | E-Ticket | ER-09 | Nối | N | R-30 |
| ED-ER-09-B | E-Seat | ER-09 | Nối | 1 | R-30 |
| ED-ER-10-A | E-BaseFare | ER-10 | Nối | N | R-31 |
| ED-ER-10-B | E-Route | ER-10 | Nối | 1 | R-31 |
| ED-ER-11-A | E-Ticket | ER-11 | Nối | 1 | R-32 |
| ED-ER-11-B | E-Refund | ER-11 | Nối | 1 | R-32 |
| ED-ER-12-A | E-PhoneReservation | ER-12 | Nối | N | R-33 |
| ED-ER-12-B | E-Trip | ER-12 | Nối | 1 | R-33 |
| ED-ER-13-A | E-PhoneReservation | ER-13 | Nối | 1 | R-37 |
| ED-ER-13-B | E-Seat | ER-13 | Nối | N | R-37 |
| EA-Route-routeId | E-Route | AT-Route-routeId | Nối | - | Thuộc tính |
| EA-Route-departurePoint | E-Route | AT-Route-departurePoint | Nối | - | Thuộc tính |
| EA-Route-arrivalPoint | E-Route | AT-Route-arrivalPoint | Nối | - | Thuộc tính |
| EA-BaseFare-baseFareId | E-BaseFare | AT-BaseFare-baseFareId | Nối | - | Thuộc tính |
| EA-BaseFare-busType | E-BaseFare | AT-BaseFare-busType | Nối | - | Thuộc tính |
| EA-BaseFare-amount | E-BaseFare | AT-BaseFare-amount | Nối | - | Thuộc tính |
| EA-HolidaySurcharge-holidaySurchargeId | E-HolidaySurcharge | AT-HolidaySurcharge-holidaySurchargeId | Nối | - | Thuộc tính |
| EA-HolidaySurcharge-startDate | E-HolidaySurcharge | AT-HolidaySurcharge-startDate | Nối | - | Thuộc tính |
| EA-HolidaySurcharge-endDate | E-HolidaySurcharge | AT-HolidaySurcharge-endDate | Nối | - | Thuộc tính |
| EA-HolidaySurcharge-ratePercent | E-HolidaySurcharge | AT-HolidaySurcharge-ratePercent | Nối | - | Thuộc tính |
| EA-Booking-bookingId | E-Booking | AT-Booking-bookingId | Nối | - | Thuộc tính |
| EA-Booking-ticketPrice | E-Booking | AT-Booking-ticketPrice | Nối | - | Thuộc tính |
| EA-Booking-totalAmount | E-Booking | AT-Booking-totalAmount | Nối | - | Thuộc tính |
| EA-Booking-holdStartTime | E-Booking | AT-Booking-holdStartTime | Nối | - | Thuộc tính |
| EA-Booking-status | E-Booking | AT-Booking-status | Nối | - | Thuộc tính |
| EA-Booking-paymentAttemptCount | E-Booking | AT-Booking-paymentAttemptCount | Nối | - | Thuộc tính |
| EA-Booking-paymentReference | E-Booking | AT-Booking-paymentReference | Nối | - | Thuộc tính |
| EA-Booking-travelerInfos | E-Booking | AT-Booking-travelerInfos | Nối | - | Thuộc tính |
| EA-Trip-tripId | E-Trip | AT-Trip-tripId | Nối | - | Thuộc tính |
| EA-Trip-departureTime | E-Trip | AT-Trip-departureTime | Nối | - | Thuộc tính |
| EA-Trip-busType | E-Trip | AT-Trip-busType | Nối | - | Thuộc tính |
| EA-Trip-status | E-Trip | AT-Trip-status | Nối | - | Thuộc tính |
| EA-Trip-availableSeatCount | E-Trip | AT-Trip-availableSeatCount | Nối | - | Thuộc tính |
| EA-PhoneReservation-reservationId | E-PhoneReservation | AT-PhoneReservation-reservationId | Nối | - | Thuộc tính |
| EA-PhoneReservation-status | E-PhoneReservation | AT-PhoneReservation-status | Nối | - | Thuộc tính |
| EA-Ticket-ticketCode | E-Ticket | AT-Ticket-ticketCode | Nối | - | Thuộc tính |
| EA-Ticket-travelerName | E-Ticket | AT-Ticket-travelerName | Nối | - | Thuộc tính |
| EA-Ticket-travelerPhone | E-Ticket | AT-Ticket-travelerPhone | Nối | - | Thuộc tính |
| EA-Ticket-price | E-Ticket | AT-Ticket-price | Nối | - | Thuộc tính |
| EA-Ticket-status | E-Ticket | AT-Ticket-status | Nối | - | Thuộc tính |
| EA-Ticket-purchaseChannel | E-Ticket | AT-Ticket-purchaseChannel | Nối | - | Thuộc tính |
| EA-Ticket-checkedTime | E-Ticket | AT-Ticket-checkedTime | Nối | - | Thuộc tính |
| EA-Seat-seatCode | E-Seat | AT-Seat-seatCode | Nối | - | Thuộc tính |
| EA-Seat-status | E-Seat | AT-Seat-status | Nối | - | Thuộc tính |
| EA-Refund-refundAmount | E-Refund | AT-Refund-refundAmount | Nối | - | Thuộc tính |
| EA-Refund-refundRatePercent | E-Refund | AT-Refund-refundRatePercent | Nối | - | Thuộc tính |
| EA-Refund-refundMethod | E-Refund | AT-Refund-refundMethod | Nối | - | Thuộc tính |
| EA-Refund-refundOutcome | E-Refund | AT-Refund-refundOutcome | Nối | - | Thuộc tính |

## F9. Script DDL

Không sinh script (SINH_DDL = Không có).

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-109 | Chỗ gắn với đặt chỗ qua điện thoại chưa thanh toán (R-37) có chuyển sang trạng thái đang giữ để không bán cho lần đặt khác không, và khi quá hạn thanh toán (BR-24) chỗ được xử lý ra sao? (Chỗ chuyển HELD như chỗ của lần đặt trực tuyến / Chỗ giữ nguyên trạng thái và chỉ kiểm tra qua liên kết đặt chỗ) | TBL-08.status, ck_seat_hold, ck_seat_single_holder, fk_seat_phone_reservation; ST-03 | P12 F6.1: trạng thái Held của ST-03 "gắn với lần đặt qua Booking.seats" trong khi R-37 và GL-07 nói đặt chỗ qua điện thoại giữ chỗ; liên quan Q-76, Q-05 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-108 | Mỗi cặp (điểm đi, điểm đến) là đúng một tuyến. | Nguồn gọi tuyến bằng nhãn "<Điểm đi> - <Điểm đến>" (P12 F1 IF-10.findTrip; UC-013 nhận diện chuyến theo tuyến và giờ xuất bến), nên cặp điểm phải xác định một tuyến; nguồn không nêu có tuyến trùng điểm đi và điểm đến hay không | TBL-01 uq_route_points |
| ASM-109 | Một tuyến có tối đa một chuyến tại một giờ xuất bến. | IF-10.findTrip(route, departureDateTime) trả về một Trip và UC-013 nhận diện chuyến cần huỷ theo tuyến và giờ xuất bến; nguồn không nêu hai xe chạy cùng tuyến cùng giờ | TBL-04 uq_trip_route_departure |
| ASM-110 | Chỗ của đặt chỗ qua điện thoại chưa thanh toán không chuyển status sang HELD trong mô hình dữ liệu này; việc giữ chỗ thể hiện bằng seat.phone_reservation_id. | ST-03 của P12 chỉ định trạng thái Held gắn với lần đặt (Booking.seats); P13 không thêm trạng thái mà P12 chưa có. Chờ Q-109 | TBL-08.status, ck_seat_hold, ck_seat_single_holder |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P12 | ST-03, R-37 | ST-03 định nghĩa Held là chỗ gắn với lần đặt qua Booking.seats, còn R-37 cho PhoneReservation giữ chỗ nhưng ST-03 không có chuyển trạng thái cho trường hợp này (Q-109) | Khi chạy lại P12 cùng P07 của UC-004 đến UC-006, bổ sung chuyển trạng thái của DC-Seat cho đặt chỗ qua điện thoại hoặc ghi rõ chỗ của đặt chỗ không đổi trạng thái |
| P12 | R-25 | P12 để P13 quyết định lưu liên kết hay truy vấn theo ngày; P13 chọn truy vấn theo ngày, không lưu khoá ngoại | Ghi trong P12 rằng R-25 là liên kết suy ra theo ngày xuất bến (Repository nạp mức tăng áp dụng), không phải thuộc tính lưu |
| P12 | Giao ước PKG-28 DC-Money | P13 lưu tiền bằng DECIMAL(12,0), giả định Money là số nguyên đồng | Khi thiết kế PKG-28, ghi Money có đơn vị đồng, giá trị nguyên không âm; nếu Money cần phần thập phân thì P13 chạy lại |

## Vấn đề còn mở

- Target 6 và 7: đạt cho cả 10 bảng; các FD dựa trên BR và ASM-108, ASM-109, ASM-105. FD của TBL-03 (start_date là khoá) suy ra từ ASM-105 nên đổi theo Q-20 (phạm vi tuyến, loại xe của mức tăng giá).
- Dữ liệu của DC-PhoneReservation chỉ có hai thuộc tính (reservationId, status) cộng liên kết tới chuyến và chỗ; UC-004, UC-005, UC-006 chưa phân tích nên bảng phone_reservation tối thiểu. Cần chạy lại P13 khi P12 bổ sung thuộc tính.
- Trạng thái chỗ lưu thành cột (ASM-42) trong khi Q-75 chưa trả lời; nếu trả lời là suy ra từ vé và đặt chỗ thì bỏ seat.status, ck_seat_hold và đổi các index của seat.
- Ràng buộc liên bảng ở cuối F4.2 do ứng dụng giữ; chưa có trigger hoặc ràng buộc CSDL tương ứng.
- Phiên bản PostgreSQL và thời gian lưu dữ liệu chuyến, vé chưa được nguồn nêu; chưa có chiến lược lưu trữ hoặc phân vùng.
- Mã Q và ASM cấp tiếp từ Q-108 và ASM-107, là số lớn nhất trong các file đầu vào đã đọc; P07, P08, P10, P11a, P11b không nằm trong đầu vào của bước này nên có thể đã có mã lớn hơn.
- Chọn giữa hai quy tắc (C9): F6.1/Bước 4 yêu cầu multiplicity 0..1 --> NULL, còn ASM-44 nói lần đặt DRAFT không được lưu; đã giữ NULL cho ticket_price, total_amount, hold_start_time, payment_reference và thêm CHECK theo status (ck_booking_state, ck_booking_payment_reference).
- Chọn giữa hai quy tắc (C9): quy tắc khoá chính mặc định là khoá thay thế id, còn ticket_code là khoá tự nhiên; đã chọn ticket_code vì thoả điều kiện bất biến, ngắn và duy nhất (lý do ở F1).
- Chọn giữa hai quy tắc (C9): F8.2 vẽ cạnh Chen bằng endArrow=none, còn C7.3 yêu cầu orthogonalEdgeStyle cho ERD; đã dùng cạnh thẳng cho ER khái niệm theo F8.2 và orthogonalEdgeStyle cho ERD logic.
- Hai file .drawio được kiểm bằng tính toán (toạ độ bội số 10, khoảng cách tối thiểu 40, cạnh không cắt qua node, XML hợp lệ); chưa mở bằng draw.io để xem nhãn và nét vẽ. Sơ đồ Chen rộng khoảng 3.000 đơn vị.

