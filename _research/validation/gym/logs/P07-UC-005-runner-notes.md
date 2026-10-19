Model của phiên chạy: Sonnet

# Nhật ký người chạy - P07 cho UC-005 Mua hoặc gia hạn gói tập

Phạm vi đọc đã tuân thủ: prompt P07, 00-Conventions.md, README.md, project-profile.md, P04 UC-005 toàn bộ, P01 Mục 2, P02 bảng 4a, 4b, P03 Mục 1, 2, P05, P06 (các mục liên quan). Mã Q, ASM lớn nhất quét bằng công cụ trên cột Mã của mục Câu hỏi mở các artifact P00 đến P06 và đặc tả P04 (Q-80, chưa có ASM). Đầu ra: P07-uc-analysis/UC-005-purchase-or-renew-membership-package-analysis.md và ba file diagrams/P07-{sequence,communication,class}-UC-005.drawio. Cả bốn file được sinh bằng một script đặt ở thư mục tạm của phiên (một nguồn dữ liệu cho bảng .md và .drawio) để hai dạng không lệch nhau; script không nằm trong dự án.

Kết quả tự kiểm tra Target: mục 1 đạt một phần (luồng 4a, 4b, 4c, 12a của P04 chưa có hành động nên không có message, xem vướng mắc 9), các mục 2 đến 16 đạt. Cả ba file .drawio qua kiểm tra XML (python3 xml.dom.minidom), ID duy nhất trong từng trang, toạ độ bội số 10, không hai node cách nhau dưới 40 và không cạnh nào cắt node ở communication và VOPC (kiểm tra bằng script hình học, chưa mở bằng draw.io để xem). Sequence chưa kiểm tra bằng mắt.

## Vướng mắc

### 1. Tác nhân chính thứ hai dùng chung luồng: không có hướng dẫn cho sequence diagram và đánh số STT

- Vị trí: F7, "Use case có nhiều tác nhân chính dùng chung luồng (P02 U-R10 b): biến thể của tác nhân thứ hai vào cùng communication diagram, giữ STT của trang biến thể". F3.1, "một boundary cho mỗi cặp tác nhân và use case". F5 c), "Message ở trang tách riêng dùng STT của message tại điểm rẽ trong trang luồng chính, kèm hậu tố chữ thường theo mã luồng".
- Gặp: UC-005 có hai tác nhân chính người (Hội viên ACT-02, Lễ tân ACT-05) cùng đi bước 1 đến 13, mỗi người một boundary. Prompt chỉ nói communication diagram nhận "biến thể", không nói sequence diagram vẽ biến thể thế nào (trang riêng hay alt) và STT của biến thể là gì. Quy tắc hậu tố theo "mã luồng" không áp dụng được vì biến thể không có mã luồng. Tham chiếu "P02 U-R10 b" là quy tắc trong P02 mà bước này không được đọc nên người chạy không biết nội dung.
- Xử lý: vẽ biến thể Lễ tân thành trang SD2 đầy đủ (bước 1 đến 8, 8a, 8b, 11 đến 13) và tự đặt quy ước hậu tố r ở số thứ nhất (1r, 1r.1, 2r...). Ghi quy ước trong F5. Đề nghị prompt nêu rõ cách vẽ và cách đánh số biến thể tác nhân.

### 2. Giá trị MUC_CHI_TIET và "DAY_DU" không được định nghĩa trong prompt P07

- Vị trí: A6, "Khi DAY_DU: thêm mọi luồng thay thế (kể cả luồng ở trang riêng) với cùng số thứ tự theo F7"; F7, "Communication diagram cho luồng thay thế (chỉ khi DAY_DU)"; Target 12, "(chỉ khi DAY_DU)".
- Gặp: hồ sơ dự án có trường MUC_CHI_TIET = GON, nhưng prompt P07 không nói DAY_DU là giá trị của trường nào, GON có nghĩa gì với P07. Một người chạy chưa đọc template hồ sơ không suy ra được.
- Xử lý: coi GON là không phải DAY_DU, nên communication chỉ gồm luồng chính và biến thể Lễ tân, không vẽ 8a, 8b, 9a, 10a. Ghi trong F7 và Vấn đề còn mở.

### 3. Chép nguyên cột mô tả của P04 mâu thuẫn với yêu cầu dùng thuật ngữ chuẩn của P05

- Vị trí: F2, "Bước do tác nhân thực hiện chép nguyên, cột bổ sung ghi 'Không đổi'" và cột "Mô tả trong đặc tả"; YEU_CAU_BO_SUNG, "dùng thuật ngữ chuẩn của P05".
- Gặp: luồng 10a của P04 viết "giao dịch thanh toán", từ P05 (GL-12) xếp vào nhóm không dùng. Prompt không nói cột "Mô tả trong đặc tả" được chép nguyên văn hay được chuẩn hoá.
- Xử lý: cột "Mô tả trong đặc tả" chép nguyên văn P04 (có ghi chú ở đầu F2), cột bổ sung và mọi tên lớp, trách nhiệm dùng "giao dịch thu tiền". Dòng "Giao dịch thanh toán" trong bảng lọc danh từ ghi Loại - trùng với PaymentTransaction.

### 4. Quy tắc "tập hợp do control lặp" làm phình sơ đồ và không nói cách lấy tập

- Vị trí: A6, "Trách nhiệm tác động lên một tập đối tượng cùng lớp (huỷ, gom, lọc, tổng hợp) giao cho đối tượng toàn thể ... Đặc tả, BR, glossary không có đối tượng toàn thể thì control lặp và gửi message tới từng phần tử".
- Gặp: bước 2 (liệt kê các giá gói hiện hành) và bước 5 (chọn chương trình khuyến mãi áp dụng) là thao tác trên tập đối tượng chỉ đọc. Prompt liệt kê "huỷ, gom, lọc, tổng hợp", không rõ liệt kê chỉ đọc có thuộc không. Cũng không nói control lấy tập các phần tử ở đâu (truy vấn không có lớp nhận).
- Xử lý: áp dụng loop [mỗi giá gói hiện hành] và loop [mỗi chương trình khuyến mãi đang đặt], lifeline là một đối tượng đại diện; việc chọn tập không vẽ, ghi trong Vấn đề còn mở. Hai loop này cộng với các break làm chạm ngưỡng 3 fragment ở mức ngoài cùng (xem vướng mắc 5).

### 5. Ngưỡng 3 fragment mức ngoài cùng và cách tính ref

- Vị trí: F5, "Ngưỡng tách sơ đồ: một trang khoảng 30 message không kể message trả về, và tối đa 3 fragment ở mức ngoài cùng ... Riêng luồng chính đã vượt ngưỡng thì tách theo đoạn bước (SD1a bước 1-6, SD1b bước 7-13); trang sau bắt đầu bằng fragment ref tới trang trước."
- Gặp: luồng chính của UC-005 có 31 message không kể trả về, 2 loop, 2 break (9a, 10a). Không nói fragment ref đầu trang có tính vào "3 fragment" hay không, và không nói tách ở đâu khi hai đoạn bước đầu và cuối đều cần giữ break nguyên vẹn.
- Xử lý: tách thành 3 trang SD1a (bước 1-6), SD1b (bước 7-10 cùng 9a, 10a), SD1c (bước 11-13), tính ref đầu trang là một fragment ngoài cùng (SD1b có đúng 3). Nếu ref không tính thì SD1b, SD1c có thể gộp lại; kết quả vì thế phụ thuộc cách đọc.

### 6. Thời hạn nội bộ (BR-04): P04 đặt luồng 9a tại một bước, A2 chỉ nói rõ trường hợp bao trùm nhiều bước

- Vị trí: A2, "Control ghi nhận bắt đầu chờ bằng message tự gọi ... và nhận sự kiện hết hạn bằng message tự gọi có nhãn 'after(<thời hạn>)'" và "Khi thời hạn bao trùm nhiều bước (P04 ghi luồng hết hạn 'tại bất kỳ bước nào từ bước N+1 đến bước M'...)"; F5, "Không dùng opt cho luồng kết thúc".
- Gặp: P04 ghi 9a tại bước 9 (điều kiện "Hết thời hạn (BR-04) mà đơn mua chưa thanh toán thành công"), không ghi khoảng bước. Prompt không nói trường hợp một điểm có cần message dừng chờ khi nhận kết quả hay không, cũng không nói break của 9a đặt trước hay sau các message bước 10 (hai kết cục cạnh tranh nhau về thời gian: hết hạn hoặc nhận kết quả).
- Xử lý: vẽ break 9a ngay sau message bắt đầu chờ và trước message nhận kết quả bước 10 (trang SD1b), thêm message tự gọi "// stopWaitingForPayment (BR-04)" khi nhận kết quả để hết hạn không còn xảy ra sau thành công. Mốc bắt đầu tính 15 phút giữ theo Q-25 của P04. Ghi trong Vấn đề còn mở rằng nếu Q-25 hoặc Q-13 đổi thì chuyển 9a sang trang riêng.

### 7. NGHIEM_NGAT: cách mô hình hoá message mà cơ chế đang chờ Q-nn

- Vị trí: A3, "Tác nhân người chỉ tương tác qua kênh không phải màn hình (email, SMS, thông báo đẩy), ...: boundary của tác nhân đó thuộc loại 'Kênh thông báo'"; C1 mục 2 NGHIEM_NGAT, "không tự điền nội dung".
- Gặp: P04 9a2 và 10a ghi "(kênh thông báo: Q-53)", kênh chưa chọn (thông báo đẩy, SMS hay chỉ trên ứng dụng). Hội viên đã rời ứng dụng sau 15 phút, nên gửi tới boundary giao diện người dùng là một trong các lựa chọn của Q-53, tức là đã chọn. Không tạo boundary kênh thông báo cũng không đúng vì kênh chưa biết. Prompt không có hướng dẫn cho message đã biết nội dung nhưng chưa biết cơ chế.
- Xử lý: gửi message "showOrderCancelledNotice", "showPaymentFailedNotice" tới boundary giao diện người dùng của tác nhân, ghi rõ tạm thời chờ Q-53 và nêu trong Vấn đề còn mở hệ quả (thêm boundary kênh thông báo, tác nhân phụ ACT-09, ACT-10 ở P02, P03, P04 nếu Q-53 chọn thông báo đẩy hoặc SMS).

### 8. Kết cục "Chờ Q-nn" không cho biết quay lại hay kết thúc

- Vị trí: F5 b), "Luồng thay thế kết thúc use case (cột Quay lại / Kết thúc của P04 ghi 'Kết thúc') dùng break"; P04 mục 3 luồng 10a cột "Quay lại / Kết thúc" ghi "Chờ Q-13".
- Gặp: 10a (thanh toán lại hay tạo đơn mới hay kết thúc) chưa xác định, nhưng prompt chỉ có hai kiểu: break (kết thúc) và alt với note "quay lại bước K".
- Xử lý: dùng break vì dù Q-13 trả lời thế nào thì lần chạy này không tới được bước 11; ghi "kết cục sau thông báo: Q-13" trong nhãn message và Ghi chú fragment. Prompt nên có quy ước cho kết cục chưa xác định.

### 9. Luồng không có hành động (4a, 4b, 4c, 12a) và Target 1

- Vị trí: Target 1, "Mọi bước hệ thống trong luồng chính và luồng thay thế của đặc tả có trong F2, F4 và có ít nhất một message"; F2, "STT bước giữ nguyên như P04".
- Gặp: P04 có 4 luồng mà cột hành động là "-" và kết cục "Chờ Q-nn". Không có bước hệ thống nào để phân bổ, nhưng F2 vẫn phải giữ STT. Điều kiện rẽ ở bước 4 (gói cũ còn hiệu lực hay không) không thể vẽ bằng alt vì các toán hạng 4a, 4b, 4c không có message.
- Xử lý: F2 có dòng cho 4a, 4b, 4c, 12a với ô bổ sung "Đặc tả chưa có hành động nên không phân bổ", không có dòng ở F4, F9. Sequence vẽ bước 4 không điều kiện (calculateRenewalStartDate), đúng với BR-03 (nhánh duy nhất đặc tả nêu). Target 1 ghi "đạt một phần" trong Vấn đề còn mở.

### 10. Mô hình hoá hệ thống ngoài: cặp boundary và actor, số message tăng, STT phân cấp

- Vị trí: F5 b), "Actor đặt bên trái, sau đó boundary của actor, control, các entity, cuối cùng boundary hệ thống ngoài hoặc thiết bị và actor phụ ở bên phải"; F6, "Actor không nhận message ... Boundary: Được (actor của nó)"; F5 c), "STT: đánh số phân cấp 1, 1.1, 1.1.1: message con được gửi trong khi xử lý message cha".
- Gặp: bước 9 và 10 (gửi đơn cho cổng, cổng trả kết quả) và bước 12 (gửi dữ liệu sang hoá đơn điện tử) cần lifeline cho cả boundary lẫn actor phụ, mỗi trao đổi thêm 1 đến 2 message. Message "cổng trả kết quả" là actor gửi cho boundary không phải trả về của message trước, nên không có STT cha rõ ràng. Tương tự các message do control khởi phát sau điểm hợp của alt (bước 11 đến 13 trong SD2) không có message cha.
- Xử lý: collectPayment (boundary --> actor) là con của requestPayment (3.1.2.1); returnPaymentResult (actor --> boundary) đánh số cấp một (4); các message sau điểm hợp ở SD2 đánh số cấp một tiếp theo (6r, 7r...). Đây là quy ước tự đặt, prompt chưa có ví dụ cho mô hình gọi - gọi lại với hệ thống ngoài.

### 11. Chỗ chọn giữa các phương án khi dữ liệu nằm ở nhiều lớp, và Creator

- Vị trí: A6, "Khi dữ liệu nằm ở nhiều lớp: giao cho một lớp và thêm quan hệ tới lớp kia; hoặc tạo lớp mới ...; hoặc giao cho control"; "Lớp tạo ra đối tượng entity mới là lớp chứa hoặc ghi nhận nó, hoặc có dữ liệu khởi tạo nó (Creator)".
- Gặp: tính số tiền phải trả (bước 5) cần giá (PackagePrice) và mức giảm (Promotion) mà đặc tả chưa nêu quan hệ cấu trúc (Q-08, Q-09, Q-10). Creator của đơn (control có dữ liệu) và Creator của gói tập (Member ghi nhận) dẫn tới hai tiêu chí khác nhau của Creator trong cùng use case, prompt không xếp thứ tự ưu tiên.
- Xử lý: PackagePrice tính số tiền, nhận mức giảm làm tham số (không thêm quan hệ giữa hai entity); control tạo đơn vì giữ dữ liệu khởi tạo; Member tạo gói vì ghi nhận gói của mình. Lý do ghi ở F4.

### 12. Từ khoá "Hội viên" vừa là tác nhân vừa là entity, "gói tập" hai nghĩa, "Chi nhánh" không có giá trị Kết luận phù hợp

- Vị trí: A4, "Một danh từ chỉ hồ sơ hoặc bản ghi của tác nhân ... có thể là entity dù tác nhân cùng tên đã bị loại"; F3.2, danh sách giá trị cột Kết luận.
- Gặp: (a) AC-E-Member chỉ có một trách nhiệm hành vi trong UC-005 và không có thuộc tính nào; prompt cảnh báo entity thiếu trách nhiệm nhưng không nói gì về entity chỉ là chủ sở hữu. (b) "Gói tập" bước 2 là mặt hàng được bán, GL-16 lại định nghĩa là quyền sau khi mua; P05 không có từ cho mặt hàng. (c) "Chi nhánh" là khái niệm trong phạm vi có định danh nhưng use case chỉ lưu tham chiếu: không giá trị Kết luận nào khớp, vì "không tham gia hành vi" cần ghi "khái niệm của UC-nnn" mà chủ sở hữu (Q-03) chưa biết.
- Xử lý: (a) giữ Member làm Creator của gói, ghi nhận trong Vấn đề còn mở; (b) hỏi Q-82 và đề xuất sửa P05; (c) ghi "Loại - thuộc tính của MembershipPackage" kèm lý do, Q-03, Q-50.

### 13. Cột Nguồn (REQ) của F2: P04 không ghi REQ theo từng bước

- Vị trí: F2, cột "Nguồn (BR, GL, REQ)"; mục 3 bảng "Phần cần dùng", P06 "Các BR, NFR có UC_ID ở cột áp dụng".
- Gặp: P04 UC-005 chỉ ghi danh sách REQ chung ở mục 1 và REQ cho từng BR, không ghi REQ cho từng bước (ví dụ bước 8a, 8b, 1). Để điền cột Nguồn phải suy REQ từ P01 mục 2 (mục tiêu tác nhân) và P05 (cột Nguồn), cũng là phần không có trong bảng "Phần cần dùng" cho mục đích này. BR-38 (giảm tối đa 20%) áp dụng cho UC-027 ở P06 chứ không phải UC-005, nhưng cần cho thuộc tính discountRate; tôi dẫn BR-38 làm nguồn thay vì ghi "REQ-80 chưa có BR" theo YEU_CAU_BO_SUNG.
- Xử lý: dẫn REQ theo P01 và P05 (REQ-11, REQ-18, REQ-19, REQ-20, REQ-21), mức tin cậy trung bình; bước không có căn cứ ghi "-".

### 14. Mốc thời gian phụ thuộc dữ liệu (A2) so với UC-008 quét hằng ngày

- Vị trí: A2, "nếu P02 có use case do tác nhân thời gian kích hoạt tại một mốc tính từ dữ liệu của một đối tượng (ví dụ nhắc bạn đọc khi tới hạn trả sách của phiếu mượn), thì use case tạo ra mốc đó có trách nhiệm đăng ký mốc (hẹn lịch)".
- Gặp: UC-008 nhắc gia hạn đọc ngày hết hạn của gói do UC-005 tạo, tương tự ví dụ thư viện; nhưng P04 nói UC-008 do tác nhân thời gian chạy hằng ngày lúc 8 giờ theo lịch cố định và UC-005 không hẹn mốc riêng. Prompt chưa phân biệt "quét hằng ngày" với "hẹn theo mốc từng đối tượng".
- Xử lý: theo P04, không có message hẹn, hẹn lại hoặc huỷ; lý do ghi ở hàng cuối của F1. Nếu người dùng muốn theo ví dụ thư viện thì cần đổi P04 và UC-008.

### 15. Hình học .drawio: lifeline tạo bởi message Tạo, ref đầu trang, nhãn dài

- Vị trí: F10, "lifeline của đối tượng được tạo bởi message loại Tạo có đỉnh đặt ngang y của message đó ...; message đầu tiên ở y=120"; F5, "trang sau bắt đầu bằng fragment ref tới trang trước"; "lifeline ... rộng 120".
- Gặp: không nói điểm đích của mũi tên Tạo trên lifeline được tạo (tôi đặt tại cạnh trái hoặc phải của đầu lifeline, y trùng đỉnh). Trang bắt đầu bằng ref không có toạ độ chuẩn; message đầu vẫn phải ở y=120 nên ref phải nằm giữa y=80 (hết đầu lifeline) và y=120. Tên lớp như ":PurchaseOrRenewPackageHandler" dài hơn 120 và sẽ tràn; không có quy tắc rút tên hoặc ngắt dòng. Chưa mở bằng draw.io để xem bố cục thật.
- Xử lý: ref cao 30 tại y=80; lifeline Tạo như trên; nhãn giữ nguyên tên, chấp nhận tràn.

### 16. Tên control theo HAU_TO_TEN_LOP và cách lấy <TênUseCase>

- Vị trí: F3.3, "tên dạng <TênUseCase>Controller hoặc <TênUseCase>Control, theo trường HAU_TO_TEN_LOP".
- Gặp: hồ sơ dự án ghi hậu tố control là Handler, không thuộc hai dạng được liệt kê. Prompt cũng không nói <TênUseCase> lấy từ tên tiếng Anh đầy đủ ("Purchase Or Renew Membership Package", dài) hay rút gọn.
- Xử lý: theo hồ sơ, dùng Handler; rút "Membership" để tên còn PurchaseOrRenewPackageHandler (tương tự PurchaseOrRenewPackageUI) cho gọn.

### 17. Multiplicity "-" hay "?" cho quan hệ tạm thời và quan hệ có bằng chứng nhưng không có link

- Vị trí: A8, "nếu không rõ thì ghi '?' ở phía đó (F8 b) và ghi câu hỏi hoặc giả định, không đoán"; F8 b), "cả hai phía chưa rõ ghi '-'"; F8 b), "Mức phân tích: association giữa boundary và control, control và entity thường là quan hệ tạm".
- Gặp: A8 buộc mỗi "?" phải có Q hoặc ASM, còn F8 b) cho phép "-" mà không nói có cần Q. Với 10 quan hệ boundary - control - entity thì tạo Q cho từng cái là vô nghĩa.
- Xử lý: quan hệ tạm thời ghi "-", không tạo Q; hai quan hệ entity - entity có phía "?" dẫn Q có sẵn (Q-13, Q-81, Q-69); R-UC005-13 (PackageOrder - Member) không có link nhưng có bằng chứng GL-09, Dữ liệu vào 1 trường 5, nên ghi "-" và dẫn Q-01.

### 18. Quá tải ngữ cảnh và trùng lặp thông tin giữa các bảng

- Vị trí: F5, F7, F8, F9 và F3.4.
- Gặp: cùng một dữ liệu (message, lớp, trách nhiệm) xuất hiện ở F3.4, F4, F5 (bảng Node và Edge cho 4 trang), F7 (nhãn link), F8 và F9. Với 56 message, 32 lifeline, 17 link, 13 quan hệ, giữ nhất quán bằng tay trong một lượt sinh là rủi ro cao; tôi phải dùng script để sinh. Artifact dài khoảng 73 KB.
- Xử lý: sinh từ một nguồn dữ liệu; nên cân nhắc cho phép bỏ F9 khi F4 và F5 đã đủ, hoặc giới hạn F5 b) chỉ liệt kê lifeline một lần cho mọi trang.

## Mục Target không đạt hoặc đạt một phần

- Target 1: đạt một phần, lý do ở vướng mắc 9.
- Target 12: đạt trong phạm vi GON (vướng mắc 2).
- Target 14: file .drawio khớp bảng mô hình và qua kiểm tra XML; chưa kiểm tra hiển thị trong draw.io, nên bố cục (đặc biệt chồng chữ ở nhãn dài) chưa được xác nhận.
- Các mục còn lại đạt.

## Mã đã cấp

Q-81 (ghi nhận giao dịch thu tiền không thành công), Q-82 (gói tập được bán so với Giá gói). Q lớn nhất sau lần chạy: Q-82. ASM: chưa cấp. Không dùng dải mã riêng.
