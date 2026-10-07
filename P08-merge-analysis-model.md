# P08 - Hợp nhất mô hình phân tích (Unify Analysis Classes)

## 1. Mục đích

Bước này gom lớp phân tích của mọi use case đã phân tích ở P07 thành một mô hình phân tích duy nhất cho toàn hệ thống: phát hiện và giải quyết trùng lặp (cùng khái niệm khác tên, cùng tên khác khái niệm), gộp trách nhiệm, xác định quan hệ giữa các lớp (association, aggregation, composition, generalization, multiplicity) và vẽ analysis class diagram tổng thể. Kết quả là đầu vào chính của thiết kế kiến trúc (P09), ánh xạ phần tử thiết kế (P10) và thiết kế lớp (P12).

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md, 00-Conventions.md | Có | Luật chung, chế độ giả định |
| Đầu vào | P07-uc-analysis/*.md (mọi use case trong phạm vi) | Có | Bảng lớp phân tích, bảng quan hệ VOPC, sequence của từng use case |
| Đầu vào | P02-usecases.md | Có | Danh sách use case trong phạm vi, để phát hiện use case chưa phân tích |
| Đầu vào | P05-glossary.md | Nên có | Phân định đồng nghĩa và đồng âm |
| Đầu vào | P06-supplementary-spec.md | Nên có | BR làm căn cứ multiplicity, composition, generalization |
| Đầu vào | P01-actors.md | Có | Boundary gắn với tác nhân nào |
| Đầu vào | P04-uc-specs/ | Không | Tra lại câu gốc khi cần bằng chứng cho quan hệ |
| Đầu ra | P08-analysis-model.md | Có | Mô hình phân tích hợp nhất |
| Đầu ra | diagrams/P08-class-analysis.drawio | Có | Analysis class diagram tổng thể và các view |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md và các file đầu vào ở bảng trên.
- Chạy một lần cho toàn hệ thống, sau khi mọi use case trong phạm vi đã có artifact P07. Khi thêm use case mới, chạy lại bước này với phiên bản tăng lên.
- Chưa có P05 hoặc P06 vẫn chạy được. Hệ quả: phép thử đồng nghĩa, đồng âm chỉ dựa vào P04 và tài liệu nguồn, nên các cặp lớp không chứng minh được là một khái niệm vẫn được giữ tách và có Q-nn; căn cứ multiplicity, composition lấy từ sổ BR của P04. Chạy lại P08 sau khi có P05, P06.
- Hệ thống lớn (trên khoảng 30 lớp phân tích): vẫn chạy một lần, nhưng sơ đồ được tách thành nhiều view theo quy tắc ở mục F5.

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| CACH_CHIA_VIEW | Tuỳ chọn | Cách chia sơ đồ tổng thể thành các view khi hệ thống lớn |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được hồ sơ dự án (project-profile.md), bộ quy ước chung (00-Conventions.md) và các artifact đã chốt: P01-actors.md, P02-usecases.md, P05-glossary.md, P06-supplementary-spec.md, toàn bộ P07-uc-analysis/*.md và (nếu có) P04-uc-specs/. Tuân thủ 00-Conventions.md, đặc biệt C1, C3, C5, C7.
Phạm vi: toàn hệ thống, mọi use case có trong P02-usecases.md và nằm trong phạm vi của dự án.

Cách chia view cho sơ đồ tổng thể:
{{PH:CACH_CHIA_VIEW | Hướng dẫn: [TUỲ CHỌN] khi hệ thống có nhiều lớp, nêu cách chia sơ đồ; ghi "Không có" thì áp dụng quy tắc mặc định ở F5 | Ví dụ: "Một view entity toàn hệ thống, một view cho mỗi nhóm chức năng trong P02" (quản lý kho); "Một view cho phân hệ đặt lịch, một view cho phân hệ quản trị" (phòng khám)}}

[Role]
Bạn là chuyên gia phân tích hướng đối tượng, thành thạo hợp nhất lớp phân tích (unify analysis classes), mô hình miền (domain model) và ngữ nghĩa quan hệ lớp của UML 2.5.1. Bạn thận trọng: chỉ gộp khi chứng minh được hai lớp là một khái niệm, chỉ thêm quan hệ khi có bằng chứng.

[Action]
A1. Kiểm tra độ phủ.
- Đối chiếu P02 với các file P07: liệt kê use case trong phạm vi chưa có artifact P07. Nếu có, ghi vào "Vấn đề còn mở" và vẫn hợp nhất phần đã có.

A2. Tập hợp.
- Gom mọi dòng của bảng lớp phân tích (F3.4 của P07) và mọi dòng của bảng quan hệ VOPC từ mọi file P07 thành danh sách thô, giữ nguyên use case nguồn.

A3. Phát hiện trùng lặp và xung đột. Xét từng cặp lớp cùng stereotype (và cặp khác stereotype nhưng tên gần nhau):
- Cùng khái niệm, khác tên (đồng nghĩa): hai lớp mô tả cùng một thứ trong miền nghiệp vụ. Phép thử: cùng định nghĩa trong glossary, hoặc một thuật ngữ là "từ đồng nghĩa không dùng" của thuật ngữ kia; cùng tập thuộc tính định danh; một đối tượng của lớp này luôn là một đối tượng của lớp kia. Kết luận: gộp vào lớp có tên theo glossary; lớp bị gộp giữ mã và ghi trạng thái "Gộp vào AC-...". Khi chưa có P05, phép thử dùng định nghĩa và câu dùng từ trong P04 và tài liệu nguồn; không chứng minh được là một khái niệm thì giữ hai lớp và tạo Q-nn hỏi hai thuật ngữ có cùng nghĩa không.
- Cùng tên, khác khái niệm (đồng âm): hai lớp cùng tên nhưng khác định nghĩa, khác vòng đời hoặc khác tập thuộc tính định danh. Kết luận: tách, đổi tên ít nhất một lớp cho rõ nghĩa; lớp giữ mã cũ là lớp đúng với glossary, lớp kia nhận mã mới và ghi mã cũ trong nhật ký.
- Cùng khái niệm, cùng tên nhưng khác mã (do P07 chạy thiếu sổ đăng ký): gộp về mã cấp sớm nhất.
- Boundary giao diện hệ thống hoặc thiết bị cho cùng một hệ thống ngoài: gộp thành một boundary, hợp các trách nhiệm.
- Boundary giao diện người dùng của các use case khác nhau: mặc định không gộp (mỗi cặp tác nhân - use case một boundary). Chỉ gộp khi hai use case luôn được thực hiện trên cùng một tương tác và glossary coi là một; ghi lý do.
- Control của các use case khác nhau: không gộp, trừ khi hai use case là một (khi đó đề xuất sửa P02, không tự gộp use case).
- Lớp có nguy cơ là thuộc tính trá hình hoặc cấu trúc cài đặt (ví dụ Address, PhoneNumber, ItemList) còn sót từ P07: ghi đề xuất sửa P07 và hạ thành thuộc tính trong mô hình hợp nhất, nêu rõ.

A4. Gộp trách nhiệm và thuộc tính.
- Với mỗi lớp hợp nhất, hợp các trách nhiệm từ mọi use case. Hai trách nhiệm cùng ý nghĩa, khác tên thì giữ một tên, ghi tên bị thay trong nhật ký. Hai trách nhiệm cùng tên, khác ý nghĩa thì đổi tên cho phân biệt.
- Hợp thuộc tính, loại trùng. Thuộc tính mâu thuẫn (ví dụ một use case coi "status" có 3 giá trị, use case khác có 4) thì ghi câu hỏi mở hoặc giả định.
- Kiểm tra lại độ cân bằng: control trên 15 trách nhiệm (sau gộp chỉ còn trách nhiệm của các use case nó điều phối) hoặc entity không có trách nhiệm hành vi nào thì ghi vào "Vấn đề còn mở" kèm đề xuất.

A5. Xác định quan hệ.
- Bắt đầu từ các quan hệ trong bảng VOPC của P07. Hợp quan hệ trùng (cùng cặp lớp, cùng ý nghĩa).
- Được thêm quan hệ giữa hai entity không có trong VOPC nào khi glossary, BR hoặc tài liệu nguồn cho bằng chứng (ví dụ glossary định nghĩa "ngăn kệ thuộc một dãy kệ"); cột Ghi chú ghi "Mới ở P08". Không thêm quan hệ chỉ vì hiểu biết chung.
- Với mỗi quan hệ giữa hai entity, chọn loại theo cây quyết định ở F3, dựa trên bằng chứng từ đặc tả, BR, glossary. Không có bằng chứng thì giữ association.
- Xác định multiplicity hai đầu từ BR, glossary, dữ liệu vào ra. Không có căn cứ thì để trống và ghi câu hỏi (NGHIEM_NGAT) hoặc giả định (CO_NHAN).
- Xác định generalization khi hai hay nhiều entity có chung thuộc tính và trách nhiệm, và glossary hoặc đặc tả nói rõ quan hệ "là một loại của".
- Quan hệ giữa boundary và control, control và entity giữ ở dạng association tạm (ghi chú "tạm thời"), chỉ để thể hiện ai dùng ai; không gán aggregation, composition cho các quan hệ này.

A6. Vẽ analysis class diagram tổng thể và các view (F5).

A7. Rà soát theo các điểm kiểm tra lớp phân tích (F6) và [Target]. Sửa, rồi mới xuất.

[Format]
Xuất file P08-analysis-model.md theo khung C5, tiêu đề "# P08 - Mô hình phân tích hợp nhất - <Tên hệ thống>". Nội dung chính gồm:

F1. Độ phủ use case
Bảng: | UC | Tên | File P07 | Trạng thái (Đã phân tích / Chưa phân tích) |

F2. Nhật ký hợp nhất
Bảng: | STT | Lớp gốc (AC, tên) | UC nguồn | Tình huống (Đồng nghĩa / Đồng âm / Trùng mã / Boundary hệ thống trùng / Thuộc tính trá hình / Giữ nguyên) | Kết quả (Gộp vào AC-... / Tách, đổi tên thành ... / Hạ thành thuộc tính của AC-... / Giữ) | Bằng chứng (GL, BR, bước UC) |
- Định nghĩa: bản ghi mọi quyết định gộp, tách, đổi tên để người đọc truy ngược từ mô hình hợp nhất về P07.
- Quy tắc: mọi lớp của mọi P07 xuất hiện đúng một lần ở cột "Lớp gốc". Lớp không thay đổi ghi "Giữ nguyên".
- Lỗi thường gặp: gộp hai lớp chỉ vì tên giống (bỏ qua đồng âm); gộp các boundary giao diện người dùng của nhiều use case thành một "MainForm" (quá lớn); không ghi bằng chứng.
- Ví dụ đúng (khách sạn): AC-E-Reservation (UC-003) và AC-E-Booking (UC-005) --> Gộp vào AC-E-Booking, bằng chứng GL-04 ghi "Đặt phòng (Booking); từ không dùng: reservation".
- Ví dụ đúng (thư viện, đồng âm): Copy trong UC-002 là "bản sách vật lý", Copy trong UC-009 là "bản sao chụp tài liệu" --> Tách: giữ AC-E-Copy cho bản sách (theo GL-03), đổi lớp kia thành PhotocopyRequest (mã mới).
- Ví dụ sai: gộp Order (đơn đặt món) và Order (thứ tự sắp xếp danh sách) vì cùng tên (sai: đồng âm).

F3. Bảng lớp hợp nhất (bảng lõi, P09, P10, P12 đọc bảng này)
| AC | Stereotype | Tên | Trách nhiệm (gộp) | Thuộc tính | Dùng trong UC | Loại boundary | Trạng thái (Hoạt động / Gộp vào AC-... / Tạm (chờ P07 của UC-nnn)) |
- Trách nhiệm: dạng "// tênTráchNhiệm: mô tả", mỗi dòng một trách nhiệm, sau mỗi trách nhiệm ghi UC nguồn trong ngoặc, ví dụ "// calculateTotal: tính tổng tiền (UC-012, UC-015)".
- Thuộc tính: tên lowerCamelCase, kiểu khái niệm nếu có; không kiểu vật lý.
- Lớp bị gộp vẫn có dòng, cột Trạng thái ghi "Gộp vào AC-...", các cột khác để "-". Mã không bị xoá hay tái sử dụng (C3).
- Lớp mà P07 đặt trước mã cho use case chưa phân tích (trạng thái "Tạm - chờ P07 của UC-nnn") ghi "Tạm (chờ P07 của UC-nnn)"; trách nhiệm chỉ gồm những gì use case gọi nó cần. Khi P07 của UC-nnn có, chạy lại P08 để chuyển sang "Hoạt động".
Mức hợp lý: mỗi lớp hoạt động có ít nhất một trách nhiệm và ít nhất một UC; tên mỗi lớp là một khái niệm duy nhất (phép thử: viết được định nghĩa một câu không dùng chữ "và").

F4. Bảng quan hệ (bảng lõi)
| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn UC | Bằng chứng | Ghi chú |
- ID dạng R-nn (cấp mới cho toàn hệ thống); cột Ghi chú ghi ID gốc R-UCnnn-nn từ P07 đã hợp vào, hoặc "Mới ở P08" khi quan hệ không có trong VOPC (A5).
- Loại: Association, Aggregation, Composition, Generalization, Dependency.
- Multiplicity: ghi dạng "A <m> - B <m>", ví dụ "A 1 - B 0..*". Được để trống khi chưa có căn cứ, kèm mã Q hoặc ASM.
- Vai trò: tên vai trò ở một hoặc hai đầu khi cần phân biệt (ví dụ hai association giữa Staff và Shift: "assignedStaff", "supervisor").
Cây quyết định loại quan hệ giữa hai entity:
1. B "là một loại" A, mọi thuộc tính và trách nhiệm của A đúng với B --> Generalization (B kế thừa A). Phép thử: câu "Mọi B đều là A" đúng theo glossary.
2. B là một phần của A, B không tồn tại khi không có A, B chỉ thuộc về một A tại một thời điểm, xoá A thì xoá B --> Composition (thoi đặc ở A). Phép thử: đặc tả hoặc BR có câu về vòng đời phụ thuộc.
3. B là một phần của A về mặt khái niệm nhưng tồn tại độc lập hoặc dùng chung được --> Aggregation (thoi rỗng ở A).
4. A và B có liên kết cấu trúc lâu dài, không có quan hệ toàn thể - bộ phận --> Association.
5. A chỉ dùng B tạm thời (tham số, kết quả) --> Dependency.
Lỗi thường gặp: dùng composition cho mọi quan hệ "có" (quá lớn); dùng generalization vì có chung một thuộc tính (nhầm với association hoặc thuộc tính); multiplicity đoán theo hiểu biết chung (vi phạm C1); quan hệ vòng thừa (A-B, B-C, A-C) khi A-C suy được từ đường A-B-C mà không có ý nghĩa riêng.
Ví dụ đúng (giao đồ ăn): FoodOrder --> OrderLine: Composition, A 1 - B 1..* (FoodOrder 1 - OrderLine 1..*), bằng chứng BR-06 "dòng món bị huỷ cùng đơn". Restaurant --> Dish: Aggregation hoặc Association tuỳ glossary; nếu món bị xoá khi nhà hàng ngừng hợp tác theo BR thì Composition.
Ví dụ đúng (phòng khám): Appointment --> Patient: Association, A 0..* - B 1 (Appointment 0..* - Patient 1).
Ví dụ sai (quản lý kho): Warehouse <|-- Product (Product kế thừa Warehouse vì cùng có "code") (sai: không có quan hệ "là một loại").

F5. Analysis class diagram tổng thể
File diagrams/P08-class-analysis.drawio, mỗi view một trang.
a) Bảng Node: | ID (mã AC) | Loại (Class) | Nhãn | Stereotype | Thuộc về (view) | Ngăn thuộc tính | Ngăn trách nhiệm |
b) Bảng Edge: dùng ID của F4, cột: | ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Thuộc về (view) |
Quy tắc chia view (mặc định, khi CACH_CHIA_VIEW trống):
- Trang tổng thể mặc định là trang "Entity": mọi entity và quan hệ giữa chúng (mô hình miền), không có boundary, control.
- Boundary, control và association tạm của chúng chỉ vẽ ở trang theo nhóm chức năng trong P02: mỗi nhóm một trang chứa boundary, control của nhóm và các entity chúng dùng. Hệ thống nhỏ có thể gộp mọi nhóm vào một trang khi không vượt ngưỡng dưới đây.
- Ngưỡng tách trang: một trang quá khoảng 20 lớp hoặc quá khoảng 25 cạnh thì tách tiếp (theo nhóm chức năng con, hoặc tách trang Entity theo cụm entity liên quan chặt). Ngưỡng tính cả cạnh vì association tạm giữa control và các lớp khác thường gấp đôi số lớp.
- Một lớp xuất hiện ở nhiều trang thì cùng ID gốc, thêm hậu tố trang cho mxCell (ví dụ AC-E-Order__V2).
Quy tắc ngữ nghĩa UML:
- Stereotype «boundary», «control», «entity» ghi ở ngăn tên; ngăn trách nhiệm ghi "// tênTráchNhiệm"; không ghi visibility, kiểu vật lý.
- Multiplicity ghi ở đầu quan hệ phía lớp mà nó đếm, là hai nhãn con ở hai đầu cạnh theo C7.3, không ghi chuỗi "A m - B n" giữa cạnh. Thoi aggregation, composition đặt phía lớp toàn thể. Tam giác generalization chỉ về lớp cha.
- Không vẽ quan hệ giữa hai boundary; không vẽ quan hệ từ entity tới boundary hoặc control.
Bố cục: boundary hàng trên, control hàng giữa, entity hàng dưới (trang theo nhóm chức năng); trang Entity bố trí lớp trung tâm (nhiều quan hệ nhất) ở giữa, lớp cha trên lớp con; edgeStyle=orthogonalEdgeStyle; theo C7.3.
Chạy bằng agent thì ghi file; chạy bằng chat thì in nội dung XML trong khối code riêng.

F6. Rà soát lớp phân tích
Bảng: | AC | Tên phản ánh đúng vai trò | Một khái niệm duy nhất | Trách nhiệm gắn kết | Cung cấp đủ hành vi cần | Yêu cầu đặc thù (BR, NFR) đã gắn | Ghi chú |
Mỗi ô ghi Đạt hoặc Không đạt kèm lý do ngắn. Lớp có trạng thái Tạm ghi "-" ở cột Cung cấp đủ hành vi cần. Lớp có ô Không đạt phải có hành động trong "Vấn đề còn mở" hoặc "Đề xuất sửa artifact trước".

F7. Mục kiểm soát theo C5.

[Target]
1. Mọi use case trong phạm vi có artifact P07, hoặc được liệt kê là chưa phân tích.
2. Mọi lớp của mọi P07 xuất hiện trong nhật ký hợp nhất với kết quả và bằng chứng.
3. Không còn hai lớp hoạt động biểu diễn cùng một khái niệm; không còn một lớp biểu diễn hai khái niệm.
4. Không mã AC nào bị xoá, đổi nghĩa hoặc tái sử dụng; lớp bị gộp có trạng thái "Gộp vào".
5. Mọi quan hệ trong VOPC của P07 có mặt trong bảng quan hệ hợp nhất (đã hợp hoặc giữ nguyên).
6. Mọi aggregation, composition, generalization và multiplicity có bằng chứng hoặc mã Q, ASM.
7. Không có quan hệ vi phạm quy tắc tương tác (boundary-boundary, entity tới boundary hoặc control).
8. Mỗi lớp hoạt động có ít nhất một trách nhiệm và ít nhất một use case.
9. Trang tổng thể là trang Entity; mỗi trang sơ đồ không quá khoảng 20 lớp và 25 cạnh; bảng mô hình và file .drawio khớp nhau và đạt C7.3.
10. Không có chi tiết công nghệ; đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này | Ví dụ: "Không vẽ boundary, control trong sơ đồ tổng thể, chỉ vẽ entity."; "Gộp mọi boundary giao diện người dùng của cùng một tác nhân thành một lớp theo quy chuẩn tổ chức."}}
````

## 5. Ghi chú cho người dùng

- Nhật ký hợp nhất dài là bình thường; đừng yêu cầu AI rút gọn, vì P10 và X1 cần truy ngược từ lớp thiết kế về use case.
- Nếu AI gộp quá nhiều boundary thành một, kiểm tra lại YEU_CAU_BO_SUNG; mặc định mỗi cặp tác nhân - use case một boundary.
- Khi nhiều multiplicity bị để trống, đó là tín hiệu đặc tả thiếu quy tắc về số lượng. Trả lời câu hỏi mở rồi chạy lại, hoặc chuyển chế độ CO_NHAN nếu dự án chấp nhận giả định.
- Dùng độc lập: có thể chạy với các bảng lớp phân tích do người dùng tự lập, miễn là mỗi bảng có đủ cột lõi của P07 (AC, Stereotype, Tên, Trách nhiệm, Thuộc tính chính, Bước UC nguồn) và bảng quan hệ.

## 6. Căn cứ

- Kruchten P., The Rational Unified Process: An Introduction, 3rd ed. (2003): hợp nhất lớp phân tích sau Use-Case Analysis.
- Larman C., Applying UML and Patterns, 3rd ed. (2004): mô hình miền, association, multiplicity, generalization (phép thử "is-a" và quy tắc 100%).
- OMG, Unified Modeling Language 2.5.1 (2017): ngữ nghĩa association, aggregation, composition, generalization, multiplicity.
- Fowler M., UML Distilled, 3rd ed. (2003): khi nào dùng aggregation và composition.
- Evans E., Domain-Driven Design (2003): ngôn ngữ chung (ubiquitous language), phân biệt đồng nghĩa và đồng âm giữa các ngữ cảnh.
- Ambler S., The Elements of UML 2.0 Style (2005): chia sơ đồ lớn thành view, bố cục sơ đồ lớp.
