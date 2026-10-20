Model của phiên chạy: Sonnet

# Nhật ký người chạy - P13 (PKG-15, PKG-29 Lớp nhóm)

Đầu ra: gym/design/P13-data-model.md (4 bảng TBL-01 đến TBL-04), gym/design/diagrams/P13-erd-logical.drawio (XML hợp lệ). Không sinh P13-erd-conceptual.drawio vì MUC_CHI_TIET là GON. Mã Q lớn nhất sau lần chạy: Q-107 (không cấp Q mới). Script DDL đã chạy thử trên PostgreSQL 14 cục bộ (bảng member giả lập), không lỗi.

## Đọc thêm so với danh sách giao việc

- README.md: chỉ 40 dòng đầu (pipeline), để xác nhận cách chạy.
- P09-architecture.md: không đọc toàn file; dùng grep rồi đọc F7 (bảng cơ chế lưu trữ và giao dịch) và F11, các dòng F2.2 nêu PostgreSQL.
- P05-glossary.md: chỉ grep các dòng GL-05, GL-08, GL-13, GL-27, GL-28, GL-29, GL-35, GL-38.
- Quét mã Q toàn thư mục design/ bằng grep chỉ lấy mã (theo C3) và grep "TBL-" để kiểm tra chưa có P13 cũ. Có liệt kê tên file trong gym/logs/ và gym/design/ bằng ls, không mở nội dung nhật ký nào.
- yeu-cau-phong-tap.md: không đọc (không cần).

## Vướng mắc

1. Vị trí: prompt mục 2 (P12 "Phần cần đọc: F1 (cột Persistent), F1b ...") và F2 ("Cột: | DC | Persistent (Có / Không) ..."). Gặp: bảng F1b của P12 (kiểu phụ trợ) không có cột Persistent, nên không biết DC-WaitlistEntry có lưu không. Chỉ suy được từ F5 R-20 ("hiện thực qua DC-WaitlistEntry (association class dạng value object...)") và F7 DC-Waitlist.entries. Xử lý: coi value object nằm trong thuộc tính đa trị là Persistent = Không, lưu qua TBL-04; thêm Đề xuất sửa P12 F1b.

2. Vị trí: F2 "Bảng thuộc tính đa trị TBL-nn (value object Persistent = Không nằm trong thuộc tính đa trị của một lớp persistent)" so với F4.2 "Association M - N: thêm bảng trung gian ... thuộc tính của association class ... đặt ở bảng trung gian". Gặp: DC-WaitlistEntry khớp cả hai, hai quy tắc cho cùng một bảng nhưng khác tên chiến lược và khác cách điền cột Thực thể (E-) ở F2 (value object không có E-, nhưng F3.1 nói association class thành thuộc tính của mối quan hệ). Xử lý: ghi cả hai cách đọc ở F2, cột E- ghi ER-04; ghi vào Vấn đề còn mở theo C9.

3. Vị trí: prompt F6.1 "Tham chiếu FK (TBL.cột, ON DELETE, ON UPDATE)", F8.1 ("Source của cạnh là bảng cha"), F9 ("CREATE TABLE theo thứ tự bảng cha trước") và YEU_CAU_BO_SUNG của người dùng ("bảng ngoài phạm vi, không thiết kế cột"). Gặp: prompt không nói cách xử lý FK trỏ tới bảng ngoài phạm vi (member của PKG-26): không có mã TBL để ghi, ERD cần node đích, DDL không tạo được FK tới bảng chưa tồn tại, kiểu cột và tên bảng chưa có. Xử lý: ghi "member.id (bảng ngoài phạm vi, PKG-26)" thay mã TBL; vẽ node EXT-member chỉ có khoá id; kiểu UUID suy từ "định danh --> string (Thiết kế: chuỗi UUID)" của P12 F2; hai FK tới member đặt ở khối ALTER TABLE cuối script. Ghi ở Vấn đề còn mở. Đây là vướng mắc quan trọng vì mọi package có tham chiếu chéo đều gặp.

4. Vị trí: P12 F7 "DC-ClassBooking.id ... Multiplicity 0..1" và "DC-Waitlist.id 0..1" so với Bước 4 prompt "NULL/NOT NULL theo multiplicity (1 --> NOT NULL; 0..1 --> NULL)". Gặp: theo quy tắc máy móc cột id phải NULL được và là khoá chính, vô lý. Bước 4 chỉ có ngoại lệ cho "lớp chỉ được lưu từ một trạng thái trở đi", không có ngoại lệ cho thuộc tính chưa có giá trị ở đối tượng chưa lưu. Xử lý: id NOT NULL (khoá chính), giải thích ở cột mô tả theo ý P12 ("bỏ trống cho tới khi IF-14.save gán"). Đề nghị prompt thêm ngoại lệ này.

5. Vị trí: F4.2 "Association M - N: ... khoá chính là cặp hai khoá ngoại (hoặc khoá thay thế kèm UNIQUE ...)" so với Q-59 của P12 (hội viên đã có trong danh sách chờ). Gặp: khoá ghép (waitlist_id, member_id) ngầm cấm hội viên có hai mục chờ trong một danh sách, trong khi nguồn chưa trả lời Q-59 và NGHIEM_NGAT cấm tự điền. P12 F5 R-20 đã chốt "định danh bởi Waitlist + Member" nên theo P12; prompt không nói P13 xử lý thế nào khi quyết định khoá của P12 ngầm chọn một đáp án của một Q mở. Xử lý: theo P12, không cấp Q mới (Q-59 đã có), ghi ở Vấn đề còn mở.

6. Vị trí: F2 và Bước 1 so với P12 Q-84 ("Q-84 chưa chốt đối tượng riêng hay chỉ là tập mục chờ ... ghép được với cả hai câu trả lời của Q-84 khi P13 ánh xạ"). Gặp: P12 đẩy quyết định cho P13, nhưng prompt P13 không có hướng dẫn cho bảng gần như rỗng (waitlist chỉ có id và group_class_id, quan hệ 1 - 0..1). Phương án thay thế là bỏ bảng waitlist, dùng waitlist_entry(group_class_id, member_id). Xử lý: giữ bảng waitlist để một lớp một bảng, có khoá id P12 yêu cầu ("để P13 làm khoá"), ghi lý do ở F2. Quyết định này có thể bị đảo khi Q-84 có trả lời.

7. Vị trí: Bước 4 "Index theo truy vấn thực tế trong UC và NFR" và KHOI_LUONG_DU_LIEU của người dùng ("giờ cao điểm 17:00 đến 20:00"). Gặp: NFR-01 nêu đỉnh 6 giờ sáng thứ Hai (1.500 phiên đặt chỗ), khác giờ cao điểm người dùng nêu; cả hai đều không có số đo (Q-42, Q-76), không đủ để có "lý do đo được" cho phi chuẩn hoá. Xử lý: không phi chuẩn hoá (đã xét booked_count và ghi lý do), index phục vụ cả hai; ghi ở Vấn đề còn mở. Số dòng class_booking chỉ có chặn trên suy từ BR-08 (6.000 x 2 x 365), prompt không nêu cách ghi ước lượng khi nguồn thiếu.

8. Vị trí: Bước 3 "Với mỗi bảng: liệt kê phụ thuộc hàm (FD) dựa trên BR" so với BR-10 ("Sức chứa của mỗi lớp nhóm được xác định theo phòng") và Q-03. Gặp: nếu hiểu BR-10 là FD room --> capacity thì group_class vi phạm 3NF; nhưng P12 giữ capacity là thuộc tính của lớp và Q-03 hỏi sức chứa lớp bằng hay thấp hơn sức chứa phòng. Xử lý: không khẳng định FD, ghi phương án tách ở F5.2 là dự kiến chưa áp dụng. Prompt không có hướng dẫn cho FD bị phụ thuộc vào Q mở.

9. Vị trí: F4.4 "Mỗi ràng buộc phải có nguồn" và BR-36, BR-37 (trùng phòng, trùng huấn luyện viên). Gặp: ràng buộc là liên dòng cùng bảng chứ không "liên bảng", cần thời lượng lớp mà P12 không có thuộc tính nào. Xử lý: đưa vào F4.4 (C-07) với cách giữ "chưa giữ được" và dẫn Q-32, Q-03, Q-05; không đề xuất sửa P12 vì nguồn chưa chốt thời lượng.

10. Vị trí: F6.1 ví dụ chuẩn và Bước 4 "chọn kiểu theo hệ quản trị". Gặp: CONG_NGHE chỉ ghi "PostgreSQL" không có phiên bản, LOAI_CSDL "Không có"; gen_random_uuid() cần PostgreSQL 13 trở lên. Xử lý: ghi giả định phiên bản là quyết định thiết kế (C1 mục 7) ở F1 và Vấn đề còn mở, không cấp Q hay ASM.

11. Vị trí: Conventions C3 và Bước 6 prompt cho "Mã Q, ASM cuối đã cấp". Gặp: lần chạy không cấp Q mới nên không rõ mục Câu hỏi mở nên ghi thế nào (C5 "Mục nào không có nội dung thì ghi Không có", nhưng bảng Q có cột). Xử lý: một dòng "Không có" kèm danh sách Q hiện có đã trích. Không phải lỗi, chỉ là chỗ chưa rõ.

## Mục Target

Tất cả đạt. Ghi chú: Target 3, 5, 8 đạt một phần ở điểm bảng member (vướng mắc 3); Target 8 đạt một phần ở C-06, C-07 (vướng mắc 9, 8). Target 11 và ERD khái niệm không áp dụng. Target 12: ERD khớp F6 (4 bảng cộng node EXT-member, 5 FK), nét liền cho hai FK nằm trong khoá chính của waitlist_entry, nét đứt cho ba FK còn lại, đã kiểm XML bằng xml.dom.minidom; chưa mở bằng draw.io để xem bằng mắt.
