# P11b - SS-06 DurableScheduler - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | SS-06 DurableScheduler (package PKG-22 Scheduling); lần chạy đầu cho mọi subsystem của P10 F2 |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102, ghi ở file chung P11b-system-interfaces.md); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-005 Mua hoặc gia hạn gói tập | AC-C-PurchaseOrRenewPackageHandler (DC-PurchaseOrRenewPackageHandler) | SD1b STT 3.1.3 startWaitingForPayment (BR-04), bước 9 --> IF-06.scheduleMark; STT 4.1.1 stopWaitingForPayment, bước 10 --> IF-06.cancelMark; STT 3.1.4 after(BR-04) handlePaymentTimeout --> IF-10.handleMarkDue | Loại mốc (hạn thanh toán), mã đơn mua, thời điểm đến hạn (15 phút, BR-04) | 9a (hết thời hạn mà đơn chưa thanh toán thành công); không đặt được mốc: P04 chưa có luồng (Q-102); mốc bắt đầu tính: Q-25 |
| UC-015 Huỷ lớp nhóm ít người đặt | AC-C-CancelUnderBookedClassHandler (DC-CancelUnderBookedClassHandler) | SD1a STT 1 handleClassCutoff (ACT-14 vào control) --> IF-10.handleMarkDue; STT 1.3 cancelAbsenceMark, 1.4 cancelWaitlistTransferMark, bước 4 --> IF-06.cancelMark | Loại mốc, mã lớp nhóm | Huỷ mốc có thực hiện hay các use case sau tự bỏ qua lớp đã huỷ: Q-64; không huỷ được mốc: P04 chưa có luồng (Q-102) |

- Các P07 tự gọi (startWaitingForPayment, stopWaitingForPayment, handlePaymentTimeout, cancelAbsenceMark, cancelWaitlistTransferMark) là hành vi đã được P10 F2 giao cho SS-06; P11b chỉ định chữ ký IF-06, IF-10 cho chúng.
- UC-008, UC-009, UC-013, UC-014, UC-016, UC-022 hẹn hoặc huỷ mốc nhưng chưa có P04, P07 (Chờ P07 UC-008, UC-009, UC-013, UC-014, UC-016, UC-022); loại mốc của chúng thêm vào DC-MarkKind khi chạy lại.

## F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-06 | IScheduler | Đặt, huỷ mốc hẹn bền; đăng ký bộ xử lý theo loại mốc; bật, tắt vòng quét. | SS-06 DurableScheduler | DC-PurchaseOrRenewPackageHandler (PKG-14); DC-CancelUnderBookedClassHandler (PKG-15); lớp của PKG-17 khi có P07 | PKG-22 Scheduling |
| IF-10 | IScheduleMarkHandler | Nhận mốc đến hạn và chuyển cho control xử lý. | DC-PurchaseOrRenewPackageHandler (PKG-14); DC-CancelUnderBookedClassHandler (PKG-15); lớp của PKG-17 khi có P07 (interface gọi ngược) | SS-06 DurableScheduler | PKG-22 Scheduling |

- Số operation: IF-06 có 5, IF-10 có 1.
- Layer: IF-06, IF-10 ở PKG-22 (Services); các Handler ở PKG-14, PKG-15 (Application) hiện thực IF-10, realization đi xuống (P09 F6 V4 a). DC-MarkKind ở PKG-22.

## F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-06 | IScheduler | Bộ định thời (ACT-13, ACT-14) | scheduleMark(kind: MarkKind, subjectRef: string, dueAt: Date): void | kind: MarkKind - PaymentDeadline hoặc ClassCutoff (loại khác khi có P07)<br>subjectRef: string - mã đối tượng gắn mốc (đơn mua, lớp nhóm), không rỗng<br>dueAt: Date - sau thời điểm hiện tại | - | MarkStoreUnavailable (Kỹ thuật tạm thời) | UC-005 (bước 9); UC-009 (Chờ P07) | Đối tượng gắn mốc tồn tại | Có một mốc chưa đến hạn gắn với (kind, subjectRef) được lưu bền | Đồng bộ | Có (cùng (kind, subjectRef) thì thay mốc cũ) | 3 giây (Thiết kế: một lần ghi CSDL, ngắn hơn thời gian người dùng chờ ở bước 9) |
| IF-06 | IScheduler | Bộ định thời (ACT-13, ACT-14) | cancelMark(kind: MarkKind, subjectRef: string): void | kind: MarkKind<br>subjectRef: string - mã đối tượng gắn mốc | - | MarkStoreUnavailable (Kỹ thuật tạm thời) | UC-005 (bước 10); UC-015 (bước 4) | - | Không còn mốc chưa đến hạn loại kind gắn với subjectRef; mốc đang được xử lý không bị dừng | Đồng bộ | Có (huỷ mốc không tồn tại không báo lỗi) | 3 giây (Thiết kế: một lần ghi CSDL) |
| IF-06 | IScheduler | Bộ định thời (ACT-13, ACT-14) | registerMarkHandler(kind: MarkKind, handler: IScheduleMarkHandler): void | kind: MarkKind<br>handler: IScheduleMarkHandler - không rỗng | - | - | UC-005, UC-015 (kỹ thuật) | Chưa start | Mốc loại kind đến hạn được chuyển cho handler | Đồng bộ | Có (đăng ký lại thay handler cũ) | - (không chờ hệ thống ngoài) |
| IF-06 | IScheduler | Bộ định thời (ACT-13, ACT-14) | start(): void | - | - | - | UC-005, UC-015 (kỹ thuật) | Đã registerMarkHandler cho các loại mốc cần dùng | Vòng quét mốc đến hạn chạy | Đồng bộ | Có | - (không chờ hệ thống ngoài) |
| IF-06 | IScheduler | Bộ định thời (ACT-13, ACT-14) | stop(): void | - | - | - | UC-005, UC-015 (kỹ thuật) | - | Vòng quét dừng; mốc đang xử lý được xử lý xong | Đồng bộ | Có | - (không chờ hệ thống ngoài) |
| IF-10 | IScheduleMarkHandler | Bộ định thời (ACT-13, ACT-14) | handleMarkDue(kind: MarkKind, subjectRef: string, dueAt: Date): void | kind: MarkKind<br>subjectRef: string<br>dueAt: Date - thời điểm mốc đến hạn | - | Handler ném lỗi thì SS-06 coi là MarkHandlingFailed (Kỹ thuật tạm thời) | UC-005 (luồng 9a); UC-015 (bước 1) | SS-06 đã giữ quyền xử lý mốc (mỗi mốc chỉ một bản chạy nhận, P09 F7) | Handler đã xử lý; mốc được đánh dấu hoàn tất | Đồng bộ (SS-06 chờ handler xong để đánh dấu hoàn tất) | Có (P09 F7: mốc có thể được giao lại) | 60 giây (Thiết kế: thời hạn giữ quyền xử lý một mốc; quá hạn mốc được giao lại cho bản chạy khác nên handler phải idempotent) |

- Ánh xạ trách nhiệm P10 F2 của SS-06: // scheduleMark --> IF-06.scheduleMark; // cancelMark --> IF-06.cancelMark; // registerMarkHandler, // start, // stop --> IF-06; mốc đến hạn --> IF-10.handleMarkDue.
- SS-06 không có boundary nguồn ở P08; trách nhiệm lấy từ P10 F2 và các message tự gọi của P07 UC-005, UC-015 (xem F1).
- Khoảng quét 10 giây là tham số kỹ thuật (Thiết kế: nhỏ hơn nhiều so với mốc ngắn nhất, 10 phút của UC-016 và 15 phút của BR-04); độ lệch mốc cho phép chờ Q-93. Thử lại một mốc xử lý lỗi: tối đa 3 lần cách 1 phút (Thiết kế: cùng mức với chính sách thử lại thông báo, handler idempotent).

## F4. Sequence diagram

File diagrams/P11b-subsystem-SS-06.drawio gồm 7 trang: "Hộp đen - UC-005 hạn thanh toán"; "Hộp đen - UC-015 mốc 2 giờ"; "Hộp trắng - scheduleMark"; "Hộp trắng - cancelMark"; "Hộp trắng - handleMarkDue"; "Phần tử"; "Phụ thuộc". STT đánh số phẳng theo trục thời gian trong mỗi trang; tọa độ bảng Node là tuyệt đối. Gate nằm trên cạnh trái khung sd, tâm gate ở y của message nên x, y của gate lệch 5 so với bội số của 10 (xem Vấn đề còn mở).

### Trang "Hộp đen - UC-005 hạn thanh toán" (SS06-BB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-BB1-FR | Fragment | sd Hộp đen UC-005 mốc hạn thanh toán | - | - | Khung sd của trang | 20 | 0 | 580 | 480 |
| SS06-BB1-L1 | Lifeline | :PurchaseOrRenewPackageHandler | «control» | - | DC-PurchaseOrRenewPackageHandler (PKG-14) | 100 | 40 | 120 | 420 |
| SS06-BB1-L2 | Lifeline | :IF-06 IScheduler | «interface» | - | Subsystem SS-06 hiện thực | 260 | 40 | 120 | 420 |
| SS06-BB1-L3 | Lifeline | :IF-10 IScheduleMarkHandler | «interface» | - | Handler hiện thực; SS-06 gọi | 420 | 40 | 120 | 420 |
| SS06-BB1-F1 | Fragment | alt [lưu mốc thành công] | - | - | đường ngăn SS06-BB1-F1-O2-SEP nét đứt tại y=180 | 80 | 140 | 320 | 70 |
| SS06-BB1-F2 | Fragment | alt [kết quả thanh toán về trong thời hạn] | - | - | đường ngăn SS06-BB1-F2-O2-SEP nét đứt tại y=340 | 80 | 260 | 480 | 150 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS06-BB1-F1 toán hạng 2: [không lưu được mốc]; SS06-BB1-F2 toán hạng 2: [hết thời hạn BR-04].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-BB1-M01 | 1 | SS06-BB1-L1 | SS06-BB1-L2 | scheduleMark(PaymentDeadline, orderRef, dueAt) | Đồng bộ | - | UC-005 bước 9; scheduleMark |
| SS06-BB1-M02 | 2 | SS06-BB1-L2 | SS06-BB1-L1 | đã lưu mốc | Trả về | SS06-BB1-F1 (toán hạng 1) | UC-005 bước 9 |
| SS06-BB1-M03 | 3 | SS06-BB1-L2 | SS06-BB1-L1 | MarkStoreUnavailable | Trả về | SS06-BB1-F1 (toán hạng 2) | UC-005 bước 9; Q-102 |
| SS06-BB1-M04 | 4 | SS06-BB1-L1 | SS06-BB1-L1 | awaitPaymentResult() | Tự gọi | - | UC-005 bước 9 (chờ trong thời hạn BR-04) |
| SS06-BB1-M05 | 5 | SS06-BB1-L1 | SS06-BB1-L2 | cancelMark(PaymentDeadline, orderRef) | Đồng bộ | SS06-BB1-F2 (toán hạng 1) | UC-005 bước 10; cancelMark |
| SS06-BB1-M06 | 6 | SS06-BB1-L2 | SS06-BB1-L1 | đã huỷ mốc | Trả về | SS06-BB1-F2 (toán hạng 1) | UC-005 bước 10 |
| SS06-BB1-M07 | 7 | SS06-BB1-L2 | SS06-BB1-L3 | handleMarkDue(PaymentDeadline, orderRef, dueAt) | Bất đồng bộ | SS06-BB1-F2 (toán hạng 2) | UC-005 luồng 9a; handleMarkDue |
| SS06-BB1-M08 | 8 | SS06-BB1-L3 | SS06-BB1-L1 | handlePaymentTimeout(orderRef) | Đồng bộ | SS06-BB1-F2 (toán hạng 2) | UC-005 luồng 9a |

### Trang "Hộp đen - UC-015 mốc 2 giờ" (SS06-BB2)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-BB2-FR | Fragment | sd Hộp đen UC-015 mốc trước giờ học | - | - | Khung sd của trang | 20 | 0 | 580 | 360 |
| SS06-BB2-L1 | Lifeline | :CancelUnderBookedClassHandler | «control» | - | DC-CancelUnderBookedClassHandler (PKG-15) | 100 | 40 | 120 | 300 |
| SS06-BB2-L2 | Lifeline | :IF-10 IScheduleMarkHandler | «interface» | - | Handler hiện thực; SS-06 gọi | 260 | 40 | 120 | 300 |
| SS06-BB2-L3 | Lifeline | :IF-06 IScheduler | «interface» | - | Subsystem SS-06 hiện thực | 420 | 40 | 120 | 300 |
| SS06-BB2-F1 | Fragment | loop [mỗi loại mốc phụ thuộc lớp: AbsenceCheck, WaitlistTransfer (Q-64)] | - | - | - | 70 | 170 | 500 | 130 |
| SS06-BB2-F2 | Fragment | alt [huỷ xong] | - | SS06-BB2-F1 | đường ngăn SS06-BB2-F2-O2-SEP nét đứt tại y=260 | 80 | 220 | 480 | 70 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS06-BB2-F2 toán hạng 2: [lỗi lưu trữ].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-BB2-M01 | 1 | SS06-BB2-L3 | SS06-BB2-L2 | handleMarkDue(ClassCutoff, classRef, dueAt) | Bất đồng bộ | - | UC-015 bước 1; handleMarkDue |
| SS06-BB2-M02 | 2 | SS06-BB2-L2 | SS06-BB2-L1 | handleClassCutoff(classRef) | Đồng bộ | - | UC-015 bước 1 đến 7 |
| SS06-BB2-M03 | 3 | SS06-BB2-L1 | SS06-BB2-L3 | cancelMark(kind, classRef) | Đồng bộ | SS06-BB2-F1 | UC-015 bước 4; cancelMark (Q-64) |
| SS06-BB2-M04 | 4 | SS06-BB2-L3 | SS06-BB2-L1 | đã huỷ mốc | Trả về | SS06-BB2-F2 (toán hạng 1) | UC-015 bước 4 |
| SS06-BB2-M05 | 5 | SS06-BB2-L3 | SS06-BB2-L1 | MarkStoreUnavailable | Trả về | SS06-BB2-F2 (toán hạng 2) | UC-015 bước 4; Q-102 |

### Trang "Hộp trắng - scheduleMark" (SS06-WB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-WB1-FR | Fragment | sd scheduleMark | - | - | Khung sd của trang | 20 | 0 | 580 | 520 |
| SS06-WB1-L1 | Lifeline | :DurableSchedulerFacade | «facade» | SS-06 | DC-DurableSchedulerFacade; hiện thực IF-06 | 100 | 40 | 120 | 460 |
| SS06-WB1-L2 | Lifeline | :MarkStore | «store» | SS-06 | DC-MarkStore | 260 | 40 | 120 | 460 |
| SS06-WB1-L3 | Lifeline | :DataStoreAccess | «store» | PKG-20 | DC-DataStoreAccess (PKG-20), ngoài subsystem | 420 | 40 | 120 | 460 |
| SS06-WB1-FR-G1 | Gate | scheduleMark | - | SS06-WB1-FR | Gate vào khung, message STT 1 | 15 | 115 | 10 | 10 |
| SS06-WB1-FR-G6 | Gate | đã lưu mốc | - | SS06-WB1-FR | Gate ra khung, message STT 6 | 15 | 315 | 10 | 10 |
| SS06-WB1-FR-G9 | Gate | MarkStoreUnavailable | - | SS06-WB1-FR | Gate ra khung, message STT 9 | 15 | 435 | 10 | 10 |
| SS06-WB1-F1 | Fragment | alt [ghi thành công] | - | - | đường ngăn SS06-WB1-F1-O2-SEP nét đứt tại y=340 | 80 | 220 | 480 | 230 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS06-WB1-F1 toán hạng 2: [CSDL lỗi].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-WB1-M01 | 1 | SS06-WB1-FR-G1 | SS06-WB1-L1 | scheduleMark(kind, subjectRef, dueAt) | Đồng bộ | - | scheduleMark; UC-005 bước 9 |
| SS06-WB1-M02 | 2 | SS06-WB1-L1 | SS06-WB1-L2 | saveMark(kind, subjectRef, dueAt) | Đồng bộ | - | scheduleMark |
| SS06-WB1-M03 | 3 | SS06-WB1-L2 | SS06-WB1-L3 | upsert(markRecord) | Đồng bộ | - | scheduleMark |
| SS06-WB1-M04 | 4 | SS06-WB1-L3 | SS06-WB1-L2 | đã ghi | Trả về | SS06-WB1-F1 (toán hạng 1) | scheduleMark |
| SS06-WB1-M05 | 5 | SS06-WB1-L2 | SS06-WB1-L1 | đã lưu | Trả về | SS06-WB1-F1 (toán hạng 1) | scheduleMark |
| SS06-WB1-M06 | 6 | SS06-WB1-L1 | SS06-WB1-FR-G6 | đã lưu mốc | Trả về | SS06-WB1-F1 (toán hạng 1) | scheduleMark |
| SS06-WB1-M07 | 7 | SS06-WB1-L3 | SS06-WB1-L2 | DataStoreError | Trả về | SS06-WB1-F1 (toán hạng 2) | scheduleMark |
| SS06-WB1-M08 | 8 | SS06-WB1-L2 | SS06-WB1-L1 | MarkStoreUnavailable | Trả về | SS06-WB1-F1 (toán hạng 2) | scheduleMark; Q-102 |
| SS06-WB1-M09 | 9 | SS06-WB1-L1 | SS06-WB1-FR-G9 | MarkStoreUnavailable | Trả về | SS06-WB1-F1 (toán hạng 2) | scheduleMark; Q-102 |

### Trang "Hộp trắng - cancelMark" (SS06-WB2)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-WB2-FR | Fragment | sd cancelMark | - | - | Khung sd của trang | 20 | 0 | 580 | 520 |
| SS06-WB2-L1 | Lifeline | :DurableSchedulerFacade | «facade» | SS-06 | DC-DurableSchedulerFacade; hiện thực IF-06 | 100 | 40 | 120 | 460 |
| SS06-WB2-L2 | Lifeline | :MarkStore | «store» | SS-06 | DC-MarkStore | 260 | 40 | 120 | 460 |
| SS06-WB2-L3 | Lifeline | :DataStoreAccess | «store» | PKG-20 | DC-DataStoreAccess (PKG-20), ngoài subsystem | 420 | 40 | 120 | 460 |
| SS06-WB2-FR-G1 | Gate | cancelMark | - | SS06-WB2-FR | Gate vào khung, message STT 1 | 15 | 115 | 10 | 10 |
| SS06-WB2-FR-G6 | Gate | đã huỷ mốc | - | SS06-WB2-FR | Gate ra khung, message STT 6 | 15 | 315 | 10 | 10 |
| SS06-WB2-FR-G9 | Gate | MarkStoreUnavailable | - | SS06-WB2-FR | Gate ra khung, message STT 9 | 15 | 435 | 10 | 10 |
| SS06-WB2-F1 | Fragment | alt [xoá thành công] | - | - | đường ngăn SS06-WB2-F1-O2-SEP nét đứt tại y=340 | 80 | 220 | 480 | 230 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS06-WB2-F1 toán hạng 2: [CSDL lỗi].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-WB2-M01 | 1 | SS06-WB2-FR-G1 | SS06-WB2-L1 | cancelMark(kind, subjectRef) | Đồng bộ | - | cancelMark; UC-005 bước 10, UC-015 bước 4 |
| SS06-WB2-M02 | 2 | SS06-WB2-L1 | SS06-WB2-L2 | removePendingMarks(kind, subjectRef) | Đồng bộ | - | cancelMark |
| SS06-WB2-M03 | 3 | SS06-WB2-L2 | SS06-WB2-L3 | deletePending(kind, subjectRef) | Đồng bộ | - | cancelMark |
| SS06-WB2-M04 | 4 | SS06-WB2-L3 | SS06-WB2-L2 | đã xoá | Trả về | SS06-WB2-F1 (toán hạng 1) | cancelMark |
| SS06-WB2-M05 | 5 | SS06-WB2-L2 | SS06-WB2-L1 | đã huỷ | Trả về | SS06-WB2-F1 (toán hạng 1) | cancelMark |
| SS06-WB2-M06 | 6 | SS06-WB2-L1 | SS06-WB2-FR-G6 | đã huỷ mốc | Trả về | SS06-WB2-F1 (toán hạng 1) | cancelMark |
| SS06-WB2-M07 | 7 | SS06-WB2-L3 | SS06-WB2-L2 | DataStoreError | Trả về | SS06-WB2-F1 (toán hạng 2) | cancelMark |
| SS06-WB2-M08 | 8 | SS06-WB2-L2 | SS06-WB2-L1 | MarkStoreUnavailable | Trả về | SS06-WB2-F1 (toán hạng 2) | cancelMark; Q-102 |
| SS06-WB2-M09 | 9 | SS06-WB2-L1 | SS06-WB2-FR-G9 | MarkStoreUnavailable | Trả về | SS06-WB2-F1 (toán hạng 2) | cancelMark; Q-102 |

### Trang "Hộp trắng - handleMarkDue" (SS06-WB3)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS06-WB3-FR | Fragment | sd handleMarkDue | - | - | Khung sd của trang | 20 | 0 | 900 | 640 |
| SS06-WB3-L1 | Lifeline | :DurableSchedulerFacade | «facade» | SS-06 | DC-DurableSchedulerFacade; hiện thực IF-06 | 100 | 40 | 120 | 580 |
| SS06-WB3-L2 | Lifeline | :MarkPoller | «facade» | SS-06 | DC-MarkPoller | 260 | 40 | 120 | 580 |
| SS06-WB3-L3 | Lifeline | :MarkStore | «store» | SS-06 | DC-MarkStore | 420 | 40 | 120 | 580 |
| SS06-WB3-L4 | Lifeline | :DataStoreAccess | «store» | PKG-20 | DC-DataStoreAccess (PKG-20), ngoài subsystem | 580 | 40 | 120 | 580 |
| SS06-WB3-L5 | Actor | Bộ định thời (ACT-13, ACT-14) | «actor» | - | Tác nhân thời gian | 740 | 40 | 120 | 580 |
| SS06-WB3-FR-G8 | Gate | handleMarkDue | - | SS06-WB3-FR | Gate ra khung, message STT 8 | 15 | 395 | 10 | 10 |
| SS06-WB3-FR-G9 | Gate | đã xử lý | - | SS06-WB3-FR | Gate vào khung, message STT 9 | 15 | 435 | 10 | 10 |
| SS06-WB3-FR-G11 | Gate | MarkHandlingFailed | - | SS06-WB3-FR | Gate vào khung, message STT 11 | 15 | 515 | 10 | 10 |
| SS06-WB3-F1 | Fragment | loop [mỗi mốc đã nhận] | - | - | - | 70 | 290 | 500 | 290 |
| SS06-WB3-F2 | Fragment | alt [handler xử lý xong] | - | SS06-WB3-F1 | đường ngăn SS06-WB3-F2-O2-SEP nét đứt tại y=500 | 240 | 420 | 320 | 150 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS06-WB3-F2 toán hạng 2: [handler báo lỗi hoặc quá 60 giây].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS06-WB3-M01 | 1 | SS06-WB3-L5 | SS06-WB3-L2 | tick (mỗi 10 giây) | Bất đồng bộ | - | handleMarkDue; UC-005 luồng 9a, UC-015 bước 1 |
| SS06-WB3-M02 | 2 | SS06-WB3-L2 | SS06-WB3-L3 | claimDueMarks(now) | Đồng bộ | - | handleMarkDue |
| SS06-WB3-M03 | 3 | SS06-WB3-L3 | SS06-WB3-L4 | claimDue(now, claimerId) | Đồng bộ | - | handleMarkDue; mỗi mốc chỉ một bản chạy nhận |
| SS06-WB3-M04 | 4 | SS06-WB3-L4 | SS06-WB3-L3 | dueMarks | Trả về | - | handleMarkDue |
| SS06-WB3-M05 | 5 | SS06-WB3-L3 | SS06-WB3-L2 | dueMarks | Trả về | - | handleMarkDue |
| SS06-WB3-M06 | 6 | SS06-WB3-L2 | SS06-WB3-L1 | handlerFor(kind) | Đồng bộ | SS06-WB3-F1 | handleMarkDue |
| SS06-WB3-M07 | 7 | SS06-WB3-L1 | SS06-WB3-L2 | handler | Trả về | SS06-WB3-F1 | handleMarkDue |
| SS06-WB3-M08 | 8 | SS06-WB3-L2 | SS06-WB3-FR-G8 | handleMarkDue(kind, subjectRef, dueAt) | Đồng bộ | SS06-WB3-F1 | handleMarkDue (IF-10); timeout 60 giây |
| SS06-WB3-M09 | 9 | SS06-WB3-FR-G9 | SS06-WB3-L2 | đã xử lý | Trả về | SS06-WB3-F2 (toán hạng 1) | handleMarkDue |
| SS06-WB3-M10 | 10 | SS06-WB3-L2 | SS06-WB3-L3 | markDone(mark) | Đồng bộ | SS06-WB3-F2 (toán hạng 1) | handleMarkDue |
| SS06-WB3-M11 | 11 | SS06-WB3-FR-G11 | SS06-WB3-L2 | MarkHandlingFailed | Trả về | SS06-WB3-F2 (toán hạng 2) | handleMarkDue; Q-93 |
| SS06-WB3-M12 | 12 | SS06-WB3-L2 | SS06-WB3-L3 | releaseForRetry(mark) | Đồng bộ | SS06-WB3-F2 (toán hạng 2) | handleMarkDue; tối đa 3 lần, cách 1 phút |

Quy tắc ngữ nghĩa đã áp dụng: message mức thiết kế ghi chữ ký với đối số; message bất đồng bộ đầu mũi tên mở, nét liền (endArrow=open;endFill=0;html=1;); client chỉ gọi interface; không có message từ subsystem tới lớp giao diện người dùng; mỗi message đi qua khung sd có một gate riêng.

## F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-DurableSchedulerFacade | DurableSchedulerFacade | Điều phối | Hiện thực IF-06: nhận scheduleMark, cancelMark; giữ bảng handler theo loại mốc; chuyển start, stop cho MarkPoller | package-private | IF-06 |
| DC-MarkPoller | MarkPoller | Điều phối | Vòng quét mốc đến hạn mỗi 10 giây: nhận mốc qua MarkStore, gọi handler qua IF-10, đánh dấu hoàn tất hoặc giao lại | package-private | - |
| DC-MarkStore | MarkStore | Lưu trữ trong subsystem | Lưu bền mốc, nhận mốc đến hạn bằng cập nhật có điều kiện để mỗi mốc chỉ một bản chạy nhận, qua DC-DataStoreAccess của PKG-20 | package-private | - |
| DC-MarkKind | MarkKind (PKG-22) | Kiểu dữ liệu | PaymentDeadline (UC-005, BR-04), ClassCutoff (UC-015), AbsenceCheck (UC-016, Chờ P07), WaitlistTransfer (UC-013, Chờ P07) | public | - |
| DC-MarkStoreUnavailable | MarkStoreUnavailable (PKG-22) | Ngoại lệ | Không ghi hoặc xoá được mốc do lỗi kho dữ liệu | public | - |

b) Class diagram phần tử: trang "Phần tử" (SS06-EL). Tọa độ bảng Node là tuyệt đối trên trang; file .drawio ghi tọa độ của phần tử con tương đối theo khung subsystem. Kiểu dữ liệu và ngoại lệ ở F5 a không vẽ lại ở sơ đồ.

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-06 | Subsystem | SS-06 DurableScheduler | «subsystem» | - | Khung subsystem | 40 | 180 | 800 | 220 |
| IF-06 | Interface | IF-06 IScheduler | «interface» | PKG-22 | Interface subsystem cung cấp | 70 | 40 | 220 | 60 |
| IF-10 | Interface | IF-10 IScheduleMarkHandler | «interface» | PKG-22 | Interface gọi ngược; Handler hiện thực | 330 | 40 | 220 | 60 |
| DC-DurableSchedulerFacade | Class | DurableSchedulerFacade | «facade» | SS-06 | Điều phối; hiện thực IF-06 | 80 | 260 | 200 | 60 |
| DC-MarkPoller | Class | MarkPoller | «facade» | SS-06 | Điều phối nền (vòng quét mốc đến hạn) | 340 | 260 | 200 | 60 |
| DC-MarkStore | Class | MarkStore | «store» | SS-06 | Lưu trữ trong subsystem (kho mốc hẹn) | 600 | 260 | 200 | 60 |
| DC-DataStoreAccess | Class | DataStoreAccess | «store» | PKG-20 | Ngoài subsystem; public trong PKG-20 | 640 | 480 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS06-EL-E1 | DC-DurableSchedulerFacade | IF-06 | Realization | - | Facade hiện thực IF-06 | - |
| SS06-EL-E2 | DC-MarkPoller | IF-10 | Dependency | «use» | Poller gọi IF-10 khi mốc đến hạn | - |
| SS06-EL-E3 | DC-DurableSchedulerFacade | DC-MarkPoller | Dependency | «use» | Bật, tắt vòng quét; cung cấp bộ xử lý theo loại mốc | - |
| SS06-EL-E4 | DC-MarkPoller | DC-MarkStore | Dependency | «use» | Nhận và đánh dấu mốc | - |
| SS06-EL-E5 | DC-DurableSchedulerFacade | DC-MarkStore | Dependency | «use» | Lưu và huỷ mốc | (180,350); (660,350) |
| SS06-EL-E6 | DC-MarkStore | DC-DataStoreAccess | Dependency | «use» | Ghi mốc bền qua DC-DataStoreAccess | - |

c) Cơ chế kiến trúc áp dụng

| Cơ chế | Nguồn | Cách tích hợp |
|---|---|---|
| Bảo mật dữ liệu | P09 F7 | Mốc chỉ chứa loại mốc, mã đối tượng, thời điểm; không chứa dữ liệu cá nhân. |
| Giao dịch và xử lý lặp lại | P09 F7 (mỗi mốc chỉ một bản chạy nhận; mốc xử lý lặp lại được) | MarkStore nhận mốc bằng cập nhật có điều kiện trên bản ghi mốc; handler idempotent kiểm tra trạng thái đối tượng trước khi xử lý. |
| Ghi nhật ký | Thiết kế: P09 F7 không nêu | Ghi mốc đặt, huỷ, nhận, hoàn tất, giao lại và độ trễ so với dueAt; lý do: chưa chốt độ lệch cho phép (Q-93). |
| Cấu hình | Thiết kế: P09 F7 không nêu | Khoảng quét, thời hạn giữ quyền xử lý, số lần giao lại đọc từ cấu hình; lý do: điều chỉnh theo Q-93 mà không sửa mã. |

## F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-06 | IF-10 | Qua interface | Chuyển mốc đến hạn cho Application mà không phụ thuộc lớp trong Application (P09 F6 V4 a) | Ưu tiên |
| SS-06 | PKG-20 (DC-DataStoreAccess) | Vào package | Lưu mốc bền trong CSDL; chỉ PKG-20 truy cập CSDL (P09 F7, P10 F6 dòng PKG-22 --> PKG-20) | Dùng thận trọng |

Trang "Phụ thuộc" (SS06-DP)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-06 | SubsystemBox | SS-06 DurableScheduler | «subsystem» | - | Subsystem đang xét | 40 | 40 | 240 | 160 |
| IF-10 | Interface | IF-10 IScheduleMarkHandler | «interface» | PKG-22 | Interface gọi ngược | 420 | 40 | 240 | 60 |
| PKG-20 | Package | PKG-20 Persistence | - | PKG-03 Services | Chứa DC-DataStoreAccess | 420 | 140 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS06-DP-E1 | SS-06 | IF-10 | Dependency | «use» | Qua interface: chuyển mốc đến hạn cho Application | - |
| SS06-DP-E2 | SS-06 | PKG-20 | Dependency | «use» | Vào package: lưu mốc hẹn bền qua DC-DataStoreAccess | - |

## F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| scheduleMark | CSDL lỗi khi ghi mốc | Kỹ thuật tạm thời | DataStoreError | Không tự thử lại | MarkStoreUnavailable | Không có luồng P04 UC-005 khi không đặt được mốc hạn thanh toán; ghi Đề xuất sửa P04 | Q-102 |
| cancelMark | CSDL lỗi khi xoá mốc | Kỹ thuật tạm thời | DataStoreError | Không tự thử lại | MarkStoreUnavailable | Không có luồng P04 UC-005 bước 10, UC-015 bước 4 khi không huỷ được mốc; ghi Đề xuất sửa P04 | Q-102, Q-64 |
| cancelMark | Huỷ mốc đúng lúc mốc đã được nhận xử lý | Không rõ kết quả | Không thấy mốc chưa đến hạn | Không dừng handler đang chạy; handler idempotent kiểm tra trạng thái đối tượng | Hoàn tất bình thường | UC-005: kết quả thanh toán đến sát hạn, Q-14 | Q-14 |
| handleMarkDue | Handler báo lỗi hoặc quá 60 giây | Kỹ thuật tạm thời | MarkHandlingFailed | Nhả quyền xử lý, giao lại sau 1 phút, tối đa 3 lần; hết lần thì đặt trạng thái Lỗi và ghi nhật ký | - | Luồng 9a của UC-005 và bước 1 của UC-015 không thực hiện được; P04 không có luồng, ghi Đề xuất sửa P04 | Q-93, Q-102 |
| handleMarkDue | Nhiều bản chạy cùng thấy một mốc | Kỹ thuật tạm thời | Cập nhật có điều kiện không thành công | Bản chạy không nhận được bỏ qua mốc | - | Không áp dụng (P09 F7) | - |
| handleMarkDue | Mốc được xử lý trễ so với dueAt | Kỹ thuật tạm thời | So sánh thời điểm nhận với dueAt | Vẫn gọi handler, ghi độ trễ | - | 9a (UC-005), bước 1 (UC-015) | Q-93 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | IF-06: SS06-EL-E1 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt | IF-10: SS06-EL-E2 và trang Phụ thuộc |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Xem F5 a; DC-DataStoreAccess là phần tử public của PKG-20, ngoài subsystem |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt | scheduleMark: SS06-WB1; cancelMark: SS06-WB2; handleMarkDue (IF-10): SS06-WB3; registerMarkHandler, start, stop chỉ chuyển tiếp một bước ở DC-DurableSchedulerFacade (bảng handler, bật tắt MarkPoller) |

## Câu hỏi mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Vấn đề còn mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).
