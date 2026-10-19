Model của phiên chạy: Sonnet

# Nhật ký người chạy - P04 cho UC-005 (Mua hoặc gia hạn gói tập) - gym VietFit

Đầu ra: design/P04-uc-specs/UC-005-purchase-or-renew-membership-package.md, design/diagrams/P04-activity-UC-005.drawio, design/P04-uc-specs/_BR-register.md. Lần chạy P04 đầu tiên của dự án (chưa có sổ BR, chưa có đặc tả P04 khác, chưa có P05, P06). Mã Q, ASM lớn nhất trước khi chạy: Q-49, chưa có ASM (chế độ NGHIEM_NGAT). Sau khi chạy: Q-57, 8 Q mới (Q-50 đến Q-57), 5 BR (BR-01 đến BR-05), 13 bước luồng chính, 8 luồng thay thế (4a, 4b, 4c, 8a, 8b, 9a, 10a, 12a) trong 10 hàng của bảng, 37 node và 38 cạnh (kể cả 5 NoteLink).

Kết quả tự kiểm tra Target: đạt, trừ mục 8 (đạt một phần, xem mục 8 dưới đây) và mục 12 (đạt một phần, xem mục 1 dưới đây). Hai mục này cũng được ghi ở "Vấn đề còn mở" của đặc tả. File .drawio đã kiểm bằng xml.dom.minidom, hợp lệ; một script tự viết còn kiểm khoảng cách node tối thiểu 40, toạ độ bội số của 10 và không cạnh nào cắt qua node.

## Các vướng mắc

### 1. Target 5a mâu thuẫn mềm với chế độ NGHIEM_NGAT (Target 12, C1.1)

- Vị trí: [Target] 5a: "Luồng chính và mọi luồng thay thế kết thúc use case có tác nhân người tham gia đều có bước hệ thống báo kết quả (thành công hoặc lý do thất bại) cho tác nhân người đó ... nguồn không nêu cách báo thì có Q-nn" so với [Target] 12: "Không có luồng, quy tắc, trường dữ liệu, ngưỡng nào do AI tự thêm ở chế độ NGHIEM_NGAT".
- Gặp gì: nguồn chỉ nói "Đơn mua chưa thanh toán thành công trong 15 phút thì bị huỷ", không nói hội viên được báo. Để thoả 5a phải viết bước "Thông báo ..." ở luồng 9a2 và 10a; bước này là phần tử không có câu gốc. Câu "nguồn không nêu cách báo thì có Q-nn" chỉ dặn có Q về kênh, không nói bước báo có được viết khi chính việc báo cũng không có trong nguồn.
- Xử lý: viết bước báo (9a2, 10a) và tạo Q-53 hỏi kênh (và gián tiếp hỏi có báo hay không); ghi sự đánh đổi vào Vấn đề còn mở. Đề nghị prompt nói rõ 5a thắng 12 hay ngược lại.

### 2. Nhiều tác nhân chính với luồng thay thế chỉ do một tác nhân thực hiện (F4.2 mục 12 và F10.4)

- Vị trí: F4.2 mục 12: "ghi tên các tác nhân nối bằng ' / ' và mọi khác biệt về hành vi giữa họ đặt thành luồng thay thế"; F10.4: "Nhiều tác nhân chính ghi chung (quy tắc F4.2 mục 12) thì dùng một partition".
- Gặp gì: UC-005 có hai tác nhân chính (ACT-02 Hội viên, ACT-05 Lễ tân), P01 không có tổng quát hoá. Các bước chung (1, 3, 7) ghi "Hội viên / Lễ tân". Nhưng luồng 8a, 8b chỉ do Lễ tân làm; ghi "Hội viên / Lễ tân" là sai nghĩa, ghi "Lễ tân" thì F10.4 ("một partition cho mỗi chủ thể xuất hiện trong cột Thực hiện bởi") đòi một partition riêng. Prompt không nói cách xử lý khi một tác nhân vừa nằm trong chủ thể ghép vừa đứng riêng.
- Xử lý: tạo hai partition P-ACT-02-05 "Hội viên / Lễ tân" và P-ACT-05 "Lễ tân" (4 partition tổng cộng). Ngoài ra luồng chính (bước 9, 10) chỉ đúng cho hội viên (cổng thanh toán) nhưng vẫn ghi chung với lễ tân ở bước 1, 3, 7 theo F4.2 mục 12, khiến "luồng chính" không còn là một kịch bản của một tác nhân. Ghi trong Vấn đề còn mở.

### 3. Vị trí bước bắt đầu chờ 15 phút khi chính vị trí là câu hỏi mở (F4.2 mục 15)

- Vị trí: F4.2 mục 15: "bước bắt đầu chờ đặt đúng vị trí nguồn nêu"; P00 Q-25: "Thời hạn 15 phút của đơn mua tính từ lúc tạo đơn hay từ lúc bắt đầu thanh toán".
- Gặp gì: nguồn không nêu vị trí; Q-25 đã có nhưng chưa trả lời. Prompt không nói khi vị trí đang là câu hỏi mở thì chọn thế nào ở NGHIEM_NGAT (không giả định, nhưng luồng cần một vị trí). Phụ thêm: Q-25 còn hỏi có áp dụng cho đơn bán tại quầy không, nên đặt bước chờ trước hay sau chỗ rẽ kênh thu tiền cũng đổi nghĩa.
- Xử lý: đặt ở bước 9 (sau chỗ rẽ kênh thu tiền, trước khi gửi cổng thanh toán), dùng hình thức liền nhau của F4.2 mục 15 (bước 9 chờ, bước 10 sự kiện tới, luồng 9a). Ghi lựa chọn vào Mục 8 và Vấn đề còn mở, dẫn Q-25. Lẽ ra cần quy tắc hoặc ví dụ cho tình huống này.

### 4. Luồng chính "điển hình" không có căn cứ nguồn cho kịch bản phổ biến nhất (F4.1, F5.4)

- Vị trí: F4.1: "một kịch bản thành công điển hình"; [Action] 4: "Chỉ giữ các trường hợp có căn cứ trong nguồn".
- Gặp gì: nguồn chỉ nêu ngày bắt đầu gói mới cho một nhánh (REQ-17: gia hạn khi gói cũ còn hiệu lực). Mua gói mới (kịch bản phổ biến nhất), gia hạn khi gói cũ đã hết hạn (Q-24) và gia hạn khi gói cũ đang bảo lưu đều không có ngày bắt đầu. Luồng "điển hình" thực tế buộc phải chọn nhánh gia hạn còn hiệu lực làm luồng chính, còn mua mới thành luồng thay thế "Chờ Q-51". Prompt không dự liệu việc nhánh phổ biến nhất lại phải là luồng thay thế chờ câu hỏi.
- Xử lý: luồng chính đi theo REQ-17; bước 4 có ba luồng 4a, 4b, 4c kết thúc ở "Chờ Q-nn" (Q-51, Q-24, Q-52); giải thích ở Mục 8. Kéo theo hậu điều kiện tối thiểu của ba luồng này chưa xác định, ghi bằng Q.

### 5. Hậu điều kiện tối thiểu khi nhiều luồng kết thúc bằng "Chờ Q-nn" (F3)

- Vị trí: F3: "Chỉ ghi điều có căn cứ; nếu không có gì thì ghi 'Không có thay đổi dữ liệu nào được lưu' khi mọi luồng thất bại đều kết thúc trước bước lưu, ngược lại ghi Q-nn".
- Gặp gì: luồng 9a có thay đổi dữ liệu (huỷ đơn) nên không dùng được câu mẫu; các luồng 4a, 4b, 4c, 10a, 12a chưa kết thúc rõ. "ghi Q-nn" không nói ghi vào đâu (hàng F1 hay mục Câu hỏi mở).
- Xử lý: ghi hậu điều kiện tối thiểu cho luồng 9a và liệt kê các luồng chờ Q kèm mã Q ngay trong hàng đó.

### 6. "Chờ Q-nn" trỏ tới Q của bước trước không có trong mục Câu hỏi mở của đặc tả (Target 8)

- Vị trí: [Target] 8: "'Chờ Q-nn' với Q-nn có trong mục Câu hỏi mở"; Conventions C3: "mã chỉ trỏ tới một câu hỏi duy nhất".
- Gặp gì: Q-24 (gia hạn khi gói cũ đã hết hạn), Q-13 (thanh toán lại) đã cấp ở P00. Chép lại vào mục Câu hỏi mở của P04 sẽ làm một mã có hai chỗ định nghĩa; không chép thì Target 8 đọc theo nghĩa đen là không đạt. P02 xử lý bằng một câu dẫn mã bên dưới bảng.
- Xử lý: theo cách của P02, một đoạn liệt kê Q cũ liên quan dưới bảng Câu hỏi mở; coi Target 8 đạt một phần. Đề nghị Target 8 sửa thành "có trong mục Câu hỏi mở của artifact này hoặc của artifact đầu vào".

### 7. F4.2 mục 17 (mốc của use case do tác nhân thời gian kích hoạt)

- Vị trí: F4.2 mục 17: "use case tạo, đổi hoặc làm mất hiệu lực dữ liệu mà một use case do tác nhân thời gian kích hoạt dùng làm mốc ... có bước hệ thống 'Hẹn / hẹn lại / huỷ mốc'".
- Gặp gì: UC-005 tạo gói tập và ngày hết hạn mà UC-008 (ACT-13, mỗi ngày 8 giờ) đọc, nhưng UC-008 chạy theo lịch cố định hằng ngày chứ không hẹn mốc riêng cho từng gói. Câu ví dụ "hạn trả của phiếu mượn" gợi một mốc từng đối tượng; không rõ trường hợp quét hằng ngày có thuộc quy tắc hay không.
- Xử lý: không thêm bước hẹn mốc; ghi lý do ở Mục 8. Còn mốc 15 phút của chính UC-005 là luồng 9a trong phiên theo P02 U-R07.

### 8. Danh sách mục bắt buộc của khung A so với điều kiện "chỉ khi" (Format A, C5, Target 16)

- Vị trí: Format A: "## Giả định (chỉ khi CO_NHAN)", "## 8a. Kịch bản chính (chỉ khi DAY_DU)"; Conventions C5: "Mục nào không có nội dung thì ghi 'Không có', không xoá mục"; Target 16: "Mọi mục của khung C5 có mặt".
- Gặp gì: mục Giả định ở NGHIEM_NGAT vừa "chỉ khi CO_NHAN" vừa "không xoá mục". Hồ sơ ghi MUC_CHI_TIET = GON, còn prompt nhắc "DAY_DU"; hồ sơ mẫu không cho tôi biết các giá trị hợp lệ (đọc suy ra GON và DAY_DU là hai giá trị đối lập).
- Xử lý: giữ mục Giả định với "Không có (chế độ NGHIEM_NGAT, không dùng mục này)", như P02 đã làm; bỏ mục 8a vì GON.

### 9. Khoảng cách trục dọc trong bố cục nhánh (F10.6) không dùng được khi action rộng 180

- Vị trí: F10.6: "các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải rồi rẽ tới từng action".
- Gặp gì: action chính rộng 180 có mép phải cách tâm decision 70, nên trục dọc cách decision 30 về bên phải cắt qua các action chính ở dưới (A-5, A-6). Tôi phải dời trục tới 130 so với tâm. Ngoài ra, bố cục nhiều nhánh vượt partition (từ hệ thống sang partition Lễ tân, sang Cổng thanh toán) chiếm nhiều công sức tính toạ độ tay; tôi viết script riêng để sinh bảng Node, bảng Edge và .drawio từ một nguồn và kiểm cạnh cắt node. Prompt không có hướng dẫn về nhánh đi ngược sang partition ở bên trái của hệ thống.
- Xử lý: trục 130 và điểm uốn tuyệt đối trong cột Điểm uốn. Bảng Node thêm bốn cột x, y, w, h theo khuyến nghị C7.1 dù F10.5 không liệt kê.

### 10. Ví dụ ở cột Ví dụ buộc phải bịa giá trị

- Vị trí: F6.1: "Ví dụ: giá trị thực tế, hợp lệ, nhất quán".
- Gặp gì: trường mà điều kiện hợp lệ là "Chưa quy định (Q-nn)" (chi nhánh, mã giao dịch POS, gói cần gia hạn) vẫn cần ví dụ; số tiền, ngày, tên chi nhánh không có trong nguồn. Ví dụ thực chất là dữ liệu bịa, dễ bị đọc nhầm là quy định.
- Xử lý: dùng giá trị minh hoạ nhất quán (giá 1.200.000 đ, khuyến mãi 10 phần trăm không vượt trần 20 phần trăm cho 1.080.000 đ, ngày hết hạn 30/11/2026 và ngày bắt đầu 01/12/2026) và ghi chú trong Vấn đề còn mở rằng đó là giá trị minh hoạ.

### 11. Phạm vi đọc và quá tải ngữ cảnh

- Vị trí: mục 3 "Phần cần dùng" và [Action] 1e.
- Gặp gì: để cấp tiếp Q, ASM phải quét mục Câu hỏi mở của P00 (khoảng 45 Q, nhiều dòng rất dài), P01, P02, P02R, P03; phần P00 Câu hỏi mở lớn hơn nhiều so với phần liên quan UC-005. Mục Câu hỏi mở của P00 còn cần đọc để chọn Q liên quan (Q-01, Q-08, Q-09, Q-10, Q-13, Q-14, Q-24, Q-25, Q-35, Q-37, Q-39, Q-43, Q-45, Q-47); không có chỉ dẫn lọc Q theo REQ ngoài "các Q-nn liên quan tới các REQ đó". Cột "Ảnh hưởng tới" của Q đôi khi nhắc "luồng mua gói (P04)" thay vì mã REQ, nên lọc bằng mã REQ bỏ sót; tôi phải đọc cả bảng.
- Xử lý: đọc cả mục Câu hỏi mở của P00 và tự chọn các Q liên quan; không đọc phần khác của P00, P02 ngoài các dòng cần.

### 12. Tiền điều kiện xác thực của Lễ tân (F3)

- Vị trí: F3: "Tiền điều kiện đã xác thực chỉ ghi cho tác nhân được P03 nối với UC Đăng nhập".
- Gặp gì: P03 chỉ nối ACT-02 với UC-004; UC-005 có hai tác nhân chính nên tiền điều kiện đúng cho hội viên và không cho lễ tân (Q-47 chưa trả lời). Tiền điều kiện có điều kiện theo tác nhân ("khi tự mua ...") nghe gượng, trong khi F3 yêu cầu mệnh đề trạng thái kiểm chứng được.
- Xử lý: ghi một mệnh đề "Hội viên, khi tự mua hoặc gia hạn trên ứng dụng, đã được xác thực ...", dẫn Q-47 ở Mục 8.

### 13. Thứ tự bước 11 (kích hoạt gói) và bước 12 (gửi hoá đơn điện tử)

- Vị trí: F4.2 mục 2 chỉ nói bước gửi không chờ kết quả; nguồn Mục 10 câu 2 không nêu thứ tự giữa kích hoạt gói và xuất hoá đơn.
- Gặp gì: thứ tự quyết định hệ thống phải làm gì khi hệ thống hoá đơn điện tử lỗi; không có hướng dẫn chọn thứ tự khi nguồn không nêu.
- Xử lý: đặt sau kích hoạt gói và tạo Q-54 hỏi cả thứ tự lẫn xử lý lỗi.

## Mục Target không đạt hoàn toàn

- Target 8: đạt một phần (xem vướng mắc 6).
- Target 12: đạt một phần (xem vướng mắc 1; thêm bước 6, 7 là cặp yêu cầu - phản hồi suy ra, và bước 2 hiển thị giá để chọn gói).
- Các mục còn lại: đạt.
