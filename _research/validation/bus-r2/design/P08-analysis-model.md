# P08 - Mô hình phân tích hợp nhất - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P08 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P01-actors.md (phiên bản 1.0, Mục 2); P02-usecases.md (phiên bản 1.1, Mục 4); P05-glossary.md (phiên bản 1.0, Mục 2); P06-supplementary-spec.md (phiên bản 1.0, Mục 3, 5 và 6); P07-uc-analysis/UC-009-book-ticket-online-analysis.md (phiên bản 1.0; F3.4, F6, F8 b), Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở); P07-uc-analysis/UC-017-cancel-trip-analysis.md (phiên bản 1.0; cùng các mục). Không dùng P04-uc-specs (đầu vào không bắt buộc). Placeholder CACH_CHIA_VIEW: Không có (áp dụng quy tắc mặc định ở F5). YEU_CAU_BO_SUNG: phạm vi lần chạy là UC-009 và UC-017, các use case khác trong P02 chưa được phân tích. Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-58, ASM-42; lần chạy này cấp Q-59 đến Q-61, ASM-43 đến ASM-44 |
| Phạm vi | Toàn hệ thống theo P02 (27 use case trong phạm vi, không tính UC-013 đã loại); lần chạy này hợp nhất 2 use case đã có P07: UC-009, UC-017 |
| Mã Q, ASM cuối đã cấp | Q-61, ASM-44 |

## F1. Độ phủ use case

| UC | Tên | File P07 | Trạng thái |
|---|---|---|---|
| UC-001 | Đăng ký tài khoản (Register Account) | - | Chưa phân tích |
| UC-002 | Quản lý tài khoản nhân viên (Manage Staff Accounts) | - | Chưa phân tích |
| UC-003 | Đăng nhập (Log In) | - | Chưa phân tích |
| UC-004 | Bán vé tại quầy (Sell Ticket At Counter) | - | Chưa phân tích |
| UC-005 | Nhận đặt chỗ qua điện thoại (Take Phone Reservation) | - | Chưa phân tích |
| UC-006 | Thu tiền vé đặt qua điện thoại (Collect Payment For Phone Reservation) | - | Chưa phân tích |
| UC-007 | Huỷ vé đặt chỗ quá hạn (Cancel Overdue Reservation) | - | Chưa phân tích |
| UC-008 | Tra cứu chuyến xe (Search Trips) | - | Chưa phân tích |
| UC-009 | Đặt vé trực tuyến (Book Ticket Online) | P07-uc-analysis/UC-009-book-ticket-online-analysis.md | Đã phân tích |
| UC-010 | Thanh toán vé trực tuyến (Pay Ticket Online) | - | Chưa phân tích |
| UC-011 | Xem lịch sử vé (View Ticket History) | - | Chưa phân tích |
| UC-012 | Trả vé (Return Ticket) | - | Chưa phân tích |
| UC-013 | Trả vé tại quầy (Return Ticket At Counter) | - | Loại (gộp vào UC-012), không tính vào phạm vi |
| UC-014 | Đổi vé trực tuyến (Exchange Ticket Online) | - | Chưa phân tích |
| UC-015 | Đổi vé tại quầy (Exchange Ticket At Counter) | - | Chưa phân tích |
| UC-016 | Lập lịch chạy tuần (Create Weekly Schedule) | - | Chưa phân tích |
| UC-017 | Huỷ chuyến (Cancel Trip) | P07-uc-analysis/UC-017-cancel-trip-analysis.md | Đã phân tích |
| UC-018 | Hoàn tiền mặt chuyến bị huỷ (Refund Cash For Cancelled Trip) | - | Chưa phân tích |
| UC-019 | Quản lý danh mục bến xe (Manage Station Catalog) | - | Chưa phân tích |
| UC-020 | Quản lý danh mục tuyến xe (Manage Route Catalog) | - | Chưa phân tích |
| UC-021 | Quản lý danh mục xe (Manage Vehicle Catalog) | - | Chưa phân tích |
| UC-022 | Quản lý danh mục tài xế (Manage Driver Catalog) | - | Chưa phân tích |
| UC-023 | Đặt giá vé (Set Ticket Fare) | - | Chưa phân tích |
| UC-024 | Đặt mức tăng giá ngày lễ (Set Holiday Surcharge) | - | Chưa phân tích |
| UC-025 | Gửi danh sách hành khách cho phụ xe (Send Passenger List To Attendant) | - | Chưa phân tích |
| UC-026 | Soát vé hành khách lên xe (Check Ticket At Boarding) | - | Chưa phân tích |
| UC-027 | Xem báo cáo doanh thu (View Revenue Report) | - | Chưa phân tích |
| UC-028 | Xem báo cáo tỉ lệ lấp đầy (View Occupancy Report) | - | Chưa phân tích |

Tổng kết: 27 use case trong phạm vi, 2 đã phân tích, 25 chưa phân tích (chi tiết ở Vấn đề còn mở).

## F2. Nhật ký hợp nhất

| STT | Lớp gốc (AC, tên) | UC nguồn | Tình huống | Kết quả | Bằng chứng (GL, BR, bước UC) |
|---|---|---|---|---|---|
| 1 | AC-B-BookTicketOnlineForm, BookTicketOnlineForm | UC-009 | Giữ nguyên | Giữ | Bước 1, 2a, 3, 4a, 4b, 4c, 5a, 6, 7a, 8a, 12, *a; giao diện người dùng của ACT-01; BR-01, BR-02, BR-03, BR-05 |
| 2 | AC-B-SmsGateway, SmsGateway | UC-009 | Giữ nguyên | Giữ | Bước 10, 11; ACT-07; NFR-12 |
| 3 | AC-C-BookTicketOnlineController, BookTicketOnlineController | UC-009 | Giữ nguyên | Giữ | Bước 1 đến 12, *a; BR-03 |
| 4 | AC-C-SearchTripsController, SearchTripsController | UC-009 | Giữ nguyên | Giữ, trạng thái Tạm (chờ P07 của UC-008) | Bước 2 (include UC-008) |
| 5 | AC-C-PayTicketOnlineController, PayTicketOnlineController | UC-009 | Giữ nguyên | Giữ, trạng thái Tạm (chờ P07 của UC-010) | Bước 5a, 8 (include UC-010); ASM-41 |
| 6 | AC-E-Trip, Trip | UC-009 | Giữ nguyên | Giữ | GL-03; bước 4; BR-05 |
| 7 | AC-E-Seat, Seat | UC-009 | Giữ nguyên | Giữ (một lớp chỗ của chuyến xe theo ASM-43) | GL-01, GL-02, GL-08; bước 4, 5; BR-02; NFR-04 |
| 8 | AC-E-Fare, Fare | UC-009 | Giữ nguyên | Giữ | GL-05, GL-16; bước 5; REQ-60, REQ-61; ASM-40 |
| 9 | AC-E-Booking, Booking | UC-009 | Giữ nguyên | Giữ | GL-12; bước 4, 5, 8, 9; BR-01, BR-03, BR-04 |
| 10 | AC-E-Ticket, Ticket | UC-009 | Giữ nguyên | Giữ | GL-23, GL-15; bước 9, 11a; BR-04; ASM-39 |
| 11 | AC-B-CancelTripForm, CancelTripForm | UC-017 | Giữ nguyên | Giữ | Bước 1, 2, 3, 4a, 4b, 14, *a; giao diện người dùng của ACT-03; BR-09, BR-10 |
| 12 | AC-B-SmsGateway, SmsGateway | UC-017 | Tái dùng mã | Giữ; hợp trách nhiệm sendTripCancellationBySms và thuộc tính noticeContent vào AC-B-SmsGateway | Bước 8, 9; cùng một hệ thống ngoài ACT-07 với dòng của UC-009; NFR-12; BR-11 |
| 13 | AC-B-PaymentGateway, PaymentGateway | UC-017 | Giữ nguyên | Giữ | Bước 11, 12; ACT-06; NFR-11 |
| 14 | AC-C-CancelTripController, CancelTripController | UC-017 | Giữ nguyên | Giữ | Bước 1 đến 14, *a; BR-07, BR-08, BR-09, BR-10, BR-11 |
| 15 | AC-E-Trip, Trip | UC-017 | Tái dùng mã | Giữ; hợp trách nhiệm và thuộc tính (status, cancelReason, vehicle, driver) vào AC-E-Trip, xem F2a | GL-03, GL-04, GL-07; bước 2, 4, 5; BR-09, BR-10 |
| 16 | AC-E-Ticket, Ticket | UC-017 | Tái dùng mã | Giữ; hợp trách nhiệm và thuộc tính vào AC-E-Ticket, xem F2a | GL-23, GL-24, GL-25, GL-10, GL-11; bước 7 đến 14; BR-04, BR-07, BR-08, BR-11 |
| 17 | AC-E-PaymentTransaction, PaymentTransaction | UC-017 | Giữ nguyên | Giữ | GL-06; bước 13; ASM-32; NFR-06 |

## F2a. Nhật ký trách nhiệm, thuộc tính và cặp đã xét

| STT | Lớp | Mục gốc (trách nhiệm, thuộc tính hoặc cặp lớp) | UC nguồn | Tình huống | Kết quả | Bằng chứng |
|---|---|---|---|---|---|---|
| 1 | AC-E-Trip | Trách nhiệm checkDepartureNotReached: UC-009 (BR-05) và UC-017 (BR-10) | UC-009, UC-017 | Gộp trách nhiệm cùng tên, cùng ý nghĩa | Giữ một trách nhiệm checkDepartureNotReached; mô tả nêu cả hai BR | GL-07 "Mốc để xét ngừng bán vé trực tuyến (BR-05) và để xét huỷ chuyến (BR-10)"; P07 UC-017 ghi cùng ý nghĩa |
| 2 | AC-E-Ticket | Thuộc tính status: UC-009 chỉ có giá trị Đã phát hành, UC-017 thêm giá trị Đã huỷ | UC-009, UC-017 | Thuộc tính mâu thuẫn | Hợp thành status (Đã phát hành, Đã huỷ); giá trị đã trả, đã đổi chờ P07 của UC-012, UC-014; không mâu thuẫn nên không cần Q | GL-23, GL-24; ASM-29 của P04 UC-017 |
| 3 | AC-E-Ticket | Thuộc tính purchaseChannel: UC-009 chỉ có Trực tuyến, UC-017 có Trực tuyến và Tại quầy | UC-009, UC-017 | Thuộc tính mâu thuẫn | Hợp thành purchaseChannel (Trực tuyến, Tại quầy) | GL-11, GL-27, GL-28; BR-08 |
| 4 | AC-E-Trip | Thuộc tính vehicleType (UC-009) và vehicle (UC-017) | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ cả hai thuộc tính: vehicleType là loại xe để xác định giá vé, vehicle là xe đảm nhiệm chuyến; vehicleType suy được từ xe nhưng Xe chưa có lớp (UC-021 chưa phân tích), xem Vấn đề còn mở | GL-03, GL-14; REQ-47, REQ-60 |
| 5 | AC-E-Ticket | Thuộc tính smsStatus (UC-009, SMS mã vé) và cancelNoticeStatus (UC-017, SMS báo huỷ chuyến) | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ hai thuộc tính: hai SMS có sự kiện, nội dung và thời điểm khác nhau, cần ghi nhận riêng | NFR-12; BR-11; ASM-39, ASM-42 |
| 6 | AC-B-SmsGateway | Trách nhiệm sendTicketCodesBySms (UC-009) và sendTripCancellationBySms (UC-017) | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ hai trách nhiệm: nội dung gửi khác nhau (mã vé; thông báo huỷ chuyến kèm tuyến, giờ xuất bến); P12 có thể hợp thành một thao tác gửi tổng quát | NFR-12; REQ-20, REQ-56 |
| 7 | AC-E-Booking, AC-E-Ticket | Thuộc tính travelerName, travelerPhone có ở cả hai lớp | UC-009 | Cặp đã xét, giữ tách | Giữ ở cả hai: người đi chung của lần đặt (ASM-19) được ghi lên từng vé; không tạo lớp Người đi vì P05 xếp họ tên, số điện thoại người đi là thuộc tính lẻ | GL-17, GL-12; P05 Mục 3 |
| 8 | AC-E-Booking, AC-E-Ticket | Thuộc tính seatFare (lần đặt) và fare (vé) | UC-009 | Cặp đã xét, giữ tách | Giữ hai thuộc tính: giá ghi khi giữ chỗ được chuyển thành giá của vé khi phát hành, hai thời điểm và hai lớp khác nhau | GL-05; ASM-40 |
| 9 | AC-E-Booking, AC-E-Ticket | Cặp lớp đã xét đồng nghĩa | UC-009 | Cặp đã xét, giữ tách | Giữ tách: Booking là nhóm chỗ giữ chỗ và thanh toán chung, Ticket là chứng từ của một chỗ có mã vé riêng | GL-12, GL-23; BR-01, BR-04 |
| 10 | AC-E-Ticket, AC-E-PaymentTransaction | Cặp lớp đã xét đồng nghĩa | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ tách: vé là chứng từ, giao dịch thanh toán là lần thu tiền qua Cổng thanh toán; một giao dịch có thể thu nhiều vé | GL-06, GL-23; ASM-32 |
| 11 | AC-B-SmsGateway, AC-B-PaymentGateway | Hai boundary giao diện hệ thống đã xét gộp | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ tách: hai hệ thống ngoài khác nhau (ACT-07 Cổng SMS, ACT-06 Cổng thanh toán) | P01 Mục 2 ACT-06, ACT-07; NFR-10, NFR-11, NFR-12 |
| 12 | AC-B-BookTicketOnlineForm, AC-B-CancelTripForm | Hai boundary giao diện người dùng đã xét gộp | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ tách: khác tác nhân (ACT-01, ACT-03), khác use case, khác tương tác; mặc định mỗi cặp tác nhân - use case một boundary | P01 Mục 2; A3 |
| 13 | AC-C-BookTicketOnlineController, AC-C-CancelTripController | Hai control đã xét gộp | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ tách: hai use case khác nhau (UC-009, UC-017) | P02 Mục 4; A3 |
| 14 | AC-C-PayTicketOnlineController, AC-B-PaymentGateway, AC-E-PaymentTransaction | Ba lớp khác stereotype có tên gần nhau (Pay, Payment) đã xét | UC-009, UC-017 | Cặp đã xét, giữ tách | Giữ tách: control điều phối UC-010, boundary là Cổng thanh toán, entity là lần thu tiền | GL-06; P01 Mục 2 ACT-06; A3 |
| 15 | AC-C-SearchTripsController, AC-E-Trip | Hai lớp khác stereotype có tên gần nhau (Trip) đã xét | UC-009 | Cặp đã xét, giữ tách | Giữ tách: control điều phối UC-008 Tra cứu chuyến xe, entity là chuyến xe | GL-03; P02 Mục 4 UC-008 |

## F3. Bảng lớp hợp nhất

| AC | Stereotype | Tên | Trách nhiệm (gộp) | Thuộc tính | Dùng trong UC | Loại boundary | Trạng thái |
|---|---|---|---|---|---|---|---|
| AC-B-BookTicketOnlineForm | boundary | BookTicketOnlineForm | // requestBookTicket: nhận yêu cầu mua vé của hành khách (UC-009)<br>// selectSeats: nhận các chỗ hành khách chọn (UC-009)<br>// enterTravelerInfo: nhận họ tên và số điện thoại người đi (UC-009)<br>// cancelBooking: nhận yêu cầu huỷ mua vé của hành khách (UC-009)<br>// notifyNoTripSelected: thông báo chưa chọn được chuyến (UC-009)<br>// notifySeatsUnavailable: thông báo chỗ không còn trống (UC-009; BR-02)<br>// notifySeatLimitExceeded: thông báo giới hạn số chỗ mỗi lần đặt (UC-009; BR-01)<br>// notifyTripDeparted: thông báo chuyến đã đến giờ xuất bến (UC-009; BR-05)<br>// notifyTravelerInfoMissing: thông báo thông tin người đi còn thiếu (UC-009)<br>// notifyPaymentFailed: thông báo thanh toán không thành công (UC-009)<br>// notifyHoldExpired: thông báo hết thời hạn giữ chỗ (UC-009; BR-03)<br>// notifyBookingCancelled: thông báo đã huỷ yêu cầu mua vé (UC-009)<br>// showIssuedTickets: hiển thị các vé đã phát hành, mã vé và tổng tiền (UC-009) | selectedSeats (chỗ đã chọn)<br>travelerName (Văn bản)<br>travelerPhone (Văn bản)<br>issuedTickets (mã vé, chuyến, chỗ, giá vé)<br>totalAmount (Số tiền) | UC-009 | Giao diện người dùng | Hoạt động |
| AC-B-SmsGateway | boundary | SmsGateway | // sendTicketCodesBySms: chuyển yêu cầu gửi SMS mã vé cho Cổng SMS và nhận kết quả của lời gọi (UC-009; NFR-12)<br>// sendTripCancellationBySms: chuyển yêu cầu gửi SMS thông báo huỷ chuyến (số điện thoại, tuyến, giờ xuất bến, mã vé) cho Cổng SMS và nhận kết quả của lời gọi (UC-017; NFR-12, ASM-30) | recipientPhone (Văn bản)<br>ticketCodes (Văn bản)<br>noticeContent (Văn bản) | UC-009, UC-017 | Giao diện hệ thống | Hoạt động |
| AC-C-BookTicketOnlineController | control | BookTicketOnlineController | // startBookTicketOnline: điều phối đặt vé trực tuyến, gọi UC-008 để hành khách tìm chuyến (UC-009)<br>// processSeatSelection: điều phối kiểm tra các chỗ đã chọn, xác định giá vé và giữ chỗ (UC-009)<br>// processTravelerInfo: điều phối ghi người đi, gọi UC-010, phát hành vé, gửi mã vé và hiển thị kết quả (UC-009)<br>// requestCancelBooking: điều phối huỷ yêu cầu mua vé của hành khách (UC-009)<br>// startWaitingForPaymentResult: bắt đầu chờ kết quả thanh toán trong thời hạn giữ chỗ (UC-009; BR-03)<br>// stopWaitingForPaymentResult: dừng chờ khi đã có kết quả thanh toán hoặc use case kết thúc (UC-009)<br>// handleHoldExpiry: xử lý khi hết thời hạn giữ chỗ (after(BR-03)) (UC-009) | - | UC-009 | - | Hoạt động |
| AC-C-SearchTripsController | control | SearchTripsController | // searchTrips: điều phối tra cứu chuyến xe của UC-008 (tạm, chờ P07 của UC-008) (UC-009) | - | UC-009 | - | Tạm (chờ P07 của UC-008) |
| AC-C-PayTicketOnlineController | control | PayTicketOnlineController | // payTicketOnline: điều phối thanh toán vé trực tuyến của UC-010 (tạm, chờ P07 của UC-010) (UC-009)<br>// cancelPayment: dừng phiên thanh toán của lần đặt vé khi hết thời hạn giữ chỗ (UC-009; ASM-41, tạm) | - | UC-009 | - | Tạm (chờ P07 của UC-010) |
| AC-E-Trip | entity | Trip | // checkDepartureNotReached: kiểm tra giờ xuất bến chưa tới (UC-009 theo BR-05, UC-017 theo BR-10)<br>// listTripsInSchedule: cung cấp các chuyến trong lịch chạy kèm tuyến, giờ xuất bến, xe, tài xế, trạng thái (UC-017)<br>// checkNotCancelled: kiểm tra chuyến chưa ở trạng thái Đã huỷ (UC-017; BR-09)<br>// cancelTrip: chuyển chuyến sang Đã huỷ kèm lý do huỷ chuyến và cung cấp tuyến, giờ xuất bến của chuyến đã huỷ (UC-017) | departureTime (Ngày, Giờ)<br>route (Tuyến xe)<br>vehicleType (Loại xe)<br>status (Trạng thái: Chưa huỷ, Đã huỷ)<br>cancelReason (Trạng thái: Xe hỏng, Thời tiết)<br>vehicle (Xe)<br>driver (Tài xế) | UC-009, UC-017 | - | Hoạt động |
| AC-E-Seat | entity | Seat | // checkAvailable: kiểm tra chỗ chưa có vé và chưa bị giữ (UC-009; BR-02)<br>// markHeld: chuyển chỗ sang đang giữ, chỉ một yêu cầu giữ được chỗ (UC-009; NFR-04)<br>// markSold: chuyển chỗ sang đã bán khi vé được phát hành (UC-009)<br>// markAvailable: trả chỗ về trạng thái trống (UC-009) | seatCode (Văn bản)<br>tripState (Trạng thái: Trống, Đang giữ, Đã bán) | UC-009 | - | Hoạt động |
| AC-E-Fare | entity | Fare | // determineFare: xác định giá vé một chỗ theo tuyến xe, loại xe và mức tăng giá (UC-009; REQ-60, REQ-61, ASM-40) | route (Tuyến xe)<br>vehicleType (Loại xe)<br>amount (Số tiền)<br>surchargePercent (Phần trăm, nếu có) | UC-009 | - | Hoạt động |
| AC-E-Booking | entity | Booking | // createBooking: tạo lần đặt vé ở trạng thái đang chọn cho chuyến và các chỗ đã chọn (UC-009)<br>// checkSeatCountWithinLimit: kiểm tra số chỗ không quá giới hạn mỗi lần đặt (UC-009; BR-01)<br>// holdSeats: giữ các chỗ, ghi giá vé, đặt thời điểm bắt đầu và thời hạn giữ chỗ (UC-009; BR-03)<br>// recordTravelerInfo: ghi họ tên, số điện thoại người đi và kiểm tra đã được cung cấp (UC-009)<br>// calculateTotalAmount: tính tổng tiền bằng tổng giá vé các chỗ (UC-009)<br>// releaseHeldSeats: trả lại các chỗ đang giữ cho người khác (UC-009; BR-03, ASM-24)<br>// issueTickets: phát hành vé cho các chỗ đang giữ, mỗi chỗ một vé (UC-009; BR-04) | trip (Chuyến xe)<br>seatCodes (Văn bản)<br>status (Trạng thái: Đang chọn, Đang giữ chỗ, Đã phát hành vé, Đã trả chỗ)<br>holdStartedAt (Giờ)<br>holdExpiry (Giờ)<br>travelerName (Văn bản)<br>travelerPhone (Văn bản)<br>seatFare (Số tiền) | UC-009 | - | Hoạt động |
| AC-E-Ticket | entity | Ticket | // createTicket: khởi tạo vé gắn chuyến, chỗ, người đi, giá vé, kênh mua vé trực tuyến (UC-009)<br>// generateTicketCode: gán mã vé riêng cho vé (UC-009; BR-04)<br>// recordSmsNotSent: ghi nhận mã vé chưa gửi được qua SMS (UC-009; ASM-39)<br>// cancelTicketsOfTrip: chuyển mọi vé đang có hiệu lực của chuyến sang Đã huỷ, đặt trạng thái hoàn tiền Chưa hoàn cho vé đã thanh toán (ASM-29) và cung cấp các vé đã huỷ (UC-017)<br>// groupTicketCodesByTravelerPhone: gom mã vé của các vé đã huỷ theo số điện thoại người đi để mỗi số nhận một SMS (UC-017; BR-04, ASM-30)<br>// recordCancelNoticeNotSent: ghi nhận các vé của một số điện thoại chưa được báo huỷ chuyến qua SMS (UC-017; ASM-31, ASM-42)<br>// selectOnlineTicketsToRefund: chọn các vé mua trực tuyến đã thanh toán trong số vé đã huỷ còn ở trạng thái hoàn tiền Chưa hoàn (UC-017; BR-08)<br>// calculateRefundAmount: tính số tiền hoàn bằng 100% giá vé đã ghi của vé (UC-017; BR-07)<br>// markRefunded: chuyển trạng thái hoàn tiền của vé sang Đã hoàn khi Cổng thanh toán xác nhận đã hoàn (UC-017; ASM-29)<br>// recordRefundNotCompleted: giữ trạng thái hoàn tiền Chưa hoàn và ghi nhận vé hoàn tiền không thành công (UC-017; ASM-33, ASM-42)<br>// summarizeTripCancellation: tổng hợp số vé đã huỷ, số điện thoại đã báo và chưa báo được, vé mua trực tuyến đã hoàn và chưa hoàn được, số vé mua tại quầy chờ hoàn tiền mặt (UC-017; BR-08) | ticketCode (Văn bản)<br>travelerName (Văn bản)<br>travelerPhone (Văn bản)<br>fare (Số tiền)<br>purchaseChannel (Trạng thái: Trực tuyến, Tại quầy)<br>status (Trạng thái: Đã phát hành, Đã huỷ)<br>smsStatus (Trạng thái: Chưa gửi được)<br>paymentStatus (Trạng thái: Đã thanh toán, Chưa thanh toán)<br>refundStatus (Trạng thái: Chưa hoàn, Đã hoàn)<br>cancelNoticeStatus (Trạng thái: Chưa báo được)<br>refundAttemptStatus (Trạng thái: Hoàn không thành công) | UC-009, UC-017 | - | Hoạt động |
| AC-B-CancelTripForm | boundary | CancelTripForm | // requestCancelTrip: nhận yêu cầu huỷ chuyến của nhân viên điều hành (UC-017)<br>// showScheduledTrips: hiển thị các chuyến trong lịch chạy kèm tuyến, giờ xuất bến, xe, tài xế, trạng thái chuyến (UC-017)<br>// selectTripAndReason: nhận chuyến cần huỷ và lý do huỷ chuyến (UC-017)<br>// notifyTripAlreadyCancelled: thông báo chuyến đã bị huỷ (UC-017; BR-09)<br>// notifyTripDeparted: thông báo chuyến đã đến giờ xuất bến (UC-017; BR-10)<br>// abortCancelTrip: nhận yêu cầu bỏ huỷ chuyến của nhân viên điều hành (UC-017)<br>// notifyCancelTripAborted: thông báo đã bỏ yêu cầu huỷ chuyến (UC-017)<br>// showCancellationResult: hiển thị kết quả huỷ chuyến (UC-017) | scheduledTrips (danh sách tuyến, giờ xuất bến, xe, tài xế, trạng thái chuyến)<br>selectedTrip (Chuyến xe)<br>cancelReason (Trạng thái: Xe hỏng, Thời tiết)<br>cancellationResult (kết quả huỷ chuyến) | UC-017 | Giao diện người dùng | Hoạt động |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestTicketRefund: chuyển yêu cầu hoàn tiền một vé (giao dịch thanh toán, mã vé, số tiền hoàn) cho Cổng thanh toán và nhận kết quả hoàn tiền (UC-017; NFR-11, ASM-32) | transactionCode (Văn bản)<br>ticketCode (Văn bản)<br>refundAmount (Số tiền)<br>refundResult (Trạng thái: Thành công, Không thành công) | UC-017 | Giao diện hệ thống | Hoạt động |
| AC-C-CancelTripController | control | CancelTripController | // startCancelTrip: điều phối bắt đầu huỷ chuyến, lấy các chuyến trong lịch chạy để hiển thị (UC-017)<br>// processTripCancellation: điều phối kiểm tra chuyến, huỷ chuyến, huỷ vé, báo SMS, hoàn tiền và hiển thị kết quả (UC-017)<br>// requestAbortCancelTrip: điều phối bỏ yêu cầu huỷ chuyến, không thay đổi dữ liệu (UC-017)<br>// cancelOverdueReservationMark: huỷ mốc 60 phút trước giờ xuất bến của UC-007 cho chuyến đã huỷ (UC-017; ASM-28)<br>// cancelPassengerListMark: huỷ mốc 15 phút trước giờ xuất bến của UC-025 cho chuyến đã huỷ (UC-017; ASM-28) | - | UC-017 | - | Hoạt động |
| AC-E-PaymentTransaction | entity | PaymentTransaction | // recordRefund: ghi nhận khoản hoàn của một vé vào giao dịch thanh toán đã thu tiền vé, cộng vào số đã hoàn của giao dịch và không để số đã hoàn vượt số đã thu (UC-017; ASM-32, NFR-06) | transactionCode (Văn bản)<br>collectedAmount (Số tiền)<br>refundedAmount (Số tiền) | UC-017 | - | Hoạt động |

Không có lớp nào bị gộp trong lần chạy này, nên không có dòng "Gộp vào". Tên mỗi lớp là một khái niệm, định nghĩa một câu:

- BookTicketOnlineForm: giao diện hành khách dùng để mua vé trực tuyến.
- SmsGateway: giao diện hệ thống tới Cổng SMS của nhà mạng.
- BookTicketOnlineController: bộ điều phối use case Đặt vé trực tuyến.
- SearchTripsController: bộ điều phối use case Tra cứu chuyến xe (tạm).
- PayTicketOnlineController: bộ điều phối use case Thanh toán vé trực tuyến (tạm).
- Trip: một lần xe khách chạy trên một tuyến xe vào một giờ xuất bến (GL-03).
- Seat: chỗ cụ thể của một chuyến xe, mang trạng thái bán trên chuyến đó (ASM-43, GL-02).
- Fare: giá vé của một chỗ trên chuyến theo tuyến xe, loại xe và mức tăng giá nếu có (GL-05).
- Booking: nhóm các chỗ của một chuyến xe mà hành khách chọn mua cùng một lúc (GL-12).
- Ticket: chứng từ ghi nhận quyền của một người đi tại một chỗ trên một chuyến xe, có mã vé riêng (GL-23).
- CancelTripForm: giao diện nhân viên điều hành dùng để huỷ chuyến.
- PaymentGateway: giao diện hệ thống tới Cổng thanh toán của đối tác.
- CancelTripController: bộ điều phối use case Huỷ chuyến.
- PaymentTransaction: lần thu tiền vé từ hành khách qua Cổng thanh toán (GL-06).

## F4. Bảng quan hệ

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn UC | Bằng chứng | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| R-01 | BookTicketOnlineForm (AC-B-BookTicketOnlineForm) | BookTicketOnlineController (AC-C-BookTicketOnlineController) | Association | - | - | UC-009 | Link CL02 (P07 UC-009); ai dùng ai | R-UC009-01; tạm thời |
| R-02 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | SearchTripsController (AC-C-SearchTripsController) | Dependency | - | - | UC-009 | Bước 2: UC-009 include UC-008 | R-UC009-02; «include»; tạm thời |
| R-03 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | PayTicketOnlineController (AC-C-PayTicketOnlineController) | Dependency | - | - | UC-009 | Bước 5a, 8: UC-009 include UC-010 | R-UC009-03; «include»; tạm thời |
| R-04 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | Trip (AC-E-Trip) | Association | - | - | UC-009 | Link CL05; bước 4 | R-UC009-04; tạm thời |
| R-05 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | Seat (AC-E-Seat) | Association | - | - | UC-009 | Link CL06; bước 4 | R-UC009-05; tạm thời |
| R-06 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | Fare (AC-E-Fare) | Association | - | - | UC-009 | Link CL07; bước 5, ASM-40 | R-UC009-06; tạm thời |
| R-07 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | Booking (AC-E-Booking) | Association | - | - | UC-009 | Link CL08; bước 4 đến 9 | R-UC009-07; tạm thời |
| R-08 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | Ticket (AC-E-Ticket) | Association | - | - | UC-009 | Link CL09; bước 11a, ASM-39 | R-UC009-08; tạm thời |
| R-09 | BookTicketOnlineController (AC-C-BookTicketOnlineController) | SmsGateway (AC-B-SmsGateway) | Association | - | - | UC-009 | Link CL10; bước 10 | R-UC009-09; tạm thời |
| R-10 | Booking (AC-E-Booking) | Seat (AC-E-Seat) | Association | A 0..* - B 1..5 | - | UC-009 | GL-12 "Nhóm các chỗ của một chuyến xe"; BR-01 (tối đa 5 chỗ mỗi lần đặt); phía Booking theo ASM-44 (Booking có trạng thái "Đã trả chỗ" nên vẫn được lưu sau khi trả chỗ) | R-UC009-10; phía A thay "?" bằng 0..* theo ASM-44 (chờ Q-60); giữ Association vì GL-12 và đặc tả không có câu về vòng đời phụ thuộc |
| R-11 | Booking (AC-E-Booking) | Ticket (AC-E-Ticket) | Association | A 0..1 - B 0..5 | - | UC-009 | GL-12 "Tổng tiền của lần đặt bằng tổng Giá vé của các vé"; BR-01, BR-04 (tối đa 5 chỗ, mỗi chỗ một vé); lần đặt chưa thanh toán thành công không có vé | R-UC009-11; phía A thay "?" bằng 0..1 theo ASM-44 (chờ Q-60); lower 0 vì vé bán tại quầy (UC-004 chưa phân tích, Q-12) chưa chắc thuộc một lần đặt |
| R-12 | Booking (AC-E-Booking) | Trip (AC-E-Trip) | Association | A 0..* - B 1 | - | UC-009 | GL-12 "Nhóm các chỗ của một chuyến xe"; bước 3 và bước 4 | R-UC009-12; giữ dù suy được qua R-21 vì mang ràng buộc mọi chỗ của một lần đặt cùng một chuyến |
| R-13 | CancelTripForm (AC-B-CancelTripForm) | CancelTripController (AC-C-CancelTripController) | Association | - | - | UC-017 | Link CL02 (P07 UC-017); ai dùng ai | R-UC017-01; tạm thời |
| R-14 | CancelTripController (AC-C-CancelTripController) | Trip (AC-E-Trip) | Association | - | - | UC-017 | Link CL03; bước 2, 4, 5 | R-UC017-02; tạm thời |
| R-15 | CancelTripController (AC-C-CancelTripController) | Ticket (AC-E-Ticket) | Association | - | - | UC-017 | Link CL04; bước 7 đến 14 | R-UC017-03; tạm thời |
| R-16 | CancelTripController (AC-C-CancelTripController) | PaymentTransaction (AC-E-PaymentTransaction) | Association | - | - | UC-017 | Link CL05; bước 13 | R-UC017-04; tạm thời |
| R-17 | CancelTripController (AC-C-CancelTripController) | SmsGateway (AC-B-SmsGateway) | Association | - | - | UC-017 | Link CL06; bước 8, 9 | R-UC017-05; tạm thời |
| R-18 | CancelTripController (AC-C-CancelTripController) | PaymentGateway (AC-B-PaymentGateway) | Association | - | - | UC-017 | Link CL07; bước 11, 12 | R-UC017-06; tạm thời |
| R-19 | Ticket (AC-E-Ticket) | Trip (AC-E-Trip) | Association | A 0..* - B 1 | - | UC-017 | Bước 7 "các vé đang có hiệu lực của chuyến"; GL-23 (thành phần chuyến xe); luồng 7a (chuyến có thể không có vé) | R-UC017-07; giữ dù suy được qua R-21 và R-22 vì UC-017 truy vấn vé theo chuyến |
| R-20 | Ticket (AC-E-Ticket) | PaymentTransaction (AC-E-PaymentTransaction) | Association | A 0..* - B 0..1 | - | UC-017 | P04 UC-017 Dữ liệu ra 3 dòng 1; GL-06 (giao dịch Không thành công không có vé); ASM-32 (một giao dịch thu nhiều vé); BR-08 (vé mua tại quầy không có giao dịch) | R-UC017-08; liên kết vé với giao dịch mà P07 UC-009 chuyển cho P08 xét |
| R-21 | Seat (AC-E-Seat) | Trip (AC-E-Trip) | Association | A 1..* - B 1 | - | Mới ở P08 | GL-02 "Chỗ của một chuyến xe", GL-08 "các chỗ đã chọn của một chuyến xe"; REQ-03 (40 hoặc 29 chỗ mỗi chuyến theo loại xe); ASM-43 (chờ Q-59) | Mới ở P08 |
| R-22 | Ticket (AC-E-Ticket) | Seat (AC-E-Seat) | Association | A 0..* - B 1 | - | Mới ở P08 | GL-23 "quyền của một người đi được ngồi hoặc nằm tại một chỗ trên một chuyến xe", BR-04 (mỗi chỗ một mã vé); phía Ticket theo ASM-44 (vé đã huỷ vẫn được lưu, GL-24) | Mới ở P08; P07 UC-009 có chỗ trong issuedTickets và createTicket nhưng VOPC không có quan hệ này |

Multiplicity của các quan hệ tạm thời giữa boundary, control và entity để "-" vì chỉ thể hiện ai dùng ai. Số ở phía A là số đối tượng A ứng với một đối tượng B.

## F5. Analysis class diagram tổng thể

File diagrams/P08-class-analysis.drawio, ba trang. Trang Entity là trang tổng thể. Hệ thống hiện có 14 lớp, nên ba trang chia theo quy tắc mặc định: một trang Entity, mỗi nhóm chức năng của P02 có use case đã phân tích một trang (nhóm "Đặt vé trực tuyến" của UC-009, nhóm "Lịch chạy và chuyến" của UC-017).

| Trang | Số lớp | Số cạnh |
|---|---|---|
| Entity | 6 | 7 |
| Đặt vé trực tuyến | 10 | 15 |
| Lịch chạy và chuyến | 7 | 8 |

a) Bảng Node

| ID (mã AC) | ID mxCell | Loại (Class) | Nhãn | Stereotype | Thuộc về (view) | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AC-E-Booking | AC-E-Booking | Class | Booking | entity | Entity | trip<br>seatCodes<br>status<br>holdStartedAt<br>holdExpiry<br>travelerName<br>travelerPhone<br>seatFare | // createBooking<br>// checkSeatCountWithinLimit<br>// holdSeats<br>// recordTravelerInfo<br>// calculateTotalAmount<br>// releaseHeldSeats<br>// issueTickets | 40 | 40 | 280 | 350 |
| AC-E-Seat | AC-E-Seat | Class | Seat | entity | Entity | seatCode<br>tripState | // checkAvailable<br>// markHeld<br>// markSold<br>// markAvailable | 400 | 40 | 280 | 170 |
| AC-E-Trip | AC-E-Trip | Class | Trip | entity | Entity | departureTime<br>route<br>vehicleType<br>status<br>cancelReason<br>vehicle<br>driver | // checkDepartureNotReached<br>// listTripsInSchedule<br>// checkNotCancelled<br>// cancelTrip | 760 | 40 | 280 | 270 |
| AC-E-PaymentTransaction | AC-E-PaymentTransaction | Class | PaymentTransaction | entity | Entity | transactionCode<br>collectedAmount<br>refundedAmount | // recordRefund | 40 | 490 | 280 | 130 |
| AC-E-Ticket | AC-E-Ticket | Class | Ticket | entity | Entity | ticketCode<br>travelerName<br>travelerPhone<br>fare<br>purchaseChannel<br>status<br>smsStatus<br>paymentStatus<br>refundStatus<br>cancelNoticeStatus<br>refundAttemptStatus | // createTicket<br>// generateTicketCode<br>// recordSmsNotSent<br>// cancelTicketsOfTrip<br>// groupTicketCodesByTravelerPhone<br>// recordCancelNoticeNotSent<br>// selectOnlineTicketsToRefund<br>// calculateRefundAmount<br>// markRefunded<br>// recordRefundNotCompleted<br>// summarizeTripCancellation | 400 | 490 | 280 | 490 |
| AC-E-Fare | AC-E-Fare | Class | Fare | entity | Entity | route<br>vehicleType<br>amount<br>surchargePercent | // determineFare | 760 | 490 | 280 | 150 |
| AC-B-BookTicketOnlineForm | AC-B-BookTicketOnlineForm__V2 | Class | BookTicketOnlineForm | boundary | Đặt vé trực tuyến | selectedSeats<br>travelerName<br>travelerPhone<br>issuedTickets<br>totalAmount | // requestBookTicket<br>// selectSeats<br>// enterTravelerInfo<br>// cancelBooking<br>// notifyNoTripSelected<br>// notifySeatsUnavailable<br>// notifySeatLimitExceeded<br>// notifyTripDeparted<br>// notifyTravelerInfoMissing<br>// notifyPaymentFailed<br>// notifyHoldExpired<br>// notifyBookingCancelled<br>// showIssuedTickets | 840 | 40 | 280 | 410 |
| AC-B-SmsGateway | AC-B-SmsGateway__V2 | Class | SmsGateway | boundary | Đặt vé trực tuyến | recipientPhone<br>ticketCodes<br>noticeContent | // sendTicketCodesBySms<br>// sendTripCancellationBySms | 1280 | 40 | 280 | 150 |
| AC-C-SearchTripsController | AC-C-SearchTripsController__V2 | Class | SearchTripsController | control | Đặt vé trực tuyến | - | // searchTrips | 400 | 540 | 280 | 90 |
| AC-C-BookTicketOnlineController | AC-C-BookTicketOnlineController__V2 | Class | BookTicketOnlineController | control | Đặt vé trực tuyến | - | // startBookTicketOnline<br>// processSeatSelection<br>// processTravelerInfo<br>// requestCancelBooking<br>// startWaitingForPaymentResult<br>// stopWaitingForPaymentResult<br>// handleHoldExpiry | 840 | 540 | 280 | 210 |
| AC-C-PayTicketOnlineController | AC-C-PayTicketOnlineController__V2 | Class | PayTicketOnlineController | control | Đặt vé trực tuyến | - | // payTicketOnline<br>// cancelPayment | 1280 | 540 | 280 | 110 |
| AC-E-Fare | AC-E-Fare__V2 | Class | Fare | entity | Đặt vé trực tuyến | route<br>vehicleType<br>amount<br>surchargePercent | // determineFare | 40 | 870 | 280 | 150 |
| AC-E-Trip | AC-E-Trip__V2 | Class | Trip | entity | Đặt vé trực tuyến | departureTime<br>route<br>vehicleType<br>status<br>cancelReason<br>vehicle<br>driver | // checkDepartureNotReached<br>// listTripsInSchedule<br>// checkNotCancelled<br>// cancelTrip | 400 | 870 | 280 | 270 |
| AC-E-Seat | AC-E-Seat__V2 | Class | Seat | entity | Đặt vé trực tuyến | seatCode<br>tripState | // checkAvailable<br>// markHeld<br>// markSold<br>// markAvailable | 760 | 870 | 280 | 170 |
| AC-E-Booking | AC-E-Booking__V2 | Class | Booking | entity | Đặt vé trực tuyến | trip<br>seatCodes<br>status<br>holdStartedAt<br>holdExpiry<br>travelerName<br>travelerPhone<br>seatFare | // createBooking<br>// checkSeatCountWithinLimit<br>// holdSeats<br>// recordTravelerInfo<br>// calculateTotalAmount<br>// releaseHeldSeats<br>// issueTickets | 1120 | 870 | 280 | 350 |
| AC-E-Ticket | AC-E-Ticket__V2 | Class | Ticket | entity | Đặt vé trực tuyến | ticketCode<br>travelerName<br>travelerPhone<br>fare<br>purchaseChannel<br>status<br>smsStatus<br>paymentStatus<br>refundStatus<br>cancelNoticeStatus<br>refundAttemptStatus | // createTicket<br>// generateTicketCode<br>// recordSmsNotSent<br>// cancelTicketsOfTrip<br>// groupTicketCodesByTravelerPhone<br>// recordCancelNoticeNotSent<br>// selectOnlineTicketsToRefund<br>// calculateRefundAmount<br>// markRefunded<br>// recordRefundNotCompleted<br>// summarizeTripCancellation | 1480 | 870 | 280 | 490 |
| AC-B-CancelTripForm | AC-B-CancelTripForm__V3 | Class | CancelTripForm | boundary | Lịch chạy và chuyến | scheduledTrips<br>selectedTrip<br>cancelReason<br>cancellationResult | // requestCancelTrip<br>// showScheduledTrips<br>// selectTripAndReason<br>// notifyTripAlreadyCancelled<br>// notifyTripDeparted<br>// abortCancelTrip<br>// notifyCancelTripAborted<br>// showCancellationResult | 40 | 40 | 280 | 290 |
| AC-B-SmsGateway | AC-B-SmsGateway__V3 | Class | SmsGateway | boundary | Lịch chạy và chuyến | recipientPhone<br>ticketCodes<br>noticeContent | // sendTicketCodesBySms<br>// sendTripCancellationBySms | 400 | 40 | 280 | 150 |
| AC-B-PaymentGateway | AC-B-PaymentGateway__V3 | Class | PaymentGateway | boundary | Lịch chạy và chuyến | transactionCode<br>ticketCode<br>refundAmount<br>refundResult | // requestTicketRefund | 760 | 40 | 280 | 150 |
| AC-C-CancelTripController | AC-C-CancelTripController__V3 | Class | CancelTripController | control | Lịch chạy và chuyến | - | // startCancelTrip<br>// processTripCancellation<br>// requestAbortCancelTrip<br>// cancelOverdueReservationMark<br>// cancelPassengerListMark | 400 | 420 | 280 | 170 |
| AC-E-Trip | AC-E-Trip__V3 | Class | Trip | entity | Lịch chạy và chuyến | departureTime<br>route<br>vehicleType<br>status<br>cancelReason<br>vehicle<br>driver | // checkDepartureNotReached<br>// listTripsInSchedule<br>// checkNotCancelled<br>// cancelTrip | 40 | 680 | 280 | 270 |
| AC-E-Ticket | AC-E-Ticket__V3 | Class | Ticket | entity | Lịch chạy và chuyến | ticketCode<br>travelerName<br>travelerPhone<br>fare<br>purchaseChannel<br>status<br>smsStatus<br>paymentStatus<br>refundStatus<br>cancelNoticeStatus<br>refundAttemptStatus | // createTicket<br>// generateTicketCode<br>// recordSmsNotSent<br>// cancelTicketsOfTrip<br>// groupTicketCodesByTravelerPhone<br>// recordCancelNoticeNotSent<br>// selectOnlineTicketsToRefund<br>// calculateRefundAmount<br>// markRefunded<br>// recordRefundNotCompleted<br>// summarizeTripCancellation | 400 | 680 | 280 | 490 |
| AC-E-PaymentTransaction | AC-E-PaymentTransaction__V3 | Class | PaymentTransaction | entity | Lịch chạy và chuyến | transactionCode<br>collectedAmount<br>refundedAmount | // recordRefund | 760 | 680 | 280 | 130 |

b) Bảng Edge

| ID | ID mxCell | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Thuộc về (view) | Điểm uốn |
|---|---|---|---|---|---|---|---|
| R-10 | R-10 | AC-E-Booking | AC-E-Seat | Association | đầu nguồn 0..*; đầu đích 1..5 | Entity | - |
| R-11 | R-11 | AC-E-Booking | AC-E-Ticket | Association | đầu nguồn 0..1; đầu đích 0..5 | Entity | (70,420); (430,420) |
| R-12 | R-12 | AC-E-Booking | AC-E-Trip | Association | đầu nguồn 0..*; đầu đích 1 | Entity | (290,430); (790,430) |
| R-19 | R-19 | AC-E-Ticket | AC-E-Trip | Association | đầu nguồn 0..*; đầu đích 1 | Entity | (650,440); (1010,440) |
| R-20 | R-20 | AC-E-Ticket | AC-E-PaymentTransaction | Association | đầu nguồn 0..*; đầu đích 0..1 | Entity | - |
| R-21 | R-21 | AC-E-Seat | AC-E-Trip | Association | đầu nguồn 1..*; đầu đích 1 | Entity | - |
| R-22 | R-22 | AC-E-Ticket | AC-E-Seat | Association | đầu nguồn 0..*; đầu đích 1 | Entity | - |
| R-01 | R-01__V2 | AC-B-BookTicketOnlineForm__V2 | AC-C-BookTicketOnlineController__V2 | Association | - | Đặt vé trực tuyến | (980,480); (870,480) |
| R-02 | R-02__V2 | AC-C-BookTicketOnlineController__V2 | AC-C-SearchTripsController__V2 | Dependency | «include» | Đặt vé trực tuyến | - |
| R-03 | R-03__V2 | AC-C-BookTicketOnlineController__V2 | AC-C-PayTicketOnlineController__V2 | Dependency | «include» | Đặt vé trực tuyến | - |
| R-04 | R-04__V2 | AC-C-BookTicketOnlineController__V2 | AC-E-Trip__V2 | Association | - | Đặt vé trực tuyến | (930,780); (540,780) |
| R-05 | R-05__V2 | AC-C-BookTicketOnlineController__V2 | AC-E-Seat__V2 | Association | - | Đặt vé trực tuyến | (980,790); (900,790) |
| R-06 | R-06__V2 | AC-C-BookTicketOnlineController__V2 | AC-E-Fare__V2 | Association | - | Đặt vé trực tuyến | (880,800); (180,800) |
| R-07 | R-07__V2 | AC-C-BookTicketOnlineController__V2 | AC-E-Booking__V2 | Association | - | Đặt vé trực tuyến | (1030,810); (1260,810) |
| R-08 | R-08__V2 | AC-C-BookTicketOnlineController__V2 | AC-E-Ticket__V2 | Association | - | Đặt vé trực tuyến | (1080,820); (1620,820) |
| R-09 | R-09__V2 | AC-C-BookTicketOnlineController__V2 | AC-B-SmsGateway__V2 | Association | - | Đặt vé trực tuyến | (1090,490); (1420,490) |
| R-10 | R-10__V2 | AC-E-Booking__V2 | AC-E-Seat__V2 | Association | đầu nguồn 0..*; đầu đích 1..5 | Đặt vé trực tuyến | - |
| R-11 | R-11__V2 | AC-E-Booking__V2 | AC-E-Ticket__V2 | Association | đầu nguồn 0..1; đầu đích 0..5 | Đặt vé trực tuyến | - |
| R-12 | R-12__V2 | AC-E-Booking__V2 | AC-E-Trip__V2 | Association | đầu nguồn 0..*; đầu đích 1 | Đặt vé trực tuyến | (1260,1390); (430,1390) |
| R-21 | R-21__V2 | AC-E-Seat__V2 | AC-E-Trip__V2 | Association | đầu nguồn 1..*; đầu đích 1 | Đặt vé trực tuyến | - |
| R-22 | R-22__V2 | AC-E-Ticket__V2 | AC-E-Seat__V2 | Association | đầu nguồn 0..*; đầu đích 1 | Đặt vé trực tuyến | (1730,1400); (900,1400) |
| R-19 | R-19__V2 | AC-E-Ticket__V2 | AC-E-Trip__V2 | Association | đầu nguồn 0..*; đầu đích 1 | Đặt vé trực tuyến | (1510,1410); (650,1410) |
| R-13 | R-13__V3 | AC-B-CancelTripForm__V3 | AC-C-CancelTripController__V3 | Association | - | Lịch chạy và chuyến | (180,360); (430,360) |
| R-14 | R-14__V3 | AC-C-CancelTripController__V3 | AC-E-Trip__V3 | Association | - | Lịch chạy và chuyến | (430,620); (180,620) |
| R-15 | R-15__V3 | AC-C-CancelTripController__V3 | AC-E-Ticket__V3 | Association | - | Lịch chạy và chuyến | - |
| R-16 | R-16__V3 | AC-C-CancelTripController__V3 | AC-E-PaymentTransaction__V3 | Association | - | Lịch chạy và chuyến | (650,630); (900,630) |
| R-17 | R-17__V3 | AC-C-CancelTripController__V3 | AC-B-SmsGateway__V3 | Association | - | Lịch chạy và chuyến | - |
| R-18 | R-18__V3 | AC-C-CancelTripController__V3 | AC-B-PaymentGateway__V3 | Association | - | Lịch chạy và chuyến | (650,370); (900,370) |
| R-19 | R-19__V3 | AC-E-Ticket__V3 | AC-E-Trip__V3 | Association | đầu nguồn 0..*; đầu đích 1 | Lịch chạy và chuyến | - |
| R-20 | R-20__V3 | AC-E-Ticket__V3 | AC-E-PaymentTransaction__V3 | Association | đầu nguồn 0..*; đầu đích 0..1 | Lịch chạy và chuyến | - |

## F6. Rà soát lớp phân tích

| AC | Tên phản ánh đúng vai trò | Một khái niệm duy nhất | Trách nhiệm gắn kết | Cung cấp đủ hành vi cần | Yêu cầu đặc thù (BR, NFR) đã gắn | Ghi chú |
|---|---|---|---|---|---|---|
| AC-B-BookTicketOnlineForm | Đạt | Đạt: giao diện đặt vé của hành khách | Đạt: 13 trách nhiệm đều nhận hoặc hiển thị | Đạt | Đạt: BR-01, BR-02, BR-03, BR-05 qua các thông báo | - |
| AC-B-CancelTripForm | Đạt | Đạt: giao diện huỷ chuyến của nhân viên điều hành | Đạt: 8 trách nhiệm nhận hoặc hiển thị | Đạt | Đạt: BR-09, BR-10 qua thông báo | NFR-03 dựa vào tiền điều kiện của UC-017, không gắn lớp |
| AC-B-SmsGateway | Đạt | Đạt: cổng SMS | Đạt: hai trách nhiệm cùng là gửi SMS | Đạt | Đạt: NFR-12, BR-11 | Hai trách nhiệm xem F2a |
| AC-B-PaymentGateway | Đạt | Đạt: cổng thanh toán | Đạt | Đạt cho UC-017; trách nhiệm thu tiền thêm khi có P07 của UC-010 | Đạt: NFR-11 | NFR-10 gắn khi có P07 của UC-010 |
| AC-C-BookTicketOnlineController | Đạt | Đạt | Đạt: 7 trách nhiệm điều phối | Đạt | Đạt: BR-03, BR-06, NFR-02 | - |
| AC-C-SearchTripsController | Đạt | Đạt | Đạt | - | - | Tạm, chờ P07 của UC-008 |
| AC-C-PayTicketOnlineController | Đạt | Đạt | Đạt | - | - | Tạm, chờ P07 của UC-010 |
| AC-C-CancelTripController | Đạt | Đạt | Đạt: 5 trách nhiệm điều phối | Đạt | Đạt: BR-07, BR-08, BR-09, BR-10, BR-11, NFR-05, NFR-06 | NFR-03 dựa vào tiền điều kiện của UC-017 |
| AC-E-Trip | Đạt | Đạt | Đạt: 4 trách nhiệm về lịch và trạng thái chuyến | Đạt cho UC-009, UC-017; UC-016 bổ sung khi có P07 | Đạt: BR-05, BR-09, BR-10 | Chưa dùng checkNotCancelled ở UC-009, xem Q-61 |
| AC-E-Seat | Đạt | Đạt theo ASM-43 (chờ Q-59); GL-01 định nghĩa Chỗ là vị trí trên sơ đồ chỗ | Đạt: 4 trách nhiệm về trạng thái chỗ | Đạt cho UC-009; UC-021 bổ sung khi có P07 | Đạt: BR-02, NFR-04 | Xem Đề xuất sửa artifact trước (P05) |
| AC-E-Fare | Đạt | Đạt: giá vé theo GL-05 | Đạt | Đạt cho UC-009; UC-023, UC-024 bổ sung khi có P07 | Đạt: REQ-60, REQ-61 | Không có quan hệ với entity nào, xem Vấn đề còn mở |
| AC-E-Booking | Đạt | Đạt: lần đặt vé (GL-12) | Đạt: 7 trách nhiệm quanh vòng đời lần đặt | Đạt | Đạt: BR-01, BR-03, BR-04 | - |
| AC-E-Ticket | Đạt | Đạt: vé (GL-23) | Không đạt: 11 trách nhiệm, trong đó 4 trách nhiệm tác động lên tập vé của chuyến (cancelTicketsOfTrip, groupTicketCodesByTravelerPhone, selectOnlineTicketsToRefund, summarizeTripCancellation) trộn với trách nhiệm của một vé | Đạt | Đạt: BR-04, BR-07, BR-08, BR-11, NFR-05, NFR-06 | Hành động ở Vấn đề còn mở |
| AC-E-PaymentTransaction | Đạt | Đạt: giao dịch thanh toán (GL-06) | Đạt | Đạt cho UC-017; UC-010 bổ sung khi có P07 | Đạt: NFR-06, ASM-32 | - |

## F7. Mục kiểm soát

Các mục Câu hỏi mở, Giả định, Đề xuất sửa artifact trước và Vấn đề còn mở theo C5 nằm ngay dưới đây.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-59 | AC-E-Seat đại diện cho chỗ cụ thể của một chuyến xe (có trạng thái bán trên chuyến) hay cho vị trí trên sơ đồ chỗ của loại xe? (Một lớp "chỗ của chuyến xe", vị trí chỉ là thuộc tính seatCode / Hai lớp: vị trí trên sơ đồ chỗ của loại xe và chỗ của chuyến xe) | AC-E-Seat, R-10, R-21, R-22, F3, P05 GL-01 | P05 GL-01 "Vị trí ngồi hoặc nằm có mã riêng trên sơ đồ chỗ của một loại xe" so với GL-02 "Chỗ của một chuyến xe chưa có vé"; P07 UC-009 Vấn đề còn mở dòng 3 (tripState) |
| Q-60 | Lần đặt vé và vé đã trả chỗ, đã huỷ, đã trả có còn được lưu và còn gắn với chỗ của chuyến xe không, và một vé có thuộc nhiều nhất một lần đặt vé không? (Có, các bản ghi cũ vẫn được lưu và gắn với chỗ / Không, chỉ lần đặt và vé đang có hiệu lực gắn với chỗ) | R-10, R-11, R-22 (multiplicity) | BR-02 "Không được có hai vé cùng một chỗ trên một chuyến" không nêu vé đã huỷ; P05 GL-24 "Vé đã huỷ" vẫn là vé; P07 UC-009 Booking có trạng thái "Đã trả chỗ" |
| Q-61 | UC-009 xử lý thế nào khi chuyến đã bị huỷ ở UC-017: hành khách chọn một chuyến đã huỷ ở bước 4, và lần đặt vé đang giữ chỗ của chuyến vừa bị huỷ? (UC-008 chỉ cung cấp chuyến chưa huỷ nên UC-009 không kiểm tra thêm / UC-009 bước 4 kiểm tra thêm chuyến chưa huỷ và UC-017 trả các chỗ đang giữ của chuyến bị huỷ / Khác) | AC-E-Trip (checkNotCancelled), AC-E-Booking, AC-E-Seat, UC-009 bước 4, UC-017 bước 7 | P07 UC-009 F3.4: Trip chỉ có checkDepartureNotReached; P07 UC-017 Vấn đề còn mở: "UC-017 không đổi Seat và Booking của UC-009 ... chuyến đã huỷ không còn được bán"; BR-09 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-43 | AC-E-Seat là chỗ cụ thể của một chuyến xe, định danh bằng chuyến và mã chỗ, mang trạng thái bán trên chuyến đó; vị trí trên sơ đồ chỗ chỉ là thuộc tính seatCode, chưa tách thành lớp riêng. Mỗi chỗ thuộc đúng một chuyến xe (R-21). | Chờ Q-59. P05 chỉ có Chỗ (GL-01) là vị trí trên sơ đồ chỗ, còn P07 gắn trạng thái theo chuyến vào Seat; chọn một lớp để không thêm khái niệm ngoài P05, và vì sơ đồ chỗ thuộc UC-021 chưa phân tích | AC-E-Seat, R-10, R-21, R-22 |
| ASM-44 | Lần đặt vé và vé vẫn được lưu sau khi trả chỗ, huỷ hoặc hết hạn, nên một chỗ của chuyến xe gắn với 0..* lần đặt vé và 0..* vé theo thời gian; tại một thời điểm chỉ một lần đặt và một vé đang có hiệu lực cho chỗ (BR-02, GL-08). Một vé thuộc nhiều nhất một lần đặt vé. | Chờ Q-60. P07 UC-009 đặt trạng thái "Đã trả chỗ" cho Booking, P05 GL-24 giữ "Vé đã huỷ" là vé, BR-02 chỉ cấm hai vé cùng chỗ trên một chuyến; GL-12 gom các vé vào một lần đặt | R-10, R-11, R-22 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P05 | GL-01, GL-02, GL-08 | Chỗ (GL-01) là vị trí trên sơ đồ chỗ của loại xe, còn Chỗ trống (GL-02) và Giữ chỗ (GL-08) nói về chỗ của một chuyến xe; chưa có thuật ngữ cho chỗ của chuyến xe, nên AC-E-Seat phải chọn một nghĩa theo ASM-43 | Thêm thuật ngữ "Chỗ của chuyến xe" (trạng thái Trống, Đang giữ, Đã bán) và nêu quan hệ với Chỗ (GL-01), Sơ đồ chỗ (GL-19), theo câu trả lời Q-59 |
| P07 | UC-009 (F8 b; AC-E-Ticket) | VOPC không có quan hệ Ticket-Trip và Ticket-Seat dù createTicket "gắn chuyến, chỗ" và issuedTickets có chuyến, chỗ; R-UC009-10 và R-UC009-11 để multiplicity "?" ở phía A | Thêm hai quan hệ Ticket-Trip, Ticket-Seat vào VOPC; điền phía A của R-UC009-10 (0..*) và R-UC009-11 (0..1) theo ASM-44 (chờ Q-60) |
| P04 | UC-009 (bước 4, tiền điều kiện) | Không nêu cách xử lý chuyến đã bị huỷ ở UC-017 (Q-61); Trip có checkNotCancelled nhưng UC-009 không dùng | Theo câu trả lời Q-61, thêm kiểm tra chuyến chưa huỷ vào bước 4 hoặc nêu rõ UC-008 chỉ cung cấp chuyến chưa huỷ |

## Vấn đề còn mở

- Độ phủ: 25 trong 27 use case của P02 chưa có P07 (xem F1). Đã đặt trước hai control tạm AC-C-SearchTripsController (chờ P07 của UC-008) và AC-C-PayTicketOnlineController (chờ P07 của UC-010). Khi thêm P07, chạy lại P08 với phiên bản tăng lên để chuyển trạng thái sang Hoạt động.
- Lớp do use case khác sở hữu, trách nhiệm hiện chỉ gồm những gì UC-009, UC-017 cần: AC-E-Trip (UC-016), AC-E-Seat (UC-021), AC-E-Fare (UC-023, UC-024), AC-B-PaymentGateway và AC-E-PaymentTransaction (UC-010), AC-B-SmsGateway (cũng được UC-003, UC-014 dùng).
- F6, AC-E-Ticket, Trách nhiệm gắn kết không đạt: bốn trách nhiệm tác động lên tập vé của chuyến lẫn với trách nhiệm của một vé. P08 giữ nguyên trong Ticket vì P05 và BR không có khái niệm tập vé của chuyến, và không thêm lớp khi thiếu bằng chứng; P12 quyết định giao cho lớp tập hợp vé của chuyến hay cho Trip.
- Trip có vehicleType (Loại xe) và vehicle (Xe). vehicleType suy được từ xe qua loại xe (GL-14). Xe và Tài xế chưa có lớp (P05 Mục 3 xếp là từ phổ thông; UC-021, UC-022 chưa phân tích). Xét sau P07 của UC-021, UC-022 và khi đó bỏ vehicleType nếu thừa.
- Trạng thái nằm ở ba lớp: Seat.tripState, Booking.status, Ticket.status. Một trạng thái có thể suy từ trạng thái kia (chỗ Đã bán khi có vé đang có hiệu lực). P12 chọn nguồn sự thật của từng trạng thái.
- Booking-Trip (R-12) và Ticket-Trip (R-19) suy được qua Seat-Trip (R-21). Giữ vì có trong VOPC của P07 (mọi quan hệ VOPC phải có mặt) và mang ý nghĩa riêng (lần đặt cùng một chuyến; UC-017 truy vấn vé theo chuyến). P12 xét bỏ khi lập thuộc tính.
- AC-E-Fare chưa có quan hệ nào với entity khác: giá vé liên hệ với chuyến qua giá trị route, vehicleType chứ không qua tham chiếu đối tượng, và P07 chưa cho bằng chứng khác. Xét lại khi có P07 của UC-023, UC-024 (Tuyến xe GL-22, Loại xe GL-14, Mức tăng giá GL-16 có thể thành lớp).
- Chưa có quan hệ Booking-PaymentTransaction: UC-009 chỉ nhận kết quả thanh toán từ UC-010. R-20 (Ticket 0..* - PaymentTransaction 0..1) có thể đổi khi P07 của UC-010, UC-012 và UC-014 (thanh toán phần chênh lệch có thể tạo giao dịch thứ hai cho một vé).
- Booking-Seat (R-10): GL-12 gọi lần đặt là "Nhóm các chỗ", gần nghĩa aggregation. P08 giữ Association vì đặc tả và BR không nêu quan hệ toàn thể - bộ phận hay vòng đời phụ thuộc.
- Theo C9, YEU_CAU_BO_SUNG giới hạn phạm vi vào UC-009, UC-017 nên mô hình hợp nhất mới phủ hai use case; không xung đột với A1 vì các use case còn lại đã được liệt kê ở F1.
- File diagrams/P08-class-analysis.drawio sinh bằng chương trình từ cùng dữ liệu với F3, F4, F5 và đã kiểm tra tự động (XML hợp lệ, toạ độ bội số của 10, khoảng cách giữa node tối thiểu 40, cạnh không cắt node, mỗi trang không quá 20 lớp và 25 cạnh). Chưa mở bằng draw.io để xem bằng mắt; nhãn multiplicity ở các cạnh ngắn có thể cần chỉnh vị trí.
