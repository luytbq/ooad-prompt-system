# P13 - Mô hình dữ liệu - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P13 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CONG_NGHE: PostgreSQL 16); P12-class-design/PKG-09-15-16-rental-core.md 1.0; P06; P04 (4 UC); P09; P05 |
| Phạm vi | Lớp persistent của PKG-15, PKG-16 (phạm vi P12 đã có) |

Placeholder: LOAI_CSDL = Không có; QUY_UOC_CSDL = Không có; KHOI_LUONG_DU_LIEU = Không có; SINH_DDL = "Có, cú pháp PostgreSQL"; YEU_CAU_BO_SUNG = Không có.

## F1. Quyết định loại CSDL

| Hạng mục | Quyết định | Căn cứ |
|---|---|---|
| Loại CSDL | Quan hệ | P09 F7 (giao dịch nhiều đối tượng khi thuê, trả xe; báo cáo UC-024) |
| Hệ quản trị | PostgreSQL 16 | CONG_NGHE |
| Chiến lược khoá chính | Khoá thay thế UUID tên id, sinh bằng gen_random_uuid() | P12 đã chọn id: UUID cho mọi entity (QUY_UOC_KIEU_DU_LIEU của P12). Mặc định của bước (BIGINT tự tăng) không dùng để không lệch P12 (C1.3) |
| Quy ước tên | Bảng số ít snake_case; ràng buộc pk_, fk_<bang>_<cot bỏ _id>, uq_, ck_, ix_, ux_ | NGON_NGU_TEN_PHAN_TU; mặc định của bước |
| Tiền | BIGINT, đơn vị đồng | DC-Money bọc long; không dùng số thực |
| Thời điểm | TIMESTAMPTZ | Instant (UTC) |

## F2. Bảng lớp persistent và chiến lược ánh xạ

| DC | Persistent | Thực thể | TBL | Chiến lược | Lý do |
|---|---|---|---|---|---|
| DC-RiderAccount | Có | E-RiderAccount | TBL-01 | Một lớp - một bảng | - |
| DC-Station | Có | E-Station | TBL-02 | Một lớp - một bảng | - |
| DC-Dock | Có | E-Dock | TBL-03 | Một lớp - một bảng | - |
| DC-Bike | Có | E-Bike | TBL-04 | Một lớp - một bảng | - |
| DC-PaymentHold | Có | E-PaymentHold | TBL-05 | Một lớp - một bảng | - |
| DC-Trip | Có | E-Trip | TBL-06 | Một lớp - một bảng | - |
| DC-RentalRequest | Có | E-RentalRequest | TBL-07 | Một lớp - một bảng | - |
| DC-TransferOrder | Có | E-TransferOrder | TBL-08 | Một lớp - một bảng | - |
| DC-Money, DC-CardReference, DC-HoldReference | Không (value object) | - | - | Nhúng vào TBL-01, TBL-05, TBL-06 | Một cột mỗi value object |
| DC-TripInvoice | Không | - | - | - | Chỉ tạo khi gửi email (Q-32) |
| DC-FareCalculator, DC-RentalOutcome | Không | - | - | - | Không trạng thái lưu trữ |
| Enumeration (7) | Không | - | - | CHECK trên cột | Tập giá trị cố định |
| DC-RentBikeService, DC-ReturnBikeService, DC-RecordLostBikeService, DC-DockEventHandler, DC-RentalTimerHandler | Không | - | - | - | Control |

## F3. Mô hình khái niệm (ER)

### F3.1 Thực thể

| E | Tên thực thể | Mô tả | Định danh | Thuộc tính | Thực thể yếu | Nguồn DC |
|---|---|---|---|---|---|---|
| E-RiderAccount | Tài khoản người thuê xe | GL-13 | id (thay thế) | email (khoá ứng viên), cardReference, outstandingFare, status | Không | DC-RiderAccount |
| E-Station | Trạm | GL-19 | id | name | Không | DC-Station |
| E-Dock | Ụ khoá | GL-23 | id | qrCode (khoá ứng viên) | Không | DC-Dock |
| E-Bike | Xe | GL-25 | id | status | Không | DC-Bike |
| E-PaymentHold | Khoản tạm giữ | GL-08 | id | holdReference (khoá ứng viên), amount, capturedAmount, status; /remainder dẫn xuất | Không | DC-PaymentHold |
| E-Trip | Chuyến đi | GL-04 | id | startTime, endTime, fare, status | Không | DC-Trip |
| E-RentalRequest | Lượt thuê chờ rút xe | P12 thiết kế | id | createdAt, status | Không | DC-RentalRequest |
| E-TransferOrder | Lệnh điều chuyển | GL-09 | id | requestedBikes (Q-25), status | Không | DC-TransferOrder |

### F3.2 Mối quan hệ

| ER | Tên | A | B | Bản số | Tham gia A, B | Thuộc tính | Nguồn R |
|---|---|---|---|---|---|---|---|
| ER-01 | thực hiện | E-RiderAccount | E-Trip | 1:N | A tuỳ chọn, B bắt buộc | - | R-03 |
| ER-02 | giữ | E-Dock | E-Bike | 1:1 | A tuỳ chọn, B tuỳ chọn | - | R-10 |
| ER-03 | dùng xe | E-Trip | E-Bike | N:1 | A tuỳ chọn, B bắt buộc | - | R-11 |
| ER-04 | bắt đầu tại | E-Trip | E-Dock | N:1 | B bắt buộc | - | R-12 |
| ER-05 | kết thúc tại | E-Trip | E-Dock | N:1 | B tuỳ chọn | - | R-21 |
| ER-06 | được bảo đảm bởi | E-Trip | E-PaymentHold | 1:1 | A tuỳ chọn, B bắt buộc | - | R-13 |
| ER-07 | thuộc | E-Dock | E-Station | N:1 | A bắt buộc (1..*), B bắt buộc | - | R-32 |
| ER-08 | lấy xe từ, chuyển tới | E-TransferOrder | E-Station | N:1 (hai mối quan hệ) | B bắt buộc | - | R-30, R-31 |
| ER-09 | yêu cầu (lượt thuê) | E-RentalRequest | E-RiderAccount, E-Dock, E-Bike, E-PaymentHold | N:1 (bốn mối quan hệ, PaymentHold 1:1) | bắt buộc | - | R-49 đến R-52 |

## F4. Mô hình logic

### F4.1 Lược đồ quan hệ

| TBL | Tên bảng | Lược đồ | Khoá ứng viên khác | Nguồn |
|---|---|---|---|---|
| TBL-01 | rider_account | rider_account(PK: id, email, card_reference, outstanding_fare, status) | email | E-RiderAccount |
| TBL-02 | station | station(PK: id, name) | - | E-Station |
| TBL-03 | dock | dock(PK: id, qr_code, FK: station_id, FK: docked_bike_id) | qr_code; docked_bike_id | E-Dock |
| TBL-04 | bike | bike(PK: id, status) | - | E-Bike |
| TBL-05 | payment_hold | payment_hold(PK: id, hold_reference, amount, captured_amount, status) | hold_reference | E-PaymentHold |
| TBL-06 | trip | trip(PK: id, FK: rider_account_id, FK: bike_id, FK: start_dock_id, FK: end_dock_id, FK: payment_hold_id, start_time, end_time, fare, status) | payment_hold_id | E-Trip |
| TBL-07 | rental_request | rental_request(PK: id, FK: rider_account_id, FK: dock_id, FK: bike_id, FK: payment_hold_id, created_at, status) | payment_hold_id | E-RentalRequest |
| TBL-08 | transfer_order | transfer_order(PK: id, FK: from_station_id, FK: to_station_id, requested_bikes, status) | - | E-TransferOrder |

### F4.2 Ánh xạ quan hệ giữa lớp

| R | Loại | Multiplicity | Cách ánh xạ | FK hoặc bảng trung gian | Kiểu | ON DELETE |
|---|---|---|---|---|---|---|
| R-03 | Association | Trip 0..* - RiderAccount 1 | FK ở phía N | trip.rider_account_id NOT NULL | độc lập | RESTRICT |
| R-10 | Association | Dock 0..1 - Bike 0..1 | 1-1, FK ở phía Dock kèm UNIQUE | dock.docked_bike_id NULL UNIQUE | độc lập | SET NULL |
| R-11 | Association | Trip 0..* - Bike 1 | FK phía N | trip.bike_id NOT NULL | độc lập | RESTRICT |
| R-12 | Association | Trip 0..* - Dock 1 | FK phía N | trip.start_dock_id NOT NULL | độc lập | RESTRICT |
| R-21 | Association | Trip 0..* - Dock 0..1 | FK phía N | trip.end_dock_id NULL | độc lập | RESTRICT |
| R-13 | Association | Trip 0..1 - PaymentHold 1 | 1-1, FK ở phía tuỳ chọn (Trip) kèm UNIQUE | trip.payment_hold_id NOT NULL UNIQUE | độc lập | RESTRICT |
| R-32 | Association | Dock 1..* - Station 1 | FK phía N | dock.station_id NOT NULL | độc lập | RESTRICT |
| R-30, R-31 | Association | TransferOrder 0..* - Station 1 | FK phía N | transfer_order.from_station_id, to_station_id NOT NULL | độc lập | RESTRICT |
| R-49, R-51 | Association | RentalRequest 0..* - RiderAccount 1, Bike 1 | FK phía N | rental_request.rider_account_id, bike_id | độc lập | RESTRICT |
| R-50 | Association | RentalRequest 0..1 - Dock 1 | FK phía N; "0..1" chỉ áp dụng cho lượt đang chờ, hiện thực bằng index duy nhất một phần | rental_request.dock_id; ux_rental_request_dock_awaiting | độc lập | RESTRICT |
| R-52 | Association | RentalRequest 0..1 - PaymentHold 1 | FK kèm UNIQUE | rental_request.payment_hold_id UNIQUE | độc lập | RESTRICT |
| R-48, R-02 đến R-26 (dependency) | Dependency | - | Không ánh xạ | - | - | - |

### F4.3 Ánh xạ generalization

Không có cây kế thừa persistent.

## F5. Chuẩn hoá

### F5.1 Bảng kiểm tra

| TBL | Khoá | FD | 1NF | 2NF | 3NF | BCNF | Kết luận |
|---|---|---|---|---|---|---|---|
| TBL-01 | id; email | id --> mọi cột; email --> id | Đạt | Đạt (khoá đơn) | Đạt | Đạt (hai khoá đơn, không chồng lấn) | 3NF |
| TBL-02 | id | id --> name | Đạt | Đạt | Đạt | Đạt | 3NF |
| TBL-03 | id; qr_code; docked_bike_id | id --> qr_code, station_id, docked_bike_id; qr_code --> id | Đạt | Đạt | Đạt | Đạt | 3NF |
| TBL-04 | id | id --> status | Đạt | Đạt | Đạt | Đạt | 3NF |
| TBL-05 | id; hold_reference | id --> mọi cột | Đạt | Đạt | Đạt | Đạt | 3NF |
| TBL-06 | id; payment_hold_id | id --> mọi cột. fare phụ thuộc (start_time, end_time) qua BR-07 | Đạt | Đạt | Không đạt theo nghĩa hẹp: fare là dẫn xuất từ start_time, end_time | Đạt | Giữ fare có chủ đích (F5.3) |
| TBL-07 | id; payment_hold_id | id --> mọi cột | Đạt | Đạt | Đạt | Đạt | 3NF |
| TBL-08 | id | id --> mọi cột | Đạt (requested_bikes nếu là danh sách xe thì vi phạm 1NF, Q-25) | Đạt | Đạt | Đạt | 3NF có điều kiện |

### F5.2 Quá trình tách

Không có bảng phải tách.

### F5.3 Phi chuẩn hoá có chủ đích

| TBL.cột | Dạng | Lý do | Cơ chế giữ nhất quán |
|---|---|---|---|
| trip.fare | Lưu giá trị dẫn xuất | Giá trị lịch sử: cước đã thu không được đổi nếu BR-07 hoặc bảng giá cước đổi sau này (Q-15); cước là số tiền đã thu từ khoản tạm giữ | Ghi một lần trong Trip.end; không cập nhật lại |

## F6. Mô hình vật lý

### F6.1 Bảng cột

| TBL | Tên bảng | Cột | Kiểu | PK/FK/UNIQUE | NULL | Mặc định | Nguồn DC | Tham chiếu FK | CHECK / mô tả |
|---|---|---|---|---|---|---|---|---|---|
| TBL-01 | rider_account | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-RiderAccount.id | - | - |
| TBL-01 | rider_account | email | VARCHAR(254) | UQ | NOT NULL | - | DC-RiderAccount.email | - | Độ dài 254 theo RFC 5321, chờ Q-47 |
| TBL-01 | rider_account | card_reference | VARCHAR(100) | - | NULL | - | DC-RiderAccount.cardReference | - | Chỉ mã tham chiếu (NFR-04); độ dài chờ Q-42 |
| TBL-01 | rider_account | outstanding_fare | BIGINT | - | NOT NULL | 0 | DC-RiderAccount.outstandingFare | - | CHECK (outstanding_fare >= 0); đồng |
| TBL-01 | rider_account | status | VARCHAR(10) | - | NOT NULL | 'ACTIVE' | DC-RiderAccount.status | - | CHECK (status IN ('ACTIVE','LOCKED')) |
| TBL-02 | station | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-Station.id | - | - |
| TBL-02 | station | name | VARCHAR(100) | - | NOT NULL | - | DC-Station.name | - | Độ dài chờ Q-47 |
| TBL-03 | dock | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-Dock.id | - | - |
| TBL-03 | dock | qr_code | VARCHAR(100) | UQ | NOT NULL | - | DC-Dock.qrCode | - | Định dạng, độ dài chờ Q-40 |
| TBL-03 | dock | station_id | UUID | FK | NOT NULL | - | R-32 | TBL-02.id, RESTRICT, NO ACTION | - |
| TBL-03 | dock | docked_bike_id | UUID | FK, UQ | NULL | - | R-10 | TBL-04.id, SET NULL, NO ACTION | Một xe ở tối đa một ụ |
| TBL-04 | bike | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-Bike.id | - | - |
| TBL-04 | bike | status | VARCHAR(25) | - | NOT NULL | 'AVAILABLE' | DC-Bike.status | - | CHECK (status IN ('AVAILABLE','AWAITING_INSPECTION','LOST')); Q-27 |
| TBL-05 | payment_hold | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-PaymentHold.id | - | - |
| TBL-05 | payment_hold | hold_reference | VARCHAR(100) | UQ | NOT NULL | - | DC-PaymentHold.holdReference | - | Q-30 |
| TBL-05 | payment_hold | amount | BIGINT | - | NOT NULL | - | DC-PaymentHold.amount | - | CHECK (amount > 0) |
| TBL-05 | payment_hold | captured_amount | BIGINT | - | NULL | - | DC-PaymentHold.capturedAmount | - | CHECK (captured_amount BETWEEN 0 AND amount) |
| TBL-05 | payment_hold | status | VARCHAR(10) | - | NOT NULL | 'ACTIVE' | DC-PaymentHold.status | - | CHECK (status IN ('ACTIVE','CANCELLED','CAPTURED','SETTLED')) |
| TBL-06 | trip | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-Trip.id | - | - |
| TBL-06 | trip | rider_account_id | UUID | FK | NOT NULL | - | R-03 | TBL-01.id, RESTRICT | - |
| TBL-06 | trip | bike_id | UUID | FK | NOT NULL | - | R-11 | TBL-04.id, RESTRICT | - |
| TBL-06 | trip | start_dock_id | UUID | FK | NOT NULL | - | R-12 | TBL-03.id, RESTRICT | - |
| TBL-06 | trip | end_dock_id | UUID | FK | NULL | - | R-21 | TBL-03.id, RESTRICT | - |
| TBL-06 | trip | payment_hold_id | UUID | FK, UQ | NOT NULL | - | R-13 | TBL-05.id, RESTRICT | - |
| TBL-06 | trip | start_time | TIMESTAMPTZ | - | NOT NULL | - | DC-Trip.startTime | - | - |
| TBL-06 | trip | end_time | TIMESTAMPTZ | - | NULL | - | DC-Trip.endTime | - | CHECK (end_time IS NULL OR end_time >= start_time) |
| TBL-06 | trip | fare | BIGINT | - | NULL | - | DC-Trip.fare | - | CHECK (fare >= 0) |
| TBL-06 | trip | status | VARCHAR(12) | - | NOT NULL | 'IN_PROGRESS' | DC-Trip.status | - | CHECK (status IN ('IN_PROGRESS','COMPLETED')); CHECK ((status = 'COMPLETED') = (end_time IS NOT NULL AND fare IS NOT NULL AND end_dock_id IS NOT NULL)) |
| TBL-07 | rental_request | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-RentalRequest.id | - | - |
| TBL-07 | rental_request | rider_account_id | UUID | FK | NOT NULL | - | R-49 | TBL-01.id, RESTRICT | - |
| TBL-07 | rental_request | dock_id | UUID | FK | NOT NULL | - | R-50 | TBL-03.id, RESTRICT | - |
| TBL-07 | rental_request | bike_id | UUID | FK | NOT NULL | - | R-51 | TBL-04.id, RESTRICT | - |
| TBL-07 | rental_request | payment_hold_id | UUID | FK, UQ | NOT NULL | - | R-52 | TBL-05.id, RESTRICT | - |
| TBL-07 | rental_request | created_at | TIMESTAMPTZ | - | NOT NULL | now() | DC-RentalRequest.createdAt | - | - |
| TBL-07 | rental_request | status | VARCHAR(16) | - | NOT NULL | 'AWAITING_REMOVAL' | DC-RentalRequest.status | - | CHECK (status IN ('AWAITING_REMOVAL','STARTED','EXPIRED')) |
| TBL-08 | transfer_order | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-TransferOrder.id | - | - |
| TBL-08 | transfer_order | from_station_id | UUID | FK | NOT NULL | - | R-30 | TBL-02.id, RESTRICT | - |
| TBL-08 | transfer_order | to_station_id | UUID | FK | NOT NULL | - | R-31 | TBL-02.id, RESTRICT | Trạm trùng nhau: Q-33 |
| TBL-08 | transfer_order | requested_bikes | (Q-25) | - | NOT NULL | - | DC-TransferOrder.requestedBikes | - | Kiểu chờ Q-25 |
| TBL-08 | transfer_order | status | VARCHAR(10) | - | NOT NULL | 'PENDING' | DC-TransferOrder.status | - | CHECK (status IN ('PENDING','COMPLETED')) |

### F6.2 Ánh xạ kiểu

| Kiểu thiết kế | Kiểu vật lý |
|---|---|
| UUID | UUID |
| String | VARCHAR(n) |
| Money (long, đồng) | BIGINT |
| Instant | TIMESTAMPTZ |
| Enumeration | VARCHAR(n) + CHECK |

### F6.3 Index

| TBL | Tên index | Cột | Loại | Phục vụ truy vấn |
|---|---|---|---|---|
| TBL-06 | ux_trip_rider_in_progress | rider_account_id WHERE status = 'IN_PROGRESS' | UNIQUE một phần | IF-08.existsInProgressByRider (UC-005 bước 2); đồng thời chặn hai chuyến đang diễn ra của một tài khoản (BR-02) khi hai yêu cầu song song |
| TBL-06 | ux_trip_bike_in_progress | bike_id WHERE status = 'IN_PROGRESS' | UNIQUE một phần | IF-08.findInProgressByBike (UC-007 bước 3) |
| TBL-07 | ux_rental_request_dock_awaiting | dock_id WHERE status = 'AWAITING_REMOVAL' | UNIQUE một phần | IF-14.findAwaitingByDock (UC-005 bước 7); R-50 |
| TBL-07 | ux_rental_request_rider_awaiting | rider_account_id WHERE status = 'AWAITING_REMOVAL' | UNIQUE một phần | Chặn hai lượt thuê chờ song song của một tài khoản (mở rộng BR-02 cho khoảng chờ rút xe, xem Vấn đề còn mở) |
| TBL-03 | ix_dock_station | station_id | thường | Đếm ụ, xe theo trạm (UC-004, UC-012 chưa phân tích; NFR-01) |
| TBL-03 | uq_dock_qr_code | qr_code | UNIQUE (có sẵn) | IF-11.findByQrCode (UC-005 bước 3, NFR-02) |

FK khác (trip.start_dock_id, end_dock_id, rental_request.bike_id...) không có index: không có truy vấn trong UC đã phân tích lọc theo các cột này; xoá bảng cha bị RESTRICT và hiếm.

## F7. Mô hình tài liệu

Không áp dụng (CSDL quan hệ).

## F8. ERD

File diagrams/P13-erd-logical.drawio. ER khái niệm (DAY_DU) không vẽ, xem Vấn đề còn mở.

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| TBL-01 đến TBL-08 | Table | rider_account, station, dock, bike, payment_hold, trip, rental_request, transfer_order | - | - | Cột theo F6.1 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
|---|---|---|---|---|---|
| fk_dock_station | TBL-02 | TBL-03 | Độc lập | ERmandOne - ERoneToMany | - |
| fk_dock_docked_bike | TBL-04 | TBL-03 | Độc lập | ERzeroToOne - ERzeroToOne | UNIQUE |
| fk_trip_rider_account | TBL-01 | TBL-06 | Độc lập | ERmandOne - ERzeroToMany | - |
| fk_trip_bike | TBL-04 | TBL-06 | Độc lập | ERmandOne - ERzeroToMany | - |
| fk_trip_start_dock | TBL-03 | TBL-06 | Độc lập | ERmandOne - ERzeroToMany | - |
| fk_trip_end_dock | TBL-03 | TBL-06 | Độc lập | ERzeroToOne - ERzeroToMany | - |
| fk_trip_payment_hold | TBL-05 | TBL-06 | Độc lập | ERmandOne - ERzeroToOne | UNIQUE |
| fk_rental_request_rider_account | TBL-01 | TBL-07 | Độc lập | ERmandOne - ERzeroToMany | - |
| fk_rental_request_dock | TBL-03 | TBL-07 | Độc lập | ERmandOne - ERzeroToMany | - |
| fk_rental_request_bike | TBL-04 | TBL-07 | Độc lập | ERmandOne - ERzeroToMany | - |
| fk_rental_request_payment_hold | TBL-05 | TBL-07 | Độc lập | ERmandOne - ERzeroToOne | UNIQUE |
| fk_transfer_order_from_station | TBL-02 | TBL-08 | Độc lập | ERmandOne - ERzeroToMany | - |
| fk_transfer_order_to_station | TBL-02 | TBL-08 | Độc lập | ERmandOne - ERzeroToMany | - |

## F9. Script DDL

```sql
CREATE TABLE rider_account (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    email VARCHAR(254) NOT NULL,
    card_reference VARCHAR(100) NULL,
    outstanding_fare BIGINT NOT NULL DEFAULT 0,
    status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE',
    CONSTRAINT pk_rider_account PRIMARY KEY (id),
    CONSTRAINT uq_rider_account_email UNIQUE (email),
    CONSTRAINT ck_rider_account_outstanding_fare CHECK (outstanding_fare >= 0),
    CONSTRAINT ck_rider_account_status CHECK (status IN ('ACTIVE','LOCKED'))
);

CREATE TABLE station (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    CONSTRAINT pk_station PRIMARY KEY (id)
);

CREATE TABLE bike (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    status VARCHAR(25) NOT NULL DEFAULT 'AVAILABLE',
    CONSTRAINT pk_bike PRIMARY KEY (id),
    CONSTRAINT ck_bike_status CHECK (status IN ('AVAILABLE','AWAITING_INSPECTION','LOST'))
);

CREATE TABLE payment_hold (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    hold_reference VARCHAR(100) NOT NULL,
    amount BIGINT NOT NULL,
    captured_amount BIGINT NULL,
    status VARCHAR(10) NOT NULL DEFAULT 'ACTIVE',
    CONSTRAINT pk_payment_hold PRIMARY KEY (id),
    CONSTRAINT uq_payment_hold_hold_reference UNIQUE (hold_reference),
    CONSTRAINT ck_payment_hold_amount CHECK (amount > 0),
    CONSTRAINT ck_payment_hold_captured_amount CHECK (captured_amount BETWEEN 0 AND amount),
    CONSTRAINT ck_payment_hold_status CHECK (status IN ('ACTIVE','CANCELLED','CAPTURED','SETTLED'))
);

CREATE TABLE dock (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    qr_code VARCHAR(100) NOT NULL,
    station_id UUID NOT NULL,
    docked_bike_id UUID NULL,
    CONSTRAINT pk_dock PRIMARY KEY (id),
    CONSTRAINT uq_dock_qr_code UNIQUE (qr_code),
    CONSTRAINT fk_dock_station FOREIGN KEY (station_id) REFERENCES station(id) ON DELETE RESTRICT,
    CONSTRAINT uq_dock_docked_bike_id UNIQUE (docked_bike_id),
    CONSTRAINT fk_dock_docked_bike FOREIGN KEY (docked_bike_id) REFERENCES bike(id) ON DELETE SET NULL
);

CREATE TABLE trip (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    rider_account_id UUID NOT NULL,
    bike_id UUID NOT NULL,
    start_dock_id UUID NOT NULL,
    end_dock_id UUID NULL,
    payment_hold_id UUID NOT NULL,
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ NULL,
    fare BIGINT NULL,
    status VARCHAR(12) NOT NULL DEFAULT 'IN_PROGRESS',
    CONSTRAINT pk_trip PRIMARY KEY (id),
    CONSTRAINT fk_trip_rider_account FOREIGN KEY (rider_account_id) REFERENCES rider_account(id) ON DELETE RESTRICT,
    CONSTRAINT fk_trip_bike FOREIGN KEY (bike_id) REFERENCES bike(id) ON DELETE RESTRICT,
    CONSTRAINT fk_trip_start_dock FOREIGN KEY (start_dock_id) REFERENCES dock(id) ON DELETE RESTRICT,
    CONSTRAINT fk_trip_end_dock FOREIGN KEY (end_dock_id) REFERENCES dock(id) ON DELETE RESTRICT,
    CONSTRAINT uq_trip_payment_hold_id UNIQUE (payment_hold_id),
    CONSTRAINT fk_trip_payment_hold FOREIGN KEY (payment_hold_id) REFERENCES payment_hold(id) ON DELETE RESTRICT,
    CONSTRAINT ck_trip_end_time CHECK (end_time IS NULL OR end_time >= start_time),
    CONSTRAINT ck_trip_fare CHECK (fare >= 0),
    CONSTRAINT ck_trip_status CHECK (status IN ('IN_PROGRESS','COMPLETED')),
    CONSTRAINT ck_trip_status_1 CHECK ((status = 'COMPLETED') = (end_time IS NOT NULL AND fare IS NOT NULL AND end_dock_id IS NOT NULL))
);

CREATE TABLE rental_request (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    rider_account_id UUID NOT NULL,
    dock_id UUID NOT NULL,
    bike_id UUID NOT NULL,
    payment_hold_id UUID NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    status VARCHAR(16) NOT NULL DEFAULT 'AWAITING_REMOVAL',
    CONSTRAINT pk_rental_request PRIMARY KEY (id),
    CONSTRAINT fk_rental_request_rider_account FOREIGN KEY (rider_account_id) REFERENCES rider_account(id) ON DELETE RESTRICT,
    CONSTRAINT fk_rental_request_dock FOREIGN KEY (dock_id) REFERENCES dock(id) ON DELETE RESTRICT,
    CONSTRAINT fk_rental_request_bike FOREIGN KEY (bike_id) REFERENCES bike(id) ON DELETE RESTRICT,
    CONSTRAINT uq_rental_request_payment_hold_id UNIQUE (payment_hold_id),
    CONSTRAINT fk_rental_request_payment_hold FOREIGN KEY (payment_hold_id) REFERENCES payment_hold(id) ON DELETE RESTRICT,
    CONSTRAINT ck_rental_request_status CHECK (status IN ('AWAITING_REMOVAL','STARTED','EXPIRED'))
);

CREATE TABLE transfer_order (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    from_station_id UUID NOT NULL,
    to_station_id UUID NOT NULL,
    status VARCHAR(10) NOT NULL DEFAULT 'PENDING',
    CONSTRAINT pk_transfer_order PRIMARY KEY (id),
    CONSTRAINT fk_transfer_order_from_station FOREIGN KEY (from_station_id) REFERENCES station(id) ON DELETE RESTRICT,
    CONSTRAINT fk_transfer_order_to_station FOREIGN KEY (to_station_id) REFERENCES station(id) ON DELETE RESTRICT,
    CONSTRAINT ck_transfer_order_status CHECK (status IN ('PENDING','COMPLETED'))
);
    -- requested_bikes: kiểu chờ Q-25, chưa tạo cột

CREATE UNIQUE INDEX ux_trip_rider_in_progress ON trip (rider_account_id) WHERE status = 'IN_PROGRESS';
CREATE UNIQUE INDEX ux_trip_bike_in_progress ON trip (bike_id) WHERE status = 'IN_PROGRESS';
CREATE UNIQUE INDEX ux_rental_request_dock_awaiting ON rental_request (dock_id) WHERE status = 'AWAITING_REMOVAL';
CREATE UNIQUE INDEX ux_rental_request_rider_awaiting ON rental_request (rider_account_id) WHERE status = 'AWAITING_REMOVAL';
CREATE INDEX ix_dock_station ON dock (station_id);
```

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-48 | Dữ liệu chuyến đi, khoản tạm giữ, lượt thuê được lưu bao lâu, có cần xoá hoặc ẩn danh theo thời gian không? | TBL-05, TBL-06, TBL-07; ON DELETE | Nguồn không nêu |

Liên quan: Q-25 (kiểu requested_bikes), Q-27, Q-30, Q-40, Q-42, Q-47.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P12 | DC-RentalRequest, R-50 | Multiplicity "RentalRequest 0..1 - Dock 1" chỉ đúng cho lượt đang chờ; theo thời gian một ụ có nhiều lượt | Đổi thành "0..* - 1" và ghi ràng buộc {tối đa một lượt AWAITING_REMOVAL mỗi ụ} |

## Vấn đề còn mở

- Target 2: DC-TransferOrder.requestedBikes chưa có kiểu (Q-25); DDL không tạo cột này nên TBL-08 chưa dùng được.
- Target 9: VARCHAR(254), VARCHAR(100) không có căn cứ trong nguồn (Q-40, Q-42, Q-47); ở NGHIEM_NGAT vẫn phải chọn một độ dài để sinh DDL.
- Index ux_rental_request_rider_awaiting mở rộng BR-02 sang khoảng chờ rút xe; cần xác nhận khi trả lời Q-45.
- Bảng lưu mốc thời gian của SS-04 (P09 F3) chưa có vì PKG-21 chưa thiết kế lớp.
- ER khái niệm (P13-erd-conceptual) không vẽ trong lần chạy này để giới hạn phạm vi kiểm chứng; MUC_CHI_TIET = DAY_DU yêu cầu có.
