# Nhật ký người chạy P07-UC-002

Model: Sonnet (tham số model sonnet của công cụ Agent).

Phạm vi lần chạy: P07 cho UC-002 Đặt vé trực tuyến, LUONG_CAN_VE = Không có, YEU_CAU_BO_SUNG = Không có. Đầu ra: design/P07-uc-analysis/UC-002-book-ticket-online-analysis.md và ba file .drawio (sequence 3 trang, communication, class).

## Vướng mắc

1. Ngưỡng một trang sequence so với luồng chính
- Vị trí: F5, "Ngưỡng tách sơ đồ: một trang tối đa khoảng 30 message và tối đa 3 fragment ở mức ngoài cùng; vượt ngưỡng thì tách luồng thay thế sang trang riêng".
- Gặp: luồng chính UC-002 có 13 bước, chuỗi tìm chuyến, sơ đồ chỗ, kiểm tra, tính giá, giữ chỗ, include, phát hành, gửi SMS cho ra 41 message không trả về (46 dòng kể cả trả về) trên SD1, vượt 30. Ngưỡng chỉ nói tách luồng thay thế, không nói gì khi chính luồng chính vượt ngưỡng.
- Xử lý: giữ luồng chính một trang để communication diagram (F7 "phạm vi là luồng chính của sơ đồ SD1") cùng phạm vi; ghi vào Vấn đề còn mở. Không biết đây là lỗi prompt hay chấp nhận được.

2. "Luồng thay thế đã gộp" và giới hạn 3 fragment ngoài cùng
- Vị trí: A6 "Luồng thay thế ngắn (1-3 message khác biệt) vẽ trong cùng sơ đồ bằng combined fragment"; F7 "Communication diagram cho luồng thay thế (chỉ khi DAY_DU): thêm các luồng thay thế đã gộp vào SD1".
- Gặp: UC-002 có 8 luồng thay thế (2a, 4a, 6a, 6b, 7a, 7b, 9a, 10a), đều ngắn (1-4 message). Gộp hết vào SD1 thì có hơn 3 fragment ngoài cùng. MUC_CHI_TIET là DAY_DU nên đáng ra phải gộp.
- Xử lý: gộp 9a (break) và 10a (loop, opt) vào SD1; tách 2a, 4a sang SD2 và 6a, 6b, 7a, 7b sang SD3. Communication chỉ lấy SD1. Prompt không nói communication có phải gồm cả luồng ở trang riêng không; chọn không gồm. Ghi vào Vấn đề còn mở.

3. Đánh số STT cho message ở trang sơ đồ riêng
- Vị trí: F5c "Luồng thay thế trong fragment dùng tiếp số của luồng chính".
- Gặp: không có quy tắc cho message ở trang tách riêng (SD2, SD3) vì không còn "tiếp số" trên cùng trang. Cũng không có quy tắc thể hiện điểm rẽ nhánh khi trang không có message luồng chính.
- Xử lý: dùng STT của message cùng điểm rẽ nhánh trong SD1 kèm hậu tố a hoặc b (ví dụ 3.1.4a); điểm rẽ nhánh ghi ở cột Ghi chú của fragment. Toán hạng else của alt lặp lại message luồng chính để alt có đủ hai toán hạng có guard.

4. Luồng "Quay lại bước n" không có ký pháp
- Vị trí: F5 nói về break cho luồng kết thúc use case; không nói gì về luồng thay thế quay lại bước trước (P04 cột "Quay lại / Kết thúc").
- Gặp: 2a, 4a, 6a, 6b, 7a, 7b, 10a đều quay lại. Sequence diagram không có cách chuẩn vẽ "quay lại"; loop không khớp với 2a, 4a, 6a, 6b, 7a, 7b vì vòng lặp do hành khách thao tác.
- Xử lý: 10a dùng loop (vì control gọi lại UC-003); các luồng còn lại dùng alt, ghi "Quay lại bước n" ở cột Ghi chú fragment, không vẽ vòng lại.

5. Bảng F2 không có cột điều kiện và cột quay lại
- Vị trí: F2 "| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung | Nguồn |".
- Gặp: P04 có cột Điều kiện, Hành động, Quay lại / Kết thúc cho luồng thay thế; F2 chỉ có một cột "Mô tả trong đặc tả".
- Xử lý: gộp điều kiện, hành động và đích quay lại thành một ô, bắt đầu bằng "Điều kiện:".

6. Bước 9a có "Thực hiện bởi" là "-" và thời điểm xảy ra
- Vị trí: A2 "Thời hạn nội bộ ... Control ghi nhận bắt đầu chờ bằng message tự gọi ... nhận sự kiện hết hạn bằng message tự gọi có nhãn after(<thời hạn>)... luồng hết hạn vẽ bằng fragment alt hoặc break theo F5".
- Gặp: P04 UC-002 9a ghi "Thực hiện bởi" là "-" và Mục 8 nói thời hạn giữ chỗ tiếp tục chạy khi UC-003 đang thực hiện, tức hết hạn có thể xảy ra trong bước 10. Sequence diagram không vẽ được "ngắt giữa chừng một message tới UC khác".
- Xử lý: đặt break 9a trước message gọi UC-003 theo thứ tự bước của P04; ghi vào Đề xuất sửa P04 và Vấn đề còn mở.

7. Danh sách giá trị cột Kết luận (F3.2) không đủ
- Vị trí: F3.2 "Cột Kết luận chỉ nhận một trong các giá trị: ...".
- Gặp: điều kiện định dạng số điện thoại (10 chữ số, bắt đầu bằng 0) và mốc "ngày hiện tại" đến từ giả định ASM-15, không có BR; giá trị "tham số của quy tắc BR-nn" không áp dụng đúng. Danh từ như "SMS", "nội dung SMS" (dữ liệu đi qua boundary, không lưu) cũng không có giá trị khớp.
- Xử lý: ghi "Loại - tham số của quy tắc ASM-15" (ngoài danh sách) và "Loại - thao tác hoặc sự kiện" cho SMS với lý do cụ thể. Ghi vào Vấn đề còn mở.

8. Hai quy tắc đặt tên khác nhau cho boundary và control
- Vị trí: F3.1 "<Hành động hoặc đối tượng><Form|Screen|UI>" và F3.3 "<TênUseCase>Controller".
- Gặp: tên tiếng Anh của UC-002 là Book Ticket Online nên control là BookTicketOnlineController, còn boundary theo hành động là BookTicketForm. Hai tên lệch nhau; control của UC-003 được đặt trước thành PayTicketOnlineController dựa trên tên Pay Ticket Online trong P02.
- Xử lý: làm đúng từng quy tắc. Chưa rõ có chủ ý hay không.

9. Boundary kiểm tra hình thức so với thứ tự bước
- Vị trí: F3.4 "Boundary chỉ được kiểm tra hình thức dữ liệu nhập (bắt buộc, định dạng)"; P04 bước 7 và Q-34 (thứ tự báo lỗi).
- Gặp: bước 7 (thiếu họ tên, sai định dạng số điện thoại) có thể giao cho BookTicketForm, nhưng đặc tả đặt sau bước 6 và Q-34 quy định thứ tự báo lỗi.
- Xử lý: giao cho Booking (validateTravelerInfo), ghi lý do ở F4 và Vấn đề còn mở (chọn giữa hai quy tắc).

10. Điều kiện hợp lệ ở Dữ liệu vào 1 không có bước kiểm tra
- Vị trí: đầu vào P04 UC-002 Dữ liệu vào 1 #3 "Ngày theo lịch, không trước ngày hiện tại (ASM-15)".
- Gặp: không bước hay luồng thay thế nào kiểm tra; Target 1 và 2 (mọi thứ truy được về bước) không có chỗ cho kiểm tra này. Đầu vào không khớp với yêu cầu đầu ra.
- Xử lý: không thêm chức năng (C1); ghi vào Đề xuất sửa P04.

11. Multiplicity chỉ rõ một phía
- Vị trí: F8b "Multiplicity (dạng "A <m> - B <m>")" và A8 "nếu không rõ thì để trống".
- Gặp: nhiều quan hệ chỉ biết một phía (ví dụ BR-01 cho Booking - Seat là "1..5" phía Seat). Dạng chuẩn không nói cách ghi khi một phía trống.
- Xử lý: ghi "A - B 1..5"; khi cả hai phía trống ghi "-". Nhãn multiplicity trong .drawio chỉ vẽ phía có giá trị.

12. Granularity của trách nhiệm thông báo
- Vị trí: A7 "Message giống nhau về ý nghĩa gộp thành một trách nhiệm" so với mục tiêu truy vết từng bước.
- Gặp: 6 luồng thay thế khác nhau đều là "thông báo lỗi" trên BookTicketForm. Gộp thành một showNotice thì mất truy vết tới bước; tách thì boundary có 14 trách nhiệm (không có ngưỡng cho boundary).
- Xử lý: tách mỗi thông báo một trách nhiệm có tên riêng.

13. C7.3 không thoả được cho sequence diagram
- Vị trí: C7.3 "không có hai node chồng lên nhau; cạnh không cắt qua node" so với F10 sequence (fragment bao các message, message nối hai lifeline).
- Gặp: trong sequence diagram message luôn đi qua các lifeline ở giữa, fragment phủ lên lifeline. Không thể thoả đồng thời C7.3 và F10.
- Xử lý: theo F10 cho sequence; áp dụng đầy đủ C7.3 cho communication và VOPC (đã kiểm tra bằng script: không node chồng nhau, khoảng cách tối thiểu 40, cạnh không cắt node, toạ độ bội số 10). Ghi ở Vấn đề còn mở (Target 14 đạt một phần).

14. Định tuyến cạnh VOPC
- Vị trí: C7.1 (làn y riêng, cổng ra vào chia đều) và C7.3 (toạ độ bội số 10).
- Gặp: cổng ra vào chia đều theo phân số của chiều rộng lớp thì điểm uốn không là bội số 10.
- Xử lý: chọn chiều rộng lớp 240 và phân số bội của 1/8 để mọi điểm uốn là bội số 10; làn cách nhau 10.

15. Giả định cần thêm do P04 thiếu
- Vị trí: A4 "Ứng viên còn lại là entity nếu hệ thống phải lưu ..." và P04 UC-002 Dữ liệu ra 2 "sơ đồ chỗ của xe của chuyến".
- Gặp: P04 và P05 không nói chỗ thuộc xe hay thuộc chuyến, nơi giữ thông tin người đi trước khi có vé, thời điểm có lần đặt. Cần để vẽ Seat, Booking.
- Xử lý: CO_NHAN nên ghi ASM-42, ASM-43, ASM-44 và một câu hỏi Q-69 (khái niệm chưa rõ). Mã Q, ASM cấp tiếp từ Q-68 và ASM-41 (số lớn nhất tìm thấy trong P06).

16. Quá tải ngữ cảnh khi đọc đầu vào
- Vị trí: mục 2 liệt kê P01, P02, P03, P05, P06 đều là đầu vào.
- Gặp: các file này tổng khoảng 170 KB, chỉ một phần nhỏ liên quan UC-002 (bảng tác nhân, quan hệ RL-27, thuật ngữ GL, BR, mục P02 của UC-006, UC-014 để xét A2). Prompt không nói đọc phần nào (README mục 8 có gợi ý cho P04 nhưng không cho P07).
- Xử lý: đọc theo mục bằng tìm kiếm; không gặp mất thông tin, nhưng với dự án lớn bước này dễ quá tải.

17. Mốc thời gian phụ thuộc dữ liệu (A2)
- Vị trí: A2 "Mốc thời gian phụ thuộc dữ liệu: nếu P02 có use case do tác nhân thời gian kích hoạt tại một mốc tính từ dữ liệu của một đối tượng".
- Gặp: UC-006 (60 phút trước giờ xuất bến, trên đặt chỗ qua điện thoại) và UC-014 (15 phút trước giờ xuất bến) do ACT-10 kích hoạt, nhưng mốc tính từ giờ xuất bến của chuyến (UC-012 tạo), không phải từ đối tượng UC-002 tạo. Hạn giữ chỗ 10 phút của UC-002 do tác nhân "-" (EV-03), thuộc thời hạn nội bộ.
- Xử lý: kết luận UC-002 không có message hẹn mốc, ghi lý do ở Vấn đề còn mở. Ranh giới "vé phát hành sau mốc UC-014" chờ Q-11 (đã có sẵn).

18. Sequence diagram không có message từ boundary tới actor chính cho phần hiển thị
- Vị trí: F6 "Boundary ... Được (actor của nó)" và F5 "Message từ actor tới boundary mô tả hành động của actor".
- Gặp: không có hướng dẫn việc hiển thị kết quả cho actor có vẽ thành message từ boundary tới actor không. Vẽ thì thêm khoảng 10 message nữa.
- Xử lý: không vẽ message hiển thị tới actor chính; message "// showTrips" ... từ control tới boundary đại diện cho việc hiển thị. Riêng actor phụ Cổng SMS có message từ SmsGateway vì đó là trao đổi dữ liệu thực sự.

## Target không đạt hoặc đạt một phần

- Target 14: đạt một phần (vướng mắc 13).
- Ngưỡng F5 cho SD1: không đạt (vướng mắc 1); không nằm trong 16 mục Target nhưng ghi vào Vấn đề còn mở của artifact.
- Các mục Target 1 đến 13, 15, 16: đạt. Target 1 và 2 đạt với ghi chú vướng mắc 10 (Dữ liệu vào 1).
