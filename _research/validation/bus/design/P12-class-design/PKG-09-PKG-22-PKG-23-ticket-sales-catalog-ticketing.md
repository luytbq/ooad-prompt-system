# P12 - Thiết kế lớp - PKG-09 TicketSalesService, PKG-22 TripCatalog, PKG-23 Ticketing - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P12 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (CONG_NGHE đã chốt theo P09: Java 17, Spring Boot, PostgreSQL; CHE_DO_GIA_DINH = CO_NHAN; MUC_CHI_TIET = DAY_DU); 00-Conventions.md (bản hiện có); P10-design-elements.md 1.0; P08-analysis-model.md 1.0; P07-uc-analysis/UC-002, UC-008, UC-013, UC-015 (1.0); P09-architecture.md 1.0; P11b-system-interfaces.md 1.0 (SS-01, SS-02, SS-04, SS-05, SS-07: IF-01, IF-02, IF-03, IF-06, IF-07, IF-08, IF-10, IF-11); P11a-gui/screen-list.md 1.0 (không có SCR thuộc phạm vi vì phạm vi không chứa lớp boundary); P04-uc-specs/UC-002, UC-008, UC-013, UC-015 (1.0); P06-supplementary-spec.md 1.0; P05-glossary.md 1.0. Chưa có file P12 nào khác. Tham số: PHAM_VI_THIET_KE = PKG-09 TicketSalesService, PKG-22 TripCatalog, PKG-23 Ticketing; QUY_UOC_KIEU_DU_LIEU = Không có; MAU_THIET_KE_DA_CHOT = Không có; YEU_CAU_BO_SUNG = Không có |
| Phạm vi | PKG-09 TicketSalesService, PKG-22 TripCatalog, PKG-23 Ticketing: dịch vụ ứng dụng của UC-002, UC-003 (tạm), UC-008 và các lớp miền, interface kho dữ liệu của chúng. Các package khác (PKG-05 đến PKG-08, PKG-10, PKG-11, PKG-14 đến PKG-21, PKG-24, PKG-25, PKG-28) thuộc lần chạy khác hoặc P11b |

Tóm tắt: 45 phần tử thiết kế trong phạm vi (9 ở PKG-09, 12 ở PKG-22, 24 ở PKG-23): 3 control, 12 entity (gồm 3 entity phần hành vi không persistent), 3 interface, 12 value object, 12 enumeration, 3 exception; 103 operation, 89 thuộc tính, 50 quan hệ R-02 đến R-67 (P08 giữ mã: R-02 đến R-06, R-09, R-10, R-22 đến R-33, R-37; mới R-38 đến R-67), 3 state machine ST-01 đến ST-03 (Booking, Ticket, Seat), 5 file class diagram (3 theo package, riêng PKG-23 có hai trang, và 2 theo UC) và 3 file state machine. Phạm vi vượt ngưỡng khoảng 15-20 lớp của prompt (18 phần tử từ P10 và P11b, thêm 27 interface, kiểu dữ liệu, enumeration, ngoại lệ do thiết kế) nhưng được chạy một lượt theo tham số của người chạy (Vấn đề còn mở).

Quy ước áp dụng trong file này:

- Kiểu dữ liệu theo Java 17 (CONG_NGHE): String, Integer, Boolean, LocalDate, LocalDateTime, Duration, List<T>, Map<K,V>; Money, TicketCode, PhoneNumber, PaymentReference là kiểu giá trị của PKG-28 (P10 F3); Clock là java.time.Clock. Chữ ký IF-nn lấy nguyên P11b (kiểu trung lập): Date --> LocalDate, DateTime --> LocalDateTime; giá trị enumeration của P11b dạng Succeeded --> SUCCEEDED, HoldExpiry --> HOLD_EXPIRY. Định danh là String, khớp P11b. Operation không trả về ghi ": void". Value object được hiện thực bằng Java record bất biến. Visibility: + public, - private, ~ package-private.
- Thuộc tính có kiểu là value object hoặc enumeration ghi ở F7, không vẽ thành association; association chỉ dùng cho entity, dịch vụ và interface. Phụ thuộc chỉ phát sinh qua kiểu trong chữ ký tới value object, enumeration, exception không liệt kê ở F5.
- F4 chỉ liệt kê message có lớp nhận hoặc lớp gửi thuộc phạm vi lần chạy. Message trả về gộp vào dòng của message gọi (thành kiểu trả về), trừ khi thiết kế đổi ngữ nghĩa (UC-002 msg 3.1.9 trả về). Message tới lớp boundary (show...) gắn với kết quả trả về hoặc ngoại lệ của dịch vụ, vì boundary thuộc PKG-05, PKG-26, PKG-27 ngoài phạm vi.
- Thời điểm hiện tại: dịch vụ nhận java.time.Clock qua constructor (Bước 2.6) và truyền now, requestTime, checkTime cho entity; entity không gọi đồng hồ hệ thống.

## Kiểm tra đầu vào và danh sách phần tử trong phạm vi

Placeholder: đủ (QUY_UOC_KIEU_DU_LIEU, MAU_THIET_KE_DA_CHOT, YEU_CAU_BO_SUNG là Không có, dùng mặc định). Không còn khối placeholder nào chưa được thay.

| Nguồn (Bước 0) | Phần tử | Ghi chú |
|---|---|---|
| (a) Bảng ánh xạ P10 F3, PKG-09 | DC-BookTicketOnlineService, DC-PayTicketOnlineService, DC-ReturnTicketService | Ánh xạ 1-1 từ control phân tích |
| (a) P10 F3, PKG-22 | DC-Trip, DC-Route, DC-Seat, DC-BaseFare, DC-HolidaySurcharge | DC-Trip còn lại sau khi tách DC-TripCancellation |
| (a) P10 F3, PKG-23 | DC-Booking, DC-Ticket, DC-TicketReturnPolicy, DC-TicketSmsContent, DC-TripCancellation, DC-Refund, DC-PhoneReservation | DC-Ticket tách ba lớp |
| (b) Bảng phần tử mới do cơ chế kiến trúc P10 | IF-10 (PKG-22), IF-11 (PKG-23) | Interface kho dữ liệu |
| (c) Lớp bên trong subsystem do P11b cấp mã (SS-07, F5a) | DC-SeatAlreadyHeldException (PKG-22) | Các lớp khác của SS-07 (DC-TripCatalogRepositoryImpl...) thuộc PKG-14, ngoài phạm vi |
| (d) Interface IF thuộc phạm vi | IF-10, IF-11 | Chữ ký lấy từ P11b F3 |
| Thêm ở P12 (Bước 1.5) | IF-15 và các DC kiểu dữ liệu, enumeration, ngoại lệ ở F1 có Nguồn AC bắt đầu bằng Thiết kế | Có lý do ở F1 |
| Chỉ dùng qua interface, không chi tiết hoá | IF-01, IF-02 (PKG-15), IF-03 (PKG-16), IF-07, IF-08 (PKG-19); các kiểu PKG-15, PKG-16, PKG-19, PKG-28 trong chữ ký | Vẽ tên, ghi ở F5, F9 |

UC có lớp trong phạm vi (cột Dùng trong UC của P08): UC-002, UC-008, UC-013, UC-015; UC-003 qua DC-PayTicketOnlineService (Tạm, ASM-100). Đã đọc P07 của cả bốn UC.

Chữ ký interface tạm: Không có. Mọi interface thuộc phạm vi (IF-10, IF-11) và được dùng (IF-01, IF-02, IF-03, IF-07, IF-08) đã có chữ ký ở P11b F3; IF-15 do P12 cấp mới và có chữ ký đầy đủ ở F2.

Giao ước với package khác (kiểu và operation phạm vi này dùng, do package đó thiết kế; ghi để lần chạy PKG-28, PKG-15, PKG-16, PKG-19 giữ nhất quán):

| Kiểu | Package | Operation hoặc thành phần phạm vi này dùng |
|---|---|---|
| DC-Money | PKG-28 | Money.zero() (classifier); plus(Money): Money; times(Integer): Money; percent(Integer): Money = số tiền x tỉ lệ / 100, làm tròn đến đồng HALF_UP (ASM-102); so sánh bằng theo giá trị |
| DC-PhoneNumber | PKG-28 | PhoneNumber.isValid(String): Boolean (classifier, 10 chữ số bắt đầu bằng 0, ASM-15); PhoneNumber.of(String): PhoneNumber |
| DC-TicketCode, DC-PaymentReference | PKG-28 | Giá trị bất biến, so sánh bằng theo giá trị |
| DC-PersistenceUnavailableException | PKG-28 | Ngoại lệ kỹ thuật tạm thời của IF-10, IF-11, IF-15 (P11b F5a) |
| DC-PaymentRequestResult, DC-RefundResult, DC-PaymentOutcome, DC-PaymentGatewayUnavailableException | PKG-15 | status Accepted / Rejected / Unknown; status Succeeded / Declined / Unknown; outcome Succeeded / Failed |
| DC-SmsResult, DC-SmsGatewayUnavailableException | PKG-16 | status Accepted / Rejected / Unknown |
| DC-TriggerKind, DC-TriggerReference, DC-TriggerStoreUnavailableException | PKG-19 | kind HOLD_EXPIRY; reference.kind, reference.targetId |

## F1. Bảng lớp thiết kế

| DC | Tên | Stereotype | PKG | Trách nhiệm | Nguồn AC | Loại | Persistent | Ghi chú thiết kế |
|---|---|---|---|---|---|---|---|---|
| DC-BookTicketOnlineService | BookTicketOnlineService | «control» | PKG-09 | Điều phối use case UC-002 Đặt vé trực tuyến từ tìm chuyến, giữ chỗ, xử lý hết thời hạn giữ chỗ tới phát hành và gửi vé, là ranh giới giao dịch của các bước đó | AC-C-BookTicketOnlineController | class | Không | Lớp dịch vụ ứng dụng (P09 F5), đổi tên so với control phân tích (P10 F3). Hiện thực IF-08 (R-43). Phụ thuộc đồng hồ java.time.Clock qua constructor để kiểm thử mốc 10 phút. Giữ chờ thanh toán trong Booking và SS-05, không giữ trong bộ nhớ (P09 F7). Một lý do thay đổi: luồng nghiệp vụ UC-002 |
| DC-PayTicketOnlineService | PayTicketOnlineService | «control» | PKG-09 | Gửi yêu cầu thanh toán lần đặt tới cổng thanh toán và chuyển kết quả thanh toán do cổng gọi về cho việc hoàn tất lần đặt | AC-C-PayTicketOnlineController | class | Không | Trạng thái Tạm: P04, P07 của UC-003 chưa có (ASM-100). Hiện thực IF-02 (R-46). Package-private (P10 F5). Phụ thuộc hai chiều với BookTicketOnlineService (R-03, R-47), ghi ở Vấn đề còn mở |
| DC-ReturnTicketService | ReturnTicketService | «control» | PKG-09 | Điều phối use case UC-008 Trả vé từ nhận diện vé, kiểm tra điều kiện, hoàn tiền tới huỷ vé, là ranh giới giao dịch khi huỷ vé và ghi khoản hoàn | AC-C-ReturnTicketController | class | Không | Lớp dịch vụ ứng dụng (P09 F5), dùng chung cho ACT-01 và ACT-02 qua tham số kênh yêu cầu trả (ASM-45). Không giữ trạng thái giữa hai bước nên cancelReturnRequest không có operation (F4) |
| DC-TripOffer | TripOffer | «value object» | PKG-09 | Gói thông tin một chuyến khớp tiêu chí tìm kiếm để hiển thị cho hành khách | Thiết kế: P04 UC-002 Dữ liệu ra 1; giữ PKG-08 không phụ thuộc Trip (P09 F4) | value object | Không | Java record bất biến |
| DC-BookingHold | BookingHold | «value object» | PKG-09 | Gói kết quả giữ chỗ của một lần đặt để hành khách thanh toán | Thiết kế: P07 msg 3.1.7, 3.1.9 trả mã lần đặt, tổng tiền, hạn giữ chỗ, kết quả yêu cầu thanh toán | value object | Không | Java record bất biến |
| DC-ReturnQuote | ReturnQuote | «value object» | PKG-09 | Gói thông tin vé, thời gian còn lại, mức hoàn và số tiền hoàn hiển thị khi xác nhận trả vé | Thiết kế: P04 UC-008 Dữ liệu ra 1 | value object | Không | Java record bất biến |
| DC-ReturnReceipt | ReturnReceipt | «value object» | PKG-09 | Gói kết quả trả vé thành công để thông báo cho tác nhân | Thiết kế: P04 UC-008 Dữ liệu ra 2 | value object | Không | Java record bất biến |
| DC-TicketSalesRuleException | TicketSalesRuleException | «exception» | PKG-09 | Báo luồng thay thế nghiệp vụ của UC-002, UC-008 làm dịch vụ bán vé từ chối yêu cầu, kèm lý do | Thiết kế: luồng thay thế 2a đến 10a của P04 UC-002 và 2a đến 9a của P04 UC-008 | class | Không | Kế thừa RuntimeException. Một ngoại lệ mang mã lý do để PKG-08 chuyển thành mã lỗi và thông điệp MSG của P11a; không dùng cho lỗi kỹ thuật |
| DC-TicketSalesRule | TicketSalesRule | «enumeration» | PKG-09 | Liệt kê lý do dịch vụ bán vé từ chối yêu cầu | Thiết kế: luồng thay thế của P04 UC-002, UC-008 | enumeration | Không | - |
| DC-Trip | Trip | «entity» | PKG-22 | Lưu một lần chạy của một tuyến tại một giờ xuất bến, giữ tập chỗ của chuyến và xác định giá vé, thời gian còn lại, trạng thái huỷ của chuyến | AC-E-Trip | class | Có | Tách từ AC-E-Trip (P10 F3): phần phối hợp huỷ chuyến sang DC-TripCancellation. Không có state machine: chỉ hai trạng thái ACTIVE, CANCELLED và một chuyển (xem Vấn đề còn mở). Tìm chuyến do IF-10 thực hiện |
| DC-Route | Route | «entity» | PKG-22 | Lưu đường chạy cố định nối một điểm đi với một điểm đến | AC-E-Route | class | Có | Lớp dữ liệu: // checkRouteMatches được gộp vào truy vấn IF-10.findTrips, findTrip (xem F4). Không có state machine |
| DC-Seat | Seat | «entity» | PKG-22 | Lưu một vị trí trên xe của một chuyến cùng trạng thái còn trống, đang giữ hoặc đã có vé | AC-E-Seat | class | Có | Có state machine ST-03. Trạng thái lưu thuộc tính (ASM-42), chờ Q-75; Q-69 chưa trả lời nên Trip giữ Seat theo composition |
| DC-BaseFare | BaseFare | «entity» | PKG-22 | Lưu mức giá vé của một cặp tuyến và loại xe và tính giá một vé từ mức giá đó cùng mức tăng giá lễ Tết | AC-E-BaseFare | class | Có | - |
| DC-HolidaySurcharge | HolidaySurcharge | «entity» | PKG-22 | Lưu mức tăng giá theo phần trăm cho một khoảng ngày lễ, Tết và cho biết mức tăng áp dụng cho một ngày xuất bến | AC-E-HolidaySurcharge | class | Có | - |
| DC-TripSchedule | TripSchedule | «value object» | PKG-22 | Gói tên tuyến và giờ xuất bến của một chuyến để hiển thị và lập nội dung tin nhắn | Thiết kế: P07 getRouteAndDepartureTime trả hai giá trị trong một message | value object | Không | Java record bất biến, so sánh bằng theo giá trị hai thành phần; không có operation |
| DC-TripStatus | TripStatus | «enumeration» | PKG-22 | Liệt kê trạng thái của chuyến | Thiết kế: tập giá trị cố định của AC-E-Trip status (GL-04, ASM-26) | enumeration | Không | - |
| DC-SeatStatus | SeatStatus | «enumeration» | PKG-22 | Liệt kê trạng thái của chỗ | Thiết kế: tập giá trị cố định của AC-E-Seat status (ASM-42) | enumeration | Không | - |
| DC-BusType | BusType | «enumeration» | PKG-22 | Liệt kê loại xe của nhà xe | Thiết kế: tập giá trị cố định của AC-E-Trip busType (GL-21, REQ-02) | enumeration | Không | - |
| IF-10 | ITripCatalogRepository | «interface» | PKG-22 | Lưu và truy xuất tuyến, chuyến, chỗ, giá vé; chống trùng chỗ bằng cập nhật có điều kiện | P10 IF-10; P11b SS-07 | interface | Không | Chữ ký lấy nguyên P11b mục F3; hiện thực bởi DC-TripCatalogRepositoryImpl (PKG-14, ngoài phạm vi lần chạy). Tham số route của findTrip là nhãn <Điểm đi> - <Điểm đến> (Đề xuất sửa P11b) |
| DC-SeatAlreadyHeldException | SeatAlreadyHeldException | «exception» | PKG-22 | Báo chỗ đã bị lần đặt khác giữ hoặc đã có vé khi giữ chỗ | P11b SS-07 (F5a, đặt ở PKG-22 cạnh IF-10) | class | Không | Ngoại lệ nghiệp vụ nằm trong chữ ký IF-10.saveTrip; P10 chưa liệt kê (Đề xuất sửa P10). Kế thừa RuntimeException |
| DC-InvalidStateException | InvalidStateException | «exception» | PKG-22 | Báo operation của entity bị gọi khi đối tượng đang ở trạng thái không cho phép | Thiết kế: bộ ngoại lệ chung cho các state machine ST-01 đến ST-03 và quy tắc trạng thái của Trip | class | Không | Đặt ở PKG-22 vì PKG-23 đã phụ thuộc PKG-22 (P09 R8); kế thừa RuntimeException. Lỗi lập trình hoặc vi phạm tiền điều kiện, không phải luồng thay thế của P04 |
| DC-Booking | Booking | «entity» | PKG-23 | Lưu một lần đặt vé trực tuyến, kiểm tra điều kiện đặt, giữ chỗ trong thời hạn giữ chỗ và phát hành vé khi thanh toán thành công | AC-E-Booking | class | Có | Có state machine ST-01. Chỉ lưu từ khi vào HELD (ASM-44). Hằng MAX_SEATS và HOLD_DURATION lấy từ BR-01, BR-07 |
| DC-Ticket | Ticket | «entity» | PKG-23 | Lưu vé của một chỗ trên một chuyến, kiểm soát vòng đời phát hành, soát, huỷ và ghi nhận khoản hoàn của vé | AC-E-Ticket | class | Có | Tách từ AC-E-Ticket (P10 F3): quy tắc trả vé sang DC-TicketReturnPolicy, nội dung SMS sang DC-TicketSmsContent. Có state machine ST-02. findTicket do IF-11 thực hiện (P11b) |
| DC-TicketReturnPolicy | TicketReturnPolicy | «entity» | PKG-23 | Áp dụng quy tắc trả vé và hoàn tiền: kênh trả, thời hạn trả, mức hoàn, hình thức hoàn và số tiền hoàn khi huỷ chuyến | AC-E-Ticket | class | Không | Tách từ AC-E-Ticket (P10 F3), phần hành vi của entity tách ra thành dịch vụ miền không có trạng thái, không persistent; nhận Ticket qua tham số. Hằng ngưỡng lấy từ BR-12 đến BR-14, BR-17 |
| DC-TicketSmsContent | TicketSmsContent | «entity» | PKG-23 | Lập nội dung và khoá chống gửi trùng của tin nhắn SMS gửi vé và báo huỷ chuyến | AC-E-Ticket | class | Không | Tách từ AC-E-Ticket (P10 F3), phần hành vi của entity thành dịch vụ miền không có trạng thái, không persistent; nhận Ticket qua tham số. Nội dung theo ASM-17, ASM-29 |
| DC-TripCancellation | TripCancellation | «entity» | PKG-23 | Phối hợp Trip với các vé còn hiệu lực và đặt chỗ chưa thanh toán của chuyến để tổng hợp và thực hiện việc huỷ chuyến | AC-E-Trip | class | Không | Tách từ AC-E-Trip (P10 F3) để PKG-22 không phụ thuộc PKG-23. Là đơn vị công việc: IF-11.saveTripCancellation ghi chuyến, vé, đặt chỗ đã huỷ trong một giao dịch. Không có thuộc tính; trạng thái nằm ở các association R-58 đến R-61 |
| DC-Refund | Refund | «entity» | PKG-23 | Lưu khoản hoàn tiền của một vé đã huỷ gồm mức hoàn, số tiền hoàn, hình thức hoàn và kết quả hoàn | AC-E-Refund | class | Có | Do Ticket tạo; định danh bằng vé (R-32). Không có state machine: kết quả hoàn do dịch vụ xác định khi tạo, xử lý lại hoàn chưa thành công thuộc use case chưa có |
| DC-PhoneReservation | PhoneReservation | «entity» | PKG-23 | Lưu yêu cầu giữ chỗ trên một chuyến do nhân viên bán vé ghi nhận khi khách gọi điện và cho biết đã thanh toán hay chưa | AC-E-PhoneReservation | class | Có | Chỉ phần UC-013 cần. Chưa có state machine: các chuyển do UC-004, UC-005, UC-006 chưa phân tích (xem Vấn đề còn mở). Q-76: số chỗ của một đặt chỗ chưa trả lời |
| IF-11 | ITicketingRepository | «interface» | PKG-23 | Lưu và truy xuất lần đặt, vé, đặt chỗ qua điện thoại, khoản hoàn và đơn vị huỷ chuyến | P10 IF-11; P11b SS-07 | interface | Không | Chữ ký lấy nguyên P11b mục F3; hiện thực bởi DC-TicketingRepositoryImpl (PKG-14, ngoài phạm vi lần chạy). findTicket với travelerPhone null nghĩa là không lọc theo số điện thoại (vé bán tại quầy, ASM-18; Đề xuất sửa P11b) |
| IF-15 | ITicketingIdGenerator | «interface» | PKG-23 | Cấp mã lần đặt và mã vé duy nhất trên toàn hệ thống | Thiết kế: mã vé duy nhất (BR-10) khi nhiều bản back-end cùng chạy (P09 F1-01); mã IF-15 nối tiếp IF-14 của P11b; Đề xuất sửa P10 | interface | Không | Interface mới do cơ chế thiết kế, đặt ở Domain cạnh nơi dùng (P09 R6); hiện thực bởi SS-07 (dãy số của CSDL). Truyền cho Booking.issueTickets để Booking không gọi bộ sinh toàn cục |
| DC-TravelerInfo | TravelerInfo | «value object» | PKG-23 | Gói chỗ, họ tên và số điện thoại thô của một người đi do hành khách nhập | Thiết kế: AC-E-Booking travelerInfos (ASM-43) | value object | Không | Java record bất biến; số điện thoại giữ dạng chuỗi thô để Booking.validateTravelerInfo báo lỗi thay vì ném khi nhập sai |
| DC-BookingSummary | BookingSummary | «value object» | PKG-23 | Gói các vé đã phát hành và tổng tiền của một lần đặt để hiển thị | Thiết kế: P07 getBookingSummary trả hai giá trị | value object | Không | Java record bất biến |
| DC-TicketCheckResult | TicketCheckResult | «value object» | PKG-23 | Gói kết luận soát một vé cùng dữ liệu cần hiển thị | Thiết kế: P07 determineCheckResult trả nhiều giá trị | value object | Không | Java record bất biến |
| DC-RefundQuote | RefundQuote | «value object» | PKG-23 | Gói mức hoàn và số tiền hoàn tính được khi trả vé | Thiết kế: P07 calculateRefundAmount trả mức hoàn và số tiền hoàn | value object | Không | Java record bất biến |
| DC-TicketReturnInfo | TicketReturnInfo | «value object» | PKG-23 | Gói thông tin vé hiển thị khi yêu cầu trả vé | Thiết kế: P07 getTicketReturnInfo trả nhiều giá trị (P04 UC-008 Dữ liệu ra 1) | value object | Không | Java record bất biến |
| DC-CancelImpactInfo | CancelImpactInfo | «value object» | PKG-23 | Gói kênh mua và số tiền hoàn của một vé còn hiệu lực khi chuyến bị huỷ | Thiết kế: P07 getCancelImpactInfo trả kênh mua và số tiền hoàn | value object | Không | Java record bất biến |
| DC-CancellationSummary | CancellationSummary | «value object» | PKG-23 | Gói số liệu tổng hợp hiển thị trước khi xác nhận huỷ chuyến | Thiết kế: P07 getCancellationSummary trả nhiều giá trị (P04 UC-013 Dữ liệu ra 1) | value object | Không | Java record bất biến |
| DC-BookingStatus | BookingStatus | «enumeration» | PKG-23 | Liệt kê trạng thái của lần đặt | Thiết kế: tập giá trị cố định của AC-E-Booking status (ST-01) | enumeration | Không | - |
| DC-TicketStatus | TicketStatus | «enumeration» | PKG-23 | Liệt kê trạng thái của vé | Thiết kế: tập giá trị cố định của AC-E-Ticket status (GL-37) | enumeration | Không | - |
| DC-PurchaseChannel | PurchaseChannel | «enumeration» | PKG-23 | Liệt kê kênh mua vé | Thiết kế: tập giá trị cố định của AC-E-Ticket purchaseChannel (GL-13) | enumeration | Không | - |
| DC-RefundMethod | RefundMethod | «enumeration» | PKG-23 | Liệt kê hình thức hoàn tiền | Thiết kế: tập giá trị cố định của AC-E-Refund refundMethod (BR-15, BR-16) | enumeration | Không | - |
| DC-RefundOutcome | RefundOutcome | «enumeration» | PKG-23 | Liệt kê kết quả hoàn của khoản hoàn | Thiết kế: tập giá trị cố định của AC-E-Refund refundResult (ASM-54) | enumeration | Không | Khác DC-RefundResult của PKG-15 (kết quả một lời gọi cổng) |
| DC-PhoneReservationStatus | PhoneReservationStatus | «enumeration» | PKG-23 | Liệt kê trạng thái của đặt chỗ qua điện thoại | Thiết kế: tập giá trị cố định của AC-E-PhoneReservation status (GL-07) | enumeration | Không | - |
| DC-TravelerInfoProblem | TravelerInfoProblem | «enumeration» | PKG-23 | Liệt kê kết quả kiểm tra thông tin người đi | Thiết kế: luồng 7a, 7b của P04 UC-002 | enumeration | Không | - |
| DC-CheckOutcome | CheckOutcome | «enumeration» | PKG-23 | Liệt kê kết luận soát một vé | Thiết kế: BR-20, BR-21, BR-22 và kết quả Hợp lệ (GL-14) | enumeration | Không | WRONG_TRIP do lớp điều phối soát vé của PKG-11 gán khi mã vé không có trong danh sách (BR-20); Ticket không bao giờ trả giá trị này |

Kết luận về control (Bước 1.4) và tên lớp (Bước 1.5a):

| DC | Có thật cần không | Có cần tách không | Căn cứ (độ phức tạp, thay đổi, phân tán, giao dịch) |
|---|---|---|---|
| DC-BookTicketOnlineService | Cần: điều phối tám operation qua năm bên cộng tác, thứ tự báo lỗi (Q-34), xử lý mốc hết hạn, SMS | Không tách: một tác nhân và một lý do thay đổi (luồng UC-002); phần thanh toán đã tách sang DC-PayTicketOnlineService | Độ phức tạp trung bình; phân tán: bốn lời gọi ra ngoài giao dịch (IF-07, IF-01, IF-03); ranh giới giao dịch T1 ở submitBooking, completeBooking, handleTrigger |
| DC-PayTicketOnlineService | Cần: IF-02 buộc có bên hiện thực ở Application (P10) và cần nơi ghi khoá yêu cầu thanh toán | Không tách; có thể gộp vào dịch vụ của UC-003 khi có P07 | Tạm (ASM-100); giao dịch ngắn ghi paymentAttemptCount trước khi gọi cổng |
| DC-ReturnTicketService | Cần: điều phối kiểm tra, hoàn tiền ngoài giao dịch, huỷ vé và ghi khoản hoàn | Không tách: ACT-01 và ACT-02 cùng luồng, khác nhau ở tham số kênh yêu cầu trả (ASM-45) | Giao dịch T1 chỉ bao bước huỷ vé; lời gọi IF-01 nằm ngoài giao dịch (P11b) |
| DC-TripCancellation | Cần: bỏ vòng PKG-22 <--> PKG-23 (P10) và là đơn vị công việc của IF-11.saveTripCancellation | Không tách | Phối hợp ba lớp miền; không có quy tắc nghiệp vụ riêng ngoài thứ tự huỷ |

Tên lớp: giữ tên P10 cho mọi DC (hậu tố Service cho lớp dịch vụ ứng dụng, hậu tố RestController dành cho PKG-08), không đổi tên và không thấy nguy cơ nhầm; không có controller của MVC trong phạm vi. Lớp mới đặt tên theo vai trò: Policy, SmsContent, Status, Info, Summary, Quote, Receipt, Offer, Hold.

Entity persistent và tách lazy (Bước 1.3): Trip, Route, Seat, BaseFare, HolidaySurcharge, Booking, Ticket, Refund, PhoneReservation là persistent; không tách lớp dữ liệu phụ nạp muộn vì chưa có NFR đo được (NFR-01 chưa có mức đạt, Q-22). Association class: không có. Tập giá trị cố định đã thành enumeration; giá trị có quy tắc riêng (số tiền, mã vé, số điện thoại) là value object của PKG-28 (P10).

Mỗi lớp một mục đích (Bước 1.6): các câu ở cột Trách nhiệm của F1 đều không nối hai trách nhiệm khác lý do thay đổi; DC-Ticket đã được tách theo P10 để đạt điều này.

## F2. Bảng operation

| DC | Visibility | Chữ ký | Mô tả | Tiền/hậu điều kiện | Nguồn (message P07 / UC bước) | Phạm vi | Ngoại lệ / lỗi |
|---|---|---|---|---|---|---|---|
| DC-BookTicketOnlineService | + | BookTicketOnlineService(tripCatalog: ITripCatalogRepository, ticketing: ITicketingRepository, scheduler: ITriggerScheduler, smsSender: ISmsSender, idGenerator: ITicketingIdGenerator, smsContent: TicketSmsContent, payService: PayTicketOnlineService, clock: Clock) | Khởi tạo dịch vụ với các phụ thuộc; clock là java.time.Clock cấu hình múi giờ Asia/Ho_Chi_Minh, thay bằng Clock cố định khi kiểm thử | Tiền: các tham số khác null | Bổ sung: constructor (Bước 2.6, đồng hồ qua constructor) | Instance | - |
| DC-BookTicketOnlineService | + | searchTrips(departurePoint: String, arrivalPoint: String, departureDate: LocalDate): List<TripOffer> | Tìm các chuyến khớp điểm đi, điểm đến, ngày đi, mỗi chuyến kèm số chỗ còn trống và giá vé; rỗng khi không có chuyến (luồng 2a). Giao dịch chỉ đọc | Tiền: các tham số không rỗng, ngày đi không trước ngày hiện tại (ASM-15, P04 chưa có luồng kiểm tra). Hậu: không đổi dữ liệu | P07 UC-002 msg 1.1 // searchTrips; 1.1.1; 1.1.2 | Instance | PersistenceUnavailableException |
| DC-BookTicketOnlineService | + | getSeatMap(tripId: String): Map<String, Boolean> | Trả sơ đồ chỗ của chuyến: mã chỗ --> còn trống (GL-02, Dữ liệu ra 2). Giao dịch chỉ đọc | Tiền: chuyến tồn tại. Hậu: không đổi dữ liệu | P07 UC-002 msg 2.1 // getSeatMap; 2.1.1; 2.1.2 | Instance | TicketSalesRuleException (TRIP_NOT_FOUND; NO_SEAT_LEFT luồng 4a), PersistenceUnavailableException |
| DC-BookTicketOnlineService | + | submitBooking(tripId: String, travelerInfos: List<TravelerInfo>): BookingHold | Lập lần đặt, kiểm tra BR-01, BR-02, BR-03 và thông tin người đi theo thứ tự Q-34, tính tổng tiền, giữ chỗ, hẹn mốc hết thời hạn giữ chỗ rồi gửi yêu cầu thanh toán; trả mã lần đặt, tổng tiền, hạn giữ chỗ và kết quả yêu cầu thanh toán | Tiền: chuyến tồn tại. Hậu: Booking HELD, các Seat HELD, mốc HOLD_EXPIRY đã đăng ký, yêu cầu thanh toán đã gửi | P07 UC-002 msg 3.1 // submitBooking; 3.1.1 đến 3.1.7; 3.1.9 | Instance | TicketSalesRuleException (TRIP_NOT_FOUND, SEAT_LIMIT_EXCEEDED, SEATS_UNAVAILABLE, MISSING_TRAVELER_INFO, INVALID_PHONE), PaymentGatewayUnavailableException, PersistenceUnavailableException |
| DC-BookTicketOnlineService | + | retryPayment(bookingId: String): PaymentRequestResult | Gửi lại yêu cầu thanh toán cho lần đặt đang giữ chỗ khi thanh toán trước không thành công (luồng 10a, ASM-14) | Tiền: Booking HELD và chưa hết thời hạn giữ chỗ. Hậu: một yêu cầu thanh toán mới với khoá mới | P07 UC-002 SD1 loop 10a (msg 3.1.9 lặp); ASM-14 | Instance | TicketSalesRuleException (HOLD_EXPIRED), PaymentGatewayUnavailableException, PersistenceUnavailableException |
| DC-BookTicketOnlineService | + | handleTrigger(reference: TriggerReference): void | Xử lý mốc hết thời hạn giữ chỗ do SS-05 giao: trả chỗ của lần đặt còn HELD; lần đặt không còn HELD hoặc không tồn tại thì bỏ qua (mốc giao ít nhất một lần). Giao dịch ngắn, không gọi hệ thống ngoài | Tiền: reference.kind là HOLD_EXPIRY. Hậu: Booking EXPIRED và các Seat AVAILABLE nếu lần đặt còn HELD | P11b IF-08.handleTrigger; P07 UC-002 msg 3.1.8 // handleSeatHoldExpired | Instance | IllegalArgumentException (kind khác HOLD_EXPIRY), PersistenceUnavailableException |
| DC-BookTicketOnlineService | + | completeBooking(bookingId: String, paymentReference: PaymentReference): BookingSummary | Hoàn tất lần đặt sau thanh toán thành công: phát hành vé, lưu, rồi gửi SMS từng vé; lần đặt đã TICKETED thì trả lại kết quả cũ (kết quả thanh toán có thể giao lặp). Lỗi SMS không huỷ vé | Tiền: Booking HELD hoặc TICKETED. Hậu: Booking TICKETED, vé ISSUED, Seat SOLD | P07 UC-002 msg 3.1.11 đến 3.1.14 (bước 11 đến 13) | Instance | TicketSalesRuleException (HOLD_EXPIRED khi lần đặt EXPIRED), PersistenceUnavailableException |
| DC-BookTicketOnlineService | + | getBookingStatus(bookingId: String): BookingStatus | Cho biết trạng thái lần đặt để client biết hết thời hạn giữ chỗ hoặc đã phát hành vé (client hỏi lại, server không đẩy thông báo; Q-108). Giao dịch chỉ đọc | Tiền: lần đặt tồn tại. Hậu: không đổi | P07 UC-002 msg 3.1.8.2 // showHoldExpiredNotice (dữ liệu hiển thị); 3.1.10 | Instance | IllegalArgumentException, PersistenceUnavailableException |
| DC-BookTicketOnlineService | + | getIssuedTickets(bookingId: String): BookingSummary | Trả các vé đã phát hành và tổng tiền của lần đặt đã TICKETED để hiển thị. Giao dịch chỉ đọc | Tiền: Booking TICKETED. Hậu: không đổi | P07 UC-002 msg 3.1.15 // showIssuedTickets (dữ liệu hiển thị) | Instance | TicketSalesRuleException (HOLD_EXPIRED khi EXPIRED), IllegalArgumentException, PersistenceUnavailableException |
| DC-PayTicketOnlineService | + | PayTicketOnlineService(paymentGateway: IPaymentGateway, ticketing: ITicketingRepository, bookingCompletion: BookTicketOnlineService) | Khởi tạo dịch vụ với cổng thanh toán (IF-01), kho lần đặt (IF-11) và dịch vụ hoàn tất lần đặt | Tiền: các tham số khác null | Bổ sung: constructor | Instance | - |
| DC-PayTicketOnlineService | ~ | payTickets(booking: Booking): PaymentRequestResult | Ghi lần gửi yêu cầu thanh toán lên Booking trong giao dịch ngắn rồi mới gọi IF-01.requestPayment(requestKey, totalAmount); không giữ giao dịch qua lời gọi cổng; không tự thử lại (P11b) | Tiền: Booking HELD, totalAmount > 0. Hậu: paymentAttemptCount tăng 1; cổng đã tiếp nhận khi status Accepted | P07 UC-002 msg 3.1.9 // payTickets | Instance | PaymentGatewayUnavailableException, PersistenceUnavailableException |
| DC-PayTicketOnlineService | + | receivePaymentResult(requestKey: String, outcome: PaymentOutcome, paymentReference: PaymentReference, amount: Money): void | Nhận kết quả thanh toán từ cổng (IF-02): Succeeded và amount bằng totalAmount thì gọi completeBooking; Failed thì giữ nguyên lần đặt để thanh toán lại (ASM-14); amount lệch thì ghi nhật ký, không phát hành. Không ném ngoại lệ về phía SS-01; xử lý lặp theo requestKey an toàn | Tiền: requestKey có dạng <bookingId>-<số lần>. Hậu: lần đặt TICKETED khi thành công | P11b IF-02.receivePaymentResult; P07 UC-002 msg 3.1.9 (trả về kết quả thanh toán) | Instance | - |
| DC-ReturnTicketService | + | ReturnTicketService(ticketing: ITicketingRepository, tripCatalog: ITripCatalogRepository, paymentGateway: IPaymentGateway, policy: TicketReturnPolicy, clock: Clock) | Khởi tạo dịch vụ với các phụ thuộc; clock thay bằng Clock cố định khi kiểm thử biên 4 giờ, 24 giờ | Tiền: các tham số khác null | Bổ sung: constructor (Bước 2.6) | Instance | - |
| DC-ReturnTicketService | + | startReturnTicket(ticketCode: TicketCode, travelerPhone: PhoneNumber, requestChannel: PurchaseChannel): ReturnQuote | Nhận diện vé, kiểm tra vé chưa huỷ, đúng kênh mua, còn từ 4 giờ trở lên, rồi trả thông tin vé, thời gian còn lại, mức hoàn và số tiền hoàn để tác nhân xác nhận. travelerPhone là null khi nhân viên bán vé trả vé tại quầy (ASM-18). Giao dịch chỉ đọc | Hậu: không đổi dữ liệu | P07 UC-008 msg 1.1 // startReturnTicket; 1.1.1 đến 1.1.7; SD5 1c.1 | Instance | TicketSalesRuleException (TICKET_NOT_FOUND, TICKET_CANCELLED, WRONG_CHANNEL, RETURN_TIME_LIMIT), PersistenceUnavailableException |
| DC-ReturnTicketService | + | confirmReturn(ticketCode: TicketCode, travelerPhone: PhoneNumber, requestChannel: PurchaseChannel, displayedRefundAmount: Money): ReturnReceipt | Kiểm tra lại điều kiện, tính lại số tiền hoàn tại thời điểm xác nhận và so với số tiền đã hiển thị (ASM-106), xác định hình thức hoàn, hoàn qua cổng khi cần rồi huỷ vé và ghi khoản hoàn trong một giao dịch ngắn | Tiền: tác nhân đã xác nhận số tiền displayedRefundAmount. Hậu: vé CANCELLED, chỗ AVAILABLE, có Refund; khi hoàn qua cổng không thành công thì không đổi gì | P07 UC-008 msg 2.1 // confirmReturn; 2.1.1 đến 2.1.4; SD4 2.1.3a; SD5 2c.1 | Instance | TicketSalesRuleException (TICKET_NOT_FOUND, TICKET_CANCELLED, WRONG_CHANNEL, RETURN_TIME_LIMIT, REFUND_AMOUNT_CHANGED, REFUND_FAILED), PersistenceUnavailableException |
| DC-TicketSalesRuleException | + | getReason(): TicketSalesRule | Cho biết lý do từ chối | Hậu: không đổi | Bổ sung: DC-BookTicketRestController, DC-ReturnTicketRestController (PKG-08) chọn thông điệp | Instance | - |
| DC-Trip | + | Trip(tripId: String, route: Route, departureTime: LocalDateTime, busType: BusType, baseFare: BaseFare, holidaySurcharge: HolidaySurcharge, seatCodes: List<String>) | Khởi tạo chuyến ACTIVE và tạo một Seat AVAILABLE cho mỗi mã chỗ (composition R-23). holidaySurcharge có thể null khi ngày xuất bến không thuộc khoảng tăng giá. Bảy tham số vì chỉ UC-012 gọi một nơi; ném IllegalArgumentException khi seatCodes rỗng hoặc trùng mã | Tiền: seatCodes không rỗng, mã không trùng. Hậu: status ACTIVE, mọi Seat AVAILABLE | Bổ sung: khởi tạo (UC-012 chưa phân tích sẽ gọi; ORM) | Instance | IllegalArgumentException |
| DC-Trip | + | getTripId(): String | Cho biết mã chuyến | Hậu: không đổi | Bổ sung: DC-BookTicketOnlineService dựng TripOffer, IF-10 nhận biết chuyến | Instance | - |
| DC-Trip | + | getBusType(): BusType | Cho biết loại xe của chuyến | Hậu: không đổi | Bổ sung: dựng TripOffer (Dữ liệu ra 1 #3 của P04 UC-002) | Instance | - |
| DC-Trip | + | getSeatMap(): Map<String, Boolean> | Trả sơ đồ chỗ: mã chỗ --> còn trống hay không (giữ thứ tự sơ đồ xe), mỗi chỗ hỏi Seat.isAvailable() | Hậu: không đổi | P07 UC-002 msg 2.1.1 // getSeatMap; 2.1.1.1 // checkAvailable | Instance | - |
| DC-Trip | + | countAvailableSeats(): Integer | Đếm chỗ còn trống của chuyến (BR-03); là giá trị của thuộc tính dẫn xuất availableSeatCount | Hậu: không đổi | P07 UC-002 msg 1.1.1.2 // checkAvailable (Trip --> Seat); P08 availableSeatCount | Instance | - |
| DC-Trip | + | areSeatsAvailable(seatCodes: List<String>): Boolean | Kiểm tra mọi mã chỗ đã chọn thuộc chuyến và còn trống; mã không thuộc chuyến coi là không còn trống | Tiền: seatCodes không rỗng. Hậu: không đổi (BR-02, BR-03) | P07 UC-002 msg 3.1.3 // checkSeatsAvailable; 3.1.3.1 // checkAvailable | Instance | - |
| DC-Trip | + | findSeats(seatCodes: List<String>): List<Seat> | Lấy các Seat của chuyến theo mã chỗ, cùng thứ tự seatCodes; ném IllegalArgumentException khi có mã không thuộc chuyến | Tiền: đã qua areSeatsAvailable. Hậu: không đổi | Bổ sung: Booking.holdSeats cần đối tượng Seat để giữ chỗ | Instance | IllegalArgumentException |
| DC-Trip | + | determineTicketPrice(): Money | Xác định giá một vé của chuyến: mức tăng giá lễ Tết áp dụng cho ngày xuất bến (0% khi holidaySurcharge null) rồi nhờ BaseFare tính giá (BR-04, BR-05). Cùng một giá cho mọi chỗ nên không có tham số chỗ | Hậu: không đổi | P07 UC-002 msg 3.1.5.1 // determineTicketPrice (từng chỗ); 1.1.1.3, 1.1.1.4; 3.1.5.1.1, 3.1.5.1.2 | Instance | - |
| DC-Trip | + | getRouteAndDepartureTime(): TripSchedule | Cung cấp tên tuyến dạng điểm đi - điểm đến và giờ xuất bến để hiển thị và lập SMS | Hậu: không đổi | P07 UC-002 msg 3.1.12.1; UC-008 msg 1.1.6.1; UC-013 msg 2.1.7.1; UC-015 msg 1.1.3, 3.1.2 // getRouteAndDepartureTime | Instance | - |
| DC-Trip | + | calculateTimeToDeparture(requestTime: LocalDateTime): Duration | Tính thời gian còn lại từ requestTime tới giờ xuất bến; âm khi requestTime sau giờ xuất bến | Hậu: không đổi (GL-34, ASM-23) | P07 UC-008 msg 1.1.4.1 // calculateTimeToDeparture | Instance | - |
| DC-Trip | + | isCancelled(): Boolean | Cho biết chuyến đã ở trạng thái CANCELLED (ASM-26) | Hậu: không đổi | P07 UC-013 msg 1.1.2 // checkNotCancelled | Instance | - |
| DC-Trip | + | isBeforeDeparture(now: LocalDateTime): Boolean | Cho biết now trước giờ xuất bến; chuyến chỉ huỷ được khi true (ASM-24). Bằng giờ xuất bến coi là đã tới giờ | Hậu: không đổi | P07 UC-013 msg 1.1.3 // checkBeforeDeparture | Instance | - |
| DC-Trip | + | markCancelled(): void | Chuyển chuyến sang CANCELLED; chỉ DC-TripCancellation gọi (ASM-26) | Tiền: status ACTIVE. Hậu: status CANCELLED | P07 UC-013 msg 2.1.1 // cancelTrip (phần đổi trạng thái chuyến, P10 F3) | Instance | InvalidStateException |
| DC-Route | + | Route(routeId: String, departurePoint: String, arrivalPoint: String) | Khởi tạo tuyến; ném IllegalArgumentException khi điểm đi hoặc điểm đến rỗng | Tiền: hai điểm không rỗng | Bổ sung: khởi tạo (UC-012, UC-016 chưa phân tích sẽ gọi; ORM) | Instance | IllegalArgumentException |
| DC-Route | + | getDisplayName(): String | Trả tên tuyến dạng <Điểm đi> - <Điểm đến> theo định dạng hiển thị của P04 | Hậu: không đổi | Bổ sung: Trip.getRouteAndDepartureTime dựng TripSchedule (P04 UC-002 Dữ liệu ra 1 #1) | Instance | - |
| DC-Seat | + | Seat(seatCode: String) | Khởi tạo chỗ ở trạng thái AVAILABLE; chỉ Trip gọi khi tạo tập chỗ | Hậu: status AVAILABLE | ST-03 sự kiện create; Bổ sung: khởi tạo | Instance | IllegalArgumentException |
| DC-Seat | + | isAvailable(): Boolean | Cho biết chỗ còn trống: status là AVAILABLE (BR-03) | Hậu: không đổi | P07 UC-002 msg 1.1.1.2, 2.1.1.1, 3.1.3.1 // checkAvailable | Instance | - |
| DC-Seat | + | hold(): void | Chuyển chỗ sang HELD cho một lần đặt; hết thời hạn hay thanh toán xong sẽ được trả hoặc bán | Tiền: status AVAILABLE (BR-03). Hậu: status HELD | P07 UC-002 msg 3.1.6.1 // hold; ST-03 sự kiện hold | Instance | SeatAlreadyHeldException |
| DC-Seat | + | release(): void | Trả chỗ về AVAILABLE khi hết thời hạn giữ chỗ (BR-08) hoặc vé của chỗ được trả (ASM-20). Ở AVAILABLE thì bỏ qua để mốc hết hạn giao lặp không gây lỗi | Tiền: HELD hoặc SOLD, hoặc AVAILABLE (bỏ qua). Hậu: status AVAILABLE | P07 UC-002 msg 3.1.8.1.1; UC-008 msg 2.1.3.1 // release; ST-03 sự kiện release | Instance | - |
| DC-Seat | + | markSold(): void | Chuyển chỗ đang giữ sang SOLD khi vé của chỗ được phát hành | Tiền: status HELD. Hậu: status SOLD | ST-03 sự kiện markSold (bổ sung theo Bước 4.4; Đề xuất sửa P07 UC-002 msg 3.1.11) | Instance | InvalidStateException |
| DC-Seat | + | getSeatCode(): String | Cung cấp mã chỗ | Hậu: không đổi | P07 UC-008 msg 1.1.6.2; UC-015 msg 2.1.2.1 // getSeatCode | Instance | - |
| DC-BaseFare | + | BaseFare(baseFareId: String, busType: BusType, amount: Money, route: Route) | Khởi tạo mức giá cho một cặp tuyến và loại xe; ném IllegalArgumentException khi amount không dương | Tiền: amount > 0 | Bổ sung: khởi tạo (UC-016 chưa phân tích sẽ gọi; ORM) | Instance | IllegalArgumentException |
| DC-BaseFare | + | calculateTicketPrice(surchargeRatePercent: Integer): Money | Tính giá một vé = amount x (100 + surchargeRatePercent) / 100, làm tròn đến đồng (BR-05, ASM-102). busType không cần làm tham số vì BaseFare đã gắn với loại xe | Tiền: surchargeRatePercent trong 0..30 (BR-32). Hậu: không đổi | P07 UC-002 msg 1.1.1.4, 3.1.5.1.2 // calculateTicketPrice | Instance | IllegalArgumentException |
| DC-HolidaySurcharge | + | HolidaySurcharge(holidaySurchargeId: String, startDate: LocalDate, endDate: LocalDate, ratePercent: Integer) | Khởi tạo mức tăng; ném IllegalArgumentException khi endDate trước startDate hoặc ratePercent ngoài 0..30 | Tiền: endDate >= startDate; 0 <= ratePercent <= 30 (BR-32) | Bổ sung: khởi tạo (UC-017 chưa phân tích sẽ gọi; ORM) | Instance | IllegalArgumentException |
| DC-HolidaySurcharge | + | getSurchargeRate(departureDate: LocalDate): Integer | Trả ratePercent khi startDate <= departureDate <= endDate, ngược lại 0 (BR-05) | Hậu: không đổi | P07 UC-002 msg 1.1.1.3, 3.1.5.1.1 // getSurchargeRate | Instance | - |
| IF-10 | + | findTrips(origin: String, destination: String, departureDate: Date): List<Trip> | Tìm các chuyến có tuyến khớp điểm đi, điểm đến và ngày xuất bến là departureDate; rỗng khi không có chuyến (luồng 2a) | Tiền: departureDate không trước ngày hiện tại (ASM-15). Hậu: không đổi dữ liệu | P11b IF-10.findTrips | Instance | PersistenceUnavailableException |
| IF-10 | + | findTrip(route: String, departureDateTime: DateTime): Trip | Tìm chuyến theo tuyến và giờ xuất bến; null khi không có (luồng 2a của UC-013) | Hậu: không đổi dữ liệu | P11b IF-10.findTrip | Instance | PersistenceUnavailableException |
| IF-10 | + | findTripById(tripId: String): Trip | Tìm chuyến theo mã chuyến; null khi không có | Hậu: không đổi dữ liệu | P11b IF-10.findTripById | Instance | PersistenceUnavailableException |
| IF-10 | + | saveTrip(trip: Trip): void | Ghi chuyến cùng trạng thái các chỗ đã đổi bằng cập nhật có điều kiện; hai phiên cùng giữ một chỗ thì một bên thành công | Tiền: trip đã đọc trước đó. Hậu: ghi bền (REQ-67) | P11b IF-10.saveTrip | Instance | SeatAlreadyHeldException, PersistenceUnavailableException |
| DC-SeatAlreadyHeldException | + | getSeatCode(): String | Cho biết mã chỗ vi phạm, null khi không biết | Hậu: không đổi | Bổ sung: lớp gọi ghi nhật ký chỗ xung đột | Instance | - |
| DC-Booking | + | createBooking(bookingId: String, trip: Trip, travelerInfos: List<TravelerInfo>): Booking | Khởi tạo lần đặt DRAFT của một chuyến với thông tin người đi của từng chỗ; chưa kiểm tra quy tắc và chưa lưu (ASM-43, ASM-44) | Tiền: travelerInfos không rỗng. Hậu: status DRAFT, paymentAttemptCount 0 | P07 UC-002 msg 3.1.1 // createBooking; ST-01 sự kiện createBooking | Classifier | IllegalArgumentException |
| DC-Booking | + | isWithinSeatLimit(): Boolean | Cho biết số chỗ của lần đặt không quá MAX_SEATS (BR-01) | Hậu: không đổi | P07 UC-002 msg 3.1.2 // checkMaxSeats | Instance | - |
| DC-Booking | + | validateTravelerInfo(): TravelerInfoProblem | Kiểm tra từng chỗ có họ tên không rỗng và số điện thoại hợp lệ; thiếu thông tin được báo trước sai định dạng (Q-34, ASM-15) | Hậu: không đổi | P07 UC-002 msg 3.1.4 // validateTravelerInfo | Instance | - |
| DC-Booking | + | calculateTotal(): Money | Chốt giá một vé bằng Trip.determineTicketPrice() rồi tính tổng tiền bằng giá một vé nhân số chỗ (BR-06) | Tiền: status DRAFT. Hậu: ticketPrice, totalAmount được ghi | P07 UC-002 msg 3.1.5 // calculateTotal; 3.1.5.1 | Instance | InvalidStateException |
| DC-Booking | + | holdSeats(now: LocalDateTime): void | Giữ mọi chỗ của lần đặt: lấy Seat từ Trip.findSeats, gọi Seat.hold từng chỗ, ghi holdStartTime; tất cả hoặc không (giao dịch của dịch vụ gọi huỷ phần đã đổi khi một chỗ lỗi) | Tiền: status DRAFT, mọi chỗ AVAILABLE. Hậu: mọi Seat HELD, holdStartTime = now, status HELD | P07 UC-002 msg 3.1.6 // holdSeats; 3.1.6.1; ST-01 sự kiện holdSeats | Instance | SeatAlreadyHeldException, InvalidStateException |
| DC-Booking | + | releaseSeats(): void | Trả các chỗ đang giữ khi hết thời hạn giữ chỗ (BR-08). Ở trạng thái khác HELD thì bỏ qua vì mốc hết hạn được giao ít nhất một lần | Tiền: HELD (khác thì bỏ qua). Hậu: mọi Seat AVAILABLE, status EXPIRED | P07 UC-002 msg 3.1.8.1 // releaseSeats; 3.1.8.1.1; ST-01 sự kiện releaseSeats | Instance | - |
| DC-Booking | + | issueTickets(paymentReference: PaymentReference, idGenerator: ITicketingIdGenerator): List<Ticket> | Phát hành mỗi chỗ đang giữ một vé có mã vé duy nhất (BR-09, BR-10), đổi Seat sang SOLD, ghi paymentReference, kết thúc liên kết giữ chỗ (ASM-55) và trả danh sách vé mới | Tiền: status HELD. Hậu: status TICKETED; mỗi vé ISSUED với channel ONLINE; mọi Seat SOLD | P07 UC-002 msg 3.1.11 // issueTickets; 3.1.11.1 // createTicket; ST-01 sự kiện issueTickets | Instance | InvalidStateException |
| DC-Booking | + | getBookingSummary(): BookingSummary | Cung cấp các vé đã phát hành và tổng tiền của lần đặt | Tiền: status TICKETED. Hậu: không đổi | P07 UC-002 msg 3.1.14 // getBookingSummary | Instance | InvalidStateException |
| DC-Booking | + | getHoldExpiryTime(): LocalDateTime | Tính thời điểm hết thời hạn giữ chỗ = holdStartTime + HOLD_DURATION | Tiền: holdStartTime có giá trị. Hậu: không đổi | P07 UC-002 msg 3.1.7 // startWaitingForPayment (dueAt của IF-07.scheduleTrigger) | Instance | InvalidStateException |
| DC-Booking | + | isHoldExpired(now: LocalDateTime): Boolean | Cho biết now không trước thời điểm hết thời hạn giữ chỗ | Tiền: holdStartTime có giá trị. Hậu: không đổi | Bổ sung: DC-BookTicketOnlineService.retryPayment từ chối thanh toán lại sau hạn (luồng 10a, BR-07) | Instance | InvalidStateException |
| DC-Booking | + | startPaymentAttempt(): String | Ghi nhận một lần gửi yêu cầu thanh toán và trả khoá yêu cầu <bookingId>-<số lần> dùng làm requestKey của IF-01.requestPayment | Tiền: status HELD. Hậu: paymentAttemptCount tăng 1 | Bổ sung: Tạm theo ASM-100, UC-003 chưa phân tích; P11b IF-01.requestPayment | Instance | InvalidStateException |
| DC-Booking | + | getBookingId(): String | Cho biết mã lần đặt | Hậu: không đổi | Bổ sung: IF-10, IF-11, DC-PayTicketOnlineService nhận biết lần đặt | Instance | - |
| DC-Booking | + | getTotalAmount(): Money | Cho biết tổng tiền | Hậu: không đổi | Bổ sung: dựng BookingHold, số tiền gửi IF-01.requestPayment | Instance | - |
| DC-Booking | + | getStatus(): BookingStatus | Cho biết trạng thái lần đặt | Hậu: không đổi | Bổ sung: DC-BookTicketOnlineService.getBookingStatus, kiểm tra trạng thái khi nhận mốc và kết quả thanh toán | Instance | - |
| DC-Booking | + | getTrip(): Trip | Cho biết chuyến của lần đặt | Hậu: không đổi | Bổ sung: dịch vụ ghi lại chuyến sau khi đổi trạng thái chỗ (IF-10.saveTrip) | Instance | - |
| DC-Ticket | + | createTicket(ticketCode: TicketCode, trip: Trip, seat: Seat, travelerInfo: TravelerInfo, price: Money, purchaseChannel: PurchaseChannel): Ticket | Khởi tạo vé ISSUED cho một chỗ với mã vé duy nhất (BR-09, BR-10); số điện thoại thô của travelerInfo được chuyển thành PhoneNumber | Tiền: travelerInfo hợp lệ, price > 0. Hậu: status ISSUED, checkedTime rỗng | P07 UC-002 msg 3.1.11.1 // createTicket; ST-02 sự kiện createTicket | Classifier | IllegalArgumentException |
| DC-Ticket | + | isCancelled(): Boolean | Cho biết vé ở trạng thái CANCELLED (ASM-20) | Hậu: không đổi | P07 UC-008 msg 1.1.2 // checkNotCancelled | Instance | - |
| DC-Ticket | + | cancelTicket(refundRatePercent: Integer, refundAmount: Money, refundMethod: RefundMethod): Refund | Huỷ vé do được trả: status CANCELLED, trả chỗ (Seat.release), tạo khoản hoàn. refundOutcome là REFUNDED với hình thức qua cổng (cổng đã xác nhận trước khi gọi) và AWAITING_CASH_PAYOUT với tiền mặt (ASM-46, ASM-54) | Tiền: status ISSUED. Hậu: status CANCELLED, Seat AVAILABLE, có một Refund (R-32) | P07 UC-008 msg 2.1.3 // cancelTicket; 2.1.3.1; 2.1.3.2 // createRefund; ST-02 sự kiện cancelTicket | Instance | InvalidStateException |
| DC-Ticket | + | cancelWithTrip(): void | Huỷ vé vì chuyến bị huỷ: chỉ đổi status, không đụng chỗ (ASM-26, Q-44) | Tiền: status ISSUED. Hậu: status CANCELLED | P07 UC-013 msg 2.1.1.1 // cancelWithTrip; ST-02 sự kiện cancelWithTrip | Instance | InvalidStateException |
| DC-Ticket | + | recordRefund(refundRatePercent: Integer, refundAmount: Money, refundMethod: RefundMethod, refundOutcome: RefundOutcome): Refund | Ghi nhận khoản hoàn của vé đã huỷ cùng chuyến (mức 100% theo BR-17 do dịch vụ truyền vào) với kết quả hoàn do dịch vụ xác định (ASM-48) | Tiền: status CANCELLED, chưa có Refund. Hậu: có một Refund | P07 UC-013 msg 2.1.6 // recordRefund; 2.1.6.1 // createRefund; SD4 2.1.6a | Instance | InvalidStateException |
| DC-Ticket | + | determineCheckResult(): TicketCheckResult | Kết luận kết quả soát: vé CANCELLED là CANCELLED_TICKET (BR-21), vé có checkedTime là ALREADY_CHECKED kèm thời điểm soát trước (BR-22), còn lại VALID; kèm mã chỗ và họ tên người đi. Kiểm đã huỷ trước đã soát sau (Q-47) | Hậu: không đổi | P07 UC-015 msg 2.1.2 // determineCheckResult; 2.1.2.1 | Instance | - |
| DC-Ticket | + | markChecked(checkTime: LocalDateTime): void | Ghi checkedTime cho vé đã được kết luận hợp lệ (ASM-35) | Tiền: status ISSUED, checkedTime rỗng. Hậu: checkedTime = checkTime | P07 UC-015 msg 2.1.3 // markChecked; ST-02 sự kiện markChecked | Instance | InvalidStateException |
| DC-Ticket | + | getTicketCode(): TicketCode | Cho biết mã vé | Hậu: không đổi | Bổ sung: IF-11, IF-01, SMS, kết quả trả vé | Instance | - |
| DC-Ticket | + | getTravelerName(): String | Cho biết họ tên người đi | Hậu: không đổi | Bổ sung: DC-TicketSmsContent (ASM-17) | Instance | - |
| DC-Ticket | + | getTravelerPhone(): PhoneNumber | Cho biết số điện thoại người đi | Hậu: không đổi | Bổ sung: người nhận IF-03.sendSms | Instance | - |
| DC-Ticket | + | getPrice(): Money | Cho biết giá vé đã thanh toán | Hậu: không đổi | Bổ sung: DC-TicketReturnPolicy tính số tiền hoàn (ASM-22) | Instance | - |
| DC-Ticket | + | getPurchaseChannel(): PurchaseChannel | Cho biết kênh mua | Hậu: không đổi | Bổ sung: DC-TicketReturnPolicy (BR-11, BR-15, BR-16), DC-TripCancellation đếm theo kênh | Instance | - |
| DC-Ticket | + | getSeatCode(): String | Cho biết mã chỗ của vé, hỏi Seat.getSeatCode() | Hậu: không đổi | P07 UC-008 msg 1.1.6.2; UC-015 msg 2.1.2.1 (qua vé) | Instance | - |
| DC-Ticket | + | getTrip(): Trip | Cho biết chuyến của vé | Hậu: không đổi | Bổ sung: DC-TicketReturnPolicy, DC-TicketSmsContent lấy giờ xuất bến; dịch vụ ghi chuyến sau khi trả chỗ | Instance | - |
| DC-TicketReturnPolicy | + | matchesPurchaseChannel(ticket: Ticket, requestChannel: PurchaseChannel): Boolean | Cho biết kênh mua của vé trùng kênh đang yêu cầu trả (BR-11) | Hậu: không đổi | P07 UC-008 msg 1.1.3 // checkPurchaseChannel | Instance | - |
| DC-TicketReturnPolicy | + | getTimeToDeparture(ticket: Ticket, requestTime: LocalDateTime): Duration | Trả thời gian còn lại từ requestTime tới giờ xuất bến của chuyến của vé, hỏi Trip.calculateTimeToDeparture (ASM-23) | Hậu: không đổi | P07 UC-008 msg 1.1.4 // checkReturnTimeLimit (phần tính thời gian còn lại); 1.1.4.1 | Instance | - |
| DC-TicketReturnPolicy | + | isReturnTimeAllowed(timeToDeparture: Duration): Boolean | Cho biết thời gian còn lại từ MIN_RETURN_TIME trở lên (BR-12); đúng 4 giờ vẫn được trả | Hậu: không đổi | P07 UC-008 msg 1.1.4 // checkReturnTimeLimit (phần so với 4 giờ, BR-12); tách riêng để kiểm thử biên 4 giờ | Instance | - |
| DC-TicketReturnPolicy | + | calculateRefundAmount(ticket: Ticket, timeToDeparture: Duration): RefundQuote | Xác định mức hoàn 90% khi từ 24 giờ trở lên (BR-13), 50% khi từ 4 giờ đến dưới 24 giờ (BR-14) và số tiền hoàn = giá vé x mức hoàn, làm tròn đến đồng (ASM-102) | Tiền: isReturnTimeAllowed(timeToDeparture) là true. Hậu: không đổi | P07 UC-008 msg 1.1.5 // calculateRefundAmount | Instance | IllegalArgumentException |
| DC-TicketReturnPolicy | + | getTicketReturnInfo(ticket: Ticket): TicketReturnInfo | Cung cấp mã vé, tuyến, giờ xuất bến, mã chỗ, giá vé để hiển thị cho tác nhân (ASM-19) | Hậu: không đổi | P07 UC-008 msg 1.1.6 // getTicketReturnInfo | Instance | - |
| DC-TicketReturnPolicy | + | determineRefundMethod(ticket: Ticket): RefundMethod | Xác định hình thức hoàn theo kênh mua: ONLINE là VIA_GATEWAY (BR-15), COUNTER là CASH_AT_COUNTER (BR-16, ASM-28) | Hậu: không đổi | P07 UC-008 msg 2.1.1; UC-013 msg 2.1.4 // determineRefundMethod | Instance | - |
| DC-TicketReturnPolicy | + | getCancelImpactInfo(ticket: Ticket): CancelImpactInfo | Cung cấp kênh mua và số tiền hoàn bằng 100% giá vé của một vé còn hiệu lực khi chuyến bị huỷ (BR-17) | Hậu: không đổi | P07 UC-013 msg 1.1.4.1 // getCancelImpactInfo | Instance | - |
| DC-TicketReturnPolicy | + | calculateTripCancelRefundAmount(ticket: Ticket): Money | Tính số tiền hoàn bằng 100% giá vé đã thanh toán, không phụ thuộc thời gian còn lại (BR-17, BR-19, ASM-22) | Hậu: không đổi | P07 UC-013 msg 2.1.3 // calculateTripCancelRefundAmount | Instance | - |
| DC-TicketSmsContent | + | getTicketSmsContent(ticket: Ticket): String | Lập nội dung SMS gửi vé gồm mã vé, tuyến, giờ xuất bến HH:mm dd/MM/yyyy, mã chỗ, họ tên người đi (ASM-17) | Hậu: không đổi | P07 UC-002 msg 3.1.12 // getTicketSmsContent; 3.1.12.1 | Instance | - |
| DC-TicketSmsContent | + | getTripCancelSmsContent(ticket: Ticket, refundAmount: Money, refundMethod: RefundMethod): String | Lập nội dung SMS báo huỷ chuyến gồm mã vé, tuyến, giờ xuất bến, câu báo chuyến bị huỷ, số tiền hoàn, hình thức hoàn (ASM-29) | Hậu: không đổi | P07 UC-013 msg 2.1.7 // getTripCancelSmsContent; 2.1.7.1 | Instance | - |
| DC-TicketSmsContent | + | getTicketSmsMessageKey(ticket: Ticket): String | Trả khoá chống gửi trùng ổn định giữa các lần gửi lại, dạng <mã vé>:TICKET (P11b IF-03 messageKey) | Hậu: không đổi | Bổ sung: tham số messageKey của IF-03.sendSms | Instance | - |
| DC-TicketSmsContent | + | getTripCancelSmsMessageKey(ticket: Ticket): String | Trả khoá chống gửi trùng dạng <mã vé>:TRIP_CANCEL | Hậu: không đổi | Bổ sung: tham số messageKey của IF-03.sendSms | Instance | - |
| DC-TripCancellation | + | create(trip: Trip, tickets: List<Ticket>, phoneReservations: List<PhoneReservation>, policy: TicketReturnPolicy): TripCancellation | Khởi tạo đơn vị huỷ chuyến, giữ lại các vé còn hiệu lực (GL-38) và đặt chỗ chưa thanh toán (ASM-27) trong dữ liệu đưa vào | Tiền: tickets, phoneReservations là của trip. Hậu: không đổi chuyến, vé, đặt chỗ | Bổ sung: khởi tạo từ dữ liệu IF-11.findTicketsOfTrip, findPhoneReservationsOfTrip | Classifier | IllegalArgumentException |
| DC-TripCancellation | + | getCancellationSummary(): CancellationSummary | Tổng hợp tuyến, giờ xuất bến, số vé còn hiệu lực theo kênh mua, số đặt chỗ chưa thanh toán và tổng số tiền hoàn (BR-17) | Hậu: không đổi | P07 UC-013 msg 1.1.4 // getCancellationSummary; 1.1.4.1; 1.1.4.2 | Instance | - |
| DC-TripCancellation | + | cancelTrip(): List<Ticket> | Chuyển chuyến sang CANCELLED, huỷ từng vé còn hiệu lực và từng đặt chỗ chưa thanh toán của chuyến; trả danh sách vé vừa huỷ để hoàn tiền và báo SMS | Tiền: chuyến chưa huỷ. Hậu: Trip CANCELLED; vé còn hiệu lực CANCELLED; đặt chỗ chưa thanh toán CANCELLED | P07 UC-013 msg 2.1.1 // cancelTrip; 2.1.1.1; 2.1.1.2 | Instance | InvalidStateException |
| DC-Refund | + | createRefund(refundAmount: Money, refundRatePercent: Integer, refundMethod: RefundMethod, refundOutcome: RefundOutcome): Refund | Khởi tạo khoản hoàn của một vé đã huỷ; chỉ Ticket gọi | Tiền: refundAmount >= 0, 0 <= refundRatePercent <= 100. Hậu: khoản hoàn bất biến | P07 UC-008 msg 2.1.3.2; UC-013 msg 2.1.6.1, SD4 2.1.6a.1 // createRefund | Classifier | IllegalArgumentException |
| DC-PhoneReservation | + | PhoneReservation(reservationId: String, trip: Trip) | Khởi tạo đặt chỗ UNPAID trên một chuyến | Hậu: status UNPAID | Bổ sung: khởi tạo (UC-004 chưa phân tích sẽ gọi; ORM) | Instance | IllegalArgumentException |
| DC-PhoneReservation | + | isUnpaid(): Boolean | Cho biết đặt chỗ chưa thanh toán (ASM-27) | Hậu: không đổi | P07 UC-013 msg 1.1.4.2 // checkUnpaid | Instance | - |
| DC-PhoneReservation | + | cancelWithTrip(): void | Huỷ đặt chỗ chưa thanh toán cùng chuyến bị huỷ; đặt chỗ đã thanh toán hoặc đã huỷ thì bỏ qua (ASM-27) | Tiền: UNPAID (khác thì bỏ qua). Hậu: status CANCELLED | P07 UC-013 msg 2.1.1.2 // cancelWithTrip | Instance | - |
| IF-11 | + | saveBooking(booking: Booking): void | Ghi lần đặt cùng các vé đã phát hành và trạng thái | Hậu: ghi bền trong giao dịch của dịch vụ gọi | P11b IF-11.saveBooking | Instance | PersistenceUnavailableException |
| IF-11 | + | findBooking(bookingId: String): Booking | Tìm lần đặt theo mã; null khi không có | Hậu: không đổi dữ liệu | P11b IF-11.findBooking | Instance | PersistenceUnavailableException |
| IF-11 | + | findTicket(ticketCode: TicketCode, travelerPhone: PhoneNumber): Ticket | Tìm vé khớp mã vé và, khi travelerPhone khác null, khớp số điện thoại người đi; null khi không khớp (luồng 2a của UC-008) | Hậu: không đổi dữ liệu | P11b IF-11.findTicket | Instance | PersistenceUnavailableException |
| IF-11 | + | findTicketsOfTrip(tripId: String): List<Ticket> | Tìm các vé của chuyến kèm trạng thái | Hậu: không đổi dữ liệu | P11b IF-11.findTicketsOfTrip | Instance | PersistenceUnavailableException |
| IF-11 | + | findPhoneReservationsOfTrip(tripId: String): List<PhoneReservation> | Tìm các đặt chỗ qua điện thoại của chuyến | Hậu: không đổi dữ liệu | P11b IF-11.findPhoneReservationsOfTrip | Instance | PersistenceUnavailableException |
| IF-11 | + | saveTicket(ticket: Ticket): void | Ghi vé cùng trạng thái và khoản hoàn nếu có | Hậu: ghi bền trong một giao dịch | P11b IF-11.saveTicket | Instance | PersistenceUnavailableException |
| IF-11 | + | saveTripCancellation(cancellation: TripCancellation): void | Ghi chuyến đã huỷ cùng các vé còn hiệu lực và đặt chỗ chưa thanh toán đã huỷ | Hậu: ghi bền trong một giao dịch | P11b IF-11.saveTripCancellation | Instance | PersistenceUnavailableException |
| IF-15 | + | nextBookingId(): String | Cấp mã lần đặt mới | Hậu: mã chưa từng cấp | Bổ sung: DC-BookTicketOnlineService đặt bookingId cho createBooking | Instance | PersistenceUnavailableException |
| IF-15 | + | nextTicketCode(): TicketCode | Cấp mã vé mới duy nhất trên toàn hệ thống (BR-10) | Hậu: mã chưa từng cấp | P07 UC-002 msg 3.1.11.1 (mã vé duy nhất) | Instance | PersistenceUnavailableException |

### F2a. Cơ chế lập lịch (Bước 1.6a)

| Mốc | Nguồn | Hẹn | Huỷ | Điểm vào khi tới mốc | Xử lý khi đối tượng đã đổi trạng thái |
|---|---|---|---|---|---|
| Hết thời hạn giữ chỗ 10 phút của lần đặt (BR-07, EV-03) | P07 UC-002 msg 3.1.7 // startWaitingForPayment, msg 3.1.8 // after(BR-07) handleSeatHoldExpired. Mốc là thời hạn nội bộ của UC-002 (P07 UC-002 Mục 1), được đăng ký ở SS-05 theo P09 F7 | DC-BookTicketOnlineService.submitBooking gọi IF-07.scheduleTrigger(HOLD_EXPIRY, bookingId, tripId, Booking.getHoldExpiryTime()); khoá (kind, targetId) nên đăng ký lại không tạo mốc thứ hai | Không huỷ khi thanh toán xong: IF-07.cancelTriggers huỷ theo nhóm chuyến (P11b) chứ không theo lần đặt; mốc còn lại đến hạn sẽ bị bỏ qua nhờ guard | IF-08.handleTrigger --> DC-BookTicketOnlineService.handleTrigger | Guard trong method: lần đặt không tồn tại hoặc không còn HELD thì bỏ qua; kind khác HOLD_EXPIRY thì ném IllegalArgumentException (chờ Đề xuất sửa P10 về bộ định tuyến theo kind) |
| Mốc UC-006 (60 phút), UC-014 (15 phút) tính từ giờ xuất bến | P07 UC-013 msg 2.1.2 // cancelTripTriggers | Do UC-012 (chưa phân tích) | DC-CancelTripService (PKG-10) gọi IF-07.cancelTriggers; ngoài phạm vi lần chạy | UC-006, UC-014 chưa có P07 | Chưa có |

## F3. Thiết kế method

| DC.operation | Thuật toán / các bước chính | Đối tượng và operation khác được dùng | Cách dùng thuộc tính, tham số, quan hệ | Hành vi theo trạng thái |
|---|---|---|---|---|
| DC-BookTicketOnlineService.searchTrips(departurePoint, arrivalPoint, departureDate) | 1. Giao dịch chỉ đọc. 2. trips = IF-10.findTrips(departurePoint, arrivalPoint, departureDate). 3. Với mỗi chuyến dựng TripOffer(tripId, getRouteAndDepartureTime(), getBusType(), countAvailableSeats(), determineTicketPrice()). 4. Sắp xếp theo giờ xuất bến tăng dần (Thiết kế: thứ tự hiển thị ổn định). 5. Trả danh sách; rỗng khi không có chuyến (luồng 2a) | IF-10.findTrips; Trip.getRouteAndDepartureTime, getBusType, countAvailableSeats, determineTicketPrice | departureDate truyền nguyên cho truy vấn; không lưu trạng thái trong dịch vụ | - |
| DC-BookTicketOnlineService.getSeatMap(tripId) | 1. Giao dịch chỉ đọc. 2. trip = IF-10.findTripById(tripId); null thì ném TRIP_NOT_FOUND. 3. Nếu trip.countAvailableSeats() bằng 0 thì ném NO_SEAT_LEFT (luồng 4a). 4. Trả trip.getSeatMap() | IF-10.findTripById; Trip.countAvailableSeats, getSeatMap | tripId xác định chuyến | - |
| DC-BookTicketOnlineService.submitBooking(tripId, travelerInfos) | 1. Giao dịch T1 (đọc, giữ chỗ, ghi). trip = IF-10.findTripById(tripId); null thì ném TRIP_NOT_FOUND. 2. booking = Booking.createBooking(IF-15.nextBookingId(), trip, travelerInfos). 3. Nếu không booking.isWithinSeatLimit() thì ném SEAT_LIMIT_EXCEEDED (luồng 6a). 4. Nếu không trip.areSeatsAvailable(mã chỗ của travelerInfos) thì ném SEATS_UNAVAILABLE (6b). 5. problem = booking.validateTravelerInfo(): MISSING_INFO thì ném MISSING_TRAVELER_INFO (7a), INVALID_PHONE thì ném INVALID_PHONE (7b); thứ tự 3, 4, 5 theo Q-34. 6. booking.calculateTotal(); booking.holdSeats(LocalDateTime.now(clock)). 7. IF-10.saveTrip(trip) (cập nhật có điều kiện) rồi IF-11.saveBooking(booking); commit T1. SeatAlreadyHeldException ở bước 6 hoặc 7 thì rollback và ném SEATS_UNAVAILABLE (Q-106). 8. Ngoài giao dịch: IF-07.scheduleTrigger(HOLD_EXPIRY, bookingId, tripId, booking.getHoldExpiryTime()). Nếu kho mốc lỗi (TriggerStoreUnavailableException): giao dịch bù T2 gọi booking.releaseSeats(), saveTrip, saveBooking rồi ném lại lỗi để chỗ không bị giữ vô hạn (Q-104). 9. Ngoài giao dịch: paymentRequest = payService.payTickets(booking); PaymentGatewayUnavailableException được ném ra, lần đặt vẫn HELD (ASM-14). 10. Trả BookingHold(bookingId, totalAmount, holdExpiryTime, paymentRequest) | IF-10.findTripById, saveTrip; IF-15.nextBookingId; Booking.createBooking, isWithinSeatLimit, validateTravelerInfo, calculateTotal, holdSeats, getHoldExpiryTime, releaseSeats; Trip.areSeatsAvailable; IF-11.saveBooking; IF-07.scheduleTrigger; PayTicketOnlineService.payTickets | Ranh giới giao dịch bao trọn bước 1 đến 7; không giữ giao dịch qua lời gọi IF-07 và IF-01 (P11b) | Booking vào HELD ở bước 6 (ST-01); Seat vào HELD (ST-03) |
| DC-BookTicketOnlineService.retryPayment(bookingId) | 1. booking = IF-11.findBooking(bookingId); null thì ném IllegalArgumentException. 2. Nếu booking.getStatus() khác HELD hoặc booking.isHoldExpired(LocalDateTime.now(clock)) thì ném HOLD_EXPIRED. 3. Trả payService.payTickets(booking) | IF-11.findBooking; Booking.getStatus, isHoldExpired; PayTicketOnlineService.payTickets | Mỗi lần gọi payTickets tăng paymentAttemptCount nên có requestKey mới | Chỉ HELD được thanh toán lại |
| DC-BookTicketOnlineService.handleTrigger(reference) | 1. Nếu reference.kind khác HOLD_EXPIRY thì ném IllegalArgumentException (SS-05 coi là lỗi xử lý, giao lại). 2. Giao dịch ngắn. booking = IF-11.findBooking(reference.targetId); null hoặc getStatus() khác HELD thì kết thúc, không làm gì (mốc giao ít nhất một lần). 3. booking.releaseSeats(). 4. IF-10.saveTrip(booking.getTrip()); IF-11.saveBooking(booking); commit. Cập nhật có điều kiện theo phiên bản: nếu thanh toán thành công commit trước thì bên này thua, ném PersistenceUnavailableException và được giao lại, lần giao lại thấy TICKETED và kết thúc | IF-11.findBooking, saveBooking; IF-10.saveTrip; Booking.getStatus, releaseSeats, getTrip | reference.targetId là mã lần đặt (P11b IF-07) | Chỉ lần đặt HELD bị trả chỗ (ST-01 T4) |
| DC-BookTicketOnlineService.completeBooking(bookingId, paymentReference) | 1. Giao dịch T1. booking = IF-11.findBooking(bookingId); null thì ném IllegalArgumentException. 2. Nếu status TICKETED thì trả booking.getBookingSummary() (kết quả thanh toán giao lặp). Nếu EXPIRED hoặc DRAFT thì ném HOLD_EXPIRED (thanh toán đến sau khi chỗ đã trả, Q-10; lớp gọi ghi nhật ký để xử lý tay). 3. tickets = booking.issueTickets(paymentReference, IF-15). 4. IF-10.saveTrip(booking.getTrip()) (Seat SOLD); IF-11.saveBooking(booking) kèm vé; commit T1. 5. Ngoài giao dịch, với mỗi vé: IF-03.sendSms(ticket.getTravelerPhone(), smsContent.getTicketSmsContent(ticket), smsContent.getTicketSmsMessageKey(ticket)). Kết quả khác Accepted hoặc SmsGatewayUnavailableException thì ghi nhật ký, không huỷ vé, gửi tiếp vé kế (Q-56). 6. Trả booking.getBookingSummary() | IF-11.findBooking, saveBooking; IF-10.saveTrip; Booking.issueTickets, getBookingSummary; TicketSmsContent; IF-03.sendSms | paymentReference lưu trên Booking (ASM-41); gửi SMS đồng bộ từng vé theo P07 (P11b nêu rủi ro thời gian, giữ nguyên) | Booking HELD --> TICKETED (ST-01 T3); chấp nhận khi HELD dù đã quá 10 phút nhưng mốc chưa xử lý (ASM-103) |
| DC-BookTicketOnlineService.getBookingStatus(bookingId) và getIssuedTickets(bookingId) | getBookingStatus: 1. Giao dịch chỉ đọc. 2. booking = IF-11.findBooking(bookingId); null thì ném IllegalArgumentException. 3. Trả booking.getStatus(). getIssuedTickets: 1 và 2 như trên. 3. Nếu status EXPIRED thì ném HOLD_EXPIRED. 4. Trả booking.getBookingSummary() (ném InvalidStateException khi chưa TICKETED, lớp gọi chỉ hỏi sau khi thấy TICKETED) | IF-11.findBooking; Booking.getStatus, getBookingSummary | Client hỏi lại theo chu kỳ do client quyết định (Q-108) | Phản ánh trạng thái ST-01 |
| DC-PayTicketOnlineService.payTickets(booking) | 1. Giao dịch ngắn. requestKey = booking.startPaymentAttempt(); IF-11.saveBooking(booking); commit. 2. Ngoài giao dịch: result = IF-01.requestPayment(requestKey, booking.getTotalAmount()). 3. Trả result (Accepted, Rejected, Unknown). Không tự thử lại (P11b) | Booking.startPaymentAttempt, getTotalAmount; IF-11.saveBooking; IF-01.requestPayment | paymentAttemptCount ghi trước khi gọi cổng để khoá yêu cầu không bị dùng lại sau khi khởi động lại | Chỉ lần đặt HELD |
| DC-PayTicketOnlineService.receivePaymentResult(requestKey, outcome, paymentReference, amount) | 1. Bọc toàn bộ trong try-catch: không ném ngoại lệ ra ngoài (IF-02). 2. bookingId = phần của requestKey trước dấu gạch nối cuối. 3. booking = IF-11.findBooking(bookingId); null thì ghi nhật ký rồi kết thúc. 4. Nếu outcome Succeeded: nếu amount khác booking.getTotalAmount() thì ghi nhật ký cảnh báo và không phát hành; ngược lại gọi bookingCompletion.completeBooking(bookingId, paymentReference). 5. Nếu outcome Failed: ghi nhật ký, giữ lần đặt HELD để thanh toán lại (ASM-14). 6. Ngoại lệ nghiệp vụ HOLD_EXPIRED từ completeBooking được ghi nhật ký để đối soát (Q-10) | IF-11.findBooking; Booking.getTotalAmount; BookTicketOnlineService.completeBooking | requestKey có dạng <bookingId>-<số lần> do Booking.startPaymentAttempt sinh | Chỉ phát hành khi lần đặt còn HELD (kiểm trong completeBooking) |
| DC-ReturnTicketService.startReturnTicket(ticketCode, travelerPhone, requestChannel) | 1. Giao dịch chỉ đọc. ticket = IF-11.findTicket(ticketCode, travelerPhone); null thì ném TICKET_NOT_FOUND (2a). 2. Nếu ticket.isCancelled() thì ném TICKET_CANCELLED (2b). 3. Nếu không policy.matchesPurchaseChannel(ticket, requestChannel) thì ném WRONG_CHANNEL (3a). 4. now = LocalDateTime.now(clock); timeLeft = policy.getTimeToDeparture(ticket, now); nếu không policy.isReturnTimeAllowed(timeLeft) thì ném RETURN_TIME_LIMIT (3b). 5. quote = policy.calculateRefundAmount(ticket, timeLeft); info = policy.getTicketReturnInfo(ticket). 6. Trả ReturnQuote(info, timeLeft, quote.ratePercent, quote.amount). Bước 1 đến 4 nằm trong private loadReturnableTicket dùng chung với confirmReturn | IF-11.findTicket; Ticket.isCancelled; TicketReturnPolicy.matchesPurchaseChannel, getTimeToDeparture, isReturnTimeAllowed, calculateRefundAmount, getTicketReturnInfo | requestChannel suy từ tác nhân: ACT-01 là ONLINE, ACT-02 là COUNTER (ASM-45); travelerPhone null với ACT-02 (ASM-18) | Vé CANCELLED bị từ chối (ST-02) |
| DC-ReturnTicketService.confirmReturn(ticketCode, travelerPhone, requestChannel, displayedRefundAmount) | 1. Lặp bước 1 đến 4 của startReturnTicket (dịch vụ không giữ trạng thái giữa hai bước). 2. quote = policy.calculateRefundAmount(ticket, timeLeft); nếu quote.amount khác displayedRefundAmount thì ném REFUND_AMOUNT_CHANGED (ASM-106). 3. method = policy.determineRefundMethod(ticket). 4. Nếu method là VIA_GATEWAY: result = IF-01.requestRefund(ticket.getTicketCode(), quote.amount, 'refund-' + ticketCode); result.status khác Succeeded hoặc PaymentGatewayUnavailableException thì ném REFUND_FAILED, không đổi dữ liệu (ASM-21, ASM-107). 5. Giao dịch T1: ticket.cancelTicket(quote.ratePercent, quote.amount, method); IF-10.saveTrip(ticket.getTrip()) (Seat AVAILABLE); IF-11.saveTicket(ticket) kèm Refund; commit. 6. Trả ReturnReceipt(ticketCode, CANCELLED, quote.amount, method). Nếu bước 5 lỗi sau khi cổng đã hoàn thì ghi nhật ký requestKey để đối soát bằng IF-01.queryRefundStatus (Q-55, Q-104) | IF-11.findTicket, saveTicket; TicketReturnPolicy; IF-01.requestRefund; Ticket.cancelTicket, getTrip; IF-10.saveTrip | requestKey 'refund-' + mã vé là khoá cố định cho một vé vì mỗi vé chỉ hoàn một lần (ASM-46); không giữ giao dịch qua lời gọi cổng | Ticket ISSUED --> CANCELLED (ST-02 T3, T5); Seat --> AVAILABLE (ST-03 T5) |
| DC-Trip.determineTicketPrice() | 1. rate = holidaySurcharge là null ? 0 : holidaySurcharge.getSurchargeRate(departureTime.toLocalDate()). 2. Trả baseFare.calculateTicketPrice(rate) | HolidaySurcharge.getSurchargeRate; BaseFare.calculateTicketPrice | baseFare, holidaySurcharge là quan hệ R-24, R-25 | - |
| DC-Trip.areSeatsAvailable(seatCodes) | 1. Nếu seatCodes có mã trùng nhau thì trả false. 2. Với mỗi mã: tìm Seat có seatCode trùng trong seats; không thấy hoặc không isAvailable() thì trả false. 3. Trả true | Seat.isAvailable | seats là quan hệ R-23 | Chỉ Seat AVAILABLE tính là còn trống |
| DC-Trip.getSeatMap() và countAvailableSeats() | getSeatMap: 1. Tạo LinkedHashMap theo thứ tự seats. 2. Với mỗi Seat: put(seat.getSeatCode(), seat.isAvailable()). 3. Trả bản không sửa được. countAvailableSeats: đếm Seat có isAvailable() là true | Seat.getSeatCode, isAvailable | - | - |
| DC-Trip.markCancelled() | 1. Nếu status là CANCELLED thì ném InvalidStateException. 2. status = CANCELLED | - | Chỉ DC-TripCancellation.cancelTrip gọi | ACTIVE --> CANCELLED; CANCELLED bị từ chối |
| DC-BaseFare.calculateTicketPrice(surchargeRatePercent) | 1. Nếu surchargeRatePercent ngoài 0..30 thì ném IllegalArgumentException (BR-32). 2. Trả amount.percent(100 + surchargeRatePercent), làm tròn đến đồng HALF_UP (ASM-102). Ví dụ P04: 300.000 đ, mức tăng 20% --> 360.000 đ | Money.percent | amount, busType của BaseFare | - |
| DC-HolidaySurcharge.getSurchargeRate(departureDate) | 1. Nếu departureDate không trước startDate và không sau endDate thì trả ratePercent. 2. Ngược lại trả 0 (ASM-105) | - | startDate, endDate, ratePercent | - |
| DC-Seat.hold(), release(), markSold() | hold: AVAILABLE --> HELD; HELD hoặc SOLD thì ném SeatAlreadyHeldException. release: HELD hoặc SOLD --> AVAILABLE; AVAILABLE thì không làm gì. markSold: HELD --> SOLD; AVAILABLE hoặc SOLD thì ném InvalidStateException | - | status | Xem ST-03 và bảng sự kiện bị từ chối |
| DC-Booking.validateTravelerInfo() | 1. Nếu có phần tử travelerInfos với travelerName rỗng sau khi cắt khoảng trắng hoặc travelerPhone rỗng thì trả MISSING_INFO. 2. Ngược lại nếu có travelerPhone mà PhoneNumber.isValid trả false (10 chữ số, bắt đầu bằng 0, ASM-15) thì trả INVALID_PHONE. 3. Ngược lại trả NONE. Thứ tự thiếu thông tin trước sai định dạng theo Q-34 | PhoneNumber.isValid | travelerInfos | Không phụ thuộc trạng thái |
| DC-Booking.calculateTotal() | 1. Nếu status khác DRAFT thì ném InvalidStateException. 2. ticketPrice = trip.determineTicketPrice(). 3. totalAmount = ticketPrice.times(travelerInfos.size()) (BR-06). 4. Trả totalAmount | Trip.determineTicketPrice; Money.times | ticketPrice chốt một lần dùng cho mọi vé và số tiền hoàn sau này (ASM-22) | Chỉ DRAFT |
| DC-Booking.holdSeats(now) | 1. Nếu status khác DRAFT thì ném InvalidStateException. 2. seats = trip.findSeats(mã chỗ của travelerInfos). 3. Với mỗi Seat: seat.hold() (ném SeatAlreadyHeldException nếu không AVAILABLE). 4. holdStartTime = now; status = HELD. Tất cả hoặc không: ngoại lệ ở bước 3 thì giao dịch của dịch vụ huỷ phần đã đổi và đối tượng trong bộ nhớ bị bỏ | Trip.findSeats; Seat.hold | seats là quan hệ R-27 chỉ có giá trị từ bước 4 | DRAFT --> HELD (ST-01 T2); Seat AVAILABLE --> HELD |
| DC-Booking.releaseSeats() | 1. Nếu status khác HELD thì kết thúc (bỏ qua). 2. Với mỗi Seat trong seats: seat.release(). 3. Xoá liên kết seats; status = EXPIRED | Seat.release | seats (R-27) | HELD --> EXPIRED (ST-01 T4); các trạng thái khác bỏ qua |
| DC-Booking.issueTickets(paymentReference, idGenerator) | 1. Nếu status khác HELD thì ném InvalidStateException. 2. Với mỗi Seat trong seats, theo thứ tự travelerInfos: info = TravelerInfo cùng seatCode; ticket = Ticket.createTicket(idGenerator.nextTicketCode(), trip, seat, info, ticketPrice, ONLINE); seat.markSold(). 3. tickets = danh sách vé mới; this.paymentReference = paymentReference. 4. Xoá liên kết seats (ASM-55); status = TICKETED. 5. Trả tickets | IF-15.nextTicketCode; Ticket.createTicket; Seat.markSold | tickets là quan hệ R-28; ticketPrice là giá chốt ở calculateTotal | HELD --> TICKETED (ST-01 T3); Seat HELD --> SOLD |
| DC-Booking.startPaymentAttempt() | 1. Nếu status khác HELD thì ném InvalidStateException. 2. paymentAttemptCount tăng 1. 3. Trả bookingId + '-' + paymentAttemptCount | - | paymentAttemptCount | Chỉ HELD |
| DC-Ticket.cancelTicket(refundRatePercent, refundAmount, refundMethod) | 1. Nếu status khác ISSUED thì ném InvalidStateException. 2. status = CANCELLED. 3. seat.release(). 4. outcome = refundMethod là VIA_GATEWAY ? REFUNDED : AWAITING_CASH_PAYOUT. 5. refund = Refund.createRefund(refundAmount, refundRatePercent, refundMethod, outcome). 6. Trả refund | Seat.release; Refund.createRefund | seat, refund là quan hệ R-30, R-32 | ISSUED hoặc Checked --> CANCELLED (ST-02 T3, T5); CANCELLED bị từ chối |
| DC-Ticket.cancelWithTrip() và recordRefund(...) | cancelWithTrip: 1. Nếu status khác ISSUED thì ném InvalidStateException. 2. status = CANCELLED; không đụng Seat (ASM-26, Q-44). recordRefund: 1. Nếu status khác CANCELLED hoặc refund đã có thì ném InvalidStateException. 2. refund = Refund.createRefund(refundAmount, refundRatePercent, refundMethod, refundOutcome). 3. Trả refund | Refund.createRefund | refund (R-32) | ISSUED --> CANCELLED (ST-02 T4, T6) |
| DC-Ticket.determineCheckResult() và markChecked(checkTime) | determineCheckResult: 1. Nếu status CANCELLED thì trả CANCELLED_TICKET kèm ticketCode, seatCode (BR-21). 2. Nếu checkedTime khác rỗng thì trả ALREADY_CHECKED kèm ticketCode, seatCode, previousCheckedTime = checkedTime (BR-22). 3. Ngược lại trả VALID kèm ticketCode, seatCode, travelerName. Thứ tự đã huỷ trước đã soát sau (Q-47). markChecked: 1. Nếu status khác ISSUED hoặc checkedTime khác rỗng thì ném InvalidStateException. 2. checkedTime = checkTime | Seat.getSeatCode | checkedTime, status; không tự lấy giờ hệ thống, giờ do lớp điều phối soát vé truyền vào | Issued --> Checked (ST-02 T2); các trạng thái khác bị từ chối |
| DC-TicketReturnPolicy.getTimeToDeparture(), isReturnTimeAllowed(), calculateRefundAmount() | getTimeToDeparture: trả ticket.getTrip().calculateTimeToDeparture(requestTime). isReturnTimeAllowed: trả timeToDeparture >= MIN_RETURN_TIME (BR-12). calculateRefundAmount: 1. Nếu không isReturnTimeAllowed thì ném IllegalArgumentException. 2. rate = timeToDeparture >= FULL_RATE_TIME ? HIGH_RATE_PERCENT : LOW_RATE_PERCENT (BR-13, BR-14). 3. amount = ticket.getPrice().percent(rate). 4. Trả RefundQuote(rate, amount). Biên theo ví dụ P04: đúng 24 giờ hoàn 90%, đúng 4 giờ hoàn 50%, 3 giờ không được trả | Trip.calculateTimeToDeparture; Money.percent | Hằng MIN_RETURN_TIME, FULL_RATE_TIME, HIGH_RATE_PERCENT, LOW_RATE_PERCENT | - |
| DC-TripCancellation.getCancellationSummary() | 1. schedule = trip.getRouteAndDepartureTime(). 2. Với mỗi vé còn hiệu lực: info = policy.getCancelImpactInfo(ticket); tăng đếm theo info.purchaseChannel; cộng info.refundAmount vào tổng. 3. unpaid = số đặt chỗ có isUnpaid() là true. 4. Trả CancellationSummary(schedule, onlineCount, counterCount, unpaid, tổng) | Trip.getRouteAndDepartureTime; TicketReturnPolicy.getCancelImpactInfo; PhoneReservation.isUnpaid; Money.plus | tickets, phoneReservations, policy (R-59, R-60, R-61) | Chỉ vé ISSUED và đặt chỗ UNPAID được đếm |
| DC-TripCancellation.cancelTrip() | 1. trip.markCancelled(). 2. Với mỗi vé còn hiệu lực: ticket.cancelWithTrip(). 3. Với mỗi đặt chỗ chưa thanh toán: reservation.cancelWithTrip(). 4. Trả bản sao danh sách vé vừa huỷ. Ranh giới giao dịch do DC-CancelTripService (PKG-10) giữ qua IF-11.saveTripCancellation | Trip.markCancelled; Ticket.cancelWithTrip; PhoneReservation.cancelWithTrip | trip, tickets, phoneReservations (R-58 đến R-60) | Trip ACTIVE --> CANCELLED; Ticket --> CANCELLED |
| DC-TicketSmsContent.getTicketSmsContent(ticket) | 1. schedule = ticket.getTrip().getRouteAndDepartureTime(). 2. Ghép theo thứ tự mã vé, tuyến, giờ xuất bến định dạng HH:mm dd/MM/yyyy, mã chỗ, họ tên người đi (ASM-17). 3. Trả chuỗi. getTripCancelSmsContent ghép thêm câu báo chuyến bị huỷ, số tiền hoàn và hình thức hoàn (ASM-29) | Ticket getters; Trip.getRouteAndDepartureTime | Mẫu câu là hằng của lớp; độ dài tối đa của cổng xử lý trong SS-02 (P11b) | - |

## F4. Ánh xạ message --> operation

| UC / sơ đồ | STT message (P07) | Từ (AC) | Đến (AC) | Message phân tích (// tênTráchNhiệm) | Operation thiết kế (chữ ký đầy đủ) |
|---|---|---|---|---|---|
| UC-002 SD1 | 1.1 | AC-B-BookTicketForm | AC-C-BookTicketOnlineController | // searchTrips | DC-BookTicketOnlineService.searchTrips(departurePoint: String, arrivalPoint: String, departureDate: LocalDate): List<TripOffer> |
| UC-002 SD1 | 1.1.1 | AC-C-BookTicketOnlineController | AC-E-Trip | // findMatchingTrips | IF-10.findTrips(origin: String, destination: String, departureDate: Date): List<Trip>. Khác lớp nhận: thực thể không tự truy vấn tập chuyến chứa nó (P11b IF-10) |
| UC-002 SD1 | 1.1.1.1 | AC-E-Trip | AC-E-Route | // checkRouteMatches | Gộp vào IF-10.findTrips: điều kiện khớp điểm đi, điểm đến là một phần của truy vấn nên DC-Route không có operation tương ứng |
| UC-002 SD1 | 1.1.1.2 | AC-E-Trip | AC-E-Seat | // checkAvailable | DC-Seat.isAvailable(): Boolean, được DC-Trip.countAvailableSeats(): Integer gọi |
| UC-002 SD1 | 1.1.1.3 | AC-E-Trip | AC-E-HolidaySurcharge | // getSurchargeRate | DC-HolidaySurcharge.getSurchargeRate(departureDate: LocalDate): Integer, được DC-Trip.determineTicketPrice(): Money gọi |
| UC-002 SD1 | 1.1.1.4 | AC-E-Trip | AC-E-BaseFare | // calculateTicketPrice | DC-BaseFare.calculateTicketPrice(surchargeRatePercent: Integer): Money |
| UC-002 SD1 | 1.1.2 | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showTrips | Giá trị trả về List<TripOffer> của searchTrips; hiển thị do DC-BookTicketView (PKG-05, ngoài phạm vi lần chạy) |
| UC-002 SD2 | 1.1.2 | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showTrips | Giá trị trả về List<TripOffer> không rỗng của searchTrips (toán hạng else của alt 2a) |
| UC-002 SD2 | 1.1.2a | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showNoTripFoundNotice | searchTrips trả danh sách rỗng; thông báo do DC-BookTicketView |
| UC-002 SD1 | 2.1 | AC-B-BookTicketForm | AC-C-BookTicketOnlineController | // getSeatMap | DC-BookTicketOnlineService.getSeatMap(tripId: String): Map<String, Boolean> |
| UC-002 SD1 | 2.1.1 | AC-C-BookTicketOnlineController | AC-E-Trip | // getSeatMap | IF-10.findTripById(tripId: String): Trip rồi DC-Trip.getSeatMap(): Map<String, Boolean> |
| UC-002 SD1 | 2.1.1.1 | AC-E-Trip | AC-E-Seat | // checkAvailable | DC-Seat.isAvailable(): Boolean |
| UC-002 SD1 | 2.1.2 | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showSeatMap | Giá trị trả về Map<String, Boolean> của getSeatMap; hiển thị do DC-BookTicketView |
| UC-002 SD2 | 2.1.2 | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showSeatMap | Giá trị trả về Map<String, Boolean> của getSeatMap (toán hạng else của alt 4a) |
| UC-002 SD2 | 2.1.2a | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showNoSeatLeftNotice | getSeatMap ném TicketSalesRuleException(NO_SEAT_LEFT) |
| UC-002 SD1 | 3.1 | AC-B-BookTicketForm | AC-C-BookTicketOnlineController | // submitBooking | DC-BookTicketOnlineService.submitBooking(tripId: String, travelerInfos: List<TravelerInfo>): BookingHold |
| UC-002 SD1 | 3.1.1 | AC-C-BookTicketOnlineController | AC-E-Booking | // createBooking | DC-Booking.createBooking(bookingId: String, trip: Trip, travelerInfos: List<TravelerInfo>): Booking |
| UC-002 SD1 | 3.1.2 | AC-C-BookTicketOnlineController | AC-E-Booking | // checkMaxSeats | DC-Booking.isWithinSeatLimit(): Boolean |
| UC-002 SD3 | 3.1.2a | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showSeatLimitExceededNotice | submitBooking ném TicketSalesRuleException(SEAT_LIMIT_EXCEEDED) |
| UC-002 SD1 | 3.1.3 | AC-C-BookTicketOnlineController | AC-E-Trip | // checkSeatsAvailable | DC-Trip.areSeatsAvailable(seatCodes: List<String>): Boolean |
| UC-002 SD1 | 3.1.3.1 | AC-E-Trip | AC-E-Seat | // checkAvailable | DC-Seat.isAvailable(): Boolean |
| UC-002 SD3 | 3.1.3a | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showSeatsUnavailableNotice | submitBooking ném TicketSalesRuleException(SEATS_UNAVAILABLE) |
| UC-002 SD1 | 3.1.4 | AC-C-BookTicketOnlineController | AC-E-Booking | // validateTravelerInfo | DC-Booking.validateTravelerInfo(): TravelerInfoProblem |
| UC-002 SD3 | 3.1.4a | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showMissingTravelerInfoNotice | submitBooking ném TicketSalesRuleException(MISSING_TRAVELER_INFO) |
| UC-002 SD3 | 3.1.4b | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showInvalidPhoneNotice | submitBooking ném TicketSalesRuleException(INVALID_PHONE) |
| UC-002 SD1 | 3.1.5 | AC-C-BookTicketOnlineController | AC-E-Booking | // calculateTotal | DC-Booking.calculateTotal(): Money |
| UC-002 SD1 | 3.1.5.1 | AC-E-Booking | AC-E-Trip | // determineTicketPrice (từng chỗ) | DC-Trip.determineTicketPrice(): Money (cùng giá cho mọi chỗ nên không có tham số chỗ) |
| UC-002 SD1 | 3.1.5.1.1 | AC-E-Trip | AC-E-HolidaySurcharge | // getSurchargeRate | DC-HolidaySurcharge.getSurchargeRate(departureDate: LocalDate): Integer |
| UC-002 SD1 | 3.1.5.1.2 | AC-E-Trip | AC-E-BaseFare | // calculateTicketPrice | DC-BaseFare.calculateTicketPrice(surchargeRatePercent: Integer): Money |
| UC-002 SD1 | 3.1.6 | AC-C-BookTicketOnlineController | AC-E-Booking | // holdSeats | DC-Booking.holdSeats(now: LocalDateTime): void |
| UC-002 SD1 | 3.1.6.1 | AC-E-Booking | AC-E-Seat | // hold | DC-Seat.hold(): void |
| UC-002 SD1 | 3.1.7 | AC-C-BookTicketOnlineController | AC-C-BookTicketOnlineController | // startWaitingForPayment | IF-07.scheduleTrigger(kind: TriggerKind, targetId: String, groupId: String, dueAt: DateTime): TriggerReference, gọi trong DC-BookTicketOnlineService.submitBooking với dueAt = Booking.getHoldExpiryTime(). Khác lớp nhận: mốc do subsystem SS-05 giữ (Bước 1.6a) |
| UC-002 SD1 | 3.1.8 | AC-C-BookTicketOnlineController | AC-C-BookTicketOnlineController | // after(BR-07) handleSeatHoldExpired | DC-BookTicketOnlineService.handleTrigger(reference: TriggerReference): void (hiện thực IF-08.handleTrigger) |
| UC-002 SD1 | 3.1.8.1 | AC-C-BookTicketOnlineController | AC-E-Booking | // releaseSeats | DC-Booking.releaseSeats(): void |
| UC-002 SD1 | 3.1.8.1.1 | AC-E-Booking | AC-E-Seat | // release | DC-Seat.release(): void |
| UC-002 SD1 | 3.1.8.2 | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showHoldExpiredNotice | DC-BookTicketOnlineService.getBookingStatus(bookingId: String): BookingStatus trả EXPIRED; client hỏi lại, server không đẩy thông báo (Q-108) |
| UC-002 SD1 | 3.1.9 | AC-C-BookTicketOnlineController | AC-C-PayTicketOnlineController | // payTickets | DC-PayTicketOnlineService.payTickets(booking: Booking): PaymentRequestResult |
| UC-002 SD1 | 3.1.9 (trả về) | AC-C-PayTicketOnlineController | AC-C-BookTicketOnlineController | kết quả thanh toán (thành công hoặc không thành công) | Chuyển thành bất đồng bộ theo P11b ASM-100: DC-PayTicketOnlineService.receivePaymentResult(requestKey: String, outcome: PaymentOutcome, paymentReference: PaymentReference, amount: Money): void (IF-02) gọi DC-BookTicketOnlineService.completeBooking(bookingId: String, paymentReference: PaymentReference): BookingSummary khi Succeeded |
| UC-002 SD1 | 3.1.10 | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showPaymentFailedNotice | DC-PayTicketOnlineService.receivePaymentResult với outcome Failed giữ lần đặt HELD; thanh toán lại bằng DC-BookTicketOnlineService.retryPayment(bookingId: String): PaymentRequestResult; cách client biết kết quả: Q-108 |
| UC-002 SD1 | 3.1.11 | AC-C-BookTicketOnlineController | AC-E-Booking | // issueTickets | DC-Booking.issueTickets(paymentReference: PaymentReference, idGenerator: ITicketingIdGenerator): List<Ticket> |
| UC-002 SD1 | 3.1.11.1 | AC-E-Booking | AC-E-Ticket | // createTicket | DC-Ticket.createTicket(ticketCode: TicketCode, trip: Trip, seat: Seat, travelerInfo: TravelerInfo, price: Money, purchaseChannel: PurchaseChannel): Ticket; mã vé từ IF-15.nextTicketCode() |
| UC-002 SD1 | 3.1.12 | AC-C-BookTicketOnlineController | AC-E-Ticket | // getTicketSmsContent | DC-TicketSmsContent.getTicketSmsContent(ticket: Ticket): String. Khác lớp nhận: trách nhiệm tách khỏi AC-E-Ticket (P10 F3) |
| UC-002 SD1 | 3.1.12.1 | AC-E-Ticket | AC-E-Trip | // getRouteAndDepartureTime | DC-Trip.getRouteAndDepartureTime(): TripSchedule, được DC-TicketSmsContent gọi qua Ticket.getTrip() |
| UC-002 SD1 | 3.1.13 | AC-C-BookTicketOnlineController | AC-B-SmsGateway | // sendTicketSms | IF-03.sendSms(recipient: PhoneNumber, content: String, messageKey: String): SmsResult |
| UC-002 SD1 | 3.1.13.1 | AC-B-SmsGateway | ACT-07 | // deliverSms | Bên trong SS-02 (P11b), ngoài phạm vi lần chạy |
| UC-002 SD1 | 3.1.14 | AC-C-BookTicketOnlineController | AC-E-Booking | // getBookingSummary | DC-Booking.getBookingSummary(): BookingSummary |
| UC-002 SD1 | 3.1.15 | AC-C-BookTicketOnlineController | AC-B-BookTicketForm | // showIssuedTickets | Giá trị trả về BookingSummary của completeBooking và DC-BookTicketOnlineService.getIssuedTickets(bookingId: String): BookingSummary; hiển thị do DC-BookTicketView |
| UC-008 SD1 | 1.1 | AC-B-ReturnTicketForm | AC-C-ReturnTicketController | // startReturnTicket | DC-ReturnTicketService.startReturnTicket(ticketCode: TicketCode, travelerPhone: PhoneNumber, requestChannel: PurchaseChannel): ReturnQuote |
| UC-008 SD1 | 1.1.1 | AC-C-ReturnTicketController | AC-E-Ticket | // findTicket | IF-11.findTicket(ticketCode: TicketCode, travelerPhone: PhoneNumber): Ticket. Khác lớp nhận: P11b đặt việc tìm vé ở kho vé; DC-Ticket không có findTicket (P10 F3 gán cho DC-Ticket) |
| UC-008 SD1 | 1.1.2 | AC-C-ReturnTicketController | AC-E-Ticket | // checkNotCancelled | DC-Ticket.isCancelled(): Boolean |
| UC-008 SD1 | 1.1.3 | AC-C-ReturnTicketController | AC-E-Ticket | // checkPurchaseChannel | DC-TicketReturnPolicy.matchesPurchaseChannel(ticket: Ticket, requestChannel: PurchaseChannel): Boolean. Khác lớp nhận: P10 F3 |
| UC-008 SD1 | 1.1.4 | AC-C-ReturnTicketController | AC-E-Ticket | // checkReturnTimeLimit | DC-TicketReturnPolicy.getTimeToDeparture(ticket: Ticket, requestTime: LocalDateTime): Duration và isReturnTimeAllowed(timeToDeparture: Duration): Boolean. Tách đôi một message để kiểm thử độc lập biên 4 giờ (BR-12) |
| UC-008 SD1 | 1.1.4.1 | AC-E-Ticket | AC-E-Trip | // calculateTimeToDeparture | DC-Trip.calculateTimeToDeparture(requestTime: LocalDateTime): Duration |
| UC-008 SD1 | 1.1.5 | AC-C-ReturnTicketController | AC-E-Ticket | // calculateRefundAmount | DC-TicketReturnPolicy.calculateRefundAmount(ticket: Ticket, timeToDeparture: Duration): RefundQuote. Khác lớp nhận: P10 F3 |
| UC-008 SD1 | 1.1.6 | AC-C-ReturnTicketController | AC-E-Ticket | // getTicketReturnInfo | DC-TicketReturnPolicy.getTicketReturnInfo(ticket: Ticket): TicketReturnInfo. Khác lớp nhận: P10 F3 |
| UC-008 SD1 | 1.1.6.1 | AC-E-Ticket | AC-E-Trip | // getRouteAndDepartureTime | DC-Trip.getRouteAndDepartureTime(): TripSchedule |
| UC-008 SD1 | 1.1.6.2 | AC-E-Ticket | AC-E-Seat | // getSeatCode | DC-Ticket.getSeatCode(): String, gọi DC-Seat.getSeatCode(): String |
| UC-008 SD1 | 1.1.7 | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showReturnInfo | Giá trị trả về ReturnQuote của startReturnTicket; hiển thị do DC-ReturnTicketView (PKG-05) |
| UC-008 SD2 | 1.1.1a | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showTicketNotFoundNotice | startReturnTicket ném TicketSalesRuleException(TICKET_NOT_FOUND) |
| UC-008 SD2 | 1.1.2 | AC-C-ReturnTicketController | AC-E-Ticket | // checkNotCancelled | DC-Ticket.isCancelled(): Boolean |
| UC-008 SD2 | 1.1.2a | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showTicketCancelledNotice | startReturnTicket ném TicketSalesRuleException(TICKET_CANCELLED) |
| UC-008 SD3 | 1.1.3a | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showWrongChannelNotice | startReturnTicket ném TicketSalesRuleException(WRONG_CHANNEL) |
| UC-008 SD3 | 1.1.4a | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showReturnTimeLimitNotice | startReturnTicket ném TicketSalesRuleException(RETURN_TIME_LIMIT) |
| UC-008 SD1 | 2.1 | AC-B-ReturnTicketForm | AC-C-ReturnTicketController | // confirmReturn | DC-ReturnTicketService.confirmReturn(ticketCode: TicketCode, travelerPhone: PhoneNumber, requestChannel: PurchaseChannel, displayedRefundAmount: Money): ReturnReceipt |
| UC-008 SD1 | 2.1.1 | AC-C-ReturnTicketController | AC-E-Ticket | // determineRefundMethod | DC-TicketReturnPolicy.determineRefundMethod(ticket: Ticket): RefundMethod. Khác lớp nhận: P10 F3 |
| UC-008 SD1 | 2.1.2 | AC-C-ReturnTicketController | AC-B-PaymentGateway | // requestRefund | IF-01.requestRefund(ticketCode: TicketCode, amount: Money, requestKey: String): RefundResult |
| UC-008 SD1 | 2.1.2.1 | AC-B-PaymentGateway | ACT-06 | // submitRefundRequest | Bên trong SS-01 (P11b), ngoài phạm vi lần chạy |
| UC-008 SD1 | 2.1.2.2 | ACT-06 | AC-B-PaymentGateway | // returnRefundResult | Giá trị trả về RefundResult của IF-01.requestRefund (P11b thay hai message bằng một lời gọi có kết quả) |
| UC-008 SD1 | 2.1.3 | AC-C-ReturnTicketController | AC-E-Ticket | // cancelTicket | DC-Ticket.cancelTicket(refundRatePercent: Integer, refundAmount: Money, refundMethod: RefundMethod): Refund |
| UC-008 SD1 | 2.1.3.1 | AC-E-Ticket | AC-E-Seat | // release | DC-Seat.release(): void |
| UC-008 SD1 | 2.1.3.2 | AC-E-Ticket | AC-E-Refund | // createRefund | DC-Refund.createRefund(refundAmount: Money, refundRatePercent: Integer, refundMethod: RefundMethod, refundOutcome: RefundOutcome): Refund |
| UC-008 SD1 | 2.1.4 | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showReturnResult | Giá trị trả về ReturnReceipt của confirmReturn; hiển thị do DC-ReturnTicketView |
| UC-008 SD4 | 2a.1 | AC-B-ReturnTicketForm | AC-C-ReturnTicketController | // cancelReturnRequest | Không có operation: dịch vụ không giữ trạng thái giữa startReturnTicket và confirmReturn nên huỷ yêu cầu chỉ xảy ra ở client (xoá báo giá trong DC-ReturnTicketStore); xem Bước 1.4 |
| UC-008 SD4 | 2a.1.1 | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showReturnAbortedNotice | Không có operation của dịch vụ; thông báo do DC-ReturnTicketView |
| UC-008 SD4 | 2.1.3a | AC-C-ReturnTicketController | AC-B-ReturnTicketForm | // showRefundFailedNotice | confirmReturn ném TicketSalesRuleException(REFUND_FAILED) |
| UC-008 SD5 | 1c.1 | AC-B-CounterReturnTicketForm | AC-C-ReturnTicketController | // startReturnTicket | DC-ReturnTicketService.startReturnTicket với requestChannel = COUNTER và travelerPhone = null (ASM-45, ASM-18) |
| UC-008 SD5 | 1c.2 | AC-C-ReturnTicketController | AC-B-CounterReturnTicketForm | // showReturnInfo | Giá trị trả về ReturnQuote; hiển thị do DC-CounterReturnTicketView (PKG-26) |
| UC-008 SD5 | 2c.1 | AC-B-CounterReturnTicketForm | AC-C-ReturnTicketController | // confirmReturn | DC-ReturnTicketService.confirmReturn với requestChannel = COUNTER |
| UC-008 SD5 | 2c.1.1 | AC-C-ReturnTicketController | AC-E-Ticket | // determineRefundMethod | DC-TicketReturnPolicy.determineRefundMethod(ticket) trả CASH_AT_COUNTER; bỏ qua IF-01 (luồng 7a) |
| UC-008 SD5 | 2c.2 | AC-C-ReturnTicketController | AC-B-CounterReturnTicketForm | // showReturnResult | Giá trị trả về ReturnReceipt; hiển thị do DC-CounterReturnTicketView |
| UC-013 SD1 | 1.1.1 | AC-C-CancelTripController | AC-E-Trip | // findTrip | IF-10.findTrip(route: String, departureDateTime: DateTime): Trip. Khác lớp nhận: P11b IF-10 |
| UC-013 SD1 | 1.1.1.1 | AC-E-Trip | AC-E-Route | // checkRouteMatches | Gộp vào IF-10.findTrip (điều kiện truy vấn) |
| UC-013 SD1 | 1.1.2 | AC-C-CancelTripController | AC-E-Trip | // checkNotCancelled | DC-Trip.isCancelled(): Boolean |
| UC-013 SD1 | 1.1.3 | AC-C-CancelTripController | AC-E-Trip | // checkBeforeDeparture | DC-Trip.isBeforeDeparture(now: LocalDateTime): Boolean |
| UC-013 SD1 | 1.1.4 | AC-C-CancelTripController | AC-E-Trip | // getCancellationSummary | DC-TripCancellation.getCancellationSummary(): CancellationSummary. Khác lớp nhận: P10 F3 (tách DC-TripCancellation) |
| UC-013 SD1 | 1.1.4.1 | AC-E-Trip | AC-E-Ticket | // getCancelImpactInfo | DC-TicketReturnPolicy.getCancelImpactInfo(ticket: Ticket): CancelImpactInfo, được DC-TripCancellation gọi |
| UC-013 SD1 | 1.1.4.2 | AC-E-Trip | AC-E-PhoneReservation | // checkUnpaid | DC-PhoneReservation.isUnpaid(): Boolean, được DC-TripCancellation gọi |
| UC-013 SD1 | 2.1.1 | AC-C-CancelTripController | AC-E-Trip | // cancelTrip | DC-TripCancellation.cancelTrip(): List<Ticket>. Khác lớp nhận: P10 F3; phần đổi trạng thái chuyến là DC-Trip.markCancelled(): void |
| UC-013 SD1 | 2.1.1.1 | AC-E-Trip | AC-E-Ticket | // cancelWithTrip | DC-Ticket.cancelWithTrip(): void, được DC-TripCancellation gọi |
| UC-013 SD1 | 2.1.1.2 | AC-E-Trip | AC-E-PhoneReservation | // cancelWithTrip | DC-PhoneReservation.cancelWithTrip(): void, được DC-TripCancellation gọi |
| UC-013 SD1 | 2.1.3 | AC-C-CancelTripController | AC-E-Ticket | // calculateTripCancelRefundAmount | DC-TicketReturnPolicy.calculateTripCancelRefundAmount(ticket: Ticket): Money. Khác lớp nhận: P10 F3 |
| UC-013 SD1 | 2.1.4 | AC-C-CancelTripController | AC-E-Ticket | // determineRefundMethod | DC-TicketReturnPolicy.determineRefundMethod(ticket: Ticket): RefundMethod. Khác lớp nhận: P10 F3 |
| UC-013 SD1 | 2.1.6 | AC-C-CancelTripController | AC-E-Ticket | // recordRefund | DC-Ticket.recordRefund(refundRatePercent: Integer, refundAmount: Money, refundMethod: RefundMethod, refundOutcome: RefundOutcome): Refund |
| UC-013 SD1 | 2.1.6.1 | AC-E-Ticket | AC-E-Refund | // createRefund | DC-Refund.createRefund(refundAmount: Money, refundRatePercent: Integer, refundMethod: RefundMethod, refundOutcome: RefundOutcome): Refund |
| UC-013 SD1 | 2.1.7 | AC-C-CancelTripController | AC-E-Ticket | // getTripCancelSmsContent | DC-TicketSmsContent.getTripCancelSmsContent(ticket: Ticket, refundAmount: Money, refundMethod: RefundMethod): String. Khác lớp nhận: P10 F3 |
| UC-013 SD1 | 2.1.7.1 | AC-E-Ticket | AC-E-Trip | // getRouteAndDepartureTime | DC-Trip.getRouteAndDepartureTime(): TripSchedule |
| UC-013 SD2 | 1.1.2 | AC-C-CancelTripController | AC-E-Trip | // checkNotCancelled | DC-Trip.isCancelled(): Boolean |
| UC-013 SD2 | 1.1.3 | AC-C-CancelTripController | AC-E-Trip | // checkBeforeDeparture | DC-Trip.isBeforeDeparture(now: LocalDateTime): Boolean |
| UC-013 SD4 | 2.1.6a | AC-C-CancelTripController | AC-E-Ticket | // recordRefund | DC-Ticket.recordRefund(...) với refundOutcome = FAILED |
| UC-013 SD4 | 2.1.6a.1 | AC-E-Ticket | AC-E-Refund | // createRefund | DC-Refund.createRefund(...) với refundOutcome = FAILED |
| UC-015 SD1 | 1.1.1 | AC-C-CheckBoardingTicketController | AC-E-Trip | // findTrip | IF-10.findTrip(route: String, departureDateTime: DateTime): Trip. Khác lớp nhận: P11b IF-10 |
| UC-015 SD1 | 1.1.1.1 | AC-E-Trip | AC-E-Route | // checkRouteMatches | Gộp vào IF-10.findTrip (điều kiện truy vấn) |
| UC-015 SD1 | 1.1.3 | AC-C-CheckBoardingTicketController | AC-E-Trip | // getRouteAndDepartureTime | DC-Trip.getRouteAndDepartureTime(): TripSchedule |
| UC-015 SD1 | 2.1.2 | AC-C-CheckBoardingTicketController | AC-E-Ticket | // determineCheckResult | DC-Ticket.determineCheckResult(): TicketCheckResult |
| UC-015 SD1 | 2.1.2.1 | AC-E-Ticket | AC-E-Seat | // getSeatCode | DC-Seat.getSeatCode(): String, được DC-Ticket.determineCheckResult gọi |
| UC-015 SD1 | 2.1.3 | AC-C-CheckBoardingTicketController | AC-E-Ticket | // markChecked | DC-Ticket.markChecked(checkTime: LocalDateTime): void |
| UC-015 SD1 | 3.1.2 | AC-C-CheckBoardingTicketController | AC-E-Trip | // getRouteAndDepartureTime | DC-Trip.getRouteAndDepartureTime(): TripSchedule |
| UC-015 SD2 | 2.1.2 | AC-C-CheckBoardingTicketController | AC-E-Ticket | // determineCheckResult | DC-Ticket.determineCheckResult(): TicketCheckResult |
| UC-015 SD2 | 2.1.2.1 | AC-E-Ticket | AC-E-Seat | // getSeatCode | DC-Seat.getSeatCode(): String |

F4 có 109 dòng.

## F5. Bảng quan hệ

Loại và điều hướng chọn theo cây quyết định F5 (field --> association; tham số, biến cục bộ --> dependency). Kiểu nền tảng java.time.Clock không có DC. Quan hệ Realization của IF-10, IF-11, IF-15 do SS-07 (PKG-14) giữ, ngoài phạm vi.

| ID | Lớp A | Lớp B | Loại | Multiplicity | Điều hướng | Lý do | Vai trò (A / B) | Căn cứ hiển thị |
|---|---|---|---|---|---|---|---|---|
| R-02 | DC-BookTicketOnlineService | IF-03 | Association | A 1 - B 1 | A --> B | Gốc P08 R-02 (BookTicketOnlineController --> SmsGateway); SmsGateway thành IF-03 (P10 F3). Dịch vụ giữ ISmsSender làm field suốt vòng đời; mỗi vé một lần gọi sendSms (msg 3.1.13). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / smsSender | field |
| R-03 | DC-BookTicketOnlineService | DC-PayTicketOnlineService | Association | A 1 - B 1 | A --> B | Gốc P08 R-03 (Dependency, «include» UC-003). Đổi sang Association vì dịch vụ được tiêm qua constructor và giữ làm field suốt vòng đời (cây quyết định F5 bước 1). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / payService | field |
| R-04 | DC-BookTicketOnlineService | DC-Trip | Dependency |  | A --> B | Gốc P08 R-04 (Association). Đổi sang Dependency: Trip nạp từ IF-10 trong từng method, không giữ làm field; dịch vụ không giữ trạng thái giữa các lời gọi (NFR-01) | - / - | biến cục bộ |
| R-05 | DC-BookTicketOnlineService | DC-Booking | Dependency |  | A --> B | Gốc P08 R-05 (Association). Đổi sang Dependency: Booking được tạo bằng Booking.createBooking hoặc nạp từ IF-11 trong method | - / - | biến cục bộ |
| R-06 | DC-BookTicketOnlineService | DC-Ticket | Dependency |  | A --> B | Gốc P08 R-06 (Association). Đổi sang Dependency: Ticket là kết quả của Booking.issueTickets trong completeBooking | - / - | biến cục bộ |
| R-09 | DC-ReturnTicketService | IF-01 | Association | A 1 - B 1 | A --> B | Gốc P08 R-09 (ReturnTicketController --> PaymentGateway); PaymentGateway thành IF-01. Field paymentGateway; mỗi lần xác nhận trả vé mua trực tuyến gọi requestRefund. Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / paymentGateway | field |
| R-10 | DC-ReturnTicketService | DC-Ticket | Dependency |  | A --> B | Gốc P08 R-10 (Association). Đổi sang Dependency: Ticket nạp từ IF-11.findTicket trong method | - / - | biến cục bộ |
| R-22 | DC-Trip | DC-Route | Association | A 0..* - B 1 | A --> B | Gốc P08 R-22 (GL-04 một lần chạy của một tuyến). Trip cần tuyến để lập TripSchedule | - / route | field |
| R-23 | DC-Trip | DC-Seat | Composition | A 1 - B 1..* | A --> B | Gốc P08 R-23 (Association). Đổi sang Composition: ASM-42 và P10 F4 ghi Trip tạo và giữ Seat, Seat không tồn tại ngoài chuyến, bị xoá cùng chuyến; Q-69 vẫn mở | - / seats | field |
| R-24 | DC-Trip | DC-BaseFare | Association | A 0..* - B 1 | A --> B | Gốc P08 R-24 (ASM-56). Chuyến tra giá theo tuyến và loại xe của chuyến; BaseFare dùng chung nhiều chuyến | - / baseFare | field |
| R-25 | DC-Trip | DC-HolidaySurcharge | Association | A 0..* - B 0..1 | A --> B | Gốc P08 R-25, phía B để trống chờ Q-20; điền 0..1 theo ASM-105 (các khoảng ngày không chồng nhau). Repository nạp mức tăng áp dụng cho ngày xuất bến của chuyến; P13 quyết định lưu liên kết hay truy vấn theo ngày | - / holidaySurcharge | field |
| R-26 | DC-Booking | DC-Trip | Association | A 0..* - B 1 | A --> B | Gốc P08 R-26 (GL-18 trên cùng một chuyến). Lần đặt cần chuyến để giữ chỗ và tính giá | - / trip | field |
| R-27 | DC-Booking | DC-Seat | Association | A 0..1 - B 1..5 | A --> B | Gốc P08 R-27 (ASM-55): liên kết thể hiện việc đang giữ chỗ, lập ở holdSeats và kết thúc ở releaseSeats hoặc issueTickets; B 1..5 theo BR-01 | - / seats | field |
| R-28 | DC-Booking | DC-Ticket | Association | A 0..1 - B 0..5 | A --> B | Gốc P08 R-28. Giữ Association: Ticket tồn tại độc lập sau khi lần đặt hoàn tất (vé mua tại quầy không có lần đặt); không có câu về vòng đời phụ thuộc | - / tickets | field |
| R-29 | DC-Ticket | DC-Trip | Association | A 0..* - B 1 | A --> B | Gốc P08 R-29 (GL-37 một chỗ xác định của một chuyến). Vé cần chuyến để lấy giờ xuất bến | - / trip | field |
| R-30 | DC-Ticket | DC-Seat | Association | A 0..* - B 1 | A --> B | Gốc P08 R-30, phía Ticket để trống chờ Q-36; điền 0..* theo ASM-20 (chỗ của vé đã trả được bán lại nên một Seat có nhiều vé theo thời gian, tối đa một vé còn hiệu lực) | - / seat | field |
| R-31 | DC-BaseFare | DC-Route | Association | A 0..* - B 1 | A --> B | Gốc P08 R-31 (GL-09 mức giá của một cặp tuyến và loại xe) | - / route | field |
| R-32 | DC-Ticket | DC-Refund | Composition | A 1 - B 0..1 | A --> B | Gốc P08 R-32 (Association). Đổi sang Composition: Refund do Ticket tạo (cancelTicket, recordRefund), thuộc đúng một vé (ASM-46, ASM-48) và không có nghĩa khi vé bị xoá | - / refund | field |
| R-33 | DC-Trip | DC-PhoneReservation | Association | A 1 - B 0..* | B --> A | Gốc P08 R-33 (GL-07 giữ chỗ trên một chuyến). Điều hướng một chiều từ PhoneReservation sang Trip để PKG-22 không phụ thuộc PKG-23 (P09 R8); tìm đặt chỗ của chuyến bằng IF-11.findPhoneReservationsOfTrip | trip / - | field |
| R-37 | DC-PhoneReservation | DC-Seat | Association | A 0..1 - B ? | A --> B | Gốc P08 R-37; phía Seat chờ Q-76 (số chỗ của một đặt chỗ qua điện thoại) | - / seat | field |
| R-38 | DC-BookTicketOnlineService | IF-10 | Association | A 1 - B 1 | A --> B | Dịch vụ tìm chuyến, giữ chỗ và ghi trạng thái chỗ qua kho chuyến (P09 R6). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / tripCatalog | field |
| R-39 | DC-BookTicketOnlineService | IF-11 | Association | A 1 - B 1 | A --> B | Dịch vụ ghi lần đặt, vé qua kho vé (P09 R6). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / ticketing | field |
| R-40 | DC-BookTicketOnlineService | IF-07 | Association | A 1 - B 1 | A --> B | Đăng ký mốc hết thời hạn giữ chỗ (Bước 1.6a, msg 3.1.7). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / scheduler | field |
| R-41 | DC-BookTicketOnlineService | IF-15 | Association | A 1 - B 1 | A --> B | Cấp mã lần đặt, truyền bộ sinh mã vé cho Booking.issueTickets. Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / idGenerator | field |
| R-42 | DC-BookTicketOnlineService | DC-TicketSmsContent | Association | A 1 - B 1 | A --> B | Lập nội dung và khoá SMS cho từng vé (msg 3.1.12). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / smsContent | field |
| R-43 | DC-BookTicketOnlineService | IF-08 | Realization |  | A --> B | Hiện thực ITriggerHandler: điểm vào khi tới mốc hết thời hạn giữ chỗ (P10 F2, Bước 1.6a) | - / - | - |
| R-44 | DC-PayTicketOnlineService | IF-01 | Association | A 1 - B 1 | A --> B | Gửi yêu cầu thanh toán (Tạm, ASM-100). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / paymentGateway | field |
| R-45 | DC-PayTicketOnlineService | IF-11 | Association | A 1 - B 1 | A --> B | Ghi lần gửi yêu cầu thanh toán lên Booking trước khi gọi cổng. Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / ticketing | field |
| R-46 | DC-PayTicketOnlineService | IF-02 | Realization |  | A --> B | Hiện thực IPaymentResultListener: nhận kết quả thanh toán do cổng gọi về (P10 F2) | - / - | - |
| R-47 | DC-PayTicketOnlineService | DC-BookTicketOnlineService | Association | A 1 - B 1 | A --> B | Gọi completeBooking khi thanh toán thành công; cùng R-03 tạo phụ thuộc hai chiều giữa hai control cùng package (Vấn đề còn mở). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / bookingCompletion | field |
| R-48 | DC-ReturnTicketService | IF-11 | Association | A 1 - B 1 | A --> B | Nạp vé và ghi vé cùng khoản hoàn. Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / ticketing | field |
| R-49 | DC-ReturnTicketService | IF-10 | Association | A 1 - B 1 | A --> B | Ghi chuyến sau khi vé trả chỗ (IF-10.saveTrip). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / tripCatalog | field |
| R-50 | DC-ReturnTicketService | DC-TicketReturnPolicy | Association | A 1 - B 1 | A --> B | Áp dụng quy tắc trả vé, hoàn tiền (msg 1.1.3 đến 1.1.6, 2.1.1). Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / policy | field |
| R-51 | DC-BookTicketOnlineService | java.time.Clock | Association | A 1 - B 1 | A --> B | Đồng bộ thời điểm hiện tại qua constructor (Bước 2.6); kiểu nền tảng, không có DC. Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / clock | field |
| R-52 | DC-ReturnTicketService | java.time.Clock | Association | A 1 - B 1 | A --> B | Thời điểm trả vé qua constructor (Bước 2.6); kiểu nền tảng, không có DC. Multiplicity 1 - 1: thể hiện singleton do container tiêm (Thiết kế) | - / clock | field |
| R-53 | IF-10 | DC-Trip | Dependency |  | A --> B | Trip là kiểu trả về, tham số của findTrips, findTrip, findTripById, saveTrip | - / - | tham số, kiểu trả về |
| R-54 | IF-11 | DC-Booking | Dependency |  | A --> B | Booking là kiểu trả về, tham số của saveBooking, findBooking | - / - | tham số, kiểu trả về |
| R-55 | IF-11 | DC-Ticket | Dependency |  | A --> B | Ticket là kiểu trả về, tham số của findTicket, findTicketsOfTrip, saveTicket | - / - | tham số, kiểu trả về |
| R-56 | IF-11 | DC-PhoneReservation | Dependency |  | A --> B | PhoneReservation là kiểu trả về của findPhoneReservationsOfTrip | - / - | kiểu trả về |
| R-57 | IF-11 | DC-TripCancellation | Dependency |  | A --> B | TripCancellation là tham số của saveTripCancellation | - / - | tham số |
| R-58 | DC-TripCancellation | DC-Trip | Association | A 1 - B 1 | A --> B | Đơn vị huỷ chuyến giữ chuyến cần huỷ suốt vòng đời của nó (cancelTrip gọi Trip.markCancelled) | - / trip | field |
| R-59 | DC-TripCancellation | DC-Ticket | Association | A 1 - B 0..* | A --> B | Giữ các vé còn hiệu lực của chuyến để tổng hợp và huỷ (msg 1.1.4.1, 2.1.1.1) | - / tickets | field |
| R-60 | DC-TripCancellation | DC-PhoneReservation | Association | A 1 - B 0..* | A --> B | Giữ các đặt chỗ chưa thanh toán của chuyến để đếm và huỷ (msg 1.1.4.2, 2.1.1.2) | - / phoneReservations | field |
| R-61 | DC-TripCancellation | DC-TicketReturnPolicy | Association | A 1 - B 1 | A --> B | Dùng quy tắc tính số tiền hoàn khi huỷ chuyến trong getCancellationSummary | - / policy | field |
| R-62 | DC-TicketReturnPolicy | DC-Ticket | Dependency |  | A --> B | Mọi operation nhận Ticket qua tham số, không giữ trạng thái | - / - | tham số |
| R-63 | DC-TicketSmsContent | DC-Ticket | Dependency |  | A --> B | Mọi operation nhận Ticket qua tham số, không giữ trạng thái | - / - | tham số |
| R-64 | DC-Booking | IF-15 | Dependency |  | A --> B | Bộ sinh mã được truyền qua tham số của issueTickets, Booking không gọi bộ sinh toàn cục (Bước 2.6) | - / - | tham số |
| R-65 | DC-Seat | DC-SeatAlreadyHeldException | Dependency |  | A --> B | Seat.hold ném ngoại lệ khi chỗ không còn AVAILABLE | - / - | ném ngoại lệ |
| R-66 | IF-10 | DC-SeatAlreadyHeldException | Dependency |  | A --> B | IF-10.saveTrip ném ngoại lệ khi cập nhật có điều kiện thất bại (P11b) | - / - | ném ngoại lệ |
| R-67 | DC-PayTicketOnlineService | DC-Booking | Dependency |  | A --> B | Booking là tham số của payTickets | - / - | tham số |

## F6. State machine

Ba lớp có state machine: DC-Booking (ST-01), DC-Ticket (ST-02), DC-Seat (ST-03). Lớp không có state machine: DC-Trip (chỉ hai trạng thái ACTIVE, CANCELLED và một chuyển markCancelled, dưới ngưỡng 3 trạng thái; điều kiện huỷ nằm ở isCancelled, isBeforeDeparture); DC-PhoneReservation (các chuyển ngoài huỷ cùng chuyến thuộc UC-004, UC-005, UC-006 chưa phân tích, xem Vấn đề còn mở); DC-Refund (không đổi sau khi tạo).

### F6.1. Bảng trạng thái

| ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết | entry | do | exit |
|---|---|---|---|---|---|---|
| ST-01 | DC-Booking | Draft | status = DRAFT; chưa giữ chỗ, chưa lưu (ASM-44) | - | - | - |
| ST-01 | DC-Booking | Held | status = HELD; holdStartTime có giá trị | ghi holdStartTime; các Seat sang HELD | chờ thanh toán tối đa HOLD_DURATION (BR-07) | - |
| ST-01 | DC-Booking | Ticketed | status = TICKETED | phát hành vé; các Seat sang SOLD; ghi paymentReference | - | - |
| ST-01 | DC-Booking | Expired | status = EXPIRED | các Seat về AVAILABLE (BR-08) | - | - |
| ST-02 | DC-Ticket | Issued | status = ISSUED; checkedTime rỗng | - | - | - |
| ST-02 | DC-Ticket | Checked | status = ISSUED; checkedTime có giá trị | ghi checkedTime | - | - |
| ST-02 | DC-Ticket | Cancelled | status = CANCELLED | - | - | - |
| ST-03 | DC-Seat | Available | status = AVAILABLE | - | - | - |
| ST-03 | DC-Seat | Held | status = HELD | gắn với lần đặt qua Booking.seats (R-27) | - | - |
| ST-03 | DC-Seat | Sold | status = SOLD | - | - | - |

### F6.2. Bảng chuyển trạng thái

| ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích | STT | Operation tương ứng | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| ST-01 | DC-Booking | (initial) | createBooking(bookingId, trip, travelerInfos) | - | status = DRAFT | Draft | T1 | DC-Booking.createBooking | P07 UC-002 msg 3.1.1; ASM-44 |
| ST-01 | DC-Booking | Draft | holdSeats(now) | mọi Seat AVAILABLE | holdStartTime = now; Seat.hold từng chỗ | Held | T2 | DC-Booking.holdSeats | BR-03; P07 UC-002 msg 3.1.6 |
| ST-01 | DC-Booking | Held | issueTickets(paymentReference, idGenerator) | - | tạo Ticket; Seat.markSold; ghi paymentReference | Ticketed | T3 | DC-Booking.issueTickets | BR-09, BR-10; P07 UC-002 msg 3.1.11 |
| ST-01 | DC-Booking | Held | releaseSeats() | - | Seat.release từng chỗ | Expired | T4 | DC-Booking.releaseSeats | BR-08; P07 UC-002 msg 3.1.8.1 |
| ST-02 | DC-Ticket | (initial) | createTicket(...) | - | status = ISSUED | Issued | T1 | DC-Ticket.createTicket | BR-09, BR-10; P07 UC-002 msg 3.1.11.1 |
| ST-02 | DC-Ticket | Issued | markChecked(checkTime) | - | checkedTime = checkTime | Checked | T2 | DC-Ticket.markChecked | ASM-35; P07 UC-015 msg 2.1.3 |
| ST-02 | DC-Ticket | Issued | cancelTicket(rate, amount, method) | - | Seat.release; tạo Refund | Cancelled | T3 | DC-Ticket.cancelTicket | ASM-20; P07 UC-008 msg 2.1.3 |
| ST-02 | DC-Ticket | Issued | cancelWithTrip() | - | - | Cancelled | T4 | DC-Ticket.cancelWithTrip | ASM-26; P07 UC-013 msg 2.1.1.1 |
| ST-02 | DC-Ticket | Checked | cancelTicket(rate, amount, method) | - | Seat.release; tạo Refund | Cancelled | T5 | DC-Ticket.cancelTicket | ASM-104; Q-74 |
| ST-02 | DC-Ticket | Checked | cancelWithTrip() | - | - | Cancelled | T6 | DC-Ticket.cancelWithTrip | ASM-104; Q-74 |
| ST-03 | DC-Seat | (initial) | create(seatCode) | - | status = AVAILABLE | Available | T1 | DC-Seat.Seat (constructor) | Bổ sung: khởi tạo |
| ST-03 | DC-Seat | Available | hold() | - | - | Held | T2 | DC-Seat.hold | BR-03; P07 UC-002 msg 3.1.6.1 |
| ST-03 | DC-Seat | Held | markSold() | - | - | Sold | T3 | DC-Seat.markSold | Bước 4.4; Đề xuất sửa P07 UC-002 msg 3.1.11 |
| ST-03 | DC-Seat | Held | release() | hết thời hạn giữ chỗ | - | Available | T4 | DC-Seat.release | BR-08; P07 UC-002 msg 3.1.8.1.1 |
| ST-03 | DC-Seat | Sold | release() | vé của chỗ được trả | - | Available | T5 | DC-Seat.release | ASM-20; P07 UC-008 msg 2.1.3.1 |

Sự kiện bị từ chối hoặc bỏ qua (không phải chuyển trạng thái):

| ST | Trạng thái | Sự kiện | Xử lý |
|---|---|---|---|
| ST-01 | Draft | releaseSeats | Bỏ qua (không phải HELD) |
| ST-01 | Draft | issueTickets, startPaymentAttempt | Ném InvalidStateException |
| ST-01 | Held | holdSeats, calculateTotal | Ném InvalidStateException |
| ST-01 | Ticketed, Expired | releaseSeats | Bỏ qua |
| ST-01 | Ticketed, Expired | issueTickets, holdSeats | Ném InvalidStateException; dịch vụ kiểm tra trạng thái trước và trả kết quả cũ khi Ticketed |
| ST-02 | Checked | markChecked | Ném InvalidStateException; lớp điều phối soát vé không gọi vì determineCheckResult đã trả ALREADY_CHECKED |
| ST-02 | Cancelled | markChecked, cancelTicket, cancelWithTrip | Ném InvalidStateException; DC-ReturnTicketService kiểm tra isCancelled trước, DC-TripCancellation chỉ nhận vé còn hiệu lực |
| ST-03 | Available | release | Bỏ qua (mốc hết hạn giao lặp) |
| ST-03 | Available, Sold | markSold | Ném InvalidStateException |
| ST-03 | Held, Sold | hold | Ném SeatAlreadyHeldException |

### F6.3. Ánh xạ về mô hình lớp

| ST | Thuộc tính biểu diễn trạng thái | Kiểu (enumeration) | Operation được thêm/sửa |
|---|---|---|---|
| ST-01 | DC-Booking.status | DC-BookingStatus | Không thêm: createBooking, holdSeats, releaseSeats, issueTickets đã có từ P07 |
| ST-02 | DC-Ticket.status; checkedTime phân biệt Issued và Checked | DC-TicketStatus | Không thêm: createTicket, markChecked, cancelTicket, cancelWithTrip đã có từ P07 |
| ST-03 | DC-Seat.status | DC-SeatStatus | Thêm markSold() và constructor Seat(seatCode) (P07 chưa có message Booking --> Seat khi phát hành vé) |

### F6.4. Sơ đồ state machine

Ba file: diagrams/P12-state-DC-Booking.drawio, diagrams/P12-state-DC-Ticket.drawio, diagrams/P12-state-DC-Seat.drawio, mỗi file một trang. Style theo Conventions C7 (State, Activity initial, chuyển trạng thái); trạng thái Ticketed, Expired, Cancelled, Sold là trạng thái cuối nghiệp vụ, không vẽ final vì không có sự kiện lưu trữ trong nguồn.

ST-01 DC-Booking

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-01-I | Initial | (initial) | - | DC-Booking | - | 200 | 40 | 40 | 40 |
| ST-01-S1 | State | Draft | - | DC-Booking | status = DRAFT; chưa giữ chỗ, chưa lưu (ASM-44) | 120 | 140 | 200 | 60 |
| ST-01-S2 | State | Held<br>entry / ghi holdStartTime; các Seat sang HELD<br>do / chờ thanh toán tối đa HOLD_DURATION (BR-07) | - | DC-Booking | status = HELD; holdStartTime có giá trị | 80 | 300 | 280 | 100 |
| ST-01-S3 | State | Ticketed<br>entry / phát hành vé; các Seat sang SOLD; ghi paymentReference | - | DC-Booking | status = TICKETED | 20 | 500 | 280 | 90 |
| ST-01-S4 | State | Expired<br>entry / các Seat về AVAILABLE (BR-08) | - | DC-Booking | status = EXPIRED | 400 | 500 | 240 | 80 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn (sự kiện [guard] / hành động) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-01-T1 | ST-01-I | ST-01-S1 | Transition | createBooking(bookingId, trip, travelerInfos) / status = DRAFT | Sự kiện tạo | - |
| ST-01-T2 | ST-01-S1 | ST-01-S2 | Transition | holdSeats(now) [mọi Seat AVAILABLE] / holdStartTime = now | BR-03 | - |
| ST-01-T3 | ST-01-S2 | ST-01-S3 | Transition | issueTickets(paymentReference, idGenerator) / tạo Ticket, Seat.markSold | BR-09, BR-10 | (140,450); (100,450) |
| ST-01-T4 | ST-01-S2 | ST-01-S4 | Transition | releaseSeats() / Seat.release từng chỗ | BR-08; mốc IF-08 | (300,450); (480,450) |

ST-02 DC-Ticket

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-02-I | Initial | (initial) | - | DC-Ticket | - | 200 | 40 | 40 | 40 |
| ST-02-S1 | State | Issued | - | DC-Ticket | status = ISSUED; checkedTime rỗng | 120 | 140 | 200 | 60 |
| ST-02-S2 | State | Checked<br>entry / ghi checkedTime | - | DC-Ticket | status = ISSUED; checkedTime có giá trị | 120 | 300 | 200 | 70 |
| ST-02-S3 | State | Cancelled | - | DC-Ticket | status = CANCELLED | 120 | 500 | 200 | 60 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn (sự kiện [guard] / hành động) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-02-T1 | ST-02-I | ST-02-S1 | Transition | createTicket(...) / status = ISSUED | BR-09, BR-10 | - |
| ST-02-T2 | ST-02-S1 | ST-02-S2 | Transition | markChecked(checkTime) / checkedTime = checkTime | ASM-35 | - |
| ST-02-T3 | ST-02-S1 | ST-02-S3 | Transition | cancelTicket(rate, amount, method) / Seat.release, tạo Refund | ASM-20 | (420,160); (420,520) |
| ST-02-T4 | ST-02-S1 | ST-02-S3 | Transition | cancelWithTrip() | ASM-26 | (480,180); (480,540) |
| ST-02-T5 | ST-02-S2 | ST-02-S3 | Transition | cancelTicket(rate, amount, method) / Seat.release, tạo Refund | ASM-104, Q-74 | - |
| ST-02-T6 | ST-02-S2 | ST-02-S3 | Transition | cancelWithTrip() | ASM-104, Q-74 | (60,340); (60,530) |

ST-03 DC-Seat

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-03-I | Initial | (initial) | - | DC-Seat | - | 200 | 40 | 40 | 40 |
| ST-03-S1 | State | Available | - | DC-Seat | status = AVAILABLE | 120 | 140 | 200 | 60 |
| ST-03-S2 | State | Held<br>entry / gắn với lần đặt qua Booking.seats (R-27) | - | DC-Seat | status = HELD | 120 | 300 | 200 | 70 |
| ST-03-S3 | State | Sold | - | DC-Seat | status = SOLD | 120 | 480 | 200 | 60 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn (sự kiện [guard] / hành động) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-03-T1 | ST-03-I | ST-03-S1 | Transition | create(seatCode) / status = AVAILABLE | Sự kiện tạo | - |
| ST-03-T2 | ST-03-S1 | ST-03-S2 | Transition | hold() | BR-03 | - |
| ST-03-T3 | ST-03-S2 | ST-03-S3 | Transition | markSold() | Bước 4.4 | - |
| ST-03-T4 | ST-03-S2 | ST-03-S1 | Transition | release() [hết thời hạn giữ chỗ] | BR-08 | (60,335); (60,170) |
| ST-03-T5 | ST-03-S3 | ST-03-S1 | Transition | release() [vé của chỗ được trả] | ASM-20 | (400,510); (400,190) |


## F7. Bảng thuộc tính

| DC | Visibility | Tên | Kiểu | Multiplicity | Mặc định | Ràng buộc | Phạm vi | Derived | Nguồn | Mô tả |
|---|---|---|---|---|---|---|---|---|---|---|
| DC-TripOffer | - | tripId | String | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 1 | Mã chuyến để chọn chuyến |
| DC-TripOffer | - | schedule | TripSchedule | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 1 #1, #2 | Tuyến và giờ xuất bến |
| DC-TripOffer | - | busType | BusType | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 1 #3 | Loại xe |
| DC-TripOffer | - | availableSeatCount | Integer | 1 | - | {>= 0, readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 1 #4; BR-03 | Số chỗ còn trống |
| DC-TripOffer | - | ticketPrice | Money | 1 | - | {> 0, readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 1 #5; BR-05 | Giá một vé |
| DC-BookingHold | - | bookingId | String | 1 | - | {readOnly} | Instance | Không | GL-18 | Mã lần đặt |
| DC-BookingHold | - | totalAmount | Money | 1 | - | {> 0, readOnly} | Instance | Không | BR-06 | Tổng tiền phải thanh toán |
| DC-BookingHold | - | holdExpiryTime | LocalDateTime | 1 | - | {readOnly} | Instance | Không | BR-07 | Thời điểm hết thời hạn giữ chỗ |
| DC-BookingHold | - | paymentRequest | PaymentRequestResult | 1 | - | {readOnly} | Instance | Không | P11b IF-01.requestPayment | Kết quả gửi yêu cầu thanh toán (có thể có đích chuyển hướng, Q-83) |
| DC-ReturnQuote | - | ticketInfo | TicketReturnInfo | 1 | - | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #1 đến #4 | Mã vé, tuyến, giờ xuất bến, chỗ, giá vé |
| DC-ReturnQuote | - | timeToDeparture | Duration | 1 | - | {>= 4 giờ, readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #5; BR-12 | Thời gian còn lại trước giờ xuất bến |
| DC-ReturnQuote | - | refundRatePercent | Integer | 1 | - | {50 hoặc 90, readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #6 | Mức hoàn |
| DC-ReturnQuote | - | refundAmount | Money | 1 | - | {>= 0, readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #7 | Số tiền hoàn |
| DC-ReturnReceipt | - | ticketCode | TicketCode | 1 | - | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 2 #1 | Mã vé đã trả |
| DC-ReturnReceipt | - | ticketStatus | TicketStatus | 1 | CANCELLED | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 2 #2 | Trạng thái vé sau khi trả |
| DC-ReturnReceipt | - | refundAmount | Money | 1 | - | {>= 0, readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 2 #3 | Số tiền hoàn |
| DC-ReturnReceipt | - | refundMethod | RefundMethod | 1 | - | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 2 #4 | Hình thức hoàn |
| DC-TicketSalesRuleException | - | reason | TicketSalesRule | 1 | - | {readOnly} | Instance | Không | P04 UC-002, UC-008 luồng thay thế | Quy tắc hoặc luồng gây từ chối |
| DC-Trip | - | tripId | String | 1 | - | {unique, readOnly} | Instance | Không | AC-E-Trip; ASM-24 | Định danh chuyến |
| DC-Trip | - | departureTime | LocalDateTime | 1 | - | {readOnly} | Instance | Không | AC-E-Trip departureTime; GL-10 | Giờ xuất bến gồm cả ngày (GL-10); múi giờ Asia/Ho_Chi_Minh theo Clock của dịch vụ |
| DC-Trip | - | busType | BusType | 1 | - | {readOnly} | Instance | Không | AC-E-Trip busType; GL-21 | Loại xe của chuyến, căn cứ chọn BaseFare và tạo tập chỗ |
| DC-Trip | - | status | TripStatus | 1 | ACTIVE | - | Instance | Không | AC-E-Trip status; ASM-26 | Chuyến chưa huỷ hoặc đã huỷ |
| DC-Trip | - | /availableSeatCount | Integer | 1 | - | {>= 0} | Instance | Có: số Seat có isAvailable() là true | AC-E-Trip availableSeatCount; Q-75 | Không lưu: Seat.status là nguồn duy nhất (Q-75, ASM-42) |
| DC-Route | - | routeId | String | 1 | - | {unique, readOnly} | Instance | Không | AC-E-Route; GL-36 | Định danh tuyến |
| DC-Route | - | departurePoint | String | 1 | - | {không rỗng} | Instance | Không | AC-E-Route departurePoint; P04 UC-002 Dữ liệu vào 1 #1 | Điểm đi |
| DC-Route | - | arrivalPoint | String | 1 | - | {không rỗng} | Instance | Không | AC-E-Route arrivalPoint; P04 UC-002 Dữ liệu vào 1 #2 | Điểm đến |
| DC-Seat | - | seatCode | String | 1 | - | {readOnly, unique trong chuyến} | Instance | Không | AC-E-Seat seatCode; GL-02 | Mã chỗ trên sơ đồ chỗ, ví dụ A05 |
| DC-Seat | - | status | SeatStatus | 1 | AVAILABLE | - | Instance | Không | AC-E-Seat status; ST-03; ASM-42 | Trạng thái chỗ theo state machine ST-03 |
| DC-BaseFare | - | baseFareId | String | 1 | - | {unique, readOnly} | Instance | Không | AC-E-BaseFare; GL-09 | Định danh mức giá |
| DC-BaseFare | - | busType | BusType | 1 | - | {readOnly} | Instance | Không | AC-E-BaseFare busType; BR-04 | Loại xe mà mức giá áp dụng |
| DC-BaseFare | - | amount | Money | 1 | - | {> 0} | Instance | Không | AC-E-BaseFare amount; GL-09 | Mức giá theo tuyến và loại xe (đồng) |
| DC-HolidaySurcharge | - | holidaySurchargeId | String | 1 | - | {unique, readOnly} | Instance | Không | AC-E-HolidaySurcharge; GL-25 | Định danh mức tăng |
| DC-HolidaySurcharge | - | startDate | LocalDate | 1 | - | {readOnly} | Instance | Không | AC-E-HolidaySurcharge startDate | Ngày đầu của khoảng ngày (tính cả ngày này, ASM-105) |
| DC-HolidaySurcharge | - | endDate | LocalDate | 1 | - | {readOnly, >= startDate} | Instance | Không | AC-E-HolidaySurcharge endDate | Ngày cuối của khoảng ngày (tính cả ngày này, ASM-105) |
| DC-HolidaySurcharge | - | ratePercent | Integer | 1 | - | {0..30} | Instance | Không | AC-E-HolidaySurcharge ratePercent; BR-32 | Mức tăng theo phần trăm, tối đa 30% (BR-32) |
| DC-TripSchedule | - | routeName | String | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 1 #1 | <Điểm đi> - <Điểm đến> |
| DC-TripSchedule | - | departureTime | LocalDateTime | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 1 #2 | Giờ xuất bến gồm ngày |
| DC-SeatAlreadyHeldException | - | seatCode | String | 0..1 | - | {readOnly} | Instance | Không | P11b IF-10.saveTrip | Mã chỗ vi phạm khi biết |
| DC-Booking | - | bookingId | String | 1 | - | {unique, readOnly} | Instance | Không | GL-18; IF-11.findBooking | Định danh lần đặt |
| DC-Booking | - | ticketPrice | Money | 0..1 | - | {> 0} | Instance | Không | BR-05; ASM-22 | Giá một vé chốt lúc calculateTotal, là giá khách đã trả dùng cho mọi vé của lần đặt |
| DC-Booking | - | totalAmount | Money | 0..1 | - | {= ticketPrice x số chỗ} | Instance | Không | AC-E-Booking totalAmount; BR-06 | Tổng tiền của lần đặt; giữ lại sau khi giá thay đổi |
| DC-Booking | - | holdStartTime | LocalDateTime | 0..1 | - | {có khi status khác DRAFT} | Instance | Không | AC-E-Booking holdStartTime; BR-07 | Thời điểm bắt đầu giữ chỗ |
| DC-Booking | - | status | BookingStatus | 1 | DRAFT | - | Instance | Không | AC-E-Booking status; ST-01 | Trạng thái lần đặt theo state machine ST-01 |
| DC-Booking | - | travelerInfos | List<TravelerInfo> | 1..* | - | {mỗi seatCode một phần tử} | Instance | Không | AC-E-Booking travelerInfos; ASM-43 | Họ tên, số điện thoại người đi của từng chỗ; kiểm BR-01 bằng isWithinSeatLimit |
| DC-Booking | - | paymentAttemptCount | Integer | 1 | 0 | {>= 0} | Instance | Không | Thiết kế: IF-01.requestPayment cần khoá idempotency mỗi lần thanh toán (P11b) | Số lần đã gửi yêu cầu thanh toán; Tạm vì UC-003 chưa phân tích (ASM-100) |
| DC-Booking | - | paymentReference | PaymentReference | 0..1 | - | {có khi TICKETED} | Instance | Không | ASM-41; P09 F7 | Mã tham chiếu giao dịch của cổng, lưu để hoàn tiền |
| DC-Booking | - | MAX_SEATS | Integer | 1 | 5 | {readOnly} | Classifier | Không | BR-01 | Số chỗ tối đa của một lần đặt trực tuyến |
| DC-Booking | - | HOLD_DURATION | Duration | 1 | 10 phút | {readOnly} | Classifier | Không | BR-07 | Thời hạn giữ chỗ |
| DC-Ticket | - | ticketCode | TicketCode | 1 | - | {unique, readOnly} | Instance | Không | AC-E-Ticket ticketCode; BR-10 | Mã vé duy nhất trên toàn hệ thống |
| DC-Ticket | - | travelerName | String | 1 | - | {không rỗng} | Instance | Không | AC-E-Ticket travelerName | Họ tên người đi |
| DC-Ticket | - | travelerPhone | PhoneNumber | 1 | - | {10 chữ số, bắt đầu bằng 0 (ASM-15)} | Instance | Không | AC-E-Ticket travelerPhone | Số điện thoại người đi nhận vé qua SMS |
| DC-Ticket | - | price | Money | 1 | - | {> 0, readOnly} | Instance | Không | AC-E-Ticket price; ASM-22 | Số tiền đã thanh toán cho vé, là cơ sở tính số tiền hoàn |
| DC-Ticket | - | status | TicketStatus | 1 | ISSUED | - | Instance | Không | AC-E-Ticket status; ST-02 | Vé còn hiệu lực hay đã huỷ |
| DC-Ticket | - | purchaseChannel | PurchaseChannel | 1 | - | {readOnly} | Instance | Không | AC-E-Ticket purchaseChannel; GL-13 | Kênh mua: ONLINE hoặc COUNTER |
| DC-Ticket | - | checkedTime | LocalDateTime | 0..1 | - | {có khi đã soát} | Instance | Không | AC-E-Ticket checkedTime; ASM-35 | Thời điểm soát vé khi vé hợp lệ được ghi nhận |
| DC-TicketReturnPolicy | - | MIN_RETURN_TIME | Duration | 1 | 4 giờ | {readOnly} | Classifier | Không | BR-12 | Thời gian còn lại tối thiểu để được trả vé |
| DC-TicketReturnPolicy | - | FULL_RATE_TIME | Duration | 1 | 24 giờ | {readOnly} | Classifier | Không | BR-13, BR-14 | Từ mốc này trở lên hoàn mức cao |
| DC-TicketReturnPolicy | - | HIGH_RATE_PERCENT | Integer | 1 | 90 | {readOnly} | Classifier | Không | BR-13 | Mức hoàn khi còn từ 24 giờ trở lên |
| DC-TicketReturnPolicy | - | LOW_RATE_PERCENT | Integer | 1 | 50 | {readOnly} | Classifier | Không | BR-14 | Mức hoàn khi còn từ 4 giờ đến dưới 24 giờ |
| DC-TicketReturnPolicy | - | TRIP_CANCEL_RATE_PERCENT | Integer | 1 | 100 | {readOnly} | Classifier | Không | BR-17 | Mức hoàn khi chuyến bị nhà xe huỷ |
| DC-Refund | - | refundAmount | Money | 1 | - | {>= 0, readOnly} | Instance | Không | AC-E-Refund refundAmount; BR-13, BR-14, BR-17 | Số tiền hoàn cho khách |
| DC-Refund | - | refundRatePercent | Integer | 1 | - | {0..100, readOnly} | Instance | Không | AC-E-Refund refundRate; GL-24 | Mức hoàn theo phần trăm giá vé |
| DC-Refund | - | refundMethod | RefundMethod | 1 | - | {readOnly} | Instance | Không | AC-E-Refund refundMethod; BR-15, BR-16 | Hình thức hoàn |
| DC-Refund | - | refundOutcome | RefundOutcome | 1 | - | - | Instance | Không | AC-E-Refund refundResult; ASM-54 | Kết quả hoàn: đã hoàn, chưa thành công hoặc chờ chi tiền mặt |
| DC-PhoneReservation | - | reservationId | String | 1 | - | {unique, readOnly} | Instance | Không | GL-07 | Định danh đặt chỗ qua điện thoại |
| DC-PhoneReservation | - | status | PhoneReservationStatus | 1 | UNPAID | - | Instance | Không | AC-E-PhoneReservation status; GL-07, ASM-27 | Chưa thanh toán, đã thanh toán tại quầy hoặc đã huỷ |
| DC-TravelerInfo | - | seatCode | String | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu vào 2 #1 | Mã chỗ của người đi |
| DC-TravelerInfo | - | travelerName | String | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu vào 2 #2 | Họ tên người đi, có thể rỗng khi hành khách bỏ trống |
| DC-TravelerInfo | - | travelerPhone | String | 1 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu vào 2 #3 | Số điện thoại thô |
| DC-BookingSummary | - | tickets | List<Ticket> | 1..5 | - | {readOnly} | Instance | Không | P04 UC-002 Dữ liệu ra 4 | Các vé đã phát hành |
| DC-BookingSummary | - | totalAmount | Money | 1 | - | {readOnly} | Instance | Không | BR-06; Dữ liệu ra 4 #7 | Tổng tiền của lần đặt |
| DC-TicketCheckResult | - | outcome | CheckOutcome | 1 | - | {readOnly} | Instance | Không | BR-20, BR-21, BR-22 | Kết luận soát |
| DC-TicketCheckResult | - | ticketCode | TicketCode | 1 | - | {readOnly} | Instance | Không | P04 UC-015 Dữ liệu ra 2 | Mã vé |
| DC-TicketCheckResult | - | seatCode | String | 0..1 | - | {readOnly} | Instance | Không | P04 UC-015 Dữ liệu ra 2 | Mã chỗ, rỗng khi sai chuyến |
| DC-TicketCheckResult | - | travelerName | String | 0..1 | - | {readOnly} | Instance | Không | P04 UC-015 Dữ liệu ra 2 | Họ tên người đi khi hợp lệ |
| DC-TicketCheckResult | - | previousCheckedTime | LocalDateTime | 0..1 | - | {readOnly} | Instance | Không | BR-22 | Thời điểm soát trước khi vé đã soát |
| DC-RefundQuote | - | ratePercent | Integer | 1 | - | {50 hoặc 90, readOnly} | Instance | Không | BR-13, BR-14 | Mức hoàn theo phần trăm |
| DC-RefundQuote | - | amount | Money | 1 | - | {>= 0, readOnly} | Instance | Không | BR-13, BR-14; ASM-22 | Số tiền hoàn |
| DC-TicketReturnInfo | - | ticketCode | TicketCode | 1 | - | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #1 | Mã vé |
| DC-TicketReturnInfo | - | schedule | TripSchedule | 1 | - | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #2 | Tuyến và giờ xuất bến |
| DC-TicketReturnInfo | - | seatCode | String | 1 | - | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #3 | Mã chỗ |
| DC-TicketReturnInfo | - | price | Money | 1 | - | {readOnly} | Instance | Không | P04 UC-008 Dữ liệu ra 1 #4 | Giá vé đã thanh toán |
| DC-CancelImpactInfo | - | purchaseChannel | PurchaseChannel | 1 | - | {readOnly} | Instance | Không | P04 UC-013 Dữ liệu ra 1 | Kênh mua của vé |
| DC-CancelImpactInfo | - | refundAmount | Money | 1 | - | {readOnly} | Instance | Không | BR-17 | Số tiền hoàn bằng 100% giá vé |
| DC-CancellationSummary | - | schedule | TripSchedule | 1 | - | {readOnly} | Instance | Không | P04 UC-013 Dữ liệu ra 1 #1 | Tuyến và giờ xuất bến |
| DC-CancellationSummary | - | onlineTicketCount | Integer | 1 | - | {>= 0, readOnly} | Instance | Không | P04 UC-013 Dữ liệu ra 1 | Số vé còn hiệu lực mua trực tuyến |
| DC-CancellationSummary | - | counterTicketCount | Integer | 1 | - | {>= 0, readOnly} | Instance | Không | P04 UC-013 Dữ liệu ra 1 | Số vé còn hiệu lực mua tại quầy |
| DC-CancellationSummary | - | unpaidReservationCount | Integer | 1 | - | {>= 0, readOnly} | Instance | Không | P04 UC-013 Dữ liệu ra 1; ASM-27 | Số đặt chỗ qua điện thoại chưa thanh toán |
| DC-CancellationSummary | - | totalRefundAmount | Money | 1 | - | {>= 0, readOnly} | Instance | Không | BR-17 | Tổng số tiền hoàn của các vé còn hiệu lực |

### F7a. Giá trị của enumeration

| DC | Giá trị | Ý nghĩa và nguồn |
|---|---|---|
| DC-TicketSalesRule | TRIP_NOT_FOUND | Không có chuyến với mã đã chọn |
| DC-TicketSalesRule | NO_SEAT_LEFT | Chuyến không còn chỗ trống nào (luồng 4a, BR-03) |
| DC-TicketSalesRule | SEAT_LIMIT_EXCEEDED | Quá 5 chỗ một lần đặt (luồng 6a, BR-01) |
| DC-TicketSalesRule | SEATS_UNAVAILABLE | Có chỗ không còn trống (luồng 6b, BR-02, BR-03; Q-106) |
| DC-TicketSalesRule | MISSING_TRAVELER_INFO | Thiếu họ tên hoặc số điện thoại người đi (luồng 7a) |
| DC-TicketSalesRule | INVALID_PHONE | Số điện thoại người đi sai định dạng (luồng 7b, ASM-15) |
| DC-TicketSalesRule | HOLD_EXPIRED | Lần đặt đã hết thời hạn giữ chỗ (luồng 9a, BR-08) |
| DC-TicketSalesRule | TICKET_NOT_FOUND | Không có vé khớp thông tin (luồng 2a của UC-008) |
| DC-TicketSalesRule | TICKET_CANCELLED | Vé đã huỷ (luồng 2b của UC-008, ASM-20) |
| DC-TicketSalesRule | WRONG_CHANNEL | Vé mua qua kênh khác kênh yêu cầu trả (luồng 3a, BR-11) |
| DC-TicketSalesRule | RETURN_TIME_LIMIT | Còn dưới 4 giờ trước giờ xuất bến (luồng 3b, BR-12) |
| DC-TicketSalesRule | REFUND_AMOUNT_CHANGED | Số tiền hoàn lúc xác nhận khác số đã hiển thị (ASM-106) |
| DC-TicketSalesRule | REFUND_FAILED | Hoàn tiền qua cổng không thành công hoặc không rõ, vé giữ nguyên (luồng 9a của UC-008, ASM-21, ASM-107) |
| DC-TripStatus | ACTIVE | Chuyến chưa huỷ (GL-04) |
| DC-TripStatus | CANCELLED | Chuyến đã huỷ (GL-04, ASM-26) |
| DC-SeatStatus | AVAILABLE | Còn trống (BR-03, GL-03) |
| DC-SeatStatus | HELD | Đang giữ cho một lần đặt (GL-11) |
| DC-SeatStatus | SOLD | Đã có vé còn hiệu lực |
| DC-BusType | SLEEPER_40 | Giường nằm 40 chỗ (GL-21) |
| DC-BusType | SEATER_29 | Ghế ngồi 29 chỗ (GL-21) |
| DC-BookingStatus | DRAFT | Mới lập, chưa giữ chỗ, chưa lưu (ASM-44) |
| DC-BookingStatus | HELD | Đang giữ chỗ chờ thanh toán (BR-07) |
| DC-BookingStatus | TICKETED | Đã thanh toán, vé đã phát hành (BR-09) |
| DC-BookingStatus | EXPIRED | Hết thời hạn giữ chỗ, chỗ đã trả (BR-08) |
| DC-TicketStatus | ISSUED | Đã phát hành, còn hiệu lực (GL-38) |
| DC-TicketStatus | CANCELLED | Đã huỷ (GL-39) |
| DC-PurchaseChannel | ONLINE | Trực tuyến (GL-13) |
| DC-PurchaseChannel | COUNTER | Tại quầy (GL-13) |
| DC-RefundMethod | VIA_GATEWAY | Qua cổng thanh toán (BR-15) |
| DC-RefundMethod | CASH_AT_COUNTER | Tiền mặt tại quầy (BR-16) |
| DC-RefundOutcome | REFUNDED | Đã hoàn, cổng xác nhận (GL-16) |
| DC-RefundOutcome | FAILED | Chưa thành công (ASM-31) |
| DC-RefundOutcome | AWAITING_CASH_PAYOUT | Chờ chi tiền mặt tại quầy (ASM-28) |
| DC-PhoneReservationStatus | UNPAID | Chưa thanh toán, đang giữ chỗ (GL-07) |
| DC-PhoneReservationStatus | PAID | Đã thanh toán tại quầy, thành vé (GL-07); UC-005 sẽ đặt |
| DC-PhoneReservationStatus | CANCELLED | Đã huỷ (GL-07) |
| DC-TravelerInfoProblem | NONE | Thông tin đủ và hợp lệ |
| DC-TravelerInfoProblem | MISSING_INFO | Thiếu họ tên hoặc số điện thoại của ít nhất một chỗ (luồng 7a) |
| DC-TravelerInfoProblem | INVALID_PHONE | Có số điện thoại sai định dạng (luồng 7b, ASM-15) |
| DC-CheckOutcome | VALID | Hợp lệ |
| DC-CheckOutcome | CANCELLED_TICKET | Không hợp lệ, vé đã huỷ (BR-21) |
| DC-CheckOutcome | ALREADY_CHECKED | Không hợp lệ, vé đã soát (BR-22) |
| DC-CheckOutcome | WRONG_TRIP | Không hợp lệ, sai chuyến (BR-20) |

## F8. Class diagram

| Sơ đồ | Phạm vi (PKG / UC) | File .drawio | Số lớp |
|---|---|---|---|
| Class diagram PKG-09 | PKG-09 TicketSalesService | diagrams/P12-class-PKG-09.drawio (trang PKG-09 TicketSalesService) | 9 lớp trong package, 8 tham chiếu |
| Class diagram PKG-22 | PKG-22 TripCatalog | diagrams/P12-class-PKG-22.drawio (trang PKG-22 TripCatalog) | 12 lớp trong package, 3 tham chiếu |
| Class diagram PKG-23 lớp lõi | PKG-23 Ticketing | diagrams/P12-class-PKG-23.drawio (trang PKG-23 Ticketing - lớp lõi) | 9 lớp trong package, 2 tham chiếu |
| Class diagram PKG-23 kiểu dữ liệu | PKG-23 Ticketing | diagrams/P12-class-PKG-23.drawio (trang PKG-23 Ticketing - kiểu dữ liệu) | 15 lớp trong package, 0 tham chiếu |
| Class diagram tham gia UC-002 | UC-002 (PKG-09, PKG-22, PKG-23) | diagrams/P12-class-UC-002.drawio | 17 lớp, ngăn ẩn bớt ghi ... |
| Class diagram tham gia UC-008 | UC-008 (PKG-09, PKG-22, PKG-23) | diagrams/P12-class-UC-008.drawio | 9 lớp, ngăn ẩn bớt ghi ... |

Class diagram theo UC chỉ vẽ cho UC-002 và UC-008, hai UC có control trong phạm vi; UC-013 (control ở PKG-10) và UC-015 (control ở PKG-11) vẽ ở lần chạy của các package đó. Ngăn operation của sơ đồ UC chỉ giữ operation có nguồn là UC đó (cột Nguồn của F2), ngăn thuộc tính ghi ...; lớp tham chiếu chỉ ghi tên. Trên sơ đồ package, interface của subsystem (IF-01, IF-02, IF-03, IF-07, IF-08) và lớp ngoài package chỉ ghi tên; dependency tới entity của package khác từ control (R-04, R-05, R-06, R-10, R-42, R-50, R-67) liệt kê ở F5, không vẽ ở sơ đồ PKG-09.

### Sơ đồ PKG-09

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| IF-08 | Interface | ITriggerHandler | «interface» | PKG-19 | tham chiếu | 60 | 40 | 200 | 40 |
| IF-02 | Interface | IPaymentResultListener | «interface» | PKG-15 | tham chiếu | 600 | 40 | 220 | 40 |
| DC-BookTicketOnlineService | Class | BookTicketOnlineService | «control» | PKG-09 | trong package | 60 | 160 | 460 | 290 |
| DC-PayTicketOnlineService | Class | PayTicketOnlineService | «control» | PKG-09 | trong package | 600 | 160 | 460 | 130 |
| DC-ReturnTicketService | Class | ReturnTicketService | «control» | PKG-09 | trong package | 1140 | 160 | 460 | 180 |
| IF-03 | Interface | ISmsSender | «interface» | PKG-16 | tham chiếu | 60 | 630 | 200 | 40 |
| IF-07 | Interface | ITriggerScheduler | «interface» | PKG-19 | tham chiếu | 340 | 630 | 200 | 40 |
| IF-15 | Interface | ITicketingIdGenerator | «interface» | PKG-23 | tham chiếu | 620 | 630 | 210 | 40 |
| IF-10 | Interface | ITripCatalogRepository | «interface» | PKG-22 | tham chiếu | 910 | 630 | 220 | 40 |
| IF-11 | Interface | ITicketingRepository | «interface» | PKG-23 | tham chiếu | 1210 | 630 | 200 | 40 |
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-15 | tham chiếu | 1490 | 630 | 200 | 40 |
| DC-TripOffer | Class | TripOffer | «value object» | PKG-09 | trong package | 60 | 730 | 330 | 130 |
| DC-BookingHold | Class | BookingHold | «value object» | PKG-09 | trong package | 470 | 730 | 350 | 120 |
| DC-ReturnQuote | Class | ReturnQuote | «value object» | PKG-09 | trong package | 900 | 730 | 360 | 120 |
| DC-ReturnReceipt | Class | ReturnReceipt | «value object» | PKG-09 | trong package | 1340 | 730 | 360 | 120 |
| DC-TicketSalesRuleException | Class | TicketSalesRuleException | «exception» | PKG-09 | trong package | 1780 | 730 | 260 | 110 |
| DC-TicketSalesRule | Enumeration | TicketSalesRule | «enumeration» | PKG-09 | trong package | 2120 | 730 | 240 | 260 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-43 | DC-BookTicketOnlineService | IF-08 | Realization | - | A --> B | (290,110); (160,110) |
| R-46 | DC-PayTicketOnlineService | IF-02 | Realization | - | A --> B | (830,120); (710,120) |
| R-03 | DC-BookTicketOnlineService | DC-PayTicketOnlineService | Association | đầu A: 1; đầu B: payService 1 | A --> B | (290,480); (690,480) |
| R-47 | DC-PayTicketOnlineService | DC-BookTicketOnlineService | Association | đầu A: 1; đầu B: bookingCompletion 1 | A --> B | (780,490); (350,490) |
| R-02 | DC-BookTicketOnlineService | IF-03 | Association | đầu A: 1; đầu B: smsSender 1 | A --> B | (120,500); (160,500) |
| R-38 | DC-BookTicketOnlineService | IF-10 | Association | đầu A: 1; đầu B: tripCatalog 1 | A --> B | (400,510); (980,510) |
| R-39 | DC-BookTicketOnlineService | IF-11 | Association | đầu A: 1; đầu B: ticketing 1 | A --> B | (460,520); (1260,520) |
| R-40 | DC-BookTicketOnlineService | IF-07 | Association | đầu A: 1; đầu B: scheduler 1 | A --> B | (180,530); (440,530) |
| R-41 | DC-BookTicketOnlineService | IF-15 | Association | đầu A: 1; đầu B: idGenerator 1 | A --> B | (230,540); (720,540) |
| R-44 | DC-PayTicketOnlineService | IF-01 | Association | đầu A: 1; đầu B: paymentGateway 1 | A --> B | (970,550); (1560,550) |
| R-45 | DC-PayTicketOnlineService | IF-11 | Association | đầu A: 1; đầu B: ticketing 1 | A --> B | (880,560); (1310,560) |
| R-48 | DC-ReturnTicketService | IF-11 | Association | đầu A: 1; đầu B: ticketing 1 | A --> B | (1370,570); (1360,570) |
| R-49 | DC-ReturnTicketService | IF-10 | Association | đầu A: 1; đầu B: tripCatalog 1 | A --> B | (1260,580); (1060,580) |
| R-09 | DC-ReturnTicketService | IF-01 | Association | đầu A: 1; đầu B: paymentGateway 1 | A --> B | (1480,590); (1620,590) |

### Sơ đồ PKG-22

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-Booking | Class | Booking | «entity» | PKG-23 | tham chiếu | 70 | 40 | 200 | 40 |
| DC-Ticket | Class | Ticket | «entity» | PKG-23 | tham chiếu | 350 | 40 | 200 | 40 |
| DC-PhoneReservation | Class | PhoneReservation | «entity» | PKG-23 | tham chiếu | 630 | 40 | 200 | 40 |
| IF-10 | Interface | ITripCatalogRepository | «interface» | PKG-22 | trong package | 910 | 40 | 460 | 130 |
| DC-Trip | Class | Trip | «entity» | PKG-22 | trong package | 70 | 310 | 460 | 390 |
| DC-Seat | Class | Seat | «entity» | PKG-22 | trong package | 610 | 310 | 350 | 200 |
| DC-Route | Class | Route | «entity» | PKG-22 | trong package | 70 | 820 | 460 | 170 |
| DC-BaseFare | Class | BaseFare | «entity» | PKG-22 | trong package | 610 | 820 | 460 | 170 |
| DC-HolidaySurcharge | Class | HolidaySurcharge | «entity» | PKG-22 | trong package | 1150 | 820 | 460 | 190 |
| DC-SeatAlreadyHeldException | Class | SeatAlreadyHeldException | «exception» | PKG-22 | trong package | 1690 | 820 | 260 | 110 |
| DC-InvalidStateException | Class | InvalidStateException | «exception» | PKG-22 | trong package | 70 | 1080 | 240 | 40 |
| DC-TripSchedule | Class | TripSchedule | «value object» | PKG-22 | trong package | 390 | 1080 | 300 | 80 |
| DC-TripStatus | Enumeration | TripStatus | «enumeration» | PKG-22 | trong package | 770 | 1080 | 240 | 80 |
| DC-SeatStatus | Enumeration | SeatStatus | «enumeration» | PKG-22 | trong package | 1090 | 1080 | 240 | 100 |
| DC-BusType | Enumeration | BusType | «enumeration» | PKG-22 | trong package | 1410 | 1080 | 240 | 80 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-26 | DC-Booking | DC-Trip | Association | đầu A: 0..*; đầu B: trip 1 | A --> B | (140,200); (160,200) |
| R-27 | DC-Booking | DC-Seat | Association | đầu A: 0..1; đầu B: seats 1..5 | A --> B | (200,210); (700,210) |
| R-29 | DC-Ticket | DC-Trip | Association | đầu A: 0..*; đầu B: trip 1 | A --> B | (420,220); (250,220) |
| R-30 | DC-Ticket | DC-Seat | Association | đầu A: 0..*; đầu B: seat 1 | A --> B | (480,230); (790,230) |
| R-33 | DC-Trip | DC-PhoneReservation | Association | đầu A: trip 1; đầu B: 0..* | B --> A | (350,240); (700,240) |
| R-37 | DC-PhoneReservation | DC-Seat | Association | đầu A: 0..1; đầu B: seat Q-76 | A --> B | (760,250); (870,250) |
| R-53 | IF-10 | DC-Trip | Dependency | - | A --> B | (1060,260); (440,260) |
| R-23 | DC-Trip | DC-Seat | Composition | đầu A: 1; đầu B: seats 1..* | A --> B | (250,730); (730,730) |
| R-22 | DC-Trip | DC-Route | Association | đầu A: 0..*; đầu B: route 1 | A --> B | (160,740); (300,740) |
| R-24 | DC-Trip | DC-BaseFare | Association | đầu A: 0..*; đầu B: baseFare 1 | A --> B | (350,750); (840,750) |
| R-25 | DC-Trip | DC-HolidaySurcharge | Association | đầu A: 0..*; đầu B: holidaySurcharge 0..1 | A --> B | (440,760); (1380,760) |
| R-31 | DC-BaseFare | DC-Route | Association | đầu A: 0..*; đầu B: route 1 | A --> B | (840,1040); (300,1040) |
| R-65 | DC-Seat | DC-SeatAlreadyHeldException | Dependency | - | A --> B | (840,770); (1780,770) |
| R-66 | IF-10 | DC-SeatAlreadyHeldException | Dependency | - | A --> B | (1220,270); (40,270); (40,780); (1860,780) |

### Sơ đồ PKG-23 lớp lõi

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| IF-15 | Interface | ITicketingIdGenerator | «interface» | PKG-23 | trong package | 60 | 40 | 240 | 80 |
| IF-11 | Interface | ITicketingRepository | «interface» | PKG-23 | trong package | 380 | 40 | 460 | 200 |
| DC-Booking | Class | Booking | «entity» | PKG-23 | trong package | 60 | 350 | 460 | 520 |
| DC-Ticket | Class | Ticket | «entity» | PKG-23 | trong package | 600 | 350 | 460 | 470 |
| DC-PhoneReservation | Class | PhoneReservation | «entity» | PKG-23 | trong package | 1140 | 350 | 370 | 150 |
| DC-TripCancellation | Class | TripCancellation | «entity» | PKG-23 | trong package | 1590 | 350 | 460 | 120 |
| DC-Trip | Class | Trip | «entity» | PKG-22 | tham chiếu | 60 | 1070 | 200 | 40 |
| DC-Seat | Class | Seat | «entity» | PKG-22 | tham chiếu | 340 | 1070 | 200 | 40 |
| DC-Refund | Class | Refund | «entity» | PKG-23 | trong package | 620 | 1070 | 460 | 170 |
| DC-TicketReturnPolicy | Class | TicketReturnPolicy | «entity» | PKG-23 | trong package | 1160 | 1070 | 460 | 330 |
| DC-TicketSmsContent | Class | TicketSmsContent | «entity» | PKG-23 | trong package | 1700 | 1070 | 460 | 130 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-54 | IF-11 | DC-Booking | Dependency | - | A --> B | (470,270); (370,270) |
| R-55 | IF-11 | DC-Ticket | Dependency | - | A --> B | (560,280); (830,280) |
| R-56 | IF-11 | DC-PhoneReservation | Dependency | - | A --> B | (660,290); (1320,290) |
| R-57 | IF-11 | DC-TripCancellation | Dependency | - | A --> B | (750,300); (1820,300) |
| R-64 | DC-Booking | IF-15 | Dependency | - | A --> B | (210,310); (180,310) |
| R-26 | DC-Booking | DC-Trip | Association | đầu A: 0..*; đầu B: trip 1 | A --> B | (180,900); (100,900) |
| R-27 | DC-Booking | DC-Seat | Association | đầu A: 0..1; đầu B: seats 1..5 | A --> B | (290,910); (390,910) |
| R-28 | DC-Booking | DC-Ticket | Association | đầu A: 0..1; đầu B: tickets 0..5 | A --> B | (400,920); (720,920) |
| R-29 | DC-Ticket | DC-Trip | Association | đầu A: 0..*; đầu B: trip 1 | A --> B | (660,930); (140,930) |
| R-30 | DC-Ticket | DC-Seat | Association | đầu A: 0..*; đầu B: seat 1 | A --> B | (770,940); (440,940) |
| R-32 | DC-Ticket | DC-Refund | Composition | đầu A: 1; đầu B: refund 0..1 | A --> B | (830,950); (850,950) |
| R-33 | DC-Trip | DC-PhoneReservation | Association | đầu A: trip 1; đầu B: 0..* | B --> A | (180,960); (1230,960) |
| R-37 | DC-PhoneReservation | DC-Seat | Association | đầu A: 0..1; đầu B: seat Q-76 | A --> B | (1320,970); (490,970) |
| R-58 | DC-TripCancellation | DC-Trip | Association | đầu A: 1; đầu B: trip 1 | A --> B | (1680,980); (220,980) |
| R-59 | DC-TripCancellation | DC-Ticket | Association | đầu A: 1; đầu B: tickets 0..* | A --> B | (1770,990); (940,990) |
| R-60 | DC-TripCancellation | DC-PhoneReservation | Association | đầu A: 1; đầu B: phoneReservations 0..* | A --> B | (1870,1000); (1420,1000) |
| R-61 | DC-TripCancellation | DC-TicketReturnPolicy | Association | đầu A: 1; đầu B: policy 1 | A --> B | (1960,1010); (1470,1010) |
| R-62 | DC-TicketReturnPolicy | DC-Ticket | Dependency | - | A --> B | (1310,1020); (890,1020) |
| R-63 | DC-TicketSmsContent | DC-Ticket | Dependency | - | A --> B | (1930,1030); (1000,1030) |

### Sơ đồ PKG-23 kiểu dữ liệu

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-TravelerInfo | Class | TravelerInfo | «value object» | PKG-23 | trong package | 60 | 40 | 250 | 100 |
| DC-BookingSummary | Class | BookingSummary | «value object» | PKG-23 | trong package | 390 | 40 | 290 | 80 |
| DC-TicketCheckResult | Class | TicketCheckResult | «value object» | PKG-23 | trong package | 760 | 40 | 370 | 130 |
| DC-RefundQuote | Class | RefundQuote | «value object» | PKG-23 | trong package | 1210 | 40 | 320 | 80 |
| DC-TicketReturnInfo | Class | TicketReturnInfo | «value object» | PKG-23 | trong package | 60 | 230 | 260 | 120 |
| DC-CancelImpactInfo | Class | CancelImpactInfo | «value object» | PKG-23 | trong package | 400 | 230 | 320 | 80 |
| DC-CancellationSummary | Class | CancellationSummary | «value object» | PKG-23 | trong package | 800 | 230 | 350 | 130 |
| DC-BookingStatus | Enumeration | BookingStatus | «enumeration» | PKG-23 | trong package | 60 | 420 | 240 | 120 |
| DC-TicketStatus | Enumeration | TicketStatus | «enumeration» | PKG-23 | trong package | 380 | 420 | 240 | 80 |
| DC-PurchaseChannel | Enumeration | PurchaseChannel | «enumeration» | PKG-23 | trong package | 700 | 420 | 240 | 80 |
| DC-RefundMethod | Enumeration | RefundMethod | «enumeration» | PKG-23 | trong package | 1020 | 420 | 240 | 80 |
| DC-RefundOutcome | Enumeration | RefundOutcome | «enumeration» | PKG-23 | trong package | 60 | 600 | 240 | 100 |
| DC-PhoneReservationStatus | Enumeration | PhoneReservationStatus | «enumeration» | PKG-23 | trong package | 380 | 600 | 240 | 100 |
| DC-TravelerInfoProblem | Enumeration | TravelerInfoProblem | «enumeration» | PKG-23 | trong package | 700 | 600 | 240 | 100 |
| DC-CheckOutcome | Enumeration | CheckOutcome | «enumeration» | PKG-23 | trong package | 1020 | 600 | 240 | 120 |

Edge: không có (trang chỉ liệt kê kiểu dữ liệu; thuộc tính kiểu value object, enumeration không vẽ cạnh).

### Sơ đồ UC-002

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| IF-08 | Interface | ITriggerHandler | «interface» | PKG-19 | tham chiếu | 90 | 40 | 200 | 40 |
| IF-02 | Interface | IPaymentResultListener | «interface» | PKG-15 | tham chiếu | 630 | 40 | 220 | 40 |
| DC-BookTicketOnlineService | Class | BookTicketOnlineService | «control» | PKG-09 | trong package | 90 | 160 | 460 | 240 |
| DC-PayTicketOnlineService | Class | PayTicketOnlineService | «control» | PKG-09 | trong package | 630 | 160 | 460 | 120 |
| IF-03 | Interface | ISmsSender | «interface» | PKG-16 | tham chiếu | 90 | 570 | 200 | 40 |
| IF-07 | Interface | ITriggerScheduler | «interface» | PKG-19 | tham chiếu | 370 | 570 | 200 | 40 |
| IF-15 | Interface | ITicketingIdGenerator | «interface» | PKG-23 | tham chiếu | 650 | 570 | 210 | 40 |
| IF-10 | Interface | ITripCatalogRepository | «interface» | PKG-22 | tham chiếu | 940 | 570 | 220 | 40 |
| IF-11 | Interface | ITicketingRepository | «interface» | PKG-23 | tham chiếu | 1240 | 570 | 200 | 40 |
| DC-TicketSmsContent | Class | TicketSmsContent | «entity» | PKG-23 | trong package | 1520 | 570 | 320 | 80 |
| DC-Booking | Class | Booking | «entity» | PKG-23 | trong package | 90 | 750 | 460 | 280 |
| DC-Ticket | Class | Ticket | «entity» | PKG-23 | trong package | 630 | 750 | 460 | 160 |
| DC-Trip | Class | Trip | «entity» | PKG-22 | trong package | 90 | 1150 | 370 | 200 |
| DC-Seat | Class | Seat | «entity» | PKG-22 | trong package | 540 | 1150 | 240 | 170 |
| DC-Route | Class | Route | «entity» | PKG-22 | trong package | 90 | 1450 | 240 | 120 |
| DC-BaseFare | Class | BaseFare | «entity» | PKG-22 | trong package | 410 | 1450 | 420 | 120 |
| DC-HolidaySurcharge | Class | HolidaySurcharge | «entity» | PKG-22 | trong package | 910 | 1450 | 370 | 120 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-43 | DC-BookTicketOnlineService | IF-08 | Realization | - | A --> B | (320,110); (190,110) |
| R-46 | DC-PayTicketOnlineService | IF-02 | Realization | - | A --> B | (860,120); (740,120) |
| R-03 | DC-BookTicketOnlineService | DC-PayTicketOnlineService | Association | đầu A: 1; đầu B: payService 1 | A --> B | (320,430); (780,430) |
| R-47 | DC-PayTicketOnlineService | DC-BookTicketOnlineService | Association | đầu A: 1; đầu B: bookingCompletion 1 | A --> B | (940,440); (360,440) |
| R-02 | DC-BookTicketOnlineService | IF-03 | Association | đầu A: 1; đầu B: smsSender 1 | A --> B | (130,450); (190,450) |
| R-38 | DC-BookTicketOnlineService | IF-10 | Association | đầu A: 1; đầu B: tripCatalog 1 | A --> B | (430,460); (1050,460) |
| R-39 | DC-BookTicketOnlineService | IF-11 | Association | đầu A: 1; đầu B: ticketing 1 | A --> B | (470,470); (1340,470) |
| R-40 | DC-BookTicketOnlineService | IF-07 | Association | đầu A: 1; đầu B: scheduler 1 | A --> B | (240,480); (470,480) |
| R-41 | DC-BookTicketOnlineService | IF-15 | Association | đầu A: 1; đầu B: idGenerator 1 | A --> B | (280,490); (750,490) |
| R-42 | DC-BookTicketOnlineService | DC-TicketSmsContent | Association | đầu A: 1; đầu B: smsContent 1 | A --> B | (510,500); (1680,500) |
| R-05 | DC-BookTicketOnlineService | DC-Booking | Dependency | - | A --> B | (210,510); (40,510); (40,680); (240,680) |
| R-06 | DC-BookTicketOnlineService | DC-Ticket | Dependency | - | A --> B | (400,520); (50,520); (50,690); (780,690) |
| R-04 | DC-BookTicketOnlineService | DC-Trip | Dependency | - | A --> B | (170,530); (60,530); (60,1060); (180,1060) |
| R-26 | DC-Booking | DC-Trip | Association | đầu A: 0..*; đầu B: trip 1 | A --> B | (210,1070); (270,1070) |
| R-27 | DC-Booking | DC-Seat | Association | đầu A: 0..1; đầu B: seats 1..5 | A --> B | (320,1080); (620,1080) |
| R-28 | DC-Booking | DC-Ticket | Association | đầu A: 0..1; đầu B: tickets 0..5 | A --> B | (430,1090); (860,1090) |
| R-29 | DC-Ticket | DC-Trip | Association | đầu A: 0..*; đầu B: trip 1 | A --> B | (750,1100); (370,1100) |
| R-30 | DC-Ticket | DC-Seat | Association | đầu A: 0..*; đầu B: seat 1 | A --> B | (970,1110); (700,1110) |
| R-23 | DC-Trip | DC-Seat | Composition | đầu A: 1; đầu B: seats 1..* | A --> B | (310,1380); (660,1380) |
| R-22 | DC-Trip | DC-Route | Association | đầu A: 0..*; đầu B: route 1 | A --> B | (160,1390); (210,1390) |
| R-24 | DC-Trip | DC-BaseFare | Association | đầu A: 0..*; đầu B: baseFare 1 | A --> B | (240,1400); (620,1400) |
| R-25 | DC-Trip | DC-HolidaySurcharge | Association | đầu A: 0..*; đầu B: holidaySurcharge 0..1 | A --> B | (390,1410); (1090,1410) |
| R-31 | DC-BaseFare | DC-Route | Association | đầu A: 0..*; đầu B: route 1 | A --> B | (620,1600); (210,1600) |
| R-63 | DC-TicketSmsContent | DC-Ticket | Dependency | - | A --> B | (1680,700); (940,700) |
| R-64 | DC-Booking | IF-15 | Dependency | - | A --> B | (400,710); (750,710) |

### Sơ đồ UC-008

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-15 | tham chiếu | 70 | 40 | 200 | 40 |
| IF-10 | Interface | ITripCatalogRepository | «interface» | PKG-22 | tham chiếu | 350 | 40 | 220 | 40 |
| IF-11 | Interface | ITicketingRepository | «interface» | PKG-23 | tham chiếu | 650 | 40 | 200 | 40 |
| DC-ReturnTicketService | Class | ReturnTicketService | «control» | PKG-09 | trong package | 70 | 170 | 460 | 150 |
| DC-TicketReturnPolicy | Class | TicketReturnPolicy | «entity» | PKG-23 | trong package | 70 | 400 | 460 | 250 |
| DC-Ticket | Class | Ticket | «entity» | PKG-23 | trong package | 70 | 730 | 460 | 170 |
| DC-Trip | Class | Trip | «entity» | PKG-22 | trong package | 70 | 990 | 450 | 140 |
| DC-Seat | Class | Seat | «entity» | PKG-22 | trong package | 600 | 990 | 240 | 140 |
| DC-Refund | Class | Refund | «entity» | PKG-23 | trong package | 920 | 990 | 460 | 140 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-09 | DC-ReturnTicketService | IF-01 | Association | đầu A: 1; đầu B: paymentGateway 1 | A --> B | (190,110); (170,110) |
| R-49 | DC-ReturnTicketService | IF-10 | Association | đầu A: 1; đầu B: tripCatalog 1 | A --> B | (300,120); (460,120) |
| R-48 | DC-ReturnTicketService | IF-11 | Association | đầu A: 1; đầu B: ticketing 1 | A --> B | (410,130); (750,130) |
| R-50 | DC-ReturnTicketService | DC-TicketReturnPolicy | Association | đầu A: 1; đầu B: policy 1 | A --> B | (220,350); (300,350) |
| R-10 | DC-ReturnTicketService | DC-Ticket | Dependency | - | A --> B | (380,360); (40,360); (40,680); (220,680) |
| R-62 | DC-TicketReturnPolicy | DC-Ticket | Dependency | - | A --> B | (300,690); (380,690) |
| R-29 | DC-Ticket | DC-Trip | Association | đầu A: 0..*; đầu B: trip 1 | A --> B | (190,930); (290,930) |
| R-30 | DC-Ticket | DC-Seat | Association | đầu A: 0..*; đầu B: seat 1 | A --> B | (300,940); (720,940) |
| R-32 | DC-Ticket | DC-Refund | Composition | đầu A: 1; đầu B: refund 0..1 | A --> B | (410,950); (1150,950) |
| R-23 | DC-Trip | DC-Seat | Composition | đầu A: 1; đầu B: seats 1..* | A --> B | (290,1160); (720,1160) |


## F9. Gán package và kiểm tra phụ thuộc package

| PKG | Lớp (DC) | Phụ thuộc vào PKG (suy từ F5) | Hợp lệ theo P09 |
|---|---|---|---|
| PKG-09 | DC-BookTicketOnlineService, DC-PayTicketOnlineService, DC-ReturnTicketService, DC-TripOffer, DC-BookingHold, DC-ReturnQuote, DC-ReturnReceipt, DC-TicketSalesRuleException, DC-TicketSalesRule | PKG-15 (IF-01, IF-02), PKG-16 (IF-03), PKG-19 (IF-07, IF-08), PKG-22 (IF-10, Trip), PKG-23 (IF-11, IF-15, Booking, Ticket, TicketReturnPolicy, TicketSmsContent), PKG-28 (Money, TicketCode, PhoneNumber, PaymentReference) | Có (R1, R2, R5, R7). PKG-28 chưa có trong P10 F4 nên ghi Đề xuất sửa P10; PKG-17 chưa dùng vì UC-005 chưa phân tích |
| PKG-22 | DC-Trip, DC-Route, DC-Seat, DC-BaseFare, DC-HolidaySurcharge, DC-TripSchedule, DC-TripStatus, DC-SeatStatus, DC-BusType, IF-10, DC-SeatAlreadyHeldException, DC-InvalidStateException | PKG-28 (Money) | Có. Không phụ thuộc PKG-23: Trip không có thuộc tính, tham số, kiểu trả về thuộc PKG-23; việc tìm vé, đặt chỗ của chuyến qua IF-11 và DC-TripCancellation |
| PKG-23 | DC-Booking, DC-Ticket, DC-TicketReturnPolicy, DC-TicketSmsContent, DC-TripCancellation, DC-Refund, DC-PhoneReservation, IF-11, IF-15, DC-TravelerInfo, DC-BookingSummary, DC-TicketCheckResult, DC-RefundQuote, DC-TicketReturnInfo, DC-CancelImpactInfo, DC-CancellationSummary, 8 enumeration | PKG-22 (Trip, Seat, SeatAlreadyHeldException, InvalidStateException, TripSchedule), PKG-28 (Money, TicketCode, PhoneNumber, PaymentReference, PersistenceUnavailableException) | Có (R8: một chiều PKG-23 --> PKG-22) |

Kiểm tra: không có vòng giữa PKG-09, PKG-22, PKG-23, PKG-28; không có phụ thuộc đi lên (PKG-22 và PKG-23 ở Domain không tham chiếu Services hay Application); realization đi xuống: DC-PayTicketOnlineService và DC-BookTicketOnlineService hiện thực IF-02 (PKG-15), IF-08 (PKG-19) ở layer thấp hơn; IF-10, IF-11, IF-15 do Domain định nghĩa và SS-07 (PKG-14, Services) hiện thực. Phụ thuộc nhảy layer Application --> Domain được R1 cho phép.

Visibility lớp: DC-BookTicketOnlineService và DC-ReturnTicketService public (PKG-08 gọi); DC-PayTicketOnlineService package-private (P10 F5), hiện thực IF-02 công khai; các value object, enumeration và ngoại lệ của PKG-09 public vì nằm trong chữ ký của hai dịch vụ public; mọi lớp của PKG-22 và PKG-23 public theo P10 F5 (SS-07 ánh xạ mọi lớp miền). Chữ ký của hai dịch vụ public dùng TravelerInfo, BookingSummary, TicketCode, PhoneNumber, Money, PurchaseChannel, TripSchedule, BusType, BookingStatus của PKG-22, PKG-23, PKG-28 nên PKG-08 cần phụ thuộc thêm các package đó (Đề xuất sửa P10).


## F10. Design pattern đã áp dụng

| Pattern | Vấn đề trong thiết kế này | Lớp tham gia (vai trò trong pattern) | Lý do chọn | Phương án đơn giản hơn đã xét |
|---|---|---|---|---|
| Repository | Tách truy cập dữ liệu khỏi logic nghiệp vụ; Domain nằm dưới Services nên Persistence phải hiện thực interface do Domain định nghĩa (P09 R6) | IF-10, IF-11, IF-15 (Repository, bộ sinh mã); DC-BookTicketOnlineService, DC-PayTicketOnlineService, DC-ReturnTicketService (client); SS-07 (hiện thực) | P09 F5 và F7 đã quyết định; chống trùng chỗ cần cập nhật có điều kiện ở một nơi | Dịch vụ gọi thẳng ORM: Application phụ thuộc Persistence, ngược R6 |
| Callback qua interface do layer dưới định nghĩa (đảo phụ thuộc) | Cổng thanh toán và bộ định thời ở Services phải gọi lên Application khi có kết quả thanh toán, khi tới mốc hết hạn | IF-02 và DC-PayTicketOnlineService; IF-08 và DC-BookTicketOnlineService | P09 R5, P10 F2 | Polling cổng thanh toán và quét lần đặt từ Application: tốn tài nguyên và vẫn cần mốc 10 phút |
| Factory Method (static factory) | Đối tượng phải ra đời đúng bất biến: lần đặt DRAFT chưa lưu (ASM-44), vé có mã duy nhất (BR-10), khoản hoàn gắn với vé | Booking.createBooking, Ticket.createTicket, Refund.createRefund (TripCancellation.create) | Constructor công khai cho phép tạo Ticket, Refund ngoài Booking, Ticket | Constructor công khai: không ép được nơi tạo Refund và Ticket |
| Value Object (Java record) | P07 trả nhiều giá trị trong một message (BookingSummary, TicketReturnInfo, RefundQuote...) | TripSchedule, TravelerInfo, các kiểu Summary, Info, Quote, Offer, Hold, Receipt | Bất biến, so sánh theo giá trị, tránh tham số rời rạc | Trả Map hoặc mảng đối tượng: mất kiểm tra kiểu |

Không áp dụng State pattern: ba state machine ST-01 đến ST-03 chỉ có 3 đến 4 trạng thái và mỗi lớp dưới 5 operation đổi trạng thái; enumeration kèm guard trong method đủ và dễ kiểm thử (YAGNI). Không dùng Singleton: đồng hồ và bộ sinh mã được truyền qua constructor hoặc tham số.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-108 | Khi hành khách đang ở trang của cổng thanh toán, hệ thống báo cho hành khách việc hết thời hạn giữ chỗ, thanh toán không thành công hoặc vé đã phát hành bằng cách nào? (Website hỏi lại định kỳ / Server đẩy thông báo / Cổng chuyển hướng hành khách về website kèm kết quả) | DC-BookTicketOnlineService.getBookingStatus, getIssuedTickets, retryPayment; DC-BookTicketRestController (PKG-08); DC-BookTicketStore (PKG-05); P07 UC-002 msg 3.1.8.2, 3.1.10, 3.1.15 | P04 UC-002 bước 9a2, 10a nêu hệ thống thông báo nhưng nguồn và P04 không nêu kênh thông báo khi hành khách rời website sang cổng thanh toán (liên quan Q-83, Q-24) |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-102 | Số tiền do phép nhân phần trăm tạo ra (giá vé sau mức tăng, số tiền hoàn) được làm tròn đến đồng theo HALF_UP. | ASM-12 ghi không làm tròn nhưng tiền Việt Nam không có đơn vị nhỏ hơn đồng; với mức tăng nguyên phần trăm và giá theo nghìn đồng, kết quả thường đã tròn. Chờ Q-19, Q-38 | DC-BaseFare.calculateTicketPrice; DC-TicketReturnPolicy.calculateRefundAmount; DC-Money.percent |
| ASM-103 | Kết quả thanh toán thành công đến khi lần đặt còn HELD thì vé vẫn được phát hành, kể cả khi đã quá 10 phút nhưng mốc hết hạn chưa được xử lý; đến sau khi lần đặt EXPIRED thì không phát hành, ghi nhật ký để nhà xe xử lý tay. | P04 UC-002 Mục 8 và Q-10 không nêu thứ tự; bên commit trước thắng nhờ cập nhật có điều kiện (P09 F7), tránh phát hành vé cho chỗ đã trả | DC-BookTicketOnlineService.completeBooking; ST-01 T3, T4 |
| ASM-104 | Vé đã soát (Checked) vẫn huỷ được bằng cancelTicket và cancelWithTrip. | P04 không chặn việc trả vé hay huỷ chuyến với vé đã soát; Q-74 hỏi tác dụng của kết quả soát vé | ST-02 T5, T6; DC-Ticket.cancelTicket, cancelWithTrip |
| ASM-105 | Khoảng ngày của mức tăng giá gồm cả ngày đầu và ngày cuối; hai khoảng ngày cùng áp dụng cho một chuyến không chồng nhau nên mỗi chuyến có tối đa một mức tăng. | GL-25 "khoảng ngày" không nêu cận; BR-05 nêu một mức tăng cho chuyến; phạm vi tuyến, loại xe chờ Q-20 | R-25 phía HolidaySurcharge 0..1; DC-HolidaySurcharge.getSurchargeRate |
| ASM-106 | Khi xác nhận trả vé, hệ thống tính lại mức hoàn tại thời điểm xác nhận và so với số tiền đã hiển thị; khác nhau thì từ chối với lý do REFUND_AMOUNT_CHANGED để tác nhân xem báo giá mới. | ASM-19 yêu cầu tác nhân xác nhận với số tiền đã hiển thị; dịch vụ không giữ trạng thái giữa hai bước (NFR-01) nên không giữ được báo giá theo thời điểm kiểm tra của ASM-23. Chờ Q-39 | DC-ReturnTicketService.confirmReturn; DC-TicketSalesRule.REFUND_AMOUNT_CHANGED |
| ASM-107 | Cổng thanh toán trả hoàn tiền Declined, Unknown hoặc không kết nối được đều xử lý như hoàn không thành công: vé giữ nguyên, không ghi khoản hoàn. | ASM-21 chỉ nêu hoàn không thành công; P11b nêu client quyết định cho Unknown và Q-55 chưa có luồng | DC-ReturnTicketService.confirmReturn; DC-TicketSalesRule.REFUND_FAILED |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F2, F3 (IF-15) | Thiếu interface cấp mã lần đặt và mã vé duy nhất khi nhiều bản back-end cùng chạy (BR-10) | Thêm IF-15 ITicketingIdGenerator định nghĩa ở PKG-23, hiện thực bởi SS-07, dùng bởi PKG-09; P11b bổ sung operation nextBookingId, nextTicketCode cho SS-07 |
| P10 | F3, F4 | Thiếu phần tử: DC-SeatAlreadyHeldException, DC-InvalidStateException, DC-TripSchedule, ba enumeration (PKG-22); 15 kiểu dữ liệu và enumeration (PKG-23); DC-TripOffer, DC-BookingHold, DC-ReturnQuote, DC-ReturnReceipt, DC-TicketSalesRuleException, DC-TicketSalesRule (PKG-09) | Thêm vào bảng phần tử mới do cơ chế thiết kế, danh sách ở F1 (cột Nguồn AC bắt đầu bằng Thiết kế hoặc P11b) |
| P10 | F4, F6 | PKG-09 dùng kiểu PKG-28 (Money, TicketCode, PhoneNumber, PaymentReference) nhưng P10 F4 không có PKG-09 --> PKG-28; PKG-08 dùng kiểu PKG-22, PKG-23, PKG-28 trong chữ ký dịch vụ | Thêm PKG-09 --> PKG-28 và PKG-08 --> PKG-22, PKG-23, PKG-28 (hợp lệ theo R1, Application --> Domain, không tạo vòng) |
| P10 | F3 (AC-E-Ticket // findTicket; AC-E-Trip // findMatchingTrips, // findTrip; AC-E-Route // checkRouteMatches) | P11b đặt việc tìm vé và tìm chuyến ở IF-11.findTicket, IF-10.findTrips, findTrip; entity không tự truy vấn tập chứa mình | Sửa lời F3: các trách nhiệm tìm kiếm thuộc interface kho dữ liệu; DC-Route chỉ là lớp dữ liệu |
| P10 | F2 (IF-08) | ITriggerHandler chỉ có một bên hiện thực là DC-BookTicketOnlineService nên chỉ xử lý HOLD_EXPIRY; khi UC-006, UC-014 có P07 sẽ có thêm loại mốc | Thêm bộ định tuyến theo kind ở PKG-09 hoặc interface xử lý riêng cho mỗi loại mốc khi có P07 của UC-006, UC-014 |
| P07 | UC-002 msg 3.1.11 | Khi phát hành vé, chỗ chuyển từ đang giữ sang đã có vé nhưng không có message tới Seat | Thêm message // markSold từ Booking tới Seat trong vòng lặp phát hành; P08 thêm trách nhiệm tương ứng cho AC-E-Seat (liên quan Q-75) |
| P07 | UC-002 msg 3.1.9 và 3.1.10 | Kết quả thanh toán được vẽ là kết quả trả về đồng bộ của payTickets, trái P11b ASM-100 (kết quả đến bất đồng bộ qua IF-02) | P07 UC-003 và lần chạy lại UC-002 vẽ thanh toán là yêu cầu rồi sự kiện kết quả; P12 đã tách submitBooking và completeBooking |
| P08 | R-03, R-04, R-05, R-06, R-10 | P12 đổi loại: R-03 Dependency --> Association; R-04, R-05, R-06, R-10 Association --> Dependency (lý do ở F5) | Ghi vào P08 khi chạy lại |
| P08 | R-23, R-32 | P12 đổi Association --> Composition (ASM-42, P10 F4; ASM-46, ASM-48) | Ghi vào P08 khi chạy lại |
| P08 | R-25, R-30, R-33 | P12 điền multiplicity R-25 B 0..1 (ASM-105), R-30 A 0..* (ASM-20) và điều hướng R-33 từ PhoneReservation sang Trip | Ghi vào P08 khi chạy lại (R-33, R-34 đã nêu ở P10) |
| P11b | IF-10.findTrip | Tham số route kiểu String làm mất cấu trúc điểm đi, điểm đến mà form UC-013 đang có | Đổi thành findTrip(departurePoint, arrivalPoint, departureDateTime) hoặc ghi định dạng <Điểm đi> - <Điểm đến> |
| P11b | IF-11.findTicket | travelerPhone là tham số bắt buộc nhưng nhân viên bán vé trả vé tại quầy không có số điện thoại (ASM-18) | Cho phép travelerPhone null nghĩa là không lọc theo số điện thoại |
| P11b | IF-01.requestPayment, IF-02.receivePaymentResult | requestKey là khoá do hệ thống sinh nhưng không nêu cách suy ra lần đặt từ khoá khi cổng gọi về | Ghi định dạng requestKey = <bookingId>-<số lần> do Booking.startPaymentAttempt sinh |
| P04 | UC-008 luồng thay thế | Thiếu luồng khi số tiền hoàn lúc xác nhận khác số đã hiển thị (ranh giới 24 giờ, 4 giờ trôi qua giữa hai bước) | Thêm luồng thay thế ở bước 6 hoặc ghi mức hoàn tính lại lúc xác nhận (liên quan Q-39, ASM-106) |

## Vấn đề còn mở

- Ngưỡng quy mô (mục 3 của prompt): phạm vi có 45 phần tử thiết kế, vượt ngưỡng khoảng 15-20 lớp mỗi lần chạy; đã chạy một lượt theo tham số, không chia hai lượt. Số phần tử tăng chủ yếu vì 15 kiểu dữ liệu và enumeration của PKG-23, 9 của PKG-09 và PKG-22 cần cho chữ ký đầy đủ.
- Target 3: câu trách nhiệm của DC-Booking, DC-Trip, DC-Ticket liệt kê nhiều mệnh đề (kiểm tra, giữ, phát hành; tìm giá, thời gian còn lại, huỷ) cùng một lý do thay đổi là luồng đặt vé hoặc quy tắc vé; đạt nếu coi cùng một lý do thay đổi, X1 nên kiểm lại cohesion của DC-Booking và DC-Trip.
- Target 6: vòng đời đầy đủ mới đủ cho DC-Booking, DC-Ticket, DC-Seat. DC-Route, DC-BaseFare, DC-HolidaySurcharge, DC-PhoneReservation chỉ có tạo (và huỷ cùng chuyến với DC-PhoneReservation), DC-Refund bất biến sau khi tạo, DC-Trip có tạo và huỷ chuyến: phần thay đổi, xoá thuộc UC-004, UC-006, UC-012, UC-016, UC-017 chưa phân tích.
- Target 7: ba nhóm message không thành operation riêng của lớp nhận, có lý do ở F4: checkRouteMatches (gộp vào truy vấn IF-10), cancelReturnRequest và showReturnAbortedNotice (dịch vụ không giữ trạng thái), và các message show... tới boundary (ánh xạ vào kết quả trả về hoặc ngoại lệ của dịch vụ, boundary ở PKG-05, PKG-26, PKG-27 ngoài phạm vi). Message UC-013, UC-015 có người gửi là control của PKG-10, PKG-11 chưa vào F4.
- Target 8: các constructor của Route, Seat, BaseFare, HolidaySurcharge, Trip, PhoneReservation và các getter có nguồn Bổ sung; chưa có bên gọi trong bốn UC đã phân tích đối với constructor (UC-004, UC-012, UC-016, UC-017 chưa có P07).
- Target 11: luồng thay thế của P04 UC-002 và UC-008 đều có TicketSalesRule tương ứng; lỗi kỹ thuật (cổng thanh toán không phản hồi, SMS lỗi, kho dữ liệu lỗi) có ngoại lệ kỹ thuật của P11b nhưng P04 chưa có luồng (Q-55, Q-56, Q-104, Q-106).
- Ngoài Target 17 (mức class, không phải mức package): DC-BookTicketOnlineService và DC-PayTicketOnlineService phụ thuộc hai chiều (R-03, R-47) vì kết quả thanh toán bất đồng bộ; chấp nhận tạm vì UC-003 chưa phân tích, đảo bằng sự kiện hoặc interface khi có P07 của UC-003.
- Target 17 (package): PKG-09 --> PKG-28 và PKG-08 --> PKG-22, PKG-23, PKG-28 chưa có trong P10 F4 (Đề xuất sửa P10); hợp lệ theo R1.
- Target 18: DC-Trip không có state machine (hai trạng thái); DC-PhoneReservation chưa có state machine vì chuyển UNPAID --> PAID và hết hạn thuộc UC-004, UC-005, UC-006 chưa phân tích, trong khi BR-24 phụ thuộc trạng thái; làm khi có P07 của các UC đó.
- Target 24: bố cục kiểm bằng tính toán (khoảng cách tối thiểu 40, toạ độ bội số 10, cạnh trực giao không cắt qua node, mỗi cạnh một làn riêng); chiều cao lớp ước lượng theo số ký tự nên có thể lệch khi mở bằng draw.io; chưa mở bằng draw.io để xem nhãn và nét vẽ. Các sơ đồ rộng khoảng 2.000 đến 2.800 đơn vị.
- Target 12: đồng hồ qua constructor cho hai dịch vụ; entity nhận thời điểm qua tham số thay vì constructor vì entity được ORM tạo lại, ghi ở Quy ước áp dụng. Mốc hết thời hạn giữ chỗ có cơ chế lập lịch (F2a).
- Chọn giữa hai quy tắc (C9): prompt yêu cầu operation của interface lấy nguyên chữ ký P11b còn CONG_NGHE đã chốt Java nên dùng kiểu Java; đã giữ nguyên chữ ký P11b (Date, DateTime) và ghi ánh xạ sang LocalDate, LocalDateTime ở Quy ước áp dụng.
- Chọn giữa hai quy tắc (C9): prompt cho interface mới do cơ chế thiết kế gồm đồng hồ, nhưng CONG_NGHE đã có java.time.Clock; không cấp IF cho đồng hồ, chỉ cấp IF-15 cho bộ sinh mã vì cần hiện thực ở SS-07.
- Chọn giữa hai quy tắc (C9): C1 mục 3 cấm đổi mã và phần tử đã chốt, còn Bước 3 cho đổi loại quan hệ P08 kèm lý do; đã giữ mã R-nn của P08 và ghi thay đổi ở cột Lý do (R-03, R-04, R-05, R-06, R-10, R-23, R-32).
- Chọn giữa hai quy tắc (C9): F2 yêu cầu mỗi message gán cho đúng một operation của lớp nhận, còn P10 F3 và P11b chuyển một số trách nhiệm sang lớp khác; F4 ghi "Khác lớp nhận" kèm lý do cho từng dòng, riêng checkReturnTimeLimit gán cho hai operation để kiểm thử biên 4 giờ độc lập.

