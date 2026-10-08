# Nhật ký người chạy P07-UC-008

Model: Sonnet (tham số model sonnet của công cụ Agent).

Phạm vi: chạy P07 cho UC-008 Trả vé (UC_ID = UC-008 Trả vé; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có). Đầu ra: P07-uc-analysis/UC-008-return-ticket-analysis.md, diagrams/P07-sequence-UC-008.drawio (5 trang), P07-communication-UC-008.drawio, P07-class-UC-008.drawio. Ba file .drawio đã kiểm tra bằng xml.dom.minidom, hợp lệ; toạ độ bội số 10 (trừ toạ độ con tương đối trong ngăn lớp). Cấp tiếp mã: Q-70, ASM-45, ASM-46.

## Vướng mắc

1. Một boundary cho mỗi cặp (tác nhân, use case) so với P04 gộp hai tác nhân chính
- Vị trí: F3.1 "Quy tắc: một boundary cho mỗi cặp tác nhân và use case"; Target 3 "Mỗi tác nhân tương tác trực tiếp ... có đúng một boundary"; F3.1 Mức hợp lý "số boundary bằng số tác nhân tham gia".
- Gặp: P04 UC-008 ghi "Hành khách / Nhân viên bán vé" chung một cột cho bước 1 và 6, luồng chính viết cho hành khách, khác biệt ACT-02 chỉ ở 3a và 7a. Prompt không nói cách xử lý use case có hai tác nhân chính dùng chung luồng.
- Xử lý: hai boundary (ReturnTicketForm cho ACT-01, CounterReturnTicketForm cho ACT-02), một control chung. Hệ quả: SD1 chỉ vẽ ACT-01, phải thêm SD5 cho ACT-02. Hai boundary có danh sách trách nhiệm giống hệt nhau (11 dòng), nhìn như trùng lặp. Prompt không có hướng dẫn đặt tên hai boundary cùng use case (quy tắc đặt tên chỉ nói "theo hành động của use case"), tôi tự chọn tiền tố Counter.

2. Communication diagram chỉ theo SD1, luồng của tác nhân thứ hai không có chỗ đứng
- Vị trí: F7 "phạm vi là luồng chính của sơ đồ SD1"; F8 "Mỗi link trong F7 giữa hai lớp khác nhau sinh một quan hệ"; A8 "Không có quan hệ nào trong VOPC mà không có link hoặc bằng chứng từ đặc tả".
- Gặp: CounterReturnTicketForm chỉ xuất hiện ở SD5 nên không có link trong F7; quan hệ R-UC008-02 (CounterReturnTicketForm - ReturnTicketController) chỉ có bằng chứng bước UC và SD5. Prompt không nói luồng chính của tác nhân thứ hai (biến thể của luồng chính, không phải luồng thay thế) có vào communication diagram hay không; F7 chỉ nói "luồng thay thế đã gộp".
- Xử lý: giữ communication diagram theo SD1, ghi lý do ở Vấn đề còn mở, lấy bằng chứng R-UC008-02 từ SD5 và bước UC.

3. Phần luồng 7a: không có hành động, không có message
- Vị trí: Target 1 "Mọi bước hệ thống ... có ít nhất một message"; F5 "mọi bước hệ thống phải có ít nhất một message".
- Gặp: P04 luồng 7a có Thực hiện bởi "-", Hành động "-" (chỉ rẽ nhánh sang bước 10). Không có hành động để thành message. Prompt không có mục xử lý bước rẽ nhánh rỗng.
- Xử lý: biểu diễn bằng fragment opt bỏ qua nhánh hoàn qua cổng ở SD1, và ghi chú ở SD5 (return message 2c.1.1 gắn bước 7a). Ghi vào Vấn đề còn mở.

4. Ngưỡng F5 và quy tắc bố cục F10 mâu thuẫn khi có fragment
- Vị trí: F10 "message đầu tiên ở y=120, mỗi message sau cách 40"; F5 "tối đa 3 fragment ở mức ngoài cùng"; C7.3 "cạnh không cắt qua node".
- Gặp: fragment cần chỗ cho nhãn ở góc trên trái, alt cần chỗ cho đường ngăn toán hạng và guard của toán hạng 2; không thể vừa giữ y=120 và cách đúng 40 vừa tránh đè nhãn. Trong sequence diagram message luôn đi qua lifeline ở giữa và fragment phủ lên lifeline, mâu thuẫn C7.3 (giống ghi nhận ở P07 UC-002).
- Xử lý: trang có fragment bắt đầu message đầu tiên thấp hơn; khoảng cách quanh fragment là 80 hoặc 60. Ghi ở Vấn đề còn mở (Target 14 đạt một phần).

5. Luồng 2a "Quay lại bước 1" và việc phải lặp message ở toán hạng thứ hai của alt
- Vị trí: F5 "alt có ít nhất hai toán hạng ... mỗi toán hạng có guard"; "Luồng thay thế trong fragment dùng tiếp số của luồng chính".
- Gặp: luồng 2a không kết thúc use case nên dùng alt, nhưng prompt không nói toán hạng thứ hai chứa gì khi luồng chính không có message ở vị trí đó. Tôi lặp message 1.1.2 của luồng chính vào toán hạng 2 (như UC-002 đã làm). Quy tắc đánh STT cho luồng thay thế ở trang riêng ("dùng tiếp số của luồng chính") không rõ khi message thuộc nhánh khác; tôi dùng STT của message cùng điểm rẽ nhánh kèm hậu tố a, và hậu tố c cho biến thể của ACT-02.

6. Sổ AC và thuộc tính/ý nghĩa trách nhiệm tái dùng
- Vị trí: F3.4 "Cùng khái niệm đã có mã ở use case khác thì dùng lại đúng mã"; "Chỉ ghi trách nhiệm được dùng trong use case này"; A7 "Message giống nhau về ý nghĩa gộp thành một trách nhiệm".
- Gặp: AC-E-Seat // release của UC-002 nghĩa là trả chỗ đang giữ khi hết hạn giữ chỗ (BR-08); UC-008 cần chuyển chỗ của vé đã trả về còn trống (BR-03, ASM-20). Hai ý nghĩa gần nhau nhưng không giống hẳn; prompt không nói khi nào tách tên. Tôi dùng lại tên release và ghi vào Vấn đề còn mở cho P08. Tương tự, thêm thuộc tính purchaseChannel cho AC-E-Ticket mà UC-002 không có.
- Gặp thêm: AC-B-PaymentGateway. UC-002 ghi boundary của ACT-06 thuộc P07 của UC-003 (chưa chạy), còn UC-008 có ACT-06 tương tác trực tiếp; A3 nói boundary của tác nhân chỉ thuộc use case được include hoặc extend thì thuộc UC đó, nhưng UC-008 không include UC-003. Tôi đặt mã tại UC-008 và để UC-003 tái dùng; prompt không có quy tắc cho trường hợp hai use case độc lập cùng dùng một hệ thống ngoài mà use case thứ hai chưa chạy.

7. Entity thiếu trách nhiệm và chỗ đặt phép tính
- Vị trí: F3.4 "Entity chỉ có trách nhiệm dạng get/set là entity thiếu trách nhiệm"; A6 Creator, Information Expert.
- Gặp: khoản hoàn tiền (Refund, GL-16) chỉ được ghi nhận ở bước 10 (ASM-21 của P04: không ghi khoản hoàn khi hoàn thất bại) nên phép tính số tiền hoàn ở bước 4 không thể giao cho Refund chưa tồn tại; giao cho Ticket. Refund chỉ còn createRefund. Prompt không có hướng dẫn chọn giữa tạo đối tượng entity tạm sớm hay giao phép tính cho entity khác; tôi chọn Ticket và ghi nhận Refund mỏng (Target 9 đạt một phần). Seat cũng mỏng (getSeatCode, release).
- Gặp thêm: kênh yêu cầu trả (BR-11) không có trong Dữ liệu vào 1 của P04; xử lý bằng ASM-45, Q-70 và đề xuất sửa P04.

8. Bộ lọc danh từ: giá trị Kết luận cố định không đủ cho vài trường hợp
- Vị trí: F3.2 "Cột Kết luận chỉ nhận một trong các giá trị".
- Gặp: "Thời điểm trả vé", "Yêu cầu hoàn tiền" (tham số hoặc message) dùng "Loại - thao tác hoặc sự kiện" cho vừa; "Phiên làm việc, xác thực" dùng "Loại - là tác nhân hoặc ngoài phạm vi"; "Thời gian còn lại trước giờ xuất bến" là giá trị suy ra, dùng "Loại - thuộc tính của Trip" cho gần nhất. Không có giá trị "giá trị suy ra", nên một số dòng chỉ gần đúng.

9. Đầu vào không khớp
- P02 Bảng 4b thiếu REQ-18, REQ-42 cho UC-008 (đã ghi ở P04 UC-008, không nhắc lại ở P07).
- P06 BR-03, BR-02 diễn đạt "chưa có vé" chặn bán lại chỗ đã trả (đã ghi ở P04 và P06); ở P07 dùng ASM-20 với "vé còn hiệu lực" cho release, không sửa artifact trước.
- Quy tắc mốc thời gian A2: UC-014 và UC-006 là use case do tác nhân thời gian kích hoạt; không có đối tượng nào mà UC-008 tạo hay đổi để buộc hẹn mốc. Điều kiện của A2 "mốc tính từ dữ liệu của một đối tượng" mơ hồ khi mốc tính từ chuyến chứ không từ vé; tôi kết luận không có message hẹn và ghi lý do.

10. Quá tải ngữ cảnh và công sức thủ công
- Prompt dài; các bảng F5, F7, F8 phải khớp nhau với file .drawio. Tôi sinh bảng và file .drawio từ cùng một mô tả dữ liệu bằng script ở thư mục tạm để không lệch; prompt khuyến nghị sinh từ bảng nhưng không nói cách. Việc tạo ID, toạ độ lifeline, vị trí fragment (y từng message, tính cả đường ngăn toán hạng) khá nhiều quy tắc phải tự suy ra, và F10 không nói cách tính chiều cao fragment và vị trí nhãn toán hạng thứ hai.

## Mục Target không đạt hoàn toàn

- Target 9: đạt một phần. Refund (createRefund) và Seat (getSeatCode, release) mỏng; lý do ở mục 7 trên và Vấn đề còn mở của artifact.
- Target 14: đạt một phần. Sequence diagram: message đi qua lifeline ở giữa và fragment phủ lên lifeline theo ký pháp UML; communication diagram có nhãn link dài, có thể chồng lên node kề (không đo bằng công cụ vẽ, chỉ kiểm bằng toạ độ). Bảng và file .drawio khớp nhau về ID, STT, số message (22 message không trả về ở SD1 và ở communication diagram).
- Target 1: đạt, kèm ghi chú về bước 7a (không có hành động) và các ref của SD5.
- Các Target còn lại (2 đến 8, 10 đến 13, 15, 16): đạt theo tự kiểm tra. Target 12 đạt với phạm vi SD1 và ghi rõ SD5 không vào communication diagram.
