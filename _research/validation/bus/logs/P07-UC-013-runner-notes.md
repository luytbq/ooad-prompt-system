# Nhật ký người chạy P07-UC-013

Model: Sonnet (tham số model sonnet của công cụ Agent).

Tham số: UC_ID = UC-013 Huỷ chuyến; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có. CHE_DO_GIA_DINH = CO_NHAN, MUC_CHI_TIET = DAY_DU, HAU_TO_TEN_LOP = Mặc định.

Đầu ra: P07-uc-analysis/UC-013-cancel-trip-analysis.md; diagrams/P07-sequence-UC-013.drawio (4 trang SD1 đến SD4), P07-communication-UC-013.drawio (COMM1), P07-class-UC-013.drawio (VOPC1). Cả ba file .drawio qua kiểm tra XML hợp lệ. Số liệu: 9 lớp (3 boundary, 1 control, 5 entity; 6 tái dùng, 3 mới), 35 dòng message ở SD1 (28 không kể trả về), 9 quan hệ VOPC, Q-71 đến Q-72, ASM-47 đến ASM-49.

## Kết quả tự kiểm tra theo Target

| Target | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | Bước 5a và 6a không có message riêng vì P04 ghi "-"; thể hiện bằng fragment opt FR1, FR3 ở SD1 và dòng trong F4, F9 |
| 2 | Đạt | Message cancelTripTriggers truy về bước 5 và quy tắc A2 (xem mục 1 dưới đây) |
| 3 đến 8 | Đạt | |
| 9 | Đạt một phần | Refund chỉ có createRefund, Route chỉ có checkRouteMatches; ghi vào Vấn đề còn mở |
| 10 đến 13 | Đạt | |
| 14 | Đạt một phần | Message sequence đi qua lifeline ở giữa nên không thoả "cạnh không cắt qua node"; ghi vào Vấn đề còn mở. Communication và VOPC được kiểm tra bằng script (bội số 10, khoảng cách node tối thiểu 40, cạnh không cắt node, không chồng cạnh) |
| 15 | Đạt | Cần thêm message huỷ mốc, xem mục 1 |
| 16 | Đạt | |

## Vướng mắc

### 1. Mâu thuẫn giữa "không thêm chức năng mới" và quy tắc mốc thời gian

- Vị trí: A2, "Mô tả bổ sung chỉ làm rõ điều đã có trong đặc tả, BR, glossary. Không thêm chức năng mới." và "use case làm mốc thay đổi hoặc mất hiệu lực (trả sách, gia hạn) có trách nhiệm hẹn lại hoặc huỷ mốc"; Target 15.
- Gặp: P04 UC-013 không nêu việc huỷ mốc 60 phút (UC-006) và 15 phút (UC-014), nhưng chuyến bị huỷ làm hai mốc này mất ý nghĩa. Quy tắc A2 và Target 15 đòi có message huỷ mốc.
- Xử lý: thêm message tự gọi "// cancelTripTriggers" của control (2.1.2) ở bước 5, ghi ASM-47, hỏi Q-71, đề xuất sửa P04 và ghi vào Vấn đề còn mở theo C9. Ngoài ra prompt không nói "đối tượng làm mốc" là chuyến (UC-012 hẹn) hay đặt chỗ (UC-004 hẹn); ở đây UC-013 huỷ cả hai nên không phân biệt được, nhưng với use case chỉ đổi một trong hai thì sẽ mơ hồ.

### 2. Danh sách giá trị cột Kết luận ở F3.2 quá hẹp

- Vị trí: F3.2, "Cột Kết luận chỉ nhận một trong các giá trị: ...".
- Gặp: (a) "Lịch chạy" là tập các Trip do UC-012 xếp, chỉ được nhắc tới; (b) "lần đặt đang giữ chỗ" do UC-002 tạo, không phải use case được include hoặc extend; (c) số liệu tổng hợp hiển thị (số vé, tổng số tiền hoàn, số tin nhắn) và định dạng hiển thị không khớp giá trị nào.
- Xử lý: (a) dùng "Loại - không tham gia hành vi của use case này (khái niệm của UC-012)"; (b) dùng "Loại - thuộc phân tích của UC-002" dù định nghĩa giá trị này nói về use case được include hoặc mở rộng; (c) dùng "Loại - thao tác hoặc sự kiện" cho số liệu tổng hợp và "Loại - cấu trúc cài đặt" cho định dạng, danh sách. Ghi vào Vấn đề còn mở.

### 3. Ngưỡng 30 message của F5 không nói có tính message trả về không

- Vị trí: F5, "một trang tối đa khoảng 30 message và tối đa 3 fragment ở mức ngoài cùng".
- Gặp: SD1 có 35 dòng gồm 7 message trả về (28 không kể trả về). Prompt vừa gọi "message trả về" là một loại message trong bảng, vừa nói message trả về không xuất hiện trên communication diagram.
- Xử lý: đếm không kể trả về (28), không tách luồng chính để giữ communication diagram cùng phạm vi với SD1; ghi vào Vấn đề còn mở.

### 4. Không có hướng dẫn cho thao tác lặp "với từng X" và lifeline đại diện nhiều đối tượng

- Vị trí: A6 và F5 (chỉ nhắc fragment loop "ghi guard hoặc số lần"); P04 UC-013 dùng "với từng vé" ở bước 6 đến 10.
- Gặp: không rõ có nên nhóm theo từng vé (bước 6 đến 9 cho một vé rồi sang vé khác) hay theo từng bước (bước 6 cho mọi vé rồi bước 7 cho mọi vé); và lifeline :Ticket đại diện một vé hay mọi vé. Cách nhóm theo từng vé làm mất thứ tự bước giữa các vé; thêm nữa bước 8a/9 trong vòng lặp tạo nhiều fragment lồng nhau.
- Xử lý: dùng loop FR2 cho bước 6 đến 9 và loop FR4 cho bước 10 (SMS sau mọi hoàn tiền), message đọc ghi nhiều đối tượng cùng loại ghi "(từng vé ...)" không vẽ loop theo tiền lệ UC-002. Fragment ngoài cùng của SD1 chỉ còn 1 (opt FR1) nhờ lồng.

### 5. Luồng thay thế tiếp tục (8a) có message giống bước chính, chỉ khác tham số

- Vị trí: F5, "Luồng thay thế ngắn (1-3 message khác biệt) vẽ trong cùng sơ đồ bằng combined fragment alt, opt hoặc break" và "alt có ít nhất hai toán hạng".
- Gặp: luồng 8a (ghi khoản hoàn chưa thành công) và bước 9 (ghi khoản hoàn) cùng dùng recordRefund và createRefund, chỉ khác kết quả. Vẽ alt trong SD1 phải lặp cả hai message ở hai toán hạng và lifeline Refund bị tạo hai lần ở hai toán hạng, mâu thuẫn với "đỉnh lifeline đặt ngang message Tạo".
- Xử lý: đưa 8a sang trang SD4 (alt, toán hạng 2 là fragment ref tới SD1) và để SD1 chỉ có recordRefund chung. Prompt không nêu cách xử lý khi cùng một đối tượng được tạo ở hai nhánh alt.

### 6. Bố cục y=120 và khoảng cách 40 mâu thuẫn với nhãn fragment

- Vị trí: F10, "message đầu tiên ở y=120, mỗi message sau cách 40; fragment là hình chữ nhật ... nhãn toán tử ở góc trên trái".
- Gặp: fragment mở ngay đầu trang (SD2, SD3, SD4) và các fragment lồng nhau cần chỗ cho nhãn và đường ngăn toán hạng; không thể giữ y=120 và 40 cho mọi message.
- Xử lý: tăng khoảng cách quanh fragment (mở fragment cộng 40, đóng fragment cộng 30), message đầu tiên của trang có fragment mở đầu ở y=160; mọi toạ độ vẫn là bội số 10. Ghi vào Vấn đề còn mở.

### 7. Quy định về ID dòng toán hạng alt và link tự gọi không có trong prompt

- Vị trí: F5 b) "Fragment: nhãn ghi toán tử ... và guard"; F7 "Mỗi cặp đối tượng có trao đổi được nối bằng đúng một link".
- Gặp: prompt không nói toán hạng thứ hai của alt có dòng riêng trong bảng Node không, ID thế nào; không nói message tự gọi (cancelTripTriggers) có link riêng trong communication diagram và có vào VOPC không.
- Xử lý: theo tiền lệ của P07 UC-002, UC-008 đã có (đọc như đầu vào): dòng Fragment ID "<trang>-FR<n>-O2" kèm cạnh ngăn "-O2-SEP"; link tự gọi vẽ thành một link (LK-07) từ đối tượng tới chính nó, không vào VOPC. Nếu không có hai file đó, người chạy phải tự đoán.

### 8. Số liệu tổng hợp ở bước 11 không có lớp sở hữu

- Vị trí: A5 "Mặc định một control cho mỗi use case ... không giữ dữ liệu nghiệp vụ lâu dài" và Target 9 (god control).
- Gặp: Dữ liệu ra 3 gồm số vé theo từng kết quả hoàn, số tin nhắn, danh sách mã vé hoàn không thành công. Giao cho entity thì phải thêm lớp tổng hợp không có định danh; giao cho control thì có nguy cơ coi là logic.
- Xử lý: control giữ tạm kết quả từ các message trả về trong một lần thực hiện, truyền thẳng vào showCancelTripResult; ghi lý do ở F4 và đề xuất P04 xem lại (Đề xuất sửa artifact trước). Prompt không nêu cách xử lý số liệu tổng hợp chỉ dùng để hiển thị.

### 9. Thiếu entity cho khái niệm chưa có P07: đặt chỗ qua điện thoại

- Vị trí: A4 "Tra sổ đăng ký AC và glossary để tái dùng mã"; A1 chỉ có quy tắc đặt mã tạm cho use case include, extend.
- Gặp: PhoneReservation (GL-07) chưa có mã vì UC-004, UC-005, UC-006 chưa có P07, nhưng UC-013 cần đọc và huỷ nó. Prompt không có quy tắc đặt mã cho entity sẽ được use case khác dùng.
- Xử lý: cấp mã AC-E-PhoneReservation, trạng thái "Mới", ghi vào Vấn đề còn mở để UC-004, UC-006 tái dùng đúng mã. Quan hệ Trip và PhoneReservation (multiplicity A 1 - B 0..*) suy từ GL-07, không có bằng chứng nào cho phía còn lại.

### 10. Mã Q và ASM chỉ đọc trong thư mục cùng bước

- Vị trí: C3, "Bước chạy lặp nhiều lần ... đọc thêm mục Câu hỏi mở và Giả định của các file cùng bước đã có trong thư mục đầu ra và cấp tiếp từ số lớn nhất trong đó".
- Gặp: số lớn nhất trong các file P07 là Q-70 và ASM-46, nên cấp Q-71, ASM-47. Các đặc tả P04 khác (ví dụ UC-015) nằm ngoài danh sách đầu vào của lần chạy này và có thể đã cấp số lớn hơn; không kiểm tra được vì ngoài phạm vi đọc.
- Xử lý: lấy số lớn nhất trong mọi đầu vào được đọc (P01 đến P06, P04 UC-013, P07 đã có) rồi cấp tiếp. Nguy cơ trùng mã với artifact không được đọc vẫn còn.

### 11. Khác biệt ý nghĩa của khoản hoàn giữa hai use case

- Vị trí: F3.4, "lớp tái dùng không chép lại trách nhiệm của use case khác (P08 sẽ gộp)".
- Gặp: AC-E-Refund của UC-008 chỉ tạo khi hoàn thành công (ASM-46), của UC-013 tạo cả khi chưa thành công và chờ tiền mặt. Cùng một mã AC và cùng trách nhiệm createRefund nhưng ngữ nghĩa kết quả hoàn khác nhau; prompt không có cột hay cách đánh dấu khác biệt ngữ nghĩa khi tái dùng.
- Xử lý: ghi ASM-48 và đề xuất P08 gộp (Đề xuất sửa artifact trước, dòng P07 UC-008).

### 12. Ghi chú về phạm vi đọc

- Thư mục scratchpad của phiên có nhiều file từ các lần chạy khác (tên file hiển thị khi liệt kê thư mục). Không đọc file nào trong đó; các script sinh tài liệu của lần chạy này đặt trong thư mục con riêng.
