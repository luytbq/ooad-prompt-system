# P11b - SS-05 TurnstileAccess - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | SS-05 TurnstileAccess (package PKG-12 ExternalApi); lần chạy đầu cho mọi subsystem của P10 F2 |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102, ghi ở file chung P11b-system-interfaces.md); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-018 Vào chi nhánh | Cửa quay --> AC-C-EnterBranchHandler (DC-EnterBranchHandler) | SD1a STT 2 receiveScannedCode (ACT-12 vào boundary) và 2.1 handleEntryRequest (boundary vào control), bước 2 | Mã QR đọc được, chi nhánh của cửa quay, thời điểm quẹt (Q-67) | Thông điệp cửa quay không đọc được: P04 chưa có luồng (Q-67, Q-72) |
| UC-018 Vào chi nhánh | AC-C-EnterBranchHandler (DC-EnterBranchHandler) --> cửa quay | sendEntryResult: SD1b 2.1.3, 2.1.4; SD1c 2.1.5, 2.1.7; SD2a 2.1.1b; SD2b 2.1.1a.3, 2.1.1a.5; openDoor: SD1c 2.1.7.1 (bước 6, 7) | Kết quả cho phép hoặc không cho phép, quy tắc bị vi phạm (BR-15 đến BR-19) | 3a1a, 3a1b, 3b, 4a, 4b, 4c (từ chối, cách báo cho người quét: Q-70); cửa quay không nhận được kết quả: Q-72 |
| UC-018 Vào chi nhánh | Người quét (ACT-02, ACT-03) --> cửa quay | SD1a STT 1 scanQrCode (bước 1) | Mã QR trên ứng dụng hoặc vé | Không áp dụng: thao tác vật lý trên cửa quay, ngoài phần mềm (P10 F2) |

- Trong thiết kế, cửa quay chủ động gọi vào phần mềm qua API và nhận kết quả trong phản hồi (hồ sơ dự án: cửa quay "gửi mã QR đọc được tới phần mềm qua API và mở cửa theo kết quả trả về"). Vì vậy // receiveScannedCode, // sendEntryResult, // openDoor của AC-B-TurnstileDevice được phủ bởi IF-09.decideEntry và phản hồi của SS-05, không còn operation riêng trong IF-05.

## F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-05 | ITurnstileEndpoint | Điểm vào của cửa quay: bật, tắt nhận lượt quét và đăng ký bộ nhận lượt quét. | SS-05 TurnstileAccess | Bước khởi động tiến trình API (ngoài các package của mô hình) | PKG-12 ExternalApi |
| IF-09 | IEntryScanReceiver | Nhận lượt quét từ cửa quay (qua SS-05) và trả quyết định cho phép hoặc không cho phép. | DC-EnterBranchHandler (PKG-16); interface theo chiều ngược, phía hệ thống cung cấp, phía thiết bị dùng | SS-05 TurnstileAccess (thay mặt cửa quay) | PKG-16 BranchAccessService |

- Số operation: IF-05 có 3, IF-09 có 1.
- Ai cung cấp, ai dùng: IF-09 do hệ thống cung cấp (DC-EnterBranchHandler hiện thực), thiết bị dùng thông qua SS-05. IF-05 do SS-05 cung cấp, bước khởi động tiến trình API dùng.
- Layer: SS-05 ở PKG-12 (Presentation), IF-09 ở PKG-16 (Application) theo P10; lời gọi đi xuống và realization nằm trong PKG-16, không đi lên. Quy tắc "lớp hiện thực ở layer trên" của chiều ngược không áp dụng được cho Presentation (không có layer cao hơn), ghi ở Vấn đề còn mở.

## F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-05 | ITurnstileEndpoint | Cửa quay (ACT-12) | enableReceiving(): void | - | - | - | UC-018 (kỹ thuật) | Đã registerScanReceiver | SS-05 bắt đầu nhận yêu cầu của cửa quay | Đồng bộ | Có | - (không chờ hệ thống ngoài) |
| IF-05 | ITurnstileEndpoint | Cửa quay (ACT-12) | disableReceiving(): void | - | - | - | UC-018 (kỹ thuật) | - | SS-05 trả phản hồi lỗi cho mọi yêu cầu của cửa quay | Đồng bộ | Có | - (không chờ hệ thống ngoài) |
| IF-05 | ITurnstileEndpoint | Cửa quay (ACT-12) | registerScanReceiver(receiver: IEntryScanReceiver): void | receiver: IEntryScanReceiver - không rỗng | - | - | UC-018 (kỹ thuật) | Chưa enableReceiving hoặc đang tắt | Lượt quét sau đó được chuyển tới receiver | Đồng bộ | Có (đăng ký lại thay bộ nhận cũ) | - (không chờ hệ thống ngoài) |
| IF-09 | IEntryScanReceiver | Cửa quay (ACT-12) | decideEntry(code: string, turnstileBranch: string, scannedAt: Date): EntryDecision | code: string - mã QR đọc được, không rỗng (định dạng: Q-68)<br>turnstileBranch: string - chi nhánh của cửa quay (cách biết chi nhánh: Q-67)<br>scannedAt: Date - thời điểm quẹt (Q-67) | EntryDecision: permitted: boolean; denialReason: EntryDenialReason khi permitted = false (PackageNotValid theo BR-15, PackageOnHold theo BR-16, PackageNotForBranch theo BR-17, PassNotValidToday theo BR-18, PassNotForBranch theo BR-19, UnknownQrCode theo BR-15 và BR-18) | Từ chối theo quy tắc là kết quả Nghiệp vụ (permitted = false); EntryProcessingFailed (Kỹ thuật tạm thời) | UC-018 (bước 2 đến 7) | Cửa quay đã gửi lượt quét; receiver đã đăng ký | permitted = true: đã ghi nhận lượt quẹt (BR-20); permitted = false: lượt quẹt có ghi nhận hay không chờ Q-71 | Đồng bộ | Không (mỗi lần cho phép ghi một lượt quẹt; lượt gửi lặp: Q-86) | 1 giây (NFR-02; mốc đo chờ Q-41) |

- Ánh xạ trách nhiệm P08 của AC-B-TurnstileDevice: // receiveScannedCode --> IF-09.decideEntry (tham số vào); // sendEntryResult --> EntryDecision (kết quả trả về) và phản hồi cho cửa quay; // openDoor --> cửa quay mở cửa khi phản hồi là cho phép; // scanQrCode là thao tác vật lý ngoài phần mềm (P10 F2) nên không có operation.
- IF-05 gồm ba operation vòng đời theo P10 F2: chúng cần để nối bộ nhận lượt quét và bật, tắt điểm vào; không phục vụ riêng một bước của UC-018 nên ghi UC-018 (kỹ thuật).
- Nội dung thông điệp, giao thức và cách xác thực thiết bị của cửa quay chờ Q-67, Q-47, Q-89 và IF-07 (Chờ P07 UC-004); interface không mang các chi tiết đó.

## F4. Sequence diagram

File diagrams/P11b-subsystem-SS-05.drawio gồm 4 trang: "Hộp đen - UC-018 vào chi nhánh"; "Hộp trắng - nhận lượt quét (decideEntry)"; "Phần tử"; "Phụ thuộc". STT đánh số phẳng theo trục thời gian trong mỗi trang; tọa độ bảng Node là tuyệt đối. Gate nằm trên cạnh trái khung sd, tâm gate ở y của message nên x, y của gate lệch 5 so với bội số của 10 (xem Vấn đề còn mở).

### Trang "Hộp đen - UC-018 vào chi nhánh" (SS05-BB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS05-BB1-FR | Fragment | sd Hộp đen UC-018 vào chi nhánh | - | - | Khung sd của trang | 20 | 0 | 740 | 560 |
| SS05-BB1-L1 | Actor | Cửa quay (ACT-12) | «actor» | - | Thiết bị gọi vào phần mềm | 100 | 40 | 120 | 500 |
| SS05-BB1-L2 | Lifeline | :IF-05 ITurnstileEndpoint | «interface» | - | Subsystem SS-05 hiện thực | 260 | 40 | 120 | 500 |
| SS05-BB1-L3 | Lifeline | :IF-09 IEntryScanReceiver | «interface» | - | DC-EnterBranchHandler hiện thực; SS-05 gọi | 420 | 40 | 120 | 500 |
| SS05-BB1-L4 | Lifeline | :EnterBranchHandler | «control» | - | DC-EnterBranchHandler (PKG-16); lớp phân tích AC-C-EnterBranchHandler | 580 | 40 | 120 | 500 |
| SS05-BB1-F1 | Fragment | alt [lượt quét được cho phép] | - | - | đường ngăn SS05-BB1-F1-O2-SEP nét đứt tại y=300; đường ngăn SS05-BB1-F1-O3-SEP nét đứt tại y=380 | 240 | 220 | 480 | 230 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS05-BB1-F1 toán hạng 2: [lượt quét bị từ chối]; SS05-BB1-F1 toán hạng 3: [lỗi xử lý nội bộ].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS05-BB1-M01 | 1 | SS05-BB1-L1 | SS05-BB1-L2 | lượt quét (mã QR, chi nhánh, thời điểm quẹt) | Đồng bộ | - | UC-018 bước 1, 2 (thông điệp cửa quay: Q-67) |
| SS05-BB1-M02 | 2 | SS05-BB1-L2 | SS05-BB1-L3 | decideEntry(code, turnstileBranch, scannedAt) | Đồng bộ | - | UC-018 bước 2; decideEntry |
| SS05-BB1-M03 | 3 | SS05-BB1-L3 | SS05-BB1-L4 | handleEntryRequest(code, turnstileBranch, scannedAt) | Đồng bộ | - | UC-018 bước 2 đến 6 |
| SS05-BB1-M04 | 4 | SS05-BB1-L4 | SS05-BB1-L3 | EntryDecision (permitted = true) | Trả về | SS05-BB1-F1 (toán hạng 1) | UC-018 bước 6 |
| SS05-BB1-M05 | 5 | SS05-BB1-L3 | SS05-BB1-L2 | EntryDecision (permitted = true) | Trả về | SS05-BB1-F1 (toán hạng 1) | UC-018 bước 6, 7 |
| SS05-BB1-M06 | 6 | SS05-BB1-L4 | SS05-BB1-L3 | EntryDecision (permitted = false, denialReason) | Trả về | SS05-BB1-F1 (toán hạng 2) | UC-018 luồng 3a1a, 3a1b, 3b, 4a, 4b, 4c |
| SS05-BB1-M07 | 7 | SS05-BB1-L3 | SS05-BB1-L2 | EntryDecision (permitted = false, denialReason) | Trả về | SS05-BB1-F1 (toán hạng 2) | UC-018 luồng 3a1a, 3a1b, 3b, 4a, 4b, 4c |
| SS05-BB1-M08 | 8 | SS05-BB1-L4 | SS05-BB1-L3 | EntryProcessingFailed | Trả về | SS05-BB1-F1 (toán hạng 3) | Q-72 |
| SS05-BB1-M09 | 9 | SS05-BB1-L3 | SS05-BB1-L2 | EntryProcessingFailed | Trả về | SS05-BB1-F1 (toán hạng 3) | Q-72 |
| SS05-BB1-M10 | 10 | SS05-BB1-L2 | SS05-BB1-L1 | phản hồi cho cửa quay (cho phép / không cho phép / lỗi) | Trả về | - | UC-018 bước 6, 7 |

### Trang "Hộp trắng - nhận lượt quét (decideEntry)" (SS05-WB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS05-WB1-FR | Fragment | sd decideEntry | - | - | Khung sd của trang | 20 | 0 | 740 | 720 |
| SS05-WB1-L1 | Lifeline | :TurnstileEndpoint | «facade» | SS-05 | DC-TurnstileEndpoint; hiện thực IF-05 | 100 | 40 | 120 | 660 |
| SS05-WB1-L2 | Lifeline | :TurnstileMessageMapper | «mapper» | SS-05 | DC-TurnstileMessageMapper | 260 | 40 | 120 | 660 |
| SS05-WB1-L3 | Lifeline | :TurnstileApiAdapter | «adapter» | SS-05 | DC-TurnstileApiAdapter | 420 | 40 | 120 | 660 |
| SS05-WB1-L4 | Actor | Cửa quay (ACT-12) | «actor» | - | Thiết bị gọi vào phần mềm | 580 | 40 | 120 | 660 |
| SS05-WB1-FR-G5 | Gate | decideEntry | - | SS05-WB1-FR | Gate ra khung, message STT 5 | 15 | 275 | 10 | 10 |
| SS05-WB1-FR-G6 | Gate | EntryDecision | - | SS05-WB1-FR | Gate vào khung, message STT 6 | 15 | 315 | 10 | 10 |
| SS05-WB1-FR-G11 | Gate | EntryProcessingFailed | - | SS05-WB1-FR | Gate vào khung, message STT 11 | 15 | 515 | 10 | 10 |
| SS05-WB1-F1 | Fragment | alt [thông điệp hợp lệ và đã bật nhận] | - | - | đường ngăn SS05-WB1-F1-O2-SEP nét đứt tại y=620 | 70 | 210 | 660 | 450 |
| SS05-WB1-F2 | Fragment | alt [IF-09 trả quyết định] | - | SS05-WB1-F1 | đường ngăn SS05-WB1-F2-O2-SEP nét đứt tại y=500 | 80 | 300 | 640 | 310 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS05-WB1-F1 toán hạng 2: [thông điệp không đọc được hoặc chưa bật nhận]; SS05-WB1-F2 toán hạng 2: [IF-09 báo lỗi xử lý].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS05-WB1-M01 | 1 | SS05-WB1-L4 | SS05-WB1-L3 | scanRequest(message) | Đồng bộ | - | UC-018 bước 2 (thông điệp cửa quay: Q-67) |
| SS05-WB1-M02 | 2 | SS05-WB1-L3 | SS05-WB1-L2 | toScanSignal(message) | Đồng bộ | - | decideEntry |
| SS05-WB1-M03 | 3 | SS05-WB1-L2 | SS05-WB1-L3 | scanSignal | Trả về | - | decideEntry |
| SS05-WB1-M04 | 4 | SS05-WB1-L3 | SS05-WB1-L1 | handleScan(scanSignal) | Đồng bộ | SS05-WB1-F1 (toán hạng 1) | decideEntry |
| SS05-WB1-M05 | 5 | SS05-WB1-L1 | SS05-WB1-FR-G5 | decideEntry(code, turnstileBranch, scannedAt) | Đồng bộ | SS05-WB1-F1 (toán hạng 1) | decideEntry (IF-09); UC-018 bước 2 |
| SS05-WB1-M06 | 6 | SS05-WB1-FR-G6 | SS05-WB1-L1 | EntryDecision | Trả về | SS05-WB1-F2 (toán hạng 1) | decideEntry; UC-018 bước 6 |
| SS05-WB1-M07 | 7 | SS05-WB1-L1 | SS05-WB1-L3 | EntryDecision | Trả về | SS05-WB1-F2 (toán hạng 1) | decideEntry |
| SS05-WB1-M08 | 8 | SS05-WB1-L3 | SS05-WB1-L2 | toDeviceResponse(decision) | Đồng bộ | SS05-WB1-F2 (toán hạng 1) | decideEntry |
| SS05-WB1-M09 | 9 | SS05-WB1-L2 | SS05-WB1-L3 | deviceResponse | Trả về | SS05-WB1-F2 (toán hạng 1) | decideEntry |
| SS05-WB1-M10 | 10 | SS05-WB1-L3 | SS05-WB1-L4 | deviceResponse | Trả về | SS05-WB1-F2 (toán hạng 1) | UC-018 bước 6, 7 |
| SS05-WB1-M11 | 11 | SS05-WB1-FR-G11 | SS05-WB1-L1 | EntryProcessingFailed | Trả về | SS05-WB1-F2 (toán hạng 2) | decideEntry; Q-72 |
| SS05-WB1-M12 | 12 | SS05-WB1-L1 | SS05-WB1-L3 | EntryProcessingFailed | Trả về | SS05-WB1-F2 (toán hạng 2) | decideEntry; Q-72 |
| SS05-WB1-M13 | 13 | SS05-WB1-L3 | SS05-WB1-L4 | errorResponse | Trả về | SS05-WB1-F2 (toán hạng 2) | decideEntry; Q-72 |
| SS05-WB1-M14 | 14 | SS05-WB1-L3 | SS05-WB1-L4 | errorResponse | Trả về | SS05-WB1-F1 (toán hạng 2) | decideEntry; Q-67 |

Quy tắc ngữ nghĩa đã áp dụng: message mức thiết kế ghi chữ ký với đối số; message bất đồng bộ đầu mũi tên mở, nét liền (endArrow=open;endFill=0;html=1;); client chỉ gọi interface; không có message từ subsystem tới lớp giao diện người dùng; mỗi message đi qua khung sd có một gate riêng.

## F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-TurnstileEndpoint | TurnstileEndpoint | Điều phối | Hiện thực IF-05: giữ trạng thái bật, tắt và bộ nhận đã đăng ký; nhận tín hiệu quét từ Adapter và gọi IF-09; đo thời gian xử lý mỗi lượt quét để so với ngưỡng 1 giây (NFR-02) | package-private | IF-05 |
| DC-TurnstileApiAdapter | TurnstileApiAdapter | Giao tiếp ngoài | Điểm nhận yêu cầu API của cửa quay; trả phản hồi mở hoặc giữ đóng cửa hoặc phản hồi lỗi | package-private | - |
| DC-TurnstileMessageMapper | TurnstileMessageMapper | Chuyển đổi dữ liệu | Đổi thông điệp của cửa quay thành tín hiệu quét (mã QR, chi nhánh, thời điểm) và EntryDecision thành phản hồi cho cửa quay | package-private | - |
| DC-EntryDecision | EntryDecision (PKG-16) | Kiểu dữ liệu | permitted, denialReason; cùng package với IF-09 | public | - |
| DC-EntryDenialReason | EntryDenialReason (PKG-16) | Kiểu dữ liệu | Danh sách lý do từ chối theo BR-15 đến BR-19 | public | - |
| DC-EntryProcessingFailed | EntryProcessingFailed (PKG-16) | Ngoại lệ | Lỗi xử lý nội bộ khi quyết định lượt quét | public | - |

b) Class diagram phần tử: trang "Phần tử" (SS05-EL). Tọa độ bảng Node là tuyệt đối trên trang; file .drawio ghi tọa độ của phần tử con tương đối theo khung subsystem. Kiểu dữ liệu và ngoại lệ ở F5 a không vẽ lại ở sơ đồ.

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-05 | Subsystem | SS-05 TurnstileAccess | «subsystem» | - | Khung subsystem | 40 | 180 | 800 | 200 |
| IF-09 | Interface | IF-09 IEntryScanReceiver | «interface» | PKG-16 | Interface gọi ngược; DC-EnterBranchHandler hiện thực | 300 | 40 | 240 | 60 |
| IF-05 | Interface | IF-05 ITurnstileEndpoint | «interface» | PKG-12 | Interface subsystem cung cấp | 580 | 40 | 240 | 60 |
| DC-TurnstileMessageMapper | Class | TurnstileMessageMapper | «mapper» | SS-05 | Chuyển đổi dữ liệu | 80 | 260 | 200 | 60 |
| DC-TurnstileApiAdapter | Class | TurnstileApiAdapter | «adapter» | SS-05 | Giao tiếp ngoài | 340 | 260 | 200 | 60 |
| DC-TurnstileEndpoint | Class | TurnstileEndpoint | «facade» | SS-05 | Điều phối; hiện thực IF-05 | 600 | 260 | 200 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS05-EL-E1 | DC-TurnstileEndpoint | IF-05 | Realization | - | Endpoint hiện thực IF-05 | - |
| SS05-EL-E2 | DC-TurnstileEndpoint | IF-09 | Dependency | «use» | Endpoint gọi IF-09 cho mỗi lượt quét | (640,130); (420,130) |
| SS05-EL-E3 | DC-TurnstileApiAdapter | DC-TurnstileMessageMapper | Dependency | «use» | Đọc và lập thông điệp của cửa quay | - |
| SS05-EL-E4 | DC-TurnstileApiAdapter | DC-TurnstileEndpoint | Dependency | «use» | Chuyển tín hiệu quét cho Endpoint | - |

c) Cơ chế kiến trúc áp dụng

| Cơ chế | Nguồn | Cách tích hợp |
|---|---|---|
| Bảo mật dữ liệu | P09 F7 (kênh mã hoá; xác thực thiết bị qua IF-07) | Lời gọi của cửa quay qua kênh mã hoá. Xác thực thiết bị gọi vào dùng IF-07, chữ ký Chờ P07 UC-004 nên chưa có bước xác thực trong sơ đồ. |
| Giao dịch và xử lý lặp lại | P09 F7 | Quyết định và ghi lượt quẹt do DC-EnterBranchHandler thực hiện trong IF-09; SS-05 không loại trùng lượt gửi lặp (Q-86). |
| Ghi nhật ký | Thiết kế: P09 F7 không nêu | Ghi mỗi lượt quét gồm chi nhánh, thời điểm nhận, thời gian xử lý, quyết định (không ghi nguyên mã QR); lý do: có căn cứ đo NFR-02 khi Q-41 chốt mốc đo. |
| Cấu hình | Thiết kế: P09 F7 không nêu | Chưa có lớp cấu hình riêng vì cách biết chi nhánh của cửa quay chưa rõ (Q-67); thêm khi Q-67 trả lời. |
| Không gọi hệ thống ngoài trong đường xử lý lượt quét | P09 F7 dòng ACT-12 (NFR-02) | SS-05 chỉ gọi IF-09; trong IF-09 không có lời gọi hệ thống ngoài. |

## F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-05 | IF-09 | Qua interface | Chuyển lượt quét cho Application mà không phụ thuộc lớp trong Application (P09 F6 V4) | Ưu tiên |
| SS-05 | IF-07 (SS-07) | Qua interface | Xác thực thiết bị gọi vào (P09 F6, P10 F2); chữ ký Chờ P07 UC-004 | Ưu tiên |

Trang "Phụ thuộc" (SS05-DP)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-05 | SubsystemBox | SS-05 TurnstileAccess | «subsystem» | - | Subsystem đang xét | 40 | 40 | 240 | 160 |
| IF-09 | Interface | IF-09 IEntryScanReceiver | «interface» | PKG-16 | Interface gọi ngược | 420 | 40 | 240 | 60 |
| IF-07 | Interface | IF-07 IAuthenticator | «interface» | PKG-21 | Chữ ký chờ P07 UC-004 | 420 | 140 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS05-DP-E1 | SS-05 | IF-09 | Dependency | «use» | Qua interface: chuyển lượt quét cho Application | - |
| SS05-DP-E2 | SS-05 | IF-07 | Dependency | «use» | Qua interface: xác thực thiết bị gọi vào (Chờ P07 UC-004) | - |

## F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| decideEntry | Thông điệp thiếu mã QR, chi nhánh hoặc thời điểm quẹt, hoặc không đọc được | Thiết bị | Mapper không đọc được thông điệp | Không gọi IF-09; trả phản hồi lỗi cho cửa quay | Phản hồi lỗi (không phải quyết định) | Không có luồng P04 cho thông điệp cửa quay hỏng; ghi Đề xuất sửa P04 | Q-67, Q-72 |
| decideEntry | Lượt quét bị từ chối theo quy tắc | Nghiệp vụ | EntryDecision.permitted = false | Chuyển nguyên quyết định thành phản hồi giữ đóng cửa | EntryDecision với denialReason | 3a1a, 3a1b, 3b, 4a, 4b, 4c | Q-70 |
| decideEntry | Lỗi xử lý nội bộ khi quyết định lượt quét | Kỹ thuật tạm thời | EntryProcessingFailed từ IF-09 | Trả phản hồi lỗi; không tự quyết định mở hay đóng | Phản hồi lỗi | Không có luồng P04 khi phần mềm lỗi lúc xử lý lượt quét; ghi Đề xuất sửa P04 | Q-72 |
| decideEntry | Xử lý lâu hơn 1 giây | Không rõ kết quả | Đo thời gian xử lý của SS-05 | Vẫn trả kết quả khi có; ghi nhật ký vượt ngưỡng; cửa quay có thể đã bỏ chờ | Như bình thường | Không có luồng P04 (NFR-02) | Q-41, Q-72 |
| decideEntry | Cửa quay gửi lặp cùng một lượt quét | Không rõ kết quả | Không phát hiện được (thông điệp chưa có mã yêu cầu của thiết bị) | Không loại trùng | Có thể ghi hai lượt quẹt | Bước 5 | Q-86, Q-67 |
| decideEntry | Cửa quay gọi vào khi chưa bật nhận hoặc chưa có bộ nhận | Kỹ thuật tạm thời | Trạng thái của TurnstileEndpoint | Không gọi IF-09; trả phản hồi lỗi | Phản hồi lỗi | Không có luồng P04 | Q-72 |
| decideEntry | Cửa quay mất kết nối với phần mềm | Thiết bị | Phần mềm không thấy yêu cầu (thiết bị là bên chủ động gọi) | Không phát hiện được từ phía phần mềm | - | Không có luồng P04; giám sát thiết bị không có trong nguồn | Q-72 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | IF-05: SS05-EL-E1 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Đạt | IF-09: SS05-EL-E2 và trang Phụ thuộc; IF-07: trang Phụ thuộc (chữ ký Chờ P07 UC-004) |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Xem F5 a |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt | decideEntry: SS05-WB1; enableReceiving, disableReceiving, registerScanReceiver hiện thực 1-1 bởi DC-TurnstileEndpoint (chỉ đổi trạng thái bật, tắt và giữ tham chiếu bộ nhận) |

## Câu hỏi mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Vấn đề còn mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).
