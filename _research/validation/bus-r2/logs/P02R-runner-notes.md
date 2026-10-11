Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P02R - bus-r2

Đầu ra: bus-r2/design/P02R-review.md. Phạm vi TAC_NHAN, DANH_SACH_UC; 0 Nghiêm trọng, 2 Trung bình, 2 Thấp; kết luận Đạt. Q-41, Q-42, ASM-15, ASM-16 mới (lớn nhất sau lần chạy: Q-42, ASM-16). Không có sơ đồ .drawio. Cả tám mục Target tự kiểm Đạt.

## Vướng mắc

1. U-R10 (nhánh a, b) với U-R12, U-AP15, và cách P02 dùng U-R12.
   - Vị trí: Phần A, U-R10: "a) Hai use case riêng khi thoả ít nhất một: luồng của người đại diện có một đoạn tương tác riêng từ 2 bước trở lên mà luồng của người được đại diện không có ... b) Không thoả a: một use case nối cả hai tác nhân chính"; U-R12: "chỉ tách hoặc tổng quát hoá use case khi luồng khác đáng kể"; U-AP15 "Thanh toán tiền mặt, Thanh toán thẻ".
   - Gặp: P02 tách UC-012/UC-013 (trả vé) và UC-014/UC-015 (đổi vé) theo kênh, viện "tác nhân phụ khác" và "tra vé, trao tiền mặt". Không rõ một "bước" là gì, "đoạn riêng" tính theo bước ở mức nào (tra vé và trao tiền mặt mỗi cái một bước nhưng có bước tương ứng ở luồng kia). Tác nhân phụ khác không nằm trong điều kiện a, nhưng U-R12 và U-AP15 dễ bị đọc theo hai chiều ngược nhau.
   - Xử lý: bắt lỗi UC-012/013 (UCR-02) vì không có đoạn riêng rõ; không bắt UC-014/015 vì ASM-14 cho UC-015 đoạn thu tiền mặt và in vé; ghi phụ thuộc Q-40 ở Mục 6. Hỏi người viết bằng Q-41, chọn gộp bằng ASM-15. Ranh giới "2 bước" mang tính chủ quan; hai review viên có thể ra hai kết quả khác nhau.

2. Q-41/ASM-15 và Q-42/ASM-16: prompt P02R không nói review có được tạo ASM hay không.
   - Vị trí: Phần C: "thêm bảng thông tin và các mục kiểm soát theo Conventions C5 (Câu hỏi mở, Giả định khi CO_NHAN ...)"; Conventions C1.2: "chỗ thiếu làm thay đổi danh sách chức năng, tác nhân hoặc use case phải có ASM-nn chọn một phương án của Q-nn"; Target 3: "Không có phát hiện đòi thêm chức năng mà tài liệu nguồn không nêu".
   - Gặp: Q-41 và Q-42 làm thay đổi danh sách đề xuất sau sửa nên theo C1.2 phải có ASM. Nhưng một người review chỉ nên chấm, tạo giả định là việc của bước tạo. Với Q-42 (UC-014 có gửi SMS mã vé mới) còn căng với Target 3 vì thêm tác nhân phụ nguồn không nêu rõ.
   - Xử lý: tạo ASM-15, ASM-16 theo C1.2, ghi ngay trong phát hiện là "cần xác nhận với nguồn" và nêu điều kiện bỏ phát hiện khi Q trả lời khác. Nên làm rõ trong P02R: review có tạo ASM không.

3. Mục 5 có điều kiện, C5 cấm xoá mục.
   - Vị trí: Phần C: "Mục 5. Quan hệ đề xuất sau sửa (khi phạm vi có SO_DO)"; C5: "Mục nào không có nội dung thì ghi Không có, không xoá mục".
   - Gặp: phạm vi không có SO_DO; không rõ bỏ hẳn hay giữ mục.
   - Xử lý: giữ tiêu đề, ghi "Không áp dụng: phạm vi review không có SO_DO". Mục 4b (điều kiện tương tự) có nội dung nên không bị ảnh hưởng.

4. "Đề xuất sửa artifact trước" không có nghĩa rõ trong P02R.
   - Vị trí: Phần C nêu mục này trong các mục kiểm soát; C1.3 định nghĩa là sửa bước trước.
   - Gặp: cả bản review là đề nghị sửa P02 (qua Mục 3), nên mục này trùng.
   - Xử lý: ghi "Không có", dẫn về Mục 3.

5. Mục 2 (bảng kiểm kê) vô ích khi đối tượng đã có mã.
   - Vị trí: "Đối tượng đã có mã thì ghi 'Không có, dùng mã gốc'".
   - Gặp: 37 dòng đều ghi cột Mã tạm cùng một chuỗi, chỉ có cột tên mang tin. Vẫn cần làm để thoả Target 8.
   - Xử lý: giữ nguyên bảng, một dòng mỗi phần tử. Có thể cho phép ghi ngắn: "Đối tượng đã có mã, bỏ bảng; Target 8 kiểm bằng Mục 4, 4b".

6. U-R04 và U-R05 đọc theo nghĩa đen mâu thuẫn với kết quả hợp lý.
   - Vị trí: U-R04: "CRUD dữ liệu danh mục cùng tác nhân gộp thành 'Quản lý X'; tách khi thoả một trong ..."; U-R05: "các báo cáo cùng tác nhân cùng cách thao tác gộp".
   - Gặp: P02 có bốn use case "Quản lý danh mục ..." cùng ACT-03, và hai báo cáo UC-027, UC-028 cùng ACT-04. Không rõ X là một danh mục hay mọi danh mục cùng tác nhân; không rõ "cùng cách thao tác" có kể khác tham số nhập (kỳ, tuyến, chuyến) không. Đọc đúng chữ thì phải gộp, nhưng gộp báo cáo buộc tên có "và" (U-N7) hoặc tên mơ hồ (U-N3).
   - Xử lý: không bắt lỗi; ghi lựa chọn ở Vấn đề còn mở. Nên làm rõ X và "cùng cách thao tác" trong prompt.

7. U-N7 "khoảng 2-6 từ" không nói đếm từ hay âm tiết tiếng Việt.
   - Vị trí: "U-N7 Khoảng 2-6 từ, không có 'và' nối hai mục tiêu".
   - Gặp: UC-025 "Gửi danh sách hành khách cho phụ xe" là 5 từ ghép hoặc 8 âm tiết; P02 đếm 7 và tự ghi vượt. 
   - Xử lý: không bắt lỗi (heuristic, "khoảng"); ghi ở Vấn đề còn mở.

8. Quy tắc "(qua <use case gốc>)" chỉ định nghĩa cho Subfunction, UC-008 là User-goal dùng chung.
   - Vị trí: Phần A, mục Subfunction: "Use case Subfunction mà tác nhân chính của use case gốc vẫn tương tác trực tiếp thì ghi tác nhân đó kèm '(qua <use case gốc>)'".
   - Gặp: UC-008 là User-goal độc lập (nguồn nói không cần tài khoản) nhưng cũng là đoạn dùng chung cho use case của ACT-02. Prompt không có quy tắc về User-goal được include, nên không có mã tiêu chí khớp chính xác cho UCR-01 (dùng U-T8, U-T11, đều gần đúng).
   - Xử lý: mượn cách ghi "(qua ...)" ở đề xuất sửa. Nên có tiêu chí cho trường hợp này, hoặc nêu rõ nó thuộc P03/D-AP11.

9. Không có mã tiêu chí khớp cho "thiếu tác nhân phụ".
   - Vị trí: Phần A, A-C4 chỉ nói tác nhân phụ bị ghi sai tính chất; U-R06, U-R08 là quy tắc ca tranh cãi.
   - Gặp: UCR-04 (UC-014 thiếu Cổng SMS) không có mã chính xác.
   - Xử lý: dùng U-R06, U-R08, A-C4 và hạ xuống Thấp. Nên thêm tiêu chí "thiếu tác nhân phụ".

10. Mức độ mặc định của U-T10 (Trung bình) quá nặng cho lỗi cột REQ không khớp.
    - Vị trí: Phần B: "U-T và U-R mặc định Trung bình".
    - Gặp: UCR-03 chỉ là lệch cột truy vết giữa Bảng 4b và Mục 5, không đổi tập use case; hạ xuống Thấp có ghi lý do, như Phần B cho phép. Cần cho phép này để Đạt/Đạt có điều kiện không bị đẩy sai.

11. Đầu vào quá lớn so với phạm vi đọc.
    - Gặp: P00 (khoảng 50 KB), P01 và P02 (tổng khoảng 73 KB) phải đọc toàn bộ, vì Mục 5 ma trận truy vết cần đối chiếu cột REQ. Không quá tải nhưng mỗi lần đọc phải chia trang. Kiểm tra tay sự lệch REQ giữa Bảng 4b và Mục 5 dễ sót.
    - Xử lý: đối chiếu từng REQ trong Mục 5 với cột REQ của UC tương ứng; chưa chắc đã bắt hết lệch. Nên có hướng dẫn: kiểm truy vết hai bảng bằng công cụ.

12. Quét mã Q, ASM trong THU_MUC_DAU_RA.
    - Gặp: C3 yêu cầu quét cả file không thuộc đầu vào; thư mục design/ chỉ có bốn artifact, lớn nhất Q-40 (P02) và ASM-14 (P02). Đã quét bằng lệnh có ranh giới ở cột Mã. Không vướng.

## Target

Cả tám mục Đạt. Target 3 chỉ Đạt sát ranh giới: UCR-04 dựa trên "vé mới" (Mục 5, câu 4) và REQ-19, REQ-20, không đòi chức năng mới nhưng thêm tác nhân phụ cho UC-014; đã gắn "cần xác nhận", Q-42 và ASM-16 (xem vướng mắc 2).
