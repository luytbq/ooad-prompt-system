# Hồ sơ dự án (project-profile.md)

Sao chép file này vào thư mục đầu ra của dự án, đổi tên thành project-profile.md và điền một lần. Mọi prompt trong pipeline đều đọc file này, nên thông tin ở đây không cần điền lại trong từng prompt.

Cách điền: thay toàn bộ khối {{PH:...}} bằng nội dung thật. Dòng có [TUỲ CHỌN] có thể để "Không có".

---

## 1. Thông tin chung

| Trường | Giá trị |
|---|---|
| TEN_HE_THONG | {{PH:TEN_HE_THONG \| Hướng dẫn: tên ngắn gọn dùng trong mọi artifact, có thể kèm tên viết tắt \| Ví dụ: "Hệ thống đặt lịch khám ClinicBook"; "Hệ thống quản lý kho WMS-Lite"}} |
| MO_TA_MOT_CAU | {{PH:MO_TA_MOT_CAU \| Hướng dẫn: một câu nêu hệ thống phục vụ ai và để làm gì, không nêu chức năng chi tiết \| Ví dụ: "Cho phép bệnh nhân đặt lịch khám trực tuyến và giúp lễ tân điều phối lịch bác sĩ."}} |
| TAI_LIEU_NGUON | {{PH:TAI_LIEU_NGUON \| Hướng dẫn: liệt kê file mô tả yêu cầu sẽ được đính kèm (đề bài, biên bản phỏng vấn, tài liệu nghiệp vụ). Tài liệu đứng trước có ưu tiên cao hơn khi mâu thuẫn \| Ví dụ: "1. yeu-cau-phong-kham.md; 2. bien-ban-hop-20-09.md"}} |
| THU_MUC_DAU_RA | {{PH:THU_MUC_DAU_RA \| Hướng dẫn: thư mục gốc chứa mọi artifact. Chỉ có tác dụng khi chạy bằng agent có quyền ghi file; chạy bằng chat thì AI trả nội dung từng file \| Ví dụ: "./design/"}} |

## 2. Chế độ làm việc

| Trường | Giá trị |
|---|---|
| CHE_DO_GIA_DINH | {{PH:CHE_DO_GIA_DINH \| Hướng dẫn: chọn một. NGHIEM_NGAT: chỉ dựa vào tài liệu nguồn, chỗ thiếu thành câu hỏi mở (hợp với đề bài cố định, hồ sơ thầu, hợp đồng). CO_NHAN: cho phép giả định khi thiếu, mỗi giả định có mã ASM và được liệt kê (hợp với dự án thật khi chưa hỏi được khách hàng) \| Ví dụ: "NGHIEM_NGAT"}} |
| NGON_NGU_DAU_RA | {{PH:NGON_NGU_DAU_RA \| Hướng dẫn: ngôn ngữ văn bản của artifact \| Ví dụ: "Tiếng Việt, giữ thuật ngữ UML tiếng Anh" (mặc định); "English"}} |
| NGON_NGU_TEN_PHAN_TU | {{PH:NGON_NGU_TEN_PHAN_TU \| Hướng dẫn: ngôn ngữ đặt tên lớp, thuộc tính, phương thức, bảng, cột \| Ví dụ: "Tiếng Anh, PascalCase cho lớp, camelCase cho thuộc tính và phương thức, snake_case cho bảng và cột" (mặc định)}} |
| HAU_TO_TEN_LOP | {{PH:HAU_TO_TEN_LOP \| Hướng dẫn: hậu tố đặt tên lớp phân tích, dùng thống nhất cho mọi use case. Để "Mặc định" nếu dùng quy ước của P07 \| Ví dụ: "Boundary người dùng: Form; boundary kênh thông báo (email, SMS, thông báo đẩy): tên kênh, ví dụ Email, SmsNotifier; boundary hệ thống ngoài: Gateway; boundary thiết bị: Device; control: Controller"; "Boundary người dùng: UI; control: Handler". Boundary kênh thông báo không dùng hậu tố của form; boundary thiết bị hoặc hệ thống ngoài có tên trùng một entity luôn thêm hậu tố Device hoặc Gateway (P07 F3.1)}} |
| MUC_CHI_TIET | {{PH:MUC_CHI_TIET \| Hướng dẫn: chọn một. DAY_DU: làm đủ mọi mục của mỗi bước. GON: bỏ các mục đánh dấu "chỉ khi DAY_DU" trong prompt, dùng khi cần bản nháp nhanh \| Ví dụ: "DAY_DU"}} |

## 3. Bối cảnh kỹ thuật [TUỲ CHỌN]

NEN_TANG, CONG_NGHE chỉ dùng từ bước P09 trở đi; để "Chưa chốt" nếu muốn AI đề xuất có so sánh phương án. HE_THONG_NGOAI được P01 (ranh giới hệ thống), P06 (giao tiếp ngoài), P09 và P11b đọc, và có giá trị như tài liệu nguồn ở mức ưu tiên thấp nhất (sau mọi file trong TAI_LIEU_NGUON). Khi hai trường này là "Chưa chốt", P09 so sánh phương án công nghệ, nêu khuyến nghị và xuất mục "Cập nhật hồ sơ dự án" gồm giá trị NEN_TANG, CONG_NGHE đã chốt. Sau P09, thay hai dòng NEN_TANG, CONG_NGHE trong bảng dưới đây bằng hai dòng của khối đó trước khi chạy P10 (chấp nhận khuyến nghị thì không cần chạy lại P09), vì P10, P11a, P12, P13, X2 đọc hai trường này để chọn mẫu giao diện, kiểu dữ liệu, hệ quản trị CSDL và khung kiểm thử.

| Trường | Giá trị |
|---|---|
| NEN_TANG | {{PH:NEN_TANG \| Hướng dẫn: [TUỲ CHỌN] loại ứng dụng và nền tảng \| Ví dụ: "Web app responsive"; "Ứng dụng desktop"; "Mobile Android + web quản trị"; "Chưa chốt"}} |
| CONG_NGHE | {{PH:CONG_NGHE \| Hướng dẫn: [TUỲ CHỌN] ngôn ngữ lập trình, framework, hệ quản trị CSDL đã chốt \| Ví dụ: "Java 17, Spring Boot, PostgreSQL"; "Chưa chốt"}} |
| HE_THONG_NGOAI | {{PH:HE_THONG_NGOAI \| Hướng dẫn: [TUỲ CHỌN] hệ thống, thiết bị có sẵn mà phần mềm phải kết nối, kèm tài liệu API nếu có \| Ví dụ: "Cổng SMS của nhà mạng (API REST, tài liệu sms-api.pdf)"; "Máy quét mã vạch USB"; "Hệ thống ERP của công ty (chưa có tài liệu API)"}} |

## 4. Ràng buộc đặc thù của dự án [TUỲ CHỌN]

Các quy định áp dụng cho mọi bước mà tài liệu nguồn không ghi: quy chuẩn của tổ chức, mẫu tài liệu bắt buộc, giới hạn phạm vi.

{{PH:RANG_BUOC_DAC_THU | Hướng dẫn: [TUỲ CHỌN] mỗi ràng buộc một dòng, ghi rõ áp dụng cho bước nào nếu không áp dụng cho tất cả | Ví dụ: "- Chỉ phân tích phân hệ bán hàng, bỏ qua phân hệ kế toán."; "- Đặc tả use case theo mẫu 7 hàng của tổ chức (P04)."; "- Tên mã use case dạng UC01 thay vì UC-001."}}
