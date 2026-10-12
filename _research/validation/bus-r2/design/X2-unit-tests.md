# X2 - Thiết kế unit test DC-Trip, DC-Booking, DC-Ticket - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | X2 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CONG_NGHE đã chốt: Java 17, Spring Boot, Thymeleaf, PostgreSQL; MUC_CHI_TIET = DAY_DU; CHE_DO_GIA_DINH = CO_NHAN; hồ sơ không nêu framework test); P12-class-design/PKG-13-PKG-27-PKG-28-booking-ticketing.md phiên bản 1.0 (F1, F1b, F2, F3, F5, F6 ST-01 và ST-03, ST-04, F7, Câu hỏi mở, Giả định, Đề xuất sửa artifact trước; chỉ phần của DC-Trip, DC-Booking, DC-Ticket, DC-Seat và kiểu phụ trợ liên quan); P06-supplementary-spec.md phiên bản 1.0 (Mục 6 BR-01 đến BR-11, NFR-04 đến NFR-06); P04-uc-specs/UC-009-book-ticket-online.md và UC-017-cancel-trip.md phiên bản 1.0 (mục 3, 5, 6, 8, 8a, Câu hỏi mở, Giả định); P13-data-model.md phiên bản 1.0 (F6.1, F6.1-b: ràng buộc dữ liệu của trip, booking, ticket); X1-design-review.md (chỉ mục Câu hỏi mở, Giả định, để cấp tiếp mã Q, ASM). Placeholder: PHAM_VI_TEST = "DC-Booking, DC-Ticket, DC-Trip (file P12-class-design/PKG-13-PKG-27-PKG-28-booking-ticketing.md)"; MUC_TIEU_PHU = Không có (mặc định: 100% C1 cho phương thức ưu tiên Cao); SINH_MA_TEST = Không có; MA_TC_BAT_DAU = Không có; YEU_CAU_BO_SUNG = Không có. Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-76, ASM-56 (X1 và P12); lần chạy này cấp Q-77 và ASM-57 |
| Phạm vi | DC-Trip, DC-Booking, DC-Ticket (PKG-27, PKG-28): 25 dòng ở F1, 11 operation được chọn, 65 test case (TC-001 đến TC-065). 9 operation chưa chọn (7 Cao, 2 Trung bình) hoãn sang lần chạy sau (xem Vấn đề còn mở) |
| Mã Q, ASM cuối đã cấp | Q-77, ASM-57 |

Kiểm tra đầu vào (Bước 0): placeholder đã điền đủ theo C6; bốn placeholder tuỳ chọn MUC_TIEU_PHU, SINH_MA_TEST, MA_TC_BAT_DAU và YEU_CAU_BO_SUNG dùng giá trị "Không có", nên F5 (khung mã test) không được sinh. P12 có thiết kế method ở F3 cho 7 trong 11 operation được chọn (Trip.cancel, Booking.holdSeats, recordTravelerInfo, releaseHeldSeats, issueTickets, Ticket.cancelForTrip, calculateRefundAmount) nên hộp trắng làm ở mức thiết kế với 7 sơ đồ CFG; bốn operation còn lại (Trip.isBeforeDeparture, Booking.isSeatCountWithinLimit, isHoldExpired, Ticket.isOnlineRefundPending) không có dòng ở F3 và không có mã nguồn nên C0, C1 ghi "Đo khi có mã nguồn". Các chỗ P12 chưa đủ cho việc test (hậu điều kiện không quan sát được qua operation công khai, điều kiện đầu không dựng được qua operation công khai, thiếu hành vi cho đầu vào ngoài miền) ghi ở "Đề xuất sửa artifact trước", ASM-57 và Q-77. Chế độ CO_NHAN: các kết quả mong đợi dựa vào giả định đã chốt của bước trước dẫn mã ASM đó ở cột Nguồn (ASM-18, ASM-21, ASM-24, ASM-25, ASM-26, ASM-29); không phát sinh giả định mới ngoài ASM-57.

## F1. Bảng chọn operation

Tiêu chí chọn theo Bước 1 của prompt: ưu tiên Cao cho phương thức hiện thực BR, phương thức có nhiều nhánh, sự kiện của state machine, phương thức kiểm tra hợp lệ dữ liệu vào. Lần chạy này giới hạn 11 operation theo ngưỡng "khoảng 10 operation hoặc 60 TC" của mục 3 prompt; các operation Cao chưa chọn ghi "Không: hoãn lần chạy sau" và được liệt kê ở Vấn đề còn mở với mã TC bắt đầu đề nghị TC-066.

| DC.operation | Tiêu chí (BR / rẽ nhánh / tính toán / sự kiện ST / kiểm tra hợp lệ / điều phối UC / gọi hệ thống ngoài) | Ưu tiên (Cao / Trung bình / Thấp) | Chọn (Có / Không: lý do) |
|---|---|---|---|
| DC-Trip.Trip(departureTime, route, vehicleType, vehicle, driver) | Kiểm tra hợp lệ (IllegalArgumentException khi tham số rỗng); sự kiện ST-01 create | Cao | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Trip.isBeforeDeparture(now) | BR (BR-05, BR-10); so sánh thời gian ở biên | Cao | Có |
| DC-Trip.isCancelled() | Truy vấn một so sánh trạng thái (BR-09) | Thấp | Không: không có logic riêng, được dùng làm phép kiểm tra trạng thái ở TC-001 đến TC-005 |
| DC-Trip.cancel(reason, now) | BR (BR-09, BR-10); rẽ nhánh; sự kiện ST-01 cancel | Cao | Có |
| DC-Trip.getId, getRoute, getDepartureTime, getVehicleType, getStatus, getCancelReason, getVehicle, getDriver | Getter | Thấp | Không: getter không có logic (được dùng để kiểm tra trạng thái sau ở các TC) |
| DC-Booking.createBooking(trip, seats) | Kiểm tra hợp lệ (seats rỗng, chỗ không thuộc chuyến); sự kiện ST-03 create | Cao | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Booking.isSeatCountWithinLimit() | BR (BR-01) | Cao | Có |
| DC-Booking.holdSeats(seatFare, now) | BR (BR-03, BR-02); rẽ nhánh; vòng lặp; sự kiện ST-03 holdSeats | Cao | Có |
| DC-Booking.recordTravelerInfo(travelerName, travelerPhone, now) | Kiểm tra hợp lệ (luồng 7a); BR-03 (luồng 5a); sự kiện ST-03 | Cao | Có |
| DC-Booking.calculateTotalAmount() | Tính toán (giá vé một chỗ nhân số chỗ) | Cao | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Booking.clearHoldExpiry() | Sự kiện ST-03 clearHoldExpiry; rẽ nhánh | Cao | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Booking.isHoldExpired(now) | BR (BR-03); so sánh thời gian ở biên | Cao | Có |
| DC-Booking.releaseHeldSeats() | Sự kiện ST-03 releaseHeldSeats; rẽ nhánh; vòng lặp | Cao | Có |
| DC-Booking.issueTickets(ticketCodes, transaction) | BR (BR-04); rẽ nhánh; vòng lặp; sự kiện ST-03 issueTickets | Cao | Có |
| DC-Booking.getId, getStatus, getTrip, getSeats, getTravelerName, getTravelerPhone, getHoldExpiry, getSeatFare | Getter | Thấp | Không: getter không có logic (được dùng để kiểm tra trạng thái sau ở các TC) |
| DC-Ticket.createTicket(trip, seat, travelerName, travelerPhone, fare, ticketCode, transaction) | Kiểm tra hợp lệ (seat thuộc trip); sự kiện ST-04 create | Cao | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC); được dùng làm bước chuẩn bị ở nhiều TC |
| DC-Ticket.recordSmsNotSent() | Sự kiện ST-04 (tự chuyển, cờ ghi nhận) | Trung bình | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Ticket.cancelForTrip() | Rẽ nhánh theo paymentStatus (ASM-29); sự kiện ST-04 cancelForTrip | Cao | Có |
| DC-Ticket.isActive() | Truy vấn một so sánh trạng thái (GL-25) | Thấp | Không: không có logic riêng |
| DC-Ticket.isOnlineRefundPending() | BR (BR-08); điều kiện ghép bốn thành phần | Cao | Có |
| DC-Ticket.calculateRefundAmount() | BR (BR-07), tính toán; kiểm tra tiền điều kiện | Cao | Có |
| DC-Ticket.markRefunded() | Sự kiện ST-04 markRefunded; NFR-05 (không hoàn lần hai) | Cao | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Ticket.recordRefundNotCompleted() | Sự kiện ST-04 recordRefundNotCompleted (luồng 12a) | Cao | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Ticket.markCancelNoticeNotSent() | Sự kiện ST-04 (tự chuyển, cờ ghi nhận; luồng 9a) | Trung bình | Không: hoãn lần chạy sau (vượt ngưỡng 10 operation / 60 TC) |
| DC-Ticket.getTicketCode, getSeat, getTravelerName, getTravelerPhone, getFare, getStatus, getRefundStatus, getPaymentTransaction, getSmsStatus, getCancelNoticeStatus, getRefundAttemptStatus | Getter | Thấp | Không: getter không có logic (được dùng để kiểm tra trạng thái sau ở các TC) |

## F2. Phân tích kỹ thuật cho từng operation

Quy ước chung cho F2 và F3: các operation nhận thời điểm hiện tại qua tham số now nên không cần đồng hồ giả lập; mọi giá trị thời gian là LocalDateTime giờ địa phương, đơn vị nhỏ nhất của giá trị biên là 1 giây (Thiết kế: nguồn không nêu độ phân giải của thời điểm; chọn giây để tách được hai phía của biên mà không phụ thuộc cách hiển thị tới phút). EC null, tham số ngoài miền mà P12 không nêu hành vi và các thuộc tính vi phạm ràng buộc F7 được liệt kê trong EC nhưng không có TC: xem ASM-57.

### F2.1 DC-Trip.cancel

F2.1.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | cancel(reason: CancelReason, now: LocalDateTime): void; reason là lý do nhân viên điều hành chọn (VEHICLE_BREAKDOWN hoặc BAD_WEATHER), now là thời điểm hiện tại do bên gọi cấp | P12 F2, F1b DC-CancelReason |
| Tiền điều kiện | status = SCHEDULED (BR-09) và now < departureTime (BR-10); kiểm tra theo thứ tự này | P12 F2 DC-Trip.cancel; ASM-26 (chờ Q-46) |
| Hậu điều kiện | status = CANCELLED, cancelReason = reason | P12 F2 |
| Ngoại lệ | TripAlreadyCancelledException (luồng 4a), TripDepartedException (luồng 4b) | P12 F2; P04 UC-017 mục 3 |
| BR | BR-09 chuyến đã huỷ không huỷ lại; BR-10 chuyến từ giờ xuất bến trở đi không huỷ được | P06 Mục 6; P04 UC-017 mục 6 |
| Luồng thay thế | 4a chuyến đã huỷ: từ chối; 4b chuyến đã tới giờ xuất bến: từ chối | P04 UC-017 mục 3 |
| Điều kiện hợp lệ | Lý do huỷ chuyến là một trong hai giá trị Xe hỏng, Thời tiết (chờ Q-36) | P04 UC-017 Dữ liệu vào 1 dòng 2; ASM-25 |
| Chuyển trạng thái | ST-01: Scheduled --> Cancelled khi cancel [now < departureTime]; Cancelled hoặc quá giờ xuất bến thì từ chối | P12 F6 ST-01 |

Không áp dụng: F2.1.7 (không có phụ thuộc ngoài, now là tham số).

F2.1.2. Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-01 | status | status = SCHEDULED | Hợp lệ | SCHEDULED | BR-09 |
| EC-02 | status | status = CANCELLED | Không hợp lệ | CANCELLED (đã huỷ trước đó) | BR-09; UC-017 4a |
| EC-03 | now | now < departureTime | Hợp lệ | 2026-12-14T09:00:00 | BR-10 |
| EC-04 | now | now >= departureTime | Không hợp lệ | 2026-12-15T20:30:00 | BR-10; UC-017 4b; ASM-26 |
| EC-05 | reason | reason thuộc {VEHICLE_BREAKDOWN, BAD_WEATHER} | Hợp lệ | VEHICLE_BREAKDOWN, BAD_WEATHER | ASM-25 |
| EC-06 | reason | reason = null | Không hợp lệ | null | ASM-57 (không có TC) |
| EC-07 | now | now = null | Không hợp lệ | null | ASM-57 (không có TC) |

F2.1.3. Giá trị biên (departureTime của chuyến thử = 2026-12-15T20:30:00)

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-01 | max của EC-03 | now = 2026-12-15T20:29:59 | EC-03 | Huỷ thành công: status = CANCELLED |
| BV-02 | min của EC-04 | now = 2026-12-15T20:30:00 | EC-04 | TripDepartedException; status vẫn SCHEDULED |

F2.1.4. Bảng quyết định (C1: status = SCHEDULED; C2: now < departureTime)

```text
| Điều kiện / Hành động | DT1-R1 | DT1-R2 | DT1-R3 | DT1-R4 |
| C1: status = SCHEDULED | Y | Y | N | N |
| C2: now < departureTime | Y | N | Y | N |
| A1: status = CANCELLED, cancelReason = reason | X | - | - | - |
| A2: ném TripDepartedException | - | X | - | - |
| A3: ném TripAlreadyCancelledException | - | - | X | X |
```

Không gộp quy tắc nào. DT1-R4 (cả hai điều kiện sai) nhận A3 vì F2 ghi kiểm tra status trước now và ASM-26 ghi phản hồi chuyến đã huỷ (4a) trước chuyến đã tới giờ (4b); căn cứ P12 F2 DC-Trip.cancel, P04 UC-017 ASM-26, P12 F6 ST-01 bảng sự kiện bị từ chối.

F2.1.5. Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Scheduled | cancel(reason, now) | [now < departureTime] đúng (biên 20:29:59) | Không ngoại lệ | Cancelled, cancelReason = reason | ST-01 chuyển 2 |
| Scheduled | cancel(reason, now) | [now < departureTime] sai (biên 20:30:00) | TripDepartedException | Scheduled, cancelReason rỗng | ST-01 sự kiện bị từ chối dòng 1 |
| Cancelled | cancel(reason, now) | không có chuyển | TripAlreadyCancelledException | Cancelled, cancelReason giữ giá trị cũ | ST-01 sự kiện bị từ chối dòng 2 |

F2.1.6. Hộp trắng (thiết kế method: P12 F3 DC-Trip.cancel)

Bảng node (nguồn chuẩn của sơ đồ X2-cfg-DC-Trip-cancel.drawio; x, y, w, h là toạ độ góc trên trái và kích thước):

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) | x | y | w | h |
|---|---|---|---|---|---|---|
| N1 | Bắt đầu | bắt đầu | 280 | 60 | 40 | 40 |
| N2 | status = CANCELLED? | quyết định | 120 | 190 | 360 | 140 |
| N3 | Ném TripAlreadyCancelledException (luồng 4a) | khối lệnh | 660 | 220 | 320 | 80 |
| N4 | now >= departureTime? | quyết định | 120 | 370 | 360 | 140 |
| N5 | Ném TripDepartedException (luồng 4b) | khối lệnh | 660 | 400 | 320 | 80 |
| N6 | status = CANCELLED; cancelReason = reason | khối lệnh | 140 | 580 | 320 | 80 |
| N7 | Kết thúc | kết thúc | 280 | 780 | 40 | 40 |

Bảng cạnh (cột Điểm uốn theo Conventions C7.1; "-" là đi thẳng):

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) | Điểm uốn |
|---|---|---|---|---|
| CE1 | N1 | N2 | - | - |
| CE2 | N2 | N3 | Đúng | - |
| CE3 | N2 | N4 | Sai | - |
| CE4 | N4 | N5 | Đúng | - |
| CE5 | N4 | N6 | Sai | - |
| CE6 | N6 | N7 | - | - |
| CE7 | N3 | N7 | - | (1040,260); (1040,800) |
| CE8 | N5 | N7 | - | (1040,440); (1040,800) |

V(G) = E - N + 2 = 8 - 7 + 2 = 3; kiểm tra bằng số quyết định nhị phân + 1 = 2 + 1 = 3 (quyết định: N2, N4). Số đường đi cơ sở độc lập: 3.

Đường đi cơ sở:

- ĐĐ1: N1-N2-N4-N6-N7 (huỷ thành công)
- ĐĐ2: N1-N2-N3-N7 (chuyến đã huỷ (4a))
- ĐĐ3: N1-N2-N4-N5-N7 (đã tới giờ xuất bến (4b))

Bảng phủ nhánh (mọi N có ít nhất một cạnh vào hoặc ra nên phủ hết cạnh thì phủ hết N):

| Nhánh (CE) | TC phủ |
|---|---|
| CE1 (N1 --> N2) | TC-001, TC-002, TC-003, TC-004, TC-005 |
| CE2 (N2 --> N3, Đúng) | TC-004, TC-005 |
| CE3 (N2 --> N4, Sai) | TC-001, TC-002, TC-003 |
| CE4 (N4 --> N5, Đúng) | TC-003 |
| CE5 (N4 --> N6, Sai) | TC-001, TC-002 |
| CE6 (N6 --> N7) | TC-001, TC-002 |
| CE7 (N3 --> N7) | TC-004, TC-005 |
| CE8 (N5 --> N7) | TC-003 |

Độ phủ đạt được: C0 = 7/7 lệnh (node) = 100%; C1 = 8/8 nhánh (cạnh) = 100%.

Sơ đồ CFG: diagrams/X2-cfg-DC-Trip-cancel.drawio (ID cell trùng N, CE).

Vòng lặp: không có.

### F2.2 DC-Trip.isBeforeDeparture

F2.2.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isBeforeDeparture(now: LocalDateTime): boolean | P12 F2 |
| Tiền điều kiện | Không | P12 F2 |
| Hậu điều kiện | true khi now < departureTime (BR-05, BR-10); không đổi trạng thái | P12 F2 |
| Ngoại lệ | Không | P12 F2 |
| BR | BR-05 vé của một chuyến chỉ bán trực tuyến cho đến giờ xuất bến, từ giờ xuất bến trở đi không giữ chỗ (ASM-21, chờ Q-13); BR-10 | P06 Mục 6; P04 UC-009 mục 6 |
| Luồng thay thế | UC-009 4c chuyến đã tới giờ xuất bến | P04 UC-009 mục 3 |

Không áp dụng: F2.2.4 (một điều kiện), F2.2.5 (không là sự kiện của state machine), F2.2.6 (không có thiết kế method ở P12 F3 và không có mã nguồn; C0, C1 đo khi có mã nguồn), F2.2.7 (không có phụ thuộc ngoài).

F2.2.2. Phân vùng tương đương (phân vùng theo đầu ra; "Hợp lệ" là lớp cho kết quả true, tức còn được bán vé; "Không hợp lệ" là lớp cho kết quả false)

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-08 | now | now < departureTime | Hợp lệ (true) | 2026-12-15T20:29:59 | BR-05 |
| EC-09 | now | now >= departureTime | Không hợp lệ (false) | 2026-12-15T20:30:00 | BR-05; UC-009 4c |
| EC-10 | now | now = null | Không hợp lệ | null | ASM-57 (không có TC) |
| EC-11 | trạng thái chuyến | status = SCHEDULED | Hợp lệ (kết quả chỉ phụ thuộc now) | SCHEDULED | P12 F2 hậu điều kiện |
| EC-12 | trạng thái chuyến | status = CANCELLED | Hợp lệ (kết quả chỉ phụ thuộc now) | CANCELLED | P12 F2 hậu điều kiện |

F2.2.3. Giá trị biên (departureTime = 2026-12-15T20:30:00)

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-03 | max của EC-08 | now = 2026-12-15T20:29:59 | EC-08 | true |
| BV-04 | min của EC-09 | now = 2026-12-15T20:30:00 | EC-09 | false |

### F2.3 DC-Booking.isSeatCountWithinLimit

F2.3.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isSeatCountWithinLimit(): boolean | P12 F2 |
| Tiền điều kiện | Không (lần đặt luôn có ít nhất một chỗ do createBooking từ chối danh sách rỗng) | P12 F2 DC-Booking.createBooking |
| Hậu điều kiện | true khi số chỗ <= MAX_SEATS = 5 (BR-01) | P12 F2; F7 MAX_SEATS |
| Ngoại lệ | Không | P12 F2 |
| BR | BR-01 mỗi lần đặt vé chọn tối đa 5 chỗ | P06 Mục 6; P04 UC-009 mục 6 |
| Luồng thay thế | UC-009 4b số chỗ lớn hơn 5: từ chối | P04 UC-009 mục 3 |
| Điều kiện hợp lệ | Từ 1 đến 5 chỗ | P04 UC-009 Dữ liệu vào 1 |

Không áp dụng: F2.3.4 (một điều kiện), F2.3.5 (không là sự kiện của state machine), F2.3.6 (không có thiết kế method ở P12 F3 và không có mã nguồn; C0, C1 đo khi có mã nguồn), F2.3.7 (không có phụ thuộc ngoài; DC-Seat dùng bản thật).

F2.3.2. Phân vùng tương đương (theo đầu ra)

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-13 | số chỗ n của lần đặt | 1 <= n <= 5 | Hợp lệ (true) | 3 | BR-01 |
| EC-14 | số chỗ n | n >= 6 | Không hợp lệ (false) | 6 | BR-01; UC-009 4b |
| EC-15 | số chỗ n | n <= 0 | Không thể xảy ra: createBooking ném IllegalArgumentException khi danh sách chỗ rỗng | - | P12 F2 DC-Booking.createBooking (không có TC) |

F2.3.3. Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-05 | min của EC-13 | n = 1 | EC-13 | true |
| BV-06 | max của EC-13 | n = 5 | EC-13 | true |
| BV-07 | min của EC-14 (max + 1) | n = 6 | EC-14 | false |

### F2.4 DC-Booking.holdSeats

F2.4.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | holdSeats(seatFare: Money, now: LocalDateTime): void; seatFare là giá vé một chỗ đã xác định, now là thời điểm giữ | P12 F2 |
| Tiền điều kiện | status = SELECTING, số chỗ <= MAX_SEATS (= 5) | P12 F2 |
| Hậu điều kiện | status = HOLDING; mọi Seat HELD; holdStartedAt = now; holdExpiry = now + HOLD_DURATION (10 phút); seatFare đã ghi. holdStartedAt không có getter nên không quan sát được trực tiếp (xem Đề xuất sửa artifact trước); kiểm tra gián tiếp qua getHoldExpiry() = now + 10 phút | P12 F2, F7; BR-03; ASM-18 (chờ Q-18) |
| Ngoại lệ | SeatsUnavailableException khi có chỗ không còn trống; IllegalStateException khi status khác SELECTING | P12 F2 |
| BR | BR-03 giữ chỗ 10 phút tính từ lúc hệ thống giữ chỗ; BR-02 không hai vé cùng một chỗ; NFR-04 chỉ một yêu cầu giữ được chỗ | P06 Mục 4, 6; P04 UC-009 mục 6, 7 |
| Luồng thay thế | UC-009 4a có chỗ không còn trống: từ chối | P04 UC-009 mục 3 |
| Chuyển trạng thái | ST-03: Selecting --> Holding khi holdSeats [mọi chỗ AVAILABLE]; ST-02: Available --> Held cho từng chỗ | P12 F6 ST-03 chuyển 2, ST-02 chuyển 2 |
| Ví dụ trong đặc tả | Giữ chỗ lúc 20:00 thì hết thời hạn lúc 20:10 | P04 UC-009 mục 8 |

F2.4.2. Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-16 | status của Booking | SELECTING | Hợp lệ | SELECTING | P12 F2 |
| EC-17 | status của Booking | HOLDING | Không hợp lệ (IllegalStateException) | HOLDING | P12 F6 ST-03 |
| EC-18 | status của Booking | SEATS_RELEASED | Không hợp lệ (IllegalStateException) | SEATS_RELEASED | P12 F6 ST-03 |
| EC-19 | status của Booking | TICKETS_ISSUED | Không hợp lệ (IllegalStateException) | TICKETS_ISSUED | P12 F6 ST-03 |
| EC-20 | trạng thái các chỗ | mọi chỗ AVAILABLE | Hợp lệ | A05, A06 AVAILABLE | BR-02 |
| EC-21 | trạng thái các chỗ | có ít nhất một chỗ HELD | Không hợp lệ (SeatsUnavailableException) | A05 HELD | BR-02; NFR-04; UC-009 4a |
| EC-22 | trạng thái các chỗ | không có chỗ HELD, có ít nhất một chỗ SOLD | Không hợp lệ (SeatsUnavailableException) | A05 SOLD | BR-02; ST-02 |
| EC-23 | số chỗ n | 1 <= n <= 5 | Hợp lệ | 2 | BR-01 |
| EC-24 | số chỗ n | n >= 6 | Không hợp lệ (vi phạm tiền điều kiện, P12 không nêu hành vi) | 6 | ASM-57 (không có TC) |
| EC-25 | seatFare | Money lớn hơn 0 | Hợp lệ | 250.000 đồng | P12 F7 DC-Booking.seatFare |
| EC-26 | seatFare | Money nhỏ hơn hoặc bằng 0, hoặc null | Không hợp lệ (P12 không nêu hành vi) | 0, null | ASM-57 (không có TC) |
| EC-27 | now | LocalDateTime hợp lệ | Hợp lệ | 2026-12-14T20:00:00 | P12 F2 |
| EC-28 | now | now = null | Không hợp lệ | null | ASM-57 (không có TC) |

F2.4.3. Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-08 | min của EC-23 | n = 1 | EC-23 | Giữ thành công, 1 chỗ HELD |
| BV-09 | max - 1 của EC-23 | n = 4 | EC-23 | Giữ thành công, 4 chỗ HELD |
| BV-10 | max của EC-23 | n = 5 | EC-23 | Giữ thành công, 5 chỗ HELD |
| BV-11 | biên ngày của đầu ra holdExpiry (EC-27) | now = 2026-12-14T23:55:00 | EC-27 | holdExpiry = 2026-12-15T00:05:00 |

F2.4.4. Bảng quyết định (C1: status = SELECTING; C2: mọi chỗ AVAILABLE)

```text
| Điều kiện / Hành động | DT2-R1 | DT2-R2 | DT2-R3 | DT2-R4 |
| C1: status = SELECTING | Y | Y | N | N |
| C2: mọi chỗ AVAILABLE | Y | N | Y | N |
| A1: giữ chỗ thành công (HOLDING, chỗ HELD) | X | - | - | - |
| A2: ném SeatsUnavailableException | - | X | - | - |
| A3: ném IllegalStateException | - | - | X | X |
```

Không gộp quy tắc nào. DT2-R4 nhận A3 vì P12 F6 (bảng sự kiện bị từ chối) ghi mọi trạng thái khác SELECTING từ chối holdSeats bằng IllegalStateException bất kể trạng thái chỗ, và P12 F3 bước 1 kiểm tra status trước khi đụng tới chỗ. Ghi chú: DT2-R3 ứng với Booking SEATS_RELEASED (các chỗ đã về AVAILABLE); DT2-R4 ứng với Booking HOLDING (chỗ HELD) và TICKETS_ISSUED (chỗ SOLD).

F2.4.5. Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Selecting | holdSeats(seatFare, now) | [mọi chỗ AVAILABLE] đúng (0 chỗ không AVAILABLE) | Không ngoại lệ | Holding; chỗ HELD; holdExpiry = now + 10 phút | ST-03 chuyển 2 |
| Selecting | holdSeats(seatFare, now) | [mọi chỗ AVAILABLE] sai (1 chỗ HELD hoặc SOLD, lần đặt 1 chỗ) | SeatsUnavailableException | Selecting không đổi, holdExpiry và seatFare rỗng; chỗ giữ nguyên trạng thái trước | ST-03 sự kiện bị từ chối dòng 4 |
| Selecting | holdSeats(seatFare, now) | [mọi chỗ AVAILABLE] sai ở chỗ thứ hai trở đi | SeatsUnavailableException | Chưa xác định: chờ Q-77 | ST-03 sự kiện bị từ chối dòng 4 |
| Holding | holdSeats | không có chuyển | IllegalStateException | Holding không đổi | ST-03 sự kiện bị từ chối dòng 3 |
| SeatsReleased | holdSeats | không có chuyển | IllegalStateException | SeatsReleased không đổi | ST-03 sự kiện bị từ chối dòng 7 |
| TicketsIssued | holdSeats | không có chuyển | IllegalStateException | TicketsIssued không đổi | ST-03 sự kiện bị từ chối dòng 8 |

F2.4.6. Hộp trắng (thiết kế method: P12 F3 DC-Booking.holdSeats(Money, LocalDateTime))

Bảng node (nguồn chuẩn của sơ đồ X2-cfg-DC-Booking-holdSeats.drawio; x, y, w, h là toạ độ góc trên trái và kích thước):

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) | x | y | w | h |
|---|---|---|---|---|---|---|
| N8 | Bắt đầu | bắt đầu | 280 | 60 | 40 | 40 |
| N9 | status khác SELECTING? | quyết định | 120 | 190 | 360 | 140 |
| N10 | Ném IllegalStateException | khối lệnh | 660 | 220 | 320 | 80 |
| N11 | Còn chỗ chưa duyệt (theo mã chỗ tăng dần)? | quyết định | 120 | 370 | 360 | 140 |
| N12 | seat.markHeld() ném SeatsUnavailableException? | quyết định | 120 | 550 | 360 | 140 |
| N13 | holdStartedAt = now; holdExpiry = now + HOLD_DURATION; seatFare = seatFare; status = HOLDING | khối lệnh | 140 | 760 | 320 | 80 |
| N14 | Kết thúc | kết thúc | 280 | 960 | 40 | 40 |
| N15 | Ném SeatsUnavailableException (ngoại lệ lan ra) | khối lệnh | 660 | 580 | 320 | 80 |

Bảng cạnh (cột Điểm uốn theo Conventions C7.1; "-" là đi thẳng):

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) | Điểm uốn |
|---|---|---|---|---|
| CE9 | N8 | N9 | - | - |
| CE10 | N9 | N10 | Đúng | - |
| CE11 | N9 | N11 | Sai | - |
| CE12 | N11 | N12 | Đúng | - |
| CE13 | N12 | N15 | Đúng | - |
| CE14 | N12 | N11 | Sai | (80,620); (80,440) |
| CE15 | N11 | N13 | Sai | (540,440); (540,800) |
| CE16 | N13 | N14 | - | - |
| CE17 | N10 | N14 | - | (1040,260); (1040,980) |
| CE18 | N15 | N14 | - | (1040,620); (1040,980) |

V(G) = E - N + 2 = 10 - 8 + 2 = 4; kiểm tra bằng số quyết định nhị phân + 1 = 3 + 1 = 4 (quyết định: N9, N11, N12). Số đường đi cơ sở độc lập: 4.

Đường đi cơ sở:

- ĐĐ1: N8-N9-N10-N14 (status khác SELECTING)
- ĐĐ2: N8-N9-N11-N12-N15-N14 (chỗ đầu tiên không AVAILABLE)
- ĐĐ3: N8-N9-N11-N12-N11-N13-N14 (một chỗ, giữ thành công)
- ĐĐ4: N8-N9-N11-N12-N11-N12-N11-N13-N14 (hai chỗ, giữ thành công)

Đường a b d f g (không duyệt chỗ nào) không khả thi vì lần đặt luôn có ít nhất một chỗ (createBooking từ chối danh sách rỗng).

Bảng phủ nhánh (mọi N có ít nhất một cạnh vào hoặc ra nên phủ hết cạnh thì phủ hết N):

| Nhánh (CE) | TC phủ |
|---|---|
| CE9 (N8 --> N9) | TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-019, TC-020, TC-021 |
| CE10 (N9 --> N10, Đúng) | TC-019, TC-020, TC-021 |
| CE11 (N9 --> N11, Sai) | TC-012, TC-013, TC-014, TC-015, TC-016, TC-017 |
| CE12 (N11 --> N12, Đúng) | TC-012, TC-013, TC-014, TC-015, TC-016, TC-017 |
| CE13 (N12 --> N15, Đúng) | TC-016, TC-017 |
| CE14 (N12 --> N11, Sai) | TC-012, TC-013, TC-014, TC-015 |
| CE15 (N11 --> N13, Sai) | TC-012, TC-013, TC-014, TC-015 |
| CE16 (N13 --> N14) | TC-012, TC-013, TC-014, TC-015 |
| CE17 (N10 --> N14) | TC-019, TC-020, TC-021 |
| CE18 (N15 --> N14) | TC-016, TC-017 |

Độ phủ đạt được: C0 = 8/8 lệnh (node) = 100%; C1 = 10/10 nhánh (cạnh) = 100%.

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-holdSeats.drawio (ID cell trùng N, CE).

Vòng lặp (duyệt các chỗ của lần đặt, n = 5 theo BR-01, m = 2):

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Duyệt chỗ trong holdSeats (N11) | 5 | 2 | 0: không xảy ra (lần đặt có ít nhất 1 chỗ); 1: có; m = 2: có; n-1 = 4: có; n = 5: có; n+1 = 6: vi phạm tiền điều kiện, ASM-57, không có TC | 1 chỗ: TC-013; 2 chỗ: TC-012; 4 chỗ: TC-014; 5 chỗ: TC-015 |

F2.4.7. Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat | Dùng bản thật (không giả lập) | Seat(trip, seatCode) tạo chỗ AVAILABLE; markHeld, markSold thiết lập HELD, SOLD cho điều kiện đầu | Entity thuần, không truy cập ngoài; quan sát được trạng thái bằng getTripState() |
| DC-Trip | Dùng bản thật | Trip T1 theo quy ước dữ liệu thử | Entity thuần |
| DC-Money (PKG-31, chưa có P12) | Fake | Giá trị tiền 250.000 đồng, so sánh bằng toBigDecimal() | Lớp chưa hiện thực; chữ ký tạm trong P12 |

### F2.5 DC-Booking.isHoldExpired

F2.5.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isHoldExpired(now: LocalDateTime): boolean | P12 F2 |
| Tiền điều kiện | Không | P12 F2 |
| Hậu điều kiện | true khi holdExpiry có giá trị và now >= holdExpiry (BR-03); không đổi trạng thái | P12 F2 |
| Ngoại lệ | Không | P12 F2 |
| BR | BR-03 hết 10 phút mà chưa thanh toán thành công thì chỗ được trả lại; thời hạn tính từ lúc giữ chỗ (ASM-18) | P06 Mục 6; P04 UC-009 mục 6, 8 |
| Luồng thay thế | UC-009 5a hết thời hạn giữ chỗ | P04 UC-009 mục 3 |

Không áp dụng: F2.5.5 (không là sự kiện của state machine), F2.5.6 (không có thiết kế method ở P12 F3 và không có mã nguồn; C0, C1 đo khi có mã nguồn), F2.5.7 (không có phụ thuộc ngoài).

F2.5.2. Phân vùng tương đương (theo đầu ra; "Hợp lệ" là lớp false, tức chưa hết hạn; "Không hợp lệ" là lớp true, tức đã hết hạn). Điều kiện đầu holdExpiry = 2026-12-14T20:10:00 (giữ chỗ lúc 20:00).

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-29 | holdExpiry và now | holdExpiry có giá trị và now < holdExpiry | Hợp lệ (false) | now = 2026-12-14T20:09:59 | BR-03 |
| EC-30 | holdExpiry và now | holdExpiry có giá trị và now >= holdExpiry | Không hợp lệ (true) | now = 2026-12-14T20:10:00 | BR-03 |
| EC-31 | holdExpiry | holdExpiry rỗng (đã trả chỗ hoặc dừng chờ) | Hợp lệ (false) | Booking SEATS_RELEASED | P12 F2 hậu điều kiện; F6 ST-03 chuyển 6 |
| EC-32 | now | now = null | Không hợp lệ | null | ASM-57 (không có TC) |

F2.5.3. Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-12 | max của EC-29 | now = 2026-12-14T20:09:59 | EC-29 | false |
| BV-13 | min của EC-30 | now = 2026-12-14T20:10:00 | EC-30 | true |

F2.5.4. Bảng quyết định (C1: holdExpiry có giá trị; C2: now >= holdExpiry)

```text
| Điều kiện / Hành động | DT3-R1 | DT3-R2 | DT3-R3 |
| C1: holdExpiry có giá trị | Y | Y | N |
| C2: now >= holdExpiry | Y | N | - |
| A1: trả true | X | - | - |
| A2: trả false | - | X | X |
```

DT3-R3 gộp hai quy tắc (N, Y) và (N, N) vì khi holdExpiry rỗng phép so sánh không xác định và F2 hậu điều kiện viết "holdExpiry có giá trị và now >= holdExpiry" (phép AND, kết quả false bất kể C2); căn cứ P12 F2 DC-Booking.isHoldExpired.

### F2.6 DC-Booking.recordTravelerInfo

F2.6.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | recordTravelerInfo(travelerName: String, travelerPhone: String, now: LocalDateTime): void; hai chuỗi là họ tên và số điện thoại người đi do hành khách nhập (ASM-19) | P12 F2 |
| Tiền điều kiện | status = HOLDING và chưa tới holdExpiry | P12 F2 |
| Hậu điều kiện | travelerName, travelerPhone đã ghi (họ tên đã cắt khoảng trắng hai đầu; số điện thoại đã bỏ khoảng trắng, dấu chấm, dấu gạch ngang); status vẫn HOLDING | P12 F2; F3 bước 4; bảng Chữ ký interface tạm DC-PhoneNumber.of |
| Ngoại lệ | TravelerInfoMissingException (7a), HoldExpiredException (5a, và khi status là SEATS_RELEASED), IllegalStateException (SELECTING, TICKETS_ISSUED) | P12 F2; F6 ST-03 sự kiện bị từ chối |
| BR | BR-03 thời hạn giữ chỗ | P06 Mục 6 |
| Luồng thay thế | UC-009 5a hết thời hạn giữ chỗ trong bước 6 đến 8; 7a chưa cung cấp họ tên hoặc số điện thoại | P04 UC-009 mục 3 |
| Điều kiện hợp lệ | Họ tên và số điện thoại bắt buộc; điều kiện hợp lệ khác chưa quy định (Q-44); họ tên tối đa 100 ký tự (ASM-52, P13 traveler_name VARCHAR(100)) | P04 UC-009 Dữ liệu vào 2; P12 F7; P13 F6.1 |
| Chuyển trạng thái | ST-03: Holding --> Holding khi recordTravelerInfo [now < holdExpiry và đã có họ tên, số điện thoại] | P12 F6 ST-03 chuyển 3 |

F2.6.2. Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-33 | status của Booking | HOLDING | Hợp lệ | HOLDING | P12 F2 |
| EC-34 | status của Booking | SEATS_RELEASED | Không hợp lệ (HoldExpiredException) | SEATS_RELEASED | P12 F6 ST-03 |
| EC-35 | status của Booking | SELECTING | Không hợp lệ (IllegalStateException) | SELECTING | P12 F6 ST-03 |
| EC-36 | status của Booking | TICKETS_ISSUED | Không hợp lệ (IllegalStateException) | TICKETS_ISSUED | P12 F6 ST-03 |
| EC-37 | now (khi status = HOLDING, holdExpiry = 2026-12-14T20:10:00) | now < holdExpiry | Hợp lệ | 2026-12-14T20:05:00 | BR-03 |
| EC-38 | now | now >= holdExpiry | Không hợp lệ (HoldExpiredException, 5a) | 2026-12-14T20:10:00 | BR-03; UC-009 5a |
| EC-39 | travelerName | còn từ 1 đến 100 ký tự sau khi cắt khoảng trắng hai đầu | Hợp lệ | "Nguyễn Văn An" | UC-009 Dữ liệu vào 2; ASM-52 |
| EC-40 | travelerName | rỗng hoặc chỉ gồm khoảng trắng (0 ký tự sau khi cắt) | Không hợp lệ (TravelerInfoMissingException, 7a) | "", "   " | UC-009 7a; P12 F3 bước 3 |
| EC-41 | travelerName | null, hoặc dài hơn 100 ký tự | Không hợp lệ (P12 không nêu hành vi) | null; chuỗi 101 ký tự | ASM-57 (không có TC) |
| EC-42 | travelerPhone | sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang còn ít nhất một ký tự và chỉ gồm chữ số | Hợp lệ | "0912345678", "091-234.5678" | UC-009 Dữ liệu vào 2; DC-PhoneNumber.of (chữ ký tạm) |
| EC-43 | travelerPhone | rỗng sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang | Không hợp lệ (TravelerInfoMissingException, 7a) | "", " . - " | UC-009 7a; P12 F3 bước 3 |
| EC-44 | travelerPhone | null, hoặc còn ký tự khác chữ số sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang | Không hợp lệ (điều kiện hợp lệ khác chờ Q-44; P12 không nêu hành vi) | null; "09123abc" | ASM-57, Q-44 (không có TC) |

F2.6.3. Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-14 | max của EC-37 | now = 2026-12-14T20:09:59 | EC-37 | Ghi thành công |
| BV-15 | min của EC-38 | now = 2026-12-14T20:10:00 | EC-38 | HoldExpiredException; họ tên, số điện thoại không được ghi |
| BV-16 | max của EC-40 (độ dài 0) | travelerName = "" | EC-40 | TravelerInfoMissingException |
| BV-17 | min của EC-39 (độ dài 1 sau khi cắt) | travelerName = " A " | EC-39 | Ghi thành công, họ tên = "A" |

F2.6.4. Bảng quyết định (cho Booking ở trạng thái HOLDING; C1: now < holdExpiry; C2: họ tên đã cung cấp; C3: số điện thoại đã cung cấp)

```text
| Điều kiện / Hành động | DT4-R1 | DT4-R2 | DT4-R3 | DT4-R4 | DT4-R5 |
| C1: now < holdExpiry | Y | Y | Y | Y | N |
| C2: họ tên đã cung cấp | Y | Y | N | N | - |
| C3: số điện thoại đã cung cấp | Y | N | Y | N | - |
| A1: ghi họ tên, số điện thoại | X | - | - | - | - |
| A2: ném TravelerInfoMissingException | - | X | X | X | - |
| A3: ném HoldExpiredException | - | - | - | - | X |
```

DT4-R5 gộp bốn quy tắc (N, *, *): kiểm tra hết thời hạn giữ chỗ đứng trước kiểm tra họ tên, số điện thoại ở P12 F3 bước 2 và bước 3, F2 và P04 UC-009 (5a, 7a) không nêu thứ tự và không mâu thuẫn; căn cứ gộp: P12 F3 DC-Booking.recordTravelerInfo bước 2 trước bước 3. DT4-R4 (cả hai thiếu) cho cùng một ngoại lệ với DT4-R2, DT4-R3 nên không cần phân biệt thiếu trường nào. Điều kiện ghép (họ tên rỗng hoặc số điện thoại rỗng) hiện thực luồng 7a nên mỗi điều kiện con nhận cả hai giá trị: họ tên rỗng ở TC-029, TC-030, họ tên có giá trị ở TC-028; số điện thoại rỗng ở TC-028, TC-030, có giá trị ở TC-029.

F2.6.5. Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Holding | recordTravelerInfo(name, phone, now) | [now < holdExpiry và đã có họ tên, số điện thoại] đúng (biên 20:09:59) | Không ngoại lệ | Holding; họ tên, số điện thoại đã ghi | ST-03 chuyển 3 |
| Holding | recordTravelerInfo | [now < holdExpiry] sai (biên 20:10:00) | HoldExpiredException | Holding; họ tên, số điện thoại chưa ghi | ST-03 sự kiện bị từ chối dòng 1 |
| Holding | recordTravelerInfo | [đã có họ tên, số điện thoại] sai | TravelerInfoMissingException | Holding; họ tên, số điện thoại chưa ghi | ST-03 sự kiện bị từ chối dòng 2 |
| Selecting | recordTravelerInfo | không có chuyển | IllegalStateException | Selecting không đổi | ST-03 sự kiện bị từ chối dòng 5 |
| SeatsReleased | recordTravelerInfo | không có chuyển | HoldExpiredException | SeatsReleased không đổi | ST-03 sự kiện bị từ chối dòng 6 |
| TicketsIssued | recordTravelerInfo | không có chuyển | IllegalStateException | TicketsIssued không đổi | ST-03 sự kiện bị từ chối dòng 8 |

F2.6.6. Hộp trắng (thiết kế method: P12 F3 DC-Booking.recordTravelerInfo(String, String, LocalDateTime))

Bảng node (nguồn chuẩn của sơ đồ X2-cfg-DC-Booking-recordTravelerInfo.drawio; x, y, w, h là toạ độ góc trên trái và kích thước):

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) | x | y | w | h |
|---|---|---|---|---|---|---|
| N16 | Bắt đầu | bắt đầu | 280 | 60 | 40 | 40 |
| N17 | status = SEATS_RELEASED? | quyết định | 120 | 190 | 360 | 140 |
| N18 | Ném HoldExpiredException (chỗ đã trả) | khối lệnh | 660 | 220 | 320 | 80 |
| N19 | status khác HOLDING? | quyết định | 120 | 370 | 360 | 140 |
| N20 | Ném IllegalStateException | khối lệnh | 660 | 400 | 320 | 80 |
| N21 | isHoldExpired(now)? | quyết định | 120 | 550 | 360 | 140 |
| N22 | Ném HoldExpiredException (luồng 5a) | khối lệnh | 660 | 580 | 320 | 80 |
| N23 | travelerName rỗng sau khi cắt khoảng trắng? | quyết định | 120 | 730 | 360 | 140 |
| N24 | travelerPhone rỗng sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang? | quyết định | 120 | 910 | 360 | 140 |
| N25 | Ném TravelerInfoMissingException (luồng 7a) | khối lệnh | 660 | 760 | 320 | 80 |
| N26 | travelerName = tên đã cắt khoảng trắng; travelerPhone = PhoneNumber.of(chuỗi đã chuẩn hoá) | khối lệnh | 140 | 1120 | 320 | 80 |
| N27 | Kết thúc | kết thúc | 280 | 1320 | 40 | 40 |

Bảng cạnh (cột Điểm uốn theo Conventions C7.1; "-" là đi thẳng):

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) | Điểm uốn |
|---|---|---|---|---|
| CE19 | N16 | N17 | - | - |
| CE20 | N17 | N18 | Đúng | - |
| CE21 | N17 | N19 | Sai | - |
| CE22 | N19 | N20 | Đúng | - |
| CE23 | N19 | N21 | Sai | - |
| CE24 | N21 | N22 | Đúng | - |
| CE25 | N21 | N23 | Sai | - |
| CE26 | N23 | N25 | Đúng | - |
| CE27 | N23 | N24 | Sai | - |
| CE28 | N24 | N25 | Đúng | (820,980) |
| CE29 | N24 | N26 | Sai | - |
| CE30 | N26 | N27 | - | - |
| CE31 | N18 | N27 | - | (1040,260); (1040,1340) |
| CE32 | N20 | N27 | - | (1040,440); (1040,1340) |
| CE33 | N22 | N27 | - | (1040,620); (1040,1340) |
| CE34 | N25 | N27 | - | (1040,800); (1040,1340) |

V(G) = E - N + 2 = 16 - 12 + 2 = 6; kiểm tra bằng số quyết định nhị phân + 1 = 5 + 1 = 6 (quyết định: N17, N19, N21, N23, N24). Số đường đi cơ sở độc lập: 6.

Đường đi cơ sở:

- ĐĐ1: N16-N17-N18-N27 (SEATS_RELEASED)
- ĐĐ2: N16-N17-N19-N20-N27 (status SELECTING hoặc TICKETS_ISSUED)
- ĐĐ3: N16-N17-N19-N21-N22-N27 (hết thời hạn giữ chỗ (5a))
- ĐĐ4: N16-N17-N19-N21-N23-N25-N27 (họ tên thiếu (7a))
- ĐĐ5: N16-N17-N19-N21-N23-N24-N25-N27 (họ tên có, số điện thoại thiếu (7a))
- ĐĐ6: N16-N17-N19-N21-N23-N24-N26-N27 (ghi họ tên và số điện thoại)

Bảng phủ nhánh (mọi N có ít nhất một cạnh vào hoặc ra nên phủ hết cạnh thì phủ hết N):

| Nhánh (CE) | TC phủ |
|---|---|
| CE19 (N16 --> N17) | TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-033, TC-034 |
| CE20 (N17 --> N18, Đúng) | TC-033 |
| CE21 (N17 --> N19, Sai) | TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031, TC-032, TC-034 |
| CE22 (N19 --> N20, Đúng) | TC-032, TC-034 |
| CE23 (N19 --> N21, Sai) | TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031 |
| CE24 (N21 --> N22, Đúng) | TC-026, TC-027 |
| CE25 (N21 --> N23, Sai) | TC-025, TC-028, TC-029, TC-030, TC-031 |
| CE26 (N23 --> N25, Đúng) | TC-029, TC-030 |
| CE27 (N23 --> N24, Sai) | TC-025, TC-028, TC-031 |
| CE28 (N24 --> N25, Đúng) | TC-028 |
| CE29 (N24 --> N26, Sai) | TC-025, TC-031 |
| CE30 (N26 --> N27) | TC-025, TC-031 |
| CE31 (N18 --> N27) | TC-033 |
| CE32 (N20 --> N27) | TC-032, TC-034 |
| CE33 (N22 --> N27) | TC-026, TC-027 |
| CE34 (N25 --> N27) | TC-028, TC-029, TC-030 |

Độ phủ đạt được: C0 = 12/12 lệnh (node) = 100%; C1 = 16/16 nhánh (cạnh) = 100%.

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-recordTravelerInfo.drawio (ID cell trùng N, CE).

Vòng lặp: không có.

F2.6.7. Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-PhoneNumber (PKG-31, chưa có P12) | Fake | PhoneNumber.of(chuỗi) trả đối tượng có value() là chuỗi đã bỏ khoảng trắng, dấu chấm, dấu gạch ngang | Lớp chưa hiện thực; chữ ký tạm trong P12; kiểm tra value() = "0912345678" |
| DC-Seat, DC-Trip | Dùng bản thật | Chuẩn bị Booking HOLDING qua createBooking, holdSeats | Entity thuần |
| DC-Money (PKG-31) | Fake | seatFare = 250.000 đồng khi chuẩn bị holdSeats | Lớp chưa hiện thực |

### F2.7 DC-Booking.releaseHeldSeats

F2.7.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | releaseHeldSeats(): void; dùng chung cho thanh toán thất bại, hết thời hạn, hành khách huỷ (ASM-24) | P12 F2 |
| Tiền điều kiện | status = HOLDING hoặc SEATS_RELEASED | P12 F2 |
| Hậu điều kiện | status = SEATS_RELEASED; mọi Seat AVAILABLE; holdExpiry rỗng | P12 F2 |
| Ngoại lệ | IllegalStateException khi status là SELECTING hoặc TICKETS_ISSUED | P12 F2 |
| BR | BR-03 hết thời hạn thì chỗ trả lại cho người khác | P06 Mục 6 |
| Luồng thay thế | UC-009 5a (hết thời hạn), 8a (thanh toán thất bại), *a (hành khách huỷ): trả lại chỗ đang giữ | P04 UC-009 mục 3 |
| Chuyển trạng thái | ST-03: Holding --> SeatsReleased; SeatsReleased --> SeatsReleased (bỏ qua); ST-02: Held --> Available cho từng chỗ | P12 F6 ST-03 chuyển 6, 8; ST-02 chuyển 4 |

Không áp dụng: F2.7.4 (kết quả chỉ phụ thuộc status, đã phủ bằng F2.7.5).

F2.7.2. Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-45 | status của Booking | HOLDING | Hợp lệ (trả chỗ) | HOLDING | P12 F2 |
| EC-46 | status của Booking | SEATS_RELEASED | Hợp lệ (không làm gì) | SEATS_RELEASED | P12 F2; F6 ST-03 chuyển 8 |
| EC-47 | status của Booking | SELECTING | Không hợp lệ (IllegalStateException) | SELECTING | P12 F2 |
| EC-48 | status của Booking | TICKETS_ISSUED | Không hợp lệ (IllegalStateException) | TICKETS_ISSUED | P12 F2 |
| EC-49 | số chỗ n khi HOLDING | 1 <= n <= 5 | Hợp lệ | 2 | BR-01 |
| EC-50 | số chỗ n khi HOLDING | n = 0 hoặc n >= 6 | Không thể xảy ra: createBooking từ chối danh sách rỗng, holdSeats yêu cầu số chỗ <= 5 | - | P12 F2 (không có TC) |

F2.7.3. Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-18 | min của EC-49 | n = 1 | EC-49 | 1 chỗ AVAILABLE, status SEATS_RELEASED |
| BV-19 | max - 1 của EC-49 | n = 4 | EC-49 | 4 chỗ AVAILABLE |
| BV-20 | max của EC-49 | n = 5 | EC-49 | 5 chỗ AVAILABLE |

F2.7.5. Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Holding | releaseHeldSeats | không có guard | Không ngoại lệ; mọi chỗ AVAILABLE | SeatsReleased; holdExpiry rỗng | ST-03 chuyển 6 |
| SeatsReleased | releaseHeldSeats | không có guard | Không ngoại lệ, không đổi gì | SeatsReleased không đổi | ST-03 chuyển 8 |
| Selecting | releaseHeldSeats | không có chuyển | IllegalStateException | Selecting không đổi | ST-03 sự kiện bị từ chối dòng 5 |
| TicketsIssued | releaseHeldSeats | không có chuyển | IllegalStateException | TicketsIssued không đổi; chỗ vẫn SOLD | ST-03 sự kiện bị từ chối dòng 8 |

F2.7.6. Hộp trắng (thiết kế method: P12 F3 DC-Booking.releaseHeldSeats())

Bảng node (nguồn chuẩn của sơ đồ X2-cfg-DC-Booking-releaseHeldSeats.drawio; x, y, w, h là toạ độ góc trên trái và kích thước):

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) | x | y | w | h |
|---|---|---|---|---|---|---|
| N28 | Bắt đầu | bắt đầu | 280 | 60 | 40 | 40 |
| N29 | status = SEATS_RELEASED? | quyết định | 120 | 190 | 360 | 140 |
| N30 | Kết thúc, không làm gì | khối lệnh | 660 | 220 | 320 | 80 |
| N31 | status khác HOLDING? | quyết định | 120 | 370 | 360 | 140 |
| N32 | Ném IllegalStateException | khối lệnh | 660 | 400 | 320 | 80 |
| N33 | Còn chỗ chưa duyệt? | quyết định | 120 | 550 | 360 | 140 |
| N34 | seat.markAvailable() | khối lệnh | 140 | 760 | 320 | 80 |
| N35 | status = SEATS_RELEASED; holdExpiry = rỗng | khối lệnh | 140 | 940 | 320 | 80 |
| N36 | Kết thúc | kết thúc | 280 | 1140 | 40 | 40 |

Bảng cạnh (cột Điểm uốn theo Conventions C7.1; "-" là đi thẳng):

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) | Điểm uốn |
|---|---|---|---|---|
| CE35 | N28 | N29 | - | - |
| CE36 | N29 | N30 | Đúng | - |
| CE37 | N29 | N31 | Sai | - |
| CE38 | N31 | N32 | Đúng | - |
| CE39 | N31 | N33 | Sai | - |
| CE40 | N33 | N34 | Đúng | - |
| CE41 | N34 | N33 | - | (80,800); (80,620) |
| CE42 | N33 | N35 | Sai | (540,620); (540,980) |
| CE43 | N35 | N36 | - | - |
| CE44 | N30 | N36 | - | (1040,260); (1040,1160) |
| CE45 | N32 | N36 | - | (1040,440); (1040,1160) |

V(G) = E - N + 2 = 11 - 9 + 2 = 4; kiểm tra bằng số quyết định nhị phân + 1 = 3 + 1 = 4 (quyết định: N29, N31, N33). Số đường đi cơ sở độc lập: 4.

Đường đi cơ sở:

- ĐĐ1: N28-N29-N30-N36 (đã SEATS_RELEASED, bỏ qua)
- ĐĐ2: N28-N29-N31-N32-N36 (status SELECTING hoặc TICKETS_ISSUED)
- ĐĐ3: N28-N29-N31-N33-N34-N33-N35-N36 (một chỗ)
- ĐĐ4: N28-N29-N31-N33-N34-N33-N34-N33-N35-N36 (hai chỗ)

Bảng phủ nhánh (mọi N có ít nhất một cạnh vào hoặc ra nên phủ hết cạnh thì phủ hết N):

| Nhánh (CE) | TC phủ |
|---|---|
| CE35 (N28 --> N29) | TC-035, TC-036, TC-037, TC-038, TC-039, TC-040, TC-041 |
| CE36 (N29 --> N30, Đúng) | TC-039 |
| CE37 (N29 --> N31, Sai) | TC-035, TC-036, TC-037, TC-038, TC-040, TC-041 |
| CE38 (N31 --> N32, Đúng) | TC-040, TC-041 |
| CE39 (N31 --> N33, Sai) | TC-035, TC-036, TC-037, TC-038 |
| CE40 (N33 --> N34, Đúng) | TC-035, TC-036, TC-037, TC-038 |
| CE41 (N34 --> N33) | TC-035, TC-036, TC-037, TC-038 |
| CE42 (N33 --> N35, Sai) | TC-035, TC-036, TC-037, TC-038 |
| CE43 (N35 --> N36) | TC-035, TC-036, TC-037, TC-038 |
| CE44 (N30 --> N36) | TC-039 |
| CE45 (N32 --> N36) | TC-040, TC-041 |

Độ phủ đạt được: C0 = 9/9 lệnh (node) = 100%; C1 = 11/11 nhánh (cạnh) = 100%.

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-releaseHeldSeats.drawio (ID cell trùng N, CE).

Vòng lặp (duyệt chỗ trong releaseHeldSeats, n = 5, m = 2):

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Duyệt chỗ trong releaseHeldSeats (N33) | 5 | 2 | 0: không xảy ra (Booking HOLDING có ít nhất 1 chỗ); 1: có; m = 2: có; n-1 = 4: có; n = 5: có; n+1 = 6: không thể xảy ra ở HOLDING (holdSeats yêu cầu số chỗ <= 5) | 1 chỗ: TC-035; 2 chỗ: TC-036; 4 chỗ: TC-037; 5 chỗ: TC-038 |

F2.7.7. Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Seat, DC-Trip | Dùng bản thật | Chuẩn bị Booking HOLDING, TICKETS_ISSUED qua các operation công khai; đọc getTripState() | Entity thuần |
| DC-Money, DC-TicketCode, DC-PaymentTransaction | Fake (Money, TicketCode), dummy (PaymentTransaction) | Chỉ dùng khi chuẩn bị Booking TICKETS_ISSUED ở TC-041 | Lớp thuộc PKG-29, PKG-31 chưa hiện thực |

### F2.8 DC-Booking.issueTickets

F2.8.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | issueTickets(ticketCodes: List<TicketCode>, transaction: PaymentTransaction): List<Ticket>; ticketCodes là các mã vé đã cấp, đủ số chỗ; transaction là giao dịch thu tiền thành công | P12 F2 |
| Tiền điều kiện | status = HOLDING; ticketCodes có số phần tử bằng số chỗ (BR-04) | P12 F2 |
| Hậu điều kiện | status = TICKETS_ISSUED; mọi Seat SOLD; holdExpiry rỗng; kết quả là các Ticket ISSUED, mỗi vé có fare = seatFare, kênh trực tuyến, đã thanh toán, mang họ tên, số điện thoại người đi, giao dịch thanh toán và mã vé riêng; vé thứ i (theo mã chỗ tăng dần) mang mã vé thứ i. purchaseChannel và paymentStatus của vé không có getter nên không quan sát được trực tiếp (xem Đề xuất sửa artifact trước) | P12 F2, F3; P04 UC-009 Dữ liệu ra 1 (mã vé và chỗ cùng thứ tự) |
| Ngoại lệ | HoldExpiredException khi SEATS_RELEASED; IllegalArgumentException khi số mã vé khác số chỗ; IllegalStateException cho status khác (SELECTING, TICKETS_ISSUED) | P12 F2; F6 ST-03 |
| BR | BR-04 mỗi chỗ có một mã vé | P06 Mục 6; P04 UC-009 mục 6 |
| Luồng thay thế | UC-009 5a (đã trả chỗ vì hết thời hạn); luồng chính bước 9 | P04 UC-009 mục 2, 3 |
| Chuyển trạng thái | ST-03: Holding --> TicketsIssued khi issueTickets [số mã vé = số chỗ] | P12 F6 ST-03 chuyển 5 |

F2.8.2. Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-51 | status của Booking | HOLDING (đã ghi người đi) | Hợp lệ | HOLDING | P12 F2 |
| EC-52 | status của Booking | SEATS_RELEASED | Không hợp lệ (HoldExpiredException) | SEATS_RELEASED | P12 F6 ST-03 |
| EC-53 | status của Booking | SELECTING | Không hợp lệ (IllegalStateException) | SELECTING | P12 F6 ST-03 |
| EC-54 | status của Booking | TICKETS_ISSUED | Không hợp lệ (IllegalStateException) | TICKETS_ISSUED | P12 F6 ST-03 |
| EC-55 | ticketCodes.size() so với số chỗ | bằng số chỗ | Hợp lệ | 2 mã cho 2 chỗ | BR-04 |
| EC-56 | ticketCodes.size() so với số chỗ | nhỏ hơn số chỗ (kể cả danh sách rỗng) | Không hợp lệ (IllegalArgumentException) | 1 mã cho 2 chỗ | BR-04; P12 F2 |
| EC-57 | ticketCodes.size() so với số chỗ | lớn hơn số chỗ | Không hợp lệ (IllegalArgumentException) | 3 mã cho 2 chỗ | BR-04; P12 F2 |
| EC-58 | ticketCodes, transaction, thông tin người đi | ticketCodes = null, transaction = null, hoặc Booking HOLDING chưa ghi người đi (recordTravelerInfo chưa gọi) | Không hợp lệ (P12 không nêu hành vi) | null; HOLDING chưa ghi người đi | ASM-57 (không có TC) |
| EC-59 | số chỗ n | 1 <= n <= 5 | Hợp lệ | 2 | BR-01 |

F2.8.3. Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-21 | max của EC-56 (size = số chỗ - 1) | 2 chỗ, 1 mã vé | EC-56 | IllegalArgumentException; Booking vẫn HOLDING, chỗ vẫn HELD |
| BV-22 | EC-55 (size = số chỗ) | 2 chỗ, 2 mã vé | EC-55 | Phát hành 2 vé |
| BV-23 | min của EC-57 (size = số chỗ + 1) | 2 chỗ, 3 mã vé | EC-57 | IllegalArgumentException; Booking vẫn HOLDING, chỗ vẫn HELD |
| BV-24 | min của EC-59 | n = 1 | EC-59 | Phát hành 1 vé |
| BV-25 | max - 1 của EC-59 | n = 4 | EC-59 | Phát hành 4 vé |
| BV-26 | max của EC-59 | n = 5 | EC-59 | Phát hành 5 vé |

F2.8.4. Bảng quyết định (C1: status = HOLDING; C2: số mã vé = số chỗ)

```text
| Điều kiện / Hành động | DT5-R1 | DT5-R2 | DT5-R3 |
| C1: status = HOLDING | Y | Y | N |
| C2: số mã vé = số chỗ | Y | N | - |
| A1: phát hành vé (TICKETS_ISSUED, chỗ SOLD) | X | - | - |
| A2: ném IllegalArgumentException | - | X | - |
| A3: ném HoldExpiredException (SEATS_RELEASED) hoặc IllegalStateException (SELECTING, TICKETS_ISSUED) | - | - | X |
```

DT5-R3 gộp hai quy tắc (N, Y) và (N, N): P12 F3 bước 1 kiểm tra status trước số mã vé, F6 ST-03 bảng sự kiện bị từ chối xét status của lần đặt cho issueTickets mà không xét số mã vé, F2 và P04 không mâu thuẫn; căn cứ gộp: P12 F3 bước 1 trước bước 2 và P12 F6 ST-03. Ngoại lệ cụ thể theo status được phân biệt ở F2.8.5.

F2.8.5. Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Holding | issueTickets(codes, transaction) | [số mã vé = số chỗ] đúng (biên size = n) | Trả n vé ISSUED | TicketsIssued; chỗ SOLD; holdExpiry rỗng | ST-03 chuyển 5 |
| Holding | issueTickets(codes, transaction) | [số mã vé = số chỗ] sai (size = n - 1 và size = n + 1) | IllegalArgumentException | Holding không đổi; chỗ vẫn HELD | P12 F2 ngoại lệ |
| SeatsReleased | issueTickets | không có chuyển | HoldExpiredException | SeatsReleased không đổi | ST-03 sự kiện bị từ chối dòng 6 |
| Selecting | issueTickets | không có chuyển | IllegalStateException | Selecting không đổi | ST-03 sự kiện bị từ chối dòng 5 |
| TicketsIssued | issueTickets | không có chuyển | IllegalStateException | TicketsIssued không đổi; không phát sinh vé mới | ST-03 sự kiện bị từ chối dòng 8 |

F2.8.6. Hộp trắng (thiết kế method: P12 F3 DC-Booking.issueTickets(List<TicketCode>, PaymentTransaction))

Bảng node (nguồn chuẩn của sơ đồ X2-cfg-DC-Booking-issueTickets.drawio; x, y, w, h là toạ độ góc trên trái và kích thước):

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) | x | y | w | h |
|---|---|---|---|---|---|---|
| N37 | Bắt đầu | bắt đầu | 280 | 60 | 40 | 40 |
| N38 | status = SEATS_RELEASED? | quyết định | 120 | 190 | 360 | 140 |
| N39 | Ném HoldExpiredException | khối lệnh | 660 | 220 | 320 | 80 |
| N40 | status khác HOLDING? | quyết định | 120 | 370 | 360 | 140 |
| N41 | Ném IllegalStateException | khối lệnh | 660 | 400 | 320 | 80 |
| N42 | ticketCodes.size() khác số chỗ? | quyết định | 120 | 550 | 360 | 140 |
| N43 | Ném IllegalArgumentException | khối lệnh | 660 | 580 | 320 | 80 |
| N44 | Còn chỗ chưa xử lý (theo mã chỗ tăng dần)? | quyết định | 120 | 730 | 360 | 140 |
| N45 | Ticket.createTicket(...) cho chỗ thứ i; seat.markSold() | khối lệnh | 140 | 940 | 320 | 80 |
| N46 | status = TICKETS_ISSUED; holdExpiry = rỗng; trả danh sách vé | khối lệnh | 140 | 1120 | 320 | 80 |
| N47 | Kết thúc | kết thúc | 280 | 1320 | 40 | 40 |

Bảng cạnh (cột Điểm uốn theo Conventions C7.1; "-" là đi thẳng):

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) | Điểm uốn |
|---|---|---|---|---|
| CE46 | N37 | N38 | - | - |
| CE47 | N38 | N39 | Đúng | - |
| CE48 | N38 | N40 | Sai | - |
| CE49 | N40 | N41 | Đúng | - |
| CE50 | N40 | N42 | Sai | - |
| CE51 | N42 | N43 | Đúng | - |
| CE52 | N42 | N44 | Sai | - |
| CE53 | N44 | N45 | Đúng | - |
| CE54 | N45 | N44 | - | (80,980); (80,800) |
| CE55 | N44 | N46 | Sai | (540,800); (540,1160) |
| CE56 | N46 | N47 | - | - |
| CE57 | N39 | N47 | - | (1040,260); (1040,1340) |
| CE58 | N41 | N47 | - | (1040,440); (1040,1340) |
| CE59 | N43 | N47 | - | (1040,620); (1040,1340) |

V(G) = E - N + 2 = 14 - 11 + 2 = 5; kiểm tra bằng số quyết định nhị phân + 1 = 4 + 1 = 5 (quyết định: N38, N40, N42, N44). Số đường đi cơ sở độc lập: 5.

Đường đi cơ sở:

- ĐĐ1: N37-N38-N39-N47 (SEATS_RELEASED)
- ĐĐ2: N37-N38-N40-N41-N47 (status SELECTING hoặc TICKETS_ISSUED)
- ĐĐ3: N37-N38-N40-N42-N43-N47 (số mã vé khác số chỗ)
- ĐĐ4: N37-N38-N40-N42-N44-N45-N44-N46-N47 (một chỗ)
- ĐĐ5: N37-N38-N40-N42-N44-N45-N44-N45-N44-N46-N47 (hai chỗ)

Bảng phủ nhánh (mọi N có ít nhất một cạnh vào hoặc ra nên phủ hết cạnh thì phủ hết N):

| Nhánh (CE) | TC phủ |
|---|---|
| CE46 (N37 --> N38) | TC-042, TC-043, TC-044, TC-045, TC-046, TC-047, TC-048, TC-049, TC-050 |
| CE47 (N38 --> N39, Đúng) | TC-046 |
| CE48 (N38 --> N40, Sai) | TC-042, TC-043, TC-044, TC-045, TC-047, TC-048, TC-049, TC-050 |
| CE49 (N40 --> N41, Đúng) | TC-047, TC-048 |
| CE50 (N40 --> N42, Sai) | TC-042, TC-043, TC-044, TC-045, TC-049, TC-050 |
| CE51 (N42 --> N43, Đúng) | TC-049, TC-050 |
| CE52 (N42 --> N44, Sai) | TC-042, TC-043, TC-044, TC-045 |
| CE53 (N44 --> N45, Đúng) | TC-042, TC-043, TC-044, TC-045 |
| CE54 (N45 --> N44) | TC-042, TC-043, TC-044, TC-045 |
| CE55 (N44 --> N46, Sai) | TC-042, TC-043, TC-044, TC-045 |
| CE56 (N46 --> N47) | TC-042, TC-043, TC-044, TC-045 |
| CE57 (N39 --> N47) | TC-046 |
| CE58 (N41 --> N47) | TC-047, TC-048 |
| CE59 (N43 --> N47) | TC-049, TC-050 |

Độ phủ đạt được: C0 = 11/11 lệnh (node) = 100%; C1 = 14/14 nhánh (cạnh) = 100%.

Sơ đồ CFG: diagrams/X2-cfg-DC-Booking-issueTickets.drawio (ID cell trùng N, CE).

Vòng lặp (duyệt chỗ để tạo vé, n = 5, m = 2):

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Duyệt chỗ trong issueTickets (N44) | 5 | 2 | 0: không xảy ra (Booking HOLDING có ít nhất 1 chỗ); 1: có; m = 2: có; n-1 = 4: có; n = 5: có; n+1 = 6: không thể xảy ra ở HOLDING (holdSeats yêu cầu số chỗ <= 5) | 1 chỗ: TC-043; 2 chỗ: TC-042; 4 chỗ: TC-044; 5 chỗ: TC-045 |

F2.8.7. Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-PaymentTransaction (PKG-29, chưa có chữ ký đầy đủ) | Dummy | Một đối tượng giả; xác minh mỗi vé trả về getPaymentTransaction() là Optional chứa đúng đối tượng này | Lớp chưa hiện thực |
| DC-TicketCode (PKG-31) | Fake | TicketCode.of("SV0001"), "SV0002", ...; xác minh getTicketCode().value() theo thứ tự chỗ | Lớp chưa hiện thực; chữ ký tạm |
| DC-PhoneNumber (PKG-31) | Fake | Số điện thoại người đi đã ghi ở bước chuẩn bị | Lớp chưa hiện thực |
| DC-Money (PKG-31) | Fake | fare = 250.000 đồng | Lớp chưa hiện thực |
| DC-Seat, DC-Trip, DC-Ticket | Dùng bản thật | Ticket.createTicket tạo vé thật; Seat.markSold đổi trạng thái chỗ | Entity thuần |

### F2.9 DC-Ticket.cancelForTrip

F2.9.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | cancelForTrip(): void | P12 F2 |
| Tiền điều kiện | status = ISSUED | P12 F2 |
| Hậu điều kiện | status = CANCELLED; refundStatus = NOT_REFUNDED khi paymentStatus = PAID, ngược lại giữ NOT_APPLICABLE | P12 F2; ASM-29 (chờ Q-48) |
| Ngoại lệ | IllegalStateException khi vé không ISSUED | P12 F2 |
| BR | BR-08 hoàn tiền qua cùng kênh với kênh mua vé | P06 Mục 6 |
| Luồng thay thế | UC-017 bước 7 (chuyển vé sang Đã huỷ, ghi nhận vé đã thanh toán chưa hoàn tiền) | P04 UC-017 mục 2 |
| Chuyển trạng thái | ST-04: Issued --> CancelledRefundPending [paymentStatus = PAID]; Issued --> CancelledNoRefundDue [paymentStatus = UNPAID] | P12 F6 ST-04 chuyển 2, 3 |

Không áp dụng: F2.9.3 (không có lớp có thứ tự).

F2.9.2. Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-60 | status của vé | ISSUED | Hợp lệ | vé vừa phát hành | P12 F2 |
| EC-61 | status của vé | CANCELLED, refundStatus = NOT_REFUNDED (CancelledRefundPending) | Không hợp lệ (IllegalStateException) | vé đã cancelForTrip, paymentStatus PAID | P12 F6 ST-04 |
| EC-62 | status của vé | CANCELLED, refundStatus = REFUNDED (CancelledRefunded) | Không hợp lệ (IllegalStateException) | vé đã hoàn tiền | P12 F6 ST-04; NFR-05 |
| EC-63 | status của vé | CANCELLED, refundStatus = NOT_APPLICABLE (CancelledNoRefundDue) | Không hợp lệ (IllegalStateException) | vé UNPAID đã huỷ | P12 F6 ST-04 |
| EC-64 | paymentStatus (khi ISSUED) | PAID | Hợp lệ (refundStatus thành NOT_REFUNDED) | PAID | ASM-29 |
| EC-65 | paymentStatus (khi ISSUED) | UNPAID | Hợp lệ (refundStatus giữ NOT_APPLICABLE) | UNPAID | ASM-29 |

F2.9.4. Bảng quyết định (C1: status = ISSUED; C2: paymentStatus = PAID)

```text
| Điều kiện / Hành động | DT6-R1 | DT6-R2 | DT6-R3 |
| C1: status = ISSUED | Y | Y | N |
| C2: paymentStatus = PAID | Y | N | - |
| A1: CANCELLED, refundStatus = NOT_REFUNDED | X | - | - |
| A2: CANCELLED, refundStatus giữ NOT_APPLICABLE | - | X | - |
| A3: ném IllegalStateException | - | - | X |
```

DT6-R3 gộp hai quy tắc (N, Y) và (N, N): F2 ghi ngoại lệ "khi vé không ISSUED" độc lập với paymentStatus; căn cứ gộp: P12 F2 DC-Ticket.cancelForTrip, F3 bước 1. Ba trạng thái nguồn của DT6-R3 (EC-61, EC-62, EC-63) mỗi trạng thái một TC.

F2.9.5. Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Issued | cancelForTrip | [paymentStatus = PAID] đúng | Không ngoại lệ | CancelledRefundPending (status CANCELLED, refundStatus NOT_REFUNDED) | ST-04 chuyển 2 |
| Issued | cancelForTrip | [paymentStatus = UNPAID] | Không ngoại lệ | CancelledNoRefundDue (status CANCELLED, refundStatus NOT_APPLICABLE) | ST-04 chuyển 3 |
| CancelledRefundPending | cancelForTrip | không có chuyển | IllegalStateException | CancelledRefundPending không đổi | ST-04 sự kiện bị từ chối dòng 2 |
| CancelledRefunded | cancelForTrip | không có chuyển | IllegalStateException | CancelledRefunded không đổi | ST-04 sự kiện bị từ chối dòng 3 |
| CancelledNoRefundDue | cancelForTrip | không có chuyển | IllegalStateException | CancelledNoRefundDue không đổi | ST-04 sự kiện bị từ chối dòng 4 |

F2.9.6. Hộp trắng (thiết kế method: P12 F3 DC-Ticket.cancelForTrip())

Bảng node (nguồn chuẩn của sơ đồ X2-cfg-DC-Ticket-cancelForTrip.drawio; x, y, w, h là toạ độ góc trên trái và kích thước):

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) | x | y | w | h |
|---|---|---|---|---|---|---|
| N48 | Bắt đầu | bắt đầu | 280 | 60 | 40 | 40 |
| N49 | status khác ISSUED? | quyết định | 120 | 190 | 360 | 140 |
| N50 | Ném IllegalStateException | khối lệnh | 660 | 220 | 320 | 80 |
| N51 | status = CANCELLED | khối lệnh | 140 | 400 | 320 | 80 |
| N52 | paymentStatus = PAID? | quyết định | 120 | 550 | 360 | 140 |
| N53 | refundStatus = NOT_REFUNDED | khối lệnh | 660 | 580 | 320 | 80 |
| N54 | Kết thúc | kết thúc | 280 | 780 | 40 | 40 |

Bảng cạnh (cột Điểm uốn theo Conventions C7.1; "-" là đi thẳng):

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) | Điểm uốn |
|---|---|---|---|---|
| CE60 | N48 | N49 | - | - |
| CE61 | N49 | N50 | Đúng | - |
| CE62 | N49 | N51 | Sai | - |
| CE63 | N51 | N52 | - | - |
| CE64 | N52 | N53 | Đúng | - |
| CE65 | N52 | N54 | Sai | - |
| CE66 | N53 | N54 | - | (820,800) |
| CE67 | N50 | N54 | - | (1040,260); (1040,800) |

V(G) = E - N + 2 = 8 - 7 + 2 = 3; kiểm tra bằng số quyết định nhị phân + 1 = 2 + 1 = 3 (quyết định: N49, N52). Số đường đi cơ sở độc lập: 3.

Đường đi cơ sở:

- ĐĐ1: N48-N49-N50-N54 (vé không ISSUED)
- ĐĐ2: N48-N49-N51-N52-N54 (vé chưa thanh toán)
- ĐĐ3: N48-N49-N51-N52-N53-N54 (vé đã thanh toán)

Bảng phủ nhánh (mọi N có ít nhất một cạnh vào hoặc ra nên phủ hết cạnh thì phủ hết N):

| Nhánh (CE) | TC phủ |
|---|---|
| CE60 (N48 --> N49) | TC-051, TC-052, TC-053, TC-054, TC-055 |
| CE61 (N49 --> N50, Đúng) | TC-053, TC-054, TC-055 |
| CE62 (N49 --> N51, Sai) | TC-051, TC-052 |
| CE63 (N51 --> N52) | TC-051, TC-052 |
| CE64 (N52 --> N53, Đúng) | TC-051 |
| CE65 (N52 --> N54, Sai) | TC-052 |
| CE66 (N53 --> N54) | TC-051 |
| CE67 (N50 --> N54) | TC-053, TC-054, TC-055 |

Độ phủ đạt được: C0 = 7/7 lệnh (node) = 100%; C1 = 8/8 nhánh (cạnh) = 100%.

Sơ đồ CFG: diagrams/X2-cfg-DC-Ticket-cancelForTrip.drawio (ID cell trùng N, CE).

Vòng lặp: không có.

F2.9.7. Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Money, DC-PhoneNumber, DC-TicketCode (PKG-31) | Fake | Tham số của createTicket khi chuẩn bị vé | Lớp chưa hiện thực |
| DC-PaymentTransaction (PKG-29) | Dummy | Tham số của createTicket | Lớp chưa hiện thực |
| Bộ dựng vé UNPAID, kênh COUNTER (chỉ có ở test) | Fake (test builder) | Tạo Ticket ISSUED với paymentStatus = UNPAID, purchaseChannel = COUNTER, không giao dịch thanh toán | Không có operation công khai nào tạo vé loại này (UC-004, UC-005, UC-006 chưa có P07); xem Đề xuất sửa artifact trước |

### F2.10 DC-Ticket.isOnlineRefundPending

F2.10.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | isOnlineRefundPending(): boolean | P12 F2 |
| Tiền điều kiện | Không | P12 F2 |
| Hậu điều kiện | true khi purchaseChannel = ONLINE, paymentStatus = PAID, status = CANCELLED và refundStatus = NOT_REFUNDED (BR-08); không đổi trạng thái | P12 F2 |
| Ngoại lệ | Không | P12 F2 |
| BR | BR-08 vé mua trực tuyến hoàn qua cổng thanh toán, vé mua tại quầy hoàn tiền mặt tại quầy (ASM-08, chờ Q-07) | P06 Mục 6; P04 UC-017 mục 6 |
| Điều kiện hợp lệ của tổ hợp | Vé ONLINE luôn PAID (createTicket; P13 ck_ticket_channel_payment); vé ISSUED có refundStatus = NOT_APPLICABLE; vé CANCELLED và PAID có refundStatus NOT_REFUNDED hoặc REFUNDED; vé CANCELLED và UNPAID có refundStatus NOT_APPLICABLE | P12 F6 ST-04; P13 F6.1-b ck_ticket_state_refund, ck_ticket_channel_payment |

Không áp dụng: F2.10.3 (không có lớp có thứ tự), F2.10.5 (không là sự kiện của state machine), F2.10.6 (không có thiết kế method ở P12 F3 và không có mã nguồn; C0, C1 đo khi có mã nguồn).

F2.10.2. Phân vùng tương đương (theo đầu ra; "Hợp lệ" là lớp true, "Không hợp lệ" là lớp false)

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-66 | tổ hợp (kênh, thanh toán, trạng thái, hoàn tiền) | ONLINE, PAID, CANCELLED, NOT_REFUNDED | Hợp lệ (true) | vé trực tuyến đã huỷ chờ hoàn tiền | BR-08 |
| EC-67 | tổ hợp | ONLINE, PAID, CANCELLED, REFUNDED | Không hợp lệ (false) | vé trực tuyến đã hoàn tiền | BR-08; NFR-05 |
| EC-68 | tổ hợp | ONLINE, PAID, ISSUED (NOT_APPLICABLE) | Không hợp lệ (false) | vé trực tuyến còn hiệu lực | P12 F2 |
| EC-69 | tổ hợp | COUNTER, PAID (mọi trạng thái) | Không hợp lệ (false) | vé quầy đã thanh toán, đã huỷ, NOT_REFUNDED | BR-08 (hoàn tiền mặt tại quầy, UC-018) |
| EC-70 | tổ hợp | COUNTER, UNPAID (mọi trạng thái) | Không hợp lệ (false) | vé quầy chưa thanh toán, đã huỷ, NOT_APPLICABLE | ASM-29 |

Các tổ hợp ONLINE với UNPAID, ISSUED với refundStatus khác NOT_APPLICABLE, CANCELLED và PAID với NOT_APPLICABLE, CANCELLED và UNPAID với refundStatus khác NOT_APPLICABLE không thể xảy ra (xem điều kiện hợp lệ của tổ hợp ở F2.10.1).

F2.10.4. Bảng quyết định (C1: purchaseChannel = ONLINE; C2: paymentStatus = PAID; C3: status = CANCELLED; C4: refundStatus = NOT_REFUNDED)

```text
| Điều kiện / Hành động | DT7-R1 | DT7-R2 | DT7-R3 | DT7-R4 | DT7-R5 | DT7-R6 |
| C1: kênh = ONLINE | Y | Y | Y | N | Y | Y |
| C2: paymentStatus = PAID | Y | Y | Y | - | Y | N |
| C3: status = CANCELLED | Y | Y | N | - | N | - |
| C4: refundStatus = NOT_REFUNDED | Y | N | N | - | Y | - |
| A1: trả true | X | - | - | - | - | - |
| A2: trả false | - | X | X | X | - | - |
| N/A: không thể xảy ra | - | - | - | - | X | X |
```

DT7-R5 (ONLINE, PAID, ISSUED, NOT_REFUNDED) không thể xảy ra vì vé ISSUED luôn có refundStatus = NOT_APPLICABLE (P12 F6 ST-04). DT7-R6 gộp bốn quy tắc (ONLINE, UNPAID, *, *) không thể xảy ra vì vé ONLINE luôn PAID (P12 F2 createTicket, P13 ck_ticket_channel_payment). DT7-R4 gộp tám quy tắc (COUNTER, *, *, *) cùng cho false: hậu điều kiện F2 là phép AND thuần của bốn điều kiện, không có hành động khác nhau theo thứ tự kiểm tra, nên C1 sai là đủ cho false; căn cứ gộp: P12 F2 DC-Ticket.isOnlineRefundPending. Tổng số tổ hợp: 1 + 1 + 1 + 1 (DT7-R5) + 8 (DT7-R4) + 4 (DT7-R6) = 16 = 2^4. Vì DT7-R4 gộp, C2, C3, C4 phải nhận cả hai giá trị trong các TC của DT7-R4 để điều kiện ghép được kiểm tra đủ (Bước 4.3): TC-059 (COUNTER, PAID, CANCELLED, NOT_REFUNDED) và TC-060 (COUNTER, UNPAID, CANCELLED, NOT_APPLICABLE); C3 nhận giá trị N ở TC-058 và C4 nhận giá trị N ở TC-057, TC-058, TC-060.

F2.10.7. Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Money, DC-PhoneNumber, DC-TicketCode (PKG-31), DC-PaymentTransaction (PKG-29) | Fake, dummy | Tham số của createTicket khi chuẩn bị vé | Lớp chưa hiện thực |
| Bộ dựng vé kênh COUNTER (chỉ có ở test) | Fake (test builder) | Tạo Ticket COUNTER, PAID hoặc UNPAID; chuyển sang CANCELLED bằng cancelForTrip | Không có operation công khai tạo vé kênh quầy; xem Đề xuất sửa artifact trước |

### F2.11 DC-Ticket.calculateRefundAmount

F2.11.1. Cơ sở kiểm thử

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | calculateRefundAmount(): Money | P12 F2 |
| Tiền điều kiện | isOnlineRefundPending() = true | P12 F2 |
| Hậu điều kiện | Không đổi trạng thái; kết quả = fare (100% giá vé đã ghi, BR-07), không vượt số đã thu (NFR-06) | P12 F2 |
| Ngoại lệ | IllegalStateException khi vé không cần hoàn tiền | P12 F2 |
| BR | BR-07 số tiền hoàn cho mỗi vé của chuyến bị huỷ bằng 100% giá vé của vé đó; NFR-05 hoàn đúng một lần; NFR-06 không hoàn quá số đã thu | P06 Mục 6, Mục 3; P04 UC-017 mục 6, 7 |
| Ví dụ trong đặc tả | Giá vé 250.000 đ thì số tiền hoàn của một vé là 250.000 đ; giá vé dùng để hoàn là giá đã ghi khi bán | P04 UC-017 mục 8 |
| Điều kiện hợp lệ | fare lớn hơn 0 | P12 F7; P13 ck_ticket_fare |
| Chuyển trạng thái | calculateRefundAmount hợp lệ ở CancelledRefundPending (không đổi trạng thái); bị từ chối ở Issued, CancelledRefunded, CancelledNoRefundDue | P12 F6 ST-04 sự kiện bị từ chối |

Không áp dụng: F2.11.4 (một điều kiện tiền).

F2.11.2. Phân vùng tương đương

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-71 | trạng thái vé | thoả isOnlineRefundPending (ONLINE, PAID, CANCELLED, NOT_REFUNDED) | Hợp lệ | TK-P | P12 F2 tiền điều kiện |
| EC-72 | trạng thái vé | ISSUED | Không hợp lệ (IllegalStateException) | TK | P12 F6 ST-04 |
| EC-73 | trạng thái vé | CANCELLED, REFUNDED | Không hợp lệ (IllegalStateException) | TK-R | P12 F6 ST-04; NFR-05 |
| EC-74 | trạng thái vé | CANCELLED, không thoả isOnlineRefundPending và không REFUNDED (CancelledNoRefundDue, hoặc vé kênh COUNTER) | Không hợp lệ (IllegalStateException) | vé UNPAID đã huỷ | P12 F6 ST-04; BR-08 |
| EC-75 | fare | Money lớn hơn 0 | Hợp lệ | 250.000 đồng | P12 F7 |
| EC-76 | fare | Money nhỏ hơn hoặc bằng 0 | Không hợp lệ (P12 không nêu hành vi) | 0 | ASM-57 (không có TC) |

F2.11.3. Giá trị biên

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-27 | min của EC-75 | fare = 1 đồng | EC-75 | Số tiền hoàn = 1 đồng (100% giá vé, không làm tròn xuống 0) |

F2.11.5. Chuyển trạng thái

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| CancelledRefundPending | calculateRefundAmount | [isOnlineRefundPending] đúng | Trả fare | CancelledRefundPending không đổi | P12 F2 |
| Issued | calculateRefundAmount | không có chuyển | IllegalStateException | Issued không đổi | ST-04 sự kiện bị từ chối dòng 1 |
| CancelledRefunded | calculateRefundAmount | không có chuyển | IllegalStateException | CancelledRefunded không đổi | ST-04 sự kiện bị từ chối dòng 3 |
| CancelledNoRefundDue | calculateRefundAmount | không có chuyển | IllegalStateException | CancelledNoRefundDue không đổi | ST-04 sự kiện bị từ chối dòng 4 |

F2.11.6. Hộp trắng (thiết kế method: P12 F3 DC-Ticket.calculateRefundAmount())

Bảng node (nguồn chuẩn của sơ đồ X2-cfg-DC-Ticket-calculateRefundAmount.drawio; x, y, w, h là toạ độ góc trên trái và kích thước):

| N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) | x | y | w | h |
|---|---|---|---|---|---|---|
| N55 | Bắt đầu | bắt đầu | 280 | 60 | 40 | 40 |
| N56 | isOnlineRefundPending() sai? | quyết định | 120 | 190 | 360 | 140 |
| N57 | Ném IllegalStateException | khối lệnh | 660 | 220 | 320 | 80 |
| N58 | Trả về fare | khối lệnh | 140 | 400 | 320 | 80 |
| N59 | Kết thúc | kết thúc | 280 | 600 | 40 | 40 |

Bảng cạnh (cột Điểm uốn theo Conventions C7.1; "-" là đi thẳng):

| CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) | Điểm uốn |
|---|---|---|---|---|
| CE68 | N55 | N56 | - | - |
| CE69 | N56 | N57 | Đúng | - |
| CE70 | N56 | N58 | Sai | - |
| CE71 | N58 | N59 | - | - |
| CE72 | N57 | N59 | - | (1040,260); (1040,620) |

V(G) = E - N + 2 = 5 - 5 + 2 = 2; kiểm tra bằng số quyết định nhị phân + 1 = 1 + 1 = 2 (quyết định: N56). Số đường đi cơ sở độc lập: 2.

Đường đi cơ sở:

- ĐĐ1: N55-N56-N57-N59 (vé không cần hoàn tiền)
- ĐĐ2: N55-N56-N58-N59 (vé cần hoàn tiền)

Bảng phủ nhánh (mọi N có ít nhất một cạnh vào hoặc ra nên phủ hết cạnh thì phủ hết N):

| Nhánh (CE) | TC phủ |
|---|---|
| CE68 (N55 --> N56) | TC-061, TC-062, TC-063, TC-064, TC-065 |
| CE69 (N56 --> N57, Đúng) | TC-063, TC-064, TC-065 |
| CE70 (N56 --> N58, Sai) | TC-061, TC-062 |
| CE71 (N58 --> N59) | TC-061, TC-062 |
| CE72 (N57 --> N59) | TC-063, TC-064, TC-065 |

Độ phủ đạt được: C0 = 5/5 lệnh (node) = 100%; C1 = 5/5 nhánh (cạnh) = 100%.

Sơ đồ CFG: diagrams/X2-cfg-DC-Ticket-calculateRefundAmount.drawio (ID cell trùng N, CE).

Vòng lặp: không có.

F2.11.7. Test double

| Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| DC-Money (PKG-31) | Fake | Giá trị tiền so sánh bằng toBigDecimal(); fare 250.000 đồng và 1 đồng | Lớp chưa hiện thực |
| DC-PhoneNumber, DC-TicketCode (PKG-31), DC-PaymentTransaction (PKG-29) | Fake, dummy | Tham số của createTicket khi chuẩn bị vé | Lớp chưa hiện thực |
| Bộ dựng vé UNPAID, kênh COUNTER (chỉ có ở test) | Fake (test builder) | Chuẩn bị vé CancelledNoRefundDue ở TC-065 | Không có operation công khai tạo vé loại này |

## F3. Bảng test case

Quy ước dữ liệu thử dùng trong các TC (mỗi TC tự dựng đối tượng mới trong bước chuẩn bị, không dùng chung trạng thái giữa các TC):

- T1: Trip có departureTime = 2026-12-15T20:30:00, route = "Hà Nội - Vinh", vehicleType = SLEEPER_40, vehicle = "Xe giường nằm 40 chỗ", driver = "Trần Văn Bình"; status = SCHEDULED.
- Chỗ A01 đến A06: Seat(T1, "A01") đến Seat(T1, "A06"), trạng thái AVAILABLE. Lần đặt hai chỗ dùng A05, A06 (khớp ví dụ P04 UC-009 Dữ liệu ra 1).
- SEL(danh sách chỗ): Booking.createBooking(T1, danh sách chỗ), status SELECTING.
- FARE = Money 250.000 đồng. H0 = 2026-12-14T20:00:00 (thời điểm giữ chỗ); E0 = 2026-12-14T20:10:00 (hạn giữ chỗ tương ứng, BR-03).
- HOLD(danh sách chỗ): SEL(danh sách chỗ) sau holdSeats(FARE, H0): status HOLDING, holdExpiry = E0, các chỗ HELD.
- INFO: sau recordTravelerInfo("Nguyễn Văn An", "0912345678", 2026-12-14T20:05:00).
- REL(danh sách chỗ): HOLD sau releaseHeldSeats(): status SEATS_RELEASED, các chỗ AVAILABLE, holdExpiry rỗng.
- TX: đối tượng PaymentTransaction giả (dummy). SV000k: TicketCode.of("SV000k").
- ISS(danh sách chỗ): HOLD + INFO + issueTickets([SV0001, SV0002, ...] theo số chỗ, TX): status TICKETS_ISSUED, các chỗ SOLD.
- TK: Ticket.createTicket(T1, A05, "Nguyễn Văn An", PhoneNumber "0912345678", FARE, SV0001, TX): status ISSUED, refundStatus NOT_APPLICABLE.
- TK-P: TK sau cancelForTrip(): status CANCELLED, refundStatus NOT_REFUNDED (chờ hoàn tiền). TK-R: TK-P sau markRefunded(): refundStatus REFUNDED.
- TK-C(PAID hoặc UNPAID): vé kênh COUNTER, ISSUED, dựng bằng bộ dựng test (không có giao dịch thanh toán).
- Money so sánh bằng toBigDecimal(); thời gian so sánh bằng equals của LocalDateTime.

| TC | DC.operation | Kỹ thuật (phân vùng tương đương / giá trị biên / bảng quyết định / chuyển trạng thái / use case / đường đi) | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn (BR / UC bước) | Phủ (EC, BV, DT-R, chuyển trạng thái, nhánh CE) | Test double | Ưu tiên |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | DC-Trip.cancel | giá trị biên; bảng quyết định; đường đi | T1 status SCHEDULED | reason = VEHICLE_BREAKDOWN; now = 2026-12-15T20:29:59 | Không ngoại lệ; getStatus() = CANCELLED; getCancelReason() = Optional.of(VEHICLE_BREAKDOWN); isCancelled() = true | BR-10; UC-017 bước 5; ASM-26 (chờ Q-46); ASM-25 | BV-01, EC-01, EC-03, EC-05, DT1-R1; ST-01 chuyển 2; CE1, CE3, CE5, CE6 | Không | Cao |
| TC-002 | DC-Trip.cancel | phân vùng tương đương; đường đi | T1 status SCHEDULED | reason = BAD_WEATHER; now = 2026-12-14T09:00:00 | Không ngoại lệ; getStatus() = CANCELLED; getCancelReason() = Optional.of(BAD_WEATHER) | BR-09, BR-10; UC-017 bước 5; ASM-25 | EC-01, EC-03, EC-05, DT1-R1; CE1, CE3, CE5, CE6 | Không | Cao |
| TC-003 | DC-Trip.cancel | giá trị biên; bảng quyết định; chuyển trạng thái | T1 status SCHEDULED | reason = VEHICLE_BREAKDOWN; now = 2026-12-15T20:30:00 | Ném TripDepartedException; getStatus() = SCHEDULED; getCancelReason() = Optional.empty(); isCancelled() = false | BR-10; UC-017 luồng 4b; ASM-26 (chờ Q-46) | BV-02, EC-04, DT1-R2; ST-01 sự kiện bị từ chối dòng 1; CE1, CE3, CE4, CE8 | Không | Cao |
| TC-004 | DC-Trip.cancel | bảng quyết định; chuyển trạng thái | T1 đã cancel(BAD_WEATHER, 2026-12-14T08:00:00) nên status CANCELLED | reason = VEHICLE_BREAKDOWN; now = 2026-12-14T09:00:00 | Ném TripAlreadyCancelledException; getStatus() = CANCELLED; getCancelReason() = Optional.of(BAD_WEATHER) (không bị ghi đè) | BR-09; UC-017 luồng 4a | EC-02, DT1-R3; ST-01 sự kiện bị từ chối dòng 2; CE1, CE2, CE7 | Không | Cao |
| TC-005 | DC-Trip.cancel | bảng quyết định (cả hai điều kiện sai) | T1 đã cancel(BAD_WEATHER, 2026-12-14T08:00:00) nên status CANCELLED | reason = VEHICLE_BREAKDOWN; now = 2026-12-15T20:30:00 | Ném TripAlreadyCancelledException (chuyến đã huỷ được kiểm tra trước giờ xuất bến); getStatus() = CANCELLED; getCancelReason() = Optional.of(BAD_WEATHER) | BR-09, BR-10; UC-017 luồng 4a, 4b; ASM-26 (chờ Q-46) | EC-02, EC-04, DT1-R4; ST-01 sự kiện bị từ chối dòng 2; CE1, CE2, CE7 | Không | Cao |
| TC-006 | DC-Trip.isBeforeDeparture | giá trị biên | T1 status SCHEDULED | now = 2026-12-15T20:29:59 | Trả true; status vẫn SCHEDULED | BR-05, BR-10; UC-009 bước 4; ASM-21 (chờ Q-13) | BV-03, EC-08, EC-11 | Không | Cao |
| TC-007 | DC-Trip.isBeforeDeparture | giá trị biên | T1 status SCHEDULED | now = 2026-12-15T20:30:00 | Trả false; status vẫn SCHEDULED | BR-05; UC-009 luồng 4c; ASM-21 (chờ Q-13) | BV-04, EC-09, EC-11 | Không | Cao |
| TC-008 | DC-Trip.isBeforeDeparture | phân vùng tương đương | T1 đã cancel(BAD_WEATHER, 2026-12-14T08:00:00) nên status CANCELLED | now = 2026-12-15T20:29:59 | Trả true (kết quả chỉ phụ thuộc now); status vẫn CANCELLED | BR-05; P12 F2 hậu điều kiện | EC-08, EC-12 | Không | Trung bình |
| TC-009 | DC-Booking.isSeatCountWithinLimit | giá trị biên | SEL([A01]) | Không có tham số | Trả true | BR-01; UC-009 bước 4 | BV-05, EC-13 | DC-Seat thật | Cao |
| TC-010 | DC-Booking.isSeatCountWithinLimit | giá trị biên | SEL([A01, A02, A03, A04, A05]) | Không có tham số | Trả true | BR-01; UC-009 bước 4 | BV-06, EC-13 | DC-Seat thật | Cao |
| TC-011 | DC-Booking.isSeatCountWithinLimit | giá trị biên | SEL([A01, A02, A03, A04, A05, A06]) | Không có tham số | Trả false | BR-01; UC-009 luồng 4b | BV-07, EC-14 | DC-Seat thật | Cao |
| TC-012 | DC-Booking.holdSeats | phân vùng tương đương; bảng quyết định; đường đi (vòng lặp m = 2) | SEL([A05, A06]), cả hai chỗ AVAILABLE | seatFare = FARE (250.000 đồng); now = 2026-12-14T20:00:00 | Không ngoại lệ; getStatus() = HOLDING; A05 và A06 getTripState() = HELD; getHoldExpiry() = Optional.of(2026-12-14T20:10:00); getSeatFare() = Optional.of(250.000 đồng); holdStartedAt = 2026-12-14T20:00:00 (chưa có getter, kiểm tra gián tiếp qua holdExpiry) | BR-03, BR-02; ASM-18 (chờ Q-18); UC-009 bước 5, mục 8 (giữ lúc 20:00 hết hạn lúc 20:10); ASM-40 | EC-16, EC-20, EC-23, EC-25, EC-27, DT2-R1; ST-03 chuyển 2; ST-02 chuyển 2; CE9, CE11, CE12, CE14, CE15, CE16 | DC-Money fake | Cao |
| TC-013 | DC-Booking.holdSeats | giá trị biên; đường đi (vòng lặp 1 lần) | SEL([A05]), chỗ AVAILABLE | seatFare = FARE; now = 2026-12-14T23:55:00 | Không ngoại lệ; getStatus() = HOLDING; A05 getTripState() = HELD; getHoldExpiry() = Optional.of(2026-12-15T00:05:00) | BR-03; ASM-18 (chờ Q-18); BR-01 | BV-08, BV-11, EC-16, EC-20, EC-23, DT2-R1; ST-03 chuyển 2; CE9, CE11, CE12, CE14, CE15, CE16 | DC-Money fake | Cao |
| TC-014 | DC-Booking.holdSeats | giá trị biên; đường đi (vòng lặp n-1 = 4 lần) | SEL([A01, A02, A03, A04]), mọi chỗ AVAILABLE | seatFare = FARE; now = 2026-12-14T20:00:00 | Không ngoại lệ; getStatus() = HOLDING; cả 4 chỗ getTripState() = HELD; getHoldExpiry() = Optional.of(2026-12-14T20:10:00) | BR-01, BR-03; UC-009 bước 5 | BV-09, EC-16, EC-20, EC-23, DT2-R1; CE9, CE11, CE12, CE14, CE15, CE16 | DC-Money fake | Cao |
| TC-015 | DC-Booking.holdSeats | giá trị biên; đường đi (vòng lặp n = 5 lần) | SEL([A01, A02, A03, A04, A05]), mọi chỗ AVAILABLE | seatFare = FARE; now = 2026-12-14T20:00:00 | Không ngoại lệ; getStatus() = HOLDING; cả 5 chỗ getTripState() = HELD; getHoldExpiry() = Optional.of(2026-12-14T20:10:00) | BR-01, BR-03; UC-009 bước 5 | BV-10, EC-16, EC-20, EC-23, DT2-R1; CE9, CE11, CE12, CE14, CE15, CE16 | DC-Money fake | Cao |
| TC-016 | DC-Booking.holdSeats | bảng quyết định; chuyển trạng thái | SEL([A05]); A05 đã markHeld() cho yêu cầu khác nên HELD | seatFare = FARE; now = 2026-12-14T20:00:00 | Ném SeatsUnavailableException; getStatus() = SELECTING; getHoldExpiry() = Optional.empty(); getSeatFare() = Optional.empty(); A05 getTripState() = HELD (không đổi) | BR-02; NFR-04; UC-009 luồng 4a; ST-02 chuyển 2 | EC-16, EC-21, DT2-R2; ST-03 sự kiện bị từ chối dòng 4; CE9, CE11, CE12, CE13, CE18 | DC-Money fake | Cao |
| TC-017 | DC-Booking.holdSeats | bảng quyết định; chuyển trạng thái | SEL([A05]); A05 đã markHeld() rồi markSold() nên SOLD | seatFare = FARE; now = 2026-12-14T20:00:00 | Ném SeatsUnavailableException; getStatus() = SELECTING; getHoldExpiry() = Optional.empty(); A05 getTripState() = SOLD (không đổi) | BR-02; UC-009 luồng 4a | EC-16, EC-22, DT2-R2; ST-03 sự kiện bị từ chối dòng 4; CE9, CE11, CE12, CE13, CE18 | DC-Money fake | Cao |
| TC-018 | DC-Booking.holdSeats | bảng quyết định (chỗ thứ hai không trống) | SEL([A05, A06]); A05 AVAILABLE; A06 đã markHeld() cho yêu cầu khác nên HELD | seatFare = FARE; now = 2026-12-14T20:00:00 | Ném SeatsUnavailableException; trạng thái Booking và A05 sau lỗi: Chưa xác định: chờ Q-77 | BR-02; NFR-04; UC-009 luồng 4a | Không tính vào độ phủ ở F4 (chờ Q-77); đường a-b-d-e-d-e-h-g của CFG holdSeats | DC-Money fake | Cao |
| TC-019 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | HOLD([A05, A06]) tại H0: status HOLDING, A05, A06 HELD, holdExpiry E0 | seatFare = FARE; now = 2026-12-14T20:02:00 | Ném IllegalStateException; getStatus() = HOLDING; getHoldExpiry() = Optional.of(2026-12-14T20:10:00) (không đổi); A05, A06 vẫn HELD | P12 F2 ngoại lệ; ST-03 sự kiện bị từ chối dòng 3 | EC-17, DT2-R4; ST-03 sự kiện bị từ chối dòng 3; CE9, CE10, CE17 | DC-Money fake | Cao |
| TC-020 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | REL([A05, A06]): status SEATS_RELEASED, A05, A06 AVAILABLE | seatFare = FARE; now = 2026-12-14T20:12:00 | Ném IllegalStateException; getStatus() = SEATS_RELEASED; A05, A06 vẫn AVAILABLE; getHoldExpiry() = Optional.empty() | P12 F2 ngoại lệ; ST-03 sự kiện bị từ chối dòng 7 | EC-18, DT2-R3; ST-03 sự kiện bị từ chối dòng 7; CE9, CE10, CE17 | DC-Money fake | Cao |
| TC-021 | DC-Booking.holdSeats | chuyển trạng thái; bảng quyết định | ISS([A05, A06]): status TICKETS_ISSUED, A05, A06 SOLD | seatFare = FARE; now = 2026-12-14T20:06:00 | Ném IllegalStateException; getStatus() = TICKETS_ISSUED; A05, A06 vẫn SOLD | P12 F2 ngoại lệ; ST-03 sự kiện bị từ chối dòng 8 | EC-19, DT2-R4; ST-03 sự kiện bị từ chối dòng 8; CE9, CE10, CE17 | DC-Money, DC-TicketCode fake; DC-PaymentTransaction dummy | Cao |
| TC-022 | DC-Booking.isHoldExpired | giá trị biên; bảng quyết định | HOLD([A05, A06]) tại H0, holdExpiry = E0 (2026-12-14T20:10:00) | now = 2026-12-14T20:09:59 | Trả false; status vẫn HOLDING, holdExpiry vẫn E0 | BR-03; ASM-18 (chờ Q-18) | BV-12, EC-29, DT3-R2 | DC-Money fake | Cao |
| TC-023 | DC-Booking.isHoldExpired | giá trị biên; bảng quyết định | HOLD([A05, A06]) tại H0, holdExpiry = E0 | now = 2026-12-14T20:10:00 | Trả true; status vẫn HOLDING, holdExpiry vẫn E0 | BR-03; UC-009 luồng 5a; ASM-18 (chờ Q-18) | BV-13, EC-30, DT3-R1 | DC-Money fake | Cao |
| TC-024 | DC-Booking.isHoldExpired | phân vùng tương đương; bảng quyết định | REL([A05, A06]): status SEATS_RELEASED, holdExpiry rỗng | now = 2026-12-14T20:30:00 | Trả false (holdExpiry rỗng) | BR-03; P12 F2 hậu điều kiện | EC-31, DT3-R3 | DC-Money fake | Trung bình |
| TC-025 | DC-Booking.recordTravelerInfo | giá trị biên; bảng quyết định; chuyển trạng thái | HOLD([A05, A06]) tại H0, holdExpiry = E0 | travelerName = "Nguyễn Văn An"; travelerPhone = "0912345678"; now = 2026-12-14T20:09:59 | Không ngoại lệ; getTravelerName() = Optional.of("Nguyễn Văn An"); getTravelerPhone().get().value() = "0912345678"; getStatus() = HOLDING; getHoldExpiry() = Optional.of(E0) | UC-009 bước 6, 7; BR-03; ASM-19 | BV-14, EC-33, EC-37, EC-39, EC-42, DT4-R1; ST-03 chuyển 3; CE19, CE21, CE23, CE25, CE27, CE29, CE30 | DC-PhoneNumber fake | Cao |
| TC-026 | DC-Booking.recordTravelerInfo | giá trị biên; bảng quyết định; chuyển trạng thái | HOLD([A05, A06]) tại H0, holdExpiry = E0 | travelerName = "Nguyễn Văn An"; travelerPhone = "0912345678"; now = 2026-12-14T20:10:00 | Ném HoldExpiredException; getTravelerName() = Optional.empty(); getTravelerPhone() = Optional.empty(); getStatus() = HOLDING | BR-03; UC-009 luồng 5a; ASM-18 (chờ Q-18) | BV-15, EC-33, EC-38, DT4-R5; ST-03 sự kiện bị từ chối dòng 1; CE19, CE21, CE23, CE24, CE33 | DC-PhoneNumber fake | Cao |
| TC-027 | DC-Booking.recordTravelerInfo | bảng quyết định (hết hạn và thiếu thông tin cùng lúc) | HOLD([A05, A06]) tại H0, holdExpiry = E0 | travelerName = ""; travelerPhone = ""; now = 2026-12-14T20:10:01 | Ném HoldExpiredException (hết thời hạn được kiểm tra trước thông tin thiếu); getTravelerName() = Optional.empty(); getTravelerPhone() = Optional.empty() | UC-009 luồng 5a, 7a; BR-03; P12 F3 bước 2 trước bước 3 | EC-33, EC-38, EC-40, EC-43, DT4-R5; CE19, CE21, CE23, CE24, CE33 | DC-PhoneNumber fake | Cao |
| TC-028 | DC-Booking.recordTravelerInfo | bảng quyết định; chuyển trạng thái | HOLD([A05, A06]) tại H0, holdExpiry = E0 | travelerName = "Nguyễn Văn An"; travelerPhone = ""; now = 2026-12-14T20:05:00 | Ném TravelerInfoMissingException; getTravelerName() = Optional.empty(); getTravelerPhone() = Optional.empty(); getStatus() = HOLDING | UC-009 bước 7, luồng 7a | EC-33, EC-37, EC-39, EC-43, DT4-R2; ST-03 sự kiện bị từ chối dòng 2; CE19, CE21, CE23, CE25, CE27, CE28, CE34 | DC-PhoneNumber fake | Cao |
| TC-029 | DC-Booking.recordTravelerInfo | giá trị biên; bảng quyết định | HOLD([A05, A06]) tại H0, holdExpiry = E0 | travelerName = ""; travelerPhone = "0912345678"; now = 2026-12-14T20:05:00 | Ném TravelerInfoMissingException; getTravelerName() = Optional.empty(); getTravelerPhone() = Optional.empty(); getStatus() = HOLDING | UC-009 bước 7, luồng 7a | BV-16, EC-33, EC-37, EC-40, EC-42, DT4-R3; ST-03 sự kiện bị từ chối dòng 2; CE19, CE21, CE23, CE25, CE26, CE34 | DC-PhoneNumber fake | Cao |
| TC-030 | DC-Booking.recordTravelerInfo | bảng quyết định (cả hai thiếu) | HOLD([A05, A06]) tại H0, holdExpiry = E0 | travelerName = "   " (3 dấu cách); travelerPhone = " . - "; now = 2026-12-14T20:05:00 | Ném TravelerInfoMissingException; getTravelerName() = Optional.empty(); getTravelerPhone() = Optional.empty() | UC-009 bước 7, luồng 7a | EC-33, EC-37, EC-40, EC-43, DT4-R4; ST-03 sự kiện bị từ chối dòng 2; CE19, CE21, CE23, CE25, CE26, CE34 | DC-PhoneNumber fake | Cao |
| TC-031 | DC-Booking.recordTravelerInfo | giá trị biên; phân vùng tương đương | HOLD([A05, A06]) tại H0, holdExpiry = E0 | travelerName = " A " (một ký tự, có khoảng trắng hai đầu); travelerPhone = "091-234.5678"; now = 2026-12-14T20:05:00 | Không ngoại lệ; getTravelerName() = Optional.of("A"); getTravelerPhone().get().value() = "0912345678"; getStatus() = HOLDING | UC-009 bước 6, 7; P12 F3 bước 4; DC-PhoneNumber.of (chuẩn hoá theo SCR-03) | BV-17, EC-33, EC-37, EC-39, EC-42, DT4-R1; CE19, CE21, CE23, CE25, CE27, CE29, CE30 | DC-PhoneNumber fake | Trung bình |
| TC-032 | DC-Booking.recordTravelerInfo | chuyển trạng thái | SEL([A05, A06]): status SELECTING, chưa giữ chỗ | travelerName = "Nguyễn Văn An"; travelerPhone = "0912345678"; now = 2026-12-14T20:05:00 | Ném IllegalStateException; getStatus() = SELECTING; getTravelerName() = Optional.empty() | P12 F2 ngoại lệ | EC-35; ST-03 sự kiện bị từ chối dòng 5; CE19, CE21, CE22, CE32 | DC-PhoneNumber fake | Cao |
| TC-033 | DC-Booking.recordTravelerInfo | chuyển trạng thái | REL([A05, A06]): status SEATS_RELEASED | travelerName = "Nguyễn Văn An"; travelerPhone = "0912345678"; now = 2026-12-14T20:05:00 | Ném HoldExpiredException; getStatus() = SEATS_RELEASED; getTravelerName() = Optional.empty() | BR-03; UC-009 luồng 5a; P12 F6 ST-03 | EC-34; ST-03 sự kiện bị từ chối dòng 6; CE19, CE20, CE31 | DC-PhoneNumber fake | Cao |
| TC-034 | DC-Booking.recordTravelerInfo | chuyển trạng thái | ISS([A05, A06]): status TICKETS_ISSUED | travelerName = "Trần Thị Bình"; travelerPhone = "0987654321"; now = 2026-12-14T20:06:00 | Ném IllegalStateException; getStatus() = TICKETS_ISSUED; getTravelerName() = Optional.of("Nguyễn Văn An") (không bị ghi đè) | P12 F2 ngoại lệ | EC-36; ST-03 sự kiện bị từ chối dòng 8; CE19, CE21, CE22, CE32 | DC-PhoneNumber, DC-Money, DC-TicketCode fake; DC-PaymentTransaction dummy | Cao |
| TC-035 | DC-Booking.releaseHeldSeats | giá trị biên; chuyển trạng thái; đường đi (vòng lặp 1 lần) | HOLD([A05]) tại H0 | Không có tham số | Không ngoại lệ; getStatus() = SEATS_RELEASED; A05 getTripState() = AVAILABLE; getHoldExpiry() = Optional.empty() | BR-03; ASM-24; UC-009 luồng 5a, 8a, *a | BV-18, EC-45, EC-49; ST-03 chuyển 6; ST-02 chuyển 4; CE35, CE37, CE39, CE40, CE41, CE42, CE43 | DC-Money fake | Cao |
| TC-036 | DC-Booking.releaseHeldSeats | phân vùng tương đương; đường đi (vòng lặp m = 2 lần) | HOLD([A05, A06]) tại H0 | Không có tham số | Không ngoại lệ; getStatus() = SEATS_RELEASED; A05 và A06 getTripState() = AVAILABLE; getHoldExpiry() = Optional.empty() | BR-03; ASM-24; UC-009 luồng 5a, 8a, *a | EC-45, EC-49; ST-03 chuyển 6; ST-02 chuyển 4; CE35, CE37, CE39, CE40, CE41, CE42, CE43 | DC-Money fake | Cao |
| TC-037 | DC-Booking.releaseHeldSeats | giá trị biên; đường đi (vòng lặp n-1 = 4 lần) | HOLD([A01, A02, A03, A04]) tại H0 | Không có tham số | Không ngoại lệ; getStatus() = SEATS_RELEASED; cả 4 chỗ getTripState() = AVAILABLE | BR-03; ASM-24 | BV-19, EC-45, EC-49; ST-03 chuyển 6; CE35, CE37, CE39, CE40, CE41, CE42, CE43 | DC-Money fake | Trung bình |
| TC-038 | DC-Booking.releaseHeldSeats | giá trị biên; đường đi (vòng lặp n = 5 lần) | HOLD([A01, A02, A03, A04, A05]) tại H0 | Không có tham số | Không ngoại lệ; getStatus() = SEATS_RELEASED; cả 5 chỗ getTripState() = AVAILABLE | BR-01, BR-03; ASM-24 | BV-20, EC-45, EC-49; ST-03 chuyển 6; CE35, CE37, CE39, CE40, CE41, CE42, CE43 | DC-Money fake | Trung bình |
| TC-039 | DC-Booking.releaseHeldSeats | chuyển trạng thái | REL([A05, A06]); sau đó đặt A05 markHeld() cho yêu cầu khác (A05 HELD) | Không có tham số (gọi lần hai) | Không ngoại lệ, không đổi gì; getStatus() = SEATS_RELEASED; A05 vẫn HELD (chỗ đã thuộc người khác không bị trả nhầm); A06 AVAILABLE | ASM-24; P12 F6 ST-03 chuyển 8 | EC-46; ST-03 chuyển 8; CE35, CE36, CE44 | DC-Money fake | Cao |
| TC-040 | DC-Booking.releaseHeldSeats | chuyển trạng thái | SEL([A05, A06]): status SELECTING | Không có tham số | Ném IllegalStateException; getStatus() = SELECTING | P12 F2 ngoại lệ | EC-47; ST-03 sự kiện bị từ chối dòng 5; CE35, CE37, CE38, CE45 | Không | Cao |
| TC-041 | DC-Booking.releaseHeldSeats | chuyển trạng thái | ISS([A05, A06]): status TICKETS_ISSUED, A05, A06 SOLD | Không có tham số | Ném IllegalStateException; getStatus() = TICKETS_ISSUED; A05, A06 vẫn SOLD | P12 F2 ngoại lệ; BR-04 | EC-48; ST-03 sự kiện bị từ chối dòng 8; CE35, CE37, CE38, CE45 | DC-PhoneNumber, DC-Money, DC-TicketCode fake; DC-PaymentTransaction dummy | Cao |
| TC-042 | DC-Booking.issueTickets | phân vùng tương đương; bảng quyết định; đường đi (vòng lặp m = 2 lần) | HOLD([A05, A06]) tại H0 + INFO; holdExpiry = E0 | ticketCodes = [SV0001, SV0002]; transaction = TX | Trả 2 vé theo thứ tự chỗ A05, A06: vé 1 getSeat() = A05, getTicketCode().value() = "SV0001"; vé 2 getSeat() = A06, getTicketCode().value() = "SV0002"; mỗi vé getStatus() = ISSUED, getFare() = 250.000 đồng (= seatFare), getTravelerName() = "Nguyễn Văn An", getTravelerPhone().value() = "0912345678", getPaymentTransaction() = Optional.of(TX), getRefundStatus() = NOT_APPLICABLE, getSmsStatus() = NO_ISSUE, purchaseChannel = ONLINE và paymentStatus = PAID (chưa có getter, xem Đề xuất sửa artifact trước); Booking getStatus() = TICKETS_ISSUED, getHoldExpiry() = Optional.empty(); A05, A06 getTripState() = SOLD | BR-04; UC-009 bước 9; P04 UC-009 Dữ liệu ra 1 (A05 mang mã nhỏ hơn A06); ST-04 chuyển 1 | BV-22, EC-51, EC-55, EC-59, DT5-R1; ST-03 chuyển 5; ST-04 chuyển 1; ST-02 chuyển 3; CE46, CE48, CE50, CE52, CE53, CE54, CE55, CE56 | DC-PaymentTransaction dummy; DC-TicketCode, DC-PhoneNumber, DC-Money fake | Cao |
| TC-043 | DC-Booking.issueTickets | giá trị biên; đường đi (vòng lặp 1 lần) | HOLD([A05]) tại H0 + INFO | ticketCodes = [SV0001]; transaction = TX | Trả 1 vé: getSeat() = A05, getTicketCode().value() = "SV0001", getStatus() = ISSUED; Booking getStatus() = TICKETS_ISSUED; A05 getTripState() = SOLD | BR-04; UC-009 bước 9 | BV-24, EC-51, EC-55, EC-59, DT5-R1; ST-03 chuyển 5; CE46, CE48, CE50, CE52, CE53, CE54, CE55, CE56 | như TC-042 | Cao |
| TC-044 | DC-Booking.issueTickets | giá trị biên; đường đi (vòng lặp n-1 = 4 lần) | HOLD([A01, A02, A03, A04]) tại H0 + INFO | ticketCodes = [SV0001, SV0002, SV0003, SV0004]; transaction = TX | Trả 4 vé, vé thứ i mang chỗ A0i và mã SV000i; cả 4 chỗ SOLD; Booking getStatus() = TICKETS_ISSUED | BR-04; UC-009 bước 9 | BV-25, EC-51, EC-55, EC-59, DT5-R1; ST-03 chuyển 5; CE46, CE48, CE50, CE52, CE53, CE54, CE55, CE56 | như TC-042 | Cao |
| TC-045 | DC-Booking.issueTickets | giá trị biên; đường đi (vòng lặp n = 5 lần) | HOLD([A01, A02, A03, A04, A05]) tại H0 + INFO | ticketCodes = [SV0001, SV0002, SV0003, SV0004, SV0005]; transaction = TX | Trả 5 vé, vé thứ i mang chỗ A0i và mã SV000i; cả 5 chỗ SOLD; Booking getStatus() = TICKETS_ISSUED | BR-01, BR-04; UC-009 bước 9 | BV-26, EC-51, EC-55, EC-59, DT5-R1; ST-03 chuyển 5; CE46, CE48, CE50, CE52, CE53, CE54, CE55, CE56 | như TC-042 | Cao |
| TC-046 | DC-Booking.issueTickets | chuyển trạng thái; bảng quyết định | REL([A05, A06]): status SEATS_RELEASED (hết hạn trong lúc thanh toán), A05, A06 AVAILABLE | ticketCodes = [SV0001, SV0002]; transaction = TX | Ném HoldExpiredException; getStatus() = SEATS_RELEASED; A05, A06 vẫn AVAILABLE; không có vé nào được tạo | BR-03, BR-06; UC-009 luồng 5a; P12 F6 ST-03 | EC-52, DT5-R3; ST-03 sự kiện bị từ chối dòng 6; CE46, CE47, CE57 | DC-TicketCode fake; DC-PaymentTransaction dummy | Cao |
| TC-047 | DC-Booking.issueTickets | chuyển trạng thái; bảng quyết định | SEL([A05, A06]): status SELECTING | ticketCodes = [SV0001, SV0002]; transaction = TX | Ném IllegalStateException; getStatus() = SELECTING; A05, A06 vẫn AVAILABLE | P12 F2 ngoại lệ; P12 F6 ST-03 | EC-53, DT5-R3; ST-03 sự kiện bị từ chối dòng 5; CE46, CE48, CE49, CE58 | DC-TicketCode fake; DC-PaymentTransaction dummy | Cao |
| TC-048 | DC-Booking.issueTickets | chuyển trạng thái; bảng quyết định | ISS([A05, A06]): status TICKETS_ISSUED, A05, A06 SOLD | ticketCodes = [SV0003, SV0004]; transaction = TX | Ném IllegalStateException; getStatus() = TICKETS_ISSUED; không có vé mới; A05, A06 vẫn SOLD | BR-04; P12 F6 ST-03 | EC-54, DT5-R3; ST-03 sự kiện bị từ chối dòng 8; CE46, CE48, CE49, CE58 | như TC-042 | Cao |
| TC-049 | DC-Booking.issueTickets | giá trị biên; bảng quyết định | HOLD([A05, A06]) tại H0 + INFO | ticketCodes = [SV0001] (1 mã cho 2 chỗ); transaction = TX | Ném IllegalArgumentException; getStatus() = HOLDING; A05, A06 vẫn HELD; getHoldExpiry() = Optional.of(E0) | BR-04; P12 F2 ngoại lệ | BV-21, EC-51, EC-56, DT5-R2; CE46, CE48, CE50, CE51, CE59 | như TC-042 | Cao |
| TC-050 | DC-Booking.issueTickets | giá trị biên; bảng quyết định | HOLD([A05, A06]) tại H0 + INFO | ticketCodes = [SV0001, SV0002, SV0003] (3 mã cho 2 chỗ); transaction = TX | Ném IllegalArgumentException; getStatus() = HOLDING; A05, A06 vẫn HELD; getHoldExpiry() = Optional.of(E0) | BR-04; P12 F2 ngoại lệ | BV-23, EC-51, EC-57, DT5-R2; CE46, CE48, CE50, CE51, CE59 | như TC-042 | Cao |
| TC-051 | DC-Ticket.cancelForTrip | bảng quyết định; chuyển trạng thái; đường đi | TK: status ISSUED, paymentStatus PAID, refundStatus NOT_APPLICABLE | Không có tham số | Không ngoại lệ; getStatus() = CANCELLED; getRefundStatus() = NOT_REFUNDED; isActive() = false; getSmsStatus() = NO_ISSUE (không đổi) | ASM-29 (chờ Q-48); UC-017 bước 7 | EC-60, EC-64, DT6-R1; ST-04 chuyển 2; CE60, CE62, CE63, CE64, CE66 | DC-Money, DC-PhoneNumber, DC-TicketCode fake; DC-PaymentTransaction dummy | Cao |
| TC-052 | DC-Ticket.cancelForTrip | bảng quyết định; chuyển trạng thái; đường đi | TK-C(UNPAID): status ISSUED, paymentStatus UNPAID, refundStatus NOT_APPLICABLE | Không có tham số | Không ngoại lệ; getStatus() = CANCELLED; getRefundStatus() = NOT_APPLICABLE (giữ nguyên) | ASM-29 (chờ Q-48); UC-017 bước 7, mục 8 (vé đặt qua điện thoại chưa thanh toán không có hoàn tiền) | EC-60, EC-65, DT6-R2; ST-04 chuyển 3; CE60, CE62, CE63, CE65 | Bộ dựng vé test (fake) | Cao |
| TC-053 | DC-Ticket.cancelForTrip | chuyển trạng thái; bảng quyết định | TK-P: status CANCELLED, refundStatus NOT_REFUNDED | Không có tham số (gọi lần hai) | Ném IllegalStateException; getStatus() = CANCELLED; getRefundStatus() = NOT_REFUNDED (không đổi) | P12 F2 ngoại lệ; P12 F6 ST-04 | EC-61, DT6-R3; ST-04 sự kiện bị từ chối dòng 2; CE60, CE61, CE67 | như TC-051 | Cao |
| TC-054 | DC-Ticket.cancelForTrip | chuyển trạng thái; bảng quyết định | TK-R: status CANCELLED, refundStatus REFUNDED | Không có tham số | Ném IllegalStateException; getStatus() = CANCELLED; getRefundStatus() = REFUNDED (không đổi) | P12 F2 ngoại lệ; NFR-05; P12 F6 ST-04 | EC-62, DT6-R3; ST-04 sự kiện bị từ chối dòng 3; CE60, CE61, CE67 | như TC-051 | Cao |
| TC-055 | DC-Ticket.cancelForTrip | chuyển trạng thái; bảng quyết định | TK-C(UNPAID) đã cancelForTrip(): status CANCELLED, refundStatus NOT_APPLICABLE | Không có tham số (gọi lần hai) | Ném IllegalStateException; getStatus() = CANCELLED; getRefundStatus() = NOT_APPLICABLE (không đổi) | P12 F2 ngoại lệ; P12 F6 ST-04 | EC-63, DT6-R3; ST-04 sự kiện bị từ chối dòng 4; CE60, CE61, CE67 | Bộ dựng vé test (fake) | Trung bình |
| TC-056 | DC-Ticket.isOnlineRefundPending | bảng quyết định; phân vùng tương đương | TK-P: ONLINE, PAID, CANCELLED, NOT_REFUNDED | Không có tham số | Trả true; trạng thái vé không đổi | BR-08; UC-017 bước 11 | EC-66, DT7-R1 | như TC-051 | Cao |
| TC-057 | DC-Ticket.isOnlineRefundPending | bảng quyết định | TK-R: ONLINE, PAID, CANCELLED, REFUNDED | Không có tham số | Trả false; getRefundStatus() = REFUNDED (không đổi) | BR-08; NFR-05 | EC-67, DT7-R2 | như TC-051 | Cao |
| TC-058 | DC-Ticket.isOnlineRefundPending | bảng quyết định | TK: ONLINE, PAID, ISSUED, NOT_APPLICABLE | Không có tham số | Trả false; getStatus() = ISSUED (không đổi) | BR-08; P12 F2 hậu điều kiện | EC-68, DT7-R3 | như TC-051 | Cao |
| TC-059 | DC-Ticket.isOnlineRefundPending | bảng quyết định (kênh COUNTER) | TK-C(PAID) đã cancelForTrip(): COUNTER, PAID, CANCELLED, NOT_REFUNDED | Không có tham số | Trả false (vé quầy hoàn tiền mặt tại quầy theo UC-018); getRefundStatus() = NOT_REFUNDED (không đổi) | BR-08 (ASM-08, chờ Q-07); UC-017 mục 8 | EC-69, DT7-R4 | Bộ dựng vé test (fake) | Cao |
| TC-060 | DC-Ticket.isOnlineRefundPending | bảng quyết định (kênh COUNTER chưa thanh toán) | TK-C(UNPAID) đã cancelForTrip(): COUNTER, UNPAID, CANCELLED, NOT_APPLICABLE | Không có tham số | Trả false; getRefundStatus() = NOT_APPLICABLE (không đổi) | BR-08; ASM-29 (chờ Q-48); UC-017 mục 8 | EC-70, DT7-R4 | Bộ dựng vé test (fake) | Cao |
| TC-061 | DC-Ticket.calculateRefundAmount | phân vùng tương đương; đường đi | TK-P: ONLINE, PAID, CANCELLED, NOT_REFUNDED, fare = 250.000 đồng | Không có tham số | Trả Money 250.000 đồng (100% giá vé đã ghi); getStatus() = CANCELLED; getRefundStatus() = NOT_REFUNDED (không đổi) | BR-07; UC-017 bước 11, mục 8 (250.000 đ hoàn 250.000 đ); NFR-06 | EC-71, EC-75, ST-04 (hợp lệ ở CancelledRefundPending); CE68, CE70, CE71 | như TC-051 | Cao |
| TC-062 | DC-Ticket.calculateRefundAmount | giá trị biên; đường đi | Vé ONLINE, PAID tạo bằng createTicket với fare = 1 đồng, rồi cancelForTrip(): CANCELLED, NOT_REFUNDED | Không có tham số | Trả Money 1 đồng | BR-07; NFR-06; P13 ck_ticket_fare (fare > 0) | BV-27, EC-71, EC-75; CE68, CE70, CE71 | như TC-051 | Cao |
| TC-063 | DC-Ticket.calculateRefundAmount | chuyển trạng thái; đường đi | TK: status ISSUED | Không có tham số | Ném IllegalStateException; getStatus() = ISSUED; getRefundStatus() = NOT_APPLICABLE | P12 F2 ngoại lệ; BR-08; P12 F6 ST-04 | EC-72; ST-04 sự kiện bị từ chối dòng 1; CE68, CE69, CE72 | như TC-051 | Cao |
| TC-064 | DC-Ticket.calculateRefundAmount | chuyển trạng thái | TK-R: status CANCELLED, refundStatus REFUNDED | Không có tham số | Ném IllegalStateException (không tính hoàn lần hai); getRefundStatus() = REFUNDED (không đổi) | NFR-05; BR-07; P12 F6 ST-04 | EC-73; ST-04 sự kiện bị từ chối dòng 3; CE68, CE69, CE72 | như TC-051 | Cao |
| TC-065 | DC-Ticket.calculateRefundAmount | chuyển trạng thái | TK-C(UNPAID) đã cancelForTrip(): CANCELLED, NOT_APPLICABLE | Không có tham số | Ném IllegalStateException; getRefundStatus() = NOT_APPLICABLE (không đổi) | BR-08; ASM-29 (chờ Q-48); P12 F6 ST-04 | EC-74; ST-04 sự kiện bị từ chối dòng 4; CE68, CE69, CE72 | Bộ dựng vé test (fake) | Trung bình |

## F4. Ma trận phủ

Bảng phủ phân vùng tương đương, giá trị biên, quy tắc bảng quyết định (sinh từ cột Phủ của F3):

| Mục cần phủ | TC phủ | Đạt (Có / Không: lý do) |
|---|---|---|
| EC-01 (status: status = SCHEDULED) | TC-001, TC-002 | Có |
| EC-02 (status: status = CANCELLED) | TC-004, TC-005 | Có |
| EC-03 (now: now < departureTime) | TC-001, TC-002 | Có |
| EC-04 (now: now >= departureTime) | TC-003, TC-005 | Có |
| EC-05 (reason: reason thuộc {VEHICLE_BREAKDOWN, BAD_WEATHER}) | TC-001, TC-002 | Có |
| EC-06 (reason: reason = null) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-07 (now: now = null) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-08 (now: now < departureTime) | TC-006, TC-008 | Có |
| EC-09 (now: now >= departureTime) | TC-007 | Có |
| EC-10 (now: now = null) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-11 (trạng thái chuyến: status = SCHEDULED) | TC-006, TC-007 | Có |
| EC-12 (trạng thái chuyến: status = CANCELLED) | TC-008 | Có |
| EC-13 (số chỗ n của lần đặt: 1 <= n <= 5) | TC-009, TC-010 | Có |
| EC-14 (số chỗ n: n >= 6) | TC-011 | Có |
| EC-15 (số chỗ n: n <= 0) | - | Không: không thể xảy ra (createBooking từ chối danh sách rỗng) |
| EC-16 (status của Booking: SELECTING) | TC-012, TC-013, TC-014, TC-015, TC-016, TC-017 | Có |
| EC-17 (status của Booking: HOLDING) | TC-019 | Có |
| EC-18 (status của Booking: SEATS_RELEASED) | TC-020 | Có |
| EC-19 (status của Booking: TICKETS_ISSUED) | TC-021 | Có |
| EC-20 (trạng thái các chỗ: mọi chỗ AVAILABLE) | TC-012, TC-013, TC-014, TC-015 | Có |
| EC-21 (trạng thái các chỗ: có ít nhất một chỗ HELD) | TC-016 | Có |
| EC-22 (trạng thái các chỗ: không có chỗ HELD, có ít nhất một chỗ SOLD) | TC-017 | Có |
| EC-23 (số chỗ n: 1 <= n <= 5) | TC-012, TC-013, TC-014, TC-015 | Có |
| EC-24 (số chỗ n: n >= 6) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-25 (seatFare: Money lớn hơn 0) | TC-012 | Có |
| EC-26 (seatFare: Money nhỏ hơn hoặc bằng 0, hoặc null) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-27 (now: LocalDateTime hợp lệ) | TC-012 | Có |
| EC-28 (now: now = null) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-29 (holdExpiry và now: holdExpiry có giá trị và now < holdExpiry) | TC-022 | Có |
| EC-30 (holdExpiry và now: holdExpiry có giá trị và now >= holdExpiry) | TC-023 | Có |
| EC-31 (holdExpiry: holdExpiry rỗng (đã trả chỗ hoặc dừng chờ)) | TC-024 | Có |
| EC-32 (now: now = null) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-33 (status của Booking: HOLDING) | TC-025, TC-026, TC-027, TC-028, TC-029, TC-030, TC-031 | Có |
| EC-34 (status của Booking: SEATS_RELEASED) | TC-033 | Có |
| EC-35 (status của Booking: SELECTING) | TC-032 | Có |
| EC-36 (status của Booking: TICKETS_ISSUED) | TC-034 | Có |
| EC-37 (now (khi status = HOLDING, holdExpiry = 2026-12-14T20:10:00): now < holdExpiry) | TC-025, TC-028, TC-029, TC-030, TC-031 | Có |
| EC-38 (now: now >= holdExpiry) | TC-026, TC-027 | Có |
| EC-39 (travelerName: còn từ 1 đến 100 ký tự sau khi cắt khoảng trắng hai đầu) | TC-025, TC-028, TC-031 | Có |
| EC-40 (travelerName: rỗng hoặc chỉ gồm khoảng trắng (0 ký tự sau khi cắt)) | TC-027, TC-029, TC-030 | Có |
| EC-41 (travelerName: null, hoặc dài hơn 100 ký tự) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-42 (travelerPhone: sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang còn ít nhất một ký tự và chỉ gồm chữ số) | TC-025, TC-029, TC-031 | Có |
| EC-43 (travelerPhone: rỗng sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang) | TC-027, TC-028, TC-030 | Có |
| EC-44 (travelerPhone: null, hoặc còn ký tự khác chữ số sau khi bỏ khoảng trắng, dấu chấm, dấu gạch ngang) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-45 (status của Booking: HOLDING) | TC-035, TC-036, TC-037, TC-038 | Có |
| EC-46 (status của Booking: SEATS_RELEASED) | TC-039 | Có |
| EC-47 (status của Booking: SELECTING) | TC-040 | Có |
| EC-48 (status của Booking: TICKETS_ISSUED) | TC-041 | Có |
| EC-49 (số chỗ n khi HOLDING: 1 <= n <= 5) | TC-035, TC-036, TC-037, TC-038 | Có |
| EC-50 (số chỗ n khi HOLDING: n = 0 hoặc n >= 6) | - | Không: không thể xảy ra ở trạng thái HOLDING |
| EC-51 (status của Booking: HOLDING (đã ghi người đi)) | TC-042, TC-043, TC-044, TC-045, TC-049, TC-050 | Có |
| EC-52 (status của Booking: SEATS_RELEASED) | TC-046 | Có |
| EC-53 (status của Booking: SELECTING) | TC-047 | Có |
| EC-54 (status của Booking: TICKETS_ISSUED) | TC-048 | Có |
| EC-55 (ticketCodes.size() so với số chỗ: bằng số chỗ) | TC-042, TC-043, TC-044, TC-045 | Có |
| EC-56 (ticketCodes.size() so với số chỗ: nhỏ hơn số chỗ (kể cả danh sách rỗng)) | TC-049 | Có |
| EC-57 (ticketCodes.size() so với số chỗ: lớn hơn số chỗ) | TC-050 | Có |
| EC-58 (ticketCodes, transaction, thông tin người đi: ticketCodes = null, transaction = null, hoặc Booking HOLDING chưa ghi người đi (recordTravelerInfo chưa gọi)) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| EC-59 (số chỗ n: 1 <= n <= 5) | TC-042, TC-043, TC-044, TC-045 | Có |
| EC-60 (status của vé: ISSUED) | TC-051, TC-052 | Có |
| EC-61 (status của vé: CANCELLED, refundStatus = NOT_REFUNDED (CancelledRefundPending)) | TC-053 | Có |
| EC-62 (status của vé: CANCELLED, refundStatus = REFUNDED (CancelledRefunded)) | TC-054 | Có |
| EC-63 (status của vé: CANCELLED, refundStatus = NOT_APPLICABLE (CancelledNoRefundDue)) | TC-055 | Có |
| EC-64 (paymentStatus (khi ISSUED): PAID) | TC-051 | Có |
| EC-65 (paymentStatus (khi ISSUED): UNPAID) | TC-052 | Có |
| EC-66 (tổ hợp (kênh, thanh toán, trạng thái, hoàn tiền): ONLINE, PAID, CANCELLED, NOT_REFUNDED) | TC-056 | Có |
| EC-67 (tổ hợp: ONLINE, PAID, CANCELLED, REFUNDED) | TC-057 | Có |
| EC-68 (tổ hợp: ONLINE, PAID, ISSUED (NOT_APPLICABLE)) | TC-058 | Có |
| EC-69 (tổ hợp: COUNTER, PAID (mọi trạng thái)) | TC-059 | Có |
| EC-70 (tổ hợp: COUNTER, UNPAID (mọi trạng thái)) | TC-060 | Có |
| EC-71 (trạng thái vé: thoả isOnlineRefundPending (ONLINE, PAID, CANCELLED, NOT_REFUNDED)) | TC-061, TC-062 | Có |
| EC-72 (trạng thái vé: ISSUED) | TC-063 | Có |
| EC-73 (trạng thái vé: CANCELLED, REFUNDED) | TC-064 | Có |
| EC-74 (trạng thái vé: CANCELLED, không thoả isOnlineRefundPending và không REFUNDED (CancelledNoRefundDue, hoặc vé kênh COUNTER)) | TC-065 | Có |
| EC-75 (fare: Money lớn hơn 0) | TC-061, TC-062 | Có |
| EC-76 (fare: Money nhỏ hơn hoặc bằng 0) | - | Không: ASM-57 (đầu vào null hoặc vi phạm ràng buộc, P12 không nêu hành vi) |
| BV-01 (max của EC-03: now = 2026-12-15T20:29:59) | TC-001 | Có |
| BV-02 (min của EC-04: now = 2026-12-15T20:30:00) | TC-003 | Có |
| BV-03 (max của EC-08: now = 2026-12-15T20:29:59) | TC-006 | Có |
| BV-04 (min của EC-09: now = 2026-12-15T20:30:00) | TC-007 | Có |
| BV-05 (min của EC-13: n = 1) | TC-009 | Có |
| BV-06 (max của EC-13: n = 5) | TC-010 | Có |
| BV-07 (min của EC-14 (max + 1): n = 6) | TC-011 | Có |
| BV-08 (min của EC-23: n = 1) | TC-013 | Có |
| BV-09 (max - 1 của EC-23: n = 4) | TC-014 | Có |
| BV-10 (max của EC-23: n = 5) | TC-015 | Có |
| BV-11 (biên ngày của đầu ra holdExpiry (EC-27): now = 2026-12-14T23:55:00) | TC-013 | Có |
| BV-12 (max của EC-29: now = 2026-12-14T20:09:59) | TC-022 | Có |
| BV-13 (min của EC-30: now = 2026-12-14T20:10:00) | TC-023 | Có |
| BV-14 (max của EC-37: now = 2026-12-14T20:09:59) | TC-025 | Có |
| BV-15 (min của EC-38: now = 2026-12-14T20:10:00) | TC-026 | Có |
| BV-16 (max của EC-40 (độ dài 0): travelerName = "") | TC-029 | Có |
| BV-17 (min của EC-39 (độ dài 1 sau khi cắt): travelerName = " A ") | TC-031 | Có |
| BV-18 (min của EC-49: n = 1) | TC-035 | Có |
| BV-19 (max - 1 của EC-49: n = 4) | TC-037 | Có |
| BV-20 (max của EC-49: n = 5) | TC-038 | Có |
| BV-21 (max của EC-56 (size = số chỗ - 1): 2 chỗ, 1 mã vé) | TC-049 | Có |
| BV-22 (EC-55 (size = số chỗ): 2 chỗ, 2 mã vé) | TC-042 | Có |
| BV-23 (min của EC-57 (size = số chỗ + 1): 2 chỗ, 3 mã vé) | TC-050 | Có |
| BV-24 (min của EC-59: n = 1) | TC-043 | Có |
| BV-25 (max - 1 của EC-59: n = 4) | TC-044 | Có |
| BV-26 (max của EC-59: n = 5) | TC-045 | Có |
| BV-27 (min của EC-75: fare = 1 đồng) | TC-062 | Có |
| DT1-R1 | TC-001, TC-002 | Có |
| DT1-R2 | TC-003 | Có |
| DT1-R3 | TC-004 | Có |
| DT1-R4 | TC-005 | Có |
| DT2-R1 | TC-012, TC-013, TC-014, TC-015 | Có |
| DT2-R2 | TC-016, TC-017 | Có |
| DT2-R3 | TC-020 | Có |
| DT2-R4 | TC-019, TC-021 | Có |
| DT3-R1 | TC-023 | Có |
| DT3-R2 | TC-022 | Có |
| DT3-R3 | TC-024 | Có |
| DT4-R1 | TC-025, TC-031 | Có |
| DT4-R2 | TC-028 | Có |
| DT4-R3 | TC-029 | Có |
| DT4-R4 | TC-030 | Có |
| DT4-R5 | TC-026, TC-027 | Có |
| DT5-R1 | TC-042, TC-043, TC-044, TC-045 | Có |
| DT5-R2 | TC-049, TC-050 | Có |
| DT5-R3 | TC-046, TC-047, TC-048 | Có |
| DT6-R1 | TC-051 | Có |
| DT6-R2 | TC-052 | Có |
| DT6-R3 | TC-053, TC-054, TC-055 | Có |
| DT7-R1 | TC-056 | Có |
| DT7-R2 | TC-057 | Có |
| DT7-R3 | TC-058 | Có |
| DT7-R4 | TC-059, TC-060 | Có |
| DT7-R5 | - | Không: N/A (tổ hợp không thể xảy ra) |
| DT7-R6 | - | Không: N/A (tổ hợp không thể xảy ra) |

Bảng phủ chuyển trạng thái (chuyển hợp lệ và sự kiện bị từ chối theo P12 F6):

| Mục cần phủ (chuyển trạng thái) | TC phủ | Đạt (Có / Không: lý do) |
|---|---|---|
| DC-Trip.cancel: ST-01 chuyển 2 | TC-001 | Có |
| DC-Trip.cancel: ST-01 sự kiện bị từ chối dòng 1 | TC-003 | Có |
| DC-Trip.cancel: ST-01 sự kiện bị từ chối dòng 2 | TC-004, TC-005 | Có |
| DC-Booking.holdSeats: ST-03 chuyển 2 | TC-012, TC-013 | Có |
| DC-Booking.holdSeats: ST-02 chuyển 2 | TC-012 | Có |
| DC-Booking.holdSeats: ST-03 sự kiện bị từ chối dòng 4 | TC-016, TC-017 | Có |
| DC-Booking.holdSeats: ST-03 sự kiện bị từ chối dòng 3 | TC-019 | Có |
| DC-Booking.holdSeats: ST-03 sự kiện bị từ chối dòng 7 | TC-020 | Có |
| DC-Booking.holdSeats: ST-03 sự kiện bị từ chối dòng 8 | TC-021 | Có |
| DC-Booking.recordTravelerInfo: ST-03 chuyển 3 | TC-025 | Có |
| DC-Booking.recordTravelerInfo: ST-03 sự kiện bị từ chối dòng 1 | TC-026 | Có |
| DC-Booking.recordTravelerInfo: ST-03 sự kiện bị từ chối dòng 2 | TC-028, TC-029, TC-030 | Có |
| DC-Booking.recordTravelerInfo: ST-03 sự kiện bị từ chối dòng 5 | TC-032 | Có |
| DC-Booking.recordTravelerInfo: ST-03 sự kiện bị từ chối dòng 6 | TC-033 | Có |
| DC-Booking.recordTravelerInfo: ST-03 sự kiện bị từ chối dòng 8 | TC-034 | Có |
| DC-Booking.releaseHeldSeats: ST-03 chuyển 6 | TC-035, TC-036, TC-037, TC-038 | Có |
| DC-Booking.releaseHeldSeats: ST-02 chuyển 4 | TC-035, TC-036 | Có |
| DC-Booking.releaseHeldSeats: ST-03 chuyển 8 | TC-039 | Có |
| DC-Booking.releaseHeldSeats: ST-03 sự kiện bị từ chối dòng 5 | TC-040 | Có |
| DC-Booking.releaseHeldSeats: ST-03 sự kiện bị từ chối dòng 8 | TC-041 | Có |
| DC-Booking.issueTickets: ST-03 chuyển 5 | TC-042, TC-043, TC-044, TC-045 | Có |
| DC-Booking.issueTickets: ST-04 chuyển 1 | TC-042 | Có |
| DC-Booking.issueTickets: ST-02 chuyển 3 | TC-042 | Có |
| DC-Booking.issueTickets: ST-03 sự kiện bị từ chối dòng 6 | TC-046 | Có |
| DC-Booking.issueTickets: ST-03 sự kiện bị từ chối dòng 5 | TC-047 | Có |
| DC-Booking.issueTickets: ST-03 sự kiện bị từ chối dòng 8 | TC-048 | Có |
| DC-Ticket.cancelForTrip: ST-04 chuyển 2 | TC-051 | Có |
| DC-Ticket.cancelForTrip: ST-04 chuyển 3 | TC-052 | Có |
| DC-Ticket.cancelForTrip: ST-04 sự kiện bị từ chối dòng 2 | TC-053 | Có |
| DC-Ticket.cancelForTrip: ST-04 sự kiện bị từ chối dòng 3 | TC-054 | Có |
| DC-Ticket.cancelForTrip: ST-04 sự kiện bị từ chối dòng 4 | TC-055 | Có |
| DC-Ticket.calculateRefundAmount: ST-04 sự kiện bị từ chối dòng 1 | TC-063 | Có |
| DC-Ticket.calculateRefundAmount: ST-04 sự kiện bị từ chối dòng 3 | TC-064 | Có |
| DC-Ticket.calculateRefundAmount: ST-04 sự kiện bị từ chối dòng 4 | TC-065 | Có |

Bảng phủ nhánh CE: mỗi operation có CFG đã có bảng phủ nhánh riêng ở F2.1.6, F2.4.6, F2.6.6, F2.7.6, F2.8.6, F2.9.6, F2.11.6; tất cả CE đều có TC phủ.

Bảng phủ BR và luồng thay thế P04 liên quan tới các operation được chọn:

| Mục cần phủ | TC phủ | Đạt (Có / Không: lý do) |
|---|---|---|
| BR-01 tối đa 5 chỗ mỗi lần đặt | TC-009, TC-010, TC-011 (isSeatCountWithinLimit); TC-013, TC-014, TC-015 (holdSeats n = 1, 4, 5); TC-035 đến TC-038; TC-043 đến TC-045 | Có, ở mức entity. Việc chặn lần đặt hơn 5 chỗ và báo luồng 4b thuộc DC-BookTicketOnlineService.processSeatSelection (ngoài phạm vi, kiểm thử control) |
| BR-02 không hai vé cùng một chỗ | TC-016, TC-017, TC-018 (holdSeats từ chối chỗ HELD hoặc SOLD) | Có một phần. Tính duy nhất tuyệt đối và việc chỉ một yêu cầu giữ được chỗ khi đồng thời (NFR-04) cần kiểm thử tích hợp với cơ sở dữ liệu (khoá ghi IF-05.findByTripAndSeatCodesForUpdate, ràng buộc duy nhất của P13) và kiểm thử đồng thời, ngoài unit test |
| BR-03 giữ chỗ 10 phút | TC-012, TC-013, TC-014, TC-015 (holdExpiry = giữ + 10 phút); TC-022, TC-023, TC-024 (isHoldExpired); TC-025, TC-026, TC-027, TC-033 (recordTravelerInfo); TC-035 đến TC-038 (trả chỗ); TC-046 (issueTickets sau khi đã trả chỗ) | Có, ở mức entity. Quét định kỳ và gọi handleHoldExpiry thuộc DC-BookTicketOnlineService, DC-HoldExpiryTrigger (ngoài phạm vi, kiểm thử control và tích hợp bộ định thời) |
| BR-04 mỗi chỗ một mã vé | TC-042, TC-043, TC-044, TC-045 (mỗi chỗ một vé, mã vé theo thứ tự chỗ), TC-049, TC-050 (số mã vé khác số chỗ) | Có một phần. Tính duy nhất toàn hệ thống của mã vé do IF-07.nextTicketCodes bảo đảm: kiểm thử kho dữ liệu hoặc tích hợp, ngoài unit test của entity |
| BR-05 bán vé trực tuyến tới giờ xuất bến | TC-006, TC-007, TC-008 | Có, ở mức entity. Việc từ chối giữ chỗ và báo luồng 4c thuộc processSeatSelection (ngoài phạm vi) |
| BR-06 giao dịch đến muộn không phát hành vé, hoàn tiền | TC-046 (issueTickets từ chối khi chỗ đã trả) | Có một phần. Hoàn tiền khoản thu đến muộn thuộc UC-010 (DC-PayTicketOnlineService), chưa có P07, ngoài phạm vi |
| BR-07 hoàn 100% giá vé | TC-061, TC-062, TC-064 | Có |
| BR-08 hoàn tiền qua cùng kênh mua vé | TC-056 đến TC-060; TC-051, TC-052 | Có, ở mức entity (nhận diện vé trực tuyến cần hoàn qua cổng). Hoàn tiền mặt tại quầy thuộc UC-018, ngoài phạm vi |
| BR-09 chuyến đã huỷ không huỷ lại | TC-004, TC-005 | Có |
| BR-10 chuyến từ giờ xuất bến không huỷ được | TC-001, TC-003, TC-005 | Có |
| BR-11 báo SMS cho mọi hành khách đã có vé | - | Không: gom vé theo số điện thoại và gửi SMS thuộc DC-TripTicketCancellation, DC-CancelTripService (ngoài phạm vi); kiểm thử với Cổng SMS giả lập ở mức control |
| UC-009 luồng 2a (chưa chọn chuyến) | - | Không: thuộc UC-008 và giao diện, ngoài phạm vi |
| UC-009 luồng 4a (chỗ không còn trống) | TC-016, TC-017, TC-018 | Có, ở mức entity |
| UC-009 luồng 4b (hơn 5 chỗ) | TC-011 | Có, ở mức entity |
| UC-009 luồng 4c (chuyến đã tới giờ xuất bến) | TC-007 | Có, ở mức entity |
| UC-009 luồng 5a (hết thời hạn giữ chỗ) | TC-026, TC-027, TC-033, TC-046, TC-035 đến TC-038 | Có, ở mức entity |
| UC-009 luồng 7a (thiếu họ tên hoặc số điện thoại) | TC-028, TC-029, TC-030 | Có |
| UC-009 luồng 8a và *a (trả chỗ ngay) | TC-035 đến TC-038 | Có, ở mức entity |
| UC-009 luồng 11a (SMS mã vé không gửi được) | - | Không: thuộc DC-Ticket.recordSmsNotSent, hoãn lần chạy sau |
| UC-017 luồng 4a (chuyến đã huỷ) | TC-004, TC-005 | Có |
| UC-017 luồng 4b (chuyến đã tới giờ xuất bến) | TC-003, TC-005 | Có |
| UC-017 bước 7 và luồng 7a (chuyển vé sang Đã huỷ) | TC-051, TC-052 (phần của một vé) | Có một phần. Duyệt tập vé của chuyến và luồng 7a (chuyến không có vé) thuộc DC-TripTicketCancellation.cancelTicketsOfTrip (ngoài phạm vi) |
| UC-017 bước 11 (hoàn tiền vé trực tuyến) | TC-056 đến TC-061 | Có, ở mức entity |
| UC-017 luồng 9a (SMS huỷ chuyến không gửi được) | - | Không: thuộc DC-Ticket.markCancelNoticeNotSent, hoãn lần chạy sau |
| UC-017 luồng 12a (hoàn tiền không thành công) | - | Không: thuộc DC-Ticket.recordRefundNotCompleted, hoãn lần chạy sau |
| UC-017 luồng *a (bỏ yêu cầu huỷ chuyến) | - | Không: không đổi dữ liệu, thuộc giao diện và control, ngoài phạm vi |

Tóm tắt độ phủ C0, C1 so với MUC_TIEU_PHU (mặc định: 100% C1 cho phương thức ưu tiên Cao; operation không có thiết kế method ở P12 F3 và không có mã nguồn thì mục tiêu là mọi lớp tương đương và giá trị biên có TC, C0 và C1 ghi "Đo khi có mã nguồn"):

| Operation | Ưu tiên | Mục tiêu | C0 đạt được | C1 đạt được | Đạt (Có / Không: lý do) |
|---|---|---|---|---|---|
| DC-Trip.cancel | Cao | 100% C1 | 7/7 (100%) | 8/8 (100%) | Có |
| DC-Trip.isBeforeDeparture | Cao | Mọi EC, BV có TC | Đo khi có mã nguồn | Đo khi có mã nguồn | Có (EC-08, EC-09, EC-11, EC-12, BV-03, BV-04 có TC; EC-10 theo ASM-57) |
| DC-Booking.isSeatCountWithinLimit | Cao | Mọi EC, BV có TC | Đo khi có mã nguồn | Đo khi có mã nguồn | Có (EC-13, EC-14, BV-05 đến BV-07 có TC; EC-15 không thể xảy ra) |
| DC-Booking.holdSeats | Cao | 100% C1 | 8/8 (100%) | 10/10 (100%) | Có |
| DC-Booking.isHoldExpired | Cao | Mọi EC, BV có TC | Đo khi có mã nguồn | Đo khi có mã nguồn | Có (EC-29 đến EC-31, BV-12, BV-13 có TC; EC-32 theo ASM-57) |
| DC-Booking.recordTravelerInfo | Cao | 100% C1 | 12/12 (100%) | 16/16 (100%) | Có |
| DC-Booking.releaseHeldSeats | Cao | 100% C1 | 9/9 (100%) | 11/11 (100%) | Có |
| DC-Booking.issueTickets | Cao | 100% C1 | 11/11 (100%) | 14/14 (100%) | Có |
| DC-Ticket.cancelForTrip | Cao | 100% C1 | 7/7 (100%) | 8/8 (100%) | Có |
| DC-Ticket.isOnlineRefundPending | Cao | Mọi EC, quy tắc DT7 có TC | Đo khi có mã nguồn | Đo khi có mã nguồn | Có (EC-66 đến EC-70, DT7-R1 đến DT7-R4 có TC; DT7-R5, DT7-R6 không thể xảy ra) |
| DC-Ticket.calculateRefundAmount | Cao | 100% C1 | 5/5 (100%) | 5/5 (100%) | Có |

Các số C0, C1 là độ phủ theo CFG mức thiết kế (P12 F3), không phải đo từ mã nguồn; khi có mã nguồn chạy lại Bước 4 với mã đính kèm để cập nhật.

## F5. Khung mã test

Không sinh: SINH_MA_TEST = Không có.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-77 | Khi DC-Booking.holdSeats ném SeatsUnavailableException ở một chỗ mà các chỗ đứng trước (theo mã chỗ tăng dần) đã được markHeld, thì ngay sau khi ngoại lệ lan ra, Booking và các chỗ đó ở trạng thái nào? (Mọi đối tượng quay về trạng thái trước khi gọi: các chỗ đã giữ trở lại AVAILABLE, Booking vẫn SELECTING / Không bảo đảm gì ở mức đối tượng, chỉ bảo đảm hoàn tác ở mức giao dịch lưu trữ nên đối tượng bị bỏ) | TC-018; DC-Booking.holdSeats hậu điều kiện khi thất bại; ST-03 chuyển 2 và sự kiện bị từ chối dòng 4; ST-02 chuyển 2 | P12 F2 DC-Booking.holdSeats chỉ nêu hậu điều kiện khi thành công; DC-BookTicketOnlineService.processSeatSelection nêu "Hậu thất bại: không lưu gì (giao dịch hoàn tác)"; P12 F6 ST-03 ghi "giao dịch hoàn tác nên lần đặt bị bỏ" mà không nói trạng thái của đối tượng trong bộ nhớ |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-57 | Các lớp đầu vào là tham số null hoặc vi phạm tiền điều kiện hay ràng buộc thuộc tính mà P12 không nêu hành vi (reason, now, seatFare, travelerName, travelerPhone, ticketCodes, transaction bằng null; seatFare, fare không dương; holdSeats với hơn 5 chỗ; họ tên dài hơn 100 ký tự; số điện thoại chứa ký tự khác chữ số; issueTickets khi Booking HOLDING chưa ghi người đi) được liệt kê ở EC nhưng không có test case trong lần chạy này; sẽ thiết kế TC khi P12 bổ sung hành vi. | Chọn không thiết kế TC thay vì suy ra ngoại lệ, vì P12 chỉ nêu ngoại lệ cho các vi phạm có tên; giả định chỉ xác định phạm vi test, không chọn hành vi nghiệp vụ nên không đổi luồng, dữ liệu, quy tắc và không cần Q (Conventions C1 mục 2); số chữ số hoặc định dạng số điện thoại đã có Q-44 | EC-06, EC-07, EC-10, EC-24, EC-26, EC-28, EC-32, EC-41, EC-44, EC-58, EC-76 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P12 | F2 DC-Booking.holdSeats (hậu điều kiện thất bại); F6 ST-03 | Hậu điều kiện chỉ nêu khi thành công; khi ngoại lệ ném giữa chừng, trạng thái Booking và các chỗ đã markHeld ở mức đối tượng không được nêu (Q-77) | Bổ sung hậu điều kiện khi thất bại, hoặc ghi rõ đối tượng bị bỏ và chỉ giao dịch lưu trữ được bảo đảm |
| P12 | F7 DC-Booking.holdStartedAt; F2 DC-Booking.holdSeats | Hậu điều kiện "holdStartedAt = now" không quan sát được qua operation công khai (không có getter, P12 Vấn đề còn mở cũng ghi không operation nào đọc) | Thêm getHoldStartedAt(): Optional<LocalDateTime>, hoặc bỏ holdStartedAt khỏi hậu điều kiện (đã kiểm tra gián tiếp qua holdExpiry = holdStartedAt + HOLD_DURATION) |
| P12 | F2 DC-Ticket (purchaseChannel, paymentStatus), F7 | Hậu điều kiện createTicket ghi purchaseChannel = ONLINE và paymentStatus = PAID nhưng không có getter nên không quan sát được trực tiếp | Thêm getPurchaseChannel(): PurchaseChannel và getPaymentStatus(): PaymentStatus |
| P12 | F2 DC-Ticket, DC-Booking (tạo vé kênh COUNTER, vé UNPAID) | Điều kiện đầu paymentStatus = UNPAID và purchaseChannel = COUNTER của cancelForTrip, isOnlineRefundPending, calculateRefundAmount không dựng được bằng operation công khai (createTicket luôn ONLINE, PAID); TC-052, TC-055, TC-059, TC-060, TC-065 phải dùng bộ dựng chỉ có ở test | Khi P07 của UC-004, UC-005, UC-006 có, thêm operation tạo vé kênh quầy (đã thanh toán, chưa thanh toán); cho đến lúc đó chấp nhận bộ dựng test |
| P12 | Bảng Chữ ký interface tạm DC-Money; F2 | Không có operation tạo giá trị Money từ số tiền nên không viết được điều kiện đầu và dữ liệu vào bằng Money cụ thể | Khi chạy P12 cho PKG-31 thêm factory (ví dụ Money.of(amount: long)) và so sánh bằng |
| P12 | F2 DC-Booking.issueTickets (tiền điều kiện) | Tiền điều kiện không nêu việc người đi đã được ghi (recordTravelerInfo) dù createTicket cần họ tên và số điện thoại; hành vi khi chưa ghi không có (nằm trong ASM-57) | Thêm vào tiền điều kiện "travelerName, travelerPhone đã ghi" và ngoại lệ tương ứng |
| P12 | F2 DC-Booking.holdSeats, DC-Booking.recordTravelerInfo, DC-Trip.cancel, DC-Ticket.calculateRefundAmount | Không nêu hành vi khi tham số null, khi số chỗ hơn 5 (tiền điều kiện của holdSeats trong khi createBooking không giới hạn số chỗ), khi họ tên dài hơn 100 ký tự (ràng buộc F7), khi fare không dương | Ghi hành vi mong đợi (ngoại lệ) hoặc ghi "bên gọi bảo đảm" cho từng trường hợp |

## Vấn đề còn mở

- Ngưỡng của mục 3 ("khoảng 10 operation được chọn hoặc 60 TC"): lần chạy này chọn 11 operation và 65 TC, vượt nhẹ. Lý do: có 18 operation ưu tiên Cao trong phạm vi (theo Bước 1), nên đã chọn 11 operation hiện thực BR hoặc sự kiện state machine có nhiều nhánh nhất; các TC vòng lặp (n-1, n) chiếm phần tăng thêm. Không tách thêm vì các TC cùng operation khác nhau chủ yếu ở dữ liệu.
- Operation hoãn sang lần chạy sau (F1, cột Chọn): DC-Trip.Trip (constructor); DC-Booking.createBooking, calculateTotalAmount, clearHoldExpiry; DC-Ticket.createTicket, recordSmsNotSent, markRefunded, recordRefundNotCompleted, markCancelNoticeNotSent (9 operation, gồm 7 Cao và 2 Trung bình). Đề nghị chạy tiếp theo lớp: lần sau DC-Booking và DC-Trip (4 operation), rồi DC-Ticket (5 operation), với MA_TC_BAT_DAU = TC-066. Target 1 đạt (mọi operation có dòng F1 và quyết định chọn); Target 6 đạt cho các operation được chọn, các luồng thay thế của operation hoãn ghi ở F4.
- Target 7: TC-018 có kết quả "Chưa xác định: chờ Q-77" cho phần trạng thái sau lỗi; phần ngoại lệ SeatsUnavailableException đã xác định.
- Target 9: operation Trip.isBeforeDeparture, Booking.isSeatCountWithinLimit, Booking.isHoldExpired, Ticket.isOnlineRefundPending không có thiết kế method ở P12 F3 và chưa có mã nguồn nên C0, C1 ghi "Đo khi có mã nguồn". C0, C1 của 7 operation còn lại tính trên CFG mức thiết kế.
- Target 12: TC-005, TC-027, TC-030 có hai điều kiện sai cùng lúc theo quy tắc bảng quyết định (DT1-R4, DT4-R5, DT4-R4); điều kiện được kiểm trước và căn cứ ghi ở F2.1.4 (status trước now, P12 F2 và ASM-26) và F2.6.4 (hết thời hạn trước thông tin thiếu, P12 F3 bước 2 trước bước 3).
- Target 13: không áp dụng vì không sinh khung mã test.
- Chọn giữa hai quy tắc (Conventions C9): (1) F3 của P12 là thiết kế method, không phải đặc tả; Bước 3.3 cho phép dùng thứ tự F3 làm căn cứ gộp khi F2 và P04 không mâu thuẫn, còn Bước 3.6 yêu cầu không tự quyết kết quả khi đặc tả không nói tổ hợp hai điều kiện cùng sai. Đã chọn dùng thứ tự F3 ở DT4-R5 và DT5-R3 (và thứ tự F6 ở DT2-R4) vì P12 F6 hoặc F3 nêu thứ tự một cách tường minh; nếu P12 F3 thay đổi thứ tự kiểm tra thì các TC này đổi theo. (2) Conventions C1 mục 2 (CO_NHAN) yêu cầu ASM có thể đổi quy tắc đi kèm Q, còn F2.x.2 của X2 cho phép "một Q hoặc một ASM" cho lớp null; đã chọn ASM-57 không kèm Q vì ASM-57 không chọn hành vi.
- Các TC chuẩn bị điều kiện đầu bằng chuỗi operation công khai (HOLD, INFO, ISS dùng holdSeats, recordTravelerInfo, issueTickets): mỗi TC dựng đối tượng riêng nên độc lập, nhưng lỗi ở operation chuẩn bị làm hỏng nhiều TC; khuyến nghị dùng hàm dựng riêng trong mã test.
- Money, PhoneNumber, TicketCode, PaymentTransaction dùng fake hoặc dummy theo chữ ký tạm của P12; khi P12 chạy cho PKG-29, PKG-31, cập nhật test double và dữ liệu vào.
