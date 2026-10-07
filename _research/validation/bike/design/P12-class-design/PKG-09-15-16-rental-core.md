# P12 - Thiết kế lớp PKG-09, PKG-15, PKG-16 - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P12 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CONG_NGHE Java 17, Spring Boot 3); P04 UC-005, UC-007, UC-009, UC-013; P05; P06; P07 (4 UC); P08; P09; P10; P11a (screen-list); P11b (SS-01, SS-02) 1.0 |
| Phạm vi | PKG-09 Rental, PKG-15 RentalDomain, PKG-16 FleetDomain |

Placeholder: PHAM_VI_THIET_KE = "PKG-09 Rental, PKG-15 RentalDomain, PKG-16 FleetDomain (chưa có file P12 nào khác)"; QUY_UOC_KIEU_DU_LIEU = "Tiền: value object Money bọc long, đơn vị đồng; Thời điểm: Instant; Thời lượng: Duration; Định danh: UUID; Tập hợp: List; Giá trị có thể vắng: Optional"; MAU_THIET_KE_DA_CHOT = "Truy cập dữ liệu qua Repository (P09 F5, P10 IF-07 đến IF-13)"; YEU_CAU_BO_SUNG = Không có.

Bước 0: phần tử trong phạm vi lấy từ P10 F3 (DC-RentBikeService, DC-ReturnBikeService, DC-RecordLostBikeService, DC-RiderAccount, DC-Trip, DC-FareCalculator, DC-PaymentHold, DC-Station, DC-Dock, DC-Bike, DC-TransferOrder), P10 cơ chế (DC-DockEventHandler, DC-RentalTimerHandler, IF-07 đến IF-13). Lớp bên trong SS-01, SS-02 không thuộc phạm vi (PKG-18, PKG-19). UC tham gia: UC-005, UC-007, UC-009, UC-013 (phần miền).

## F1. Bảng lớp thiết kế

| DC | Tên | Stereotype | PKG | Trách nhiệm | Nguồn AC | Loại | Persistent | Ghi chú thiết kế |
|---|---|---|---|---|---|---|---|---|
| DC-RiderAccount | RiderAccount | «entity» | PKG-15 | Giữ thông tin tài khoản người thuê xe và quyết định tài khoản có đủ điều kiện thuê xe hay không. | AC-E-RiderAccount | class | Có | Có trạng thái đơn giản ACTIVE/LOCKED, không vẽ state machine (2 trạng thái) |
| DC-Trip | Trip | «entity» | PKG-15 | Giữ vòng đời một chuyến đi từ khi xe được rút tới khi xe được trả. | AC-E-Trip | class | Có | tách từ AC-E-Trip (phần tính giá sang DC-FareCalculator); ST-01 |
| DC-FareCalculator | FareCalculator | «entity» | PKG-15 | Tính cước theo thời lượng theo BR-07. | AC-E-Trip | class | Không | tách từ AC-E-Trip; không trạng thái |
| DC-PaymentHold | PaymentHold | «entity» | PKG-15 | Ghi nhận một khoản tạm giữ trên thẻ và các lần thu, huỷ, trả lại của nó. | AC-E-PaymentHold | class | Có | ST-02 |
| DC-RentalRequest | RentalRequest | «entity» | PKG-15 | Ghi nhận một lượt thuê đang chờ rút xe để mọi tiến trình máy chủ đều xử lý được sự kiện rút xe hoặc hết 60 giây. | Thiết kế: NFR-03 (máy chủ không giữ trạng thái, P09 F3) thay cho trạng thái chờ giữ trong AC-C-RentBikeController | class | Có | ST-03 |
| DC-Money | Money | «value object» | PKG-15 | Biểu diễn một số tiền đồng không âm và các phép tính trên nó. | Thiết kế: QUY_UOC_KIEU_DU_LIEU; P11b chữ ký IF-01 | value object | Không | Bất biến |
| DC-CardReference | CardReference | «value object» | PKG-15 | Bọc mã tham chiếu thẻ do cổng thanh toán cấp. | Thiết kế: P11b chữ ký IF-01; NFR-04 | value object | Không | - |
| DC-HoldReference | HoldReference | «value object» | PKG-15 | Bọc mã khoản tạm giữ do cổng thanh toán trả về. | Thiết kế: P11b chữ ký IF-01 | value object | Không | - |
| DC-TripInvoice | TripInvoice | «value object» | PKG-15 | Mang nội dung hoá đơn của một chuyến. | Thiết kế: kết quả msg UC-007 1.1.9 | value object | Không | Thành phần chờ Q-24 |
| DC-AccountStatus | AccountStatus | «enumeration» | PKG-15 | Liệt kê giá trị AccountStatus. | Thiết kế: BR-10, GL-15 | enumeration | Không | ACTIVE, LOCKED |
| DC-TripStatus | TripStatus | «enumeration» | PKG-15 | Liệt kê giá trị TripStatus. | Thiết kế: ST-01 | enumeration | Không | IN_PROGRESS, COMPLETED (xe thất lạc: Q-04) |
| DC-HoldStatus | HoldStatus | «enumeration» | PKG-15 | Liệt kê giá trị HoldStatus. | Thiết kế: ST-02 | enumeration | Không | ACTIVE, CANCELLED, CAPTURED, SETTLED |
| DC-RentalRequestStatus | RentalRequestStatus | «enumeration» | PKG-15 | Liệt kê giá trị RentalRequestStatus. | Thiết kế: ST-03 | enumeration | Không | AWAITING_REMOVAL, STARTED, EXPIRED |
| DC-RentalEligibility | RentalEligibility | «enumeration» | PKG-15 | Liệt kê giá trị RentalEligibility. | Thiết kế: BR-01, BR-02, BR-03 | enumeration | Không | ELIGIBLE, NO_CARD_LINKED, TRIP_IN_PROGRESS, OUTSTANDING_FARE |
| DC-Station | Station | «entity» | PKG-16 | Giữ thông tin một trạm. | AC-E-Station | class | Có | Chỉ có dữ liệu trong phạm vi (UC-012 chưa phân tích) |
| DC-Dock | Dock | «entity» | PKG-16 | Giữ thông tin một ụ khoá và xe ụ đang giữ. | AC-E-Dock | class | Có | - |
| DC-Bike | Bike | «entity» | PKG-16 | Giữ trạng thái của một xe và quyết định xe có được cho thuê. | AC-E-Bike | class | Có | Không vẽ state machine: chuyển trạng thái chủ yếu thuộc UC-008, UC-011 chưa phân tích |
| DC-TransferOrder | TransferOrder | «entity» | PKG-16 | Ghi nhận một lệnh điều chuyển xe giữa hai trạm. | AC-E-TransferOrder | class | Có | Trạng thái PENDING, COMPLETED (Q-09); không vẽ state machine (2 trạng thái) |
| DC-BikeStatus | BikeStatus | «enumeration» | PKG-16 | Liệt kê giá trị BikeStatus. | Thiết kế: GL-22 | enumeration | Không | AVAILABLE, AWAITING_INSPECTION, LOST (Q-27) |
| DC-TransferOrderStatus | TransferOrderStatus | «enumeration» | PKG-16 | Liệt kê giá trị TransferOrderStatus. | Thiết kế: GL-09 | enumeration | Không | PENDING, COMPLETED |
| DC-RentBikeService | RentBikeService | «control» | PKG-09 | Điều phối UC-005 Thuê xe từ lúc quét mã tới lúc chuyến bắt đầu hoặc lượt thuê hết hạn. | AC-C-RentBikeController | class | Không | Đổi tên ở P10; ranh giới giao dịch từng bước (không bao lời gọi cổng thanh toán) |
| DC-ReturnBikeService | ReturnBikeService | «control» | PKG-09 | Điều phối UC-007 Trả xe từ lúc ụ báo nhận xe tới lúc gửi hoá đơn. | AC-C-ReturnBikeController | class | Không | - |
| DC-RecordLostBikeService | RecordLostBikeService | «control» | PKG-09 | Điều phối UC-009 khi một chuyến đạt mốc 24 giờ. | AC-C-RecordLostBikeController | class | Không | - |
| DC-DockEventHandler | DockEventHandler | «control» | PKG-09 | Chuyển sự kiện của ụ khoá tới dịch vụ ứng dụng tương ứng. | P10 cơ chế callback thiết bị | class | Không | Hiện thực IF-03 |
| DC-RentalTimerHandler | RentalTimerHandler | «control» | PKG-09 | Chuyển mốc thời gian đến hạn tới dịch vụ ứng dụng tương ứng. | P10 cơ chế callback lập lịch | class | Không | Hiện thực IF-06 |
| DC-RentalOutcome | RentalOutcome | «value object» | PKG-09 | Mang kết quả requestRental cho endpoint. | Thiết kế: kết quả msg UC-005 1.1 | value object | Không | status: UNLOCK_SENT hoặc REJECTED; reason: RentalEligibility hoặc HOLD_DECLINED hoặc BIKE_NOT_RENTABLE |
| IF-07 | IRiderAccountRepository | «interface» | PKG-15 | Truy cập kho dữ liệu của lớp miền tương ứng. | P10 cơ chế Persistence | interface | Không | - |
| IF-08 | ITripRepository | «interface» | PKG-15 | Truy cập kho dữ liệu của lớp miền tương ứng. | P10 cơ chế Persistence | interface | Không | - |
| IF-09 | IPaymentHoldRepository | «interface» | PKG-15 | Truy cập kho dữ liệu của lớp miền tương ứng. | P10 cơ chế Persistence | interface | Không | - |
| IF-14 | IRentalRequestRepository | «interface» | PKG-15 | Truy cập kho dữ liệu của lớp miền tương ứng. | Đề xuất sửa P10 (mã tạm, chờ P10 cấp) | interface | Không | - |
| IF-10 | IStationRepository | «interface» | PKG-16 | Truy cập kho dữ liệu của lớp miền tương ứng. | P10 cơ chế Persistence | interface | Không | - |
| IF-11 | IDockRepository | «interface» | PKG-16 | Truy cập kho dữ liệu của lớp miền tương ứng. | P10 cơ chế Persistence | interface | Không | - |
| IF-12 | IBikeRepository | «interface» | PKG-16 | Truy cập kho dữ liệu của lớp miền tương ứng. | P10 cơ chế Persistence | interface | Không | - |
| IF-13 | ITransferOrderRepository | «interface» | PKG-16 | Truy cập kho dữ liệu của lớp miền tương ứng. | P10 cơ chế Persistence | interface | Không | - |
| IF-01 | IPaymentGateway | «interface» | PKG-18 | Tham chiếu (ngoài phạm vi, chữ ký ở P11b hoặc F2) | P10 | interface | Không | tham chiếu |
| IF-02 | IDockCommandSender | «interface» | PKG-19 | Tham chiếu (ngoài phạm vi, chữ ký ở P11b hoặc F2) | P10 | interface | Không | tham chiếu |
| IF-03 | IDockEventListener | «interface» | PKG-19 | Tham chiếu (ngoài phạm vi, chữ ký ở P11b hoặc F2) | P10 | interface | Không | tham chiếu |
| IF-04 | IInvoiceSender | «interface» | PKG-20 | Tham chiếu (ngoài phạm vi, chữ ký ở P11b hoặc F2) | P10 | interface | Không | tham chiếu |
| IF-05 | IScheduler | «interface» | PKG-21 | Tham chiếu (ngoài phạm vi, chữ ký ở P11b hoặc F2) | P10 | interface | Không | tham chiếu |
| IF-06 | ITimerListener | «interface» | PKG-21 | Tham chiếu (ngoài phạm vi, chữ ký ở P11b hoặc F2) | P10 | interface | Không | tham chiếu |

Trả lời bốn câu hỏi cho control (Bước 1.4):

| Control | Có thật cần | Có cần tách | Căn cứ | Ranh giới giao dịch |
|---|---|---|---|---|
| DC-RentBikeService | Có: điều phối 5 bước, 2 hệ thống ngoài, hẹn giờ | Không: một UC, một tác nhân | NFR-02 | Ba giao dịch ngắn: (1) ghi PaymentHold và RentalRequest sau khi cổng trả Approved; (2) handleBikeRemoved; (3) handleRemovalTimeout. Lời gọi IF-01, IF-02 nằm ngoài giao dịch (P09 F7) |
| DC-ReturnBikeService | Có | Không | - | Giao dịch (1) ghi Dock, Trip; lời gọi capture, releaseRemainder ngoài giao dịch; giao dịch (2) ghi PaymentHold |
| DC-RecordLostBikeService | Có | Không | - | Giao dịch sau khi capture trả kết quả |
| DC-DockEventHandler, DC-RentalTimerHandler | Có: hiện thực listener của subsystem (P10) | Không | P09 F6 | Không |

## F2. Bảng operation

| DC | Visibility | Chữ ký | Mô tả | Tiền/hậu điều kiện | Nguồn | Phạm vi | Ngoại lệ / lỗi |
|---|---|---|---|---|---|---|---|
| DC-RiderAccount | + | checkRentalEligibility(hasTripInProgress: boolean): RentalEligibility | Kiểm tra BR-01, BR-03 trên dữ liệu của tài khoản và BR-02 qua tham số; trả về ELIGIBLE hoặc lý do đầu tiên không đạt theo thứ tự BR-01, BR-02, BR-03 | Tiền: không. Hậu: không đổi trạng thái | P07 UC-005 msg 1.1.1 // checkRentalEligibility | Instance | - |
| DC-RiderAccount | + | lock(): void | Chuyển tài khoản sang LOCKED (BR-10); gọi lại khi đã LOCKED thì không đổi | Hậu: status = LOCKED | P07 UC-009 msg 1.5 // lock | Instance | - |
| DC-RiderAccount | + | getEmail(): String | Trả email để gửi hoá đơn | - | P07 UC-007 msg 1.1.9.1 // getContactEmail | Instance | - |
| DC-RiderAccount | + | getCardReference(): CardReference | Trả mã tham chiếu thẻ để tạm giữ | Tiền: đã liên kết thẻ | P07 UC-005 msg 1.1.6 (dữ liệu truyền) | Instance | IllegalStateException khi chưa liên kết thẻ |
| DC-Trip | + | start(rider: RiderAccount, bike: Bike, startDock: Dock, hold: PaymentHold, startTime: Instant): Trip | Factory tạo chuyến IN_PROGRESS | Hậu: status = IN_PROGRESS; ST-01 (initial) | P07 UC-005 msg 2.1.2 // startTrip | Classifier | - |
| DC-Trip | + | isInProgress(): boolean | Cho biết chuyến đang diễn ra | - | P07 UC-005 msg 1.1.1.1 // isOngoing | Instance | - |
| DC-Trip | + | end(endDock: Dock, endTime: Instant, calculator: FareCalculator): Money | Kết thúc chuyến, ghi ụ trả, thời điểm kết thúc, tính và lưu cước; trả về cước | Tiền: IN_PROGRESS. Hậu: COMPLETED, endTime, endDock, fare có giá trị | P07 UC-007 msg 1.1.3 // endTrip, 1.1.4 // calculateFare; ST-01 sự kiện end | Instance | IllegalTripStateException khi không IN_PROGRESS; IllegalArgumentException khi endTime < startTime |
| DC-Trip | + | exceedsMaxDuration(now: Instant): boolean | Kiểm tra BR-09: now - startTime > MAX_DURATION và chuyến IN_PROGRESS | - | P07 UC-009 msg 1.1 // checkExceedsMaxDuration | Instance | - |
| DC-Trip | + | composeInvoice(): TripInvoice | Lập nội dung hoá đơn từ chuyến đã kết thúc (thành phần chờ Q-24) | Tiền: COMPLETED | P07 UC-007 msg 1.1.9 // composeInvoice | Instance | IllegalTripStateException |
| DC-Trip | + | getBike(): Bike | Trả xe của chuyến | - | P07 UC-009 trả về msg 1.1 | Instance | - |
| DC-Trip | + | getPaymentHold(): PaymentHold | Trả khoản tạm giữ của chuyến | - | P07 UC-007 msg 1.1.5, UC-009 msg 1.3 (dữ liệu truyền) | Instance | - |
| DC-Trip | + | getRider(): RiderAccount | Trả tài khoản của chuyến | - | P07 UC-007 msg 1.1.9.1, UC-009 msg 1.5 | Instance | - |
| DC-FareCalculator | + | calculate(duration: Duration): Money | Cước = 0 nếu duration <= FREE_PERIOD; ngược lại BLOCK_PRICE x ceil((duration - FREE_PERIOD) / BLOCK) | Tiền: duration >= 0. Hậu: không đổi trạng thái | P07 UC-007 msg 1.1.4 // calculateFare (BR-07) | Instance | IllegalArgumentException khi duration âm |
| DC-PaymentHold | + | record(holdReference: HoldReference, amount: Money): PaymentHold | Factory tạo khoản tạm giữ ACTIVE | Hậu: status = ACTIVE | P07 UC-005 msg 1.1.8 // recordHold | Classifier | - |
| DC-PaymentHold | + | markCancelled(): void | Ghi khoản tạm giữ đã huỷ | Tiền: ACTIVE. Hậu: CANCELLED | P07 UC-005 msg 3.3 // markCancelled; ST-02 | Instance | IllegalHoldStateException |
| DC-PaymentHold | + | recordCapture(amount: Money): void | Ghi số tiền đã thu | Tiền: ACTIVE, amount <= this.amount. Hậu: CAPTURED | P07 UC-007 msg 1.1.6, UC-009 msg 1.4 // recordCapture; ST-02 | Instance | IllegalHoldStateException; IllegalArgumentException khi vượt số tiền |
| DC-PaymentHold | + | recordRemainderReleased(): void | Ghi phần dư đã trả lại | Tiền: CAPTURED. Hậu: SETTLED | P07 UC-007 msg 1.1.8 // recordRemainderReleased; ST-02 | Instance | IllegalHoldStateException |
| DC-PaymentHold | + | getRemainder(): Money | Trả phần dư | - | P07 UC-007 msg 1.1.7 (dữ liệu truyền) | Instance | - |
| DC-PaymentHold | + | getHoldReference(): HoldReference | Trả mã khoản tạm giữ | - | P07 UC-005 msg 3.2 | Instance | - |
| DC-RentalRequest | + | open(rider: RiderAccount, dock: Dock, bike: Bike, hold: PaymentHold, now: Instant): RentalRequest | Factory tạo lượt chờ rút xe | Hậu: AWAITING_REMOVAL | P07 UC-005 msg 1.1.10 // startRemovalWait | Classifier | - |
| DC-RentalRequest | + | complete(): void | Đánh dấu xe đã được rút | Tiền: AWAITING_REMOVAL. Hậu: STARTED | P07 UC-005 msg 2.1 // handleBikeRemoved; ST-03 | Instance | IllegalStateException |
| DC-RentalRequest | + | expire(): void | Đánh dấu hết thời hạn chờ | Tiền: AWAITING_REMOVAL. Hậu: EXPIRED | P07 UC-005 msg 3 // handleRemovalTimeout; ST-03 | Instance | IllegalStateException |
| DC-RentalRequest | + | isAwaitingRemoval(): boolean | Cho biết còn chờ rút xe | - | ST-03 | Instance | - |
| DC-Money | + | of(amount: long): Money | Factory | Tiền: amount >= 0 | Bổ sung: khởi tạo | Classifier | IllegalArgumentException |
| DC-Money | + | plus(other: Money): Money | Cộng | - | Bổ sung: FareCalculator | Instance | - |
| DC-Money | + | minus(other: Money): Money | Trừ | Tiền: this >= other | Bổ sung: PaymentHold.getRemainder | Instance | IllegalArgumentException |
| DC-Money | + | times(factor: long): Money | Nhân | Tiền: factor >= 0 | Bổ sung: FareCalculator | Instance | IllegalArgumentException |
| DC-Money | + | equals(o: Object): boolean | So sánh bằng theo amount | - | Bổ sung: equality | Instance | - |
| DC-Dock | + | releaseBike(): Bike | Ghi nhận ụ không còn giữ xe, trả xe vừa rời ụ | Tiền: dockedBike có giá trị. Hậu: dockedBike rỗng | P07 UC-005 msg 2.1.1 // releaseBike | Instance | IllegalStateException khi ụ trống |
| DC-Dock | + | acceptBike(bike: Bike): void | Ghi nhận ụ đang giữ xe | Tiền: ụ trống (BR-08). Hậu: dockedBike = bike | P07 UC-007 msg 1.1.1 // acceptBike | Instance | IllegalStateException khi ụ đang giữ xe khác |
| DC-Dock | + | getDockedBike(): Optional<Bike> | Trả xe ụ đang giữ | - | P07 UC-005 trả về msg 1.1.3 | Instance | - |
| DC-Bike | + | isRentable(): boolean | BR-04: status khác AWAITING_INSPECTION (và khác LOST, Q-27) | - | P07 UC-005 msg 1.1.4 // checkRentable | Instance | - |
| DC-Bike | + | markLost(): void | Ghi xe thất lạc | Hậu: status = LOST (Q-27) | P07 UC-009 msg 1.2 // markLost | Instance | - |
| DC-TransferOrder | + | create(from: Station, to: Station, requestedBikes: <Q-25>): TransferOrder | Factory tạo lệnh PENDING | Tiền: from, to khác null (trùng nhau: Q-33). Hậu: PENDING | P07 UC-013 msg 2.1.3 // initializeTransferOrder | Classifier | IllegalArgumentException |
| DC-RentBikeService | + | requestRental(riderId: UUID, dockQrCode: String): RentalOutcome | Kiểm tra điều kiện, tạm giữ, gửi lệnh mở khoá, hẹn giờ 60 giây; trả kết quả UNLOCK_SENT hoặc lý do từ chối | Tiền: người thuê đã xác thực. Hậu (thành công): PaymentHold ACTIVE, RentalRequest AWAITING_REMOVAL, lệnh mở khoá đã giao | P07 UC-005 msg 1.1 // requestRental, 1.1.2, 1.1.5, 1.1.7 // rejectRental | Instance | UnknownDockException (mã QR không có ụ); PaymentOutcomeUnknownException; DockCommunicationException (Q-44) |
| DC-RentBikeService | ~ | handleBikeRemoved(event: DockEvent): void | Hoàn tất lượt thuê đang chờ ở ụ: ụ nhả xe, tạo chuyến, huỷ hẹn 60 giây, hẹn mốc 24 giờ | Tiền: có RentalRequest AWAITING_REMOVAL ở ụ (không có: Q-45). Hậu: Trip IN_PROGRESS | P07 UC-005 msg 2.1 // handleBikeRemoved | Instance | - |
| DC-RentBikeService | ~ | handleRemovalTimeout(requestId: UUID): void | Khi hết 60 giây mà lượt thuê còn chờ: gửi lệnh khoá, huỷ tạm giữ, đánh dấu hết hạn | Tiền: RentalRequest tồn tại. Hậu: EXPIRED, PaymentHold CANCELLED | P07 UC-005 msg 3 // handleRemovalTimeout (BR-06) | Instance | - |
| DC-ReturnBikeService | ~ | handleBikeReturned(event: DockEvent): void | Ghi ụ giữ xe, kết thúc chuyến, thu cước, trả phần dư, huỷ mốc 24 giờ, gửi hoá đơn | Tiền: xe có chuyến IN_PROGRESS (không có: Q-04). Hậu: Trip COMPLETED, PaymentHold SETTLED | P07 UC-007 msg 1.1 // handleBikeReturned, 1.1.10 // sendInvoice | Instance | PaymentOutcomeUnknownException, PaymentGatewayUnavailableException (xử lý chờ Q-23) |
| DC-RecordLostBikeService | ~ | handleTripDurationReached(tripId: UUID, now: Instant): void | Nếu chuyến còn IN_PROGRESS và quá 24 giờ: đánh dấu xe thất lạc, thu toàn bộ tạm giữ, khoá tài khoản | Hậu: Bike LOST, PaymentHold CAPTURED, RiderAccount LOCKED | P07 UC-009 msg 1 // notifyTripDurationReached | Instance | PaymentOutcomeUnknownException (Q-23) |
| DC-DockEventHandler | + | onBikeRemoved(event: DockEvent): void | Chuyển cho RentBikeService.handleBikeRemoved | - | P11b IF-03.onBikeRemoved | Instance | - |
| DC-DockEventHandler | + | onBikeReturned(event: DockEvent): void | Chuyển cho ReturnBikeService.handleBikeReturned | - | P11b IF-03.onBikeReturned | Instance | - |
| DC-RentalTimerHandler | + | onTimerFired(timer: TimerEvent): void | REMOVAL_TIMEOUT --> RentBikeService.handleRemovalTimeout; TRIP_MAX_DURATION --> RecordLostBikeService.handleTripDurationReached | - | IF-06 (chữ ký tạm, P11b chưa thiết kế SS-04) | Instance | - |
| IF-07 | + | findById(id: UUID): Optional<RiderAccount> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-07 | + | save(account: RiderAccount): void | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-08 | + | existsInProgressByRider(riderId: UUID): boolean | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-08 | + | findInProgressByBike(bikeId: UUID): Optional<Trip> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-08 | + | findById(id: UUID): Optional<Trip> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-08 | + | save(trip: Trip): void | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-09 | + | save(hold: PaymentHold): void | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-14 | + | findAwaitingByDock(dockId: UUID): Optional<RentalRequest> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-14 | + | findById(id: UUID): Optional<RentalRequest> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-14 | + | save(request: RentalRequest): void | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-10 | + | findById(id: UUID): Optional<Station> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-11 | + | findByQrCode(qrCode: String): Optional<Dock> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-11 | + | findById(id: UUID): Optional<Dock> | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-11 | + | save(dock: Dock): void | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-12 | + | save(bike: Bike): void | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |
| IF-13 | + | save(order: TransferOrder): void | Truy cập kho dữ liệu | - | P10 cơ chế Persistence; dùng trong F3 | Instance | - |

Chữ ký tạm cho interface ngoài phạm vi P11b (dùng trong F3, chờ chạy P11b cho SS-03, SS-04):

| IF | Chữ ký tạm | Nguồn |
|---|---|---|
| IF-04 IInvoiceSender | + sendInvoice(email: String, invoice: TripInvoice): void | P10 SS-03 // deliverInvoice |
| IF-05 IScheduler | + schedule(type: TimerType, subjectId: UUID, dueAt: Instant): void<br>+ cancel(type: TimerType, subjectId: UUID): void | P10 SS-04 |
| IF-06 ITimerListener | + onTimerFired(timer: TimerEvent): void | P10 SS-04 |

## F3. Bảng thiết kế method

| DC.operation | Thuật toán / các bước chính | Đối tượng và operation khác được dùng | Cách dùng thuộc tính, tham số, quan hệ | Hành vi theo trạng thái |
|---|---|---|---|---|
| DC-RentBikeService.requestRental(riderId, dockQrCode) | 1. account = accounts.findById(riderId). 2. eligibility = account.checkRentalEligibility(trips.existsInProgressByRider(riderId)); khác ELIGIBLE thì trả REJECTED(eligibility). 3. dock = docks.findByQrCode(dockQrCode), không có thì ném UnknownDockException. 4. bike = dock.getDockedBike(); rỗng thì trả REJECTED (Q-20). 5. bike.isRentable() sai thì trả REJECTED(BIKE_NOT_RENTABLE). 6. requestId = UUID mới; result = paymentGateway.placeHold(account.getCardReference(), Money.of(200000), requestId); Declined thì trả REJECTED(HOLD_DECLINED). 7. Giao dịch: hold = PaymentHold.record(result.holdRef, Money.of(200000)); request = RentalRequest.open(account, dock, bike, hold, now); lưu cả hai. 8. dockCommands.sendUnlockCommand(dock.id, request.id). 9. scheduler.schedule(REMOVAL_TIMEOUT, request.id, now + 60 giây). 10. Trả UNLOCK_SENT | IF-07, IF-08, IF-11, IF-01, IF-09, IF-14, IF-02, IF-05 | Số 200.000 là BR-05 (hằng trong PaymentHold? xem Vấn đề còn mở) | - |
| DC-RentBikeService.handleBikeRemoved(event) | 1. request = requests.findAwaitingByDock(event.dockId); không có thì bỏ qua và ghi nhận (Q-45). 2. Giao dịch: dock.releaseBike(); trip = Trip.start(request.rider, request.bike, request.dock, request.hold, event.occurredAt); request.complete(); lưu. 3. scheduler.cancel(REMOVAL_TIMEOUT, request.id). 4. scheduler.schedule(TRIP_MAX_DURATION, trip.id, trip.startTime + 24 giờ) | IF-14, IF-11, IF-08, IF-05 | Trip.startTime = thời điểm ụ báo (GL-04) | ST-03: complete chỉ từ AwaitingRemoval |
| DC-RentBikeService.handleRemovalTimeout(requestId) | 1. request = requests.findById. 2. Không còn AwaitingRemoval thì kết thúc (sự kiện rút xe đã tới trước). 3. dockCommands.sendLockCommand(dock.id). 4. paymentGateway.cancelHold(hold.holdReference). 5. Giao dịch: hold.markCancelled(); request.expire(); lưu | IF-14, IF-02, IF-01, IF-09 | - | ST-03, ST-02 |
| DC-ReturnBikeService.handleBikeReturned(event) | 1. dock = docks.findById(event.dockId); trip = trips.findInProgressByBike(event.bikeId); không có thì dừng (Q-04). 2. Giao dịch: dock.acceptBike(trip.getBike()); fare = trip.end(dock, event.occurredAt, fareCalculator); lưu. 3. hold = trip.getPaymentHold(); fare > amount thì chưa quy định (Q-02). 4. paymentGateway.capture(hold.holdReference, fare) (fare = 0: Q-31); hold.recordCapture(fare). 5. paymentGateway.releaseRemainder(hold.holdReference, hold.getRemainder()); hold.recordRemainderReleased(); lưu. 6. scheduler.cancel(TRIP_MAX_DURATION, trip.id). 7. invoiceSender.sendInvoice(trip.getRider().getEmail(), trip.composeInvoice()) | IF-11, IF-08, IF-01, IF-09, IF-05, IF-04, DC-FareCalculator | - | ST-01 end; ST-02 |
| DC-RecordLostBikeService.handleTripDurationReached(tripId, now) | 1. trip = trips.findById; trip.exceedsMaxDuration(now) sai thì kết thúc (chuyến đã kết thúc). 2. trip.getBike().markLost(); lưu. 3. hold = trip.getPaymentHold(); paymentGateway.capture(hold.holdReference, hold.amount); hold.recordCapture(hold.amount). 4. trip.getRider().lock(); lưu | IF-08, IF-12, IF-01, IF-09, IF-07 | - | ST-02 Captured --> final [remainder = 0] |
| DC-FareCalculator.calculate(duration) | 1. duration âm thì ném IllegalArgumentException. 2. duration <= 30 phút thì trả 0. 3. billable = duration - 30 phút. 4. blocks = ceil(billable / 15 phút), tính trên giây (đơn vị làm tròn chờ Q-46). 5. Trả 5.000 x blocks | Money.times | Hằng FREE_PERIOD, BLOCK, BLOCK_PRICE (BR-07; Q-15 nếu thuộc bảng giá cước) | - |
| DC-Trip.end(endDock, endTime, calculator) | 1. status khác IN_PROGRESS thì ném IllegalTripStateException. 2. endTime < startTime thì ném IllegalArgumentException. 3. Ghi endDock, endTime. 4. fare = calculator.calculate(Duration.between(startTime, endTime)). 5. status = COMPLETED; trả fare | DC-FareCalculator | R-21, R-48 | ST-01 |
| DC-RiderAccount.checkRentalEligibility(hasTripInProgress) | Thứ tự: cardReference rỗng --> NO_CARD_LINKED; hasTripInProgress --> TRIP_IN_PROGRESS; outstandingFare > 0 --> OUTSTANDING_FARE; còn lại ELIGIBLE. Tài khoản LOCKED: chưa quy định (Q-21) | - | cardReference, outstandingFare | - |
| DC-PaymentHold.recordCapture(amount) | 1. status khác ACTIVE thì ném. 2. amount > this.amount thì ném IllegalArgumentException. 3. capturedAmount = amount; status = CAPTURED | - | - | ST-02 |

## F4. Bảng ánh xạ message --> operation

| UC | STT message | Từ | Đến | Message phân tích | Operation thiết kế |
|---|---|---|---|---|---|
| UC-005 | 1 | ACT-01 | AC-B-RentBikeForm | // scanDockQrCode | Ngoài phạm vi (PKG-05) |
| UC-005 | 1.1 | AC-B-RentBikeForm | AC-C-RentBikeController | // requestRental | DC-RentBikeService.requestRental(riderId: UUID, dockQrCode: String): RentalOutcome (gọi từ DC-RentalEndpoint) |
| UC-005 | 1.1.1 | AC-C-RentBikeController | AC-E-RiderAccount | // checkRentalEligibility | DC-RiderAccount.checkRentalEligibility(hasTripInProgress: boolean): RentalEligibility |
| UC-005 | 1.1.1.1 | AC-E-RiderAccount | AC-E-Trip | // isOngoing | IF-08.existsInProgressByRider(riderId: UUID): boolean (gọi từ DC-RentBikeService; lý do: tránh RiderAccount duyệt tập chuyến) |
| UC-005 | 1.1.2, 1.1.5, 1.1.7 | AC-C-RentBikeController | AC-B-RentBikeForm | // rejectRental | Giá trị trả về RentalOutcome REJECTED của requestRental |
| UC-005 | 1.1.2.1, 1.1.5.1, 1.1.7.1 | AC-B-RentBikeForm | ACT-01 | // showRentalRejected | Ngoài phạm vi (PKG-05, MSG-02, MSG-03) |
| UC-005 | 1.1.3 | AC-C-RentBikeController | AC-E-Dock | // findDockByQrCode | IF-11.findByQrCode(qrCode: String): Optional<Dock>; DC-Dock.getDockedBike(): Optional<Bike> (trả về) |
| UC-005 | 1.1.4 | AC-C-RentBikeController | AC-E-Bike | // checkRentable | DC-Bike.isRentable(): boolean |
| UC-005 | 1.1.6, 1.1.6.1 | AC-C-RentBikeController | AC-B-PaymentGateway | // requestHold | IF-01.placeHold(cardRef: CardReference, amount: Money, requestId: UUID): HoldResult |
| UC-005 | 1.1.8 | AC-C-RentBikeController | AC-E-PaymentHold | // recordHold | DC-PaymentHold.record(holdReference: HoldReference, amount: Money): PaymentHold |
| UC-005 | 1.1.9, 1.1.9.1 | AC-C-RentBikeController | AC-B-DockDevice | // sendUnlockCommand | IF-02.sendUnlockCommand(dockId: DockId, requestId: UUID): void |
| UC-005 | 1.1.10 | AC-C-RentBikeController | (tự gọi) | // startRemovalWait | DC-RentalRequest.open(...): RentalRequest; IF-05.schedule(REMOVAL_TIMEOUT, requestId, dueAt) |
| UC-005 | 2, 2.1 | ACT-08 --> AC-B-DockDevice --> control | AC-C-RentBikeController | // reportBikeRemoved, // handleBikeRemoved | IF-03.onBikeRemoved(event: DockEvent) --> DC-DockEventHandler --> DC-RentBikeService.handleBikeRemoved(event: DockEvent): void |
| UC-005 | 2.1.1 | AC-C-RentBikeController | AC-E-Dock | // releaseBike | DC-Dock.releaseBike(): Bike |
| UC-005 | 2.1.2 | AC-C-RentBikeController | AC-E-Trip | // startTrip | DC-Trip.start(rider, bike, startDock, hold, startTime): Trip |
| UC-005 | 3 | (tự gọi) | AC-C-RentBikeController | // handleRemovalTimeout | IF-06.onTimerFired --> DC-RentalTimerHandler --> DC-RentBikeService.handleRemovalTimeout(requestId: UUID): void |
| UC-005 | 3.1, 3.1.1 | AC-C-RentBikeController | AC-B-DockDevice | // sendLockCommand | IF-02.sendLockCommand(dockId: DockId): void |
| UC-005 | 3.2, 3.2.1 | AC-C-RentBikeController | AC-B-PaymentGateway | // requestCancelHold | IF-01.cancelHold(holdRef: HoldReference): void |
| UC-005 | 3.3 | AC-C-RentBikeController | AC-E-PaymentHold | // markCancelled | DC-PaymentHold.markCancelled(): void |
| UC-007 | 1, 1.1 | ACT-08 --> DockDevice | AC-C-ReturnBikeController | // reportBikeReturned, // handleBikeReturned | IF-03.onBikeReturned --> DC-DockEventHandler --> DC-ReturnBikeService.handleBikeReturned(event: DockEvent): void |
| UC-007 | 1.1.1 | control | AC-E-Dock | // acceptBike | DC-Dock.acceptBike(bike: Bike): void |
| UC-007 | 1.1.2 | control | AC-E-Bike | // getOngoingTrip | IF-08.findInProgressByBike(bikeId: UUID): Optional<Trip> (lý do: P10 bỏ Bike --> Trip) |
| UC-007 | 1.1.3, 1.1.4 | control | AC-E-Trip | // endTrip, // calculateFare | DC-Trip.end(endDock, endTime, calculator): Money; DC-FareCalculator.calculate(duration: Duration): Money |
| UC-007 | 1.1.5, 1.1.5.1 | control | AC-B-PaymentGateway | // requestCapture | IF-01.capture(holdRef: HoldReference, amount: Money): CaptureResult |
| UC-007 | 1.1.6 | control | AC-E-PaymentHold | // recordCapture | DC-PaymentHold.recordCapture(amount: Money): void |
| UC-007 | 1.1.7, 1.1.7.1 | control | AC-B-PaymentGateway | // requestReleaseRemainder | IF-01.releaseRemainder(holdRef: HoldReference, amount: Money): ReleaseResult |
| UC-007 | 1.1.8 | control | AC-E-PaymentHold | // recordRemainderReleased | DC-PaymentHold.recordRemainderReleased(): void |
| UC-007 | 1.1.9 | control | AC-E-Trip | // composeInvoice | DC-Trip.composeInvoice(): TripInvoice |
| UC-007 | 1.1.9.1 | AC-E-Trip | AC-E-RiderAccount | // getContactEmail | DC-RiderAccount.getEmail(): String (gọi từ service qua trip.getRider()) |
| UC-007 | 1.1.10, 1.1.10.1 | control | AC-B-ReturnBikeForm | // sendInvoice, // deliverInvoice | IF-04.sendInvoice(email: String, invoice: TripInvoice): void (chữ ký tạm) |
| UC-009 | 1 | ACT-09 | AC-C-RecordLostBikeController | // notifyTripDurationReached | IF-06.onTimerFired --> DC-RentalTimerHandler --> DC-RecordLostBikeService.handleTripDurationReached(tripId: UUID, now: Instant): void |
| UC-009 | 1.1 | control | AC-E-Trip | // checkExceedsMaxDuration | DC-Trip.exceedsMaxDuration(now: Instant): boolean |
| UC-009 | 1.2 | control | AC-E-Bike | // markLost | DC-Bike.markLost(): void |
| UC-009 | 1.3, 1.3.1 | control | AC-B-PaymentGateway | // requestCapture | IF-01.capture(holdRef, amount) |
| UC-009 | 1.4 | control | AC-E-PaymentHold | // recordCapture | DC-PaymentHold.recordCapture(amount: Money): void |
| UC-009 | 1.5 | control | AC-E-RiderAccount | // lock | DC-RiderAccount.lock(): void |
| UC-013 | 2.1.1, 2.1.2 | AC-C-CreateTransferOrderController | AC-E-Station | // findStation | IF-10.findById(id: UUID): Optional<Station> (control thuộc PKG-11, ngoài phạm vi) |
| UC-013 | 2.1.3 | AC-C-CreateTransferOrderController | AC-E-TransferOrder | // initializeTransferOrder | DC-TransferOrder.create(from, to, requestedBikes): TransferOrder |

## F5. Bảng quan hệ

| ID | Lớp A | Lớp B | Loại | Multiplicity | Điều hướng | Lý do | Vai trò | Căn cứ hiển thị |
|---|---|---|---|---|---|---|---|---|
| R-03 | DC-Trip | DC-RiderAccount | Association | A 0..* - B 1 | A --> B | P08 R-03; chỉ giữ chiều Trip --> RiderAccount; BR-02 kiểm bằng truy vấn IF-08 thay vì duyệt tập chuyến của tài khoản | - / rider | field |
| R-10 | DC-Dock | DC-Bike | Association | A 0..1 - B 0..1 | A --> B | P08 R-10; Dock cần biết xe đang giữ | - / dockedBike | field |
| R-11 | DC-Trip | DC-Bike | Association | A 0..* - B 1 | A --> B | P08 R-11; một chiều theo đề xuất P10 (tránh vòng PKG-15 - PKG-16) | - / bike | field |
| R-12 | DC-Trip | DC-Dock | Association | A 0..* - B 1 | A --> B | P08 R-12 | - / startDock | field |
| R-13 | DC-Trip | DC-PaymentHold | Association | A 0..1 - B 1 | A --> B | P08 R-13 | - / paymentHold | field |
| R-21 | DC-Trip | DC-Dock | Association | A 0..* - B 0..1 | A --> B | P08 R-21 | - / endDock | field |
| R-30 | DC-TransferOrder | DC-Station | Association | A 0..* - B 1 | A --> B | P08 R-30 | - / fromStation | field |
| R-31 | DC-TransferOrder | DC-Station | Association | A 0..* - B 1 | A --> B | P08 R-31 | - / toStation | field |
| R-32 | DC-Dock | DC-Station | Association | A 1..* - B 1 | A --> B | P08 R-32 (Q-34); chiều Dock --> Station đủ cho phạm vi | docks / station | field |
| R-02 | DC-RentBikeService | DC-RiderAccount | Dependency | - | A --> B | P08 R-02 đổi từ association tạm thành dependency: nạp qua IF-07 trong method | - | local |
| R-04 | DC-RentBikeService | DC-Dock | Dependency | - | A --> B | P08 R-04; local | - | local |
| R-05 | DC-RentBikeService | DC-Bike | Dependency | - | A --> B | P08 R-05; local | - | local |
| R-06 | DC-RentBikeService | IF-01 | Association | - | A --> B | P08 R-06; boundary PaymentGateway thành IF-01 (P10); field được tiêm | - / paymentGateway | field |
| R-07 | DC-RentBikeService | DC-PaymentHold | Dependency | - | A --> B | P08 R-07; local | - | local |
| R-08 | DC-RentBikeService | IF-02 | Association | - | A --> B | P08 R-08; chiều nhận sự kiện chuyển sang R-45 qua IF-03 | - / dockCommands | field |
| R-09 | DC-RentBikeService | DC-Trip | Dependency | - | A --> B | P08 R-09; tạo qua Trip.start | - | local |
| R-14 | DC-ReturnBikeService | IF-04 | Association | - | A --> B | P08 R-14; boundary ReturnBikeForm thành SS-03 (P10) | - / invoiceSender | field |
| R-15 | DC-DockEventHandler | DC-ReturnBikeService | Association | - | A --> B | P08 R-15; sự kiện ụ tới control đi qua DockEventHandler (IF-03) | - / returnBikeService | field |
| R-16 | DC-ReturnBikeService | DC-Dock | Dependency | - | A --> B | P08 R-16; local | - | local |
| R-17 | DC-ReturnBikeService | DC-Bike | Dependency | - | A --> B | P08 R-17; local | - | local |
| R-18 | DC-ReturnBikeService | DC-Trip | Dependency | - | A --> B | P08 R-18; local | - | local |
| R-19 | DC-ReturnBikeService | IF-01 | Association | - | A --> B | P08 R-19 | - / paymentGateway | field |
| R-20 | DC-ReturnBikeService | DC-PaymentHold | Dependency | - | A --> B | P08 R-20; local | - | local |
| R-22 | DC-RecordLostBikeService | DC-Trip | Dependency | - | A --> B | P08 R-22; local | - | local |
| R-23 | DC-RecordLostBikeService | DC-Bike | Dependency | - | A --> B | P08 R-23; local | - | local |
| R-24 | DC-RecordLostBikeService | IF-01 | Association | - | A --> B | P08 R-24 | - / paymentGateway | field |
| R-25 | DC-RecordLostBikeService | DC-PaymentHold | Dependency | - | A --> B | P08 R-25; local | - | local |
| R-26 | DC-RecordLostBikeService | DC-RiderAccount | Dependency | - | A --> B | P08 R-26; local | - | local |
| R-33 | DC-RentBikeService | IF-07 | Association | - | A --> B | Nạp tài khoản | - / accounts | field |
| R-34 | DC-RentBikeService | IF-08 | Association | - | A --> B | BR-02, lưu chuyến | - / trips | field |
| R-35 | DC-RentBikeService | IF-11 | Association | - | A --> B | Tìm ụ theo mã QR | - / docks | field |
| R-36 | DC-RentBikeService | IF-09 | Association | - | A --> B | Lưu khoản tạm giữ | - / holds | field |
| R-37 | DC-RentBikeService | IF-14 | Association | - | A --> B | Lưu lượt chờ rút xe | - / requests | field |
| R-38 | DC-RentBikeService | IF-05 | Association | - | A --> B | Hẹn giờ 60 giây, 24 giờ | - / scheduler | field |
| R-39 | DC-ReturnBikeService | IF-08 | Association | - | A --> B | Tìm chuyến theo xe | - / trips | field |
| R-40 | DC-ReturnBikeService | IF-11 | Association | - | A --> B | Nạp ụ | - / docks | field |
| R-41 | DC-ReturnBikeService | IF-05 | Association | - | A --> B | Huỷ mốc 24 giờ | - / scheduler | field |
| R-42 | DC-RecordLostBikeService | IF-08 | Association | - | A --> B | Nạp chuyến | - / trips | field |
| R-43 | DC-DockEventHandler | IF-03 | Realization | - | - | P10 E-21 | - | - |
| R-44 | DC-RentalTimerHandler | IF-06 | Realization | - | - | P10 E-22 | - | - |
| R-45 | DC-DockEventHandler | DC-RentBikeService | Association | - | A --> B | Chuyển sự kiện rút xe | - / rentBikeService | field |
| R-46 | DC-RentalTimerHandler | DC-RentBikeService | Association | - | A --> B | Chuyển mốc 60 giây | - / rentBikeService | field |
| R-47 | DC-RentalTimerHandler | DC-RecordLostBikeService | Association | - | A --> B | Chuyển mốc 24 giờ | - / recordLostBikeService | field |
| R-48 | DC-Trip | DC-FareCalculator | Dependency | - | A --> B | Tham số của Trip.end | - | parameter |
| R-49 | DC-RentalRequest | DC-RiderAccount | Association | A 0..* - B 1 | A --> B | Lượt thuê thuộc một tài khoản | - / rider | field |
| R-50 | DC-RentalRequest | DC-Dock | Association | A 0..1 - B 1 | A --> B | Mỗi ụ có tối đa một lượt chờ (Q-45) | - / dock | field |
| R-51 | DC-RentalRequest | DC-Bike | Association | A 0..* - B 1 | A --> B | Xe được mở khoá | - / bike | field |
| R-52 | DC-RentalRequest | DC-PaymentHold | Association | A 0..1 - B 1 | A --> B | Khoản tạm giữ của lượt | - / hold | field |
| R-53 | DC-ReturnBikeService | DC-FareCalculator | Association | - | A --> B | Truyền vào Trip.end; một thể hiện dùng chung | - / fareCalculator | field |
| R-54 | DC-ReturnBikeService | IF-09 | Association | - | A --> B | Lưu khoản tạm giữ | - / holds | field |
| R-55 | DC-RecordLostBikeService | IF-07 | Association | - | A --> B | Lưu tài khoản bị khoá | - / accounts | field |
| R-56 | DC-RecordLostBikeService | IF-09 | Association | - | A --> B | Lưu khoản tạm giữ | - / holds | field |
| R-57 | DC-RecordLostBikeService | IF-12 | Association | - | A --> B | Lưu xe thất lạc | - / bikes | field |

## F6. State machine

### F6.1 Trạng thái

| ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết | entry | do | exit |
|---|---|---|---|---|---|---|
| ST-01 | DC-Trip | InProgress | status = IN_PROGRESS | - | - | - |
| ST-01 | DC-Trip | Completed | status = COMPLETED, endTime, fare có giá trị | fare = calculator.calculate(endTime - startTime) | - | - |
| ST-02 | DC-PaymentHold | Active | status = ACTIVE | - | - | - |
| ST-02 | DC-PaymentHold | Cancelled | status = CANCELLED | - | - | - |
| ST-02 | DC-PaymentHold | Captured | status = CAPTURED | - | - | - |
| ST-02 | DC-PaymentHold | Settled | status = SETTLED | - | - | - |
| ST-03 | DC-RentalRequest | AwaitingRemoval | status = AWAITING_REMOVAL | - | - | - |
| ST-03 | DC-RentalRequest | Started | status = STARTED | - | - | - |
| ST-03 | DC-RentalRequest | Expired | status = EXPIRED | - | - | - |

### F6.2 Chuyển trạng thái

| STT | ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích | Operation | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ST-01 | DC-Trip | (initial) | start | - | - | InProgress | DC-Trip.start | UC-005 bước 8 |
| 2 | ST-01 | DC-Trip | InProgress | end(endDock, endTime, calculator) | [endTime >= startTime] | / ghi endDock, endTime | Completed | DC-Trip.end | UC-007 bước 3, 4 |
| 3 | ST-01 | DC-Trip | Completed | - | - | - | (final) | - | - |
| 4 | ST-02 | DC-PaymentHold | (initial) | record | - | - | Active | DC-PaymentHold.record | UC-005 bước 5 |
| 5 | ST-02 | DC-PaymentHold | Active | markCancelled | - | - | Cancelled | markCancelled | UC-005 6a2 |
| 6 | ST-02 | DC-PaymentHold | Active | recordCapture(amount) | [amount <= this.amount] | / capturedAmount = amount | Captured | recordCapture | UC-007 bước 5, UC-009 bước 3 |
| 7 | ST-02 | DC-PaymentHold | Captured | recordRemainderReleased | - | - | Settled | recordRemainderReleased | UC-007 bước 6 |
| 8 | ST-02 | DC-PaymentHold | Captured | (hoàn tất) | [remainder = 0] | - | (final) | - | UC-009 |
| 9 | ST-02 | DC-PaymentHold | Cancelled, Settled | - | - | - | (final) | - | - |
| 10 | ST-03 | DC-RentalRequest | (initial) | open | - | - | AwaitingRemoval | DC-RentalRequest.open | UC-005 bước 6 |
| 11 | ST-03 | DC-RentalRequest | AwaitingRemoval | complete | - | - | Started | complete | UC-005 bước 7 |
| 12 | ST-03 | DC-RentalRequest | AwaitingRemoval | expire | [now - createdAt >= 60 giây] | - | Expired | expire | BR-06 |
| 13 | ST-03 | DC-RentalRequest | Started, Expired | - | - | - | (final) | - | - |

### F6.3 Ánh xạ về mô hình lớp

| ST | Thuộc tính biểu diễn trạng thái | Kiểu | Operation được thêm/sửa |
|---|---|---|---|
| ST-01 | DC-Trip.status | TripStatus | start, end |
| ST-02 | DC-PaymentHold.status | HoldStatus | record, markCancelled, recordCapture, recordRemainderReleased |
| ST-03 | DC-RentalRequest.status | RentalRequestStatus | open, complete, expire, isAwaitingRemoval |

### F6.4 Sơ đồ

Files: diagrams/P12-state-DC-Trip.drawio, diagrams/P12-state-DC-PaymentHold.drawio, diagrams/P12-state-DC-RentalRequest.drawio. Node ID theo <ST>-S<n>, <ST>-I, <ST>-F<n>; cạnh <ST>-T<n> theo bảng F6.2 (ST-01-T1 đến T3, ST-02-T1 đến T7, ST-03-T1 đến T5). ST-01 có note ST-01-N1 về Q-04.

## F7. Bảng thuộc tính

| DC | Visibility | Tên | Kiểu | Multiplicity | Mặc định | Ràng buộc | Nguồn |
|---|---|---|---|---|---|---|---|
| DC-RiderAccount | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế: định danh |
| DC-RiderAccount | - | email | String | 1 | - | định dạng email (REQ-02); độ dài chờ Q-47 | AC-E-RiderAccount |
| DC-RiderAccount | - | cardReference | CardReference | 0..1 | - | chỉ mã do cổng cấp (NFR-04) | AC-E-RiderAccount, GL-12 |
| DC-RiderAccount | - | outstandingFare | Money | 1 | Money.ZERO | {>= 0} | AC-E-RiderAccount, GL-14 |
| DC-RiderAccount | - | status | AccountStatus | 1 | ACTIVE | - | AC-E-RiderAccount, BR-10 |
| DC-Trip | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế: định danh |
| DC-Trip | - | startTime | Instant | 1 | - | {readOnly} | AC-E-Trip |
| DC-Trip | - | endTime | Instant | 0..1 | - | > startTime | AC-E-Trip |
| DC-Trip | - | fare | Money | 0..1 | - | {>= 0} | AC-E-Trip, GL-05 |
| DC-Trip | - | status | TripStatus | 1 | IN_PROGRESS | - | ST-01 |
| DC-Trip | + | MAX_DURATION | Duration | 1 | 24 giờ | {readOnly}, Classifier | BR-09 |
| DC-FareCalculator | + | FREE_PERIOD | Duration | 1 | 30 phút | {readOnly}, Classifier | BR-07 |
| DC-FareCalculator | + | BLOCK | Duration | 1 | 15 phút | {readOnly}, Classifier | BR-07 |
| DC-FareCalculator | + | BLOCK_PRICE | Money | 1 | 5.000 đồng | {readOnly}, Classifier | BR-07 |
| DC-PaymentHold | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế |
| DC-PaymentHold | - | holdReference | HoldReference | 1 | - | {readOnly, unique} | AC-E-PaymentHold; Q-30 |
| DC-PaymentHold | - | amount | Money | 1 | - | = 200.000 đồng khi tạo (BR-05) | AC-E-PaymentHold |
| DC-PaymentHold | - | capturedAmount | Money | 0..1 | - | 0 <= capturedAmount <= amount | AC-E-PaymentHold |
| DC-PaymentHold | - | status | HoldStatus | 1 | ACTIVE | - | ST-02 |
| DC-PaymentHold | - | /remainder | Money | 1 | - | Derived: amount - capturedAmount; không lưu | P07 UC-007 msg 1.1.7 |
| DC-RentalRequest | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế; dùng làm requestId của IF-01, IF-02 |
| DC-RentalRequest | - | createdAt | Instant | 1 | - | {readOnly} | BR-06 (mốc 60 giây, Q-10) |
| DC-RentalRequest | - | status | RentalRequestStatus | 1 | AWAITING_REMOVAL | - | ST-03 |
| DC-RentalRequest | + | REMOVAL_TIMEOUT | Duration | 1 | 60 giây | {readOnly}, Classifier | BR-06 |
| DC-Money | - | amount | long | 1 | - | {>= 0, readOnly}; đơn vị đồng | GL-05 |
| DC-Money | + | ZERO | Money | 1 | 0 | {readOnly}, Classifier | Thiết kế |
| DC-CardReference | - | value | String | 1 | - | không rỗng; định dạng chờ Q-42 | GL-12 |
| DC-HoldReference | - | value | String | 1 | - | không rỗng (Q-30) | Q-30 |
| DC-TripInvoice | - | startTime | Instant | 1 | - | - | Q-24 |
| DC-TripInvoice | - | endTime | Instant | 1 | - | - | Q-24 |
| DC-TripInvoice | - | fare | Money | 1 | - | - | Q-24 |
| DC-Station | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế |
| DC-Station | - | name | String | 1 | - | độ dài chờ Q-47 | AC-E-Station |
| DC-Dock | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế; dùng làm DockId của IF-02 (Q-36) |
| DC-Dock | - | qrCode | String | 1 | - | {unique}; định dạng chờ Q-40 | AC-E-Dock, GL-11 |
| DC-Bike | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế |
| DC-Bike | - | status | BikeStatus | 1 | AVAILABLE | - | AC-E-Bike, GL-22 |
| DC-TransferOrder | - | id | UUID | 1 | - | {readOnly, unique} | Thiết kế |
| DC-TransferOrder | - | status | TransferOrderStatus | 1 | PENDING | - | GL-09 |
| DC-TransferOrder | - | requestedBikes | Chưa quy định (Q-25) | 1 | - | Q-25 | AC-E-TransferOrder |
| DC-RentalOutcome | - | accepted | boolean | 1 | - | - | UC-005 |
| DC-RentalOutcome | - | rejectionReason | String | 0..1 | - | chờ Q-22 | UC-005 2a-5a |

## F8. Class diagram

| Sơ đồ | Phạm vi | File .drawio | Số lớp |
|---|---|---|---|
| RentalDomain | PKG-15 | diagrams/P12-class-PKG-15.drawio | 20 (2 tham chiếu) |
| FleetDomain | PKG-16 | diagrams/P12-class-PKG-16.drawio | 10 |
| Rental | PKG-09 | diagrams/P12-class-PKG-09.drawio | 19 (14 tham chiếu) |

Bảng Node của mỗi sơ đồ: ID trùng DC hoặc IF ở F1, ngăn thuộc tính và operation lấy từ F7, F2 (lớp ngoài package chỉ ghi tên, "tham chiếu"). Bảng Edge: mọi quan hệ ở F5 có cả hai lớp trong sơ đồ, ID trùng R-nn; association một chiều vẽ đầu mở, multiplicity và vai trò là nhãn con ở hai đầu.

## F9. Gán package và kiểm tra phụ thuộc package

| PKG | Lớp (DC) | Phụ thuộc vào PKG | Hợp lệ theo P09 |
|---|---|---|---|
| PKG-09 | DC-RentBikeService, DC-ReturnBikeService, DC-RecordLostBikeService, DC-DockEventHandler, DC-RentalTimerHandler, DC-RentalOutcome | PKG-15, PKG-16, PKG-18 (IF-01), PKG-19 (IF-02, IF-03), PKG-20 (IF-04), PKG-21 (IF-05, IF-06) | Có (nới lỏng, qua interface) |
| PKG-15 | DC-RiderAccount, DC-Trip, DC-FareCalculator, DC-PaymentHold, DC-RentalRequest, DC-Money, DC-CardReference, DC-HoldReference, DC-TripInvoice, 5 enumeration, IF-07, IF-08, IF-09, IF-14 | PKG-16 (R-11, R-12, R-21, R-50, R-51) | Có |
| PKG-16 | DC-Station, DC-Dock, DC-Bike, DC-TransferOrder, 2 enumeration, IF-10 đến IF-13 | Không | Có |
| PKG-18, PKG-19 | (ngoài phạm vi) | PKG-15 (Money, CardReference, HoldReference trong chữ ký IF-01); PKG-16 (DockId) | Không: layer dưới phụ thuộc layer trên (P11b Vấn đề còn mở) |

## F10. Design pattern đã áp dụng

| Pattern | Vấn đề trong thiết kế này | Lớp tham gia | Lý do chọn | Phương án đơn giản hơn đã xét |
|---|---|---|---|---|
| Repository | Tách truy cập dữ liệu khỏi lớp miền và dịch vụ | IF-07 đến IF-14; hiện thực ở PKG-17 | MAU_THIET_KE_DA_CHOT; P09 F5 | Dịch vụ gọi ORM trực tiếp: vi phạm quy tắc layer của P09 |
| Observer (listener) | Subsystem layer dưới phải báo sự kiện lên layer ứng dụng không tạo phụ thuộc ngược | IF-03, IF-06 (Subject: SS-02, SS-04; Observer: DC-DockEventHandler, DC-RentalTimerHandler) | P09 F6 | Subsystem gọi thẳng dịch vụ: phụ thuộc ngược layer |
| Value Object | Tiền không âm, không dùng số thực | DC-Money, DC-CardReference, DC-HoldReference | QUY_UOC_KIEU_DU_LIEU; F12 "không dùng float cho tiền" | long trần: không kiểm soát được âm và đơn vị |

Không dùng Strategy cho DC-FareCalculator: chỉ có một công thức (BR-07); nếu Q-15 xác nhận bảng giá cước thay đổi được thì cân nhắc lại.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-46 | Thời lượng chuyến để tính cước tính tới giây hay làm tròn phút trước (ví dụ 30 phút 20 giây có bị tính 5.000 đồng không)? | DC-FareCalculator.calculate | Mục 4 "mỗi 15 phút hoặc phần lẻ" |
| Q-47 | Độ dài tối đa của email, tên trạm, mã QR là bao nhiêu? | F7, P13 | Nguồn không nêu |

Liên quan: Q-02, Q-04, Q-15, Q-20, Q-21, Q-22, Q-23, Q-25, Q-27, Q-30, Q-31, Q-33, Q-34, Q-45.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | IF-14 IRentalRequestRepository, DC-RentalRequest | P12 cần kho dữ liệu cho lớp mới RentalRequest; C3 chỉ cho P10, P11b cấp mã IF | Cấp IF-14 trong P10 bảng phần tử mới do cơ chế kiến trúc |
| P11b | SS-03, SS-04 | P12 cần chữ ký IF-04, IF-05, IF-06 | Chạy P11b cho SS-03, SS-04; thay chữ ký tạm ở F2 |
| P07 | UC-005 | Không có message hẹn mốc 24 giờ khi chuyến bắt đầu; UC-009 do ACT-09 kích hoạt nhưng không bước nào đăng ký mốc đó | Thêm message "// scheduleMaxDurationCheck" sau 2.1.2 |
| P07 | UC-007 | Không có message huỷ mốc 24 giờ khi chuyến kết thúc | Thêm message sau 1.1.3 |

## Vấn đề còn mở

- Phạm vi chỉ gồm 3 package; PKG-05, PKG-06, PKG-11, PKG-17 đến PKG-23 chưa thiết kế lớp.
- Target 1: DC-RentalEndpoint, DC-TransferOrderEndpoint và lớp giao diện ngoài phạm vi.
- Target 13: dependency R-02, R-04, R-05, R-07, R-09, R-16 đến R-18, R-20, R-22, R-23, R-25, R-26 (dịch vụ --> entity) có trong F5 nhưng không vẽ trên P12-class-PKG-09 vì entity thuộc sơ đồ PKG-15, PKG-16; sơ đồ đã có 19 lớp.
- Số tiền 200.000 đồng (BR-05) xuất hiện trong method requestRental; nên thành hằng HOLD_AMOUNT của DC-PaymentHold. Chưa sửa để giữ F7 khớp F2.
- DC-TransferOrder.requestedBikes chưa có kiểu (Q-25).
- Enumeration trong F1 ghi giá trị ở cột Ghi chú; F7 không liệt kê giá trị enumeration.
