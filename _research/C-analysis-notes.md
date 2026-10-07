# Ghi chép nghiên cứu nhánh C (P07, P08, P09, P10, P11a, P11b)

File nội bộ, không thuộc sản phẩm. Số slide ghi theo số in trên slide; PDF gộp nhiều slide mỗi trang thì ghi thêm trang PDF.

## 1. Quy định trích từ slide

### 1.1. 03.1-Architectural Design.pdf (nội dung thực chất là Use-Case Analysis; PDF 4 slide mỗi trang, trang PDF n chứa slide 4n-3 đến 4n)

| Slide (trang PDF) | Quy định | Dùng ở |
|---|---|---|
| 3 (1) | Thiết kế kiến trúc gồm: cấu trúc mức cao và các thành phần; thiết kế mức cao cho giao diện ngoài và giữa thành phần; thiết kế mức cao cho CSDL | P09 A6, F7 |
| 4 (1) | Đầu vào thiết kế kiến trúc: glossary, supplementary spec, project specific guidelines, use-case model, analysis model | P09 đầu vào |
| 5 (2) | Supplement the use-case specification: "The system displays a list of courses" --> "retrieves and displays ... from the ... database" | P07 A2, F2 |
| 8 (2) | Use Cases --> Analysis Classes --> Design Elements --> Source Code: Use-Case Analysis là bước đầu | P07 mục đích |
| 9-10 (3) | Toàn bộ hành vi use case phải được phân bổ cho lớp phân tích; ba loại boundary, control, entity | P07 A6 |
| 11 (3) | Boundary: trung gian với bên ngoài; loại UI, system interface, device interface; "One boundary class per actor/use-case pair"; environment dependent | P07 A3, F3.1 |
| 12 (3) | Hình vai trò: actor chỉ nối boundary; boundary nối control; control nối entity; entity nối entity | P07 F6 |
| 14 (4) | UI boundary: tập trung thông tin trình bày, không chi tiết UI; system/device boundary: tập trung giao thức cần định nghĩa, không cách hiện thực | P07 F3.1 lỗi thường gặp |
| 15-16 (4) | Entity: key abstractions, từ use case, business-domain model, glossary; environment independent | P07 A4 |
| 17 (5) | Lọc danh từ: gạch chân danh từ trong flow of events; loại redundant, vague, actors (out of scope), implementation constructs, attributes (save for later), operations | P07 A4, F3.2 |
| 19-21 (5, 6) | Control: điều phối; use-case dependent, environment independent; "In general, one control class per use case"; use case thao tác dữ liệu đơn giản có thể không cần control; use case phức tạp có thể cần nhiều control (transaction manager, resource coordinator, error handler) | P07 A5 |
| 25 (7) | Với mỗi flow of events: identify analysis classes; allocate responsibilities; model interactions in interaction diagrams | P07 A6 |
| 26 (7) | Boundary: hành vi giao tiếp với actor; entity: hành vi trên dữ liệu đóng gói; control: hành vi riêng của use case | P07 A6 |
| 27 (7) | Ai có dữ liệu thì nhận trách nhiệm; nhiều lớp có dữ liệu: giao cho một lớp và thêm quan hệ, hoặc tạo lớp mới, hoặc giao cho control | P07 A6, F4 |
| 29-39 (8-10) | Sequence (thứ tự thời gian) và communication (cấu trúc, link); anatomy: lifeline, message, execution occurrence, reflexive message, hierarchical numbering 1, 1.1, ref interaction occurrence; tương đương ngữ nghĩa | P07 F5, F7 |
| 37 (10) | Một interaction diagram có thể không đủ: basic flow và các alternate flow vẽ riêng | P07 F5 ngưỡng tách |
| 41 (11) | Responsibility ghi "// PerformResponsibility" trong class diagram | P07 ký pháp "// tênTráchNhiệm" |
| 42 (11) | "Relationship for every link!" (link communication --> association 0..* ở class diagram) | P07 A8, F8 |
| 43 (11) | Unify analysis classes giữa các use case; boundary hệ thống ngoài (Course Catalog System, Billing System) xuất hiện ở nhiều use case và được hợp nhất | P07 A3 (tái dùng boundary hệ thống), P08 |
| 44 (11) | Review points lớp phân tích: tên phản ánh vai trò; một trừu tượng; trách nhiệm gắn kết; đủ hành vi; yêu cầu đặc thù được xử lý | P08 F6 |
| 45 (12) | Review points message: đủ luồng chính và phụ kể cả ngoại lệ; đủ đối tượng; hành vi phân bổ rõ ràng, đúng đối tượng; nhiều sơ đồ thì quan hệ rõ | P07 Target |

### 1.2. 03.2-Architectural Patterns-edited.pdf (1 slide mỗi trang; trang PDF p là slide p khi p <= 26, slide p+1 khi p >= 27 vì thiếu slide 27)

| Slide | Quy định | Dùng ở |
|---|---|---|
| 3 | Định nghĩa mẫu kiến trúc; mẫu hiện thực trong framework (3-layer, MVC, microservices) | P09 |
| 5-7 | Mục tiêu thiết kế tốt; 11 nguyên tắc: divide and conquer, cohesion, coupling, abstraction, reusability, reuse, flexibility, anticipate obsolescence, portability, testability, design defensively | P09 Role |
| 8-9 | Kiến trúc biểu diễn bằng nhiều view; refine: xác định tương tác, interface (trừu tượng, không hiện thực), phân bổ dữ liệu và chức năng cho thành phần | P09 A4, A6 |
| 11-13 | Multi-layer: UI, application logic, OS/DB/network access; UI --> Domain/Application --> Services (Persistence, Logging, Security subsystem); ví dụ package UI, AppCoordination, Domain, Services | P09 A4, F4 |
| 14 | Client-server (component, «communication») | P09 F2 |
| 15 | Broker (client proxy --> broker --> remote object) | P09 F2 |
| 16 | Transaction-processing (input --> dispatcher --> handlers) | P09 F2 |
| 17 | Pipe-and-filter (lưu ý đồng thời) | P09 F2 |
| 18 | MVC active (model updates, view fills, controller writes, notifies); "Problems?" nhiều model, view chằng chịt | P09 F2 rủi ro MVC |
| 19 | MVC passive (routing --> controller --> model, controller --> view) | P09 F2 |
| 20-21 | MVC so với 3-tier; MVC trong front-end/back-end | P09 F2, F5 |
| 22-23 | Front-end và back-end có thể dùng mẫu khác nhau | P09 A2 (kết hợp mẫu) |
| 24 | MVVM (data binding, commands, notifications) | P09 F2 |
| 25-26 | MVP (View, Presenter, Model/Interactor) | P09 F2, F5 |
| 28-29 | Flux (action, dispatcher, store, view) | P09 F2 |
| 30-31 | VIPER (view, interactor, presenter, entity, routing/wireframe) | P09 F2 |
| 33 | Bốn sơ đồ UML cho kiến trúc: package, subsystem, component, deployment | P09 F9, F10; P10 F7 |
| 34 | Package: nhóm phần tử liên quan logic; phụ thuộc «imports» | P09 F9 |
| 35 | Subsystem diagram: interface, specification elements, realization elements | P10, P11b |

### 1.3. 04-Identify Design Elements.pdf (4 slide mỗi trang)

| Slide (trang PDF) | Quy định | Dùng ở |
|---|---|---|
| 5 (2) | Ánh xạ nhiều-nhiều từ lớp phân tích sang phần tử thiết kế (class, subsystem, package) | P10 A2 |
| 6 (2) | Ánh xạ trực tiếp khi lớp đơn giản, một trừu tượng logic; lớp phức tạp: tách nhiều lớp, thành package, thành subsystem, kết hợp | P10 A2, F3 |
| 7 (2) | Định nghĩa class, package | P10 |
| 8 (2) | Tiêu chí nhóm package: đơn vị cấu hình, phân công nhóm phát triển, loại người dùng, sản phẩm và dịch vụ có sẵn | P10 A3, placeholder TIEU_CHI_NHOM_PACKAGE |
| 9 (3) | Boundary: giao diện dễ thay đổi đáng kể --> package riêng; ít thay đổi --> cùng package với lớp gắn kết chức năng | P10 A3, placeholder KHA_NANG_THAY_DOI_GIAO_DIEN |
| 10-11 (3) | Gắn kết chức năng: thay đổi lan truyền; bỏ lớp ảnh hưởng lớp kia; nhiều message; boundary trình bày entity; cùng actor; có quan hệ; tạo instance. Không cùng package: liên quan actor khác nhau; optional và mandatory | P10 A3 |
| 12 (3) | Visibility: chỉ lớp public được tham chiếu ngoài package | P10 A4, F5 |
| 13 (4) | Coupling: không cross-coupled; lower không phụ thuộc upper; không nhảy layer | P09 F6, P10 A5, F6 |
| 14-17 (4, 5) | Ví dụ package: main form aggregate boundary form; entity package với association và generalization; package External System Interfaces chứa interface I... | P10 F7, P11b A2 |

### 1.4. 05-Interface Design.pdf (4 slide mỗi trang)

| Slide (trang PDF) | Quy định | Dùng ở |
|---|---|---|
| 3 (1) | Tài liệu gốc phần GUI: JITEC Textbook No. 3 | P11a Căn cứ |
| 4, 8 (1, 2) | GUI design gồm 4 bước: standardizing screen configuration, screen images, screen transition diagram, screen specifications | P11a cấu trúc |
| 5 (2) | Display: kích thước, độ phân giải, số màu. Screen: vị trí nút chuẩn (OK, Cancel, Register, Search), vị trí thông điệp, tiêu đề và menu, nhất quán chữ số, diễn đạt câu, phối màu | P11a F1 |
| 6 (2) | Control: kiểu, kích thước, màu, chữ; quy trình kiểm tra nhập; thứ tự tiêu điểm (tab). Menu: theo chuẩn vùng client. Bàn phím: nhất quán phím tắt | P11a F1 |
| 7 (2) | Messages: hiển thị khi xử lý lâu (busy). Error: xử lý chuẩn. Help: nhất quán thuật ngữ với manual | P11a F1 |
| 9 (3) | Màn hình từ use case và boundary tương tác người dùng (ánh xạ boundary --> screen), từ mô tả input/output của đặc tả | P11a A2 |
| 10-11 (3) | Công cụ thiết kế; ví dụ wireframe | P11a F4, F6 |
| 13 (4) | Sơ đồ dịch chuyển: phân loại màn hình theo 4 mẫu, nối theo phân loại | P11a A3 |
| 14 (4) | Mẫu 1 simple transition: nét đứt, đầu mũi tên | P11a F3 |
| 15 (4) | Mẫu 2 dependent child (pop-up, cha không thao tác được): nét liền, thoi rỗng ở cha | P11a F3 |
| 16 (4) | Mẫu 3 independent child (pop-up, cha vẫn thao tác được): nét đứt, thoi rỗng ở cha | P11a F3 |
| 17 (5) | Mẫu 4 dependent screen with data: nét liền, mũi tên, nhãn dữ liệu ("Selected slide") | P11a F3 |
| 18 (5) | Sơ đồ liên kết: không vẽ cạnh đóng pop-up | P11a F3 quy tắc |
| 20-21 (5, 6) | Screen spec: screen image, list of functions (tên phần tử, chức năng, sự kiện, thuộc tính, kiểm tra nhập, xuất), defining field attributes | P11a F5 |
| 22 (6) | Mẫu spec: đầu trang (tên hệ thống, ngày tạo, approved by, reviewed by, person in charge), bảng Control, Operation, Function | P11a F5 a, d |
| 23-24 (6) | Field attributes: Item name, Number of digits (bytes), Type, Field attribute, Remarks | P11a F5 e |
| 26 (7) | System/Device interface design: identify subsystem, identify subsystem interfaces, subsystem design | P11b cấu trúc |
| 27-28 (7) | Subsystem realizes interface (canonical, elided); đóng gói hoàn toàn; nhiều biến thể hiện thực | P11b F5 |
| 30 (8) | Package không cung cấp hành vi, không đóng gói hoàn toàn; subsystem thì có, dễ thay thế | P10 A1 |
| 31 (8) | Dùng subsystem để chia phần có thể đặt hàng, phát triển, triển khai, thay đổi độc lập; bảo mật; biểu diễn sản phẩm có sẵn và hệ thống ngoài | P10 A1 |
| 33 (8) | Ứng viên subsystem: lớp cung cấp dịch vụ phức tạp, boundary (UI và external system); sản phẩm có sẵn (communication, DB access, types, utilities, application-specific) | P10 A1 |
| 34 (9) | "Superman class" boundary --> subsystem + interface | P10 A1 |
| 36 (9) | Bước xác định interface: ứng viên, điểm giống, phụ thuộc interface, ánh xạ vào subsystem, hành vi, đóng gói interface | P11b A2 |
| 37 (9) | Interface guideline: tên phản ánh vai trò; mô tả trách nhiệm; tên operation phản ánh kết quả, mô tả tham số và kết quả; tài liệu kèm sequence, state, test plan | P11b A3, F2, F3 |
| 38-39 (10) | Boundary hệ thống --> subsystem + interface; mọi lớp phân tích khác ánh xạ trực tiếp | P10 F1, F3 |
| 40 (10) | Tên interface bắt đầu bằng "I" | P10 F2, P11b F2 |
| 41-42 (10, 11) | Subsystem context: control phụ thuộc interface (required), subsystem hiện thực (provided) | P10 F8 |
| 44 (11) | Mục tiêu: loose coupling, plug-and-play, cô lập thay đổi; không lộ chi tiết, chỉ phụ thuộc interface | P11b A4, A6 |
| 45-48 (11, 12) | Các bước: distribute behavior (sequence cho mỗi operation, class diagram), document elements, describe dependencies, checkpoints | P11b A4-A6 |
| 49 (12) | Gate: điểm nối trên biên sequence diagram | P11b F4 |
| 50-52 (13) | Black-box (client --> supplier subsystem) và white-box (subsystem manager điều phối design element) | P11b F4 |
| 54, 56 (14) | Ví dụ subsystem gồm lớp điều phối, lớp transaction, lớp interface ngoài | P11b A4, F5 |
| 58-59 (15) | Phụ thuộc subsystem vào subsystem qua interface (ưu tiên), vào package (thận trọng) | P11b A6, F6 |
| 61 (15) | Checkpoints: realization cho mỗi interface cung cấp; dependency cho mỗi interface dùng; không phần tử bên trong public; mỗi operation có interaction diagram hoặc ánh xạ 1-1 | P11b F7 b |

## 2. Tài liệu ngoài đã dùng

| Tài liệu | Quy tắc lấy về | Bước |
|---|---|---|
| Jacobson, Booch, Rumbaugh, The Unified Software Development Process (1999); Kruchten, RUP: An Introduction (2003) | Use-case realization, lớp phân tích B/C/E, hợp nhất lớp, Identify Design Elements, subsystem design | P07, P08, P10, P11b |
| Rosenberg, Stephens, Use Case Driven Object Modeling with UML (2007) | Quy tắc robustness: actor chỉ nói với boundary; boundary chỉ nói với controller và actor; entity chỉ nói với controller; controller nói với boundary, entity, controller, không nói với actor | P07 F6 |
| Larman, Applying UML and Patterns (2004) | GRASP Information Expert, Creator, Controller, Low Coupling, High Cohesion; domain model, multiplicity, phép thử is-a; layered logical architecture | P07 A6, P08 F4, P09 |
| OMG UML 2.5.1 | Ngữ nghĩa lifeline, message, combined fragment, gate, communication diagram, class relationships, package, component, deployment | P07-P11b |
| Fowler, UML Distilled (2003) | Sequence ở mức khái niệm và mức thiết kế; aggregation và composition | P07, P08, P11b |
| Ambler, The Elements of UML 2.0 Style (2005) | Bố cục, đặt tên, giữ sơ đồ đơn giản, tách view | Ngưỡng sơ đồ |
| Wirfs-Brock, McKean, Object Design (2003); Riel, Object-Oriented Design Heuristics (1996) | Trách nhiệm, phát hiện god class | P07 ngưỡng control |
| Evans, Domain-Driven Design (2003) | Ngôn ngữ chung, đồng nghĩa và đồng âm | P08 A3 |
| Bass, Clements, Kazman, Software Architecture in Practice (2021) | ASR, quality attribute scenario | P09 A1, F1 |
| Buschmann và cộng sự, POSA vol. 1 (1996); Lethbridge, Laganière (2005) | Layers, Pipes and Filters, Broker, MVC; các nguyên tắc thiết kế tốt (nguồn gốc nội dung slide 03.2) | P09 |
| Martin, Agile Software Development (2002), Clean Architecture (2017) | REP, CCP, CRP, ADP, SDP, SAP; ISP, DIP | P09 F6, P10, P11b |
| Nygard, ADR (2011), Release It! (2018) | Bản ghi quyết định; timeout, retry, cô lập lỗi | P09 F3, P11b A5 |
| Hohpe, Woolf, Enterprise Integration Patterns (2003) | Idempotent receiver | P11b A5 |
| Japan Information Processing Development Corporation, Japan Information-Technology Engineers Examination Center, Textbook for Software Design and Development Engineers, No. 3: System Development, Operations and Maintenance, 2nd ed. | Nguồn của bốn mẫu dịch chuyển màn hình; chuẩn hoá cấu hình màn hình, đặc tả màn hình và thuộc tính trường. Không trích trong sản phẩm (P11a) để giữ trung lập | P11a F2, F3, F5 |
| Nielsen 10 heuristics; Shneiderman 8 golden rules (bản 6th ed. dùng "seek universal usability" thay "shortcuts"); WCAG 2.2 AA; Material 3; Apple HIG; Baymard | Chuẩn trình bày và đánh giá | P11a F1, F7 |

## 3. Chênh lệch giữa slide và tài liệu ngoài, lựa chọn áp dụng

1. Entity gọi entity. ICONIX cấm (entity chỉ nói với controller). Slide 12, 16, 27 cho phép entity liên kết entity và giao trách nhiệm cho lớp có dữ liệu kèm quan hệ tới lớp kia. Chọn theo slide: entity được gọi entity khi có quan hệ cấu trúc.
2. Use case không có control. Slide 21 cho phép. Sản phẩm mặc định luôn giữ control (có thể tối giản) để quy tắc tương tác F6 và bảng ánh xạ P09 F5 thống nhất; chỉ bỏ khi YEU_CAU_BO_SUNG cho phép. Đây là mặc định chặt hơn slide, không trái slide.
3. Boundary hệ thống ngoài. Slide 11 "một boundary cho mỗi cặp actor/UC", slide 43 cho thấy boundary hệ thống ngoài dùng chung nhiều UC. Chọn: vẫn một boundary cho mỗi cặp, nhưng boundary hệ thống, thiết bị được đặt tên theo hệ thống và tái dùng mã; boundary người dùng không dùng chung.
4. Ký pháp trách nhiệm. Slide 41 dùng "// PerformResponsibility" (PascalCase); slide 05 dùng "// submit bill()". Chọn "// tênTráchNhiệm" lowerCamelCase không ngoặc để P12 chuyển thẳng thành tên phương thức, và dấu "//" phân biệt với chữ ký phương thức.
5. Tiêu chí nhóm package: slide 04 dùng tiêu chí gắn kết chức năng của RUP; Martin có REP, CCP, CRP. Chọn slide làm chính, Martin làm tham chiếu ở Role và kiểm tra coupling.
6. Kích thước vùng bấm: WCAG 2.5.8 là 24 x 24 px; Material 48 dp; HIG 44 pt. Chọn WCAG là tối thiểu bắt buộc, hướng dẫn nền tảng khi NEN_TANG phù hợp.
7. Screen spec: slide chỉ có Control, Operation, Function và bảng field attributes 5 cột. Sản phẩm giữ các cột đó, thêm cột Loại, Nguồn, Ràng buộc dữ liệu theo yêu cầu người tích hợp. Không mâu thuẫn slide.
8. Cạnh đóng pop-up: slide 18 không vẽ cạnh quay về. Sản phẩm cấm vẽ cạnh đóng pop-up.
9. Tên file slide 03.1 là "Architectural Design" nhưng nội dung là Use-Case Analysis. P09 lấy nội dung kiến trúc từ 03.1 slide 3-4 và toàn bộ 03.2.

## 4. Lý do các ngưỡng định lượng

Mọi ngưỡng dưới đây là heuristic để AI tự phát hiện bất thường, không phải luật UML; prompt dùng từ "khoảng", "thường".

| Ngưỡng | Ở đâu | Lý do |
|---|---|---|
| Sequence tối đa khoảng 30 message, 3 fragment ngoài cùng mỗi trang | P07 F5 | Slide 37 (một sơ đồ có thể không đủ); Ambler khuyên giữ sơ đồ đơn giản, tách theo kịch bản; khoảng 30 message với khoảng cách 40 px vừa một trang A4 dọc |
| Control 2-10 trách nhiệm mỗi UC; trên 10 là dấu hiệu god control; sau hợp nhất 15 | P07 F3.4, P08 A4 | Riel (tránh god class), CRC card của Beck và Cunningham (trách nhiệm vừa một thẻ); control sau hợp nhất chỉ gom trách nhiệm của UC nó điều phối nên nới lên 15 |
| 4-12 lớp mỗi UC | P07 F3.4 | Cấu hình điển hình 1 control, 1-2 boundary, 2-8 entity |
| Tối đa khoảng 20 lớp mỗi trang class diagram | P08 F5 | Ambler (tách view); giới hạn khả năng đọc |
| 3-10 yêu cầu có ý nghĩa kiến trúc | P09 F1 | Bass et al. thường ưu tiên số ít kịch bản chất lượng quan trọng nhất |
| 3-5 layer, 1-8 package cấp cao mỗi layer | P09 F4 | Ví dụ slide 03.2 (3-4 layer); Larman |
| 2-15 phần tử mỗi package | P10 F4 | CCP, CRP: package quá nhỏ gây phụ thuộc vụn, quá lớn gắn kết thấp |
| 1-7 operation mỗi interface, trên 10 cân nhắc tách | P11b F2 | ISP (Martin); các ví dụ interface trong slide 05 có 1-4 operation |
| 1-5 màn hình mỗi UC | P11a F2 | Mỗi màn hình một mục tiêu con (xem, nhập, xác nhận, kết quả) |

## 5. Thử chạy P07 trong đầu (miền giao đồ ăn)

UC mẫu: "UC-012 Đặt món". Tác nhân chính Khách hàng; nhà hàng nhận đơn mới; include "UC-013 Thanh toán" (tác nhân Cổng thanh toán). Luồng: khách mở giỏ, chọn địa chỉ, hệ thống tính phí giao theo BR, khách xác nhận, hệ thống kiểm tra nhà hàng còn mở và món còn bán, include thanh toán, tạo đơn, báo nhà hàng.

Chỗ mơ hồ phát hiện và cách sửa trong P07:
1. Cổng thanh toán là tác nhân của UC được include, P02 có thể liệt kê nó là tác nhân phụ của UC-012. Prompt ban đầu sẽ tạo boundary cổng thanh toán trong UC-012. Đã thêm quy tắc ở A3: tác nhân chỉ thuộc UC được include/extend thì boundary thuộc phân tích của UC đó; sửa Target 3 tương ứng.
2. UC-013 chưa phân tích thì control của nó chưa có mã. Đã thêm ở A1: đặt trước mã control, trạng thái "Tạm - chờ P07".
3. Nhà hàng chỉ nhận thông tin (không thao tác trong UC). Prompt ban đầu không nói rõ có cần boundary không. Đã thêm ở A3: tác nhân phụ là người chỉ nhận thông tin vẫn cần boundary giao diện người dùng.
4. Message của actor ban đầu viết tiếng Việt ("// chọn khung giờ") trong khi message khác tiếng Anh. Đã thống nhất: mọi message cùng dạng lowerCamelCase theo NGON_NGU_TEN_PHAN_TU.
5. Lớp Cart tái dùng từ UC "Thêm món vào giỏ": không rõ cột trách nhiệm ghi mọi trách nhiệm hay chỉ trong UC này. Đã quy định: chỉ trách nhiệm dùng trong UC này.
6. Mục A5 ban đầu diễn đạt rối về trường hợp không có control. Đã viết lại: mặc định giữ control; chỉ bỏ khi YEU_CAU_BO_SUNG cho phép.
Kết quả mong đợi sau sửa: AC-B-PlaceFoodOrderForm, AC-B-RestaurantOrderBoard (hoặc tên tương đương), AC-C-PlaceFoodOrderController, AC-E-Cart, AC-E-FoodOrder, AC-E-OrderLine, AC-E-DeliveryAddress (chỉ khi địa chỉ có định danh và được lưu để chọn lại; nếu không thì là thuộc tính), AC-E-Restaurant, AC-E-Dish; message tới AC-C-PayOrderController (tạm) cho bước include. Không có vi phạm F6.

## 6. Đề xuất đổi hợp đồng

1. C3 thêm mã MSG-nn (thông điệp, P11a, phạm vi cục bộ trong P11a-gui/ui-standards.md) và R-nn / R-UCnnn-nn (quan hệ lớp: P07 cấp R-UCnnn-nn, P08 cấp R-nn toàn hệ thống). Hiện prompt đã dùng các mã này và ghi là cục bộ.
2. C4 thêm thư mục P11a-gui/mockups/ (HTML tĩnh tuỳ chọn) và liệt kê tên file sơ đồ: P07-sequence-UC-nnn, P07-communication-UC-nnn, P07-class-UC-nnn, P08-class-analysis, P09-package-layers, P09-deployment, P10-package-design, P10-subsystem-context, P11a-screen-transition, P11b-subsystem-SS-nn.
3. C7.3 bảng style bổ sung: bốn kiểu dịch chuyển màn hình (xem P11a F3), message bất đồng bộ (endArrow=open;endFill=0;), subsystem (shape=component;), interface dạng elided (ellipse 20 x 20), node deployment (shape=cube;), fragment sequence (rectangle fillColor=none, align=left, verticalAlign=top).
4. Bảng lõi P07 thêm cột (được phép): Loại boundary, Mới hoặc tái dùng, GL; thêm bảng quan hệ VOPC | ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn | để P08 đọc. Bảng sequence thêm cột Loại, Fragment.
5. Bảng lõi P08 thêm cột Loại boundary, Trạng thái (Hoạt động / Gộp vào AC-...), vì C3 yêu cầu giữ mã phần tử bị loại.
6. P09 thêm bảng lõi "Quy tắc ánh xạ stereotype sang layer" (F5). Nhánh D (P12) nên đọc bảng này cùng bảng ánh xạ P10 F3.
7. P11b cấp DC cho phần tử bên trong subsystem (F5 a). Nhánh D (P12) phải coi các DC này là lớp thiết kế cần chi tiết hoá, nguồn là "P11b SS-nn" thay vì AC.
8. P11a phụ thuộc bảng dữ liệu vào ra của P04 (cột Điều kiện hợp lệ). Hợp đồng P04 ghi "(nếu slide có)"; đề nghị nhánh B luôn xuất bảng này, nếu không P11a sẽ sinh nhiều câu hỏi mở về ràng buộc trường.
9. P11a-gui/screen-list.md thêm cột Lớp thiết kế (DC), Mục đích, Bước UC phục vụ; cột Loại dùng bốn giá trị theo mẫu dịch chuyển (Độc lập, Con phụ thuộc, Con độc lập, Phụ thuộc có dữ liệu).
10. P11b bảng lõi thêm cột Tiền điều kiện, Hậu điều kiện, Đồng bộ, Idempotent, Timeout.

## 7. Điểm còn băn khoăn

- Communication diagram trong draw.io: mũi tên chiều message là edge tự do, AI dễ đặt lệch. Có thể cân nhắc cho phép ghi chiều trong nhãn (ví dụ "1: // x (A-->B)") thay cho mũi tên rời.
- Kích thước đầu ra P07 lớn (7 bảng, 3 sơ đồ). Chế độ GON hiện chưa cắt mục nào của P07 vì slide yêu cầu cả sequence và communication. Người tích hợp có thể quyết định cho GON bỏ communication diagram cho luồng thay thế.
- Hậu tố tên boundary và control (Form/UI, Controller/Control) phụ thuộc lựa chọn của dự án; nếu không ghi trong YEU_CAU_BO_SUNG, các lần chạy P07 có thể không thống nhất cho tới khi sổ đăng ký AC có mục đầu tiên.
- P09 dùng "controller" của MVC và "control" của phân tích: đã cảnh báo, nhưng P12 cần giữ phân biệt khi đặt tên lớp.
