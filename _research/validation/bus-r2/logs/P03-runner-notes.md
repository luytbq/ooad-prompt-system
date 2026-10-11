Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P03 - bus-r2

Đầu ra: bus-r2/design/P03-usecase-model.md và bốn file diagrams/P03-usecase-overview.drawio, P03-usecase-online-booking.drawio, P03-usecase-counter-sales.drawio, P03-usecase-return-exchange.drawio. Placeholder KIEU_DUONG_ASSOCIATION, CACH_PHAN_RA_SO_DO, YEU_CAU_BO_SUNG đều "Không có" (mặc định KHONG_MUI_TEN, THEO_NHOM). Số liệu: 9 tác nhân, 27 UC hiệu lực, 48 quan hệ (41 association, 6 include, 1 extend, 0 generalization), 4 sơ đồ. Q-43 và ASM-17 mới (lớn nhất sau lần chạy: Q-43, ASM-17).

Cách kiểm: script ngoài (không thuộc bộ prompt) kiểm toạ độ bội số 10, khoảng cách node tối thiểu 40, lề trong boundary tối thiểu 40, đường nối không cắt qua node nào ngoài hai đầu mút (tính theo hình chữ nhật bao, từ tâm node qua các điểm uốn), bảng Node/Edge khớp file .drawio (ID, nhãn, toạ độ, nguồn/đích, điểm uốn), tập tác nhân của association khớp cột Tác nhân chính/phụ của P02 Bảng 4a, và minidom parse cả bốn file .drawio. Tất cả đạt. Mục Target 8 chỉ đạt một phần (xem vướng mắc 3).

## Vướng mắc

1. Toạ độ bội số của 10 mâu thuẫn với độ lệch 55 và tâm elip.
   - Vị trí: Phần D, L-12: "cột hai cách cột một 80 và lệch xuống nửa bước dòng (55)"; L-10: "mọi toạ độ là bội số của 10"; Conventions C7.1: điểm uốn "bội số của 10"; L-04: UC h = 70.
   - Gặp phải: top của UC cột hai = top cột một + 55 không phải bội số của 10. Tâm dọc của UC h = 70 luôn có phần dư 5, nên điểm uốn bội số của 10 không thể nằm đúng tâm elip để đoạn cuối đi ngang.
   - Xử lý: dùng độ lệch 50; điểm uốn lấy bội số của 10 gần tâm (đoạn cuối lệch tối đa 5 so với tâm, vẫn đi qua khe giữa hai UC cột đối diện). Ghi vào Vấn đề còn mở của artifact.

2. Quan hệ giữa UC khác nhóm thuộc sơ đồ phân rã nào chưa rõ.
   - Vị trí: Bước 8: "Sơ đồ phân rã chỉ tạo cho nhóm ... có ít nhất một quan hệ include, extend hoặc generalization giữa UC, và vẽ đầy đủ quan hệ của nhóm đó"; "tác nhân và UC thuộc nhóm khác chỉ xuất hiện khi có quan hệ trực tiếp với UC trong nhóm".
   - Gặp phải: UC-008 (nhóm Đặt vé trực tuyến) được UC-004, UC-005 (nhóm Bán vé tại quầy) và UC-014, UC-015 (nhóm Trả vé và đổi vé) include; UC-010 (Đặt vé trực tuyến) extend UC-014 (Trả vé và đổi vé). Hiểu "đầy đủ quan hệ của nhóm" theo mọi quan hệ chạm tới nhóm thì sơ đồ Đặt vé trực tuyến phải chứa thêm UC-004, 005, 014, 015 mà không có tác nhân đi kèm (tác nhân nhóm khác không có quan hệ trực tiếp với UC trong nhóm), tạo UC mồ côi. Prompt cũng không nói có vẽ association của UC nhóm khác hay không.
   - Xử lý: mỗi quan hệ liên nhóm vẽ ở sơ đồ của nhóm chứa UC gốc; UC nhóm khác chỉ vẽ làm đầu mút, ghi chú "(nhóm <tên>)", không vẽ association của nó. Hệ quả: sơ đồ Đặt vé trực tuyến không có bốn include đến từ nhóm khác. Ghi vào Vấn đề còn mở.

3. Target 8 (D-AP15) không thoả chắc chắn, không có ngưỡng đo.
   - Vị trí: bảng lỗi D-AP15 "Nhiều đường cắt nhau"; Target 8 "Không có lỗi D-AP01 đến D-AP20"; L-12 đặt UC dùng chung nhiều vai trò ở cột giữa với đường đi qua hành lang.
   - Gặp phải: sơ đồ Tổng quát (27 UC, 9 tác nhân, 41 association) theo bố cục dải L-12 có 24 giao điểm giữa các đường nối dù không đường nào cắt qua elip. Nguồn chính: UC-003 Đăng nhập nối 5 tác nhân chính ở 5 dải khác nhau và Cổng SMS; ba tác nhân phụ bên phải nối UC ở nhiều dải. Thử mọi vị trí dọc của ba tác nhân phụ (lưới 60) không xuống dưới 24. D-AP15 không nêu số giao điểm tối đa nên không phán được đạt hay không.
   - Xử lý: báo Target 8 "chưa đạt hẳn" với số liệu cụ thể trong Vấn đề còn mở. Không đổi cấu trúc bố cục L-12 để giảm giao điểm.

4. Căn cứ nguồn cho include của UC User-goal (UC-008).
   - Vị trí: Bước 3a: "hoặc UC-B là UC User-goal mà nguồn nêu rõ luôn phải thực hiện như một phần bắt buộc của UC-A"; 3c "Có căn cứ trong nguồn"; mô tả Bước 3: "UC được include không đứng một mình".
   - Gặp phải: P02 (UC-008, Vấn đề còn mở) giao P03 xét include UC-008 cho UC-009, UC-004, UC-005, UC-014, UC-015. Chỉ UC-009 có câu nguồn rõ (Mục 1 câu 2). UC-004, UC-005 dựa ASM-03 (REQ-29 chỉ nói "bán vé tại quầy hoặc nhận đặt chỗ", không nêu UC-015). Với UC-014, UC-015 nguồn chỉ nói "đổi sang chuyến khác cùng tuyến", không nêu cách chọn chuyến. UC-008 lại đứng một mình được, trái câu "UC được include không đứng một mình" (câu này đúng cho Subfunction, không cho nhánh User-goal của 3a).
   - Xử lý: tạo ASM-17 (Chờ Q-43) cho UC-014, UC-015 để có căn cứ theo C1 mục 2; UC-004, UC-005 trích ASM-03. Ghi lý do 2.2b cho đường ACT-01 nối UC-008.

5. Điều kiện 4a mệnh đề thứ ba đặt ghi chú Q4 b ở UC-Y, nhưng P02 ghi ở UC-X.
   - Vị trí: Bước 4a: "UC-X là UC Subfunction đã được include ở UC khác và UC-Y chỉ dùng nó khi một điều kiện kiểm chứng được đúng (P02 ghi Q4 b cho UC-Y ở Mô tả ngắn)".
   - Gặp phải: P02 ghi "Q4 b với UC-014" ở Mô tả ngắn của UC-010 (UC-X), còn Mô tả ngắn của UC-014 (UC-Y) chỉ nói "trả thêm chênh lệch qua UC-010 nếu vé mới đắt hơn", không có chữ Q4 b. Cột Tác nhân chính của UC-010 lại ghi "ACT-01 (qua UC-009, UC-014)" khiến thoạt nhìn giống include từ UC-014.
   - Xử lý: đọc theo ý nghĩa (điều kiện kiểm chứng được: vé mới đắt hơn) và vẽ UC-010 extend UC-014 với điểm mở rộng "Thu phần chênh lệch"; UC-010 vừa bị UC-009 include vừa extend UC-014.

6. Nhãn UC có ngăn extension points trên sơ đồ không vẽ extend.
   - Vị trí: Phần B Mục 5 "UC có điểm mở rộng thì nhãn gồm tên và ngăn extension points" so với Bước 8 phương án hai "không vẽ include, extend, generalization giữa UC trên sơ đồ này".
   - Gặp phải: UC-014 có điểm mở rộng nhưng sơ đồ Tổng quát không vẽ extend, ngăn extension points sẽ nằm trơ trọi.
   - Xử lý: Tổng quát dùng nhãn thường (w 160, h 70); ngăn extension points (w 200, h 90) chỉ ở sơ đồ Trả vé và đổi vé. Ghi vào Vấn đề còn mở.

7. Ngôn ngữ nhãn phần tử.
   - Vị trí: Phần B Mục 5: "Nhãn: tên tiếng Việt (hoặc theo NGON_NGU_TEN_PHAN_TU của hồ sơ dự án)"; project-profile.md ghi NGON_NGU_TEN_PHAN_TU "Tiếng Anh, PascalCase cho lớp, camelCase cho thuộc tính và phương thức, snake_case cho bảng và cột".
   - Gặp phải: hồ sơ không nói tên tác nhân, use case; Conventions C2 mặc định có hai cột tiếng Việt, tiếng Anh.
   - Xử lý: dùng tên tiếng Việt của P01, P02 làm nhãn. Cần người dùng xác nhận nếu muốn nhãn tiếng Anh.

8. UC chính ở góc trên trái so với UC được include bên phải.
   - Vị trí: L-05 "UC chính của nhóm ở góc trên trái của boundary" và L-06 "UC được include đặt bên phải UC gốc".
   - Gặp phải: sơ đồ Đặt vé trực tuyến, UC-008 (được include, đồng thời là mục tiêu riêng của hành khách) có thể xem là UC chính của nhóm nhưng phải nằm bên phải UC-009.
   - Xử lý: UC gốc UC-009 ở cột trái, UC-008 ở cột phải hàng trên (cùng cột include, đỉnh cao nhất).

9. Chỗ đặt UC dùng chung nhiều dải và tác nhân phụ.
   - Vị trí: L-12 dòng "UC nối từ hai tác nhân chính trở lên ... đặt ở cột giữa, ... căn tâm dọc theo khoảng giữa các tác nhân nó nối".
   - Gặp phải: UC-003 nối 5 tác nhân chính và 1 tác nhân phụ; khoảng giữa các tác nhân rơi đúng hàng ra của UC-017 sang tác nhân phụ. Quy tắc không nói ưu tiên giữa "căn tâm" và "không chắn đường".
   - Xử lý: đặt UC-003 ở cột giữa, tâm dọc 1085 (gần tâm ACT-03, thấp hơn đường ra của UC-017 ở y 1000 là 50). Đường từ ACT-01..ACT-05 đi qua hành lang theo điểm uốn L-12, mỗi đường một làn riêng cách 10.

10. Mục 3 "chỉ khi có" so với C5 "Mục nào không có nội dung thì ghi Không có".
    - Xử lý: giữ mục, ghi "Không có".

11. Quy ước hướng association của tác nhân phụ.
    - Vị trí: Phần B Mục 1 "Association ghi nguồn là tác nhân, đích là use case".
    - Gặp phải: với tác nhân phụ bên phải, điểm uốn trong Điểm uốn phải liệt kê từ tác nhân tới UC (ngược với chiều đi từ UC ra).
    - Xử lý: liệt kê theo thứ tự từ nguồn (tác nhân) tới đích (UC), theo Conventions C7.1.

12. Đọc ngoài phạm vi (vô tình).
    - Khi tìm cách ghi dòng đầu nhật ký, lệnh head -5 đã in 5 dòng đầu của bus-r2/logs/P02R-runner-notes.md (nhật ký bước khác, không được đọc). Chỉ thấy dòng model, tiêu đề và dòng tóm tắt đầu ra; không dùng nội dung đó cho P03.

## Kết quả tự kiểm theo Target

| Mục | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | Mã và tên khớp P01, P02; UC-013 (Loại) không vẽ |
| 2 | Đạt | Khớp P02 Bảng 4a (đã kiểm bằng script); UC-008 và UC-010 theo Bước 2.2 ("qua ..." không nối) |
| 3 | Đạt | Không association tác nhân-tác nhân, UC-UC |
| 4 | Đạt | Ngoại lệ 2.2b: ACT-01 nối UC-008, có lý do ở RL-15 |
| 5 | Đạt | 6 include đúng chiều, một tầng, không chu trình; 3c dựa ASM-03 và ASM-17 |
| 6 | Đạt | RL-48 có điều kiện, điểm mở rộng, note, có trong Mục 2 |
| 7 | Đạt | Không có generalization (P01 không có tổng quát hoá tác nhân; P02 không có UC cha) |
| 8 | Không đạt một phần | D-AP15: 24 giao điểm đường nối (vướng mắc 3); D-AP01 đến D-AP14, D-AP16 đến D-AP20 không vi phạm |
| 9 | Đạt | |
| 10 | Đạt | Không đường nào cắt qua elip; trình tự thời gian chỉ ở mức gần đúng theo nghiệp vụ |
| 11 | Đạt | N = 27 (21 đến 40) và M = 9 > 8: phương án hai; sơ đồ phân rã tối đa 5 UC |
| 12 | Đạt | Đã so từng phần tử bảng và .drawio bằng script |
| 13 | Đạt | minidom parse đạt; toạ độ và điểm uốn bội số 10; khoảng cách tối thiểu 40 |
| 14 | Đạt | Mọi include, extend có lý do và REQ |
| 15 | Đạt | Có Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở |
