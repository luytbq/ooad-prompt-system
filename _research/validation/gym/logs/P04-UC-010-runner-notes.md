Model của phiên chạy: Sonnet

# Nhật ký người chạy P04 cho UC-010 Đặt chỗ lớp nhóm

Đầu ra: design/P04-uc-specs/UC-010-book-class-spot.md; design/diagrams/P04-activity-UC-010.drawio (XML hợp lệ, 30 node kể cả 2 partition, 30 cạnh); design/P04-uc-specs/_BR-register.md (thêm BR-06 đến BR-12). Cấp Q-58 đến Q-62, không có ASM (NGHIEM_NGAT). Số lớn nhất tìm được trước khi cấp: Q-57 (UC-005), ASM chưa có.

Kiểm tra đã làm: toạ độ bội số của 10, không node chồng nhau, không cạnh cắt qua node (kiểm bằng script trên toạ độ tuyệt đối), bảng Node, bảng Edge và .drawio sinh từ cùng một nguồn dữ liệu nên khớp ID.

## Mục Target không đạt hoàn toàn

- Target 5a (đạt một phần): luồng 7a2a (hội viên từ chối vào danh sách chờ) kết thúc use case mà không có bước hệ thống báo kết quả riêng. Lý do: bước 7a1 đã báo lớp đủ chỗ, và thêm một bước "báo huỷ" cho lựa chọn của chính tác nhân là bịa. Đã ghi ở Vấn đề còn mở.
- Target 12 (đạt một phần): luồng 7a được viết theo cách hội viên chọn vào danh sách chờ, là một trong hai cách đọc của nguồn; có Q-62. Các bước 2 và 9 không có câu gốc trực tiếp. Đã ghi ở Vấn đề còn mở.
- Các mục khác tự đánh giá Đạt.

## Vướng mắc

1. Vị trí: [Action] 4 và Conventions C1.2 NGHIEM_NGAT: "Chỗ nào nguồn thiếu hoặc mơ hồ thì ghi vào mục 'Câu hỏi mở' ... không tự điền nội dung". Đề này: nguồn Mục 3 câu 3 "Lớp đã đủ chỗ thì hội viên được vào danh sách chờ" mơ hồ giữa "hệ thống tự đưa vào" và "hội viên chọn vào" (P02 viết "hội viên vào danh sách chờ", P00 REQ-26 viết "có thể vào"). Use case này bắt buộc có luồng 7a (REQ-26, EV-08). Prompt không nói cách viết luồng khi nguồn mơ hồ giữa hai cách mà luồng vẫn phải tồn tại ("Chờ Q-nn" ở F5.4 chỉ dùng khi "cách xử lý tiếp theo chưa được nguồn quy định"). Xử lý: viết theo cách khớp REQ-26 ("có thể"), tạo Q-62, ghi rõ trong Vấn đề còn mở cách sửa nếu trả lời khác. Đề nghị bổ sung vào prompt một quy tắc cho tình huống này ở NGHIEM_NGAT.

2. Vị trí: F7.4 mục 2 "nếu hai quy tắc mâu thuẫn thì tạo Q-nn" và [Action] 1e. Đề này: REQ-23 (đặt sớm nhất 7 ngày trước giờ học) mâu thuẫn REQ-93 (mở đặt tuần mới lúc 6 giờ sáng thứ Hai), Q-11 đã có từ P00. Prompt không nói bước và luồng kiểm tra viết thế nào khi hai BR mâu thuẫn và chưa có câu trả lời. Xử lý: tách thành BR-06 và BR-07 (Ghi chú sổ BR ghi mâu thuẫn, chờ Q-11), bước 5 và luồng 5b dẫn cả hai mà không chọn bên nào, không tạo Q mới. Hệ quả: điều kiện của 5b không kiểm chứng được cho tới khi Q-11 trả lời. Mục 12a yêu cầu tính lại số liệu từ BR; tôi tính ví dụ trong Vấn đề còn mở (26/10/2026 là thứ Hai; 18:00 ngày 19/10 so với 6:00 ngày 26/10).

3. Vị trí: F10.6 "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action". Đề này: decision D-5 rộng 40 nằm dưới action rộng 180 (cạnh phải của action cách tâm 90, của decision cách 20). Trục dọc cách decision 30 về bên phải (x tương đối 200) cắt qua action kế tiếp của luồng chính, vì action này trải tới x tương đối 240. Xử lý: đặt trục ở x tương đối 260, cách tâm cột chính 110 (qua mép phải action 20 đơn vị). Quy tắc 30 nên ghi là "cách mép phải node rộng nhất của cột chính 20 đến 30".

4. Vị trí: F10.2 và F10.6 về cạnh quay lại, không có quy tắc cho nhiều cạnh quay về cùng một merge node (đề này 3 cạnh 5a, 5b, 6a về M-2). Xử lý: tự đặt các làn dọc ngoài cột nhánh (x 1110, 1130, 1150) và các làn ngang phía trên merge (y 90, 80, 70), làn ngoài hơn đi cao hơn để không cắt nhau; ba cạnh dùng chung đoạn cuối vào cạnh trên của M-2. Cột Điểm uốn dùng toạ độ tuyệt đối còn toạ độ node trong bảng Node là tương đối theo partition, nên người đọc phải tự đổi (partition hệ thống lệch 520).

5. Vị trí: F10.2 "Khi luồng Na là cách làm khác thay cho chính bước N do tác nhân chọn, D-N đặt ngay trước A-N" và "Luồng thay thế không có hành động ... cạnh mang guard của luồng đi thẳng từ decision D-N tới final". Đề này: luồng lồng 7a2a là lựa chọn của tác nhân tại hành động 7a2 của luồng 7a (không phải bước của luồng chính). Quy tắc ID "D-<số bước>" không bao quát decision cho bước lồng. Xử lý: dùng ID D-7a2 đặt trong partition hội viên ngay trước A-7a2, nhánh không hành động nối thẳng tới FINAL-2. Chưa rõ prompt có chủ ý cho phép lồng kiểu này không.

6. Vị trí: F10.4 "Decision thể hiện lựa chọn của tác nhân đặt trong partition của tác nhân" cùng với F10.6 bố cục. Đề này: nhánh 7a đi từ partition hệ thống sang partition hội viên (D-7a2) rồi quay lại hệ thống (A-7a3). Cạnh nối ngang bị cột chính của hệ thống (A-8, A-9) chắn. Không có hướng dẫn đặt chuỗi nhánh có qua lại partition. Xử lý: đặt A-7a3, A-7a4, FINAL-3 phía dưới điểm kết thúc của luồng chính (chiều cao sơ đồ 1700), cạnh E-26 đi theo đường dọc trong partition hội viên rồi ngang vào A-7a3. Bố cục chấp nhận được nhưng hơi lạ khi nhánh nằm dưới điểm kết thúc chính.

7. Vị trí: F5.3 "Nguồn không nêu thứ tự ưu tiên thì theo thứ tự xuất hiện trong nguồn; ghi Q-nn ở NGHIEM_NGAT" cùng F4.2 mục 11. Đề này: bốn điều kiện kiểm tra (khoá, lớp huỷ và thời hạn, hạn mức 2 lớp, đủ chỗ) cùng có thể đúng; nguồn không nêu thứ tự phản hồi. Nếu gộp một bước thì phải tạo Q về thứ tự; tôi tách thành bốn bước theo từng đối tượng (hội viên, lớp, hội viên, lớp) để tránh luồng chồng lấn. Thứ tự bốn bước là chọn lựa của người viết, ghi ở mục 8. Prompt cho phép "tách bước" nhưng không nói thứ tự tách lấy từ đâu và có cần Q khi tách hay không.

8. Vị trí: [Action] 1c "mọi REQ mà một bước, luồng, BR hoặc trường dữ liệu của đặc tả này dùng tới (kể cả REQ Chức năng của use case khác cung cấp dữ liệu, ví dụ giá, mã đơn)". Đề này: Dữ liệu ra 1 dùng REQ-70 (loại Dữ liệu, không phải Chức năng), REQ-69 (Chức năng của UC-009), và luồng 5a dùng REQ-73, REQ-76 (chức năng huỷ lớp của UC-015, UC-014). Câu "kể cả REQ Chức năng" không nói rõ có tính REQ loại Dữ liệu hay không. Xử lý: tính cả bốn REQ, thêm một dòng "Đề xuất sửa artifact trước" cho P02. Ngoài ra bảng "mục tiêu" Mục 1 của P02 liệt kê REQ của UC-010 không có REQ-38 và REQ-94, khác bảng 4b; tôi theo bảng 4b.

9. Vị trí: F4.2 mục 17 "use case tạo, đổi hoặc làm mất hiệu lực dữ liệu mà một use case do tác nhân thời gian kích hoạt dùng làm mốc". Đề này: UC-010 tạo chỗ đã đặt mà UC-015 (đếm người đặt lúc 2 giờ trước giờ học) và UC-016 (tính vắng mặt) đọc, nhưng mốc thời gian của chúng là giờ học do lịch lớp đặt. Chưa rõ "dữ liệu dùng làm mốc" có gồm bản ghi đặt chỗ hay chỉ mốc giờ. Xử lý: coi mốc là giờ học, không viết bước hẹn mốc, ghi lý do ở mục 8.

10. Vị trí: F6 và NGHIEM_NGAT (không tự thêm trường dữ liệu). Đề này: Dữ liệu ra 1 chỉ lấy bốn trường theo REQ-70 (loại lớp, phòng, huấn luyện viên, giờ). Hội viên chọn lớp mà lịch không cho biết chi nhánh (chuỗi có 4 chi nhánh) hay số chỗ còn lại; nguồn không nêu hiển thị các thông tin này, và Q-12 chỉ hỏi về điều kiện gói. Tôi không tạo Q riêng vì không có điểm bám trong nguồn ngoài việc suy ra; có thể coi đây là lỗ hổng của quy tắc "không thêm trường" khi tác nhân cần thông tin để ra quyết định (F4.2 mục 5, F4.5 nói bước hiển thị chỉ giữ khi thông tin cần cho quyết định sau).

11. Vị trí: F3 "Hậu điều kiện (thành công): trạng thái hệ thống sau khi luồng chính kết thúc". Đề này: mục tiêu P02 của UC-010 gồm hai kết cục thành công (có chỗ, hoặc có vị trí chờ), kết cục thứ hai nằm ở luồng thay thế 7a kết thúc "(thành công)". Prompt không nói hậu điều kiện cho biến thể thành công. Xử lý: thêm một dòng thứ hai trong cùng ô, nêu rõ "Khi use case kết thúc ở luồng 7a". Hậu điều kiện tối thiểu vẫn đúng vì mọi luồng thất bại kết thúc trước bước lưu.

12. Vị trí: F4.4 / C1.6, đọc đầu vào. Prompt P04 dài (408 dòng, khoảng 34.000 token) phải đọc hai lần; P00, P02 dài nên đọc bằng tìm theo tiêu đề và mã REQ như prompt hướng dẫn, mục Câu hỏi mở của P00 (43 câu) phải đọc toàn bộ vì cần cấp mã Q và biết Q liên quan. Chưa tới mức quá tải ngữ cảnh nhưng tổng đọc lớn. Không có thêm vướng mắc ngoài việc phải tự tách phần cần đọc của P02 (Mục 5, Mục 4 và EV-08 nằm rải rác).

13. Vị trí: Conventions C7.1 (khuyến nghị thêm cột x, y, w, h vào bảng Node) so với F10.5 (liệt kê cột bảng Node không có x, y, w, h). Xử lý: thêm bốn cột sau cột Ghi chú. Hai nơi nên thống nhất.

## Không có vướng mắc ở các điểm sau

Cấp mã Q (C3), cấp mã BR (F7.4) và xuất lại sổ BR; tên tác nhân, tên use case, quan hệ (P03 không có include, extend, generalization với UC-010); khung C5.
