# P10 - Phần tử thiết kế - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P10 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG giữ nguyên, CONG_NGHE thay theo khối F11 của P09); P08-analysis-model.md (phiên bản 1.0; F3, F4, Câu hỏi mở, Giả định); P09-architecture.md (phiên bản 1.0; F3, F4, F5, F6, F7, F11, Câu hỏi mở, Giả định); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P06-supplementary-spec.md (phiên bản 1.0; Mục 3 đến Mục 5); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2). P07-uc-analysis/*.md không tra lại vì P08 F4 đã dẫn link của P07. Mã Q, ASM lớn nhất do người dùng cung cấp (Q-94; chưa có ASM). TIEU_CHI_NHOM_PACKAGE: Không có. KHA_NANG_THAY_DOI_GIAO_DIEN: cổng thanh toán trực tuyến và cổng SMS có thể đổi nhà cung cấp; hệ thống hoá đơn điện tử chưa có tài liệu API nên giao diện chưa ổn định; giao thức của cửa quay do nhà cung cấp thiết bị hiện tại quy định và ổn định; giao diện người dùng của ứng dụng di động và ứng dụng web ổn định. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018 (P08 ghi 24 use case còn lại là Chưa phân tích); đề xuất sửa artifact trước của các bước trước chưa áp dụng vì chờ câu trả lời Q |
| Phạm vi | Toàn hệ thống (28 use case của P02); phần tử thiết kế có lớp phân tích nguồn chỉ cho UC-005, UC-010, UC-015, UC-018 (23 lớp của P08); package của 24 use case còn lại giữ chỗ, xem F4 |
| Mã Q, ASM cuối đã cấp | Q-94 (P10 không cấp Q mới); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Subsystem ứng viên và quyết định

| Lớp phân tích (AC) | Tiêu chí thoả | Quyết định | Lý do |
|---|---|---|---|
| AC-B-PaymentGateway | Hệ thống ngoài; Có thể thay thế | Subsystem | Cổng thanh toán có thể đổi nhà cung cấp (KHA_NANG_THAY_DOI_GIAO_DIEN); che giao thức REST của đối tác (NFR-07) sau IF-01 để control không phụ thuộc chi tiết giao thức |
| AC-B-EInvoiceGateway | Hệ thống ngoài; Có thể thay thế | Subsystem | Hệ thống hoá đơn điện tử chưa có tài liệu API nên giao diện chưa ổn định (KHA_NANG_THAY_DOI_GIAO_DIEN, NFR-12); che định dạng dữ liệu (Q-39) sau IF-02 |
| AC-B-PushNotificationGateway | Hệ thống ngoài | Subsystem | Boundary giao diện hệ thống ngoài (ACT-10), giao thức chưa có tài liệu (NFR-10). KHA_NANG_THAY_DOI_GIAO_DIEN không nêu đổi nhà cung cấp nên không dùng tiêu chí Có thể thay thế |
| AC-B-SmsGateway | Hệ thống ngoài; Có thể thay thế | Subsystem | Cổng SMS có thể đổi nhà cung cấp (KHA_NANG_THAY_DOI_GIAO_DIEN, NFR-11) |
| AC-B-TurnstileDevice | Thiết bị | Subsystem | Boundary giao diện thiết bị (ACT-12, NFR-09, NFR-02). Giao thức ổn định (KHA_NANG_THAY_DOI_GIAO_DIEN) nên không dựa vào tiêu chí Có thể thay thế; vẫn là subsystem vì che định dạng thông điệp thiết bị (Q-67) và để P11b thiết kế hợp đồng giao tiếp. SS-05 nằm trong PKG-12 là điểm vào thiết bị của P09 F5 |
| AC-B-PurchaseOrRenewPackageUI | Không có | Không | Giao diện người dùng, ổn định (KHA_NANG_THAY_DOI_GIAO_DIEN); không thoả tiêu chí nào |
| AC-B-SellPackageUI | Không có | Không | Như trên |
| AC-B-BookClassSpotUI | Không có | Không | Như trên |
| AC-C-PurchaseOrRenewPackageHandler | Không có | Không | Control điều phối một use case; độ dài điều phối không phải tiêu chí subsystem |
| AC-C-BookClassSpotHandler | Không có | Không | Như trên |
| AC-C-CancelUnderBookedClassHandler | Không có | Không | Như trên |
| AC-C-EnterBranchHandler | Không có | Không | Như trên |
| AC-E-MembershipPackage, AC-E-Member, AC-E-PackageOrder, AC-E-PaymentTransaction, AC-E-PackagePrice, AC-E-Promotion, AC-E-GroupClass, AC-E-ClassBooking, AC-E-Waitlist, AC-E-EntryScan, AC-E-DayPass | Không có | Không | Lớp miền mang hành vi nghiệp vụ, không thay thế được, không cần giới hạn truy cập riêng; phần lưu trữ ghi ở bảng cơ chế của F3 |
| - (PKG-22; ACT-13, ACT-14) | Dịch vụ phức tạp dùng chung; Sản phẩm có sẵn | Subsystem | Phục vụ UC-005 và UC-015 đã có P07 (mốc hạn thanh toán BR-04, mốc 2 giờ trước giờ học) và UC-008, UC-013, UC-016, UC-022; che kho mốc hẹn bền, vòng quét mốc, cơ chế mỗi mốc chỉ một bản chạy nhận (P09 F7); thường dùng thư viện hẹn giờ có sẵn |
| - (PKG-21) | Bảo mật; Sản phẩm có sẵn | Subsystem | PKG-10, PKG-11, PKG-12 phụ thuộc PKG-21 (P09 F6) cho các yêu cầu của UC-005, UC-010, UC-018 đã có P07; cần giới hạn truy cập (chỉ hội viên và huấn luyện viên phụ trách xem chỉ số cơ thể, P09 F7); thường dùng thư viện xác thực có sẵn |
| - (PKG-20) | Không có | Không | Phần hiện thực interface kho dữ liệu không thành subsystem (A1); ghi ở bảng phần tử thiết kế mới do cơ chế kiến trúc (F3) |

Package của P09 chỉ phục vụ use case chưa có P07 và không có lớp hoạt động nào trong P08 (PKG-06, PKG-08, PKG-09, PKG-13, PKG-17, PKG-18, PKG-19, PKG-31) giữ chỗ ở F4, chưa tạo subsystem; xem Vấn đề còn mở.

## F2. Bảng subsystem

| SS | Tên | Interface (IF) | Trách nhiệm | Che giấu phần tử nào | AC nguồn | ACT liên quan | PKG chứa |
|---|---|---|---|---|---|---|---|
| SS-01 | OnlinePayment | IF-01 IPaymentGateway | // requestPayment: chuyển thông tin đơn mua cho cổng thanh toán<br>// returnPaymentResult: nhận kết quả giao dịch từ cổng và chuyển cho Application qua IF-08 | Giao thức REST của đối tác; chuyển đổi thông tin đơn mua và kết quả giao dịch sang thông điệp của cổng; quản lý kết nối và xử lý khi cổng không phản hồi (Q-77); cách nhận kết quả, cổng gửi về hoặc phần mềm tra cứu (Q-45) | AC-B-PaymentGateway | ACT-08 | PKG-23 |
| SS-02 | EInvoiceSubmission | IF-02 IEInvoiceGateway | // sendTransactionData: chuyển dữ liệu giao dịch thu tiền cho hệ thống hoá đơn điện tử | Định dạng và trường dữ liệu theo API hoá đơn (Q-39); quản lý kết nối; xử lý khi bên nhận từ chối (Q-54). Không có chức năng lập, điều chỉnh, huỷ hoá đơn (NFR-05) | AC-B-EInvoiceGateway | ACT-11 | PKG-25 |
| SS-03 | PushNotification | IF-03 IPushNotificationGateway | // sendPushNotification: nhận yêu cầu gửi thông báo đẩy của một hội viên và chuyển cho dịch vụ thông báo đẩy | Giao thức dịch vụ thông báo đẩy của nền tảng Android, iOS; chuyển nội dung thông báo sang thông điệp của dịch vụ; xử lý khi không gửi được (Q-65, Q-79) | AC-B-PushNotificationGateway | ACT-10 | PKG-24 |
| SS-04 | SmsMessaging | IF-04 ISmsGateway | // sendSms: nhận yêu cầu gửi SMS tới một hội viên và chuyển cho cổng SMS | Giao thức REST của cổng SMS; chuyển nội dung và số điện thoại sang thông điệp của cổng; xử lý khi không gửi được (Q-65, Q-79) | AC-B-SmsGateway | ACT-09 | PKG-24 |
| SS-05 | TurnstileAccess | IF-05 ITurnstileEndpoint | // receiveScannedCode: nhận mã QR đọc được, chi nhánh và thời điểm quẹt từ cửa quay, chuyển cho Application qua IF-09<br>// sendEntryResult: gửi cho cửa quay kết quả cho phép hoặc không cho phép<br>// openDoor: yêu cầu cửa quay mở cửa khi kết quả là cho phép<br>Interface gồm: // enableReceiving, // disableReceiving, // registerScanReceiver (bật, tắt, đăng ký bộ nhận lượt quét); lượt quét đi qua IF-09 | Giao thức và định dạng thông điệp của cửa quay (Q-67); chuyển kết quả thành phản hồi mở hoặc giữ đóng cửa (Q-70, Q-72); đo thời gian phản hồi trong 1 giây (NFR-02); xác thực thiết bị gọi vào qua IF-07. Thao tác scanQrCode của người quét là thao tác trên thiết bị, ngoài phần mềm | AC-B-TurnstileDevice | ACT-12 (ACT-02, ACT-03 tác động qua thiết bị) | PKG-12 |
| SS-06 | DurableScheduler | IF-06 IScheduler | // scheduleMark: đặt mốc hẹn bền (hạn thanh toán BR-04, 2 giờ trước giờ học; mốc của UC-008, UC-013, UC-016, UC-022 khi có P07)<br>// cancelMark: huỷ mốc hẹn gắn với một đối tượng (cancelAbsenceMark, cancelWaitlistTransferMark của AC-C-CancelUnderBookedClassHandler)<br>Interface gồm thêm: // registerMarkHandler, // start, // stop (đăng ký bộ nhận, bật, tắt cho tiến trình nền); mốc đến hạn đi qua IF-10 | Kho mốc hẹn bền trong CSDL (qua PKG-20); vòng quét mốc đến hạn; cơ chế mỗi mốc chỉ một bản chạy nhận; xử lý lặp lại được (P09 F7) | Cơ chế: P09 F7 (dòng ACT-13, ACT-14), F6 V4 a | ACT-13, ACT-14 | PKG-22 |
| SS-07 | Authentication | IF-07 IAuthenticator | // authenticateCaller: xác thực người dùng (ACT-01 đến ACT-07) hoặc thiết bị (ACT-12) gọi vào<br>// identifyCallerRole: cho biết định danh và vai trò của người gọi để Application kiểm tra quyền (chỉ hội viên và huấn luyện viên phụ trách xem chỉ số cơ thể) | Kiểm tra thông tin xác thực; quản lý phiên hoặc thẻ truy cập; thông tin xác thực của thiết bị cửa quay; tra cứu định danh hội viên qua PKG-26. Cách xác thực của nhân viên và quy định bảo vệ dữ liệu chờ Q-47, Q-89 | Cơ chế: P09 F3 (một điểm vào cho xác thực), F4 PKG-21, F7 dòng dữ liệu cần bảo vệ | ACT-01 đến ACT-07, ACT-12 | PKG-21 |

Bảng Interface gọi ngược (dãy IF-nn dùng chung với bảng trên):

| IF | Tên | Định nghĩa tại PKG | Subsystem gọi | Lớp hiện thực (DC, PKG) | Trách nhiệm | Nguồn (P09 A5, UC) |
|---|---|---|---|---|---|---|
| IF-08 | IPaymentResultReceiver | PKG-23 | SS-01 | DC-PurchaseOrRenewPackageHandler (PKG-14) | // returnPaymentResult: nhận kết quả giao dịch từ cổng thanh toán (thành công, không thành công) để xử lý tiếp bước 10 đến 13, 10a | P09 A5 (layer dưới định nghĩa, layer trên hiện thực, realization đi xuống); P09 F7 dòng ACT-08; AC-B-PaymentGateway // returnPaymentResult; UC-005 |
| IF-09 | IEntryScanReceiver | PKG-16 | SS-05 | DC-EnterBranchHandler (PKG-16) | // receiveScannedCode: nhận mã QR, chi nhánh và thời điểm quẹt từ cửa quay, trả kết quả cho phép hoặc không cho phép (// sendEntryResult) | P09 F7 dòng ACT-12; AC-B-TurnstileDevice // receiveScannedCode, // sendEntryResult; UC-018 |
| IF-10 | IScheduleMarkHandler | PKG-22 | SS-06 | DC-PurchaseOrRenewPackageHandler (PKG-14); DC-CancelUnderBookedClassHandler (PKG-15); lớp của PKG-17 khi có P07 | // handleMarkDue: nhận mốc hẹn đến hạn (hạn thanh toán BR-04, 2 giờ trước giờ học) và chuyển cho control xử lý | P09 F6 V4 a; P09 F7 dòng ACT-13, ACT-14; UC-005, UC-015 |
| IF-11 | IAccountRepository | PKG-26 | - (lớp Application gọi) | DC-AccountRepositoryImpl (PKG-20) | // lưu và truy xuất DC-Member (operation do P12 thiết kế) | P09 F5 dòng Entity (phần lưu trữ); F6 V4 b |
| IF-12 | IMembershipRepository | PKG-27 | - (lớp Application gọi) | DC-MembershipRepositoryImpl (PKG-20) | // lưu và truy xuất DC-MembershipPackage, DC-PackageOrder, DC-PaymentTransaction (operation do P12 thiết kế) | P09 F5 dòng Entity (phần lưu trữ); F6 V4 b |
| IF-13 | IPricingRepository | PKG-28 | - (lớp Application gọi) | DC-PricingRepositoryImpl (PKG-20) | // lưu và truy xuất DC-PackagePrice, DC-Promotion (operation do P12 thiết kế) | P09 F5 dòng Entity (phần lưu trữ); F6 V4 b |
| IF-14 | IGroupClassRepository | PKG-29 | - (lớp Application gọi) | DC-GroupClassRepositoryImpl (PKG-20) | // lưu và truy xuất DC-GroupClass, DC-ClassBooking, DC-Waitlist; việc ghi chỗ đã đặt là một giao dịch CSDL khoá dòng của lớp (P09 F7, BR-11); operation do P12 thiết kế | P09 F5 dòng Entity (phần lưu trữ); F6 V4 b; F7 chiến lược giao dịch |
| IF-15 | IBranchAccessRepository | PKG-30 | - (lớp Application gọi) | DC-BranchAccessRepositoryImpl (PKG-20) | // lưu và truy xuất DC-EntryScan, DC-DayPass (operation do P12 thiết kế) | P09 F5 dòng Entity (phần lưu trữ); F6 V4 b |

PKG-31 chưa có entity nên chưa có interface kho dữ liệu (giữ chỗ).

## F3. Ánh xạ lớp phân tích sang phần tử thiết kế

| AC | Kết quả | Phần tử thiết kế | PKG | Lý do |
|---|---|---|---|---|
| AC-B-PurchaseOrRenewPackageUI | Tách thành nhiều lớp | DC-PurchaseOrRenewPackageView<br>DC-PurchaseOrRenewPackageStore<br>DC-PurchaseOrRenewPackageController | PKG-05<br>PKG-05<br>PKG-10 | Bảng ánh xạ P09 F5 dòng Boundary giao diện người dùng: View và Store (Flux) ở package phía khách theo tác nhân ACT-02, phần tiếp nhận yêu cầu là REST controller ở PKG-10. Tên Controller là vai trò MVC của REST, khác lớp control hậu tố Handler |
| AC-B-SellPackageUI | Tách thành nhiều lớp | DC-SellPackageView<br>DC-SellPackageStore<br>DC-SellPackageController | PKG-07<br>PKG-07<br>PKG-11 | Như trên: tác nhân ACT-05 --> PKG-07, REST controller cho client web ở PKG-11 |
| AC-B-PaymentGateway | Subsystem | SS-01 OnlinePayment | PKG-23 | Chọn ở F1 |
| AC-B-EInvoiceGateway | Subsystem | SS-02 EInvoiceSubmission | PKG-25 | Chọn ở F1 |
| AC-C-PurchaseOrRenewPackageHandler | Lớp thiết kế DC | DC-PurchaseOrRenewPackageHandler | PKG-14 | Lớp đơn giản, một trừu tượng |
| AC-E-MembershipPackage | Lớp thiết kế DC | DC-MembershipPackage | PKG-27 | Lớp đơn giản, một trừu tượng |
| AC-E-Member | Tách thành nhiều lớp | DC-Member<br>DC-MemberPackages<br>DC-MemberBookingQuota | PKG-26<br>PKG-27<br>PKG-29 | Tạm, chờ P07 của UC-003. DC-Member giữ matchesQrCode, checkBookingNotSuspended, determineNotificationChannel (dữ liệu của chính hội viên). activatePackage và checkPackageEligibility hỏi dữ liệu ở PKG-27 nên chuyển sang DC-MemberPackages; checkDailyBookingLimit đếm chỗ đã đặt ở PKG-29 nên chuyển sang DC-MemberBookingQuota, vì PKG-27, PKG-29 phụ thuộc PKG-26 và Domain không có cạnh ngược (P09 F6 V7, F8). recordEntryScan trùng AC-E-EntryScan // createEntryScan nên hợp vào DC-EntryScan |
| AC-E-PackageOrder | Lớp thiết kế DC | DC-PackageOrder | PKG-27 | Lớp đơn giản, một trừu tượng |
| AC-E-PaymentTransaction | Lớp thiết kế DC | DC-PaymentTransaction | PKG-27 | Lớp đơn giản, một trừu tượng |
| AC-E-PackagePrice | Lớp thiết kế DC | DC-PackagePrice | PKG-28 | Lớp đơn giản, một trừu tượng. Tạm, chờ P07 của UC-026 |
| AC-E-Promotion | Lớp thiết kế DC | DC-Promotion | PKG-28 | Lớp đơn giản, một trừu tượng. Tạm, chờ P07 của UC-027 |
| AC-B-BookClassSpotUI | Tách thành nhiều lớp | DC-BookClassSpotView<br>DC-BookClassSpotStore<br>DC-BookClassSpotController | PKG-05<br>PKG-05<br>PKG-10 | Như AC-B-PurchaseOrRenewPackageUI: tác nhân ACT-02 --> PKG-05, REST controller ở PKG-10 |
| AC-C-BookClassSpotHandler | Lớp thiết kế DC | DC-BookClassSpotHandler | PKG-15 | Lớp đơn giản, một trừu tượng |
| AC-E-GroupClass | Lớp thiết kế DC | DC-GroupClass | PKG-29 | Lớp đơn giản, một trừu tượng. Tạm, chờ P07 của UC-009 |
| AC-E-ClassBooking | Lớp thiết kế DC | DC-ClassBooking | PKG-29 | Lớp đơn giản, một trừu tượng |
| AC-E-Waitlist | Lớp thiết kế DC | DC-Waitlist | PKG-29 | Lớp đơn giản, một trừu tượng |
| AC-B-PushNotificationGateway | Subsystem | SS-03 PushNotification | PKG-24 | Chọn ở F1 |
| AC-B-SmsGateway | Subsystem | SS-04 SmsMessaging | PKG-24 | Chọn ở F1 |
| AC-C-CancelUnderBookedClassHandler | Lớp thiết kế DC | DC-CancelUnderBookedClassHandler | PKG-15 | Lớp đơn giản, một trừu tượng |
| AC-B-TurnstileDevice | Subsystem | SS-05 TurnstileAccess | PKG-12 | Chọn ở F1. P09 F5 xếp vào PKG-12, SS-05 nằm trong PKG-12 |
| AC-C-EnterBranchHandler | Lớp thiết kế DC | DC-EnterBranchHandler | PKG-16 | Lớp đơn giản, một trừu tượng |
| AC-E-EntryScan | Lớp thiết kế DC | DC-EntryScan | PKG-30 | Lớp đơn giản, một trừu tượng; nhận thêm trách nhiệm recordEntryScan trùng createEntryScan của AC-E-Member |
| AC-E-DayPass | Lớp thiết kế DC | DC-DayPass | PKG-30 | Lớp đơn giản, một trừu tượng. Tạm, chờ P07 của UC-017 |

Thống kê: 23 lớp phân tích; 14 ánh xạ 1-1 sang lớp thiết kế, 4 tách thành nhiều lớp (tỷ lệ tách 17%), 5 thành subsystem, không lớp nào thành package.

Phần tử thiết kế mới do cơ chế kiến trúc (không từ lớp phân tích):

| DC hoặc SS | Tên | PKG | Cơ chế | Nguồn (P09 mục, NFR) |
|---|---|---|---|---|
| SS-06 | DurableScheduler | PKG-22 | Hẹn giờ | P09 F4 PKG-22; F6 V4 a; F7 dòng ACT-13, ACT-14 |
| SS-07 | Authentication | PKG-21 | Bảo mật | P09 F3 (một điểm vào cho xác thực), F4 PKG-21, F7 dòng dữ liệu cần bảo vệ |
| IF-08 | IPaymentResultReceiver | PKG-23 | Gọi ngược (đảo phụ thuộc) | Bảng Interface gọi ngược; P09 A5; AC-B-PaymentGateway // returnPaymentResult |
| IF-09 | IEntryScanReceiver | PKG-16 | Gọi ngược (đảo phụ thuộc) | Bảng Interface gọi ngược; P09 F7 dòng ACT-12 |
| IF-10 | IScheduleMarkHandler | PKG-22 | Gọi ngược (đảo phụ thuộc) | P09 F6 V4 a |
| IF-11 | IAccountRepository | PKG-26 | Persistence | P09 F5 dòng Entity (phần lưu trữ); F6 V4 b |
| IF-12 | IMembershipRepository | PKG-27 | Persistence | P09 F5, F6 V4 b |
| IF-13 | IPricingRepository | PKG-28 | Persistence | P09 F5, F6 V4 b |
| IF-14 | IGroupClassRepository | PKG-29 | Persistence | P09 F5, F6 V4 b; F7 chiến lược giao dịch; NFR-01 |
| IF-15 | IBranchAccessRepository | PKG-30 | Persistence | P09 F5, F6 V4 b |
| DC-AccountRepositoryImpl | AccountRepositoryImpl | PKG-20 | Persistence | Hiện thực IF-11 (P09 F5, F6 V4 b) |
| DC-MembershipRepositoryImpl | MembershipRepositoryImpl | PKG-20 | Persistence | Hiện thực IF-12 |
| DC-PricingRepositoryImpl | PricingRepositoryImpl | PKG-20 | Persistence | Hiện thực IF-13 |
| DC-GroupClassRepositoryImpl | GroupClassRepositoryImpl | PKG-20 | Persistence | Hiện thực IF-14 |
| DC-BranchAccessRepositoryImpl | BranchAccessRepositoryImpl | PKG-20 | Persistence | Hiện thực IF-15 |
| DC-DataStoreAccess | DataStoreAccess | PKG-20 | Persistence | P09 F7 (chỉ PKG-20 truy cập CSDL); PKG-22 lưu mốc hẹn qua lớp này |
| DC-Money | Money | PKG-32 | Kiểu giá trị dùng chung | P10 A3 (kiểu giá trị trong chữ ký interface); thuộc tính kiểu Số tiền của P08 (amountDue, amount, price); NFR-07, NFR-12 |
| DC-PhoneNumber | PhoneNumber | PKG-32 | Kiểu giá trị dùng chung | P10 A3; nguồn Mục 1 và Mục 10 (đăng ký bằng số điện thoại, SMS); NFR-11 |
| DC-TransactionReference | TransactionReference | PKG-32 | Kiểu giá trị dùng chung | P10 A3; đối chiếu kết quả giao dịch với đơn mua và dữ liệu hoá đơn (AC-B-PaymentGateway // returnPaymentResult, AC-E-PaymentTransaction // prepareInvoiceData); NFR-07, NFR-12 |

Giá trị cụ thể của chữ ký interface do P11b chốt; PKG-32 bổ sung kiểu khi chữ ký cần.

## F4. Bảng package

Layer vẫn là PKG-01 Presentation, PKG-02 Application, PKG-03 Services, PKG-04 Domain như P09. Các package PKG-05 đến PKG-31 giữ mã của P09; PKG-32 cấp mới (mã lớn nhất của P09 là PKG-31). Không có use case tuỳ chọn (extend) trong P03 (Mục 2 không có điểm mở rộng) nên không có lớp tuỳ chọn cần tách khỏi lớp bắt buộc.

| PKG | Tên | Layer (PKG) | Trách nhiệm | Phần tử chứa (DC, SS, IF) | Tiêu chí nhóm | Phụ thuộc vào (PKG) |
|---|---|---|---|---|---|---|
| PKG-05 | MemberMobileUI | PKG-01 | Giao diện di động cho Người quan tâm và Hội viên | DC-PurchaseOrRenewPackageView<br>DC-PurchaseOrRenewPackageStore<br>DC-BookClassSpotView<br>DC-BookClassSpotStore | Cùng tác nhân ACT-02 (UC-005, UC-010); View và Store của một màn hình thay đổi cùng nhau; giao diện di động ổn định (KHA_NANG_THAY_DOI_GIAO_DIEN) nên View, Store cùng package | - (gọi PKG-10 qua mạng) |
| PKG-06 | TrainerMobileUI | PKG-01 | Giao diện di động cho Huấn luyện viên (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: chỉ phục vụ UC-021, UC-024, UC-025 chưa có P07 | - (gọi PKG-10 qua mạng) |
| PKG-07 | ReceptionWebUI | PKG-01 | Giao diện web cho Lễ tân | DC-SellPackageView<br>DC-SellPackageStore | Cùng tác nhân ACT-05 (UC-005 bán tại quầy); View và Store của một màn hình thay đổi cùng nhau; giao diện web ổn định | - (gọi PKG-11 qua mạng) |
| PKG-08 | BranchManagerWebUI | PKG-01 | Giao diện web cho Quản lý chi nhánh (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: chỉ phục vụ UC-009, UC-014 chưa có P07 | - (gọi PKG-11 qua mạng) |
| PKG-09 | ChainDirectorWebUI | PKG-01 | Giao diện web cho Giám đốc chuỗi (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: chỉ phục vụ UC-026, UC-027, UC-028 chưa có P07 | - (gọi PKG-11 qua mạng) |
| PKG-10 | MobileApi | PKG-01 | Tiếp nhận yêu cầu REST từ ứng dụng di động | DC-PurchaseOrRenewPackageController<br>DC-BookClassSpotController | Cùng loại client (di động); controller chỉ chuyển yêu cầu sang Application; phần tiếp nhận yêu cầu nhóm theo loại client như P09 | PKG-14, PKG-15, PKG-21 |
| PKG-11 | WebApi | PKG-01 | Tiếp nhận yêu cầu REST từ ứng dụng web của nhân viên | DC-SellPackageController | Cùng loại client (web). Một phần tử: có lý do thay đổi riêng (đổi theo ứng dụng web, khác ứng dụng di động); controller của UC-007, UC-009, UC-014, UC-017, UC-026 đến UC-028 bổ sung khi có P07 | PKG-14, PKG-21 |
| PKG-12 | ExternalApi | PKG-01 | Tiếp nhận lời gọi từ thiết bị gọi vào phần mềm | SS-05 TurnstileAccess<br>IF-05 ITurnstileEndpoint | Package subsystem: chứa SS-05 và IF-05, cùng một thiết bị ACT-12; giao diện thiết bị tách khỏi lớp nghiệp vụ | PKG-16, PKG-21 |
| PKG-13 | AccountService | PKG-02 | Điều phối nhóm Tiếp cận và tài khoản (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: UC-001, UC-002, UC-004 chưa có P07, UC-003 chỉ có lớp Tạm AC-E-Member | (theo P09: PKG-21, PKG-26, PKG-28, PKG-29) |
| PKG-14 | MembershipService | PKG-02 | Điều phối nhóm Gói tập | DC-PurchaseOrRenewPackageHandler | Nhóm chức năng Gói tập. Một phần tử: có lý do thay đổi riêng (nhóm chức năng độc lập), UC-006 đến UC-008 bổ sung khi có P07 | PKG-22, PKG-23, PKG-25, PKG-26, PKG-27, PKG-28 |
| PKG-15 | GroupClassService | PKG-02 | Điều phối nhóm Lớp nhóm | DC-BookClassSpotHandler<br>DC-CancelUnderBookedClassHandler | Nhóm chức năng Lớp nhóm; hai control cùng tương tác DC-GroupClass và DC-Member (R-15, R-16, R-21, R-22) | PKG-22, PKG-24, PKG-26, PKG-29 |
| PKG-16 | BranchAccessService | PKG-02 | Điều phối nhóm Ra vào chi nhánh | DC-EnterBranchHandler<br>IF-09 IEntryScanReceiver | Nhóm chức năng Ra vào chi nhánh; IF-09 cùng package với lớp hiện thực DC-EnterBranchHandler | PKG-26, PKG-27, PKG-30 |
| PKG-17 | PersonalTrainingService | PKG-02 | Điều phối nhóm Huấn luyện cá nhân (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: UC-019 đến UC-025 chưa có P07 | (theo P09: PKG-22, PKG-25, PKG-26, PKG-31) |
| PKG-18 | PricingService | PKG-02 | Điều phối đặt giá và khuyến mãi (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: UC-026, UC-027 chưa có P07 | (theo P09: PKG-28) |
| PKG-19 | ReportingService | PKG-02 | Điều phối báo cáo chuỗi (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: UC-028 chưa có P07 | (theo P09: PKG-27, PKG-29, PKG-31) |
| PKG-20 | Persistence | PKG-03 | Hiện thực lưu trữ cho các interface kho dữ liệu của Domain và truy cập CSDL dùng chung | DC-AccountRepositoryImpl<br>DC-MembershipRepositoryImpl<br>DC-PricingRepositoryImpl<br>DC-GroupClassRepositoryImpl<br>DC-BranchAccessRepositoryImpl<br>DC-DataStoreAccess | Cùng lý do thay đổi (đổi cách truy cập CSDL) và cùng dùng DC-DataStoreAccess; hiện thực của IF-11 đến IF-15 đi xuống Domain | PKG-26, PKG-27, PKG-28, PKG-29, PKG-30 |
| PKG-21 | Security | PKG-03 | Xác thực người dùng và thiết bị gọi vào | SS-07 Authentication<br>IF-07 IAuthenticator | Package subsystem: chứa SS-07 và IF-07; cần giới hạn truy cập vì lý do bảo mật | PKG-26 |
| PKG-22 | Scheduling | PKG-03 | Điều khiển các mốc hẹn giờ bền vững | SS-06 DurableScheduler<br>IF-06 IScheduler<br>IF-10 IScheduleMarkHandler | Package subsystem: chứa SS-06, IF-06 và interface gọi ngược IF-10 do chính package định nghĩa | PKG-20 |
| PKG-23 | PaymentIntegration | PKG-03 | Giao tiếp với cổng thanh toán trực tuyến | SS-01 OnlinePayment<br>IF-01 IPaymentGateway<br>IF-08 IPaymentResultReceiver | Package subsystem: chứa SS-01, IF-01, IF-08; giao diện hệ thống có thể đổi nhà cung cấp nên tách khỏi lớp nghiệp vụ | PKG-32 |
| PKG-24 | NotificationChannels | PKG-03 | Gửi thông báo đẩy và SMS | SS-03 PushNotification<br>IF-03 IPushNotificationGateway<br>SS-04 SmsMessaging<br>IF-04 ISmsGateway | Package subsystem: hai kênh thông báo cùng được Application chọn theo từng hội viên (CRP); mỗi kênh một subsystem, một interface | PKG-32 |
| PKG-25 | EInvoiceIntegration | PKG-03 | Gửi dữ liệu giao dịch thu tiền sang hệ thống hoá đơn điện tử | SS-02 EInvoiceSubmission<br>IF-02 IEInvoiceGateway | Package subsystem: chứa SS-02 và IF-02; giao diện chưa ổn định nên tách khỏi lớp nghiệp vụ | PKG-32 |
| PKG-26 | Account | PKG-04 | Biểu diễn hội viên và dữ liệu định danh | DC-Member<br>IF-11 IAccountRepository | Entity gốc của hội viên mà các package Domain khác tham chiếu; interface kho dữ liệu cùng package với entity | - |
| PKG-27 | Membership | PKG-04 | Biểu diễn gói tập, đơn mua, giao dịch thu tiền và gói tập của một hội viên | DC-MembershipPackage<br>DC-PackageOrder<br>DC-PaymentTransaction<br>DC-MemberPackages<br>IF-12 IMembershipRepository | Nhóm Gói tập; các lớp có quan hệ với nhau (R-11, R-12, R-13) và DC-MemberPackages tạo, kiểm tra DC-MembershipPackage | PKG-26, PKG-32 |
| PKG-28 | Pricing | PKG-04 | Biểu diễn giá gói tập và chương trình khuyến mãi | DC-PackagePrice<br>DC-Promotion<br>IF-13 IPricingRepository | Nhóm Giá và báo cáo; DC-PackagePrice.calculateAmountDue cần DC-Promotion nên cùng package (P08 F6) | PKG-32 |
| PKG-29 | GroupClass | PKG-04 | Biểu diễn lớp nhóm, chỗ đã đặt, danh sách chờ và hạn mức đặt chỗ của hội viên | DC-GroupClass<br>DC-ClassBooking<br>DC-Waitlist<br>DC-MemberBookingQuota<br>IF-14 IGroupClassRepository | Nhóm Lớp nhóm; các lớp có quan hệ với nhau (R-17, R-18) và DC-MemberBookingQuota đếm DC-ClassBooking | PKG-26 |
| PKG-30 | BranchAccess | PKG-04 | Biểu diễn lượt quẹt vào cửa và vé tập một ngày | DC-EntryScan<br>DC-DayPass<br>IF-15 IBranchAccessRepository | Nhóm Ra vào chi nhánh; cùng được DC-EnterBranchHandler tương tác (R-27) | PKG-26 |
| PKG-31 | PersonalTraining | PKG-04 | Biểu diễn gói buổi tập cá nhân, buổi tập và chỉ số cơ thể (giữ chỗ) | - (giữ chỗ, chưa có phần tử) | Giữ chỗ: UC-019 đến UC-025 chưa có P07 | (theo P09: PKG-26) |
| PKG-32 | ValueTypes | PKG-04 | Kiểu giá trị dùng chung trong chữ ký interface: tiền, số điện thoại, mã tham chiếu giao dịch | DC-Money<br>DC-PhoneNumber<br>DC-TransactionReference | Mới ở P10. Cùng lý do thay đổi (định dạng giá trị); đặt ở layer thấp nhất để chữ ký interface ở Services không kéo Services phụ thuộc layer trên | - |

## F5. Visibility

| PKG | Phần tử | Visibility (public / package-private) | Được dùng bởi (PKG) |
|---|---|---|---|
| PKG-05 | DC-PurchaseOrRenewPackageView | package-private | - |
| PKG-05 | DC-PurchaseOrRenewPackageStore | package-private | - |
| PKG-05 | DC-BookClassSpotView | package-private | - |
| PKG-05 | DC-BookClassSpotStore | package-private | - |
| PKG-07 | DC-SellPackageView | package-private | - |
| PKG-07 | DC-SellPackageStore | package-private | - |
| PKG-10 | DC-PurchaseOrRenewPackageController | package-private | - (nhận lời gọi mạng từ PKG-05) |
| PKG-10 | DC-BookClassSpotController | package-private | - (nhận lời gọi mạng từ PKG-05) |
| PKG-11 | DC-SellPackageController | package-private | - (nhận lời gọi mạng từ PKG-07) |
| PKG-12 | SS-05 TurnstileAccess | package-private | - (chỉ truy cập qua IF-05) |
| PKG-12 | IF-05 ITurnstileEndpoint | public | - (bước khởi động tiến trình API, ngoài các package của mô hình) |
| PKG-14 | DC-PurchaseOrRenewPackageHandler | public | PKG-10, PKG-11 |
| PKG-15 | DC-BookClassSpotHandler | public | PKG-10 |
| PKG-15 | DC-CancelUnderBookedClassHandler | package-private | - (chỉ được gọi qua IF-10) |
| PKG-16 | DC-EnterBranchHandler | package-private | - (chỉ được gọi qua IF-09) |
| PKG-16 | IF-09 IEntryScanReceiver | public | PKG-12 |
| PKG-20 | DC-AccountRepositoryImpl | package-private | - (chỉ được gọi qua IF-11) |
| PKG-20 | DC-MembershipRepositoryImpl | package-private | - (chỉ được gọi qua IF-12) |
| PKG-20 | DC-PricingRepositoryImpl | package-private | - (chỉ được gọi qua IF-13) |
| PKG-20 | DC-GroupClassRepositoryImpl | package-private | - (chỉ được gọi qua IF-14) |
| PKG-20 | DC-BranchAccessRepositoryImpl | package-private | - (chỉ được gọi qua IF-15) |
| PKG-20 | DC-DataStoreAccess | public | PKG-22 |
| PKG-21 | SS-07 Authentication | package-private | - (chỉ truy cập qua IF-07) |
| PKG-21 | IF-07 IAuthenticator | public | PKG-10, PKG-11, PKG-12 |
| PKG-22 | SS-06 DurableScheduler | package-private | - (chỉ truy cập qua IF-06) |
| PKG-22 | IF-06 IScheduler | public | PKG-14, PKG-15 |
| PKG-22 | IF-10 IScheduleMarkHandler | public | PKG-14, PKG-15 |
| PKG-23 | SS-01 OnlinePayment | package-private | - (chỉ truy cập qua IF-01) |
| PKG-23 | IF-01 IPaymentGateway | public | PKG-14 |
| PKG-23 | IF-08 IPaymentResultReceiver | public | PKG-14 |
| PKG-24 | SS-03 PushNotification | package-private | - (chỉ truy cập qua IF-03) |
| PKG-24 | IF-03 IPushNotificationGateway | public | PKG-15 |
| PKG-24 | SS-04 SmsMessaging | package-private | - (chỉ truy cập qua IF-04) |
| PKG-24 | IF-04 ISmsGateway | public | PKG-15 |
| PKG-25 | SS-02 EInvoiceSubmission | package-private | - (chỉ truy cập qua IF-02) |
| PKG-25 | IF-02 IEInvoiceGateway | public | PKG-14 |
| PKG-26 | DC-Member | public | PKG-14, PKG-15, PKG-16, PKG-20, PKG-21, PKG-27, PKG-29, PKG-30 |
| PKG-26 | IF-11 IAccountRepository | public | PKG-14, PKG-15, PKG-16, PKG-20, PKG-21 |
| PKG-27 | DC-MembershipPackage | public | PKG-14, PKG-20 |
| PKG-27 | DC-PackageOrder | public | PKG-14, PKG-20 |
| PKG-27 | DC-PaymentTransaction | public | PKG-14, PKG-20 |
| PKG-27 | DC-MemberPackages | public | PKG-14, PKG-16 |
| PKG-27 | IF-12 IMembershipRepository | public | PKG-14, PKG-16, PKG-20 |
| PKG-28 | DC-PackagePrice | public | PKG-14, PKG-20 |
| PKG-28 | DC-Promotion | public | PKG-14, PKG-20 |
| PKG-28 | IF-13 IPricingRepository | public | PKG-14, PKG-20 |
| PKG-29 | DC-GroupClass | public | PKG-15, PKG-20 |
| PKG-29 | DC-ClassBooking | public | PKG-20 |
| PKG-29 | DC-Waitlist | public | PKG-20 |
| PKG-29 | DC-MemberBookingQuota | public | PKG-15 |
| PKG-29 | IF-14 IGroupClassRepository | public | PKG-15, PKG-20 |
| PKG-30 | DC-EntryScan | public | PKG-16, PKG-20 |
| PKG-30 | DC-DayPass | public | PKG-16, PKG-20 |
| PKG-30 | IF-15 IBranchAccessRepository | public | PKG-16, PKG-20 |
| PKG-32 | DC-Money | public | PKG-23, PKG-25, PKG-27, PKG-28 |
| PKG-32 | DC-PhoneNumber | public | PKG-24 |
| PKG-32 | DC-TransactionReference | public | PKG-23, PKG-25 |

## F6. Kiểm tra coupling giữa package

Cột Nhảy layer ghi "Không áp dụng" vì P09 chọn layered nới lỏng (F6 V1). Bảng liệt kê 35 phụ thuộc giữa package; phụ thuộc tới subsystem đi qua interface (IF-01 đến IF-07), phụ thuộc gọi ngược đi qua IF-08 đến IF-10.

| Phụ thuộc (PKG --> PKG) | Suy ra từ (quan hệ lớp, message) | Cross-coupled | Lower --> Upper | Nhảy layer | Vòng | Kết luận và cách sửa |
|---|---|---|---|---|---|---|
| PKG-10 --> PKG-14 | R-01: DC-PurchaseOrRenewPackageController gọi DC-PurchaseOrRenewPackageHandler | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-10 --> PKG-15 | R-14: DC-BookClassSpotController gọi DC-BookClassSpotHandler | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-10 --> PKG-21 | Controller gọi IF-07 để xác thực (P09 F6) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-11 --> PKG-14 | R-02: DC-SellPackageController gọi DC-PurchaseOrRenewPackageHandler | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-11 --> PKG-21 | Controller gọi IF-07 để xác thực (P09 F6) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-12 --> PKG-16 | R-25: SS-05 đẩy lượt quét vào DC-EnterBranchHandler qua IF-09 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-12 --> PKG-21 | SS-05 gọi IF-07 để xác thực thiết bị (P09 F6) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-14 --> PKG-22 | AC-C-PurchaseOrRenewPackageHandler // startWaitingForPayment, // stopWaitingForPayment, // handlePaymentTimeout (BR-04): gọi IF-06, hiện thực IF-10 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-14 --> PKG-23 | R-07: gọi IF-01, hiện thực IF-08 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-14 --> PKG-25 | R-10: gọi IF-02 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-14 --> PKG-26 | R-08 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-14 --> PKG-27 | R-03, R-06, R-09 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-14 --> PKG-28 | R-04, R-05 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-15 --> PKG-22 | AC-C-CancelUnderBookedClassHandler // cancelAbsenceMark, // cancelWaitlistTransferMark (Q-64): gọi IF-06, hiện thực IF-10 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-15 --> PKG-24 | R-23, R-24: gọi IF-03, IF-04 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-15 --> PKG-26 | R-15, R-22 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-15 --> PKG-29 | R-16, R-21 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 --> PKG-26 | R-26 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 --> PKG-27 | AC-E-Member // checkPackageEligibility chuyển sang DC-MemberPackages (R-12) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-16 --> PKG-30 | R-27, R-28 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-20 --> PKG-26 | DC-AccountRepositoryImpl hiện thực IF-11 (P09 F6 V4 b) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-20 --> PKG-27 | DC-MembershipRepositoryImpl hiện thực IF-12 (P09 F6 V4 b) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-20 --> PKG-28 | DC-PricingRepositoryImpl hiện thực IF-13 (P09 F6 V4 b) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-20 --> PKG-29 | DC-GroupClassRepositoryImpl hiện thực IF-14 (P09 F6 V4 b) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-20 --> PKG-30 | DC-BranchAccessRepositoryImpl hiện thực IF-15 (P09 F6 V4 b) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-21 --> PKG-26 | SS-07 tra cứu định danh hội viên (P09 F4) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-22 --> PKG-20 | SS-06 lưu mốc hẹn bền qua DC-DataStoreAccess (P09 F4, F7) | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-23 --> PKG-32 | Chữ ký IF-01, IF-08 dùng DC-Money, DC-TransactionReference | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-24 --> PKG-32 | Chữ ký IF-04 dùng DC-PhoneNumber | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-25 --> PKG-32 | Chữ ký IF-02 dùng DC-Money, DC-TransactionReference | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-27 --> PKG-26 | R-12, R-13 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-27 --> PKG-32 | Số tiền của DC-PackageOrder, DC-PaymentTransaction dùng DC-Money | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-28 --> PKG-32 | Giá của DC-PackagePrice dùng DC-Money | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-29 --> PKG-26 | R-19, R-20 | Không | Không | Không áp dụng | Không | Hợp lệ |
| PKG-30 --> PKG-26 | R-28 | Không | Không | Không áp dụng | Không | Hợp lệ |

Kết luận: không có cặp package nào phụ thuộc lẫn nhau, không có vòng, không có phụ thuộc hoặc realization đi lên. Phụ thuộc có hướng cần xử lý: quan hệ hai chiều của AC-E-Member với DC-MembershipPackage, DC-ClassBooking, DC-EntryScan ở P08 (R-12, R-19, R-28) được giải bằng cách chọn chiều PKG-27, PKG-29, PKG-30 --> PKG-26 và chuyển hành vi hỏi dữ liệu sang DC-MemberPackages, DC-MemberBookingQuota (F3), đúng P09 F6 V7.

## F7. Package diagram thiết kế

File diagrams/P10-package-design.drawio. Toạ độ ở bảng Node là tuyệt đối trên trang; file .drawio ghi toạ độ của phần tử con tương đối theo package chứa nó. Điểm uốn ở bảng Edge là toạ độ tuyệt đối. Sơ đồ vẽ các package có subsystem, interface hoặc lớp hiện thực interface gọi ngược (Class chỉ vẽ cho lớp hiện thực interface gọi ngược); các phần tử còn lại và package giữ chỗ xem F4. Phụ thuộc của PKG-20 tới Domain được vẽ bằng realization từ lớp hiện thực tới interface kho dữ liệu (IF-11 đến IF-15). Lời gọi qua mạng từ PKG-05, PKG-07 tới PKG-10, PKG-11 không là phụ thuộc package (P09 V6) nên không vẽ.

a) Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú (visibility) | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-01 | Layer | PKG-01 Presentation | «layer» | - | - | 40 | 40 | 3090 | 190 |
| PKG-02 | Layer | PKG-02 Application | «layer» | - | - | 40 | 330 | 3090 | 190 |
| PKG-03 | Layer | PKG-03 Services | «layer» | - | - | 40 | 720 | 3090 | 460 |
| PKG-04 | Layer | PKG-04 Domain | «layer» | - | - | 40 | 1380 | 3090 | 260 |
| PKG-05 | Package | PKG-05 MemberMobileUI | - | PKG-01 | - | 60 | 80 | 200 | 60 |
| PKG-07 | Package | PKG-07 ReceptionWebUI | - | PKG-01 | - | 300 | 80 | 200 | 60 |
| PKG-10 | Package | PKG-10 MobileApi | - | PKG-01 | - | 900 | 80 | 200 | 60 |
| PKG-11 | Package | PKG-11 WebApi | - | PKG-01 | - | 1160 | 80 | 200 | 60 |
| PKG-12 | Package | PKG-12 ExternalApi | - | PKG-01 | - | 1560 | 80 | 390 | 120 |
| SS-05 | Subsystem | SS-05 TurnstileAccess | «subsystem» | PKG-12 | Không public (chỉ interface public) | 1580 | 130 | 150 | 50 |
| IF-05 | Interface | ITurnstileEndpoint | «interface» | PKG-12 | public | 1770 | 130 | 160 | 50 |
| PKG-14 | Package | PKG-14 MembershipService | - | PKG-02 | - | 900 | 370 | 220 | 120 |
| DC-PurchaseOrRenewPackageHandler | Class | DC-PurchaseOrRenewPackageHandler | - | PKG-14 | public | 920 | 420 | 180 | 50 |
| PKG-15 | Package | PKG-15 GroupClassService | - | PKG-02 | - | 1160 | 370 | 220 | 120 |
| DC-CancelUnderBookedClassHandler | Class | DC-CancelUnderBookedClassHandler | - | PKG-15 | package-private | 1180 | 420 | 180 | 50 |
| PKG-16 | Package | PKG-16 BranchAccessService | - | PKG-02 | - | 1560 | 370 | 420 | 120 |
| DC-EnterBranchHandler | Class | DC-EnterBranchHandler | - | PKG-16 | package-private | 1580 | 420 | 180 | 50 |
| IF-09 | Interface | IEntryScanReceiver | «interface» | PKG-16 | public | 1800 | 420 | 160 | 50 |
| PKG-23 | Package | PKG-23 PaymentIntegration | - | PKG-03 | - | 60 | 760 | 590 | 120 |
| IF-08 | Interface | IPaymentResultReceiver | «interface» | PKG-23 | public | 80 | 810 | 160 | 50 |
| SS-01 | Subsystem | SS-01 OnlinePayment | «subsystem» | PKG-23 | Không public (chỉ interface public) | 280 | 810 | 150 | 50 |
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-23 | public | 470 | 810 | 160 | 50 |
| PKG-25 | Package | PKG-25 EInvoiceIntegration | - | PKG-03 | - | 910 | 760 | 390 | 120 |
| SS-02 | Subsystem | SS-02 EInvoiceSubmission | «subsystem» | PKG-25 | Không public (chỉ interface public) | 930 | 810 | 150 | 50 |
| IF-02 | Interface | IEInvoiceGateway | «interface» | PKG-25 | public | 1120 | 810 | 160 | 50 |
| PKG-24 | Package | PKG-24 NotificationChannels | - | PKG-03 | - | 1560 | 760 | 780 | 120 |
| SS-03 | Subsystem | SS-03 PushNotification | «subsystem» | PKG-24 | Không public (chỉ interface public) | 1580 | 810 | 150 | 50 |
| IF-03 | Interface | IPushNotificationGateway | «interface» | PKG-24 | public | 1770 | 810 | 160 | 50 |
| IF-04 | Interface | ISmsGateway | «interface» | PKG-24 | public | 1970 | 810 | 160 | 50 |
| SS-04 | Subsystem | SS-04 SmsMessaging | «subsystem» | PKG-24 | Không public (chỉ interface public) | 2170 | 810 | 150 | 50 |
| PKG-22 | Package | PKG-22 Scheduling | - | PKG-03 | - | 60 | 1030 | 590 | 120 |
| IF-10 | Interface | IScheduleMarkHandler | «interface» | PKG-22 | public | 80 | 1080 | 160 | 50 |
| SS-06 | Subsystem | SS-06 DurableScheduler | «subsystem» | PKG-22 | Không public (chỉ interface public) | 280 | 1080 | 150 | 50 |
| IF-06 | Interface | IScheduler | «interface» | PKG-22 | public | 470 | 1080 | 160 | 50 |
| PKG-20 | Package | PKG-20 Persistence | - | PKG-03 | - | 1560 | 1030 | 900 | 120 |
| DC-AccountRepositoryImpl | Class | DC-AccountRepositoryImpl | - | PKG-20 | package-private | 1580 | 1080 | 140 | 50 |
| DC-MembershipRepositoryImpl | Class | DC-MembershipRepositoryImpl | - | PKG-20 | package-private | 1760 | 1080 | 140 | 50 |
| DC-PricingRepositoryImpl | Class | DC-PricingRepositoryImpl | - | PKG-20 | package-private | 1940 | 1080 | 140 | 50 |
| DC-GroupClassRepositoryImpl | Class | DC-GroupClassRepositoryImpl | - | PKG-20 | package-private | 2120 | 1080 | 140 | 50 |
| DC-BranchAccessRepositoryImpl | Class | DC-BranchAccessRepositoryImpl | - | PKG-20 | package-private | 2300 | 1080 | 140 | 50 |
| PKG-21 | Package | PKG-21 Security | - | PKG-03 | - | 2700 | 1030 | 390 | 120 |
| SS-07 | Subsystem | SS-07 Authentication | «subsystem» | PKG-21 | Không public (chỉ interface public) | 2720 | 1080 | 150 | 50 |
| IF-07 | Interface | IAuthenticator | «interface» | PKG-21 | public | 2910 | 1080 | 160 | 50 |
| PKG-32 | Package | PKG-32 ValueTypes | - | PKG-04 | - | 60 | 1420 | 220 | 60 |
| PKG-26 | Package | PKG-26 Account | - | PKG-04 | - | 320 | 1420 | 220 | 120 |
| IF-11 | Interface | IAccountRepository | «interface» | PKG-26 | public | 350 | 1470 | 160 | 50 |
| PKG-27 | Package | PKG-27 Membership | - | PKG-04 | - | 900 | 1420 | 220 | 120 |
| IF-12 | Interface | IMembershipRepository | «interface» | PKG-27 | public | 930 | 1470 | 160 | 50 |
| PKG-28 | Package | PKG-28 Pricing | - | PKG-04 | - | 1160 | 1420 | 220 | 120 |
| IF-13 | Interface | IPricingRepository | «interface» | PKG-28 | public | 1190 | 1470 | 160 | 50 |
| PKG-29 | Package | PKG-29 GroupClass | - | PKG-04 | - | 1560 | 1420 | 220 | 120 |
| IF-14 | Interface | IGroupClassRepository | «interface» | PKG-29 | public | 1590 | 1470 | 160 | 50 |
| PKG-30 | Package | PKG-30 BranchAccess | - | PKG-04 | - | 1820 | 1420 | 220 | 120 |
| IF-15 | Interface | IBranchAccessRepository | «interface» | PKG-30 | public | 1850 | 1470 | 160 | 50 |

b) Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| PD-01 | PKG-10 | PKG-14 | Dependency | - | DC-PurchaseOrRenewPackageController gọi DC-PurchaseOrRenewPackageHandler | (990,240); (1020,240) |
| PD-02 | PKG-10 | PKG-15 | Dependency | - | DC-BookClassSpotController gọi DC-BookClassSpotHandler; không vẽ DC-BookClassSpotHandler vì không hiện thực interface gọi ngược | (1000,250); (1280,250) |
| PD-03 | PKG-10 | IF-07 | Dependency | - | Controller xác thực người gọi qua interface | (1010,260); (1420,260); (1420,900); (2980,900) |
| PD-04 | PKG-11 | PKG-14 | Dependency | - | DC-SellPackageController gọi DC-PurchaseOrRenewPackageHandler | (1260,270); (1030,270) |
| PD-05 | PKG-11 | IF-07 | Dependency | - | Controller xác thực người gọi qua interface | (1270,280); (2500,280); (2500,910); (2990,910) |
| PD-06 | SS-05 | IF-09 | Dependency | - | Subsystem đẩy lượt quét vào Application qua interface gọi ngược | (1650,290); (1880,290) |
| PD-07 | SS-05 | IF-07 | Dependency | - | Subsystem xác thực thiết bị gọi vào qua interface | (1660,300); (2510,300); (2510,920); (3000,920) |
| PD-08 | PKG-14 | IF-01 | Dependency | - | Package dùng subsystem thì phụ thuộc vào interface | (990,530); (550,530) |
| PD-09 | PKG-14 | IF-02 | Dependency | - | Package dùng subsystem thì phụ thuộc vào interface | (1020,540); (1200,540) |
| PD-10 | PKG-14 | IF-06 | Dependency | - | Đặt và huỷ mốc hẹn BR-04 | (1000,550); (690,550); (690,930); (550,930) |
| PD-11 | PKG-14 | PKG-26 | Dependency | - | R-08 | (980,560); (700,560); (700,1190); (420,1190) |
| PD-12 | PKG-14 | PKG-27 | Dependency | - | R-03, R-06, R-09 | (1010,570); (710,570); (710,1200); (1000,1200) |
| PD-13 | PKG-14 | PKG-28 | Dependency | - | R-04, R-05 | (1030,580); (1430,580); (1430,1210); (1270,1210) |
| PD-14 | PKG-15 | IF-03 | Dependency | - | Package dùng subsystem thì phụ thuộc vào interface | (1280,590); (1850,590) |
| PD-15 | PKG-15 | IF-04 | Dependency | - | Package dùng subsystem thì phụ thuộc vào interface | (1290,600); (2050,600) |
| PD-16 | PKG-15 | IF-06 | Dependency | - | Huỷ mốc hẹn của UC-016, UC-013 gắn với lớp | (1260,610); (720,610); (720,940); (560,940) |
| PD-17 | PKG-15 | PKG-26 | Dependency | - | R-15, R-22 | (1250,620); (730,620); (730,1220); (430,1220) |
| PD-18 | PKG-15 | PKG-29 | Dependency | - | R-16, R-21 | (1270,630); (1440,630); (1440,1230); (1670,1230) |
| PD-19 | PKG-16 | PKG-26 | Dependency | - | R-26 | (1760,640); (740,640); (740,1240); (440,1240) |
| PD-20 | PKG-16 | PKG-27 | Dependency | - | Kiểm tra gói qua DC-MemberPackages | (1770,650); (1450,650); (1450,1250); (1010,1250) |
| PD-21 | PKG-16 | PKG-30 | Dependency | - | R-27, R-28 | (1780,660); (1460,660); (1460,1260); (1930,1260) |
| PD-22 | DC-PurchaseOrRenewPackageHandler | IF-08 | Realization | - | Nhận kết quả thanh toán; realization đi xuống | (1040,670); (160,670) |
| PD-23 | DC-PurchaseOrRenewPackageHandler | IF-10 | Realization | - | Nhận mốc hết thời hạn thanh toán BR-04; realization đi xuống | (1050,680); (750,680); (750,950); (160,950) |
| PD-24 | DC-CancelUnderBookedClassHandler | IF-10 | Realization | - | Nhận mốc 2 giờ trước giờ học; realization đi xuống | (1300,690); (760,690); (760,960); (170,960) |
| PD-25 | DC-EnterBranchHandler | IF-09 | Realization | - | Nhận lượt quét từ cửa quay | - |
| PD-26 | DC-AccountRepositoryImpl | IF-11 | Realization | - | Hiện thực kho dữ liệu, realization đi xuống Domain | (1650,1310); (460,1310) |
| PD-27 | DC-MembershipRepositoryImpl | IF-12 | Realization | - | Hiện thực kho dữ liệu, realization đi xuống Domain | (1830,1320); (1020,1320) |
| PD-28 | DC-PricingRepositoryImpl | IF-13 | Realization | - | Hiện thực kho dữ liệu, realization đi xuống Domain | (2010,1330); (1280,1330) |
| PD-29 | DC-GroupClassRepositoryImpl | IF-14 | Realization | - | Hiện thực kho dữ liệu, realization đi xuống Domain | (2190,1340); (1680,1340) |
| PD-30 | DC-BranchAccessRepositoryImpl | IF-15 | Realization | - | Hiện thực kho dữ liệu, realization đi xuống Domain | (2370,1350); (1940,1350) |
| PD-31 | PKG-21 | PKG-26 | Dependency | - | Tra cứu định danh hội viên (P09 F4) | (2900,1300); (450,1300) |
| PD-32 | PKG-22 | PKG-20 | Dependency | - | Lưu mốc hẹn qua DC-DataStoreAccess (không vẽ lớp này vì không hiện thực interface gọi ngược) | - |
| PD-33 | PKG-23 | PKG-32 | Dependency | - | Chữ ký IF-01, IF-08 dùng DC-Money, DC-TransactionReference | (360,970); (770,970); (770,1270); (160,1270) |
| PD-34 | PKG-24 | PKG-32 | Dependency | - | Chữ ký IF-04 dùng DC-PhoneNumber | (1950,990); (790,990); (790,1290); (180,1290) |
| PD-35 | PKG-25 | PKG-32 | Dependency | - | Chữ ký IF-02 dùng DC-Money, DC-TransactionReference | (1110,980); (780,980); (780,1280); (170,1280) |
| PD-36 | PKG-27 | PKG-26 | Dependency | - | R-12, R-13 | (1010,1560); (420,1560) |
| PD-37 | PKG-27 | PKG-32 | Dependency | - | Số tiền của đơn mua và giao dịch dùng DC-Money | (1000,1570); (160,1570) |
| PD-38 | PKG-28 | PKG-32 | Dependency | - | Giá gói dùng DC-Money | (1270,1580); (170,1580) |
| PD-39 | PKG-29 | PKG-26 | Dependency | - | R-19, R-20 | (1670,1590); (430,1590) |
| PD-40 | PKG-30 | PKG-26 | Dependency | - | R-28 | (1930,1600); (440,1600) |
| PD-41 | SS-01 | IF-01 | Realization | - | Subsystem hiện thực interface | - |
| PD-42 | SS-01 | IF-08 | Dependency | - | Subsystem gọi ngược khi có kết quả | - |
| PD-43 | SS-02 | IF-02 | Realization | - | Subsystem hiện thực interface | - |
| PD-44 | SS-03 | IF-03 | Realization | - | Subsystem hiện thực interface | - |
| PD-45 | SS-04 | IF-04 | Realization | - | Subsystem hiện thực interface | - |
| PD-46 | SS-05 | IF-05 | Realization | - | Subsystem hiện thực interface | - |
| PD-47 | SS-06 | IF-06 | Realization | - | Subsystem hiện thực interface | - |
| PD-48 | SS-06 | IF-10 | Dependency | - | Subsystem gọi ngược khi mốc đến hạn | - |
| PD-49 | SS-07 | IF-07 | Realization | - | Subsystem hiện thực interface | - |

## F8. Subsystem context diagram

File diagrams/P10-subsystem-context.drawio, mỗi subsystem một trang (7 trang). Mỗi trang gồm interface dạng canonical kèm trách nhiệm dạng "// ...", subsystem hiện thực nó (nằm ngang với interface), interface gọi ngược nếu có, và các lớp thiết kế phụ thuộc vào interface hoặc hiện thực interface gọi ngược. Toạ độ ở bảng Node là tuyệt đối trên trang.

### Trang SS-01 OnlinePayment

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-PurchaseOrRenewPackageHandler | Class | DC-PurchaseOrRenewPackageHandler | - | PKG-14 | public | 40 | 40 | 240 | 50 |
| IF-08 | Interface | IPaymentResultReceiver | «interface» | PKG-23 | public; trách nhiệm: // returnPaymentResult | 40 | 200 | 260 | 60 |
| SS-01 | Subsystem | SS-01 OnlinePayment | «subsystem» | PKG-23 | Không public (chỉ interface public) | 380 | 200 | 170 | 60 |
| IF-01 | Interface | IPaymentGateway | «interface» | PKG-23 | public; trách nhiệm: // requestPayment | 630 | 200 | 260 | 60 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SC01-01 | SS-01 | IF-01 | Realization | - | Subsystem hiện thực interface | - |
| SC01-02 | SS-01 | IF-08 | Dependency | - | Subsystem gọi ngược qua interface | - |
| SC01-03 | DC-PurchaseOrRenewPackageHandler | IF-01 | Dependency | - | Lớp thiết kế dùng interface | (160,120); (760,120) |
| SC01-04 | DC-PurchaseOrRenewPackageHandler | IF-08 | Realization | - | Lớp hiện thực interface gọi ngược; realization đi xuống | - |

### Trang SS-02 EInvoiceSubmission

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-PurchaseOrRenewPackageHandler | Class | DC-PurchaseOrRenewPackageHandler | - | PKG-14 | public | 40 | 40 | 240 | 50 |
| SS-02 | Subsystem | SS-02 EInvoiceSubmission | «subsystem» | PKG-25 | Không public (chỉ interface public) | 40 | 200 | 170 | 60 |
| IF-02 | Interface | IEInvoiceGateway | «interface» | PKG-25 | public; trách nhiệm: // sendTransactionData | 290 | 200 | 260 | 60 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SC02-01 | SS-02 | IF-02 | Realization | - | Subsystem hiện thực interface | - |
| SC02-02 | DC-PurchaseOrRenewPackageHandler | IF-02 | Dependency | - | Lớp thiết kế dùng interface | (160,120); (420,120) |

### Trang SS-03 PushNotification

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-CancelUnderBookedClassHandler | Class | DC-CancelUnderBookedClassHandler | - | PKG-15 | package-private | 40 | 40 | 240 | 50 |
| SS-03 | Subsystem | SS-03 PushNotification | «subsystem» | PKG-24 | Không public (chỉ interface public) | 40 | 200 | 170 | 60 |
| IF-03 | Interface | IPushNotificationGateway | «interface» | PKG-24 | public; trách nhiệm: // sendPushNotification | 290 | 200 | 260 | 60 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SC03-01 | SS-03 | IF-03 | Realization | - | Subsystem hiện thực interface | - |
| SC03-02 | DC-CancelUnderBookedClassHandler | IF-03 | Dependency | - | Lớp thiết kế dùng interface | (160,120); (420,120) |

### Trang SS-04 SmsMessaging

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-CancelUnderBookedClassHandler | Class | DC-CancelUnderBookedClassHandler | - | PKG-15 | package-private | 40 | 40 | 240 | 50 |
| SS-04 | Subsystem | SS-04 SmsMessaging | «subsystem» | PKG-24 | Không public (chỉ interface public) | 40 | 200 | 170 | 60 |
| IF-04 | Interface | ISmsGateway | «interface» | PKG-24 | public; trách nhiệm: // sendSms | 290 | 200 | 260 | 60 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SC04-01 | SS-04 | IF-04 | Realization | - | Subsystem hiện thực interface | - |
| SC04-02 | DC-CancelUnderBookedClassHandler | IF-04 | Dependency | - | Lớp thiết kế dùng interface | (160,120); (420,120) |

### Trang SS-05 TurnstileAccess

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-EnterBranchHandler | Class | DC-EnterBranchHandler | - | PKG-16 | package-private | 40 | 40 | 240 | 50 |
| IF-09 | Interface | IEntryScanReceiver | «interface» | PKG-16 | public; trách nhiệm: // receiveScannedCode, // sendEntryResult | 40 | 200 | 260 | 80 |
| SS-05 | Subsystem | SS-05 TurnstileAccess | «subsystem» | PKG-12 | Không public (chỉ interface public) | 380 | 200 | 170 | 60 |
| IF-05 | Interface | ITurnstileEndpoint | «interface» | PKG-12 | public; trách nhiệm: // enableReceiving, // disableReceiving, // registerScanReceiver | 630 | 200 | 260 | 100 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SC05-01 | SS-05 | IF-05 | Realization | - | Subsystem hiện thực interface | - |
| SC05-02 | SS-05 | IF-09 | Dependency | - | Subsystem gọi ngược qua interface | - |
| SC05-03 | DC-EnterBranchHandler | IF-09 | Realization | - | Lớp hiện thực interface gọi ngược; realization đi xuống | (160,120); (170,120) |

### Trang SS-06 DurableScheduler

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-PurchaseOrRenewPackageHandler | Class | DC-PurchaseOrRenewPackageHandler | - | PKG-14 | public | 40 | 40 | 240 | 50 |
| DC-CancelUnderBookedClassHandler | Class | DC-CancelUnderBookedClassHandler | - | PKG-15 | package-private | 320 | 40 | 240 | 50 |
| IF-10 | Interface | IScheduleMarkHandler | «interface» | PKG-22 | public; trách nhiệm: // handleMarkDue | 40 | 200 | 260 | 60 |
| SS-06 | Subsystem | SS-06 DurableScheduler | «subsystem» | PKG-22 | Không public (chỉ interface public) | 380 | 200 | 170 | 60 |
| IF-06 | Interface | IScheduler | «interface» | PKG-22 | public; trách nhiệm: // scheduleMark, // cancelMark, // registerMarkHandler, // start, // stop | 630 | 200 | 260 | 140 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SC06-01 | SS-06 | IF-06 | Realization | - | Subsystem hiện thực interface | - |
| SC06-02 | SS-06 | IF-10 | Dependency | - | Subsystem gọi ngược qua interface | - |
| SC06-03 | DC-PurchaseOrRenewPackageHandler | IF-06 | Dependency | - | Lớp thiết kế dùng interface | (160,120); (750,120) |
| SC06-04 | DC-PurchaseOrRenewPackageHandler | IF-10 | Realization | - | Lớp hiện thực interface gọi ngược; realization đi xuống | (170,130); (160,130) |
| SC06-05 | DC-CancelUnderBookedClassHandler | IF-06 | Dependency | - | Lớp thiết kế dùng interface | (440,140); (760,140) |
| SC06-06 | DC-CancelUnderBookedClassHandler | IF-10 | Realization | - | Lớp hiện thực interface gọi ngược; realization đi xuống | (450,150); (170,150) |

### Trang SS-07 Authentication

Node:

| ID | Loại | Nhãn | Stereotype | Thuộc về (PKG) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| DC-PurchaseOrRenewPackageController | Class | DC-PurchaseOrRenewPackageController | - | PKG-10 | package-private | 40 | 40 | 240 | 50 |
| DC-BookClassSpotController | Class | DC-BookClassSpotController | - | PKG-10 | package-private | 320 | 40 | 240 | 50 |
| DC-SellPackageController | Class | DC-SellPackageController | - | PKG-11 | package-private | 600 | 40 | 240 | 50 |
| SS-05 | Subsystem | SS-05 TurnstileAccess | «subsystem» | PKG-12 | Không public (chỉ interface public) | 880 | 40 | 150 | 50 |
| SS-07 | Subsystem | SS-07 Authentication | «subsystem» | PKG-21 | Không public (chỉ interface public) | 40 | 200 | 170 | 60 |
| IF-07 | Interface | IAuthenticator | «interface» | PKG-21 | public; trách nhiệm: // authenticateCaller, // identifyCallerRole | 290 | 200 | 260 | 80 |

Edge:

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SC07-01 | SS-07 | IF-07 | Realization | - | Subsystem hiện thực interface | - |
| SC07-02 | DC-PurchaseOrRenewPackageController | IF-07 | Dependency | - | Lớp thiết kế dùng interface | (160,120); (410,120) |
| SC07-03 | DC-BookClassSpotController | IF-07 | Dependency | - | Lớp thiết kế dùng interface | (440,130); (420,130) |
| SC07-04 | DC-SellPackageController | IF-07 | Dependency | - | Lớp thiết kế dùng interface | (720,140); (430,140) |
| SC07-05 | SS-05 | IF-07 | Dependency | - | Lớp thiết kế dùng interface | (960,150); (440,150) |

## F9. Mục kiểm soát

Gồm bốn mục Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở ngay dưới đây.

## Câu hỏi mở

Không có

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P09 | F4 (PKG-23, PKG-24, PKG-25, PKG-27, PKG-28) | Chữ ký interface của subsystem ở Services dùng kiểu tiền, số điện thoại, mã tham chiếu giao dịch; P09 ghi PKG-23, PKG-24, PKG-25 không phụ thuộc package nào và chưa có package kiểu giá trị ở Domain | Thêm PKG-32 ValueTypes (PKG-04 Domain) và các cạnh PKG-23, PKG-24, PKG-25, PKG-27, PKG-28 --> PKG-32 vào F4, F6, F9. Chưa áp dụng |
| P09 | F6 V4; F5 dòng Boundary giao diện thiết bị | V4 chỉ nêu hai chỗ gọi ngược (mốc hẹn, kho dữ liệu). P10 thêm IF-08 (kết quả thanh toán) và IF-09 (lượt quét của cửa quay); F5 xếp cửa quay là điểm vào ở PKG-12 và không phải subsystem, P10 đặt SS-05 trong PKG-12 | Bổ sung hai chỗ gọi ngược vào V4 và ghi PKG-12 chứa SS-05, IF-05. Chưa áp dụng |
| P08 | AC-E-Member (activatePackage, checkPackageEligibility, checkDailyBookingLimit, recordEntryScan), AC-E-EntryScan | Bốn trách nhiệm của AC-E-Member hỏi dữ liệu ở package Domain khác (P09 F8); recordEntryScan trùng createEntryScan của AC-E-EntryScan | Khi chạy lại P08, ghi phân bổ theo F3 của P10 (DC-MemberPackages, DC-MemberBookingQuota, DC-EntryScan) và bỏ recordEntryScan khỏi AC-E-Member. Chưa áp dụng |

Các đề xuất sửa của các bước trước chờ câu trả lời Q (theo YEU_CAU_BO_SUNG) không được lặp lại ở đây.

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Hồ sơ dự án: NEN_TANG, CONG_NGHE đã ghi đúng khối F11 của P09, mẫu F3 của P09 (front-end/back-end, layered nới lỏng, component kết hợp Flux, REST controller MVC passive) khớp React Native, React SPA, NestJS nên không có lệch công nghệ. Q-76, Q-94 đóng theo hồ sơ đã cập nhật sau P09; P10 không dẫn hai mã này như câu hỏi còn mở.
- Target 1: phạm vi chỉ có 23 lớp phân tích của bốn use case; 24 use case còn lại chưa có P07. Package giữ chỗ không có phần tử: PKG-06, PKG-08, PKG-09, PKG-13, PKG-17, PKG-18, PKG-19, PKG-31. Chạy lại P10 khi P08, P09 thay đổi.
- Cạnh phụ thuộc của P09 chưa suy ra vì chưa có phần tử nguồn: PKG-14 --> PKG-24 (Q-53, UC-008), PKG-15 --> PKG-30 (UC-016), PKG-16 --> PKG-25 (UC-017), mọi cạnh của PKG-13, PKG-17, PKG-18, PKG-19. Nếu Q-45 trả lời cổng thanh toán tự gửi kết quả về, cần cạnh PKG-12 --> IF-01 và thao tác nhận thông điệp của cổng trong IF-01 (P11b); hợp lệ về layer.
- Target 4: SS-05 là thiết bị gọi vào qua API nên không có phía phần mềm tự gọi thiết bị. IF-05 gồm bật, tắt, đăng ký bộ nhận theo Target; bước khởi động tiến trình API gọi IF-05, nằm ngoài các package của mô hình nên IF-05 không có cạnh phụ thuộc tới. IF-09 đặt ở PKG-16 (Application), SS-05 ở PKG-12 (Presentation) nên phụ thuộc đã đi xuống, interface được giữ để tách giao thức thiết bị khỏi control.
- SS-06, SS-07 không có lớp phân tích nguồn; trách nhiệm lấy từ P09 nên tạm, chờ Q-93 (độ lệch mốc), Q-47, Q-89 (xác thực, bảo mật). SS-07 được xét vì PKG-10, PKG-11, PKG-12 phụ thuộc PKG-21 cho UC-005, UC-010, UC-018.
- DC-PurchaseOrRenewPackageHandler hiện thực IF-10 và còn trách nhiệm giữ trạng thái chờ (startWaitingForPayment, stopWaitingForPayment, handlePaymentTimeout) mà P09 đã đề xuất sửa P07 UC-005 và chưa áp dụng; lớp hiện thực IF-10 có thể đổi khi P07 đổi, PKG không đổi. Tương tự DC-CancelUnderBookedClassHandler (cancelAbsenceMark, cancelWaitlistTransferMark, Q-64).
- PKG-05 gộp giao diện của ACT-01 và ACT-02: hiện chỉ chứa phần tử của ACT-02 nên không vi phạm quy tắc tác nhân. Khi có P07 của UC-001, UC-002, UC-003, giữ PKG-05 làm package cha, cấp package con theo tác nhân (mã từ PKG-33) và ghi Đề xuất sửa P09.
- Phần tiếp nhận yêu cầu REST (PKG-10, PKG-11) nhóm theo loại client như P09, không tách theo tác nhân; quy tắc tác nhân của A3 chỉ áp dụng cho View, Store ở PKG-05, PKG-07.
- Quan hệ DC-PackageOrder với DC-MembershipPackage, DC-PackagePrice chưa có (Q-82, Q-87) nên chưa có cạnh PKG-27 --> PKG-28 hay ngược lại; nếu thêm, giữ một chiều trong cùng layer Domain.
- PKG-20 Persistence phục vụ 5 package Domain; giữ một package vì cùng lý do thay đổi (đổi cách truy cập CSDL). Nếu P12 thấy cohesion thấp thì tách theo nhóm chức năng, không đổi layer (P09 Vấn đề còn mở).
- Phụ thuộc trực tiếp từ Application tới PKG-32 chưa ghi vì chữ ký interface chưa chốt (P11b); bổ sung khi có, chiều hợp lệ (layer trên phụ thuộc layer dưới). Kiểu định danh sẽ thêm vào PKG-32 khi P11b, P12 cần.
- Chọn giữa hai quy tắc (C9): (1) prompt đặt phạm vi toàn hệ thống, YEU_CAU_BO_SUNG giới hạn phân tích ở bốn use case; theo YEU_CAU_BO_SUNG (ưu tiên 2) chỉ lớp của bốn use case có phần tử, package còn lại giữ chỗ. (2) A1 coi boundary thiết bị là subsystem, P09 F5 xếp cửa quay là điểm vào ở PKG-12; theo thứ tự ưu tiên A3 (quy tắc layer của P09 trước), SS-05 nằm trong PKG-12.
