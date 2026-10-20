# P13 - Mô hình dữ liệu - PKG-15 GroupClassService, PKG-29 GroupClass - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P13 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CHE_DO_GIA_DINH NGHIEM_NGAT, NGON_NGU_TEN_PHAN_TU snake_case cho bảng và cột, CONG_NGHE hệ quản trị PostgreSQL, MUC_CHI_TIET GON); P12-class-design/PKG-15-PKG-29-group-class.md (1.0; F1, F1b, F3, F5, F6, F7, Câu hỏi mở, Giả định, Vấn đề còn mở); P06-supplementary-spec.md (1.0; NFR-01, NFR-10, BR-06 đến BR-14, BR-36, BR-37); P04-uc-specs/UC-010-book-class-spot.md và UC-015-cancel-under-booked-class.md (1.0; mục 2, 3, 5, 6, 8) cùng _BR-register.md (BR-01 đến BR-40); P09-architecture.md (1.0; F2.2, F7 bảng cơ chế lưu trữ, F11); P05-glossary.md (1.0; GL-05, GL-08, GL-13, GL-27, GL-28, GL-29, GL-35, GL-38). LOAI_CSDL: Không có (dùng CONG_NGHE). QUY_UOC_CSDL: Không có. KHOI_LUONG_DU_LIEU: 4 chi nhánh, khoảng 6.000 hội viên, khoảng 25 lớp nhóm mỗi ngày mỗi chi nhánh (khoảng 36.500 lớp mỗi năm), giờ cao điểm 17:00 đến 20:00 truy vấn lịch lớp và đặt chỗ nhiều nhất. SINH_DDL: Có (PostgreSQL). YEU_CAU_BO_SUNG: chỉ mô hình dữ liệu cho lớp persistent có trong file P12 của PKG-15, PKG-29; lớp persistent của package khác chỉ ghi là bảng ngoài phạm vi, không thiết kế cột. Mã Q lớn nhất do người dùng cung cấp: Q-107, quét lại ở thư mục đầu ra cho cùng kết quả; chưa có ASM; chưa có P13 nào khác |
| Phạm vi | 3 lớp persistent của PKG-29 (DC-GroupClass, DC-ClassBooking, DC-Waitlist) cùng bảng lưu mục chờ của DC-WaitlistEntry; UC-010 Đặt chỗ lớp nhóm, UC-015 Huỷ lớp nhóm ít người đặt. 4 bảng (TBL-01 đến TBL-04) |
| Mã Q, ASM cuối đã cấp | Q-107 (lần chạy này không cấp Q mới); ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Mã khác cuối đã cấp | TBL-04; ER-04; E-GroupClass, E-ClassBooking, E-Waitlist, E-Member (E-Member chỉ tham chiếu) |

## F1. Quyết định loại CSDL

| Hạng mục | Quyết định | Căn cứ (NFR / P09 / CONG_NGHE) |
|---|---|---|
| Loại CSDL | Quan hệ | CONG_NGHE; P09 F7 "Loại cơ chế lưu trữ": quan hệ, vì ghi chỗ đã đặt là một giao dịch khoá dòng lớp (BR-11, NFR-01) |
| Hệ quản trị | PostgreSQL. Phiên bản chưa chốt; Thiết kế: dùng từ 13 trở lên để gen_random_uuid() có sẵn, không cần extension | CONG_NGHE; P09 F11 |
| Chiến lược khoá chính | Bảng thực thể độc lập (group_class, class_booking, waitlist) dùng khoá thay thế id kiểu UUID; bảng trung gian waitlist_entry dùng khoá ghép (waitlist_id, member_id) | P12 F2 (định danh --> string, Thiết kế: chuỗi UUID), F7 (id của DC-GroupClass, DC-ClassBooking, DC-Waitlist); Conventions P13 F1 mặc định |
| Quy ước tên | Bảng số ít, snake_case, tiếng Anh. Ràng buộc: pk_<bang>, fk_<bang_con>_<bang_cha>, uq_<bang>_<cot>, ck_<bang>_<cot>; index ix_<bang>_<cot> | NGON_NGU_TEN_PHAN_TU; QUY_UOC_CSDL Không có |
| Kiểu thời điểm | TIMESTAMPTZ | Thiết kế: giờ học và thời điểm vào danh sách chờ là thời điểm tuyệt đối; ngày của lớp tính theo một múi giờ cấu hình cho cả chuỗi (P12 F3 DC-MemberBookingQuota) ở tầng ứng dụng |
| Giao dịch | Mức cô lập mặc định READ COMMITTED; BR-11 giữ bằng khoá dòng group_class (SELECT ... FOR UPDATE) trong giao dịch của bookClass | P09 F7 chiến lược giao dịch; P12 F3 bookClass bước 4 |
| Khối lượng | group_class: khoảng 36.500 dòng mỗi năm (4 chi nhánh x 25 lớp x 365 ngày). class_booking: chặn trên 6.000 x 2 x 365 = 4.380.000 dòng mỗi năm theo BR-08 (tối đa 2 chỗ mỗi hội viên mỗi ngày), thực tế nhỏ hơn và còn bị chặn bởi tổng sức chứa (chưa biết, Q-03). waitlist: tối đa một dòng mỗi lớp, tối đa 36.500 mỗi năm. waitlist_entry: nguồn không nêu cận trên (Q-62, Q-84). Thời gian lưu: chờ Q-89 | KHOI_LUONG_DU_LIEU; NFR-01; BR-08 |
| Tải | Giờ cao điểm 17:00 đến 20:00: đọc lịch lớp theo khoảng giờ học và đặt chỗ. Mốc mở đặt chỗ tuần mới 6 giờ sáng thứ Hai: tới 1.500 phiên đặt chỗ đồng thời (NFR-01, mức đạt chưa đo được, Q-42, Q-76), tranh chấp khoá chủ yếu trên dòng group_class của từng lớp | KHOI_LUONG_DU_LIEU; NFR-01 |
| Phạm vi dữ liệu | 4 bảng của PKG-29. Bảng member (PKG-26) là bảng ngoài phạm vi: chỉ tham chiếu khoá chính id, không thiết kế cột. Kho mốc hẹn của PKG-22 (UC-015 bước 4) là bảng ngoài phạm vi | YEU_CAU_BO_SUNG; P09 F7 |

## F2. Bảng lớp persistent và chiến lược ánh xạ

| DC | Persistent (Có / Không) | Thực thể (E-) | TBL | Chiến lược | Lý do |
|---|---|---|---|---|---|
| DC-BookClassSpotHandler | Không | - | - | - | Lớp control, điều phối UC-010, không có đối tượng tồn tại sau khi chương trình kết thúc |
| DC-CancelUnderBookedClassHandler | Không | - | - | - | Lớp control, điều phối UC-015 |
| DC-GroupClass | Có | E-GroupClass | TBL-01 | Một lớp - một bảng | Gốc tập hợp của chỗ đã đặt và danh sách chờ (R-17, R-18); có định danh riêng và state machine ST-01 |
| DC-ClassBooking | Có | E-ClassBooking | TBL-02 | Một lớp - một bảng | Có định danh riêng (DC-ClassBooking.id); R-17 là association, không phải composition, nên không là bộ phận nhúng: chỗ đã đặt không bị xoá cùng lớp huỷ (Q-63) |
| DC-Waitlist | Có | E-Waitlist | TBL-03 | Một lớp - một bảng | Có định danh riêng (DC-Waitlist.id); mỗi lớp tối đa một danh sách (R-18). Giữ bảng riêng để ghép được với cả hai câu trả lời của Q-84 (đối tượng riêng hay chỉ là tập mục chờ) |
| DC-MemberBookingQuota | Không | - | - | - | Dịch vụ miền, đếm class_booking qua IF-14; MAX_BOOKINGS_PER_DAY là hằng số lớp (BR-08), không lưu |
| DC-Member (PKG-26) | Có (theo P12 của PKG-26, chưa có) | E-Member | Ngoài phạm vi | - | Ngoài phạm vi lần chạy này: chỉ tham chiếu, không thiết kế cột. Tên bảng dự kiến member, khoá id UUID (Thiết kế: cùng kiểu định danh string UUID của P12 F2); chờ lần chạy P13 cho PKG-26 xác nhận |
| IF-14 IGroupClassRepository, IF-16 IClock | Không | - | - | - | Interface, không có đối tượng lưu |
| DC-ClassInfo | Không | - | - | - | Value object chiếu từ TBL-01 (mã lớp, loại lớp, phòng, huấn luyện viên, giờ học), không lưu riêng |
| DC-WaitlistEntry | Không | ER-04 (thuộc tính joinedAt của mối quan hệ) | TBL-04 | Bảng thuộc tính đa trị TBL-04 | Value object nằm trong thuộc tính đa trị DC-Waitlist.entries; đồng thời là association class của R-20 nên cũng là bảng trung gian của quan hệ nhiều - nhiều (F4.2). Hai cách đọc cho cùng một bảng |
| DC-WaitlistPlacement, DC-BookClassResult | Không | - | - | - | Value object kết quả trả về của handler, không lưu |
| DC-GroupClassStatus | Không | - | TBL-01 | Miền giá trị (CHECK) | Enumeration hai giá trị cố định SCHEDULED, CANCELLED thành CHECK trên group_class.status; không có nhu cầu người dùng thêm giá trị nên không lập bảng danh mục |
| DC-Bookability, DC-CancellationCheck, DC-BookingOutcome | Không | - | - | - | Enumeration kết quả đánh giá hoặc kết cục xử lý, không là thuộc tính của lớp persistent |
| DC-GroupClassNotFoundException, DC-SpotUnavailableException, DC-InvalidClassStateException, DC-WaitlistNotAllowedException | Không | - | - | - | Exception, không lưu |

## F3. Mô hình khái niệm (ER)

F3.1. Thực thể

| E | Tên thực thể | Mô tả | Định danh | Thuộc tính (đánh dấu: định danh, phức hợp, đa trị, dẫn xuất) | Thực thể yếu (Có / Không) | Nguồn DC |
|---|---|---|---|---|---|---|
| E-GroupClass | Lớp nhóm | Lần tập chung do một huấn luyện viên phụ trách, thuộc một loại lớp, diễn ra tại một phòng vào một giờ học xác định (GL-29) | id (định danh thay thế) | id (định danh); classType; room; trainer; startTime; capacity; status; /bookedCount (dẫn xuất, không lưu) | Không | DC-GroupClass |
| E-ClassBooking | Chỗ đã đặt | Phần sức chứa của một lớp mà một hội viên đã đặt cho mình (GL-05) | id (định danh thay thế) | id (định danh) | Không | DC-ClassBooking |
| E-Waitlist | Danh sách chờ | Danh sách có thứ tự các hội viên chờ nhận chỗ của một lớp đã đủ chỗ (GL-08) | id (định danh thay thế) | id (định danh); entries (đa trị, hiện thực qua mối quan hệ ER-04 vì mỗi mục chờ trỏ tới một hội viên) | Không | DC-Waitlist |
| E-Member | Hội viên | Ngoài phạm vi (PKG-26), chỉ tham chiếu | Ngoài phạm vi | Ngoài phạm vi | Không | DC-Member |

F3.2. Mối quan hệ

| ER | Tên mối quan hệ (động từ) | Thực thể A | Thực thể B | Bản số | Tham gia A, B | Thuộc tính của mối quan hệ | Nguồn R (P12) |
|---|---|---|---|---|---|---|---|
| ER-01 | nhận | E-GroupClass | E-ClassBooking | 1:N | A tuỳ chọn (lớp có thể chưa có chỗ nào), B bắt buộc | - | R-17 |
| ER-02 | có | E-GroupClass | E-Waitlist | 1:1 | A tuỳ chọn (danh sách chờ tạo muộn, Q-84), B bắt buộc | - | R-18 |
| ER-03 | được đặt bởi | E-ClassBooking | E-Member | N:1 | A bắt buộc, B tuỳ chọn | - | R-19 |
| ER-04 | chờ | E-Waitlist | E-Member | M:N | A tuỳ chọn, B tuỳ chọn | joinedAt | R-20 |

Mức khái niệm không vẽ ER (chỉ khi MUC_CHI_TIET là DAY_DU).

## F4. Mô hình logic (CSDL quan hệ)

F4.1. Lược đồ quan hệ

| TBL | Tên bảng | Lược đồ (PK ghi trước, đánh dấu PK:, FK:) | Khoá ứng viên khác | Nguồn (E / DC) |
|---|---|---|---|---|
| TBL-01 | group_class | group_class(PK: id, class_type, room, trainer, start_time, capacity, status) | Không có. (room, start_time) và (trainer, start_time) không khai báo UNIQUE vì BR-36, BR-37 xét trùng giờ theo khoảng, thời lượng chờ Q-32 | E-GroupClass / DC-GroupClass |
| TBL-02 | class_booking | class_booking(PK: id, FK: group_class_id, FK: member_id) | Không có. Cặp (group_class_id, member_id) không khai báo UNIQUE vì đặt trùng cùng một lớp chờ Q-59 | E-ClassBooking / DC-ClassBooking |
| TBL-03 | waitlist | waitlist(PK: id, FK: group_class_id) | group_class_id (UNIQUE, mỗi lớp tối đa một danh sách, R-18) | E-Waitlist / DC-Waitlist |
| TBL-04 | waitlist_entry | waitlist_entry(PK: waitlist_id FK, PK: member_id FK, joined_at) | Không có | ER-04 / DC-WaitlistEntry |

F4.2. Ánh xạ quan hệ giữa lớp

| R (P12) | Loại | Multiplicity | Cách ánh xạ | FK hoặc bảng trung gian | Kiểu quan hệ dữ liệu (phụ thuộc / độc lập) | ON DELETE |
|---|---|---|---|---|---|---|
| R-17 | Association | DC-GroupClass 1 - DC-ClassBooking 0..* | FK ở bảng phía N | class_booking.group_class_id NOT NULL --> group_class.id (fk_class_booking_group_class) | độc lập | RESTRICT |
| R-18 | Association | DC-GroupClass 1 - DC-Waitlist 0..1 | 1 - 1: FK ở bảng phía tuỳ chọn, kèm UNIQUE | waitlist.group_class_id NOT NULL UNIQUE --> group_class.id (fk_waitlist_group_class) | độc lập | RESTRICT |
| R-19 | Association | DC-ClassBooking 0..* - DC-Member 1 | FK ở bảng phía N | class_booking.member_id NOT NULL --> member.id, bảng ngoài phạm vi (fk_class_booking_member) | độc lập | RESTRICT |
| R-20 | Association, association class DC-WaitlistEntry | DC-Waitlist 0..* - DC-Member 0..* | Bảng trung gian TBL-04; khoá chính là cặp hai khoá ngoại vì định danh mục chờ là Waitlist + Member | waitlist_entry(PK: waitlist_id FK, PK: member_id FK, joined_at); fk_waitlist_entry_waitlist, fk_waitlist_entry_member | phụ thuộc với cả hai bảng cha | CASCADE với waitlist (mục chờ là bộ phận của danh sách); RESTRICT với member |
| R-15, R-16, R-21, R-22, R-40, R-41, R-42 | Dependency | - | Dependency không ánh xạ thành khoá ngoại | Không áp dụng | Không áp dụng | Không áp dụng |
| R-29 đến R-37, R-39 | Association giữa lớp control hoặc service và interface (tiêm phụ thuộc) | - | Một đầu không persistent | Không áp dụng | Không áp dụng | Không áp dụng |
| R-38 | Realization | - | Không ánh xạ | Không áp dụng | Không áp dụng | Không áp dụng |

F4.3. Ánh xạ generalization

| Cây kế thừa (lớp cha - các lớp con) | Chiến lược | Bảng | Cột phân biệt loại | Lý do chọn |
|---|---|---|---|---|
| Không có cây kế thừa persistent trong phạm vi | - | - | - | P12 của PKG-15, PKG-29 không có generalization |

F4.4. Ràng buộc liên bảng

| Mã | Ràng buộc | Bảng | Nguồn (BR / ST / R-nn / ASM) | Cách giữ (trigger / ứng dụng trong giao dịch) |
|---|---|---|---|---|
| C-01 | Số dòng class_booking của một lớp không vượt group_class.capacity | TBL-01, TBL-02 | BR-11, R-17 | Ứng dụng trong giao dịch: IF-14.runInTransaction, nạp lớp bằng findByIdForUpdate (khoá dòng group_class), reserveSpot kiểm getBookedCount() < capacity, rồi save. Khớp P12 F3 bookClass bước 4 đến 9 và DC-GroupClass.reserveSpot. Không dùng trigger vì cùng một khoá dòng đã tuần tự hoá mọi yêu cầu cùng lớp |
| C-02 | class_booking và waitlist_entry chỉ được thêm khi group_class.status là SCHEDULED | TBL-01, TBL-02, TBL-04 | ST-01 (T2, T3, sự kiện bị từ chối ở trạng thái Cancelled) | Ứng dụng: DC-GroupClass.reserveSpot, addToWaitlist kiểm status trước khi thêm (P12 F3), cùng giao dịch khoá dòng lớp |
| C-03 | Mục chờ chỉ được thêm khi lớp đã đủ chỗ (số chỗ đã đặt bằng sức chứa) | TBL-01, TBL-02, TBL-04 | BR-12, ST-01 (T3) | Ứng dụng: DC-GroupClass.addToWaitlist kiểm getBookedCount() >= capacity lúc thêm. Không là bất biến lâu dài vì chỗ có thể trống sau đó (UC-011, UC-012 chưa có P07) nên không khai báo ở CSDL |
| C-04 | Mỗi hội viên có tối đa 2 chỗ đã đặt trong cùng một ngày diễn ra lớp | TBL-01, TBL-02 | BR-08, R-19 | Ứng dụng: DC-MemberBookingQuota.hasReachedDailyLimit đếm qua IF-14.countMemberBookingsBetween (P12 F3 bookClass bước 6). Khoá dòng group_class không bảo vệ ràng buộc này khi một hội viên đặt hai lớp khác nhau đồng thời (rủi ro đã ghi ở P12 Vấn đề còn mở). Cách tính ngày và việc tính lớp trong danh sách chờ chờ Q-60 |
| C-05 | Hội viên bị khoá quyền đặt lớp không được thêm class_booking | TBL-02 và bảng member (ngoài phạm vi) | BR-09 | Ứng dụng: P12 F3 bookClass bước 3 kiểm hội viên đang bị khoá; trạng thái khoá nằm ở dữ liệu của PKG-26 |
| C-06 | group_class.capacity xác định theo phòng, không vượt sức chứa phòng | TBL-01 | BR-10 | Chưa giữ được: phòng là chuỗi tạm, chưa có bảng phòng và sức chứa phòng (Q-03) |
| C-07 | Một phòng và một huấn luyện viên không được xếp hai lớp trùng giờ | TBL-01 | BR-36, BR-37 | Chưa giữ được: P12 không có thời lượng hay giờ kết thúc của lớp (Q-32), room và trainer là chuỗi tạm (Q-03, Q-05). Khi có thời lượng, giữ bằng EXCLUDE constraint (khoảng thời gian) hoặc kiểm tra trong giao dịch tạo lớp của UC-009 |

## F5. Chuẩn hoá (CSDL quan hệ)

F5.1. Bảng kiểm tra

| TBL | Khoá (chính và ứng viên) | Phụ thuộc hàm (FD) | 1NF | 2NF | 3NF | BCNF | Kết luận |
|---|---|---|---|---|---|---|---|
| TBL-01 group_class | PK: id. Không có khoá ứng viên khác | id --> class_type, room, trainer, start_time, capacity, status. Không khẳng định room --> capacity vì sức chứa lớp so với sức chứa phòng chờ Q-03 (BR-10) | Đạt | Đạt (khoá một cột) | Đạt | Đạt | Đạt, xem F5.2 về khả năng tách phòng |
| TBL-02 class_booking | PK: id | id --> group_class_id, member_id. Cặp (group_class_id, member_id) không xác định id vì đặt trùng chờ Q-59 | Đạt | Đạt | Đạt | Đạt | Đạt |
| TBL-03 waitlist | PK: id; khoá ứng viên: group_class_id | id --> group_class_id; group_class_id --> id (mỗi lớp tối đa một danh sách, R-18) | Đạt | Đạt | Đạt | Đạt: hai khoá ứng viên một cột, mọi định thức là siêu khoá | Đạt |
| TBL-04 waitlist_entry | PK: (waitlist_id, member_id) | (waitlist_id, member_id) --> joined_at | Đạt | Đạt: joined_at phụ thuộc cả khoá, không phụ thuộc riêng waitlist_id hay member_id | Đạt | Đạt | Đạt |

F5.2. Quá trình tách

Không có bảng không đạt. Dự kiến, chưa áp dụng: nếu Q-03 trả lời sức chứa lớp được xác định đúng bằng sức chứa phòng, group_class có phụ thuộc bắc cầu id --> room --> capacity và phải tách thành room(id, branch_id, capacity) cùng group_class.room_id. Tương tự nếu Q-05 chốt huấn luyện viên là đối tượng có hồ sơ riêng thì trainer thành khoá ngoại.

F5.3. Phi chuẩn hoá có chủ đích

| TBL.cột | Dạng phi chuẩn hoá | Lý do (NFR / BR, số liệu) | Cơ chế giữ nhất quán |
|---|---|---|---|
| Không có | - | Đã xét lưu sẵn số chỗ đã đặt trong group_class (dẫn xuất từ class_booking, DC-GroupClass./bookedCount) và không chọn: mức đạt của NFR-01 chưa đo được (Q-42, Q-76), đếm theo index ix_class_booking_group_class trên khoảng 100 lớp mỗi ngày chưa có bằng chứng không đạt, và cột lưu sẵn thêm một nguồn lệch với BR-11 | Không áp dụng |

## F6. Mô hình vật lý

F6.1. Bảng cột

| TBL | Tên bảng | Cột | Kiểu | PK/FK/UNIQUE | NULL | Mặc định | Nguồn DC | Tham chiếu FK (TBL.cột, ON DELETE, ON UPDATE) | CHECK / mô tả |
|---|---|---|---|---|---|---|---|---|---|
| TBL-01 | group_class | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-GroupClass.id | | Tên ràng buộc pk_group_class. Mã lớp do UC-009 cấp khi tạo (P12 F7); mặc định của CSDL chỉ dùng khi ứng dụng không truyền |
| TBL-01 | group_class | class_type | VARCHAR(100) | | NOT NULL | | DC-GroupClass.classType | | Thiết kế: độ dài dự phòng cho tên loại lớp (nguồn nêu yoga, aerobic, đạp xe trong nhà). Không CHECK tập giá trị vì danh mục đóng hay mở chờ Q-04. Thuộc tính tạm của P12 |
| TBL-01 | group_class | room | VARCHAR(100) | | NOT NULL | | DC-GroupClass.room | | Thiết kế: độ dài dự phòng cho tên phòng. Chuỗi tạm, chưa là khoá ngoại vì chưa có bảng phòng (Q-03) |
| TBL-01 | group_class | trainer | VARCHAR(100) | | NOT NULL | | DC-GroupClass.trainer | | Thiết kế: độ dài dự phòng cho họ tên người. Chuỗi tạm, chưa là khoá ngoại vì hồ sơ huấn luyện viên chờ Q-05 |
| TBL-01 | group_class | start_time | TIMESTAMPTZ | | NOT NULL | | DC-GroupClass.startTime | | Giờ học: ngày và giờ bắt đầu (GL-13); chờ Q-73 về cách gọi |
| TBL-01 | group_class | capacity | INTEGER | | NOT NULL | | DC-GroupClass.capacity | | CHECK (capacity >= 0), tên ck_group_class_capacity (P12 F7 {số nguyên, >= 0}; BR-10) |
| TBL-01 | group_class | status | VARCHAR(20) | | NOT NULL | 'SCHEDULED' | DC-GroupClass.status | | CHECK (status IN ('SCHEDULED', 'CANCELLED')), tên ck_group_class_status (DC-GroupClassStatus, ST-01). Thiết kế: 20 ký tự đủ cho giá trị dài nhất với dư. Lớp lưu từ trạng thái khởi tạo SCHEDULED nên mặc định khớp P12 F7 |
| TBL-02 | class_booking | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-ClassBooking.id | | Tên pk_class_booking. P12 F7 ghi multiplicity 0..1 vì đối tượng chưa lưu chưa có id; cột trong CSDL luôn có giá trị nên NOT NULL |
| TBL-02 | class_booking | group_class_id | UUID | FK | NOT NULL | | R-17 | TBL-01.id, RESTRICT, RESTRICT | Tên fk_class_booking_group_class. Mỗi chỗ đã đặt thuộc đúng một lớp (P12 R-17, phía 1 bắt buộc) |
| TBL-02 | class_booking | member_id | UUID | FK | NOT NULL | | R-19 | member.id (bảng ngoài phạm vi, PKG-26), RESTRICT, RESTRICT | Tên fk_class_booking_member. Mỗi chỗ đã đặt do đúng một hội viên đặt (P12 R-19). Kiểu UUID theo kiểu định danh string UUID của P12; chờ P13 của PKG-26 xác nhận |
| TBL-03 | waitlist | id | UUID | PK | NOT NULL | gen_random_uuid() | DC-Waitlist.id | | Tên pk_waitlist. Như class_booking.id về multiplicity 0..1 |
| TBL-03 | waitlist | group_class_id | UUID | FK, UQ | NOT NULL | | R-18 | TBL-01.id, RESTRICT, RESTRICT | Tên fk_waitlist_group_class, uq_waitlist_group_class. Mỗi danh sách thuộc đúng một lớp, mỗi lớp tối đa một danh sách |
| TBL-04 | waitlist_entry | waitlist_id | UUID | PK, FK | NOT NULL | | R-20 | TBL-03.id, CASCADE, RESTRICT | Tên pk_waitlist_entry (waitlist_id, member_id), fk_waitlist_entry_waitlist. Mục chờ là bộ phận của danh sách, xoá danh sách kéo theo mục chờ |
| TBL-04 | waitlist_entry | member_id | UUID | PK, FK | NOT NULL | | R-20 | member.id (bảng ngoài phạm vi, PKG-26), RESTRICT, RESTRICT | Tên fk_waitlist_entry_member. Khoá chính ghép làm một hội viên có tối đa một mục chờ trong một danh sách (định danh Waitlist + Member theo P12 F5 R-20); hội viên vào chờ lại sau khi rời cần dòng cũ đã bị xoá, chờ UC-011, UC-012 |
| TBL-04 | waitlist_entry | joined_at | TIMESTAMPTZ | | NOT NULL | | DC-WaitlistEntry.joinedAt | | Thời điểm hội viên vào danh sách, do ứng dụng truyền từ IF-16.now(). Cơ sở thứ tự xếp chờ nhưng quy tắc thứ tự chờ Q-61 (compareWaitOrder); hai mục cùng thời điểm chưa phân định thứ tự |

Không có cột cho DC-GroupClass./bookedCount (dẫn xuất, P12 F7), DC-GroupClass.UNDER_BOOKED_THRESHOLD và DC-MemberBookingQuota.MAX_BOOKINGS_PER_DAY (hằng số lớp). DC-Waitlist.entries lưu qua TBL-04.

F6.2. Ánh xạ kiểu dữ liệu đã dùng (PostgreSQL)

| Kiểu thiết kế | Kiểu vật lý đã dùng |
|---|---|
| String có độ dài tối đa | VARCHAR(n), n là quyết định thiết kế (Thiết kế: dự phòng), không có độ dài mang nghĩa nghiệp vụ trong P04, BR |
| Integer / number nguyên | INTEGER |
| Date (thời điểm) | TIMESTAMPTZ (có múi giờ) |
| Enumeration | VARCHAR(20) kèm CHECK tập giá trị |
| Định danh thay thế | UUID, theo kiểu định danh string UUID của P12; sinh bằng gen_random_uuid() khi ứng dụng không truyền |

F6.3. Index

| TBL | Tên index | Cột (theo thứ tự) | Loại (UNIQUE / thường / khác) | Phục vụ truy vấn (UC bước / NFR) |
|---|---|---|---|---|
| TBL-01 | ix_group_class_start_time | start_time | thường | UC-010 bước 2: IF-14.findSchedule lọc lớp theo khoảng giờ học, tải cao nhất 17:00 đến 20:00 (KHOI_LUONG_DU_LIEU); IF-14.countMemberBookingsBetween lọc lớp theo khoảng giờ học trong ngày (BR-08, UC-010 bước 6); phạm vi lịch chờ Q-83 |
| TBL-02 | ix_class_booking_group_class | group_class_id | thường | Nạp và đếm chỗ đã đặt của một lớp: UC-010 bước 7, 8 (BR-11, findByIdForUpdate); UC-015 bước 2 (BR-13) và bước 5 (collectBookedMembers); index cho khoá ngoại fk_class_booking_group_class |
| TBL-02 | ix_class_booking_member | member_id, group_class_id | thường | UC-010 bước 6: IF-14.countMemberBookingsBetween đếm chỗ đã đặt của một hội viên rồi nối group_class để lọc ngày (BR-08); NFR-01 |
| TBL-03 | uq_waitlist_group_class | group_class_id | UNIQUE | Nạp danh sách chờ theo lớp: UC-010 bước 7a3 (findByIdForUpdate); đồng thời thực thi R-18 |
| TBL-04 | ix_waitlist_entry_waitlist_joined | waitlist_id, joined_at | thường | Đọc các mục chờ của một danh sách theo thứ tự thời điểm vào để tính vị trí: UC-010 bước 7a3, 7a4 (DC-Waitlist.addMember, Dữ liệu ra 3); thứ tự cuối cùng chờ Q-61 |

Khoá chính và UNIQUE đã có index. waitlist_entry.member_id không có index riêng: không có truy vấn nào trong UC-010, UC-015 đi từ hội viên tới mục chờ (Q-60 chưa chốt có tính lớp trong danh sách chờ).

## F7. Mô hình tài liệu

Không áp dụng (CSDL quan hệ).

## F8. ERD

F8.1. ERD logic/vật lý: diagrams/P13-erd-logical.drawio (một trang). Không có ERD khái niệm vì MUC_CHI_TIET là GON.

Node

| ID (TBL) | Loại (Table / Collection / Note) | Nhãn (tên bảng) | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| TBL-01 | Table | group_class | - | PKG-29 | Cột theo F6.1 | 440 | 40 | 300 | 208 |
| TBL-02 | Table | class_booking | - | PKG-29 | Cột theo F6.1 | 40 | 40 | 300 | 104 |
| TBL-03 | Table | waitlist | - | PKG-29 | Cột theo F6.1 | 840 | 40 | 300 | 78 |
| TBL-04 | Table | waitlist_entry | - | PKG-29 | Cột theo F6.1 | 840 | 320 | 300 | 104 |
| EXT-member | Table | member (ngoài phạm vi, PKG-26) | - | PKG-26 | Chỉ vẽ khoá id làm đích khoá ngoại; cột khác không thiết kế | 440 | 330 | 300 | 80 |

Edge

| ID (tên ràng buộc fk_...) | Nguồn (bảng cha) | Đích (bảng con chứa FK) | Loại quan hệ (Phụ thuộc / Độc lập) | Nhãn / multiplicity (ký pháp chân chim hai đầu) | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| fk_class_booking_group_class | TBL-01 | TBL-02 | Độc lập | cha một bắt buộc; con 0..* | R-17 | - |
| fk_waitlist_group_class | TBL-01 | TBL-03 | Độc lập | cha một bắt buộc; con 0..1 | R-18, FK kèm UNIQUE | - |
| fk_class_booking_member | EXT-member | TBL-02 | Độc lập | cha một bắt buộc; con 0..* | R-19 | (190,370) |
| fk_waitlist_entry_waitlist | TBL-03 | TBL-04 | Phụ thuộc | cha một bắt buộc; con 0..* | R-20, FK nằm trong PK | - |
| fk_waitlist_entry_member | EXT-member | TBL-04 | Phụ thuộc | cha một bắt buộc; con 0..* | R-20, FK nằm trong PK | - |

## F9. Script DDL

```sql
CREATE TABLE group_class (
    id          UUID         NOT NULL DEFAULT gen_random_uuid(),
    class_type  VARCHAR(100) NOT NULL,
    room        VARCHAR(100) NOT NULL,
    trainer     VARCHAR(100) NOT NULL,
    start_time  TIMESTAMPTZ  NOT NULL,
    capacity    INTEGER      NOT NULL,
    status      VARCHAR(20)  NOT NULL DEFAULT 'SCHEDULED',
    CONSTRAINT pk_group_class PRIMARY KEY (id),
    CONSTRAINT ck_group_class_capacity CHECK (capacity >= 0),
    CONSTRAINT ck_group_class_status CHECK (status IN ('SCHEDULED', 'CANCELLED'))
);

CREATE TABLE class_booking (
    id              UUID NOT NULL DEFAULT gen_random_uuid(),
    group_class_id  UUID NOT NULL,
    member_id       UUID NOT NULL,
    CONSTRAINT pk_class_booking PRIMARY KEY (id),
    CONSTRAINT fk_class_booking_group_class FOREIGN KEY (group_class_id)
        REFERENCES group_class (id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

CREATE TABLE waitlist (
    id              UUID NOT NULL DEFAULT gen_random_uuid(),
    group_class_id  UUID NOT NULL,
    CONSTRAINT pk_waitlist PRIMARY KEY (id),
    CONSTRAINT uq_waitlist_group_class UNIQUE (group_class_id),
    CONSTRAINT fk_waitlist_group_class FOREIGN KEY (group_class_id)
        REFERENCES group_class (id) ON DELETE RESTRICT ON UPDATE RESTRICT
);

CREATE TABLE waitlist_entry (
    waitlist_id  UUID        NOT NULL,
    member_id    UUID        NOT NULL,
    joined_at    TIMESTAMPTZ NOT NULL,
    CONSTRAINT pk_waitlist_entry PRIMARY KEY (waitlist_id, member_id),
    CONSTRAINT fk_waitlist_entry_waitlist FOREIGN KEY (waitlist_id)
        REFERENCES waitlist (id) ON DELETE CASCADE ON UPDATE RESTRICT
);

CREATE INDEX ix_group_class_start_time ON group_class (start_time);
CREATE INDEX ix_class_booking_group_class ON class_booking (group_class_id);
CREATE INDEX ix_class_booking_member ON class_booking (member_id, group_class_id);
CREATE INDEX ix_waitlist_entry_waitlist_joined ON waitlist_entry (waitlist_id, joined_at);

-- Bảng member thuộc PKG-26, phải tồn tại trước khi chạy hai lệnh dưới đây.
ALTER TABLE class_booking
    ADD CONSTRAINT fk_class_booking_member FOREIGN KEY (member_id)
        REFERENCES member (id) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE waitlist_entry
    ADD CONSTRAINT fk_waitlist_entry_member FOREIGN KEY (member_id)
        REFERENCES member (id) ON DELETE RESTRICT ON UPDATE RESTRICT;
```

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | Lần chạy này không cấp Q mới. Các điểm chưa chốt đều đã có Q: Q-03, Q-04, Q-05 (phòng, loại lớp, huấn luyện viên), Q-32 (thời lượng lớp), Q-59 (đặt trùng), Q-60 (cách tính ngày), Q-61, Q-62 (thứ tự và cách vào danh sách chờ), Q-63 (chỗ đã đặt và danh sách chờ khi lớp huỷ), Q-83 (phạm vi lịch), Q-84 (danh sách chờ là đối tượng riêng), Q-89 (thời gian lưu dữ liệu) | - | - |

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P12 | F1b (cột Persistent) | Bảng kiểu phụ trợ không có cột Persistent nên P13 phải tự suy value object nào lưu. DC-WaitlistEntry chỉ lộ ra là đối tượng được lưu qua R-20 và thuộc tính DC-Waitlist.entries | Thêm cột Persistent vào F1b, ghi DC-WaitlistEntry là value object lưu qua bảng trung gian của R-20 |

## Vấn đề còn mở

Các mục Target đạt, trừ các điểm sau:

- Target 3, 5, 8 đạt một phần với bảng member: cột member_id kiểu UUID và tên bảng member là suy từ kiểu định danh của P12 (string UUID), chưa có P13 của PKG-26 xác nhận. Hai ràng buộc fk_class_booking_member, fk_waitlist_entry_member nằm ở khối ALTER TABLE cuối script và chỉ chạy được khi bảng member đã tồn tại.
- Target 8 đạt một phần: C-06 (sức chứa theo phòng, BR-10) và C-07 (trùng phòng, trùng huấn luyện viên, BR-36, BR-37) chưa giữ được ở CSDL do room, trainer là chuỗi tạm và lớp chưa có thời lượng (Q-03, Q-05, Q-32). C-04 (BR-08) giữ ở ứng dụng và còn rủi ro đồng thời đã nêu ở P12.
- Target 6 đạt: mọi bảng có FD và đạt 3NF, BCNF. Điểm cần theo dõi: sức chứa xác định theo phòng (BR-10) có thể làm group_class vi phạm 3NF khi Q-03 được trả lời (F5.2).
- Chọn giữa hai quy tắc (C9): F2 của prompt coi value object nằm trong thuộc tính đa trị là bảng thuộc tính đa trị, còn F4.2 coi association class là bảng trung gian của quan hệ nhiều - nhiều. DC-WaitlistEntry thuộc cả hai; cả hai cho cùng bảng TBL-04 với khoá chính (waitlist_id, member_id), ghi ở cả F2 và F4.2.
- Khoá chính ghép của waitlist_entry ngầm cấm một hội viên có hai mục chờ trong cùng một danh sách, trong khi Q-59 (hội viên đã đứng trong danh sách chờ có được vào lần nữa không) chưa có trả lời. Khoá chính theo định danh Waitlist + Member của P12 F5 R-20; nếu Q-59 cho phép vào lại hoặc cần lưu lịch sử rời danh sách, đổi sang khoá thay thế kèm cột trạng thái.
- Hành vi khi hội viên huỷ chỗ hoặc rời danh sách chờ (xoá dòng hay đánh dấu) thuộc UC-011, UC-012, UC-013 chưa có P07 nên chưa có cột trạng thái cho class_booking và waitlist_entry; khi các use case đó có P12, chạy lại P13 cho phạm vi này.
- Giờ cao điểm 17:00 đến 20:00 (tham số KHOI_LUONG_DU_LIEU) khác mốc tải đỉnh 6 giờ sáng thứ Hai của NFR-01; index thiết kế phục vụ cả hai, nhưng không có số đo nên chưa kiểm chứng được mức đạt (Q-42, Q-76).
- Phiên bản PostgreSQL chưa chốt; script dùng gen_random_uuid() có sẵn từ phiên bản 13. Script đã chạy thử không lỗi trên PostgreSQL 14 với bảng member giả lập khoá id UUID.
- Chưa mở file .drawio bằng draw.io để kiểm tra bằng mắt; đã kiểm bằng chương trình XML hợp lệ, không nén, toạ độ bội số của 10, không chồng node, khoảng cách node từ 40.
