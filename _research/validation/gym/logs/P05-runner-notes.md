Model của phiên chạy: Sonnet

# Nhật ký người chạy P05 - Từ điển thuật ngữ - gym (VietFit)

Kết quả: gym/design/P05-glossary.md, 43 thuật ngữ (GL-01 đến GL-43), 30 dòng ứng viên không đưa vào, Q-73 đến Q-75 mới (Q lớn nhất sau lần chạy: Q-75; ASM: chưa cấp), 9 dòng đề xuất sửa artifact trước. Không có file .drawio (P05 không có sơ đồ). Mọi mục Target tự đánh giá Đạt, có lưu ý ở mục Vấn đề còn mở của artifact. Đã kiểm bằng script: 43 dòng bảng lõi đủ 7 cột, tên tiếng Anh không trùng, bảng sắp đúng thứ tự chữ cái tiếng Việt, không có em dash, mũi tên Unicode, inline code.

## Vướng mắc

1. Phạm vi thu thập ứng viên khi nhiều use case chưa có đặc tả P04
   - Vị trí: mục 4, Action 2: "đọc P00, P02, các đặc tả P04 (luồng sự kiện, bảng dữ liệu, BR, tiền điều kiện, hậu điều kiện) và sổ BR. Lấy mọi danh từ, cụm danh từ chỉ đối tượng nghiệp vụ"; mục 3: "Có thể chạy sớm sau P02 để có bản nháp".
   - Gặp: chỉ 4 trên 28 use case có đặc tả. Prompt không nói rõ thuật ngữ chỉ có trong P00 hoặc P02 (Buổi tập cá nhân, Chỉ số cơ thể, Khung giờ trống, Chuyển nhượng gói tập, Tỉ lệ lấp đầy, Gói sắp hết hạn...) có phải đưa vào hay đợi đặc tả. Target 2 chỉ đòi phủ thuật ngữ trong đặc tả P04, còn Target 1 và F2 chỉ đòi xuất hiện trong "ít nhất một artifact (REQ, UC, BR)".
   - Xử lý: đưa vào theo F2 (xuất hiện ở REQ) để tránh bỏ sót, định nghĩa chỉ dựa trên REQ và P02, ghi cảnh báo ở mục Vấn đề còn mở. Hệ quả: 43 thuật ngữ, gần cuối khoảng 15-50 của F2; một phần định nghĩa mỏng vì UC chưa đặc tả. Cột Nguồn có UC chưa đặc tả (ví dụ UC-024), không rõ có hợp lệ không vì UC có trong P02 Mục 4.

2. F2 thiếu lý do loại cho nhiều ứng viên thực tế
   - Vị trí: F2 "Không đưa vào" (5 gạch) và F5: "Lý do theo các mục 'Không đưa vào' ở F2, hoặc 'Đồng nghĩa của GL-nn'".
   - Gặp: có nhiều loại ứng viên không khớp gạch nào: thuộc tính của thuật ngữ khác (thời hạn gói, ngày hết hạn, trạng thái đơn), thành phần dữ liệu trao đổi với thiết bị (kết quả cho phép vào), cách gọi theo vị trí (người đứng đầu danh sách chờ), đại lượng đếm, vai trò trong một quan hệ (gói cũ, gói mới), tên tác nhân hệ thống ngoài. Phần "Lỗi thường gặp: quá nhỏ" nói thuộc tính lẻ nên ghi ở Ghi chú của thuật ngữ cha nhưng không nằm trong danh sách lý do của F5.
   - Xử lý: tự viết lý do ngắn, ví dụ "Thuộc tính của Gói tập (ghi ở Ghi chú của Gói tập)". Đề xuất bổ sung vào F2/F5 các lý do "Thuộc tính / thành phần của GL-nn" và "Cách gọi theo vị trí của GL-nn".

3. Quy tắc đưa tên tác nhân vào từ điển mâu thuẫn mục đích bước
   - Vị trí: mục 1: "là nguồn đặt tên cho lớp entity"; F2: "Tên tác nhân chỉ đưa vào khi là vai trò nghiệp vụ đặc thù cần định nghĩa phân biệt với vai trò gần giống".
   - Gặp: Hội viên, Huấn luyện viên là entity cần tên tiếng Anh (Member, Trainer) nhưng không rõ "vai trò gần giống" nào. Hội viên, Khách vãng lai, Người quan tâm phân biệt được theo tài khoản và gói; Huấn luyện viên chỉ phân biệt hai nghĩa "phụ trách" (lớp nhóm, buổi tập cá nhân). Lễ tân, Quản lý chi nhánh, Giám đốc chuỗi không có vai trò gần giống nên bị loại, dù Quản lý chi nhánh và Giám đốc chuỗi vốn có thể cần tên entity.
   - Xử lý: đưa 4 tên (Hội viên, Khách vãng lai, Người quan tâm, Huấn luyện viên), loại 3 tên nhân viên, ghi lưu ý ở Vấn đề còn mở. Nhận xét: cột Tiếng Anh của tác nhân đã có ở P01 nên việc đưa tác nhân vào P05 có phần trùng lặp.

4. Chi nhánh, Phòng, SMS ở ranh giới F2
   - Vị trí: F2 mục b: "Từ phổ thông nhưng có nghĩa riêng, hẹp hơn hoặc khác" và "Không đưa vào: Từ phổ thông dùng đúng nghĩa thông thường".
   - Gặp: "chi nhánh" và "phòng" là từ phổ thông, nghĩa trong dự án gần nghĩa thông thường nhưng là entity trung tâm (sức chứa, cửa quay, gói theo chi nhánh), và "phòng tập" còn trùng nghĩa với "chuỗi phòng tập". Không có tiêu chí phân định.
   - Xử lý: đưa vào, ghi ở Vấn đề còn mở để người dùng quyết định.

5. Cách gọi theo vị trí ("người đặt chỗ", "người đứng đầu danh sách chờ", "người kế tiếp", "người đó") không có chỗ ghi
   - Vị trí: F3 cột "Từ đồng nghĩa không dùng"; F4: "cách gọi khác của nguồn (kể cả cách gọi xuất hiện nhiều nhất...) ghi vào cột Từ đồng nghĩa không dùng"; Action 7 phải đề xuất sửa mọi chỗ dùng.
   - Gặp: các cách gọi này là mô tả theo trạng thái của hội viên, có trong nguồn, REQ, BR-13 (nội dung BR trích nguyên nguồn). Nếu coi là đồng nghĩa của Hội viên thì phải đề xuất sửa hàng loạt artifact và cả BR, vô lý vì P01 đã gộp chúng vào ACT-02 (Mục 4).
   - Xử lý: không coi là đồng nghĩa, ghi ở Ghi chú của Hội viên, Danh sách chờ, Chỗ đã đặt và đưa vào bảng ứng viên không đưa vào. Nên làm rõ trong F4 hoặc F3 cách xử lý "cách gọi theo trạng thái".

6. Dạng rút gọn "gói" dễ nhầm hai khái niệm
   - Vị trí: F3 Từ đồng nghĩa không dùng: "Dạng rút gọn có thể chỉ khái niệm khác ('phiếu') thì ghi ở cột này"; đồng thời "dạng rút gọn ... không cần đề xuất sửa".
   - Gặp: nguồn và REQ dùng "gói" riêng (bảo lưu gói, chuyển nhượng gói, gói cũ, gói mới) trong khi có hai khái niệm Gói tập và Gói buổi tập cá nhân (Q-17, Q-18 đã hỏi). Làm đúng chữ F3 thì phải liệt "gói" ở cột đồng nghĩa và đề xuất sửa rất nhiều chỗ (chưa kể các cách dùng "gói cũ", "gói mới" hợp lý).
   - Xử lý: ghi "gói (dùng riêng, dễ nhầm...)" ở cột đồng nghĩa của Gói tập, vừa chấp nhận "gói" khi ngữ cảnh rõ ở Ghi chú, và chỉ đề xuất sửa các REQ mà Q-17 hỏi trực tiếp (REQ-47, REQ-48, REQ-51, REQ-53). Quy tắc có phần lấp lửng: không nêu cách phân định "ngữ cảnh rõ". Cũng đổi tên GL-06 thành "Chuyển nhượng gói tập" (theo tên UC-007) để tránh dùng "gói" riêng trong tên thuật ngữ.

7. Thứ tự sắp xếp chữ cái tiếng Việt chưa quy định
   - Vị trí: Action 8: "Sắp xếp thuật ngữ theo thứ tự chữ cái của cột Thuật ngữ"; Target 10: "bảng sắp theo chữ cái".
   - Gặp: không nói cách xử lý dấu thanh và chữ đ, ơ, ư, ô; hai cách sắp (bỏ dấu hoặc theo bảng chữ cái tiếng Việt) cho kết quả khác (ví dụ Giá gói trước hay sau Gia hạn).
   - Xử lý: dùng bảng chữ cái tiếng Việt, so chữ cái gốc trước rồi dấu thanh, ghi quy ước ở mục 1 Giới thiệu và kiểm bằng script.

8. Hai tên cho cùng một thời điểm: "giờ học" và "giờ bắt đầu"
   - Vị trí: Action 4: "Một từ mang hai nghĩa ... tạo Q-nn nếu không chắc"; Action 7 về BR trái định nghĩa.
   - Gặp: đặc tả UC-010 định nghĩa "Giờ học" là "ngày và giờ bắt đầu của lớp", UC-015 ghi rõ không giải thích hai cụm là một, BR-20 dùng "giờ bắt đầu lớp". Nguồn có 5 lần "giờ học" và 1 lần "giờ bắt đầu". Hướng dẫn không nói khi nghi đồng nghĩa nhưng chưa chắc thì có chọn thuật ngữ và đề xuất sửa không.
   - Xử lý: chọn Giờ học (theo tần suất, F4 mục 3), tạo Q-73, và đề xuất sửa các artifact có điều kiện "chờ Q-73". Phần đề xuất sửa BR-20 ghi cho P04 UC-018 theo Action 7.

9. Giao dịch thu tiền và giao dịch thanh toán
   - Vị trí: Action 4 và F4: "Nếu hai cách gọi có thể là hai khái niệm khác nhau ... không gộp; tạo hai thuật ngữ hoặc Q-nn".
   - Gặp: REQ-91 và BR-05 nói "giao dịch thu tiền"; UC-005 luồng 10a nói "giao dịch thanh toán". Có thể cùng một sự kiện nhìn từ hai phía hoặc "giao dịch thanh toán" chỉ là phần qua cổng. Nguồn không đủ để chắc.
   - Xử lý: coi là cùng khái niệm (dựa trên BR-05 áp dụng ở bước 12 của UC-005 sau thanh toán), đưa "giao dịch thanh toán" vào đồng nghĩa không dùng, và đề xuất sửa UC-005; không tạo Q riêng vì Q-37 đã hỏi phạm vi giao dịch thu tiền. Nếu chặt chẽ ở NGHIEM_NGAT thì nên có Q; ghi lại đây để người đánh giá cân nhắc.

10. Hệ quả của việc chưa áp dụng đề xuất sửa P02 (YEU_CAU_BO_SUNG)
    - Vị trí: Tham số bước, "REQ ... chỉ là dữ liệu do use case khác cung cấp".
    - Gặp: cột Nguồn của một số thuật ngữ (ví dụ Giá gói dùng REQ-78, Chương trình khuyến mãi dùng REQ-79, Chỉ số cơ thể) trỏ REQ mà P02 chưa gán cho UC đặc tả. Prompt không nói cột Nguồn dùng REQ theo P02 hay theo đặc tả.
    - Xử lý: ghi cả REQ và UC từ P02 lẫn UC đặc tả; cột Nguồn có mã REQ nên thoả "tối thiểu một mã". Không đưa đề xuất sửa P02 mới cho phần này vì đã chấp nhận ở yêu cầu bổ sung.

11. Dư đầu vào ngoài phạm vi đọc khi làm việc
    - Vị trí: mục 3: "chỉ cần mục 1 đến mục 8 và mục Câu hỏi mở, Giả định; không cần mục 9 Activity diagram; chạy bằng agent thì chỉ đọc các mục này".
    - Gặp: ranh giới "mục Câu hỏi mở, Giả định" so với hai mục cùng cấp liền sau là "Đề xuất sửa artifact trước" và "Vấn đề còn mở". Tôi đã đọc luôn cả hai mục này của bốn đặc tả (đọc theo khoảng dòng từ Câu hỏi mở đến hết file), và đã dùng một lần grep trên toàn P02-usecases.md để tìm cách gọi đồng nghĩa nên thấy cả các dòng ngoài Mục 4, Mục 5 của P02. Các đề xuất sửa P02 trong artifact chỉ trích dòng ở Mục 4, Mục 5 (UC-016, REQ-04, REQ-05, REQ-35, REQ-47...). Ghi ở đây để người đánh giá biết kết quả không phụ thuộc phần đọc dư này, nhưng nhắc rằng mục 3 không nói rõ Đề xuất sửa và Vấn đề còn mở có thuộc phạm vi đọc không.

12. Độ dài ngữ cảnh
    - Vị trí: mục 3: "giảm kích thước đầu vào khi chạy bằng chat".
    - Gặp: P00 khoảng 70 KB và P02 khoảng 74 KB; dù chỉ cần Mục 4, 5 của P02, P00 phải đọc toàn bộ vì "REQ, nhất là REQ loại Dữ liệu" mà prompt không chỉ rõ cần mục nào của P00. Tôi đọc toàn P00 (REQ, Q) để cấp mã Q, vẫn trong khả năng nhưng lớn. Gợi ý prompt chỉ rõ P00 chỉ cần mục 4 (bảng REQ) và mục Câu hỏi mở.

## Mục Target không đạt

Không có mục nào ở trạng thái Không đạt. Các lưu ý nằm ở mục Vấn đề còn mở của P05-glossary.md (phụ thuộc đặc tả P04 chưa có, các thuật ngữ ở ranh giới F2, định nghĩa của GL-20 theo hệ quả).
