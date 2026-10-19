Model của phiên chạy: Sonnet

# Nhật ký người chạy - P07 cho UC-010 Đặt chỗ lớp nhóm

Đầu ra: design/P07-uc-analysis/UC-010-book-class-spot-analysis.md; design/diagrams/P07-sequence-UC-010.drawio (2 trang SD1a, SD1b), P07-communication-UC-010.drawio (1 trang), P07-class-UC-010.drawio (1 trang). Q mới: Q-83, Q-84 (Q lớn nhất sau lần chạy: Q-84; chưa có ASM). 6 lớp phân tích (1 boundary, 1 control, 4 entity), 7 quan hệ VOPC, 23 message không kể message trả về (SD1a 11, SD1b 12).

Cách kiểm tra: ba file .drawio qua xml.dom.minidom hợp lệ; script riêng kiểm tra ID duy nhất, toạ độ bội số 10 (trừ x=-1, x=1 của nhãn multiplicity theo C7.3), tham chiếu nguồn, đích tồn tại, không chồng node ở communication và VOPC. Không có công cụ dựng hình nên bố cục chưa được xem bằng mắt; Target 14 chỉ kiểm được về cấu trúc và toạ độ.

Kết quả Target: mục 1 đạt (bước 7a2a không có hành động hệ thống nên không có message, ghi ở Vấn đề còn mở); mục 12 đạt theo cách hiểu GON không phải DAY_DU (xem mục 9 dưới đây); các mục còn lại đạt. Không có mục Không đạt nào.

## Các vướng mắc

### 1. Quy tắc loop của A6 không áp dụng được cho phép đếm, và ngưỡng 3 fragment ép tách trang

- Vị trí: A6 "đối tượng toàn thể gửi message tới từng phần tử trong loop [mỗi <phần tử>]"; F5 "tối đa 3 fragment ở mức ngoài cùng".
- Gặp gì: UC-010 có hai phép đếm trên tập (số chỗ đã đặt của lớp ở bước 7, số lớp hội viên đã đặt trong ngày ở bước 6). Phần tử ClassBooking không có dữ liệu hay hành vi nào để trả lời từng message, nên loop chỉ sinh message vô nghĩa ("// confirmActive"). Nếu vẽ loop cho cả hai phép đếm cộng loop lịch lớp ở bước 2, thêm break 4a, alt 5, alt 6, break 7a thì có 7 fragment ở mức ngoài cùng.
- Xử lý: đặt phép đếm vào hai entity toàn thể (Member, GroupClass) như trách nhiệm nội bộ, không vẽ message tới ClassBooking, ghi lý do ở Vấn đề còn mở; quan hệ VOPC tương ứng lấy căn cứ GL-05, BR-08, BR-11. Loop duy nhất giữ lại là loop lịch lớp ở bước 2 vì control phải lặp (không có đối tượng toàn thể). Luồng chính tách thành SD1a và SD1b để mỗi trang có 3 fragment. Prompt không nói phép đếm thuần tuý có phải vẽ loop hay không.

### 2. Không rõ fragment ref và fragment lồng có tính vào ngưỡng 3 fragment ở mức ngoài cùng không

- Vị trí: F5 "tối đa 3 fragment ở mức ngoài cùng"; "trang riêng bắt đầu bằng fragment ref tới sơ đồ luồng chính".
- Gặp gì: trang SD1b bắt đầu bằng ref, kèm alt 6a và break 7a (trong đó có alt lồng cho 7a2, 7a2a). Không rõ ref có tính, và alt lồng trong break có tính không.
- Xử lý: tính ref là một fragment, không tính fragment lồng; SD1b có đúng 3. Nếu cách hiểu khác thì phải tách thêm trang.

### 3. Luồng kết thúc có nhánh kết thúc con (7a và 7a2a)

- Vị trí: F5 b) "break đặt trực tiếp trong interaction của trang (mức ngoài cùng), không lồng trong toán hạng của alt, opt, loop, par"; Target 15.
- Gặp gì: luồng 7a kết thúc use case, trong đó 7a2a (hội viên không yêu cầu vào danh sách chờ) lại là một nhánh kết thúc khác, không có hành động hệ thống. Prompt chỉ nói break không lồng trong alt, không nói alt lồng trong break, và không nói cách vẽ toán hạng không có message.
- Xử lý: break 7a ở mức ngoài cùng, bên trong là alt hai toán hạng (7a2 và 7a2a); toán hạng 7a2a chỉ có ghi chú "Kết thúc use case (thất bại)" và được chừa một khoảng chiều cao.

### 4. Bảng Node của sequence thiếu loại Note; bảng message thiếu cột ID

- Vị trí: F5 b) "| ID | Loại (Actor / Lifeline / Fragment) | ..."; F5 c) "| STT | Từ | Đến | Message | ... |"; F5 c) "ghi note 'tiếp tục luồng chính'... ghi note 'quay lại bước K'"; C7.3 "ID của mxCell trùng hoặc suy ra được từ ID trong bảng mô hình".
- Gặp gì: F5 yêu cầu note nhưng bảng Node chỉ có ba loại; bảng message không có cột ID mà C7.3 đòi ID cell khớp bảng.
- Xử lý: thêm loại Note vào bảng Node (đặt note ở lề phải, shape=note theo C7.3); quy ước ID message là <mã trang>-M-<STT>, message trả về thêm -R, ghi quy ước ở đầu F5 thay vì thêm cột. Prompt nên nêu rõ hai điểm này.

### 5. Cách đánh STT khi break xen giữa luồng chính

- Vị trí: F5 c) "Luồng thay thế trong fragment dùng tiếp số của luồng chính".
- Gặp gì: sau break 7a, luồng chính vẫn có bước 8 và 9 (chạy khi break không xảy ra). Nếu "tiếp số" theo thứ tự xuất hiện trên trang thì bước 8 mang số lớn hơn message 7a nhưng thuộc cùng chuỗi 2.1; hành động của hội viên ở 7a2 là message mức đỉnh nên thành "3" trong khi bước 8 là "2.1.10", không đơn điệu theo thời gian.
- Xử lý: message break lấy số tiếp theo trong chuỗi 2.1 (2.1.9 cho 7a1), hành động hội viên 7a2 là "3", các message bước 8 và 9 giữ chuỗi 2.1 (2.1.10, 2.1.11). Ghi cách đánh số ở đầu F5. Prompt không có ví dụ cho trường hợp này.

### 6. Kiểm tra rồi lưu (bước 7 và 8) và nhánh lỗi tại bước 8

- Vị trí: đặc tả P04 mục 8 "Khi hai hội viên cùng đặt chỗ cuối cùng của một lớp, hội viên đến sau đi theo luồng 7a"; BR-11 "kể cả khi nhiều hội viên đặt chỗ cùng lúc"; F5 ngưỡng fragment.
- Gặp gì: prompt không hướng dẫn mô hình hoá việc kiểm tra và ghi phải liền mạch (check-then-act). Vẽ thêm nhánh lỗi tại bước 8 về 7a cần thêm một fragment, vượt ngưỡng 3 của SD1b.
- Xử lý: gộp kiểm tra lại và tạo chỗ đã đặt vào một trách nhiệm reserveSpot của GroupClass (F4 ghi lý do), nhánh lỗi chỉ ghi bằng note trong SD1b và nêu ở Vấn đề còn mở. Nếu muốn vẽ nhánh này thì cần quy tắc cho phép tham chiếu luồng 7a mà không tính vào ngưỡng.

### 7. F3.2 thiếu giá trị Kết luận cho một số loại danh từ

- Vị trí: F3.2 "Cột Kết luận chỉ nhận một trong các giá trị: ..."; A4 "riêng tập hợp có tên riêng trong glossary, có định danh nghiệp vụ và vòng đời riêng... có thể là entity".
- Gặp gì: (a) "lịch lớp nhóm" (GL-26) là tập hợp có tên trong glossary nhưng chưa đủ căn cứ làm entity; trong danh sách không có giá trị cho "tập hợp kết quả truy vấn", tôi buộc phải dùng "Loại - cấu trúc cài đặt", trái với việc đây là thuật ngữ nghiệp vụ. (b) "1.500 hội viên đặt chỗ cùng lúc" là tham số của NFR-01, danh sách chỉ có "tham số của quy tắc BR-nn hoặc ASM-nn"; tôi gắn tạm vào BR-11. (c) "danh sách chờ" (GL-08) thì A4 cho phép là entity nhưng vòng đời riêng là điều tôi suy ra từ UC-011 đến UC-013, không có trong UC-010; tôi giữ là entity và đặt Q-84 để người dùng xác nhận.
- Xử lý: như mô tả; đề nghị thêm giá trị cho tập hợp kết quả và cho tham số NFR.

### 8. Entity của khái niệm do use case khác quản lý nhưng chỉ đọc

- Vị trí: A4 "là khái niệm trong phạm vi nhưng không tham gia hành vi của use case này (chỉ được nhắc tới, không được đọc, ghi hay kiểm tra)"; F3.2 "Loại - thuộc tính của X"; A1 "Mới - chủ sở hữu UC-xxx".
- Gặp gì: loại lớp, phòng, huấn luyện viên là khái niệm có thuật ngữ P05 và có thể có entity riêng (Q-03, Q-04, Q-05), nhưng UC-010 chỉ hiển thị. Tương tự khoá quyền đặt lớp (GL-23) do UC-016 tạo, UC-010 chỉ đọc. Prompt không nói ngưỡng giữa "thuộc tính của lớp nhóm" và "entity chủ sở hữu UC-xxx" khi chủ sở hữu chưa chạy P07.
- Xử lý: đưa loại lớp, phòng, huấn luyện viên, sức chứa về thuộc tính của GroupClass; khoá quyền đặt lớp là thuộc tính bookingSuspension của Member theo GL-23 ("Trạng thái của một hội viên"). Ghi ở Vấn đề còn mở để P08 quyết định tách entity.

### 9. DAY_DU không được định nghĩa

- Vị trí: A6 "Khi DAY_DU: thêm mọi luồng thay thế"; F7 "Communication diagram cho luồng thay thế (chỉ khi DAY_DU)"; Target 12 "(chỉ khi DAY_DU)". Hồ sơ dự án ghi MUC_CHI_TIET là GON.
- Gặp gì: P07 dùng DAY_DU như một giá trị nhưng trong các file được phép đọc không có định nghĩa quan hệ giữa DAY_DU và các giá trị của MUC_CHI_TIET. Ngoài ra sequence diagram của tôi gộp luồng thay thế vào trang chứa bước rẽ, nên "phần sequence diagram nó thể hiện" của communication (luồng chính) có khoảng trống STT (2.1.2, 2.1.4...).
- Xử lý: coi GON không phải DAY_DU, communication chỉ gồm 13 message luồng chính, giữ nguyên STT; ghi ở Vấn đề còn mở cách mở rộng. Hệ quả: quan hệ GroupClass - Waitlist (R-UC010-05) lấy căn cứ từ sequence, không từ link communication.

### 10. Quy ước multiplicity "?" buộc phải thêm Q

- Vị trí: A8 "nếu không rõ thì ghi '?' ở phía đó (F8 b) và ghi câu hỏi hoặc giả định, không đoán"; F8 b) "Số ở phía A là số đối tượng A ứng với một đối tượng B".
- Gặp gì: ở chế độ NGHIEM_NGAT, các phía "?" cần Q. Với ClassBooking tôi dẫn được Q có sẵn (Q-22, Q-59, Q-60); với Waitlist phải tạo Q-84. Cách đọc "số ở phía A là số đối tượng A ứng với một đối tượng B" dễ nhầm với UML (nhãn đầu A ghi số A trên một B), tôi áp dụng đúng chiều UML: nhãn ở đầu nguồn (Lớp A) ghi số A trên mỗi B.
- Xử lý: như mô tả; không có vướng mắc khác.

### 11. Xung đột C7.3 với bố cục sequence

- Vị trí: C7.3 "không có hai node chồng lên nhau; cạnh không cắt qua node"; F10 "fragment là hình chữ nhật... bao các message của nó".
- Gặp gì: fragment, ghi chú và lifeline vốn chồng lên nhau trong sequence diagram; message cắt qua các lifeline ở giữa. Quy tắc không loại trừ sequence.
- Xử lý: kiểm tra không chồng chỉ với communication và VOPC; trong sequence, fragment trải suốt các lifeline, note đặt ở lề phải ngoài vùng fragment.

### 12. Trang bắt đầu bằng fragment ref lệch quy tắc y=120

- Vị trí: F10 "message đầu tiên ở y=120, mỗi message sau cách 40".
- Gặp gì: SD1b bắt đầu bằng fragment ref (cần một hàng riêng) nên message đầu tiên không thể ở y=120.
- Xử lý: fragment ref đặt ở y=100, message đầu tiên ở y=180, ghi ở cuối F5.

### 13. Gộp trách nhiệm thông báo từ chối

- Vị trí: A7 "Message giống nhau về ý nghĩa gộp thành một trách nhiệm"; F5 c) "// tênTráchNhiệm" cho từng message.
- Gặp gì: bốn thông báo từ chối (4a, 5a, 5b, 6a) khác lý do nhưng cùng ý nghĩa; UC-005 trước đó tách theo từng thông báo. Không rõ mức gộp nào là đúng.
- Xử lý: gộp thành showBookingRejectedNotice, lý do ghi trong ngoặc ở message (dữ liệu truyền đi bằng lời). showClassFullNotice (7a1) giữ riêng vì kèm đề nghị vào danh sách chờ.

### 14. Phạm vi đọc và tìm mã Q

- Vị trí: 00-Conventions.md C3 "Mã lớn nhất tìm trong mục Câu hỏi mở và Giả định của mọi artifact đã có trong THU_MUC_DAU_RA"; mục 3 của prompt "Mọi artifact trong thư mục đầu ra: Mã ở mục Câu hỏi mở, Giả định".
- Gặp gì: đề bài cho sẵn Q lớn nhất là Q-82 và tôi chỉ xác nhận bằng grep mẫu có ranh giới trên các file markdown trong design/; chưa kiểm chéo các file ngoài thư mục đầu ra. Mã quét được khớp (Q-82, chưa có ASM).
- Xử lý: cấp Q-83, Q-84 liền số.

### 15. NFR không có chỗ trong cấu trúc artifact

- Vị trí: mục 3 "P06-supplementary-spec.md | Các BR, NFR có UC_ID ở cột áp dụng"; Format không có mục nào cho NFR.
- Gặp gì: NFR-01 (1.500 hội viên đặt chỗ cùng lúc) áp dụng cho UC-010 nhưng P07 không có chỗ ghi nhận hay quy tắc cho thấy NFR ảnh hưởng thế nào tới lớp phân tích.
- Xử lý: trích NFR-01 ở cột Nguồn của F2 bước 8, giải thích ở Vấn đề còn mở rằng cơ chế thuộc P09 và P12.
