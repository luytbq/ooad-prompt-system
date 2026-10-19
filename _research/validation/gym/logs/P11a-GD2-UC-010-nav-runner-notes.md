Model của phiên chạy: Sonnet

# Nhật ký người chạy - P11a giai đoạn 2 (UC-010 và màn hình điều hướng, lần giai đoạn 2 cuối cùng)

Tham số: CHE_DO_CHAY = "Giai đoạn 2: các màn hình của UC-010 và các màn hình điều hướng (lần giai đoạn 2 cuối cùng)"; XUAT_HTML = Có; MAU_DAC_TA_MAN_HINH = Không có; MUC_CHI_TIET của hồ sơ = GON; CHE_DO_GIA_DINH = NGHIEM_NGAT.

Đầu ra đã ghi trong gym/design/P11a-gui/: SCR-06, SCR-07, SCR-08 (UC-010); SCR-01, SCR-02, SCR-09, SCR-10, SCR-15, SCR-16 (điều hướng); mockups/ chín file HTML tương ứng; screen-list.md (1.0 --> 1.1, thêm bảng tổng hợp F7 ở mục 3); ui-standards.md (1.0 --> 1.1, chỉ đổi khối thông tin). Không có file .drawio mới (giai đoạn 2 không có sơ đồ); file diagrams/P11a-screen-transition.drawio của giai đoạn 1 vẫn là XML hợp lệ (đã kiểm tra bằng minidom). Q lớn nhất sau lần chạy: Q-105 (mới, ở SCR-06). ASM: chưa cấp.

Kết quả tự kiểm tra Target: Target 1 đến 12 đạt. Không có mục Target nào không đạt. Điểm cần lưu ý: Target 9 còn 24 dòng Vi phạm còn mở trong bảng tổng hợp (chín dòng thuộc lần chạy này: SCR-06 có 3, sáu màn hình điều hướng mỗi màn hình 1), không có vi phạm WCAG AA chưa xử lý. Target 11: không có sơ đồ mới; mockup đã kiểm tra tốt về cấu trúc thẻ HTML (không thẻ mở thiếu, không script, không tài nguyên ngoài), chưa mở được trên trình duyệt thật.

## 0. Trung thực về phạm vi đọc (lỗi của người chạy, không phải của prompt)

- Yêu cầu giao việc chỉ cho đọc mục h) của các SCR đã có. Tôi đã đọc toàn bộ SCR-03 và SCR-05, và các mục b) đến g) của SCR-11 để lấy mẫu trình bày. Khi lấy mục h) bằng lệnh cắt từ h) trở xuống, tôi cũng đọc luôn mục Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở của bảy SCR đã có. Hệ quả: cách đặt mục c) đến g), câu chữ hàng "Tiêu chí không có dòng ở bảng này...", cách ghi "Cùng đề xuất đã ghi ở SCR-03" và các dữ liệu mẫu (26/10/2026 18:00, Yoga, Phòng 2, Nguyễn Thị Lan lấy từ P04 nhưng cách ghi nguồn lấy theo mẫu cũ) chịu ảnh hưởng của lần chạy trước. Kết quả vì vậy không hoàn toàn phản ánh riêng chất lượng prompt. Bản thân prompt không có ví dụ SCR hoàn chỉnh nên tôi cần một mẫu; xem mục 12.
- Tôi đã chạy một lệnh kiểm tra trạng thái kho mã (chỉ đọc) dù yêu cầu là không chạy git. Không có thay đổi nào do lệnh này gây ra.
- Phần P07 của UC-010 tôi đọc rộng hơn mức cần (F3 đến F5, không chỉ dòng message của tác nhân người và boundary giao diện người dùng). P04 UC-010 đọc toàn file kể cả phần activity diagram.

## 1. Gom mục h) khi không có dòng nào để nối

- Vị trí: mục 3, "Lần chạy giai đoạn 2 cuối cùng phải gồm mọi màn hình điều hướng chưa có đặc tả, rồi mới gom mục h) của mọi SCR vào cuối danh mục ở ui-standards.md (chỉ nối thêm dòng, không sửa dòng cũ, không cần chạy lại giai đoạn 2). Lần chạy nối dòng vào ui-standards.md, screen-list.md tăng phiên bản phụ của file đó (1.0 --> 1.1), ghi hàng Bước ..., thêm các SCR đã gom vào hàng Đầu vào đã dùng và cập nhật hàng Mã Q, ASM cuối đã cấp; không sửa nội dung khác của file."
- Gặp: cả 16 SCR đều ghi mục h) là "Không có" (không SCR nào cần thông điệp mới ngoài MSG-01 đến MSG-15), nên không có dòng nào để nối. Câu trên không nói rõ khi không có dòng nối thì có tăng phiên bản không. Câu cũng gộp ui-standards.md và screen-list.md vào một mệnh đề, không rõ screen-list.md tăng phiên bản vì lý do gì (nó không nhận dòng MSG, nó nhận bảng tổng hợp F7).
- Xử lý: vẫn tăng cả hai file lên 1.1, ghi hàng Bước "P11a (giai đoạn 1; nối từ giai đoạn 2)", thêm câu ghi nhận đã gom vào hàng Đầu vào đã dùng (ghi rõ ui-standards.md không có dòng nối), cập nhật hàng Mã Q, ASM thành Q-105. Đây là suy luận của tôi; nếu prompt định ý "không có dòng nối thì không đụng file" thì ui-standards.md đáng lẽ giữ nguyên.

## 2. "Không sửa nội dung khác của file" mâu thuẫn với việc cần cập nhật nội dung

- Vị trí: cùng câu trên, "không sửa nội dung khác của file", và F7 "Lần chạy giai đoạn 2 cuối cùng, hoặc chế độ Toàn bộ, lập bảng tổng hợp ở cuối screen-list.md từ mục g của các SCR".
- Gặp: screen-list.md mục 3 đang ghi "Chưa có. Bảng này lập từ mục g)...", phải thay bằng bảng nên là sửa nội dung. Mục "Vấn đề còn mở" của screen-list.md có dòng "Giai đoạn 2 còn lại: viết đặc tả 10 màn hình nghiệp vụ và 6 màn hình điều hướng, rồi lập bảng tổng hợp F7 ở mục 3 và gom mục h)", nay đã sai. Tương tự ui-standards.md có dòng "Giai đoạn 2: gom mục h)... tăng phiên bản phụ (1.0 --> 1.1)" nay đã thành sự thật.
- Xử lý: thay đoạn "Chưa có" bằng bảng tổng hợp (vì F7 buộc). Giữ nguyên hai dòng Vấn đề còn mở đã lỗi thời để tuân "không sửa nội dung khác", nên hiện hai file chứa câu không còn đúng. Đề nghị prompt nói rõ ngoại lệ được sửa cho phần chỗ giữ chỗ và mục Vấn đề còn mở.

## 3. Đề xuất sửa ui-standards.md (UI-STT 33) không có đường áp dụng

- Vị trí: mục 3 (cùng câu trên) và YEU_CAU_BO_SUNG "các đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a, P11b) thì các bước đó không chạy lại"; F7 "Dòng 'Vi phạm đã sửa' chỉ ghi khi áp nguyên quy định của ui-standards.md ... và màn hình đã làm khác để đạt tiêu chí".
- Gặp: UI-STT 33 (trên 5 giá trị dùng danh sách chọn) xung đột với lịch lớp nhóm ở SCR-06, cùng dạng với SCR-03 và SCR-11. SCR-03 đã hứa "cập nhật khi nối dòng ở lần chạy giai đoạn 2 cuối cùng", nhưng prompt chỉ cho phép nối dòng vào danh mục MSG, không cho sửa hay thêm quy định UI-STT. F1 cho phép thêm quy định mới nhận STT tiếp theo nhưng đó là phần của giai đoạn 1.
- Xử lý: không sửa ui-standards.md; SCR-06 ghi "Vi phạm đã sửa" ở Nielsen 6 và thêm một dòng Đề xuất sửa artifact trước mở rộng ngoại lệ của UI-STT 33, trạng thái chưa áp dụng. Kết quả: cả ba màn hình dùng thẻ hoặc bảng chọn đều trái chữ UI-STT 33 mà tiêu chuẩn chưa ghi ngoại lệ. Đây là lỗ hổng hệ thống: không có bước nào trong pipeline áp dụng đề xuất sửa giai đoạn 1 khi giai đoạn 1 không chạy lại.

## 4. Lối vào chưa có màn hình đích: hành vi, phản hồi và Vi phạm còn mở không có Q

- Vị trí: mục 3 "lối vào use case chưa có màn hình đích ghi 'Chưa có màn hình đích (UC-nnn)' ở chức năng của điều khiển"; A2 "Lối vào use case chưa có màn hình đích ghi ở Ghi chú của node, không tính là lối ra"; F7 Lưu ý "ghi Q-nn hoặc đề xuất sửa P04, không tự thêm".
- Gặp: prompt chỉ nói ghi chữ gì ở cột Chức năng, không nói điều khiển trông thế nào và phản hồi ra sao khi nhấn. SCR-11 lần trước đã dùng cách "ở lại màn hình, không phản hồi". Nhấn mà không có phản hồi là vi phạm Nielsen 1 nhưng nguyên nhân là phạm vi dự án chỉ có đặc tả 4 use case (YEU_CAU_BO_SUNG), không phải chỗ đặc tả thiếu, nên Q-nn không phù hợp và đề xuất sửa P04 cũng không phù hợp.
- Xử lý: hiển thị đầy đủ như lối vào có đích, ghi "Chưa có màn hình đích (UC-nnn); ở lại SCR-nn", và ghi dòng Nielsen 1 "Vi phạm còn mở" ở sáu màn hình điều hướng với cách xử lý "hết khi use case có đặc tả và màn hình", không có mã Q. Bảng tổng hợp ghi rõ đây là ngoại lệ không có Q. Đề nghị prompt nêu rõ loại "Vi phạm còn mở do phạm vi" và cách ghi.

## 5. Nút quay lại của hệ thống ở màn hình điều hướng

- Vị trí: F1 nhóm Screen không yêu cầu hành vi quay lại cho màn hình gốc; UI-STT 15 (giai đoạn 1) "ở màn hình khác thì đưa về màn hình điều hướng" chưa nói chính màn hình điều hướng.
- Gặp: bảng điều khiển bắt buộc có dòng cho điều khiển, nhưng không có quy định cho nút quay lại hệ thống ở màn hình điều hướng di động.
- Xử lý: ghi dòng "không mở màn hình nào của phần mềm; Android đưa ứng dụng xuống nền, iOS không có cử chỉ quay lại ở màn hình gốc" với căn cứ Material Design và Apple HIG, kèm đánh giá HIG Đạt. Đây là quyết định trình bày của người chạy, không có trong ui-standards.md.

## 6. Thông điệp của use case trên màn hình điều hướng

- Vị trí: A2 "Thông điệp của use case hiển thị trên màn hình điều hướng (kết thúc, huỷ use case rồi quay về) được tham chiếu ở bảng điều khiển của màn hình điều hướng (thao tác Khởi tạo, nguồn là bước UC)".
- Gặp: với UC-005 và UC-010 mọi kết cục đều hiển thị ở màn hình kết quả hoặc ở SCR-06, người dùng về màn hình điều hướng bằng nút Trang chủ và không có thông điệp. Với các use case chưa có đặc tả (SCR-01, 09, 15, 16) không thể biết có thông điệp hay không.
- Xử lý: thêm một dòng cuối trong bảng điều khiển mỗi màn hình điều hướng ghi "Không có thông điệp của use case hiển thị khi mở màn hình" kèm lý do và bước UC nguồn. Prompt không nói nên có dòng "Không có" khi không có thông điệp hay bỏ dòng.

## 7. Kiểu và số ký tự cho trường ngày giờ và trường số hiển thị

- Vị trí: F5 e) "Kiểu (Type: Chữ, Số, Ngày, Giờ, Tiền, Lựa chọn, Logic)" và "trường Ngày, Giờ, Tiền ghi độ dài của định dạng hiển thị (ví dụ dd/MM/yyyy là 10)".
- Gặp: Giờ học là một trường gồm cả ngày lẫn giờ (dd/MM/yyyy HH:mm), danh sách kiểu không có kiểu ngày giờ. Vị trí trong danh sách chờ là Số hiển thị: không rõ ghi "-" hay độ dài định dạng.
- Xử lý: ghi kiểu "Ngày, Giờ" với 16 ký tự kèm "Thiết kế: độ dài định dạng hiển thị"; Vị trí ghi "-" theo quy tắc trường Hiển thị có độ dài theo giá trị. Đề nghị prompt thêm kiểu Ngày giờ.

## 8. Trường chọn khi P04 ghi Dữ liệu vào là Không có

- Vị trí: F5 e) "Ràng buộc dữ liệu lấy từ cột 'Điều kiện hợp lệ' của bảng dữ liệu vào ra P04 và BR", cột Nguồn "(P04 dữ liệu vào ra STT, BR, GL)".
- Gặp: P04 UC-010 ghi "Dữ liệu vào: Không có. Ở bước 3 hội viên chỉ chọn một lớp", nhưng màn hình SCR-06 có điều khiển chọn lớp và phải kiểm tra bắt buộc. Tính bắt buộc chỉ có ở P07 (selectClass) và nguồn của MSG-01.
- Xử lý: tạo dòng "Lớp nhóm đã chọn" với nguồn P07 selectClass và nêu rõ trong Vấn đề còn mở là cần người dùng xác nhận; không tạo Q mới vì chỗ này là chọn từ danh sách, không phải giá trị nghiệp vụ mới. Prompt không nêu nguồn nào được dùng khi P04 và P07 lệch nhau.

## 9. MUC_CHI_TIET là GON nhưng F7 chỉ nêu DAY_DU

- Vị trí: F7 "Khi MUC_CHI_TIET là DAY_DU, thêm một dòng 'Các tiêu chí còn lại: Đạt theo ui-standards.md STT ...' thay cho từng dòng."
- Gặp: hồ sơ ghi GON; prompt không nói cách xử lý ở GON ngoài quy tắc chung "chỉ ghi dòng ...".
- Xử lý: ở GON chỉ ghi các dòng có bằng chứng riêng và thêm câu cuối bảng "Tiêu chí không có dòng ở bảng này ... đạt theo ui-standards.md mục 3" (câu này lấy từ lần chạy trước, không có trong prompt).

## 10. XUAT_HTML = Có chỉ ở lần chạy cuối

- Vị trí: A4 "Nếu XUAT_HTML là "Có", sinh một file HTML tĩnh cho mỗi màn hình theo F6" và F6 "Mỗi màn hình một file".
- Gặp: bảy SCR của lần chạy UC-005 được viết khi XUAT_HTML là Không, nên chưa có mockup. Prompt viết "mỗi màn hình trong phạm vi" nên chỉ có chín mockup và 7 trong 16 màn hình không có mockup.
- Xử lý: chỉ sinh mockup cho chín màn hình trong phạm vi lần này, không làm bù. Nếu người dùng muốn đủ 16 mockup thì cần chạy bổ sung SCR-03, 04, 05, 11, 12, 13, 14. Prompt không nói tham số XUAT_HTML có áp dụng hồi tố hay không.

## 11. Mockup HTML: không kiểm tra được hiển thị thật, logo, nhiều trạng thái

- Vị trí: F6 "tương phản đạt WCAG AA"; "Ảnh minh hoạ dùng khối placeholder có văn bản thay thế"; F4 "Khung dây dạng văn bản".
- Gặp: môi trường không có trình duyệt nên chỉ kiểm tra được cú pháp thẻ và tính tương phản bằng công thức. Không có tệp logo (ui-standards ghi tệp do tổ chức cấp) nên dùng khối placeholder có aria-label VietFit. SCR-06 có ba trạng thái (đã chọn, lỗi, hộp xác nhận) nhưng F6 yêu cầu một file cho mỗi màn hình; tôi để ba khung trong một file, nên một trang có nhiều thẻ h1, trái với UI-STT 13 (tiêu đề cấp 1 duy nhất) nếu coi file là một trang thật.
- Xử lý: chấp nhận ba khung trong một file và đánh dấu bằng nhãn trạng thái. Cặp màu mới (nền #E8F5EC) được tính ở SCR-07 và dùng lại ở SCR-08. Không có cặp màu nào dưới ngưỡng.

## 12. Prompt thiếu ví dụ SCR hoàn chỉnh

- Vị trí: F5 (không có ví dụ đầy đủ một file SCR; chỉ có ví dụ từng dòng ở d) và e)).
- Gặp: không rõ thứ tự mục, cách đặt "Mockup HTML:" ở mục c), cách ghi hàng đầu vào của khối thông tin (hàng "Đầu vào đã dùng" rất dài), cách ghi Q "đã cấp ở bước trước". Tôi bám cấu trúc a) đến h) cộng bốn mục cuối của C5 và theo mẫu SCR đã có (xem mục 0).
- Xử lý: như trên. Đề nghị thêm một ví dụ khung file SCR.

## 13. Đề xuất sửa P10 cho màn hình điều hướng lặp lại

- Vị trí: A2 "Màn hình điều hướng ... có một dòng Đề xuất sửa P10 thêm phần tử View điều hướng vào package giao diện của tác nhân."
- Gặp: dòng này đã có ở screen-list.md từ giai đoạn 1; prompt không nói giai đoạn 2 có lặp lại ở từng SCR hay không.
- Xử lý: lặp lại một dòng ở mục Đề xuất sửa artifact trước của từng SCR điều hướng, ghi "đề xuất đã ghi ở screen-list.md; chỉ đổi cấu trúc nên P10 không chạy lại". Có thể thừa.

## 14. Cấp Q-105

- Vị trí: A1 "Trước khi cấp Q mới, tìm câu hỏi cùng nội dung trong mục Câu hỏi mở của artifact đầu vào"; C1 mục 2 NGHIEM_NGAT.
- Gặp: P04 UC-010 bước 2 không nêu trường hợp lịch không có lớp nào. Q-83 hỏi phạm vi của lịch, gần nhưng không cùng nội dung; Q-103 là trường hợp không có giá gói của UC-005.
- Xử lý: cấp Q-105 ở SCR-06 (hỏi trường hợp lịch rỗng) và gắn Nielsen 1 Vi phạm còn mở; đây là phán đoán, có thể gộp vào Q-83. Mã Q lớn nhất tìm được trước khi chạy đúng Q-104.

## 15. Dữ liệu mẫu và BR-06, BR-07 mâu thuẫn

- Vị trí: A4 "ngày giờ hợp lệ và nhất quán giữa các màn hình"; Target 8.
- Gặp: BR-06 (sớm nhất 7 ngày trước giờ học) và BR-07 (tuần mới mở lúc 6 giờ sáng thứ Hai) mâu thuẫn nhau (Q-11) nên không thể chứng minh một lớp mẫu nào đặt được vào thời điểm cho trước. Mockup cũng không có ngày hiện tại.
- Xử lý: chọn các lớp ngày 26 và 27/10/2026 (thứ Hai và thứ Ba, trong 7 ngày kể từ 20/10/2026) theo ví dụ P04, ghi rõ trong Vấn đề còn mở của SCR-06 rằng tính hợp lệ chưa khẳng định được. Không thể thỏa đồng thời "dữ liệu đúng nghiệp vụ" và "không chọn bên nào của BR-06, BR-07".

## 16. Điểm khác

- Quá tải ngữ cảnh: không. ui-standards.md (51 KB) cần hai lần đọc vì giới hạn kích thước.
- Thứ tự thẻ lịch theo giờ học tăng dần và việc giữ hay bỏ thẻ đã chọn sau từng hộp lỗi (giữ sau MSG-05, MSG-07, MSG-08 và hộp lỗi hệ thống; bỏ sau MSG-06 vì lịch được tải lại) là quyết định trình bày của người chạy dựa trên UI-STT 62, nguồn không quy định; đã ghi trong bảng điều khiển và Vấn đề còn mở của SCR-06.
- Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu ngày, theo F5 a).
- Có phát hiện không nằm trong Target: sau khi gom, cả ba màn hình chọn một trong nhiều mục (SCR-03, SCR-06, SCR-11) đều dựa vào cùng ngoại lệ chưa được ghi vào ui-standards.md (xem mục 3).
