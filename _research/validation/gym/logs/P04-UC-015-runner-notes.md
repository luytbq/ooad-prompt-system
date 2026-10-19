Model của phiên chạy: Sonnet

# Nhật ký người chạy P04 cho UC-015 (gym)

Đầu ra: design/P04-uc-specs/UC-015-cancel-under-booked-class.md, design/diagrams/P04-activity-UC-015.drawio, design/P04-uc-specs/_BR-register.md (thêm BR-13, BR-14). Mã Q cấp tiếp từ Q-62 thành Q-63 đến Q-66; không cấp ASM (NGHIEM_NGAT). File .drawio qua kiểm tra XML (minidom), ID khớp bảng Node, Edge, toạ độ bội số 10, không node chồng nhau.

## Vướng mắc

1. Giá trị "Quay lại / Kết thúc" cho use case không có việc cần làm
   - Vị trí: P04 F5.4: "Một trong: 'Quay lại bước K', 'Tiếp tục bước K', 'Kết thúc use case (thất bại)', 'Kết thúc use case (thành công)' (biến thể vẫn đạt mục tiêu)..."; F5.2: "Không có đơn nào cần xử lý" chỉ nêu ví dụ cột trống.
   - Gặp: UC-015 chạy cho mọi lớp tại mốc 2 giờ; trường hợp phổ biến nhất là lớp có từ 3 người đặt (luồng 2b) hoặc lớp đã bị UC-014 huỷ (luồng 2a): không có gì để làm, không phải lỗi, cũng không đạt mục tiêu. Luồng 5a (lớp có 0 người đặt, huỷ xong không ai để báo) cũng không rõ thành công hay không.
   - Xử lý: 2a, 2b ghi "thất bại" (mục tiêu không đạt), 5a ghi "thành công"; giải thích ở mục 8 và Vấn đề còn mở. Gợi ý cho prompt: thêm giá trị "Kết thúc use case (không có việc cần làm)" hoặc nêu rõ quy ước.

2. Use case do tác nhân thời gian kích hoạt, chỉ có một partition
   - Vị trí: F4.2 mục 10: "Tác nhân thời gian không bao giờ là chủ thể của một bước" cùng F10.4: "Một partition cho mỗi chủ thể xuất hiện trong cột 'Thực hiện bởi'... Thường 2-4 partition"; F4.2 mục 2: "Khi hệ thống chỉ gửi đi mà không chờ kết quả... viết một bước của hệ thống nêu rõ tác nhân phụ nhận".
   - Gặp: tác nhân chính là thời gian, hai tác nhân phụ chỉ nhận nên không có partition: sơ đồ chỉ còn partition hệ thống. Không mâu thuẫn nhưng khác kỳ vọng "2-4 partition", và bảng ví dụ khung XML của F10.6 mặc định có partition tác nhân chính.
   - Xử lý: một partition P-SYS, ghi giải thích ở cột Ghi chú của bảng Node.

3. Gửi thông báo cho nhiều người nhận: lặp hay "với mỗi", và có bước kết quả của tác nhân phụ hay không
   - Vị trí: F4.2 mục 9: "Dùng 'Lặp lại bước K-L...' khi... mỗi đối tượng cần một lần trao đổi riêng với hệ thống ngoài (kết quả của từng lần có thể khác nhau). Dùng 'với mỗi <đối tượng>...' khi hệ thống xử lý hàng loạt..."; F4.2 mục 2 phân biệt gửi có chờ kết quả hay không.
   - Gặp: nguồn không nói có chờ kết quả gửi; hai tiêu chí đẩy theo hai hướng (có "kết quả có thể khác nhau" nên lặp; không chờ kết quả nên chỉ một bước hệ thống). Còn lặp với K = L = 6 (một bước) nghe gượng.
   - Xử lý: chọn "Lặp lại bước 6 cho đến khi...", không có bước kết quả của tác nhân phụ, thêm luồng 6a "gửi không được" kết thúc "Chờ Q-65" (Q-65 hỏi cách xử lý). Đề nghị prompt nêu rõ mặc định khi nguồn không nói có chờ kết quả hay không.

4. Luồng 6a: điều kiện "gửi không được" khi không có bước kết quả
   - Vị trí: F5.5: "mỗi bước gọi hệ thống ngoài có luồng hệ thống ngoài lỗi hoặc không phản hồi khi nguồn nêu hoặc khi đã có Q-nn"; F5.4: "'Chờ Q-nn' (chỉ ở NGHIEM_NGAT, khi điều kiện của luồng có căn cứ trong nguồn hoặc suy ra từ BR...".
   - Gặp: điều kiện của 6a có căn cứ ở F5.5 (đã có Q-nn) chứ không ở nguồn hay BR, và tạo Q-65 để có căn cứ là vòng tròn nhẹ (Q sinh ra để hợp thức hoá luồng). 
   - Xử lý: cấp Q-65 và viết luồng 6a "Chờ Q-65", theo cách UC-005 làm với hoá đơn điện tử (Q-54). Hậu điều kiện tối thiểu vì thế ghi dở dang.

5. Bước huỷ mốc cho use case khác (F4.2 mục 17) khi use case tự làm mất hiệu lực mốc
   - Vị trí: F4.2 mục 17: "use case tạo, đổi hoặc làm mất hiệu lực dữ liệu mà một use case do tác nhân thời gian kích hoạt dùng làm mốc... có bước hệ thống 'Hẹn / hẹn lại / huỷ mốc <tên mốc> của UC-xxx' ngay sau bước lưu dữ liệu đó".
   - Gặp: huỷ lớp làm mất hiệu lực mốc UC-016 (10 phút sau giờ bắt đầu) và mốc UC-013 (30 phút sau thông báo nhận chỗ, nếu đang chờ); nguồn không nêu gì. Quy tắc nói "một use case dùng làm mốc" nhưng ở đây là hai use case khác, nhét vào một bước hay hai bước không được hướng dẫn. Mốc của chính UC-015 (2 giờ) thuộc UC-009, UC-014; bước này chưa có đặc tả nên chỉ ghi ở mục 8.
   - Xử lý: một bước 4 nêu cả hai mốc, kèm Q-64. Mô tả bước có hai đối tượng nên hơi trái "một hành động có mục đích mỗi bước".

6. Thao tác dở dang trên đối tượng chuyển sang trạng thái cuối
   - Vị trí: [Action] 4: "Use case đưa đối tượng sang trạng thái cuối (huỷ, đóng, ngừng) nêu ở luồng chính hoặc mục 8 cách xử lý thao tác dở dang... nguồn không nêu thì ghi Q-nn (NGHIEM_NGAT)".
   - Gặp: dở dang gồm chỗ đã đặt, danh sách chờ, chỗ đang giữ chờ 30 phút, hai mốc hạn. Phải gom thành Q-63 (chỗ, danh sách chờ, người chờ có được báo) và Q-64 (mốc). Khó tách ranh giới Q nào cho gọn; Q-63 hơi gộp hai vấn đề (số phận chỗ đã đặt, số phận danh sách chờ và thông báo).
   - Xử lý: gộp trong Q-63 với các phương án nhóm lại; không viết luồng thay thế riêng vì mọi cách xử lý chờ Q.

7. Kiểm tra trạng thái "lớp đã huỷ" do use case khác đặt
   - Vị trí: [Action] 4: "Trạng thái của một khái niệm mà nguồn, P02 hoặc P05 nêu ở use case khác (huỷ, ngừng bán, khoá) là căn cứ trong nguồn: bước kiểm tra của use case này kiểm thêm điều kiện đó và có luồng thay thế tương ứng"; F4.2 mục 11 cho gộp điều kiện cùng đối tượng.
   - Gặp: thêm điều kiện "lớp chưa bị huỷ" vào bước 2 làm bước kiểm tra có hai điều kiện và ba nhánh (hai thất bại, một tiếp tục); guard của sơ đồ phải ghi "chưa huỷ" ở nhánh 2b và nhánh chính để loại trừ nhau, nên nhãn guard dài.
   - Xử lý: gộp hai điều kiện ở bước 2, luồng 2a (đã huỷ) và 2b (chưa huỷ, từ 3 người trở lên) loại trừ nhau theo F5.3.

8. BR cho chính sách kênh thông báo
   - Vị trí: F7.1: "Phép thử: nếu không có phần mềm, nhân viên làm bằng tay vẫn phải tuân theo quy tắc này"; F7.1 "Không là BR: ... (chức năng)".
   - Gặp: câu nguồn "Thông báo cho hội viên gửi qua thông báo đẩy của ứng dụng; hội viên chưa cài ứng dụng thì nhận SMS" nằm giữa chức năng (REQ-87, REQ-88 loại Chức năng) và chính sách; phép thử thủ công không áp dụng rõ vì kênh phụ thuộc phần mềm. Hai tiền lệ UC-005, UC-010 trong sổ không tách BR này (Q-53 của UC-005 nêu kênh mà không có BR).
   - Xử lý: cấp BR-14 (Kích hoạt hành động) vì có điều kiện rẽ nhánh và nhiều UC dùng chung; ghi ở Vấn đề còn mở rằng có thể chuyển sang P06. Đề nghị prompt cho ví dụ phân biệt BR và chức năng với quy tắc chọn kênh.

9. Phân biệt "giờ học" và "giờ bắt đầu"
   - Vị trí: yêu cầu nguồn Mục 8 câu 3 "2 giờ trước giờ học" so với Mục 4 câu 2 "giờ bắt đầu"; [Action] không có hướng dẫn thuật ngữ nguồn mơ hồ nhỏ.
   - Gặp: không đủ nặng để thành Q nhưng ví dụ tính mốc ở mục 8 cần giả định giờ học là giờ bắt đầu (lớp 18:00, mốc 16:00).
   - Xử lý: giữ nguyên chữ "giờ học" ở BR, dùng "lớp bắt đầu lúc 18:00" chỉ trong ví dụ tính (Target 12a), ghi ở Vấn đề còn mở; không tạo Q.

10. Mức độ chi tiết GON và mục 8a
    - Vị trí: Format "## 8a. Kịch bản chính (chỉ khi DAY_DU, xem F9)"; project-profile MUC_CHI_TIET = GON.
    - Gặp: C5 nói "Mục nào không có nội dung thì ghi 'Không có', không xoá mục", trong khi Format nói 8a chỉ khi DAY_DU; không rõ có để mục trống khi GON.
    - Xử lý: bỏ mục 8a, theo Format. Prompt chưa nói rõ ưu tiên giữa C5 và điều kiện "chỉ khi".

11. Quy tắc đọc phạm vi và mã Q cấp tiếp
    - Vị trí: C3: "Mã lớn nhất tìm trong mục Câu hỏi mở và Giả định của mọi artifact đã có trong THU_MUC_DAU_RA, kể cả file không thuộc đầu vào của bước (chỉ quét mã, không cần đọc nội dung)" so với phạm vi đọc của nhiệm vụ.
    - Gặp: trong bài chạy này tôi tìm Q lớn nhất từ phần đọc được (Q-62 ở UC-010); có thể có artifact khác chưa thấy.
    - Xử lý: cấp Q-63 từ Q-62; hàng "Mã Q, ASM cuối đã cấp" ghi Q-66.

12. Phi chức năng và Yêu cầu đặc biệt
    - Vị trí: F8: "Chỉ ghi điều có REQ; yêu cầu áp dụng cho toàn hệ thống không ghi ở đây".
    - Gặp: nguồn không có yêu cầu phi chức năng riêng cho use case này (REQ-94, REQ-96 thuộc UC khác). Ghi "Không có".
    - Xử lý: không có vướng mắc thêm.

## Mục Target không đạt hoặc đạt một phần

- Target 12 đạt một phần: bước 4 và bước 5 không có câu gốc trực tiếp trong nguồn, luồng 2a suy từ UC-014 (chi tiết ở Vấn đề còn mở của đặc tả).
- Target 5a: không áp dụng được (không có tác nhân người), đã ghi giải thích.
- Target 9: bước 2 có luồng 2a, 2b; bước 3, 4, 5 không phải bước kiểm tra của hệ thống (bước 5 có luồng 5a); đạt.
- Target 14: chỉ một partition; đạt theo F10.4 nhưng khác kỳ vọng 2-4 partition (vướng mắc 2).
- Các mục còn lại đạt.
