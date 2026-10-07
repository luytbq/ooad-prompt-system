# P02 - Xác định use case (Identify Use Cases)

## 1. Mục đích

Bước này đi từ tài liệu nguồn và danh sách tác nhân tới danh sách use case ở đúng mức mục tiêu người dùng (user-goal): mỗi use case là một mục tiêu hoàn chỉnh của một tác nhân chính, tạo ra kết quả có giá trị quan sát được. Bước này có quy trình quyết định tường minh: lập danh sách mục tiêu tác nhân, danh sách sự kiện, sinh ứng viên, cho từng ứng viên qua bộ phép thử, rồi gộp, tách, loại và đặt tên. Mọi ứng viên, kể cả bị loại, đều được ghi lại cùng lý do.

Kết quả là đầu vào của P03 (sơ đồ use case và quan hệ), P04 (đặc tả từng use case) và mọi bước phân tích, thiết kế về sau. Danh sách use case sai mức (quá nhỏ, quá lớn, lẫn với chức năng nội bộ) là nguồn lỗi phổ biến nhất của toàn bộ mô hình.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md | Có | Luật chung |
| Đầu vào | project-profile.md | Có | Chế độ giả định, ngôn ngữ |
| Đầu vào | P00-problem-brief.md | Có (khi chạy pipeline) | Bảng REQ, phạm vi |
| Đầu vào | P01-actors.md | Có | Tác nhân, loại, tính chất, mục tiêu sơ bộ |
| Đầu vào | Tài liệu nguồn | Có | Đối chiếu câu chữ gốc |
| Đầu vào | P02R-review.md | Tuỳ chọn (khi chạy lại sau review) | Áp dụng các UCR được ghi trong YEU_CAU_BO_SUNG |
| Đầu ra | P02-usecases.md | - | Danh sách mục tiêu tác nhân, danh sách sự kiện, bảng ứng viên, bảng use case, ma trận truy vết |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, P00-problem-brief.md, P01-actors.md, tài liệu nguồn.
- Chạy một lần cho toàn hệ thống. Với hệ thống rất lớn có thể chạy theo từng phân hệ bằng placeholder PHAM_VI_LAN_CHAY; khi đó mã UC và CAND phải nối tiếp các lần chạy trước.
- Chạy lại khi P00 hoặc P01 thay đổi; giữ nguyên mã đã cấp, phần tử bị loại vẫn giữ mã và ghi "Loại".
- Chạy lại sau review: chỉ khi có ít nhất một UCR được áp dụng. Đính kèm thêm P02-usecases.md hiện có và P02R-review.md, ghi trong YEU_CAU_BO_SUNG các mã UCR cần áp dụng (ví dụ "Áp dụng UCR-01, UCR-03; không áp dụng UCR-02"). UCR không áp dụng ghi mã và lý do vào mục Vấn đề còn mở của P02. Khi không áp dụng UCR nào, không chạy lại P02; ghi quyết định vào YEU_CAU_BO_SUNG của P03 (xem P02R mục 5).
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| PHAM_VI_LAN_CHAY | Tuỳ chọn | Giới hạn lần chạy vào một phân hệ và mã bắt đầu |
| QUY_UOC_DA_CHOT | Tuỳ chọn | Các ca tranh cãi mà dự án đã chốt cách xử lý (đăng nhập, CRUD, báo cáo...) |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Đọc theo thứ tự: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md, P00-problem-brief.md (bảng REQ, phạm vi), P01-actors.md (tác nhân đã chốt), rồi tài liệu nguồn.
Nếu có P02-usecases.md cũ và P02R-review.md đi kèm thì đây là lần chạy lại sau review: giữ mọi mã UC, CAND, EV, Q, ASM; chỉ áp dụng các UCR ghi trong Yêu cầu bổ sung, cùng các sửa hệ quả để artifact nhất quán; chép các Q-nn do P02R cấp vào mục Câu hỏi mở (giữ mã, cột Nguồn gây mơ hồ ghi "P02R"); tăng phiên bản; ghi các phần tử đã đổi theo từng UCR vào mục "Thay đổi so với phiên bản trước" (Mục 7). UCR không áp dụng ghi mã và lý do vào mục Vấn đề còn mở.
Nếu không có P00-problem-brief.md, dùng trực tiếp tài liệu nguồn và thay mã REQ bằng trích dẫn ngắn trong ngoặc kép kèm vị trí. Nếu không có P01-actors.md, dừng lại và yêu cầu chạy P01 trước, trừ khi yêu cầu bổ sung cho phép tự xác định tác nhân (khi đó áp dụng tóm tắt: tác nhân là vai trò bên ngoài ranh giới, tương tác trực tiếp, có mục tiêu hoặc cung cấp dịch vụ, có căn cứ trong nguồn).

Phạm vi lần chạy:
{{PH:PHAM_VI_LAN_CHAY | Hướng dẫn: [TUỲ CHỌN] chạy toàn hệ thống thì thay cả khối bằng "Không có". Nếu chỉ chạy một phân hệ, ghi tên phân hệ, các REQ thuộc phân hệ, mã UC và CAND bắt đầu | Ví dụ: "Phân hệ đặt lịch, REQ-01 đến REQ-18, bắt đầu từ UC-001 và CAND-01" ; "Phân hệ xuất kho, REQ-30 đến REQ-52, bắt đầu từ UC-021 và CAND-40"}}

Các quy ước đã chốt cho ca tranh cãi (ghi đè quy tắc mặc định U-R tương ứng):
{{PH:QUY_UOC_DA_CHOT | Hướng dẫn: [TUỲ CHỌN] mỗi dòng một quy ước, nêu mã quy tắc U-R bị ghi đè nếu biết. Dùng mặc định thì thay cả khối bằng "Không có" | Ví dụ: "U-R01: không mô hình hoá Đăng nhập thành use case, chỉ ghi là tiền điều kiện." ; "U-R04: tách riêng Thêm sách và Xoá sách vì hai thao tác do hai vai trò khác nhau thực hiện." ; "U-R05: mỗi báo cáo tài chính là một use case riêng."}}

[Role]
Bạn là chuyên gia phân tích yêu cầu, thành thạo mô hình use case theo UML 2.5.1, phương pháp mục tiêu của Cockburn (goal levels), các phép thử của Larman (EBP, Boss test, Size test) và danh mục lỗi use case của Wiegers, Lilly, Adolph và cộng sự. Bạn nhìn hệ thống từ bên ngoài, qua con mắt tác nhân: use case là việc tác nhân muốn đạt được, không phải việc phần mềm làm bên trong. Bạn chỉ dựa vào tài liệu nguồn.

[Action]
Thực hiện tuần tự các bước sau. Mỗi bước có đầu ra trung gian được ghi vào artifact theo [Format].

Bước 1. Lập danh sách mục tiêu tác nhân (actor-goal list).
1.1. Với mỗi tác nhân Chính (và Chính và phụ) trong P01, đọc mọi REQ liên quan và trả lời:
  a) Tác nhân muốn đạt được điều gì bằng hệ thống? Vì sao họ dùng hệ thống?
  b) Tác nhân có tạo, lưu, thay đổi, xoá hoặc đọc dữ liệu nào trong hệ thống không? Nếu có, để đạt mục tiêu nghiệp vụ gì?
  c) Tác nhân có cần báo cho hệ thống biết về sự kiện hoặc thay đổi bên ngoài không?
  d) Tác nhân có cần được hệ thống báo về điều gì xảy ra bên trong không? (câu trả lời có thể là một use case xem hoặc là bước của use case khác, xét ở Bước 5)
1.2. Mỗi mục tiêu ghi một dòng, kèm mức mục tiêu dự kiến (Summary / User-goal / Subfunction) theo định nghĩa ở [Format] mục "Mức mục tiêu".
1.3. Mục tiêu Summary được ghi lại để làm khung, sau đó phân rã thành các mục tiêu User-goal thành phần (mỗi phiên làm việc của một tác nhân là một mục tiêu).

Bước 2. Lập danh sách sự kiện (event list).
2.1. Sự kiện nghiệp vụ: điều gì xảy ra ngoài hệ thống khiến một tác nhân người tìm tới hệ thống (khách muốn đặt bàn, hàng về tới kho, bạn đọc mang sách tới trả).
2.2. Sự kiện thời gian: thời điểm hoặc chu kỳ mà nguồn nêu hệ thống phải làm gì đó (cuối ngày, 24 giờ trước giờ hẹn, ngày đầu tháng, 24 giờ sau khi đặt phòng mà khách chưa đặt cọc). Hết giờ chờ trong một phiên đang mở của UC (chờ tác nhân thao tác, chờ thiết bị hoặc hệ thống ngoài phản hồi) vẫn ghi là sự kiện thời gian nhưng phản hồi của nó là luồng thay thế của UC đó (U-R07).
2.3. Sự kiện từ hệ thống ngoài hoặc thiết bị: hệ thống ngoài tự gửi dữ liệu hoặc yêu cầu tới hệ thống (ERP gửi danh mục hàng mới, ngân hàng báo đã nhận chuyển khoản), thiết bị tự phát tín hiệu (cảm biến báo chỗ đỗ trống). Tín hiệu thiết bị phát ra do một người thao tác trên thiết bị (thủ kho quét mã, tài xế quẹt thẻ tại barrier) là sự kiện Nghiệp vụ của người đó, nguồn phát là người đó (U-R18).
2.4. Với mỗi sự kiện ghi: nguồn phát (ACT; "-" với sự kiện thời gian trong phiên của một UC), phản hồi mong đợi của hệ thống, REQ. Mỗi sự kiện cần một phản hồi; phản hồi đó hoặc là một use case, hoặc là một phần của use case, hoặc bị loại có lý do.
Chỉ ghi sự kiện mà nguồn nêu hoặc suy ra trực tiếp từ câu chữ của nguồn.

Bước 3. Sinh ứng viên use case.
Gộp mọi mục tiêu ở Bước 1, mọi phản hồi ở Bước 2, và thêm các ứng viên từ phân tích động từ: đọc từng REQ chức năng, lấy mỗi cụm động từ mà chủ thể là tác nhân hoặc là hệ thống ("hệ thống gửi", "hệ thống tính") thành một ứng viên. Cố ý sinh dư: ứng viên quá nhỏ, quá lớn, trùng lặp sẽ được lọc ở bước sau. Gán mỗi ứng viên mã CAND-nn và ghi nguồn phát hiện (Mục tiêu / Sự kiện / Động từ).

Bước 4. Chuẩn hoá nhanh.
Gom các ứng viên cùng nghĩa (cùng tác nhân, cùng kết quả, khác từ ngữ) vào một dòng: giữ ứng viên đầu, các ứng viên còn lại kết luận "Gộp vào" (khi ứng viên đầu thành UC) và lý do "trùng nghĩa".

Bước 5. Cho từng ứng viên qua cây quyết định. Đi theo đúng thứ tự câu hỏi; dừng ở câu hỏi đầu tiên cho kết luận.
Ngoại lệ ưu tiên: nếu ứng viên thuộc một ca tranh cãi có quy tắc U-R ở [Format] phần B (đăng nhập, đăng xuất, tài khoản, CRUD, xem và báo cáo, thông báo, tác vụ theo lịch, hệ thống ngoài, người đại diện, biến thể, phê duyệt, thao tác lặp, cấu hình, ngoài phạm vi, xem danh sách và tìm kiếm, người thao tác qua thiết bị), áp dụng quy tắc U-R đó trước và lấy kết luận của nó; quy tắc U-R ưu tiên hơn cây quyết định. Ví dụ: Đăng nhập là Subfunction nhưng được giữ theo U-R01, không đi qua Q4.
Q1. Ứng viên có phải hành vi quan sát được từ bên ngoài, có ít nhất một tác nhân trao đổi thông tin với hệ thống không?
  - Không (xử lý nội bộ: lưu, kiểm tra hợp lệ, tính toán, sinh mã, ghi nhật ký, đồng bộ nội bộ, "hệ thống tự..." mà không có sự kiện thời gian hay tác nhân kích hoạt): nếu nó xảy ra trong một ứng viên khác thì kết luận "Là bước của UC-nnn"; nếu không thuộc ứng viên nào thì "Loại" (thường là yêu cầu phi chức năng hoặc quy tắc nghiệp vụ, ghi để P06 xử lý). Phép thử không đạt: U-T9.
  - Có: sang Q2.
Q2. Ứng viên có phải là mô tả giao diện (màn hình, menu, trang, nút, biểu mẫu, hộp thoại) không?
  - Có: tìm mục tiêu nghiệp vụ mà giao diện đó phục vụ; kết luận "Là bước của UC-nnn" hoặc "Gộp vào UC-nnn". Phép thử không đạt: U-T12.
  - Không: sang Q3.
Q3. Mức mục tiêu là gì (theo định nghĩa ở [Format])?
  - Summary: kết luận "Tách thành CAND-xx, CAND-yy..." và bổ sung các ứng viên User-goal thành phần nếu chưa có. Phép thử không đạt: U-T1, U-T6.
  - Subfunction: sang Q4.
  - User-goal: sang Q5.
Q4. Ứng viên Subfunction có đủ điều kiện đứng thành use case riêng không? Chỉ giữ khi thoả ít nhất một điều kiện sau, và mọi điều kiện đều có căn cứ trong nguồn:
  a) Là một đoạn tương tác liền mạch (thường từ 3 bước trao đổi trở lên) được dùng lặp lại trong từ hai use case User-goal trở lên (ứng viên cho quan hệ include ở P03).
  b) Là hành vi tuỳ chọn hoặc ngoại lệ có điều kiện, đủ lớn (thường từ 3 bước trở lên) hoặc được nguồn mô tả như một dịch vụ riêng có thể bổ sung sau (ứng viên cho quan hệ extend ở P03).
  c) Là phần rất lớn của một use case User-goal khiến use case đó vượt ngưỡng kích thước (ứng viên tách ra để dễ quản lý).
  d) Là một mục tiêu con bên trong một use case User-goal, đồng thời thoả cả ba vế: có kết quả riêng kiểm chứng được; được nguồn mô tả tách bạch (có quy tắc, dữ liệu, tác nhân phụ hoặc luồng lỗi riêng); có thể thực hiện lại hoặc thất bại độc lập mà không huỷ toàn bộ mục tiêu cha (ứng viên cho quan hệ include ở P03, UC gốc là use case chứa nó). Điều kiện này không phụ thuộc số bước ước lượng.
     Ví dụ đúng: "Thanh toán đơn" trong "Đặt món" của hệ thống giao đồ ăn, khi nguồn nêu phương thức thanh toán, cổng thanh toán và trường hợp thanh toán bị từ chối. Kết quả riêng là khoản tiền đã được cổng thanh toán xác nhận; thanh toán thất bại thì khách chọn phương thức khác và thanh toán lại, đơn đang đặt không bị huỷ.
     Ví dụ sai: "Nhập địa chỉ giao hàng" trong "Đặt món". Không có kết quả riêng ngoài dữ liệu cho bước sau, nguồn không mô tả nó như một phần tách bạch; kết luận "Là bước của UC-nnn" (UC Đặt món).
  - Thoả: "Giữ thành UC-nnn", cột Mức ghi "Subfunction", nêu trong Mô tả ngắn điều kiện a, b, c hoặc d.
  - Không thoả: "Là bước của UC-nnn". Phép thử không đạt: U-T1, U-T4.
Q5. Chạy bộ phép thử U-T1 đến U-T11 (định nghĩa ở dưới). Ghi mọi phép thử không đạt.
  - Đạt tất cả: sang Bước 6 với kết luận tạm "Giữ".
  - Không đạt: áp dụng hành động tương ứng trong bảng anti-pattern U-AP ở [Format] (gộp, tách, là bước của, loại).

Bộ phép thử use case (áp dụng ở Q5; P02R dùng lại cùng mã):
  U-T1 Mức mục tiêu: là mục tiêu User-goal của tác nhân chính. Phép thử nghỉ giải lao: sau khi hoàn tất, tác nhân có thể rời đi với cảm giác đã xong một việc có ý nghĩa không? "Đã đặt được lịch khám" thì có; "đã chọn được bác sĩ" thì chưa.
  U-T2 EBP (elementary business process): một người, ở một nơi, trong một lần, đáp ứng một sự kiện nghiệp vụ, tạo giá trị nghiệp vụ đo được và để dữ liệu ở trạng thái nhất quán.
  U-T3 Boss test: nếu cấp trên hỏi "Hôm nay làm được gì?" và tác nhân trả lời bằng tên ứng viên, cấp trên có hài lòng không? "Nhập 30 phiếu nhập kho" thì hài lòng; "Đăng nhập" hay "Chọn kho" thì không.
  U-T4 Size test: ứng viên là một chuỗi nhiều bước trao đổi, không phải một thao tác đơn. Luồng chính dự kiến khoảng 3-15 bước (xem mức hợp lý ở [Format]). Dưới 3 bước thường là bước hoặc subfunction; trên 15 bước hoặc có nhiều điểm dừng chờ tác nhân khác thường là summary.
  U-T5 Giá trị quan sát được: có một tác nhân cụ thể nhận kết quả có giá trị mà họ nhận ra được (có lịch hẹn, có thông tin cần tra, phiếu được duyệt, tiền được rút). Kết quả chỉ hệ thống thấy (một bản ghi được tạo mà không ai cần) không tính.
  U-T6 Một phiên: hoàn tất được trong một phiên làm việc liên tục của tác nhân chính, không phải chờ một tác nhân khác hành động vào lúc khác (nhiều giờ, nhiều ngày) mới kết thúc.
  U-T7 Trạng thái nhất quán: khi kết thúc (thành công hoặc thất bại), hệ thống ở trạng thái nhất quán; không để dữ liệu nửa vời phải có use case khác hoàn tất mới đúng.
  U-T8 Có tác nhân chính: có đúng một tác nhân chính khởi xướng mỗi lần thực hiện (có thể có nhiều tác nhân được phép khởi xướng, xem U-R10), là người, hệ thống ngoài, thiết bị hoặc thời gian; không phải "hệ thống".
  U-T9 Hành vi bên ngoài: mô tả điều tác nhân làm cùng hệ thống, không phải xử lý nội bộ của phần mềm.
  U-T10 Truy vết: truy vết được về ít nhất một REQ chức năng hoặc câu nguồn; không phải chức năng thêm theo kinh nghiệm.
  U-T11 Độc lập và không trùng: không có use case khác với hành vi hoặc luồng sự kiện gần như giống hệt; không phụ thuộc vào việc use case khác đang chạy.
  U-T12 Không phải giao diện: không phải tên màn hình, menu, trang, nút.

Bước 6. Rà lại toàn bộ ứng viên với các quy tắc ca tranh cãi U-R01 đến U-R18 (ở [Format] phần B) để chắc không ứng viên nào thuộc ca tranh cãi mà bị bỏ sót ở Bước 5. Nếu QUY_UOC_DA_CHOT ghi đè một quy tắc thì theo quy ước đó. Ghi mã quy tắc đã áp dụng vào cột Lý do của ứng viên.

Bước 7. Gộp, tách, loại lần cuối trên các ứng viên "Giữ".
7.1. Gộp khi: cùng tác nhân chính, cùng mục tiêu, chỉ khác dữ liệu hoặc khác lựa chọn nhỏ (các lựa chọn trở thành luồng thay thế ở P04); hoặc thuộc nhóm CRUD dữ liệu danh mục theo U-R04.
7.2. Tách khi: một ứng viên có nhiều tác nhân chính với mục tiêu khác nhau; có nhiều phiên tách rời; có các thao tác mang quy tắc nghiệp vụ riêng lớn; vượt ngưỡng kích thước.
7.3. Loại khi: không truy vết được (U-T10), ngoài phạm vi theo P00, hoặc là yêu cầu phi chức năng.
7.4. Sau mỗi thay đổi, cập nhật cột Kết luận để mọi ứng viên có đúng một kết luận cuối cùng, và mọi "Gộp vào", "Là bước của" trỏ tới một UC đang tồn tại.

Bước 8. Đặt tên theo quy tắc U-N1 đến U-N8 ở [Format]. Kiểm tra từng tên với danh sách từ cấm.

Bước 9. Hoàn thiện bảng use case.
9.1. Cấp mã UC-nnn theo thứ tự: nhóm chức năng, trong nhóm theo trình tự thời gian nghiệp vụ (việc xảy ra trước đánh số trước). Nhóm chứa use case khởi đầu quy trình nghiệp vụ chính được đánh số trước; các nhóm còn lại theo thứ tự xuất hiện trong nguồn. Quy trình nghiệp vụ chính là quy trình tạo ra giá trị cốt lõi cho tác nhân chính quan trọng nhất (tác nhân người có nhiều UC User-goal nhất; nếu hoà thì chọn tác nhân gắn với mục tiêu nghiệp vụ đầu tiên ở P00 mục 1). Nhóm chứa điều kiện tiên quyết của quy trình đó (đăng ký tài khoản, đăng ký thành viên) đánh số trước nhóm quy trình. Chỉ tính UC mà chính tác nhân chính đó phải làm trước; dữ liệu do tác nhân khác chuẩn bị (lịch làm việc của bác sĩ, thực đơn của nhà hàng) không làm nhóm chứa nó được đánh số trước.
9.2. Điền đủ các cột theo [Format]; xác định tác nhân phụ bằng cách hỏi "trong use case này hệ thống cần gọi tới ai hoặc cái gì bên ngoài?".
9.3. Chia nhóm chức năng theo [Format] cột Nhóm chức năng.

Bước 10. Truy vết và kiểm tra ngưỡng.
10.1. Lập ma trận REQ chức năng (và REQ loại Giao tiếp ngoài có hành vi) tới UC. Mọi REQ phải được phủ; REQ không phủ phải có lý do (ngoài phạm vi, là yêu cầu phi chức năng, là quy tắc nghiệp vụ gắn với UC-nnn, chờ Q-nn).
10.2. Mọi tác nhân trong P01 phải tham gia ít nhất một UC; nếu không, ghi vào "Đề xuất sửa artifact trước" (bước P01).
10.3. Đếm số UC trên mỗi tác nhân chính và tổng số UC, so với mức hợp lý ở [Format]; lệch ngưỡng thì rà lại ứng viên theo U-AP liên quan, rồi ghi nhận xét vào mục "Thống kê".

Bước 11. Chạy checklist [Target], sửa những mục chưa đạt; mục không sửa được ghi vào "Vấn đề còn mở".

[Format]
Xuất một file P02-usecases.md theo khung chung Conventions C5, gồm các mục theo thứ tự dưới đây. Không thêm lời dẫn.

=== Phần A. Định nghĩa dùng cho mọi mục ===

Use case: một tập các chuỗi hành động mà hệ thống thực hiện, tạo ra một kết quả có giá trị quan sát được cho một tác nhân cụ thể. Use case mô tả một cuộc đối thoại trọn vẹn giữa tác nhân và hệ thống, gom đủ mọi cách (thành công, thay thế, thất bại) để đạt một mục tiêu. Use case không phải là một chức năng của phần mềm, không phải một màn hình, không phải một bước.

Mức mục tiêu (goal level):
- Summary (quá lớn để là một use case): gom nhiều mục tiêu User-goal, thường kéo dài nhiều phiên, nhiều ngày, nhiều tác nhân chính. Dấu hiệu: tên là tên cả một quy trình hoặc cả một phân hệ; có "và" nối hai hành động của hai thời điểm; có chờ đợi tác nhân khác.
  Ví dụ (đều quá lớn): "Quản lý phòng khám"; "Khám chữa bệnh" (gồm đặt lịch, tiếp đón, khám, thanh toán); "Mượn và trả sách"; "Xử lý đơn giao đồ ăn từ lúc đặt đến lúc giao"; "Vận hành kho"; "Lưu trú tại khách sạn" (đặt phòng, nhận phòng, trả phòng).
- User-goal (đúng mức): một mục tiêu của một tác nhân chính, hoàn tất trong một phiên, thường vài phút đến dưới nửa giờ, tác nhân có thể rời đi với kết quả trọn vẹn.
  Ví dụ đúng: "Đặt lịch khám", "Huỷ lịch khám", "Cho mượn sách", "Gia hạn sách", "Đặt món", "Nhận đơn giao" (tài xế), "Lập phiếu nhập kho", "Duyệt phiếu xuất kho", "Nhận phòng", "Trả phòng", "Rút tiền", "Thanh toán phí gửi xe".
- Subfunction (quá nhỏ để đứng một mình, trừ ngoại lệ ở Q4): một bước hoặc một đoạn trong use case User-goal, tự nó không đem lại kết quả trọn vẹn.
  Ví dụ (quá nhỏ): "Nhập mã PIN", "Chọn khung giờ" (quá nhỏ khi chỉ một UC dùng; được giữ thành UC dùng chung theo Q4 a khi từ hai UC cùng dùng đoạn tương tác đó), "Chọn món vào giỏ", "Quét mã vạch hàng", "Kiểm tra thẻ bạn đọc", "Tính phí gửi xe", "Xem chi tiết phòng".

Bảng anti-pattern (dấu hiệu nhận biết, phép thử không đạt, hành động):
| Mã | Tên | Dấu hiệu | Ví dụ sai | Hành động |
|---|---|---|---|---|
| U-AP01 | Bước hoặc thao tác (quá nhỏ) | Tên là một hành động đơn của tác nhân; dưới 3 bước; không có kết quả trọn vẹn | "Nhập mã PIN", "Chọn ngày khám", "Nhập số lượng hàng" | Là bước của UC-nnn |
| U-AP02 | Thao tác giao diện, màn hình, menu | Có từ: màn hình, trang, menu, nút, nhấn, mở, form, tab, pop-up | "Màn hình trang chủ", "Menu quản trị", "Mở form đặt phòng", "Nhấn nút Tìm" | Là bước của, hoặc Gộp vào UC phục vụ mục tiêu tương ứng |
| U-AP03 | Chức năng phần mềm nội bộ | Chủ thể là "hệ thống"; động từ kỹ thuật: lưu, ghi, cập nhật CSDL, kiểm tra hợp lệ, tính, sinh mã, gửi email, đồng bộ, mã hoá | "Lưu thông tin lịch hẹn vào CSDL", "Gửi email xác nhận", "Kiểm tra số lượng tồn", "Tính tiền phạt", "Sinh mã đơn" | Là bước của UC-nnn; nếu độc lập với mọi UC thì xét U-R07 hoặc Loại (chuyển P06) |
| U-AP04 | Mức summary (quá lớn) | Tên của cả quy trình hoặc phân hệ; nhiều tác nhân chính; nhiều phiên | "Quản lý kho", "Xử lý đơn hàng", "Khám chữa bệnh" | Tách thành các UC User-goal |
| U-AP05 | Quy trình nhiều phiên ghép một | Có "và" nối hai việc ở hai thời điểm; có chờ phê duyệt, chờ giao hàng | "Mượn và trả sách", "Lập và duyệt phiếu xuất", "Đặt phòng và nhận phòng" | Tách theo mỗi phiên của mỗi tác nhân chính |
| U-AP06 | Phân rã chức năng | Nhiều UC nhỏ nối nhau thành cây hoặc chuỗi; tên dạng "thao tác + đối tượng"; nhiều UC không có kết quả giá trị; khó hiểu mô hình tổng thể | "Nhập thông tin xe", "Chọn chỗ đỗ", "In vé", "Xác nhận vào bãi" là bốn UC | Hỏi "tác nhân muốn đạt điều gì?", gom thành một UC ("Gửi xe vào bãi") |
| U-AP07 | CRUD vụn | Bốn UC Thêm, Xem, Sửa, Xoá cho cùng một dữ liệu danh mục, cùng tác nhân | "Thêm thuốc", "Sửa thuốc", "Xoá thuốc", "Xem thuốc" | Gộp thành "Quản lý X" theo U-R04 |
| U-AP08 | "Quản lý X" che giấu giao dịch nghiệp vụ | "Quản lý X" gom các giao dịch có quy tắc riêng, sự kiện riêng, hoặc của nhiều tác nhân | "Quản lý lịch hẹn" của bệnh nhân gom Đặt, Đổi, Huỷ lịch; "Quản lý đơn" gom Đặt món và Huỷ đơn | Tách theo U-R04 |
| U-AP09 | Tên theo góc nhìn hệ thống | Động từ là việc hệ thống làm: hiển thị, nhận, xử lý, cung cấp | "Hiển thị danh sách phòng trống", "Nhận yêu cầu đặt món", "Xử lý giao dịch rút tiền" | Đổi sang góc nhìn tác nhân: "Tra cứu phòng trống", "Đặt món", "Rút tiền" |
| U-AP10 | Tên kỹ thuật hoặc mơ hồ | Động từ yếu (xử lý, thực hiện, quản lý chung chung), tên công nghệ, viết tắt nội bộ | "Xử lý dữ liệu", "Thực hiện nghiệp vụ", "Quản lý hệ thống", "API đặt hàng", "CRUD kho" | Đặt lại theo U-N1 đến U-N8 |
| U-AP11 | Không có tác nhân kích hoạt | "Hệ thống tự động..." không có sự kiện thời gian, không có tác nhân | "Hệ thống tự cập nhật trạng thái phòng" | Là bước của UC gây ra thay đổi, hoặc áp dụng U-R07 nếu có lịch |
| U-AP12 | Trùng lặp | Hai UC cùng tác nhân, cùng kết quả, luồng gần giống | "Tìm sách theo tên" và "Tìm sách theo tác giả" | Gộp; khác biệt thành luồng thay thế |
| U-AP13 | Thừa (không truy vết) | Không có REQ; thêm theo thói quen hệ thống cùng loại | "Đánh giá tài xế" khi nguồn không nêu | Loại |
| U-AP14 | Thiếu (REQ không được phủ) | REQ chức năng không có UC nào phủ | Nguồn nêu "thủ kho kiểm kê định kỳ" nhưng không có UC kiểm kê | Bổ sung ứng viên |
| U-AP15 | Biến thể thành UC riêng | Các UC chỉ khác phương thức, kênh, loại dữ liệu nhưng cùng mục tiêu và luồng | "Thanh toán bằng tiền mặt", "Thanh toán bằng thẻ" khi luồng chỉ khác một bước | Gộp; biến thể thành luồng thay thế. Chỉ tách hoặc dùng tổng quát hoá khi luồng khác nhau nhiều (U-R12) |
| U-AP16 | Tác vụ kỹ thuật thành UC | Sao lưu, dọn nhật ký, giám sát máy chủ không có tác nhân nghiệp vụ và nguồn chỉ nêu như ràng buộc | "Sao lưu CSDL hằng đêm" | Loại (chuyển P06 như yêu cầu phi chức năng), trừ khi nguồn nêu một vai trò chủ động thực hiện nó |

=== Phần B. Quy tắc cho ca tranh cãi ===

U-R01 Đăng nhập.
- Quy tắc: khi nguồn yêu cầu xác thực, tạo một UC "Đăng nhập" (Log In), tác nhân chính là mọi tác nhân người phải xác thực (hoặc tác nhân cha của họ nếu P01 đã có tổng quát hoá). Đăng nhập được mô hình hoá như một use case riêng vì nó là một cuộc đối thoại hoàn chỉnh với hệ thống, có luồng thay thế và ngoại lệ riêng (sai mật khẩu, khoá tài khoản).
- Không nối Đăng nhập vào mọi UC bằng include; việc đã đăng nhập được ghi là tiền điều kiện của các UC khác ở P04.
- Cột Mức ghi "Subfunction" và Mô tả ngắn nêu rõ đây là điều kiện để dùng các UC khác. Lý do: tự nó không qua được Boss test, nhưng việc tách riêng giúp mọi UC khác không lặp lại phần xác thực.
- Nguồn không nói thẳng yêu cầu xác thực nhưng ngụ ý (nhắc "đăng nhập", "tài khoản", "mật khẩu" của một vai trò, hoặc nêu một chức năng "không cần đăng nhập"): vẫn tạo UC Đăng nhập, chỉ nối các tác nhân mà nguồn nhắc tài khoản hoặc đăng nhập của họ; với tác nhân người còn lại: ở NGHIEM_NGAT ghi Q-nn về việc có phải đăng nhập không, và chưa nối; ở CO_NHAN ghi ASM-nn nêu những tác nhân phải đăng nhập, nối các tác nhân đó với UC Đăng nhập (cột Tác nhân chính), và ghi mã ASM ở cột Lý do của ứng viên Đăng nhập.
- Nếu nguồn không nêu và không ngụ ý xác thực, không tạo (U-T10).

U-R02 Đăng xuất.
- Quy tắc: không tạo UC riêng. Đăng xuất chỉ có 1-2 bước, không có kết quả giá trị (U-T3, U-T4). Kết luận "Là bước của" UC Đăng nhập (kết thúc phiên) hoặc "Loại" nếu nguồn chỉ nhắc qua.
- Ngoại lệ: nguồn yêu cầu hành vi đáng kể khi kết thúc phiên (chốt ca, bàn giao tiền) thì đó là một UC nghiệp vụ khác, đặt tên theo nghiệp vụ ("Chốt ca thu ngân"), không phải "Đăng xuất".

U-R03 Đăng ký tài khoản và các chức năng tài khoản.
- Đăng ký tài khoản là UC User-goal của tác nhân chưa có tài khoản (kết quả: có tài khoản để dùng dịch vụ). Tác nhân chính là vai trò khách chưa đăng ký nếu P01 có, ngược lại là tác nhân sẽ sở hữu tài khoản.
- Tạo tài khoản cho người khác do quản trị viên làm thuộc "Quản lý tài khoản người dùng" (U-R04).
- Quên mật khẩu hoặc khôi phục truy cập: một UC riêng khi nguồn nêu (mục tiêu: lấy lại quyền truy cập).
- Đổi mật khẩu, cập nhật hồ sơ cá nhân: gộp thành một UC "Cập nhật tài khoản cá nhân" nếu cùng tác nhân và nguồn nêu cả hai; một UC riêng nếu nguồn chỉ nêu một.

U-R04 CRUD (thêm, xem, sửa, xoá).
- Mặc định gộp: các thao tác thêm, xem, sửa, xoá trên cùng một loại dữ liệu danh mục hoặc dữ liệu cấu hình (danh mục thuốc, danh mục sách, loại phòng, bảng giá gửi xe), do cùng một tác nhân thực hiện, không có quy tắc nghiệp vụ riêng lớn, gộp thành một UC "Quản lý <dữ liệu>". Lý do: từng thao tác CRUD riêng lẻ là thao tác quản trị dữ liệu, không đem lại kết quả có giá trị riêng; bốn UC riêng làm mô hình vụn (U-AP07).
- Tách thành UC riêng khi có ít nhất một điều kiện:
  a) Các thao tác do các tác nhân khác nhau thực hiện (bạn đọc tra cứu sách, thủ thư thêm và sửa sách: "Tra cứu sách" là UC của bạn đọc, "Quản lý danh mục sách" là UC của thủ thư).
  b) Thao tác là một giao dịch nghiệp vụ, tức là phản hồi một sự kiện nghiệp vụ và có quy tắc riêng, không chỉ là quản trị dữ liệu: "Đặt lịch khám" (tạo lịch hẹn), "Huỷ lịch khám" (xoá hoặc đổi trạng thái lịch hẹn, có quy tắc thời hạn huỷ), "Lập phiếu nhập kho", "Nhận phòng". Giao dịch nghiệp vụ không bao giờ bị gộp vào "Quản lý X" (U-AP08).
  c) Một thao tác có luồng hoặc quy tắc lớn khác hẳn (sửa giá cần phê duyệt, xoá cần kiểm tra ràng buộc phức tạp mà nguồn mô tả chi tiết) khiến UC gộp vượt ngưỡng kích thước.
  d) Các thao tác có sự kiện kích hoạt hoặc thời điểm khác nhau rõ rệt, hoặc quyền truy cập khác nhau mà nguồn nêu.
- Mỗi loại dữ liệu danh mục một UC "Quản lý <dữ liệu>" (danh mục loại phòng, danh mục dịch vụ đi kèm là hai UC). Chỉ gộp nhiều loại dữ liệu vào một UC khi nguồn mô tả chúng luôn được cập nhật cùng nhau trong một lần làm việc, hoặc một loại chỉ là thuộc tính phụ của loại kia.
- Chỉ đưa vào "Quản lý X" những thao tác mà nguồn nêu. Nếu nguồn chỉ nêu "thêm và sửa", Mô tả ngắn ghi rõ "thêm và sửa", không tự thêm "xoá".
- Ví dụ đúng: "Quản lý danh mục thuốc" (quản trị viên thêm, sửa, ngừng dùng thuốc). Ví dụ sai: "Quản lý đơn hàng" cho khách hàng giao đồ ăn (che giấu Đặt món và Huỷ đơn).

U-R05 Xem, tra cứu, báo cáo.
- Là UC khi tác nhân có mục tiêu thông tin độc lập, tự tìm tới hệ thống để lấy thông tin phục vụ quyết định hoặc công việc của mình: "Tra cứu sách", "Xem lịch sử khám", "Xem báo cáo tồn kho", "Tra cứu phòng trống" (khi khách chỉ muốn xem, chưa đặt).
- Là bước của UC khác khi việc xem chỉ phục vụ một bước của mục tiêu khác: xem danh sách phòng trống trong khi đặt phòng là bước của "Đặt phòng".
- Tìm kiếm rồi xem chi tiết là một UC ("Tra cứu X"), không tách "Tìm X" và "Xem chi tiết X". Sắp xếp, lọc, phân trang, xuất tệp, in là tuỳ chọn hoặc bước, không phải UC (trừ khi xuất hoặc in là mục tiêu độc lập mà nguồn nêu, ví dụ in hoá đơn đỏ theo yêu cầu).
- Báo cáo: gộp thành một UC "Xem báo cáo <nhóm>" khi cùng tác nhân, cùng cách thao tác (chọn kỳ, chọn tiêu chí, xem kết quả), chỉ khác nội dung dữ liệu; tách mỗi báo cáo một UC khi tác nhân khác nhau, mục đích khác nhau, hoặc có luồng riêng (phê duyệt, gửi đi).

U-R06 Thông báo và nhắc nhở.
- Gửi thông báo (email, SMS, thông báo đẩy) như hệ quả của một UC là bước của UC đó (U-AP03). Kênh gửi bên ngoài (Cổng SMS, Hệ thống email) là tác nhân phụ của UC đó.
- Nhắc nhở theo lịch (nhắc lịch khám trước 24 giờ, nhắc trả sách sắp hết hạn) là UC riêng với tác nhân chính là tác nhân thời gian (U-R07), tác nhân phụ là kênh gửi. Người nhận tin qua kênh ngoài không phải tác nhân của UC này (họ không tương tác với hệ thống); ghi họ trong Mục tiêu như bên hưởng lợi.
- Người dùng xem thông báo bên trong hệ thống (hộp thông báo của ứng dụng) là UC "Xem thông báo" của người đó chỉ khi nguồn nêu hành vi này.

U-R07 Tác vụ theo lịch.
- Là UC với tác nhân chính là tác nhân thời gian khi đồng thời: nguồn nêu rõ thời điểm hoặc chu kỳ; không có người hay hệ thống ngoài ra lệnh; kết quả có giá trị nghiệp vụ cho một bên liên quan (tự huỷ lịch hẹn mà bệnh nhân chưa xác nhận qua tin nhắn trong 24 giờ sau khi đặt, để giải phóng khung giờ; tính phí phạt quá hạn cuối ngày; lập báo cáo tồn kho cuối ngày gửi kế toán); và mốc thời gian rơi vào lúc không còn phiên nào của tác nhân đang mở.
- Hết giờ chờ trong phiên: khi tác nhân chính vẫn đang ở phiên của một UC và hệ thống chờ một sự kiện có hạn giờ (chờ tác nhân thao tác tiếp, chờ thiết bị hoặc hệ thống ngoài phản hồi, chờ thanh toán), việc hết hạn là luồng thay thế hoặc ngoại lệ của chính UC đó. Không tạo UC riêng, không tạo tác nhân thời gian; ứng viên kết luận "Là bước của UC-nnn" và ghi "U-R07 hết giờ trong phiên" ở cột Lý do. Ví dụ (ATM): khách không rút tiền trong 30 giây sau khi máy đẩy tiền ra thì máy thu hồi tiền là luồng thay thế của "Rút tiền"; ví dụ (khách sạn): khách không hoàn tất thanh toán trong 10 phút thì phòng giữ tạm được nhả là luồng thay thế của "Đặt phòng".
- Tác vụ có mốc thời gian nguồn nêu rõ, chỉ chuyển dữ liệu giữa hai thành phần Trong ranh giới để phục vụ một tác nhân người ở UC khác (gửi danh sách giao hàng xuống ứng dụng của tài xế 30 phút trước ca), vẫn là UC của tác nhân thời gian; ghi tác nhân hưởng lợi ở cột Mục tiêu. Q1 không áp dụng cho trường hợp này vì đã có sự kiện thời gian kích hoạt.
- Tên đặt theo kết quả nghiệp vụ ("Huỷ lịch hẹn quá hạn xác nhận", "Nhắc lịch khám"), không đặt "Chạy tác vụ đêm".
- Nếu P01 không có tác nhân thời gian mà nguồn có hành vi này: ghi vào "Đề xuất sửa artifact trước" (bước P01) và vẫn lập ứng viên.
- Tác vụ kỹ thuật (sao lưu, dọn dữ liệu tạm) theo U-AP16.

U-R08 Hệ thống ngoài: tác nhân chính hay phụ.
- Phụ: hệ thống gọi tới nó để hoàn tất một UC do tác nhân khác khởi xướng (cổng thanh toán trừ tiền trong "Đặt món", cổng SMS gửi mã xác nhận). Không tạo UC riêng cho lời gọi đó.
- Chính: nó tự gửi yêu cầu hoặc dữ liệu vào hệ thống, vào thời điểm do nó quyết định, và hệ thống phải xử lý như một mục tiêu riêng (ERP gửi danh mục hàng hoá mới, ngân hàng báo đã nhận chuyển khoản sau vài giờ). Khi đó tạo UC với tác nhân chính là hệ thống ngoài, tên theo nghiệp vụ ("Ghi nhận thanh toán chuyển khoản", "Đồng bộ danh mục hàng hoá").
- Phản hồi đồng bộ hoặc gần như tức thời trong cùng phiên (cổng thanh toán trả kết quả ngay) là bước của UC đang chạy, không phải UC riêng.

U-R09 Cơ sở dữ liệu và "hệ thống tự làm".
- CSDL của hệ thống không phải tác nhân; đọc, ghi CSDL không phải UC (U-AP03).
- "Hệ thống tự động X" khi X xảy ra như hệ quả của một UC là bước của UC đó, kể cả khi X xảy ra do hết giờ chờ trong phiên của UC đó (U-R07, hết giờ trong phiên); khi X xảy ra theo thời điểm ngoài mọi phiên thì theo U-R07; khi không xác định được nguyên nhân kích hoạt thì ghi câu hỏi mở.

U-R10 Nhập liệu thay mặt người khác (người đại diện).
- Tác nhân chính là người trực tiếp thao tác trên hệ thống (thao tác qua một thiết bị vẫn là trực tiếp, xem U-R18). Nhân viên quầy đặt phòng hộ khách gọi điện tới: nhân viên quầy là tác nhân chính; khách là bên liên quan (không phải tác nhân của UC đó).
- Nếu cả người được đại diện (tự làm trực tuyến) và người đại diện (làm hộ) đều làm cùng một mục tiêu, xét hai điều kiện sau theo thứ tự; hai điều kiện loại trừ nhau, mỗi trường hợp chỉ rơi vào đúng một:
  a) Hai UC riêng khi thoả ít nhất một trong hai:
     - Luồng của người đại diện có một đoạn tương tác riêng từ 2 bước trở lên mà luồng của người được đại diện không có, ví dụ tạo hồ sơ cho người được phục vụ, xác minh danh tính người được phục vụ.
     - Kết quả khác nhau: đối tượng được tạo hoặc thay đổi kết thúc ở trạng thái khác (phòng do nhân viên quầy đặt được giữ ngay, phòng do khách tự đặt chờ đặt cọc).
     Tên phân biệt theo góc nhìn tác nhân ("Đặt phòng" và "Đặt phòng cho khách"), phần chung là ứng viên include ở P03.
  b) Không thoả a: một UC, nối với cả hai tác nhân chính, khác biệt thành luồng thay thế ở P04. Trường hợp này gồm: chỉ khác một bước tìm hoặc chọn người, đối tượng được phục vụ (một bước, không tính là đoạn tương tác riêng); chỉ khác điều kiện hoặc ngưỡng của cùng một quy tắc (mốc thời gian, giới hạn số lượng khác nhau theo vai trò), ghi thành BR có điều kiện theo vai trò ở P04. Nếu hai tác nhân dùng chung nhiều UC như vậy, xét đề xuất tác nhân cha theo U-R11.
- Ghi vào cột Lý do: "U-R10 a" kèm điều kiện thoả, hoặc "U-R10 b".

U-R11 Nhiều tác nhân cùng một UC.
- Một UC có thể có nhiều tác nhân được phép khởi xướng; mỗi lần thực hiện chỉ có một người khởi xướng. Ghi tất cả vào cột Tác nhân chính.
- Khi từ hai tác nhân trở lên cùng khởi xướng từ hai UC trở lên giống nhau, chỉ đề xuất tổng quát hoá tác nhân (ghi vào "Đề xuất sửa artifact trước", bước P01) khi các tác nhân thoả điều kiện ở P01 Bước 5: phép thử "là một" và nguồn cho thấy họ làm các việc chung theo cùng một cách. Tác nhân khác bản chất (khách tự làm và nhân viên làm hộ theo U-R10 b) giữ nhiều association, không đề xuất.

U-R12 Biến thể của cùng một mục tiêu.
- Biến thể theo phương thức, kênh, loại dữ liệu (thanh toán tiền mặt hay thẻ, tìm theo tên hay theo mã, nhận phòng có đặt trước hay khách vãng lai) mặc định là luồng thay thế của một UC (U-AP15).
- Chỉ tách thành UC riêng hoặc đề xuất tổng quát hoá use case (quyết định ở P03) khi mỗi biến thể có luồng chính khác nhau đáng kể, có tác nhân phụ khác nhau hoặc quy tắc nghiệp vụ riêng lớn mà nguồn mô tả.

U-R13 Quy trình có phê duyệt hoặc nhiều bên nối tiếp.
- Mỗi bước do một tác nhân khác thực hiện vào lúc khác là một UC riêng: "Lập phiếu xuất kho" (thủ kho) và "Duyệt phiếu xuất kho" (quản lý kho); "Đặt món" (khách hàng), "Xác nhận đơn" (nhà hàng), "Nhận đơn giao" (tài xế). Không gom thành một UC quy trình (U-AP05).
- Trình tự giữa các UC được thể hiện bằng tiền điều kiện và hậu điều kiện ở P04 và bằng activity diagram nghiệp vụ nếu cần, không bằng quan hệ trên sơ đồ use case.

U-R14 Thao tác lặp trong một phiên.
- Thêm nhiều mặt hàng vào một phiếu, chọn nhiều món, quét nhiều mã là vòng lặp trong một UC, không phải nhiều UC.
- "Thêm món vào giỏ" không phải UC riêng nếu giỏ chỉ tồn tại để đặt món trong cùng phiên; là UC riêng chỉ khi nguồn cho giỏ tồn tại lâu dài, được quản lý độc lập qua nhiều phiên và tác nhân có mục tiêu riêng với nó.

U-R15 Cấu hình và quản trị hệ thống.
- Thiết lập tham số nghiệp vụ (giờ mở cửa, số ngày mượn tối đa, bảng giá) do một vai trò quản trị thực hiện là UC "Cấu hình <nhóm tham số>" hoặc thuộc "Quản lý <dữ liệu>" theo U-R04, chỉ khi nguồn nêu.
- Phân quyền, quản lý tài khoản người dùng do quản trị viên làm là UC "Quản lý tài khoản người dùng" khi nguồn nêu.

U-R16 Hành vi ngoài phạm vi và hành vi đã bị nguồn loại trừ.
- Ứng viên thuộc mục "Ngoài phạm vi" của P00, hoặc bị nguồn loại trừ tường minh, kết luận "Loại" với lý do trích dẫn câu loại trừ. Không tạo UC dù hành vi đó phổ biến ở hệ thống cùng loại.
- Ứng viên thuộc danh sách "Chờ Q-nn" ở mục phạm vi của P00 (câu phạm vi mâu thuẫn với mô tả chi tiết) kết luận "Chờ Q-nn", không tự chọn giữ hay loại. Ở chế độ CO_NHAN, P00 đã xếp chức năng theo một ASM-nn: theo ASM đó và ghi mã ASM ở cột Lý do.

U-R17 Xem danh sách và tìm kiếm, lọc.
- Xem danh sách (hiển thị sẵn hoặc duyệt theo trang) và tìm kiếm hoặc lọc theo tiêu chí trên cùng loại thông tin, do cùng tác nhân thực hiện, phục vụ cùng mục tiêu: một UC, đặt tên theo mục tiêu ("Tra cứu phòng trống", "Tra cứu sách"). Tìm kiếm, lọc là luồng thay thế hoặc bước tuỳ chọn của UC đó; việc xem danh sách khi tác nhân không nhập tiêu chí là luồng chính hoặc luồng thay thế.
- Tách thành UC riêng chỉ khi tìm kiếm có quy tắc nghiệp vụ, dữ liệu vào hoặc tác nhân khác đáng kể mà nguồn nêu (ví dụ: bạn đọc xem danh sách sách mới trên trang chủ, còn thủ thư tìm theo mã vạch và tình trạng lưu kho để xử lý sách hỏng: hai tác nhân, hai mục tiêu).
- Ghi vào cột Lý do: "U-R17" kèm kết luận gộp hoặc điều kiện tách thoả.

U-R18 Người thao tác qua thiết bị.
- Khi một người tác động lên hệ thống thông qua một thiết bị (quét thẻ hoặc mã, đưa vật vào thiết bị, bấm nút trên máy), tác nhân chính của UC là người có mục tiêu, theo phép thử "Ai muốn kết quả này?". Thiết bị là tác nhân phụ khi nó nằm ngoài ranh giới và có giao tiếp riêng với hệ thống (P01 xếp Loại Thiết bị hoặc Hệ thống ngoài); thiết bị thuộc ranh giới chỉ là kênh nhập, không ghi vào cột tác nhân.
- Thiết bị là tác nhân chính chỉ khi nó tự phát sự kiện mà không có người nào có mục tiêu đứng sau (cảm biến chỗ đỗ báo chỗ trống, đồng hồ đo tự gửi số liệu).
- Các UC cùng cơ chế (người thao tác trên cùng một loại thiết bị) phải có cùng cách chọn tác nhân chính.
- Nguồn chưa nêu ai thao tác trên thiết bị: ở NGHIEM_NGAT kết luận "Chờ Q-nn" về tác nhân chính (Q-nn hỏi vai trò người thao tác); ở CO_NHAN chọn vai trò theo ASM-nn. Không lấy thiết bị làm tác nhân chính thay cho người.
- Nếu P01 xếp thiết bị là tác nhân chính trong khi có người thao tác trên nó: ghi vào "Đề xuất sửa artifact trước" (bước P01).
- Ví dụ (quản lý kho): "Lập phiếu nhập kho", thủ kho quét mã vạch từng kiện: tác nhân chính Thủ kho, tác nhân phụ Máy quét mã vạch (khi là thiết bị ngoài ranh giới). Ví dụ (bãi đỗ xe): "Ra bãi", tài xế quẹt thẻ tại barrier: tác nhân chính Tài xế, tác nhân phụ Barrier; "Cập nhật tình trạng chỗ đỗ" khi cảm biến báo chỗ trống: tác nhân chính Cảm biến chỗ đỗ.
- Ghi vào cột Lý do: "U-R18".

=== Phần C. Quy tắc đặt tên use case ===
U-N1 Dạng "động từ + bổ ngữ", động từ mạnh, cụ thể, ở thể chủ động, nêu hành động của tác nhân chính: "Đặt lịch khám", "Cho mượn sách", "Lập phiếu nhập kho". Tiếng Anh: động từ nguyên thể viết hoa chữ đầu mỗi từ, "Book Appointment", "Lend Book", "Create Goods Receipt".
U-N2 Góc nhìn tác nhân chính (người khởi xướng), không phải góc nhìn hệ thống: "Rút tiền", không "Xử lý rút tiền", không "Cấp tiền". Với tác nhân thời gian, tên nêu kết quả nghiệp vụ.
U-N3 Tên nêu được kết quả có giá trị, đọc tên là biết use case đem lại gì: "Gia hạn sách" (kết quả: hạn trả mới). Tránh động từ yếu hoặc mơ hồ: xử lý, thực hiện, làm, chạy, hỗ trợ, quản lý hệ thống. Khi nguồn dùng "xử lý" cho một việc nghiệp vụ, đặt tên theo kết quả của việc đó: "Xử lý đơn quá hạn giao" --> "Huỷ đơn quá hạn giao" hoặc "Ghi nhận đơn giao thất bại", theo kết quả nguồn nêu.
U-N4 Dùng thuật ngữ của miền nghiệp vụ (đã có trong glossary nếu có), nhất quán giữa các use case: nếu đã dùng "lịch hẹn" thì không lúc "lịch hẹn", lúc "cuộc hẹn".
U-N5 Không chứa từ giao diện hoặc kỹ thuật: màn hình, trang, form, nút, nhấn, click, menu, pop-up, CSDL, bảng, bản ghi, API, gọi, lưu, insert, update. "Cập nhật" bị cấm khi chỉ nói việc ghi dữ liệu ("Cập nhật CSDL", "Cập nhật bản ghi phòng"); được giữ khi là động từ nghiệp vụ của nguồn kèm bổ ngữ nêu kết quả ("Cập nhật tình trạng chỗ đỗ", "Cập nhật hồ sơ cá nhân").
U-N6 Duy nhất và tự giải thích: không có hai UC trùng tên hoặc chỉ khác một từ đồng nghĩa; tên không cần đọc mô tả mới hiểu.
U-N7 Độ dài: thường 2-6 từ tiếng Việt. Dài hơn thường là dấu hiệu gộp hai mục tiêu (có "và") hoặc nhét điều kiện vào tên.
U-N8 "Quản lý <dữ liệu>" chỉ dùng cho nhóm CRUD dữ liệu danh mục theo U-R04; không dùng cho giao dịch nghiệp vụ.
Ví dụ sai và cách sửa: "Hiển thị lịch trống của bác sĩ" --> "Tra cứu lịch trống của bác sĩ"; "Nhấn nút đặt bàn" --> thuộc "Đặt bàn"; "Xử lý trả sách" --> "Nhận trả sách" (tác nhân thủ thư) hoặc "Trả sách" (tác nhân bạn đọc tự thao tác tại máy tự phục vụ); "Update inventory" --> là bước của "Lập phiếu nhập kho"; "Mượn và trả sách" --> tách thành "Cho mượn sách", "Nhận trả sách".

=== Phần D. Nội dung artifact ===

Mục 1. Danh sách mục tiêu tác nhân
| ACT | Mục tiêu | Mức mục tiêu dự kiến (Summary / User-goal / Subfunction) | REQ | CAND |
- Mỗi tác nhân chính (kể cả thời gian, hệ thống ngoài là chính) có ít nhất một dòng.
- Mục tiêu viết theo lời của tác nhân, dạng cụm động từ.

Mục 2. Danh sách sự kiện
| EV | Sự kiện | Loại (Nghiệp vụ / Thời gian / Hệ thống ngoài / Thiết bị) | Nguồn phát (ACT) | Phản hồi mong đợi của hệ thống | REQ | CAND |
- Mã EV-nn theo Conventions C3; không đổi khi chạy lại. P04 dẫn mã này ở hàng Sự kiện kích hoạt.
- Loại Thiết bị chỉ dùng cho tín hiệu thiết bị tự phát (U-R18); tín hiệu phát ra do người thao tác trên thiết bị có Loại Nghiệp vụ, nguồn phát là người đó.
- Sự kiện thời gian trong phiên của một UC (hết giờ chờ, U-R07): Nguồn phát ghi "-", CAND tương ứng kết luận "Là bước của UC-nnn".
- Ví dụ: "EV-03 | Bệnh nhân muốn huỷ lịch đã đặt | Nghiệp vụ | ACT-01 | Huỷ lịch, giải phóng khung giờ | REQ-06 | CAND-05". "EV-07 | Đến 24 giờ trước giờ hẹn | Thời gian | ACT-06 | Gửi tin nhắc lịch qua cổng SMS | REQ-11 | CAND-12". "EV-09 | Hệ thống ERP gửi danh mục hàng hoá mới | Hệ thống ngoài | ACT-05 | Cập nhật danh mục hàng trong kho | REQ-21 | CAND-18".

Mục 3. Bảng ứng viên use case
| CAND | Ứng viên | Kết luận | Phép thử không đạt | Lý do | REQ | Nguồn phát hiện |
- Kết luận: một trong "Giữ thành UC-nnn", "Gộp vào UC-nnn", "Là bước của UC-nnn", "Tách thành CAND-xx, CAND-yy", "Loại", "Chờ Q-nn".
- "Chờ Q-nn" chỉ dùng ở chế độ NGHIEM_NGAT. Ở chế độ CO_NHAN, ứng viên có dấu hiệu trong nguồn nhưng chưa đủ căn cứ thì được tạo ASM-nn chọn một phương án của Q-nn (hoặc dùng ASM-nn mà P00, P01 đã ghi), kết luận theo ASM đó và ghi mã ASM ở cột Lý do; Q-nn vẫn giữ để người dùng xác nhận (Conventions mục C1.2). Ví dụ (phòng khám): nguồn nêu lễ tân xếp lịch làm việc của bác sĩ nhưng không nói ai tạo hồ sơ bác sĩ --> CO_NHAN: ASM-nn "Quản trị viên tạo và sửa hồ sơ bác sĩ", ứng viên "Quản lý hồ sơ bác sĩ" kết luận Giữ thành UC-nnn; NGHIEM_NGAT: Chờ Q-nn. Tác nhân chính của UC theo ASM lấy trong P01; P01 không có vai trò phù hợp thì ghi "Đề xuất sửa artifact trước" (bước P01) và vẫn kết luận theo ASM với tác nhân được đề xuất.
- "Chờ Q-nn" (NGHIEM_NGAT): ứng viên có dấu hiệu trong nguồn nhưng chưa đủ căn cứ để giữ hoặc loại, và câu hỏi mở Q-nn quyết định số phận của nó. Cột Lý do nêu câu trả lời nào dẫn tới UC. Ứng viên này không vào Mục 4; P03 bỏ qua. Khi Q-nn được trả lời, chạy lại P02 để đổi kết luận. Không dùng "Chờ Q-nn" cho ứng viên không có căn cứ trong nguồn (kết luận "Loại" theo U-T10).
- Phép thử không đạt: mã U-T và mã U-AP liên quan, hoặc "-" khi Giữ.
- Lý do: một câu, nêu mã U-R nếu đã áp dụng.
- Nguồn phát hiện: Mục tiêu / Sự kiện / Động từ, kèm mã EV nếu có.
- Mọi ứng viên có đúng một kết luận cuối; mọi UC-nnn được trỏ tới đều có trong Mục 4.
- Ví dụ: "CAND-07 | Gửi email xác nhận lịch hẹn | Là bước của UC-001 | U-T9, U-AP03 | Hệ quả của việc đặt lịch, không có tác nhân chủ động | REQ-05 | Động từ".
- Ví dụ: "CAND-15 | Mượn và trả sách | Tách thành CAND-16, CAND-17 | U-T6, U-AP05 | Hai phiên cách nhau nhiều ngày | REQ-08 | Mục tiêu".

Mục 4. Bảng use case
Gồm hai bảng cùng thứ tự dòng, cùng mã UC. Bảng 4a (lõi) là bảng mà P03 và các bước sau đọc để lấy tác nhân, mức, nhóm; bảng 4b (mô tả) giữ phần chữ dài để người đọc kiểm tra từng UC.
Bảng 4a. Bảng lõi
| UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mức | Nhóm chức năng |
Bảng 4b. Bảng mô tả
| UC | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | REQ | CAND nguồn |
Quy tắc cho từng cột (dù cột nằm ở bảng nào):

Cột UC: mã UC-nnn theo Conventions C3, cấp theo Bước 9.1; hai bảng có đúng cùng tập mã UC.

Cột Tên (VI), Tên (EN): theo U-N1 đến U-N8.

Cột Tác nhân chính: mã ACT (và tên ở lần đầu), nhiều tác nhân ngăn bằng dấu phẩy khi áp dụng U-R10 hoặc U-R11. UC mức Subfunction giữ theo Q4:
- Tác nhân chính của UC gốc vẫn tương tác trực tiếp trong phần được tách (chọn, nhập, xác nhận): ghi tác nhân chính của UC gốc kèm "(qua UC-xxx)", UC-xxx là UC gốc. Với Q4a, ghi tác nhân chính của mọi UC gốc có tương tác trong phần đó. Ví dụ: "Thanh toán đơn" giữ theo Q4d, khách hàng chọn phương thức và nhập thông tin thẻ: "ACT-01 (qua UC-004)".
- Phần được tách không có tác nhân nào tương tác trực tiếp (chỉ gồm bước của hệ thống và tác nhân phụ): ghi "-" và "Được gọi từ UC-xxx".
- P03 vẫn không vẽ association từ tác nhân chính ghi "(qua UC-xxx)" tới UC này (P03 Bước 2.2).

Cột Tác nhân phụ: mã ACT các tác nhân mà hệ thống gọi tới trong UC; "-" nếu không có.

Cột Mục tiêu (kết quả có giá trị):
- Định nghĩa: kết quả mà tác nhân chính nhận được khi UC thành công, nhìn từ phía tác nhân.
- Quy tắc: một câu, bắt đầu bằng tác nhân hoặc kết quả, kiểm chứng được. Không mô tả cách hệ thống làm.
- Ví dụ đúng: "Bệnh nhân có một lịch khám đã được giữ chỗ với bác sĩ và khung giờ mong muốn." "Thủ kho có phiếu nhập kho được ghi nhận, tồn kho tăng tương ứng."
- Ví dụ sai: "Hệ thống lưu lịch hẹn vào CSDL." (góc nhìn hệ thống, kỹ thuật). "Đặt lịch thành công." (không nói ai nhận gì).

Cột Mô tả ngắn:
- Định nghĩa: 1-3 câu nêu mục đích của UC và phạm vi hành vi, đủ để người đọc hình dung đúng UC.
- Quy tắc: nêu tác nhân, việc chính, các biến thể chính nếu gộp (ví dụ "thêm, sửa, ngừng dùng thuốc"); không liệt kê từng bước; không dùng từ giao diện.
- Ví dụ đúng: "Lễ tân ghi nhận việc bệnh nhân có lịch hẹn tới khám, xác nhận thông tin và xếp bệnh nhân vào hàng chờ của bác sĩ."
- Ví dụ sai: "Lễ tân nhấn nút Check-in, hệ thống mở màn hình danh sách và lưu trạng thái." (bước, giao diện, kỹ thuật).

Cột Sự kiện kích hoạt: sự kiện khiến UC bắt đầu, thường lấy từ Mục 2 (ghi mã EV). Ví dụ: "Khách muốn nhận phòng đã đặt (EV-02)". "Đến 23:00 hằng ngày (EV-08)".

Cột Nhóm chức năng:
- Định nghĩa: nhóm nghiệp vụ dùng để chia package và sơ đồ phân rã ở P03.
- Quy tắc: nhóm theo lĩnh vực nghiệp vụ hoặc theo đối tượng nghiệp vụ chính (Đặt lịch, Tiếp đón, Danh mục, Báo cáo), không nhóm theo màn hình hay theo tầng kỹ thuật. Mỗi nhóm thường 3-12 UC; một nhóm chỉ có 1 UC thì cân nhắc nhập vào nhóm gần nhất. Hệ thống dưới khoảng 15 UC có thể chỉ có 1-3 nhóm.

Cột REQ: mọi REQ mà UC phủ.

Cột Mức: User-goal hoặc Subfunction (Subfunction chỉ khi được giữ theo Q4 hoặc U-R01; ghi điều kiện a, b, c hoặc d của Q4 trong Mô tả ngắn).

Cột CAND nguồn: các CAND đã giữ hoặc gộp vào UC này.

Mục 5. Ma trận truy vết REQ --> UC
| REQ | Nội dung tóm tắt | UC phủ | Ghi chú (lý do nếu không phủ) |
- Liệt kê mọi REQ của P00, mỗi REQ một dòng. REQ Chức năng và Giao tiếp ngoài phải có UC phủ hoặc có lý do. REQ Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng, Ràng buộc ghi UC khi đã gắn với UC cụ thể; chưa gắn thì cột UC phủ ghi "-" và cột Ghi chú ghi "Chuyển P06".

Mục 6. Thống kê và nhận xét ngưỡng
| ACT | Số UC là tác nhân chính | Số UC là tác nhân phụ | Nhận xét |
Cuối bảng ghi: tổng số UC, số UC mỗi nhóm, số UC mức Subfunction, và nhận xét khi lệch mức hợp lý.

Mục 7. Các mục kiểm soát theo Conventions C5. Khi chạy lại sau review, thêm mục "Thay đổi so với phiên bản trước" đặt trước mục Câu hỏi mở: | UCR | Phần tử đã đổi (UC, CAND, dòng REQ) | Thay đổi |. Sửa hệ quả không thuộc UCR nào ghi UCR là "Hệ quả của UCR-xx".

=== Phần E. Mức hợp lý (heuristic, không phải luật cứng) ===
- Mỗi tác nhân chính người thường có khoảng 2-12 UC. Trên khoảng 15 là dấu hiệu phân rã chức năng hoặc tác nhân quá rộng; chỉ 1 UC là bình thường với tác nhân thời gian và hệ thống ngoài, nhưng với tác nhân người thì nên kiểm tra lại mục tiêu có bị gộp quá mức không.
- Hệ thống cỡ vừa thường có khoảng 10-40 UC User-goal. Hàng trăm UC gần như chắc chắn là phân rã chức năng; dưới 5 UC cho một nguồn nhiều trang thường là mức summary.
- Luồng chính dự kiến của một UC khoảng 3-15 bước (dễ đọc nhất khoảng 3-9 bước). Ngưỡng này dùng để ước lượng ở bước này; đặc tả chi tiết ở P04.
- UC mức Subfunction thường không quá khoảng 20% tổng số UC; nhiều hơn là dấu hiệu tách include quá mức.
- Nếu một con số lệch ngưỡng nhưng có căn cứ rõ trong nguồn, giữ nguyên và giải thích trong Mục 6; không gộp hoặc tách chỉ để đạt con số.

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Mọi tác nhân chính trong P01 có ít nhất một dòng ở danh sách mục tiêu và ít nhất một UC.
2. Mọi sự kiện ở Mục 2 có ứng viên tương ứng, và ứng viên đó có kết luận cuối.
3. Mọi ứng viên có đúng một kết luận thuộc sáu giá trị cho phép; mọi kết luận "Chờ Q-nn" trỏ tới câu hỏi có trong mục Câu hỏi mở, và ở chế độ CO_NHAN không có kết luận "Chờ Q-nn" (ứng viên đó có ASM-nn); mọi tham chiếu UC-nnn, CAND-nn trỏ tới phần tử tồn tại.
4. Mọi UC mức User-goal đạt U-T1 đến U-T12, trừ phép thử bị một quy tắc U-R hoặc QUY_UOC_DA_CHOT ghi đè (mã U-R hoặc quy ước đó được ghi ở cột Lý do); mọi UC mức Subfunction thoả Q4 hoặc U-R01.
5. Không UC nào khớp một anti-pattern U-AP01 đến U-AP16.
6. Mọi tên UC tuân thủ U-N1 đến U-N8; không có từ cấm.
7. Không có "Quản lý X" gom giao dịch nghiệp vụ; mọi "Quản lý X" chỉ gồm thao tác mà nguồn nêu.
8. Mọi REQ chức năng được phủ bởi ít nhất một UC, hoặc có lý do trong ma trận.
9. Mọi UC truy vết về ít nhất một REQ; không có UC dựa trên hiểu biết chung ngoài nguồn.
10. Cột Mục tiêu của mọi UC viết từ góc nhìn tác nhân và kiểm chứng được.
11. Các ca tranh cãi đã áp dụng đúng quy tắc U-R (hoặc quy ước đã chốt), mã quy tắc được ghi trong cột Lý do.
12. Thống kê ngưỡng đã lập; mọi chỗ lệch có nhận xét.
13. Không đổi tên, mã tác nhân của P01; mọi đề nghị sửa P01 nằm ở "Đề xuất sửa artifact trước".
14. Artifact có đủ các mục kiểm soát theo C5.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho bước này; ưu tiên cao hơn quy tắc mặc định của bước (trừ Conventions C1). Không có thì thay cả khối bằng "Không có" | Ví dụ: "Tên use case chỉ cần tiếng Việt, bỏ cột Tên (EN)." ; "Nhóm chức năng theo ba phân hệ đã chốt: Bán hàng, Kho, Báo cáo." ; "Giữ Đăng xuất thành use case riêng theo mẫu tài liệu của tổ chức."}}
````

## 5. Ghi chú cho người dùng

- Kết quả quá nhiều use case nhỏ (ví dụ trên 15 UC cho một tác nhân): xem cột "Phép thử không đạt" của các ứng viên đã giữ; thường cần gộp theo U-AP01, U-AP06, U-AP07. Có thể chạy P02R lên chính kết quả để có bảng phát hiện.
- Kết quả quá ít use case, tên kiểu "Quản lý X" khắp nơi: thường là U-AP04 hoặc U-AP08. Kiểm tra lại các giao dịch nghiệp vụ theo U-R04 b.
- Tranh cãi về Đăng nhập, CRUD, báo cáo: chốt một lần trong QUY_UOC_DA_CHOT, rồi chạy lại. Quy ước này nên giữ nguyên cho cả P02R khi review.
- Nguồn quá mơ hồ khiến nhiều ứng viên chờ câu hỏi mở: trả lời câu hỏi, cập nhật P00, rồi chạy lại P02.
- Dùng độc lập: đính kèm tài liệu nguồn và một danh sách tác nhân (có thể viết tay), điền tối thiểu hồ sơ dự án. Khi không có P00, trích dẫn nguồn thay cho mã REQ.

## 6. Căn cứ

- OMG, Unified Modeling Language 2.5.1, chương 18 Use Cases (định nghĩa use case, observable result of value, subject).
- Alistair Cockburn, Writing Effective Use Cases (goal levels summary / user-goal / subfunction, actor-goal list, phép thử nghỉ giải lao, primary và supporting actor, số bước khuyến nghị của luồng chính).
- Craig Larman, Applying UML and Patterns, 3rd ed. (EBP test, Boss test, Size test, tìm use case từ mục tiêu tác nhân và phân tích sự kiện, gộp CRUD thành Manage X).
- Ivar Jacobson, Ian Spence, Kurt Bittner, Use-Case 2.0 (use case là mọi cách dùng hệ thống để đạt một mục tiêu cho một người dùng).
- Kurt Bittner, Ian Spence, Use Case Modeling (tránh phân rã chức năng, số lượng use case hợp lý, CRUD).
- Steve Adolph, Paul Bramble, Alistair Cockburn, Andy Pols, Patterns for Effective Use Cases (UserValuedTransactions, CompleteSingleGoal, VerbPhraseName, MergeDroplets, RedistributeTheWealth, CleanHouse).
- Daryl Kulak, Eamonn Guiney, Use Cases: Requirements in Context (use case không phải chức năng, không phải màn hình).
- Karl Wiegers, Joy Beatty, Software Requirements, 3rd ed. (bẫy use case: quá nhiều use case, đưa thiết kế và định nghĩa dữ liệu vào use case, người dùng không hiểu use case).
- Edward Yourdon, Modern Structured Analysis (phân tích sự kiện: sự kiện bên ngoài và sự kiện thời gian).
- Susan Lilly, Use Case Pitfalls: Top 10 Problems from Real Projects Using Use Cases, TOOLS 30, 1999 (viết từ góc nhìn hệ thống, quá nhiều use case).
