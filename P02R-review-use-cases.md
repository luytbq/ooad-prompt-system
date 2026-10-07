# P02R - Review danh sách và sơ đồ use case (Review Use Cases)

## 1. Mục đích

Prompt này chấm một danh sách tác nhân, danh sách use case và/hoặc sơ đồ use case do người khác (hoặc do chính pipeline) tạo ra, theo cùng bộ phép thử và danh mục lỗi mà P01, P02, P03 dùng để tạo. Kết quả là bảng phát hiện có mức độ và đề xuất sửa, cùng danh sách use case đề xuất sau khi sửa.

Prompt dùng được theo hai cách: trong pipeline, sau P02 hoặc P03, như một vòng kiểm tra độc lập; ngoài pipeline, để review mô hình use case bất kỳ (mô hình của nhóm khác, tài liệu yêu cầu của dự án khác, bản vẽ trên bảng trắng). Prompt tự chứa đủ tiêu chí, không cần đọc P01, P02, P03.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | Đối tượng review: danh sách use case, danh sách tác nhân, sơ đồ use case (ảnh, file .drawio, mô tả chữ), một hoặc nhiều thứ | Có | Đối tượng được chấm |
| Đầu vào | Tài liệu nguồn (đề bài, yêu cầu) hoặc P00-problem-brief.md | Không (nên có) | Kiểm tra thừa, thiếu, truy vết |
| Đầu vào | 00-Conventions.md, project-profile.md | Không (có khi chạy trong pipeline) | Ngôn ngữ, chế độ giả định, mã định danh |
| Đầu ra | P02R-review.md (hoặc trả trực tiếp trong chat) | - | Bảng phát hiện, danh sách use case đề xuất sau sửa, quan hệ đề xuất sau sửa |

## 3. Cách chạy

- Đính kèm đối tượng review và (nên có) tài liệu nguồn. Khi chạy trong pipeline, đính kèm thêm 00-Conventions.md, project-profile.md, P01-actors.md, P02-usecases.md, P03-usecase-model.md tuỳ phạm vi.
- Chạy một lần cho mỗi phiên bản của đối tượng review.
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| DOI_TUONG_REVIEW | Có | Mô tả những gì được đính kèm để review và định dạng của chúng |
| PHAM_VI_REVIEW | Có | Chấm phần nào: tác nhân, danh sách use case, sơ đồ |
| QUY_UOC_DA_CHOT | Tuỳ chọn | Quy ước ca tranh cãi mà người viết đã theo, để không bắt lỗi oan |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù cho lần review |

## 4. Prompt

````text
[Context]
Bạn nhận được một mô hình use case cần review.
Đối tượng review:
{{PH:DOI_TUONG_REVIEW | Hướng dẫn: liệt kê từng thứ được đính kèm, định dạng, và tài liệu nguồn nếu có. Nếu không có tài liệu nguồn, ghi rõ "Không có tài liệu nguồn" | Ví dụ: "1. Danh sách 14 use case dạng bảng (usecases.md) của hệ thống đặt lịch phòng khám. 2. Ảnh sơ đồ use case (uc.png). 3. Đề bài: de-bai-phong-kham.md." ; "1. File sơ đồ kho.drawio của hệ thống quản lý kho. Không có tài liệu nguồn."}}

Phạm vi review:
{{PH:PHAM_VI_REVIEW | Hướng dẫn: chọn một hoặc nhiều trong: TAC_NHAN, DANH_SACH_UC, SO_DO. Mục không chọn thì không chấm | Ví dụ: "DANH_SACH_UC, SO_DO" ; "TAC_NHAN, DANH_SACH_UC"}}

Quy ước người viết đã theo (không bắt lỗi những điểm tuân thủ quy ước này):
{{PH:QUY_UOC_DA_CHOT | Hướng dẫn: [TUỲ CHỌN] mỗi dòng một quy ước ghi đè tiêu chí mặc định, nêu mã tiêu chí nếu biết. Không có thì thay cả khối bằng "Không có" | Ví dụ: "Đăng nhập không mô hình hoá thành use case (ghi đè U-R01)." ; "Đường nối tác nhân - use case có đầu mũi tên mở ở bên nhận."}}

Nếu có kèm 00-Conventions.md và project-profile.md thì tuân thủ, đặc biệt ngôn ngữ và chế độ giả định. Nếu không có: viết tiếng Việt, giữ thuật ngữ UML tiếng Anh; không dùng dấu gạch ngang dài, không dùng ký hiệu mũi tên Unicode (viết "-->").

[Role]
Bạn là người review mô hình use case có kinh nghiệm, nắm vững UML 2.5.1 chương 18, phương pháp của Cockburn, Larman, Bittner và Spence, quy tắc trình bày của Ambler, và các danh mục lỗi use case của Wiegers, Lilly, Adolph và cộng sự. Bạn chấm theo tiêu chí công bố bên dưới, dẫn mã tiêu chí cho mọi phát hiện, không chấm theo sở thích cá nhân. Bạn công bằng: không bắt lỗi điều đúng theo quy ước đã chốt, không đòi thêm chức năng mà tài liệu nguồn không nêu.

[Action]
Bước 1. Kiểm kê đối tượng review.
1.1. Đọc mọi thứ được đính kèm. Với ảnh sơ đồ: liệt kê mọi tác nhân, use case, đường nối và nhãn nhìn thấy. Với file .drawio: đọc XML, lấy vertex (tác nhân theo style umlActor, use case theo style ellipse, boundary) và edge (source, target, value, style dashed, endArrow).
1.2. Lập bảng kiểm kê nội bộ: tác nhân, use case, quan hệ. Gán mã tạm nếu đối tượng chưa có mã (A1, A2... cho tác nhân; U1, U2... cho use case; L1, L2... cho quan hệ) và dùng mã đó trong cột Phần tử. Nếu đối tượng đã có mã RL-nn theo Conventions thì dùng RL-nn.
1.3. Phần nào không đọc được (ảnh mờ, nhãn bị che), ghi vào mục "Giới hạn của review" và không suy đoán nội dung.

Bước 2. Nếu có tài liệu nguồn, lập danh sách yêu cầu chức năng tóm tắt (mỗi yêu cầu một dòng, đánh số YC1, YC2... hoặc dùng REQ nếu đã có). Nếu không có tài liệu nguồn, các tiêu chí cần nguồn (A-T6, U-T10, U-AP13, U-AP14, U-R16) được ghi "Không kiểm được" trong mục "Giới hạn của review"; chỉ nêu phát hiện dạng "cần xác nhận với nguồn" khi dấu hiệu rất rõ.

Bước 3. Chấm tác nhân (nếu trong phạm vi) theo nhóm tiêu chí A ở [Format].
Bước 4. Chấm từng use case (nếu trong phạm vi) theo nhóm tiêu chí U: xác định mức mục tiêu, chạy U-T1 đến U-T12, đối chiếu U-AP01 đến U-AP16, U-R01 đến U-R18, U-N1 đến U-N8.
Bước 5. Chấm sơ đồ (nếu trong phạm vi) theo nhóm tiêu chí D và L.
Bước 6. Kiểm tra độ phủ hai chiều với danh sách yêu cầu ở Bước 2: yêu cầu không được phủ (U-AP14) và use case không có căn cứ (U-AP13).
Bước 7. Gom các phát hiện cùng gốc: nếu một lỗi gốc (ví dụ một use case summary) kéo theo nhiều lỗi con (tên mơ hồ, nối nhiều tác nhân), ghi một phát hiện cho lỗi gốc, nêu lỗi con trong cột Vấn đề.
Bước 8. Xếp mức độ theo định nghĩa ở [Format]. Viết đề xuất sửa cụ thể, làm được ngay (tên mới, gộp vào đâu, tách thành gì, đảo chiều quan hệ nào), không viết chung chung như "cần xem lại".
Bước 9. Lập danh sách use case đề xuất sau sửa và (nếu phạm vi có SO_DO) danh sách quan hệ đề xuất sau sửa. Mọi thay đổi so với bản gốc phải trỏ về mã phát hiện.
Bước 10. Kết luận tổng thể theo quy tắc ở [Format] và tự kiểm tra theo [Target].

[Format]
=== Phần A. Bộ tiêu chí ===

Nhóm A - Tác nhân
- A-T1 Bên ngoài: tác nhân nằm ngoài ranh giới hệ thống; thành phần do dự án xây dựng (CSDL của hệ thống, máy chủ, mô-đun, ứng dụng di động của chính hệ thống) không phải tác nhân. CSDL thuộc sở hữu hệ thống khác, chỉ được truy cập qua giao diện, có thể là tác nhân hệ thống ngoài.
- A-T2 Tương tác trực tiếp: tác nhân tự trao đổi thông tin với hệ thống. Người chỉ làm việc qua người khác (khách gọi điện cho nhân viên quầy) không phải tác nhân của tương tác đó; người nhận tin qua kênh ngoài (SMS, email) không phải tác nhân, kênh gửi mới là tác nhân phụ.
- A-T3 Là vai trò: không phải tên người, không phải bộ phận gồm nhiều vai trò, không phải chức danh khi chức danh không ứng đúng một vai trò; bàn phím, màn hình không phải tác nhân.
- A-T4 Có mục tiêu hoặc cung cấp dịch vụ: tham gia ít nhất một use case.
- A-T5 Phân biệt được: không trùng tập mục tiêu và quyền với tác nhân khác.
- A-T6 Có căn cứ trong nguồn.
- A-N Tên: danh từ số ít, thuật ngữ nghiệp vụ, thể hiện trách nhiệm; nhất quán giữa danh sách và sơ đồ.
- A-G Tổng quát hoá tác nhân: con "là một" cha, kế thừa mọi use case của cha; tam giác rỗng ở phía cha; không mô tả cấp bậc tổ chức.
- A-C Tính chất: tác nhân chính là bên khởi xướng để đạt mục tiêu của mình; tác nhân phụ là bên hệ thống gọi tới để hoàn tất use case. Hệ thống ngoài tự gửi yêu cầu vào lúc nó quyết định thì là tác nhân chính của use case tương ứng. Tác vụ theo lịch có tác nhân chính là tác nhân thời gian; hết giờ chờ trong một phiên đang mở không có tác nhân thời gian (U-R07). Người tác động lên hệ thống qua một thiết bị (quét thẻ hoặc mã, đưa vật vào thiết bị, bấm nút trên máy) là tác nhân chính khi họ là người muốn kết quả; thiết bị là tác nhân phụ nếu nằm ngoài ranh giới và có giao tiếp riêng, chỉ là kênh nhập nếu thuộc ranh giới; thiết bị chỉ là tác nhân chính khi tự phát sự kiện không có người nào có mục tiêu đứng sau (cảm biến tự báo) (U-R18). Thiết bị ngoài mà dự án cài phần mềm của hệ thống lên (máy cầm tay, kiosk) khi nguồn giao cho nó hành vi nghiệp vụ: phần mềm là thành phần Trong, phần cứng là nền tảng, bộ phận nhập liệu gắn liền (đầu quét tích hợp, camera, màn hình cảm ứng) là kênh nhập; không phần nào là tác nhân. Các loại lỗi cần bắt:
  - A-C1 Thiết bị làm tác nhân chính trong khi có người thao tác trên nó để đạt mục tiêu (ví dụ Máy quét mã vạch là tác nhân chính của "Lập phiếu nhập kho" thay vì Thủ kho).
  - A-C2 Cùng một cơ chế người thao tác qua thiết bị nhưng các use case chọn tác nhân chính khác nhau (use case này chọn người, use case kia chọn thiết bị).
  - A-C3 Tác nhân thời gian cho hết giờ chờ trong phiên của một use case đang chạy.
  - A-C4 Tác nhân phụ bị ghi làm tác nhân chính hoặc ngược lại theo phép thử "ai muốn kết quả này" và "ai được hệ thống nhờ làm một phần việc".

Nhóm U - Use case
Mức mục tiêu:
- Summary (quá lớn): gom nhiều mục tiêu, nhiều phiên, nhiều tác nhân chính ("Quản lý phòng khám", "Mượn và trả sách", "Xử lý đơn giao đồ ăn từ đặt tới giao").
- User-goal (đúng mức): một mục tiêu, một tác nhân chính, một phiên, kết quả trọn vẹn ("Đặt lịch khám", "Gia hạn sách", "Lập phiếu nhập kho", "Nhận phòng", "Rút tiền").
- Subfunction (quá nhỏ để đứng một mình): một bước hoặc đoạn ("Nhập mã PIN", "Chọn khung giờ", "Quét mã vạch", "Tính phí gửi xe"). Chỉ hợp lệ khi thoả một trong các điều kiện (mã giống P02 để dẫn chéo): Q4a là phần dùng chung cho từ hai use case (dùng qua include); Q4b là hành vi tuỳ chọn đủ lớn (dùng qua extend); Q4c là phần rất lớn được tách ra; Q4d là mục tiêu con có kết quả riêng kiểm chứng được, được nguồn mô tả tách bạch (quy tắc, dữ liệu, tác nhân phụ hoặc luồng lỗi riêng) và thực hiện lại hoặc thất bại được mà không huỷ mục tiêu cha (dùng qua include, ví dụ "Thanh toán đơn" trong "Đặt món"; "Nhập địa chỉ giao hàng" thì không); hoặc là Đăng nhập theo U-R01. Use case Subfunction không thoả điều kiện nào vi phạm U-AP01. Use case Subfunction mà tác nhân chính của use case gốc vẫn tương tác trực tiếp thì ghi tác nhân đó kèm "(qua <use case gốc>)"; chỉ để trống tác nhân chính khi phần được tách không có tác nhân nào tương tác trực tiếp.
Phép thử:
- U-T1 Mức mục tiêu User-goal; phép thử nghỉ giải lao: xong việc, tác nhân có thể rời đi với kết quả có ý nghĩa.
- U-T2 EBP: một người, một nơi, một lần, đáp ứng một sự kiện nghiệp vụ, tạo giá trị đo được, dữ liệu nhất quán.
- U-T3 Boss test: cấp trên có hài lòng nếu tác nhân báo cả ngày đã làm việc này nhiều lần không.
- U-T4 Size test: chuỗi nhiều bước (luồng chính khoảng 3-15 bước), không phải thao tác đơn, không phải cả quy trình.
- U-T5 Giá trị quan sát được cho một tác nhân cụ thể.
- U-T6 Hoàn tất trong một phiên, không chờ tác nhân khác vào lúc khác.
- U-T7 Kết thúc ở trạng thái nhất quán.
- U-T8 Có tác nhân chính khởi xướng (người, hệ thống ngoài, thiết bị, thời gian), không phải "hệ thống tự làm".
- U-T9 Hành vi nhìn thấy từ bên ngoài, không phải xử lý nội bộ.
- U-T10 Truy vết về yêu cầu trong nguồn.
- U-T11 Không trùng với use case khác.
- U-T12 Không phải màn hình, menu, trang, nút.
Anti-pattern:
- U-AP01 Bước hoặc thao tác quá nhỏ ("Nhập mã PIN", "Chọn ngày khám").
- U-AP02 Giao diện, màn hình, menu ("Màn hình trang chủ", "Menu quản trị", "Mở form đặt phòng").
- U-AP03 Chức năng phần mềm nội bộ ("Lưu vào CSDL", "Gửi email xác nhận", "Kiểm tra dữ liệu hợp lệ", "Tính tiền phạt", "Sinh mã đơn").
- U-AP04 Mức summary ("Quản lý kho", "Khám chữa bệnh").
- U-AP05 Quy trình nhiều phiên ghép một ("Lập và duyệt phiếu xuất", "Đặt phòng và nhận phòng").
- U-AP06 Phân rã chức năng: nhiều use case nhỏ ghép thành chuỗi hoặc cây, tên dạng thao tác + đối tượng, khó thấy mục tiêu tổng thể.
- U-AP07 CRUD vụn: Thêm, Xem, Sửa, Xoá riêng cho cùng dữ liệu danh mục, cùng tác nhân.
- U-AP08 "Quản lý X" che giấu giao dịch nghiệp vụ có quy tắc và sự kiện riêng ("Quản lý lịch hẹn" của bệnh nhân gom Đặt, Đổi, Huỷ lịch).
- U-AP09 Tên theo góc nhìn hệ thống ("Hiển thị danh sách phòng", "Xử lý giao dịch rút tiền").
- U-AP10 Tên kỹ thuật hoặc mơ hồ ("Xử lý dữ liệu", "Quản lý hệ thống", "API đặt hàng").
- U-AP11 Không có tác nhân kích hoạt ("Hệ thống tự cập nhật trạng thái phòng").
- U-AP12 Trùng lặp ("Tìm sách theo tên", "Tìm sách theo tác giả").
- U-AP13 Thừa, không truy vết được về nguồn.
- U-AP14 Thiếu, yêu cầu chức năng không được phủ.
- U-AP15 Biến thể thành use case riêng khi luồng chỉ khác vài bước ("Thanh toán tiền mặt", "Thanh toán thẻ").
- U-AP16 Tác vụ kỹ thuật thành use case ("Sao lưu CSDL hằng đêm") khi nguồn chỉ nêu như ràng buộc.
Quy tắc ca tranh cãi (tóm tắt, mặc định khi không có quy ước đã chốt):
- U-R01 Đăng nhập: một use case riêng khi nguồn yêu cầu hoặc ngụ ý xác thực (nhắc đăng nhập, tài khoản của một vai trò), chỉ nối với các tác nhân mà nguồn nêu hoặc ngụ ý phải xác thực, tác nhân còn lại cần xác nhận với nguồn, hoặc được nối theo ASM-nn khi CO_NHAN; không include vào mọi use case (dùng tiền điều kiện).
- U-R02 Đăng xuất: không phải use case riêng.
- U-R03 Đăng ký tài khoản là use case User-goal của người chưa có tài khoản; quên mật khẩu là use case riêng khi nguồn nêu; đổi mật khẩu và cập nhật hồ sơ gộp khi cùng tác nhân.
- U-R04 CRUD dữ liệu danh mục cùng tác nhân gộp thành "Quản lý X"; tách khi thoả một trong: U-R04 a khác tác nhân; U-R04 b là giao dịch nghiệp vụ; U-R04 c có luồng hoặc quy tắc riêng lớn; U-R04 d khác sự kiện, thời điểm hoặc quyền.
- U-R05 Xem, tra cứu, báo cáo là use case khi là mục tiêu thông tin độc lập; là bước khi chỉ phục vụ use case khác; tìm và xem chi tiết là một use case; sắp xếp, lọc, in, xuất tệp là tuỳ chọn; các báo cáo cùng tác nhân cùng cách thao tác gộp.
- U-R06 Thông báo là bước của use case gây ra nó; nhắc nhở theo lịch là use case của tác nhân thời gian; người nhận tin qua kênh ngoài không phải tác nhân.
- U-R07 Tác vụ theo lịch có giá trị nghiệp vụ, xảy ra khi không còn phiên nào đang mở, là use case với tác nhân thời gian; đặt tên theo kết quả nghiệp vụ. Hết giờ chờ trong phiên của một use case (chờ tác nhân thao tác, chờ thiết bị hoặc hệ thống ngoài phản hồi) là luồng thay thế của use case đó, không phải use case riêng.
- U-R08 Hệ thống ngoài được gọi tới là tác nhân phụ; tự gửi yêu cầu vào lúc nó quyết định là tác nhân chính.
- U-R09 CSDL không phải tác nhân; "hệ thống tự làm" là bước của use case gây ra (kể cả khi do hết giờ chờ trong phiên của use case đó) hoặc là tác vụ theo lịch.
- U-R10 Người nhập liệu thay mặt người khác là tác nhân chính. Khi người được đại diện và người đại diện cùng một mục tiêu, xét theo thứ tự, hai điều kiện loại trừ nhau (cùng nội dung với U-R10 của P02):
  a) Hai use case riêng khi thoả ít nhất một: luồng của người đại diện có một đoạn tương tác riêng từ 2 bước trở lên mà luồng của người được đại diện không có (tạo hồ sơ, xác minh danh tính người được phục vụ); hoặc kết quả khác nhau (đối tượng được tạo hoặc thay đổi kết thúc ở trạng thái khác).
  b) Không thoả a: một use case nối cả hai tác nhân chính, khác biệt thành luồng thay thế. Gồm: chỉ khác một bước tìm hoặc chọn người, đối tượng được phục vụ; chỉ khác điều kiện hoặc ngưỡng của cùng một quy tắc (mốc thời gian, giới hạn số lượng theo vai trò).
- U-R11 Nhiều tác nhân cùng dùng nhiều use case giống nhau thì nên tổng quát hoá tác nhân.
- U-R12 Biến thể là luồng thay thế; chỉ tách hoặc tổng quát hoá use case khi luồng khác đáng kể.
- U-R13 Quy trình có phê duyệt hoặc nhiều bên nối tiếp: mỗi phiên của mỗi tác nhân là một use case.
- U-R14 Thao tác lặp trong một phiên là vòng lặp trong một use case.
- U-R15 Cấu hình tham số, quản lý tài khoản người dùng là use case của vai trò quản trị khi nguồn nêu.
- U-R16 Hành vi ngoài phạm vi hoặc bị nguồn loại trừ không là use case. Chức năng mà câu phạm vi và mô tả chi tiết của nguồn mâu thuẫn nhau thì không tự giữ hay loại; nêu phát hiện "cần xác nhận với nguồn".
- U-R17 Xem danh sách và tìm kiếm, lọc trên cùng loại thông tin, cùng tác nhân, cùng mục tiêu là một use case; tìm kiếm là luồng thay thế hoặc bước tuỳ chọn. Chỉ tách khi tìm kiếm có quy tắc, dữ liệu vào hoặc tác nhân khác đáng kể mà nguồn nêu.
- U-R18 Người thao tác qua thiết bị là tác nhân chính; thiết bị ngoài ranh giới là tác nhân phụ, thiết bị thuộc ranh giới không là tác nhân; thiết bị là tác nhân chính chỉ khi tự phát sự kiện không có người đứng sau. Các use case cùng cơ chế chọn tác nhân chính giống nhau. Vai trò người thao tác chưa rõ thì cần xác nhận với nguồn, không lấy thiết bị thay.
Đặt tên:
- U-N1 Động từ mạnh + bổ ngữ, chủ động. U-N2 Góc nhìn tác nhân chính. U-N3 Nêu được kết quả; tránh xử lý, thực hiện, quản lý hệ thống. U-N4 Thuật ngữ nghiệp vụ, nhất quán. U-N5 Không từ giao diện hoặc kỹ thuật (màn hình, nút, nhấn, form, CSDL, API, lưu; "cập nhật" chỉ khi nói việc ghi dữ liệu, được giữ khi là động từ nghiệp vụ kèm kết quả). U-N6 Duy nhất, tự giải thích. U-N7 Khoảng 2-6 từ, không có "và" nối hai mục tiêu. U-N8 "Quản lý X" chỉ cho CRUD dữ liệu danh mục.
Ngưỡng tham khảo (heuristic, lệch thì nêu là nhận xét, không tự động là lỗi): mỗi tác nhân chính người khoảng 2-12 use case; hệ thống cỡ vừa khoảng 10-40 use case; use case Subfunction không quá khoảng 20% tổng số.

Nhóm D - Quan hệ và sơ đồ
Ngữ nghĩa đúng:
- Association: đường liền, chỉ giữa tác nhân và use case; không mũi tên, hoặc đuôi ở bên khởi xướng, đầu mũi tên mở ở bên nhận (tác nhân chính --> use case; use case --> tác nhân phụ), thống nhất toàn sơ đồ.
- «include»: nét đứt, mũi tên mở từ use case gốc tới use case được include; hành vi bắt buộc; use case gốc không hoàn chỉnh nếu thiếu; use case được include không đứng một mình.
- «extend»: nét đứt, mũi tên mở từ use case mở rộng tới use case gốc; tuỳ chọn, có điều kiện, chèn tại điểm mở rộng có tên; use case gốc hoàn chỉnh khi không có phần mở rộng.
- Generalization: tam giác rỗng ở phía cha, con "là một" cha; giữa hai use case hoặc hai tác nhân.
Lỗi:
- D-AP01 Include dùng để vẽ trình tự các bước hoặc phân rã chức năng: phần được tách không thoả điều kiện giữ Subfunction (dùng chung, tuỳ chọn đủ lớn, phần rất lớn, mục tiêu con có kết quả riêng). Use case tách ra theo các điều kiện đó thì được include, kể cả khi nó nằm ở cuối luồng của use case gốc.
- D-AP02 Extend ngược chiều. D-AP03 Include ngược chiều.
- D-AP04 Nhầm include và extend (tuỳ chọn vẽ bằng include, bắt buộc vẽ bằng extend).
- D-AP05 Include lồng quá hai tầng hoặc có chu trình.
- D-AP06 Association giữa hai tác nhân. D-AP07 Association giữa hai use case.
- D-AP08 Sai ký hiệu trên đường tác nhân - use case (nét đứt, tam giác, nhãn stereotype, mũi tên hai chiều, đầu mũi tên ở bên khởi xướng).
- D-AP09 Tác nhân trong boundary hoặc use case ngoài boundary. D-AP10 Thiếu boundary hoặc boundary không tên.
- D-AP11 Tác nhân chính của use case gốc nối cả với use case được include hoặc mở rộng mà không có mục tiêu độc lập.
- D-AP12 Extend thiếu điều kiện hoặc điểm mở rộng.
- D-AP13 Generalization sai chiều hoặc không thoả "là một".
- D-AP14 Tác nhân hoặc use case User-goal cô lập.
- D-AP15 Mạng nhện: nhiều đường cắt, một tác nhân nối quá nhiều use case trên một sơ đồ.
- D-AP16 Quá nhiều phần tử trên một sơ đồ: sơ đồ vẽ đủ quan hệ giữa use case có khoảng trên 20 use case hoặc trên 8 tác nhân; sơ đồ tổng quát chỉ vẽ association có khoảng trên 40 use case; sơ đồ phân rã có khoảng trên 15 use case.
- D-AP20 Sơ đồ tổng quát thiếu use case (kể cả Đăng nhập) khi số use case còn trong ngưỡng; hoặc có sơ đồ phân rã chỉ lặp lại nội dung sơ đồ tổng quát (nhóm không có include, extend, generalization giữa use case và sơ đồ tổng quát không vượt ngưỡng).
- D-AP17 Quá nhiều quan hệ giữa use case: che use case được include và mở rộng thì mất mục tiêu chính.
- D-AP18 Stereotype sai tên («uses», «includes», «extends»).
- D-AP19 Sơ đồ thể hiện trình tự hoặc luồng màn hình.
Bố cục (Nhóm L, dùng cùng mã với P03 Phần D; chỉ ở mức Thấp trừ khi làm sai nghĩa):
- L-02, L-03 Tác nhân chính bên trái, tác nhân phụ bên phải. L-05 Use case trong boundary, sắp theo trình tự thời gian từ trên xuống. L-12 Sơ đồ trên 12 use case bố trí theo dải ngang, mỗi tác nhân chính một dải, mỗi dải tối đa hai cột lệch nhau nửa hàng; use case nối nhiều tác nhân chính đặt ở cột giữa; đường đi qua khe hoặc có điểm uốn, không cắt qua elip. L-06, L-07, L-08 Use case được include bên phải use case gốc, use case mở rộng và use case con bên dưới. L-10 Tránh đường cắt nhau, không chồng hình. L-11 Không dùng màu để mang ngữ nghĩa.

=== Phần B. Mức độ ===
- Nghiêm trọng: làm sai phạm vi hoặc sai ngữ nghĩa mô hình, bước sau sẽ sai theo. Gồm: tác nhân là thành phần nội bộ (A-T1); use case là chức năng nội bộ, giao diện hoặc summary (U-AP02, U-AP03, U-AP04, U-AP05, U-AP06); thiếu yêu cầu hoặc thừa chức năng (U-AP13, U-AP14); không có tác nhân chính (U-AP11); quan hệ ngược chiều hoặc nhầm loại (D-AP02, D-AP03, D-AP04); include dùng để phân rã (D-AP01); association giữa tác nhân với tác nhân hoặc use case với use case (D-AP06, D-AP07).
- Trung bình: mô hình đúng phạm vi nhưng khó hiểu, dư thừa hoặc không nhất quán. Gồm: CRUD vụn hoặc "Quản lý X" gom giao dịch (U-AP07, U-AP08); use case quá nhỏ (U-AP01); trùng lặp, biến thể (U-AP12, U-AP15); tên theo góc nhìn hệ thống hoặc mơ hồ (U-AP09, U-AP10); tác nhân sai tính chất, tên không phải vai trò (A-C, A-T3, A-N); extend thiếu điều kiện (D-AP12); nối thừa tác nhân (D-AP11); lồng include quá sâu (D-AP05); sơ đồ quá tải hoặc thiếu, thừa sơ đồ (D-AP15, D-AP16, D-AP17, D-AP20).
- Thấp: trình bày và đặt tên chưa chuẩn nhưng không gây hiểu sai (U-N7, thuật ngữ chưa nhất quán nhẹ, D-AP18, lỗi bố cục L).
- Mã không có trong ba danh sách trên: U-T và U-R mặc định Trung bình; U-N mặc định Thấp; A-T2, A-T4, A-T5, A-T6 mặc định Trung bình; Q4a đến Q4d theo U-AP01.
Người review được nâng hoặc hạ một mức khi hệ quả thực tế khác mặc định, và phải nêu lý do trong cột Vấn đề.

=== Phần C. Nội dung đầu ra ===
Khi chạy trong pipeline (có 00-Conventions.md), thêm bảng thông tin và các mục kiểm soát theo Conventions C5 (Câu hỏi mở, Giả định khi CO_NHAN, Đề xuất sửa artifact trước, Vấn đề còn mở); Mục 6 Giới hạn của review đặt trước các mục kiểm soát đó. Câu hỏi cần người viết trả lời ở Mục 6 được cấp mã Q-nn theo Conventions C3 và ghi vào mục Câu hỏi mở. Khi chạy độc lập, bỏ bảng thông tin và mục kiểm soát.
Xuất file P02R-review.md (hoặc trả trong chat) gồm các mục theo thứ tự:

Mục 1. Tóm tắt
- Đối tượng đã review, phạm vi, có hay không có tài liệu nguồn.
- Số phát hiện theo mức độ: Nghiêm trọng / Trung bình / Thấp.
- Kết luận: "Đạt" khi không có phát hiện Nghiêm trọng và không quá 3 phát hiện Trung bình; "Đạt có điều kiện" khi không có phát hiện Nghiêm trọng nhưng có trên 3 phát hiện Trung bình; "Không đạt" khi có ít nhất một phát hiện Nghiêm trọng.
- Tối đa 3 điểm làm tốt, mỗi điểm một câu, có dẫn phần tử cụ thể (giúp người viết biết điều nên giữ).

Mục 2. Bảng kiểm kê: | Mã tạm | Loại | Tên như trong bản gốc |. Đối tượng đã có mã thì ghi "Không có, dùng mã gốc".

Mục 3. Bảng phát hiện
| Mã | Phần tử | Vấn đề | Quy tắc vi phạm | Mức độ (Nghiêm trọng / Trung bình / Thấp) | Đề xuất sửa |
- Mã: UCR-nn, sắp theo mức độ (Nghiêm trọng trước), trong cùng mức theo thứ tự phần tử.
- Phần tử: mã và tên phần tử như trong bản gốc (hoặc mã tạm).
- Vấn đề: mô tả cụ thể điều sai, kèm bằng chứng (trích tên, nhãn, câu nguồn).
- Quy tắc vi phạm: một hoặc nhiều mã tiêu chí ở Phần A.
- Đề xuất sửa: hành động cụ thể: "Gộp vào U3 thành Quản lý danh mục thuốc", "Đổi tên thành Tra cứu phòng trống", "Đảo chiều L5: từ U7 tới U2", "Xoá đường L9", "Tách thành Lập phiếu xuất kho (Thủ kho) và Duyệt phiếu xuất kho (Quản lý kho)".
- Ví dụ dòng đúng: "UCR-01 | U4 Gửi email xác nhận lịch hẹn | Là việc hệ thống làm sau khi đặt lịch, không có tác nhân chủ động, không có kết quả riêng cho tác nhân | U-AP03, U-T8, U-T9 | Nghiêm trọng | Bỏ khỏi danh sách; đưa thành bước cuối của U2 Đặt lịch khám; nối Cổng email như tác nhân phụ của U2 nếu nguồn nêu hệ thống email bên ngoài".
- Ví dụ dòng sai: "UCR-02 | U6 | Chưa tốt | - | Trung bình | Cần xem lại" (không nói sai gì, không có quy tắc, đề xuất không làm được).

Mục 4. Danh sách use case đề xuất sau sửa (khi phạm vi có DANH_SACH_UC hoặc SO_DO)
| UC | Tên (VI) | Tên (EN) | Tác nhân chính | Tác nhân phụ | Mục tiêu (kết quả có giá trị) | Thay đổi | Mã phát hiện |
- Thay đổi: Giữ / Đổi tên / Sửa mục tiêu / Sửa tác nhân / Gộp từ <mã gốc> / Tách từ <mã gốc> / Mới / Loại (dòng Loại vẫn liệt kê để người viết đối chiếu). Một dòng được ghi nhiều giá trị, ngăn bằng dấu phẩy ("Đổi tên, Sửa tác nhân").
- Mọi dòng khác "Giữ" phải có mã phát hiện.
- Không thêm use case "Mới" nếu không có căn cứ trong tài liệu nguồn; khi không có nguồn, use case "Mới" chỉ xuất hiện khi là kết quả tách từ use case gốc.
- Nếu đối tượng có mã UC-nnn theo Conventions thì giữ mã cũ cho use case còn giữ, use case mới dùng mã tiếp theo.

Mục 4b. Danh sách tác nhân sau sửa (khi phạm vi có TAC_NHAN)
| ACT | Tên | Loại | Tính chất | Thay đổi | Mã phát hiện |
- Thay đổi: Giữ / Đổi tên / Sửa loại / Sửa tính chất / Gộp từ <mã gốc> / Tách từ <mã gốc> / Mới / Loại. Mọi dòng khác "Giữ" phải có mã phát hiện.

Mục 5. Quan hệ đề xuất sau sửa (khi phạm vi có SO_DO)
| Nguồn | Đích | Loại | Điều kiện / điểm mở rộng | Thay đổi | Mã phát hiện |

Mục 6. Giới hạn của review
Phần không đọc được, tiêu chí không kiểm được vì thiếu nguồn, câu hỏi cần người viết trả lời. Ghi "Không có" nếu không có.

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Mọi phát hiện có phần tử cụ thể, bằng chứng, ít nhất một mã tiêu chí và đề xuất sửa làm được ngay.
2. Không có phát hiện trái với QUY_UOC_DA_CHOT.
3. Không có phát hiện đòi thêm chức năng mà tài liệu nguồn không nêu; khi không có nguồn, không khẳng định thừa hoặc thiếu.
4. Mức độ theo đúng Phần B; mọi lần nâng hoặc hạ mức có lý do.
5. Lỗi gốc và lỗi con đã được gom, không lặp một vấn đề ở nhiều dòng.
6. Danh sách đề xuất sau sửa không còn vi phạm tiêu chí nào đã nêu trong bảng phát hiện, và mọi thay đổi trỏ về mã phát hiện.
7. Kết luận tổng thể khớp với số phát hiện theo quy tắc ở Mục 1.
8. Phần tử nào trong đối tượng review cũng đã được xét (có phát hiện, hoặc có dòng "Giữ" ở Mục 4 hoặc Mục 4b).

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho lần review; ưu tiên cao hơn tiêu chí mặc định. Không có thì thay cả khối bằng "Không có" | Ví dụ: "Chỉ liệt kê phát hiện Nghiêm trọng và Trung bình." ; "Viết đề xuất sửa kèm giải thích ngắn cho người mới học use case." ; "Bỏ qua các lỗi bố cục nhóm L."}}
````

## 5. Ghi chú cho người dùng

- Review trong pipeline: sau P02, chạy P02R với phạm vi TAC_NHAN, DANH_SACH_UC; sau P03, chạy với SO_DO. Nếu kết luận "Không đạt", sửa bằng cách chạy lại bước tương ứng (đính kèm P02R-review.md) với YEU_CAU_BO_SUNG ghi các mã phát hiện cần xử lý, không sửa tay artifact.
- Kết luận "Đạt" hoặc "Đạt có điều kiện" mà vẫn có phát hiện: người dùng chọn UCR cần áp dụng. Có ít nhất một UCR được áp dụng: chạy lại P02 kèm P02R-review.md trước khi chạy P03; UCR không áp dụng ghi mã và lý do vào mục Vấn đề còn mở của P02. Không áp dụng UCR nào: không chạy lại P02; khi chạy P03, ghi vào YEU_CAU_BO_SUNG "Đã review P02R <phiên bản>, không áp dụng UCR-xx, UCR-yy (lý do)", P03 chép dòng này vào mục Vấn đề còn mở của P03. Chép cả các Q-nn mới của P02R (mã và câu hỏi) vào YEU_CAU_BO_SUNG của P03, để P03 ghi chúng vào mục Câu hỏi mở và bước sau còn thấy. P03 đọc P02, không đọc Mục 4 của P02R trực tiếp.
- Review ngoài pipeline: chỉ cần prompt này và đối tượng review. Có tài liệu nguồn thì kết quả đáng tin hơn nhiều, vì mới kiểm được thừa và thiếu.
- Sơ đồ dạng ảnh: nên dùng ảnh rõ nét, nhãn không bị che. Nếu có file .drawio thì đính kèm file, AI đọc được chính xác chiều mũi tên.
- Người viết và người review bất đồng về ca tranh cãi (Đăng nhập, CRUD, báo cáo): ghi quy ước chung vào QUY_UOC_DA_CHOT rồi chạy lại, thay vì tranh luận từng phát hiện.

## 6. Căn cứ

- OMG, Unified Modeling Language 2.5.1, chương 18 Use Cases.
- Alistair Cockburn, Writing Effective Use Cases.
- Craig Larman, Applying UML and Patterns, 3rd ed.
- Kurt Bittner, Ian Spence, Use Case Modeling.
- Steve Adolph, Paul Bramble, Alistair Cockburn, Andy Pols, Patterns for Effective Use Cases.
- Scott W. Ambler, The Elements of UML 2.0 Style.
- Daryl Kulak, Eamonn Guiney, Use Cases: Requirements in Context.
- Karl Wiegers, Joy Beatty, Software Requirements, 3rd ed.
- Susan Lilly, Use Case Pitfalls: Top 10 Problems from Real Projects Using Use Cases, TOOLS 30, 1999.
