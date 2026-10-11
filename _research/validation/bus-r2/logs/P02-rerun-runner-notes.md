Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P02-rerun (chạy lại sau review, áp dụng UCR-01 đến UCR-04)

Kết quả: ghi đè bus-r2/design/P02-usecases.md, phiên bản 1.0 thành 1.1. 28 mã UC (UC-013 chuyển Loại, 27 UC hiệu lực: 25 User-goal, 2 Subfunction), 66 CAND, 29 EV, 77 REQ. Mã Q, ASM lớn nhất: Q-42, ASM-16 (đều do P02R cấp, chép nguyên mã, không cấp mã mới). Đã đối chiếu bằng script: tập REQ mỗi UC ở Bảng 4b khớp Mục 5; mọi kết luận CAND trỏ tới UC tồn tại và khác UC-013.

## Vướng mắc

1. Vị trí: Mục 4 [Context], "chép các Q-nn do P02R cấp vào mục Câu hỏi mở (giữ mã, cột Nguồn gây mơ hồ ghi \"P02R\")". Gặp: P02R cấp thêm ASM-15 (cho UCR-02) và ASM-16 (cho UCR-04), nhưng prompt chỉ nhắc chép Q-nn, không nhắc ASM-nn. Xử lý: chép cả ASM-15, ASM-16 vào mục Giả định vì Conventions C1.2 đòi mọi giả định mà nội dung dựa vào đều phải được liệt kê, và UCR-02, UCR-04 viện dẫn chúng.

2. Vị trí: Mục 4 [Context], cùng câu trên, cột "Nguồn gây mơ hồ ghi \"P02R\"". Gặp: P02R đã có nội dung cụ thể cho cột này (Mục 5 câu 1 và câu 3; ASM-04). Ghi đúng một chữ "P02R" thì mất căn cứ nguồn. Xử lý: ghi "P02R: <căn cứ gốc của P02R>", bắt đầu bằng "P02R". Chưa chắc là cách hiểu mà tác giả prompt muốn.

3. Vị trí: Phần D Mục 4, cột Mức "User-goal hoặc Subfunction"; Mục 4 [Context] "giữ mọi mã UC"; Conventions C3 "Phần tử bị loại vẫn giữ mã và ghi trạng thái Loại". Gặp: UCR-02 gộp UC-013 vào UC-012 và yêu cầu UC-013 "Loại, giữ mã". Prompt không nói UC bị loại nằm ở đâu trong Mục 4 và ghi trạng thái ở cột nào (cột Mức chỉ có hai giá trị). P03 đọc Bảng 4a nên có thể vẽ nhầm UC đã loại. Xử lý: giữ dòng UC-013 ở cả Bảng 4a, 4b; cột Mức ghi "Loại (gộp vào UC-012)", tác nhân chính và phụ ghi "-", Mô tả ngắn nêu lý do và điều kiện khôi phục (Q-41 trả lời "Có"). Cần prompt quy định rõ (cột Mức có giá trị "Loại" hay bảng riêng) và P03 phải biết bỏ qua dòng này.

4. Vị trí: Phần D Mục 6 "tổng số UC" và Target 12. Gặp: sau UCR-02 có hai cách đếm (28 mã, 27 hiệu lực). Prompt không nói UC Loại có tính vào tổng, vào số UC mỗi nhóm, và vào tỉ lệ Subfunction không. Xử lý: ghi cả hai ("27 hiệu lực trên 28 mã UC"), tính tỉ lệ Subfunction và số UC mỗi nhóm trên UC hiệu lực.

5. Vị trí: Mục 3 Bước 4 "giữ ứng viên đầu, các ứng viên còn lại kết luận Gộp vào (khi ứng viên đầu thành UC)" và Phần D Mục 3 danh sách sáu kết luận. Gặp: CAND-11 trước đó "Giữ thành UC-013"; sau UCR-02 phải đổi kết luận. UCR-02 không nói kết luận mới của CAND-11. Xử lý: CAND-06 giữ "Giữ thành UC-012" (ứng viên đầu), CAND-11 thành "Gộp vào UC-012", phép thử không đạt ghi U-T11, U-AP15 (trùng lặp, biến thể). CAND-50 (bước hoàn tiền mặt) chuyển từ "Là bước của UC-013" sang UC-012. Nếu tác giả muốn kết luận khác (ví dụ "Là bước của UC-012") thì prompt nên nêu.

6. Vị trí: Phần D Mục 4 cột Tác nhân chính, "UC mức Subfunction giữ theo Q4: ... ghi tác nhân chính của UC gốc kèm \"(qua UC-xxx)\"". Gặp: UCR-01 áp dụng cách ghi "(qua ...)" cho UC-008, là User-goal chứ không phải Subfunction, nên quy tắc cột này không bao quát. Theo P03 Bước 2.2 (tham chiếu ở cùng đoạn) ghi "(qua)" thì P03 không vẽ association ACT-02 với UC-008, ACT-02 tới UC-008 qua include từ UC-004, UC-005, UC-015. Điều này khớp ý UCR-01 nhưng prompt không cho phép tường minh với User-goal. Ngoài ra UCR-01 dùng dấu chấm phẩy ("ACT-01; ACT-02 ... (qua ...)") còn prompt nói nhiều tác nhân "ngăn bằng dấu phẩy". Xử lý: theo UCR-01 (dấu chấm phẩy để tách phần có "(qua ...)" khỏi phần tác nhân trực tiếp), giữ UC-008 là User-goal. Cần mở rộng quy tắc "(qua UC-xxx)" cho UC User-goal dùng chung nếu đó là chủ ý.

7. Vị trí: Phần D Mục 1 "Mỗi tác nhân chính ... có ít nhất một dòng" và Bước 1.1. Gặp: UCR-01 nói Mục 1 không có mục tiêu tìm chuyến của ACT-02 nhưng đề xuất sửa chỉ nhắc cột Tác nhân chính. Xử lý: thêm một dòng Mục 1 cho ACT-02 (mức User-goal, CAND-01, CAND-34), coi là sửa hệ quả. Mức "User-goal" ở dòng này hơi gượng vì với ACT-02 đây là đoạn trong bán vé; chọn theo mức của UC-008.

8. Vị trí: Mục 7 "Sửa hệ quả không thuộc UCR nào ghi UCR là \"Hệ quả của UCR-xx\"". Gặp: các sửa tiêu đề (phiên bản, đầu vào, mã Q, ASM cuối) là hệ quả chung của UCR-02 và UCR-04, không thuộc một UCR. Xử lý: ghi "Hệ quả của UCR-02 và UCR-04". Các sửa hệ quả khác (EV-08, Mục 1, Mục 6, lý do CAND) ghi chung trong dòng của UCR gốc, không tách dòng riêng.

9. Vị trí: Conventions C5 "Phiên bản | 1.0 (tăng khi chạy lại)". Gặp: không nói tăng số phụ hay số chính. Xử lý: 1.0 thành 1.1.

10. Vị trí: P02R Mục 3 UCR-03 "ở Mục 5 thêm UC-010 vào dòng REQ-17 (hoặc bỏ REQ-17 khỏi cột REQ của UC-010)". Gặp: hai phương án, prompt không nói chọn cái nào. Xử lý: chọn thêm UC-010 vào Mục 5 vì UC-010 mô tả thanh toán trong thời gian giữ chỗ (ASM-12), có căn cứ phủ REQ-17. Ngoài ra UCR-03 liệt kê các chỗ lệch; script đối chiếu tìm đúng các chỗ đó và không thêm chỗ nào khác.

11. Vị trí: Mục 3 "Chạy lại sau review ... UCR không áp dụng ghi mã và lý do vào mục Vấn đề còn mở". Gặp: cả bốn UCR đều được áp dụng nên không có mục nào để ghi. Không rõ có cần ghi câu "không có UCR bị bỏ qua" không. Xử lý: không ghi thêm. Mục Vấn đề còn mở chỉ sửa lại ghi chú xung đột quy tắc về trả vé và đổi vé cho khớp kết quả sau UCR-02.

12. Vị trí: P02R Mục 4 (danh sách UC đề xuất sau sửa) so với Bảng 4b. Gặp: P02R viết lại Mục tiêu của UC-012 cho hai kênh; các cột còn lại (Mô tả ngắn, Sự kiện kích hoạt, REQ, CAND nguồn) P02R không cho nên tự suy (thêm EV-13, REQ-35, REQ-41, CAND-11, CAND-50). Xử lý: tự suy từ UC-013 cũ; ghi trong Mục "Thay đổi so với phiên bản trước".

13. Vị trí: Phần D, Mục 4 Mô tả ngắn (UC-012). Gặp: "Khách" (mục tiêu theo P02R) và "Hành khách" (tên ACT-01) cùng xuất hiện, U-N4 yêu cầu thuật ngữ nhất quán. Xử lý: giữ "Khách" trong cột Mục tiêu của UC-012 theo P02R (bao hàm cả khách mua tại quầy, vốn không là tác nhân), giữ "Hành khách" khi nói tác nhân ACT-01.

14. Vị trí: Quy mô ngữ cảnh. Gặp: prompt P02 dài (418 dòng, hơn 30000 token), cộng P02 cũ 57KB, P02R 20KB, P00 51KB; công cụ đọc file cắt ở 25000 token nên phải đọc làm nhiều lượt. Không ảnh hưởng kết quả nhưng gần ngưỡng quá tải nếu chạy bằng chat. Tôi không đọc toàn bộ P00 (chỉ mục REQ liên quan và danh sách mã Q, ASM) vì các thay đổi lần này không đụng phạm vi P00.

## Mục Target không đạt

Không có. Đã kiểm 14 mục Target: Target 3 (mọi tham chiếu UC, CAND tồn tại; UC-013 không còn là đích của kết luận nào), Target 5 và 6 (UC-012 "Trả vé" 2 từ, không trùng U-AP), Target 8 (ma trận REQ đủ 77 dòng), Target 12 (nhóm Giá vé, Soát vé, Báo cáo vẫn 2 UC, đã có nhận xét).
