Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P07 UC-009 - bus-r2

Tham số: BUOC = P07-UC-009; UC_ID = "UC-009 Đặt vé trực tuyến"; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có. Đây là file P07 đầu tiên (sổ AC rỗng). UC-008 và UC-010 chưa có P04, chưa có P07.

Đầu ra:
- design/P07-uc-analysis/UC-009-book-ticket-online-analysis.md (10 lớp AC: 2 boundary, 3 control trong đó 2 control tạm, 5 entity; 46 dòng trong bảng lọc danh từ; Q-55 đến Q-57; ASM-39 đến ASM-41; 3 dòng đề xuất sửa P04).
- design/diagrams/P07-sequence-UC-009.drawio (4 trang: SD1a bước 1-5, SD1b bước 6-8, SD1c bước 9-12, SD2 luồng *a; 46 message không kể trả về).
- design/diagrams/P07-communication-UC-009.drawio (1 trang, 12 đối tượng, 15 link).
- design/diagrams/P07-class-UC-009.drawio (1 trang, 10 lớp, 12 quan hệ).
Mã Q, ASM lớn nhất sau lần chạy: Q-57, ASM-41 (trước đó Q-54 ở P06, ASM-38 ở P06).

Cách làm: sinh .md và 3 file .drawio từ cùng một mô hình dữ liệu (script nằm ở scratchpad, không đưa vào repo) để bảng và sơ đồ không lệch. Đã kiểm tra tự động: 3 file XML hợp lệ (xml.dom.minidom), toạ độ bội số của 10, node không chồng và cách nhau tối thiểu 40, link communication không cắt node, mọi message tuân F6, mọi message tới lớp có trách nhiệm tương ứng và ngược lại, mọi bước hệ thống có message. Không có công cụ hiển thị draw.io nên chưa xem sơ đồ bằng mắt.

Kết quả tự kiểm tra Target: 16/16 Đạt, có chú thích ở mục 3, 12, 14, 15, 16 (xem dưới). Mục 14 chỉ đạt ở phần kiểm tra tự động, phần bố cục bằng mắt chưa kiểm (đã ghi vào Vấn đề còn mở của artifact).

## Vướng mắc

1. A2, fragment par và ngưỡng tách trang của F5
   - Vị trí: A2 "vẽ fragment par hai toán hạng ngay sau message bắt đầu chờ. Toán hạng 1 chứa mọi message từ bước N+1 tới bước M" và F5 "một trang khoảng 30 message không kể message trả về, và tối đa 3 fragment ở mức ngoài cùng ... trang sau bắt đầu bằng fragment ref tới trang trước".
   - Gặp: luồng chính cùng các luồng thay thế gộp được của UC-009 có 40 message không kể trả về và 9 fragment nên phải tách trang. Message bắt đầu chờ (bước 5) nằm cuối SD1a, còn par (bước 6-8) nằm đầu SD1b sau fragment ref, nên par không "ngay sau" message bắt đầu chờ trên cùng một trang.
   - Xử lý: tách SD1a (1-5), SD1b (6-8, mở đầu bằng ref SD1a rồi par), SD1c (9-12). Coi ref SD1a là cầu nối giữa message bắt đầu chờ và par. Prompt nên nói rõ khi par rơi sang trang sau thì ref đứng trước par là chấp nhận được.

2. F5, break cho luồng kết thúc và alt cho luồng quay lại, khi cả hai nằm trong một điểm kiểm tra ba nhánh
   - Vị trí: F5 "Luồng thay thế kết thúc use case ... dùng break ... Không dùng opt" và "Luồng 'Quay lại bước K' vẽ bằng alt: toán hạng luồng chính chỉ ghi guard và note 'tiếp tục luồng chính'".
   - Gặp: bước 4 có 4a (quay lại bước 2), 4b (quay lại bước 3), 4c (kết thúc), cùng một điểm kiểm tra và có thứ tự ưu tiên ASM-23. Ba fragment rời sẽ vượt "tối đa 3 fragment ở mức ngoài cùng" cùng break 2a.
   - Xử lý: tính cả ba kiểm tra (message 2.1.2 đến 2.1.4) trước, rồi một alt ba toán hạng theo thứ tự ASM-23; 4c là break lồng trong toán hạng thứ ba. Prompt chưa nêu cách vẽ khi một điểm kiểm tra có cả luồng quay lại và luồng kết thúc.

3. F5, STT của luồng ở trang riêng và luồng không có điểm rẽ duy nhất
   - Vị trí: F5 "Message ở trang tách riêng dùng STT của message tại điểm rẽ trong trang luồng chính, kèm hậu tố chữ thường theo mã luồng (luồng 7a rẽ tại message 3.1.4 --> 3.1.4a, 3.1.4a.1...)" và "Luồng thay thế trong fragment dùng tiếp số của luồng chính".
   - Gặp: (a) luồng *a xảy ra "tại bất kỳ bước nào trước bước 8", không có một message rẽ duy nhất; mã luồng "*a" không phải chữ thường. (b) luồng 5a do sự kiện hết hạn kích hoạt, không có message cha nên "tiếp số của luồng chính" không xác định.
   - Xử lý: (a) vẽ SD2 tại điểm rẽ đại diện sau message 2.1.10 (sau khi giữ chỗ), STT "2.1.10*a", "2.1.10*a.1", dùng opt [đã giữ chỗ] cho trường hợp huỷ trước khi giữ chỗ; ghi rõ trong Vấn đề còn mở. (b) đánh số 5a là message cấp 1 tiếp theo (4, 4.1...) trong toán hạng 2 của par.

4. F5, message từ boundary tới tác nhân người khi hiển thị kết quả
   - Vị trí: F6 "Boundary ... Actor: Được (actor của nó)" và F5 "Message từ actor tới boundary mô tả hành động của actor". Không câu nào nói có vẽ message hiển thị từ boundary tới actor hay không.
   - Gặp: nếu vẽ thì mỗi thông báo (2a, 4a, 4b, 4c, 5a, 7a, 8a, 12, *a) thêm một message, gần gấp đôi số message và làm Hành khách xuất hiện ở mọi trang; nếu không vẽ thì actor người không nhận gì.
   - Xử lý: không vẽ message boundary --> actor người; message control --> boundary đã thể hiện việc hiển thị (ghi ở đầu mục F5). Với Cổng SMS (actor hệ thống ngoài) vẽ đủ hai chiều vì bước 10 và 11 nêu rõ. Prompt nên chốt một quy ước.

5. A1 và F3.4, "chủ sở hữu UC-xxx" cho entity do use case khác quản lý
   - Vị trí: A1 "Entity hoặc boundary hệ thống ngoài mà khái niệm do use case khác (không include, không extend) quản lý, và use case đó chưa có P07: ... ghi 'Mới - chủ sở hữu UC-xxx'".
   - Gặp: Trip, Seat, Fare có nhiều use case liên quan (Trip: UC-016 lập lịch, UC-017 huỷ, UC-020 tuyến; Seat: UC-021 sơ đồ chỗ; Fare: UC-023, UC-024). Prompt không nêu tiêu chí chọn chủ sở hữu. Ticket, Booking, SmsGateway do chính UC-009 tạo hoặc là tác nhân của UC-009 nhưng cũng dùng ở UC-003, UC-004, UC-014, UC-017.
   - Xử lý: chọn UC tạo hoặc đặt dữ liệu gốc (Trip: UC-016, Seat: UC-021, Fare: UC-023); Ticket, Booking, SmsGateway ghi "Mới" vì UC-009 là use case đầu tiên chạm trực tiếp. Ghi trong Vấn đề còn mở.

6. F3.2, danh sách giá trị cột Kết luận không có chỗ cho trạng thái, phân loại và thuật ngữ hai vai trò
   - Vị trí: F3.2 "Cột Kết luận chỉ nhận một trong các giá trị: ...".
   - Gặp: "Chỗ trống" (trạng thái), "Vé mua trực tuyến, Kênh mua vé" (phân loại), "Giữ chỗ" (thao tác nhưng cũng là trạng thái), "Giá vé" (vừa là thuộc tính của vé vừa là bảng giá theo tuyến, loại xe do UC-023 đặt), "Người đi" (hai thuộc tính không định danh). Không giá trị nào khớp đúng.
   - Xử lý: dùng "Loại - thuộc tính của X" cho trạng thái và phân loại, "Loại - thao tác hoặc sự kiện" cho Giữ chỗ, tách "Giá vé" thành hai dòng (thuộc tính của Ticket; Entity Fare). Ghi lý do ở cột Lý do.

7. F3.2 và F3.4, trạng thái của chỗ theo chuyến so với P05 GL-01
   - Vị trí: F3.4 "Tên: ... entity lấy từ glossary" và A4 "Tra sổ đăng ký AC và glossary".
   - Gặp: GL-01 định nghĩa Chỗ là vị trí trên sơ đồ chỗ của loại xe, còn "trạng thái của chỗ trên một chuyến xe" chỉ nằm trong Ghi chú, không có thuật ngữ cho "chỗ của chuyến". BR-02, BR-03 và NFR-04 đều nói về chỗ trên một chuyến.
   - Xử lý: một entity Seat với thuộc tính tripState, lifeline :Seat đại diện cho từng chỗ đã chọn; ghi ở Vấn đề còn mở để P08 xét tách. Không cấp Q vì là lựa chọn mô hình, không phải điểm nguồn thiếu.

8. A2 và C1, ranh giới giữa "làm rõ" và "thêm chức năng" khi cấp ASM ở P07
   - Vị trí: A2 "Mô tả bổ sung chỉ làm rõ điều đã có ... Không thêm chức năng mới. Nếu một bước mơ hồ tới mức không phân bổ được ... CO_NHAN thì ghi giả định ASM-nn" và C1 mục 2 "Giả định phải sinh ra nội dung".
   - Gặp: P04 UC-009 không nêu (a) nơi ghi nhận "mã vé chưa gửi được qua SMS" (11a), (b) thời điểm xác định giá vé (cần có ở bước 8 để gọi UC-010 và ở bước 12), (c) hành vi với UC-010 đang chạy khi hết thời hạn giữ chỗ (5a). Cả ba không phải "mơ hồ tới mức không phân bổ được", nhưng phân bổ buộc phải chọn và (c) sinh thêm message cancelPayment tới control UC-010 (gần như chức năng mới).
   - Xử lý: tạo ba cặp Q-55/ASM-39, Q-56/ASM-40, Q-57/ASM-41 và ba dòng Đề xuất sửa P04. Có thể bị coi là cấp ASM thừa so với tinh thần "không thêm chức năng"; prompt nên nêu rõ khi nào được thêm message không có trong đặc tả (nên chỉ khi P04 chưa đủ để phân bổ).

9. F3.4, Mức hợp lý "Một control có khoảng 2-10 trách nhiệm" với control tạm
   - Vị trí: F3.4 "Một control có khoảng 2-10 trách nhiệm trong một use case" và A1 về control tạm.
   - Gặp: control tạm của UC-008 chỉ có một trách nhiệm (searchTrips), của UC-010 có hai; mức 2-10 thiếu nghĩa với control chưa được phân tích. Ngược lại control của UC-009 có 7 trách nhiệm nhưng chỉ vì mỗi message nhận (kể cả tự gọi startWaiting/stopWaiting) là một trách nhiệm.
   - Xử lý: coi 2-10 chỉ áp cho control của chính use case đang phân tích; ghi "tạm" ở trách nhiệm của control tạm.

10. F7 và F8, multiplicity khi đặc tả chỉ gián tiếp nêu
    - Vị trí: A8 "Ghi multiplicity khi đặc tả hoặc BR nêu rõ; nếu không rõ thì để trống" và F8 b) "số ở phía A là số đối tượng A ứng với một đối tượng B".
    - Gặp: BR-01 nêu "tối đa 5 chỗ" (Booking có 1 đến 5 Seat) nhưng phía ngược lại (số Booking ứng với một Seat theo thời gian) không rõ; BR-04 "mỗi chỗ một mã vé" cho Booking với Ticket 0..5 (lần đặt chưa thanh toán thành công không có vé), do suy luận.
    - Xử lý: phía chưa rõ ghi "?"; quan hệ Booking-Trip (không có link trong F7) dựa trên GL-12 và ghi nguồn rõ.

11. Mục 3 (bảng phần cần đọc) và đầu vào P02
    - Vị trí: mục 3 "P02-usecases.md | Dòng UC_ID ở Mục 4, các dòng UC có tác nhân thời gian (A2)".
    - Gặp: "các dòng UC có tác nhân thời gian" mà ACT-09 Bộ định thời nằm ở P01 và Mục 4 của P02; phải đọc cả Bảng 4a để tìm (UC-007, UC-025). Bước tìm thủ công này dễ sót khi dự án lớn.
    - Xử lý: đọc toàn bảng 4a, 4b của P02. Kết luận UC-009 không tạo, đổi, huỷ mốc nào (ghi ở F2 bước 9 và Vấn đề còn mở). Prompt có thể nêu cột Tác nhân chính của Bảng 4a là nơi lọc.

12. Cột "Thuộc về (container)" của message trong bảng message
    - Vị trí: F5 b) "Cột Thuộc về của message nằm trong fragment ghi ID fragment" so với F5 c) bảng message có cột "Fragment" nhưng không có cột Thuộc về.
    - Gặp: bảng message dùng tên cột "Fragment". Với message trong toán hạng thứ hai của alt không rõ ghi ID fragment hay ID toán hạng.
    - Xử lý: cột Fragment ghi ID fragment cho toán hạng đầu và "<ID>-O<n>" cho toán hạng từ hai; cột Thuộc về của dòng fragment lồng ghi ID toán hạng chứa nó. Thêm cột ID đầu bảng message (F10 yêu cầu ID cell trùng ID bảng nhưng F5 c) không có cột ID).

13. Thêm loại Note trong bảng Node của sequence diagram
    - Vị trí: F5 b) "Loại (Actor / Lifeline / Fragment)" và F5 c) nhắc "note 'tiếp tục luồng chính'", "note 'quay lại bước K'".
    - Gặp: note là phần tử vẽ nhưng không có loại trong bảng Node.
    - Xử lý: thêm loại "Note" vào bảng Node, ID dạng <trang>-N<n>.

## Mục Target không đạt hoặc đạt có điều kiện

- Mục 3: đạt. ACT-06 Cổng thanh toán không có boundary ở UC-009 vì chỉ tương tác trong UC-010 (đúng điều kiện trừ của Target 3).
- Mục 12: đạt theo cách sinh tự động (cùng danh sách message, cùng STT); communication gồm cả message của SD2 vì MUC_CHI_TIET là DAY_DU.
- Mục 14: bảng và .drawio khớp do sinh từ cùng dữ liệu; XML hợp lệ, toạ độ bội 10; chưa xem sơ đồ bằng mắt (không có draw.io), nên bố cục (nhãn dài, cạnh không cắt node ở mức nhìn) mới kiểm bằng phép tính.
- Mục 15: đạt. Mốc thời gian: UC-009 không tạo, đổi hay huỷ mốc của UC-007, UC-025 nên không có message hẹn; ghi lý do ở F2 bước 9 và Vấn đề còn mở.
- Mục 16: Q-55 đến Q-57 và ASM-39 đến ASM-41 nối liền từ Q-54, ASM-38 (P06), không trùng, không bỏ trống.
