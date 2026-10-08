# P12 - Nhật ký người chạy - Phạm vi PKG-09, PKG-22, PKG-23

Model: Sonnet (tham số model sonnet của công cụ Agent).

Đầu ra: design/P12-class-design/PKG-09-PKG-22-PKG-23-ticket-sales-catalog-ticketing.md; design/diagrams/P12-class-PKG-09.drawio, P12-class-PKG-22.drawio, P12-class-PKG-23.drawio (2 trang), P12-class-UC-002.drawio, P12-class-UC-008.drawio, P12-state-DC-Booking.drawio, P12-state-DC-Ticket.drawio, P12-state-DC-Seat.drawio. Tất cả file .drawio qua kiểm tra XML hợp lệ bằng xml.dom.minidom. Số liệu: 45 phần tử thiết kế (3 control, 12 entity, 3 interface, 12 value object, 12 enumeration, 3 exception), 103 operation, 89 thuộc tính, 50 quan hệ (R-02 đến R-10 và R-22 đến R-37 giữ mã P08, R-38 đến R-67 mới), 3 state machine, 109 dòng F4, Q-108, ASM-102 đến ASM-107.

Cách làm: dữ liệu lớp, quan hệ, state machine nằm trong một script sinh (ngoài thư mục dự án) để bảng F1, F2, F5, F7, F8 và file .drawio cùng một nguồn; script kiểm tra tự động khoảng cách node tối thiểu 40, toạ độ bội 10, cạnh trực giao không cắt node, và đối chiếu mọi message P07 có lớp nhận hoặc lớp gửi trong phạm vi với F4.

## Mục Target không đạt hoặc đạt một phần

- Target 3 (đạt có điều kiện): câu trách nhiệm của DC-Booking, DC-Trip, DC-Ticket có nhiều mệnh đề cùng một lý do thay đổi. Tiêu chí "không có liên từ và nối hai trách nhiệm khác lý do thay đổi" mang tính chủ quan, không có thước đo.
- Target 6 (không đạt một phần): vòng đời đầy đủ (tạo, thay đổi, huỷ) chỉ có cho Booking, Ticket, Seat. Route, BaseFare, HolidaySurcharge, PhoneReservation chỉ có tạo vì UC-004, UC-006, UC-012, UC-016, UC-017 chưa có P07.
- Target 7 (đạt kèm ngoại lệ có lý do): bốn nhóm message không thành operation riêng của lớp nhận (checkRouteMatches, cancelReturnRequest, các show... tới boundary, các message bên trong subsystem).
- Target 8 (đạt một phần): constructor của entity và getter ghi nguồn "Bổ sung" nhưng chưa có bên gọi trong bốn UC đã phân tích.
- Target 17 (đạt kèm đề xuất): PKG-09 --> PKG-28 và PKG-08 --> PKG-22, PKG-23, PKG-28 thiếu trong P10 F4 (hợp lệ theo R1, ghi Đề xuất sửa P10).
- Target 18 (đạt có điều kiện): không làm state machine cho DC-Trip (2 trạng thái) và DC-PhoneReservation (chuyển phụ thuộc UC chưa phân tích) dù Target nói lớp có BR phụ thuộc trạng thái đều phải có.
- Target 24 (đạt một phần): bố cục kiểm bằng tính toán, chưa mở draw.io; chiều cao lớp ước lượng theo số ký tự nên có thể lệch khi hiển thị; sơ đồ rộng 2.000 đến 2.800 đơn vị.
- Các Target còn lại (1, 1a, 1b, 2, 4, 5, 9 đến 16, 19 đến 23, 25 đến 27) tự đánh giá Đạt.

## Vướng mắc

1. Ngưỡng quy mô và cách đếm lớp
   - Vị trí: mục 3, "Từ khoảng 15-20 lớp trở lên: chạy lặp theo package, mỗi lần tối đa khoảng 15-20 lớp (một package, hoặc nhóm package có quan hệ chặt nếu tổng không vượt ngưỡng)".
   - Gặp: tham số của người chạy gồm ba package trong một lần; P10 và P11b đã cho 18 phần tử, sau khi thêm kiểu dữ liệu, enumeration, ngoại lệ, interface mới thì thành 45. Prompt không nói enumeration, value object, exception có tính vào ngưỡng hay không, và đầu ra file .md khoảng 186 KB, vượt xa "khả năng duyệt trong một lần đọc".
   - Xử lý: chạy một lượt (YEU_CAU_BO_SUNG là Không có nên không dùng cách chia hai lượt), ghi vào Vấn đề còn mở.

2. Lớp phụ trợ không có hướng dẫn
   - Vị trí: Bước 1.5 "Lớp mới hoàn toàn (lớp tiện ích, factory, lớp giá trị, entity cho trạng thái chờ do NFR buộc lưu bền) chỉ được thêm khi có lý do thiết kế cụ thể"; F1 "Tên lớp không chứa tiền tố mã".
   - Gặp: chữ ký đầy đủ cần kiểu trả về nhiều giá trị (value object), enumeration trạng thái, ngoại lệ nghiệp vụ, DTO giữ cho PKG-08 không phụ thuộc entity. Prompt không nói ngoại lệ và DTO có phải là "lớp thiết kế" cần mã DC và dòng F1 hay không, cũng không nói kiểu giá trị dùng nhiều lần của P10 (PKG-28) có phải dùng lại.
   - Xử lý: cấp DC cho mọi kiểu này với Nguồn AC "Thiết kế: <lý do>", ghi Đề xuất sửa P10 để bổ sung.

3. Phạm vi message của F4 khi chạy theo package
   - Vị trí: Bước 2.1 và F4 "Mỗi message của P07 trong phạm vi có một dòng. Message tới tác nhân người (hiển thị) ánh xạ tới operation của lớp boundary".
   - Gặp: UC trải nhiều package; boundary (PKG-05, PKG-26, PKG-27) và control của UC-013, UC-015 (PKG-10, PKG-11) ngoài phạm vi, nên không có lớp boundary để nhận message show... Message trả về có thành dòng riêng không cũng không nói.
   - Xử lý: tự đặt quy tắc (ghi ở đầu file): chỉ message có lớp nhận hoặc lớp gửi thuộc phạm vi; message trả về gộp vào dòng gọi; message show... ánh xạ vào kết quả trả về hoặc ngoại lệ của dịch vụ. Đối chiếu tự động với P07 cho thấy đủ dòng.

4. Mâu thuẫn "đúng một operation của lớp nhận" với P10 và P11b
   - Vị trí: F2 "Mỗi message trong interaction diagram của phạm vi được gán cho đúng một operation của lớp nhận"; F4 "ánh xạ message sang lớp khác lớp nhận mà không ghi lý do" là lỗi.
   - Gặp: P10 F3 tách DC-Ticket, DC-Trip và chuyển trách nhiệm sang lớp khác; P11b chuyển findTicket, findMatchingTrips, findTrip sang IF-11, IF-10 và gộp requestRefund với returnRefundResult. P10 F3 còn gán // findTicket cho DC-Ticket trong khi P11b đặt ở IF-11.findTicket (hai artifact đầu vào mâu thuẫn).
   - Xử lý: theo P11b cho các lời gọi qua interface; ghi "Khác lớp nhận" kèm lý do ở từng dòng F4; riêng checkReturnTimeLimit tách thành hai operation để kiểm thử biên 4 giờ; ghi Đề xuất sửa P10.

5. Thanh toán đồng bộ trong P07 và bất đồng bộ trong P11b
   - Vị trí: đầu vào, P07 UC-002 msg 3.1.9 (trả về kết quả thanh toán) và 3.1.8.2, 3.1.10 (hệ thống thông báo) so với P11b ASM-100 (kết quả đến qua IF-02).
   - Gặp: prompt không nói cách hoà giải khi diagram phân tích và interface đã chốt lệch nhau, cũng không nói server báo cho client thế nào trong kiến trúc layered web. Hai control PayTicketOnline và BookTicketOnline phụ thuộc hai chiều.
   - Xử lý: tách submitBooking và completeBooking, thêm getBookingStatus, retryPayment; Q-108 cho kênh thông báo; ghi phụ thuộc hai chiều ở Vấn đề còn mở.

6. Kiểu dữ liệu: chữ ký IF "nguyên văn" và kiểu ngôn ngữ
   - Vị trí: Bước 2.1 "Operation của interface IF lấy nguyên chữ ký đã chốt ở P11b mục F3, không đổi" so với [Format] "nếu CONG_NGHE đã chốt ngôn ngữ thì dùng kiểu của ngôn ngữ đó".
   - Gặp: P11b dùng kiểu trung lập (Date, DateTime, List<T>, giá trị enumeration kiểu Succeeded) trong khi hồ sơ chốt Java 17.
   - Xử lý: giữ nguyên chữ ký IF, dùng kiểu Java cho lớp mới và ghi bảng ánh xạ ở đầu file.

7. Đồng hồ và bộ sinh qua constructor
   - Vị trí: Bước 2.6 "lớp chứa method nhận phụ thuộc đồng hồ hoặc bộ sinh qua constructor"; Bước 1.5 liệt kê "interface đồng hồ" là ví dụ IF mới.
   - Gặp: entity do ORM tạo lại nên nhận phụ thuộc qua constructor không thực tế; Java đã có java.time.Clock. Prompt không nói trường hợp entity, không nói khi nền tảng đã có kiểu đồng hồ có cần IF hay không.
   - Xử lý: dịch vụ nhận Clock qua constructor và truyền now, requestTime, checkTime cho entity qua tham số; chỉ cấp IF-15 cho bộ sinh mã vì cần hiện thực ở SS-07. Ghi trong Vấn đề còn mở (C9).

8. Tham chiếu tới quy tắc của prompt khác không đọc được
   - Vị trí: Bước 1.7 và F9 "Kiểm tra gán package theo P10 A3", "P09 A5".
   - Gặp: P12 trỏ tới mục A3 của prompt P10 và A5 của prompt P09, nằm ngoài phạm vi đọc của người chạy; chỉ suy được nội dung từ cách artifact P10 trích dẫn (hai boundary của hai tác nhân không cùng package; interface đặt ở layer của lớp hiện thực hoặc thấp hơn).
   - Xử lý: dùng diễn giải trong artifact P10 và nêu rõ quy tắc đã áp dụng ở F9.

9. Khi nào có state machine
   - Vị trí: Bước 4.1 "ít hơn 3 thường không cần" (F6 Mức hợp lý) so với Target 18 "Lớp có BR phụ thuộc trạng thái đều có state machine".
   - Gặp: DC-Trip chỉ có 2 trạng thái nhưng có điều kiện huỷ; DC-PhoneReservation có BR-24 nhưng các chuyển nằm ở UC chưa phân tích; ST-02 Ticket có trạng thái "Checked" suy ra từ checkedTime chứ không phải giá trị enumeration.
   - Xử lý: không làm cho Trip, PhoneReservation, Refund; làm cho Booking, Ticket, Seat; ghi lý do ở F6 và Vấn đề còn mở.

10. Trạng thái cuối và pseudo state final
    - Vị trí: F6 ví dụ "(Cancelled, NoShow, Completed đều có chuyển tới (final) khi lưu trữ)" so với Mức hợp lý "mọi trạng thái không phải cuối có ít nhất một chuyển ra".
    - Gặp: không rõ trạng thái cuối nghiệp vụ (Ticketed, Expired, Cancelled, Sold) có buộc nối tới final không khi nguồn không có sự kiện lưu trữ.
    - Xử lý: không vẽ final, ghi rõ ở F6.4. Cũng chưa rõ cách ghi sự kiện bị từ chối: F6.2 chỉ cho chuyển trạng thái nên thêm bảng riêng "Sự kiện bị từ chối hoặc bỏ qua".

11. Multiplicity của association do tiêm phụ thuộc, và quan hệ P08 thiếu multiplicity
    - Vị trí: F5 "Chỉ có ý nghĩa với association, aggregation, composition; để trống với dependency..." và "Multiplicity phải có căn cứ từ BR hoặc tài liệu nguồn; thiếu căn cứ thì ghi Q hoặc ASM".
    - Gặp: association từ dịch vụ tới interface (field do container tiêm) không có BR nào cho multiplicity; R-25, R-30, R-37 của P08 để trống.
    - Xử lý: ghi "A 1 - B 1" với lý do "singleton do container tiêm (Thiết kế)"; R-25 dùng ASM-105, R-30 dùng ASM-20, R-37 giữ "?" và trỏ Q-76.

12. Giữ mã R-nn của P08 khi lớp phân tích đổi bản chất
    - Vị trí: F5 "Quan hệ có gốc ở P08 giữ nguyên mã R-nn của P08 (kể cả khi đổi loại ...)".
    - Gặp: R-02, R-09 nối control với boundary hệ thống nay thành subsystem (đầu B đổi từ AC sang IF); R-12 đến R-15 (control PKG-10), R-34 đến R-36 (PKG-24), R-01, R-07, R-08, R-11, R-16 đến R-21 (boundary) thuộc lần chạy khác; prompt không nói quan hệ P08 ngoài phạm vi package được xử lý ra sao.
    - Xử lý: giữ mã R-02, R-09 với đầu B là IF; để các R-nn ngoài phạm vi cho lần chạy tương ứng, ghi rõ ở đầu file; đổi loại R-03, R-04, R-05, R-06, R-10, R-23, R-32 có lý do.

13. Class diagram theo UC
    - Vị trí: Bước 6.1 "Class diagram tham gia UC (chỉ khi DAY_DU): vẽ thêm cho từng UC phức tạp".
    - Gặp: "phức tạp" không định nghĩa; nhiều UC có control ngoài phạm vi (UC-013, UC-015); không nói tên file khi có nhiều UC ngoài mẫu P12-class-<phạm vi>.
    - Xử lý: vẽ UC-002, UC-008 (control trong phạm vi) với tên P12-class-UC-002, P12-class-UC-008; UC-013, UC-015 để cho lần chạy PKG-10, PKG-11. Ngăn operation lọc theo cột Nguồn chứa mã UC.

14. Interface của package khác trên sơ đồ package
    - Vị trí: Bước 6.1 "Với package chứa control, lớp ngoài package chỉ vẽ interface được dùng".
    - Gặp: IF-10, IF-11, IF-15 vừa là phần tử chi tiết của PKG-22, PKG-23 (trong cùng lần chạy) vừa là interface ngoài PKG-09; IF-01 đến IF-08 không có chi tiết.
    - Xử lý: trên sơ đồ PKG-09 vẽ mọi interface ngoài package chỉ ghi tên; chi tiết operation ở sơ đồ PKG-22, PKG-23.

15. Giá trị nghiệp vụ nảy sinh khi thiết kế
    - Vị trí: [Format] "Giá trị nghiệp vụ ... thiếu thì Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN)" so với C1 mục 7 (tham số kỹ thuật là quyết định thiết kế).
    - Gặp: làm tròn tiền, thứ tự xử lý khi thanh toán đến sau hạn, tính lại mức hoàn khi xác nhận, đóng/mở khoảng ngày tăng giá: ranh giới giữa "quyết định thiết kế" và "giá trị nghiệp vụ" mờ.
    - Xử lý: coi các điểm ảnh hưởng số tiền khách thấy hoặc kết quả vé là nghiệp vụ và ghi ASM-102 đến ASM-107; chỉ tham số kỹ thuật (khoá yêu cầu, định dạng requestKey, sắp xếp) ghi "Thiết kế".

16. Đầu vào P11a
    - Vị trí: mục 2 "P11a-gui/screen-list.md và SCR-nn-*.md: Có nếu có giao diện người dùng"; mục 3 "SCR của P11a liên quan".
    - Gặp: phạm vi lần chạy không chứa lớp boundary nên không có SCR liên quan; chỉ đọc screen-list để xác nhận. Không phải lỗi prompt nhưng bảng đầu vào ghi "Có" mà thực tế không cần file SCR.
    - Xử lý: ghi rõ ở "Đầu vào đã dùng".

17. Chi tiết nhỏ khác
    - Constructor chưa có chỗ trong F2 (cột Phạm vi chỉ Instance hoặc Classifier): ghi constructor ở Instance, factory tĩnh ở Classifier.
    - Prompt F8 yêu cầu bảng Node/Edge, C7.1 khuyến nghị cột x, y, w, h; chiều cao node phải ước lượng vì text bọc dòng, không có công cụ render để kiểm tra.
    - Hằng nghiệp vụ (MAX_SEATS, HOLD_DURATION, ngưỡng hoàn tiền) đặt ở thuộc tính classifier private; F7 nói hằng có thể public, không nêu khi nào nên làm vậy.
    - Đã tình cờ liệt kê tên file trong thư mục bus/logs (không mở nội dung) khi kiểm tra thư mục tồn tại; không đọc file nào ngoài phạm vi.
