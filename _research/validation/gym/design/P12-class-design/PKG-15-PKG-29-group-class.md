# P12 - Thiết kế lớp - PKG-15 GroupClassService, PKG-29 GroupClass - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P12 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CHE_DO_GIA_DINH NGHIEM_NGAT, CONG_NGHE TypeScript với NestJS, MUC_CHI_TIET GON); P10-design-elements.md (1.0; F2, F3, F4, F5, F6, Đề xuất sửa artifact trước, Vấn đề còn mở); P08-analysis-model.md (1.0; F3, F4, F6, Câu hỏi mở, Đề xuất sửa artifact trước); P09-architecture.md (1.0; F3, F4, F5, F6, F7, F8, Vấn đề còn mở); P07-uc-analysis/UC-010-book-class-spot-analysis.md và UC-015-cancel-under-booked-class-analysis.md (1.0; F1 đến F5, Câu hỏi mở, Đề xuất sửa artifact trước, Vấn đề còn mở); P11b-system-interfaces.md (1.0; F8, Câu hỏi mở, Đề xuất sửa artifact trước, Vấn đề còn mở) cùng SS-03, SS-04, SS-06 (F1, F2, F3, F5, F7); P11a-gui/screen-list.md (1.1; mục 1, mục 2, Câu hỏi mở, Đề xuất sửa artifact trước) cùng SCR-06, SCR-07, SCR-08 (d, e, h, Câu hỏi mở); P04-uc-specs/UC-010, UC-015 (1.0; mục 1 đến 8, Câu hỏi mở) và _BR-register.md (BR-06 đến BR-14, BR-23); P06-supplementary-spec.md (NFR-01, NFR-10, NFR-11); P05-glossary.md (GL-05, GL-08, GL-13, GL-19 đến GL-23, GL-26 đến GL-29, GL-35, GL-36, GL-38, GL-39). Mã Q, ASM lớn nhất do người dùng cung cấp: Q-105, quét lại ở thư mục đầu ra cho cùng kết quả; chưa có ASM; chưa có file P12 nào khác. QUY_UOC_KIEU_DU_LIEU: Không có (dùng kiểu TypeScript). MAU_THIET_KE_DA_CHOT: Không có. YEU_CAU_BO_SUNG: chỉ UC-005, UC-010, UC-015, UC-018 có P04, P07; các đề xuất sửa chỉ đổi cấu trúc thiết kế (P10 cho P09 F4, V4, F5; P10 cho P08 về AC-E-Member; P07 UC-010 cho P04 chờ Q-83) coi là chưa áp dụng và không chạy lại bước trước |
| Phạm vi | PKG-15 GroupClassService (DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler) và PKG-29 GroupClass (DC-GroupClass, DC-ClassBooking, DC-Waitlist, DC-MemberBookingQuota, IF-14 IGroupClassRepository); UC-010 Đặt chỗ lớp nhóm, UC-015 Huỷ lớp nhóm ít người đặt. 7 lớp có hành vi, cộng IF-16 cấp mới và 12 kiểu phụ trợ |
| Mã Q, ASM cuối đã cấp | Q-107 (Q mới của lần chạy: Q-106, Q-107); ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Mã khác cuối đã cấp | R-42 (R-nn mới: R-29 đến R-42); ST-01; IF-16; DC mới: DC-ClassInfo, DC-WaitlistEntry, DC-WaitlistPlacement, DC-BookClassResult, DC-GroupClassStatus, DC-Bookability, DC-CancellationCheck, DC-BookingOutcome, DC-GroupClassNotFoundException, DC-SpotUnavailableException, DC-InvalidClassStateException, DC-WaitlistNotAllowedException |

## F1. Bảng lớp thiết kế

| DC | Tên | Stereotype | PKG | Trách nhiệm | Nguồn AC | Loại | Persistent | Ghi chú thiết kế |
|---|---|---|---|---|---|---|---|---|
| DC-BookClassSpotHandler | BookClassSpotHandler | «control» | PKG-15 | Điều phối các bước của UC-010 Đặt chỗ lớp nhóm trong ranh giới giao dịch ghi chỗ đã đặt | AC-C-BookClassSpotHandler | class | Không | public (P10 F5: PKG-10 gọi). Giữ tên P10; Controller là vai trò MVC của DC-BookClassSpotController ở PKG-10. Bốn câu hỏi 1.4: cần (điều phối nhiều bước kiểm tra, mở giao dịch); không tách (một use case, một tác nhân, một lý do thay đổi); căn cứ: độ phức tạp vừa, giao dịch khoá dòng lớp (BR-11, NFR-01) |
| DC-CancelUnderBookedClassHandler | CancelUnderBookedClassHandler | «control» | PKG-15 | Điều phối UC-015 Huỷ lớp nhóm ít người đặt khi mốc 2 giờ trước giờ học đến | AC-C-CancelUnderBookedClassHandler | class | Không | package-private (P10 F5: chỉ gọi qua IF-10); hiện thực IF-10 (R-38). Bốn câu hỏi 1.4: cần (điều phối huỷ lớp, huỷ mốc, gom hội viên, lặp gửi thông báo vì entity không gọi boundary); không tách (một use case); căn cứ: độ phức tạp vừa, ranh giới giao dịch ở bước 2 đến 4 |
| DC-GroupClass | GroupClass | «entity» | PKG-29 | Là gốc tập hợp của một lớp nhóm, kiểm soát vòng đời trạng thái của lớp cùng chỗ đã đặt và danh sách chờ của lớp | AC-E-GroupClass | class | Có | Có state machine ST-01. Tạm: UC-009 chưa có P07 nên classType, room, trainer, capacity là thuộc tính tạm (Q-03, Q-04, Q-05). Gốc tập hợp của DC-ClassBooking, DC-Waitlist (R-17, R-18): nạp đủ khi IF-14.findByIdForUpdate; lịch lớp lấy từ IF-14.findSchedule trả DC-ClassInfo, không nạp chỗ đã đặt của khoảng 100 lớp mỗi ngày (Thiết kế: NFR-01, 25 lớp mỗi ngày mỗi chi nhánh, 4 chi nhánh). Số operation public 11, thuộc tính 9 |
| DC-ClassBooking | ClassBooking | «entity» | PKG-29 | Ghi nhận chỗ một hội viên đã đặt trong một lớp nhóm | AC-E-ClassBooking | class | Có | Entity mỏng, giữ vì P10 F3 đã ánh xạ và UC-011, UC-012, UC-016 sẽ bổ sung hành vi (huỷ, chuyển, vắng mặt). Do GroupClass tạo (R-17), không giữ tham chiếu ngược tới lớp; định danh sinh khi lưu |
| DC-Waitlist | Waitlist | «entity» | PKG-29 | Giữ danh sách có thứ tự các hội viên chờ nhận chỗ của một lớp nhóm đã đủ chỗ | AC-E-Waitlist | class | Có | Thiết kế một đối tượng cho mỗi lớp, tạo khi có hội viên đầu tiên vào chờ (Q-84 chưa chốt đối tượng riêng hay chỉ là tập mục chờ; thiết kế theo phương án đối tượng riêng tạo muộn vì ghép được với cả hai câu trả lời của Q-84 khi P13 ánh xạ). Quy tắc thứ tự chờ chờ Q-61. Mỗi mục chờ là DC-WaitlistEntry, từ association class (hội viên, danh sách), định danh bởi Waitlist + Member |
| DC-MemberBookingQuota | MemberBookingQuota | «service» | PKG-29 | Kiểm tra số chỗ một hội viên đã đặt trong một ngày so với mức tối đa của BR-08 | AC-E-Member (tách từ AC-E-Member theo P10 F3, trách nhiệm checkDailyBookingLimit) | class | Không | Dịch vụ miền ở Domain: đếm ClassBooking qua IF-14 cùng package. Không đặt ở DC-Member vì PKG-26 không được phụ thuộc PKG-29 (P09 F6 V7) |
| IF-14 | IGroupClassRepository | «interface» | PKG-29 | Định nghĩa việc nạp và lưu lớp nhóm cùng chỗ đã đặt, danh sách chờ trong giao dịch khoá dòng lớp | P10 cơ chế Persistence | interface | Không | Hiện thực bởi DC-GroupClassRepositoryImpl (PKG-20, ngoài phạm vi lần chạy này). Có operation mở giao dịch vì control là ranh giới giao dịch (1.4) mà Application không được phụ thuộc PKG-20 (P09 F5) |
| IF-16 | IClock | «interface» | PKG-32 (vị trí chờ P10) | Cung cấp thời điểm hiện tại cho lớp dịch vụ để kiểm thử được các mốc thời gian | Thiết kế: lớp control nhận đồng hồ qua constructor (Bước 2.6); TypeScript, Node.js không có kiểu đồng hồ chuẩn như java.time.Clock nên cấp IF mới, số nối tiếp IF-15 của P10 | interface | Không | Dùng chung cho mọi lớp dịch vụ cần thời điểm hiện tại (PKG-14, PKG-15, PKG-16). Entity nhận thời điểm qua tham số, không dùng IF-16. Đề xuất sửa P10 bên dưới |

F1b. Kiểu phụ trợ

| DC | Loại | PKG | Thành phần hoặc giá trị | Dùng trong chữ ký (DC.operation, IF.operation) |
|---|---|---|---|---|
| DC-ClassInfo | value object | PKG-29 | classId: string; classType: string; room: string; trainer: string; startTime: Date | DC-GroupClass.provideClassInfo, DC-GroupClass.reserveSpot, IF-14.findSchedule, DC-BookClassSpotHandler.getClassSchedule, DC-BookClassResult, DC-WaitlistPlacement, DC-CancelUnderBookedClassHandler.notifyBookedMembers, composeClassCancelledNotice |
| DC-WaitlistEntry | value object | PKG-29 | member: DC-Member; joinedAt: Date | DC-Waitlist.compareWaitOrder; thuộc tính DC-Waitlist.entries |
| DC-WaitlistPlacement | value object | PKG-15 | classInfo: DC-ClassInfo; position: number (số nguyên dương, 1 là đứng đầu) | DC-BookClassSpotHandler.joinWaitlist |
| DC-BookClassResult | value object | PKG-15 | outcome: DC-BookingOutcome; classInfo: DC-ClassInfo hoặc null (chỉ có khi outcome là BOOKED) | DC-BookClassSpotHandler.bookClass |
| DC-GroupClassStatus | enumeration | PKG-29 | SCHEDULED, CANCELLED | DC-GroupClass.getStatus; thuộc tính DC-GroupClass.status (ST-01) |
| DC-Bookability | enumeration | PKG-29 | BOOKABLE, CLASS_CANCELLED, OUTSIDE_BOOKING_WINDOW | DC-GroupClass.assessBookability |
| DC-CancellationCheck | enumeration | PKG-29 | CANCELLABLE, ALREADY_CANCELLED (luồng 2a), ENOUGH_BOOKINGS (luồng 2b) | DC-GroupClass.assessCancellation |
| DC-BookingOutcome | enumeration | PKG-15 | BOOKED, MEMBER_SUSPENDED (4a), CLASS_CANCELLED (5a), OUTSIDE_BOOKING_WINDOW (5b), DAILY_LIMIT_REACHED (6a), CLASS_FULL (7a1) | DC-BookClassResult; DC-BookClassSpotHandler.bookClass. Tách khỏi DC-Bookability vì entity ở Domain không được phụ thuộc kiểu của Application |
| DC-GroupClassNotFoundException | exception | PKG-29 | Mã lớp không có trong kho dữ liệu | DC-BookClassSpotHandler.bookClass, joinWaitlist |
| DC-SpotUnavailableException | exception | PKG-29 | Lớp đã đủ chỗ tại lúc lưu chỗ đã đặt (BR-11) | DC-GroupClass.reserveSpot |
| DC-InvalidClassStateException | exception | PKG-29 | Thao tác không hợp lệ ở trạng thái hiện tại của lớp (ST-01) | DC-GroupClass.reserveSpot, addToWaitlist, cancelClass |
| DC-WaitlistNotAllowedException | exception | PKG-29 | Lớp chưa đủ chỗ nên không nhận vào danh sách chờ; kết cục nghiệp vụ chờ Q-106 | DC-GroupClass.addToWaitlist, DC-BookClassSpotHandler.joinWaitlist |

## F2. Bảng operation

Bảng ánh xạ kiểu (một lần): Boolean --> boolean; Integer, Số lượng --> number (số nguyên); String --> string; Date, Ngày, Giờ --> Date; định danh --> string (Thiết kế: chuỗi UUID, cùng kiểu với subjectRef: string của IF-06, IF-10); danh sách trả về --> ReadonlyArray của kiểu phần tử; operation chạm CSDL hoặc I/O trả kết quả T --> Promise của T; void của operation chạm CSDL hoặc I/O (IF-06.scheduleMark, IF-06.cancelMark, IF-10.handleMarkDue) --> Promise của void. Operation không trả về ghi ": void". Constructor của lớp dịch vụ nhận phụ thuộc tiêm (quan hệ R-29 đến R-39) không lập dòng riêng; constructor của entity có dòng.

| DC | Visibility | Chữ ký | Mô tả | Tiền/hậu điều kiện | Nguồn (message P07 / UC bước) | Phạm vi | Ngoại lệ / lỗi |
|---|---|---|---|---|---|---|---|
| DC-BookClassSpotHandler | + | getClassSchedule(): Promise<ReadonlyArray<ClassInfo>> | Trả về lịch lớp nhóm để hội viên chọn lớp, mỗi phần tử là DC-ClassInfo (mã lớp, loại lớp, phòng, huấn luyện viên, giờ học). Phạm vi các lớp trong lịch chờ Q-83 | Tiền: hội viên đã xác thực (UC-010). Hậu: không đổi dữ liệu | P07 UC-010 msg 1.1 startBooking, 1.1.1 provideClassInfo, 1.1.2 showClassSchedule; bước 2 | Instance | - |
| DC-BookClassSpotHandler | + | bookClass(memberId: string, classId: string): Promise<BookClassResult> | Đặt chỗ lớp nhóm cho hội viên, kiểm tra lần lượt quyền đặt lớp (BR-09), lớp chưa huỷ và thời hạn đặt chỗ (BR-06, BR-07), số lớp trong ngày (BR-08), chỗ trống (BR-10, BR-11), rồi lưu chỗ đã đặt. Mọi kết cục thất bại nghiệp vụ trả về trong outcome của DC-BookClassResult, không ném ngoại lệ. classInfo chỉ có khi outcome là BOOKED | Tiền: hội viên đã xác thực. Hậu thành công (BOOKED): lớp có thêm đúng một chỗ đã đặt của hội viên, số chỗ đã đặt không vượt sức chứa (BR-11). Hậu thất bại: chỗ đã đặt và danh sách chờ không đổi | P07 UC-010 msg 2.1 bookClass; 2.1.2, 2.1.4, 2.1.5, 2.1.7, 2.1.9, 2.1.11 (kiểu trả về); bước 3 đến 9 | Instance | DC-GroupClassNotFoundException (classId không có); MemberNotFoundException (PKG-26, xem F4b) |
| DC-BookClassSpotHandler | + | joinWaitlist(memberId: string, classId: string): Promise<WaitlistPlacement> | Thêm hội viên vào danh sách chờ của lớp đã đủ chỗ, trả về loại lớp, giờ học và vị trí trong danh sách chờ (Dữ liệu ra 3) | Tiền: lớp đã đủ chỗ và chưa huỷ; nếu lớp đổi trạng thái giữa 7a1 và 7a3 thì Q-106. Hậu: danh sách chờ của lớp có hội viên | P07 UC-010 msg 3.1 joinWaitlist; 3.1.2 showWaitlistPosition (kiểu trả về); bước 7a2 đến 7a4 | Instance | DC-GroupClassNotFoundException; MemberNotFoundException; DC-WaitlistNotAllowedException (Q-106) |
| DC-CancelUnderBookedClassHandler | + | handleMarkDue(kind: MarkKind, subjectRef: string, dueAt: Date): Promise<void> | Hiện thực IF-10: xử lý mốc ClassCutoff của lớp có mã subjectRef, huỷ lớp khi lớp chưa huỷ và có dưới 3 người đặt chỗ (BR-13), huỷ hai mốc còn chờ của lớp, rồi chuyển yêu cầu gửi thông báo lớp bị huỷ cho từng hội viên đã đặt chỗ (BR-14). Xử lý lặp lại được: mốc giao lại khi lớp đã huỷ thì kết thúc, không đổi dữ liệu | Tiền: SS-06 đã giữ quyền xử lý mốc (P11b IF-10). Hậu thành công: lớp ở trạng thái CANCELLED, mốc AbsenceCheck và WaitlistTransfer của lớp không còn chờ (Q-64), mỗi hội viên đã đặt chỗ có yêu cầu gửi trong hàng chờ gửi nền. Hậu luồng 2a, 2b, 5a: không đổi dữ liệu | P11b IF-10.handleMarkDue; P07 UC-015 msg 1 handleClassCutoff; bước 1 đến 7 | Instance | Lỗi lan ra cho SS-06 coi là MarkHandlingFailed (Q-102); Error khi kind khác ClassCutoff |
| DC-CancelUnderBookedClassHandler | + | onModuleInit(): void | Đăng ký chính nó làm bộ nhận mốc ClassCutoff với IF-06 khi tiến trình nền khởi động | Tiền: IF-06 chưa start. Hậu: mốc ClassCutoff đến hạn được chuyển cho handleMarkDue | Bổ sung: P11b IF-06.registerMarkHandler | Instance | - |
| DC-CancelUnderBookedClassHandler | - | cancelAbsenceMark(classId: string): Promise<void> | Huỷ mốc tính vắng mặt của UC-016 gắn với lớp bằng IF-06.cancelMark(AbsenceCheck, classId) | Hậu: không còn mốc AbsenceCheck chờ của lớp; huỷ mốc không tồn tại không lỗi (P11b IF-06) | P07 UC-015 msg 1.3 cancelAbsenceMark; bước 4 | Instance | MarkStoreUnavailable (PKG-22; kết cục chờ Q-102) |
| DC-CancelUnderBookedClassHandler | - | cancelWaitlistTransferMark(classId: string): Promise<void> | Huỷ mốc chuyển chỗ của UC-013 gắn với lớp bằng IF-06.cancelMark(WaitlistTransfer, classId). Khoá mốc theo mã lớp là theo P11b F1; cách khoá thực của UC-013 chờ Q-107 | Hậu: không còn mốc WaitlistTransfer chờ của lớp | P07 UC-015 msg 1.4 cancelWaitlistTransferMark; bước 4; Q-64 | Instance | MarkStoreUnavailable (Q-102) |
| DC-CancelUnderBookedClassHandler | - | notifyBookedMembers(members: ReadonlyArray<Member>, info: ClassInfo): Promise<void> | Với từng hội viên: hỏi kênh nhận thông báo (BR-14), rồi chuyển yêu cầu gửi thông báo đẩy qua IF-03 hoặc SMS qua IF-04 với nội dung do composeClassCancelledNotice soạn. Hội viên bị từ chối đầu vào (InvalidNotificationContent, InvalidPhoneNumber) được ghi nhật ký và bỏ qua, không chặn hội viên khác (kết cục chờ Q-65) | Tiền: lớp đã CANCELLED và giao dịch đã commit. Hậu: mỗi hội viên có yêu cầu gửi trong hàng chờ gửi nền của SS-03 hoặc SS-04, trừ hội viên bị từ chối đầu vào | P07 UC-015 msg 1.7 determineNotificationChannel, 1.8 sendPushNotification, 1.9 sendSms; bước 6, 7 | Instance | - |
| DC-CancelUnderBookedClassHandler | - | composeClassCancelledNotice(info: ClassInfo): NotificationContent | Soạn thông báo lớp bị huỷ từ loại lớp và giờ học (Dữ liệu ra 1). Câu chữ và nội dung khác của thông báo chờ Q-66 | Hậu: nội dung không rỗng | Bổ sung: P07 UC-015 msg 1.8, 1.9 (nội dung thông báo); Dữ liệu ra 1 | Instance | - |
| DC-GroupClass | + | GroupClass(id: string, classType: string, room: string, trainer: string, startTime: Date, capacity: number) | Khởi tạo lớp ở trạng thái SCHEDULED, chưa có chỗ đã đặt và danh sách chờ | Tiền: capacity >= 0. Hậu: status = SCHEDULED (ST-01 chuyển từ initial) | Bổ sung: khởi tạo; ST-01 sự kiện create; UC-009 chưa có P07 | Classifier | - |
| DC-GroupClass | + | provideClassInfo(): ClassInfo | Trả về loại lớp, phòng, huấn luyện viên, giờ học của lớp kèm mã lớp | Hậu: không đổi dữ liệu | P07 UC-010 msg 1.1.1 provideClassInfo, 2.1.10 (trả về); UC-015 msg 1.6 provideCancelledClassInfo | Instance | - |
| DC-GroupClass | + | assessBookability(now: Date): Bookability | Đánh giá lớp có đặt chỗ được tại thời điểm now: CLASS_CANCELLED khi lớp đã huỷ, OUTSIDE_BOOKING_WINDOW khi now ngoài thời hạn đặt chỗ tính từ giờ học, ngược lại BOOKABLE | Tiền: không. Quy tắc thời hạn đặt chỗ chưa chốt vì BR-06 mâu thuẫn BR-07 (Q-11), mốc muộn nhất chờ Q-58. Hậu: không đổi dữ liệu | P07 UC-010 msg 2.1.3 checkBookable; bước 5 | Instance | - |
| DC-GroupClass | + | hasAvailableSpot(): boolean | Cho biết số chỗ đã đặt còn dưới sức chứa (BR-10, BR-11). Chỗ giữ riêng cho người trong danh sách chờ chưa được tính (Q-22) | Hậu: không đổi dữ liệu | P07 UC-010 msg 2.1.8 checkSpotAvailable; bước 7 | Instance | - |
| DC-GroupClass | + | reserveSpot(member: Member): ClassInfo | Tạo chỗ đã đặt cho hội viên và trả về DC-ClassInfo của lớp (Dữ liệu ra 2) | Tiền: status SCHEDULED, số chỗ đã đặt nhỏ hơn sức chứa tại lúc gọi (BR-11). Hậu: getBookedCount tăng 1, lớp có thêm một chỗ đã đặt của hội viên | P07 UC-010 msg 2.1.10 reserveSpot, 2.1.10.1 initializeBooking; bước 8 | Instance | DC-SpotUnavailableException (đã đủ chỗ tại lúc lưu); DC-InvalidClassStateException (lớp CANCELLED) |
| DC-GroupClass | + | addToWaitlist(member: Member, now: Date): number | Thêm hội viên vào danh sách chờ của lớp (tạo DC-Waitlist khi chưa có, Q-84) và trả về vị trí của hội viên, 1 là đứng đầu | Tiền: status SCHEDULED, lớp đã đủ chỗ (số chỗ đã đặt bằng sức chứa, BR-12). Hậu: danh sách chờ chứa hội viên | P07 UC-010 msg 3.1.1 addToWaitlist; bước 7a3 | Instance | DC-WaitlistNotAllowedException (lớp chưa đủ chỗ, Q-106); DC-InvalidClassStateException (lớp CANCELLED) |
| DC-GroupClass | + | assessCancellation(): CancellationCheck | Đánh giá lớp có huỷ được theo BR-13: ALREADY_CANCELLED khi lớp đã huỷ, ENOUGH_BOOKINGS khi số người đặt chỗ từ 3 trở lên, ngược lại CANCELLABLE | Hậu: không đổi dữ liệu. Cách đếm khi một hội viên giữ nhiều chỗ chờ Q-59; chỗ giữ riêng và chỗ của hội viên bị khoá chờ Q-22, Q-20 | P07 UC-015 msg 1.1 checkUnderBookedCancellable; bước 2, 2a, 2b | Instance | - |
| DC-GroupClass | + | cancelClass(): void | Chuyển lớp sang trạng thái đã huỷ | Tiền: status SCHEDULED. Hậu: status CANCELLED; chỗ đã đặt và danh sách chờ không đổi (Q-63) | P07 UC-015 msg 1.2 cancelClass; ST-01 sự kiện cancelClass | Instance | DC-InvalidClassStateException (đã CANCELLED) |
| DC-GroupClass | + | collectBookedMembers(): ReadonlyArray<Member> | Trả về các hội viên có chỗ đã đặt trong lớp, mỗi hội viên một lần | Hậu: không đổi dữ liệu | P07 UC-015 msg 1.5 collectBookedMembers, 1.5.1 provideBookedMember; bước 5 | Instance | - |
| DC-GroupClass | + | getStatus(): GroupClassStatus | Trả về trạng thái của lớp | Hậu: không đổi | Bổ sung: quan sát hậu điều kiện của cancelClass | Instance | - |
| DC-GroupClass | + | getBookedCount(): number | Trả về số chỗ đã đặt của lớp | Hậu: không đổi | Bổ sung: quan sát hậu điều kiện của reserveSpot | Instance | - |
| DC-ClassBooking | ~ | ClassBooking(member: Member) | Khởi tạo chỗ đã đặt của hội viên; chỉ DC-GroupClass tạo | Tiền: member không rỗng. Hậu: provideBookedMember trả member | P07 UC-010 msg 2.1.10.1 initializeBooking | Classifier | - |
| DC-ClassBooking | + | provideBookedMember(): Member | Trả về hội viên đã đặt chỗ này | Hậu: không đổi | P07 UC-015 msg 1.5.1 provideBookedMember | Instance | - |
| DC-Waitlist | ~ | Waitlist() | Khởi tạo danh sách chờ rỗng | Hậu: entries rỗng | Bổ sung: khởi tạo | Classifier | - |
| DC-Waitlist | + | addMember(member: Member, now: Date): number | Thêm mục chờ của hội viên với thời điểm vào now và trả về vị trí của hội viên theo thứ tự xếp chờ, 1 là đứng đầu | Hậu: contains(member) là true. Thứ tự xếp chờ chờ Q-61; hội viên đã có trong danh sách chờ Q-59 | P07 UC-010 msg 3.1.1.1 addMember; bước 7a3 | Instance | - |
| DC-Waitlist | - | compareWaitOrder(a: WaitlistEntry, b: WaitlistEntry): number | So sánh thứ tự xếp chờ của hai mục chờ, là chỗ duy nhất chứa quy tắc thứ tự để đổi theo câu trả lời Q-61 | Thân hàm chờ Q-61 | Bổ sung: quy tắc thứ tự xếp chờ (Q-61) | Instance | - |
| DC-Waitlist | + | contains(member: Member): boolean | Cho biết hội viên có trong danh sách chờ | Hậu: không đổi | Bổ sung: quan sát hậu điều kiện của addMember | Instance | - |
| DC-MemberBookingQuota | + | hasReachedDailyLimit(memberId: string, classStartTime: Date): Promise<boolean> | Cho biết hội viên đã có đủ số chỗ đã đặt tối đa trong ngày diễn ra lớp mới, tức số chỗ đã đặt thuộc lớp diễn ra cùng ngày với classStartTime đã đạt MAX_BOOKINGS_PER_DAY (BR-08) | Hậu: không đổi dữ liệu. Cách tính ngày và việc có tính lớp trong danh sách chờ chờ Q-60; chỗ đã đặt của lớp đã huỷ được đếm chờ Q-63 | P07 UC-010 msg 2.1.6 checkDailyBookingLimit (Khác lớp nhận: P10 F3); bước 6 | Instance | - |
| IF-14 | + | findSchedule(): Promise<ReadonlyArray<ClassInfo>> | Trả về thông tin các lớp trong lịch lớp nhóm, không nạp chỗ đã đặt. Phạm vi lịch chờ Q-83 | Hậu: không đổi dữ liệu | P10 F2 IF-14; P07 UC-010 msg 1.1.1 (Khác lớp nhận, xem F4) | Instance | - |
| IF-14 | + | findByIdForUpdate(classId: string): Promise<GroupClass \| null> | Nạp lớp cùng chỗ đã đặt (kèm hội viên) và danh sách chờ, khoá dòng của lớp đến hết giao dịch hiện hành; trả null khi không có lớp | Tiền: đang trong runInTransaction. Hậu: dòng lớp bị khoá (BR-11) | P10 F2 IF-14; P09 F7 chiến lược giao dịch | Instance | - |
| IF-14 | + | save(groupClass: GroupClass): Promise<void> | Lưu thay đổi của lớp: trạng thái, chỗ đã đặt mới, mục chờ mới; gán định danh cho đối tượng mới | Tiền: đang trong runInTransaction. Hậu: thay đổi nằm trong giao dịch hiện hành | P10 F2 IF-14 | Instance | - |
| IF-14 | + | countMemberBookingsBetween(memberId: string, from: Date, toExclusive: Date): Promise<number> | Đếm chỗ đã đặt của hội viên thuộc lớp có giờ học trong khoảng từ from tới trước toExclusive | Hậu: không đổi dữ liệu | P10 F2 IF-14; P07 UC-010 msg 2.1.6 | Instance | - |
| IF-14 | + | runInTransaction<T>(work: () => Promise<T>): Promise<T> | Chạy work trong một giao dịch CSDL: mọi repository gọi trong work dùng chung giao dịch, work ném lỗi thì hoàn tác, ngược lại commit | Tiền: không lồng nhau. Hậu: giao dịch đã commit hoặc đã hoàn tác (Thiết kế: ngữ cảnh giao dịch theo luồng bất đồng bộ, hiện thực ở PKG-20) | P09 F7 chiến lược giao dịch; Bổ sung: control là ranh giới giao dịch | Instance | - |
| IF-16 | + | now(): Date | Trả về thời điểm hiện tại | Hậu: không đổi | Bổ sung: Bước 2.6 (đồng hồ qua constructor) | Instance | - |

Chữ ký interface tạm (Bước 0): interface dùng trong phạm vi mà P11b không phủ và P12 của package chứa interface chưa chạy.

| IF | Operation | Lý do | Message P07 nguồn |
|---|---|---|---|
| IF-11 IAccountRepository | findById(memberId: string): Promise<Member \| null> | P11b không phủ IF-11 (kho dữ liệu do P12 thiết kế, P10 F2); PKG-26 chưa có file P12 | P07 UC-010 msg 2.1.1 checkBookingNotSuspended (cần nạp hội viên); UC-015 msg 1.7 (hội viên nạp cùng chỗ đã đặt) |

Đề xuất sửa artifact trước: chạy P12 cho PKG-26 rồi đối chiếu chữ ký ở bảng này và F4b. Khi có, chạy lại P12 cho phạm vi này nếu chữ ký khác.

## F3. Bảng thiết kế method

| DC.operation | Thuật toán / các bước chính | Đối tượng và operation khác được dùng | Cách dùng thuộc tính, tham số, quan hệ | Hành vi theo trạng thái (nếu có ST) |
|---|---|---|---|---|
| DC-BookClassSpotHandler.bookClass(String, String) | 1. now = IClock.now(). 2. Mở giao dịch bằng IF-14.runInTransaction, trong đó: 3. nạp hội viên bằng IF-11.findById, null thì ném MemberNotFoundException; nếu hội viên đang bị khoá quyền đặt lớp thì trả MEMBER_SUSPENDED (4a). 4. Nạp lớp bằng IF-14.findByIdForUpdate (khoá dòng lớp), null thì ném DC-GroupClassNotFoundException. 5. assessBookability(now): CLASS_CANCELLED --> trả CLASS_CANCELLED (5a), OUTSIDE_BOOKING_WINDOW --> trả OUTSIDE_BOOKING_WINDOW (5b). 6. Nếu MemberBookingQuota.hasReachedDailyLimit(memberId, startTime của lớp) thì trả DAILY_LIMIT_REACHED (6a). 7. Nếu không hasAvailableSpot() thì trả CLASS_FULL (7a1). 8. reserveSpot(member); bắt DC-SpotUnavailableException thì trả CLASS_FULL (khớp P04 mục 8: người đến sau đi theo luồng 7a). 9. IF-14.save(lớp). 10. Trả BOOKED kèm DC-ClassInfo | IClock.now, IF-11.findById, Member (kiểm tra khoá quyền đặt lớp, xem F4b), IF-14.findByIdForUpdate, save, runInTransaction, DC-GroupClass.assessBookability, hasAvailableSpot, reserveSpot, provideClassInfo, DC-MemberBookingQuota.hasReachedDailyLimit | Ranh giới giao dịch bao trọn bước 2 đến 9; khoá dòng lớp giữ từ bước 4 đến hết giao dịch nên bước 7 và 8 không có khe hở với yêu cầu đồng thời (BR-11). Thứ tự kiểm tra là thứ tự trình bày của P04 mục 8 | Lớp CANCELLED thì dừng ở bước 5. Hội viên đặt đúng lúc mốc huỷ: giao dịch của handleMarkDue và bookClass cùng khoá dòng lớp nên xếp hàng |
| DC-BookClassSpotHandler.joinWaitlist(String, String) | 1. now = IClock.now(). 2. Trong IF-14.runInTransaction: nạp hội viên (IF-11.findById) và lớp (IF-14.findByIdForUpdate), null thì ném ngoại lệ tương ứng. 3. position = lớp.addToWaitlist(member, now). 4. IF-14.save(lớp). 5. Trả DC-WaitlistPlacement(lớp.provideClassInfo(), position) | IClock, IF-11, IF-14, DC-GroupClass.addToWaitlist, provideClassInfo | Khoá dòng lớp để hai hội viên cùng vào chờ nhận hai vị trí khác nhau | Lớp CANCELLED hoặc chưa đủ chỗ: ngoại lệ từ addToWaitlist, kết cục nghiệp vụ chờ Q-106 |
| DC-CancelUnderBookedClassHandler.handleMarkDue(MarkKind, String, Date) | 1. kind khác ClassCutoff thì ném Error. 2. Trong IF-14.runInTransaction: nạp lớp bằng findByIdForUpdate(subjectRef); null thì ghi nhật ký rồi kết thúc (mốc gắn lớp không còn). 3. assessCancellation(): ALREADY_CANCELLED hoặc ENOUGH_BOOKINGS thì kết thúc (2a, 2b), không lưu gì. 4. cancelClass(), IF-14.save(lớp). 5. cancelAbsenceMark(subjectRef), cancelWaitlistTransferMark(subjectRef). 6. members = collectBookedMembers(), info = provideClassInfo(); trả cặp (info, members) khi commit. 7. Ngoài giao dịch: members rỗng thì kết thúc (5a). 8. notifyBookedMembers(members, info) | IF-14, DC-GroupClass.assessCancellation, cancelClass, collectBookedMembers, provideClassInfo, IF-06.cancelMark (qua hai operation private), notifyBookedMembers | Ranh giới giao dịch bao trọn bước 2 đến 6 (huỷ lớp và huỷ mốc cùng commit); gửi thông báo sau commit để không báo cho lớp chưa huỷ. dueAt chỉ ghi nhật ký | Lớp đã CANCELLED khi mốc đến: nhánh 2a, không gửi lại thông báo; hệ quả khi mốc giao lại sau khi đã huỷ mà chưa gửi hết thông báo ghi ở Vấn đề còn mở (Q-85) |
| DC-CancelUnderBookedClassHandler.notifyBookedMembers(ReadonlyArray<Member>, ClassInfo) | 1. content = composeClassCancelledNotice(info). 2. Với mỗi hội viên: channel = member.determineNotificationChannel(). 3. Kênh thông báo đẩy --> IF-03.sendPushNotification(member, content). 4. Kênh SMS --> IF-04.sendSms(member.getPhoneNumber(), content). 5. Bắt InvalidNotificationContent, InvalidPhoneNumber: ghi nhật ký mã hội viên rồi sang hội viên kế tiếp | IF-03, IF-04, Member, composeClassCancelledNotice | Lặp trong control vì entity không gọi boundary (P07 F4) | - |
| DC-GroupClass.reserveSpot(Member) | 1. status CANCELLED thì ném DC-InvalidClassStateException. 2. getBookedCount() >= capacity thì ném DC-SpotUnavailableException. 3. Tạo ClassBooking(member) và thêm vào bookings. 4. Trả provideClassInfo() | DC-ClassBooking | bookings (R-17), capacity | Chỉ nhận ở SCHEDULED (ST-01) |
| DC-GroupClass.assessBookability(Date) | 1. status CANCELLED thì trả CLASS_CANCELLED. 2. Nếu now ngoài thời hạn đặt chỗ tính từ startTime thì trả OUTSIDE_BOOKING_WINDOW: bước này chưa đặc tả được vì BR-06 (sớm nhất 7 ngày trước giờ học) mâu thuẫn BR-07 (tuần mới mở lúc 6 giờ sáng thứ Hai) và mốc muộn nhất chờ Q-58. 3. Trả BOOKABLE | - | startTime, status, now | Lớp CANCELLED trả ngay |
| DC-GroupClass.addToWaitlist(Member, Date) | 1. status CANCELLED thì ném DC-InvalidClassStateException. 2. Chưa đủ chỗ (getBookedCount() < capacity) thì ném DC-WaitlistNotAllowedException. 3. waitlist rỗng thì tạo DC-Waitlist mới (Q-84). 4. Trả waitlist.addMember(member, now) | DC-Waitlist | waitlist (R-18) | Chỉ nhận ở SCHEDULED khi đã đủ chỗ (ST-01) |
| DC-GroupClass.assessCancellation() | 1. status CANCELLED thì trả ALREADY_CANCELLED. 2. Số người đặt chỗ = getBookedCount() (cách đếm: Q-59, Q-22, Q-20). 3. Nhỏ hơn UNDER_BOOKED_THRESHOLD thì trả CANCELLABLE, ngược lại ENOUGH_BOOKINGS | - | bookings, UNDER_BOOKED_THRESHOLD (BR-13) | Trả ngay ở CANCELLED |
| DC-GroupClass.collectBookedMembers() | 1. Với mỗi ClassBooking trong bookings gọi provideBookedMember(). 2. Loại trùng theo getId() của hội viên để mỗi hội viên được báo một lần (P04 bước 7: mọi hội viên đã đặt chỗ; hội viên giữ nhiều chỗ chờ Q-59). 3. Trả danh sách | DC-ClassBooking.provideBookedMember, Member.getId (F4b) | bookings | - |
| DC-Waitlist.addMember(Member, Date) | 1. Tạo DC-WaitlistEntry(member, now) và thêm vào entries. 2. Sắp lại entries bằng compareWaitOrder (Q-61). 3. Trả chỉ số của mục vừa thêm cộng 1 | DC-WaitlistEntry, compareWaitOrder | entries, now | - |
| DC-MemberBookingQuota.hasReachedDailyLimit(String, Date) | 1. from = 00:00 của ngày chứa classStartTime theo múi giờ của máy chủ ứng dụng; toExclusive = from cộng 1 ngày (Thiết kế: một múi giờ cấu hình cho cả chuỗi; cách tính ngày chờ Q-60). 2. n = IF-14.countMemberBookingsBetween(memberId, from, toExclusive). 3. Trả n >= MAX_BOOKINGS_PER_DAY | IF-14.countMemberBookingsBetween | MAX_BOOKINGS_PER_DAY (BR-08) | - |

## F4. Bảng ánh xạ message --> operation

| UC | STT message (P07) | Từ (AC/DC) | Đến (AC/DC) | Message phân tích (// tênTráchNhiệm) | Operation thiết kế (chữ ký đầy đủ) |
|---|---|---|---|---|---|
| UC-010 | 1.1 | AC-B-BookClassSpotUI (qua DC-BookClassSpotController) | AC-C-BookClassSpotHandler | // startBooking | DC-BookClassSpotHandler.getClassSchedule(): Promise<ReadonlyArray<ClassInfo>> |
| UC-010 | 1.1.1 | AC-C-BookClassSpotHandler | AC-E-GroupClass | // provideClassInfo (lặp mỗi lớp trong lịch) | Khác lớp nhận: IF-14.findSchedule(): Promise<ReadonlyArray<ClassInfo>> (Thiết kế: lịch lấy thẳng thông tin lớp từ kho dữ liệu, không nạp chỗ đã đặt của khoảng 100 lớp mỗi ngày, NFR-01); DC-GroupClass.provideClassInfo(): ClassInfo vẫn dùng cho msg 2.1.10 và UC-015 msg 1.6 |
| UC-010 | 1.1.2 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showClassSchedule | Trả về: DC-BookClassSpotHandler.getClassSchedule trả ReadonlyArray<ClassInfo> |
| UC-010 | 2.1 | AC-B-BookClassSpotUI (qua DC-BookClassSpotController) | AC-C-BookClassSpotHandler | // bookClass | DC-BookClassSpotHandler.bookClass(memberId: string, classId: string): Promise<BookClassResult> |
| UC-010 | 2.1.2 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showBookingRejectedNotice (khoá quyền đặt lớp, BR-09) | Trả về: DC-BookClassSpotHandler.bookClass trả DC-BookClassResult có outcome MEMBER_SUSPENDED |
| UC-010 | 2.1.3 | AC-C-BookClassSpotHandler | AC-E-GroupClass | // checkBookable | DC-GroupClass.assessBookability(now: Date): Bookability |
| UC-010 | 2.1.4 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showBookingRejectedNotice (lớp đã huỷ) | Trả về: bookClass trả outcome CLASS_CANCELLED |
| UC-010 | 2.1.5 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showBookingRejectedNotice (ngoài thời hạn đặt chỗ, BR-06, BR-07) | Trả về: bookClass trả outcome OUTSIDE_BOOKING_WINDOW |
| UC-010 | 2.1.6 | AC-C-BookClassSpotHandler | AC-E-Member | // checkDailyBookingLimit | Khác lớp nhận: P10 F3 AC-E-Member --> DC-MemberBookingQuota.hasReachedDailyLimit(memberId: string, classStartTime: Date): Promise<boolean> |
| UC-010 | 2.1.7 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showBookingRejectedNotice (đủ số lớp trong ngày, BR-08) | Trả về: bookClass trả outcome DAILY_LIMIT_REACHED |
| UC-010 | 2.1.8 | AC-C-BookClassSpotHandler | AC-E-GroupClass | // checkSpotAvailable | DC-GroupClass.hasAvailableSpot(): boolean |
| UC-010 | 2.1.9 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showClassFullNotice | Trả về: bookClass trả outcome CLASS_FULL |
| UC-010 | 3.1 | AC-B-BookClassSpotUI (qua DC-BookClassSpotController) | AC-C-BookClassSpotHandler | // joinWaitlist | DC-BookClassSpotHandler.joinWaitlist(memberId: string, classId: string): Promise<WaitlistPlacement> |
| UC-010 | 3.1.1 | AC-C-BookClassSpotHandler | AC-E-GroupClass | // addToWaitlist (hội viên) | DC-GroupClass.addToWaitlist(member: Member, now: Date): number |
| UC-010 | 3.1.1.1 | AC-E-GroupClass | AC-E-Waitlist | // addMember (hội viên) | DC-Waitlist.addMember(member: Member, now: Date): number |
| UC-010 | 3.1.2 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showWaitlistPosition | Trả về: DC-BookClassSpotHandler.joinWaitlist trả DC-WaitlistPlacement |
| UC-010 | 2.1.10 | AC-C-BookClassSpotHandler | AC-E-GroupClass | // reserveSpot (hội viên) | DC-GroupClass.reserveSpot(member: Member): ClassInfo |
| UC-010 | 2.1.10.1 | AC-E-GroupClass | AC-E-ClassBooking | // initializeBooking (hội viên, lớp nhóm), «create» | DC-ClassBooking «create» ClassBooking(member: Member). Khác tham số: lớp nhóm là chủ sở hữu qua R-17, ClassBooking không giữ tham chiếu ngược nên không nhận lớp |
| UC-010 | 2.1.11 | AC-C-BookClassSpotHandler | AC-B-BookClassSpotUI | // showBookedSpot | Trả về: bookClass trả outcome BOOKED kèm classInfo |
| UC-015 | 1 | ACT-14 (qua SS-06) | AC-C-CancelUnderBookedClassHandler | // handleClassCutoff | Khác lớp nhận: P11b SS-06 IF-10.handleMarkDue --> DC-CancelUnderBookedClassHandler.handleMarkDue(kind: MarkKind, subjectRef: string, dueAt: Date): Promise<void> |
| UC-015 | 1.1 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | // checkUnderBookedCancellable | DC-GroupClass.assessCancellation(): CancellationCheck |
| UC-015 | 1.2 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | // cancelClass | DC-GroupClass.cancelClass(): void |
| UC-015 | 1.3 | AC-C-CancelUnderBookedClassHandler | AC-C-CancelUnderBookedClassHandler (tự gọi) | // cancelAbsenceMark | DC-CancelUnderBookedClassHandler.cancelAbsenceMark(classId: string): Promise<void>, gọi IF-06.cancelMark(MarkKind.AbsenceCheck, classId) theo P11b IF-06 |
| UC-015 | 1.4 | AC-C-CancelUnderBookedClassHandler | AC-C-CancelUnderBookedClassHandler (tự gọi) | // cancelWaitlistTransferMark | DC-CancelUnderBookedClassHandler.cancelWaitlistTransferMark(classId: string): Promise<void>, gọi IF-06.cancelMark(MarkKind.WaitlistTransfer, classId) |
| UC-015 | 1.5 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | // collectBookedMembers | DC-GroupClass.collectBookedMembers(): ReadonlyArray<Member> |
| UC-015 | 1.5.1 | AC-E-GroupClass | AC-E-ClassBooking | // provideBookedMember | DC-ClassBooking.provideBookedMember(): Member |
| UC-015 | 1.6 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | // provideCancelledClassInfo | DC-GroupClass.provideClassInfo(): ClassInfo (gộp với provideClassInfo của UC-010) |
| UC-015 | 1.7 | AC-C-CancelUnderBookedClassHandler | AC-E-Member | // determineNotificationChannel | Lớp nhận ngoài phạm vi (PKG-26): xem F4b |
| UC-015 | 1.8 | AC-C-CancelUnderBookedClassHandler | AC-B-PushNotificationGateway | // sendPushNotification (hội viên, lớp nhóm bị huỷ) | Khác lớp nhận: P11b SS-03 IF-03.sendPushNotification(recipient: Member, content: NotificationContent): Promise<NotificationReceipt> |
| UC-015 | 1.9 | AC-C-CancelUnderBookedClassHandler | AC-B-SmsGateway | // sendSms (hội viên, lớp nhóm bị huỷ) | Khác lớp nhận: P11b SS-04 IF-04.sendSms(phone: PhoneNumber, content: NotificationContent): Promise<NotificationReceipt> |

F4b. Chữ ký yêu cầu với lớp ngoài phạm vi. Message có lớp gửi trong phạm vi mà lớp nhận thuộc package khác (không phải interface) được để cho lần chạy chứa lớp nhận; bảng này ghi chữ ký mà thiết kế trên đang dùng để lần chạy đó đối chiếu.

| Message P07 | Lớp nhận (PKG) | Chữ ký yêu cầu | Dùng bởi |
|---|---|---|---|
| UC-010 msg 2.1.1 checkBookingNotSuspended | DC-Member (PKG-26) | isBookingSuspended(now: Date): boolean | DC-BookClassSpotHandler.bookClass |
| UC-015 msg 1.7 determineNotificationChannel | DC-Member (PKG-26) | determineNotificationChannel(): NotificationChannel, với NotificationChannel là enumeration có giá trị PUSH, SMS (BR-14, Q-36) | DC-CancelUnderBookedClassHandler.notifyBookedMembers |
| UC-015 msg 1.9 sendSms (số điện thoại) | DC-Member (PKG-26) | getPhoneNumber(): PhoneNumber (P11b SS-04 F3: P12 bổ sung thuộc tính số điện thoại vào DC-Member) | DC-CancelUnderBookedClassHandler.notifyBookedMembers |
| UC-015 msg 1.5 (loại trùng hội viên) | DC-Member (PKG-26) | getId(): string | DC-GroupClass.collectBookedMembers |
| UC-010 msg 2.1.1 | MemberNotFoundException (PKG-26) | Ngoại lệ khi IF-11.findById trả null | DC-BookClassSpotHandler.bookClass, joinWaitlist |
| UC-015 msg 1.8, 1.9 | DC-NotificationContent (PKG-24) | NotificationContent(title: string, body: string); InvalidNotificationContent, InvalidPhoneNumber là ngoại lệ của IF-03, IF-04 (P11b SS-03, SS-04 F5) | DC-CancelUnderBookedClassHandler.composeClassCancelledNotice, notifyBookedMembers |

## F5. Bảng quan hệ

| ID | Lớp A | Lớp B | Loại | Multiplicity | Điều hướng | Lý do | Vai trò | Căn cứ hiển thị |
|---|---|---|---|---|---|---|---|---|
| R-15 | DC-BookClassSpotHandler | DC-Member | Dependency | | A --> B | Handler nhận hội viên từ IF-11.findById trong một method rồi truyền cho GroupClass; giữ mã R-15 của P08 (Association tạm thời đổi thành Dependency theo cây quyết định) | | biến cục bộ |
| R-16 | DC-BookClassSpotHandler | DC-GroupClass | Dependency | | A --> B | Handler nạp lớp bằng IF-14.findByIdForUpdate trong một method; giữ mã R-16 của P08, đổi loại | | biến cục bộ |
| R-17 | DC-GroupClass | DC-ClassBooking | Association | A 1 - B 0..* | A --> B | Một chỗ đã đặt thuộc đúng một lớp (GL-05, BR-11); một lớp có 0 đến nhiều chỗ đã đặt (UC-015 luồng 5a nêu lớp không có hội viên), số chỗ không vượt sức chứa là bất biến của BR-11. Giữ chiều từ lớp vì msg 1.5.1 và việc đếm đi từ lớp; không composition vì chỗ đã đặt không bị xoá cùng lớp huỷ (Q-63). Giữ mã R-17 của P08 và thay "B ?" bằng "B 0..*" | bookings | field |
| R-18 | DC-GroupClass | DC-Waitlist | Association | A 1 - B 0..1 | A --> B | Danh sách chờ là của một lớp (GL-08, BR-12), tối đa một danh sách cho mỗi lớp; cận dưới 0 theo thiết kế tạo muộn, chờ Q-84. Giữ mã R-18 của P08 | waitlist | field |
| R-19 | DC-ClassBooking | DC-Member | Association | A 0..* - B 1 | A --> B | Chỗ đã đặt do đúng một hội viên đặt (GL-05); một hội viên có 0 đến nhiều chỗ đã đặt, BR-08 chỉ giới hạn theo ngày nên không cận trên chung (Q-59, Q-60). Giữ mã R-19 của P08 nhưng đảo Lớp A, B: P10 F6 đã chọn chiều PKG-29 --> PKG-26 để PKG-26 không phụ thuộc PKG-29 (P09 F6 V7), nên đầu trong phạm vi là Lớp A | member | field |
| R-20 | DC-Waitlist | DC-Member | Association | A 0..* - B 0..* | A --> B | Danh sách có thứ tự các hội viên chờ (GL-08): một danh sách nhiều hội viên; một hội viên có thể chờ nhiều lớp (Q-60 nêu lớp trong danh sách chờ của hội viên); mối quan hệ nhiều - nhiều có thuộc tính joinedAt nên hiện thực qua DC-WaitlistEntry (association class dạng value object, định danh bởi Waitlist + Member). Giữ mã R-20 của P08, thay "A ? - B ?" bằng "A 0..* - B 0..*"; không có cận trên trong nguồn (Q-61, Q-62, Q-84) | waiters | field (qua entries) |
| R-21 | DC-CancelUnderBookedClassHandler | DC-GroupClass | Dependency | | A --> B | Handler nạp lớp bằng IF-14.findByIdForUpdate trong một method; giữ mã R-21 của P08, đổi loại | | biến cục bộ |
| R-22 | DC-CancelUnderBookedClassHandler | DC-Member | Dependency | | A --> B | Handler nhận các hội viên từ GroupClass.collectBookedMembers và truyền qua tham số của notifyBookedMembers; giữ mã R-22 của P08, đổi loại | | tham số |
| R-29 | DC-BookClassSpotHandler | IF-14 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc | repository | field |
| R-30 | DC-BookClassSpotHandler | IF-11 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc | accounts | field |
| R-31 | DC-BookClassSpotHandler | DC-MemberBookingQuota | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc; thay phần checkDailyBookingLimit của R-15 | quota | field |
| R-32 | DC-BookClassSpotHandler | IF-16 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc | clock | field |
| R-33 | DC-CancelUnderBookedClassHandler | IF-14 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc | repository | field |
| R-34 | DC-CancelUnderBookedClassHandler | IF-06 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc | scheduler | field |
| R-35 | DC-CancelUnderBookedClassHandler | IF-03 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc; thay R-23 (P08 đặt gateway --> control, thiết kế đi từ control tới interface theo P11b) | pushGateway | field |
| R-36 | DC-CancelUnderBookedClassHandler | IF-04 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc; thay R-24 (như R-35) | smsGateway | field |
| R-37 | DC-CancelUnderBookedClassHandler | IF-16 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc | clock | field |
| R-38 | DC-CancelUnderBookedClassHandler | IF-10 | Realization | | A --> B | Handler hiện thực interface gọi ngược do PKG-22 định nghĩa (P09 F6 V4 a, P10 bảng Interface gọi ngược) | | |
| R-39 | DC-MemberBookingQuota | IF-14 | Association | A 0..* - B 1 | A --> B | Thiết kế: tiêm phụ thuộc | repository | field |
| R-40 | DC-GroupClass | DC-Member | Dependency | | A --> B | Member là tham số của reserveSpot, addToWaitlist | | tham số |
| R-41 | IF-14 | DC-GroupClass | Dependency | | A --> B | GroupClass là kiểu trả về và tham số của IF-14 | | tham số |
| R-42 | DC-CancelUnderBookedClassHandler | DC-NotificationContent | Dependency | | A --> B | Handler tạo NotificationContent trong composeClassCancelledNotice (PKG-24) | | biến cục bộ |

## F6. State machine

F6.1. Bảng trạng thái

| ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết | entry | do | exit |
|---|---|---|---|---|---|---|
| ST-01 | DC-GroupClass | Scheduled | status = SCHEDULED. Lớp còn hiệu lực. "Đã đủ chỗ" (GL-28) là điều kiện getBookedCount() >= capacity, không phải trạng thái lưu, vì số chỗ đổi bởi UC-011, UC-012 chưa có P07 và định nghĩa đủ chỗ còn Q-22 | - | - | - |
| ST-01 | DC-GroupClass | Cancelled | status = CANCELLED. Lớp bị huỷ do BR-13 hoặc do quản lý chi nhánh huỷ vì sự cố (REQ-76, UC-014 chưa có P07) | - | - | - |

F6.2. Bảng chuyển trạng thái

| ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích | STT | Operation tương ứng | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| ST-01 | DC-GroupClass | (initial) | create(id, classType, room, trainer, startTime, capacity) | | status = SCHEDULED | Scheduled | T1 | DC-GroupClass.GroupClass(...) | UC-009 (chưa có P07) |
| ST-01 | DC-GroupClass | Scheduled | reserveSpot(member) | [getBookedCount() < capacity] | thêm ClassBooking của hội viên | Scheduled | T2 | DC-GroupClass.reserveSpot | BR-11; UC-010 bước 8 |
| ST-01 | DC-GroupClass | Scheduled | addToWaitlist(member, now) | [getBookedCount() >= capacity] | thêm mục chờ vào danh sách chờ (tạo Waitlist nếu chưa có) | Scheduled | T3 | DC-GroupClass.addToWaitlist | BR-12; UC-010 bước 7a3 |
| ST-01 | DC-GroupClass | Scheduled | cancelClass() | | status = CANCELLED | Cancelled | T4 | DC-GroupClass.cancelClass | BR-13; UC-015 bước 3 |

Trạng thái Cancelled không có chuyển ra và không nối tới (final): nguồn chưa nêu sự kiện lưu trữ hay xoá lớp (ghi ở F6.4).

Sự kiện bị từ chối:

| ST | Trạng thái | Sự kiện | Xử lý (bỏ qua / ngoại lệ <tên>) |
|---|---|---|---|
| ST-01 | Scheduled | reserveSpot [getBookedCount() >= capacity] | ngoại lệ DC-SpotUnavailableException |
| ST-01 | Scheduled | addToWaitlist [getBookedCount() < capacity] | ngoại lệ DC-WaitlistNotAllowedException (Q-106) |
| ST-01 | Cancelled | reserveSpot, addToWaitlist, cancelClass | ngoại lệ DC-InvalidClassStateException |

Các operation truy vấn (provideClassInfo, assessBookability, hasAvailableSpot, assessCancellation, collectBookedMembers, getStatus, getBookedCount) hợp lệ ở cả hai trạng thái và không phải sự kiện.

F6.3. Bảng ánh xạ về mô hình lớp

| ST | Thuộc tính biểu diễn trạng thái | Kiểu (enumeration) | Operation được thêm/sửa |
|---|---|---|---|
| ST-01 | DC-GroupClass.status | DC-GroupClassStatus (SCHEDULED, CANCELLED) | Thêm getStatus; reserveSpot, addToWaitlist, cancelClass kiểm tra status trước khi làm (F3) |

F6.4. Sơ đồ state machine: file diagrams/P12-state-DC-GroupClass.drawio, một trang. Không vẽ (final) vì nguồn chưa có sự kiện kết thúc vòng đời của lớp. Lớp DC-ClassBooking, DC-Waitlist chưa có state machine: hành vi chuyển trạng thái của chúng thuộc UC-011, UC-012, UC-013, UC-016 chưa có P07 (ghi ở Vấn đề còn mở).

Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| ST-01-I | Initial |  | - | - | Initial | 660 | 40 | 40 | 40 |
| ST-01-S1 | State | Scheduled | - | - | status = SCHEDULED | 600 | 140 | 160 | 60 |
| ST-01-S2 | State | Cancelled | - | - | status = CANCELLED | 600 | 340 | 160 | 60 |

Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| ST-01-T1 | ST-01-I | ST-01-S1 | Transition | create(...) / status = SCHEDULED | Sự kiện tạo; UC-009 chưa có P07 | - |
| ST-01-T2 | ST-01-S1 | ST-01-S1 | Transition | reserveSpot(member) [bookedCount < capacity] / thêm ClassBooking | Tự chuyển | (820,160); (820,180) |
| ST-01-T3 | ST-01-S1 | ST-01-S1 | Transition | addToWaitlist(member, now) [bookedCount >= capacity] / thêm WaitlistEntry | Tự chuyển | (540,160); (540,180) |
| ST-01-T4 | ST-01-S1 | ST-01-S2 | Transition | cancelClass() / status = CANCELLED | BR-13; UC-015 bước 3 | - |

## F7. Bảng thuộc tính

DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler, IF-14, IF-16 không có thuộc tính; phụ thuộc tiêm ghi ở F5.

| DC | Visibility | Tên | Kiểu | Multiplicity | Mặc định | Ràng buộc | Phạm vi | Derived | Nguồn | Mô tả |
|---|---|---|---|---|---|---|---|---|---|---|
| DC-GroupClass | - | id | string | 1 | | {readOnly, unique} | Instance | Không | Bổ sung: định danh để P13 làm khoá | Mã lớp; lớp do UC-009 tạo nên giá trị cấp khi tạo |
| DC-GroupClass | - | classType | string | 1 | | | Instance | Không | P08 AC-E-GroupClass; GL-27 | Loại lớp (yoga, aerobic, đạp xe trong nhà theo nguồn); danh mục đóng hay mở chờ Q-04; thuộc tính tạm |
| DC-GroupClass | - | room | string | 1 | | | Instance | Không | P08 AC-E-GroupClass; GL-35 | Phòng diễn ra lớp; phòng thuộc chi nhánh nào chờ Q-03; thuộc tính tạm |
| DC-GroupClass | - | trainer | string | 1 | | | Instance | Không | P08 AC-E-GroupClass; GL-21 | Họ tên huấn luyện viên phụ trách; chờ Q-05; thuộc tính tạm |
| DC-GroupClass | - | startTime | Date | 1 | | | Instance | Không | P08 AC-E-GroupClass; GL-13 | Giờ học (ngày và giờ bắt đầu); chờ Q-73 |
| DC-GroupClass | - | capacity | number | 1 | | {số nguyên, >= 0} | Instance | Không | P08 AC-E-GroupClass; BR-10 | Sức chứa của lớp, xác định theo phòng; chờ Q-03 |
| DC-GroupClass | - | status | GroupClassStatus | 1 | SCHEDULED | | Instance | Không | ST-01 | Trạng thái của lớp |
| DC-GroupClass | - | /bookedCount | number | 1 | | | Instance | Có: số phần tử của bookings (R-17) | BR-10, BR-11, BR-13 | Số chỗ đã đặt; không lưu, tính khi đọc; getBookedCount trả giá trị này |
| DC-GroupClass | + | UNDER_BOOKED_THRESHOLD | number | 1 | 3 | {readOnly} | Classifier | Không | BR-13 | Ngưỡng số người đặt chỗ dưới đó lớp bị huỷ |
| DC-ClassBooking | - | id | string | 0..1 | | {readOnly} | Instance | Không | Bổ sung: định danh để P13 làm khoá | Thiết kế: bỏ trống cho tới khi IF-14.save gán, để entity không tự sinh giá trị ngẫu nhiên |
| DC-Waitlist | - | id | string | 0..1 | | {readOnly} | Instance | Không | Bổ sung: định danh để P13 làm khoá | Như DC-ClassBooking.id |
| DC-Waitlist | - | entries | WaitlistEntry | 0..* | | {ordered} | Instance | Không | P08 AC-E-Waitlist; GL-08 | Các mục chờ theo thứ tự xếp chờ (Q-61); mỗi mục giữ hội viên (R-20) và thời điểm vào joinedAt |
| DC-MemberBookingQuota | + | MAX_BOOKINGS_PER_DAY | number | 1 | 2 | {readOnly} | Classifier | Không | BR-08 | Số chỗ tối đa mỗi hội viên được đặt trong một ngày |

## F8. Class diagram

| Sơ đồ | Phạm vi (PKG / UC) | File .drawio | Số lớp |
|---|---|---|---|
| Class diagram PKG-15 | PKG-15 | diagrams/P12-class-PKG-15.drawio | 2 lớp của package, 7 interface tham chiếu |
| Class diagram PKG-29 | PKG-29 | diagrams/P12-class-PKG-29.drawio | 5 lớp, interface của package, 1 lớp tham chiếu |
| State machine DC-GroupClass | ST-01 | diagrams/P12-state-DC-GroupClass.drawio | 1 lớp |

Không vẽ class diagram tham gia UC vì MUC_CHI_TIET là GON (chỉ khi DAY_DU). Kiểu phụ trợ ở F1b không vẽ vì không có quan hệ nào khác ngoài chữ ký. Các quan hệ R-15, R-16, R-21, R-22, R-31, R-40 tới entity hoặc dịch vụ của package khác liệt kê ở F5; R-31 không vẽ ở sơ đồ PKG-15 theo quy tắc package chứa control.

Sơ đồ PKG-15: Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-BookClassSpotHandler | Class | BookClassSpotHandler | «control» | PKG-15 | Lớp trong package | 40 | 240 | 520 | 140 |
| DC-CancelUnderBookedClassHandler | Class | CancelUnderBookedClassHandler | «control» | PKG-15 | Lớp trong package; hiện thực IF-10 | 760 | 240 | 580 | 200 |
| IF-11 | Interface | IF-11 IAccountRepository | «interface» | PKG-26 | tham chiếu | 40 | 40 | 280 | 50 |
| IF-06 | Interface | IF-06 IScheduler | «interface» | PKG-22 | tham chiếu | 760 | 40 | 280 | 50 |
| IF-10 | Interface | IF-10 IScheduleMarkHandler | «interface» | PKG-22 | tham chiếu | 1080 | 40 | 280 | 50 |
| IF-03 | Interface | IF-03 IPushNotificationGateway | «interface» | PKG-24 | tham chiếu | 1440 | 240 | 340 | 50 |
| IF-04 | Interface | IF-04 ISmsGateway | «interface» | PKG-24 | tham chiếu | 1440 | 340 | 340 | 50 |
| IF-14 | Interface | IF-14 IGroupClassRepository | «interface» | PKG-29 | tham chiếu | 380 | 560 | 300 | 50 |
| IF-16 | Interface | IF-16 IClock | «interface» | PKG-32 | tham chiếu (cấp mới ở P12, vị trí chờ P10) | 1000 | 560 | 300 | 50 |

Sơ đồ PKG-15: Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-29 | DC-BookClassSpotHandler | IF-14 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc | (200,480); (480,480) |
| R-30 | DC-BookClassSpotHandler | IF-11 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc | - |
| R-32 | DC-BookClassSpotHandler | IF-16 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc | (320,460); (1100,460) |
| R-33 | DC-CancelUnderBookedClassHandler | IF-14 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc | (840,490); (600,490) |
| R-34 | DC-CancelUnderBookedClassHandler | IF-06 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc | - |
| R-35 | DC-CancelUnderBookedClassHandler | IF-03 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc; thay R-23 (đảo chiều theo IF-03) | - |
| R-36 | DC-CancelUnderBookedClassHandler | IF-04 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc; thay R-24 (đảo chiều theo IF-04) | - |
| R-37 | DC-CancelUnderBookedClassHandler | IF-16 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc | (1240,510); (1200,510) |
| R-38 | DC-CancelUnderBookedClassHandler | IF-10 | Realization | - | Handler hiện thực interface gọi ngược IF-10 | - |

Sơ đồ PKG-29: Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-GroupClass | Class | GroupClass | «entity» | PKG-29 | Lớp trong package; persistent; gốc tập hợp | 40 | 300 | 700 | 430 |
| DC-ClassBooking | Class | ClassBooking | «entity» | PKG-29 | Lớp trong package; persistent | 860 | 320 | 400 | 120 |
| DC-Waitlist | Class | Waitlist | «entity» | PKG-29 | Lớp trong package; persistent | 860 | 480 | 520 | 170 |
| DC-MemberBookingQuota | Class | MemberBookingQuota | «service» | PKG-29 | Lớp trong package; không persistent | 860 | 40 | 560 | 110 |
| IF-14 | Interface | IF-14 IGroupClassRepository | «interface» | PKG-29 | Interface kho dữ liệu trong package | 40 | 40 | 680 | 180 |
| DC-Member | Class | Member | «entity» | PKG-26 | tham chiếu | 1540 | 340 | 240 | 60 |

Sơ đồ PKG-29: Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| R-17 | DC-GroupClass | DC-ClassBooking | Association | A 1 - B 0..* | Một lớp có 0..* chỗ đã đặt, không vượt sức chứa (BR-11); vai trò bookings | - |
| R-18 | DC-GroupClass | DC-Waitlist | Association | A 1 - B 0..1 | Cận dưới 0 chờ Q-84; vai trò waitlist | - |
| R-19 | DC-ClassBooking | DC-Member | Association | A 0..* - B 1 | Đảo Lớp A, B so với P08; vai trò member | - |
| R-20 | DC-Waitlist | DC-Member | Association | A 0..* - B 0..* | Qua WaitlistEntry; vai trò waiters | (1660,540) |
| R-39 | DC-MemberBookingQuota | IF-14 | Association | A 0..* - B 1 | Thiết kế: tiêm phụ thuộc | - |
| R-40 | DC-GroupClass | DC-Member | Dependency | - | Member là tham số của reserveSpot, addToWaitlist | (500,250); (1740,250) |
| R-41 | IF-14 | DC-GroupClass | Dependency | - | GroupClass là kiểu trả về, tham số của IF-14 | - |

## F9. Gán package và kiểm tra phụ thuộc package

| PKG | Lớp (DC) | Phụ thuộc vào PKG (suy từ F5) | Hợp lệ theo P09 (Có / Không: lý do) |
|---|---|---|---|
| PKG-15 GroupClassService | DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler, DC-BookClassResult, DC-WaitlistPlacement, DC-BookingOutcome | PKG-29 (R-16, R-21, R-29, R-31, R-33); PKG-26 (R-15, R-22, R-30); PKG-22 (R-34, R-38); PKG-24 (R-35, R-36, R-42); PKG-32 (R-32, R-37, kiểu PhoneNumber) | Có: Application phụ thuộc xuống Domain và Services (P09 F6 V1, V5), realization R-38 đi xuống PKG-22 (V4 a). PKG-32 chưa có trong cột Phụ thuộc vào của P10 F4 cho PKG-15: Đề xuất sửa P10 bên dưới. Cạnh PKG-15 --> PKG-30 của P09 chưa suy ra vì UC-016 chưa có P07 |
| PKG-29 GroupClass | DC-GroupClass, DC-ClassBooking, DC-Waitlist, DC-MemberBookingQuota, IF-14, DC-ClassInfo, DC-WaitlistEntry, DC-GroupClassStatus, DC-Bookability, DC-CancellationCheck, bốn exception | PKG-26 (R-19, R-20, R-40) | Có: cùng layer Domain, một chiều PKG-29 --> PKG-26 (V3, V7), không vòng vì PKG-26 không phụ thuộc PKG-29. Realization của IF-14 bởi DC-GroupClassRepositoryImpl đi từ PKG-20 xuống PKG-29 (V4 b), thiết kế ở lần chạy PKG-20 |

Kiểm tra gán package: hai handler cùng layer, cùng nhóm Lớp nhóm, cùng tác nhân hội viên hoặc thời gian nhưng chung một nhóm chức năng theo P10; bốn entity và dịch vụ cùng nhóm Lớp nhóm. Chỉ lớp public của package được tham chiếu từ ngoài: DC-ClassInfo, DC-GroupClass và các kiểu phụ trợ của PKG-29 được PKG-15 dùng và PKG-20 hiện thực nên public; DC-ClassBooking, DC-Waitlist, DC-WaitlistEntry chỉ PKG-20 dùng.

## F10. Design pattern đã áp dụng

| Pattern | Vấn đề trong thiết kế này | Lớp tham gia (vai trò trong pattern) | Lý do chọn | Phương án đơn giản hơn đã xét |
|---|---|---|---|---|
| Repository | Tách truy cập dữ liệu khỏi logic nghiệp vụ; mọi truy cập CSDL qua PKG-20 (P09 F7) | IF-14 (repository interface, Domain), DC-GroupClassRepositoryImpl (hiện thực, PKG-20), DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler, DC-MemberBookingQuota (bên dùng) | P09 F5 và F6 V4 b đã chốt interface kho dữ liệu ở Domain và hiện thực ở Persistence | Control gọi ORM trực tiếp: không đủ vì P09 F7 chỉ cho PKG-20 truy cập CSDL |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-106 | Khi hội viên yêu cầu vào danh sách chờ (UC-010 bước 7a2) mà lúc đó lớp nhóm đã bị huỷ, đã còn chỗ (hội viên khác vừa huỷ chỗ), hoặc hội viên không còn đủ điều kiện đặt chỗ (quyền đặt lớp vừa bị khoá, đã đặt đủ số lớp trong ngày), hệ thống xử lý thế nào? (Từ chối và thông báo lý do rồi quay lại bước 2 / Còn chỗ thì đặt chỗ luôn cho hội viên / Vẫn cho vào danh sách chờ / Khác - nêu rõ) | DC-BookClassSpotHandler.joinWaitlist; DC-GroupClass.addToWaitlist (DC-WaitlistNotAllowedException); ST-01 sự kiện bị từ chối; P04 UC-010 luồng 7a | UC-010 luồng 7a1 đến 7a3 nêu hội viên "yêu cầu vào danh sách chờ" sau khi được thông báo lớp đủ chỗ, không nêu trạng thái lớp và hội viên có thể đổi trong khoảng đó; không có luồng thay thế cho 7a3 |
| Q-107 | Mốc chuyển chỗ của UC-013 (30 phút sau khi báo có chỗ trống cho người đứng đầu danh sách chờ) gắn với lớp nhóm hay gắn với từng lời mời nhận chỗ, một lớp có thể có nhiều mốc chuyển chỗ cùng lúc không, và khi lớp bị huỷ thì cần huỷ những mốc nào? (Mỗi lớp tối đa một mốc đang chờ, khoá theo mã lớp / Mỗi lời mời một mốc, khoá theo mã lời mời - nêu cách tìm các mốc của một lớp / Khác - nêu rõ) | DC-CancelUnderBookedClassHandler.cancelWaitlistTransferMark (khoá subjectRef của IF-06.cancelMark, MarkKind.WaitlistTransfer); P07 UC-013 khi có | GL-08 (hạn 30 phút xác nhận nhận chỗ, REQ-29), UC-015 bước 4 "mốc chuyển chỗ của UC-013 gắn với lớp", P07 UC-015 Vấn đề còn mở (mốc tính từ lúc báo, không từ giờ học), P11b IF-06 khoá mốc theo (loại mốc, mã đối tượng) |

Các câu hỏi đã cấp ở bước trước và làm đổi thiết kế này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-03, Q-04, Q-05 (phòng, loại lớp, huấn luyện viên, sức chứa); Q-11, Q-58 (thời hạn đặt chỗ); Q-20, Q-22 (chỗ của hội viên bị khoá, chỗ giữ riêng); Q-36 (hội viên chưa cài ứng dụng); Q-59, Q-60 (đặt trùng, cách tính ngày); Q-61, Q-62 (thứ tự xếp chờ, tự vào hay chọn vào); Q-63 (chỗ đã đặt và danh sách chờ khi lớp bị huỷ); Q-64 (huỷ mốc); Q-65, Q-79 (gửi không được); Q-66 (nội dung thông báo); Q-73 (giờ học); Q-83 (phạm vi lịch); Q-84 (danh sách chờ là đối tượng riêng); Q-85 (lưu việc đã gửi thông báo); Q-102 (lỗi cơ chế hẹn giờ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3 (bảng phần tử mới), F4 (PKG-15, PKG-29, PKG-32), F5 | P12 cấp mã DC cho kiểu phụ trợ dùng qua ranh giới package và IF-16: PKG-29 có DC-ClassInfo, DC-WaitlistEntry, DC-GroupClassStatus, DC-Bookability, DC-CancellationCheck, DC-GroupClassNotFoundException, DC-SpotUnavailableException, DC-InvalidClassStateException, DC-WaitlistNotAllowedException (PKG-15 và PKG-20 dùng); PKG-15 có DC-BookClassResult, DC-BookingOutcome, DC-WaitlistPlacement (PKG-10 dùng). Nền tảng TypeScript không có kiểu đồng hồ chuẩn nên cấp IF-16 IClock (Bước 1.5, 2.6), chưa có package chứa | Thêm các phần tử trên vào bảng phần tử mới, cột Phần tử chứa của F4 và F5 (public như nêu); đặt IF-16 ở PKG-32 hoặc ở package tiện ích do P10 quyết định (P12 chưa tạo PKG mới); thêm cạnh PKG-15 --> PKG-32 vào F4, F6, F9 (IF-16, PhoneNumber, layer trên phụ thuộc layer dưới). Chưa áp dụng |
| P08 | F4 R-19 (AC-E-Member, AC-E-ClassBooking); R-23, R-24 | R-19 đặt AC-E-Member là Lớp A trong khi P10 F6 chọn chiều PKG-29 --> PKG-26; R-23, R-24 đặt boundary thông báo là Lớp A, còn control gọi interface của boundary theo P11b | Khi chạy lại P08, ghi R-19 với Lớp A là AC-E-ClassBooking và R-23, R-24 với control là Lớp A; chỉ đổi cấu trúc, không chạy lại P07. Chưa áp dụng |
| P04 | UC-010 luồng 7a (7a3) | Đặc tả không nêu kết cục khi lớp hoặc hội viên đã đổi trạng thái giữa 7a1 và 7a3 (Q-106) | Khi Q-106 có câu trả lời, thêm luồng thay thế cho 7a3 rồi chạy lại P07 UC-010. Chưa áp dụng vì Q-106 chưa có trả lời |

## Vấn đề còn mở

Cách chia lần chạy: toàn hệ thống vượt 20 lớp có hành vi nên chạy theo package; lần này gồm hai package có quan hệ chặt (PKG-15 điều phối, PKG-29 miền) với 7 lớp có hành vi, dưới ngưỡng 15 nên một lượt, không dùng cách chia hai lượt. Các mục Target đạt, trừ các điểm sau:

- Target 12 đạt một phần: thân DC-GroupClass.assessBookability (bước kiểm tra thời hạn đặt chỗ) và DC-Waitlist.compareWaitOrder chưa đặc tả được vì nguồn chưa chốt (Q-11, Q-58, Q-61). Chữ ký, vị trí và nguồn đã cố định để câu trả lời chỉ đổi thân hàm. Các nhánh chờ Q khác (Q-22, Q-59, Q-60, Q-63, Q-65, Q-66, Q-83, Q-84, Q-102, Q-106, Q-107) đã ghi tại operation tương ứng.
- Target 6 đạt một phần: vòng đời đầy đủ của DC-GroupClass (tạo bởi UC-009, huỷ vì sự cố bởi UC-014), DC-ClassBooking (huỷ, chuyển, vắng mặt bởi UC-011, UC-012, UC-016) và DC-Waitlist (rời danh sách, nhận chỗ bởi UC-011, UC-012, UC-013) thuộc các use case chưa có P07. Target 18: DC-ClassBooking và DC-Waitlist chưa có state machine vì chưa có P07 của các use case đó; ST-01 chỉ có hai trạng thái lưu và sẽ thêm chuyển trạng thái khi có P07 của UC-009, UC-011, UC-014.
- Target 24: bảng Node/Edge khớp F1, F2, F5, F7; file .drawio đã kiểm tra bằng chương trình (XML hợp lệ, không nén, tọa độ bội số của 10, không chồng node, không cạnh cắt qua node, khoảng cách node từ 40). Chưa mở bằng draw.io để kiểm tra bằng mắt, nhất là nhãn của hai cạnh tự chuyển trong ST-01.
- Phạm vi: DC-GroupClassRepositoryImpl (PKG-20) hiện thực IF-14 và phải hiện thực cả runInTransaction với ngữ cảnh giao dịch dùng chung cho IF-11 và IF-14; DC-BookClassSpotView, DC-BookClassSpotStore (PKG-05), DC-BookClassSpotController (PKG-10) cùng SCR-06, SCR-07, SCR-08 thuộc lần chạy của package đó. Quan hệ R-14 (Lớp A là boundary, PKG-05), R-23, R-24 (Lớp A là boundary thông báo, PKG-24) chỉ liệt kê mã, không thiết kế ở đây; R-31 thay phần checkDailyBookingLimit của R-15.
- Chữ ký chờ đối chiếu: các chữ ký ở F4b và bảng Chữ ký interface tạm (IF-11.findById, DC-Member.isBookingSuspended, determineNotificationChannel, getPhoneNumber, getId, MemberNotFoundException, NotificationContent) do lần chạy PKG-26 và PKG-24 chốt; chạy P12 cho PKG-26 rồi đối chiếu, chạy lại P12 cho phạm vi này nếu khác.
- Rủi ro đồng thời của BR-08 mà khoá dòng lớp không bảo vệ: hai yêu cầu đồng thời của cùng một hội viên cho hai lớp khác nhau trong cùng ngày có thể cùng vượt qua bước 6 vì mỗi giao dịch chỉ khoá dòng của lớp mình. Rủi ro thấp (cùng một hội viên bấm hai lần) nên chưa thêm khoá theo hội viên; nếu cần, thêm operation khoá dòng hội viên vào IF-11 và gọi trước bước 4 của bookClass. Chờ người dùng quyết định, không phải câu hỏi nghiệp vụ.
- Mất thông báo khi mốc giao lại: nếu tiến trình dừng giữa lúc commit huỷ lớp và lúc chuyển hết yêu cầu gửi, mốc được SS-06 giao lại sẽ gặp lớp đã huỷ (nhánh 2a) và không gửi tiếp cho hội viên chưa được báo. Chỉ đóng được khi nguồn quy định lưu trạng thái thông báo từng hội viên (Q-85) hoặc kết cục khi gửi không được (Q-65); hàng chờ gửi nền của SS-03, SS-04 cũng nằm trong bộ nhớ nên mất khi tiến trình dừng (P11b Vấn đề còn mở).
- Chỗ đã đặt của lớp đã huỷ vẫn được hasReachedDailyLimit đếm vì chỗ đã đặt chưa đổi khi lớp bị huỷ (Q-63): hội viên có lớp bị huỷ trong ngày có thể bị tính vào mức tối đa 2 lớp. Cần trả lời Q-63 để quyết định đếm hay không.
- Quy ước tên: P11b viết giá trị MarkKind dạng PascalCase (ClassCutoff, AbsenceCheck, WaitlistTransfer), còn mặc định của P12 là UPPER_SNAKE_CASE cho giá trị enumeration; các enumeration mới ở đây dùng UPPER_SNAKE_CASE, các giá trị MarkKind của PKG-22 giữ nguyên theo P11b. DC-CancelUnderBookedClassHandler là package-private theo P10 F5 nhưng handleMarkDue là public vì phải hiện thực IF-10.
- Chọn giữa hai quy tắc (C9): Bước 2.1 yêu cầu F4 chỉ chứa message có lớp nhận trong phạm vi, nhưng handler trong phạm vi gọi DC-Member (PKG-26) chưa có P12; theo C1 mục 3 và nhu cầu nhất quán chữ ký, thêm bảng F4b thay vì bỏ qua. F5 để Lớp A của R-19 đổi theo P10 F6 trái với mã P08 (Đề xuất sửa P08 ở trên).
- PKG-15 thiếu cạnh tới PKG-30 theo P09 (UC-016 chưa có P07), không suy ra ở lần chạy này; DC-ClassBooking mỏng (hai operation) giữ theo P10 F3.
