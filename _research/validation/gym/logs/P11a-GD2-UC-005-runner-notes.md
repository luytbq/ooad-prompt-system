Model của phiên chạy: Sonnet

# Nhật ký người chạy - P11a giai đoạn 2, màn hình của UC-005 (lần chạy giai đoạn 2 đầu tiên)

## Kết quả chạy

- Ghi 7 file: SCR-03, SCR-04, SCR-05 (ứng dụng di động, ACT-02), SCR-11, SCR-12, SCR-13, SCR-14 (ứng dụng web, ACT-05) trong gym/design/P11a-gui/. Không ghi mockup HTML (XUAT_HTML là Không). Không có file .drawio mới ở giai đoạn 2 (không sửa sơ đồ dịch chuyển).
- Cấp Q-103 (màn hình khi không có giá gói, ghi ở SCR-03) và Q-104 (cách xác định người mua tại quầy, ghi ở SCR-11). Q lớn nhất sau lần chạy: Q-104. ASM: chưa cấp (NGHIEM_NGAT).
- Không tạo mục h) mới: không có MSG mới; các lỗi bắt buộc dùng MSG-01 theo mẫu có tham số.
- Không sửa ui-standards.md, screen-list.md, screen-transition.md vì chưa phải lần giai đoạn 2 cuối cùng.
- Kiểm tra tự động đã làm: số cột bảng Markdown khớp tiêu đề, không có em dash, không có mũi tên Unicode, không có inline code, mọi mã MSG, TR, Q, BR được trích đều tồn tại, tỉ lệ tương phản của cặp màu mới đo bằng công thức WCAG.
- Mục Target: Target 1, 2, 5, 11 là của giai đoạn 1 hoặc không đổi ở lần chạy này. Target 3 và 7 đạt một phần (xem mục 11 và mục 12 bên dưới). Các mục còn lại đạt; các dòng Vi phạm còn mở đều do đặc tả chưa quy định và đã gắn mã Q, không có vi phạm WCAG AA chưa xử lý.

## Vướng mắc

1. Vị trí: mục 3, bảng "Phần cần dùng", so với mục 2 "Đầu vào". Câu trích: "P01-actors.md, P02-usecases.md | Có | Tác nhân người và use case của từng tác nhân (màn hình điều hướng)". Gặp: bảng "Phần cần dùng" không có dòng cho P01 và P02 dù mục 2 liệt kê hai file này là đầu vào bắt buộc. Xử lý: chỉ đọc bảng 4a của P02 (để lấy tên UC-007, UC-017 cho mục menu của lễ tân) và Mục 2 của P01 (đối chiếu ACT-02, ACT-05). Không rõ phần nào là "phần cần dùng" nên đoán theo mục đích.

2. Vị trí: A1, "Trước khi cấp Q mới, tìm câu hỏi cùng nội dung trong mục Câu hỏi mở của artifact đầu vào (P09, P10, P11b nếu đã có)". Gặp: P11b không có trong bảng "Phần cần dùng" và không có trong danh sách đọc của lần chạy này, nhưng câu này bắt buộc dò P11b. Câu này nằm ở A1 (giai đoạn 1) còn giai đoạn 2 không nhắc lại. Xử lý: chỉ dò các dòng Q-100 đến Q-102 của P11b để chống trùng và quét mã lớn nhất; không có câu nào trùng nội dung. Không rõ giai đoạn 2 có phải dò lại P09, P10, P11b khi cấp Q hay không; tôi coi có.

3. Vị trí: F5 a), "thêm các hàng Ngày tạo, Người duyệt, Người kiểm tra, Người phụ trách vào bảng thông tin C5, giá trị theo THONG_TIN_TAI_LIEU". Gặp: THONG_TIN_TAI_LIEU của đề không có Ngày tạo. Xử lý: giữ hàng Ngày tạo với ô trống (theo hướng dẫn placeholder "ô tương ứng để trống"). Không rõ nên giữ hàng trống hay bỏ hàng.

4. Vị trí: F7, "Khi MUC_CHI_TIET là DAY_DU, thêm một dòng 'Các tiêu chí còn lại: Đạt theo ui-standards.md STT ...' thay cho từng dòng", cùng Target 9 "mọi màn hình trong phạm vi được đánh giá theo F7". Gặp: hồ sơ dự án đặt MUC_CHI_TIET là GON, prompt không nói gì cho GON. Bảng F7 mỗi SCR chỉ có dòng có bằng chứng riêng nên không có chỗ nào chứng minh các tiêu chí còn lại đã được đánh giá. Xử lý: thêm một câu dưới bảng "Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3". Đây là việc tự thêm; nên có hướng dẫn rõ cho GON.

5. Vị trí: F5 d), danh mục Thao tác: "Hết thời gian (sự kiện thời gian trên màn hình)" và "Nhận kết quả (kết quả bất đồng bộ từ hệ thống)". Gặp: hạn 15 phút của đơn mua (BR-04) do máy chủ đếm (P09: control không giữ trạng thái chờ, mốc hẹn bền ở máy chủ), màn hình không có bộ đếm. Xử lý: dùng Nhận kết quả cho cả ba kết cục ở SCR-04 (thành công, không thành công, đơn bị huỷ quá hạn) và không dùng Hết thời gian. Danh mục thao tác không phân biệt thời gian phía máy khách và phía máy chủ.

6. Vị trí: F5 d), "mỗi nút có dòng 'Nhấn'", và F3 "Hành vi khi rời màn hình đang giữ tài nguyên qua menu ghi ở đặc tả màn hình đó". Gặp: các điều khiển chuẩn (Trang chủ, menu trái, nút quay lại của hệ thống) và nút của hộp thông điệp (MSG-02, MSG-03, MSG-11) không thuộc đặc tả UC nhưng vẫn là nút. Menu web lặp lại nguyên văn ở bốn SCR web (khoảng 4 dòng mỗi SCR). Xử lý: đưa các điều khiển này thành dòng, nguồn ghi UI-STT; hành vi rời qua menu ở SCR-13 (đơn đã tạo, không có huỷ, Q-57, Q-25) và Trang chủ ở SCR-04 (khi MSG-04 hiển thị, Q-96) ghi tại dòng đó. Prompt không nói menu có phải là dòng của bảng điều khiển hay chỉ tham chiếu một lần.

7. Vị trí: F5 e), "Trường do tác nhân nhập: độ dài tối đa và miền giá trị mà nguồn không nêu là giá trị nghiệp vụ, ghi Q-nn". Gặp: P04 UC-005 có ba Dữ liệu vào mà cột Bắt buộc và Điều kiện hợp lệ là "Chưa quy định" (Chi nhánh áp dụng Q-50, Gói đang có cần gia hạn Q-56, Người mua gói Q-01). Prompt không nói có phải vẽ điều khiển cho trường chưa xác định kiểu hay không. Xử lý: Chi nhánh áp dụng chỉ hiển thị (Dữ liệu ra 1 STT 3); Gói đang có cần gia hạn có dòng ở mục e) nhưng không có điều khiển trên hình ảnh; Người mua gói có ô nhập ở SCR-11 vì UC cần người mua để tạo đơn (GL-09, P07 createOrder). Hệ quả: màn hình chưa phân biệt được mua mới và gia hạn (Q-56).

8. Vị trí: UI-STT 31 (phase 1) "Quy tắc bắt buộc lấy từ cột Bắt buộc của bảng Dữ liệu vào ở P04", so với F5 e). Gặp: với Người mua gói, cột Bắt buộc ghi "Chưa quy định (Q-01)" nên quy tắc này không dùng được. Xử lý: đặt bắt buộc dựa trên GL-09 và P07, ghi rõ căn cứ ở cột Ghi chú và ở Vấn đề còn mở để người dùng xác nhận. Đây là một suy luận, có thể bị coi là giả định trong chế độ NGHIEM_NGAT; prompt không nói trường hợp này.

9. Vị trí: F5 e), "trường Ngày, Giờ, Tiền ghi độ dài của định dạng hiển thị (ví dụ dd/MM/yyyy là 10)". Gặp: định dạng tiền có độ dài thay đổi theo giá trị (1.080.000 đ, 250.000 đ) và đặc tả không nêu giá trị tối đa của giá gói. Xử lý: ghi 13 kèm "Thiết kế: độ rộng vùng hiển thị tiền (999.999.999 đ), không phải miền giá trị". Quy tắc này mơ hồ với kiểu Tiền và dễ lẫn giữa độ rộng hiển thị với miền giá trị nghiệp vụ.

10. Vị trí: A4, "số liệu tổng hợp phải khớp (tổng tiền bằng tổng các dòng cộng phí theo BR)". Gặp: P04 UC-005 Dữ liệu ra 2 chỉ có Gói tập, Ngày bắt đầu, Số tiền phải trả, không có mức giảm khuyến mãi; ví dụ P04 lại là 1.200.000 đ (giá) và 1.080.000 đ (số tiền phải trả). Màn hình không có dòng để chứng minh tổng khớp. Xử lý: dùng đúng hai giá trị ví dụ, ghi ở Dữ liệu mẫu rằng chênh lệch là khuyến mãi 10% (BR-38 tối đa 20%); ghi Vi phạm còn mở Nielsen 1 ở SCR-04 và SCR-12 gắn Q-09 và đề xuất sửa P04 Dữ liệu ra 2. Quy tắc A4 và quy tắc "không thêm trường ngoài đặc tả" (A4) xung đột ở điểm này.

11. Vị trí: Target 3, "Không có trường, nút, chức năng nào không truy được về đặc tả, bảng dữ liệu vào ra, BR hoặc trách nhiệm boundary", so với UI-STT 76 và F7. Gặp: SCR-12 hiển thị lại Người mua gói (Dữ liệu vào 1 STT 5, không thuộc Dữ liệu ra 2, theo UI-STT 76); SCR-13 có nhóm Hình thức thu (điều kiện chọn luồng 8a hoặc 8b, không là Dữ liệu vào của P04, chỉ có paymentMethod ở P07). Xử lý: giữ và ghi nguồn gián tiếp, ghi Đề xuất sửa P04 (bổ sung Hình thức thu vào Dữ liệu vào, chờ Q-98) và ghi ở Vấn đề còn mở. Target 3 đạt một phần vì truy vết là gián tiếp.

12. Vị trí: F5 e) và Target 7. Gặp: độ dài Mã giao dịch POS và Người mua gói không nguồn nào nêu. Xử lý: ghi "Chưa quy định (Q-55)" và "Chưa quy định (Q-104)" thay cho một con số. Target 7 yêu cầu "không có độ dài ... tự đặt mà không có mã Q" nên đạt, nhưng cột Số ký tự tối đa không có giá trị cụ thể nên P13 chưa dùng lại được; prompt không nói cột này được phép ghi "Chưa quy định (Q-nn)".

13. Vị trí: ui-standards.md (phase 1) UI-STT 33, "Tập giá trị loại trừ lẫn nhau có từ 2 đến 5 giá trị (thời hạn gói 1, 3, 6, 12 tháng; loại gói) hiển thị dạng nút chọn (radio)", so với Dữ liệu ra 1 (giá cho từng gói). Gặp: áp nguyên thì thành hai nhóm nút chọn riêng và không hiển thị được giá của từng tổ hợp; có tối đa 8 tổ hợp. Xử lý: dùng một nhóm thẻ (di động) hoặc bảng có nút chọn (web) theo UI-STT 34, ghi dòng Nielsen 6 "Vi phạm đã sửa" ở SCR-03 và SCR-11 theo định nghĩa ở A6, và ghi Đề xuất sửa UI-STT 33. Chưa rõ sau lần chạy này, vì prompt chỉ cho phép "chỉ nối thêm dòng" vào ui-standards.md ở lần cuối và chỉ cho mục h), nên quy định ngoại lệ có thể không bao giờ được thêm vào ui-standards.md.

14. Vị trí: ui-standards.md (phase 1), các quy định mâu thuẫn nhẹ gặp khi áp dụng. UI-STT 29 "tối đa 4 từ" so với UI-STT 75 "Xác nhận đã thu 1.080.000 đ" (coi số tiền là một thành phần); UI-STT 41 trích BR-11 (BR-11 là sức chứa lớp nhóm) cho việc chống gửi hai lần; UI-STT 76 đòi tóm tắt có chi nhánh áp dụng và người mua trong khi Dữ liệu ra 2 không có; UI-STT 51 nói Esc hoặc quay lại hệ thống đóng hộp thông điệp nhưng MSG-04 không có nút; UI-STT 41 (nút chính thành Đang xử lý) và UI-STT 56 (chỉ báo xoay MSG-10) cùng quy định chỉ báo bận; UI-STT 20 ghi Toàn chuỗi viết hoa còn ví dụ P04 là "toàn chuỗi". Xử lý: chọn một cách, ghi tại chỗ (xem Ghi chú ở d) của SCR-04, SCR-13); không sửa ui-standards.md. Đây là lỗi của giai đoạn 1 nhưng prompt giai đoạn 2 không có cơ chế báo lỗi chuẩn ngoài Đề xuất sửa artifact trước.

15. Vị trí: UI-STT 38 (phase 1) "Kiểm tra từng trường ngay khi rời trường", so với nhóm nút chọn. Gặp: nhóm nút chọn, nhóm thẻ, bảng chọn một dòng không có sự kiện rời trường có nghĩa (người dùng Tab qua mà chưa thao tác thì báo lỗi là không hợp lý). Xử lý: kiểm tra lúc nhấn nút chính, ghi rõ ở mục f). Không có quy định chuẩn cho trường hợp này; F5 f) chỉ nói "Thời điểm kiểm tra" mà không hướng dẫn cho điều khiển loại chọn.

16. Vị trí: F4, "Khung dây dạng văn bản trong khối code" và F5 c). Gặp: màn hình có nhiều trạng thái (SCR-04 có hộp chờ MSG-04; SCR-13 có hai hình thức thu; SCR-03, SCR-11 có trạng thái lỗi) nhưng F4 chỉ mô tả một khung. Xử lý: thêm khung thứ hai cho trạng thái quan trọng; không có hướng dẫn số khung tối đa. Khung web rộng 118 ký tự để thể hiện cả menu, không đại diện đúng tỉ lệ 1366 px.

17. Vị trí: F2, "Lớp thiết kế: DC tương ứng trong P10 nếu có" và F5 b) "DC". Gặp: P10 tách mỗi boundary thành View, Store, Controller (PKG-05, PKG-10); cột chỉ có một chỗ. Xử lý: ghi View và ghi "đi cùng Store" (theo cách của screen-list.md). Controller (REST) bị bỏ vì là phía máy chủ.

18. Vị trí: 00-Conventions.md C3, "Mã lớn nhất tìm trong mục Câu hỏi mở và Giả định của mọi artifact đã có trong THU_MUC_DAU_RA" và mục 3 của prompt "Chạy tuần tự các lần giai đoạn 2". Gặp: mỗi file SCR ghi "Mã Q, ASM cuối đã cấp" là mã lớn nhất toàn dự án sau lần chạy; trong một lần chạy nhiều SCR, mã cuối (Q-104) đứng trong cả SCR-03 chỉ định nghĩa Q-103. Xử lý: ghi Q-104 ở cả bảy file. Chưa rõ nên ghi mã cuối của lần chạy hay mã cuối tại thời điểm file được viết. Lần giai đoạn 2 kế tiếp phải quét Câu hỏi mở của các SCR (không phải artifact đầu vào đã liệt kê ở mục 3); mục 3 không nhắc phải đọc Câu hỏi mở của các SCR trước.

19. Vị trí: mục 3, "Phần cần dùng" của P07. Câu trích: "Dòng bảng message có Từ hoặc Đến là tác nhân người hoặc boundary giao diện người dùng". Gặp: file P07 của UC-005 dài 525 dòng, bảng message nằm ở bốn sơ đồ SD1a, SD1b, SD1c, SD2, và công cụ đọc cắt ở giới hạn nên phải đọc nhiều lần. Phần lớn thông tin cần (tên trách nhiệm, thứ tự) cũng có ở F4 và F3.4 của chính file đó. Quá tải ngữ cảnh mức vừa: tổng đầu vào đọc khoảng 250 KB cho 7 màn hình.

20. Vị trí: mục 3, "Phạm vi 'các màn hình của UC-nnn' gồm màn hình có cột UC của screen-list.md chứa UC-nnn, trừ màn hình điều hướng". Gặp: SCR-02 và SCR-10 có UC-005 trong cột UC nhưng là màn hình điều hướng; đã loại đúng. Nhưng lối vào UC-005 trên SCR-02, SCR-10 chưa có đặc tả nên mục "Đến từ" của SCR-03 và SCR-11 tham chiếu các màn hình chưa có file. Chấp nhận được; ghi để người dùng biết.

## Mục Target không đạt hoặc đạt một phần

- Target 3: đạt một phần do mục 11 (Người mua gói ở SCR-12, Hình thức thu ở SCR-13).
- Target 7: đạt một phần do mục 12 (độ dài chưa có giá trị cụ thể cho Mã giao dịch POS và Người mua gói).
- Target 9: không còn vi phạm WCAG AA chưa xử lý; có các dòng Vi phạm còn mở của Nielsen gắn Q-103, Q-56, Q-104, Q-57, Q-96, Q-13, Q-09, Q-55, Q-54, đều do đặc tả.
- Target 8: dữ liệu mẫu nhất quán giữa các màn hình (1.200.000 đ, 1.080.000 đ, 01/12/2026, 6 tháng Toàn chuỗi, Nguyễn Văn An, 004217) nhưng chênh lệch giá và số tiền phải trả không giải thích được trên màn hình (mục 10).
