# Nhật ký người chạy - P02R

Đề: bus (yeu-cau-xe-khach.md). Đầu vào: project-profile.md, P00-problem-brief.md 1.0, P01-actors.md 1.0, P02-usecases.md 1.0. Đầu ra: design/P02R-review.md. Không có sơ đồ .drawio (P02R không sinh sơ đồ).

Kết quả: 0 Nghiêm trọng, 1 Trung bình, 3 Thấp, kết luận "Đạt". 10 tác nhân và 18 use case đã xét; cấp mới Q-30, không cấp ASM.

## Vướng mắc

### 1. Target 8 không có chỗ ghi nhận tác nhân không có phát hiện

- Vị trí: [Target] câu 8 "Phần tử nào trong đối tượng review cũng đã được xét (có phát hiện hoặc được giữ nguyên trong Mục 4)."; Phần C Mục 4 chỉ có cột UC.
- Gặp gì: phạm vi có TAC_NHAN, 10 tác nhân đều không có phát hiện. Mục 4 là danh sách use case, không có bảng tác nhân sau sửa, nên tác nhân "giữ nguyên" không có chỗ nào để thể hiện.
- Xử lý: thêm một câu cuối Mục 1 liệt kê các tác nhân đã xét và giữ nguyên. Đề nghị: thêm "Mục 4b. Danh sách tác nhân đề xuất sau sửa (khi phạm vi có TAC_NHAN)" hoặc sửa Target 8 cho phép liệt kê ở Mục 1.

### 2. Cột Thay đổi ở Mục 4 thiếu giá trị cho sửa mục tiêu hoặc tác nhân

- Vị trí: Phần C Mục 4 "Thay đổi: Giữ / Đổi tên / Gộp từ <mã gốc> / Tách từ <mã gốc> / Mới / Loại".
- Gặp gì: UCR-01 đề xuất sửa mục tiêu và tác nhân chính của UC-003, sửa tác nhân phụ của UC-007, không đổi tên. Không giá trị nào trong danh sách khớp.
- Xử lý: ghi tự do "Đổi mục tiêu và tác nhân chính", "Đổi tác nhân phụ", kèm mã UCR. Đề nghị thêm giá trị "Sửa nội dung (mục tiêu / tác nhân)".

### 3. Mục 2 và Mục 5 "chỉ khi" mâu thuẫn với Conventions C5 "không xoá mục"

- Vị trí: Phần C "Mục 2. Bảng kiểm kê (chỉ khi đối tượng chưa có mã)" và "Mục 5. Quan hệ đề xuất sau sửa (khi phạm vi có SO_DO)"; Conventions C5 "Mục nào không có nội dung thì ghi 'Không có', không xoá mục."
- Gặp gì: đối tượng đã có mã ACT, UC và phạm vi không có SO_DO, nên cả hai mục không áp dụng. Không rõ nên bỏ hẳn (theo chữ "chỉ khi") hay giữ tiêu đề (theo C5).
- Xử lý: giữ tiêu đề, ghi "Không có" kèm lý do; ghi lựa chọn vào Vấn đề còn mở của artifact theo C9.

### 4. Phần B không gán mức mặc định cho nhiều mã tiêu chí

- Vị trí: Phần B, ba mức chỉ liệt kê một phần mã. Không có U-T1 đến U-T12, U-N1 đến U-N6, U-N8, U-R01 đến U-R18, A-T2, A-T4 đến A-T6.
- Gặp gì: UCR-02 đến UCR-04 vi phạm U-N3, U-N4, U-N6; UCR-01 vi phạm U-T11 kèm U-AP12. Phải suy mức theo câu mô tả chung ("thuật ngữ chưa nhất quán nhẹ", "trùng lặp").
- Xử lý: xếp theo mã có trong Phần B gần nhất (U-AP12 --> Trung bình; U-N lệch thuật ngữ --> Thấp), ghi cách xếp vào Vấn đề còn mở. Đề nghị thêm câu "Mã không liệt kê: xếp theo hệ quả, mặc định Thấp với U-N, Trung bình với U-T và U-R" hoặc bảng ánh xạ đầy đủ.

### 5. Điều kiện giữ Subfunction không có mã tiêu chí để dẫn

- Vị trí: Nhóm U, đoạn "Mức mục tiêu ... Subfunction ... Chỉ hợp lệ khi là phần dùng chung cho từ hai use case ..."; Phần C Mục 3 "Quy tắc vi phạm: một hoặc nhiều mã tiêu chí ở Phần A."
- Gặp gì: khi xét UC-003 Thanh toán vé trực tuyến (Subfunction) và quan hệ với UC-007, các điều kiện "dùng chung", "mục tiêu con có kết quả riêng" là căn cứ chính nhưng không có mã. Đã phải dẫn U-T11, U-AP12 thay thế.
- Xử lý: dẫn mã gần nhất; nêu điều kiện Subfunction bằng lời trong cột Vấn đề. Đề nghị gán mã (ví dụ U-L1 Summary, U-L2 Subfunction hợp lệ) để phát hiện về mức mục tiêu dẫn được mã.

### 6. Đầu vào dẫn mã quy tắc của prompt P02 mà P02R không có

- Vị trí: mục 1 của prompt "Prompt tự chứa đủ tiêu chí, không cần đọc P01, P02, P03."; U-R10 "(cùng nội dung với U-R10 của P02)".
- Gặp gì: P02-usecases.md dẫn "Q4 d" (UC-003, CAND-30), "Q1" (CAND-23, Vấn đề còn mở), "Bước 7.2" (CAND-35), "Bước 9.1", "U-R04 d" (CAND-18). Bộ tiêu chí P02R không có cây quyết định Q1 đến Q4 hay các bước này, U-R04 ở P02R không chia a, b, c, d. Người review không kiểm được lý do đó có đúng quy tắc gốc không, chỉ đối chiếu được với nội dung tóm tắt.
- Xử lý: đối chiếu "Q4 d" với điều kiện Subfunction "mục tiêu con có kết quả riêng kiểm chứng được" của P02R; đối chiếu "U-R04 d" với vế "khác sự kiện hoặc quyền" của U-R04. Không ra phát hiện về việc dẫn mã. Đề nghị P02R chép tóm tắt cây quyết định Q1 đến Q4 và chia vế U-R04 như P02, hoặc P02 không dẫn mã nội bộ vào artifact.

### 7. A-T3 và U-R18 cho kết luận khác nhau với đầu quét tích hợp trên máy cầm tay

- Vị trí: A-T3 "bàn phím, màn hình không phải tác nhân"; A-C "thiết bị là tác nhân phụ nếu nằm ngoài ranh giới và có giao tiếp riêng, chỉ là kênh nhập nếu thuộc ranh giới"; U-R18 "thiết bị ngoài ranh giới là tác nhân phụ".
- Gặp gì: ACT-09 Đầu quét mã vạch là bộ phận của máy soát vé cầm tay (phần cứng ngoài, phần mềm soát vé trong phạm vi theo ASM-01). Hệ thống không "nhờ" đầu quét làm việc gì (phép thử A-C4), người phụ xe bấm quét; về chức năng nó giống bàn phím của thiết bị (A-T3). Nhưng theo U-R18 nó nằm ngoài ranh giới phần mềm nên là tác nhân phụ. Tiêu chí không nói thiết bị nhập liệu tích hợp trên nền tảng chạy ứng dụng thuộc loại nào.
- Xử lý: không ra phát hiện vì P01 tuân thủ U-R18 và đã ghi ASM-06; nêu điều kiện ở Mục 6 của artifact. Đề nghị thêm một câu vào A-C: "Bộ phận nhập liệu tích hợp của thiết bị chạy phần mềm của hệ thống (bàn phím, màn hình cảm ứng, đầu quét gắn liền) là kênh nhập, không phải tác nhân".

### 8. U-R07 và U-AP03, U-T9 chưa phân xử trường hợp chuyển dữ liệu giữa hai phần nội bộ theo lịch

- Vị trí: U-R07 "Tác vụ theo lịch có giá trị nghiệp vụ, xảy ra khi không còn phiên nào đang mở, là use case với tác nhân thời gian"; U-AP03 "Chức năng phần mềm nội bộ"; U-T9 "Hành vi nhìn thấy từ bên ngoài, không phải xử lý nội bộ."
- Gặp gì: UC-014 gửi danh sách hành khách từ máy chủ về ứng dụng soát vé, cả hai đều trong phạm vi theo ASM-01. P02 tự ghi xung đột này ở Vấn đề còn mở. P02R không có tiêu chí nói "giá trị nghiệp vụ" của U-R07 có thắng "xử lý nội bộ" của U-T9 không.
- Xử lý: giữ UC-014 theo U-R07 (nguồn nêu mốc 15 phút và giá trị cho phụ xe), ghi phụ thuộc Q-01 ở Mục 6. Đề nghị bổ sung U-R07 một câu cho trường hợp đồng bộ dữ liệu giữa các thành phần của hệ thống mà nguồn nêu mốc thời gian.

### 9. Placeholder PHAM_VI_REVIEW nhận văn xuôi thay vì giá trị liệt kê

- Vị trí: mục 4, "{{PH:PHAM_VI_REVIEW | Hướng dẫn: chọn một hoặc nhiều trong: TAC_NHAN, DANH_SACH_UC, SO_DO."
- Gặp gì: giá trị được giao là "Tác nhân và danh sách use case. Không chấm sơ đồ vì P03 chưa chạy." Không phải mã liệt kê nhưng nghĩa rõ.
- Xử lý: quy về TAC_NHAN, DANH_SACH_UC. Không ảnh hưởng kết quả. Ghi lại vì một AI chặt chẽ theo C6 có thể dừng lại hỏi.

### 10. Mục "Đề xuất sửa artifact trước" lặp lại bảng phát hiện

- Vị trí: Phần C "Khi chạy trong pipeline (có 00-Conventions.md), thêm bảng thông tin và các mục kiểm soát theo Conventions C5 (Câu hỏi mở, Giả định khi CO_NHAN, Đề xuất sửa artifact trước, Vấn đề còn mở)".
- Gặp gì: mọi UCR đều là đề xuất sửa P02, nên mục "Đề xuất sửa artifact trước" hoặc chép lại Mục 3, hoặc bỏ trống. Prompt không nói quan hệ giữa hai mục; mục 5 "Ghi chú cho người dùng" cho cách áp dụng UCR qua chạy lại P02, không qua mục này.
- Xử lý: mỗi dòng chỉ trỏ mã UCR và cách áp dụng (chạy lại P02 kèm UCR trong YEU_CAU_BO_SUNG), không chép nội dung. Đề nghị prompt nói rõ: "Đề xuất sửa artifact trước chỉ ghi điều không thuộc đối tượng review (ví dụ P00, P01 khi phạm vi chỉ có DANH_SACH_UC); phát hiện về đối tượng review chỉ nằm ở Mục 3".

### 11. Bước 1.2 chỉ nói dùng mã RL-nn, không nói mã ACT-nn, UC-nnn

- Vị trí: Bước 1.2 "Nếu đối tượng đã có mã RL-nn theo Conventions thì dùng RL-nn."
- Gặp gì: đối tượng có ACT-nn, UC-nnn, không có RL-nn. Câu chỉ nhắc RL nên chưa nói rõ có dùng mã gốc của tác nhân và use case không; Mục 4 có nói giữ mã UC-nnn, Mục 2 nói "chỉ khi chưa có mã".
- Xử lý: dùng ACT-nn, UC-nnn gốc. Đề nghị viết "Nếu đối tượng đã có mã theo Conventions (ACT-nn, UC-nnn, RL-nn) thì dùng mã đó".

### 12. "Câu hỏi cần người viết trả lời" khi người viết là pipeline

- Vị trí: Phần C "Câu hỏi cần người viết trả lời ở Mục 6 được cấp mã Q-nn theo Conventions C3".
- Gặp gì: Q-30 (cách giao vé mới khi đổi vé) là câu hỏi cho chủ tài liệu nguồn, không phải cho P02. Chữ "người viết" lẫn hai đối tượng.
- Xử lý: cấp Q-30 vào mục Câu hỏi mở theo dạng câu hỏi nguồn của C3. Không ảnh hưởng.

### 13. Khối lượng đầu vào

- Vị trí: mục 3 "Khi chạy trong pipeline, đính kèm thêm 00-Conventions.md, project-profile.md, P01-actors.md, P02-usecases.md".
- Gặp gì: tổng đầu vào khoảng 160 KB (P00 khoảng 48 KB, P02 khoảng 49 KB, prompt khoảng 33 KB, Conventions và README khoảng 30 KB). Với agent đọc file thì chịu được; khi chạy bằng chat có thể sát giới hạn. Prompt không nói phần nào của P00 là đủ (thực tế chỉ cần bảng REQ, Câu hỏi mở và Giả định để cấp tiếp mã Q, ASM).
- Xử lý: đọc đủ. Đề nghị mục 3 ghi "từ P00 chỉ cần Mục 4 Danh sách yêu cầu, Câu hỏi mở, Giả định".

## Target

Cả 8 mục Target đạt. Target 8 đạt nhờ cách xử lý ở vướng mắc 1 (liệt kê tác nhân ở Mục 1), không theo đúng câu chữ "giữ nguyên trong Mục 4".
