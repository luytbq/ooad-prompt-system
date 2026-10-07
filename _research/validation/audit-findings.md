# Audit tĩnh bộ prompt - kết quả từng phần

Trạng thái: HOÀN TẤT. Mục 1 đến 4 là phần rà đầu (AF-01 đến AF-12, đã sửa); mục 5 là phần rà tiếp (AF-13 đến AF-37) và kết quả xác minh Lilly.

## 1. Bảng phát hiện

| ID | File | Vị trí (mục, câu trích) | Loại (1-9) | Mô tả | Đề xuất sửa cụ thể | Mức độ |
|---|---|---|---|---|---|---|
| AF-01 | 00-ProjectProfile-Template.md | Mục 2, CHE_DO_GIA_DINH: "(hợp với bài tập, hồ sơ thầu, hợp đồng)" | 7 | Chứa từ bị cấm "bài tập" trong file sản phẩm | Thay bằng "(hợp với đề bài cố định, hồ sơ thầu, hợp đồng)" | Cao |
| AF-02 | 00-Conventions.md C3 và P00 | C3: "SH-nn - Bên liên quan - P00"; P00 F4: "Bảng: \| STT \| Bên liên quan \| ..." | 2 | C3 quy định P00 cấp mã SH-nn nhưng P00 dùng cột STT, không cấp SH. P01 Mục 3 cũng không trỏ SH | P00 F4: đổi cột "STT" thành "SH" với câu "SH: mã SH-nn theo Conventions C3, không đổi khi chạy lại". P01 Mục 3 thêm cột "SH" đầu bảng: "\| SH \| Bên liên quan \| ...", ghi "Mã SH lấy từ P00" | Cao |
| AF-03 | P02 Mục 2 và C3 | P02: "Mã EV-nn là mã cục bộ trong artifact này." C3: "EV-nn \| Sự kiện kích hoạt \| P02" | 2, 6 | C3 coi EV là mã toàn hệ thống (bước sau trỏ tới được), P02 nói là mã cục bộ; P04 chép cột Sự kiện kích hoạt kèm mã EV | Sửa P02: "Mã EV-nn theo Conventions C3; mã không đổi khi chạy lại, các bước sau (P04) dẫn mã này." | Trung |
| AF-04 | P01 | Bước 6: "P04 dùng danh sách này để viết mục bên liên quan và lợi ích." | 1, 3 | P04 không có mục bên liên quan và lợi ích (cạnh gãy) | Hoặc bỏ câu, hoặc thay bằng "P04 dùng danh sách này khi viết hậu điều kiện liên quan tới bên hưởng lợi; P05 dùng để kiểm tra thuật ngữ vai trò." | Trung |
| AF-05 | P02 và P04 | P02 cột Tác nhân chính: "nhiều tác nhân ngăn bằng dấu phẩy khi áp dụng U-R10 hoặc U-R11"; P04 F1: "\| Tác nhân chính \| ACT-nn Tên \|", F10.4: "tác nhân chính" số ít | 6 | P04 không xử lý UC có nhiều tác nhân chính: không rõ cột Thực hiện bởi ghi ai, bao nhiêu partition | Thêm vào P04 F1: "Nhiều tác nhân chính (theo P02) thì liệt kê tất cả." Thêm F4.2: "UC có nhiều tác nhân chính: cột Thực hiện bởi ghi tác nhân cha nếu P01 có tổng quát hoá, ngược lại ghi tên tác nhân chính đầu tiên và nêu trong Thông tin bổ sung rằng các tác nhân còn lại thực hiện cùng luồng; khác biệt thành luồng thay thế." F10.4: "một partition cho nhóm tác nhân chính, nhãn là các tên nối bằng ' / '." | Trung |
| AF-06 | P02 và P04 | P02: UC Subfunction dùng chung có thể có Tác nhân chính "-", ghi "Được gọi từ UC-xxx"; P04 F4.2 quy tắc 10: "Bước đầu tiên là sự kiện kích hoạt (thường là tác nhân chính yêu cầu...)" | 1, 6 | P04 chưa có quy tắc cho UC được include không có tác nhân chính: bước 1, partition, tiền điều kiện | Thêm P04 F4.2 quy tắc 11: "UC được include (Tác nhân chính '-' ở P02): bước 1 là 'Hệ thống bắt đầu <mục tiêu> khi được gọi từ UC-xxx'; tiền điều kiện là trạng thái tại điểm gọi; bước cuối 'Trả kết quả <thành công/thất bại> cho use case gọi'. Activity diagram đặt INIT trong partition hệ thống." | Trung |
| AF-07 | P02 và P04 | P02 U-T4, Phần E: "khoảng 3-15 bước (dễ đọc nhất khoảng 3-9 bước)"; P04 F4.4: "thường 4-12 bước. Dưới 3... Trên 15..." | 5, 6 | Hai ngưỡng khác cách diễn đạt cho cùng khái niệm, dễ gây hiểu là hai quy tắc | P04 F4.4 sửa thành "Số bước: khoảng 3-15 bước, dễ đọc nhất khoảng 3-9 (bảng tách bước tác nhân và bước hệ thống nên thường dài hơn, 4-12 là phổ biến)." | Thấp |
| AF-08 | 00-Conventions.md C7.3 và P04 F10.6 | C7.3: "Control flow (activity) \| endArrow=open;html=1;edgeStyle=orthogonalEdgeStyle;"; P04: "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=open;endFill=0;". Swimlane C7.3 "swimlane;html=1;" với P04 "swimlane;html=1;startSize=40;" | 6 | Hai style cho cùng phần tử | P04 F10.6 thay bằng "control flow theo Conventions C7.3; partition theo C7.3 dạng 'swimlane;html=1;', thêm startSize=40". Hoặc cập nhật C7.3 cho khớp P04 | Thấp |
| AF-09 | P02 | Căn cứ: "Craig Larman ... (EBP, Boss test, Size test, EBP test, ...)" | 8 | Lặp "EBP" hai lần | Thay bằng "(EBP test, Boss test, Size test, tìm use case từ mục tiêu tác nhân và phân tích sự kiện, gộp CRUD thành Manage X)" | Thấp |
| AF-10 | P01, P02 | Căn cứ Lilly, TOOLS 30, 1999 | 8 | Theo trí nhớ, danh sách 10 vấn đề của Lilly gồm: ranh giới hệ thống không rõ; use case viết từ góc nhìn hệ thống; tên tác nhân không nhất quán; quá nhiều use case; quan hệ tác nhân và use case rối như mạng nhện; đặc tả quá dài; đặc tả khó hiểu; không mô tả đúng quyền chức năng; khách hàng không hiểu; không bao giờ xong. Nội dung trích ở P01, P02 khớp mục 1-4. Chưa xác minh trực tuyến | Nếu không xác minh được, diễn đạt an toàn: "Susan Lilly, Use Case Pitfalls: Top 10 Problems from Real Projects Using Use Cases, Proceedings of TOOLS 30, IEEE, 1999 (danh mục lỗi thường gặp khi dùng use case trong dự án thực tế)." | Thấp |
| AF-11 | P04 | F1 hàng "Hậu điều kiện (thành công)", "Hậu điều kiện tối thiểu" thay hàng "Hậu điều kiện" của hợp đồng | 1 | Cần xác nhận P07 đọc đúng tên hàng (P07 chưa rà) | Khi rà P07: nếu P07 nhắc "Hậu điều kiện" thì sửa thành "Hậu điều kiện (thành công)" | Trung (chờ xác minh) |
| AF-12 | P04 | F4.2 có quy tắc đánh số "2b." chen giữa 2 và 3 | 4 | Đánh số lạ, dễ bị hiểu là luồng thay thế 2b | Đổi "2b." thành quy tắc 11 ở cuối danh sách | Thấp |

## 2. Ma trận phụ thuộc (phần đã rà)

| Cạnh | File đầu vào yêu cầu | Tên theo C4 | Bảng/cột đọc | Trạng thái |
|---|---|---|---|---|
| P00 --> P01 | P00-problem-brief.md | Khớp | Bảng REQ, Phạm vi, Bên liên quan | Gãy một phần: mã SH không tồn tại (AF-02) |
| P00 --> P02 | P00-problem-brief.md | Khớp | Bảng REQ, Ngoài phạm vi | Khớp |
| P01 --> P02 | P01-actors.md | Khớp | Bảng tác nhân (Loại, Tính chất, Mục tiêu) | Khớp |
| P01 --> P04 | P01-actors.md | Khớp | Tên tác nhân, loại Thời gian | Khớp; P01 Bước 6 trỏ mục không tồn tại ở P04 (AF-04) |
| P02 --> P04 | P02-usecases.md | Khớp | Tên, tác nhân chính/phụ, mục tiêu, mô tả, sự kiện kích hoạt, REQ | Gãy một phần: nhiều tác nhân chính, UC không có tác nhân chính (AF-05, AF-06); mã EV (AF-03) |
| P03 --> P04 | P03-usecase-model.md | Khớp | Quan hệ, điều kiện extend, điểm mở rộng | Chưa kiểm (P03 chưa rà) |
| P04 --> P05 | P04-uc-specs/*.md, _BR-register.md | Khớp | Luồng, dữ liệu, BR | Khớp |
| P04 --> P06 | P04-uc-specs/*.md, _BR-register.md | Khớp | Yêu cầu đặc biệt, bảng BR, sổ BR | Khớp |
| P04 --> P07 | P04-uc-specs/*.md | Khớp | Chưa kiểm | Chưa kiểm (AF-11) |
| P06 --> P09, P11b, P12, P13, X2 | P06-supplementary-spec.md | Khớp | NFR, BR | Chưa kiểm |
| Các cạnh P07 trở đi | | | | Chưa kiểm |

## 3. Kiểm tra định dạng và từ cấm (phần đã rà)

- Từ cấm: chỉ phát hiện AF-01 trong các file đã rà. Chưa grep toàn bộ file còn lại.
- Em dash, mũi tên Unicode, backtick đơn: P00, P04, P05, P06 sạch (đã grep). Các file khác chưa grep.

## 4. Việc còn lại

1. Rà P02R, P03, P07 đến P13, X1, X2, README theo 9 tiêu chí.
2. Grep từ cấm và định dạng trên toàn bộ file sản phẩm.
3. Xác minh trích dẫn Lilly bằng WebSearch.
4. Hoàn thiện ma trận phụ thuộc cho P07 trở đi.

## 5. Phần rà tiếp

Phạm vi: README.md (bản mới), P02R, P03, P07, P08, P09, P10, P11a, P11b, P12, P13, X1, X2; đối chiếu thêm P02, P04, P06, 00-Conventions.md, 00-ProjectProfile-Template.md. Rà tĩnh, không chạy prompt. Không sửa file sản phẩm.

Tổng hợp: Cao 0, Trung 5 (AF-13 đến AF-17), Thấp 20 (AF-18 đến AF-37). Cập nhật trạng thái hai phát hiện cũ ở mục 5.4.

### 5.1. Bảng phát hiện

| ID | File | Vị trí (mục, câu trích) | Loại (1-9) | Mô tả | Đề xuất sửa cụ thể | Mức độ |
|---|---|---|---|---|---|---|
| AF-13 | P12, X1, P11b | P12 [Format] Quy ước chung: "Interface cũng dùng DC-, ví dụ DC-ISmsGateway"; P12 F5 ví dụ R-12: "DC-SmsGatewayAdapter \| DC-ISmsGateway \| Realization \| ... Adapter hiện thực IF-02"; X1 F2 ví dụ RV-07 "DC-ISmsGateway (IF-02)"; P11b F3 ví dụ "IF-02 \| ISmsNotifier" | 2, 5 | Một interface mang hai mã (IF-nn do P10, P11b cấp và DC-I... do P12 cấp), trái C3 "mã không tái sử dụng, mỗi phần tử một mã". Ví dụ cùng miền phòng khám gọi IF-02 là ISmsNotifier ở P11b nhưng ISmsGateway ở P12, X1. P13 và X1 CNS ("mọi IF trong P11b có lớp «interface»") không biết dùng mã nào | Chọn một: interface giữ mã IF-nn ở mọi bước. P12 Quy ước chung sửa thành "Interface giữ mã IF-nn đã cấp ở P10, P11b, không cấp mã DC; bảng F1 ghi IF-nn ở cột DC, Loại 'interface'". Sửa ví dụ R-12 thành "DC-SmsGatewayAdapter \| IF-02 \| Realization"; X1 RV-07 thành "phụ thuộc IF-02 ISmsNotifier"; thống nhất tên ISmsNotifier trong mọi ví dụ | Trung (Đã sửa) |
| AF-14 | P03 | Phần B Mục 5: "ID: mã ACT-nn, UC-nnn; boundary là SYS; package là PKG-<slug>" | 2 | Tiền tố PKG- đã được C3 dành cho package/layer thiết kế (PKG-nn, P09, P10). Node package trên sơ đồ use case (nhóm chức năng) dùng cùng tiền tố với nghĩa khác, dễ bị P09 hoặc người đọc coi là package kiến trúc | Đổi thành "package nhóm chức năng là GRP-<slug>" (hoặc "UCPKG-<slug>") và ghi chú "không phải mã PKG của C3". Sửa tương ứng cột Thuộc về "GRP-... nếu có package" | Trung (Đã sửa) |
| AF-15 | P02R | Bước 1.2: "Gán mã tạm ... (A1, A2... cho tác nhân; U1, U2... cho use case; R1, R2... cho quan hệ)"; Bước 2: "đánh số N1, N2..."; ví dụ đề xuất "Đảo chiều R5: từ U7 tới U2" | 2 | Mã tạm R1 cho quan hệ trên biểu đồ use case trùng tiền tố với R-nn (quan hệ lớp), trong khi C3 dành RL-nn cho quan hệ biểu đồ UC. N1 (yêu cầu) trùng dạng với N-nn (note) của P03 | Bước 1.2 đổi "R1, R2..." thành "L1, L2..." (hoặc "RL-t1") và ghi "nếu đối tượng đã có mã RL-nn theo Conventions thì dùng RL-nn". Bước 2 đổi "N1, N2" thành "YC1, YC2". Sửa ví dụ trong Phần C Mục 3 cho khớp | Trung (Đã sửa) |
| AF-16 | P02R | Phần C: "Xuất file P02R-review.md (hoặc trả trong chat) gồm các mục theo thứ tự: Mục 1 ... Mục 6. Giới hạn của review" | 4 | P02R-review.md có trong C4 nhưng đặc tả đầu ra không theo khung C5 (thiếu bảng thông tin đầu file, Câu hỏi mở, Giả định, Đề xuất sửa artifact trước, Vấn đề còn mở). Mọi prompt khác đều ghi "theo khung C5" | Thêm vào đầu Phần C: "Khi chạy trong pipeline (có 00-Conventions.md), artifact theo khung C5: bảng thông tin ở đầu, Mục 6 Giới hạn của review đặt trước các mục kiểm soát của C5. Khi chạy độc lập, bỏ bảng thông tin và mục kiểm soát." | Trung (Đã sửa) |
| AF-17 | README.md | Mục 5, bảng phụ thuộc: "P05, P06 \| P09 (nếu NFR đổi), P12, P13, X2"; "P03 \| P04 ..., P07 của UC đó"; "P13 \| X1" | 1 | Bảng chạy lại thiếu cạnh có thật theo mục 2 của các prompt: P07, P08, P11a (bắt buộc đọc P05, P06), P10, P11b (bắt buộc đọc P06) không được rà khi sửa P05, P06; P09, P10 đọc P03 (quan hệ extend để tách tuỳ chọn) nhưng không có trong dòng P03; X2 đọc P13 nhưng dòng P13 chỉ có X1 | Sửa ba dòng: "P05, P06 \| P07 của UC dùng thuật ngữ, BR, NFR đã đổi, P08 trở đi (P09 nếu NFR đổi)"; "P03 \| P04 và P07 của UC có quan hệ thay đổi, P09, P10"; "P13 \| X1, X2" | Trung (Đã sửa) |
| AF-18 | P02R, P03 | P02R Nhóm L: "L-01 Tác nhân chính bên trái ... L-05 Không dùng màu"; P03 Phần D: "L-01 Boundary: góc trên trái tại (200, 40) ... L-11 Không dùng màu"; P03 Phần A: "Bảng lỗi sơ đồ (... P02R dùng cùng mã)" | 2 | Cùng mã L-nn nhưng nghĩa khác nhau giữa hai prompt (P02R L-03 là vị trí include và extend, P03 L-03 là vị trí tác nhân phụ). Review P03 bằng P02R dễ dẫn chiếu sai mã | Đổi mã bố cục của P02R thành LR-01 đến LR-05, hoặc ánh xạ về mã P03 (P02R L-01 = P03 L-02, L-03; L-02 = P03 L-05; L-03 = P03 L-06, L-07, L-08; L-04 = P03 L-10; L-05 = P03 L-11) và ghi "dùng cùng mã với P03 Phần D" | Thấp (Đã sửa) |
| AF-19 | Profile, P09, P11a, P12, P13, X1, X2, P03, P07, P08, P10, P11b, P02R | Profile MUC_CHI_TIET: "GON: bỏ các mục đánh dấu 'chỉ khi DAY_DU'"; các prompt viết "Chỉ khi DAY_DU", "chỉ khi MUC_CHI_TIET là DAY_DU", "khi DAY_DU", "Khi MUC_CHI_TIET là DAY_DU", "bắt buộc khi DAY_DU; khi GON chỉ cho ..."; P07 mục 2: "project-profile.md \| ... mức chi tiết" nhưng không có quy tắc nào dùng | 5, 6 | Năm cách diễn đạt cho cùng cơ chế; nhãn trong profile ("chỉ khi DAY_DU") chỉ khớp nguyên văn ở P09 mục 2. P03, P07, P08, P10, P11b, P02R không có mục nào thay đổi theo GON; P07 khai báo đọc mức chi tiết mà không dùng | Chuẩn hoá một nhãn "(chỉ khi DAY_DU)" đặt ngay sau tên mục ở mọi prompt; profile giữ nguyên câu. P07 bỏ "mức chi tiết" khỏi cột Dùng để, hoặc thêm quy tắc GON (ví dụ "(chỉ khi DAY_DU) communication diagram cho luồng thay thế đã gộp") | Thấp (Đã sửa) |
| AF-20 | 00-Conventions C7.3, P03, P02R | C7.3: "biến thể có mũi tên chỉ bên khởi xướng"; P03 mục 3: "Có vẽ đầu mũi tên chỉ bên khởi xướng"; P03 placeholder và Phần A: "đầu mũi tên mở chỉ về phía bên nhận"; P02R: "mũi tên mở chỉ bên nhận"; tên giá trị MUI_TEN_KHOI_XUONG | 5 | Cùng một ký hiệu được mô tả bằng hai cụm ngược nghĩa bề mặt ("chỉ bên khởi xướng" và "chỉ về phía bên nhận"); người đọc có thể vẽ ngược chiều | Thống nhất một câu ở C7.3, P03, P02R: "đuôi ở bên khởi xướng, đầu mũi tên mở ở bên nhận (tác nhân chính --> use case; use case --> tác nhân phụ)". Giữ tên giá trị MUI_TEN_KHOI_XUONG nhưng thêm câu này vào Hướng dẫn | Thấp (Đã sửa) |
| AF-21 | P11a | F5 e) ví dụ đúng: "... \| P04 UC-007 mục 4, BR-08 \|" | 3 | Trong đặc tả P04, dữ liệu vào ra là mục 5 ("## 5. Dữ liệu vào và dữ liệu ra"); mục 4 là Luồng con | Sửa thành "P04 UC-007 mục 5 Dữ liệu vào 1 STT 1, BR-08" | Thấp (Đã sửa) |
| AF-22 | P11b | F4: "Bố cục theo P07 mục sequence (lifeline cách 160, message cách 40...)" | 3 | Không có "mục sequence" trong P07; quy tắc bố cục sequence nằm ở P07 F10 | Sửa thành "Bố cục theo P07 F10 (phần Sequence)" | Thấp (Đã sửa) |
| AF-23 | 00-Conventions C3, P11b | C3: "DC-xxx \| Lớp thiết kế \| P10, P12"; P11b F5 a): "Mã DC cấp theo C3" cho phần tử bên trong subsystem | 2 | P11b cấp mã DC nhưng C3 không ghi P11b là bước tạo; P12 Bước 0 (c) đã dựa vào mã DC do P11b cấp | Sửa C3 cột Bước tạo của DC-xxx thành "P10, P11b, P12" | Thấp (Đã sửa) |
| AF-24 | P11a | A1: "mã MSG-nn cục bộ trong P11a" | 2 | Cùng dạng AF-03: C3 coi MSG-nn là mã hệ thống, P11a gọi là cục bộ; P12 lớp boundary và X2 có thể cần dẫn MSG | Sửa thành "mã MSG-nn theo C3, không đổi khi chạy lại" | Thấp (Đã sửa) |
| AF-25 | P07, P08, P12, P13 | P07 F8 b): "Multiplicity (A..B)"; P08 F4: "A: 1, B: 0..*"; P12 F5: "A 1 - B 0..*"; P13 F4.2 ví dụ: "Reservation 0..* - 1 Room" | 5 | Bốn cách ghi multiplicity cho cùng khái niệm dọc một chuỗi mà P12 giữ mã R-nn của P08 và P13 đọc R-nn của P12. Dễ đọc nhầm đầu | Chọn cách của P12 ("A <m> - B <m>") làm chuẩn, sửa P07 F8 b) và P08 F4 dùng cùng cách; ví dụ P13 viết "Reservation 0..* - Room 1" | Thấp (Đã sửa) |
| AF-26 | P02R, X1, X2 | P02R Phần B: "Nghiêm trọng / Trung bình / Nhỏ"; X1 F2: "Nghiêm trọng / Cao / Trung bình / Thấp"; X2 F1: Ưu tiên "Cao / Trung bình / Thấp" | 5 | Hai thang mức độ phát hiện khác nhau cho hai bước review cùng pipeline; "Nhỏ" và "Thấp" cùng nghĩa khác tên | Giữ số mức khác nhau nếu muốn, nhưng thống nhất tên mức thấp nhất là "Thấp" ở P02R; nêu trong README rằng P02R dùng 3 mức, X1 dùng 4 mức | Thấp (Đã sửa) |
| AF-27 | P12 | F1 ví dụ đúng: "DC-StockIssueController \| StockIssueController \| «control» \| ... \| AC-C-IssueStockController"; Bước 1.5a: "lớp control phân tích thành lớp dịch vụ ứng dụng (BorrowBookService, IssueStockService)" | 6 | Ví dụ đổi tên lớp khi ánh xạ 1-1 mà không ghi lý do, trái P10 A2 ("giữ tên lớp phân tích khi ánh xạ 1-1") và trái chính 1.5a (gợi ý IssueStockService) | Sửa ví dụ F1 thành "DC-IssueStockController \| IssueStockController \| ... \| AC-C-IssueStockController" (kiến trúc không MVC) và sửa F3, X2 ví dụ dùng cùng tên | Thấp (Đã sửa) |
| AF-28 | X1 | Bước 1: "lỗi một module không lan (isolation)"; Căn cứ: "Meyer B. ...: tiêu chí module (decomposability, composability, understandability, continuity, protection)" | 5, 8 | Tiêu chí thứ năm của Meyer là protection; Action gọi là isolation | Sửa Bước 1 thành "(protection)" | Thấp (Đã sửa) |
| AF-29 | X2 | F3: "\| TC \| DC.phương thức \|"; F1: "\| DC.operation \|"; mục 1 "phương thức quan trọng" | 5 | P12 phân biệt operation (chữ ký) và method (hiện thực); X2 dùng "phương thức" cho cả hai và đổi tên cột giữa F1 và F3 | Dùng "DC.operation" ở mọi cột; giữ "phương thức" chỉ trong văn xuôi hoặc thay bằng "operation" | Thấp (Đã sửa) |
| AF-30 | X2, 00-Conventions C7.3 | X2 F2.x.6: "khối lệnh dùng rounded=0 ...; cạnh endArrow=block;endFill=1;html=1;" | 6 | C7.3 không có dòng style cho CFG; X2 dùng style riêng khác Control flow (activity) của C7.3 (endArrow=open) | Thêm dòng "Đồ thị luồng điều khiển (X2)" vào bảng style C7.3 với đúng style X2 đang dùng, hoặc cho X2 dùng style Action và Control flow của C7.3 | Thấp (Đã sửa) |
| AF-31 | P13, X1, X2, P04 | P13 F8.2: "thuộc tính (A-<E>-<ten>)"; P04 F10.2: action "A-N"; X2: "cạnh E<n>", "DT<k>-R<n>"; X1 nhóm tiêu chí "PKG" và mã tạm "EXT-" | 2 | Mã cục bộ trùng tiền tố với mã C3 hoặc mã của bước khác: A- (action P04 và thuộc tính Chen P13), E<n> gần E-<Ten>, R<n> gần R-nn, nhóm "PKG" trùng tiền tố PKG-nn. Rủi ro nhầm thấp vì khác định dạng nhưng vi phạm tiêu chí không trùng tiền tố | P13 đổi ID thuộc tính Chen thành "AT-<E>-<ten>"; X2 đổi cạnh CFG thành "CE<n>", quy tắc bảng quyết định thành "DT<k>-Q<n>"; X1 đổi mã nhóm "PKG" thành "PKP" (nguyên lý package) | Thấp (Đã sửa) |
| AF-32 | P03 | Phần B Mục 4 ví dụ: "diagrams/P03-usecase-dat-lich.drawio"; "slug viết thường không dấu" | 6 | C4 định nghĩa slug là tên tiếng Anh viết thường; ví dụ P03 dùng slug tiếng Việt không dấu | Sửa ví dụ thành "P03-usecase-booking.drawio" và câu quy tắc thành "slug theo Conventions C4" | Thấp (Đã sửa) |
| AF-33 | X2 | F3 ví dụ: thứ tự dòng "TC-001, TC-002, TC-004, TC-003" | 4 | Ví dụ đúng lại đánh mã không tuần tự, trái quy tắc cấp mã tuần tự | Đổi thứ tự dòng thành TC-001 (0), TC-002 (1), TC-003 (50), TC-004 (51) và sửa tên trong khung JUnit cho khớp | Thấp (Đã sửa) |
| AF-34 | P07 đến P13, X1, X2, P03, P12 | [Target] câu "Không có dấu gạch ngang dài, ký hiệu mũi tên Unicode" lặp ở P07, P08, P09, P10, P11a, P11b, P12, P13, X1, X2; Bước 0 của P12, P13, X1, X2 chép lại quy tắc C6 về placeholder chưa điền; P03 Phần E chép lại danh sách style C7.3; P12 F9 chép gần nguyên văn tiêu chí nhóm package của P10 A3 | 9 | Chép lại Conventions và bước trước, trái câu đầu 00-Conventions ("phần chung ... không được chép lại"); P12 F9 chép lại tiêu chí nhóm package trong khi P12 không được tạo PKG mới, gây hiểu là P12 được nhóm lại | Bỏ các câu lặp C2, C6 (hoặc thay bằng "Đạt C2, C5, C6"); P03 Phần E chỉ giữ phần bổ sung (fontStyle=2, note nối edge); P12 F9 thay đoạn tiêu chí bằng "Kiểm tra gán package theo P10 A3; vi phạm ghi đề xuất sửa P10" | Thấp (Đã sửa) |
| AF-35 | P11a, X1, X2 | Placeholder MAU_DAC_TA_MAN_HINH, XUAT_HTML (P11a), MA_RV_BAT_DAU (X1), MA_TC_BAT_DAU (X2) chỉ có một ví dụ | 4 | Authoring-guide yêu cầu ví dụ từ ít nhất hai miền. Với placeholder dạng giá trị (Có/Không, mã bắt đầu) yêu cầu này không có ý nghĩa, riêng MAU_DAC_TA_MAN_HINH nên có hai ví dụ | MAU_DAC_TA_MAN_HINH thêm ví dụ thứ hai (ví dụ "Mẫu 5 cột của phòng QA: Mã, Tên, Mô tả, Quy tắc, Ghi chú"); ghi ngoại lệ trong authoring-guide cho placeholder dạng giá trị | Thấp (Đã sửa) |
| AF-36 | P11a | Căn cứ: "Japan Information Processing Development Corporation, Japan Information-Technology Engineers Examination Center, Textbook for Software Design and Development Engineers, No. 3 ..." | 7, 8 | Không chứa từ cấm, là tài liệu đã xuất bản, nhưng là giáo trình gốc của chương trình đào tạo ITSS mà authoring-guide mục 1 muốn tránh nhắc tới. Cần người quyết định có giữ không | Nếu muốn trung lập tuyệt đối: thay bằng Galitz (đã có) cho phần đặc tả màn hình và ghi nguồn bốn mẫu dịch chuyển vào _research | Thấp (cần xác nhận) (Đã sửa) |
| AF-37 | P07, P04 | P04 F4.2 quy tắc 13: use case được include có Tác nhân chính "-"; P07 A1 "Liệt kê tác nhân chính", A3 "Với mỗi cặp (tác nhân, use case) tìm một lớp boundary", Target 3; chỉ F5 ghi "Use case được include: phân tích như một use case bình thường với tác nhân là tác nhân của use case gọi" | 1, 6 | Quy tắc cho use case được include nằm ở cuối F5 (sequence), không ở A1, A3 nơi xác định tác nhân và boundary; AI có thể bỏ sót boundary hoặc tạo boundary trùng với use case gọi | Thêm vào A1: "Use case có Tác nhân chính '-' (được include): lấy tác nhân từ use case gọi trong P03; boundary giao diện người dùng của phần hành vi này thuộc use case được include" | Thấp (Đã sửa) |

### 5.2. Ma trận phụ thuộc bổ sung

Các cạnh còn thiếu ở mục 2. Cột "Tên theo C4" so tên file prompt sau yêu cầu với tên đầu ra prompt trước và C4.

| Cạnh | File đầu vào yêu cầu | Tên theo C4 | Bảng/cột đọc | Trạng thái |
|---|---|---|---|---|
| P03 --> P04 | P03-usecase-model.md | Khớp | Mục 1 Bảng quan hệ (Loại, Điều kiện extend / điểm mở rộng); Mục 2 Điểm mở rộng (Vị trí trong luồng, Điều kiện) | Khớp. Ngữ nghĩa include, extend, generalization, Đăng nhập (tiền điều kiện, không include) nhất quán giữa P02R, P03, P04 |
| P04 --> P07 | P04-uc-specs/UC-nnn-slug.md | Khớp | Luồng chính, luồng thay thế (STT 1, 3a, 3a1), mục 5 Dữ liệu vào ra, mục 6 BR, activity | Khớp. P07 không đọc hàng "Hậu điều kiện" nên AF-11 không còn. Use case được include không có tác nhân chính: xem AF-37 |
| P03 --> P07 | P03-usecase-model.md | Khớp | Include, extend, điểm mở rộng, điều kiện | Khớp |
| P01, P05, P06 --> P07 | P01-actors.md, P05-glossary.md, P06-supplementary-spec.md | Khớp | Loại tác nhân (Người / Hệ thống ngoài / Thiết bị / Thời gian); GL; BR, NFR | Khớp |
| P07 --> P08 | P07-uc-analysis/*.md | Khớp | F3.4 Bảng lớp phân tích; F8 b) bảng quan hệ VOPC (R-UCnnn-nn) | Khớp; định dạng multiplicity lệch (AF-25) |
| P02 --> P08, P09, P10 | P02-usecases.md | Khớp | Danh sách UC, cột Nhóm chức năng | Khớp |
| P08 --> P09 | P08-analysis-model.md | Khớp | F3 lớp hoạt động, Stereotype, Loại boundary | Khớp |
| P08 --> P10 | P08-analysis-model.md | Khớp | F3 (AC, Trạng thái Hoạt động, Trách nhiệm), F4 quan hệ R-nn | Khớp |
| P09 --> P10 | P09-architecture.md | Khớp | F4 PKG (cấp tiếp mã), F5 ánh xạ stereotype, F6 quy tắc phụ thuộc | Khớp |
| P06 --> P09 | P06-supplementary-spec.md | Khớp | NFR, ràng buộc | Khớp; P06 không xếp hạng NFR, P09 bù bằng TIEU_CHI_UU_TIEN |
| P03 --> P09, P10 | P03-usecase-model.md | Khớp | Quan hệ extend (tách tuỳ chọn và bắt buộc) | Khớp; README không liệt kê (AF-17) |
| P07, P08, P10, P04 --> P11a | P07-uc-analysis/, P08, P10, P04-uc-specs/ | Khớp | Message actor - boundary; boundary người dùng; DC của boundary; cột Điều kiện hợp lệ của bảng dữ liệu vào ra | Khớp; ví dụ trỏ sai mục P04 (AF-21) |
| P10 --> P11b | P10-design-elements.md | Khớp | F2 bảng subsystem (SS, IF, Trách nhiệm, Che giấu, AC nguồn, ACT, PKG) | Khớp |
| P07, P04 --> P11b | P07-uc-analysis/, P04-uc-specs/ | Khớp | Message control - boundary hệ thống; luồng lỗi | Khớp; tham chiếu bố cục sai tên mục (AF-22) |
| P10 --> P12 | P10-design-elements.md | Khớp | F3 ánh xạ (cột PKG), bảng phần tử mới do cơ chế kiến trúc | Khớp |
| P09 --> P12 | P09-architecture.md | Khớp | F3, F4, F5, F6 | Khớp |
| P11b --> P12 | P11b-system-interfaces.md | Khớp | F3 operation, F5 phần tử DC | Gãy một phần: mã interface IF-nn và DC-I... (AF-13); C3 thiếu P11b là bước cấp DC (AF-23) |
| P11a --> P12 | P11a-gui/screen-list.md, SCR-nn-*.md | Khớp | SCR, DC | Khớp |
| P07, P08 --> P12 | P07-uc-analysis/, P08 | Khớp | Message "// tênTráchNhiệm" và STT; cột "Dùng trong UC"; R-nn | Khớp |
| P12 --> P13 | P12-class-design.md hoặc P12-class-design/*.md | Khớp | F1 cột Persistent, Ghi chú "từ association class"; F5 R-nn; F7 thuộc tính; generalization | Khớp |
| P12 --> X1 | P12-class-design.md | Khớp | F1 đến F9 | Khớp |
| P12 --> X2 | P12-class-design.md | Khớp | F2 chữ ký, tiền/hậu điều kiện, ngoại lệ; F3 method; F6 state machine | Khớp; tên cột "DC.phương thức" (AF-29) |
| P13 --> X1, X2 | P13-data-model.md | Khớp | F4, F5, F6 | Khớp; README thiếu cạnh P13 --> X2 (AF-17) |
| P06, P04 --> P12, P13, X2 | P06-supplementary-spec.md, P04-uc-specs/*.md | Khớp | BR, dữ liệu vào ra, điều kiện hợp lệ, luồng thay thế | Khớp |

Tên file sơ đồ: mọi đầu ra .drawio của P03, P07 đến P13, X2 khớp C7.2 (riêng ví dụ slug P03, AF-32). Tham chiếu chéo "mục Fx của Pyy" còn lại (P08 --> P07 F3.4; P10 --> P09 F5; P12 --> P09 F3-F6, P10 F3, P11b F3, F5; X1 --> P12 F3; X2 --> P12 F2, F3, F6; C7.3 --> P11a F3) đều trỏ đúng. Mọi định danh viết hoa trong các prompt đã rà hoặc là placeholder khai báo đúng cú pháp, hoặc là trường của profile, hoặc là giá trị liệt kê (NGHIEM_NGAT, DAY_DU, MUI_TEN_KHOI_XUONG...).

### 5.3. Kiểm tra định dạng và từ cấm (toàn bộ file sản phẩm)

- Grep từ cấm theo danh sách của tiêu chí 7 (không phân biệt hoa thường) trên mọi .md ở thư mục gốc prompt-system (21 file, gồm README, Conventions, Profile, P00 đến P13, P02R, X1, X2): không có kết quả. Grep bổ sung Student, Professor, Course Catalog, Billing System, rush order, DVD, đại học, đồ án, học phần: không có kết quả.
- Em dash (U+2014): không có. Mũi tên Unicode (U+2190 đến U+21FF, U+27F0 đến U+27FF, U+2900 đến U+297F): không có.
- Backtick đơn ngoài code block: không có (đã loại trừ nội dung trong fence ba và bốn dấu backtick).
- Cấu trúc: 12 prompt đã rà đều đủ 6 mục theo thứ tự, đúng một khối code bốn dấu backtick nhãn text, đủ thẻ [Context] [Role] [Action] [Format] [Target] [Yêu cầu bổ sung], YEU_CAU_BO_SUNG [TUỲ CHỌN] ở cuối, placeholder đúng cú pháp. Ngoại lệ nhỏ về số ví dụ ở AF-35.

### 5.4. Xác minh trích dẫn Lilly và cập nhật phát hiện cũ

Nguồn đã xác minh: toàn văn bài báo (PDF 10 trang, bản lưu trữ của Gannon University tải từ IEEE Xplore) và trang IEEE Xplore, IEEE CSDL. Thông tin xuất bản: Susan Lilly (SRA International), "Use Case Pitfalls: Top 10 Problems from Real Projects Using Use Cases", Proceedings of TOOLS 30 (Technology of Object-Oriented Languages and Systems), IEEE Computer Society, 1999, trang 174-183.

Danh sách 10 vấn đề nguyên văn:
1. The system boundary is undefined or inconsistent.
2. The use cases are written from the system's (not the actors') point of view.
3. The actor names are inconsistent.
4. Too many use cases.
5. The actor-to-use case relationships resemble a spider's web.
6. The use case specifications are too long.
7. The use case specifications are confusing.
8. The use case doesn't correctly describe functional entitlement.
9. The customer doesn't understand the use cases.
10. The use cases are never finished.

Đối chiếu nội dung gán cho Lilly:
- P01 ("ranh giới không rõ, tên tác nhân không nhất quán"): khớp vấn đề 1 và 3.
- P02 ("viết từ góc nhìn hệ thống, quá nhiều use case"): khớp vấn đề 2 và 4.
- P03 ("quan hệ tác nhân - use case kiểu mạng nhện"): khớp vấn đề 5; cách chữa trong bài (tách vai trò tác nhân cụ thể hơn, dùng tổng quát hoá tác nhân) cũng khớp cách sửa D-AP15 của P03.
- P02R (Role: "danh mục lỗi use case của ... Lilly"; Căn cứ không ghi chú nội dung): khớp, vì bài là danh mục lỗi.
- Bài có nhắc «uses», «extends» trong phần chữa vấn đề 2 (use case chỉ nối qua uses/extends mà toàn xử lý nội bộ) nhưng không có mục riêng về lạm dụng include, extend; không prompt nào gán nội dung đó cho Lilly, nên không có trích dẫn sai.

Kết luận: trích dẫn Lilly ở P01, P02, P02R, P03 đúng tác giả, tiêu đề, hội nghị, năm và nội dung. Có thể bổ sung "IEEE, tr. 174-183" nếu muốn đầy đủ.

Cập nhật trạng thái:
- AF-10: Đã xác minh, danh sách theo trí nhớ ở mục 1 đúng cả 10 mục. Không cần sửa sản phẩm.
- AF-11: Không cần sửa. P07 không nhắc hàng "Hậu điều kiện" của P04; P12 lấy tiền/hậu điều kiện từ BR và bước UC.
- AF-17: Đã sửa. README mục 5 hiện có đủ ba dòng theo đề xuất: "P03 | P04 và P07 của UC có quan hệ thay đổi, P09, P10"; "P05, P06 | P07 của UC dùng thuật ngữ, BR, NFR đã đổi, P08 trở đi (P09 khi NFR đổi)"; "P13 | X1, X2".
