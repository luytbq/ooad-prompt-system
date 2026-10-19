Model của phiên chạy: Sonnet

# Nhật ký người chạy - P03 - Dự án gym (VietFit)

Đã đọc: P03-use-case-diagram.md, 00-Conventions.md, README.md, design/project-profile.md, yeu-cau-phong-tap.md, design/P00-problem-brief.md, design/P01-actors.md, design/P02-usecases.md (1.1), design/P02R-review.md (1.0). Không mở file nào khác trong _research/ (chỉ liệt kê tên file trong design/ và logs/).

Đã ghi: design/P03-usecase-model.md, design/diagrams/P03-usecase-overview.drawio. Kết quả: 14 tác nhân, 28 UC, 45 association (RL-01 đến RL-45), 0 include, 0 extend, 0 generalization, 1 sơ đồ (tổng quát), không có sơ đồ phân rã. Q cuối Q-49 (P03 không cấp Q mới), ASM chưa cấp. File .drawio parse được bằng xml.dom.minidom; đã đối chiếu tự động Node/Edge trong .md với mxCell (ID, nhãn, toạ độ, source, target, điểm uốn): 0 lệch.

Tự kiểm tra Target: 1 đến 15 đều Đạt. Hai mục đạt kèm điều kiện: Mục 8 (D-AP15) còn 8 cặp đường association cắt nhau (không đường nào cắt qua elip); Mục 11 vượt ngưỡng M = 14 tác nhân nhưng đúng phương án thứ hai của Bước 8. Mục 5, 6, 7, 14 đạt do không có quan hệ giữa UC nào để kiểm.

## Vướng mắc (theo mức quan trọng giảm dần)

1. Mâu thuẫn L-12 với L-10 và Conventions C7.3 về bội số của 10.
   - Vị trí: Phần D, L-12: "cột hai cách cột một 80 và lệch xuống nửa bước dòng (55)"; L-10: "mọi toạ độ là bội số của 10"; Target 13: "toạ độ bội số của 10".
   - Gặp: UC cột hai có y = y cột một + 55 thì không thể là bội số của 10. Thêm nữa, UC cao 70 có tâm dọc tận cùng 5, nên điểm uốn "tại (cạnh trái boundary + 40, tâm dọc của UC đích)" cũng không thể là bội số của 10.
   - Xử lý: dùng độ lệch 50; điểm uốn làm tròn xuống 5 đơn vị so với tâm UC. Đường đi lệch tâm 5 đơn vị vẫn nằm trong khe 40 giữa hai UC. Ghi vào Vấn đề còn mở theo C9.

2. L-12 đặt điểm uốn trùng cạnh trái UC cột một.
   - Vị trí: L-12: "điểm uốn tại (cạnh trái boundary + 40, ...)" và L-01: "lề trong tối thiểu 40".
   - Gặp: UC cột một đặt ở lề tối thiểu 40 thì cạnh trái của nó nằm đúng x = cạnh trái boundary + 40; đoạn dọc của đường nối tác nhân đi sát hoặc dọc theo cạnh các elip cột một.
   - Xử lý: dùng lề trong 80 (cột một x = 280, đoạn dọc x = 240 = cạnh trái boundary + 40, hành lang tới UC cột giữa x = 220 = cạnh trái + 20). Vẫn thoả lề tối thiểu 40.

3. Thiếu quy tắc bố cục cho đường tới tác nhân phụ khi có nhiều tác nhân phụ và nhiều đường chung điểm đầu mút.
   - Vị trí: L-12: "Đường từ UC cột một sang tác nhân phụ bên phải đi ngang qua khe của cột hai" và L-03.
   - Gặp với đề này: 5 tác nhân phụ, 14 đường UC --> tác nhân phụ; ACT-09 và ACT-10 cùng nối 4 UC (hai đường rời cùng một UC sẽ chồng lên nhau); UC-005 có 2 tác nhân chính và 2 tác nhân phụ. Prompt không nói đặt tác nhân phụ theo thứ tự nào, đường đi theo làn nào, hai đường cùng đầu mút tách nhau thế nào. Một số UC cột giữa (UC-018, UC-025) còn chắn đường ngang sang phải của các dải.
   - Xử lý: tự đặt mỗi tác nhân phụ một làn dọc trong hành lang bên phải boundary (x = 960 đến 1040), lệch hai đường cùng UC ±10, và tự viết script tìm vị trí tác nhân phụ, thứ tự dải, vị trí UC cột giữa để không đường nào cắt qua elip và ít cắt nhau (từ 41 cặp cắt xuống 8). Tính tay bố cục này với 45 đường là quá tải; nên thêm vào L-12 quy tắc làn dọc cho tác nhân phụ và quy tắc tách hai đường cùng đầu mút.

4. L-12 không nói cách xử lý tác nhân chính không có UC riêng và điểm kết thúc đường tới UC cột giữa.
   - Vị trí: L-12: "mỗi tác nhân chính bên trái một dải" và "đi ngang theo hành lang tới cột giữa, rồi tới UC".
   - Gặp: ACT-03 Khách vãng lai chỉ nối UC-018 (UC dùng chung với ACT-02), nên không có UC nào để lập dải; vị trí đặt tác nhân không có hướng dẫn. Ba UC dùng chung (UC-005 với ACT-05, UC-018 với ACT-03, UC-025 với ACT-04) đều đi cùng ACT-02, trong khi ACT-02 chỉ kề được hai dải; câu "rồi tới UC" không nói đoạn cuối đi thế nào (ngang tới tâm UC hay thêm điểm uốn).
   - Xử lý: ACT-03 đặt ở dải riêng chỉ chứa tác nhân; UC-005 đặt cột một giữa hai dải ACT-05 và ACT-02 (hành lang 150); UC-018, UC-025 đặt cột giữa; đoạn cuối đi thẳng từ điểm uốn trên hành lang tới tâm UC.

5. Xung đột giữa L-09 và L-02, L-05.
   - Vị trí: L-09: "Nếu vẫn cắt, đổi thứ tự hàng UC trước khi chấp nhận đường cắt"; L-02: "Tác nhân chính quan trọng nhất ... đặt trên cùng"; L-05: "UC sắp theo trình tự thời gian".
   - Gặp: để đường tới ACT-11 và đường tới ACT-09, ACT-10 không chồng phạm vi dọc, phải đặt ACT-05 trên ACT-02 và đưa UC-019, 020, 023 lên trước UC-006, 010, 011, 012 trong dải ACT-02. ACT-02 (11 UC, nhiều nhất) không ở trên cùng.
   - Xử lý: ACT-01 trên cùng vì gắn với UC khởi đầu quy trình (L-02 cho phép một trong hai tiêu chí); thứ tự UC trong dải ACT-02 vẫn theo luồng nghiệp vụ nhưng khối mua và đặt buổi tập cá nhân đứng trước khối lớp nhóm. Ghi vào Vấn đề còn mở. Thứ tự giữa bốn UC của ACT-14 (mốc hạn độc lập) không có căn cứ thời gian, xếp theo mã UC.

6. Chiều association ở Mục 1 mâu thuẫn với chiều vẽ khi chọn MUI_TEN_KHOI_XUONG.
   - Vị trí: Phần B Mục 1: "Association ghi nguồn là tác nhân, đích là use case"; Phần E: "source là bên khởi xướng"; Phần A: "use case --> tác nhân phụ".
   - Gặp: với tác nhân phụ, bảng Edge (nguồn = UC) và Mục 1 (nguồn = tác nhân) đảo nhau, trong khi Target 12 chỉ yêu cầu khớp bảng Node, Edge với .drawio.
   - Xử lý: Mục 1 theo Phần B, bảng Edge và .drawio theo hướng vẽ; ID RL-nn giống nhau; ghi vào Vấn đề còn mở. Nên viết rõ trong Phần B rằng cột Nguồn, Đích của Mục 1 không đổi theo KIEU_DUONG_ASSOCIATION.

7. Placeholder CACH_PHAN_RA_SO_DO mâu thuẫn nhẹ với Bước 8 và không có tác dụng khi không có quan hệ giữa UC.
   - Vị trí: placeholder: "THEO_TAC_NHAN: mỗi tác nhân chính người một sơ đồ, gồm mọi use case của tác nhân đó"; Bước 8: "Sơ đồ phân rã chỉ tạo cho nhóm (hoặc tác nhân ...) có ít nhất một quan hệ include, extend hoặc generalization giữa UC".
   - Gặp: với P02 này (UC Subfunction duy nhất là Đăng nhập, không UC nào thoả Bước 3, 4, 5) không tác nhân nào có quan hệ giữa UC, nên giá trị THEO_TAC_NHAN không tạo sơ đồ nào. Người đặt tham số có thể mong đợi sơ đồ theo tác nhân.
   - Xử lý: theo Bước 8 (không sơ đồ phân rã), ghi lý do ở Mục 4 và Vấn đề còn mở. Nên thêm vào placeholder một câu "chỉ áp dụng khi có sơ đồ phân rã".

8. Prompt không có hướng dẫn cho UC nối tiếp theo thời gian giữa các phiên và cho hành vi dùng chung mà P02 đã kết luận là bước.
   - Vị trí: Bước 3 "Không dùng include cho: vẽ trình tự ..."; Bước 4; Bước 7 "Nếu phát hiện một hành vi dùng chung ... mà P02 chưa có UC tương ứng"; Q-49 của P02 nêu "quan hệ giữa UC-012 và UC-013 (P03)".
   - Gặp: UC-011 --> UC-012 --> UC-013 và UC-020 --> UC-021 --> UC-022 nối tiếp qua phiên và tác nhân khác nhau; Bước 3 đến 5 không có loại quan hệ nào cho kiểu này. Gửi thông báo đẩy, SMS dùng chung cho 4 UC (CAND-64, CAND-65), P02 kết luận bước vì Q4 a không thoả, trong khi Bước 7 mời đề xuất UC mới cho hành vi dùng chung.
   - Xử lý: không tạo quan hệ, không đề xuất UC mới (tôn trọng "không đổi" của P02 và C1.3); lý do ghi ở Vấn đề còn mở, kèm lưu ý rà lại UC-012 và UC-013 khi Q-49 được trả lời.

9. UC Subfunction không được UC nào include (UC-004 Đăng nhập).
   - Vị trí: Bước 3 a "UC-B được P02 giữ ở mức Subfunction" và D-AP14.
   - Gặp: P02 giữ Đăng nhập là Subfunction theo U-R01 nhưng ghi "không nối include", còn Bước 3 cấm include cho "xác thực đăng nhập của mọi UC". Prompt không nói rõ đây là trường hợp Subfunction đứng riêng, nối trực tiếp tác nhân chính hợp lệ.
   - Xử lý: UC-004 chỉ nối ACT-02 (đúng cột P02), Ghi chú nút nêu lý do.

10. Quá tải ngữ cảnh và đầu vào dư.
   - Vị trí: Mục 2 và Mục 3 của prompt: đính kèm P00, P01, P02 nguyên file và tài liệu nguồn.
   - Gặp: P00 khoảng 70 KB, P02 khoảng 74 KB (một lần đọc bị cắt, phải đọc lại theo đoạn). P03 thực tế chỉ dùng bảng tác nhân P01 Mục 2, P02 Mục 4a, 4b, Mục 5 (REQ) và Mục 7; không dùng bảng ứng viên, sự kiện của P02 hay danh sách REQ của P00 ngoài việc tra loại REQ.
   - Xử lý: đọc đủ theo phạm vi cho phép. Nên ghi trong Mục 3 rằng P03 chỉ cần các mục trên, như đã làm cho P05, P06.

11. Cột REQ của association chủ quan.
   - Vị trí: Phần B Mục 1: "REQ: Association ghi các REQ nêu tác nhân đó tham gia UC".
   - Gặp: với tác nhân thời gian, tác nhân phụ và UC có nhiều REQ quy tắc, "REQ nêu tác nhân tham gia" không xác định tập duy nhất.
   - Xử lý: chọn các REQ loại Chức năng hoặc Giao tiếp ngoài gắn trực tiếp với vai trò đó (ví dụ ACT-09 với UC-011: REQ-27, REQ-88, REQ-90). Có thể khác lựa chọn của người chạy khác.

12. Nhận xét nhỏ.
   - Vị trí: Phần B "Không thêm lời dẫn" so với việc ghi chú ngắn sau bảng Mục 1 và Mục 4 khi không có quan hệ. Tôi thêm hai câu ghi chú ngắn vì Mục 2, 3 chỉ có "Không có" mà thiếu lý do; prompt không nêu chỗ ghi lý do "không có quan hệ" ngoài Vấn đề còn mở.
   - Vị trí: Target 10 "không đường nào cắt qua elip" và L-12 cuối dùng "hình chữ nhật bao". Tôi kiểm bằng hình chữ nhật bao có đệm 4 đơn vị bằng script; draw.io vẽ đường tới tâm nên phần cắt rìa bao ngoài elip không tính.
   - Vị trí: P02R-review.md vẫn ghi tên cũ của UC-005, UC-021 (Mua gói tập, Duyệt yêu cầu đặt buổi tập). Prompt không nói rõ nguồn tên chuẩn khi P02R và P02 lệch; dùng P02 1.1 theo "Chỉ dùng ... use case có trong P02".
