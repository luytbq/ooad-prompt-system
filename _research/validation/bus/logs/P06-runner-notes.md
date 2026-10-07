# Nhật ký người chạy P06

Model: Sonnet (tham số model sonnet của công cụ Agent).

Đầu ra: design/P06-supplementary-spec.md (10 NFR, 33 BR hợp nhất, 7 Q mới Q-51 đến Q-57, 4 ASM mới ASM-38 đến ASM-41, 5 đề xuất sửa), design/P04-uc-specs/_BR-register.md (22 BR cũ + 11 BR mới BR-23 đến BR-33). Checklist: đạt 12/12 theo đánh giá của người chạy, riêng Target 4 đạt có điều kiện (xem mục 1).

## 1. Ngưỡng NFR ở chế độ CO_NHAN
- Vị trí: Action bước 6 "tạo Q-nn đề nghị bên liên quan chọn ngưỡng (NGHIEM_NGAT) hoặc tạo ASM-nn với ngưỡng đề xuất và lý do (CO_NHAN)"; F4 "Không lấy cách tính, số liệu từ ví dụ trong prompt này"; Target 4 "ghi 'Chưa đo được' kèm Q-nn (hoặc ASM-nn khi CO_NHAN)".
- Gặp: REQ-66 có ngưỡng "2.000 người" nhưng thiếu thời gian phản hồi, cách tính, mức đạt. Không rõ ở CO_NHAN phải đề xuất một con số hay chỉ cần ASM diễn giải. Ngoài ra "Chưa đo được" (không ngưỡng) và "Chưa quy định (Q-nn)" (thiếu từng phần) có thể cùng áp dụng cho một NFR.
- Xử lý: ghi tiêu chí đo dạng "Chưa đo được (Q-22)" kèm phần đo được và "Chưa quy định (Q-52)"; ASM-38 đến ASM-40 chỉ diễn giải, không đề xuất con số thời gian phản hồi vì không có căn cứ trong nguồn. Target 4 đánh giá đạt có điều kiện, ghi ở Vấn đề còn mở.

## 2. REQ loại Dữ liệu (REQ-01, REQ-02) không có chỗ rõ ràng
- Vị trí: Action bước 2 liệt kê "REQ loại Phi chức năng, Ràng buộc, Giao tiếp ngoài" và các trường hồ sơ; P02 Mục 5 ghi REQ-01, REQ-02 "Chuyển P06 (điều kiện dung lượng)"; P00 ghi chú "dùng làm điều kiện dung lượng ở P06".
- Gặp: prompt P06 không nhắc loại Dữ liệu, Target 1 cũng không đòi phủ. Hai bước trước lại chuyển chúng sang P06.
- Xử lý: không tạo NFR riêng (mỗi con số là một đại lượng, tách ra sẽ thành 5 NFR gượng ép); dùng làm điều kiện dữ liệu mẫu của NFR-01 (ASM-40) và đưa vào ma trận REQ --> NFR/BR để không bị mồ côi. Nên bổ sung loại Dữ liệu vào bước 2 hoặc nêu cách xử lý.

## 3. Xếp REQ-68 (không lưu thông tin thẻ) vào Mục 3 hay Mục 4
- Vị trí: F4 "NFR dạng có/không (không lưu dữ liệu X, ...)"; F3 "bảo mật" thuộc nhóm F; F5 "Ràng buộc thiết kế (mục 4): chỉ gồm điều nguồn hoặc hồ sơ đã chốt: nền tảng, ngôn ngữ, hệ quản trị dữ liệu, chuẩn bắt buộc, luật"; P00 xếp REQ-68 loại Ràng buộc.
- Gặp: P00 loại Ràng buộc, nhưng ví dụ ở F4 và F3 lại dẫn tới NFR bảo mật.
- Xử lý: xếp Mục 3, nhóm "F - Functionality (bảo mật) / Security". Ghi ở Vấn đề còn mở theo C9. Prompt nên nói rõ loại Ràng buộc của P00 không bắt buộc tương ứng Mục 4.

## 4. Mục 2 bị trống, định nghĩa "chức năng dùng chung" hẹp
- Vị trí: Action bước 3 "REQ loại Chức năng áp dụng cho nhiều use case mà không phải là một use case ... Chỉ lấy khi có REQ".
- Gặp: REQ-19 và REQ-48 cùng dùng kênh SMS nhưng mỗi cái là bước của một use case. Không REQ nào khác khớp. Phân biệt "chức năng dùng chung" với "kênh dùng chung đã là Giao tiếp ngoài" không rõ.
- Xử lý: Mục 2 ghi "Không có", giải thích ở Vấn đề còn mở. Dòng bảng "Không có" của Mục 2 điền ô đầu, các ô còn lại để trống (prompt chỉ nói "ghi Không có").

## 5. Quy tắc "giữ nguyên cột lõi" mâu thuẫn với "hợp nhất UC áp dụng"
- Vị trí: F6 "Cột lõi BR, Quy tắc, Loại, Áp dụng cho UC, REQ giữ nguyên nội dung từ sổ BR"; Action 8f "Hợp nhất danh sách UC áp dụng của mỗi BR"; F6 "BR chưa có trong đặc tả P04 nào lấy UC từ ma trận REQ --> UC của P02".
- Gặp: BR cũ như BR-02 (REQ-67) chỉ ghi UC-002 trong sổ, nhưng P02 gắn REQ-67 với UC-004, UC-005, UC-007 chưa có P04. Không rõ có thêm vào cột Áp dụng không.
- Xử lý: giữ nguyên cột cho 22 BR cũ để Target 10 khớp sổ; ghi UC bổ sung theo P02 ở cột Ghi chú và đánh dấu "(P02)" trong ma trận UC --> NFR/BR. Cần quy định rõ trong prompt.

## 6. Đề xuất đổi nội dung BR từ các bước trước hướng tới P06
- Vị trí: Action 8 "Không sửa nội dung quy tắc đã chốt; nội dung cần sửa thì ghi đề xuất"; UC-008 đề xuất "Khi hợp nhất BR ở P06 ... diễn đạt BR-02 là ..." ; P05 đề xuất "P04 (UC-002), P06 | BR-03 ...".
- Gặp: các artifact trước giao cho P06 việc diễn đạt lại BR-02, BR-03, BR-18, BR-19, trong khi prompt cấm đổi nội dung. Tình huống BR-02/BR-03 bị chính đề xuất đó coi là "mâu thuẫn với ASM-20" nhưng quy tắc d (mâu thuẫn giữa hai BR) chỉ áp dụng cho cặp BR, không cho BR với ASM.
- Xử lý: giữ nguyên nội dung, ghi năm dòng đề xuất sửa; không tạo Q mới vì Q-36 và Q-05 đã có. Prompt nên nói rõ cách xử lý mâu thuẫn giữa BR và giả định.

## 7. REQ-62 xếp loại Quy tắc nghiệp vụ nhưng giống chức năng kích hoạt theo thời gian
- Vị trí: F2 "bỏ phần mềm đi, câu vẫn có nghĩa với nhân viên --> quy tắc nghiệp vụ"; Target 8 "Mọi REQ loại Quy tắc nghiệp vụ trong P00 có BR tương ứng".
- Gặp: "Danh sách hành khách ... được gửi về máy soát vé 15 phút trước giờ xuất bến" không có nghĩa khi bỏ phần mềm; P00 vẫn xếp Quy tắc nghiệp vụ.
- Xử lý: theo P00 và Target 8, cấp BR-33 loại Kích hoạt hành động. Không có cơ chế trả REQ về P00 khi phép thử F2 không khớp, ngoài mục Đề xuất sửa.

## 8. Cấp một NFR hay nhiều NFR khi cùng REQ xuất hiện ở nhiều đặc tả P04
- Vị trí: Target 2 "Mọi dòng 'Yêu cầu đặc biệt' ... đã thành NFR có cột Áp dụng cho ghi đúng UC"; Action bước 7 "áp dụng cho UC đó".
- Gặp: REQ-35 xuất hiện ở UC-008 và UC-013, REQ-20 ở UC-002 và UC-013, phát biểu gần giống nhau.
- Xử lý: gộp thành một NFR với hai UC (NFR-07, NFR-08) và ghi ở Vấn đề còn mở. Prompt chưa nói gộp hay tách.

## 9. Ví dụ trong F4/F5 dễ dẫn tới thêm nội dung ngoài nguồn
- Vị trí: F4 "Tiêu chí đo ... Mỗi phần chỉ ghi điều nguồn nêu" cùng F4 "NFR dạng có/không: Tiêu chí đo là kiểm tra đặc tính ... (kiểm thử tích hợp)"; F5 ví dụ đúng "không yêu cầu cài đặt", "môi trường thử của nhà cung cấp".
- Gặp: phương pháp "kiểm thử tích hợp" không có trong nguồn nhưng F4 cho phép với NFR có/không; ví dụ F5 chứa chi tiết (môi trường thử, không cài đặt) mà nguồn SaoViet không có.
- Xử lý: dùng phương pháp kiểm tra cho NFR có/không, không chép chi tiết từ ví dụ; các phần thiếu (giao thức, model thiết bị, hành vi khi hệ thống ngoài lỗi) ghi "Chưa quy định (Q-nn)", tạo Q-54 đến Q-57. Ranh giới "nếu nguồn có" của F5 về hành vi khi hệ thống ngoài không phản hồi chưa rõ có bắt buộc tạo Q hay không; tôi tạo Q cho cổng thanh toán và cổng SMS.

## 10. Cột Nhóm cho ràng buộc thiết kế
- Vị trí: F3 "Cột Nhóm ghi dạng 'P - Performance / Performance efficiency'" và dòng "+ Ràng buộc thiết kế ... Không tương ứng trực tiếp".
- Gặp: cột sau dấu "/" không có giá trị ISO cho ràng buộc, trong khi Target 3 đòi "kèm đặc tính ISO/IEC 25010 tương ứng".
- Xử lý: ghi "+ Ràng buộc thiết kế / Không tương ứng trực tiếp".

## 11. Mã Q và ASM phụ thuộc P05 là đầu vào "Tuỳ chọn"
- Vị trí: Mục 2 "P05-glossary.md | Tuỳ chọn"; C3 "tìm mã Q và ASM lớn nhất đã thấy".
- Gặp: Q lớn nhất (Q-50) và ASM lớn nhất (ASM-37) nằm trong P05; nếu bỏ P05 sẽ trùng mã. Nếu P05 không có mà P02R hoặc P03 có Q, ASM cao hơn thì cũng trùng, nhưng P03 không nằm trong đầu vào P06.
- Xử lý: cấp tiếp từ Q-51 và ASM-38 dựa trên P05. Nên ghi cách xác định số lớn nhất khi không đọc hết các artifact (ví dụ qua P03).

## 12. Cỡ đầu vào
- Vị trí: Mục 3 "mọi đặc tả P04", "P02 (chỉ cần Mục 4 và Mục 5)".
- Gặp: P00 khoảng 50 KB, P02 khoảng 56 KB (chỉ đọc phần cần), bốn đặc tả P04 khoảng 130 KB, trong đó phần lớn là activity diagram không dùng. Phải đọc theo mục để tránh quá tải. Không vướng mắc nghiêm trọng với 4 UC; với hệ thống 18 UC đã đặc tả đủ sẽ lớn. Nên cho phép chỉ đính kèm Mục "Quy tắc nghiệp vụ", "Yêu cầu đặc biệt", Câu hỏi mở, Giả định của mỗi đặc tả.

## Target không đạt
Không có Target nào không đạt; Target 4 đạt có điều kiện (mục 1).
