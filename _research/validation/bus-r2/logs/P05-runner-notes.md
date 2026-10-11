Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P05 (bus-r2)

Đầu ra: bus-r2/design/P05-glossary.md (28 thuật ngữ GL-01 đến GL-28, 20 dòng ứng viên không đưa vào, 1 đề xuất sửa artifact trước, không cấp Q, ASM mới; Q-50, ASM-33 giữ nguyên).

Kết quả tự kiểm tra Target: cả 10 mục Đạt (có chú thích ở mục 1, 4, 9 dưới đây). Mục 9 không áp dụng vì chưa có bản P05 cũ.

## Vướng mắc

1. Phạm vi thuật ngữ, YEU_CAU_BO_SUNG mâu thuẫn với Action bước 2
   - Vị trí: mục 4, Action bước 2: "đọc P00, P02, các đặc tả P04 (luồng sự kiện, bảng dữ liệu, BR, tiền điều kiện, hậu điều kiện) và sổ BR. Lấy mọi danh từ, cụm danh từ chỉ đối tượng nghiệp vụ"; tham số bước: "chỉ có hai đặc tả P04 là UC-009 và UC-017; các use case khác trong P02 chưa được đặc tả".
   - Gặp: không rõ câu bổ sung là thông tin về đầu vào hay là giới hạn phạm vi. P00 có 77 REQ với nhiều khái niệm (Bến xe, Máy soát vé, Tài khoản...) chưa xuất hiện trong đặc tả nào.
   - Xử lý: hiểu là giới hạn phạm vi theo C9; chỉ đưa vào thuật ngữ có trong UC-009, UC-017, sổ BR; P00, P02 dùng để lấy mã nguồn và kiểm tra đồng nghĩa. Ứng viên còn lại ghi vào mục 3 với lý do "Chưa đưa vào lần chạy này".

2. F5 không có loại lý do cho ứng viên hoãn
   - Vị trí: F5: "Lý do theo các mục 'Không đưa vào' ở F2, hoặc 'Đồng nghĩa của GL-nn'".
   - Gặp: các ứng viên hoãn (Bến xe, Trả vé, Đổi vé, Soát vé, Tài khoản) không thuộc mục nào của F2 (chúng thoả F2 a), nên không có lý do hợp lệ để ghi.
   - Xử lý: tự đặt lý do "Chưa đưa vào lần chạy này: chỉ xuất hiện ở use case chưa có đặc tả P04", ghi trong Vấn đề còn mở.

3. Thứ tự chữ cái tiếng Việt chưa được quy định
   - Vị trí: Action bước 8 "Sắp xếp thuật ngữ theo thứ tự chữ cái của cột Thuật ngữ"; Target 10 "bảng sắp theo chữ cái".
   - Gặp: các cặp như "Số tiền hoàn" và "Sơ đồ chỗ" (ô, ơ), "Vé đã huỷ" và "Vé đang có hiệu lực" (dấu thanh, dấu cách), "Giá vé" và "Giao dịch" cho kết quả khác nhau tuỳ cách so sánh. Một công cụ sắp xếp theo mã Unicode sẽ cho thứ tự khác với bảng chữ cái tiếng Việt.
   - Xử lý: dùng bảng chữ cái tiếng Việt (ô trước ơ), bỏ qua dấu thanh, dấu cách đứng trước chữ cái; ghi quy ước trong Vấn đề còn mở. Bước sau và người rà cần biết quy ước này để kiểm lại thứ tự.

4. F4 mâu thuẫn nhẹ giữa mục 3 (cách gọi nhiều nhất) và mục 5 (tên use case) khi một cách gọi là dạng đầy đủ của cách gọi kia
   - Vị trí: F4 "3. Cách gọi xuất hiện nhiều nhất trong tài liệu nguồn" và "5. Cách gọi đã dùng trong tên use case đã chốt"; F3 cột Từ đồng nghĩa không dùng: "Dạng rút gọn của chính thuật ngữ chính thức (bỏ bổ ngữ mà nghĩa không đổi...)".
   - Gặp: "chuyến" nhiều hơn "chuyến xe" trong nguồn, nhưng tên UC-008 dùng "chuyến xe"; "tuyến" và "tuyến xe" tương tự (UC-020). F3 chỉ cho phép dạng rút gọn đi theo hướng "bỏ bổ ngữ", nên nếu chọn dạng ngắn làm chính thức thì dạng dài ở P00, P02 thành từ đồng nghĩa phải đề xuất sửa.
   - Xử lý: chọn dạng đầy đủ ("Chuyến xe", "Tuyến xe") làm chính thức, dạng ngắn là rút gọn được chấp nhận, ghi lý do ở Ghi chú và Vấn đề còn mở. Prompt nên nói rõ ưu tiên khi hai dạng chênh nhau chỉ ở bổ ngữ.

5. Biến thể ngữ pháp không thuộc "dạng rút gọn"
   - Vị trí: F3 cột Từ đồng nghĩa không dùng và Action bước 7 ("Dạng rút gọn được chấp nhận... không cần đề xuất").
   - Gặp: "chuyến bị huỷ" và "chuyến đã huỷ", "vé bị huỷ" và "vé đã huỷ", "chỗ còn trống" và "chỗ trống", "chỗ đang giữ" và "giữ chỗ" khác nhau ở từ chức năng, không phải bỏ bổ ngữ. Prompt không nói đây là từ đồng nghĩa hay dạng chấp nhận.
   - Xử lý: coi là cách nói cùng nghĩa, được chấp nhận, ghi ở Ghi chú; các ứng viên dạng "chỗ đang giữ", "chỗ còn trống" ghi vào mục 3 là "Đồng nghĩa của GL-nn".

6. Tên tác nhân là thuật ngữ chính thức, nhưng nguồn dùng "hành khách" rộng hơn mô tả ACT-01
   - Vị trí: F4 đoạn đầu: "Vai trò đã có tên tác nhân ở P01 thì tên tác nhân là thuật ngữ chính thức của vai trò đó"; Action bước 4: "Một từ mang hai nghĩa khác nhau trong nguồn thì tách thành hai thuật ngữ".
   - Gặp: P01 mô tả ACT-01 là người mua vé qua website, còn nguồn và REQ-56, REQ-69, BR-11 dùng "hành khách đã có vé", "danh sách hành khách" cho người đi theo vé. Nếu theo nghĩa hẹp của ACT-01 thì khoảng 15 chỗ ở P00, P01, P02, P04 là "dùng sai nghĩa" và phải đề xuất sửa, dù đó là trích nguồn.
   - Xử lý: định nghĩa "Hành khách" bao quát (người mua vé hoặc người đi theo vé), tách "Người đi" là hành khách ghi trên vé; không đề xuất sửa các chỗ trên. Prompt không có hướng dẫn cho trường hợp phạm vi nghĩa của tên tác nhân rộng hơn mô tả P01; có thể chọn phương án khác và ra kết quả rất khác về số đề xuất.

7. Tên tiếng Anh: Title Case với dấu cách hay PascalCase
   - Vị trí: F3 cột Tiếng Anh ("Time Slot", "Goods Receipt") và project-profile.md NGON_NGU_TEN_PHAN_TU "PascalCase cho lớp".
   - Gặp: ví dụ của F3 viết có dấu cách, hồ sơ dự án đòi PascalCase cho tên lớp; không rõ cột này theo quy ước nào.
   - Xử lý: viết theo ví dụ F3 (Title Case, dấu cách), ghi trong Vấn đề còn mở.

8. Chế độ CO_NHAN nhưng không phát sinh Q, ASM
   - Vị trí: Action bước 5: "Chỗ nguồn không đủ để định nghĩa thì ghi định nghĩa phần đã biết và tạo Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN)"; C5 khối thông tin "Mã Q, ASM cuối đã cấp".
   - Gặp: mọi chỗ thiếu nguồn của các thuật ngữ đều đã có Q, ASM từ P00 đến P04 (Q-10, Q-11, Q-18, Q-24, ASM-19, ASM-29...), nên chỉ dẫn mã sẵn có. Hai mục Câu hỏi mở và Giả định ghi "Không có". Khối thông tin ghi Q-50, ASM-33 (giữ nguyên), không rõ có cần ghi rõ "không cấp mới".
   - Xử lý: ghi "không cấp mã Q, ASM mới" ở hàng Đầu vào đã dùng.

9. Điểm cần xem lại: nội dung do P04 tự khẳng định không có ASM
   - Vị trí: Action bước 5 "chỉ dựa trên nguồn và các artifact đã có".
   - Gặp: định nghĩa Vé mua tại quầy (gồm vé đặt qua điện thoại đã thanh toán tại quầy) và Vé đang có hiệu lực lấy từ UC-017 mục 8 "Thông tin bổ sung", là phần P04 viết ra mà không gắn ASM hoặc Q (mục 8 của P04 không phải nơi cấp ASM). Prompt P05 không nói artifact trước nào được coi là đủ căn cứ.
   - Xử lý: dẫn "UC-017 mục 8" ở Ghi chú, không tạo Q mới. Mục Target 8 coi là Đạt vì bám artifact đã có.

10. Đầu vào quá tải ở mức vừa phải
   - Gặp: P00 (khoảng 51 KB), hai đặc tả P04 (29 KB, 36 KB) và P02 mục 4, 5 phải đọc gần hết để tìm đồng nghĩa; P04 chứa nhiều bảng Node, Edge của activity diagram không liên quan tới thuật ngữ. Prompt chỉ cho phép rút gọn P02, không nói P04 chỉ cần các mục 1 đến 3, 5, 6, 8 (bỏ mục 9).
   - Xử lý: đọc cả file; dùng grep để kiểm tra tần suất các cách gọi (giữ tạm, thời gian giữ, hành khách đã có vé, vé trực tuyến...).

## Mục Target không đạt

Không có. Lưu ý kèm theo: Target 2 chỉ kiểm cho UC-009, UC-017 và sổ BR theo phạm vi ở vướng mắc 1; Target 9 không áp dụng (chạy lần đầu).
