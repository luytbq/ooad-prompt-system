Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P04 UC-009 - bus-r2

Đầu ra: bus-r2/design/P04-uc-specs/UC-009-book-ticket-online.md, bus-r2/design/diagrams/P04-activity-UC-009.drawio, bus-r2/design/P04-uc-specs/_BR-register.md (tạo mới, BR-01 đến BR-06). Placeholder UC_ID = UC-009; TEN_HE_THONG_TRONG_LUONG và YEU_CAU_BO_SUNG = Không có. Chế độ CO_NHAN, MUC_CHI_TIET = DAY_DU. Đây là lần chạy P04 đầu tiên: chưa có sổ BR, chưa có đặc tả P04 nào. Mã Q, ASM lớn nhất trước lần chạy: Q-43, ASM-17 (P03); sau lần chạy: Q-45, ASM-24. Luồng chính 12 bước, 8 luồng thay thế có số bước cộng luồng *a. File .drawio qua kiểm tra xml.dom.minidom, 37 node, 38 cạnh, đã kiểm bằng script: toạ độ bội số của 10, không node chồng, khoảng cách node tối thiểu 40, không cạnh nào cắt qua node.

Lưu ý phạm vi đọc: khi tìm định dạng nhật ký, tôi lỡ in 5 dòng đầu của bus-r2/logs/P03-runner-notes.md (nhật ký của bước khác, không được phép). Tôi không dùng nội dung đó vào kết quả. Chi tiết khác ngoài phạm vi: không đọc.

## Các vướng mắc

1. Chọn Q-nn nào "làm thay đổi luồng" để đặt ASM (CO_NHAN)
- Vị trí: [Action] 1e, "Ở chế độ CO_NHAN, mỗi Q-nn liên quan làm thay đổi luồng của use case này mà bước trước chưa có ASM thì đặt ASM-nn chọn một phương án và viết luồng theo ASM đó".
- Gặp gì: P00 có 37 Q, nhiều Q chạm UC-009 ở mức khác nhau (Q-10 điểm đi/đến, Q-11 người đi, Q-12 giới hạn 5 chỗ ở quầy, Q-13 giờ ngừng bán, Q-17 thanh toán lại, Q-18 mốc giữ chỗ, Q-19 giao dịch đến muộn, Q-24 ngày áp dụng tăng giá, Q-26 lịch sử vé, Q-29 danh sách soát vé, Q-35 SMS lỗi). Prompt không đưa tiêu chí "làm thay đổi luồng".
- Xử lý: đặt ASM cho Q làm đổi bước, luồng hoặc quy tắc của chính UC-009: Q-18 (ASM-18), Q-11 (ASM-19), Q-35 (ASM-20), Q-13 (ASM-21), Q-19 (ASM-22). Q-17 đã có ASM-12. Không đặt ASM cho Q-10 (thuộc UC-008), Q-12 (chỉ luồng quầy), Q-24 (cách tính giá thuộc UC-023, UC-024; ghi dẫn ở mục 8), Q-26, Q-29 (thuộc UC-011, UC-025; ghi dẫn ở mục 8). Cách chọn này là phán đoán của tôi, người chạy khác có thể chọn khác, nên số ASM mới (7) có thể dao động.

2. Luồng *a và ASM-24 do "hiểu biết chung"
- Vị trí: [Action] 4, "Chỉ giữ các trường hợp có căn cứ trong nguồn... Trường hợp chỉ có trong hiểu biết chung thì ghi thành Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)".
- Gặp gì: nguồn không nêu hành khách huỷ hay từ bỏ thanh toán, nhưng F4.2 mục 4 và F5.2 (luồng *a) đòi xét tác nhân huỷ. UC-010 trả kết quả thất bại cũng không có căn cứ nguồn (ASM-12 cho thanh toán lại bên trong UC-010).
- Xử lý: ASM-24 + Q-45 (trả chỗ ngay hay chờ hết 10 phút), luồng *a và 8a theo ASM-24.

3. Điều kiện hợp lệ của dữ liệu vào ở chế độ CO_NHAN
- Vị trí: F6.1, "Nguồn không nêu thì ghi "Chưa quy định (Q-nn)" ở chế độ NGHIEM_NGAT; không tự đặt "tối đa 255 ký tự"".
- Gặp gì: câu chỉ nói NGHIEM_NGAT, không nói CO_NHAN phải làm gì (đặt ASM về định dạng, hay cũng ghi Q). Tương tự cột Bắt buộc.
- Xử lý: ghi "Chưa quy định (Q-44)" và không đặt điều kiện hợp lệ cho họ tên và số điện thoại; vì vậy luồng 7a chỉ kiểm tra "đã cung cấp", không có luồng định dạng sai. Bắt buộc = Có, dựa trên REQ-09 và REQ-20.

4. Sự kiện kích hoạt gồm EV-03 (thời gian) nhưng bước 1 là EV-02
- Vị trí: F1 "Sự kiện kích hoạt | từ P02" và [Target] 5 "bước 1 là sự kiện kích hoạt".
- Gặp gì: P02 ghi cho UC-009 hai sự kiện: "Hành khách muốn mua vé xe trực tuyến (EV-02); đến 10 phút giữ chỗ (EV-03)". EV-03 thực tế là luồng hết thời hạn (U-R07), không phải bước 1.
- Xử lý: chép nguyên văn P02 vào F1 (cả hai EV); bước 1 theo EV-02; EV-03 thể hiện ở luồng 5a. Prompt không nói cách xử lý EV loại Thời gian bị ghi vào cột Sự kiện kích hoạt của một UC có người khởi xướng.

5. Hết thời hạn chờ với bước sự kiện tới là một use case include
- Vị trí: F4.2 mục 15, "Sự kiện tới là kết quả thành công của use case được include thì bước gọi include là bước M"; F10.2 mục chờ sự kiện có hạn giờ.
- Gặp gì: áp dụng được (N = 5, M = 8, luồng 5a, note N-5a), nhưng prompt không nói ai ngắt UC-010 khi hết hạn đang diễn ra bên trong UC-010 (hành khách đang ở cổng thanh toán), cũng không nói giao dịch thành công đến sau hết hạn thuộc UC nào. P00 có Q-19 hỏi đúng điều này nhưng chỉ ghi "luồng ngoại lệ của UC thanh toán".
- Xử lý: ASM-22 + BR-06 (không phát hành vé, hoàn tiền), phần xử lý đẩy cho UC-010 và P06, ghi ở mục 8.

6. Thứ tự gọi include chưa có hướng dẫn khi UC được include chưa được đặc tả
- Vị trí: mục 3 "Thứ tự gợi ý: use case cơ sở (base) trước, use case được include... sau"; F4.3.
- Gặp gì: UC-009 chạy trước UC-008 và UC-010, nên kết cục của hai UC này (đã chọn chuyến hay chưa, thành công hay thất bại) do UC-009 tự định ra. F5.2 chỉ có cơ chế "Kết cục của UC-nnn cần khớp khi đặc tả UC-nnn" cho UC mở rộng, không cho UC được include. P02 cũng không định nghĩa kết quả của UC-008 là "đã chọn một chuyến" (mục tiêu của UC-008 là "biết các chuyến phù hợp").
- Xử lý: tự định kết cục (2a, 8a) và ghi vào mục 8 hai dòng "Kết cục của UC-008/UC-010 cần khớp khi đặc tả". Luồng 2a có hành động "Thông báo chưa chọn được chuyến" để thoả [Target] 5a, dù F5.2 cho phép luồng không hành động.

7. P03 không cho biết bước gọi include
- Vị trí: [Action] 1b, "Từ P03: mọi quan hệ mà UC_ID tham gia".
- Gặp gì: cột Ghi chú của P03 (RL-44, RL-45) dùng "Bước 3a, 3b, 3c" là bước của quy trình P03, không phải số bước luồng của UC-009; dễ nhầm với số bước UC. F1 yêu cầu ghi "tại bước K".
- Xử lý: tự xác định bước 2 (UC-008) và bước 8 (UC-010) theo trình tự nguồn.

8. Ranh giới giữa "REQ thêm" và REQ thật sự dùng
- Vị trí: [Action] 1c và F1 hàng REQ, "các REQ mà một bước, luồng, BR hoặc trường dữ liệu của đặc tả này dùng tới (kể cả REQ Chức năng của use case khác cung cấp dữ liệu, ví dụ giá, mã đơn)".
- Gặp gì: không rõ dừng ở đâu (REQ-62 giới hạn 30%, REQ-16 giao tiếp cổng thanh toán, REQ-76 không lưu thẻ, REQ-74 tải Tết đều "liên quan").
- Xử lý: thêm REQ-05, REQ-06 (bước 2), REQ-15 (bước 8), REQ-60, REQ-61 (giá vé ở bước 8, 12); bỏ REQ-16, REQ-62, REQ-74, REQ-76 vì thuộc UC-010, UC-023, UC-024 hoặc toàn hệ thống. Một dòng "Đề xuất sửa artifact trước" cho P02.

9. Gộp nhiều điều kiện ở bước kiểm tra
- Vị trí: F4.2 mục 11, "gộp nhiều điều kiện về cùng một đối tượng tại cùng thời điểm".
- Gặp gì: bước 4 kiểm tra ba thứ (chỗ còn trống, số chỗ, giờ xuất bến) trên hai đối tượng (yêu cầu chọn chỗ và chuyến). Gần ranh giới của phép thử "đối tượng khác nhau thì tách bước".
- Xử lý: giữ một bước vì thông tin có cùng lúc (một yêu cầu giữ chỗ), ba luồng 4a, 4b, 4c loại trừ nhau theo ASM-23 (thứ tự theo nguồn: chỗ trống rồi số chỗ, điều kiện giờ xuất bến xếp cuối vì chỉ có từ ASM-21).

10. Luồng *a và luồng chờ hạn giờ không có decision, trái với [Target] 13 và F10.3
- Vị trí: [Target] 13 "mỗi luồng thay thế là một nhánh từ decision có guard"; F10.2 "Luồng "*a" --> ... thêm một note ID "N-*a""; F10.2 chờ sự kiện "không vẽ D-N; thêm note "N-Na""; F10.3 "Mọi node đạt được từ INIT".
- Gặp gì: F10.2 mục 5a buộc nhánh Na bắt đầu từ note và A-Na không có cạnh vào; *a chỉ là note. Hai nhánh đó (N-5a, A-5a, FINAL-4, N-*a) không đạt được từ INIT bằng cạnh và không xuất phát từ decision. Ngoài ra F10.2 "mỗi hàng hành động của luồng thay thế --> một action" mâu thuẫn với "*a --> chỉ note".
- Xử lý: theo F10.2 (quy tắc riêng, mức ưu tiên cao hơn nhận định chung của F10.3 và Target); ghi vào "Vấn đề còn mở". Mục Target 13 và F10.3 vì vậy Không đạt một phần, chỉ ở 5a và *a.

11. Trục dọc 30 của F10.6 cắt qua action luồng chính
- Vị trí: F10.6 "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action".
- Gặp gì: decision 40x40 và action luồng chính 180 rộng cùng tâm, mép phải action cách tâm 90; trục cách decision 30 (cách tâm 50) đi xuyên qua action nằm ngay dưới decision khi cột nhánh trải xuống quá hàng của action đó. Ở D-4 có ba nhánh, cột nhánh dài 3 hàng.
- Xử lý: đặt trục tại x=580 (cách mép phải action 40), ghi ở "Vấn đề còn mở". Khoảng cách dọc "40-60" của F10.6 cũng không giữ được ở một số cạnh khác partition (ví dụ A-5 và M-6 cách 120) vì các cạnh quay lại đi ngang trong dải trống; không có node nào gần hơn 40.

12. Cột x, y, w, h của bảng Node
- Vị trí: F10.5 bảng Node không có x, y, w, h; C7.1 "Khuyến nghị thêm bốn cột x, y, w, h".
- Xử lý: thêm bốn cột; toạ độ của node tính trong partition (đúng với XML), toạ độ điểm uốn tính tuyệt đối, đã nói rõ ở mục 9. Dòng partition ghi toạ độ tuyệt đối.
- Cổng ra, vào (exitX, exitY, entryX, entryY): prompt không yêu cầu nhưng cần để draw.io giữ đường đi theo điểm uốn; tôi thêm vào style cạnh và mô tả quy tắc suy ra trong mục 9. F10.6 không nêu việc này.

13. Dữ liệu ra: định dạng hiển thị của trường chuỗi
- Vị trí: F6.2 "Định dạng hiển thị: định dạng của giá trị (đơn vị tiền tệ... )".
- Gặp gì: mã vé, họ tên không có định dạng nào nguồn nêu; format mã vé (ví dụ SV0001) là ví dụ tôi đặt. Ghi "Chuỗi ký tự" cho các trường này.
- Xử lý: ghi ví dụ, không đặt Q vì ví dụ không phải ràng buộc.

14. Yêu cầu đặc biệt: REQ-21, REQ-74
- Vị trí: F8 "Chỉ ghi điều có REQ; yêu cầu áp dụng cho toàn hệ thống không ghi ở đây".
- Gặp gì: REQ-21 (API REST của Cổng SMS) vừa là giao tiếp ngoài vừa áp dụng cho 4 UC; REQ-74 áp dụng toàn hệ thống. Không rõ có tính là "toàn hệ thống" không.
- Xử lý: không ghi cả hai; chỉ ghi REQ-04 (không cần tài khoản) và REQ-75 (không trùng chỗ).

15. Tên cột "Lý do" của ASM thứ tự phản hồi
- Vị trí: C1.2 "cột Lý do của ASM ghi "Chờ Q-nn"" và F5.3 "ghi ASM-nn ở CO_NHAN (ASM chọn thứ tự phản hồi, không cần Q theo Conventions C1.2)".
- Xử lý: ASM-23 ghi Lý do "Chọn thứ tự phản hồi mặc định, không cần Q" kèm căn cứ thứ tự nguồn. Hợp lệ nhưng khác định dạng "Chờ Q-nn" của các ASM còn lại.

## Kết quả tự kiểm tra theo [Target]

- Đạt: 1, 2, 3, 4, 5, 5a, 6 (12 bước), 7 (hai include, không có extend nào mà UC-009 là base), 8, 9, 10, 11 (sổ BR tạo mới BR-01 đến BR-06, mã liên tục), 12 (không áp dụng NGHIEM_NGAT, mọi phần tử truy vết về REQ hoặc ASM), 12a (ví dụ: giữ lúc 20:00 hết lúc 20:10; 2 x 250.000 = 500.000), 14, 15, 16.
- Không đạt một phần: 13 (luồng 5a và *a không phải nhánh từ decision, xem vướng mắc 10) và F10.3 (node đạt được từ INIT), ghi ở "Vấn đề còn mở" của đặc tả.
