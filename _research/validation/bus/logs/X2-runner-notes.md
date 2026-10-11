# X2 - Nhật ký người chạy - Hệ thống bán vé xe khách SaoViet Bus

Model: Sonnet (tham số model sonnet của công cụ Agent).

Phạm vi chạy: PHAM_VI_TEST = DC-TicketReturnPolicy, DC-Booking, DC-Ticket (PKG-23), AI chọn operation. Kết quả: 37 operation có dòng F1, 25 được chọn, 150 TC (142 có kết quả mong đợi xác định, 8 chờ Q), 141 EC, 47 BV, 8 bảng quyết định, 12 CFG kèm 12 file .drawio, Q-110 đến Q-114, ASM-111 đến ASM-114. Cách làm: dữ liệu test được nhập vào một script trong thư mục tạm, script sinh tự động file .md (bảng F2.x.6, F3, F4) và các file .drawio để mã EC, BV, DT, N, CE, TC và ma trận phủ nhất quán; script kiểm tra V(G) bằng hai cách, đường đi hợp lệ trên CFG, khoảng cách node, cạnh không cắt node. File .drawio đều qua kiểm tra XML.

## Vướng mắc

### 1. Quy mô đầu ra so với yêu cầu "mọi" của Target
- Vị trí: mục 3 "Chạy theo nhóm lớp (một package hoặc vài lớp liên quan) để kết quả không quá dài" và Target 1 "Mọi phương thức trong phạm vi có dòng ở F1", Target 3 "Mọi lớp có thứ tự có giá trị biên", Target 5, Target 6.
- Gặp gì: PHAM_VI_TEST do người điều phối giao là ba lớp với "AI chọn" nên có 37 operation, chọn 25. Để thoả đồng thời các Target "mọi", file X2-unit-tests.md dài khoảng 223 KB, 2.900 dòng. Prompt không nêu ngưỡng số operation hay số TC cho một lần chạy (khác P12 có ngưỡng 15-20 lớp).
- Xử lý: chạy một lượt, ghi nhận ở Vấn đề còn mở. Đề xuất cho prompt: thêm ngưỡng (ví dụ tối đa khoảng 10 operation ưu tiên Cao mỗi lần) hoặc cho phép F2.x của operation đơn giản viết rút gọn.

### 2. Hộp trắng chỉ có cho một phần operation, mục tiêu độ phủ mặc định không đo được cho phần còn lại
- Vị trí: Bước 4 "Kỹ thuật hộp trắng (khi có thiết kế method hoặc mã nguồn)"; MUC_TIEU_PHU mặc định "100% C1 cho phương thức ưu tiên Cao, 100% C0 cho phương thức còn lại".
- Gặp gì: P12 F3 chỉ có thiết kế method cho 12 trong 25 operation được chọn (một dòng F3 có thể gộp hai operation, ví dụ "DC-Ticket.cancelWithTrip() và recordRefund(...)"). 13 operation còn lại (isWithinSeatLimit, isHoldExpired, matchesPurchaseChannel...) không có CFG nên không tính được C0, C1 như mục tiêu mặc định. Prompt không nói mục tiêu mặc định xử lý ra sao khi thiếu F3.
- Xử lý: với 13 operation đó ghi "Chưa đo" và ước tính 100% theo lớp tương đương ở F4, kèm Vấn đề còn mở yêu cầu đo lại khi có mã. Với isReturnTimeAllowed ghi V(G) = 1 theo mô tả và không vẽ CFG.

### 3. Ngữ nghĩa cột "Hợp lệ / Không hợp lệ" với toán tử kiểm tra
- Vị trí: F2.x.2 "| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |" và Bước 3.1 "Luôn có cả lớp hợp lệ và lớp không hợp lệ (sai kiểu, ngoài miền, rỗng, null)".
- Gặp gì: nhiều operation là predicate hoặc phân loại (matchesPurchaseChannel, isReturnTimeAllowed, isHoldExpired, determineCheckResult). Mọi giá trị đầu vào đều hợp lệ về miền, chỉ khác kết quả (true hoặc false). Ví dụ minh hoạ trong prompt (issue(quantity)) là phân vùng theo miền đầu vào, không rõ áp dụng ra sao cho predicate. Cũng có phương thức bỏ qua thay vì ném ngoại lệ (releaseSeats ở trạng thái khác HELD).
- Xử lý: đặt quy ước ở đầu file: "Hợp lệ" là lớp cho kết quả thuận theo BR, "Không hợp lệ" là lớp cho kết quả từ chối; lớp bỏ qua ghi "Hợp lệ (không đổi)". Đề xuất cho prompt: thêm một câu về cách gán nhãn cho predicate.

### 4. Lớp null và tham số ngoài hợp đồng mâu thuẫn với "không tự quyết"
- Vị trí: Bước 3.1 "(sai kiểu, ngoài miền, rỗng, null)" với Bước 3.6 "Khi đặc tả không nói kết quả ... không tự quyết: ghi Q/ASM" và F2.x.2 "(trừ khi kiểu dữ liệu làm cho lớp không hợp lệ không thể xảy ra, ghi lý do)".
- Gặp gì: P12 không khai báo hành vi cho null, bookingId rỗng, vé sai trạng thái đưa vào TicketReturnPolicy. Tạo TC cho từng tham số null của 25 operation sẽ sinh hàng chục câu hỏi giống nhau.
- Xử lý: mỗi operation có EC "null" nhưng không có TC; gộp một giả định ASM-111 (CO_NHAN) giải thích. Ghi F4 "Không: ASM-111". Đây là lựa chọn của người chạy, prompt không nêu cách gộp.

### 5. "Gộp quy tắc ... chỉ khi đặc tả cho biết thứ tự kiểm tra": "đặc tả" chỉ nguồn nào
- Vị trí: Bước 3.3 "gộp quy tắc có hành động giống nhau bằng giá trị '-' (không quan tâm) chỉ khi đặc tả cho biết thứ tự kiểm tra"; Target 4 "quy tắc gộp có căn cứ".
- Gặp gì: thứ tự kiểm tra có khi nằm ở P04 (UC-002 7b "Thông tin đủ ... và có ít nhất một số điện thoại sai", UC-015 5c "chưa bị huỷ và đã được soát") và có khi chỉ nằm ở P12 F3 (cancelTicket: kiểm status trước method). Prompt không nói F3 (thiết kế) có được coi là "đặc tả" hay không.
- Xử lý: chấp nhận cả P04 và P12 F3, ghi căn cứ ngay dưới bảng quyết định; chỗ không có căn cứ rõ (markChecked, holdSeats) thì không gộp, giữ đủ quy tắc.

### 6. Kết quả mong đợi không quan sát được vì P12 thiếu accessor
- Vị trí: Bước 3.6 "ghi giá trị cụ thể (giá trị trả về, ngoại lệ, trạng thái đối tượng sau ...). Với trường hợp lỗi, kiểm tra cả việc trạng thái không bị thay đổi"; mục 2 "P12 ... Chữ ký, tiền/hậu điều kiện".
- Gặp gì: P12 F7 có thuộc tính Seat.status, Ticket.status, checkedTime, refund, Booking.paymentReference, paymentAttemptCount, các thuộc tính của Refund, nhưng F2 không có getter cho chúng. Hậu điều kiện "ghi paymentReference", "Seat HELD sang SOLD" không kiểm tra được qua giao diện công khai. Prompt không nói xử lý ra sao khi thiết kế thiếu khả năng quan sát.
- Xử lý: ASM-114 (accessor trùng tên thuộc tính) và mục "Đề xuất sửa artifact trước" cho P12. Một số TC (startPaymentAttempt) quan sát gián tiếp qua khoá trả về.

### 7. Thứ tự bước trong F3 làm lộ lỗ hổng không phải do X2 tạo ra
- Vị trí: Bước 0 "Nếu phương thức trong phạm vi thiếu tiền/hậu điều kiện hoặc ngoại lệ ở P12, ghi vào 'Đề xuất sửa artifact trước'".
- Gặp gì: DC-Ticket.cancelTicket đổi status và release Seat (bước 2, 3) trước khi Refund.createRefund kiểm miền tham số (bước 5); F2 của cancelTicket không khai báo IllegalArgumentException. DC-Booking.holdSeats ghi "tất cả hoặc không" nhưng F3 không hoàn tác. Tiền điều kiện này không "thiếu" theo nghĩa Bước 0 (có nhưng mâu thuẫn nội bộ), prompt không có tình huống cho mâu thuẫn trong P12.
- Xử lý: ghi Q-110, Q-111 và đề xuất sửa P12; các TC liên quan để "Chưa xác định: chờ Q".

### 8. TC có kết quả chưa xác định: có liệt kê hay không
- Vị trí: F3 "Kết quả mong đợi ... cụ thể"; Target 7 "Mọi test case có ... kết quả mong đợi cụ thể" với Target 8 "chỗ đặc tả không nói có Q/ASM".
- Gặp gì: Target 7 và 8 không thoả đồng thời cho các ca bị Q chặn. Prompt không nói ca bị chặn là TC thật hay chỉ là mục trong Q.
- Xử lý: liệt kê 8 TC với kết quả "Chưa xác định: chờ Q-nn", không tính vào độ phủ ở F4 (đánh dấu "Không: chờ Q-nn"); Target 7 vì vậy không đạt trọn vẹn cho 8 TC đó (ghi ở Vấn đề còn mở).

### 9. Quy ước mã nội bộ dễ nhầm với mã Q-nn
- Vị trí: Format "quy tắc bảng quyết định DT<k>-Q<n> (bảng thứ k, quy tắc n)" và ví dụ bảng quyết định có cột "Q1 | Q2 | Q3".
- Gặp gì: "Q1" của quy tắc dễ lẫn với câu hỏi mở "Q-nn" trong cùng file, nhất là trong cột Phủ ("DT3-Q3" cạnh "Q-110"). Mã "N<n>" cho node cũng gần "N/A".
- Xử lý: dùng tiêu đề cột đầy đủ DT<k>-Q<n> trong bảng quyết định thay vì Q1, Q2 như khung mẫu. Không có hậu quả sai lệch, chỉ khó đọc.

### 10. Cấp mã Q và ASM khi có phiên khác chạy song song
- Vị trí: Conventions C3 "tìm mã Q và ASM lớn nhất đã thấy, rồi cấp tiếp từ số đó".
- Gặp gì: trong các file đầu vào được phép đọc (P04, P06, P12, P13, project-profile) lớn nhất là Q-109 và ASM-110; X2 cấp từ Q-110 và ASM-111. Phiên X1 chạy song song cấp từ Q-150 và ASM-150 nên tạm không đụng. Tuy nhiên C3 không nói có phải quét cả artifact ngoài danh sách đầu vào của bước (P07, P11a, P11b...) không; tôi chỉ quét đầu vào của X2 theo mục 2 và phạm vi đọc được phép, nên không loại trừ được trùng mã với artifact khác.
- Xử lý: cấp tiếp từ số lớn nhất tìm thấy; ghi rủi ro ở đây.

### 11. Bảng node của CFG không có toạ độ, .drawio không sinh lại tất định từ bảng .md
- Vị trí: F2.x.6 "Bảng node: | N | Nội dung | Loại |" và C7.1 "Khuyến nghị thêm bốn cột x, y, w, h vào bảng Node để file .drawio sinh ra từ bảng một cách tất định".
- Gặp gì: khung F2.x.6 của prompt không có cột x, y, w, h hay cột Điểm uốn của cạnh; C7.1 coi bảng .md là nguồn chuẩn để sinh lại .drawio. Với CFG có cạnh quay lại vòng lặp, cần điểm uốn để cạnh không cắt node.
- Xử lý: giữ đúng khung F2.x.6 (không thêm cột) nên toạ độ và điểm uốn chỉ có trong file .drawio. Bố cục kiểm bằng tính toán (bội số 10, khoảng cách node tối thiểu 40, cạnh không cắt node); chưa mở bằng draw.io để xem nhãn. Đề xuất cho prompt: thêm cột x, y, w, h và Điểm uốn vào khung F2.x.6.

### 12. Tên file CFG với <DC>
- Vị trí: Đầu ra "diagrams/X2-cfg-<DC>-<operation>.drawio"; C7.2 "X2-cfg-<DC>-<operation>".
- Gặp gì: <DC> có thể hiểu là mã đầy đủ "DC-Booking" hoặc chỉ "Booking". Ví dụ P12 trong C7.2 dùng "P12-state-<DC>" và các file đó có dạng P12-state-DC-Booking.
- Xử lý: dùng mã đầy đủ, ví dụ X2-cfg-DC-Booking-holdSeats.drawio.

### 13. Style CFG trong C7.3 và định tuyến cạnh
- Vị trí: C7.3 dòng "Đồ thị luồng điều khiển (X2)" và "dùng edgeStyle=orthogonalEdgeStyle cho sơ đồ lớp, sơ đồ package, ERD".
- Gặp gì: style cạnh CFG là "endArrow=block;endFill=1;html=1;" không có orthogonalEdgeStyle, nên cạnh quay lại vòng lặp và cạnh rẽ nhánh đi thẳng sẽ cắt node nếu không có điểm uốn. Style nút bắt đầu, kết thúc trỏ sang dòng "Activity initial / final" (kích thước 40x40), còn khung C7.3 yêu cầu node cách nhau tối thiểu 40, khối lệnh rộng.
- Xử lý: thêm mxPoint tường minh cho cạnh cần (theo C7.1), giữ nguyên style đã quy định. Không có xung đột phải chọn.

### 14. Đường đi cơ sở và V(G) lớn
- Vị trí: F2.x.6 "danh sách đường đi cơ sở (chuỗi node)"; Bước 4.2 "V(G) là số đường đi cơ sở độc lập".
- Gặp gì: prompt không nói cách chọn tập đường đi độc lập; với vòng lặp, một đường đi có thể lặp nhiều lần.
- Xử lý: tập đường độc lập tuyến tính (hạng của vectơ cạnh) chọn trong số các đường của bộ TC, ưu tiên đường ngắn; đạt đủ V(G) đường ở cả 12 CFG. Mọi V(G) không lớn hơn 6 nên không có đề xuất tách phương thức.

### 15. Chênh giữa P12 và đặc tả P04 phát hiện khi suy kết quả mong đợi
- Vị trí: Bước 2 "Thu thập cơ sở kiểm thử ... BR liên quan (P06); luồng thay thế (P04)".
- Gặp gì: BR-07 không nói biên 10 phút đóng hay mở (P12 chọn "không trước" tức hết hạn đúng 10 phút); BR-12 đến BR-14 không nói độ chính xác thời gian (giây hay phút). Hai điểm này là BV quan trọng nên cần giả định.
- Xử lý: ASM-112, ASM-113 và đề xuất bổ sung ở P06.

## Kết quả tự kiểm tra theo Target

1. Đạt: 37 operation đều có dòng F1 (25 chọn, 12 không chọn với lý do: 1 ủy quyền, 11 getter).
2. Đạt: mọi operation chọn có EC hợp lệ và không hợp lệ, lớp rời nhau; phần lớp không thể xảy ra được ghi lý do; lớp null theo ASM-111.
3. Đạt: BV tại và ngay ngoài biên đúng phía (BR-12 4 giờ, BR-13/14 24 giờ, BR-01 5 và 6, BR-07 biên 10 phút theo ASM-112); với lớp chưa xác định (Q-111) có BV nhưng TC chờ Q.
4. Đạt: 8 bảng quyết định, quy tắc N/A và quy tắc gộp có căn cứ; markChecked, holdSeats không gộp.
5. Đạt: createBooking, holdSeats, releaseSeats, issueTickets, createTicket, markChecked, cancelTicket, cancelWithTrip có TC chuyển hợp lệ, guard đúng/sai (holdSeats) và sự kiện ở trạng thái không cho phép.
6. Đạt một phần: mọi BR và luồng P04 liên quan tới lớp trong phạm vi có TC hoặc lý do ở F4; BR-20, UC-008 2a/6a/9a, UC-013 luồng kiểm tra chuyến, UC-002 2a/4a, UC-015 5a thuộc lớp ngoài phạm vi (ghi lý do và mức kiểm thử).
7. Không đạt trọn vẹn: 8 TC có kết quả "Chưa xác định: chờ Q-nn" (xem vướng mắc 8). 142 TC còn lại có điều kiện đầu, dữ liệu vào cụ thể, kết quả (gồm trạng thái sau), nguồn.
8. Đạt: chỗ đặc tả không nói có Q-110 đến Q-114 hoặc ASM-111 đến ASM-114.
9. Đạt một phần: 12 CFG đạt 100% C0, C1; 13 operation không có F3 chỉ ước tính (xem vướng mắc 2). V(G) lớn nhất là 6.
10. Đạt: validateTravelerInfo (hai vòng tuần tự), holdSeats, releaseSeats, issueTickets có TC cho 1, 2 (m), 4 (n-1), 5 (n); 0 và n+1 ghi không áp dụng kèm lý do (đã bị createBooking, isWithinSeatLimit chặn).
11. Đạt: phụ thuộc ngoài được thay bằng stub, fake, mock; không dùng đồng hồ hệ thống vì thời gian nhận qua tham số.
12. Đạt một phần: mỗi TC một hành vi; các TC bảng quyết định có chủ ý chứa hai giá trị không hợp lệ (validateTravelerInfo ưu tiên MISSING_INFO trước INVALID_PHONE) và có ghi rõ.
13. Không áp dụng: SINH_MA_TEST = Không có.
14. Đạt: C2 (không em dash, không mũi tên Unicode), C5 (khung và các mục kiểm soát), C6 (placeholder đã điền, mục tuỳ chọn dùng mặc định); .drawio hợp lệ XML.
