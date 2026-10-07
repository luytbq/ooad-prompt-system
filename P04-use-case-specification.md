# P04 - Đặc tả use case và activity diagram (Use Case Specification)

## 1. Mục đích

Bước này viết đặc tả chi tiết cho một use case: mô tả ngắn, tiền điều kiện, hậu điều kiện, luồng sự kiện chính, luồng thay thế và ngoại lệ, dữ liệu vào ra, quy tắc nghiệp vụ, yêu cầu đặc biệt, kèm activity diagram có swimlane. Chạy lặp, mỗi lần một use case.

Đặc tả use case là hợp đồng hành vi giữa tác nhân và hệ thống. Bước phân tích use case (lớp boundary, control, entity và sequence diagram) sẽ đi theo từng bước của luồng sự kiện ở đây, nên mỗi bước phải rõ ai làm, làm gì, trao đổi thông tin gì. Quy tắc nghiệp vụ phát hiện ở bước này được cấp mã BR qua một sổ đăng ký chung, để các lần chạy cho các use case khác nhau không trùng mã.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md | Có | Luật chung |
| Đầu vào | project-profile.md | Có | Tên hệ thống, chế độ giả định, ngôn ngữ |
| Đầu vào | Tài liệu nguồn trong TAI_LIEU_NGUON | Có | Tra câu gốc khi REQ chưa đủ chi tiết |
| Đầu vào | P00-problem-brief.md | Có | REQ, câu hỏi mở đã có |
| Đầu vào | P01-actors.md | Có | Tên tác nhân chính thức |
| Đầu vào | P02-usecases.md | Có | Tên, tác nhân, mục tiêu, sự kiện kích hoạt, REQ của use case |
| Đầu vào | P03-usecase-model.md | Có | Quan hệ include, extend, generalization và điểm mở rộng; chỉ cần Mục 1 và Mục 2 |
| Đầu vào | P04-uc-specs/_BR-register.md | Có nếu đã tồn tại | Sổ đăng ký BR: mã BR đã cấp ở các lần chạy trước |
| Đầu vào | Đặc tả P04 của use case liên quan (được include, extend, cha) | Tuỳ chọn | Giữ nhất quán điểm gọi, điểm mở rộng, bước quay lại |
| Đầu vào | Mục Câu hỏi mở và Giả định của mọi đặc tả P04 đã có | Có nếu đã tồn tại | Cấp tiếp mã Q, ASM từ số lớn nhất (Conventions C3) |
| Đầu vào | P05-glossary.md, P06-supplementary-spec.md | Tuỳ chọn (khi chạy lại) | Dùng đúng thuật ngữ, đúng mã BR đã hợp nhất |
| Đầu ra | P04-uc-specs/UC-nnn-slug.md | | Đặc tả use case và bảng mô hình activity diagram |
| Đầu ra | diagrams/P04-activity-UC-nnn.drawio | | Activity diagram |
| Đầu ra | P04-uc-specs/_BR-register.md | | Sổ đăng ký BR đã cập nhật (toàn bộ file) |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, tài liệu nguồn, P00, P01, P02, P03, sổ BR (nếu đã có), đặc tả của các use case liên quan (nếu đã có), mục Câu hỏi mở và Giả định của các đặc tả P04 đã có (để cấp tiếp mã Q, ASM).
- Mỗi lần chạy chỉ dùng phần của artifact đầu vào liên quan tới UC_ID:

| Artifact | Phần cần dùng |
|---|---|
| P00-problem-brief.md | Các dòng REQ ghi ở cột REQ của UC_ID trong P02, các dòng REQ loại Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng, Giao tiếp ngoài về cùng đối tượng nghiệp vụ, và các Q-nn liên quan tới các REQ đó |
| P01-actors.md | Mục 2 (bảng tác nhân); đủ nếu chỉ lấy các dòng tác nhân chính, phụ của UC_ID |
| P02-usecases.md | Dòng UC_ID trong bảng 4a và bảng 4b của Mục 4; dòng EV của sự kiện kích hoạt ở Mục 2 |
| P03-usecase-model.md | Các dòng của Mục 1 (bảng quan hệ) và Mục 2 (điểm mở rộng) có UC_ID; không cần bảng Node, Edge và nội dung .drawio |
| Sổ BR, mục Câu hỏi mở và Giả định của các đặc tả P04 đã có | Toàn bộ (cần để cấp tiếp mã) |
| Tài liệu nguồn | Toàn bộ, hoặc các đoạn chứa câu trích của các REQ trên khi nguồn dài |

- Khi chạy bằng chat với cửa sổ ngữ cảnh nhỏ, nhất là khi lặp P04 cho nhiều use case trong cùng cuộc trò chuyện: dán trích đoạn theo bảng trên thay cho cả file P00, P01, P02, P03, kèm một dòng ghi rõ "Trích đoạn liên quan UC-nnn của <file>". Khi chạy bằng agent có quyền đọc file, đính kèm đủ file; agent tự lấy phần cần dùng.
- Lặp cho từng use case. Chạy tuần tự, không chạy song song hai use case cùng lúc, vì mỗi lần chạy đọc và ghi sổ BR. Sau mỗi lần chạy, lưu lại sổ BR mới trước khi chạy use case tiếp theo.
- Thứ tự gợi ý: use case cơ sở (base) trước, use case được include và use case mở rộng (extend) sau; use case cha trước use case con. Như vậy điểm gọi và điểm mở rộng đã có sẵn khi viết use case phụ thuộc.
- Placeholder trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| UC_ID | Có | Mã use case cần đặc tả trong lần chạy này |
| TEN_HE_THONG_TRONG_LUONG | Tuỳ chọn | Chủ ngữ dùng cho các bước do hệ thống thực hiện |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Quy định riêng của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md, tài liệu nguồn, P00-problem-brief.md, P01-actors.md, P02-usecases.md, P03-usecase-model.md (mỗi file có thể chỉ là trích đoạn liên quan tới use case cần đặc tả; P03 có thể chỉ gồm Mục 1 và Mục 2), và có thể có: P04-uc-specs/_BR-register.md (sổ đăng ký quy tắc nghiệp vụ), đặc tả P04 của các use case liên quan, mục Câu hỏi mở và Giả định của các đặc tả P04 đã có, P05-glossary.md, P06-supplementary-spec.md.

Đây là bước P04 của pipeline. Lần chạy này đặc tả đúng một use case:
{{PH:UC_ID | Hướng dẫn: mã use case trong P02-usecases.md, đúng định dạng UC-nnn, chỉ một mã mỗi lần chạy | Ví dụ: "UC-003" (Đặt lịch tái khám, hệ thống phòng khám); "UC-007" (Gia hạn phiếu mượn, hệ thống thư viện)}}

Chủ ngữ cho các bước do hệ thống thực hiện:
{{PH:TEN_HE_THONG_TRONG_LUONG | Hướng dẫn: [TUỲ CHỌN] một danh từ ngắn, dùng nhất quán trong cột "Thực hiện bởi" và tên swimlane. Để dùng mặc định "Hệ thống" thì thay cả khối bằng "Không có" | Ví dụ: "Hệ thống"; "Phần mềm ClinicBook"; "WMS-Lite"}}

Đặc tả này là đầu vào của bước phân tích use case (lớp boundary, control, entity, sequence diagram), của glossary và của đặc tả bổ sung. Các bước đó đọc bảng luồng sự kiện theo số bước, đọc mã BR, nên cấu trúc bảng và cách đánh số phải đúng như phần Format.

[Role]
Bạn là chuyên gia phân tích yêu cầu, viết đặc tả use case theo phong cách RUP kết hợp hướng dẫn viết bước của Cockburn, và vẽ activity diagram đúng UML 2.5.1. Bạn viết cho hai nhóm người đọc: người nghiệp vụ (phải hiểu được mà không cần biết kỹ thuật) và người thiết kế (phải suy ra được trách nhiệm của hệ thống ở từng bước).

[Action]
Thực hiện tuần tự:

1. Thu thập đầu vào của use case UC_ID:
   a. Từ P02 Mục 4: tên (VI, EN), tác nhân chính, tác nhân phụ (bảng 4a); mục tiêu, mô tả ngắn, sự kiện kích hoạt, danh sách REQ (bảng 4b).
   b. Từ P03: mọi quan hệ mà UC_ID tham gia: include (UC_ID là base hay là use case được include), extend (UC_ID là base hay là extension, tên điểm mở rộng, điều kiện), generalization (UC_ID là cha hay con).
   c. Từ P00 và tài liệu nguồn: mọi câu trích của các REQ trên, cùng các REQ loại Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng, Giao tiếp ngoài liên quan tới cùng đối tượng nghiệp vụ. Ghi các REQ này vào danh sách truy vết.
   d. Từ sổ BR (nếu có): danh sách mã BR đã cấp và nội dung.
   e. Các câu hỏi mở Q-nn trong P00 liên quan tới use case này. Tìm mã Q và ASM lớn nhất trong P00 đến P03 và trong mọi đặc tả P04 đã có; Q, ASM mới của lần chạy này cấp tiếp từ số đó (Conventions C3).
   Nếu UC_ID không có trong P02, dừng và báo lỗi. Nếu đầu vào là trích đoạn mà thiếu một phần cần dùng (dòng REQ được P02 dẫn nhưng không có trong trích đoạn P00), ghi Q-nn "Thiếu đầu vào" nêu rõ phần thiếu, không suy đoán nội dung.
2. Xác định điểm bắt đầu và điểm kết thúc thành công: sự kiện nào khởi động use case (tác nhân yêu cầu, hệ thống ngoài gửi dữ liệu, hay tới thời điểm định trước), và kết quả quan sát được nào đánh dấu mục tiêu của tác nhân chính đã đạt.
3. Viết luồng sự kiện chính (kịch bản thành công điển hình, một mạch từ đầu tới cuối) theo quy tắc F4: liệt kê các cặp tác nhân yêu cầu, hệ thống phản hồi; thêm các bước hệ thống kiểm tra, tính toán, lưu, thông báo mà nguồn nêu. Tại điểm gọi use case được include, viết bước gọi tường minh.
4. Rà từng bước của luồng chính và hỏi: bước này có thể diễn ra khác đi không (biến thể thông thường), có trường hợp lạ không, có thể thất bại không (dữ liệu sai, không đủ điều kiện, tài nguyên bị khoá, hệ thống ngoài không phản hồi, tác nhân huỷ). Chỉ giữ các trường hợp có căn cứ trong nguồn hoặc suy ra trực tiếp từ một quy tắc nghiệp vụ đã có (ví dụ quy tắc "tối đa 5 cuốn" suy ra trường hợp đã đủ 5 cuốn). Trường hợp chỉ có trong hiểu biết chung thì ghi thành Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN). Trường hợp vi phạm một quy tắc nghiệp vụ đã có là suy ra trực tiếp; phản hồi mặc định của hệ thống cho trường hợp đó theo F5.7, không cần Q-nn. Hết thời hạn chờ một sự kiện mà nguồn nêu thời hạn là suy ra trực tiếp (F4.2 mục 15).
5. Viết luồng thay thế và ngoại lệ theo quy tắc F5, gồm cả nhánh chèn use case mở rộng tại điểm mở rộng.
6. Viết tiền điều kiện, hậu điều kiện theo F3.
7. Lập bảng dữ liệu vào, dữ liệu ra theo F6 cho các bước có trao đổi thông tin.
8. Tách quy tắc nghiệp vụ theo F7: tìm mọi chính sách, giới hạn, công thức, điều kiện nghiệp vụ nằm trong các bước và bảng dữ liệu, đưa ra bảng BR, đối chiếu sổ BR để dùng lại mã cũ hoặc cấp mã mới, rồi cập nhật sổ BR.
9. Ghi yêu cầu đặc biệt (F8), thông tin bổ sung và kịch bản chính (F9).
10. Dựng activity diagram theo F10: bảng Node, bảng Edge, rồi sinh file .drawio từ hai bảng đó.
11. Đối chiếu chéo: mỗi bước luồng chính có đúng một action; mỗi luồng thay thế có một nhánh từ decision; mọi điểm quay lại khớp giữa bảng luồng và sơ đồ; mọi BR trong bảng BR có trong sổ BR.
12. Chạy checklist ở phần [Target], sửa những gì chưa đạt, ghi phần không sửa được vào mục "Vấn đề còn mở".

[Format]
Xuất ba nội dung. Nếu có quyền ghi file thì ghi thành file; nếu không thì in lần lượt, mỗi nội dung mở đầu bằng một dòng "File: <đường dẫn>".

A. File P04-uc-specs/UC-nnn-slug.md (slug theo Conventions C4), theo khung C5, gồm đúng các mục sau theo thứ tự:

# P04 - Đặc tả use case UC-nnn <Tên VI> - <TEN_HE_THONG>
(bảng thông tin theo C5, Phạm vi ghi UC-nnn)
## 1. Thông tin chung
## 2. Luồng sự kiện chính
## 3. Luồng sự kiện thay thế và ngoại lệ
## 4. Luồng con            (chỉ khi có, xem F4.6; không có thì ghi "Không có")
## 5. Dữ liệu vào và dữ liệu ra
## 6. Quy tắc nghiệp vụ
## 7. Yêu cầu đặc biệt
## 8. Thông tin bổ sung
## 8a. Kịch bản chính      (chỉ khi DAY_DU, xem F9)
## 9. Activity diagram
## Câu hỏi mở
## Giả định                (chỉ khi CO_NHAN)
## Đề xuất sửa artifact trước
## Vấn đề còn mở

B. File diagrams/P04-activity-UC-nnn.drawio (F10.6).

C. File P04-uc-specs/_BR-register.md đã cập nhật (F7.4).

Quy tắc chi tiết cho từng thành phần:

F1. Bảng thông tin chung
Bảng hai cột | Thuộc tính | Giá trị |, các hàng theo đúng thứ tự:
| Mã use case | UC-nnn |
| Tên use case | Tên VI (Tên EN), đúng như P02 |
| Tác nhân chính | ACT-nn Tên |
| Tác nhân phụ | ACT-nn Tên, hoặc "Không có" |
| Mô tả ngắn | theo F2 |
| Sự kiện kích hoạt | từ P02 |
| Tiền điều kiện | theo F3 |
| Hậu điều kiện (thành công) | theo F3 |
| Hậu điều kiện tối thiểu | theo F3 |
| Quan hệ | liệt kê từ P03, mỗi dòng một quan hệ, ví dụ "«include» UC-009 Thanh toán trực tuyến (tại bước 8)"; "Được mở rộng bởi UC-012 Chọn giao hàng hẹn giờ tại điểm mở rộng 'Chọn thời điểm giao'"; "Là con của UC-004 Xác thực người dùng". Không có thì "Không có" |
| Điểm mở rộng | tên điểm mở rộng và bước đặt điểm đó, chỉ khi UC_ID là base của extend; không có thì "Không có" |
| REQ | danh sách REQ truy vết |
Tên tác nhân và tên use case chép đúng từ P01, P02; không đổi cách gọi.

F2. Mô tả ngắn
- Định nghĩa: 1-3 câu nêu mục đích của use case và giá trị tác nhân chính nhận được.
- Mẫu câu: "Use case này mô tả tương tác giữa <tác nhân> và <hệ thống> khi <tác nhân> muốn <mục tiêu>." Có thể thêm một câu về kết quả.
- Lỗi thường gặp: kể lại các bước (quá chi tiết); chỉ lặp tên use case ("Use case cho phép đặt lịch"); nêu giao diện ("màn hình đặt lịch").
- Đúng: "Use case này mô tả tương tác giữa bạn đọc và hệ thống khi bạn đọc muốn gia hạn thời hạn trả của một cuốn sách đang mượn. Kết quả là ngày hết hạn mới được ghi nhận."
- Sai: "Bạn đọc đăng nhập, chọn sách, bấm nút Gia hạn, hệ thống hiện thông báo." (kể bước, dùng từ giao diện)

F3. Tiền điều kiện và hậu điều kiện
- Tiền điều kiện: trạng thái của hệ thống phải đúng trước khi use case bắt đầu. Hệ thống không kiểm tra lại tiền điều kiện trong luồng sự kiện; điều gì cần kiểm tra trong luồng thì không phải tiền điều kiện.
  - Viết dạng mệnh đề trạng thái kiểm chứng được, mỗi điều kiện một dòng (ngăn bằng <br>).
  - Không nhắc tới use case khác theo kiểu thứ tự thực hiện ("Đã thực hiện UC Đăng nhập"). Được nêu trạng thái mà use case khác tạo ra ("Thủ kho đã được xác thực và đang có phiên làm việc").
  - Không có tiền điều kiện thực sự thì ghi "Không có". Không bịa để lấp chỗ trống.
  - Đúng: "Bạn đọc đã được xác thực.<br>Bạn đọc có ít nhất một phiếu mượn chưa trả."
  - Sai: "Bạn đọc muốn gia hạn sách." (đây là sự kiện kích hoạt, không phải trạng thái); "Sách chưa quá hạn." (điều này hệ thống phải kiểm tra trong luồng, vì có thể sai, nên là luồng thay thế)
- Hậu điều kiện (thành công): trạng thái hệ thống sau khi luồng chính kết thúc: dữ liệu nào được tạo, đổi, trạng thái nào chuyển, thông báo nào đã gửi. Kiểm chứng được bằng cách xem dữ liệu của hệ thống.
  - Đúng: "Phiếu mượn có ngày hết hạn mới bằng ngày hết hạn cũ cộng thời hạn gia hạn; số lần gia hạn của phiếu tăng 1."
  - Sai: "Bạn đọc hài lòng." (không kiểm chứng được); "Hệ thống hiển thị thông báo thành công." (đây là hành động, không phải trạng thái; chỉ ghi nếu thông báo được lưu hoặc gửi đi)
- Hậu điều kiện tối thiểu: điều hệ thống bảo đảm cả khi use case kết thúc ở bất kỳ luồng thất bại nào, thường là "không có thay đổi dở dang" hoặc "lần thử được ghi nhận". Chỉ ghi điều có căn cứ; nếu không có gì thì ghi "Không có thay đổi dữ liệu nào được lưu" khi mọi luồng thất bại đều kết thúc trước bước lưu, ngược lại ghi Q-nn.
  - Đúng: "Nếu use case kết thúc không thành công, tồn kho và phiếu nhập không thay đổi."
- Không lặp nội dung giữa hai hàng; không nêu use case sẽ chạy tiếp theo.

F4. Luồng sự kiện chính
Bảng: | STT | Thực hiện bởi | Hành động |
F4.1 Định nghĩa: một kịch bản thành công điển hình từ sự kiện kích hoạt tới khi mục tiêu của tác nhân chính đạt được. Chỉ một luồng chính; không có nhánh.
F4.2 Quy tắc viết bước:
  1. STT là số nguyên 1, 2, 3... liên tục. Không có bước con 3.1 trong luồng chính (dùng luồng con F4.6 nếu cần).
  2. Thực hiện bởi: tên tác nhân chính xác như P01, hoặc chủ ngữ hệ thống thống nhất (mặc định "Hệ thống"). Tác nhân thời gian không bao giờ là chủ thể của một bước (xem mục 10). Tác nhân phụ (hệ thống ngoài) là chủ thể của một bước khi nó trả về thông tin mà luồng dùng tiếp: "Cổng thanh toán | Trả về kết quả giao dịch." Khi hệ thống chỉ gửi đi mà không chờ kết quả (gửi email, gửi SMS), viết một bước của hệ thống nêu rõ tác nhân phụ nhận: "Hệ thống | Gửi email xác nhận cho bạn đọc qua dịch vụ email."
  3. Hành động bắt đầu bằng động từ, ở thể chủ động, thì hiện tại, một hành động có mục đích mỗi bước. Chủ ngữ đã ở cột "Thực hiện bởi", cột Hành động không lặp chủ ngữ.
  4. Viết theo cặp yêu cầu - phản hồi: sau bước tác nhân gửi thông tin là bước hệ thống phản hồi (kiểm tra, xử lý, hiển thị). Hai bước tác nhân liên tiếp chỉ khi tác nhân làm hai việc có ý nghĩa nghiệp vụ khác nhau; "nhập" và "gửi" cùng một thông tin gộp thành một bước ("nhập và gửi thông tin giao hàng").
  5. Bước của hệ thống nêu kết quả nghiệp vụ, không nêu cách cài đặt: "kiểm tra số cuốn đang mượn của bạn đọc", không phải "truy vấn bảng loans"; "lưu phiếu mượn", không phải "insert vào CSDL".
  6. Không dùng từ ngữ giao diện. Tránh: nhấn, bấm, click, nút, mở, đóng, cửa sổ, pop-up, hộp thoại, form, biểu mẫu, ô nhập, trường (trong câu hành động), danh sách thả xuống, cuộn, kéo, thả, duyệt, màn hình X, bản ghi. Dùng: yêu cầu, chọn, nhập, cung cấp, chỉ định, gửi, xác nhận, khởi động, hiển thị, thông báo, nhắc (tác nhân cung cấp).
  7. Không nhắc tới luồng thay thế trong luồng chính, không có "nếu". Điều kiện rẽ nhánh nằm ở F5. Bước kiểm tra viết dạng "kiểm tra <điều kiện>", kết quả thành công ngầm hiểu ở bước sau.
  8. Nêu rõ thông tin trao đổi ở mức nghiệp vụ, dẫn tới bảng dữ liệu khi nhiều trường: "nhập tiêu chí tìm kiếm (xem Dữ liệu vào 1)".
  9. Lặp lại: viết bằng một bước "Lặp lại bước 3-4 cho đến khi <điều kiện>" hoặc "với mỗi <đối tượng>, <hành động>". Không vẽ lặp bằng cách chép bước.
  10. Bước đầu tiên là sự kiện kích hoạt (thường là tác nhân chính yêu cầu). Khi tác nhân chính là thời gian, bước 1 ghi Thực hiện bởi là chủ ngữ hệ thống, Hành động "Tới <thời điểm>" (ví dụ "Hệ thống | Tới 20 giờ hằng ngày."); nhờ vậy sơ đồ không cần partition cho tác nhân thời gian (F10.2). Bước cuối cùng là phản hồi làm mục tiêu đạt được (thường hệ thống lưu, hiển thị kết quả, hoặc thông báo).
  11. Một bước kiểm tra được gộp nhiều điều kiện về cùng một đối tượng tại cùng thời điểm ("Kiểm tra thẻ bạn đọc còn hiệu lực và bạn đọc không có sách quá hạn"); mỗi điều kiện thất bại là một luồng thay thế riêng tại bước đó. Điều kiện kiểm tra ở thời điểm khác nhau hoặc trên đối tượng khác nhau thì tách bước.
  12. Use case có nhiều tác nhân chính (P02 liệt kê nhiều tác nhân ở cột Tác nhân chính): hàng Tác nhân chính liệt kê tất cả. Cột Thực hiện bởi ghi tác nhân cha nếu P01 có tổng quát hoá các tác nhân đó; nếu không, ghi tên các tác nhân nối bằng " / " và mọi khác biệt về hành vi giữa họ đặt thành luồng thay thế.
  13. Use case được include (P02 giữ theo Q4, cột Tác nhân chính ghi "-" hoặc ghi tác nhân kèm "(qua UC-xxx)"): bước 1 là "Hệ thống | Bắt đầu <mục tiêu> khi được gọi từ UC-xxx <tên>"; tiền điều kiện là trạng thái tại điểm gọi; bước cuối là "Hệ thống | Trả kết quả thành công cho use case gọi"; luồng thất bại kết thúc bằng "Trả kết quả thất bại <lý do> cho use case gọi". Activity diagram đặt nút khởi đầu trong partition hệ thống.
    - P02 ghi tác nhân chính kèm "(qua UC-xxx)": hàng Tác nhân chính chép đúng như P02; từ bước 2, các bước tác nhân đó thực hiện sau điểm gọi (chọn, nhập, xác nhận) ghi tác nhân đó ở cột Thực hiện bởi như mọi use case khác, và activity diagram có partition cho tác nhân này. Ví dụ: "Thanh toán đơn" được gọi từ "Đặt món": 1. Hệ thống | Bắt đầu thanh toán khi được gọi từ UC-004 Đặt món; 2. Khách hàng | Chọn phương thức thanh toán; 3. Khách hàng | Nhập thông tin thẻ.
    - P02 ghi "-" (không tác nhân nào tương tác trực tiếp trong phần này): hàng Tác nhân chính ghi "Không có (được gọi từ UC-xxx <tên>)".
  14. Use case mở rộng (extension, UC_ID là use case mở rộng trong quan hệ «extend» ở P03):
    - Hàng Tác nhân chính theo mục 13. Bước 1 là "Hệ thống | Bắt đầu <mục tiêu> tại điểm mở rộng '<tên điểm>' của UC-xxx <tên>"; tiền điều kiện gồm trạng thái tại điểm mở rộng, không lặp lại điều kiện mở rộng (điều kiện đó thuộc UC gốc).
    - Bước cuối của luồng chính ghi nơi UC gốc đi tiếp: "Hệ thống | Trả quyền điều khiển cho UC-xxx, tiếp tục tại bước K". Mỗi luồng thay thế kết thúc bằng một trong: "Tiếp tục UC-xxx tại bước K", "Kết thúc UC-xxx (thất bại)", "Kết thúc UC-xxx (thành công)". K là số bước luồng chính của UC gốc và có thể khác nhau giữa các luồng, ví dụ quay về bước tác nhân nhập lại thông tin khi phần mở rộng không thực hiện được với thông tin hiện có.
    - Mục 8 Thông tin bổ sung liệt kê mọi kết cục đối với UC gốc, mỗi dòng một kết cục: "<luồng> --> Tiếp tục UC-xxx tại bước K" hoặc "<luồng> --> Kết thúc UC-xxx". UC gốc dùng danh sách này để viết hàng chèn use case mở rộng (F5.2).
    - Ví dụ (khách sạn): "Yêu cầu xe đưa đón" mở rộng "Đặt phòng" tại điểm "Chọn dịch vụ kèm theo". Luồng chính kết thúc "Trả quyền điều khiển cho UC-003, tiếp tục tại bước 7"; luồng 3a "Không còn xe trống vào giờ khách chọn" kết thúc "Tiếp tục UC-003 tại bước 5" để khách chọn lại dịch vụ kèm theo.
  15. Chờ sự kiện có hạn giờ: khi trong phiên của use case hệ thống phải chờ một sự kiện từ tác nhân, thiết bị hoặc hệ thống ngoài trong một thời hạn (thường là một BR), luồng chính viết hai bước liền nhau: bước hệ thống bắt đầu chờ, nêu thời hạn bằng mã BR, rồi bước sự kiện tới do chủ thể của sự kiện thực hiện. Hết thời hạn là luồng thay thế của chính use case này (P02 U-R07), gắn vào bước bắt đầu chờ (F5.2), không tạo use case riêng, không có tác nhân thời gian. Ví dụ (ATM, Rút tiền): "6 | Hệ thống | Đẩy tiền ra khe và chờ khách hàng lấy tiền trong thời hạn (BR-04)." "7 | Khách hàng | Lấy tiền khỏi khe." Luồng "6a | Hết thời hạn (BR-04) mà khách hàng chưa lấy tiền | Hệ thống | Thu hồi tiền và ghi nhận giao dịch không thành công. | Kết thúc use case (thất bại)".
F4.3 Bước gọi use case được include: là một bước của hệ thống, gọi tường minh bằng mã và tên: "Gọi use case UC-009 Thanh toán trực tuyến để bạn đọc thanh toán phí." Kết quả thất bại của use case được include xử lý bằng luồng thay thế tại chính bước đó (ví dụ 8a). Không chép các bước của use case được include vào base.
F4.4 Mức hợp lý:
  - Số bước: khoảng 3-15 bước, dễ đọc nhất khoảng 3-9 (bảng tách bước tác nhân và bước hệ thống nên 4-12 là phổ biến). Dưới 3 bước thường là use case quá nhỏ (một thao tác CRUD, một bước của quy trình lớn hơn); ghi vào "Đề xuất sửa artifact trước" cho P02. Trên 15 bước thường là gộp nhiều mục tiêu, hoặc bước quá chi tiết; gộp bước theo phép thử bên dưới, hoặc tách luồng con, hoặc đề xuất tách use case (không tự tạo use case mới).
  - Phép thử mức bước: mỗi bước trả lời được câu "tác nhân hoặc hệ thống đạt được điều gì ở bước này?" bằng một kết quả có tên nghiệp vụ. Nếu câu trả lời là một cử động thao tác (gõ, chọn một ô) thì quá chi tiết; nếu câu trả lời chứa nhiều kết quả khác bản chất (vừa kiểm tra, vừa tính phí, vừa lưu) thì quá chung.
  - Quá chi tiết (sai): "1. Bạn đọc nhập mã thẻ. 2. Bạn đọc nhập mật khẩu. 3. Bạn đọc nhấn Đăng nhập." Đúng: "1. Bạn đọc cung cấp mã thẻ và mật khẩu."
  - Quá chung (sai): "3. Hệ thống xử lý đơn đặt món." Đúng: "3. Hệ thống kiểm tra các món còn phục vụ. 4. Hệ thống tính tổng tiền và phí giao hàng. 5. Hệ thống hiển thị tóm tắt đơn."
F4.5 Lỗi thường gặp khác:
  - Viết theo góc nhìn bên trong hệ thống ("Controller gọi service"), mất góc nhìn tác nhân.
  - Chủ ngữ mơ hồ ("Thông tin được lưu", "Người dùng" khi có nhiều vai trò).
  - Bước "Hệ thống hiển thị màn hình chính" không mang giá trị nghiệp vụ; chỉ giữ khi hiển thị thông tin tác nhân cần để ra quyết định ở bước sau.
  - Nhét luồng lỗi vào luồng chính ("Hệ thống kiểm tra mã OTP, nếu sai thì báo lỗi").
- Ví dụ đúng (hệ thống phòng khám, use case Đặt lịch tái khám):
  | 1 | Bệnh nhân | Yêu cầu đặt lịch tái khám. |
  | 2 | Hệ thống | Hiển thị các lần khám gần đây có hẹn tái khám của bệnh nhân. |
  | 3 | Bệnh nhân | Chọn lần khám cần tái khám và ngày mong muốn. |
  | 4 | Hệ thống | Hiển thị các khung giờ còn trống của bác sĩ đã khám lần đó trong ngày đã chọn. |
  | 5 | Bệnh nhân | Chọn khung giờ và gửi yêu cầu. |
  | 6 | Hệ thống | Kiểm tra ngày đã chọn còn trong thời hạn tái khám mà bác sĩ đã hẹn. |
  | 7 | Hệ thống | Tạo lịch tái khám ở trạng thái "Đã giữ chỗ". |
  | 8 | Hệ thống | Hiển thị thông tin lịch tái khám vừa tạo. |
- Ví dụ sai (hệ thống giao đồ ăn):
  | 1 | Khách hàng | Mở ứng dụng và bấm vào giỏ hàng. | (từ giao diện)
  | 2 | Hệ thống | Nếu giỏ hàng trống thì báo lỗi, ngược lại chuyển sang trang thanh toán. | (có "nếu", từ giao diện)
  | 3 | Hệ thống | Xử lý thanh toán. | (quá chung, không gọi tường minh use case thanh toán đã include)
F4.6 Luồng con (subflow): một đoạn bước được dùng lại nhiều lần trong cùng use case hoặc làm luồng chính quá dài. Đặt mã S1, S2; bước con S1.1, S1.2. Trong luồng chính gọi bằng bước "Thực hiện luồng con S1 <tên>". Luồng con không phải use case, không xuất hiện trên biểu đồ use case. Dùng hạn chế; nếu đoạn bước dùng chung giữa nhiều use case thì đó là ứng viên include, ghi vào "Đề xuất sửa artifact trước" cho P03.
F4.7 Use case cha, con (generalization): đặc tả cha ghi các bước chung, bước để trống cho con điền ghi dạng "<Bước do use case con định nghĩa: mô tả>". Đặc tả con ghi "Kế thừa UC-nnn", liệt kê bước nào ghi đè, điền chỗ trống, hoặc thêm mới, và dẫn tới số bước của cha ("Bước 4-7 như UC-004").

F5. Luồng sự kiện thay thế và ngoại lệ
Bảng: | STT | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
F5.1 Định nghĩa: mọi đường đi khác luồng chính gồm biến thể thông thường (cách khác để đạt mục tiêu), trường hợp lạ, và ngoại lệ (lỗi, không đạt mục tiêu). Mỗi luồng thay thế gắn với bước phát sinh trong luồng chính.
F5.2 Đánh số:
  - Na: luồng thay thế thứ a phát sinh tại bước N của luồng chính. N là bước mà tại đó điều kiện được phát hiện (thường là bước kiểm tra của hệ thống, hoặc bước tác nhân chọn khác đi). Các luồng tại cùng bước lấy a, b, c theo thứ tự.
  - Hết thời hạn chờ một sự kiện (F4.2 mục 15): N là bước hệ thống bắt đầu chờ, không phải bước sự kiện tới (sự kiện không tới thì bước đó không xảy ra). Điều kiện ghi "Hết <thời hạn> (BR-xx) mà <sự kiện> chưa xảy ra".
  - Luồng có một hành động: một hàng STT "Na" ghi đủ năm cột.
  - Luồng không có hành động (điều kiện chỉ dẫn tới kết thúc hoặc bỏ qua một đoạn, ví dụ "Không có đơn nào cần xử lý"): một hàng STT "Na", cột Thực hiện bởi và cột Hành động ghi "-", cột Quay lại / Kết thúc ghi đích. Không bịa hành động để lấp chỗ trống.
  - Luồng có nhiều hành động: hàng "Na" ghi Điều kiện, cột Thực hiện bởi ghi "-", cột Hành động ghi tên ngắn của luồng, cột Quay lại ghi "-"; các hàng tiếp theo "Na1", "Na2"... ghi từng hành động, cột Điều kiện để trống, hàng cuối ghi Quay lại / Kết thúc.
  - Luồng thay thế lồng trong luồng thay thế: "Na1b" là nhánh phát sinh tại hành động Na1. Hạn chế lồng quá hai mức; sâu hơn thì tách luồng con.
  - Luồng có thể xảy ra ở bất kỳ bước nào (tác nhân huỷ, hết phiên): STT "*a", Điều kiện ghi "Tại bất kỳ bước nào trước bước K, <điều kiện>".
  - Chèn use case mở rộng: một hàng tại bước chứa điểm mở rộng, Điều kiện là điều kiện mở rộng lấy từ P03, Hành động "Chèn use case UC-nnn <tên> tại điểm mở rộng '<tên điểm>'", Quay lại "Tiếp tục bước K" (kết cục thông thường).
  - Use case mở rộng có kết cục khác đối với UC gốc (quay về một bước khác, hoặc kết thúc UC gốc; lấy từ mục 8 của đặc tả UC mở rộng nếu đã có, hoặc từ nguồn): viết thành luồng nhiều hành động. Hàng "Na" ghi điều kiện mở rộng, Thực hiện bởi "-", Hành động tên ngắn, Quay lại "-"; hàng "Na1" là hàng chèn use case mở rộng như trên, Quay lại "Tiếp tục bước K"; mỗi kết cục khác là một nhánh lồng "Na1a", "Na1b"..., Điều kiện "UC-nnn kết thúc với <kết cục>", Thực hiện bởi và Hành động ghi "-", Quay lại ghi "Quay lại bước J", "Kết thúc use case (thất bại)" hoặc "Kết thúc use case (thành công)". Bước J phải khớp bước ghi trong đặc tả UC mở rộng; nếu chưa có đặc tả UC mở rộng thì ghi kết cục theo nguồn và thêm vào Thông tin bổ sung "Kết cục của UC-nnn cần khớp khi đặc tả UC-nnn".
F5.3 Cột Điều kiện: điều kiện hệ thống phát hiện được hoặc lựa chọn của tác nhân, viết dạng mệnh đề đúng/sai, không bắt đầu bằng "Nếu" để giữ cột gọn. Điều kiện của các luồng cùng bước phải loại trừ lẫn nhau và loại trừ với điều kiện đi tiếp của luồng chính.
  - Đúng: "Bạn đọc đang mượn đủ 5 cuốn"; "Cổng thanh toán trả về giao dịch bị từ chối"; "Khách hàng chọn nhận món tại quán".
  - Sai: "Có lỗi" (không rõ lỗi gì); "Dữ liệu không hợp lệ hoặc hệ thống bận hoặc hết hàng" (gộp ba điều kiện có cách xử lý khác nhau).
  - Khi hai điều kiện cùng bước có thể cùng đúng (ví dụ thẻ bạn đọc hết hạn và bạn đọc có sách quá hạn), chọn một trong hai cách: viết điều kiện sau loại trừ điều kiện trước ("2b: Thẻ còn hiệu lực và bạn đọc có sách quá hạn") theo thứ tự ưu tiên của nguồn; hoặc tách bước kiểm tra thành hai bước. Nguồn không nêu thứ tự ưu tiên thì theo thứ tự xuất hiện trong nguồn và ghi Q-nn.
F5.4 Cột Quay lại / Kết thúc: bắt buộc ở hàng cuối của mỗi luồng. Một trong: "Quay lại bước K" (K là bước luồng chính), "Tiếp tục bước K", "Kết thúc use case (thất bại)", "Kết thúc use case (thành công)" (biến thể vẫn đạt mục tiêu), "Quay lại bước do tác nhân chọn (trong khoảng bước K1 đến bước hiện tại)" (chỉ dùng cho luồng *a khi nguồn cho tác nhân trở về một bước bất kỳ đã qua), "Chờ Q-nn" (chỉ ở NGHIEM_NGAT, khi điều kiện của luồng có căn cứ trong nguồn hoặc suy ra từ BR nhưng cách xử lý tiếp theo chưa được nguồn quy định; Q-nn hỏi cách xử lý; cột Hành động ghi hành động đã biết hoặc "-"). Use case mở rộng dùng thêm các giá trị ở F4.2 mục 14. Bước K, K1 phải tồn tại. Tránh quay lại tạo vòng vô hạn; nếu nguồn có giới hạn số lần thử thì tách luồng khi vượt giới hạn (ví dụ 5a: sai lần 1-2 quay lại bước 4; 5b: sai lần thứ 3 kết thúc).
F5.5 Mức hợp lý: mỗi bước kiểm tra của hệ thống thường có ít nhất một luồng thay thế; mỗi bước tác nhân nhập liệu có luồng dữ liệu không hợp lệ khi có điều kiện hợp lệ; mỗi bước gọi hệ thống ngoài có luồng hệ thống ngoài lỗi hoặc không phản hồi khi nguồn nêu hoặc khi đã có Q-nn. Không tạo luồng cho lỗi hạ tầng chung (mất điện, mất mạng, lỗi máy chủ) trừ khi nguồn nêu; lỗi chung thuộc đặc tả bổ sung.
F5.6 Lỗi thường gặp:
  - Đánh số theo thứ tự xuất hiện (A1, A2) làm mất vị trí phát sinh. Dùng Na.
  - Thiếu điểm quay lại, người đọc không biết use case đi tiếp thế nào.
  - Luồng thay thế thực chất là một use case khác có mục tiêu riêng (ví dụ "Bạn đọc muốn đặt giữ sách thay vì mượn"); ghi vào "Đề xuất sửa artifact trước" cho P02.
  - Chép lại toàn bộ luồng chính trong luồng thay thế.
- Ví dụ đúng (hệ thống thư viện, use case Gia hạn phiếu mượn):
  | 4a | Phiếu mượn đã được gia hạn đủ số lần tối đa (BR-06) | Hệ thống | Thông báo phiếu mượn không thể gia hạn thêm. | Kết thúc use case (thất bại) |
  | 4b | Đầu sách đang có bạn đọc khác đặt giữ chỗ | - | Sách đang được đặt giữ | - |
  | 4b1 | | Hệ thống | Thông báo sách đang được đặt giữ và ngày hết hạn hiện tại. | |
  | 4b2 | | Hệ thống | Nhắc bạn đọc trả sách đúng hạn. | Kết thúc use case (thất bại) |
  | *a | Tại bất kỳ bước nào trước bước 6, bạn đọc huỷ yêu cầu | Hệ thống | Huỷ yêu cầu gia hạn, không thay đổi phiếu mượn. | Kết thúc use case (thất bại) |
- Ví dụ sai:
  | A1 | Lỗi | Hệ thống | Báo lỗi | | (số không gắn bước, điều kiện mơ hồ, thiếu điểm quay lại)
F5.7 Phản hồi mặc định khi vi phạm quy tắc nghiệp vụ: nguồn nêu điều kiện (BR) nhưng không nêu hệ thống phản hồi thế nào khi điều kiện không đạt. Ở cả hai chế độ giả định, hành động của luồng thất bại đó mặc định là "Từ chối <yêu cầu> và thông báo quy tắc bị vi phạm (BR-xx)", Quay lại / Kết thúc là "Kết thúc use case (thất bại)" hoặc quay lại bước tác nhân nhập hay chọn khi tác nhân sửa được dữ liệu vi phạm. Không tạo Q-nn cho việc thông báo; chỉ tạo Q-nn khi nguồn gợi ý một xử lý khác từ chối (chuyển người duyệt, cho phép kèm phí).

F6. Dữ liệu vào và dữ liệu ra
Chỉ lập khi use case có tác nhân cung cấp thông tin nhiều hơn một mục, hoặc hệ thống trả về danh sách hoặc bộ thông tin có cấu trúc. Không có thì ghi "Không có".
F6.1 Dữ liệu vào: mỗi nhóm dữ liệu một bảng, tiêu đề "Dữ liệu vào N (bước K)".
Bảng: | STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
  - Trường dữ liệu: tên nghiệp vụ theo nguồn, không phải tên cột, không phải tên điều khiển giao diện.
  - Bắt buộc: "Có", "Không", hoặc "Có khi <điều kiện>". Nguồn nêu có trường bắt buộc nhưng không nói trường nào thì ghi "Chưa quy định (Q-nn)" ở chế độ NGHIEM_NGAT, như cột Điều kiện hợp lệ.
  - Điều kiện hợp lệ: cụ thể, kiểm chứng được: độ dài, miền giá trị, định dạng, tính duy nhất, quan hệ với dữ liệu đã có, dẫn BR nếu điều kiện là quy tắc nghiệp vụ. Nguồn không nêu thì ghi "Chưa quy định (Q-nn)" ở chế độ NGHIEM_NGAT; không tự đặt "tối đa 255 ký tự".
  - Ví dụ: giá trị thực tế, hợp lệ, nhất quán với các trường khác và với quy tắc nghiệp vụ (ngày trả sau ngày mượn, tổng tiền bằng tổng các dòng).
  - Đúng: | 1 | Số lượng nhập | Số đơn vị mặt hàng thực nhận | Có | Số nguyên dương, không lớn hơn số lượng trên đơn đặt hàng (BR-03) | 120 |
  - Sai: | 1 | Textbox số lượng | | Có | Hợp lệ | abc | (tên điều khiển giao diện, điều kiện không kiểm chứng được, ví dụ không hợp lệ)
F6.2 Dữ liệu ra: tiêu đề "Dữ liệu ra N (bước K)".
Bảng: | STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |
  - Định dạng hiển thị: định dạng của giá trị (đơn vị tiền tệ, dấu phân cách hàng nghìn, định dạng ngày giờ, số chữ số thập phân, căn lề khi là cột số). Không mô tả bố cục màn hình.
  - Đúng: | 3 | Phí giao hàng | Phí tính theo khoảng cách | Số nguyên, phân cách hàng nghìn bằng dấu chấm, kèm "đ", căn phải | 15.000 đ |
F6.3 Lỗi thường gặp: liệt kê dữ liệu hệ thống tự sinh (mã tự tăng) như dữ liệu vào; đưa thuộc tính nội bộ không hiển thị vào dữ liệu ra; điều kiện hợp lệ mâu thuẫn với BR.

F7. Quy tắc nghiệp vụ và sổ đăng ký BR
F7.1 Định nghĩa: quy tắc nghiệp vụ là chính sách, giới hạn, công thức, điều kiện do tổ chức hoặc luật đặt ra, tồn tại độc lập với phần mềm và có thể thay đổi độc lập với luồng sự kiện. Phép thử: nếu không có phần mềm, nhân viên làm bằng tay vẫn phải tuân theo quy tắc này.
  - Là BR: "Mỗi bạn đọc mượn đồng thời tối đa 5 cuốn"; "Phí giao hàng bằng 5.000 đồng mỗi km, tối thiểu 15.000 đồng"; "Chỉ nhận phòng từ 14 giờ".
  - Không là BR: "Mã OTP gồm 6 chữ số" khi nguồn nêu như quy ước kỹ thuật (thuộc điều kiện hợp lệ của dữ liệu); "Trả kết quả trong 2 giây" (phi chức năng); "Bạn đọc có thể gia hạn" (chức năng).
F7.2 Loại: một trong Sự kiện (fact, mệnh đề luôn đúng về nghiệp vụ) / Ràng buộc (constraint, điều bắt buộc hoặc bị cấm) / Kích hoạt hành động (action enabler, khi điều kiện đúng thì phải làm gì) / Suy luận (inference, từ điều kiện suy ra một kết luận mới) / Tính toán (computation, công thức).
F7.3 Bảng trong đặc tả: | BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
  - Quy tắc: một câu nguyên tử, đầy đủ ngưỡng, đơn vị, phạm vi áp dụng; đọc riêng vẫn hiểu.
  - Bước áp dụng: số bước luồng chính, luồng thay thế, hoặc bảng dữ liệu nơi quy tắc được kiểm tra hoặc dùng; "Tiền điều kiện" khi quy tắc nằm ở tiền điều kiện (hệ thống không kiểm tra lại trong luồng theo F3).
  - Trong sổ BR: "Mới" (cấp ở lần chạy này) hoặc "Đã có" (dùng lại mã).
  - Trong luồng sự kiện và bảng dữ liệu, dẫn mã BR thay vì chép lại nội dung quy tắc: "Kiểm tra số cuốn đang mượn (BR-04)".
F7.4 Cấp mã BR qua sổ đăng ký:
  1. Đọc sổ P04-uc-specs/_BR-register.md nếu có. Nếu chưa có sổ, bắt đầu từ BR-01. Nếu P06-supplementary-spec.md đã có (chạy lại), sổ và bảng BR của P06 là danh sách hợp nhất; mã lớn nhất lấy từ cả hai.
  2. Với mỗi quy tắc tìm thấy: so nghĩa với mọi BR trong sổ. Cùng nghĩa (cùng đối tượng, cùng ngưỡng, cùng điều kiện) thì dùng lại mã cũ, thêm UC_ID vào cột "UC áp dụng" của sổ. Khác ngưỡng hoặc khác điều kiện là quy tắc khác, cấp mã mới, và nếu hai quy tắc mâu thuẫn thì tạo Q-nn.
  3. Quy tắc mới: mã = mã lớn nhất đã cấp + 1, không lấp chỗ trống, không dùng lại mã có trạng thái "Loại" hoặc "Gộp".
  4. Không sửa nội dung, không xoá, không đổi mã của BR đã có trong sổ. Thấy BR cũ sai thì ghi vào "Đề xuất sửa artifact trước" (bước P04 hoặc P06, mã BR, đề nghị).
  5. Xuất lại toàn bộ sổ theo mẫu:
     # Sổ đăng ký quy tắc nghiệp vụ - <TEN_HE_THONG>
     | BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái |
     Cấp lần đầu tại: "P04 UC-nnn". Trạng thái: "Hiệu lực" (mặc định), "Gộp vào BR-xx", "Loại" (hai trạng thái sau chỉ do P06 đặt).
F7.5 Lỗi thường gặp: để quy tắc nằm lẫn trong câu hành động mà không tách mã; cấp mã mới cho quy tắc đã có ở use case khác; đánh số BR lại từ BR-01 ở mỗi use case; ghi quy tắc do AI tự nghĩ ra.

F8. Yêu cầu đặc biệt
Bảng: | STT | Yêu cầu | Nhóm (FURPS+) | REQ |
- Định nghĩa: yêu cầu phi chức năng, ràng buộc chỉ áp dụng cho use case này (thời gian phản hồi của một bước, bảo mật của một dữ liệu, số người dùng đồng thời của chức năng này).
- Không cấp mã NFR ở bước này; bước đặc tả bổ sung sẽ cấp mã và dẫn ngược UC_ID. Chỉ ghi điều có REQ; yêu cầu áp dụng cho toàn hệ thống không ghi ở đây.
- Đúng: | 1 | Kết quả tra cứu khung giờ trống trả về trong không quá 2 giây với 150 người dùng đồng thời | Performance | REQ-21 |

F9. Thông tin bổ sung
Ghi chú giúp hiểu use case mà không thuộc mục nào ở trên (tần suất sử dụng, ghi chú về dữ liệu dùng chung với use case khác). Không có thì "Không có". Không dùng mục này để chứa yêu cầu chưa có REQ.
Mục 8a Kịch bản chính (chỉ khi DAY_DU): liệt kê 2-5 kịch bản tiêu biểu, mỗi kịch bản một dòng ghi tổ hợp luồng đi qua và kết quả, ví dụ "KB1: Luồng chính --> gia hạn thành công"; "KB2: Luồng chính + 4a --> không gia hạn được". Chỉ dùng luồng đã có ở mục 2, 3. X2 dùng danh sách này khi thiết kế kiểm thử theo use case.

F10. Activity diagram
F10.1 Định nghĩa và phạm vi: activity diagram của đúng use case này, thể hiện luồng điều khiển của luồng chính và mọi luồng thay thế, chia swimlane (activity partition) theo chủ thể thực hiện. Không vẽ chi tiết bên trong use case được include hoặc use case mở rộng.
F10.2 Ánh xạ bắt buộc giữa đặc tả và sơ đồ:
  - Mỗi bước luồng chính N --> đúng một action có ID "A-N", nhãn là cụm động từ rút gọn của hành động, nằm trong swimlane của cột "Thực hiện bởi".
  - Bước gọi use case được include --> một call behavior action ID "A-N", Loại "CallBehaviorAction", nhãn "UC-nnn <tên>".
  - Mỗi hàng hành động của luồng thay thế (Na hoặc Na1, Na2...) --> một action ID "A-Na", "A-Na1"... Hàng tiêu đề của luồng nhiều hành động không có action riêng; tên luồng dùng làm guard.
  - Luồng thay thế không có hành động (cột Hành động ghi "-") --> không có action; một cạnh mang guard của luồng đi thẳng từ decision D-N tới final node (Kết thúc) hoặc merge node M-K (Tiếp tục bước K).
  - Luồng thay thế phát sinh tại bước N --> một decision ID "D-N" đặt ngay sau A-N. Guard của nhánh luồng chính là phủ định (hoặc điều kiện đi tiếp) của các điều kiện thay thế; guard của nhánh Na là cột Điều kiện, rút gọn, trong ngoặc vuông.
  - Chèn use case mở rộng --> nhánh từ D-N với guard là điều kiện mở rộng, tới call behavior action "A-Na" nhãn "UC-nnn <tên>", rồi về merge node trước bước tiếp tục. Khi use case mở rộng có nhiều kết cục (F5.2): call behavior action là "A-Na1", ngay sau nó là decision "D-Na1" với một nhánh cho mỗi kết cục; nhánh thông thường tới M-K, nhánh "Na1a", "Na1b" tới merge node M-J hoặc final node.
  - Activity diagram của chính use case mở rộng: mỗi kết cục đối với UC gốc là một activity final node riêng (FINAL-1, FINAL-2...) kèm note "N-FINAL-n" ghi "Tiếp tục UC-xxx tại bước K" hoặc "Kết thúc UC-xxx"; không vẽ action của UC gốc.
  - "Quay lại bước K" hoặc "Tiếp tục bước K" --> cạnh tới merge node "M-K" đặt ngay trước A-K. Mọi action có từ hai luồng vào trở lên phải nhận luồng qua merge node, vì theo UML nhiều luồng vào trực tiếp một action nghĩa là action chờ tất cả (join ngầm), làm sơ đồ sai nghĩa.
  - "Kết thúc use case" --> cạnh tới một activity final node. Được dùng nhiều final node (FINAL-1, FINAL-2...) để tránh cạnh dài cắt qua sơ đồ.
  - Luồng "*a" (bất kỳ bước nào) --> không nối decision vào từng bước; thêm một note ID "N-*a" mô tả điều kiện và hành động, gắn vào partition của tác nhân. Luồng *a có điểm quay lại do tác nhân chọn chỉ thể hiện bằng note N-*a (ghi khoảng bước K1 đến bước hiện tại), không vẽ cạnh quay lại. Chỉ khi công cụ hỗ trợ và người dùng yêu cầu mới dùng interruptible activity region.
  - Chờ sự kiện có hạn giờ (F4.2 mục 15) --> decision D-N ngay sau action A-N (bước bắt đầu chờ), đặt trong partition hệ thống, với hai guard: [<sự kiện> trong <thời hạn>] đi tới action của bước sự kiện tới, và [hết <thời hạn>] đi tới nhánh Na. Khi YEU_CAU_BO_SUNG yêu cầu ký hiệu UML đầy đủ: bước sự kiện tới là một AcceptEventAction, đặt cùng một AcceptTimeEvent nhãn "Sau <thời hạn>" trong một interruptible activity region; cạnh ra từ AcceptTimeEvent là cạnh ngắt (interrupting edge) đi ra ngoài vùng tới nhánh Na; khi đó không vẽ D-N.
  - Luồng có Quay lại / Kết thúc "Chờ Q-nn" --> nhánh từ decision với guard là điều kiện của luồng, qua các action đã biết (nếu có), tới một activity final node riêng kèm note "N-<số luồng>" ghi "Chờ Q-nn".
  - Luồng lặp --> decision sau bước cuối của vòng lặp với guard [còn <đối tượng>] quay về merge node trước bước đầu vòng lặp, và guard [hết <đối tượng>] đi tiếp.
  - Use case khởi động theo thời gian (tác nhân loại Thời gian trong P01): bước 1 là action Loại "AcceptTimeEvent", nhãn là thời điểm ("Tới 20 giờ hằng ngày"), đặt trong partition của hệ thống; không tạo partition cho tác nhân thời gian.
  - Fork, join chỉ dùng khi nguồn nói rõ các hành động diễn ra đồng thời hoặc không phụ thuộc thứ tự và đều phải hoàn thành. Không tự thêm song song.
F10.3 Quy tắc ký hiệu UML:
  - Đúng một initial node (INIT), đặt trong partition của chủ thể thực hiện bước 1, ở trên cùng.
  - Action: hình chữ nhật bo góc, nhãn bắt đầu bằng động từ, tối đa khoảng 8 từ, không chép nguyên câu dài.
  - Decision: một luồng vào, từ hai luồng ra trở lên; mỗi luồng ra có guard trong ngoặc vuông; các guard loại trừ lẫn nhau và phủ hết trường hợp (được dùng [khác] cho trường hợp còn lại). Không ghi chữ trong hình thoi.
  - Merge: từ hai luồng vào trở lên, một luồng ra, không guard.
  - Fork: một luồng vào, nhiều luồng ra; join: nhiều luồng vào, một luồng ra. Không dùng hình thoi thay cho thanh fork/join và ngược lại.
  - Cạnh (control flow) có mũi tên ở đầu đích; không có cạnh hai chiều; không có action "treo" (không có luồng ra) trừ final node.
  - Mọi node đạt được từ INIT và từ mọi node đi tới được một final node.
F10.4 Swimlane (partition):
  - Một partition cho mỗi chủ thể xuất hiện trong cột "Thực hiện bởi" (luồng chính và luồng thay thế): tác nhân chính, hệ thống, tác nhân phụ. Nhiều tác nhân chính ghi chung (quy tắc F4.2 mục 12) thì dùng một partition, nhãn là tên các tác nhân nối bằng " / ". Tên partition đúng tên tác nhân trong P01 và chủ ngữ hệ thống đã chọn. Tác nhân phụ không làm chủ thể bước nào (chỉ nhận thông tin) thì không có partition; tên của nó đã nằm trong nhãn action gửi.
  - Thứ tự từ trái sang phải: tác nhân chính, hệ thống, các tác nhân phụ. Thường 2-4 partition; trên 5 partition thì kiểm tra lại use case có quá lớn không.
  - Mỗi action nằm trong đúng một partition. Decision đặt trong partition của chủ thể đánh giá điều kiện (thường là hệ thống, vì hệ thống kiểm tra kết quả do tác nhân phụ trả về), ngay dưới action phát sinh điều kiện; decision thể hiện lựa chọn của tác nhân ("Khách hàng chọn nhận món tại quán") đặt trong partition của tác nhân đó.
F10.5 Bảng mô hình trong mục 9 của đặc tả (nguồn chuẩn theo Conventions C7.1):
  Node: | ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú |
   - Loại: Partition / Initial / ActivityFinal / Action / CallBehaviorAction / AcceptTimeEvent / AcceptEventAction / InterruptibleRegion / Decision / Merge / Fork / Join / Note. AcceptEventAction và InterruptibleRegion chỉ dùng theo F10.2 mục chờ sự kiện có hạn giờ khi được yêu cầu.
   - ID: partition "P-ACT-nn" cho tác nhân (theo mã ACT) và "P-SYS" cho hệ thống; INIT; FINAL-n; A-<số bước>; D-<số bước>; M-<số bước đích>; FK-n, JN-n; N-<mã>.
   - Stereotype: để "-" (activity diagram của use case không dùng stereotype).
   - Thuộc về: ID partition.
   - Bước UC: số bước tương ứng (1, 4a, 4b1...) hoặc "-".
  Edge: | ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
   - ID: E-01, E-02... theo thứ tự đọc từ trên xuống.
   - Điểm uốn: cột tuỳ chọn theo Conventions C7.1, bắt buộc điền cho cạnh quay lại (tới merge node M-K) và cạnh vượt qua partition khác, vì định tuyến tự động của draw.io dễ cắt qua node; các cạnh khác ghi "-".
   - Loại quan hệ: ControlFlow (hoặc NoteLink cho đường nối note).
   - Nhãn: guard trong ngoặc vuông khi cạnh ra từ decision, ngược lại "-".
  Kèm bảng đối chiếu ngắn: | Bước UC | Node | để người đọc kiểm tra ánh xạ 1-1.
F10.6 File .drawio (theo Conventions C7.3):
  - Tên file diagrams/P04-activity-UC-nnn.drawio; một trang, tên trang "UC-nnn".
  - Partition là swimlane dọc đặt cạnh nhau, cùng chiều cao, cùng y=0: style "swimlane;html=1;startSize=40;". Chiều rộng mỗi partition tối thiểu 280, tăng lên khi có nhánh thay thế nằm ngang. Partition của tác nhân rộng tối thiểu 520 khi có luồng thay thế chứa hành động của tác nhân đó, để action của nhánh đặt lệch sang phải trục chính mà không nằm trên đường của cạnh khác.
  - Node là cell con của partition (parent = ID partition), toạ độ tương đối trong partition. Cạnh có parent="1", source, target là ID node.
  - Style: initial "ellipse;html=1;fillColor=#000000;" 40x40; final "ellipse;shape=endState;html=1;fillColor=#000000;" 40x40 (kích thước chẵn chục để tâm trùng trục dọc của action 180 rộng khi toạ độ là bội số của 10); action "rounded=1;whiteSpace=wrap;html=1;arcSize=40;" 180x60; call behavior action dùng style action thêm "fontStyle=1;" và nhãn "UC-nnn <tên>"; AcceptTimeEvent dùng style action, nhãn bắt đầu bằng "Tới" hoặc "Sau"; AcceptEventAction dùng style action, nhãn là tên sự kiện; InterruptibleRegion "rounded=1;dashed=1;fillColor=none;html=1;"; decision, merge "rhombus;html=1;" 40x40; fork, join "shape=line;strokeWidth=4;html=1;" 160x10; note "shape=note;whiteSpace=wrap;html=1;size=14;"; control flow "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=open;endFill=0;"; guard là value của cạnh.
  - Bố cục: luồng chính đi từ trên xuống, các action luồng chính của cùng partition thẳng một trục dọc; khoảng cách dọc giữa hai node liên tiếp 40-60; nhánh thay thế lệch ngang sang phải trục chính tối thiểu 220; nhiều luồng thay thế cùng một decision: action đầu của các nhánh xếp thành một cột bên phải, cách nhau 100 theo chiều dọc, các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action (ghi ở cột Điểm uốn), nhãn guard đặt ở đoạn cuối của cạnh (mxGeometry x="0.7") để các nhãn không chồng nhau; toạ độ là bội số của 10; không node chồng nhau; cạnh không cắt qua node. Cạnh có Điểm uốn trong bảng Edge sinh thành mxGeometry chứa <Array as="points"> với mỗi điểm một <mxPoint x=".." y=".."/> (toạ độ tuyệt đối), để sinh lại từ bảng vẫn giữ đúng đường đi.
  - Mẫu khung XML (minh hoạ cấu trúc, hệ thống thư viện):
    <mxfile><diagram id="UC-007" name="UC-007"><mxGraphModel><root>
      <mxCell id="0"/><mxCell id="1" parent="0"/>
      <mxCell id="P-ACT-01" value="Bạn đọc" style="swimlane;html=1;startSize=40;" vertex="1" parent="1"><mxGeometry x="0" y="0" width="300" height="900" as="geometry"/></mxCell>
      <mxCell id="P-SYS" value="Hệ thống" style="swimlane;html=1;startSize=40;" vertex="1" parent="1"><mxGeometry x="300" y="0" width="500" height="900" as="geometry"/></mxCell>
      <mxCell id="INIT" value="" style="ellipse;html=1;fillColor=#000000;" vertex="1" parent="P-ACT-01"><mxGeometry x="130" y="60" width="40" height="40" as="geometry"/></mxCell>
      <mxCell id="A-1" value="Yêu cầu gia hạn phiếu mượn" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;" vertex="1" parent="P-ACT-01"><mxGeometry x="60" y="130" width="180" height="60" as="geometry"/></mxCell>
      <mxCell id="E-01" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=open;endFill=0;" edge="1" parent="1" source="INIT" target="A-1"><mxGeometry relative="1" as="geometry"/></mxCell>
      ...
    </root></mxGraphModel></diagram></mxfile>
F10.7 Lỗi thường gặp của activity diagram:
  - Vẽ thành flowchart của thuật toán bên trong hệ thống (vòng lặp duyệt mảng, truy vấn CSDL) thay vì luồng của use case.
  - Số action không khớp số bước; nhãn action khác nghĩa bước.
  - Decision không có guard, guard chồng lấn ("[tuổi >= 18]" và "[tuổi > 16]"), hoặc chữ viết trong hình thoi thay cho guard.
  - Luồng quay lại nối thẳng vào action đã có luồng vào (thiếu merge node).
  - Dùng fork/join cho rẽ nhánh loại trừ; dùng decision cho song song.
  - Thiếu final node ở nhánh kết thúc thất bại; action cụt không có luồng ra.
  - Action của hệ thống đặt trong partition của tác nhân.
  - Tô màu để phân biệt luồng lỗi (màu không mang ngữ nghĩa, Conventions C7.3).

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Tên use case, tên tác nhân, quan hệ, điểm mở rộng khớp nguyên văn P01, P02, P03.
2. Mô tả ngắn 1-3 câu, nêu mục đích và giá trị, không kể bước, không có từ giao diện.
3. Tiền điều kiện là trạng thái kiểm chứng được, không phải sự kiện kích hoạt, không bị kiểm tra lại trong luồng, không nhắc thứ tự use case khác.
4. Có hậu điều kiện thành công và hậu điều kiện tối thiểu, đều là trạng thái kiểm chứng được.
5. Luồng chính: bước 1 là sự kiện kích hoạt; bước cuối làm mục tiêu đạt được; mọi bước có chủ thể rõ, bắt đầu bằng động từ, một hành động; không có "nếu"; không có từ giao diện; không có chi tiết cài đặt.
5a. Luồng chính và mọi luồng thay thế kết thúc use case có tác nhân người tham gia đều có bước hệ thống báo kết quả (thành công hoặc lý do thất bại) cho tác nhân người đó, qua màn hình hoặc kênh thông báo mà nguồn nêu; nguồn không nêu cách báo thì có Q-nn.
6. Số bước luồng chính trong khoảng 3-15; ngoài khoảng thì đã có lý do hoặc đề xuất ở "Đề xuất sửa artifact trước".
7. Mỗi quan hệ include có đúng một bước gọi tường minh trong luồng chính; mỗi quan hệ extend mà use case này là base có một hàng luồng thay thế chèn use case mở rộng tại điểm mở rộng với điều kiện và bước tiếp tục, và mọi kết cục khác của use case mở rộng có nhánh riêng (F5.2). Nếu use case này là extension hoặc được include, luồng chính nêu rõ điểm bắt đầu và nơi quay về base; use case mở rộng ghi nơi quay về ở bước cuối và ở mọi luồng thay thế (F4.2 mục 14).
8. Mọi luồng thay thế đánh số Na theo bước phát sinh, có điều kiện rõ, các điều kiện cùng bước loại trừ nhau, có Quay lại / Kết thúc trỏ tới bước tồn tại (hoặc "Chờ Q-nn" với Q-nn có trong mục Câu hỏi mở); hết thời hạn chờ gắn vào bước bắt đầu chờ.
9. Mọi bước kiểm tra của hệ thống có ít nhất một luồng thay thế, hoặc có Q-nn giải thích vì sao chưa có.
10. Mọi trường dữ liệu vào có Bắt buộc, Điều kiện hợp lệ (hoặc "Chưa quy định (Q-nn)"), Ví dụ hợp lệ và nhất quán.
11. Mọi quy tắc nghiệp vụ đã được tách thành BR, được dẫn mã trong bước áp dụng; BR trùng nghĩa với sổ dùng lại mã cũ; BR mới có mã tiếp nối mã lớn nhất; sổ BR xuất lại đầy đủ và không mất dòng cũ.
12. Không có luồng, quy tắc, trường dữ liệu, ngưỡng nào do AI tự thêm ở chế độ NGHIEM_NGAT; mọi phần tử truy vết được về REQ hoặc câu trích nguồn.
12a. Mọi số liệu suy ra từ BR (ngưỡng, mốc, ví dụ tính toán trong luồng, Vấn đề còn mở hay Câu hỏi mở) được tính lại từ công thức của BR và ghi kèm phép tính, ví dụ (bãi đỗ xe, BR-05: giờ đầu 10.000 đồng, mỗi giờ tiếp theo 5.000 đồng, trần 60.000 đồng mỗi lượt) "phí chạm trần khi 10.000 + 5.000 x (số giờ - 1) = 60.000, tức từ giờ thứ 11".
13. Activity diagram: mỗi bước luồng chính đúng một action; mỗi hàng hành động luồng thay thế đúng một action; mỗi luồng thay thế là một nhánh từ decision có guard trong ngoặc vuông; quay lại đi qua merge node; mọi nhánh kết thúc ở final node hoặc nhập lại luồng chính.
14. Partition đủ mọi chủ thể trong cột "Thực hiện bởi", đúng thứ tự, mỗi action đúng partition.
15. Bảng Node, bảng Edge và file .drawio khớp nhau về ID; XML hợp lệ, không nén, có cell 0 và 1; toạ độ bội số của 10; không node chồng nhau.
16. Mọi mục của khung C5 có mặt; mục trống ghi "Không có"; không em dash, không mũi tên Unicode.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này, ưu tiên cao hơn quy tắc mặc định (trừ Conventions C1). Không dùng thì thay cả khối bằng "Không có" | Ví dụ: "Đặc tả theo mẫu bảng một khối: mọi mục nằm trong một bảng, luồng sự kiện là bảng con"; "Không vẽ activity diagram cho use case có dưới 5 bước"; "Đánh số luồng thay thế dạng A1, A2 kèm cột Vị trí phát sinh"; "Luồng chính tối đa 10 bước"}}
````

## 5. Ghi chú cho người dùng

- Luồng chính quá dài hoặc có "nếu": yêu cầu AI chạy lại mục F4.4 (phép thử mức bước). Nếu vẫn dài, use case có thể gộp nhiều mục tiêu; quay lại P02.
- AI bịa luồng ngoại lệ phổ biến (mất mạng, hết phiên) mà nguồn không nói: kiểm tra chế độ NGHIEM_NGAT trong hồ sơ; các trường hợp này chỉ nên nằm ở câu hỏi mở.
- Mã BR bị trùng giữa hai use case: do chạy hai use case song song hoặc quên đính kèm sổ BR mới nhất. Sửa bằng cách chạy lại use case chạy sau cùng, kèm sổ BR đúng. Bước đặc tả bổ sung cũng phát hiện và báo trùng mã.
- File .drawio bố cục chưa đẹp: mở bằng draw.io, kéo lại vị trí; nếu thay đổi nội dung (thêm, bớt node) thì sửa bảng mô hình trong đặc tả trước rồi sinh lại.
- Use case được include hoặc use case mở rộng: chạy sau use case base và đính kèm đặc tả base, để bước quay về base khớp số bước.
- Dùng độc lập: bước này dùng được riêng để viết một đặc tả use case khi đã có danh sách use case từ nguồn khác. Khi đó thay P01, P02, P03 bằng một đoạn mô tả ngắn trong YEU_CAU_BO_SUNG: tên use case, tác nhân, quan hệ với use case khác.

## 6. Căn cứ

- OMG, Unified Modeling Language (UML) 2.5.1, 2017: use case, include, extend, extension point; activity, action, call behavior action, control flow, initial, activity final, decision, merge, fork, join, activity partition; ngữ nghĩa nhiều luồng vào một action.
- A. Cockburn, Writing Effective Use Cases, Addison-Wesley, 2001: mẫu fully dressed, hậu điều kiện tối thiểu và thành công, quy tắc viết bước (chủ ngữ rõ, thể hiện ý định không phải cử động, mỗi bước tiến trình tiến lên), đánh số extension theo bước (3a, *a), số bước khuyến nghị.
- K. Bittner, I. Spence, Use Case Modeling, Addison-Wesley, 2003: luồng cơ bản, luồng thay thế có vị trí, điều kiện, điểm quay lại; luồng con; tiền điều kiện, hậu điều kiện.
- C. Larman, Applying UML and Patterns, 3rd ed., Prentice Hall, 2004: use case ở mức mục tiêu người dùng, phong cách viết "essential", tách quy tắc nghiệp vụ và yêu cầu đặc biệt.
- Rational Unified Process, mẫu Use-Case Specification (brief description, flows of events, subflows, pre/postconditions, extension points, special requirements).
- K. Wiegers, J. Beatty, Software Requirements, 3rd ed., 2013: phân loại quy tắc nghiệp vụ (fact, constraint, action enabler, inference, computation), đặc tả dữ liệu.
- S. Ambler, The Elements of UML 2.0 Style, Cambridge University Press, 2005: quy tắc guard (loại trừ, đầy đủ), swimlane, đặt tên action.
