# P11a - screen-list - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 1) |
| Phiên bản | 1.1 (giai đoạn 1 phiên bản 1.0; thêm bảng tổng hợp F7 ở giai đoạn 2) |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P01-actors.md (Mục 2); P02-usecases.md (Mục 4); P04-uc-specs/UC-009-book-ticket-online.md và UC-017-cancel-trip.md (luồng sự kiện, bảng dữ liệu vào ra, thông điệp); P05-glossary.md; P06-supplementary-spec.md; P07-uc-analysis/UC-009 và UC-017 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng boundary giao diện người dùng); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4); P11a-gui/ui-standards.md (phiên bản 1.0, UI-STT 7, 8, 11, 34, F1b). Placeholder: CHE_DO_CHAY = Giai đoạn 1; XUAT_HTML = Không; THONG_TIN_TAI_LIEU = Không có; YEU_CAU_BO_SUNG = phạm vi UC-009, UC-017 và màn hình điều hướng cần thiết. Q, ASM lớn nhất quét trước lần chạy: Q-65, ASM-48 |
| Phạm vi | UC-009, UC-017 và hai màn hình điều hướng của ACT-01, ACT-03 |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 (giai đoạn 2 cấp Q-70 đến Q-72, ASM-52 đến ASM-54, ghi ở SCR-03 và SCR-06) |

## Boundary cần màn hình (nguồn: P10 F3, F4)

Layer của PKG tra ở P10 F4, cột Layer (PKG-01 là layer Presentation theo P09 F4).

| AC | Phần tử thiết kế (P10 F3) | PKG | Layer (P10 F4) | Kết luận |
|---|---|---|---|---|
| AC-B-BookTicketOnlineForm | DC-BookTicketOnlineView, DC-BookTicketOnlineRequestHandler | PKG-05 PassengerWeb | PKG-01 Presentation | Cần màn hình: SCR-02, SCR-03, SCR-04 |
| AC-B-CancelTripForm | DC-CancelTripView, DC-CancelTripRequestHandler | PKG-07 DispatchWeb | PKG-01 Presentation | Cần màn hình: SCR-06, SCR-07, SCR-08 |
| AC-B-SmsGateway | SS-02 SmsNotification (IF-02) | PKG-22 SmsIntegration | PKG-03 Services | Không cần màn hình (bảng phụ) |
| AC-B-PaymentGateway | SS-01 OnlinePayment (IF-01) | PKG-21 PaymentIntegration | PKG-03 Services | Không cần màn hình (bảng phụ) |

DC-HoldExpiryTrigger (PKG-11 TimerTrigger) cũng thuộc layer Presentation nhưng là bộ định thời của ACT-09, không phải boundary giao diện người dùng nên không có màn hình.

## Danh sách màn hình

| SCR | Tên | Boundary AC nguồn | UC | Tác nhân | Loại | Lớp thiết kế (DC) | Mục đích | Bước UC phục vụ |
|---|---|---|---|---|---|---|---|---|
| SCR-01 | Trang chủ hành khách (Passenger home) | Điều hướng: mở UC-001, UC-003, UC-008, UC-009, UC-011, UC-012, UC-014 | UC-001, UC-003, UC-008, UC-009, UC-011, UC-012, UC-014 | ACT-01 Hành khách | Độc lập | Chưa có (điều hướng) | Chọn use case của hành khách; lối vào mua vé (UC-009); nơi hiển thị MSG-01 và MSG-09 | UC-009 bước 1, 2a, *a |
| SCR-02 | Chọn chỗ (Select seats) | AC-B-BookTicketOnlineForm | UC-009 | ACT-01 Hành khách | Phụ thuộc có dữ liệu | DC-BookTicketOnlineView | Xem sơ đồ chỗ của chuyến đã chọn, chọn từ 1 đến 5 chỗ trống để giữ chỗ, hoặc huỷ yêu cầu mua vé | UC-009 bước 3, 4, 4a, 4b, 4c, *a |
| SCR-03 | Nhập thông tin người đi (Enter traveler info) | AC-B-BookTicketOnlineForm | UC-009 | ACT-01 Hành khách | Phụ thuộc có dữ liệu | DC-BookTicketOnlineView | Xem các chỗ đang giữ và thời hạn giữ chỗ, nhập họ tên và số điện thoại người đi, chuyển sang thanh toán hoặc huỷ yêu cầu | UC-009 bước 5, 6, 7, 7a, 5a, 8a, *a |
| SCR-04 | Vé đã phát hành (Issued tickets) | AC-B-BookTicketOnlineForm | UC-009 | ACT-01 Hành khách | Phụ thuộc có dữ liệu | DC-BookTicketOnlineView | Xem mã vé, chuyến, chỗ, họ tên người đi, giá vé và tổng tiền của các vé đã phát hành | UC-009 bước 12 (kết quả của bước 9 đến 11) |
| SCR-05 | Trang chủ điều hành (Dispatcher home) | Điều hướng: mở UC-016, UC-017, UC-019, UC-020, UC-021, UC-022 | UC-016, UC-017, UC-019, UC-020, UC-021, UC-022 | ACT-03 Nhân viên điều hành | Độc lập | Chưa có (điều hướng) | Chọn use case của nhân viên điều hành; lối vào huỷ chuyến (UC-017); nơi hiển thị MSG-12 | UC-017 bước 1, *a |
| SCR-06 | Chọn chuyến cần huỷ (Select trip to cancel) | AC-B-CancelTripForm | UC-017 | ACT-03 Nhân viên điều hành | Độc lập | DC-CancelTripView | Xem các chuyến trong lịch chạy, chọn chuyến cần huỷ và lý do huỷ, hoặc bỏ yêu cầu | UC-017 bước 2, 3, 4a, 4b, *a |
| SCR-07 | Xác nhận huỷ chuyến (Confirm trip cancellation) | AC-B-CancelTripForm | UC-017 | ACT-03 Nhân viên điều hành | Con phụ thuộc | DC-CancelTripView | Xem lại chuyến và lý do, xác nhận thao tác huỷ không hoàn tác trước khi hệ thống kiểm tra và xử lý | UC-017 bước 3 (gửi chuyến và lý do), 4 |
| SCR-08 | Kết quả huỷ chuyến (Trip cancellation result) | AC-B-CancelTripForm | UC-017 | ACT-03 Nhân viên điều hành | Phụ thuộc có dữ liệu | DC-CancelTripView | Xem kết quả huỷ chuyến: số vé đã huỷ, số điện thoại đã báo và chưa báo được, vé hoàn tiền, vé chờ hoàn tiền mặt | UC-017 bước 14 (kết quả của bước 5 đến 13) |

SCR-01 và SCR-05 là hai màn hình điều hướng duy nhất của lần chạy; ACT-02, ACT-04, ACT-05 chưa có màn hình vì chưa có use case của họ trong phạm vi.

## Boundary không có màn hình

| AC | Loại boundary | Ánh xạ ở P10 (SS, DC) | Lý do |
|---|---|---|---|
| AC-B-SmsGateway | Giao diện hệ thống (kênh thông báo SMS) | SS-02 SmsNotification, IF-02 ISmsGateway, PKG-22 | Kênh thông báo đi qua Cổng SMS (ACT-07), không có người dùng thao tác; kết quả gửi SMS hiển thị qua màn hình của use case gọi nó (SCR-04, SCR-08) |
| AC-B-PaymentGateway | Giao diện hệ thống | SS-01 OnlinePayment, IF-01 IPaymentGateway, PKG-21 | Giao tiếp với Cổng thanh toán (ACT-06) bằng API; trang thanh toán thuộc UC-010 chưa có đặc tả |

## Phân bổ trách nhiệm boundary

| AC | Trách nhiệm (P08 F3) | Màn hình hoặc thông điệp |
|---|---|---|
| AC-B-BookTicketOnlineForm | requestBookTicket | Lối vào "Mua vé" ở SCR-01 |
| AC-B-BookTicketOnlineForm | selectSeats | SCR-02 |
| AC-B-BookTicketOnlineForm | enterTravelerInfo | SCR-03 |
| AC-B-BookTicketOnlineForm | cancelBooking | Nút "Huỷ yêu cầu mua vé" ở SCR-02, SCR-03 |
| AC-B-BookTicketOnlineForm | notifyNoTripSelected | MSG-01 (banner tại SCR-01) |
| AC-B-BookTicketOnlineForm | notifySeatsUnavailable | MSG-02 (hộp modal từ SCR-02) |
| AC-B-BookTicketOnlineForm | notifySeatLimitExceeded | MSG-03 (banner tại SCR-02) |
| AC-B-BookTicketOnlineForm | notifyTripDeparted | MSG-04 (hộp modal từ SCR-02) |
| AC-B-BookTicketOnlineForm | notifyTravelerInfoMissing | MSG-05, MSG-06 (lỗi tại trường, SCR-03) |
| AC-B-BookTicketOnlineForm | notifyPaymentFailed | MSG-07 (hộp modal, sau SCR-03) |
| AC-B-BookTicketOnlineForm | notifyHoldExpired | MSG-08 (hộp modal, SCR-03) |
| AC-B-BookTicketOnlineForm | notifyBookingCancelled | MSG-09 (banner tại SCR-01) |
| AC-B-BookTicketOnlineForm | showIssuedTickets | SCR-04 |
| AC-B-CancelTripForm | requestCancelTrip | Lối vào "Huỷ chuyến" ở SCR-05 |
| AC-B-CancelTripForm | showScheduledTrips | SCR-06 |
| AC-B-CancelTripForm | selectTripAndReason | SCR-06 (chọn), SCR-07 (xác nhận gửi) |
| AC-B-CancelTripForm | notifyTripAlreadyCancelled | MSG-10 (banner tại SCR-06) |
| AC-B-CancelTripForm | notifyTripDeparted | MSG-11 (banner tại SCR-06) |
| AC-B-CancelTripForm | abortCancelTrip | Nút "Bỏ yêu cầu huỷ chuyến" ở SCR-06 |
| AC-B-CancelTripForm | notifyCancelTripAborted | MSG-12 (banner tại SCR-05) |
| AC-B-CancelTripForm | showCancellationResult | SCR-08 |

## Bảng tổng hợp đánh giá chuẩn (F7)

Tổng hợp từ mục g) của SCR-02, SCR-03, SCR-04, SCR-06, SCR-07, SCR-08 (giai đoạn 2, lần chạy cuối) và Shneiderman toàn bộ sáu màn hình. Màn hình điều hướng SCR-01 và SCR-05 chưa có đặc tả nên chưa đánh giá. Có 7 dòng Vi phạm còn mở và 2 dòng Vi phạm đã sửa ở mức màn hình; đánh giá chuẩn hoá của giai đoạn 1 nằm ở cuối ui-standards.md.

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-02 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Vùng "Đã chọn" cập nhật ngay khi chọn; MSG-13 sau 1 giây khi kiểm tra và giữ chỗ | - |
| SCR-02 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Có "Huỷ yêu cầu mua vé" và mục "Trang chủ"; không có nút "Quay lại" vì SCR-02 là bước đầu sau UC-008 và đặc tả không có dịch chuyển lùi | - |
| SCR-02 | Nielsen 5 Ngăn lỗi | Đạt | Nút "Tiếp tục" vô hiệu khi chưa chọn chỗ; gợi ý "Chọn tối đa 5 chỗ"; chỗ không chọn được không bấm được | Giao diện không chặn chọn chỗ thứ 6 để luồng 4b còn đến được; hệ thống chặn bằng MSG-03 |
| SCR-02 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | MSG-02, MSG-03, MSG-04 nêu điều sai và việc cần làm; MSG-03 giữ các chỗ đã chọn | - |
| SCR-02 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Ba trạng thái chỗ khác nhau bằng viền, biểu tượng (dấu tick, gạch chéo) và chú giải chữ | - |
| SCR-02 | WCAG 1.4.11 Tương phản thành phần | Đạt | Viền chỗ trống #1F4E8C 2 px trên trắng 8,31:1; viền chỗ không chọn được #6B7280 trên nền ô #D5DAE0 là 3,44:1; chữ mã chỗ #52606D trên #D5DAE0 là 4,59:1 | - |
| SCR-02 | WCAG 2.1.1 Bàn phím | Đạt | Lưới chỗ một điểm dừng Tab, mũi tên di chuyển, Space chọn (UI-STT 41) | - |
| SCR-02 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Ô chỗ 44 x 44 px, khoảng cách 8 px | - |
| SCR-02 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | "Đã chọn" và MSG-03 khai báo role; MSG-02, MSG-04, MSG-14 là hộp modal giữ tiêu điểm | - |
| SCR-02 | Baymard: giữ nguyên dữ liệu đã nhập khi báo lỗi | Đạt | MSG-03 và MSG-14 giữ nguyên các chỗ đã chọn | - |
| SCR-02 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 1 đến 17, 18, 19, 27, 32, 34 đến 37, 39, 40, 43 đến 45, 47 đến 49, 53, 57 đến 64 | - |
| SCR-03 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Thời hạn giữ chỗ và thời gian còn lại luôn hiển thị; MSG-13 khi xử lý thanh toán | - |
| SCR-03 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Có "Huỷ yêu cầu mua vé" và mục "Trang chủ" trả chỗ ngay; không có nút "Quay lại" SCR-02 vì đặc tả không có dịch chuyển lùi từ bước 6 | - |
| SCR-03 | Nielsen 5 Ngăn lỗi | Vi phạm còn mở | Mục "Trang chủ" và "Huỷ yêu cầu mua vé" trả chỗ ngay không qua xác nhận, hành khách bấm nhầm sẽ mất chỗ đã giữ | Q-71; chưa thêm hộp xác nhận vì đặc tả không có |
| SCR-03 | Nielsen 6 Nhận biết thay vì nhớ lại | Vi phạm còn mở | Tóm tắt có tuyến, giờ xuất bến, chỗ nhưng không có giá vé và tổng tiền vì P04 chưa có dữ liệu này trước bước 12 | Q-70 |
| SCR-03 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | MSG-05, MSG-06 ngay dưới ô, nói rõ việc cần làm; MSG-15 nêu số trường cần sửa | - |
| SCR-03 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Lỗi có biểu tượng và tiền tố "Lỗi:"; trường bắt buộc ghi "(bắt buộc)" bằng chữ | - |
| SCR-03 | WCAG 2.2.1 Điều chỉnh thời gian | Đạt | Thời hạn 10 phút do BR-03 quy định nên không cho kéo dài (ngoại lệ thiết yếu); thời gian còn lại hiển thị, trình đọc màn hình được báo ở ba mốc (MSG-16) | - |
| SCR-03 | WCAG 3.3.1 Nhận biết lỗi | Đạt | Lỗi hiện bằng chữ cạnh ô, gắn aria-describedby, kèm banner MSG-15 khi có từ hai lỗi | - |
| SCR-03 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhãn luôn hiển thị, gắn for; gợi ý ví dụ nằm dưới nhãn, không dùng placeholder thay nhãn | - |
| SCR-03 | WCAG 3.3.4 Ngăn lỗi với dữ liệu tài chính | Vi phạm còn mở | Hành khách sang bước thanh toán mà chưa thấy tổng tiền trên màn hình này | Q-70; tổng tiền được xác nhận ở màn hình thanh toán của UC-010 |
| SCR-03 | WCAG 3.3.7 Không bắt nhập lại | Đạt | Họ tên và số điện thoại chỉ nhập một lần cho cả lần đặt (ASM-19); MSG-14 giữ dữ liệu | - |
| SCR-03 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Mốc còn 5 phút, 1 phút, 30 giây thông báo bằng role status; MSG-15 và lỗi trường khai báo role alert | - |
| SCR-03 | Baymard: form một cột, nhãn trên ô, đánh dấu bắt buộc | Đạt | Hai ô một cột, nhãn trên ô, ghi "(bắt buộc)" | - |
| SCR-03 | Baymard: giảm số trường tới mức đặc tả yêu cầu | Đạt | Chỉ có hai ô của Dữ liệu vào 2; không có tài khoản, không có trường thẻ | - |
| SCR-03 | Baymard: hiển thị tóm tắt đơn và tổng tiền | Vi phạm còn mở | Chỉ có tóm tắt chuyến và chỗ, chưa có giá vé và tổng tiền | Q-70 |
| SCR-03 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 1 đến 17, 18, 19, 22, 27 đến 33, 34 đến 37, 39, 40, 43 đến 45, 47 đến 55, 57 đến 64, 69 | - |
| SCR-04 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Tiêu đề "Vé đã phát hành" và bảng mã vé cho hành khách biết kết quả | - |
| SCR-04 | Nielsen 2 Khớp giữa hệ thống và thế giới thực | Đạt | Dùng "vé", "mã vé", "chỗ", "người đi" theo glossary; tiền ghi "250.000 đ" | - |
| SCR-04 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | Khi SMS mã vé không gửi được (luồng 11a), màn hình không báo cho hành khách nên hành khách có thể chờ SMS không bao giờ đến | Q-67; chưa thêm dòng thông tin vì đặc tả không nêu |
| SCR-04 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Bảng vé dùng th có scope; dòng tổng tiền có nhãn "Tổng tiền" | - |
| SCR-04 | WCAG 3.2.4 Định danh nhất quán | Đạt | Nút "Về trang chủ" cùng nhãn và cùng đích với mục "Trang chủ" | - |
| SCR-04 | WCAG 1.4.10 Reflow | Đạt | Bảng chuyển thành thẻ dưới 600 px (UI-STT 25) | - |
| SCR-04 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 1 đến 17, 18, 27, 32, 33 đến 37, 45, 47, 49, 53, 57 đến 64 | - |
| SCR-06 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Cột "Trạng thái" cho biết chuyến Chưa huỷ hay Đã huỷ ngay trên danh sách | - |
| SCR-06 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | "Bỏ yêu cầu huỷ chuyến" và "Trang chủ" thoát không thay đổi dữ liệu; xác nhận ở SCR-07 có "Không huỷ" | - |
| SCR-06 | Nielsen 5 Ngăn lỗi | Đạt | Nút "Tiếp tục huỷ chuyến" vô hiệu tới khi chọn đủ chuyến và lý do; lý do không chọn sẵn; thao tác huỷ phải qua SCR-07 | Chuyến đã huỷ hoặc đã xuất bến vẫn chọn được vì luồng 4a, 4b của đặc tả |
| SCR-06 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mỗi dòng hiển thị đủ tuyến, giờ, xe, tài xế, trạng thái để nhận biết chuyến | - |
| SCR-06 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Khoảng 80 chuyến mỗi ngày (nguồn mục mở đầu) nên lịch chạy một tuần có hàng trăm dòng, chỉ có phân trang 20 dòng, không có lọc theo ngày hoặc tuyến | Q-72; chưa thêm bộ lọc vì đặc tả không có |
| SCR-06 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | MSG-10, MSG-11 nêu chuyến nào, vì sao không huỷ được và việc cần làm; làm mới danh sách | - |
| SCR-06 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Bảng dùng th có scope; nhóm lý do dùng fieldset và legend | - |
| SCR-06 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Trạng thái "Đã huỷ" có chữ và biểu tượng; dòng được chọn có nút chọn đánh dấu | - |
| SCR-06 | WCAG 1.4.10 Reflow | Đạt | Bảng chuyển thành thẻ dưới 600 px, kể cả khi phóng to 400% trên máy tính bàn | - |
| SCR-06 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Thứ tự Tab: thanh trên, banner, bảng, nhóm lý do, nút hành động (UI-STT 32) | - |
| SCR-06 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhóm lý do có nhãn "(bắt buộc)"; mỗi nút chọn có nhãn đọc được | - |
| SCR-06 | WCAG 3.3.7 Không bắt nhập lại | Đạt | MSG-10, MSG-11, MSG-14 giữ nguyên lý do đã chọn | - |
| SCR-06 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 2, 4 đến 17, 18, 19, 23, 27, 28, 32 đến 37, 39, 40, 43 đến 45, 47 đến 55, 57 đến 64 | - |
| SCR-07 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | MSG-13 khi xử lý; không đóng hộp cho tới khi có kết quả | - |
| SCR-07 | Nielsen 2 Khớp giữa hệ thống và thế giới thực | Đạt | Nhãn nút đặt theo hành động: "Xác nhận huỷ chuyến", "Không huỷ" | - |
| SCR-07 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | "Không huỷ" và Esc đóng hộp không thay đổi dữ liệu | - |
| SCR-07 | Nielsen 4 Nhất quán và theo chuẩn | Vi phạm đã sửa | Bản đầu cho MSG-14 hiện chồng lên hộp xác nhận (hai hộp modal lồng nhau) | Đóng SCR-07 trước, hiển thị MSG-14 tại SCR-06 (chức năng 4) |
| SCR-07 | Nielsen 5 Ngăn lỗi | Đạt | Thao tác không hoàn tác có hộp xác nhận riêng nêu lại chuyến, lý do, hệ quả; tiêu điểm đầu ở nút an toàn; Enter không kích hoạt nút nguy hiểm | - |
| SCR-07 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Tiêu đề hộp có biểu tượng và tiền tố "Cảnh báo:"; nút nguy hiểm khác nút phụ bằng nhãn | - |
| SCR-07 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ trắng trên #B3261E 6,54:1; cảnh báo #7A4A00 trên #FFF4D6 6,83:1 | - |
| SCR-07 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Tiêu điểm vào "Không huỷ", giữ trong hộp, trả về nút "Tiếp tục huỷ chuyến" khi đóng | - |
| SCR-07 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Việc huỷ gây hoàn tiền phải xác nhận trước khi gửi, hệ quả nêu bằng chữ | - |
| SCR-07 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Hộp khai báo role alertdialog; MSG-13 khai báo role status | - |
| SCR-07 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 2, 4 đến 17, 18, 19, 20, 27, 32, 33, 39, 40, 43 đến 45, 47, 53, 57 đến 68 | - |
| SCR-08 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Màn hình kết quả nêu đủ bảy dữ liệu ra: số vé huỷ, SMS đã và chưa báo, hoàn tiền đã và chưa được, vé chờ hoàn tiền mặt | - |
| SCR-08 | Nielsen 4 Nhất quán và theo chuẩn | Đạt | Cùng bố cục mục chi tiết chỉ đọc (nhãn trên hoặc trái, giá trị đậm) và nút "Về trang chủ" như SCR-04 | - |
| SCR-08 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | Khi có số điện thoại chưa báo được hoặc vé chưa hoàn được, màn hình nêu danh sách nhưng không nêu cách xử lý tiếp vì cơ chế xử lý lại chưa quy định | Q-49, Q-50 (P04 UC-017) |
| SCR-08 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Vi phạm đã sửa | Bản đầu chỉ tô nền vàng cho dòng "Số điện thoại chưa báo được" và "Vé chưa hoàn được" khi có giá trị | Thêm biểu tượng và tiền tố chữ "Cảnh báo:" (UI-STT 17) |
| SCR-08 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ cảnh báo #7A4A00 trên #FFF4D6 6,83:1 | - |
| SCR-08 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Mỗi nhóm kết quả là danh sách mô tả (dt, dd) có tiêu đề nhóm cấp dưới không nhảy cấp | - |
| SCR-08 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Vùng kết quả khai báo role status để trình đọc màn hình đọc kết quả khi mở màn hình, tiêu điểm vẫn ở tiêu đề | - |
| SCR-08 | Các tiêu chí còn lại | Đạt | Đạt theo ui-standards.md STT 2, 4 đến 17, 18, 27, 32 đến 37, 45, 47, 49, 53, 57 đến 64 | - |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: nhất quán | Đạt | Cả sáu màn hình dùng chung bố cục vùng, vị trí nút (nút chính bên phải, nút phụ bên trái), thanh trên và nhãn nút theo UI-STT 7, 8, 10, 34 | - |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: khả dụng cho mọi người dùng | Đạt | Hành khách không cần tài khoản (NFR-02); hai nhóm thiết bị theo UI-STT 1, 2; tương phản và bàn phím theo UI-STT 57 đến 64 | - |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: phản hồi đầy đủ | Đạt | SCR-02, SCR-03, SCR-07 có MSG-13 khi xử lý; mọi lỗi nghiệp vụ có MSG; SCR-04 và SCR-08 là màn hình kết quả | - |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: hội thoại có điểm kết thúc rõ | Đạt | UC-009 kết thúc ở SCR-04 hoặc hộp MSG-04, MSG-07, MSG-08 và về SCR-01; UC-017 kết thúc ở SCR-08 hoặc MSG-12 và về SCR-05 | - |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: ngăn lỗi | Đạt | Nút chính vô hiệu khi thiếu lựa chọn bắt buộc (SCR-02, SCR-06); xác nhận riêng cho huỷ chuyến (SCR-07) | SCR-03 còn thiếu xác nhận khi rời bằng menu (Q-71) |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: hoàn tác dễ dàng | Đạt | Không có chức năng hoàn tác trong đặc tả (UI-STT 68); lối thoát trước khi gửi: SCR-02, SCR-03 (Huỷ yêu cầu mua vé), SCR-06, SCR-07 (Không huỷ) | Không thêm chức năng |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: người dùng làm chủ | Đạt | Mọi thao tác do người dùng khởi phát; Esc và nút thoát ở màn hình có lối thoát | - |
| Tất cả (SCR-02, 03, 04, 06, 07, 08) | Shneiderman: giảm tải trí nhớ ngắn hạn | Vi phạm còn mở | SCR-03 không hiển thị giá vé và tổng tiền ở bước ngay trước thanh toán (Q-70); các màn hình khác hiển thị đủ chuyến và chỗ | Q-70 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-67 | Khi SMS mã vé không gửi được (UC-009 luồng 11a), màn hình vé đã phát hành có báo cho hành khách biết SMS chưa gửi được để họ tự ghi lại mã vé không? (Không báo, chỉ hiển thị mã vé như bước 12 / Có báo bằng một dòng thông tin trên SCR-04) | SCR-04; UC-009 luồng 11a, bước 12; ASM-20; Nielsen #1, #9 | UC-009 bước 12 và luồng 11a: "mã vé vẫn được hiển thị cho hành khách ở bước 12 (ASM-20)" không nêu có báo việc SMS thất bại cho hành khách hay không; P07 UC-009 không có trách nhiệm thông báo cho việc này |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | - |

ASM-49 (kèm Q-66) và ASM-50 của lần chạy này ghi ở screen-transition.md.

Q-70, Q-71 và ASM-52, ASM-53 của giai đoạn 2 ghi ở SCR-03-enter-traveler-info.md; Q-72 và ASM-54 ghi ở SCR-06-select-trip-to-cancel.md.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3, F4 (PKG-05 PassengerWeb) | SCR-01 là màn hình điều hướng của ACT-01, chưa có phần tử View điều hướng trong package giao diện của tác nhân | Thêm phần tử View điều hướng (ví dụ DC-PassengerHomeView) vào PKG-05 khi chạy lại P10 |
| P10 | F3, F4 (PKG-07 DispatchWeb) | SCR-05 là màn hình điều hướng của ACT-03, chưa có phần tử View điều hướng trong package giao diện của tác nhân | Thêm phần tử View điều hướng (ví dụ DC-DispatchHomeView) vào PKG-07 khi chạy lại P10 |

## Vấn đề còn mở

- Ba màn hình của UC-009 cùng ánh xạ về DC-BookTicketOnlineView và ba màn hình của UC-017 cùng ánh xạ về DC-CancelTripView, vì P10 chỉ có một View mỗi boundary; P12 quyết định tách View theo màn hình hay dùng một View nhiều mẫu giao diện.
- UC-008 Tra cứu chuyến xe và UC-010 Thanh toán vé trực tuyến chưa có đặc tả P04, P07 nên chưa có màn hình tìm chuyến và màn hình thanh toán; cách nối qua hai use case này ghi ở ASM-49 và Q-66 (screen-transition.md).
- Mức hợp lý: mỗi use case 3 màn hình (trong khoảng 1 đến 5); mỗi boundary giao diện người dùng ở layer Presentation có ít nhất một màn hình.
- Mục Phân bổ trách nhiệm boundary và bảng Boundary cần màn hình là phần bổ sung ngoài khung F2 để đối chiếu Target 2 và Target 4.
