# Nhánh A - Ghi chép nghiên cứu: tác nhân, use case, sơ đồ use case (P01, P02, P02R, P03)

File nội bộ, không thuộc sản phẩm. Ghi nguồn của từng quy tắc trong P01, P02, P02R, P03; chênh lệch giữa slide và tài liệu ngoài; kết quả chạy thử; đề xuất đổi hợp đồng.

Ký hiệu vị trí: "new sN / pM" là slide số N, trang PDF M của 02-RequirementModelingWithUC-new.pdf (4 slide mỗi trang); "old sN / pM" tương tự cho 02-RequirementModelingWithUC.pdf. Đã xem cả hình (Read theo trang), không chỉ text.

## 1. Quy định từ slide

### 1.1. Tác nhân
- new s10 / p3, old s10 / p3: "An actor represents anything that interacts with the software."
- new s11 / p3, old s11 / p3: actor là vai trò (roles a user of the system can play); có thể là người, máy, hệ thống khác; có thể là thiết bị ngoại vi "or even database"; có thể chủ động trao đổi, là bên cho thông tin, hoặc bên nhận thông tin thụ động; "Actors are not part of the system. Actors are EXTERNAL."
- new s12 / p3 (chỉ bản new): "Actors and the system boundary": xác định ranh giới trước; mọi thứ bên ngoài ranh giới tương tác với hệ thống là thể hiện của một actor. Hình: Call Center System, câu hỏi "Is the Auto Caller System an actor or part of the system?". --> P01 Bước 1 (quyết định Trong / Ngoài trước khi tìm tác nhân).
- new s13 / p4, old s12 / p3: một người đóng nhiều vai (một người vừa là giảng viên vừa là người học; hai người cùng đóng một vai). --> A-T3 "là vai trò".
- new s14 / p4, old s13 / p4: lọc danh từ trong đề, lấy chủ thể hành động làm actor; kiểm tra không thừa không thiếu giữa đề và danh sách actor; tên actor thể hiện vai trò và trách nhiệm. --> P01 Bước 2.1, Bước 7.3, quy tắc tên.
- new s15 / p4, old s14 / p4: sáu câu hỏi tìm actor. --> P01 Bước 2.2 (giữ nguyên sáu câu).
- new s102 / p26: Checkpoints actor: đã đủ actor chưa; mỗi actor tham gia ít nhất một UC; mỗi actor có thật là một vai trò, cần gộp hay tách; hai actor có đóng cùng vai với một UC không; tên trực quan, người dùng và khách hàng hiểu được. --> A-T4, A-T5, P01 Bước 4, Target 3-6.

### 1.2. Use case
- new s10 / p3: UC mô tả chuỗi sự kiện do phần mềm thực hiện, tạo "observable result of value to a particular actor". --> định nghĩa trong P02 phần A, U-T5.
- new s20 / p5, old s17 / p5: tập các thể hiện; mô hình hoá đối thoại giữa một hoặc nhiều actor và hệ thống; mô tả hành động hệ thống làm để đem lại giá trị cho actor.
- new s21 / p5, old s18 / p5: lọc động từ, lấy chuỗi hành động thành UC; kiểm tra thừa thiếu; kiểm tra nhất quán UC với actor; khảo sát xem khách hàng, đại diện nghiệp vụ, phân tích viên, lập trình viên có hiểu tên và mô tả không. --> P02 Bước 3 (phân tích động từ), Bước 10, U-N6.
- new s22 / p5, old s19 / p5: tên UC duy nhất, trực quan, tự giải thích; nêu rõ kết quả có giá trị; theo góc nhìn actor khởi xướng; mô tả hành vi UC hỗ trợ; bắt đầu bằng động từ, dạng động từ + danh từ đơn giản. --> U-N1, U-N2, U-N3, U-N6.
- new s23 / p6, old s20 / p5: năm câu hỏi tìm UC (mục tiêu actor; vì sao dùng; tạo, lưu, đổi, xoá, đọc dữ liệu và vì sao; báo hệ thống về sự kiện ngoài; được báo về sự kiện trong hệ thống). --> P02 Bước 1.1 a-d.
- new s25 / p6: "Each communicates-association is a whole dialog" (hình: các bước 1-8 của một UC chuyển khoản, actor khách hàng và actor liên minh ngân hàng cùng tham gia, mũi tên từ khách hàng tới UC và từ UC tới actor phụ). --> P03 Bước 2.1 (association là cả cuộc đối thoại), tính chất Chính / Phụ.
- new s26 / p6: "What is NOT a use case: Functional decomposition, System design specifications, User interface specifications". --> U-AP02, U-AP03, U-AP06.
- new s27 / p7: phân rã chức năng là chia bài toán thành phần nhỏ rời rạc, không có nghĩa khi đứng riêng; UC giữ chức năng cùng nhau để mô tả một lần dùng trọn vẹn, cung cấp ngữ cảnh.
- new s28 / p7: hình ví dụ sai: một actor khách hàng nối tới Insert Card, Enter PIN, Select Transfer Funds, Enter Amount, Select From/To Account... --> ví dụ U-AP06 (miền bãi đỗ xe thay cho ATM gốc để tránh trùng ví dụ).
- new s29 / p7: triệu chứng phân rã chức năng: UC rất nhỏ, quá nhiều UC, UC không có kết quả giá trị, tên thao tác mức thấp ("Operation" + "object", "Function" + "data", ví dụ "Insert Card"), khó hiểu mô hình tổng thể. Hành động sửa: tìm ngữ cảnh lớn hơn ("Why are you building this system?"), đặt mình vào vai người dùng ("What does the user want to achieve?", "Whose goal does this use case satisfy?", "What value does this use case add?", "What is the story behind this use case?"). --> U-AP06 (dấu hiệu và cách sửa).
- new s30 / p7: "CRUD Use Cases": loại các UC CRUD nếu chúng là UC quản trị dữ liệu không đem lại kết quả có giá trị. Hình: bốn UC Create/View/Update/Delete a course bị gạch chéo, thay bằng một UC "CRUD courses"; "Do not confuse use cases with functions. Focus on value." --> U-R04 (mặc định gộp), U-AP07.
- new s31 / p8: checkpoint sơ đồ: mô tả ngắn phản ánh đúng UC; không có UC hành vi rất giống nhau; không có hành vi thừa, mọi UC truy vết về yêu cầu chức năng; "All CRUD use cases have been removed". --> U-T10, U-T11, U-AP07, U-AP12, U-AP13.
- new s40 / p10: "Use-Case Size: Too Small? Too Big? Is it more than one use case?" --> U-T4, U-AP01, U-AP04.
- new s42 / p10: ví dụ UC "View cart" (xem có giá trị, luồng 3 bước). --> U-R05 (xem là UC khi là mục tiêu thông tin).
- new s43 / p10: "Use case: Only extend/include": tách khi UC quá lớn (để chia việc, dễ quản lý) hoặc khi một phần luồng lặp lại ở nhiều UC (để dùng lại, dễ bảo trì); luồng chuyển màn hình không thể hiện trên sơ đồ use case, thuộc thiết kế giao diện. --> P02 Q4 a, c; P03 Bước 3; D-AP19.
- new s103 / p26: checkpoint UC: mỗi UC có ít nhất một actor; mỗi UC độc lập với UC khác; không có UC hành vi giống nhau; tên duy nhất, trực quan; khách hàng và người dùng hiểu tên và mô tả. --> U-T8, U-T11, U-N6.
- new s104 / p26: checkpoint mô hình: dễ hiểu, hình dung được chức năng và quan hệ; mọi yêu cầu chức năng được đáp ứng; không có hành vi thừa; chia package hợp lý. --> ma trận truy vết, nhóm chức năng.
- new s105 / p26: UC có quá phức tạp không. --> U-T4 phía trên, U-AP04.
- new s66-67 / p16: ví dụ UC "Log in" của ATM với mô tả ngắn; new s7 (text p2): sơ đồ tổng quát có UC "Login" nối actor. --> U-R01 (Đăng nhập là UC).

### 1.3. Quan hệ
- old s22 / p6: quan hệ "không nên dùng nhiều"; ba nhóm: giữa actor (generalization, association), giữa actor và UC (association), giữa UC (generalization, include, extend).
- old s23 / p6: generalization actor: con kế thừa đặc điểm và hành vi của cha; hình Commercial Customer --> Customer, tam giác ở cha.
- old s24 / p6: "Association" giữa actor: hình dưới (Student --> Registrar --> Register for Courses) bị gạch chéo đỏ; hình trên (Student --> Register for Courses) đúng. --> D-AP06: không nối actor với actor.
- new s36-37 / p9, old s25-26 / p7: association thể hiện actor và UC giao tiếp, mỗi bên gửi và nhận thông điệp; "The arrow head is optional but it's commonly used to denote the initiator"; mũi tên chỉ ai khởi xướng; không mũi tên nghĩa là hai bên đều có thể khởi xướng. Hình: Actor 1 --> Use Case --> Actor 2, Actor 3.
- old s27 / p7: "Arrowhead Conventions": Supervisor --> Monitor for alarms --> các cảm biến (mũi tên từ UC tới actor phụ).
- new s32 / p8, old s28 / p7: include "always use", extend "sometimes use"; hình: Place rush order «extend» Place order (mũi tên tới Place order), Place order «include» Pay order, Validate user là cha của hai UC con.
- new s46-47 / p11: include là quan hệ từ UC gốc tới UC được include; hành vi được đưa tường minh vào UC gốc; thực hiện trọn khi tới điểm include.
- new s48 / p12: hình: phần C chung của A và B được tách ra thành UC C.
- new s49 / p12: UC gốc gọi tường minh hành vi UC khác tại vị trí xác định trong UC gốc; UC được include không bao giờ đứng một mình. Hình: Customer nối Place order (đúng), Customer nối Pay order bị gạch chéo đỏ. --> P03 Bước 2.2, D-AP11.
- new s50 / p12: hình: actor nối UC gốc và UC khác, cả hai include UC dùng chung; UC dùng chung không nối actor; đặc tả UC gốc có bước "Call ... use case". --> P03 Bước 2.2.
- new s51 / p12: lý do dùng include: tách hành vi chung của hai UC trở lên (tránh mô tả lặp, giữ nhất quán); tách và đóng gói hành vi khỏi UC gốc (đơn giản hoá luồng, tách hành vi không thuộc mục đích chính). --> P03 Bước 3a, P02 Q4 a, c.
- new s52-53 / p13: extend nối từ UC mở rộng tới UC gốc; chèn hành vi chỉ khi điều kiện đúng, tại điểm mở rộng có tên; thực hiện khi tới điểm mở rộng và điều kiện đúng. Hình: Extension --> Base, nét đứt «extend».
- new s54 / p13, old s31 / p8: UC gốc ngầm đưa hành vi UC khác vào tại vị trí do UC mở rộng chỉ định; UC gốc có thể đứng một mình. --> P03 Bước 4b.
- new s55-56 / p13-14: ví dụ UC xem giá chứng khoán được mở rộng bởi hai UC tuỳ chọn tại điểm mở rộng "Optional Services"; hai UC mở rộng không nối actor khách hàng; UC mở rộng có actor phụ riêng (News System) trong đặc tả. --> P03 Bước 2.2a.
- new s57 / p14: lý do dùng extend: tách hành vi tuỳ chọn hoặc ngoại lệ, chỉ chạy khi có điều kiện, đơn giản hoá luồng UC gốc (ví dụ kích hoạt báo động); thêm hành vi mở rộng, phát triển riêng, có thể ở phiên bản sau. --> P02 Q4b, P03 Bước 4a.
- new s58 / p14: UC trừu tượng (được include, UC mở rộng) không cần hoàn chỉnh, chỉ tồn tại cho UC khác, không được thực hiện một mình; UC cụ thể phải hoàn chỉnh; gợi ý: che mọi UC trừu tượng mà vẫn hiểu mục đích chính của hệ thống. --> P03 Bước 6 (phép thử che), D-AP17.
- new s59 / p14, old s29 / p8: generalization UC: con kế thừa hành vi và nghĩa của cha, có thể thêm hoặc ghi đè, thay được cha ở mọi chỗ. Hình: Log in là cha của Log in by account, Log in by retinal scan; actor User nối Log in, actor Desktop App User nối UC con. --> P03 Bước 5.1.
- new s60 / p15: vì sao không nên cấu trúc quá mức: giải pháp khó thấy khi UC bị phân mảnh; phân rã chức năng làm giảm dễ hiểu, tăng phức tạp, tăng công review, kiểm thử; mô hình trông như thiết kế. --> D-AP01, D-AP17.
- new s61 / p15, old s32 / p8: sơ đồ UC là hợp đồng giữa khách hàng và đội phát triển, dùng trong mọi pha.
- new s62 / p15, old s33 / p9: không nên dùng quá nhiều quan hệ giữa UC (rối, khó nhìn); chỉ dùng khi cần; sơ đồ UC không thể hiện trình tự các UC. --> D-AP17, D-AP19, U-R13.
- new s90 (text p23): "Use cases do not interact with each other. However, a postcondition for one use case can be the same as the precondition for another." --> U-R13 (trình tự qua tiền, hậu điều kiện).
- new s82-83 (text p21): tránh từ giao diện: click, open, button, pop-up, record, drag, form, close, drop, field, drop-down, scroll, browse, window. --> U-N5, U-AP02.

## 2. Tài liệu ngoài đã dùng

| Nguồn | Quy tắc lấy về | Dùng ở |
|---|---|---|
| OMG UML 2.5.1, chương 18 | UseCase tạo observable result of value cho actor hoặc stakeholder; subject là ranh giới; Actor chỉ có association nhị phân tới UseCase, Class, Component (không tới actor khác); Include: từ including tới addition, hành vi addition được chèn, không có chu trình; Extend: từ extension tới extendedCase, có condition (tuỳ chọn) và danh sách extensionLocation; ExtensionPoint hiển thị trong ngăn "extension points" của elip; condition hiển thị bằng note gắn vào đường extend "Condition: {...} extension point: ..."; generalization cho UC và actor; UC trừu tượng tên in nghiêng | P03 phần A, E; P01 Bước 1 |
| Cockburn, Writing Effective Use Cases | Goal levels: summary (cloud, kite), user-goal (sea level), subfunction (fish, clam); actor-goal list; primary actor, supporting actor, offstage actor; stakeholders and interests; luồng chính khoảng 3-9 bước; phép thử nghỉ giải lao (coffee break); một người một lần ngồi (khoảng 2-20 phút); hạn chế include, extend | P01 tính chất; P02 mức mục tiêu, U-T1, U-T4, Bước 1 |
| Larman, Applying UML and Patterns 3e | EBP (one person, one place, one time, business event, measurable value, consistent state); Boss test, EBP test, Size test; Log In không qua Boss test; tìm UC: chọn ranh giới, tìm actor chính, mục tiêu, định nghĩa UC; phân tích sự kiện; CRUD gộp thành Manage X; primary / supporting / offstage | U-T2, U-T3, U-T4, U-T7, U-R04, P02 Bước 2 |
| Jacobson, Spence, Bittner, Use-Case 2.0 | UC là mọi cách dùng hệ thống để đạt một mục tiêu của một người dùng; mô hình UC gọn, nhìn bức tranh tổng thể | Định nghĩa UC, gom biến thể (U-R12) |
| Bittner, Spence, Use Case Modeling | Tránh phân rã chức năng bằng include; CRUD; số lượng UC hợp lý, mô hình quá nhiều UC là dấu hiệu sai mức | U-AP06, U-AP07, ngưỡng |
| Adolph, Bramble, Cockburn, Pols, Patterns for Effective Use Cases | VisibleBoundary, ClearCastOfCharacters, UserValuedTransactions, CompleteSingleGoal, VerbPhraseName, CommonSubBehavior, InterruptsAsExtensions, MergeDroplets (gộp UC vụn), RedistributeTheWealth (tách UC quá lớn), CleanHouse (loại UC không có giá trị) | P01 Bước 1, U-T1, U-N1, Bước 7 |
| Ambler, The Elements of UML 2.0 Style; agilemodeling.com/style/useCaseDiagram.htm (đã đối chiếu ngày thực hiện) | UC bắt đầu bằng động từ mạnh; thuật ngữ miền; UC chính và actor chính góc trên trái; xếp UC theo thời gian từ trên xuống; actor ở ngoài; actor là vai trò không phải chức danh; tên danh từ số ít; «system» cho actor hệ thống; actor không tương tác với nhau; actor Time cho sự kiện theo lịch; tránh mũi tên trên association; include khi biết chính xác lúc gọi; extend khi có thể gọi qua nhiều bước; dùng quan hệ tiết kiệm; không dùng «uses», «includes», «extends»; không quá hai tầng quan hệ UC; include bên phải, extend bên dưới, UC con bên dưới; quy tắc "is like"; boundary có ý nghĩa | P01 tên, Loại Thời gian; P03 phần D, D-AP05, D-AP18 |
| Kulak, Guiney, Use Cases: Requirements in Context | UC không phải chức năng, không phải màn hình; UC hướng hệ thống là lỗi | U-AP02, U-AP03, U-AP09 |
| Wiegers, Beatty, Software Requirements 3e | Bẫy use case: quá nhiều UC, UC quá phức tạp, đưa thiết kế giao diện vào UC, đưa định nghĩa dữ liệu vào UC, người dùng không hiểu UC, lạm dụng include và extend | U-AP01, U-AP02, D-AP17 |
| Lilly, Use Case Pitfalls (TOOLS 30, 1999) | Mười lỗi (nhớ theo tài liệu, không truy cập được toàn văn khi làm): ranh giới không rõ hoặc không nhất quán; UC viết từ góc nhìn hệ thống; tên actor không nhất quán; quá nhiều UC; quan hệ actor - UC như mạng nhện; đặc tả quá dài; đặc tả khó hiểu; UC không mô tả đúng quyền chức năng; khách hàng không hiểu UC; UC không bao giờ xong | P01 Bước 1, U-AP09, D-AP15 |
| Yourdon, Modern Structured Analysis | Phân tích sự kiện: sự kiện bên ngoài, sự kiện thời gian | P02 Bước 2 |

Ghi chú về ngưỡng (tất cả là heuristic, đã ghi rõ trong sản phẩm):
- Luồng chính 3-15 bước, dễ đọc 3-9: Cockburn khuyến nghị 3-9 bước; hợp đồng P04 và prompt cũ của người dùng dùng tối đa 14-15 bước. Chọn 3-15 làm ngưỡng ước lượng ở P02.
- 2-12 UC mỗi actor người, 10-40 UC cho hệ thống cỡ vừa, Subfunction không quá 20%: tổng hợp kinh nghiệm từ Bittner và Spence, Larman (hệ thống mẫu có vài chục UC), cảnh báo "too many use cases" của Wiegers, Lilly, và triệu chứng "too many use cases" ở new s29. Không có nguồn nào đưa con số cứng; sản phẩm ghi là heuristic và yêu cầu giải thích thay vì ép số.
- Sơ đồ không quá khoảng 20 UC và 8 actor, phân rã không quá khoảng 15 UC: dựa trên khả năng đọc (giới hạn bộ nhớ làm việc 7 cộng trừ 2 nhóm của Miller áp dụng cho số cụm trên sơ đồ, lỗi mạng nhện của Lilly, "tangle" ở new s62). Heuristic.
- Include tối đa hai tầng: Ambler.
- Số actor người 2-8: kinh nghiệm; mục đích là phát hiện đặt tên theo chức danh.

## 3. Chênh lệch giữa slide và tài liệu ngoài, lựa chọn đã áp dụng

| Chủ đề | Slide | Tài liệu ngoài | Lựa chọn trong sản phẩm |
|---|---|---|---|
| Đăng nhập | Là UC (sơ đồ tổng quát có Login; ví dụ đặc tả Log in của ATM; Log in có UC con) | Larman: Log In không qua Boss test, là subfunction; Cockburn: không phải user-goal | Theo slide: Đăng nhập là một UC riêng (U-R01), ghi Mức Subfunction, không include vào mọi UC, dùng tiền điều kiện. Cho phép ghi đè qua QUY_UOC_DA_CHOT |
| Mũi tên association | Tuỳ chọn, "commonly used to denote the initiator"; hình dùng mũi tên | Ambler: tránh mũi tên; Conventions C7: endArrow=none | Mặc định không mũi tên (theo C7, không trái slide vì slide nói tuỳ chọn); placeholder KIEU_DUONG_ASSOCIATION cho phép MUI_TEN_KHOI_XUONG. Mũi tên sai loại (nét đứt, tam giác, stereotype) luôn là lỗi |
| CSDL là actor | "They can be a peripheral device or even database" | UML, Cockburn: thành phần của subject không phải actor | CSDL của chính hệ thống không bao giờ là actor; CSDL thuộc hệ thống khác, chỉ truy cập qua giao diện, có thể là actor hệ thống ngoài. Cách hiểu này dung hoà được câu trên slide |
| Association giữa actor | old s22 liệt kê "association" giữa actor; old s24 gạch chéo hình actor nối actor | UML: actor chỉ association tới UC, Class, Component; Ambler: actor không tương tác với nhau | Cấm (D-AP06), theo hình ví dụ của slide |
| UC được include và actor | "never stands alone"; hình gạch chéo đường actor tới UC được include | UML cho phép UC được include là UC cụ thể có actor riêng | Mặc định không nối actor chính của UC gốc với UC được include hoặc UC mở rộng (theo slide); ngoại lệ có lý do khi UC đó cũng là mục tiêu độc lập (Bước 2.2b), và actor phụ chỉ tham gia phần đó được nối (theo ví dụ News System ở new s56) |
| CRUD | Gộp thành một UC "CRUD courses"; checkpoint "All CRUD use cases have been removed" | Larman, Cockburn: Manage X; tách khi khác actor, khác quy tắc | Mặc định gộp theo slide; tiêu chí tách lấy từ tài liệu ngoài, không mâu thuẫn slide vì slide chỉ loại CRUD "không có kết quả giá trị" |
| Tác nhân thời gian | Slide không nêu | UML không định nghĩa; Ambler khuyên dùng actor Time; Cockburn coi timer là trigger | Cho phép (hợp đồng P01 có Loại Thời gian); chỉ khi nguồn nêu hành vi định kỳ có giá trị nghiệp vụ |
| Tìm actor, UC | Lọc danh từ, động từ; bộ câu hỏi | Cockburn, Larman: hướng mục tiêu, actor-goal list, phân tích sự kiện | Dùng cả hai: P01 Bước 2 (danh từ, câu hỏi, sự kiện); P02 Bước 1-3 (mục tiêu, sự kiện, động từ) |
| Trình tự trên sơ đồ | "the sequence of use cases are not specified" | Ambler: gợi ý thời gian bằng vị trí trên dưới | Vị trí trên dưới chỉ là gợi ý bố cục (L-05), không có đường nối thể hiện trình tự (D-AP19) |
| Mũi tên extend | Hình: Place rush order --> Place order (từ UC mở rộng) | UML: từ extension tới extended | Thống nhất |
| Bố cục actor phụ bên phải | Hình slide đặt actor phụ bên phải (new s25, s64) | Ambler chỉ nói actor chính góc trên trái, actor bên ngoài | Actor chính trái, phụ phải (L-02, L-03) |

## 4. Tham khảo cách người dùng đã làm (không đưa nội dung đặc thù vào sản phẩm)

- ActorList.md, UsecaseList.md: người dùng trả lời bộ câu hỏi tìm actor, lập bảng actor, bảng đối tượng bị loại kèm lý do, bảng chức năng bị loại kèm quy tắc vi phạm, bảng kiểm tra lại theo quy tắc. Sản phẩm giữ cấu trúc này (bảng ứng viên bị loại ở P01, bảng ứng viên có kết luận ở P02) nhưng chuẩn hoá thành mã phép thử.
- Người dùng từng tạo UC "Refund order" được include bởi "Cancel order" với actor chính "thông qua" UC khác: đây là ca P02 Q4 và P03 Bước 2.2 xử lý (hoàn tiền là bước bắt buộc chỉ một UC dùng, thường nên là bước; chỉ tách khi đủ lớn). Không dùng ví dụ này trong sản phẩm.
- Prompts-UCSpec.md, prompts.docx: khung CRAFT, Action mô tả cách làm, Format nêu ràng buộc cụ thể (số bước, cấm từ giao diện), Target là tiêu chí tự kiểm. Sản phẩm theo khung này.
- Người dùng ưu tiên chế độ không giả định cho bài làm theo đề: sản phẩm phân biệt NGHIEM_NGAT và CO_NHAN theo Conventions.

## 5. Chạy thử trong đầu

Đề thử (tự viết, miền phòng khám, 14 ý):
1. Bệnh nhân đăng ký tài khoản bằng số điện thoại và đăng nhập để đặt lịch.
2. Bệnh nhân chọn chuyên khoa, bác sĩ, ngày và khung giờ trống để đặt lịch; mỗi khung 30 phút.
3. Bệnh nhân được huỷ lịch trước giờ hẹn ít nhất 4 giờ.
4. Bệnh nhân gọi điện thì lễ tân đặt lịch hộ trên hệ thống.
5. Hệ thống gửi SMS xác nhận qua cổng SMS của nhà mạng khi đặt hoặc huỷ lịch.
6. 24 giờ trước giờ hẹn hệ thống gửi SMS nhắc lịch.
7. Bệnh nhân tới, lễ tân xác nhận đã đến và xếp vào hàng chờ.
8. Bác sĩ xem danh sách bệnh nhân chờ trong ngày, ghi kết quả khám và đơn thuốc.
9. Bệnh nhân xem lịch sử khám và đơn thuốc.
10. Quản trị viên quản lý danh sách bác sĩ, chuyên khoa và lịch làm việc của bác sĩ.
11. Quản trị viên quản lý tài khoản nhân viên.
12. Cuối ngày hệ thống đánh dấu lịch hẹn không đến là vắng mặt.
13. Chủ phòng khám xem báo cáo số lượt khám theo bác sĩ theo tháng.
14. Dữ liệu lưu trên CSDL của phòng khám, sao lưu hằng đêm.

Kết quả P01 dự kiến: Ranh giới: Cổng SMS Ngoài, CSDL Trong. Tác nhân: Bệnh nhân, Lễ tân, Bác sĩ, Quản trị viên, Chủ phòng khám (Chính), Cổng SMS (Phụ), Bộ định thời (Chính). Không tổng quát hoá (chỉ chung Đăng nhập, không đủ điều kiện "giảm đáng kể số đường nối"). Bên liên quan: bệnh nhân khi đặt qua điện thoại (qua Lễ tân). Loại: CSDL (A-T1), máy chủ sao lưu (A-T1).

Kết quả P02 dự kiến (14 UC): Đăng ký tài khoản; Đăng nhập (U-R01; với nhân viên nguồn không nói phải đăng nhập, chế độ NGHIEM_NGAT sinh câu hỏi mở); Đặt lịch khám (Bệnh nhân, Lễ tân theo U-R10a; phụ Cổng SMS); Huỷ lịch khám; Nhắc lịch khám (Bộ định thời, U-R06, U-R07); Tiếp đón bệnh nhân; Ghi kết quả khám (xem danh sách chờ là bước, U-R05); Xem lịch sử khám; Đánh dấu lịch hẹn vắng mặt (Bộ định thời); Quản lý danh mục bác sĩ; Quản lý danh mục chuyên khoa; Quản lý lịch làm việc bác sĩ; Quản lý tài khoản nhân viên; Xem báo cáo lượt khám. Loại: Gửi SMS xác nhận (bước), Chọn khung giờ (bước, chỉ một UC dùng nên không include), Sao lưu (U-AP16, chuyển P06), Đăng xuất (không có trong nguồn).

P03 dự kiến: 14 UC, 7 actor, dưới ngưỡng, một sơ đồ tổng quát; không có include, extend (đúng tinh thần dùng quan hệ tiết kiệm).

Chỗ mơ hồ phát hiện và đã sửa:
1. Thứ tự áp dụng: cây quyết định Q4 sẽ đẩy Đăng nhập (Subfunction) thành "Là bước của" trước khi tới U-R01 ở Bước 6. Sửa: thêm "ngoại lệ ưu tiên" ở đầu Bước 5 (quy tắc U-R áp dụng trước cây quyết định), Bước 6 đổi thành bước rà soát.
2. Quản trị viên quản lý ba loại dữ liệu: U-R04 chưa nói gộp theo từng loại hay gộp chung. Sửa: thêm quy tắc "mỗi loại dữ liệu danh mục một UC Quản lý, chỉ gộp khi luôn cập nhật cùng nhau hoặc là thuộc tính phụ".
3. P01 ví dụ sai ghi "Đăng nhập" không phải mục tiêu, dễ khiến người đọc nghĩ P02 cũng loại Đăng nhập. Sửa: thêm "đăng nhập được xét riêng ở P02".
Chỗ đã kiểm tra, không cần sửa: "ghi kết quả khám và đơn thuốc" có chữ "và" nhưng cùng một phiên, không phạm U-AP05 (U-AP05 và U-N7 nói rõ "hai mục tiêu", "hai thời điểm"); việc sinh câu hỏi mở cho đăng nhập của nhân viên đúng với C1.

Kiểm tra file .drawio mẫu trong P03: đã tách ra, xmllint hợp lệ, xuất PNG bằng draw.io CLI thành công; note điều kiện bám đúng vào đường «extend» (draw.io hỗ trợ edge có target là edge).

## 6. Quyết định thiết kế

- Mã tiêu chí dùng chung cho P01, P02, P03, P02R: A-T1..A-T6 (tác nhân), U-T1..U-T12 (phép thử UC), U-AP01..U-AP16 (anti-pattern UC), U-R01..U-R17 (ca tranh cãi), U-N1..U-N8 (đặt tên), D-AP01..D-AP19 (lỗi sơ đồ), L-01..L-11 (bố cục). P02R chép lại tiêu chí dạng rút gọn để tự đủ khi dùng ngoài pipeline.
- Không tạo file danh mục anti-pattern riêng: nội dung đã nằm trong P02 phần A và P03 phần A; file riêng sẽ tạo nguy cơ lệch.
- P02 dùng cây quyết định Q1-Q5 có thứ tự cố định để kết quả lặp lại được giữa các lần chạy.
- UC mức Subfunction chỉ được giữ theo điều kiện Q4 a, b, c, d (a, b, c khớp new s43, s51, s57; d giữ mục tiêu con có kết quả riêng để include kiểu đặt hàng và thanh toán ra ổn định) hoặc U-R01.
- P03 không tự thêm UC; UC phát sinh đi qua bảng "UC đề xuất bổ sung" và "Đề xuất sửa artifact trước", đúng C1.3.
- Kết luận review P02R có quy tắc định lượng (Đạt / Đạt có điều kiện / Không đạt) để hai lần review cho cùng kết quả.

## 7. Đề xuất đổi hợp đồng

1. P01, bảng tác nhân: thêm cột "Tính chất (Chính / Phụ / Chính và phụ)" sau cột Loại (đã thêm trong P01, không bỏ cột lõi). Thêm mục "Ranh giới hệ thống" và "Bên liên quan không phải tác nhân" (P04 cần cho mục stakeholders and interests).
2. P02, bảng use case: thêm hai cột cuối "Mức (User-goal / Subfunction)" và "CAND nguồn". P03 cần cột Mức để quyết định include, extend.
3. P02, bảng ứng viên: thêm giá trị kết luận "Tách thành CAND-xx, CAND-yy" cho ứng viên mức summary, và cột "Nguồn phát hiện". Đề nghị cập nhật danh sách giá trị kết luận trong handoff-contracts.md.
4. P02: thêm mục "Danh sách mục tiêu tác nhân" và "Danh sách sự kiện" với mã cục bộ EV-nn. Đề nghị bổ sung EV-nn vào Conventions C3 (bước tạo: P02) nếu người tích hợp muốn mã này dùng được ở P04 (cột sự kiện kích hoạt).
5. P03, bảng quan hệ: thêm cột "Sơ đồ"; mã quan hệ RL-nn chưa có trong C3, đề nghị bổ sung (bước tạo: P03). Thêm bảng "Điểm mở rộng" (P04 dùng), bảng "UC đề xuất bổ sung".
6. P03, bảng Node: thêm các cột x, y, w, h để file .drawio sinh được từ bảng một cách tất định. Đề nghị cân nhắc đưa bốn cột này vào C7.1 cho mọi sơ đồ.
7. P02R: mã phát hiện UCR-nn chưa có trong C3; đề nghị bổ sung (bước tạo: P02R). Tên file đầu ra P02R-review.md chưa có trong C4; đề nghị bổ sung.
8. Conventions C7.3: style association đang là endArrow=none; đề nghị ghi thêm biến thể endArrow=open cho lựa chọn MUI_TEN_KHOI_XUONG, vì slide coi mũi tên chỉ bên khởi xướng là cách phổ biến.
