Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy P13 - Mô hình hoá dữ liệu (bus-r2)

Tham số bước: BUOC = P13; LOAI_CSDL, QUY_UOC_CSDL, KHOI_LUONG_DU_LIEU, SINH_DDL = "Không có"; YEU_CAU_BO_SUNG = giới hạn phạm vi vào lớp persistent của PKG-27 và PKG-28. Đầu ra: design/P13-data-model.md, design/diagrams/P13-erd-logical.drawio, design/diagrams/P13-erd-conceptual.drawio (MUC_CHI_TIET = DAY_DU nên có cả ER khái niệm). Kết quả: 5 thực thể, 6 bảng, 7 ER, 9 ràng buộc liên bảng, 9 dòng index, 9 ràng buộc CHECK nhiều cột. Q, ASM cuối: Q-74, ASM-56 (không cấp mới).

## Phạm vi đã đọc

Đã đọc: P13-data-modeling.md, 00-Conventions.md, README.md, project-profile.md, yeu-cau-xe-khach.md, P12 (các phần nêu dưới), P06 (cả file), P04 UC-009 và UC-017 (mục 2 đến 8, Câu hỏi mở, Giả định), P09 (F1, F2.2, F5, F7, F11, Câu hỏi mở, Giả định), P05 (bảng thuật ngữ). Không đọc nhật ký của bước khác, không đọc _research ngoài runner-template.md.

Hai lần đọc vượt phần mục 2 của P13 cho phép, cần ghi lại để người đánh giá biết: (1) đọc P12 từ dòng 759 tới hết file để lấy Câu hỏi mở, Giả định, nên đã thấy F9 và F10 (mục 2 ghi "không cần F4, F8, F10") và dòng đầu F8; không dùng nội dung đó. (2) Mở đầu tệp P12-class-PKG-27.drawio vài trăm ký tự để xem kiểu style swimlane; không dùng thông tin nào ngoài kiểu style đã có sẵn ở C7.

## Vướng mắc

### 1. Mục 2: P12 "F7a" không tồn tại

Vị trí: mục 2, hàng P12-class-design: "Phần cần đọc: F1 (cột Persistent), F1b, F5 (quan hệ), F6 (state machine), F7, F7a, Câu hỏi mở, Giả định".
Gặp phải: file P12 của đề này có F1, F1b, F2 đến F10 nhưng không có F7a. Có thể F7a là bản cũ của F1b hoặc mục chưa tồn tại.
Xử lý: bỏ qua F7a, ghi trong khối "Đầu vào đã dùng" rằng P12 không có F7a.

### 2. Mâu thuẫn giữa phần đọc được phép và yêu cầu đối chiếu F3

Vị trí: mục 2 liệt kê phần P12 cần đọc (không có F3, F2); F4.4: "Mỗi ràng buộc phải có nguồn và được đối chiếu với thiết kế method ở P12 F3 của mọi operation ghi các cột liên quan".
Gặp phải: không thể vừa đọc đúng danh sách ở mục 2 vừa đối chiếu thân method ở F3. Các ràng buộc liên bảng C-03, C-04, C-08 phụ thuộc vào ranh giới giao dịch nằm ở F3.
Xử lý: đối chiếu theo cột "Operation tương ứng" của P12 F6 và Vấn đề còn mở của P12; ghi rõ ở F4.4 và Vấn đề còn mở rằng Target 8 chưa đạt phần đối chiếu F3. Đề nghị thêm F3 vào danh sách phần cần đọc ở mục 2 hoặc bỏ yêu cầu đối chiếu ở F4.4.

### 3. Mục 2 không nêu mục cần đọc của P06, P04, P09

Vị trí: mục 2, các hàng P06, P04, P09 chỉ ghi tên file, không như hàng P12 (có danh sách phần cần đọc).
Gặp phải: P06 nhỏ nên đọc cả file; P04 chỉ đọc mục 5, 6, 8 và Câu hỏi mở; với P09 phải tự đoán mục chứa "Cơ chế lưu trữ đã chọn, phân tán dữ liệu" (chọn F7, F2.2, F11 và F1 dòng 9). Không có hướng dẫn rõ nên có nguy cơ đọc thiếu hoặc thừa.
Xử lý: tự chọn như trên; hệ quả là chưa chắc không bỏ sót ràng buộc dữ liệu nằm ở P09 F6 hoặc F10.

### 4. F2: không có giá trị Chiến lược cho enumeration

Vị trí: F2, "Chiến lược: 'Một lớp - một bảng'; 'Nhúng vào TBL-nn' ...; 'Bảng thuộc tính đa trị TBL-nn'" và Bước 1 "Enumeration thành miền giá trị của thuộc tính".
Gặp phải: P12 F1b có 12 enumeration và 10 exception, F1 có control, interface, value object; danh sách chiến lược không có giá trị cho enumeration thành CHECK, và cột TBL phải điền gì cho lớp Không.
Xử lý: ghi Chiến lược "Miền giá trị (CHECK) của TBL-nn.cột", cột TBL ghi "-". Gom 10 exception và 3 value object hiển thị vào hàng chung. Đề nghị thêm giá trị này vào danh sách chiến lược.

### 5. F2 và Bước 0: bảng trung gian của quan hệ không có DC và quy tắc cấp mã TBL

Vị trí: F2 "TBL-nn cấp theo thứ tự xuất hiện ở F2"; F2 cột DC.
Gặp phải: bảng trung gian booking_seat (R-10) không ứng với lớp P12 nào, nhưng F2 chỉ có dòng theo DC. Thứ tự "xuất hiện" khi bảng này sinh ở F4.2 chứ không ở F2 là không rõ.
Xử lý: thêm một dòng F2 với cột DC ghi "R-10 (DC-Booking - DC-Seat)", Persistent ghi "Có (bảng trung gian của quan hệ)", cấp TBL-06 sau các bảng thực thể.

### 6. F4.2: câu về khoá ngoại trỏ khoá ứng viên nhiều cột khó hiểu

Vị trí: F4.2: "FK được trỏ khoá ứng viên nhiều cột (UNIQUE) khi trỏ khoá thay thế sẽ tạo phụ thuộc bắc cầu." và câu kế "Một FK ghép thể hiện nhiều R-nn: một cạnh ERD, ghi mọi R-nn ở Ghi chú của cạnh và ở F4.2".
Gặp phải: câu thứ nhất thiếu chủ ngữ rõ ràng, không biết là cảnh báo (không nên làm) hay mô tả hệ quả (được phép nhưng phải khai báo). Đề này có đúng tình huống: ticket giữ cả seat_id lẫn trip_id (P12 có R-19 và R-22), cần khoá ngoại ghép (seat_id, trip_id) trỏ UNIQUE (id, trip_id) của seat.
Xử lý: hiểu là hệ quả cần khai báo; dùng khoá ngoại ghép, ghi phụ thuộc bắc cầu ở F5.1, F5.3 và đề xuất P12 cân nhắc bỏ R-19 (Đề xuất sửa artifact trước). Cạnh ERD duy nhất fk_ticket_seat ghi cả R-19 và R-22.

### 7. Phi chuẩn hoá: quy tắc của P13 mâu thuẫn với dữ liệu P12 giữ

Vị trí: Bước 3: "Phi chuẩn hoá chỉ khi có lý do đo được ... hoặc lý do ngữ nghĩa"; Bước 6: "Phát hiện sai ở P12 ... ghi vào Đề xuất sửa artifact trước, không tự sửa P12".
Gặp phải: P12 cố ý giữ R-19 và Ticket.trip dù suy được qua Seat (Vấn đề còn mở của P12), và cho phép R-12 tương tự. Đây không phải sai, nhưng buộc ticket vi phạm 3NF. Lý do ngữ nghĩa của P12 yếu, không có số đo.
Xử lý: giữ theo P12, khai báo ở F5.3 với lý do ngữ nghĩa và cơ chế (khoá ghép), ghi phương án 3NF ở F5.2 và Đề xuất sửa artifact trước. Cần X1 quyết định.

### 8. Bước 4: multiplicity 0..1 của P12 và quy tắc "lưu từ một trạng thái"

Vị trí: Bước 4: "Khi lớp chỉ được lưu từ một trạng thái trở đi (P12 hoặc ASM nêu), xét NULL/NOT NULL và DEFAULT theo các trạng thái được lưu".
Gặp phải: P12 F7 ghi Booking.holdStartedAt, seatFare multiplicity 0..1, DEFAULT của status là SELECTING, nhưng F1 nói chỉ lưu từ HOLDING. Phải suy từ P12 F6 (chuyển 2 holdSeats đặt cả seatFare và holdStartedAt) mới kết luận NOT NULL. Quy tắc của prompt đúng nhưng đòi người chạy tự đọc state machine; không có chỉ dẫn mức độ suy luận cho phép.
Xử lý: NOT NULL cho hold_started_at và seat_fare, status không DEFAULT, CHECK không có SELECTING; ghi căn cứ ở cột CHECK / mô tả.

### 9. Độ dài, scale: ranh giới giữa quyết định thiết kế và Q/ASM mơ hồ

Vị trí: Bước 4 và C1 mục 7: "Chỉ khi độ dài hoặc định dạng mang nghĩa nghiệp vụ (mã phiếu đúng 10 ký tự theo quy định của tổ chức, số lẻ thập phân của đơn giá) mà nguồn không nêu mới ghi Q hoặc ASM".
Gặp phải: ba trường hợp biên: (a) độ dài ticket_code, nguồn chỉ có ví dụ SV0001, không rõ có quy định hay không; (b) số chữ số thập phân của surcharge_percent (nguồn chỉ nói "phần trăm", "tối đa 30%"); (c) hằng số 10 phút và 30% đưa vào CHECK có nên không. Cả ba đều gần "nghĩa nghiệp vụ" nhưng không có căn cứ nào chặn.
Xử lý: coi (a), (b) là quyết định thiết kế (VARCHAR(20); DECIMAL(5,2) cho phép mức lẻ), ghi "Thiết kế: <lý do>"; scale tiền DECIMAL(12,0) dựa ASM-56 của P12. Đưa BR-03 (10 phút) và BR-24 (30%) vào CHECK, ghi ở Vấn đề còn mở rằng đổi giá trị phải đổi CHECK. Không cấp Q, ASM mới. Nếu người đánh giá coi (a) hoặc (b) là giá trị nghiệp vụ thì thiếu một Q.

### 10. F6.1 không có chỗ cho CHECK, UNIQUE nhiều cột và khoá ngoại ghép

Vị trí: F6.1: "khoá nhiều cột ghi cùng nhãn ở mỗi cột và ghi tên ràng buộc ở cột CHECK / mô tả".
Gặp phải: hướng dẫn chỉ nói về khoá nhiều cột, không nói CHECK nhiều cột (ck_booking_hold_expiry, ck_ticket_state_refund...). Cũng không rõ cột IDENTITY ghi ở "Mặc định" hay "mô tả".
Xử lý: thêm bảng F6.1-b cho ràng buộc nhiều cột; ghi "IDENTITY" ở cột Mặc định. Đề nghị bổ sung vào F6.1.

### 11. F8.1: kích thước và toạ độ bên trong bảng

Vị trí: F8.1 "Style draw.io: ... swimlane, stackLayout, startSize=26"; C7.3 "toạ độ là bội số của 10".
Gặp phải: startSize=26 nên các cell cột nằm ở y = 26 + 20 x i, không thể là bội số 10 nếu hiểu mọi toạ độ. Prompt không nêu chiều cao dòng. Điểm nối cổng (exitX, exitY) cần đúng y bội số 10 cho điểm uốn nên phải dùng phân số lẻ (0.526316, 0.857143, 0.142857).
Xử lý: chỉ áp dụng bội số 10 cho node cấp cao và điểm uốn; chiều cao dòng 20, chiều cao bảng làm tròn lên bội số 10; cổng nối dùng phân số.

### 12. F8.2: ER Chen có đồ thị đầy đủ K4, cạnh thuộc tính rất nhiều

Vị trí: F8.2 và C7.3 "khoảng cách tối thiểu giữa hai node là 40", "cạnh không cắt qua node".
Gặp phải: bốn thực thể Trip, Seat, Booking, Ticket nối với nhau từng đôi (6 mối quan hệ), khó vẽ phẳng; 35 thuộc tính ellipse với khoảng cách 40 tạo canvas khoảng 2.800 x 1.600; bảng Edge có 49 dòng. Prompt không nói cách xử lý thuộc tính quá nhiều, cũng không nêu cách vẽ mức tham gia bắt buộc (nét đôi trong Chen).
Xử lý: đặt Seat (ít thuộc tính) vào giữa tam giác Trip, Booking, Ticket; cột thuộc tính đặt xa thực thể để đường nối không chạm ellipse kề; viết kiểm tra hình học bằng chương trình. Mức tham gia chỉ nêu trong bảng F3.2, không vẽ.

### 13. Khoá ngoại trỏ bảng của package chưa có P12 (R-20)

Vị trí: không có chỉ dẫn; Target 3 "Mọi association ... được ánh xạ trong F4.2 đúng quy tắc".
Gặp phải: Ticket R-20 trỏ DC-PaymentTransaction (PKG-29) chưa có P12, P13. Không thể khai báo khoá ngoại, không thể cấp TBL cho bảng cha, không biết kiểu khoá chính.
Xử lý: giữ cột payment_transaction_id BIGINT NULL, không khai báo FK, nối ghi chú trong ERD, đặt ràng buộc ck_ticket_channel_transaction theo BR-08; ghi ở Vấn đề còn mở. Target 3 đạt một phần. Prompt nên có quy tắc cho "bảng cha chưa có".

### 14. Phạm vi PKG-13 và vị trí của Booking

Vị trí: YEU_CAU_BO_SUNG: "chỉ các lớp persistent của PKG-27 Operations và PKG-28 Ticketing".
Gặp phải: không mâu thuẫn, nhưng PKG-13 (có file P12 chung) không có lớp persistent. Booking nằm ở PKG-28 (P12 F9), không ở PKG-13 như người đọc có thể nghĩ. Ghi lại để người đánh giá không hiểu nhầm là bỏ sót.
Xử lý: F2 vẫn liệt kê lớp PKG-13 với Persistent = Không.

## Kết quả tự kiểm tra theo Target

1. Đạt. 2. Đạt (hằng số lớp MAX_SEATS, HOLD_DURATION không lưu, có lý do). 3. Đạt một phần: R-20 chưa có khoá ngoại (vướng mắc 13). 4. Đạt (không có cây kế thừa). 5. Đạt. 6. Đạt, ticket có dòng phi chuẩn hoá F5.3 (vướng mắc 7). 7. Đạt (fare, seat, ticket kiểm tra BCNF). 8. Đạt một phần: chưa đối chiếu P12 F3 (vướng mắc 2). 9. Đạt (xem vướng mắc 9 về ranh giới Q/ASM). 10. Đạt. 11. Không áp dụng (CSDL quan hệ). 12. Đạt về XML, bội số 10, khoảng cách 40, cạnh không cắt node (kiểm bằng chương trình); chưa mở bằng draw.io để xem bằng mắt. 13. Không áp dụng (SINH_DDL = Không có). 14. Đạt. 15. Đạt (C2, C5, C6; không em dash, không mũi tên Unicode, không biểu tượng cảm xúc, không inline code).
