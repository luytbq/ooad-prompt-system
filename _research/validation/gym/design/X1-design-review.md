# X1 - Review thiết kế - PKG-15 GroupClassService, PKG-29 GroupClass - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | X1 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CHE_DO_GIA_DINH NGHIEM_NGAT, MUC_CHI_TIET GON, CONG_NGHE TypeScript với NestJS, PostgreSQL); P12-class-design/PKG-15-PKG-29-group-class.md (1.0; F1, F1b, F2, F3, F4, F5, F6, F7, F9, Câu hỏi mở, Đề xuất sửa artifact trước, Vấn đề còn mở; không đọc bảng Node, Edge của F8); P13-data-model.md (1.0; F1, F2, F4, F5, F6, bảng Edge của F8.1, Câu hỏi mở, Vấn đề còn mở); P09-architecture.md (1.0; F4, F5, F6, F7); P10-design-elements.md (1.0; F2, F3, F4, F5, F6, Đề xuất sửa artifact trước); P11b-system-interfaces (1.0; SS-06 F2, F3, F5, F7 và SS-03, SS-04 F2, F3, F6 qua grep, mục Đề xuất sửa artifact trước của file chung); P07-uc-analysis UC-010, UC-015 (1.0; bảng message F5); P08-analysis-model.md (1.0; F4 dòng R-14 đến R-24); P05-glossary.md (1.0; GL-05, GL-08, GL-13, GL-19 đến GL-23, GL-26 đến GL-29, GL-35, GL-36, GL-38, GL-39); P06-supplementary-spec.md (NFR-01, NFR-10, NFR-11). Mã Q lớn nhất do người dùng cung cấp: Q-107, quét lại ở thư mục đầu ra cho cùng kết quả; chưa có ASM. YEU_CAU_BO_SUNG: các đề xuất sửa artifact trước chỉ đổi cấu trúc, cách gọi hoặc thêm REQ vào cột REQ của P02 coi là chưa áp dụng |
| Phạm vi | Thiết kế lớp P12 của PKG-15 GroupClassService và PKG-29 GroupClass; mô hình dữ liệu P13 tương ứng (TBL-01 đến TBL-04); trong bối cảnh P09, P10, P11b. Nghiệp vụ: UC-005, UC-010, UC-015, UC-018 (lớp trong phạm vi chủ yếu phục vụ UC-010, UC-015). Lần review đầu, RV bắt đầu từ RV-01 |
| Mã Q, ASM cuối đã cấp | Q-107 (lần chạy này không cấp Q mới); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Phạm vi và phương pháp

| Hạng mục | Nội dung |
|---|---|
| Artifact và phiên bản đã review | P12 PKG-15-PKG-29 1.0; P13 1.0 (4 bảng); đối chiếu P09 1.0, P10 1.0, P11b 1.0, P07 UC-010, UC-015 1.0, P08 1.0 |
| Phần tử trong phạm vi | 2 package (PKG-15, PKG-29); 6 lớp có hành vi (DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler, DC-GroupClass, DC-ClassBooking, DC-Waitlist, DC-MemberBookingQuota); 2 interface (IF-14, IF-16); 12 kiểu phụ trợ (F1b); 33 operation (F2); 22 quan hệ (R-15 đến R-22, R-29 đến R-42); 1 state machine (ST-01); 4 bảng (TBL-01 đến TBL-04), 5 khoá ngoại (hai khoá tới bảng member ngoài phạm vi) |
| Nhóm tiêu chí đã áp dụng | Tất cả: MOD, CPL, COH, SOLID, GRASP, PRN, PKP, SML, CNS, DAT |
| Phần không review được và lý do | (1) Thân hàm DC-GroupClass.assessBookability (bước kiểm tra thời hạn đặt chỗ) và DC-Waitlist.compareWaitOrder chưa đặc tả vì chờ Q-11, Q-58, Q-61 nên coupling, cohesion của hai operation này ghi theo chữ ký. (2) Không đọc bảng Node, Edge của P12 F8: tiêu chí CNS "Class diagram khớp bảng" ghi "Không xét: không đọc F8". (3) Lớp ngoài phạm vi (DC-Member PKG-26, DC-GroupClassRepositoryImpl PKG-20, SS-03, SS-04, SS-06) chỉ xét qua chữ ký và mô tả trong P12 F4b, P10, P11b. (4) Chỉ số Ca, Ce, I, A, D (F6.3) không tính vì MUC_CHI_TIET là GON (prompt: chỉ khi DAY_DU). (5) P07 UC-005, UC-018 không có lớp trong PKG-15, PKG-29 (đã grep: không có GroupClass, ClassBooking, Waitlist) nên chỉ UC-010, UC-015 được kiểm tra truy vết message. (6) Mức đạt NFR-01 chưa đo được (Q-42) nên các phát hiện về tải ghi Cần xác nhận |

## F2. Bảng phát hiện

| RV | Nguyên lý / tiêu chí vi phạm | Phần tử | Bằng chứng | Mức độ | Đề xuất sửa | Bước cần sửa | Nhóm | Độ tin cậy | Trạng thái |
|---|---|---|---|---|---|---|---|---|---|
| RV-01 | MOD Protection; GRASP Protected Variations | DC-CancelUnderBookedClassHandler.handleMarkDue, cancelAbsenceMark, cancelWaitlistTransferMark, notifyBookedMembers; IF-14.runInTransaction; IF-06; SS-03, SS-04 (hàng chờ gửi nền) | P12 F3 handleMarkDue: "Ranh giới giao dịch bao trọn bước 2 đến 6 (huỷ lớp và huỷ mốc cùng commit); gửi thông báo sau commit". P12 Vấn đề còn mở: "nếu tiến trình dừng giữa lúc commit huỷ lớp và lúc chuyển hết yêu cầu gửi, mốc được SS-06 giao lại sẽ gặp lớp đã huỷ (nhánh 2a) và không gửi tiếp cho hội viên chưa được báo; hàng chờ gửi nền của SS-03, SS-04 cũng nằm trong bộ nhớ". Cùng mục: runInTransaction cần "ngữ cảnh giao dịch dùng chung cho IF-11 và IF-14", không nêu IF-06 nên khẳng định huỷ mốc cùng commit chưa có cơ chế đỡ | Cao | Ghi yêu cầu thông báo cho từng hội viên vào một bảng hàng chờ thông báo trong chính giao dịch huỷ lớp (transactional outbox, thêm một interface kho hàng chờ ở Domain); tiến trình nền đọc hàng chờ rồi gọi IF-03, IF-04 và đánh dấu đã chuyển. Với hai mốc: huỷ sau commit bằng IF-06.cancelMark (đã idempotent theo P11b) và bỏ lời khẳng định "cùng commit", hoặc đặc tả IF-06 tham gia cùng ngữ cảnh giao dịch. Việc mất thông báo khi dừng tiến trình không cần chờ câu trả lời nghiệp vụ nên không cấp Q | P11b; P12; P13 | MOD | Cần xác nhận: Q-85 (cũ, có lưu việc đã gửi hay không) và Q-65 (cũ, gửi không được) chỉ quyết định có thêm báo cáo trạng thái hay không, không chặn việc dùng hàng chờ kỹ thuật; thông tin thiếu: cơ chế hàng chờ của SS-03, SS-04 là ngoài phạm vi, giao cho P11b | Mở |
| RV-02 | MOD Protection; DAT Ràng buộc BR không giữ ở CSDL | DC-BookClassSpotHandler.bookClass; DC-MemberBookingQuota.hasReachedDailyLimit; P13 C-04 | P12 Vấn đề còn mở: "hai yêu cầu đồng thời của cùng một hội viên cho hai lớp khác nhau trong cùng ngày có thể cùng vượt qua bước 6 vì mỗi giao dịch chỉ khoá dòng của lớp mình ... chưa thêm khoá theo hội viên". P13 F4.4 C-04: "Khoá dòng group_class không bảo vệ ràng buộc này". BR-08 (tối đa 2 lớp mỗi hội viên mỗi ngày) nằm trên đường tải đỉnh NFR-01 (1.500 phiên đồng thời lúc 6 giờ sáng thứ Hai) | Cao | Trong bookClass bước 3, nạp hội viên bằng một operation khoá dòng (IF-11.findByIdForUpdate, thay cho findById) rồi mới khoá lớp ở bước 4; mọi giao dịch cần cả hai dòng khoá hội viên trước, lớp sau. Cập nhật C-04 ở P13 sang cách giữ này. Không cần Q vì là quyết định kỹ thuật theo C1.7 (nâng một mức từ Trung bình: BR-08 nằm trên đường tải đỉnh của NFR-01) | P12; P13 | MOD | Chắc chắn | Mở |
| RV-03 | CPL Content coupling (nguy cơ); GRASP Information Expert; PRN Encapsulation | DC-GroupClass, DC-Waitlist, DC-ClassBooking; IF-14.findByIdForUpdate, IF-14.save; DC-GroupClassRepositoryImpl (PKG-20) | P12 F2 DC-GroupClass.GroupClass(...): "Khởi tạo lớp ở trạng thái SCHEDULED, chưa có chỗ đã đặt và danh sách chờ"; F7: status, bookings, waitlist, entries đều visibility "-" (private) và không có operation nào đặt lại chúng; F2 IF-14.findByIdForUpdate: "Nạp lớp cùng chỗ đã đặt (kèm hội viên) và danh sách chờ"; IF-14.save: "Lưu thay đổi của lớp: trạng thái, chỗ đã đặt mới, mục chờ mới". F7 DC-ClassBooking.id "{readOnly}": "bỏ trống cho tới khi IF-14.save gán". Không có operation tái dựng đối tượng từ CSDL, cũng không có operation cho biết phần thay đổi cần lưu, nên PKG-20 chỉ nạp và lưu được bằng cách đọc, ghi trực tiếp thuộc tính private (kể cả thuộc tính readOnly) | Cao | Thêm cho DC-GroupClass một factory tĩnh tái dựng từ dữ liệu đã lưu (restore) và operation công bố thay đổi cần lưu (chỗ đã đặt mới, mục chờ mới, trạng thái); định danh của DC-ClassBooking, DC-Waitlist truyền qua factory hoặc cấp ngay lúc tạo (UUID sinh ở ứng dụng) để bỏ ngoại lệ readOnly. Cập nhật chữ ký IF-14 và F3 tương ứng | P12 | PRN | Cần xác nhận: cách PKG-20 hiện thực ánh xạ (ORM đọc thuộc tính private hay dùng factory) là kỹ thuật ngoài phạm vi, giao cho lần chạy P12 của PKG-20; mức Cao thay vì Nghiêm trọng vì chưa thấy mã hiện thực | Mở |
| RV-04 | CPL Control coupling; SOLID ISP | IF-10.handleMarkDue; DC-CancelUnderBookedClassHandler.handleMarkDue | P12 F2: "handleMarkDue(kind: MarkKind, subjectRef: string, dueAt: Date)" với ngoại lệ "Error khi kind khác ClassCutoff". P11b SS-06 F3: "registerMarkHandler(kind: MarkKind, handler: IScheduleMarkHandler)" nên SS-06 đã chọn handler theo kind trước khi gọi; kind lại được truyền xuống để handler kiểm tra lần nữa. IF-10 được DC-PurchaseOrRenewPackageHandler và DC-CancelUnderBookedClassHandler cùng hiện thực (P10 bảng Interface gọi ngược) | Trung bình | Bỏ tham số kind khỏi IF-10.handleMarkDue (mỗi handler đã gắn với đúng một kind lúc registerMarkHandler), hoặc tách IF-10 thành interface theo từng loại mốc (Extract Interface) nếu một handler phải nhận nhiều loại. Bỏ nhánh ném Error ở P12 F3 bước 1 | P11b; P12 | CPL | Chắc chắn | Mở |
| RV-05 | SOLID SRP; SML Divergent change; COH | DC-CancelUnderBookedClassHandler (handleMarkDue, notifyBookedMembers, composeClassCancelledNotice, cancelAbsenceMark, cancelWaitlistTransferMark, onModuleInit) | P12 F2, F3: lớp vừa điều phối giao dịch huỷ lớp, vừa huỷ hai mốc, vừa soạn nội dung thông báo ("composeClassCancelledNotice ... câu chữ chờ Q-66"), vừa chọn kênh theo từng hội viên ("hỏi kênh nhận thông báo (BR-14)"), vừa nuốt lỗi từng hội viên ("ghi nhật ký và bỏ qua, kết cục chờ Q-65"), vừa tự đăng ký với bộ hẹn giờ. Năm lý do thay đổi độc lập đều đang chờ Q (Q-64, Q-65, Q-66, Q-36, Q-102) mà cùng dồn vào một lớp | Trung bình | Extract Class DC-ClassCancelledNotifier (PKG-15) nhận notifyBookedMembers và composeClassCancelledNotice; handler chỉ gọi notifier sau commit. Giữ nguyên chữ ký IF-10 và các operation P07 | P12 | SOLID | Chắc chắn | Mở |
| RV-06 | CPL Stamp coupling; CNS Phụ thuộc package thiếu ở P09, P10 | IF-03.sendPushNotification(recipient: Member, ...); DC-CancelUnderBookedClassHandler.notifyBookedMembers; PKG-24 --> PKG-26 | P11b SS-03 F2: "sendPushNotification(recipient: Member, content: NotificationContent)" trong khi IF-04 nhận "phone: PhoneNumber"; SS-03 chỉ dùng Member để tra địa chỉ thiết bị (Q-101). P09 F4 và P10 F4 ghi PKG-24 phụ thuộc "-" hoặc PKG-32, không có PKG-26. P11b file chung (Đề xuất sửa artifact trước) đã đề xuất thêm cạnh PKG-24 --> PKG-26: đã đề xuất ở P11b, chưa áp dụng | Trung bình | Đổi chữ ký IF-03 sang kiểu định danh hội viên (recipientId: string) để Services nhận dữ liệu nguyên tố và không phụ thuộc entity; việc tra địa chỉ thiết bị do SS-03 thực hiện qua kho dữ liệu đã có. Nếu giữ chữ ký nhận Member thì P10 phải thêm cạnh PKG-24 --> PKG-26 vào F4, F6 | P11b; P12 | CPL | Cần xác nhận: Q-101 (cũ, nguồn địa chỉ thiết bị) quyết định SS-03 tra địa chỉ bằng cách nào | Mở |
| RV-07 | SML Hidden dependencies; Temporal coupling ẩn; PRN DRY | IF-14.runInTransaction; IF-11 (R-30); DC-BookClassSpotHandler.bookClass; DC-CancelUnderBookedClassHandler.handleMarkDue | P12 F2: "runInTransaction ... mọi repository gọi trong work dùng chung giao dịch" đặt trong IF-14 nhưng bookClass bước 2 đến 3 gọi IF-11.findById bên trong giao dịch của IF-14; Vấn đề còn mở: "DC-GroupClassRepositoryImpl ... phải hiện thực cả runInTransaction với ngữ cảnh giao dịch dùng chung cho IF-11 và IF-14". Bên gọi phải nhớ chỉ gọi IF-11 trong work của IF-14, ràng buộc không nằm ở chữ ký; mỗi interface kho IF-11 đến IF-15 sẽ cần lặp operation này khi P12 của PKG-14, PKG-16 chạy | Trung bình | Extract Interface ITransactionRunner (một operation run(work)) đặt ở package Domain dùng chung, mọi control nhận qua constructor; bỏ runInTransaction khỏi IF-14. Vị trí package do P10 quyết định cùng chỗ với IF-16 (xem RV-17) | P12 | SML | Chắc chắn | Mở |
| RV-08 | MOD Protection; SML Temporal coupling ẩn | DC-BookClassSpotHandler.joinWaitlist, bookClass; DC-Waitlist.addMember; TBL-04.joined_at | P12 F3 joinWaitlist: "1. now = IClock.now(). 2. Trong IF-14.runInTransaction: nạp ... lớp (IF-14.findByIdForUpdate) ... 3. position = lớp.addToWaitlist(member, now)": now lấy trước khi chờ khoá dòng lớp. P13 F6.1 joined_at: "do ứng dụng truyền từ IF-16.now(). Cơ sở thứ tự xếp chờ". Hai yêu cầu đồng thời lấy now theo thứ tự t1 < t2 nhưng có thể nhận khoá theo thứ tự ngược, nên vị trí đã trả cho người nhận khoá trước bị lệch khi người có now nhỏ hơn được chèn sau. bookClass bước 1 có cùng thứ tự với assessBookability | Trung bình | Gọi IClock.now() sau khi đã nạp lớp bằng findByIdForUpdate (trong khoá), mọi thời điểm so sánh và ghi joined_at lấy từ lần gọi đó | P12 | MOD | Chắc chắn | Mở |
| RV-09 | GRASP Information Expert; SML Inappropriate intimacy; DAT Truy vấn thường xuyên theo NFR | DC-ClassBooking.member (R-19); DC-GroupClass.bookings; IF-14.findByIdForUpdate | P12 F2 IF-14.findByIdForUpdate: "Nạp lớp cùng chỗ đã đặt (kèm hội viên) và danh sách chờ"; F5 R-19: DC-ClassBooking --> DC-Member "field"; F7 /bookedCount: "số phần tử của bookings". Đường bookClass chỉ cần một con số (getBookedCount) nhưng phải nạp mọi chỗ đã đặt cùng đối tượng hội viên khi giữ khoá dòng lớp; NFR-01 yêu cầu 1.500 phiên đồng thời. Đồng thời R-19, R-20 làm PKG-29 phụ thuộc PKG-26 chỉ để giữ tham chiếu đối tượng | Trung bình | Replace Object with Id: DC-ClassBooking giữ memberId: string thay cho DC-Member; collectBookedMembers trả danh sách memberId, handler nạp hội viên qua IF-11 (một operation findByIds). Đếm chỗ đã đặt bằng truy vấn đếm theo ix_class_booking_group_class thay vì nạp tập hợp | P12; P13 | GRASP | Cần xác nhận: mức đạt NFR-01 chưa đo được (Q-42, cũ); chưa biết sức chứa lớp lớn nhất (Q-03, cũ) | Mở |
| RV-10 | DAT Thiếu UNIQUE cho khoá nghiệp vụ; CNS nhất quán giữa hai bảng | TBL-02 class_booking; TBL-04 waitlist_entry; DC-GroupClass.reserveSpot | P13 F4.1: TBL-02 "Cặp (group_class_id, member_id) không khai báo UNIQUE vì đặt trùng cùng một lớp chờ Q-59" trong khi TBL-04 F6.1: "Khoá chính ghép làm một hội viên có tối đa một mục chờ trong một danh sách". P12 F3 reserveSpot không kiểm hội viên đã có chỗ. Một hội viên bấm hai lần trong giờ cao điểm tạo hai chỗ đã đặt chiếm hai chỗ của sức chứa | Trung bình | Sau khi Q-59 có câu trả lời: nếu không cho đặt trùng thì thêm UNIQUE (group_class_id, member_id) và kiểm trong reserveSpot (ném ngoại lệ đã đặt), nếu cho phép thì đổi khoá chính của waitlist_entry sang khoá thay thế. Hai bảng phải theo cùng một câu trả lời | P12; P13 | DAT | Cần xác nhận: Q-59 (cũ) | Mở |
| RV-11 | SML Hidden dependencies; GRASP Protected Variations | DC-MemberBookingQuota.hasReachedDailyLimit | P12 F3: "from = 00:00 của ngày chứa classStartTime theo múi giờ của máy chủ ứng dụng ... (Thiết kế: một múi giờ cấu hình cho cả chuỗi; cách tính ngày chờ Q-60)". Múi giờ đọc ngầm từ môi trường tiến trình, không qua constructor như IClock; số node máy chủ chưa chốt (P09 F7, Q-91) nên ranh giới ngày của BR-08 có thể khác nhau giữa các node | Trung bình | Thêm vào IF-16 (hoặc một interface cấu hình nhỏ) operation trả khoảng ngày chứa một thời điểm theo múi giờ cấu hình của chuỗi, tiêm vào DC-MemberBookingQuota; bỏ việc đọc múi giờ tiến trình | P12 | SML | Cần xác nhận: Q-60 (cũ, cách tính ngày) | Mở |
| RV-12 | SOLID ISP | IF-14; DC-MemberBookingQuota (R-39) | P12 F2: IF-14 gồm findSchedule, findByIdForUpdate, save, countMemberBookingsBetween, runInTransaction; F5 R-39 DC-MemberBookingQuota --> IF-14 chỉ gọi countMemberBookingsBetween (F3 hasReachedDailyLimit bước 2) và phải phụ thuộc cả thao tác ghi, khoá | Thấp | Extract Interface IClassBookingCounter (countMemberBookingsBetween) cho DC-MemberBookingQuota; DC-GroupClassRepositoryImpl hiện thực cả hai. Có thể gộp với việc tách runInTransaction ở RV-07 | P12 | SOLID | Chắc chắn | Mở |
| RV-13 | PRN DRY; SML Speculative generality | DC-GroupClass.hasAvailableSpot, reserveSpot, addToWaitlist; DC-BookClassSpotHandler.bookClass bước 8 | P12 F3: cùng điều kiện sức chứa viết ba lần: hasAvailableSpot, reserveSpot bước 2 ("getBookedCount() >= capacity thì ném DC-SpotUnavailableException"), addToWaitlist bước 2 ("getBookedCount() < capacity"); bookClass bước 8 bắt DC-SpotUnavailableException trong khi cùng mục ghi "khoá dòng lớp giữ từ bước 4 đến hết giao dịch nên bước 7 và 8 không có khe hở" | Thấp | Extract Method: reserveSpot và addToWaitlist gọi hasAvailableSpot thay vì lặp biểu thức; bỏ nhánh bắt DC-SpotUnavailableException ở bookClass (giữ ngoại lệ làm bất biến của entity) | P12 | PRN | Chắc chắn | Mở |
| RV-14 | SML Lazy class / Data class | DC-ClassBooking | P12 F1: "Entity mỏng, giữ vì P10 F3 đã ánh xạ và UC-011, UC-012, UC-016 sẽ bổ sung hành vi"; F2 chỉ có constructor và provideBookedMember | Thấp | Giữ nguyên; bổ sung hành vi khi P07 của UC-011, UC-012, UC-016 có. Không gộp vào DC-GroupClass vì có định danh và bảng riêng (TBL-02) | P12 | SML | Chắc chắn | Chấp nhận có lý do |
| RV-15 | PRN KISS / YAGNI | DC-Waitlist; TBL-03 waitlist | P12 F1: "thiết kế theo phương án đối tượng riêng tạo muộn vì ghép được với cả hai câu trả lời của Q-84"; P13 F4.1 TBL-03 chỉ có (id, group_class_id UNIQUE) và TBL-04 tham chiếu waitlist_id | Thấp | Khi Q-84 trả lời danh sách chờ chỉ là tập mục chờ, bỏ TBL-03 và cho waitlist_entry tham chiếu group_class_id, DC-Waitlist gộp vào DC-GroupClass. Hiện chờ câu trả lời nên giữ | P12; P13 | PRN | Cần xác nhận: Q-84 (cũ) | Chấp nhận có lý do |
| RV-16 | CNS Message P07 không có dòng ở P12 F4 | P07 UC-010 msg 2.1.1 checkBookingNotSuspended; P12 F4, F4b | P12 F4 có dòng 2.1.2 ngay sau 2.1 và không có 2.1.1, trong khi cùng bảng có dòng UC-015 msg 1.7 "Lớp nhận ngoài phạm vi (PKG-26): xem F4b"; msg 2.1.1 chỉ nằm ở F4b | Thấp | Thêm dòng UC-010 2.1.1 vào F4 với nội dung "Lớp nhận ngoài phạm vi (PKG-26): xem F4b", như dòng 1.7 | P12 | CNS | Chắc chắn | Mở |
| RV-17 | PKP CRP; CNS Phụ thuộc package thiếu ở P09, P10 | IF-16 IClock; PKG-32; PKG-15 --> PKG-32 | P12 F1: IF-16 đặt "PKG-32 (vị trí chờ P10)"; P12 F9: PKG-15 phụ thuộc PKG-32 (R-32, R-37, PhoneNumber) nhưng P10 F4 hàng PKG-15 ghi "PKG-22, PKG-24, PKG-26, PKG-29". P12 Đề xuất sửa artifact trước (P10) đã nêu: đã đề xuất ở P12, chưa áp dụng. PKG-32 ValueTypes (P10 F4) chứa kiểu giá trị, còn IClock là interface dịch vụ nên bên chỉ dùng kiểu giá trị phải kéo theo cả interface | Thấp | P10 thêm cạnh PKG-15 --> PKG-32 vào F4, F6; đặt IF-16 (và ITransactionRunner ở RV-07) vào một package Domain riêng cho abstraction kỹ thuật dùng chung thay vì PKG-32 | P10; P12 | PKP | Chắc chắn | Mở |
| RV-18 | CNS Persistent không khớp | P12 F1b DC-WaitlistEntry; P13 F2 | P13 F2 dòng DC-WaitlistEntry: Persistent "Không" nhưng TBL "TBL-04"; P12 F1b không có cột Persistent. P13 Đề xuất sửa artifact trước đã đề xuất thêm cột này: đã đề xuất ở P13, chưa áp dụng | Thấp | Thêm cột Persistent vào P12 F1b và ghi DC-WaitlistEntry là value object lưu qua TBL-04; P13 F2 ghi "Có (value object lưu qua bảng trung gian)" | P12; P13 | CNS | Chắc chắn | Mở |
| RV-19 | SML Temporal coupling ẩn | DC-CancelUnderBookedClassHandler.onModuleInit; IF-06.start | P12 F2 onModuleInit: "Tiền: IF-06 chưa start"; P11b SS-06 F3 start(): "Tiền: Đã registerMarkHandler cho các loại mốc cần dùng". Thứ tự đăng ký rồi start chỉ nằm ở tiền điều kiện, không ở chữ ký hay nơi khởi động | Thấp | Ghi ở P12 nơi gọi start (bước khởi động tiến trình nền) và để IF-06.start báo lỗi khi thiếu handler của loại mốc cần dùng, hoặc đổi onModuleInit thành đăng ký trong module khởi động | P12 | SML | Cần xác nhận: thứ tự vòng đời của NestJS (onModuleInit trước onApplicationBootstrap) phụ thuộc cấu hình ứng dụng, thuộc kỹ thuật ngoài phạm vi | Mở |

## F3. Đánh giá coupling

| Phần tử A (phụ thuộc) | Phần tử B (được dùng) | Kênh phụ thuộc | Mức coupling | Bằng chứng | Chấp nhận (Có / Không: RV) |
|---|---|---|---|---|---|
| DC-CancelUnderBookedClassHandler | IF-10 (R-38) | tham số (kind: MarkKind) | Control | P12 F2 handleMarkDue(kind, subjectRef, dueAt), "Error khi kind khác ClassCutoff" | Không: RV-04 |
| DC-CancelUnderBookedClassHandler | IF-03 (R-35) | tham số (recipient: Member) | Stamp | P11b SS-03 F2: chỉ dùng Member để tra địa chỉ thiết bị | Không: RV-06 |
| DC-GroupClassRepositoryImpl (PKG-20, ngoài phạm vi) | DC-GroupClass.status, bookings, waitlist; DC-ClassBooking.id; DC-Waitlist.id, entries | truy cập trực tiếp dữ liệu | Content (nguy cơ, Cần xác nhận) | P12 F2, F7: thuộc tính private, không có operation tái dựng hay công bố thay đổi | Không: RV-03 |
| DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler | IF-11 và IF-14 (R-29, R-30, R-33) | toàn cục (ngữ cảnh giao dịch dùng chung ngầm) | Ngoài thang: temporal coupling ẩn | P12 Vấn đề còn mở: "ngữ cảnh giao dịch dùng chung cho IF-11 và IF-14" | Không: RV-07 |
| DC-MemberBookingQuota | môi trường tiến trình (múi giờ) | toàn cục | Ngoài thang: hidden dependency | P12 F3 hasReachedDailyLimit bước 1 | Không: RV-11 |
| DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler | IF-16 (R-32, R-37) | thuộc tính | Data | now() không tham số; thứ tự gọi so với khoá lấy ở RV-08 | Không: RV-08 |
| DC-MemberBookingQuota | IF-14 (R-39) | thuộc tính | Data (giao diện rộng hơn phần dùng) | chỉ dùng countMemberBookingsBetween | Không: RV-12 |
| DC-BookClassSpotHandler | DC-Member (R-15)<br>DC-GroupClass (R-16)<br>DC-MemberBookingQuota (R-31)<br>IF-14 (R-29)<br>IF-11 (R-30)<br>DC-BookClassResult<br>DC-WaitlistPlacement | biến cục bộ / thuộc tính / kiểu trả về | Data | bookClass(memberId: string, classId: string); enumeration Bookability và BookingOutcome mang nghĩa nghiệp vụ, bên nhận chỉ ánh xạ, không rẽ nhánh hành vi bên gọi | Có |
| DC-CancelUnderBookedClassHandler | DC-GroupClass (R-21)<br>DC-Member (R-22)<br>IF-14 (R-33)<br>IF-06 (R-34)<br>IF-04 (R-36)<br>DC-NotificationContent (R-42) | biến cục bộ / tham số / thuộc tính | Data | notifyBookedMembers(members, info); IF-06.cancelMark(kind, subjectRef) | Có |
| DC-GroupClass | DC-ClassBooking (R-17)<br>DC-Waitlist (R-18)<br>DC-Member (R-40)<br>DC-ClassInfo | thuộc tính / tham số / kiểu trả về | Data | reserveSpot(member), addToWaitlist(member, now); Member được lưu nguyên khối nên không phải stamp | Có |
| DC-ClassBooking | DC-Member (R-19) | thuộc tính | Data | ClassBooking(member); tham chiếu đối tượng thay vì định danh xét ở RV-09 | Có |
| DC-Waitlist | DC-WaitlistEntry<br>DC-Member (R-20) | thuộc tính | Data | entries; addMember(member, now) | Có |
| IF-14 | DC-GroupClass (R-41)<br>DC-ClassInfo | tham số / kiểu trả về | Data | findByIdForUpdate, save(groupClass), findSchedule | Có |
| Bảng class_booking, waitlist_entry | bảng group_class, waitlist, member | bảng CSDL dùng chung | Data | Mỗi bảng do một interface kho (IF-14, IF-11) ghi; không có bảng ghi bởi nhiều module (P13 F4.2) | Có |

## F4. Đánh giá cohesion

| Phần tử (PKG / DC / DC.operation) | Mức cohesion | Lý do (nhóm phần tử và lý do đặt cùng nhau) | Chấp nhận (Có / Không: RV) |
|---|---|---|---|
| PKG-15 GroupClassService | Functional | Hai control cùng nhóm chức năng Lớp nhóm, cùng dùng DC-GroupClass (P10 F4 tiêu chí nhóm) | Có |
| PKG-29 GroupClass | Functional | Aggregate lớp nhóm, chỗ đã đặt, danh sách chờ, hạn mức đặt, kho dữ liệu; các lớp có quan hệ R-17, R-18 | Có |
| DC-BookClassSpotHandler | Functional | Ba sự kiện hệ thống của UC-010 (getClassSchedule, bookClass, joinWaitlist), cùng một use case, một lý do thay đổi | Có |
| DC-CancelUnderBookedClassHandler | Sequential | Chuỗi xử lý UC-015 nhưng trộn soạn nội dung, chọn kênh, huỷ mốc, đăng ký bộ hẹn giờ | Không: RV-05 |
| DC-GroupClass | Functional | Mọi operation cùng hướng tới vòng đời và sức chứa của một lớp; 11 operation công khai, 9 thuộc tính. Theo dõi: UC-009, UC-011 đến UC-014 sẽ thêm operation vào cùng lớp | Có |
| DC-ClassBooking | Functional | Một khái niệm chỗ đã đặt, mỏng | Có (RV-14) |
| DC-Waitlist | Functional | Giữ danh sách có thứ tự và quy tắc thứ tự tại compareWaitOrder | Có |
| DC-MemberBookingQuota | Functional | Một trách nhiệm: BR-08 | Có |
| IF-14 IGroupClassRepository | Communicational | Cùng dữ liệu lớp nhóm nhưng gồm giao dịch, lịch (đọc), đếm, nạp và lưu aggregate | Không: RV-07, RV-12 |
| IF-16 IClock | Functional | Một operation now() | Có |
| DC-BookClassSpotHandler.bookClass | Sequential | 10 bước kiểm tra theo thứ tự P04 mục 8, đầu ra bước trước là điều kiện bước sau | Có |
| DC-CancelUnderBookedClassHandler.handleMarkDue | Sequential | 8 bước huỷ lớp, huỷ mốc, gom hội viên, gửi thông báo; phần thông báo tách ở RV-05 | Không: RV-05 |
| Kiểu phụ trợ PKG-29: DC-ClassInfo, DC-WaitlistEntry, DC-GroupClassStatus, DC-Bookability, DC-CancellationCheck, DC-GroupClassNotFoundException, DC-SpotUnavailableException, DC-InvalidClassStateException, DC-WaitlistNotAllowedException | Functional | Value object, enumeration, exception không có hành vi | Có |
| Kiểu phụ trợ PKG-15: DC-WaitlistPlacement, DC-BookClassResult, DC-BookingOutcome | Functional | Value object, enumeration kết quả của handler | Có |

## F5. Danh mục nguyên lý, design smell, nhất quán, dữ liệu

| Nguyên lý | Phần tử đã xét | Kết luận (Đạt / Vi phạm: RV) |
|---|---|---|
| MOD Decomposable | PKG-15, PKG-29 chia theo nhóm chức năng Lớp nhóm và Domain | Đạt |
| MOD Composable | IF-14, IF-16, IF-10, IF-03, IF-04, IF-06 | Vi phạm: RV-07 (IF-14 chỉ ghép được cùng IF-11 qua ngữ cảnh ngầm) |
| MOD Understandable | DC-GroupClass (11 operation, ST-01), DC-BookClassSpotHandler | Đạt |
| MOD Continuity | Đổi cổng SMS nhà mạng: 0 lớp, 1 package (SS-04, PKG-24). Thêm kênh thông báo thứ ba: 2 lớp, 3 package (DC-CancelUnderBookedClassHandler, DC-Member; PKG-15, PKG-24, PKG-26). Đổi quy tắc thứ tự xếp chờ (Q-61): 1 lớp, 1 package (DC-Waitlist, PKG-29) cộng index TBL-04. Đổi ngưỡng huỷ lớp BR-13: 1 lớp, 1 package (DC-GroupClass, PKG-29). Đổi mức tối đa BR-08: 1 lớp, 1 package (DC-MemberBookingQuota, PKG-29) | Đạt |
| MOD Protection | handleMarkDue, joinWaitlist, bookClass, thông báo sau commit | Vi phạm: RV-01, RV-02, RV-08 |
| SOLID SRP | DC-CancelUnderBookedClassHandler; DC-GroupClass (theo dõi, chưa vi phạm); các lớp còn lại | Vi phạm: RV-05 |
| SOLID OCP | notifyBookedMembers rẽ nhánh theo kênh (PUSH, SMS) tại một nơi duy nhất trong phạm vi, UC-005 không gửi thông báo (đã grep P07) | Đạt |
| SOLID LSP | Không có cây kế thừa; DC-CancelUnderBookedClassHandler hiện thực IF-10 | Đạt |
| SOLID ISP | IF-14, IF-10 | Vi phạm: RV-12, RV-04 |
| SOLID DIP | Control phụ thuộc IF-14, IF-11, IF-06, IF-03, IF-04, IF-16; IF-14 ở Domain, hiện thực ở PKG-20 (đi xuống); IF-10 định nghĩa ở PKG-22, hiện thực ở PKG-15 (đi xuống); không có new lớp hạ tầng trong F3 | Đạt |
| GRASP Information Expert | DC-GroupClass (đếm, huỷ), DC-MemberBookingQuota, tải aggregate | Vi phạm: RV-03, RV-09 |
| GRASP Creator | DC-GroupClass tạo DC-ClassBooking, DC-Waitlist (R-17, R-18); DC-CancelUnderBookedClassHandler tạo NotificationContent | Đạt |
| GRASP Controller | DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler đại diện use case, boundary ở PKG-05, PKG-10 ngoài phạm vi | Đạt |
| GRASP Low Coupling, High Cohesion | Xem F3, F4 | Vi phạm: RV-04, RV-05, RV-06, RV-07 |
| GRASP Polymorphism | Không có rẽ nhánh theo loại trong phạm vi | Đạt |
| GRASP Pure Fabrication | DC-MemberBookingQuota, IF-14 (repository), IF-16 | Đạt |
| GRASP Indirection | IF-14, IF-16, IF-03, IF-04, IF-06 | Đạt |
| GRASP Protected Variations | Kho dữ liệu, đồng hồ, cổng thông báo, bộ hẹn giờ đều qua interface; múi giờ và giao dịch chưa được bọc | Vi phạm: RV-01, RV-11 |
| PRN Encapsulation | DC-GroupClass và aggregate khi nạp, lưu | Vi phạm: RV-03 |
| PRN Composition over inheritance | Không dùng kế thừa | Đạt |
| PRN Program to an interface | Handler nhận IF-14, IF-11, IF-16, IF-06, IF-03, IF-04 qua constructor | Đạt |
| PRN Law of Demeter | Handler chỉ gọi đối tượng nhận qua constructor, tham số, giá trị trả về của chính nó (F3 bookClass, handleMarkDue); không có chuỗi a.getB().getC() | Đạt |
| PRN DRY | Điều kiện sức chứa (BR-11) viết ba lần; BR-08 chỉ ở DC-MemberBookingQuota | Vi phạm: RV-13 |
| PRN KISS | DC-Waitlist, TBL-03 | Vi phạm: RV-15 (Chấp nhận có lý do) |
| PRN YAGNI | IF-16 có ba bên dùng thật (bookClass, handleMarkDue, kiểm thử); kiểu phụ trợ đều có chỗ dùng | Đạt |
| SML God class / Large class | DC-GroupClass 11 operation, 9 thuộc tính, một khái niệm | Không phát hiện vi phạm |
| SML Data class / Lazy class | DC-ClassBooking | Vi phạm: RV-14 (Chấp nhận có lý do) |
| SML Feature envy | Handler gọi assessBookability, hasAvailableSpot, reserveSpot trên GroupClass; không dùng dữ liệu lớp khác nhiều hơn của mình | Không phát hiện vi phạm |
| SML Shotgun surgery / Divergent change | DC-CancelUnderBookedClassHandler | Vi phạm: RV-05 |
| SML Long parameter list, Data clumps, Primitive obsession | Tối đa 3 tham số (handleMarkDue, GroupClass constructor 6 tham số cùng là thuộc tính của lớp) | Không phát hiện vi phạm |
| SML Switch statements | Rẽ nhánh theo outcome và theo kênh, không theo mã loại lặp lại | Không phát hiện vi phạm |
| SML Message chains, Middle man, Inappropriate intimacy | ClassBooking --> Member tham chiếu đối tượng | Vi phạm: RV-09 |
| SML Hidden dependencies, Temporal coupling ẩn | runInTransaction, múi giờ, now() trước khoá, onModuleInit | Vi phạm: RV-07, RV-08, RV-11, RV-19 |
| PKP ADP (không vòng) | Xem F6.2 | Đạt |
| PKP Hướng layer, không nhảy layer | PKG-15 --> PKG-29, PKG-26, PKG-22, PKG-24, PKG-32; PKG-29 --> PKG-26 | Đạt |
| PKP Chỉ lớp public được tham chiếu từ ngoài | P12 F9 đoạn kiểm tra gán package: DC-ClassBooking, DC-Waitlist, DC-WaitlistEntry chỉ PKG-20 dùng | Đạt |
| PKP REP, CCP | PKG-29 cùng lý do thay đổi (nhóm Lớp nhóm) | Đạt |
| PKP CRP | PKG-32 chứa kiểu giá trị lẫn IF-16 (đề xuất) | Vi phạm: RV-17 |
| PKP SDP, SAP | Không tính được vì MUC_CHI_TIET là GON (F6.3 bỏ qua) | Chưa xét đủ |
| CNS Message P07 có dòng ở P12 F4; operation public có nguồn | UC-010, UC-015 | Vi phạm: RV-16 |
| CNS AC có DC; IF có lớp «interface» và hiện thực | AC-E-Member tách sang DC-MemberBookingQuota; IF-14, IF-16, IF-10 | Đạt |
| CNS State machine khớp operation, thuộc tính; guard khớp BR | ST-01 T1 đến T4, status, getStatus | Đạt |
| CNS Multiplicity P12 khớp BR và NULL, FK ở P13; lớp persistent có bảng | R-17 đến R-20 và F4.2 khớp; DC-WaitlistEntry Persistent | Vi phạm: RV-18 |
| CNS Phụ thuộc package khớp P09, P10 | PKG-15 --> PKG-32, PKG-24 --> PKG-26 | Vi phạm: RV-06, RV-17 |
| CNS Class diagram khớp bảng | Không đọc F8 | Không xét: không đọc F8 |
| CNS Tên dùng đúng glossary | ClassBooking (GL-05), Waitlist (GL-08), GroupClass (GL-29), classType (GL-27), room (GL-35), capacity (GL-38), startTime (GL-13), BookingSuspension (GL-23) | Đạt |
| DAT 3NF, phi chuẩn hoá | TBL-01 đến TBL-04 (P13 F5.1); F5.3 không phi chuẩn hoá | Đạt (theo dõi Q-03: phụ thuộc bắc cầu phòng --> sức chứa nếu Q-03 xác nhận) |
| DAT Composition CASCADE, FK, M:N, UNIQUE | waitlist_entry CASCADE theo waitlist; R-17 RESTRICT; thiếu UNIQUE cho cặp hội viên - lớp | Vi phạm: RV-10 |
| DAT Kiểu tiền, CHECK miền giá trị | Không có cột tiền; ck_group_class_capacity, ck_group_class_status | Đạt |
| DAT Index và truy vấn theo NFR | ix_group_class_start_time, ix_class_booking_group_class, ix_class_booking_member, uq_waitlist_group_class, ix_waitlist_entry_waitlist_joined phục vụ các truy vấn ghi ở P13 F6.3; đường nạp aggregate đầy đủ xét ở RV-09 | Đạt (kèm RV-09) |

## F6. Phụ thuộc package

F6.1. Bảng phụ thuộc

| PKG nguồn | PKG đích | Quan hệ lớp tạo ra phụ thuộc (R-nn) | Hợp lệ theo layer (Có / Không) |
|---|---|---|---|
| PKG-15 | PKG-29 | R-16, R-21, R-29, R-31, R-33 | Có (Application --> Domain) |
| PKG-15 | PKG-26 | R-15, R-22, R-30 (IF-11) | Có (Application --> Domain) |
| PKG-15 | PKG-22 | R-34, R-38 (realization IF-10 đi xuống) | Có (Application --> Services, V4 a) |
| PKG-15 | PKG-24 | R-35, R-36, R-42 | Có (Application --> Services, V5) |
| PKG-15 | PKG-32 | R-32, R-37, kiểu PhoneNumber | Có (Application --> Domain); chưa có ở P10 F4: RV-17 |
| PKG-29 | PKG-26 | R-19, R-20, R-40 | Có (cùng layer Domain, một chiều, V3, V7) |
| PKG-20 | PKG-29 | realization IF-14 (ngoài phạm vi) | Có (Services --> Domain, V4 b) |
| PKG-10 | PKG-15 | R-14 (ngoài phạm vi) | Có (Presentation --> Application) |
| PKG-24 | PKG-26 | IF-03 recipient: Member (ngoài phạm vi) | Có (Services --> Domain); chưa có ở P09 F4, P10 F4: RV-06 |

F6.2. Vòng phụ thuộc: Không có. Đã dò theo các cạnh trên cộng cạnh P09 F6 của PKG-20, PKG-22, PKG-24: PKG-15 --> {PKG-29, PKG-26, PKG-22, PKG-24, PKG-32}; PKG-29 --> PKG-26; PKG-22 --> PKG-20 --> {PKG-26, PKG-29, ...}; PKG-24 --> {PKG-32, PKG-26}; PKG-26, PKG-32 không phụ thuộc package nào.

F6.3. Chỉ số: Không áp dụng (MUC_CHI_TIET là GON, prompt chỉ tính khi DAY_DU).

## F7. Tổng hợp

| Mức độ | Số phát hiện | Mã RV |
|---|---|---|
| Nghiêm trọng | 0 | - |
| Cao | 3 | RV-01, RV-02, RV-03 |
| Trung bình | 8 | RV-04, RV-05, RV-06, RV-07, RV-08, RV-09, RV-10, RV-11 |
| Thấp | 8 | RV-12, RV-13, RV-14, RV-15, RV-16, RV-17, RV-18, RV-19 |

Thứ tự chạy lại đề xuất:

1. P10: RV-17.
2. P11b: RV-01, RV-04, RV-06.
3. P12 (PKG-15, PKG-29): RV-01 đến RV-19.
4. P13: RV-01, RV-02, RV-09, RV-10, RV-15, RV-18.

Nhóm không phát hiện vi phạm: SML God class, Feature envy, Long parameter list, Switch statements; SOLID LSP, OCP; PRN Law of Demeter.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Không có | Lần chạy này không cấp Q mới. Các phát hiện Cần xác nhận dẫn Q cũ: Q-59 (RV-10), Q-60 (RV-11), Q-84 (RV-15), Q-85, Q-65 (RV-01), Q-101 (RV-06), Q-03, Q-42 (RV-09) | - | - |

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Xem F2 | - | Toàn bộ đề xuất nằm ở F2 | - |

## Vấn đề còn mở

- Target 1 đạt một phần: P12 F8 (Node, Edge) không đọc nên tiêu chí CNS "Class diagram khớp bảng" ghi "Không xét: không đọc F8"; SDP, SAP ghi "Chưa xét đủ" vì MUC_CHI_TIET là GON.
- Target 1, 4 đạt một phần với DC-GroupClass.assessBookability và DC-Waitlist.compareWaitOrder: thân hàm chưa đặc tả (Q-11, Q-58, Q-61) nên coupling và cohesion của hai operation chỉ xét theo chữ ký.
- Target 8: RV-01, RV-03, RV-06, RV-09, RV-10, RV-11, RV-15, RV-19 là Cần xác nhận; thông tin thiếu ghi tại cột Độ tin cậy của từng dòng.
- Chọn giữa hai nguyên lý (RV-09): Information Expert muốn giữ tham chiếu đối tượng hội viên trong chỗ đã đặt để GroupClass tự trả danh sách hội viên, còn Low Coupling và hiệu năng NFR-01 muốn giữ định danh. Chọn định danh, đánh đổi: handler phải nạp hội viên qua IF-11 ở UC-015.
- Q-76 được P13 dẫn cùng Q-42 cho NFR-01 nhưng P10 Vấn đề còn mở ghi Q-76 đã đóng theo hồ sơ cập nhật sau P09; review chỉ dẫn Q-42.
