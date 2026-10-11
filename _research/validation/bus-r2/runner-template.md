Bạn là một AI agent có quyền đọc ghi file, được người dùng giao chạy một bước của bộ prompt phân tích thiết kế (cách chạy "agent có quyền đọc ghi file" trong README). Bạn chưa từng thấy bộ prompt này trước đây.

Đường dẫn:
- Bộ prompt: /home/luytbq/.treehouse/ooad-prompt-system-5c423b/2/ooad-prompt-system/ (các file ở gốc repo: 00-Conventions.md, 00-ProjectProfile-Template.md, README.md, Pxx-*.md, X1, X2).
- Dự án: /home/luytbq/.treehouse/ooad-prompt-system-5c423b/2/ooad-prompt-system/_research/validation/bus-r2/ . Tài liệu nguồn yeu-cau-xe-khach.md nằm ở đây; THU_MUC_DAU_RA "./design/" tương ứng với thư mục bus-r2/design/.

Phạm vi đọc (bắt buộc, để kết quả chỉ phản ánh chất lượng prompt):
- Được đọc: file prompt của bước, 00-Conventions.md, README.md, bus-r2/design/project-profile.md, bus-r2/yeu-cau-xe-khach.md, và các artifact đầu vào trong bus-r2/design/ mà mục 2 và mục 3 của prompt yêu cầu.
- Không được đọc bất kỳ file nào khác trong _research/ (authoring-guide, các file *-notes.md, handoff-contracts.md, validation/bus, validation/bike, validation/clinic, validation/aims, audit-findings, mọi file findings, bus-r2/fix-log.md, bus-r2/findings.md, nhật ký của bước khác trong bus-r2/logs/). Không đọc prompt của bước khác trừ khi prompt bước này bảo đọc.

Việc cần làm:
1. Đọc kỹ prompt của bước, thực thi khối prompt ở mục 4 như AI nhận prompt đó. Điền placeholder theo hướng dẫn ở mục 3 của prompt, với các giá trị ghi ở phần "Tham số bước" dưới đây; placeholder không được nêu thì để giá trị mặc định hoặc "Không có".
2. Ghi đầu ra (artifact .md và sơ đồ .drawio nếu có) vào bus-r2/design/ đúng tên và vị trí theo 00-Conventions.md mục C4 và mục 2 của prompt. Ghi đè nếu đã tồn tại.
3. Tự kiểm tra đầu ra theo các mục Target của prompt trước khi kết thúc. File .drawio phải là XML hợp lệ (kiểm tra bằng python3 -c "import xml.dom.minidom,sys; xml.dom.minidom.parse(sys.argv[1])" <file>).
4. Ghi nhật ký người chạy vào bus-r2/logs/<BUOC>-runner-notes.md (tạo thư mục nếu chưa có). Dòng đầu nhật ký ghi model của phiên chạy (Sonnet). Liệt kê mọi chỗ trong prompt hoặc Conventions mà bạn thấy mơ hồ, mâu thuẫn, thiếu hướng dẫn, đầu vào không khớp đầu ra, quá tải ngữ cảnh, hoặc không thể thoả đồng thời. Mỗi mục: vị trí trong prompt (mục, câu trích nguyên văn), bạn đã gặp gì với đề này, bạn đã xử lý thế nào. Ghi cả mục Target nào không đạt và lý do. Không có gì thì ghi "Không có vướng mắc". Viết tiếng Việt, không dùng em dash, không dùng mũi tên Unicode (dùng -->).
5. Trả lời ngắn (dưới 200 từ): danh sách file đã ghi, số lượng phần tử chính (REQ, ACT, UC, Q, ASM... tuỳ bước), mã Q, ASM lớn nhất sau lần chạy, và 3 vướng mắc quan trọng nhất.

Không sửa file prompt sản phẩm. Không chạy git.

Tham số bước:
