# Nhật ký người chạy P11a-GD2

Model: Sonnet (tham số model sonnet của công cụ Agent).

Phạm vi lần chạy: giai đoạn 2 cho 8 màn hình (SCR-01, SCR-02, SCR-03, SCR-04, SCR-05 của UC-002 và lối vào điều hướng; SCR-17, SCR-18, SCR-19 của UC-015). Đầu ra: 8 file P11a-gui/SCR-nn-slug.md. Không có file .drawio (giai đoạn 2 không sinh sơ đồ) và không có mockup HTML (XUAT_HTML là Không có). Mã cấp mới: Q-88 đến Q-91, ASM-61 đến ASM-65, MSG-40 đến MSG-43. Phạm vi đọc thực tế: toàn bộ prompt, Conventions, ui-standards.md, screen-list.md, screen-transition.md, P04 UC-002 và UC-015; P07 UC-002 và UC-015 các mục 1, 2, 3.4 và phần Câu hỏi mở; chỉ lướt P05 (tra GL), P06 (tra NFR), P10 (tra tên DC). P08, P09, P01, P02 không đọc toàn văn vì screen-list.md đã trích; kết quả không bị ảnh hưởng nhưng prompt không nói mức đọc tối thiểu.

## 1. Phạm vi "các màn hình của UC-002, UC-015" không xác định màn hình điều hướng và màn hình dùng chung

- Vị trí: mục 3 "Giai đoạn 2 (lặp, mỗi lần một nhóm màn hình, ví dụ theo use case)" và F2 "màn hình điều hướng ghi 'Điều hướng' và liệt kê UC được mở từ nó".
- Gặp phải: SCR-01 là màn hình điều hướng có cột UC là "UC-002, UC-008 (UC-001, UC-007, ... chưa có màn hình đích)". Nó thuộc UC-002 một nửa và UC-008 một nửa; nếu phiên chạy UC-008 song song cũng viết SCR-01 thì ghi đè lẫn nhau. Prompt không nói màn hình điều hướng thuộc nhóm nào.
- Xử lý: coi SCR-01 thuộc phạm vi vì cột UC có UC-002, viết đủ cả hai thẻ UC-002 và UC-008, ghi rõ phần UC-008 nằm ngoài phạm vi chạy. SCR-09 và SCR-13 không đụng tới. Đề xuất: prompt nên quy định màn hình điều hướng được viết ở lần chạy đầu tiên có use case mà nó mở, hoặc có một nhóm riêng.

## 2. Cấp mã Q, ASM, MSG khi nhiều phiên chạy song song

- Vị trí: C3 "Lần nào cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất đã thấy, rồi cấp tiếp"; F1b "mã MSG-nn theo C3, không đổi khi chạy lại".
- Gặp phải: giai đoạn 1 dừng ở Q-87, ASM-60, MSG-39. Theo yêu cầu của người giao việc, P11b cấp từ Q-100, ASM-100 nên không đụng. Nhưng giai đoạn 2 lặp theo nhóm: nếu phiên GD2 cho UC-008 hoặc UC-013 chạy song song thì cũng cấp Q-88, ASM-61, MSG-40 và trùng mã. C3 chỉ xử lý được lặp tuần tự (đọc file cùng bước đã có), không xử lý song song.
- Xử lý: cấp từ Q-88, ASM-61, MSG-40 như quy tắc. Đề xuất: ghi trong C3 hoặc prompt P11a rằng chạy GD2 song song cần chia dải mã trước.

## 3. Không có chỗ quy định để đăng ký MSG mới phát sinh ở giai đoạn 2

- Vị trí: F1b "Danh mục thông điệp" thuộc ui-standards.md (giai đoạn 1); Target 4 "Mọi thông điệp trong đặc tả có trong danh mục MSG"; C1 mục 3 "không tự sửa trong artifact của bước này ... ghi vào Đề xuất sửa artifact trước"; C3 cấp MSG cho P11a.
- Gặp phải: khi viết bảng kiểm tra dữ liệu nhập (F5f) phát sinh lỗi mà P04 không nêu và danh mục giai đoạn 1 chưa có: thiếu trường bắt buộc, ngày sai định dạng, ngày đã qua, chưa chọn chỗ, máy chưa có danh sách chuyến. Giai đoạn 2 không có file ra để ghi danh mục; sửa ui-standards.md vừa trái chỉ dẫn "chỉ ghi SCR-nn" của người giao việc vừa khó xác định có được phép hay không (cùng bước P11a nhưng là artifact đã chốt).
- Xử lý: định nghĩa MSG-40 đến MSG-42 trong SCR-02 (mục h) và MSG-43 trong SCR-17, các SCR khác dùng lại (SCR-03, SCR-17, SCR-18 dùng MSG-40 do SCR-02 định nghĩa, phụ thuộc chéo file). Ghi đề xuất hợp nhất vào ui-standards.md ở mục "Đề xuất sửa artifact trước". Mục h) không có trong khung F5 nên tôi tự thêm; đề xuất F5 bổ sung quy tắc "thông điệp mới phát sinh ở giai đoạn 2".

## 4. F5e và Target 7 mâu thuẫn với C1 mục 7 về độ dài trường

- Vị trí: F5e "không tự đặt độ dài, miền giá trị khi nguồn không nêu, ghi Q-nn hoặc ASM-nn"; Target 7 "không có độ dài ... tự đặt không có mã Q hoặc ASM"; C1 mục 7 "độ dài cột ... là quyết định thiết kế, ... không cần Q-nn hay ASM-nn" (từ P09 trở đi).
- Gặp phải: Họ tên người đi, Mã vé, Giá vé, Mã chỗ không có độ dài trong P04. Tính là kỹ thuật thì C1.7 cho tự chọn; tính là dữ liệu thì F5e bắt hỏi.
- Xử lý: Họ tên 100 ký tự ghi là "quyết định thiết kế (C1.7)" và trỏ Q-32 đã có (giới hạn nghiệp vụ). Mã vé, giá vé, mã chỗ không đặt giới hạn, ghi "-" và Q-90 cho mã vé. Chưa rõ ràng: đề xuất prompt nói rõ độ dài trường hiển thị nằm theo C1.7 hay F5e.

## 5. F5d: tập Thao tác không chứa sự kiện hệ thống và thiết bị

- Vị trí: F5d "Thao tác (Operation: Khởi tạo, Nhấn, Chọn, Nhập, Rời trường, Nhấn đúp)".
- Gặp phải: đồng hồ giữ chỗ hết hạn (SCR-04), đầu quét đưa mã vào ô (SCR-18), nút Back của hệ điều hành, phím Enter không khớp tập. Quy tắc "mỗi nút có dòng Nhấn" và "Khởi tạo mô tả nội dung khi mở màn hình" không bao quát sự kiện thời gian.
- Xử lý: đồng hồ dùng "Khởi tạo" và mô tả hết hạn trong cột Chức năng; đầu quét và Enter dùng "Nhập"; Back dùng "Nhấn". Đề xuất mở rộng tập Thao tác (Hết thời gian, Quét).

## 6. F5e: cột "Số ký tự tối đa" không có giá trị cho trường kiểu danh sách, tiền, giờ

- Vị trí: F5e "Số ký tự tối đa (Number of digits)".
- Gặp phải: trường chọn từ danh sách, tiền, kết quả hai giá trị không có số ký tự có nghĩa.
- Xử lý: dùng "-" kèm lý do trong ngoặc, hoặc độ dài suy ra từ định dạng (ngày 10, ngày giờ 16, số vé tối đa 2 chữ số vì xe tối đa 40 chỗ). Chưa có quy ước.

## 7. F7 mức DAY_DU: khối lượng và khả năng đánh giá hình thức

- Vị trí: F7 "Dòng cho tiêu chí Đạt và Không áp dụng (chỉ khi DAY_DU): ghi thêm để bảng phủ mọi tiêu chí" và A6 "Đánh giá từng màn hình".
- Gặp phải: câu "chỉ khi DAY_DU" đặt ngay sau "Không áp dụng" nên không rõ nó chỉ áp cho Không áp dụng hay cho cả Đạt. Mỗi màn hình có 10 Nielsen + 8 Shneiderman + 24 WCAG + 2 nền tảng + 7 Baymard = 51 dòng nên 8 màn hình có 408 dòng. Thực tế phần lớn bằng chứng là trỏ về quy định STT của ui-standards.md và chỉ một số dòng có bằng chứng riêng của màn hình. Khả năng đây là đánh giá hình thức cao, một người đọc khó phân biệt dòng nào đã thực sự kiểm.
- Xử lý: sinh bảng bằng script với một bộ bằng chứng chung cho web và cho Android rồi ghi đè bằng bằng chứng riêng ở các dòng có đặc thù; mỗi màn hình đủ 51 dòng. Các dòng "Vi phạm đã sửa" (SCR-02 Nielsen 5, SCR-03 Nielsen 8, SCR-17 Nielsen 5, SCR-18 Nielsen 8) là các quyết định tôi đã đổi khi thiết kế; phần "bản nháp" mô tả cách tôi nghĩ ban đầu, không phải một bản nháp đã lưu. Đề xuất: yêu cầu F7 gộp tiêu chí Đạt dùng chung nhiều màn hình, hoặc cho phép bảng chung như screen-list.md giai đoạn 1 đã làm.

## 8. Đầu vào không khớp đầu ra: P04 thiếu dữ liệu cho một số nội dung màn hình

- Vị trí: A4 "Mọi thông tin hiển thị và mọi trường nhập truy được về bảng dữ liệu vào ra, luồng sự kiện hoặc trách nhiệm boundary. Không thêm trường, nút, chức năng ngoài đặc tả."
- Gặp phải:
  - SCR-04: P04 UC-002 không có Dữ liệu ra cho bước 8-10 (chỗ, người đi, tổng tiền, thời gian giữ chỗ còn lại). Xử lý ASM-62.
  - SCR-18: Dữ liệu ra 1 (số vé đã soát) chỉ nêu ở bước 2, số liệu sẽ đứng yên suốt phiên. Xử lý ASM-64 (cập nhật sau mỗi vé hợp lệ).
  - SCR-02: Dữ liệu vào 1 có điều kiện hợp lệ nhưng luồng không có bước kiểm tra (P07 UC-002 đã nêu); phải bịa MSG-40 đến MSG-42.
  - SCR-18: bước 3a "Nhập mã vé ... Tiếp tục bước 5" không nêu điều khiển gửi mã nên tôi thêm nút "Kiểm tra mã vé" (cũng có Enter); nút này không có trong P04, chỉ suy ra từ bước 3a.
  - SCR-03: không có hành vi khi hành khách không chọn chỗ nào.
  - SCR-19: lối ra sau khi xem kết quả không có (xem mục 9).
  - SCR-17: P04 không nêu trường hợp máy chưa có danh sách (Q-85 đã mở) nên phải ASM-63.
- Xử lý: mỗi chỗ đều có mã ASM hoặc Q và đề xuất sửa P04. Target 3 vì thế chỉ đạt một phần: nút "Chọn ngày", "Kiểm tra mã vé", bộ đếm chỗ đã chọn, đồng hồ tiến độ là điều khiển trình bày hoặc suy ra, không có dòng nguồn trực tiếp.

## 9. Quy định giai đoạn 1 không khớp với màn hình cụ thể

- STT 42 (Esc đóng hộp bằng nút phụ) với hộp MSG-10 chỉ có một nút dẫn tới SCR-02 (luồng 9a2 buộc chuyển SCR-02, E-06). Xử lý: Esc không có tác dụng ở hộp này, ghi mâu thuẫn C9 và đề nghị thêm ngoại lệ.
- STT 32 (kiểm tra khi rời trường) với ô mã vé ở SCR-18 luôn giữ tiêu điểm cho đầu quét (STT 67). Xử lý: không kiểm tra khi rời trường, kiểm tra khi gửi; ghi Baymard "Vi phạm còn mở" cho tiêu chí kiểm tra khi rời trường.
- STT 32 (kiểm tra tại giao diện trước rồi gửi) với Q-34 (thứ tự báo lỗi 6a trước 7a): giao diện báo lỗi thông tin người đi trước MSG-06 khi cùng lúc có cả hai. Ghi ở Vấn đề còn mở của SCR-03.
- STT 65 (thay thế mục lịch sử) chỉ nêu web; STT 69 không nêu Back ở SCR-19; screen-transition.md không có cạnh hay điều khiển ra khỏi SCR-19 (ghi "bắt đầu phiên mới từ SCR-17"). Xử lý ASM-65 (Back về SCR-17) và đề nghị sửa STT 65, 69 và screen-transition.md.
- Menu theo STT 35 và 38 xuất hiện ở mọi màn hình web và dẫn tới màn hình đầu của use case khác, nhưng sơ đồ dịch chuyển chỉ có cạnh E-02, E-07 từ SCR-01; STT 39 chỉ miễn vẽ cạnh cho liên kết tên hệ thống. Xử lý: coi menu là điều hướng chung giống STT 39 (ghi ở SCR-01 và các file khác); hành vi chỗ đang giữ khi rời màn hình bằng menu không đặc tả: Q-89.
- Prompt F3 ("Cạnh quay lại màn hình trước chỉ vẽ khi ... chuẩn A1 quy định rõ") và STT 65 không mâu thuẫn nhưng hai thứ phải đọc song song mới ra kết quả; chi tiết nên gom về một chỗ.

## 10. Dữ liệu mẫu và hình ảnh

- Vị trí: A4 "Dữ liệu mẫu ... đúng nghiệp vụ", F4 "Khung dây dạng văn bản".
- Gặp phải: P04 chỉ cho ví dụ giường nằm 40 chỗ với giá 360.000 đ; chuyến thứ hai (22:30), vé SV0000124, bố cục lưới 40 chỗ (A01-A20, B01-B20 với 12 chỗ trống) là dữ liệu tôi dựng, không có trong nguồn. Tổng hợp đã kiểm: 2 x 360.000 = 720.000; 36 - 35 = 1; 12 chỗ trống đếm đúng trên lưới. Bố cục lưới không có nguồn: Q-88 và ASM-61.
- Khung dây ký tự đơn dòng khó biểu diễn trạng thái (lỗi, hộp thoại, trạng thái rỗng); mỗi màn hình chỉ vẽ một trạng thái chính cộng một hoặc hai biến thể bằng khung phụ. Prompt không nói số trạng thái tối thiểu.
- Căn lề khung dây phải căn bằng script vì chữ có dấu; cần đếm theo ký tự NFC. Không phải lỗi prompt, chỉ ghi lại để người chạy khác không căn bằng tay.

## 11. Khung C5 và F5a trùng nhau; tiêu đề file

- Vị trí: F (mở đầu) "Mỗi file theo khung C5 ... Tiêu đề: '# P11a - <Tên file> - <Tên hệ thống>'" và F5a "Bảng đầu trang: Tên hệ thống, Mã và tên màn hình, Ngày tạo, ...".
- Gặp phải: có hai bảng đầu trang chồng nhau (bảng Thuộc tính/Giá trị của C5 và bảng 6 cột F5a) với THONG_TIN_TAI_LIEU là Không có nên hầu hết ô F5a để trống. "<Tên file>" của một đặc tả màn hình không xác định (tên file là slug tiếng Anh). Xử lý: tiêu đề "# P11a - SCR-nn <Tên màn hình tiếng Việt> - <Tên hệ thống>", giữ cả hai bảng; F5a ô Ngày tạo, Người duyệt, Người kiểm tra, Người phụ trách để trống.
- Mục h) "Thông điệp mới" tôi thêm sau mục g) (xem mục 3); thứ tự C5 yêu cầu các mục kiểm soát ở cuối nên h) đặt trước Câu hỏi mở.

## 12. Mức đạt các mục Target cho 8 màn hình

- Target 1, 2, 5: thuộc giai đoạn 1, không đánh giá lại ở lần chạy này.
- Target 3: đạt một phần (xem mục 8). Mọi điều khiển còn lại đều có cột Nguồn.
- Target 4: đạt cho MSG của UC-002 (MSG-04 đến MSG-14) và UC-015 (MSG-33 đến MSG-39) trong phạm vi; MSG-15 đến MSG-32 thuộc UC-008, UC-013. MSG-40 đến MSG-43 mới chưa có trong danh mục (đề xuất sửa).
- Target 6: đạt (8/8 màn hình có hình ảnh, bảng điều khiển, bảng thuộc tính trường, bảng kiểm tra dữ liệu nhập; màn hình không có trường ghi một dòng "Không có").
- Target 7: đạt có điều kiện (Họ tên 100 ký tự ghi Q-32; mã vé và giá vé không đặt giới hạn).
- Target 8: đạt (đã kiểm các phép cộng).
- Target 9: không còn vi phạm WCAG AA chưa có cách xử lý; còn "Vi phạm còn mở" ở Nielsen 3, Nielsen 10, Shneiderman hoàn tác, Shneiderman người dùng làm chủ (SCR-18, SCR-04) và Baymard kiểm tra khi rời trường (SCR-18), mỗi dòng đã có Q-86, Q-87, Q-89 hoặc ghi ngoại lệ.
- Target 10: đạt về tên, mã SCR, bước UC, cạnh E-nn so với screen-list.md và screen-transition.md; điểm lệch duy nhất là lối ra của SCR-19 (ASM-65) và menu điều hướng chung.
- Target 11: không áp dụng ở lần chạy này (không có .drawio, không có mockup).
- Target 12: C2 (không em dash, không mũi tên Unicode, đã kiểm bằng grep), C5 (đủ các mục kiểm soát ở cuối), C6 (không còn placeholder) đạt.

## 13. Không kiểm được bằng công cụ

- Tương phản màu chỉ dùng lại các cặp đã tính ở ui-standards.md STT 18, không tính lại.
- Chưa mở khung dây bằng trình duyệt hay bản dựng thật nên các kích thước (44 px, 48 dp) là quy định, không đo trên hình.
