# P11b - Giao diện hệ thống và thiết bị - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | Tất cả subsystem của P10 F2 (SS-01 đến SS-07), lần chạy đầu; SS-07 chờ P07 UC-004. Đầu ra tách mỗi subsystem một file vì dự kiến vượt khoảng 100 KB |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## Danh sách file subsystem

| SS | File | Phiên bản |
|---|---|---|
| SS-01 OnlinePayment | P11b-system-interfaces/SS-01-online-payment.md (sơ đồ: diagrams/P11b-subsystem-SS-01.drawio) | 1.0 |
| SS-02 EInvoiceSubmission | P11b-system-interfaces/SS-02-einvoice-submission.md (sơ đồ: diagrams/P11b-subsystem-SS-02.drawio) | 1.0 |
| SS-03 PushNotification | P11b-system-interfaces/SS-03-push-notification.md (sơ đồ: diagrams/P11b-subsystem-SS-03.drawio) | 1.0 |
| SS-04 SmsMessaging | P11b-system-interfaces/SS-04-sms-messaging.md (sơ đồ: diagrams/P11b-subsystem-SS-04.drawio) | 1.0 |
| SS-05 TurnstileAccess | P11b-system-interfaces/SS-05-turnstile-access.md (sơ đồ: diagrams/P11b-subsystem-SS-05.drawio) | 1.0 |
| SS-06 DurableScheduler | P11b-system-interfaces/SS-06-durable-scheduler.md (sơ đồ: diagrams/P11b-subsystem-SS-06.drawio) | 1.0 |
| SS-07 Authentication | P11b-system-interfaces/SS-07-authentication.md (sơ đồ: diagrams/P11b-subsystem-SS-07.drawio) | 1.0 |

Bước sau (P12, X1) đọc file chung này rồi file của các SS mà phạm vi dùng. Bảng Interface gọi ngược của P10 (IF-08, IF-09, IF-10) có chữ ký ở file của subsystem gọi: IF-08 ở SS-01, IF-09 ở SS-05, IF-10 ở SS-06. Interface kho dữ liệu IF-11 đến IF-15 không thuộc P11b (P12 thiết kế).

## F8. Tổng hợp toàn hệ thống

| SS | IF | Số operation | UC dùng | Rủi ro chính |
|---|---|---|---|---|
| SS-01 OnlinePayment | IF-01, IF-08 | IF-01: 2; IF-08: 1 | UC-005 | Cách nhận kết quả (Q-45) và giao diện thu tiền (Q-96) chưa chốt; chưa có tài liệu API nên cách tra cứu theo mã tham chiếu chưa kiểm chứng; kết quả không rõ chưa có luồng P04 (Q-77, Q-14) |
| SS-02 EInvoiceSubmission | IF-02 | IF-02: 1 | UC-005 | Chưa có tài liệu API (Q-39), bên nhận có loại trùng hay không chưa biết (Q-100), xử lý khi từ chối chưa chốt (Q-54); hàng chờ thử lại trong bộ nhớ mất khi tiến trình dừng (Q-88) |
| SS-03 PushNotification | IF-03 | IF-03: 1 | UC-015 | Chưa có tài liệu giao thức (NFR-10); địa chỉ thiết bị chưa có trong mô hình (Q-101); xử lý khi gửi không được chưa chốt (Q-65, Q-79); hàng chờ nền mất khi tiến trình dừng |
| SS-04 SmsMessaging | IF-04 | IF-04: 1 | UC-015 | Xử lý khi gửi không được chưa chốt (Q-65, Q-79); SMS có thể gửi trùng khi thử lại; hàng chờ nền mất khi tiến trình dừng |
| SS-05 TurnstileAccess | IF-05, IF-09 | IF-05: 3; IF-09: 1 | UC-018 | Giao thức, nội dung trao đổi và cách xác thực chưa có tài liệu (Q-67, IF-07); hành vi khi lỗi hoặc quá 1 giây chưa chốt (Q-72, Q-41); lượt quét gửi lặp có thể ghi trùng (Q-86) |
| SS-06 DurableScheduler | IF-06, IF-10 | IF-06: 5; IF-10: 1 | UC-005, UC-015 | Độ lệch mốc chưa chốt (Q-93); xử lý khi không đặt, huỷ được mốc chưa chốt (Q-102, Q-64); mốc của UC-008, UC-009, UC-013, UC-014, UC-016, UC-022 chưa có P07 |
| SS-07 Authentication | IF-07 | IF-07: 0 (Chờ P07 UC-004, 2 trách nhiệm chưa có chữ ký) | Chờ P07 UC-004 | Toàn bộ chữ ký chờ P07 UC-004; cách xác thực và bảo vệ dữ liệu chưa chốt (Q-47, Q-89) |

Tổng: 7 subsystem, 10 interface (IF-01 đến IF-10), 16 operation có chữ ký, 3 câu hỏi mở mới (Q-100 đến Q-102), 17 sơ đồ sequence (7 hộp đen, 10 hộp trắng) cùng 13 trang phần tử và phụ thuộc, trên 7 file .drawio.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-100 | Hệ thống hoá đơn điện tử có loại bỏ dữ liệu giao dịch thu tiền gửi trùng (nhận khoá chống trùng, hoặc từ chối giao dịch đã nhận) để việc phần mềm gửi lại tối đa 3 lần không làm xuất hai hoá đơn cho một giao dịch không? (Có, nêu trường dùng làm khoá chống trùng / Không, phần mềm phải tra cứu trước khi gửi lại - nêu cách tra cứu / Khác - nêu rõ) | IF-02 sendTransactionData (cột Idempotent, thử lại); F7 của SS-02; DC-EInvoiceRetryQueue | HE_THONG_NGOAI ghi hệ thống hoá đơn điện tử chưa có tài liệu API; CHINH_SACH_LOI: gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần; nguồn Mục 10 câu 2: "Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử" không nêu việc gửi trùng |
| Q-101 | Địa chỉ nhận thông báo đẩy của thiết bị hội viên (mã đăng ký thiết bị do nền tảng cấp cho ứng dụng đã cài) do ai ghi nhận và lưu ở đâu, và hội viên dùng nhiều thiết bị thì thông báo gửi tới những thiết bị nào? (Ứng dụng đăng ký khi hội viên đăng nhập, gửi tới mọi thiết bị đã đăng ký / Chỉ thiết bị đăng nhập gần nhất / Khác - nêu rõ) | IF-03 sendPushNotification (đối tượng nhận); thuộc tính của AC-E-Member (DC-Member); F7 của SS-03; Q-36 | Nguồn Mục 10 câu 1: "Thông báo cho hội viên gửi qua thông báo đẩy của ứng dụng" không nêu cách xác định thiết bị nhận; P08 AC-E-Member không có thuộc tính này |
| Q-102 | Khi cơ chế hẹn giờ gặp lỗi kỹ thuật, các tình huống sau được xử lý thế nào: (a) không đặt được mốc hạn thanh toán 15 phút của đơn mua (UC-005 bước 9); (b) không huỷ được mốc hạn thanh toán đã có kết quả hoặc mốc của lớp bị huỷ (UC-005 bước 10, UC-015 bước 4); (c) mốc đã đến hạn nhưng việc xử lý không thành công sau 3 lần giao lại (UC-005 luồng 9a, UC-015 bước 1)? (Dừng use case và báo nhân viên - nêu từng tình huống / Tiếp tục và xử lý bù sau - nêu cách / Khác - nêu rõ) | IF-06 scheduleMark, cancelMark (lỗi MarkStoreUnavailable); IF-10 handleMarkDue (MarkHandlingFailed); UC-005 bước 9, 10, luồng 9a; UC-015 bước 1, 4; F7 của SS-06 | Nguồn Mục 2 câu 2: "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ" và Mục 8 câu 3: lớp có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học "thì hệ thống tự huỷ lớp" không nêu xử lý khi cơ chế hẹn giờ gặp lỗi |

Các câu hỏi đã cấp ở bước trước và làm đổi thiết kế này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-13 (thanh toán lại khi thất bại), Q-14 (kết quả thanh toán đến sau khi đơn bị huỷ), Q-25 (cách tính 15 phút), Q-36 (cách xác định hội viên chưa cài ứng dụng), Q-39 (trường dữ liệu hoá đơn điện tử), Q-41 (mốc đo 1 giây), Q-45 (cổng tự gửi kết quả hay phần mềm tra cứu), Q-47, Q-89 (xác thực, bảo vệ dữ liệu), Q-53 (kênh báo kết quả mua gói), Q-54 (xử lý khi hoá đơn điện tử không nhận), Q-64 (huỷ mốc của UC-016, UC-013), Q-65, Q-79 (gửi thông báo không được), Q-66 (nội dung thông báo), Q-67 (nội dung trao đổi với cửa quay), Q-68 (mã QR), Q-70 (cách báo người quét), Q-71 (ghi nhận lượt bị từ chối), Q-72 (cửa quay không nhận được kết quả), Q-77 (cổng thanh toán không phản hồi), Q-86 (số lượt quẹt), Q-88 (sẵn sàng, mất dữ liệu), Q-93 (độ lệch mốc), Q-96 (giao diện thu tiền), Q-98 (lễ tân thanh toán qua cổng).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F2 dòng SS-05 (cột Trách nhiệm), IF-05 | P10 gán // receiveScannedCode, // sendEntryResult, // openDoor cho IF-05. Cửa quay gọi vào qua API và nhận kết quả trong phản hồi, nên ba trách nhiệm này được phủ bởi tham số và kết quả của IF-09.decideEntry cùng phản hồi của SS-05, không có operation riêng trong IF-05 | Sửa cột Trách nhiệm của SS-05: IF-05 chỉ gồm enableReceiving, disableReceiving, registerScanReceiver; lượt quét đi qua IF-09. Chỉ đổi cấu trúc thiết kế, không chạy lại P08, P09. Chưa áp dụng |
| P10 | F4 (PKG-16, PKG-22, PKG-23, PKG-24, PKG-25), F5 | Chữ ký interface dùng kiểu mới đặt cùng package với interface để layer dưới không phụ thuộc layer trên, P10 chưa liệt kê | Thêm vào cột Phần tử chứa và F5 (public): PKG-16: DC-EntryDecision, DC-EntryDenialReason, DC-EntryProcessingFailed; PKG-22: DC-MarkKind, DC-MarkStoreUnavailable; PKG-23: DC-PaymentRequestResult, DC-PaymentResult, DC-PaymentGatewayUnavailable, DC-PaymentOutcomeUnknown; PKG-24: DC-NotificationContent, DC-NotificationReceipt, DC-InvalidNotificationContent, DC-InvalidPhoneNumber; PKG-25: DC-InvoiceSubmissionResult. Chưa áp dụng |
| P10 | F4, F6 (PKG-23, PKG-24, PKG-25) | Chữ ký IF-01, IF-02, IF-03 dùng entity DC-PackageOrder, DC-PaymentTransaction (PKG-27) và DC-Member (PKG-26), nhưng P10 F6 chỉ có cạnh PKG-23, PKG-24, PKG-25 --> PKG-32 | Thêm cạnh PKG-23 --> PKG-27, PKG-25 --> PKG-27, PKG-24 --> PKG-26 (hợp lệ, đi xuống, không vòng) vào F4, F6, F7; nếu muốn Services không phụ thuộc entity thì đổi chữ ký sang kiểu định danh đặt ở PKG-32 và chạy lại P11b cho SS-01, SS-02, SS-03. Chưa áp dụng |
| P04 | UC-004 (và UC-024, UC-025) | IF-07 của SS-07 chưa có chữ ký vì UC-004 chưa có P04, P07; bước xác thực thiết bị của SS-05 phụ thuộc IF-07 | Chạy P04, P07 cho UC-004 (và UC-024, UC-025 cho quyền xem chỉ số cơ thể), rồi chạy lại P11b cho SS-07 và SS-05 |
| P04 | UC-005 luồng 9, 10 | Chưa có luồng cho cổng thanh toán không phản hồi (PaymentGatewayUnavailable) và kết quả không rõ sau khi đã gửi (PaymentOutcomeUnknown) | Khi Q-77 có câu trả lời, thêm luồng cho hai tình huống và kết cục của đơn mua, rồi chạy lại P07 UC-005. Chưa áp dụng |
| P04 | UC-005 bước 9, 10, luồng 9a; UC-015 bước 1, 4 | Chưa có luồng khi không đặt được, không huỷ được mốc hẹn giờ (MarkStoreUnavailable) hoặc mốc đến hạn mà việc xử lý không thành công (MarkHandlingFailed) | Khi Q-102 có câu trả lời, thêm luồng cho các tình huống (a), (b), (c) và kết cục, rồi chạy lại P07 UC-005, UC-015. Chưa áp dụng |
| P04 | UC-018 luồng thay thế | Chưa có luồng khi thông điệp của cửa quay không đọc được hoặc phần mềm lỗi lúc xử lý lượt quét (phản hồi lỗi cho cửa quay) | Khi Q-67, Q-72 có câu trả lời, thêm luồng cho hai tình huống, rồi chạy lại P07 UC-018. Chưa áp dụng |

## Vấn đề còn mở

Các mục Target đạt, trừ mục 1 (đạt một phần) và các điểm cần lưu ý dưới đây:

- Target 1: SS-07 có interface IF-07 nhưng không có chữ ký, trạng thái "Chờ P07 UC-004", vì P07 của bốn use case không có message tới PKG-21 và P04 không có luồng xác thực. P10 F1 dẫn UC-005, UC-010, UC-018 làm lý do xét SS-07; thiết kế theo A1 (dựa vào P04, P07) nên không định nghĩa chữ ký. Hệ quả: SS-05 chưa có bước xác thực thiết bị trong sơ đồ hộp trắng. Chạy lại P11b cho SS-07 và SS-05 sau P04, P07 của UC-004.
- Target 2: // scanQrCode của AC-B-TurnstileDevice không có operation (thao tác vật lý trên cửa quay, ngoài phần mềm, P10 F2); // sendEntryResult và // openDoor được phủ bởi kết quả của IF-09.decideEntry và phản hồi của SS-05, không là operation riêng. UC-010 không dùng subsystem nào nên không có sơ đồ hộp đen cho UC-010.
- Target 3: các operation vòng đời enableReceiving, disableReceiving, registerScanReceiver (IF-05) và registerMarkHandler, start, stop (IF-06) do P10 F2 giao cho interface, không phục vụ riêng một bước của use case; ghi UC kèm "kỹ thuật" và Timeout "-" vì không chờ hệ thống ngoài. A3 chỉ cho phép operation kỹ thuật phục vụ chính sách lỗi, nên các operation này không khớp hẳn A3; giữ vì P10 F2 đã giao và Target 1 đòi mọi subsystem có interface dùng được.
- Target 6: CHINH_SACH_LOI (ưu tiên cao hơn quy tắc bước, C9) yêu cầu gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, trong khi A5 chỉ cho thử lại khi operation idempotent. Giải quyết bằng khoá chống trùng do hệ thống sinh (mã tham chiếu giao dịch) và Q-100 về việc bên nhận loại trùng; chưa có Q-100 trả lời thì rủi ro hai hoá đơn cho một giao dịch còn. Thông báo đẩy và SMS thử lại có thể gửi trùng, chấp nhận vì không có tác dụng phụ tài chính. requestPayment không idempotent và không thử lại.
- Hàng chờ thử lại của SS-02, SS-03, SS-04 giữ trong bộ nhớ tiến trình nền (P10 chưa cho PKG-24, PKG-25 phụ thuộc PKG-22), nên mất khi tiến trình dừng; nếu dự án cần bền thì dùng IF-06 hoặc quyết định ở P09 theo Q-88.
- Cách nhận kết quả thanh toán (Q-45) và giao diện thu tiền (Q-96) chưa chốt: IF-01, IF-08 dùng được cho cả hai cách (cổng đẩy kết quả hoặc phần mềm gọi queryPaymentStatus); sơ đồ SS01-WB3 vẽ từ lúc SS-01 nhận được thông điệp kết quả. Nếu Q-45 chọn cổng tự gửi về thì thêm điểm vào nhận thông điệp của cổng ở PKG-12 và cạnh PKG-12 --> PKG-23 (P10 Vấn đề còn mở).
- Mã tham chiếu giao dịch do phần mềm sinh trước khi gửi để tra cứu được cả khi mất phản hồi; việc API tra cứu của cổng nhận mã này cần tài liệu API (TAI_LIEU_GIAO_TIEP: Không có), chưa kiểm chứng. Tương tự timeout, retry của ba cổng chưa kiểm chứng với tài liệu.
- Chọn giữa hai quy tắc (C9): A2 đặt interface chiều ngược ở layer của subsystem thiết bị và lớp hiện thực ở layer trên; SS-05 ở Presentation, không có layer cao hơn. Giữ P10: IF-09 ở PKG-16 (Application), SS-05 gọi xuống, realization không đi lên.
- Target 10: gate là ellipse 10 x 10 có tâm trên cạnh trái khung sd và ở y của message (bội số của 10), nên x, y của gate lệch 5 so với bội số của 10, trái với C7.3 mục toạ độ bội số của 10; mọi cell khác đều theo bội số của 10. Tác nhân hệ thống ngoài và thiết bị ở sơ đồ sequence vẽ bằng lifeline có nhãn «actor». Chưa mở được draw.io để kiểm tra mắt thường; đã kiểm tra bằng chương trình: XML hợp lệ, không hai lifeline hay fragment chồng nhau, mọi fragment nằm trong khung, class diagram không cạnh nào cắt qua node.
- Sơ đồ hộp trắng của IF-09 (SS05-WB1) bắt đầu từ tin nhắn của cửa quay, không từ gate vào, vì IF-09 là interface do hệ thống cung cấp và SS-05 là bên gọi; trang hộp trắng của IF-08, IF-10 cũng vẽ phía subsystem gọi (SS01-WB3, SS06-WB3), không vẽ phần bên trong Handler (thuộc P12).
- Kiểu trong chữ ký dùng kiểu của TypeScript theo CONG_NGHE (string, boolean, Date, void) cộng kiểu của mô hình; việc bọc Promise cho lời gọi vào/ra thuộc P12. Cột Đồng bộ ghi ngữ nghĩa chờ kết quả, không ghi cách viết mã.
- Mã DC cho phần tử bên trong subsystem cấp mới ở P11b theo C3; P12 thiết kế thuộc tính và phương thức. Loại phần tử MarkKind chỉ có hai giá trị có P07 (PaymentDeadline, ClassCutoff) cộng hai giá trị chỉ để huỷ (AbsenceCheck, WaitlistTransfer); thêm giá trị khi UC-008, UC-009, UC-013, UC-014, UC-016, UC-022 có P04, P07.
