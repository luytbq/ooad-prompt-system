# P08 - Nhật ký người chạy

Model: Sonnet (tham số model sonnet của công cụ Agent).

Đầu ra: design/P08-analysis-model.md, design/diagrams/P08-class-analysis.drawio (3 trang: Entity, Bán vé, Vận hành chuyến). Kết quả: 24 lớp (8 boundary, 5 control trong đó 1 tạm, 11 entity), 37 quan hệ R-01 đến R-37, 3 câu hỏi mới (Q-75 đến Q-77), 3 giả định mới (ASM-54 đến ASM-56). File .drawio hợp lệ XML (minidom) và đã kiểm tra bằng script: khoảng cách node tối thiểu 40, toạ độ bội số 10, mọi đoạn cạnh trực giao, không đoạn nào cắt vào trong node. Chưa mở bằng draw.io.

## Các vướng mắc

1. Phạm vi mâu thuẫn giữa Context và YEU_CAU_BO_SUNG.
   - Vị trí: [Context] "Phạm vi: toàn hệ thống, mọi use case có trong P02-usecases.md và nằm trong phạm vi của dự án." và A1 "liệt kê use case trong phạm vi chưa có artifact P07".
   - Gặp: đề chỉ có 4 use case có P07 trong tổng số 18 use case của P02, YEU_CAU_BO_SUNG giới hạn phạm vi 4 use case.
   - Xử lý: theo C9 chọn YEU_CAU_BO_SUNG; F1 vẫn liệt kê đủ 18 use case, 14 use case ghi "Chưa phân tích (ngoài phạm vi lần chạy theo YEU_CAU_BO_SUNG)", ghi vào Vấn đề còn mở. Prompt không nói rõ use case ngoài phạm vi theo YEU_CAU_BO_SUNG có tính là "chưa phân tích" của Target 1 hay không.

2. Quy tắc "đúng một lần" của nhật ký hợp nhất mơ hồ với lớp tái dùng.
   - Vị trí: F2 "mọi lớp của mọi P07 xuất hiện đúng một lần ở cột 'Lớp gốc'"; bảng có cột "UC nguồn" ở số ít.
   - Gặp: Trip, Ticket xuất hiện cùng mã ở 4 file P07; 24 mã duy nhất nhưng 37 dòng lớp.
   - Xử lý: chọn 37 dòng (mỗi dòng của bảng F3.4 của mỗi P07 một dòng), F3 giữ 24 dòng. Ghi trong Vấn đề còn mở. Prompt nên nói rõ đơn vị đếm là (AC, UC) hay AC.

3. Nhật ký F2 không có chỗ cho quyết định ở mức trách nhiệm, thuộc tính và cho cặp đã xét nhưng giữ tách.
   - Vị trí: A4 "Hai trách nhiệm cùng ý nghĩa, khác tên thì giữ một tên, ghi tên bị thay trong nhật ký" và A3 phép thử đồng nghĩa; F2 cột "Tình huống" chỉ có 6 giá trị, "Kết quả" chỉ nói tới lớp.
   - Gặp: cần ghi sendTicketSms và sendTripCancelSms --> sendSms, release của Seat ở UC-002 và UC-008, refundResult mâu thuẫn, và các cặp (Booking, PhoneReservation), (ReturnTicketForm, CounterReturnTicketForm).
   - Xử lý: thêm hai bảng ngoài khung F2: F2a (cặp đã xét, giữ tách) và F2b (nhật ký trách nhiệm, thuộc tính). Tình huống của lớp tái dùng cùng mã không có giá trị phù hợp, dùng "Giữ nguyên"; cho PaymentGateway, SmsGateway ở UC-013 dùng "Boundary hệ thống trùng" dù hai dòng đã cùng mã.

4. Ngữ nghĩa chiều của multiplicity "A <m> - B <m>" không rõ.
   - Vị trí: F4 "ghi dạng 'A <m> - B <m>'" và ví dụ "Appointment --> Patient: Association, A 0..* - B 1"; F5 "Multiplicity ghi ở đầu quan hệ phía lớp mà nó đếm"; P07 dùng "A - B 1..5" cho Booking - Seat.
   - Gặp: ví dụ đọc được theo hai cách (số ở phía A đếm A, hoặc số ở phía A là số A mà B có); F5 chỉ rõ nhãn ở đầu của lớp nó đếm, ví dụ Appointment 0..* ở đầu Appointment, nhất quán với UML chuẩn.
   - Xử lý: theo F5, số ở phía A đếm số đối tượng A ứng với một đối tượng B, và ghi quy ước này vào F4. Nhãn con x=-1 ở đầu nguồn (Lớp A) mang multiplicity của A. Prompt nên nêu quy ước này ngay ở F4.

5. Hợp quan hệ cùng cặp nhưng đảo chiều và multiplicity mâu thuẫn với glossary.
   - Vị trí: A5 "Hợp quan hệ trùng (cùng cặp lớp, cùng ý nghĩa)".
   - Gặp: R-UC013-07 vẽ Trip A 1 - Ticket B 0..*, R-UC002-14 vẽ Ticket A 0..* - Trip B 1 (cùng quan hệ, đảo chiều). R-UC002-13 ghi phía Booking là 1 nhưng GL-18 (lần đặt trực tuyến) và GL-13 (kênh mua tại quầy) cho thấy vé quầy không có Booking.
   - Xử lý: lấy hướng Ticket --> Trip, đảo multiplicity; sửa phía Booking thành 0..1 và ghi vào Đề xuất sửa artifact trước. Prompt không nói cách xử lý chiều khi hợp, và không nói P08 có được đổi multiplicity của P07 hay không (C1.3 chỉ cấm đổi tên, mã, bỏ phần tử).

6. Thêm quan hệ mới "Mới ở P08" chạm ranh giới bằng chứng.
   - Vị trí: A5 "Được thêm quan hệ giữa hai entity không có trong VOPC nào khi glossary, BR hoặc tài liệu nguồn cho bằng chứng"; "Không thêm quan hệ chỉ vì hiểu biết chung".
   - Gặp: GL-07 và GL-11 nói chỗ được giữ cho "một đặt chỗ qua điện thoại" nhưng không có VOPC nào nối PhoneReservation với Seat (UC-004 chưa phân tích).
   - Xử lý: thêm R-37 (PhoneReservation - Seat), phía Seat để trống kèm Q-76. Không rõ prompt có muốn thêm khi use case sở hữu quan hệ (UC-004) chưa phân tích hay chờ.

7. Quan hệ control - control không được nhắc.
   - Vị trí: A5 "Quan hệ giữa boundary và control, control và entity giữ ở dạng association tạm"; F5 "Không vẽ quan hệ giữa hai boundary; không vẽ quan hệ từ entity tới boundary hoặc control".
   - Gặp: R-UC002-03 là Dependency giữa BookTicketOnlineController và PayTicketOnlineController («include»).
   - Xử lý: giữ Dependency, vẽ nét đứt. Prompt không nói rõ quan hệ control - control và Loại cho nó.

8. Bảng Node của C7.1/F5 không đủ cho lớp xuất hiện ở nhiều trang.
   - Vị trí: F5 a) "| ID (mã AC) | Loại | Nhãn | Stereotype | Thuộc về (view) | ..." và C7.3 "ID của mxCell trùng hoặc suy ra được từ ID trong bảng mô hình"; C7.1 "Thuộc về (container)".
   - Gặp: một AC có nhiều dòng (một dòng mỗi view), cột ID không còn duy nhất; hai nơi đặt tên khác nhau cho cột "Thuộc về".
   - Xử lý: thêm cột "ID mxCell" (hậu tố __V2, __V3, trang Entity không hậu tố); dùng tên trang làm giá trị "Thuộc về (view)". Thêm cột x, y, w, h và cột "Điểm uốn" ở bảng Edge.

9. Style lớp của C7.3 không chứa chỗ cho stereotype.
   - Vị trí: C7.3 bảng style "Class: swimlane;...startSize=26" và dòng "Boundary / Control / Entity (icon)"; F5 "Stereotype ... ghi ở ngăn tên".
   - Gặp: startSize=26 chỉ đủ một dòng, stereotype và tên cần hai dòng; hai dòng style (Class và icon) cùng áp cho một lớp phân tích.
   - Xử lý: dùng style Class với startSize=40 và nhãn "«entity»<br>Tên"; không dùng icon. Prompt nên chọn một trong hai.

10. Cột "Vai trò" của F4 và nhãn vai trò C7.3 không khớp dữ liệu P07.
    - Vị trí: F4 "Vai trò: tên vai trò ở một hoặc hai đầu khi cần phân biệt"; P07 cột Vai trò chứa cụm mô tả ("chuyến thuộc một tuyến", "tạm thời").
    - Gặp: dữ liệu P07 không phải tên vai trò; không có cặp lớp nào cần phân biệt hai association.
    - Xử lý: ghi "-" ở cột Vai trò, chuyển các cụm mô tả sang Ghi chú, không vẽ nhãn vai trò.

11. Quy tắc định tuyến cạnh C7.1/C7.3 nặng cho người chạy.
    - Vị trí: C7.1 "Mỗi cạnh đi qua một dải dùng một làn y riêng, hai làn cách nhau 10 ... Khoảng cách giữa hai hàng tối thiểu 40 + 10 x số cạnh"; C7.3 "toạ độ là bội số của 10", "cạnh không cắt qua node".
    - Gặp: bố cục tay 3 trang, 16 đến 21 cạnh mỗi trang là không khả thi nếu không viết script; cổng ra/vào dạng phân số (exitX) không cho ra toạ độ bội số 10 nếu chiều rộng node bất kỳ.
    - Xử lý: viết script sinh bố cục (hàng, làn, cổng), chọn w=250 để cổng bội số 10 ứng với phân số chính xác, tự kiểm tra node chồng, khoảng cách, đoạn cạnh cắt node. Cổng của cạnh ngang giữa hai node cùng hàng (exitY) là phân số theo chiều cao nên toạ độ y thẳng hàng nhưng exitY không phải số tròn. Chưa kiểm chứng hiển thị thật trong draw.io; nhãn multiplicity ở khe 60 giữa hai node cùng hàng có thể chồng nhau.

12. Quy tắc chia view mặc định và nhóm chức năng.
    - Vị trí: F5 "mỗi nhóm một trang chứa boundary, control của nhóm và các entity chúng dùng"; "Ngưỡng tách trang: ... 20 lớp hoặc ... 25 cạnh".
    - Gặp: PaymentGateway, SmsGateway dùng ở hai nhóm (Bán vé, Vận hành chuyến); nhóm lấy từ cột "Nhóm" của P02 bảng 4a. Hệ thống 24 lớp nhưng gộp một trang vượt 20 lớp.
    - Xử lý: các lớp dùng ở nhiều nhóm xuất hiện ở cả hai trang với hậu tố trang. Cạnh entity - entity giữa hai entity cùng có mặt ở trang được vẽ luôn (ví dụ Trip - Seat ở trang Vận hành chuyến, dù quan hệ đến từ UC-002).

13. Không có ngưỡng cho trách nhiệm gắn kết của entity.
    - Vị trí: A4 "control trên 15 trách nhiệm ... hoặc entity không có trách nhiệm hành vi nào thì ghi vào 'Vấn đề còn mở'"; F6 "Trách nhiệm gắn kết".
    - Gặp: Ticket hợp thành 17 trách nhiệm, Trip 11; không có tiêu chí số lượng cho entity.
    - Xử lý: đánh Ticket "Không đạt" về gắn kết (có hành động ở Vấn đề còn mở), Trip "Đạt". Tiêu chí chủ quan. Tiêu chí "Cung cấp đủ hành vi cần" cũng không được định nghĩa khi chưa có hết use case.

14. Phép thử đồng âm chỉ nêu cho lớp, không cho trách nhiệm hoặc thuộc tính.
    - Vị trí: A3 "Cùng tên, khác khái niệm (đồng âm): hai lớp cùng tên"; A4 "Hai trách nhiệm cùng tên, khác ý nghĩa thì đổi tên".
    - Gặp: status ở 5 lớp, checkNotCancelled ở Trip và Ticket, cancelWithTrip ở Ticket và PhoneReservation, findTicket ở Ticket và TripPassengerList: cùng tên khác lớp. Seat.release của UC-002 và UC-008 cùng tên, khác nguyên nhân, cùng kết quả (P07 UC-008 để P08 quyết định).
    - Xử lý: coi cùng tên khác lớp là không phải đồng âm, ghi ở F2a; gộp release thành một trách nhiệm.

15. Quá tải ngữ cảnh khi đọc đầu vào.
    - Vị trí: mục 2 "P07-uc-analysis/*.md (mọi use case trong phạm vi)".
    - Gặp: 4 file P07 mỗi file 64 đến 73 KB (sequence, communication, bảng lọc danh từ), tổng khoảng 270 KB; chỉ bảng F3.4, F6 (quy tắc tương tác), F8 VOPC và các mục cuối cần cho P08.
    - Xử lý: chỉ đọc các mục đó, không đọc sequence và communication; P04 không tra. Prompt nên nói rõ P08 chỉ cần mục nào của P07 (README mục 8 đã gợi ý cho các bước khác).

16. Cấp mã Q, ASM tiếp theo.
    - Vị trí: C3 "đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất".
    - Gặp: Q và ASM nằm rải trong P04, P05, P06, P07 và cả P02; phải grep toàn thư mục design/ để tìm số lớn nhất (Q-74, ASM-53) và cấp tiếp Q-75 đến Q-77, ASM-54 đến ASM-56. Không có sổ đăng ký Q, ASM tập trung.

17. Tên mục F2b, F2a và mục bắt buộc của F7.
    - Vị trí: F7 "Mục kiểm soát theo C5".
    - Xử lý: viết đủ 4 mục Câu hỏi mở, Giả định (CO_NHAN), Đề xuất sửa artifact trước, Vấn đề còn mở; cả bốn đều có nội dung.

## Mục Target không đạt hoặc đạt một phần

- Target 9 đạt một phần: bảng mô hình và .drawio sinh từ cùng dữ liệu nên khớp, trang Entity là trang tổng thể, mỗi trang tối đa 16 lớp và 21 cạnh, kiểm tra tự động toạ độ đạt; nhưng chưa mở bằng draw.io để xem thực tế, nhãn multiplicity ở khe hẹp có thể chồng.
- Target 1 đạt theo cách đã chọn (liệt kê 14 use case chưa phân tích), xem mục 1.
- Target 3, 4, 5, 6, 7, 8, 10 đạt. Target 5: 43 quan hệ VOPC của P07 ánh xạ đủ vào R-01 đến R-36 (bảng đối chiếu trong F4). Target 6: mọi multiplicity có bằng chứng hoặc Q, ASM; 5 quan hệ có phía để trống kèm Q (Q-20, Q-36, Q-73, Q-76, Q-77).
- F6 có hai ô Không đạt (AC-E-Ticket gắn kết, AC-E-Seat yêu cầu đặc thù), đều có hành động trong Vấn đề còn mở.
