# P08 - Mô hình phân tích hợp nhất - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P08 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P01-actors.md 1.0; P02-usecases.md 1.1; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-002-book-ticket-online-analysis.md 1.0; P07-uc-analysis/UC-008-return-ticket-analysis.md 1.0; P07-uc-analysis/UC-013-cancel-trip-analysis.md 1.0; P07-uc-analysis/UC-015-check-boarding-ticket-analysis.md 1.0. Không tra P04-uc-specs/ vì bằng chứng đã có trong P07, P05, P06 |
| Phạm vi | UC-002, UC-008, UC-013, UC-015 (4 use case đã phân tích ở P07); các use case khác trong P02 chưa được phân tích |

Quy ước trích nguồn: "GL-nn" là thuật ngữ của P05, "BR-nn" là quy tắc của P06, "R-UCnnn-nn" là quan hệ trong VOPC của P07, "Mục n" của P07 theo khung F1 đến F10 của P07. Tham số bước: CACH_CHIA_VIEW = Không có (áp dụng quy tắc mặc định ở F5); YEU_CAU_BO_SUNG = "Phạm vi phân tích của lần chạy này là 4 use case UC-002, UC-008, UC-013, UC-015; các use case khác trong P02 chưa được phân tích." Chế độ giả định CO_NHAN, hậu tố tên lớp Mặc định.

Tóm tắt: 37 dòng lớp trong 4 file P07 được hợp nhất thành 24 lớp phân tích (8 boundary, 5 control trong đó 1 control tạm, 11 entity); 43 quan hệ trong VOPC được hợp thành 36 quan hệ, thêm 1 quan hệ mới ở P08, tổng 37 quan hệ R-01 đến R-37. Không có lớp bị gộp vào lớp khác và không có lớp đồng âm cần tách. Không có aggregation, composition, generalization vì chưa có bằng chứng.

## F1. Độ phủ use case

| UC | Tên | File P07 | Trạng thái |
|---|---|---|---|
| UC-001 | Tra cứu chuyến xe | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-002 | Đặt vé trực tuyến | P07-uc-analysis/UC-002-book-ticket-online-analysis.md | Đã phân tích |
| UC-003 | Thanh toán vé trực tuyến | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-004 | Nhận đặt chỗ qua điện thoại | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-005 | Bán vé tại quầy | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-006 | Huỷ đặt chỗ qua điện thoại quá hạn | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-007 | Đổi vé | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-008 | Trả vé | P07-uc-analysis/UC-008-return-ticket-analysis.md | Đã phân tích |
| UC-009 | Đăng ký tài khoản | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-010 | Đăng nhập | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-011 | Xem lịch sử vé | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-012 | Xếp chuyến vào lịch chạy tuần | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-013 | Huỷ chuyến | P07-uc-analysis/UC-013-cancel-trip-analysis.md | Đã phân tích |
| UC-014 | Chuẩn bị danh sách hành khách của chuyến | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-015 | Soát vé lên xe | P07-uc-analysis/UC-015-check-boarding-ticket-analysis.md | Đã phân tích |
| UC-016 | Đặt giá vé | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-017 | Đặt mức tăng giá lễ Tết | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |
| UC-018 | Xem báo cáo kinh doanh | - | Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG) |

4 use case đã phân tích, 14 use case chưa phân tích. UC-003 được UC-002 include và đã có lớp tạm AC-C-PayTicketOnlineController.

## F2. Nhật ký hợp nhất

Mỗi dòng là một lớp trong bảng lớp phân tích F3.4 của một file P07; 4 file P07 có 11 + 8 + 9 + 9 = 37 dòng, mỗi dòng xuất hiện đúng một lần ở cột "Lớp gốc". Các dòng cùng mã AC ở nhiều use case là cùng một lớp được tái dùng, hợp vào một dòng của F3.

| STT | Lớp gốc (AC, tên) | UC nguồn | Tình huống | Kết quả | Bằng chứng (GL, BR, bước UC) |
|---|---|---|---|---|---|
| 1 | AC-B-BookTicketForm, BookTicketForm | UC-002 | Giữ nguyên | Giữ | Mục 3.1 P07 UC-002: một boundary cho cặp (ACT-01, UC-002); không có boundary giao diện người dùng khác cùng tương tác |
| 2 | AC-B-SmsGateway, SmsGateway | UC-002 | Giữ nguyên | Giữ; hợp trách nhiệm sendTicketSms với sendTripCancelSms của UC-013 thành sendSms (xem F2b) | GL-30 "gửi vé hoặc báo huỷ chuyến" là một khái niệm SMS; bước 12 UC-002 |
| 3 | AC-C-BookTicketOnlineController, BookTicketOnlineController | UC-002 | Giữ nguyên | Giữ | Control của UC-002, không gộp control của use case khác |
| 4 | AC-C-PayTicketOnlineController, PayTicketOnlineController | UC-002 | Giữ nguyên | Giữ, trạng thái Tạm (chờ P07 của UC-003) | Mục 3.3 P07 UC-002; RL-27 (UC-002 include UC-003), bước 10 |
| 5 | AC-E-Trip, Trip | UC-002 | Giữ nguyên | Giữ; hợp trách nhiệm của UC-008, UC-013, UC-015 | GL-04 |
| 6 | AC-E-Route, Route | UC-002 | Giữ nguyên | Giữ; hợp với dòng của UC-013, UC-015 | GL-36 |
| 7 | AC-E-Seat, Seat | UC-002 | Giữ nguyên | Giữ; hợp trách nhiệm của UC-008, UC-015 | GL-02, GL-03 |
| 8 | AC-E-Booking, Booking | UC-002 | Giữ nguyên | Giữ (đã xét với AC-E-PhoneReservation, xem F2a) | GL-18 khác GL-07 |
| 9 | AC-E-Ticket, Ticket | UC-002 | Giữ nguyên | Giữ; hợp trách nhiệm, thuộc tính của UC-008, UC-013, UC-015 | GL-37 |
| 10 | AC-E-BaseFare, BaseFare | UC-002 | Giữ nguyên | Giữ | GL-09; BR-04 |
| 11 | AC-E-HolidaySurcharge, HolidaySurcharge | UC-002 | Giữ nguyên | Giữ | GL-25; BR-05 |
| 12 | AC-B-ReturnTicketForm, ReturnTicketForm | UC-008 | Giữ nguyên | Giữ (đã xét gộp với AC-B-CounterReturnTicketForm, không gộp, xem F2a) | Mục 3.1 P07 UC-008: một boundary cho cặp (ACT-01, UC-008) |
| 13 | AC-B-CounterReturnTicketForm, CounterReturnTicketForm | UC-008 | Giữ nguyên | Giữ | Mục 3.1 P07 UC-008: cặp (ACT-02, UC-008); ASM-18 (không có số điện thoại người đi) |
| 14 | AC-B-PaymentGateway, PaymentGateway | UC-008 | Giữ nguyên | Giữ; hợp trách nhiệm với dòng của UC-013 | ACT-06 bước 8, 9; BR-15 |
| 15 | AC-C-ReturnTicketController, ReturnTicketController | UC-008 | Giữ nguyên | Giữ | Một control cho UC-008, phục vụ cả ACT-01 và ACT-02 |
| 16 | AC-E-Trip, Trip | UC-008 | Giữ nguyên | Giữ (cùng mã AC-E-Trip của UC-002; hợp trách nhiệm) | GL-04, GL-10, GL-34 |
| 17 | AC-E-Seat, Seat | UC-008 | Giữ nguyên | Giữ (cùng mã AC-E-Seat của UC-002; hợp trách nhiệm release, xem F2b) | GL-02, GL-03; BR-03, ASM-20 |
| 18 | AC-E-Ticket, Ticket | UC-008 | Giữ nguyên | Giữ (cùng mã AC-E-Ticket của UC-002; hợp trách nhiệm, thêm thuộc tính purchaseChannel) | GL-13, GL-22, GL-37, GL-39 |
| 19 | AC-E-Refund, Refund | UC-008 | Giữ nguyên | Giữ; hợp với dòng của UC-013, refundResult có ba giá trị (ASM-54) | GL-16, GL-24 |
| 20 | AC-B-CancelTripForm, CancelTripForm | UC-013 | Giữ nguyên | Giữ | Mục 3.1 P07 UC-013: cặp (ACT-03, UC-013) |
| 21 | AC-B-PaymentGateway, PaymentGateway | UC-013 | Boundary hệ thống trùng | Giữ AC-B-PaymentGateway (cùng mã với dòng của UC-008), hợp trách nhiệm requestRefund, returnRefundResult | ACT-06 bước 7, 8 của UC-013 giống bước 8, 9 của UC-008; GL-16 |
| 22 | AC-B-SmsGateway, SmsGateway | UC-013 | Boundary hệ thống trùng | Giữ AC-B-SmsGateway (cùng mã với dòng của UC-002), hợp trách nhiệm thành sendSms | ACT-07 bước 10 của UC-013; GL-30 |
| 23 | AC-C-CancelTripController, CancelTripController | UC-013 | Giữ nguyên | Giữ | Control của UC-013 |
| 24 | AC-E-Trip, Trip | UC-013 | Giữ nguyên | Giữ (cùng mã AC-E-Trip; hợp trách nhiệm) | GL-04, GL-10, GL-19 |
| 25 | AC-E-Route, Route | UC-013 | Giữ nguyên | Giữ (cùng mã AC-E-Route) | GL-36 |
| 26 | AC-E-Ticket, Ticket | UC-013 | Giữ nguyên | Giữ (cùng mã AC-E-Ticket; hợp trách nhiệm determineRefundMethod) | GL-08, GL-13, GL-37, GL-38, GL-39 |
| 27 | AC-E-PhoneReservation, PhoneReservation | UC-013 | Giữ nguyên | Giữ (đã xét với AC-E-Booking, xem F2a) | GL-07 "Yêu cầu giữ chỗ trên một chuyến do nhân viên bán vé ghi nhận khi khách gọi điện" |
| 28 | AC-E-Refund, Refund | UC-013 | Giữ nguyên | Giữ (cùng mã AC-E-Refund; hợp trách nhiệm createRefund) | GL-16, GL-24; BR-17 |
| 29 | AC-B-CheckBoardingTicketForm, CheckBoardingTicketForm | UC-015 | Giữ nguyên | Giữ | Mục 3.1 P07 UC-015: cặp (ACT-05, UC-015) |
| 30 | AC-B-BarcodeScanner, BarcodeScanner | UC-015 | Giữ nguyên | Giữ (boundary giao diện thiết bị của ACT-09, không có boundary thiết bị khác) | ACT-09 bước 4; GL-22, GL-23, GL-40 |
| 31 | AC-C-CheckBoardingTicketController, CheckBoardingTicketController | UC-015 | Giữ nguyên | Giữ | Control của UC-015 |
| 32 | AC-E-TicketCheckSession, TicketCheckSession | UC-015 | Giữ nguyên | Giữ (đã xét với AC-E-TripPassengerList, xem F2a) | GL-28; ASM-51 |
| 33 | AC-E-Trip, Trip | UC-015 | Giữ nguyên | Giữ (cùng mã AC-E-Trip; hợp trách nhiệm findTrip với UC-013) | GL-04, GL-10 |
| 34 | AC-E-Route, Route | UC-015 | Giữ nguyên | Giữ (cùng mã AC-E-Route) | GL-36 |
| 35 | AC-E-TripPassengerList, TripPassengerList | UC-015 | Giữ nguyên | Giữ, không hạ thành thuộc tính (có thuật ngữ riêng và hành vi tìm vé, đếm vé) | GL-05; BR-20; ASM-50; chờ Q-73 |
| 36 | AC-E-Ticket, Ticket | UC-015 | Giữ nguyên | Giữ (cùng mã AC-E-Ticket; thêm thuộc tính checkedTime, trách nhiệm determineCheckResult, markChecked) | GL-14, GL-26, GL-37; BR-21, BR-22 |
| 37 | AC-E-Seat, Seat | UC-015 | Giữ nguyên | Giữ (cùng mã AC-E-Seat; hợp trách nhiệm getSeatCode với UC-008) | GL-02 |

### F2a. Các cặp đã xét và giữ tách

| STT | Cặp lớp | Phép thử | Kết luận |
|---|---|---|---|
| 1 | AC-E-Booking và AC-E-PhoneReservation | GL-18 là lần đặt trực tuyến giữ chỗ 10 phút để thanh toán qua cổng (BR-07); GL-07 là yêu cầu giữ chỗ do nhân viên ghi nhận khi khách gọi điện, chờ thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến (BR-24). Khác vòng đời, khác tác nhân, GL-07 liệt kê "Vé đặt qua điện thoại" là từ không dùng, không liệt kê Booking | Khác khái niệm, giữ hai lớp |
| 2 | AC-B-ReturnTicketForm và AC-B-CounterReturnTicketForm | Hai boundary giao diện người dùng của hai tác nhân khác nhau (ACT-01, ACT-02); thuộc tính nhập khác nhau (ticketCode và travelerPhone so với ticketCode, ASM-18); 11 trách nhiệm trùng tên. Glossary không coi là một | Không gộp theo quy tắc mặc định mỗi cặp tác nhân - use case một boundary |
| 3 | AC-E-TripPassengerList và AC-E-Ticket | GL-05 là tập dữ liệu các vé của một chuyến, GL-37 là chứng từ của một chỗ. Một danh sách chứa nhiều vé | Khác khái niệm, giữ hai lớp |
| 4 | AC-E-TripPassengerList và AC-E-TicketCheckSession | GL-05 là dữ liệu đầu vào của việc soát vé, GL-28 là khoảng làm việc của phụ xe với vòng đời và trạng thái gửi riêng (sendStatus) | Khác khái niệm, giữ hai lớp |
| 5 | AC-E-BaseFare và AC-E-HolidaySurcharge | GL-09 là mức giá theo cặp tuyến và loại xe, GL-25 là tỉ lệ phần trăm theo khoảng ngày; thuộc tính định danh khác nhau (busType; startDate, endDate) | Khác khái niệm, giữ hai lớp |
| 6 | AC-E-Trip và AC-E-Route | GL-04 là một lần chạy tại một giờ xuất bến, GL-36 là đường chạy cố định; một tuyến có nhiều chuyến | Khác khái niệm, giữ hai lớp |
| 7 | AC-B-BarcodeScanner và AC-B-CheckBoardingTicketForm | Hai boundary của hai tác nhân khác loại (ACT-09 thiết bị, ACT-05 người); khác loại boundary | Không gộp |
| 8 | Bốn control AC-C-BookTicketOnlineController, AC-C-ReturnTicketController, AC-C-CancelTripController, AC-C-CheckBoardingTicketController | Mỗi control điều phối một use case khác nhau; P02 không có hai use case nào là một | Không gộp control của các use case khác nhau |
| 9 | Đồng âm: các thuộc tính status của Trip, Seat, Booking, Ticket, PhoneReservation; checkNotCancelled của Trip và Ticket; cancelWithTrip của Ticket và PhoneReservation; findTicket của Ticket và TripPassengerList; getSeatMap của Trip và BookTicketOnlineController | Cùng tên nhưng nằm ở các lớp khác nhau, mỗi tên chỉ có nghĩa trong lớp của nó | Không phải đồng âm ở mức lớp; không đổi tên |
| 10 | Thuộc tính trá hình: Booking.travelerInfos, Trip.availableSeatCount, Trip.busType | travelerInfos đã là thuộc tính của Booking (ASM-43); availableSeatCount là số chỗ còn trống của chuyến; busType là giá trị của Loại xe (GL-21), P07 UC-002 đã xếp thành thuộc tính của Trip vì không có hành vi riêng; Xe (GL-41) không tham gia hành vi của 4 use case | Giữ ở dạng thuộc tính, không có lớp trá hình cần hạ trong 24 lớp |

### F2b. Nhật ký hợp nhất trách nhiệm và thuộc tính

| STT | Lớp | Mục gốc | UC nguồn | Tình huống | Kết quả | Bằng chứng |
|---|---|---|---|---|---|---|
| 1 | AC-B-SmsGateway | sendTicketSms (UC-002); sendTripCancelSms (UC-013) | UC-002, UC-013 | Cùng ý nghĩa, khác tên | Giữ một tên sendSms; tên bị thay: sendTicketSms, sendTripCancelSms | GL-30: SMS là một khái niệm dùng cho vé và báo huỷ chuyến; chỉ khác nội dung, nội dung do Ticket lập |
| 2 | AC-E-Seat | release (UC-002); release (UC-008) | UC-002, UC-008 | Cùng tên, cùng kết quả | Giữ một trách nhiệm release, mô tả gộp hai nguyên nhân (hết thời hạn giữ chỗ, vé của chỗ được trả) | GL-03 chỗ trả về trạng thái còn trống; BR-08, BR-03, ASM-20 |
| 3 | AC-E-Trip | getRouteAndDepartureTime (UC-002, UC-008, UC-013, UC-015) | 4 UC | Cùng tên, cùng ý nghĩa | Giữ một trách nhiệm | GL-04, GL-10 |
| 4 | AC-E-Route | checkRouteMatches (UC-002, UC-013, UC-015) | UC-002, UC-013, UC-015 | Cùng tên, cùng ý nghĩa | Giữ một trách nhiệm | GL-36 |
| 5 | AC-E-Trip | findTrip (UC-013, UC-015) | UC-013, UC-015 | Cùng tên, cùng ý nghĩa | Giữ một trách nhiệm; UC-013 kèm ngày xuất bến, UC-015 chỉ tuyến và giờ xuất bến, GL-10 giờ xuất bến gồm ngày | GL-10 |
| 6 | AC-E-Trip | findMatchingTrips (UC-002) và findTrip (UC-013, UC-015) | UC-002, UC-013, UC-015 | Khác ý nghĩa, khác tên | Giữ hai trách nhiệm: findMatchingTrips trả các chuyến khớp tiêu chí của hành khách, findTrip xác định một chuyến nhân viên đã chỉ định | Bước 2 của UC-002, UC-013, UC-015 |
| 7 | AC-E-Ticket | determineRefundMethod (UC-008, UC-013) | UC-008, UC-013 | Cùng tên, cùng ý nghĩa | Giữ một trách nhiệm | BR-15, BR-16 |
| 8 | AC-E-Refund | createRefund (UC-008, UC-013) | UC-008, UC-013 | Cùng tên, cùng ý nghĩa | Giữ một trách nhiệm | GL-16 |
| 9 | AC-E-Seat | getSeatCode (UC-008, UC-015) | UC-008, UC-015 | Cùng tên, cùng ý nghĩa | Giữ một trách nhiệm | GL-02 |
| 10 | AC-B-PaymentGateway | requestRefund, returnRefundResult (UC-008, UC-013) | UC-008, UC-013 | Cùng tên, cùng ý nghĩa | Giữ hai trách nhiệm, hợp thuộc tính ticketCode, refundAmount | BR-15; GL-16 |
| 11 | AC-E-Ticket | cancelTicket (UC-008) và cancelWithTrip (UC-013) | UC-008, UC-013 | Cùng ý nghĩa một phần, khác tên và khác tác dụng đi kèm | Giữ hai trách nhiệm: cancelTicket kèm trả chỗ và tạo khoản hoàn trong cùng thao tác; cancelWithTrip chỉ đổi trạng thái, không đụng chỗ (ASM-26, Q-44) và ghi khoản hoàn riêng bằng recordRefund | GL-39 "do đã được trả, thuộc chuyến bị huỷ"; P07 UC-008 bước 10, P07 UC-013 bước 5, 9 |
| 12 | AC-E-Ticket | calculateRefundAmount (UC-008) và calculateTripCancelRefundAmount (UC-013) | UC-008, UC-013 | Khác quy tắc tính | Giữ hai trách nhiệm (BR-13, BR-14 theo thời gian còn lại so với BR-17 luôn 100%) | BR-13, BR-14, BR-17 |
| 13 | AC-E-Ticket | getTicketSmsContent (UC-002) và getTripCancelSmsContent (UC-013) | UC-002, UC-013 | Khác nội dung | Giữ hai trách nhiệm | GL-30; ASM-29 |
| 14 | AC-E-Ticket, AC-E-Trip | checkNotCancelled (UC-008 của Ticket; UC-013 của Trip) | UC-008, UC-013 | Cùng tên, khác lớp | Giữ ở mỗi lớp, không phải đồng âm trong một lớp | GL-38, GL-39 so với trạng thái huỷ của chuyến (ASM-26) |
| 15 | AC-E-Ticket, AC-E-PhoneReservation | cancelWithTrip | UC-013 | Cùng tên, khác lớp | Giữ ở mỗi lớp | ASM-26, ASM-27 |
| 16 | AC-C-CheckBoardingTicketController | checkTicket (gọi từ BarcodeScanner và CheckBoardingTicketForm) | UC-015 | Một trách nhiệm, hai nơi gọi | Giữ một trách nhiệm | Message 2.1 và 2a.1 của P07 UC-015 |
| 17 | AC-E-Refund | refundResult (UC-008: hai giá trị suy ra từ ASM-46; UC-013: ba giá trị, ASM-48) | UC-008, UC-013 | Thuộc tính mâu thuẫn | Hợp ba giá trị đã hoàn, chưa thành công, chờ chi tiền mặt; thời điểm tạo khoản hoàn theo ASM-54 | ASM-46, ASM-48, ASM-54; GL-16 |
| 18 | AC-E-Seat | status (UC-002: ba giá trị còn trống, đang giữ, đã có vé; GL-02: hai giá trị còn trống, không còn trống; BR-03 là suy luận) | UC-002, UC-008, UC-015 | Thuộc tính mâu thuẫn | Giữ thuộc tính status với ba giá trị theo ASM-42; câu hỏi Q-75 | GL-02, GL-03, BR-03, ASM-42, Q-75 |
| 19 | AC-E-Ticket | status, purchaseChannel, checkedTime (UC-002, UC-008, UC-013, UC-015) | 4 UC | Hợp thuộc tính, không mâu thuẫn | Hợp thành bảy thuộc tính ticketCode, travelerName, travelerPhone, price, status, purchaseChannel, checkedTime; status chỉ ghi vé đã phát hành hay đã huỷ (P07 UC-015) | GL-13, GL-14, GL-37 |
| 20 | AC-E-Trip | status (UC-013), departureTime, busType, availableSeatCount (UC-002) | UC-002, UC-013 | Hợp thuộc tính, không mâu thuẫn | Hợp thành bốn thuộc tính | GL-04, GL-10 |

## F3. Bảng lớp hợp nhất

| AC | Stereotype | Tên | Trách nhiệm (gộp) | Thuộc tính | Dùng trong UC | Loại boundary | Trạng thái |
|---|---|---|---|---|---|---|---|
| AC-B-BookTicketForm | boundary | BookTicketForm | // requestBooking: nhận yêu cầu đặt vé và tiêu chí tìm chuyến từ hành khách (UC-002)<br>// selectTrip: nhận chuyến hành khách chọn (UC-002)<br>// selectSeatsAndEnterTravelerInfo: nhận chỗ đã chọn và họ tên, số điện thoại người đi của từng chỗ (UC-002)<br>// showTrips: hiển thị các chuyến khớp kèm số chỗ còn trống và giá vé (UC-002)<br>// showSeatMap: hiển thị sơ đồ chỗ với trạng thái từng chỗ (UC-002)<br>// showNoTripFoundNotice: thông báo không có chuyến phù hợp (UC-002)<br>// showNoSeatLeftNotice: thông báo chuyến đã hết chỗ trống (UC-002)<br>// showSeatLimitExceededNotice: thông báo số chỗ vượt giới hạn một lần đặt (UC-002)<br>// showSeatsUnavailableNotice: thông báo các chỗ không còn trống (UC-002)<br>// showMissingTravelerInfoNotice: nhắc cung cấp đủ họ tên, số điện thoại người đi (UC-002)<br>// showInvalidPhoneNotice: thông báo số điện thoại không đúng định dạng (UC-002)<br>// showHoldExpiredNotice: thông báo hết thời hạn giữ chỗ, lần đặt không thành công (UC-002)<br>// showPaymentFailedNotice: thông báo thanh toán không thành công (UC-002)<br>// showIssuedTickets: hiển thị các vé đã phát hành và tổng tiền (UC-002) | departurePoint<br>arrivalPoint<br>travelDate<br>selectedSeats<br>travelerNames<br>travelerPhones | UC-002 | Giao diện người dùng | Hoạt động |
| AC-B-ReturnTicketForm | boundary | ReturnTicketForm | // requestReturnTicket: nhận yêu cầu trả vé và thông tin nhận diện vé từ tác nhân (UC-008)<br>// confirmReturnTicket: nhận xác nhận trả vé của tác nhân (UC-008)<br>// declineReturnTicket: nhận việc tác nhân không xác nhận trả vé (UC-008)<br>// showReturnInfo: hiển thị thông tin vé, thời gian còn lại, mức hoàn và số tiền hoàn (UC-008)<br>// showTicketNotFoundNotice: thông báo không tìm thấy vé khớp thông tin đã cung cấp (UC-008)<br>// showTicketCancelledNotice: thông báo vé đã bị huỷ (UC-008)<br>// showWrongChannelNotice: thông báo vé mua qua kênh khác kênh yêu cầu trả (BR-11) (UC-008)<br>// showReturnTimeLimitNotice: thông báo còn dưới 4 giờ trước giờ xuất bến (BR-12) (UC-008)<br>// showReturnAbortedNotice: thông báo yêu cầu trả vé đã được huỷ, vé giữ nguyên (UC-008)<br>// showRefundFailedNotice: thông báo hoàn tiền không thành công, vé chưa được trả (UC-008)<br>// showReturnResult: hiển thị kết quả trả vé gồm trạng thái vé, số tiền hoàn, hình thức hoàn (UC-008) | ticketCode<br>travelerPhone | UC-008 | Giao diện người dùng | Hoạt động |
| AC-B-CounterReturnTicketForm | boundary | CounterReturnTicketForm | // requestReturnTicket: nhận yêu cầu trả vé và thông tin nhận diện vé từ tác nhân (UC-008)<br>// confirmReturnTicket: nhận xác nhận trả vé của tác nhân (UC-008)<br>// declineReturnTicket: nhận việc tác nhân không xác nhận trả vé (UC-008)<br>// showReturnInfo: hiển thị thông tin vé, thời gian còn lại, mức hoàn và số tiền hoàn (UC-008)<br>// showTicketNotFoundNotice: thông báo không tìm thấy vé khớp thông tin đã cung cấp (UC-008)<br>// showTicketCancelledNotice: thông báo vé đã bị huỷ (UC-008)<br>// showWrongChannelNotice: thông báo vé mua qua kênh khác kênh yêu cầu trả (BR-11) (UC-008)<br>// showReturnTimeLimitNotice: thông báo còn dưới 4 giờ trước giờ xuất bến (BR-12) (UC-008)<br>// showReturnAbortedNotice: thông báo yêu cầu trả vé đã được huỷ, vé giữ nguyên (UC-008)<br>// showRefundFailedNotice: thông báo hoàn tiền không thành công, vé chưa được trả (UC-008)<br>// showReturnResult: hiển thị kết quả trả vé gồm trạng thái vé, số tiền hoàn, hình thức hoàn (UC-008) | ticketCode | UC-008 | Giao diện người dùng | Hoạt động |
| AC-B-CancelTripForm | boundary | CancelTripForm | // requestCancelTrip: nhận yêu cầu huỷ chuyến và tuyến, ngày xuất bến, giờ xuất bến của chuyến từ tác nhân (UC-013)<br>// confirmCancelTrip: nhận xác nhận huỷ chuyến của tác nhân (UC-013)<br>// declineCancelTrip: nhận việc tác nhân không xác nhận huỷ chuyến (UC-013)<br>// showCancelTripInfo: hiển thị tuyến, giờ xuất bến, số vé theo kênh mua, số đặt chỗ chưa thanh toán và tổng số tiền hoàn (UC-013)<br>// showTripNotFoundNotice: thông báo không có chuyến khớp thông tin đã chỉ định (UC-013)<br>// showTripAlreadyCancelledNotice: thông báo chuyến đã bị huỷ (UC-013)<br>// showTripDepartedNotice: thông báo chuyến đã tới giờ xuất bến (UC-013)<br>// showCancelTripAbortedNotice: thông báo yêu cầu huỷ chuyến đã được bỏ, chuyến giữ nguyên (UC-013)<br>// showCancelTripResult: hiển thị kết quả huỷ chuyến (UC-013) | departurePoint<br>arrivalPoint<br>departureDate (Ngày)<br>departureTime (Giờ) | UC-013 | Giao diện người dùng | Hoạt động |
| AC-B-CheckBoardingTicketForm | boundary | CheckBoardingTicketForm | // requestStartCheck: nhận yêu cầu bắt đầu soát vé và tuyến, giờ xuất bến của chuyến cần soát từ phụ xe (UC-015)<br>// enterTicketCode: nhận mã vé phụ xe nhập khi vé không có mã vạch (UC-015)<br>// requestEndCheck: nhận yêu cầu kết thúc soát vé của chuyến (UC-015)<br>// showCheckSessionInfo: hiển thị tuyến, giờ xuất bến, số vé còn hiệu lực, số vé đã soát (UC-015)<br>// showValidTicketResult: hiển thị kết quả Hợp lệ kèm mã vé, chỗ, họ tên người đi (UC-015)<br>// showInvalidTicketResult: hiển thị kết quả Không hợp lệ kèm lý do, mã vé và, khi có, chỗ, thời điểm soát trước (UC-015)<br>// showCheckSummary: hiển thị tuyến, giờ xuất bến, số vé đã soát, số vé còn hiệu lực chưa soát, trạng thái gửi kết quả (UC-015) | departurePoint<br>arrivalPoint<br>departureTime (Giờ)<br>ticketCode | UC-015 | Giao diện người dùng | Hoạt động |
| AC-B-BarcodeScanner | boundary | BarcodeScanner | // readBarcode: nhận mã vạch do đầu quét đọc từ vé và chuyển mã vé cho control (UC-015) | ticketCode | UC-015 | Giao diện thiết bị | Hoạt động |
| AC-B-SmsGateway | boundary | SmsGateway | // sendSms: gửi nội dung tin nhắn (vé hoặc báo huỷ chuyến) tới số điện thoại người đi qua Cổng SMS (UC-002, UC-013) | recipientPhone<br>smsContent | UC-002, UC-013 | Giao diện hệ thống | Hoạt động |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestRefund: gửi yêu cầu hoàn số tiền hoàn của vé tới Cổng thanh toán (UC-008, UC-013)<br>// returnRefundResult: nhận kết quả hoàn tiền từ Cổng thanh toán (UC-008, UC-013) | ticketCode<br>refundAmount (Số tiền) | UC-008, UC-013 | Giao diện hệ thống | Hoạt động |
| AC-C-BookTicketOnlineController | control | BookTicketOnlineController | // searchTrips: điều phối tìm các chuyến khớp tiêu chí (UC-002)<br>// getSeatMap: điều phối lấy sơ đồ chỗ của chuyến đã chọn (UC-002)<br>// submitBooking: điều phối kiểm tra, tính tiền, giữ chỗ, thanh toán, phát hành và gửi vé (UC-002)<br>// startWaitingForPayment: bắt đầu chờ thanh toán trong thời hạn giữ chỗ (BR-07) (UC-002)<br>// handleSeatHoldExpired: xử lý sự kiện hết thời hạn giữ chỗ (UC-002) | - | UC-002 | - | Hoạt động |
| AC-C-PayTicketOnlineController | control | PayTicketOnlineController | // payTickets: nhận yêu cầu thanh toán tổng tiền của lần đặt từ UC-002 (UC-002) | - | UC-002 | - | Tạm (chờ P07 của UC-003) |
| AC-C-ReturnTicketController | control | ReturnTicketController | // startReturnTicket: điều phối nhận diện vé, kiểm tra điều kiện trả, tính số tiền hoàn và hiển thị cho tác nhân (UC-008)<br>// confirmReturn: điều phối xác định hình thức hoàn, hoàn tiền qua cổng thanh toán khi cần, huỷ vé và thông báo kết quả (UC-008)<br>// cancelReturnRequest: kết thúc yêu cầu trả vé khi tác nhân không xác nhận (UC-008) | - | UC-008 | - | Hoạt động |
| AC-C-CancelTripController | control | CancelTripController | // startCancelTrip: điều phối tìm chuyến, kiểm tra điều kiện huỷ và hiển thị thông tin huỷ chuyến (UC-013)<br>// confirmCancel: điều phối huỷ chuyến, hoàn tiền, gửi tin nhắn và thông báo kết quả (UC-013)<br>// cancelCancelTripRequest: kết thúc yêu cầu huỷ chuyến khi tác nhân không xác nhận (UC-013)<br>// cancelTripTriggers: huỷ các mốc kích hoạt tự động của UC-006 và UC-014 tính từ giờ xuất bến của chuyến đã huỷ (ASM-47) (UC-013) | - | UC-013 | - | Hoạt động |
| AC-C-CheckBoardingTicketController | control | CheckBoardingTicketController | // startCheck: điều phối tìm chuyến, mở phiên soát vé và hiển thị thông tin chuyến (UC-015)<br>// checkTicket: điều phối kiểm tra mã vé, ghi nhận vé đã soát và báo kết quả của một lần quét (gọi từ BarcodeScanner và CheckBoardingTicketForm) (UC-015)<br>// endCheck: điều phối gửi kết quả soát vé của phiên và hiển thị kết quả soát vé của chuyến (UC-015) | - | UC-015 | - | Hoạt động |
| AC-E-Trip | entity | Trip | // findMatchingTrips: tìm các chuyến có tuyến và ngày xuất bến khớp tiêu chí (UC-002)<br>// getSeatMap: cung cấp các chỗ của chuyến kèm trạng thái (UC-002)<br>// checkSeatsAvailable: kiểm tra mọi chỗ đã chọn của chuyến còn trống (UC-002)<br>// determineTicketPrice: xác định giá một vé của chuyến (UC-002)<br>// getRouteAndDepartureTime: cung cấp tuyến và giờ xuất bến của chuyến (UC-002, UC-008, UC-013, UC-015)<br>// calculateTimeToDeparture: tính thời gian còn lại từ thời điểm trả tới giờ xuất bến của chuyến (UC-008)<br>// findTrip: tìm chuyến trong lịch chạy khớp tuyến, giờ xuất bến (và ngày xuất bến khi có) đã chỉ định (UC-013, UC-015)<br>// checkNotCancelled: kiểm tra chuyến chưa ở trạng thái đã huỷ (ASM-26) (UC-013)<br>// checkBeforeDeparture: kiểm tra thời điểm hiện tại chưa tới giờ xuất bến (ASM-24) (UC-013)<br>// getCancellationSummary: tổng hợp tuyến, giờ xuất bến, số vé còn hiệu lực theo kênh mua, số đặt chỗ chưa thanh toán và tổng số tiền hoàn (BR-17) (UC-013)<br>// cancelTrip: chuyển chuyến sang đã huỷ và yêu cầu vé còn hiệu lực, đặt chỗ chưa thanh toán của chuyến cùng chuyển sang đã huỷ (ASM-26, ASM-27) (UC-013) | departureTime (Giờ)<br>busType<br>availableSeatCount (Số lượng)<br>status (Trạng thái) | UC-002, UC-008, UC-013, UC-015 | - | Hoạt động |
| AC-E-Route | entity | Route | // checkRouteMatches: kiểm tra điểm đi, điểm đến của tuyến khớp tiêu chí hoặc tuyến đã chỉ định (UC-002, UC-013, UC-015) | departurePoint<br>arrivalPoint | UC-002, UC-013, UC-015 | - | Hoạt động |
| AC-E-Seat | entity | Seat | // checkAvailable: xác định chỗ còn trống theo BR-03 (UC-002)<br>// hold: chuyển chỗ sang trạng thái đang giữ cho một lần đặt (UC-002)<br>// release: trả chỗ về trạng thái còn trống khi hết thời hạn giữ chỗ (BR-08) hoặc khi vé của chỗ được trả (BR-03, ASM-20) (UC-002, UC-008)<br>// getSeatCode: cung cấp mã chỗ của vé (UC-008, UC-015) | seatCode<br>status (Trạng thái) | UC-002, UC-008, UC-015 | - | Hoạt động |
| AC-E-Booking | entity | Booking | // createBooking: khởi tạo lần đặt từ các chỗ đã chọn và thông tin người đi (UC-002)<br>// checkMaxSeats: kiểm tra số chỗ của lần đặt không quá 5 (BR-01) (UC-002)<br>// validateTravelerInfo: kiểm tra họ tên và số điện thoại người đi của mọi chỗ (ASM-15) (UC-002)<br>// calculateTotal: tính tổng tiền bằng tổng giá vé các chỗ (BR-06) (UC-002)<br>// holdSeats: giữ các chỗ của lần đặt và ghi nhận thời điểm bắt đầu giữ (UC-002)<br>// releaseSeats: trả các chỗ đang giữ khi hết thời hạn (BR-08) (UC-002)<br>// issueTickets: phát hành vé cho các chỗ đang giữ (BR-09, BR-10) (UC-002)<br>// getBookingSummary: cung cấp các vé đã phát hành và tổng tiền (UC-002) | totalAmount (Số tiền)<br>holdStartTime (Giờ)<br>status (Trạng thái)<br>travelerInfos (danh sách họ tên và số điện thoại người đi theo từng chỗ (ASM-43)) | UC-002 | - | Hoạt động |
| AC-E-Ticket | entity | Ticket | // createTicket: khởi tạo vé với mã vé duy nhất cho một chỗ (BR-10) (UC-002)<br>// getTicketSmsContent: lập nội dung SMS gồm mã vé, tuyến, giờ xuất bến, chỗ, họ tên người đi (UC-002)<br>// findTicket: tìm vé khớp mã vé và, khi hành khách yêu cầu, khớp số điện thoại người đi (UC-008)<br>// checkNotCancelled: kiểm tra vé chưa ở trạng thái đã huỷ (ASM-20) (UC-008)<br>// checkPurchaseChannel: kiểm tra kênh mua của vé trùng kênh yêu cầu trả (BR-11) (UC-008)<br>// checkReturnTimeLimit: kiểm tra thời gian còn lại trước giờ xuất bến từ 4 giờ trở lên và cho biết thời gian còn lại (BR-12) (UC-008)<br>// calculateRefundAmount: xác định mức hoàn 90% hoặc 50% và tính số tiền hoàn theo giá vé khi vé được trả (BR-13, BR-14) (UC-008)<br>// getTicketReturnInfo: cung cấp mã vé, tuyến, giờ xuất bến, chỗ, giá vé để hiển thị (UC-008)<br>// determineRefundMethod: xác định hình thức hoàn theo kênh mua (BR-15, BR-16) (UC-008, UC-013)<br>// cancelTicket: chuyển vé sang đã huỷ do được trả, trả chỗ và tạo khoản hoàn tiền (UC-008)<br>// getCancelImpactInfo: cung cấp kênh mua và số tiền hoàn bằng 100% giá vé của vé còn hiệu lực (BR-17) (UC-013)<br>// cancelWithTrip: chuyển vé sang đã huỷ do chuyến bị huỷ (ASM-26) (UC-013)<br>// calculateTripCancelRefundAmount: tính số tiền hoàn bằng 100% giá vé đã thanh toán khi chuyến bị huỷ (BR-17, ASM-22) (UC-013)<br>// recordRefund: ghi nhận khoản hoàn của vé với số tiền hoàn, hình thức hoàn và kết quả hoàn (ASM-48) (UC-013)<br>// getTripCancelSmsContent: lập nội dung tin nhắn báo huỷ chuyến gồm mã vé, tuyến, giờ xuất bến, số tiền hoàn, hình thức hoàn (ASM-29) (UC-013)<br>// determineCheckResult: kết luận vé hợp lệ hay không hợp lệ theo trạng thái huỷ và thời điểm soát, kèm lý do, mã chỗ, họ tên người đi, thời điểm soát trước (BR-21, BR-22) (UC-015)<br>// markChecked: ghi nhận vé đã soát kèm thời điểm soát (ASM-35) (UC-015) | ticketCode<br>travelerName<br>travelerPhone<br>price (Số tiền)<br>status (Trạng thái)<br>purchaseChannel (Trạng thái: Trực tuyến hoặc Tại quầy)<br>checkedTime (Giờ) | UC-002, UC-008, UC-013, UC-015 | - | Hoạt động |
| AC-E-BaseFare | entity | BaseFare | // calculateTicketPrice: tính giá một vé từ giá theo tuyến và loại xe và mức tăng giá (BR-05) (UC-002) | busType<br>amount (Số tiền) | UC-002 | - | Hoạt động |
| AC-E-HolidaySurcharge | entity | HolidaySurcharge | // getSurchargeRate: xác định mức tăng áp dụng cho ngày xuất bến, 0% nếu ngoài khoảng ngày (BR-05) (UC-002) | startDate (Ngày)<br>endDate (Ngày)<br>ratePercent (Số lượng, đơn vị phần trăm) | UC-002 | - | Hoạt động |
| AC-E-Refund | entity | Refund | // createRefund: khởi tạo khoản hoàn tiền của vé đã huỷ, ghi mức hoàn, số tiền hoàn, hình thức hoàn và kết quả hoàn (UC-008, UC-013) | refundAmount (Số tiền)<br>refundRate (Số lượng, đơn vị phần trăm)<br>refundMethod (Trạng thái: Qua cổng thanh toán hoặc Tiền mặt tại quầy)<br>refundResult (Trạng thái: đã hoàn, chưa thành công, chờ chi tiền mặt) | UC-008, UC-013 | - | Hoạt động |
| AC-E-PhoneReservation | entity | PhoneReservation | // checkUnpaid: xác định đặt chỗ qua điện thoại chưa thanh toán (ASM-27) (UC-013)<br>// cancelWithTrip: chuyển đặt chỗ chưa thanh toán sang đã huỷ cùng chuyến (ASM-27) (UC-013) | status (Trạng thái) | UC-013 | - | Hoạt động |
| AC-E-TicketCheckSession | entity | TicketCheckSession | // startSession: khởi tạo phiên soát vé cho một chuyến (UC-015)<br>// sendResult: gửi kết quả soát vé của chuyến về dữ liệu vé của hệ thống và cho biết trạng thái gửi (UC-015)<br>// markResultSent: ghi nhận kết quả soát vé đã gửi (UC-015)<br>// keepResultPending: giữ kết quả soát vé chưa gửi để tự gửi khi máy có sóng trở lại (UC-015) | sendStatus (Trạng thái: Đã gửi hoặc Chờ gửi khi có sóng) | UC-015 | - | Hoạt động |
| AC-E-TripPassengerList | entity | TripPassengerList | // findTicket: tìm trong danh sách vé có mã vé đã nhận; không có vé thì vé không thuộc chuyến (BR-20) (UC-015)<br>// summarizeTicketCounts: tính số vé còn hiệu lực, số vé đã soát, số vé còn hiệu lực chưa soát của chuyến (UC-015) | - | UC-015 | - | Hoạt động |

Thuộc tính không ghi kiểu khái niệm là kiểu Văn bản theo P07. Số lớp: 24 (8 boundary, 5 control trong đó 1 control tạm, 11 entity).

## F4. Bảng quan hệ

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn UC | Bằng chứng | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| R-01 | AC-B-BookTicketForm | AC-C-BookTicketOnlineController | Association | - | - | UC-002 | Quy tắc tương tác F6 của P07 | tạm thời; R-UC002-01 |
| R-02 | AC-C-BookTicketOnlineController | AC-B-SmsGateway | Association | - | - | UC-002 | Bước 12 của UC-002 | tạm thời; R-UC002-02 |
| R-03 | AC-C-BookTicketOnlineController | AC-C-PayTicketOnlineController | Dependency | - | - | UC-002 | Bước 10, RL-27 (include UC-003) | tạm thời; «include»; R-UC002-03 |
| R-04 | AC-C-BookTicketOnlineController | AC-E-Trip | Association | - | - | UC-002 | Bước 2, 4 | tạm thời; R-UC002-04 |
| R-05 | AC-C-BookTicketOnlineController | AC-E-Booking | Association | - | - | UC-002 | Bước 6 đến 11 | tạm thời; R-UC002-05 |
| R-06 | AC-C-BookTicketOnlineController | AC-E-Ticket | Association | - | - | UC-002 | Bước 11, 12 | tạm thời; R-UC002-06 |
| R-07 | AC-B-ReturnTicketForm | AC-C-ReturnTicketController | Association | - | - | UC-008 | Bước 1, 5, 6, 11 | tạm thời; R-UC008-01 |
| R-08 | AC-B-CounterReturnTicketForm | AC-C-ReturnTicketController | Association | - | - | UC-008 | Bước 1, 5, 6, 11 (luồng của ACT-02) | tạm thời; R-UC008-02 |
| R-09 | AC-C-ReturnTicketController | AC-B-PaymentGateway | Association | - | - | UC-008 | Bước 8, 9 | tạm thời; R-UC008-03 |
| R-10 | AC-C-ReturnTicketController | AC-E-Ticket | Association | - | - | UC-008 | Bước 2 đến 10 | tạm thời; R-UC008-04 |
| R-11 | AC-B-CancelTripForm | AC-C-CancelTripController | Association | - | - | UC-013 | Bước 1, 3, 4, 11 | tạm thời; R-UC013-01 |
| R-12 | AC-C-CancelTripController | AC-E-Trip | Association | - | - | UC-013 | Bước 2, 5 | tạm thời; R-UC013-02 |
| R-13 | AC-C-CancelTripController | AC-E-Ticket | Association | - | - | UC-013 | Bước 3, 5 đến 10 | tạm thời; R-UC013-03 |
| R-14 | AC-C-CancelTripController | AC-B-PaymentGateway | Association | - | - | UC-013 | Bước 7, 8 | tạm thời; R-UC013-04 |
| R-15 | AC-C-CancelTripController | AC-B-SmsGateway | Association | - | - | UC-013 | Bước 10 | tạm thời; R-UC013-05 |
| R-16 | AC-B-CheckBoardingTicketForm | AC-C-CheckBoardingTicketController | Association | - | - | UC-015 | Bước 1, 3a, 11 | tạm thời; R-UC015-01 |
| R-17 | AC-B-BarcodeScanner | AC-C-CheckBoardingTicketController | Association | - | - | UC-015 | Bước 4 | tạm thời; R-UC015-02 |
| R-18 | AC-C-CheckBoardingTicketController | AC-E-TicketCheckSession | Association | - | - | UC-015 | Bước 2, 10 | tạm thời; R-UC015-03 |
| R-19 | AC-C-CheckBoardingTicketController | AC-E-Trip | Association | - | - | UC-015 | Bước 2 | tạm thời; R-UC015-04 |
| R-20 | AC-C-CheckBoardingTicketController | AC-E-TripPassengerList | Association | - | - | UC-015 | Bước 5, 11 | tạm thời; R-UC015-05 |
| R-21 | AC-C-CheckBoardingTicketController | AC-E-Ticket | Association | - | - | UC-015 | Bước 5 đến 7 | tạm thời; R-UC015-06 |
| R-22 | AC-E-Trip | AC-E-Route | Association | A 0..* - B 1 | - | UC-002, UC-013, UC-015 | GL-04 "Một lần chạy của một tuyến"; GL-36 | Hợp R-UC002-07, R-UC013-06, R-UC015-07 |
| R-23 | AC-E-Trip | AC-E-Seat | Association | A 1 - B 1..* | - | UC-002 | GL-02 "Vị trí dành cho một người đi trên xe của một chuyến"; ASM-42 | R-UC002-08; chưa chọn Composition vì Q-69 (chỗ thuộc xe hay thuộc chuyến) chưa trả lời |
| R-24 | AC-E-Trip | AC-E-BaseFare | Association | A 0..* - B 1 | - | UC-002 | BR-04; GL-09 "các chuyến thuộc tuyến đó chạy loại xe đó"; ASM-56 | R-UC002-09; chuyến tra giá theo tuyến và loại xe của chuyến; điền multiplicity theo ASM-56 |
| R-25 | AC-E-Trip | AC-E-HolidaySurcharge | Association | A 0..* - B | - | UC-002 | BR-05; GL-25 "các chuyến thuộc khoảng ngày đó" | R-UC002-10; phía HolidaySurcharge để trống, phạm vi tuyến, loại xe chờ Q-20 |
| R-26 | AC-E-Booking | AC-E-Trip | Association | A 0..* - B 1 | - | UC-002 | GL-18 "trên cùng một chuyến" | R-UC002-11 |
| R-27 | AC-E-Booking | AC-E-Seat | Association | A 0..1 - B 1..5 | - | UC-002 | BR-01; BR-03; GL-11 | R-UC002-12; phía Booking 0..1 theo ASM-55 (quan hệ thể hiện việc đang giữ chỗ, BR-08 trả chỗ khi hết hạn) |
| R-28 | AC-E-Booking | AC-E-Ticket | Association | A 0..1 - B 0..5 | - | UC-002 | BR-01; BR-10; GL-18 (lần đặt trực tuyến); GL-13 | R-UC002-13; sửa phía Booking từ 1 thành 0..1 vì vé mua tại quầy không có lần đặt (GL-18, GL-13) |
| R-29 | AC-E-Ticket | AC-E-Trip | Association | A 0..* - B 1 | - | UC-002, UC-008, UC-013 | GL-37 "một chỗ xác định của một chuyến" | Hợp R-UC002-14, R-UC008-05, R-UC013-07 (R-UC013-07 vẽ theo chiều Trip - Ticket, đảo chiều khi hợp) |
| R-30 | AC-E-Ticket | AC-E-Seat | Association | A - B 1 | - | UC-002, UC-008, UC-015 | BR-10; GL-37 | Hợp R-UC002-15, R-UC008-06, R-UC015-08; phía Ticket để trống chờ Q-36 (chỗ trả về còn trống có được bán lại bằng vé mới không) |
| R-31 | AC-E-BaseFare | AC-E-Route | Association | A 0..* - B 1 | - | UC-002 | BR-04; GL-09 "Mức giá do quản lý nhà xe đặt cho một cặp tuyến và loại xe" | R-UC002-16; điền phía BaseFare 0..* theo GL-09 (một tuyến có giá theo từng loại xe) |
| R-32 | AC-E-Ticket | AC-E-Refund | Association | A 1 - B 0..1 | - | UC-008, UC-013 | GL-16; ASM-46; ASM-48; ASM-54 | Hợp R-UC008-07, R-UC013-09 |
| R-33 | AC-E-Trip | AC-E-PhoneReservation | Association | A 1 - B 0..* | - | UC-013 | GL-07 "giữ chỗ trên một chuyến" | R-UC013-08 |
| R-34 | AC-E-Trip | AC-E-TripPassengerList | Association | A 1 - B | - | UC-015 | GL-05 "của một chuyến"; BR-33 | R-UC015-09; phía TripPassengerList để trống chờ Q-73 (bản sao riêng trên máy hay dữ liệu dùng chung) |
| R-35 | AC-E-TripPassengerList | AC-E-Ticket | Association | A 1 - B 0..* | - | UC-015 | GL-05 "Tập dữ liệu các vé đã phát hành của một chuyến"; ASM-33; ASM-50 | R-UC015-10 |
| R-36 | AC-E-TicketCheckSession | AC-E-Trip | Association | A - B 1 | - | UC-015 | GL-28 "của một chuyến"; ASM-32 | R-UC015-11; phía TicketCheckSession để trống chờ Q-77 |
| R-37 | AC-E-PhoneReservation | AC-E-Seat | Association | A 0..1 - B | - | UC-013 | GL-07; GL-11 "một đặt chỗ qua điện thoại" | Mới ở P08; phía Seat để trống chờ Q-76 (số chỗ của một đặt chỗ qua điện thoại) |

Quan hệ giữa boundary với control và giữa control với entity (R-01 đến R-21) giữ ở dạng association tạm, chỉ thể hiện ai dùng ai; R-03 là dependency do «include» giữa hai control. Multiplicity "A <m> - B <m>" đọc theo quy ước: số ở phía A đếm số đối tượng A ứng với một đối tượng B, số ở phía B đếm số đối tượng B ứng với một đối tượng A. Phía để trống có mã Q hoặc ASM ở cột Ghi chú.

Đối chiếu độ phủ VOPC: 16 + 7 + 9 + 11 = 43 quan hệ của P07 được hợp vào 36 quan hệ R-01 đến R-36; R-37 là quan hệ mới. Bảng hợp: R-UC002-01 đến R-UC002-06 --> R-01 đến R-06; R-UC002-07 đến R-UC002-16 --> R-22, R-23, R-24, R-25, R-26, R-27, R-28, R-29, R-30, R-31; R-UC008-01 đến R-UC008-04 --> R-07 đến R-10; R-UC008-05, R-UC008-06, R-UC008-07 --> R-29, R-30, R-32; R-UC013-01 đến R-UC013-05 --> R-11 đến R-15; R-UC013-06 đến R-UC013-09 --> R-22, R-29, R-33, R-32; R-UC015-01 đến R-UC015-06 --> R-16 đến R-21; R-UC015-07 đến R-UC015-11 --> R-22, R-30, R-34, R-35, R-36.

Aggregation, composition, generalization: không có. Trip --> Seat chưa chọn composition vì Q-69 (chỗ thuộc xe hay thuộc chuyến) chưa trả lời. Booking --> Ticket, Ticket --> Refund, Trip --> PhoneReservation không có câu về vòng đời phụ thuộc. Không có cặp entity nào có câu "Mọi B đều là A" trong glossary nên không có generalization. Các tam giác Trip - Ticket - Seat, Trip - Route - BaseFare, Trip - TripPassengerList - Ticket đều được giữ vì mỗi cạnh có ý nghĩa riêng (vé tồn tại trước danh sách hành khách; BaseFare tra theo tuyến và loại xe chứ không chỉ theo tuyến; Ticket gắn trực tiếp một chuyến theo GL-37).

## F5. Analysis class diagram tổng thể

File diagrams/P08-class-analysis.drawio, ba trang: Entity (trang tổng thể, mô hình miền), Bán vé, Vận hành chuyến (hai nhóm chức năng của P02 có use case đã phân tích). Hệ thống có 24 lớp, dưới ngưỡng 30 lớp nhưng vẫn chia view theo quy tắc mặc định vì sơ đồ gộp vượt ngưỡng 20 lớp và 25 cạnh của một trang. Mỗi lớp xuất hiện ở trang nào thì cell có ID gốc; trang Entity dùng ID gốc, hai trang còn lại thêm hậu tố __V2, __V3 cho mọi cell (lớp, cạnh, nhãn).

| Trang | Số lớp | Số cạnh |
|---|---|---|
| Entity | 11 | 16 |
| Bán vé | 16 | 21 |
| Vận hành chuyến | 15 | 21 |

a) Bảng Node

| ID (mã AC) | Loại (Class) | Nhãn | Stereotype | Thuộc về (view) | Ngăn thuộc tính | Ngăn trách nhiệm | ID mxCell | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AC-E-Route | Class | Route | «entity» | Entity | departurePoint<br>arrivalPoint | // checkRouteMatches | AC-E-Route | 40 | 40 | 250 | 110 |
| AC-E-BaseFare | Class | BaseFare | «entity» | Entity | busType<br>amount | // calculateTicketPrice | AC-E-BaseFare | 350 | 40 | 250 | 110 |
| AC-E-HolidaySurcharge | Class | HolidaySurcharge | «entity» | Entity | startDate<br>endDate<br>ratePercent | // getSurchargeRate | AC-E-HolidaySurcharge | 660 | 40 | 250 | 130 |
| AC-E-TicketCheckSession | Class | TicketCheckSession | «entity» | Entity | sendStatus | // startSession<br>// sendResult<br>// markResultSent<br>// keepResultPending | AC-E-TicketCheckSession | 970 | 40 | 250 | 150 |
| AC-E-Booking | Class | Booking | «entity» | Entity | totalAmount<br>holdStartTime<br>status<br>travelerInfos | // createBooking<br>// checkMaxSeats<br>// validateTravelerInfo<br>// calculateTotal<br>// holdSeats<br>// releaseSeats<br>// issueTickets<br>// getBookingSummary | AC-E-Booking | 40 | 270 | 250 | 290 |
| AC-E-Trip | Class | Trip | «entity» | Entity | departureTime<br>busType<br>availableSeatCount<br>status | // findMatchingTrips<br>// getSeatMap<br>// checkSeatsAvailable<br>// determineTicketPrice<br>// getRouteAndDepartureTime<br>// calculateTimeToDeparture<br>// findTrip<br>// checkNotCancelled<br>// checkBeforeDeparture<br>// getCancellationSummary<br>// cancelTrip | AC-E-Trip | 350 | 270 | 250 | 350 |
| AC-E-Ticket | Class | Ticket | «entity» | Entity | ticketCode<br>travelerName<br>travelerPhone<br>price<br>status<br>purchaseChannel<br>checkedTime | // createTicket<br>// getTicketSmsContent<br>// findTicket<br>// checkNotCancelled<br>// checkPurchaseChannel<br>// checkReturnTimeLimit<br>// calculateRefundAmount<br>// getTicketReturnInfo<br>// determineRefundMethod<br>// cancelTicket<br>// getCancelImpactInfo<br>// cancelWithTrip<br>// calculateTripCancelRefundAmount<br>// recordRefund<br>// getTripCancelSmsContent<br>// determineCheckResult<br>// markChecked | AC-E-Ticket | 660 | 270 | 250 | 530 |
| AC-E-Seat | Class | Seat | «entity» | Entity | seatCode<br>status | // checkAvailable<br>// hold<br>// release<br>// getSeatCode | AC-E-Seat | 40 | 900 | 250 | 170 |
| AC-E-PhoneReservation | Class | PhoneReservation | «entity» | Entity | status | // checkUnpaid<br>// cancelWithTrip | AC-E-PhoneReservation | 350 | 900 | 250 | 110 |
| AC-E-TripPassengerList | Class | TripPassengerList | «entity» | Entity | - | // findTicket<br>// summarizeTicketCounts | AC-E-TripPassengerList | 660 | 900 | 250 | 110 |
| AC-E-Refund | Class | Refund | «entity» | Entity | refundAmount<br>refundRate<br>refundMethod<br>refundResult | // createRefund | AC-E-Refund | 970 | 900 | 250 | 150 |
| AC-B-BookTicketForm | Class | BookTicketForm | «boundary» | Bán vé | departurePoint<br>arrivalPoint<br>travelDate<br>selectedSeats<br>travelerNames<br>travelerPhones | // requestBooking<br>// selectTrip<br>// selectSeatsAndEnterTravelerInfo<br>// showTrips<br>// showSeatMap<br>// showNoTripFoundNotice<br>// showNoSeatLeftNotice<br>// showSeatLimitExceededNotice<br>// showSeatsUnavailableNotice<br>// showMissingTravelerInfoNotice<br>// showInvalidPhoneNotice<br>// showHoldExpiredNotice<br>// showPaymentFailedNotice<br>// showIssuedTickets | AC-B-BookTicketForm__V2 | 40 | 40 | 250 | 450 |
| AC-B-SmsGateway | Class | SmsGateway | «boundary» | Bán vé | recipientPhone<br>smsContent | // sendSms | AC-B-SmsGateway__V2 | 350 | 40 | 250 | 110 |
| AC-B-ReturnTicketForm | Class | ReturnTicketForm | «boundary» | Bán vé | ticketCode<br>travelerPhone | // requestReturnTicket<br>// confirmReturnTicket<br>// declineReturnTicket<br>// showReturnInfo<br>// showTicketNotFoundNotice<br>// showTicketCancelledNotice<br>// showWrongChannelNotice<br>// showReturnTimeLimitNotice<br>// showReturnAbortedNotice<br>// showRefundFailedNotice<br>// showReturnResult | AC-B-ReturnTicketForm__V2 | 970 | 40 | 250 | 310 |
| AC-B-CounterReturnTicketForm | Class | CounterReturnTicketForm | «boundary» | Bán vé | ticketCode | // requestReturnTicket<br>// confirmReturnTicket<br>// declineReturnTicket<br>// showReturnInfo<br>// showTicketNotFoundNotice<br>// showTicketCancelledNotice<br>// showWrongChannelNotice<br>// showReturnTimeLimitNotice<br>// showReturnAbortedNotice<br>// showRefundFailedNotice<br>// showReturnResult | AC-B-CounterReturnTicketForm__V2 | 1280 | 40 | 250 | 290 |
| AC-B-PaymentGateway | Class | PaymentGateway | «boundary» | Bán vé | ticketCode<br>refundAmount | // requestRefund<br>// returnRefundResult | AC-B-PaymentGateway__V2 | 1590 | 40 | 250 | 130 |
| AC-C-BookTicketOnlineController | Class | BookTicketOnlineController | «control» | Bán vé | - | // searchTrips<br>// getSeatMap<br>// submitBooking<br>// startWaitingForPayment<br>// handleSeatHoldExpired | AC-C-BookTicketOnlineController__V2 | 40 | 570 | 250 | 170 |
| AC-C-PayTicketOnlineController | Class | PayTicketOnlineController | «control» | Bán vé | - | // payTickets | AC-C-PayTicketOnlineController__V2 | 350 | 570 | 250 | 90 |
| AC-C-ReturnTicketController | Class | ReturnTicketController | «control» | Bán vé | - | // startReturnTicket<br>// confirmReturn<br>// cancelReturnRequest | AC-C-ReturnTicketController__V2 | 1280 | 570 | 250 | 130 |
| AC-E-Trip | Class | Trip | «entity» | Bán vé | departureTime<br>busType<br>availableSeatCount<br>status | // findMatchingTrips<br>// getSeatMap<br>// checkSeatsAvailable<br>// determineTicketPrice<br>// getRouteAndDepartureTime<br>// calculateTimeToDeparture<br>// findTrip<br>// checkNotCancelled<br>// checkBeforeDeparture<br>// getCancellationSummary<br>// cancelTrip | AC-E-Trip__V2 | 40 | 820 | 250 | 350 |
| AC-E-Booking | Class | Booking | «entity» | Bán vé | totalAmount<br>holdStartTime<br>status<br>travelerInfos | // createBooking<br>// checkMaxSeats<br>// validateTravelerInfo<br>// calculateTotal<br>// holdSeats<br>// releaseSeats<br>// issueTickets<br>// getBookingSummary | AC-E-Booking__V2 | 350 | 820 | 250 | 290 |
| AC-E-Ticket | Class | Ticket | «entity» | Bán vé | ticketCode<br>travelerName<br>travelerPhone<br>price<br>status<br>purchaseChannel<br>checkedTime | // createTicket<br>// getTicketSmsContent<br>// findTicket<br>// checkNotCancelled<br>// checkPurchaseChannel<br>// checkReturnTimeLimit<br>// calculateRefundAmount<br>// getTicketReturnInfo<br>// determineRefundMethod<br>// cancelTicket<br>// getCancelImpactInfo<br>// cancelWithTrip<br>// calculateTripCancelRefundAmount<br>// recordRefund<br>// getTripCancelSmsContent<br>// determineCheckResult<br>// markChecked | AC-E-Ticket__V2 | 660 | 820 | 250 | 530 |
| AC-E-Route | Class | Route | «entity» | Bán vé | departurePoint<br>arrivalPoint | // checkRouteMatches | AC-E-Route__V2 | 40 | 1470 | 250 | 110 |
| AC-E-BaseFare | Class | BaseFare | «entity» | Bán vé | busType<br>amount | // calculateTicketPrice | AC-E-BaseFare__V2 | 350 | 1470 | 250 | 110 |
| AC-E-HolidaySurcharge | Class | HolidaySurcharge | «entity» | Bán vé | startDate<br>endDate<br>ratePercent | // getSurchargeRate | AC-E-HolidaySurcharge__V2 | 660 | 1470 | 250 | 130 |
| AC-E-Seat | Class | Seat | «entity» | Bán vé | seatCode<br>status | // checkAvailable<br>// hold<br>// release<br>// getSeatCode | AC-E-Seat__V2 | 970 | 1470 | 250 | 170 |
| AC-E-Refund | Class | Refund | «entity» | Bán vé | refundAmount<br>refundRate<br>refundMethod<br>refundResult | // createRefund | AC-E-Refund__V2 | 1280 | 1470 | 250 | 150 |
| AC-B-CancelTripForm | Class | CancelTripForm | «boundary» | Vận hành chuyến | departurePoint<br>arrivalPoint<br>departureDate<br>departureTime | // requestCancelTrip<br>// confirmCancelTrip<br>// declineCancelTrip<br>// showCancelTripInfo<br>// showTripNotFoundNotice<br>// showTripAlreadyCancelledNotice<br>// showTripDepartedNotice<br>// showCancelTripAbortedNotice<br>// showCancelTripResult | AC-B-CancelTripForm__V3 | 40 | 40 | 250 | 310 |
| AC-B-PaymentGateway | Class | PaymentGateway | «boundary» | Vận hành chuyến | ticketCode<br>refundAmount | // requestRefund<br>// returnRefundResult | AC-B-PaymentGateway__V3 | 350 | 40 | 250 | 130 |
| AC-B-SmsGateway | Class | SmsGateway | «boundary» | Vận hành chuyến | recipientPhone<br>smsContent | // sendSms | AC-B-SmsGateway__V3 | 660 | 40 | 250 | 110 |
| AC-B-CheckBoardingTicketForm | Class | CheckBoardingTicketForm | «boundary» | Vận hành chuyến | departurePoint<br>arrivalPoint<br>departureTime<br>ticketCode | // requestStartCheck<br>// enterTicketCode<br>// requestEndCheck<br>// showCheckSessionInfo<br>// showValidTicketResult<br>// showInvalidTicketResult<br>// showCheckSummary | AC-B-CheckBoardingTicketForm__V3 | 970 | 40 | 250 | 270 |
| AC-B-BarcodeScanner | Class | BarcodeScanner | «boundary» | Vận hành chuyến | ticketCode | // readBarcode | AC-B-BarcodeScanner__V3 | 1280 | 40 | 250 | 90 |
| AC-C-CancelTripController | Class | CancelTripController | «control» | Vận hành chuyến | - | // startCancelTrip<br>// confirmCancel<br>// cancelCancelTripRequest<br>// cancelTripTriggers | AC-C-CancelTripController__V3 | 350 | 430 | 250 | 150 |
| AC-C-CheckBoardingTicketController | Class | CheckBoardingTicketController | «control» | Vận hành chuyến | - | // startCheck<br>// checkTicket<br>// endCheck | AC-C-CheckBoardingTicketController__V3 | 970 | 430 | 250 | 130 |
| AC-E-TicketCheckSession | Class | TicketCheckSession | «entity» | Vận hành chuyến | sendStatus | // startSession<br>// sendResult<br>// markResultSent<br>// keepResultPending | AC-E-TicketCheckSession__V3 | 40 | 670 | 250 | 150 |
| AC-E-Trip | Class | Trip | «entity» | Vận hành chuyến | departureTime<br>busType<br>availableSeatCount<br>status | // findMatchingTrips<br>// getSeatMap<br>// checkSeatsAvailable<br>// determineTicketPrice<br>// getRouteAndDepartureTime<br>// calculateTimeToDeparture<br>// findTrip<br>// checkNotCancelled<br>// checkBeforeDeparture<br>// getCancellationSummary<br>// cancelTrip | AC-E-Trip__V3 | 350 | 670 | 250 | 350 |
| AC-E-Ticket | Class | Ticket | «entity» | Vận hành chuyến | ticketCode<br>travelerName<br>travelerPhone<br>price<br>status<br>purchaseChannel<br>checkedTime | // createTicket<br>// getTicketSmsContent<br>// findTicket<br>// checkNotCancelled<br>// checkPurchaseChannel<br>// checkReturnTimeLimit<br>// calculateRefundAmount<br>// getTicketReturnInfo<br>// determineRefundMethod<br>// cancelTicket<br>// getCancelImpactInfo<br>// cancelWithTrip<br>// calculateTripCancelRefundAmount<br>// recordRefund<br>// getTripCancelSmsContent<br>// determineCheckResult<br>// markChecked | AC-E-Ticket__V3 | 660 | 670 | 250 | 530 |
| AC-E-TripPassengerList | Class | TripPassengerList | «entity» | Vận hành chuyến | - | // findTicket<br>// summarizeTicketCounts | AC-E-TripPassengerList__V3 | 970 | 670 | 250 | 110 |
| AC-E-Route | Class | Route | «entity» | Vận hành chuyến | departurePoint<br>arrivalPoint | // checkRouteMatches | AC-E-Route__V3 | 350 | 1300 | 250 | 110 |
| AC-E-PhoneReservation | Class | PhoneReservation | «entity» | Vận hành chuyến | status | // checkUnpaid<br>// cancelWithTrip | AC-E-PhoneReservation__V3 | 660 | 1300 | 250 | 110 |
| AC-E-Seat | Class | Seat | «entity» | Vận hành chuyến | seatCode<br>status | // checkAvailable<br>// hold<br>// release<br>// getSeatCode | AC-E-Seat__V3 | 970 | 1300 | 250 | 170 |
| AC-E-Refund | Class | Refund | «entity» | Vận hành chuyến | refundAmount<br>refundRate<br>refundMethod<br>refundResult | // createRefund | AC-E-Refund__V3 | 1280 | 1300 | 250 | 150 |

b) Bảng Edge

Cột Điểm uốn là toạ độ tuyệt đối theo thứ tự từ nguồn tới đích, "-" nghĩa là cạnh đi thẳng. Nhãn multiplicity vẽ thành hai nhãn con ở hai đầu cạnh (đầu nguồn là Lớp A, đầu đích là Lớp B), không vẽ nhãn cho phía để trống và cho quan hệ tạm.

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Thuộc về (view) | Điểm uốn |
|---|---|---|---|---|---|---|
| R-22 | AC-E-Trip | AC-E-Route | Association | A 0..* - B 1 | Entity | (410,210); (230,210) |
| R-23 | AC-E-Trip | AC-E-Seat | Association | A 1 - B 1..* | Entity | (410,820); (190,820) |
| R-24 | AC-E-Trip | AC-E-BaseFare | Association | A 0..* - B 1 | Entity | - |
| R-25 | AC-E-Trip | AC-E-HolidaySurcharge | Association | A 0..* - B | Entity | (500,220); (720,220) |
| R-26 | AC-E-Booking | AC-E-Trip | Association | A 0..* - B 1 | Entity | - |
| R-27 | AC-E-Booking | AC-E-Seat | Association | A 0..1 - B 1..5 | Entity | - |
| R-28 | AC-E-Booking | AC-E-Ticket | Association | A 0..1 - B 0..5 | Entity | (230,830); (680,830) |
| R-29 | AC-E-Ticket | AC-E-Trip | Association | A 0..* - B 1 | Entity | - |
| R-30 | AC-E-Ticket | AC-E-Seat | Association | A - B 1 | Entity | (760,840); (270,840) |
| R-31 | AC-E-BaseFare | AC-E-Route | Association | A 0..* - B 1 | Entity | - |
| R-32 | AC-E-Ticket | AC-E-Refund | Association | A 1 - B 0..1 | Entity | (850,860); (1030,860) |
| R-33 | AC-E-Trip | AC-E-PhoneReservation | Association | A 1 - B 0..* | Entity | - |
| R-34 | AC-E-Trip | AC-E-TripPassengerList | Association | A 1 - B | Entity | (540,850); (720,850) |
| R-35 | AC-E-TripPassengerList | AC-E-Ticket | Association | A 1 - B 0..* | Entity | - |
| R-36 | AC-E-TicketCheckSession | AC-E-Trip | Association | A - B 1 | Entity | (1030,230); (580,230) |
| R-37 | AC-E-PhoneReservation | AC-E-Seat | Association | A 0..1 - B | Entity | - |
| R-01 | AC-B-BookTicketForm | AC-C-BookTicketOnlineController | Association | - | Bán vé | - |
| R-02 | AC-C-BookTicketOnlineController | AC-B-SmsGateway | Association | - | Bán vé | (230,510); (410,510) |
| R-03 | AC-C-BookTicketOnlineController | AC-C-PayTicketOnlineController | Dependency | - | Bán vé | - |
| R-04 | AC-C-BookTicketOnlineController | AC-E-Trip | Association | - | Bán vé | - |
| R-05 | AC-C-BookTicketOnlineController | AC-E-Booking | Association | - | Bán vé | (190,760); (410,760) |
| R-06 | AC-C-BookTicketOnlineController | AC-E-Ticket | Association | - | Bán vé | (270,770); (720,770) |
| R-07 | AC-B-ReturnTicketForm | AC-C-ReturnTicketController | Association | - | Bán vé | (1160,520); (1340,520) |
| R-08 | AC-B-CounterReturnTicketForm | AC-C-ReturnTicketController | Association | - | Bán vé | - |
| R-09 | AC-C-ReturnTicketController | AC-B-PaymentGateway | Association | - | Bán vé | (1470,530); (1650,530) |
| R-10 | AC-C-ReturnTicketController | AC-E-Ticket | Association | - | Bán vé | (1340,780); (850,780) |
| R-22 | AC-E-Trip | AC-E-Route | Association | A 0..* - B 1 | Bán vé | - |
| R-23 | AC-E-Trip | AC-E-Seat | Association | A 1 - B 1..* | Bán vé | (270,1400); (990,1400) |
| R-24 | AC-E-Trip | AC-E-BaseFare | Association | A 0..* - B 1 | Bán vé | (190,1370); (410,1370) |
| R-25 | AC-E-Trip | AC-E-HolidaySurcharge | Association | A 0..* - B | Bán vé | (220,1380); (720,1380) |
| R-26 | AC-E-Booking | AC-E-Trip | Association | A 0..* - B 1 | Bán vé | - |
| R-27 | AC-E-Booking | AC-E-Seat | Association | A 0..1 - B 1..5 | Bán vé | (540,1410); (1030,1410) |
| R-28 | AC-E-Booking | AC-E-Ticket | Association | A 0..1 - B 0..5 | Bán vé | - |
| R-29 | AC-E-Ticket | AC-E-Trip | Association | A 0..* - B 1 | Bán vé | (720,1390); (240,1390) |
| R-30 | AC-E-Ticket | AC-E-Seat | Association | A - B 1 | Bán vé | (810,1420); (1070,1420) |
| R-31 | AC-E-BaseFare | AC-E-Route | Association | A 0..* - B 1 | Bán vé | - |
| R-32 | AC-E-Ticket | AC-E-Refund | Association | A 1 - B 0..1 | Bán vé | (890,1430); (1340,1430) |
| R-11 | AC-B-CancelTripForm | AC-C-CancelTripController | Association | - | Vận hành chuyến | (230,370); (410,370) |
| R-12 | AC-C-CancelTripController | AC-E-Trip | Association | - | Vận hành chuyến | - |
| R-13 | AC-C-CancelTripController | AC-E-Ticket | Association | - | Vận hành chuyến | (540,610); (720,610) |
| R-14 | AC-C-CancelTripController | AC-B-PaymentGateway | Association | - | Vận hành chuyến | - |
| R-15 | AC-C-CancelTripController | AC-B-SmsGateway | Association | - | Vận hành chuyến | (540,380); (720,380) |
| R-16 | AC-B-CheckBoardingTicketForm | AC-C-CheckBoardingTicketController | Association | - | Vận hành chuyến | - |
| R-17 | AC-B-BarcodeScanner | AC-C-CheckBoardingTicketController | Association | - | Vận hành chuyến | (1340,390); (1160,390) |
| R-18 | AC-C-CheckBoardingTicketController | AC-E-TicketCheckSession | Association | - | Vận hành chuyến | (990,600); (230,600) |
| R-19 | AC-C-CheckBoardingTicketController | AC-E-Trip | Association | - | Vận hành chuyến | (1030,620); (540,620) |
| R-20 | AC-C-CheckBoardingTicketController | AC-E-TripPassengerList | Association | - | Vận hành chuyến | - |
| R-21 | AC-C-CheckBoardingTicketController | AC-E-Ticket | Association | - | Vận hành chuyến | (1070,630); (850,630) |
| R-22 | AC-E-Trip | AC-E-Route | Association | A 0..* - B 1 | Vận hành chuyến | - |
| R-23 | AC-E-Trip | AC-E-Seat | Association | A 1 - B 1..* | Vận hành chuyến | (540,1230); (990,1230) |
| R-29 | AC-E-Ticket | AC-E-Trip | Association | A 0..* - B 1 | Vận hành chuyến | - |
| R-30 | AC-E-Ticket | AC-E-Seat | Association | A - B 1 | Vận hành chuyến | (810,1250); (1070,1250) |
| R-32 | AC-E-Ticket | AC-E-Refund | Association | A 1 - B 0..1 | Vận hành chuyến | (890,1260); (1340,1260) |
| R-33 | AC-E-Trip | AC-E-PhoneReservation | Association | A 1 - B 0..* | Vận hành chuyến | (500,1220); (720,1220) |
| R-34 | AC-E-Trip | AC-E-TripPassengerList | Association | A 1 - B | Vận hành chuyến | (580,1240); (1030,1240) |
| R-35 | AC-E-TripPassengerList | AC-E-Ticket | Association | A 1 - B 0..* | Vận hành chuyến | - |
| R-36 | AC-E-TicketCheckSession | AC-E-Trip | Association | A - B 1 | Vận hành chuyến | - |
| R-37 | AC-E-PhoneReservation | AC-E-Seat | Association | A 0..1 - B | Vận hành chuyến | - |

## F6. Rà soát lớp phân tích

| AC | Tên phản ánh đúng vai trò | Một khái niệm duy nhất | Trách nhiệm gắn kết | Cung cấp đủ hành vi cần | Yêu cầu đặc thù (BR, NFR) đã gắn | Ghi chú |
|---|---|---|---|---|---|---|
| AC-B-BookTicketForm | Đạt: tên theo hành động của use case | Đạt: giao diện đặt vé của ACT-01 | Đạt: chỉ nhận nhập và hiển thị | Đạt: đủ cho bước 1 đến 13 của UC-002 | Đạt: BR-01, BR-07 thể hiện qua thông báo | - |
| AC-B-ReturnTicketForm | Đạt | Đạt: giao diện trả vé của ACT-01 | Đạt | Đạt: đủ cho UC-008 | Đạt: BR-11, BR-12 thể hiện qua thông báo | 11 trách nhiệm trùng tên với CounterReturnTicketForm (F2a) |
| AC-B-CounterReturnTicketForm | Đạt | Đạt: giao diện trả vé của ACT-02 | Đạt | Đạt: đủ cho UC-008 | Đạt: BR-11, BR-12 | 11 trách nhiệm trùng tên với ReturnTicketForm (F2a) |
| AC-B-CancelTripForm | Đạt | Đạt: giao diện huỷ chuyến của ACT-03 | Đạt | Đạt: đủ cho UC-013 | Đạt: BR-17 thể hiện qua tổng số tiền hoàn | - |
| AC-B-CheckBoardingTicketForm | Đạt | Đạt: giao diện soát vé của ACT-05 | Đạt | Đạt: đủ cho UC-015 | Đạt: BR-20, BR-21, BR-22 thể hiện qua lý do không hợp lệ | - |
| AC-B-BarcodeScanner | Đạt: tên theo thiết bị | Đạt: giao diện thiết bị của ACT-09 | Đạt | Đạt: readBarcode | Đạt: GL-22, GL-40; Q-54 (model máy, loại mã vạch) chưa trả lời | - |
| AC-B-SmsGateway | Đạt: tên theo hệ thống | Đạt: giao diện Cổng SMS của ACT-07 | Đạt: một trách nhiệm sendSms | Đạt: UC-002 bước 12, UC-013 bước 10 | Đạt: GL-30; lỗi gửi SMS chưa có luồng (Q-56) | - |
| AC-B-PaymentGateway | Đạt: tên theo hệ thống | Đạt: giao diện Cổng thanh toán của ACT-06 | Đạt: hai trách nhiệm về hoàn tiền | Đạt: UC-008, UC-013; trách nhiệm thanh toán sẽ do P07 của UC-003 bổ sung | Đạt: BR-15; NFR-07 (API chưa có tài liệu, Q-24) | - |
| AC-C-BookTicketOnlineController | Đạt | Đạt: điều phối UC-002 | Đạt: 5 trách nhiệm điều phối | Đạt | Đạt: BR-07 (startWaitingForPayment, handleSeatHoldExpired) | - |
| AC-C-PayTicketOnlineController | Đạt | Đạt: điều phối UC-003 | Đạt | - | Đạt: BR thanh toán thuộc UC-003 chưa phân tích | Trạng thái Tạm |
| AC-C-ReturnTicketController | Đạt | Đạt: điều phối UC-008 | Đạt: 3 trách nhiệm | Đạt | Đạt: BR-11 đến BR-16 qua Ticket | - |
| AC-C-CancelTripController | Đạt | Đạt: điều phối UC-013 | Đạt: 4 trách nhiệm | Đạt | Đạt: BR-18, BR-19 qua Ticket và SmsGateway | - |
| AC-C-CheckBoardingTicketController | Đạt | Đạt: điều phối UC-015 | Đạt: 3 trách nhiệm | Đạt | Đạt: BR-20 đến BR-22 qua Ticket và TripPassengerList | - |
| AC-E-Trip | Đạt: GL-04 | Đạt: một lần chạy của một tuyến | Đạt: 11 trách nhiệm đều về tìm, kiểm tra điều kiện và huỷ chuyến; rà lại ở P10 | Đạt: đủ cho 4 use case | Đạt: BR-05 (giá vé), BR-17 (tổng hợp huỷ chuyến) | - |
| AC-E-Route | Đạt: GL-36 | Đạt | Đạt | Đạt | Đạt: không có BR riêng | Chỉ một trách nhiệm hành vi |
| AC-E-Seat | Đạt: GL-02 | Đạt | Đạt | Đạt | Không đạt: BR-03 là suy luận nhưng status được lưu với ba giá trị (ASM-42), Q-75 | Có hành động: Q-75 |
| AC-E-Booking | Đạt: GL-18 | Đạt: một lần đặt | Đạt: 8 trách nhiệm về tạo, kiểm tra, giữ, phát hành | Đạt | Đạt: BR-01, BR-06, BR-08, BR-09, BR-10 | - |
| AC-E-Ticket | Đạt: GL-37 | Đạt: vé của một chỗ | Không đạt: 17 trách nhiệm gom phát hành, trả vé, huỷ theo chuyến, lập SMS, soát vé | Đạt: đủ cho 4 use case | Đạt: BR-10 đến BR-17, BR-21, BR-22 | Có hành động: Vấn đề còn mở (cân nhắc tách ở P10) |
| AC-E-BaseFare | Đạt: GL-09 | Đạt | Đạt | Đạt | Đạt: BR-04, BR-05 | Chỉ một trách nhiệm hành vi |
| AC-E-HolidaySurcharge | Đạt: GL-25 | Đạt | Đạt | Đạt | Đạt: BR-05; BR-32 thuộc UC-017 chưa phân tích | Chỉ một trách nhiệm hành vi |
| AC-E-Refund | Đạt: GL-16 | Đạt | Đạt | Đạt: tính số tiền hoàn do Ticket đảm nhận vì Refund chưa tồn tại lúc tính (ASM-46, ASM-48) | Đạt: BR-13 đến BR-17 | Chỉ một trách nhiệm hành vi |
| AC-E-PhoneReservation | Đạt: GL-07 | Đạt | Đạt | Đạt: chỉ phần UC-013 cần; UC-004, UC-006 bổ sung khi phân tích | Đạt: BR-24 thuộc UC-004, UC-006 | Chỉ có thuộc tính status; chờ P07 của UC-004, UC-006 |
| AC-E-TicketCheckSession | Đạt: GL-28 | Đạt | Đạt | Đạt | Đạt: ASM-51 | - |
| AC-E-TripPassengerList | Đạt: GL-05 | Đạt | Đạt | Đạt | Đạt: BR-20, BR-33 | Chưa có thuộc tính, chờ Q-73 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-75 | Trạng thái của chỗ là thuộc tính được lưu với ba giá trị (còn trống, đang giữ, đã có vé) hay được suy ra từ vé và lần đặt theo BR-03? (Lưu / Suy ra) | AC-E-Seat (status), AC-E-Trip (availableSeatCount), R-23, R-30; P10, P12, P13 | BR-03 loại "Suy luận"; GL-02 "Trạng thái: Còn trống, Không còn trống"; ASM-42 ba giá trị |
| Q-76 | Một đặt chỗ qua điện thoại giữ một chỗ hay nhiều chỗ? (Một chỗ / Nhiều chỗ, tối đa bao nhiêu) | R-37 phía AC-E-Seat; P07 của UC-004 | GL-07 "Yêu cầu giữ chỗ trên một chuyến" không nêu số chỗ; BR-01 chỉ giới hạn lần đặt trực tuyến |
| Q-77 | Một chuyến có thể có nhiều phiên soát vé cùng lúc (nhiều phụ xe, nhiều máy soát vé) không? (Một phiên / Nhiều phiên) | R-36 phía AC-E-TicketCheckSession | GL-28 "Khoảng làm việc trong đó phụ xe soát ... của một chuyến"; ASM-32 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-54 | Mỗi vé đã huỷ có tối đa một khoản hoàn tiền (Refund) với refundResult gồm ba giá trị đã hoàn, chưa thành công, chờ chi tiền mặt. Khi trả vé (UC-008), khoản hoàn chỉ được tạo khi hoàn thành công hoặc chờ chi tiền mặt, vì khi hoàn không thành công vé chưa được huỷ. Khi huỷ chuyến (UC-013), khoản hoàn được tạo cả khi chưa thành công, vì vé đã huỷ trước khi hoàn. | Dung hoà ASM-46 của P07 UC-008 và ASM-48 của P07 UC-013, hai giả định cùng nói về một lớp nhưng khác thời điểm tạo | AC-E-Refund; R-32; F2b |
| ASM-55 | Quan hệ Booking - Seat thể hiện việc đang giữ chỗ: tại một thời điểm một chỗ được giữ cho tối đa một lần đặt, và quan hệ chấm dứt khi hết thời hạn giữ chỗ hoặc khi vé được phát hành. | BR-03 "không đang được giữ cho một lần đặt chưa hết thời hạn" và GL-11 "dành riêng cho một lần đặt" nêu việc giữ cho một lần đặt; nguồn không nêu lịch sử giữ chỗ nhiều lần đặt | R-27 |
| ASM-56 | Mỗi chuyến có đúng một giá vé theo tuyến và loại xe tại thời điểm bán vé. | GL-08, BR-04, BR-05: giá vé của chuyến được tính từ giá theo tuyến và loại xe; chuyến không có giá thì không bán được vé | R-24; AC-E-BaseFare |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P07 (UC-002) | R-UC002-13 | Phía Booking ghi 1 nhưng vé mua tại quầy không có lần đặt (GL-18 chỉ nói lần đặt trực tuyến, GL-13 có kênh mua tại quầy) | Sửa thành 0..1 khi chạy lại P07 UC-002; P08 đã dùng 0..1 ở R-28 |
| P07 (UC-002, UC-013) | AC-B-SmsGateway: sendTicketSms, sendTripCancelSms | Hai trách nhiệm cùng ý nghĩa, P08 hợp thành sendSms | Chấp nhận P08 làm nguồn chuẩn cho tên trách nhiệm; cập nhật P07 khi chạy lại |
| P07 (UC-008) | ASM-46 | Giả định khoản hoàn chỉ tạo khi hoàn thành công, khác ASM-48 của UC-013 | Trích ASM-54 của P08 khi chạy lại P07 UC-008 |
| P05 | GL-02, GL-03 | GL-02 ghi hai trạng thái chỗ, trong khi P07 UC-002 dùng ba trạng thái (ASM-42) | Rà lại sau khi Q-75 được trả lời |

## Vấn đề còn mở

- Phạm vi (Target 1): 14 use case trong P02 chưa có artifact P07 (UC-001, UC-003, UC-004, UC-005, UC-006, UC-007, UC-009, UC-010, UC-011, UC-012, UC-014, UC-016, UC-017, UC-018). Mục [Context] của prompt đặt phạm vi là toàn hệ thống, còn YEU_CAU_BO_SUNG giới hạn 4 use case; đã chọn YEU_CAU_BO_SUNG (C9, ưu tiên 2). Mô hình chưa có các khái niệm của use case chưa phân tích (khoản thanh toán GL-17, tài khoản, xe, tài xế, lịch chạy GL-19, báo cáo) và các lớp hiện có sẽ nhận thêm trách nhiệm khi chạy lại P08.
- AC-C-PayTicketOnlineController ở trạng thái Tạm (chờ P07 của UC-003); chạy lại P08 khi có P07 của UC-003 để chuyển sang Hoạt động. AC-B-PaymentGateway cần trách nhiệm thanh toán từ P07 của UC-003.
- F6 không đạt ở AC-E-Ticket (trách nhiệm gắn kết): 17 trách nhiệm gom phát hành, trả vé, huỷ theo chuyến, lập SMS, soát vé. Đề xuất P10 cân nhắc tách trách nhiệm lập nội dung SMS và trách nhiệm trả vé ra phần tử thiết kế riêng khi lớp thiết kế được xác định; ở mức phân tích giữ một khái niệm Vé (GL-37).
- F6 không đạt ở AC-E-Seat (yêu cầu đặc thù): trạng thái chỗ lưu hay suy ra, hành động là Q-75.
- Target 9 đạt một phần: chỉ có thể kiểm tra bố cục theo bảng và theo kiểm tra tự động toạ độ (khoảng cách tối thiểu 40, toạ độ bội số 10, cạnh trực giao không cắt node); chưa mở bằng draw.io nên nhãn multiplicity ở khe hẹp giữa hai node cùng hàng (60) có thể chồng lên nhau, cần chỉnh tay.
- Hai boundary AC-B-ReturnTicketForm và AC-B-CounterReturnTicketForm có 11 trách nhiệm trùng tên. Quy tắc mặc định (mỗi cặp tác nhân - use case một boundary) được giữ; nếu tổ chức muốn một boundary chung cho hai tác nhân, ghi vào YEU_CAU_BO_SUNG và chạy lại. P07 UC-008 đã đề xuất xem xét tác nhân cha tổng quát hoá ACT-01, ACT-02 ở P01.
- AC-E-TripPassengerList chưa có thuộc tính và R-34 thiếu multiplicity phía TripPassengerList (Q-73). AC-E-PhoneReservation chỉ có thuộc tính status (P07 của UC-004, UC-006 sẽ bổ sung). AC-E-Route, AC-E-BaseFare, AC-E-HolidaySurcharge, AC-E-Refund mỗi lớp chỉ có một trách nhiệm hành vi (hợp lệ theo Target 8, nhưng nên rà lại khi UC-001, UC-016, UC-017 được phân tích).
- Multiplicity còn trống: R-25 (phía HolidaySurcharge, Q-20), R-30 (phía Ticket, Q-36), R-34 (phía TripPassengerList, Q-73), R-36 (phía TicketCheckSession, Q-77), R-37 (phía Seat, Q-76).
- Chọn giữa hai quy tắc (C9): F2 yêu cầu mọi lớp của mọi P07 xuất hiện đúng một lần ở cột Lớp gốc, còn F3 yêu cầu mỗi lớp một dòng; lớp tái dùng ở nhiều use case có một dòng ở F2 cho mỗi file P07 (37 dòng) và một dòng ở F3 (24 dòng).
- Chọn giữa hai quy tắc (C9): F5 yêu cầu trang tổng thể là trang Entity và boundary, control chỉ vẽ ở trang theo nhóm chức năng; PaymentGateway và SmsGateway thuộc cả hai nhóm Bán vé và Vận hành chuyến nên xuất hiện ở cả hai trang (ID có hậu tố __V2, __V3), cùng với Trip, Route, Ticket, Seat, Refund.
- Chọn giữa hai quy tắc (C9): C7.3 chỉ định bảng Node của C7.1 gồm cột Thuộc về (container), còn F5 yêu cầu cột Thuộc về (view); đã dùng tên trang làm giá trị cột này.
