# Nhật ký người chạy - P04 UC-015 Soát vé lên xe

Tham số: UC_ID = UC-015; TEN_HE_THONG_TRONG_LUONG = Không có (dùng "Hệ thống"); YEU_CAU_BO_SUNG = Không có. Hồ sơ dự án: CO_NHAN, DAY_DU.

Đầu ra: design/P04-uc-specs/UC-015-check-boarding-ticket.md; design/P04-uc-specs/_BR-register.md (thêm BR-20, BR-21, BR-22, thêm UC-015 vào BR-10); design/diagrams/P04-activity-UC-015.drawio (XML hợp lệ, kiểm tra bằng xml.dom.minidom).

## Vướng mắc

1. Phạm vi tìm mã Q, ASM lớn nhất.
   - Vị trí: [Action] bước 1e, "Tìm mã Q và ASM lớn nhất trong P00 đến P03 và trong mọi đặc tả P04 đã có".
   - Gặp: thư mục có P02R-review.md (nằm "giữa" P00 và P03 theo tên bước) nhưng bảng đầu vào Mục 2 và bảng Mục 3 không liệt kê P02R. P02 có ghi Q-30 "nêu ở P02R-review.md 1.0", tức P02R có thể cấp mã Q.
   - Xử lý: chỉ grep mã Q-nn, ASM-nn trong P02R để chắc không trùng (kết quả: chỉ tới Q-30, các mã lớn hơn là phần đuôi của REQ-40, REQ-61). Mã lớn nhất lấy từ P00 đến P03 và UC-002, UC-008, UC-013: Q-44, ASM-31. Cấp mới Q-45 đến Q-47, ASM-32 đến ASM-36. Đề nghị prompt ghi rõ "P00, P01, P02, P02R (nếu có), P03".

2. Bước lặp mâu thuẫn với ánh xạ một bước một action.
   - Vị trí: F4.2 mục 9 "Lặp lại: viết bằng một bước 'Lặp lại bước 3-4 cho đến khi <điều kiện>'"; F10.2 "Mỗi bước luồng chính N --> đúng một action có ID 'A-N'"; Target 13 "mỗi bước luồng chính đúng một action".
   - Gặp: UC-015 là phiên soát vé của một chuyến, quét từng vé là vòng lặp (P02 U-R14). Bước 8 "Lặp lại bước 3-7 cho đến khi không còn hành khách lên xe xuất trình vé" không có action tương ứng. Đặc tả UC-013 đã có cùng vướng mắc (ghi ở Vấn đề còn mở của UC-013), nên đây là lỗi lặp lại của prompt.
   - Xử lý: theo mục "Luồng lặp" của F10.2, bước 8 ánh xạ sang M-8 và D-8 (đặt trong partition phụ xe vì phụ xe quyết định), không có A-8. Ghi vào Vấn đề còn mở. Target 13 không đạt ở bước 8. Đề nghị F10.2 nêu ngoại lệ: bước lặp ánh xạ sang decision lặp, không có action.

3. Luồng thay thế thay cho chính bước phát sinh, không có quy tắc đặt decision.
   - Vị trí: F10.2 "Luồng thay thế phát sinh tại bước N --> một decision ID 'D-N' đặt ngay sau A-N"; F5.2 "N là bước mà tại đó điều kiện được phát hiện (thường là bước kiểm tra của hệ thống, hoặc bước tác nhân chọn khác đi)".
   - Gặp: luồng 3a (vé mua trực tuyến chỉ có mã vé SMS, phụ xe nhập tay thay cho quét) là lựa chọn khác đi của tác nhân tại bước 3. Đặt D-3 sau A-3 nghĩa là đã quét rồi mới rẽ nhánh, sai nghĩa.
   - Xử lý: đặt D-3 trước A-3 (sau M-3), ghi lý do ở cột Ghi chú của D-3 và Vấn đề còn mở. Đề nghị F10.2 thêm: khi luồng Na là cách làm khác thay cho bước N do tác nhân chọn, D-N đặt trước A-N.

4. Sự kiện kích hoạt của P02 không khớp với bước 1.
   - Vị trí: F1 "Sự kiện kích hoạt | từ P02"; Target 5 "Luồng chính: bước 1 là sự kiện kích hoạt"; F4.2 mục 10 "Bước đầu tiên là sự kiện kích hoạt".
   - Gặp: P02 ghi "Hành khách lên xe xuất trình vé, phụ xe quét mã vé (EV-19)", là sự kiện của từng lần quét, trong khi P02 cũng định nghĩa UC-015 là phiên soát vé của chuyến với quét từng vé là vòng lặp. Bước 1 hợp lý là phụ xe bắt đầu soát vé của chuyến; sự kiện EV-19 rơi vào bước 3 trong vòng lặp. Không thoả đồng thời F1 (chép P02) và Target 5.
   - Xử lý: giữ nguyên văn P02 ở bảng thông tin chung, bước 1 là bắt đầu phiên; ghi đề xuất sửa P02 (EV-19 và sự kiện kích hoạt của UC-015) và Vấn đề còn mở. Target 5 không đạt một phần.

5. Hành động tiếp diễn sau khi use case kết thúc.
   - Vị trí: F4.2 mục 15 (chờ sự kiện có hạn giờ trong phiên); F5.4 danh sách giá trị Quay lại / Kết thúc.
   - Gặp: REQ-60 "gửi lại kết quả khi có sóng". Khi kết thúc soát mà máy mất sóng, kết quả phải được gửi về sau, vào lúc không xác định, không có tác nhân, không có thời hạn, sau khi phụ xe đã xong việc. F4.2 mục 15 chỉ cho chờ có hạn giờ trong phiên; F5.4 không có giá trị nào cho việc "hệ thống tiếp tục làm X sau khi use case kết thúc". P02 coi việc gửi lại là bước của UC-015 (CAND-46).
   - Xử lý: luồng 10a một hàng "Lưu kết quả soát vé chưa gửi trên máy soát vé và tự gửi về ... khi máy có sóng trở lại", Quay lại "Tiếp tục bước 11"; hậu điều kiện thành công ghi hai trạng thái (đã gửi hoặc đang lưu để tự gửi). Thời điểm gửi khi có sóng là giả định ASM-35 (Q-46).

6. Trục rẽ nhánh 30 về bên phải decision cắt qua action luồng chính.
   - Vị trí: F10.6 "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action"; C7.3 "cạnh không cắt qua node".
   - Gặp: D-5 có ba luồng (5a, 5b, 5c). Trục cách D-5 30 (x = 730) nằm trong bề ngang A-6 (590-770), nên đoạn dọc xuống 5b, 5c cắt A-6. Không thoả đồng thời.
   - Xử lý: đặt trục ở x = 800 (cách mép phải A-6 là 30). Đề nghị F10.6 đổi thành "cách mép phải của action luồng chính 30".

7. Tác nhân phụ bên phải hệ thống buộc cạnh vượt partition.
   - Vị trí: F10.4 "Thứ tự từ trái sang phải: tác nhân chính, hệ thống, các tác nhân phụ".
   - Gặp: bước 3 (phụ xe) --> bước 4 (đầu quét) đi từ partition trái sang partition phải, vượt qua partition hệ thống; cạnh này cắt cạnh A-3a --> M-5. Không cắt node, nhưng không tránh được giao cạnh.
   - Xử lý: E-08 đi ở y = 610, có Điểm uốn theo F10.5; ghi giao cạnh vào Vấn đề còn mở. Không phải lỗi, chỉ là hệ quả của quy tắc thứ tự partition khi tác nhân phụ nhận luồng trực tiếp từ tác nhân chính.

8. Điều kiện lập bảng dữ liệu vào chưa rõ mức xét.
   - Vị trí: F6 "Chỉ lập khi use case có tác nhân cung cấp thông tin nhiều hơn một mục".
   - Gặp: phụ xe cung cấp hai mục ở hai bước khác nhau (chuyến ở bước 1, mã vé ở bước 4 hoặc 3a), mỗi bước chỉ một mục. Không rõ "nhiều hơn một mục" xét theo cả use case hay theo từng bước.
   - Xử lý: hiểu theo cả use case, lập Dữ liệu vào 1 và Dữ liệu vào 2, mỗi bảng một trường, để có điều kiện hợp lệ cho Target 10.

9. Hậu điều kiện tối thiểu khi use case không có luồng thất bại.
   - Vị trí: F3 "Hậu điều kiện tối thiểu: điều hệ thống bảo đảm cả khi use case kết thúc ở bất kỳ luồng thất bại nào ... nếu không có gì thì ghi 'Không có thay đổi dữ liệu nào được lưu' khi mọi luồng thất bại đều kết thúc trước bước lưu, ngược lại ghi Q-nn".
   - Gặp: mọi luồng thay thế của UC-015 đều quay về luồng chính, không luồng nào kết thúc thất bại. Hai lựa chọn F3 nêu đều không áp dụng; Target 4 vẫn đòi có hàng này.
   - Xử lý: ghi "Use case không có luồng kết thúc thất bại" kèm bảo đảm có căn cứ (lần quét không hợp lệ không đổi trạng thái vé). Đề nghị F3 thêm trường hợp này.

10. Chế độ CO_NHAN: khi nào kèm Q-nn với ASM-nn.
    - Vị trí: Conventions C1 mục 2 (CO_NHAN chỉ đòi ASM-nn); F5.3 "Nguồn không nêu thứ tự ưu tiên thì theo thứ tự xuất hiện trong nguồn và ghi Q-nn" (không phân biệt chế độ); [Action] bước 4 "ghi thành Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)".
    - Gặp: F5.3 đòi Q-nn ở cả hai chế độ, còn bước 4 cho CO_NHAN dùng ASM. Các đặc tả trước kèm cặp Q và ASM ("Chờ Q-nn") cho phần lớn giả định nhưng không phải tất cả.
    - Xử lý: Q-47 (thứ tự lý do không hợp lệ) theo F5.3, không ASM; ASM-33, ASM-35 kèm Q-45, Q-46 vì ảnh hưởng tới UC-014 và thiết kế đồng bộ; ASM-32 không kèm Q; ASM-34, ASM-36 trỏ Q đã có (Q-04, Q-21, Q-30).

11. Phân loại BR từ một REQ nêu gộp.
    - Vị trí: F7.2 (năm loại); F7.3 "Quy tắc: một câu nguyên tử".
    - Gặp: REQ-58 nêu chung "Vé không hợp lệ khi soát nếu vé sai chuyến, vé đã huỷ hoặc vé đã soát". Có thể xem là Ràng buộc (cấm cho lên xe) hoặc Suy luận (từ điều kiện suy ra vé không hợp lệ). Tách thành ba BR để mỗi luồng 5a, 5b, 5c dẫn một mã.
    - Xử lý: BR-20, BR-21, BR-22 loại Suy luận, cùng REQ-58.

12. REQ của use case rộng hơn P02.
    - Vị trí: F1 "REQ | danh sách REQ truy vết"; Mục 3 bảng "các dòng REQ loại Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng, Giao tiếp ngoài về cùng đối tượng nghiệp vụ".
    - Gặp: "cùng đối tượng nghiệp vụ" không có tiêu chí; đặc tả cần REQ-18, REQ-19, REQ-23, REQ-42, REQ-61 mà P02 không ghi cho UC-015 (REQ-19, REQ-61 là loại Chức năng, không thuộc bốn loại bảng Mục 3 cho phép lấy thêm).
    - Xử lý: thêm vào hàng REQ và ghi đề xuất sửa P02, theo cách UC-013 đã làm.

13. Ngữ cảnh.
    - Vị trí: Mục 3, "Khi chạy bằng agent có quyền đọc file, đính kèm đủ file; agent tự lấy phần cần dùng".
    - Gặp: prompt P04 khoảng 68 KB, cộng P00, P02 và ba đặc tả P04 đã có khoảng 200 KB. Agent đọc được, nhưng phần cần dùng của mỗi file chỉ vài dòng. Không ảnh hưởng kết quả.
    - Xử lý: đọc đủ các mục Câu hỏi mở, Giả định của UC-002, UC-008, UC-013 và Mục 8 của UC-008, UC-013 (trạng thái vé đã huỷ liên quan REQ-58).

## Target

| Target | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | Tên UC, tác nhân chép từ P01, P02; không có quan hệ giữa UC |
| 2 | Đạt | |
| 3 | Đạt | Hai tiền điều kiện là trạng thái (ASM-09, ASM-33) |
| 4 | Đạt | Hậu điều kiện tối thiểu xử lý theo vướng mắc 9 |
| 5 | Không đạt một phần | Bước 1 không khớp nguyên văn sự kiện kích hoạt của P02 (vướng mắc 4) |
| 5a | Đạt | Mọi đường đi kết thúc qua bước 11 |
| 6 | Đạt | 11 bước |
| 7 | Đạt | Không có include, extend |
| 8 | Đạt | |
| 9 | Đạt | Bước kiểm tra duy nhất (bước 5) có 5a, 5b, 5c |
| 10 | Đạt | |
| 11 | Đạt | BR-20 đến BR-22 mới, BR-10 dùng lại; sổ 22 dòng, không mất dòng cũ |
| 12 | Đạt | CO_NHAN; nội dung không có trong nguồn đều dẫn ASM-32 đến ASM-36 |
| 12a | Đạt | Số liệu ví dụ ghi phép tính (38 - 2 = 36; 36 - 35 = 1; 80 x 40 = 3.200) |
| 13 | Không đạt một phần | Bước 8 (bước lặp) không có action (vướng mắc 2) |
| 14 | Đạt | P-ACT-05, P-SYS, P-ACT-09 |
| 15 | Đạt | 58 ID khớp giữa bảng và .drawio; kiểm tra tự động: toạ độ bội số của 10, không node chồng, không cạnh cắt node |
| 16 | Đạt | |
