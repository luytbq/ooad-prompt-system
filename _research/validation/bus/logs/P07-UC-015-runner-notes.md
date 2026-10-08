# Nhật ký người chạy P07-UC-015

Model: Sonnet (tham số model sonnet của công cụ Agent).

Tham số: UC_ID = UC-015 Soát vé lên xe; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có. Đầu ra: P07-uc-analysis/UC-015-check-boarding-ticket-analysis.md, diagrams/P07-sequence-UC-015.drawio (SD1, SD2), diagrams/P07-communication-UC-015.drawio, diagrams/P07-class-UC-015.drawio. Ba file .drawio qua kiểm tra XML hợp lệ (xml.dom.minidom), ID cell không trùng, toạ độ bội số 10 (trừ offset con của ngăn lớp), không có hai node cách nhau dưới 40 trong communication và VOPC.

Kết quả tự kiểm tra Target: 1 đến 8, 10 đến 13, 15, 16 đạt (Target 15 không áp dụng vì UC-015 không có thời hạn nội bộ và không tạo, đổi, kết thúc mốc của tác nhân thời gian). Target 9 và 14 đạt một phần, lý do ở mục 4 và 5 bên dưới.

## 1. Mâu thuẫn A3 và F6 về thao tác vật lý trên thiết bị

- Vị trí: A3 "Thao tác vật lý đi vào hệ thống qua boundary thiết bị"; F6 "Boundary chỉ trao đổi với actor của nó"; F6 bảng "Actor | Boundary: Được".
- Gặp gì: bước 3 do ACT-05 Phụ xe quét, bước 4 do ACT-09 Đầu quét đọc. ACT-05 đã có boundary riêng (CheckBoardingTicketForm) nhưng thao tác quét diễn ra trên đầu quét, thuộc boundary BarcodeScanner của ACT-09. Nếu vẽ ACT-05 --> BarcodeScanner thì vi phạm câu F6; nếu không vẽ thì bước 3 không có message.
- Xử lý: một message readBarcode từ ACT-09 tới BarcodeScanner mang cả bước 3 và 4 (ASM-53), không vẽ message ACT-05 --> BarcodeScanner; đề xuất sửa P04 gộp bước 3, 4. Prompt không có ví dụ cho trường hợp tác nhân chính thao tác vật lý trên thiết bị của tác nhân phụ.

## 2. Quy tắc "mỗi luồng cần vẽ một trang" và "luồng ngắn vẽ cùng sơ đồ"

- Vị trí: mục 2 bảng đầu ra "mỗi luồng cần vẽ một trang"; A6 "Luồng thay thế ngắn (1-3 message khác biệt) vẽ trong cùng sơ đồ bằng combined fragment"; F5 ngưỡng "khoảng 30 message".
- Gặp gì: ba câu cho kết quả khác nhau với 3a, 5a, 5b, 5c, 10a. Đưa hết vào SD1 thì khoảng 43 dòng (32 của SD1 cộng 11 của SD2), vượt ngưỡng.
- Xử lý: 10a (2 message) vào SD1; 3a, 5a, 5b, 5c ra SD2 (alt lồng nhau, ref về SD1). Hệ quả: communication diagram không có 3a, 5a, 5b, 5c (F7 chỉ gộp luồng đã gộp vào SD1). Chưa rõ ngưỡng 30 tính có hay không có message trả về; đếm không kể trả về (SD1: 23 message, 32 dòng) theo cách các file P07 đã có.

## 3. Cách đánh STT khi hai nhánh cùng dẫn tới một chuỗi message

- Vị trí: F5c "STT: đánh số phân cấp... message con được gửi trong khi xử lý message cha. Luồng thay thế trong fragment dùng tiếp số của luồng chính".
- Gặp gì: checkTicket được gọi từ hai boundary (BarcodeScanner ở nhánh quét, Form ở nhánh 3a); các message kiểm tra (findTicket...) sau đó là con của message nào thì không xác định. Nhãn kiểu 2.1.2a, 2.1.3b, 2.1.3c cho luồng thay thế không có quy tắc, phải theo tiền lệ UC-013 (1.1.1a).
- Xử lý: các message kiểm tra mang STT 2.1.1, 2.1.2... như con của 2.1 (nhánh quét), SD2 giữ nguyên STT đó cho nhánh 3a (2a.1 gọi cùng chuỗi). Chấp nhận lệch nhẹ về phân cấp ở nhánh 3a.

## 4. Lọc danh từ: danh sách có phải entity không, giá trị Kết luận thiếu

- Vị trí: A4 "Loại - là cấu trúc cài đặt (ví dụ 'bảng', 'file', 'danh sách', 'form')"; F3.2 ví dụ sai "danh sách phòng trống --> Entity RoomList"; F3.2 danh sách giá trị cột Kết luận.
- Gặp gì: "danh sách hành khách của chuyến" vừa là thuật ngữ glossary (GL-05) vừa có dạng "danh sách". Phiên soát vé (GL-28) và kết quả chưa gửi khi mất sóng cũng chưa rõ là entity hay trạng thái. Các giá trị tính (số vé còn hiệu lực, số vé đã soát) và "kết quả soát vé" không có giá trị Kết luận khớp hẳn.
- Xử lý: TripPassengerList và TicketCheckSession làm entity (ASM-50, ASM-51), hỏi Q-73, Q-74; số vé đếm ghi "Loại - thuộc tính của TripPassengerList"; "kết quả soát vé" ghi "Loại - thao tác hoặc sự kiện"; lý do không hợp lệ ghi "Loại - thuộc tính của kết quả soát vé" (X không là lớp). Prompt không nói khi nào danh sách có định danh nghiệp vụ thì được là entity, và không có giá trị cho "giá trị tính, không lưu".
- Target 9 đạt một phần: Seat chỉ có getSeatCode, getRouteAndDepartureTime của Trip chỉ cung cấp dữ liệu, Route chỉ có checkRouteMatches; đặc tả không nêu hành vi nào khác.

## 5. Tiêu chí hình học: sequence và communication

- Vị trí: C7.3 "cạnh không cắt qua node"; F10 "message đầu tiên ở y=120, mỗi message sau cách 40"; F10 style fragment.
- Gặp gì: message sequence luôn đi qua lifeline ở giữa; fragment phủ lifeline. F10 không nói cách vẽ đường ngăn toán hạng alt, fragment ref, message tự gọi, khoảng chừa cho nhãn fragment. Message đầu trang có fragment không thể ở y=120 và cách đúng 40.
- Xử lý: theo tiền lệ UC-013 (cell text cho guard toán hạng 2 và đường ngăn nét đứt; self-call dùng Array points); SD2 bắt đầu message ở y=160; quanh fragment cách 50 hoặc 80. Target 14 đạt một phần: nhãn link dài của communication có thể chồng lên nhau khi mở bằng draw.io, chưa kiểm bằng hình.
- F7 chỉ nói "mỗi cặp đối tượng một link", không nêu link tự gọi: dùng link tự gọi LK-06 (tiền lệ UC-013), không đưa vào VOPC.

## 6. Thuộc tính và trách nhiệm của lớp tái dùng

- Vị trí: F3.4 "Chỉ ghi trách nhiệm được dùng trong use case này; lớp tái dùng không chép lại trách nhiệm của use case khác".
- Gặp gì: quy tắc chỉ nói về trách nhiệm, không nói về thuộc tính của lớp tái dùng, và không nói cách thêm thuộc tính mới vào lớp đã có (Ticket cần checkedTime, vì vé đã soát chưa có chỗ ghi trong UC-002, UC-008, UC-013). Cũng không rõ Trip.findTrip tái dùng tên của UC-013 nhưng nguồn ghi "Tái dùng từ UC-002".
- Xử lý: ghi các thuộc tính dùng ở UC-015 (kể cả checkedTime mới), cột Mới hoặc tái dùng "Tái dùng từ UC-002, bổ sung trách nhiệm", ghi chú tên findTrip lấy từ UC-013. Trạng thái "đã soát" suy ra từ checkedTime, không thêm giá trị vào status.

## 7. Biên giữa máy soát vé và phần còn lại của hệ thống

- Vị trí: A2 "Không nêu công nghệ"; A6 "Mọi bước hệ thống... phải có ít nhất một message"; đầu vào P04 bước 10, 10a.
- Gặp gì: bước 10 "Gửi kết quả ... từ máy soát vé về dữ liệu vé của hệ thống" và 10a "tự gửi khi máy có sóng trở lại" là trao đổi giữa hai phần nội bộ (ASM-01), không có tác nhân. Không có lớp nhận phía hệ thống nào đủ căn cứ, và việc tự gửi diễn ra sau khi use case kết thúc.
- Xử lý: message sendResult tới TicketCheckSession; 10a là message tự gọi keepResultPending; không có lớp nhận; việc tự gửi lại ghi ASM-52; hỏi Q-74 về tác dụng của kết quả; đề xuất sửa P04 bước 10. Prompt không có hướng dẫn cho hành vi nội bộ giữa hai phần của cùng hệ thống.

## 8. Khối lượng ngữ cảnh

- Đầu vào theo mục 3 gồm 3 file P07 đã có (khoảng 200 KB), P05 (37 KB), P06 (29 KB), P02 (56 KB), prompt (47 KB). Không đọc hết P02, P05, P06; chỉ đọc các dòng liên quan UC-015 (grep theo GL, NFR, UC-015). Prompt yêu cầu "đọc toàn bộ" nhưng với 3 file P07 trước thì không khả thi nếu đọc toàn văn; đã đọc các bảng F3.4, F4, F7, F8 và mục Câu hỏi mở, Giả định của các file P07 để lập sổ AC và số Q, ASM lớn nhất (Q-72, ASM-49).

## 9. Các điểm nhỏ

- F2 "mỗi ô bổ sung tối đa 3 câu": ô bước 5 phải gói ba kiểm tra (đúng chuyến, huỷ, soát) và thứ tự (Q-47) vào 3 câu nên câu dài.
- F9 chỉ đòi mỗi bước hệ thống có một dòng; vẫn ghi cả bước do tác nhân (1, 3, 3a, 4, 8, 9) để đủ truy vết; bước 8 chỉ có fragment loop, không có message.
- Multiplicity chỉ rõ một đầu (R-UC015-08, R-UC015-11) ghi dạng "A - B 1" theo tiền lệ UC-008; F8 không nêu cách ghi một đầu.
- Ba quan hệ VOPC (R-UC015-09, 10, 11) không có link F7 nhưng có căn cứ glossary (GL-05, GL-28, ASM-32); F8 cho phép "bằng chứng từ đặc tả" nhưng không nói rõ glossary có tính là bằng chứng không.
