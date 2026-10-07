# Nhật ký người chạy - P04 UC-013 Huỷ chuyến

Model: mặc định của phiên điều phối (Claude Opus 5.5, claude-opus-5-5).

Tham số: UC_ID = UC-013; TEN_HE_THONG_TRONG_LUONG = Không có (dùng "Hệ thống"); YEU_CAU_BO_SUNG = Không có. Chế độ CO_NHAN, MUC_CHI_TIET = DAY_DU.

Đầu ra: design/P04-uc-specs/UC-013-cancel-trip.md; design/P04-uc-specs/_BR-register.md (thêm BR-17 đến BR-19, thêm UC-013 vào BR-10, BR-15, BR-16); design/diagrams/P04-activity-UC-013.drawio (XML hợp lệ, 32 node, 32 cạnh, không node chồng nhau, không cạnh cắt qua node theo kiểm tra tự động).

Mã đã cấp: Q-40 đến Q-44 (5), ASM-24 đến ASM-31 (8), BR-17 đến BR-19 (3 mới), dùng lại BR-10, BR-15, BR-16; dùng lại ASM-09, ASM-20, ASM-22 của artifact trước.

## Vướng mắc

### 1. Bước lặp và ánh xạ 1-1 bước - action mâu thuẫn nhau

- Vị trí: F4.2 mục 9 "Lặp lại: viết bằng một bước "Lặp lại bước 3-4 cho đến khi <điều kiện>" hoặc "với mỗi <đối tượng>, <hành động>"." và F10.2 "Mỗi bước luồng chính N --> đúng một action có ID "A-N"", F10.2 "Luồng lặp --> decision sau bước cuối của vòng lặp với guard [còn <đối tượng>]".
- Gặp gì: UC-013 phải hoàn tiền và gửi SMS cho từng vé của chuyến, có tác nhân phụ (Cổng thanh toán) trả kết quả cho từng vé. Viết dạng "Lặp lại bước 7-9" thì bước lặp là một bước luồng chính nhưng trên sơ đồ là decision, không có action A-N tương ứng, vi phạm ánh xạ 1-1 và Target 13. Prompt không nói bước "Lặp lại" có action hay không.
- Xử lý: dùng dạng "với từng vé" trong các bước 6 đến 10 (vế thứ hai của F4.2 mục 9), không vẽ vòng lặp. Ghi vào Vấn đề còn mở của đặc tả.

### 2. Không có hướng dẫn cho kết quả từng phần của thao tác hàng loạt với hệ thống ngoài

- Vị trí: F5.3 "Điều kiện của các luồng cùng bước phải loại trừ lẫn nhau"; F5.4 chỉ cho "Kết thúc use case (thành công)" hoặc "(thất bại)", "Quay lại", "Tiếp tục".
- Gặp gì: Cổng thanh toán có thể hoàn thành công cho một số vé và thất bại cho vé khác. Chuyến đã huỷ ở bước 5 nên không thể kết thúc thất bại hay quay lại; mục tiêu chỉ đạt một phần. Prompt không có loại kết cục "thành công một phần", cũng không nói điều kiện luồng viết thế nào khi kết quả là tập hợp.
- Xử lý: luồng 8a điều kiện "ít nhất một vé không thành công", ghi nhận khoản hoàn chưa thành công rồi "Tiếp tục bước 9"; hậu điều kiện thành công nêu cả trạng thái chưa thành công (ASM-31).

### 3. Hậu điều kiện tối thiểu chỉ có hai khuôn

- Vị trí: F3 "nếu không có gì thì ghi "Không có thay đổi dữ liệu nào được lưu" khi mọi luồng thất bại đều kết thúc trước bước lưu, ngược lại ghi Q-nn".
- Gặp gì: mọi luồng kết thúc thất bại đều trước bước 5 nên khuôn thứ nhất áp được, nhưng luồng 8a (lỗi sau bước lưu) không phải luồng kết thúc thất bại nên không thuộc khuôn nào. Không rõ hậu điều kiện tối thiểu có cần nói về lỗi sau bước lưu không.
- Xử lý: hậu điều kiện tối thiểu chỉ nói về các luồng kết thúc thất bại; trạng thái sau 8a đặt ở hậu điều kiện thành công.

### 4. Bước phát sinh của luồng thay thế khi điều kiện biết sớm hơn điểm tách nhánh

- Vị trí: F5.2 "N là bước mà tại đó điều kiện được phát hiện (thường là bước kiểm tra của hệ thống, hoặc bước tác nhân chọn khác đi)".
- Gặp gì: "chuyến không có vé" và "không có vé mua trực tuyến" đã biết ở bước 3 (hệ thống hiển thị số vé), nhưng nhánh phải tách sau bước 5 (chuyến vẫn phải huỷ) và sau bước 6. Đánh số theo bước phát hiện (3a) thì nhánh bỏ qua bước huỷ chuyến, sai nghĩa.
- Xử lý: đánh số theo bước tách nhánh (5a, 6a), ghi lý do vào Vấn đề còn mở.

### 5. Điểm uốn bắt buộc cho cạnh vượt partition mâu thuẫn với "-" cho cạnh thẳng

- Vị trí: F10.5 "bắt buộc điền cho cạnh quay lại (tới merge node M-K) và cạnh vượt qua partition khác"; Conventions C7.1 "cạnh đi thẳng hoặc để draw.io tự định tuyến ghi "-"".
- Gặp gì: E-14 (D-4 --> A-4a) đi thẳng ngang từ partition tác nhân sang partition hệ thống.
- Xử lý: ghi một điểm nằm trên đường thẳng tại ranh giới partition (320,760) để thoả cả hai quy tắc. Prompt nên nói rõ cạnh thẳng vượt partition ghi gì.

### 6. Trục rẽ nhánh "cách decision 30 về bên phải" cắt qua action luồng chính

- Vị trí: F10.6 "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action".
- Gặp gì: D-2 rộng 40, action luồng chính A-3 rộng 180 cùng trục, nên trục cách mép phải decision 30 nằm trong bề ngang A-3; cạnh E-06, E-07 sẽ cắt qua A-3, trái C7.3.
- Xử lý: đặt trục ở x = 600 tuyệt đối (cách mép phải action luồng chính 30). Cùng vướng mắc đã gặp ở UC-002, UC-008 (đọc từ Vấn đề còn mở của hai đặc tả này), chưa được sửa trong prompt.

### 7. Dùng lại mã BR khi việc áp dụng cho use case này dựa trên giả định

- Vị trí: F7.4 mục 2 "Cùng nghĩa (cùng đối tượng, cùng ngưỡng, cùng điều kiện) thì dùng lại mã cũ, thêm UC_ID vào cột "UC áp dụng" của sổ".
- Gặp gì: BR-15, BR-16 (kênh hoàn theo kênh mua) có nội dung chung, nhưng nguồn chỉ nêu chúng trong bối cảnh trả vé (Mục 5); áp dụng cho huỷ chuyến phụ thuộc Q-14 (ASM-28). Prompt không nói ghi điều kiện áp dụng ở đâu trong sổ, sổ không có cột ghi chú.
- Xử lý: dùng lại mã, ghi "UC-013 (ASM-28)" trong cột UC áp dụng; nêu trong Vấn đề còn mở cách gỡ nếu Q-14 trả lời "Không".

### 8. Ranh giới BR và chức năng với quy tắc kích hoạt hành động

- Vị trí: F7.1 "Không là BR: ... "Bạn đọc có thể gia hạn" (chức năng)"; F7.2 loại "Kích hoạt hành động (action enabler, khi điều kiện đúng thì phải làm gì)".
- Gặp gì: REQ-48 (gửi SMS khi huỷ chuyến), REQ-49 (hoàn tiền khi huỷ chuyến) được P00 xếp loại Chức năng, nhưng có dạng "khi điều kiện đúng thì phải làm gì". Prompt không nói REQ loại Chức năng có được tách thành BR kích hoạt hành động không.
- Xử lý: tách BR-18, BR-19 theo tiền lệ BR-09 (từ REQ-17, cũng là REQ Chức năng) và phép thử F7.1; ghi lý do vào Vấn đề còn mở.

### 9. "Cùng đối tượng nghiệp vụ" trong bảng phần cần dùng của P00 mơ hồ

- Vị trí: mục 3 bảng "Phần cần dùng", dòng P00: "các dòng REQ loại Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng, Giao tiếp ngoài về cùng đối tượng nghiệp vụ"; Action 1c.
- Gặp gì: đối tượng của UC-013 là chuyến, vé, khoản hoàn, tin nhắn. Phải tự quyết REQ-34, REQ-36 (kênh hoàn), REQ-09 (số điện thoại người đi), REQ-42 (chuyến), REQ-25 (đặt chỗ qua điện thoại), REQ-58 (vé đã huỷ khi soát) có thuộc phạm vi không. Hàng REQ của F1 vì vậy dài hơn cột REQ của P02, mà prompt không nói khi đó có bắt buộc ghi đề xuất sửa P02 không.
- Xử lý: đưa sáu REQ này vào hàng REQ và ghi đề xuất sửa P02 (theo cách UC-008 đã làm).

### 10. Đề xuất sửa đặc tả P04 của use case khác

- Vị trí: Conventions C1.3 "Nếu phát hiện bước trước sai ... ghi vào mục "Đề xuất sửa artifact trước""; F7.4 mục 4 chỉ nêu "bước P04 hoặc P06" cho BR.
- Gặp gì: huỷ chuyến làm UC-002 thiếu luồng (lần đặt đang giữ chỗ khi chuyến bị huỷ, Q-44). UC-002 là cùng bước P04, không phải "bước trước"; prompt không nói chỗ ghi phát hiện về use case khác cùng bước.
- Xử lý: ghi vào "Đề xuất sửa artifact trước" với cột Bước "P04 (UC-002)".

### 11. Phạm vi tìm mã Q, ASM lớn nhất chưa thống nhất

- Vị trí: Action 1e "Tìm mã Q và ASM lớn nhất trong P00 đến P03 và trong mọi đặc tả P04 đã có"; Conventions C3 "đọc các artifact đầu vào đã có".
- Gặp gì: P02R-review.md cũng cấp Q (Q-30) nhưng không thuộc đầu vào của P04, và "P00 đến P03" không rõ có gồm P02R không. Lần này không ảnh hưởng (mã lớn nhất là Q-39 ở UC-008, ASM-23 ở UC-008), nhưng có thể trùng mã nếu P02R cấp mã lớn hơn mà P02 không chép lại.
- Xử lý: cấp tiếp từ Q-40, ASM-24 sau khi rà P00, P01, P02, P03 và hai đặc tả P04.

### 12. Chế độ CO_NHAN: chưa rõ giả định có cần kèm câu hỏi mở không

- Vị trí: Conventions C1.2 CO_NHAN "được phép giả định khi nguồn thiếu, nhưng mỗi giả định phải có mã ASM-nn"; Action 4 "ghi thành Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)".
- Gặp gì: các artifact trước luôn ghép ASM với "Chờ Q-nn", nhưng quy tắc không đòi. Không rõ khi nào cần cả hai.
- Xử lý: ghép Q với ASM khi câu trả lời có thể đổi luồng hoặc dữ liệu (ASM-24, 26 đến 31); ASM-25 (bước xác nhận) không kèm Q, theo cách ASM-19 của UC-008.

### 13. Dữ liệu ra cho nội dung gửi tới hệ thống ngoài

- Vị trí: F6 "Chỉ lập khi ... hệ thống trả về danh sách hoặc bộ thông tin có cấu trúc"; F6.2 cột "Định dạng hiển thị".
- Gặp gì: nội dung tin nhắn SMS gửi tới người đi qua Cổng SMS là bộ thông tin có cấu trúc, nhưng không "hiển thị" cho tác nhân trong use case. Không rõ có lập bảng Dữ liệu ra cho nó không.
- Xử lý: lập Dữ liệu ra 2 (bước 10) cho nội dung tin nhắn, cột Định dạng hiển thị ghi định dạng giá trị trong tin.

### 14. Quá tải ngữ cảnh

- Vị trí: mục 2 và mục 3 (đính kèm đủ P00, P01, P02, P03, sổ BR, các đặc tả P04 đã có).
- Gặp gì: prompt khoảng 66 KB, Conventions khoảng 30 KB, P00 khoảng 50 KB, P02 khoảng 56 KB, mỗi đặc tả P04 khoảng 30 KB. Phải đọc cả P00 để tìm Q liên quan và mã lớn nhất. Agent đọc đủ được nhưng chạy bằng chat sẽ vượt giới hạn khi số đặc tả P04 tăng.
- Xử lý: đọc theo bảng "Phần cần dùng"; với đặc tả P04 đã có chỉ đọc Câu hỏi mở, Giả định, và mục liên quan của UC-008 (BR-15, BR-16, trạng thái vé đã huỷ).

## Target

Tự kiểm tra 16 mục Target (kể cả 5a, 12a): tất cả Đạt. Các điểm cần lưu ý:

- Target 5: bước cuối (11) là hiển thị kết quả; mục tiêu (chuyến huỷ, hoàn tiền, báo SMS) đạt ở bước 5 đến 10, bước 11 báo kết quả cho nhân viên điều hành theo Target 5a.
- Target 7: UC-013 không có quan hệ include, extend, generalization; mục này không áp dụng.
- Target 13: đạt nhờ cách xử lý ở vướng mắc 1 (không có bước "Lặp lại").
- Target 15: kiểm tra tự động trên bảng Node, Edge: ID khớp file .drawio, toạ độ bội số của 10, không node chồng nhau, không đoạn cạnh nào cắt qua node; XML parse được bằng xml.dom.minidom. Bố cục chưa mở bằng draw.io để xem bằng mắt.
