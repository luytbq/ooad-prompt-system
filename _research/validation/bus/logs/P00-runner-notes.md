# Nhật ký người chạy - P00

Model: mặc định của phiên điều phối (Claude Opus 5.5, claude-opus-5-5).

Đầu vào đã đọc: P00-problem-brief.md (prompt), 00-Conventions.md, README.md, bus/design/project-profile.md, bus/yeu-cau-xe-khach.md. Placeholder: TRONG_TAM_PHAN_TICH = Không có; YEU_CAU_BO_SUNG = Không có. CHE_DO_GIA_DINH = CO_NHAN.

Đầu ra: bus/design/P00-problem-brief.md (68 REQ, 14 SH, 25 Q, 5 ASM, 28 dòng vấn đề chất lượng). Bước này không sinh sơ đồ .drawio.

## Vướng mắc

### 1. F3 câu 1 mâu thuẫn với ví dụ REQ-14 ở F2

- Vị trí: F3 câu 1: "Câu nêu hành vi nghiệp vụ và chỉ nhắc hệ thống ngoài như kênh thực hiện thì đi tiếp các câu sau, ghi hệ thống ngoài ở cột Ghi chú." So với ví dụ đúng ở F2: "REQ-14 | Hệ thống gửi thông tin đơn hàng cho cổng thanh toán để thu tiền trước khi chuyển đơn cho nhà hàng. | Giao tiếp ngoài".
- Gặp gì: Mục 3 và Mục 5 của đề có "thanh toán qua cổng thanh toán trực tuyến của đối tác", "Vé mua trực tuyến được hoàn qua cổng thanh toán", "gửi qua SMS". Theo F3 thì là Chức năng (kênh ghi ở Ghi chú); theo ví dụ REQ-14 thì là Giao tiếp ngoài. Ví dụ REQ-14 vừa có hành vi nghiệp vụ (thu tiền trước khi chuyển đơn) vừa nhắc hệ thống ngoài, đúng trường hợp F3 bảo đi tiếp.
- Xử lý: theo F3. Hành vi thành REQ Chức năng hoặc Quy tắc nghiệp vụ có ghi kênh; mỗi hệ thống ngoài có thêm REQ Giao tiếp ngoài riêng (REQ-15, REQ-20, REQ-24, REQ-35). Ghi lựa chọn vào "Vấn đề còn mở" theo C9.

### 2. HE_THONG_NGOAI của hồ sơ dự án: có là nguồn của P00 không

- Vị trí: Conventions C1.1: "Nguồn sự thật là tài liệu đầu vào: tài liệu nguồn của dự án ..., trường HE_THONG_NGOAI của hồ sơ dự án (xếp sau mọi tài liệu nguồn)". P00 mục 2 và [Context] chỉ nói "các tài liệu nguồn liệt kê ở trường TAI_LIEU_NGUON"; Action 1, 11 và F8 chỉ nói "tài liệu nguồn".
- Gặp gì: HE_THONG_NGOAI chứa thông tin không có trong đề: máy soát vé là Android có đầu quét mã vạch, do nhà xe tự trang bị; cổng SMS dùng API REST; máy in là máy in nhiệt; cổng thanh toán "chưa có tài liệu API". Prompt không nói có được tạo REQ từ trường này không, trích thế nào, xếp thứ tự mã ra sao, có đưa vào ma trận phủ nguồn không.
- Xử lý: coi là nguồn theo C1.1. Chỉ dùng để bổ sung REQ Giao tiếp ngoài, Ràng buộc (REQ-56) và mục Ngoài phạm vi; mỗi REQ đó vẫn kèm câu trích đề nên đặt mã theo vị trí trong đề. Trích dạng "project-profile.md, HE_THONG_NGOAI". Thêm 4 dòng HE_THONG_NGOAI vào ma trận phủ nguồn. Đề xuất: P00 nêu rõ cách dùng HE_THONG_NGOAI.

### 3. Máy soát vé: hồ sơ ghi là hệ thống ngoài, đề giao cho máy hành vi nghiệp vụ

- Vị trí: HE_THONG_NGOAI "Máy soát vé cầm tay Android ..."; đề Mục 8 "Máy báo hợp lệ hay không hợp lệ ... Máy cần soát được cả khi xe ở vùng mất sóng và gửi lại kết quả khi có sóng".
- Gặp gì: đây là vấn đề của đầu vào hơn là của prompt. Nhưng P00 không có hướng dẫn khi hồ sơ dự án và tài liệu nguồn mâu thuẫn về ranh giới hệ thống. F4 chỉ xử lý mâu thuẫn giữa "câu nêu phạm vi" và "đoạn mô tả chi tiết" trong tài liệu nguồn.
- Xử lý: ghi Mơ hồ ở mục 5, tạo Q-01 (xếp đầu vì đổi phạm vi), tạo ASM-01 (phần mềm thuộc phạm vi, phần cứng là thiết bị ngoài), bảng SH ghi "Chưa rõ".

### 4. F4 không có chỗ cho chỗ thiếu làm đổi phạm vi (không phải mâu thuẫn)

- Vị trí: F4: "hai danh sách 'Trong phạm vi' và 'Ngoài phạm vi' (thêm danh sách 'Chờ Q-nn' khi có mâu thuẫn phạm vi ...)"; "Sai: 'Ngoài phạm vi: báo cáo thống kê' khi nguồn không nói gì về báo cáo (đây là chỗ thiếu, phải thành Q-nn ...)".
- Gặp gì: Mục 6 cần danh mục tuyến, xe, tài xế để lập lịch, nhưng không nói ai cập nhật danh mục. Không xếp được vào Trong (tự thêm chức năng), không xếp được vào Ngoài (nguồn không nói), cũng không có mâu thuẫn để dùng "Chờ Q-nn".
- Xử lý: tạo Q-03, thêm một câu "Chưa xếp vào danh sách nào ... chờ trả lời Q-03" dưới mục Phạm vi và ghi lý do vào "Vấn đề còn mở". Không tạo ASM để khỏi thêm chức năng dù đang ở CO_NHAN.

### 5. CO_NHAN: không có tiêu chí khi nào tạo ASM, khi nào chỉ tạo Q, khi nào tạo REQ dựa trên giả định

- Vị trí: Action 10: "CO_NHAN thì được tạo ASM-nn và có thể tạo REQ dựa trên giả định"; F6: "Không tự thay bằng con số (trừ chế độ CO_NHAN với ASM-nn)"; Target 7: "có Q-nn (hoặc ASM-nn khi CO_NHAN)".
- Gặp gì: đề có 25 chỗ cần hỏi. Prompt cho phép nhưng không nói nên giả định tới đâu: có nên tự đặt ngưỡng thời gian phản hồi cho REQ-66, đặt luật hoàn chênh lệch khi đổi sang vé rẻ hơn, thêm chức năng cập nhật danh mục hay không. Target 7 dùng "hoặc", gợi ý ASM thay được Q, trong khi F4 ở CO_NHAN lại bảo "vẫn giữ Q-nn".
- Xử lý: mọi vấn đề đều có Q. Chỉ tạo ASM (5 cái) khi cần một cách hiểu về cấu trúc để bước sau chạy được (ranh giới máy soát vé, kênh đổi trả, cách tính thời gian chạy, vai trò "quản lý", giữ chỗ khi đặt qua điện thoại). Không giả định con số nghiệp vụ. Chỉ một REQ dựa trên giả định (REQ-46). Đề xuất: P00 thêm tiêu chí chọn giữa Q và ASM, và nêu rõ ASM có thay Q hay đi kèm Q.

### 6. F6 "100%" xung đột với Target 7 khi hiểu theo nghĩa đen

- Vị trí: F6: "Tổng thể tuyệt đối: tất cả, mọi, luôn luôn, không bao giờ, 100%."; Target 7: "Mọi từ thuộc F6 xuất hiện trong REQ đã có dòng ở mục 5 và có Q-nn".
- Gặp gì: REQ-50 "Vé của chuyến bị huỷ được hoàn 100% giá vé" là tỉ lệ hoàn tiền xác định, không phải tuyên bố tuyệt đối. Hiểu đúng nghĩa đen thì phải tạo một Q không có nội dung cần hỏi.
- Xử lý: ghi dòng 27 ở mục 5 kết luận không mơ hồ, gắn Q-14 (câu hỏi đã có về cùng REQ), ghi vào "Vấn đề còn mở". Tương tự "tối đa" trong REQ-08, REQ-54 có kèm số nên không tính theo F6.

### 7. Quy tắc tách nguyên tử không nói gì về danh sách điều kiện và danh sách chiều báo cáo

- Vị trí: F2 quy tắc 1: "nếu có thể đạt một nửa câu và không đạt nửa kia, câu đó phải tách"; quy tắc 2 chỉ có ngoại lệ cho thao tác quản lý (thêm, sửa, xoá): "giữ một REQ ... và ghi chú 'Chưa tách vì nguồn không phân biệt'"; quy tắc 6 chỉ cho thành phần dữ liệu.
- Gặp gì: "Máy báo ... không hợp lệ (sai chuyến, vé đã huỷ, vé đã soát)" và "báo cáo doanh thu theo ngày, theo tuyến" đều qua được phép thử tách, nhưng tách ba điều kiện kiểm tra vé ra ba REQ thì quá vụn.
- Xử lý: tách báo cáo thành REQ-63, REQ-64, REQ-65; giữ một REQ-58 cho quy tắc kiểm tra vé, ghi "chưa tách ba trường hợp vì nguồn nêu chung một quy tắc kiểm tra" (mượn cách ghi của quy tắc 2). Hai cách xử lý này không hoàn toàn nhất quán vì prompt không có tiêu chí.

### 8. Mẫu câu F2 cần chủ thể, nhưng F6 bảo giữ câu bị động của nguồn

- Vị trí: F2: "Chức năng: '<Chủ thể> có thể <động từ> <đối tượng> ...'"; F6: "câu bị động không có chủ thể: 'đơn được duyệt' (ai duyệt?)" và "giữ nguyên từ đó trong Nội dung chuẩn hoá nếu nguồn chỉ có vậy".
- Gặp gì: "vé đặt qua điện thoại phải được thanh toán tại quầy" không có người thu tiền. Viết theo mẫu thì phải có chủ thể; giữ bị động thì sai mẫu (vi phạm "Tuân thủ" ở F5).
- Xử lý: REQ-26 ghi chủ thể "Nhân viên bán vé" (Mục 4 chỉ nêu vai trò này ở quầy), Ghi chú nói rõ chủ thể là suy luận, thêm dòng 26 ở mục 5. Với Quy tắc nghiệp vụ (REQ-36) giữ bị động vì mẫu câu Quy tắc nghiệp vụ không đòi chủ thể.

### 9. Thứ tự mã cho REQ dựa trên giả định

- Vị trí: Action 3: "Làm theo thứ tự xuất hiện trong nguồn để mã REQ tăng dần theo vị trí"; F2: "đánh số theo thứ tự xuất hiện trong nguồn".
- Gặp gì: REQ-46 chỉ có "Giả định ASM-03", không có vị trí trong nguồn.
- Xử lý: đặt ngay sau các REQ nó phục vụ (REQ-43 đến REQ-45).

### 10. Vị trí trích dẫn khi nguồn không đánh số đoạn, dòng

- Vị trí: F2: "kèm vị trí (tên tài liệu nếu có nhiều tài liệu, mục, đoạn, dòng)"; C5: "Artifact chỉ chứa kết quả, không chứa lời dẫn".
- Gặp gì: đề có đoạn mở đầu không đánh số và các mục 1-10, mỗi mục một đoạn nhiều câu. Phải tự đặt quy ước "Đoạn mở đầu", "Mục n, câu k". Để người đọc hiểu quy ước cần một câu giải thích trong artifact, có thể bị coi là lời dẫn mà C5 cấm.
- Xử lý: thêm một câu "Quy ước vị trí trích dẫn" ngay dưới bảng thông tin. Coi đây là nội dung cần thiết, không phải lời dẫn.

### 11. Mẫu câu Ràng buộc không phủ câu cấm

- Vị trí: F2: "Ràng buộc: '<Hệ thống/giải pháp> phải <ràng buộc ...>'".
- Gặp gì: "Hệ thống không lưu thông tin thẻ của hành khách" là câu cấm.
- Xử lý: viết "Hệ thống không được lưu thông tin thẻ của hành khách." (REQ-68).

### 12. Loại bên liên quan chồng nhau

- Vị trí: F4: "Loại: Người dùng trực tiếp / Người hưởng lợi gián tiếp / Chủ sở hữu, người đặt hàng / Người vận hành, quản trị / ...".
- Gặp gì: quản lý nhà xe vừa dùng hệ thống (đặt giá, xem báo cáo), vừa có thể coi là chủ sở hữu hoặc người vận hành. Cột Loại chỉ nhận một giá trị.
- Xử lý: Quản lý nhà xe (SH-12) là Người dùng trực tiếp; Nhà xe SaoViet (SH-01) là Chủ sở hữu.

### 13. Dòng "Mâu thuẫn" đã hoà giải: không rõ có cần ghi không và ghi Loại gì

- Vị trí: F7: "Nếu hai câu hoà giải được bằng điều kiện ..., ghi là 'Không mâu thuẫn, tách thành hai REQ có điều kiện' và không tạo Q."
- Gặp gì: "dưới 4 giờ không được trả" (Mục 5) và "hoàn 100% giá vé" khi huỷ chuyến (Mục 6). Không rõ câu "ghi là" thay cho cột Loại vấn đề hay cột Hướng xử lý.
- Xử lý: dòng 28, Loại vấn đề "Mâu thuẫn", Hướng xử lý "Không mâu thuẫn, tách thành hai REQ có điều kiện", cột Q/ASM "Không có".

### 14. C5 đòi phiên bản của đầu vào

- Vị trí: C5: "Đầu vào đã dùng | Danh sách file và phiên bản".
- Gặp gì: tài liệu nguồn và hồ sơ không có số phiên bản.
- Xử lý: ghi "(bản hiện có)".

## Kết quả tự kiểm tra theo Target

| Target | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | Ma trận phủ theo từng câu của đề, thêm dòng cho các trường hồ sơ đã dùng |
| 2 | Đạt | 67 REQ có câu trích, REQ-46 có ASM-03 |
| 3 | Đạt | Riêng REQ-58 giữ ba điều kiện kiểm tra trong một quy tắc, có ghi chú (vướng mắc 7) |
| 4 | Đạt | Mọi ngưỡng (5 chỗ, 10 phút, 60 phút, 24 giờ, 4 giờ, 1 lần, 10 giờ, 100%, 30%, 15 phút) là REQ Quy tắc nghiệp vụ riêng |
| 5 | Đạt | Chức năng 31, Quy tắc nghiệp vụ 23, Dữ liệu 5, Giao tiếp ngoài 4, Ràng buộc 3, Phi chức năng 2 |
| 6 | Đạt | Đã đối chiếu từng con số với đề |
| 7 | Đạt có điều kiện | "100%" ở REQ-50 gắn Q-14 chứ không có câu hỏi riêng (vướng mắc 6) |
| 8 | Đạt | CO_NHAN; không có con số tự thêm; nội dung giả định đều có mã ASM |
| 9 | Đạt | Ngoài phạm vi chỉ gồm điều nguồn hoặc HE_THONG_NGOAI nói rõ; không có câu phạm vi mâu thuẫn |
| 10 | Đạt | 14 SH ghi theo vai trò, có 4 hệ thống, thiết bị ngoài |
| 11 | Đạt | Chi tiết "API", "API REST", "Android" lấy từ HE_THONG_NGOAI, không tự thêm |
| 12 | Không áp dụng | Lần chạy đầu |
| 13 | Đạt | Đã kiểm bằng lệnh: không có em dash, không có mũi tên Unicode; số cột bảng nhất quán |
