Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy P01 - bus-r2

Đầu ra: bus-r2/design/P01-actors.md (9 ACT, 3 SH ở Mục 3, 19 dòng ứng viên bị loại, Q-38 và Q-39, ASM-10 và ASM-11). Mã Q, ASM lớn nhất trước khi chạy: Q-37, ASM-09 (đọc từ P00). Sau khi chạy: Q-39, ASM-11.

Tự kiểm tra Target: 11 mục đều Đạt. Không có file .drawio ở bước này.

## Vướng mắc

1. Số tác nhân thời gian: một hay hai.
   - Vị trí: Format, cột Loại, "Thời gian": tên "Bộ định thời" hoặc "tên nêu chu kỳ khi có nhiều nhịp độc lập"; Bước 3 A-T5 "Phân biệt được: tập mục tiêu ... khác với mọi tác nhân còn lại".
   - Gặp: đề có hai mốc thời gian không người khởi xướng, cùng neo vào giờ xuất bến: 60 phút (tự huỷ vé đặt qua điện thoại, REQ-32) và 15 phút (gửi danh sách về máy soát vé, REQ-69). Prompt không nói thế nào là "nhịp độc lập", nên không phân định được giữa một Bộ định thời hai dòng Kích hoạt và hai tác nhân. A-T5 theo chữ có thể dẫn tới tách vì hai tập mục tiêu khác nhau.
   - Xử lý: gộp một ACT-09 với hai dòng Kích hoạt, ghi lựa chọn ở Vấn đề còn mở.

2. Hết thời gian giữ chỗ 10 phút có phải tác nhân thời gian không.
   - Vị trí: Bước 2.3, "Hết giờ chờ trong một phiên đang mở của tác nhân (... chờ thanh toán) không tạo ứng viên tác nhân thời gian ... Chỉ tạo ứng viên khi mốc thời gian rơi vào lúc không còn phiên nào của tác nhân đang mở".
   - Gặp: nguồn giữ chỗ 10 phút "để hành khách thanh toán", nhưng hành khách có thể đóng trình duyệt thì phiên không còn mở mà chỗ vẫn bị giữ; prompt không nói "phiên" là phiên trình duyệt hay phiên nghiệp vụ.
   - Xử lý: theo chữ "chờ thanh toán" loại ứng viên, ghi vào Mục 4 với lý do Bước 2.3.

3. Quy tắc tổng quát hoá mâu thuẫn nhẹ với A-T5 / Bước 4.1.
   - Vị trí: A-T5 "tập mục tiêu, quyền hoặc cách tương tác khác với mọi tác nhân còn lại"; Bước 5 "Chỉ tạo tác nhân cha khi ... Có từ hai tác nhân con".
   - Gặp: "Hành khách có tài khoản" có thêm mục tiêu (xem lịch sử vé) so với hành khách vãng lai; theo A-T5 có thể tách, nhưng chỉ tách thành một vai trò con thì Bước 5 không cho tạo cha. Tương tự "Nhân viên nhà xe" chung mỗi mục tiêu đăng nhập, "thường từ hai mục tiêu chung trở lên" chỉ là heuristic, không rõ có áp dụng cứng không.
   - Xử lý: không tách, không tạo cha, ghi ở Vấn đề còn mở.

4. Nhãn Giao tiếp ngoài của P00 không khớp với kết luận ranh giới của P01.
   - Vị trí: P00 REQ-64 "Hệ thống trao đổi dữ liệu vé với máy soát vé cầm tay" (Giao tiếp ngoài), SH-11 "Tương tác trực tiếp: Có"; P01 Bước 1.2 (thiết bị chạy phần mềm của hệ thống thì phần mềm là Trong, máy là nền tảng).
   - Gặp: Bước 7.1 đòi mọi REQ Giao tiếp ngoài có ít nhất một tác nhân; máy soát vé không là tác nhân nên REQ-64 và REQ-77 không có tác nhân Thiết bị. Prompt không nói rõ nên gắn vào người thao tác (Phụ xe) hay ghi lý do.
   - Xử lý: gắn REQ-64, REQ-77 vào ACT-05, ghi lý do ở Vấn đề còn mở; không đưa vào Đề xuất sửa artifact trước vì P00 không sai về nội dung.

5. Điều kiện áp dụng Bước 1.2 về thiết bị phụ thuộc điều mà nguồn không nói.
   - Vị trí: Bước 1.2 "thiết bị trong HE_THONG_NGOAI mà dự án cài phần mềm của hệ thống lên ... khi nguồn giao cho nó hành vi nghiệp vụ".
   - Gặp: nguồn giao hành vi cho "máy" nhưng không nói dự án có xây phần mềm trên máy không. Prompt không nói coi điều kiện "dự án cài phần mềm" là suy ra từ hành vi hay là chỗ thiếu.
   - Xử lý: coi là chỗ thiếu làm đổi danh sách tác nhân (Conventions C1.2), tạo Q-38 và ASM-10.

6. Có nên hỏi về tính chất của Cổng thanh toán không.
   - Vị trí: Format, cột Tính chất, ví dụ "Cổng thanh toán tự gửi thông báo ... thì là Chính và phụ"; Conventions C1.2 "chỗ thiếu làm thay đổi ... tác nhân".
   - Gặp: C1.2 chỉ nhắc danh sách tác nhân hoặc mục tiêu, không nói thuộc tính Tính chất; nguồn không nêu cổng có callback hay không (P00 Q-19 chỉ gián tiếp).
   - Xử lý: tạo Q-39 và ASM-11 cho an toàn. Có thể là dư so với ý prompt.

7. Q-01 / Q-02 của P00 và tác nhân Người quản trị hệ thống: prompt không nói có nên liệt kê ứng viên không được nguồn nhắc nhưng được P00 đưa ra làm phương án. Xử lý: ghi vào Mục 4 với A-T6.

8. Cột REQ của tác nhân chỉ nói "REQ chứng minh sự tồn tại và vai trò"; không nói có kèm REQ Quy tắc nghiệp vụ hay Dữ liệu không. Xử lý: kèm REQ quy tắc, dữ liệu có liên quan trực tiếp tới mục tiêu của tác nhân; REQ-02, REQ-19, REQ-75 không gắn tác nhân nào.

9. Quá tải ngữ cảnh: không gặp. P00 dài khoảng 51 KB nhưng đọc được hết trong hai lượt.

## Mục Target không đạt

Không có.
