# P07 - Phân tích use case UC-010 Đặt chỗ lớp nhóm - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-010-book-class-spot.md (phiên bản 1.0; toàn bộ); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; dòng UC-010 ở bảng 4a, 4b; các dòng UC có tác nhân thời gian UC-008, UC-013, UC-015, UC-016, UC-022); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2); P05-glossary.md (phiên bản 1.0; GL-05, GL-08, GL-13, GL-19, GL-21, GL-23, GL-26, GL-27, GL-28, GL-29, GL-35, GL-38, mục Câu hỏi mở); P06-supplementary-spec.md (phiên bản 1.0; BR-06 đến BR-12, NFR-01, mục Câu hỏi mở); P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md (phiên bản 1.0; F1, F3.4, F8 b), Câu hỏi mở, Giả định, Vấn đề còn mở); mã Q, ASM quét ở mục Câu hỏi mở, Giả định của mọi artifact trong thư mục đầu ra (Q lớn nhất trước lần chạy: Q-82; chưa có ASM). UC_ID: UC-010 Đặt chỗ lớp nhóm. LUONG_CAN_VE: Không có. YEU_CAU_BO_SUNG: các đề xuất sửa artifact trước của P04, P05, P06 chưa áp dụng và các bước đó không chạy lại; REQ-69, REQ-70, REQ-73, REQ-76 chỉ là dữ liệu do use case khác cung cấp; dùng thuật ngữ chuẩn của P05 thay cho cách gọi chưa đổi ở P00 đến P04; ghi chú "chưa có BR" ở P05 nay đã có mã BR ở P06 |
| Phạm vi | UC-010 |
| Mã Q, ASM cuối đã cấp | Q-84; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-010 Đặt chỗ lớp nhóm (Book Class Spot) |
| Tác nhân chính (ACT, loại) | ACT-02 Hội viên (Người) |
| Tác nhân phụ (ACT, loại) | Không có |
| Include (UC) | Không có |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2: không có điểm mở rộng) |
| File P07 đã có được dùng làm sổ đăng ký AC | P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md (phiên bản 1.0). Sổ gồm AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI, AC-B-PaymentGateway, AC-B-EInvoiceGateway, AC-C-PurchaseOrRenewPackageHandler, AC-E-MembershipPackage, AC-E-Member, AC-E-PackageOrder, AC-E-PaymentTransaction, AC-E-PackagePrice, AC-E-Promotion. Use case này tái dùng AC-E-Member; các khái niệm khác của sổ không tham gia hành vi của UC-010 |
| Mốc thời gian phụ thuộc dữ liệu (A2) | Không có message hẹn, hẹn lại hoặc huỷ mốc. UC-015 (2 giờ trước giờ học) và UC-016 (10 phút sau giờ học) lấy mốc từ giờ học của lớp nhóm; UC-010 không tạo, đổi hay huỷ lớp nhóm hay giờ học. UC-013 lấy mốc từ lúc thông báo có chỗ trống, do UC-011 tạo; UC-010 chỉ thêm hội viên vào danh sách chờ, là đối tượng phụ thuộc, không phải đối tượng mốc. UC-008 chạy theo lịch cố định hằng ngày, UC-022 gắn với yêu cầu đặt buổi tập cá nhân, đều không liên quan tới chỗ đã đặt và danh sách chờ. Khớp với P04 mục 8 |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Hội viên | Yêu cầu đặt chỗ lớp nhóm. | Không đổi | EV-08, REQ-22 |
| 2 | Phần mềm VietFit | Hiển thị lịch các lớp nhóm để hội viên chọn lớp (xem Dữ liệu ra 1). | Hệ thống lấy từ từng lớp nhóm trong lịch lớp nhóm loại lớp, phòng, huấn luyện viên và giờ học, rồi hiển thị cho hội viên chọn. Phạm vi các lớp nhóm trong lịch chờ Q-83. | GL-26, GL-29, GL-27, GL-35, GL-21, GL-13; Dữ liệu ra 1; REQ-70 (dữ liệu do UC-009 cung cấp); Q-83 |
| 3 | Hội viên | Chọn lớp nhóm cần đặt chỗ trong lịch lớp nhóm. | Không đổi | REQ-22 |
| 4 | Phần mềm VietFit | Kiểm tra quyền đặt lớp của hội viên không đang bị khoá (BR-09). | Hệ thống lấy trạng thái khoá quyền đặt lớp của hội viên đang đặt chỗ và kiểm tra hội viên không đang trong thời gian khoá 7 ngày. Dữ liệu khoá do UC-016 ghi, use case này chỉ đọc. | BR-09, GL-23, REQ-38 |
| 5 | Phần mềm VietFit | Kiểm tra lớp nhóm đã chọn chưa bị huỷ và giờ học nằm trong thời hạn cho phép đặt chỗ (BR-06, BR-07). | Hệ thống lấy từ lớp nhóm đã chọn trạng thái huỷ và giờ học, kiểm tra lớp chưa bị huỷ, rồi kiểm tra thời điểm đặt nằm trong thời hạn cho phép tính từ giờ học. BR-06 và BR-07 mâu thuẫn nhau nên phân tích không chọn bên nào (Q-11, Q-58). | BR-06, BR-07, GL-13, GL-29, REQ-23, REQ-93, Q-11, Q-58 |
| 6 | Phần mềm VietFit | Kiểm tra số lớp hội viên đã đặt trong ngày chưa đạt mức tối đa (BR-08). | Hệ thống lấy các chỗ đã đặt của hội viên, đếm số chỗ thuộc lớp diễn ra cùng ngày với lớp đã chọn và kiểm tra số đó còn dưới mức tối đa 2. Cách tính ngày và việc có tính lớp đang trong danh sách chờ chờ Q-60. | BR-08, GL-05, REQ-24, Q-60 |
| 7 | Phần mềm VietFit | Kiểm tra số chỗ đã đặt của lớp nhóm còn dưới sức chứa (BR-10, BR-11). | Hệ thống lấy sức chứa của lớp nhóm, xác định theo phòng, đếm số chỗ đã đặt của lớp và kiểm tra số đó còn dưới sức chứa. Chỗ giữ riêng cho người trong danh sách chờ có tính hay không chờ Q-22. | BR-10, BR-11, GL-38, GL-28, GL-05, REQ-25, REQ-95, Q-03, Q-22 |
| 8 | Phần mềm VietFit | Lưu chỗ đã đặt của hội viên trong lớp nhóm (BR-11). | Hệ thống kiểm tra lại số chỗ đã đặt còn dưới sức chứa tại đúng lúc lưu, rồi tạo chỗ đã đặt gắn hội viên với lớp nhóm. Không để hội viên khác đặt chỗ xen giữa việc kiểm tra và việc lưu; nếu lớp vừa đủ chỗ thì hội viên đến sau đi theo luồng 7a. | BR-11, GL-05, REQ-94, REQ-95, NFR-01 |
| 9 | Phần mềm VietFit | Hiển thị thông tin chỗ đã đặt cho hội viên (xem Dữ liệu ra 2). | Hệ thống lấy từ lớp nhóm vừa đặt chỗ loại lớp, phòng, huấn luyện viên và giờ học, rồi hiển thị cho hội viên. | GL-05, GL-29; Dữ liệu ra 2 |
| 4a | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo quyền đặt lớp đang bị khoá (BR-09). | Hệ thống cho hội viên biết lý do từ chối là quyền đặt lớp đang bị khoá. Chỗ đã đặt và danh sách chờ của lớp không đổi. | BR-09, GL-23 |
| 5a | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo lớp nhóm đã bị huỷ. | Hệ thống cho hội viên biết lý do từ chối là lớp nhóm đã bị huỷ rồi quay lại bước 2. Chỗ đã đặt và danh sách chờ của lớp không đổi. | GL-29, REQ-73, REQ-76 (trạng thái huỷ do UC-014, UC-015 đặt) |
| 5b | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo quy tắc bị vi phạm (BR-06, BR-07). | Hệ thống cho hội viên biết lý do từ chối là giờ học nằm ngoài thời hạn cho phép đặt chỗ rồi quay lại bước 2. Chỗ đã đặt và danh sách chờ của lớp không đổi. | BR-06, BR-07, Q-11, Q-58 |
| 6a | Phần mềm VietFit | Từ chối yêu cầu đặt chỗ và thông báo quy tắc bị vi phạm (BR-08). | Hệ thống cho hội viên biết lý do từ chối là số lớp đã đặt trong ngày đạt mức tối đa rồi quay lại bước 2. Chỗ đã đặt và danh sách chờ của lớp không đổi. | BR-08, Q-60 |
| 7a | - | Vào danh sách chờ | Dòng điều kiện: số chỗ đã đặt của lớp bằng sức chứa. Không có hành động riêng, các bước 7a1 đến 7a4 thực hiện luồng. | BR-11, BR-12, GL-28 |
| 7a1 | Phần mềm VietFit | Thông báo lớp nhóm đã đủ chỗ và đề nghị hội viên vào danh sách chờ (BR-12). | Hệ thống cho hội viên biết lớp đã đủ chỗ và đề nghị vào danh sách chờ của lớp. Hội viên tự chọn vào danh sách chờ hay hệ thống tự đưa vào chờ Q-62. | BR-12, GL-08, GL-28, Q-62 |
| 7a2 | Hội viên | Yêu cầu vào danh sách chờ của lớp nhóm. | Không đổi | REQ-26, BR-12 |
| 7a2a | - | Hội viên không yêu cầu vào danh sách chờ | Không đổi (không có hành động của hệ thống, use case kết thúc thất bại) | REQ-26 |
| 7a3 | Phần mềm VietFit | Thêm hội viên vào danh sách chờ của lớp nhóm (thứ tự xếp Q-61). | Hệ thống thêm hội viên vào danh sách chờ của lớp nhóm và xác định vị trí của hội viên trong danh sách. Cách xếp thứ tự chờ Q-61; danh sách chờ là đối tượng riêng của lớp hay không chờ Q-84. | GL-08, REQ-26, Q-61, Q-84 |
| 7a4 | Phần mềm VietFit | Hiển thị vị trí của hội viên trong danh sách chờ (xem Dữ liệu ra 3). | Hệ thống hiển thị loại lớp, giờ học của lớp và vị trí của hội viên trong danh sách chờ. | GL-08, GL-27, GL-13; Dữ liệu ra 3 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-02 Hội viên | Người | BookClassSpotUI (AC-B-BookClassSpotUI) | Giao diện người dùng | Mới | Một boundary cho cặp (Hội viên, UC-010), hậu tố UI theo HAU_TO_TEN_LOP. Nhận yêu cầu và lựa chọn của hội viên; hiển thị lịch lớp, thông báo từ chối, thông tin chỗ đã đặt và vị trí chờ. UC-010 không có tác nhân phụ nên không có boundary khác. |

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | hội viên (người đặt chỗ) | Bước 1, 3, 7a2; Tác nhân chính | Loại - là tác nhân hoặc ngoài phạm vi | ACT-02 là người dùng của hệ thống. |
| 2 | hội viên (hồ sơ: quyền đặt lớp, các chỗ đã đặt) | Bước 4, 6; BR-08, BR-09 | Entity (AC-E-Member) | Hệ thống lưu thông tin về hội viên (khoá quyền đặt lớp, các chỗ đã đặt) vượt quá một lần thực hiện và kiểm tra trên dữ liệu đó (BR-08, BR-09). Entity biểu diễn thông tin về hội viên, không phải bản thân tác nhân ACT-02. Tái dùng mã từ UC-005; GL-19. |
| 3 | Phần mềm VietFit, hệ thống | Mọi bước hệ thống | Loại - mơ hồ | Tên chủ ngữ của hệ thống đang xây dựng, không phải khái niệm nghiệp vụ (P05 mục 3). |
| 4 | yêu cầu đặt chỗ, yêu cầu vào danh sách chờ | Bước 1, 7a2 | Loại - thao tác hoặc sự kiện | Hành động của hội viên (EV-08), không lưu. |
| 5 | lịch các lớp nhóm | Bước 2, 3; Dữ liệu ra 1; GL-26 | Loại - cấu trúc cài đặt | Tập hợp lấy ra từ các lớp nhóm để hiển thị; nguồn chưa nêu định danh và vòng đời riêng của lịch (Q-16, Q-83). Control lặp theo từng lớp nhóm (A6). |
| 6 | lớp nhóm (lớp) | Bước 2 đến 9, mọi luồng; GL-29 | Entity (AC-E-GroupClass) | Có trạng thái huỷ, giờ học, sức chứa và hành vi kiểm tra đặt chỗ (BR-06, BR-07, BR-10, BR-11). Do UC-009 lập, UC-009 chưa có P07. |
| 7 | loại lớp | Dữ liệu ra 1, 2, 3; GL-27 | Loại - thuộc tính của GroupClass | Use case này chỉ hiển thị, không đọc hay kiểm tra hành vi riêng. Danh mục loại lớp chờ Q-04. |
| 8 | phòng | Dữ liệu ra 1, 2; BR-10; GL-35 | Loại - thuộc tính của GroupClass | Use case này chỉ hiển thị tên phòng; sức chứa ghi trên lớp nhóm (dòng 18). P08 xem lại có entity Room hay không (Q-03). |
| 9 | huấn luyện viên | Dữ liệu ra 1, 2; GL-21 | Loại - thuộc tính của GroupClass | Use case này chỉ hiển thị họ tên huấn luyện viên phụ trách lớp. Hồ sơ huấn luyện viên do use case khác quản lý (Q-05). |
| 10 | giờ học (ngày và giờ bắt đầu), ngày | Bước 2, 5; Dữ liệu ra 1, 2, 3; BR-06; GL-13 | Loại - thuộc tính của GroupClass | startTime của lớp, là mốc tính thời hạn đặt chỗ (BR-06) và ngày để đếm số lớp trong ngày (BR-08). |
| 11 | thời hạn cho phép đặt chỗ (7 ngày trước giờ học; tuần mới mở lúc 6 giờ sáng thứ Hai) | Bước 5, 5b; BR-06, BR-07 | Loại - tham số của quy tắc BR-06, BR-07 | Hằng số nằm trong hai quy tắc đang mâu thuẫn nhau (Q-11, Q-58). |
| 12 | lớp đã bị huỷ (trạng thái huỷ) | Bước 5, 5a | Loại - thuộc tính của GroupClass | status của lớp, do UC-014 và UC-015 đặt (REQ-73, REQ-76). |
| 13 | quyền đặt lớp, khoá quyền đặt lớp, 7 ngày khoá | Bước 4, 4a; BR-09; GL-23 | Loại - khái niệm do UC-016 tạo, use case này chỉ đọc qua entity Member | GL-23 định nghĩa là trạng thái của hội viên; UC-016 không được include hay extend bởi UC-010. Member giữ thuộc tính bookingSuspension; 7 ngày là tham số của BR-09. |
| 14 | số lớp hội viên đã đặt trong ngày | Bước 6, 6a; BR-08 | Loại - giá trị suy ra từ ClassBooking | Đếm khi cần, không lưu; cách tính ngày chờ Q-60. |
| 15 | mức tối đa 2 lớp một ngày | Bước 6, 6a; BR-08 | Loại - tham số của quy tắc BR-08 | Hằng số nằm trong quy tắc. |
| 16 | chỗ đã đặt | Bước 8, 9; Dữ liệu ra 2; GL-05 | Entity (AC-E-ClassBooking) | Hệ thống lưu vượt quá một lần thực hiện (UC-011, UC-012, UC-015, UC-016 đọc hoặc đổi, P04 mục 8); có định danh nghiệp vụ là cặp hội viên và lớp nhóm. |
| 17 | số chỗ đã đặt của lớp | Bước 7, 7a; BR-11 | Loại - giá trị suy ra từ ClassBooking | Đếm khi cần, không lưu. |
| 18 | sức chứa | Bước 7, 7a; BR-10, BR-11; GL-38 | Loại - thuộc tính của GroupClass | capacity của lớp, xác định theo phòng (BR-10); quan hệ với sức chứa của phòng chờ Q-03. |
| 19 | lớp đã đủ chỗ | Bước 7, 7a; GL-28 | Loại - giá trị suy ra từ GroupClass | Số chỗ đã đặt bằng sức chứa, tính khi cần. |
| 20 | danh sách chờ | Bước 7a, 7a1, 7a3; BR-12; GL-08 | Entity (AC-E-Waitlist) | Tập hợp có tên riêng trong glossary, có định danh nghiệp vụ theo lớp nhóm và vòng đời qua UC-011, UC-012, UC-013 (A4); có hành vi giữ thứ tự và xác định vị trí. Danh sách có phải đối tượng riêng của lớp hay không chờ Q-84. |
| 21 | vị trí trong danh sách chờ | Bước 7a4; Dữ liệu ra 3 | Loại - giá trị suy ra từ Waitlist | Tính khi cần, không lưu. |
| 22 | thứ tự xếp chờ | Bước 7a3; Dữ liệu ra 3 | Loại - mơ hồ | Nguồn không nêu quy tắc xếp (Q-61). |
| 23 | thông báo, quy tắc bị vi phạm, lý do từ chối | Bước 4a, 5a, 5b, 6a, 7a1 | Loại - dữ liệu trao đổi qua boundary BookClassSpotUI | Nội dung hiển thị cho hội viên, không lưu. |
| 24 | thông tin chỗ đã đặt | Bước 9; Dữ liệu ra 2 | Loại - dữ liệu trao đổi qua boundary BookClassSpotUI | Hiển thị loại lớp, phòng, huấn luyện viên, giờ học lấy từ GroupClass, không lưu thêm. |
| 25 | phiên làm việc, hội viên đã được xác thực | Tiền điều kiện | Loại - cấu trúc cài đặt | Thuộc UC-004; P05 mục 3 không đưa vào thuật ngữ. |
| 26 | 1.500 hội viên đặt chỗ cùng lúc | Yêu cầu đặc biệt 1; NFR-01 | Loại - tham số của quy tắc BR-11 | Mức tải của NFR-01 gắn với việc đặt cùng lúc của BR-11, không phải khái niệm lưu trữ. |
| 27 | gói tập | Không có trong luồng; Q-12 | Loại - không tham gia hành vi của use case này (khái niệm của UC-005) | Đặc tả không có kiểm tra gói tập (Q-12). Nếu Q-12 trả lời cần gói thì thêm MembershipPackage (AC-E-MembershipPackage) vào phân tích. |

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| BookClassSpotHandler (AC-C-BookClassSpotHandler) | UC-010 Đặt chỗ lớp nhóm | Mới | Một control điều phối trình tự kiểm tra, lưu và hiển thị kết quả; hậu tố Handler theo HAU_TO_TEN_LOP. Không tách control phụ vì không có phần điều phối lớn dùng lại ở nhiều use case. |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-BookClassSpotUI | boundary | BookClassSpotUI | // requestBookClass: nhận yêu cầu đặt chỗ lớp nhóm của hội viên<br>// showClassSchedule: hiển thị lịch các lớp nhóm (loại lớp, phòng, huấn luyện viên, giờ học)<br>// selectClass: nhận lớp nhóm hội viên chọn, kiểm tra hình thức (bắt buộc chọn một lớp)<br>// showBookingRejectedNotice: thông báo từ chối yêu cầu đặt chỗ kèm lý do<br>// showClassFullNotice: thông báo lớp đã đủ chỗ và đề nghị vào danh sách chờ<br>// requestJoinWaitlist: nhận yêu cầu vào danh sách chờ của hội viên<br>// showWaitlistPosition: hiển thị loại lớp, giờ học và vị trí trong danh sách chờ<br>// showBookedSpot: hiển thị thông tin chỗ đã đặt (loại lớp, phòng, huấn luyện viên, giờ học) | selectedClass (lớp nhóm đã chọn) | 1, 2, 3, 4a, 5a, 5b, 6a, 7a1, 7a2, 7a4, 9 | Giao diện người dùng | Mới | GL-26, GL-29 |
| AC-C-BookClassSpotHandler | control | BookClassSpotHandler | // startBooking: điều phối lấy và hiển thị lịch lớp nhóm (bước 1-2)<br>// bookClass: điều phối các kiểm tra quyền đặt lớp, lớp nhóm, số lớp trong ngày, chỗ trống, lưu chỗ đã đặt và hiển thị kết quả (bước 3-9, 4a, 5a, 5b, 6a, 7a1)<br>// joinWaitlist: điều phối thêm hội viên vào danh sách chờ và hiển thị vị trí (7a2-7a4) | - | 1-9, 4a, 5a, 5b, 6a, 7a1-7a4 | - | Mới | - |
| AC-E-Member | entity | Member | // checkBookingNotSuspended: kiểm tra hội viên không đang bị khoá quyền đặt lớp (BR-09)<br>// checkDailyBookingLimit: đếm các chỗ đã đặt của hội viên thuộc lớp diễn ra cùng ngày với lớp đã chọn và so với mức tối đa (BR-08; cách tính ngày Q-60) | bookingSuspension (Trạng thái, mới ở UC này) | 4, 6 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-19, GL-23 |
| AC-E-GroupClass | entity | GroupClass | // provideClassInfo: cung cấp loại lớp, phòng, huấn luyện viên, giờ học để hiển thị<br>// checkBookable: kiểm tra lớp chưa bị huỷ và thời điểm đặt nằm trong thời hạn cho phép tính từ giờ học (BR-06, BR-07)<br>// checkSpotAvailable: đếm chỗ đã đặt của lớp và so với sức chứa (BR-10, BR-11)<br>// reserveSpot: kiểm tra lại chỗ trống tại lúc lưu rồi tạo chỗ đã đặt cho hội viên (BR-11)<br>// addToWaitlist: thêm hội viên vào danh sách chờ của lớp và cho biết vị trí | classType (Văn bản)<br>room (Văn bản)<br>trainer (Văn bản)<br>startTime (Ngày, Giờ)<br>capacity (Số lượng)<br>status (Trạng thái) | 2, 5, 7, 7a3, 8, 9 | - | Mới - chủ sở hữu UC-009 | GL-29, GL-13, GL-26, GL-27, GL-35, GL-21, GL-38, GL-28 |
| AC-E-ClassBooking | entity | ClassBooking | // initializeBooking: nhận hội viên và lớp nhóm, ghi nhận chỗ đã đặt | - | 8 | - | Mới | GL-05 |
| AC-E-Waitlist | entity | Waitlist | // addMember: thêm hội viên vào danh sách chờ (thứ tự xếp Q-61) và cho biết vị trí của hội viên | - | 7a3 | - | Mới | GL-08 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestBookClass | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 1 | // startBooking | AC-C-BookClassSpotHandler | Controller | - |
| 2 | // provideClassInfo | AC-E-GroupClass | Information Expert | Loại lớp, phòng, huấn luyện viên, giờ học nằm ở lớp nhóm. Không có đối tượng toàn thể cho lịch lớp nhóm (F3.2 dòng 5) nên control lặp theo từng lớp nhóm (A6). |
| 2 | // showClassSchedule | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 3 | // selectClass | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 3 | // bookClass | AC-C-BookClassSpotHandler | Controller | - |
| 4 | // checkBookingNotSuspended | AC-E-Member | Information Expert | Trạng thái khoá nằm ở hội viên (GL-23). Không giao control vì sẽ thành god control, không giao boundary vì boundary không chứa quy tắc nghiệp vụ. |
| 4a | // showBookingRejectedNotice | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 5 | // checkBookable | AC-E-GroupClass | Information Expert | Trạng thái huỷ và giờ học cùng nằm ở lớp nhóm nên một trách nhiệm trả kết quả đã huỷ, ngoài thời hạn hoặc hợp lệ. Hai kiểm tra thuộc cùng một bước và cùng dữ liệu nên không tách. |
| 5a | // showBookingRejectedNotice | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 5b | // showBookingRejectedNotice | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 6 | // checkDailyBookingLimit | AC-E-Member | Information Expert | Dữ liệu nằm ở nhiều lớp: các chỗ đã đặt do Member nắm qua quan hệ với ClassBooking, ngày của lớp đã chọn do GroupClass nắm. Chọn Member vì đếm các chỗ của hội viên là tổng hợp trên tập của hội viên (A6) và coupling thấp nhất, control chỉ truyền lớp đã chọn. Phương án khác: giao GroupClass thì lớp phải biết mọi chỗ đã đặt của hội viên ở lớp khác (coupling cao); giao control thì thành god control. |
| 6a | // showBookingRejectedNotice | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 7 | // checkSpotAvailable | AC-E-GroupClass | Information Expert | Dữ liệu nằm ở nhiều lớp: sức chứa xác định theo phòng (BR-10) và tập chỗ đã đặt của lớp. Chọn GroupClass vì sức chứa là thuộc tính của lớp trong phân tích này và lớp nắm tập chỗ đã đặt của mình. Phương án khác: tạo entity Room giữ sức chứa thì thêm một lớp chỉ trả dữ liệu; P08 quyết định (Q-03). |
| 7a1 | // showClassFullNotice | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 7a2 | // requestJoinWaitlist | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 7a2 | // joinWaitlist | AC-C-BookClassSpotHandler | Controller | - |
| 7a3 | // addToWaitlist | AC-E-GroupClass | Information Expert | Danh sách chờ là của một lớp nhóm (GL-08) nên lớp nhóm nắm quan hệ tới Waitlist; control chỉ biết lớp nhóm (Low Coupling). Phương án khác: control gọi Waitlist trực tiếp thì control phải tìm danh sách chờ của lớp. |
| 7a3 | // addMember | AC-E-Waitlist | Information Expert | Waitlist nắm thứ tự và vị trí của hội viên chờ (GL-08). |
| 7a4 | // showWaitlistPosition | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |
| 8 | // reserveSpot | AC-E-GroupClass | Information Expert | Kiểm tra lại số chỗ và tạo chỗ đã đặt cùng thuộc lớp nhóm để không có hội viên khác xen giữa (BR-11). Phương án khác: control gọi kiểm tra rồi gọi tạo thì khe hở giữa hai lời gọi vi phạm BR-11. |
| 8 | // initializeBooking | AC-E-ClassBooking | Creator | Lớp nhóm ghi nhận chỗ đã đặt và có dữ liệu khởi tạo (hội viên, lớp nhóm). Phương án khác: Member tạo vì hội viên là người đặt, nhưng Member không nắm số chỗ của lớp nên không bảo đảm được BR-11. |
| 9 | // showBookedSpot | AC-B-BookClassSpotUI | Giao tiếp tác nhân | - |

## F5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-010.drawio gồm hai trang. Luồng chính cùng luồng 4a, 5a, 5b, 6a, 7a và vòng lặp ở bước 2 tạo 5 fragment ở mức ngoài cùng (loop, break 4a, alt 5, alt 6, break 7a), vượt ngưỡng 3, nên luồng chính tách theo đoạn bước thành SD1a (bước 1-5) và SD1b (bước 6-9). Mỗi trang có đúng 3 fragment ở mức ngoài cùng (SD1b tính cả fragment ref tới SD1a). Mọi luồng thay thế vẽ trong trang chứa bước rẽ.

Quy ước STT: luồng thay thế trong fragment dùng tiếp số của chuỗi 2.1 (4a là 2.1.2, 5a là 2.1.4, 5b là 2.1.5, 6a là 2.1.7, 7a1 là 2.1.9); hành động của hội viên ở bước 7a2 là message 3. Message bước 8 và 9 sau break 7a giữ chuỗi 2.1 (2.1.10, 2.1.11) vì break chỉ chạy thay cho phần còn lại của trang. ID cell trong file .drawio của mỗi message là <mã trang>-M-<STT>, message trả về thêm hậu tố -R.

### SD1a - Luồng chính bước 1-5 và luồng 4a, 5a, 5b

a) Tên sơ đồ và luồng thể hiện: SD1a - Luồng chính bước 1-5 và luồng 4a (break), 5a, 5b (alt, quay lại bước 2). Vòng loop ở bước 2 lấy thông tin từng lớp nhóm trong lịch, do control lặp (F3.2 dòng 5).

b) Bảng lifeline

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| SD1a-L1 | Actor | Hội viên (ACT-02) | - | - | Tác nhân chính ACT-02 |
| SD1a-L2 | Lifeline | :BookClassSpotUI | «boundary» | - | Boundary giao diện người dùng của ACT-02 |
| SD1a-L3 | Lifeline | :BookClassSpotHandler | «control» | - | Control của UC-010 |
| SD1a-L4 | Lifeline | :Member | «entity» | - | - |
| SD1a-L5 | Lifeline | :GroupClass | «entity» | - | - |
| SD1a-F1 | Fragment | loop [mỗi lớp nhóm trong lịch lớp nhóm] | - | - | Operand 1 |
| SD1a-F2 | Fragment | break [quyền đặt lớp của hội viên đang bị khoá (4a)] | - | - | Operand 1 |
| SD1a-F3 | Fragment | alt [lớp nhóm đã bị huỷ (5a)] | - | - | Operand 1 |
| SD1a-F3-O2 | Fragment | [lớp nhóm chưa huỷ, giờ học ngoài thời hạn đặt chỗ (5b)] | - | SD1a-F3 | Toán hạng 2; đường ngăn SD1a-F3-O2-SEP |
| SD1a-F3-O3 | Fragment | [lớp nhóm chưa huỷ, giờ học trong thời hạn đặt chỗ] | - | SD1a-F3 | Toán hạng 3; đường ngăn SD1a-F3-O3-SEP |
| SD1a-N1 | Note | Kết thúc use case (thất bại) | - | SD1a-F2 | Ghi chú đặt ở lề phải sơ đồ |
| SD1a-N2 | Note | Quay lại bước 2 | - | SD1a-F3 | Ghi chú đặt ở lề phải sơ đồ |
| SD1a-N3 | Note | Quay lại bước 2 | - | SD1a-F3 | Ghi chú đặt ở lề phải sơ đồ |
| SD1a-N4 | Note | Tiếp tục luồng chính (SD1b, bước 6) | - | SD1a-F3 | Ghi chú đặt ở lề phải sơ đồ |

c) Bảng message

| STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | SD1a-L1 | SD1a-L2 | // requestBookClass | Đồng bộ | - | 1 |
| 1.1 | SD1a-L2 | SD1a-L3 | // startBooking | Đồng bộ | - | 1 |
| 1.1.1 | SD1a-L3 | SD1a-L5 | // provideClassInfo | Đồng bộ | SD1a-F1 | 2 |
| 1.1.1 (trả về) | SD1a-L5 | SD1a-L3 | loại lớp, phòng, huấn luyện viên, giờ học | Trả về | SD1a-F1 | 2 |
| 1.1.2 | SD1a-L3 | SD1a-L2 | // showClassSchedule (loại lớp, phòng, huấn luyện viên, giờ học của từng lớp) | Đồng bộ | - | 2 |
| 2 | SD1a-L1 | SD1a-L2 | // selectClass | Đồng bộ | - | 3 |
| 2.1 | SD1a-L2 | SD1a-L3 | // bookClass (lớp nhóm đã chọn) | Đồng bộ | - | 3 |
| 2.1.1 | SD1a-L3 | SD1a-L4 | // checkBookingNotSuspended | Đồng bộ | - | 4 |
| 2.1.1 (trả về) | SD1a-L4 | SD1a-L3 | quyền đặt lớp đang bị khoá hoặc không | Trả về | - | 4 |
| 2.1.2 | SD1a-L3 | SD1a-L2 | // showBookingRejectedNotice (quyền đặt lớp đang bị khoá, BR-09) | Đồng bộ | SD1a-F2 | 4a |
| 2.1.3 | SD1a-L3 | SD1a-L5 | // checkBookable | Đồng bộ | - | 5 |
| 2.1.3 (trả về) | SD1a-L5 | SD1a-L3 | lớp đã huỷ, ngoài thời hạn đặt chỗ hoặc hợp lệ | Trả về | - | 5 |
| 2.1.4 | SD1a-L3 | SD1a-L2 | // showBookingRejectedNotice (lớp nhóm đã bị huỷ) | Đồng bộ | SD1a-F3 | 5a |
| 2.1.5 | SD1a-L3 | SD1a-L2 | // showBookingRejectedNotice (giờ học ngoài thời hạn đặt chỗ, BR-06, BR-07) | Đồng bộ | SD1a-F3-O2 | 5b |

Số message không kể message trả về: 11.

### SD1b - Luồng chính bước 6-9 và luồng 6a, 7a

a) Tên sơ đồ và luồng thể hiện: SD1b - Luồng chính bước 6-9 và luồng 6a (alt, quay lại bước 2), 7a (break, kết thúc use case; gồm 7a1 đến 7a4 và 7a2a). Trang bắt đầu bằng fragment ref tới SD1a, tiếp tục từ toán hạng "lớp nhóm chưa huỷ, giờ học trong thời hạn đặt chỗ". Luồng 7a2a (hội viên không yêu cầu vào danh sách chờ) không có hành động của hệ thống nên toán hạng chỉ có ghi chú kết thúc.

b) Bảng lifeline

| ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| SD1b-L1 | Actor | Hội viên (ACT-02) | - | - | Tác nhân chính ACT-02 |
| SD1b-L2 | Lifeline | :BookClassSpotUI | «boundary» | - | Boundary giao diện người dùng của ACT-02 |
| SD1b-L3 | Lifeline | :BookClassSpotHandler | «control» | - | Control của UC-010 |
| SD1b-L4 | Lifeline | :Member | «entity» | - | - |
| SD1b-L5 | Lifeline | :GroupClass | «entity» | - | - |
| SD1b-L6 | Lifeline | :ClassBooking | «entity» | - | Được tạo bởi message 2.1.10.1; đỉnh lifeline ngang message đó |
| SD1b-L7 | Lifeline | :Waitlist | «entity» | - | Chỉ tham gia luồng 7a |
| SD1b-F1 | Fragment | ref SD1a - luồng chính bước 1-5 | - | - | Tham chiếu tới trang SD1a |
| SD1b-F2 | Fragment | alt [hội viên đã đặt đủ số lớp tối đa trong ngày (6a)] | - | - | Operand 1 |
| SD1b-F2-O2 | Fragment | [hội viên chưa đặt đủ số lớp tối đa trong ngày] | - | SD1b-F2 | Toán hạng 2; đường ngăn SD1b-F2-O2-SEP |
| SD1b-F3 | Fragment | break [lớp nhóm đã đủ chỗ (7a)] | - | - | Operand 1 |
| SD1b-F4 | Fragment | alt [hội viên yêu cầu vào danh sách chờ (7a2)] | - | SD1b-F3 | Operand 1 |
| SD1b-F4-O2 | Fragment | [hội viên không yêu cầu vào danh sách chờ (7a2a)] | - | SD1b-F4 | Toán hạng 2; đường ngăn SD1b-F4-O2-SEP |
| SD1b-N1 | Note | Quay lại bước 2 | - | SD1b-F2 | Ghi chú đặt ở lề phải sơ đồ |
| SD1b-N2 | Note | Tiếp tục luồng chính | - | SD1b-F2 | Ghi chú đặt ở lề phải sơ đồ |
| SD1b-N3 | Note | Kết thúc use case (thành công) | - | SD1b-F4 | Ghi chú đặt ở lề phải sơ đồ |
| SD1b-N4 | Note | Kết thúc use case (thất bại) | - | SD1b-F4 | Ghi chú đặt ở lề phải sơ đồ |
| SD1b-N5 | Note | Tại lúc lưu, lớp nhóm kiểm tra lại số chỗ đã đặt còn dưới sức chứa (BR-11); lớp vừa đủ chỗ thì hội viên đến sau đi theo luồng 7a (P04 mục 8) | - | - | Ghi chú đặt ở lề phải sơ đồ |

c) Bảng message

| STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 2.1.6 | SD1b-L3 | SD1b-L4 | // checkDailyBookingLimit (lớp nhóm đã chọn) | Đồng bộ | - | 6 |
| 2.1.6 (trả về) | SD1b-L4 | SD1b-L3 | đã đủ số lớp tối đa trong ngày hoặc chưa | Trả về | - | 6 |
| 2.1.7 | SD1b-L3 | SD1b-L2 | // showBookingRejectedNotice (số lớp đã đặt trong ngày đạt mức tối đa, BR-08) | Đồng bộ | SD1b-F2 | 6a |
| 2.1.8 | SD1b-L3 | SD1b-L5 | // checkSpotAvailable | Đồng bộ | - | 7 |
| 2.1.8 (trả về) | SD1b-L5 | SD1b-L3 | còn chỗ hoặc đã đủ chỗ | Trả về | - | 7 |
| 2.1.9 | SD1b-L3 | SD1b-L2 | // showClassFullNotice | Đồng bộ | SD1b-F3 | 7a1 |
| 3 | SD1b-L1 | SD1b-L2 | // requestJoinWaitlist | Đồng bộ | SD1b-F4 | 7a2 |
| 3.1 | SD1b-L2 | SD1b-L3 | // joinWaitlist | Đồng bộ | SD1b-F4 | 7a2 |
| 3.1.1 | SD1b-L3 | SD1b-L5 | // addToWaitlist (hội viên) | Đồng bộ | SD1b-F4 | 7a3 |
| 3.1.1.1 | SD1b-L5 | SD1b-L7 | // addMember (hội viên) | Đồng bộ | SD1b-F4 | 7a3 |
| 3.1.1.1 (trả về) | SD1b-L7 | SD1b-L5 | vị trí trong danh sách chờ | Trả về | SD1b-F4 | 7a3 |
| 3.1.1 (trả về) | SD1b-L5 | SD1b-L3 | vị trí trong danh sách chờ, loại lớp, giờ học | Trả về | SD1b-F4 | 7a3 |
| 3.1.2 | SD1b-L3 | SD1b-L2 | // showWaitlistPosition (loại lớp, giờ học, vị trí trong danh sách chờ) | Đồng bộ | SD1b-F4 | 7a4 |
| 2.1.10 | SD1b-L3 | SD1b-L5 | // reserveSpot (hội viên) | Đồng bộ | - | 8 |
| 2.1.10.1 | SD1b-L5 | SD1b-L6 | // initializeBooking (hội viên, lớp nhóm) | Tạo | - | 8 |
| 2.1.10 (trả về) | SD1b-L5 | SD1b-L3 | loại lớp, phòng, huấn luyện viên, giờ học của lớp đã đặt | Trả về | - | 8 |
| 2.1.11 | SD1b-L3 | SD1b-L2 | // showBookedSpot (loại lớp, phòng, huấn luyện viên, giờ học) | Đồng bộ | - | 9 |

Số message không kể message trả về: 12. Lifeline SD1b-L1 đến SD1b-L5 đặt ở y=40; SD1b-L6 (ClassBooking) có đỉnh ngang message tạo 2.1.10.1. Do trang bắt đầu bằng fragment ref nên message đầu tiên ở y=180 thay vì y=120.

## F6. Quy tắc tương tác giữa các lớp phân tích

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-010.drawio, một trang COM1. Phạm vi là luồng chính của cả hai trang SD1a và SD1b (13 message: 1, 1.1, 1.1.1, 1.1.2, 2, 2.1, 2.1.1, 2.1.3, 2.1.6, 2.1.8, 2.1.10, 2.1.10.1, 2.1.11), giữ nguyên STT. Message của luồng 4a, 5a, 5b, 6a, 7a (2.1.2, 2.1.4, 2.1.5, 2.1.7, 2.1.9, 3, 3.1, 3.1.1, 3.1.1.1, 3.1.2) chỉ có ở sequence diagram vì MUC_CHI_TIET của hồ sơ là GON. Chiều message ghi trong nhãn link.

### a) Bảng Node

| ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| CO-ACT02 | Actor | Hội viên (ACT-02) | - | - | Tác nhân chính ACT-02 | 40 | 190 | 40 | 80 |
| CO-UI | Object | :BookClassSpotUI | «boundary» | - | Boundary giao diện người dùng | 360 | 200 | 160 | 60 |
| CO-CTRL | Object | :BookClassSpotHandler | «control» | - | Control của UC-010 | 800 | 200 | 200 | 60 |
| CO-MEM | Object | :Member | «entity» | - | Entity AC-E-Member | 400 | 440 | 160 | 60 |
| CO-GC | Object | :GroupClass | «entity» | - | Entity AC-E-GroupClass | 960 | 440 | 160 | 60 |
| CO-CB | Object | :ClassBooking | «entity» | - | Entity AC-E-ClassBooking, được tạo bởi 2.1.10.1 | 960 | 640 | 160 | 60 |

### b) Bảng Edge (link)

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message |
|---|---|---|---|---|---|
| LK-01 | CO-ACT02 | CO-UI | Link | 1: // requestBookClass (-->)<br>2: // selectClass (-->) | 1: Nguồn-->Đích; 2: Nguồn-->Đích |
| LK-02 | CO-UI | CO-CTRL | Link | 1.1: // startBooking (-->)<br>1.1.2: // showClassSchedule (<--)<br>2.1: // bookClass (-->)<br>2.1.11: // showBookedSpot (<--) | 1.1: Nguồn-->Đích; 1.1.2: Đích-->Nguồn; 2.1: Nguồn-->Đích; 2.1.11: Đích-->Nguồn |
| LK-03 | CO-CTRL | CO-GC | Link | 1.1.1: // provideClassInfo (-->)<br>2.1.3: // checkBookable (-->)<br>2.1.8: // checkSpotAvailable (-->)<br>2.1.10: // reserveSpot (-->) | 1.1.1: Nguồn-->Đích; 2.1.3: Nguồn-->Đích; 2.1.8: Nguồn-->Đích; 2.1.10: Nguồn-->Đích |
| LK-04 | CO-CTRL | CO-MEM | Link | 2.1.1: // checkBookingNotSuspended (-->)<br>2.1.6: // checkDailyBookingLimit (-->) | 2.1.1: Nguồn-->Đích; 2.1.6: Nguồn-->Đích |
| LK-05 | CO-GC | CO-CB | Link | 2.1.10.1: «create» // initializeBooking (-->) | 2.1.10.1: Nguồn-->Đích |

## F8. VOPC (View Of Participating Classes)

File diagrams/P07-class-UC-010.drawio, một trang VOPC.

### a) Bảng Node (lớp)

| ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-B-BookClassSpotUI | Class | BookClassSpotUI | «boundary» | - | selectedClass (lớp nhóm đã chọn) | // requestBookClass<br>// showClassSchedule<br>// selectClass<br>// showBookingRejectedNotice<br>// showClassFullNotice<br>// requestJoinWaitlist<br>// showWaitlistPosition<br>// showBookedSpot | 640 | 40 | 300 | 250 |
| AC-C-BookClassSpotHandler | Class | BookClassSpotHandler | «control» | - | - | // startBooking<br>// bookClass<br>// joinWaitlist | 640 | 340 | 300 | 150 |
| AC-E-Member | Class | Member | «entity» | - | bookingSuspension (Trạng thái) | // checkBookingNotSuspended<br>// checkDailyBookingLimit | 40 | 600 | 300 | 130 |
| AC-E-ClassBooking | Class | ClassBooking | «entity» | - | - | // initializeBooking | 440 | 600 | 300 | 110 |
| AC-E-GroupClass | Class | GroupClass | «entity» | - | classType (Văn bản)<br>room (Văn bản)<br>trainer (Văn bản)<br>startTime (Ngày, Giờ)<br>capacity (Số lượng)<br>status (Trạng thái) | // provideClassInfo<br>// checkBookable<br>// checkSpotAvailable<br>// reserveSpot<br>// addToWaitlist | 840 | 600 | 300 | 290 |
| AC-E-Waitlist | Class | Waitlist | «entity» | - | - | // addMember | 1240 | 600 | 300 | 110 |

### b) Bảng quan hệ (bảng Edge)

Quan hệ giữa boundary - control và control - entity ghi Loại Association, mang ghi chú "tạm thời" ở cột Nguồn, multiplicity "-" vì đặc tả không nêu; P08 và P12 quyết định dạng thiết kế. Link actor - boundary (LK-01) không vào VOPC. R-UC010-05 lấy căn cứ từ message 3.1.1.1 của SD1b vì luồng 7a không vẽ ở communication diagram. R-UC010-06 và R-UC010-07 không có link, có bằng chứng từ đặc tả. Các phép đếm chỗ đã đặt (bước 6, 7) do Member và GroupClass tự thực hiện trên các chỗ đã đặt của mình nên không có message tới ClassBooking; quan hệ R-UC010-04 và R-UC010-06 vẫn cần để biết chỗ đã đặt thuộc hội viên nào và lớp nào.

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC010-01 | AC-B-BookClassSpotUI | AC-C-BookClassSpotHandler | Association | - | - | Link LK-02 (1.1, 1.1.2, 2.1, 2.1.11); tạm thời |
| R-UC010-02 | AC-C-BookClassSpotHandler | AC-E-Member | Association | - | - | Link LK-04 (2.1.1, 2.1.6); tạm thời |
| R-UC010-03 | AC-C-BookClassSpotHandler | AC-E-GroupClass | Association | - | - | Link LK-03 (1.1.1, 2.1.3, 2.1.8, 2.1.10); tạm thời |
| R-UC010-04 | AC-E-GroupClass | AC-E-ClassBooking | Association | A 1 - B ? | - | Link LK-05 (2.1.10.1); GL-05 (chỗ đã đặt là chỗ của một lớp nhóm), BR-11 (số chỗ đã đặt không vượt sức chứa), số chỗ đã đặt của một lớp chưa chốt do Q-22 |
| R-UC010-05 | AC-E-GroupClass | AC-E-Waitlist | Association | A 1 - B ? | - | Message 3.1.1.1 của SD1b (luồng 7a, không vẽ ở communication diagram); GL-08 (danh sách chờ của một lớp nhóm); số danh sách chờ của một lớp chờ Q-84 |
| R-UC010-06 | AC-E-Member | AC-E-ClassBooking | Association | A 1 - B ? | - | Bằng chứng đặc tả, không có link: GL-05 (chỗ đã đặt do một hội viên đặt), BR-08 (đếm lớp hội viên đã đặt trong ngày); số chỗ đã đặt của một hội viên chờ Q-59, Q-60 |
| R-UC010-07 | AC-E-Waitlist | AC-E-Member | Association | - | - | Bằng chứng đặc tả, không có link: GL-08 (danh sách có thứ tự các hội viên chờ nhận chỗ), P04 luồng 7a3; số hội viên và số danh sách chờ của một hội viên chờ Q-61, Q-84 |

Điểm uốn của các cạnh trong file .drawio (toạ độ tuyệt đối, theo C7.1):

| ID cạnh | Nguồn | Đích | Điểm uốn |
|---|---|---|---|
| R-UC010-01 | AC-B-BookClassSpotUI | AC-C-BookClassSpotHandler | - |
| R-UC010-02 | AC-C-BookClassSpotHandler | AC-E-Member | (670,540); (190,540) |
| R-UC010-03 | AC-C-BookClassSpotHandler | AC-E-GroupClass | (910,550); (990,550) |
| R-UC010-04 | AC-E-GroupClass | AC-E-ClassBooking | - |
| R-UC010-05 | AC-E-GroupClass | AC-E-Waitlist | - |
| R-UC010-06 | AC-E-Member | AC-E-ClassBooking | - |
| R-UC010-07 | AC-E-Waitlist | AC-E-Member | (1390,940); (190,940) |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1, 1.1 | AC-B-BookClassSpotUI, AC-C-BookClassSpotHandler |
| 2 | 1.1.1, 1.1.1 (trả về), 1.1.2 | AC-C-BookClassSpotHandler, AC-E-GroupClass, AC-B-BookClassSpotUI |
| 3 | 2, 2.1 | AC-B-BookClassSpotUI, AC-C-BookClassSpotHandler |
| 4 | 2.1.1, 2.1.1 (trả về) | AC-C-BookClassSpotHandler, AC-E-Member |
| 4a | 2.1.2 | AC-C-BookClassSpotHandler, AC-B-BookClassSpotUI |
| 5 | 2.1.3, 2.1.3 (trả về) | AC-C-BookClassSpotHandler, AC-E-GroupClass |
| 5a | 2.1.4 | AC-C-BookClassSpotHandler, AC-B-BookClassSpotUI |
| 5b | 2.1.5 | AC-C-BookClassSpotHandler, AC-B-BookClassSpotUI |
| 6 | 2.1.6, 2.1.6 (trả về) | AC-C-BookClassSpotHandler, AC-E-Member |
| 6a | 2.1.7 | AC-C-BookClassSpotHandler, AC-B-BookClassSpotUI |
| 7 | 2.1.8, 2.1.8 (trả về) | AC-C-BookClassSpotHandler, AC-E-GroupClass |
| 7a1 | 2.1.9 | AC-C-BookClassSpotHandler, AC-B-BookClassSpotUI |
| 7a2 | 3, 3.1 | AC-B-BookClassSpotUI, AC-C-BookClassSpotHandler |
| 7a3 | 3.1.1, 3.1.1.1, 3.1.1.1 (trả về), 3.1.1 (trả về) | AC-C-BookClassSpotHandler, AC-E-GroupClass, AC-E-Waitlist |
| 7a4 | 3.1.2 | AC-C-BookClassSpotHandler, AC-B-BookClassSpotUI |
| 8 | 2.1.10, 2.1.10.1, 2.1.10 (trả về) | AC-C-BookClassSpotHandler, AC-E-GroupClass, AC-E-ClassBooking |
| 9 | 2.1.11 | AC-C-BookClassSpotHandler, AC-B-BookClassSpotUI |

Bước 7a2a không có hành động của hệ thống nên không có dòng ở bảng này.

## F10. File .drawio

| File | Trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-010.drawio | SD1a, SD1b | Sequence diagram phân tích ở F5; ID cell lifeline, fragment, toán hạng, đường ngăn, ghi chú và message theo bảng F5 |
| diagrams/P07-communication-UC-010.drawio | COM1 | Communication diagram ở F7; ID cell trùng ID bảng Node và Edge |
| diagrams/P07-class-UC-010.drawio | VOPC | VOPC ở F8; ID cell lớp là mã AC, ID cạnh là mã R-UC010-nn, nhãn multiplicity là cell con của cạnh với hậu tố -A (đầu Lớp A) và -B (đầu Lớp B) |

Cả ba file là XML không nén, có cell id="0" và id="1", toạ độ là bội số của 10 (riêng x=-1 và x=1 của nhãn multiplicity theo C7.3).

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-83 | Lịch lớp nhóm hiển thị ở bước 2 gồm những lớp nhóm nào: mọi lớp của chuỗi, chỉ lớp của một chi nhánh, hay chỉ lớp trong một khoảng ngày; lớp đã bị huỷ hoặc đã đủ chỗ có được hiển thị để chọn không? (Lọc theo chi nhánh - nêu rõ / Lọc theo khoảng ngày - nêu rõ / Mọi lớp chưa diễn ra / Khác - nêu rõ) | F2 bước 2, 5a; vòng loop ở SD1a; AC-E-GroupClass (// provideClassInfo) | UC-010 bước 2 "Hiển thị lịch các lớp nhóm để hội viên chọn lớp" và Dữ liệu ra 1 không nêu phạm vi của lịch; luồng 5a cho thấy hội viên có thể chọn lớp đã bị huỷ nhưng nguồn không nêu lớp đã huỷ có hiển thị |
| Q-84 | Danh sách chờ (GL-08) của một lớp nhóm là một đối tượng riêng tồn tại cho mỗi lớp nhóm (kể cả khi chưa có ai chờ), hay chỉ là tập các mục chờ (hội viên, lớp nhóm, thứ tự) và không có đối tượng danh sách? (Đối tượng riêng cho mỗi lớp / Chỉ là tập mục chờ / Khác - nêu rõ) | AC-E-Waitlist; R-UC010-05, R-UC010-07; F4 bước 7a3 | GL-08 định nghĩa "Danh sách có thứ tự các hội viên chờ nhận chỗ của một lớp nhóm đã đủ chỗ" và UC-010 bước 7a3 "Thêm hội viên vào danh sách chờ của lớp nhóm"; nguồn không nêu danh sách có tồn tại trước khi có người vào hay không |

Các câu hỏi đã cấp ở bước trước và làm đổi phân tích này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-03, Q-04, Q-05 (danh mục phòng, loại lớp, huấn luyện viên và sức chứa), Q-11, Q-58 (cách mở đặt chỗ, mâu thuẫn BR-06 và BR-07, mốc muộn nhất), Q-12 (điều kiện về gói tập), Q-16 (lịch lập từng tuần hay lịch mẫu), Q-20 (chỗ đã đặt và vị trí chờ của hội viên bị khoá), Q-22 (chỗ giữ riêng có tính vào số chỗ đã đặt), Q-42, Q-76 (ngưỡng và cách tính hiệu năng của NFR-01), Q-59, Q-60 (đặt trùng cùng lớp, cách tính ngày và lớp trong danh sách chờ), Q-61, Q-62 (thứ tự xếp chờ, tự vào hay chọn vào danh sách chờ), Q-73 (giờ học và giờ bắt đầu).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-010 bước 2, Dữ liệu ra 1 | Đặc tả không nêu phạm vi các lớp nhóm trong lịch hiển thị ở bước 2 (Q-83), trong khi luồng 5a giả định lớp đã bị huỷ vẫn chọn được | Khi Q-83 có câu trả lời, bổ sung phạm vi lịch vào bước 2 và Dữ liệu ra 1, rồi chạy lại P07 cho UC-010. Chưa áp dụng vì Q-83 chưa có trả lời |

## Vấn đề còn mở

Các mục Target đạt, trừ các điểm sau cần người dùng lưu ý:

- Target 12 (đạt theo MUC_CHI_TIET là GON): communication diagram chỉ gồm luồng chính. Nếu dự án chuyển sang vẽ mọi luồng thay thế thì thêm 4a, 5a, 5b, 6a, 7a (kể cả Waitlist và link GroupClass - Waitlist) vào communication diagram.
- Target 1: bước 7a2a không có hành động của hệ thống nên không có dòng ở F4, F9 và không có message; bước này có dòng ở F2 và có toán hạng ghi chú trong SD1b.
- Bước 8: GroupClass kiểm tra lại số chỗ tại lúc lưu (BR-11) và, nếu lớp vừa đủ chỗ, hội viên đi theo luồng 7a (P04 mục 8). Nhánh này chỉ ghi bằng ghi chú trong SD1b, không vẽ thêm fragment vì đã dùng đủ 3 fragment ở mức ngoài cùng của trang và luồng 7a đã vẽ ngay sau bước 7.
- A6: hai phép đếm (chỗ đã đặt của hội viên theo ngày ở bước 6, chỗ đã đặt của lớp ở bước 7) do đối tượng toàn thể (Member, GroupClass) thực hiện nội bộ trên tập chỗ đã đặt của mình, không vẽ vòng loop gửi message tới từng ClassBooking, vì ClassBooking không có dữ liệu hay hành vi nào cần cung cấp cho phép đếm. Không có lifeline nào đại diện cho tập và ClassBooking không giữ trách nhiệm cấp tập hợp.
- ClassBooking chỉ có trách nhiệm khởi tạo trong use case này (entity mỏng); hành vi huỷ, chuyển, tính vắng mặt trên chỗ đã đặt thuộc UC-011, UC-012, UC-015, UC-016 và được P08 gộp.
- Loại lớp, phòng, huấn luyện viên, sức chứa được đưa về thuộc tính của GroupClass (F3.2 dòng 7 đến 10, 18) vì use case này chỉ hiển thị hoặc so sánh. P08 quyết định tách entity Room, Trainer, ClassType hay không khi có P07 của UC-009 (Q-03, Q-04, Q-05).
- Khoá quyền đặt lớp được giữ là thuộc tính bookingSuspension của Member theo GL-23 ("Trạng thái của một hội viên"). Khoảng ngày khoá và việc nhân viên gỡ khoá (Q-43) có thể đòi hỏi một entity riêng; xem lại khi có P07 của UC-016.
- Bước 5 gộp hai kiểm tra (lớp chưa huỷ, thời hạn đặt chỗ) vào một trách nhiệm checkBookable; BR-06 và BR-07 mâu thuẫn nhau (Q-11) nên chưa xác định được điều kiện chính xác, phân tích chỉ nêu việc kiểm tra theo thời hạn đặt chỗ.
- Lớp có chủ sở hữu ở use case khác chưa có P07 và phải dùng lại mã: AC-E-GroupClass (UC-009), AC-E-Member (đã có ở UC-005, chủ sở hữu UC-003). Lớp do P07 này đặt mã lần đầu và các use case sau phải dùng lại: AC-E-ClassBooking (UC-011, UC-012, UC-015, UC-016), AC-E-Waitlist (UC-011, UC-012, UC-013).
- NFR-01 (1.500 hội viên đặt chỗ cùng lúc) không tạo lớp phân tích; cơ chế bảo đảm hiệu năng và tính đúng của BR-11 khi đặt cùng lúc thuộc P09 và P12. Ở mức phân tích, tính đúng được thể hiện bằng việc reserveSpot kiểm tra lại và tạo chỗ đã đặt trong cùng một lớp.
- Khi hiển thị lịch ở bước 2, loop lấy thông tin từng lớp nhóm vẽ một lần trong SD1a; việc chọn các lớp thuộc lịch (truy vấn theo phạm vi) không vẽ vì đặc tả không nêu (Q-83).
