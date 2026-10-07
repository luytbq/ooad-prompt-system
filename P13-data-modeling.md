# P13 - Mô hình hoá dữ liệu (Data Modeling)

## 1. Mục đích

Bước này thiết kế cơ sở dữ liệu cho các lớp persistent đã chốt ở P12 qua ba mức: mô hình khái niệm (ER, độc lập hệ quản trị CSDL), mô hình logic (quan hệ hoặc tài liệu/NoSQL, phụ thuộc loại hệ quản trị) và mô hình vật lý (bảng, cột, kiểu, khoá, ràng buộc, index của hệ quản trị cụ thể). Bước này ánh xạ lớp, quan hệ và kế thừa sang cấu trúc lưu trữ, chuẩn hoá tới 3NF (BCNF khi cần) và ghi rõ mọi chỗ phi chuẩn hoá có chủ đích. Đầu ra là nguồn cho lập trình tầng truy cập dữ liệu, cho X1 (review) và X2 (dữ liệu kiểm thử).

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md | Có | Hệ quản trị CSDL trong CONG_NGHE, quy ước đặt tên, chế độ giả định |
| Đầu vào | P12-class-design.md (hoặc P12-class-design/*.md) | Có | Lớp persistent, thuộc tính, quan hệ, generalization, state machine |
| Đầu vào | P06-supplementary-spec.md | Có | BR (ràng buộc dữ liệu), NFR (hiệu năng, khối lượng, lưu trữ, bảo mật) |
| Đầu vào | P04-uc-specs/*.md | Có | Bảng dữ liệu vào/ra (độ dài, định dạng, bắt buộc), truy vấn tìm kiếm trong luồng |
| Đầu vào | P09-architecture.md | Có | Cơ chế lưu trữ (persistence) đã chọn, phân tán dữ liệu |
| Đầu vào | P05-glossary.md | Không | Tên bảng, cột nhất quán với thuật ngữ |
| Đầu ra | P13-data-model.md | Có | Mô hình khái niệm, logic, vật lý, chuẩn hoá, ánh xạ lớp - bảng |
| Đầu ra | diagrams/P13-erd-logical.drawio | Có | ERD mức logic/vật lý (bảng, cột, khoá, quan hệ) |
| Đầu ra | diagrams/P13-erd-conceptual.drawio | (chỉ khi DAY_DU) | ER diagram mức khái niệm (ký pháp Chen) |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, P12 và các file đầu vào ở bảng trên.
- Chạy một lần cho toàn hệ thống (mô hình dữ liệu cần nhìn tổng thể để tránh trùng bảng). Khi hệ thống rất lớn, có thể chạy theo nhóm package có dữ liệu liên quan, lần sau đính kèm P13 đã có.
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| LOAI_CSDL | Tuỳ chọn | Loại và hệ quản trị CSDL, khi khác hoặc chi tiết hơn CONG_NGHE trong hồ sơ |
| QUY_UOC_CSDL | Tuỳ chọn | Quy ước đặt tên bảng, cột, khoá, chiến lược khoá chính |
| KHOI_LUONG_DU_LIEU | Tuỳ chọn | Ước lượng số bản ghi, tần suất truy vấn để quyết định index và phi chuẩn hoá |
| SINH_DDL | Tuỳ chọn | Có sinh script tạo bảng hay không |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù khác |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md và các artifact đã chốt: P12 (bắt buộc), P06, P04, P09, P05 (những file có đính kèm).
Đọc hồ sơ dự án để biết CONG_NGHE (hệ quản trị CSDL), NGON_NGU_TEN_PHAN_TU (quy ước tên bảng, cột), CHE_DO_GIA_DINH, MUC_CHI_TIET.
Loại CSDL và hệ quản trị:
{{PH:LOAI_CSDL | Hướng dẫn: [TUỲ CHỌN] ghi loại (quan hệ / tài liệu NoSQL / kết hợp) và hệ quản trị cụ thể nếu khác hoặc chi tiết hơn CONG_NGHE; dùng CONG_NGHE thì thay cả khối bằng "Không có"; hồ sơ còn "Chưa chốt" thì AI dùng hệ quản trị ở P09 mục F2.2, F11 | Ví dụ: "Quan hệ, PostgreSQL 16"; "Tài liệu, MongoDB 7, riêng nhật ký giao dịch dùng PostgreSQL"; "Quan hệ, MySQL 8 InnoDB"}}
Quy ước CSDL của dự án:
{{PH:QUY_UOC_CSDL | Hướng dẫn: [TUỲ CHỌN] quy ước tên bảng (số ít/số nhiều, snake_case), tên khoá chính, khoá ngoại, ràng buộc, index; chiến lược khoá chính (khoá tự nhiên hay khoá thay thế tự tăng/UUID); cột kỹ thuật bắt buộc; dùng mặc định thì thay cả khối bằng "Không có" | Ví dụ: "Bảng số ít snake_case; PK tên id kiểu BIGINT tự tăng; FK tên <bang>_id; mọi bảng có created_at, updated_at"; "Khoá chính UUID; tên ràng buộc pk_<bang>, fk_<bang>_<bang_cha>, uq_<bang>_<cot>, ix_<bang>_<cot>"}}
Khối lượng dữ liệu và tải:
{{PH:KHOI_LUONG_DU_LIEU | Hướng dẫn: [TUỲ CHỌN] ước lượng số bản ghi của các bảng lớn và truy vấn thường xuyên, nếu NFR ở P06 chưa nêu; không có thì thay cả khối bằng "Không có" | Ví dụ: "Khoảng 2.000 lịch hẹn mỗi ngày, lưu 3 năm; lễ tân tra lịch theo bác sĩ và ngày liên tục"; "50.000 mã hàng, 5 kho, khoảng 3.000 phiếu xuất mỗi ngày"}}
Sinh script DDL:
{{PH:SINH_DDL | Hướng dẫn: [TUỲ CHỌN] "Có" để sinh script CREATE TABLE/INDEX theo hệ quản trị đã chốt (hoặc lệnh tạo collection, validator, index với NoSQL); không cần thì thay cả khối bằng "Không có" | Ví dụ: "Có, cú pháp PostgreSQL"; "Không"}}

[Role]
Bạn là chuyên gia thiết kế cơ sở dữ liệu, thành thạo mô hình ER (Chen), mô hình quan hệ và lý thuyết chuẩn hoá (Codd, Date), ánh xạ đối tượng - quan hệ (Fowler, Ambler), mô hình tài liệu NoSQL (aggregate, embed và reference), và tối ưu vật lý (kiểu, ràng buộc, index).

[Action]
Bước 0. Kiểm tra đầu vào và chốt loại CSDL.
- Kiểm tra placeholder theo Conventions C6.
- Xác định loại CSDL từ LOAI_CSDL, nếu không có thì từ CONG_NGHE. Nếu CONG_NGHE còn "Chưa chốt": dùng hệ quản trị trong phương án công nghệ của P09 (mục F2.2, F11) và ghi vào Vấn đề còn mở "Hồ sơ chưa cập nhật theo P09". Chỉ khi không có P09 hoặc P09 không nêu CSDL: lập bảng so sánh quan hệ và tài liệu theo NFR (tính nhất quán giao dịch nhiều đối tượng, truy vấn đột xuất/báo cáo, cấu trúc dữ liệu thay đổi, khả năng mở rộng), đề xuất một phương án; ở NGHIEM_NGAT ghi thành câu hỏi mở kèm đề xuất và tiếp tục với phương án đề xuất; ở CO_NHAN ghi ASM.
- Lập danh sách lớp có Persistent = Có trong P12. Lớp persistent là lớp có đối tượng phải tồn tại sau khi chương trình kết thúc (thường là entity). Liệt kê lớp không persistent để khẳng định đã xét.

Bước 1. Mô hình khái niệm (ER).
- Mỗi lớp persistent là một ứng viên thực thể. Lớp giá trị (value object) không thành thực thể riêng mà thành thuộc tính phức hợp của thực thể chứa nó. Enumeration thành miền giá trị của thuộc tính.
- Thuộc tính của thực thể lấy từ thuộc tính của lớp (bỏ thuộc tính derived không lưu, bỏ thuộc tính chỉ có ý nghĩa khi chạy chương trình).
- Chọn định danh (khoá) cho mỗi thực thể; nếu lớp không có thuộc tính định danh tự nhiên duy nhất, ghi thực thể dùng định danh thay thế.
- Mỗi association, aggregation, composition giữa hai lớp persistent là một mối quan hệ; ghi bản số (1:1, 1:N, M:N) và tính bắt buộc tham gia (từ multiplicity). Association class hoặc thuộc tính gắn với cặp đối tượng thành thuộc tính của mối quan hệ.
- Composition cho ra thực thể yếu (bộ phận phụ thuộc toàn thể về định danh và vòng đời) khi bộ phận không có định danh riêng.

Bước 2. Mô hình logic.
Với CSDL quan hệ:
- Mỗi thực thể thành một quan hệ (bảng); mỗi dòng của bảng là một đối tượng; mỗi cột tương ứng một thuộc tính persistent.
- Ánh xạ quan hệ giữa lớp theo bảng quy tắc ở [Format] F4.2; ánh xạ generalization theo F4.3.
- Thuộc tính đa trị (tập hợp giá trị đơn) thành bảng riêng; thuộc tính phức hợp (value object) thành nhiều cột có tiền tố chung hoặc bảng riêng nếu dùng chung.
- Ghi khoá chính, khoá ngoại, khoá ứng viên khác (UNIQUE).
Với CSDL tài liệu (NoSQL):
- Xác định aggregate: nhóm đối tượng được đọc, ghi và bảo đảm nhất quán cùng nhau; mỗi aggregate thường là một tài liệu trong một collection. Gốc aggregate thường là entity có composition tới các bộ phận.
- Với mỗi quan hệ quyết định nhúng (embed) hay tham chiếu (reference) theo F7.
Với kết hợp: ghi rõ dữ liệu nào nằm ở loại CSDL nào và lý do.

Bước 3. Chuẩn hoá (CSDL quan hệ).
- Với mỗi bảng: liệt kê phụ thuộc hàm (FD) dựa trên BR và ngữ nghĩa dữ liệu, không dựa trên dữ liệu mẫu.
- Kiểm tra lần lượt 1NF, 2NF, 3NF; kiểm tra BCNF khi bảng có nhiều khoá ứng viên chồng lấn. Tách bảng khi vi phạm, ghi quá trình tách.
- Phi chuẩn hoá chỉ khi có lý do đo được (NFR hiệu năng với khối lượng dữ liệu cụ thể) hoặc lý do ngữ nghĩa (giữ giá trị lịch sử); mỗi chỗ phi chuẩn hoá ghi cơ chế giữ nhất quán.

Bước 4. Mô hình vật lý.
- Chọn kiểu cột theo hệ quản trị (F6.2), độ dài lấy từ điều kiện hợp lệ ở P04 hoặc BR. Thiếu căn cứ thì độ dài cột là quyết định thiết kế theo Conventions C1 mục 7: chọn giá trị và ghi "Thiết kế: <lý do>" ở cột CHECK / mô tả (chuẩn như RFC 5321 cho email, E.164 cho số điện thoại, mặc định của nền tảng, độ dài dự phòng cho tên người), không cần Q hay ASM. Chỉ khi độ dài hoặc định dạng mang nghĩa nghiệp vụ (mã phiếu đúng 10 ký tự theo quy định của tổ chức, số lẻ thập phân của đơn giá) mà nguồn không nêu mới ghi Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN).
- NULL/NOT NULL theo multiplicity (1 --> NOT NULL; 0..1 --> NULL); DEFAULT theo giá trị mặc định ở P12; CHECK theo ràng buộc P12, BR và tập giá trị enumeration; UNIQUE cho khoá ứng viên; FK với hành vi ON DELETE/ON UPDATE theo loại quan hệ.
- Index theo truy vấn thực tế trong UC và NFR (F6.3).
- Nếu SINH_DDL là "Có", sinh script theo hệ quản trị đã chốt, thứ tự tạo bảng cha trước bảng con.

Bước 5. ERD.
- Lập bảng mô hình Node/Edge, sau đó sinh file .drawio (F8). ER khái niệm (chỉ khi DAY_DU).

Bước 6. Truy vết và tự kiểm tra.
- Mọi thuộc tính persistent của P12 có cột (hoặc trường tài liệu) tương ứng hoặc lý do không lưu; mọi cột có nguồn.
- Chạy [Target], sửa những gì sửa được, ghi phần còn lại vào "Vấn đề còn mở".
- Phát hiện sai ở P12 (ví dụ multiplicity mâu thuẫn BR, thiếu thuộc tính định danh) ghi vào "Đề xuất sửa artifact trước", không tự sửa P12.

[Format]
Đầu ra là file P13-data-model.md theo khung Conventions C5 gồm các mục F1 đến F9 theo thứ tự, sau đó là các mục kiểm soát (Câu hỏi mở, Giả định nếu CO_NHAN, Đề xuất sửa artifact trước, Vấn đề còn mở).

Quy ước chung:
- Mã bảng/collection: TBL-nn theo Conventions C3, cấp tuần tự, không đổi khi chạy lại. Tên bảng, cột theo QUY_UOC_CSDL hoặc NGON_NGU_TEN_PHAN_TU (mặc định snake_case, tiếng Anh, tên bảng số ít).
- Chiến lược khoá chính mặc định khi QUY_UOC_CSDL không nêu: bảng của thực thể độc lập dùng khoá thay thế (surrogate) tên id, kiểu theo kiểu của thuộc tính định danh trong P12 (ví dụ P12 chốt định danh UUID thì dùng UUID); P12 không có thuộc tính định danh thì dùng BIGINT tự tăng; khoá tự nhiên (mã hàng, số phiếu, email) giữ ràng buộc UNIQUE; bảng bộ phận của composition và bảng trung gian dùng khoá ghép có chứa khoá ngoại tới bảng cha. Khoá tự nhiên chỉ làm khoá chính khi chắc chắn không đổi và ngắn; ghi lý do.
- Mã thực thể khái niệm: E-<TenThucThe>; mã mối quan hệ khái niệm: ER-nn. Mã ràng buộc khoá ngoại dùng làm ID cạnh ERD: fk_<bang_con>_<bang_cha> (thêm hậu tố khi có nhiều FK giữa cùng hai bảng).
- Tham chiếu nguồn: DC-<Lop>.<thuocTinh> cho cột; R-nn cho quan hệ từ P12.

F1. Quyết định loại CSDL
Bảng: | Hạng mục | Quyết định | Căn cứ (NFR / P09 / CONG_NGHE) |
Gồm: loại CSDL, hệ quản trị, chiến lược khoá chính, quy ước tên, phạm vi dữ liệu mỗi loại (khi kết hợp).
- Lỗi thường gặp: chọn NoSQL chỉ vì "hiện đại" trong khi nghiệp vụ cần giao dịch nhiều đối tượng (trừ tồn nhiều mặt hàng và ghi phiếu xuất trong một giao dịch); chọn quan hệ nhưng lưu JSON cho mọi thứ.

F2. Bảng lớp persistent và chiến lược ánh xạ
Cột: | DC | Persistent (Có / Không) | Thực thể (E-) | TBL | Chiến lược | Lý do |
- Chiến lược: "Một lớp - một bảng"; "Nhúng vào TBL-nn" (value object, bộ phận nhúng); "Single table", "Class table", "Concrete table" (kế thừa, xem F4.3); "Tài liệu gốc aggregate"; "Nhúng trong tài liệu TBL-nn".
- Lớp Persistent = Không: ghi lý do (control, boundary, lớp tiện ích, dữ liệu chỉ tồn tại trong phiên).
- Lỗi thường gặp: tạo bảng cho lớp control hoặc boundary; bỏ sót lớp persistent; tạo bảng cho enumeration mà không có nhu cầu quản lý danh mục (khi tập giá trị cố định, dùng CHECK là đủ; khi người dùng được thêm giá trị, dùng bảng danh mục).

F3. Mô hình khái niệm (ER)
F3.1. Thực thể: | E | Tên thực thể | Mô tả | Định danh | Thuộc tính (đánh dấu: định danh, phức hợp, đa trị, dẫn xuất) | Thực thể yếu (Có / Không) | Nguồn DC |
F3.2. Mối quan hệ: | ER | Tên mối quan hệ (động từ) | Thực thể A | Thực thể B | Bản số (1:1 / 1:N / M:N) | Tham gia A, B (bắt buộc / tuỳ chọn) | Thuộc tính của mối quan hệ | Nguồn R (P12) |
- Định nghĩa: mô hình khái niệm biểu diễn cấu trúc thông tin của thế giới thực một cách tự nhiên, không chịu ràng buộc của hệ quản trị CSDL. Ba thành phần: thực thể, mối quan hệ, thuộc tính.
- Quy tắc: tên thực thể là danh từ số ít; tên mối quan hệ là động từ đọc được theo chiều A - B ("Độc giả mượn Bản sách"); không có khoá ngoại, không có kiểu dữ liệu vật lý ở mức này.
- Mức hợp lý: mỗi lớp persistent (không phải value object) tương ứng một thực thể; mọi association giữa lớp persistent có một mối quan hệ; M:N có thuộc tính thì thuộc tính nằm ở mối quan hệ.
- Lỗi thường gặp: đưa cột khoá ngoại vào thực thể ở mức khái niệm; biến mọi quan hệ M:N thành thực thể ngay ở mức khái niệm khi chưa có thuộc tính riêng (được phép, nhưng làm mất ý nghĩa khái niệm); mối quan hệ đặt tên danh từ.
- Ví dụ đúng (thư viện): | ER-02 | mượn | E-Reader | E-BookCopy | M:N | Reader tuỳ chọn, BookCopy tuỳ chọn | loanDate, dueDate, returnDate | R-04 |
- Ví dụ sai: | ER-02 | Loan | E-Reader | E-BookCopy | 1:N | | reader_id | Sai: tên danh từ, bản số sai (một bản sách qua thời gian được nhiều độc giả mượn), có cột khoá ngoại ở mức khái niệm.

F4. Mô hình logic (CSDL quan hệ)
F4.1. Lược đồ quan hệ: | TBL | Tên bảng | Lược đồ (PK ghi trước, đánh dấu PK:, FK:) | Khoá ứng viên khác | Nguồn (E / DC) |
Ví dụ: | TBL-05 | stock_issue_line | stock_issue_line(PK: issue_id FK, PK: line_no, product_id FK, quantity) | (issue_id, product_id) | E-StockIssueLine / DC-StockIssueLine |

F4.2. Ánh xạ quan hệ giữa lớp: | R (P12) | Loại | Multiplicity | Cách ánh xạ | FK hoặc bảng trung gian | Kiểu quan hệ dữ liệu (phụ thuộc / độc lập) | ON DELETE |
Quy tắc ánh xạ:
- Association 1 - N (kể cả 0..1 - N): khoá ngoại đặt ở bảng phía N, tham chiếu khoá chính bảng phía 1. Khoá ngoại không thuộc khoá chính --> quan hệ độc lập (non-identifying, nét đứt trong ERD). Phía 1 bắt buộc --> FK NOT NULL; tuỳ chọn (0..1) --> FK cho phép NULL. ON DELETE mặc định RESTRICT (không xoá cha khi còn con); SET NULL chỉ khi phía cha tuỳ chọn và BR cho phép.
- Association 1 - 1: khoá ngoại đặt ở bảng phía tuỳ chọn (hoặc phía phụ thuộc) và có UNIQUE; nếu hai phía bắt buộc và luôn được đọc cùng nhau, cân nhắc gộp thành một bảng; nếu một phía ít dùng và lớn, giữ bảng riêng dùng chung khoá chính (PK của bảng phụ đồng thời là FK).
- Lớp có định danh do hai lớp cha xác định (P12 ghi "từ association class", ví dụ tồn của một mặt hàng tại một kho): ánh xạ như bảng trung gian, khoá chính là cặp khoá ngoại (quan hệ phụ thuộc, nét liền), ON DELETE RESTRICT nếu dữ liệu có giá trị nghiệp vụ cần giữ.
- Association M - N: thêm bảng trung gian chứa hai khoá ngoại tham chiếu hai bảng; khoá chính là cặp hai khoá ngoại (hoặc khoá thay thế kèm UNIQUE trên cặp khoá ngoại khi cùng một cặp được xuất hiện nhiều lần theo thời gian); thuộc tính của association class hoặc của mối quan hệ đặt ở bảng trung gian.
- Composition: bộ phận phụ thuộc toàn thể; khoá ngoại tới bảng toàn thể nằm trong khoá chính của bảng bộ phận --> quan hệ phụ thuộc (identifying, nét liền trong ERD); ON DELETE CASCADE để hiện thực việc xoá toàn thể kéo theo bộ phận.
- Aggregation: ánh xạ bằng khoá ngoại; có thể là quan hệ phụ thuộc (FK trong PK) như composition nhưng không CASCADE khi bộ phận dùng chung; được phép ánh xạ thành quan hệ độc lập (FK ngoài PK) để khoá chính đơn giản khi bộ phận có định danh riêng.
- Chiều điều hướng trong P12 không ảnh hưởng vị trí khoá ngoại: khoá ngoại luôn nằm ở phía N (hoặc ở bảng trung gian).
- Dependency trong P12 không ánh xạ thành khoá ngoại.
Ví dụ đúng:
- Giao đồ ăn: | R-03 | Composition | Order 1 - 1..* OrderLine | FK trong PK bảng con | order_line(PK: order_id FK, PK: line_no) | phụ thuộc | CASCADE |
- Khách sạn: | R-11 | Association | Reservation 0..* - Room 1 | FK ở bảng phía N | reservation.room_id NOT NULL | độc lập | RESTRICT |
- Thư viện: | R-15 | Association | Book M - N Author | Bảng trung gian | book_author(PK: book_id FK, PK: author_id FK, author_order) | độc lập với mỗi bảng cha | CASCADE ở bảng trung gian |
Ví dụ sai:
- Đặt cột list_of_line_ids trong bảng order: vi phạm 1NF, không có ràng buộc toàn vẹn.
- Đặt FK room.reservation_id: sai phía (một phòng có nhiều đặt phòng theo thời gian).
- Composition Order - OrderLine với ON DELETE RESTRICT: không hiện thực được ngữ nghĩa bộ phận chết cùng toàn thể.

F4.3. Ánh xạ generalization: | Cây kế thừa (lớp cha - các lớp con) | Chiến lược | Bảng | Cột phân biệt loại | Lý do chọn |
Ba chiến lược:
- Class table (mỗi lớp một bảng, dữ liệu chuẩn hoá): bảng lớp cha chứa thuộc tính chung; mỗi lớp con một bảng chứa thuộc tính riêng, khoá chính đồng thời là khoá ngoại tới bảng cha. Ưu: không dư thừa, thêm lớp con không đổi bảng cha, ràng buộc NOT NULL riêng từng lớp con được. Nhược: đọc một đối tượng cần join.
- Concrete table (mỗi lớp cụ thể một bảng, lặp thuộc tính và quan hệ kế thừa, dữ liệu phi chuẩn hoá): mỗi lớp con là một bảng đầy đủ cột của cha và của nó. Ưu: đọc một loại không cần join. Nhược: truy vấn đa hình cần UNION; khó bảo đảm khoá duy nhất giữa các bảng; đổi thuộc tính lớp cha phải sửa mọi bảng; khoá ngoại tới "lớp cha" không khai báo được.
- Single table (một bảng cho cả cây): một bảng chứa mọi cột của cả cây và một cột phân biệt loại. Ưu: đơn giản, truy vấn đa hình nhanh, không join. Nhược: nhiều cột NULL; không đặt NOT NULL cho cột riêng lớp con được (thay bằng CHECK theo loại); bảng phình khi cây lớn.
Hướng dẫn chọn: mặc định class table khi lớp con có nhiều thuộc tính riêng và có truy vấn đa hình; single table khi lớp con ít thuộc tính riêng và hay truy vấn chung; concrete table khi hầu như không truy vấn đa hình và không có khoá ngoại trỏ tới lớp cha. Mọi lựa chọn ghi lý do.
Ví dụ (giao đồ ăn, Payment với CardPayment, CashPayment, WalletPayment): chọn single table payment(id, order_id, amount, paid_at, payment_type, card_last4, auth_code, wallet_txn_id) với CHECK (payment_type = 'CARD' AND card_last4 IS NOT NULL) OR ...; lý do: lớp con chỉ có 1-2 thuộc tính riêng, báo cáo doanh thu truy vấn chung mọi loại.
Ví dụ sai: dùng concrete table cho Person - Doctor, Receptionist rồi bảng appointment cần FK tới "người tạo lịch" là Person: không khai báo được khoá ngoại.

F5. Chuẩn hoá (CSDL quan hệ)
F5.1. Bảng kiểm tra: | TBL | Khoá (chính và ứng viên) | Phụ thuộc hàm (FD) | 1NF | 2NF | 3NF | BCNF | Kết luận |
F5.2. Quá trình tách (với bảng không đạt): liệt kê bảng trước, FD vi phạm, các bảng sau khi tách.
F5.3. Phi chuẩn hoá có chủ đích: | TBL.cột | Dạng phi chuẩn hoá | Lý do (NFR / BR, số liệu) | Cơ chế giữ nhất quán |
Định nghĩa:
- Phụ thuộc hàm X --> Y: trong một bảng, mỗi giá trị của tập cột X ứng với tối đa một giá trị của Y (biết X thì chỉ có một khả năng của Y).
- 1NF: mọi giá trị là nguyên tố (không tách nhỏ hơn theo nghĩa nghiệp vụ), không có nhóm lặp, không có cột chứa danh sách.
- 2NF: đạt 1NF và không có thuộc tính không khoá phụ thuộc vào một phần của khoá chính (chỉ cần xét khi khoá gồm nhiều cột).
- 3NF: đạt 2NF và không có thuộc tính không khoá phụ thuộc bắc cầu vào khoá chính (khoá --> A --> B với A không phải khoá).
- BCNF: với mọi FD X --> Y không tầm thường, X là siêu khoá. Phần lớn bảng đạt 3NF cũng đạt BCNF; chỉ cần kiểm tra kỹ khi có nhiều khoá ứng viên gồm nhiều cột chồng lấn nhau.
Quy tắc:
- FD phải có căn cứ từ BR hoặc ngữ nghĩa nghiệp vụ; không suy từ vài dòng dữ liệu mẫu.
- Mục tiêu mặc định là 3NF; BCNF khi áp dụng được mà không làm mất ràng buộc quan trọng (nếu mất, ghi lý do giữ 3NF).
- Phi chuẩn hoá phải có lý do và cơ chế nhất quán; không phi chuẩn hoá "cho tiện".
Ví dụ quá trình chuẩn hoá (quản lý kho): bảng ban đầu R(issue_no, product_code, warehouse_code, warehouse_address, product_name, unit, quantity), khoá chính {issue_no, product_code}. FD: issue_no --> warehouse_code (mỗi phiếu xuất từ một kho); warehouse_code --> warehouse_address; product_code --> product_name, unit; {issue_no, product_code} --> quantity.
- 2NF: product_name, unit phụ thuộc một phần khoá (product_code); warehouse_code, warehouse_address phụ thuộc một phần khoá (issue_no). Tách thành R1(issue_no, warehouse_code, warehouse_address), R2(product_code, product_name, unit), R3(issue_no, product_code, quantity).
- 3NF: R1 có phụ thuộc bắc cầu issue_no --> warehouse_code --> warehouse_address. Tách R1 thành R4(issue_no, warehouse_code) và R5(warehouse_code, warehouse_address).
- Kết quả: stock_issue(issue_no, warehouse_code), warehouse(warehouse_code, warehouse_address), product(product_code, product_name, unit), stock_issue_line(issue_no, product_code, quantity).
Ví dụ BCNF (phòng khám): bảng assignment(patient_id, service_code, doctor_id) với BR "mỗi bác sĩ chỉ thực hiện một dịch vụ" và "mỗi bệnh nhân với mỗi dịch vụ được phân một bác sĩ". FD: {patient_id, service_code} --> doctor_id; doctor_id --> service_code. Khoá ứng viên: {patient_id, service_code}, {patient_id, doctor_id}. Bảng đạt 3NF (service_code là thuộc tính khoá) nhưng không đạt BCNF vì doctor_id không phải siêu khoá. Tách thành doctor_service(doctor_id, service_code) và patient_doctor(patient_id, doctor_id); ghi rõ ràng buộc {patient_id, service_code} duy nhất không còn khai báo được bằng khoá, phải kiểm tra ở ứng dụng hoặc trigger. Nếu ràng buộc đó quan trọng hơn, giữ 3NF và ghi lý do.
Ví dụ 1NF (thư viện): reader(reader_id, name, phone_numbers = "0901000001, 0912000002") vi phạm 1NF; tách reader_phone(reader_id, phone_number).
Phân biệt giá trị lịch sử với dư thừa: order_line.unit_price (giá tại thời điểm đặt) không phải dư thừa của dish.price, vì là một sự kiện khác (giá có thể đổi sau khi đặt); ghi rõ trong mô tả cột. Ngược lại, loan.reader_name sao chép reader.name không có lý do là dư thừa, phải bỏ.
Ví dụ phi chuẩn hoá hợp lý: order.total_amount lưu sẵn (dẫn xuất từ các dòng) vì NFR yêu cầu danh sách đơn của nhà hàng hiển thị dưới 1 giây với khoảng 5.000 đơn mỗi ngày; cơ chế: tính lại trong cùng giao dịch khi thêm, sửa, xoá dòng đơn.
Lỗi thường gặp: tách bảng quá mức (mỗi cột một bảng) gây join không cần; tách theo dữ liệu mẫu chứ không theo FD; phi chuẩn hoá không ghi cơ chế cập nhật dẫn tới dữ liệu mâu thuẫn.

F6. Mô hình vật lý
F6.1. Bảng cột (bảng lõi), mỗi dòng một cột:
| TBL | Tên bảng | Cột | Kiểu | PK/FK/UNIQUE | NULL | Mặc định | Nguồn DC |
Cột thêm: | Tham chiếu FK (TBL.cột, ON DELETE, ON UPDATE) | CHECK / mô tả |
- Cột PK/FK/UNIQUE: ghi PK, FK, UQ, hoặc kết hợp "PK, FK"; khoá nhiều cột ghi cùng nhãn ở mỗi cột và ghi tên ràng buộc ở cột CHECK / mô tả.
- NULL: "NOT NULL" hoặc "NULL".
- Nguồn DC: DC-<Lop>.<thuocTinh>; cột khoá ngoại ghi R-nn; cột kỹ thuật (khoá thay thế, cột phân biệt loại, cột phiên bản) ghi "Thiết kế: <lý do>".
- Ví dụ đúng (quản lý kho):
| TBL-04 | stock_item | warehouse_id | BIGINT | PK, FK | NOT NULL | | R-06 | TBL-01.id, RESTRICT | |
| TBL-04 | stock_item | product_id | BIGINT | PK, FK | NOT NULL | | R-07 | TBL-02.id, RESTRICT | |
| TBL-04 | stock_item | quantity_on_hand | INTEGER | | NOT NULL | 0 | DC-StockItem.quantityOnHand | | CHECK (quantity_on_hand >= 0) |
- Ví dụ sai: | TBL-04 | stock_item | qty | VARCHAR(255) | | NULL | | | | | Sai: tên viết tắt không rõ, kiểu chuỗi cho số lượng, cho phép NULL trong khi multiplicity là 1, không có nguồn, thiếu CHECK không âm theo BR.
F6.2. Ánh xạ kiểu dữ liệu (điều chỉnh theo hệ quản trị đã chốt, ghi bảng ánh xạ đã dùng):
| Kiểu thiết kế | Kiểu vật lý gợi ý |
|---|---|
| String có độ dài tối đa | VARCHAR(n), n lấy từ điều kiện hợp lệ P04/BR, hoặc quyết định thiết kế theo C1 mục 7 ("Thiết kế: <lý do>") |
| String dài không giới hạn | TEXT |
| Integer / Long | INTEGER / BIGINT |
| Decimal (tiền, số lượng thập phân) | DECIMAL(p, s), không dùng FLOAT/REAL |
| Boolean | BOOLEAN (hoặc kiểu tương đương của hệ quản trị) |
| Date / DateTime | DATE / TIMESTAMP (ghi rõ có múi giờ hay không) |
| Enumeration | VARCHAR(n) kèm CHECK tập giá trị, hoặc khoá ngoại tới bảng danh mục |
| Định danh thay thế | Theo QUY_UOC_CSDL; không có thì theo kiểu định danh của P12; P12 không có thì BIGINT tự tăng |
F6.3. Index: | TBL | Tên index | Cột (theo thứ tự) | Loại (UNIQUE / thường / khác) | Phục vụ truy vấn (UC bước / NFR) |
Quy tắc: khoá chính và UNIQUE đã có index; tạo index cho cột khoá ngoại nếu hệ quản trị không tự tạo và có join hoặc xoá bảng cha; tạo index cho cột trong điều kiện lọc, join, sắp xếp của truy vấn thường xuyên được nêu trong UC/NFR; index nhiều cột xếp cột so sánh bằng trước cột so sánh khoảng; không tạo index chỉ trên cột có ít giá trị phân biệt (cờ Boolean) trừ khi hệ quản trị hỗ trợ index một phần phù hợp; mỗi index làm chậm ghi, nên mỗi index phải chỉ ra truy vấn nó phục vụ.
Ví dụ đúng (phòng khám): | TBL-07 | appointment | ix_appointment_doctor_start | doctor_id, start_time | thường | UC-003 bước 2: lễ tân xem lịch bác sĩ theo ngày; NFR-04 |
Ví dụ sai: index trên mọi cột của mọi bảng "cho nhanh".

F7. Mô hình tài liệu (chỉ khi dùng CSDL NoSQL dạng tài liệu)
F7.1. Aggregate và collection: | TBL | Collection | Gốc aggregate (DC) | Nhúng (DC, qua R-nn) | Tham chiếu (DC --> TBL, qua R-nn) | Lý do | Giới hạn kích thước tài liệu |
F7.2. Trường tài liệu: dùng bảng lõi F6.1, cột "Cột" ghi đường dẫn trường (ví dụ lines[].product_id), cột "Kiểu" ghi kiểu của hệ quản trị (string, int, decimal, date, objectId, array, object).
F7.3. Index của collection theo F6.3.
Quy tắc nhúng (embed) hay tham chiếu (reference):
- Nhúng khi: quan hệ là composition (bộ phận không tồn tại ngoài gốc); dữ liệu luôn được đọc cùng gốc; số bộ phận có giới hạn nhỏ và biết trước; bộ phận không cần truy vấn độc lập; cần cập nhật nguyên tử cùng gốc (đa số hệ quản trị tài liệu bảo đảm nguyên tử trên một tài liệu).
- Tham chiếu khi: quan hệ nhiều - nhiều; số phần tử tăng không giới hạn (nhật ký, bình luận, lịch sử giao dịch); đối tượng được dùng chung và cập nhật độc lập (danh mục sản phẩm, hồ sơ bác sĩ); tài liệu có nguy cơ vượt giới hạn kích thước.
- Sao chép có chủ đích (snapshot) một vài trường của đối tượng tham chiếu vào tài liệu (tên món, giá tại thời điểm đặt) được phép khi cần giá trị lịch sử hoặc tránh truy vấn thêm; ghi cơ chế cập nhật hoặc ghi rõ là giá trị không cập nhật.
- Aggregate là đơn vị nhất quán: thao tác cần nhất quán trên nhiều aggregate phải ghi cách xử lý (giao dịch nhiều tài liệu nếu hệ quản trị hỗ trợ, hoặc bù trừ).
Ví dụ đúng (giao đồ ăn): collection orders, gốc Order, nhúng lines[] (mỗi dòng có dish_id tham chiếu, dish_name và unit_price là snapshot) và delivery_address; tham chiếu customer_id, restaurant_id; lý do: đơn luôn đọc cùng dòng, số dòng nhỏ, dòng không truy vấn độc lập.
Ví dụ sai: nhúng toàn bộ lịch sử đơn hàng vào tài liệu customer: mảng tăng không giới hạn, cập nhật đơn phải ghi lại tài liệu khách hàng lớn.

F8. ERD
F8.1. ERD logic/vật lý (bắt buộc): diagrams/P13-erd-logical.drawio.
- Node: | ID (TBL) | Loại (Table / Collection / Note) | Nhãn (tên bảng) | Stereotype | Thuộc về | Ghi chú |; danh sách cột lấy từ F6.1.
- Edge: | ID (tên ràng buộc fk_...) | Nguồn (bảng cha) | Đích (bảng con chứa FK) | Loại quan hệ (Phụ thuộc / Độc lập) | Nhãn / multiplicity (ký pháp chân chim hai đầu) | Ghi chú |
- Quy tắc ngữ nghĩa: ký pháp chân chim (crow's foot); quan hệ phụ thuộc (FK nằm trong PK bảng con) vẽ nét liền; quan hệ độc lập (FK ngoài PK) vẽ nét đứt; đầu phía bảng cha thể hiện "một" (bắt buộc: một vạch kép; tuỳ chọn: vòng tròn và vạch); đầu phía bảng con thể hiện "nhiều" (0..*: vòng tròn và chân chim; 1..*: vạch và chân chim) hoặc "một" với quan hệ 1-1. Mỗi cột trong bảng ghi dạng "PK tên: KIỂU", "FK tên: KIỂU", "PK,FK tên: KIỂU", "UQ tên: KIỂU".
- Style draw.io: bảng dùng style Class của Conventions C7 (swimlane, stackLayout, startSize=26) với mỗi cột là một cell con style text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1; ; cạnh: edgeStyle=orthogonalEdgeStyle;html=1;startArrow=ERmandOne;endArrow=ERzeroToMany;startFill=0;endFill=0; (thay ERmandOne, ERzeroToOne, ERone, ERmany, ERoneToMany, ERzeroToMany theo multiplicity), thêm dashed=1 cho quan hệ độc lập. Source của cạnh là bảng cha, target là bảng con.
- Bố cục: bảng cha phía trên hoặc bên trái bảng con; bảng trung gian M:N đặt giữa hai bảng; toạ độ bội số 10, khoảng cách tối thiểu 40, cạnh không cắt qua bảng.
F8.2. ER khái niệm (chỉ khi DAY_DU): diagrams/P13-erd-conceptual.drawio, ký pháp Chen.
- Node: thực thể (E-), mối quan hệ (ER-), thuộc tính (AT-<E>-<ten>).
- Quy tắc ngữ nghĩa: thực thể là hình chữ nhật; thực thể yếu là hình chữ nhật viền kép; mối quan hệ là hình thoi (viền kép với mối quan hệ xác định thực thể yếu); thuộc tính là hình elip nối với thực thể hoặc mối quan hệ; thuộc tính định danh gạch chân; thuộc tính đa trị là elip viền kép; thuộc tính dẫn xuất là elip nét đứt. Bản số (1, N, M) ghi trên đoạn nối giữa thực thể và hình thoi.
- Style draw.io: thực thể rounded=0;whiteSpace=wrap;html=1; ; thực thể yếu shape=ext;double=1;rounded=0;whiteSpace=wrap;html=1; ; mối quan hệ rhombus;whiteSpace=wrap;html=1; ; thuộc tính ellipse;whiteSpace=wrap;html=1; (định danh thêm fontStyle=4; đa trị shape=doubleEllipse; dẫn xuất dashed=1); cạnh endArrow=none;html=1; .
- Lỗi thường gặp (cả hai sơ đồ): thiếu bảng trung gian nhưng vẽ chân chim ở cả hai đầu trong ERD vật lý; vẽ quan hệ phụ thuộc bằng nét đứt; ERD không khớp F6 (thiếu cột, thiếu FK); vẽ cạnh chân chim ngược phía.

F9. Script DDL (chỉ khi SINH_DDL là "Có")
- Một code block theo cú pháp hệ quản trị đã chốt: CREATE TABLE theo thứ tự bảng cha trước; ràng buộc đặt tên theo QUY_UOC_CSDL; CREATE INDEX theo F6.3. Với NoSQL: lệnh tạo collection, validator schema nếu hệ quản trị hỗ trợ, tạo index.
- Script phải khớp F6 hoàn toàn (tên, kiểu, NULL, DEFAULT, CHECK, FK, index).

[Target]
Trả lời Đạt/Không đạt cho từng câu, sửa trước khi trả kết quả; mục không đạt còn lại ghi vào "Vấn đề còn mở".
1. Mọi lớp Persistent = Có trong P12 có thực thể và bảng/collection (hoặc được nhúng) trong F2; không có bảng cho lớp control/boundary.
2. Mọi thuộc tính persistent của lớp có cột tương ứng hoặc lý do không lưu (derived không lưu).
3. Mọi association/aggregation/composition giữa lớp persistent được ánh xạ trong F4.2 đúng quy tắc (FK ở phía N, bảng trung gian cho M:N, composition là quan hệ phụ thuộc có CASCADE).
4. Mọi cây kế thừa persistent có chiến lược ánh xạ và lý do.
5. Mọi bảng có khoá chính; khoá ứng viên nghiệp vụ có UNIQUE.
6. Mọi bảng có FD liệt kê và đạt 3NF, hoặc có dòng phi chuẩn hoá có chủ đích kèm lý do và cơ chế nhất quán.
7. Bảng có nhiều khoá ứng viên chồng lấn đã được kiểm tra BCNF.
8. NULL/NOT NULL khớp multiplicity; DEFAULT khớp giá trị mặc định P12; CHECK phủ ràng buộc BR và tập giá trị enumeration.
9. Kiểu tiền tệ không dùng số thực dấu phẩy động; độ dài chuỗi có căn cứ (P04, BR, hoặc "Thiết kế: <lý do>"); Q, ASM chỉ dùng cho độ dài, định dạng mang nghĩa nghiệp vụ; kiểu khoá chính khớp kiểu định danh của P12.
10. Mỗi index có truy vấn cụ thể mà nó phục vụ.
11. Với NoSQL: mỗi quyết định nhúng/tham chiếu có lý do theo F7; không có mảng tăng không giới hạn trong tài liệu.
12. ERD khớp F6 (bảng, cột, FK); quan hệ phụ thuộc nét liền, độc lập nét đứt; chân chim đúng phía; file .drawio hợp lệ, không nén.
13. Script DDL (nếu có) khớp F6.
14. Không đổi tên, mã phần tử của P12; mọi đề nghị sửa nằm ở "Đề xuất sửa artifact trước".
15. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho bước mô hình dữ liệu; có ưu tiên cao hơn quy tắc mặc định của bước (trừ Conventions C1); không có thì thay cả khối bằng "Không có" | Ví dụ: "Mọi bảng dùng xoá mềm bằng cột deleted_at, không dùng ON DELETE CASCADE."; "Không sinh ER khái niệm, chỉ ERD vật lý."; "Dữ liệu cá nhân bệnh nhân (số điện thoại, địa chỉ) phải đánh dấu cần mã hoá ở cột CHECK / mô tả."}}
````

## 5. Ghi chú cho người dùng

- Độ dài cột không có trong nguồn được chọn như quyết định thiết kế và ghi "Thiết kế: <lý do>", không thành câu hỏi mở. Muốn áp quy ước riêng, ghi trong YEU_CAU_BO_SUNG (ví dụ "tên người tối đa 100 ký tự"). Câu hỏi mở về độ dài chỉ còn cho giá trị mang nghĩa nghiệp vụ; khi đó bổ sung bảng dữ liệu vào/ra ở P04.
- FD bị AI suy sai: FD phản ánh quy tắc nghiệp vụ. Nếu kết quả tách bảng không hợp lý, kiểm tra BR ở P06; bổ sung BR (ví dụ "mỗi phiếu xuất chỉ từ một kho") rồi chạy lại.
- Thay đổi lớn về khoá chính hoặc chiến lược kế thừa sau khi đã lập trình rất tốn kém; chốt F1 và F4.3 sớm.
- Dùng độc lập (không có P12): đính kèm class diagram hoặc danh sách lớp, thuộc tính, quan hệ do người dùng tự viết; thay mã DC/R-nn bằng tên lớp và mô tả quan hệ. Có thể dùng bước này chỉ để chuẩn hoá một lược đồ có sẵn: đính kèm lược đồ và yêu cầu chỉ làm F5.
- Sau P13, chạy X1 để review chéo thiết kế lớp và dữ liệu (ví dụ thuộc tính P12 không khớp cột P13).

## 6. Căn cứ

- Chen P. P., The Entity-Relationship Model: Toward a Unified View of Data, ACM TODS, 1976.
- Codd E. F., A Relational Model of Data for Large Shared Data Banks, CACM, 1970; Further Normalization of the Data Base Relational Model, 1972.
- Date C. J., An Introduction to Database Systems, 8th ed.: phụ thuộc hàm, 1NF, 2NF, 3NF, BCNF.
- Elmasri R., Navathe S., Fundamentals of Database Systems: ánh xạ ER sang quan hệ, ký pháp ER.
- ANSI/SPARC three-schema architecture (lược đồ ngoài, khái niệm, trong).
- Fowler M., Patterns of Enterprise Application Architecture: Single Table Inheritance, Class Table Inheritance, Concrete Table Inheritance, Foreign Key Mapping, Association Table Mapping, Dependent Mapping, Embedded Value, Identity Field.
- Ambler S., Agile Database Techniques; Mapping Objects to Relational Databases.
- Sadalage P., Fowler M., NoSQL Distilled: aggregate-oriented data model, aggregate và nhất quán.
- Evans E., Domain-Driven Design: aggregate, aggregate root.
- Tài liệu mô hình hoá dữ liệu của MongoDB: nhúng và tham chiếu.
