# P11a - Danh sách màn hình - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 1) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005, UC-010, UC-015, UC-018 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa, Từ đồng nghĩa không dùng); P06-supplementary-spec.md (phiên bản 1.0; Mục 3 đến Mục 6); P07-uc-analysis/ bốn file (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4, Đề xuất sửa artifact trước, Vấn đề còn mở). Mã Q, ASM lớn nhất do người dùng cung cấp (Q-94; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả. CHE_DO_CHAY: Giai đoạn 1. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (dùng ở đặc tả màn hình giai đoạn 2). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; các use case khác của P02 chưa đặc tả, màn hình của chúng chỉ là lối vào trên màn hình điều hướng; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; ba đề xuất của P10 cho P08, P09 chỉ đổi cấu trúc thiết kế nên P08, P09 không chạy lại |
| Phạm vi | Toàn hệ thống (giai đoạn 1); màn hình nghiệp vụ cho UC-005, UC-010; UC-015, UC-018 không có màn hình; các use case khác chỉ là lối vào trên màn hình điều hướng |
| Mã Q, ASM cuối đã cấp | Q-99; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

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

Chưa có. Bảng này lập từ mục g) của các SCR ở lần chạy giai đoạn 2 cuối cùng hoặc chế độ Toàn bộ; đánh giá ui-standards.md ở giai đoạn 1 nằm cuối ui-standards.md.


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
