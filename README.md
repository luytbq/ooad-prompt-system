# Bộ prompt phân tích và thiết kế phần mềm hướng đối tượng (UML)

Bộ prompt dẫn AI đi qua toàn bộ quá trình phân tích và thiết kế một phần mềm, từ mô tả yêu cầu thô tới use case, lớp phân tích, kiến trúc, giao diện, lớp thiết kế, mô hình dữ liệu, review thiết kế và thiết kế unit test. Mỗi bước sinh ra artifact có cấu trúc cố định, có mã định danh và truy vết, để bước sau dùng làm đầu vào.

Bộ prompt không gắn với một bài toán nào. Phần phụ thuộc bài toán nằm ở hồ sơ dự án (điền một lần) và ở các placeholder có hướng dẫn cách điền ngay trong prompt.

## 1. Pipeline

```text
Tài liệu yêu cầu
   |
P00 Chuẩn hoá yêu cầu ---------------------------------------------+
   |                                                               |
P01 Xác định tác nhân                                              |
   |                                                               |
P02 Xác định use case  <---- P02R Review use case (dùng độc lập được)
   |                                                               |
P03 Biểu đồ use case                                               |
   |                                                               |
P04 Đặc tả use case + activity diagram  (lặp cho từng UC)          |
   |                                                               |
P05 Glossary                                                       |
   |                                                               |
P06 Supplementary specification (NFR, BR)  <-----------------------+
   |
P07 Phân tích use case: lớp BCE, sequence, communication  (lặp cho từng UC)
   |
P08 Hợp nhất mô hình phân tích
   |
P09 Thiết kế kiến trúc (chốt công nghệ, cập nhật project-profile.md khi hồ sơ ghi "Chưa chốt")
   |
P10 Xác định phần tử thiết kế (lớp, package, subsystem)
   |
   +--> P11a Thiết kế giao diện người dùng
   +--> P11b Thiết kế giao diện hệ thống / thiết bị
   |
P12 Thiết kế lớp (operation, quan hệ, state machine, thuộc tính)
   |
P13 Mô hình hoá dữ liệu
   |
X1 Review thiết kế (coupling, cohesion, nguyên lý)   X2 Thiết kế unit test
```

## 2. Danh sách file

| File | Nội dung |
|---|---|
| 00-Conventions.md | Luật chung: nguyên tắc, mã định danh, thư mục đầu ra, placeholder, quy ước sơ đồ draw.io. Đính kèm ở mọi bước |
| 00-ProjectProfile-Template.md | Mẫu hồ sơ dự án, điền một lần cho mỗi dự án |
| P00 đến P13, P02R, X1, X2 | Prompt của từng bước |

Bảng đầu vào, đầu ra của từng bước nằm ở mục 2 của mỗi file prompt. Bảng tổng hợp ở mục 5 dưới đây.

Thư mục _research/ không thuộc bộ prompt, chỉ là ghi chép của người xây dựng:

| Thư mục / file | Nội dung |
|---|---|
| _research/authoring-guide.md | Quy tắc viết và sửa prompt trong bộ này |
| _research/handoff-contracts.md | Bảng lõi giao tiếp giữa các bước |
| _research/A-, B-, C-, D-*-notes.md | Ghi chép nghiên cứu theo nhóm bước, nguồn của từng quy tắc |
| _research/slides-text/ | Tài liệu tham khảo dạng text dùng khi nghiên cứu |
| _research/validation/ | Các lần chạy thử pipeline (đề bài, artifact, sơ đồ, nhật ký lỗi đã sửa) |

Khi chia sẻ bộ prompt, chỉ cần các file ở gốc repo.

## 3. Bắt đầu nhanh

1. Tạo thư mục dự án, sao chép 00-ProjectProfile-Template.md vào đó, đổi tên thành project-profile.md và điền.
2. Mở P00-problem-brief.md, sao chép khối prompt ở mục 4, điền placeholder (nếu có), gửi cho AI kèm 00-Conventions.md, project-profile.md và tài liệu yêu cầu.
3. Đọc artifact AI trả về. Trả lời các câu hỏi mở (Q-nn) bằng cách bổ sung vào tài liệu nguồn hoặc vào placeholder YEU_CAU_BO_SUNG, rồi chạy lại bước đó nếu câu trả lời làm thay đổi kết quả.
4. Lần lượt chạy các bước tiếp theo. Mỗi bước đính kèm 00-Conventions.md, project-profile.md và các artifact đầu vào ghi ở mục 2 của prompt. Chạy P05 rồi P06, sau đó mới chạy P07. P06 đọc P05 để dùng đúng thuật ngữ và để cấp tiếp mã Q, ASM. Không chạy song song hai bước cùng cấp mã Q, ASM hoặc cùng ghi một file (P04-uc-specs/_BR-register.md), xem 00-Conventions.md mục C3. P07, P08 vẫn chạy được khi chưa có P05, P06, với hệ quả ghi ở mục 3 của hai prompt đó.
5. Review danh sách use case (tuỳ chọn, nên làm): chạy P02R --> chọn các UCR cần áp dụng. Có ít nhất một UCR được áp dụng: chạy lại P02 kèm P02R-review.md, ghi mã UCR trong YEU_CAU_BO_SUNG (UCR không áp dụng ghi lý do vào Vấn đề còn mở của P02) --> chạy P03 từ P02 đã sửa. Không áp dụng UCR nào: không chạy lại P02, chạy P03 với YEU_CAU_BO_SUNG ghi "Đã review P02R <phiên bản>, không áp dụng UCR-xx (lý do)" kèm các Q-nn mới của P02R.
6. Chốt công nghệ sau P09 (khi hồ sơ ghi NEN_TANG hoặc CONG_NGHE là "Chưa chốt"): đọc bảng so sánh phương án công nghệ ở P09 mục F2.2. Chấp nhận khuyến nghị, hoặc chạy lại P09 với placeholder PHUONG_AN_DA_CHON. Sau đó thay hai dòng NEN_TANG, CONG_NGHE trong bảng ở project-profile.md mục 3 bằng hai dòng của khối "Cập nhật hồ sơ dự án" (P09 mục F11) rồi mới chạy P10, vì P10 trở đi đọc NEN_TANG, CONG_NGHE từ hồ sơ. Chấp nhận khuyến nghị thì không cần chạy lại P09; P10 coi giá trị trong hồ sơ là đã chốt và không xét trạng thái "chờ xác nhận" ở P09.
7. X1 và X2 cùng cấp Q, ASM. Chạy tuần tự (X1 trước, X2 đọc mục Câu hỏi mở, Giả định của X1), hoặc khi chạy song song thì ghi trong YEU_CAU_BO_SUNG của mỗi bước một dải mã riêng, ví dụ X2 từ Q-<lớn nhất + 1>, X1 từ Q-<lớn nhất + 41>. Cùng cách này áp dụng cho mọi cặp bước chạy song song (P11a và P11b, các lần lặp P04, P07, P11a giai đoạn 2).

## 4. Ba cách chạy

| Cách | Phù hợp | Lưu ý |
|---|---|---|
| Chat thường (một cuộc trò chuyện mỗi bước hoặc vài bước) | Dự án nhỏ, dưới khoảng 10 use case | Tự đính kèm file đầu vào và tự lưu kết quả thành file đúng tên ở Conventions mục C4 |
| Project có kho tài liệu (Claude Projects, ChatGPT Projects...) | Dự án vừa | Đưa Conventions, profile và các artifact đã chốt vào kho tài liệu; mỗi bước chỉ dán prompt |
| Agent có quyền đọc ghi file (Claude Code, Cursor, Copilot agent...) | Dự án lớn, muốn tự động | Đặt bộ prompt và thư mục đầu ra trong cùng workspace; yêu cầu agent "chạy prompt Pxx", agent tự đọc đầu vào và ghi đầu ra. Sơ đồ .drawio được ghi thẳng ra file |

## 5. Bảng phụ thuộc và chạy lại

Khi sửa một artifact, các bước phụ thuộc vào nó cần chạy lại hoặc rà lại.

| Sửa artifact của bước | Rà lại các bước |
|---|---|
| P00 | Tất cả |
| P01, P02 | P03, P04 của UC liên quan, P05, P06, P07 trở đi |
| P02R (review) | P02 chạy lại kèm P02R-review.md khi có UCR được áp dụng, rồi các bước phụ thuộc P02; không có UCR nào được áp dụng thì không chạy lại |
| P03 | P04 và P07 của UC có quan hệ thay đổi, P09, P10 |
| P04 (một UC) | P05, P06, P07 của UC đó, P08 trở đi |
| P05, P06 | P07 của UC dùng thuật ngữ, BR, NFR đã đổi, P08 trở đi (P09 khi NFR đổi). P06 cấp BR mới thì rà lại Ghi chú của P05 (dẫn "REQ-nn (chưa có BR)") |
| P07 (một UC) | P08 trở đi |
| P08, P09, P10 | P11a, P11b, P12, P13 |
| P11a, P11b | P12 |
| P12 | P13, X1, X2 |
| P13 | X1, X2 |
| X1, X2 (phát hiện cần sửa) | Chạy lại bước ở cột "Bước cần sửa" (X1 mục F7) hoặc ở mục "Đề xuất sửa artifact trước" (X2), rồi các bước phụ thuộc theo bảng này |

## 6. Cấu trúc một file prompt

1. Mục đích.
2. Đầu vào và đầu ra.
3. Cách chạy: đính kèm gì, chạy một lần hay lặp, placeholder cần điền.
4. Prompt: một khối duy nhất để sao chép, theo khung CRAFT (Context, Role, Action, Format, Target) và khối Yêu cầu bổ sung. Phần Format đặc tả chi tiết từng thành phần đầu ra: định nghĩa, quy tắc, mức hợp lý, lỗi thường gặp, ví dụ đúng và sai.
5. Ghi chú cho người dùng.
6. Căn cứ: tài liệu, tiêu chuẩn đã dùng để xây dựng quy tắc.

## 7. Tuỳ biến cho dự án của bạn

- Quy định dùng chung cho mọi bước (phạm vi, mẫu tài liệu của tổ chức, quy ước đặt mã khác): ghi vào mục "Ràng buộc đặc thù" của project-profile.md.
- Quy định cho riêng một bước: ghi vào placeholder YEU_CAU_BO_SUNG ở cuối prompt của bước đó.
- Thứ tự ưu tiên khi quy tắc xung đột: xem 00-Conventions.md mục C9.
- Muốn đổi quy tắc mặc định lâu dài: sửa trực tiếp phần Format của prompt, và sửa bảng lõi ở mục tương ứng nếu bước sau đọc bảng đó.

## 8. Giới hạn

- AI có thể sai. Mỗi artifact cần được người có chuyên môn đọc lại, đặc biệt P02 (danh sách use case) vì mọi bước sau phụ thuộc vào nó. Có thể chạy P02R để AI tự review trước. P02R xếp phát hiện theo 3 mức (Nghiêm trọng / Trung bình / Thấp); X1 dùng 4 mức (Nghiêm trọng / Cao / Trung bình / Thấp).
- File .drawio do AI sinh thường đúng ngữ nghĩa nhưng bố cục chưa đẹp. Mở bằng draw.io để chỉnh vị trí; nếu sửa nội dung thì sửa bảng mô hình trong artifact .md trước (Conventions mục C7.1).
- Dự án nhiều use case sinh nhiều artifact. Khi chạy bằng chat, chỉ đính kèm đúng đầu vào mà bước yêu cầu để không vượt giới hạn ngữ cảnh. Nhiều bước chỉ cần một phần của artifact trước (ví dụ P05, P06 chỉ cần Mục 4 và Mục 5 của P02), xem mục 3 của từng prompt. P04 chạy lặp cho từng use case nên dễ vượt giới hạn nhất: mỗi lần chỉ cần các dòng liên quan tới UC_ID (dòng UC trong P02 Mục 4, các dòng REQ của UC đó trong P00 và Q-nn liên quan, bảng tác nhân của P01, các dòng có UC_ID trong P03 Mục 1 và Mục 2); khi chạy bằng chat, dán các trích đoạn này thay cho cả file (bảng ở P04 mục 3).
