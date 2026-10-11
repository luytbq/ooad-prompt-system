# P09 - Thiết kế kiến trúc - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P09 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | project-profile.md (mục 3 Bối cảnh kỹ thuật); 00-Conventions.md; P01-actors.md (phiên bản 1.0, Mục 2); P02-usecases.md (phiên bản 1.1, Mục 4); P05-glossary.md (phiên bản 1.0, cột Thuật ngữ, Tiếng Anh); P06-supplementary-spec.md (phiên bản 1.0, Mục 3 đến 5, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0, F1, F3, F4, Câu hỏi mở, Giả định); yeu-cau-xe-khach.md (đối chiếu nguồn). Không dùng P03-usecase-model.md (không cần kiểm tra nhóm chức năng). Placeholder: RANG_BUOC_KIEN_TRUC = Không có; TIEU_CHI_UU_TIEN = Không có; PHUONG_AN_DA_CHON = Không có; YEU_CAU_BO_SUNG = "Phạm vi phân tích hiện có: 2 use case UC-009 và UC-017 đã qua P07, P08; các use case khác chưa phân tích." Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-61, ASM-44; lần chạy này cấp Q-62 đến Q-65, ASM-45 đến ASM-48 |
| Phạm vi | Toàn hệ thống theo P02 (27 use case trong phạm vi, không tính UC-013 đã loại, 9 nhóm chức năng); mô hình phân tích mới phủ 2 use case UC-009, UC-017 nên 7 nhóm chức năng còn lại chỉ có package theo nhóm (F8) |
| Mã Q, ASM cuối đã cấp | Q-65, ASM-48 |

## F1. Yêu cầu có ý nghĩa kiến trúc

| STT | Nguồn (NFR, ràng buộc, ACT) | Kịch bản thuộc tính chất lượng (kích thích --> phản hồi --> thước đo) | Mức ưu tiên | Ảnh hưởng kiến trúc |
|---|---|---|---|---|
| 1 | NFR-04 (REQ-75); nguồn Mục 10: "Không được để hai vé cùng một chỗ trên một chuyến"; ACT-01 | Nhiều hành khách chọn cùng một chỗ của một chuyến cùng lúc --> đúng một yêu cầu giữ được chỗ, các yêu cầu còn lại nhận phản hồi chỗ không còn trống --> số yêu cầu giữ được chỗ bằng 1 | 1 (ràng buộc cứng) | Giữ chỗ là thao tác nguyên tử trên một kho dữ liệu duy nhất dùng chung cho mọi bản sao ứng dụng; không dùng khoá hay bộ nhớ trong tiến trình làm nguồn sự thật về chỗ; cần kho dữ liệu có giao dịch (F7) |
| 2 | NFR-01 (REQ-76); nguồn Mục 10: "Hệ thống không lưu thông tin thẻ của hành khách"; NFR-10; ACT-01, ACT-06 | Hành khách thanh toán trực tuyến --> thông tin thẻ do Cổng thanh toán xử lý, hệ thống chỉ gửi yêu cầu thu tiền và nhận kết quả --> số nơi lưu thông tin thẻ do hệ thống quản lý (dữ liệu, nhật ký, cấu hình) bằng 0 | 1 (ràng buộc cứng) | Tích hợp Cổng thanh toán nằm trong một package riêng (PKG-21); form của hệ thống không có trường thẻ; nhật ký không ghi dữ liệu thẻ. Cách hành khách nhập thẻ phụ thuộc API của cổng (chưa có tài liệu) |
| 3 | NFR-02 (REQ-04); nguồn Mục 2: "đặt vé không bắt buộc có tài khoản"; ACT-01 | Hành khách chưa đăng nhập, số điện thoại chưa có tài khoản đặt vé --> đặt vé hoàn tất tới khi vé được phát hành --> có (đặc tính có hoặc không) | 1 (ràng buộc cứng) | Khu vực hành khách (PKG-05) không bắt đăng nhập cho tìm chuyến và đặt vé, dùng phiên ẩn danh; khu vực nhân viên là các package giao diện khác (PKG-06 đến PKG-08) |
| 4 | NFR-07, NFR-09, NFR-14 (REQ-67, REQ-77, REQ-64, REQ-68, REQ-69); ACT-05 | Máy soát vé mất kết nối liên tục trong toàn bộ thời gian soát vé của một chuyến --> ứng dụng báo hợp lệ hoặc không hợp lệ cho mã quét, lưu kết quả cục bộ, gửi lại khi có kết nối --> 100% mã vé có trong danh sách đã nhận có kết quả đúng (ASM-35, chờ Q-31) | 2 (ngưỡng đo được) | Logic soát vé và kho dữ liệu cục bộ chạy trên máy cầm tay Android (node thứ hai); máy chủ chỉ cung cấp danh sách và nhận kết quả qua một điểm vào nhỏ (PKG-09); package Boarding chạy ở hai node (A4) |
| 5 | NFR-08 (REQ-74, REQ-01, REQ-02, REQ-03); ACT-01 | 2.000 phiên đồng thời tra cứu chuyến xe, xem sơ đồ chỗ và giữ chỗ --> hệ thống phản hồi --> không quá 2 giây ở phân vị 95, không tính thời gian chờ Cổng thanh toán và Cổng SMS (ASM-36, chờ Q-34, Q-52) | 2 (ngưỡng đo được) | Tầng ứng dụng không giữ trạng thái phiên trong bộ nhớ riêng của một bản sao, để chạy được nhiều bản sao sau bộ cân bằng tải; truy vấn đọc (tìm chuyến, sơ đồ chỗ) tách khỏi ghi; bộ nhớ đệm nếu dùng không được làm sai NFR-04 |
| 6 | NFR-05, NFR-06 (REQ-58, REQ-57); ACT-03, ACT-06 | Nhân viên điều hành huỷ chuyến, hệ thống hoàn tiền vé mua trực tuyến --> mỗi vé được yêu cầu hoàn tiền đúng một lần, số hoàn không vượt số đã thu --> số yêu cầu hoàn tiền gửi tới cổng cho mỗi vé bằng 1; số hoàn nhỏ hơn hoặc bằng số đã thu; việc tính lần xử lý lại: Chưa quy định (Q-50) | 2 (ngưỡng đo được) | Trạng thái hoàn tiền của vé và số đã hoàn của giao dịch lưu bền cùng kho với vé; mọi lần hoàn đi qua một điểm duy nhất (PKG-21); không giữ giao dịch kho dữ liệu mở trong lúc gọi cổng |
| 7 | NFR-10, NFR-11, NFR-12, NFR-13 (REQ-15, REQ-16, REQ-40, REQ-57, REQ-12, REQ-20, REQ-21, REQ-56, REQ-26, REQ-27); ACT-06, ACT-07, ACT-08 | Hệ thống ngoài không phản hồi, báo lỗi hoặc đổi API --> dữ liệu đã lưu của hệ thống không bị đảo ngược, lỗi được ghi nhận (ASM-20, ASM-31, ASM-33, ASM-37) --> mỗi lời gọi nhận một kết quả thành công hoặc không thành công; thời gian chờ và số lần thử lại: Thiết kế: chọn ở P11b, P12 (tham số kỹ thuật, C1 mục 7) | 3 (định tính) | Mỗi hệ thống ngoài được che sau một interface trong một package riêng ở Services (PKG-21, PKG-22, PKG-23); thay đổi API chỉ sửa package đó |
| 8 | NFR-03 (REQ-55); ASM-34, chờ Q-51; ACT-03 | Phiên của vai trò khác ACT-03 thực hiện huỷ chuyến --> bị từ chối --> chỉ phiên của ACT-03 huỷ được chuyến (có hoặc không) | 3 (định tính) | Phân quyền theo vai trò kiểm tra tại điểm vào của từng khu vực nhân viên; mỗi vai trò nhân viên có package giao diện riêng (PKG-06 đến PKG-08) |
| 9 | ACT-09 (REQ-14, REQ-17, REQ-31, REQ-32, REQ-69, REQ-70); BR-03; NFR-14 | Đến mốc 10 phút giữ chỗ, 60 phút hoặc 15 phút trước giờ xuất bến --> hệ thống nhả chỗ, huỷ vé đặt qua điện thoại chưa thanh toán, cấp danh sách cho máy soát vé --> thực hiện đúng mốc theo P02; độ trễ cho phép của mốc: Thiết kế: chu kỳ quét 30 giây, nhỏ hơn đơn vị phút của các mốc | 3 (định tính) | Mốc thời gian suy từ dữ liệu bền (thời hạn giữ chỗ, giờ xuất bến), không giữ trong bộ nhớ của một tiến trình, để chịu khởi động lại và nhiều bản sao; một package tiếp nhận mốc (PKG-11) gọi Application |

Thiết kế: xếp theo quy tắc F1 (không có TIEU_CHI_UU_TIEN và P06 không xếp hạng NFR): ràng buộc cứng của nguồn trước, rồi NFR có ngưỡng đo được, rồi định tính; trong cùng nhóm giữ thứ tự bảng.

## F2. Phương án và so sánh

### F2.1. Mẫu kiến trúc

Hồ sơ ghi NEN_TANG và CONG_NGHE là "Chưa chốt" nên bảng so sánh là bắt buộc. Mẫu cho phía giao diện chưa chọn ở đây mà chọn ở F3 sau khi có phương án công nghệ (A3b).

| PA | Mẫu kiến trúc (và kết hợp) | Mô tả ngắn | Điều kiện phù hợp |
|---|---|---|---|
| PA1 | Multi-layer 4 layer (Presentation, Application, Services, Domain), triển khai một khối; kết hợp client-server cho máy soát vé | Một ứng dụng web phân lớp trên máy chủ ứng dụng, một kho dữ liệu quan hệ; ứng dụng soát vé trên máy cầm tay có kho cục bộ và đồng bộ với máy chủ qua một điểm vào nhỏ | Một nhóm chức năng lớn dùng chung dữ liệu chỗ và vé; không có yêu cầu phân tán; một client đặc biệt (ngoại tuyến) |
| PA2 | Front-end/Back-end tách hai khối: front-end chạy trong trình duyệt, back-end phân lớp cung cấp API | Giao diện web (hành khách, nhân viên) là ứng dụng một trang gọi API; máy soát vé gọi cùng API | Nhiều loại client dùng chung dịch vụ, cần giao diện web tương tác phong phú |
| PA3 | Microservices theo nhóm chức năng (bán vé, vận hành, soát vé) qua cổng API hoặc broker | Mỗi nhóm một dịch vụ, một kho dữ liệu riêng, giao tiếp qua mạng | Nhiều nhóm phát triển độc lập, cần mở rộng từng phần riêng |

| Tiêu chí (từ F1) | Trọng số | PA1 | PA2 | PA3 |
|---|---|---|---|---|
| Giữ chỗ nguyên tử (NFR-04) | Cao | Tốt: một kho dữ liệu, một giao dịch cho mỗi lần giữ chỗ | Tốt: back-end vẫn một kho dữ liệu | Kém: chỗ, vé, thanh toán thuộc nhiều dịch vụ, cần giao dịch phân tán |
| Không lưu dữ liệu thẻ, phân quyền, đặt vé không cần tài khoản (NFR-01, NFR-02, NFR-03) | Cao | Tốt: một điểm vào cho HTML, chỉ thêm một API nhỏ cho máy soát vé | Trung bình: thêm API công khai cho bốn giao diện web phải bảo vệ | Trung bình: nhiều điểm vào cần bảo vệ |
| Soát vé ngoại tuyến (NFR-07, NFR-09, NFR-14) | Cao | Tốt: client có kho cục bộ, API đồng bộ nhỏ | Tốt: như PA1 | Trung bình: yêu cầu với client không đổi, thêm dịch vụ soát vé riêng |
| Hiệu năng 2.000 phiên (NFR-08) | Trung bình | Tốt: nhân bản bản sao không giữ trạng thái, gọi hàm trong tiến trình | Tốt: tài nguyên giao diện phục vụ riêng, giảm tải máy chủ | Trung bình: mỗi yêu cầu qua nhiều lời gọi mạng nội bộ, thêm độ trễ |
| Hoàn tiền đúng một lần (NFR-05, NFR-06) | Trung bình | Tốt: vé và giao dịch cùng một kho | Tốt: như PA1 | Trung bình: trạng thái hoàn tiền và vé ở hai dịch vụ |
| Cô lập hệ thống ngoài (NFR-10 đến NFR-13) | Thấp | Tốt: package tích hợp ở Services | Tốt: như PA1 | Tốt: dịch vụ tích hợp riêng |
| Phù hợp quy mô: 27 use case, 9 nhóm chức năng, nguồn không nêu yêu cầu phân tán | Trung bình | Tốt: một khối triển khai, một chuỗi công cụ | Trung bình: hai khối, hai chuỗi công cụ cho bốn giao diện web | Kém: nhiều dịch vụ, vận hành phức tạp mà không có yêu cầu nào đòi hỏi |
| Kết luận | | Chọn: đáp ứng các tiêu chí trọng số cao, đơn giản nhất | Loại: không có yêu cầu nào của nguồn cần giao diện chạy phía client, thêm bề mặt API phải bảo vệ | Loại: quá lớn so với quy mô, làm yếu NFR-04 và NFR-05 |

### F2.2. Chốt công nghệ

Hồ sơ ghi NEN_TANG và CONG_NGHE là "Chưa chốt"; PHUONG_AN_DA_CHON = Không có nên dùng phương án khuyến nghị.

| CN | Nền tảng | Phía máy chủ (ngôn ngữ, framework) | Phía giao diện | CSDL | Giao tiếp ngoài |
|---|---|---|---|---|---|
| CN1 | Web dựng phía máy chủ cho website đặt vé và phần mềm nhân viên (chạy trên trình duyệt); ứng dụng Android gốc cho máy soát vé | Java 17, Spring Boot | Web: Thymeleaf (HTML dựng phía máy chủ); máy soát vé: Kotlin, Android | PostgreSQL ở máy chủ; SQLite trên máy soát vé | HTTPS, JSON tới API Cổng thanh toán và API REST Cổng SMS; HTTPS, JSON giữa máy soát vé và máy chủ; in vé qua trình duyệt ở máy tính quầy |
| CN2 | Web dựng phía máy chủ như CN1; ứng dụng .NET MAUI cho máy soát vé | C# 12, .NET 8, ASP.NET Core MVC | Web: Razor; máy soát vé: .NET MAUI (Android) | PostgreSQL ở máy chủ; SQLite trên máy soát vé | Như CN1 |
| CN3 | Web dựng phía máy chủ như CN1; ứng dụng web tiến bộ (PWA) chạy trong trình duyệt của máy soát vé | TypeScript, Node.js, NestJS | Web: mẫu HTML dựng phía máy chủ; máy soát vé: PWA với Service Worker, IndexedDB | PostgreSQL ở máy chủ; IndexedDB trên máy soát vé | Như CN1 |

| Tiêu chí (F1, ràng buộc P06, HE_THONG_NGOAI) | CN1 | CN2 | CN3 |
|---|---|---|---|
| Giữ chỗ nguyên tử (NFR-04), hoàn tiền một lần (NFR-05, NFR-06) | Tốt: PostgreSQL có giao dịch và ràng buộc duy nhất, Spring quản lý giao dịch khai báo | Tốt: PostgreSQL, Entity Framework Core quản lý giao dịch | Tốt: PostgreSQL, thư viện giao dịch của Node.js ít chuẩn hoá hơn nhưng đủ dùng |
| Máy soát vé Android ngoại tuyến, đầu quét mã vạch (NFR-07, NFR-09, NFR-14) | Tốt: ứng dụng Android gốc cài trên máy, SQLite cục bộ, truy cập đầu quét qua API của Android | Trung bình: MAUI cần mã nối riêng cho đầu quét tích hợp, kém trưởng thành hơn Android gốc | Kém: PWA chạy trong trình duyệt, lưu trữ cục bộ có thể bị hệ điều hành dọn, đầu quét chỉ dùng được ở chế độ bàn phím; NFR-09 nêu ứng dụng cài trên thiết bị |
| Hiệu năng 2.000 phiên (NFR-08) | Tốt: nhiều bản sao Spring Boot không giữ trạng thái, có pool kết nối | Tốt: tương đương CN1 | Tốt: Node.js xử lý tốt nhiều kết nối chờ I/O |
| Tích hợp Cổng thanh toán (API chưa có tài liệu) và Cổng SMS (API REST) | Tốt: thư viện HTTP chuẩn, không phụ thuộc SDK riêng | Tốt: HttpClient chuẩn | Tốt: thư viện HTTP chuẩn |
| In vé nhiệt tại quầy (NFR-13) | Trung bình: in từ trình duyệt, không điều khiển trực tiếp máy in | Trung bình: như CN1 | Trung bình: như CN1 |
| Phù hợp quy mô dự án | Tốt: hệ sinh thái trưởng thành, hai ngôn ngữ (Java, Kotlin) cùng chạy trên JVM | Tốt: một ngôn ngữ cho máy chủ và máy cầm tay | Tốt: một ngôn ngữ cho máy chủ và máy cầm tay |

Kết luận:
- Phương án khuyến nghị: CN1. Lý do: CN1 là phương án duy nhất đạt mức Tốt ở tiêu chí khó nhất, soát vé ngoại tuyến trên máy Android có đầu quét (NFR-07, NFR-09, NFR-14); CN2 trung bình ở tiêu chí đó, CN3 kém. Ba phương án ngang nhau ở giữ chỗ nguyên tử, hiệu năng và tích hợp hệ thống ngoài, nên tiêu chí máy soát vé quyết định.
- Phương án được dùng: CN1.
- Trạng thái: Khuyến nghị - chờ người dùng xác nhận.
- Phương án phụ thuộc các quyết định kiến trúc mà nguồn không nêu: Q-62, Q-63, Q-64, Q-65 (ASM-45 đến ASM-48), và ASM-10 (Q-38).

## F3. Quyết định kiến trúc

| Mục | Nội dung |
|---|---|
| Bối cảnh | Hệ thống bán vé xe khách liên tỉnh: 12 tuyến, 3 bến xe, khoảng 80 chuyến mỗi ngày; 27 use case thuộc 9 nhóm chức năng; 5 loại người dùng (ACT-01 đến ACT-05), 3 hệ thống ngoài hoặc thiết bị (ACT-06 đến ACT-08) và bộ định thời (ACT-09). Ràng buộc cứng: không hai vé cùng một chỗ, không lưu thông tin thẻ. Một client đặc biệt: máy soát vé cầm tay Android phải soát được khi mất kết nối. Nguồn không nêu yêu cầu phân tán |
| Quyết định (mẫu và cách kết hợp) | PA1: multi-layer 4 layer, layered nới lỏng (Presentation --> Application --> Services --> Domain; Domain là layer thấp nhất, chứa lớp entity và interface kho dữ liệu; Persistence ở Services hiện thực interface đó). Triển khai thành một ứng dụng web trên máy chủ ứng dụng với một kho dữ liệu quan hệ. Kết hợp client-server cho ứng dụng soát vé: client có logic soát vé và kho cục bộ, đồng bộ với máy chủ qua HTTPS khi có kết nối. Application và Domain tách riêng vì nghiệp vụ có nhiều quy tắc trạng thái (chỗ, lần đặt, vé, hoàn tiền) cần dùng chung giữa nhiều nhóm chức năng |
| Mẫu cho phía giao diện (A3b) | Web: MVC passive trong Presentation phía máy chủ (controller nhận yêu cầu và chọn view, view không quan sát model; dữ liệu đưa cho view là view model do Application cấp). Máy soát vé Android: MVVM (View gắn dữ liệu với ViewModel). Chọn sau F2.2, khớp CN1 |
| Công nghệ | CN1 (F2.2): Java 17, Spring Boot, Thymeleaf, PostgreSQL; Kotlin, Android, SQLite trên máy soát vé. Trạng thái: Khuyến nghị - chờ người dùng xác nhận |
| Phương án đã loại và lý do | PA2: không có yêu cầu nào của nguồn cần giao diện chạy phía client; thêm API công khai phải bảo vệ (NFR-01, NFR-03) và hai chuỗi công cụ. PA3: quá lớn so với 27 use case, làm yếu giữ chỗ nguyên tử và hoàn tiền một lần (NFR-04, NFR-05). CN2: soát vé ngoại tuyến trung bình do MAUI cần mã nối cho đầu quét. CN3: soát vé ngoại tuyến kém vì PWA không bảo đảm lưu trữ cục bộ và đầu quét |
| Hệ quả tích cực | Một kho dữ liệu cho giữ chỗ và hoàn tiền nên đúng một yêu cầu thắng khi tranh chỗ. Tích hợp ngoài tách riêng nên thay đổi API chỉ sửa một package. Máy soát vé hoạt động độc lập khi mất kết nối. Một khối triển khai, vận hành đơn giản |
| Hệ quả tiêu cực và cách giảm thiểu | Kho dữ liệu duy nhất là điểm lỗi duy nhất: NFR không nêu sẵn sàng nên chấp nhận, ghi ở Rủi ro. Mở rộng theo từng nhóm chức năng không độc lập: giảm thiểu bằng bản sao không giữ trạng thái và truy vấn đọc tách khỏi ghi. Hai ngôn ngữ (Java, Kotlin) và hai nơi chạy package Boarding: giảm thiểu bằng cách giữ quy tắc soát vé nhỏ, kiểm thử cùng bộ ca. Layer Application và Domain tách làm thêm lớp chuyển tiếp: chấp nhận vì cần dùng chung entity |
| NFR được đáp ứng | NFR-01 (PKG-21), NFR-02 (PKG-05), NFR-03 (PKG-12, PKG-06 đến PKG-08), NFR-04 (PKG-20, PKG-28 cùng kho quan hệ), NFR-05 và NFR-06 (PKG-21, PKG-29), NFR-07, NFR-09, NFR-14 (PKG-09, PKG-10, PKG-18, PKG-25, PKG-26), NFR-08 (bản sao không giữ trạng thái, F7), NFR-10 đến NFR-13 (PKG-21, PKG-22, PKG-23) |
| Rủi ro còn mở | (1) Quyết định mà nguồn không nêu: phần mềm nhân viên chạy trên trình duyệt (Q-62, ASM-45); máy in vé nối máy tính quầy (Q-63, ASM-46); máy chủ đặt tập trung, ba bến xe truy cập qua Internet (Q-64, ASM-47); máy soát vé tự lấy danh sách khi có kết nối (Q-65, ASM-48). (2) API Cổng thanh toán chưa có tài liệu: chưa chứng minh được cách nhập thẻ không đi qua hệ thống (NFR-01), phụ thuộc Q-39, Q-53. (3) Mẫu máy soát vé, phiên bản Android và cách truy cập đầu quét chưa biết (ASM-10, Q-38). (4) Kích thước máy chủ và số bản sao chưa xác định vì ngưỡng NFR-08 chưa chốt (Q-34, Q-52). (5) Kho dữ liệu duy nhất là điểm lỗi duy nhất, không có NFR về sẵn sàng. (6) Mất kết nối giữa lúc Cổng thanh toán xác nhận và lúc hệ thống ghi nhận chưa có cơ chế đối soát (ASM-37, Q-53) |

## F4. Layer và package cấp cao

| PKG | Tên | Layer | Trách nhiệm | Phụ thuộc vào (PKG) | Nguồn (NFR, UC nhóm, ACT) |
|---|---|---|---|---|---|
| PKG-01 | Presentation | - | Nhận yêu cầu từ người dùng, máy soát vé và bộ định thời rồi chuyển cho layer Application. | PKG-02 | ACT-01 đến ACT-05, ACT-09; NFR-02, NFR-03 |
| PKG-02 | Application | - | Thực hiện luồng của từng use case bằng cách điều phối Domain và Services. | PKG-03, PKG-04 | P02 Mục 4 (9 nhóm chức năng); NFR-04, NFR-05 |
| PKG-03 | Services | - | Cung cấp dịch vụ kỹ thuật cho layer trên: lưu trữ, tích hợp hệ thống ngoài, bảo mật, kho cục bộ. | PKG-04 | ACT-06, ACT-07, ACT-08; NFR-01, NFR-10 đến NFR-13 |
| PKG-04 | Domain | - | Biểu diễn khái niệm nghiệp vụ, quy tắc trạng thái của chúng và interface kho dữ liệu. | - | P08 F3 (6 entity); NFR-04, NFR-06 |
| PKG-05 | PassengerWeb | PKG-01 | Hiển thị website đặt vé và tiếp nhận thao tác của hành khách (View, Controller của MVC passive). | PKG-12, PKG-13, PKG-15 | ACT-01; NFR-02, NFR-08; P08: AC-B-BookTicketOnlineForm; chưa có lớp P08 (UC-001, UC-003, UC-008, UC-010, UC-011, UC-012, UC-014) |
| PKG-06 | CounterWeb | PKG-01 | Hiển thị phần mềm bán vé và tiếp nhận thao tác của nhân viên bán vé. | PKG-12, PKG-14, PKG-15, PKG-16 | ACT-02; chưa có lớp P08 (UC-003, UC-004, UC-005, UC-006, UC-012, UC-015, UC-018) |
| PKG-07 | DispatchWeb | PKG-01 | Hiển thị phần mềm lập lịch chạy, huỷ chuyến, duy trì danh mục và tiếp nhận thao tác của nhân viên điều hành. | PKG-12, PKG-16, PKG-17 | ACT-03; NFR-03; P08: AC-B-CancelTripForm; chưa có lớp P08 (UC-003, UC-016, UC-019, UC-020, UC-021, UC-022) |
| PKG-08 | ManagementWeb | PKG-01 | Hiển thị phần mềm đặt giá, báo cáo, quản lý tài khoản nhân viên và tiếp nhận thao tác của quản lý nhà xe. | PKG-12, PKG-17, PKG-19 | ACT-04; chưa có lớp P08 (UC-002, UC-003, UC-023, UC-024, UC-027, UC-028) |
| PKG-09 | BoardingApi | PKG-01 | Cung cấp điểm vào HTTPS cho máy soát vé: đăng nhập, cấp danh sách hành khách, nhận kết quả soát. | PKG-12, PKG-18 | ACT-05; NFR-09, NFR-14; chưa có lớp P08 (UC-003, UC-025, UC-026) |
| PKG-10 | BoardingApp | PKG-01 | Hiển thị màn hình soát vé trên máy cầm tay và nhận thao tác quét của phụ xe (View, ViewModel của MVVM). | PKG-18 | ACT-05; NFR-07, NFR-09; node: Máy soát vé cầm tay; chưa có lớp P08 (UC-003, UC-026) |
| PKG-11 | TimerTrigger | PKG-01 | Phát các mốc thời gian (hết hạn giữ chỗ, quá hạn đặt chỗ qua điện thoại, cấp danh sách soát vé) sang Application. | PKG-13, PKG-14, PKG-18 | ACT-09; NFR-14; P08: AC-C-BookTicketOnlineController (handleHoldExpiry); chưa có lớp P08 (UC-007, UC-025) |
| PKG-12 | Account | PKG-02 | Điều phối các use case nhóm Tài khoản, cung cấp kiểm tra vai trò cho Presentation. | PKG-22, PKG-24, PKG-30 | P02 nhóm Tài khoản; NFR-03; chưa có lớp P08 (UC-001, UC-002, UC-003) |
| PKG-13 | Booking | PKG-02 | Điều phối các use case nhóm Đặt vé trực tuyến (tra cứu chuyến, đặt vé, thanh toán, lịch sử vé). | PKG-21, PKG-22, PKG-27, PKG-28, PKG-29 | P02 nhóm Đặt vé trực tuyến; NFR-04, NFR-08; P08: AC-C-BookTicketOnlineController, AC-C-SearchTripsController (tạm), AC-C-PayTicketOnlineController (tạm); chưa có lớp P08 (UC-008, UC-010, UC-011) |
| PKG-14 | CounterSales | PKG-02 | Điều phối các use case nhóm Bán vé tại quầy (bán vé, nhận đặt chỗ, thu tiền, huỷ đặt chỗ quá hạn). | PKG-13, PKG-23, PKG-27, PKG-28 | P02 nhóm Bán vé tại quầy; chưa có lớp P08 (UC-004, UC-005, UC-006, UC-007) |
| PKG-15 | TicketChange | PKG-02 | Điều phối các use case nhóm Trả vé và đổi vé. | PKG-13, PKG-21, PKG-22, PKG-23, PKG-27, PKG-28, PKG-29 | P02 nhóm Trả vé và đổi vé; NFR-05, NFR-06; chưa có lớp P08 (UC-012, UC-014, UC-015) |
| PKG-16 | TripManagement | PKG-02 | Điều phối các use case nhóm Lịch chạy và chuyến (lập lịch, huỷ chuyến, hoàn tiền mặt chuyến bị huỷ). | PKG-21, PKG-22, PKG-27, PKG-28, PKG-29 | P02 nhóm Lịch chạy và chuyến; NFR-03, NFR-05, NFR-06; P08: AC-C-CancelTripController; chưa có lớp P08 (UC-016, UC-018) |
| PKG-17 | ReferenceData | PKG-02 | Điều phối các use case duy trì danh mục tham chiếu (bến, tuyến, xe, tài xế, giá vé, mức tăng giá). | PKG-27 | P02 nhóm Danh mục và Giá vé; chưa có lớp P08 (UC-019 đến UC-024) |
| PKG-18 | Boarding | PKG-02 | Điều phối các use case nhóm Soát vé (cấp danh sách hành khách, soát mã vé, nhận kết quả soát), chạy ở máy chủ và máy soát vé. | PKG-25, PKG-26, PKG-27, PKG-28 | P02 nhóm Soát vé; NFR-07, NFR-14; node: Máy chủ ứng dụng, Máy soát vé cầm tay; chưa có lớp P08 (UC-025, UC-026) |
| PKG-19 | Reporting | PKG-02 | Điều phối các use case nhóm Báo cáo (doanh thu, tỉ lệ lấp đầy). | PKG-27, PKG-28, PKG-29 | P02 nhóm Báo cáo; chưa có lớp P08 (UC-027, UC-028) |
| PKG-20 | Persistence | PKG-03 | Hiện thực interface kho dữ liệu của Domain trên cơ sở dữ liệu quan hệ. | PKG-27, PKG-28, PKG-29, PKG-30 | NFR-04, NFR-05, NFR-06; P08: AC-E-* (phần lưu trữ) |
| PKG-21 | PaymentIntegration | PKG-03 | Che Cổng thanh toán sau interface thu tiền và hoàn tiền. | - | ACT-06; NFR-01, NFR-10, NFR-11; P08: AC-B-PaymentGateway |
| PKG-22 | SmsIntegration | PKG-03 | Che Cổng SMS sau interface gửi tin nhắn. | - | ACT-07; NFR-12; P08: AC-B-SmsGateway |
| PKG-23 | TicketPrinting | PKG-03 | Tạo dữ liệu vé in có mã vạch cho máy in vé nhiệt tại quầy. | - | ACT-08; NFR-13; chưa có lớp P08 (UC-004, UC-006, UC-015) |
| PKG-24 | Security | PKG-03 | Cấp, kiểm tra phiên làm việc và băm, so khớp thông tin xác thực. | PKG-30 | NFR-03; chưa có lớp P08 (UC-003) |
| PKG-25 | LocalStore | PKG-03 | Lưu cục bộ trên máy soát vé danh sách hành khách của chuyến và kết quả soát chờ gửi. | - | NFR-07; node: Máy soát vé cầm tay; chưa có lớp P08 (UC-026) |
| PKG-26 | BoardingSyncClient | PKG-03 | Trao đổi dữ liệu soát vé giữa máy soát vé và máy chủ qua HTTPS khi có kết nối. | - | NFR-14; node: Máy soát vé cầm tay; chưa có lớp P08 (UC-025, UC-026) |
| PKG-27 | Operations | PKG-04 | Chứa khái niệm chuyến xe, tuyến, bến, xe, tài xế, giá vé, mức tăng giá và interface kho dữ liệu của chúng. | - | P08: AC-E-Trip, AC-E-Fare; chưa có lớp P08 cho tuyến, bến, xe, tài xế, mức tăng giá (UC-016, UC-019 đến UC-024) |
| PKG-28 | Ticketing | PKG-04 | Chứa khái niệm chỗ, lần đặt vé, vé, quy tắc trạng thái của chúng và interface kho dữ liệu của chúng. | PKG-27, PKG-29 | P08: AC-E-Seat, AC-E-Booking, AC-E-Ticket; NFR-04 |
| PKG-29 | Payment | PKG-04 | Chứa khái niệm giao dịch thanh toán, khoản hoàn tiền và interface kho dữ liệu của chúng. | - | P08: AC-E-PaymentTransaction; NFR-05, NFR-06 |
| PKG-30 | Accounts | PKG-04 | Chứa khái niệm tài khoản, vai trò và interface kho dữ liệu của chúng. | - | chưa có lớp P08 (UC-001, UC-002, UC-003) |

Mức hợp lý: 4 layer; Presentation 7 package, Application 8, Services 7, Domain 4. Dòng layer ghi hợp các phụ thuộc của package con; F6 và F9 chỉ xét phụ thuộc giữa package.

## F5. Quy tắc ánh xạ lớp phân tích sang kiến trúc

Lưu ý: "controller" của MVC (PKG-05 đến PKG-08, phần tiếp nhận yêu cầu ở Presentation phía máy chủ) là thành phần giao diện, khác lớp control của phân tích (nằm ở Application).

| Stereotype hoặc loại lớp phân tích | Layer hoặc vai trò trong mẫu đích | Ghi chú |
|---|---|---|
| boundary giao diện người dùng | Presentation (PKG-01): View và Controller của MVC passive ở PKG-05 (ACT-01), PKG-06 (ACT-02), PKG-07 (ACT-03), PKG-08 (ACT-04); View và ViewModel của MVVM ở PKG-10 (ACT-05, máy soát vé) | Chọn package theo tác nhân của use case, không gộp giao diện của hai tác nhân; ví dụ AC-B-BookTicketOnlineForm --> PKG-05, AC-B-CancelTripForm --> PKG-07 |
| boundary kênh thông báo (SMS) | Services: subsystem PKG-22 SmsIntegration | P08 xếp AC-B-SmsGateway ở "Loại boundary" là Giao diện hệ thống nên cùng một lớp thoả cả dòng này và dòng boundary giao diện hệ thống; P08 chưa có kênh email hoặc thông báo đẩy |
| boundary giao diện hệ thống | Services: subsystem PKG-21 PaymentIntegration (Cổng thanh toán), PKG-22 SmsIntegration (Cổng SMS) | Mỗi hệ thống ngoài một package, che sau interface (P10 tạo SS và IF). Điểm vào từ máy soát vé là PKG-09 (Presentation), không phải boundary hệ thống ngoài vì máy soát vé không là tác nhân (ASM-10) |
| boundary giao diện thiết bị | Services: subsystem PKG-23 TicketPrinting (máy in vé nhiệt ACT-08) | P08 chưa có lớp loại này (UC-004, UC-006, UC-015 chưa phân tích). Đầu quét mã vạch là kênh nhập của ACT-05, thuộc PKG-10 |
| control | Application (PKG-02): lớp dịch vụ ứng dụng trong package theo nhóm chức năng của use case (bảng phụ bên dưới) | AC-C-BookTicketOnlineController, AC-C-SearchTripsController, AC-C-PayTicketOnlineController --> PKG-13; AC-C-CancelTripController --> PKG-16. Phần chờ hết thời hạn của control (after(BR-03)) được PKG-11 kích hoạt từ dữ liệu bền, control không giữ bộ đếm trong bộ nhớ |
| entity (phần hành vi nghiệp vụ) | Domain (PKG-04): lớp miền trong package theo khái niệm | AC-E-Trip, AC-E-Fare --> PKG-27 Operations; AC-E-Seat, AC-E-Booking, AC-E-Ticket --> PKG-28 Ticketing; AC-E-PaymentTransaction --> PKG-29 Payment |
| entity (phần lưu trữ) | Interface kho dữ liệu ở Domain (cùng package với entity); hiện thực ở PKG-20 Persistence (Services) | Persistence hiện thực interface đi xuống Domain; Application chỉ dùng interface |

Bảng phụ: nhóm chức năng của P02 --> package.

| Nhóm chức năng (UC) | Package Application | Package Presentation | Package khác |
|---|---|---|---|
| Tài khoản (UC-001, UC-002, UC-003) | PKG-12 Account | PKG-05 (UC-001, UC-003 của hành khách), PKG-06, PKG-07, PKG-08 (đăng nhập nhân viên, UC-002 ở PKG-08), PKG-09 và PKG-10 (đăng nhập phụ xe) | PKG-24 Security, PKG-30 Accounts |
| Bán vé tại quầy (UC-004, UC-005, UC-006, UC-007) | PKG-14 CounterSales | PKG-06; UC-007 do PKG-11 kích hoạt | PKG-23 TicketPrinting |
| Đặt vé trực tuyến (UC-008, UC-009, UC-010, UC-011) | PKG-13 Booking | PKG-05 | PKG-21, PKG-22 |
| Trả vé và đổi vé (UC-012, UC-014, UC-015) | PKG-15 TicketChange | PKG-05 (UC-012, UC-014), PKG-06 (UC-012, UC-015) | PKG-21, PKG-22, PKG-23 |
| Lịch chạy và chuyến (UC-016, UC-017, UC-018) | PKG-16 TripManagement | PKG-07 (UC-016, UC-017), PKG-06 (UC-018) | PKG-21, PKG-22 |
| Danh mục (UC-019 đến UC-022) | PKG-17 ReferenceData | PKG-07 | PKG-27 |
| Giá vé (UC-023, UC-024) | PKG-17 ReferenceData | PKG-08 | PKG-27 |
| Soát vé (UC-025, UC-026) | PKG-18 Boarding | PKG-10 (máy soát vé), PKG-09 (máy chủ); UC-025 do PKG-11 kích hoạt | PKG-25, PKG-26 |
| Báo cáo (UC-027, UC-028) | PKG-19 Reporting | PKG-08 | - |

## F6. Quy tắc dependency

- QT-1: Kiểu layered nới lỏng: package được phụ thuộc package cùng layer (một chiều) hoặc ở layer dưới, không bắt buộc layer liền dưới. Lý do: Application cần dùng trực tiếp lớp miền và interface kho dữ liệu ở Domain; ép đi qua Services thêm lớp chuyển tiếp không mang trách nhiệm.
- QT-2: Không có mũi tên dependency hoặc realization đi từ layer dưới lên layer trên.
- QT-3: Không có vòng phụ thuộc giữa các package, kể cả vòng qua nhiều package.
- QT-4: Package ở Presentation chỉ phụ thuộc package ở Application, không phụ thuộc trực tiếp Services hoặc Domain; thay đổi công nghệ giao diện hoặc kho dữ liệu không lan qua nhau.
- QT-5: Interface kho dữ liệu, kể cả truy vấn tổng hợp cho báo cáo, đặt ở Domain; PKG-20 Persistence hiện thực (realization đi xuống); không package nào phụ thuộc PKG-20.
- QT-6: Application phụ thuộc interface của PKG-21, PKG-22, PKG-23 (do chính package đó định nghĩa ở Services), không phụ thuộc lớp bên trong các subsystem này.
- QT-7: Trao đổi giữa máy soát vé và PKG-09 trên máy chủ đi qua mạng bằng HTTPS, không là phụ thuộc package; được mô tả ở F7 và F10, không vẽ ở F9.
- QT-8: Hiện không có chỗ nào layer dưới cần gọi ngược lên layer trên (thông tin đi lên bằng giá trị trả về); nếu P10 phát sinh thông báo hoặc callback thì layer dưới định nghĩa interface, layer trên hiện thực (DIP).

Bảng kiểm tra, một dòng cho mỗi phụ thuộc trong F4 (58 dòng). Phụ thuộc cùng layer: PKG-14 --> PKG-13, PKG-15 --> PKG-13, PKG-28 --> PKG-27, PKG-28 --> PKG-29; đồ thị phụ thuộc không có vòng.

| Phụ thuộc (PKG --> PKG) | Hợp lệ | Quy tắc áp dụng |
|---|---|---|
| PKG-05 PassengerWeb --> PKG-12 Account | Có | QT-1, QT-4 |
| PKG-05 PassengerWeb --> PKG-13 Booking | Có | QT-1, QT-4 |
| PKG-05 PassengerWeb --> PKG-15 TicketChange | Có | QT-1, QT-4 |
| PKG-06 CounterWeb --> PKG-12 Account | Có | QT-1, QT-4 |
| PKG-06 CounterWeb --> PKG-14 CounterSales | Có | QT-1, QT-4 |
| PKG-06 CounterWeb --> PKG-15 TicketChange | Có | QT-1, QT-4 |
| PKG-06 CounterWeb --> PKG-16 TripManagement | Có | QT-1, QT-4 |
| PKG-07 DispatchWeb --> PKG-12 Account | Có | QT-1, QT-4 |
| PKG-07 DispatchWeb --> PKG-16 TripManagement | Có | QT-1, QT-4 |
| PKG-07 DispatchWeb --> PKG-17 ReferenceData | Có | QT-1, QT-4 |
| PKG-08 ManagementWeb --> PKG-12 Account | Có | QT-1, QT-4 |
| PKG-08 ManagementWeb --> PKG-17 ReferenceData | Có | QT-1, QT-4 |
| PKG-08 ManagementWeb --> PKG-19 Reporting | Có | QT-1, QT-4 |
| PKG-09 BoardingApi --> PKG-12 Account | Có | QT-1, QT-4 |
| PKG-09 BoardingApi --> PKG-18 Boarding | Có | QT-1, QT-4 |
| PKG-10 BoardingApp --> PKG-18 Boarding | Có | QT-1, QT-4 |
| PKG-11 TimerTrigger --> PKG-13 Booking | Có | QT-1, QT-4 |
| PKG-11 TimerTrigger --> PKG-14 CounterSales | Có | QT-1, QT-4 |
| PKG-11 TimerTrigger --> PKG-18 Boarding | Có | QT-1, QT-4 |
| PKG-12 Account --> PKG-22 SmsIntegration | Có | QT-1, QT-6 |
| PKG-12 Account --> PKG-24 Security | Có | QT-1 |
| PKG-12 Account --> PKG-30 Accounts | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-13 Booking --> PKG-21 PaymentIntegration | Có | QT-1, QT-6 |
| PKG-13 Booking --> PKG-22 SmsIntegration | Có | QT-1, QT-6 |
| PKG-13 Booking --> PKG-27 Operations | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-13 Booking --> PKG-28 Ticketing | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-13 Booking --> PKG-29 Payment | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-14 CounterSales --> PKG-13 Booking | Có | QT-1, QT-3 (cùng layer, một chiều) |
| PKG-14 CounterSales --> PKG-23 TicketPrinting | Có | QT-1, QT-6 |
| PKG-14 CounterSales --> PKG-27 Operations | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-14 CounterSales --> PKG-28 Ticketing | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-15 TicketChange --> PKG-13 Booking | Có | QT-1, QT-3 (cùng layer, một chiều) |
| PKG-15 TicketChange --> PKG-21 PaymentIntegration | Có | QT-1, QT-6 |
| PKG-15 TicketChange --> PKG-22 SmsIntegration | Có | QT-1, QT-6 |
| PKG-15 TicketChange --> PKG-23 TicketPrinting | Có | QT-1, QT-6 |
| PKG-15 TicketChange --> PKG-27 Operations | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-15 TicketChange --> PKG-28 Ticketing | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-15 TicketChange --> PKG-29 Payment | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-16 TripManagement --> PKG-21 PaymentIntegration | Có | QT-1, QT-6 |
| PKG-16 TripManagement --> PKG-22 SmsIntegration | Có | QT-1, QT-6 |
| PKG-16 TripManagement --> PKG-27 Operations | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-16 TripManagement --> PKG-28 Ticketing | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-16 TripManagement --> PKG-29 Payment | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-17 ReferenceData --> PKG-27 Operations | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-18 Boarding --> PKG-25 LocalStore | Có | QT-1 |
| PKG-18 Boarding --> PKG-26 BoardingSyncClient | Có | QT-1 |
| PKG-18 Boarding --> PKG-27 Operations | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-18 Boarding --> PKG-28 Ticketing | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-19 Reporting --> PKG-27 Operations | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-19 Reporting --> PKG-28 Ticketing | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-19 Reporting --> PKG-29 Payment | Có | QT-1, QT-5 (dùng entity và interface kho dữ liệu) |
| PKG-20 Persistence --> PKG-27 Operations | Có | QT-1, QT-2, QT-5 (realization đi xuống) |
| PKG-20 Persistence --> PKG-28 Ticketing | Có | QT-1, QT-2, QT-5 (realization đi xuống) |
| PKG-20 Persistence --> PKG-29 Payment | Có | QT-1, QT-2, QT-5 (realization đi xuống) |
| PKG-20 Persistence --> PKG-30 Accounts | Có | QT-1, QT-2, QT-5 (realization đi xuống) |
| PKG-24 Security --> PKG-30 Accounts | Có | QT-1, QT-2 |
| PKG-28 Ticketing --> PKG-27 Operations | Có | QT-1, QT-3 (cùng layer, một chiều) |
| PKG-28 Ticketing --> PKG-29 Payment | Có | QT-1, QT-3 (cùng layer, một chiều) |

## F7. Định hướng giao tiếp ngoài và dữ liệu

| ACT (hệ thống ngoài, thiết bị, tác nhân thời gian) hoặc node khác của chính hệ thống | PKG chứa | Nguyên tắc cô lập | Rủi ro (lỗi, timeout, thay đổi API) |
|---|---|---|---|
| ACT-06 Cổng thanh toán | PKG-21 PaymentIntegration (Services, máy chủ) | Interface thu tiền và hoàn tiền; Application chỉ thấy kết quả thành công hoặc không thành công; hệ thống gọi cổng, cổng không tự gửi thông báo (ASM-11); không mang dữ liệu thẻ qua hệ thống (NFR-01) | API chưa có tài liệu (HE_THONG_NGOAI); cổng không trả kết quả (ASM-37, Q-53); giao dịch thành công đến sau hạn giữ chỗ (ASM-22); hoàn tiền không thành công hoặc hoàn một phần (ASM-33, ASM-32, Q-50, Q-20); thay đổi API chỉ sửa PKG-21 |
| ACT-07 Cổng SMS | PKG-22 SmsIntegration (Services, máy chủ) | Interface gửi tin nhắn một chiều từ hệ thống tới cổng, nhận kết quả của lời gọi; vé và chuyến đã lưu không bị đảo ngược khi gửi lỗi (NFR-12) | SMS không gửi được hoặc cổng không phản hồi (ASM-20, Q-35, ASM-31, Q-49); thay đổi API REST của nhà mạng |
| ACT-08 Máy in vé nhiệt | PKG-23 TicketPrinting (Services, máy chủ) tạo dữ liệu vé in có mã vạch; trình duyệt trên Máy tính quầy gửi lệnh in (ASM-46) | Interface tạo vé in; máy chủ không điều khiển máy in trực tiếp | Lỗi in, hết giấy không báo ngược về máy chủ; máy in nối cách khác (Q-63); loại mã vạch phải đọc được bằng đầu quét của máy soát vé, chọn ở P11b |
| ACT-09 Bộ định thời | PKG-11 TimerTrigger (Presentation, máy chủ) | Bộ định thời nội bộ đọc mốc từ dữ liệu bền (thời hạn giữ chỗ, giờ xuất bến, trạng thái chuyến) rồi gọi Application; không có logic nghiệp vụ | Nhiều bản sao cùng thấy một mốc, xử lý trùng: dùng trạng thái trong kho dữ liệu để mỗi mốc chỉ xử lý một lần; lệch đồng hồ giữa các máy chủ |
| Node khác của hệ thống: Máy soát vé cầm tay (không là tác nhân, ASM-10) | PKG-09 BoardingApi (máy chủ) và PKG-26 BoardingSyncClient (máy soát vé) | Máy soát vé tự lấy danh sách hành khách của chuyến từ mốc 15 phút trước giờ xuất bến khi có kết nối (ASM-48) và gửi kết quả soát đã lưu; nội dung trao đổi là dữ liệu soát vé, không lộ cấu trúc kho dữ liệu | Mất kết nối giữa chừng; máy chưa nhận được danh sách (Q-54, ASM-38); vé phát sinh sau khi cấp danh sách (Q-29); nội dung danh sách (Q-30); kết quả soát gửi trùng khi gửi lại |

| Mục | Quyết định | Lý do |
|---|---|---|
| Loại cơ chế lưu trữ | Kho quan hệ (PostgreSQL theo CN1) ở máy chủ; SQLite cục bộ trên máy soát vé | NFR-04, NFR-05, NFR-06 cần giao dịch và ràng buộc duy nhất; báo cáo UC-027, UC-028 cần truy vấn tổng hợp. Máy soát vé chỉ cần kho nhỏ cho một chuyến (Thiết kế: dung lượng nhỏ, không cần máy chủ CSDL) |
| Layer truy cập dữ liệu | PKG-20 Persistence (Services) hiện thực interface kho dữ liệu ở Domain; PKG-25 LocalStore trên máy soát vé | QT-5 và A6 |
| Chiến lược giao dịch mức cao | Giữ chỗ và phát hành vé: mỗi thao tác một giao dịch kho dữ liệu, ràng buộc duy nhất trên (chuyến, chỗ) cho vé và giữ chỗ còn hiệu lực. Hoàn tiền: ghi nhận trạng thái hoàn tiền của vé trước và sau lời gọi cổng ở hai giao dịch ngắn, không giữ giao dịch mở lúc gọi cổng; mỗi vé một khoá chống gọi trùng. Mốc thời gian: PKG-11 đọc dữ liệu bền | NFR-04 (số yêu cầu giữ được chỗ bằng 1), NFR-05 (hoàn đúng một lần), NFR-06 (số hoàn không vượt số thu). Thiết kế: thao tác ngoài hệ thống không nên giữ khoá cơ sở dữ liệu |
| Dữ liệu cần bảo vệ | Không lưu thông tin thẻ (NFR-01); thông tin xác thực của nhân viên lưu dạng băm một chiều có muối; họ tên và số điện thoại người đi, mã vé truyền qua HTTPS; kho cục bộ trên máy soát vé chỉ chứa dữ liệu của chuyến đang soát | NFR-01, NFR-03. Thiết kế: thông lệ bảo mật mặc định (băm có muối, mã hoá khi truyền, giảm thiểu dữ liệu trên thiết bị); nội dung danh sách cấp cho máy chờ Q-30 |
| Phiên làm việc | Trạng thái phiên (hành khách ẩn danh, nhân viên) lưu ở kho dữ liệu hoặc cookie có ký, không lưu trong bộ nhớ riêng của một bản sao | NFR-08 (nhiều bản sao sau bộ cân bằng tải) |

## F8. Kiểm tra chứa mô hình phân tích

| Nhóm lớp phân tích (theo stereotype hoặc nhóm chức năng) | Số lớp | Layer, PKG đích | Vấn đề |
|---|---|---|---|
| boundary giao diện người dùng (AC-B-BookTicketOnlineForm, AC-B-CancelTripForm) | 2 | Presentation: PKG-05, PKG-07 | Không có |
| boundary giao diện hệ thống (AC-B-SmsGateway, AC-B-PaymentGateway) | 2 | Services: PKG-22, PKG-21 | AC-B-SmsGateway cũng là kênh thông báo; xếp theo "Loại boundary" của P08 |
| boundary giao diện thiết bị | 0 | Services: PKG-23 (dự kiến) | P08 chưa có lớp loại này (UC-004, UC-006, UC-015 chưa phân tích) |
| control nhóm Đặt vé trực tuyến (AC-C-BookTicketOnlineController, AC-C-SearchTripsController tạm, AC-C-PayTicketOnlineController tạm) | 3 | Application: PKG-13 | Hai control tạm chờ P07 của UC-008, UC-010. Kiểm tra trạng thái chờ (A7): control chờ kết quả thanh toán và chờ hết thời hạn giữ chỗ, nhưng trạng thái đã nằm trong entity Booking (status, holdExpiry); kiến trúc nhiều bản sao và khởi động lại vẫn giữ được, PKG-11 kích hoạt xử lý hết hạn từ dữ liệu bền. Không cần Đề xuất sửa P07 |
| control nhóm Lịch chạy và chuyến (AC-C-CancelTripController) | 1 | Application: PKG-16 | Hai thao tác cancelOverdueReservationMark, cancelPassengerListMark ("huỷ mốc") thực hiện bằng cách PKG-11 kiểm tra trạng thái chuyến khi mốc đến; không cần entity cho mốc |
| entity: AC-E-Trip, AC-E-Fare | 2 | Domain: PKG-27 Operations | Fare chưa có quan hệ entity (P08 Vấn đề còn mở); chưa có lớp tuyến, bến, xe, tài xế |
| entity: AC-E-Seat, AC-E-Booking, AC-E-Ticket | 3 | Domain: PKG-28 Ticketing | Ranh giới Seat phụ thuộc Q-59, Q-60; PKG-28 phụ thuộc PKG-29 vì R-20 (Ticket - PaymentTransaction) |
| entity: AC-E-PaymentTransaction | 1 | Domain: PKG-29 Payment | Không có |
| Nhóm chưa phân tích | 0 | Tài khoản (UC-001, UC-002, UC-003): PKG-12, PKG-24, PKG-30; Bán vé tại quầy (UC-004 đến UC-007): PKG-14, PKG-06, PKG-23; Đặt vé trực tuyến phần UC-008, UC-010, UC-011: PKG-13; Trả vé và đổi vé (UC-012, UC-014, UC-015): PKG-15; Lịch chạy và chuyến phần UC-016, UC-018: PKG-16; Danh mục (UC-019 đến UC-022) và Giá vé (UC-023, UC-024): PKG-17; Soát vé (UC-025, UC-026): PKG-18, PKG-09, PKG-10, PKG-25, PKG-26; Báo cáo (UC-027, UC-028): PKG-19, PKG-08 | 25 trong 27 use case chưa có P07; các package này đã có chỗ nhưng trách nhiệm chi tiết chờ P07, P08 của use case đó |

Tổng: 14 lớp hoạt động và tạm trong P08, đều có layer đích.

## F9. Package diagram

File diagrams/P09-package-layers.drawio. x, y là toạ độ tuyệt đối trên trang (đơn vị điểm ảnh); trong file .drawio, node con của layer dùng toạ độ tương đối với layer chứa nó.

a) Bảng Node

| ID (PKG) | Loại | Nhãn | Stereotype | Thuộc về (PKG layer chứa) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| PKG-01 | Layer | Presentation | «layer» | - | Layer trên cùng | 20 | 20 | 2680 | 140 |
| PKG-02 | Layer | Application | «layer» | - | Layer giữa trên | 20 | 390 | 2680 | 140 |
| PKG-03 | Layer | Services | «layer» | - | Layer giữa dưới | 20 | 890 | 2680 | 140 |
| PKG-04 | Layer | Domain | «layer» | - | Layer thấp nhất | 20 | 1300 | 2680 | 140 |
| PKG-05 | Package | PassengerWeb | - | PKG-01 | Máy chủ ứng dụng; giao diện của ACT-01 | 60 | 70 | 220 | 60 |
| PKG-06 | Package | CounterWeb | - | PKG-01 | Máy chủ ứng dụng; giao diện của ACT-02 | 430 | 70 | 220 | 60 |
| PKG-07 | Package | DispatchWeb | - | PKG-01 | Máy chủ ứng dụng; giao diện của ACT-03 | 800 | 70 | 220 | 60 |
| PKG-08 | Package | ManagementWeb | - | PKG-01 | Máy chủ ứng dụng; giao diện của ACT-04 | 1170 | 70 | 220 | 60 |
| PKG-09 | Package | BoardingApi | - | PKG-01 | Máy chủ ứng dụng; điểm vào HTTPS cho máy soát vé | 1540 | 70 | 220 | 60 |
| PKG-10 | Package | BoardingApp | - | PKG-01 | Máy soát vé cầm tay; giao diện của ACT-05 | 1910 | 70 | 220 | 60 |
| PKG-11 | Package | TimerTrigger | - | PKG-01 | Máy chủ ứng dụng; đại diện ACT-09 | 2280 | 70 | 220 | 60 |
| PKG-12 | Package | Account | - | PKG-02 | - | 60 | 440 | 220 | 60 |
| PKG-13 | Package | Booking | - | PKG-02 | - | 360 | 440 | 220 | 60 |
| PKG-14 | Package | CounterSales | - | PKG-02 | - | 660 | 440 | 220 | 60 |
| PKG-15 | Package | TicketChange | - | PKG-02 | - | 960 | 440 | 220 | 60 |
| PKG-16 | Package | TripManagement | - | PKG-02 | - | 1520 | 440 | 220 | 60 |
| PKG-17 | Package | ReferenceData | - | PKG-02 | - | 1820 | 440 | 220 | 60 |
| PKG-18 | Package | Boarding | - | PKG-02 | Chạy ở hai node: Máy chủ ứng dụng và Máy soát vé cầm tay; mỗi node chỉ dùng các phụ thuộc có mặt trên node đó (PKG-25, PKG-26 chỉ có trên máy soát vé) | 2120 | 440 | 220 | 60 |
| PKG-19 | Package | Reporting | - | PKG-02 | - | 2420 | 440 | 220 | 60 |
| PKG-20 | Package | Persistence | - | PKG-03 | Máy chủ ứng dụng; hiện thực interface kho dữ liệu của Domain | 2160 | 940 | 220 | 60 |
| PKG-21 | Package | PaymentIntegration | - | PKG-03 | Máy chủ ứng dụng; che ACT-06 | 700 | 940 | 220 | 60 |
| PKG-22 | Package | SmsIntegration | - | PKG-03 | Máy chủ ứng dụng; che ACT-07 | 380 | 940 | 220 | 60 |
| PKG-23 | Package | TicketPrinting | - | PKG-03 | Máy chủ ứng dụng; che ACT-08 | 1020 | 940 | 220 | 60 |
| PKG-24 | Package | Security | - | PKG-03 | - | 60 | 940 | 220 | 60 |
| PKG-25 | Package | LocalStore | - | PKG-03 | Máy soát vé cầm tay | 1520 | 940 | 220 | 60 |
| PKG-26 | Package | BoardingSyncClient | - | PKG-03 | Máy soát vé cầm tay | 1840 | 940 | 220 | 60 |
| PKG-27 | Package | Operations | - | PKG-04 | - | 560 | 1350 | 220 | 60 |
| PKG-28 | Package | Ticketing | - | PKG-04 | - | 1020 | 1350 | 220 | 60 |
| PKG-29 | Package | Payment | - | PKG-04 | - | 1560 | 1350 | 220 | 60 |
| PKG-30 | Package | Accounts | - | PKG-04 | - | 100 | 1350 | 220 | 60 |

b) Bảng Edge

Mọi cạnh là phụ thuộc nét đứt đầu mở từ package phụ thuộc tới package được dùng, 58 cạnh, khớp từng dòng với cột "Phụ thuộc vào" của F4. Cạnh của PKG-20 tới Domain là phụ thuộc kèm realization interface kho dữ liệu đi xuống. Cột Điểm uốn là toạ độ tuyệt đối từ nguồn tới đích.

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | PKG-05 | PKG-12 | Dependency | - | - | (170,180); (180,180) |
| E-02 | PKG-05 | PKG-13 | Dependency | - | - | (270,200); (370,200) |
| E-03 | PKG-05 | PKG-15 | Dependency | - | - | (250,190); (980,190) |
| E-04 | PKG-06 | PKG-12 | Dependency | - | - | (440,210); (230,210) |
| E-05 | PKG-06 | PKG-14 | Dependency | - | - | (640,240); (680,240) |
| E-06 | PKG-06 | PKG-15 | Dependency | - | - | (620,230); (1030,230) |
| E-07 | PKG-06 | PKG-16 | Dependency | - | - | (600,220); (1540,220) |
| E-08 | PKG-07 | PKG-12 | Dependency | - | - | (810,250); (210,250) |
| E-09 | PKG-07 | PKG-16 | Dependency | - | - | (1010,270); (1570,270) |
| E-10 | PKG-07 | PKG-17 | Dependency | - | - | (990,260); (1840,260) |
| E-11 | PKG-08 | PKG-12 | Dependency | - | - | (1180,280); (150,280) |
| E-12 | PKG-08 | PKG-17 | Dependency | - | - | (1270,300); (1860,300) |
| E-13 | PKG-08 | PKG-19 | Dependency | - | - | (1250,290); (2440,290) |
| E-14 | PKG-09 | PKG-12 | Dependency | - | - | (1550,310); (130,310) |
| E-15 | PKG-09 | PKG-18 | Dependency | - | Phần Boarding chạy trên máy chủ | (1750,320); (2140,320) |
| E-16 | PKG-10 | PKG-18 | Dependency | - | Phần Boarding chạy trên máy soát vé | (2120,330); (2160,330) |
| E-17 | PKG-11 | PKG-13 | Dependency | - | Mốc hết thời hạn giữ chỗ của UC-009 | (2290,340); (560,340) |
| E-18 | PKG-11 | PKG-14 | Dependency | - | Mốc 60 phút trước giờ xuất bến của UC-007 | (2310,350); (860,350) |
| E-19 | PKG-11 | PKG-18 | Dependency | - | Mốc 15 phút trước giờ xuất bến của UC-025 | (2330,360); (2320,360) |
| E-20 | PKG-12 | PKG-22 | Dependency | - | - | (260,740); (390,740) |
| E-21 | PKG-12 | PKG-24 | Dependency | - | - | (160,730); (190,730) |
| E-22 | PKG-12 | PKG-30 | Dependency | - | - | (240,550); (1280,550); (1280,1050); (310,1050) |
| E-23 | PKG-13 | PKG-21 | Dependency | - | - | (550,760); (710,760) |
| E-24 | PKG-13 | PKG-22 | Dependency | - | - | (490,750); (460,750) |
| E-25 | PKG-13 | PKG-27 | Dependency | - | - | (510,580); (1290,580); (1290,1080); (760,1080) |
| E-26 | PKG-13 | PKG-28 | Dependency | - | - | (470,570); (1310,570); (1310,1070); (1220,1070) |
| E-27 | PKG-13 | PKG-29 | Dependency | - | - | (450,560); (1340,560); (1340,1060); (1610,1060) |
| E-28 | PKG-14 | PKG-13 | Dependency | - | Cùng layer; UC-004, UC-005 dùng đoạn tra cứu chuyến của UC-008 | (670,770); (570,770) |
| E-29 | PKG-14 | PKG-23 | Dependency | - | - | (870,780); (1040,780) |
| E-30 | PKG-14 | PKG-27 | Dependency | - | - | (850,600); (1300,600); (1300,1100); (740,1100) |
| E-31 | PKG-14 | PKG-28 | Dependency | - | - | (830,590); (1330,590); (1330,1090); (1200,1090) |
| E-32 | PKG-15 | PKG-13 | Dependency | - | Cùng layer; UC-014, UC-015 dùng đoạn tra cứu chuyến của UC-008, thanh toán UC-010 | (970,790); (530,790) |
| E-33 | PKG-15 | PKG-21 | Dependency | - | - | (1020,810); (910,810) |
| E-34 | PKG-15 | PKG-22 | Dependency | - | - | (1000,800); (590,800) |
| E-35 | PKG-15 | PKG-23 | Dependency | - | - | (1130,820); (1070,820) |
| E-36 | PKG-15 | PKG-27 | Dependency | - | - | (1170,630); (1320,630); (1320,1130); (720,1130) |
| E-37 | PKG-15 | PKG-28 | Dependency | - | - | (1150,620); (1350,620); (1350,1120); (1160,1120) |
| E-38 | PKG-15 | PKG-29 | Dependency | - | - | (1110,610); (1380,610); (1380,1110); (1630,1110) |
| E-39 | PKG-16 | PKG-21 | Dependency | - | - | (1560,840); (890,840) |
| E-40 | PKG-16 | PKG-22 | Dependency | - | - | (1530,830); (540,830) |
| E-41 | PKG-16 | PKG-27 | Dependency | - | - | (1580,640); (1360,640); (1360,1140); (700,1140) |
| E-42 | PKG-16 | PKG-28 | Dependency | - | - | (1600,650); (1390,650); (1390,1150); (1140,1150) |
| E-43 | PKG-16 | PKG-29 | Dependency | - | - | (1620,660); (1420,660); (1420,1160); (1650,1160) |
| E-44 | PKG-17 | PKG-27 | Dependency | - | - | (1830,670); (1370,670); (1370,1170); (660,1170) |
| E-45 | PKG-18 | PKG-25 | Dependency | - | - | (2170,850); (1730,850) |
| E-46 | PKG-18 | PKG-26 | Dependency | - | - | (2190,860); (2050,860) |
| E-47 | PKG-18 | PKG-27 | Dependency | - | - | (2130,680); (1400,680); (1400,1180); (630,1180) |
| E-48 | PKG-18 | PKG-28 | Dependency | - | - | (2150,690); (1430,690); (1430,1190); (1120,1190) |
| E-49 | PKG-19 | PKG-27 | Dependency | - | - | (2430,700); (1410,700); (1410,1200); (610,1200) |
| E-50 | PKG-19 | PKG-28 | Dependency | - | - | (2450,710); (1440,710); (1440,1210); (1100,1210) |
| E-51 | PKG-19 | PKG-29 | Dependency | - | - | (2470,720); (1450,720); (1450,1220); (1670,1220) |
| E-52 | PKG-20 | PKG-27 | Dependency | - | Persistence hiện thực interface kho dữ liệu đặt ở Domain (đi xuống) | (2200,1250); (580,1250) |
| E-53 | PKG-20 | PKG-28 | Dependency | - | Persistence hiện thực interface kho dữ liệu đặt ở Domain (đi xuống) | (2220,1260); (1080,1260) |
| E-54 | PKG-20 | PKG-29 | Dependency | - | Persistence hiện thực interface kho dữ liệu đặt ở Domain (đi xuống) | (2240,1270); (1770,1270) |
| E-55 | PKG-20 | PKG-30 | Dependency | - | Persistence hiện thực interface kho dữ liệu đặt ở Domain (đi xuống) | (2180,1240); (290,1240) |
| E-56 | PKG-24 | PKG-30 | Dependency | - | - | (200,1230); (140,1230) |
| E-57 | PKG-28 | PKG-27 | Dependency | - | Cùng layer; Booking, Seat, Ticket tham chiếu Trip | (1050,1460); (770,1460) |
| E-58 | PKG-28 | PKG-29 | Dependency | - | Cùng layer; Ticket tham chiếu PaymentTransaction (R-20) | (1230,1470); (1590,1470) |

## F10. Deployment diagram

File diagrams/P09-deployment.drawio. Hệ thống có bảy node thực thi (không tính hai hệ thống ngoài) nên cần sơ đồ (MUC_CHI_TIET = DAY_DU). Không ghi địa chỉ IP, tên máy cụ thể.

a) Bảng Node

| ID | Node (thiết bị, môi trường thực thi) | Artifact triển khai | Package chứa | Ghi chú |
|---|---|---|---|---|
| N-01 | Thiết bị của hành khách (trình duyệt web) | - | - | Chỉ hiển thị HTML do PKG-05 sinh ra (Presentation phía máy chủ) |
| N-02 | Máy tính quầy bán vé (trình duyệt web) | - | - | Hiển thị HTML của PKG-06 và gửi lệnh in tới N-07 (ASM-45, ASM-46) |
| N-03 | Máy tính nhân viên điều hành, quản lý (trình duyệt web) | - | - | Hiển thị HTML của PKG-07, PKG-08 |
| N-04 | Máy soát vé cầm tay (Android, đầu quét mã vạch) | A-01 Ứng dụng soát vé | PKG-10, PKG-18 (phần chạy trên máy soát vé), PKG-25, PKG-26 | Do nhà xe tự trang bị (HE_THONG_NGOAI); ứng dụng do dự án xây dựng (ASM-10, Q-38); mẫu máy chưa biết |
| N-05 | Máy chủ ứng dụng (môi trường JVM) | A-02 Ứng dụng web | PKG-05 đến PKG-09, PKG-11 đến PKG-24 (gồm PKG-18 phần máy chủ), PKG-27 đến PKG-30 | Một node baseline, có thể chạy nhiều bản sao không giữ trạng thái (ASM-47, Q-64) |
| N-06 | Máy chủ cơ sở dữ liệu | A-03 Cơ sở dữ liệu quan hệ | - (PKG-20 truy cập từ N-05) | Kho dữ liệu duy nhất của hệ thống (F7) |
| N-07 | Máy in vé nhiệt (ACT-08) | - | - | Thiết bị gắn với N-02 (ASM-46, Q-63) |
| N-08 | Cổng thanh toán của đối tác (ACT-06, hệ thống ngoài) | - | - | Chỉ để thể hiện đường truyền; không thuộc hệ thống |
| N-09 | Cổng SMS của nhà mạng (ACT-07, hệ thống ngoài) | - | - | Chỉ để thể hiện đường truyền; không thuộc hệ thống |

b) Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn giao thức | Ghi chú |
|---|---|---|---|---|---|
| L-01 | N-01 | N-05 | Communication path | Internet, mã hoá | Hành khách truy cập website |
| L-02 | N-02 | N-05 | Communication path | Internet, mã hoá | Quầy ở ba bến xe truy cập máy chủ tập trung (ASM-47) |
| L-03 | N-03 | N-05 | Communication path | Internet, mã hoá | Nhân viên điều hành, quản lý |
| L-04 | N-04 | N-05 | Communication path | Mạng di động, mã hoá, có thể gián đoạn | Đồng bộ danh sách và kết quả soát (PKG-26 --> PKG-09); máy vẫn soát được khi gián đoạn |
| L-05 | N-05 | N-06 | Communication path | Mạng nội bộ máy chủ | PKG-20 truy cập kho dữ liệu |
| L-06 | N-05 | N-08 | Communication path | Internet, mã hoá | PKG-21 gọi API thanh toán và hoàn tiền |
| L-07 | N-05 | N-09 | Communication path | Internet, mã hoá | PKG-22 gọi API REST gửi SMS |
| L-08 | N-02 | N-07 | Communication path | Kết nối cục bộ | In vé giấy có mã vạch (ASM-46) |

## F11. Cập nhật hồ sơ dự án

Thay hai dòng NEN_TANG, CONG_NGHE trong bảng ở project-profile.md mục 3 bằng khối sau, trước khi chạy P10:

```text
| NEN_TANG | Ứng dụng web dựng phía máy chủ (website đặt vé và phần mềm nhân viên nhà xe chạy trên trình duyệt) và ứng dụng Android gốc cho máy soát vé cầm tay |
| CONG_NGHE | Máy chủ: Java 17, Spring Boot; giao diện web: Thymeleaf; máy soát vé: Kotlin, Android, SQLite; hệ quản trị CSDL: PostgreSQL |
```

Trạng thái: Khuyến nghị - chờ người dùng xác nhận.

Q-nn mà giá trị trên phụ thuộc: Q-38, Q-62, Q-63, Q-64, Q-65. Chấp nhận khối này là chấp nhận phương án đã dùng cho các Q đó.

Nhắc: cập nhật hồ sơ trước khi chạy P10. Chấp nhận khuyến nghị thì không cần chạy lại P09; muốn chọn phương án khác thì điền PHUONG_AN_DA_CHON (ví dụ "CN2") rồi chạy lại P09.

## F12. Mục kiểm soát

Các mục Câu hỏi mở, Giả định, Đề xuất sửa artifact trước và Vấn đề còn mở theo C5 nằm ngay dưới đây.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-62 | Phần mềm cho nhân viên nhà xe (nhân viên bán vé, nhân viên điều hành, quản lý nhà xe) dùng trên trình duyệt web hay là ứng dụng cài đặt trên máy tính? (Trình duyệt web, dùng chung máy chủ với website / Ứng dụng cài đặt trên máy tính) | F2.2, F3, F11; PKG-06, PKG-07, PKG-08; F10 | Đoạn mở đầu, câu 4: "Nhà xe cần phần mềm bán vé và quản lý chuyến."; project-profile.md: NEN_TANG "Chưa chốt" |
| Q-63 | Máy in vé nhiệt tại quầy được nối với máy tính của nhân viên bán vé hay nối mạng độc lập với máy chủ? (Nối với máy tính quầy, in từ máy tính đó / Nối mạng độc lập, máy chủ gửi lệnh in trực tiếp) | PKG-23, F7, F10; ACT-08 | project-profile.md: HE_THONG_NGOAI "Máy in vé nhiệt tại quầy"; NFR-13 "gửi dữ liệu vé tới máy in vé nhiệt" |
| Q-64 | Hệ thống đặt ở máy chủ tập trung cho cả ba bến xe, hay mỗi bến xe có máy chủ riêng? (Một máy chủ ứng dụng và một máy chủ cơ sở dữ liệu tập trung, nhân viên các bến truy cập qua Internet / Máy chủ riêng tại từng bến xe) | F10, F7, NFR-04 (kho dữ liệu duy nhất), NFR-08 | Đoạn mở đầu: "12 tuyến xe khách liên tỉnh xuất phát từ 3 bến xe"; Mục 10, câu 1 và câu 2 |
| Q-65 | Máy soát vé nhận danh sách hành khách của chuyến bằng cách nào: tự lấy từ máy chủ khi có kết nối, hay máy chủ chủ động đẩy tới máy? (Máy tự lấy khi có kết nối từ mốc 15 phút trước giờ xuất bến / Máy chủ đẩy thông báo tới máy) | PKG-09, PKG-26, PKG-18, F7; NFR-14; liên quan Q-54 | Mục 8, câu 4: "15 phút trước giờ xuất bến, hệ thống gửi danh sách hành khách của chuyến về máy soát vé" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-45 | Phần mềm cho nhân viên nhà xe chạy trên trình duyệt web, cùng máy chủ ứng dụng với website đặt vé; mỗi vai trò nhân viên có khu vực giao diện riêng. | Chờ Q-62. Nguồn chỉ nêu "phần mềm bán vé và quản lý chuyến", không nêu hình thức; chọn trình duyệt để không phải cài đặt và cập nhật phần mềm trên máy các bến | F2.2, F3, F11; PKG-06, PKG-07, PKG-08 |
| ASM-46 | Máy in vé nhiệt nối với máy tính của nhân viên bán vé; máy chủ tạo dữ liệu vé in có mã vạch, trình duyệt trên máy tính quầy gửi lệnh in. | Chờ Q-63. Nguồn nêu in vé giấy có mã vạch nhưng không nêu cách nối máy in; chọn cách cần ít hạ tầng nhất | PKG-23, F7, F10; ACT-08 |
| ASM-47 | Hệ thống đặt ở một máy chủ ứng dụng (có thể nhân bản không giữ trạng thái) và một máy chủ cơ sở dữ liệu tập trung; nhân viên ở ba bến xe và máy soát vé truy cập qua Internet có mã hoá. | Chờ Q-64. Nguồn không nêu nơi đặt hệ thống; chọn kho dữ liệu duy nhất để NFR-04 (không hai vé cùng một chỗ giữa ba bến) đúng mà không cần đồng bộ | F10, F7, F3 |
| ASM-48 | Máy soát vé tự lấy danh sách hành khách của chuyến từ máy chủ mỗi khi có kết nối, danh sách chỉ được cấp từ mốc 15 phút trước giờ xuất bến; máy chủ không chủ động đẩy tới máy. | Chờ Q-65. Nguồn nêu "hệ thống gửi" nhưng máy ở vùng mất sóng không nhận được kết nối từ máy chủ; chọn máy chủ động lấy để không phụ thuộc kênh đẩy của bên thứ ba | PKG-09, PKG-26, PKG-18, F7; NFR-14 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Không có mục Target nào ở trạng thái Không đạt. Target 9 (khớp bảng và file .drawio, đạt C7.3) đã kiểm bằng chương trình (XML hợp lệ, toạ độ bội số của 10, khoảng cách tối thiểu giữa hai node là 40, cạnh không cắt qua node); chưa mở bằng draw.io để xem bằng mắt.
- Phương án công nghệ CN1 là khuyến nghị, chưa được người dùng xác nhận (F2.2, F11); NEN_TANG, CONG_NGHE trong project-profile.md vẫn là "Chưa chốt" cho tới khi người dùng dán khối F11.
- Mô hình phân tích mới phủ 2 trong 27 use case (F8): package của bảy nhóm chức năng còn lại, PKG-06, PKG-08, PKG-09, PKG-10, PKG-12, PKG-14 đến PKG-19, PKG-23 đến PKG-26, PKG-30, chỉ có trách nhiệm ở mức nhóm; chạy lại P09 khi P07, P08 phủ thêm use case làm đổi nhóm lớp (đặc biệt Boarding và Account) hoặc khi NFR đổi.
- Lựa chọn khi hai quy tắc xung đột: A4 muốn mỗi package trách nhiệm một câu, nhưng PKG-18 Boarding chạy ở hai node với phụ thuộc khác nhau theo node; giữ một package theo nhóm chức năng Soát vé (cohesion theo nghiệp vụ) và ghi quy tắc "mỗi node chỉ dùng phụ thuộc có mặt trên node" ở F9a. Có thể P10 tách thành hai package nếu thấy cần.
- Lựa chọn khi hai quy tắc xung đột: F5 yêu cầu dòng riêng cho boundary kênh thông báo và boundary giao diện hệ thống, trong khi P08 xếp AC-B-SmsGateway ở cả hai; ánh xạ cùng vào PKG-22 và ghi chú ở cả hai dòng.
- Chu kỳ quét mốc 30 giây (F1 dòng 9) là tham số kỹ thuật chọn theo C1 mục 7; giá trị cuối chọn ở P12.
