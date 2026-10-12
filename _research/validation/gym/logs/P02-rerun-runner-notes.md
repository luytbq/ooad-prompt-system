Model của phiên chạy: Sonnet

# Nhật ký người chạy - P02 chạy lại sau review (áp dụng UCR-01, UCR-02, UCR-03)

Đầu ra: gym/design/P02-usecases.md (phiên bản 1.0 --> 1.1, ghi đè tại chỗ). Không có file .drawio. Số UC: 28 (không đổi), CAND-01 đến CAND-71, EV-01 đến EV-31 (không đổi). Q lớn nhất Q-49, ASM chưa cấp.

Kết quả Target: 14 mục đều Đạt. Chạy lại chỉ đổi 2 tên UC (UC-005, UC-021) và 4 câu Mục tiêu (UC-011, UC-015, UC-021, UC-022).

## Vướng mắc

1. Số phiên bản mới không được quy định.
   - Vị trí: Context, "tăng phiên bản"; Conventions C5, "1.0 (tăng khi chạy lại)".
   - Gặp: không nói tăng theo kiểu nào (1.1 hay 2.0), và P02R đã trích "P02 phiên bản 1.0" nên P03 trở đi sẽ phải trỏ tới phiên bản mới.
   - Xử lý: chọn 1.1 vì chỉ đổi tên và câu mục tiêu, không đổi danh sách UC. Ghi lựa chọn trong mục Thay đổi so với phiên bản trước.

2. Không rõ tên ứng viên (CAND) có phải đổi theo khi UC đổi tên hay không.
   - Vị trí: Context, "giữ mọi mã UC, CAND, EV, Q, ASM; ... cùng các sửa hệ quả để artifact nhất quán".
   - Gặp: CAND-05 "Mua gói tập" và CAND-43 "Xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân" là tên ứng viên, còn UC-005, UC-021 đã đổi tên. Câu "sửa hệ quả để nhất quán" không nói tên ứng viên có thuộc phạm vi đó không. Đổi tên ứng viên thì mất dấu vết lịch sử; giữ nguyên thì U-N4 (nhất quán thuật ngữ) có thể bị đọc là lệch.
   - Xử lý: giữ nguyên tên mọi CAND vì CAND là bản ghi quá trình sinh ứng viên, và UCR không nêu. Không đưa vào bảng thay đổi.

3. Cột "Nguồn gây mơ hồ" ghi "P02R: " nhưng P02R lần này không cấp Q hoặc ASM nào.
   - Vị trí: Context, "chép các Q-nn, ASM-nn do P02R cấp vào mục Câu hỏi mở, Giả định (giữ mã, cột Nguồn gây mơ hồ ghi \"P02R: \" kèm căn cứ P02R đã ghi)".
   - Gặp: P02R-review.md ghi "Câu hỏi mở: Không có (review không cấp Q-nn mới)". Prompt không nói trường hợp rỗng này cần ghi gì.
   - Xử lý: không chép gì, ghi rõ ở Vấn đề còn mở của P02 rằng P02R phiên bản 1.0 không cấp Q, ASM mới.

4. Hàng "UCR không áp dụng" khi áp dụng đủ mọi UCR.
   - Vị trí: Context, "UCR không áp dụng ghi mã và lý do vào mục Vấn đề còn mở"; Cách chạy mục 3.
   - Gặp: cả ba UCR đều được áp dụng, prompt không nói có cần ghi một câu xác nhận "không có UCR bị bỏ qua" hay để trống.
   - Xử lý: thêm một gạch đầu dòng ở Vấn đề còn mở nêu rõ không có UCR nào bị bỏ qua.

5. Câu đề xuất của UCR-02 cho UC-015 đọc nhập nhằng.
   - Vị trí: P02R-review.md mục 3 UCR-02 (đầu vào, không phải prompt): "Những hội viên đã đặt chỗ lớp có dưới 3 người biết lớp đã bị huỷ".
   - Gặp: có thể đọc là "lớp có dưới 3 người biết" hoặc "dưới 3 người đặt chỗ". Prompt P02 không nói nguyên văn đề xuất của UCR có được chỉnh câu chữ hay phải chép nguyên.
   - Xử lý: giữ ý của UCR (bỏ vế "chỗ phòng được giải phóng") nhưng chỉnh thành "Những hội viên đã đặt chỗ trong lớp có dưới 3 người đặt biết lớp đã bị huỷ." cho rõ nghĩa, ghi nguyên văn thay đổi trong bảng Thay đổi. Đây là sai lệch nhỏ so với văn bản UCR; người dùng có thể đảo lại nếu muốn bám sát từng chữ.

6. Phạm vi đọc đầu vào của lần chạy lại hơi nặng so với việc cần làm.
   - Vị trí: Cách chạy, "Đính kèm thêm P02-usecases.md hiện có và P02R-review.md"; Context, "Đọc theo thứ tự ... P00 ... P01 ...".
   - Gặp: để đổi 2 tên và 4 câu mục tiêu, vẫn phải đọc toàn bộ P02 (khoảng 400 dòng, vượt giới hạn đọc một lần của công cụ, phải đọc 3 lượt) cộng prompt khoảng 420 dòng và Conventions. Không có chỉ dẫn rằng lần chạy lại chỉ cần đọc phần P02R chỉ tới. Không gây lỗi, chỉ tốn ngữ cảnh.
   - Xử lý: đọc đủ; với P00 chỉ lấy danh sách Q (để xác nhận Q lớn nhất Q-49), không đọc lại toàn bộ.

7. Việc kiểm tra Target khi chạy lại không có hướng dẫn thu hẹp.
   - Vị trí: Bước 11, "Chạy checklist [Target]".
   - Gặp: 14 mục Target viết cho lần chạy đầu. Với lần chạy lại chỉ các mục 6 (tên), 10 (Mục tiêu), 14 (khung C5) bị ảnh hưởng, nhưng prompt không cho phép rút gọn.
   - Xử lý: rà cả 14 mục ở mức nhanh, trọng tâm mục 6 (tên UC-005 có 6 từ, đạt U-N7; UC-021 "Phản hồi yêu cầu đặt buổi tập" 6 từ, không có từ cấm), mục 10 (bốn câu mục tiêu mới viết từ góc nhìn tác nhân và kiểm chứng được) và mục 14. Có một lưu ý nhỏ: "Phản hồi" gần nghĩa với động từ yếu theo U-N3 nhưng UCR yêu cầu và tên vẫn nêu kết quả "xác nhận hoặc từ chối" qua Mục tiêu; chấp nhận.

## Mục Target không đạt

Không có.

## Ghi chú thêm

- Tên UC-005 mới dùng "hoặc" nối "mua" và "gia hạn". U-N7 cảnh báo dấu hiệu "và" nối hai mục tiêu; "hoặc" ở đây nối hai biến thể của một mục tiêu (U-R12), đã ghi giải thích ở Vấn đề còn mở.
- Mục 6 (thống kê) và Mục 5 (ma trận REQ) không đổi vì danh sách UC, tác nhân, REQ phủ không đổi.
