# Nhật ký người chạy P11a-GD1

Model: Sonnet (tham số model sonnet của công cụ Agent).

Phạm vi lần chạy: P11a-gui-design.md, CHE_DO_CHAY = "Giai đoạn 1". Đầu ra: P11a-gui/ui-standards.md, screen-list.md, screen-transition.md, diagrams/P11a-screen-transition.drawio. Mã mới cấp: Q-84 đến Q-87, ASM-59, ASM-60 (mã lớn nhất đã thấy ở đầu vào là Q-83 và ASM-58 trong P09; P11b chạy song song cấp từ Q-100, ASM-100 nên không trùng). Mã MSG-01 đến MSG-39; SCR-01 đến SCR-19.

## Vướng mắc đã gặp

1. Vị trí: mục 2, hàng P09 và P10: "danh sách boundary cần màn hình (P10 mục F3, dòng có phần tử thiết kế ở layer giao diện)". Gặp: bảng F3 của P10 có các cột AC, Kết quả, Phần tử thiết kế, PKG, Lý do, không có cột layer. Xử lý: đối chiếu cột PKG của F3 với bảng F4 (PKG-05, PKG-26, PKG-27, PKG-07 đều thuộc PKG-01 Presentation) để xác định 5 boundary giao diện người dùng. Nên thêm cột layer vào F3 của P10 hoặc sửa câu trong prompt thành "đối chiếu F4".

2. Vị trí: mục 4 [Action] A6 nằm dưới "Giai đoạn 2", nhưng [Format] F7 ghi "tổng hợp ở cuối screen-list.md", [Target] 9 ghi "Mọi màn hình đã được đánh giá theo F7" và F7 ghi "Luôn ghi các dòng vi phạm. Dòng cho tiêu chí Đạt và Không áp dụng (chỉ khi DAY_DU): ghi thêm để bảng phủ mọi tiêu chí". Gặp: ở giai đoạn 1 chưa có hình ảnh, bảng điều khiển, bảng thuộc tính trường nên chưa đánh giá được từng màn hình; bảng đầy đủ cho 19 màn hình khoảng 1000 dòng. Xử lý: ghi mục 3 của screen-list.md đánh giá chuẩn hoá và cách nhóm màn hình, mỗi tiêu chí một dòng, cột SCR gom theo phạm vi áp dụng; ghi rõ đánh giá trên hình ảnh để giai đoạn 2. Target 9 chỉ đạt một phần (còn 3 nhóm vi phạm còn mở, đều có Q-86, Q-87). Câu "(chỉ khi DAY_DU)" cũng mơ hồ: không rõ áp dụng cho dòng Đạt hay chỉ cho dòng Không áp dụng; hiểu là áp dụng cho cả hai và hồ sơ ghi MUC_CHI_TIET là DAY_DU.

3. Vị trí: A2 "Màn hình điều hướng ... chỉ chứa lối vào các use case của tác nhân đó trong P02" cùng YEU_CAU_BO_SUNG "các use case khác mới có trong P02". Gặp: P02 có 18 use case, chỉ 4 có P04, P07; màn hình điều hướng phải liệt kê cả use case chưa có màn hình đích, nên có lối vào "treo" (UC-001, UC-007, UC-009, UC-011, UC-004, UC-005, UC-012). Xử lý: vẫn tạo SCR-01, SCR-09, SCR-13, ghi các lối vào treo ở cột Boundary AC nguồn, cột UC và ghi chú node; quy định STT 35 ghi mục menu của use case chưa có màn hình chỉ đưa vào bản dựng khi có màn hình. Prompt không nói điều hướng nên phủ use case chưa phân tích hay không.

4. Vị trí: A2 "Thông điệp ngắn ... dùng hộp thông điệp chuẩn ..., không cần mã SCR riêng, trừ khi có nội dung, điều khiển riêng ngoài mẫu chuẩn" và F2 loại "Con phụ thuộc (pop-up modal ...)". Gặp: ranh giới giữa hộp thông điệp chuẩn (không SCR) và màn hình con phụ thuộc (có SCR) không có tiêu chí rõ. Xử lý: hộp xác nhận trả vé và huỷ chuyến có 5 đến 7 trường dữ liệu và hai nút theo hành động nên là SCR-07, SCR-11, SCR-15 loại Con phụ thuộc; mọi thông điệp còn lại là MSG. Đã ghi lựa chọn ở Vấn đề còn mở của screen-list.md.

5. Vị trí: F3 bốn mẫu dịch chuyển và quy tắc "Không vẽ cạnh đóng pop-up". Gặp: bốn mẫu không nói pop-up khi thao tác xác nhận xong thì chuyển sang màn hình mới (SCR-07 --> SCR-08) thuộc mẫu nào; cũng không nói luồng "Kết thúc use case (thất bại)" của P04 sau thông điệp thì đi đâu. Xử lý: cạnh pop-up sang màn hình kết quả dùng mẫu 4 (dữ liệu truyền là kết quả); sau thất bại kết thúc use case ở UC-002 luồng 9a2 vẽ cạnh E-06 mẫu 1 về SCR-02 theo MSG-10; các kết thúc thất bại khác (UC-008, UC-013) giữ nguyên màn hình đầu use case, không vẽ cạnh. Hai quyết định này là suy luận của người chạy.

6. Vị trí: A3 "Kiểm tra mọi màn hình đến được từ màn hình khởi đầu của tác nhân, và mọi màn hình có lối thoát" và F3 "Mỗi tác nhân có một node Start ..., chỉ khi đặc tả có điểm khởi đầu đó". Gặp: P04 và P02 không có màn hình khởi đầu hay màn hình đăng nhập cho nhân viên và phụ xe (chỉ có ASM-09 "đã được xác thực" và Q-27 ở P02). Xử lý: tạo 4 node Start và ghi ASM-60 (điểm khởi đầu, màn hình đầu tiên của mỗi tác nhân). Màn hình kết thúc (SCR-05, 08, 12, 16, 19) coi là lối thoát "có ghi rõ"; liên kết tên hệ thống về trang chủ ghi ở quy định STT 39 và không vẽ cạnh. Quy tắc "mọi SCR có lối ra" và "cạnh quay lại chỉ vẽ khi có trong đặc tả" gần như mâu thuẫn với nhau cho các màn hình kết thúc; đã chọn không vẽ cạnh về trang chủ.

7. Vị trí: F2 cột "Loại (theo mẫu dịch chuyển dẫn tới màn hình)" và A2 "Phân loại mỗi màn hình theo mẫu dịch chuyển dẫn tới nó (F2)". Gặp: Loại của màn hình phụ thuộc vào cạnh vào, mà cạnh chỉ được xác định ở A3, sau khi lập screen-list; một màn hình có nhiều cạnh vào với mẫu khác nhau (chưa gặp ở đề này) cũng chưa có quy tắc. Xử lý: lập screen-list và screen-transition cùng lúc, kiểm tra khớp Loại với mẫu cạnh vào (SCR-02 nhận mẫu 1 từ SCR-01 và SCR-04, nhất quán).

8. Vị trí: F7 và [Format] F1 ví dụ đúng "Nút chính: ... cao 40 px". Gặp: 40 px thấp hơn Apple HIG 44 pt trong khi website hành khách nhận cả cảm ứng (THIET_BI_HIEN_THI). Xử lý: web hành khách 44 px (điện thoại 48 px), web nhân viên 40 px, Android 48 dp; ghi chọn theo C9 trong Vấn đề còn mở của ui-standards.md và ghi hai dòng "Vi phạm đã sửa" ở F7 (chiều cao nút và header cố định che tiêu điểm) vì bản nháp đầu của người chạy mắc hai lỗi này; đây là sửa trong quá trình soạn, không phải lỗi của prompt.

9. Vị trí: F1 nhóm Help "vị trí trợ giúp, nhất quán thuật ngữ với glossary và tài liệu hướng dẫn; trợ giúp theo ngữ cảnh". Gặp: nguồn, P04, P06 không có tài liệu hướng dẫn hay yêu cầu trợ giúp; thêm trang trợ giúp là thêm chức năng. Xử lý: chỉ quy định gợi ý theo ngữ cảnh dưới nhãn trường (STT 53), không có trang trợ giúp (STT 54), ghi Q-86; hệ quả là Nielsen 10 ghi "Vi phạm còn mở" và WCAG 3.2.6 ghi "Không áp dụng".

10. Vị trí: A1 "Căn cứ theo thứ tự: NFR và ràng buộc trong P06, hồ sơ dự án ...". Gặp: P06 không có NFR về khả dụng, khả năng tiếp cận, ngôn ngữ giao diện; hồ sơ dự án cũng không có. Hầu hết căn cứ rơi về mức chuẩn chung (WCAG 2.2 AA, Nielsen, Material, HIG) và THIET_BI_HIEN_THI. Xử lý: ghi căn cứ từng dòng, ghi ASM-59 cho ngôn ngữ chỉ tiếng Việt, ghi đề xuất bổ sung NFR vào P06.

11. Vị trí: mục 2 "P04-uc-specs/ ... bảng dữ liệu vào ra" và UC-002 bước 10 gọi UC-003. Gặp: UC-003 Thanh toán vé trực tuyến chưa có P04, P07 và không có boundary giao diện ở P08; nội dung thanh toán (chuyển sang cổng hay form nhúng) không có căn cứ. Xử lý: SCR-04 chỉ gồm phần UC-002 (xem lại chỗ, người đi, tổng tiền BR-06, đồng hồ giữ chỗ BR-07, thông điệp 9a2 và 10a, nút Thanh toán), ghi Q-84 và đề xuất chạy P04, P07 cho UC-003. Đồng hồ giữ chỗ và nút Thanh toán không nằm trong bảng dữ liệu ra của P04 mà suy từ BR-07 và bước 10; đã ghi căn cứ.

12. Vị trí: C3 "Lần chạy nào cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất đã thấy, rồi cấp tiếp". Gặp: mã Q, ASM xuất hiện cả trong văn bản tham chiếu lẫn bảng Câu hỏi mở; tìm bằng grep trên mọi artifact đầu vào cho Q-83 (P09) và ASM-58 (P09). Mã P10 có Q-79, không có ASM. Có phiên song song cấp từ Q-100, nên tồn tại khoảng trống Q-88 đến Q-99 là chủ ý. Prompt không nêu cách tìm trong tình huống hai phiên chạy song song.

13. Vị trí: C7.1 bảng Node "Thuộc về (container)" và F3 "Thuộc về (tác nhân)", F3 cột Loại chỉ có "Screen / Start". Gặp: sơ đồ gom theo tác nhân cần container (partition) nhưng cột Loại không có giá trị Partition. Xử lý: giữ bảng Node đúng hai giá trị Loại, thêm bảng Partition riêng trong screen-transition.md; cột x, y, w, h là toạ độ tuyệt đối còn .drawio ghi toạ độ tương đối theo partition (đã nêu ở đầu file).

14. Vị trí: C7.3 "dùng edgeStyle=orthogonalEdgeStyle cho sơ đồ lớp, sơ đồ package, ERD" và F3 style từng mẫu. Gặp: F3 quy định nguyên chuỗi style; sơ đồ dịch chuyển không nằm trong danh sách cần orthogonalEdgeStyle nhưng có hai cạnh cần đi vòng. Xử lý: giữ nguyên chuỗi style của F3, thêm fontSize, labelBackgroundColor và điểm neo exit, entry; cạnh E-06 và E-07 dùng điểm uốn tường minh theo cột Điểm uốn của C7.1.

15. Vị trí: F3 "Bố cục: màn hình là hình chữ nhật ... rộng 160, cao 60". Gặp: chữ gồm mã, stereotype và tên màn hình (ví dụ "SCR-03 «Phụ thuộc có dữ liệu»" cộng tên dài) không vừa node cao 60 ở cỡ chữ mặc định. Xử lý: đặt cỡ chữ 10; chưa mở draw.io để kiểm tra chữ có tràn không (ghi ở Vấn đề còn mở của screen-transition.md).

16. Vị trí: F1 "Danh mục thông điệp: mỗi thông điệp hệ thống nêu trong đặc tả (lỗi, xác nhận, thành công, đang xử lý)". Gặp: P04 không nêu thông điệp đang xử lý, lỗi hệ thống, lỗi mất kết nối; mặt khác kết quả quét "Hợp lệ"/"Không hợp lệ" của UC-015 là dữ liệu ra chứ không hẳn là thông điệp. Xử lý: MSG-01, 02, 03, 13, 14, 25, 30, 39 là thông điệp chuẩn theo A1 (Nielsen 1, 9), ghi nguồn là chuẩn; MSG-33 đến MSG-36 là kết quả quét hiển thị trong vùng kết quả, không phải hộp. Cột Loại chỉ có 5 giá trị nên thông báo huỷ yêu cầu (UC-008 6a, UC-013 4a) xếp "Xác nhận" cho gần nghĩa nhất, thông báo "Không có chuyến/vé" xếp "Lỗi".

17. Vị trí: F1 và F5 về mã quy định chuẩn hoá. Gặp: C3 không có mã cho từng quy định ở ui-standards.md, trong khi screen-list.md và các bước sau cần trích chúng. Xử lý: dùng "quy định STT n" làm tham chiếu; nếu sau này chèn dòng giữa bảng, tham chiếu bị lệch. Nên cấp mã cho quy định hoặc ghi rõ STT không đổi khi chạy lại.

18. Quá tải ngữ cảnh: tổng đầu vào cho phép khoảng 825 KB. Đã đọc đầy đủ: prompt, Conventions, README, hồ sơ dự án, nguồn, P01, P04 bốn use case (bỏ phần activity diagram), P06 mục 1 đến 6 và Câu hỏi mở. Đọc một phần: P02 (chỉ Bảng 4a, 4b), P05 (bảng thuật ngữ, cắt 330 ký tự mỗi dòng), P07 (UC-002 bảng message SD1; UC-008, UC-013, UC-015 chỉ lọc message của tác nhân và boundary, phần còn lại lấy từ P08), P08 (bảng lớp và Câu hỏi mở), P09 (tìm theo từ khoá mẫu giao diện, bảng PKG), P10 (F3, F4, các mục cuối). Có thể bỏ sót chi tiết ở P07 UC-008, UC-013, UC-015, P05 cột ghi chú.

## Mục Target không đạt hoàn toàn

- Target 3, 4 (nửa sau "được tham chiếu ở chức năng của điều khiển"), 6, 7, 8: thuộc giai đoạn 2 (đặc tả từng màn hình, bảng điều khiển, thuộc tính trường, dữ liệu mẫu); chưa có nên chưa kiểm tra được. Phần mã MSG phủ đủ các thông điệp của bốn P04 đã đạt.
- Target 9: một phần (xem mục 2 ở trên); còn Nielsen 3, Nielsen 10 và Shneiderman hoàn tác ghi "Vi phạm còn mở" (Q-86, Q-87).
- Target 11: bảng mô hình và .drawio khớp (sinh từ cùng dữ liệu), XML hợp lệ (đã kiểm bằng minidom), bố cục kiểm bằng tính toán; chưa mở bằng draw.io. Mockup HTML không áp dụng (XUAT_HTML là Không có).
- Target 1, 2, 5, 10, 12: đạt.

## Ghi chú khác

- Không có đầu vào nào không khớp tên file hoặc thiếu; P04-uc-specs có _BR-register.md không cần dùng ở giai đoạn 1.
- Placeholder không được nêu giá trị (NHAN_DIEN_THUONG_HIEU, MAU_DAC_TA_MAN_HINH, XUAT_HTML, THONG_TIN_TAI_LIEU) đặt "Không có"; theo C6 hiểu là không dùng. NHAN_DIEN_THUONG_HIEU Không có nên bảng màu là quyết định thiết kế, đã ghi ở ui-standards.md.
