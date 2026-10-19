# P07 - Phân tích use case UC-015 Huỷ lớp nhóm ít người đặt - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-015-cancel-under-booked-class.md (phiên bản 1.0; toàn bộ); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; dòng UC-015 ở bảng 4a, 4b; các dòng UC có tác nhân thời gian UC-008, UC-013, UC-015, UC-016, UC-022; mục Câu hỏi mở); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2); P05-glossary.md (phiên bản 1.0; GL-05, GL-08, GL-13, GL-19, GL-20, GL-29, GL-36, GL-39, mục Câu hỏi mở, Đề xuất sửa artifact trước); P06-supplementary-spec.md (phiên bản 1.0; BR-13, BR-14, NFR-10, NFR-11, mục Câu hỏi mở); P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md (phiên bản 1.0; F1, F3.4, F8 b), Câu hỏi mở, Giả định, Vấn đề còn mở); P07-uc-analysis/UC-010-book-class-spot-analysis.md (phiên bản 1.0; F1, F3.4, F8 b), Câu hỏi mở, Giả định, Vấn đề còn mở); mã Q, ASM quét ở mục Câu hỏi mở, Giả định của mọi artifact trong thư mục đầu ra (Q lớn nhất trước lần chạy: Q-84; chưa có ASM). UC_ID: UC-015 Huỷ lớp nhóm ít người đặt. LUONG_CAN_VE: Không có. YEU_CAU_BO_SUNG: đề xuất sửa artifact trước của P04, P05, P06 chưa áp dụng và các bước đó không chạy lại; REQ-22, REQ-30, REQ-34, REQ-35, REQ-70, REQ-76 mà đặc tả P04 đề nghị thêm vào cột REQ của P02 chỉ là dữ liệu do use case khác cung cấp; các đề xuất đổi cách gọi của P05 chưa áp dụng vào P00 đến P04, dùng thuật ngữ chuẩn của P05; ghi chú "chưa có BR" ở P05 nay đã có mã BR ở P06 |
| Phạm vi | UC-015 |
| Mã Q, ASM cuối đã cấp | Q-85; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-015 Huỷ lớp nhóm ít người đặt (Cancel Under-Booked Class) |
| Tác nhân chính (ACT, loại) | ACT-14 Bộ định thời theo hạn (Thời gian) |
| Tác nhân phụ (ACT, loại) | ACT-09 Cổng SMS (Hệ thống ngoài); ACT-10 Dịch vụ thông báo đẩy (Hệ thống ngoài). Hội viên đã đặt chỗ là bên nhận thụ động (P04 mục 8), không phải tác nhân |
| Include (UC) | Không có |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2: không có điểm mở rộng) |
| File P07 đã có được dùng làm sổ đăng ký AC | P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md (phiên bản 1.0) và P07-uc-analysis/UC-010-book-class-spot-analysis.md (phiên bản 1.0). Sổ gồm AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI, AC-B-PaymentGateway, AC-B-EInvoiceGateway, AC-C-PurchaseOrRenewPackageHandler, AC-E-MembershipPackage, AC-E-Member, AC-E-PackageOrder, AC-E-PaymentTransaction, AC-E-PackagePrice, AC-E-Promotion (UC-005); AC-B-BookClassSpotUI, AC-C-BookClassSpotHandler, AC-E-GroupClass, AC-E-ClassBooking, AC-E-Waitlist (UC-010; AC-E-Member tái dùng). Use case này tái dùng AC-E-GroupClass, AC-E-ClassBooking, AC-E-Member; AC-E-Waitlist không tham gia hành vi của UC-015 (Q-63); các khái niệm còn lại của sổ không tham gia. Chưa có AC nào cho boundary thông báo |
| Mốc thời gian phụ thuộc dữ liệu (A2) | UC-015 do tác nhân thời gian kích hoạt tại mốc 2 giờ trước giờ học; đối tượng mốc là lớp nhóm (AC-E-GroupClass, giá trị giờ học). Mốc này do UC-009 Lập lịch lớp nhóm hẹn và UC-014 Huỷ lớp nhóm vì sự cố huỷ (P04 mục 8); UC-015 chỉ nhận mốc đã tới nên không có message hẹn mốc của chính nó. UC-015 làm lớp nhóm mất hiệu lực (huỷ lớp) nên có message huỷ mốc của UC-016 (10 phút sau giờ học) và UC-013 (chuyển chỗ sau 30 phút) gắn với lớp, vẽ theo bước 4 của P04: message 1.3 và 1.4, nguồn ghi mã UC-016, UC-013. UC-008 (ACT-13) chạy theo lịch cố định hằng ngày và UC-022 (ACT-14) gắn với yêu cầu đặt buổi tập cá nhân nên không liên quan |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Phần mềm VietFit | Tới mốc 2 giờ trước giờ học của một lớp nhóm (BR-13). | Bộ định thời theo hạn báo cho control rằng mốc 2 giờ trước giờ học của một lớp nhóm đã tới, kèm lớp nhóm có mốc đó. Mốc được tính từ giờ học của lớp; use case này không hẹn mốc. | BR-13; GL-13, GL-29; REQ-73, REQ-74 (EV-27) |
| 2 | Phần mềm VietFit | Kiểm tra lớp nhóm chưa bị huỷ và số người đặt chỗ của lớp dưới 3 (BR-13). | Lớp nhóm tự kiểm tra trạng thái của mình chưa phải đã huỷ, đếm các chỗ đã đặt của lớp để có số người đặt chỗ và so với ngưỡng 3 của BR-13. Lớp nhóm giữ trạng thái và các chỗ đã đặt nên là nơi kiểm tra; cách đếm khi một hội viên giữ nhiều chỗ chờ Q-59, chỗ giữ riêng và chỗ của hội viên bị khoá chờ Q-22, Q-20. | BR-13; GL-05, GL-29; REQ-73, REQ-74; REQ-22 (chỗ đã đặt do UC-010) |
| 3 | Phần mềm VietFit | Huỷ lớp nhóm (BR-13). | Lớp nhóm chuyển trạng thái của chính nó sang đã huỷ. Chỗ đã đặt và danh sách chờ của lớp chưa đổi vì đặc tả chưa nêu (Q-63). | BR-13; GL-29; REQ-73, REQ-74 |
| 4 | Phần mềm VietFit | Huỷ mốc tính vắng mặt của UC-016 và mốc chuyển chỗ của UC-013 gắn với lớp (Q-64). | Control yêu cầu huỷ hai mốc còn chờ của lớp vừa huỷ: mốc tính vắng mặt (10 phút sau giờ học) và mốc chuyển chỗ từ danh sách chờ, để hai use case đó không kích hoạt cho lớp đã huỷ. Mức phân tích không chọn cơ chế lập lịch (P12 thiết kế); nếu UC-016 và UC-013 tự kiểm tra trạng thái lớp thì bước này không cần (Q-64). | Q-64; REQ-30, REQ-34, REQ-35 (mốc của UC-013, UC-016); GL-13 |
| 5 | Phần mềm VietFit | Xác định các hội viên đã đặt chỗ của lớp. | Lớp nhóm hỏi từng chỗ đã đặt của lớp để lấy hội viên đã đặt chỗ đó, kết quả là các hội viên đã đặt chỗ của lớp. Control giữ danh sách này trong lần chạy để gửi thông báo, không lưu lâu dài. | GL-05, GL-19; REQ-22 (chỗ đã đặt do UC-010) |
| 6 | Phần mềm VietFit | Gửi thông báo lớp bị huỷ (xem Dữ liệu ra 1) cho một hội viên đã đặt chỗ chưa được thông báo, qua dịch vụ thông báo đẩy, hoặc qua cổng SMS khi hội viên chưa cài ứng dụng (BR-14). | Control lấy loại lớp và giờ học của lớp bị huỷ từ lớp nhóm, hỏi hội viên kênh nhận thông báo theo BR-14 (cách xác định hội viên chưa cài ứng dụng chờ Q-36), rồi chuyển yêu cầu gửi tới boundary của dịch vụ thông báo đẩy hoặc của cổng SMS. Nội dung khác của thông báo chờ Q-66. | BR-14; GL-20, GL-36, GL-39; REQ-75, REQ-87, REQ-88, REQ-89, REQ-90; REQ-70 (loại lớp, giờ học do UC-009) |
| 7 | Phần mềm VietFit | Lặp lại bước 6 cho đến khi mọi hội viên đã đặt chỗ của lớp được gửi thông báo. | Control lặp bước 6 cho từng hội viên trong danh sách nhận ở bước 5 cho tới khi hết. Entity không gọi boundary nên việc lặp thuộc control. | BR-14; REQ-75 |
| 2a | - | Lớp nhóm đã bị huỷ trước mốc 2 giờ (do quản lý chi nhánh huỷ vì sự cố, UC-014). Không có hành động. | Kết quả kiểm tra ở bước 2 cho biết lớp đã ở trạng thái đã huỷ; control kết thúc use case, không có thay đổi dữ liệu nào được lưu. | BR-13; REQ-76 (lớp huỷ vì sự cố do UC-014) |
| 2b | - | Lớp nhóm chưa bị huỷ và có từ 3 người đặt chỗ trở lên (BR-13). Không có hành động. | Kết quả kiểm tra ở bước 2 cho biết số người đặt chỗ từ 3 trở lên; control kết thúc use case, không có thay đổi dữ liệu nào được lưu. | BR-13; REQ-73, REQ-74 |
| 5a | - | Lớp nhóm không có hội viên nào đã đặt chỗ. Không có hành động. | Kết quả ở bước 5 là không có hội viên; control kết thúc use case vì không còn ai cần được thông báo (lớp đã ở trạng thái đã huỷ từ bước 3). | GL-05 |
| 6a | - | Dịch vụ thông báo đẩy hoặc cổng SMS không gửi được thông báo cho hội viên. Chờ Q-65. | Đặc tả chưa có hành động; xử lý khi không gửi được chờ Q-65, trạng thái thông báo của các hội viên còn lại chờ Q-65 và Q-85. | Q-65, Q-85; NFR-10, NFR-11 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary (Giao diện người dùng / Kênh thông báo / Giao diện hệ thống / Giao diện thiết bị) | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-14 Bộ định thời theo hạn | Thời gian | Không có | - | - | Tác nhân thời gian chỉ kích hoạt use case; control AC-C-CancelUnderBookedClassHandler nhận sự kiện mốc (A3, F6 ngoại lệ). |
| ACT-10 Dịch vụ thông báo đẩy | Hệ thống ngoài | PushNotificationGateway (AC-B-PushNotificationGateway) | Giao diện hệ thống | Mới | Tác nhân hệ thống ngoài sinh boundary giao diện hệ thống; đặt tên theo hệ thống với hậu tố Gateway theo HAU_TO_TEN_LOP. Tái dùng được ở UC-008, UC-011, UC-014 cùng giao tiếp với dịch vụ này. |
| ACT-09 Cổng SMS | Hệ thống ngoài | SmsGateway (AC-B-SmsGateway) | Giao diện hệ thống | Mới | Như trên, cho cổng SMS của nhà mạng. Tái dùng được ở UC-008, UC-011, UC-014. |

Hội viên đã đặt chỗ nhận thông báo là bên nhận thụ động, không là tác nhân của use case này (P04 mục 8), nên không có boundary riêng; thông báo tới hội viên đi qua hai boundary hệ thống ở trên.

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Phần mềm VietFit, hệ thống | Cột Thực hiện bởi của bước 1-7 | Loại - mơ hồ | Là chính hệ thống đang phân tích, không là khái niệm nghiệp vụ. |
| 2 | Bộ định thời theo hạn | Tác nhân chính; bước 1 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-14, tác nhân thời gian. |
| 3 | Dịch vụ thông báo đẩy, cổng SMS | Tác nhân phụ; bước 6; BR-14 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-10, ACT-09; có boundary AC-B-PushNotificationGateway, AC-B-SmsGateway. |
| 4 | mốc 2 giờ trước giờ học | Bước 1; BR-13 | Loại - thao tác hoặc sự kiện | Sự kiện kích hoạt EV-27 của tác nhân thời gian, control nhận bằng message 1. |
| 5 | 2 giờ, 3 (ngưỡng dưới 3 người) | Bước 1, bước 2; BR-13 | Loại - tham số của quy tắc BR-13 | Hằng số và ngưỡng nằm trong BR-13. |
| 6 | giờ học | Bước 1; Dữ liệu ra 1; BR-13 | Loại - thuộc tính của AC-E-GroupClass | GL-13; thuộc tính startTime đã có ở UC-010. |
| 7 | lớp nhóm | Bước 1, 2, 3, 4, 5; Dữ liệu ra 1; BR-13 | Entity (AC-E-GroupClass) | GL-29. Hệ thống lưu trạng thái và các chỗ đã đặt của lớp vượt một lần chạy; lớp có hành vi riêng (kiểm tra có huỷ được không, huỷ, gom hội viên). Tái dùng từ UC-010. |
| 8 | trạng thái (đã huỷ), lớp nhóm bị huỷ | Bước 3; Dữ liệu ra 1; hậu điều kiện | Loại - thuộc tính của AC-E-GroupClass | "Lớp bị huỷ" là trạng thái của Lớp nhóm (P05 mục 3); thuộc tính status. |
| 9 | loại lớp | Dữ liệu ra 1 trường 1 | Loại - thuộc tính của AC-E-GroupClass | GL-29; thuộc tính classType đã có ở UC-010. |
| 10 | số người đặt chỗ | Bước 2; luồng 2b; BR-13 | Loại - giá trị suy ra từ AC-E-ClassBooking | Đếm các chỗ đã đặt của lớp khi cần, không lưu; số người bằng số chỗ khi mỗi hội viên một chỗ (GL-05, Q-59). |
| 11 | chỗ đã đặt (trong "đặt chỗ") | Bước 2, 5; BR-13 | Entity (AC-E-ClassBooking) | GL-05. Hệ thống lưu chỗ đã đặt vượt một lần chạy; ClassBooking cho biết hội viên của chỗ (bước 5). Tái dùng từ UC-010. |
| 12 | người đặt chỗ | Bước 2; BR-13 | Loại - trùng hoặc đồng nghĩa với Hội viên (GL-19) | GL-19 ghi cách gọi theo trạng thái là cùng chỉ hội viên. |
| 13 | hội viên (đã đặt chỗ) | Bước 5, 6, 7; BR-14; hậu điều kiện | Entity (AC-E-Member) | GL-19. Biểu diễn thông tin về hội viên, không phải bản thân tác nhân; hội viên có hành vi riêng là cho biết kênh nhận thông báo. Tái dùng từ UC-005, UC-010. |
| 14 | thông báo lớp bị huỷ, nội dung khác của thông báo | Bước 6; Dữ liệu ra 1 | Loại - dữ liệu trao đổi qua boundary AC-B-PushNotificationGateway hoặc AC-B-SmsGateway | Không lưu vì nguồn không nêu (Q-85); nội dung khác chưa quy định (Q-66). |
| 15 | thông báo đẩy | Bước 6; BR-14 | Loại - dữ liệu trao đổi qua boundary AC-B-PushNotificationGateway | GL-39; kênh và nội dung đi qua boundary. |
| 16 | SMS | Bước 6; BR-14 | Loại - dữ liệu trao đổi qua boundary AC-B-SmsGateway | GL-36. |
| 17 | ứng dụng | Bước 6; BR-14 | Loại - cấu trúc cài đặt | Ứng dụng di động là nền tảng chạy phần mềm (P05 mục 3), không là khái niệm nghiệp vụ. |
| 18 | hội viên chưa cài ứng dụng | Bước 6; BR-14 | Loại - giá trị suy ra từ AC-E-Member | GL-20; kênh nhận thông báo tính từ thông tin của hội viên khi cần (// determineNotificationChannel). Cách xác định chờ Q-36 nên không gán thuộc tính. |
| 19 | trạng thái thông báo | Hậu điều kiện tối thiểu (luồng 6a); bước 6 "chưa được thông báo" | Loại - mơ hồ | Chưa biết hệ thống có lưu việc đã gửi hay không (Q-85); trong lần chạy control chỉ giữ danh sách hội viên đang lặp. |
| 20 | mốc tính vắng mặt, mốc chuyển chỗ | Bước 4; hậu điều kiện | Loại - cấu trúc cài đặt | Mốc hẹn giờ của UC-016 và UC-013 là cơ chế lập lịch (P05 mục 3 loại, P12 thiết kế); hẹn, huỷ mốc ghi bằng message tự gọi của control theo A2 (1.3, 1.4). |
| 21 | vắng mặt | Bước 4 (tên mốc) | Loại - không tham gia hành vi của use case này (khái niệm của UC-016) | Chỉ nhắc tên mốc; use case này không đọc hay ghi vắng mặt. |
| 22 | danh sách chờ | Bước 4 (mốc chuyển chỗ); hậu điều kiện | Loại - không tham gia hành vi của use case này (khái niệm của UC-010, UC-013) | Đặc tả không đọc hay ghi danh sách chờ khi huỷ lớp; xử lý chờ Q-63, nên AC-E-Waitlist không tham gia. |
| 23 | quản lý chi nhánh | Luồng 2a | Loại - là tác nhân hoặc ngoài phạm vi | ACT-06, tác nhân của UC-014. |
| 24 | sự cố | Luồng 2a | Loại - không tham gia hành vi của use case này (khái niệm của UC-014) | Lý do huỷ lớp của UC-014; use case này chỉ nhận biết lớp đã ở trạng thái đã huỷ. |
| 25 | dữ liệu | Hậu điều kiện tối thiểu | Loại - mơ hồ | Chỉ nói chung "thay đổi dữ liệu", không là khái niệm cụ thể. |

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| CancelUnderBookedClassHandler (AC-C-CancelUnderBookedClassHandler) | UC-015 Huỷ lớp nhóm ít người đặt | Mới | Một control nhận mốc từ tác nhân thời gian và điều phối trình tự kiểm tra, huỷ lớp, huỷ mốc, gom hội viên, gửi thông báo; hậu tố Handler theo HAU_TO_TEN_LOP. Không tách control phụ vì không có phần điều phối lớn dùng lại ở nhiều use case. |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-PushNotificationGateway | boundary | PushNotificationGateway | // sendPushNotification: nhận yêu cầu gửi thông báo đẩy của một hội viên và chuyển cho dịch vụ thông báo đẩy | - | 6, 7 | Giao diện hệ thống | Mới | GL-39 |
| AC-B-SmsGateway | boundary | SmsGateway | // sendSms: nhận yêu cầu gửi SMS tới một hội viên và chuyển cho cổng SMS | - | 6, 7 | Giao diện hệ thống | Mới | GL-36 |
| AC-C-CancelUnderBookedClassHandler | control | CancelUnderBookedClassHandler | // handleClassCutoff: nhận mốc 2 giờ trước giờ học của một lớp nhóm và điều phối bước 1-7, lặp gửi thông báo cho từng hội viên<br>// cancelAbsenceMark: yêu cầu huỷ mốc tính vắng mặt của UC-016 gắn với lớp (Q-64)<br>// cancelWaitlistTransferMark: yêu cầu huỷ mốc chuyển chỗ của UC-013 gắn với lớp (Q-64) | - | 1-7, 2a, 2b, 5a | - | Mới | - |
| AC-E-GroupClass | entity | GroupClass | // checkUnderBookedCancellable: kiểm tra lớp chưa huỷ và số người đặt chỗ dưới 3 (BR-13; Q-59, Q-22, Q-20)<br>// cancelClass: chuyển trạng thái lớp sang đã huỷ (BR-13)<br>// collectBookedMembers: gom các hội viên đã đặt chỗ của lớp bằng cách hỏi từng chỗ đã đặt<br>// provideCancelledClassInfo: cung cấp loại lớp và giờ học của lớp bị huỷ để đưa vào thông báo | classType (Văn bản)<br>startTime (Ngày, Giờ)<br>status (Trạng thái) | 2, 2a, 2b, 3, 5, 5a, 6 | - | Tái dùng từ UC-010, bổ sung trách nhiệm | GL-29, GL-13 |
| AC-E-ClassBooking | entity | ClassBooking | // provideBookedMember: cung cấp hội viên đã đặt chỗ này | - | 5 | - | Tái dùng từ UC-010, bổ sung trách nhiệm | GL-05 |
| AC-E-Member | entity | Member | // determineNotificationChannel: cho biết hội viên nhận thông báo qua thông báo đẩy hay SMS (BR-14; cách xác định hội viên chưa cài ứng dụng chờ Q-36) | - | 6, 7 | - | Tái dùng từ UC-005, UC-010, bổ sung trách nhiệm | GL-19, GL-20 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc (Giao tiếp tác nhân / Information Expert / Controller / Creator / Lớp mới / Giao cho control) | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // handleClassCutoff | AC-C-CancelUnderBookedClassHandler | Controller | Tác nhân thời gian không có boundary (A3), control nhận sự kiện (F6 ngoại lệ). |
| 2, 2a, 2b | // checkUnderBookedCancellable | AC-E-GroupClass | Information Expert | Dữ liệu ở nhiều lớp: trạng thái lớp (GroupClass) và các chỗ đã đặt (ClassBooking). Chọn GroupClass giữ cả hai qua quan hệ GroupClass - ClassBooking (R-UC015-05): coupling thấp, lớp tự biết mình có huỷ được không. Không chọn control đếm chỗ đã đặt (control nắm quy tắc thuộc dữ liệu của entity, god control) và không chọn ClassBooking đếm (trách nhiệm cấp tập hợp không giao cho lớp phần tử, A6). |
| 3 | // cancelClass | AC-E-GroupClass | Information Expert | Lớp nhóm nắm trạng thái của chính nó. |
| 4 | // cancelAbsenceMark, // cancelWaitlistTransferMark | AC-C-CancelUnderBookedClassHandler | Giao cho control | Giờ học (dữ liệu tính mốc) ở GroupClass nhưng mốc là cơ chế lập lịch do P12 thiết kế, không là dữ liệu nghiệp vụ của lớp; giao cho entity sẽ kéo cơ chế lập lịch vào entity. A2 giao message hẹn, huỷ mốc cho control. |
| 5, 5a | // collectBookedMembers | AC-E-GroupClass | Information Expert | Gom hội viên là trách nhiệm tác động lên tập chỗ đã đặt: giao cho đối tượng toàn thể là GroupClass, gửi message tới từng ClassBooking trong loop (A6). Không chọn control lặp vì đặc tả và glossary có đối tượng toàn thể. |
| 5 | // provideBookedMember | AC-E-ClassBooking | Information Expert | Chỗ đã đặt biết hội viên đặt chỗ đó (GL-05). |
| 6 | // provideCancelledClassInfo | AC-E-GroupClass | Information Expert | Lớp nhóm giữ loại lớp và giờ học (Dữ liệu ra 1). |
| 6, 7 | // determineNotificationChannel | AC-E-Member | Information Expert | Dữ liệu ở nhiều lớp: BR-14 chọn kênh theo hội viên, thông tin cài ứng dụng thuộc hội viên. Chọn Member; không chọn control (quy tắc thuộc dữ liệu của hội viên, god control) và không chọn boundary (boundary không chứa quy tắc nghiệp vụ). |
| 6, 7 | // sendPushNotification | AC-B-PushNotificationGateway | Giao tiếp tác nhân | - |
| 6, 7 | // sendSms | AC-B-SmsGateway | Giao tiếp tác nhân | - |
| 6, 7 | Lặp qua các hội viên (trong // handleClassCutoff) | AC-C-CancelUnderBookedClassHandler | Controller | Việc gửi đi qua boundary; entity không gọi boundary (F6) nên GroupClass không thể lặp và gửi. Control lặp trên danh sách hội viên nhận ở 1.5 (trả về). |

## F5. Sequence diagram phân tích

Luồng chính, luồng 2a, 2b, 5a, 6a nằm ở hai trang vì mức ngoài cùng của một trang tối đa 3 fragment: break 2a/2b, loop gom hội viên, break 5a thuộc SD1a; loop gửi thông báo thuộc SD1b. Luồng 2a và 2b cùng kết cục không có message riêng nên gộp vào một break.

### SD1a - Luồng chính bước 1-5 và luồng 2a, 2b, 5a

Bảng lifeline (bảng Node)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1 | Actor | Bộ định thời theo hạn (ACT-14) | - | - | Tác nhân chính, loại Thời gian; không có boundary, gửi message thẳng tới control (F6 ngoại lệ) | 40 | 40 | 120 | 760 |
| L2 | Lifeline | :CancelUnderBookedClassHandler | control | - | AC-C-CancelUnderBookedClassHandler | 200 | 40 | 120 | 760 |
| L3 | Lifeline | :GroupClass | entity | - | AC-E-GroupClass | 360 | 40 | 120 | 760 |
| L4 | Lifeline | :ClassBooking | entity | - | AC-E-ClassBooking; một đối tượng đại diện cho từng chỗ đã đặt trong loop | 520 | 40 | 120 | 760 |
| F1 | Fragment | break [2a: lớp đã huỷ trước mốc 2 giờ; 2b: lớp chưa huỷ và có từ 3 người đặt chỗ trở lên] | - | - | Luồng 2a, 2b; kết thúc use case (thất bại); đặt ở mức ngoài cùng | 180 | 230 | 300 | 100 |
| F2 | Fragment | loop [mỗi chỗ đã đặt của lớp] | - | - | Gom hội viên đã đặt chỗ (A6): GroupClass là đối tượng toàn thể gửi message tới từng ClassBooking | 340 | 520 | 300 | 100 |
| F3 | Fragment | break [5a: lớp không có hội viên đã đặt chỗ] | - | - | Luồng 5a; kết thúc use case (thành công); đặt ở mức ngoài cùng | 180 | 680 | 300 | 80 |
| N1 | Note | kết thúc use case (thất bại), không có thay đổi dữ liệu nào được lưu | - | F1 | Nội dung toán hạng của break F1 | 200 | 290 | 260 | 30 |
| N2 | Note | kết thúc use case (thành công) | - | F3 | Nội dung toán hạng của break F3 | 200 | 720 | 260 | 30 |

Bảng message

| STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC | ID | y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L1 | L2 | // handleClassCutoff (lớp nhóm có mốc) | Đồng bộ | - | 1 | M1 | 120 |
| 1.1 | L2 | L3 | // checkUnderBookedCancellable (BR-13) | Đồng bộ | - | 2, 2a, 2b | M2 | 160 |
| 1.1 (trả về) | L3 | L2 | kết quả kiểm tra | Trả về | - | 2, 2a, 2b | M3 | 200 |
| 1.2 | L2 | L3 | // cancelClass | Đồng bộ | - | 3 | M4 | 370 |
| 1.3 | L2 | L2 | // cancelAbsenceMark (lớp nhóm, giờ học) [UC-016] | Tự gọi | - | 4 | M5 | 410 |
| 1.4 | L2 | L2 | // cancelWaitlistTransferMark (lớp nhóm, giờ học) [UC-013] | Tự gọi | - | 4 | M6 | 450 |
| 1.5 | L2 | L3 | // collectBookedMembers | Đồng bộ | - | 5, 5a | M7 | 490 |
| 1.5.1 | L3 | L4 | // provideBookedMember | Đồng bộ | F2 | 5 | M8 | 560 |
| 1.5.1 (trả về) | L4 | L3 | hội viên đã đặt chỗ | Trả về | F2 | 5 | M9 | 600 |
| 1.5 (trả về) | L3 | L2 | các hội viên đã đặt chỗ | Trả về | - | 5, 5a | M10 | 650 |

### SD1b - Luồng chính bước 6, 7 và luồng 6a

Bảng lifeline (bảng Node)

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L2 | Lifeline | :CancelUnderBookedClassHandler | control | - | AC-C-CancelUnderBookedClassHandler | 40 | 40 | 120 | 680 |
| L3 | Lifeline | :GroupClass | entity | - | AC-E-GroupClass | 200 | 40 | 120 | 680 |
| L5 | Lifeline | :Member | entity | - | AC-E-Member; một đối tượng đại diện cho từng hội viên trong loop | 360 | 40 | 120 | 680 |
| L6 | Lifeline | :PushNotificationGateway | boundary | - | AC-B-PushNotificationGateway, boundary của ACT-10 | 520 | 40 | 120 | 680 |
| L7 | Actor | Dịch vụ thông báo đẩy (ACT-10) | - | - | Tác nhân phụ, loại Hệ thống ngoài | 680 | 40 | 120 | 680 |
| L8 | Lifeline | :SmsGateway | boundary | - | AC-B-SmsGateway, boundary của ACT-09 | 840 | 40 | 120 | 680 |
| L9 | Actor | Cổng SMS (ACT-09) | - | - | Tác nhân phụ, loại Hệ thống ngoài | 1000 | 40 | 120 | 680 |
| F4 | Fragment | ref SD1a (bước 1-5, lớp có hội viên đã đặt chỗ) | - | - | Trang tiếp nối SD1a; không lặp lại các message của SD1a | 20 | 90 | 160 | 50 |
| F5 | Fragment | loop [mỗi hội viên đã đặt chỗ chưa được thông báo] | - | - | Bước 7 (lặp lại bước 6 cho tới khi hết hội viên); control lặp vì entity không gọi boundary (F6) | 20 | 250 | 1100 | 430 |
| F6 | Fragment | alt [kênh thông báo là thông báo đẩy] | - | F5 | BR-14; lồng trong loop F5 | 40 | 370 | 1040 | 240 |
| F6-O2 | Fragment | [kênh thông báo là SMS (hội viên chưa cài ứng dụng)] | - | F6 | Toán hạng thứ hai của alt F6; đường ngăn là edge F6-O2-SEP nét đứt tại y=490 | 50 | 500 | 520 | 20 |
| N3 | Note | luồng 6a: xử lý khi không gửi được thông báo chờ Q-65, đặc tả chưa có hành động nên không có message | - | F5 | Luồng 6a | 60 | 630 | 700 | 30 |

Bảng message

| STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC | ID | y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.6 | L2 | L3 | // provideCancelledClassInfo | Đồng bộ | - | 6 | M11 | 180 |
| 1.6 (trả về) | L3 | L2 | loại lớp và giờ học của lớp bị huỷ | Trả về | - | 6 | M12 | 220 |
| 1.7 | L2 | L5 | // determineNotificationChannel (BR-14) | Đồng bộ | F5 | 6, 7 | M13 | 300 |
| 1.7 (trả về) | L5 | L2 | kênh thông báo | Trả về | F5 | 6, 7 | M14 | 340 |
| 1.8 | L2 | L6 | // sendPushNotification (hội viên, lớp nhóm bị huỷ) | Đồng bộ | F6 | 6, 7 | M15 | 420 |
| 1.8.1 | L6 | L7 | // requestPushDelivery (hội viên, lớp nhóm bị huỷ) | Đồng bộ | F6 | 6, 7 | M16 | 460 |
| 1.9 | L2 | L8 | // sendSms (hội viên, lớp nhóm bị huỷ) | Đồng bộ | F6-O2 | 6, 7 | M17 | 540 |
| 1.9.1 | L8 | L9 | // requestSmsDelivery (hội viên, lớp nhóm bị huỷ) | Đồng bộ | F6-O2 | 6, 7 | M18 | 580 |

## F6. Quy tắc tương tác giữa các lớp phân tích

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

Message 1 (ACT-14 --> control) dùng ngoại lệ tác nhân thời gian --> Control. Message 1.5.1 (GroupClass --> ClassBooking) là entity gọi entity có quan hệ cấu trúc (R-UC015-05).

## F7. Communication diagram

File diagrams/P07-communication-UC-015.drawio, phạm vi là luồng chính (SD1a và SD1b). MUC_CHI_TIET là GON nên không thêm luồng thay thế; các luồng 2a, 2b, 5a, 6a không có message riêng nên không thêm message nào so với luồng chính.

### a) Bảng Node

| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1 | Actor | Bộ định thời theo hạn (ACT-14) | - | - | Cùng đối tượng với lifeline L1 của F5 | 40 | 240 | 60 | 80 |
| L2 | Object | :CancelUnderBookedClassHandler | control | - | Cùng đối tượng với lifeline L2 của F5 | 240 | 240 | 280 | 60 |
| L3 | Object | :GroupClass | entity | - | Cùng đối tượng với lifeline L3 của F5 | 240 | 440 | 200 | 60 |
| L4 | Object | :ClassBooking | entity | - | Cùng đối tượng với lifeline L4 của F5 | 240 | 620 | 200 | 60 |
| L5 | Object | :Member | entity | - | Cùng đối tượng với lifeline L5 của F5 | 560 | 440 | 200 | 60 |
| L6 | Object | :PushNotificationGateway | boundary | - | Cùng đối tượng với lifeline L6 của F5 | 800 | 140 | 240 | 60 |
| L7 | Actor | Dịch vụ thông báo đẩy (ACT-10) | - | - | Cùng đối tượng với lifeline L7 của F5 | 1120 | 130 | 60 | 80 |
| L8 | Object | :SmsGateway | boundary | - | Cùng đối tượng với lifeline L8 của F5 | 800 | 340 | 240 | 60 |
| L9 | Actor | Cổng SMS (ACT-09) | - | - | Cùng đối tượng với lifeline L9 của F5 | 1120 | 330 | 60 | 80 |

### b) Bảng Edge (link)

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message | Điểm uốn |
| --- | --- | --- | --- | --- | --- | --- |
| LK-01 | L1 | L2 | Link | 1: // handleClassCutoff (lớp nhóm có mốc) (-->) | Nguồn-->Đích | - |
| LK-02 | L2 | L3 | Link | 1.1: // checkUnderBookedCancellable (BR-13) (-->)<br>1.2: // cancelClass (-->)<br>1.5: // collectBookedMembers (-->)<br>1.6: // provideCancelledClassInfo (-->) | Nguồn-->Đích | - |
| LK-03 | L2 | L2 | Link | 1.3: // cancelAbsenceMark (lớp nhóm, giờ học) [UC-016] (-->)<br>1.4: // cancelWaitlistTransferMark (lớp nhóm, giờ học) [UC-013] (-->) | Nguồn-->Đích | (330,200); (430,200) |
| LK-04 | L3 | L4 | Link | 1.5.1: // provideBookedMember (-->) | Nguồn-->Đích | - |
| LK-05 | L2 | L5 | Link | 1.7: // determineNotificationChannel (BR-14) (-->) | Nguồn-->Đích | - |
| LK-06 | L2 | L6 | Link | 1.8: // sendPushNotification (hội viên, lớp nhóm bị huỷ) (-->) | Nguồn-->Đích | - |
| LK-07 | L6 | L7 | Link | 1.8.1: // requestPushDelivery (hội viên, lớp nhóm bị huỷ) (-->) | Nguồn-->Đích | - |
| LK-08 | L2 | L8 | Link | 1.9: // sendSms (hội viên, lớp nhóm bị huỷ) (-->) | Nguồn-->Đích | - |
| LK-09 | L8 | L9 | Link | 1.9.1: // requestSmsDelivery (hội viên, lớp nhóm bị huỷ) (-->) | Nguồn-->Đích | - |

Link tự nối LK-03 mang message tự gọi 1.3 và 1.4 của control, không sinh quan hệ VOPC. Link actor - control LK-01 và actor - boundary LK-07, LK-09 không vào VOPC. Không vẽ mũi tên nhỏ chiều message.

## F8. VOPC (View Of Participating Classes)

File diagrams/P07-class-UC-015.drawio.

### a) Bảng Node (lớp)

| ID (mã AC) | Loại | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AC-B-PushNotificationGateway | Class | PushNotificationGateway | boundary | - | - | // sendPushNotification | 40 | 40 | 300 | 110 |
| AC-B-SmsGateway | Class | SmsGateway | boundary | - | - | // sendSms | 420 | 40 | 300 | 110 |
| AC-C-CancelUnderBookedClassHandler | Class | CancelUnderBookedClassHandler | control | - | - | // handleClassCutoff<br>// cancelAbsenceMark<br>// cancelWaitlistTransferMark | 200 | 220 | 400 | 150 |
| AC-E-GroupClass | Class | GroupClass | entity | - | classType (Văn bản)<br>startTime (Ngày, Giờ)<br>status (Trạng thái) | // checkUnderBookedCancellable<br>// cancelClass<br>// collectBookedMembers<br>// provideCancelledClassInfo | 40 | 430 | 300 | 210 |
| AC-E-ClassBooking | Class | ClassBooking | entity | - | - | // provideBookedMember | 420 | 430 | 300 | 110 |
| AC-E-Member | Class | Member | entity | - | - | // determineNotificationChannel | 800 | 430 | 300 | 110 |

### b) Bảng quan hệ (bảng Edge)

Quan hệ giữa boundary - control và control - entity ghi Loại Association, mang ghi chú "tạm thời" ở cột Nguồn, multiplicity "-" vì đặc tả không nêu; P08 và P12 quyết định dạng thiết kế. R-UC015-06 không có link trong F7, có bằng chứng từ đặc tả. R-UC015-05 cùng cặp lớp với R-UC010-04, R-UC015-06 cùng cặp lớp với R-UC010-06 (P08 gộp).

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC015-01 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | Association | - | - | Link LK-02 (1.1, 1.2, 1.5, 1.6); tạm thời |
| R-UC015-02 | AC-C-CancelUnderBookedClassHandler | AC-E-Member | Association | - | - | Link LK-05 (1.7); tạm thời |
| R-UC015-03 | AC-B-PushNotificationGateway | AC-C-CancelUnderBookedClassHandler | Association | - | - | Link LK-06 (1.8); tạm thời |
| R-UC015-04 | AC-B-SmsGateway | AC-C-CancelUnderBookedClassHandler | Association | - | - | Link LK-08 (1.9); tạm thời |
| R-UC015-05 | AC-E-GroupClass | AC-E-ClassBooking | Association | A 1 - B ? | - | Link LK-04 (1.5.1); GL-05 (chỗ đã đặt là chỗ của một lớp nhóm), BR-13 (đếm người đặt chỗ của lớp); số chỗ đã đặt của một lớp chưa chốt do Q-22, Q-20, Q-59 |
| R-UC015-06 | AC-E-Member | AC-E-ClassBooking | Association | A 1 - B ? | - | Bằng chứng đặc tả, không có link: GL-05 (chỗ đã đặt do một hội viên đặt), bước 5 (lấy hội viên của từng chỗ đã đặt, message 1.5.1 (trả về)); số chỗ đã đặt của một hội viên chờ Q-59 |

Điểm uốn của các cạnh trong file .drawio (toạ độ tuyệt đối, theo C7.1):

| ID cạnh | Nguồn | Đích | Điểm uốn |
|---|---|---|---|
| R-UC015-01 | AC-C-CancelUnderBookedClassHandler | AC-E-GroupClass | (250,390); (190,390) |
| R-UC015-02 | AC-C-CancelUnderBookedClassHandler | AC-E-Member | (550,400); (950,400) |
| R-UC015-03 | AC-B-PushNotificationGateway | AC-C-CancelUnderBookedClassHandler | (190,180); (300,180) |
| R-UC015-04 | AC-B-SmsGateway | AC-C-CancelUnderBookedClassHandler | (570,190); (500,190) |
| R-UC015-05 | AC-E-GroupClass | AC-E-ClassBooking | - |
| R-UC015-06 | AC-E-Member | AC-E-ClassBooking | - |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1 | ACT-14, AC-C-CancelUnderBookedClassHandler |
| 2 | 1.1, 1.1 (trả về) | AC-C-CancelUnderBookedClassHandler, AC-E-GroupClass |
| 2a | 1.1, 1.1 (trả về); break F1 | AC-C-CancelUnderBookedClassHandler, AC-E-GroupClass |
| 2b | 1.1, 1.1 (trả về); break F1 | AC-C-CancelUnderBookedClassHandler, AC-E-GroupClass |
| 3 | 1.2 | AC-C-CancelUnderBookedClassHandler, AC-E-GroupClass |
| 4 | 1.3, 1.4 | AC-C-CancelUnderBookedClassHandler |
| 5 | 1.5, 1.5.1, 1.5.1 (trả về), 1.5 (trả về) | AC-C-CancelUnderBookedClassHandler, AC-E-GroupClass, AC-E-ClassBooking |
| 5a | 1.5, 1.5 (trả về); break F3 | AC-C-CancelUnderBookedClassHandler, AC-E-GroupClass |
| 6 | 1.6, 1.6 (trả về), 1.7, 1.7 (trả về), 1.8, 1.8.1, 1.9, 1.9.1 | AC-C-CancelUnderBookedClassHandler, AC-E-GroupClass, AC-E-Member, AC-B-PushNotificationGateway, AC-B-SmsGateway, ACT-10, ACT-09 |
| 7 | 1.7, 1.7 (trả về), 1.8, 1.8.1, 1.9, 1.9.1 (lặp trong loop F5) | AC-C-CancelUnderBookedClassHandler, AC-E-Member, AC-B-PushNotificationGateway, AC-B-SmsGateway, ACT-10, ACT-09 |

## F10. File .drawio

| File | Trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-015.drawio | SD1a, SD1b | Bảng Node và bảng message ở F5; ID cell trùng cột ID (lifeline L1-L9, message M1-M18, fragment F1-F6, F6-O2, F6-O2-SEP, note N1-N3) |
| diagrams/P07-communication-UC-015.drawio | Communication - luồng chính | Bảng Node (L1-L9) và bảng Edge (LK-01 đến LK-09) ở F7 |
| diagrams/P07-class-UC-015.drawio | VOPC UC-015 | Bảng Node (mã AC) và bảng quan hệ (R-UC015-01 đến R-UC015-06) ở F8; nhãn multiplicity là cell con của cạnh (id <ID cạnh>-mA, <ID cạnh>-mB) |

Cả ba file là XML không nén, có cell id="0" và id="1", toạ độ bội số của 10.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-85 | Hệ thống có lưu lại việc đã gửi thông báo lớp bị huỷ cho từng hội viên (hội viên nào đã được gửi, kênh gửi, kết quả) để tra cứu hoặc gửi lại không, hay chỉ gửi đi và không lưu gì? (Lưu mỗi lần gửi kèm kết quả / Chỉ gửi, không lưu / Khác - nêu rõ) | F2 bước 6, 7, 6a; F3.2 dòng 14, 19; có thể phát sinh entity ghi nhận thông báo; AC-C-CancelUnderBookedClassHandler (// handleClassCutoff) | UC-015 bước 6 "một hội viên đã đặt chỗ chưa được thông báo", bước 7 "cho đến khi mọi hội viên đã đặt chỗ của lớp được gửi thông báo" và hậu điều kiện tối thiểu "trạng thái thông báo của các hội viên còn lại"; nguồn Mục 8 câu 3 "gửi thông báo cho những người đã đặt" không nêu việc lưu |

Các câu hỏi đã cấp ở bước trước và làm đổi phân tích này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-20, Q-22 (chỗ của hội viên bị khoá và chỗ giữ riêng có tính vào số người đặt chỗ), Q-36 (cách xác định hội viên chưa cài ứng dụng), Q-43 (hệ thống tự huỷ lớp hay có bước nhân viên duyệt), Q-59 (một hội viên giữ nhiều chỗ trong một lớp, số người so với số chỗ), Q-63 (chỗ đã đặt và danh sách chờ khi lớp bị huỷ), Q-64 (huỷ mốc của UC-016, UC-013), Q-65 (gửi không được), Q-66 (nội dung thông báo), Q-79 (cách xử lý chung khi gửi không được).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Không có.

## Vấn đề còn mở

Các mục Target đạt, trừ mục 1 (đạt một phần) và mục 12 (đạt theo MUC_CHI_TIET là GON), với các điểm cần người dùng lưu ý:

- Target 1: luồng 6a trong đặc tả chưa có hành động ("Chờ Q-65") nên không có dòng F4, F9 và không có message; luồng này có dòng ở F2 và một note N3 ở SD1b. Khi Q-65 có câu trả lời và P04 bổ sung hành động, chạy lại P07.
- Target 12: communication diagram chỉ gồm luồng chính. Các luồng 2a, 2b, 5a không có message riêng và 6a chưa có hành động nên chuyển sang DAY_DU không thêm message; chỉ đổi khi Q-65 thêm hành động cho 6a.
- Chọn giữa hai quy tắc (C9): boundary của ACT-09, ACT-10 được xếp là Giao diện hệ thống (P01 ghi loại Hệ thống ngoài, A3 sinh boundary giao diện hệ thống, hậu tố Gateway) thay vì Kênh thông báo kiểu PushNotifier, SmsNotifier trong HAU_TO_TEN_LOP, vì hội viên nhận thông báo là bên nhận thụ động, không là tác nhân, nên không có tác nhân người đi qua kênh thông báo. Nếu người dùng muốn coi hội viên là tác nhân nhận thông báo thì cần sửa P01, P02, P03 và chạy lại P07.
- Tách SD1a, SD1b do ngưỡng 3 fragment ở mức ngoài cùng (break 2a/2b, loop gom hội viên, break 5a, loop gửi thông báo là 4); tổng message không kể trả về là 13, dưới ngưỡng 30. Luồng 2a và 2b gộp một break vì cùng kết cục và không có message riêng; guard nêu cả hai điều kiện. Các break chứa note thay vì message.
- A6: phép đếm ở bước 2 do GroupClass thực hiện nội bộ trên tập chỗ đã đặt của mình, không vẽ loop tới từng ClassBooking, giữ cách làm của UC-010 vì ClassBooking không có dữ liệu cần cung cấp cho phép đếm. Việc gom hội viên ở bước 5 có loop vì cần lấy hội viên của từng chỗ đã đặt. Lifeline :ClassBooking và :Member đại diện cho một đối tượng trong loop, không đại diện cho tập.
- Mốc (A2, bước 4): Q-64 chưa trả lời; nếu UC-016 và UC-013 tự kiểm tra trạng thái lớp thì bỏ message 1.3 và 1.4. Mốc chuyển chỗ của UC-013 tính từ lúc thông báo nhận chỗ, không phải từ giờ học của lớp; P04 viết là "gắn với lớp" và phân tích theo P04, cách tìm các mốc đang chờ của một lớp thuộc P12. P07 của UC-009 phải có message hẹn mốc 2 giờ (và mốc 10 phút sau giờ học của UC-016), P07 của UC-014 phải có message huỷ mốc 2 giờ khi chúng chạy (P04 mục 8).
- Message 1 mang "lớp nhóm có mốc" trong khi đặc tả ghi Dữ liệu vào là "Không có"; hiểu theo bước 1 ("mốc ... của một lớp nhóm") là mốc gắn với một lớp cụ thể, không coi là tác nhân cung cấp dữ liệu.
- AC-E-ClassBooking chỉ có trách nhiệm // provideBookedMember (entity thiếu trách nhiệm hành vi), vì chỗ đã đặt chưa đổi khi lớp bị huỷ (Q-63). AC-E-Member chỉ có một trách nhiệm và không có thuộc tính mới (Q-36). P08 hợp nhất với các use case khác của hai entity này.
- Hai boundary do P07 này đặt mã lần đầu và các use case sau phải dùng lại: AC-B-PushNotificationGateway, AC-B-SmsGateway (UC-008, UC-011, UC-014). Lớp có chủ sở hữu ở use case khác chưa có P07: AC-E-GroupClass (UC-009), AC-E-Member (UC-003). // cancelClass dùng lại được ở UC-014 nếu cùng hành vi chuyển trạng thái sang đã huỷ.
- Tính đúng khi đồng thời (hội viên đặt chỗ hoặc huỷ chỗ đúng lúc mốc, BR-23 cho huỷ chậm nhất 2 giờ trước giờ học, mốc muộn nhất để đặt chờ Q-58) giữa hai message 1.1 và 1.2 thuộc P09 và P12; ở mức phân tích kiểm tra và huỷ là hai message theo hai bước đặc tả. Cách UC-011 ghi nhận huỷ chỗ (xoá hay đổi trạng thái) ảnh hưởng tới vòng gom 1.5.1; rà lại khi có P07 của UC-011.
- Cách áp dụng YEU_CAU_BO_SUNG: REQ-22, REQ-30, REQ-34, REQ-35, REQ-70, REQ-76 chỉ trích ở cột Nguồn của F2 kèm use case cung cấp dữ liệu, không tạo đề xuất sửa P02; dùng "giờ học" (GL-13) và "lớp nhóm" (GL-29) thay cho cách gọi chưa đổi ở P00 đến P04; không có chỗ nào của use case này dẫn ghi chú "chưa có BR" của P05.
