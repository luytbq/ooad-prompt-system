# P09 - Thiết kế kiến trúc - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P09 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (mục 3 Bối cảnh kỹ thuật, mục 2 CHE_DO_GIA_DINH, MUC_CHI_TIET); yeu-cau-phong-tap.md; P01-actors.md (phiên bản 1.0; Mục 1, Mục 2, Giả định); P02-usecases.md (phiên bản 1.1; Mục 4 Bảng 4a); P05-glossary.md (phiên bản 1.0; cột Thuật ngữ, Tiếng Anh); P06-supplementary-spec.md (phiên bản 1.0; Mục 3 đến Mục 5, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F1, F3, F4, Câu hỏi mở, Giả định). P03-usecase-model.md không dùng (nhóm chức năng lấy từ P02 Bảng 4a). RANG_BUOC_KIEN_TRUC: Không có. TIEU_CHI_UU_TIEN: Bảo mật, Sẵn sàng, Hiệu năng, Bảo trì. PHUONG_AN_DA_CHON: Không có. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018 (24 use case còn lại Chưa phân tích ở P08), kiến trúc phải chứa được toàn bộ 28 use case của P02; đề xuất sửa artifact trước của các bước trước chưa áp dụng vì chờ câu trả lời Q. Q lớn nhất trước lần chạy: Q-87; chưa có ASM |
| Phạm vi | Toàn hệ thống (28 use case của P02; lớp phân tích của P08 cho UC-005, UC-010, UC-015, UC-018) |
| Mã Q, ASM cuối đã cấp | Q-94; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Yêu cầu có ý nghĩa kiến trúc

Thứ tự ưu tiên thuộc tính chất lượng theo TIEU_CHI_UU_TIEN: 1 Bảo mật, 2 Sẵn sàng, 3 Hiệu năng, 4 Bảo trì. P06 không xếp hạng NFR. Các dòng thuộc loại ràng buộc cứng (nền tảng, ranh giới phạm vi) ghi "Thiết kế: xếp theo quy tắc F1" và xếp trước các dòng NFR.

| STT | Nguồn (NFR, ràng buộc, ACT) | Kịch bản thuộc tính chất lượng (kích thích --> phản hồi --> thước đo) | Mức ưu tiên | Ảnh hưởng kiến trúc |
|---|---|---|---|---|
| 1 | NFR-03, NFR-04 (ràng buộc nền tảng); ACT-01 đến ACT-07; hồ sơ dự án NEN_TANG | Hội viên, huấn luyện viên mở ứng dụng di động; lễ tân, quản lý chi nhánh, giám đốc chuỗi mở ứng dụng web --> cùng một phần xử lý phía sau phục vụ cả hai loại client --> chạy được trên Android, iOS và trình duyệt máy tính (có hoặc không); phiên bản tối thiểu: Chưa quy định (Q-78) | Ràng buộc cứng. Thiết kế: xếp theo quy tắc F1 | Mẫu front-end/back-end: hai loại client mỏng gọi một bộ API dùng chung; không có phần xử lý nghiệp vụ trên client |
| 2 | NFR-05, NFR-06 (ràng buộc thiết kế); hồ sơ dự án mục 4 | Giao dịch thu tiền phát sinh --> chỉ gửi dữ liệu sang hệ thống hoá đơn điện tử; có báo cáo số buổi tập cá nhân --> không có chức năng lập, điều chỉnh, huỷ hoá đơn và không có chức năng tính thù lao (có hoặc không) | Ràng buộc cứng. Thiết kế: xếp theo quy tắc F1 | Package tích hợp hoá đơn điện tử chỉ có chiều gửi; không có package lập hoá đơn hoặc tính thù lao |
| 3 | TIEU_CHI_UU_TIEN (Bảo mật); yêu cầu nguồn Mục 7 "chỉ hội viên đó và huấn luyện viên phụ trách được xem các chỉ số này" (UC-025, REQ-67, REQ-68); ACT-02, ACT-04 | Người không phải hội viên đó hoặc huấn luyện viên phụ trách yêu cầu xem chỉ số cơ thể --> hệ thống từ chối --> không có lần xem trái phép (có hoặc không); P06 không có NFR bảo mật nào khác nên yêu cầu bảo mật còn lại Chưa quy định (Q-89) | 1 (Bảo mật) | Package Security riêng; mọi lời gọi từ client đều qua API có xác thực; kiểm tra quyền sở hữu dữ liệu ở layer Application; client không truy cập CSDL trực tiếp |
| 4 | TIEU_CHI_UU_TIEN (Sẵn sàng); yêu cầu nguồn Mục 5 "Cửa quay hỏi phần mềm"; NFR-09; ACT-12 | Một tiến trình phía sau dừng hoặc khởi động lại --> lượt quét ở cửa quay và các yêu cầu đặt chỗ vẫn được phục vụ, mốc hẹn giờ không bị mất --> thước đo: Chưa quy định (Q-88); hành vi của cửa quay khi không nhận được kết quả: Q-72 | 2 (Sẵn sàng) | Phần xử lý phía sau không giữ trạng thái nghiệp vụ trong bộ nhớ, chạy được từ một đến nhiều bản chạy; tách tiến trình nền khỏi tiến trình API (PA3) |
| 5 | NFR-01; BR-11 (qua P08 F3); ACT-02; UC-010 | 1.500 hội viên đặt chỗ lớp nhóm cùng lúc lúc 6 giờ sáng thứ Hai --> mọi yêu cầu được xử lý và số chỗ đã đặt của một lớp không vượt sức chứa --> thời gian phản hồi: Chưa đo được (Q-42, Q-76); điều kiện không vượt sức chứa: có hoặc không | 3 (Hiệu năng) | Ghi chỗ đã đặt là một giao dịch CSDL kiểm tra sức chứa tại lúc ghi; gửi thông báo tách khỏi đường xử lý đặt chỗ; API không giữ trạng thái đặt chỗ trong bộ nhớ |
| 6 | NFR-02; ACT-12; UC-018 | Hội viên hoặc khách vãng lai quét mã QR ở cửa quay --> cửa quay nhận kết quả cho phép hoặc không cho phép --> không quá 1 giây (NFR-02); mốc bắt đầu, mốc kết thúc: Q-41; cách tính và mức tải: Q-76 | 3 (Hiệu năng) | Đường xử lý lượt quét ngắn (điểm vào cho thiết bị, một package Application, CSDL), không gọi hệ thống ngoài trong đường này |
| 7 | NFR-07 đến NFR-12; ACT-08 đến ACT-11 | Hệ thống ngoài đổi API hoặc không phản hồi --> chỉ package tích hợp của hệ thống đó phải sửa, các package khác không đổi --> xử lý khi lỗi: Chưa quy định (Q-77, Q-65, Q-79, Q-54, Q-72); trường dữ liệu, giao thức: Chưa quy định (Q-39, Q-67) | 4 (Bảo trì) | Mỗi hệ thống ngoài được che sau một interface; package tích hợp nằm ở layer Services |
| 8 | ACT-13, ACT-14; sáu mốc hẹn của P01 Mục 2 và BR-04 | Mốc thời gian đến (8 giờ sáng mỗi ngày; 2 giờ trước giờ học; 10 phút sau giờ bắt đầu; 30 phút sau thông báo nhận chỗ; hạn 12 giờ của huấn luyện viên; 15 phút của đơn mua) lúc không có phiên của tác nhân nào đang mở --> hệ thống thực hiện hành động của mốc --> độ lệch tối đa so với mốc: Chưa quy định (Q-93) | 2 (Sẵn sàng) | Package Scheduling với kho mốc hẹn bền vững trong CSDL; control không giữ trạng thái chờ trong bộ nhớ (xem A7 ở F8) |
| 9 | Đoạn mở đầu của nguồn và NFR-01 (dữ liệu mẫu): 4 chi nhánh, khoảng 6.000 hội viên, 40 huấn luyện viên, khoảng 25 lớp nhóm mỗi ngày mỗi chi nhánh | Vận hành thường ngày ở quy mô nguồn --> một triển khai trung tâm phục vụ cả bốn chi nhánh --> số node và hạ tầng: Chưa quy định (Q-91) | 4 (Bảo trì). Thiết kế: xếp theo quy tắc F1 | Không dùng microservices hay broker; một mã nguồn phía sau chia package theo nhóm chức năng |
| 10 | TIEU_CHI_UU_TIEN (Bảo trì); 28 use case chia 6 nhóm chức năng ở P02 Bảng 4a | Thêm hoặc đổi một use case --> thay đổi gói gọn trong các package của nhóm chức năng tương ứng --> P06 không có NFR bảo trì nên thước đo định lượng: Chưa quy định; kiểm tra bằng bảng phụ thuộc ở F6 | 4 (Bảo trì) | Package Application và Domain chia theo nhóm chức năng; quy tắc phụ thuộc F6 kiểm tra được |

## F2. Phương án và so sánh

### F2.1. Mẫu kiến trúc

Hồ sơ dự án ghi CONG_NGHE là "Chưa chốt" nên bảng so sánh bắt buộc. Mẫu cho phía giao diện chưa xét ở đây, chọn ở A3b sau khi có phương án công nghệ (F2.2).

| PA | Mẫu kiến trúc (và kết hợp) | Mô tả ngắn | Điều kiện phù hợp |
|---|---|---|---|
| PA1 | Front-end/back-end; back-end multi-layer một khối triển khai, một loại tiến trình | Hai loại client gọi API; back-end 4 layer; mốc hẹn giờ và gửi thông báo chạy cùng tiến trình xử lý yêu cầu | Quy mô nhỏ, tải đồng đều, không có yêu cầu tách tải |
| PA2 | Front-end/back-end; back-end tách thành các dịch vụ theo nhóm chức năng (6 nhóm) qua cổng API hoặc broker | Mỗi nhóm chức năng của P02 là một dịch vụ có CSDL riêng; client gọi qua cổng API | Nhiều đội phát triển độc lập, yêu cầu triển khai và mở rộng riêng từng nhóm |
| PA3 | Front-end/back-end; back-end multi-layer một mã nguồn, hai chế độ chạy: tiến trình API (yêu cầu đồng bộ) và tiến trình nền (mốc hẹn giờ, gửi thông báo) | Cùng 4 layer và cùng package như PA1; hai chế độ chạy có thể gộp trong một tiến trình ở môi trường nhỏ | Có đợt tải đột biến ở đường đồng bộ (đặt chỗ, cửa quay) và có việc nền phải chạy bền |

| Tiêu chí (từ F1) | Trọng số | PA1 | PA2 | PA3 |
|---|---|---|---|---|
| Bảo mật (F1 dòng 3) | 4 | Tốt: một điểm vào API, một nơi áp quyền | Trung bình: nhiều dịch vụ, nhiều ranh giới và thông tin xác thực phải bảo vệ | Tốt: như PA1 |
| Sẵn sàng (F1 dòng 4, 8) | 3 | Trung bình: việc nền và đường đồng bộ cùng vòng đời, lỗi mốc hẹn hoặc đợt gửi thông báo ảnh hưởng đường cửa quay | Trung bình: cô lập lỗi theo dịch vụ nhưng thêm điểm lỗi mạng giữa dịch vụ | Tốt: tiến trình nền tách khỏi tiến trình API, mốc hẹn bền trong CSDL |
| Hiệu năng (F1 dòng 5, 6) | 2 | Trung bình: đợt thông báo của UC-014, UC-015 tranh tài nguyên với đặt chỗ lúc cao điểm | Kém: mỗi lượt quét cửa quay đi qua cổng API và nhiều dịch vụ qua mạng, rủi ro với mức 1 giây của NFR-02 | Tốt: đường đồng bộ ngắn, việc nền chạy riêng |
| Bảo trì (F1 dòng 7, 9, 10) | 1 | Tốt: một mã nguồn, một chế độ chạy | Kém: sáu dịch vụ và sáu CSDL cho 28 use case của một chuỗi 4 chi nhánh | Trung bình: một mã nguồn nhưng thêm cấu hình chế độ chạy |
| Ràng buộc nền tảng, ràng buộc cứng (F1 dòng 1, 2) | Loại nếu Kém | Tốt | Tốt | Tốt |
| Tổng điểm (Tốt = 3, Trung bình = 2, Kém = 1, nhân trọng số) | - | 25 | 17 | 29 |
| Kết luận | - | Loại: Sẵn sàng và Hiệu năng thấp hơn PA3 ở hai tiêu chí xếp trên Bảo trì | Loại: quá lớn so với quy mô, rủi ro với NFR-02 | Chọn |

Chênh lệch giữa PA1 và PA3 do Sẵn sàng và Hiệu năng, hai tiêu chí chưa có thước đo (Q-88, Q-76). Cấu trúc layer và package của PA1 và PA3 giống nhau nên nếu Q-88 và Q-76 cho thấy không cần tách tiến trình nền thì chạy PA3 ở chế độ gộp một tiến trình, không phải thiết kế lại.

### F2.2. Chốt công nghệ

Hồ sơ dự án: NEN_TANG đã chốt ở mức loại ứng dụng (di động Android, iOS; web trên trình duyệt máy tính), CONG_NGHE là "Chưa chốt". PHUONG_AN_DA_CHON là "Không có" nên dùng phương án khuyến nghị.

| CN | Nền tảng | Phía máy chủ (ngôn ngữ, framework) | Phía giao diện | CSDL | Giao tiếp ngoài |
|---|---|---|---|---|---|
| CN1 | Di động native Android và iOS; web SPA | Java 17, Spring Boot | Kotlin (Android), Swift (iOS), React với TypeScript (web) | PostgreSQL | REST/JSON gọi từ máy chủ; thông báo đẩy qua dịch vụ của từng nền tảng |
| CN2 | Di động đa nền tảng một mã nguồn; web SPA | Node.js, NestJS (TypeScript) | React Native (TypeScript) cho di động, React (TypeScript) cho web | PostgreSQL | REST/JSON gọi từ máy chủ; thông báo đẩy qua dịch vụ của từng nền tảng |
| CN3 | Di động đa nền tảng một mã nguồn; web render phía máy chủ | Java 17, Spring Boot | Flutter (Dart) cho di động; mẫu giao diện render phía máy chủ (Thymeleaf) cho web | PostgreSQL | REST/JSON gọi từ máy chủ; thông báo đẩy qua dịch vụ của từng nền tảng |

| Tiêu chí (F1, ràng buộc P06, HE_THONG_NGOAI) | CN1 | CN2 | CN3 |
|---|---|---|---|
| Nền tảng NFR-03, NFR-04 (loại nếu Kém) | Tốt: native chạy Android, iOS; SPA chạy trên trình duyệt | Tốt: React Native chạy Android, iOS; SPA chạy trên trình duyệt | Tốt: Flutter chạy Android, iOS; trang render chạy trên trình duyệt |
| Giao tiếp hệ thống ngoài NFR-07 đến NFR-12 (loại nếu Kém) | Tốt: ba hệ thống ngoài dùng REST, thư viện HTTP sẵn có; tài liệu API hoá đơn điện tử và cửa quay chưa có nên chưa đánh giá sâu hơn được (Q-39, Q-67) | Tốt: như CN1 | Tốt: như CN1 |
| Bảo mật (trọng số 4) | Tốt: một cơ chế xác thực bằng token cho cả hai loại client, hệ sinh thái bảo mật trưởng thành | Tốt: một cơ chế xác thực bằng token cho cả hai loại client | Trung bình: hai cơ chế (phiên và chống CSRF cho web, token cho di động) | 
| Sẵn sàng, hẹn giờ bền (trọng số 3) | Tốt: thư viện lập lịch có kho lưu trong CSDL và khoá giữa nhiều bản chạy | Tốt: lập lịch dựa trên hàng đợi lưu trong CSDL, đủ dùng cho sáu loại mốc | Trung bình: lập lịch như CN1 nhưng web có phiên phía máy chủ, cần kho phiên dùng chung khi chạy nhiều bản |
| Hiệu năng NFR-01, NFR-02 (trọng số 2) | Tốt: đa luồng, pool kết nối, giao dịch khoá dòng quen thuộc | Trung bình: một luồng sự kiện, phù hợp tác vụ chủ yếu chờ I/O; ngưỡng chưa đo nên chưa kết luận được (Q-76) | Tốt: như CN1 |
| Bảo trì (trọng số 1) | Kém: hai mã nguồn di động riêng cộng một mã nguồn web, phía máy chủ khác ngôn ngữ với web | Tốt: hai mã nguồn (di động, web), cùng TypeScript với phía máy chủ | Trung bình: một mã nguồn di động (Dart), web nằm trong máy chủ nhưng ba ngôn ngữ |
| Phù hợp quy mô và đội (trọng số 1; Thiết kế: đội chưa biết nên đánh giá theo số mã nguồn trên 28 use case, Q-94) | Trung bình: ba mã nguồn giao diện | Tốt: ít mã nguồn nhất | Tốt: ít mã nguồn giao diện |
| Tổng điểm (Tốt = 3, Trung bình = 2, Kém = 1, nhân trọng số) | 30 | 31 | 25 |

Kết luận: khuyến nghị CN2. Lý do gắn tiêu chí: CN2 đạt Tốt ở Bảo mật và Sẵn sàng (hai tiêu chí xếp đầu), là phương án duy nhất Tốt ở Bảo trì, và giảm số mã nguồn cho đội chưa biết quy mô. Điểm yếu Hiệu năng (Trung bình) có thể kiểm soát vì ngưỡng NFR-01, NFR-02 chưa đo được (Q-76) và PA3 đã tách việc nền khỏi đường đồng bộ. Chênh lệch với CN1 chỉ 1 điểm; CN1 là phương án thay thế nếu Q-76 đặt ngưỡng hiệu năng chặt hoặc Q-94 cho biết đội thành thạo Java và phát triển native. Phương án được dùng: CN2. Trạng thái: Khuyến nghị - chờ người dùng xác nhận.

## F3. Quyết định kiến trúc

| Mục | Nội dung |
|---|---|
| Bối cảnh | Hệ thống phục vụ chuỗi 4 chi nhánh với hai loại client (ứng dụng di động Android, iOS cho hội viên và huấn luyện viên; ứng dụng web cho lễ tân, quản lý chi nhánh, giám đốc chuỗi), 6 hệ thống ngoài và thiết bị, 6 mốc hẹn giờ do hệ thống tự thực hiện, và đợt đặt chỗ đồng thời tới 1.500 hội viên. Thứ tự ưu tiên: Bảo mật, Sẵn sàng, Hiệu năng, Bảo trì. |
| Quyết định (mẫu và cách kết hợp) | PA3: front-end/back-end. Back-end multi-layer nới lỏng 4 layer Presentation --> Application --> Services --> Domain (Domain thấp nhất), một mã nguồn, hai chế độ chạy (tiến trình API, tiến trình nền). Triển khai theo client-server: client mỏng gọi API qua mạng. Application và Domain chia package theo 6 nhóm chức năng của P02. Không có logic nghiệp vụ trên client (chờ Q-90). |
| Mẫu cho phía giao diện (A3b) | Ứng dụng di động (React Native) và ứng dụng web (React SPA): kiến trúc component kết hợp Flux (luồng dữ liệu một chiều qua store). Phần tiếp nhận yêu cầu ở back-end (REST controller) thuộc layer Presentation phía máy chủ, dùng MVC passive: controller nhận yêu cầu, gọi package Application, trả biểu diễn JSON; biểu diễn đó không quan sát model. |
| Công nghệ | CN2 (F2.2): React Native (TypeScript), React SPA (TypeScript), Node.js với NestJS (TypeScript), PostgreSQL. Trạng thái: Khuyến nghị - chờ người dùng xác nhận. |
| Phương án đã loại và lý do | PA1: Sẵn sàng và Hiệu năng thấp hơn PA3. PA2: quá lớn so với quy mô, rủi ro với NFR-02 vì lượt quét đi qua nhiều dịch vụ qua mạng. CN1 và CN3: điểm thấp hơn CN2 (F2.2); CN1 là phương án thay thế gần nhất. Mẫu transaction-processing, pipe-and-filter, broker: không có nhu cầu (đầu vào không phải dòng giao dịch đồng nhất, không có xử lý tuần tự nhiều bước biến đổi, không có thành phần phân tán cần định vị nhau). |
| Hệ quả tích cực | Một điểm vào cho xác thực và phân quyền. Tách đường đồng bộ khỏi việc nền giúp bảo vệ cửa quay và đặt chỗ lúc cao điểm. Mốc hẹn bền nên khởi động lại không mất mốc. Package theo nhóm chức năng khiến thay đổi gói gọn. Mọi hệ thống ngoài che sau interface nên đổi API chỉ sửa một package. |
| Hệ quả tiêu cực và cách giảm thiểu | Thêm cấu hình hai chế độ chạy: cho phép chạy gộp một tiến trình ở môi trường nhỏ. Control không giữ trạng thái chờ trong bộ nhớ nên P07 cần đổi (Đề xuất sửa artifact trước). Mỗi yêu cầu đi qua nhiều layer: giữ đường cửa quay chỉ qua một package Application. Client mỏng nên mất kết nối là dùng không được (Q-90). |
| NFR được đáp ứng (mã) | NFR-01 (giao dịch ghi chỗ, tách thông báo), NFR-02 (đường ngắn), NFR-03, NFR-04 (hai loại client), NFR-05, NFR-06 (ranh giới phạm vi), NFR-07 đến NFR-12 (package tích hợp che sau interface). Mức đạt định lượng của NFR-01, NFR-02 chờ Q-41, Q-42, Q-76. |
| Rủi ro còn mở | Quyết định mà nguồn không nêu: (1) loại client: huấn luyện viên dùng ứng dụng di động chung với hội viên hay ứng dụng riêng --> chờ Q-92; (2) có cần dùng khi mất kết nối --> chờ Q-90 (hiện thiết kế không có logic cục bộ trên client); (3) nơi đặt phần xử lý phía sau và CSDL, số node, mạng giữa cửa quay và máy chủ --> chờ Q-91; (4) số bản chạy, yêu cầu sẵn sàng --> chờ Q-88; (5) yêu cầu bảo mật và dữ liệu cá nhân --> chờ Q-89; (6) độ lệch của mốc hẹn --> chờ Q-93; (7) ràng buộc đội và hạ tầng ảnh hưởng chọn công nghệ --> chờ Q-94. Rủi ro khác: cổng thanh toán tự gửi kết quả hay không (Q-45) làm thêm điểm vào ở PKG-12. |

## F4. Layer và package cấp cao

Cột "Phụ thuộc vào" của dòng layer ghi hợp các phụ thuộc của package con tới package ngoài layer đó. Mọi package phía máy chủ chạy ở node "máy chủ ứng dụng" (tiến trình API và tiến trình nền); node cụ thể và số node chờ Q-91. Package giao diện phía khách ghi node ở cột Nguồn. Lời gọi qua mạng từ package giao diện phía khách tới PKG-10, PKG-11 không là phụ thuộc package (xem F6, F7).

| PKG | Tên | Layer | Trách nhiệm | Phụ thuộc vào (PKG) | Nguồn (NFR, UC nhóm, ACT) |
|---|---|---|---|---|---|
| PKG-01 | Presentation | - | Tiếp nhận thao tác của người dùng, yêu cầu của thiết bị và hệ thống ngoài rồi hiển thị hoặc trả kết quả | PKG-13, PKG-14, PKG-15, PKG-16, PKG-17, PKG-18, PKG-19, PKG-21 | NFR-02, NFR-03, NFR-04; ACT-01 đến ACT-07, ACT-12 |
| PKG-02 | Application | - | Điều phối từng use case theo nhóm chức năng của P02 mà không giữ trạng thái nghiệp vụ trong bộ nhớ | PKG-21, PKG-22, PKG-23, PKG-24, PKG-25, PKG-26, PKG-27, PKG-28, PKG-29, PKG-30, PKG-31 | 28 use case của P02 (6 nhóm chức năng); NFR-01, NFR-02, NFR-07 đến NFR-12 |
| PKG-03 | Services | - | Cung cấp dịch vụ kỹ thuật dùng chung: lưu trữ, bảo mật, hẹn giờ, giao tiếp hệ thống ngoài | PKG-26, PKG-27, PKG-28, PKG-29, PKG-30, PKG-31 | NFR-07 đến NFR-12; ACT-08 đến ACT-14 |
| PKG-04 | Domain | - | Chứa lớp miền và interface kho dữ liệu | - | Lớp entity của P08 (AC-E-*) |
| PKG-05 | MemberMobileUI | PKG-01 | Cung cấp giao diện di động cho Người quan tâm và Hội viên | - (gọi PKG-10 qua mạng) | ACT-01, ACT-02; UC-001, UC-002, UC-003, UC-005, UC-006, UC-010, UC-011, UC-012, UC-018 (hiển thị mã QR), UC-019, UC-020, UC-023, UC-025; NFR-03; node: thiết bị di động Android, iOS; lớp P08: AC-B-PurchaseOrRenewPackageUI, AC-B-BookClassSpotUI; chưa có lớp P08 (UC-001, UC-002, UC-003, UC-006, UC-011, UC-012, UC-019, UC-020, UC-023, UC-025); chờ Q-92 |
| PKG-06 | TrainerMobileUI | PKG-01 | Cung cấp giao diện di động cho Huấn luyện viên | - (gọi PKG-10 qua mạng) | ACT-04; UC-021, UC-024, UC-025; NFR-03; node: thiết bị di động Android, iOS; chưa có lớp P08 (UC-021, UC-024, UC-025); chờ Q-92 |
| PKG-07 | ReceptionWebUI | PKG-01 | Cung cấp giao diện web cho Lễ tân | - (gọi PKG-11 qua mạng) | ACT-05; UC-005 (bán tại quầy), UC-007, UC-017; NFR-04; node: trình duyệt máy tính của lễ tân; lớp P08: AC-B-SellPackageUI; chưa có lớp P08 (UC-007, UC-017) |
| PKG-08 | BranchManagerWebUI | PKG-01 | Cung cấp giao diện web cho Quản lý chi nhánh | - (gọi PKG-11 qua mạng) | ACT-06; UC-009, UC-014; NFR-04; node: trình duyệt máy tính; chưa có lớp P08 (UC-009, UC-014) |
| PKG-09 | ChainDirectorWebUI | PKG-01 | Cung cấp giao diện web cho Giám đốc chuỗi | - (gọi PKG-11 qua mạng) | ACT-07; UC-026, UC-027, UC-028; NFR-04; node: trình duyệt máy tính; chưa có lớp P08 (UC-026, UC-027, UC-028) |
| PKG-10 | MobileApi | PKG-01 | Tiếp nhận yêu cầu REST từ ứng dụng di động | PKG-13, PKG-14, PKG-15, PKG-16, PKG-17, PKG-21 | NFR-03; ACT-01, ACT-02, ACT-04; UC-001 đến UC-006, UC-010 đến UC-012, UC-018 (lấy mã QR), UC-019 đến UC-025 |
| PKG-11 | WebApi | PKG-01 | Tiếp nhận yêu cầu REST từ ứng dụng web của nhân viên | PKG-14, PKG-15, PKG-16, PKG-18, PKG-19, PKG-21 | NFR-04; ACT-05, ACT-06, ACT-07; UC-005, UC-007, UC-009, UC-014, UC-017, UC-026, UC-027, UC-028 |
| PKG-12 | ExternalApi | PKG-01 | Tiếp nhận lời gọi từ thiết bị gọi vào phần mềm | PKG-16, PKG-21 | NFR-02, NFR-09; ACT-12; lớp P08: AC-B-TurnstileDevice; UC-018; chờ Q-67; thêm cạnh tới PKG-14 nếu Q-45 trả lời cổng thanh toán tự gửi kết quả |
| PKG-13 | AccountService | PKG-02 | Điều phối các use case nhóm Tiếp cận và tài khoản (UC-001 đến UC-004) | PKG-26, PKG-28, PKG-29, PKG-21 | Nhóm Tiếp cận và tài khoản; ACT-01, ACT-02; chưa có lớp P08 (UC-001, UC-002, UC-004; UC-003 chỉ có lớp Tạm AC-E-Member); chờ Q-47 |
| PKG-14 | MembershipService | PKG-02 | Điều phối các use case nhóm Gói tập (UC-005 đến UC-008) | PKG-27, PKG-26, PKG-28, PKG-23, PKG-25, PKG-24, PKG-22 | Nhóm Gói tập; ACT-02, ACT-05, ACT-08, ACT-09, ACT-10, ACT-11, ACT-13; NFR-05, NFR-07, NFR-10, NFR-11, NFR-12; lớp P08: AC-C-PurchaseOrRenewPackageHandler; chưa có lớp P08 (UC-006, UC-007, UC-008) |
| PKG-15 | GroupClassService | PKG-02 | Điều phối các use case nhóm Lớp nhóm (UC-009 đến UC-016) | PKG-29, PKG-26, PKG-30, PKG-24, PKG-22 | Nhóm Lớp nhóm; ACT-02, ACT-06, ACT-09, ACT-10, ACT-14; NFR-01, NFR-10, NFR-11; lớp P08: AC-C-BookClassSpotHandler, AC-C-CancelUnderBookedClassHandler; chưa có lớp P08 (UC-009, UC-011, UC-012, UC-013, UC-014, UC-016) |
| PKG-16 | BranchAccessService | PKG-02 | Điều phối các use case nhóm Ra vào chi nhánh (UC-017, UC-018) | PKG-30, PKG-26, PKG-27, PKG-25 | Nhóm Ra vào chi nhánh; ACT-02, ACT-03, ACT-05, ACT-11, ACT-12; NFR-02; lớp P08: AC-C-EnterBranchHandler; chưa có lớp P08 (UC-017) |
| PKG-17 | PersonalTrainingService | PKG-02 | Điều phối các use case nhóm Huấn luyện cá nhân (UC-019 đến UC-025) | PKG-31, PKG-26, PKG-25, PKG-22 | Nhóm Huấn luyện cá nhân; ACT-02, ACT-04, ACT-11, ACT-14; chưa có lớp P08 (UC-019 đến UC-025); chờ Q-15 |
| PKG-18 | PricingService | PKG-02 | Điều phối việc đặt giá gói và chương trình khuyến mãi (UC-026, UC-027) | PKG-28 | Nhóm Giá và báo cáo (phần giá); ACT-07; chưa có lớp P08 phía control (UC-026, UC-027) |
| PKG-19 | ReportingService | PKG-02 | Điều phối việc lập báo cáo chuỗi (UC-028) | PKG-27, PKG-29, PKG-31 | Nhóm Giá và báo cáo (phần báo cáo); ACT-07; NFR-06; chưa có lớp P08 (UC-028) |
| PKG-20 | Persistence | PKG-03 | Hiện thực lưu trữ cho các interface kho dữ liệu do Domain định nghĩa | PKG-26, PKG-27, PKG-28, PKG-29, PKG-30, PKG-31 | NFR-01 (giao dịch ghi chỗ đã đặt); toàn hệ thống; node: máy chủ ứng dụng truy cập CSDL (chờ Q-91, Q-88) |
| PKG-21 | Security | PKG-03 | Xác thực người dùng và thiết bị gọi vào | PKG-26 | TIEU_CHI_UU_TIEN (Bảo mật); UC-004, UC-025; chờ Q-47, Q-89 |
| PKG-22 | Scheduling | PKG-03 | Điều khiển các mốc hẹn giờ bền vững | PKG-20 | ACT-13, ACT-14; BR-04; UC-005, UC-008, UC-013, UC-015, UC-016, UC-022; chờ Q-93 |
| PKG-23 | PaymentIntegration | PKG-03 | Giao tiếp với cổng thanh toán trực tuyến của đối tác | - | ACT-08; NFR-07; lớp P08: AC-B-PaymentGateway; chờ Q-45, Q-77 |
| PKG-24 | NotificationChannels | PKG-03 | Gửi thông báo đẩy và SMS tới hội viên qua dịch vụ thông báo đẩy và cổng SMS | - | ACT-09, ACT-10; NFR-10, NFR-11; lớp P08: AC-B-PushNotificationGateway, AC-B-SmsGateway; chờ Q-65, Q-79 |
| PKG-25 | EInvoiceIntegration | PKG-03 | Gửi dữ liệu giao dịch thu tiền sang hệ thống hoá đơn điện tử | - | ACT-11; NFR-05, NFR-12; lớp P08: AC-B-EInvoiceGateway; chờ Q-39, Q-54 |
| PKG-26 | Account | PKG-04 | Biểu diễn hội viên và dữ liệu định danh của hội viên | - | Nhóm Tiếp cận và tài khoản; lớp P08: AC-E-Member (Tạm, UC-003) |
| PKG-27 | Membership | PKG-04 | Biểu diễn gói tập, đơn mua và giao dịch thu tiền | PKG-26 | Nhóm Gói tập; lớp P08: AC-E-MembershipPackage, AC-E-PackageOrder, AC-E-PaymentTransaction |
| PKG-28 | Pricing | PKG-04 | Biểu diễn giá gói tập và chương trình khuyến mãi | - | Nhóm Giá và báo cáo; lớp P08: AC-E-PackagePrice, AC-E-Promotion (Tạm, UC-026, UC-027) |
| PKG-29 | GroupClass | PKG-04 | Biểu diễn lớp nhóm, chỗ đã đặt và danh sách chờ | PKG-26 | Nhóm Lớp nhóm; lớp P08: AC-E-GroupClass (Tạm, UC-009), AC-E-ClassBooking, AC-E-Waitlist |
| PKG-30 | BranchAccess | PKG-04 | Biểu diễn lượt quẹt vào cửa và vé tập một ngày | PKG-26 | Nhóm Ra vào chi nhánh; lớp P08: AC-E-EntryScan, AC-E-DayPass (Tạm, UC-017) |
| PKG-31 | PersonalTraining | PKG-04 | Biểu diễn gói buổi tập cá nhân, buổi tập và chỉ số cơ thể | PKG-26 | Nhóm Huấn luyện cá nhân; chưa có lớp P08 (UC-019 đến UC-025) |

## F5. Quy tắc ánh xạ lớp phân tích sang kiến trúc

Mẫu đích: layered nới lỏng ở back-end; component kết hợp Flux ở client; MVC passive ở REST controller. "Controller" của MVC (REST controller ở PKG-10, PKG-11, PKG-12) là thành phần giao diện của back-end, khác lớp control của phân tích.

| Stereotype hoặc loại lớp phân tích | Layer hoặc vai trò trong mẫu đích | Ghi chú |
|---|---|---|
| Boundary giao diện người dùng | Layer Presentation (PKG-01). Là View (component) và store (Flux) trong package giao diện phía khách theo tác nhân: ACT-01, ACT-02 --> PKG-05; ACT-04 --> PKG-06; ACT-05 --> PKG-07; ACT-06 --> PKG-08; ACT-07 --> PKG-09 | Mỗi lớp thuộc đúng một package theo tác nhân chính của lớp. Phần kiểm tra hình thức dữ liệu nhập nằm ở boundary; phần tiếp nhận yêu cầu ở back-end là REST controller ở PKG-10 (cho client di động) hoặc PKG-11 (cho client web), không phải lớp control. Ví dụ P08: AC-B-PurchaseOrRenewPackageUI, AC-B-BookClassSpotUI --> PKG-05; AC-B-SellPackageUI --> PKG-07 |
| Boundary "Kênh thông báo" (P08 F3, cột Loại boundary) | Layer Presentation, package giao diện phía khách của tác nhân người nhận, khi tác nhân người chỉ nhận thông báo | P08 hiện không có lớp loại này: các boundary tới cổng SMS (ACT-09) và dịch vụ thông báo đẩy (ACT-10) mang Loại boundary "Giao diện hệ thống" và theo dòng bên dưới |
| Boundary giao diện hệ thống | Layer Services: subsystem trong package tích hợp, che sau interface do chính package định nghĩa. ACT-08 --> PKG-23; ACT-09, ACT-10 --> PKG-24; ACT-11 --> PKG-25 | Ví dụ P08: AC-B-PaymentGateway --> PKG-23; AC-B-EInvoiceGateway --> PKG-25; AC-B-PushNotificationGateway, AC-B-SmsGateway --> PKG-24. P10 xác định subsystem và IF-nn |
| Boundary giao diện thiết bị | Layer Presentation phía máy chủ: điểm vào dành cho thiết bị ở PKG-12 | Thiết bị gọi vào phần mềm (cửa quay ACT-12), nên phần tiếp nhận là điểm vào API, không phải subsystem gọi ra. Ví dụ P08: AC-B-TurnstileDevice --> PKG-12. Định dạng thông điệp thiết bị (Q-67) chỉ nằm trong PKG-12 |
| Control | Layer Application: lớp dịch vụ ứng dụng trong package theo nhóm chức năng của use case (PKG-13 đến PKG-19) | Ví dụ P08: AC-C-PurchaseOrRenewPackageHandler --> PKG-14; AC-C-BookClassSpotHandler, AC-C-CancelUnderBookedClassHandler --> PKG-15; AC-C-EnterBranchHandler --> PKG-16. Control không giữ trạng thái chờ giữa hai sự kiện trong bộ nhớ (F6, F8). Sự kiện thời gian của ACT-13, ACT-14 vào control qua interface gọi ngược do PKG-22 định nghĩa |
| Entity (phần hành vi nghiệp vụ) | Layer Domain (PKG-04): lớp miền trong package theo nhóm chức năng (PKG-26 đến PKG-31) | Ví dụ P08: AC-E-Member --> PKG-26; AC-E-MembershipPackage, AC-E-PackageOrder, AC-E-PaymentTransaction --> PKG-27; AC-E-PackagePrice, AC-E-Promotion --> PKG-28; AC-E-GroupClass, AC-E-ClassBooking, AC-E-Waitlist --> PKG-29; AC-E-EntryScan, AC-E-DayPass --> PKG-30 |
| Entity (phần lưu trữ) | Interface kho dữ liệu đặt ở Domain, cùng package với entity; phần hiện thực lưu trữ ở PKG-20 Persistence thuộc Services | Realization đi từ PKG-20 xuống Domain. Application chỉ dùng interface kho dữ liệu của Domain |

## F6. Quy tắc phụ thuộc

- V1: kiểu layered nới lỏng, mỗi layer được phụ thuộc mọi layer thấp hơn. Lý do: Presentation phía máy chủ cần Security (Services) để xác thực mà không qua Application, và Application cần dùng trực tiếp entity (Domain) lẫn subsystem (Services).
- V2: layer dưới không phụ thuộc layer trên; không có mũi tên dependency hoặc realization đi lên (thứ tự layer: Presentation, Application, Services, Domain).
- V3: không có vòng phụ thuộc giữa các package, kể cả vòng qua nhiều package. Phụ thuộc trong cùng layer chỉ một chiều theo F4.
- V4: thông tin truyền ngược lên qua interface do layer dưới định nghĩa, layer trên hiện thực. Hai chỗ dùng: (a) PKG-22 Scheduling định nghĩa interface gọi ngược cho mốc hẹn, PKG-14, PKG-15, PKG-17 hiện thực (realization đi xuống PKG-22); (b) PKG-26 đến PKG-31 định nghĩa interface kho dữ liệu, PKG-20 hiện thực (realization đi xuống Domain).
- V5: package phụ thuộc vào interface của subsystem (PKG-23, PKG-24, PKG-25), không phụ thuộc vào lớp bên trong subsystem; chỉ layer Application phụ thuộc các package này.
- V6: lời gọi qua mạng giữa hai node không là phụ thuộc package: PKG-05 đến PKG-09 gọi PKG-10, PKG-11; thiết bị và hệ thống ngoài gọi PKG-12; PKG-20 gọi CSDL. Không ghi ở F4, F6, F9; ghi ở F7.
- V7: giữa các package Domain, hướng phụ thuộc theo F4 là hướng duy nhất cho phép; liên kết hai chiều của P08 giữa hai package Domain được P10 giải bằng cách chọn chiều theo F4 và chuyển hành vi về package phía trên (xem F8, dòng AC-E-Member).
- Không cạnh nào còn chờ câu hỏi mở được vẽ: nếu Q-45 trả lời cổng thanh toán tự gửi kết quả về thì thêm cạnh PKG-12 --> PKG-14 (hợp lệ, cùng chiều xuống); nếu Q-15 trả lời huấn luyện viên được báo qua kênh thông báo thì thêm cạnh PKG-17 --> PKG-24 (hợp lệ).

Bảng kiểm tra, một dòng cho mỗi phụ thuộc trong F4:

| Phụ thuộc (PKG --> PKG) | Hợp lệ | Quy tắc áp dụng |
|---|---|---|
| PKG-10 MobileApi --> PKG-13 AccountService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-10 MobileApi --> PKG-14 MembershipService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-10 MobileApi --> PKG-15 GroupClassService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-10 MobileApi --> PKG-16 BranchAccessService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-10 MobileApi --> PKG-17 PersonalTrainingService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-10 MobileApi --> PKG-21 Security | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-11 WebApi --> PKG-14 MembershipService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-11 WebApi --> PKG-15 GroupClassService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-11 WebApi --> PKG-16 BranchAccessService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-11 WebApi --> PKG-18 PricingService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-11 WebApi --> PKG-19 ReportingService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-11 WebApi --> PKG-21 Security | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-12 ExternalApi --> PKG-16 BranchAccessService | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-12 ExternalApi --> PKG-21 Security | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-13 AccountService --> PKG-26 Account | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-13 AccountService --> PKG-28 Pricing | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-13 AccountService --> PKG-29 GroupClass | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-13 AccountService --> PKG-21 Security | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-14 MembershipService --> PKG-27 Membership | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-14 MembershipService --> PKG-26 Account | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-14 MembershipService --> PKG-28 Pricing | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-14 MembershipService --> PKG-23 PaymentIntegration | Có | V5: phụ thuộc vào interface của subsystem |
| PKG-14 MembershipService --> PKG-25 EInvoiceIntegration | Có | V5: phụ thuộc vào interface của subsystem |
| PKG-14 MembershipService --> PKG-24 NotificationChannels | Có | V5: phụ thuộc vào interface của subsystem |
| PKG-14 MembershipService --> PKG-22 Scheduling | Có | V4: gọi ngược qua interface (DIP) |
| PKG-15 GroupClassService --> PKG-29 GroupClass | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-15 GroupClassService --> PKG-26 Account | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-15 GroupClassService --> PKG-30 BranchAccess | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-15 GroupClassService --> PKG-24 NotificationChannels | Có | V5: phụ thuộc vào interface của subsystem |
| PKG-15 GroupClassService --> PKG-22 Scheduling | Có | V4: gọi ngược qua interface (DIP) |
| PKG-16 BranchAccessService --> PKG-30 BranchAccess | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-16 BranchAccessService --> PKG-26 Account | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-16 BranchAccessService --> PKG-27 Membership | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-16 BranchAccessService --> PKG-25 EInvoiceIntegration | Có | V5: phụ thuộc vào interface của subsystem |
| PKG-17 PersonalTrainingService --> PKG-31 PersonalTraining | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-17 PersonalTrainingService --> PKG-26 Account | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-17 PersonalTrainingService --> PKG-25 EInvoiceIntegration | Có | V5: phụ thuộc vào interface của subsystem |
| PKG-17 PersonalTrainingService --> PKG-22 Scheduling | Có | V4: gọi ngược qua interface (DIP) |
| PKG-18 PricingService --> PKG-28 Pricing | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-19 ReportingService --> PKG-27 Membership | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-19 ReportingService --> PKG-29 GroupClass | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-19 ReportingService --> PKG-31 PersonalTraining | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-20 Persistence --> PKG-26 Account | Có | V4: gọi ngược qua interface (DIP) |
| PKG-20 Persistence --> PKG-27 Membership | Có | V4: gọi ngược qua interface (DIP) |
| PKG-20 Persistence --> PKG-28 Pricing | Có | V4: gọi ngược qua interface (DIP) |
| PKG-20 Persistence --> PKG-29 GroupClass | Có | V4: gọi ngược qua interface (DIP) |
| PKG-20 Persistence --> PKG-30 BranchAccess | Có | V4: gọi ngược qua interface (DIP) |
| PKG-20 Persistence --> PKG-31 PersonalTraining | Có | V4: gọi ngược qua interface (DIP) |
| PKG-21 Security --> PKG-26 Account | Có | V2: layered nới lỏng, layer trên phụ thuộc layer dưới |
| PKG-22 Scheduling --> PKG-20 Persistence | Có | V3: cùng layer, một chiều, không vòng |
| PKG-27 Membership --> PKG-26 Account | Có | V3: cùng layer, một chiều, không vòng |
| PKG-29 GroupClass --> PKG-26 Account | Có | V3: cùng layer, một chiều, không vòng |
| PKG-30 BranchAccess --> PKG-26 Account | Có | V3: cùng layer, một chiều, không vòng |
| PKG-31 PersonalTraining --> PKG-26 Account | Có | V3: cùng layer, một chiều, không vòng |

## F7. Định hướng giao tiếp ngoài và dữ liệu

| ACT (hệ thống ngoài, thiết bị, tác nhân thời gian) hoặc node khác của chính hệ thống | PKG chứa | Nguyên tắc cô lập | Rủi ro (lỗi, timeout, thay đổi API) |
|---|---|---|---|
| ACT-08 Cổng thanh toán | PKG-23 PaymentIntegration | Interface "gửi đơn mua, lấy kết quả" do PKG-23 định nghĩa; PKG-14 chỉ biết interface; định dạng API của đối tác ở trong PKG-23 | Cổng không phản hồi hoặc báo lỗi (Q-77); kết quả đến sau khi đơn đã huỷ (Q-14); cổng tự gửi kết quả về (Q-45, nếu có thì thêm điểm vào ở PKG-12); thay đổi API |
| ACT-09 Cổng SMS, ACT-10 Dịch vụ thông báo đẩy | PKG-24 NotificationChannels | Một interface cho mỗi kênh; việc chọn kênh theo từng hội viên làm ở Application, PKG-24 chỉ gửi. Thiết kế: gửi thông báo qua tiến trình nền để không làm chậm đường đặt chỗ (NFR-01) | Không gửi được (Q-65, Q-79); cách xác định hội viên chưa cài ứng dụng (Q-36); kênh thông báo kết quả mua gói (Q-53); thay đổi API; giao thức dịch vụ thông báo đẩy chưa có tài liệu |
| ACT-11 Hệ thống hoá đơn điện tử | PKG-25 EInvoiceIntegration | Chỉ có chiều gửi dữ liệu giao dịch thu tiền (NFR-05); PKG-25 không có chức năng lập, điều chỉnh, huỷ hoá đơn | Tài liệu API chưa có, trường dữ liệu chưa rõ (Q-39); bên nhận từ chối hoặc không nhận (Q-54); thay đổi API |
| ACT-12 Cửa quay | PKG-12 ExternalApi (điểm vào cho thiết bị) | Định dạng thông điệp của cửa quay chỉ nằm trong PKG-12, chuyển thành lời gọi tới PKG-16; không gọi hệ thống ngoài trong đường xử lý lượt quét (NFR-02) | Nội dung trao đổi, giao thức chưa có (Q-67); cách báo cho người quét (Q-70); cửa quay không nhận được kết quả (Q-72); mốc đo và tải (Q-41, Q-76); thay đổi API |
| ACT-13 Bộ định thời hằng ngày, ACT-14 Bộ định thời theo hạn | PKG-22 Scheduling | PKG-22 giữ kho mốc hẹn bền vững trong CSDL và định nghĩa interface gọi ngược; Application hiện thực. Thiết kế: mỗi mốc chỉ được một bản chạy nhận để không xử lý trùng khi chạy nhiều bản | Độ lệch mốc (Q-93); có bước nhân viên duyệt hoặc gỡ không (Q-43); mốc bắt đầu 12 giờ của huấn luyện viên (Q-80) |
| Máy in vé (chờ Q-44) | Chờ Q-44 | Nếu in từ trình duyệt qua máy in thông thường: không cần package riêng, in từ PKG-07; nếu máy in nối riêng nhận lệnh in: thêm subsystem ở layer Services | Chưa có package vì ranh giới còn chờ Q-44 |
| Máy POS của ngân hàng (không kết nối, NFR-08) | Không có | Mã giao dịch POS do lễ tân nhập ở PKG-07 và đi qua PKG-11 | Quy tắc định dạng và kiểm tra trùng mã (Q-55) |
| Node khác: ứng dụng di động (PKG-05, PKG-06) | PKG-10 MobileApi (phía máy chủ) | Chỉ gọi API; không có logic nghiệp vụ cục bộ. Thiết kế: REST/JSON qua kênh mã hoá | Phiên bản hệ điều hành tối thiểu (Q-78); dùng khi mất kết nối (Q-90); một hay hai ứng dụng (Q-92) |
| Node khác: ứng dụng web (PKG-07, PKG-08, PKG-09) | PKG-11 WebApi (phía máy chủ) | Chỉ gọi API; mọi thao tác nhân viên qua PKG-11 | Trình duyệt tối thiểu (Q-78); giới hạn nơi truy cập (Q-89); dùng khi mất kết nối (Q-90) |
| Node khác: kho dữ liệu (CSDL) | PKG-20 Persistence | Chỉ PKG-20 truy cập CSDL; Domain định nghĩa interface kho, Persistence hiện thực | Đặt ở đâu và số node (Q-91); sao lưu, mất dữ liệu tối đa (Q-88) |

| Mục | Quyết định | Lý do |
|---|---|---|
| Loại cơ chế lưu trữ | Quan hệ (PostgreSQL, theo CN2) | Dữ liệu có liên kết chặt giữa hội viên, gói, đơn, lớp, chỗ đã đặt; ràng buộc BR-11 cần giao dịch. Thiết kế: cơ chế quan hệ phù hợp giao dịch nhiều bước |
| Layer truy cập dữ liệu | Services, package PKG-20 Persistence; interface kho dữ liệu ở Domain | Persistence phải tham chiếu lớp miền để ánh xạ, nên Domain ở thấp nhất để phụ thuộc đi xuống (A4) |
| Chiến lược giao dịch mức cao | Ghi chỗ đã đặt là một giao dịch CSDL: khoá dòng của lớp, kiểm tra số chỗ đã đặt so với sức chứa, rồi ghi. Mốc hẹn và nhận kết quả thanh toán xử lý lặp lại được (idempotent) | BR-11 (không vượt sức chứa kể cả đặt cùng lúc), NFR-01. Thiết kế: kiểm tra tại chỗ ghi mới đúng với nhiều bản chạy API; xử lý lặp lại được vì mốc hẹn và kết quả ngoài có thể đến hai lần |
| Dữ liệu cần bảo vệ | Chỉ số cơ thể (UC-024, UC-025), họ tên và số điện thoại của hội viên (UC-003), giao dịch thu tiền và mã giao dịch POS (UC-005), thông tin xác thực | Yêu cầu nguồn Mục 7 giới hạn người xem chỉ số cơ thể. Quyền xem kiểm tra ở Application (huấn luyện viên phụ trách) và Security (định danh). Thiết kế: truyền dữ liệu qua kênh mã hoá. Mã hoá dữ liệu lưu trữ, quy định tuân thủ, thời gian lưu: chờ Q-89 |

## F8. Kiểm tra chứa mô hình phân tích

P08 có 23 lớp (cả 23 ở trạng thái Hoạt động hoặc Tạm; không lớp nào "Gộp vào").

| Nhóm lớp phân tích (theo stereotype hoặc nhóm chức năng) | Số lớp | Layer, PKG đích | Vấn đề |
|---|---|---|---|
| Boundary giao diện người dùng | 3 | Presentation: PKG-05 (AC-B-PurchaseOrRenewPackageUI, AC-B-BookClassSpotUI), PKG-07 (AC-B-SellPackageUI) | Không |
| Boundary giao diện hệ thống | 4 | Services: PKG-23 (AC-B-PaymentGateway), PKG-25 (AC-B-EInvoiceGateway), PKG-24 (AC-B-PushNotificationGateway, AC-B-SmsGateway) | Không. Hậu tố "Gateway" của P08 giữ nguyên (C1 mục 3) |
| Boundary giao diện thiết bị | 1 | Presentation phía máy chủ: PKG-12 (AC-B-TurnstileDevice) | Boundary vừa nhận thao tác của người quét (ACT-02, ACT-03) vừa trao đổi với cửa quay; ở kiến trúc này người quét chỉ tác động qua thiết bị nên toàn bộ vào PKG-12 |
| Control | 4 | Application: PKG-14 (AC-C-PurchaseOrRenewPackageHandler), PKG-15 (AC-C-BookClassSpotHandler, AC-C-CancelUnderBookedClassHandler), PKG-16 (AC-C-EnterBranchHandler) | Hai control giữ trạng thái chờ giữa hai sự kiện: AC-C-PurchaseOrRenewPackageHandler (startWaitingForPayment, stopWaitingForPayment, handlePaymentTimeout) và AC-C-CancelUnderBookedClassHandler (cancelAbsenceMark, cancelWaitlistTransferMark). Kiến trúc không cho giữ trạng thái này trong bộ nhớ: ghi Đề xuất sửa P07 bên dưới |
| Entity nhóm Tiếp cận và tài khoản | 1 | Domain: PKG-26 (AC-E-Member, Tạm chờ P07 của UC-003) | AC-E-Member có hành vi hỏi dữ liệu ở package khác (checkPackageEligibility, activatePackage hỏi gói ở PKG-27; checkDailyBookingLimit đếm chỗ đã đặt ở PKG-29). Theo F4 PKG-27, PKG-29 phụ thuộc PKG-26, nên P10 chuyển các hành vi này sang package phía trên hoặc dùng interface do PKG-26 định nghĩa; không thêm cạnh ngược |
| Entity nhóm Gói tập | 3 | Domain: PKG-27 (AC-E-MembershipPackage, AC-E-PackageOrder, AC-E-PaymentTransaction) | Quan hệ PackageOrder với MembershipPackage, PackagePrice chưa có (Q-82, Q-87); chưa ảnh hưởng chiều phụ thuộc |
| Entity nhóm Giá và báo cáo | 2 | Domain: PKG-28 (AC-E-PackagePrice, AC-E-Promotion; cả hai Tạm) | AC-E-PackagePrice.calculateAmountDue cần mức giảm của Promotion (P08 F6 ghi Không đạt); hai lớp cùng PKG-28 nên không phát sinh phụ thuộc giữa package |
| Entity nhóm Lớp nhóm | 3 | Domain: PKG-29 (AC-E-GroupClass Tạm, AC-E-ClassBooking, AC-E-Waitlist) | Không |
| Entity nhóm Ra vào chi nhánh | 2 | Domain: PKG-30 (AC-E-EntryScan, AC-E-DayPass Tạm) | Không |
| Nhóm chưa phân tích | 0 lớp | Package đã có theo nhóm: PKG-13 (UC-001, UC-002, UC-004), PKG-17 và PKG-31 (UC-019 đến UC-025), PKG-19 (UC-028), PKG-18 (UC-026, UC-027, phần control), PKG-06 (UC-021, UC-024, UC-025), PKG-08 (UC-009, UC-014), PKG-09 (UC-026, UC-027, UC-028); phần chưa phân tích của PKG-05, PKG-07, PKG-14, PKG-15, PKG-16 (UC-003, UC-006, UC-007, UC-008, UC-009, UC-011 đến UC-014, UC-016, UC-017, UC-019 đến UC-025) | Kiến trúc chứa được cả 28 use case của P02 (6 nhóm chức năng đều có package ở Application và Domain). Khi có P07 của các use case này, chạy lại P08 rồi rà lại F8 |

Tổng số lớp: 3 + 4 + 1 + 4 + 1 + 3 + 2 + 3 + 2 = 23, khớp P08 F3. Mọi lớp hoạt động hoặc Tạm có layer đích.

## F9. Package diagram

File diagrams/P09-package-layers.drawio. Toạ độ ở bảng Node là tuyệt đối trên trang; file .drawio ghi toạ độ của package con tương đối theo layer chứa nó. Mọi cạnh là phụ thuộc đi từ package phụ thuộc tới package được dùng; không có cạnh đi lên. Điểm uốn ở bảng Edge là toạ độ tuyệt đối.

a) Bảng Node

| ID (PKG) | Loại (Package / Layer) | Nhãn | Stereotype | Thuộc về (PKG layer chứa) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-01 | Layer | Presentation | «layer» | - | Chứa 5 package giao diện phía khách và 3 package tiếp nhận yêu cầu phía máy chủ | 20 | 20 | 1720 | 240 |
| PKG-02 | Layer | Application | «layer» | - | Một package cho mỗi nhóm chức năng của P02; nhóm Giá và báo cáo tách hai package theo trách nhiệm | 20 | 440 | 1720 | 140 |
| PKG-03 | Layer | Services | «layer» | - | Dịch vụ kỹ thuật và subsystem giao tiếp hệ thống ngoài | 20 | 930 | 1720 | 140 |
| PKG-04 | Layer | Domain | «layer» | - | Layer thấp nhất: entity và interface kho dữ liệu | 20 | 1360 | 1720 | 180 |
| PKG-05 | Package | MemberMobileUI | - | PKG-01 | - | 120 | 80 | 160 | 60 |
| PKG-06 | Package | TrainerMobileUI | - | PKG-01 | - | 320 | 80 | 160 | 60 |
| PKG-07 | Package | ReceptionWebUI | - | PKG-01 | - | 520 | 80 | 160 | 60 |
| PKG-08 | Package | BranchManagerWebUI | - | PKG-01 | - | 720 | 80 | 160 | 60 |
| PKG-09 | Package | ChainDirectorWebUI | - | PKG-01 | - | 920 | 80 | 160 | 60 |
| PKG-10 | Package | MobileApi | - | PKG-01 | - | 280 | 180 | 160 | 60 |
| PKG-11 | Package | WebApi | - | PKG-01 | - | 680 | 180 | 160 | 60 |
| PKG-12 | Package | ExternalApi | - | PKG-01 | - | 1080 | 180 | 160 | 60 |
| PKG-13 | Package | AccountService | - | PKG-02 | - | 120 | 500 | 160 | 60 |
| PKG-14 | Package | MembershipService | - | PKG-02 | - | 320 | 500 | 160 | 60 |
| PKG-15 | Package | GroupClassService | - | PKG-02 | - | 520 | 500 | 160 | 60 |
| PKG-16 | Package | BranchAccessService | - | PKG-02 | - | 720 | 500 | 160 | 60 |
| PKG-17 | Package | PersonalTrainingService | - | PKG-02 | - | 920 | 500 | 160 | 60 |
| PKG-18 | Package | PricingService | - | PKG-02 | - | 1120 | 500 | 160 | 60 |
| PKG-19 | Package | ReportingService | - | PKG-02 | - | 1320 | 500 | 160 | 60 |
| PKG-20 | Package | Persistence | - | PKG-03 | - | 320 | 990 | 160 | 60 |
| PKG-21 | Package | Security | - | PKG-03 | - | 520 | 990 | 160 | 60 |
| PKG-22 | Package | Scheduling | - | PKG-03 | - | 120 | 990 | 160 | 60 |
| PKG-23 | Package | PaymentIntegration | - | PKG-03 | - | 720 | 990 | 160 | 60 |
| PKG-24 | Package | NotificationChannels | - | PKG-03 | - | 920 | 990 | 160 | 60 |
| PKG-25 | Package | EInvoiceIntegration | - | PKG-03 | - | 1120 | 990 | 160 | 60 |
| PKG-26 | Package | Account | - | PKG-04 | - | 120 | 1420 | 160 | 60 |
| PKG-27 | Package | Membership | - | PKG-04 | - | 320 | 1420 | 160 | 60 |
| PKG-28 | Package | Pricing | - | PKG-04 | - | 1120 | 1420 | 160 | 60 |
| PKG-29 | Package | GroupClass | - | PKG-04 | - | 520 | 1420 | 160 | 60 |
| PKG-30 | Package | BranchAccess | - | PKG-04 | - | 720 | 1420 | 160 | 60 |
| PKG-31 | Package | PersonalTraining | - | PKG-04 | - | 920 | 1420 | 160 | 60 |
| N-01 | Note | Lời gọi qua mạng từ ứng dụng khách tới PKG-10, PKG-11 không là phụ thuộc package | - | PKG-01 | Ghi chú sơ đồ | 1120 | 80 | 360 | 60 |

b) Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | PKG-10 | PKG-13 | Dependency | - | Hội viên: xem giá, lịch, đăng ký, đăng nhập (UC-001 đến UC-004) | (290,290); (270,290) |
| E-02 | PKG-10 | PKG-14 | Dependency | - | Mua, gia hạn, bảo lưu gói tập (UC-005, UC-006) | (400,310); (390,310) |
| E-03 | PKG-10 | PKG-15 | Dependency | - | Đặt, huỷ chỗ, nhận chỗ từ danh sách chờ (UC-010, UC-011, UC-012) | (430,320); (530,320) |
| E-04 | PKG-10 | PKG-16 | Dependency | - | Lấy mã QR hiển thị trên ứng dụng (UC-018) | (420,330); (730,330) |
| E-05 | PKG-10 | PKG-17 | Dependency | - | Buổi tập cá nhân và chỉ số cơ thể của hội viên, huấn luyện viên (UC-019 đến UC-025) | (410,360); (930,360) |
| E-06 | PKG-10 | PKG-21 | Dependency | - | Xác thực và phân quyền lời gọi từ ứng dụng di động (chờ Q-89) | (300,280); (60,280); (60,610); (550,610) |
| E-07 | PKG-11 | PKG-14 | Dependency | - | Lễ tân bán gói, chuyển nhượng gói (UC-005, UC-007) | (690,340); (470,340) |
| E-08 | PKG-11 | PKG-15 | Dependency | - | Quản lý chi nhánh lập lịch, huỷ lớp vì sự cố (UC-009, UC-014) | (700,370); (670,370) |
| E-09 | PKG-11 | PKG-16 | Dependency | - | Lễ tân bán vé tập một ngày (UC-017) | (800,380); (790,380) |
| E-10 | PKG-11 | PKG-18 | Dependency | - | Giám đốc chuỗi đặt giá, khuyến mãi (UC-026, UC-027) | (830,390); (1130,390) |
| E-11 | PKG-11 | PKG-19 | Dependency | - | Giám đốc chuỗi xem báo cáo (UC-028) | (820,410); (1330,410) |
| E-12 | PKG-11 | PKG-21 | Dependency | - | Xác thực và phân quyền lời gọi từ ứng dụng web (chờ Q-89) | (710,300); (70,300); (70,620); (560,620) |
| E-13 | PKG-12 | PKG-16 | Dependency | - | Lượt quét mã QR từ cửa quay (UC-018) | (1100,400); (870,400) |
| E-14 | PKG-12 | PKG-21 | Dependency | - | Xác thực thiết bị gọi vào (chờ Q-67, Q-89) | (1090,350); (80,350); (80,630); (570,630) |
| E-15 | PKG-13 | PKG-26 | Dependency | - | Đăng ký, đăng nhập hội viên | (270,710); (1520,710); (1520,1190); (270,1190) |
| E-16 | PKG-13 | PKG-28 | Dependency | - | Xem giá gói tập (UC-001) | (210,730); (1670,730); (1670,1310); (1270,1310) |
| E-17 | PKG-13 | PKG-29 | Dependency | - | Xem lịch lớp nhóm (UC-002) | (230,720); (1600,720); (1600,1240); (670,1240) |
| E-18 | PKG-13 | PKG-21 | Dependency | - | Thông tin xác thực khi đăng ký, đăng nhập (chờ Q-47, Q-89) | (220,640); (540,640) |
| E-19 | PKG-14 | PKG-27 | Dependency | - | Gói tập, đơn mua, giao dịch thu tiền | (460,760); (1570,760); (1570,1210); (470,1210) |
| E-20 | PKG-14 | PKG-26 | Dependency | - | Hội viên sở hữu gói | (470,750); (1530,750); (1530,1200); (260,1200) |
| E-21 | PKG-14 | PKG-28 | Dependency | - | Giá gói, khuyến mãi khi tính số tiền phải trả | (430,770); (1680,770); (1680,1320); (1260,1320) |
| E-22 | PKG-14 | PKG-23 | Dependency | - | Gửi đơn mua, nhận kết quả thanh toán (ACT-08) | (450,670); (730,670) |
| E-23 | PKG-14 | PKG-25 | Dependency | - | Gửi dữ liệu giao dịch thu tiền (ACT-11) | (420,690); (1130,690) |
| E-24 | PKG-14 | PKG-24 | Dependency | - | Nhắc gia hạn (UC-008), thông báo đơn bị huỷ (chờ Q-53) | (440,680); (940,680) |
| E-25 | PKG-14 | PKG-22 | Dependency | - | Mốc 15 phút của đơn mua (BR-04), mốc 8 giờ sáng hằng ngày (UC-008); package hiện thực interface gọi ngược do Scheduling định nghĩa | (330,600); (260,600) |
| E-26 | PKG-15 | PKG-29 | Dependency | - | Lớp nhóm, chỗ đã đặt, danh sách chờ | (660,800); (1610,800); (1610,1250); (660,1250) |
| E-27 | PKG-15 | PKG-26 | Dependency | - | Hội viên đặt chỗ | (670,790); (1540,790); (1540,1180); (240,1180) |
| E-28 | PKG-15 | PKG-30 | Dependency | - | Lượt quẹt vào cửa làm căn cứ tính vắng mặt (UC-016, chưa có lớp P08) | (650,810); (1630,810); (1630,1270); (870,1270) |
| E-29 | PKG-15 | PKG-24 | Dependency | - | Thông báo lớp bị huỷ, có chỗ trống (UC-011, UC-014, UC-015) | (640,700); (950,700) |
| E-30 | PKG-15 | PKG-22 | Dependency | - | Mốc 2 giờ trước giờ học (UC-015), 10 phút sau giờ bắt đầu (UC-016), 30 phút sau thông báo nhận chỗ (UC-013); hiện thực interface gọi ngược | (530,650); (250,650) |
| E-31 | PKG-16 | PKG-30 | Dependency | - | Lượt quẹt vào cửa, vé tập một ngày | (850,840); (1640,840); (1640,1280); (860,1280) |
| E-32 | PKG-16 | PKG-26 | Dependency | - | Hội viên và mã QR | (870,820); (1550,820); (1550,1160); (220,1160) |
| E-33 | PKG-16 | PKG-27 | Dependency | - | Kiểm tra gói còn hiệu lực, không đang bảo lưu, áp dụng cho chi nhánh (BR-15, BR-16, BR-17) | (860,830); (1580,830); (1580,1220); (460,1220) |
| E-34 | PKG-16 | PKG-25 | Dependency | - | Gửi dữ liệu giao dịch thu tiền khi bán vé (UC-017) | (840,740); (1140,740) |
| E-35 | PKG-17 | PKG-31 | Dependency | - | Gói buổi tập cá nhân, buổi tập, chỉ số cơ thể (chưa có lớp P08) | (1060,860); (1650,860); (1650,1290); (1070,1290) |
| E-36 | PKG-17 | PKG-26 | Dependency | - | Hội viên và huấn luyện viên phụ trách | (1070,850); (1560,850); (1560,1170); (210,1170) |
| E-37 | PKG-17 | PKG-25 | Dependency | - | Gửi dữ liệu giao dịch thu tiền khi bán gói buổi tập cá nhân (UC-019) | (1050,780); (1150,780) |
| E-38 | PKG-17 | PKG-22 | Dependency | - | Mốc hạn 12 giờ của yêu cầu đặt buổi (UC-022); hiện thực interface gọi ngược | (930,660); (240,660) |
| E-39 | PKG-18 | PKG-28 | Dependency | - | Giá gói, khuyến mãi | (1270,870); (1690,870); (1690,1330); (1250,1330) |
| E-40 | PKG-19 | PKG-27 | Dependency | - | Doanh thu từ giao dịch thu tiền (UC-028, chưa có lớp P08) | (1470,880); (1590,880); (1590,1230); (450,1230) |
| E-41 | PKG-19 | PKG-29 | Dependency | - | Tỉ lệ lấp đầy lớp nhóm (UC-028) | (1460,890); (1620,890); (1620,1260); (650,1260) |
| E-42 | PKG-19 | PKG-31 | Dependency | - | Số buổi tập cá nhân của huấn luyện viên (UC-028) | (1450,900); (1660,900); (1660,1300); (1060,1300) |
| E-43 | PKG-20 | PKG-26 | Dependency | - | Hiện thực interface kho dữ liệu do Domain định nghĩa | (330,1090); (250,1090) |
| E-44 | PKG-20 | PKG-27 | Dependency | - | Hiện thực interface kho dữ liệu do Domain định nghĩa | (400,1110); (390,1110) |
| E-45 | PKG-20 | PKG-28 | Dependency | - | Hiện thực interface kho dữ liệu do Domain định nghĩa | (410,1150); (1130,1150) |
| E-46 | PKG-20 | PKG-29 | Dependency | - | Hiện thực interface kho dữ liệu do Domain định nghĩa | (440,1120); (540,1120) |
| E-47 | PKG-20 | PKG-30 | Dependency | - | Hiện thực interface kho dữ liệu do Domain định nghĩa | (430,1130); (730,1130) |
| E-48 | PKG-20 | PKG-31 | Dependency | - | Hiện thực interface kho dữ liệu do Domain định nghĩa | (420,1140); (930,1140) |
| E-49 | PKG-21 | PKG-26 | Dependency | - | Định danh người dùng gắn với hội viên (nhân viên, huấn luyện viên chờ Q-01 đến Q-06, Q-89) | (530,1100); (230,1100) |
| E-50 | PKG-22 | PKG-20 | Dependency | - | Kho lưu mốc hẹn bền vững trong CSDL | - |
| E-51 | PKG-27 | PKG-26 | Dependency | - | Gói, đơn mua gắn với hội viên (R-12, R-13) | (330,1530); (270,1530) |
| E-52 | PKG-29 | PKG-26 | Dependency | - | Chỗ đã đặt, danh sách chờ gắn với hội viên (R-19, R-20) | (530,1520); (260,1520) |
| E-53 | PKG-30 | PKG-26 | Dependency | - | Lượt quẹt vào cửa gắn với hội viên (R-28) | (730,1510); (250,1510) |
| E-54 | PKG-31 | PKG-26 | Dependency | - | Buổi tập cá nhân gắn với hội viên | (930,1500); (240,1500) |

## F10. Deployment diagram

Không có. MUC_CHI_TIET của hồ sơ dự án là GON, không phải DAY_DU nên không tạo diagrams/P09-deployment.drawio. Thông tin node nằm ở F4 (cột Nguồn), F7 và F11.

## F11. Cập nhật hồ sơ dự án

Thay hai dòng NEN_TANG, CONG_NGHE hiện có trong bảng ở project-profile.md mục 3 bằng khối sau (NEN_TANG giữ nguyên giá trị hiện có, CONG_NGHE thay "Chưa chốt"):

```text
| NEN_TANG | Ứng dụng di động Android và iOS cho hội viên và huấn luyện viên; ứng dụng web chạy trên trình duyệt máy tính cho lễ tân, quản lý chi nhánh và giám đốc chuỗi |
| CONG_NGHE | Ứng dụng di động: React Native (TypeScript); ứng dụng web: React SPA (TypeScript); máy chủ: Node.js với NestJS (TypeScript), giao tiếp REST/JSON; hệ quản trị CSDL: PostgreSQL |
```

Trạng thái: Khuyến nghị - chờ người dùng xác nhận.

Q-nn mà giá trị trên phụ thuộc: Q-76, Q-94. Chấp nhận khối này là chấp nhận phương án đã dùng cho các Q đó.

Nhắc: cập nhật hồ sơ trước khi chạy P10.

## F12. Mục kiểm soát

Gồm các mục Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở ngay dưới đây.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-88 | Hệ thống phải hoạt động liên tục trong khung giờ nào, được ngừng tối đa bao lâu mỗi lần và mỗi tháng (đặc biệt phần phục vụ cửa quay và đặt chỗ lớp nhóm), và được mất tối đa bao nhiêu dữ liệu khi có sự cố? (Nêu khung giờ, thời gian ngừng tối đa, lượng dữ liệu được phép mất) | F1 dòng 4, 8; tiêu chí Sẵn sàng ở F2.1; số bản chạy phía máy chủ; sao lưu (F7) | Nguồn không có yêu cầu sẵn sàng; P06 không có NFR sẵn sàng (Vấn đề còn mở của P06); TIEU_CHI_UU_TIEN xếp Sẵn sàng thứ hai |
| Q-89 | Ngoài việc "chỉ hội viên đó và huấn luyện viên phụ trách được xem các chỉ số này", hệ thống có yêu cầu bảo mật nào khác không (cách xác thực của nhân viên và huấn luyện viên, quy định bảo vệ dữ liệu cá nhân phải tuân thủ, mã hoá dữ liệu lưu trữ, thời gian lưu dữ liệu, giới hạn nơi nhân viên truy cập ứng dụng web)? (Nêu từng yêu cầu / Không có yêu cầu thêm) | F1 dòng 3; PKG-21 Security; F7 dòng dữ liệu cần bảo vệ | Yêu cầu nguồn Mục 7 chỉ nêu quyền xem chỉ số cơ thể; P06 không có NFR bảo mật; TIEU_CHI_UU_TIEN xếp Bảo mật thứ nhất |
| Q-90 | Ứng dụng di động và ứng dụng web có cần dùng được một phần khi mất kết nối mạng không (ví dụ lễ tân bán gói tại quầy khi mất mạng)? (Không, luôn cần kết nối / Có - nêu chức năng cần dùng được) | F3 dòng Quyết định (không có logic cục bộ trên client); PKG-05 đến PKG-09; A4 về client có logic nghiệp vụ cục bộ | Nguồn và hồ sơ dự án không nêu việc dùng khi mất kết nối |
| Q-91 | Phần xử lý phía sau và CSDL đặt ở đâu (đám mây của nhà cung cấp, máy chủ riêng của VietFit, hay tại từng chi nhánh), cửa quay tại chi nhánh gọi tới máy chủ qua mạng nào, và có ràng buộc về nơi lưu dữ liệu không? (Nêu từng nội dung) | F1 dòng 9; số node triển khai; F4 đoạn dẫn; F7 | Hồ sơ dự án chỉ nêu nền tảng client; "Cửa quay hỏi phần mềm" (Mục 5) không nói phần mềm chạy ở đâu |
| Q-92 | Hội viên và huấn luyện viên dùng chung một ứng dụng di động (giao diện theo vai trò) hay hai ứng dụng riêng? (Một ứng dụng chung / Hai ứng dụng riêng) | PKG-05, PKG-06 (đóng gói và phát hành), F3 | Hồ sơ dự án NEN_TANG: "Ứng dụng di động Android và iOS cho hội viên và huấn luyện viên" không nói một hay hai ứng dụng |
| Q-93 | Các mốc hẹn giờ (8 giờ sáng hằng ngày, 2 giờ trước giờ học, 10 phút sau giờ bắt đầu, 30 phút sau thông báo nhận chỗ, hạn 12 giờ của huấn luyện viên, 15 phút của đơn mua) được phép lệch tối đa bao nhiêu so với mốc? (Nêu độ lệch tối đa cho từng loại hoặc chung) | F1 dòng 8; PKG-22 Scheduling | Nguồn nêu các mốc nhưng không nêu độ chính xác thực hiện |
| Q-94 | Đội phát triển và vận hành của VietFit đã thành thạo ngôn ngữ, framework nào, và có ràng buộc ngân sách, giấy phép hoặc nhà cung cấp hạ tầng nào ảnh hưởng việc chọn công nghệ? (Nêu danh sách / Không có ràng buộc) | F2.2 (khuyến nghị CN2, CN1 là phương án thay thế); F11 | Hồ sơ dự án ghi CONG_NGHE "Chưa chốt" và không nêu năng lực đội hay ràng buộc chi phí |

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P07 | UC-005, AC-C-PurchaseOrRenewPackageHandler (startWaitingForPayment, stopWaitingForPayment, handlePaymentTimeout) | Control giữ trạng thái "đang chờ thanh toán" và thời hạn BR-04 giữa hai sự kiện (xác nhận mua, kết quả thanh toán hoặc hết 15 phút). Kiến trúc P09 chạy phía sau từ một đến nhiều bản chạy, có thể khởi động lại (F1 dòng 4), nên không giữ trạng thái này trong bộ nhớ | Thêm thuộc tính hạn thanh toán vào AC-E-PackageOrder hoặc một entity riêng cho trạng thái chờ, để control đọc trạng thái từ entity khi sự kiện đến; độ lệch mốc chờ Q-93 |
| P07 | UC-015, AC-C-CancelUnderBookedClassHandler (cancelAbsenceMark, cancelWaitlistTransferMark) | Control yêu cầu huỷ mốc hẹn của UC-016 và UC-013 gắn với lớp. Mốc hẹn sống trong bộ nhớ không phù hợp kiến trúc; mốc phải là dữ liệu bền để huỷ được | Thêm entity mốc hẹn (loại mốc, đối tượng gắn, thời điểm, trạng thái) để control huỷ hoặc tạo mốc thông qua entity; liên quan Q-64 |
| P06 | Mục 3 (NFR) | P06 không có NFR sẵn sàng và bảo mật, trong khi TIEU_CHI_UU_TIEN xếp hai thuộc tính này đứng đầu; kiến trúc phải dựa vào câu hỏi mở thay cho ngưỡng | Khi Q-88, Q-89 có câu trả lời, thêm NFR vào P06 rồi chạy lại P09 |

Các đề xuất sửa của các bước trước chưa áp dụng (theo YEU_CAU_BO_SUNG) không được lặp lại ở đây.

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 1: mọi dòng F1 truy được về nguồn; không có ngưỡng tự đặt. Thước đo của dòng 3, 4, 7, 8, 9, 10 là "Chưa quy định" kèm Q vì P06 không có NFR bảo mật, sẵn sàng, bảo trì; dòng 5, 6 chưa đo được đầy đủ (Q-41, Q-42, Q-76).
- Target 8: phương án công nghệ CN2 chỉ hơn CN1 một điểm (31 so với 30) với trọng số suy từ TIEU_CHI_UU_TIEN; trạng thái "Khuyến nghị - chờ người dùng xác nhận", chờ Q-94 và Q-76. Cần dán khối F11 vào project-profile.md trước khi chạy P10.
- F10 và diagrams/P09-deployment.drawio không tạo vì MUC_CHI_TIET là GON. Hệ thống có từ hai node thực thi (thiết bị di động, trình duyệt, máy chủ, CSDL); nếu cần sơ đồ triển khai thì chạy lại P09 với mức chi tiết DAY_DU.
- Cạnh phụ thuộc phụ thuộc câu hỏi mở không được vẽ: PKG-12 --> PKG-14 (Q-45), PKG-17 --> PKG-24 (Q-15). Cạnh PKG-15 --> PKG-30 và PKG-19 --> PKG-27, PKG-29, PKG-31 dựa trên mô tả P02 của UC-016, UC-028 (chưa có lớp P08), có thể đổi khi P08 có lớp của hai use case này.
- Hành vi của AC-E-Member hỏi dữ liệu ở PKG-27, PKG-29 (F8): P09 chọn chiều phụ thuộc Domain theo F4; P10 xử lý việc di chuyển hành vi. Chưa là lỗi của P08.
- PKG-20 Persistence là một package phục vụ cả 6 package Domain; nếu P10 thấy cohesion thấp thì tách theo nhóm chức năng, không đổi layer.
- PKG-05 gộp giao diện của ACT-01 Người quan tâm và ACT-02 Hội viên vì cùng một ứng dụng và Người quan tâm trở thành Hội viên ngay sau UC-003; nếu P10 A3 cần tách giao diện của hai tác nhân thì tách PKG-05 thành hai package.
- Chọn giữa hai quy tắc (C9): YEU_CAU_BO_SUNG yêu cầu chứa được 28 use case, trong khi F8 chỉ có lớp P08 của 4 use case; theo YEU_CAU_BO_SUNG (ưu tiên 2), mọi nhóm chức năng đều có package và F8 có dòng "Nhóm chưa phân tích".
