# X1 - Nhật ký người chạy

Model: Sonnet (tham số model sonnet của công cụ Agent).

Phạm vi review: PKG-09, PKG-22, PKG-23 (P12) và P13. Đầu ra: bus/design/X1-design-review.md (21 RV, 7 Q, 4 ASM). Không có file .drawio nên không có bước kiểm XML.

## 1. Vi phạm phạm vi đọc của chính người chạy

- Vị trí: nhiệm vụ giao "Không đọc bus/findings.md, bus/runner-template.md và các file khác trong bus/logs/" và chỉ đọc artifact đầu vào của mục 2 prompt.
- Đã gặp: để kiểm tra nguồn của ASM-26 và Q-44 tôi chạy grep trên P04-uc-specs/UC-013-cancel-trip.md và P04-uc-specs/_BR-register.md (P04 không nằm trong đầu vào của X1), và chạy ls thư mục bus/logs (chỉ thấy tên file, không đọc nội dung).
- Xử lý: mọi bằng chứng trong X1 chỉ trích từ P12, P13, P09, P10, P11b, P07, P08, P06; nội dung BR trích từ P06. RV-02 ghi "Cần xác nhận" thay vì "Chắc chắn" để không dựa vào chữ của ASM-26 trong P04. Kết quả phát hiện RV-02 vẫn có thể bị ảnh hưởng bởi việc đã đọc P04 nên cần người đọc nhật ký lưu ý.

## 2. Mơ hồ, mâu thuẫn, thiếu hướng dẫn trong prompt X1

1. Mục 4 [Format] F4 và [Target] 3: "Mọi lớp trong phạm vi có dòng ở F4 với mức cohesion." Với đề này có 45 phần tử, trong đó 12 enumeration, 12 value object, 3 exception chỉ là kiểu dữ liệu. Prompt không nói có được gộp một dòng cho nhóm kiểu dữ liệu hay không. Đã xử lý: mỗi phần tử một dòng, lý do ngắn. Kết quả dài, giá trị thấp. Gợi ý: cho phép gộp bằng thẻ br như F3 đã cho với Data coupling, hoặc nói rõ enumeration, value object, exception mặc định Functional.
2. [Target] 2 và F3: "Mọi cặp phần tử có quan hệ trong phạm vi có mặt ở F3". Không nói quan hệ Realization, Dependency tới kiểu tham số (R-53 đến R-57, R-62 đến R-67), quan hệ tới java.time.Clock có phải là cặp cần liệt kê không. Đã xử lý: liệt kê cả 50 quan hệ R-02 đến R-67 (gộp Data theo phần tử A và kênh), kiểm bằng script rằng không thiếu R-nn nào.
3. F3 cột Kênh phụ thuộc chỉ có "thuộc tính / tham số / biến cục bộ / toàn cục / kế thừa / truy cập trực tiếp dữ liệu". Với common coupling qua bảng CSDL do hai repository cùng ghi (RV-05) và External coupling (định dạng chuỗi requestKey, nhãn tuyến) không có giá trị tương ứng. Đã xử lý: ghi mô tả tự do ở cột Kênh ("dữ liệu dùng chung ...") và ghi External coupling theo đoạn "Ngoài thang". Gợi ý: thêm kênh "bảng CSDL dùng chung" và "định dạng chuỗi".
4. F3 quy tắc "Mỗi cặp có mức khác Data coupling một dòng riêng". Có các cặp ở mức Data nhưng vi phạm nguyên lý khác (Law of Demeter, vòng phụ thuộc: RV-01, RV-04, RV-08). Không rõ có tách dòng riêng hay không vì cột "Chấp nhận" cần ghi "Không: RV". Đã xử lý: tách dòng riêng khi cột Chấp nhận là "Không".
5. F2 Mức độ: định nghĩa "Nghiêm trọng: thiết kế không hiện thực đúng yêu cầu hoặc BR" không nói rõ trường hợp yêu cầu chỉ có ở giả định (ASM-26) hoặc câu hỏi mở (Q-44) (RV-02), thiếu cơ chế khoá lạc quan (RV-03), rò rỉ dữ liệu cá nhân (RV-14). Không có mức cho lỗi bảo mật hoặc hiệu năng. Đã xử lý: xếp RV-02, RV-03 mức Cao, RV-14 mức Trung bình, ghi lý do trong cột Bằng chứng. Cuối X1 có ghi RV-03 và RV-05 là ứng viên nâng lên Nghiêm trọng.
6. F2 cột "Nhóm" liệt kê MOD / CPL / COH / SOLID / GRASP / PRN / PKP / SML / CNS / DAT, không có nhóm cho giao dịch, đồng thời, bảo mật, hành vi không hiện thực yêu cầu. Đã xử lý: xếp vào CNS hoặc DAT. Ngoài ra ví dụ của NHOM_TIEU_CHI trong mục 4 ghi "PKG, CNS" trong khi danh sách nhóm dùng PKP: mâu thuẫn tên nhóm (PKG hay PKP).
7. F2 "Mức hợp lý: một dòng một nguyên nhân gốc" và [Target] 7. RV-03 (khoá lạc quan), RV-04 (Seat bị điều khiển ngoài Trip), RV-05 (hai chủ ghi một bảng) cùng chạm trạng thái chỗ. Prompt không cho tiêu chí phân biệt nguyên nhân gốc với biểu hiện. Đã xử lý: tách ba dòng vì bằng chứng và hệ quả khác tầng (hành vi, ánh xạ dữ liệu, đồng thời), ghi nhận định này ở Vấn đề còn mở của X1.
8. F2 cột "Bước cần sửa" yêu cầu "mã bước pipeline cần chạy lại sớm nhất", nhưng F7 chỉ có một danh sách theo bước. Các phát hiện cần sửa nhiều bước (RV-05 sửa P11b rồi P12, P13; RV-03 sửa P12 rồi P13) không có chỗ ghi các bước sau. Đã xử lý: ghi bước sớm nhất ở cột, mô tả các bước sau trong cột Đề xuất, và thêm một dòng giải thích ở F7 mục 4.
9. F6.3: "Ca (số lớp ngoài package phụ thuộc vào lớp trong package)", "A = số lớp trừu tượng và interface / tổng số lớp". Không nói có đếm value object, enumeration, ngoại lệ, kiểu PKG-28 và kiểu nền tảng Java hay không, và xử lý lớp thuộc package chưa có P12 (PKG-08, PKG-10, PKG-11, PKG-14, PKG-24). Đã xử lý: tự định nghĩa cách đếm ở đầu F6.3, ghi ASM-150, kết quả là ước lượng (Ca của PKG-22 và PKG-23 chưa chốt).
10. Mục 4 [Format]: "Mục 'Đề xuất sửa artifact trước' ghi 'Xem bảng phát hiện F2'". C5 yêu cầu bảng bốn cột. Không rõ ghi một câu hay một dòng bảng. Đã xử lý: một dòng bảng với Bước là "Nhiều bước" và cột Đề nghị là câu bắt buộc.
11. Bước 0 "Lập danh mục phần tử trong phạm vi: package, subsystem, interface, lớp, operation, quan hệ, bảng". F1 chỉ yêu cầu "số package, lớp, bảng". Đã xử lý: ghi thêm số operation, thuộc tính, quan hệ, state machine, ER.
12. Bước 7 ví dụ mâu thuẫn nguyên lý nói "ghi lựa chọn và đánh đổi". Không nói ghi vào cột nào của F2. Đã xử lý: ghi trong cột Bằng chứng của RV-08 (Information Expert so với High Cohesion) và nhắc ở Vấn đề còn mở.
13. Mục 2 liệt kê đầu vào "P07-uc-analysis/*.md, P08-analysis-model.md" để kiểm tra truy vết message --> operation, nhưng P12 F4 đã có sẵn 109 dòng ánh xạ; prompt không nói có phải tự dựng lại bảng từ P07 hay chỉ đối chiếu. Đã xử lý: chỉ đối chiếu mẫu UC-002 SD1 (46 message) và các dòng UC-013, UC-015, không dựng lại toàn bộ.
14. Chưa có hướng dẫn cho phát hiện đã được artifact bước trước tự nêu trong "Đề xuất sửa artifact trước" (RV-10 nhãn tuyến, RV-11 kind của mốc, RV-17 InvalidStateException vốn là đề xuất P10 của P12). Đã xử lý: vẫn ghi RV, trạng thái Mở, nêu P12 đã có đề xuất.

## 3. Mâu thuẫn hoặc đầu vào không khớp

- Conventions C3: "Lần chạy nào cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất đã thấy, rồi cấp tiếp từ số đó" so với YEU_CAU_BO_SUNG "cấp mã Q mới từ Q-150 và ASM mới từ ASM-150". Mã lớn nhất tôi thấy là Q-109 (P13) và ASM-110 (P13). Đã xử lý theo C9 (yêu cầu bổ sung ưu tiên cao hơn quy tắc bước và C3 không thuộc C1); ghi lựa chọn ở Vấn đề còn mở. Khoảng trống Q-110 đến Q-149 để các lần chạy khác.
- P11b F4 (SS07-WB1-M04) nói cập nhật có điều kiện "phiên bản chuyến" và P12 F3 handleTrigger nói "theo phiên bản", còn P12 F7 và P13 F6.1 không có thuộc tính hoặc cột phiên bản: đầu vào không khớp, đã thành RV-03.
- P13 F4.2 ràng buộc "seat.status = 'SOLD' khi và chỉ khi chỗ có vé ISSUED" không khớp P12 DC-Ticket.cancelWithTrip (không đụng chỗ): RV-15.
- Conventions C1.5 / prompt nói F1 phải nêu "phiên bản" artifact: các artifact đều ghi 1.0 nên không có vướng mắc.

## 4. Quá tải ngữ cảnh

- P12 dài 1039 dòng (khoảng 186 KB), P13 66 KB, P11b 205 KB, P09 54 KB, P10 60 KB. Đã đọc P12 đầy đủ theo từng đoạn; P13 đọc F2 đến F6 (bỏ F8 ERD, F7, F9); P11b chỉ đọc qua grep các dòng IF-10, IF-11, SS-07; P09 đọc F4 đến F7; P10 đọc F3 đến F6; P07 chỉ đọc bảng message của UC-002 SD1. Có nguy cơ bỏ sót phát hiện nằm ở các phần chưa đọc (ví dụ ERD P13, SD của UC-013, UC-015, mô tả UC-008).
- Ca, Ce ở F6.3 tính tay từ chữ ký trong P12 nên có thể lệch một vài đơn vị.

## 5. Kết quả tự kiểm tra theo Target

| Target | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | 45 phần tử đều có dòng ở F4; F3 và F5 phủ thêm |
| 2 | Đạt | 50 quan hệ R-02 đến R-67 đều có mặt ở F3 (kiểm bằng script); cách hiểu "cặp" xem mục 2 điểm 2 |
| 3 | Đạt | 50 dòng F4 (45 phần tử, 3 package, 2 operation); gộp dòng chưa được prompt nói rõ (mục 2 điểm 1) |
| 4 | Đạt | Mọi RV trích nguyên văn từ P12, P13, P11b, P09, P10, P06, P07 kèm vị trí |
| 5 | Đạt | Có mức độ và tên refactoring trong từng RV |
| 6 | Đạt | F7 có thứ tự P10, P11b, P12, P13; RV có nhiều bước ghi ở cột Đề xuất |
| 7 | Đạt có điều kiện | RV-03, RV-04, RV-05 gần nhau, đã tách và ghi nhận định ở Vấn đề còn mở |
| 8 | Đạt | 7 phát hiện "Cần xác nhận" có thông tin thiếu và Q-150 đến Q-156 |
| 9 | Đạt | Mỗi đề xuất pattern hoặc lớp mới nêu vấn đề giải quyết (vòng phụ thuộc, vi phạm Demeter, định dạng chuỗi) |
| 10 | Đạt | F6.1 đủ ba package nguồn và đích; F6.2 ghi không có vòng package và một vòng cấp lớp |
| 11 | Đạt | Không sửa artifact nào đang review |
| 12 | Đạt | Kiểm bằng grep: không có em dash, không có mũi tên Unicode, không có inline code; khung C5 đủ; không còn placeholder |
