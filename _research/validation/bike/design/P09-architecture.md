# P09 - Thiết kế kiến trúc - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P09 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE "Chưa chốt"); P01-actors.md 1.0; P02-usecases.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P08-analysis-model.md 1.0 |
| Phạm vi | Toàn hệ thống |

Placeholder: RANG_BUOC_KIEN_TRUC = Không có; TIEU_CHI_UU_TIEN = Không có; YEU_CAU_BO_SUNG = Không có.

## F1. Yêu cầu có ý nghĩa kiến trúc

| STT | Nguồn (NFR, ràng buộc, ACT) | Kịch bản thuộc tính chất lượng (kích thích --> phản hồi --> thước đo) | Mức ưu tiên | Ảnh hưởng kiến trúc |
|---|---|---|---|---|
| 1 | NFR-02, ACT-08 | Người thuê xe quét mã QR --> hệ thống kiểm tra, tạm giữ tiền, gửi lệnh mở khoá tới ụ --> lệnh tới ụ trong không quá 2 giây (phạm vi gồm tạm giữ hay không: Q-13; điều kiện tải: Q-28) | Cao | Đường xử lý đồng bộ ngắn nhất có thể; gửi lệnh tới ụ qua kênh đẩy (MQTT) không qua hàng đợi chậm; mọi gọi ra ngoài có timeout |
| 2 | NFR-03 | 1.500 chuyến đi đang diễn ra đồng thời --> hệ thống vẫn phục vụ thuê, trả xe --> tiêu chí "phục vụ được" chờ Q-14 | Cao | Máy chủ ứng dụng không giữ trạng thái phiên để nhân bản được; mỗi chuyến có hai mốc thời gian (60 giây, 24 giờ) cần bộ định thời bền vững, không phụ thuộc bộ nhớ một tiến trình |
| 3 | NFR-07, ACT-08 | Ụ khoá gửi báo xe rút ra, xe đưa vào qua MQTT --> hệ thống xử lý sự kiện UC-005, UC-007, UC-014 --> đúng giao thức nhà cung cấp (tài liệu chưa có) | Cao | Cô lập giao tiếp thiết bị sau một interface; sự kiện từ thiết bị đi ngược từ layer dịch vụ kỹ thuật lên layer ứng dụng cần cơ chế callback không tạo phụ thuộc ngược |
| 4 | NFR-06, ACT-07 | Hệ thống gọi tạm giữ, thu, huỷ, hoàn tiền --> cổng chấp nhận --> hành vi khi cổng lỗi chờ Q-08, Q-23 | Cao | Cô lập cổng thanh toán sau một interface; thay cổng hoặc API không ảnh hưởng nghiệp vụ |
| 5 | NFR-04 | Có yêu cầu đọc dữ liệu của hệ thống --> không nơi nào chứa số thẻ --> 0 bản ghi chứa số thẻ | Cao | Chỉ lớp tích hợp cổng thanh toán thấy dữ liệu thẻ trong luồng liên kết (UC-002); lưu trữ chỉ giữ mã tham chiếu |
| 6 | NFR-05, ACT-01 đến ACT-06 | Người thuê xe dùng ứng dụng di động; nhân viên và ban giám đốc dùng client chưa quy định (Q-35) --> các client dùng chung dịch vụ | Trung bình | Tách front-end (hai loại client) khỏi back-end dùng chung |
| 7 | NFR-01, ACT-08 | Ụ khoá báo thay đổi xe --> bản đồ trạm phản ánh --> độ trễ chờ Q-12 | Trung bình | Cần kênh cập nhật số xe, số ụ trống từ back-end tới client; chọn đẩy hay kéo khi Q-12 có câu trả lời |
| 8 | ACT-09, BR-06, BR-09 | Mốc 60 giây và 24 giờ tới --> hệ thống xử lý UC-005 6a, UC-009 --> không bỏ sót mốc khi máy chủ khởi động lại | Trung bình | Package Scheduling lưu mốc thời gian bền vững và gọi ngược layer ứng dụng qua interface |

## F2. Phương án và so sánh

| PA | Mẫu kiến trúc (và kết hợp) | Mô tả ngắn | Điều kiện phù hợp |
|---|---|---|---|
| PA1 | Front-end/Back-end; back-end Multi-layer 4 layer (Presentation, Application, Domain, TechnicalServices), một tiến trình triển khai nhân bản được; front-end di động MVVM, web nhân viên MVC passive; thiết bị qua MQTT broker | Một back-end dùng chung, chia package theo nhóm chức năng; tích hợp ngoài ở layer dịch vụ kỹ thuật | Một nhóm phát triển, khoảng 24 use case, cần dễ bảo trì và cô lập tích hợp |
| PA2 | Microservices kết hợp Broker (dịch vụ Thuê trả xe, Thanh toán, Thiết bị, Đội xe, Chăm sóc khách hàng) | Mỗi nhóm chức năng một dịch vụ, giao tiếp qua message broker | Nhiều nhóm độc lập, yêu cầu mở rộng riêng từng phần |
| PA3 | Client-server hai tầng: ứng dụng di động và web truy cập trực tiếp CSDL, một dịch vụ nhỏ nhận MQTT | Logic nghiệp vụ nằm ở client | Hệ thống nội bộ nhỏ, không có tích hợp thanh toán |

| Tiêu chí (từ F1) | Trọng số | PA1 | PA2 | PA3 |
|---|---|---|---|---|
| 1. Mở khoá trong 2 giây | 3 | Tốt: một tiến trình, gọi trong bộ nhớ, chỉ hai lời gọi ra ngoài | Trung bình: thêm các chặng qua broker giữa dịch vụ | Kém: client phải tự điều phối cổng thanh toán và ụ |
| 2. 1.500 chuyến đồng thời | 3 | Tốt: back-end không trạng thái nhân bản được | Tốt: mở rộng từng dịch vụ | Kém: tải dồn vào CSDL dùng chung |
| 3. Tích hợp ụ khoá MQTT | 3 | Tốt: package DeviceIntegration cô lập | Tốt: dịch vụ Thiết bị riêng | Trung bình: dịch vụ MQTT tách rời nghiệp vụ |
| 4. Tích hợp cổng thanh toán | 3 | Tốt: package PaymentIntegration cô lập | Tốt | Kém: khoá API nằm ở client |
| 5. Không lưu số thẻ | 3 | Tốt: một điểm tiếp xúc | Tốt | Kém: client truy cập dữ liệu trực tiếp |
| 6. Nhiều loại client | 2 | Tốt: API dùng chung | Tốt | Trung bình |
| 8. Mốc thời gian bền vững | 2 | Tốt: Scheduling dùng CSDL chung | Trung bình: cần đồng bộ mốc giữa dịch vụ | Kém |
| Chi phí phát triển, vận hành (một nhóm) | 2 | Tốt | Kém: nhiều dịch vụ, broker, giám sát phân tán | Tốt |
| Kết luận | | Chọn | Loại: phức tạp vượt quy mô, không có yêu cầu phân tán theo nhóm | Loại: vi phạm NFR-04, NFR-06 về cô lập |

## F3. Quyết định kiến trúc

| Mục | Nội dung |
|---|---|
| Bối cảnh | Một back-end phục vụ ứng dụng di động (NFR-05), client của nhân viên (Q-35), khoảng 900-1.200 ụ khoá qua MQTT (NFR-07), cổng thanh toán (NFR-06); yêu cầu 2 giây (NFR-02) và 1.500 chuyến đồng thời (NFR-03). |
| Quyết định | PA1: Front-end/Back-end. Back-end Multi-layer nới lỏng 4 layer: Presentation (API), Application (dịch vụ ứng dụng theo nhóm chức năng), Domain (lớp miền), TechnicalServices (lưu trữ, tích hợp, lập lịch). Front-end: ứng dụng di động người thuê xe (MVVM), web cho nhân viên (MVC passive). Ụ khoá kết nối qua MQTT broker. |
| Phương án đã loại và lý do | PA2: chi phí vượt quy mô một nhóm, thêm độ trễ cho NFR-02. PA3: logic và khoá tích hợp ở client, vi phạm cô lập NFR-04, NFR-06. |
| Hệ quả tích cực | Cô lập hai tích hợp ngoài; một đường xử lý thuê xe trong một tiến trình; nhân bản được back-end. |
| Hệ quả tiêu cực và cách giảm thiểu | Một khối triển khai: lỗi một package ảnh hưởng toàn hệ thống --> tách package theo nhóm chức năng, quy tắc phụ thuộc F6 để tách được về sau. Nhân bản nhiều tiến trình làm mốc thời gian bị xử lý trùng --> Scheduling lưu mốc trong CSDL và nhận việc có khoá (quyết định chi tiết ở P12). |
| NFR được đáp ứng | NFR-02, NFR-03 (có điều kiện Q-14), NFR-04, NFR-05, NFR-06, NFR-07; NFR-01 chờ Q-12 |
| Rủi ro còn mở | Độ trễ cổng thanh toán nằm ngoài kiểm soát (Q-13); giao thức MQTT chưa có tài liệu (Q-36); client của nhân viên chưa quy định (Q-35). |

## F4. Layer và package cấp cao

| PKG | Tên | Layer | Trách nhiệm | Phụ thuộc vào (PKG) | Nguồn (NFR, UC nhóm, ACT) |
|---|---|---|---|---|---|
| PKG-01 | Presentation | - | Tiếp nhận tương tác của người dùng và client. | PKG-02 | NFR-05 |
| PKG-02 | Application | - | Điều phối các use case. | PKG-03, PKG-04 | P02 nhóm chức năng |
| PKG-03 | Domain | - | Giữ quy tắc nghiệp vụ trên dữ liệu miền. | - | P08 entity |
| PKG-04 | TechnicalServices | - | Cung cấp lưu trữ, tích hợp ngoài và lập lịch. | PKG-03 (qua interface do Domain định nghĩa) | NFR-06, NFR-07, ACT-09 |
| PKG-05 | RiderApp | PKG-01 | Giao diện di động của người thuê xe. | PKG-07 | NFR-05, ACT-01 |
| PKG-06 | StaffWeb | PKG-01 | Giao diện của nhân viên và ban giám đốc. | PKG-07 | ACT-02 đến ACT-06, Q-35 |
| PKG-07 | ApiEndpoints | PKG-01 | Tiếp nhận yêu cầu từ client và chuyển cho dịch vụ ứng dụng. | PKG-02 | NFR-05 |
| PKG-08 | Account | PKG-02 | Điều phối use case nhóm Tài khoản (UC-001 đến UC-003). | PKG-03, PKG-18 | UC-001 đến UC-003 |
| PKG-09 | Rental | PKG-02 | Điều phối use case nhóm Thuê trả xe (UC-004 đến UC-009). | PKG-03, PKG-18, PKG-19, PKG-20, PKG-21 | UC-004 đến UC-009 |
| PKG-10 | Maintenance | PKG-02 | Điều phối use case nhóm Bảo trì. | PKG-03 | UC-010, UC-011 |
| PKG-11 | Dispatch | PKG-02 | Điều phối use case nhóm Điều phối. | PKG-03, PKG-19 | UC-012 đến UC-015 |
| PKG-12 | CustomerCare | PKG-02 | Điều phối use case nhóm Chăm sóc khách hàng. | PKG-03, PKG-18 | UC-016 đến UC-018 |
| PKG-13 | Administration | PKG-02 | Điều phối use case nhóm Danh mục. | PKG-03 | UC-019 đến UC-023 |
| PKG-14 | Reporting | PKG-02 | Tổng hợp báo cáo hằng tuần. | PKG-03 | UC-024 |
| PKG-15 | RentalDomain | PKG-03 | Giữ quy tắc về tài khoản người thuê xe, chuyến đi, khoản tạm giữ. | PKG-16 | GL-04, GL-08, GL-13 |
| PKG-16 | FleetDomain | PKG-03 | Giữ quy tắc về trạm, ụ khoá, xe, lệnh điều chuyển. | - | GL-09, GL-19, GL-23, GL-25 |
| PKG-17 | Persistence | PKG-04 | Lưu và nạp đối tượng miền. | PKG-03 (hiện thực interface kho dữ liệu) | NFR-03 |
| PKG-18 | PaymentIntegration | PKG-04 | Giao tiếp với cổng thanh toán. | - | ACT-07, NFR-04, NFR-06 |
| PKG-19 | DeviceIntegration | PKG-04 | Giao tiếp với ụ khoá qua MQTT. | - | ACT-08, NFR-02, NFR-07 |
| PKG-20 | Notification | PKG-04 | Gửi email tới người thuê xe. | - | REQ-24, Q-19 |
| PKG-21 | Scheduling | PKG-04 | Lưu và kích hoạt mốc thời gian. | - | ACT-09, BR-06, BR-09 |

## F5. Quy tắc ánh xạ lớp phân tích sang kiến trúc

| Stereotype hoặc loại lớp phân tích | Layer hoặc vai trò trong mẫu đích | Ghi chú |
|---|---|---|
| boundary giao diện người dùng | PKG-01: View (và ViewModel) trong RiderApp hoặc StaffWeb, cùng endpoint tương ứng trong ApiEndpoints | "Controller" của MVC ở StaffWeb là thành phần giao diện, khác lớp control của phân tích |
| boundary giao diện hệ thống | PKG-04: subsystem trong PaymentIntegration, che sau interface | Sẽ thành SS ở P10 |
| boundary giao diện thiết bị | PKG-04: subsystem trong DeviceIntegration, che sau interface; sự kiện từ thiết bị gọi ngược qua interface listener do DeviceIntegration định nghĩa, Application hiện thực | Không tạo phụ thuộc DeviceIntegration --> Application |
| control | PKG-02: lớp dịch vụ ứng dụng trong package của nhóm chức năng | - |
| entity (phần hành vi nghiệp vụ) | PKG-03: lớp miền trong RentalDomain hoặc FleetDomain | - |
| entity (phần lưu trữ) | PKG-17: hiện thực interface kho dữ liệu do PKG-03 định nghĩa | - |
| Mốc thời gian (tác nhân ACT-09, thời hạn chờ 60 giây) | PKG-21: Scheduling gọi ngược qua interface listener do Scheduling định nghĩa | - |

## F6. Quy tắc phụ thuộc

- Kiểu layered: nới lỏng. Application được dùng trực tiếp TechnicalServices (tích hợp, lập lịch) mà không qua Domain, vì Domain không nên biết cổng thanh toán hay ụ khoá.
- Presentation chỉ phụ thuộc Application (không gọi Domain, TechnicalServices trực tiếp).
- Layer dưới không phụ thuộc layer trên, trừ PKG-17 Persistence phụ thuộc PKG-03 Domain qua interface kho dữ liệu do Domain định nghĩa (A5 cho phép, ghi rõ).
- Không có vòng phụ thuộc giữa các package.
- Thông tin ngược lên: DeviceIntegration và Scheduling định nghĩa interface listener trong chính package của mình; Application đăng ký lớp hiện thực. Phụ thuộc vẫn đi từ Application xuống.
- Package phụ thuộc vào interface của subsystem (PaymentIntegration, DeviceIntegration), không phụ thuộc lớp bên trong.

| Phụ thuộc (PKG --> PKG) | Hợp lệ | Quy tắc áp dụng |
|---|---|---|
| PKG-05 --> PKG-07 | Có | Cùng layer |
| PKG-06 --> PKG-07 | Có | Cùng layer |
| PKG-07 --> PKG-02 | Có | Xuống một layer |
| PKG-02 --> PKG-03 | Có | Xuống một layer |
| PKG-08 --> PKG-18 | Có | Nới lỏng, qua interface |
| PKG-09 --> PKG-18, PKG-19, PKG-20, PKG-21 | Có | Nới lỏng, qua interface |
| PKG-11 --> PKG-19 | Có | Nới lỏng, qua interface |
| PKG-12 --> PKG-18 | Có | Nới lỏng, qua interface |
| PKG-15 --> PKG-16 | Có | Cùng layer, một chiều |
| PKG-17 --> PKG-03 | Có (ngoại lệ) | Qua interface do layer trên định nghĩa |

## F7. Định hướng giao tiếp ngoài và dữ liệu

| ACT (hệ thống ngoài, thiết bị) | PKG chứa | Nguyên tắc cô lập | Rủi ro (lỗi, timeout, thay đổi API) |
|---|---|---|---|
| ACT-07 Cổng thanh toán | PKG-18 | Một interface cho 5 thao tác (liên kết thẻ, tạm giữ, thu, huỷ, hoàn); không lớp nào ngoài PKG-18 thấy định dạng API | Chưa có tài liệu API; timeout làm vượt 2 giây (Q-13); lỗi thu tiền chưa có quy định (Q-23) |
| ACT-08 Ụ khoá | PKG-19 | Một interface gửi lệnh (mở, khoá) và một interface listener nhận sự kiện (rút xe, nhận xe, thẻ nhân viên); nội dung MQTT (topic, định dạng) chỉ nằm trong PKG-19 | Chưa có tài liệu giao thức (Q-36); mất kết nối, thông điệp trùng hoặc đến muộn |
| Kênh email (Q-19) | PKG-20 | Một interface gửi email | Chưa rõ là dịch vụ ngoài hay tự gửi |

| Mục | Quyết định | Lý do |
|---|---|---|
| Loại cơ chế lưu trữ | CSDL quan hệ | Thuê, trả xe cần giao dịch nhất quán trên nhiều đối tượng (chuyến, xe, ụ, khoản tạm giữ); báo cáo hằng tuần cần truy vấn tổng hợp (UC-024). Sản phẩm cụ thể chưa chốt; tiêu chí: hỗ trợ giao dịch ACID, khoá hàng, truy vấn tổng hợp, sao lưu |
| Layer truy cập dữ liệu | PKG-17 Persistence trong TechnicalServices | F5 |
| Chiến lược giao dịch mức cao | Mỗi thao tác của use case là một giao dịch cục bộ; lời gọi cổng thanh toán nằm ngoài giao dịch CSDL, kết quả được ghi lại sau (tránh giữ khoá khi chờ mạng) | NFR-02, NFR-06 |
| Dữ liệu cần bảo vệ | Chỉ lưu mã tham chiếu thẻ; không ghi số thẻ vào nhật ký | NFR-04 |

## F8. Kiểm tra chứa mô hình phân tích

| Nhóm lớp phân tích | Số lớp | Layer, PKG đích | Vấn đề |
|---|---|---|---|
| boundary người dùng: RentBikeForm, ReturnBikeForm | 2 | PKG-05 RiderApp, PKG-07; ReturnBikeForm là email --> PKG-20 | ReturnBikeForm không phải giao diện màn hình (Q-19) |
| boundary người dùng: CreateTransferOrderForm | 1 | PKG-06 StaffWeb, PKG-07 | - |
| boundary hệ thống: PaymentGateway | 1 | PKG-18 | - |
| boundary thiết bị: DockDevice | 1 | PKG-19 | - |
| control của nhóm Thuê trả xe (RentBike, ReturnBike, RecordLostBike) | 3 | PKG-09 | - |
| control của nhóm Điều phối (CreateTransferOrder) | 1 | PKG-11 | - |
| entity RiderAccount, Trip, PaymentHold | 3 | PKG-15 | - |
| entity Station, Dock, Bike, TransferOrder | 4 | PKG-16 | - |

## F9. Package diagram

File diagrams/P09-package-layers.drawio.

| ID (PKG) | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| PKG-01 | Layer | Presentation | «layer» | - | y=40 |
| PKG-02 | Layer | Application | «layer» | - | y=300 |
| PKG-03 | Layer | Domain | «layer» | - | y=600 |
| PKG-04 | Layer | TechnicalServices | «layer» | - | y=860 |
| PKG-05, PKG-06, PKG-07 | Package | RiderApp, StaffWeb, ApiEndpoints | - | PKG-01 | - |
| PKG-08 đến PKG-14 | Package | Account, Rental, Maintenance, Dispatch, CustomerCare, Administration, Reporting | - | PKG-02 | - |
| PKG-15, PKG-16 | Package | RentalDomain, FleetDomain | - | PKG-03 | - |
| PKG-17 đến PKG-21 | Package | Persistence, PaymentIntegration, DeviceIntegration, Notification, Scheduling | - | PKG-04 | - |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú |
|---|---|---|---|---|---|
| D-01 | PKG-05 | PKG-07 | Dependency | - | - |
| D-02 | PKG-06 | PKG-07 | Dependency | - | - |
| D-03 | PKG-07 | PKG-02 | Dependency | - | Tới layer (mọi package bên trong) |
| D-04 | PKG-02 | PKG-03 | Dependency | - | Tới layer |
| D-05 | PKG-09 | PKG-18 | Dependency | - | - |
| D-06 | PKG-09 | PKG-19 | Dependency | - | - |
| D-07 | PKG-09 | PKG-20 | Dependency | - | - |
| D-08 | PKG-09 | PKG-21 | Dependency | - | - |
| D-09 | PKG-12 | PKG-18 | Dependency | - | - |
| D-10 | PKG-11 | PKG-19 | Dependency | - | - |
| D-11 | PKG-08 | PKG-18 | Dependency | - | - |
| D-12 | PKG-17 | PKG-03 | Dependency | Hiện thực interface kho dữ liệu do Domain định nghĩa | Mũi tên đi lên (ngoại lệ F6) |
| D-13 | PKG-15 | PKG-16 | Dependency | - | - |

## F10. Deployment diagram

File diagrams/P09-deployment.drawio.

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| N-01 | Node | Điện thoại người thuê xe | «device» | - | Artifact A-01 RiderApp |
| N-02 | Node | Máy tính nhân viên | «device» | - | Artifact A-02 StaffWeb (trình duyệt), Q-35 |
| N-03 | Node | Máy chủ ứng dụng | «execution environment» | - | Artifact A-03 CityBikeServer; nhân bản được (NFR-03) |
| N-04 | Node | Máy chủ CSDL | «device» | - | CSDL quan hệ |
| N-05 | Node | MQTT broker | «execution environment» | - | Q-36: broker do CityBike hay nhà cung cấp vận hành |
| N-06 | Node | Ụ khoá | «device» | - | ACT-08 |
| N-07 | Node | Cổng thanh toán ngân hàng | «external system» | - | ACT-07 |
| N-08 | Node | Kênh gửi email | «external system» | - | Q-19 |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú |
|---|---|---|---|---|---|
| CP-01 | N-01 | N-03 | Communication path | Internet, mã hoá | - |
| CP-02 | N-02 | N-03 | Communication path | Internet hoặc mạng nội bộ, mã hoá | Q-35 |
| CP-03 | N-03 | N-04 | Communication path | Mạng nội bộ | - |
| CP-04 | N-03 | N-05 | Communication path | Mạng nội bộ, MQTT | - |
| CP-05 | N-05 | N-06 | Communication path | MQTT qua mạng của nhà cung cấp | Q-36 |
| CP-06 | N-03 | N-07 | Communication path | Internet, mã hoá, API của ngân hàng | - |
| CP-07 | N-03 | N-08 | Communication path | Internet | - |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-35 | Nhân viên (chăm sóc khách hàng, bảo trì, điều phối), quản trị viên và ban giám đốc dùng hệ thống qua loại client nào (web, ứng dụng di động, ứng dụng desktop)? | PKG-06, N-02, P11a | Nguồn chỉ nêu ứng dụng di động cho người dùng (Mục 1) |
| Q-36 | MQTT broker do CityBike vận hành hay do nhà cung cấp thiết bị cung cấp; topic và định dạng thông điệp là gì? | PKG-19, N-05, P11b | Mục 14 "giao thức MQTT do nhà cung cấp thiết bị quy định" |

Liên quan: Q-12, Q-13, Q-14, Q-19, Q-28.

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 8: không chốt sản phẩm công nghệ (ngôn ngữ, framework, hệ quản trị CSDL, broker) vì hồ sơ ghi "Chưa chốt"; F7 chỉ nêu tiêu chí. NEN_TANG được quyết định ở mức loại nền tảng (F3).
- Target 5 và F9: D-12 là mũi tên đi lên (Persistence --> Domain). A5 cho phép phụ thuộc qua interface do layer trên định nghĩa; F9 coi mọi mũi tên đi lên là lỗi. Giữ D-12 và ghi ở đây.
- PKG-06 StaffWeb được chọn là web dù nguồn không nêu client của nhân viên (Q-35); là quyết định kiến trúc có thể đổi.
