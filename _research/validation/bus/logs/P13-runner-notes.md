# Nhật ký người chạy P13

Model: Sonnet (tham số model sonnet của công cụ Agent).

Đã ghi: design/P13-data-model.md, design/diagrams/P13-erd-logical.drawio, design/diagrams/P13-erd-conceptual.drawio. Cả hai file .drawio qua kiểm tra xml.dom.minidom. Target 1 đến 15 tự kiểm đạt, riêng mục "chưa kiểm bằng draw.io" ghi ở Vấn đề còn mở của artifact.

## Vướng mắc

1. Quá tải ngữ cảnh khi đọc P12
- Vị trí: Mục 2 bảng đầu vào "P12-class-design.md (hoặc P12-class-design/*.md)" và mục 3 "Đính kèm: ... P12".
- Gặp gì: file P12 của đề dài khoảng 186 KB (45 phần tử, 103 operation, 50 quan hệ). P13 chỉ cần F1 (cột Persistent), F5, F6 (trạng thái), F7, F7a và phần Giả định, Câu hỏi mở; F2, F3, F4, F8 là vô ích với P13.
- Xử lý: đọc có chọn lọc theo tiêu đề mục. Prompt không nói mục nào của P12 cần cho P13 nên phải tự suy.

2. Quy tắc khoá chính mặc định mơ hồ khi P12 đã có định danh String
- Câu trích: "bảng của thực thể độc lập dùng khoá thay thế (surrogate) tên id, kiểu theo kiểu của thuộc tính định danh trong P12" và "Khoá tự nhiên (mã hàng, số phiếu, email) giữ ràng buộc UNIQUE".
- Gặp gì: P12 có tripId, bookingId... là String do hệ thống cấp, vốn đã là khoá thay thế; đặt tên cột id hay giữ trip_id không rõ. Với DC-Ticket.ticketCode (mã in trên vé, quét mã vạch) thì vừa là định danh duy nhất của P12 vừa là khoá tự nhiên, nên quy tắc cho hai kết quả trái nhau.
- Xử lý: các định danh String khác thành cột id VARCHAR(36); ticketCode làm khoá chính tự nhiên (bất biến, ngắn, duy nhất, là khoá tra cứu) và ghi lý do ở F1. Ghi ở Vấn đề còn mở của artifact.

3. Multiplicity 0..1 --> NULL mâu thuẫn với lớp không được lưu ở trạng thái đầu
- Câu trích: "NULL/NOT NULL theo multiplicity (1 --> NOT NULL; 0..1 --> NULL)" và Target 8 "NULL/NOT NULL khớp multiplicity".
- Gặp gì: Booking.ticketPrice, totalAmount, holdStartTime có multiplicity 0..1 chỉ vì trạng thái DRAFT, mà ASM-44 nói DRAFT không bao giờ được lưu; bản ghi thật luôn có giá trị.
- Xử lý: giữ NULL theo quy tắc, thêm CHECK theo status (ck_booking_state). Prompt không nói cách xử lý khi multiplicity chỉ phản ánh trạng thái chưa lưu.

4. Quan hệ P12 uỷ quyền cho P13 quyết định nhưng quy tắc F4.2 buộc có khoá ngoại
- Câu trích: P12 R-25 "P13 quyết định lưu liên kết hay truy vấn theo ngày"; Target 3 "Mọi association ... được ánh xạ trong F4.2 đúng quy tắc (FK ở phía N, ...)".
- Gặp gì: lưu FK trip.holiday_surcharge_id sẽ cũ đi khi sửa khoảng ngày và dư thừa với ngày xuất bến. F4.2 không có quy tắc cho "liên kết suy ra".
- Xử lý: không có FK, tra theo ngày bằng ràng buộc EXCLUDE kiểu gist; ghi dòng R-25 ở F4.2 với kiểu "Không áp dụng". Target 3 đạt theo cách hiểu có ngoại lệ có lý do.

5. Thiếu hướng dẫn cho khoá ngoại ghép trỏ khoá ứng viên và khoá ngoại dùng chung cột
- Gặp gì: R-24 (Trip - BaseFare) cần FK ghép (route_id, bus_type) trỏ khoá ứng viên của base_fare (nếu lưu base_fare_id sẽ vi phạm 3NF vì phụ thuộc bắc cầu); R-29 và R-30 của Ticket dùng chung cột trip_id. Mục F4.2, F6.1, F8.1 chỉ nói khoá ngoại một cột. Edge ID "fk_<bang_con>_<bang_cha> (thêm hậu tố khi có nhiều FK giữa cùng hai bảng)" không nói cách ghi khi một khoá ngoại ghép thể hiện hai quan hệ P12 (R-29, R-30).
- Xử lý: đánh dấu FK ở từng cột của khoá ghép, ghi tên ràng buộc ở cột CHECK / mô tả (theo hướng dẫn "khoá nhiều cột"), vẽ một cạnh fk_ticket_seat cho cả R-29 và R-30 và ghi chú. Không có hướng dẫn cho index một phần (partial), ràng buộc EXCLUDE trong F6.3 và F8.1; tôi ghi chúng vào cột Loại và vào mô tả.

6. Bảng cho thuộc tính đa trị phức hợp của lớp value object mâu thuẫn nhẹ với F2
- Câu trích: Bước 2 "thuộc tính đa trị (tập hợp giá trị đơn) thành bảng riêng; thuộc tính phức hợp (value object) thành nhiều cột"; F2 "Lớp Persistent = Không: ghi lý do".
- Gặp gì: DC-TravelerInfo có Persistent = Không trong P12 nhưng danh sách Booking.travelerInfos (đa trị, phức hợp) phải lưu (dịch vụ không giữ trạng thái giữa submitBooking và completeBooking). Bước 2 không nói trường hợp vừa đa trị vừa phức hợp; Target 1 chỉ nói lớp Persistent = Có.
- Xử lý: tạo TBL-06 booking_traveler, ghi ở F2 dòng DC-TravelerInfo với Persistent = Không và chiến lược "Nhúng vào TBL-06". Khoá ngoại seat_code của TBL-06 tới seat không khai báo được mà không thêm cột trip_id (vi phạm 3NF), nên để ứng dụng giữ.

7. Mã TBL không có quy tắc thứ tự
- Câu trích: "TBL-nn theo Conventions C3, cấp tuần tự, không đổi khi chạy lại".
- Xử lý: cấp theo thứ tự bảng cha trước bảng con. Không rõ khi chạy lại P13 cho thêm package thì mã mới nối tiếp thế nào (thứ tự cha trước con sẽ bị phá).

8. Q, ASM đánh số tiếp nhưng chỉ đọc được một phần đầu vào
- Câu trích: C3 "Lần nào chạy cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất đã thấy".
- Gặp gì: phạm vi đọc không gồm P07, P08, P10, P11a, P11b nên chỉ thấy Q-108 và ASM-107 (từ P12). Các artifact đó có thể có mã lớn hơn; Q-109 và ASM-108 đến ASM-110 có thể trùng.
- Xử lý: cấp tiếp từ số lớn nhất thấy được và ghi cảnh báo ở Vấn đề còn mở.

9. Mâu thuẫn kiểu cạnh ERD giữa C7.3 và F8.2
- Câu trích: C7.3 "dùng edgeStyle=orthogonalEdgeStyle cho sơ đồ lớp, sơ đồ package, ERD"; F8.2 "cạnh endArrow=none;html=1;".
- Xử lý: ERD logic dùng orthogonalEdgeStyle kèm điểm uốn; ER Chen dùng cạnh thẳng theo F8.2 (ghi ở Vấn đề còn mở, theo C9). Cạnh thẳng nên "cạnh không cắt qua node" kiểm bằng tính toán đoạn thẳng giữa tâm hai node.

10. C7.3 yêu cầu nhãn multiplicity là cell con, F8.2 nói "ghi trên đoạn nối"
- Xử lý: dùng cell con edgeLabel cho cả hai sơ đồ. Với Chen không có hướng dẫn x của nhãn nên đặt x=-0.55 (gần phía thực thể).

11. Ký pháp tuỳ chọn tham gia 0..1 ở đầu cha
- Câu trích: F8.1 "đầu phía bảng cha thể hiện 'một' (bắt buộc: một vạch kép; tuỳ chọn: vòng tròn và vạch)"; danh sách style trong F8.1 "ERmandOne, ERzeroToOne, ERone, ERmany, ERoneToMany, ERzeroToMany".
- Gặp gì: quan hệ có cha tuỳ chọn (seat.holding_booking_id) dùng ERzeroToOne ở đầu cha; đầu con với bản số 1..5 dùng ERoneToMany (không có ký pháp cho giới hạn trên 5). Hướng dẫn đủ nhưng bản số cụ thể chỉ ghi ở nhãn văn bản.

12. Chiều của "Tham gia A, B" ở F3.2
- Câu trích: "Tham gia A, B (bắt buộc / tuỳ chọn)" kèm "Bản số (từ multiplicity)".
- Gặp gì: không nói tham gia của A suy từ bản số tối thiểu ở đầu B hay đầu A. Tôi dùng quy ước: A bắt buộc khi bản số tối thiểu ở phía B lớn hơn 0 và ghi quy ước dưới bảng. Với R-37 phía B còn "?" (Q-76) nên ghi "chưa rõ".

13. F2 phải liệt kê cả lớp không persistent
- Gặp gì: phạm vi có 45 phần tử; prompt không cho phép gộp dòng nên F2 dài 45 dòng, nhiều dòng giống nhau (enumeration, value object). Không có hướng dẫn rút gọn.

14. Phiên bản hệ quản trị và thời gian lưu dữ liệu không có trong đầu vào
- CONG_NGHE chỉ nói "PostgreSQL". Tính năng EXCLUDE gist và index một phần cần phiên bản tối thiểu; tôi ghi "từ 9.2" là quyết định thiết kế. Không có yêu cầu lưu trữ nên không có chiến lược phân vùng; ghi ở Vấn đề còn mở.

15. Ví dụ F6.1 thiếu ON UPDATE
- Câu trích: cột "Tham chiếu FK (TBL.cột, ON DELETE, ON UPDATE)" nhưng ví dụ đúng chỉ ghi "TBL-01.id, RESTRICT".
- Xử lý: ghi đủ ba phần, ON UPDATE là NO ACTION vì khoá bất biến (readOnly).

16. Ràng buộc liên bảng không khai báo được
- Prompt không có chỗ ghi mục này; tôi ghi cuối F4.2 (seat SOLD với vé, booking_traveler.seat_code thuộc chuyến của booking, refund_method khớp kênh mua). Target 8 "CHECK phủ ràng buộc BR" khó đạt trọn cho các BR liên bảng.

## Target không đạt
Không có Target nào ghi Không đạt. Hai chỗ đạt có điều kiện: Target 3 (R-25 không có FK, lý do ở mục 4) và Target 8 (ràng buộc BR liên bảng do ứng dụng giữ, mục 16). Target 11, 13 không áp dụng (CSDL quan hệ, SINH_DDL = Không có).
