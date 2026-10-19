# P11b - SS-02 EInvoiceSubmission - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | SS-02 EInvoiceSubmission (package PKG-25 EInvoiceIntegration); lần chạy đầu cho mọi subsystem của P10 F2 |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102, ghi ở file chung P11b-system-interfaces.md); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| UC-005 Mua hoặc gia hạn gói tập | AC-C-PurchaseOrRenewPackageHandler (DC-PurchaseOrRenewPackageHandler) | SD1c STT 4.1.6 sendTransactionData (dữ liệu giao dịch thu tiền), bước 12; SD2 STT 9r cùng message | Dữ liệu giao dịch thu tiền do AC-E-PaymentTransaction // prepareInvoiceData cung cấp (trường dữ liệu: Q-39) | 12a (hệ thống hoá đơn điện tử không nhận hoặc từ chối dữ liệu giao dịch), chờ Q-54 |

- UC-007, UC-017, UC-019 cũng gửi dữ liệu giao dịch thu tiền (P08, NFR-12) nhưng chưa có P04, P07; khi có, chạy lại P11b cho SS-02 để thêm UC dùng IF-02.

## F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-02 | IEInvoiceGateway | Gửi dữ liệu một giao dịch thu tiền sang hệ thống hoá đơn điện tử, không lập, điều chỉnh, huỷ hoá đơn. | SS-02 EInvoiceSubmission | DC-PurchaseOrRenewPackageHandler (PKG-14) | PKG-25 EInvoiceIntegration |

- Số operation: IF-02 có 1. Phạm vi chỉ có chiều gửi dữ liệu (NFR-05, ràng buộc đặc thù mục 4 của hồ sơ dự án).
- Layer: IF-02 ở PKG-25 (Services); kiểu trong chữ ký DC-PaymentTransaction (PKG-27) và DC-TransactionReference (PKG-32) ở Domain, DC-InvoiceSubmissionResult ở PKG-25.

## F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-02 | IEInvoiceGateway | Hệ thống hoá đơn điện tử (ACT-11) | sendTransactionData(transaction: PaymentTransaction): InvoiceSubmissionResult | transaction: PaymentTransaction - giao dịch thu tiền đã ghi nhận, có mã tham chiếu | InvoiceSubmissionResult: status (Accepted / Rejected / Queued), transactionRef: TransactionReference | Rejected (Nghiệp vụ, trong kết quả); Queued (Kỹ thuật tạm thời hoặc Không rõ kết quả ở lần gửi đầu, subsystem sẽ thử lại ở nền) | UC-005 (bước 12) | Giao dịch thu tiền đã ghi nhận ở bước 11 | Accepted: bên nhận đã nhận dữ liệu; Queued: còn tối đa 3 lần thử lại, cách nhau 1 phút | Đồng bộ cho lần gửi đầu; các lần thử lại chạy ở nền | Có với khoá idempotency (mã tham chiếu giao dịch); bên nhận có loại trùng hay không chờ Q-100 | 15 giây mỗi lần gửi (CHINH_SACH_LOI) |

- Ánh xạ trách nhiệm P08 của AC-B-EInvoiceGateway: // sendTransactionData --> IF-02.sendTransactionData.
- Thử lại tối đa 3 lần cách nhau 1 phút theo CHINH_SACH_LOI. Gửi hoá đơn có hệ quả tài chính nên chỉ thử lại khi dữ liệu mang khoá chống trùng do hệ thống sinh (mã tham chiếu giao dịch); bên nhận có thực sự loại trùng theo khoá hay không chưa có tài liệu nên ghi Q-100.
- Gói tập vẫn kích hoạt hay giao dịch phải dừng khi gửi không được là giá trị nghiệp vụ chờ Q-54; operation chỉ báo trạng thái Rejected, Queued để control quyết định.

## F4. Sequence diagram

File diagrams/P11b-subsystem-SS-02.drawio gồm 4 trang: "Hộp đen - UC-005 gửi dữ liệu hoá đơn"; "Hộp trắng - sendTransactionData"; "Phần tử"; "Phụ thuộc". STT đánh số phẳng theo trục thời gian trong mỗi trang; tọa độ bảng Node là tuyệt đối. Gate nằm trên cạnh trái khung sd, tâm gate ở y của message nên x, y của gate lệch 5 so với bội số của 10 (xem Vấn đề còn mở).

### Trang "Hộp đen - UC-005 gửi dữ liệu hoá đơn" (SS02-BB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS02-BB1-FR | Fragment | sd Hộp đen UC-005 hoá đơn điện tử | - | - | Khung sd của trang | 20 | 0 | 420 | 280 |
| SS02-BB1-L1 | Lifeline | :PurchaseOrRenewPackageHandler | «control» | - | DC-PurchaseOrRenewPackageHandler (PKG-14) | 100 | 40 | 120 | 220 |
| SS02-BB1-L2 | Lifeline | :IF-02 IEInvoiceGateway | «interface» | - | Subsystem SS-02 hiện thực | 260 | 40 | 120 | 220 |
| SS02-BB1-F1 | Fragment | alt [bên nhận đã nhận hoặc từ chối] | - | - | đường ngăn SS02-BB1-F1-O2-SEP nét đứt tại y=180 | 80 | 140 | 320 | 70 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS02-BB1-F1 toán hạng 2: [chưa gửi được, subsystem thử lại ở nền].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS02-BB1-M01 | 1 | SS02-BB1-L1 | SS02-BB1-L2 | sendTransactionData(transaction) | Đồng bộ | - | UC-005 bước 12; sendTransactionData |
| SS02-BB1-M02 | 2 | SS02-BB1-L2 | SS02-BB1-L1 | InvoiceSubmissionResult (Accepted / Rejected) | Trả về | SS02-BB1-F1 (toán hạng 1) | UC-005 bước 12; luồng 12a khi Rejected |
| SS02-BB1-M03 | 3 | SS02-BB1-L2 | SS02-BB1-L1 | InvoiceSubmissionResult (Queued) | Trả về | SS02-BB1-F1 (toán hạng 2) | UC-005 luồng 12a; Q-54 |

### Trang "Hộp trắng - sendTransactionData" (SS02-WB1)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS02-WB1-FR | Fragment | sd sendTransactionData | - | - | Khung sd của trang | 20 | 0 | 900 | 960 |
| SS02-WB1-L1 | Lifeline | :EInvoiceGatewayFacade | «facade» | SS-02 | DC-EInvoiceGatewayFacade; hiện thực IF-02 | 100 | 40 | 120 | 900 |
| SS02-WB1-L2 | Lifeline | :EInvoiceDataMapper | «mapper» | SS-02 | DC-EInvoiceDataMapper | 260 | 40 | 120 | 900 |
| SS02-WB1-L3 | Lifeline | :EInvoiceClient | «adapter» | SS-02 | DC-EInvoiceClient | 420 | 40 | 120 | 900 |
| SS02-WB1-L4 | Lifeline | :EInvoiceRetryQueue | «store» | SS-02 | DC-EInvoiceRetryQueue | 580 | 40 | 120 | 900 |
| SS02-WB1-L5 | Actor | Hệ thống hoá đơn điện tử (ACT-11) | «actor» | - | Tác nhân hệ thống ngoài | 740 | 40 | 120 | 900 |
| SS02-WB1-FR-G1 | Gate | sendTransactionData | - | SS02-WB1-FR | Gate vào khung, message STT 1 | 15 | 115 | 10 | 10 |
| SS02-WB1-FR-G8 | Gate | InvoiceSubmissionResult (Accepted / Rejected) | - | SS02-WB1-FR | Gate ra khung, message STT 8 | 15 | 395 | 10 | 10 |
| SS02-WB1-FR-G12 | Gate | InvoiceSubmissionResult (Queued) | - | SS02-WB1-FR | Gate ra khung, message STT 12 | 15 | 555 | 10 | 10 |
| SS02-WB1-F1 | Fragment | alt [bên nhận phản hồi trong 15 giây] | - | - | đường ngăn SS02-WB1-F1-O2-SEP nét đứt tại y=420 | 80 | 300 | 800 | 270 |
| SS02-WB1-F2 | Fragment | loop [tối đa 3 lần thử lại, cách 1 phút, dừng khi bên nhận phản hồi] | - | - | - | 400 | 620 | 480 | 190 |

Nhãn của các toán hạng sau toán hạng đầu (đặt dưới đường ngăn nét đứt): SS02-WB1-F1 toán hạng 2: [lỗi tạm thời hoặc quá 15 giây].

Bảng message

| ID | STT | Từ | Đến | Message | Loại | Fragment | Operation hoặc UC bước |
|---|---|---|---|---|---|---|---|
| SS02-WB1-M01 | 1 | SS02-WB1-FR-G1 | SS02-WB1-L1 | sendTransactionData(transaction) | Đồng bộ | - | sendTransactionData; UC-005 bước 12 |
| SS02-WB1-M02 | 2 | SS02-WB1-L1 | SS02-WB1-L2 | toInvoiceMessage(transaction) | Đồng bộ | - | sendTransactionData; trường dữ liệu chờ Q-39 |
| SS02-WB1-M03 | 3 | SS02-WB1-L2 | SS02-WB1-L1 | invoiceMessage (kèm khoá chống trùng) | Trả về | - | sendTransactionData |
| SS02-WB1-M04 | 4 | SS02-WB1-L1 | SS02-WB1-L3 | submit(invoiceMessage) | Đồng bộ | - | sendTransactionData; timeout 15 giây |
| SS02-WB1-M05 | 5 | SS02-WB1-L3 | SS02-WB1-L5 | sendInvoiceData(invoiceMessage) | Đồng bộ | - | UC-005 bước 12 |
| SS02-WB1-M06 | 6 | SS02-WB1-L5 | SS02-WB1-L3 | phản hồi của bên nhận | Trả về | SS02-WB1-F1 (toán hạng 1) | UC-005 bước 12 |
| SS02-WB1-M07 | 7 | SS02-WB1-L3 | SS02-WB1-L1 | submitResult | Trả về | SS02-WB1-F1 (toán hạng 1) | sendTransactionData |
| SS02-WB1-M08 | 8 | SS02-WB1-L1 | SS02-WB1-FR-G8 | InvoiceSubmissionResult (Accepted / Rejected) | Trả về | SS02-WB1-F1 (toán hạng 1) | sendTransactionData; luồng 12a khi Rejected |
| SS02-WB1-M09 | 9 | SS02-WB1-L3 | SS02-WB1-L1 | SubmitFailed | Trả về | SS02-WB1-F1 (toán hạng 2) | sendTransactionData; lỗi tạm thời hoặc không rõ kết quả |
| SS02-WB1-M10 | 10 | SS02-WB1-L1 | SS02-WB1-L4 | enqueueRetry(invoiceMessage) | Đồng bộ | SS02-WB1-F1 (toán hạng 2) | sendTransactionData |
| SS02-WB1-M11 | 11 | SS02-WB1-L4 | SS02-WB1-L1 | queued | Trả về | SS02-WB1-F1 (toán hạng 2) | sendTransactionData |
| SS02-WB1-M12 | 12 | SS02-WB1-L1 | SS02-WB1-FR-G12 | InvoiceSubmissionResult (Queued) | Trả về | SS02-WB1-F1 (toán hạng 2) | sendTransactionData; luồng 12a (Q-54) |
| SS02-WB1-M13 | 13 | SS02-WB1-L4 | SS02-WB1-L4 | startRetryTimer(tối đa 3 lần) | Tự gọi | - | Thử lại ở nền, cách 1 phút |
| SS02-WB1-M14 | 14 | SS02-WB1-L4 | SS02-WB1-L4 | waitOneMinute() | Tự gọi | SS02-WB1-F2 | Thử lại ở nền |
| SS02-WB1-M15 | 15 | SS02-WB1-L4 | SS02-WB1-L3 | submit(invoiceMessage) | Đồng bộ | SS02-WB1-F2 | Thử lại; timeout 15 giây |
| SS02-WB1-M16 | 16 | SS02-WB1-L3 | SS02-WB1-L5 | sendInvoiceData(invoiceMessage) | Đồng bộ | SS02-WB1-F2 | Thử lại |
| SS02-WB1-M17 | 17 | SS02-WB1-L5 | SS02-WB1-L3 | phản hồi hoặc lỗi | Trả về | SS02-WB1-F2 | Thử lại |
| SS02-WB1-M18 | 18 | SS02-WB1-L3 | SS02-WB1-L4 | submitResult | Trả về | SS02-WB1-F2 | Thử lại |
| SS02-WB1-M19 | 19 | SS02-WB1-L4 | SS02-WB1-L1 | retryOutcome(outcome) | Bất đồng bộ | - | Kết thúc thử lại |
| SS02-WB1-M20 | 20 | SS02-WB1-L1 | SS02-WB1-L1 | recordOutcome(outcome) | Tự gọi | - | Ghi nhật ký; luồng 12a (Q-54) |

Quy tắc ngữ nghĩa đã áp dụng: message mức thiết kế ghi chữ ký với đối số; message bất đồng bộ đầu mũi tên mở, nét liền (endArrow=open;endFill=0;html=1;); client chỉ gọi interface; không có message từ subsystem tới lớp giao diện người dùng; mỗi message đi qua khung sd có một gate riêng.

## F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| DC-EInvoiceGatewayFacade | EInvoiceGatewayFacade | Điều phối | Hiện thực IF-02: gọi Mapper và Client cho lần gửi đầu (timeout 15 giây), đưa vào hàng chờ khi lỗi tạm thời hoặc không rõ kết quả, ghi nhật ký kết quả cuối | package-private | IF-02 |
| DC-EInvoiceDataMapper | EInvoiceDataMapper | Chuyển đổi dữ liệu | Đổi PaymentTransaction thành thông điệp của hệ thống hoá đơn kèm khoá chống trùng (trường dữ liệu: Q-39) | package-private | - |
| DC-EInvoiceClient | EInvoiceClient | Giao tiếp ngoài | Proxy gọi API REST của hệ thống hoá đơn điện tử; phân biệt từ chối nghiệp vụ với lỗi tạm thời | package-private | - |
| DC-EInvoiceRetryQueue | EInvoiceRetryQueue | Lưu trữ trong subsystem | Giữ trong bộ nhớ tiến trình nền các thông điệp chờ thử lại, hẹn 1 phút giữa hai lần, tối đa 3 lần | package-private | - |
| DC-EInvoiceGatewayConfig | EInvoiceGatewayConfig | Lưu trữ trong subsystem | Giữ địa chỉ và thông tin xác thực lấy từ cấu hình môi trường | package-private | - |
| DC-InvoiceSubmissionResult | InvoiceSubmissionResult (PKG-25) | Kiểu dữ liệu | status (Accepted / Rejected / Queued), transactionRef | public | - |

b) Class diagram phần tử: trang "Phần tử" (SS02-EL). Tọa độ bảng Node là tuyệt đối trên trang; file .drawio ghi tọa độ của phần tử con tương đối theo khung subsystem. Kiểu dữ liệu và ngoại lệ ở F5 a không vẽ lại ở sơ đồ.

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-02 | Subsystem | SS-02 EInvoiceSubmission | «subsystem» | - | Khung subsystem | 40 | 180 | 1320 | 260 |
| IF-02 | Interface | IF-02 IEInvoiceGateway | «interface» | PKG-25 | Interface subsystem cung cấp | 320 | 40 | 240 | 60 |
| DC-EInvoiceDataMapper | Class | EInvoiceDataMapper | «mapper» | SS-02 | Chuyển đổi dữ liệu | 80 | 260 | 200 | 60 |
| DC-EInvoiceGatewayFacade | Class | EInvoiceGatewayFacade | «facade» | SS-02 | Điều phối; hiện thực IF-02 | 340 | 260 | 200 | 60 |
| DC-EInvoiceRetryQueue | Class | EInvoiceRetryQueue | «store» | SS-02 | Lưu trữ trong subsystem (hàng chờ thử lại) | 600 | 260 | 200 | 60 |
| DC-EInvoiceClient | Class | EInvoiceClient | «adapter» | SS-02 | Giao tiếp ngoài | 860 | 260 | 200 | 60 |
| DC-EInvoiceGatewayConfig | Class | EInvoiceGatewayConfig | «config» | SS-02 | Cấu hình địa chỉ và thông tin xác thực | 1120 | 260 | 200 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS02-EL-E1 | DC-EInvoiceGatewayFacade | IF-02 | Realization | - | Facade hiện thực IF-02 | - |
| SS02-EL-E2 | DC-EInvoiceGatewayFacade | DC-EInvoiceDataMapper | Dependency | «use» | Chuyển đổi kiểu mô hình và thông điệp | - |
| SS02-EL-E3 | DC-EInvoiceGatewayFacade | DC-EInvoiceRetryQueue | Dependency | «use» | Đưa yêu cầu vào hàng chờ thử lại | - |
| SS02-EL-E4 | DC-EInvoiceRetryQueue | DC-EInvoiceClient | Dependency | «use» | Hàng chờ gửi lại qua client | - |
| SS02-EL-E5 | DC-EInvoiceClient | DC-EInvoiceGatewayConfig | Dependency | «use» | Đọc địa chỉ và thông tin xác thực | - |
| SS02-EL-E6 | DC-EInvoiceGatewayFacade | DC-EInvoiceClient | Dependency | «use» | Lần gửi đầu đi thẳng qua client | (440,350); (960,350) |

c) Cơ chế kiến trúc áp dụng

| Cơ chế | Nguồn | Cách tích hợp |
|---|---|---|
| Bảo mật dữ liệu | P09 F7 (giao dịch thu tiền là dữ liệu cần bảo vệ, truyền qua kênh mã hoá) | Lời gọi qua kênh mã hoá; nhật ký chỉ ghi mã tham chiếu giao dịch, không ghi nội dung hoá đơn. |
| Giao dịch và xử lý lặp lại | P09 F7 (xử lý lặp lại được) | Khoá chống trùng là mã tham chiếu giao dịch, giữ nguyên ở mọi lần thử lại. |
| Ghi nhật ký | Thiết kế: P09 F7 không nêu | Ghi mỗi lần gửi và kết quả cuối (Accepted, Rejected, hết 3 lần thử); lý do: có căn cứ gửi lại hoặc đối soát khi luồng 12a được chốt (Q-54). |
| Cấu hình địa chỉ và thông tin xác thực | Thiết kế: P09 F7 không nêu | DC-EInvoiceGatewayConfig đọc từ cấu hình môi trường; lý do: API hoá đơn chưa ổn định (KHA_NANG_THAY_DOI_GIAO_DIEN ở P10), cần đổi mà không sửa mã. |
| Hàng chờ thử lại | Thiết kế: P09 F7 không nêu | Giữ trong bộ nhớ tiến trình nền, không dùng IF-06, vì PKG-25 chưa phụ thuộc PKG-22 trong P10 và lượng dữ liệu nhỏ; hạn chế: mất khi tiến trình dừng (Q-88). |

## F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-02 | PKG-27 (DC-PaymentTransaction) | Vào package | Chữ ký sendTransactionData nhận giao dịch thu tiền; entity ở Domain dùng trực tiếp trong chữ ký (P09 A4, P11b A3) | Dùng thận trọng |
| SS-02 | PKG-32 (DC-TransactionReference) | Vào package | Khoá chống trùng và kết quả dùng mã tham chiếu giao dịch (P10 PKG-32) | Dùng thận trọng |

Trang "Phụ thuộc" (SS02-DP)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-02 | SubsystemBox | SS-02 EInvoiceSubmission | «subsystem» | - | Subsystem đang xét | 40 | 40 | 240 | 160 |
| PKG-27 | Package | PKG-27 Membership | - | PKG-04 Domain | Chứa DC-PaymentTransaction | 420 | 40 | 240 | 60 |
| PKG-32 | Package | PKG-32 ValueTypes | - | PKG-04 Domain | Chứa DC-TransactionReference | 420 | 140 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS02-DP-E1 | SS-02 | PKG-27 | Dependency | «use» | Vào package: chữ ký IF-02 dùng DC-PaymentTransaction | - |
| SS02-DP-E2 | SS-02 | PKG-32 | Dependency | «use» | Vào package: khoá chống trùng và kết quả dùng DC-TransactionReference | - |

## F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| sendTransactionData | Bên nhận từ chối dữ liệu (sai hoặc thiếu trường) | Nghiệp vụ | Phản hồi từ chối của bên nhận | Không thử lại (gửi lại cùng dữ liệu cho cùng kết quả) | InvoiceSubmissionResult.status = Rejected | 12a | Q-54, Q-39 |
| sendTransactionData | Không kết nối được hoặc bên nhận báo quá tải | Kỹ thuật tạm thời | Lỗi kết nối hoặc mã báo tạm thời | Đưa vào hàng chờ, thử lại ở nền tối đa 3 lần cách 1 phút (CHINH_SACH_LOI) | status = Queued | 12a | Q-54 |
| sendTransactionData | Quá 15 giây sau khi đã gửi | Không rõ kết quả | Hết thời gian chờ | Như dòng trên, gửi lại cùng khoá chống trùng; chỉ an toàn nếu bên nhận loại trùng | status = Queued | 12a | Q-54, Q-100 |
| sendTransactionData | Hết 3 lần thử lại vẫn thất bại | Kỹ thuật tạm thời | Bộ đếm lần thử lại | Dừng thử, ghi nhật ký giao dịch chưa có hoá đơn; không báo client vì đã trả Queued | Không trả thêm | 12a | Q-54 |
| sendTransactionData | Tiến trình nền dừng khi hàng chờ còn mục | Kỹ thuật tạm thời | Khởi động lại tiến trình | Hàng chờ trong bộ nhớ nên mất; việc gửi lại ngoài phạm vi P11b | Không trả thêm | 12a | Q-54, Q-88 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Đạt | IF-02: SS02-EL-E1 |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Không áp dụng | SS-02 không dùng interface nào |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Đạt | Xem F5 a |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Đạt | sendTransactionData: SS02-WB1 |

## Câu hỏi mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Vấn đề còn mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).
