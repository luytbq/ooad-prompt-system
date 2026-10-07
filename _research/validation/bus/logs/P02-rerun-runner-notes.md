# Nhật ký người chạy - P02-rerun (chạy lại P02 sau review P02R)

Đầu vào: 00-Conventions.md, README.md, P02-identify-use-cases.md, project-profile.md, yeu-cau-xe-khach.md, P00-problem-brief.md 1.0, P01-actors.md 1.0, P02-usecases.md 1.0, P02R-review.md 1.0.
Placeholder: PHAM_VI_LAN_CHAY = Không có; QUY_UOC_DA_CHOT = Không có; YEU_CAU_BO_SUNG = "Áp dụng UCR-01, UCR-02, UCR-03, UCR-04 của P02R-review.md phiên bản 1.0."
Đầu ra: design/P02-usecases.md phiên bản 1.1 (18 UC, 49 CAND, 22 EV, ASM-08 đến ASM-11, Q-26 đến Q-30). Không có sơ đồ .drawio ở bước này.

## Vướng mắc

### 1. Khối prompt không có chỉ dẫn nào cho lần chạy lại sau review

- Vị trí: mục 4, [Context]: "Đọc theo thứ tự: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md, P00-problem-brief.md (bảng REQ, phạm vi), P01-actors.md (tác nhân đã chốt), rồi tài liệu nguồn." So với mục 3: "Đính kèm thêm P02-usecases.md hiện có và P02R-review.md, ghi trong YEU_CAU_BO_SUNG các mã UCR cần áp dụng".
- Gặp gì: phần hướng dẫn chạy lại chỉ nằm ở mục 3 (dành cho người dùng). Bên trong khối prompt, [Context] không nhắc P02 hiện có hay P02R, [Action] không có bước "đọc bản trước, giữ mã, áp dụng UCR". AI nhận đúng khối prompt chỉ thấy câu "Áp dụng UCR-01..." ở [Yêu cầu bổ sung] và phải tự suy ra phải tìm file P02R, phải giữ mã cũ (C3), phải tăng phiên bản (C5).
- Xử lý: tự đọc P02R-review.md và P02-usecases.md 1.0 theo mục 2, mục 3 của prompt; giữ mọi mã; tăng phiên bản lên 1.1; ghi hai file này vào hàng "Đầu vào đã dùng".

### 2. Không rõ chạy lại toàn bộ Bước 1 đến Bước 11 hay chỉ áp dụng phần thay đổi của UCR

- Vị trí: mục 3: "Chạy lại sau review: chỉ khi có ít nhất một UCR được áp dụng." và [Action] "Thực hiện tuần tự các bước sau."
- Gặp gì: chạy lại toàn bộ quy trình trên cùng đầu vào có thể sinh khác biệt ngoài phạm vi UCR (ví dụ đánh giá lại UC-014 theo U-T9, hay Q-30 có thể dẫn tới tách UC-007). Prompt không nói lần chạy lại được phép đổi những gì ngoài UCR, cũng không nói có được sửa lỗi nhất quán tự phát hiện hay không.
- Xử lý: áp dụng đúng bốn UCR cộng các chỉnh sửa hệ quả để artifact nhất quán (Mục 1, 2, 3, 5, 6, ASM-10, ASM-11). Có thêm một sửa nhất quán ngoài UCR: bỏ UC-003 khỏi dòng REQ-17 ở Mục 5 vì Bảng 4b bản 1.0 không ghi REQ-17 cho UC-003. Ghi rõ trong Vấn đề còn mở của P02.

### 3. Không có chỗ quy định để ghi nhật ký thay đổi của lần chạy lại

- Vị trí: mục 3: "UCR không áp dụng ghi mã và lý do vào mục Vấn đề còn mở của P02." Conventions C5 chỉ có hàng "Phiên bản | 1.0 (tăng khi chạy lại)".
- Gặp gì: prompt chỉ quy định chỗ ghi UCR không áp dụng. UCR được áp dụng thì ghi ở đâu, thay đổi những phần tử nào, đều không có chỗ. C5 không có mục lịch sử thay đổi, mà C5 lại cấm lời dẫn. Bước sau (P03, P04) không biết UC nào đổi so với bản trước để rà lại theo bảng phụ thuộc README mục 5.
- Xử lý: ghi các UCR đã áp dụng ở hàng "Đầu vào đã dùng" và một gạch đầu dòng tóm tắt thay đổi trong Vấn đề còn mở, dù mục này theo C5 chỉ dành cho checklist chưa đạt. Trong các cột Lý do có liên quan ghi thêm mã UCR.

### 4. Đề xuất có điều kiện của UCR không có cách ghi

- Vị trí: P02R UCR-01: "Nếu Q-28 được trả lời (b) (mọi chênh lệch trả tại quầy): bỏ ACT-06 khỏi UC-007 và giữ UC-003 như bản gốc."; UCR-03: "Nếu Q-29 được trả lời 'Một lần': giữ tên và mục tiêu gốc." Prompt P02 mục 3 chỉ có hai trạng thái: áp dụng hoặc không áp dụng.
- Gặp gì: hai UCR chỉ đúng khi giả định ASM-10, ASM-11 còn đứng. Prompt không nói phải ghi điều kiện ngược này ở đâu để khi Q được trả lời người dùng biết phải đảo lại.
- Xử lý: ghi điều kiện ngược trong Vấn đề còn mở, ở cột "Ảnh hưởng tới" của Q-29 và ở cột "Phần tử phụ thuộc" của ASM-10.

### 5. Câu hỏi mở do P02R nêu (Q-30) có được chuyển sang P02 hay không

- Vị trí: P02R Mục 6: "Câu hỏi cần người viết trả lời: Q-30 (cách giao vé mới khi đổi vé)." Prompt P02 không nhắc câu hỏi phát sinh từ P02R. Conventions C1 mục 2 (CO_NHAN) cho phép giả định, nhưng P02R ghi "Giả định: Không có".
- Gặp gì: P03, P04 đọc P02 chứ không đọc P02R. Nếu Q-30 chỉ nằm ở P02R thì sẽ bị bỏ sót. Ở chế độ CO_NHAN đáng lẽ có thể ghi ASM cho Q-30, nhưng làm thế sẽ đổi tác nhân phụ của UC-007, ngoài phạm vi các UCR được chọn.
- Xử lý: chép Q-30 vào Câu hỏi mở của P02, giữ nguyên mã, ghi rõ nguồn là P02R-review.md 1.0. Không tạo ASM. Nhắc Q-30 trong Mô tả ngắn UC-007 và Vấn đề còn mở.

### 6. UCR-01 ngầm chuyển REQ-13 nhưng không nói rõ

- Vị trí: P02R UCR-01: "Sửa mục tiêu UC-003 thành ... (thời hạn giữ chỗ 10 phút để lại ở UC-002) ... thêm REQ-40 vào cột REQ của UC-003."
- Gặp gì: UCR nói thêm REQ-40 nhưng không nói bỏ REQ-13 (giữ chỗ 10 phút) khỏi UC-003. Câu "để lại ở UC-002" có thể hiểu là chỉ sửa mục tiêu hoặc là chuyển hẳn REQ.
- Xử lý: hiểu là chuyển hẳn. Bỏ REQ-13 khỏi Bảng 4b của UC-003 và khỏi Mục 5. Giữ REQ-13 ở cột REQ của CAND-30 vì đó là nơi phát hiện ứng viên. Ghi lại trong Vấn đề còn mở.

### 7. Q4 d không còn thoả trọn khi UC-003 được gọi từ UC-007

- Vị trí: mục 4, Q4 d: "có thể thực hiện lại hoặc thất bại độc lập mà không huỷ toàn bộ mục tiêu cha"; Q4 a: "Là một đoạn tương tác liền mạch (thường từ 3 bước trao đổi trở lên) được dùng lặp lại trong từ hai use case User-goal trở lên".
- Gặp gì: nguồn chỉ cho căn cứ vế thứ ba của Q4 d ở nhánh UC-002 (Mục 3, câu 2). Với UC-007, nguồn không nói thanh toán chênh lệch thất bại thì xử lý thế nào. Q4 cũng đòi "mọi điều kiện đều có căn cứ trong nguồn", trong khi việc UC-007 dùng cổng thanh toán chỉ dựa trên ASM-10.
- Xử lý: ghi UC-003 thoả Q4 d (theo nhánh UC-002) và Q4 a (dùng ở UC-002, UC-007 theo ASM-10). Ghi lỗ hổng trong Vấn đề còn mở để P04 UC-007 nêu luồng thất bại.

### 8. Phạm vi của U-N4 khi đổi thuật ngữ

- Vị trí: Phần C, U-N4: "Dùng thuật ngữ của miền nghiệp vụ ..., nhất quán giữa các use case". UCR-02 chỉ đề nghị đổi tên và mục tiêu UC-006.
- Gặp gì: chữ "vé đặt qua điện thoại" còn ở tên CAND-11, CAND-22, Mục 1 (ACT-02, ACT-10), EV-08, tóm tắt REQ-26 đến REQ-28 ở Mục 5, cũng như ở P00 và P01. Prompt không nói thuật ngữ phải nhất quán tới đâu: chỉ tên UC, hay cả ứng viên, sự kiện, ma trận, và có cần đề nghị sửa P00, P01 không.
- Xử lý: đổi trong mọi phần chữ của P02 (kể cả tên ứng viên, sự kiện, tóm tắt REQ). Thêm một dòng "Đề xuất sửa artifact trước" cho P01 (mục tiêu của ACT-02, ACT-10). Không đề nghị sửa P00 vì REQ trích nguyên câu nguồn, mà nguồn dùng lẫn hai cách gọi.

### 9. Mục tiêu theo UCR-03 lệch quy tắc cột Mục tiêu

- Vị trí: Phần D, cột Mục tiêu: "kết quả mà tác nhân chính nhận được khi UC thành công, nhìn từ phía tác nhân ... một câu, bắt đầu bằng tác nhân hoặc kết quả"; Target 10: "Cột Mục tiêu của mọi UC viết từ góc nhìn tác nhân và kiểm chứng được."
- Gặp gì: câu UCR-03 đề nghị ("Các chuyến xếp trong lần làm việc có tuyến, giờ xuất bến, xe và tài xế, được ghi vào lịch chạy của tuần ...") bắt đầu bằng kết quả nhưng không nêu ai nhận kết quả. Ví dụ đúng của prompt đều nêu tác nhân ("Thủ kho có phiếu nhập kho ..."). Câu này có thể bị coi là đạt nửa vời Target 10.
- Xử lý: chép nguyên câu của UCR-03 vì YEU_CAU_BO_SUNG ưu tiên hơn quy tắc của bước (C9); câu vẫn bắt đầu bằng kết quả nên coi là đạt.

### 10. Target 3 không nói "mục Câu hỏi mở" là của artifact nào

- Vị trí: [Target] 3: "mọi kết luận 'Chờ Q-nn' trỏ tới câu hỏi có trong mục Câu hỏi mở".
- Gặp gì: CAND-43 (Chờ Q-14) và CAND-47 đến CAND-49 (Chờ Q-03) trỏ tới câu hỏi trong P00, không có trong Câu hỏi mở của P02. Đọc chữ theo nghĩa hẹp thì không đạt; đọc theo C3 (mã Q liên tục toàn dự án) thì đạt.
- Xử lý: coi là đạt vì mã trỏ tới đúng một câu hỏi. Ghi lý do trong Vấn đề còn mở, không chép lại Q-03, Q-14.

### 11. U-N7 đếm "từ" theo đơn vị nào

- Vị trí: Phần C, U-N7: "Độ dài: thường 2-6 từ tiếng Việt."
- Gặp gì: "Chuẩn bị danh sách hành khách của chuyến" (UCR-04) có 8 âm tiết, tức 5 từ ghép. "Huỷ đặt chỗ qua điện thoại quá hạn" có 7 âm tiết. Prompt không nói đếm theo âm tiết hay theo từ.
- Xử lý: đếm theo từ (chuẩn bị, danh sách, hành khách, của, chuyến = 5) nên đạt. Nếu đếm theo âm tiết thì hai tên này lệch ngưỡng nhẹ, nhưng vì U-N7 dùng chữ "thường" nên không coi là vi phạm.

### 12. Quy tắc tăng phiên bản

- Vị trí: Conventions C5: "| Phiên bản | 1.0 (tăng khi chạy lại) |".
- Gặp gì: không nói tăng 1.0 lên 1.1 hay lên 2.0, cũng không phân biệt sửa nhỏ theo review với chạy lại do P00, P01 đổi.
- Xử lý: dùng 1.1.

## Target không đạt

Không có mục Target nào không đạt. Có hai mục chỉ đạt khi chọn một cách hiểu: Target 3 (vướng mắc 10) và Target 10 với UC-012 (vướng mắc 9). Kết quả tự kiểm: Target 1 đến 14 đều Đạt. Đã kiểm bằng script: Bảng 4a và 4b có cùng 18 mã UC theo cùng thứ tự; ma trận Mục 5 khớp hai chiều với cột REQ của Bảng 4b; mọi UC được trỏ tới ở Mục 3 đều có trong Mục 4; không có em dash và không có mũi tên Unicode.
