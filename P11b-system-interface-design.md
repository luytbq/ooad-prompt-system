# P11b - Thiết kế giao diện hệ thống và thiết bị (System/Device Interface Design)

## 1. Mục đích

Bước này thiết kế giao diện giữa phần mềm và các hệ thống ngoài, thiết bị: với mỗi subsystem đã xác định ở P10, định nghĩa interface (operation, tham số, kết quả, ngoại lệ), thiết kế bên trong subsystem (phân bổ hành vi cho các phần tử, sequence diagram qua interface ở dạng hộp đen và hộp trắng, tài liệu hoá phần tử), mô tả phụ thuộc của subsystem, và quyết định mức thiết kế cho lỗi, timeout, thử lại, idempotency. Kết quả giúp phần còn lại của hệ thống chỉ phụ thuộc vào interface ổn định, còn chi tiết giao thức được che giấu và thay thế được.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md (HE_THONG_NGOAI), 00-Conventions.md | Có | Hệ thống ngoài, tài liệu API, luật chung |
| Đầu vào | P10-design-elements.md | Có | Bảng subsystem (SS, IF, trách nhiệm, phần tử che giấu), package |
| Đầu vào | P08-analysis-model.md | Có | Trách nhiệm của boundary giao diện hệ thống, thiết bị; entity được truyền qua interface |
| Đầu vào | P07-uc-analysis/*.md | Có | Message control gửi tới boundary hệ thống (thứ tự, dữ liệu, luồng lỗi) |
| Đầu vào | P04-uc-specs/ | Có | Luồng thay thế và ngoại lệ khi hệ thống ngoài lỗi |
| Đầu vào | P06-supplementary-spec.md | Có | NFR về thời gian phản hồi, sẵn sàng, bảo mật, nhất quán |
| Đầu vào | P09-architecture.md | Có | Layer, quy tắc phụ thuộc, định hướng giao tiếp ngoài |
| Đầu vào | Tài liệu API hoặc giao thức của hệ thống ngoài, thiết bị | Khi có | Ánh xạ operation sang lời gọi ngoài |
| Đầu ra | P11b-system-interfaces.md | Có | Interface, operation, thiết kế subsystem; khi tách theo subsystem thì là file chung (F8 và mục kiểm soát) |
| Đầu ra | P11b-system-interfaces/SS-nn-<slug>.md | Khi đầu ra dài | Mục F1-F7 của từng subsystem (xem [Format]) |
| Đầu ra | diagrams/P11b-subsystem-SS-nn.drawio | Có | Mỗi subsystem một file, nhiều trang |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, các file đầu vào và tài liệu API của hệ thống ngoài (nếu có). Mỗi file chỉ cần phần sau (khi chạy bằng agent, chỉ đọc các phần này, tìm theo tiêu đề và theo mã):

| Artifact | Phần cần dùng |
|---|---|
| P10-design-elements.md | F2 và bảng Interface gọi ngược, F4, F5 |
| P08-analysis-model.md | Dòng boundary nguồn của subsystem ở F3, các entity được truyền qua interface |
| P07-uc-analysis/*.md | Dòng bảng message có Từ hoặc Đến là boundary nguồn của subsystem; Câu hỏi mở, Giả định |
| P04-uc-specs/ | Luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị |
| P06-supplementary-spec.md | NFR nhóm Giao tiếp ngoài, Hiệu năng, Bảo mật, Sẵn sàng |
| P09-architecture.md | F6, F7 |

- Chạy một lần cho mọi subsystem trong bảng F2 của P10 (phạm vi "Tất cả"). Interface kho dữ liệu không thuộc P11b (P12 thiết kế). Subsystem không có boundary nguồn ở P08 lấy trách nhiệm từ cột Trách nhiệm của P10 F2 và message P07 tới package đó. Hệ thống có nhiều subsystem phức tạp có thể chạy lặp, mỗi lần một subsystem (placeholder PHAM_VI_SUBSYSTEM), ghi nối vào cùng file đầu ra với phiên bản tăng.
- Khi chạy lặp: trước khi chạy P12 cho một package, chạy P11b cho mọi subsystem có interface được package đó dùng. Thiếu chữ ký interface, P12 chỉ đặt được chữ ký tạm.

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| PHAM_VI_SUBSYSTEM | Có | Subsystem thiết kế trong lần chạy |
| TAI_LIEU_GIAO_TIEP | Tuỳ chọn | Tài liệu API, giao thức, đặc tả thiết bị |
| CHINH_SACH_LOI | Tuỳ chọn | Chính sách lỗi đã chốt (timeout, số lần thử lại, xử lý kết quả không rõ) |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được hồ sơ dự án (đặc biệt HE_THONG_NGOAI), 00-Conventions.md và các artifact đã chốt: P04-uc-specs/, P06, P07-uc-analysis/, P08, P09, P10. Tuân thủ 00-Conventions.md, đặc biệt C1, C3, C5, C7.

Subsystem cần thiết kế:
{{PH:PHAM_VI_SUBSYSTEM | Hướng dẫn: "Tất cả" hoặc danh sách mã SS trong P10 | Ví dụ: "Tất cả"; "SS-01 PaymentGateway" (giao đồ ăn); "SS-02 SmsNotification, SS-03 BarcodeScanner" (phòng khám, quản lý kho)}}

Tài liệu giao tiếp của hệ thống ngoài, thiết bị:
{{PH:TAI_LIEU_GIAO_TIEP | Hướng dẫn: [TUỲ CHỌN] tên file hoặc tóm tắt API, giao thức, định dạng thông điệp, mã lỗi; ghi "Không có" thì thiết kế ở mức interface, không ánh xạ chi tiết lời gọi ngoài | Ví dụ: "sms-api.pdf: gửi tin một chiều, trả mã trạng thái, giới hạn 10 tin mỗi giây" (phòng khám); "Máy quét mã vạch giả lập bàn phím, gửi mã kèm phím Enter" (quản lý kho)}}

Chính sách lỗi đã chốt:
{{PH:CHINH_SACH_LOI | Hướng dẫn: [TUỲ CHỌN] timeout, số lần thử lại, cách xử lý khi không biết giao dịch ngoài đã thành công hay chưa; ghi "Không có" thì suy từ NFR, thiếu căn cứ thì AI chọn giá trị kỹ thuật theo Conventions C1 mục 7 ("Thiết kế: <lý do>") | Ví dụ: "Timeout 30 giây, không tự thử lại giao dịch trừ tiền, tra cứu trạng thái trước khi báo lỗi" (giao đồ ăn); "Gửi SMS thử lại tối đa 3 lần, cách nhau 1 phút" (phòng khám)}}

[Role]
Bạn là nhà thiết kế phần mềm chuyên tích hợp hệ thống, thành thạo thiết kế subsystem và interface (xác định interface, định nghĩa operation, phân bổ hành vi trong subsystem, phụ thuộc subsystem), ký pháp UML 2.5.1 cho interface, realization, sequence diagram (gate, black-box, white-box), và các nguyên tắc tích hợp an toàn: timeout, thử lại có giới hạn, idempotency, xử lý kết quả không rõ, cô lập lỗi.

[Action]
A1. Xác nhận subsystem.
- Với mỗi subsystem trong phạm vi, đọc dòng tương ứng ở bảng subsystem của P10 và trách nhiệm của boundary nguồn trong P08.
- Liệt kê mọi use case có control gửi message tới boundary nguồn (từ P07), kèm message, dữ liệu truyền, luồng lỗi liên quan trong P04.
- Interface hoặc operation chỉ phục vụ use case chưa có P04, P07: không định nghĩa chữ ký. F2 ghi trạng thái "Chờ P07 UC-nnn"; F3 ghi một dòng trách nhiệm "// ..." lấy từ P10 F2, các cột còn lại ghi "Chờ P07"; ghi Đề xuất sửa artifact trước: chạy P04, P07 cho use case đó rồi chạy lại P11b cho subsystem này.

A2. Xác định interface.
- Lập tập interface ứng viên cho mọi subsystem trong phạm vi từ trách nhiệm của chúng.
- Tìm điểm giống nhau giữa các interface (cùng operation ở hai subsystem, operation của các vai trò khác nhau trong một subsystem). Tách interface khi hai nhóm client dùng hai nhóm operation khác nhau; gộp khi hai interface là một vai trò.
- Xác định phụ thuộc giữa các interface (kiểu dữ liệu, ngoại lệ dùng chung).
- Ánh xạ interface vào subsystem (realization). Giữ mã IF đã cấp ở P10; interface mới cấp mã tiếp theo.
- Đặt interface vào package theo P10. Package chứa interface ở cùng layer với subsystem hiện thực nó hoặc thấp hơn, không ở layer của control dùng nó, để realization không đi lên (P09 A5). Interface theo chiều ngược (listener do phía hệ thống cung cấp, thiết bị gọi vào) theo cùng quy tắc: interface đặt ở layer của subsystem thiết bị, lớp hiện thực ở layer trên.

A3. Định nghĩa operation.
- Mỗi trách nhiệm "// ..." của boundary nguồn trở thành một hoặc nhiều operation. Không thêm operation không phục vụ use case nào, trừ operation kỹ thuật cần cho chính sách lỗi (ví dụ tra cứu trạng thái giao dịch) và phải ghi lý do.
- Tên operation phản ánh kết quả (ví dụ authorizePayment, sendAppointmentReminder, readBarcode). Tham số và kết quả dùng kiểu của mô hình (entity, kiểu giá trị) hoặc kiểu dữ liệu chuẩn; không để lộ kiểu của giao thức ngoài (chuỗi JSON, mã HTTP) ra interface.
- Kiểu trong chữ ký dùng kiểu của ngôn ngữ trong CONG_NGHE khi đã chốt; chưa chốt thì dùng kiểu trung lập (String, Integer, Decimal, Boolean, Date, DateTime, Duration, List<T>).
- Kiểu giá trị dùng trong chữ ký interface ở layer dưới (tiền, mã tham chiếu thẻ, định danh) phải nằm ở package cùng layer với interface hoặc thấp hơn. Kiểu đó nằm ở package thuộc layer cao hơn layer của interface (theo thứ tự layer ở P09 F4) thì dùng kiểu chuẩn hoặc kiểu riêng của interface, và ghi Đề xuất sửa P10 chuyển kiểu đó xuống package kiểu dữ liệu dùng chung ở layer không cao hơn interface. Khi Domain là layer thấp nhất (P09 A4), entity và kiểu giá trị của Domain được dùng trực tiếp trong chữ ký.
- Với mỗi operation: tham số vào (tên, kiểu, ràng buộc), kết quả (kiểu, ý nghĩa), ngoại lệ hoặc kết quả lỗi (phân loại ở A5), tiền điều kiện, hậu điều kiện, đồng bộ hay bất đồng bộ, idempotent hay không.
- Thiết bị đẩy sự kiện vào hệ thống (máy quét, cảm biến): thiết kế thêm interface theo chiều ngược (listener) do phía hệ thống cung cấp, subsystem thiết bị gọi vào; ghi rõ ai cung cấp, ai dùng.

A4. Thiết kế bên trong subsystem.
- Phân bổ hành vi cho phần tử bên trong: một lớp điều phối (subsystem manager hoặc lớp hiện thực interface) nhận lời gọi; lớp giao tiếp (proxy, adapter) nói chuyện với hệ thống ngoài hoặc thiết bị; lớp chuyển đổi dữ liệu giữa kiểu mô hình và định dạng ngoài khi cần. Dùng lại phần tử có sẵn nếu hợp.
- Tích hợp các cơ chế kiến trúc liên quan theo P09 (ghi nhật ký, bảo mật, cấu hình).
- Vẽ sequence diagram hộp đen: control của use case --> interface (lifeline là interface), cho từng operation được dùng, kèm luồng lỗi.
- Vẽ sequence diagram hộp trắng: bên trong subsystem, bắt đầu từ gate nhận message tới lớp điều phối, qua các phần tử bên trong, tới tác nhân hệ thống ngoài hoặc thiết bị. Mỗi operation của interface có ít nhất một sơ đồ, trừ khi operation được hiện thực 1-1 bởi một lớp đơn giản (ghi rõ).
- Tài liệu hoá phần tử: class diagram các phần tử bên trong, quan hệ, lớp nào hiện thực interface.

A5. Thiết kế xử lý lỗi.
- Phân loại lỗi của mỗi operation: lỗi nghiệp vụ bị hệ thống ngoài từ chối (ví dụ thẻ không đủ số dư, số điện thoại không hợp lệ); lỗi kỹ thuật tạm thời (mất kết nối, quá tải); kết quả không rõ (timeout sau khi đã gửi yêu cầu); lỗi thiết bị (mất kết nối, dữ liệu đọc hỏng).
- Trước khi cấp Q mới, tìm câu hỏi cùng nội dung trong mục Câu hỏi mở của artifact đầu vào (P09, P10, P11a nếu đã có); có rồi thì trích mã cũ.
- Mỗi loại lỗi được ánh xạ tới luồng thay thế hoặc ngoại lệ trong P04. Nếu P04 không có luồng tương ứng, ghi Đề xuất sửa artifact trước (P04) và Q-nn, không tự tạo hành vi nghiệp vụ.
- Timeout kết nối, số lần và khoảng cách thử lại là tham số kỹ thuật: lấy từ CHINH_SACH_LOI, NFR hoặc TAI_LIEU_GIAO_TIEP; không có thì chọn giá trị theo Conventions C1 mục 7 và ghi "Thiết kế: <lý do>" (ví dụ suy từ NFR thời gian phản hồi toàn luồng, mặc định khuyến nghị của nhà cung cấp), không cần Q hay ASM. Thời hạn mà người dùng cảm nhận được (khách chờ kết quả thanh toán bao lâu thì báo lỗi) là giá trị nghiệp vụ: nguồn không nêu thì ghi Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN).
- Thử lại: chỉ tự thử lại operation idempotent hoặc được làm idempotent (khoá idempotency do hệ thống sinh, hệ thống ngoài hỗ trợ theo TAI_LIEU_GIAO_TIEP). Operation có tác dụng phụ tài chính không idempotent thì không tự thử lại; với kết quả không rõ, thiết kế bước tra cứu trạng thái hoặc đối soát nếu hệ thống ngoài hỗ trợ, nếu không thì ghi Q.
- Cô lập lỗi: ngoại lệ của giao thức ngoài không lọt ra khỏi subsystem; subsystem chuyển thành ngoại lệ hoặc kết quả của interface.
- Dữ liệu nhạy cảm (thẻ, mật khẩu, thông tin cá nhân) qua interface: nêu nguyên tắc bảo vệ theo NFR bảo mật, không thiết kế thuật toán mã hoá cụ thể khi NFR không yêu cầu.

A6. Mô tả phụ thuộc subsystem.
- Subsystem phụ thuộc subsystem khác thì phụ thuộc qua interface (ưu tiên). Subsystem phụ thuộc package (ví dụ package kiểu dữ liệu dùng chung, entity) thì dùng thận trọng, ghi lý do.
- Kiểm tra theo điểm kiểm tra ở F7.

A7. Tự kiểm tra theo [Target], xuất kết quả.

[Format]
Xuất file P11b-system-interfaces.md theo khung C5, tiêu đề "# P11b - Giao diện hệ thống và thiết bị - <Tên hệ thống>". Mỗi subsystem một mục cấp 2 "## SS-nn <Tên>", trong đó có các mục F1-F7. Mục tổng hợp F8 ở cuối.
Khi đầu ra dự kiến dài hơn khoảng 100 KB (thường từ 5 subsystem có sơ đồ hộp trắng trở lên), tách mỗi subsystem một file P11b-system-interfaces/SS-nn-<slug>.md theo khung C5 (tiêu đề "# P11b - SS-nn <Tên> - <Tên hệ thống>"), chứa F1-F7 của subsystem đó. File chung P11b-system-interfaces.md vẫn có, gồm bảng "Danh sách file subsystem" (| SS | File | Phiên bản |), F8 và các mục kiểm soát; Câu hỏi mở, Giả định của mọi subsystem ghi ở file chung để bước sau tìm mã ở một chỗ. Chạy lặp theo PHAM_VI_SUBSYSTEM thì chỉ ghi file của subsystem đó và cập nhật file chung. Bước sau (P12, X1) đọc file chung rồi file của các SS mà phạm vi dùng.

F1. Bối cảnh sử dụng
Bảng: | UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |

F2. Interface
Bảng: | IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
- Tên bắt đầu bằng I, phản ánh vai trò, không tên nhà cung cấp.
- Mức hợp lý: 1-7 operation mỗi interface. Trên khoảng 10 operation thì kiểm tra có thể tách theo nhóm client (nguyên tắc phân tách interface).
- Lỗi thường gặp: một interface chung "IExternalService" cho mọi hệ thống ngoài (quá lớn); mỗi operation một interface (quá nhỏ); tên interface theo công nghệ ("IRestClient").

F3. Operation (bảng lõi)
| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
- Operation: chữ ký đầy đủ theo NGON_NGU_TEN_PHAN_TU, ví dụ "authorizePayment(order: FoodOrder, card: PaymentCard): PaymentResult".
- Tham số vào: mỗi tham số một dòng (thẻ <br>) "tên: kiểu - ràng buộc".
- Kết quả: kiểu và ý nghĩa các giá trị, ví dụ "PaymentResult: status (Approved / Declined), transactionRef".
- Lỗi / ngoại lệ: tên ngoại lệ hoặc giá trị lỗi và loại (Nghiệp vụ / Kỹ thuật tạm thời / Không rõ kết quả / Thiết bị).
- Idempotent: Có / Không / Có với khoá idempotency.
- Timeout: giá trị và nguồn (NFR, CHINH_SACH_LOI, "Thiết kế: <lý do>", hoặc Q, ASM khi là giá trị nghiệp vụ).
Ví dụ đúng (phòng khám): | IF-02 | ISmsNotifier | Cổng SMS | sendReminder(appointment: Appointment): NotificationResult | appointment: Appointment - trạng thái Đã xác nhận | NotificationResult: status (Sent / Rejected), providerMessageId | InvalidPhoneNumber (Nghiệp vụ); ProviderUnavailable (Kỹ thuật tạm thời) | UC-006 | Lịch hẹn có số điện thoại | Có bản ghi gửi | Không | Có với khoá appointmentId + loại nhắc | 10 giây (Thiết kế: gửi SMS bất đồng bộ, không chặn người dùng; bằng mặc định khuyến nghị của cổng SMS) |
Ví dụ đúng (quản lý kho, thiết bị đẩy sự kiện): | IF-05 | IBarcodeListener | Máy quét mã vạch | onBarcodeScanned(code: Barcode): void | code: Barcode - chuỗi đã đọc | - | ScanError (Thiết bị) qua onScanError | UC-007 | Màn hình nhập kho đang mở | - | Bất đồng bộ | - | - |, ghi chú: interface do hệ thống cung cấp, subsystem thiết bị gọi vào.
Ví dụ sai: | IF-01 | IPayment | ... | post(url: String, body: String): int | ... | ... | Exception | (sai: lộ giao thức, kết quả là mã HTTP, ngoại lệ chung chung, không UC).

F4. Sequence diagram
Trong file diagrams/P11b-subsystem-SS-nn.drawio, mỗi sơ đồ một trang:
- Trang "Hộp đen - <operation hoặc UC>": lifeline control của use case, lifeline interface (nhãn ":IF-Tên", stereotype «interface»), có thể có entity cung cấp dữ liệu. Không vẽ phần bên trong subsystem. Luồng lỗi bằng fragment alt.
- Trang "Hộp trắng - <operation>": khung sd với tên operation; message đến từ gate bên trái khung (nhãn là tên operation); lifeline lớp điều phối, lớp giao tiếp, lớp chuyển đổi, tác nhân hệ thống ngoài hoặc thiết bị ở phải cùng; fragment alt cho lỗi, loop cho thử lại (nếu có), break cho kết quả không rõ khi dừng.
Bảng Node: | ID | Loại (Lifeline / Actor / Gate / Fragment) | Nhãn | Stereotype | Thuộc về | Ghi chú |
Bảng message: | STT | Từ | Đến | Message | Loại (Đồng bộ / Bất đồng bộ / Trả về / Tự gọi) | Fragment | Operation hoặc UC bước |
Quy tắc ngữ nghĩa UML: message ở mức thiết kế ghi chữ ký với đối số (khác mức phân tích); message bất đồng bộ đầu mũi tên mở, nét liền (style: endArrow=open;endFill=0;html=1;); gate là điểm trên khung sd, tên gate là tên message đi qua; client chỉ gọi interface, không gọi lớp bên trong subsystem; không có message từ subsystem tới lớp giao diện người dùng.
Mỗi message đi qua khung sd (vào hoặc ra, kể cả trả về và lời gọi interface chiều ngược) có một gate riêng, ID "<ID khung>-G<STT>", style ellipse;html=1; kích thước 10 x 10, đặt trên cạnh khung. Lifeline interface ghi ":IF-nn Tên". Lifeline control ghi ":<tên DC của P10>", mã AC ghi ở Ghi chú. STT đánh số phẳng 1, 2, 3 theo trục thời gian trong mỗi trang.
Bố cục: lifeline đặt ở y = 40, cách nhau 160 theo trục x, rộng 120; message đầu tiên ở y = 120, hai message cách nhau 40; toạ độ bội số 10; theo C7.3.

F5. Phần tử của subsystem
a) Bảng phần tử: | DC | Tên | Vai trò (Điều phối / Giao tiếp ngoài / Chuyển đổi dữ liệu / Lưu trữ trong subsystem / Kiểu dữ liệu / Ngoại lệ) | Trách nhiệm | Visibility (public cho interface và cho kiểu dữ liệu, ngoại lệ xuất hiện trong chữ ký interface; package-private cho phần tử còn lại) | Hiện thực IF |
   Mã DC cấp theo C3, P12 sẽ thiết kế chi tiết thuộc tính, phương thức nếu cần.
b) Class diagram phần tử: trang "Phần tử" trong file drawio. Bảng Node: | ID | Loại (Class / Interface / Subsystem) | Nhãn | Stereotype | Thuộc về (SS) | Ghi chú |; Bảng Edge: | ID | Nguồn | Đích | Loại quan hệ (Realization / Association / Dependency / Composition) | Nhãn / multiplicity | Ghi chú |.
   Quy tắc: subsystem hiện thực interface bằng realization (nét đứt, tam giác rỗng) theo dạng canonical, hoặc dạng elided (vòng tròn interface nối bằng đường liền) khi sơ đồ đông; lớp bên trong nằm trong khung subsystem.

F6. Phụ thuộc subsystem
Bảng: | Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
Trang "Phụ thuộc" trong file drawio: subsystem, interface, package, mũi tên phụ thuộc nét đứt đầu mở.

F7. Thiết kế xử lý lỗi và điểm kiểm tra
a) Bảng lỗi: | Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
   Ví dụ đúng (giao đồ ăn): authorizePayment | Timeout sau khi gửi | Không rõ kết quả | Hết thời gian chờ | Không thử lại; gọi queryPaymentStatus bằng khoá idempotency tối đa 1 lần | PaymentPending nếu vẫn chưa rõ | UC-013 5b | Q-11 (P04 chưa có luồng "chờ xác nhận thanh toán").
   Ví dụ sai: authorizePayment | Timeout | tự thử lại 3 lần (sai: có thể trừ tiền nhiều lần khi operation không idempotent).
b) Điểm kiểm tra (trả lời Đạt / Không đạt cho từng subsystem): mỗi interface subsystem cung cấp có quan hệ realization; mỗi interface subsystem dùng có quan hệ phụ thuộc; không phần tử bên trong subsystem nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface; mỗi operation có sơ đồ hộp trắng, hoặc được hiện thực bởi một lớp duy nhất theo ánh xạ 1-1 dễ thấy.

F8. Tổng hợp toàn hệ thống (cuối file)
- Bảng: | SS | IF | Số operation | UC dùng | Rủi ro chính |.
- Mục kiểm soát theo C5.

[Target]
1. Mọi subsystem trong phạm vi có ít nhất một interface; mọi interface có ít nhất một operation dùng bởi một UC, trừ interface ở trạng thái "Chờ P07 UC-nnn" có dòng Đề xuất sửa artifact trước (A1).
2. Mọi trách nhiệm của boundary nguồn (P08) được phủ bởi operation; không có operation không phục vụ UC, trừ operation kỹ thuật có lý do.
3. Operation có đủ tham số, kiểu, kết quả, lỗi, tiền và hậu điều kiện, đồng bộ, idempotent, timeout (có nguồn hoặc "Thiết kế: <lý do>"; Q, ASM chỉ cho giá trị nghiệp vụ); kiểu giá trị trong chữ ký không kéo layer dưới phụ thuộc layer trên.
4. Interface không để lộ kiểu và lỗi của giao thức ngoài.
5. Mỗi loại lỗi được ánh xạ tới luồng P04, hoặc có đề xuất sửa P04 và câu hỏi mở.
6. Không tự thử lại operation không idempotent có tác dụng phụ.
7. Có sequence hộp đen cho mỗi UC dùng subsystem và hộp trắng cho mỗi operation (hoặc lý do ánh xạ 1-1).
8. Client chỉ phụ thuộc interface; không phần tử bên trong subsystem nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface; phụ thuộc subsystem vào package có lý do.
9. Thiết bị đẩy sự kiện có interface chiều ngược, ghi rõ bên cung cấp và bên dùng.
10. Bảng mô hình và file .drawio khớp nhau, đạt C7.3.
11. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này | Ví dụ: "Mọi interface đặt trong package ExternalSystemInterfaces."; "Dùng lại interface IPaymentGateway đã có ở dự án khác, không đổi chữ ký."; "Không vẽ sơ đồ hộp trắng cho subsystem gửi email."}}
````

## 5. Ghi chú cho người dùng

- Nếu chưa có tài liệu API của hệ thống ngoài, vẫn chạy được: interface được thiết kế theo nhu cầu của use case, phần ánh xạ lời gọi ngoài để trống. Khi có tài liệu, chạy lại chỉ để bổ sung bên trong subsystem, interface không nên đổi.
- Câu hỏi mở về lỗi (timeout, kết quả không rõ) thường cho thấy đặc tả use case thiếu luồng ngoại lệ. Nên bổ sung P04 rồi chạy lại P07 của use case đó.
- Không để AI tự thử lại giao dịch tài chính. Nếu kết quả có dòng "thử lại" cho operation trừ tiền mà không có khoá idempotency, đó là lỗi thiết kế.
- Dùng độc lập: cần tối thiểu danh sách hệ thống ngoài, thiết bị kèm nhu cầu dịch vụ của từng use case (có thể viết tay thay cho P07, P10) và các luồng lỗi mong muốn.

## 6. Căn cứ

- Kruchten P., The Rational Unified Process: An Introduction, 3rd ed. (2003): thiết kế subsystem, interface, phân bổ hành vi và điểm kiểm tra subsystem.
- OMG, Unified Modeling Language 2.5.1 (2017): interface, realization, component, sequence diagram, gate, combined fragment.
- Martin R. C., Agile Software Development: Principles, Patterns, and Practices (2002): nguyên tắc phân tách interface, đảo phụ thuộc.
- Gamma E. và cộng sự, Design Patterns (1994): Adapter, Proxy, Facade cho lớp giao tiếp ngoài.
- Hohpe G., Woolf B., Enterprise Integration Patterns (2003): thông điệp, idempotent receiver, xử lý lỗi tích hợp.
- Nygard M., Release It!, 2nd ed. (2018): timeout, thử lại có giới hạn, cô lập lỗi.
- Fowler M., UML Distilled, 3rd ed. (2003): sequence diagram ở mức thiết kế.
