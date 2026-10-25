Model của phiên chạy: Sonnet

# Nhật ký người chạy P01 - Hệ thống quản lý chuỗi cầm đồ Phúc An

Tham số: QUYET_DINH_RANH_GIOI = "Ứng dụng di động cho khách: Trong. Máy in nhãn mã vạch: Ngoài."; YEU_CAU_BO_SUNG = Không có. Đầu ra: design/P01-actors.md (18 ACT: 8 Người, 5 Hệ thống ngoài, 3 Thiết bị, 2 Thời gian; 6 dòng Mục 3; 1 Q mới Q-36; 3 ASM mới ASM-09 đến ASM-11). Không có sơ đồ .drawio ở bước này.

## Vướng mắc

1. Vị trí: Bước 2.3, "Mỗi nhóm hành vi như vậy tạo một ứng viên tác nhân thời gian" và [Format] "tên nêu chu kỳ khi có nhiều nhịp độc lập ("Bộ định thời cuối ngày")".
   Gặp: nguồn có hai nhịp (9 giờ sáng nhắc khách; 0 giờ chuyển chờ thanh lý). Không rõ "nhịp độc lập" cần tách thành hai tác nhân hay gộp một Timer; phép thử A-T5 (khác tập mục tiêu) nghiêng về tách, nhưng mục Lỗi thường gặp/Ambler hướng một Timer.
   Xử lý: tách thành ACT-17 và ACT-18, ghi cách gộp lại ở Vấn đề còn mở.

2. Vị trí: Bước 1.2, "Chỉ thiết bị rời có giao tiếp riêng với phần mềm (máy in nối qua mạng, barrier nhận lệnh) mới là tác nhân Thiết bị".
   Gặp: HE_THONG_NGOAI ghi "Máy quét mã vạch" và "Đầu đọc căn cước (USB)" mà không nói rõ có giao tiếp riêng hay là kênh nhập gắn vào máy trạm. Máy quét mã vạch kiểu bàn phím (keyboard wedge) về bản chất là kênh nhập.
   Xử lý: coi cả hai là thiết bị rời nằm ngoài ranh giới (có REQ Giao tiếp ngoài REQ-06, REQ-58 do P00 xếp) nên là tác nhân Phụ; không tạo Q.

3. Vị trí: Bước 1.2 / Mục 1, "mọi phần mềm, thiết bị, hệ thống, kho dữ liệu được nguồn nhắc tới" so với quy tắc ngoài "không bỏ sót thành phần chỉ nhắc thoáng qua".
   Gặp: "in hợp đồng", "in biên nhận" ngụ ý một máy in văn bản mà HE_THONG_NGOAI không liệt kê (chỉ có máy in nhãn). Prompt không nói rõ xử lý với thiết bị ngụ ý nhưng chưa liệt kê ở CO_NHAN (hỏi hay giả định tồn tại).
   Xử lý: Q-36 và ASM-11 (máy in thông thường, không phải tác nhân), ghi một dòng ranh giới Ngoài.

4. Vị trí: Conventions C1.2, "chỗ thiếu làm thay đổi danh sách chức năng, tác nhân hoặc use case phải có ASM-nn" và C3 "Chỉ tính mã ở cột Mã".
   Gặp: P00 để Q-31 (ai tra cứu bằng mã vạch) và Q-22 (kênh báo quản lý cửa hàng) chỉ là Q, không có ASM, nên P01 buộc phải chọn vai trò và tự lập ASM. Prompt P01 không nói rõ ASM mới của P01 có phải trỏ "Chờ Q-nn" của Q cũ của P00 (dùng lại mã Q cũ) hay tạo Q mới.
   Xử lý: dùng lại Q-31 và Q-22 của P00 (cột Lý do "Chờ Q-31", "Chờ Q-22"), không tạo Q trùng; cấp Q-36 chỉ cho vấn đề mới. Đồng thời đưa REQ-94 vào "Đề xuất sửa artifact trước".

5. Vị trí: Bước 4.1 / Mục 2 cột Tên, "Chức danh chỉ được dùng làm tên khi chức danh đó ứng với đúng một vai trò" cùng Mục 5 vai trò kiêm nhiệm (REQ-96).
   Gặp: REQ-96 nói một nhân viên kiêm hai chức danh; không rõ có cần quan hệ tổng quát hoá hay vai trò kiêm. Giữ hai tác nhân riêng, không cha con (không thoả "là một").
   Xử lý: hai tác nhân riêng, nêu kiêm nhiệm trong Mô tả vai trò; ghi vào Mục 4.

6. Vị trí: Mục 2 cột Loại, "Người: vai trò do con người đảm nhận, tương tác qua giao diện người dùng" và Bước 3 A-T2.
   Gặp: Khách tại quầy không tự thao tác (giao dịch qua nhân viên), chỉ dùng trực tiếp ứng dụng di động. Prompt không có hướng dẫn tách một tên thành "tác nhân khi dùng kênh A, bên liên quan khi dùng kênh B" nên cùng một SH xuất hiện hai lần (ACT-01 và Mục 3).
   Xử lý: giữ ACT-01 Khách và lập hai dòng SH-02 ở Mục 3 theo kênh; không coi là mâu thuẫn A-T2.

7. Vị trí: Mục 4, "Mỗi danh từ chủ thể trong nguồn mà không thành tác nhân phải xuất hiện ở bảng này hoặc ở Mục 3".
   Gặp: số chủ thể rất nhiều (cơ quan công an, nhà mạng, hãng sản xuất đầu đọc...), có nhiều danh từ hiếm khi chủ thể (két, thẻ căn cước). Không rõ mức đủ nên bảng dài 30 dòng, gần như chắc chắn thừa so với nhu cầu.
   Xử lý: liệt kê rộng; không đặt giới hạn.

8. Vị trí: Bước 7.1, "Mọi REQ loại Chức năng và Giao tiếp ngoài có ít nhất một tác nhân liên quan, hoặc có lý do".
   Gặp: REQ-88 (hệ thống ghi nhật ký) và REQ-46 (huỷ giao dịch quá 10 phút) là hành vi tự động trong hệ thống; nguồn không có tác nhân khởi xướng. Với REQ-14 (gợi ý giá) nguồn không nói ai nhận.
   Xử lý: REQ-88 có lý do ở Vấn đề còn mở; REQ-46 gắn ACT-10 và ACT-01; REQ-14 gắn ACT-03 có ghi chú.

Mục Target: 11/11 Đạt (Mục 8 có lý do ở Vấn đề còn mở).
