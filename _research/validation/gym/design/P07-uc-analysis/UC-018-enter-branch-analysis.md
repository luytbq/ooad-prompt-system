# P07 - Phân tích use case UC-018 Vào chi nhánh - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-018-enter-branch.md (phiên bản 1.0; toàn bộ); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; dòng UC-018 ở bảng 4a, 4b; các dòng UC có tác nhân thời gian UC-008, UC-013, UC-015, UC-016, UC-022); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2); P05-glossary.md (phiên bản 1.0; GL-01, GL-03, GL-13, GL-16, GL-17, GL-19, GL-22, GL-30, GL-32, GL-41, GL-42, mục Câu hỏi mở, Đề xuất sửa artifact trước); P06-supplementary-spec.md (phiên bản 1.0; BR-15 đến BR-20, BR-29, NFR-02, NFR-09, mục Câu hỏi mở); P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md, UC-010-book-class-spot-analysis.md, UC-015-cancel-under-booked-class-analysis.md (phiên bản 1.0; F1, F3.4, F8 b), Câu hỏi mở, Giả định, Vấn đề còn mở); mã Q, ASM quét ở mục Câu hỏi mở, Giả định của mọi artifact trong thư mục đầu ra (Q lớn nhất trước lần chạy: Q-85; chưa có ASM). UC_ID: UC-018 Vào chi nhánh. LUONG_CAN_VE: Không có. YEU_CAU_BO_SUNG: đề xuất sửa artifact trước của P04, P05, P06 chưa áp dụng và các bước đó không chạy lại; REQ-10, REQ-43, REQ-46, REQ-51 mà đặc tả P04 đề nghị thêm vào cột REQ của P02 chỉ là dữ liệu do use case khác cung cấp; hiển thị mã QR (CAND-34) là tiền điều kiện của UC-018 theo phương án (a) của đặc tả; các đề xuất đổi cách gọi của P05 chưa áp dụng vào P00 đến P04, dùng thuật ngữ chuẩn của P05; ghi chú "chưa có BR" ở P05 nay đã có mã BR ở P06 |
| Phạm vi | UC-018 |
| Mã Q, ASM cuối đã cấp | Q-86; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-018 Vào chi nhánh (Enter Branch) |
| Tác nhân chính (ACT, loại) | ACT-02 Hội viên (Người); ACT-03 Khách vãng lai (Người) |
| Tác nhân phụ (ACT, loại) | ACT-12 Cửa quay (Thiết bị) |
| Include (UC) | Không có |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2: không có điểm mở rộng) |
| File P07 đã có được dùng làm sổ đăng ký AC | P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md, UC-010-book-class-spot-analysis.md, UC-015-cancel-under-booked-class-analysis.md (phiên bản 1.0). Sổ gồm AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI, AC-B-PaymentGateway, AC-B-EInvoiceGateway, AC-C-PurchaseOrRenewPackageHandler, AC-E-MembershipPackage, AC-E-Member, AC-E-PackageOrder, AC-E-PaymentTransaction, AC-E-PackagePrice, AC-E-Promotion (UC-005); AC-B-BookClassSpotUI, AC-C-BookClassSpotHandler, AC-E-GroupClass, AC-E-ClassBooking, AC-E-Waitlist (UC-010); AC-B-PushNotificationGateway, AC-B-SmsGateway, AC-C-CancelUnderBookedClassHandler (UC-015). Use case này tái dùng AC-E-Member và AC-E-MembershipPackage; các khái niệm còn lại của sổ không tham gia hành vi của UC-018 |
| Mốc thời gian phụ thuộc dữ liệu (A2) | Không có message hẹn, hẹn lại hoặc huỷ mốc. UC-016 (ACT-14) kích hoạt 10 phút sau giờ học của lớp nhóm; đối tượng mốc là lớp nhóm (giờ học), UC-018 không tạo, đổi hay làm mất hiệu lực lớp nhóm. Lượt quẹt (AC-E-EntryScan) mà UC-018 tạo chỉ là dữ liệu UC-016 đọc khi mốc tới, không chứa giá trị dùng để tính mốc. UC-008 (ACT-13) chạy theo lịch cố định hằng ngày và tự đọc ngày hết hạn của gói, UC-018 không đổi ngày hết hạn; UC-013, UC-015, UC-022 (ACT-14) gắn với thông báo nhận chỗ, lớp nhóm, yêu cầu đặt buổi tập cá nhân, không liên quan tới lượt quẹt hay vé. Khớp với P04 mục 8 |
| Tiền điều kiện ngoài luồng | Hiển thị mã QR trên ứng dụng (CAND-34) là tiền điều kiện của hội viên theo phương án (a), không là bước của use case này; vé tập một ngày có mã QR do UC-017 tạo (REQ-43) |

## F2. Đặc tả bổ sung

Hàng 3a, 3a1c là hàng điều kiện của đặc tả nên cột Thực hiện bởi ghi "-"; cột Mô tả trong đặc tả ghi điều kiện rồi hành động. REQ-10 (BR-17), REQ-43 (mã QR trên vé), REQ-46 và REQ-51 (BR-29, ngày hết hạn lùi theo bảo lưu) chỉ là dữ liệu do UC-005, UC-026, UC-017, UC-006 cung cấp.

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Hội viên / Khách vãng lai | Quét mã QR tại đầu đọc của cửa quay. | Không đổi | REQ-39, REQ-44; GL-32 |
| 2 | Cửa quay | Gửi mã QR đọc được và chi nhánh của cửa quay tới phần mềm (xem Dữ liệu vào 1). | Không đổi | REQ-40, NFR-09; Q-67 |
| 3 | Phần mềm VietFit | Kiểm tra mã QR là mã của một hội viên. | Hệ thống đối chiếu mã QR đọc được với mã QR của từng hội viên cho đến khi gặp hội viên có mã khớp. Hội viên khớp được dùng cho bước 4 và 5. Không có hội viên khớp thì chuyển sang luồng 3a hoặc 3b; cách tạo và thời hạn của mã QR hội viên chờ Q-68. | REQ-39; GL-19, GL-32; Q-68 |
| 3a | - | Mã QR là mã trên vé tập một ngày, không phải mã của hội viên: Khách vãng lai vào bằng vé tập một ngày. | Hệ thống đối chiếu mã QR đọc được với mã QR in trên từng vé tập một ngày cho đến khi gặp vé có mã khớp. Vé do UC-017 Bán vé tập một ngày tạo, use case này chỉ đọc vé. | REQ-44, REQ-45, REQ-43 (do UC-017 cung cấp); GL-42, GL-32 |
| 3a1 | Phần mềm VietFit | Kiểm tra vé dùng được trong ngày mua vé và tại chi nhánh đã mua (BR-18, BR-19). Tiếp tục bước 6. | Hệ thống kiểm tra ngày hiện tại là ngày mua vé ghi trên vé (BR-18), rồi kiểm tra chi nhánh của cửa quay là chi nhánh đã mua vé (BR-19). Vé đạt cả hai kiểm tra thì tiếp tục bước 6; số lần dùng vé trong ngày chờ Q-40. | BR-18, BR-19; GL-42; Q-40 |
| 3a1a | Phần mềm VietFit | Điều kiện: hôm nay không phải ngày mua vé (BR-18). Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-18) cho cửa quay; cách báo cho người quét chờ Q-70. Kết thúc use case (thất bại). | Hệ thống tạo kết quả không cho phép kèm quy tắc bị vi phạm BR-18 và gửi cho cửa quay; cửa quay không mở. Cách báo cho người quét chờ Q-70. | BR-18; Q-70 |
| 3a1b | Phần mềm VietFit | Điều kiện: hôm nay là ngày mua vé và vé được mua ở chi nhánh khác chi nhánh của cửa quay (BR-19). Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-19) cho cửa quay; cách báo cho người quét chờ Q-70. Kết thúc use case (thất bại). | Hệ thống tạo kết quả không cho phép kèm quy tắc bị vi phạm BR-19 và gửi cho cửa quay; cửa quay không mở. Cách báo cho người quét chờ Q-70. | BR-19; Q-70 |
| 3a1c | - | Điều kiện: vé đúng ngày, đúng chi nhánh và đã được dùng để vào chi nhánh trước đó trong ngày. Hành động và kết thúc: chờ Q-40. | Đặc tả chưa có hành động (chờ Q-40), nên không có message. | Q-40 |
| 3b | Phần mềm VietFit | Điều kiện: mã QR không phải mã của hội viên và không phải mã trên vé tập một ngày. Từ chối cho vào và thông báo mã QR không hợp lệ (BR-15, BR-18) cho cửa quay; cách báo cho người quét chờ Q-70. Kết thúc use case (thất bại). | Hệ thống tạo kết quả không cho phép kèm lý do mã QR không hợp lệ và gửi cho cửa quay; cửa quay không mở. Cách báo cho người quét chờ Q-70. | BR-15, BR-18; Q-70 |
| 4 | Phần mềm VietFit | Kiểm tra gói tập của hội viên còn hiệu lực, không đang bảo lưu và áp dụng cho chi nhánh của cửa quay (BR-15, BR-16, BR-17). | Hệ thống lấy các gói tập của hội viên đã xác định ở bước 3 và với mỗi gói kiểm tra theo thứ tự: chưa quá ngày hết hạn (BR-15; Q-74), không đang bảo lưu (BR-16), áp dụng cho chi nhánh của cửa quay (BR-17; Q-50). Kết quả cho hội viên được tổng hợp từ kết quả của từng gói; quy tắc tổng hợp khi có nhiều gói chờ Q-69. | BR-15, BR-16, BR-17, BR-29; REQ-41, REQ-10, REQ-46, REQ-51; GL-01, GL-16, GL-17; Q-18, Q-69, Q-74, Q-75 |
| 4a | Phần mềm VietFit | Điều kiện: hội viên không có gói tập còn hiệu lực (BR-15); hội viên chỉ có gói buổi tập cá nhân chờ Q-18, nhiều gói cùng lúc chờ Q-69. Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-15) cho cửa quay; cách báo cho người quét chờ Q-70. Kết thúc use case (thất bại). | Hệ thống tạo kết quả không cho phép kèm quy tắc bị vi phạm BR-15 và gửi cho cửa quay; cửa quay không mở. Cách báo cho người quét chờ Q-70. | BR-15; Q-18, Q-69, Q-70 |
| 4b | Phần mềm VietFit | Điều kiện: hội viên có gói còn hiệu lực và gói đó đang bảo lưu (BR-16). Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-16) cho cửa quay; cách báo cho người quét chờ Q-70. Kết thúc use case (thất bại). | Hệ thống tạo kết quả không cho phép kèm quy tắc bị vi phạm BR-16 và gửi cho cửa quay; cửa quay không mở. Cách báo cho người quét chờ Q-70. | BR-16; Q-70 |
| 4c | Phần mềm VietFit | Điều kiện: gói còn hiệu lực, không đang bảo lưu và không áp dụng cho chi nhánh của cửa quay (BR-17). Từ chối cho vào và thông báo quy tắc bị vi phạm (BR-17) cho cửa quay; cách báo cho người quét chờ Q-70. Kết thúc use case (thất bại). | Hệ thống tạo kết quả không cho phép kèm quy tắc bị vi phạm BR-17 và gửi cho cửa quay; cửa quay không mở. Cách báo cho người quét chờ Q-70. | BR-17; Q-70 |
| 5 | Phần mềm VietFit | Ghi nhận lượt quẹt vào cửa của hội viên tại chi nhánh (BR-20). | Hệ thống tạo lượt quẹt vào cửa gắn với hội viên đã xác định, kèm chi nhánh của cửa quay và thời điểm quẹt, để UC-016 dùng xác định vắng mặt (BR-20). Số lượt ghi cho mỗi hội viên chờ Q-86; lượt bị từ chối và lượt dùng vé chờ Q-71. | BR-20; REQ-35; GL-30, GL-41; Q-71, Q-86 |
| 6 | Phần mềm VietFit | Trả kết quả cho phép vào cho cửa quay (xem Dữ liệu ra 1). | Hệ thống gửi cho cửa quay kết quả "Cho phép", lý do để trống. Bước này cũng là bước tiếp nối của luồng 3a1 khi vé dùng được; thời gian phản hồi 1 giây chờ Q-41. | REQ-40, REQ-96, NFR-02, NFR-09; Q-41, Q-67, Q-72 |
| 7 | Cửa quay | Mở cửa. | Không đổi | REQ-40 |
| 8 | Hội viên / Khách vãng lai | Đi qua cửa quay vào chi nhánh. | Không đổi | REQ-39, REQ-44 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-02 Hội viên | Người | TurnstileDevice (AC-B-TurnstileDevice) | Giao diện thiết bị | Mới | Hội viên chỉ thao tác vật lý trên cửa quay (quét mã, đi qua), không có màn hình của phần mềm trong luồng; thao tác đi vào hệ thống qua boundary thiết bị (F6, ngoại lệ thiết bị). Hiển thị mã QR trên ứng dụng là tiền điều kiện (CAND-34). Không tạo boundary kênh thông báo vì cách báo kết quả cho người quét chưa quy định (Q-70). |
| ACT-03 Khách vãng lai | Người | TurnstileDevice (AC-B-TurnstileDevice) | Giao diện thiết bị | Mới | Cùng lý do với ACT-02: khách chỉ quét mã trên vé và đi qua cửa quay. Hai tác nhân chính dùng chung một boundary vì cùng thao tác trên cùng một cửa quay. |
| ACT-12 Cửa quay | Thiết bị | TurnstileDevice (AC-B-TurnstileDevice) | Giao diện thiết bị | Mới | Đặt tên theo thiết bị, hậu tố Device theo HAU_TO_TEN_LOP. Use case khác giao tiếp với cửa quay (nếu có) dùng lại mã này. Không trùng tên entity nào vì use case không lưu thông tin riêng của cửa quay. |

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Hội viên (người quét mã, người đi qua cửa quay) | Bước 1, 8 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-02; thao tác vật lý đi qua AC-B-TurnstileDevice. |
| 2 | Khách vãng lai | Bước 1, 8; luồng 3a | Loại - là tác nhân hoặc ngoài phạm vi | ACT-03; không có hồ sơ trong use case này (GL-22). |
| 3 | Người quét | Luồng 3a1a, 3a1b, 3b, 4a, 4b, 4c | Loại - là tác nhân hoặc ngoài phạm vi | Chỉ hội viên hoặc khách vãng lai đang quét (ACT-02, ACT-03); cách báo cho người quét chờ Q-70. |
| 4 | Hội viên (hồ sơ có mã QR, các gói tập và các lượt quẹt) | Bước 3, 4, 5; BR-15, BR-16, BR-17, BR-20 | Entity AC-E-Member | Biểu diễn thông tin về hội viên, không phải bản thân tác nhân ACT-02. Hệ thống lưu mã QR, quan hệ với gói tập và lượt quẹt vượt quá một lần thực hiện (GL-19, GL-30). |
| 5 | Mã QR, mã QR đọc được | Bước 1, 2, 3; Dữ liệu vào 1 trường 1 | Loại - dữ liệu trao đổi qua boundary AC-B-TurnstileDevice | Chuỗi do đầu đọc đọc được, không lưu; chỉ để đối chiếu với mã của hội viên và của vé (GL-32); định dạng chờ Q-68. |
| 6 | Mã QR của hội viên | Bước 3; tiền điều kiện | Loại - thuộc tính của Member | qrCode (mới ở UC này); cách tạo và thời hạn chờ Q-68. |
| 7 | Mã QR trên vé | Luồng 3a; BR-18, BR-19 | Loại - thuộc tính của DayPass | qrCode. |
| 8 | Đầu đọc mã QR | Bước 1; Dữ liệu vào 1 | Loại - là tác nhân hoặc ngoài phạm vi | Bộ phận của cửa quay ACT-12 (P01). |
| 9 | Cửa quay | Bước 1, 2, 6, 7; BR-15, BR-16, BR-17 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-12; tương tác qua AC-B-TurnstileDevice. Use case không đọc, ghi hay kiểm tra thông tin riêng của cửa quay (mã cửa quay chờ Q-67) nên không là entity. |
| 10 | Cửa (của cửa quay) | Bước 7 | Loại - là tác nhân hoặc ngoài phạm vi | Bộ phận của cửa quay (ACT-12); mở cửa là hành động của tác nhân. |
| 11 | Chi nhánh của cửa quay | Bước 2; Dữ liệu vào 1 trường 2; BR-17, BR-19 | Loại - dữ liệu trao đổi qua boundary AC-B-TurnstileDevice | Giá trị cửa quay gửi kèm mã QR để so sánh và ghi nhận, không lưu riêng; cách cửa quay cho biết chi nhánh chờ Q-67. |
| 12 | Chi nhánh áp dụng của gói tập | Bước 4; BR-17 | Loại - thuộc tính của MembershipPackage | appliedBranch, chỉ để so sánh; use case không đọc, ghi hay kiểm tra thông tin của chi nhánh (GL-03; Q-03, Q-50). |
| 13 | Chi nhánh đã mua vé | Luồng 3a1; BR-19 | Loại - thuộc tính của DayPass | purchaseBranch (GL-03; Q-03). |
| 14 | Chi nhánh của lượt quẹt | Bước 5; hậu điều kiện | Loại - thuộc tính của EntryScan | branch (GL-30). |
| 15 | Phần mềm VietFit, hệ thống | Bước 3, 4, 5, 6 | Loại - mơ hồ | Chủ thể của use case, không là một lớp; trách nhiệm được phân bổ cho các lớp BCE ở F4. |
| 16 | Gói tập (của hội viên) | Bước 4; BR-15, BR-16, BR-17 | Entity AC-E-MembershipPackage | Quyền vào tập có thời hạn, ngày hết hạn, trạng thái, tồn tại lâu hơn một lần thực hiện; do UC-005 tạo, UC-006 đổi trạng thái (GL-16). |
| 17 | Gói tập còn hiệu lực | Bước 4, luồng 4a; BR-15 | Loại - giá trị suy ra từ MembershipPackage | Tính khi cần từ expiryDate (Q-74, Q-75), không lưu (GL-17). |
| 18 | Ngày hết hạn | Bước 4 (ngầm trong "còn hiệu lực"); BR-15 | Loại - thuộc tính của MembershipPackage | expiryDate; đã được UC-006 lùi theo số ngày bảo lưu (REQ-51, BR-29). |
| 19 | Bảo lưu, gói đang bảo lưu | Bước 4; luồng 4b; BR-16 | Loại - khái niệm do UC-006 tạo, use case này chỉ đọc hoặc đổi trạng thái qua entity MembershipPackage | Use case này chỉ đọc trạng thái đang bảo lưu qua status của gói (GL-01; Q-75). |
| 20 | Gói buổi tập cá nhân | Luồng 4a | Loại - không tham gia hành vi của use case này (khái niệm của UC-019) | Chỉ được nhắc ở điều kiện 4a; có tính là gói tập khi vào chi nhánh hay không chờ Q-18 (GL-14). |
| 21 | Vé tập một ngày, vé | Luồng 3a, 3a1, 3a1c; BR-18, BR-19 | Entity AC-E-DayPass | Chứng từ có mã QR, ngày mua và chi nhánh mua, tồn tại lâu hơn một lần thực hiện (GL-42); do UC-017 tạo. |
| 22 | Ngày mua vé | Luồng 3a1, 3a1a; BR-18 | Loại - thuộc tính của DayPass | purchaseDate. |
| 23 | Hôm nay, trong ngày | Luồng 3a1a; BR-18 | Loại - giá trị suy ra từ thời điểm quẹt | Ngày của thời điểm quẹt, so với purchaseDate khi cần, không lưu. |
| 24 | Lần dùng vé trước đó | Luồng 3a1c; hậu điều kiện | Loại - mơ hồ | Chưa rõ là đối tượng lưu riêng hay thuộc tính của DayPass; chờ Q-40, Q-71. |
| 25 | Lượt quẹt vào cửa | Bước 5; hậu điều kiện; BR-20 | Entity AC-E-EntryScan | Bản ghi gắn hội viên, chi nhánh, thời điểm quẹt, lưu vượt quá một lần thực hiện để UC-016 dùng xác định vắng mặt (GL-30). |
| 26 | Lượt quẹt bị từ chối | Hậu điều kiện tối thiểu | Loại - mơ hồ | Có được ghi nhận hay không chờ Q-71; chưa là entity. |
| 27 | Thời điểm quẹt | Dữ liệu vào 1 trường 3; BR-20 | Loại - thuộc tính của EntryScan | scanTime; nguồn của giá trị (cửa quay gửi hay phần mềm đọc giờ) chờ Q-67. |
| 28 | Kết quả cho phép vào | Bước 6; Dữ liệu ra 1 trường 1 | Loại - dữ liệu trao đổi qua boundary AC-B-TurnstileDevice | Giá trị "Cho phép" hoặc "Không cho phép" gửi cho cửa quay, không lưu. |
| 29 | Lý do không cho phép, quy tắc bị vi phạm, thông báo cho cửa quay | Luồng 3a1a, 3a1b, 4a, 4b, 4c; Dữ liệu ra 1 trường 2 | Loại - dữ liệu trao đổi qua boundary AC-B-TurnstileDevice | Không lưu; nội dung và cách báo cho người quét chờ Q-70. |
| 30 | Mã QR không hợp lệ | Luồng 3b | Loại - dữ liệu trao đổi qua boundary AC-B-TurnstileDevice | Lý do trả cho cửa quay khi mã không khớp hội viên hay vé, không lưu. |
| 31 | Vắng mặt | BR-20; mục 8 của đặc tả | Loại - không tham gia hành vi của use case này (khái niệm của UC-016) | Chỉ được nhắc làm mục đích dùng lượt quẹt (GL-41). |
| 32 | Lớp nhóm, giờ học, chỗ đã đặt (trong BR-20) | BR-20 | Loại - không tham gia hành vi của use case này (khái niệm của UC-009, UC-010) | Use case này không đọc hay kiểm tra; dùng "giờ học" (GL-13) theo thuật ngữ chuẩn của P05, chờ Q-73. |
| 33 | Khoảng từ 30 phút trước đến 10 phút sau giờ học | BR-20 | Loại - tham số của quy tắc BR-20 | Hằng số của BR-20, UC-016 dùng. |
| 34 | Ứng dụng của hội viên, mã QR hiển thị trên ứng dụng | Tiền điều kiện | Loại - không tham gia hành vi của use case này (khái niệm của CAND-34, tiền điều kiện theo phương án (a)) | Hiển thị mã QR nằm ngoài luồng của UC-018. |
| 35 | Xác thực của hội viên | Tiền điều kiện | Loại - không tham gia hành vi của use case này (khái niệm của UC-004) | Chỉ là tiền điều kiện. |

Yêu cầu phi chức năng "phản hồi trong vòng 1 giây" (NFR-02) không phải danh từ của luồng sự kiện và không tạo lớp phân tích; mốc đo chờ Q-41.

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| EnterBranchHandler (AC-C-EnterBranchHandler) | UC-018 Vào chi nhánh | Mới | Một control điều phối luồng của cả hai tác nhân chính; hậu tố Handler theo HAU_TO_TEN_LOP. Không tách control phụ vì không có phần điều phối lớn dùng lại ở nhiều use case. |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-TurnstileDevice | boundary | TurnstileDevice | // scanQrCode: nhận thao tác đưa mã QR vào đầu đọc của người vào<br>// receiveScannedCode: nhận mã QR đọc được, chi nhánh và thời điểm quẹt từ cửa quay<br>// sendEntryResult: gửi cho cửa quay kết quả cho phép hoặc không cho phép kèm quy tắc bị vi phạm (nội dung và cách báo cho người quét chờ Q-70)<br>// openDoor: yêu cầu cửa quay mở cửa khi kết quả là cho phép | scannedQrCode (Văn bản)<br>turnstileBranch (Văn bản)<br>scanTime (Ngày, Giờ) | 1, 2, 3a1a, 3a1b, 3b, 4a, 4b, 4c, 6, 7 | Giao diện thiết bị | Mới | GL-30, GL-32 |
| AC-C-EnterBranchHandler | control | EnterBranchHandler | // handleEntryRequest: nhận lượt quét từ cửa quay và điều phối xác định hội viên, kiểm tra gói, ghi nhận lượt quẹt, trả kết quả (bước 2-6, 3b, 4a, 4b, 4c)<br>// handleDayPassEntry: điều phối nhánh vé khi mã QR không phải mã hội viên: đối chiếu vé, kiểm tra ngày và chi nhánh, rồi tiếp tục bước 6 (3a, 3a1, 3a1a, 3a1b) | - | 2-6, 3a, 3a1, 3a1a, 3a1b, 3b, 4a, 4b, 4c | - | Mới | - |
| AC-E-Member | entity | Member | // matchesQrCode: đối chiếu mã QR đọc được với mã QR của hội viên (Q-68)<br>// checkPackageEligibility: kiểm tra hội viên có gói tập còn hiệu lực, không đang bảo lưu, áp dụng cho chi nhánh của cửa quay, bằng cách hỏi từng gói và tổng hợp kết quả (BR-15, BR-16, BR-17; nhiều gói Q-69)<br>// recordEntryScan: ghi nhận lượt quẹt vào cửa của hội viên kèm chi nhánh và thời điểm quẹt | qrCode (Văn bản, mới ở UC này) | 3, 4, 4a, 4b, 4c, 5 | - | Tái dùng từ UC-005, UC-010, UC-015, bổ sung trách nhiệm | GL-19, GL-32 |
| AC-E-MembershipPackage | entity | MembershipPackage | // checkEntryEligibility: kiểm tra gói chưa quá ngày hết hạn (BR-15; Q-74), không đang bảo lưu (BR-16), áp dụng cho chi nhánh của cửa quay (BR-17; Q-50), theo thứ tự đó | expiryDate (Ngày)<br>status (Trạng thái; giá trị đang bảo lưu theo Q-75)<br>appliedBranch (Văn bản, Q-50) | 4, 4a, 4b, 4c | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-01, GL-16, GL-17 |
| AC-E-EntryScan | entity | EntryScan | // createEntryScan: khởi tạo lượt quẹt vào cửa từ hội viên, chi nhánh của cửa quay và thời điểm quẹt | scanTime (Ngày, Giờ)<br>branch (Văn bản) | 5 | - | Mới | GL-30 |
| AC-E-DayPass | entity | DayPass | // matchesQrCode: đối chiếu mã QR đọc được với mã QR in trên vé<br>// checkUsableToday: kiểm tra hôm nay là ngày mua vé (BR-18)<br>// checkUsableAtBranch: kiểm tra chi nhánh của cửa quay là chi nhánh đã mua vé (BR-19) | qrCode (Văn bản)<br>purchaseDate (Ngày)<br>purchaseBranch (Văn bản) | 3a, 3a1, 3a1a, 3a1b | - | Mới - chủ sở hữu UC-017 | GL-42, GL-32 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // scanQrCode | AC-B-TurnstileDevice | Giao tiếp tác nhân | Người vào chỉ thao tác vật lý trên cửa quay nên message đi tới boundary thiết bị (F6, ngoại lệ thiết bị; bước 1 và 2 liền nhau). |
| 2 | // receiveScannedCode | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 2 | // handleEntryRequest | AC-C-EnterBranchHandler | Controller | - |
| 3 | // matchesQrCode | AC-E-Member | Information Expert | Mã QR của hội viên nằm ở hội viên. Không có đối tượng toàn thể nắm tập hội viên trong đặc tả, BR, glossary nên control lặp và gửi message tới từng hội viên (A6). |
| 3a | // handleDayPassEntry | AC-C-EnterBranchHandler | Controller | - |
| 3a | // matchesQrCode | AC-E-DayPass | Information Expert | Mã QR trên vé nằm ở vé; không có đối tượng toàn thể nắm tập vé nên control lặp (A6). |
| 3a1 | // checkUsableToday | AC-E-DayPass | Information Expert | Ngày mua vé nằm ở vé. Đặt phép so sánh ở control sẽ làm control nắm quy tắc BR-18 thuộc dữ liệu của vé. |
| 3a1 | // checkUsableAtBranch | AC-E-DayPass | Information Expert | Chi nhánh đã mua vé nằm ở vé; cùng lý do với BR-18. |
| 3a1a | // sendEntryResult | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 3a1b | // sendEntryResult | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 3b | // sendEntryResult | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 4 | // checkPackageEligibility | AC-E-Member | Information Expert | Dữ liệu nằm ở hai lớp: tập gói tập thuộc hội viên (quan hệ cấu trúc Member - MembershipPackage), ngày hết hạn, trạng thái, chi nhánh áp dụng nằm ở gói. Chọn giao việc hỏi từng gói và tổng hợp cho Member, vì Member là đối tượng toàn thể nắm tập gói (A6). Phương án để control lặp trên gói thêm quan hệ Handler - MembershipPackage và đặt quy tắc tổng hợp (Q-69) ở control (coupling cao hơn, cohesion thấp hơn). |
| 4 | // checkEntryEligibility | AC-E-MembershipPackage | Information Expert | Ngày hết hạn, trạng thái, chi nhánh áp dụng nằm ở gói; giao cho gói để Member không nắm dữ liệu của gói. |
| 4a | // sendEntryResult | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 4b | // sendEntryResult | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 4c | // sendEntryResult | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 5 | // recordEntryScan | AC-E-Member | Creator | Member là lớp chứa và ghi nhận lượt quẹt của chính hội viên (GL-30). Phương án để control tạo trực tiếp lượt quẹt làm control nắm việc khởi tạo thuộc entity và thêm quan hệ Handler - EntryScan. |
| 5 | // createEntryScan | AC-E-EntryScan | Creator | Khởi tạo dữ liệu của chính lượt quẹt từ hội viên, chi nhánh, thời điểm quẹt. |
| 6 | // sendEntryResult | AC-B-TurnstileDevice | Giao tiếp tác nhân | - |
| 7 | // openDoor | AC-B-TurnstileDevice | Giao tiếp tác nhân | Cửa quay (ACT-12) mở cửa theo kết quả; boundary thiết bị chuyển lệnh mở cửa. |

Bước 8 do người vào thực hiện, không có tương tác với phần mềm nên không có dòng ở F4. Luồng 3a1c chưa có hành động (Q-40) nên không có dòng.

## F5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-018.drawio gồm 5 trang. Luồng chính của hội viên tách thành SD1a (bước 1-3), SD1b (bước 4, luồng 4a, 4b), SD1c (luồng 4c, bước 5-7) vì mỗi trang chỉ chứa tối đa 3 fragment ở mức ngoài cùng. Luồng 3a, 3b, 3a1, 3a1a, 3a1b của khách vãng lai vẽ ở SD2a, SD2b; mọi luồng kết thúc use case dùng break ở mức ngoài cùng của trang. Luồng 3a1c chưa có hành động (Q-40) nên không có message. Bước 8 do người vào thực hiện, không có message. STT message của luồng rẽ ở message 2.1.1 (luồng 3a, 3b) có hậu tố a, b; message 3a1a, 3a1b dùng tiếp STT của luồng 3a.

### SD1a - Luồng chính, bước 1-3 (Hội viên)

a) Sơ đồ SD1a: Luồng chính bước 1-3. Trang "SD1a" trong diagrams/P07-sequence-UC-018.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1a-L1 | Actor | Hội viên (ACT-02) | «actor» | - | Tác nhân chính | 40 | 40 | 120 | 360 |
| SD1a-L2 | Lifeline | :EnterBranchHandler | «control» | - | Lớp AC-C-EnterBranchHandler | 200 | 40 | 120 | 360 |
| SD1a-L3 | Lifeline | :Member | «entity» | - | Lớp AC-E-Member; trong loop là từng hội viên được đối chiếu | 360 | 40 | 120 | 360 |
| SD1a-L4 | Lifeline | :TurnstileDevice | «boundary» | - | Lớp AC-B-TurnstileDevice; boundary chung của ACT-02, ACT-03, ACT-12 (người vào chỉ thao tác vật lý trên cửa quay) | 520 | 40 | 120 | 360 |
| SD1a-L5 | Actor | Cửa quay (ACT-12) | «actor» | - | Tác nhân phụ, thiết bị | 680 | 40 | 120 | 360 |
| SD1a-F1 | Fragment | loop [mỗi hội viên, đến khi mã QR khớp] | - | - | Control lặp vì không có đối tượng toàn thể nắm tập hội viên (A6) | 30 | 240 | 780 | 120 |
| SD1a-N1 | Note | Không có hội viên nào khớp: luồng 3a, 3b (SD2a, rẽ tại message 2.1.1) | - | - | - | 840 | 340 | 400 | 50 |
| SD1a-N2 | Note | Có hội viên khớp: tiếp tục SD1b (bước 4) | - | - | - | 840 | 400 | 400 | 30 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1a-M01 | 1 | SD1a-L1 | SD1a-L4 | // scanQrCode (mã QR hiển thị trên ứng dụng) | Đồng bộ | - | 1 |
| SD1a-M02 | 2 | SD1a-L5 | SD1a-L4 | // receiveScannedCode (mã QR đọc được, chi nhánh của cửa quay, thời điểm quẹt) | Đồng bộ | - | 2 |
| SD1a-M03 | 2.1 | SD1a-L4 | SD1a-L2 | // handleEntryRequest (mã QR đọc được, chi nhánh của cửa quay, thời điểm quẹt) | Đồng bộ | - | 2 |
| SD1a-M04 | 2.1.1 | SD1a-L2 | SD1a-L3 | // matchesQrCode (mã QR đọc được) | Đồng bộ | SD1a-F1 | 3 |
| SD1a-M05 | 2.1.1 (trả về) | SD1a-L3 | SD1a-L2 | mã QR có khớp hội viên này hay không | Trả về | SD1a-F1 | 3 |

### SD1b - Luồng chính bước 4 và luồng 4a, 4b (Hội viên)

a) Sơ đồ SD1b: Luồng chính bước 4; luồng 4a, 4b. Trang "SD1b" trong diagrams/P07-sequence-UC-018.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1b-L1 | Lifeline | :EnterBranchHandler | «control» | - | Lớp AC-C-EnterBranchHandler | 40 | 40 | 120 | 570 |
| SD1b-L2 | Lifeline | :Member | «entity» | - | Lớp AC-E-Member; hội viên có mã QR khớp ở SD1a | 200 | 40 | 120 | 570 |
| SD1b-L3 | Lifeline | :MembershipPackage | «entity» | - | Lớp AC-E-MembershipPackage; trong loop là từng gói tập của hội viên | 360 | 40 | 120 | 570 |
| SD1b-L4 | Lifeline | :TurnstileDevice | «boundary» | - | Lớp AC-B-TurnstileDevice; boundary chung của ACT-02, ACT-03, ACT-12 (người vào chỉ thao tác vật lý trên cửa quay) | 520 | 40 | 120 | 570 |
| SD1b-F1 | Fragment | loop [mỗi gói tập của hội viên] | - | - | Member nắm tập gói tập của hội viên nên Member lặp (A6); cách tổng hợp khi có nhiều gói chờ Q-69 | 30 | 210 | 620 | 120 |
| SD1b-F2 | Fragment | break [hội viên không có gói tập còn hiệu lực (BR-15)] | - | - | Luồng 4a, kết thúc use case (thất bại); cách báo cho người quét chờ Q-70 | 30 | 390 | 620 | 80 |
| SD1b-F3 | Fragment | break [hội viên có gói còn hiệu lực và gói đang bảo lưu (BR-16)] | - | - | Luồng 4b, kết thúc use case (thất bại); cách báo cho người quét chờ Q-70 | 30 | 490 | 620 | 80 |
| SD1b-N1 | Note | Tiếp theo SD1a, sau message 2.1.1 khi mã QR khớp một hội viên | - | - | - | 30 | 120 | 620 | 30 |
| SD1b-N2 | Note | Gói chưa vi phạm BR-15, BR-16: tiếp tục SD1c (luồng 4c, bước 5) | - | - | - | 680 | 550 | 400 | 50 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1b-M01 | 2.1.2 | SD1b-L1 | SD1b-L2 | // checkPackageEligibility (chi nhánh của cửa quay) | Đồng bộ | - | 4 |
| SD1b-M02 | 2.1.2.1 | SD1b-L2 | SD1b-L3 | // checkEntryEligibility (chi nhánh của cửa quay) | Đồng bộ | SD1b-F1 | 4 |
| SD1b-M03 | 2.1.2.1 (trả về) | SD1b-L3 | SD1b-L2 | kết quả của gói: hợp lệ / hết hiệu lực / đang bảo lưu / không áp dụng cho chi nhánh | Trả về | SD1b-F1 | 4 |
| SD1b-M04 | 2.1.2 (trả về) | SD1b-L2 | SD1b-L1 | kết quả kiểm tra gói của hội viên: hợp lệ / không có gói còn hiệu lực / gói đang bảo lưu / gói không áp dụng cho chi nhánh | Trả về | - | 4 |
| SD1b-M05 | 2.1.3 | SD1b-L1 | SD1b-L4 | // sendEntryResult (không cho phép, quy tắc bị vi phạm BR-15) | Đồng bộ | SD1b-F2 | 4a |
| SD1b-M06 | 2.1.4 | SD1b-L1 | SD1b-L4 | // sendEntryResult (không cho phép, quy tắc bị vi phạm BR-16) | Đồng bộ | SD1b-F3 | 4b |

### SD1c - Luồng chính bước 4c, 5-7 (Hội viên)

a) Sơ đồ SD1c: Luồng chính bước 5-7; luồng 4c. Trang "SD1c" trong diagrams/P07-sequence-UC-018.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1c-L1 | Lifeline | :EnterBranchHandler | «control» | - | Lớp AC-C-EnterBranchHandler | 40 | 40 | 120 | 420 |
| SD1c-L2 | Lifeline | :Member | «entity» | - | Lớp AC-E-Member; hội viên có mã QR khớp ở SD1a | 200 | 40 | 120 | 420 |
| SD1c-L3 | Lifeline | :EntryScan | «entity» | - | Đối tượng được tạo bởi message loại Tạo; đỉnh lifeline ngang y của message; lớp AC-E-EntryScan | 360 | 320 | 120 | 140 |
| SD1c-L4 | Lifeline | :TurnstileDevice | «boundary» | - | Lớp AC-B-TurnstileDevice; boundary chung của ACT-02, ACT-03, ACT-12 (người vào chỉ thao tác vật lý trên cửa quay) | 520 | 40 | 120 | 420 |
| SD1c-L5 | Actor | Cửa quay (ACT-12) | «actor» | - | Tác nhân phụ, thiết bị | 680 | 40 | 120 | 420 |
| SD1c-F1 | Fragment | ref SD1b - Bước 4, luồng 4a, 4b | - | - | Hội viên chưa bị từ chối ở 4a, 4b | 30 | 120 | 780 | 40 |
| SD1c-F2 | Fragment | break [hội viên có gói còn hiệu lực, không đang bảo lưu, không áp dụng cho chi nhánh của cửa quay (BR-17)] | - | - | Luồng 4c, kết thúc use case (thất bại); cách báo cho người quét chờ Q-70 | 30 | 180 | 780 | 80 |
| SD1c-N1 | Note | Bước 8: người vào đi qua cửa quay, không tương tác với phần mềm | - | - | - | 840 | 400 | 400 | 50 |
| SD1c-N2 | Note | Luồng 3a1 (vé dùng được) tiếp tục từ message 2.1.7 (bước 6) | - | - | - | 840 | 460 | 400 | 50 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1c-M01 | 2.1.5 | SD1c-L1 | SD1c-L4 | // sendEntryResult (không cho phép, quy tắc bị vi phạm BR-17) | Đồng bộ | SD1c-F2 | 4c |
| SD1c-M02 | 2.1.6 | SD1c-L1 | SD1c-L2 | // recordEntryScan (chi nhánh của cửa quay, thời điểm quẹt) | Đồng bộ | - | 5 |
| SD1c-M03 | 2.1.6.1 | SD1c-L2 | SD1c-L3 | «create» // createEntryScan (hội viên, chi nhánh của cửa quay, thời điểm quẹt) | Tạo | - | 5 |
| SD1c-M04 | 2.1.7 | SD1c-L1 | SD1c-L4 | // sendEntryResult (cho phép) | Đồng bộ | - | 6 |
| SD1c-M05 | 2.1.7.1 | SD1c-L4 | SD1c-L5 | // openDoor | Đồng bộ | - | 7 |

### SD2a - Luồng 3a, 3b (Khách vãng lai, đối chiếu mã QR)

a) Sơ đồ SD2a: Luồng 3a, 3b. Trang "SD2a" trong diagrams/P07-sequence-UC-018.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD2a-L1 | Actor | Khách vãng lai (ACT-03) | «actor» | - | Tác nhân chính; biến thể của message 1 trong SD1a | 40 | 40 | 120 | 440 |
| SD2a-L2 | Lifeline | :EnterBranchHandler | «control» | - | Lớp AC-C-EnterBranchHandler | 200 | 40 | 120 | 440 |
| SD2a-L3 | Lifeline | :DayPass | «entity» | - | Lớp AC-E-DayPass; trong loop là từng vé được đối chiếu | 360 | 40 | 120 | 440 |
| SD2a-L4 | Lifeline | :TurnstileDevice | «boundary» | - | Lớp AC-B-TurnstileDevice; boundary chung của ACT-02, ACT-03, ACT-12 (người vào chỉ thao tác vật lý trên cửa quay) | 520 | 40 | 120 | 440 |
| SD2a-F1 | Fragment | ref SD1a - Bước 1-3 (tác nhân quét là Khách vãng lai ACT-03) | - | - | Message 1, 2, 2.1, 2.1.1 như SD1a; không có hội viên khớp ở message 2.1.1 | 30 | 120 | 620 | 40 |
| SD2a-F2 | Fragment | loop [mỗi vé tập một ngày, đến khi mã QR khớp] | - | - | Control lặp vì không có đối tượng toàn thể nắm tập vé (A6) | 30 | 220 | 620 | 120 |
| SD2a-F3 | Fragment | break [mã QR không khớp hội viên nào và không khớp vé nào (3b)] | - | - | Luồng 3b, kết thúc use case (thất bại); cách báo cho người quét chờ Q-70 | 30 | 360 | 620 | 80 |
| SD2a-N1 | Note | Mã QR khớp một vé: tiếp tục SD2b (bước 3a1) | - | - | - | 680 | 420 | 400 | 30 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2a-M01 | 2.1.1a | SD2a-L2 | SD2a-L2 | // handleDayPassEntry | Tự gọi | - | 3a |
| SD2a-M02 | 2.1.1a.1 | SD2a-L2 | SD2a-L3 | // matchesQrCode (mã QR đọc được) | Đồng bộ | SD2a-F2 | 3a |
| SD2a-M03 | 2.1.1a.1 (trả về) | SD2a-L3 | SD2a-L2 | mã QR có khớp vé này hay không | Trả về | SD2a-F2 | 3a |
| SD2a-M04 | 2.1.1b | SD2a-L2 | SD2a-L4 | // sendEntryResult (không cho phép, mã QR không hợp lệ: BR-15, BR-18) | Đồng bộ | SD2a-F3 | 3b |

### SD2b - Luồng 3a1, 3a1a, 3a1b (Khách vãng lai, kiểm tra vé)

a) Sơ đồ SD2b: Luồng 3a1, 3a1a, 3a1b. Trang "SD2b" trong diagrams/P07-sequence-UC-018.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD2b-L1 | Lifeline | :EnterBranchHandler | «control» | - | Lớp AC-C-EnterBranchHandler | 40 | 40 | 120 | 510 |
| SD2b-L2 | Lifeline | :DayPass | «entity» | - | Lớp AC-E-DayPass; vé có mã QR khớp ở SD2a | 200 | 40 | 120 | 510 |
| SD2b-L3 | Lifeline | :TurnstileDevice | «boundary» | - | Lớp AC-B-TurnstileDevice; boundary chung của ACT-02, ACT-03, ACT-12 (người vào chỉ thao tác vật lý trên cửa quay) | 360 | 40 | 120 | 510 |
| SD2b-F1 | Fragment | break [hôm nay không phải ngày mua vé (BR-18)] | - | - | Luồng 3a1a, kết thúc use case (thất bại); cách báo cho người quét chờ Q-70 | 30 | 250 | 460 | 80 |
| SD2b-F2 | Fragment | break [hôm nay là ngày mua vé và vé được mua ở chi nhánh khác chi nhánh của cửa quay (BR-19)] | - | - | Luồng 3a1b, kết thúc use case (thất bại); cách báo cho người quét chờ Q-70 | 30 | 430 | 460 | 80 |
| SD2b-N1 | Note | Tiếp theo SD2a, sau message 2.1.1a.1 khi mã QR khớp một vé | - | - | - | 30 | 120 | 460 | 30 |
| SD2b-N2 | Note | Luồng 3a1c (vé đúng ngày, đúng chi nhánh, đã dùng trước đó): đặc tả chưa có hành động, chờ Q-40, không có message | - | - | - | 520 | 490 | 400 | 70 |
| SD2b-N3 | Note | Vé dùng được: tiếp tục luồng chính từ message 2.1.7 (bước 6) ở SD1c | - | - | - | 520 | 570 | 400 | 50 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2b-M01 | 2.1.1a.2 | SD2b-L1 | SD2b-L2 | // checkUsableToday (BR-18) | Đồng bộ | - | 3a1 |
| SD2b-M02 | 2.1.1a.2 (trả về) | SD2b-L2 | SD2b-L1 | hôm nay có phải ngày mua vé | Trả về | - | 3a1 |
| SD2b-M03 | 2.1.1a.3 | SD2b-L1 | SD2b-L3 | // sendEntryResult (không cho phép, quy tắc bị vi phạm BR-18) | Đồng bộ | SD2b-F1 | 3a1a |
| SD2b-M04 | 2.1.1a.4 | SD2b-L1 | SD2b-L2 | // checkUsableAtBranch (chi nhánh của cửa quay) (BR-19) | Đồng bộ | - | 3a1 |
| SD2b-M05 | 2.1.1a.4 (trả về) | SD2b-L2 | SD2b-L1 | chi nhánh của cửa quay có phải chi nhánh đã mua vé | Trả về | - | 3a1 |
| SD2b-M06 | 2.1.1a.5 | SD2b-L1 | SD2b-L3 | // sendEntryResult (không cho phép, quy tắc bị vi phạm BR-19) | Đồng bộ | SD2b-F2 | 3a1b |

## F6. Quy tắc tương tác giữa các lớp phân tích

Không có vi phạm. Các điểm cần ghi nhận: message 1 từ ACT-02 (hoặc ACT-03) tới AC-B-TurnstileDevice dùng ngoại lệ thiết bị của F6 (bước 1 và bước 2 liền nhau); message 2 và message 2.1.7.1 là giao tiếp giữa actor ACT-12 và boundary của nó; Member gọi MembershipPackage và EntryScan dựa trên quan hệ cấu trúc R-UC018-04, R-UC018-05; message 2.1.1a là message tự gọi của control.

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-018.drawio, một trang. Phạm vi: luồng chính của hội viên (mọi trang SD1, chỉ các message không nằm trong fragment break) và biến thể của tác nhân chính thứ hai ACT-03 (message 1, và các message của luồng 3a đạt ở SD2a, SD2b: 2.1.1a, 2.1.1a.1, 2.1.1a.2, 2.1.1a.4). MUC_CHI_TIET là GON nên các luồng kết thúc use case (3a1a, 3a1b, 3b, 4a, 4b, 4c) không vẽ ở communication diagram; STT giữ nguyên STT của sequence diagram nên có khoảng trống (2.1.3 đến 2.1.5).

a) Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| L1 | Actor | Hội viên (ACT-02) | «actor» | - | Tác nhân chính | 40 | 40 | 60 | 80 |
| L2 | Actor | Khách vãng lai (ACT-03) | «actor» | - | Tác nhân chính; biến thể của message 1 | 40 | 200 | 60 | 80 |
| L3 | Object | :TurnstileDevice | «boundary» | - | Lớp AC-B-TurnstileDevice | 360 | 40 | 220 | 60 |
| L4 | Actor | Cửa quay (ACT-12) | «actor» | - | Tác nhân phụ, thiết bị | 840 | 30 | 60 | 80 |
| L5 | Object | :EnterBranchHandler | «control» | - | Lớp AC-C-EnterBranchHandler | 360 | 240 | 220 | 60 |
| L6 | Object | :Member | «entity» | - | Lớp AC-E-Member | 200 | 440 | 200 | 60 |
| L7 | Object | :DayPass | «entity» | - | Lớp AC-E-DayPass; chỉ có ở biến thể Khách vãng lai | 760 | 440 | 200 | 60 |
| L8 | Object | :MembershipPackage | «entity» | - | Lớp AC-E-MembershipPackage | 40 | 640 | 200 | 60 |
| L9 | Object | :EntryScan | «entity» | - | Lớp AC-E-EntryScan | 360 | 640 | 200 | 60 |

b) Bảng Edge (link)

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message | Điểm uốn |
|---|---|---|---|---|---|---|
| LK-01 | L1 | L3 | Link | 1: // scanQrCode (-->) | Chiều: Nguồn-->Đích | - |
| LK-02 | L4 | L3 | Link | 2: // receiveScannedCode (-->)<br>2.1.7.1: // openDoor (<--) | 2: Nguồn-->Đích; 2.1.7.1: Đích-->Nguồn | - |
| LK-03 | L3 | L5 | Link | 2.1: // handleEntryRequest (-->)<br>2.1.7: // sendEntryResult (<--) | 2.1: Nguồn-->Đích; 2.1.7: Đích-->Nguồn | - |
| LK-04 | L5 | L6 | Link | 2.1.1: // matchesQrCode (-->)<br>2.1.2: // checkPackageEligibility (-->)<br>2.1.6: // recordEntryScan (-->) | Nguồn-->Đích | - |
| LK-05 | L6 | L8 | Link | 2.1.2.1: // checkEntryEligibility (-->) | Nguồn-->Đích | - |
| LK-06 | L6 | L9 | Link | 2.1.6.1: «create» // createEntryScan (-->) | Nguồn-->Đích | - |
| LK-07 | L5 | L5 | Link | 2.1.1a: // handleDayPassEntry (-->) | Link tự nối; biến thể Khách vãng lai (luồng 3a); Nguồn-->Đích | (700,250); (700,290) |
| LK-08 | L5 | L7 | Link | 2.1.1a.1: // matchesQrCode (-->)<br>2.1.1a.2: // checkUsableToday (-->)<br>2.1.1a.4: // checkUsableAtBranch (-->) | Biến thể Khách vãng lai (luồng 3a, 3a1); Nguồn-->Đích | - |
| LK-09 | L2 | L3 | Link | 1: // scanQrCode (-->) | Biến thể Khách vãng lai: cùng message 1 do ACT-03 thực hiện; Nguồn-->Đích | - |

## F8. VOPC (View Of Participating Classes)

File diagrams/P07-class-UC-018.drawio.

### a) Bảng Node (lớp)

| ID (mã AC) | Loại | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-B-TurnstileDevice | Class | TurnstileDevice | boundary | - | scannedQrCode (Văn bản)<br>turnstileBranch (Văn bản)<br>scanTime (Ngày, Giờ) | // scanQrCode<br>// receiveScannedCode<br>// sendEntryResult<br>// openDoor | 600 | 40 | 300 | 210 |
| AC-C-EnterBranchHandler | Class | EnterBranchHandler | control | - | - | // handleEntryRequest<br>// handleDayPassEntry | 600 | 340 | 300 | 130 |
| AC-E-MembershipPackage | Class | MembershipPackage | entity | - | expiryDate (Ngày)<br>status (Trạng thái)<br>appliedBranch (Văn bản, Q-50) | // checkEntryEligibility | 40 | 640 | 300 | 150 |
| AC-E-Member | Class | Member | entity | - | qrCode (Văn bản, mới ở UC này) | // matchesQrCode<br>// checkPackageEligibility<br>// recordEntryScan | 420 | 640 | 300 | 150 |
| AC-E-EntryScan | Class | EntryScan | entity | - | scanTime (Ngày, Giờ)<br>branch (Văn bản) | // createEntryScan | 800 | 640 | 300 | 130 |
| AC-E-DayPass | Class | DayPass | entity | - | qrCode (Văn bản)<br>purchaseDate (Ngày)<br>purchaseBranch (Văn bản) | // matchesQrCode<br>// checkUsableToday<br>// checkUsableAtBranch | 1180 | 640 | 300 | 190 |

### b) Bảng quan hệ (bảng Edge)

Quan hệ giữa boundary - control và control - entity ghi Loại Association, mang ghi chú "tạm thời" ở cột Nguồn, multiplicity "-" vì đặc tả không nêu; P08 và P12 quyết định dạng thiết kế. Link actor - boundary (LK-01, LK-02, LK-09) và link tự nối (LK-07) không vào VOPC. R-UC018-03 lấy căn cứ từ link của biến thể Khách vãng lai. R-UC018-04 cùng cặp lớp với R-UC005-12 (P08 gộp).

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC018-01 | AC-B-TurnstileDevice | AC-C-EnterBranchHandler | Association | - | - | Link LK-03 (2.1, 2.1.7); tạm thời |
| R-UC018-02 | AC-C-EnterBranchHandler | AC-E-Member | Association | - | - | Link LK-04 (2.1.1, 2.1.2, 2.1.6); tạm thời |
| R-UC018-03 | AC-C-EnterBranchHandler | AC-E-DayPass | Association | - | - | Link LK-08 (2.1.1a.1, 2.1.1a.2, 2.1.1a.4; biến thể Khách vãng lai); tạm thời |
| R-UC018-04 | AC-E-Member | AC-E-MembershipPackage | Association | A 1 - B ? | - | Link LK-05 (2.1.2.1); GL-16, GL-19 (gói tập thuộc một hội viên); số gói của một hội viên chờ Q-69; cùng cặp lớp với R-UC005-12 (P08 gộp) |
| R-UC018-05 | AC-E-Member | AC-E-EntryScan | Association | A 1 - B ? | - | Link LK-06 (2.1.6.1); GL-30, bước 5 (lượt quẹt vào cửa của hội viên); số lượt quẹt của một hội viên chờ Q-86 |

Điểm uốn của các cạnh trong file .drawio (toạ độ tuyệt đối, theo C7.1):

| ID cạnh | Nguồn | Đích | Điểm uốn |
|---|---|---|---|
| R-UC018-01 | AC-B-TurnstileDevice | AC-C-EnterBranchHandler | - |
| R-UC018-02 | AC-C-EnterBranchHandler | AC-E-Member | - |
| R-UC018-03 | AC-C-EnterBranchHandler | AC-E-DayPass | (850,520); (1330,520) |
| R-UC018-04 | AC-E-Member | AC-E-MembershipPackage | - |
| R-UC018-05 | AC-E-Member | AC-E-EntryScan | - |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1 | AC-B-TurnstileDevice |
| 2 | 2, 2.1 | AC-B-TurnstileDevice, AC-C-EnterBranchHandler |
| 3 | 2.1.1 | AC-C-EnterBranchHandler, AC-E-Member |
| 3a | 2.1.1a, 2.1.1a.1 | AC-C-EnterBranchHandler, AC-E-DayPass |
| 3a1 | 2.1.1a.2, 2.1.1a.4 | AC-C-EnterBranchHandler, AC-E-DayPass |
| 3a1a | 2.1.1a.3 | AC-C-EnterBranchHandler, AC-B-TurnstileDevice |
| 3a1b | 2.1.1a.5 | AC-C-EnterBranchHandler, AC-B-TurnstileDevice |
| 3b | 2.1.1b | AC-C-EnterBranchHandler, AC-B-TurnstileDevice |
| 4 | 2.1.2, 2.1.2.1 | AC-C-EnterBranchHandler, AC-E-Member, AC-E-MembershipPackage |
| 4a | 2.1.3 | AC-C-EnterBranchHandler, AC-B-TurnstileDevice |
| 4b | 2.1.4 | AC-C-EnterBranchHandler, AC-B-TurnstileDevice |
| 4c | 2.1.5 | AC-C-EnterBranchHandler, AC-B-TurnstileDevice |
| 5 | 2.1.6, 2.1.6.1 | AC-C-EnterBranchHandler, AC-E-Member, AC-E-EntryScan |
| 6 | 2.1.7 | AC-C-EnterBranchHandler, AC-B-TurnstileDevice |
| 7 | 2.1.7.1 | AC-B-TurnstileDevice |

Bước 3a1c (chưa có hành động, Q-40) và bước 8 (người vào đi qua cửa quay) không có message.

## F10. File .drawio

| File | Số trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-018.drawio | 5 | SD1a, SD1b, SD1c, SD2a, SD2b |
| diagrams/P07-communication-UC-018.drawio | 1 | Luồng chính và biến thể Khách vãng lai |
| diagrams/P07-class-UC-018.drawio | 1 | VOPC UC-018 |

XML không nén, cell id="0" và id="1", ID cell trùng ID trong các bảng mô hình ở F5, F7, F8, toạ độ là bội số của 10.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-86 | Mỗi lần hội viên quét mã và được phép vào có tạo một lượt quẹt riêng (kể cả khi hội viên quét nhiều lần trong ngày hoặc tại nhiều chi nhánh), hay mỗi hội viên chỉ có một lượt quẹt cho mỗi ngày hoặc mỗi lần vào chi nhánh? (Mỗi lần quét được phép vào là một lượt / Một lượt cho mỗi hội viên mỗi ngày, nêu cách xử lý lần quét sau / Khác - nêu rõ) | AC-E-EntryScan (// createEntryScan); AC-E-Member (// recordEntryScan); R-UC018-05; F2 bước 5; UC-016 | UC-018 bước 5 "Ghi nhận lượt quẹt vào cửa của hội viên tại chi nhánh" và BR-20 "không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu lớp" không nêu số lượt ghi khi hội viên quét nhiều lần |

Các câu hỏi đã cấp ở bước trước và làm đổi phân tích này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-67 (nội dung cửa quay gửi và nhận, thời điểm quẹt, cách biết chi nhánh), Q-68 (cách tạo, thời hạn mã QR hội viên), Q-69 (hội viên có nhiều gói), Q-70 (cách báo cho người quét, thứ tự lý do), Q-71 (ghi nhận lượt bị từ chối, lượt dùng vé), Q-72 (cửa quay không nhận được kết quả), Q-40 (số lần dùng vé trong ngày), Q-41 (mốc đo 1 giây), Q-18 (gói buổi tập cá nhân có tính khi vào chi nhánh), Q-03, Q-50 (danh mục chi nhánh, chi nhánh áp dụng của gói), Q-73 (giờ học và giờ bắt đầu), Q-74, Q-75 (ngày hết hạn, trạng thái gói).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Không có. Các đề xuất đã nêu ở P04 UC-018, P05, P06 (REQ bổ sung vào cột REQ của P02, hiển thị mã QR là tiền điều kiện, đổi cách gọi theo P05, ghi chú "chưa có BR" ở P05) được xử lý theo YEU_CAU_BO_SUNG và không lặp lại ở đây.

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 1: luồng 3a1c trong đặc tả chưa có hành động ("Chờ Q-40") nên không có dòng F4, F9 và không có message; luồng này có dòng ở F2 và một note ở SD2b. Khi Q-40 có câu trả lời và P04 bổ sung hành động, chạy lại P07. Bước 1, 2, 7, 8 do tác nhân thực hiện; bước 8 không có message vì không có tương tác với phần mềm.
- Target 3 (đạt theo cách hiểu): ba tác nhân tương tác trực tiếp (ACT-02, ACT-03, ACT-12) cùng đi qua một boundary AC-B-TurnstileDevice vì hai tác nhân người chỉ thao tác vật lý trên cửa quay và chưa có kênh báo kết quả cho họ (Q-70). Nếu Q-70 chọn màn hình của ứng dụng hoặc thông báo đẩy thì cần thêm boundary giao diện người dùng hoặc kênh thông báo cho ACT-02, ACT-03 (và có thể thêm tác nhân phụ ở P01 đến P03), rồi chạy lại P07.
- Target 9: AC-E-EntryScan chỉ có trách nhiệm khởi tạo (createEntryScan) và AC-E-Member nhận thêm ba trách nhiệm; hành vi trên lượt quẹt (xác định vắng mặt theo BR-20) thuộc UC-016 nên chưa xuất hiện ở đây, P08 hợp nhất. Control có 2 trách nhiệm, không có god control.
- Target 12 (đạt theo MUC_CHI_TIET là GON): communication diagram chỉ gồm các message không nằm trong break của luồng chính và biến thể Khách vãng lai (luồng 3a đạt). Nếu dự án chuyển sang vẽ mọi luồng thay thế thì thêm các message // sendEntryResult 2.1.3, 2.1.4, 2.1.5, 2.1.1b vào link LK-03 (TurnstileDevice - Handler) và 2.1.1a.3, 2.1.1a.5 cũng vào LK-03; không cần link mới.
- Target 15: các luồng kết thúc use case đều dùng break ở mức ngoài cùng của trang. Vì luồng 3a (ACT-03) là một nhánh rẽ có luồng kết thúc con (3a1a, 3a1b) nên nhánh được vẽ ở trang riêng SD2a, SD2b thay vì alt trong trang chính; sau luồng 3a1 đạt, SD2b ghi note tiếp tục từ message 2.1.7 ở SD1c. Không có thời hạn nội bộ nào ngoài 1 giây phản hồi (NFR-02, Q-41), nên không có message after(...) và không có mốc hẹn lịch (A2).
- Ngưỡng 3 fragment ở mức ngoài cùng buộc tách luồng chính thành ba trang dù luồng chính (SD1a đến SD1c) chỉ có 13 message không kể trả về (dưới ngưỡng 30). Loop đối chiếu hội viên (SD1a), loop gói tập của hội viên (SD1b), loop đối chiếu vé (SD2a) được vẽ theo A6 vì không có đối tượng toàn thể nắm tập hội viên, tập vé; việc đối chiếu mã QR là truy vấn khoá, nếu dự án coi là không cần vẽ thì bỏ ba loop và gộp trang.
- Biến thể Khách vãng lai: message 1 của ACT-03 dùng lại STT 1 của SD1a (SD2a mở bằng ref SD1a); communication diagram có link riêng LK-09 cho ACT-03 với cùng STT 1.
- Message 1 (người quét vào boundary thiết bị) và message 2 (actor ACT-12 vào cùng boundary) cùng mô tả một thao tác vật lý ở hai bước liền nhau của đặc tả (bước 1 do người, bước 2 do cửa quay). Tách thành hai message để giữ đúng cột Thực hiện bởi của P04.
- Quy tắc tổng hợp khi hội viên có nhiều gói (Q-69) và ngày hết hạn có tính còn hiệu lực (Q-74) chưa chốt nên AC-E-Member // checkPackageEligibility và AC-E-MembershipPackage // checkEntryEligibility chỉ nêu việc kiểm tra theo thứ tự BR-15, BR-16, BR-17; chạy lại P07 khi các Q này có câu trả lời.
- Lớp có chủ sở hữu ở use case khác chưa có P07 và phải dùng lại mã: AC-E-DayPass (UC-017). Lớp do P07 này đặt mã lần đầu và các use case sau phải dùng lại: AC-B-TurnstileDevice (nếu có use case khác giao tiếp với cửa quay), AC-E-EntryScan (UC-016). AC-E-Member và AC-E-MembershipPackage đã có từ UC-005; thuộc tính qrCode của Member và trách nhiệm mới của hai lớp này do P08 hợp nhất.
- Khách vãng lai không có entity: nguồn không nêu hồ sơ của khách (GL-22), vé gắn với chi nhánh và ngày mua, không gắn với một khách cụ thể.
- Cách áp dụng YEU_CAU_BO_SUNG: REQ-10, REQ-43, REQ-46, REQ-51 chỉ trích ở cột Nguồn của F2 kèm use case cung cấp dữ liệu, không tạo đề xuất sửa P02; hiển thị mã QR (CAND-34) xử lý là tiền điều kiện nên không có boundary hay message cho việc đó; dùng "giờ học" (GL-13) thay cho "giờ bắt đầu lớp" ở BR-20 khi nhắc tới; không có chỗ nào của use case này dẫn ghi chú "chưa có BR" của P05, và ngày hết hạn lùi theo bảo lưu dẫn BR-29 của P06.

