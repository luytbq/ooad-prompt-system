# P01 - Xác định tác nhân (Identify Actors)

## 1. Mục đích

Bước này xác định ranh giới hệ thống và toàn bộ tác nhân (actor): những vai trò người dùng, hệ thống ngoài, thiết bị và tác nhân thời gian nằm bên ngoài ranh giới và tương tác trực tiếp với hệ thống. Kết quả là danh sách tác nhân có mã ACT, loại, tính chất (chính / phụ), mục tiêu sơ bộ và truy vết về yêu cầu, cùng danh sách ứng viên đã bị loại kèm lý do.

Đây là bước đầu tiên của mô hình use case. P02 dùng mục tiêu của từng tác nhân để lập danh sách use case, P03 dùng bảng tác nhân để vẽ sơ đồ, P04 dùng tác nhân chính và phụ để viết đặc tả. Sai ở bước này (thiếu tác nhân, nhầm tác nhân với thành phần nội bộ, nhầm vai trò với cá nhân) sẽ lan sang mọi bước sau.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md | Có | Luật chung: mã định danh, khung artifact, chế độ giả định |
| Đầu vào | project-profile.md | Có | Tên hệ thống, tài liệu nguồn, chế độ giả định, ngôn ngữ |
| Đầu vào | P00-problem-brief.md | Có (khi chạy pipeline) | Bảng REQ, phạm vi, danh sách bên liên quan |
| Đầu vào | Tài liệu nguồn ghi trong hồ sơ dự án | Có | Đối chiếu câu chữ gốc khi REQ chưa đủ rõ |
| Đầu ra | P01-actors.md | - | Ranh giới hệ thống, bảng tác nhân, bên liên quan không phải tác nhân, ứng viên bị loại |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, P00-problem-brief.md và tài liệu nguồn.
- Chạy một lần cho toàn hệ thống. Chạy lại khi P00 thay đổi; khi chạy lại, giữ nguyên mã ACT đã cấp.
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| QUYET_DINH_RANH_GIOI | Tuỳ chọn | Các thành phần mà người dùng đã chốt là nằm trong hay ngoài hệ thống |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Đọc theo thứ tự: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md (tên hệ thống, tài liệu nguồn, chế độ giả định, ngôn ngữ, HE_THONG_NGOAI), P00-problem-brief.md (bảng REQ, phạm vi, danh sách bên liên quan), rồi tài liệu nguồn.
Nếu không có P00-problem-brief.md, dùng trực tiếp tài liệu nguồn: thay mã REQ bằng trích dẫn ngắn trong ngoặc kép kèm vị trí, và ghi điều này vào mục "Vấn đề còn mở".
Phạm vi lần chạy: toàn bộ hệ thống ghi trong hồ sơ dự án.

Quyết định ranh giới đã chốt trước (nếu có):
{{PH:QUYET_DINH_RANH_GIOI | Hướng dẫn: [TUỲ CHỌN] liệt kê thành phần đã được chốt nằm trong hoặc ngoài hệ thống cần xây dựng, mỗi dòng một thành phần kèm "Trong" hoặc "Ngoài". Chưa chốt gì thì thay cả khối bằng "Không có" | Ví dụ: "Cổng thanh toán của ngân hàng: Ngoài. Ứng dụng di động cho khách: Trong." ; "Hệ thống ERP của công ty: Ngoài. Máy quét mã vạch cầm tay: Ngoài. Mô-đun in phiếu xuất: Trong."}}

[Role]
Bạn là chuyên gia phân tích yêu cầu phần mềm, thành thạo mô hình use case theo UML 2.5.1 và phương pháp hướng mục tiêu của Cockburn và Larman. Bạn phân biệt chặt chẽ vai trò với cá nhân, tác nhân với bên liên quan, thứ bên ngoài với thứ bên trong hệ thống. Bạn chỉ dựa vào tài liệu nguồn, không thêm tác nhân theo kinh nghiệm về các hệ thống cùng loại.

[Action]
Thực hiện tuần tự các bước sau. Giữ ghi chép trung gian trong đầu, chỉ đưa kết quả cuối vào artifact theo [Format].

Bước 1. Xác định ranh giới hệ thống (subject).
1.1. Nêu hệ thống cần xây dựng là gì (tên trong hồ sơ dự án) và nó bao gồm những phần mềm, thiết bị nào mà dự án sẽ xây dựng hoặc chịu trách nhiệm.
1.2. Với mỗi thành phần được nhắc tới trong nguồn (phần mềm, thiết bị, hệ thống, kho dữ liệu, ứng dụng), quyết định Trong hay Ngoài theo quy tắc:
  - Trong: dự án xây dựng, cấu hình hoặc chịu trách nhiệm về hành vi của nó. Thành phần bên trong không bao giờ là tác nhân.
  - Ngoài: đã tồn tại độc lập, do bên khác sở hữu hoặc vận hành, hệ thống chỉ giao tiếp qua giao diện (API, giao thức, tệp trao đổi, tín hiệu thiết bị).
  - Nếu QUYET_DINH_RANH_GIOI đã chốt thì dùng đúng quyết định đó.
  - Thành phần có trong trường HE_THONG_NGOAI của hồ sơ dự án là Ngoài, trừ khi tài liệu nguồn nói khác; cột Căn cứ ghi "Hồ sơ dự án: HE_THONG_NGOAI".
  - Nếu nguồn không đủ để quyết định: ở chế độ NGHIEM_NGAT ghi câu hỏi Q-nn; ở chế độ CO_NHAN ghi giả định ASM-nn. Không im lặng chọn.
1.3. Kho dữ liệu của chính hệ thống (cơ sở dữ liệu, tệp lưu trữ, bộ nhớ đệm, bộ nhớ thiết bị của ứng dụng) luôn ở Trong. Một cơ sở dữ liệu thuộc sở hữu của hệ thống khác, mà hệ thống chỉ đọc hoặc ghi qua giao diện và không quản lý nội dung, thì ở Ngoài và được xét như một hệ thống ngoài.

Bước 2. Thu thập ứng viên tác nhân bằng ba nguồn, gộp lại thành một danh sách chưa lọc.
2.1. Phân tích danh từ: đọc từng REQ và câu nguồn, lấy mọi danh từ chỉ chủ thể thực hiện hành động hoặc nhận kết quả (người, bộ phận, chức danh, hệ thống, thiết bị, "hằng ngày", "định kỳ", "vào lúc").
2.2. Trả lời sáu câu hỏi, mỗi câu trả lời là một ứng viên:
  a) Ai hoặc cái gì sử dụng hệ thống?
  b) Ai hoặc cái gì nhận thông tin từ hệ thống?
  c) Ai hoặc cái gì cung cấp thông tin cho hệ thống?
  d) Hệ thống được dùng ở bộ phận, địa điểm nào trong tổ chức, bởi ai ở đó?
  e) Ai hoặc cái gì hỗ trợ, quản trị, bảo trì hệ thống (chỉ khi nguồn nêu chức năng quản trị cụ thể)?
  f) Hệ thống, thiết bị nào khác trao đổi dữ liệu với hệ thống?
2.3. Phân tích sự kiện: tìm các hành vi xảy ra theo thời điểm hoặc chu kỳ mà không có người khởi xướng (ví dụ "cuối ngày", "trước giờ hẹn 24 giờ", "mỗi tháng"). Mỗi nhóm hành vi như vậy tạo một ứng viên tác nhân thời gian. Hết giờ chờ trong một phiên đang mở của tác nhân (chờ tác nhân thao tác tiếp, chờ thiết bị hoặc hệ thống ngoài phản hồi, chờ thanh toán) không tạo ứng viên tác nhân thời gian: đó là luồng thay thế của use case đang chạy (P02 U-R07). Chỉ tạo ứng viên khi mốc thời gian rơi vào lúc không còn phiên nào của tác nhân đang mở (ví dụ lịch đặt phòng chưa đặt cọc sau 24 giờ).

Bước 3. Cho từng ứng viên qua bộ phép thử tác nhân. Một ứng viên chỉ thành tác nhân khi đạt cả sáu phép thử.
  A-T1 Bên ngoài: ứng viên nằm ngoài ranh giới đã xác định ở Bước 1.
  A-T2 Tương tác trực tiếp: ứng viên tự trao đổi thông tin với hệ thống (gửi dữ liệu, ra lệnh, nhận kết quả qua giao diện của hệ thống). Người chỉ tương tác qua một người khác (gọi điện cho nhân viên quầy, đưa giấy cho thủ thư) không phải tác nhân của tương tác đó. Người thao tác trên một thiết bị (quét thẻ, quét mã, đưa vật vào thiết bị, bấm nút trên máy) mà thiết bị chuyển thao tác đó vào hệ thống vẫn đạt phép thử này: thiết bị là kênh hoặc tác nhân phụ, không phải người trung gian (xem cột Tính chất).
  A-T3 Là vai trò: tên mô tả vai trò trong quan hệ với hệ thống, có thể do nhiều cá nhân hoặc nhiều thể hiện đảm nhận; không phải một cá nhân cụ thể, không phải một bộ phận tổ chức nếu các thành viên bộ phận làm những việc khác nhau với hệ thống.
  A-T4 Có mục tiêu hoặc có vai trò trong ít nhất một chức năng: tác nhân chính có ít nhất một mục tiêu với hệ thống; tác nhân phụ cung cấp ít nhất một dịch vụ mà nguồn nêu.
  A-T5 Phân biệt được: tập mục tiêu, quyền hoặc cách tương tác khác với mọi tác nhân còn lại. Hai ứng viên có cùng tập mục tiêu và cùng quyền là một vai trò, phải gộp.
  A-T6 Có căn cứ: truy vết được về ít nhất một REQ hoặc câu nguồn.
Ghi phép thử không đạt vào bảng ứng viên bị loại. Nếu ứng viên hỏng A-T4 nhưng là người có lợi ích với hệ thống, xếp vào nhóm bên liên quan không phải tác nhân (Bước 6).

Bước 4. Chuẩn hoá tác nhân đã giữ.
4.1. Gộp các tên đồng nghĩa chỉ cùng một vai trò (ví dụ "khách", "người đặt phòng", "khách hàng" cùng chỉ một vai trò thì chọn một tên, ghi tên còn lại vào Mô tả vai trò). Chọn cách gọi của nguồn khi cách gọi đó chỉ đúng một vai trò; khi cách gọi của nguồn quá chung ("người dùng" trong hệ thống có nhiều vai trò), đặt tên vai trò cụ thể theo thuật ngữ nghiệp vụ và ghi cách gọi của nguồn vào Mô tả vai trò. Tên tác nhân chọn ở đây là thuật ngữ chính thức mà P05 dùng cho vai trò đó (P05 F4).
4.2. Tách một ứng viên thành nhiều tác nhân khi cùng một tên nhưng thực chất là các vai trò có mục tiêu khác nhau (ví dụ "nhân viên" gồm người nhận hàng và người duyệt phiếu).
4.3. Xếp Loại: Người / Hệ thống ngoài / Thiết bị / Thời gian, theo định nghĩa trong [Format].
4.4. Xếp Tính chất: Chính / Phụ / Chính và phụ, theo quy tắc trong [Format].
4.5. Đặt tên theo quy tắc đặt tên trong [Format].

Bước 5. Xét quan hệ tổng quát hoá (generalization) giữa các tác nhân.
Chỉ tạo tác nhân cha khi đồng thời thoả:
  a) Có từ hai tác nhân con trở lên cùng tham gia một nhóm mục tiêu chung (thường từ hai mục tiêu chung trở lên), và việc gom lại làm giảm đáng kể số đường nối trên sơ đồ.
  b) Phép thử "là một": mỗi con là một loại của cha và thay được cha ở mọi chỗ cha xuất hiện; con kế thừa mọi mục tiêu của cha và có thể có thêm mục tiêu riêng.
  c) Nguồn cho thấy các tác nhân con làm các việc chung đó theo cùng một cách.
Tác nhân cha có thể là vai trò trừu tượng không có cá nhân nào chỉ đóng riêng nó (ví dụ "Người dùng nội bộ"); ghi rõ trong Mô tả vai trò là "trừu tượng".
Không dùng tổng quát hoá để mô tả cấp bậc quản lý hay sơ đồ tổ chức. Một người cấp cao hơn chỉ là con của vai trò cấp dưới khi họ thực sự làm mọi việc của vai trò đó với hệ thống.

Bước 6. Lập danh sách bên liên quan không phải tác nhân (offstage): những người hoặc tổ chức có lợi ích với kết quả của hệ thống nhưng không tương tác trực tiếp (ví dụ chủ doanh nghiệp, cơ quan thuế, khách hàng khi chỉ nhận email xác nhận qua dịch vụ email bên ngoài). Ghi mã SH tương ứng từ P00 vào cột SH của Mục 3. P04 dùng danh sách này khi viết hậu điều kiện liên quan tới bên hưởng lợi; P05 dùng để kiểm tra thuật ngữ vai trò.

Bước 7. Kiểm tra độ phủ hai chiều.
7.1. Mọi REQ loại Chức năng và Giao tiếp ngoài có ít nhất một tác nhân liên quan, hoặc có lý do.
7.2. Mọi tác nhân có ít nhất một REQ.
7.3. Không thừa: không có tác nhân mà nguồn không nhắc tới hoặc không suy ra trực tiếp được. Không thiếu: mọi chủ thể hành động trong nguồn đã được xét (giữ hoặc loại có lý do).

Bước 8. Chạy checklist ở [Target]. Sửa những mục chưa đạt; mục không sửa được thì ghi vào "Vấn đề còn mở".

[Format]
Xuất một file P01-actors.md theo khung chung của Conventions mục C5, gồm các mục theo đúng thứ tự dưới đây. Không thêm lời dẫn.

Mục 1. Ranh giới hệ thống
Một câu nêu hệ thống cần xây dựng. Sau đó là bảng:
| Thành phần | Trong / Ngoài / Chờ Q-nn | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
- Thành phần: mọi phần mềm, thiết bị, hệ thống, kho dữ liệu được nguồn nhắc tới.
- Trong / Ngoài / Chờ Q-nn: "Chờ Q-nn" chỉ dùng ở chế độ NGHIEM_NGAT khi Bước 1.2 chưa quyết định được, kèm Hệ quả "Chờ trả lời Q-nn"; ở chế độ CO_NHAN ghi Trong hoặc Ngoài và nêu ASM-nn ở cột Căn cứ.
- Hệ quả: "Là tác nhân ACT-nn", "Là thành phần nội bộ, không phải tác nhân", hoặc "Chờ trả lời Q-nn".
- Lỗi thường gặp: coi cơ sở dữ liệu, máy chủ, mô-đun, ứng dụng di động của chính hệ thống là tác nhân; bỏ sót thành phần mà nguồn chỉ nhắc thoáng qua (ví dụ "gửi tin nhắn cho khách" ngụ ý một cổng tin nhắn ngoài; ở chế độ NGHIEM_NGAT chỉ ghi nhận khi nguồn nêu rõ đó là hệ thống bên ngoài, ngược lại thành câu hỏi mở).
- Ví dụ đúng: "Cổng thanh toán của ngân hàng | Ngoài | REQ-12 | Là tác nhân ACT-05". "Cơ sở dữ liệu đơn hàng | Trong | REQ-03 | Là thành phần nội bộ, không phải tác nhân".
- Ví dụ sai: "Hệ quản trị CSDL | Ngoài | ... | Là tác nhân" (sai vì CSDL của chính hệ thống là thành phần nội bộ, dù phần mềm quản trị CSDL do hãng khác làm ra).

Mục 2. Bảng tác nhân
| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |

Cột ACT: mã ACT-nn theo Conventions C3, đánh số liên tục theo thứ tự: tác nhân người, hệ thống ngoài, thiết bị, thời gian. Tác nhân cha trừu tượng đặt ngay trước các con.

Cột Tên (VI), Tên (EN):
- Định nghĩa: tên vai trò mà cả người dùng nghiệp vụ và người phát triển đều hiểu.
- Quy tắc: danh từ hoặc cụm danh từ số ít, dùng thuật ngữ của miền nghiệp vụ; tên EN viết hoa chữ cái đầu mỗi từ (Receptionist, Payment Gateway). Tên thể hiện vai trò và trách nhiệm, không phải tên người, không phải tên sản phẩm thương mại khi vai trò quan trọng hơn sản phẩm (dùng "Cổng thanh toán" thay vì tên một hãng cụ thể, trừ khi nguồn bắt buộc đúng hãng đó; khi đó ghi tên hãng trong Mô tả vai trò).
- Chức danh chỉ được dùng làm tên khi chức danh đó ứng với đúng một vai trò trong hệ thống. Nếu một chức danh đóng nhiều vai trò khác nhau, hoặc nhiều chức danh cùng đóng một vai trò, đặt tên theo vai trò.
- Hệ thống ngoài: tên theo dịch vụ nó cung cấp cho hệ thống (Cổng SMS, Hệ thống ERP, Cổng thanh toán). Thiết bị: tên loại thiết bị (Máy quét mã vạch, Cảm biến chỗ đỗ). Thời gian: "Bộ định thời" (EN: Timer) hoặc tên nêu chu kỳ khi có nhiều nhịp độc lập ("Bộ định thời cuối ngày").
- Ví dụ đúng: "Lễ tân / Receptionist", "Thủ kho / Storekeeper", "Tài xế / Driver", "Cổng SMS / SMS Gateway", "Bộ định thời / Timer".
- Ví dụ sai: "Chị Lan" (tên người); "Người dùng" khi hệ thống có nhiều vai trò khác nhau (quá chung, che mất sự khác biệt về quyền); "Phòng kế toán" khi trong phòng có người lập phiếu và người duyệt phiếu (bộ phận, không phải vai trò); "MySQL" (thành phần nội bộ, tên công nghệ); "Màn hình đặt lịch" (giao diện của chính hệ thống).

Cột Loại:
- Người: vai trò do con người đảm nhận, tương tác qua giao diện người dùng.
- Hệ thống ngoài: phần mềm độc lập bên ngoài ranh giới, trao đổi qua giao diện máy (API, tệp, hàng đợi thông điệp). Hệ thống ngoài có thể là tác nhân chính (tự gửi yêu cầu tới hệ thống) hoặc phụ.
- Thiết bị: phần cứng bên ngoài có hành vi riêng và giao thức riêng mà hệ thống phải giao tiếp (máy quét mã vạch gửi mã, cảm biến gửi tín hiệu, barrier nhận lệnh mở, máy in hoá đơn nhận lệnh in). Bàn phím, chuột, màn hình cảm ứng mà con người dùng để thao tác không phải tác nhân: người thao tác mới là tác nhân.
- Thời gian: tác nhân đại diện cho sự kiện theo lịch, khởi xướng các chức năng chạy định kỳ hoặc tại một thời điểm mà nguồn nêu rõ, không có người hay hệ thống nào ra lệnh. Chỉ tạo khi nguồn có hành vi như vậy. Tác vụ kỹ thuật (sao lưu, dọn nhật ký) không tạo tác nhân thời gian nếu nguồn chỉ nêu như yêu cầu phi chức năng.

Cột Tính chất:
- Chính: tác nhân khởi xướng tương tác để đạt mục tiêu của mình với hệ thống (người gọi hệ thống phục vụ mình). Tác nhân thời gian luôn là Chính.
- Phụ (supporting): tác nhân cung cấp dịch vụ cho hệ thống trong quá trình phục vụ tác nhân chính; hệ thống là bên gọi nó (cổng thanh toán trừ tiền, cổng SMS gửi tin, máy in in phiếu). Người cũng có thể là tác nhân phụ khi hệ thống cần họ tham gia một bước (ví dụ người duyệt được hệ thống yêu cầu xác nhận trong cùng phiên).
- Chính và phụ: tác nhân là Chính trong một số chức năng và Phụ trong chức năng khác.
- Phép thử phân biệt: "Ai muốn điều này xảy ra và bắt đầu nó?" là Chính. "Ai được hệ thống nhờ làm một phần việc?" là Phụ.
- Người tác động lên hệ thống qua một thiết bị (quét thẻ hoặc mã, đưa vật vào thiết bị, bấm nút trên máy): tác nhân chính là người có mục tiêu, theo phép thử "Ai muốn kết quả này?", không phải thiết bị nhận thao tác. Thiết bị là tác nhân Phụ khi nó là thiết bị hoặc hệ thống nằm ngoài ranh giới, có giao tiếp riêng với hệ thống (gửi tín hiệu, nhận lệnh theo giao thức riêng); thiết bị chỉ là kênh nhập, không phải tác nhân, khi nó thuộc ranh giới (Bước 1.2). Thiết bị chỉ là tác nhân Chính khi nó tự phát sự kiện mà không có người nào có mục tiêu đứng sau (cảm biến tự báo, đồng hồ đo tự gửi số liệu). Nguồn chưa nêu ai thao tác trên thiết bị: ghi Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN) về vai trò người thao tác, không lấy thiết bị làm tác nhân chính thay cho người.
  Ví dụ (quản lý kho): thủ kho quét mã vạch từng kiện hàng để ghi nhận hàng nhập. Thủ kho là tác nhân chính; Máy quét mã vạch là tác nhân phụ khi là thiết bị ngoài ranh giới có giao thức riêng, hoặc chỉ là kênh nhập khi dự án cung cấp nó như một phần của hệ thống. Ví dụ (bãi đỗ xe): cảm biến chỗ đỗ báo chỗ trống khi xe rời đi; không người nào tìm tới hệ thống với mục tiêu này, nên Cảm biến chỗ đỗ là tác nhân chính của việc cập nhật tình trạng chỗ đỗ. Trong cùng bãi, tài xế quẹt thẻ tại barrier để ra bãi thì Tài xế là tác nhân chính, Barrier là tác nhân phụ.
- Người nhận kết quả thụ động qua kênh bên ngoài (nhận SMS, nhận email) không phải tác nhân của chức năng đó; kênh gửi (Cổng SMS, Hệ thống email) mới là tác nhân phụ nếu nằm ngoài ranh giới. Người nhận được ghi ở Mục 3.
- Ví dụ: trong hệ thống giao đồ ăn, Khách hàng là Chính khi đặt món, Cổng thanh toán là Phụ khi hệ thống yêu cầu trừ tiền. Nếu Cổng thanh toán tự gửi thông báo kết quả thanh toán vào một thời điểm không xác định và việc đó khởi động một xử lý riêng, thì Cổng thanh toán là "Chính và phụ".

Cột Mô tả vai trò:
- 1-3 câu: vai trò là ai trong tổ chức hoặc hệ sinh thái, tương tác với hệ thống qua đâu, các tên đồng nghĩa đã gộp, cá nhân hoặc chức danh nào thường đóng vai trò này nếu nguồn nêu. Với tác nhân cha ghi "Vai trò trừu tượng, gom phần chung của ACT-xx, ACT-yy".
- Không liệt kê chức năng chi tiết (thuộc P02).

Cột Mục tiêu với hệ thống:
- Tác nhân chính: 1-5 mục tiêu ở mức nghiệp vụ, mỗi mục tiêu một cụm động từ, ngăn bằng thẻ br. Đây là mục tiêu sơ bộ để P02 lập danh sách mục tiêu tác nhân; không cần đủ chi tiết như use case.
- Tác nhân phụ: dịch vụ cung cấp cho hệ thống, bắt đầu bằng "Cung cấp:" (ví dụ "Cung cấp: gửi tin nhắn tới số điện thoại").
- Tác nhân thời gian: các thời điểm hoặc chu kỳ kích hoạt (ví dụ "Kích hoạt: 24 giờ trước mỗi lịch hẹn").
- Ví dụ đúng (Thủ thư): "Cho mượn sách<br>Nhận trả sách<br>Cập nhật danh mục sách".
- Ví dụ sai (Thủ thư): "Nhấn nút Lưu<br>Đăng nhập" (thao tác giao diện và điều kiện truy cập, không phải mục tiêu nghiệp vụ; đăng nhập được xét riêng ở P02).

Cột Tổng quát hoá từ: mã ACT của tác nhân cha nếu có, ngược lại "-".

Cột REQ: danh sách mã REQ chứng minh sự tồn tại và vai trò của tác nhân.

Mục 3. Bên liên quan không phải tác nhân
| SH | Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
Cột SH: mã SH-nn tương ứng trong bảng bên liên quan của P00; P00 không có bên liên quan này thì ghi "-".
- Ví dụ đúng: "SH-03 | Bệnh nhân (khi đặt lịch qua điện thoại) | Có lịch khám đúng giờ mong muốn | ACT-02 Lễ tân | REQ-04".
- Ví dụ đúng: "SH-01 | Chủ kho | Số liệu tồn kho chính xác để ra quyết định nhập hàng | Báo cáo do ACT-03 Kế toán kho lập | REQ-15".
Nếu không có, ghi "Không có".

Mục 4. Ứng viên tác nhân bị loại
| Ứng viên | Lý do loại | REQ |
- Lý do loại phải nêu phép thử không đạt (A-T1 đến A-T6) và giải thích một câu, hoặc nêu "Gộp vào ACT-nn" khi là tên đồng nghĩa.
- Mỗi danh từ chủ thể trong nguồn mà không thành tác nhân phải xuất hiện ở bảng này hoặc ở Mục 3, để người đọc thấy nó đã được xét.
- Ví dụ đúng: "Cơ sở dữ liệu | A-T1: thành phần nội bộ của hệ thống | REQ-03". "Khách vãng lai | Gộp vào ACT-01 Khách hàng: cùng mục tiêu và cùng quyền | REQ-01". "Máy chủ | A-T1: hạ tầng của chính hệ thống | -". "Kế toán trưởng | A-T2: chỉ nhận báo cáo in từ Kế toán kho, không thao tác trên hệ thống | REQ-15 (xếp vào Mục 3)".

Mục 5. Các mục kiểm soát theo Conventions C5: Câu hỏi mở, Giả định (chỉ khi CO_NHAN), Đề xuất sửa artifact trước, Vấn đề còn mở.

Mức hợp lý (heuristic, không phải luật cứng; lệch thì kiểm tra lại, không tự ép số):
- Số tác nhân người thường từ 2 đến khoảng 8 với một hệ thống cỡ vừa. Nhiều hơn thường là dấu hiệu đặt tên theo chức danh thay vì vai trò, hoặc chưa gộp các tên đồng nghĩa. Chỉ có 1 tác nhân người thường là dấu hiệu thiếu vai trò quản trị hoặc vận hành mà nguồn có nêu.
- Mỗi tác nhân chính thường có 1-5 mục tiêu sơ bộ ở bước này.
- Cây tổng quát hoá tác nhân không quá 2 tầng; sâu hơn thường là mô tả sơ đồ tổ chức.

Lỗi thường gặp cần tự soát:
- Nhầm tác nhân với thành phần nội bộ: CSDL, máy chủ, mô-đun, "hệ thống" chính nó, ứng dụng di động do dự án làm.
- Nhầm tác nhân với cá nhân hoặc chức danh: "Anh Minh", "Giám đốc" (khi giám đốc chỉ xem báo cáo giống quản lý).
- Nhầm tác nhân với bên liên quan: người có lợi ích nhưng không thao tác (chủ doanh nghiệp, cơ quan quản lý, người nhận SMS).
- Nhầm thiết bị nhập liệu của con người với tác nhân thiết bị: bàn phím, chuột, màn hình.
- Lấy thiết bị làm tác nhân chính khi có người thao tác trên thiết bị đó để đạt mục tiêu của mình (máy quét, đầu đọc thẻ, barrier); người thao tác mới là tác nhân chính.
- Tạo tác nhân thời gian cho hết giờ chờ trong một phiên đang mở (đó là luồng thay thế của use case đang chạy).
- Tạo tác nhân cho mỗi quyền (Người thêm sách, Người xoá sách) thay vì cho mỗi vai trò.
- Bỏ sót tác nhân phụ: hệ thống ngoài mà nguồn nêu rõ là hệ thống sẽ gọi tới.
- Bỏ sót tác nhân thời gian khi nguồn có hành vi định kỳ.
- Dùng tổng quát hoá sai chiều (tam giác rỗng phải ở phía tác nhân cha) hoặc không thoả phép thử "là một".

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Bảng ranh giới liệt kê mọi thành phần mà nguồn nhắc tới, mỗi thành phần có quyết định Trong hoặc Ngoài có căn cứ.
2. Không có tác nhân nào là thành phần bên trong ranh giới (kể cả CSDL của hệ thống).
3. Mọi tác nhân đạt cả sáu phép thử A-T1 đến A-T6.
4. Mọi tên tác nhân là vai trò, số ít, thuật ngữ nghiệp vụ; không có tên người, tên bộ phận chung chung, tên công nghệ.
5. Mọi tác nhân có đủ Loại, Tính chất, Mục tiêu với hệ thống và ít nhất một REQ.
6. Không có hai tác nhân cùng tập mục tiêu và cùng quyền.
7. Mọi quan hệ tổng quát hoá thoả phép thử "là một" và có ít nhất hai con.
8. Mọi REQ loại Chức năng và Giao tiếp ngoài liên quan tới ít nhất một tác nhân, hoặc có lý do trong "Vấn đề còn mở".
9. Mọi danh từ chủ thể trong nguồn đã được xét: là tác nhân, là bên liên quan ở Mục 3, hoặc là ứng viên bị loại ở Mục 4.
10. Không có tác nhân hoặc mục tiêu nào dựa trên hiểu biết chung ngoài nguồn; chỗ thiếu đã thành Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN).
11. Artifact có đủ các mục kiểm soát theo C5, mục trống ghi "Không có".

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho bước này; ưu tiên cao hơn quy tắc mặc định của bước (trừ Conventions C1). Không có thì thay cả khối bằng "Không có" | Ví dụ: "Không tạo tác nhân thời gian; các tác vụ định kỳ coi là yêu cầu phi chức năng." ; "Gộp Lễ tân và Điều phối viên thành một tác nhân vì phòng khám chỉ có một vị trí." ; "Tên tiếng Anh của tác nhân dùng theo danh mục vai trò của tổ chức: Clerk, Supervisor."}}
````

## 5. Ghi chú cho người dùng

- Kết quả có tác nhân "Người dùng" duy nhất cho mọi chức năng: nguồn chưa phân vai rõ. Kiểm tra lại P00 hoặc trả lời câu hỏi mở về phân quyền, rồi chạy lại.
- Kết quả có quá nhiều tác nhân người (trên 8-10): thường do đặt tên theo chức danh. Ghi vào YEU_CAU_BO_SUNG danh sách vai trò đã chốt rồi chạy lại.
- Tranh cãi về một thành phần (ví dụ ứng dụng di động có phải một hệ thống riêng không): chốt ở QUYET_DINH_RANH_GIOI thay vì để AI suy đoán.
- Dùng độc lập (không chạy pipeline): chỉ cần đính kèm tài liệu nguồn và điền nhanh hồ sơ dự án (tối thiểu TEN_HE_THONG, TAI_LIEU_NGUON, CHE_DO_GIA_DINH). Khi không có P00, AI sẽ dùng trích dẫn nguồn thay cho mã REQ.
- Muốn kiểm tra chéo một danh sách tác nhân có sẵn: dùng P02R-review-use-cases.md (có phần tiêu chí tác nhân).

## 6. Căn cứ

- OMG, Unified Modeling Language 2.5.1, chương 18 Use Cases (Actor, subject, ràng buộc association của actor, generalization).
- Alistair Cockburn, Writing Effective Use Cases (primary actor, supporting actor, offstage actor, stakeholders and interests, phạm vi và ranh giới).
- Craig Larman, Applying UML and Patterns, 3rd ed. (primary / supporting / offstage actor, cách tìm tác nhân và mục tiêu).
- Kurt Bittner, Ian Spence, Use Case Modeling (actor là vai trò, ranh giới hệ thống).
- Scott W. Ambler, The Elements of UML 2.0 Style (tác nhân mô hình hoá vai trò không phải chức danh, tên danh từ số ít, tác nhân Time cho sự kiện theo lịch, tác nhân không tương tác với nhau, quy tắc "is like" cho kế thừa tác nhân).
- Susan Lilly, Use Case Pitfalls: Top 10 Problems from Real Projects Using Use Cases, TOOLS 30, 1999 (ranh giới không rõ, tên tác nhân không nhất quán).
