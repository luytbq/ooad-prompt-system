# P01 - Nhật ký người chạy - SaoViet Bus

Đầu ra: design/P01-actors.md (phiên bản 1.0). Bước này không có sơ đồ .drawio.
Kết quả chính: 10 tác nhân (5 người, 2 hệ thống ngoài, 2 thiết bị, 1 thời gian), 5 bên liên quan không phải tác nhân, 16 ứng viên bị loại, 0 Q mới, 2 ASM mới (ASM-06, ASM-07), không có đề xuất sửa P00.

## Vướng mắc

### 1. Thiết bị ngoài làm nền tảng chạy phần mềm thuộc phạm vi

- Vị trí: Action Bước 1.2, "Thành phần có trong trường HE_THONG_NGOAI của hồ sơ dự án là Ngoài, trừ khi tài liệu nguồn nói khác"; Format cột Tính chất, "thiết bị chỉ là kênh nhập, không phải tác nhân, khi nó thuộc ranh giới (Bước 1.2)".
- Gặp gì: hồ sơ dự án ghi "Máy soát vé cầm tay Android có đầu quét mã vạch, do nhà xe tự trang bị" là hệ thống ngoài, còn P00 ASM-01 đưa phần mềm soát vé vào phạm vi. Nguồn giao hành vi nghiệp vụ cho "máy" (báo hợp lệ, soát khi mất sóng, gửi lại kết quả). Prompt chỉ có hai trường hợp: thiết bị thuộc ranh giới (kênh nhập) hoặc thiết bị ngoài có giao thức riêng (tác nhân phụ). Không có hướng dẫn cho phần cứng do bên khác trang bị nhưng là nền tảng chạy một phần của hệ thống. Cũng không rõ giả định ASM của bước trước có tính là "tài liệu nguồn nói khác" hay không.
- Xử lý: tách thành ba dòng trong Mục 1: ứng dụng soát vé (Trong, ASM-01), đầu quét mã vạch (Ngoài, tác nhân phụ ACT-09), phần cứng còn lại (Ngoài, nền tảng, không phải tác nhân). Ghi ASM-06 cho lựa chọn này.

### 2. Cột Hệ quả của Mục 1 không có giá trị cho thành phần Ngoài nhưng không phải tác nhân

- Vị trí: Format Mục 1, "Hệ quả: "Là tác nhân ACT-nn", "Là thành phần nội bộ, không phải tác nhân", hoặc "Chờ trả lời Q-nn"."; Target 1 "Bảng ranh giới liệt kê mọi thành phần mà nguồn nhắc tới".
- Gặp gì: nguồn nhắc tới mạng di động ("vùng mất sóng"), điện thoại, sổ tay ghi vé, phần cứng máy soát vé. Các thành phần này ở ngoài ranh giới nhưng không phải tác nhân (đường truyền, nền tảng, cách làm cũ bị thay thế). Không thể vừa liệt kê đủ (Target 1) vừa chỉ dùng ba giá trị Hệ quả.
- Xử lý: giữ các dòng, ghi Hệ quả mô tả riêng và trỏ sang Mục 4; ghi lựa chọn theo C9 vào Vấn đề còn mở của artifact.

### 3. Lý do loại ở Mục 4 bắt buộc nêu phép thử, nhưng Bước 2.3 loại trước khi có phép thử

- Vị trí: Format Mục 4, "Lý do loại phải nêu phép thử không đạt (A-T1 đến A-T6) và giải thích một câu, hoặc nêu "Gộp vào ACT-nn""; Action Bước 2.3, "Hết giờ chờ trong một phiên đang mở ... không tạo ứng viên tác nhân thời gian".
- Gặp gì: hết 10 phút giữ chỗ (REQ-16) bị loại theo Bước 2.3, không ứng với phép thử nào. Mục 4 lại yêu cầu "mỗi danh từ chủ thể ... phải xuất hiện" nên muốn ghi để người đọc thấy đã xét.
- Xử lý: ghi dòng ở Mục 4 với lý do "Không thành ứng viên theo Bước 2.3", ghi vào Vấn đề còn mở.

### 4. Yêu cầu chức năng có chủ thể là thành phần nội bộ

- Vị trí: Action Bước 7.1, "Mọi REQ loại Chức năng và Giao tiếp ngoài có ít nhất một tác nhân liên quan, hoặc có lý do"; Target 8.
- Gặp gì: REQ-60 ("Máy soát vé gửi lại kết quả soát vé khi có sóng") và REQ-61 (hệ thống gửi danh sách hành khách về máy soát vé) theo ASM-01 là trao đổi giữa hai phần nội bộ. Prompt không nói nên gắn REQ kiểu này với tác nhân nào hay chỉ ghi lý do. Gắn sai sẽ làm P02 sinh use case không có tác nhân thật.
- Xử lý: REQ-60 gắn với ACT-05 Phụ xe (người tạo ra kết quả soát), REQ-61 gắn với ACT-10 Bộ định thời (mốc 15 phút); giải thích và nêu hệ quả nếu Q-01 đổi trong Vấn đề còn mở.

### 5. Một tác nhân thời gian hay nhiều

- Vị trí: Format cột Tên, "Thời gian: "Bộ định thời" (EN: Timer) hoặc tên nêu chu kỳ khi có nhiều nhịp độc lập ("Bộ định thời cuối ngày")".
- Gặp gì: có hai mốc tương đối theo giờ xuất bến của từng chuyến (60 phút: huỷ vé đặt qua điện thoại; 15 phút: gửi danh sách hành khách). Không rõ hai mốc tương đối cùng gốc có phải "nhiều nhịp độc lập" không. Phép thử A-T5 cũng không áp dụng rõ cho tác nhân thời gian.
- Xử lý: một tác nhân ACT-10 Bộ định thời với hai dòng Kích hoạt.

### 6. Tính chất của cổng thanh toán phụ thuộc cơ chế API chưa biết

- Vị trí: Format cột Tính chất, ví dụ "Nếu Cổng thanh toán tự gửi thông báo kết quả thanh toán vào một thời điểm không xác định và việc đó khởi động một xử lý riêng, thì Cổng thanh toán là "Chính và phụ"."
- Gặp gì: nguồn không nêu cơ chế báo kết quả, hồ sơ ghi "chưa có tài liệu API"; P00 Q-10 (cổng báo thành công sau khi hết giữ chỗ) gợi ý có thông báo không đồng bộ. Ở bước phân tích, quyết định Phụ hay Chính và phụ phụ thuộc chi tiết giao tiếp chưa có.
- Xử lý: xếp Phụ theo câu chữ nguồn, ghi ASM-07 nêu điều kiện đổi thành Chính và phụ (chờ Q-24, Q-10).

### 7. Tổng quát hoá khi chỉ có một biến thể

- Vị trí: Action Bước 5 a), "Có từ hai tác nhân con trở lên"; Target 7 "có ít nhất hai con".
- Gặp gì: hành khách có tài khoản có thêm quyền xem lịch sử vé so với hành khách không có tài khoản (A-T5 "tập mục tiêu, quyền ... khác"). Không thể lập cha - con vì chỉ có một con, nhưng tách hai tác nhân riêng thì lặp đường nối. Prompt không nói cách xử lý biến thể quyền của cùng một vai trò.
- Xử lý: gộp vào ACT-01, coi tài khoản là điều kiện của mục tiêu xem lịch sử vé, ghi ở Mục 4.

### 8. Không có liên kết SH --> ACT cho bên liên quan đã thành tác nhân

- Vị trí: Format Mục 2 (không có cột SH); Mục 3 "Cột SH: mã SH-nn tương ứng trong bảng bên liên quan của P00".
- Gặp gì: P00 có SH-02, SH-04, SH-05, SH-06, SH-08, SH-10, SH-12, SH-13, SH-14 là người dùng hoặc hệ thống trực tiếp. Bảng tác nhân không có chỗ ghi SH tương ứng, nên truy vết SH --> ACT chỉ suy được qua tên.
- Xử lý: không thêm cột (giữ đúng Format); ghi nhận ở đây.

### 9. Chi tiết nhỏ của khung artifact

- Vị trí: Conventions C5, "# <Mã bước> - <Tên artifact> - <Tên hệ thống>" và "Đầu vào đã dùng | Danh sách file và phiên bản".
- Gặp gì: prompt P01 không nêu Tên artifact cho tiêu đề; tài liệu nguồn và hồ sơ dự án không có số phiên bản.
- Xử lý: dùng tiêu đề "Danh sách tác nhân"; ghi "(bản hiện có)" cho file không có phiên bản, như P00 đã làm.

### 10. Dòng của chính hệ thống trong bảng ranh giới

- Vị trí: Format Mục 1, "Một câu nêu hệ thống cần xây dựng. Sau đó là bảng" và "Thành phần: mọi phần mềm, thiết bị, hệ thống, kho dữ liệu được nguồn nhắc tới".
- Gặp gì: không rõ có cần một dòng cho chính hệ thống hay các phần con (phần dành cho nhân viên) khi nguồn không gọi tên chúng; không rõ kho dữ liệu chỉ được ngụ ý (bộ nhớ của máy soát vé khi mất sóng) có tính là "được nguồn nhắc tới".
- Xử lý: không có dòng cho chính hệ thống (đã nêu ở câu mở đầu và ở Mục 4); có dòng cho dữ liệu lưu trên máy soát vé vì REQ-59, REQ-60 ngụ ý trực tiếp, áp dụng Bước 1.3.

## Kết quả tự kiểm tra theo Target

| Target | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | Có lệch giá trị cột Hệ quả, xem vướng mắc 2 |
| 2 | Đạt | Ứng dụng soát vé, website, dữ liệu trên máy đều ở Trong và không là tác nhân |
| 3 | Đạt | ACT-09 đạt A-T1 và A-T2 nhờ ASM-06; phụ thuộc Q-01 |
| 4 | Đạt | |
| 5 | Đạt | |
| 6 | Đạt | |
| 7 | Đạt | Không có tổng quát hoá |
| 8 | Đạt | REQ-60, REQ-61 gắn tác nhân kèm lý do ở Vấn đề còn mở, xem vướng mắc 4 |
| 9 | Đạt | |
| 10 | Đạt | Mục tiêu đổi, trả vé dựa trên ASM-02 của P00 |
| 11 | Đạt | |
