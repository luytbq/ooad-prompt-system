Model của phiên chạy: Sonnet

# Nhật ký người chạy P06 - đề gym (VietFit)

Đầu ra: design/P06-supplementary-spec.md (12 NFR, 40 BR, 5 Q mới Q-76 đến Q-80, không ASM), design/P04-uc-specs/_BR-register.md (ghi đè, 40 dòng). Không có sơ đồ .drawio ở bước này. Tự kiểm tra: sổ BR khớp bảng BR (mã, quy tắc, loại, UC áp dụng, REQ, trạng thái, ghi chú) bằng script; không có em dash, mũi tên Unicode.

## Vướng mắc

1. Mục 2 hay BR-14 (phân loại chức năng dùng chung với quy tắc nghiệp vụ)
- Vị trí: [Action] 3: "gửi thông báo theo một kênh chung"; F2: "Phép thử nhanh: bỏ phần mềm đi, câu vẫn có nghĩa với nhân viên --> quy tắc nghiệp vụ"; Target 6: "Không có phần tử nào vừa là NFR vừa là BR".
- Gặp: REQ-87, REQ-88 loại Chức năng, dùng chung bốn UC, đúng ví dụ "kênh chung" của Action 3; nhưng P04 UC-015 đã xếp thành BR-14 (Hiệu lực), P05 dẫn BR-14. Theo phép thử F2 câu này không có nghĩa khi bỏ phần mềm (nhắc tới "ứng dụng"), tức không phải BR. Prompt không có hướng dẫn cho chiều ngược (BR đã chốt thực chất là chức năng): [Action] 4 chỉ nói chuyển ứng viên sang bước 8, và bước 8 cấm sửa nội dung BR đã chốt.
- Xử lý: giữ BR-14 là BR, mục 2 ghi "Không có", ghi lý do ở Vấn đề còn mở và Ghi chú ma trận. Đề nghị bổ sung vào prompt cách xử lý BR thực chất là chức năng dùng chung (Loại + đề xuất sửa P04 hay giữ).

2. Cột Áp dụng cho UC khi BR có REQ phụ (BR-17)
- Vị trí: [Action] 8f và F6: "Cột Áp dụng cho UC là hợp của ba nguồn: ... UC chưa có đặc tả P04 mà ma trận REQ --> UC của P02 gắn với REQ của BR".
- Gặp: BR-17 có REQ-41 và REQ-10; P02 gắn REQ-10 với UC-001, UC-005, UC-026. Áp dụng máy móc thì quy tắc cửa quay "áp dụng" cho UC xem giá, mua gói, đặt giá, sai nghĩa. Prompt không phân biệt REQ chính và REQ phụ của một BR.
- Xử lý: chỉ lấy UC của REQ chính (REQ-41), giữ UC-018, ghi lý do ở Ghi chú và Vấn đề còn mở. Đề nghị prompt nói rõ chỉ hợp theo REQ chính, hoặc cho phép loại UC có lý do.

3. Đề xuất sửa P02 chưa áp dụng của P04 và cột Áp dụng cho UC
- Vị trí: [Action] 8e: "lấy các UC gắn với REQ đó trong ma trận truy vết REQ --> UC (Mục 5) của P02".
- Gặp: bốn đặc tả P04 đề nghị thêm REQ (REQ-78, 79, 69, 70, 73, 76, 22, 30, 34, 35, 10, 43, 46, 51) vào cột REQ của UC nhưng chưa áp dụng vào P02. Prompt không nói dùng P02 hiện hành hay P02 sau đề xuất.
- Xử lý: theo YEU_CAU_BO_SUNG, chỉ dùng P02 Mục 5 hiện hành; REQ đề nghị thêm không tính. Không có vướng mắc thêm nhờ YEU_CAU_BO_SUNG, nhưng prompt nên nêu quy tắc mặc định.

4. NFR từ hồ sơ dự án: RANG_BUOC_DAC_THU là ranh giới phạm vi, không phải ràng buộc thiết kế
- Vị trí: [Action] 2: "các trường HE_THONG_NGOAI, NEN_TANG, RANG_BUOC_DAC_THU trong hồ sơ dự án"; F5: "Ràng buộc thiết kế (mục 4): chỉ gồm điều nguồn hoặc hồ sơ dự án đã chốt (NEN_TANG, CONG_NGHE, RANG_BUOC_DAC_THU)".
- Gặp: hai ràng buộc đặc thù của hồ sơ (hoá đơn điện tử chỉ nhận dữ liệu; thù lao huấn luyện viên tính ngoài phần mềm) là loại trừ phạm vi, đã nằm ở P00 "Ngoài phạm vi". Phép thử F2 ("Điều gì giới hạn lựa chọn giải pháp?") mơ hồ cho loại này.
- Xử lý: tạo NFR-05, NFR-06 ở mục 4 dạng có/không, ghi bản chất ở Vấn đề còn mở. Không có REQ riêng nên REQ cột lấy REQ-92, REQ-83 (gần nhất); prompt chưa nói cột REQ dùng gì cho NFR bắt nguồn từ hồ sơ (với NEN_TANG cũng vậy, tôi mượn REQ-06, 11, 22, 39, 18, 69, 78 theo P01 Mục 1).

5. NEN_TANG gộp hai nền tảng và nhiều vai trò trong một trường
- Vị trí: F4 "Mỗi NFR một đại lượng"; F5 mục 4.
- Gặp: NEN_TANG nêu Android và iOS, web, và đối tượng dùng. Không rõ tách thành 1, 2 hay 3 NFR.
- Xử lý: 2 NFR (di động Android và iOS; web trên trình duyệt máy tính), "Toàn hệ thống". Q-78 hỏi phiên bản tối thiểu vì prompt nói NFR có/không "không cần Q-nn cho phương pháp" nhưng thiếu phiên bản thì không viết được kịch bản kiểm thử.

6. Cột Nhóm khi MO_HINH_CHAT_LUONG là ISO/IEC 25010 và nhóm không có đặc tính ISO
- Vị trí: F3: "Khi MO_HINH_CHAT_LUONG là ISO/IEC 25010 thì đảo thứ tự hai tên"; F3 dòng "+ Ràng buộc thiết kế | ... | Không tương ứng trực tiếp".
- Gặp: không có tên ISO để đặt trước cho ràng buộc thiết kế. Giao tiếp: F5 viết "+ Giao tiếp / Compatibility", đảo thành "Compatibility (Interoperability) / + Giao tiếp".
- Xử lý: ghi "Không tương ứng / + Ràng buộc thiết kế". Prompt nên cho dạng chuẩn.

7. NFR hiệu năng có tải nhưng không có ngưỡng đo (REQ-94)
- Vị trí: F4: "Nguồn định tính, không có ngưỡng: ... Tiêu chí đo ghi 'Chưa đo được (Q-nn)'" và "NFR dạng có/không".
- Gặp: REQ-94 có con số (1.500 hội viên) nhưng không có ngưỡng thời gian; REQ-96 có ngưỡng (1 giây) nhưng không có mốc đo. Hai quy tắc F4 (định tính hoàn toàn; ngưỡng có, điều kiện thiếu) không khớp hẳn REQ-94.
- Xử lý: phát biểu giữ 1.500 làm tải; Tiêu chí đo ghi mức đạt "Chưa đo được (Q-42)", cách tính "Chưa quy định (Q-76)". Prompt nên có ví dụ cho trường hợp tải có, ngưỡng đáp ứng không có.

8. Chủ thể "Cửa quay" của REQ-96
- Vị trí: F4: "Đối tượng phải cụ thể"; P00 giữ chủ thể "Cửa quay".
- Gặp: cửa quay là thiết bị do nhà cung cấp lắp, phần mềm chỉ kiểm soát phần trả lời. Đã có Q-41 hỏi mốc đo.
- Xử lý: giữ "Cửa quay (ACT-12) phản hồi trong vòng 1 giây", mốc đo chờ Q-41. Không đề xuất sửa P00.

9. Điều kiện đo và dữ liệu REQ-01 đến REQ-04
- Vị trí: [Action] 2: "REQ loại Dữ liệu mà P02 Mục 5 ghi 'Chuyển P06' (dùng làm điều kiện đo ... hoặc thành NFR nhóm P về dung lượng dữ liệu khi nguồn nêu như một yêu cầu)".
- Gặp: không rõ số liệu quy mô của nguồn có "nêu như một yêu cầu" không (câu mô tả hiện trạng). Phán đoán chủ quan.
- Xử lý: coi là điều kiện đo (dữ liệu mẫu) của NFR-01, NFR-02, không tạo NFR dung lượng; ghi lý do ở ma trận. REQ-03 (40 huấn luyện viên) chỉ dùng cho dữ liệu mẫu của NFR-01, hơi gượng.

10. Hành vi khi hệ thống ngoài không phản hồi
- Vị trí: F5: "dẫn Q, ASM đã có ở P00, P04 về đúng tình huống này; chưa có thì tạo Q-nn".
- Gặp: Q-65 (UC-015) chỉ hỏi cho thông báo lớp bị huỷ; Q-54 (UC-005) hỏi cho hoá đơn; cổng thanh toán không phản hồi chưa có Q. Mức "đúng tình huống" không rõ khi Q có sẵn hẹp hơn NFR áp dụng nhiều UC.
- Xử lý: tạo Q-77 (cổng thanh toán), Q-79 (mở rộng Q-65 cho mọi loại thông báo); dẫn Q-54, Q-72, Q-65 có sẵn. Máy POS không tạo Q theo ngoại lệ "chỉ nhận dữ liệu" (nhưng máy POS ở đây thậm chí không kết nối).

11. Mâu thuẫn BR-06 và BR-07: "tạo Q-nn" so với Q có sẵn
- Vị trí: [Action] 8d: "Phát hiện mâu thuẫn giữa hai BR: giữ cả hai, tạo Q-nn".
- Gặp: đã có Q-11 (P00) hỏi đúng mâu thuẫn này, sổ BR ghi sẵn "chờ Q-11". Tạo Q mới sẽ trùng, trái C3 "mã chỉ trỏ tới một câu hỏi".
- Xử lý: dùng Q-11, không tạo Q mới. Prompt nên ghi "tạo Q-nn nếu chưa có Q về mâu thuẫn đó".

12. Dòng "Ghi nhận <việc> chờ <sự kiện>" ở mục 8 của P04
- Vị trí: [Action] 2: "mọi việc 'Ghi nhận <việc> chờ <sự kiện>' ở mục 8 Thông tin bổ sung của đặc tả P04 (P04 F5.4)".
- Gặp: bốn đặc tả không có dòng nào đúng mẫu này (UC-005 có luồng chờ Q nhưng không theo mẫu). Không phải lỗi, chỉ ghi nhận đã tìm và không có.
- Xử lý: không tạo NFR nhóm R. Không có NFR độ tin cậy nào trong lần chạy này.

13. Mục Giả định ở chế độ NGHIEM_NGAT
- Vị trí: [Format] "## Giả định  (chỉ khi CO_NHAN)" so với C5 "Mục nào không có nội dung thì ghi 'Không có', không xoá mục" và các artifact P04, P05 có mục này ghi "Không có".
- Gặp: hai chỉ dẫn lệch nhau.
- Xử lý: bỏ mục vì [Format] nói "chỉ khi CO_NHAN" và liệt kê "đúng các mục sau". Chọn theo quy tắc riêng của bước (C9 mục 4 cao hơn C5); ghi ở Vấn đề còn mở.

14. Thuật ngữ P05 so với chữ của REQ khi cấp BR mới
- Vị trí: YEU_CAU_BO_SUNG "dùng thuật ngữ chuẩn của P05" so với Action 8e (cấp BR từ REQ) và F6 "Không sửa nội dung quy tắc đã chốt".
- Gặp: BR mới lấy từ REQ dùng "gói" riêng (REQ-47, 48, 51, 53), mà P05 khuyên "gói tập" nhưng chỉ khi Q-17 trả lời. Đổi sang "gói tập" là ngầm trả lời Q-17.
- Xử lý: giữ "gói" ở BR-25, 26, 29, 30 kèm Ghi chú Q-17; dùng "lớp nhóm", "giờ học" ở BR mới (BR-22, 36, 37). BR-20 giữ "giờ bắt đầu lớp", dẫn Q-73 và đề xuất sửa P04 theo Action 8d.

15. Số dòng đề xuất sửa P05 cho "(chưa có BR)"
- Vị trí: [Action] 10: "nếu P05-glossary.md có Ghi chú dẫn 'REQ-nn (chưa có BR)'".
- Gặp: P05 ghi theo nhiều dạng ("chưa có BR", "cả hai chưa có BR", "Các REQ-47 đến REQ-51 chưa có BR"), không đúng mẫu "REQ-nn (chưa có BR)". Phải rà tay từng GL (11 GL), có nguy cơ sót; GL-04 ghi REQ-68 (Chức năng) không có BR mới.
- Xử lý: rà tay, 11 dòng đề xuất. Prompt nên cho mẫu tìm hoặc để P05 ghi dạng chuẩn.

16. Quy mô ngữ cảnh và phạm vi đọc
- Vị trí: mục 3: "mọi đặc tả P04 (chỉ cần ... )" và C3 "kể cả file không thuộc đầu vào của bước (chỉ quét mã, không cần đọc nội dung)".
- Gặp: P00 phải đọc gần đủ (70 KB) vì cần REQ loại và Q; P02 Mục 5 gần 100 dòng. Chấp nhận được. C3 yêu cầu quét mã Q, ASM ở P02R-review.md và P03-usecase-model.md (ngoài danh sách được đọc của giao việc); tôi chỉ chạy grep mã ở cột Mã, không đọc nội dung. Kết quả: Q lớn nhất trước khi chạy là Q-75 (P05), ASM không có.
- Xử lý: ghi ở hàng Đầu vào đã dùng.

## Target không đạt

Không có mục Target nào không đạt. Các điểm đạt có điều kiện, đã ghi ở mục Vấn đề còn mở của artifact: Target 6 (BR-14 xếp BR, mục 2 trống), Target 7 và 10 (BR-17 cột UC áp dụng theo REQ chính), Target 4 (NFR-01, NFR-02 chưa đo được đầy đủ do Q-42, Q-41, Q-76).
