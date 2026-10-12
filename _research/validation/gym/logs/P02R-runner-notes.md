Model của phiên chạy: Sonnet

# Nhật ký người chạy - P02R - Dự án VietFit (gym)

Đầu ra: gym/design/P02R-review.md (3 phát hiện Thấp, kết luận Đạt, không cấp Q hoặc ASM mới). Mã Q lớn nhất sau lần chạy: Q-49. ASM: chưa cấp.

Placeholder đã điền: DOI_TUONG_REVIEW, PHAM_VI_REVIEW = TAC_NHAN, DANH_SACH_UC; QUY_UOC_DA_CHOT = Không có; YEU_CAU_BO_SUNG = Không có. Không có Target nào không đạt.

## Vướng mắc

1. Đề xuất sửa artifact trước trùng với bảng phát hiện
   - Vị trí: [Format] Phần C: "thêm bảng thông tin và các mục kiểm soát theo Conventions C5 (Câu hỏi mở, Giả định khi CO_NHAN, Đề xuất sửa artifact trước, Vấn đề còn mở)".
   - Gặp: toàn bộ đầu ra của P02R đã là đề xuất sửa P01, P02 (cột Đề xuất sửa của Mục 3, Mục 4, Mục 4b). Conventions C3 định nghĩa mục "Đề xuất sửa artifact trước" là chỗ ghi lỗi của bước trước, nên prompt không nói mục này ở P02R chứa gì khác Mục 3.
   - Xử lý: viết một bảng con trỏ (bước P02, các UC liên quan, tham chiếu UCR, cách áp dụng theo mục 5 của prompt) và một dòng P01 "Không có". Chấp nhận trùng lặp. Nên có câu quy định rõ mục này ở P02R chỉ là con trỏ hoặc được bỏ.

2. Bảng kiểm kê khi đối tượng đã có mã gốc
   - Vị trí: Mục 2 "Đối tượng đã có mã thì ghi 'Không có, dùng mã gốc'"; Bước 1.2 "Nếu đối tượng đã có mã RL-nn theo Conventions thì dùng RL-nn".
   - Gặp: Bước 1.2 chỉ nhắc mã RL-nn, không nhắc ACT-nn, UC-nnn. Cột đầu của Mục 2 là "Mã tạm" nhưng ghi "Không có, dùng mã gốc" thì mã gốc phải nằm ở cột "Tên như trong bản gốc" (chưa có cột mã gốc riêng). Kết quả là 42 dòng lặp cùng một giá trị, ít thông tin.
   - Xử lý: ghi "Không có, dùng mã gốc" ở cột đầu và đặt "ACT-nn Tên" hoặc "UC-nnn Tên" ở cột sau. Nên sửa Bước 1.2 thành "mã gốc theo Conventions (ACT-nn, UC-nnn, RL-nn)" và cho phép một dòng gộp thay cho bảng khi toàn bộ đã có mã.

3. Phạm vi "danh sách use case" trong file P02 không rõ
   - Vị trí: PHAM_VI_REVIEW "DANH_SACH_UC"; Mục 2 "Đối tượng review: danh sách use case ...".
   - Gặp: P02 có 7 mục (mục tiêu, sự kiện, ứng viên, bảng use case, ma trận truy vết, thống kê, kiểm soát). Prompt không nói phần nào là đối tượng chấm, phần nào chỉ để đối chiếu. Ứng viên bị loại và chờ Q (CAND-13 đến CAND-15, CAND-24, CAND-66 đến CAND-69) có là "phần tử" phải xét theo Target 8 không?
   - Xử lý: coi Mục 4 (Bảng 4a, 4b) là đối tượng chấm, các mục còn lại là bằng chứng đối chiếu; ghi điều này vào Mục 1 của đầu ra. Target 8 hiểu theo cách đó.

4. Bảng tác nhân sau sửa không có cột tên tiếng Anh
   - Vị trí: Mục 4b "| ACT | Tên | Loại | Tính chất | Thay đổi | Mã phát hiện |" so với Mục 4 có cột Tên (VI) và Tên (EN); Conventions C2: "tên use case và tác nhân có cả tiếng Việt và tiếng Anh ở hai cột riêng".
   - Gặp: Mục 4b chỉ có một cột Tên, mâu thuẫn nhẹ với C2 (Conventions thứ tự ưu tiên thấp hơn prompt, C9 mục 4 trên mục 5).
   - Xử lý: theo đúng cột của prompt (một cột Tên, tiếng Việt). Không ảnh hưởng kết quả nhưng nếu bước sau đọc Mục 4b thay P01 sẽ mất tên tiếng Anh.

5. Tác vụ theo lịch và mốc hạn tương đối
   - Vị trí: A-C: "Tác vụ theo lịch có tác nhân chính là tác nhân thời gian; hết giờ chờ trong một phiên đang mở không có tác nhân thời gian (U-R07)"; U-R07: "Tác vụ theo lịch có giá trị nghiệp vụ, xảy ra khi không còn phiên nào đang mở ... Hết giờ chờ trong phiên của một use case (chờ tác nhân thao tác, chờ thiết bị hoặc hệ thống ngoài phản hồi) là luồng thay thế".
   - Gặp: P02 có UC-013 (30 phút sau thông báo nhận chỗ), UC-022 (12 giờ huấn luyện viên chưa phản hồi), UC-015 (2 giờ trước giờ học), UC-016 (10 phút sau giờ bắt đầu) là mốc hạn tương đối so với một sự kiện, không phải lịch cố định; còn hạn 15 phút của đơn mua thì P02 xử lý là luồng thay thế của UC-005. Cụm "chờ tác nhân thao tác" có thể đọc là áp dụng cho UC-022 (chờ huấn luyện viên thao tác), trong khi cụm "trong phiên" lại loại. Prompt không định nghĩa "phiên đang mở" ngoài U-T6 ("không chờ tác nhân khác vào lúc khác").
   - Xử lý: dựa vào U-T6 và U-R13 để chấp nhận cách phân loại của P02 (chờ tác nhân khác ở lúc khác thì không còn phiên mở), không lập phát hiện, ghi ở Mục 6 của đầu ra. Đây là điểm dễ cho hai người review ra hai kết luận khác nhau; nên có một câu phân biệt "mốc hạn tương đối giữa hai phiên của hai tác nhân" với "chờ trong cùng phiên".
   - Liên quan: hạn 15 phút của đơn mua có thể rơi vào lúc hội viên đã đóng ứng dụng (không còn phiên mở), prompt không nói cách xử lý ca này.

6. Size test (U-T4) không áp dụng được ở thời điểm P02
   - Vị trí: U-T4 "chuỗi nhiều bước (luồng chính khoảng 3-15 bước)"; Bước 4 "chạy U-T1 đến U-T12".
   - Gặp: chưa có luồng chính (P04 chưa chạy), nên U-T4 chỉ đoán được từ mô tả ngắn. Với UC-013, UC-022 (gần như một hành động) không thể kết luận quá nhỏ hay không. Prompt cũng không nói khi tiêu chí không kiểm được vì thiếu luồng thì ghi ở đâu (Bước 2 chỉ nói về tiêu chí cần nguồn).
   - Xử lý: ghi U-T4 vào Mục 6 "không kiểm được trực tiếp" và không lập phát hiện. Nên mở rộng Bước 2 hoặc Mục 6 sang "tiêu chí không kiểm được vì thiếu luồng".

7. Cách đếm "từ" cho U-N7
   - Vị trí: "U-N7 Khoảng 2-6 từ, không có 'và' nối hai mục tiêu".
   - Gặp: UC-022 "Huỷ yêu cầu đặt buổi quá hạn" là 7 âm tiết nhưng khoảng 5 từ ghép tiếng Việt; P02 tự nhận vượt 6 từ. Prompt không nói đếm âm tiết hay từ ghép; chữ "Khoảng" cho dung sai.
   - Xử lý: không lập phát hiện vì chấp nhận dung sai; ghi ở đây. Nên nêu "đếm âm tiết" hoặc "đếm từ ghép" để hai người review thống nhất.

8. Không có tiêu chí cho lỗi nội dung cột Mục tiêu
   - Vị trí: Phần A nhóm U, chỉ có phép thử và anti-pattern cho use case và tên; Phần B "U-T và U-R mặc định Trung bình".
   - Gặp: có lỗi thật trong cột Mục tiêu của P02 (khẳng định hệ quả nguồn không nêu, viết cho bên không phải tác nhân chính: UC-011, UC-015, UC-021, UC-022) nhưng không có mã tiêu chí khớp trực tiếp. U-T5 (giá trị cho một tác nhân cụ thể) và U-T10 (truy vết) khớp một phần; mức mặc định Trung bình quá nặng so với hệ quả (không đổi danh sách).
   - Xử lý: dùng U-T5, U-T10 và hạ xuống Thấp có nêu lý do trong cột Vấn đề (Phần B cho phép nâng, hạ). Nên thêm một tiêu chí về nội dung Mục tiêu (bám nguồn, nhìn từ tác nhân chính) hoặc nêu rõ U-T5 áp dụng cho cả câu mục tiêu.

9. Ký hiệu Q4a đến Q4d gần giống mã câu hỏi Q-nn
   - Vị trí: "Q4a là phần dùng chung ... Q4d là mục tiêu con ..." và Phần B "Q4a đến Q4d theo U-AP01".
   - Gặp: Q4a, Q4d dễ nhầm với mã câu hỏi mở Q-nn khi Mục 6 của đầu ra cũng phải cấp Q-nn; P02 viết "Q4 d" cách một khoảng trắng nên còn gây khó tìm. Không ảnh hưởng kết quả lần này vì không phát sinh Q mới.
   - Xử lý: tránh dùng ký hiệu Q4 trong đầu ra. Nên đổi tên thành ví dụ SF-a đến SF-d trong prompt.

10. Điều kiện cấp Q ở Mục 6 và nguồn Q
    - Vị trí: Phần C: "Câu hỏi cần người viết trả lời ở Mục 6 được cấp mã Q-nn theo Conventions C3".
    - Gặp: điểm mơ hồ duy nhất đáng hỏi là lựa chọn mô hình hoá hạn 30 phút và 12 giờ (vướng mắc 5), nhưng đó là quyết định mô hình, không phải mơ hồ của nguồn, trong khi Conventions định nghĩa cột "Nguồn gây mơ hồ" cho Q-nn. Prompt không nói câu hỏi cho người viết về lựa chọn mô hình có phải Q-nn hay không.
    - Xử lý: không cấp Q; ghi lại ở Mục 6 như lựa chọn đã được P02 nêu trong Vấn đề còn mở.

11. Quá tải ngữ cảnh
    - Gặp: đầu vào bắt buộc gồm P00 (khoảng 320 dòng, 35K token), P02 (khoảng 400 dòng, 36K token), P01, nguồn, profile, prompt và Conventions. Công cụ đọc file chặn 25K token một lần nên phải đọc P00 và P02 theo hai trang. Review vẫn làm được nhưng P00 chủ yếu dùng để đối chiếu REQ; prompt cho phép chỉ đính kèm nguồn, nên với dự án lớn có thể dùng yeu-cau-phong-tap.md thay P00.
    - Xử lý: đọc đủ ba file, không bỏ sót phần nào.

## Mục Target

Cả 8 mục Target tự kiểm Đạt:
- Mục 1: ba phát hiện đều có phần tử, bằng chứng, mã tiêu chí, đề xuất làm được ngay.
- Mục 2: QUY_UOC_DA_CHOT là Không có.
- Mục 3: không đòi thêm chức năng ngoài nguồn.
- Mục 4: mức Thấp; UCR-02 hạ từ Trung bình mặc định, có lý do.
- Mục 5: UCR-02 gom bốn use case cùng gốc.
- Mục 6: Mục 4 sau sửa đã áp dụng đề xuất, không còn vi phạm.
- Mục 7: 0 Nghiêm trọng và 0 Trung bình, kết luận Đạt.
- Mục 8: đủ 28 dòng ở Mục 4 và 14 dòng ở Mục 4b.
