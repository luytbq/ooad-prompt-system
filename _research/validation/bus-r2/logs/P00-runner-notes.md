Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P00 - bus-r2

Tham số: TRONG_TAM_PHAN_TICH = Không có; YEU_CAU_BO_SUNG = Không có. Lần chạy đầu, chưa có Q, ASM nào trong bus-r2/design/ nên mã bắt đầu từ Q-01, ASM-01.

Kết quả: 77 REQ, 11 SH, 37 Q (Q-37 là lớn nhất), 9 ASM (ASM-09 là lớn nhất), 37 dòng ở mục 5. Mọi mục Target tự kiểm Đạt, có ghi các lựa chọn khó ở mục Vấn đề còn mở của artifact.

## Vướng mắc

1. Vị trí: F2, cột REQ: "REQ chỉ có nguồn là trường HE_THONG_NGOAI nhận mã sau mọi REQ lấy từ tài liệu nguồn", và F3 câu 1: "Mỗi hệ thống, thiết bị ngoài mà nguồn hoặc HE_THONG_NGOAI nêu có một REQ Giao tiếp ngoài riêng".
   Gặp: cả bốn hệ thống ngoài (cổng thanh toán, cổng SMS, máy soát vé, máy in vé) đều vừa được nguồn nhắc gián tiếp vừa có trong hồ sơ. Prompt không nói REQ Giao tiếp ngoài trích cả hai nguồn thì đánh mã theo vị trí câu nguồn hay xếp cuối.
   Xử lý: REQ có cả câu trích nguồn và HE_THONG_NGOAI đánh mã theo vị trí câu nguồn (REQ-16, 21, 27, 64); chỉ REQ-77 (Android) có nguồn duy nhất là hồ sơ nên xếp cuối. Trích nguồn gồm cả hai.

2. Vị trí: F2 quy tắc 5: "Ngưỡng định lượng (số ngày, số giờ, số phút, số lần, số lượng tối đa) luôn tách thành REQ Quy tắc nghiệp vụ", so với F3 câu 4: "vẫn đúng kể cả khi làm bằng tay không có phần mềm".
   Gặp: "giữ 10 phút" và "15 phút trước giờ xuất bến gửi danh sách về máy" là tham số hành vi của hệ thống, không đúng khi làm bằng tay.
   Xử lý: theo quy tắc 5 (luôn tách, loại Quy tắc nghiệp vụ) cho REQ-14 và REQ-70; ghi ở Vấn đề còn mở. Nên làm rõ ngưỡng thời gian của hành vi hệ thống thuộc loại nào (Quy tắc nghiệp vụ hay Phi chức năng).

3. Vị trí: F2 quy tắc 6: "Không tách danh sách thành phần dữ liệu của một đối tượng" và quy tắc 7 về số liệu quy mô.
   Gặp: "Đội xe gồm khoảng 50 xe giường nằm 40 chỗ và 20 xe ghế ngồi 29 chỗ" là hai loại xe, mỗi loại có số xe và số chỗ riêng, có thể coi là hai REQ.
   Xử lý: giữ một REQ Dữ liệu (REQ-03). Prompt chưa nói số liệu quy mô có nhiều thành phần song song thì tách hay gộp.

4. Vị trí: F2 cột REQ: "REQ dựa trên giả định nhận mã ngay sau REQ nguồn mà nó phục vụ", so với "không nhảy số".
   Gặp: một ASM phục vụ nhiều REQ nguồn (ASM-02 đăng nhập nhân viên phục vụ bốn vai trò ở Mục 4 đến Mục 9; ASM-06 danh mục phục vụ REQ-01, 03, 06, 46, 47). Không rõ chọn REQ nguồn nào làm mốc.
   Xử lý: đặt ngay sau REQ nguồn xuất hiện đầu tiên (REQ-22 cho ASM-02, REQ-47 cho ASM-06).

5. Vị trí: Action bước 10 và Conventions C1.2: "chỗ thiếu làm thay đổi danh sách chức năng hoặc phạm vi" thì bắt buộc ASM.
   Gặp: ranh giới mơ hồ. Ví dụ Q-08 (đổi sang vé rẻ hơn): chọn "không hoàn" không thêm chức năng, nhưng đây đúng là dạng "quy tắc nguồn chỉ nêu cho một nhánh" nên tôi vẫn tạo ASM-05. Trong khi Q-12 (giới hạn 5 chỗ chỉ nêu cho luồng website) cũng là quy tắc một nhánh nhưng chỉ tạo Q, vì không thêm chức năng.
   Xử lý: tạo ASM khi chỗ thiếu thêm chức năng, tác nhân, hoặc là quy tắc một nhánh có hệ quả tiền; các chỗ thiếu còn lại chỉ có Q. Nên có tiêu chí rõ hơn.

6. Vị trí: Conventions C1.1 ("Không dùng hiểu biết chung ... để thêm chức năng, tác nhân") và F7: "Không ghi 'Thiếu' cho mọi chức năng mà loại hệ thống này thường có".
   Gặp: đăng nhập nhân viên và quản lý danh mục xe, tuyến, tài xế là điều hệ thống loại này thường có, nhưng nguồn cũng có chỗ dẫn tới (lập lịch phải "chọn tuyến, xe, tài xế"; nhân viên "dùng" hệ thống). Q-01 (đăng nhập nhân viên) là ca sát ranh giới nhất.
   Xử lý: chỉ ghi Thiếu khi có câu trích dẫn gợi ra (mục 5, hàng 1 và 2), và vẫn tạo Q + ASM theo CO_NHAN.

7. Vị trí: F2 "Mức hợp lý": "Tài liệu nguồn 1 trang thường cho khoảng 15-40 REQ; ... có thể tới 60-70 REQ".
   Gặp: kết quả 77 REQ trên nguồn khoảng 1 trang, vượt khung. Nguyên nhân: 21 REQ Quy tắc nghiệp vụ, 12 REQ giả định (CO_NHAN), 5 REQ hệ thống ngoài.
   Xử lý: giữ nguyên, ghi ở Vấn đề còn mở. Khung 60-70 chưa tính REQ giả định và Giao tiếp ngoài từ hồ sơ.

8. Vị trí: F2 "Trích nguồn": "kèm vị trí (tên tài liệu nếu có nhiều tài liệu, mục, đoạn, dòng)".
   Gặp: nguồn đánh số Mục 1 đến 10 nhưng mỗi mục có nhiều câu, đoạn mở đầu không đánh số; không có quy ước gọi câu.
   Xử lý: tự đặt "Mục n, câu m" và "Đoạn mở đầu, câu m". Mục 9 chỉ có một câu nên ghi "Mục 9".

9. Vị trí: F4 "Ngoài phạm vi chỉ gồm điều nguồn nói rõ, hoặc do TRONG_TAM_PHAN_TICH loại, hoặc là hệ thống khác mà hệ thống này chỉ trao đổi dữ liệu".
   Gặp: không có câu loại trừ nào trong nguồn; TRONG_TAM_PHAN_TICH là Không có. Mục Ngoài phạm vi chỉ có thể dựa vào nhánh "hệ thống khác".
   Xử lý: liệt kê bốn hệ thống, thiết bị ngoài, mỗi mục kèm câu trích. Không tự loại chức năng nào. Mục "Chờ Q-nn" bỏ vì không có mâu thuẫn phạm vi.

10. Vị trí: F3 câu 2/3 và mục 10 nguồn: "Hệ thống không lưu thông tin thẻ của hành khách".
    Gặp: câu phủ định có thể là Ràng buộc (pháp lý, quy trình) hoặc Phi chức năng (bảo mật).
    Xử lý: chọn Ràng buộc (REQ-76). F3 chỉ nói khi không rõ giữa Quy tắc nghiệp vụ và Phi chức năng thì chọn Phi chức năng; chưa bao quát lựa chọn Ràng buộc với câu phủ định.

11. Vị trí: F3 câu 2: "chỉ câu bắt buộc nền tảng hoặc công nghệ là Ràng buộc" áp dụng cho "Hành khách đặt vé qua website".
    Gặp: "qua website" có thể là Ràng buộc nền tảng hoặc chỉ là kênh của chức năng; hồ sơ ghi NEN_TANG là "Chưa chốt".
    Xử lý: giữ trong REQ Chức năng (REQ-04), ghi ở Vấn đề còn mở.

12. Vị trí: Target 7: "Mọi từ thuộc F6 xuất hiện trong REQ đã có dòng ở mục 5 và có Q-nn".
    Gặp: "khoảng" trong "khoảng 80 chuyến", "khoảng 50 xe", "khoảng 2.000" không có trong danh sách F6 nên không bắt buộc, nhưng "khoảng 2.000" trong yêu cầu hiệu năng không kiểm chứng được. Tôi ghi dòng 34 ở mục 5 (Không kiểm chứng được) với Q-34; hai số liệu quy mô còn lại để nguyên.
    Xử lý: như trên. Nên nói rõ "khoảng" kèm số có thuộc F6 không.

13. Vị trí: F9: "Sắp theo mức ảnh hưởng: câu hỏi làm đổi phạm vi hoặc danh sách chức năng đứng trước" với Conventions C3 (Q đánh số liên tục).
    Gặp: để bảng đúng thứ tự thì phải gán mã Q theo mức ảnh hưởng, nên mã Q không theo thứ tự xuất hiện trong nguồn; ASM thì tôi đánh theo thứ tự xuất hiện REQ. Không mâu thuẫn nhưng tốn công đánh số trước khi viết.
    Xử lý: chốt danh sách Q và ASM trước, gán mã theo mức ảnh hưởng.

14. Vị trí: Format, đoạn "(bảng thông tin theo C5)": hàng "Mã Q, ASM cuối đã cấp".
    Gặp: không vướng. Ghi nhận cho đủ: hàng Đầu vào đã dùng không cần ghi dải mã vì không dùng YEU_CAU_BO_SUNG.

Không có vướng mắc nào khác. Đã kiểm tra: không em dash, không mũi tên Unicode, không inline code; mục trống ghi "Không có". Không có file .drawio ở bước này.
