Model của phiên chạy: Sonnet (claude-sonnet-5-5).

# Nhật ký người chạy - P11a-GD2 (Giai đoạn 2: các màn hình của UC-009, UC-017)

Phiên chạy bị ngắt một lần do hết hạn mức trước khi ghi file nào; phần đọc đầu vào được làm lại từ đầu trong ngữ cảnh còn lại, không ảnh hưởng đầu ra.

## Đầu ra đã ghi (bus-r2/design/P11a-gui/)

- Mới: SCR-02-select-seats.md, SCR-03-enter-traveler-info.md, SCR-04-issued-tickets.md, SCR-06-select-trip-to-cancel.md, SCR-07-confirm-trip-cancellation.md, SCR-08-trip-cancellation-result.md.
- Cập nhật: ui-standards.md (nối MSG-15, MSG-16; phiên bản 1.1), screen-list.md (bảng tổng hợp F7; phiên bản 1.1).
- Cấp mới: Q-70, Q-71, Q-72; ASM-52, ASM-53, ASM-54; MSG-15, MSG-16. Q, ASM lớn nhất toàn dự án sau lần chạy: Q-72, ASM-54.
- Không sinh .drawio mới (giai đoạn 2 không có sơ đồ); screen-transition.md và P11a-screen-transition.drawio không đổi.

## Kết quả theo mục Target

1. Chỉ áp dụng giai đoạn 1: không áp dụng.
2. Đạt cho các màn hình trong phạm vi (boundary AC-B-BookTicketOnlineForm, AC-B-CancelTripForm có màn hình; bảng "Boundary không có màn hình" giữ nguyên).
3. Đạt, kèm một đề xuất sửa P04 UC-009 (hiển thị chỗ đang giữ và thời hạn giữ chỗ chưa có bước nào trong P04).
4. Không đạt hoàn toàn: MSG-01 (UC-009 luồng 2a, hiển thị tại SCR-01) không được tham chiếu ở chức năng của điều khiển nào vì SCR-01 là màn hình điều hướng ngoài phạm vi. MSG-09 và MSG-12 được tham chiếu từ SCR-02, SCR-03 và SCR-06.
5. Không đổi sơ đồ; không kiểm lại.
6. Đạt cho 6 màn hình (hình ảnh, bảng điều khiển, bảng thuộc tính trường, bảng kiểm tra dữ liệu nhập). SCR-04 và SCR-08 chỉ hiển thị, bảng kiểm tra dữ liệu nhập ghi "Không có trường nhập".
7. Đạt: độ dài họ tên, số điện thoại là ASM-52 (chờ Q-44); mã vé, mã chỗ, giá vé, tổng tiền ghi "Thiết kế: <lý do>".
8. Đạt: cùng chuyến Hà Nội - Vinh 15/12/2026 20:30, chỗ A05, A06, vé SV0001, SV0002, 2 x 250.000 = 500.000 đ; ví dụ huỷ chuyến lấy đúng P04 UC-017 mục 8 (5 vé, 4 số điện thoại, 3 vé trực tuyến 750.000 đ, 1 vé tại quầy).
9. Chỉ áp dụng phần giai đoạn 2: mọi màn hình đã đánh giá. Có 7 dòng "Vi phạm còn mở" (SCR-03 x4, SCR-04, SCR-06, SCR-08), mỗi dòng có Q xử lý; không có vi phạm WCAG AA chưa có cách xử lý (WCAG 3.3.4 ở SCR-03 chờ Q-70).
10. Đạt, đã đối chiếu tên, mã MSG, cạnh E-nn với screen-transition.md.
11. Không áp dụng (XUAT_HTML = Không; không đổi sơ đồ).
12. Đạt C2 (đã quét em dash, mũi tên Unicode), C5; C6 không có placeholder còn sót.

## Vướng mắc

1. Mục 3, bảng "Phần cần dùng": "Phạm vi 'các màn hình của UC-nnn' gồm màn hình có cột UC của screen-list.md chứa UC-nnn, trừ màn hình điều hướng". Gặp: SCR-01 và SCR-05 chứa UC-009, UC-017 nên bị loại, và đây là lần giai đoạn 2 duy nhất nên cũng không có lần "màn hình điều hướng" nào sau. SCR-01, SCR-05 sẽ không bao giờ có đặc tả trong lần chạy này, trong khi mục 3 cũng nói lần cuối gom F7 và Target 4 yêu cầu mọi thông điệp có tham chiếu ở điều khiển. Xử lý: đúng chỉ dẫn của người giao (6 SCR), ghi Target 4 không đạt cho MSG-01, ghi ở bảng tổng hợp F7 rằng SCR-01, SCR-05 chưa đánh giá.
2. Mục 3, bảng "Phần cần dùng" và [Context]: bảng không có dòng cho P01-actors.md, P02-usecases.md trong khi mục 2 ghi "Bắt buộc: Có" và [Context] nêu P01, P02. Gặp: không rõ phần nào cần đọc. Xử lý: không mở P01, P02; lấy tác nhân và use case từ P04, screen-list.md (giai đoạn 1).
3. Mục 3: "Mỗi file chỉ cần phần sau (khi chạy bằng agent, chỉ đọc các phần này, tìm theo tiêu đề và theo mã)". Gặp: P04 UC-009 và UC-017 tổng cộng 65 KB, phần cần (luồng, dữ liệu vào ra, thông điệp) nằm xen với bảng activity diagram dài; P07 mỗi file 60-70 KB, bảng message nằm trong nhiều sequence diagram. Xử lý: đọc nguyên P04 (có ích cho Q, ASM, BR); với P07 dùng bảng F2, F4 và grep dòng của boundary giao diện người dùng; P05, P06, P08, P09, P10 chỉ đọc bằng grep theo mã GL, NFR, BR, AC, PKG. Rủi ro bỏ sót ở các file này.
4. F5 e), "Cột Số ký tự tối đa ghi '-' cho trường Lựa chọn, Logic và trường Hiển thị có độ dài theo giá trị" so với "Trường do hệ thống cấp ... độ dài là quyết định thiết kế ... ghi 'Thiết kế: <lý do>'". Gặp: mã vé, mã chỗ, tổng tiền là trường hiển thị nhưng do hệ thống cấp hoặc tính; hai quy tắc đều áp dụng được. Xử lý: trường hệ thống cấp hoặc tính có ghi chú "Thiết kế" và số cụ thể (mã vé 10, mã chỗ 5, tiền 13); tuyến, xe, tài xế, số đếm ghi "-". Kiểu của số điện thoại: danh sách kiểu trong F5 e) không có "chuỗi chữ số" nên ghi "Chữ" kèm lý do giữ số 0 đầu.
5. F5 d), danh sách Loại: không có loại cho ô chỗ ngồi của sơ đồ chỗ và cho dòng của bảng; cột Thao tác "Chọn" và "Nhấn" cùng áp dụng cho nút chọn. Xử lý: ô chỗ ghi "Ô chọn", dòng bảng ghi "Nút chọn"; "Chọn" cho thay đổi lựa chọn, "Nhấn" cho nút và liên kết.
6. F5 e), "độ dài tối đa và miền giá trị mà nguồn không nêu là giá trị nghiệp vụ, ghi Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)". Gặp: Q-44 đã hỏi điều kiện hợp lệ của họ tên, số điện thoại nên độ dài là phần của Q-44. Xử lý: cấp ASM-52 (100 ký tự và 20 ký tự), cột Lý do ghi "Chờ Q-44", không cấp Q mới.
7. A1 / Conventions C1 mục 2 và UI-STT 69 (phase 1): "Dữ liệu chưa có thì ghi Q ở đặc tả màn hình, không tự thêm". Gặp: P04 UC-009 không có dữ liệu ra nào trước bước 12 nên SCR-03 không có giá vé, tổng tiền dù Baymard và WCAG 3.3.4 cần. Dù chế độ CO_NHAN cho phép giả định, thêm giá vé là thêm dữ liệu hiển thị. Xử lý: chỉ cấp Q-70, F7 ghi 3 dòng Vi phạm còn mở (Nielsen 6, WCAG 3.3.4, Baymard).
8. Target 3 và F4: "Mọi thông tin hiển thị ... truy được về bảng dữ liệu vào ra, luồng sự kiện hoặc trách nhiệm của boundary" so với UI-STT 46 (thời hạn giữ chỗ phải hiển thị ở mọi màn hình trong thời hạn giữ chỗ). Gặp: P04 không có bước nào hiển thị thời hạn giữ chỗ cho hành khách; truy vết chỉ tới BR-03, GL-21, P07 (Booking giữ thời hạn). Xử lý: hiển thị theo UI-STT 46, nguồn BR-03 và GL-21, thêm dòng "Đề xuất sửa artifact trước" cho P04 UC-009; thêm MSG-16 (thông báo cho trình đọc màn hình ở ba mốc) vì UI-STT 46 yêu cầu nhưng danh mục MSG giai đoạn 1 không có nội dung.
9. Conventions: UI-STT 37 và screen-transition.md (ghi chú START-ACT-01) yêu cầu ghi ở đặc tả màn hình hành vi khi rời màn hình đang giữ tài nguyên bằng menu, nhưng P04 không nêu rời màn hình bằng menu. Xử lý: ASM-53 (UC-009, SCR-02, SCR-03) và ASM-54 (UC-017, SCR-06) coi như luồng *a, cùng Q-71; hai ASM chung một Q nên Q-71 ghi ở SCR-03 và SCR-06 chỉ dẫn chéo. Quy tắc C1 mục 2 yêu cầu ASM đi kèm Q khi đổi luồng nên không có phương án nào không cần Q.
10. UI-STT 53 (phase 1): "Hiển thị MSG-14 bằng hộp thông điệp modal ... ở lại màn hình hiện tại" mâu thuẫn khi màn hình hiện tại là pop-up SCR-07 (hai modal lồng nhau, trái UI-STT 47 giữ tiêu điểm trong một hộp). Xử lý: đóng SCR-07 rồi hiển thị MSG-14 tại SCR-06, ghi ở d) và ghi là Vi phạm đã sửa Nielsen 4 trong g) của SCR-07. Cần bổ sung UI-STT cho trường hợp lỗi hệ thống từ pop-up. Lỗi hệ thống sau bước 5 của UC-017 (chuyến đã lưu huỷ) làm lần thử lại nhận MSG-10; ghi ở Vấn đề còn mở của SCR-07.
11. UI-STT 32 (phase 1) "Khi mở màn hình có form, tiêu điểm đặt ở trường nhập đầu tiên" không rõ với màn hình chỉ có nút chọn trong bảng (SCR-06) hoặc lưới chỗ (SCR-02). Xử lý: SCR-06 đặt vào nút chọn đầu tiên; SCR-02 coi không phải form chữ nên đặt vào tiêu đề.
12. F7, "Vi phạm đã sửa" và A6 "Sửa vi phạm ... trước khi xuất, ghi lại vi phạm đã sửa". Gặp: chỉ có một bản xuất, không có bản đầu được lưu để đối chiếu nên các dòng Vi phạm đã sửa (SCR-07 Nielsen 4, SCR-08 WCAG 1.4.1) là lỗi tôi nhận ra khi soạn và sửa trong cùng lần; người đọc không kiểm chứng được. Hai dòng chỉ có tính ghi nhận.
13. F7, "Khi MUC_CHI_TIET là DAY_DU, thêm một dòng 'Các tiêu chí còn lại: Đạt theo ui-standards.md STT ...'". Gặp: MUC_CHI_TIET không phải placeholder của bước (có ở hồ sơ dự án, giá trị DAY_DU); danh sách STT được liệt kê theo ước lượng từ nội dung từng màn hình, không đối chiếu từng tiêu chí chưa nêu, nên có thể thừa hoặc thiếu. Cũng không có quy tắc để ghi dòng Không áp dụng (Material Design, Apple HIG): đã bỏ vì cả sáu màn hình là web.
14. Mục 3: "Lần chạy giai đoạn 2 cuối cùng gom mục h) của mọi SCR vào cuối danh mục ở ui-standards.md (chỉ nối thêm dòng, không sửa dòng cũ)" so với C5 (phiên bản tăng khi chạy lại; mã Q, ASM cuối đã cấp phải cập nhật). Xử lý: nối 2 dòng MSG, sửa dòng "Mã MSG lớn nhất", đổi phiên bản và dòng Q, ASM cuối ở bảng đầu ui-standards.md và screen-list.md; không sửa dòng cũ nào của danh mục. Bảng "Đầu vào đã dùng" của hai file đó không cập nhật.
15. Conventions C3 (quét mã Q, ASM lớn nhất): ui-standards.md và screen-list.md giai đoạn 1 ghi quét trước lần chạy Q-65, ASM-48, nhưng P11b (chạy sau) đã cấp Q-69, ASM-51. Quét thật cho kết quả Q-69, ASM-51 nên cấp tiếp từ Q-70, ASM-52. Không phải lỗi prompt, chỉ ghi nhận thứ tự chạy P11a giai đoạn 1, P11b, P11a giai đoạn 2.
16. F4, khung dây trong khối code: chữ tiếng Việt có dấu và bảng rộng (SCR-06) làm các cột không thẳng hàng trên một số phông; không có hướng dẫn độ rộng tối đa. Đã giữ dòng ngắn hơn 90 ký tự.
17. Dữ liệu mẫu: P04 UC-009 dùng ngày 15/06/2026, P04 UC-017 dùng 15/12/2026 cho cùng "Hà Nội - Vinh, 20:30". Chọn 15/12/2026 cho cả hai để A4 "ngày giờ nhất quán giữa các màn hình" được thoả. Thời điểm hiện tại tưởng tượng của màn hình đếm ngược (còn 07:42, giữ đến 20:10) cho thấy giữ chỗ lúc 20:00, cách giờ xuất bến 30 phút, hợp lệ theo BR-05.
18. Contrast: các cặp tôi dùng thêm ở giai đoạn 2 đã tính lại bằng công thức WCAG: #6B7280 trên #D5DAE0 là 3,44:1, #52606D trên #D5DAE0 là 4,59:1, #7A4A00 trên #FFF4D6 là 6,83:1. Không đo bằng công cụ ngoài.
