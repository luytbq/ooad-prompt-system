# P05 - Nhật ký người chạy

Model: mặc định của phiên điều phối (Claude Opus 5.5, claude-opus-5-5).

Bước: P05 Từ điển thuật ngữ. Placeholder: NGUON_THUAT_NGU_CHUAN = Không có; YEU_CAU_BO_SUNG = Không có. Chế độ CO_NHAN. Lần chạy đầu, chưa có P05 cũ.

Kết quả: 41 thuật ngữ (GL-01 đến GL-41), 41 dòng ứng viên không đưa vào, 3 câu hỏi mới (Q-48 đến Q-50), 1 giả định mới (ASM-37), 9 dòng đề xuất sửa artifact trước. Không có sơ đồ.

## Vướng mắc

1. Một từ trùng tên tác nhân nhưng mang nghĩa khác
   - Vị trí: F4, câu "Vai trò đã có tên tác nhân ở P01 thì tên tác nhân là thuật ngữ chính thức của vai trò đó"; Action bước 4 "Một từ mang hai nghĩa khác nhau trong nguồn thì tách thành hai thuật ngữ có tên phân biệt".
   - Gặp gì: nguồn dùng "hành khách" vừa cho người đặt vé trên website (ACT-01) vừa cho người lên xe, người có vé ("khi hành khách lên xe", "mọi hành khách đã có vé", "danh sách hành khách"). F4 chỉ nói cách gọi khác của cùng vai trò, không nói trường hợp chính tên tác nhân bị nguồn dùng cho một khái niệm khác. Không có chỗ quy định từ trùng tên một thuật ngữ khác có được ghi vào cột "Từ đồng nghĩa không dùng" hay không.
   - Xử lý: tách GL-12 Hành khách (ACT-01) và GL-26 Người đi; ghi "hành khách (nghĩa người lên xe, người có vé)" vào cột đồng nghĩa không dùng của GL-26 và của GL-12, kèm giải thích. Giữ tên GL-05 Danh sách hành khách của chuyến theo nguồn và tên UC-014 dù "hành khách" ở đây nghĩa là người đi; ghi rõ ở Ghi chú. Tạo đề xuất sửa P01, P02, P04 cho các chỗ dùng sai nghĩa.

2. Từ đa nghĩa "giá vé" và việc đổi tên use case
   - Vị trí: F4 thứ tự ưu tiên mục 3 "Cách gọi xuất hiện nhiều nhất trong tài liệu nguồn"; F4 đoạn "Chỉ ghi đề xuất đổi tên use case (bước 7) khi danh từ trong tên use case chỉ một khái niệm khác với thuật ngữ chính thức".
   - Gặp gì: "giá vé" vừa là mức đặt theo tuyến và loại xe (Mục 7, BR-04, UC-016) vừa là giá một vé đã cộng mức tăng giá lễ Tết, dùng để tính hoàn (Mục 5, Mục 6, BR-13, BR-14, BR-17, các bảng dữ liệu P04). Áp mục 3 cho nghĩa thứ hai giữ "giá vé"; nghĩa thứ nhất phải đặt tên khác, dẫn tới quy tắc F4 bắt đề xuất đổi tên UC-016 Đặt giá vé. Prompt không cân nhắc chi phí đổi tên use case đã chốt so với chọn tên khác cho thuật ngữ; mục 5 của F4 ("tránh phải đổi artifact trước") đứng sau mục 3 nên không cứu được.
   - Xử lý: GL-08 Giá vé (giá một vé), GL-09 Giá vé theo tuyến và loại xe (tên lấy từ BR-05); đề xuất đổi tên UC-016 và sửa REQ-51, REQ-52, BR-04, tiền điều kiện UC-002.

3. Cách gọi tắt của cùng thuật ngữ
   - Vị trí: F3 cột Từ đồng nghĩa không dùng "Chỉ ghi từ thực sự xuất hiện hoặc dễ gây nhầm trong bối cảnh dự án"; Target 7 "Mọi chỗ artifact trước dùng từ đồng nghĩa không chính thức đã được ghi".
   - Gặp gì: F4 mục 4 chọn "Máy soát vé cầm tay" (cụ thể hơn), nhưng P02, P04 dùng "máy soát vé" hàng chục lần; tương tự "quầy", "khoản hoàn", "tin nhắn". Nếu coi là đồng nghĩa không dùng thì Target 7 buộc liệt kê hàng chục đề xuất vô nghĩa. Prompt không có khái niệm "cách gọi tắt được chấp nhận".
   - Xử lý: coi cách gọi tắt rõ nghĩa là chấp nhận được, chỉ ghi cách gọi gây nhầm ("máy" đứng riêng). Ghi chính sách này vào Vấn đề còn mở. Target 7 tính Đạt theo cách hiểu này.

4. Quy tắc chưa có mã BR
   - Vị trí: F3 quy tắc định nghĩa 6 "quy tắc thuộc BR, dẫn mã ở Ghi chú"; Target 4 "quy tắc dẫn mã BR ở Ghi chú".
   - Gặp gì: sổ BR mới phủ bốn use case đã đặc tả, nên các quy tắc REQ-27 (60 phút), REQ-43, REQ-44, REQ-45 (chồng chuyến, 10 giờ lái), REQ-54 (30%), REQ-62 (15 phút) chưa có mã BR để dẫn. Prompt giả định mọi quy tắc đã có mã BR khi chạy P05, trong khi README cho P05 và P06 chạy song song và P06 mới cấp BR từ REQ còn lại.
   - Xử lý: dẫn mã REQ kèm "chưa có mã BR", ghi vào Vấn đề còn mở.

5. P05 chạy khi mới có 4 trong 18 đặc tả P04
   - Vị trí: mục 1 "Bước chạy một lần sau khi đã có đặc tả use case"; Action bước 2 thu thập từ P04; Target 2 chỉ xét khái niệm "dùng trong đặc tả P04".
   - Gặp gì: các khái niệm của UC chưa đặc tả (lịch chạy, tài xế, xe, thời gian chạy, phần chênh lệch, lịch sử vé, doanh thu, tỉ lệ lấp đầy) chỉ có REQ và mô tả P02. Target 2 đạt dễ dàng vì chỉ đo phần đã đặc tả, nên không phát hiện bỏ sót ở phần còn lại.
   - Xử lý: vẫn đưa các khái niệm này vào từ REQ và P02, ghi Vấn đề còn mở đề nghị chạy lại sau khi đủ đặc tả.

6. Tiêu chí "từ phổ thông" xung đột với vai trò nguồn đặt tên entity
   - Vị trí: F2 "Không đưa vào: Từ phổ thông dùng đúng nghĩa thông thường"; mục 1 "là nguồn đặt tên cho lớp entity, thuộc tính, bảng dữ liệu".
   - Gặp gì: "Tài xế", "Xe" là từ phổ thông nhưng là entity cốt lõi của lập lịch (REQ-42 đến REQ-45). Loại đi thì bước sau tự dịch tên lớp, trái mục đích; đưa vào thì có thể bị coi vi phạm Target 3.
   - Xử lý: đưa vào với lý do F2 b (nghĩa hẹp: xe, tài xế được xếp vào chuyến trong lịch chạy). Target 3 tính Đạt, nhưng đây là phán đoán.

7. Thứ tự chữ cái không xác định
   - Vị trí: Action bước 8 "Sắp xếp thuật ngữ theo thứ tự chữ cái của cột Thuật ngữ"; Target 10.
   - Gặp gì: với tiếng Việt, thứ tự bảng chữ cái (đ sau d, ơ sau ô) khác thứ tự mã Unicode mà công cụ sắp xếp thường dùng; "Đặt chỗ" đứng trước hay sau "Doanh thu" tuỳ cách hiểu. Prompt không nói.
   - Xử lý: dùng thứ tự bảng chữ cái tiếng Việt, ghi vào Vấn đề còn mở.

8. Cột của mục "Đề xuất sửa artifact trước"
   - Vị trí: Action bước 7 "(bước, mã phần tử, từ đang dùng, thuật ngữ chính thức)" so với Conventions C5 "| Bước | Mã phần tử | Vấn đề | Đề nghị |".
   - Gặp gì: hai bộ cột khác nhau, không rõ dùng bộ nào.
   - Xử lý: giữ bốn cột C5, ghi "Từ đang dùng" trong cột Vấn đề và thuật ngữ chính thức trong cột Đề nghị.

9. Cấp mã Q, ASM và phạm vi đọc P02
   - Vị trí: Conventions C3 "Lần chạy nào cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất đã thấy"; prompt mục 2 "với P02 chỉ cần Mục 4 (bảng use case) và Mục 5".
   - Gặp gì: Mục 4 của P02 trích Q-30, ASM-08 đến ASM-11 mà không có nội dung (nằm ở mục Câu hỏi mở, Giả định của P02 và P03, ngoài phần được đọc). Để tìm mã lớn nhất phải quét cả file P02. Ngoài ra một phiên P06 đang chạy song song cũng cấp Q, ASM từ cùng mốc Q-47, ASM-36, nên Q-48 đến Q-50 và ASM-37 có nguy cơ trùng mã. Conventions không có cơ chế cho hai bước chạy song song (README lại khuyến khích chạy P05, P06 cùng lúc).
   - Xử lý: chỉ quét mã (grep) trên P02, không đọc nội dung ngoài Mục 4, Mục 5; cấp tiếp từ Q-48, ASM-37. Q-30 được trích theo ngữ cảnh mà P04 đã dùng (mã vé sau khi đổi). Người hợp nhất cần kiểm tra trùng mã với P06.

10. Định nghĩa thiếu nguồn ở chế độ CO_NHAN
    - Vị trí: Action bước 5 "Chỗ nguồn không đủ để định nghĩa thì ghi định nghĩa phần đã biết và tạo Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)".
    - Gặp gì: câu này đọc như ở CO_NHAN chỉ tạo ASM, nhưng các bước trước của dự án luôn ghép ASM với một Q "Chờ Q-nn". Với các chỗ chỉ cần ghi "phần đã biết" mà không phải điền nội dung (doanh thu theo ngày nào, điểm đi có phải bến xe không), không rõ có buộc tạo ASM không.
    - Xử lý: tỉ lệ lấp đầy cần cách tính cho Ghi chú nên tạo Q-48 kèm ASM-37; Q-49, Q-50 chỉ tạo câu hỏi vì định nghĩa không điền nội dung giả định. Doanh thu trước hay sau hoàn dùng Q-23 có sẵn, không tạo ASM.

11. Khái niệm "trạng thái" và "giá trị" lấn sang thuộc tính
    - Vị trí: F2 c (trạng thái là thuật ngữ) và F2 lỗi "quá nhỏ" (thuộc tính lẻ ghi trong Ghi chú của thuật ngữ cha).
    - Gặp gì: "Vé còn hiệu lực", "Vé đã huỷ", "Vé đã soát", "Vé mua trực tuyến" đều là trạng thái hoặc giá trị của Vé; prompt không có tiêu chí khi nào trạng thái thành thuật ngữ riêng, khi nào ghi trong Ghi chú.
    - Xử lý: tách thành thuật ngữ riêng khi nguồn hoặc BR dùng nó như một khái niệm có quy tắc riêng (vé còn hiệu lực ở BR-18, BR-19; vé đã huỷ ở REQ-58, BR-21); còn lại ghi Ghi chú và bảng ứng viên không đưa vào.

12. Phát hiện ngoài phạm vi thuật ngữ
    - Vị trí: Action bước 7 chỉ yêu cầu tìm từ đồng nghĩa và dùng sai nghĩa.
    - Gặp gì: khi viết định nghĩa GL-03 Chỗ còn trống, thấy BR-03 không loại trừ chỗ của đặt chỗ qua điện thoại chưa thanh toán (ASM-05). Đây là mâu thuẫn nội dung, không phải từ đồng nghĩa.
    - Xử lý: ghi vào Đề xuất sửa artifact trước theo C1.3.

## Target

| Target | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | Mọi GL có ít nhất một mã REQ |
| 2 | Đạt | Chỉ đo được trên 4 đặc tả đã có (vướng mắc 5) |
| 3 | Đạt | Phán đoán với Tài xế, Xe, SMS (vướng mắc 6) |
| 4 | Đạt | Quy tắc chưa có mã BR dẫn mã REQ (vướng mắc 4) |
| 5 | Đạt | Tách Hành khách / Người đi, Giá vé / Giá vé theo tuyến và loại xe |
| 6 | Đạt | 41 tên tiếng Anh, không trùng; đã tránh trùng tên tiếng Anh của tác nhân (Passenger dùng cho ACT-01 nên người đi là Traveler) |
| 7 | Đạt | Theo cách hiểu cách gọi tắt được chấp nhận (vướng mắc 3) |
| 8 | Không áp dụng | Chế độ CO_NHAN |
| 9 | Không áp dụng | Lần chạy đầu |
| 10 | Đạt | Thứ tự chữ cái tiếng Việt (vướng mắc 7) |
