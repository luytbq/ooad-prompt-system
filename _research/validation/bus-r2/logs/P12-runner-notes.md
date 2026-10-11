Model của phiên chạy: Sonnet (Sonnet 5.5, claude-sonnet-5-5).

# Nhật ký người chạy - P12 Thiết kế lớp - PKG-13, PKG-27, PKG-28

Phạm vi lần chạy: PKG-13 Booking, PKG-27 Operations, PKG-28 Ticketing (chưa có file P12 nào khác). Placeholder QUY_UOC_KIEU_DU_LIEU, MAU_THIET_KE_DA_CHOT, YEU_CAU_BO_SUNG đều "Không có".

Đầu ra:
- design/P12-class-design/PKG-13-PKG-27-PKG-28-booking-ticketing.md
- diagrams/P12-class-PKG-13.drawio, P12-class-PKG-27.drawio, P12-class-PKG-28.drawio, P12-class-UC-009.drawio
- diagrams/P12-state-DC-Trip.drawio, P12-state-DC-Seat.drawio, P12-state-DC-Booking.drawio, P12-state-DC-Ticket.drawio

Số liệu: 15 dòng F1 (14 lớp có hành vi, 1 view model), 26 kiểu phụ trợ ở F1b, 91 operation, 47 thuộc tính, 38 quan hệ (R-02 đến R-45, trong đó R-23 đến R-45 mới), 4 state machine ST-01 đến ST-04, 8 file .drawio (đều qua xml.dom.minidom). Q-73, Q-74, ASM-55, ASM-56 mới; mã Q, ASM cuối: Q-74, ASM-56. Không cấp IF mới.

Cách làm: dữ liệu mô hình (lớp, operation, thuộc tính, quan hệ, state machine) viết một lần trong chương trình tạm rồi sinh cả bảng .md lẫn file .drawio để hai dạng không lệch; chương trình kiểm tự động node không chồng, khoảng cách tối thiểu 40, toạ độ và điểm uốn bội số của 10, cạnh không cắt qua node. Chương trình không nằm trong sản phẩm.

Phạm vi đọc: chỉ đọc các file được phép (prompt P12, Conventions, README, project-profile, tài liệu nguồn) và các artifact đầu vào mục 2, mục 3 của prompt: P10, P08, P09, P11b, P11a (screen-list, SCR-02, SCR-03, SCR-04), P07 UC-009, UC-017 (đọc có chọn lọc), P04 UC-009, UC-017, P06, P05. Không mở nhật ký khác. Có quét mã Q, ASM, R, IF bằng grep trên toàn bộ design/ theo Conventions C3.

## Vướng mắc

### 1. Tên file khi phạm vi là một phần của hệ thống nhưng dưới ngưỡng
- Vị trí: mục 3, "Hệ thống nhỏ (khoảng dưới 15 lớp có hành vi): chạy một lần cho toàn hệ thống, đầu ra một file P12-class-design.md." và "Mỗi lần một file P12-class-design/<PKG-nn>-<slug>.md".
- Gặp: phạm vi do người dùng điền là 3 package, 14 lớp có hành vi (dưới 15) nhưng không phải "toàn hệ thống". Ngưỡng nói về cả hệ thống nên không dùng được để chọn tên file; prompt không định nghĩa <slug> cho lần chạy nhiều package.
- Xử lý: dùng dạng theo package, nối mã PKG như C4 và Conventions ví dụ: P12-class-design/PKG-13-PKG-27-PKG-28-booking-ticketing.md; slug tự đặt.

### 2. Chữ ký tạm chỉ được nói cho interface IF, không nói cho lớp và kiểu của package chưa chạy P12
- Vị trí: Bước 0, "Interface IF được dùng trong phạm vi mà P11b chưa có chữ ký ... đặt chữ ký tạm trong một bảng riêng "Chữ ký interface tạm"".
- Gặp: ngoài IF-01 (thu tiền, P11b ghi "Chờ P07 UC-010"), phạm vi còn gọi IF-08 và DC-PaymentTransaction (PKG-29), DC-Money, DC-PhoneNumber, DC-TicketCode (PKG-31) mà chưa package nào chạy P12. Prompt chỉ nói thứ tự "layer thấp trước" ở mục 5 (ghi chú) và không có quy tắc cho trường hợp người dùng chọn package layer cao (PKG-13) cùng package layer thấp một phần (PKG-27, PKG-28) mà bỏ PKG-29, PKG-31.
- Xử lý: mở rộng bảng "Chữ ký interface tạm" cho cả lớp và kiểu giá trị của package khác; ghi Đề xuất sửa P11b và chạy lại P12 cho PKG-13 khi có chữ ký.

### 3. Message có lớp nhận ngoài phạm vi nhưng kết quả của nó quyết định chữ ký của control trong phạm vi
- Vị trí: Bước 2.1, "Message tới lớp ngoài phạm vi để cho lần chạy chứa lớp nhận." và F4 "Message gửi tới tác nhân người (hiển thị) ánh xạ tới operation của lớp boundary."
- Gặp: DC-BookTicketOnlineService phải thông báo 4a, 4b, 4c, 5a, 7a, 8a, 11a cho View ở PKG-05 (notifySeatsUnavailable, ...). Cách thể hiện (ngoại lệ, kiểu trả về, view model) là một phần chữ ký của control nên không thể để lần chạy PKG-05 quyết. Prompt không có chỗ ghi hợp đồng này.
- Xử lý: thêm bảng F4b ngoài khung F4 (message nhận ngoài phạm vi và cách phạm vi này thể hiện kết quả bằng ngoại lệ hoặc view model).

### 4. F1b mâu thuẫn với Bước 1.5 và Target 1 về nơi ghi view model
- Vị trí: Bước 1.5 "Value object, enumeration, ngoại lệ nghiệp vụ cấp mã DC và có dòng ở F1, nhưng gom vào bảng F1b "Kiểu phụ trợ", không lập dòng F7 riêng"; F1b "Mỗi kiểu phụ trợ có một dòng ở đây thay cho dòng F1, F7 đầy đủ."
- Gặp: câu đầu nói "có dòng ở F1", câu sau nói "thay cho dòng F1". Thêm nữa DC-BookTicketOnlineViewModel do P10 cấp mã và có thuộc tính từ lớp phân tích, đồng thời là value object; Target 1 buộc mọi DC của P10 có ở F1.
- Xử lý: view model có dòng F1 và F7 (vì P10 cấp và có thuộc tính nguồn); mọi kiểu phụ trợ do P12 sinh chỉ ở F1b.

### 5. PKG-31 "Không nhận lớp khác" nên enumeration và ngoại lệ dùng chung không có chỗ đặt
- Vị trí: Bước 1.5 "Kiểu dữ liệu dùng chung nhiều package đặt ở package kiểu dùng chung của P10, không cấp lại trong từng package"; P10 F4 PKG-31 "Không nhận lớp khác".
- Gặp: DC-CancelReason, DC-TripDepartedException dùng chung PKG-13 và PKG-16 nhưng PKG-31 chỉ nhận 4 kiểu giá trị.
- Xử lý: đặt ở package chủ sở hữu (PKG-27), PKG-16 đã phụ thuộc PKG-27; ghi ở F1b.

### 6. Lớp mới do thiết kế trong package có sẵn không có luồng cập nhật P10
- Vị trí: Bước 1.5, "Interface mới do cơ chế thiết kế ... cấp mã IF-nn ... ghi lý do và Đề xuất sửa artifact trước: cập nhật P10." (chỉ nói interface); Bước 1.5 "Lớp mới hoàn toàn ... cấp mã DC mới, cột "Nguồn AC" ghi "Thiết kế" kèm lý do."
- Gặp: DC-TripTicketCancellation (tách bốn trách nhiệm tập vé khỏi Ticket, P10 F1 "P12 xét tách") cần xuất hiện ở P10 F3, F4, F5 vì PKG-16 sẽ phụ thuộc nó; prompt không nói có phải đề xuất sửa P10 cho lớp DC mới (chỉ cho IF).
- Xử lý: vẫn ghi Đề xuất sửa artifact trước (P10 F3, F4, F5) theo C1 mục 3.

### 7. Mốc thời gian nội bộ BR-03 và điểm vào của bộ định thời không được Bước 1.6a bao quát
- Vị trí: Bước 1.6a, "Mốc thời gian đã đăng ký ở P07 (message hẹn, hẹn lại, huỷ mốc cho use case do tác nhân thời gian kích hoạt)"; P10 F3 "startWaitingForPaymentResult, stopWaitingForPaymentResult do P12 chốt thành thao tác ghi, xoá thời hạn giữ chỗ trên Booking".
- Gặp: UC-009 không có message hẹn, huỷ mốc; chỉ có self-message after(BR-03) handleHoldExpiry và hai self-message chờ. Bước 1.6a nói thiết kế "điểm vào khi tới mốc gọi control của use case do tác nhân thời gian kích hoạt", nhưng ở đây bộ định thời (PKG-11, Presentation) chỉ được phụ thuộc Application (P09 QT-4) và không được đọc kho dữ liệu, nên control phải mở thêm operation liệt kê lần đặt tới hạn. Prompt không có hướng dẫn cho dạng "quét định kỳ" ngoài một cụm "bộ lập lịch bền vững hoặc quét định kỳ".
- Xử lý: thêm DC-BookTicketOnlineService.listExpiredHolds và handleHoldExpiry (guard theo trạng thái), IF-06.findIdsHoldExpiredAt; ghi nguồn "Bổ sung: cơ chế quét mốc (Bước 1.6a)". Hai self-message start, stop chờ gộp vào holdSeats, clearHoldExpiry.

### 8. Không có hướng dẫn tách một control dài thành nhiều yêu cầu web và nhiều giao dịch
- Vị trí: Bước 1.4 "Control thường là nơi đặt ranh giới giao dịch (transaction)."; F3 "nêu rõ ranh giới giao dịch nếu có".
- Gặp: P07 vẽ processTravelerInfo là một chuỗi liên tục (ghi người đi, thanh toán, phát hành vé, gửi SMS) trong khi kiến trúc web không giữ trạng thái giữa các yêu cầu và P09 F7 cấm giữ khoá cơ sở dữ liệu lúc gọi cổng. Phải chọn ba giao dịch ngắn, nạp lại Booking sau khi gọi cổng, và ném ngoại lệ sau khi commit (ngoại lệ không kiểm tra làm hoàn tác việc trả chỗ). Prompt không có tiêu chí cho tình huống này.
- Xử lý: mô tả ở F3 của DC-BookTicketOnlineService.processSeatSelection, processTravelerInfo, handleHoldExpiry; ghi nguyên tắc ở F1b.

### 9. Control Tạm (UC chưa có P04, P07): nguồn operation và giới hạn chi tiết hoá
- Vị trí: Bước 1.1/F1 không nói về lớp Tạm; F2 "Nguồn: ... hoặc "Bổ sung: <lý do>" (khởi tạo, quản lý, equality)".
- Gặp: DC-SearchTripsService (UC-008) và DC-PayTicketOnlineService (UC-010) chỉ có một hai message trong P07 UC-009. Cần viewSeatMap (sơ đồ chỗ cho SCR-02) và tham số tìm chuyến (điểm đi, điểm đến, ngày đi lấy từ tài liệu nguồn). Ngoài "khởi tạo, quản lý, equality", prompt không nêu loại nguồn "chờ UC khác".
- Xử lý: ghi "(Tạm)" trong nguồn và cột Ghi chú thiết kế; liệt kê ở Vấn đề còn mở; chạy lại P12 PKG-13 khi có P07 của UC-008, UC-010.

### 10. Xung đột giữa "không getter hàng loạt", "operation quan sát hậu điều kiện" và ngưỡng 15-20 operation public
- Vị trí: Bước 2.4 "Không thêm getter/setter hàng loạt; chỉ thêm khi có bên gọi cần. Thuộc tính mà hậu điều kiện của operation nêu ... có operation truy vấn chỉ đọc"; F1 "số operation public thường không quá khoảng 15-20".
- Gặp: DC-Ticket 20 operation public (11 getter), DC-Booking 17 (8 getter). Mỗi getter có bên gọi hoặc để quan sát hậu điều kiện nhưng làm lớp chạm ngưỡng.
- Xử lý: giữ, ghi lý do ở F1 và Vấn đề còn mở. Bất tiện: sơ đồ lớp phải liệt kê hết nên hộp lớp cao 600 px.

### 11. Số tham số lớn nhưng không nên gom
- Vị trí: F2 "từ khoảng 4 tham số trở lên thì xem xét gom thành đối tượng tham số, nhưng chỉ truyền đối tượng khi bên nhận dùng phần lớn dữ liệu của nó".
- Gặp: Ticket.createTicket 7 tham số (dùng hết), Trip constructor 5. Gom thành đối tượng tham số sẽ thêm kiểu trung gian hoặc buộc Ticket phụ thuộc Booking (tạo vòng Booking-Ticket). Prompt không nói cách chọn khi hai quy tắc giằng.
- Xử lý: giữ, ghi lý do ở Vấn đề còn mở.

### 12. Constructor là Instance hay Classifier
- Vị trí: F2 "Phạm vi: Classifier (static ...) khi operation không cần trạng thái của một đối tượng cụ thể (factory tạo đối tượng, tiện ích thuần tính toán)".
- Gặp: constructor không rõ thuộc nhóm "factory tạo đối tượng" hay Instance, ảnh hưởng gạch chân trên sơ đồ.
- Xử lý: constructor ghi Instance; static factory (createBooking, createTicket) ghi Classifier; nêu ở F2.

### 13. Multiplicity của association do tiêm phụ thuộc
- Vị trí: Format, "Multiplicity của association do tiêm phụ thuộc ... là quyết định thiết kế, ghi "Thiết kế: tiêm phụ thuộc"".
- Gặp: không nói giá trị cụ thể cho hai đầu (bean singleton: một dịch vụ, một interface). Có 15 dòng như vậy (R-02, R-03, R-09, R-23 đến R-32, R-39, R-40).
- Xử lý: ghi "A 1 - B 1" kèm "Thiết kế: tiêm phụ thuộc" ở Lý do.

### 14. Interface kho dữ liệu không xuất hiện trong P07 nhưng bắt buộc có trong F4, F5
- Vị trí: Bước 3.1 "Với mỗi cặp lớp có trao đổi message (mỗi link trong communication diagram)"; F5 "Mỗi link trong interaction diagram có một quan hệ tương ứng".
- Gặp: P07 vẽ control gọi thẳng entity (R-04 đến R-08); thiết kế theo P09 QT-5 buộc control đi qua IF-03 đến IF-07 (P10 cơ chế). Do đó R-04 đến R-08 đổi sang Dependency và thêm R-23 đến R-31 (Association tới interface) mà không có link tương ứng trong P07; việc nạp entity (findByIdForUpdate, findByTripAndSeatCodesForUpdate...) cũng không là message nào. Prompt không nói cách ghi các operation này ở F2, F4 ngoài nguồn "Bổ sung".
- Xử lý: nguồn ghi "Bổ sung: nạp ..." và ghi vào cột Operation của F4 như phần của dòng gọi; thêm R-41 đến R-45 (cặp kho - entity) để sơ đồ có cạnh.

### 15. State machine với trạng thái ghép và cờ trực giao
- Vị trí: F6 "Mọi trạng thái đạt được từ initial ... mỗi sự kiện có thể xảy ra đều có xử lý"; "Trạng thái ... được biểu diễn bằng thuộc tính (thường là enumeration)".
- Gặp: Ticket có hai thuộc tính trạng thái (status, refundStatus) và ba cờ ghi nhận lỗi độc lập (smsStatus, cancelNoticeStatus, refundAttemptStatus). Prompt không hướng dẫn trạng thái trực giao hay composite state cho trường hợp này; Node/Edge ở F6.4 phải khớp file nên chuyển tự thân của cờ không vẽ được gọn.
- Xử lý: gộp thành bốn trạng thái ghép tên (Issued, CancelledRefundPending, CancelledRefunded, CancelledNoRefundDue); hai chuyển đặt cờ ghi ở F6.2 kèm chú thích "không vẽ", không có trong bảng Edge F6.4. Booking có trạng thái SELECTING không bao giờ được lưu: initial vẫn là "trạng thái khi đối tượng được tạo", nhưng đối tượng bị bỏ khi kiểm tra thất bại mà prompt không cho cách ghi (final chỉ khi có sự kiện kết thúc); ghi ở Ghi chú F6.

### 16. Class diagram không thể đọc trên một trang khi phải liệt kê đủ F2 và F7
- Vị trí: F8 "Nội dung ngăn thuộc tính và ngăn operation của mỗi lớp lấy đúng từ F7, F2 (không thêm, không bớt)" và "Mức hợp lý: một sơ đồ nên đọc được trên một trang"; "Với package chứa control, lớp ngoài package chỉ vẽ interface được dùng".
- Gặp: với chữ ký đầy đủ (có kiểu), hộp DC-Ticket cao 610 px, rộng 520 px; sơ đồ PKG-28 rộng khoảng 2500 px, cao 1200 px, không đọc trên một trang. Prompt cũng không cho cách tính chiều cao ngăn khi dòng bị cuộn; phải ước lượng độ rộng chữ. Quy tắc "package chứa control" chưa nói rõ với package chứa entity có bị control của package khác tham chiếu.
- Xử lý: giữ nguyên nội dung đầy đủ, chiều rộng tối đa 520 và ước lượng số dòng khi cuộn; không vẽ dependency từ control PKG-13 vào sơ đồ PKG-27, PKG-28 (đã ở F5 và sơ đồ UC-009).

### 17. Quá tải ngữ cảnh khi đọc đầu vào
- Vị trí: mục 3, "Đính kèm tối thiểu cho mỗi lần: P07 của các UC có lớp trong phạm vi ..., P08, P09, P10, phần P11b của các SS mà phạm vi dùng, SCR của P11a liên quan."
- Gặp: đầu vào thực tế khoảng 600 KB (P07 hai file 130 KB, P08 55 KB, P09 66 KB, P10 44 KB, P11b 59 KB, prompt 71 KB, Conventions 24 KB). Mục 2 chỉ định đúng mục cần đọc cho P08 (F3 bảng quan hệ), P09 (F3 đến F6) và P10 (F3) nhưng với P07 nói chung "Message trong sequence/communication diagram" và không có chỉ dẫn rút gọn như README mục 8 cho P04.
- Xử lý: đọc có chọn lọc theo mục (sed, grep) và chỉ lấy bảng message có lớp nhận trong phạm vi của UC-017. Không thấy quá tải ở bước sinh vì dùng chương trình sinh bảng từ dữ liệu.

### 18. Cách chọn Q, ASM trong chế độ CO_NHAN cho giá trị gần nghiệp vụ
- Vị trí: Format, "Giá trị nghiệp vụ (hạn mức, thời hạn, giá, phí, ngưỡng mà người dùng cảm nhận được) và multiplicity phải có nguồn BR, tài liệu nguồn; thiếu thì Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN)."
- Gặp: cách làm tròn giá có mức tăng giá (thuộc "giá" nên cần Q, ASM) và phạm vi chuyến hiển thị ở UC-017 (lịch chạy) không nêu trong nguồn; ranh giới giữa "tham số kỹ thuật" và "giá trị nghiệp vụ" ở đây mờ (làm tròn có vẻ kỹ thuật nhưng đổi số tiền khách trả).
- Xử lý: cấp Q-73, Q-74 và ASM-55, ASM-56 (mỗi ASM đi kèm Q, đúng C1 mục 2).

### 19. Thuộc tính trạng thái chỉ có một giá trị ghi nhận lỗi
- Vị trí: Bước 5.1 "thuộc tính của lớp phân tích"; F7 "Thuộc tính trạng thái kiểu Boolean nhiều cờ ... thay vì một enumeration" (lỗi thường gặp) và Target 26 "Không đổi tên, mã phần tử đã chốt".
- Gặp: P08 có smsStatus (Chưa gửi được), cancelNoticeStatus (Chưa báo được), refundAttemptStatus (Hoàn không thành công) chỉ có một giá trị; để giữ tên thuộc tính và tránh cờ Boolean phải thêm giá trị NO_ISSUE giả. Không rõ giữ tên hay đổi sang cờ Boolean.
- Xử lý: giữ tên P08, kiểu enumeration hai giá trị (NO_ISSUE và giá trị lỗi).

## Kết quả tự kiểm theo Target

Đạt: 1, 1a, 1b, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27.

Không đạt hoặc đạt một phần (ghi ở Vấn đề còn mở của artifact):
- Target 6 (vòng đời đầy đủ của lớp persistent): chỉ đầy đủ cho Booking, Ticket trong phạm vi UC-009, UC-017. Tạo, sửa Trip, Seat, Fare thuộc UC-016, UC-021, UC-023, UC-024; trả chỗ của vé đã bán và trạng thái đã trả, đã đổi của vé thuộc UC-012, UC-014; chưa có P07; không có xoá, lưu trữ vì nguồn không nêu.
- Target 12: UC-009 không có message hẹn mốc; hai mốc huỷ của UC-017 thuộc DC-CancelTripService (PKG-16) nên chưa kiểm ở lần chạy này.
- Target 24: bảng Node/Edge khớp file (cùng sinh từ một dữ liệu), XML hợp lệ, không chồng node, cạnh không cắt qua node, toạ độ bội số của 10; chưa mở bằng draw.io để xem bằng mắt, nhãn multiplicity và nhãn chuyển trạng thái có thể cần chỉnh; kích thước sơ đồ lớp vượt một trang (vướng mắc 16).
- Mức hợp lý F1: DC-Ticket (20) và DC-Booking (17) ở ngưỡng trên số operation public; Ticket.createTicket 7 tham số (vướng mắc 10, 11).
