# Nhật ký người chạy P06 - SaoViet Bus

Model: mặc định của phiên điều phối (Claude Opus 5.5, claude-opus-5-5).

Placeholder: MO_HINH_CHAT_LUONG = Không có (dùng FURPS+ mặc định); YEU_CAU_BO_SUNG = Không có. Chế độ hồ sơ: CO_NHAN.

Kết quả: 11 NFR (Mục 2: 0; Mục 3: 4; Mục 4: 2; Mục 5: 5), 33 BR (22 cũ, 11 mới BR-23 đến BR-33, không gộp, không loại), 4 Q mới (Q-48 đến Q-51), 2 ASM mới (ASM-37, ASM-38).

## Vướng mắc

1. Mâu thuẫn về cột "Áp dụng cho UC" của BR đã có.
   - Vị trí: F6 "Cột lõi BR, Quy tắc, Loại, Áp dụng cho UC, REQ giữ nguyên nội dung từ sổ BR" và "BR chưa có trong đặc tả P04 nào lấy UC từ ma trận REQ --> UC của P02"; đối lập Action 8f "Hợp nhất danh sách UC áp dụng của mỗi BR" và bước 10 "Cập nhật sổ BR cho khớp bảng BR hợp nhất (trạng thái, UC áp dụng, BR mới)".
   - Gặp: BR-02 (REQ-67) trong sổ chỉ có UC-002, trong khi P02 Mục 5 gắn REQ-67 với UC-002, UC-004, UC-005, UC-007 và ghi "Quy tắc chung; chuyển P06". Tương tự BR-04 (UC-016), BR-10 (UC-005). Nếu giữ nguyên theo F6 thì bảng UC --> BR (F7) thiếu BR cho UC chưa đặc tả.
   - Xử lý: giữ nguyên nội dung quy tắc; bổ sung UC chưa có đặc tả P04 mà P02 Mục 5 gắn với REQ của BR (BR-02, BR-03, BR-04, BR-05, BR-06, BR-10), ghi nguồn ở Ghi chú và ghi lựa chọn C9 ở Vấn đề còn mở. Áp dụng máy móc theo REQ cho kết quả hơi lạ ở BR-05 (công thức giá gắn với UC-016, UC-017 là nơi đặt đầu vào, không phải nơi tính).

2. Đánh số Q, ASM khi chỉ được đọc một phần P02 và khi P05 chạy song song.
   - Vị trí: Conventions C3 "Lần chạy nào cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất đã thấy"; P06 mục 2 và mục 3 "với P02 chỉ cần Mục 4 (bảng use case) và Mục 5".
   - Gặp: mục Câu hỏi mở và Giả định của P02 (và P03) không được đọc, nên mã lớn nhất phải suy từ P04 (Q-47, ASM-36), dựa vào việc P04 chạy sau và đã cấp tiếp. Nếu P04 chưa chạy hoặc bỏ sót thì có nguy cơ trùng mã. Thêm nữa, P05 và P06 đều đứng sau P04 trong pipeline và README cho phép chạy hai bước này độc lập; nếu chạy song song, cả hai cùng cấp Q-48 trở đi. Prompt không có quy tắc chống trùng Q, ASM giữa hai bước song song (khác với BR có Action 8b).
   - Xử lý: cấp Q-48 đến Q-51, ASM-37, ASM-38 tiếp từ P04; ghi vào nhật ký này. Đề nghị: mục 3 của P06 nói rõ đính kèm thêm mục Câu hỏi mở, Giả định của P02, P03; README nói rõ P05, P06 chạy tuần tự hoặc dành dải mã riêng.

3. CO_NHAN với NFR không có ngưỡng: "Chưa đo được" hay ngưỡng giả định.
   - Vị trí: Action 6 "tạo Q-nn đề nghị bên liên quan chọn ngưỡng (NGHIEM_NGAT) hoặc tạo ASM-nn với ngưỡng đề xuất và lý do (CO_NHAN)"; F4 "Nguồn định tính, không có ngưỡng: ... Tiêu chí đo ghi 'Chưa đo được (Q-nn)'"; F4 "Không lấy cách tính, số liệu từ ví dụ trong prompt này"; C1.1 "Không dùng hiểu biết chung ... để thêm ... quy tắc mà nguồn không nêu".
   - Gặp: REQ-66 "chịu được khoảng 2.000 người" không có ngưỡng thời gian phản hồi (Q-22 có sẵn). Ở CO_NHAN, Action 6 bảo đặt ngưỡng đề xuất, nhưng lý do của mọi ngưỡng thời gian phản hồi chỉ có thể là hiểu biết chung, va với C1.1. Ví dụ đúng trong F4 dùng "2 giây" và "phân vị 95", lại bị cấm lấy theo, nên người chạy phải cố tình chọn số khác (3 giây, phân vị 90) chỉ để khác ví dụ. Không rõ khi đã có ASM thì Tiêu chí đo còn ghi "Chưa đo được" không.
   - Xử lý: NFR-02 dùng ngưỡng ASM-38 (3 giây, phân vị 90), Tiêu chí đo ghi đủ phương pháp, điều kiện, cách tính, mức đạt kèm "(ASM-38, chờ Q-22)", không ghi "Chưa đo được". Đề nghị prompt nói rõ ở CO_NHAN mẫu Tiêu chí đo khi dùng ASM và cho biết nguồn hợp lệ cho lý do của ngưỡng đề xuất.

4. REQ-66 "chịu được" chứa hai đại lượng.
   - Vị trí: F4 "Mỗi NFR một đại lượng"; F3 "Một NFR chỉ thuộc một nhóm; nếu thấy thuộc hai nhóm thì chưa nguyên tử, tách ra".
   - Gặp: "chịu được 2.000 người" vừa là số người dùng đồng thời (sức chứa) vừa ngầm chứa thời gian phản hồi và tỉ lệ lỗi. Không có hướng dẫn cách tách khi tiêu chí "chịu được" lại phụ thuộc NFR khác.
   - Xử lý: tách NFR-01 (sức chứa, mức đạt dẫn sang NFR-02 và tỉ lệ lỗi theo ASM-37) và NFR-02 (thời gian phản hồi). Tỉ lệ lỗi không thành NFR riêng mà nằm trong mức đạt của NFR-01 (ASM-37, Q-48); có thể bị coi là hai đại lượng trong một NFR.

5. REQ loại Dữ liệu được P02 "chuyển P06" nhưng P06 không thu thập.
   - Vị trí: Action 2 "Thu thập ứng viên NFR: mọi REQ loại Phi chức năng, Ràng buộc, Giao tiếp ngoài trong P00"; F7 "gồm mọi REQ loại Phi chức năng, Quy tắc nghiệp vụ, Giao tiếp ngoài, Ràng buộc".
   - Gặp: P02 Mục 5 ghi REQ-01, REQ-02 (Dữ liệu, quy mô tuyến, chuyến, xe) "Chuyển P06 (điều kiện dung lượng)". Đầu vào không khớp đầu ra giữa P02 và P06.
   - Xử lý: dùng REQ-01, REQ-02 làm điều kiện đo (dữ liệu mẫu) của NFR-01 và vẫn đưa vào Bảng 7a với ghi chú, không tạo NFR dung lượng riêng.

6. Phân loại REQ-68 "không lưu thông tin thẻ".
   - Vị trí: F2 "Câu nói tới công nghệ, nền tảng, chuẩn, luật mà không nói hành vi --> ràng buộc"; F2 ví dụ NFR bảo mật "Mật khẩu được lưu dưới dạng băm"; F3 nhóm F gồm "bảo mật"; F5 Mục 4 "chỉ gồm điều nguồn hoặc hồ sơ đã chốt ... nền tảng, ngôn ngữ, hệ quản trị dữ liệu, chuẩn bắt buộc, luật".
   - Gặp: P00 xếp REQ-68 loại Ràng buộc; câu không nêu công nghệ mà nêu đặc tính lưu trữ dữ liệu, giống ví dụ NFR bảo mật. Prompt không nói rõ NFR nhóm "F - Functionality / Security" nằm ở Mục 2 (Yêu cầu chức năng dùng chung) hay Mục 3 (Yêu cầu phi chức năng), vì F3 gộp chức năng dùng chung và bảo mật vào cùng nhóm F.
   - Xử lý: NFR-04 nhóm F - Functionality / Security, đặt ở Mục 3; ghi lý do ở Bảng 7a và Vấn đề còn mở.

7. Cột Nhóm của ràng buộc thiết kế.
   - Vị trí: F3 "Cột Nhóm ghi dạng 'P - Performance / Performance efficiency'" và Target 3 "Mọi NFR có đúng một nhóm FURPS+ kèm đặc tính ISO/IEC 25010 tương ứng"; ví dụ F5 chỉ ghi "+ Ràng buộc thiết kế".
   - Gặp: ví dụ đúng của F5 không có phần ISO, Target 3 đòi có.
   - Xử lý: ghi "+ Ràng buộc thiết kế / Không tương ứng trực tiếp" theo bảng F3.

8. Hành vi khi hệ thống ngoài không phản hồi.
   - Vị trí: F5 "hành vi khi hệ thống ngoài không phản hồi nếu nguồn có".
   - Gặp: nguồn không nêu cho cả bốn hệ thống, thiết bị ngoài. Không rõ khi nguồn không có thì bỏ qua hay tạo Q (F4 bảo tạo Q cho phần thiếu của Tiêu chí đo, F5 chỉ nói "nếu nguồn có").
   - Xử lý: dẫn Q, ASM có sẵn từ P04 cho cổng thanh toán (Q-10, Q-37, Q-43, ASM-21, ASM-31); tạo Q-49 cho cổng SMS vì cả UC-002 và UC-013 đều chưa xử lý; với máy in và đầu quét chỉ tạo Q về model, kết nối (Q-50, Q-51).

9. Mục 2 "Yêu cầu chức năng dùng chung" rỗng nhưng có nhu cầu thực.
   - Vị trí: Action 3 "Chỉ lấy khi có REQ".
   - Gặp: các đặc tả P04 đều có tiền điều kiện nhân viên "đã được xác thực" (ASM-09 của P02), là chức năng dùng chung (phân quyền) nhưng không có REQ.
   - Xử lý: ghi Mục 2 "Không có", nêu ở Vấn đề còn mở. Không tạo Q vì ASM-09 đã có.

10. Mâu thuẫn BR với giả định, không phải giữa hai BR.
    - Vị trí: Action 8d "Phát hiện mâu thuẫn giữa hai BR: giữ cả hai, tạo Q-nn"; Action 8 "Không sửa nội dung quy tắc đã chốt; nội dung cần sửa thì ghi đề xuất".
    - Gặp: P04 UC-008 đề nghị P06 diễn đạt lại BR-02, BR-03 theo "vé còn hiệu lực" (vì ASM-20 cho bán lại chỗ đã trả). Đây là mâu thuẫn BR với ASM của P04, và chính P04 giao việc sửa cho P06, trong khi P06 bị cấm sửa nội dung BR.
    - Xử lý: giữ nguyên nội dung, ghi Ghi chú (Q-36) và Đề xuất sửa artifact trước cho P04 UC-002.

11. Quá tải ngữ cảnh: bốn đặc tả P04 đầy đủ (gồm bảng Node, Edge của activity diagram) là phần lớn đầu vào, trong khi P06 chỉ cần Mục 6, 7, 8, Câu hỏi mở, Giả định. Mục 3 của prompt bảo đính kèm "mọi đặc tả P04" mà không giới hạn mục như với P02. Đã bỏ qua phần activity diagram khi đọc.

## Target

Đạt: 1, 2, 3, 4, 5 (CO_NHAN, ngưỡng giả định có ASM), 6, 7, 8, 9, 10, 11, 12.
Ghi chú: Target 3 có thể bị coi là chưa đạt ở NFR-01 nếu tính tỉ lệ lỗi trong mức đạt là đại lượng thứ hai (vướng mắc 4). Target 7 về "không có hai BR cùng nghĩa cùng Hiệu lực": BR-02 và BR-03 có phần giao nhau (cùng REQ-67) nhưng khác loại (Ràng buộc và Suy luận), không coi là trùng nghĩa.
