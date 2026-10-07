# Nhánh B - Ghi chép nghiên cứu (P00, P04, P05, P06)

File nội bộ, không thuộc sản phẩm. Số trang slide ghi theo số slide in trên slide (không phải số trang PDF; PDF in 4 slide mỗi trang, trang PDF = ceil(slide/4)).

## 1. Quy định trích từ slide

### 1.1 01.1-SoftwareDevelopmentProcess.pdf
- Slide 11 (trang PDF 3): quy trình phân tích yêu cầu phần mềm (theo SLCP/12207): mô tả yêu cầu gồm điều kiện môi trường, yêu cầu chức năng và giao tiếp, định nghĩa dữ liệu và CSDL, một số yêu cầu phi chức năng (reliability, usability, time efficiency), yêu cầu nghiệm thu. --> P00 cây phân loại có đủ các loại Chức năng, Giao tiếp ngoài, Dữ liệu, Phi chức năng, Ràng buộc.
- Slide 18: yếu tố thành công gồm đáp ứng chức năng, đúng hạn, chất lượng (Reliability, Usability, Performance, Maintainability). --> P06 nhóm FURPS.
- Slide 34: artifact của Requirements vào A&D: Use-Case Model, Glossary, Supplementary Specification.

### 1.2 02-RequirementModelingWithUC-new.pdf (bản chính dùng để bám)
- Slide 3-4: nội dung mô tả yêu cầu (như 1.1). Slide 6: artifact yêu cầu: Use-Case Model (actors, use cases), Glossary, Supplementary Specification, Use-Case Specifications.
- Slide 38-39: outline use case: tên, mô tả ngắn, luồng cơ bản đánh số bước, luồng thay thế; một luồng cơ bản (kịch bản thành công từ đầu tới cuối), nhiều luồng thay thế (regular variants, odd cases, exceptional flows).
- Slide 40: câu hỏi để outline: sự kiện nào bắt đầu, kết thúc thế nào, lặp thế nào; có tình huống tuỳ chọn, trường hợp lạ, biến thể, điều gì sai, điều gì không xảy ra, tài nguyên nào bị khoá. --> P04 Action bước 4.
- Slide 42-43: màn hình, chuyển màn hình không nằm trong use case (thuộc thiết kế giao diện).
- Slide 44: ví dụ bước "Software asks bank consortium...", "Bank consortium returns destination name": tác nhân phụ là chủ thể một bước khi trả thông tin. "Customer enters and submits an amount" gộp nhập và gửi. --> P04 F4.2 quy tắc 2, 4.
- Slide 64-65: đặc tả use case gồm Code, Name, Brief description, Flow of Events, Relationships, Activity diagrams, Use-case diagrams, Special requirements, Pre-conditions, Post-conditions, Other diagrams. --> bảng thông tin chung P04 F1 có hàng Quan hệ; mục 7 Yêu cầu đặc biệt; mục 9 Activity diagram.
- Slide 66: hướng dẫn: mô tả kịch bản cho mỗi UC gồm External Interface, Permanent data; kiểm tra thừa thiếu giữa đề và yêu cầu; nhất quán; khả thi. --> P00 ma trận phủ nguồn; P04 dữ liệu vào ra.
- Slide 67: mô tả ngắn: "This use case describes the interaction between ... when ... wishes to ...". --> mẫu câu P04 F2.
- Slide 68-69: luồng sự kiện: một luồng cơ bản, nhiều luồng thay thế; scenario là một thể hiện của use case.
- Slide 70-71: ví dụ ATM Login: bảng luồng chính 3 cột # | Doer | Action; bảng luồng thay thế cùng 3 cột, STT dạng 4a, 6a, 6b, hàng "at any time" không có số; hành động luồng thay thế chứa điều kiện ("... if the PIN number is not valid less than 3 times") và điểm quay lại ("goes to Step 2"). --> cột Thực hiện bởi, STT Na, luồng *a.
- Slide 72: chi tiết luồng thay thế theo RUP: Location, Condition, Actions, Resume location. --> 5 cột luồng thay thế trong hợp đồng: STT (vị trí) | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc.
- Slide 73: RUP style: luồng cơ bản đánh số và đặt tên bước; bước không tham chiếu luồng thay thế; thể hiện tác nhân chính đạt mục tiêu. Mẫu RUP: Brief Description, Basic Flow, Alternative Flows, Subflows, Key Scenarios, Preconditions, Postconditions, Extension Points, Special Requirements, Additional Information. --> P04 cấm "nếu" trong luồng chính; có Luồng con, Điểm mở rộng, Thông tin bổ sung.
- Slide 74-75: đặc tả dữ liệu vào: No | Data fields | Description | Mandatory | Valid condition | Example; dữ liệu ra: No | Data fields | Description | Display format | Example (display format gồm căn lề, định dạng tiền, định dạng ngày). Luồng chính dẫn "(see Table x)". --> P04 F6.
- Slide 76: include: gọi tường minh use case được include tại một bước (inclusion point) của luồng cơ bản; extend: chèn hành vi tại extension point nếu extending condition đúng; generalization: dùng placeholder trong use case cha.
- Slide 77: ví dụ "Software calls the use case ..." là một bước của hệ thống. --> P04 F4.3.
- Slide 78: extend trong đặc tả: base có luồng thay thế "A1. In the step 2, if customer chooses ..., insert use case ..., then resume at the step 3". --> P04 F5.2 hàng chèn extension.
- Slide 57: use case mở rộng kết thúc bằng "The base use case continues"; nêu "extends ... at extension point ...". --> P04 Target 7.
- Slide 79-80: cha, con: cha định nghĩa bước chung, bước mặc định, placeholder rỗng; con ghi đè, điền placeholder, thêm bước; con dẫn "Step 4->7 of the parent". --> P04 F4.7.
- Slide 81 (và bản cũ slide 47-48): luồng con (subflow) cho hành vi lặp. --> P04 F4.6.
- Slide 82-83: không đưa giao diện vào use case. Từ tránh: Click, Open, Button, Pop-up, Record, Drag, Close, Field, Scroll, Window, Form, Drop, Drop-down, Browse. Từ dùng: Prompts, Initiates, Submits, Starts, Informs, Chooses, Specifies, Selects, Displays. Activity diagram giúp tìm luồng thay thế; nhược điểm là khó đồng bộ với đặc tả. --> P04 F4.2 quy tắc 6; ánh xạ 1-1 để giảm lệch.
- Slide 84-85: activity diagram trong use-case model mô tả hoạt động của một use case; ký hiệu: initial, action, decision, guard condition trong ngoặc vuông, fork, join (synchronization bar), transition, final.
- Slide 86-87: partition (swimlane) theo trách nhiệm; ví dụ Astah có swimlane Customer, Sale, Stockroom. --> P04 F10.4.
- Slide 88: tiền điều kiện: trạng thái hệ thống trước khi bắt đầu; câu đơn giản, điều kiện phải đúng; không nhắc use case khác phải chạy trước; rõ ràng, dễ kiểm chứng; tuỳ chọn, chỉ dùng khi cần. Ví dụ có "Student has logged into the system" (trạng thái đã đăng nhập được chấp nhận). --> P04 F3.
- Slide 89: hậu điều kiện: trạng thái cuối; dùng khi trạng thái là tiền điều kiện của use case khác hoặc kết quả không hiển nhiên; không nhắc use case sau; ví dụ nêu cả trường hợp thành công và thất bại không thay đổi gì. --> P04 tách Hậu điều kiện thành công và tối thiểu (khớp ví dụ slide).
- Slide 90: use case không tương tác nhau; hậu điều kiện của use case này có thể là tiền điều kiện của use case khác.
- Slide 91: Special requirements (NFR, dữ liệu, quy tắc nghiệp vụ gắn với use case); Extension points; Additional information. --> P04 mục 7, 8, hàng Điểm mở rộng.
- Slide 93-95: Glossary: định nghĩa thuật ngữ quan trọng cho mọi mô hình; chỉ một glossary cho hệ thống; giúp giao tiếp chuyên gia miền và developer; gồm Introduction và Terms; định nghĩa đủ chi tiết để đặc trưng đầy đủ và không mơ hồ; có thể dùng như từ điển dữ liệu không chính thức. --> P05 cấu trúc Giới thiệu + Thuật ngữ, cột Ghi chú kiêm từ điển dữ liệu.
- Slide 98-100: Supplementary Specification: NFR và yêu cầu chức năng không nằm trong use case; không gắn một use case cụ thể: Functionality (chức năng chung nhiều use case), Usability (dễ dùng, đào tạo), Reliability (định lượng như MTBF, lỗi trên nghìn dòng mã), Performance (thời gian phản hồi cụ thể, dẫn use case liên quan theo tên), Supportability. --> P06 mục 2 chức năng dùng chung; cột Áp dụng cho.
- Slide 104-106 checkpoints: use case spec (ai thực hiện rõ, mục đích rõ, mô tả ngắn đúng, rõ bắt đầu kết thúc, rõ tương tác và thông tin trao đổi, có use case quá phức tạp không); glossary (mỗi thuật ngữ định nghĩa rõ, ngắn gọn; mỗi thuật ngữ xuất hiện trong mô tả use case; dùng nhất quán trong mô tả tác nhân và use case). --> Target của P04, P05.

### 1.3 02-RequirementModelingWithUC.pdf (bản cũ)
Nội dung trùng bản mới; khác biệt: bản cũ có slide 47-48 về subflow cho hành vi lặp ("Simple, repetitive behavior can be captured within the basic flow"; "Repetitive flow of events can be captured using a subflow"); không có slide dữ liệu vào ra (74-75 bản mới). Sản phẩm theo bản mới và lấy thêm quy tắc lặp của bản cũ (P04 F4.2 quy tắc 9, F4.6).

## 2. Tài liệu ngoài và quy tắc lấy từ đâu

| Quy tắc trong sản phẩm | Nguồn |
|---|---|
| 8 đặc tính REQ (P00 F5): necessary, unambiguous, complete, singular, feasible, verifiable, correct, conforming | ISO/IEC/IEEE 29148:2018 mục 5.2.5 (chuẩn có 9 đặc tính, thêm "appropriate"; nhiệm vụ yêu cầu 8, "appropriate" gộp vào "cần thiết" và "đúng mức trừu tượng", xem mục 3) |
| Từ cần cảnh giác (P00 F6) | ISO/IEC/IEEE 29148:2018 mục 5.2.7 (superlatives, subjective language, vague pronouns, ambiguous adverbs/adjectives, open-ended terms, comparative phrases, loopholes, totality, incomplete references); INCOSE Guide for Writing Requirements |
| Tách REQ nguyên tử, tách BR và NFR khỏi câu chức năng | Wiegers & Beatty ch. 11 (writing requirements), ch. 9 (business rules); 29148 "singular" |
| Bên liên quan khác tác nhân | Wiegers & Beatty ch. 2; Cockburn (stakeholders and interests) |
| Mẫu đặc tả, hậu điều kiện tối thiểu và thành công, trigger | Cockburn, Writing Effective Use Cases, ch. 5-7, mẫu fully dressed |
| Quy tắc viết bước: chủ ngữ rõ, ý định không phải cử động, mỗi bước tiến lên, "validate" thay vì "check whether" | Cockburn ch. 7 (Action steps, 14 guidelines) |
| Đánh số extension theo bước (3a, *a), điều kiện là điều hệ thống phát hiện được | Cockburn ch. 7 (Extensions) |
| Số bước luồng chính 3-9 | Cockburn: "keep the main success scenario 3-9 steps". Sản phẩm dùng 4-12 thông thường, trần 15 (xem mục 3) |
| Luồng thay thế có vị trí, điều kiện, hành động, điểm quay lại; luồng con | Bittner & Spence, Use Case Modeling ch. 5-6; RUP (khớp slide 72-73) |
| Essential style, không UI | Larman ch. 6; Constantine & Lockwood (essential use cases) |
| Phân loại BR 5 loại | Wiegers & Beatty ch. 9 (fact, constraint, action enabler, inference, computation) |
| Glossary, data dictionary | Wiegers & Beatty ch. 13; Larman ch. 7; RUP Glossary |
| Định nghĩa bằng genus + differentia, tránh vòng tròn | ISO 704:2022 |
| Một khái niệm một tên | Evans, DDD (ubiquitous language) |
| FURPS, FURPS+ | Grady 1992; Larman ch. 7 (FURPS+ và Supplementary Specification: + gồm implementation, interface, operations, packaging, legal) |
| Đặc tính chất lượng | ISO/IEC 25010:2011 (8 đặc tính) và 25010:2023 (9 đặc tính: thêm Safety; Usability --> Interaction capability; Portability --> Flexibility) |
| NFR đo được: Scale, Meter, Must | Gilb, Competitive Engineering (Planguage); Wiegers & Beatty ch. 14 |
| Activity: decision 1 vào nhiều ra, guard loại trừ và đầy đủ, [else]; merge; fork/join; call behavior action; partition; accept time event | UML 2.5.1 ch. 15-16 |
| Nhiều luồng vào một action = join ngầm, phải dùng merge | UML 2.5.1 mục 16.2.3.4 (action bắt đầu khi mọi input control flow có token) |
| Guard không chồng lấn, phủ hết; swimlane sắp logic, ít hơn 5 | Ambler, The Elements of UML 2.0 Style, ch. 9 (activity diagrams) |

## 3. Chênh lệch giữa slide và tài liệu ngoài, lựa chọn đã áp dụng

1. Đánh số luồng thay thế: slide 71 đánh 6a cho lỗi PIN tại bước 6 ("displays the main menu if the PIN is valid"), tức bước 6 chứa điều kiện; slide 73 lại yêu cầu bước không tham chiếu luồng thay thế. Cockburn đánh số theo bước phát hiện điều kiện (bước kiểm tra). Chọn: cấm "nếu" trong luồng chính (theo slide 73), đánh số Na theo bước phát hiện (thường là bước kiểm tra). Vẫn dùng dạng "Na" như slide 71.
2. Slide 71 để hàng "at any time" không có số; Cockburn dùng *a. Chọn "*a" để máy đọc được, điều kiện ghi "Tại bất kỳ bước nào trước bước K".
3. Slide 72 (RUP) đặt tên luồng thay thế và mô tả bằng văn xuôi; slide 71 dùng bảng. Hợp đồng chọn bảng 5 cột (khớp 4 thành phần Location/Condition/Actions/Resume của slide 72 + cột Doer của slide 71). Luồng nhiều hành động dùng hàng tiêu đề Na chứa tên luồng (khớp "Have names" của slide 73).
4. Slide 88-89 nói tiền/hậu điều kiện là tuỳ chọn. Hợp đồng yêu cầu có hàng. Chọn: hàng luôn có, ghi "Không có" khi không có thật; không bịa. Hậu điều kiện tách thành công và tối thiểu (Cockburn), khớp ví dụ slide 89 nêu cả hai kết cục.
5. Số bước: slide không có ngưỡng. Cockburn 3-9. Người dùng từng dùng tối đa 14-15. Chọn 4-12 thông thường, cảnh báo dưới 3 và trên 15 (Target chấp nhận 3-15), vì đặc tả kiểu bảng Doer/Action tách bước tác nhân và bước hệ thống nên dài hơn văn xuôi Cockburn khoảng 1,5 lần.
6. Slide 75 có "Display format" gồm căn lề: là chi tiết trình bày, hơi lệch quy tắc "không UI" của slide 82. Chọn: giữ cột (bám slide) nhưng giới hạn ở định dạng giá trị, căn lề cột số; cấm mô tả bố cục màn hình.
7. 29148 có 9 đặc tính (thêm appropriate); đề bài của team lead liệt kê 8. Sản phẩm dùng 8 như yêu cầu; "appropriate" (mức trừu tượng phù hợp) đã được phủ bởi quy tắc không viết giải pháp trong F2 và Conventions C1.5.
8. Slide activity diagram (slide 85) không dùng merge node và không có partition; slide 86-87 có partition. Chọn: bắt buộc partition, bắt buộc merge node khi nhiều luồng vào (UML 2.5.1). Mẫu activity diagram người dùng từng vẽ dùng merge đúng cách và partition dọc; sản phẩm giữ bố cục partition dọc. Mẫu cũ tô màu khác cho call behavior action; sản phẩm không dùng màu mang nghĩa (Conventions C7), thay bằng in đậm và nhãn mã UC.
9. Slide dùng "Glossary" gồm Introduction + Terms dạng văn xuôi đánh số. Hợp đồng dùng bảng. Chọn bảng, thêm mục Giới thiệu để khớp slide.

## 4. Quản lý mã BR (quyết định thiết kế)

Vấn đề: P04 chạy lặp cho từng use case, có thể ở nhiều cuộc chat khác nhau; nếu mỗi lần tự đánh BR-01 thì trùng mã.

Giải pháp đã áp dụng:
- Sổ đăng ký BR: file P04-uc-specs/_BR-register.md, cột | BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái |.
- P04: đọc sổ; quy tắc cùng nghĩa dùng lại mã và thêm UC vào cột UC áp dụng; quy tắc mới lấy mã lớn nhất + 1; xuất lại toàn bộ sổ. Chạy P04 tuần tự. Đặc tả P04 chỉ chứa bảng BR của use case đó với cột "Trong sổ BR" (Mới / Đã có) và dẫn mã trong bước.
- P06: danh sách BR chính thức. Hợp nhất sổ + bảng BR của mọi đặc tả P04 + REQ loại Quy tắc nghiệp vụ chưa có BR (cấp mã mới, UC lấy từ ma trận REQ --> UC của P02, chỉ "Chưa gắn UC" khi P02 cũng không gắn). Xử lý trùng mã (giữ mã cho quy tắc cấp trước, cấp mã mới cho quy tắc sau, đề xuất sửa P04), trùng nghĩa (mã lớn "Gộp vào BR-xx"), mâu thuẫn (Q-nn). Đồng bộ lại sổ.
- Mã không bao giờ đổi hay xoá (Conventions C3).
Lý do không để P06 cấp toàn bộ mã: P04 cần dẫn mã BR ngay trong bước luồng sự kiện và bảng dữ liệu; P07 đọc đặc tả P04, nên mã phải có từ P04.

## 5. Thử chạy P04 trong đầu (thư viện, UC Mượn sách)

Giả lập nguồn: thủ thư lập phiếu mượn cho bạn đọc; mỗi bạn đọc mượn tối đa 5 cuốn; bạn đọc có sách quá hạn không được mượn; hạn trả 14 ngày; hệ thống gửi email xác nhận.
Kết quả thử: luồng chính 8 bước (thủ thư cung cấp mã thẻ; hệ thống kiểm tra thẻ và sách quá hạn; hiển thị thông tin bạn đọc; thủ thư cung cấp mã sách; hệ thống kiểm tra giới hạn và tình trạng sách; tạo phiếu mượn; gửi email; hiển thị phiếu). Luồng thay thế 2a, 2b, 5a, 5b; BR-01 (tối đa 5 cuốn), BR-02 (không mượn khi có sách quá hạn), BR-03 (hạn 14 ngày); sơ đồ 2 partition, D-2, D-5, M-4.
Chỗ mơ hồ phát hiện và đã sửa:
1. Hai điều kiện cùng bước có thể cùng đúng (thẻ hết hạn và có sách quá hạn) làm guard chồng lấn. Đã thêm quy tắc ở F5.3: điều kiện sau loại trừ điều kiện trước theo thứ tự ưu tiên, hoặc tách bước.
2. Không rõ một bước kiểm tra được gộp nhiều điều kiện hay không. Đã thêm F4.2 quy tắc 2b.
3. Tác nhân phụ chỉ nhận email không làm chủ thể bước nào: không rõ có swimlane không. Đã thêm quy tắc ở F4.2 quy tắc 2 và F10.4 (không có partition).
4. Use case kích hoạt theo thời gian: không rõ bước 1 và INIT đặt ở đâu. Đã thêm AcceptTimeEvent ở F10.2, F10.5, F10.6.
Chỗ còn để AI tự quyết: nhãn action rút gọn (tối đa khoảng 8 từ) có thể lệch nghĩa nhẹ so với bước; đã có bảng đối chiếu Bước UC --> Node để người đọc kiểm tra.

## 6. Đề xuất đổi hợp đồng

1. Thêm file P04-uc-specs/_BR-register.md vào Conventions C4 (sổ đăng ký BR, P04 ghi, P06 đồng bộ). Cần người tích hợp thêm vào cây thư mục C4 và README.
2. P04 bảng thông tin: thêm các hàng ngoài hợp đồng: Tác nhân chính / Tác nhân phụ (tách), Sự kiện kích hoạt, Hậu điều kiện (thành công) và Hậu điều kiện tối thiểu (thay cho một hàng Hậu điều kiện), Quan hệ, Điểm mở rộng, REQ. Bước P07 nếu đọc "Hậu điều kiện" thì đọc hàng "Hậu điều kiện (thành công)".
3. P04 dữ liệu ra dùng cột khác dữ liệu vào theo slide: | STT | Trường dữ liệu | Mô tả | Định dạng hiển thị | Ví dụ |. Dữ liệu vào giữ đúng cột hợp đồng.
4. P04 bảng BR trong đặc tả: | BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |.
5. P04 thêm mục Luồng con (mã S1, bước S1.1) và mục Yêu cầu đặc biệt (không cấp mã NFR; P06 cấp). Bước P07 cần biết bước "Thực hiện luồng con S1" trỏ tới mục 4.
6. Bảng Node activity diagram thêm cột "Bước UC"; quy ước ID node A-<bước>, D-<bước>, M-<bước đích>, P-ACT-nn, P-SYS. P07 có thể dùng cột Bước UC để nối sequence với activity.
7. Conventions C7.3 chưa có style cho control flow của activity diagram; P04 dùng "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=open;endFill=0;". Đề nghị thêm vào bảng style C7.3. Style partition dọc P04 dùng "swimlane;html=1;startSize=40;" (một biến thể của dòng Swimlane trong C7.3).
8. P05 thêm cột Ghi chú (thành phần dữ liệu, trạng thái, BR liên quan) và bảng "Ứng viên không đưa vào".
9. P06: NFR, ràng buộc thiết kế, giao tiếp ngoài, chức năng dùng chung dùng chung dãy mã NFR-nn (Nhóm phân biệt). Bảng BR thêm cột Trạng thái, Ghi chú. P11b (giao tiếp hệ thống) nên đọc mục 5 của P06.
10. P00 bảng bên liên quan không có mã (chưa có mã trong C3). Nếu bước sau cần trỏ tới bên liên quan thì thêm mã SH-nn vào C3.

## 7. Điểm còn băn khoăn

- Chạy P04 song song (nhiều agent) vẫn có thể trùng mã BR; hiện chỉ giải quyết bằng hướng dẫn chạy tuần tự và bước hợp nhất ở P06. Phương án mạnh hơn: tiền tố theo UC (BR-005-01) nhưng lệch C3.
- Ranh giới BR và NFR cho chính sách bảo mật (khoá tài khoản sau N lần sai) vẫn là quyết định theo cách nguồn trình bày; đã hướng dẫn chọn một nơi và ghi lý do.
- Ngưỡng số bước và số thuật ngữ là heuristic (có lý do ở mục 3), không phải chuẩn.
