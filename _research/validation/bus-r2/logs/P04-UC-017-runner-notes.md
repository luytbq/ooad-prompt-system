Model: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P04 UC-017 Huỷ chuyến

Đầu ra: design/P04-uc-specs/UC-017-cancel-trip.md; design/diagrams/P04-activity-UC-017.drawio (XML hợp lệ, 37 cạnh khớp bảng Edge); design/P04-uc-specs/_BR-register.md (thêm BR-07 đến BR-11, BR-04 thêm UC-017). Mã cuối: Q-50, ASM-33, BR-11.

## Vướng mắc

1. Mục 4 [Action] 4 và Conventions C1.2: "Trường hợp chỉ có trong hiểu biết chung thì ghi thành Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)" cùng C1.2 "ASM-nn có thể làm đổi luồng ... thì đi kèm Q-nn".
   - Gặp: UC-017 gần như không có chi tiết luồng trong nguồn (một câu ở Mục 6). Để có luồng đủ F5.5 phải tạo 9 ASM và 5 Q mới (trạng thái chuyến được huỷ, mốc, trạng thái vé, SMS lỗi, hoàn tiền lỗi, lối thoát *a, lý do huỷ, phạm vi SMS, hoàn một phần). Không có tiêu chí nào cho biết dừng ở đâu nên nguy cơ đặc tả bị "bịa" nhiều.
   - Xử lý: chỉ giữ giả định có hệ quả dữ liệu hoặc ràng buộc rõ (hoàn hai lần, soát vé, mốc); ASM-27 (lối thoát *a) coi là phản hồi mặc định nên không kèm Q. Mơ hồ: lối thoát *a có "đổi luồng" hay là "cách trình bày" thì có cần Q không.

2. Mục 4 [Action] 1e: "mỗi Q-nn liên quan làm thay đổi luồng ... mà bước trước chưa có ASM thì đặt ASM-nn".
   - Gặp: không rõ thế nào là "liên quan". Q-36 (lý do huỷ), Q-25, Q-20 xác định rõ; Q-29, Q-07 chỉ liên quan gián tiếp.
   - Xử lý: đặt ASM-25 (Q-36), ASM-30 (Q-25), ASM-32 (Q-20); Q-07 dùng ASM-08 sẵn có; Q-29 chỉ nhắc ở mục 8.

3. F4.2 mục 17 (mốc của use case do tác nhân thời gian kích hoạt): "có bước hệ thống 'Hẹn / hẹn lại / huỷ mốc <tên mốc> của UC-xxx'".
   - Gặp: huỷ chuyến làm mất hiệu lực giờ xuất bến, là mốc của hai use case (UC-007, UC-025). Câu mẫu chỉ có một mốc, một UC.
   - Xử lý: một bước 6 huỷ cả hai mốc; ghi ASM-28 chờ Q-47. Gợi ý bổ sung ví dụ nhiều mốc.

4. F5.4: "Tiếp tục bước K" với F10.2: bước "Lặp lại" không có action.
   - Gặp: luồng lỗi 9a và 12a của bên trong vòng lặp cần quay lại bước "Lặp lại" (10, 13), còn 7a và 10a (không action) nhập lại ở bước 14. Prompt không nói rõ đích là bước không có action thì vẽ thế nào.
   - Xử lý: thêm merge M-10, M-13 trước decision D-10, D-13 (decision một luồng vào, F10.3) và M-14 cho nhiều luồng nhập; mục "Vấn đề còn mở" ghi lại. Đồng thời luồng 10a (bỏ qua vòng lặp thứ hai) buộc decision lặp D-10 có ba nhánh; F10.2 chỉ mô tả hai guard (quay lại và đi tiếp) cho decision lặp.

5. F10.2 "Luồng *a" so với F10.3 "Mọi node đạt được từ INIT" và F5.2 (mỗi hàng hành động một action).
   - Gặp: note N-*a không đạt được từ INIT. Cùng vướng mắc như UC-009.
   - Xử lý: theo F10.2 (C9: quy tắc riêng của bước), ghi ở Vấn đề còn mở.

6. F10.6: "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải".
   - Gặp: trục 30 cắt qua action luồng chính rộng 180 nằm ngay dưới decision.
   - Xử lý: dùng trục x=700 (D-4) và x=980 (cạnh quay lại bước 3); các cạnh quay lại/bỏ qua dài đi theo làn bên trái x=320, 380. Ghi ở Vấn đề còn mở.

7. F10.4: "Thứ tự từ trái sang phải: tác nhân chính, hệ thống, các tác nhân phụ".
   - Gặp: không nêu thứ tự giữa hai tác nhân phụ có partition (Cổng SMS, Cổng thanh toán).
   - Xử lý: Cổng SMS trước Cổng thanh toán theo thứ tự xuất hiện trong luồng, để cạnh không cắt partition khác.

8. F3 Hậu điều kiện tối thiểu: "Use case không có luồng kết thúc thất bại: ghi ..." với F4.1.
   - Gặp: các luồng 4a, 4b quay lại bước 3, nên nếu không có *a thì use case không có đường thoát thất bại. Quyết định thêm *a (ASM-27) chỉ để có kết thúc thất bại hợp lý; prompt không nói khi nào nên thêm luồng huỷ của tác nhân (chỉ "tác nhân huỷ" ở [Action] 4).

9. F7.1 phân biệt BR và dữ liệu: "Chuyến chỉ huỷ vì xe hỏng hoặc thời tiết" có thể là chính sách (BR) hay điều kiện hợp lệ của dữ liệu.
   - Xử lý: xếp vào điều kiện hợp lệ của Dữ liệu vào 1 (ASM-25, Q-36), không cấp BR. Prompt không có tiêu chí phân biệt khi quy tắc là danh sách giá trị cho phép.

10. F4.4 và F4.2 mục 9: số bước 14, sát cận 15 vì hai bước "Lặp lại" cùng hai cặp yêu cầu - phản hồi với hệ thống ngoài. Chưa gộp thêm vì mỗi bước đã có kết quả nghiệp vụ riêng; ghi ở Vấn đề còn mở.

11. Phạm vi đọc: runner-template cho đọc P02R, P01 chỉ theo mục 3 của prompt; prompt bảo đọc "Câu hỏi mở, Giả định của mọi đặc tả P04 đã có" nên đã đọc các mục đó trong UC-009, và dùng UC-009 để lấy dữ liệu vé, giá vé, mã vé. Prompt không nói rõ UC khác có cần mô tả dữ liệu như vậy không.

## Target không đạt

Không có mục Target nào không đạt; hai ngoại lệ do mâu thuẫn quy tắc (F10.2 so với F10.3, F10.6 trục 30) đã ghi ở Vấn đề còn mở của đặc tả (vướng mắc 5, 6).
