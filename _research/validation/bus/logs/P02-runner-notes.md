# P02 - Nhật ký người chạy - bus (SaoViet Bus)

Model: mặc định của phiên điều phối (Claude Opus 5.5, claude-opus-5-5).

Đầu vào: 00-Conventions.md, README.md, P02-identify-use-cases.md, bus/design/project-profile.md, P00-problem-brief.md, P01-actors.md, bus/yeu-cau-xe-khach.md. Placeholder: PHAM_VI_LAN_CHAY, QUY_UOC_DA_CHOT, YEU_CAU_BO_SUNG đều "Không có". Đầu ra: bus/design/P02-usecases.md (P02 không sinh .drawio).

Kết quả: 22 EV, 49 CAND, 18 UC (16 User-goal, 2 Subfunction), 4 Q mới (Q-26 đến Q-29), 4 ASM mới (ASM-08 đến ASM-11), 4 CAND "Chờ Q-nn" (Q-03, Q-14), 2 đề xuất sửa P01.

## Vướng mắc

### 1. Bước 4 "gom vào một dòng" mâu thuẫn với "các ứng viên còn lại kết luận Gộp vào"

- Vị trí: [Action] Bước 4: "Gom các ứng viên cùng nghĩa (cùng tác nhân, cùng kết quả, khác từ ngữ) vào một dòng: giữ ứng viên đầu, các ứng viên còn lại kết luận "Gộp vào" (khi ứng viên đầu thành UC)". Bước 3: "Gộp mọi mục tiêu ở Bước 1, mọi phản hồi ở Bước 2, và thêm các ứng viên từ phân tích động từ".
- Gặp gì: gần như mỗi mục tiêu ở Bước 1 trùng nguyên văn một phản hồi sự kiện ở Bước 2 và một cụm động từ. Nếu mỗi nguồn sinh một CAND riêng thì bảng phình gấp ba (khoảng 20 dòng "Gộp vào ... trùng nghĩa" không mang thông tin). "Vào một dòng" gợi ý gộp chung một dòng, còn vế sau lại nói các ứng viên còn lại có kết luận riêng.
- Xử lý: ứng viên trùng nguyên nghĩa thì gộp vào một dòng, cột Nguồn phát hiện ghi đủ "Mục tiêu; Sự kiện EV-xx; Động từ"; chỉ dùng "Gộp vào" cho ứng viên khác phạm vi hoặc khác tác nhân (CAND-11, CAND-12, CAND-13, CAND-20, CAND-26). Prompt nên nói rõ chọn cách nào.

### 2. Bước 9.1 dẫn tới quy tắc của P03 mà P02 không được đọc

- Vị trí: Bước 9.1: "Quy trình nghiệp vụ chính là quy trình tạo ra giá trị cốt lõi cho tác nhân chính quan trọng nhất (tác nhân đặt trên cùng theo P03 L-02)."
- Gặp gì: P03 chạy sau P02 và không nằm trong đầu vào của P02 (mục 2, mục 3), nên không biết L-02 chọn tác nhân nào. Với đề này có ít nhất hai ứng viên: Hành khách (doanh thu trực tuyến) và Nhân viên bán vé.
- Xử lý: chọn ACT-01 Hành khách theo mục tiêu nghiệp vụ ở P00 mục 1, ghi vào Vấn đề còn mở. Prompt nên chép tiêu chí của L-02 vào P02 thay vì chỉ dẫn.

### 3. Bước 9.1 "điều kiện tiên quyết" không rõ có gồm dữ liệu vận hành do tác nhân khác tạo

- Vị trí: Bước 9.1: "Nhóm chứa điều kiện tiên quyết của quy trình đó (đăng ký tài khoản, đăng ký thành viên) đánh số trước nhóm quy trình."
- Gặp gì: muốn bán vé thì phải có lịch chạy (UC-012) và giá vé (UC-016) trước. Hiểu theo chữ thì hai nhóm này phải đánh số trước nhóm Bán vé; nhưng nhóm Vận hành chuyến còn chứa Huỷ chuyến, Soát vé (xảy ra sau). Các ví dụ chỉ nêu điều kiện tiên quyết của chính tác nhân chính. Đăng ký tài khoản ở đề này lại không bắt buộc để đặt vé.
- Xử lý: hiểu hẹp (chỉ điều kiện tác nhân chính phải làm trước), nên nhóm Bán vé đánh số đầu, các nhóm khác theo thứ tự trong nguồn. Ghi vào Vấn đề còn mở.

### 4. U-R01 ở chế độ CO_NHAN: ghi ASM nhưng vẫn "chưa nối"

- Vị trí: U-R01: "tác nhân người còn lại ghi Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN) về việc có phải đăng nhập không, chưa nối."
- Gặp gì: ASM theo C1.2 là một giả định có nội dung, các phần tử phụ thuộc phải dẫn mã ASM. Nếu ASM nói "nhân viên phải đăng nhập" thì lẽ ra nối theo ASM; quy tắc lại bảo chưa nối. Nguồn chỉ nhắc tài khoản của hành khách, còn bốn vai trò nhân viên không được nhắc.
- Xử lý: ghi ASM-09 (nhân viên phải đăng nhập) kèm Q-27, nhưng theo đúng chữ U-R01 không nối ACT-02 đến ACT-05 vào UC-010; ghi rõ trong ASM và Vấn đề còn mở để P03 biết. Prompt nên nói ở CO_NHAN có nối theo ASM hay không.

### 5. Q1 (đồng bộ nội bộ) và U-R07 (tác vụ theo lịch) cùng khớp một ứng viên

- Vị trí: Q1: "xử lý nội bộ: lưu, kiểm tra hợp lệ, tính toán, sinh mã, ghi nhật ký, đồng bộ nội bộ, "hệ thống tự..." mà không có sự kiện thời gian hay tác nhân kích hoạt". U-R07: "Là UC với tác nhân chính là tác nhân thời gian khi đồng thời: nguồn nêu rõ thời điểm ...".
- Gặp gì: "15 phút trước giờ xuất bến, hệ thống gửi danh sách hành khách của chuyến về máy soát vé" (Mục 8, câu 4). Theo ASM-01 ứng dụng soát vé thuộc hệ thống, nên đây là đồng bộ giữa hai phần nội bộ, không có tác nhân nào nhận thông tin (U-T5, U-T9 khó đạt). Nhưng có mốc thời gian rõ nên U-R07 cũng khớp, và Q1 tự loại trừ trường hợp "có sự kiện thời gian". P01 đã chốt ACT-10 có mục tiêu này.
- Xử lý: theo câu "quy tắc U-R ưu tiên hơn cây quyết định", giữ thành UC-014 với tác nhân ACT-10; ghi vào Vấn đề còn mở. Prompt nên có ví dụ cho tác vụ theo lịch mà kết quả chỉ là dữ liệu chuyển giữa các thành phần nội bộ.

### 6. U-R10: điều kiện a và b khó áp dụng khi mỗi bên có đoạn riêng của mình

- Vị trí: U-R10 a: "Luồng của người đại diện có một đoạn tương tác riêng từ 2 bước trở lên mà luồng của người được đại diện không có". U-R10 b: "chỉ khác một bước tìm hoặc chọn người".
- Gặp gì: đổi vé tại quầy (nhân viên thu tiền mặt chênh lệch) và đổi vé trực tuyến (hành khách thanh toán chênh lệch qua cổng). Đoạn riêng nằm ở cả hai phía, và phía người được đại diện (trực tuyến) còn có đoạn thanh toán qua cổng dài hơn. Quy tắc chỉ xét đoạn riêng của người đại diện. Nếu giả định thêm "in vé mới" tại quầy thì đổi vé lại rơi vào a. Kết quả phụ thuộc vào việc có giả định chi tiết luồng hay không, trong khi ở P02 luồng chưa được đặc tả.
- Xử lý: chỉ dựa vào nguồn (không giả định in vé mới), coi khác biệt là cách thu chênh lệch (một bước) và áp dụng U-R10 b cho Đổi vé và Trả vé. Bán vé tại quầy và Nhận đặt chỗ qua điện thoại theo U-R10 a vì kết quả khác.

### 7. U-R11 bắt đề xuất tổng quát hoá cho hai tác nhân khác hẳn bản chất

- Vị trí: U-R11: "Khi từ hai tác nhân trở lên cùng khởi xướng từ hai UC trở lên giống nhau, đề xuất tổng quát hoá tác nhân (ghi vào "Đề xuất sửa artifact trước", bước P01)". U-R10 b: "Nếu hai tác nhân dùng chung nhiều UC như vậy, đề xuất tác nhân cha ở P01."
- Gặp gì: Hành khách và Nhân viên bán vé cùng khởi xướng Đổi vé, Trả vé. Tác nhân cha của khách và nhân viên nhà xe không có nghĩa nghiệp vụ; ngưỡng "hai UC" quá thấp và không có ngoại lệ.
- Xử lý: vẫn ghi đề xuất vào "Đề xuất sửa artifact trước" như quy tắc bắt buộc, kèm câu cho phép P01 từ chối và giữ hai association.

### 8. "Chờ Q-nn" ở chế độ CO_NHAN và Target 3 "câu hỏi có trong mục Câu hỏi mở"

- Vị trí: Phần D Mục 3: ""Chờ Q-nn": ứng viên có dấu hiệu trong nguồn nhưng chưa đủ căn cứ để giữ hoặc loại". U-R16: "Ở chế độ CO_NHAN, P00 đã xếp chức năng theo một ASM-nn: theo ASM đó". Target 3: "mọi kết luận "Chờ Q-nn" trỏ tới câu hỏi có trong mục Câu hỏi mở".
- Gặp gì: (a) Prompt không nói ở CO_NHAN có nên tự tạo ASM thay vì "Chờ Q-nn" cho ca P00 chưa có ASM. Danh mục tuyến, xe, tài xế (Q-03) bị P00 cố ý để "chưa xếp", không ASM; hoàn tiền vé quầy khi huỷ chuyến (Q-14) cũng không có ASM. (b) Q-03, Q-14 nằm ở mục Câu hỏi mở của P00, không ở P02; Target 3 không nói "mục Câu hỏi mở" của artifact nào.
- Xử lý: dùng "Chờ Q-03" (CAND-47 đến CAND-49) và "Chờ Q-14" (CAND-43), không tạo ASM để khỏi tự thêm chức năng, theo cách P00 đã làm. Không chép lại Q-03, Q-14 vào bảng Câu hỏi mở của P02 để tránh một mã xuất hiện hai nơi; coi Target 3 đạt vì câu hỏi có trong P00.

### 9. U-R05 "mục tiêu thông tin độc lập" không có tiêu chí căn cứ nguồn

- Vị trí: U-R05: "Là UC khi tác nhân có mục tiêu thông tin độc lập ... "Tra cứu phòng trống" (khi khách chỉ muốn xem, chưa đặt)".
- Gặp gì: Mục 1 mô tả tìm chuyến, xem chỗ, chọn chỗ như một chuỗi đặt vé, nhưng câu 3 nêu riêng "Việc tìm chuyến và xem chỗ trống không cần tài khoản". Quy tắc không nói cần căn cứ thế nào để kết luận "khách chỉ muốn xem"; đặt vé cũng không cần tài khoản nên câu 3 không phân biệt được.
- Xử lý: giữ UC-001 Tra cứu chuyến xe theo ASM-08, kèm Q-26.

### 10. Tên UC cho tham số nghiệp vụ: U-R15 và U-R04 kéo về hai phía

- Vị trí: U-R15: "Thiết lập tham số nghiệp vụ ... là UC "Cấu hình <nhóm tham số>" hoặc thuộc "Quản lý <dữ liệu>" theo U-R04". U-R04: "Chỉ đưa vào "Quản lý X" những thao tác mà nguồn nêu."
- Gặp gì: nguồn chỉ nói quản lý "đặt" giá vé và "đặt" mức tăng giá. "Quản lý bảng giá vé" ngụ ý đủ thêm, sửa, xoá; "Cấu hình giá vé" nghe kỹ thuật. U-R15 không nói hai dạng tên có bắt buộc không.
- Xử lý: dùng động từ của nguồn: "Đặt giá vé", "Đặt mức tăng giá lễ Tết" (U-N1, U-N4); ghi vào Vấn đề còn mở.

### 11. Danh sách sự kiện không có loại cho tín hiệu kỹ thuật nội bộ mà nguồn nêu

- Vị trí: Bước 2.3 và Phần D Mục 2 cột Loại: "Nghiệp vụ / Thời gian / Hệ thống ngoài / Thiết bị". Bước 2.4: "Chỉ ghi sự kiện mà nguồn nêu".
- Gặp gì: nguồn nêu "gửi lại kết quả khi có sóng" (Mục 8, câu 3). "Có sóng trở lại" là sự kiện nguồn nêu nhưng không thuộc loại nào (mạng không phải tác nhân, P01 đã loại).
- Xử lý: không ghi thành EV, chỉ ghi ứng viên từ phân tích động từ CAND-46, kết luận là bước của UC-015.

### 12. Mục 5 không nói xử lý REQ loại Ràng buộc

- Vị trí: Phần D Mục 5: "Liệt kê mọi REQ loại Chức năng và Giao tiếp ngoài. REQ loại Quy tắc nghiệp vụ, Dữ liệu, Phi chức năng liệt kê khi đã gắn với UC cụ thể; còn lại ghi "Chuyển P06"."
- Gặp gì: P00 có loại "Ràng buộc" (REQ-04, REQ-56, REQ-68) không nằm trong danh sách nào. Câu "còn lại ghi Chuyển P06" cũng không rõ là có liệt kê dòng đó hay không.
- Xử lý: liệt kê đủ 68 REQ; REQ Ràng buộc gắn UC khi có liên quan và ghi "chuyển P06".

### 13. Q4 d vế thứ ba phải suy luận

- Vị trí: Q4 d: "có thể thực hiện lại hoặc thất bại độc lập mà không huỷ toàn bộ mục tiêu cha".
- Gặp gì: nguồn chỉ nói "Hết 10 phút chưa thanh toán thành công thì chỗ được trả lại", không nói tường minh hành khách được thanh toán lại. Câu "mọi điều kiện đều có căn cứ trong nguồn" ở Q4 đòi căn cứ, trong khi ví dụ Q4 d tự giả định "khách chọn phương thức khác và thanh toán lại".
- Xử lý: giữ UC-003 Thanh toán vé trực tuyến theo Q4 d, ghi rõ chỗ suy luận trong Vấn đề còn mở.

### 14. Mục 4 cột Tác nhân phụ khi UC có include Subfunction

- Vị trí: Phần D Mục 4 cột Tác nhân phụ: "mã ACT các tác nhân mà hệ thống gọi tới trong UC".
- Gặp gì: Cổng thanh toán được gọi trong UC-003, mà UC-003 được tách ra từ UC-002. Không rõ có ghi ACT-06 ở cả UC-002 không.
- Xử lý: chỉ ghi ACT-06 ở UC-003; UC-002 ghi ACT-07 (gửi vé qua SMS sau khi thanh toán).

## Target

Cả 14 mục Target đều Đạt. Ghi chú:
- Target 3 đạt khi hiểu "mục Câu hỏi mở" gồm cả của P00 (vướng mắc 8).
- Target 4: UC-014 đạt nhờ U-R07 ghi đè U-T9 (vướng mắc 5); UC-012 đạt U-T6 nhờ ASM-11.
- Target 12: ACT-05 Phụ xe chỉ có 1 UC, đã ghi nhận xét ở Mục 6.
