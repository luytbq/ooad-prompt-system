# P09 - Thiết kế kiến trúc (Architectural Design)

## 1. Mục đích

Bước này quyết định cấu trúc mức cao nhất của phần mềm: chọn mẫu kiến trúc phù hợp với yêu cầu phi chức năng và bối cảnh kỹ thuật, chốt công nghệ khi hồ sơ dự án chưa chốt, chia hệ thống thành các layer và package cấp cao, đặt quy tắc phụ thuộc giữa chúng, định hướng mức cao cho giao tiếp với hệ thống ngoài và cho lưu trữ dữ liệu. Kết quả là khung mà P10 dùng để xếp các phần tử thiết kế, P11a, P11b dùng để đặt giao diện, P12 và P13 dùng để thiết kế chi tiết.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md (mục Bối cảnh kỹ thuật) | Có | Nền tảng, công nghệ, hệ thống ngoài đã chốt hoặc "Chưa chốt" |
| Đầu vào | 00-Conventions.md | Có | Luật chung, mã PKG, quy ước sơ đồ |
| Đầu vào | P06-supplementary-spec.md | Có | NFR và ràng buộc là căn cứ chọn kiến trúc |
| Đầu vào | P08-analysis-model.md | Có | Lớp phân tích và quan hệ, để kiểm tra kiến trúc chứa được mô hình |
| Đầu vào | P01-actors.md | Có | Hệ thống ngoài, thiết bị, các nhóm người dùng |
| Đầu vào | P02-usecases.md, P03-usecase-model.md | Có | Nhóm chức năng, quy mô |
| Đầu vào | P05-glossary.md | Không | Tên package theo ngôn ngữ nghiệp vụ |
| Đầu ra | P09-architecture.md | Có | Quyết định kiến trúc, công nghệ đã chốt, layer, package cấp cao, quy tắc phụ thuộc, khối cập nhật hồ sơ dự án |
| Đầu ra | diagrams/P09-package-layers.drawio | Có | Package diagram thể hiện layer và phụ thuộc |
| Đầu ra | diagrams/P09-deployment.drawio | (chỉ khi DAY_DU) Khi hệ thống phân tán | Deployment diagram mức cao |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md và các file đầu vào.
- Chạy một lần cho toàn hệ thống. Chạy lại khi NFR hoặc bối cảnh kỹ thuật thay đổi.
- Nếu NEN_TANG hoặc CONG_NGHE trong hồ sơ dự án là "Chưa chốt", AI lập bảng so sánh 2-3 phương án công nghệ, nêu khuyến nghị có lý do, rồi mới chọn mẫu cho phía giao diện. Người dùng chốt bằng placeholder PHUONG_AN_DA_CHON (điền trước khi chạy, hoặc chạy lại sau khi đọc khuyến nghị); để trống thì AI dùng phương án khuyến nghị và ghi rõ là khuyến nghị chờ xác nhận.
- Sau khi chạy: sao chép khối trong mục "Cập nhật hồ sơ dự án" (F11) của P09-architecture.md vào project-profile.md mục 3, trước khi chạy P10.

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| RANG_BUOC_KIEN_TRUC | Tuỳ chọn | Quyết định kiến trúc đã có sẵn (bắt buộc dùng, cấm dùng) |
| TIEU_CHI_UU_TIEN | Tuỳ chọn | Thứ tự ưu tiên thuộc tính chất lượng khi NFR không nêu |
| PHUONG_AN_DA_CHON | Tuỳ chọn | Phương án công nghệ người dùng đã chốt sau khi đọc bảng so sánh (chỉ dùng khi hồ sơ ghi "Chưa chốt") |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được hồ sơ dự án (project-profile.md, đặc biệt mục Bối cảnh kỹ thuật: NEN_TANG, CONG_NGHE, HE_THONG_NGOAI), 00-Conventions.md và các artifact đã chốt: P01-actors.md, P02-usecases.md, P03-usecase-model.md, P06-supplementary-spec.md, P08-analysis-model.md, (nếu có) P05-glossary.md. Tuân thủ 00-Conventions.md, đặc biệt C1, C3, C5, C7.
Phạm vi: toàn hệ thống.

Ràng buộc kiến trúc đã có:
{{PH:RANG_BUOC_KIEN_TRUC | Hướng dẫn: [TUỲ CHỌN] quyết định đã chốt từ bên ngoài bước này (quy chuẩn tổ chức, hạ tầng sẵn có); chưa có thì thay cả khối bằng "Không có" | Ví dụ: "Bắt buộc tách front-end và back-end, back-end phân lớp 3 tầng." (giao đồ ăn); "Ứng dụng desktop một máy, không có máy chủ riêng." (quản lý bãi đỗ xe); "Không dùng kiến trúc microservices."}}

Thứ tự ưu tiên thuộc tính chất lượng:
{{PH:TIEU_CHI_UU_TIEN | Hướng dẫn: [TUỲ CHỌN] dùng khi P06 không xếp hạng NFR; liệt kê từ quan trọng nhất | Ví dụ: "Bảo trì, Bảo mật, Hiệu năng, Khả chuyển" (phòng khám); "Sẵn sàng, Hiệu năng, Khả mở rộng" (giao đồ ăn)}}

Phương án công nghệ đã chốt:
{{PH:PHUONG_AN_DA_CHON | Hướng dẫn: [TUỲ CHỌN] chỉ dùng khi NEN_TANG hoặc CONG_NGHE là "Chưa chốt"; ghi mã phương án trong bảng so sánh công nghệ của lần chạy trước (ví dụ "CN2") hoặc mô tả phương án; để "Không có" thì AI dùng phương án khuyến nghị và ghi là khuyến nghị chờ xác nhận | Ví dụ: "CN2: web render phía máy chủ, Java 17, Spring Boot, PostgreSQL" (phòng khám); "Ứng dụng desktop C#, .NET 8, SQLite" (quản lý bãi đỗ xe)}}

[Role]
Bạn là kiến trúc sư phần mềm, thành thạo các mẫu kiến trúc (multi-layer, client-server, broker, transaction-processing, pipe-and-filter, MVC, MVP, MVVM, front-end/back-end, và các biến thể cho giao diện như Flux, VIPER), phương pháp chọn kiến trúc dựa trên thuộc tính chất lượng, các nguyên tắc thiết kế tốt (chia để trị, cohesion cao, coupling thấp, trừu tượng, tái sử dụng, linh hoạt, dự phòng lỗi thời, khả chuyển, dễ kiểm thử, thiết kế phòng vệ) và ký pháp UML 2.5.1 cho package, component, deployment diagram.

[Action]
A1. Xác định yêu cầu có ý nghĩa kiến trúc.
- Từ P06, chọn các NFR và ràng buộc ảnh hưởng tới cấu trúc: hiệu năng, sẵn sàng, bảo mật, khả năng thay đổi giao diện, số loại client, tích hợp hệ thống ngoài và thiết bị, phân tán, triển khai, khả chuyển, dễ kiểm thử.
- Từ hồ sơ dự án và P01, xác định: loại ứng dụng, số loại client, hệ thống ngoài và thiết bị.
- Mỗi yêu cầu được viết lại thành kịch bản thuộc tính chất lượng ngắn: nguồn kích thích, kích thích, phản hồi, thước đo. Không tự đặt ngưỡng mà P06 không nêu; thiếu thì ghi Q-nn hoặc ASM-nn.
- Quyết định kiến trúc cần cho cấu trúc mà nguồn không nêu (loại client của một nhóm người dùng, nơi đặt thành phần trung gian, số node triển khai) được phép đưa ra ở cả hai chế độ, vì thiếu nó không dựng được kiến trúc. Mỗi quyết định như vậy ghi ở F3 dòng "Rủi ro còn mở" kèm Q-nn để người dùng xác nhận.

A2. Lập danh sách phương án.
- Chọn 2-4 phương án khả thi cho cấu trúc tổng thể từ các mẫu: Multi-layer (ví dụ 3 layer Presentation, Business/Application, Data/Services), Client-server, Front-end/Back-end (mỗi phía có mẫu riêng), Broker, Transaction-processing, Pipe-and-filter. Mẫu kiến trúc có thể kết hợp (ví dụ client-server ở mức triển khai, layered ở back-end).
- Mẫu cho phía giao diện (MVC active hoặc passive, MVP, MVVM, Flux, VIPER) phụ thuộc công nghệ giao diện, nên chỉ chọn ở A3b, sau khi có phương án công nghệ. Khi NEN_TANG và CONG_NGHE đã chốt, có thể xét cùng lúc ở bước này.
- Loại ngay phương án xung đột với RANG_BUOC_KIEN_TRUC hoặc với NEN_TANG, CONG_NGHE đã chốt.

A3. So sánh và chọn mẫu kiến trúc.
- Nếu NEN_TANG hoặc CONG_NGHE là "Chưa chốt", hoặc có từ 2 phương án khả thi trở lên: lập bảng so sánh theo các yêu cầu có ý nghĩa kiến trúc (A1), chấm mức đáp ứng, kết luận.
- Nếu hồ sơ đã chốt một mẫu: kiểm tra mẫu đó đáp ứng NFR, ghi rủi ro, không cần bảng so sánh đầy đủ.
- Ghi quyết định theo dạng bản ghi quyết định kiến trúc: bối cảnh, quyết định, phương án đã loại và lý do, hệ quả (tích cực, tiêu cực), NFR được đáp ứng.

A3a. Chốt công nghệ (chỉ khi NEN_TANG hoặc CONG_NGHE là "Chưa chốt").
- Lập 2-3 phương án công nghệ phù hợp mẫu kiến trúc đã chọn ở A3. Mỗi phương án gồm: loại ứng dụng và nền tảng (web render phía máy chủ, SPA, mobile, desktop), ngôn ngữ và framework phía máy chủ, công nghệ phía giao diện, loại và hệ quản trị CSDL, cơ chế giao tiếp với hệ thống ngoài và thiết bị khi có.
- So sánh theo: NFR có ý nghĩa kiến trúc (A1), ràng buộc trong P06 và RANG_BUOC_KIEN_TRUC, yêu cầu của hệ thống ngoài trong HE_THONG_NGOAI và P01 (giao thức, tài liệu API, thư viện sẵn có), mức phù hợp quy mô dự án. Không chọn theo xu hướng mà không gắn tiêu chí.
- Nêu phương án khuyến nghị kèm lý do gắn với tiêu chí.
- Phương án dùng cho các bước còn lại: PHUONG_AN_DA_CHON nếu người dùng đã điền; nếu để trống, dùng phương án khuyến nghị và ghi trạng thái "Khuyến nghị - chờ người dùng xác nhận" ở F2.2, F3 và F11.
- Ghi giá trị NEN_TANG, CONG_NGHE của phương án được dùng vào F11 để người dùng dán vào hồ sơ dự án.

A3b. Chọn mẫu cho phía giao diện.
- Chọn sau A3a (hoặc theo NEN_TANG, CONG_NGHE đã chốt): mẫu cho phía giao diện phải khớp công nghệ giao diện. Ví dụ: web render phía máy chủ --> MVC passive; SPA --> kiến trúc component kết hợp Flux hoặc MVVM; nền tảng có data binding --> MVVM; desktop cần kiểm thử logic trình bày --> MVP.
- Ghi mẫu đã chọn vào F3 và dùng nó cho bảng ánh xạ F5.

A4. Xác định layer và package cấp cao.
- Đặt tên layer theo mẫu đã chọn. Với multi-layer, tối thiểu có layer giao diện (presentation), layer nghiệp vụ hoặc ứng dụng (application logic, domain), layer dịch vụ kỹ thuật (persistence, tích hợp hệ thống ngoài, logging, bảo mật). Layer application và domain có thể tách hoặc gộp tuỳ độ phức tạp nghiệp vụ; ghi lý do.
- Trong mỗi layer, xác định package cấp cao theo nhóm chức năng hoặc theo trách nhiệm kỹ thuật. Mỗi package có một trách nhiệm phát biểu được trong một câu.
- Xác định quy tắc ánh xạ stereotype lớp phân tích sang layer hoặc vai trò trong mẫu, để P10 áp dụng.

A5. Đặt quy tắc phụ thuộc.
- Chọn layered nghiêm ngặt (layer chỉ phụ thuộc layer ngay dưới) hoặc nới lỏng (được phụ thuộc mọi layer dưới). Ghi lý do.
- Quy tắc bắt buộc: mũi tên phụ thuộc (kể cả realization) không bao giờ đi từ layer dưới lên layer trên; không phụ thuộc vòng giữa package.
- Khi layer dưới cần gọi ngược lên layer trên (thông báo, callback): layer dưới định nghĩa interface cho việc gọi ngược, layer trên hiện thực interface đó; realization đi từ lớp ở layer trên xuống interface ở layer dưới, theo nguyên tắc đảo phụ thuộc (DIP). Tương tự, interface mà lớp ở layer trên dùng (kho dữ liệu, subsystem giao tiếp ngoài) đặt ở package cùng layer với lớp hiện thực hoặc thấp hơn, không đặt ở layer của bên dùng.
- Ghi rõ các chỗ dùng cơ chế gọi ngược qua interface.

A6. Định hướng mức cao cho giao tiếp ngoài và dữ liệu.
- Với mỗi hệ thống ngoài và thiết bị trong P01: layer và package chứa phần giao tiếp, nguyên tắc cô lập (mỗi hệ thống ngoài được che sau một interface, sẽ thành subsystem ở P10).
- Lưu trữ: loại cơ chế lưu trữ (quan hệ, tài liệu, file) và layer chứa phần truy cập dữ liệu. Nếu CONG_NGHE chưa chốt, dùng hệ quản trị của phương án công nghệ ở A3a.

A7. Kiểm tra mô hình phân tích chứa được trong kiến trúc.
- Với mỗi lớp phân tích trong P08, xác định layer đích theo quy tắc ánh xạ A4. Lớp nào không có chỗ phù hợp là dấu hiệu kiến trúc thiếu layer hoặc package; sửa kiến trúc.
- Kiểm tra control giữ trạng thái giữa hai sự kiện của tác nhân (chờ thiết bị, chờ hệ thống ngoài, chờ hết thời hạn). Nếu kiến trúc không cho giữ trạng thái đó trong bộ nhớ (nhiều tiến trình, nhân bản, khởi động lại theo NFR sẵn sàng), ghi Đề xuất sửa P07 thêm entity cho trạng thái chờ.
- Không thực hiện ánh xạ chi tiết sang lớp thiết kế (việc của P10).

A8. Vẽ package diagram (và deployment diagram khi cần), tự kiểm tra, xuất kết quả.

[Format]
Xuất file P09-architecture.md theo khung C5, tiêu đề "# P09 - Thiết kế kiến trúc - <Tên hệ thống>". Nội dung chính:

F1. Yêu cầu có ý nghĩa kiến trúc
Bảng: | STT | Nguồn (NFR, ràng buộc, ACT) | Kịch bản thuộc tính chất lượng (kích thích --> phản hồi --> thước đo) | Mức ưu tiên | Ảnh hưởng kiến trúc |
- Mức hợp lý: 3-10 dòng. Ít hơn 3 thường là bỏ sót (hệ thống nào cũng có ít nhất yêu cầu về bảo trì, bảo mật hoặc hiệu năng nếu P06 có); nhiều hơn 10 thường là chép cả NFR không ảnh hưởng cấu trúc (ví dụ màu sắc giao diện).
- Ví dụ đúng (phòng khám): "NFR-03 --> Lễ tân mở danh sách lịch hẹn trong ngày --> hiển thị trong 2 giây với 500 lịch hẹn --> ảnh hưởng: cần tách truy vấn đọc, cân nhắc cache ở layer ứng dụng".
- Ví dụ sai: "Hệ thống phải nhanh" (không đo được, không có nguồn NFR).

F2. Phương án và so sánh
F2.1. Mẫu kiến trúc (bắt buộc khi NEN_TANG hoặc CONG_NGHE là "Chưa chốt", hoặc có từ 2 phương án khả thi)
Bảng mô tả phương án: | PA | Mẫu kiến trúc (và kết hợp) | Mô tả ngắn | Điều kiện phù hợp |
Bảng so sánh: | Tiêu chí (từ F1) | Trọng số | PA1 | PA2 | PA3 |, ô ghi mức đáp ứng (Tốt / Trung bình / Kém) kèm lý do một câu; dòng cuối là kết luận.
Hướng dẫn chọn mẫu (để suy luận, không chép máy móc):
- Multi-layer: hợp khi cần tách giao diện khỏi nghiệp vụ và dữ liệu, dễ bảo trì, dễ thay giao diện; chi phí: thêm lớp trung gian, có thể chậm nếu mỗi yêu cầu đi qua nhiều layer.
- Client-server: hợp khi nhiều client dùng chung dữ liệu và dịch vụ tập trung; cần xét mạng, bảo mật, sẵn sàng của server.
- Front-end/Back-end: hợp khi có nhiều loại client (web, mobile) dùng chung dịch vụ; mỗi phía chọn mẫu riêng.
- MVC: hợp với ứng dụng có nhiều view trên cùng dữ liệu; biến thể passive (controller nhận yêu cầu, chọn view, view không quan sát model) phổ biến với web phía server; biến thể active (view quan sát model) hợp ứng dụng desktop. Rủi ro: controller phình to, nhiều model và view chằng chịt khi hệ thống lớn.
- MVP: view thụ động, presenter giữ logic trình bày; hợp khi cần kiểm thử logic giao diện mà không cần giao diện thật.
- MVVM: view gắn dữ liệu (data binding) với view model; hợp với nền tảng có cơ chế binding.
- Broker: hợp khi các thành phần phân tán cần gọi nhau mà không biết vị trí của nhau.
- Transaction-processing: hợp khi đầu vào là dòng giao dịch nhiều loại, mỗi loại một bộ xử lý.
- Pipe-and-filter: hợp với xử lý dữ liệu tuần tự qua nhiều bước biến đổi độc lập.
- Flux, VIPER: biến thể cho tầng giao diện trên nền tảng cụ thể; chỉ đề xuất khi NEN_TANG phù hợp.
Lỗi thường gặp: chọn mẫu theo xu hướng mà không gắn NFR; chọn microservices hoặc broker cho hệ thống nhỏ một nhóm phát triển không có yêu cầu phân tán (quá lớn); chỉ ghi "dùng MVC" mà không nói MVC nằm ở đâu trong hệ thống (quá nhỏ); chọn mẫu cho phía giao diện trước khi có công nghệ giao diện.

F2.2. Chốt công nghệ (bắt buộc khi NEN_TANG hoặc CONG_NGHE là "Chưa chốt"; hồ sơ đã chốt thì ghi "Không áp dụng, hồ sơ đã chốt")
Bảng phương án: | CN | Nền tảng | Phía máy chủ (ngôn ngữ, framework) | Phía giao diện | CSDL | Giao tiếp ngoài |
Bảng so sánh: | Tiêu chí (F1, ràng buộc P06, HE_THONG_NGOAI) | CN1 | CN2 | CN3 |, ô ghi mức đáp ứng (Tốt / Trung bình / Kém) kèm lý do một câu.
Kết luận: phương án khuyến nghị và lý do; phương án được dùng (PHUONG_AN_DA_CHON hoặc khuyến nghị); trạng thái ("Đã chốt bởi người dùng" hoặc "Khuyến nghị - chờ người dùng xác nhận").
- Mức hợp lý: 2-3 phương án khác nhau thật sự (khác nền tảng hoặc khác cách dựng giao diện), không phải ba phiên bản của cùng một framework.
- Ví dụ đúng (quản lý bãi đỗ xe, một máy tính tại cổng, không có máy chủ riêng): CN1 desktop C#, .NET, SQLite; CN2 web chạy cục bộ, Node.js, SQLite; khuyến nghị CN1 vì RANG_BUOC_KIEN_TRUC yêu cầu ứng dụng một máy và thư viện điều khiển thanh chắn của nhà cung cấp chỉ có cho .NET (HE_THONG_NGOAI).
- Ví dụ sai: "Dùng React, Spring Boot, PostgreSQL vì phổ biến" (không có phương án so sánh, không gắn tiêu chí).

F3. Quyết định kiến trúc
Bảng: | Mục | Nội dung |, gồm: Bối cảnh; Quyết định (mẫu và cách kết hợp); Mẫu cho phía giao diện (A3b); Công nghệ (theo hồ sơ, hoặc phương án ở F2.2 kèm trạng thái); Phương án đã loại và lý do; Hệ quả tích cực; Hệ quả tiêu cực và cách giảm thiểu; NFR được đáp ứng (mã); Rủi ro còn mở (kể cả quyết định kiến trúc mà nguồn không nêu, kèm Q-nn theo A1).

F4. Layer và package cấp cao (bảng lõi, P10 đọc bảng này)
| PKG | Tên | Layer | Trách nhiệm | Phụ thuộc vào (PKG) | Nguồn (NFR, UC nhóm, ACT) |
- PKG: mã PKG-nn theo C3, cấp từ PKG-01. Mỗi layer là một PKG; package cấp cao bên trong layer là PKG riêng, cột Layer ghi mã PKG của layer chứa nó. P10 sẽ tiếp tục cấp mã từ số lớn nhất ở bước này.
- Tên: tiếng Anh PascalCase hoặc theo NGON_NGU_TEN_PHAN_TU, danh từ chỉ trách nhiệm, ví dụ Presentation, Application, Domain, Persistence, ExternalIntegration, Appointment, Inventory.
- Trách nhiệm: một câu, không chứa "và" nối hai trách nhiệm khác loại.
- Phụ thuộc vào: danh sách PKG; phải tuân F6.
Mức hợp lý: 3-5 layer; mỗi layer 1-8 package cấp cao. Trên 5 layer thường là chia vụn; 1 layer là chưa phân tách.
Lỗi thường gặp: package theo loại kỹ thuật ở layer nghiệp vụ (Controllers, Models chứa mọi thứ) khi hệ thống có nhiều nhóm chức năng độc lập (quá lớn, cohesion thấp); package cho từng lớp (quá nhỏ); đặt package tích hợp hệ thống ngoài trong layer giao diện (nhầm layer).
Ví dụ đúng (quản lý kho, 3 layer): PKG-01 Presentation; PKG-02 Application; PKG-03 Services; PKG-04 InventoryUI (layer PKG-01); PKG-05 Inventory (layer PKG-02); PKG-06 Persistence (layer PKG-03); PKG-07 ErpIntegration (layer PKG-03), PKG-05 phụ thuộc PKG-06, PKG-07.
Ví dụ sai: PKG-06 Persistence phụ thuộc PKG-05 Inventory để gọi hàm nghiệp vụ khi lưu (sai: layer dưới phụ thuộc layer trên).

F5. Quy tắc ánh xạ lớp phân tích sang kiến trúc (P10 đọc bảng này)
Bảng: | Stereotype hoặc loại lớp phân tích | Layer hoặc vai trò trong mẫu đích | Ghi chú |
- Tối thiểu có dòng cho: boundary giao diện người dùng; boundary kênh thông báo (email, SMS, thông báo đẩy) khi P08 có; boundary giao diện hệ thống; boundary giao diện thiết bị; control; entity (phần hành vi nghiệp vụ); entity (phần lưu trữ).
- Ví dụ (layered kết hợp MVC passive ở web): boundary người dùng --> View và phần tiếp nhận yêu cầu (Controller của MVC) ở Presentation; control --> lớp dịch vụ ứng dụng ở Application; entity --> lớp miền ở Domain, phần lưu trữ do Persistence đảm nhận; boundary hệ thống --> subsystem ở Services.
- Ví dụ (desktop MVP): boundary người dùng --> View và Presenter; control --> Application service; entity --> Model.
- Lưu ý: "controller" của MVC là thành phần giao diện, khác lớp control của phân tích; ghi rõ trong bảng để tránh nhầm.

F6. Quy tắc phụ thuộc
Liệt kê dạng câu, mỗi câu kiểm tra được:
- Kiểu layered: nghiêm ngặt hoặc nới lỏng, kèm lý do.
- Layer dưới không phụ thuộc layer trên; không có mũi tên dependency hoặc realization đi lên.
- Không có vòng phụ thuộc giữa các package (kể cả vòng qua nhiều package).
- Nếu layered nghiêm ngặt: không nhảy layer (Presentation không phụ thuộc trực tiếp Services).
- Cách truyền thông tin ngược lên nếu có: interface do layer dưới định nghĩa, layer trên hiện thực (A5).
- Package phụ thuộc vào interface của subsystem, không phụ thuộc vào lớp bên trong subsystem.
Kèm bảng kiểm tra: | Phụ thuộc (PKG --> PKG) | Hợp lệ | Quy tắc áp dụng |, một dòng cho mỗi phụ thuộc trong F4.

F7. Định hướng giao tiếp ngoài và dữ liệu
Bảng giao tiếp ngoài: | ACT (hệ thống ngoài, thiết bị) | PKG chứa | Nguyên tắc cô lập | Rủi ro (lỗi, timeout, thay đổi API) |
Bảng dữ liệu: | Mục | Quyết định | Lý do |, gồm: loại cơ chế lưu trữ; layer truy cập dữ liệu; chiến lược giao dịch mức cao (nếu NFR có yêu cầu nhất quán); dữ liệu cần bảo vệ (nếu NFR bảo mật có).

F8. Kiểm tra chứa mô hình phân tích
Bảng: | Nhóm lớp phân tích (theo stereotype hoặc nhóm chức năng) | Số lớp | Layer, PKG đích | Vấn đề |. Mọi lớp hoạt động trong P08 thuộc một nhóm.

F9. Package diagram
File diagrams/P09-package-layers.drawio.
a) Bảng Node: | ID (PKG) | Loại (Package / Layer) | Nhãn | Stereotype («layer» cho layer) | Thuộc về (PKG layer chứa) | Ghi chú |
b) Bảng Edge: | ID | Nguồn | Đích | Loại quan hệ (Dependency) | Nhãn | Ghi chú |
Quy tắc ngữ nghĩa UML: package là hình thư mục; package lồng nhau thể hiện quan hệ sở hữu; phụ thuộc là mũi tên nét đứt đầu mở từ package phụ thuộc tới package được dùng; nhãn «import» hoặc «access» chỉ ghi khi cần phân biệt; không vẽ phụ thuộc hai chiều.
Bố cục: layer trên cùng ở trên, xếp chồng theo chiều dọc; package con nằm trong layer; mũi tên phụ thuộc đi từ trên xuống; không có mũi tên nào đi lên, kể cả realization (nếu có là lỗi phải sửa bằng cách chuyển interface xuống layer của bên hiện thực hoặc thấp hơn, theo A5); realization từ package ở layer trên tới interface do layer dưới định nghĩa đi xuống nên hợp lệ; theo C7.3.

F10. Deployment diagram (chỉ khi DAY_DU), khi hệ thống có từ hai node thực thi trở lên
File diagrams/P09-deployment.drawio. Bảng Node: node (thiết bị, môi trường thực thi) và artifact triển khai; bảng Edge: đường truyền thông (communication path) có nhãn giao thức mức khái niệm (ví dụ "mạng nội bộ", "Internet, mã hoá"). Style node: shape=cube;whiteSpace=wrap;html=1;boundedLbl=1;. Không ghi địa chỉ IP, tên máy cụ thể.

F11. Cập nhật hồ sơ dự án
Khối văn bản để người dùng dán vào project-profile.md mục 3, đặt trong code block text:
| Trường | Giá trị |
|---|---|
| NEN_TANG | <giá trị đã chốt> |
| CONG_NGHE | <ngôn ngữ, framework phía máy chủ, công nghệ phía giao diện, hệ quản trị CSDL> |
Dưới khối ghi trạng thái ("Đã chốt bởi người dùng" hoặc "Khuyến nghị - chờ người dùng xác nhận") và nhắc: cập nhật hồ sơ trước khi chạy P10. Hồ sơ đã chốt cả hai trường thì ghi "Không cần cập nhật".

F12. Mục kiểm soát theo C5.

[Target]
1. Mọi yêu cầu có ý nghĩa kiến trúc truy được về NFR, ràng buộc hoặc tác nhân; không có ngưỡng tự đặt ngoài P06 (trừ khi có ASM).
2. Có bảng so sánh phương án khi NEN_TANG hoặc CONG_NGHE là "Chưa chốt" hoặc có từ 2 phương án khả thi.
3. Quyết định kiến trúc nêu rõ NFR được đáp ứng, phương án bị loại và hệ quả tiêu cực.
4. Mỗi PKG có một trách nhiệm một câu và thuộc đúng một layer.
5. Không có phụ thuộc từ layer dưới lên layer trên; không có vòng phụ thuộc; không nhảy layer nếu chọn layered nghiêm ngặt.
6. Mỗi hệ thống ngoài và thiết bị trong P01 có PKG chứa phần giao tiếp và được che sau interface.
7. Bảng ánh xạ stereotype sang layer đủ các loại lớp phân tích; mọi lớp hoạt động trong P08 có layer đích.
8. Khi NEN_TANG hoặc CONG_NGHE là "Chưa chốt": F2.2 có 2-3 phương án công nghệ so sánh theo NFR, ràng buộc, hệ thống ngoài và một khuyến nghị có lý do; phương án được dùng là PHUONG_AN_DA_CHON hoặc khuyến nghị ghi "Khuyến nghị - chờ người dùng xác nhận"; mẫu cho phía giao diện được chọn sau và khớp phương án công nghệ; F11 có khối NEN_TANG, CONG_NGHE để cập nhật hồ sơ.
9. Bảng mô hình và file .drawio khớp nhau, đạt C7.3.
10. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này | Ví dụ: "Dùng layered nới lỏng."; "Tên layer theo quy chuẩn: UI, Service, Repository."; "Bổ sung component diagram cho phía back-end."}}
````

## 5. Ghi chú cho người dùng

- Nếu đã biết công nghệ, điền NEN_TANG và CONG_NGHE trong hồ sơ dự án trước khi chạy; AI sẽ bỏ qua phần so sánh đầy đủ và kiểm tra tính phù hợp thay vào đó.
- Nếu hồ sơ ghi "Chưa chốt": đọc F2.2, chọn phương án, rồi hoặc chạy lại với PHUONG_AN_DA_CHON (khi phương án chọn khác khuyến nghị), hoặc chấp nhận khuyến nghị. Sau đó dán khối F11 vào project-profile.md mục 3 trước khi chạy P10. Bỏ qua bước này thì P12, P13, X2 không có kiểu dữ liệu, hệ quản trị CSDL, khung kiểm thử để dùng.
- Khi AI đề xuất kiến trúc phức tạp hơn quy mô dự án (ví dụ microservices cho hệ thống vài chục use case, một nhóm phát triển), dùng RANG_BUOC_KIEN_TRUC để loại và chạy lại.
- Bảng ánh xạ stereotype sang layer (F5) là đầu vào trực tiếp của P10; kiểm tra kỹ phần phân biệt "controller" của MVC với lớp control của phân tích.
- Dùng độc lập: cần tối thiểu danh sách NFR đo được, danh sách hệ thống ngoài và một bảng lớp phân tích hoặc danh sách nhóm chức năng. Không có P08 thì bỏ mục F8 và ghi trong "Vấn đề còn mở".

## 6. Căn cứ

- Bass L., Clements P., Kazman R., Software Architecture in Practice, 4th ed. (2021): yêu cầu có ý nghĩa kiến trúc, kịch bản thuộc tính chất lượng, chiến thuật kiến trúc.
- Buschmann F. và cộng sự, Pattern-Oriented Software Architecture, Volume 1: A System of Patterns (1996): Layers, Pipes and Filters, Broker, Model-View-Controller.
- Lethbridge T., Laganière R., Object-Oriented Software Engineering: Practical Software Development using UML and Java, 2nd ed. (2005): các nguyên tắc dẫn tới thiết kế tốt, các mẫu kiến trúc multi-layer, client-server, broker, transaction-processing, pipe-and-filter, MVC.
- Larman C., Applying UML and Patterns, 3rd ed. (2004): kiến trúc logic phân lớp, quy tắc phụ thuộc giữa layer.
- Fowler M., Patterns of Enterprise Application Architecture (2002): phân lớp presentation, domain, data source.
- Martin R. C., Clean Architecture (2017): nguyên tắc phụ thuộc không vòng (Acyclic Dependencies Principle), phụ thuộc hướng vào ổn định.
- Nygard M., Documenting Architecture Decisions (2011): mẫu bản ghi quyết định kiến trúc.
- OMG, Unified Modeling Language 2.5.1 (2017): package diagram, deployment diagram.
