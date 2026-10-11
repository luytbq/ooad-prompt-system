# X2 - Thiết kế unit test - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | X2 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (CONG_NGHE: Java 17, Spring Boot; CHE_DO_GIA_DINH = CO_NHAN; MUC_CHI_TIET = DAY_DU); P12-class-design/PKG-09-PKG-22-PKG-23-ticket-sales-catalog-ticketing.md 1.0 (F1, F2, F3, F6, F7, F7a); P06-supplementary-spec.md 1.0 (BR-01 đến BR-22); P04-uc-specs/UC-002, UC-008, UC-013, UC-015 (1.0); P13-data-model.md 1.0 (ràng buộc price > 0, CHECK enumeration, DECIMAL(12,0)). Không có mã nguồn. Tham số: PHAM_VI_TEST = DC-TicketReturnPolicy, DC-Booking, DC-Ticket trong PKG-23 Ticketing, AI chọn các operation có quy tắc nghiệp vụ; MUC_TIEU_PHU, SINH_MA_TEST, MA_TC_BAT_DAU, YEU_CAU_BO_SUNG = Không có (dùng mặc định: 100% C1 cho phương thức ưu tiên Cao, 100% C0 cho phương thức còn lại; TC bắt đầu từ TC-001; không sinh khung mã) |
| Phạm vi | DC-TicketReturnPolicy, DC-Booking, DC-Ticket (PKG-23 Ticketing); UC-002, UC-008, UC-013, UC-015 |

## Quy ước dùng trong file

- Hộp trắng ở mức thiết kế: không có mã nguồn, CFG dựng từ P12 F3. Phương thức không có thiết kế method ở F3 chỉ có phân tích hộp đen; mục tiêu C0, C1 của chúng chỉ ước tính (xem F4).
- Điều kiện hợp lệ của toán tử kiểm tra (trả Boolean hoặc một giá trị phân loại): "Hợp lệ" nghĩa là lớp cho kết quả thuận theo BR (true, được phép), "Không hợp lệ" là lớp cho kết quả từ chối; giá trị trong ngoặc ghi kết quả cụ thể.
- Dữ liệu dùng chung: TI-A05 = TravelerInfo(A05, "Nguyễn Văn An", "0912345678"); TI-A06 = (A06, "Trần Thị Bình", "0987654321"); TI-A07 = (A07, "Lê Văn Cường", "0901234567"); TI-A08 = (A08, "Phạm Thị Dung", "0932345678"); TI-A09 = (A09, "Hoàng Văn Em", "0945678901"); TI-A10 = (A10, "Vũ Thị Hà", "0956789012"). Chuyến giả lập khởi hành 21:00 03/02/2027, giá một vé 360.000 đ (ví dụ P04 UC-002, UC-008). Booking mặc định có bookingId BK-0001. Mọi Seat của chuyến giả lập ở trạng thái AVAILABLE trừ khi điều kiện đầu ghi khác.
- Thời điểm hiện tại không được lấy từ đồng hồ hệ thống: now, requestTime, checkTime truyền qua tham số (P12 Quy ước áp dụng), nên không cần đồng hồ giả lập trong phạm vi này.
- Lớp null của tham số tham chiếu có EC riêng nhưng không có TC, theo ASM-111. TC có kết quả chưa xác định (Q-nn) vẫn được liệt kê ở F3 để giữ chỗ và đánh dấu "Chưa xác định: chờ Q-nn".

## F1. Bảng chọn operation

| DC.operation | Tiêu chí (BR / rẽ nhánh / tính toán / sự kiện ST / kiểm tra hợp lệ / điều phối UC / gọi hệ thống ngoài) | Ưu tiên (Cao / Trung bình / Thấp) | Chọn (Có / Không: lý do) |
|---|---|---|---|
| DC-TicketReturnPolicy.matchesPurchaseChannel | BR-11; rẽ nhánh; kiểm tra hợp lệ | Cao | Có |
| DC-TicketReturnPolicy.getTimeToDeparture | ủy quyền (hỏi DC-Trip.calculateTimeToDeparture) | Thấp | Không: chỉ ủy quyền nguyên lời gọi sang DC-Trip.calculateTimeToDeparture, không có quy tắc riêng; hành vi tính thời gian còn lại thuộc DC-Trip (ngoài phạm vi), quy tắc ngưỡng đã được kiểm ở isReturnTimeAllowed và calculateRefundAmount |
| DC-TicketReturnPolicy.isReturnTimeAllowed | BR-12; rẽ nhánh; kiểm tra hợp lệ | Cao | Có |
| DC-TicketReturnPolicy.calculateRefundAmount | BR-13, BR-14; tính toán; rẽ nhánh | Cao | Có |
| DC-TicketReturnPolicy.getTicketReturnInfo | chuyển đổi dữ liệu để hiển thị (UC-008 Dữ liệu ra 1) | Trung bình | Có |
| DC-TicketReturnPolicy.determineRefundMethod | BR-15, BR-16; rẽ nhánh | Cao | Có |
| DC-TicketReturnPolicy.getCancelImpactInfo | BR-17; chuyển đổi dữ liệu | Trung bình | Có |
| DC-TicketReturnPolicy.calculateTripCancelRefundAmount | BR-17, BR-19; tính toán | Cao | Có |
| DC-Booking.createBooking | kiểm tra hợp lệ; sự kiện ST-01 (T1) | Trung bình | Có |
| DC-Booking.isWithinSeatLimit | BR-01; rẽ nhánh; kiểm tra hợp lệ | Cao | Có |
| DC-Booking.validateTravelerInfo | ASM-15; kiểm tra hợp lệ; rẽ nhánh; vòng lặp | Cao | Có |
| DC-Booking.calculateTotal | BR-06; tính toán; kiểm tra trạng thái | Cao | Có |
| DC-Booking.holdSeats | sự kiện ST-01 (T2); BR-03, BR-07; vòng lặp; gọi phụ thuộc | Cao | Có |
| DC-Booking.releaseSeats | sự kiện ST-01 (T4); BR-08; vòng lặp | Cao | Có |
| DC-Booking.issueTickets | BR-09, BR-10; sự kiện ST-01 (T3); vòng lặp; gọi phụ thuộc | Cao | Có |
| DC-Booking.getBookingSummary | kiểm tra trạng thái; chuyển đổi dữ liệu (UC-002 Dữ liệu ra 4) | Trung bình | Có |
| DC-Booking.getHoldExpiryTime | BR-07; tính toán thời gian | Cao | Có |
| DC-Booking.isHoldExpired | BR-07; rẽ nhánh; thời gian | Cao | Có |
| DC-Booking.startPaymentAttempt | kiểm tra trạng thái; sinh khoá yêu cầu thanh toán | Trung bình | Có |
| DC-Booking.getBookingId | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Booking.getTotalAmount | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Booking.getStatus | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Booking.getTrip | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Ticket.createTicket | BR-09, BR-10; kiểm tra hợp lệ; sự kiện ST-02 (T1) | Trung bình | Có |
| DC-Ticket.isCancelled | kiểm tra điều kiện (UC-008 luồng 2b) | Thấp | Có |
| DC-Ticket.cancelTicket | BR-15, BR-16; sự kiện ST-02 (T3, T5); rẽ nhánh; gọi phụ thuộc | Cao | Có |
| DC-Ticket.cancelWithTrip | BR-17, BR-19; sự kiện ST-02 (T4, T6) | Cao | Có |
| DC-Ticket.recordRefund | BR-15, BR-16, BR-17; kiểm tra điều kiện trạng thái; rẽ nhánh | Cao | Có |
| DC-Ticket.determineCheckResult | BR-21, BR-22; rẽ nhánh; kiểm tra hợp lệ | Cao | Có |
| DC-Ticket.markChecked | BR-22; sự kiện ST-02 (T2); rẽ nhánh | Cao | Có |
| DC-Ticket.getTicketCode | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Ticket.getTravelerName | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Ticket.getTravelerPhone | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Ticket.getPrice | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Ticket.getPurchaseChannel | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Ticket.getSeatCode | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |
| DC-Ticket.getTrip | getter | Thấp | Không: getter không có logic (không kèm điều kiện, ngoại lệ) |

Ngoài phạm vi (không có dòng): các operation của DC-TripCancellation, DC-TicketSmsContent, DC-Refund, DC-PhoneReservation cùng PKG-23 không nằm trong PHAM_VI_TEST. Kiểm thử DC-Refund.createRefund (miền refundRatePercent, refundAmount) được ghi nhận gián tiếp qua Q-111.

## F2. Phân tích kỹ thuật cho từng operation

### F2.1 DC-TicketReturnPolicy.matchesPurchaseChannel

Chữ ký: matchesPurchaseChannel(ticket: Ticket, requestChannel: PurchaseChannel): Boolean. Ưu tiên: Cao. Tiêu chí: BR-11; rẽ nhánh; kiểm tra hợp lệ.

#### F2.1.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | matchesPurchaseChannel(ticket: Ticket, requestChannel: PurchaseChannel): Boolean | P12 F2 |
| Tiền điều kiện / hậu điều kiện | Hậu: không đổi (vé và policy không thay đổi) | P12 F2 |
| Ngoại lệ | Không có | P12 F2 |
| BR | BR-11: vé chỉ được trả qua kênh đã mua; vé mua tại quầy gồm vé đặt qua điện thoại đã thanh toán tại quầy | P06 BR-11; P04 UC-008 Mục 6 |
| Luồng thay thế | 3a: vé mua qua kênh khác kênh đang yêu cầu trả --> từ chối | P04 UC-008 Mục 3 |
| Điều kiện hợp lệ | PurchaseChannel chỉ có ONLINE, COUNTER | P12 F7a |

#### F2.1.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-01 | Kênh mua của vé và kênh yêu cầu | Cả hai là ONLINE (trùng) | Hợp lệ | ticket ONLINE, request ONLINE | BR-11 |
| EC-02 | Kênh mua của vé và kênh yêu cầu | Cả hai là COUNTER (trùng) | Hợp lệ | ticket COUNTER, request COUNTER | BR-11 |
| EC-03 | Kênh mua của vé và kênh yêu cầu | Vé ONLINE, yêu cầu COUNTER (khác) | Không hợp lệ | ticket ONLINE, request COUNTER | BR-11, UC-008 3a |
| EC-04 | Kênh mua của vé và kênh yêu cầu | Vé COUNTER, yêu cầu ONLINE (khác) | Không hợp lệ | ticket COUNTER, request ONLINE | BR-11, UC-008 3a |
| EC-05 | ticket hoặc requestChannel | null | Không hợp lệ | null | ASM-111 |

#### F2.1.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.1.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT1-Q1 | DT1-Q2 | DT1-Q3 | DT1-Q4 |
| C1: Kênh mua của vé là ONLINE | Y | N | Y | N |
| C2: Kênh yêu cầu trả là ONLINE | Y | N | N | Y |
| A1: Trả true (cho phép tiếp tục trả vé) | X | X | - | - |
| A2: Trả false (từ chối theo luồng 3a) | - | - | X | X |
```

Hai điều kiện nhị phân, bốn quy tắc, không có tổ hợp N/A và không gộp.

#### F2.1.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.1.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.1.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Ticket | stub | getPurchaseChannel(), getPrice() trả giá trị định sẵn theo điều kiện đầu của từng TC; getTrip() trả DC-Trip stub | Cô lập quy tắc của policy khỏi vòng đời Ticket |

### F2.2 DC-TicketReturnPolicy.isReturnTimeAllowed

Chữ ký: isReturnTimeAllowed(timeToDeparture: Duration): Boolean. Ưu tiên: Cao. Tiêu chí: BR-12; rẽ nhánh; kiểm tra hợp lệ.

#### F2.2.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isReturnTimeAllowed(timeToDeparture: Duration): Boolean | P12 F2 |
| Hậu điều kiện | Không đổi; "đúng 4 giờ vẫn được trả" | P12 F2 |
| Ngoại lệ | Không có | P12 F2 |
| BR | BR-12: vé không được trả khi thời gian còn lại dưới 4 giờ (MIN_RETURN_TIME = 4 giờ) | P06 BR-12; P12 F7 |
| Luồng thay thế | 3b: còn dưới 4 giờ --> từ chối | P04 UC-008 Mục 3 |
| Điều kiện hợp lệ | Thời gian còn lại âm khi requestTime sau giờ xuất bến (Trip.calculateTimeToDeparture) | P12 F2 DC-Trip |

#### F2.2.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-06 | timeToDeparture | timeToDeparture < 0 (đã qua giờ xuất bến) | Không hợp lệ | PT-1H | BR-12; P12 F2 DC-Trip.calculateTimeToDeparture |
| EC-07 | timeToDeparture | 0 <= timeToDeparture < 4 giờ | Không hợp lệ | PT2H | BR-12, UC-008 3b |
| EC-08 | timeToDeparture | timeToDeparture >= 4 giờ | Hợp lệ | PT30H | BR-12 |
| EC-09 | timeToDeparture | null | Không hợp lệ | null | ASM-111 |

#### F2.2.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-01 | của EC-06 | PT-1S (ngay dưới giờ xuất bến) | EC-06 | Trả false |
| BV-02 | của EC-07 | PT0S (đúng giờ xuất bến) | EC-07 | Trả false |
| BV-03 | của EC-07 | PT3H59M59S (ngay dưới 4 giờ) | EC-07 | Trả false (ASM-113) |
| BV-04 | của EC-08 | PT4H (đúng 4 giờ) | EC-08 | Trả true ("đúng 4 giờ vẫn được trả") |
| BV-05 | của EC-08 | PT4H1S (ngay trên biên) | EC-08 | Trả true |

#### F2.2.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện (so sánh với MIN_RETURN_TIME).

#### F2.2.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.2.6 Hộp trắng

Không có CFG: V(G) = 1 theo mô tả P12 F3 ("trả timeToDeparture >= MIN_RETURN_TIME"): một biểu thức so sánh trả Boolean, không có điểm quyết định; không vẽ CFG. Biên của phép so sánh được kiểm bằng giá trị biên.

#### F2.2.7 Test double

Không có phụ thuộc cần giả lập: phương thức thuần, chỉ nhận Duration và hằng của lớp; không truy cập CSDL, hệ thống ngoài, thời gian hệ thống hay số ngẫu nhiên.

### F2.3 DC-TicketReturnPolicy.calculateRefundAmount

Chữ ký: calculateRefundAmount(ticket: Ticket, timeToDeparture: Duration): RefundQuote. Ưu tiên: Cao. Tiêu chí: BR-13, BR-14; tính toán; rẽ nhánh.

#### F2.3.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | calculateRefundAmount(ticket: Ticket, timeToDeparture: Duration): RefundQuote | P12 F2 |
| Tiền điều kiện | isReturnTimeAllowed(timeToDeparture) là true | P12 F2 |
| Hậu điều kiện | Không đổi; RefundQuote(ratePercent, amount) với ratePercent là 50 hoặc 90 | P12 F2, F7 |
| Ngoại lệ | IllegalArgumentException khi tiền điều kiện sai | P12 F2, F3 |
| BR | BR-13: từ 24 giờ trở lên hoàn 90% giá vé; BR-14: từ 4 giờ đến dưới 24 giờ hoàn 50% giá vé | P06 BR-13, BR-14 |
| Công thức | amount = giá vé x mức hoàn, làm tròn đến đồng HALF_UP | P12 F3; ASM-102 |
| Ví dụ P04 | Giá 360.000 đ: còn 49 giờ --> 324.000 đ; còn 12 giờ --> 180.000 đ; đúng 24 giờ --> 90%; đúng 4 giờ --> 50%; 3 giờ --> không được trả | P04 UC-008 Mục 5 |
| Điều kiện hợp lệ | Ticket.price > 0 (bất biến của Ticket) | P12 F7 |

#### F2.3.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-10 | timeToDeparture | < 4 giờ (kể cả âm) | Không hợp lệ | PT3H | BR-12; P12 F2 tiền điều kiện |
| EC-11 | timeToDeparture | 4 giờ <= timeToDeparture < 24 giờ | Hợp lệ | PT12H | BR-14 |
| EC-12 | timeToDeparture | >= 24 giờ | Hợp lệ | PT49H | BR-13 |
| EC-13 | amount = price x rate / 100 | Chia hết, kết quả nguyên đồng | Hợp lệ | price 360.000, rate 90 --> 324.000 | ASM-102 |
| EC-14 | amount = price x rate / 100 | Không chia hết, cần làm tròn HALF_UP | Hợp lệ | price 1.005, rate 50 --> 502,5 --> 503 | ASM-102 |
| EC-15 | ticket hoặc timeToDeparture | null | Không hợp lệ | null | ASM-111 |

#### F2.3.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-06 | của EC-10 | PT3H59M59S (ngay dưới 4 giờ) | EC-10 | Ném IllegalArgumentException |
| BV-07 | của EC-11 | PT4H (đúng 4 giờ) | EC-11 | ratePercent 50, amount 180.000 đ (UC-008 Mục 5) |
| BV-08 | của EC-11 | PT4H1S | EC-11 | ratePercent 50 |
| BV-09 | của EC-11 | PT23H59M59S (ngay dưới 24 giờ) | EC-11 | ratePercent 50 |
| BV-10 | của EC-12 | PT24H (đúng 24 giờ) | EC-12 | ratePercent 90, amount 324.000 đ (UC-008 Mục 5) |
| BV-11 | của EC-12 | PT24H1S | EC-12 | ratePercent 90 |

#### F2.3.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT2-Q1 | DT2-Q2 | DT2-Q3 | DT2-Q4 |
| C1: isReturnTimeAllowed(timeToDeparture) là true (>= 4 giờ) | Y | Y | N | N |
| C2: timeToDeparture >= 24 giờ | Y | N | Y | N |
| A1: RefundQuote(90, price x 90 / 100) | X | - | N/A | - |
| A2: RefundQuote(50, price x 50 / 100) | - | X | N/A | - |
| A3: Ném IllegalArgumentException | - | - | N/A | X |
```

Q3 là N/A: không thể đồng thời dưới 4 giờ và từ 24 giờ trở lên. Không gộp quy tắc.

#### F2.3.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.3.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N1 | Bắt đầu | bắt đầu |
| N2 | không isReturnTimeAllowed(timeToDeparture)? | quyết định |
| N3 | ném IllegalArgumentException | khối lệnh |
| N4 | timeToDeparture >= FULL_RATE_TIME? | quyết định |
| N5 | rate = HIGH_RATE_PERCENT (90) | khối lệnh |
| N6 | rate = LOW_RATE_PERCENT (50) | khối lệnh |
| N7 | amount = ticket.getPrice().percent(rate); trả RefundQuote(rate, amount) | khối lệnh |
| N8 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE1 | N1 | N2 | rỗng |
| CE2 | N2 | N3 | Đúng |
| CE3 | N2 | N4 | Sai |
| CE4 | N4 | N5 | Đúng |
| CE5 | N4 | N6 | Sai |
| CE6 | N5 | N7 | rỗng |
| CE7 | N6 | N7 | rỗng |
| CE8 | N7 | N8 | rỗng |
| CE9 | N3 | N8 | rỗng |

V(G) = E - N + 2 = 9 - 8 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 3 trên V(G) = 3):

- P1 (TC TC-013): N1 - N2 - N3 - N8
- P2 (TC TC-015): N1 - N2 - N4 - N6 - N7 - N8
- P3 (TC TC-019): N1 - N2 - N4 - N5 - N7 - N8

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE1 (N1 --> N2) | TC-013 đến TC-023 |
| CE2 (N2 --> N3, Đúng) | TC-013, TC-014 |
| CE3 (N2 --> N4, Sai) | TC-015 đến TC-023 |
| CE4 (N4 --> N5, Đúng) | TC-019 đến TC-021, TC-023 |
| CE5 (N4 --> N6, Sai) | TC-015 đến TC-018, TC-022 |
| CE6 (N5 --> N7) | TC-019 đến TC-021, TC-023 |
| CE7 (N6 --> N7) | TC-015 đến TC-018, TC-022 |
| CE8 (N7 --> N8) | TC-015 đến TC-023 |
| CE9 (N3 --> N8) | TC-013, TC-014 |
| N1 (lệnh/điểm quyết định) | TC-013 đến TC-023 |
| N2 (lệnh/điểm quyết định) | TC-013 đến TC-023 |
| N3 (lệnh/điểm quyết định) | TC-013, TC-014 |
| N4 (lệnh/điểm quyết định) | TC-015 đến TC-023 |
| N5 (lệnh/điểm quyết định) | TC-019 đến TC-021, TC-023 |
| N6 (lệnh/điểm quyết định) | TC-015 đến TC-018, TC-022 |
| N7 (lệnh/điểm quyết định) | TC-015 đến TC-023 |
| N8 (lệnh/điểm quyết định) | TC-013 đến TC-023 |

Độ phủ đạt được: C0 = 8/8 = 100%; C1 = 9/9 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-TicketReturnPolicy-calculateRefundAmount.drawio (ID cell trùng N, CE).

#### F2.3.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Ticket | stub | getPurchaseChannel(), getPrice() trả giá trị định sẵn theo điều kiện đầu của từng TC; getTrip() trả DC-Trip stub | Cô lập quy tắc của policy khỏi vòng đời Ticket |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.4 DC-TicketReturnPolicy.getTicketReturnInfo

Chữ ký: getTicketReturnInfo(ticket: Ticket): TicketReturnInfo. Ưu tiên: Trung bình. Tiêu chí: chuyển đổi dữ liệu để hiển thị (UC-008 Dữ liệu ra 1).

#### F2.4.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | getTicketReturnInfo(ticket: Ticket): TicketReturnInfo | P12 F2 |
| Hậu điều kiện | Không đổi; cung cấp mã vé, tuyến, giờ xuất bến, mã chỗ, giá vé | P12 F2, F7 DC-TicketReturnInfo |
| Ngoại lệ | Không có | P12 F2 |
| Luồng | Bước 5 hiển thị thông tin vé: Dữ liệu ra 1 #1 đến #4 | P04 UC-008 Mục 5 |

#### F2.4.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-16 | ticket | Vé có đủ mã vé, chuyến, chỗ, giá | Hợp lệ | SV0000123, A05, 360.000 đ | P04 UC-008 Dữ liệu ra 1 |
| EC-17 | ticket | null | Không hợp lệ | null | ASM-111 |

#### F2.4.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.4.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.4.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.4.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.4.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Ticket | stub | getPurchaseChannel(), getPrice() trả giá trị định sẵn theo điều kiện đầu của từng TC; getTrip() trả DC-Trip stub | Cô lập quy tắc của policy khỏi vòng đời Ticket |
| DC-Trip | stub | getRouteAndDepartureTime() trả TripSchedule("Hà Nội - Lào Cai", 21:00 03/02/2027) | Lấy lịch chuyến cố định |

### F2.5 DC-TicketReturnPolicy.determineRefundMethod

Chữ ký: determineRefundMethod(ticket: Ticket): RefundMethod. Ưu tiên: Cao. Tiêu chí: BR-15, BR-16; rẽ nhánh.

#### F2.5.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | determineRefundMethod(ticket: Ticket): RefundMethod | P12 F2 |
| Hậu điều kiện | Không đổi; ONLINE --> VIA_GATEWAY, COUNTER --> CASH_AT_COUNTER | P12 F2 |
| BR | BR-15: vé mua trực tuyến hoàn qua cổng thanh toán; BR-16: vé mua tại quầy hoàn bằng tiền mặt tại quầy | P06 BR-15, BR-16 |
| Luồng | UC-008 bước 7, luồng 7a; UC-013 bước 6 (ASM-28) | P04 UC-008, UC-013 |

#### F2.5.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-18 | ticket.purchaseChannel | ONLINE | Hợp lệ | ONLINE | BR-15 |
| EC-19 | ticket.purchaseChannel | COUNTER | Hợp lệ | COUNTER | BR-16 |
| EC-20 | ticket | null | Không hợp lệ | null | ASM-111 |

#### F2.5.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.5.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.5.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.5.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.5.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Ticket | stub | getPurchaseChannel(), getPrice() trả giá trị định sẵn theo điều kiện đầu của từng TC; getTrip() trả DC-Trip stub | Cô lập quy tắc của policy khỏi vòng đời Ticket |

### F2.6 DC-TicketReturnPolicy.getCancelImpactInfo

Chữ ký: getCancelImpactInfo(ticket: Ticket): CancelImpactInfo. Ưu tiên: Trung bình. Tiêu chí: BR-17; chuyển đổi dữ liệu.

#### F2.6.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | getCancelImpactInfo(ticket: Ticket): CancelImpactInfo | P12 F2 |
| Hậu điều kiện | Không đổi; trả kênh mua và số tiền hoàn bằng 100% giá vé | P12 F2, F7 DC-CancelImpactInfo |
| BR | BR-17: số tiền hoàn của vé thuộc chuyến bị huỷ bằng 100% giá vé | P06 BR-17 |
| Luồng | UC-013 bước 3: tổng số tiền hoàn theo kênh mua | P04 UC-013 Mục 2 |

#### F2.6.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-21 | ticket.purchaseChannel | ONLINE | Hợp lệ | ONLINE, price 360.000 đ | BR-17 |
| EC-22 | ticket.purchaseChannel | COUNTER | Hợp lệ | COUNTER, price 300.000 đ | BR-17 |
| EC-23 | ticket | null | Không hợp lệ | null | ASM-111 |

#### F2.6.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.6.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.6.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.6.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.6.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Ticket | stub | getPurchaseChannel(), getPrice() trả giá trị định sẵn theo điều kiện đầu của từng TC; getTrip() trả DC-Trip stub | Cô lập quy tắc của policy khỏi vòng đời Ticket |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.7 DC-TicketReturnPolicy.calculateTripCancelRefundAmount

Chữ ký: calculateTripCancelRefundAmount(ticket: Ticket): Money. Ưu tiên: Cao. Tiêu chí: BR-17, BR-19; tính toán.

#### F2.7.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | calculateTripCancelRefundAmount(ticket: Ticket): Money | P12 F2 |
| Hậu điều kiện | Không đổi; 100% giá vé đã thanh toán, không phụ thuộc thời gian còn lại | P12 F2 |
| BR | BR-17: 100% giá vé; BR-19: mọi vé còn hiệu lực được hoàn theo BR-17 | P06 BR-17, BR-19 |
| Điều kiện hợp lệ | Ticket.price > 0 (bất biến) | P12 F7 |

#### F2.7.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-24 | ticket.price | price > 0, vé ONLINE | Hợp lệ | 360.000 đ | BR-17 |
| EC-25 | ticket.price | price > 0, vé COUNTER | Hợp lệ | 300.000 đ | BR-17 |
| EC-26 | ticket | null | Không hợp lệ | null | ASM-111 |

#### F2.7.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-12 | của EC-24 | price = 1 đ (nhỏ nhất hợp lệ của price > 0) | EC-24 | Trả 1 đ (không làm tròn sai) |

#### F2.7.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.7.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.7.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.7.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Ticket | stub | getPurchaseChannel(), getPrice() trả giá trị định sẵn theo điều kiện đầu của từng TC; getTrip() trả DC-Trip stub | Cô lập quy tắc của policy khỏi vòng đời Ticket |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.8 DC-Booking.createBooking

Chữ ký: createBooking(bookingId: String, trip: Trip, travelerInfos: List<TravelerInfo>): Booking. Ưu tiên: Trung bình. Tiêu chí: kiểm tra hợp lệ; sự kiện ST-01 (T1).

#### F2.8.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | createBooking(bookingId: String, trip: Trip, travelerInfos: List<TravelerInfo>): Booking (classifier) | P12 F2 |
| Tiền điều kiện | travelerInfos không rỗng | P12 F2 |
| Hậu điều kiện | status DRAFT, paymentAttemptCount 0; chưa kiểm tra quy tắc và chưa lưu | P12 F2; ASM-43, ASM-44 |
| Ngoại lệ | IllegalArgumentException | P12 F2 |
| Thuộc tính | travelerInfos {mỗi seatCode một phần tử} | P12 F7 |
| State machine | ST-01 T1: (initial) --createBooking--> Draft | P12 F6.2 |

#### F2.8.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-27 | Số phần tử travelerInfos | 1 đến 5 | Hợp lệ | 2 | P12 F2 tiền điều kiện; BR-01 |
| EC-28 | Số phần tử travelerInfos | >= 6 (chưa kiểm BR-01 ở đây, chỉ isWithinSeatLimit kiểm) | Hợp lệ | 6 | ASM-43 |
| EC-29 | Số phần tử travelerInfos | 0 (rỗng) | Không hợp lệ | [] | P12 F2 tiền điều kiện |
| EC-30 | seatCode của các phần tử | Có hai phần tử trùng seatCode | Chưa xác định (Q-114) | A05, A05 | P12 F7 {mỗi seatCode một phần tử} |
| EC-31 | bookingId, trip hoặc travelerInfos | null | Không hợp lệ | null | ASM-111 |

#### F2.8.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-13 | của EC-29 | size = 0 | EC-29 | Ném IllegalArgumentException |
| BV-14 | của EC-27 | size = 1 | EC-27 | Booking DRAFT |
| BV-15 | của EC-27 | size = 5 | EC-27 | Booking DRAFT |
| BV-16 | của EC-28 | size = 6 | EC-28 | Booking DRAFT (không từ chối) |

#### F2.8.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.8.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| (initial) | createBooking(bookingId, trip, travelerInfos) | - | status = DRAFT, paymentAttemptCount = 0 | Draft | ST-01 T1 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.8.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho createBooking; V(G) ước theo mô tả = 2 (một điểm quyết định: travelerInfos rỗng).

#### F2.8.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |

### F2.9 DC-Booking.isWithinSeatLimit

Chữ ký: isWithinSeatLimit(): Boolean. Ưu tiên: Cao. Tiêu chí: BR-01; rẽ nhánh; kiểm tra hợp lệ.

#### F2.9.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isWithinSeatLimit(): Boolean | P12 F2 |
| Hậu điều kiện | Không đổi; true khi số chỗ không quá MAX_SEATS | P12 F2 |
| BR | BR-01: tối đa 5 chỗ trong một lần đặt trực tuyến (MAX_SEATS = 5) | P06 BR-01; P12 F7 |
| Luồng thay thế | 6a: số chỗ đã chọn lớn hơn 5 --> từ chối | P04 UC-002 Mục 3 |

#### F2.9.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-32 | Số chỗ của lần đặt | 1 đến 5 | Hợp lệ | 2 | BR-01 |
| EC-33 | Số chỗ của lần đặt | >= 6 | Không hợp lệ | 6 | BR-01, UC-002 6a |
| EC-34 | Số chỗ của lần đặt | 0 chỗ | Không thể xảy ra | - | createBooking chặn danh sách rỗng (P12 F2) |

#### F2.9.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-17 | của EC-32 | size = 1 | EC-32 | Trả true |
| BV-18 | của EC-32 | size = 5 | EC-32 | Trả true |
| BV-19 | của EC-33 | size = 6 | EC-33 | Trả false |

#### F2.9.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.9.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.9.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method; V(G) ước theo mô tả = 1 (so sánh size <= MAX_SEATS).

#### F2.9.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |

### F2.10 DC-Booking.validateTravelerInfo

Chữ ký: validateTravelerInfo(): TravelerInfoProblem. Ưu tiên: Cao. Tiêu chí: ASM-15; kiểm tra hợp lệ; rẽ nhánh; vòng lặp.

#### F2.10.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | validateTravelerInfo(): TravelerInfoProblem | P12 F2 |
| Hậu điều kiện | Không đổi. Thiếu thông tin được báo trước sai định dạng (Q-34, ASM-15) | P12 F2 |
| Ngoại lệ | Không có | P12 F2 |
| Giá trị trả về | NONE, MISSING_INFO, INVALID_PHONE | P12 F7a |
| Luồng thay thế | 7a: thiếu họ tên hoặc số điện thoại của ít nhất một chỗ; 7b: thông tin đủ và có ít nhất một số điện thoại sai định dạng | P04 UC-002 Mục 3 |
| Điều kiện hợp lệ | Họ tên không để trống (ASM-15); số điện thoại gồm 10 chữ số, bắt đầu bằng 0 (ASM-15) | P04 UC-002 Dữ liệu vào 2 |
| Thiết kế method | F3: quét mọi phần tử tìm họ tên rỗng sau khi cắt hoặc số điện thoại rỗng (MISSING_INFO); sau đó quét tìm số điện thoại sai (INVALID_PHONE); còn lại NONE | P12 F3 |

#### F2.10.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-35 | travelerName của một chỗ | Có ít nhất một ký tự không phải khoảng trắng | Hợp lệ | Nguyễn Văn An | ASM-15 |
| EC-36 | travelerName của một chỗ | Chuỗi rỗng | Không hợp lệ | "" | ASM-15, UC-002 7a |
| EC-37 | travelerName của một chỗ | Chỉ gồm khoảng trắng | Không hợp lệ | "   " | P12 F3 (cắt khoảng trắng) |
| EC-38 | travelerPhone của một chỗ | 10 chữ số, bắt đầu bằng 0 | Hợp lệ | 0912345678 | ASM-15 |
| EC-39 | travelerPhone của một chỗ | Chuỗi rỗng | Không hợp lệ | "" | UC-002 7a |
| EC-40 | travelerPhone của một chỗ | Toàn chữ số, ít hơn 10 chữ số | Không hợp lệ | 091234567 | ASM-15, UC-002 7b |
| EC-41 | travelerPhone của một chỗ | Toàn chữ số, nhiều hơn 10 chữ số | Không hợp lệ | 09123456789 | ASM-15, UC-002 7b |
| EC-42 | travelerPhone của một chỗ | Đúng 10 chữ số, không bắt đầu bằng 0 | Không hợp lệ | 1912345678 | ASM-15, UC-002 7b |
| EC-43 | travelerPhone của một chỗ | Có ký tự không phải chữ số (khác rỗng) | Không hợp lệ | 09123abc78 | ASM-15, UC-002 7b |
| EC-44 | Số phần tử travelerInfos | 1 đến 5 | Hợp lệ | 2 | BR-01; P12 F2 createBooking |
| EC-45 | Số phần tử travelerInfos | 0 hoặc >= 6 | Không thể xảy ra tại đây | - | 0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3) |

#### F2.10.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-20 | của EC-36 | Họ tên "" (độ dài sau cắt = 0) | EC-36 | MISSING_INFO |
| BV-21 | của EC-35 | Họ tên "A" (độ dài sau cắt = 1) | EC-35 | NONE (khi các trường khác hợp lệ) |
| BV-22 | của EC-40 | Số điện thoại 9 chữ số | EC-40 | INVALID_PHONE |
| BV-23 | của EC-38 | Số điện thoại 10 chữ số | EC-38 | NONE |
| BV-24 | của EC-41 | Số điện thoại 11 chữ số | EC-41 | INVALID_PHONE |

#### F2.10.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT3-Q1 | DT3-Q2 | DT3-Q3 |
| C1: Có chỗ thiếu họ tên hoặc thiếu số điện thoại | Y | N | N |
| C2: Có số điện thoại (khác rỗng) sai định dạng | - | Y | N |
| A1: Trả MISSING_INFO | X | - | - |
| A2: Trả INVALID_PHONE | - | X | - |
| A3: Trả NONE | - | - | X |
```

Q1 gộp (Y, Y) và (Y, N) bằng "-" vì UC-002 luồng 7b chỉ áp dụng khi "thông tin đủ cho mọi chỗ", nên thiếu thông tin luôn được báo trước (Q-34). Hai tổ hợp bị gộp vẫn có TC riêng để kiểm thứ tự.

#### F2.10.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.10.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N9 | Bắt đầu | bắt đầu |
| N10 | còn phần tử travelerInfos chưa duyệt (vòng 1)? | quyết định |
| N11 | travelerName rỗng sau khi cắt khoảng trắng? | quyết định |
| N12 | travelerPhone rỗng? | quyết định |
| N13 | trả MISSING_INFO | khối lệnh |
| N14 | còn phần tử chưa duyệt (vòng 2)? | quyết định |
| N15 | PhoneNumber.isValid(travelerPhone) = false? | quyết định |
| N16 | trả INVALID_PHONE | khối lệnh |
| N17 | trả NONE | khối lệnh |
| N18 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE10 | N9 | N10 | rỗng |
| CE11 | N10 | N11 | Đúng |
| CE12 | N11 | N13 | Đúng |
| CE13 | N11 | N12 | Sai |
| CE14 | N12 | N13 | Đúng |
| CE15 | N12 | N10 | Sai |
| CE16 | N10 | N14 | Sai |
| CE17 | N14 | N15 | Đúng |
| CE18 | N15 | N16 | Đúng |
| CE19 | N15 | N14 | Sai |
| CE20 | N14 | N17 | Sai |
| CE21 | N13 | N18 | rỗng |
| CE22 | N16 | N18 | rỗng |
| CE23 | N17 | N18 | rỗng |

V(G) = E - N + 2 = 14 - 10 + 2 = 6; kiểm tra bằng số điểm quyết định nhị phân + 1 = 5 + 1 = 6; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 6 trên V(G) = 6):

- P1 (TC TC-045): N9 - N10 - N11 - N13 - N18
- P2 (TC TC-047): N9 - N10 - N11 - N12 - N13 - N18
- P3 (TC TC-052): N9 - N10 - N11 - N12 - N10 - N11 - N13 - N18
- P4 (TC TC-048): N9 - N10 - N11 - N12 - N10 - N14 - N15 - N16 - N18
- P5 (TC TC-041): N9 - N10 - N11 - N12 - N10 - N14 - N15 - N14 - N17 - N18
- P6 (TC TC-042): N9 - N10 - N11 - N12 - N10 - N11 - N12 - N10 - N14 - N15 - N14 - N15 - N14 - N17 - N18

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE10 (N9 --> N10) | TC-041 đến TC-056 |
| CE11 (N10 --> N11, Đúng) | TC-041 đến TC-056 |
| CE12 (N11 --> N13, Đúng) | TC-045, TC-046, TC-052, TC-054 |
| CE13 (N11 --> N12, Sai) | TC-041 đến TC-044, TC-047 đến TC-056 |
| CE14 (N12 --> N13, Đúng) | TC-047, TC-053 |
| CE15 (N12 --> N10, Sai) | TC-041 đến TC-044, TC-048 đến TC-056 |
| CE16 (N10 --> N14, Sai) | TC-041 đến TC-044, TC-048 đến TC-051, TC-055, TC-056 |
| CE17 (N14 --> N15, Đúng) | TC-041 đến TC-044, TC-048 đến TC-051, TC-055, TC-056 |
| CE18 (N15 --> N16, Đúng) | TC-048 đến TC-051, TC-055, TC-056 |
| CE19 (N15 --> N14, Sai) | TC-041 đến TC-044, TC-055 |
| CE20 (N14 --> N17, Sai) | TC-041 đến TC-044 |
| CE21 (N13 --> N18) | TC-045 đến TC-047, TC-052 đến TC-054 |
| CE22 (N16 --> N18) | TC-048 đến TC-051, TC-055, TC-056 |
| CE23 (N17 --> N18) | TC-041 đến TC-044 |
| N9 (lệnh/điểm quyết định) | TC-041 đến TC-056 |
| N10 (lệnh/điểm quyết định) | TC-041 đến TC-056 |
| N11 (lệnh/điểm quyết định) | TC-041 đến TC-056 |
| N12 (lệnh/điểm quyết định) | TC-041 đến TC-044, TC-047 đến TC-056 |
| N13 (lệnh/điểm quyết định) | TC-045 đến TC-047, TC-052 đến TC-054 |
| N14 (lệnh/điểm quyết định) | TC-041 đến TC-044, TC-048 đến TC-051, TC-055, TC-056 |
| N15 (lệnh/điểm quyết định) | TC-041 đến TC-044, TC-048 đến TC-051, TC-055, TC-056 |
| N16 (lệnh/điểm quyết định) | TC-048 đến TC-051, TC-055, TC-056 |
| N17 (lệnh/điểm quyết định) | TC-041 đến TC-044 |
| N18 (lệnh/điểm quyết định) | TC-041 đến TC-056 |

Độ phủ đạt được: C0 = 10/10 = 100%; C1 = 14/14 = 100%.

Vòng lặp:

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Vòng 1 (duyệt travelerInfos tìm thiếu thông tin) | 5 | 2 | 0: không áp dụng (createBooking chặn danh sách rỗng); 1, 2, 4, 5; 6: không áp dụng (isWithinSeatLimit chặn trước) | TC-041 đến TC-044, TC-054 đến TC-056 |
| Vòng 2 (duyệt travelerInfos tìm số điện thoại sai) | 5 | 2 | 0: không áp dụng; 1, 2, 4, 5; 6: không áp dụng. Vòng 2 chỉ chạy khi vòng 1 không thấy thiếu thông tin | TC-041 đến TC-044, TC-054 đến TC-056 |

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-validateTravelerInfo.drawio (ID cell trùng N, CE).

#### F2.10.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-PhoneNumber (PKG-28) | fake | isValid(String): 10 chữ số, bắt đầu bằng 0 (ASM-15) | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 |

### F2.11 DC-Booking.calculateTotal

Chữ ký: calculateTotal(): Money. Ưu tiên: Cao. Tiêu chí: BR-06; tính toán; kiểm tra trạng thái.

#### F2.11.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | calculateTotal(): Money | P12 F2 |
| Tiền điều kiện | status DRAFT | P12 F2 |
| Hậu điều kiện | ticketPrice, totalAmount được ghi; ticketPrice chốt một lần dùng cho mọi vé (ASM-22) | P12 F2, F3 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| BR | BR-06: tổng tiền bằng tổng giá vé của các chỗ đã chọn; totalAmount = ticketPrice x số chỗ | P06 BR-06; P12 F7 |
| Ví dụ P04 | Giá một vé 360.000 đ; 2 chỗ --> 720.000 đ | P04 UC-002 Mục 5 |
| Thiết kế method | F3: kiểm status; ticketPrice = trip.determineTicketPrice(); totalAmount = ticketPrice.times(size) | P12 F3 |

#### F2.11.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-46 | status | DRAFT | Hợp lệ | DRAFT | P12 F2 tiền điều kiện |
| EC-47 | status | HELD | Không hợp lệ | HELD | P12 F2 |
| EC-48 | status | TICKETED | Không hợp lệ | TICKETED | P12 F2 |
| EC-49 | status | EXPIRED | Không hợp lệ | EXPIRED | P12 F2 |
| EC-50 | Số chỗ | 1 đến 5 | Hợp lệ | 2 | BR-06, BR-01 |
| EC-51 | Số chỗ | 0 hoặc >= 6 | Không thể xảy ra tại đây | - | 0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3) |

#### F2.11.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-25 | của EC-50 | Số chỗ = 1 | EC-50 | totalAmount = 360.000 đ |
| BV-26 | của EC-50 | Số chỗ = 5 | EC-50 | totalAmount = 1.800.000 đ |

#### F2.11.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.11.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.11.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N19 | Bắt đầu | bắt đầu |
| N20 | status khác DRAFT? | quyết định |
| N21 | ném InvalidStateException | khối lệnh |
| N22 | ticketPrice = trip.determineTicketPrice() | khối lệnh |
| N23 | totalAmount = ticketPrice.times(size); trả totalAmount | khối lệnh |
| N24 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE24 | N19 | N20 | rỗng |
| CE25 | N20 | N21 | Đúng |
| CE26 | N20 | N22 | Sai |
| CE27 | N22 | N23 | rỗng |
| CE28 | N23 | N24 | rỗng |
| CE29 | N21 | N24 | rỗng |

V(G) = E - N + 2 = 6 - 6 + 2 = 2; kiểm tra bằng số điểm quyết định nhị phân + 1 = 1 + 1 = 2; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 2 trên V(G) = 2):

- P1 (TC TC-060): N19 - N20 - N21 - N24
- P2 (TC TC-057): N19 - N20 - N22 - N23 - N24

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE24 (N19 --> N20) | TC-057 đến TC-062 |
| CE25 (N20 --> N21, Đúng) | TC-060 đến TC-062 |
| CE26 (N20 --> N22, Sai) | TC-057 đến TC-059 |
| CE27 (N22 --> N23) | TC-057 đến TC-059 |
| CE28 (N23 --> N24) | TC-057 đến TC-059 |
| CE29 (N21 --> N24) | TC-060 đến TC-062 |
| N19 (lệnh/điểm quyết định) | TC-057 đến TC-062 |
| N20 (lệnh/điểm quyết định) | TC-057 đến TC-062 |
| N21 (lệnh/điểm quyết định) | TC-060 đến TC-062 |
| N22 (lệnh/điểm quyết định) | TC-057 đến TC-059 |
| N23 (lệnh/điểm quyết định) | TC-057 đến TC-059 |
| N24 (lệnh/điểm quyết định) | TC-057 đến TC-062 |

Độ phủ đạt được: C0 = 6/6 = 100%; C1 = 6/6 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-calculateTotal.drawio (ID cell trùng N, CE).

#### F2.11.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.12 DC-Booking.holdSeats

Chữ ký: holdSeats(now: LocalDateTime): void. Ưu tiên: Cao. Tiêu chí: sự kiện ST-01 (T2); BR-03, BR-07; vòng lặp; gọi phụ thuộc.

#### F2.12.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | holdSeats(now: LocalDateTime): void | P12 F2 |
| Tiền điều kiện | status DRAFT; mọi chỗ AVAILABLE | P12 F2; F6.2 guard |
| Hậu điều kiện | Mọi Seat HELD, holdStartTime = now, status HELD | P12 F2 |
| Ngoại lệ | SeatAlreadyHeldException, InvalidStateException | P12 F2 |
| BR | BR-03: chỗ còn trống khi chưa có vé và không đang được giữ cho lần đặt chưa hết hạn; BR-07: giữ 10 phút | P06 BR-03, BR-07 |
| State machine | ST-01 T2: Draft --holdSeats [mọi Seat AVAILABLE]--> Held; sự kiện bị từ chối ở Held, Ticketed, Expired | P12 F6.2 |
| Thiết kế method | F3: kiểm status; seats = trip.findSeats(mã chỗ); với mỗi Seat gọi seat.hold(); sau đó holdStartTime = now, status = HELD. "Tất cả hoặc không" do giao dịch của dịch vụ | P12 F3 |
| Luồng | UC-002 bước 9 (giữ chỗ); luồng 6b (chỗ không còn trống) do dịch vụ kiểm trước | P04 UC-002 |

#### F2.12.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-52 | status | DRAFT | Hợp lệ | DRAFT | P12 F2 tiền điều kiện |
| EC-53 | status | HELD | Không hợp lệ | HELD | P12 F2 tiền điều kiện |
| EC-54 | status | TICKETED | Không hợp lệ | TICKETED | P12 F2 tiền điều kiện |
| EC-55 | status | EXPIRED | Không hợp lệ | EXPIRED | P12 F2 tiền điều kiện |
| EC-56 | Trạng thái các Seat của lần đặt | Mọi Seat AVAILABLE | Hợp lệ | A05, A06 AVAILABLE | BR-03 |
| EC-57 | Trạng thái các Seat của lần đặt | Có Seat không AVAILABLE, Seat không AVAILABLE đầu tiên (theo thứ tự travelerInfos) là HELD bởi lần đặt khác | Không hợp lệ | A05 HELD | BR-03; P12 F6.2 Seat.hold |
| EC-58 | Trạng thái các Seat của lần đặt | Có Seat không AVAILABLE, Seat không AVAILABLE đầu tiên là SOLD | Không hợp lệ | A06 SOLD | BR-02, BR-03; P12 F6.2 Seat.hold |
| EC-59 | Số chỗ | 1 đến 5 | Hợp lệ | 2 | BR-01 |
| EC-60 | Số chỗ | 0 hoặc >= 6 | Không thể xảy ra tại đây | - | 0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3) |
| EC-61 | now | null | Không hợp lệ | null | ASM-111 |

#### F2.12.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-27 | của EC-59 | Số chỗ = 1 | EC-59 | Booking HELD; 1 Seat HELD |
| BV-28 | của EC-59 | Số chỗ = 5 | EC-59 | Booking HELD; 5 Seat HELD |

#### F2.12.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT4-Q1 | DT4-Q2 | DT4-Q3 | DT4-Q4 |
| C1: status của Booking là DRAFT | Y | Y | N | N |
| C2: Mọi Seat của lần đặt là AVAILABLE | Y | N | Y | N |
| A1: Booking HELD, holdStartTime = now, mọi Seat HELD | X | - | - | - |
| A2: Ném SeatAlreadyHeldException, Booking vẫn DRAFT | - | X | - | - |
| A3: Ném InvalidStateException, Booking giữ nguyên | - | - | X | X |
```

Q4 (status sai và có Seat không AVAILABLE) báo InvalidStateException theo thứ tự bước 1 trước bước 3 của P12 F3; không gộp quy tắc. Q4 xảy ra tự nhiên với Booking HELD hoặc TICKETED.

#### F2.12.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Draft | holdSeats(now) | Đúng (mọi Seat AVAILABLE) | holdStartTime = now; mọi Seat HELD | Held | ST-01 T2 |
| Draft | holdSeats(now) | Sai (có Seat HELD hoặc SOLD) | Ném SeatAlreadyHeldException; Booking vẫn Draft | Draft | ST-01 T2 guard |
| Held | holdSeats(now) | - | Ném InvalidStateException; không đổi | Held | P12 F6.2 sự kiện bị từ chối |
| Ticketed | holdSeats(now) | - | Ném InvalidStateException; không đổi | Ticketed | P12 F6.2 |
| Expired | holdSeats(now) | - | Ném InvalidStateException; không đổi | Expired | P12 F6.2 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.12.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N25 | Bắt đầu | bắt đầu |
| N26 | status khác DRAFT? | quyết định |
| N27 | ném InvalidStateException | khối lệnh |
| N28 | seats = trip.findSeats(mã chỗ của travelerInfos) | khối lệnh |
| N29 | còn Seat chưa giữ? | quyết định |
| N30 | seat.hold() ném SeatAlreadyHeldException? | quyết định |
| N31 | SeatAlreadyHeldException lan ra | khối lệnh |
| N32 | seat đã chuyển HELD | khối lệnh |
| N33 | holdStartTime = now; status = HELD | khối lệnh |
| N34 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE30 | N25 | N26 | rỗng |
| CE31 | N26 | N27 | Đúng |
| CE32 | N26 | N28 | Sai |
| CE33 | N28 | N29 | rỗng |
| CE34 | N29 | N30 | Đúng |
| CE35 | N29 | N33 | Sai |
| CE36 | N30 | N31 | Đúng |
| CE37 | N30 | N32 | Sai |
| CE38 | N32 | N29 | rỗng |
| CE39 | N33 | N34 | rỗng |
| CE40 | N27 | N34 | rỗng |
| CE41 | N31 | N34 | rỗng |

V(G) = E - N + 2 = 12 - 10 + 2 = 4; kiểm tra bằng số điểm quyết định nhị phân + 1 = 3 + 1 = 4; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 4 trên V(G) = 4):

- P1 (TC TC-067): N25 - N26 - N27 - N34
- P2 (TC TC-070): N25 - N26 - N28 - N29 - N30 - N31 - N34
- P3 (TC TC-063): N25 - N26 - N28 - N29 - N30 - N32 - N29 - N33 - N34
- P4 (TC TC-071): N25 - N26 - N28 - N29 - N30 - N32 - N29 - N30 - N31 - N34

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE30 (N25 --> N26) | TC-063 đến TC-072 |
| CE31 (N26 --> N27, Đúng) | TC-067 đến TC-069 |
| CE32 (N26 --> N28, Sai) | TC-063 đến TC-066, TC-070 đến TC-072 |
| CE33 (N28 --> N29) | TC-063 đến TC-066, TC-070 đến TC-072 |
| CE34 (N29 --> N30, Đúng) | TC-063 đến TC-066, TC-070 đến TC-072 |
| CE35 (N29 --> N33, Sai) | TC-063 đến TC-066 |
| CE36 (N30 --> N31, Đúng) | TC-070 đến TC-072 |
| CE37 (N30 --> N32, Sai) | TC-063 đến TC-066, TC-071, TC-072 |
| CE38 (N32 --> N29) | TC-063 đến TC-066, TC-071, TC-072 |
| CE39 (N33 --> N34) | TC-063 đến TC-066 |
| CE40 (N27 --> N34) | TC-067 đến TC-069 |
| CE41 (N31 --> N34) | TC-070 đến TC-072 |
| N25 (lệnh/điểm quyết định) | TC-063 đến TC-072 |
| N26 (lệnh/điểm quyết định) | TC-063 đến TC-072 |
| N27 (lệnh/điểm quyết định) | TC-067 đến TC-069 |
| N28 (lệnh/điểm quyết định) | TC-063 đến TC-066, TC-070 đến TC-072 |
| N29 (lệnh/điểm quyết định) | TC-063 đến TC-066, TC-070 đến TC-072 |
| N30 (lệnh/điểm quyết định) | TC-063 đến TC-066, TC-070 đến TC-072 |
| N31 (lệnh/điểm quyết định) | TC-070 đến TC-072 |
| N32 (lệnh/điểm quyết định) | TC-063 đến TC-066, TC-071, TC-072 |
| N33 (lệnh/điểm quyết định) | TC-063 đến TC-066 |
| N34 (lệnh/điểm quyết định) | TC-063 đến TC-072 |

Độ phủ đạt được: C0 = 10/10 = 100%; C1 = 12/12 = 100%.

Vòng lặp:

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Vòng giữ từng Seat | 5 | 2 | 0: không áp dụng (createBooking chặn danh sách rỗng); 1, 2, 4, 5; 6: không áp dụng (isWithinSeatLimit chặn trước; holdSeats không tự kiểm, ASM-43). Vị trí Seat lỗi: đầu, cuối | TC-064 đến TC-066, TC-072 |

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-holdSeats.drawio (ID cell trùng N, CE).

#### F2.12.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

### F2.13 DC-Booking.releaseSeats

Chữ ký: releaseSeats(): void. Ưu tiên: Cao. Tiêu chí: sự kiện ST-01 (T4); BR-08; vòng lặp.

#### F2.13.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | releaseSeats(): void | P12 F2 |
| Tiền / hậu điều kiện | Tiền: HELD (khác thì bỏ qua). Hậu: mọi Seat AVAILABLE, status EXPIRED | P12 F2 |
| Ngoại lệ | Không có | P12 F2 |
| BR | BR-08: hết thời hạn giữ chỗ mà chưa thanh toán thì chỗ về trạng thái còn trống | P06 BR-08 |
| State machine | ST-01 T4: Held --releaseSeats--> Expired; ở Draft, Ticketed, Expired bỏ qua | P12 F6.2 |
| Thiết kế method | F3: nếu status khác HELD thì kết thúc; với mỗi Seat gọi release(); xoá liên kết seats; status = EXPIRED. Mốc hết hạn được giao ít nhất một lần nên gọi lặp phải vô hại | P12 F3 |
| Luồng | 9a1: trả các chỗ đang giữ về còn trống | P04 UC-002 Mục 3 |

#### F2.13.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-62 | status | HELD | Hợp lệ | HELD | P12 F2 |
| EC-63 | status | DRAFT (bỏ qua) | Hợp lệ (không đổi) | DRAFT | P12 F2, F6.2 |
| EC-64 | status | TICKETED (bỏ qua) | Hợp lệ (không đổi) | TICKETED | P12 F2, F6.2 |
| EC-65 | status | EXPIRED (bỏ qua) | Hợp lệ (không đổi) | EXPIRED | P12 F2, F6.2 |
| EC-66 | Số Seat đang giữ | 1 đến 5 | Hợp lệ | 2 | BR-01 |
| EC-67 | Số chỗ | 0 hoặc >= 6 | Không thể xảy ra tại đây | - | 0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3) |

#### F2.13.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-29 | của EC-66 | Số Seat = 1 | EC-66 | Seat AVAILABLE; status EXPIRED |
| BV-30 | của EC-66 | Số Seat = 5 | EC-66 | 5 Seat AVAILABLE; status EXPIRED |

#### F2.13.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định (status là HELD).

#### F2.13.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Held | releaseSeats() | - | Seat.release từng chỗ | Expired | ST-01 T4 |
| Draft | releaseSeats() | - | Bỏ qua, không ngoại lệ | Draft | P12 F6.2 |
| Ticketed | releaseSeats() | - | Bỏ qua, không ngoại lệ | Ticketed | P12 F6.2 |
| Expired | releaseSeats() | - | Bỏ qua, không ngoại lệ | Expired | P12 F6.2 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.13.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N35 | Bắt đầu | bắt đầu |
| N36 | status khác HELD? | quyết định |
| N37 | kết thúc, bỏ qua | khối lệnh |
| N38 | còn Seat chưa trả? | quyết định |
| N39 | seat.release() | khối lệnh |
| N40 | xoá liên kết seats; status = EXPIRED | khối lệnh |
| N41 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE42 | N35 | N36 | rỗng |
| CE43 | N36 | N37 | Đúng |
| CE44 | N36 | N38 | Sai |
| CE45 | N38 | N39 | Đúng |
| CE46 | N39 | N38 | rỗng |
| CE47 | N38 | N40 | Sai |
| CE48 | N40 | N41 | rỗng |
| CE49 | N37 | N41 | rỗng |

V(G) = E - N + 2 = 8 - 7 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 3 trên V(G) = 3):

- P1 (TC TC-078): N35 - N36 - N37 - N41
- P2 (TC TC-074): N35 - N36 - N38 - N39 - N38 - N40 - N41
- P3 (TC TC-075): N35 - N36 - N38 - N39 - N38 - N39 - N38 - N40 - N41

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE42 (N35 --> N36) | TC-074 đến TC-080 |
| CE43 (N36 --> N37, Đúng) | TC-078 đến TC-080 |
| CE44 (N36 --> N38, Sai) | TC-074 đến TC-077 |
| CE45 (N38 --> N39, Đúng) | TC-074 đến TC-077 |
| CE46 (N39 --> N38) | TC-074 đến TC-077 |
| CE47 (N38 --> N40, Sai) | TC-074 đến TC-077 |
| CE48 (N40 --> N41) | TC-074 đến TC-077 |
| CE49 (N37 --> N41) | TC-078 đến TC-080 |
| N35 (lệnh/điểm quyết định) | TC-074 đến TC-080 |
| N36 (lệnh/điểm quyết định) | TC-074 đến TC-080 |
| N37 (lệnh/điểm quyết định) | TC-078 đến TC-080 |
| N38 (lệnh/điểm quyết định) | TC-074 đến TC-077 |
| N39 (lệnh/điểm quyết định) | TC-074 đến TC-077 |
| N40 (lệnh/điểm quyết định) | TC-074 đến TC-077 |
| N41 (lệnh/điểm quyết định) | TC-074 đến TC-080 |

Độ phủ đạt được: C0 = 7/7 = 100%; C1 = 8/8 = 100%.

Vòng lặp:

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Vòng trả từng Seat | 5 | 2 | 0: không áp dụng (không có Booking HELD không chỗ); 1, 2, 4, 5; 6: không áp dụng (BR-01) | TC-074 đến TC-077 |

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-releaseSeats.drawio (ID cell trùng N, CE).

#### F2.13.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

### F2.14 DC-Booking.issueTickets

Chữ ký: issueTickets(paymentReference: PaymentReference, idGenerator: ITicketingIdGenerator): List<Ticket>. Ưu tiên: Cao. Tiêu chí: BR-09, BR-10; sự kiện ST-01 (T3); vòng lặp; gọi phụ thuộc.

#### F2.14.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | issueTickets(paymentReference: PaymentReference, idGenerator: ITicketingIdGenerator): List<Ticket> | P12 F2 |
| Tiền điều kiện | status HELD | P12 F2 |
| Hậu điều kiện | status TICKETED; mỗi vé ISSUED với channel ONLINE; mọi Seat SOLD | P12 F2 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| BR | BR-09: thanh toán thành công thì phát hành vé; BR-10: mỗi chỗ đúng một vé có một mã vé; ASM-22 giá vé dùng ticketPrice đã chốt; ASM-41 ghi paymentReference | P06 BR-09, BR-10; P12 F7 |
| State machine | ST-01 T3: Held --issueTickets--> Ticketed; sự kiện bị từ chối ở Draft, Ticketed, Expired | P12 F6.2 |
| Thiết kế method | F3: kiểm status; với mỗi Seat theo thứ tự travelerInfos: Ticket.createTicket(idGenerator.nextTicketCode(), trip, seat, info, ticketPrice, ONLINE) và seat.markSold(); ghi paymentReference; xoá liên kết seats; status = TICKETED; trả danh sách vé | P12 F3 |
| Luồng | UC-002 bước 11 | P04 UC-002 |

#### F2.14.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-68 | status | HELD | Hợp lệ | HELD | P12 F2 tiền điều kiện |
| EC-69 | status | DRAFT | Không hợp lệ | DRAFT | P12 F2 tiền điều kiện |
| EC-70 | status | TICKETED | Không hợp lệ | TICKETED | P12 F2 tiền điều kiện |
| EC-71 | status | EXPIRED | Không hợp lệ | EXPIRED | P12 F2 tiền điều kiện |
| EC-72 | Số Seat đang giữ | 1 đến 5 | Hợp lệ | 2 | BR-01, BR-10 |
| EC-73 | Số chỗ | 0 hoặc >= 6 | Không thể xảy ra tại đây | - | 0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3) |
| EC-74 | paymentReference hoặc idGenerator | null | Không hợp lệ | null | ASM-111 |

#### F2.14.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-31 | của EC-72 | Số Seat = 1 | EC-72 | 1 vé |
| BV-32 | của EC-72 | Số Seat = 5 | EC-72 | 5 vé, 5 mã khác nhau |

#### F2.14.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định (status là HELD).

#### F2.14.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Held | issueTickets(paymentReference, idGenerator) | - | Tạo Ticket; Seat.markSold; ghi paymentReference | Ticketed | ST-01 T3 |
| Draft | issueTickets(...) | - | Ném InvalidStateException; không đổi | Draft | P12 F6.2 |
| Ticketed | issueTickets(...) | - | Ném InvalidStateException; không đổi | Ticketed | P12 F6.2 |
| Expired | issueTickets(...) | - | Ném InvalidStateException; không đổi | Expired | P12 F6.2 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.14.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N42 | Bắt đầu | bắt đầu |
| N43 | status khác HELD? | quyết định |
| N44 | ném InvalidStateException | khối lệnh |
| N45 | còn Seat chưa phát hành vé? | quyết định |
| N46 | ticket = Ticket.createTicket(idGenerator.nextTicketCode(), ..., ticketPrice, ONLINE); seat.markSold() | khối lệnh |
| N47 | ghi paymentReference; xoá liên kết seats; status = TICKETED; trả danh sách vé | khối lệnh |
| N48 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE50 | N42 | N43 | rỗng |
| CE51 | N43 | N44 | Đúng |
| CE52 | N43 | N45 | Sai |
| CE53 | N45 | N46 | Đúng |
| CE54 | N46 | N45 | rỗng |
| CE55 | N45 | N47 | Sai |
| CE56 | N47 | N48 | rỗng |
| CE57 | N44 | N48 | rỗng |

V(G) = E - N + 2 = 8 - 7 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 3 trên V(G) = 3):

- P1 (TC TC-087): N42 - N43 - N44 - N48
- P2 (TC TC-081): N42 - N43 - N45 - N46 - N45 - N47 - N48
- P3 (TC TC-082): N42 - N43 - N45 - N46 - N45 - N46 - N45 - N47 - N48

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE50 (N42 --> N43) | TC-081 đến TC-089 |
| CE51 (N43 --> N44, Đúng) | TC-087 đến TC-089 |
| CE52 (N43 --> N45, Sai) | TC-081 đến TC-086 |
| CE53 (N45 --> N46, Đúng) | TC-081 đến TC-086 |
| CE54 (N46 --> N45) | TC-081 đến TC-086 |
| CE55 (N45 --> N47, Sai) | TC-081 đến TC-086 |
| CE56 (N47 --> N48) | TC-081 đến TC-086 |
| CE57 (N44 --> N48) | TC-087 đến TC-089 |
| N42 (lệnh/điểm quyết định) | TC-081 đến TC-089 |
| N43 (lệnh/điểm quyết định) | TC-081 đến TC-089 |
| N44 (lệnh/điểm quyết định) | TC-087 đến TC-089 |
| N45 (lệnh/điểm quyết định) | TC-081 đến TC-086 |
| N46 (lệnh/điểm quyết định) | TC-081 đến TC-086 |
| N47 (lệnh/điểm quyết định) | TC-081 đến TC-086 |
| N48 (lệnh/điểm quyết định) | TC-081 đến TC-089 |

Độ phủ đạt được: C0 = 7/7 = 100%; C1 = 8/8 = 100%.

Vòng lặp:

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Vòng phát hành vé cho từng Seat | 5 | 2 | 0: không áp dụng (createBooking chặn danh sách rỗng); 1, 2, 4, 5; 6: không áp dụng (isWithinSeatLimit chặn trước, BR-01) | TC-081 đến TC-084 |

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-issueTickets.drawio (ID cell trùng N, CE).

#### F2.14.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |
| IF-15 ITicketingIdGenerator | stub + mock | nextTicketCode() lần lượt trả SV0000101, SV0000102, ...; mock xác minh số lần gọi | Mã vé duy nhất sinh từ kho dữ liệu (BR-10), không dùng nguồn thật |
| DC-PhoneNumber (PKG-28) | fake | isValid(String): 10 chữ số, bắt đầu bằng 0 (ASM-15) | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.15 DC-Booking.getBookingSummary

Chữ ký: getBookingSummary(): BookingSummary. Ưu tiên: Trung bình. Tiêu chí: kiểm tra trạng thái; chuyển đổi dữ liệu (UC-002 Dữ liệu ra 4).

#### F2.15.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | getBookingSummary(): BookingSummary | P12 F2 |
| Tiền / hậu điều kiện | Tiền: status TICKETED. Hậu: không đổi | P12 F2 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| Dữ liệu ra | Các vé đã phát hành và tổng tiền (Dữ liệu ra 4 #7) | P04 UC-002 Mục 5; P12 F7 DC-BookingSummary |

#### F2.15.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-75 | status | TICKETED | Hợp lệ | TICKETED | P12 F2 tiền điều kiện |
| EC-76 | status | DRAFT | Không hợp lệ | DRAFT | P12 F2 tiền điều kiện |
| EC-77 | status | HELD | Không hợp lệ | HELD | P12 F2 tiền điều kiện |
| EC-78 | status | EXPIRED | Không hợp lệ | EXPIRED | P12 F2 tiền điều kiện |
| EC-79 | Số vé đã phát hành | 1 đến 5 | Hợp lệ | 2 | BR-01 |
| EC-80 | Số chỗ | 0 hoặc >= 6 | Không thể xảy ra tại đây | - | 0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3) |

#### F2.15.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-33 | của EC-79 | 1 vé | EC-79 | tickets 1 phần tử, totalAmount 360.000 đ |
| BV-34 | của EC-79 | 5 vé | EC-79 | tickets 5 phần tử, totalAmount 1.800.000 đ |

#### F2.15.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.15.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.15.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.15.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |
| IF-15 ITicketingIdGenerator | stub + mock | nextTicketCode() lần lượt trả SV0000101, SV0000102, ...; mock xác minh số lần gọi | Mã vé duy nhất sinh từ kho dữ liệu (BR-10), không dùng nguồn thật |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.16 DC-Booking.getHoldExpiryTime

Chữ ký: getHoldExpiryTime(): LocalDateTime. Ưu tiên: Cao. Tiêu chí: BR-07; tính toán thời gian.

#### F2.16.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | getHoldExpiryTime(): LocalDateTime | P12 F2 |
| Tiền điều kiện | holdStartTime có giá trị | P12 F2 |
| Hậu điều kiện | Không đổi; = holdStartTime + HOLD_DURATION | P12 F2 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| BR | BR-07: giữ chỗ 10 phút kể từ khi bắt đầu giữ (HOLD_DURATION = 10 phút) | P06 BR-07; P12 F7 |

#### F2.16.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-81 | holdStartTime | Có giá trị, cộng 10 phút vẫn trong cùng ngày | Hợp lệ | 10:00 03/02/2027 | BR-07 |
| EC-82 | holdStartTime | Có giá trị, cộng 10 phút sang ngày kế tiếp (và sang tháng kế tiếp) | Hợp lệ | 23:55 28/02/2027 | BR-07 |
| EC-83 | holdStartTime | Rỗng (Booking DRAFT) | Không hợp lệ | null | P12 F2 tiền điều kiện |

#### F2.16.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-35 | của EC-82 | holdStartTime = 23:55 28/02/2027 (năm 2027 không nhuận) | EC-82 | 00:05 01/03/2027 |

#### F2.16.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.16.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.16.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.16.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

### F2.17 DC-Booking.isHoldExpired

Chữ ký: isHoldExpired(now: LocalDateTime): Boolean. Ưu tiên: Cao. Tiêu chí: BR-07; rẽ nhánh; thời gian.

#### F2.17.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isHoldExpired(now: LocalDateTime): Boolean | P12 F2 |
| Tiền điều kiện | holdStartTime có giá trị | P12 F2 |
| Hậu điều kiện | Không đổi; true khi now không trước thời điểm hết thời hạn giữ chỗ (holdStartTime + 10 phút) | P12 F2 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| BR | BR-07: giữ chờ thanh toán trong 10 phút kể từ khi bắt đầu giữ. Đúng 10 phút: xem ASM-112 | P06 BR-07 |
| Luồng | 10a: thanh toán lại chỉ khi còn thời hạn giữ chỗ; 9a: hết thời hạn | P04 UC-002 Mục 3 |

#### F2.17.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-84 | now so với holdStartTime + 10 phút | now trước thời điểm hết hạn | Hợp lệ (false) | holdStartTime + 5 phút | BR-07 |
| EC-85 | now so với holdStartTime + 10 phút | now bằng hoặc sau thời điểm hết hạn | Hợp lệ (true) | holdStartTime + 15 phút | BR-07, ASM-112 |
| EC-86 | holdStartTime | Rỗng (Booking DRAFT) | Không hợp lệ | null | P12 F2 tiền điều kiện |
| EC-87 | now | null | Không hợp lệ | null | ASM-111 |

#### F2.17.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-36 | của EC-84 | now = holdStartTime (đầu thời hạn) | EC-84 | false |
| BV-37 | của EC-84 | now = holdStartTime + 9 phút 59 giây | EC-84 | false |
| BV-38 | của EC-85 | now = holdStartTime + 10 phút | EC-85 | true (ASM-112) |
| BV-39 | của EC-85 | now = holdStartTime + 10 phút 1 giây | EC-85 | true |

#### F2.17.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.17.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.17.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn.

#### F2.17.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

### F2.18 DC-Booking.startPaymentAttempt

Chữ ký: startPaymentAttempt(): String. Ưu tiên: Trung bình. Tiêu chí: kiểm tra trạng thái; sinh khoá yêu cầu thanh toán.

#### F2.18.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | startPaymentAttempt(): String | P12 F2 |
| Tiền điều kiện | status HELD | P12 F2 |
| Hậu điều kiện | paymentAttemptCount tăng 1; trả khoá <bookingId>-<số lần> | P12 F2 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| Thiết kế method | F3: kiểm status; paymentAttemptCount tăng 1; trả bookingId + "-" + paymentAttemptCount | P12 F3 |
| Ghi chú | Tạm theo ASM-100 (UC-003 chưa phân tích) | P12 F2 |

#### F2.18.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-88 | status | HELD | Hợp lệ | HELD | P12 F2 tiền điều kiện |
| EC-89 | status | DRAFT | Không hợp lệ | DRAFT | P12 F2 tiền điều kiện |
| EC-90 | status | TICKETED | Không hợp lệ | TICKETED | P12 F2 tiền điều kiện |
| EC-91 | status | EXPIRED | Không hợp lệ | EXPIRED | P12 F2 tiền điều kiện |
| EC-92 | paymentAttemptCount trước khi gọi | 0 | Hợp lệ | 0 | P12 F7 giá trị mặc định 0 |
| EC-93 | paymentAttemptCount trước khi gọi | >= 1 | Hợp lệ | 1 | P12 F7 {>= 0} |

#### F2.18.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.18.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định (status là HELD).

#### F2.18.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.18.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N49 | Bắt đầu | bắt đầu |
| N50 | status khác HELD? | quyết định |
| N51 | ném InvalidStateException | khối lệnh |
| N52 | paymentAttemptCount tăng 1; trả bookingId + "-" + paymentAttemptCount | khối lệnh |
| N53 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE58 | N49 | N50 | rỗng |
| CE59 | N50 | N51 | Đúng |
| CE60 | N50 | N52 | Sai |
| CE61 | N52 | N53 | rỗng |
| CE62 | N51 | N53 | rỗng |

V(G) = E - N + 2 = 5 - 5 + 2 = 2; kiểm tra bằng số điểm quyết định nhị phân + 1 = 1 + 1 = 2; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 2 trên V(G) = 2):

- P1 (TC TC-106): N49 - N50 - N52 - N53
- P2 (TC TC-108): N49 - N50 - N51 - N53

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE58 (N49 --> N50) | TC-106 đến TC-110 |
| CE59 (N50 --> N51, Đúng) | TC-108 đến TC-110 |
| CE60 (N50 --> N52, Sai) | TC-106, TC-107 |
| CE61 (N52 --> N53) | TC-106, TC-107 |
| CE62 (N51 --> N53) | TC-108 đến TC-110 |
| N49 (lệnh/điểm quyết định) | TC-106 đến TC-110 |
| N50 (lệnh/điểm quyết định) | TC-106 đến TC-110 |
| N51 (lệnh/điểm quyết định) | TC-108 đến TC-110 |
| N52 (lệnh/điểm quyết định) | TC-106, TC-107 |
| N53 (lệnh/điểm quyết định) | TC-106 đến TC-110 |

Độ phủ đạt được: C0 = 5/5 = 100%; C1 = 5/5 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-startPaymentAttempt.drawio (ID cell trùng N, CE).

#### F2.18.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | findSeats(codes) trả các Seat thật theo đúng thứ tự codes; determineTicketPrice() trả 360.000 đ (ví dụ P04 UC-002) | Cô lập Booking khỏi tính giá và quản lý tập chỗ của Trip |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

### F2.19 DC-Ticket.createTicket

Chữ ký: createTicket(ticketCode: TicketCode, trip: Trip, seat: Seat, travelerInfo: TravelerInfo, price: Money, purchaseChannel: PurchaseChannel): Ticket. Ưu tiên: Trung bình. Tiêu chí: BR-09, BR-10; kiểm tra hợp lệ; sự kiện ST-02 (T1).

#### F2.19.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | createTicket(ticketCode, trip, seat, travelerInfo, price, purchaseChannel): Ticket (classifier) | P12 F2 |
| Tiền điều kiện | travelerInfo hợp lệ, price > 0 | P12 F2 |
| Hậu điều kiện | status ISSUED, checkedTime rỗng; số điện thoại thô chuyển thành PhoneNumber | P12 F2 |
| Ngoại lệ | IllegalArgumentException | P12 F2 |
| Thuộc tính | travelerName {không rỗng}; travelerPhone {10 chữ số, bắt đầu bằng 0 (ASM-15)}; price {> 0} | P12 F7 |
| State machine | ST-02 T1: (initial) --createTicket--> Issued | P12 F6.2 |

#### F2.19.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-94 | price | price > 0 | Hợp lệ | 360.000 đ | P12 F2 tiền điều kiện; F7 |
| EC-95 | price | price <= 0 | Không hợp lệ | 0 đ | P12 F2 tiền điều kiện; F7 |
| EC-96 | travelerInfo.travelerName | Có ký tự không phải khoảng trắng | Hợp lệ | Nguyễn Văn An | P12 F7 |
| EC-97 | travelerInfo.travelerName | Chuỗi rỗng | Không hợp lệ | "" | P12 F7 {không rỗng} |
| EC-98 | travelerInfo.travelerName | Chỉ gồm khoảng trắng | Chưa xác định (Q-112) | "   " | P12 F7; Q-112 |
| EC-99 | travelerInfo.travelerPhone | 10 chữ số, bắt đầu bằng 0 | Hợp lệ | 0912345678 | ASM-15 |
| EC-100 | travelerInfo.travelerPhone | Chuỗi rỗng | Không hợp lệ | "" | ASM-15; P12 F7 |
| EC-101 | travelerInfo.travelerPhone | Sai định dạng (không phải 10 chữ số bắt đầu bằng 0) | Không hợp lệ | 091234567 | ASM-15; P12 F7 |
| EC-102 | purchaseChannel | ONLINE | Hợp lệ | ONLINE | P12 F7a |
| EC-103 | purchaseChannel | COUNTER | Hợp lệ | COUNTER | P12 F7a |
| EC-104 | ticketCode, trip, seat, travelerInfo, price hoặc purchaseChannel | null | Không hợp lệ | null | ASM-111 |

#### F2.19.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-40 | của EC-95 | price = 0 đ | EC-95 | Ném IllegalArgumentException |
| BV-41 | của EC-94 | price = 1 đ | EC-94 | Vé ISSUED, price 1 đ |

#### F2.19.4 Bảng quyết định

Không áp dụng: Mỗi điều kiện hợp lệ độc lập, mọi vi phạm cùng ném IllegalArgumentException (không có tổ hợp cho kết quả khác nhau).

#### F2.19.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| (initial) | createTicket(...) | - | status = ISSUED, checkedTime rỗng | Issued | ST-02 T1 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.19.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method cho createTicket.

#### F2.19.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Trip | stub | getRouteAndDepartureTime() trả TripSchedule("Hà Nội - Lào Cai", 21:00 03/02/2027) | Lấy lịch chuyến cố định, không phụ thuộc Trip thật |
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |
| DC-PhoneNumber (PKG-28) | fake | isValid(String): 10 chữ số, bắt đầu bằng 0 (ASM-15) | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.20 DC-Ticket.isCancelled

Chữ ký: isCancelled(): Boolean. Ưu tiên: Thấp. Tiêu chí: kiểm tra điều kiện (UC-008 luồng 2b).

#### F2.20.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isCancelled(): Boolean | P12 F2 |
| Hậu điều kiện | Không đổi; true khi status CANCELLED (ASM-20) | P12 F2 |
| Luồng | 2b: vé khớp và đã bị huỷ --> từ chối trả vé | P04 UC-008 Mục 3 |
| Trạng thái | Issued, Checked (status ISSUED), Cancelled | P12 F6.1 |

#### F2.20.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-105 | Trạng thái vé | Issued (ISSUED, chưa soát) | Hợp lệ (false) | ISSUED | P12 F6.1 |
| EC-106 | Trạng thái vé | Checked (ISSUED, đã soát) | Hợp lệ (false) | ISSUED, checkedTime có giá trị | P12 F6.1 |
| EC-107 | Trạng thái vé | Cancelled | Hợp lệ (true) | CANCELLED | ASM-20, UC-008 2b |

#### F2.20.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.20.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định kết quả.

#### F2.20.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.20.6 Hộp trắng

Không có CFG: P12 F3 không có thiết kế method; V(G) = 1 theo mô tả (so sánh status với CANCELLED).

#### F2.20.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

### F2.21 DC-Ticket.cancelTicket

Chữ ký: cancelTicket(refundRatePercent: Integer, refundAmount: Money, refundMethod: RefundMethod): Refund. Ưu tiên: Cao. Tiêu chí: BR-15, BR-16; sự kiện ST-02 (T3, T5); rẽ nhánh; gọi phụ thuộc.

#### F2.21.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | cancelTicket(refundRatePercent: Integer, refundAmount: Money, refundMethod: RefundMethod): Refund | P12 F2 |
| Tiền điều kiện | status ISSUED (gồm đã soát) | P12 F2; F3 bước 1 |
| Hậu điều kiện | status CANCELLED, Seat AVAILABLE, có một Refund; outcome REFUNDED khi VIA_GATEWAY, AWAITING_CASH_PAYOUT khi tiền mặt | P12 F2; ASM-46, ASM-54 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| BR | BR-15: vé online hoàn qua cổng; BR-16: vé quầy hoàn tiền mặt; ASM-20 vé đã trả là đã huỷ và chỗ trở lại còn trống | P06 BR-15, BR-16; P04 UC-008 |
| Điều kiện hợp lệ | Refund: refundAmount >= 0, 0 <= refundRatePercent <= 100 | P12 F2 DC-Refund.createRefund; F7 |
| State machine | ST-02 T3: Issued --> Cancelled; T5: Checked --> Cancelled (ASM-104); Cancelled bị từ chối | P12 F6.2 |
| Thiết kế method | F3: kiểm status; status = CANCELLED; seat.release(); outcome theo method; refund = Refund.createRefund(...); trả refund | P12 F3 |
| Luồng | UC-008 bước 10 (huỷ vé, trả chỗ, ghi nhận khoản hoàn) | P04 UC-008 |

#### F2.21.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-108 | status | ISSUED, chưa soát | Hợp lệ | ISSUED | P12 F2 |
| EC-109 | status | ISSUED, đã soát (Checked) | Hợp lệ | ISSUED, checkedTime có giá trị | ASM-104 |
| EC-110 | status | CANCELLED | Không hợp lệ | CANCELLED | P12 F2 tiền điều kiện |
| EC-111 | refundMethod | VIA_GATEWAY | Hợp lệ | VIA_GATEWAY | BR-15 |
| EC-112 | refundMethod | CASH_AT_COUNTER | Hợp lệ | CASH_AT_COUNTER | BR-16 |
| EC-113 | refundRatePercent | 0 đến 100 | Hợp lệ | 90 | P12 F7 DC-Refund |
| EC-114 | refundRatePercent | < 0 | Không hợp lệ (kết quả chưa xác định, Q-111) | -1 | P12 F2 DC-Refund.createRefund; Q-111 |
| EC-115 | refundRatePercent | > 100 | Không hợp lệ (kết quả chưa xác định, Q-111) | 101 | P12 F2 DC-Refund.createRefund; Q-111 |
| EC-116 | refundAmount | >= 0 | Hợp lệ | 324.000 đ | P12 F7 DC-Refund |
| EC-117 | refundAmount | < 0 | Không hợp lệ (kết quả chưa xác định, Q-111) | -1 đ | P12 F2 DC-Refund.createRefund; Q-111 |
| EC-118 | refundAmount hoặc refundMethod | null | Không hợp lệ | null | ASM-111 |

#### F2.21.3 Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-42 | của EC-113 | refundRatePercent = 0 | EC-113 | Refund(refundRatePercent 0) |
| BV-43 | của EC-113 | refundRatePercent = 100 | EC-113 | Refund(refundRatePercent 100) |
| BV-44 | của EC-114 | refundRatePercent = -1 | EC-114 | IllegalArgumentException; trạng thái vé chưa xác định (Q-111) |
| BV-45 | của EC-115 | refundRatePercent = 101 | EC-115 | IllegalArgumentException; trạng thái vé chưa xác định (Q-111) |
| BV-46 | của EC-116 | refundAmount = 0 đ | EC-116 | Refund(refundAmount 0 đ) |
| BV-47 | của EC-117 | refundAmount = -1 đ | EC-117 | IllegalArgumentException; trạng thái vé chưa xác định (Q-111) |

#### F2.21.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT5-Q1 | DT5-Q2 | DT5-Q3 |
| C1: status là ISSUED (chưa soát hoặc đã soát) | Y | Y | N |
| C2: refundMethod là VIA_GATEWAY | Y | N | - |
| A1: status CANCELLED, Seat AVAILABLE, Refund outcome REFUNDED | X | - | - |
| A2: status CANCELLED, Seat AVAILABLE, Refund outcome AWAITING_CASH_PAYOUT | - | X | - |
| A3: Ném InvalidStateException, vé và Seat không đổi | - | - | X |
```

Q3 gộp (N, Y) và (N, N) bằng "-" vì P12 F3 bước 1 kiểm status trước khi dùng refundMethod.

#### F2.21.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Issued | cancelTicket(rate, amount, method) | - | Seat.release; tạo Refund | Cancelled | ST-02 T3 |
| Checked | cancelTicket(rate, amount, method) | - | Seat.release; tạo Refund | Cancelled | ST-02 T5; ASM-104 |
| Cancelled | cancelTicket(rate, amount, method) | - | Ném InvalidStateException; không đổi | Cancelled | P12 F6.2 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.21.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N54 | Bắt đầu | bắt đầu |
| N55 | status khác ISSUED? | quyết định |
| N56 | ném InvalidStateException | khối lệnh |
| N57 | status = CANCELLED; seat.release() | khối lệnh |
| N58 | refundMethod là VIA_GATEWAY? | quyết định |
| N59 | outcome = REFUNDED | khối lệnh |
| N60 | outcome = AWAITING_CASH_PAYOUT | khối lệnh |
| N61 | refund = Refund.createRefund(refundAmount, rate, method, outcome); trả refund | khối lệnh |
| N62 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE63 | N54 | N55 | rỗng |
| CE64 | N55 | N56 | Đúng |
| CE65 | N55 | N57 | Sai |
| CE66 | N57 | N58 | rỗng |
| CE67 | N58 | N59 | Đúng |
| CE68 | N58 | N60 | Sai |
| CE69 | N59 | N61 | rỗng |
| CE70 | N60 | N61 | rỗng |
| CE71 | N61 | N62 | rỗng |
| CE72 | N56 | N62 | rỗng |

V(G) = E - N + 2 = 10 - 9 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 3 trên V(G) = 3):

- P1 (TC TC-127): N54 - N55 - N56 - N62
- P2 (TC TC-122): N54 - N55 - N57 - N58 - N59 - N61 - N62
- P3 (TC TC-123): N54 - N55 - N57 - N58 - N60 - N61 - N62

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE63 (N54 --> N55) | TC-122 đến TC-127 |
| CE64 (N55 --> N56, Đúng) | TC-127 |
| CE65 (N55 --> N57, Sai) | TC-122 đến TC-126 |
| CE66 (N57 --> N58) | TC-122 đến TC-126 |
| CE67 (N58 --> N59, Đúng) | TC-122, TC-124, TC-125 |
| CE68 (N58 --> N60, Sai) | TC-123, TC-126 |
| CE69 (N59 --> N61) | TC-122, TC-124, TC-125 |
| CE70 (N60 --> N61) | TC-123, TC-126 |
| CE71 (N61 --> N62) | TC-122 đến TC-126 |
| CE72 (N56 --> N62) | TC-127 |
| N54 (lệnh/điểm quyết định) | TC-122 đến TC-127 |
| N55 (lệnh/điểm quyết định) | TC-122 đến TC-127 |
| N56 (lệnh/điểm quyết định) | TC-127 |
| N57 (lệnh/điểm quyết định) | TC-122 đến TC-126 |
| N58 (lệnh/điểm quyết định) | TC-122 đến TC-126 |
| N59 (lệnh/điểm quyết định) | TC-122, TC-124, TC-125 |
| N60 (lệnh/điểm quyết định) | TC-123, TC-126 |
| N61 (lệnh/điểm quyết định) | TC-122 đến TC-126 |
| N62 (lệnh/điểm quyết định) | TC-122 đến TC-127 |

Độ phủ đạt được: C0 = 9/9 = 100%; C1 = 10/10 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-Ticket-cancelTicket.drawio (ID cell trùng N, CE).

#### F2.21.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |
| DC-Trip | stub | getRouteAndDepartureTime() trả TripSchedule("Hà Nội - Lào Cai", 21:00 03/02/2027) | Lấy lịch chuyến cố định, không phụ thuộc Trip thật |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.22 DC-Ticket.cancelWithTrip

Chữ ký: cancelWithTrip(): void. Ưu tiên: Cao. Tiêu chí: BR-17, BR-19; sự kiện ST-02 (T4, T6).

#### F2.22.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | cancelWithTrip(): void | P12 F2 |
| Tiền / hậu điều kiện | Tiền: status ISSUED. Hậu: status CANCELLED; không đụng Seat (ASM-26, Q-44) | P12 F2 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| BR | BR-19: khi chuyến bị huỷ mọi vé còn hiệu lực được huỷ và hoàn tiền | P06 BR-19 |
| State machine | ST-02 T4: Issued --> Cancelled; T6: Checked --> Cancelled (ASM-104); Cancelled bị từ chối | P12 F6.2 |
| Thiết kế method | F3: kiểm status; status = CANCELLED; không đụng Seat | P12 F3 |
| Luồng | UC-013 bước 5 | P04 UC-013 |

#### F2.22.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-119 | status | ISSUED, chưa soát | Hợp lệ | ISSUED | P12 F2 |
| EC-120 | status | ISSUED, đã soát (Checked) | Hợp lệ | ISSUED, checkedTime có giá trị | ASM-104 |
| EC-121 | status | CANCELLED | Không hợp lệ | CANCELLED | P12 F2 tiền điều kiện |

#### F2.22.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.22.4 Bảng quyết định

Không áp dụng: Chỉ có một điều kiện quyết định (status là ISSUED).

#### F2.22.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Issued | cancelWithTrip() | - | status = CANCELLED, Seat không đổi | Cancelled | ST-02 T4 |
| Checked | cancelWithTrip() | - | status = CANCELLED, Seat không đổi | Cancelled | ST-02 T6; ASM-104 |
| Cancelled | cancelWithTrip() | - | Ném InvalidStateException; không đổi | Cancelled | P12 F6.2 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.22.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N63 | Bắt đầu | bắt đầu |
| N64 | status khác ISSUED? | quyết định |
| N65 | ném InvalidStateException | khối lệnh |
| N66 | status = CANCELLED (không đụng Seat) | khối lệnh |
| N67 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE73 | N63 | N64 | rỗng |
| CE74 | N64 | N65 | Đúng |
| CE75 | N64 | N66 | Sai |
| CE76 | N66 | N67 | rỗng |
| CE77 | N65 | N67 | rỗng |

V(G) = E - N + 2 = 5 - 5 + 2 = 2; kiểm tra bằng số điểm quyết định nhị phân + 1 = 1 + 1 = 2; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 2 trên V(G) = 2):

- P1 (TC TC-131): N63 - N64 - N66 - N67
- P2 (TC TC-133): N63 - N64 - N65 - N67

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE73 (N63 --> N64) | TC-131 đến TC-133 |
| CE74 (N64 --> N65, Đúng) | TC-133 |
| CE75 (N64 --> N66, Sai) | TC-131, TC-132 |
| CE76 (N66 --> N67) | TC-131, TC-132 |
| CE77 (N65 --> N67) | TC-133 |
| N63 (lệnh/điểm quyết định) | TC-131 đến TC-133 |
| N64 (lệnh/điểm quyết định) | TC-131 đến TC-133 |
| N65 (lệnh/điểm quyết định) | TC-133 |
| N66 (lệnh/điểm quyết định) | TC-131, TC-132 |
| N67 (lệnh/điểm quyết định) | TC-131 đến TC-133 |

Độ phủ đạt được: C0 = 5/5 = 100%; C1 = 5/5 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-Ticket-cancelWithTrip.drawio (ID cell trùng N, CE).

#### F2.22.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

### F2.23 DC-Ticket.recordRefund

Chữ ký: recordRefund(refundRatePercent: Integer, refundAmount: Money, refundMethod: RefundMethod, refundOutcome: RefundOutcome): Refund. Ưu tiên: Cao. Tiêu chí: BR-15, BR-16, BR-17; kiểm tra điều kiện trạng thái; rẽ nhánh.

#### F2.23.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | recordRefund(refundRatePercent, refundAmount, refundMethod, refundOutcome): Refund | P12 F2 |
| Tiền / hậu điều kiện | Tiền: status CANCELLED, chưa có Refund. Hậu: có một Refund | P12 F2 |
| Ngoại lệ | InvalidStateException (status khác CANCELLED hoặc đã có Refund) | P12 F2, F3 |
| BR | BR-17: hoàn 100% giá vé khi huỷ chuyến; BR-15, BR-16 hình thức hoàn theo kênh mua | P06 BR-15, BR-16, BR-17 |
| Luồng | UC-013 bước 9; luồng 8a: hoàn tiền không thành công --> ghi nhận khoản hoàn chưa thành công (ASM-31) | P04 UC-013 |
| Giá trị refundOutcome | REFUNDED, FAILED, AWAITING_CASH_PAYOUT | P12 F7a |
| Thiết kế method | F3: nếu status khác CANCELLED hoặc refund đã có thì ném InvalidStateException; refund = Refund.createRefund(...); trả refund | P12 F3 |

#### F2.23.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-122 | status | CANCELLED | Hợp lệ | CANCELLED | P12 F2 tiền điều kiện |
| EC-123 | status | ISSUED, chưa soát | Không hợp lệ | ISSUED | P12 F2 tiền điều kiện |
| EC-124 | status | ISSUED, đã soát (Checked) | Không hợp lệ | ISSUED, checkedTime có giá trị | P12 F2 tiền điều kiện |
| EC-125 | Refund hiện có của vé | Chưa có Refund | Hợp lệ | vé huỷ bởi cancelWithTrip | P12 F2 tiền điều kiện |
| EC-126 | Refund hiện có của vé | Đã có Refund | Không hợp lệ | vé đã recordRefund một lần | P12 F2 tiền điều kiện |
| EC-127 | refundOutcome | REFUNDED | Hợp lệ | REFUNDED | UC-013 hậu điều kiện (vé online) |
| EC-128 | refundOutcome | FAILED | Hợp lệ | FAILED | UC-013 8a, ASM-31 |
| EC-129 | refundOutcome | AWAITING_CASH_PAYOUT | Hợp lệ | AWAITING_CASH_PAYOUT | UC-013 hậu điều kiện (vé quầy), ASM-28 |
| EC-130 | Tổ hợp (refundMethod, refundOutcome) ngoài ba tổ hợp của UC-013 | Ví dụ (VIA_GATEWAY, AWAITING_CASH_PAYOUT) | Chưa xác định (Q-113) | VIA_GATEWAY, AWAITING_CASH_PAYOUT | Q-113 |
| EC-131 | refundRatePercent | > 100 | Không hợp lệ (kết quả chưa xác định, Q-111) | 101 | P12 F2 DC-Refund.createRefund; Q-111 |
| EC-132 | refundAmount, refundMethod hoặc refundOutcome | null | Không hợp lệ | null | ASM-111 |

#### F2.23.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.23.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT6-Q1 | DT6-Q2 | DT6-Q3 | DT6-Q4 |
| C1: status là CANCELLED | Y | Y | N | N |
| C2: Vé chưa có Refund | Y | N | Y | N |
| A1: Tạo và trả Refund với đúng giá trị truyền vào | X | - | - | N/A |
| A2: Ném InvalidStateException, không tạo Refund | - | X | X | N/A |
```

Q4 là N/A: Refund chỉ được tạo cho vé đã CANCELLED và vé không quay lại ISSUED (P12 F6.2).

#### F2.23.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.23.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N68 | Bắt đầu | bắt đầu |
| N69 | status khác CANCELLED? | quyết định |
| N70 | ném InvalidStateException | khối lệnh |
| N71 | vé đã có Refund? | quyết định |
| N72 | refund = Refund.createRefund(amount, rate, method, outcome); trả refund | khối lệnh |
| N73 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE78 | N68 | N69 | rỗng |
| CE79 | N69 | N70 | Đúng |
| CE80 | N69 | N71 | Sai |
| CE81 | N71 | N70 | Đúng |
| CE82 | N71 | N72 | Sai |
| CE83 | N72 | N73 | rỗng |
| CE84 | N70 | N73 | rỗng |

V(G) = E - N + 2 = 7 - 6 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Điều kiện ghép (nếu có) được tách thành các điểm quyết định riêng trong CFG để mỗi điều kiện con nhận cả đúng và sai.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 3 trên V(G) = 3):

- P1 (TC TC-139): N68 - N69 - N70 - N73
- P2 (TC TC-134): N68 - N69 - N71 - N72 - N73
- P3 (TC TC-137): N68 - N69 - N71 - N70 - N73

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE78 (N68 --> N69) | TC-134 đến TC-140 |
| CE79 (N69 --> N70, Đúng) | TC-139, TC-140 |
| CE80 (N69 --> N71, Sai) | TC-134 đến TC-138 |
| CE81 (N71 --> N70, Đúng) | TC-137, TC-138 |
| CE82 (N71 --> N72, Sai) | TC-134 đến TC-136 |
| CE83 (N72 --> N73) | TC-134 đến TC-136 |
| CE84 (N70 --> N73) | TC-137 đến TC-140 |
| N68 (lệnh/điểm quyết định) | TC-134 đến TC-140 |
| N69 (lệnh/điểm quyết định) | TC-134 đến TC-140 |
| N70 (lệnh/điểm quyết định) | TC-137 đến TC-140 |
| N71 (lệnh/điểm quyết định) | TC-134 đến TC-138 |
| N72 (lệnh/điểm quyết định) | TC-134 đến TC-136 |
| N73 (lệnh/điểm quyết định) | TC-134 đến TC-140 |

Độ phủ đạt được: C0 = 6/6 = 100%; C1 = 7/7 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-Ticket-recordRefund.drawio (ID cell trùng N, CE).

#### F2.23.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |
| DC-Money (PKG-28) | fake | Bản Money tối giản trong bộ nhớ, percent(Integer) làm tròn đến đồng HALF_UP, times(Integer), so sánh bằng theo giá trị | PKG-28 chưa được thiết kế; hợp đồng lấy từ P12 mục Giao ước với package khác |

### F2.24 DC-Ticket.determineCheckResult

Chữ ký: determineCheckResult(): TicketCheckResult. Ưu tiên: Cao. Tiêu chí: BR-21, BR-22; rẽ nhánh; kiểm tra hợp lệ.

#### F2.24.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | determineCheckResult(): TicketCheckResult | P12 F2 |
| Hậu điều kiện | Không đổi | P12 F2 |
| Ngoại lệ | Không có | P12 F2 |
| BR | BR-21: vé đã huỷ là không hợp lệ (đã huỷ); BR-22: vé đã soát trước đó là không hợp lệ (đã soát); BR-20 (sai chuyến) do lớp điều phối soát vé xử lý, không thuộc Ticket | P06 BR-20, BR-21, BR-22; P12 F3 |
| Luồng thay thế | 5b: vé trong danh sách và đã huỷ; 5c: vé chưa huỷ và đã soát (kèm thời điểm soát trước) | P04 UC-015 Mục 3 |
| Kết quả | CANCELLED_TICKET, ALREADY_CHECKED (previousCheckedTime), VALID (travelerName); kèm ticketCode, seatCode | P12 F3, F7 DC-TicketCheckResult |
| Thiết kế method | F3: nếu CANCELLED thì CANCELLED_TICKET; nếu checkedTime khác rỗng thì ALREADY_CHECKED; còn lại VALID | P12 F3 |

#### F2.24.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-133 | Trạng thái vé | ISSUED, chưa soát | Hợp lệ (VALID) | ISSUED, checkedTime rỗng | UC-015 bước 5 |
| EC-134 | Trạng thái vé | ISSUED, đã soát | Không hợp lệ (ALREADY_CHECKED) | checkedTime = 20:15 03/02/2027 | BR-22, UC-015 5c |
| EC-135 | Trạng thái vé | CANCELLED, chưa soát | Không hợp lệ (CANCELLED_TICKET) | CANCELLED | BR-21, UC-015 5b |
| EC-136 | Trạng thái vé | CANCELLED, đã soát | Không hợp lệ (CANCELLED_TICKET) | CANCELLED, checkedTime = 20:15 03/02/2027 | BR-21; UC-015 5c chỉ áp dụng cho vé chưa huỷ |

#### F2.24.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.24.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT7-Q1 | DT7-Q2 | DT7-Q3 |
| C1: status là CANCELLED | Y | N | N |
| C2: checkedTime khác rỗng | - | Y | N |
| A1: CANCELLED_TICKET (kèm ticketCode, seatCode) | X | - | - |
| A2: ALREADY_CHECKED (kèm ticketCode, seatCode, previousCheckedTime) | - | X | - |
| A3: VALID (kèm ticketCode, seatCode, travelerName) | - | - | X |
```

Q1 gộp (Y, Y) và (Y, N) bằng "-" vì UC-015 luồng 5c giới hạn "chưa bị huỷ và đã được soát", nên vé đã huỷ luôn báo đã huỷ. Hai tổ hợp bị gộp vẫn có TC riêng.

#### F2.24.5 Chuyển trạng thái

Không áp dụng: Phương thức không phải sự kiện của state machine.

#### F2.24.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N74 | Bắt đầu | bắt đầu |
| N75 | status là CANCELLED? | quyết định |
| N76 | trả CANCELLED_TICKET(ticketCode, seatCode) | khối lệnh |
| N77 | checkedTime khác rỗng? | quyết định |
| N78 | trả ALREADY_CHECKED(ticketCode, seatCode, previousCheckedTime = checkedTime) | khối lệnh |
| N79 | trả VALID(ticketCode, seatCode, travelerName) | khối lệnh |
| N80 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE85 | N74 | N75 | rỗng |
| CE86 | N75 | N76 | Đúng |
| CE87 | N75 | N77 | Sai |
| CE88 | N77 | N78 | Đúng |
| CE89 | N77 | N79 | Sai |
| CE90 | N76 | N80 | rỗng |
| CE91 | N78 | N80 | rỗng |
| CE92 | N79 | N80 | rỗng |

V(G) = E - N + 2 = 8 - 7 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Thiết kế method không có điều kiện ghép.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 3 trên V(G) = 3):

- P1 (TC TC-145): N74 - N75 - N76 - N80
- P2 (TC TC-143): N74 - N75 - N77 - N79 - N80
- P3 (TC TC-144): N74 - N75 - N77 - N78 - N80

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE85 (N74 --> N75) | TC-143 đến TC-146 |
| CE86 (N75 --> N76, Đúng) | TC-145, TC-146 |
| CE87 (N75 --> N77, Sai) | TC-143, TC-144 |
| CE88 (N77 --> N78, Đúng) | TC-144 |
| CE89 (N77 --> N79, Sai) | TC-143 |
| CE90 (N76 --> N80) | TC-145, TC-146 |
| CE91 (N78 --> N80) | TC-144 |
| CE92 (N79 --> N80) | TC-143 |
| N74 (lệnh/điểm quyết định) | TC-143 đến TC-146 |
| N75 (lệnh/điểm quyết định) | TC-143 đến TC-146 |
| N76 (lệnh/điểm quyết định) | TC-145, TC-146 |
| N77 (lệnh/điểm quyết định) | TC-143, TC-144 |
| N78 (lệnh/điểm quyết định) | TC-144 |
| N79 (lệnh/điểm quyết định) | TC-143 |
| N80 (lệnh/điểm quyết định) | TC-143 đến TC-146 |

Độ phủ đạt được: C0 = 7/7 = 100%; C1 = 8/8 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-Ticket-determineCheckResult.drawio (ID cell trùng N, CE).

#### F2.24.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |
| DC-Trip | stub | getRouteAndDepartureTime() trả TripSchedule("Hà Nội - Lào Cai", 21:00 03/02/2027) | Lấy lịch chuyến cố định, không phụ thuộc Trip thật |

### F2.25 DC-Ticket.markChecked

Chữ ký: markChecked(checkTime: LocalDateTime): void. Ưu tiên: Cao. Tiêu chí: BR-22; sự kiện ST-02 (T2); rẽ nhánh.

#### F2.25.1 Cơ sở kiểm thử

| Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | markChecked(checkTime: LocalDateTime): void | P12 F2 |
| Tiền / hậu điều kiện | Tiền: status ISSUED, checkedTime rỗng. Hậu: checkedTime = checkTime | P12 F2 |
| Ngoại lệ | InvalidStateException | P12 F2 |
| BR | BR-22: vé đã soát trước đó là không hợp lệ | P06 BR-22 |
| State machine | ST-02 T2: Issued --markChecked--> Checked; Checked, Cancelled bị từ chối (InvalidStateException) | P12 F6.2 |
| Thiết kế method | F3: nếu status khác ISSUED hoặc checkedTime khác rỗng thì ném InvalidStateException; checkedTime = checkTime | P12 F3 |
| Luồng | UC-015 bước 6 | P04 UC-015 |

#### F2.25.2 Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-137 | Trạng thái vé | ISSUED, chưa soát | Hợp lệ | ISSUED, checkedTime rỗng | P12 F2 tiền điều kiện |
| EC-138 | Trạng thái vé | ISSUED, đã soát | Không hợp lệ | checkedTime = 20:15 03/02/2027 | BR-22; P12 F6.2 |
| EC-139 | Trạng thái vé | CANCELLED, chưa soát | Không hợp lệ | CANCELLED | P12 F6.2 |
| EC-140 | Trạng thái vé | CANCELLED, đã soát | Không hợp lệ | CANCELLED, checkedTime = 20:15 03/02/2027 | P12 F6.2 |
| EC-141 | checkTime | null | Không hợp lệ | null | ASM-111 |

#### F2.25.3 Giá trị biên

Không áp dụng: miền đầu vào là tập giá trị rời rạc (enumeration, trạng thái), không có lớp có thứ tự.

#### F2.25.4 Bảng quyết định

```text
| Điều kiện / Hành động | DT8-Q1 | DT8-Q2 | DT8-Q3 | DT8-Q4 |
| C1: status là ISSUED | Y | Y | N | N |
| C2: checkedTime rỗng | Y | N | Y | N |
| A1: checkedTime = checkTime | X | - | - | - |
| A2: Ném InvalidStateException, vé không đổi | - | X | X | X |
```

Hành động của ba quy tắc bị từ chối giống nhau và F3 dùng điều kiện "hoặc", nên thứ tự kiểm không ảnh hưởng; vẫn giữ riêng từng quy tắc.

#### F2.25.5 Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Issued | markChecked(checkTime) | - | checkedTime = checkTime | Checked | ST-02 T2 |
| Checked | markChecked(checkTime) | - | Ném InvalidStateException; checkedTime không đổi | Checked | P12 F6.2 |
| Cancelled | markChecked(checkTime) | - | Ném InvalidStateException; không đổi | Cancelled | P12 F6.2 |

Cặp (trạng thái, sự kiện) không có chuyển của phương thức này được liệt kê ở các dòng "Ném InvalidStateException" hoặc "Bỏ qua" của bảng trên, mỗi dòng có TC (xem F3, F4).

#### F2.25.6 Hộp trắng

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
|---|---|---|
| N81 | Bắt đầu | bắt đầu |
| N82 | status khác ISSUED? | quyết định |
| N83 | ném InvalidStateException | khối lệnh |
| N84 | checkedTime khác rỗng? | quyết định |
| N85 | checkedTime = checkTime | khối lệnh |
| N86 | Kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
|---|---|---|---|
| CE93 | N81 | N82 | rỗng |
| CE94 | N82 | N83 | Đúng |
| CE95 | N82 | N84 | Sai |
| CE96 | N84 | N83 | Đúng |
| CE97 | N84 | N85 | Sai |
| CE98 | N85 | N86 | rỗng |
| CE99 | N83 | N86 | rỗng |

V(G) = E - N + 2 = 7 - 6 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3; V(G) không lớn hơn 10, không cần đề xuất tách phương thức.

Điều kiện ghép (nếu có) được tách thành các điểm quyết định riêng trong CFG để mỗi điều kiện con nhận cả đúng và sai.

Đường đi cơ sở (tập đường đi độc lập tuyến tính tìm được trong số các đường của bộ TC; 3 trên V(G) = 3):

- P1 (TC TC-149): N81 - N82 - N83 - N86
- P2 (TC TC-147): N81 - N82 - N84 - N85 - N86
- P3 (TC TC-148): N81 - N82 - N84 - N83 - N86

Bảng phủ:

| Nhánh (CE) hoặc lệnh (N) | TC phủ |
|---|---|
| CE93 (N81 --> N82) | TC-147 đến TC-150 |
| CE94 (N82 --> N83, Đúng) | TC-149, TC-150 |
| CE95 (N82 --> N84, Sai) | TC-147, TC-148 |
| CE96 (N84 --> N83, Đúng) | TC-148 |
| CE97 (N84 --> N85, Sai) | TC-147 |
| CE98 (N85 --> N86) | TC-147 |
| CE99 (N83 --> N86) | TC-148 đến TC-150 |
| N81 (lệnh/điểm quyết định) | TC-147 đến TC-150 |
| N82 (lệnh/điểm quyết định) | TC-147 đến TC-150 |
| N83 (lệnh/điểm quyết định) | TC-148 đến TC-150 |
| N84 (lệnh/điểm quyết định) | TC-147, TC-148 |
| N85 (lệnh/điểm quyết định) | TC-147 |
| N86 (lệnh/điểm quyết định) | TC-147 đến TC-150 |

Độ phủ đạt được: C0 = 6/6 = 100%; C1 = 7/7 = 100%.

Vòng lặp:

Không có vòng lặp trong thiết kế method.

Sơ đồ CFG: diagrams/X2-cfg-DC-Ticket-markChecked.drawio (ID cell trùng N, CE).

#### F2.25.7 Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat | fake | Seat thật trong bộ nhớ (ST-03), không phụ thuộc ngoài; kiểm tra bằng trạng thái AVAILABLE, HELD, SOLD sau khi gọi | Quan sát được hiệu ứng lên chỗ mà không cần mô phỏng hành vi |

## F3. Bảng test case

Cột Phủ gồm EC, BV, DT-Q, chuyển trạng thái (ST nguồn) và nhánh CE (khi có CFG). TC có Kết quả mong đợi bắt đầu bằng "Chưa xác định" chờ câu hỏi mở tương ứng, chưa tính vào độ phủ ở F4.

### F3.1 DC-TicketReturnPolicy

| TC | DC.operation | Kỹ thuật | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn (BR / UC bước) | Phủ | Test double | Ưu tiên |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | DC-TicketReturnPolicy.matchesPurchaseChannel | bảng quyết định; phân vùng tương đương | ticket.purchaseChannel = ONLINE | ticket, requestChannel = ONLINE | Trả true; vé không đổi | BR-11, UC-008 bước 3 | DT1-Q1, EC-01 | DC-Ticket stub | Cao |
| TC-002 | DC-TicketReturnPolicy.matchesPurchaseChannel | bảng quyết định; phân vùng tương đương | ticket.purchaseChannel = COUNTER (vé mua tại quầy) | ticket, requestChannel = COUNTER | Trả true; vé không đổi | BR-11, UC-008 bước 3 | DT1-Q2, EC-02 | DC-Ticket stub | Cao |
| TC-003 | DC-TicketReturnPolicy.matchesPurchaseChannel | bảng quyết định; phân vùng tương đương | ticket.purchaseChannel = ONLINE | ticket, requestChannel = COUNTER | Trả false; vé không đổi | BR-11, UC-008 3a | DT1-Q3, EC-03 | DC-Ticket stub | Cao |
| TC-004 | DC-TicketReturnPolicy.matchesPurchaseChannel | bảng quyết định; phân vùng tương đương | ticket.purchaseChannel = COUNTER | ticket, requestChannel = ONLINE | Trả false; vé không đổi | BR-11, UC-008 3a | DT1-Q4, EC-04 | DC-Ticket stub | Cao |
| TC-005 | DC-TicketReturnPolicy.isReturnTimeAllowed | phân vùng tương đương | Policy mới tạo, không trạng thái | timeToDeparture = PT-1H | Trả false | BR-12, UC-008 3b | EC-06 | Không | Cao |
| TC-006 | DC-TicketReturnPolicy.isReturnTimeAllowed | giá trị biên | - | timeToDeparture = PT-1S | Trả false | BR-12 | BV-01, EC-06 | Không | Cao |
| TC-007 | DC-TicketReturnPolicy.isReturnTimeAllowed | giá trị biên | - | timeToDeparture = PT0S | Trả false | BR-12 | BV-02, EC-07 | Không | Cao |
| TC-008 | DC-TicketReturnPolicy.isReturnTimeAllowed | phân vùng tương đương | - | timeToDeparture = PT2H | Trả false | BR-12, UC-008 3b | EC-07 | Không | Cao |
| TC-009 | DC-TicketReturnPolicy.isReturnTimeAllowed | giá trị biên | - | timeToDeparture = PT3H59M59S | Trả false | BR-12, UC-008 3b | BV-03, EC-07 | Không | Cao |
| TC-010 | DC-TicketReturnPolicy.isReturnTimeAllowed | giá trị biên | - | timeToDeparture = PT4H | Trả true | BR-12 | BV-04, EC-08 | Không | Cao |
| TC-011 | DC-TicketReturnPolicy.isReturnTimeAllowed | giá trị biên | - | timeToDeparture = PT4H1S | Trả true | BR-12 | BV-05, EC-08 | Không | Cao |
| TC-012 | DC-TicketReturnPolicy.isReturnTimeAllowed | phân vùng tương đương | - | timeToDeparture = PT30H | Trả true | BR-12 | EC-08 | Không | Cao |
| TC-013 | DC-TicketReturnPolicy.calculateRefundAmount | phân vùng tương đương; bảng quyết định | ticket.price = 360.000 đ | timeToDeparture = PT3H (UC-008 ví dụ: còn 3 giờ) | Ném IllegalArgumentException; ticket không đổi | BR-12, UC-008 3b | DT2-Q4, EC-10; CE1, CE2, CE9 | DC-Ticket stub, DC-Money fake | Cao |
| TC-014 | DC-TicketReturnPolicy.calculateRefundAmount | giá trị biên | ticket.price = 360.000 đ | timeToDeparture = PT3H59M59S | Ném IllegalArgumentException; ticket không đổi | BR-12 | BV-06, EC-10; CE1, CE2, CE9 | DC-Ticket stub, DC-Money fake | Cao |
| TC-015 | DC-TicketReturnPolicy.calculateRefundAmount | giá trị biên | ticket.price = 360.000 đ | timeToDeparture = PT4H | RefundQuote(ratePercent = 50, amount = 180.000 đ) | BR-14, UC-008 Mục 5 | BV-07, DT2-Q2, EC-11, EC-13; CE1, CE3, CE5, CE7, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-016 | DC-TicketReturnPolicy.calculateRefundAmount | giá trị biên | ticket.price = 360.000 đ | timeToDeparture = PT4H1S | RefundQuote(50, 180.000 đ) | BR-14 | BV-08, EC-11; CE1, CE3, CE5, CE7, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-017 | DC-TicketReturnPolicy.calculateRefundAmount | phân vùng tương đương | ticket.price = 360.000 đ | timeToDeparture = PT12H | RefundQuote(50, 180.000 đ) | BR-14, UC-008 Mục 5 | DT2-Q2, EC-11; CE1, CE3, CE5, CE7, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-018 | DC-TicketReturnPolicy.calculateRefundAmount | giá trị biên | ticket.price = 360.000 đ | timeToDeparture = PT23H59M59S | RefundQuote(50, 180.000 đ) | BR-14 | BV-09, EC-11; CE1, CE3, CE5, CE7, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-019 | DC-TicketReturnPolicy.calculateRefundAmount | giá trị biên | ticket.price = 360.000 đ | timeToDeparture = PT24H | RefundQuote(ratePercent = 90, amount = 324.000 đ) | BR-13, UC-008 Mục 5 | BV-10, DT2-Q1, EC-12, EC-13; CE1, CE3, CE4, CE6, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-020 | DC-TicketReturnPolicy.calculateRefundAmount | giá trị biên | ticket.price = 360.000 đ | timeToDeparture = PT24H1S | RefundQuote(90, 324.000 đ) | BR-13 | BV-11, EC-12; CE1, CE3, CE4, CE6, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-021 | DC-TicketReturnPolicy.calculateRefundAmount | phân vùng tương đương | ticket.price = 360.000 đ | timeToDeparture = PT49H | RefundQuote(90, 324.000 đ) | BR-13, UC-008 Mục 5 | DT2-Q1, EC-12; CE1, CE3, CE4, CE6, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-022 | DC-TicketReturnPolicy.calculateRefundAmount | phân vùng tương đương | ticket.price = 1.005 đ | timeToDeparture = PT12H | RefundQuote(50, 503 đ) (502,5 làm tròn lên) | BR-14, ASM-102 | EC-11, EC-14; CE1, CE3, CE5, CE7, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-023 | DC-TicketReturnPolicy.calculateRefundAmount | phân vùng tương đương | ticket.price = 1.006 đ | timeToDeparture = PT49H | RefundQuote(90, 905 đ) (905,4 làm tròn xuống) | BR-13, ASM-102 | EC-12, EC-14; CE1, CE3, CE4, CE6, CE8 | DC-Ticket stub, DC-Money fake | Cao |
| TC-024 | DC-TicketReturnPolicy.getTicketReturnInfo | phân vùng tương đương | ticket stub: ticketCode SV0000123; getSeatCode() = A05; getPrice() = 360.000 đ; trip.getRouteAndDepartureTime() = ("Hà Nội - Lào Cai", 21:00 03/02/2027) | ticket | TicketReturnInfo(ticketCode SV0000123, schedule ("Hà Nội - Lào Cai", 21:00 03/02/2027), seatCode A05, price 360.000 đ); ticket không đổi | UC-008 bước 5, Dữ liệu ra 1 #1-#4 | EC-16 | DC-Ticket stub, DC-Trip stub | Trung bình |
| TC-025 | DC-TicketReturnPolicy.determineRefundMethod | phân vùng tương đương | ticket.purchaseChannel = ONLINE | ticket | Trả VIA_GATEWAY; ticket không đổi | BR-15, UC-008 bước 7 | EC-18 | DC-Ticket stub | Cao |
| TC-026 | DC-TicketReturnPolicy.determineRefundMethod | phân vùng tương đương | ticket.purchaseChannel = COUNTER | ticket | Trả CASH_AT_COUNTER; ticket không đổi | BR-16, UC-008 7a | EC-19 | DC-Ticket stub | Cao |
| TC-027 | DC-TicketReturnPolicy.getCancelImpactInfo | phân vùng tương đương | ticket.purchaseChannel = ONLINE; ticket.getPrice() = 360.000 đ | ticket | CancelImpactInfo(purchaseChannel ONLINE, refundAmount 360.000 đ); ticket không đổi | BR-17, UC-013 bước 3 | EC-21 | DC-Ticket stub, DC-Money fake | Trung bình |
| TC-028 | DC-TicketReturnPolicy.getCancelImpactInfo | phân vùng tương đương | ticket.purchaseChannel = COUNTER; ticket.getPrice() = 300.000 đ | ticket | CancelImpactInfo(purchaseChannel COUNTER, refundAmount 300.000 đ); ticket không đổi | BR-17, UC-013 bước 3 | EC-22 | DC-Ticket stub, DC-Money fake | Trung bình |
| TC-029 | DC-TicketReturnPolicy.calculateTripCancelRefundAmount | phân vùng tương đương | ticket ONLINE, price = 360.000 đ | ticket | Trả 360.000 đ; ticket không đổi | BR-17, BR-19, UC-013 bước 6 | EC-24 | DC-Ticket stub, DC-Money fake | Cao |
| TC-030 | DC-TicketReturnPolicy.calculateTripCancelRefundAmount | phân vùng tương đương | ticket COUNTER, price = 300.000 đ | ticket | Trả 300.000 đ; ticket không đổi | BR-17, BR-19, UC-013 bước 6 | EC-25 | DC-Ticket stub, DC-Money fake | Cao |
| TC-031 | DC-TicketReturnPolicy.calculateTripCancelRefundAmount | giá trị biên | ticket ONLINE, price = 1 đ | ticket | Trả 1 đ | BR-17 | BV-12, EC-24 | DC-Ticket stub, DC-Money fake | Cao |

### F3.2 DC-Booking

| TC | DC.operation | Kỹ thuật | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn (BR / UC bước) | Phủ | Test double | Ưu tiên |
|---|---|---|---|---|---|---|---|---|---|
| TC-032 | DC-Booking.createBooking | giá trị biên | - | bookingId BK-0001, trip stub, travelerInfos = [] (size 0) | Ném IllegalArgumentException; không có Booking | P12 F2 tiền điều kiện | BV-13, EC-29 | DC-Trip stub | Trung bình |
| TC-033 | DC-Booking.createBooking | giá trị biên; chuyển trạng thái | Trip stub có chỗ A05 AVAILABLE | bookingId BK-0001, trip, travelerInfos = [TI-A05] (size 1) | Booking DRAFT; getBookingId() = BK-0001; getTrip() = trip; paymentAttemptCount = 0; Seat A05 vẫn AVAILABLE | ST-01 T1, ASM-43, ASM-44 | BV-14, EC-27; ST-01 T1 | DC-Trip stub | Trung bình |
| TC-034 | DC-Booking.createBooking | giá trị biên | Trip stub có chỗ A05 đến A09 AVAILABLE | bookingId BK-0001, trip, travelerInfos = [TI-A05..TI-A09] (size 5) | Booking DRAFT; paymentAttemptCount = 0; mọi Seat vẫn AVAILABLE | BR-01, ASM-43 | BV-15, EC-27 | DC-Trip stub | Trung bình |
| TC-035 | DC-Booking.createBooking | giá trị biên | Trip stub có chỗ A05 đến A10 AVAILABLE | bookingId BK-0001, trip, travelerInfos = [TI-A05..TI-A10] (size 6) | Booking DRAFT được tạo, không ném ngoại lệ (BR-01 do isWithinSeatLimit kiểm) | ASM-43, UC-002 6a | BV-16, EC-28 | DC-Trip stub | Trung bình |
| TC-036 | DC-Booking.createBooking | phân vùng tương đương | - | bookingId BK-0001, trip, travelerInfos = [TI-A05, TI-A05] (trùng seatCode) | Chưa xác định: chờ Q-114 | P12 F7 | EC-30 | DC-Trip stub | Trung bình |
| TC-037 | DC-Booking.isWithinSeatLimit | giá trị biên | Booking DRAFT, travelerInfos = [TI-A05] | - | Trả true; Booking không đổi | BR-01 | BV-17, EC-32 | DC-Trip stub | Cao |
| TC-038 | DC-Booking.isWithinSeatLimit | phân vùng tương đương | Booking DRAFT, travelerInfos = [TI-A05, TI-A06] (UC-002 Mục 5) | - | Trả true; Booking không đổi | BR-01 | EC-32 | DC-Trip stub | Cao |
| TC-039 | DC-Booking.isWithinSeatLimit | giá trị biên | Booking DRAFT, travelerInfos = [TI-A05..TI-A09] (5 chỗ) | - | Trả true | BR-01 | BV-18, EC-32 | DC-Trip stub | Cao |
| TC-040 | DC-Booking.isWithinSeatLimit | giá trị biên | Booking DRAFT, travelerInfos = [TI-A05..TI-A10] (6 chỗ) | - | Trả false; Booking không đổi | BR-01, UC-002 6a | BV-19, EC-33 | DC-Trip stub | Cao |
| TC-041 | DC-Booking.validateTravelerInfo | giá trị biên; vòng lặp | travelerInfos = [(A05, "A", 0912345678)] (1 phần tử) | - | Trả NONE; Booking không đổi | ASM-15, UC-002 bước 7 | BV-21, BV-23, DT3-Q3, EC-35, EC-38, EC-44; CE10, CE11, CE13, CE15 đến CE17, CE19, CE20, CE23 | DC-PhoneNumber fake | Cao |
| TC-042 | DC-Booking.validateTravelerInfo | vòng lặp (m) | travelerInfos = [TI-A05, TI-A06] (2 phần tử) | - | Trả NONE; Booking không đổi | ASM-15, UC-002 bước 7 | DT3-Q3, EC-35, EC-38; CE10, CE11, CE13, CE15 đến CE17, CE19, CE20, CE23 | DC-PhoneNumber fake | Cao |
| TC-043 | DC-Booking.validateTravelerInfo | vòng lặp (n-1) | travelerInfos = [TI-A05..TI-A08] (4 phần tử) | - | Trả NONE; Booking không đổi | ASM-15, UC-002 bước 7 | DT3-Q3, EC-35, EC-38; CE10, CE11, CE13, CE15 đến CE17, CE19, CE20, CE23 | DC-PhoneNumber fake | Cao |
| TC-044 | DC-Booking.validateTravelerInfo | vòng lặp (n) | travelerInfos = [TI-A05..TI-A09] (5 phần tử) | - | Trả NONE; Booking không đổi | ASM-15, UC-002 bước 7 | DT3-Q3, EC-35, EC-38; CE10, CE11, CE13, CE15 đến CE17, CE19, CE20, CE23 | DC-PhoneNumber fake | Cao |
| TC-045 | DC-Booking.validateTravelerInfo | giá trị biên; bảng quyết định | travelerInfos = [(A05, "", 0912345678)] | - | Trả MISSING_INFO; Booking không đổi | ASM-15, UC-002 7a | BV-20, DT3-Q1, EC-36; CE10 đến CE12, CE21 | DC-PhoneNumber fake | Cao |
| TC-046 | DC-Booking.validateTravelerInfo | phân vùng tương đương | travelerInfos = [(A05, "   ", 0912345678)] (3 dấu cách) | - | Trả MISSING_INFO | P12 F3, UC-002 7a | DT3-Q1, EC-37; CE10 đến CE12, CE21 | DC-PhoneNumber fake | Cao |
| TC-047 | DC-Booking.validateTravelerInfo | phân vùng tương đương | travelerInfos = [(A05, "Nguyễn Văn An", "")] | - | Trả MISSING_INFO | ASM-15, UC-002 7a | DT3-Q1, EC-39; CE10, CE11, CE13, CE14, CE21 | DC-PhoneNumber fake | Cao |
| TC-048 | DC-Booking.validateTravelerInfo | giá trị biên; bảng quyết định | travelerInfos = [(A05, "Nguyễn Văn An", 091234567)] (9 chữ số) | - | Trả INVALID_PHONE | ASM-15, UC-002 7b | BV-22, DT3-Q2, EC-40; CE10, CE11, CE13, CE15 đến CE18, CE22 | DC-PhoneNumber fake | Cao |
| TC-049 | DC-Booking.validateTravelerInfo | giá trị biên | travelerInfos = [(A05, "Nguyễn Văn An", 09123456789)] (11 chữ số) | - | Trả INVALID_PHONE | ASM-15, UC-002 7b | BV-24, DT3-Q2, EC-41; CE10, CE11, CE13, CE15 đến CE18, CE22 | DC-PhoneNumber fake | Cao |
| TC-050 | DC-Booking.validateTravelerInfo | phân vùng tương đương | travelerInfos = [(A05, "Nguyễn Văn An", 1912345678)] | - | Trả INVALID_PHONE | ASM-15, UC-002 7b | DT3-Q2, EC-42; CE10, CE11, CE13, CE15 đến CE18, CE22 | DC-PhoneNumber fake | Cao |
| TC-051 | DC-Booking.validateTravelerInfo | phân vùng tương đương | travelerInfos = [(A05, "Nguyễn Văn An", 09123abc78)] | - | Trả INVALID_PHONE | ASM-15, UC-002 7b | DT3-Q2, EC-43; CE10, CE11, CE13, CE15 đến CE18, CE22 | DC-PhoneNumber fake | Cao |
| TC-052 | DC-Booking.validateTravelerInfo | bảng quyết định | travelerInfos = [(A05, "Nguyễn Văn An", 091234567), (A06, "", 0987654321)] | - | Trả MISSING_INFO (thiếu thông tin được báo trước sai định dạng) | UC-002 7a, 7b; Q-34 | DT3-Q1; CE10 đến CE13, CE15, CE21 | DC-PhoneNumber fake | Cao |
| TC-053 | DC-Booking.validateTravelerInfo | bảng quyết định | travelerInfos = [(A05, "Nguyễn Văn An", 091234567), (A06, "Trần Thị Bình", "")] | - | Trả MISSING_INFO | UC-002 7a, 7b; Q-34 | DT3-Q1; CE10, CE11, CE13 đến CE15, CE21 | DC-PhoneNumber fake | Cao |
| TC-054 | DC-Booking.validateTravelerInfo | vòng lặp (n) | travelerInfos = [TI-A05..TI-A08 hợp lệ, (A09, "", 0945678901)] (phần tử thứ 5 thiếu họ tên) | - | Trả MISSING_INFO | UC-002 7a | DT3-Q1, EC-36; CE10 đến CE13, CE15, CE21 | DC-PhoneNumber fake | Cao |
| TC-055 | DC-Booking.validateTravelerInfo | vòng lặp (n) | travelerInfos = [TI-A05..TI-A08 hợp lệ, (A09, "Hoàng Văn Em", 094567890)] (phần tử thứ 5 sai định dạng) | - | Trả INVALID_PHONE | UC-002 7b | DT3-Q2, EC-40; CE10, CE11, CE13, CE15 đến CE19, CE22 | DC-PhoneNumber fake | Cao |
| TC-056 | DC-Booking.validateTravelerInfo | vòng lặp | travelerInfos = [(A05, "Nguyễn Văn An", 091234567), TI-A06] (phần tử đầu sai định dạng) | - | Trả INVALID_PHONE | UC-002 7b | DT3-Q2, EC-40; CE10, CE11, CE13, CE15 đến CE18, CE22 | DC-PhoneNumber fake | Cao |
| TC-057 | DC-Booking.calculateTotal | giá trị biên | Booking DRAFT, travelerInfos = [TI-A05]; trip.determineTicketPrice() = 360.000 đ | - | Trả 360.000 đ; ticketPrice = 360.000 đ; totalAmount = 360.000 đ; status vẫn DRAFT | BR-06 | BV-25, EC-46, EC-50; CE24, CE26 đến CE28 | DC-Trip stub, DC-Seat fake, DC-Money fake | Cao |
| TC-058 | DC-Booking.calculateTotal | phân vùng tương đương | Booking DRAFT, travelerInfos = [TI-A05, TI-A06]; trip.determineTicketPrice() = 360.000 đ | - | Trả 720.000 đ; ticketPrice = 360.000 đ; totalAmount = 720.000 đ; trip.determineTicketPrice() được gọi đúng 1 lần | BR-06, UC-002 Mục 5 ví dụ | EC-46, EC-50; CE24, CE26 đến CE28 | mock xác minh số lần gọi determineTicketPrice; DC-Trip stub, DC-Seat fake, DC-Money fake | Cao |
| TC-059 | DC-Booking.calculateTotal | giá trị biên | Booking DRAFT, travelerInfos = [TI-A05..TI-A09]; trip.determineTicketPrice() = 360.000 đ | - | Trả 1.800.000 đ; totalAmount = 1.800.000 đ | BR-06 | BV-26, EC-50; CE24, CE26 đến CE28 | DC-Trip stub, DC-Seat fake, DC-Money fake | Cao |
| TC-060 | DC-Booking.calculateTotal | phân vùng tương đương | Booking HELD (đã calculateTotal 720.000 đ, đã holdSeats); sau đó stub đổi determineTicketPrice() = 400.000 đ | - | Ném InvalidStateException; ticketPrice vẫn 360.000 đ; totalAmount vẫn 720.000 đ; status HELD | P12 F2 tiền điều kiện, ASM-22 | EC-47; CE24, CE25, CE29 | DC-Trip stub, DC-Seat fake, DC-Money fake | Cao |
| TC-061 | DC-Booking.calculateTotal | phân vùng tương đương | Booking TICKETED (đã issueTickets), totalAmount = 720.000 đ | - | Ném InvalidStateException; totalAmount vẫn 720.000 đ; status TICKETED | P12 F2 tiền điều kiện | EC-48; CE24, CE25, CE29 | DC-Trip stub, DC-Seat fake, DC-Money fake | Cao |
| TC-062 | DC-Booking.calculateTotal | phân vùng tương đương | Booking EXPIRED, totalAmount = 720.000 đ | - | Ném InvalidStateException; totalAmount vẫn 720.000 đ; status EXPIRED | P12 F2 tiền điều kiện | EC-49; CE24, CE25, CE29 | DC-Trip stub, DC-Seat fake, DC-Money fake | Cao |
| TC-063 | DC-Booking.holdSeats | giá trị biên; chuyển trạng thái | Booking DRAFT [TI-A05]; Seat A05 AVAILABLE | now = 09:00 03/02/2027 | Booking HELD; holdStartTime = 09:00 03/02/2027; Seat A05 HELD | ST-01 T2, BR-03, UC-002 bước 9 | BV-27, DT4-Q1, EC-52, EC-56, EC-59; ST-01 T2; CE30, CE32 đến CE35, CE37 đến CE39 | DC-Trip stub, DC-Seat fake | Cao |
| TC-064 | DC-Booking.holdSeats | vòng lặp (m); chuyển trạng thái | Booking DRAFT [TI-A05, TI-A06]; Seat A05, A06 AVAILABLE | now = 09:00 03/02/2027 | Booking HELD; holdStartTime = 09:00 03/02/2027; A05, A06 HELD; trip.findSeats gọi với ["A05", "A06"] đúng thứ tự | ST-01 T2, BR-03 | DT4-Q1, EC-56; ST-01 T2; CE30, CE32 đến CE35, CE37 đến CE39 | mock xác minh tham số findSeats; DC-Trip stub, DC-Seat fake | Cao |
| TC-065 | DC-Booking.holdSeats | vòng lặp (n-1) | Booking DRAFT [TI-A05..TI-A08]; 4 Seat AVAILABLE | now = 09:00 03/02/2027 | Booking HELD; 4 Seat HELD | ST-01 T2 | DT4-Q1; CE30, CE32 đến CE35, CE37 đến CE39 | DC-Trip stub, DC-Seat fake | Cao |
| TC-066 | DC-Booking.holdSeats | giá trị biên; vòng lặp (n) | Booking DRAFT [TI-A05..TI-A09]; 5 Seat AVAILABLE | now = 09:00 03/02/2027 | Booking HELD; 5 Seat HELD | ST-01 T2, BR-01 | BV-28, DT4-Q1, EC-59; CE30, CE32 đến CE35, CE37 đến CE39 | DC-Trip stub, DC-Seat fake | Cao |
| TC-067 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | Booking HELD (đã holdSeats lúc 09:00), A05, A06 HELD | now = 09:05 03/02/2027 | Ném InvalidStateException; holdStartTime vẫn 09:00 03/02/2027; A05, A06 vẫn HELD | P12 F6.2, F2 tiền điều kiện | DT4-Q4, EC-53; P12 F6.2 sự kiện bị từ chối; CE30, CE31, CE40 | DC-Trip stub, DC-Seat fake | Cao |
| TC-068 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | Booking TICKETED; A05, A06 SOLD | now = 09:00 03/02/2027 | Ném InvalidStateException; status TICKETED; A05, A06 vẫn SOLD | P12 F6.2 | DT4-Q4, EC-54; P12 F6.2; CE30, CE31, CE40 | DC-Trip stub, DC-Seat fake | Cao |
| TC-069 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | Booking EXPIRED; A05, A06 AVAILABLE | now = 09:00 03/02/2027 | Ném InvalidStateException; status EXPIRED; A05, A06 vẫn AVAILABLE | P12 F6.2 | DT4-Q3, EC-55; P12 F6.2; CE30, CE31, CE40 | DC-Trip stub, DC-Seat fake | Cao |
| TC-070 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | Booking DRAFT [TI-A05, TI-A06]; A05 HELD bởi lần đặt khác, A06 AVAILABLE | now = 09:00 03/02/2027 | Ném SeatAlreadyHeldException; Booking vẫn DRAFT, holdStartTime rỗng; A06 vẫn AVAILABLE (vòng lặp dừng ở chỗ lỗi đầu tiên) | BR-03, P12 F2, F3 bước 3 | DT4-Q2, EC-57; ST-01 T2 guard; CE30, CE32 đến CE34, CE36, CE41 | DC-Trip stub, DC-Seat fake | Cao |
| TC-071 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | Booking DRAFT [TI-A05, TI-A06]; A05 AVAILABLE, A06 SOLD | now = 09:00 03/02/2027 | Ném SeatAlreadyHeldException; Booking vẫn DRAFT, holdStartTime rỗng | BR-02, BR-03, P12 F2 | DT4-Q2, EC-58; ST-01 T2 guard; CE30, CE32 đến CE34, CE36 đến CE38, CE41 | DC-Trip stub, DC-Seat fake | Cao |
| TC-072 | DC-Booking.holdSeats | vòng lặp (n) | Booking DRAFT [TI-A05..TI-A09]; A09 (chỗ cuối) HELD bởi lần đặt khác | now = 09:00 03/02/2027 | Ném SeatAlreadyHeldException; Booking vẫn DRAFT, holdStartTime rỗng | BR-03, P12 F2 | DT4-Q2, EC-57; ST-01 T2 guard; CE30, CE32 đến CE34, CE36 đến CE38, CE41 | DC-Trip stub, DC-Seat fake | Cao |
| TC-073 | DC-Booking.holdSeats | chuyển trạng thái | Booking DRAFT [TI-A05, TI-A06]; A05 AVAILABLE, A06 HELD bởi lần đặt khác | now = 09:00 03/02/2027 | Chưa xác định: chờ Q-110. Ném SeatAlreadyHeldException; trạng thái Seat A05 sau lỗi: chưa xác định (chờ Q-110) | P12 F2 "tất cả hoặc không" | EC-57 | DC-Trip stub, DC-Seat fake | Cao |
| TC-074 | DC-Booking.releaseSeats | giá trị biên; chuyển trạng thái; vòng lặp | Booking HELD [TI-A05]; Seat A05 HELD | - | status EXPIRED; Seat A05 AVAILABLE | ST-01 T4, BR-08, UC-002 9a1 | BV-29, EC-62, EC-66; ST-01 T4; CE42, CE44 đến CE48 | DC-Trip stub, DC-Seat fake | Cao |
| TC-075 | DC-Booking.releaseSeats | vòng lặp (m) | Booking HELD [TI-A05, TI-A06]; A05, A06 HELD | - | status EXPIRED; A05, A06 AVAILABLE | ST-01 T4, BR-08 | EC-62; ST-01 T4; CE42, CE44 đến CE48 | DC-Trip stub, DC-Seat fake | Cao |
| TC-076 | DC-Booking.releaseSeats | vòng lặp (n-1) | Booking HELD [TI-A05..TI-A08]; 4 Seat HELD | - | status EXPIRED; 4 Seat AVAILABLE | ST-01 T4, BR-08 | EC-62; ST-01 T4; CE42, CE44 đến CE48 | DC-Trip stub, DC-Seat fake | Cao |
| TC-077 | DC-Booking.releaseSeats | giá trị biên; vòng lặp (n) | Booking HELD [TI-A05..TI-A09]; 5 Seat HELD | - | status EXPIRED; 5 Seat AVAILABLE | ST-01 T4, BR-08 | BV-30, EC-62; ST-01 T4; CE42, CE44 đến CE48 | DC-Trip stub, DC-Seat fake | Cao |
| TC-078 | DC-Booking.releaseSeats | chuyển trạng thái | Booking DRAFT [TI-A05]; Seat A05 AVAILABLE | - | Không ngoại lệ; status vẫn DRAFT; A05 vẫn AVAILABLE | P12 F6.2, F3 bước 1 | EC-63; P12 F6.2; CE42, CE43, CE49 | DC-Trip stub, DC-Seat fake | Cao |
| TC-079 | DC-Booking.releaseSeats | chuyển trạng thái | Booking TICKETED [TI-A05, TI-A06]; A05, A06 SOLD | - | Không ngoại lệ; status vẫn TICKETED; A05, A06 vẫn SOLD (thanh toán đã thắng mốc hết hạn) | P12 F6.2, ASM-103 | EC-64; P12 F6.2; CE42, CE43, CE49 | DC-Trip stub, DC-Seat fake | Cao |
| TC-080 | DC-Booking.releaseSeats | chuyển trạng thái | Booking EXPIRED [TI-A05]; A05 AVAILABLE rồi được lần đặt khác giữ (HELD) | - | Không ngoại lệ; status vẫn EXPIRED; A05 vẫn HELD bởi lần đặt khác (mốc giao lặp không trả nhầm chỗ) | P12 F6.2, F3 (mốc giao ít nhất một lần) | EC-65; P12 F6.2; CE42, CE43, CE49 | DC-Trip stub, DC-Seat fake | Cao |
| TC-081 | DC-Booking.issueTickets | giá trị biên; vòng lặp; chuyển trạng thái | Booking HELD [TI-A05]; A05 HELD; ticketPrice 360.000 đ; generator trả SV0000101 | paymentReference PAY-0001 | Trả 1 vé: ticketCode SV0000101, seatCode A05, travelerName "Nguyễn Văn An", travelerPhone 0912345678, price 360.000 đ, purchaseChannel ONLINE, status ISSUED; Booking TICKETED; A05 SOLD; nextTicketCode gọi đúng 1 lần | BR-09, BR-10, ST-01 T3, UC-002 bước 11 | BV-31, EC-68, EC-72; ST-01 T3; CE50, CE52 đến CE56 | mock xác minh số lần gọi nextTicketCode; DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-082 | DC-Booking.issueTickets | vòng lặp (m); chuyển trạng thái | Booking HELD [TI-A05, TI-A06]; A05, A06 HELD; ticketPrice 360.000 đ; generator trả SV0000101, SV0000102 | paymentReference PAY-0001 | Trả 2 vé theo thứ tự travelerInfos: (SV0000101, A05, "Nguyễn Văn An", 0912345678) rồi (SV0000102, A06, "Trần Thị Bình", 0987654321); mỗi vé price 360.000 đ, ONLINE, ISSUED; A05, A06 SOLD; Booking TICKETED; nextTicketCode gọi đúng 2 lần | BR-09, BR-10, UC-002 Mục 5 ví dụ | EC-68; ST-01 T3; CE50, CE52 đến CE56 | mock xác minh số lần gọi nextTicketCode; DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-083 | DC-Booking.issueTickets | vòng lặp (n-1) | Booking HELD [TI-A05..TI-A08]; 4 Seat HELD; generator trả SV0000101..SV0000104 | paymentReference PAY-0001 | Trả 4 vé, mã SV0000101..SV0000104 khác nhau, seatCode A05..A08 theo thứ tự; 4 Seat SOLD; Booking TICKETED | BR-10 | EC-68; ST-01 T3; CE50, CE52 đến CE56 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-084 | DC-Booking.issueTickets | giá trị biên; vòng lặp (n) | Booking HELD [TI-A05..TI-A09]; 5 Seat HELD; generator trả SV0000101..SV0000105 | paymentReference PAY-0001 | Trả 5 vé, 5 mã khác nhau; 5 Seat SOLD; Booking TICKETED | BR-01, BR-10 | BV-32, EC-72; ST-01 T3; CE50, CE52 đến CE56 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-085 | DC-Booking.issueTickets | phân vùng tương đương | Booking HELD [TI-A05, TI-A06]; calculateTotal đã chốt ticketPrice 360.000 đ; sau đó stub đổi determineTicketPrice() = 400.000 đ | paymentReference PAY-0001 | Cả hai vé price 360.000 đ (giá chốt, không tính lại) | ASM-22, P12 F3 | EC-68; CE50, CE52 đến CE56 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-086 | DC-Booking.issueTickets | phân vùng tương đương | Booking HELD [TI-A05]; A05 HELD | paymentReference PAY-0001 | getPaymentReference() = PAY-0001 sau khi phát hành | ASM-41, ASM-114 | EC-68; CE50, CE52 đến CE56 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-087 | DC-Booking.issueTickets | chuyển trạng thái | Booking DRAFT [TI-A05]; A05 AVAILABLE | paymentReference PAY-0001 | Ném InvalidStateException; nextTicketCode không được gọi; status vẫn DRAFT; A05 vẫn AVAILABLE | P12 F6.2, F2 tiền điều kiện | EC-69; P12 F6.2; CE50, CE51, CE57 | mock xác minh không gọi generator; DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-088 | DC-Booking.issueTickets | chuyển trạng thái | Booking TICKETED (đã phát hành 2 vé, generator đã được gọi 2 lần); A05, A06 SOLD | paymentReference PAY-0001 | Ném InvalidStateException; generator vẫn chỉ được gọi 2 lần (không phát hành lại); status vẫn TICKETED; A05, A06 vẫn SOLD | P12 F6.2, BR-10 | EC-70; P12 F6.2; CE50, CE51, CE57 | mock xác minh số lần gọi; DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-089 | DC-Booking.issueTickets | chuyển trạng thái | Booking EXPIRED [TI-A05]; A05 AVAILABLE | paymentReference PAY-0001 | Ném InvalidStateException; generator không được gọi; A05 vẫn AVAILABLE | P12 F6.2, ASM-103 | EC-71; P12 F6.2; CE50, CE51, CE57 | mock xác minh không gọi generator; DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-PhoneNumber fake, DC-Money fake | Cao |
| TC-090 | DC-Booking.getBookingSummary | giá trị biên | Booking TICKETED [TI-A05], vé SV0000101, totalAmount 360.000 đ | - | BookingSummary(tickets = [SV0000101], totalAmount = 360.000 đ) | UC-002 Dữ liệu ra 4 | BV-33, EC-75, EC-79 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-Money fake | Trung bình |
| TC-091 | DC-Booking.getBookingSummary | phân vùng tương đương | Booking TICKETED [TI-A05, TI-A06], vé SV0000101, SV0000102, totalAmount 720.000 đ | - | BookingSummary(tickets = [SV0000101, SV0000102] đúng các vé đã phát hành, totalAmount = 720.000 đ) | UC-002 Dữ liệu ra 4 #7, BR-06 | EC-75, EC-79 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-Money fake | Trung bình |
| TC-092 | DC-Booking.getBookingSummary | giá trị biên | Booking TICKETED 5 chỗ, totalAmount 1.800.000 đ | - | BookingSummary(5 vé, totalAmount = 1.800.000 đ) | UC-002 Dữ liệu ra 4, BR-06 | BV-34, EC-79 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-Money fake | Trung bình |
| TC-093 | DC-Booking.getBookingSummary | phân vùng tương đương | Booking DRAFT [TI-A05] | - | Ném InvalidStateException; Booking không đổi | P12 F2 tiền điều kiện | EC-76 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-Money fake | Trung bình |
| TC-094 | DC-Booking.getBookingSummary | phân vùng tương đương | Booking HELD [TI-A05] | - | Ném InvalidStateException; Booking không đổi | P12 F2 tiền điều kiện | EC-77 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-Money fake | Trung bình |
| TC-095 | DC-Booking.getBookingSummary | phân vùng tương đương | Booking EXPIRED [TI-A05] | - | Ném InvalidStateException; Booking không đổi | P12 F2 tiền điều kiện | EC-78 | DC-Trip stub, DC-Seat fake, IF-15 ITicketingIdGenerator stub + mock, DC-Money fake | Trung bình |
| TC-096 | DC-Booking.getHoldExpiryTime | phân vùng tương đương | Booking HELD, holdStartTime = 10:00 03/02/2027 | - | Trả 10:10 03/02/2027; holdStartTime không đổi | BR-07 | EC-81 | DC-Trip stub, DC-Seat fake | Cao |
| TC-097 | DC-Booking.getHoldExpiryTime | giá trị biên | Booking HELD, holdStartTime = 23:55 28/02/2027 | - | Trả 00:05 01/03/2027 | BR-07 | BV-35, EC-82 | DC-Trip stub, DC-Seat fake | Cao |
| TC-098 | DC-Booking.getHoldExpiryTime | phân vùng tương đương | Booking DRAFT (holdStartTime rỗng) | - | Ném InvalidStateException; Booking không đổi | P12 F2 tiền điều kiện | EC-83 | DC-Trip stub, DC-Seat fake | Cao |
| TC-099 | DC-Booking.isHoldExpired | giá trị biên | Booking HELD, holdStartTime = 10:00:00 03/02/2027 | now = 10:00:00 03/02/2027 | Trả false; Booking không đổi | BR-07 | BV-36, EC-84 | DC-Trip stub, DC-Seat fake | Cao |
| TC-100 | DC-Booking.isHoldExpired | phân vùng tương đương | Booking HELD, holdStartTime = 10:00:00 03/02/2027 | now = 10:05:00 03/02/2027 | Trả false | BR-07 | EC-84 | DC-Trip stub, DC-Seat fake | Cao |
| TC-101 | DC-Booking.isHoldExpired | giá trị biên | Booking HELD, holdStartTime = 10:00:00 03/02/2027 | now = 10:09:59 03/02/2027 | Trả false | BR-07, UC-002 10a | BV-37, EC-84 | DC-Trip stub, DC-Seat fake | Cao |
| TC-102 | DC-Booking.isHoldExpired | giá trị biên | Booking HELD, holdStartTime = 10:00:00 03/02/2027 | now = 10:10:00 03/02/2027 | Trả true | BR-07, ASM-112 | BV-38, EC-85 | DC-Trip stub, DC-Seat fake | Cao |
| TC-103 | DC-Booking.isHoldExpired | giá trị biên | Booking HELD, holdStartTime = 10:00:00 03/02/2027 | now = 10:10:01 03/02/2027 | Trả true | BR-07, UC-002 9a | BV-39, EC-85 | DC-Trip stub, DC-Seat fake | Cao |
| TC-104 | DC-Booking.isHoldExpired | phân vùng tương đương | Booking HELD, holdStartTime = 10:00:00 03/02/2027 | now = 10:15:00 03/02/2027 | Trả true | BR-07, UC-002 9a | EC-85 | DC-Trip stub, DC-Seat fake | Cao |
| TC-105 | DC-Booking.isHoldExpired | phân vùng tương đương | Booking DRAFT (holdStartTime rỗng) | now = 10:00:00 03/02/2027 | Ném InvalidStateException; Booking không đổi | P12 F2 tiền điều kiện | EC-86 | DC-Trip stub, DC-Seat fake | Cao |
| TC-106 | DC-Booking.startPaymentAttempt | phân vùng tương đương | Booking HELD, bookingId BK-0001, paymentAttemptCount = 0 | - | Trả "BK-0001-1"; paymentAttemptCount = 1 | P12 F2, P11b IF-01.requestPayment | EC-88, EC-92; CE58, CE60, CE61 | DC-Trip stub, DC-Seat fake | Trung bình |
| TC-107 | DC-Booking.startPaymentAttempt | phân vùng tương đương | Booking HELD, bookingId BK-0001, đã gọi startPaymentAttempt một lần (paymentAttemptCount = 1) | - | Trả "BK-0001-2"; paymentAttemptCount = 2 | P12 F2 | EC-88, EC-93; CE58, CE60, CE61 | DC-Trip stub, DC-Seat fake | Trung bình |
| TC-108 | DC-Booking.startPaymentAttempt | phân vùng tương đương | Booking DRAFT [TI-A05], bookingId BK-0001, paymentAttemptCount = 0 | - | Ném InvalidStateException; paymentAttemptCount vẫn 0 (xác nhận bằng getPaymentAttemptCount() = 0, ASM-114) | P12 F2 tiền điều kiện | EC-89; CE58, CE59, CE62 | DC-Trip stub, DC-Seat fake | Trung bình |
| TC-109 | DC-Booking.startPaymentAttempt | phân vùng tương đương | Booking TICKETED, paymentAttemptCount = 1 | - | Ném InvalidStateException; paymentAttemptCount vẫn 1 | P12 F2 tiền điều kiện | EC-90; CE58, CE59, CE62 | DC-Trip stub, DC-Seat fake | Trung bình |
| TC-110 | DC-Booking.startPaymentAttempt | phân vùng tương đương | Booking EXPIRED, paymentAttemptCount = 1 | - | Ném InvalidStateException; paymentAttemptCount vẫn 1 | P12 F2 tiền điều kiện | EC-91; CE58, CE59, CE62 | DC-Trip stub, DC-Seat fake | Trung bình |

### F3.3 DC-Ticket

| TC | DC.operation | Kỹ thuật | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn (BR / UC bước) | Phủ | Test double | Ưu tiên |
|---|---|---|---|---|---|---|---|---|---|
| TC-111 | DC-Ticket.createTicket | phân vùng tương đương; chuyển trạng thái | Seat A05 SOLD (do Booking); trip stub | ticketCode SV0000123, trip, seat A05, travelerInfo (A05, "Nguyễn Văn An", "0912345678"), price 360.000 đ, ONLINE | Vé: ticketCode SV0000123, trip, seatCode A05, travelerName "Nguyễn Văn An", travelerPhone PhoneNumber(0912345678), price 360.000 đ, purchaseChannel ONLINE, status ISSUED, checkedTime rỗng; Seat A05 không đổi (SOLD) | BR-09, BR-10, ST-02 T1 | EC-94, EC-96, EC-99, EC-102; ST-02 T1 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-112 | DC-Ticket.createTicket | phân vùng tương đương | Seat A06 AVAILABLE; trip stub | ticketCode SV0000124, trip, seat A06, travelerInfo (A06, "Trần Thị Bình", "0987654321"), price 300.000 đ, COUNTER | Vé ISSUED, purchaseChannel COUNTER, price 300.000 đ, checkedTime rỗng | BR-10, ST-02 T1 | EC-103 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-113 | DC-Ticket.createTicket | giá trị biên | Seat A05; trip stub | ticketCode SV0000123, trip, seat A05, travelerInfo (A05, "Nguyễn Văn An", "0912345678"), price 1 đ, ONLINE | Vé ISSUED, price 1 đ | P12 F7 price > 0 | BV-41, EC-94 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-114 | DC-Ticket.createTicket | giá trị biên | Seat A05; trip stub | ticketCode SV0000123, trip, seat A05, travelerInfo (A05, "Nguyễn Văn An", "0912345678"), price 0 đ, ONLINE | Ném IllegalArgumentException; không có vé | P12 F2 tiền điều kiện | BV-40, EC-95 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-115 | DC-Ticket.createTicket | phân vùng tương đương | Seat A05; trip stub | ticketCode SV0000123, trip, seat A05, travelerInfo (A05, "", "0912345678"), price 360.000 đ, ONLINE | Ném IllegalArgumentException; không có vé | P12 F7 travelerName không rỗng | EC-97 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-116 | DC-Ticket.createTicket | phân vùng tương đương | Seat A05; trip stub | ticketCode SV0000123, trip, seat A05, travelerInfo (A05, "Nguyễn Văn An", ""), price 360.000 đ, ONLINE | Ném IllegalArgumentException; không có vé | ASM-15, P12 F7 | EC-100 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-117 | DC-Ticket.createTicket | phân vùng tương đương | Seat A05; trip stub | ticketCode SV0000123, trip, seat A05, travelerInfo (A05, "Nguyễn Văn An", "091234567" (9 chữ số)), price 360.000 đ, ONLINE | Ném IllegalArgumentException; không có vé | ASM-15, P12 F7 | EC-101 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-118 | DC-Ticket.createTicket | phân vùng tương đương | Seat A05; trip stub | ticketCode SV0000123, trip, seat A05, travelerInfo (A05, "   " (3 dấu cách), "0912345678"), price 360.000 đ, ONLINE | Chưa xác định: chờ Q-112 | P12 F7 | EC-98 | DC-Trip stub, DC-Seat fake, DC-PhoneNumber fake, DC-Money fake | Trung bình |
| TC-119 | DC-Ticket.isCancelled | phân vùng tương đương | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | - | Trả false; vé không đổi | UC-008 bước 2 | EC-105 | DC-Seat fake | Thấp |
| TC-120 | DC-Ticket.isCancelled | phân vùng tương đương | Ticket ISSUED, checkedTime = 20:15 03/02/2027 | - | Trả false | UC-008 bước 2, P12 F6.1 | EC-106 | DC-Seat fake | Thấp |
| TC-121 | DC-Ticket.isCancelled | phân vùng tương đương | Ticket CANCELLED (do cancelTicket) | - | Trả true | UC-008 2b, ASM-20 | EC-107 | DC-Seat fake | Thấp |
| TC-122 | DC-Ticket.cancelTicket | chuyển trạng thái; bảng quyết định; đường đi | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | refundRatePercent 90, refundAmount 324.000 đ, VIA_GATEWAY | Trả Refund(refundAmount 324.000 đ, refundRatePercent 90, refundMethod VIA_GATEWAY, refundOutcome REFUNDED); status CANCELLED; Seat A05 AVAILABLE | BR-15, ASM-20, ST-02 T3, UC-008 bước 10 | DT5-Q1, EC-108, EC-111, EC-113, EC-116; ST-02 T3; CE63, CE65 đến CE67, CE69, CE71 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-123 | DC-Ticket.cancelTicket | chuyển trạng thái; bảng quyết định; đường đi | Ticket ISSUED (SV0000124, A06, price 300.000 đ, COUNTER), Seat A06 SOLD | refundRatePercent 50, refundAmount 150.000 đ, CASH_AT_COUNTER | Trả Refund(refundAmount 150.000 đ, refundRatePercent 50, refundMethod CASH_AT_COUNTER, refundOutcome AWAITING_CASH_PAYOUT); status CANCELLED; Seat A06 AVAILABLE | BR-16, ASM-20, ASM-54, ST-02 T3 | DT5-Q2, EC-112; ST-02 T3; CE63, CE65, CE66, CE68, CE70, CE71 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-124 | DC-Ticket.cancelTicket | chuyển trạng thái | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD, đã markChecked(20:15 03/02/2027) | refundRatePercent 90, refundAmount 324.000 đ, VIA_GATEWAY | Trả Refund(refundAmount 324.000 đ, refundRatePercent 90, refundMethod VIA_GATEWAY, refundOutcome REFUNDED); status CANCELLED; Seat A05 AVAILABLE | ASM-104, ST-02 T5 | DT5-Q1, EC-109; ST-02 T5; CE63, CE65 đến CE67, CE69, CE71 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-125 | DC-Ticket.cancelTicket | giá trị biên | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | refundRatePercent 0, refundAmount 0 đ, VIA_GATEWAY | Trả Refund(refundAmount 0 đ, refundRatePercent 0, refundMethod VIA_GATEWAY, refundOutcome REFUNDED); status CANCELLED | P12 F7 DC-Refund | BV-42, BV-46; CE63, CE65 đến CE67, CE69, CE71 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-126 | DC-Ticket.cancelTicket | giá trị biên | Ticket ISSUED (SV0000124, A06, price 300.000 đ, COUNTER), Seat A06 SOLD | refundRatePercent 100, refundAmount 300.000 đ, CASH_AT_COUNTER | Trả Refund(refundAmount 300.000 đ, refundRatePercent 100, refundMethod CASH_AT_COUNTER, refundOutcome AWAITING_CASH_PAYOUT); status CANCELLED | P12 F7 DC-Refund | BV-43; CE63, CE65, CE66, CE68, CE70, CE71 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-127 | DC-Ticket.cancelTicket | chuyển trạng thái; bảng quyết định | Ticket CANCELLED (đã cancelTicket); Seat A05 AVAILABLE rồi được lần đặt khác giữ (HELD) | refundRatePercent 90, refundAmount 324.000 đ, VIA_GATEWAY | Ném InvalidStateException; status vẫn CANCELLED; Seat A05 vẫn HELD bởi lần đặt khác; không có Refund thứ hai | P12 F6.2, F2 tiền điều kiện | DT5-Q3, EC-110; P12 F6.2; CE63, CE64, CE72 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-128 | DC-Ticket.cancelTicket | giá trị biên | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | refundRatePercent -1, refundAmount 324.000 đ, VIA_GATEWAY | Chưa xác định: chờ Q-111. Ném IllegalArgumentException; trạng thái vé và Seat sau lỗi: chưa xác định (Q-111) | P12 F2 DC-Refund.createRefund | BV-44, EC-114 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-129 | DC-Ticket.cancelTicket | giá trị biên | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | refundRatePercent 101, refundAmount 324.000 đ, VIA_GATEWAY | Chưa xác định: chờ Q-111. Ném IllegalArgumentException; trạng thái vé và Seat sau lỗi: chưa xác định (Q-111) | P12 F2 DC-Refund.createRefund | BV-45, EC-115 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-130 | DC-Ticket.cancelTicket | giá trị biên | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | refundRatePercent 90, refundAmount -1 đ, VIA_GATEWAY | Chưa xác định: chờ Q-111. Ném IllegalArgumentException; trạng thái vé và Seat sau lỗi: chưa xác định (Q-111) | P12 F2 DC-Refund.createRefund | BV-47, EC-117 | DC-Seat fake, DC-Trip stub, DC-Money fake | Cao |
| TC-131 | DC-Ticket.cancelWithTrip | chuyển trạng thái | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | - | status CANCELLED; Seat A05 vẫn SOLD; vé chưa có Refund (getRefund() rỗng) | BR-19, ASM-26, ST-02 T4, UC-013 bước 5 | EC-119; ST-02 T4; CE73, CE75, CE76 | DC-Seat fake | Cao |
| TC-132 | DC-Ticket.cancelWithTrip | chuyển trạng thái | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD, đã markChecked(20:15 03/02/2027) | - | status CANCELLED; Seat A05 vẫn SOLD | ASM-104, ST-02 T6 | EC-120; ST-02 T6; CE73, CE75, CE76 | DC-Seat fake | Cao |
| TC-133 | DC-Ticket.cancelWithTrip | chuyển trạng thái | Ticket CANCELLED (do cancelWithTrip), Seat A05 SOLD | - | Ném InvalidStateException; status vẫn CANCELLED; Seat A05 vẫn SOLD | P12 F6.2, F2 tiền điều kiện | EC-121; P12 F6.2; CE73, CE74, CE77 | DC-Seat fake | Cao |
| TC-134 | DC-Ticket.recordRefund | bảng quyết định; đường đi | Ticket CANCELLED do cancelWithTrip (SV0000123, price 360.000 đ, ONLINE), chưa có Refund | refundRatePercent 100, refundAmount 360.000 đ, VIA_GATEWAY, REFUNDED | Trả Refund(refundAmount 360.000 đ, refundRatePercent 100, refundMethod VIA_GATEWAY, refundOutcome REFUNDED); status vẫn CANCELLED; getRefund() là Refund vừa trả | BR-17, UC-013 bước 9 | DT6-Q1, EC-122, EC-125, EC-127; CE78, CE80, CE82, CE83 | DC-Seat fake, DC-Money fake | Cao |
| TC-135 | DC-Ticket.recordRefund | phân vùng tương đương | Ticket CANCELLED do cancelWithTrip (SV0000123, price 360.000 đ, ONLINE), chưa có Refund | refundRatePercent 100, refundAmount 360.000 đ, VIA_GATEWAY, FAILED | Trả Refund(refundAmount 360.000 đ, refundRatePercent 100, refundMethod VIA_GATEWAY, refundOutcome FAILED) | UC-013 8a, ASM-31 | EC-128; CE78, CE80, CE82, CE83 | DC-Seat fake, DC-Money fake | Cao |
| TC-136 | DC-Ticket.recordRefund | phân vùng tương đương | Ticket CANCELLED do cancelWithTrip (SV0000124, price 300.000 đ, COUNTER), chưa có Refund | refundRatePercent 100, refundAmount 300.000 đ, CASH_AT_COUNTER, AWAITING_CASH_PAYOUT | Trả Refund(refundAmount 300.000 đ, refundRatePercent 100, refundMethod CASH_AT_COUNTER, refundOutcome AWAITING_CASH_PAYOUT) | BR-16, ASM-28, UC-013 bước 9 | EC-129; CE78, CE80, CE82, CE83 | DC-Seat fake, DC-Money fake | Cao |
| TC-137 | DC-Ticket.recordRefund | bảng quyết định | Ticket CANCELLED do cancelWithTrip (SV0000123, price 360.000 đ, ONLINE), chưa có Refund, đã recordRefund một lần (REFUNDED, 360.000 đ) | lần gọi thứ hai: 100, 360.000 đ, VIA_GATEWAY, REFUNDED | Ném InvalidStateException; Refund đầu tiên không đổi (360.000 đ, REFUNDED) | P12 F2 tiền điều kiện | DT6-Q2, EC-126; CE78, CE80, CE81, CE84 | DC-Seat fake, DC-Money fake | Cao |
| TC-138 | DC-Ticket.recordRefund | bảng quyết định | Ticket CANCELLED do cancelTicket (đã có Refund 324.000 đ, 90, VIA_GATEWAY, REFUNDED) | 100, 360.000 đ, VIA_GATEWAY, REFUNDED | Ném InvalidStateException; Refund hiện có không đổi | P12 F2 tiền điều kiện, UC-008 bước 10 | DT6-Q2, EC-126; CE78, CE80, CE81, CE84 | DC-Seat fake, DC-Money fake | Cao |
| TC-139 | DC-Ticket.recordRefund | bảng quyết định | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | 100, 360.000 đ, VIA_GATEWAY, REFUNDED | Ném InvalidStateException; status vẫn ISSUED; không có Refund | P12 F2 tiền điều kiện | DT6-Q3, EC-123; CE78, CE79, CE84 | DC-Seat fake, DC-Money fake | Cao |
| TC-140 | DC-Ticket.recordRefund | bảng quyết định | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD, đã markChecked(20:15 03/02/2027) | 100, 360.000 đ, VIA_GATEWAY, REFUNDED | Ném InvalidStateException; status vẫn ISSUED, checkedTime vẫn 20:15 03/02/2027; không có Refund | P12 F2 tiền điều kiện | DT6-Q3, EC-124; CE78, CE79, CE84 | DC-Seat fake, DC-Money fake | Cao |
| TC-141 | DC-Ticket.recordRefund | phân vùng tương đương | Ticket CANCELLED do cancelWithTrip (SV0000123, price 360.000 đ, ONLINE), chưa có Refund | 100, 360.000 đ, VIA_GATEWAY, AWAITING_CASH_PAYOUT | Chưa xác định: chờ Q-113 | P12 F2 | EC-130 | DC-Seat fake, DC-Money fake | Cao |
| TC-142 | DC-Ticket.recordRefund | phân vùng tương đương | Ticket CANCELLED do cancelWithTrip (SV0000123, price 360.000 đ, ONLINE), chưa có Refund | refundRatePercent 101, 360.000 đ, VIA_GATEWAY, REFUNDED | Chưa xác định: chờ Q-111. Ném IllegalArgumentException; trạng thái vé sau lỗi: chưa xác định (Q-111) | P12 F2 DC-Refund.createRefund | EC-131 | DC-Seat fake, DC-Money fake | Cao |
| TC-143 | DC-Ticket.determineCheckResult | phân vùng tương đương; bảng quyết định | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | - | TicketCheckResult(outcome VALID, ticketCode SV0000123, seatCode A05, travelerName "Nguyễn Văn An", previousCheckedTime rỗng); gọi lần hai vẫn VALID (vé không bị ghi checkedTime) | UC-015 bước 5, 7; P12 F2 hậu điều kiện không đổi | DT7-Q3, EC-133; CE85, CE87, CE89, CE92 | DC-Seat fake, DC-Trip stub | Cao |
| TC-144 | DC-Ticket.determineCheckResult | phân vùng tương đương; bảng quyết định | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD, đã markChecked(20:15:00 03/02/2027) | - | TicketCheckResult(outcome ALREADY_CHECKED, ticketCode SV0000123, seatCode A05, previousCheckedTime 20:15:00 03/02/2027, travelerName rỗng) | BR-22, UC-015 5c | DT7-Q2, EC-134; CE85, CE87, CE88, CE91 | DC-Seat fake, DC-Trip stub | Cao |
| TC-145 | DC-Ticket.determineCheckResult | phân vùng tương đương; bảng quyết định | Ticket CANCELLED do cancelWithTrip, chưa soát (SV0000123, A05) | - | TicketCheckResult(outcome CANCELLED_TICKET, ticketCode SV0000123, seatCode A05, travelerName rỗng, previousCheckedTime rỗng) | BR-21, UC-015 5b | DT7-Q1, EC-135; CE85, CE86, CE90 | DC-Seat fake, DC-Trip stub | Cao |
| TC-146 | DC-Ticket.determineCheckResult | bảng quyết định | Ticket đã markChecked(20:15:00 03/02/2027) rồi cancelTicket (CANCELLED, checkedTime còn giá trị) | - | TicketCheckResult(outcome CANCELLED_TICKET, ticketCode SV0000123, seatCode A05, previousCheckedTime rỗng) | BR-21, UC-015 5b và 5c | DT7-Q1, EC-136; CE85, CE86, CE90 | DC-Seat fake, DC-Trip stub | Cao |
| TC-147 | DC-Ticket.markChecked | chuyển trạng thái; bảng quyết định | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD | checkTime = 20:15:00 03/02/2027 | checkedTime = 20:15:00 03/02/2027; status vẫn ISSUED; determineCheckResult() sau đó trả ALREADY_CHECKED với previousCheckedTime 20:15:00 03/02/2027 | ASM-35, ST-02 T2, UC-015 bước 6 | DT8-Q1, EC-137; ST-02 T2; CE93, CE95, CE97, CE98 | DC-Seat fake | Cao |
| TC-148 | DC-Ticket.markChecked | chuyển trạng thái; bảng quyết định | Ticket ISSUED (SV0000123, trip stub, Seat A05, "Nguyễn Văn An", 0912345678, price 360.000 đ, ONLINE), Seat A05 SOLD, đã markChecked(20:15:00 03/02/2027) | checkTime = 20:30:00 03/02/2027 | Ném InvalidStateException; checkedTime vẫn 20:15:00 03/02/2027 | BR-22, P12 F6.2 | DT8-Q2, EC-138; P12 F6.2; CE93, CE95, CE96, CE99 | DC-Seat fake | Cao |
| TC-149 | DC-Ticket.markChecked | chuyển trạng thái; bảng quyết định | Ticket CANCELLED do cancelWithTrip, chưa soát | checkTime = 20:15:00 03/02/2027 | Ném InvalidStateException; checkedTime vẫn rỗng; status vẫn CANCELLED | P12 F6.2 | DT8-Q3, EC-139; P12 F6.2; CE93, CE94, CE99 | DC-Seat fake | Cao |
| TC-150 | DC-Ticket.markChecked | bảng quyết định | Ticket đã markChecked(20:15:00 03/02/2027) rồi cancelWithTrip (CANCELLED, checkedTime 20:15:00 03/02/2027) | checkTime = 20:30:00 03/02/2027 | Ném InvalidStateException; checkedTime vẫn 20:15:00 03/02/2027; status vẫn CANCELLED | P12 F6.2 | DT8-Q4, EC-140; P12 F6.2; CE93, CE94, CE99 | DC-Seat fake | Cao |

## F4. Ma trận phủ

Mục EC, BV, DT-Q, chuyển trạng thái, nhánh CE theo từng operation:

| Mục cần phủ (EC / BV / DT-Q / chuyển trạng thái / nhánh CE / BR / luồng thay thế P04) | TC phủ | Đạt (Có / Không: lý do) |
|---|---|---|
| DC-TicketReturnPolicy.matchesPurchaseChannel EC-01 | TC-001 | Có |
| DC-TicketReturnPolicy.matchesPurchaseChannel EC-02 | TC-002 | Có |
| DC-TicketReturnPolicy.matchesPurchaseChannel EC-03 | TC-003 | Có |
| DC-TicketReturnPolicy.matchesPurchaseChannel EC-04 | TC-004 | Có |
| DC-TicketReturnPolicy.matchesPurchaseChannel EC-05 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-TicketReturnPolicy.matchesPurchaseChannel DT1-Q1 | TC-001 | Có |
| DC-TicketReturnPolicy.matchesPurchaseChannel DT1-Q2 | TC-002 | Có |
| DC-TicketReturnPolicy.matchesPurchaseChannel DT1-Q3 | TC-003 | Có |
| DC-TicketReturnPolicy.matchesPurchaseChannel DT1-Q4 | TC-004 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed EC-06 | TC-005, TC-006 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed EC-07 | TC-007 đến TC-009 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed EC-08 | TC-010 đến TC-012 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed EC-09 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-TicketReturnPolicy.isReturnTimeAllowed BV-01 | TC-006 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed BV-02 | TC-007 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed BV-03 | TC-009 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed BV-04 | TC-010 | Có |
| DC-TicketReturnPolicy.isReturnTimeAllowed BV-05 | TC-011 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount EC-10 | TC-013, TC-014 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount EC-11 | TC-015 đến TC-018, TC-022 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount EC-12 | TC-019 đến TC-021, TC-023 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount EC-13 | TC-015, TC-019 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount EC-14 | TC-022, TC-023 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount EC-15 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-TicketReturnPolicy.calculateRefundAmount BV-06 | TC-014 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount BV-07 | TC-015 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount BV-08 | TC-016 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount BV-09 | TC-018 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount BV-10 | TC-019 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount BV-11 | TC-020 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount DT2-Q1 | TC-019, TC-021 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount DT2-Q2 | TC-015, TC-017 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount DT2-Q3 | - | Không: quy tắc N/A (không thể xảy ra) |
| DC-TicketReturnPolicy.calculateRefundAmount DT2-Q4 | TC-013 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE1 | TC-013 đến TC-023 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE2 | TC-013, TC-014 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE3 | TC-015 đến TC-023 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE4 | TC-019 đến TC-021, TC-023 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE5 | TC-015 đến TC-018, TC-022 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE6 | TC-019 đến TC-021, TC-023 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE7 | TC-015 đến TC-018, TC-022 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE8 | TC-015 đến TC-023 | Có |
| DC-TicketReturnPolicy.calculateRefundAmount nhánh CE9 | TC-013, TC-014 | Có |
| DC-TicketReturnPolicy.getTicketReturnInfo EC-16 | TC-024 | Có |
| DC-TicketReturnPolicy.getTicketReturnInfo EC-17 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-TicketReturnPolicy.determineRefundMethod EC-18 | TC-025 | Có |
| DC-TicketReturnPolicy.determineRefundMethod EC-19 | TC-026 | Có |
| DC-TicketReturnPolicy.determineRefundMethod EC-20 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-TicketReturnPolicy.getCancelImpactInfo EC-21 | TC-027 | Có |
| DC-TicketReturnPolicy.getCancelImpactInfo EC-22 | TC-028 | Có |
| DC-TicketReturnPolicy.getCancelImpactInfo EC-23 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-TicketReturnPolicy.calculateTripCancelRefundAmount EC-24 | TC-029, TC-031 | Có |
| DC-TicketReturnPolicy.calculateTripCancelRefundAmount EC-25 | TC-030 | Có |
| DC-TicketReturnPolicy.calculateTripCancelRefundAmount EC-26 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-TicketReturnPolicy.calculateTripCancelRefundAmount BV-12 | TC-031 | Có |
| DC-Booking.createBooking EC-27 | TC-033, TC-034 | Có |
| DC-Booking.createBooking EC-28 | TC-035 | Có |
| DC-Booking.createBooking EC-29 | TC-032 | Có |
| DC-Booking.createBooking EC-30 | TC-036 | Không: chờ Q-114 (kết quả mong đợi chưa xác định) |
| DC-Booking.createBooking EC-31 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Booking.createBooking BV-13 | TC-032 | Có |
| DC-Booking.createBooking BV-14 | TC-033 | Có |
| DC-Booking.createBooking BV-15 | TC-034 | Có |
| DC-Booking.createBooking BV-16 | TC-035 | Có |
| DC-Booking.createBooking chuyển trạng thái (initial) --createBooking(bookingId, trip, travelerInfos)--> Draft (ST-01 T1) | TC-033 | Có |
| DC-Booking.isWithinSeatLimit EC-32 | TC-037 đến TC-039 | Có |
| DC-Booking.isWithinSeatLimit EC-33 | TC-040 | Có |
| DC-Booking.isWithinSeatLimit EC-34 | - | Không: không thể xảy ra (createBooking chặn danh sách rỗng (P12 F2)) |
| DC-Booking.isWithinSeatLimit BV-17 | TC-037 | Có |
| DC-Booking.isWithinSeatLimit BV-18 | TC-039 | Có |
| DC-Booking.isWithinSeatLimit BV-19 | TC-040 | Có |
| DC-Booking.validateTravelerInfo EC-35 | TC-041 đến TC-044 | Có |
| DC-Booking.validateTravelerInfo EC-36 | TC-045, TC-054 | Có |
| DC-Booking.validateTravelerInfo EC-37 | TC-046 | Có |
| DC-Booking.validateTravelerInfo EC-38 | TC-041 đến TC-044 | Có |
| DC-Booking.validateTravelerInfo EC-39 | TC-047 | Có |
| DC-Booking.validateTravelerInfo EC-40 | TC-048, TC-055, TC-056 | Có |
| DC-Booking.validateTravelerInfo EC-41 | TC-049 | Có |
| DC-Booking.validateTravelerInfo EC-42 | TC-050 | Có |
| DC-Booking.validateTravelerInfo EC-43 | TC-051 | Có |
| DC-Booking.validateTravelerInfo EC-44 | TC-041 | Có |
| DC-Booking.validateTravelerInfo EC-45 | - | Không: không thể xảy ra tại đây (0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3)) |
| DC-Booking.validateTravelerInfo BV-20 | TC-045 | Có |
| DC-Booking.validateTravelerInfo BV-21 | TC-041 | Có |
| DC-Booking.validateTravelerInfo BV-22 | TC-048 | Có |
| DC-Booking.validateTravelerInfo BV-23 | TC-041 | Có |
| DC-Booking.validateTravelerInfo BV-24 | TC-049 | Có |
| DC-Booking.validateTravelerInfo DT3-Q1 | TC-045 đến TC-047, TC-052 đến TC-054 | Có |
| DC-Booking.validateTravelerInfo DT3-Q2 | TC-048 đến TC-051, TC-055, TC-056 | Có |
| DC-Booking.validateTravelerInfo DT3-Q3 | TC-041 đến TC-044 | Có |
| DC-Booking.validateTravelerInfo nhánh CE10 | TC-041 đến TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE11 | TC-041 đến TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE12 | TC-045, TC-046, TC-052, TC-054 | Có |
| DC-Booking.validateTravelerInfo nhánh CE13 | TC-041 đến TC-044, TC-047 đến TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE14 | TC-047, TC-053 | Có |
| DC-Booking.validateTravelerInfo nhánh CE15 | TC-041 đến TC-044, TC-048 đến TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE16 | TC-041 đến TC-044, TC-048 đến TC-051, TC-055, TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE17 | TC-041 đến TC-044, TC-048 đến TC-051, TC-055, TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE18 | TC-048 đến TC-051, TC-055, TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE19 | TC-041 đến TC-044, TC-055 | Có |
| DC-Booking.validateTravelerInfo nhánh CE20 | TC-041 đến TC-044 | Có |
| DC-Booking.validateTravelerInfo nhánh CE21 | TC-045 đến TC-047, TC-052 đến TC-054 | Có |
| DC-Booking.validateTravelerInfo nhánh CE22 | TC-048 đến TC-051, TC-055, TC-056 | Có |
| DC-Booking.validateTravelerInfo nhánh CE23 | TC-041 đến TC-044 | Có |
| DC-Booking.calculateTotal EC-46 | TC-057, TC-058 | Có |
| DC-Booking.calculateTotal EC-47 | TC-060 | Có |
| DC-Booking.calculateTotal EC-48 | TC-061 | Có |
| DC-Booking.calculateTotal EC-49 | TC-062 | Có |
| DC-Booking.calculateTotal EC-50 | TC-057 đến TC-059 | Có |
| DC-Booking.calculateTotal EC-51 | - | Không: không thể xảy ra tại đây (0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3)) |
| DC-Booking.calculateTotal BV-25 | TC-057 | Có |
| DC-Booking.calculateTotal BV-26 | TC-059 | Có |
| DC-Booking.calculateTotal nhánh CE24 | TC-057 đến TC-062 | Có |
| DC-Booking.calculateTotal nhánh CE25 | TC-060 đến TC-062 | Có |
| DC-Booking.calculateTotal nhánh CE26 | TC-057 đến TC-059 | Có |
| DC-Booking.calculateTotal nhánh CE27 | TC-057 đến TC-059 | Có |
| DC-Booking.calculateTotal nhánh CE28 | TC-057 đến TC-059 | Có |
| DC-Booking.calculateTotal nhánh CE29 | TC-060 đến TC-062 | Có |
| DC-Booking.holdSeats EC-52 | TC-063 | Có |
| DC-Booking.holdSeats EC-53 | TC-067 | Có |
| DC-Booking.holdSeats EC-54 | TC-068 | Có |
| DC-Booking.holdSeats EC-55 | TC-069 | Có |
| DC-Booking.holdSeats EC-56 | TC-063, TC-064 | Có |
| DC-Booking.holdSeats EC-57 | TC-070, TC-072 | Có |
| DC-Booking.holdSeats EC-58 | TC-071 | Có |
| DC-Booking.holdSeats EC-59 | TC-063, TC-066 | Có |
| DC-Booking.holdSeats EC-60 | - | Không: không thể xảy ra tại đây (0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3)) |
| DC-Booking.holdSeats EC-61 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Booking.holdSeats BV-27 | TC-063 | Có |
| DC-Booking.holdSeats BV-28 | TC-066 | Có |
| DC-Booking.holdSeats DT4-Q1 | TC-063 đến TC-066 | Có |
| DC-Booking.holdSeats DT4-Q2 | TC-070 đến TC-072 | Có |
| DC-Booking.holdSeats DT4-Q3 | TC-069 | Có |
| DC-Booking.holdSeats DT4-Q4 | TC-067, TC-068 | Có |
| DC-Booking.holdSeats chuyển trạng thái Draft --holdSeats(now)--> Held (ST-01 T2) | TC-063, TC-064 | Có |
| DC-Booking.holdSeats chuyển trạng thái Draft --holdSeats(now)--> Draft (ST-01 T2 guard) | TC-070 đến TC-072 | Có |
| DC-Booking.holdSeats chuyển trạng thái Held --holdSeats(now)--> Held (P12 F6.2 sự kiện bị từ chối) | TC-067 | Có |
| DC-Booking.holdSeats chuyển trạng thái Ticketed --holdSeats(now)--> Ticketed (P12 F6.2) | TC-068 | Có |
| DC-Booking.holdSeats chuyển trạng thái Expired --holdSeats(now)--> Expired (P12 F6.2) | TC-069 | Có |
| DC-Booking.holdSeats nhánh CE30 | TC-063 đến TC-072 | Có |
| DC-Booking.holdSeats nhánh CE31 | TC-067 đến TC-069 | Có |
| DC-Booking.holdSeats nhánh CE32 | TC-063 đến TC-066, TC-070 đến TC-072 | Có |
| DC-Booking.holdSeats nhánh CE33 | TC-063 đến TC-066, TC-070 đến TC-072 | Có |
| DC-Booking.holdSeats nhánh CE34 | TC-063 đến TC-066, TC-070 đến TC-072 | Có |
| DC-Booking.holdSeats nhánh CE35 | TC-063 đến TC-066 | Có |
| DC-Booking.holdSeats nhánh CE36 | TC-070 đến TC-072 | Có |
| DC-Booking.holdSeats nhánh CE37 | TC-063 đến TC-066, TC-071, TC-072 | Có |
| DC-Booking.holdSeats nhánh CE38 | TC-063 đến TC-066, TC-071, TC-072 | Có |
| DC-Booking.holdSeats nhánh CE39 | TC-063 đến TC-066 | Có |
| DC-Booking.holdSeats nhánh CE40 | TC-067 đến TC-069 | Có |
| DC-Booking.holdSeats nhánh CE41 | TC-070 đến TC-072 | Có |
| DC-Booking.releaseSeats EC-62 | TC-074 đến TC-077 | Có |
| DC-Booking.releaseSeats EC-63 | TC-078 | Có |
| DC-Booking.releaseSeats EC-64 | TC-079 | Có |
| DC-Booking.releaseSeats EC-65 | TC-080 | Có |
| DC-Booking.releaseSeats EC-66 | TC-074 | Có |
| DC-Booking.releaseSeats EC-67 | - | Không: không thể xảy ra tại đây (0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3)) |
| DC-Booking.releaseSeats BV-29 | TC-074 | Có |
| DC-Booking.releaseSeats BV-30 | TC-077 | Có |
| DC-Booking.releaseSeats chuyển trạng thái Held --releaseSeats()--> Expired (ST-01 T4) | TC-074 đến TC-077 | Có |
| DC-Booking.releaseSeats chuyển trạng thái Draft --releaseSeats()--> Draft (P12 F6.2) | TC-078 | Có |
| DC-Booking.releaseSeats chuyển trạng thái Ticketed --releaseSeats()--> Ticketed (P12 F6.2) | TC-079 | Có |
| DC-Booking.releaseSeats chuyển trạng thái Expired --releaseSeats()--> Expired (P12 F6.2) | TC-080 | Có |
| DC-Booking.releaseSeats nhánh CE42 | TC-074 đến TC-080 | Có |
| DC-Booking.releaseSeats nhánh CE43 | TC-078 đến TC-080 | Có |
| DC-Booking.releaseSeats nhánh CE44 | TC-074 đến TC-077 | Có |
| DC-Booking.releaseSeats nhánh CE45 | TC-074 đến TC-077 | Có |
| DC-Booking.releaseSeats nhánh CE46 | TC-074 đến TC-077 | Có |
| DC-Booking.releaseSeats nhánh CE47 | TC-074 đến TC-077 | Có |
| DC-Booking.releaseSeats nhánh CE48 | TC-074 đến TC-077 | Có |
| DC-Booking.releaseSeats nhánh CE49 | TC-078 đến TC-080 | Có |
| DC-Booking.issueTickets EC-68 | TC-081 đến TC-083, TC-085, TC-086 | Có |
| DC-Booking.issueTickets EC-69 | TC-087 | Có |
| DC-Booking.issueTickets EC-70 | TC-088 | Có |
| DC-Booking.issueTickets EC-71 | TC-089 | Có |
| DC-Booking.issueTickets EC-72 | TC-081, TC-084 | Có |
| DC-Booking.issueTickets EC-73 | - | Không: không thể xảy ra tại đây (0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3)) |
| DC-Booking.issueTickets EC-74 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Booking.issueTickets BV-31 | TC-081 | Có |
| DC-Booking.issueTickets BV-32 | TC-084 | Có |
| DC-Booking.issueTickets chuyển trạng thái Held --issueTickets(paymentReference, idGenerator)--> Ticketed (ST-01 T3) | TC-081 đến TC-084 | Có |
| DC-Booking.issueTickets chuyển trạng thái Draft --issueTickets(...)--> Draft (P12 F6.2) | TC-087 | Có |
| DC-Booking.issueTickets chuyển trạng thái Ticketed --issueTickets(...)--> Ticketed (P12 F6.2) | TC-088 | Có |
| DC-Booking.issueTickets chuyển trạng thái Expired --issueTickets(...)--> Expired (P12 F6.2) | TC-089 | Có |
| DC-Booking.issueTickets nhánh CE50 | TC-081 đến TC-089 | Có |
| DC-Booking.issueTickets nhánh CE51 | TC-087 đến TC-089 | Có |
| DC-Booking.issueTickets nhánh CE52 | TC-081 đến TC-086 | Có |
| DC-Booking.issueTickets nhánh CE53 | TC-081 đến TC-086 | Có |
| DC-Booking.issueTickets nhánh CE54 | TC-081 đến TC-086 | Có |
| DC-Booking.issueTickets nhánh CE55 | TC-081 đến TC-086 | Có |
| DC-Booking.issueTickets nhánh CE56 | TC-081 đến TC-086 | Có |
| DC-Booking.issueTickets nhánh CE57 | TC-087 đến TC-089 | Có |
| DC-Booking.getBookingSummary EC-75 | TC-090, TC-091 | Có |
| DC-Booking.getBookingSummary EC-76 | TC-093 | Có |
| DC-Booking.getBookingSummary EC-77 | TC-094 | Có |
| DC-Booking.getBookingSummary EC-78 | TC-095 | Có |
| DC-Booking.getBookingSummary EC-79 | TC-090 đến TC-092 | Có |
| DC-Booking.getBookingSummary EC-80 | - | Không: không thể xảy ra tại đây (0 bị createBooking chặn; >= 6 bị isWithinSeatLimit chặn trước (P12 F3 submitBooking bước 3)) |
| DC-Booking.getBookingSummary BV-33 | TC-090 | Có |
| DC-Booking.getBookingSummary BV-34 | TC-092 | Có |
| DC-Booking.getHoldExpiryTime EC-81 | TC-096 | Có |
| DC-Booking.getHoldExpiryTime EC-82 | TC-097 | Có |
| DC-Booking.getHoldExpiryTime EC-83 | TC-098 | Có |
| DC-Booking.getHoldExpiryTime BV-35 | TC-097 | Có |
| DC-Booking.isHoldExpired EC-84 | TC-099 đến TC-101 | Có |
| DC-Booking.isHoldExpired EC-85 | TC-102 đến TC-104 | Có |
| DC-Booking.isHoldExpired EC-86 | TC-105 | Có |
| DC-Booking.isHoldExpired EC-87 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Booking.isHoldExpired BV-36 | TC-099 | Có |
| DC-Booking.isHoldExpired BV-37 | TC-101 | Có |
| DC-Booking.isHoldExpired BV-38 | TC-102 | Có |
| DC-Booking.isHoldExpired BV-39 | TC-103 | Có |
| DC-Booking.startPaymentAttempt EC-88 | TC-106, TC-107 | Có |
| DC-Booking.startPaymentAttempt EC-89 | TC-108 | Có |
| DC-Booking.startPaymentAttempt EC-90 | TC-109 | Có |
| DC-Booking.startPaymentAttempt EC-91 | TC-110 | Có |
| DC-Booking.startPaymentAttempt EC-92 | TC-106 | Có |
| DC-Booking.startPaymentAttempt EC-93 | TC-107 | Có |
| DC-Booking.startPaymentAttempt nhánh CE58 | TC-106 đến TC-110 | Có |
| DC-Booking.startPaymentAttempt nhánh CE59 | TC-108 đến TC-110 | Có |
| DC-Booking.startPaymentAttempt nhánh CE60 | TC-106, TC-107 | Có |
| DC-Booking.startPaymentAttempt nhánh CE61 | TC-106, TC-107 | Có |
| DC-Booking.startPaymentAttempt nhánh CE62 | TC-108 đến TC-110 | Có |
| DC-Ticket.createTicket EC-94 | TC-111, TC-113 | Có |
| DC-Ticket.createTicket EC-95 | TC-114 | Có |
| DC-Ticket.createTicket EC-96 | TC-111 | Có |
| DC-Ticket.createTicket EC-97 | TC-115 | Có |
| DC-Ticket.createTicket EC-98 | TC-118 | Không: chờ Q-112 (kết quả mong đợi chưa xác định) |
| DC-Ticket.createTicket EC-99 | TC-111 | Có |
| DC-Ticket.createTicket EC-100 | TC-116 | Có |
| DC-Ticket.createTicket EC-101 | TC-117 | Có |
| DC-Ticket.createTicket EC-102 | TC-111 | Có |
| DC-Ticket.createTicket EC-103 | TC-112 | Có |
| DC-Ticket.createTicket EC-104 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Ticket.createTicket BV-40 | TC-114 | Có |
| DC-Ticket.createTicket BV-41 | TC-113 | Có |
| DC-Ticket.createTicket chuyển trạng thái (initial) --createTicket(...)--> Issued (ST-02 T1) | TC-111 | Có |
| DC-Ticket.isCancelled EC-105 | TC-119 | Có |
| DC-Ticket.isCancelled EC-106 | TC-120 | Có |
| DC-Ticket.isCancelled EC-107 | TC-121 | Có |
| DC-Ticket.cancelTicket EC-108 | TC-122 | Có |
| DC-Ticket.cancelTicket EC-109 | TC-124 | Có |
| DC-Ticket.cancelTicket EC-110 | TC-127 | Có |
| DC-Ticket.cancelTicket EC-111 | TC-122 | Có |
| DC-Ticket.cancelTicket EC-112 | TC-123 | Có |
| DC-Ticket.cancelTicket EC-113 | TC-122 | Có |
| DC-Ticket.cancelTicket EC-114 | TC-128 | Không: chờ Q-111 (kết quả mong đợi chưa xác định) |
| DC-Ticket.cancelTicket EC-115 | TC-129 | Không: chờ Q-111 (kết quả mong đợi chưa xác định) |
| DC-Ticket.cancelTicket EC-116 | TC-122 | Có |
| DC-Ticket.cancelTicket EC-117 | TC-130 | Không: chờ Q-111 (kết quả mong đợi chưa xác định) |
| DC-Ticket.cancelTicket EC-118 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Ticket.cancelTicket BV-42 | TC-125 | Có |
| DC-Ticket.cancelTicket BV-43 | TC-126 | Có |
| DC-Ticket.cancelTicket BV-44 | TC-128 | Không: chờ Q-111 (kết quả mong đợi chưa xác định) |
| DC-Ticket.cancelTicket BV-45 | TC-129 | Không: chờ Q-111 (kết quả mong đợi chưa xác định) |
| DC-Ticket.cancelTicket BV-46 | TC-125 | Có |
| DC-Ticket.cancelTicket BV-47 | TC-130 | Không: chờ Q-111 (kết quả mong đợi chưa xác định) |
| DC-Ticket.cancelTicket DT5-Q1 | TC-122, TC-124 | Có |
| DC-Ticket.cancelTicket DT5-Q2 | TC-123 | Có |
| DC-Ticket.cancelTicket DT5-Q3 | TC-127 | Có |
| DC-Ticket.cancelTicket chuyển trạng thái Issued --cancelTicket(rate, amount, method)--> Cancelled (ST-02 T3) | TC-122, TC-123 | Có |
| DC-Ticket.cancelTicket chuyển trạng thái Checked --cancelTicket(rate, amount, method)--> Cancelled (ST-02 T5; ASM-104) | TC-124 | Có |
| DC-Ticket.cancelTicket chuyển trạng thái Cancelled --cancelTicket(rate, amount, method)--> Cancelled (P12 F6.2) | TC-127 | Có |
| DC-Ticket.cancelTicket nhánh CE63 | TC-122 đến TC-127 | Có |
| DC-Ticket.cancelTicket nhánh CE64 | TC-127 | Có |
| DC-Ticket.cancelTicket nhánh CE65 | TC-122 đến TC-126 | Có |
| DC-Ticket.cancelTicket nhánh CE66 | TC-122 đến TC-126 | Có |
| DC-Ticket.cancelTicket nhánh CE67 | TC-122, TC-124, TC-125 | Có |
| DC-Ticket.cancelTicket nhánh CE68 | TC-123, TC-126 | Có |
| DC-Ticket.cancelTicket nhánh CE69 | TC-122, TC-124, TC-125 | Có |
| DC-Ticket.cancelTicket nhánh CE70 | TC-123, TC-126 | Có |
| DC-Ticket.cancelTicket nhánh CE71 | TC-122 đến TC-126 | Có |
| DC-Ticket.cancelTicket nhánh CE72 | TC-127 | Có |
| DC-Ticket.cancelWithTrip EC-119 | TC-131 | Có |
| DC-Ticket.cancelWithTrip EC-120 | TC-132 | Có |
| DC-Ticket.cancelWithTrip EC-121 | TC-133 | Có |
| DC-Ticket.cancelWithTrip chuyển trạng thái Issued --cancelWithTrip()--> Cancelled (ST-02 T4) | TC-131 | Có |
| DC-Ticket.cancelWithTrip chuyển trạng thái Checked --cancelWithTrip()--> Cancelled (ST-02 T6; ASM-104) | TC-132 | Có |
| DC-Ticket.cancelWithTrip chuyển trạng thái Cancelled --cancelWithTrip()--> Cancelled (P12 F6.2) | TC-133 | Có |
| DC-Ticket.cancelWithTrip nhánh CE73 | TC-131 đến TC-133 | Có |
| DC-Ticket.cancelWithTrip nhánh CE74 | TC-133 | Có |
| DC-Ticket.cancelWithTrip nhánh CE75 | TC-131, TC-132 | Có |
| DC-Ticket.cancelWithTrip nhánh CE76 | TC-131, TC-132 | Có |
| DC-Ticket.cancelWithTrip nhánh CE77 | TC-133 | Có |
| DC-Ticket.recordRefund EC-122 | TC-134 | Có |
| DC-Ticket.recordRefund EC-123 | TC-139 | Có |
| DC-Ticket.recordRefund EC-124 | TC-140 | Có |
| DC-Ticket.recordRefund EC-125 | TC-134 | Có |
| DC-Ticket.recordRefund EC-126 | TC-137, TC-138 | Có |
| DC-Ticket.recordRefund EC-127 | TC-134 | Có |
| DC-Ticket.recordRefund EC-128 | TC-135 | Có |
| DC-Ticket.recordRefund EC-129 | TC-136 | Có |
| DC-Ticket.recordRefund EC-130 | TC-141 | Không: chờ Q-113 (kết quả mong đợi chưa xác định) |
| DC-Ticket.recordRefund EC-131 | TC-142 | Không: chờ Q-111 (kết quả mong đợi chưa xác định) |
| DC-Ticket.recordRefund EC-132 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Ticket.recordRefund DT6-Q1 | TC-134 | Có |
| DC-Ticket.recordRefund DT6-Q2 | TC-137, TC-138 | Có |
| DC-Ticket.recordRefund DT6-Q3 | TC-139, TC-140 | Có |
| DC-Ticket.recordRefund DT6-Q4 | - | Không: quy tắc N/A (không thể xảy ra) |
| DC-Ticket.recordRefund nhánh CE78 | TC-134 đến TC-140 | Có |
| DC-Ticket.recordRefund nhánh CE79 | TC-139, TC-140 | Có |
| DC-Ticket.recordRefund nhánh CE80 | TC-134 đến TC-138 | Có |
| DC-Ticket.recordRefund nhánh CE81 | TC-137, TC-138 | Có |
| DC-Ticket.recordRefund nhánh CE82 | TC-134 đến TC-136 | Có |
| DC-Ticket.recordRefund nhánh CE83 | TC-134 đến TC-136 | Có |
| DC-Ticket.recordRefund nhánh CE84 | TC-137 đến TC-140 | Có |
| DC-Ticket.determineCheckResult EC-133 | TC-143 | Có |
| DC-Ticket.determineCheckResult EC-134 | TC-144 | Có |
| DC-Ticket.determineCheckResult EC-135 | TC-145 | Có |
| DC-Ticket.determineCheckResult EC-136 | TC-146 | Có |
| DC-Ticket.determineCheckResult DT7-Q1 | TC-145, TC-146 | Có |
| DC-Ticket.determineCheckResult DT7-Q2 | TC-144 | Có |
| DC-Ticket.determineCheckResult DT7-Q3 | TC-143 | Có |
| DC-Ticket.determineCheckResult nhánh CE85 | TC-143 đến TC-146 | Có |
| DC-Ticket.determineCheckResult nhánh CE86 | TC-145, TC-146 | Có |
| DC-Ticket.determineCheckResult nhánh CE87 | TC-143, TC-144 | Có |
| DC-Ticket.determineCheckResult nhánh CE88 | TC-144 | Có |
| DC-Ticket.determineCheckResult nhánh CE89 | TC-143 | Có |
| DC-Ticket.determineCheckResult nhánh CE90 | TC-145, TC-146 | Có |
| DC-Ticket.determineCheckResult nhánh CE91 | TC-144 | Có |
| DC-Ticket.determineCheckResult nhánh CE92 | TC-143 | Có |
| DC-Ticket.markChecked EC-137 | TC-147 | Có |
| DC-Ticket.markChecked EC-138 | TC-148 | Có |
| DC-Ticket.markChecked EC-139 | TC-149 | Có |
| DC-Ticket.markChecked EC-140 | TC-150 | Có |
| DC-Ticket.markChecked EC-141 | - | Không: ASM-111 (tham số null nằm ngoài hợp đồng, không kiểm thử) |
| DC-Ticket.markChecked DT8-Q1 | TC-147 | Có |
| DC-Ticket.markChecked DT8-Q2 | TC-148 | Có |
| DC-Ticket.markChecked DT8-Q3 | TC-149 | Có |
| DC-Ticket.markChecked DT8-Q4 | TC-150 | Có |
| DC-Ticket.markChecked chuyển trạng thái Issued --markChecked(checkTime)--> Checked (ST-02 T2) | TC-147 | Có |
| DC-Ticket.markChecked chuyển trạng thái Checked --markChecked(checkTime)--> Checked (P12 F6.2) | TC-148 | Có |
| DC-Ticket.markChecked chuyển trạng thái Cancelled --markChecked(checkTime)--> Cancelled (P12 F6.2) | TC-149, TC-150 | Có |
| DC-Ticket.markChecked nhánh CE93 | TC-147 đến TC-150 | Có |
| DC-Ticket.markChecked nhánh CE94 | TC-149, TC-150 | Có |
| DC-Ticket.markChecked nhánh CE95 | TC-147, TC-148 | Có |
| DC-Ticket.markChecked nhánh CE96 | TC-148 | Có |
| DC-Ticket.markChecked nhánh CE97 | TC-147 | Có |
| DC-Ticket.markChecked nhánh CE98 | TC-147 | Có |
| DC-Ticket.markChecked nhánh CE99 | TC-148 đến TC-150 | Có |

Quy tắc nghiệp vụ (BR) liên quan tới phương thức trong phạm vi:

| BR | TC phủ | Đạt |
|---|---|---|
| BR-01 Tối đa 5 chỗ mỗi lần đặt | TC-034, TC-037 đến TC-040, TC-066, TC-084 | Có |
| BR-02 Hai vé không cùng một chỗ | TC-071 | Có (phần ngăn hai vé cùng chỗ trên cùng chuyến: ràng buộc dữ liệu duy nhất (trip_id, seat_code) khi status = ISSUED ở P13 TBL-09 và Trip.areSeatsAvailable ở DC-Trip, kiểm thử ở mức DC-Trip và tích hợp CSDL; ở đây chỉ phần Seat từ chối giữ chỗ đã bán) |
| BR-03 Chỗ còn trống | TC-063, TC-064, TC-070 đến TC-072 | Có |
| BR-06 Tổng tiền lần đặt | TC-057 đến TC-059, TC-091, TC-092 | Có |
| BR-07 Giữ chỗ 10 phút | TC-096, TC-097, TC-099 đến TC-104 | Có |
| BR-08 Trả chỗ khi hết hạn giữ | TC-074 đến TC-077 | Có |
| BR-09 Phát hành vé khi thanh toán thành công | TC-081, TC-082, TC-111 | Có |
| BR-10 Mỗi chỗ một vé có một mã vé | TC-081 đến TC-084, TC-088, TC-111, TC-112 | Có |
| BR-11 Trả vé qua đúng kênh mua | TC-001 đến TC-004 | Có |
| BR-12 Không trả vé khi còn dưới 4 giờ | TC-005 đến TC-014 | Có |
| BR-13 Hoàn 90% khi còn từ 24 giờ | TC-019 đến TC-021, TC-023 | Có |
| BR-14 Hoàn 50% khi còn từ 4 đến dưới 24 giờ | TC-015 đến TC-018, TC-022 | Có |
| BR-15 Vé online hoàn qua cổng thanh toán | TC-025, TC-122 | Có |
| BR-16 Vé quầy hoàn bằng tiền mặt | TC-026, TC-123, TC-136 | Có |
| BR-17 Hoàn 100% khi chuyến bị huỷ | TC-027 đến TC-031, TC-134 | Có |
| BR-19 Huỷ chuyến thì hoàn mọi vé còn hiệu lực | TC-029, TC-030, TC-131 | Có |
| BR-21 Vé đã huỷ không hợp lệ khi soát | TC-145, TC-146 | Có |
| BR-22 Vé đã soát không hợp lệ khi soát lại | TC-144, TC-148 | Có |
| BR-20 Vé sai chuyến không hợp lệ khi soát | - | Không: (do lớp điều phối soát vé PKG-11 xác định sai chuyến, không thuộc DC-Ticket; kiểm thử ở mức tích hợp, UC-015 5a) |

BR không nằm ở lớp trong phạm vi (không liệt kê TC): BR-04, BR-05 (DC-Trip, DC-BaseFare), BR-18 (nội dung SMS, DC-TicketSmsContent, DC-TripCancellation).

Luồng thay thế và bước chính của P04:

| Luồng / bước P04 | TC phủ | Đạt |
|---|---|---|
| UC-002 bước 7, 7a, 7b (kiểm thông tin người đi) | TC-041 đến TC-056 | Có |
| UC-002 6a (quá 5 chỗ) | TC-035, TC-040 | Có |
| UC-002 6b (chỗ không còn trống) | TC-070 đến TC-072 | Có |
| UC-002 9a, 9a1 (hết thời hạn giữ chỗ, trả chỗ) | TC-074, TC-103, TC-104 | Có |
| UC-002 10a (thanh toán lại trong hạn giữ) | TC-101 | Có |
| UC-002 bước 9 (giữ chỗ) | TC-063 | Có |
| UC-002 bước 11 (phát hành vé) | TC-081 | Có |
| UC-002 2a, 4a (không có chuyến, hết chỗ) | - | Không: thuộc dịch vụ DC-BookTicketOnlineService và DC-Trip (ngoài phạm vi); kiểm thử ở mức dịch vụ |
| UC-008 2a (không tìm thấy vé) | - | Không: thuộc IF-11.findTicket và DC-ReturnTicketService (ngoài phạm vi); kiểm thử ở mức dịch vụ với kho giả lập |
| UC-008 2b (vé đã huỷ) | TC-121 | Có |
| UC-008 3a (sai kênh) | TC-003, TC-004 | Có |
| UC-008 3b (dưới 4 giờ) | TC-005, TC-008, TC-009, TC-013 | Có |
| UC-008 bước 4 (tính số tiền hoàn) | TC-015, TC-017, TC-019, TC-021 | Có |
| UC-008 bước 5 (hiển thị thông tin vé) | TC-024 | Có |
| UC-008 bước 7, 7a (hình thức hoàn) | TC-025, TC-026 | Có |
| UC-008 bước 10 (huỷ vé, trả chỗ, ghi khoản hoàn) | TC-122, TC-138 | Có |
| UC-008 6a, 9a (không xác nhận; hoàn không thành công) | - | Không: điều phối ở DC-ReturnTicketService và gọi cổng thanh toán IF-01 (ngoài phạm vi); kiểm thử ở mức dịch vụ với stub IF-01 |
| UC-013 bước 3 (tổng tiền hoàn theo kênh) | TC-027, TC-028 | Có |
| UC-013 bước 5 (huỷ vé) | TC-131 | Có |
| UC-013 bước 6 (tính hoàn 100%) | TC-029, TC-030 | Có |
| UC-013 bước 9, 8a (ghi khoản hoàn, hoàn không thành công) | TC-134 đến TC-136 | Có |
| UC-013 2a, 2b, 2c, 4a, 5a, 6a (kiểm tra chuyến, xác nhận, không có vé) | - | Không: thuộc DC-TripCancellation, DC-CancelTripController (ngoài phạm vi) |
| UC-015 bước 5, 5b, 5c (kết luận soát) | TC-143 đến TC-146 | Có |
| UC-015 bước 6 (ghi nhận đã soát) | TC-147 | Có |
| UC-015 5a (sai chuyến) | - | Không: thuộc lớp điều phối soát vé PKG-11 (ngoài phạm vi), BR-20 |

Tóm tắt độ phủ C0, C1 đạt được so với MUC_TIEU_PHU (mặc định: 100% C1 cho ưu tiên Cao, 100% C0 cho còn lại):

| DC.operation | Ưu tiên | MUC_TIEU_PHU | Đạt được | Đạt |
|---|---|---|---|---|
| DC-TicketReturnPolicy.matchesPurchaseChannel | Cao | 100% C1 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-TicketReturnPolicy.isReturnTimeAllowed | Cao | 100% C1 | Chưa đo (V(G) = 1 theo mô tả P12 F3 ("trả timeToDeparture >= MIN_RETURN_TIME"): một biểu thức so sánh trả Boolean, không có điểm quyết định; không vẽ CFG. Biên của phép so sánh được kiểm bằng giá trị biên). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-TicketReturnPolicy.calculateRefundAmount | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 3) | Có |
| DC-TicketReturnPolicy.getTicketReturnInfo | Trung bình | 100% C0 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-TicketReturnPolicy.determineRefundMethod | Cao | 100% C1 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-TicketReturnPolicy.getCancelImpactInfo | Trung bình | 100% C0 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-TicketReturnPolicy.calculateTripCancelRefundAmount | Cao | 100% C1 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Booking.createBooking | Trung bình | 100% C0 | Chưa đo (P12 F3 không có thiết kế method cho createBooking; V(G) ước theo mô tả = 2 (một điểm quyết định: travelerInfos rỗng)). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Booking.isWithinSeatLimit | Cao | 100% C1 | Chưa đo (P12 F3 không có thiết kế method; V(G) ước theo mô tả = 1 (so sánh size <= MAX_SEATS)). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Booking.validateTravelerInfo | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 6) | Có |
| DC-Booking.calculateTotal | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 2) | Có |
| DC-Booking.holdSeats | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 4) | Có |
| DC-Booking.releaseSeats | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 3) | Có |
| DC-Booking.issueTickets | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 3) | Có |
| DC-Booking.getBookingSummary | Trung bình | 100% C0 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Booking.getHoldExpiryTime | Cao | 100% C1 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Booking.isHoldExpired | Cao | 100% C1 | Chưa đo (P12 F3 không có thiết kế method cho phương thức này và chưa có mã nguồn). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Booking.startPaymentAttempt | Trung bình | 100% C0 | C0 = 100%, C1 = 100% (V(G) = 2) | Có |
| DC-Ticket.createTicket | Trung bình | 100% C0 | Chưa đo (P12 F3 không có thiết kế method cho createTicket). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Ticket.isCancelled | Thấp | 100% C0 | Chưa đo (P12 F3 không có thiết kế method; V(G) = 1 theo mô tả (so sánh status với CANCELLED)). Ước tính 100% C0, C1 vì mỗi nhánh theo mô tả có lớp tương đương và TC riêng; đo khi có mã nguồn | Chưa kiểm chứng được (ước tính đạt) |
| DC-Ticket.cancelTicket | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 3) | Có |
| DC-Ticket.cancelWithTrip | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 2) | Có |
| DC-Ticket.recordRefund | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 3) | Có |
| DC-Ticket.determineCheckResult | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 3) | Có |
| DC-Ticket.markChecked | Cao | 100% C1 | C0 = 100%, C1 = 100% (V(G) = 3) | Có |

Điều kiện ghép hiện thực BR: isReturnTimeAllowed (một so sánh), calculateRefundAmount (hai quyết định tách riêng N2, N4), recordRefund và markChecked (điều kiện "hoặc" tách thành hai điểm quyết định, mỗi điều kiện con nhận cả đúng và sai nhờ các TC ở F3). Test case biên của hộp đen được giữ cả khi nhánh đã được phủ (không xoá TC biên 4 giờ, 24 giờ dù CE đã phủ).

## F5. Khung mã test

Không áp dụng: SINH_MA_TEST là "Không có".

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-110 | Khi DC-Booking.holdSeats gặp SeatAlreadyHeldException ở một chỗ giữa chừng, các chỗ đứng trước đã được chuyển HELD có được hoàn về AVAILABLE ngay trong holdSeats hay vẫn HELD để giao dịch của dịch vụ huỷ phần đã đổi (và đối tượng trong bộ nhớ bị bỏ)? Kết quả mong đợi của trạng thái từng Seat sau lỗi là gì? | TC-073 (DC-Booking.holdSeats, chỗ lỗi thứ hai); F2.5 holdSeats | P12 F2, F3: "tất cả hoặc không (giao dịch của dịch vụ gọi huỷ phần đã đổi)" nhưng F3 bước 3 không hoàn tác trong phương thức |
| Q-111 | Khi refundRatePercent ngoài 0..100 hoặc refundAmount âm, DC-Ticket.cancelTicket và recordRefund ném IllegalArgumentException trước khi đổi trạng thái (vé giữ nguyên ISSUED, Seat không đổi, không có Refund) hay để Refund.createRefund ném sau khi status đã là CANCELLED và Seat đã release (thứ tự bước 2, 3, 5 của F3)? | DC-Ticket.cancelTicket (BV-44, BV-45, BV-47); DC-Ticket.recordRefund | P12 F2 cancelTicket chỉ khai báo InvalidStateException; DC-Refund.createRefund có tiền điều kiện miền nhưng thứ tự bước trong F3 làm đổi trạng thái trước |
| Q-112 | DC-Ticket.createTicket có từ chối (IllegalArgumentException) khi travelerName chỉ gồm khoảng trắng không? (DC-Booking.validateTravelerInfo cắt khoảng trắng và coi là thiếu họ tên; F7 chỉ ghi {không rỗng}) | DC-Ticket.createTicket (EC-98) | P12 F7 DC-Ticket.travelerName {không rỗng} không nêu có cắt khoảng trắng |
| Q-113 | DC-Ticket.recordRefund chấp nhận những tổ hợp (refundMethod, refundOutcome) nào? Ví dụ (VIA_GATEWAY, AWAITING_CASH_PAYOUT) và (CASH_AT_COUNTER, REFUNDED) có hợp lệ không, hay phải ném ngoại lệ? | DC-Ticket.recordRefund (EC-130) | P12 F2: "refundOutcome do dịch vụ xác định (ASM-48)"; P04 UC-013 chỉ nêu ba tổ hợp (online hoàn xong, online chưa thành công, quầy chờ chi tiền mặt) |
| Q-114 | DC-Booking.createBooking có từ chối (IllegalArgumentException) khi travelerInfos có hai phần tử trùng seatCode không, hay chỉ ràng buộc {mỗi seatCode một phần tử} của F7 được bảo đảm bởi lớp gọi (Trip.areSeatsAvailable trả false khi mã trùng)? | DC-Booking.createBooking (EC-30) | P12 F7 DC-Booking.travelerInfos {mỗi seatCode một phần tử}; P12 F2 createBooking chỉ nêu tiền điều kiện travelerInfos không rỗng |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-111 | Mọi tham số tham chiếu (entity, enumeration, Money, List, LocalDateTime, Duration, chuỗi) do lớp gọi truyền vào đều khác null, bookingId không rỗng, và vé truyền vào DC-TicketReturnPolicy có trạng thái phù hợp với luồng gọi (lớp gọi bảo đảm). Unit test không kiểm lớp null của tham số. | P12 không khai báo ngoại lệ hay kết quả cho null hoặc vé sai trạng thái ở các operation này; kiểm thử hành vi không được đặc tả sẽ buộc phải tự quyết kết quả mong đợi (C1 mục 2) | Các EC "null" ở F2.x.2 (không có TC); DC-TicketReturnPolicy.getCancelImpactInfo, calculateTripCancelRefundAmount với vé CANCELLED |
| ASM-112 | Thời điểm now đúng bằng holdStartTime + 10 phút là đã hết thời hạn giữ chỗ (isHoldExpired trả true). | BR-07 nêu "trong 10 phút kể từ khi bắt đầu giữ" mà không nói biên đóng hay mở; P12 F2 isHoldExpired dùng "không trước thời điểm hết hạn". Chờ xác nhận ở BR-07 | DC-Booking.isHoldExpired (biên BV của EC hết hạn); DC-Booking.getHoldExpiryTime |
| ASM-113 | Biên 4 giờ và 24 giờ của thời gian còn lại được so sánh theo độ chính xác của Duration (đến giây): 3 giờ 59 phút 59 giây là dưới 4 giờ, 23 giờ 59 phút 59 giây là dưới 24 giờ. | BR-12 đến BR-14 nêu mốc theo giờ và P04 hiển thị theo giờ, phút mà không nêu có làm tròn xuống phút hay không; Duration của P12 có độ chính xác cao hơn phút | DC-TicketReturnPolicy.isReturnTimeAllowed (BV), calculateRefundAmount (BV) |
| ASM-114 | Các thuộc tính ở P12 F7 mà F2 chưa có getter đọc được qua accessor trùng tên thuộc tính trong test (Seat.getStatus, Ticket.getStatus, Ticket.getCheckedTime, Ticket.getRefund, Booking.getPaymentReference, Booking.getPaymentAttemptCount, Refund.getRefundAmount, getRefundRatePercent, getRefundMethod, getRefundOutcome). | Kiểm tra "trạng thái sau" cần quan sát được thuộc tính; P12 F2 chỉ có getter cho một số thuộc tính | Cột Kết quả mong đợi của các TC nêu trạng thái Seat, vé, Refund, paymentReference, paymentAttemptCount |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P12 | DC-Seat, DC-Ticket, DC-Booking, DC-Refund (F2) | Nhiều thuộc tính có trong F7 nhưng không có accessor ở F2 nên trạng thái sau không quan sát được qua giao diện công khai (Seat.status phân biệt HELD với SOLD; Ticket.status, checkedTime, refund; Booking.paymentReference, paymentAttemptCount; thuộc tính của Refund) (ASM-114) | Thêm getStatus() cho DC-Seat và DC-Ticket, getCheckedTime(), getRefund() cho DC-Ticket, getPaymentReference() cho DC-Booking (ASM-41 ghi để hoàn tiền nhưng chưa có operation đọc), và accessor cho thuộc tính của DC-Refund |
| P12 | DC-Ticket.cancelTicket F3 bước 2, 3, 5 | Trạng thái vé và Seat đổi trước khi Refund.createRefund kiểm miền tham số, nên tham số sai làm vé CANCELLED nhưng không có Refund (Q-111) | Kiểm miền refundRatePercent, refundAmount trước khi đổi trạng thái (hoặc tạo Refund trước rồi mới đổi trạng thái) và khai báo IllegalArgumentException ở F2 của cancelTicket, recordRefund |
| P12 | DC-Booking.holdSeats F2, F3 | Mô tả "tất cả hoặc không" nhưng F3 không hoàn tác Seat đã giữ khi một chỗ lỗi, trạng thái Seat sau lỗi không xác định (Q-110) | Ghi rõ hợp đồng: hoặc hoàn tác trong holdSeats (release các Seat đã hold) hoặc ghi trong hậu điều kiện rằng đối tượng phải bị bỏ và trạng thái Seat không bảo đảm |
| P12 | DC-Ticket.recordRefund F2 | Không nêu tổ hợp (refundMethod, refundOutcome) hợp lệ (Q-113) | Bổ sung tiền điều kiện về ba tổ hợp của UC-013 hoặc ghi rõ không kiểm |
| P06 | BR-07 | Biên 10 phút chưa nói rõ đóng hay mở (ASM-112); BR-12 đến BR-14 chưa nêu độ chính xác thời gian (ASM-113) | Bổ sung diễn đạt "dưới 10 phút" hoặc "không quá 10 phút" và độ chính xác phút hay giây của thời gian còn lại |

## Vấn đề còn mở

- Target 9 (độ phủ): 13 trong 25 phương thức được chọn không có thiết kế method ở P12 F3 nên C0, C1 chỉ ước tính; cần đo bằng công cụ độ phủ khi có mã nguồn và chạy lại bước 4.
- Target 2 và 3: lớp "price âm" của DC-Ticket.createTicket không có EC riêng vì Money (PKG-28) chưa được thiết kế, chưa biết Money có biểu diễn giá trị âm không; lớp price <= 0 được đại diện bằng 0 đ.
- Target 6: UC-008 luồng 2a, 6a, 9a, UC-013 luồng 2a đến 6a, UC-002 luồng 2a, 4a, UC-015 luồng 5a thuộc lớp ngoài phạm vi; cần X2 chạy tiếp cho DC-ReturnTicketService, DC-BookTicketOnlineService, DC-TripCancellation (xem F4).
- Target 8: 8 test case có kết quả mong đợi chưa xác định chờ Q-110 đến Q-113 (đánh dấu "Chưa xác định" ở F3); TC của Q-114 cũng chưa xác định. Số TC bị ảnh hưởng: 8.
- Target 13: không áp dụng vì không sinh khung mã.
- Chọn giữa hai quy tắc (C9): C1 mục 2 (không tự quyết kết quả khi đặc tả không nói) ưu tiên hơn bước 3.6 yêu cầu ghi kết quả cụ thể cho mọi tổ hợp; các tổ hợp thiếu đặc tả được ghi Q hoặc ASM thay vì tự suy ra, riêng giá trị null và vé sai trạng thái ghi ASM-111 để không tạo ra hàng chục TC phụ thuộc vào suy đoán.
- Phạm vi chạy: 25 operation được chọn, 150 test case; vượt khuyến nghị "một package hoặc vài lớp liên quan" ở mục 3 của prompt nếu tính theo số TC, nhưng đã chạy một lượt theo PHAM_VI_TEST.
