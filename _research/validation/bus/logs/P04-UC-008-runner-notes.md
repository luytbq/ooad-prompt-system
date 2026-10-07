# Nhật ký người chạy P04 UC-008 Trả vé

Model: mặc định của phiên điều phối (Claude Opus 5.5, claude-opus-5-5).

Bước: P04, UC_ID = UC-008; TEN_HE_THONG_TRONG_LUONG = Không có (dùng "Hệ thống"); YEU_CAU_BO_SUNG = Không có. Chế độ CO_NHAN, MUC_CHI_TIET DAY_DU.

Đầu ra: design/P04-uc-specs/UC-008-return-ticket.md, design/P04-uc-specs/_BR-register.md (thêm BR-11 đến BR-16, thêm UC-008 vào BR-03, BR-10), design/diagrams/P04-activity-UC-008.drawio (XML hợp lệ, 3 partition, 31 node, 32 cạnh). Mã mới: Q-35 đến Q-39, ASM-18 đến ASM-23, BR-11 đến BR-16.

## Vướng mắc

1. Mục 3, bảng phần cần dùng: "P01-actors.md | Mục 2 (bảng tác nhân)"; "P03-usecase-model.md | Các dòng của Mục 1 (bảng quan hệ) và Mục 2 (điểm mở rộng)". Mâu thuẫn với [Action] 1e: "Tìm mã Q và ASM lớn nhất trong P00 đến P03". ASM-06, ASM-07 nằm ở mục Giả định của P01, không ở Mục 2; nếu chạy bằng chat chỉ dán trích đoạn theo bảng thì sẽ cấp trùng mã ASM. Xử lý: chạy bằng agent nên đọc cả mục Câu hỏi mở, Giả định của P01, P02, P03; mã lớn nhất là Q-34, ASM-17 (từ đặc tả UC-002).

2. [Action] 1e: "Tìm mã Q và ASM lớn nhất trong P00 đến P03". Không rõ "P00 đến P03" có gồm P02R-review.md không; bảng đầu vào mục 2 không liệt kê P02R, nhưng P02 ghi Q-30 "nêu ở P02R-review.md 1.0, ghi lại ở đây". Xử lý: không đọc P02R (ngoài phạm vi đầu vào); dựa vào việc P02 đã chép Q-30. Rủi ro: nếu P02R có Q hoặc ASM khác không được chép sang P02 thì mã có thể trùng.

3. F4.2 mục 12: "ghi tên các tác nhân nối bằng " / " và mọi khác biệt về hành vi giữa họ đặt thành luồng thay thế". Với UC-008, hai tác nhân dùng hai kênh khác nhau (ASM-02: hành khách trả vé trực tuyến trên website, nhân viên bán vé trả vé mua tại quầy) và hình thức hoàn khác nhau. Prompt không nói luồng chính nên theo kênh nào, cũng không nói nên tách theo tác nhân hay theo thuộc tính của vé. Xử lý: luồng chính theo vé mua trực tuyến (ACT-01 đứng trước trong P02, ACT-06 là tác nhân phụ của UC); khác biệt đặt ở 3a (sai kênh) và 7a (vé mua tại quầy, không có hành động, tiếp tục bước 10).

4. F10.5: "ID: partition "P-ACT-nn" cho tác nhân (theo mã ACT)". F10.4 cho một partition chung khi nhiều tác nhân chính ghi chung, nhưng không quy định ID của partition đó. Xử lý: dùng P-ACT-01-02.

5. F10.5: "Điểm uốn: ... bắt buộc điền cho cạnh quay lại (tới merge node M-K) và cạnh vượt qua partition khác" so với Conventions C7.1: "cạnh đi thẳng hoặc để draw.io tự định tuyến ghi "-"". Cạnh E-19 (D-6 --> A-6a) đi thẳng ngang từ partition tác nhân sang partition hệ thống. Xử lý: ghi "-" theo C7.1, nêu đường đi ở Ghi chú, ghi lựa chọn vào Vấn đề còn mở.

6. F10.6: "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action". Decision 40 rộng cùng trục với action luồng chính 180 rộng, nên trục cách decision 30 nằm trong bề ngang action kế tiếp và cạnh sẽ cắt qua action (trái C7.3). Đặc tả UC-002 đã gặp cùng vấn đề. Xử lý: đặt trục ở x = 600, cách mép phải action luồng chính 30.

7. F10.4: "Decision đặt trong partition của chủ thể đánh giá điều kiện (thường là hệ thống, vì hệ thống kiểm tra kết quả do tác nhân phụ trả về), ngay dưới action phát sinh điều kiện". Khi action phát sinh điều kiện (A-9 Trả về kết quả hoàn tiền) nằm ở partition Cổng thanh toán, hai yêu cầu "partition hệ thống" và "ngay dưới action" không thoả cùng lúc. Xử lý: D-9 ở P-SYS, thấp hơn A-9, cạnh E-26 có điểm uốn.

8. F1, hàng Quan hệ: ví dụ chỉ nêu include, extend, generalization; Target 1 đòi "quan hệ ... khớp nguyên văn P03". P03 chỉ có association (RL-11, RL-12, RL-13) cho UC-008. Không rõ association có phải liệt kê ở hàng này không. Xử lý: ghi "Không có quan hệ include, extend, generalization" kèm mã các association để đối chiếu.

9. F3: "Tiền điều kiện: trạng thái của hệ thống phải đúng trước khi use case bắt đầu". Không có hướng dẫn cho tiền điều kiện chỉ áp dụng cho một trong hai tác nhân chính. ASM-09 (nhân viên phải đăng nhập) có trong P02 nhưng P03 chưa nối ACT-02 với UC-010. Xử lý: ghi tiền điều kiện có điều kiện "Khi tác nhân là nhân viên bán vé: ... (ASM-09)".

10. F7.3: "Quy tắc: một câu nguyên tử". REQ-31, REQ-32, REQ-33 là một bảng mức hoàn theo khoảng thời gian (một công thức từng khúc). Không rõ nên giữ một BR Tính toán hay tách theo khúc. Xử lý: tách ba BR (BR-12 ràng buộc dưới 4 giờ, BR-13 90%, BR-14 50%) để mỗi luồng dẫn đúng một mã.

11. F7.5: "ghi quy tắc do AI tự nghĩ ra" là lỗi, nhưng prompt không nói quy tắc dựa trên một ASM đã có từ bước trước có được cấp BR không. Kênh trả vé theo kênh mua chỉ có ở ASM-02 (P00). Xử lý: cấp BR-11 có trích ASM-02 trong nội dung, theo tiền lệ BR-05 trích ASM-12.

12. F5.5: "mỗi bước gọi hệ thống ngoài có luồng hệ thống ngoài lỗi hoặc không phản hồi khi nguồn nêu hoặc khi đã có Q-nn". Nguồn không nêu hoàn tiền thất bại và chưa có Q nào về việc này. Không rõ "đã có Q-nn" là Q có sẵn từ bước trước hay được tạo mới trong lần chạy. [Action] 4 cho CO_NHAN ghi ASM. Xử lý: tạo Q-37 và ASM-21, viết luồng 9a; không tạo luồng "không phản hồi" vì không có căn cứ.

13. Target 5a: "qua màn hình hoặc kênh thông báo mà nguồn nêu; nguồn không nêu cách báo thì có Q-nn". Nguồn không nêu cách báo kết quả trả vé. Xử lý: coi kênh website (hành khách) và quầy (nhân viên bán vé) theo ASM-02 là kênh báo, không tạo Q riêng. Có thể bị đánh giá là chưa thoả nghĩa chữ.

14. F7.4 mục 2: "nếu hai quy tắc mâu thuẫn thì tạo Q-nn" và mục 4: "Không sửa nội dung ... của BR đã có". Trả vé làm chỗ có một vé đã huỷ, trong khi BR-02 ("hai vé không được cùng một chỗ") và BR-03 ("chỗ chưa có vé") hiểu theo nghĩa chữ chặn bán lại chỗ. Hướng dẫn đủ để xử lý: tạo Q-36, ASM-20, ghi Đề xuất sửa artifact trước cho BR-02, BR-03. Ghi lại vì lỗi diễn đạt BR-02, BR-03 ở UC-002 chỉ lộ ra khi chạy UC khác; prompt không nhắc kiểm tra BR cũ có bao quát trạng thái "đã huỷ" của đối tượng.

15. Quá tải ngữ cảnh: prompt P04 khoảng 400 dòng, Conventions 263 dòng, P00 264 dòng với bảng rộng, P02 304 dòng (54 KB). Phải đọc P02 theo mục mới giữ được ngữ cảnh. Không gây sai kết quả.

## Target

Tất cả 16 mục Target tự đánh giá Đạt. Các mục có diễn giải:
- Target 1: hàng Quan hệ diễn giải theo vướng mắc 8.
- Target 5a: kênh báo kết quả diễn giải theo vướng mắc 13.
- Target 13, 15: D-9 không thẳng dưới A-9 (vướng mắc 7); trục rẽ nhánh lệch so với F10.6 (vướng mắc 6). Không có node chồng nhau, không cạnh nào cắt qua node (đã kiểm bằng script theo toạ độ tuyệt đối).
