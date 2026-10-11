# P11a - screen-list - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 1) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P01-actors.md (Mục 2); P02-usecases.md (Mục 4); P04-uc-specs/UC-009-book-ticket-online.md và UC-017-cancel-trip.md (luồng sự kiện, bảng dữ liệu vào ra, thông điệp); P05-glossary.md; P06-supplementary-spec.md; P07-uc-analysis/UC-009 và UC-017 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng boundary giao diện người dùng); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4); P11a-gui/ui-standards.md (phiên bản 1.0, UI-STT 7, 8, 11, 34, F1b). Placeholder: CHE_DO_CHAY = Giai đoạn 1; XUAT_HTML = Không; THONG_TIN_TAI_LIEU = Không có; YEU_CAU_BO_SUNG = phạm vi UC-009, UC-017 và màn hình điều hướng cần thiết. Q, ASM lớn nhất quét trước lần chạy: Q-65, ASM-48 |
| Phạm vi | UC-009, UC-017 và hai màn hình điều hướng của ACT-01, ACT-03 |
| Mã Q, ASM cuối đã cấp | Q-68, ASM-50 |

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

Chưa lập. Bảng này được lập ở lần chạy giai đoạn 2 cuối cùng từ mục g của các SCR; đánh giá chuẩn hoá của giai đoạn 1 nằm ở cuối ui-standards.md.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-67 | Khi SMS mã vé không gửi được (UC-009 luồng 11a), màn hình vé đã phát hành có báo cho hành khách biết SMS chưa gửi được để họ tự ghi lại mã vé không? (Không báo, chỉ hiển thị mã vé như bước 12 / Có báo bằng một dòng thông tin trên SCR-04) | SCR-04; UC-009 luồng 11a, bước 12; ASM-20; Nielsen #1, #9 | UC-009 bước 12 và luồng 11a: "mã vé vẫn được hiển thị cho hành khách ở bước 12 (ASM-20)" không nêu có báo việc SMS thất bại cho hành khách hay không; P07 UC-009 không có trách nhiệm thông báo cho việc này |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | - |

ASM-49 (kèm Q-66) và ASM-50 của lần chạy này ghi ở screen-transition.md.

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
