# Nhánh D - Ghi chép nghiên cứu (P12, P13, X1, X2)

File nội bộ, không thuộc sản phẩm. Số slide là số in trên slide; các PDF in 4 slide mỗi trang nên trang PDF = làm tròn lên (số slide / 4). Ví dụ slide 42 nằm ở trang PDF 11.

## 1. Trích quy định từ slide

### 1.1. 06-Class Design.pdf (88 slide, 22 trang) --> P12

| Slide (trang) | Quy định | Dùng ở |
|---|---|---|
| 3 (1) | Sáu hoạt động theo thứ tự: Create Initial Design Classes, Define Operations/Methods, Define Relationships, Define States, Define Attributes, Class Diagram | P12 [Action] Bước 1-6 |
| 5-7 (2) | Ánh xạ nhiều - nhiều từ lớp phân tích sang phần tử thiết kế; lớp phân tích ánh xạ thẳng khi đơn giản và là một trừu tượng logic; lớp phức tạp có thể tách, thành package, subsystem; xét design pattern | Bước 1.1, Bước 7 |
| 8 (2) | Nhiều lớp đơn giản vs ít lớp phức tạp; "A class should have a single well-focused purpose" | Bước 1.6, F1 |
| 9 (3) | Boundary giao diện: phụ thuộc công cụ phát triển giao diện; boundary hệ thống ngoài thường là subsystem | Bước 1.2 |
| 10 (3) | Entity thụ động, persistent; tách FatClass theo hiệu năng (DataHelper, LazyDataHelper, 1 - 0..1). Control: có cần không, có tách không; căn cứ complexity, change probability, distribution and performance, transaction management | Bước 1.3, 1.4 |
| 12-15 (3-4) | Tiêu chí gom package: boundary riêng nếu giao diện dễ đổi; tiêu chí lớp liên quan chức năng; hai lớp liên quan tác nhân khác nhau, lớp tuỳ chọn và bắt buộc không cùng package | P12 F9 |
| 16-17 (4-5) | Chỉ lớp public của package được tham chiếu từ ngoài; package không cross-coupled; layer dưới không phụ thuộc layer trên; không nhảy layer | P12 F9, X1 PKG |
| 23-24 (6) | Operation từ message; tên theo góc nhìn client, nêu outcome, nhất quán; chữ ký operationName([direction]parameter: class,..): returnType; direction in (mặc định), out, inout; bổ sung manager functions, class copies, equality | Bước 2.1-2.4, F2 |
| 25-26 (7) | Tham số: by value/by reference, bị thay đổi, tuỳ chọn, mặc định, miền hợp lệ; càng ít càng tốt; "Pass objects instead of data bits"; tài liệu hoá (param, return, throws) | Bước 2.3, 2.5, F2 |
| 27-28 (7) | Visibility + # - | F2, F7 |
| 29 (8) | Scope: instance vs classifier, classifier gạch chân | F2, F7, F8 |
| 31 (8) | Method: special algorithms, other objects/operations, attributes/parameters, relationships | Bước 2.6, F3 |
| 33-40 (9-10) | Association, role, multiplicity (1, 0..1, 0..*, *, 1..*, 2..4, 2, 4..6); multiplicity trả lời bắt buộc/tuỳ chọn và min/max | F5 |
| 41-47 (11-12) | Association (use-a), aggregation (has-a/part-of), composition (share lifetime, whole tạo/huỷ part, part có thể bị xoá trước); "When in doubt, use association" | F5 |
| 48-50 (12-13) | Navigability: xem interaction diagram; một chiều khi chiều kia hiếm dùng hoặc số đối tượng nhỏ | F5 |
| 51-57 (13-15) | Dependency vs association: link thành association trừ khi có global, local, parameter visibility; permanent --> association; transient --> dependency; "Strive for the lightest relationships possible"; chia sẻ thể hiện --> tham số hoặc global; tạo tốn kém --> field/tham số/global | F5 cây quyết định |
| 58-59 (15) | Generalization: "is a kind of", đơn/đa kế thừa | F5 |
| 61-70 (16-18) | State machine: state, transition, event(args)[guard]/activity; initial (bắt buộc, một), final (tuỳ chọn, nhiều), choice; trạng thái từ thuộc tính động và sự tồn tại link; event từ operation; entry/do/exit; lớp nào cần; event --> operation, state --> attribute | F6 |
| 72-76 (18-19) | Attribute: name: Type = InitValue; nguồn thuộc tính (danh từ không thành lớp, method, state, thông tin tự duy trì, owned, không có hành vi); kiểu nguyên tố của ngôn ngữ; derived khi không đủ thời gian tính lại, đánh đổi hiệu năng/bộ nhớ | F7 |
| 80 (20) | Class diagram dùng cho vocabulary, collaborations, logical database schema | F8 |
| 82-85 (21-22) | Review points cho class, operation, attribute, relationship | P12 [Target], X1 CNS |
| 87-88 (22) | Tài liệu hoá: attribute (type, description), operation (signature, purpose, params, return, exceptions), method (algorithm, cách dùng params) | F2, F3 |

### 1.2. 07-Data Modeling.pdf (66 slide, 17 trang) --> P13

| Slide (trang) | Quy định | Dùng ở |
|---|---|---|
| 5-6 (2) | Ba mô hình: conceptual (E-R, độc lập DBMS) --> logical (relational/network/hierarchical, phụ thuộc DBMS) --> physical | P13 mục 1, F3-F6 |
| 7 (2) | ER: entity, relationship, attribute (hình minh hoạ ký pháp Chen) | F3, F8.2 |
| 9-12 (3) | CSDL phân cấp, mạng, quan hệ; cột gạch chân là khoá chính | Chỉ nhắc quan hệ; phân cấp và mạng không đưa vào sản phẩm vì không còn phổ biến |
| 13-19 (4-5) | NoSQL: document, schema-free; normalization vs aggregation; aggregates vs joins (static 1-N vs dynamic M-N); atomic aggregates | F7 |
| 20 (5) | Three-layer schema (external, conceptual, internal) | Căn cứ P13 |
| 21-22 (6) | RDBMS và OO không tương thích hoàn toàn | Bối cảnh |
| 25-26 (7) | Entity --> table; quan hệ 1:1, 1:m, m:1, m:n; m:n thường chia thành 1:m và m:1 | F4.2 |
| 27-28 (7) | Dependency relationship: FK nằm trong PK con, nét liền; independency: FK ngoài PK, nét đứt | F4.2, F8.1 |
| 31-32 (8) | Lớp persistent --> entity; mỗi dòng là một object; association --> FK (independency) | F2, F4.2 |
| 33-34 (9) | Aggregation --> dependency relationship bằng FK; composition --> cascading delete; có thể map về independency để đơn giản PK | F4.2 |
| 36-38 (9-10) | Kế thừa: hai phương án: bảng riêng (normalized) hoặc lặp thuộc tính kế thừa (de-normalized) | F4.3 |
| 39-40 (10) | M:N: bảng trung gian C với hai FK, thêm thuộc tính nếu cần | F4.2 |
| 43-48 (11-12) | Chuẩn hoá: mục đích (lưu trữ, toàn vẹn, mở rộng); Codd; 1NF, 2NF, 3NF; 3NF đủ cho đa số; phần lớn bảng 3NF cũng là BCNF; định nghĩa FD | F5 |
| 49-60 (13-15) | Ví dụ chuẩn hoá đơn hàng trực tuyến (Order, Product, Customer, Address, Quantity, UnitPrice) | Sản phẩm dùng ví dụ khác (phiếu xuất kho) cùng cấu trúc: 2 phụ thuộc bộ phận + 1 bắc cầu |

### 1.3. 08-Unit Test.pdf (81 slide, 21 trang) --> X2

| Slide (trang) | Quy định | Dùng ở |
|---|---|---|
| 5-6 (2) | Mức test: unit, integration, system, acceptance; unit dùng black box và white box | X2 mục 1 |
| 7-9 (2-3) | Quy trình: chọn input, định nghĩa kết quả mong đợi (oracle), chạy, so sánh; black box chọn input không biết hiện thực; white box biết hiện thực, dùng coverage | X2 Bước 3, 4 |
| 10 (3) | Test case, test suite, test plan | F3 định nghĩa |
| 12 (3) | Kỹ thuật black box: Equivalence Partitioning, Boundary-value, Decision Table, Use Case-based; white box: Control flow C0, C1; Sequence chart coverage | X2 Bước 3, 4 |
| 13-18 (4-5) | EP: chia miền đầu vào thành lớp tương đương; bài học: phải thêm lớp "Invalid value" | Bước 3.1, F2.x.2 |
| 19-20 (5) | BVA: 69/70, 100/101, -1/0; lỗi > thay vì >= | Bước 3.2, 4.5 |
| 21-25 (6-7) | Decision table: điều kiện Y/N, hành động X, N/A cho tổ hợp không thể; câu hỏi "cả hai không hợp lệ thì hai thông báo?" --> xác nhận đặc tả | Bước 3.3, 3.6 |
| 26-28 (7) | Test theo use case: kịch bản luồng chính, mỗi luồng thay thế, tổ hợp hợp lý, vòng lặp; ví dụ đăng nhập mã PIN sai 3 lần | Bước 3.5 |
| 29-35 (8-9) | C0 = lệnh thực thi / tổng lệnh; C1 = nhánh / tổng nhánh; coverage không phát hiện chức năng chưa hiện thực; một TC hộp trắng phủ nhiều TC hộp đen nhưng vẫn cần TC biên | Bước 4.3, 4.5 |
| 36 (9) | Sequence chart coverage cho integration test | Không đưa vào X2 (thuộc tích hợp) |
| 37-41 (10-11) | Vòng lặp: skip, 1, m, n-1, n, n+1; vòng lồng: cố định một vòng ở số điển hình | Bước 4.4 |
| 42-43 (11) | Kết hợp: black box trước, white box sau để phủ đường còn lại | Bước 3 "luôn làm trước", Bước 4.3 |
| 44-75 (11-19) | JUnit: tên lớp XxxTest, setUp/tearDown, assert có message, test độc lập, một thứ mỗi test, tránh try/catch, expected exception, không phụ thuộc thứ tự, không chia sẻ trạng thái | F5 |
| 76-79 (19-20) | Stub/driver; top-down cần stub, bottom-up cần driver; big-bang, sandwich | Bước 5, mục 5 |
| 80 (20) | Regression test | Mục 5 |

### 1.4. 09-Programming.pdf --> X1 (nguyên lý bổ trợ, smell)

| Slide (ước lượng) | Quy định | Dùng ở |
|---|---|---|
| khoảng 30-31 | Refactoring main principles: KISS, DRY, separate concerns, appropriate abstraction | X1 PRN |
| khoảng 33-48 | Code smells: bloaters (long method, large class, primitive obsession, long parameter list, data clumps), OO abusers (switch, temporary field, refused bequest), change preventers (divergent change, shotgun surgery), conditional complexity (cyclomatic complexity), dispensables (lazy class, data class, duplicated code, dead code, speculative generality/YAGNI), couplers (feature envy, inappropriate intimacy, LoD, message chains, middle man, hidden dependencies, hidden temporal coupling) | X1 SML, PRN; X2 V(G) |

### 1.5. 10-Modular Design 4pages.pdf (24 slide, 6 trang) --> X1 MOD

| Slide (trang) | Quy định |
|---|---|
| 3 (1) | Module: hàm, lớp, kiểu, đơn vị thiết kế; modular design quan tâm module nào, đặc tả, quan hệ |
| 10 (3) | Good design: dễ phát triển, test, đọc, trao đổi, mở rộng, bảo trì |
| 12 (3) | Ideals: decomposable, composable, understandable, continuity, isolation |
| 17-20 (5) | Cohesion, coupling; "loose coupling and high cohesion" |
| 21-24 (6) | SOLID; GoF ba nhóm (creational, structural, behavioral) |

### 1.6. 11-Coupling and Cohesion 4pages.pdf (69 slide, 18 trang) --> X1 CPL, COH

| Slide (trang) | Quy định |
|---|---|
| 8 (2) | Thang coupling: Content, Common, Control, Stamp, Data (chặt --> lỏng) |
| 9-14 (3-4) | Content: sửa dữ liệu module khác, reflection, goto; sửa: truy cập qua hàm |
| 15 (4) | Câu hỏi getter/setter cho mọi thuộc tính có phải content coupling |
| 16-19 (4-5) | Common: dữ liệu toàn cục; sửa: module quản lý dữ liệu |
| 20-25 (5-7) | Control: tham số cờ; sửa: tách operation, đa hình, pattern |
| 26-31 (7-8) | Stamp: truyền cấu trúc chỉ dùng một phần; có thể cần vì hiệu năng; sửa: truyền dữ liệu nguyên tố cần thiết |
| 32-36 (8-9) | Data coupling (tốt nhất); Law of Demeter và danh sách đối tượng được gửi message |
| 41-42 (11) | God class là anti-pattern |
| 43-45 (11-12) | Cohesion; đo ở method, class, subsystem; thang: Coincidental, Logical, Temporal, Procedural, Communicational, Functional |
| 46-65 (12-17) | Từng mức cohesion, dấu hiệu, cách sửa |
| 66-67 (17) | Ví dụ minh hoạ có thêm Sequential (đầu ra của hàm này là đầu vào hàm sau) giữa Communicational và Functional |

### 1.7. 12-Design Principles 4pages.pdf (52 slide, 13 trang) --> X1 SOLID, GRASP

| Slide (trang) | Quy định |
|---|---|
| 5 (2) | Nguyên lý cơ bản: SOLID; GRASP (High Cohesion, Low Coupling, Polymorphism, Information Expert, Pure Fabrication, Protected Variations, Indirection, Creator, Controller); Favor composition over inheritance; Program to an Interface |
| 11-18 (3-5) | SRP: một lý do thay đổi; ví dụ tách trách nhiệm sắp xếp khỏi entity |
| 20-28 (5-7) | OCP: trừu tượng là chìa khoá; đa hình động và tĩnh |
| 31-36 (8-9) | LSP: demand no more, promise no less; dùng composition thay kế thừa hiện thực |
| 39-44 (10-11) | ISP: nhiều interface theo client tốt hơn một interface tổng |
| 46-51 (12-13) | DIP: phụ thuộc trừu tượng; client sở hữu interface (ownership inversion); DIP và OCP |

Slide 12 không đề cập REP, CCP, CRP, ADP, SDP, SAP, DRY, KISS, YAGNI. Các nguyên lý này lấy từ tài liệu ngoài (Martin) và slide 09 (KISS, DRY, YAGNI).

## 2. Tài liệu ngoài đã dùng

| Tài liệu | Quy tắc lấy vào |
|---|---|
| OMG UML 2.5.1 | Cú pháp operation, property, multiplicity; ngữ nghĩa aggregation (shared) và composite; state machine: pseudo state initial, choice, final; entry/do/exit; cú pháp nhãn trigger [guard] / effect |
| Fowler, UML Distilled | "Khi phân vân dùng association"; composition: part chỉ thuộc một whole; state machine vs activity |
| Ambler, Elements of UML 2.0 Style | Đặt tên trạng thái bằng tính từ/phân từ; bố cục lớp cha trên lớp con; giới hạn kích thước sơ đồ (sơ đồ nên đọc được trên một trang) |
| Larman, Applying UML and Patterns | GRASP; bốn loại visibility (attribute, parameter, local, global) khớp slide 51-57; Controller |
| Martin, Agile Software Development; Clean Architecture | SOLID; REP, CCP, CRP, ADP, SDP, SAP; chỉ số Ca, Ce, I, A, D |
| Gamma và cộng sự | Danh mục pattern và dấu hiệu áp dụng |
| Fowler, PoEAA | Single Table, Class Table, Concrete Table Inheritance; Foreign Key Mapping; Association Table Mapping; Dependent Mapping; Embedded Value; Identity Field; Repository |
| Ambler, Agile Database Techniques | Ánh xạ đối tượng - quan hệ, khoá thay thế |
| Chen 1976; Elmasri và Navathe | Ký pháp ER: thực thể, thực thể yếu, mối quan hệ, thuộc tính khoá, đa trị, dẫn xuất |
| Codd 1970, 1972; Date | FD, 1NF-3NF, BCNF; ví dụ BCNF kinh điển (sinh ra từ cấu trúc "mỗi X chỉ thuộc một Y") |
| Sadalage và Fowler, NoSQL Distilled; Evans, DDD; tài liệu MongoDB | Aggregate, đơn vị nhất quán; quy tắc embed/reference |
| Stevens, Myers, Constantine 1974; Yourdon và Constantine 1979; Myers 1978 | Thang coupling/cohesion; external coupling; sequential cohesion |
| Meyer, OOSC | Tiêu chí module (tương ứng decomposable, composable, understandable, continuity, protection/isolation); design by contract |
| Lieberherr và Holland 1989 | Law of Demeter |
| Fowler, Refactoring | Tên smell và refactoring |
| Myers, The Art of Software Testing; ISTQB CTFL | EP, BVA, DT, state transition, statement/branch/condition coverage |
| McCabe 1976 | V(G) = E - N + 2 (với một thành phần liên thông), ngưỡng 10 |
| Beizer | Kiểm thử vòng lặp (khớp slide 37-41) |
| Meszaros, xUnit Test Patterns | Test double: stub, mock, fake, spy, dummy |

## 3. Chênh lệch giữa slide và tài liệu ngoài, lựa chọn đã áp dụng

1. "Pass objects instead of data bits" (06, slide 25) mâu thuẫn bề ngoài với stamp coupling (11, slide 26-31). Lựa chọn: truyền đối tượng khi bên nhận dùng phần lớn dữ liệu hoặc đối tượng là khái niệm trọn vẹn; nếu chỉ dùng một hai trường thì truyền trường (P12 F2 mức hợp lý, X1 F3 mức 4).
2. Kế thừa trong dữ liệu: slide 36-38 chỉ nêu hai phương án (bảng riêng chuẩn hoá; lặp thuộc tính phi chuẩn hoá). Fowler có ba (thêm Single Table). Sản phẩm giữ đủ ba và gọi tên theo Fowler; hai phương án của slide tương ứng Class Table và Concrete Table.
3. Aggregation trong dữ liệu: slide 33 ánh xạ aggregation thành dependency relationship (FK trong PK), slide 34 cho phép map về independency. UML và Fowler không ép aggregation thành identifying. Sản phẩm: aggregation "có thể" phụ thuộc, được phép độc lập khi bộ phận có định danh riêng; composition luôn phụ thuộc + CASCADE.
4. Slide 07 liệt kê mô hình mạng, phân cấp ở mức logic. Sản phẩm chỉ hỗ trợ quan hệ và tài liệu (NoSQL) vì hai mô hình kia gần như không còn dùng cho hệ thống mới; ghi ở đây để đối chiếu.
5. Cohesion: slide 45 liệt kê 6 mức, slide 67 có thêm Sequential. Yourdon và Constantine có 7 mức. Sản phẩm dùng 7 mức.
6. Coupling: slide có 5 mức; Myers có thêm External (và mức no coupling). Sản phẩm dùng 5 mức chính, ghi External là mục bổ sung ngoài thang.
7. Slide 08 không có đồ thị nhân quả (cause-effect graph), không có cyclomatic complexity (chỉ nhắc ở 09 phần smell), không có mock. Sản phẩm: bỏ đồ thị nhân quả; thêm V(G) (McCabe) vì cần để tính số đường đi cơ sở và phát hiện phương thức quá phức tạp; thêm mock/fake (Meszaros) bên cạnh stub/driver của slide.
8. Slide 08 dùng kỹ thuật "Sequence chart coverage" cho kiểm thử tích hợp. X2 là unit test nên không đưa vào; ghi trong mục 5 của X2 là việc của kiểm thử tích hợp.
9. Chuyển trạng thái (state transition testing) không có trong slide 08, lấy từ ISTQB; thêm vì P12 có state machine và giúp kiểm thử guard/BR.
10. Slide 06 mô tả state machine với action "do/" trên trạng thái và "/activity" trên chuyển. UML 2.5.1 gọi hành vi trên chuyển là effect. Sản phẩm dùng "hành động" để khớp cột lõi hợp đồng.
11. Slide 06 dùng khoá tự nhiên trong ví dụ dữ liệu (07 slide 32-40). Sản phẩm mặc định khoá thay thế cho bảng thực thể độc lập và giữ khoá tự nhiên làm UNIQUE (Ambler, Fowler Identity Field), cho phép đổi qua QUY_UOC_CSDL.
12. Slide 16 nói "Only public classes can be referenced outside of the owning package": giữ nguyên trong P12 F9.

## 4. Ngưỡng định lượng và lý do

| Ngưỡng | Ở đâu | Lý do / nguồn |
|---|---|---|
| Khoảng 15-20 operation public, 10-15 thuộc tính | P12 F1 | Heuristic phát hiện god class (Riel; Lanza và Marinescu dùng ngưỡng tương đối theo thống kê). Dùng như tín hiệu kiểm tra lại, không phải luật |
| Từ khoảng 4 tham số trở lên xem xét gom | P12 F2 | Slide 25 "fewer the better"; Fowler "Long Parameter List"; Martin, Clean Code khuyến nghị tối đa 3 |
| 3 đến khoảng 10 trạng thái | P12 F6 | Dưới 3 thường không có hành vi phụ thuộc trạng thái đáng kể (slide 69: không cần cho lớp chỉ có một trạng thái tính toán); trên 10 khó đọc, UML hỗ trợ composite state |
| Khoảng 20-25 lớp mỗi sơ đồ | P12 F8 | Ambler: sơ đồ nên vừa một trang và đọc được; con số là heuristic |
| Khoảng 30 lớp thì chạy theo package | P12 mục 3 | Giới hạn độ dài đầu ra của một lần chạy AI (mỗi lớp nhiều dòng ở bốn bảng) |
| V(G) > 10 | X2 Bước 4.2 | McCabe 1976 |
| D từ khoảng 0,5 | X1 F6.3 | Martin: D là khoảng cách tới main sequence; 0,5 là giữa thang, chỉ để nhận xét |
| Vòng lặp 0, 1, m, n-1, n, n+1 | X2 Bước 4.4 | Slide 08 trang 10; Beizer |

## 5. Chạy thử trong đầu (miền quản lý kho)

Lớp mẫu: Product, Warehouse, StockItem (tồn của mặt hàng tại kho), StockIssue, StockIssueLine, IssueStockController, IssueForm, IErpGateway.

P12, phát hiện và đã sửa:
- (Sau tích hợp) P12 đã khớp nhánh C: đọc P09 mục F3, F5 (mẫu kiến trúc, quy tắc ánh xạ stereotype sang layer) và P10 mục F3 để gán PKG; coi DC do P11b cấp (bên trong subsystem) là lớp cần chi tiết hoá, nguồn ghi "P11b SS-nn"; chuyển "// tênTráchNhiệm" của P07/P08 thành chữ ký đầy đủ; giữ mã R-nn của P08; phân biệt control phân tích với controller MVC.
- Cột Multiplicity viết "1 .. 0..*" gây nhầm với dấu ".." của multiplicity. Đổi thành "A 1 - B 0..*" và định nghĩa rõ đầu nào.
- StockItem là association class giữa Warehouse và Product nhưng P12 chưa hướng dẫn. Thêm quy tắc chuyển association class thành lớp thường, ghi chú "từ association class" để P13 dùng khoá ghép.
- Chạy theo package làm trùng mã quan hệ lớp R-01 và mã ST-01 giữa các file. Thêm quy tắc đánh số liên tục.
- Cạnh class diagram chưa nói Nguồn/Đích tương ứng Lớp A/Lớp B. Đã thêm.
- Không phát hiện mơ hồ ở state machine (StockIssue: Draft, PendingApproval, Confirmed) và ở ánh xạ IF (IErpGateway --> lớp «interface» + adapter).

P13, phát hiện và đã sửa:
- Quy tắc association --> FK ngoài PK mâu thuẫn với ví dụ stock_item có PK ghép (warehouse_id, product_id). Thêm quy tắc cho lớp có định danh do hai lớp cha xác định.
- Không có mặc định chiến lược khoá chính khi QUY_UOC_CSDL trống. Thêm mặc định (surrogate cho thực thể độc lập, khoá ghép cho bộ phận composition và bảng trung gian).
- Tên bảng số ít hay số nhiều chưa chốt. Chốt số ít mặc định.
- Chuẩn hoá phiếu xuất kho: đi đủ 2NF, 3NF, kết quả 4 bảng, đã kiểm tra lại phụ thuộc (issue_no --> warehouse_code dựa trên BR "mỗi phiếu xuất từ một kho"; nếu dự án cho phép phiếu xuất nhiều kho thì FD khác, nên sản phẩm nhấn mạnh FD phải từ BR).

Kiểm tra số liệu ví dụ: biên 0, 1, 50, 51 với tồn 50; 199.999 và 200.000 đồng; huỷ lịch đúng 24 giờ và 23 giờ 59 phút; V(G) = 3 quyết định + 1 = 4, 6 nhánh; bảng quyết định 3 điều kiện = 8 quy tắc. Đều khớp.

## 6. Đề xuất đổi hợp đồng

1. Mã quan hệ lớp: đã thống nhất theo người tích hợp, P12 dùng R-nn nối tiếp dãy mã của P08 (P07 dùng R-UCnnn-nn). Mối quan hệ ER khái niệm ở P13 đổi sang ER-nn để không trùng R-nn; thực thể khái niệm E-<Ten>. Đề nghị bổ sung ER-nn, E-<Ten> vào C3. Mã nội bộ của X2 (EC, BV, DT-R, N<n>, E<n>) chỉ dùng trong file, không cần đưa vào C3.
2. Bảng lõi P12 "Lớp": đề nghị thêm cột lõi "Persistent (Có / Không)" vì P13 bắt buộc cần. Hiện P12 đã có cột này dưới dạng cột thêm.
3. Bảng lõi P12 "Quan hệ": đề nghị quy định định dạng Multiplicity "A <m> - B <m>" và vai trò Lớp A/Lớp B theo loại quan hệ (con/cha, hiện thực/interface, client/supplier, toàn thể/bộ phận) để P13 và X1 đọc máy được.
4. Bảng lõi P12 "Phương thức": cột lõi không có mã; đề nghị ghi rõ trong hợp đồng khoá tham chiếu là DC-<Lop>.<operation> (thêm kiểu tham số khi overload), X2 dùng khoá này ở cột "DC.phương thức".
5. Bảng lõi P12 "State machine": đề nghị thêm cột STT (thứ tự chuyển) để ID cạnh sơ đồ ổn định (<ST>-T<STT>).
6. Bảng lõi X2: cột Kỹ thuật đề nghị mở rộng giá trị hợp lệ thêm "chuyển trạng thái" và "use case" (slide 08 có kiểm thử theo use case).
7. C7.3 chưa có style cho ERD và CFG. Đề nghị thêm vào bảng style: bảng ERD (swimlane stackLayout như Class), cạnh chân chim (startArrow=ERmandOne;endArrow=ERzeroToMany; dashed=1 cho quan hệ độc lập), thực thể yếu Chen (shape=ext;double=1), thuộc tính Chen (ellipse), chuyển trạng thái (endArrow=open;endFill=0).
8. C4: thêm tên file sơ đồ diagrams/P12-state-<DC>.drawio, diagrams/P13-erd-conceptual.drawio, diagrams/X2-cfg-<DC>-<operation>.drawio vào ví dụ C7.2.
9. P07 (nhánh C): để P12 F4 ánh xạ được, cột STT message trong bảng sequence P07 cần duy nhất trong mỗi UC (không đánh lại từ 1 cho mỗi luồng thay thế), hoặc P07 ghi rõ luồng (ví dụ 3a.2).

## 7. Điểm còn băn khoăn

- P12 rất dài với hệ thống vừa; ngưỡng "khoảng 30 lớp" để chuyển sang chạy theo package là ước lượng, cần kiểm chứng khi chạy thật.
- X1 phụ thuộc chất lượng đặc tả method P12 để xác định stamp coupling và cohesion; khi P12 chạy ở chế độ GON, nhiều phát hiện sẽ là "Cần xác nhận".
- P13 chưa hướng dẫn chi tiết về lịch sử/phiên bản dữ liệu (bảng lịch sử, temporal table) và xoá mềm; để cho YEU_CAU_BO_SUNG.
- Không có bước riêng cho sequence diagram mức thiết kế; P12 F4 chỉ ánh xạ message --> operation bằng bảng. Nếu người tích hợp muốn sequence thiết kế đầy đủ, cần thêm một bước hoặc mở rộng P11b/P12.
