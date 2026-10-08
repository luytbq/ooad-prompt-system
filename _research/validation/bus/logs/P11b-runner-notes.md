# P11b - Nhật ký người chạy

Model: Sonnet (tham số model sonnet của công cụ Agent).

Phạm vi chạy: PHAM_VI_SUBSYSTEM = "Tất cả" (SS-01 đến SS-08 của P10), TAI_LIEU_GIAO_TIEP = Không có, CHINH_SACH_LOI = Không có, YEU_CAU_BO_SUNG = cấp Q mới từ Q-100 và ASM mới từ ASM-100. Đầu ra: P11b-system-interfaces.md (khoảng 204 KB) và tám file diagrams/P11b-subsystem-SS-01 đến SS-08.drawio (47 trang). Cách làm: viết một bộ sinh bằng Python giữ dữ liệu mô hình ở một chỗ, từ đó sinh cả bảng Node, Message, Edge trong .md lẫn file .drawio để hai dạng không lệch nhau. Chưa mở bằng draw.io, chỉ kiểm bằng phân tích cú pháp XML, bội số 10, khoảng cách tối thiểu 40 giữa node, và kiểm tra tự động cạnh không cắt node trên các trang Phần tử và Phụ thuộc.

## Vướng mắc

### 1. Phạm vi "mọi subsystem giao tiếp ngoài" mâu thuẫn với "Tất cả" và Target 1

- Vị trí: mục 3, "Chạy một lần cho mọi subsystem giao tiếp ngoài trong P10."; Target 1, "Mọi subsystem trong phạm vi có ít nhất một interface; mọi interface có ít nhất một operation dùng bởi một UC."; placeholder PHAM_VI_SUBSYSTEM ví dụ "Tất cả" hoặc danh sách mã SS.
- Gặp: P10 có 8 subsystem, trong đó SS-07 (ServerPersistence) và SS-08 (DeviceLocalPersistence) là lưu trữ, không giao tiếp ngoài; SS-05, SS-06 là cơ chế nội bộ. Không rõ "Tất cả" có gồm lưu trữ không. Các interface kho dữ liệu IF-10 đến IF-13 do Domain định nghĩa, P09 R6 giao P12 dùng, nhưng P10 lại để SS-07, SS-08 hiện thực nên có thể là việc của P11b.
- Xử lý: thiết kế cả tám subsystem. SS-07, SS-08 dùng hộp trắng rút gọn (chỉ saveTrip, saveCheckSession có trang hộp trắng, còn lại ánh xạ 1-1). Ghi lựa chọn vào Vấn đề còn mở. Chi phí lớn (SS-07 một mình 18 operation).

### 2. Quy tắc kiểu giá trị theo layer giả định Domain nằm trên Services

- Vị trí: A3, "Kiểu đó đang ở layer trên (ví dụ layer Domain) thì dùng kiểu chuẩn hoặc kiểu riêng của interface, và ghi Đề xuất sửa P10 tạo package kiểu dữ liệu dùng chung ở layer thấp."
- Gặp: P09 đặt Domain ở layer thấp nhất (thứ tự Presentation, Application, Services, Domain) để Persistence không phụ thuộc đi lên. Vậy kiểu Ticket, Trip, TripPassengerList nằm dưới layer Services, dùng trong chữ ký interface không vi phạm. Ví dụ trong prompt lại coi Domain là layer trên, nên quy tắc không áp dụng.
- Xử lý: dùng entity trong chữ ký IF-06, IF-09, IF-10 đến IF-13; dùng kiểu giá trị của PKG-28 (Money, TicketCode, PhoneNumber, PaymentReference) cho IF-01 đến IF-05 đúng như P10 đã làm, vì PKG-15, PKG-16, PKG-18 chỉ phụ thuộc PKG-28. Ghi lý do ở Vấn đề còn mở (Target 3).

### 3. Operation phục vụ UC chưa có đặc tả (UC-003, UC-005, IF-13)

- Vị trí: A3, "Không thêm operation không phục vụ use case nào, trừ operation kỹ thuật cần cho chính sách lỗi"; Target 1.
- Gặp: IF-02 IPaymentResultListener và nửa thanh toán của IF-01 chỉ phục vụ UC-003 (chưa có P04, P07). IF-06 printTicket chỉ có UC-005 (chưa có P04, P07). IF-13 chưa có UC nào. P08 chỉ có hai trách nhiệm hoàn tiền cho PaymentGateway, không có trách nhiệm thanh toán, nhưng P10 đã định nghĩa IF-02.
- Xử lý: thêm requestPayment và queryPaymentStatus ở trạng thái Tạm theo ASM-100 (dẫn NFR-06, P10 IF-02); printTicket theo NFR-09; IF-13 giữ hai operation giữ chỗ. Target 1 không đạt cho IF-13, IF-01 (phần thanh toán) và IF-02, ghi trong Vấn đề còn mở. Dùng ASM thay vì Q cho cách thanh toán vì chế độ là CO_NHAN.

### 4. Trách nhiệm của boundary nguồn không ánh xạ một-một sang operation

- Vị trí: A3, "Mỗi trách nhiệm "// ..." của boundary nguồn trở thành một hoặc nhiều operation."; Target 2.
- Gặp: P08 có hai trách nhiệm cho cổng thanh toán là // requestRefund và // returnRefundResult, nhưng ở mức thiết kế kết quả đi theo giá trị trả về (P07 có message trả về 2.1.2). Với đầu quét, // readBarcode thực chất là sự kiện đẩy vào (IF-05), không phải operation gọi ra. P08 SmsGateway // sendSms khớp một operation nhưng P07 dùng tên sendTicketSms, sendTripCancelSms.
- Xử lý: gộp requestRefund và returnRefundResult thành một operation requestRefund trả RefundResult; ánh xạ // readBarcode sang IF-05.receiveScannedCode; thêm Đề xuất sửa P08 và P10. Không rõ Target 2 có coi việc gộp là "phủ" hay không; đánh giá là phủ.

### 5. P10 thiếu operation cho interface thiết bị và nội dung F2 mâu thuẫn với P09

- Vị trí: A2, "Giữ mã IF đã cấp ở P10; interface mới cấp mã tiếp theo."; đầu vào P10 F2.
- Gặp: P10 chỉ cho IF-04 trách nhiệm "// readBarcode" và để việc "đăng ký bộ nhận" ở cột che giấu, nên chữ ký IF-04 thiếu operation bật đầu quét. P10 F2 ghi SS-05 "duyệt dữ liệu tìm mốc đến hạn" nhưng F4 để PKG-19 không phụ thuộc package nào, nên SS-05 không đọc được Booking. P10 mục Câu hỏi mở ghi "Không có" trong khi nhiều mục khác dẫn Q-54, Q-57, Q-75, Q-79. Phần gửi lại kết quả soát vé khi mất sóng hoàn tất sau khi use case kết thúc nên cần báo ngược lên PKG-11, P10 không có interface cho việc này.
- Xử lý: thêm startScanning, stopScanning (operation kỹ thuật, có lý do ở cột UC); cho SS-05 giữ kho mốc riêng (DC-TriggerStore) và ghi Đề xuất sửa P10, P09; cấp IF-14 IResultDeliveryListener mới. Mã IF mới là IF-14 (số lớn nhất là IF-13); không rõ P11a, P12 có cùng cấp IF-14 không.

### 6. "Không public, trừ interface" và các kiểu trong chữ ký interface

- Vị trí: F5a, "Visibility (không public, trừ interface)"; F7b, "không phần tử bên trong subsystem nào public".
- Gặp: kiểu kết quả (RefundResult, SmsResult), ngoại lệ (PaymentGatewayUnavailableException) phải public để client dùng, nhưng prompt không nêu chúng thuộc "interface" hay "bên trong".
- Xử lý: coi là thuộc chữ ký interface, ghi "public (thuộc chữ ký IF-nn)" ở cột Visibility; các lớp hiện thực để package-private; điểm kiểm tra F7b ghi Đạt kèm lời giải thích. Ghi vào Vấn đề còn mở (C9).

### 7. Danh sách vai trò của phần tử không có chỗ cho kho tạm và các phần tử khác

- Vị trí: F5a, "Vai trò (Điều phối / Giao tiếp ngoài / Chuyển đổi dữ liệu / Kiểu dữ liệu / Ngoại lệ)".
- Gặp: hàng đợi gửi lại kết quả soát vé (DC-ResultOutbox) và kho mốc (DC-TriggerStore) là kho bền; kho mốc xếp vào "Giao tiếp ngoài" cho gần, hàng đợi thì không xếp được; bộ gọi kết quả đến hạn (DC-TriggerDispatcher) cũng là điều phối thứ hai.
- Xử lý: thêm vai trò "Lưu tạm" cho DC-ResultOutbox, xếp DC-TriggerStore vào "Giao tiếp ngoài", DC-TriggerDispatcher vào "Điều phối". Ghi vào Vấn đề còn mở.

### 8. Chính sách thử lại phụ thuộc vào tài liệu API không có

- Vị trí: A5, "Thử lại: chỉ tự thử lại operation idempotent hoặc được làm idempotent (khoá idempotency do hệ thống sinh, hệ thống ngoài hỗ trợ theo TAI_LIEU_GIAO_TIEP)."; CHINH_SACH_LOI = Không có.
- Gặp: TAI_LIEU_GIAO_TIEP là Không có, cổng thanh toán chưa có tài liệu API (Q-24), nên không biết cổng có hỗ trợ khoá idempotency hay tra cứu trạng thái. Prompt cho phép thiết kế "bước tra cứu trạng thái hoặc đối soát nếu hệ thống ngoài hỗ trợ, nếu không thì ghi Q" nhưng không nói chế độ mặc định khi chưa biết.
- Xử lý: mặc định không tự thử lại mọi operation tài chính; thiết kế một lần tra cứu kèm khoá do hệ thống sinh và trả Unknown nếu vẫn chưa rõ; hỏi bằng Q-100 (cổng), Q-101 (SMS). Hệ quả: thiết kế phụ thuộc giả thiết cổng có tra cứu, ghi "nếu cổng hỗ trợ".

### 9. Ranh giới giữa tham số kỹ thuật và thời hạn người dùng cảm nhận được

- Vị trí: A5, "Thời hạn mà người dùng cảm nhận được (khách chờ kết quả thanh toán bao lâu thì báo lỗi) là giá trị nghiệp vụ: nguồn không nêu thì ghi Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN)."; C1 mục 7.
- Gặp: timeout đọc 30 giây của cổng vừa là tham số kỹ thuật vừa quyết định người dùng chờ bao lâu. Không có tiêu chí tách hai thứ.
- Xử lý: timeout kết nối, đọc, tra cứu là "Thiết kế: <lý do>"; tổng thời gian tối đa người dùng của UC-008, UC-013 chờ là 45 giây ghi ASM-101. Với thanh toán, giới hạn trên là hạn giữ chỗ 10 phút của BR-07 (nguồn nêu) nên không cần ASM riêng.

### 10. Tham chiếu tới P07 F10 mà người chạy không được đọc

- Vị trí: F4, "Bố cục theo P07 F10 (phần Sequence) (lifeline cách 160, message cách 40, toạ độ bội số 10) và C7.3."
- Gặp: phạm vi đọc không cho đọc prompt P07; chỉ có số liệu trong ngoặc. Không rõ y của message đầu tiên, cách vẽ fragment, độ cao nhãn.
- Xử lý: dùng 160, 40, bội 10 theo ngoặc; lấy y bắt đầu 120 từ cách các artifact P07 trong bus/design ghi ("message đầu tiên ở y=120"), chừa thêm 30 quanh fragment và đường ngăn toán hạng. Phụ thuộc chéo prompt khiến bước này không tự chứa đủ khi chạy độc lập.

### 11. Gate, callback và sơ đồ hộp trắng cho message đi ngược

- Vị trí: F4, "message đến từ gate bên trái khung (nhãn là tên operation)"; "gate là điểm trên khung sd, tên gate là tên message đi qua".
- Gặp: prompt chỉ mô tả message vào qua gate. Kết quả trả về, ngoại lệ, và các operation chiều ngược (IF-02, IF-05, IF-08, IF-14: message do subsystem gửi ra gate) không được nói. Với callback từ cổng thanh toán, message gốc đến từ tác nhân chứ không từ gate. Một gate dùng cho nhiều message (vào, trả về) khó vẽ ngang y của từng message.
- Xử lý: mỗi message đi qua khung có một ô gate riêng (cùng tên, ID đánh số thêm -2, -3); với callback, vẽ tác nhân --> lớp nhận --> gate ở khung (gate ra), và lớp nhận gọi ngược qua gate. Bảng Node ghi từng gate là một dòng Gate.

### 12. Nhãn lifeline interface và tên control trong sơ đồ hộp đen

- Vị trí: F4, "lifeline control của use case, lifeline interface (nhãn ":IF-Tên", stereotype «interface»)".
- Gặp: không nói ":IF-Tên" là ":IF-01 IPaymentGateway" hay ":IPaymentGateway"; không nói lifeline control dùng tên AC của P07 hay DC của P10 (hai tên khác nhau do P10 đổi hậu tố Controller thành Service). Với UC-005, UC-003 chưa có P07 nên chưa có tên DC.
- Xử lý: nhãn ":IF-01 IPaymentGateway"; control dùng tên DC của P10, ghi AC trong cột Ghi chú; UC-005 dùng lifeline control tạm ":Control của UC-005 (chưa có P07)".

### 13. Cột "Hệ thống/thiết bị" và "Client (DC, PKG)" cho trường hợp không phải hệ thống ngoài hoặc chưa có DC

- Vị trí: F3 cột "Hệ thống/thiết bị"; F2 cột "Client (DC, PKG)".
- Gặp: với SS-07, SS-08, hệ thống đối tác là CSDL (không thuộc HE_THONG_NGOAI); với IF-06 client là control của UC-005 chưa có DC; với IF-13 chưa có client.
- Xử lý: ghi "CSDL quan hệ (PostgreSQL)", "CSDL cục bộ (SQLite, Room)"; ghi "Chưa có (...)" cho client chưa tồn tại.

### 14. Class diagram phần tử và kiểu dữ liệu, ngoại lệ

- Vị trí: F5b, "Class diagram phần tử: trang "Phần tử" trong file drawio."
- Gặp: không nói có vẽ kiểu dữ liệu, ngoại lệ lên class diagram không. Vẽ hết khiến nhiều node không có cạnh hoặc cạnh dài băng qua hàng khác.
- Xử lý: trang Phần tử chỉ vẽ interface, lớp điều phối, giao tiếp ngoài, chuyển đổi, tác nhân; kiểu dữ liệu và ngoại lệ chỉ có trong bảng F5a (ghi chú trong bảng). Ranh giới này do người chạy chọn.

### 15. Ranh giới giao dịch khi có lời gọi hệ thống ngoài giữa hai lần ghi

- Vị trí: không có trong prompt; P09 F7 ghi "Mỗi lần đặt, phát hành vé, trả vé, huỷ chuyến là một giao dịch ACID".
- Gặp: UC-013 gọi cổng hoàn tiền (bước 7) giữa huỷ chuyến (bước 5) và ghi khoản hoàn (bước 9); không thể giữ một giao dịch qua lời gọi ngoài. Prompt P11b không có hướng dẫn cho tình huống này.
- Xử lý: tách thành saveTripCancellation (bước 5) và saveTicket cho từng khoản hoàn (bước 9), ghi ở cột UC của IF-11. Chưa chắc phù hợp với ý P09 "một giao dịch" cho huỷ chuyến; ghi vào Đề xuất sửa.

### 16. Cấp mã Q, ASM khi có bước khác chạy song song

- Vị trí: C3, "tìm mã Q và ASM lớn nhất đã thấy, rồi cấp tiếp từ số đó."; YEU_CAU_BO_SUNG "cấp mã Q mới từ Q-100 và ASM mới từ ASM-100".
- Gặp: các đầu vào có Q lớn nhất Q-83 và ASM lớn nhất ASM-58, nên có khoảng trống Q-84 đến Q-99 và ASM-59 đến ASM-99 (C3 coi mã "chỉ trỏ tới một câu hỏi duy nhất" nên không vi phạm, nhưng lệch quy tắc "cấp tiếp"). Nếu P11a cũng được dặn bắt đầu từ cùng số, hai bước sẽ trùng mã. Người chạy P11b không biết dải số của P11a.
- Xử lý: dùng Q-100 đến Q-107, ASM-100 đến ASM-101 theo YEU_CAU_BO_SUNG (C9: yêu cầu bổ sung ưu tiên hơn quy ước chung).

### 17. Quá tải ngữ cảnh

- Vị trí: mục 3, "Đính kèm: 00-Conventions.md, project-profile.md, các file đầu vào".
- Gặp: đầu vào gồm khoảng 416 KB (P07 bốn file khoảng 270 KB, P08 77 KB, P09 54 KB, P10 60 KB, P04 bốn file), vượt khả năng đọc nguyên văn. Không đọc hết P07 mà chỉ đọc bảng message của các boundary hệ thống, thiết bị và các mục Câu hỏi mở, Giả định, Đề xuất sửa; P04 chỉ đọc các luồng liên quan; P06 chỉ đọc mục Giao tiếp ngoài và các Q liên quan; P09 đọc F3, F6, F7, F8. Có thể bỏ sót chi tiết ở phần không đọc.
- Xử lý: đọc có chọn lọc bằng grep và đọc đoạn; mục 3 của prompt không nêu "chỉ cần các dòng nào" như P04 (README mục 8 nói P04 có bảng trích đoạn, P11b thì không). Đề nghị bổ sung bảng trích đoạn cần đọc cho P11b.

### 18. Đánh số message trong sequence diagram thiết kế

- Vị trí: F4, "Bảng message: | STT | Từ | Đến | Message | Loại ... | Fragment | Operation hoặc UC bước |".
- Gặp: không nói STT là số thứ tự phẳng hay đánh số thập phân phân cấp (kiểu P07: 1.1.1); ở thiết kế có lồng lời gọi nên khó chọn.
- Xử lý: dùng số thứ tự phẳng 1, 2, 3 theo trục thời gian; thêm cột ID đầu bảng (ID cell trong .drawio).

## Mục Target không đạt hoặc đạt một phần

- Target 1: không đạt cho IF-13 (chưa có UC dùng), IF-01 phần thanh toán và IF-02 (chỉ UC-003 chưa có đặc tả, Tạm theo ASM-100). Đạt cho các interface còn lại.
- Target 2: đạt một phần. Trách nhiệm thanh toán của AC-B-PaymentGateway chờ P07 của UC-003. Operation kỹ thuật (startScanning, stopScanning, queryRefundStatus, queryPaymentStatus, findPendingCheckSessions...) có lý do ở cột UC.
- Target 3: đạt, kèm lưu ý về quy tắc layer (mục 2) và timeout có nguồn "Thiết kế: <lý do>"; chỉ ASM-101 là giá trị nghiệp vụ.
- Target 5: đạt một phần. Lỗi kết quả không rõ (hoàn tiền, thanh toán), lỗi thiết bị (máy in, đầu quét), lỗi kỹ thuật nội bộ, lỗi lưu cục bộ không có luồng P04; đã ghi Đề xuất sửa P04 và Q-55 (đã có), Q-100 đến Q-107.
- Target 7: đạt một phần. SS-07 (trừ saveTrip), SS-08 (trừ saveCheckSession), queryPaymentStatus, stopScanning dùng ánh xạ 1-1 đã ghi rõ; hộp đen UC-003, UC-005 dùng control tạm vì chưa có P07.
- Target 10: đạt một phần. Sequence diagram để fragment phủ lifeline và message đi qua lifeline ở giữa theo UML, không thoả hết "cạnh không cắt qua node" của C7.3. Trang Phần tử và Phụ thuộc đạt (kiểm tự động). Chưa mở bằng draw.io để xem nhãn và nét vẽ.
- Các Target 4, 6, 8, 9, 11: đạt (Target 6: không operation tài chính nào tự thử lại; Target 9: IF-05, IF-08, IF-02, IF-14 là chiều ngược, ghi bên cung cấp và bên dùng).
