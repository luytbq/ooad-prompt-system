# P11a - Danh sách màn hình - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 1; nối từ giai đoạn 2) |
| Phiên bản | 1.1 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005, UC-010, UC-015, UC-018 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa, Từ đồng nghĩa không dùng); P06-supplementary-spec.md (phiên bản 1.0; Mục 3 đến Mục 6); P07-uc-analysis/ bốn file (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4, Đề xuất sửa artifact trước, Vấn đề còn mở). Mã Q, ASM lớn nhất do người dùng cung cấp (Q-94; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả. CHE_DO_CHAY: Giai đoạn 1. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (dùng ở đặc tả màn hình giai đoạn 2). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; các use case khác của P02 chưa đặc tả, màn hình của chúng chỉ là lối vào trên màn hình điều hướng; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; ba đề xuất của P10 cho P08, P09 chỉ đổi cấu trúc thiết kế nên P08, P09 không chạy lại; mục g) của SCR-01 đến SCR-16 (giai đoạn 2, phiên bản 1.0, gom vào mục 3) |
| Phạm vi | Toàn hệ thống (giai đoạn 1); màn hình nghiệp vụ cho UC-005, UC-010; UC-015, UC-018 không có màn hình; các use case khác chỉ là lối vào trên màn hình điều hướng |
| Mã Q, ASM cuối đã cấp | Q-105; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Danh sách màn hình

| SCR | Tên | Boundary AC nguồn | UC | Tác nhân | Loại | Lớp thiết kế (DC) | Mục đích | Bước UC phục vụ |
|---|---|---|---|---|---|---|---|---|
| SCR-01 | Trang chủ Người quan tâm (Prospect home) | Điều hướng (UC-001, UC-002, UC-003) | UC-001, UC-002, UC-003 | ACT-01 Người quan tâm | Độc lập | Chưa có (điều hướng) | Chọn xem giá gói tập, xem lịch lớp nhóm hoặc đăng ký tài khoản hội viên | - |
| SCR-02 | Trang chủ Hội viên (Member home) | Điều hướng (UC-005, UC-006, UC-010, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025) | UC-005, UC-006, UC-010, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025 | ACT-02 Hội viên | Độc lập | Chưa có (điều hướng) | Chọn use case của hội viên | - |
| SCR-03 | Chọn gói tập (Select membership package) | AC-B-PurchaseOrRenewPackageUI | UC-005 | ACT-02 Hội viên | Độc lập | DC-PurchaseOrRenewPackageView | Xem các gói tập kèm thời hạn, loại, giá hiện hành và chọn gói cần mua hoặc gia hạn | 1-3 |
| SCR-04 | Xác nhận đơn mua (Confirm package order) | AC-B-PurchaseOrRenewPackageUI | UC-005 | ACT-02 Hội viên | Phụ thuộc có dữ liệu | DC-PurchaseOrRenewPackageView | Xem tóm tắt đơn mua (gói tập, ngày bắt đầu, số tiền phải trả), xác nhận mua và chờ kết quả thanh toán | 6-7, 9-10, 9a2, 10a |
| SCR-05 | Gói tập đã kích hoạt (Activated membership package) | AC-B-PurchaseOrRenewPackageUI | UC-005 | ACT-02 Hội viên | Phụ thuộc có dữ liệu | DC-PurchaseOrRenewPackageView | Xem gói tập vừa kích hoạt (gói tập, ngày bắt đầu, trạng thái gói) | 13 |
| SCR-06 | Chọn lớp nhóm (Select group class) | AC-B-BookClassSpotUI | UC-010 | ACT-02 Hội viên | Độc lập | DC-BookClassSpotView | Xem lịch lớp nhóm (loại lớp, phòng, huấn luyện viên, giờ học) và chọn lớp cần đặt chỗ; nhận thông báo từ chối hoặc lớp đủ chỗ bằng hộp thông điệp | 1-3, 4a, 5a, 5b, 6a, 7a1, 7a2 |
| SCR-07 | Chỗ đã đặt (Booked class spot) | AC-B-BookClassSpotUI | UC-010 | ACT-02 Hội viên | Phụ thuộc có dữ liệu | DC-BookClassSpotView | Xem thông tin chỗ đã đặt (loại lớp, phòng, huấn luyện viên, giờ học) | 9 |
| SCR-08 | Vị trí trong danh sách chờ (Waitlist position) | AC-B-BookClassSpotUI | UC-010 | ACT-02 Hội viên | Phụ thuộc có dữ liệu | DC-BookClassSpotView | Xem loại lớp, giờ học và vị trí trong danh sách chờ của lớp đã đủ chỗ | 7a4 |
| SCR-09 | Trang chủ Huấn luyện viên (Trainer home) | Điều hướng (UC-021, UC-024, UC-025) | UC-021, UC-024, UC-025 | ACT-04 Huấn luyện viên | Độc lập | Chưa có (điều hướng) | Chọn use case của huấn luyện viên | - |
| SCR-10 | Trang chủ Lễ tân (Receptionist home) | Điều hướng (UC-005, UC-007, UC-017) | UC-005, UC-007, UC-017 | ACT-05 Lễ tân | Độc lập | Chưa có (điều hướng) | Chọn use case của lễ tân | - |
| SCR-11 | Chọn gói tập và người mua (Select package and buyer) | AC-B-SellPackageUI | UC-005 | ACT-05 Lễ tân | Độc lập | DC-SellPackageView | Xem các gói tập kèm thời hạn, loại, giá hiện hành; chọn gói và người mua gói để bán tại quầy | 1-3 |
| SCR-12 | Xác nhận đơn bán tại quầy (Confirm counter sale order) | AC-B-SellPackageUI | UC-005 | ACT-05 Lễ tân | Phụ thuộc có dữ liệu | DC-SellPackageView | Xem tóm tắt đơn mua (gói tập, ngày bắt đầu, số tiền phải trả) và xác nhận bán | 6-7 |
| SCR-13 | Thu tiền tại quầy (Collect payment at counter) | AC-B-SellPackageUI | UC-005 | ACT-05 Lễ tân | Phụ thuộc có dữ liệu | DC-SellPackageView | Xác nhận đã thu đủ tiền mặt hoặc nhập mã giao dịch POS của khách quẹt thẻ | 8a, 8b |
| SCR-14 | Gói tập đã kích hoạt tại quầy (Activated package at counter) | AC-B-SellPackageUI | UC-005 | ACT-05 Lễ tân | Phụ thuộc có dữ liệu | DC-SellPackageView | Xem gói tập vừa kích hoạt cho khách (gói tập, ngày bắt đầu, trạng thái gói) | 13 |
| SCR-15 | Trang chủ Quản lý chi nhánh (Branch manager home) | Điều hướng (UC-009, UC-014) | UC-009, UC-014 | ACT-06 Quản lý chi nhánh | Độc lập | Chưa có (điều hướng) | Chọn use case của quản lý chi nhánh | - |
| SCR-16 | Trang chủ Giám đốc chuỗi (Chain director home) | Điều hướng (UC-026, UC-027, UC-028) | UC-026, UC-027, UC-028 | ACT-07 Giám đốc chuỗi | Độc lập | Chưa có (điều hướng) | Chọn use case của giám đốc chuỗi | - |

Slug của file đặc tả lấy từ tên tiếng Anh trong ngoặc, viết thường, nối bằng dấu gạch nối (ví dụ SCR-03-select-membership-package.md). Mã SCR cấp theo thứ tự tác nhân (ACT-01, ACT-02, ACT-04, ACT-05, ACT-06, ACT-07) rồi theo thứ tự dịch chuyển. Cột Lớp thiết kế ghi lớp View của P10 F3; lớp Store đi cùng View (DC-PurchaseOrRenewPackageStore, DC-BookClassSpotStore, DC-SellPackageStore). Mọi boundary giao diện người dùng ở P10 F3 (AC-B-PurchaseOrRenewPackageUI, AC-B-BookClassSpotUI ở PKG-05; AC-B-SellPackageUI ở PKG-07, đều thuộc layer PKG-01 Presentation theo P10 F4) có ít nhất một màn hình.

Thống kê: 16 màn hình gồm 6 màn hình điều hướng và 10 màn hình nghiệp vụ. Số màn hình nghiệp vụ theo boundary: AC-B-PurchaseOrRenewPackageUI 3, AC-B-BookClassSpotUI 3, AC-B-SellPackageUI 4. UC-015 và UC-018 không có màn hình nghiệp vụ. Phân bổ theo tác nhân: ACT-01 1, ACT-02 7, ACT-04 1, ACT-05 5, ACT-06 1, ACT-07 1.

## 2. Boundary không có màn hình

| AC | Loại boundary | Ánh xạ ở P10 (SS, DC) | Lý do |
|---|---|---|---|
| AC-B-PaymentGateway | Giao diện hệ thống (ACT-08) | SS-01 OnlinePayment (PKG-23) | P10 ánh xạ sang subsystem ở layer Services; không có người dùng thao tác trực tiếp. Màn hình thu tiền của cổng (nếu có trong ứng dụng) chờ Q-96 |
| AC-B-EInvoiceGateway | Giao diện hệ thống (ACT-11) | SS-02 EInvoiceSubmission (PKG-25) | P10 ánh xạ sang subsystem; chỉ gửi dữ liệu giao dịch sang hệ thống ngoài, không có người dùng |
| AC-B-PushNotificationGateway | Giao diện hệ thống (ACT-10), vai trò kênh thông báo đẩy | SS-03 PushNotification (PKG-24) | P10 ánh xạ sang subsystem; kênh thông báo, nội dung chờ Q-66 và hiển thị do hệ điều hành thực hiện |
| AC-B-SmsGateway | Giao diện hệ thống (ACT-09), vai trò kênh thông báo SMS | SS-04 SmsMessaging (PKG-24) | P10 ánh xạ sang subsystem; kênh thông báo SMS, không có màn hình của phần mềm |
| AC-B-TurnstileDevice | Giao diện thiết bị (ACT-12, ACT-02, ACT-03) | SS-05 TurnstileAccess (PKG-12) | P10 ánh xạ sang subsystem; thiết bị gọi vào qua API, người dùng chỉ quét mã và đi qua cửa quay. Cách báo cho người quét: Q-70. Màn hình hiển thị mã QR của hội viên không có boundary: Q-97 |

## 3. Bảng tổng hợp đánh giá chuẩn

Tổng hợp mục g) của SCR-01 đến SCR-16 và đánh giá Shneiderman cho toàn bộ màn hình; đánh giá ui-standards.md ở giai đoạn 1 nằm cuối ui-standards.md.

| SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-01 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-001, UC-002, UC-003 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-01 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ | - |
| SCR-01 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-01 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Các thẻ lối vào là danh sách (list) các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-01 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 64 dp, rộng hết vùng nội dung, khoảng cách 8 dp | - |
| SCR-01 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Màn hình gốc của tác nhân không có nút Quay lại và không có cử chỉ quay lại về màn hình khác của phần mềm, đúng hành vi iOS | - |
| SCR-02 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-006, UC-011, UC-012, UC-018, UC-019, UC-020, UC-023, UC-025 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-02 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ (cuộn dọc khi dài hơn màn hình) | - |
| SCR-02 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-02 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Các thẻ lối vào là danh sách (list) các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-02 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 64 dp, rộng hết vùng nội dung, khoảng cách 8 dp | - |
| SCR-02 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Thứ tự lối vào theo mã UC tăng dần (UI-STT 44) như thứ tự các use case của hội viên trong P02; nút Trang chủ ở mọi màn hình khác của ACT-02 đều dẫn về màn hình này | - |
| SCR-02 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Màn hình gốc của tác nhân không có nút Quay lại và không có cử chỉ quay lại về màn hình khác của phần mềm, đúng hành vi iOS | - |
| SCR-03 | Nielsen 6 Nhận biết thay vì nhớ lại | Vi phạm đã sửa | Áp nguyên UI-STT 33 (hai nhóm nút chọn riêng cho thời hạn và loại gói) thì giá của từng tổ hợp (Dữ liệu ra 1 STT 4) không hiển thị cạnh lựa chọn, người dùng phải nhớ giá và có thể chọn tổ hợp chưa có giá gói. Màn hình dùng một nhóm thẻ chọn, mỗi thẻ là một tổ hợp thời hạn và loại kèm giá | Thẻ chọn theo UI-STT 34; đề xuất bổ sung ngoại lệ vào UI-STT 33 (mục Đề xuất sửa artifact trước) |
| SCR-03 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm nên trạng thái chọn rõ. Chưa quy định màn hình khi không có giá gói nào để hiển thị (Q-103) | Q-103 |
| SCR-03 | Nielsen 5 Ngăn lỗi | Đạt | Chỉ chọn được tổ hợp có trong danh sách giá gói hiện hành; thiếu lựa chọn thì MSG-01 trước khi gửi máy chủ | - |
| SCR-03 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Đặc tả có Dữ liệu vào Gói đang có cần gia hạn nhưng chưa quy định cách chỉ định (Q-56), nên màn hình chưa có điều khiển để hội viên gia hạn một gói cụ thể | Q-56; không tự thêm điều khiển |
| SCR-03 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Nhóm thẻ là nhóm nút chọn (radiogroup) có nhãn Chọn gói tập; mỗi thẻ đọc thành một câu: thời hạn, loại, giá | - |
| SCR-03 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm; lỗi MSG-01 có biểu tượng và chữ | - |
| SCR-03 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 72 dp, vùng bấm là cả thẻ, khoảng cách 8 dp | - |
| SCR-03 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhóm thẻ có nhãn Chọn gói tập kèm dấu *, chú thích loại gói dưới nhóm | - |
| SCR-03 | Material Design (Android): vùng chạm, một hành động chính | Đạt | Một nút chính Tiếp tục cao 48 dp; thẻ cao tối thiểu 72 dp | - |
| SCR-03 | Apple HIG (iOS): vùng chạm, điều hướng quay lại | Đạt | Vùng chạm lớn hơn 44 pt; cử chỉ quay lại về SCR-02 theo UI-STT 15 | - |
| SCR-03 | Baymard: đánh dấu bắt buộc, thông điệp lỗi cạnh trường | Đạt | Nhãn nhóm có dấu *, đầu màn hình có chú thích * Bắt buộc, MSG-01 đặt ngay dưới nhãn nhóm | - |
| SCR-04 | Nielsen 5 Ngăn lỗi | Đạt | Màn hình xác nhận riêng cho dữ liệu tài chính (UI-STT 74): tóm tắt, nút Quay lại sửa, nút Xác nhận mua; nút khoá nhấn lại khi đang xử lý để không gửi hai lần cùng một yêu cầu (UI-STT 41) | - |
| SCR-04 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Nút đổi sang Đang xử lý, MSG-10 từ giây thứ 1, MSG-04 khi chờ thanh toán, kết quả bằng MSG-02, MSG-03 hoặc SCR-05 | - |
| SCR-04 | Nielsen 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | Khi MSG-04 hiển thị hội viên không có nút nào để huỷ hoặc rời; đặc tả không có thao tác huỷ đơn chưa thanh toán (Q-57) và chưa rõ giao diện thanh toán (Q-96) | Q-57, Q-96; không tự thêm nút huỷ |
| SCR-04 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | MSG-03 chưa nêu được việc làm tiếp sau khi giao dịch không thành công vì đặc tả chờ Q-13 | Q-13 |
| SCR-04 | Nielsen 1 Hiển thị trạng thái hệ thống (tóm tắt đơn) | Vi phạm còn mở | Giá gói ở SCR-03 là 1.200.000 đ còn số tiền phải trả là 1.080.000 đ; Dữ liệu ra 2 không có mức giảm khuyến mãi nên chênh lệch không được giải thích trên màn hình | Q-09; đề xuất sửa P04 Dữ liệu ra 2 (mục Đề xuất sửa artifact trước); không tự thêm trường |
| SCR-04 | Baymard: hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Đạt | Ba dòng tóm tắt gồm gói tập, ngày bắt đầu, số tiền phải trả, kèm nút Quay lại sửa | - |
| SCR-04 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Có tóm tắt để kiểm tra, sửa được bằng Quay lại, xác nhận bằng nút đặt tên theo hành động Xác nhận mua (UI-STT 75) | - |
| SCR-04 | WCAG 3.3.7 Không bắt nhập lại | Đạt | Gói đã chọn ở SCR-03 được chuyển sang và được giữ khi dùng Quay lại | - |
| SCR-04 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | MSG-04 và MSG-10 có vai trò status, được đọc mà không chuyển tiêu điểm (UI-STT 57) | - |
| SCR-04 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Khi mở MSG-02 hoặc MSG-03, tiêu điểm vào nút duy nhất của hộp; khi đóng trở về nút Xác nhận mua (UI-STT 52) | - |
| SCR-04 | Material Design (Android): một hành động chính | Đạt | Một nút chính Xác nhận mua ở trên, nút phụ Quay lại ở dưới, cao 48 dp | - |
| SCR-04 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Cử chỉ quay lại làm giống nút Quay lại khi đơn chưa tạo (UI-STT 15) | - |
| SCR-05 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Dải thông báo thành công MSG-13 và dòng Trạng thái gói Đã kích hoạt cho biết kết quả ngay khi mở màn hình | - |
| SCR-05 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ ba dòng thông tin của Dữ liệu ra 3 và dải thông báo; không thêm nút hay thông tin ngoài đặc tả | - |
| SCR-05 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Rời màn hình bằng nút Trang chủ hoặc nút quay lại của hệ thống, đều về SCR-02 | - |
| SCR-05 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Dải thông báo có biểu tượng dấu tích và chữ, không chỉ màu xanh | - |
| SCR-05 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Dải thông báo có vai trò status, được đọc khi mở màn hình mà không chuyển tiêu điểm | - |
| SCR-05 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ dải thông báo #1C1F2A trên nền #E8F5EC đo 14,63:1; biểu tượng và viền #1B6E3C trên nền #E8F5EC đo 5,60:1 (cặp màu này nền #E8F5EC chưa được đo ở ui-standards.md, UI-STT 22 chỉ đo #1B6E3C trên trắng) | - |
| SCR-05 | Material Design (Android): một hành động chính | Không áp dụng | Màn hình kết quả không có nút hành động theo UI-STT 25 | - |
| SCR-05 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Cử chỉ quay lại về SCR-02, không về màn hình xác nhận đã ghi dữ liệu | - |
| SCR-06 | Nielsen 6 Nhận biết thay vì nhớ lại | Vi phạm đã sửa | Áp nguyên UI-STT 33 (trên 5 giá trị thì dùng danh sách chọn, mỗi mục một dòng cao 48 dp) thì loại lớp, phòng, huấn luyện viên và giờ học (Dữ liệu ra 1 STT 1-4) không hiển thị cùng lúc để hội viên so sánh, phải mở từng mục. Màn hình dùng nhóm thẻ chọn, mỗi thẻ là một lớp với đủ bốn thông tin | Thẻ chọn theo UI-STT 34; đề xuất mở rộng ngoại lệ của UI-STT 33 ghi ở mục Đề xuất sửa artifact trước (cùng đề xuất đã ghi ở SCR-03) |
| SCR-06 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm; MSG-10 hiện từ giây thứ 1. Chưa quy định màn hình khi lịch không có lớp nào để hiển thị (Q-105) | Q-105 |
| SCR-06 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Lịch có thể rất dài (khoảng 25 lớp mỗi ngày mỗi chi nhánh, GL-29) mà đặc tả không nêu phạm vi lịch (Q-83) và không có chức năng lọc hay tìm kiếm | Q-83; không tự thêm lọc hay tìm kiếm (UI-STT 37) |
| SCR-06 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | MSG-05, MSG-06, MSG-08 nêu quy tắc và việc làm tiếp theo. Nội dung MSG-07 dựa trên BR-06, còn BR-07 mâu thuẫn BR-06 nên hội viên có thể được báo thời điểm mở đặt chỗ chưa đúng | Q-11, Q-58 |
| SCR-06 | Nielsen 5 Ngăn lỗi | Đạt | Đặt chỗ không phải thao tác tài chính và hoàn tác được bằng UC-011 nên không thêm bước xác nhận (UI-STT 74). Hướng chọn có hai phía (vào danh sách chờ) có hộp xác nhận MSG-09, nút an toàn Không vào nhận tiêu điểm đầu tiên (UI-STT 52) | - |
| SCR-06 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Nhóm thẻ là nhóm nút chọn (radiogroup) có nhãn Chọn lớp nhóm; mỗi thẻ đọc thành một câu: loại lớp, giờ học, phòng, huấn luyện viên | - |
| SCR-06 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm; MSG-01 có biểu tượng lỗi và chữ | - |
| SCR-06 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Hộp MSG-09 giữ tiêu điểm trong hộp, vào nút Không vào; khi đóng, tiêu điểm trở về nút Đặt chỗ đã mở hộp (UI-STT 52) | - |
| SCR-06 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 72 dp, vùng bấm là cả thẻ, khoảng cách 8 dp; nút Đặt chỗ cao 48 dp | - |
| SCR-06 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhóm thẻ có nhãn Chọn lớp nhóm kèm dấu *, đầu màn hình có chú thích * Bắt buộc | - |
| SCR-06 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | MSG-10 có vai trò status; MSG-01 có vai trò alert, đọc không chuyển tiêu điểm; hộp thông điệp là hộp thoại có nhãn tiêu đề | - |
| SCR-06 | Material Design (Android): vùng chạm, một hành động chính | Đạt | Một nút chính Đặt chỗ cao 48 dp; hộp MSG-09 có một nút chính Vào danh sách chờ và một nút phụ Không vào | - |
| SCR-06 | Apple HIG (iOS): vùng chạm, điều hướng quay lại | Đạt | Vùng chạm lớn hơn 44 pt; cử chỉ quay lại về SCR-02 theo UI-STT 15, đóng hộp thông điệp khi hộp đang mở | - |
| SCR-06 | Baymard: đánh dấu bắt buộc, thông điệp lỗi cạnh trường | Đạt | Nhãn nhóm có dấu *, đầu màn hình có chú thích * Bắt buộc, MSG-01 đặt ngay dưới nhãn nhóm; lỗi nghiệp vụ dùng hộp thoại vì không gắn với một trường (UI-STT 54, 59) | - |
| SCR-07 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Dải thông báo thành công MSG-14 và bốn dòng thông tin của lớp đã đặt cho biết kết quả ngay khi mở màn hình | - |
| SCR-07 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ bốn dòng thông tin của Dữ liệu ra 2 và dải thông báo; không thêm nút hay thông tin ngoài đặc tả | - |
| SCR-07 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Rời màn hình bằng nút Trang chủ hoặc nút quay lại của hệ thống, đều về SCR-02. Muốn bỏ chỗ vừa đặt thì dùng UC-011 từ SCR-02; màn hình không thêm nút huỷ vì đặc tả UC-010 không có (UI-STT 77) | - |
| SCR-07 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Dải thông báo có biểu tượng dấu tích và chữ, không chỉ màu xanh | - |
| SCR-07 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ dải thông báo #1C1F2A trên nền #E8F5EC đo 14,63:1; biểu tượng và viền #1B6E3C trên nền #E8F5EC đo 5,60:1 (cặp màu nền #E8F5EC chưa được đo ở ui-standards.md, UI-STT 22 chỉ đo #1B6E3C trên trắng) | - |
| SCR-07 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Dải thông báo có vai trò status, được đọc khi mở màn hình mà không chuyển tiêu điểm | - |
| SCR-07 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Cử chỉ quay lại về SCR-02, không về SCR-06 vì chỗ đã đặt đã được lưu | - |
| SCR-08 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Dải thông báo thành công MSG-15 và ba dòng thông tin (lớp, giờ học, vị trí) cho biết hội viên đã vào danh sách chờ và đang đứng thứ mấy | - |
| SCR-08 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ ba dòng thông tin của Dữ liệu ra 3 và dải thông báo; không thêm nút hay thông tin ngoài đặc tả | - |
| SCR-08 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Rời màn hình bằng nút Trang chủ hoặc nút quay lại của hệ thống, đều về SCR-02. Muốn rút khỏi danh sách chờ thì dùng chức năng huỷ của use case khác nếu có; màn hình không thêm nút vì đặc tả UC-010 không có (UI-STT 77) | - |
| SCR-08 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Dải thông báo có biểu tượng dấu tích và chữ, không chỉ màu xanh | - |
| SCR-08 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Cùng cặp màu dải thông báo đã đo ở SCR-07: chữ #1C1F2A trên nền #E8F5EC 14,63:1; biểu tượng và viền #1B6E3C trên nền #E8F5EC 5,60:1 | - |
| SCR-08 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Dải thông báo có vai trò status, được đọc khi mở màn hình mà không chuyển tiêu điểm | - |
| SCR-08 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Cử chỉ quay lại về SCR-02, không về SCR-06 vì hội viên đã vào danh sách chờ | - |
| SCR-09 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-021, UC-024, UC-025 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-09 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ | - |
| SCR-09 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-09 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Các thẻ lối vào là danh sách (list) các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-09 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 64 dp, rộng hết vùng nội dung, khoảng cách 8 dp | - |
| SCR-09 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Màn hình gốc của tác nhân không có nút Quay lại và không có cử chỉ quay lại về màn hình khác của phần mềm, đúng hành vi iOS | - |
| SCR-10 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-007, UC-017 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-10 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ | - |
| SCR-10 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-10 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Menu trái là vùng điều hướng (nav) có aria-current ở mục Trang chủ; các thẻ lối vào là danh sách các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-10 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao 64 px, rộng 320 px; mục menu cao 44 px | - |
| SCR-10 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu trái có cùng thứ tự các mục với SCR-11, SCR-12, SCR-13, SCR-14 (UI-STT 46, 48) | - |
| SCR-11 | Nielsen 6 Nhận biết thay vì nhớ lại (bảng gói) | Vi phạm đã sửa | Áp nguyên UI-STT 33 (hai nhóm nút chọn riêng cho thời hạn và loại gói) thì giá của từng tổ hợp (Dữ liệu ra 1 STT 4) không hiển thị cạnh lựa chọn và có thể chọn tổ hợp chưa có giá gói. Màn hình dùng một bảng, mỗi dòng là một tổ hợp thời hạn và loại kèm giá và nút chọn | Bảng theo UI-STT 34; đề xuất bổ sung ngoại lệ vào UI-STT 33 đã ghi ở SCR-03 |
| SCR-11 | Nielsen 6 Nhận biết thay vì nhớ lại (người mua) | Vi phạm còn mở | Lễ tân phải tự nhập thông tin người mua mà đặc tả chưa nêu thông tin nào dùng để nhận ra người mua và có danh sách để chọn hay không | Q-104, Q-01 |
| SCR-11 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Chưa quy định màn hình khi không có giá gói nào để hiển thị | Q-103 |
| SCR-11 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Đặc tả có Dữ liệu vào Gói đang có cần gia hạn nhưng chưa quy định cách chỉ định, nên màn hình chưa có điều khiển để lễ tân gia hạn một gói cụ thể | Q-56; không tự thêm điều khiển |
| SCR-11 | Baymard: form một cột, nhãn trên ô nhập, không placeholder thay nhãn | Đạt | Bảng gói rồi ô Người mua gói xếp một cột; nhãn Người mua gói nằm trên ô nhập; ô nhập không có placeholder | - |
| SCR-11 | Baymard: kiểm tra khi rời trường, thông điệp lỗi cạnh trường | Đạt | Ô Người mua gói kiểm tra bắt buộc khi rời trường, MSG-01 ngay dưới ô; nhấn Tiếp tục chuyển tiêu điểm tới trường sai đầu tiên | - |
| SCR-11 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Bảng gói dùng th cho tiêu đề cột, mỗi dòng có nút chọn gắn nhãn đọc thành thời hạn, loại, giá; menu có aria-current ở mục đang chọn | - |
| SCR-11 | WCAG 1.4.10 Reflow (web) | Đạt | Dưới 1024 px bảng 5 cột cuộn ngang trong khung riêng của bảng, nội dung xếp một cột (UI-STT 3) | - |
| SCR-11 | WCAG 2.1.1 Bàn phím | Đạt | Mũi tên chọn dòng của bảng, Tab tới ô Người mua gói và nút Tiếp tục, Enter ở ô Người mua gói kích hoạt nút chính (UI-STT 49, 50) | - |
| SCR-11 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu có cùng thứ tự các mục với SCR-10, SCR-12, SCR-13, SCR-14 (UI-STT 46, 48) | - |
| SCR-12 | Nielsen 5 Ngăn lỗi | Đạt | Màn hình xác nhận riêng cho dữ liệu tài chính (UI-STT 74): tóm tắt, nút Quay lại sửa, nút Xác nhận bán; nút khoá nhấn lại khi đang xử lý để không tạo hai đơn cho một lần bán | - |
| SCR-12 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Nút Quay lại về SCR-11 giữ nguyên dữ liệu khi đơn chưa tạo; menu cho phép rời bất cứ lúc nào | - |
| SCR-12 | Nielsen 1 Hiển thị trạng thái hệ thống (tóm tắt đơn) | Vi phạm còn mở | Giá gói ở SCR-11 là 1.200.000 đ còn số tiền phải trả là 1.080.000 đ; Dữ liệu ra 2 không có mức giảm khuyến mãi nên chênh lệch không được giải thích trên màn hình | Q-09; đề xuất sửa P04 Dữ liệu ra 2 đã ghi ở SCR-04; không tự thêm trường |
| SCR-12 | Baymard: hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Đạt | Bốn dòng tóm tắt gồm gói tập, người mua gói, ngày bắt đầu, số tiền phải trả, kèm nút Quay lại sửa | - |
| SCR-12 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Có tóm tắt để kiểm tra, sửa được bằng Quay lại, xác nhận bằng nút đặt tên theo hành động Xác nhận bán (UI-STT 75) | - |
| SCR-12 | WCAG 3.3.7 Không bắt nhập lại | Đạt | Gói và người mua đã chọn ở SCR-11 được chuyển sang và được giữ khi dùng Quay lại | - |
| SCR-12 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Thứ tự Tab: logo, menu, nút Quay lại rồi nút Xác nhận bán (nút phụ rồi nút chính, UI-STT 42) | - |
| SCR-12 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu cùng thứ tự các mục với SCR-10, SCR-11, SCR-13, SCR-14 (UI-STT 46, 48) | - |
| SCR-13 | Nielsen 5 Ngăn lỗi (mã giao dịch POS) | Vi phạm còn mở | Chưa quy định định dạng và kiểm tra trùng của mã giao dịch POS, nên giao diện không ngăn được nhập sai hoặc nhập trùng mã | Q-55 |
| SCR-13 | Nielsen 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | Đơn đã tạo nên không có nút Quay lại, và không có thao tác huỷ đơn chưa thu tiền; lễ tân chỉ rời bằng menu để lại đơn chờ thanh toán | Q-57, Q-25; không tự thêm nút huỷ |
| SCR-13 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | Chưa có thông điệp khi hệ thống hoá đơn điện tử không nhận dữ liệu giao dịch sau khi lễ tân xác nhận đã thu | Q-54 |
| SCR-13 | Nielsen 2 Khớp giữa hệ thống và thế giới thực | Đạt | Hai lựa chọn gọi là Tiền mặt và Thẻ ngân hàng qua máy POS, đúng thuật ngữ P05 (Giao dịch thu tiền GL-12, Máy POS GL-33) | - |
| SCR-13 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Số tiền phải trả, hình thức thu và mã hiển thị trên cùng màn hình trước khi nhấn; không chọn sẵn hình thức thu; nhãn nút chính có số tiền (UI-STT 75) | - |
| SCR-13 | WCAG 3.2.2 Khi nhập liệu (ngoài danh sách F7) | Đạt | Chọn Thẻ ngân hàng qua máy POS chỉ hiện thêm ô mã bên dưới, không tự chuyển tiêu điểm hay chuyển màn hình | - |
| SCR-13 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Nhóm nút chọn Hình thức thu có nhãn nhóm (fieldset, legend); ô Mã giao dịch POS gắn nhãn bằng for và id và gắn chú thích bằng aria-describedby | - |
| SCR-13 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Ô mã có nhãn Mã giao dịch POS kèm dấu * và chú thích Nhập mã in trên hoá đơn POS (nội dung theo GL-31) | - |
| SCR-13 | Baymard: nhãn trên ô nhập, không placeholder; chấp nhận nhiều định dạng nhập | Đạt | Nhãn đặt trên ô, không có placeholder; mã được cắt khoảng trắng đầu cuối nên mã dán từ hoá đơn không bị từ chối vì khoảng trắng (UI-STT 40) | - |
| SCR-13 | Baymard: kiểm tra khi rời trường, giữ dữ liệu khi báo lỗi | Đạt | Ô mã kiểm tra bắt buộc khi rời trường; MSG-11, MSG-12 giữ hình thức thu và mã đã nhập | - |
| SCR-14 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Dải thông báo thành công MSG-13 và dòng Trạng thái gói Đã kích hoạt cho lễ tân biết kết quả để báo khách ngay khi mở màn hình | - |
| SCR-14 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ ba dòng thông tin của Dữ liệu ra 3 và dải thông báo; không thêm nút hay thông tin ngoài đặc tả | - |
| SCR-14 | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | Rời màn hình bằng menu về SCR-10 hoặc SCR-11 bất cứ lúc nào | - |
| SCR-14 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Dải thông báo có biểu tượng dấu tích và chữ, không chỉ màu xanh | - |
| SCR-14 | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | Chữ dải thông báo #1C1F2A trên nền #E8F5EC đo 14,63:1; biểu tượng và viền #1B6E3C trên nền #E8F5EC đo 5,60:1 (cặp màu này nền #E8F5EC chưa được đo ở ui-standards.md, UI-STT 22 chỉ đo #1B6E3C trên trắng) | - |
| SCR-14 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | Dải thông báo có vai trò status, được đọc khi mở màn hình mà không chuyển tiêu điểm | - |
| SCR-14 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu cùng thứ tự các mục với SCR-10, SCR-11, SCR-12, SCR-13 (UI-STT 46, 48) | - |
| SCR-15 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-009, UC-014 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-15 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ | - |
| SCR-15 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-15 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Menu trái là vùng điều hướng (nav) có aria-current ở mục Trang chủ; các thẻ lối vào là danh sách các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-15 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao 64 px, rộng 320 px; mục menu cao 44 px | - |
| SCR-16 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Lối vào UC-026, UC-027, UC-028 chưa có màn hình đích: người dùng nhấn thẻ hoặc mục nhưng màn hình không phản hồi gì | Hết khi use case có đặc tả P04 và màn hình (phạm vi hiện chỉ bốn use case theo YEU_CAU_BO_SUNG); không tự thêm thông điệp vì đặc tả không có |
| SCR-16 | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | Mọi use case của tác nhân hiển thị cùng lúc bằng tên tiếng Việt theo P02, người dùng chọn mà không phải nhớ | - |
| SCR-16 | Nielsen 8 Thẩm mỹ và tối giản | Đạt | Chỉ có lối vào use case của tác nhân (P11a mục A2, UI-STT 44); không thêm nút, thông tin hay chức năng khác | - |
| SCR-16 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Menu trái là vùng điều hướng (nav) có aria-current ở mục Trang chủ; các thẻ lối vào là danh sách các liên kết; tiêu đề màn hình là tiêu đề cấp 1 | - |
| SCR-16 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao 64 px, rộng 320 px; mục menu cao 44 px | - |
| Toàn bộ màn hình | Shneiderman 1 Nhất quán | Đạt | Cùng bố cục vùng, vị trí và nhãn nút (UI-STT 10, 11, 14, 29); bốn màn hình kết quả (SCR-05, SCR-07, SCR-08, SCR-14) cùng dải thông báo thành công; nhóm thẻ chọn ở SCR-03 và SCR-06, bảng chọn ở SCR-11 cùng cách đánh dấu mục đang chọn; nút Trang chủ (di động) hoặc menu trái (web) ở mọi màn hình trừ hộp thông điệp | - |
| Toàn bộ màn hình | Shneiderman 2 Khả dụng cho mọi người dùng | Đạt | Không còn vi phạm WCAG 2.2 AA chưa xử lý ở 16 màn hình; web dùng được chỉ bằng bàn phím, di động dùng được với TalkBack và VoiceOver, phóng to chữ 200% (UI-STT 70, 71) | - |
| Toàn bộ màn hình | Shneiderman 3 Phản hồi đầy đủ | Vi phạm còn mở | Mọi thao tác ghi dữ liệu có chỉ báo MSG-10 từ giây thứ 1 và kết thúc bằng màn hình kết quả hoặc hộp thông điệp. Còn thiếu phản hồi ở lối vào chưa có màn hình đích trên 6 màn hình điều hướng (SCR-01, SCR-02, SCR-09, SCR-10, SCR-15, SCR-16) và ở trường hợp lịch hoặc bảng gói rỗng | Lối vào: hết khi use case có đặc tả và màn hình. Lịch, bảng gói rỗng: Q-103, Q-105 |
| Toàn bộ màn hình | Shneiderman 4 Hội thoại có điểm kết thúc rõ | Đạt | UC-005 kết thúc ở SCR-05 (hội viên) hoặc SCR-14 (lễ tân); UC-010 kết thúc ở SCR-07 hoặc SCR-08, kết thúc thất bại bằng hộp MSG-05 đến MSG-09 rồi ở lại SCR-06; mọi màn hình kết quả không có nút hành động (UI-STT 25). Giao diện chờ thanh toán trực tuyến của UC-005 chưa chốt | Q-96 |
| Toàn bộ màn hình | Shneiderman 5 Ngăn lỗi | Vi phạm còn mở | Có bước xác nhận trước ghi dữ liệu tài chính (SCR-04, SCR-12, SCR-13), hộp xác nhận MSG-09, tiêu điểm vào nút an toàn, chặn gửi hai lần (UI-STT 41, 52, 74). Còn mở: quy tắc mã giao dịch POS ở SCR-13 | Q-55 |
| Toàn bộ màn hình | Shneiderman 6 Hoàn tác dễ dàng | Vi phạm còn mở | Chỉ có nút Quay lại ở hai màn hình xác nhận trước khi đơn được tạo (SCR-04, SCR-12) và UC-011 cho chỗ đã đặt; chưa có cách huỷ đơn mua đã tạo nhưng chưa thanh toán. SCR-07, SCR-08 không thêm nút huỷ vì đặc tả UC-010 không có | Q-57; không tự thêm hoàn tác |
| Toàn bộ màn hình | Shneiderman 7 Người dùng làm chủ | Đạt | Nút Quay lại ở màn hình xác nhận chưa ghi dữ liệu, nút Trang chủ hoặc menu, Esc hoặc nút quay lại của hệ thống đóng hộp thông điệp (UI-STT 15, 45, 46, 51); không có thao tác tự chạy khi mở màn hình | - |
| Toàn bộ màn hình | Shneiderman 8 Giảm tải trí nhớ ngắn hạn | Đạt | Màn hình kết quả nhắc lại dữ liệu (SCR-05, SCR-07, SCR-08, SCR-14), tóm tắt trước xác nhận (SCR-04, SCR-12), lịch, bảng gói và lối vào hiển thị đủ thông tin cùng lúc (SCR-02, SCR-03, SCR-06, SCR-11). Ngoại lệ ở SCR-11 là trường Người mua gói, đã tính ở dòng Nielsen 6 của SCR-11 | Q-104 |

Thống kê: 137 dòng gồm 109 Đạt, 3 Vi phạm đã sửa, 24 Vi phạm còn mở, 1 Không áp dụng. Mọi dòng Vi phạm còn mở gắn mã Q, trừ 6 dòng Nielsen 1 của màn hình điều hướng và phần lối vào của dòng Shneiderman 3 (lối vào chưa có màn hình đích, hết khi use case được đặc tả). Không còn vi phạm WCAG AA chưa có cách xử lý. Mỗi màn hình chỉ có dòng Vi phạm đã sửa, Vi phạm còn mở và dòng Đạt có bằng chứng riêng; tiêu chí không có dòng đạt theo ui-standards.md mục 3.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-96 | Hội viên thanh toán trực tuyến trên giao diện nào: trang của cổng thanh toán mở trong ứng dụng, trang mở ở trình duyệt ngoài, hay biểu mẫu nhập ngay trong ứng dụng; trong lúc chờ kết quả (BR-04: 15 phút), ứng dụng hiển thị màn hình nào và hội viên có rời màn hình được không? (Trang của cổng mở trong ứng dụng / Mở trình duyệt ngoài / Biểu mẫu trong ứng dụng / Khác - nêu rõ) | SCR-04, SCR-05, TR-06; MSG-03, MSG-04; có thể cần thêm màn hình hoặc P11b (IF-01, IF-08) | P04 UC-005 bước 9, 10: cổng 'thu tiền thanh toán của hội viên' không nêu giao diện thu tiền; P08 AC-B-PaymentGateway chỉ có requestPayment, returnPaymentResult |
| Q-97 | Màn hình hiển thị mã QR của hội viên trên ứng dụng (tiền điều kiện của UC-018) có thuộc phần mềm cần thiết kế không, và thuộc use case nào? (Là một bước hoặc một use case riêng của ACT-02 - nêu rõ / Không cần màn hình riêng - nêu rõ) | Lối vào UC-018 ở SCR-02 hiện ghi Chưa có màn hình đích; thiếu màn hình cho REQ-39; P04 UC-018, P08, P10 (PKG-05) | P04 UC-018 Tiền điều kiện: mã QR đang hiển thị trên ứng dụng; P09 PKG-05 liệt kê UC-018 (hiển thị mã QR) nhưng P08 không có boundary giao diện người dùng cho việc hiển thị mã |
| Q-98 | Khi lễ tân bán gói tại quầy, khách có thể thanh toán qua cổng thanh toán trực tuyến (bước 9, 10 của luồng chính) hay chỉ trả tiền mặt hoặc quẹt thẻ qua máy POS (luồng 8a, 8b)? (Chỉ tiền mặt hoặc POS / Có cả cổng thanh toán - nêu cách khách thanh toán tại quầy) | SCR-13 (các hình thức thu), TR-16; P07 UC-005 SD2 (alt ba toán hạng) | Mục 2 câu 4 của nguồn chỉ nêu tiền mặt hoặc POS tại quầy; P04 UC-005 bước 9, 10 áp dụng chung cho Hội viên và Lễ tân |

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P10 | F3, F4 (PKG-05) | Màn hình điều hướng SCR-01 của ACT-01 chưa có lớp thiết kế giao diện tương ứng trong P10 | Thêm phần tử View điều hướng của ACT-01 vào PKG-05 MemberMobileUI |
| P10 | F3, F4 (PKG-05) | Màn hình điều hướng SCR-02 của ACT-02 chưa có lớp thiết kế giao diện tương ứng trong P10 | Thêm phần tử View điều hướng của ACT-02 vào PKG-05 MemberMobileUI |
| P10 | F3, F4 (PKG-06) | Màn hình điều hướng SCR-09 của ACT-04 chưa có lớp thiết kế giao diện tương ứng trong P10 | Thêm phần tử View điều hướng của ACT-04 vào PKG-06 TrainerMobileUI |
| P10 | F3, F4 (PKG-07) | Màn hình điều hướng SCR-10 của ACT-05 chưa có lớp thiết kế giao diện tương ứng trong P10 | Thêm phần tử View điều hướng của ACT-05 vào PKG-07 ReceptionWebUI |
| P10 | F3, F4 (PKG-08) | Màn hình điều hướng SCR-15 của ACT-06 chưa có lớp thiết kế giao diện tương ứng trong P10 | Thêm phần tử View điều hướng của ACT-06 vào PKG-08 BranchManagerWebUI |
| P10 | F3, F4 (PKG-09) | Màn hình điều hướng SCR-16 của ACT-07 chưa có lớp thiết kế giao diện tương ứng trong P10 | Thêm phần tử View điều hướng của ACT-07 vào PKG-09 ChainDirectorWebUI |
| P04, P08, P10 | P04 UC-018 Tiền điều kiện; P08 F3 AC-B-TurnstileDevice; P10 PKG-05 | Hiển thị mã QR hội viên trên ứng dụng là tiền điều kiện của UC-018, không có boundary giao diện người dùng nên không có màn hình (lối vào ở SCR-02 ghi Chưa có màn hình đích) | Khi Q-97 có trả lời là thuộc phần mềm: P04 thêm bước hoặc use case hiển thị mã QR, P08 thêm boundary giao diện người dùng, P10 thêm View vào PKG-05, rồi chạy lại P11a giai đoạn 1 để thêm màn hình. Chưa áp dụng |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 2: 3 boundary giao diện người dùng của P10 F3 đều có màn hình; 5 boundary còn lại có dòng ở bảng Boundary không có màn hình. P08 không có boundary loại Kênh thông báo; hai cổng thông báo mang loại Giao diện hệ thống và được xử lý như kênh thông báo. Mỗi màn hình nghiệp vụ có boundary nguồn, 6 màn hình còn lại là màn hình điều hướng.
- UC-015 (tác nhân thời gian, chỉ gửi thông báo đẩy và SMS) và UC-018 (hội viên chỉ quét mã ở thiết bị) không có màn hình nghiệp vụ, đúng với P10 F3. UC-005 có 7 màn hình vì hai tác nhân chính dùng hai boundary riêng (3 và 4 màn hình), không vượt ngưỡng 6 cho mỗi boundary.
- Màn hình điều hướng chứa lối vào các use case chưa đặc tả (ghi Chưa có màn hình đích khi viết đặc tả giai đoạn 2). UC-004 Đăng nhập (subfunction của ACT-02) không là lối vào trên SCR-02 vì xảy ra trước phiên làm việc; vị trí lối vào đăng nhập: Q-99 (xem screen-transition.md). UC-001, UC-002 chỉ gán cho ACT-01 vì Q-46 chưa trả lời. Khách vãng lai (ACT-03) không dùng phần mềm nên không có màn hình.
- Một View cho mỗi boundary phục vụ 3 đến 4 màn hình (cột Lớp thiết kế); việc tách View thành nhiều lớp thiết kế thuộc P12, không cần sửa P10.
- SCR-13: gộp hai hình thức thu (tiền mặt, POS) vào một màn hình vì cùng mục tiêu con và cùng một quyết định (xác nhận đã thu); nếu Q-98 trả lời có cả cổng thanh toán thì thêm hình thức thu.
- Lựa chọn giữa hai quy tắc (C9): A2 coi hộp thông điệp ngắn không cần SCR riêng, nên các thông báo từ chối của UC-010 (luồng 4a, 5a, 5b, 6a) và hộp Lớp đã đủ chỗ (luồng 7a1, 7a2) là MSG (MSG-05 đến MSG-09) thay vì màn hình; hộp MSG-09 có hai nút nhưng là mẫu xác nhận có hoặc không chuẩn.
- Giai đoạn 2 còn lại: viết đặc tả 10 màn hình nghiệp vụ và 6 màn hình điều hướng, rồi lập bảng tổng hợp F7 ở mục 3 và gom mục h) vào ui-standards.md ở lần chạy cuối.
