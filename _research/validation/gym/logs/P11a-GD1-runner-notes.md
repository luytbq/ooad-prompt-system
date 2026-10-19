Model của phiên chạy: Sonnet

# Nhật ký người chạy - P11a giai đoạn 1 (lần chạy đầu) - gym

Đầu ra đã ghi: design/P11a-gui/ui-standards.md (77 quy định, 15 MSG, 53 dòng F7), design/P11a-gui/screen-list.md (16 SCR, 5 boundary không có màn hình), design/P11a-gui/screen-transition.md (22 node gồm 6 partition và 6 Start, 18 cạnh), design/diagrams/P11a-screen-transition.drawio (XML hợp lệ, kiểm tra bằng xml.dom.minidom). Q cấp mới: Q-95 đến Q-99 (lớn nhất Q-99). ASM: chưa cấp (NGHIEM_NGAT).

Cách kiểm tra: ba file .md và file .drawio sinh từ cùng một bộ dữ liệu bằng script ở thư mục tạm; script kiểm tra riêng toạ độ bội số 10, khoảng cách giữa node từ 40, node nằm trong partition, mọi đoạn cạnh thẳng ngang hoặc dọc và không cắt node. Chưa mở file bằng draw.io để xem bố cục (không có công cụ), nên vị trí nhãn cạnh chưa được nhìn bằng mắt.

## Mục Target không đạt hoặc đạt một phần

- Target 4 (mọi thông điệp có trong danh mục MSG và được tham chiếu ở chức năng của điều khiển): phần danh mục đạt (MSG-01 đến MSG-15); phần "được tham chiếu ở chức năng của điều khiển" chưa làm được ở giai đoạn 1 vì chưa có bảng điều khiển; để giai đoạn 2.
- Target 3, 6, 7, 8 (trường, hình ảnh, bảng điều khiển, thuộc tính trường, dữ liệu mẫu): thuộc giai đoạn 2, không đánh giá ở lần chạy này.
- Target 9 giai đoạn 1: mọi tiêu chí F7 đã được đánh giá nhưng còn 3 dòng Vi phạm còn mở (Nielsen 3, Nielsen 10, Shneiderman 6) vì sửa được chỉ bằng cách thêm chức năng mà đặc tả không có; đã gắn Q-57 (có sẵn) và Q-95. Không còn vi phạm WCAG AA chưa có cách xử lý.

## Vướng mắc

1. Mục 4, F3: "Mỗi tác nhân người có một node Start ... và một partition chứa các màn hình của tác nhân đó". Với đề này Khách vãng lai (ACT-03) là tác nhân người nhưng chỉ quét vé ở cửa quay, không có màn hình. Xử lý: không tạo Start và partition cho ACT-03, ghi rõ ở screen-transition.md. Prompt không nói tác nhân người không dùng phần mềm thì làm gì.

2. Mục 4, A2: "Màn hình điều hướng ... chỉ chứa lối vào các use case của tác nhân đó trong P02". P02 gán UC-004 Đăng nhập (subfunction) cho ACT-02 nhưng đăng nhập xảy ra trước phiên làm việc, nên đặt lối vào Đăng nhập ở Trang chủ Hội viên là vô lý, còn đặt ở màn hình của Người quan tâm lại vi phạm câu trên. Xử lý: không đưa UC-004 vào màn hình nào, ghi Q-99 (điểm khởi đầu ứng dụng di động và vị trí lối vào đăng nhập). Prompt thiếu hướng dẫn cho use case đăng nhập, use case chạy trước phiên.

3. Mục 4, F3: "mọi SCR có ít nhất một lối ra (cạnh đi, hoặc là pop-up đóng về cha, hoặc là màn hình kết thúc có ghi rõ)" cùng A2: "Lối vào use case chưa có màn hình đích ghi ở Ghi chú của node, không tính là lối ra". Với đề này 4 màn hình điều hướng (SCR-01, SCR-09, SCR-15, SCR-16) chỉ có lối vào chưa có màn hình đích, nên không có cạnh đi nào. Xử lý: ghi ở Ghi chú "màn hình kết thúc của sơ đồ cho tới khi các use case này có màn hình". Chưa chắc đây là ý của prompt vì màn hình điều hướng về bản chất không phải màn hình kết thúc; nên có câu hướng dẫn riêng.

4. Mục 4, F1 ví dụ đúng: "Nút chính: nền màu chủ đạo, chữ trắng" và A1: thứ tự căn cứ "NHAN_DIEN_THUONG_HIEU --> hướng dẫn nền tảng --> chuẩn chung (... WCAG 2.2 AA ...)", cùng Target 9: "không còn vi phạm WCAG AA". Với đề này màu chủ đạo #E4572E: chữ trắng trên nền này đo 3,68:1 (dưới 4,5:1), chữ #E4572E trên nền trắng cũng 3,68:1. Không thể thoả cả "đúng nhận diện" và 4,5:1 cho chữ thường. Xử lý: giữ #E4572E làm nền nút chính, nhãn nút chính là chữ lớn in đậm 20 (cần 3:1, đạt), cấm dùng #E4572E làm màu chữ, ghi mâu thuẫn ở Vấn đề còn mở theo C9. Prompt không nêu cách xử lý khi màu thương hiệu không đạt tương phản; thứ tự căn cứ nói thương hiệu đứng trước chuẩn chung nhưng Target đòi không vi phạm.

5. Mục 4, F1: "Cột STT là mã quy định ... Các file khác trích dạng 'UI-STT nn'". C3 không có dòng mã cho quy định chuẩn hoá, nên không rõ STT là số trần hay có tiền tố. Xử lý: STT là số nguyên, trích là "UI-STT n".

6. Mục 4, [Format]: "Tiêu đề: '# P11a - <Tên file> - <Tên hệ thống>'". Không rõ <Tên file> là tên tệp (ui-standards) hay tên mô tả. Chỉ có SCR-nn-slug.md được giải thích. Xử lý: dùng tên mô tả tiếng Việt (Chuẩn hoá cấu hình màn hình, Danh sách màn hình, Sơ đồ dịch chuyển màn hình).

7. Mục 4, A2: "Thông điệp ngắn (lỗi, xác nhận có hoặc không) dùng hộp thông điệp chuẩn ... trừ khi có nội dung, điều khiển riêng ngoài mẫu chuẩn". Ranh giới giữa hộp thông điệp và màn hình không có tiêu chí đo được. Với đề này hộp "Lớp đã đủ chỗ, vào danh sách chờ không?" có hai nút và dẫn sang màn hình khác; tôi xếp là MSG (MSG-09). Kèm theo, F3 nói "Pop-up ... dẫn sang màn hình mới sau khi xác nhận: vẽ cạnh từ pop-up", nhưng hộp MSG không phải node, nên không có nguồn cho cạnh. Xử lý: vẽ cạnh từ màn hình cha SCR-06 sang SCR-08 (TR-09) và ghi sự kiện "Nhấn Vào danh sách chờ trong MSG-09". Prompt thiếu quy tắc cho trường hợp này.

8. Mục 4, F3: "Cạnh quay lại màn hình trước (nút Quay lại) chỉ vẽ khi nó là một dịch chuyển có trong đặc tả hoặc chuẩn A1 quy định rõ" cùng mục NHAN_DIEN: "logo VietFit ở góc trên bên trái". Logo chiếm vị trí mà iOS thường đặt nút Quay lại; prompt không nói cách dung hoà thương hiệu với điều hướng quay lại theo nền tảng. Xử lý: nút Quay lại là nút phụ ở vùng hành động chỉ ở SCR-04 và SCR-12 (trước khi ghi dữ liệu), nút quay lại hệ thống đưa về màn hình điều hướng; quy định ở UI-STT 15 và vẽ TR-05, TR-14. Đây là quyết định thiết kế của tôi, không có căn cứ trực tiếp trong prompt.

9. Mục 4, F1 nhóm Menu và A2 màn hình điều hướng: prompt không nói quan hệ giữa menu chung và màn hình điều hướng (menu có lặp lại danh sách lối vào không). Xử lý: ứng dụng di động chỉ có nút Trang chủ, ứng dụng web có menu trái lặp danh sách lối vào; ghi "Mọi màn hình có menu tới <SCR>" ở Start. Với di động, menu một mục là một chỗ thiếu hướng dẫn.

10. Đầu vào không khớp: P04 UC-005 luồng chính bước 9, 10 (cổng thanh toán) ghi áp dụng cho "Hội viên / Lễ tân", còn luồng 8a, 8b mới nói lễ tân thu tiền mặt hoặc POS và nguồn (Mục 2 câu 4) chỉ nêu tiền mặt hoặc POS tại quầy; P07 SD2 vẽ alt ba toán hạng. Không rõ SCR-13 có hình thức thu qua cổng không. Xử lý: Q-98, SCR-13 chỉ có tiền mặt và POS.

11. Đầu vào không khớp: P04 UC-018 Tiền điều kiện "mã QR của hội viên đang hiển thị trên ứng dụng" và P09 PKG-05 liệt kê "UC-018 (hiển thị mã QR)", nhưng P08 không có boundary giao diện người dùng cho việc hiển thị mã nên P10 F3 không có View; theo A2 và Target 2 màn hình mã QR sẽ mồ côi. Xử lý: không tạo màn hình, lối vào UC-018 ở SCR-02 ghi Chưa có màn hình đích, Q-97 và dòng Đề xuất sửa P04, P08, P10. Prompt không nói phải làm gì khi một bước cần giao diện nhưng chuỗi artifact trước không có boundary.

12. Đầu vào thiếu: mục 2 của prompt nêu P06 cung cấp "NFR về khả dụng, khả năng tiếp cận, hiệu năng hiển thị, ngôn ngữ", nhưng P06 của đề này chỉ có NFR hiệu năng của đặt chỗ và cửa quay, ràng buộc nền tảng (NFR-03, NFR-04), không có NFR khả dụng, tiếp cận, ngôn ngữ. Các quyết định như giao diện chỉ tiếng Việt, chỉ chế độ sáng, mức WCAG AA được tôi coi là quy định trình bày ("được phép quyết định ở cả hai chế độ") kèm căn cứ; ranh giới giữa "quy định trình bày" và "yêu cầu phi chức năng mà nguồn không nêu" (ví dụ có song ngữ hay không) không rõ. Chỉ Q-95 (trợ giúp) và Q-78 (trình duyệt, hệ điều hành) được dùng.

13. Mục 4, A1: "Trước khi cấp Q mới, tìm câu hỏi cùng nội dung trong mục Câu hỏi mở của artifact đầu vào (P09, P10, P11b nếu đã có)" nhưng các câu hỏi liên quan (Q-47, Q-13, Q-53, Q-68, Q-70) nằm ở P04, P06, P07, P01. Tôi tra thêm các file này (trong phạm vi được đọc). Ngoài ra prompt không nói Q mới của một lần chạy giai đoạn 1 đặt ở file nào trong ba file; tôi chia theo nội dung (Q-95 ở ui-standards.md, Q-96 đến Q-98 ở screen-list.md, Q-99 ở screen-transition.md) để mỗi mã chỉ xuất hiện trong một bảng Câu hỏi mở.

14. Mục 4, F7: "Giai đoạn 1 đánh giá ui-standards.md theo từng tiêu chí" nhưng cũng nói "Khi MUC_CHI_TIET là DAY_DU, thêm một dòng 'Các tiêu chí còn lại ...' thay cho từng dòng". Hồ sơ dự án có MUC_CHI_TIET = GON, giá trị này không được định nghĩa trong prompt (chỉ nhắc DAY_DU), nên không biết GON có làm gọn bảng F7 giai đoạn 1 không. Xử lý: ghi đủ từng tiêu chí (53 dòng) vì mục 4 bắt buộc "mọi tiêu chí F7". Ngoài ra dòng Material, HIG "màn hình web không ghi hai dòng này" nên với ui-standards.md (gộp cả hai nền tảng) tôi ghi một dòng cho Android và một dòng cho iOS.

15. Mục 4, F7: "Shneiderman (chỉ đánh giá ở bảng tổng hợp của screen-list.md và bảng của ui-standards.md)" trong khi bảng tổng hợp ở screen-list.md chỉ lập ở giai đoạn 2 cuối. Xử lý: tạo mục "Bảng tổng hợp đánh giá chuẩn" ghi Chưa có, lập ở giai đoạn 2.

16. Mục 4, F1 và Target 1 đòi nhóm Help có quy định cụ thể ("vị trí trợ giúp") trong khi đặc tả không có chức năng trợ giúp và prompt cấm tự thêm chức năng. Xử lý: UI-STT 63 quy định không có màn hình hay nút Trợ giúp, chỉ chú thích theo ngữ cảnh (UI-STT 64), Q-95; hai dòng F7 (Nielsen 10) ghi Vi phạm còn mở. Hai yêu cầu của prompt xung đột ở nhóm này.

17. Mục 4, F3 bảng Node: cột "Stereotype (Loại màn hình ở F2)" không có giá trị với Start và Partition; ghi "-". Cột "Thuộc về (tác nhân)" của Start và Partition cũng tự ghi tác nhân. Bảng Node của C7.1 khuyến nghị thêm x, y, w, h; tôi thêm và nói rõ toạ độ tuyệt đối còn file .drawio dùng toạ độ tương đối của partition, vì prompt không nêu.

18. Mục 4, F3 style: "Style: dashed=1;endArrow=open;endFill=0;html=1;" gọi là "bắt buộc dùng đúng", còn C7.3 yêu cầu cạnh không cắt qua node và C7.1 cho điểm uốn. Để cạnh đi thẳng ngang dọc khi không có edgeStyle, tôi nối thêm exitX, entryX... và fontSize, labelBackgroundColor sau chuỗi style gốc. Không rõ nối thêm thuộc tính có được coi là "đúng" không. Hai cạnh đi ngược chiều giữa cùng một cặp node (TR-04 và TR-05, TR-13 và TR-14) phải tách cổng ra, vào để không chồng nhau; prompt không có hướng dẫn.

19. Mục 4, F2: "Tên: cụm từ ngắn nêu việc tác nhân làm trên màn hình (màn hình thao tác) hoặc nội dung hiển thị (màn hình kết quả)". Màn hình xác nhận (SCR-04, SCR-12) không thuộc hai loại nào; đặt tên theo việc làm ("Xác nhận đơn mua"). Và UC-005 sinh 7 màn hình trong khi F2 nói "số màn hình mỗi use case thường 1-5; trên 6 thường là tách vụn". Tôi coi là hai boundary riêng (3 và 4 màn hình) và ghi ở Vấn đề còn mở; prompt không nói mức hợp lý tính theo use case hay theo boundary.

20. Quá tải ngữ cảnh: các file đầu vào lớn (P07 từ 44 đến 73 KB, P08, P09, P10 từ 63 đến 70 KB). Bảng "Phần cần dùng" yêu cầu lọc dòng message của tác nhân người và boundary giao diện người dùng trong bốn file P07; tôi dùng P08 F3 (trách nhiệm boundary) làm nguồn chính và chỉ tra thêm bảng message của P07 UC-005, UC-010 để lấy thứ tự và các luồng từ chối. 77 quy định có tham chiếu chéo nhau theo STT nên phải dùng script đánh số tự động để các tham chiếu "UI-STT n" không lệch; làm tay dễ sai khi chèn quy định.

21. THONG_TIN_TAI_LIEU và MAU_DAC_TA_MAN_HINH chỉ dùng ở F5 (đặc tả màn hình, giai đoạn 2). Giai đoạn 1 không có chỗ ghi nên chỉ ghi lại trong hàng Đầu vào đã dùng; XUAT_HTML là Không nên không có mockup.

Không có vướng mắc nào khác. Các mục 2 (ánh xạ boundary), 5 (cạnh), 11 (khớp bảng và .drawio) đã đạt theo kiểm tra tự động.
