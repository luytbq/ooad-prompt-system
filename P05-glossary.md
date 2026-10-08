# P05 - Từ điển thuật ngữ (Glossary)

## 1. Mục đích

Bước này lập từ điển thuật ngữ duy nhất của hệ thống: các khái niệm nghiệp vụ đặc thù, định nghĩa ngắn gọn và không mơ hồ, từ đồng nghĩa cần tránh. Từ điển giúp chuyên gia nghiệp vụ và người phát triển hiểu cùng một nghĩa, và là nguồn đặt tên cho lớp entity, thuộc tính, bảng dữ liệu ở các bước phân tích, thiết kế sau.

Bước chạy một lần sau khi đã có đặc tả use case, và chạy lại khi thêm hoặc sửa đặc tả. Mỗi hệ thống chỉ có một từ điển thuật ngữ.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md | Có | Luật chung |
| Đầu vào | project-profile.md | Có | Tên hệ thống, ngôn ngữ, chế độ giả định |
| Đầu vào | Tài liệu nguồn trong TAI_LIEU_NGUON | Có | Cách gọi gốc của nghiệp vụ, câu định nghĩa có sẵn |
| Đầu vào | P00-problem-brief.md | Có | REQ, nhất là REQ loại Dữ liệu |
| Đầu vào | P01-actors.md, P02-usecases.md | Có | Tên tác nhân, tên và mô tả use case; với P02 chỉ cần Mục 4 (bảng use case) và Mục 5 (ma trận REQ --> UC) |
| Đầu vào | P04-uc-specs/*.md | Có | Luồng sự kiện, dữ liệu vào ra, BR: nơi thuật ngữ được dùng |
| Đầu vào | P04-uc-specs/_BR-register.md | Tuỳ chọn | Thuật ngữ xuất hiện trong quy tắc nghiệp vụ |
| Đầu vào | P05-glossary.md bản cũ | Có khi chạy lại | Giữ mã GL đã cấp |
| Đầu ra | P05-glossary.md | | Từ điển thuật ngữ; đầu vào của phân tích use case, thiết kế lớp, mô hình dữ liệu |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, tài liệu nguồn, P00, P01, P02 (chỉ cần Mục 4 và Mục 5, giảm kích thước đầu vào khi chạy bằng chat), mọi đặc tả P04 đã có, sổ BR (nếu có), bản P05 cũ (nếu chạy lại).
- Chạy một lần cho toàn hệ thống. Có thể chạy sớm sau P02 để có bản nháp, rồi chạy lại sau khi xong mọi đặc tả P04.
- Placeholder trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| NGUON_THUAT_NGU_CHUAN | Tuỳ chọn | Từ điển, tiêu chuẩn ngành mà tổ chức bắt buộc dùng |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Quy định riêng của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md, tài liệu nguồn, P00-problem-brief.md, P01-actors.md, P02-usecases.md, các đặc tả P04-uc-specs/UC-nnn-*.md, có thể có P04-uc-specs/_BR-register.md và bản P05-glossary.md cũ.

Đây là bước P05 của pipeline: lập từ điển thuật ngữ duy nhất cho toàn hệ thống. Các bước sau dùng từ điển này để đặt tên lớp entity, thuộc tính, bảng dữ liệu, và mọi artifact phải dùng đúng thuật ngữ chính thức.

Nguồn thuật ngữ chuẩn của tổ chức hoặc của ngành (nếu có):
{{PH:NGUON_THUAT_NGU_CHUAN | Hướng dẫn: [TUỲ CHỌN] tài liệu định nghĩa thuật ngữ mà dự án bắt buộc theo, được đính kèm. Khi thuật ngữ của nguồn yêu cầu khác nguồn chuẩn, AI ghi câu hỏi mở thay vì tự chọn. Không có thì thay cả khối bằng "Không có" | Ví dụ: "Danh mục thuật ngữ nghiệp vụ kho của công ty, file thuat-ngu-kho.xlsx"; "Quy tắc biên mục thư viện đang áp dụng, file quy-tac-bien-muc.pdf"}}

[Role]
Bạn là chuyên gia phân tích nghiệp vụ, có kinh nghiệm xây dựng từ điển dữ liệu và thuật ngữ, viết định nghĩa theo nguyên tắc thuật ngữ học (định nghĩa bằng khái niệm bao quát và đặc điểm phân biệt).

[Action]
Thực hiện tuần tự:

1. Nếu có bản P05 cũ: giữ nguyên mã GL và thuật ngữ chính thức; thuật ngữ không còn dùng giữ mã và ghi trạng thái "Loại" ở cột Ghi chú; thuật ngữ mới lấy mã tiếp nối.
2. Thu thập ứng viên: đọc P00, P02, các đặc tả P04 (luồng sự kiện, bảng dữ liệu, BR, tiền điều kiện, hậu điều kiện) và sổ BR. Lấy mọi danh từ, cụm danh từ chỉ đối tượng nghiệp vụ, vai trò, trạng thái, sự kiện, đại lượng, chứng từ, viết tắt. Ghi nơi xuất hiện (REQ, UC, BR).
3. Lọc theo tiêu chí chọn ở mục F2. Ứng viên bị loại ghi vào bảng "Ứng viên không đưa vào" kèm lý do.
4. Gom từ đồng nghĩa: các cách gọi khác nhau chỉ cùng một khái niệm gom thành một thuật ngữ, chọn thuật ngữ chính thức theo F4. Một từ mang hai nghĩa khác nhau trong nguồn thì tách thành hai thuật ngữ có tên phân biệt và tạo Q-nn nếu không chắc.
5. Viết định nghĩa cho từng thuật ngữ theo F3, chỉ dựa trên nguồn và các artifact đã có. Chỗ nguồn không đủ để định nghĩa thì ghi định nghĩa phần đã biết và tạo Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN).
6. Ghi thành phần dữ liệu, giá trị cho phép, trạng thái, đơn vị của thuật ngữ khi nguồn nêu (cột Ghi chú), để từ điển kiêm vai trò từ điển dữ liệu không chính thức.
7. Kiểm tra dùng nhất quán: rà P01, P02, P04 để tìm chỗ dùng từ đồng nghĩa không chính thức hoặc dùng một thuật ngữ sai nghĩa. Mỗi chỗ ghi vào "Đề xuất sửa artifact trước" (bước, mã phần tử, từ đang dùng, thuật ngữ chính thức). Không tự sửa artifact trước. Dạng rút gọn được chấp nhận của thuật ngữ chính thức (F3 cột Từ đồng nghĩa không dùng) không cần đề xuất. Nội dung BR trái với định nghĩa: ghi đề xuất cho bước ở cột "Cấp lần đầu tại" của sổ BR, không ghi cho P06 (P06 chạy sau P05). Định nghĩa vẫn bám nội dung BR hiện hành, phần khác biệt ghi kèm mã Q, ASM ở Ghi chú.
8. Sắp xếp thuật ngữ theo thứ tự chữ cái của cột Thuật ngữ, rồi cấp mã GL theo thứ tự đó ở lần chạy đầu. Các lần chạy sau thuật ngữ mới lấy mã tiếp nối, vẫn sắp theo chữ cái trong bảng.
9. Chạy checklist ở phần [Target], sửa những gì chưa đạt, ghi phần không sửa được vào mục "Vấn đề còn mở".

[Format]
Xuất một file Markdown tên P05-glossary.md theo khung C5, gồm đúng các mục sau theo thứ tự:

# P05 - Từ điển thuật ngữ - <TEN_HE_THONG>
(bảng thông tin theo C5)
## 1. Giới thiệu
## 2. Thuật ngữ
## 3. Ứng viên không đưa vào
## Câu hỏi mở
## Giả định  (chỉ khi CO_NHAN)
## Đề xuất sửa artifact trước
## Vấn đề còn mở

F1. Giới thiệu
2-4 câu: mục đích của từ điển, phạm vi (hệ thống nào), quy ước dùng (mọi artifact dùng cột Thuật ngữ làm cách gọi chính thức; từ ở cột "Từ đồng nghĩa không dùng" không được dùng trong artifact mới).

F2. Tiêu chí chọn thuật ngữ
Đưa vào khi ứng viên xuất hiện trong ít nhất một artifact (REQ, UC, BR) và thoả ít nhất một điều:
  a. Khái niệm đặc thù của nghiệp vụ, người ngoài ngành có thể không hiểu. Ví dụ: "Phiếu mượn", "Đặt giữ chỗ" (thư viện); "Lô hàng", "Phiếu xuất kho" (kho); "Khung giờ khám" (phòng khám).
  b. Từ phổ thông nhưng có nghĩa riêng, hẹp hơn hoặc khác, trong hệ thống này. Ví dụ: "Đơn hàng" trong giao đồ ăn chỉ tính từ khi thanh toán thành công; "Khách" trong khách sạn phân biệt "Khách đặt phòng" và "Khách lưu trú".
  c. Trạng thái nghiệp vụ hoặc tập giá trị có ý nghĩa quy tắc. Ví dụ: "Lịch hẹn chờ xác nhận", "Sách quá hạn".
  d. Đại lượng có công thức hoặc đơn vị riêng. Ví dụ: "Phí trả muộn", "Tồn kho khả dụng".
  e. Từ viết tắt, mã hiệu. Ví dụ: "SKU", "OTP".
  f. Có từ đồng nghĩa trong nguồn cần thống nhất cách gọi.
Không đưa vào:
  - Từ phổ thông dùng đúng nghĩa thông thường: "ngày", "tên", "địa chỉ", "số điện thoại" (trừ khi có quy định riêng về định dạng hay nghĩa).
  - Thuật ngữ kỹ thuật phần mềm và UML: "use case", "cơ sở dữ liệu", "đăng nhập", "tài khoản" (trừ khi nghiệp vụ gán nghĩa riêng).
  - Từ giao diện: "màn hình", "nút", "trang chủ".
  - Tên riêng của tổ chức, người.
  - Tên use case (đã định nghĩa ở P02). Tên tác nhân chỉ đưa vào khi là vai trò nghiệp vụ đặc thù cần định nghĩa phân biệt với vai trò gần giống; khi đó cột Nguồn dẫn thêm mã ACT.
Mức hợp lý: hệ thống 10-20 use case thường có 15-50 thuật ngữ. Dưới 10 thường là bỏ sót khái niệm đặc thù; trên 80 thường là đưa cả từ phổ thông hoặc thuộc tính lẻ.
Lỗi thường gặp: quá nhỏ (đưa từng thuộc tính lẻ như "Họ tên bạn đọc", "Ngày sinh bạn đọc" thành thuật ngữ riêng thay vì ghi trong Ghi chú của "Bạn đọc"); quá lớn (đưa cả câu hay quy trình dài làm thuật ngữ, ví dụ "Quy trình xử lý đơn hàng bị huỷ sau khi tài xế đã nhận"); nhầm với BR (thuật ngữ định nghĩa khái niệm là gì; quy tắc nói khái niệm phải thế nào).

F3. Bảng thuật ngữ (bảng lõi)
Bảng: | GL | Thuật ngữ | Tiếng Anh | Định nghĩa | Từ đồng nghĩa không dùng | Nguồn (REQ / UC) | Ghi chú |
- GL: mã GL-nn theo Conventions C3.
- Thuật ngữ: cụm danh từ, số ít, viết thường trừ chữ đầu và tên riêng, đúng cách gọi chính thức.
- Tiếng Anh: tên tiếng Anh dùng để đặt tên lớp, thuộc tính, bảng ở các bước thiết kế; danh từ số ít, không viết tắt trừ viết tắt phổ biến. Ví dụ: "Phiếu mượn" --> "Loan"; "Khung giờ khám" --> "Time Slot"; "Phiếu nhập kho" --> "Goods Receipt".
- Định nghĩa: quy tắc viết:
  1. Mở đầu bằng khái niệm bao quát (thuộc loại gì), tiếp theo là đặc điểm phân biệt với các khái niệm cùng loại. Mẫu: "<Khái niệm bao quát> <đặc điểm phân biệt>." Ví dụ: "Chứng từ ghi nhận việc một bạn đọc mượn một hoặc nhiều cuốn sách tại một thời điểm, gồm ngày mượn và ngày hết hạn trả."
  2. Không dùng chính thuật ngữ để định nghĩa (định nghĩa vòng tròn). Sai: "Phiếu mượn là phiếu dùng để mượn."
  3. Không định nghĩa bằng từ đồng nghĩa đơn thuần. Sai: "Lô hàng: một lô."
  4. Viết dạng khẳng định; chỉ dùng phủ định khi đặc điểm phân biệt chính là phủ định ("Khách vãng lai: khách hàng không có tài khoản").
  5. Nêu nghĩa trong hệ thống này, không nêu nghĩa từ điển chung chung.
  6. Không mô tả giao diện, không mô tả cách lưu trữ, không nêu quy tắc thay đổi được (quy tắc thuộc BR, dẫn mã ở Ghi chú). Sai: "Sách quá hạn: sách mượn quá 14 ngày" nếu 14 ngày là quy tắc có thể đổi; đúng: "Sách quá hạn: cuốn sách đang mượn đã qua ngày hết hạn trả của phiếu mượn (thời hạn mượn theo BR-02)". Quy tắc chưa có mã BR (REQ loại Quy tắc nghiệp vụ chưa được đặc tả P04 nào dùng) thì dẫn "REQ-nn (chưa có BR)" ở Ghi chú; P06 sẽ cấp BR và đề xuất thay mã.
  7. Độ dài: một câu chính, tối đa khoảng 40 từ; thêm câu thứ hai khi cần làm rõ phạm vi. Định nghĩa dài hơn ba câu thường chứa quy tắc hoặc quy trình, cần tách.
  8. Dùng các thuật ngữ khác trong từ điển thì dùng đúng tên chính thức của chúng.
- Từ đồng nghĩa không dùng: các cách gọi khác đã gặp trong nguồn hoặc artifact, ngăn bằng dấu phẩy; không có thì "Không có". Chỉ ghi từ thực sự xuất hiện hoặc dễ gây nhầm trong bối cảnh dự án. Dạng rút gọn của chính thuật ngữ chính thức (bỏ bổ ngữ mà nghĩa không đổi trong bối cảnh dự án, ví dụ "phiếu nhập" cho "Phiếu nhập kho" khi hệ thống không có phiếu nhập nào khác) không phải từ đồng nghĩa không dùng và không cần đề xuất sửa; ghi các dạng rút gọn được chấp nhận ở cột Ghi chú. Dạng rút gọn có thể chỉ khái niệm khác ("phiếu") thì ghi ở cột này.
- Nguồn: các REQ, UC (và ACT, BR nếu có) nơi thuật ngữ xuất hiện; tối thiểu một mã.
- Ghi chú: thành phần dữ liệu (theo REQ loại Dữ liệu), tập giá trị hoặc trạng thái, đơn vị đo, mã BR liên quan, quan hệ với thuật ngữ khác ("Một Phiếu mượn gồm một hoặc nhiều Dòng mượn"), Q-nn, trạng thái "Loại" khi chạy lại.
- Ví dụ đúng:
  | GL-04 | Khung giờ khám | Time Slot | Khoảng thời gian liên tục trong lịch làm việc của một bác sĩ, dành cho đúng một lịch hẹn. | Ca khám, suất khám | REQ-03, UC-003 | Độ dài khung giờ theo BR-05. Trạng thái: Trống, Đã đặt, Bị khoá |
  | GL-09 | Tồn kho khả dụng | Available Stock | Số lượng một mặt hàng đang có trong kho trừ đi số lượng đã được giữ cho các phiếu xuất chưa hoàn tất. | Hàng còn, số lượng tồn | REQ-12, UC-006 | Đơn vị: đơn vị tính của mặt hàng. Công thức ở BR-09 |
- Ví dụ sai:
  | GL-01 | Khách hàng | Customer | Người dùng hệ thống. | | UC-001 | | (định nghĩa quá rộng, không phân biệt với tác nhân khác; thiếu nguồn REQ)
  | GL-02 | Đơn hàng | Order | Là đơn hàng mà khách hàng đặt trên màn hình giỏ hàng bằng cách bấm nút Đặt. | | | | (vòng tròn, mô tả giao diện, thiếu nguồn)

F4. Chọn thuật ngữ chính thức khi có từ đồng nghĩa
Vai trò đã có tên tác nhân ở P01 thì tên tác nhân là thuật ngữ chính thức của vai trò đó, không xét thứ tự ưu tiên bên dưới; cách gọi khác của nguồn (kể cả cách gọi xuất hiện nhiều nhất, ví dụ "người dùng" khi hệ thống có nhiều vai trò) ghi vào cột Từ đồng nghĩa không dùng. P01 đã chọn tên theo cùng nguyên tắc (tên vai trò cụ thể, giữ cách gọi của nguồn khi nó chỉ đúng một vai trò), nên không đề xuất đổi tên tác nhân chỉ vì nguồn dùng từ khác. Với khái niệm khác, theo thứ tự ưu tiên:
  1. Thuật ngữ trong NGUON_THUAT_NGU_CHUAN nếu có.
  2. Cách gọi mà tài liệu nguồn có ưu tiên cao nhất (theo thứ tự TAI_LIEU_NGUON) dùng.
  3. Cách gọi xuất hiện nhiều nhất trong tài liệu nguồn.
  4. Cách gọi cụ thể hơn, ít nghĩa phụ hơn ("Phiếu nhập kho" tốt hơn "Phiếu").
  5. Cách gọi đã dùng trong tên use case đã chốt (tránh phải đổi artifact trước).
Tên use case đã chốt là cụm động từ, không phải thuật ngữ, nên không tính là dùng từ đồng nghĩa: nguồn gọi "phiếu xuất" và P02 đã chốt "Lập phiếu xuất kho" thì thuật ngữ chính thức vẫn chọn theo thứ tự trên, tên use case giữ nguyên. Chỉ ghi đề xuất đổi tên use case (bước 7) khi danh từ trong tên use case chỉ một khái niệm khác với thuật ngữ chính thức; cách gọi cụ thể hơn hoặc thêm bổ ngữ của cùng khái niệm không phải lý do đề xuất đổi.
Khi tách một từ đa nghĩa thành hai thuật ngữ (Action bước 4): nghĩa nào đã là danh từ trong tên use case đã chốt thì giữ cách gọi gốc; nghĩa còn lại thêm bổ ngữ phân biệt (ví dụ "Giá phòng" là bảng giá theo loại phòng trong use case "Đặt giá phòng", nghĩa giá của một lần đặt thành "Giá một lần đặt"). Chỉ áp dụng mục 1 đến 4 khi không nghĩa nào có trong tên use case.
Ghi lý do chọn ở cột Ghi chú khi hai cách gọi ngang nhau. Nếu hai cách gọi có thể là hai khái niệm khác nhau (ví dụ "Khách hàng" và "Người nhận hàng" trong giao đồ ăn), không gộp; tạo hai thuật ngữ hoặc Q-nn.

F5. Ứng viên không đưa vào
Bảng: | Ứng viên | Lý do không đưa vào | Nơi xuất hiện |
Lý do theo các mục "Không đưa vào" ở F2, hoặc "Đồng nghĩa của GL-nn". Mục đích: cho người đọc thấy việc lọc có căn cứ.

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Mọi thuật ngữ xuất hiện trong ít nhất một REQ, UC hoặc BR, và cột Nguồn có mã.
2. Mọi khái niệm đặc thù, trạng thái, đại lượng, viết tắt dùng trong đặc tả P04 đều có trong bảng thuật ngữ hoặc bảng ứng viên không đưa vào.
3. Không có từ phổ thông dùng đúng nghĩa thông thường, thuật ngữ kỹ thuật phần mềm, từ giao diện trong bảng thuật ngữ.
4. Mọi định nghĩa có khái niệm bao quát và đặc điểm phân biệt; không vòng tròn; không chứa quy tắc thay đổi được (quy tắc dẫn mã BR, hoặc "REQ-nn (chưa có BR)", ở Ghi chú); không mô tả giao diện, lưu trữ.
5. Không có hai thuật ngữ chính thức cùng nghĩa; không có một thuật ngữ mang hai nghĩa.
6. Mỗi thuật ngữ có tên tiếng Anh dạng danh từ số ít, không trùng tên tiếng Anh của thuật ngữ khác.
7. Mọi chỗ artifact trước dùng từ đồng nghĩa không chính thức (không tính dạng rút gọn được chấp nhận) đã được ghi ở "Đề xuất sửa artifact trước".
8. Không có định nghĩa, thành phần dữ liệu, giá trị nào do AI tự thêm ở chế độ NGHIEM_NGAT; chỗ thiếu có Q-nn.
9. Khi chạy lại: mã GL cũ được giữ; thuật ngữ bỏ vẫn còn dòng với trạng thái "Loại".
10. Định dạng theo Conventions C2, C5, C8; bảng sắp theo chữ cái của cột Thuật ngữ.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này, ưu tiên cao hơn quy tắc mặc định (trừ Conventions C1). Không dùng thì thay cả khối bằng "Không có" | Ví dụ: "Đưa cả tên tác nhân vào từ điển"; "Tên tiếng Anh theo thuật ngữ chuẩn của ngành khách sạn (front desk, folio...)"; "Nhóm thuật ngữ theo phân hệ: Mượn trả, Biên mục, Bạn đọc"}}
````

## 5. Ghi chú cho người dùng

- Từ điển quá dài vì chứa thuộc tính lẻ: yêu cầu AI gom thuộc tính vào cột Ghi chú của thuật ngữ cha, chạy lại.
- Mục "Đề xuất sửa artifact trước" có nhiều dòng: sửa các artifact đó theo đề xuất (hoặc chấp nhận thuật ngữ đang dùng và chạy lại P05 với YEU_CAU_BO_SUNG chỉ định thuật ngữ chính thức), để bước phân tích sau không đặt hai tên lớp cho cùng một khái niệm.
- Tên tiếng Anh trong từ điển là gợi ý mạnh cho tên lớp entity và bảng dữ liệu. Nên chốt từ đây thay vì để mỗi bước sau tự dịch.
- Dùng độc lập: bước này dùng được với bất kỳ bộ tài liệu yêu cầu nào; nếu chưa có đặc tả use case, chỉ cần tài liệu nguồn và danh sách yêu cầu, cột Nguồn khi đó ghi mã REQ hoặc vị trí câu trích.

## 6. Căn cứ

- Rational Unified Process, artifact Glossary: một từ điển duy nhất cho hệ thống, gồm phần giới thiệu và phần định nghĩa thuật ngữ, có thể dùng như từ điển dữ liệu không chính thức.
- K. Wiegers, J. Beatty, Software Requirements, 3rd ed., 2013: glossary và data dictionary, định nghĩa thành phần dữ liệu.
- C. Larman, Applying UML and Patterns, 3rd ed., 2004: glossary như từ điển dữ liệu, liên hệ với domain model.
- ISO 704:2022, Terminology work - Principles and methods: định nghĩa nội hàm bằng khái niệm bao quát và đặc điểm phân biệt, tránh định nghĩa vòng tròn.
- E. Evans, Domain-Driven Design, Addison-Wesley, 2003: ngôn ngữ chung (ubiquitous language), một khái niệm một tên.
