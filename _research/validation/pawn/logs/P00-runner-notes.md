Model của phiên chạy: Sonnet

# Nhật ký người chạy P00 - Hệ thống quản lý chuỗi cầm đồ Phúc An

Tham số: TRONG_TAM_PHAN_TICH = bỏ mục 8 (chốt ca, định mức tiền mặt trong két); YEU_CAU_BO_SUNG = Không có. Đầu ra: design/P00-problem-brief.md (105 REQ, 20 SH, 35 Q, 8 ASM).

## Vướng mắc

1. Vị trí: mục F2 quy tắc 5, "Ngưỡng là điều kiện kích hoạt của hành vi hệ thống tự làm thì REQ chức năng dẫn mã REQ quy tắc" và "Mức hợp lý: mỗi REQ đọc riêng vẫn hiểu được".
   Gặp: các hành vi theo lịch (nhắc trước hạn 3 ngày, nhắc quá hạn 7 ngày, chờ thanh lý 15 ngày, huỷ giao dịch 10 phút) làm REQ-46, 62, 63, 66 chỉ đọc được khi mở REQ ngưỡng đi kèm. Hai yêu cầu của prompt không thoả đồng thời.
   Xử lý: theo quy tắc 5 (dẫn mã), ghi nhận hạn chế ở Vấn đề còn mở.

2. Vị trí: F2 quy tắc 5, "Ngưỡng định lượng (số ngày, số giờ, số phút, số lần, số lượng tối đa) luôn tách thành REQ Quy tắc nghiệp vụ".
   Gặp: "9 giờ sáng", "0 giờ mỗi ngày" là lịch chạy, không rõ có phải ngưỡng không. Câu phí trễ hạn "quá 3 ngày ... 1% tiền gốc" gồm hai con số cùng một chính sách; không rõ tách một hay hai REQ.
   Xử lý: giữ giờ chạy trong REQ chức năng; tách phí trễ hạn thành hai REQ quy tắc (ngưỡng 3 ngày, mức 1%).

3. Vị trí: F2 mục REQ, "REQ dựa trên giả định nhận mã ngay sau REQ nguồn mà nó phục vụ" cùng "đánh số theo thứ tự xuất hiện trong nguồn".
   Gặp: có hai tài liệu nguồn và biên bản (tài liệu 2) bổ sung cho các mục của tài liệu 1 (tin nhắc, phí trễ hạn, gia hạn, thanh lý); không rõ đánh số theo tài liệu hay theo chủ đề. ASM-01 phục vụ cả mục 3 lẫn đoạn mở đầu nên chọn REQ "gần nhất" tuỳ ý.
   Xử lý: đánh số theo thứ tự tài liệu rồi theo vị trí; Ghi chú nối REQ liên quan; REQ giả định đặt sau REQ nó phục vụ gần nhất.

4. Vị trí: F3 câu 1, "Mỗi hệ thống, thiết bị ngoài mà nguồn hoặc HE_THONG_NGOAI nêu có một REQ Giao tiếp ngoài riêng" và Action bước 1.
   Gặp: "Máy in nhãn mã vạch và máy quét mã vạch" ghép chung một ô trong HE_THONG_NGOAI, nguồn không nói phần mềm điều khiển máy in nhãn; mục đích của REQ máy in nhãn phải suy từ tên thiết bị (sát ranh giới "thêm ý").
   Xử lý: tách hai REQ (REQ-58 máy quét, REQ-105 máy in nhãn), kèm ASM-03 và Q-03 để làm rõ ai in nhãn.

5. Vị trí: F2 quy tắc 7, ví dụ "12 kho" và F6; Target 7.
   Gặp: "khoảng 400/600" (quy mô) không thuộc danh sách F6 nên không có dòng mục 5; "mọi hợp đồng", "mọi thay đổi" thuộc F6 "tổng thể tuyệt đối" nhưng bị giới hạn bởi danh sách trong ngoặc, rất khó phân biệt "độ phủ" với "số liệu nghiệp vụ xác định".
   Xử lý: ghi dòng mục 5 và Q cho "mọi" (Q-32, Q-33), không ghi cho "khoảng".

6. Vị trí: F3, cây quyết định cho câu thao tác thủ công ("Nhân viên định giá kiểm tra tài sản", "khách kiểm tra tài sản và ký biên nhận", "cất vào két", "dán nhãn").
   Gặp: không có loại hay hướng dẫn cho bước thủ công không có hành vi phần mềm; vừa không phải Bối cảnh thuần, vừa không hẳn Quy tắc nghiệp vụ.
   Xử lý: "kiểm tra tài sản" của nhân viên định giá xếp Bối cảnh; các câu còn lại xếp Quy tắc nghiệp vụ kèm Q hỏi phần mềm có ghi nhận không.

7. Vị trí: C1.2 / Action bước 10, "ASM-nn chọn một phương án ... khi chỗ thiếu làm thay đổi danh sách chức năng hoặc phạm vi", cùng F7 "Không ghi 'Thiếu' cho mọi chức năng mà loại hệ thống này thường có".
   Gặp: ranh giới chủ quan giữa chỗ thiếu "làm đổi danh sách chức năng" (cần ASM) và chỗ thiếu chỉ cần Q (ví dụ Q-11 chờ thanh lý còn đóng lãi được không, Q-14 chi hộ thất bại, Q-12 từ chối khoản vay đều có thể thêm chức năng). Kết quả: 35 Q, 8 ASM, khó xác định mức đủ.
   Xử lý: ASM cho 8 trường hợp "chức năng nguồn cần dữ liệu mà nguồn không nói ai tạo" hoặc "quy tắc chỉ nêu cho một nhánh"; còn lại chỉ Q.

8. Vị trí: F4 và Target 9, "Ngoài phạm vi chỉ gồm ... điều do TRONG_TAM_PHAN_TICH loại" so với câu mở đầu nguồn "quản lý ... tiền mặt tại quầy".
   Gặp: mục tiêu nghiệp vụ nêu "tiền mặt tại quầy", trong khi mục 8 (bị loại) là phần quản lý tiền mặt của ca và két; giải ngân, thu tiền vẫn thuộc phạm vi. Prompt không nói cách xử lý khi mục tiêu chung bị loại một phần.
   Xử lý: giữ mục tiêu, chú thích phần ngoài trọng tâm; ma trận ghi đoạn mở đầu là Bối cảnh, mục 8 hai dòng Ngoài phạm vi, không tạo REQ.

9. Vị trí: F7 mục Mâu thuẫn và Action bước 7, "Khi hai tài liệu mâu thuẫn, ghi cả hai ... vẫn tạo Q-nn".
   Gặp: biên bản mục 4 ("Quản lý cửa hàng đề nghị ... 12 lần") là đề nghị, không rõ đã chốt thành yêu cầu hay chưa; vẫn cần REQ (Target 1) hay không.
   Xử lý: tạo REQ-101 ghi chú "đề nghị, chưa rõ đã chốt", Mâu thuẫn với REQ-44, Q-09.

10. Vị trí: C3 cấp mã Q, ASM "đọc các artifact đầu vào đã có ... cấp tiếp" so với F9 "Sắp theo mức ảnh hưởng".
    Gặp: thư mục design chưa có Q, ASM nên bắt đầu từ 01; sắp theo mức ảnh hưởng khiến mã Q không theo thứ tự xuất hiện trong nguồn, ASM-nn và Q-nn khớp nhau (Q-01 đến Q-08) nhưng phải sắp lại số khi hoàn tất danh sách.
    Xử lý: sắp theo mức ảnh hưởng, ghi lại ở Vấn đề còn mở.

11. Vị trí: F3 ghi chú, "quy ước ... khi không rõ, chọn Phi chức năng và ghi chú".
    Gặp: "Số căn cước và ảnh thẻ căn cước ... phải được mã hoá khi lưu trữ" có thể là Ràng buộc (công nghệ) hoặc Phi chức năng (mức bảo vệ).
    Xử lý: chọn Phi chức năng (REQ-91), không ghi chú thêm.

## Mục Target

Tất cả 13 mục tự đánh giá Đạt. Lưu ý riêng: Target 3 và Target 4 đạt theo F2 nhưng REQ-46, 62, 63, 66 phụ thuộc REQ ngưỡng (xem vướng mắc 1).
