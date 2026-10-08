# P09 - Thiết kế kiến trúc - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P09 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (bản hiện có, mục 3 NEN_TANG và CONG_NGHE đang "Chưa chốt"); 00-Conventions.md (bản hiện có); P01-actors.md 1.0; P02-usecases.md 1.1; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P08-analysis-model.md 1.0; yeu-cau-xe-khach.md (bản hiện có, để trích nguồn). Tham số: RANG_BUOC_KIEN_TRUC = Không có; TIEU_CHI_UU_TIEN = Không có (dùng ASM-57); PHUONG_AN_DA_CHON = Không có (dùng phương án khuyến nghị); YEU_CAU_BO_SUNG = Không có |
| Phạm vi | Toàn hệ thống. Mô hình phân tích P08 mới phủ 4 trong 18 use case (UC-002, UC-008, UC-013, UC-015); các nhóm còn lại được đặt chỗ trong kiến trúc theo P02 và P01 |

Tóm tắt: chọn kiến trúc Front-end/Back-end, back-end phân lớp nới lỏng theo kiểu module hoá đơn khối, client-server ở mức triển khai (PA2, F2.1). Công nghệ chưa chốt nên lập 3 phương án (F2.2), khuyến nghị CN1 và dùng làm phương án cho các bước sau với trạng thái "Khuyến nghị - chờ người dùng xác nhận". Hệ thống có 4 layer, 21 package cấp cao (PKG-01 đến PKG-25), 37 phụ thuộc giữa package. Thứ tự layer từ trên xuống: Presentation, Application, Services, Domain; Domain nằm cuối cùng để Persistence ánh xạ được đối tượng miền mà không có phụ thuộc đi lên (xem F3, F6).

## F1. Yêu cầu có ý nghĩa kiến trúc

Thứ tự ưu tiên thuộc tính chất lượng theo ASM-57 vì P06 không xếp hạng NFR và TIEU_CHI_UU_TIEN không có.

| STT | Nguồn (NFR, ràng buộc, ACT) | Kịch bản thuộc tính chất lượng (kích thích --> phản hồi --> thước đo) | Mức ưu tiên | Ảnh hưởng kiến trúc |
|---|---|---|---|---|
| F1-01 | NFR-01 (REQ-66, REQ-01, REQ-02); ACT-01 | Khoảng 2.000 phiên truy cập đồng thời dịp Tết --> hệ thống xử lý hoàn tất các yêu cầu mà không phát sinh lỗi hệ thống (ASM-39) --> kiểm thử tải 2.000 phiên (ASM-38); ngưỡng thời gian phản hồi: Chưa quy định (Q-22, Q-52) | 2 (ASM-57) | Back-end không giữ trạng thái phiên trong bộ nhớ để chạy được nhiều bản song song; giao diện web là tệp tĩnh tách khỏi back-end; truy vấn đọc sơ đồ chỗ tách khỏi giao dịch ghi để có thể thêm bộ nhớ đệm ở layer Application |
| F1-02 | REQ-67; BR-02, BR-03; ACT-01, ACT-02 (SH-01: "chấm dứt trùng chỗ") | Hai chủ thể cùng chọn một chỗ của một chuyến tại cùng thời điểm (trên website hoặc tại quầy) --> chỉ một bên giữ được chỗ --> không bao giờ có hai vé còn hiệu lực cùng chỗ trên một chuyến (BR-02, có hoặc không) | 1 (ASM-57) | Một nơi lưu dữ liệu chỗ và vé có giao dịch và ràng buộc duy nhất; mọi kênh bán (web, quầy, điện thoại) đi qua cùng một back-end; không lưu quyết định giữ chỗ ở client |
| F1-03 | NFR-02 (REQ-59); NFR-10; UC-015; ACT-05, ACT-09 | Phụ xe quét một vé khi máy soát vé ở vùng mất sóng, sau khi máy đã nhận danh sách hành khách (ASM-33) --> máy báo hợp lệ hoặc không hợp lệ kèm lý do --> báo đúng cho từng vé (có hoặc không); vé bán sau mốc gửi danh sách: Q-11 | 3 (ASM-57) | Logic soát vé, dữ liệu danh sách hành khách và kết quả chờ gửi nằm trên máy soát vé; cần lưu trữ cục bộ và đồng bộ với máy chủ khi có sóng |
| F1-04 | NFR-03 (REQ-68); ACT-06 | Hành khách thanh toán trực tuyến --> hệ thống không nhận, không lưu thông tin thẻ (ASM-41) --> rà soát dữ liệu lưu trữ, mã nguồn, nhật ký: không có dữ liệu thẻ (có hoặc không) | 4 (ASM-57) | Dữ liệu thẻ chỉ đi giữa hành khách và cổng thanh toán; lưu trữ và nhật ký của hệ thống không chứa dữ liệu thẻ; xem Q-83 |
| F1-05 | NFR-04 (REQ-04), NFR-05 (REQ-56); P01 Mục 1; ACT-01 đến ACT-05 | Hành khách dùng website; phụ xe dùng ứng dụng trên máy Android --> hai loại client chạy trên nền tảng khác nhau gọi cùng nghiệp vụ --> kiểm tra triển khai: đặt vé chạy được trên website, ứng dụng soát vé cài đặt và chạy được trên máy Android (có hoặc không). Loại client của nhân viên nhà xe nguồn không nêu (Q-78) | 3 (ASM-57) | Nhiều loại client dùng chung nghiệp vụ --> Front-end/Back-end với API chung; mỗi client chọn mẫu giao diện riêng |
| F1-06 | NFR-06, NFR-07, NFR-08 (REQ-15, REQ-35, REQ-20); ACT-06, ACT-07 | Cổng thanh toán hoặc cổng SMS đổi API, không phản hồi hoặc báo lỗi --> phần còn lại của hệ thống không phải sửa --> thay đổi giới hạn trong một package tích hợp. Giao thức, xác thực, hành vi lỗi: Chưa quy định (Q-24, Q-55, Q-56) | 5 (ASM-57) | Mỗi hệ thống ngoài che sau interface trong một package riêng ở layer Services (subsystem ở P10); xử lý lỗi, hết thời gian chờ nằm trong package đó |
| F1-07 | NFR-09, NFR-10 (REQ-24, REQ-55, REQ-56); ACT-08, ACT-09 | Máy in vé, đầu quét mã vạch là thiết bị gắn với máy trạm hoặc máy soát vé --> ứng dụng dùng được thiết bị mà không phụ thuộc model cụ thể --> tích hợp thiết bị giới hạn trong một package. Model, kết nối, định dạng: Chưa quy định (Q-54, Q-57, Q-79) | 5 (ASM-57) | Thiết bị che sau interface như hệ thống ngoài; phần mềm điều khiển máy in chạy ở máy trạm tại quầy, phần đọc mã vạch chạy trên máy soát vé |
| F1-08 | ACT-10; BR-07, BR-08, BR-24, BR-33 (REQ-13, REQ-16, REQ-27, REQ-61, REQ-62) | Đến mốc 10 phút sau khi giữ chỗ, 60 phút hoặc 15 phút trước giờ xuất bến --> hệ thống tự thực hiện xử lý tương ứng (trả chỗ, huỷ đặt chỗ, chuẩn bị danh sách) --> mốc theo BR; sai số cho phép: Chưa quy định (Q-82) | 3 (ASM-57) | Cần thành phần định thời độc lập với yêu cầu của người dùng; mốc nằm trong dữ liệu (thời điểm bắt đầu giữ chỗ, giờ xuất bến) để nhiều bản back-end không xử lý trùng hay sót |

## F2. Phương án và so sánh

### F2.1. Mẫu kiến trúc

| PA | Mẫu kiến trúc (và kết hợp) | Mô tả ngắn | Điều kiện phù hợp |
|---|---|---|---|
| PA1 | Multi-layer đơn khối, giao diện web dựng phía máy chủ | Một ứng dụng web chia layer; trang dựng ở máy chủ; ứng dụng soát vé gọi thêm một nhóm API riêng | Chỉ có client là trình duyệt; ít yêu cầu về client khác |
| PA2 | Front-end/Back-end, back-end multi-layer module hoá, client-server ở mức triển khai | Back-end phơi API dùng chung; giao diện web hành khách, giao diện web nhân viên, ứng dụng soát vé là ba client; mỗi client có mẫu giao diện riêng; một cơ sở dữ liệu | Nhiều loại client dùng chung nghiệp vụ; nhóm phát triển nhỏ (ASM-58) |
| PA3 | Microservices kết hợp broker | Tách dịch vụ bán vé, vận hành chuyến, thanh toán, thông báo; giao tiếp qua broker thông điệp | Nhiều nhóm phát triển độc lập, yêu cầu mở rộng riêng từng phần |

| Tiêu chí (từ F1) | Trọng số | PA1 | PA2 | PA3 |
|---|---|---|---|---|
| F1-01 Chịu tải 2.000 phiên | Cao | Trung bình: nhân bản được nhưng mỗi thao tác chọn chỗ dựng lại trang ở máy chủ | Tốt: back-end không giữ phiên, giao diện tĩnh tách riêng, nhân bản dễ | Tốt: mở rộng từng dịch vụ, vượt nhu cầu nêu trong nguồn |
| F1-02 Không trùng chỗ | Cao nhất | Tốt: một cơ sở dữ liệu, giao dịch cục bộ | Tốt: một cơ sở dữ liệu, giao dịch cục bộ | Kém: dữ liệu chỗ, vé, thanh toán nằm ở nhiều dịch vụ, cần nhất quán phân tán |
| F1-03 Soát vé khi mất sóng | Cao | Trung bình: phải thêm API riêng, logic cục bộ vẫn phải xây | Tốt: ứng dụng soát vé là client có logic và dữ liệu cục bộ, gọi API chung | Trung bình: như PA2 nhưng thêm độ phức tạp đồng bộ giữa dịch vụ |
| F1-05 Nhiều loại client | Trung bình | Kém: giao diện gắn chặt với trang dựng ở máy chủ, client Android phải có đường riêng | Tốt: API chung cho mọi client | Tốt: API chung qua cổng vào |
| F1-06, F1-07 Cô lập hệ thống ngoài, thiết bị | Trung bình | Tốt: package tích hợp ở layer Services | Tốt: như PA1 | Tốt: mỗi tích hợp là một dịch vụ, nhiều phần tử vận hành hơn mức cần |
| Phù hợp quy mô (18 use case, nhóm nhỏ, ASM-58) | Trung bình | Tốt: đơn giản nhất | Tốt: thêm ranh giới API nhưng vẫn một khối triển khai | Kém: chi phí vận hành và nhất quán vượt quy mô, không có yêu cầu phân tán trong nguồn |
| Kết luận | | Loại: không đáp ứng tốt nhiều client | Chọn: đáp ứng cả ba tiêu chí trọng số cao và nhiều client | Loại: quá lớn so với quy mô, rủi ro với F1-02 |

### F2.2. Chốt công nghệ

NEN_TANG và CONG_NGHE trong hồ sơ dự án là "Chưa chốt". Ba phương án khác nền tảng hoặc cách dựng giao diện, cùng phù hợp PA2:

| CN | Nền tảng | Phía máy chủ (ngôn ngữ, framework) | Phía giao diện | CSDL | Giao tiếp ngoài |
|---|---|---|---|---|---|
| CN1 | Web ứng dụng một trang (SPA) cho hành khách và nhân viên; ứng dụng Android gốc cho máy soát vé | Java 17, Spring Boot, REST/JSON | Web: React, TypeScript, Redux Toolkit (Flux). Android: Kotlin, Room (SQLite cục bộ) | PostgreSQL | HTTPS tới cổng SMS (API REST); cổng thanh toán theo tài liệu API khi có (Q-24); máy in qua phần mềm trung gian ở máy trạm; đầu quét qua SDK hoặc đầu vào bàn phím của máy Android (Q-54) |
| CN2 | Web dựng phía máy chủ cho hành khách và nhân viên; ứng dụng Android gốc cho máy soát vé | Java 17, Spring Boot, Thymeleaf | Web: HTML dựng ở máy chủ, JavaScript nhẹ cho sơ đồ chỗ. Android: Kotlin, Room | PostgreSQL | Như CN1 |
| CN3 | Web SPA cho hành khách và nhân viên; ứng dụng soát vé là PWA cài được trên Android | Node.js, NestJS, TypeScript | Web: React, TypeScript. PWA: Service Worker, IndexedDB | PostgreSQL | Như CN1; đầu quét qua đầu vào bàn phím hoặc API trình duyệt (Q-54) |

| Tiêu chí (F1, ràng buộc P06, HE_THONG_NGOAI) | CN1 | CN2 | CN3 |
|---|---|---|---|
| F1-01 Chịu tải 2.000 phiên | Tốt: tệp tĩnh phục vụ riêng, API chỉ trả JSON | Trung bình: mỗi thao tác dựng lại trang ở máy chủ | Tốt: như CN1 |
| F1-02 Không trùng chỗ | Tốt: PostgreSQL có giao dịch và ràng buộc duy nhất | Tốt: như CN1 | Tốt: như CN1 |
| F1-03, NFR-05 Soát vé khi mất sóng trên máy Android | Tốt: ứng dụng gốc cài đặt, CSDL cục bộ bền | Tốt: như CN1 | Trung bình: PWA phụ thuộc trình duyệt của máy (model chưa biết, Q-54), kho cục bộ có thể bị trình duyệt xoá |
| F1-04 Không lưu thông tin thẻ | Tốt: không khác biệt giữa ba phương án, do cổng xử lý thẻ | Tốt: như CN1 | Tốt: như CN1 |
| HE_THONG_NGOAI (API thanh toán chưa có tài liệu, API SMS là REST) | Trung bình: gọi REST qua HTTPS, chưa kiểm chứng được thư viện của đối tác (Q-24) | Trung bình: như CN1 | Trung bình: như CN1 |
| Dùng chung mã miền giữa máy chủ và máy soát vé (logic soát vé giống nhau ở hai nơi) | Tốt: cùng nền JVM, dùng chung mô-đun miền | Tốt: như CN1 | Kém: hai bản cài đặt bằng hai nền tảng |
| Mức phù hợp quy mô (ASM-58) | Trung bình: ba công nghệ (Java, TypeScript, Kotlin) | Trung bình: hai công nghệ chính nhưng giao diện kém linh hoạt | Tốt: một ngôn ngữ chính |

Phương án khuyến nghị: CN1. Lý do: đạt Tốt ở các tiêu chí trọng số cao (F1-01, F1-02, F1-03), SPA phù hợp sơ đồ chỗ tương tác và cho phép phục vụ tệp tĩnh riêng khi tải cao dịp Tết, nền JVM cho phép dùng chung mô-đun miền giữa máy chủ và máy soát vé. Chi phí: ba công nghệ cần ba nhóm kỹ năng (giảm thiểu: Kotlin và Java cùng nền JVM).

Phương án được dùng cho các bước còn lại: CN1. Trạng thái: Khuyến nghị - chờ người dùng xác nhận.

## F3. Quyết định kiến trúc

| Mục | Nội dung |
|---|---|
| Bối cảnh | Hệ thống bán vé và quản lý chuyến của nhà xe SaoViet: 12 tuyến, khoảng 80 chuyến mỗi ngày, khoảng 70 xe; ba loại client (website hành khách, giao diện nhân viên, ứng dụng soát vé trên máy Android); bốn hệ thống ngoài và thiết bị (ACT-06 đến ACT-09) cùng bộ định thời (ACT-10); yêu cầu quyết định: không trùng chỗ, chịu khoảng 2.000 phiên đồng thời, soát vé khi mất sóng (F1) |
| Quyết định (mẫu và cách kết hợp) | PA2: Front-end/Back-end. Back-end là một khối triển khai chia 3 layer logic (Application, Services, Domain) cộng layer Presentation cho các client. Client-server ở mức triển khai: máy chủ ứng dụng chạy một hoặc nhiều bản không giữ trạng thái, một cơ sở dữ liệu. Layered nới lỏng. Thứ tự layer từ trên xuống: Presentation, Application, Services, Domain. Domain đặt dưới cùng vì Persistence phải tham chiếu các lớp miền để ánh xạ, nên nếu Domain nằm trên Services thì Persistence phụ thuộc đi lên; interface kho dữ liệu do Domain định nghĩa, Persistence và DeviceStore hiện thực (đi xuống) |
| Mẫu cho phía giao diện (A3b) | Chọn sau khi có CN1. Web SPA: kiến trúc component kết hợp Flux (Redux Toolkit), vì SPA không có cơ chế data binding hai chiều sẵn. Ứng dụng Android: MVVM (View, ViewModel), vì nền tảng có data binding và cần kiểm thử logic trình bày không cần màn hình. REST controller của back-end là thành phần layer Application, không phải boundary giao diện người dùng |
| Công nghệ | Theo F2.2: CN1 (Khuyến nghị - chờ người dùng xác nhận): Java 17, Spring Boot; React, TypeScript, Redux Toolkit; Kotlin, Android, Room; PostgreSQL. Khối cập nhật hồ sơ ở F11 |
| Phương án đã loại và lý do | PA1: giao diện dựng phía máy chủ không phục vụ tốt client Android và sơ đồ chỗ tương tác. PA3: microservices và broker vượt quy mô (18 use case, nhóm nhỏ, không có yêu cầu phân tán), làm khó F1-02. Layered nghiêm ngặt: loại vì Application phải dùng trực tiếp đối tượng Domain và interface kho dữ liệu nằm ở Domain |
| Hệ quả tích cực | Một nơi duy nhất quyết định chỗ và vé (F1-02); nhân bản back-end dễ vì không giữ phiên; thay đổi API cổng thanh toán, cổng SMS giới hạn trong một package; mô-đun miền dùng chung với máy soát vé giữ quy tắc soát vé giống nhau |
| Hệ quả tiêu cực và cách giảm thiểu | Thêm lớp trung gian (Api, Application) làm mỗi yêu cầu đi qua nhiều layer: giữ Application mỏng, bộ nhớ đệm cho truy vấn sơ đồ chỗ. Ba công nghệ cần nhiều kỹ năng: Java và Kotlin cùng nền JVM. Nới lỏng layered cho phép Application gọi thẳng Domain: giảm thiểu bằng quy tắc F6 cấm Presentation phụ thuộc Domain và Services. Một khối triển khai nên lỗi một phần có thể ảnh hưởng toàn bộ: tách module theo package, kiểm thử tải trước dịp Tết |
| NFR được đáp ứng | NFR-01 (nhân bản không giữ phiên, giao diện tĩnh), NFR-02 (logic và dữ liệu soát vé trên máy), NFR-03 (dữ liệu thẻ không đi vào hệ thống), NFR-04, NFR-05 (hai loại client), NFR-06 đến NFR-10 (package tích hợp riêng); REQ-67 (một cơ sở dữ liệu có ràng buộc) |
| Rủi ro còn mở | (1) Loại client của nhân viên nhà xe chọn là web, nguồn không nêu: Q-78. (2) Cách máy in vé nhận dữ liệu (phần mềm trung gian ở máy trạm) chọn vì máy in đặt tại quầy: Q-79, Q-57. (3) Số bản chạy song song, hạ tầng đặt máy chủ, yêu cầu sẵn sàng: Q-80. (4) Cách đưa danh sách hành khách xuống máy soát vé chọn là máy tự lấy khi có sóng: Q-81. (5) Sai số của các mốc thời gian tự động: Q-82. (6) Hành khách nhập thẻ tại trang của cổng thanh toán (dự kiến): Q-83, Q-24. (7) Q-75: Seat lưu trạng thái theo ASM-42 nên TripCatalog không phụ thuộc Ticketing; nếu Q-75 trả lời "suy ra từ vé và lần đặt" thì Seat cần truy vấn Ticketing, tạo phụ thuộc vòng giữa PKG-22 và PKG-23, phải chạy lại P09. (8) P08 chưa phân tích 14 use case, các package AccountService, AccountModel, PricingReportService đặt theo P02 và có thể đổi khi có P07 của các use case đó. (9) Công nghệ ở trạng thái khuyến nghị chờ xác nhận |

## F4. Layer và package cấp cao

Layered nới lỏng: layer chỉ phụ thuộc layer nằm dưới nó trong thứ tự Presentation, Application, Services, Domain. Layer chứa package; phụ thuộc ở dòng layer được tổng hợp từ package bên trong. P10 tiếp tục cấp mã từ PKG-26.

| PKG | Tên | Layer | Trách nhiệm | Phụ thuộc vào (PKG) | Nguồn (NFR, UC nhóm, ACT) |
|---|---|---|---|---|---|
| PKG-01 | Presentation | - | Hiển thị thông tin, tiếp nhận thao tác của người dùng trên các ứng dụng phía người dùng. | PKG-02 | NFR-04, NFR-05; ACT-01 đến ACT-05 |
| PKG-02 | Application | - | Điều phối xử lý của từng use case trên các đối tượng miền. | PKG-03, PKG-04 | UC-001 đến UC-018; NFR-01 |
| PKG-03 | Services | - | Cung cấp dịch vụ kỹ thuật dùng chung: truy cập lưu trữ, giao tiếp hệ thống ngoài, thiết bị, định thời. | PKG-04 | NFR-06 đến NFR-10; ACT-06 đến ACT-10 |
| PKG-04 | Domain | - | Giữ các khái niệm nghiệp vụ cùng quy tắc nghiệp vụ gắn với chúng. | - | P08 (24 lớp phân tích); BR-01 đến BR-33 |
| PKG-05 | PassengerWeb | PKG-01 | Hiển thị website cho hành khách tìm chuyến, đặt vé, thanh toán, xem lịch sử vé. | PKG-08 | NFR-01, NFR-04; ACT-01; UC-001 đến UC-003, UC-007 đến UC-011 |
| PKG-06 | StaffWeb | PKG-01 | Hiển thị giao diện web cho nhân viên bán vé, nhân viên điều hành, quản lý nhà xe. | PKG-08 | ACT-02, ACT-03, ACT-04; UC-004 đến UC-008, UC-012, UC-013, UC-016 đến UC-018 |
| PKG-07 | CheckerAppUI | PKG-01 | Hiển thị màn hình soát vé trên máy soát vé cầm tay cho phụ xe. | PKG-11 | NFR-02, NFR-05, NFR-10; ACT-05; UC-015 |
| PKG-08 | RestApi | PKG-02 | Tiếp nhận yêu cầu của các ứng dụng client qua API, chuyển cho dịch vụ ứng dụng tương ứng. | PKG-09, PKG-10, PKG-11, PKG-12, PKG-13 | NFR-01, NFR-04, NFR-05; ACT-01 đến ACT-05 |
| PKG-09 | TicketSalesService | PKG-02 | Điều phối các use case bán vé: tìm chuyến, đặt vé, thanh toán, đổi vé, trả vé, đặt chỗ qua điện thoại. | PKG-15, PKG-16, PKG-17, PKG-19, PKG-22, PKG-23 | Nhóm Bán vé (UC-001 đến UC-008); NFR-06, NFR-07, NFR-08, NFR-09 |
| PKG-10 | TripOperationsService | PKG-02 | Điều phối các use case vận hành chuyến: xếp lịch chạy, huỷ chuyến, chuẩn bị danh sách hành khách. | PKG-15, PKG-16, PKG-19, PKG-22, PKG-23, PKG-24 | Nhóm Vận hành chuyến (UC-012 đến UC-014); NFR-07, NFR-08; ACT-10 |
| PKG-11 | BoardingCheckService | PKG-02 | Điều phối việc soát vé lên xe, kể cả khi máy soát vé không có kết nối mạng. | PKG-18, PKG-21, PKG-22, PKG-23, PKG-24 | UC-015; NFR-02 |
| PKG-12 | AccountService | PKG-02 | Điều phối đăng ký tài khoản, đăng nhập, xem lịch sử vé của hành khách. | PKG-23, PKG-25 | Nhóm Tài khoản hành khách (UC-009 đến UC-011) |
| PKG-13 | PricingReportService | PKG-02 | Điều phối đặt giá vé, đặt mức tăng giá lễ Tết, lập báo cáo kinh doanh. | PKG-22, PKG-23 | Nhóm Giá vé và báo cáo (UC-016 đến UC-018) |
| PKG-14 | Persistence | PKG-03 | Lưu, truy xuất các đối tượng miền trong cơ sở dữ liệu quan hệ ở máy chủ. | PKG-22, PKG-23, PKG-24, PKG-25 | NFR-01, NFR-03; REQ-67 (BR-02, BR-03) |
| PKG-15 | PaymentIntegration | PKG-03 | Che cổng thanh toán của đối tác sau interface thu tiền, hoàn tiền. | - | ACT-06; NFR-03, NFR-06, NFR-07 |
| PKG-16 | SmsIntegration | PKG-03 | Che cổng SMS của nhà mạng sau interface gửi tin nhắn. | - | ACT-07; NFR-08 |
| PKG-17 | PrinterIntegration | PKG-03 | Che máy in vé nhiệt sau interface in vé giấy có mã vạch. | - | ACT-08; NFR-09 |
| PKG-18 | ScannerIntegration | PKG-03 | Che đầu quét mã vạch của máy soát vé sau interface nhận mã vé. | - | ACT-09; NFR-10 |
| PKG-19 | Scheduling | PKG-03 | Kích hoạt xử lý tự động theo mốc thời gian của chuyến và của lần giữ chỗ. | - | ACT-10; BR-07, BR-08, BR-24, BR-33 |
| PKG-20 | DeviceStore | PKG-03 | Lưu cục bộ trên máy soát vé danh sách hành khách, kết quả soát chưa gửi. | PKG-24 | NFR-02; UC-014, UC-015 |
| PKG-21 | ServerApiClient | PKG-03 | Gọi API của máy chủ từ máy soát vé để nhận danh sách hành khách, gửi kết quả soát. | - | NFR-02; UC-014, UC-015 |
| PKG-22 | TripCatalog | PKG-04 | Giữ khái niệm tuyến, chuyến, chỗ, giá vé theo tuyến và loại xe, mức tăng giá lễ Tết. | - | AC-E-Trip, AC-E-Route, AC-E-Seat, AC-E-BaseFare, AC-E-HolidaySurcharge; GL-02, GL-04, GL-09, GL-25, GL-36 |
| PKG-23 | Ticketing | PKG-04 | Giữ khái niệm lần đặt, vé, đặt chỗ qua điện thoại, khoản hoàn tiền. | PKG-22 | AC-E-Booking, AC-E-Ticket, AC-E-Refund, AC-E-PhoneReservation; GL-07, GL-16, GL-18, GL-37 |
| PKG-24 | BoardingModel | PKG-04 | Giữ khái niệm danh sách hành khách của chuyến, phiên soát vé. | PKG-22, PKG-23 | AC-E-TripPassengerList, AC-E-TicketCheckSession; GL-05, GL-28 |
| PKG-25 | AccountModel | PKG-04 | Giữ khái niệm tài khoản hành khách. | - | UC-009 đến UC-011 (chưa có lớp P08) |

Lý do tách Application và Domain: lớp entity của P08 mang nhiều quy tắc nghiệp vụ (BR-01 đến BR-33) dùng chung giữa nhiều use case và giữa máy chủ với máy soát vé, trong khi lớp control chỉ điều phối; tách giúp dùng chung mô-đun miền và kiểm thử quy tắc riêng.

Các package PKG-07, PKG-11, PKG-18, PKG-20, PKG-21 và mô-đun miền PKG-22 đến PKG-24 được triển khai trên máy soát vé; PKG-11 và các package Domain còn được dùng ở back-end khi nhận kết quả soát vé và chuẩn bị danh sách hành khách.

## F5. Quy tắc ánh xạ lớp phân tích sang kiến trúc

| Stereotype hoặc loại lớp phân tích | Layer hoặc vai trò trong mẫu đích | Ghi chú |
|---|---|---|
| Boundary giao diện người dùng, phía web (BookTicketForm, ReturnTicketForm, CounterReturnTicketForm, CancelTripForm) | View (component) và Store (Flux) trong PKG-05 hoặc PKG-06 ở Presentation; phần tiếp nhận yêu cầu là REST controller trong PKG-08 RestApi ở Application | "Controller" của REST và của MVC là thành phần giao diện, khác lớp control của phân tích. Tách theo tác nhân: ACT-01 vào PKG-05, ACT-02, ACT-03, ACT-04 vào PKG-06 |
| Boundary giao diện người dùng, phía Android (CheckBoardingTicketForm) | View và ViewModel (MVVM) trong PKG-07 ở Presentation | ViewModel là thành phần giao diện, khác lớp control CheckBoardingTicketController |
| Boundary kênh thông báo (email, SMS, thông báo đẩy) | P08 xếp SmsGateway vào giao diện hệ thống, áp dụng dòng boundary giao diện hệ thống bên dưới | Không có boundary kênh thông báo riêng trong P08 |
| Boundary giao diện hệ thống (SmsGateway, PaymentGateway) | Subsystem trong PKG-16 SmsIntegration, PKG-15 PaymentIntegration ở Services | Mỗi hệ thống ngoài một package, che sau interface (IF-nn ở P10) |
| Boundary giao diện thiết bị (BarcodeScanner) | Subsystem trong PKG-18 ScannerIntegration ở Services; máy in vé (ACT-08, chưa có lớp P08) dùng PKG-17 PrinterIntegration | Thiết bị gọi ngược lên control qua interface do Services định nghĩa (A5) |
| Control (BookTicketOnlineController, PayTicketOnlineController, ReturnTicketController) | Lớp dịch vụ ứng dụng trong PKG-09 TicketSalesService ở Application | PayTicketOnlineController đang ở trạng thái tạm trong P08 |
| Control (CancelTripController) | Lớp dịch vụ ứng dụng trong PKG-10 TripOperationsService | |
| Control (CheckBoardingTicketController) | Lớp dịch vụ ứng dụng trong PKG-11 BoardingCheckService, chạy trên máy soát vé | Trạng thái giữa hai lần quét lưu qua DeviceStore |
| Entity, phần hành vi nghiệp vụ (Trip, Route, Seat, BaseFare, HolidaySurcharge) | Lớp miền trong PKG-22 TripCatalog ở Domain | |
| Entity, phần hành vi nghiệp vụ (Booking, Ticket, Refund, PhoneReservation) | Lớp miền trong PKG-23 Ticketing | Ticket có 17 trách nhiệm (P08 F6), P10 cân nhắc tách |
| Entity, phần hành vi nghiệp vụ (TripPassengerList, TicketCheckSession) | Lớp miền trong PKG-24 BoardingModel | |
| Entity, phần lưu trữ | Interface kho dữ liệu đặt cùng package miền (PKG-22 đến PKG-25); hiện thực trong PKG-14 Persistence (máy chủ) hoặc PKG-20 DeviceStore (máy soát vé) | Realization đi từ Services xuống Domain |

## F6. Quy tắc phụ thuộc

- R1: Layered nới lỏng: một layer được phụ thuộc mọi layer nằm dưới. Lý do: Application cần dùng trực tiếp lớp Domain và dùng subsystem ở Services, nên không thể chỉ qua layer liền kề.
- R2: Layer dưới không phụ thuộc layer trên; không có mũi tên dependency hoặc realization đi lên.
- R3: Không có vòng phụ thuộc giữa các package, kể cả vòng qua nhiều package.
- R4: Presentation chỉ phụ thuộc PKG-08 RestApi (web) hoặc PKG-11 BoardingCheckService (ứng dụng soát vé); không phụ thuộc Services và Domain.
- R5: Layer dưới cần gọi ngược lên (kết quả thanh toán, mốc thời gian, mã vạch vừa quét) thì layer dưới định nghĩa interface, package ở layer trên hiện thực (E-09, E-12, E-17, E-21).
- R6: Interface kho dữ liệu do package Domain định nghĩa; Persistence và DeviceStore hiện thực, nên Application không phụ thuộc Persistence hay DeviceStore.
- R7: Package phụ thuộc vào interface của subsystem tích hợp (PKG-15 đến PKG-19, PKG-21), không phụ thuộc lớp bên trong.
- R8: Phụ thuộc giữa package Domain theo một chiều: BoardingModel --> Ticketing --> TripCatalog; AccountModel không phụ thuộc package Domain nào.

| Phụ thuộc (PKG --> PKG) | Hợp lệ | Quy tắc áp dụng |
|---|---|---|
| PKG-01 --> PKG-02 (layer, tổng hợp) | Có | R1, R2 |
| PKG-02 --> PKG-03 (layer, tổng hợp) | Có | R1, R2 |
| PKG-02 --> PKG-04 (layer, tổng hợp) | Có | R1, R2 |
| PKG-03 --> PKG-04 (layer, tổng hợp) | Có | R1, R2 |
| PKG-05 --> PKG-08 | Có | R1, R2, R4 |
| PKG-06 --> PKG-08 | Có | R1, R2, R4 |
| PKG-07 --> PKG-11 | Có | R1, R2, R4 |
| PKG-08 --> PKG-09 | Có | R3, R8 (cùng layer, một chiều) |
| PKG-08 --> PKG-10 | Có | R3, R8 (cùng layer, một chiều) |
| PKG-08 --> PKG-11 | Có | R3, R8 (cùng layer, một chiều) |
| PKG-08 --> PKG-12 | Có | R3, R8 (cùng layer, một chiều) |
| PKG-08 --> PKG-13 | Có | R3, R8 (cùng layer, một chiều) |
| PKG-09 --> PKG-15 | Có | R1, R2, R5 |
| PKG-09 --> PKG-16 | Có | R1, R2, R7 |
| PKG-09 --> PKG-17 | Có | R1, R2, R7 |
| PKG-09 --> PKG-19 | Có | R1, R2, R5 |
| PKG-09 --> PKG-22 | Có | R1, R2 |
| PKG-09 --> PKG-23 | Có | R1, R2 |
| PKG-10 --> PKG-15 | Có | R1, R2, R7 |
| PKG-10 --> PKG-16 | Có | R1, R2, R7 |
| PKG-10 --> PKG-19 | Có | R1, R2, R5 |
| PKG-10 --> PKG-22 | Có | R1, R2 |
| PKG-10 --> PKG-23 | Có | R1, R2 |
| PKG-10 --> PKG-24 | Có | R1, R2 |
| PKG-11 --> PKG-18 | Có | R1, R2, R5 |
| PKG-11 --> PKG-21 | Có | R1, R2, R7 |
| PKG-11 --> PKG-24 | Có | R1, R2 |
| PKG-11 --> PKG-23 | Có | R1, R2 |
| PKG-11 --> PKG-22 | Có | R1, R2 |
| PKG-12 --> PKG-25 | Có | R1, R2 |
| PKG-12 --> PKG-23 | Có | R1, R2 |
| PKG-13 --> PKG-22 | Có | R1, R2 |
| PKG-13 --> PKG-23 | Có | R1, R2 |
| PKG-14 --> PKG-22 | Có | R1, R2, R6 |
| PKG-14 --> PKG-23 | Có | R1, R2, R6 |
| PKG-14 --> PKG-24 | Có | R1, R2, R6 |
| PKG-14 --> PKG-25 | Có | R1, R2, R6 |
| PKG-20 --> PKG-24 | Có | R1, R2, R6 |
| PKG-23 --> PKG-22 | Có | R3, R8 (cùng layer, một chiều) |
| PKG-24 --> PKG-23 | Có | R3, R8 (cùng layer, một chiều) |
| PKG-24 --> PKG-22 | Có | R3, R8 (cùng layer, một chiều) |

## F7. Định hướng giao tiếp ngoài và dữ liệu

| ACT (hệ thống ngoài, thiết bị) | PKG chứa | Nguyên tắc cô lập | Rủi ro (lỗi, timeout, thay đổi API) |
|---|---|---|---|
| ACT-06 Cổng thanh toán | PKG-15 PaymentIntegration | Interface thu tiền, hoàn tiền; kết quả thanh toán trả về qua interface do PKG-15 định nghĩa, PKG-09 hiện thực; không chuyển dữ liệu thẻ vào hệ thống | API chưa có tài liệu (Q-24); không phản hồi (Q-55); kết quả trả về trùng hoặc đến muộn sau hết thời hạn giữ chỗ (Q-10); thay đổi API chỉ sửa PKG-15 |
| ACT-07 Cổng SMS | PKG-16 SmsIntegration | Interface gửi tin nhắn nhận số điện thoại và nội dung | Cổng báo lỗi hoặc không nhận (Q-56); thay đổi API chỉ sửa PKG-16 |
| ACT-08 Máy in vé | PKG-17 PrinterIntegration | Interface in vé nhận dữ liệu vé; phần điều khiển máy in chạy ở máy trạm tại quầy | Model, kết nối, định dạng chưa biết (Q-57, Q-79); máy in hết giấy hoặc mất kết nối |
| ACT-09 Đầu quét mã vạch | PKG-18 ScannerIntegration | Interface báo mã vé vừa quét lên BoardingCheckService qua interface do PKG-18 định nghĩa | Model đầu quét, loại mã vạch chưa biết (Q-54) |
| ACT-10 Bộ định thời | PKG-19 Scheduling | Interface mốc thời gian do PKG-19 định nghĩa, PKG-09 và PKG-10 hiện thực; mốc tính từ dữ liệu (thời điểm giữ chỗ, giờ xuất bến) | Nhiều bản back-end xử lý trùng một mốc; sai số mốc chưa quy định (Q-82) |
| Máy chủ (đối với máy soát vé) | PKG-21 ServerApiClient | Máy soát vé chỉ gọi API qua PKG-21; ứng dụng chạy tiếp khi gọi thất bại | Mất sóng, gửi lại kết quả; cách lấy danh sách hành khách (Q-81) |

| Mục | Quyết định | Lý do |
|---|---|---|
| Loại cơ chế lưu trữ | Quan hệ (PostgreSQL) ở máy chủ; SQLite cục bộ (Room) trên máy soát vé | Dữ liệu có quan hệ chặt giữa chuyến, chỗ, lần đặt, vé; REQ-67 cần ràng buộc và giao dịch. Thiết kế: CSDL cục bộ trên Android theo nền tảng |
| Layer truy cập dữ liệu | Interface kho dữ liệu ở Domain (PKG-22 đến PKG-25); cài đặt ở Services: PKG-14 (máy chủ), PKG-20 (máy soát vé) | Domain ở cuối thứ tự layer nên Services hiện thực interface đi xuống, không có phụ thuộc đi lên (F3, F6) |
| Chiến lược giao dịch mức cao | Mỗi lần đặt, phát hành vé, trả vé, huỷ chuyến là một giao dịch ACID; chống trùng chỗ bằng ràng buộc duy nhất cho chỗ của chuyến ở trạng thái có vé hoặc đang giữ, cộng cập nhật có điều kiện khi giữ chỗ | F1-02, BR-02, BR-03; hai tiến trình cùng chọn một chỗ chỉ một bên thành công |
| Trạng thái chờ giữa hai sự kiện | Không giữ trong bộ nhớ của back-end: thời điểm bắt đầu giữ chỗ và trạng thái lần đặt lưu trong Booking (holdStartTime, status); Scheduling duyệt dữ liệu để xử lý hết thời hạn giữ chỗ; trạng thái phiên soát vé lưu ở DeviceStore | F1-01 cần chạy nhiều bản song song và khởi động lại không mất trạng thái |
| Dữ liệu cần bảo vệ | Họ tên và số điện thoại người đi, mã vé, thông tin tài khoản hành khách: truyền qua kết nối mã hoá, mật khẩu tài khoản lưu dạng băm. Không lưu dữ liệu thẻ; mã tham chiếu giao dịch của cổng được lưu (ASM-41) | NFR-03, ASM-41, Q-53; Thiết kế: kết nối mã hoá theo mặc định cho dữ liệu cá nhân |

## F8. Kiểm tra chứa mô hình phân tích

| Nhóm lớp phân tích (theo stereotype hoặc nhóm chức năng) | Số lớp | Layer, PKG đích | Vấn đề |
|---|---|---|---|
| Boundary giao diện người dùng web, ACT-01 (BookTicketForm, ReturnTicketForm) | 2 | Presentation, PKG-05 | Không có |
| Boundary giao diện người dùng web, nhân viên (CounterReturnTicketForm, CancelTripForm) | 2 | Presentation, PKG-06 | Không có |
| Boundary giao diện người dùng, Android (CheckBoardingTicketForm) | 1 | Presentation, PKG-07 | Không có |
| Boundary giao diện hệ thống (SmsGateway, PaymentGateway) | 2 | Services, PKG-16, PKG-15 | PaymentGateway chưa có trách nhiệm thanh toán (P07 của UC-003 chưa có) |
| Boundary giao diện thiết bị (BarcodeScanner) | 1 | Services, PKG-18 | Không có |
| Control, nhóm Bán vé (BookTicketOnlineController, PayTicketOnlineController, ReturnTicketController) | 3 | Application, PKG-09 | PayTicketOnlineController ở trạng thái tạm; BookTicketOnlineController giữ chờ thanh toán giữa hai sự kiện, đã có Booking.holdStartTime và status nên không cần entity mới |
| Control, nhóm Vận hành chuyến (CancelTripController, CheckBoardingTicketController) | 2 | Application, PKG-10 (1), PKG-11 (1) | CheckBoardingTicketController chạy trên máy soát vé; TicketCheckSession.sendStatus lưu qua DeviceStore nên khởi động lại không mất trạng thái |
| Entity chuyến và giá (Trip, Route, Seat, BaseFare, HolidaySurcharge) | 5 | Domain, PKG-22 | Q-75 (trạng thái chỗ lưu hay suy ra) ảnh hưởng chiều phụ thuộc PKG-22 và PKG-23; P08 R-33 (Trip - PhoneReservation) cần điều hướng từ PhoneReservation sang Trip |
| Entity bán vé (Booking, Ticket, Refund, PhoneReservation) | 4 | Domain, PKG-23 | Ticket có 17 trách nhiệm (P08 F6); P10 cân nhắc tách |
| Entity soát vé (TripPassengerList, TicketCheckSession) | 2 | Domain, PKG-24 | R-34 (Trip - TripPassengerList) cần điều hướng từ TripPassengerList sang Trip |
| Tổng | 24 | | 8 boundary, 5 control, 11 entity |

Phần lưu trữ của 11 entity do PKG-14 (máy chủ) đảm nhận; TripPassengerList, TicketCheckSession, Ticket, Trip còn được lưu cục bộ qua PKG-20 trên máy soát vé. Các nhóm use case chưa có lớp phân tích (UC-001, UC-003 đến UC-007, UC-009 đến UC-012, UC-014, UC-016 đến UC-018) có chỗ trong PKG-09, PKG-10, PKG-12, PKG-13, PKG-25.

## F9. Package diagram

File diagrams/P09-package-layers.drawio, một trang. Mũi tên phụ thuộc đi từ trên xuống; không có mũi tên đi lên. Cạnh nhiều làn được định tuyến bằng điểm uốn trong bảng Edge; các cạnh đi xuống Domain từ Application đi qua lề phải của sơ đồ.

a) Bảng Node

| ID (PKG) | Loại (Package / Layer) | Nhãn | Stereotype | Thuộc về (PKG layer chứa) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-01 | Layer | Presentation | «layer» | - | Hiển thị thông tin, tiếp nhận thao tác của người dùng trên các ứng dụng phía người dùng. | 40 | 20 | 1860 | 160 |
| PKG-02 | Layer | Application | «layer» | - | Điều phối xử lý của từng use case trên các đối tượng miền. | 40 | 240 | 1860 | 580 |
| PKG-03 | Layer | Services | «layer» | - | Cung cấp dịch vụ kỹ thuật dùng chung: truy cập lưu trữ, giao tiếp hệ thống ngoài, thiết bị, định thời. | 40 | 880 | 1860 | 180 |
| PKG-04 | Layer | Domain | «layer» | - | Giữ các khái niệm nghiệp vụ cùng quy tắc nghiệp vụ gắn với chúng. | 40 | 1100 | 1860 | 400 |
| PKG-05 | Package | PassengerWeb | - | PKG-01 | Hiển thị website cho hành khách tìm chuyến, đặt vé, thanh toán, xem lịch sử vé. | 540 | 80 | 170 | 60 |
| PKG-06 | Package | StaffWeb | - | PKG-01 | Hiển thị giao diện web cho nhân viên bán vé, nhân viên điều hành, quản lý nhà xe. | 1000 | 80 | 170 | 60 |
| PKG-07 | Package | CheckerAppUI | - | PKG-01 | Hiển thị màn hình soát vé trên máy soát vé cầm tay cho phụ xe. | 80 | 80 | 170 | 60 |
| PKG-08 | Package | RestApi | - | PKG-02 | Tiếp nhận yêu cầu của các ứng dụng client qua API, chuyển cho dịch vụ ứng dụng tương ứng. | 770 | 300 | 170 | 60 |
| PKG-09 | Package | TicketSalesService | - | PKG-02 | Điều phối các use case bán vé: tìm chuyến, đặt vé, thanh toán, đổi vé, trả vé, đặt chỗ qua điện thoại. | 540 | 480 | 170 | 60 |
| PKG-10 | Package | TripOperationsService | - | PKG-02 | Điều phối các use case vận hành chuyến: xếp lịch chạy, huỷ chuyến, chuẩn bị danh sách hành khách. | 1000 | 480 | 170 | 60 |
| PKG-11 | Package | BoardingCheckService | - | PKG-02 | Điều phối việc soát vé lên xe, kể cả khi máy soát vé không có kết nối mạng. | 80 | 480 | 170 | 60 |
| PKG-12 | Package | AccountService | - | PKG-02 | Điều phối đăng ký tài khoản, đăng nhập, xem lịch sử vé của hành khách. | 1460 | 480 | 170 | 60 |
| PKG-13 | Package | PricingReportService | - | PKG-02 | Điều phối đặt giá vé, đặt mức tăng giá lễ Tết, lập báo cáo kinh doanh. | 1690 | 480 | 170 | 60 |
| PKG-14 | Package | Persistence | - | PKG-03 | Lưu, truy xuất các đối tượng miền trong cơ sở dữ liệu quan hệ ở máy chủ. | 1690 | 940 | 170 | 60 |
| PKG-15 | Package | PaymentIntegration | - | PKG-03 | Che cổng thanh toán của đối tác sau interface thu tiền, hoàn tiền. | 540 | 940 | 170 | 60 |
| PKG-16 | Package | SmsIntegration | - | PKG-03 | Che cổng SMS của nhà mạng sau interface gửi tin nhắn. | 770 | 940 | 170 | 60 |
| PKG-17 | Package | PrinterIntegration | - | PKG-03 | Che máy in vé nhiệt sau interface in vé giấy có mã vạch. | 1000 | 940 | 170 | 60 |
| PKG-18 | Package | ScannerIntegration | - | PKG-03 | Che đầu quét mã vạch của máy soát vé sau interface nhận mã vé. | 80 | 940 | 170 | 60 |
| PKG-19 | Package | Scheduling | - | PKG-03 | Kích hoạt xử lý tự động theo mốc thời gian của chuyến và của lần giữ chỗ. | 1230 | 940 | 170 | 60 |
| PKG-20 | Package | DeviceStore | - | PKG-03 | Lưu cục bộ trên máy soát vé danh sách hành khách, kết quả soát chưa gửi. | 1460 | 940 | 170 | 60 |
| PKG-21 | Package | ServerApiClient | - | PKG-03 | Gọi API của máy chủ từ máy soát vé để nhận danh sách hành khách, gửi kết quả soát. | 310 | 940 | 170 | 60 |
| PKG-22 | Package | TripCatalog | - | PKG-04 | Giữ khái niệm tuyến, chuyến, chỗ, giá vé theo tuyến và loại xe, mức tăng giá lễ Tết. | 80 | 1340 | 300 | 60 |
| PKG-23 | Package | Ticketing | - | PKG-04 | Giữ khái niệm lần đặt, vé, đặt chỗ qua điện thoại, khoản hoàn tiền. | 480 | 1340 | 300 | 60 |
| PKG-24 | Package | BoardingModel | - | PKG-04 | Giữ khái niệm danh sách hành khách của chuyến, phiên soát vé. | 880 | 1340 | 300 | 60 |
| PKG-25 | Package | AccountModel | - | PKG-04 | Giữ khái niệm tài khoản hành khách. | 1280 | 1340 | 300 | 60 |

b) Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ (Dependency) | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | PKG-05 | PKG-08 | Dependency | - | - | (620,200); (830,200) |
| E-02 | PKG-06 | PKG-08 | Dependency | - | - | (1080,210); (880,210) |
| E-03 | PKG-07 | PKG-11 | Dependency | - | - | - |
| E-04 | PKG-08 | PKG-09 | Dependency | - | - | (830,410); (620,410) |
| E-05 | PKG-08 | PKG-10 | Dependency | - | - | (850,440); (1080,440) |
| E-06 | PKG-08 | PKG-11 | Dependency | - | - | (800,400); (130,400) |
| E-07 | PKG-08 | PKG-12 | Dependency | - | - | (880,430); (1540,430) |
| E-08 | PKG-08 | PKG-13 | Dependency | - | - | (910,420); (1770,420) |
| E-09 | PKG-09 | PKG-15 | Dependency | - | PKG-09 hiện thực interface nhận kết quả thanh toán do PKG-15 định nghĩa | (560,720); (600,720) |
| E-10 | PKG-09 | PKG-16 | Dependency | - | - | (590,730); (830,730) |
| E-11 | PKG-09 | PKG-17 | Dependency | - | - | (610,740); (1080,740) |
| E-12 | PKG-09 | PKG-19 | Dependency | - | PKG-09 hiện thực interface mốc thời gian do PKG-19 định nghĩa | (640,750); (1290,750) |
| E-13 | PKG-09 | PKG-22 | Dependency | - | - | (660,610); (2010,610); (2010,1260); (180,1260) |
| E-14 | PKG-09 | PKG-23 | Dependency | - | - | (690,620); (2000,620); (2000,1250); (570,1250) |
| E-15 | PKG-10 | PKG-15 | Dependency | - | - | (1020,760); (650,760) |
| E-16 | PKG-10 | PKG-16 | Dependency | - | - | (1050,770); (880,770) |
| E-17 | PKG-10 | PKG-19 | Dependency | - | PKG-10 hiện thực interface mốc thời gian do PKG-19 định nghĩa | (1070,780); (1340,780) |
| E-18 | PKG-10 | PKG-22 | Dependency | - | - | (1100,630); (1990,630); (1990,1240); (230,1240) |
| E-19 | PKG-10 | PKG-23 | Dependency | - | - | (1120,640); (1980,640); (1980,1230); (610,1230) |
| E-20 | PKG-10 | PKG-24 | Dependency | - | - | (1150,650); (1970,650); (1970,1220); (1060,1220) |
| E-21 | PKG-11 | PKG-18 | Dependency | - | PKG-11 hiện thực interface nhận mã vé do PKG-18 định nghĩa | (110,700); (160,700) |
| E-22 | PKG-11 | PKG-21 | Dependency | - | - | (140,710); (390,710) |
| E-23 | PKG-11 | PKG-24 | Dependency | - | - | (160,580); (2040,580); (2040,1290); (1120,1290) |
| E-24 | PKG-11 | PKG-23 | Dependency | - | - | (190,590); (2030,590); (2030,1280); (650,1280) |
| E-25 | PKG-11 | PKG-22 | Dependency | - | - | (220,600); (2020,600); (2020,1270); (280,1270) |
| E-26 | PKG-12 | PKG-25 | Dependency | - | - | (1520,660); (1960,660); (1960,1210); (1480,1210) |
| E-27 | PKG-12 | PKG-23 | Dependency | - | - | (1570,670); (1950,670); (1950,1200); (690,1200) |
| E-28 | PKG-13 | PKG-22 | Dependency | - | - | (1750,680); (1940,680); (1940,1190); (330,1190) |
| E-29 | PKG-13 | PKG-23 | Dependency | - | - | (1800,690); (1930,690); (1930,1180); (740,1180) |
| E-30 | PKG-14 | PKG-22 | Dependency | - | PKG-14 hiện thực interface kho dữ liệu do PKG-22 định nghĩa | (1720,1130); (130,1130) |
| E-31 | PKG-14 | PKG-23 | Dependency | - | PKG-14 hiện thực interface kho dữ liệu do PKG-23 định nghĩa | (1760,1140); (520,1140) |
| E-32 | PKG-14 | PKG-24 | Dependency | - | PKG-14 hiện thực interface kho dữ liệu do PKG-24 định nghĩa | (1790,1150); (1000,1150) |
| E-33 | PKG-14 | PKG-25 | Dependency | - | PKG-14 hiện thực interface kho dữ liệu do PKG-25 định nghĩa | (1830,1170); (1380,1170) |
| E-34 | PKG-20 | PKG-24 | Dependency | - | PKG-20 hiện thực interface kho dữ liệu do PKG-24 định nghĩa | (1540,1160); (940,1160) |
| E-35 | PKG-23 | PKG-22 | Dependency | - | - | - |
| E-36 | PKG-24 | PKG-23 | Dependency | - | - | - |
| E-37 | PKG-24 | PKG-22 | Dependency | - | - | (1030,1440); (230,1440) |

## F10. Deployment diagram

File diagrams/P09-deployment.drawio. Hệ thống có từ hai node thực thi (máy chủ ứng dụng, máy chủ cơ sở dữ liệu) và các node client.

a) Bảng Node

| ID | Loại (Node / Artifact) | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| D-01 | Node | Trình duyệt của hành khách | «device» | - | Máy của hành khách (ACT-01) | 40 | 40 | 300 | 140 |
| A-01 | Artifact | Ứng dụng web hành khách | «artifact» | D-01 | PKG-05 | 20 | 60 | 200 | 50 |
| D-02 | Node | Máy trạm tại quầy | «device» | - | Máy của nhân viên bán vé, nhân viên điều hành, quản lý (ACT-02, ACT-03, ACT-04) | 40 | 260 | 300 | 200 |
| A-02 | Artifact | Ứng dụng web nhân viên | «artifact» | D-02 | PKG-06 | 20 | 60 | 200 | 50 |
| A-03 | Artifact | Phần mềm trung gian in vé | «artifact» | D-02 | PKG-17 | 20 | 120 | 200 | 50 |
| D-03 | Node | Máy in vé nhiệt | «device» | - | ACT-08, nối cục bộ với máy trạm (Q-79) | 40 | 540 | 300 | 100 |
| D-04 | Node | Máy soát vé cầm tay Android | «device» | - | Thiết bị của phụ xe (ACT-05), có đầu quét mã vạch (ACT-09) | 40 | 720 | 300 | 260 |
| A-04 | Artifact | Ứng dụng soát vé | «artifact» | D-04 | PKG-07, PKG-11, PKG-18, PKG-21 | 20 | 60 | 200 | 50 |
| A-05 | Artifact | Cơ sở dữ liệu cục bộ | «artifact» | D-04 | PKG-20 | 20 | 120 | 200 | 50 |
| A-06 | Artifact | Mô-đun miền dùng chung | «artifact» | D-04 | PKG-22, PKG-23, PKG-24 | 20 | 180 | 200 | 50 |
| D-05 | Node | Máy chủ ứng dụng | «execution environment» | - | Một hoặc nhiều bản chạy song song, không giữ trạng thái phiên (Q-80) | 600 | 300 | 320 | 240 |
| A-07 | Artifact | Ứng dụng phía máy chủ | «artifact» | D-05 | PKG-08 đến PKG-16, PKG-19, PKG-22 đến PKG-25 | 20 | 60 | 220 | 50 |
| A-08 | Artifact | Tệp giao diện web tĩnh | «artifact» | D-05 | PKG-05, PKG-06 | 20 | 120 | 220 | 50 |
| D-06 | Node | Máy chủ cơ sở dữ liệu | «execution environment» | - | Hệ quản trị CSDL quan hệ | 600 | 640 | 320 | 140 |
| A-09 | Artifact | Cơ sở dữ liệu của hệ thống | «artifact» | D-06 | PKG-14 truy cập | 20 | 60 | 220 | 50 |
| D-07 | Node | Cổng thanh toán của đối tác | «external system» | - | ACT-06, hệ thống ngoài | 1180 | 40 | 300 | 140 |
| D-08 | Node | Cổng SMS của nhà mạng | «external system» | - | ACT-07, hệ thống ngoài | 1180 | 350 | 300 | 140 |

b) Bảng Edge (communication path)

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú |
|---|---|---|---|---|---|
| DE-01 | D-01 | D-05 | Communication path | Internet, mã hoá | Hành khách dùng website |
| DE-02 | D-02 | D-05 | Communication path | Internet, mã hoá | Nhân viên dùng ứng dụng web |
| DE-03 | D-04 | D-05 | Communication path | Mạng di động, mã hoá | Máy soát vé gọi API khi có sóng |
| DE-04 | D-02 | D-03 | Communication path | Kết nối cục bộ | Máy in nhận dữ liệu vé từ phần mềm trung gian |
| DE-05 | D-05 | D-06 | Communication path | Mạng nội bộ | Truy cập cơ sở dữ liệu |
| DE-06 | D-05 | D-08 | Communication path | Internet, mã hoá | Gửi tin nhắn qua API REST |
| DE-07 | D-05 | D-07 | Communication path | Internet, mã hoá | Gửi yêu cầu thanh toán, hoàn tiền |
| DE-08 | D-01 | D-07 | Communication path | Internet, mã hoá | Dự kiến: chuyển hành khách sang trang thanh toán của cổng (Q-83) |

## F11. Cập nhật hồ sơ dự án

Dán khối sau vào project-profile.md mục 3, thay hai dòng NEN_TANG và CONG_NGHE hiện có:

```text
| Trường | Giá trị |
|---|---|
| NEN_TANG | Web (website cho hành khách, giao diện web cho nhân viên nhà xe) và ứng dụng Android cho máy soát vé cầm tay |
| CONG_NGHE | Phía máy chủ: Java 17, Spring Boot (REST); phía giao diện web: React, TypeScript, Redux Toolkit; ứng dụng soát vé: Kotlin, Android, Room (SQLite); hệ quản trị CSDL: PostgreSQL |
```

Trạng thái: Khuyến nghị - chờ người dùng xác nhận. Cập nhật project-profile.md trước khi chạy P10. Nếu chọn CN2 hoặc CN3, chạy lại P09 với PHUONG_AN_DA_CHON.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-78 | Nhân viên bán vé, nhân viên điều hành, quản lý nhà xe dùng ứng dụng web trên trình duyệt hay ứng dụng cài đặt trên máy? (Web trên trình duyệt / Ứng dụng cài đặt) | F2.2, F3, PKG-06; P11a | Mục 4, 6, 7, 9 nêu chức năng của nhân viên nhưng không nêu loại client; NFR-04 chỉ nêu website cho hành khách |
| Q-79 | Máy in vé nhiệt nối với máy nào ở quầy và nhận dữ liệu vé bằng cách nào? (Nối máy trạm của nhân viên qua phần mềm trung gian / Nối mạng, nhận trực tiếp từ máy chủ) | PKG-17, F10 (D-02, D-03); P10, P11b | Mục 4, câu 1: "in vé giấy có mã vạch"; HE_THONG_NGOAI: "Máy in vé nhiệt tại quầy"; liên quan Q-57 |
| Q-80 | Hệ thống đặt trên hạ tầng nào (máy chủ của nhà xe hay thuê ngoài) và có yêu cầu sẵn sàng, số bản chạy song song tối thiểu không? (Một bản / Nhiều bản với mức sẵn sàng do bên liên quan chọn) | F10 (D-05), F3 | Mục 10 chỉ nêu "chịu được khoảng 2.000 người truy cập cùng lúc"; P06 không có NFR sẵn sàng |
| Q-81 | Danh sách hành khách của chuyến đến máy soát vé theo cách nào lúc 15 phút trước giờ xuất bến: máy tự lấy khi có sóng hay máy chủ đẩy xuống, và xử lý thế nào nếu máy đang mất sóng lúc đó? (Máy tự lấy / Máy chủ đẩy xuống) | PKG-21, PKG-08, PKG-10; UC-014; P11b | Mục 8, câu 4: "hệ thống gửi danh sách hành khách của chuyến về máy soát vé"; liên quan Q-11 |
| Q-82 | Các xử lý tự động theo mốc thời gian (hết 10 phút giữ chỗ, 60 phút huỷ đặt chỗ, 15 phút gửi danh sách) được phép chậm tối đa bao lâu so với mốc? | PKG-19, F1-08 | Mục 3 câu 2, Mục 4 câu 2, Mục 8 câu 4 nêu mốc nhưng không nêu sai số |
| Q-83 | Hành khách nhập thông tin thẻ tại trang của cổng thanh toán (chuyển hướng hoặc nhúng của cổng) hay tại trang của hệ thống chuyển tiếp cho cổng? (Trang của cổng / Trang của hệ thống) | F1-04, PKG-05, PKG-15; NFR-03 | Mục 3 câu 1 và Mục 10 câu 3; API cổng thanh toán chưa có tài liệu (Q-24) |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-57 | Thứ tự ưu tiên thuộc tính chất lượng khi chọn kiến trúc: (1) toàn vẹn dữ liệu chỗ và vé (không trùng chỗ), (2) hiệu năng khi tải cao, (3) độ tin cậy của soát vé khi mất sóng, khả năng dùng nhiều loại client và định thời tự động, (4) bảo mật dữ liệu thẻ, (5) khả năng thay đổi phần tích hợp ngoài | P06 không xếp hạng NFR và TIEU_CHI_UU_TIEN không có; REQ-67 là ràng buộc cứng "không được", nguồn nêu tải cao là dịp Tết | F1; F2.1; F2.2 |
| ASM-58 | Dự án do một nhóm phát triển nhỏ thực hiện và vận hành, không có yêu cầu triển khai phân tán nhiều tổ chức | Nguồn không nêu quy mô nhóm; cần để đánh giá mức phù hợp quy mô và loại microservices | F2.1, F2.2, F3 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P08 | R-33, R-34, R-36 | Quan hệ vẽ từ Trip tới PhoneReservation và TripPassengerList; nếu P12 chọn điều hướng từ Trip sang hai lớp này thì PKG-22 phụ thuộc PKG-23, PKG-24, tạo vòng phụ thuộc | Ghi điều hướng từ PhoneReservation, TripPassengerList sang Trip khi chạy lại P08 hoặc ở P12 |
| P05 | Thiếu thuật ngữ "Tài khoản hành khách" | UC-009 đến UC-011 và PKG-25 AccountModel dùng khái niệm này nhưng P05 không có GL riêng | Bổ sung thuật ngữ khi chạy lại P05 |

## Vấn đề còn mở

- Target 7 đạt cho 24 lớp của P08; 14 use case chưa có P07, nên AccountService, AccountModel, PricingReportService, mô hình dữ liệu của lịch chạy (xe, tài xế) chỉ là chỗ đặt theo P02. Cần chạy lại P09 hoặc rà lại khi P08 phủ đủ.
- Chọn giữa hai quy tắc (C9): A4 và ví dụ F5 đặt Domain trên Services, còn A5 và F6 cấm phụ thuộc đi lên; Persistence cần tham chiếu lớp miền để ánh xạ. Đã chọn thứ tự Presentation, Application, Services, Domain để tuân F6 (quy tắc ưu tiên hơn ví dụ).
- Công nghệ ở trạng thái khuyến nghị chờ xác nhận; F11 chưa được dán vào project-profile.md.
- Target 9: bố cục được kiểm bằng tính toán toạ độ (không node chồng nhau, khoảng cách tối thiểu 40, không cạnh cắt qua node, mọi toạ độ là bội số của 10); chưa mở bằng draw.io để xem nhãn.
- Sơ đồ deployment: DE-08 (hành khách tới trang thanh toán của cổng) là dự kiến theo Q-83; kết nối máy in và vị trí phần mềm trung gian theo Q-79.
