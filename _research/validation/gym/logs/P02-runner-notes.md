Model của phiên chạy: Sonnet

# Nhật ký người chạy - P02 (lần chạy đầu) - gym (VietFit)

Đầu ra: gym/design/P02-usecases.md (không có sơ đồ .drawio). Kết quả: 28 UC (27 User-goal, 1 Subfunction), 71 CAND, 31 EV, 96 REQ trong ma trận (REQ-01 đến REQ-04 không phủ, loại Dữ liệu, chuyển P06). Q mới Q-46 đến Q-49; Q lớn nhất toàn dự án Q-49; chưa cấp ASM (NGHIEM_NGAT). Mục 5 được sinh bằng script từ cột REQ của bảng 4b rồi kiểm tra chéo (UC 4a và 4b cùng tập mã, mọi CAND có đúng một kết luận, mọi tham chiếu UC, CAND, EV tồn tại, không có em dash, mũi tên, inline code).

Kết quả tự kiểm tra Target: 14 mục đều ghi Đạt trong artifact, kèm các điểm lưu ý ở Vấn đề còn mở. Hai mục đạt có điều kiện: Target 3 (cách đọc "trỏ tới câu hỏi có trong mục Câu hỏi mở", xem vướng mắc 6) và Target 4 (UC của tác nhân thời gian, xem vướng mắc 5).

## Vướng mắc

1. Kết luận chỉ trỏ tới một UC nhưng nhiều ứng viên xảy ra trong nhiều UC.
- Vị trí: Format Mục 3, "Kết luận: một trong 'Giữ thành UC-nnn', 'Gộp vào UC-nnn', 'Là bước của UC-nnn'..."; Bước 7.4 "mọi 'Gộp vào', 'Là bước của' trỏ tới một UC đang tồn tại".
- Gặp: "Xuất hoá đơn điện tử" (REQ-91, 92) xảy ra trong 4 UC có thu tiền; "gửi thông báo đẩy" và "gửi SMS" (REQ-87 đến 90) xảy ra trong 4 UC. Cột Kết luận không cho trỏ nhiều UC; Q4 a không dùng được vì đoạn trao đổi dưới 3 bước.
- Xử lý: ghi "Là bước của UC-005, UC-007, UC-017, UC-019" (CAND-16) và "Là bước của UC-008, UC-011, UC-014, UC-015" (CAND-64, CAND-65), ghi lý do ở Vấn đề còn mở. Với thông báo cụ thể (REQ-27, 75, 77, 84) tách thành ứng viên riêng cho từng UC. Đề nghị prompt nói rõ có được trỏ nhiều UC hay phải tách ứng viên.

2. Bán gói tại quầy (lễ tân) so với mua gói trên ứng dụng (hội viên): rule dẫn tới gộp, tên UC không có hướng dẫn.
- Vị trí: U-R10 "Bước của người đại diện có bước tương ứng cùng mục đích ... không tính vào đoạn riêng, ví dụ ... nhận tiền mặt tại quầy so với hoàn tiền qua cổng thanh toán"; U-R12 "Tác nhân phụ hoặc kênh nhận, trả tiền khác nhau (cổng thanh toán hay tiền mặt tại quầy) không đủ để tách"; U-N2 "Góc nhìn tác nhân chính (người khởi xướng)".
- Gặp: luồng lễ tân (chọn gói, thu tiền mặt hoặc nhập mã POS) không có đoạn riêng từ 2 bước, kết quả như nhau, nên U-R10 b: một UC nối ACT-02 và ACT-05. Nhưng hai tác nhân khởi xướng dùng hai động từ đối lập (mua, bán); U-N2 chỉ nói tên theo người khởi xướng, còn ví dụ "Đặt phòng" và "Đặt phòng cho khách" chỉ áp dụng cho trường hợp tách (U-R10 a). Cũng không rõ Q-01 (lễ tân có tạo tài khoản tại quầy) có làm đoạn riêng hay không; nguồn không nói nên chưa tính.
- Xử lý: gộp thành UC-005 "Mua gói tập" (tên theo góc nhìn hội viên), ghi điều kiện xét lại theo Q-01 ở Vấn đề còn mở. Đề nghị bổ sung ở U-R10 b cách đặt tên UC có hai tác nhân khởi xướng.

3. "Mua hoặc gia hạn gói tập": không có quy tắc quyết định gộp hay tách rõ ràng.
- Vị trí: U-R12 "mặc định là luồng thay thế"; Bước 7.1 "chỉ khác dữ liệu hoặc khác lựa chọn nhỏ"; U-N7 "Có 'và' ... là dấu hiệu gộp hai mục tiêu" và U-N3 (tên nêu kết quả).
- Gặp: gia hạn khác mua ở mốc bắt đầu (REQ-17) và có sự kiện nhắc gia hạn riêng, nhưng nguồn gộp chung một câu "mua hoặc gia hạn". Gộp thì tên "Mua gói tập" không còn nêu gia hạn; tách thì hai UC gần như giống hệt (U-T11).
- Xử lý: gộp (CAND-06 Gộp vào UC-005), ghi gia hạn ở Mô tả ngắn. Đây là quyết định theo phán đoán.

4. Q4 a (include đoạn xem) mâu thuẫn nhẹ với U-R05 cho ca "xem lịch lớp khi đặt chỗ".
- Vị trí: Q4 a đoạn "Đoạn dùng chung trùng với một UC User-goal đã giữ ... kết luận 'Gộp vào UC-nnn' ... 'Được include bởi UC-xxx'"; U-R05 "xem danh sách phòng trống trong khi đặt phòng là bước của 'Đặt phòng'".
- Gặp: UC-002 "Xem lịch lớp nhóm" (ACT-01, không tài khoản) là User-goal độc lập; hội viên cũng xem lịch khi đặt chỗ (UC-010). Hai chỉ dẫn cho hai kết luận khác nhau; Q4 a cũng không nói tác nhân chính của UC độc lập có cần trùng tác nhân của UC gốc không (ở đây ACT-01 khác ACT-02).
- Xử lý: chọn "Là bước của UC-010" (CAND-21), lý do nguồn không mô tả đoạn xem từ 3 bước. Phát sinh Q-46 (hội viên có xem độc lập không).

5. Tác nhân thời gian: tiêu chí "phiên đang mở" chưa thao tác hoá; U-T1 đến U-T12 áp dụng cho UC thời gian không rõ.
- Vị trí: U-R07 "tác nhân chính vẫn đang ở phiên của một UC và hệ thống chờ một sự kiện có hạn giờ"; U-T2 "Một người, ở một nơi", U-T3 Boss test, U-T4 "3-15 bước"; Target 4 "trừ phép thử bị một quy tắc U-R ... ghi đè".
- Gặp: (a) đơn mua chờ thanh toán 15 phút (hội viên có thể thoát ứng dụng) bị coi là trong phiên, còn hạn 30 phút xác nhận nhận chỗ và hạn 12 giờ của huấn luyện viên là ngoài phiên; P01 đã chốt như vậy nên tôi giữ nhất quán (C1.3) nhưng ranh giới không suy ra được từ U-R07. (b) 4 UC của ACT-14 (UC-013, 015, 016, 022) khó đạt U-T2, U-T3, U-T4 theo nghĩa thông thường; U-R07 chỉ ghi đè ngầm.
- Xử lý: ghi "-" ở cột Phép thử không đạt và "U-R07" ở cột Lý do; giải thích số lượng 4 UC ở Mục 6. Đề nghị U-R07 nêu rõ các phép thử bị miễn cho UC của tác nhân thời gian.

6. Target 3 và mã Q kế thừa.
- Vị trí: Target 3 "mọi kết luận 'Chờ Q-nn' trỏ tới câu hỏi có trong mục Câu hỏi mở"; Conventions C3 "mã chỉ trỏ tới một câu hỏi duy nhất".
- Gặp: 8 ứng viên chờ các Q do P00, P01 cấp (Q-01 đến Q-06, Q-11, Q-45). Chép lại các Q đó vào mục Câu hỏi mở của P02 sẽ lặp mã giữa hai artifact; không chép thì mục Câu hỏi mở của P02 không chứa câu hỏi được trỏ tới.
- Xử lý: không chép, thêm một đoạn ngay dưới bảng Câu hỏi mở liệt kê các mã kế thừa và nơi chứa nội dung, và ghi ở Vấn đề còn mở. Đề nghị Target 3 sửa thành "câu hỏi có trong mục Câu hỏi mở của P02 hoặc của artifact đầu vào".

7. Ứng viên từ Q của bước trước nhưng không có sự kiện (Q-45, Q-11) và đề xuất sửa P01 có điều kiện.
- Vị trí: Bước 2.4 "Chỉ ghi sự kiện mà nguồn nêu hoặc suy ra trực tiếp"; U-R07 "Nếu P01 không có tác nhân thời gian mà nguồn có hành vi này: ghi vào 'Đề xuất sửa artifact trước' ... và vẫn lập ứng viên"; U-R08 (hệ thống ngoài tự gửi).
- Gặp: P01 để ngỏ Q-45 (cổng thanh toán tự gửi kết quả hay không) và A-T4 loại mốc 6 giờ sáng thứ Hai (Q-11). Cả hai cho ứng viên có thể thành UC nhưng nguồn chưa nêu sự kiện nên không tạo EV. U-R07 yêu cầu đề xuất sửa P01 nhưng ở đây việc có hành vi hay không còn tuỳ Q-11.
- Xử lý: lập CAND-13 và CAND-24 kết luận "Chờ Q-nn" với lý do nêu câu trả lời dẫn tới UC; ghi một đề xuất sửa P01 có điều kiện. Mục 1 chỉ yêu cầu tác nhân Chính, nhưng tôi thêm dòng cho ACT-08 để ứng viên CAND-13 có chỗ đứng; prompt không nói ứng viên từ tác nhân Phụ nằm ở đâu.

8. Bước 9.1 (đánh số UC và nhóm) khó áp dụng cho tác nhân có nhiều quy trình.
- Vị trí: "Nhóm chứa use case khởi đầu quy trình nghiệp vụ chính được đánh số trước ... Chỉ tính UC mà chính tác nhân chính đó phải làm trước".
- Gặp: tác nhân nhiều UC nhất là Hội viên (ACT-02), nhưng Hội viên có ba quy trình (gói tập, lớp nhóm, huấn luyện cá nhân) và rule không chọn quy trình nào là "chính". Điều kiện tiên quyết "đăng ký tài khoản" do ACT-01 làm, không phải ACT-02, nên câu "chính tác nhân chính đó phải làm trước" không áp dụng chặt. Ngoài ra "việc xảy ra trước đánh số trước" mơ hồ với UC huỷ lớp vì sự cố (có thể xảy ra bất cứ lúc nào).
- Xử lý: coi ACT-01 và ACT-02 là cùng một người ở hai thời điểm; chọn quy trình mua gói tập là chính (giá trị cốt lõi cho hội viên), đánh số nhóm Tiếp cận và tài khoản trước, rồi Gói tập, rồi các nhóm còn lại theo thứ tự xuất hiện trong nguồn (Lớp nhóm Mục 3, Ra vào Mục 5, Huấn luyện cá nhân Mục 7, Giá và báo cáo Mục 9).

9. Xung đột nhẹ giữa tên theo domain và danh sách từ cấm; độ dài tên.
- Vị trí: U-N4 (dùng thuật ngữ miền nghiệp vụ) với U-N5 (cấm "bảng"); U-N7 "thường 2-6 từ".
- Gặp: nguồn dùng "bảng giá" nhưng "bảng" nằm trong danh sách cấm (nghĩa bảng CSDL). UC-022 cần 7 từ để nêu rõ đối tượng và điều kiện.
- Xử lý: đặt UC-001 là "Xem giá gói tập"; giữ UC-022 "Huỷ yêu cầu đặt buổi quá hạn" (7 từ) và ghi ở Vấn đề còn mở. Đề nghị U-N5 ghi rõ cấm "bảng" chỉ khi mang nghĩa bảng dữ liệu.

10. Sự kiện cho UC bắt buộc theo rule nhưng không có trong nguồn (Đăng nhập).
- Vị trí: Bước 2.4 "Chỉ ghi sự kiện mà nguồn nêu hoặc suy ra trực tiếp"; U-R01 "ngụ ý ... vẫn tạo UC Đăng nhập".
- Gặp: nguồn không nêu việc đăng nhập nên không có sự kiện trực tiếp, nhưng U-R01 buộc tạo UC và cột Sự kiện kích hoạt cần mã EV.
- Xử lý: tạo EV-04 "Hội viên muốn dùng các chức năng chỉ dành cho người có tài khoản" suy từ câu "mà không cần tài khoản" và "tài khoản hội viên". Prompt chưa nói UC tạo theo U-R01 lấy sự kiện từ đâu.

11. Q5 và Target không khớp về phạm vi phép thử.
- Vị trí: Q5 "Chạy bộ phép thử U-T1 đến U-T11"; Target 4 "đạt U-T1 đến U-T12"; U-T12 đã dùng ở Q2.
- Gặp: không ảnh hưởng kết quả vì không có UC nào là giao diện, nhưng người chạy không rõ có phải chạy lại U-T12 ở Q5 không.
- Xử lý: coi U-T12 đã được xét ở Q2.

12. Quá tải ngữ cảnh và trùng lặp thông tin giữa các bảng.
- Vị trí: Format Mục 2, 3, 4b, 5 đều chứa cột REQ và cột CAND/EV tham chiếu chéo.
- Gặp: đầu vào P00 dài khoảng 70 KB (96 REQ, 43 Q); đầu ra có 71 CAND, 31 EV, 28 UC, ma trận 96 dòng. Cùng một quan hệ REQ-UC-CAND-EV xuất hiện ở 4 nơi, rất dễ lệch khi viết tay.
- Xử lý: sinh Mục 5 bằng script từ cột REQ của 4b và viết script kiểm tra chéo các bảng. Nếu chạy bằng chat thường (không có script), rủi ro lệch giữa các bảng cao với hệ thống cỡ này.

13. Nhóm "Giả định" khi NGHIEM_NGAT.
- Vị trí: Conventions C5 "Giả định (chỉ khi CHE_DO_GIA_DINH = CO_NHAN)" và "Mục nào không có nội dung thì ghi 'Không có', không xoá mục".
- Gặp: hai câu hơi xung đột (mục chỉ có khi CO_NHAN, nhưng không xoá mục khi trống).
- Xử lý: giữ mục, ghi "Không có (chế độ NGHIEM_NGAT, không dùng mục này)" theo mẫu của P01.

14. Ngưỡng số UC của tác nhân thời gian và nhóm nhỏ.
- Vị trí: Phần E "chỉ 1 UC là bình thường với tác nhân thời gian"; Cột Nhóm chức năng "một nhóm chỉ có 1 UC thì cân nhắc nhập".
- Gặp: ACT-14 có 4 UC (mốc hạn khác nhau); nhóm Ra vào chi nhánh chỉ 2 UC (mức hợp lý 3-12). Prompt không nêu ngưỡng trên cho tác nhân thời gian gộp nhiều mốc hạn.
- Xử lý: giữ nguyên, ghi nhận xét ở Mục 6 theo Phần E ("không gộp hoặc tách chỉ để đạt con số").

## Mục Target không đạt

Không có mục nào ghi Không đạt. Các mục đạt có điều kiện: Target 3 (vướng mắc 6), Target 4 (vướng mắc 5 về UC thời gian; UC-001, UC-002, UC-025 miễn U-T4 theo U-R05), Target 6 (UC-022 dài 7 từ, vướng mắc 9).
