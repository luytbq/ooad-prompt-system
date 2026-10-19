# P08 - Mô hình phân tích hợp nhất - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P08 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P05-glossary.md (phiên bản 1.0; Mục 2, Câu hỏi mở, Đề xuất sửa artifact trước); P06-supplementary-spec.md (phiên bản 1.0; Mục 3 đến Mục 5 các dòng NFR liên quan, Mục 6 sổ BR, Câu hỏi mở); P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md, UC-010-book-class-spot-analysis.md, UC-015-cancel-under-booked-class-analysis.md, UC-018-enter-branch-analysis.md (phiên bản 1.0; F3.4, F6, F8 b), Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở). P04-uc-specs/ không tra lại vì P05, P06, P07 đã đủ bằng chứng. Mã Q, ASM quét ở mục Câu hỏi mở, Giả định của mọi artifact trong thư mục đầu ra (Q-86 lớn nhất trước lần chạy; chưa có ASM). CACH_CHIA_VIEW: Không có (áp dụng quy tắc mặc định ở F5). YEU_CAU_BO_SUNG: phạm vi lần này là UC-005, UC-010, UC-015, UC-018, các use case khác của P02 chưa đặc tả, chưa phân tích; đề xuất sửa artifact trước của P04, P05, P06, P07 chưa áp dụng và các bước đó không chạy lại; REQ mà đặc tả P04 đề nghị thêm vào cột REQ của P02 chỉ là dữ liệu do use case khác cung cấp; các đề xuất đổi cách gọi của P05 chưa áp dụng vào P00 đến P04; hai đề xuất của P07 (UC-005 chờ Q-82, UC-010 chờ Q-83) chưa áp dụng vì chờ câu trả lời |
| Phạm vi | UC-005, UC-010, UC-015, UC-018 (bốn use case có artifact P07); 24 use case còn lại của P02 chưa phân tích, xem F1 |
| Mã Q, ASM cuối đã cấp | Q-87; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Độ phủ use case

| UC | Tên | File P07 | Trạng thái |
|---|---|---|---|
| UC-001 | Xem giá gói tập | - | Chưa phân tích |
| UC-002 | Xem lịch lớp nhóm | - | Chưa phân tích |
| UC-003 | Đăng ký tài khoản hội viên | - | Chưa phân tích |
| UC-004 | Đăng nhập | - | Chưa phân tích |
| UC-005 | Mua hoặc gia hạn gói tập | P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md | Đã phân tích |
| UC-006 | Bảo lưu gói tập | - | Chưa phân tích |
| UC-007 | Chuyển nhượng gói tập | - | Chưa phân tích |
| UC-008 | Nhắc gia hạn gói tập | - | Chưa phân tích |
| UC-009 | Lập lịch lớp nhóm | - | Chưa phân tích |
| UC-010 | Đặt chỗ lớp nhóm | P07-uc-analysis/UC-010-book-class-spot-analysis.md | Đã phân tích |
| UC-011 | Huỷ chỗ lớp nhóm | - | Chưa phân tích |
| UC-012 | Nhận chỗ từ danh sách chờ | - | Chưa phân tích |
| UC-013 | Chuyển chỗ cho người kế tiếp | - | Chưa phân tích |
| UC-014 | Huỷ lớp nhóm vì sự cố | - | Chưa phân tích |
| UC-015 | Huỷ lớp nhóm ít người đặt | P07-uc-analysis/UC-015-cancel-under-booked-class-analysis.md | Đã phân tích |
| UC-016 | Ghi nhận vắng mặt lớp nhóm | - | Chưa phân tích |
| UC-017 | Bán vé tập một ngày | - | Chưa phân tích |
| UC-018 | Vào chi nhánh | P07-uc-analysis/UC-018-enter-branch-analysis.md | Đã phân tích |
| UC-019 | Mua gói buổi tập cá nhân | - | Chưa phân tích |
| UC-020 | Đặt buổi tập cá nhân | - | Chưa phân tích |
| UC-021 | Phản hồi yêu cầu đặt buổi tập | - | Chưa phân tích |
| UC-022 | Huỷ yêu cầu đặt buổi quá hạn | - | Chưa phân tích |
| UC-023 | Huỷ buổi tập cá nhân | - | Chưa phân tích |
| UC-024 | Ghi nhận buổi tập cá nhân | - | Chưa phân tích |
| UC-025 | Xem chỉ số cơ thể | - | Chưa phân tích |
| UC-026 | Đặt giá gói tập | - | Chưa phân tích |
| UC-027 | Đặt chương trình khuyến mãi | - | Chưa phân tích |
| UC-028 | Xem báo cáo chuỗi | - | Chưa phân tích |

## F2. Nhật ký hợp nhất

| STT | Lớp gốc (AC, tên) | UC nguồn | Tình huống | Kết quả | Bằng chứng (GL, BR, bước UC) |
|---|---|---|---|---|---|
| 1 | AC-B-PurchaseOrRenewPackageUI, PurchaseOrRenewPackageUI | UC-005 | Giữ nguyên | Giữ | UC-005 bước 1, 2, 3, 6, 7, 9a2, 10a, 13; GL-16 |
| 2 | AC-B-SellPackageUI, SellPackageUI | UC-005 | Giữ nguyên | Giữ | UC-005 bước 1, 2, 3, 6, 7, 8a, 8b, 13; GL-31 |
| 3 | AC-B-PaymentGateway, PaymentGateway | UC-005 | Giữ nguyên | Giữ | UC-005 bước 9, 10; - |
| 4 | AC-B-EInvoiceGateway, EInvoiceGateway | UC-005 | Giữ nguyên | Giữ | UC-005 bước 12; GL-18 |
| 5 | AC-C-PurchaseOrRenewPackageHandler, PurchaseOrRenewPackageHandler | UC-005 | Giữ nguyên | Giữ | UC-005 bước 1-13, 8a, 8b, 9a, 10a; - |
| 6 | AC-E-MembershipPackage, MembershipPackage | UC-005 | Giữ nguyên | Giữ, hợp trách nhiệm và thuộc tính (xem F2a) | UC-005 bước 4, 11; GL-16; đồng thời dùng ở UC-018 |
| 7 | AC-E-Member, Member | UC-005 | Giữ nguyên | Giữ | UC-005 bước 11; GL-19; mã cấp sớm nhất; chủ sở hữu UC-003 |
| 8 | AC-E-PackageOrder, PackageOrder | UC-005 | Giữ nguyên | Giữ | UC-005 bước 8, 9a1, 11; GL-09 |
| 9 | AC-E-PaymentTransaction, PaymentTransaction | UC-005 | Giữ nguyên | Giữ | UC-005 bước 11, 12; GL-12, GL-31 |
| 10 | AC-E-PackagePrice, PackagePrice | UC-005 | Giữ nguyên | Giữ | UC-005 bước 2, 5; GL-10, GL-37; chủ sở hữu UC-026 |
| 11 | AC-E-Promotion, Promotion | UC-005 | Giữ nguyên | Giữ | UC-005 bước 5; GL-07; chủ sở hữu UC-027 |
| 12 | AC-B-BookClassSpotUI, BookClassSpotUI | UC-010 | Giữ nguyên | Giữ | UC-010 bước 1, 2, 3, 4a, 5a, 5b, 6a, 7a1, 7a2, 7a4, 9; GL-26, GL-29 |
| 13 | AC-C-BookClassSpotHandler, BookClassSpotHandler | UC-010 | Giữ nguyên | Giữ | UC-010 bước 1-9, 4a, 5a, 5b, 6a, 7a1-7a4; - |
| 14 | AC-E-Member, Member | UC-010 | Tái dùng mã | Giữ | UC-010 bước 4, 6; GL-19, GL-23; cùng mã AC-E-Member của UC-005 |
| 15 | AC-E-GroupClass, GroupClass | UC-010 | Giữ nguyên | Giữ, hợp trách nhiệm và thuộc tính (xem F2a) | UC-010 bước 2, 5, 7, 7a3, 8, 9; GL-29, GL-13, GL-26, GL-27, GL-35, GL-21, GL-38, GL-28; chủ sở hữu UC-009 |
| 16 | AC-E-ClassBooking, ClassBooking | UC-010 | Giữ nguyên | Giữ | UC-010 bước 8; GL-05 |
| 17 | AC-E-Waitlist, Waitlist | UC-010 | Giữ nguyên | Giữ | UC-010 bước 7a3; GL-08; có hay không đối tượng danh sách chờ: Q-84 |
| 18 | AC-B-PushNotificationGateway, PushNotificationGateway | UC-015 | Giữ nguyên | Giữ | UC-015 bước 6, 7; GL-39 |
| 19 | AC-B-SmsGateway, SmsGateway | UC-015 | Giữ nguyên | Giữ | UC-015 bước 6, 7; GL-36 |
| 20 | AC-C-CancelUnderBookedClassHandler, CancelUnderBookedClassHandler | UC-015 | Giữ nguyên | Giữ | UC-015 bước 1-7, 2a, 2b, 5a; - |
| 21 | AC-E-GroupClass, GroupClass | UC-015 | Tái dùng mã | Giữ, hợp trách nhiệm và thuộc tính (xem F2a) | UC-015 bước 2, 2a, 2b, 3, 5, 5a, 6; GL-29, GL-13; cùng mã AC-E-GroupClass của UC-010 |
| 22 | AC-E-ClassBooking, ClassBooking | UC-015 | Tái dùng mã | Giữ | UC-015 bước 5; GL-05; cùng mã AC-E-ClassBooking của UC-010 |
| 23 | AC-E-Member, Member | UC-015 | Tái dùng mã | Giữ | UC-015 bước 6, 7; GL-19, GL-20; cùng mã AC-E-Member của UC-005 |
| 24 | AC-B-TurnstileDevice, TurnstileDevice | UC-018 | Giữ nguyên | Giữ | UC-018 bước 1, 2, 3a1a, 3a1b, 3b, 4a, 4b, 4c, 6, 7; GL-30, GL-32 |
| 25 | AC-C-EnterBranchHandler, EnterBranchHandler | UC-018 | Giữ nguyên | Giữ | UC-018 bước 2-6, 3a, 3a1, 3a1a, 3a1b, 3b, 4a, 4b, 4c; - |
| 26 | AC-E-Member, Member | UC-018 | Tái dùng mã | Giữ | UC-018 bước 3, 4, 4a, 4b, 4c, 5; GL-19, GL-32; cùng mã AC-E-Member của UC-005 |
| 27 | AC-E-MembershipPackage, MembershipPackage | UC-018 | Tái dùng mã | Giữ, hợp trách nhiệm và thuộc tính (xem F2a) | UC-018 bước 4, 4a, 4b, 4c; GL-01, GL-16, GL-17; cùng mã AC-E-MembershipPackage của UC-005 |
| 28 | AC-E-EntryScan, EntryScan | UC-018 | Giữ nguyên | Giữ | UC-018 bước 5; GL-30 |
| 29 | AC-E-DayPass, DayPass | UC-018 | Giữ nguyên | Giữ | UC-018 bước 3a, 3a1, 3a1a, 3a1b; GL-42, GL-32; chủ sở hữu UC-017 |

Các dòng Tái dùng mã có kết quả "Giữ": trách nhiệm và thuộc tính của use case đó hợp thẳng vào lớp, không trùng và không mâu thuẫn với use case khác. Mọi dòng có kết quả "Giữ, hợp trách nhiệm và thuộc tính (xem F2a)" có dòng tương ứng ở F2a.

## F2a. Nhật ký trách nhiệm, thuộc tính và cặp đã xét

| STT | Lớp | Mục gốc (trách nhiệm, thuộc tính hoặc cặp lớp) | UC nguồn | Tình huống | Kết quả | Bằng chứng |
|---|---|---|---|---|---|---|
| 1 | AC-E-GroupClass | // provideCancelledClassInfo (cung cấp loại lớp và giờ học của lớp bị huỷ) và // provideClassInfo (cung cấp loại lớp, phòng, huấn luyện viên, giờ học) | UC-015, UC-010 | Đổi tên trách nhiệm | Giữ tên provideClassInfo (cấp sớm nhất ở UC-010); provideCancelledClassInfo của UC-015 hợp vào, dữ liệu UC-015 cần (loại lớp, giờ học) là tập con của dữ liệu provideClassInfo | Cùng ý nghĩa là cung cấp thông tin mô tả một lớp nhóm cho nơi gọi; GL-29 (lớp nhóm gồm loại lớp, phòng, huấn luyện viên, giờ học); UC-015 bước 6; nội dung thông báo chưa chốt (Q-66) |
| 2 | AC-E-MembershipPackage | status (Trạng thái): giá trị đã kích hoạt ở UC-005 bước 11, giá trị đang bảo lưu ở UC-018 | UC-005, UC-018 | Mở rộng tập giá trị thuộc tính | Giữ một thuộc tính status, tập giá trị là hợp của hai nơi; quan hệ loại trừ giữa các giá trị chờ Q-75 | GL-16 (Ghi chú: trạng thái nguồn nêu), GL-01, BR-16, Q-75 |
| 3 | AC-E-PackagePrice, AC-E-MembershipPackage | Cặp có tên gần nhau, trùng thuộc tính durationMonths, packageType, appliedBranch | UC-005 | Cặp đã xét, giữ tách | Giữ hai lớp | GL-10 (số tiền để mua một gói tập) khác GL-16 (quyền vào tập mà hội viên có được sau khi mua); giá do giám đốc chuỗi đặt và đổi theo thời gian, gói tập thuộc một hội viên; Q-82 hỏi mặt hàng được bán có chính là Giá gói không; Q-87 |
| 4 | AC-E-PackageOrder, AC-E-MembershipPackage | Cặp trùng thuộc tính durationMonths, packageType, appliedBranch, startDate, status | UC-005 | Cặp đã xét, giữ tách | Giữ hai lớp | GL-09 (chứng từ ghi nhận một lần mua) khác GL-16; đơn có trước gói và có thể bị huỷ khi gói chưa tồn tại (BR-04); Q-87 |
| 5 | AC-E-PackagePrice, AC-E-PackageOrder | Cặp trùng thuộc tính durationMonths, packageType, appliedBranch | UC-005 | Cặp đã xét, giữ tách | Giữ hai lớp | GL-10 là số tiền hiện hành, GL-09 là một lần mua với số tiền phải trả đã tính (GL-37); Q-82, Q-87 |
| 6 | AC-E-PackageOrder, AC-E-PaymentTransaction | Cặp cùng gắn với khoản tiền (amountDue, amount) | UC-005 | Cặp đã xét, giữ tách | Giữ hai lớp | GL-09 khác GL-12 (một lần VietFit thu tiền); đơn có thể không có hoặc có nhiều giao dịch (Q-13, Q-81), giao dịch của use case khác chưa rõ có đơn (Q-38) |
| 7 | AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI | Cặp boundary giao diện người dùng cùng use case, trùng bốn trách nhiệm (showPackageOptions, selectPackage, showOrderSummary, showActivatedPackage) và bốn thuộc tính | UC-005 | Cặp đã xét, giữ tách | Giữ hai boundary: khác tác nhân (ACT-02 hội viên, ACT-05 lễ tân), mặc định mỗi cặp tác nhân - use case một boundary; SellPackageUI có thêm xác nhận thu tiền mặt, nhập mã giao dịch POS, người mua | GL-16, GL-31; P01 ACT-02, ACT-05; UC-005 bước 8a, 8b |
| 8 | AC-B-PaymentGateway, AC-B-EInvoiceGateway | Cặp cùng hậu tố Gateway, cùng gắn với giao dịch thu tiền | UC-005 | Cặp đã xét, giữ tách | Giữ hai boundary: hai hệ thống ngoài khác nhau, không áp dụng "Boundary hệ thống trùng" | P01 ACT-08, ACT-11; NFR-07, NFR-12 |
| 9 | AC-B-PushNotificationGateway, AC-B-SmsGateway | Cặp cùng được AC-C-CancelUnderBookedClassHandler gọi để gửi thông báo, trách nhiệm tương tự | UC-015 | Cặp đã xét, giữ tách | Giữ hai boundary: hai hệ thống ngoài khác nhau, mỗi hội viên nhận một trong hai kênh theo BR-14 | P01 ACT-10, ACT-09; GL-36, GL-39; BR-14; NFR-10, NFR-11 |
| 10 | AC-C-BookClassSpotHandler, AC-C-CancelUnderBookedClassHandler | Cặp control cùng điều phối AC-E-GroupClass và AC-E-Member | UC-010, UC-015 | Cặp đã xét, giữ tách | Giữ hai control: control của hai use case khác nhau không gộp, P02 không coi hai use case là một | P02 Bảng 4a: UC-010 tác nhân chính ACT-02, UC-015 tác nhân chính ACT-14 |
| 11 | AC-E-ClassBooking, AC-E-Waitlist | Cặp cùng gắn một hội viên với một lớp nhóm | UC-010 | Cặp đã xét, giữ tách | Giữ hai lớp | GL-05 (chỗ đã đặt chiếm phần sức chứa) khác GL-08 (danh sách có thứ tự hội viên chờ, chưa giữ chỗ); BR-12 chỉ cho vào danh sách chờ khi lớp đã đủ chỗ; Q-22, Q-84 |
| 12 | AC-E-MembershipPackage, AC-E-DayPass | Cặp cùng được cửa quay kiểm tra để mở cửa, cùng có hạn dùng | UC-018 | Cặp đã xét, giữ tách | Giữ hai lớp | GL-16 khác GL-42: gói tập gắn hội viên, thời hạn theo tháng; vé gắn chi nhánh và ngày mua, không gắn hội viên (BR-18, BR-19, GL-22) |

Không có dòng Gộp trách nhiệm cùng tên, Tách trách nhiệm cùng tên, Chuyển trách nhiệm sang lớp toàn thể, Thuộc tính mâu thuẫn: không có hai trách nhiệm cùng tên khác ý nghĩa trên một lớp, các phép đếm và tổng hợp trên tập đã nằm ở lớp toàn thể (Member, GroupClass, Waitlist) theo P07 A6, và các thuộc tính trùng giữa các use case cùng kiểu, cùng nghĩa.

## F3. Bảng lớp hợp nhất

| AC | Stereotype | Tên | Trách nhiệm (gộp) | Thuộc tính | Dùng trong UC | Loại boundary | Trạng thái |
|---|---|---|---|---|---|---|---|
| AC-B-PurchaseOrRenewPackageUI | boundary | PurchaseOrRenewPackageUI | // requestPurchaseOrRenewal: nhận yêu cầu mua hoặc gia hạn của hội viên (UC-005)<br>// showPackageOptions: hiển thị các gói tập kèm thời hạn, loại, giá hiện hành (UC-005)<br>// selectPackage: nhận gói đã chọn, kiểm tra hình thức dữ liệu nhập (thời hạn, loại bắt buộc) (UC-005)<br>// showOrderSummary: hiển thị tóm tắt đơn mua (gói, ngày bắt đầu, số tiền phải trả) (UC-005)<br>// confirmPurchase: nhận xác nhận mua của hội viên (UC-005)<br>// showOrderCancelledNotice: thông báo cho hội viên đơn mua bị huỷ do hết thời hạn thanh toán (kênh: Q-53) (UC-005)<br>// showPaymentFailedNotice: thông báo cho hội viên giao dịch thu tiền không thành công (kênh: Q-53) (UC-005)<br>// showActivatedPackage: hiển thị gói tập đã kích hoạt (UC-005) | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew | UC-005 | Giao diện người dùng (ACT-02) | Hoạt động |
| AC-B-SellPackageUI | boundary | SellPackageUI | // requestPackageSale: nhận yêu cầu bán gói tập của lễ tân (UC-005)<br>// showPackageOptions: hiển thị các gói tập kèm thời hạn, loại, giá hiện hành (UC-005)<br>// selectPackage: nhận gói đã chọn và người mua gói, kiểm tra hình thức dữ liệu nhập (UC-005)<br>// showOrderSummary: hiển thị tóm tắt đơn mua cho lễ tân (UC-005)<br>// confirmSale: nhận xác nhận bán của lễ tân (UC-005)<br>// confirmCashCollected: nhận xác nhận lễ tân đã thu đủ tiền mặt (UC-005)<br>// enterPosTransactionCode: nhận mã giao dịch POS, kiểm tra bắt buộc nhập (UC-005)<br>// showActivatedPackage: hiển thị gói tập đã kích hoạt cho lễ tân (UC-005) | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew<br>buyer<br>posTransactionCode | UC-005 | Giao diện người dùng (ACT-05) | Hoạt động |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestPayment: chuyển thông tin đơn mua cho cổng thanh toán (UC-005)<br>// returnPaymentResult: nhận kết quả giao dịch từ cổng thanh toán và chuyển cho control (UC-005) | - | UC-005 | Giao diện hệ thống (ACT-08) | Hoạt động |
| AC-B-EInvoiceGateway | boundary | EInvoiceGateway | // sendTransactionData: chuyển dữ liệu giao dịch thu tiền cho hệ thống hoá đơn điện tử (UC-005) | - | UC-005 | Giao diện hệ thống (ACT-11) | Hoạt động |
| AC-C-PurchaseOrRenewPackageHandler | control | PurchaseOrRenewPackageHandler | // startPurchase: điều phối hiển thị các gói tập (bước 1-2) (UC-005)<br>// processPackageSelection: điều phối xác định ngày bắt đầu, tính số tiền phải trả, trình tóm tắt đơn mua (bước 3-6) (UC-005)<br>// placeOrder: tạo đơn mua và gửi thông tin đơn cho cổng thanh toán (bước 7-9) (UC-005)<br>// startWaitingForPayment: ghi nhận bắt đầu chờ kết quả thanh toán trong thời hạn BR-04 (UC-005)<br>// handlePaymentTimeout: nhận sự kiện hết thời hạn BR-04, huỷ đơn và báo hội viên (9a) (UC-005)<br>// stopWaitingForPayment: dừng chờ thời hạn BR-04 khi đã nhận kết quả (UC-005)<br>// handlePaymentResult: xử lý kết quả giao dịch: thông báo khi không thành công, hoặc ghi nhận đã thanh toán, kích hoạt gói, gửi hoá đơn điện tử, hiển thị gói (bước 10-13, 10a) (UC-005)<br>// confirmCashPayment: xử lý xác nhận đã thu tiền mặt tại quầy rồi tiếp tục bước 11 (8a) (UC-005)<br>// confirmPosPayment: xử lý mã giao dịch POS đã nhập rồi tiếp tục bước 11 (8b) (UC-005) | - | UC-005 | - | Hoạt động |
| AC-E-MembershipPackage | entity | MembershipPackage | // calculateRenewalStartDate: xác định ngày bắt đầu của gói mới từ ngày hết hạn của gói cũ (BR-03) (UC-005)<br>// initializePackage: nhận thời hạn, loại, ngày bắt đầu; tính ngày hết hạn (Q-74) và đặt trạng thái đã kích hoạt (UC-005)<br>// checkEntryEligibility: kiểm tra gói chưa quá ngày hết hạn (BR-15; Q-74), không đang bảo lưu (BR-16), áp dụng cho chi nhánh của cửa quay (BR-17; Q-50), theo thứ tự đó (UC-018) | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>startDate (Ngày)<br>expiryDate (Ngày)<br>status (Trạng thái) | UC-005, UC-018 | - | Hoạt động |
| AC-E-Member | entity | Member | // activatePackage: tạo gói tập mới và gắn cho hội viên sở hữu (UC-005)<br>// checkBookingNotSuspended: kiểm tra hội viên không đang bị khoá quyền đặt lớp (BR-09) (UC-010)<br>// checkDailyBookingLimit: đếm các chỗ đã đặt của hội viên thuộc lớp diễn ra cùng ngày với lớp đã chọn và so với mức tối đa (BR-08; cách tính ngày Q-60) (UC-010)<br>// determineNotificationChannel: cho biết hội viên nhận thông báo qua thông báo đẩy hay SMS (BR-14; cách xác định hội viên chưa cài ứng dụng Q-36) (UC-015)<br>// matchesQrCode: đối chiếu mã QR đọc được với mã QR của hội viên (Q-68) (UC-018)<br>// checkPackageEligibility: kiểm tra hội viên có gói tập còn hiệu lực, không đang bảo lưu, áp dụng cho chi nhánh của cửa quay, bằng cách hỏi từng gói và tổng hợp kết quả (BR-15, BR-16, BR-17; nhiều gói Q-69) (UC-018)<br>// recordEntryScan: ghi nhận lượt quẹt vào cửa của hội viên kèm chi nhánh và thời điểm quẹt (UC-018) | bookingSuspension (Trạng thái)<br>qrCode (Văn bản) | UC-005, UC-010, UC-015, UC-018 | - | Tạm (chờ P07 của UC-003) |
| AC-E-PackageOrder | entity | PackageOrder | // createOrder: nhận người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả; đặt trạng thái chờ thanh toán (UC-005)<br>// cancelUnpaidOrder: chuyển đơn chưa thanh toán thành công sang trạng thái đã huỷ khi hết thời hạn BR-04 (UC-005)<br>// recordPayment: chuyển đơn sang trạng thái đã thanh toán và ghi nhận giao dịch thu tiền (UC-005) | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>startDate (Ngày)<br>amountDue (Số tiền)<br>status (Trạng thái) | UC-005 | - | Hoạt động |
| AC-E-PaymentTransaction | entity | PaymentTransaction | // createTransaction: nhận phương thức thu, số tiền, mã giao dịch POS (nếu có) (UC-005)<br>// prepareInvoiceData: cung cấp dữ liệu giao dịch thu tiền để gửi hoá đơn điện tử (trường dữ liệu: Q-39) (UC-005) | paymentMethod (Trạng thái)<br>amount (Số tiền)<br>posTransactionCode (Văn bản) | UC-005 | - | Hoạt động |
| AC-E-PackagePrice | entity | PackagePrice | // getPriceInfo: cung cấp thời hạn, loại, chi nhánh áp dụng, giá hiện hành để hiển thị (UC-005)<br>// calculateAmountDue: tính số tiền phải trả từ giá gói và mức giảm áp dụng (Q-09) (UC-005) | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>price (Số tiền) | UC-005 | - | Tạm (chờ P07 của UC-026) |
| AC-E-Promotion | entity | Promotion | // determineApplicableDiscount: xác định mức giảm áp dụng cho gói đã chọn (cách áp dụng: Q-09; loại hàng: Q-08) (UC-005) | validFrom (Ngày)<br>validTo (Ngày)<br>discountRate (Số lượng, tối đa 20% theo BR-38) | UC-005 | - | Tạm (chờ P07 của UC-027) |
| AC-B-BookClassSpotUI | boundary | BookClassSpotUI | // requestBookClass: nhận yêu cầu đặt chỗ lớp nhóm của hội viên (UC-010)<br>// showClassSchedule: hiển thị lịch các lớp nhóm (loại lớp, phòng, huấn luyện viên, giờ học) (UC-010)<br>// selectClass: nhận lớp nhóm hội viên chọn, kiểm tra hình thức (bắt buộc chọn một lớp) (UC-010)<br>// showBookingRejectedNotice: thông báo từ chối yêu cầu đặt chỗ kèm lý do (UC-010)<br>// showClassFullNotice: thông báo lớp đã đủ chỗ và đề nghị vào danh sách chờ (UC-010)<br>// requestJoinWaitlist: nhận yêu cầu vào danh sách chờ của hội viên (UC-010)<br>// showWaitlistPosition: hiển thị loại lớp, giờ học và vị trí trong danh sách chờ (UC-010)<br>// showBookedSpot: hiển thị thông tin chỗ đã đặt (loại lớp, phòng, huấn luyện viên, giờ học) (UC-010) | selectedClass | UC-010 | Giao diện người dùng (ACT-02) | Hoạt động |
| AC-C-BookClassSpotHandler | control | BookClassSpotHandler | // startBooking: điều phối lấy và hiển thị lịch lớp nhóm (bước 1-2) (UC-010)<br>// bookClass: điều phối các kiểm tra quyền đặt lớp, lớp nhóm, số lớp trong ngày, chỗ trống, lưu chỗ đã đặt và hiển thị kết quả (bước 3-9, 4a, 5a, 5b, 6a, 7a1) (UC-010)<br>// joinWaitlist: điều phối thêm hội viên vào danh sách chờ và hiển thị vị trí (7a2-7a4) (UC-010) | - | UC-010 | - | Hoạt động |
| AC-E-GroupClass | entity | GroupClass | // provideClassInfo: cung cấp loại lớp, phòng, huấn luyện viên, giờ học của lớp để hiển thị hoặc đưa vào thông báo (UC-010, UC-015)<br>// checkBookable: kiểm tra lớp chưa bị huỷ và thời điểm đặt nằm trong thời hạn cho phép tính từ giờ học (BR-06, BR-07) (UC-010)<br>// checkSpotAvailable: đếm chỗ đã đặt của lớp và so với sức chứa (BR-10, BR-11) (UC-010)<br>// reserveSpot: kiểm tra lại chỗ trống tại lúc lưu rồi tạo chỗ đã đặt cho hội viên (BR-11) (UC-010)<br>// addToWaitlist: thêm hội viên vào danh sách chờ của lớp và cho biết vị trí (UC-010)<br>// checkUnderBookedCancellable: kiểm tra lớp chưa huỷ và số người đặt chỗ dưới 3 (BR-13; Q-59, Q-22, Q-20) (UC-015)<br>// cancelClass: chuyển trạng thái lớp sang đã huỷ (BR-13) (UC-015)<br>// collectBookedMembers: gom các hội viên đã đặt chỗ của lớp bằng cách hỏi từng chỗ đã đặt (UC-015) | classType (Văn bản)<br>room (Văn bản)<br>trainer (Văn bản)<br>startTime (Ngày, Giờ)<br>capacity (Số lượng)<br>status (Trạng thái) | UC-010, UC-015 | - | Tạm (chờ P07 của UC-009) |
| AC-E-ClassBooking | entity | ClassBooking | // initializeBooking: nhận hội viên và lớp nhóm, ghi nhận chỗ đã đặt (UC-010)<br>// provideBookedMember: cung cấp hội viên đã đặt chỗ này (UC-015) | - | UC-010, UC-015 | - | Hoạt động |
| AC-E-Waitlist | entity | Waitlist | // addMember: thêm hội viên vào danh sách chờ (thứ tự xếp Q-61) và cho biết vị trí của hội viên (UC-010) | - | UC-010 | - | Hoạt động |
| AC-B-PushNotificationGateway | boundary | PushNotificationGateway | // sendPushNotification: nhận yêu cầu gửi thông báo đẩy của một hội viên và chuyển cho dịch vụ thông báo đẩy (UC-015) | - | UC-015 | Giao diện hệ thống (ACT-10) | Hoạt động |
| AC-B-SmsGateway | boundary | SmsGateway | // sendSms: nhận yêu cầu gửi SMS tới một hội viên và chuyển cho cổng SMS (UC-015) | - | UC-015 | Giao diện hệ thống (ACT-09) | Hoạt động |
| AC-C-CancelUnderBookedClassHandler | control | CancelUnderBookedClassHandler | // handleClassCutoff: nhận mốc 2 giờ trước giờ học của một lớp nhóm và điều phối bước 1-7, lặp gửi thông báo cho từng hội viên (UC-015)<br>// cancelAbsenceMark: yêu cầu huỷ mốc tính vắng mặt của UC-016 gắn với lớp (Q-64) (UC-015)<br>// cancelWaitlistTransferMark: yêu cầu huỷ mốc chuyển chỗ của UC-013 gắn với lớp (Q-64) (UC-015) | - | UC-015 | - | Hoạt động |
| AC-B-TurnstileDevice | boundary | TurnstileDevice | // scanQrCode: nhận thao tác đưa mã QR vào đầu đọc của người vào (UC-018)<br>// receiveScannedCode: nhận mã QR đọc được, chi nhánh và thời điểm quẹt từ cửa quay (UC-018)<br>// sendEntryResult: gửi cho cửa quay kết quả cho phép hoặc không cho phép kèm quy tắc bị vi phạm (nội dung và cách báo cho người quét chờ Q-70) (UC-018)<br>// openDoor: yêu cầu cửa quay mở cửa khi kết quả là cho phép (UC-018) | scannedQrCode (Văn bản)<br>turnstileBranch (Văn bản)<br>scanTime (Ngày, Giờ) | UC-018 | Giao diện thiết bị (ACT-12, ACT-02, ACT-03) | Hoạt động |
| AC-C-EnterBranchHandler | control | EnterBranchHandler | // handleEntryRequest: nhận lượt quét từ cửa quay và điều phối xác định hội viên, kiểm tra gói, ghi nhận lượt quẹt, trả kết quả (bước 2-6, 3b, 4a, 4b, 4c) (UC-018)<br>// handleDayPassEntry: điều phối nhánh vé khi mã QR không phải mã hội viên: đối chiếu vé, kiểm tra ngày và chi nhánh, rồi tiếp tục bước 6 (3a, 3a1, 3a1a, 3a1b) (UC-018) | - | UC-018 | - | Hoạt động |
| AC-E-EntryScan | entity | EntryScan | // createEntryScan: khởi tạo lượt quẹt vào cửa từ hội viên, chi nhánh của cửa quay và thời điểm quẹt (UC-018) | scanTime (Ngày, Giờ)<br>branch (Văn bản) | UC-018 | - | Hoạt động |
| AC-E-DayPass | entity | DayPass | // matchesQrCode: đối chiếu mã QR đọc được với mã QR in trên vé (UC-018)<br>// checkUsableToday: kiểm tra hôm nay là ngày mua vé (BR-18) (UC-018)<br>// checkUsableAtBranch: kiểm tra chi nhánh của cửa quay là chi nhánh đã mua vé (BR-19) (UC-018) | qrCode (Văn bản)<br>purchaseDate (Ngày)<br>purchaseBranch (Văn bản) | UC-018 | - | Tạm (chờ P07 của UC-017) |

Không có lớp bị gộp vào lớp khác, không có đồng âm cần tách. Lớp chủ sở hữu ở use case chưa phân tích (Member - UC-003, PackagePrice - UC-026, Promotion - UC-027, GroupClass - UC-009, DayPass - UC-017) ghi trạng thái Tạm; trách nhiệm chỉ gồm những gì bốn use case trong phạm vi cần.

## F4. Bảng quan hệ

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn UC | Bằng chứng | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| R-01 | AC-B-PurchaseOrRenewPackageUI | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | UC-005 | Link LK-02 của communication diagram UC-005 | R-UC005-01; tạm thời |
| R-02 | AC-B-SellPackageUI | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | UC-005 | Link LK-17 của communication diagram UC-005 (biến thể Lễ tân) | R-UC005-02; tạm thời |
| R-03 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackageOrder | Association | - | - | UC-005 | Link LK-06 của communication diagram UC-005 | R-UC005-03; tạm thời |
| R-04 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackagePrice | Association | - | - | UC-005 | Link LK-03 của communication diagram UC-005 | R-UC005-04; tạm thời |
| R-05 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Promotion | Association | - | - | UC-005 | Link LK-05 của communication diagram UC-005 | R-UC005-05; tạm thời |
| R-06 | AC-C-PurchaseOrRenewPackageHandler | AC-E-MembershipPackage | Association | - | - | UC-005 | Link LK-04 của communication diagram UC-005 (gói cũ, cách xác định gói cũ chờ Q-56) | R-UC005-06; tạm thời |
| R-07 | AC-B-PaymentGateway | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | UC-005 | Link LK-07 của communication diagram UC-005 | R-UC005-07; tạm thời |
| R-08 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Member | Association | - | - | UC-005 | Link LK-11 của communication diagram UC-005 | R-UC005-08; tạm thời |
| R-09 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PaymentTransaction | Association | - | - | UC-005 | Link LK-13 của communication diagram UC-005 | R-UC005-09; tạm thời |
| R-10 | AC-B-EInvoiceGateway | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | UC-005 | Link LK-14 của communication diagram UC-005 | R-UC005-10; tạm thời |
| R-11 | AC-E-PackageOrder | AC-E-PaymentTransaction | Association | A ? - B ? | - | UC-005 | GL-09, GL-12; GL-12 gồm giao dịch của UC-007, UC-017, UC-019 mà GL-09 chưa nói có đơn (Q-07, Q-38); số giao dịch của một đơn chờ Q-13, Q-81 | R-UC005-11; P07 ghi phía A là 1, P08 đổi thành ? (đề xuất sửa P07 UC-005) |
| R-12 | AC-E-Member | AC-E-MembershipPackage | Association | A 1 - B ? | - | UC-005, UC-018 | GL-16, GL-19 (gói tập của một hội viên), BR-15, BR-16, BR-17; BR-03 gợi ý hội viên có thể có gói cũ và gói mới cùng lúc nhưng chưa đủ để chốt số gói (Q-69) | R-UC005-12, R-UC018-04 |
| R-13 | AC-E-PackageOrder | AC-E-Member | Association | A 0..* - B ? | - | UC-005 | GL-09 (đơn ghi nhận việc một người mua); GL-11, BR-03 (hội viên mua gói mới nối tiếp gói cũ của mình nên mua được nhiều lần); người mua tại quầy có phải hội viên chờ Q-01 | R-UC005-13; P07 để trống multiplicity, P08 điền phía A theo bằng chứng, phía B chờ Q-01 |
| R-14 | AC-B-BookClassSpotUI | AC-C-BookClassSpotHandler | Association | - | - | UC-010 | Link LK-02 của communication diagram UC-010 | R-UC010-01; tạm thời |
| R-15 | AC-C-BookClassSpotHandler | AC-E-Member | Association | - | - | UC-010 | Link LK-04 của communication diagram UC-010 | R-UC010-02; tạm thời |
| R-16 | AC-C-BookClassSpotHandler | AC-E-GroupClass | Association | - | - | UC-010 | Link LK-03 của communication diagram UC-010 | R-UC010-03; tạm thời |
| R-17 | AC-E-GroupClass | AC-E-ClassBooking | Association | A 1 - B ? | - | UC-010, UC-015 | GL-05 (chỗ đã đặt là chỗ của một lớp nhóm), BR-11, BR-13; số chỗ đã đặt của một lớp chờ Q-22, Q-20, Q-59 | R-UC010-04, R-UC015-05 |
| R-18 | AC-E-GroupClass | AC-E-Waitlist | Association | A 1 - B ? | - | UC-010 | GL-08 (danh sách chờ của một lớp nhóm), BR-12; số danh sách chờ của một lớp chờ Q-84 | R-UC010-05 |
| R-19 | AC-E-Member | AC-E-ClassBooking | Association | A 1 - B ? | - | UC-010, UC-015 | GL-05 (chỗ đã đặt do một hội viên đặt), BR-08; số chỗ đã đặt của một hội viên chờ Q-59, Q-60 | R-UC010-06, R-UC015-06 |
| R-20 | AC-E-Waitlist | AC-E-Member | Association | A ? - B ? | - | UC-010 | GL-08 (danh sách có thứ tự các hội viên chờ nhận chỗ); số hội viên của một danh sách và số danh sách của một hội viên chờ Q-60, Q-61, Q-62, Q-84 | R-UC010-07; P07 để trống multiplicity, P08 ghi ? kèm Q |
| R-21 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | Association | - | - | UC-015 | Link LK-02 của communication diagram UC-015 | R-UC015-01; tạm thời |
| R-22 | AC-C-CancelUnderBookedClassHandler | AC-E-Member | Association | - | - | UC-015 | Link LK-05 của communication diagram UC-015 | R-UC015-02; tạm thời |
| R-23 | AC-B-PushNotificationGateway | AC-C-CancelUnderBookedClassHandler | Association | - | - | UC-015 | Link LK-06 của communication diagram UC-015 | R-UC015-03; tạm thời |
| R-24 | AC-B-SmsGateway | AC-C-CancelUnderBookedClassHandler | Association | - | - | UC-015 | Link LK-08 của communication diagram UC-015 | R-UC015-04; tạm thời |
| R-25 | AC-B-TurnstileDevice | AC-C-EnterBranchHandler | Association | - | - | UC-018 | Link LK-03 của communication diagram UC-018 | R-UC018-01; tạm thời |
| R-26 | AC-C-EnterBranchHandler | AC-E-Member | Association | - | - | UC-018 | Link LK-04 của communication diagram UC-018 | R-UC018-02; tạm thời |
| R-27 | AC-C-EnterBranchHandler | AC-E-DayPass | Association | - | - | UC-018 | Link LK-08 của communication diagram UC-018 (biến thể Khách vãng lai) | R-UC018-03; tạm thời |
| R-28 | AC-E-Member | AC-E-EntryScan | Association | A 1 - B ? | - | UC-018 | GL-30 (lượt quẹt vào cửa của hội viên), UC-018 bước 5; số lượt quẹt của một hội viên chờ Q-86 | R-UC018-05 |

Không có quan hệ Aggregation, Composition, Generalization: không có câu về vòng đời phụ thuộc hay "là một loại" trong glossary, BR, P07. Quan hệ boundary - control và control - entity giữ Association tạm, multiplicity "-". Phía Multiplicity "?" còn lại: R-11 (A, B), R-12 (B), R-13 (B), R-17 (B), R-18 (B), R-19 (B), R-20 (A, B), R-28 (B), mỗi phía có Q trong cột Bằng chứng. Mọi quan hệ R-UCnnn-nn của P07 có mặt trong bảng này: 31 quan hệ P07 hợp thành 28 quan hệ, ba quan hệ trùng cùng cặp lớp, cùng chiều (R-UC015-05, R-UC015-06, R-UC018-04) hợp vào R-17, R-19, R-12.

## F5. Analysis class diagram tổng thể

File diagrams/P08-class-analysis.drawio, bốn trang: Entity (V1, 11 lớp, 8 cạnh), Gói tập (V2, 11 lớp, 13 cạnh), Lớp nhóm (V3, 9 lớp, 11 cạnh), Ra vào chi nhánh (V4, 6 lớp, 5 cạnh). Tên trang theo Nhóm chức năng của P02 Bảng 4a. Hệ thống có 23 lớp nên không gộp các nhóm vào một trang. Một lớp ở k trang có k dòng Node; mxCell ở trang V1 là mã AC, ở trang Vn khác thêm hậu tố __Vn. Cạnh theo quy tắc tương tự (R-nn, R-nn__Vn). Ngăn thuộc tính, ngăn trách nhiệm của mỗi nút lấy từ F3. Hai cạnh R-16 và R-22 giao nhau một điểm ở trang Lớp nhóm vì hai control cùng nối tới GroupClass và Member.

### a) Bảng Node

| ID (mã AC) | ID mxCell | Loại (Class) | Nhãn | Stereotype | Thuộc về (view) | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AC-E-PaymentTransaction | AC-E-PaymentTransaction | Class | PaymentTransaction | «entity» | Entity | paymentMethod (Trạng thái)<br>amount (Số tiền)<br>posTransactionCode (Văn bản) | // createTransaction<br>// prepareInvoiceData | 40 | 40 | 240 | 150 |
| AC-E-PackageOrder | AC-E-PackageOrder | Class | PackageOrder | «entity» | Entity | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>startDate (Ngày)<br>amountDue (Số tiền)<br>status (Trạng thái) | // createOrder<br>// cancelUnpaidOrder<br>// recordPayment | 40 | 300 | 240 | 230 |
| AC-E-Member | AC-E-Member | Class | Member | «entity» | Entity | bookingSuspension (Trạng thái)<br>qrCode (Văn bản) | // activatePackage<br>// checkBookingNotSuspended<br>// checkDailyBookingLimit<br>// determineNotificationChannel<br>// matchesQrCode<br>// checkPackageEligibility<br>// recordEntryScan | 380 | 300 | 240 | 230 |
| AC-E-ClassBooking | AC-E-ClassBooking | Class | ClassBooking | «entity» | Entity | - | // initializeBooking<br>// provideBookedMember | 380 | 40 | 240 | 110 |
| AC-E-GroupClass | AC-E-GroupClass | Class | GroupClass | «entity» | Entity | classType (Văn bản)<br>room (Văn bản)<br>trainer (Văn bản)<br>startTime (Ngày, Giờ)<br>capacity (Số lượng)<br>status (Trạng thái) | // provideClassInfo<br>// checkBookable<br>// checkSpotAvailable<br>// reserveSpot<br>// addToWaitlist<br>// checkUnderBookedCancellable<br>// cancelClass<br>// collectBookedMembers | 720 | 40 | 240 | 330 |
| AC-E-Waitlist | AC-E-Waitlist | Class | Waitlist | «entity» | Entity | - | // addMember | 720 | 460 | 240 | 90 |
| AC-E-MembershipPackage | AC-E-MembershipPackage | Class | MembershipPackage | «entity» | Entity | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>startDate (Ngày)<br>expiryDate (Ngày)<br>status (Trạng thái) | // calculateRenewalStartDate<br>// initializePackage<br>// checkEntryEligibility | 380 | 620 | 240 | 230 |
| AC-E-EntryScan | AC-E-EntryScan | Class | EntryScan | «entity» | Entity | scanTime (Ngày, Giờ)<br>branch (Văn bản) | // createEntryScan | 40 | 620 | 240 | 110 |
| AC-E-PackagePrice | AC-E-PackagePrice | Class | PackagePrice | «entity» | Entity | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>price (Số tiền) | // getPriceInfo<br>// calculateAmountDue | 40 | 920 | 240 | 170 |
| AC-E-Promotion | AC-E-Promotion | Class | Promotion | «entity» | Entity | validFrom (Ngày)<br>validTo (Ngày)<br>discountRate (Số lượng, tối đa 20% theo BR-38) | // determineApplicableDiscount | 380 | 920 | 240 | 130 |
| AC-E-DayPass | AC-E-DayPass | Class | DayPass | «entity» | Entity | qrCode (Văn bản)<br>purchaseDate (Ngày)<br>purchaseBranch (Văn bản) | // matchesQrCode<br>// checkUsableToday<br>// checkUsableAtBranch | 720 | 920 | 240 | 170 |
| AC-B-PurchaseOrRenewPackageUI | AC-B-PurchaseOrRenewPackageUI__V2 | Class | PurchaseOrRenewPackageUI | «boundary» | Gói tập | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew | // requestPurchaseOrRenewal<br>// showPackageOptions<br>// selectPackage<br>// showOrderSummary<br>// confirmPurchase<br>// showOrderCancelledNotice<br>// showPaymentFailedNotice<br>// showActivatedPackage | 330 | 40 | 300 | 290 |
| AC-B-SellPackageUI | AC-B-SellPackageUI__V2 | Class | SellPackageUI | «boundary» | Gói tập | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew<br>buyer<br>posTransactionCode | // requestPackageSale<br>// showPackageOptions<br>// selectPackage<br>// showOrderSummary<br>// confirmSale<br>// confirmCashCollected<br>// enterPosTransactionCode<br>// showActivatedPackage | 690 | 40 | 300 | 330 |
| AC-B-PaymentGateway | AC-B-PaymentGateway__V2 | Class | PaymentGateway | «boundary» | Gói tập | - | // requestPayment<br>// returnPaymentResult | 1050 | 40 | 240 | 110 |
| AC-B-EInvoiceGateway | AC-B-EInvoiceGateway__V2 | Class | EInvoiceGateway | «boundary» | Gói tập | - | // sendTransactionData | 1350 | 40 | 240 | 90 |
| AC-C-PurchaseOrRenewPackageHandler | AC-C-PurchaseOrRenewPackageHandler__V2 | Class | PurchaseOrRenewPackageHandler | «control» | Gói tập | - | // startPurchase<br>// processPackageSelection<br>// placeOrder<br>// startWaitingForPayment<br>// handlePaymentTimeout<br>// stopWaitingForPayment<br>// handlePaymentResult<br>// confirmCashPayment<br>// confirmPosPayment | 810 | 500 | 300 | 250 |
| AC-E-PackagePrice | AC-E-PackagePrice__V2 | Class | PackagePrice | «entity» | Gói tập | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>price (Số tiền) | // getPriceInfo<br>// calculateAmountDue | 40 | 900 | 240 | 170 |
| AC-E-Promotion | AC-E-Promotion__V2 | Class | Promotion | «entity» | Gói tập | validFrom (Ngày)<br>validTo (Ngày)<br>discountRate (Số lượng, tối đa 20% theo BR-38) | // determineApplicableDiscount | 360 | 900 | 240 | 130 |
| AC-E-MembershipPackage | AC-E-MembershipPackage__V2 | Class | MembershipPackage | «entity» | Gói tập | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>startDate (Ngày)<br>expiryDate (Ngày)<br>status (Trạng thái) | // calculateRenewalStartDate<br>// initializePackage<br>// checkEntryEligibility | 680 | 900 | 240 | 230 |
| AC-E-Member | AC-E-Member__V2 | Class | Member | «entity» | Gói tập | bookingSuspension (Trạng thái)<br>qrCode (Văn bản) | // activatePackage<br>// checkBookingNotSuspended<br>// checkDailyBookingLimit<br>// determineNotificationChannel<br>// matchesQrCode<br>// checkPackageEligibility<br>// recordEntryScan | 1000 | 900 | 240 | 230 |
| AC-E-PackageOrder | AC-E-PackageOrder__V2 | Class | PackageOrder | «entity» | Gói tập | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>startDate (Ngày)<br>amountDue (Số tiền)<br>status (Trạng thái) | // createOrder<br>// cancelUnpaidOrder<br>// recordPayment | 1320 | 900 | 240 | 230 |
| AC-E-PaymentTransaction | AC-E-PaymentTransaction__V2 | Class | PaymentTransaction | «entity» | Gói tập | paymentMethod (Trạng thái)<br>amount (Số tiền)<br>posTransactionCode (Văn bản) | // createTransaction<br>// prepareInvoiceData | 1640 | 900 | 240 | 150 |
| AC-B-BookClassSpotUI | AC-B-BookClassSpotUI__V3 | Class | BookClassSpotUI | «boundary» | Lớp nhóm | selectedClass | // requestBookClass<br>// showClassSchedule<br>// selectClass<br>// showBookingRejectedNotice<br>// showClassFullNotice<br>// requestJoinWaitlist<br>// showWaitlistPosition<br>// showBookedSpot | 70 | 40 | 240 | 230 |
| AC-B-PushNotificationGateway | AC-B-PushNotificationGateway__V3 | Class | PushNotificationGateway | «boundary» | Lớp nhóm | - | // sendPushNotification | 560 | 40 | 260 | 90 |
| AC-B-SmsGateway | AC-B-SmsGateway__V3 | Class | SmsGateway | «boundary» | Lớp nhóm | - | // sendSms | 880 | 40 | 260 | 90 |
| AC-C-BookClassSpotHandler | AC-C-BookClassSpotHandler__V3 | Class | BookClassSpotHandler | «control» | Lớp nhóm | - | // startBooking<br>// bookClass<br>// joinWaitlist | 40 | 400 | 300 | 130 |
| AC-C-CancelUnderBookedClassHandler | AC-C-CancelUnderBookedClassHandler__V3 | Class | CancelUnderBookedClassHandler | «control» | Lớp nhóm | - | // handleClassCutoff<br>// cancelAbsenceMark<br>// cancelWaitlistTransferMark | 650 | 400 | 300 | 130 |
| AC-E-Member | AC-E-Member__V3 | Class | Member | «entity» | Lớp nhóm | bookingSuspension (Trạng thái)<br>qrCode (Văn bản) | // activatePackage<br>// checkBookingNotSuspended<br>// checkDailyBookingLimit<br>// determineNotificationChannel<br>// matchesQrCode<br>// checkPackageEligibility<br>// recordEntryScan | 40 | 680 | 240 | 230 |
| AC-E-ClassBooking | AC-E-ClassBooking__V3 | Class | ClassBooking | «entity» | Lớp nhóm | - | // initializeBooking<br>// provideBookedMember | 360 | 680 | 240 | 110 |
| AC-E-GroupClass | AC-E-GroupClass__V3 | Class | GroupClass | «entity» | Lớp nhóm | classType (Văn bản)<br>room (Văn bản)<br>trainer (Văn bản)<br>startTime (Ngày, Giờ)<br>capacity (Số lượng)<br>status (Trạng thái) | // provideClassInfo<br>// checkBookable<br>// checkSpotAvailable<br>// reserveSpot<br>// addToWaitlist<br>// checkUnderBookedCancellable<br>// cancelClass<br>// collectBookedMembers | 680 | 680 | 240 | 330 |
| AC-E-Waitlist | AC-E-Waitlist__V3 | Class | Waitlist | «entity» | Lớp nhóm | - | // addMember | 1000 | 680 | 240 | 90 |
| AC-B-TurnstileDevice | AC-B-TurnstileDevice__V4 | Class | TurnstileDevice | «boundary» | Ra vào chi nhánh | scannedQrCode (Văn bản)<br>turnstileBranch (Văn bản)<br>scanTime (Ngày, Giờ) | // scanQrCode<br>// receiveScannedCode<br>// sendEntryResult<br>// openDoor | 320 | 40 | 260 | 190 |
| AC-C-EnterBranchHandler | AC-C-EnterBranchHandler__V4 | Class | EnterBranchHandler | «control» | Ra vào chi nhánh | - | // handleEntryRequest<br>// handleDayPassEntry | 300 | 360 | 300 | 110 |
| AC-E-DayPass | AC-E-DayPass__V4 | Class | DayPass | «entity» | Ra vào chi nhánh | qrCode (Văn bản)<br>purchaseDate (Ngày)<br>purchaseBranch (Văn bản) | // matchesQrCode<br>// checkUsableToday<br>// checkUsableAtBranch | 40 | 600 | 240 | 170 |
| AC-E-EntryScan | AC-E-EntryScan__V4 | Class | EntryScan | «entity» | Ra vào chi nhánh | scanTime (Ngày, Giờ)<br>branch (Văn bản) | // createEntryScan | 360 | 600 | 240 | 110 |
| AC-E-Member | AC-E-Member__V4 | Class | Member | «entity» | Ra vào chi nhánh | bookingSuspension (Trạng thái)<br>qrCode (Văn bản) | // activatePackage<br>// checkBookingNotSuspended<br>// checkDailyBookingLimit<br>// determineNotificationChannel<br>// matchesQrCode<br>// checkPackageEligibility<br>// recordEntryScan | 680 | 600 | 240 | 230 |
| AC-E-MembershipPackage | AC-E-MembershipPackage__V4 | Class | MembershipPackage | «entity» | Ra vào chi nhánh | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản)<br>startDate (Ngày)<br>expiryDate (Ngày)<br>status (Trạng thái) | // calculateRenewalStartDate<br>// initializePackage<br>// checkEntryEligibility | 1000 | 600 | 240 | 230 |

### b) Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Thuộc về (view) | Điểm uốn |
|---|---|---|---|---|---|---|
| R-11 | AC-E-PackageOrder | AC-E-PaymentTransaction | Association | đầu nguồn: ?; đầu đích: ? | Entity | - |
| R-12 | AC-E-Member | AC-E-MembershipPackage | Association | đầu nguồn: 1; đầu đích: ? | Entity | - |
| R-13 | AC-E-PackageOrder | AC-E-Member | Association | đầu nguồn: 0..*; đầu đích: ? | Entity | - |
| R-17 | AC-E-GroupClass | AC-E-ClassBooking | Association | đầu nguồn: 1; đầu đích: ? | Entity | - |
| R-18 | AC-E-GroupClass | AC-E-Waitlist | Association | đầu nguồn: 1; đầu đích: ? | Entity | - |
| R-19 | AC-E-Member | AC-E-ClassBooking | Association | đầu nguồn: 1; đầu đích: ? | Entity | - |
| R-20 | AC-E-Waitlist | AC-E-Member | Association | đầu nguồn: ?; đầu đích: ? | Entity | - |
| R-28 | AC-E-Member | AC-E-EntryScan | Association | đầu nguồn: 1; đầu đích: ? | Entity | (420,570); (160,570) |
| R-01__V2 | AC-B-PurchaseOrRenewPackageUI | AC-C-PurchaseOrRenewPackageHandler | Association | - | Gói tập | (480,420); (850,420) |
| R-02__V2 | AC-B-SellPackageUI | AC-C-PurchaseOrRenewPackageHandler | Association | - | Gói tập | (840,410); (920,410) |
| R-07__V2 | AC-B-PaymentGateway | AC-C-PurchaseOrRenewPackageHandler | Association | - | Gói tập | (1170,410); (990,410) |
| R-10__V2 | AC-B-EInvoiceGateway | AC-C-PurchaseOrRenewPackageHandler | Association | - | Gói tập | (1470,420); (1060,420) |
| R-04__V2 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackagePrice | Association | - | Gói tập | (830,780); (160,780) |
| R-05__V2 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Promotion | Association | - | Gói tập | (880,790); (480,790) |
| R-06__V2 | AC-C-PurchaseOrRenewPackageHandler | AC-E-MembershipPackage | Association | - | Gói tập | (930,800); (800,800) |
| R-08__V2 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Member | Association | - | Gói tập | (980,800); (1120,800) |
| R-03__V2 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackageOrder | Association | - | Gói tập | (1030,790); (1440,790) |
| R-09__V2 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PaymentTransaction | Association | - | Gói tập | (1080,780); (1760,780) |
| R-12__V2 | AC-E-Member | AC-E-MembershipPackage | Association | đầu nguồn: 1; đầu đích: ? | Gói tập | - |
| R-13__V2 | AC-E-PackageOrder | AC-E-Member | Association | đầu nguồn: 0..*; đầu đích: ? | Gói tập | - |
| R-11__V2 | AC-E-PackageOrder | AC-E-PaymentTransaction | Association | đầu nguồn: ?; đầu đích: ? | Gói tập | - |
| R-14__V3 | AC-B-BookClassSpotUI | AC-C-BookClassSpotHandler | Association | - | Lớp nhóm | - |
| R-23__V3 | AC-B-PushNotificationGateway | AC-C-CancelUnderBookedClassHandler | Association | - | Lớp nhóm | - |
| R-24__V3 | AC-B-SmsGateway | AC-C-CancelUnderBookedClassHandler | Association | - | Lớp nhóm | (1010,330); (900,330) |
| R-15__V3 | AC-C-BookClassSpotHandler | AC-E-Member | Association | - | Lớp nhóm | - |
| R-16__V3 | AC-C-BookClassSpotHandler | AC-E-GroupClass | Association | - | Lớp nhóm | (300,570); (740,570) |
| R-21__V3 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | Association | - | Lớp nhóm | - |
| R-22__V3 | AC-C-CancelUnderBookedClassHandler | AC-E-Member | Association | - | Lớp nhóm | (700,590); (220,590) |
| R-19__V3 | AC-E-Member | AC-E-ClassBooking | Association | đầu nguồn: 1; đầu đích: ? | Lớp nhóm | - |
| R-17__V3 | AC-E-GroupClass | AC-E-ClassBooking | Association | đầu nguồn: 1; đầu đích: ? | Lớp nhóm | - |
| R-18__V3 | AC-E-GroupClass | AC-E-Waitlist | Association | đầu nguồn: 1; đầu đích: ? | Lớp nhóm | - |
| R-20__V3 | AC-E-Waitlist | AC-E-Member | Association | đầu nguồn: ?; đầu đích: ? | Lớp nhóm | (1120,1050); (160,1050) |
| R-25__V4 | AC-B-TurnstileDevice | AC-C-EnterBranchHandler | Association | - | Ra vào chi nhánh | - |
| R-27__V4 | AC-C-EnterBranchHandler | AC-E-DayPass | Association | - | Ra vào chi nhánh | (340,530); (160,530) |
| R-26__V4 | AC-C-EnterBranchHandler | AC-E-Member | Association | - | Ra vào chi nhánh | (560,530); (760,530) |
| R-28__V4 | AC-E-Member | AC-E-EntryScan | Association | đầu nguồn: 1; đầu đích: ? | Ra vào chi nhánh | - |
| R-12__V4 | AC-E-Member | AC-E-MembershipPackage | Association | đầu nguồn: 1; đầu đích: ? | Ra vào chi nhánh | - |

## F6. Rà soát lớp phân tích

| AC | Tên phản ánh đúng vai trò | Một khái niệm duy nhất | Trách nhiệm gắn kết | Cung cấp đủ hành vi cần | Yêu cầu đặc thù (BR, NFR) đã gắn | Ghi chú |
|---|---|---|---|---|---|---|
| AC-B-PurchaseOrRenewPackageUI | Đạt: giao diện mua hoặc gia hạn của hội viên | Đạt: một giao diện của ACT-02 | Đạt: nhận, hiển thị | Đạt: đủ bước 1-13 phía hội viên | Đạt: BR-01, BR-02 (thời hạn, loại bắt buộc chọn) | Kênh thông báo chờ Q-53 |
| AC-B-SellPackageUI | Đạt: giao diện bán gói của lễ tân | Đạt: một giao diện của ACT-05 | Đạt: nhận, hiển thị | Đạt: có thêm 8a, 8b | Đạt: NFR-08 (mã POS nhập tay) | Kiểm tra trùng mã POS chờ Q-55 |
| AC-B-PaymentGateway | Đạt: cổng thanh toán (ACT-08) | Đạt | Đạt: gửi đơn, nhận kết quả | Đạt | Đạt: NFR-07 | Q-45, Q-77 |
| AC-B-EInvoiceGateway | Đạt: hệ thống hoá đơn điện tử (ACT-11) | Đạt | Đạt: chỉ gửi dữ liệu | Đạt | Đạt: BR-05, NFR-05, NFR-12 | Q-39, Q-54 |
| AC-C-PurchaseOrRenewPackageHandler | Đạt: điều phối UC-005 | Đạt: một use case | Đạt: 9 trách nhiệm, dưới 15 | Đạt | Đạt: BR-03, BR-04, BR-05 | - |
| AC-E-MembershipPackage | Đạt: GL-16 | Đạt | Đạt: ngày bắt đầu, hết hạn, kiểm tra vào cửa | Đạt: đủ cho UC-005, UC-018 | Đạt: BR-01, BR-02, BR-03, BR-15, BR-16, BR-17 | Q-74, Q-75; bảo lưu (UC-006) chưa có |
| AC-E-Member | Đạt: GL-19 | Đạt | Đạt, cần theo dõi: 7 trách nhiệm thuộc 4 ngữ cảnh (gói, đặt lớp, thông báo, vào cửa), xem lại khi thêm use case | - | Đạt: BR-08, BR-09, BR-14, BR-15, BR-16, BR-17 | Tạm (UC-003) |
| AC-E-PackageOrder | Đạt: GL-09 | Đạt | Đạt | Đạt | Đạt: BR-04 | Q-25, Q-57, Q-87 |
| AC-E-PaymentTransaction | Đạt: GL-12 | Đạt | Đạt: ghi nhận, cung cấp dữ liệu hoá đơn | Đạt | Đạt: BR-05 | Q-81 (giao dịch không thành công) |
| AC-E-PackagePrice | Đạt: GL-10 | Đạt | Không đạt: // calculateAmountDue dùng mức giảm của AC-E-Promotion trong khi hai lớp không có quan hệ (Q-08, Q-09, Q-10) | - | Đạt: BR-01, BR-02 | Tạm (UC-026); hành động ở Vấn đề còn mở |
| AC-E-Promotion | Đạt: GL-07 | Đạt | Đạt | - | Đạt: BR-38 | Tạm (UC-027) |
| AC-B-BookClassSpotUI | Đạt: giao diện đặt chỗ lớp nhóm của hội viên | Đạt | Đạt | Đạt | Đạt: BR-12 (lớp đủ chỗ, đề nghị vào danh sách chờ) | Phạm vi lịch hiển thị chờ Q-83 |
| AC-C-BookClassSpotHandler | Đạt: điều phối UC-010 | Đạt | Đạt: 3 trách nhiệm | Đạt | Đạt: BR-06 đến BR-12, NFR-01 (cơ chế thuộc P09, P12) | BR-06 mâu thuẫn BR-07 (Q-11) |
| AC-B-PushNotificationGateway | Đạt: dịch vụ thông báo đẩy (ACT-10) | Đạt | Đạt | Đạt | Đạt: BR-14, NFR-10 | Q-65, Q-79 |
| AC-B-SmsGateway | Đạt: cổng SMS (ACT-09) | Đạt | Đạt | Đạt | Đạt: BR-14, NFR-11 | Q-65, Q-79 |
| AC-C-CancelUnderBookedClassHandler | Đạt: điều phối UC-015 | Đạt | Đạt: 3 trách nhiệm | Đạt | Đạt: BR-13, BR-14 | Q-64 |
| AC-E-GroupClass | Đạt: GL-29 | Đạt | Đạt: 8 trách nhiệm quanh việc đặt, đếm, huỷ lớp | - | Đạt: BR-06, BR-07, BR-10, BR-11, BR-12, BR-13 | Tạm (UC-009); room, trainer, classType là thuộc tính tạm |
| AC-E-ClassBooking | Đạt: GL-05 | Đạt | Đạt | Đạt: khởi tạo, cung cấp hội viên | Đạt: BR-08, BR-11 (đếm qua R-17, R-19) | Entity mỏng, UC-011, UC-012, UC-016 sẽ bổ sung |
| AC-E-Waitlist | Đạt: GL-08 | Đạt, Q-84 hỏi có là đối tượng riêng không | Đạt | Đạt: thêm hội viên (UC-010) | Đạt: BR-12 | Q-61, Q-62, Q-84 |
| AC-B-TurnstileDevice | Đạt: cửa quay (ACT-12) | Đạt: một thiết bị | Đạt | Đạt | Đạt: NFR-02, NFR-09 | Q-67, Q-70 |
| AC-C-EnterBranchHandler | Đạt: điều phối UC-018 | Đạt | Đạt: 2 trách nhiệm | Đạt | Đạt: BR-15 đến BR-19, NFR-02 | Q-72 |
| AC-E-EntryScan | Đạt: GL-30 | Đạt | Đạt | Đạt: khởi tạo; xác định vắng mặt thuộc UC-016 | Đạt: BR-20 sẽ gắn khi có UC-016 | Q-71, Q-86 |
| AC-E-DayPass | Đạt: GL-42 | Đạt | Đạt | - | Đạt: BR-18, BR-19 | Tạm (UC-017) |

## F7. Mục kiểm soát

Gồm bốn mục Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở ngay dưới đây.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-87 | Mỗi gói tập của hội viên có được tạo ra từ một đơn mua cụ thể và hệ thống có cần lưu liên kết giữa đơn mua với gói tập đó không, hay đơn mua chỉ ghi nhận thời hạn, loại, chi nhánh, ngày bắt đầu đã mua mà không liên kết tới gói tập? (Có liên kết, mỗi đơn đã thanh toán tạo đúng một gói tập / Không liên kết, đơn chỉ ghi nhận nội dung mua / Khác - nêu rõ) | Quan hệ giữa AC-E-PackageOrder và AC-E-MembershipPackage (chưa có ở F4); thuộc tính trùng durationMonths, packageType, appliedBranch ở AC-E-PackageOrder, AC-E-MembershipPackage, AC-E-PackagePrice; F2a dòng 3, 4, 5 | GL-09 "Chứng từ ghi nhận việc một người mua hoặc gia hạn một gói tập" và UC-005 bước 11 (kích hoạt gói tập sau khi ghi nhận đơn đã thanh toán) không nêu có lưu liên kết giữa đơn và gói tập được tạo; liên quan Q-82 |

Các câu hỏi đã cấp ở bước trước và làm đổi mô hình này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-01 (người mua tại quầy có phải hội viên, R-13); Q-03, Q-50 (danh mục chi nhánh, chi nhánh áp dụng, thuộc tính chi nhánh); Q-07, Q-38 (giao dịch thu tiền của use case khác, R-11); Q-08, Q-09, Q-10 (phạm vi, cách áp dụng giá và khuyến mãi, F6 của PackagePrice); Q-13, Q-81 (số giao dịch của một đơn, R-11); Q-20, Q-22, Q-59, Q-60 (số chỗ đã đặt, R-17, R-19); Q-36, Q-53, Q-65, Q-79 (kênh thông báo); Q-61, Q-62, Q-84 (danh sách chờ, R-18, R-20); Q-69 (số gói của một hội viên, R-12); Q-74, Q-75 (ngày hết hạn, trạng thái gói); Q-82 (mặt hàng được bán là Giá gói hay danh mục gói); Q-83 (phạm vi lịch lớp nhóm); Q-86 (số lượt quẹt của một hội viên, R-28).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P07 | UC-005, R-UC005-11 (AC-E-PackageOrder - AC-E-PaymentTransaction) | Multiplicity "A 1 - B ?" ghi mỗi giao dịch thu tiền thuộc đúng một đơn. GL-12 gồm cả giao dịch của UC-007, UC-017, UC-019, còn GL-09 chưa nói các khoản đó có đơn hay không (Q-07, Q-38), nên phía "1" chưa có bằng chứng trên toàn hệ thống | Đổi phía A của R-UC005-11 thành "?" kèm Q-07, Q-38, hoặc giữ "1" nếu Q-07 và Q-38 trả lời mọi giao dịch thu tiền đều thuộc một đơn; chưa áp dụng, cùng nhóm với các đề xuất chờ câu trả lời |

## Vấn đề còn mở

Các mục Target đạt, trừ mục 1 (đạt một phần), với các điểm cần người dùng lưu ý:

- Target 1: 24 use case của P02 chưa có P07 (UC-001, UC-002, UC-003, UC-004, UC-006, UC-007, UC-008, UC-009, UC-011, UC-012, UC-013, UC-014, UC-016, UC-017, UC-019 đến UC-028). Mô hình mới hợp nhất bốn use case có P07. Khi thêm use case, chạy lại P08 với phiên bản tăng lên.
- Lớp Tạm: AC-E-Member (UC-003), AC-E-PackagePrice (UC-026), AC-E-Promotion (UC-027), AC-E-GroupClass (UC-009), AC-E-DayPass (UC-017). Trách nhiệm chỉ gồm những gì bốn use case trong phạm vi cần; chạy lại P08 sau P07 của các use case đó để chuyển sang Hoạt động. AC-E-Member chưa có thuộc tính định danh (số điện thoại, họ tên theo GL-19) vì chưa use case nào trong phạm vi dùng.
- Chi nhánh: P07 UC-005 chuyển cho P08 quyết định có entity Branch hay không. P08 không tạo lớp mới ngoài các lớp P07 đã đặt mã, giữ chi nhánh dạng thuộc tính văn bản (appliedBranch, branch, purchaseBranch, turnstileBranch) vì chưa có thuộc tính hay hành vi riêng của chi nhánh trong bốn use case (Q-03, Q-50). Nên xem lại khi có P07 của UC-009 (phòng thuộc chi nhánh) và UC-006, UC-007.
- Phòng, huấn luyện viên, loại lớp: P07 UC-010 chuyển cho P08 quyết định tách entity Room, Trainer, ClassType. P08 giữ room, trainer, classType là thuộc tính của GroupClass vì chỉ được hiển thị hoặc so sánh (GL-27, GL-35, GL-21); xem lại khi có P07 của UC-009 (Q-03, Q-04, Q-05).
- F6 Không đạt: AC-E-PackagePrice // calculateAmountDue cần mức giảm của Promotion nhưng hai lớp không có quan hệ. P08 không thêm quan hệ vì Q-08, Q-09, Q-10 chưa trả lời (cách áp dụng khuyến mãi, hiệu lực theo khoảng ngày). Khi có câu trả lời: thêm quan hệ giữa hai entity hoặc chuyển phép tính sang control của UC-005.
- Quan hệ giữa AC-E-PackageOrder với AC-E-MembershipPackage và AC-E-PackagePrice chưa thêm vì chưa chốt đơn mua trỏ tới lớp nào (Q-82, Q-87). Nếu Q-82 trả lời có danh mục gói riêng thì cần lớp mới và chạy lại P07 UC-005 rồi P08.
- Đề xuất của P07 chưa áp dụng (UC-005 chờ Q-82, UC-010 chờ Q-83) không làm đổi mô hình này; P08 không lặp lại chúng ở mục Đề xuất sửa artifact trước.
- Tên boundary AC-B-PushNotificationGateway, AC-B-SmsGateway giữ theo P07 (C1 mục 3) dù hồ sơ dự án cho "boundary kênh thông báo" hậu tố theo tên kênh (PushNotifier, SmsNotifier): P07 UC-015 đã chọn hậu tố Gateway cho hệ thống ngoài. Nếu muốn đổi cần sửa P07 UC-015 rồi chạy lại P08. Khi Q-53 chọn thông báo đẩy hoặc SMS cho UC-005 (luồng 9a2, 10a), UC-005 dùng lại hai boundary này; hai boundary còn được UC-008, UC-011, UC-014 dùng.
- AC-E-Member có 7 trách nhiệm thuộc 4 ngữ cảnh (F6 ghi cần theo dõi); xem lại khi thêm UC-006, UC-016, UC-020 để quyết định có tách entity hay không. AC-E-ClassBooking, AC-E-Waitlist, AC-E-EntryScan mỏng (1 đến 2 trách nhiệm) vì hành vi huỷ, chuyển chỗ, xác định vắng mặt thuộc UC-011, UC-012, UC-013, UC-016.
- Đồ thị: R-16 và R-22 giao nhau một điểm ở trang Lớp nhóm (hai control cùng nối tới hai entity), không cạnh nào cắt qua node.
- Chọn giữa hai quy tắc (C9): prompt đặt phạm vi là mọi use case trong P02, YEU_CAU_BO_SUNG giới hạn bốn use case; theo YEU_CAU_BO_SUNG (ưu tiên 2 so với quy tắc bước ưu tiên 4). Lớp chủ sở hữu ở use case chưa phân tích ghi "Tạm" theo F3 của prompt dù P07 ghi "Mới - chủ sở hữu UC-nnn".
- Cách áp dụng YEU_CAU_BO_SUNG: REQ do P04 đề nghị thêm vào P02 không ảnh hưởng mô hình lớp nên P08 không dùng; các đề xuất đổi cách gọi của P05 chưa áp dụng nên mô hình dùng thuật ngữ chuẩn của P05 (lớp nhóm, giờ học, giao dịch thu tiền) trong mô tả.
