# Nhật ký người chạy - P04 UC-002 Đặt vé trực tuyến

Model: mặc định của phiên điều phối (Claude Opus 5.5, claude-opus-5-5).

Đầu ra: design/P04-uc-specs/UC-002-book-ticket-online.md, design/P04-uc-specs/_BR-register.md, design/diagrams/P04-activity-UC-002.drawio (XML hợp lệ, kiểm bằng xml.dom.minidom).

Số lượng: 13 bước luồng chính; 9 luồng thay thế (2a, 4a, 6a, 6b, 7a, 7b, 9a gồm 9a1-9a2, 10a); 21 REQ truy vết; 10 BR mới (BR-01 đến BR-10); 4 Q mới (Q-31 đến Q-34); 6 ASM mới (ASM-12 đến ASM-17); 1 đề xuất sửa P02; activity diagram 2 partition, 36 node (không kể partition), 42 cạnh.

## Vướng mắc

### 1. Chờ có hạn giờ khi sự kiện được chờ là kết quả của use case được include

- Vị trí: F4.2 mục 15 "luồng chính viết hai bước liền nhau: bước hệ thống bắt đầu chờ, nêu thời hạn bằng mã BR, rồi bước sự kiện tới do chủ thể của sự kiện thực hiện"; F10.2 "decision D-N ngay sau action A-N (bước bắt đầu chờ) ... với hai guard: [<sự kiện> trong <thời hạn>] đi tới action của bước sự kiện tới".
- Gặp gì: ở UC-002, sự kiện được chờ là thanh toán thành công, do UC-003 (include) thực hiện. Bước "sự kiện tới" vì vậy là bước gọi include, chủ thể là Hệ thống, không phải "chủ thể của sự kiện". Trên sơ đồ, D-9 đặt trước A-10 nên guard [thanh toán trong 10 phút] được đánh giá trước khi thanh toán diễn ra. Luồng 10a (thanh toán thất bại, thanh toán lại) quay về M-10, không đi qua D-9, nên sơ đồ không thể hiện việc hết hạn trong vòng thanh toán lại. Prompt không có ví dụ nào cho tổ hợp "chờ có hạn giờ + include".
- Xử lý: theo đúng chữ của F4.2 mục 15 và F10.2 (bước 9 bắt đầu chờ, bước 10 gọi UC-003, D-9 có hai guard). Ghi giới hạn ngữ nghĩa vào Vấn đề còn mở và Thông tin bổ sung (thời hạn tiếp tục chạy trong khi UC-003 thực hiện).

### 2. Quy tắc "hai bước liền nhau" ép thứ tự bước, tạo khe giữa kiểm tra chỗ trống và giữ chỗ

- Vị trí: F4.2 mục 15 (như trên).
- Gặp gì: nguồn nói "Các chỗ đã chọn được giữ trong 10 phút" (Mục 3, câu 1), tự nhiên là giữ ngay sau khi chọn chỗ. Nhưng nếu giữ chỗ ngay sau bước 6 thì các bước nhập, kiểm tra thông tin người đi và tính tiền nằm giữa bước bắt đầu chờ và bước sự kiện tới, trái quy tắc "hai bước liền nhau". Đặt bước giữ chỗ ngay trước bước thanh toán thì có khe giữa kiểm tra chỗ còn trống (bước 6) và giữ chỗ (bước 9), về lý thuyết chỗ có thể bị người khác lấy trong khe này mà luồng không có nhánh cho trường hợp đó.
- Xử lý: gộp chọn chỗ và nhập thông tin người đi vào một bước tác nhân (bước 5), xếp kiểm tra và tính tiền trước bước giữ chỗ. Không thêm luồng cho khe (chi tiết tính nguyên tử thuộc thiết kế). Prompt nên nói rõ khi nào được tách bước bắt đầu chờ khỏi bước sự kiện tới.

### 3. Trục rẽ nhánh "cách decision 30 về bên phải" cắt qua action luồng chính

- Vị trí: F10.6 "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action"; cùng mục "action đầu của các nhánh xếp thành một cột bên phải, cách nhau 100 theo chiều dọc"; "khoảng cách dọc giữa hai node liên tiếp 40-60".
- Gặp gì: decision 40 rộng và action 180 rộng cùng trục dọc, nên trục cách decision 30 nằm ở tâm + 50, trong bề ngang action (tâm +/- 90). Nhánh thứ hai cách 100 theo chiều dọc luôn thấp hơn đỉnh action luồng chính kế tiếp (đỉnh ở tâm decision + 60 khi khoảng cách 40), nên đoạn dọc của trục cắt qua action đó (A-7 sau D-6, A-8 sau D-7). Ngoài ra, nhánh cách 100 cộng với khoảng cách tối thiểu 40 (C7.3) giữa nhánh cuối của decision trước và nhánh đầu của decision sau buộc phải nới khoảng cách luồng chính.
- Xử lý: đặt trục ở x = 600 (cách mép phải action luồng chính 30), ghi lựa chọn C9 vào Vấn đề còn mở. Nới A-7 xuống để D-6 --> A-7 cách 60 và A-6b --> A-7a cách 40.

### 4. Câu hỏi Q-10 ở chế độ CO_NHAN: giả định sẽ thêm tác nhân mà P02 chưa gán

- Vị trí: bước 4 của [Action] "Trường hợp chỉ có trong hiểu biết chung thì ghi thành Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)"; Conventions C1.3 "không đổi tên, không đổi mã, không bỏ phần tử đã chốt".
- Gặp gì: Q-10 (cổng báo thành công sau khi đã trả chỗ) là ngoại lệ có căn cứ của UC-002. Cả hai phương án của Q-10 đều có nhánh hoàn tiền qua ACT-06 Cổng thanh toán, trong khi P02 chỉ gán ACT-07 làm tác nhân phụ của UC-002. Prompt không nói khi một giả định hợp lý kéo theo thay đổi tác nhân của bước trước thì làm gì (đặt ASM và ghi đề xuất sửa P02, hay để mở).
- Xử lý: không đặt ASM, không thêm luồng; ghi vào Vấn đề còn mở và Thông tin bổ sung. Hậu điều kiện tối thiểu vì vậy chưa bao trường hợp tiền đã bị trừ.

### 5. F5.3 bắt buộc tạo Q-nn cho thứ tự ưu tiên khi nguồn không nêu

- Vị trí: F5.3 "Nguồn không nêu thứ tự ưu tiên thì theo thứ tự xuất hiện trong nguồn và ghi Q-nn."
- Gặp gì: bước 6 (quá 5 chỗ / chỗ không còn trống) và bước 7 (thiếu thông tin / sai định dạng) đều có hai điều kiện có thể cùng đúng. Quy tắc buộc tạo Q-34 cho một chi tiết giá trị thấp (thứ tự báo lỗi). Ở CO_NHAN cũng không rõ nên ghi Q hay ASM, vì quy tắc chỉ nói "ghi Q-nn" cho cả hai chế độ.
- Xử lý: tạo một Q-34 gộp cả hai bước, không tạo ASM (thứ tự mặc định đã do chính F5.3 quy định).

### 6. ASM ở CO_NHAN có cần đi kèm Q không

- Vị trí: Conventions C1.2 (CO_NHAN: "mỗi giả định phải có mã ASM-nn, ghi rõ nội dung, lý do"); bước 4 của [Action].
- Gặp gì: C1.2 không yêu cầu Q đi kèm ASM, nhưng các artifact P00-P02 của dự án đều ghi "Chờ Q-nn" trong cột Lý do. Không rõ đây là quy ước bắt buộc hay thói quen.
- Xử lý: theo tiền lệ dự án, ASM-14, ASM-15, ASM-17 có Q mới đi kèm (Q-31, Q-32, Q-33); ASM-12, ASM-13 trỏ Q có sẵn (Q-19, Q-08); ASM-16 (không có chuyến khớp) không tạo Q vì câu hỏi không có nội dung đáng hỏi.

### 7. REQ phi chức năng toàn hệ thống: Action bước 1c đòi đưa vào truy vết, F8 cấm ghi

- Vị trí: Action bước 1c "cùng các REQ loại Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng, Giao tiếp ngoài liên quan tới cùng đối tượng nghiệp vụ. Ghi các REQ này vào danh sách truy vết"; F8 "yêu cầu áp dụng cho toàn hệ thống không ghi ở đây"; F9 "Không dùng mục này để chứa yêu cầu chưa có REQ".
- Gặp gì: REQ-66 (2.000 người truy cập cùng lúc, Q-22 nhắc riêng tìm chuyến và đặt vé) liên quan trực tiếp tới UC-002 nhưng là yêu cầu toàn hệ thống. Nếu đưa vào hàng REQ thì REQ đó không gắn với phần tử nào trong đặc tả.
- Xử lý: không đưa REQ-66 vào hàng REQ, chỉ ghi một dòng ở Thông tin bổ sung chỉ sang P06.

### 8. "Cùng đối tượng nghiệp vụ" không được định nghĩa; hàng REQ lệch với P02

- Vị trí: mục 3, bảng phần cần dùng của P00 "các dòng REQ loại Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng, Giao tiếp ngoài về cùng đối tượng nghiệp vụ"; F1 hàng REQ "danh sách REQ truy vết".
- Gặp gì: bước 8 cần giá vé để có số tiền thanh toán; REQ-52, REQ-53 (giá theo tuyến, loại xe; tăng giá lễ Tết) không có trong cột REQ của UC-002 ở P02. Phải tự phán đoán "giá vé" có là cùng đối tượng với "vé đặt trực tuyến" không. Prompt cũng không nói hàng REQ của F1 phải bằng đúng cột REQ của P02 hay được mở rộng.
- Xử lý: mở rộng hàng REQ (thêm REQ-01, REQ-14, REQ-42, REQ-52, REQ-53), loại REQ-54 (giới hạn 30% thuộc việc đặt mức tăng, UC-017). Ghi đề xuất sửa P02 cho REQ-52, REQ-53.

### 9. Phần cần dùng của P03 mâu thuẫn với việc tìm mã Q, ASM lớn nhất

- Vị trí: mục 2 "P03-usecase-model.md ... chỉ cần Mục 1 và Mục 2"; mục 3 "không cần bảng Node, Edge"; Action bước 1e "Tìm mã Q và ASM lớn nhất trong P00 đến P03".
- Gặp gì: để tìm mã lớn nhất phải đọc cả mục Câu hỏi mở và Giả định của P01, P02, P03, không chỉ Mục 1, Mục 2 của P03. Ở chế độ chat với trích đoạn, người dùng dễ bỏ sót các mục này và cấp trùng mã.
- Xử lý: đọc thêm mục Câu hỏi mở, Giả định của P03 (đều "Không có"). Mã lớn nhất: Q-30, ASM-11 (P02).

### 10. Sổ BR có theo khung C5 không

- Vị trí: Conventions C5 "Mỗi artifact là file Markdown, mở đầu bằng khối thông tin và kết thúc bằng các mục kiểm soát"; F7.4 mục 5 mẫu sổ chỉ gồm tiêu đề và một bảng.
- Gặp gì: hai chỗ cho hai khung khác nhau cho cùng một file.
- Xử lý: theo F7.4 (quy tắc riêng của bước ưu tiên hơn C5 theo C9), sổ chỉ có tiêu đề và bảng.

### 11. Phần tìm chuyến trùng UC-001

- Vị trí: F4.3, F4.6 (luồng con, đề xuất include khi dùng chung); P03 Vấn đề còn mở (không include UC-002 --> UC-001).
- Gặp gì: P02 ghi tìm chuyến là đoạn mở đầu của UC-002, P03 quyết định không include. Prompt P04 không nói nên chép bốn bước tìm chuyến vào UC-002 hay coi là tiền điều kiện ("hành khách đã chọn một chuyến").
- Xử lý: chép bốn bước vào luồng chính (REQ-05, REQ-06 nằm trong cột REQ của UC-002), ghi ở Thông tin bổ sung rằng UC-001 cần dùng cùng dữ liệu và BR-03. Không đề xuất include vì F4.6 nói đoạn dùng chung giữa nhiều use case là ứng viên include nhưng P03 đã cân nhắc và bác.

### 12. Quy ước toạ độ trong bảng Node

- Vị trí: F10.5 bảng Node không có cột x, y, w, h; Conventions C7.1 "Khuyến nghị thêm bốn cột x, y, w, h"; F10.6 "toạ độ tương đối trong partition" cho node, nhưng "toạ độ tuyệt đối" cho điểm uốn.
- Gặp gì: hai hệ toạ độ trong cùng một bảng mô hình, prompt không nói ghi hệ nào vào cột x, y.
- Xử lý: thêm cột x, y, w, h với toạ độ tương đối trong partition, ghi chú rõ ngay trên bảng; điểm uốn dùng toạ độ tuyệt đối.

### 13. Vị trí nhãn guard x="0.7"

- Vị trí: F10.6 "nhãn guard đặt ở đoạn cuối của cạnh (mxGeometry x="0.7")" nằm trong câu về "nhiều luồng thay thế cùng một decision".
- Gặp gì: không rõ áp dụng cho mọi cạnh ra từ decision hay chỉ decision có từ hai nhánh thay thế.
- Xử lý: áp dụng cho mọi cạnh có guard để nhất quán.

### 14. Quá tải ngữ cảnh

- Vị trí: mục 3 "Khi chạy bằng agent có quyền đọc file, đính kèm đủ file; agent tự lấy phần cần dùng."
- Gặp gì: prompt P04 khoảng 68 KB, Conventions 21 KB, P00 48 KB, P02 54 KB. Đọc trọn P00, P02 không cần thiết; đã phải đọc chọn lọc theo tiêu đề mục. Prompt không nhắc agent đọc chọn lọc.
- Xử lý: đọc theo mục (P02 Mục 2, Bảng 4a, 4b, mục kiểm soát; P00 Mục 4, 5, Câu hỏi mở, Giả định; P03 Mục 1, 2 và mục kiểm soát).

## Target

Mọi mục Target 1-16 đạt theo chữ. Hai điểm đạt có giới hạn ngữ nghĩa, đã ghi ở Vấn đề còn mở của đặc tả:

- Target 8 và 13: hết thời hạn chờ gắn vào bước 9 và có nhánh từ D-9 đúng quy tắc, nhưng sơ đồ không thể hiện hết hạn trong vòng thanh toán lại 10a (vướng mắc 1).
- Target 4 và 7: hậu điều kiện tối thiểu và các kết cục của include đã có, nhưng trường hợp thanh toán thành công muộn sau khi trả chỗ (Q-10) chưa có luồng (vướng mắc 4).
