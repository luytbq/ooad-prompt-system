Model của phiên chạy: Sonnet

# Nhật ký người chạy P10 - lần chạy đầu - dự án gym (VietFit)

Đầu ra: design/P10-design-elements.md, design/diagrams/P10-package-design.drawio, design/diagrams/P10-subsystem-context.drawio (7 trang). Cả hai file .drawio qua kiểm tra XML bằng xml.dom.minidom. Q lớn nhất sau lần chạy: Q-94 (P10 không cấp Q mới). ASM: chưa cấp. Số phần tử: 7 subsystem (SS-01 đến SS-07), 15 interface (IF-01 đến IF-15), 35 lớp thiết kế (DC), 28 dòng package ở F4 (PKG-05 đến PKG-32, trong đó 8 giữ chỗ, PKG-32 cấp mới), 35 phụ thuộc package ở F6, diagram package 54 node và 49 cạnh, diagram context 28 node và 24 cạnh.

Không đạt Target: không có mục nào bị đánh dấu không đạt. Riêng Target 9 (đạt C7.3) chỉ được kiểm bằng script tự viết (không cắt qua node, toạ độ bội số 10, khoảng cách giữa hai node tối thiểu 40, không chồng lấn, không đoạn cạnh trùng nhau); chưa mở bằng draw.io nên chưa kiểm được nhãn tràn khung hay hình dạng thực tế.

## Vướng mắc

### 1. Hai nguồn chỉ dẫn lệch nhau về phần cần đọc của P09 (mục 3 và A0)
- Vị trí: mục 3, bảng "Phần cần dùng", dòng P09: "F4, F5, F6, F7, Câu hỏi mở, Giả định". A0: "Đối chiếu mẫu kiến trúc và mẫu cho phía giao diện ở P09 mục F3" và "dùng công nghệ ở P09 mục F11".
- Gặp gì: bảng không liệt kê F3, F11 nhưng A0 và F2 (Persistence, bảng tham chiếu "P09 A5") buộc phải đọc F3, F11. Lập luận chuyển hành vi của AC-E-Member lại dựa vào P09 F8 ("P10 chuyển các hành vi này sang package phía trên"), cũng không có trong bảng. P09 F5 và F6 dẫn tới F8 theo cách gián tiếp.
- Xử lý: đọc thêm F3, F8, F11 của P09. Đề nghị thêm F3, F8, F11 vào bảng "Phần cần dùng".

### 2. A0: Q-nn dưới khối F11 "coi là đã trả lời theo ASM tương ứng" trong chế độ NGHIEM_NGAT
- Vị trí: A0, câu "các Q-nn liệt kê dưới khối F11 coi là đã trả lời theo ASM tương ứng, ghi một dòng ở Vấn đề còn mở 'Q-nn (danh sách) đóng theo hồ sơ đã cập nhật sau P09'".
- Gặp gì: dự án NGHIEM_NGAT, không có ASM nào; câu "theo ASM tương ứng" không có đối tượng. Khối F11 liệt kê Q-76 và Q-94. Q-94 là câu hỏi về năng lực đội và ràng buộc công nghệ nên đóng theo hồ sơ hợp lý. Q-76 trong P06 NFR-01, NFR-02 là "Cách tính và mức tải" của phép đo hiệu năng, một câu hỏi về yêu cầu phi chức năng, không chỉ là chọn công nghệ. Đóng Q-76 theo hồ sơ có thể làm mất một câu hỏi NFR còn thật sự mở.
- Xử lý: ghi dòng "Q-76, Q-94 đóng theo hồ sơ đã cập nhật sau P09" như A0 yêu cầu và không dẫn hai mã làm câu hỏi mở. Đề nghị prompt nói rõ: khi hồ sơ NGHIEM_NGAT chấp nhận F11 thì việc đóng chỉ áp dụng cho phần chọn công nghệ, và P09 F11 nên chỉ liệt kê Q mà quyết định công nghệ thật sự phụ thuộc.

### 3. Xung đột A1 (thiết bị thành subsystem) với P09 F5 (cửa quay là điểm vào ở PKG-12) và Target 4 cho thiết bị gọi vào
- Vị trí: A1, "là boundary giao diện thiết bị"; F1, "mọi boundary giao diện hệ thống ngoài và thiết bị đều thành subsystem, trừ khi có lý do ghi rõ"; Target 4, "subsystem thiết bị chỉ đẩy sự kiện vào thì interface hiện thực gồm việc bật, tắt và đăng ký bộ nhận, còn sự kiện đi qua interface gọi ngược". P09 F5: "Thiết bị gọi vào phần mềm (cửa quay ACT-12), nên phần tiếp nhận là điểm vào API, không phải subsystem gọi ra".
- Gặp gì: KHA_NANG_THAY_DOI_GIAO_DIEN nói giao thức cửa quay ổn định, nên tiêu chí "Có thể thay thế" không thoả, chỉ còn tiêu chí "Thiết bị". Cửa quay gọi vào máy chủ qua REST, phần mềm không có bước bật, tắt, đăng ký bộ nhận trên thiết bị. Sự kiện đi từ PKG-12 (Presentation) xuống PKG-16 (Application) là phụ thuộc đã đi xuống nên không cần đảo phụ thuộc. Bảng Interface gọi ngược lại yêu cầu "mỗi boundary thiết bị ... chỉ đẩy sự kiện vào hệ thống có ít nhất một dòng".
- Xử lý: chọn SS-05 TurnstileAccess đặt trong PKG-12 (giữ đúng PKG của P09), IF-05 ITurnstileEndpoint có // enableReceiving, // disableReceiving, // registerScanReceiver, và IF-09 IEntryScanReceiver (định nghĩa ở PKG-16) làm interface gọi ngược. Bước khởi động tiến trình API là bên gọi IF-05, nằm ngoài mọi package của mô hình nên IF-05 không có cạnh phụ thuộc tới. Phần tử "bật, tắt, đăng ký" mang tính hình thức với thiết bị gọi vào. Ghi quyết định vào Vấn đề còn mở theo C9. Đề nghị prompt tách hai loại thiết bị: thiết bị phần mềm gọi ra hoặc nối trực tiếp (áp dụng Target 4) và thiết bị gọi vào qua API (chỉ cần interface tiếp nhận và interface gọi ngược).

### 4. P09 V4 chỉ nêu hai chỗ gọi ngược nhưng bảng Interface gọi ngược đòi mọi nguồn đẩy sự kiện
- Vị trí: F2, "Mỗi chỗ P09 ghi cơ chế gọi ngược và mỗi boundary thiết bị hoặc hệ thống ngoài chỉ đẩy sự kiện vào hệ thống có ít nhất một dòng".
- Gặp gì: P09 V4 chỉ có mốc hẹn (PKG-22) và kho dữ liệu (PKG-26 đến PKG-31). Cổng thanh toán trả kết quả (AC-B-PaymentGateway // returnPaymentResult) và cửa quay đẩy lượt quét là hai nguồn sự kiện không nằm trong V4. Cổng thanh toán còn có Q-45 (cổng gửi về hay phần mềm tra cứu) chưa trả lời.
- Xử lý: thêm IF-08 IPaymentResultReceiver (PKG-23) và IF-09 (PKG-16), giấu cách nhận kết quả (Q-45) trong SS-01 để không phụ thuộc câu trả lời. Ghi Đề xuất sửa P09 (bổ sung V4). Không rõ cột "Subsystem gọi" của dòng kho dữ liệu ghi gì khi không có subsystem; ghi "- (lớp Application gọi)".

### 5. Điều kiện xét package hạ tầng không có lớp phân tích nguồn (A1) mơ hồ với PKG-21 Security
- Vị trí: A1, "Package tích hợp, hạ tầng của P09 không có lớp phân tích nguồn ... cũng được xét khi ít nhất một use case nó phục vụ đã có P07".
- Gặp gì: cột Nguồn của PKG-21 trong P09 F4 chỉ ghi UC-004, UC-025 (chưa có P07). Nhưng P09 F6 cho PKG-10, PKG-11, PKG-12 phụ thuộc PKG-21, mà các package này phục vụ UC-005, UC-010, UC-018 đã có P07. Đọc theo cột Nguồn thì PKG-21 giữ chỗ; đọc theo phụ thuộc thì được xét. Nếu giữ chỗ thì ba cạnh PKG-10, PKG-11, PKG-12 --> PKG-21 của P09 không suy ra được từ phần tử nào.
- Xử lý: đọc theo phụ thuộc, tạo SS-07 Authentication với IF-07 IAuthenticator, trách nhiệm lấy từ P09 và đánh dấu tạm. Đề nghị A1 nêu rõ "phục vụ" tính theo cột Nguồn hay theo package phụ thuộc vào nó.

### 6. Phần tiếp nhận yêu cầu: A3 nói Application, P09 đặt ở Presentation
- Vị trí: A3, "phần tiếp nhận yêu cầu ở layer Application nhóm theo nhóm chức năng"; A2, "một boundary người dùng trở thành nhiều vai trò (ví dụ View và Presenter trong MVP, View và Controller trong MVC)". P09 F5: Boundary giao diện người dùng gồm View, store (Flux) ở client và REST controller ở PKG-10, PKG-11 (layer Presentation phía máy chủ).
- Gặp gì: prompt giả định phần tiếp nhận yêu cầu ở Application; P09 chọn REST controller ở Presentation, nhóm theo loại client (PKG-10 di động, PKG-11 web, PKG-12 thiết bị). Mẫu Flux cho client có vai trò Store mà A2 không nêu. Không rõ quy tắc tác nhân có áp dụng cho REST controller không.
- Xử lý: theo P09; coi REST controller là "phần tiếp nhận yêu cầu" không áp dụng quy tắc tác nhân (nhóm theo loại client), quy tắc tác nhân chỉ áp dụng cho View, Store ở PKG-05, PKG-07. Mỗi boundary người dùng tách ba phần tử View, Store, Controller (9 DC cho 3 boundary). Ghi vào Vấn đề còn mở.

### 7. Kiểu giá trị dùng chung (A3) chưa có hướng dẫn chọn kiểu và truy vết
- Vị trí: A3, "Kiểu giá trị (tiền, định danh, mã tham chiếu) được interface ở layer dưới dùng trong chữ ký: đặt ở package cùng layer với interface hoặc thấp hơn". Format F3: "thêm lớp thiết kế không truy được về lớp phân tích hay cơ chế kiến trúc (lớp mồ côi)".
- Gặp gì: P09 ghi PKG-23, PKG-24, PKG-25 không phụ thuộc package nào, trong khi chữ ký interface chưa biết (P11b). P10 phải quyết định có tạo package kiểu giá trị không khi chưa thấy chữ ký. Kiểu "định danh" không có thuộc tính nào trong P08 để truy vết; "Số tiền" có (amountDue, amount, price); "số điện thoại" truy được tới nguồn Mục 1 và Mục 10.
- Xử lý: tạo PKG-32 ValueTypes ở Domain với DC-Money, DC-PhoneNumber, DC-TransactionReference; ghi nguồn truy vết ở bảng cơ chế; không tạo kiểu định danh; ghi Đề xuất sửa P09. Cảnh báo rủi ro đoán trước chữ ký interface (P11b mới chốt). Đề nghị prompt nói giá trị nào bắt buộc ở P10 và giá trị nào để P11b bổ sung.

### 8. Ánh xạ tách một lớp ra nhiều package và 1-1 có nhận thêm trách nhiệm
- Vị trí: F3, "Lý do: bắt buộc khi kết quả khác 1-1; với 1-1 ghi 'Lớp đơn giản, một trừu tượng'". Cột PKG của F3 và A2, "Tách thành nhiều lớp khi: ... entity cần tách phần hành vi nghiệp vụ và phần lưu trữ theo layer của P09".
- Gặp gì: AC-E-Member có 7 trách nhiệm thuộc 4 ngữ cảnh, 4 trách nhiệm hỏi dữ liệu ở package khác mà Domain không cho phụ thuộc ngược (P09 F8). Phải tách thành ba DC ở ba package (PKG-26, PKG-27, PKG-29), một trách nhiệm (recordEntryScan) hợp vào DC-EntryScan. Bảng F3 không có chỗ diễn đạt "một trách nhiệm chuyển sang lớp 1-1 khác"; câu cố định "Lớp đơn giản, một trừu tượng" không đúng với control có 9 trách nhiệm (AC-C-PurchaseOrRenewPackageHandler). Prompt chỉ mô tả tách theo layer (hành vi và lưu trữ), không nói tách theo hướng phụ thuộc giữa package.
- Xử lý: cột PKG ghi nhiều giá trị cách nhau bằng <br>; cột Lý do của AC-E-EntryScan ghi thêm phần nhận trách nhiệm; giữ câu cố định cho 1-1 để máy đọc được. Ghi Đề xuất sửa P08. Đề nghị prompt cho phép cột Lý do 1-1 có phần bổ sung và nêu quy tắc tách entity theo hướng phụ thuộc package.

### 9. Phụ thuộc package: kế thừa từ P09 hay chỉ suy từ phần tử đã có
- Vị trí: A5, "Suy phụ thuộc package từ quan hệ giữa các lớp thiết kế (kế thừa từ quan hệ ở P08 và từ luồng message ở P07)"; F4, "tiếp nối bảng của P09".
- Gặp gì: P09 F4 có nhiều cạnh phụ thuộc dựa vào use case chưa có P07 (ví dụ PKG-14 --> PKG-24 cho UC-008 và Q-53, PKG-16 --> PKG-25 cho UC-017, mọi cạnh của PKG-13, PKG-17, PKG-18, PKG-19). Nếu chỉ suy từ lớp đã có thì F4 của P10 có cột "Phụ thuộc" ít hơn P09, dễ bị đọc là mâu thuẫn. Prompt không nói giữ hay bỏ.
- Xử lý: chỉ suy từ phần tử đã có (35 phụ thuộc ở F6); package giữ chỗ ghi "(theo P09: ...)" ở F4; liệt kê cạnh bị bỏ trong Vấn đề còn mở.

### 10. Sơ đồ package lớn và yêu cầu C7.3 khó thoả đồng thời
- Vị trí: C7.1 (điểm uốn, làn y cách nhau 10, khoảng cách hai hàng tối thiểu 40 + 10 x số cạnh); C7.3 ("toạ độ là bội số của 10; không có hai node chồng lên nhau; cạnh không cắt qua node ... khoảng cách tối thiểu giữa hai node là 40"); F7, "Class chỉ vẽ cho lớp hiện thực interface gọi ngược".
- Gặp gì: 54 node, 49 cạnh, nhiều cạnh vượt layer. Không thể tính tay; phải viết script sinh sơ đồ có định tuyến theo làn và hành lang dọc. Phải chọn chiều cao node 50 cho cả interface, subsystem, class để căn tâm trên cùng hàng với toạ độ bội số 10 (cạnh realization ngang). Khoảng cách 40 áp dụng cả cho node con trong package nên package rộng tới 900. Mỗi cổng ra, vào dùng một x riêng trên toàn sơ đồ để tránh cạnh trùng nhau. C7.3 không có style riêng cho interface canonical nên dùng style Class (swimlane) với nhãn «interface». Sơ đồ tối giản chỉ vẽ phần tử là subsystem, interface hoặc lớp hiện thực gọi ngược; bảng F4 liệt kê mọi DC nên bảng F7 không khớp F4 về số phần tử (khớp F7 với file .drawio thì đạt).
- Xử lý: sinh bảng Node, Edge và file .drawio cùng từ một mô hình trong script, kiểm tra tự động; không mở draw.io. Ghi chú ở đầu F7 rằng sơ đồ chỉ vẽ các phần tử nêu trên. Đề nghị prompt cho phép sơ đồ package ở cấp package với interface, không buộc vẽ node Class.

### 11. F8 và F7 cùng "bảng Node, Edge như F7" nhưng thiếu chỗ ghi trách nhiệm interface
- Vị trí: F8, "interface (canonical, chưa cần operation chi tiết, có thể ghi trách nhiệm dạng '// ...')"; "Bảng Node và Edge như F7".
- Gặp gì: bảng Node của F7 không có cột trách nhiệm; interface trong F8 cần ghi trách nhiệm dạng "// ..." trong ngăn. Một lớp có mặt ở nhiều trang (DC-PurchaseOrRenewPackageHandler ở ba trang) và IF-05 không có lớp nào dùng.
- Xử lý: ghi trách nhiệm vào cột Ghi chú của bảng Node và vào ngăn của interface trong .drawio; mỗi trang có bảng riêng, ID cạnh theo mã trang (SC01-01).

### 12. Kiểm tra quy tắc tác nhân khi package chỉ mới có phần tử của một tác nhân
- Vị trí: A3, "Package của P09 vi phạm quy tắc tác nhân ở trên thì giữ mã PKG đó làm package cha không chứa phần tử, cấp package con cho từng tác nhân và ghi Đề xuất sửa P09".
- Gặp gì: P09 ghi chú PKG-05 gộp ACT-01 và ACT-02 và cho phép P10 tách. Hiện chỉ có lớp của ACT-02 nên chưa vi phạm, nhưng chắc chắn vi phạm khi UC-001 đến UC-003 có lớp. Prompt không nói kiểm theo lớp đã có hay theo ACT của P09.
- Xử lý: kiểm theo lớp đã có, không tách PKG-05; ghi tách sau vào Vấn đề còn mở, mã mới từ PKG-33.

### 13. Phạm vi "toàn hệ thống" và yêu cầu bổ sung giới hạn bốn use case
- Vị trí: Context, "Phạm vi: toàn hệ thống"; F3, "Mọi lớp trong P08 F3 có Trạng thái 'Hoạt động' hoặc 'Tạm ...' có đúng một dòng"; YEU_CAU_BO_SUNG của lần chạy (24 use case chưa phân tích).
- Gặp gì: các package của 24 use case còn lại (PKG-06, PKG-08, PKG-09, PKG-13, PKG-17, PKG-18, PKG-19, PKG-31) không có phần tử; Target 5 và F4 mức hợp lý ("package 2-15 phần tử") không áp dụng cho package giữ chỗ. Một số package đạt một phần tử (PKG-11, PKG-14).
- Xử lý: package giữ chỗ ghi "(giữ chỗ, chưa có phần tử)"; hai package một phần tử ghi lý do thay đổi riêng ở cột Tiêu chí nhóm.

### 14. Mã Q lớn nhất không đồng bộ giữa các artifact
- Vị trí: C3, "Lần chạy nào cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất ...; Mã lớn nhất tìm trong mục Câu hỏi mở và Giả định của mọi artifact đã có trong THU_MUC_DAU_RA".
- Gặp gì: P08 ghi Q-87, P09 ghi Q-94; người dùng cho Q-94. C3 yêu cầu quét mọi artifact kể cả file không thuộc đầu vào; phạm vi đọc của lần chạy này hạn chế nên không quét lại.
- Xử lý: dùng Q-94 người dùng cung cấp. P10 không cấp Q mới: không thấy chỗ nguồn mơ hồ mới cần người dùng trả lời, các điểm chưa chắc dẫn Q có sẵn (Q-45, Q-47, Q-67, Q-89, Q-93).

### 15. Câu "Mức hợp lý" và "Lỗi thường gặp" không có ngưỡng cho số interface gọi ngược
- Vị trí: F1 đến F4 (mức hợp lý chỉ có cho tỷ lệ tách và số phần tử package).
- Gặp gì: có 15 interface cho 23 lớp phân tích (7 của subsystem, 3 gọi ngược, 5 kho dữ liệu); 5 interface kho dữ liệu theo package, không rõ nên theo entity hay package. Chọn theo package để giữ GON.
- Xử lý: ghi ở F3 bảng cơ chế; để P12 tách nếu cần.

Phần có sẵn tốt: bảng "Phần cần dùng" đủ để không phải đọc P04, P05; ví dụ ở F1, F3 giúp phân biệt đúng control không thành subsystem.
