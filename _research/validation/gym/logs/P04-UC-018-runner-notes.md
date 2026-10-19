Model của phiên chạy: Sonnet

# Nhật ký người chạy - P04 cho UC-018 Vào chi nhánh

Đầu ra: design/P04-uc-specs/UC-018-enter-branch.md, design/diagrams/P04-activity-UC-018.drawio, design/P04-uc-specs/_BR-register.md (thêm BR-15 đến BR-20). Q mới: Q-67 đến Q-72. ASM: chưa cấp (NGHIEM_NGAT). Luồng chính 8 bước.

## Vướng mắc

1. Mục F4.2 mục 10 và P02 CAND-34.
   - Trích: "Bước đầu tiên là sự kiện kích hoạt" (F4.2 mục 10); P02 dòng CAND-34 "Hiển thị mã QR trên ứng dụng | Là bước của UC-018"; sự kiện kích hoạt EV-13 "Hội viên quét mã QR trên ứng dụng tại cửa quay".
   - Gặp: P02 xếp bước hiển thị mã QR vào UC-018 nhưng sự kiện kích hoạt lại là lúc quét mã tại cửa quay, nên bước hiển thị không thể nằm trong luồng chính (bước 1 phải là kích hoạt).
   - Xử lý: đưa "mã QR đang hiển thị trên ứng dụng" vào tiền điều kiện của hội viên, ghi Thông tin bổ sung, thêm dòng Đề xuất sửa artifact trước cho P02. Prompt không nói cách xử lý bước của use case đứng trước sự kiện kích hoạt.

2. F4.2 mục 12 với hai tác nhân chính có hành vi kiểm tra khác nhau.
   - Trích: "mọi khác biệt về hành vi giữa họ đặt thành luồng thay thế"; P02 CAND-33 "khác biệt là luồng thay thế".
   - Gặp: hội viên (kiểm tra gói) và khách vãng lai (kiểm tra vé) là hai kịch bản ngang hàng với hai sự kiện kích hoạt EV-13, EV-14. Luồng chính buộc phải chọn hội viên làm kịch bản điển hình, còn toàn bộ đường đi của khách vãng lai (kèm ba nhánh lỗi lồng) thành luồng 3a. Luồng chính vì vậy có bước 3 "kiểm tra mã QR là mã của hội viên" và bước 5 chỉ đúng với hội viên; người đọc nghiệp vụ có thể thấy lệch.
   - Xử lý: theo đúng prompt (hội viên là luồng chính, khách vãng lai là 3a), không đề xuất tách use case.

3. F5.2 và F5.4: luồng nhiều hành động có nhánh lồng, hàng cha có Quay lại hay không.
   - Trích F5.2: "hàng cuối ghi Quay lại / Kết thúc"; ví dụ extend: hàng "Na1" có Quay lại "Tiếp tục bước K" và các nhánh lồng "Na1a" có Quay lại riêng.
   - Gặp: luồng 3a có hành động 3a1 (kiểm tra vé) vừa có nhánh thành công (tiếp tục bước 6) vừa có các nhánh lỗi lồng 3a1a, 3a1b, 3a1c. Quy tắc "hàng cuối ghi Quay lại" mâu thuẫn với ví dụ extend (hàng cha có Quay lại, nhánh lồng đứng sau).
   - Xử lý: áp dụng theo ví dụ extend: hàng 3a1 ghi "Tiếp tục bước 6", các hàng 3a1a đến 3a1c ghi kết cục riêng. Hàng tiêu đề 3a ghi "-" ở cột Thực hiện bởi và Quay lại.

4. F5.3 với F5.7: thứ tự ưu tiên khi hai điều kiện cùng bước cùng đúng.
   - Trích: "Nguồn không nêu thứ tự ưu tiên thì theo thứ tự xuất hiện trong nguồn; ghi Q-nn ở NGHIEM_NGAT".
   - Gặp: bước 4 kiểm tra ba điều kiện (4a, 4b, 4c) và bước 3a1 kiểm tra hai điều kiện (3a1a, 3a1b) có thể cùng sai; mỗi nơi theo chữ nghĩa cần một Q-nn riêng về thứ tự. Hệ quả: chỉ riêng một use case đã đẻ ra nhiều Q về thứ tự.
   - Xử lý: viết điều kiện loại trừ nhau theo thứ tự trong nguồn và gom câu hỏi thứ tự ưu tiên của lý do báo vào Q-70 (cùng câu hỏi về cách báo cho người quét), không tạo Q riêng cho từng bước.

5. Target 5a và F4.2 mục 2: bước báo kết quả cho tác nhân người khi tác nhân phụ là thiết bị.
   - Trích Target 5a: "đều có bước hệ thống báo kết quả (thành công hoặc lý do thất bại) cho tác nhân người đó, qua màn hình hoặc kênh thông báo mà nguồn nêu; nguồn không nêu cách báo thì có Q-nn".
   - Gặp: phần mềm chỉ nói chuyện với cửa quay (thiết bị). Người quét biết kết quả qua cửa mở hay không và có thể qua phản hồi của cửa; nguồn không nêu. Prompt chưa nói bước "trả kết quả cho thiết bị" có thoả Target 5a hay không.
   - Xử lý: các luồng thất bại có bước "thông báo ... cho cửa quay" kèm "cách báo cho người quét chờ Q-70"; ghi vào Vấn đề còn mở. Coi Target 5a đạt có điều kiện.

6. F4.2 mục 2 và mục 4: Cửa quay làm chủ thể của bước không "trả về thông tin".
   - Trích: "Tác nhân phụ (hệ thống ngoài) là chủ thể của một bước khi nó trả về thông tin mà luồng dùng tiếp"; "Hai bước tác nhân liên tiếp chỉ khi tác nhân làm hai việc có ý nghĩa nghiệp vụ khác nhau".
   - Gặp: bước 2 (cửa quay gửi mã QR tới phần mềm) và bước 7 (cửa quay mở cửa) do thiết bị thực hiện; bước 1 (người quét) và bước 2 là hai bước tác nhân liên tiếp; bước 7 không trả thông tin mà là hành động vật lý. Bước 8 (người đi qua cửa) cũng là hành động vật lý, không tương tác với hệ thống. Prompt chỉ nêu trường hợp tác nhân phụ trả thông tin và trường hợp hệ thống gửi đi.
   - Xử lý: giữ cả bước 2, 7, 8 vì REQ-40 nêu rõ việc trao đổi với cửa quay để mở cửa và mục tiêu P02 là "đi qua cửa quay vào chi nhánh"; tách bước 1 và 2 vì hai chủ thể làm hai việc khác nhau (quét, gửi). Có thể bị đánh giá là hơi vượt quy tắc.

7. F3: tiền điều kiện đã xác thực.
   - Trích: "Tiền điều kiện đã xác thực chỉ ghi cho tác nhân được P03 nối với UC Đăng nhập".
   - Gặp: không rõ đây là yêu cầu bắt buộc phải ghi hay chỉ là giới hạn (được ghi khi). Hội viên quét mã tại cửa quay không cần phiên làm việc; chỉ việc hiển thị mã trên ứng dụng mới cần.
   - Xử lý: ghi "Hội viên đã được xác thực và mã QR của hội viên đang hiển thị trên ứng dụng" (ACT-02 có RL-04 nối UC-004). Đây là suy luận của người chạy, không phải câu của nguồn.

8. Hậu điều kiện tối thiểu (F3) khi nguồn chưa nói luồng thất bại có ghi gì.
   - Trích: "nếu không có gì thì ghi 'Không có thay đổi dữ liệu nào được lưu' khi mọi luồng thất bại đều kết thúc trước bước lưu, ngược lại ghi Q-nn".
   - Gặp: các luồng thất bại đều kết thúc trước bước 5 (lưu lượt quẹt), nhưng việc có ghi lượt quẹt bị từ chối hay không là chính điều REQ-35 (xác định vắng mặt) cần biết. Không thể thoả cả hai vế "không có thay đổi" và "chưa biết".
   - Xử lý: ghi "cửa quay không mở; gói và vé không thay đổi; việc ghi lượt quẹt bị từ chối chờ Q-71".

9. [Action] 4 và F5.4 "Chờ Q-nn" cho điều kiện chỉ tồn tại với một phương án trả lời.
   - Trích: "Chờ Q-nn (chỉ ở NGHIEM_NGAT, khi điều kiện của luồng có căn cứ trong nguồn hoặc suy ra từ BR ...)".
   - Gặp: Q-40 (vé mở một lần hay nhiều lần) đã có từ P00. Điều kiện "vé đã dùng trước đó" chỉ có nghĩa nếu trả lời "một lần", nên căn cứ trong nguồn yếu. Nếu không thêm luồng thì Q-40 không có chỗ bám trong đặc tả.
   - Xử lý: thêm luồng 3a1c không hành động, "Chờ Q-40", kèm note N-3a1c; ghi trong Vấn đề còn mở rằng luồng bỏ nếu Q-40 trả lời "nhiều lần".

10. F7.1, F7.3: BR của use case khác nhưng REQ do P02 gắn cho UC-018.
    - Trích: P02 gắn REQ-35 cho UC-016 và UC-018; REQ-35 là quy tắc xác định vắng mặt, thực thi ở UC-016. F7.3 định nghĩa "Bước áp dụng: nơi quy tắc được kiểm tra hoặc dùng".
    - Gặp: UC-018 không kiểm tra quy tắc REQ-35, chỉ cung cấp dữ liệu (lượt quẹt). Nếu không đăng ký BR thì REQ-35 không có BR nào trong đặc tả UC-018; nếu đăng ký thì sổ có BR mà UC-016 mới là nơi áp dụng. Prompt không nói trường hợp này. Bước 5 "Ghi nhận lượt quẹt" cũng không có câu nào của nguồn nêu phần mềm ghi lượt quẹt, chỉ suy ra từ REQ-35 và câu của P02 "Lượt quẹt vào cửa là căn cứ xác định vắng mặt (UC-016)".
    - Xử lý: đăng ký BR-20 (Suy luận), Bước áp dụng ghi "5, Dữ liệu vào 1", cột Ghi chú sổ nêu UC-016 sẽ dùng lại; thêm Q-71 hỏi phạm vi ghi nhận.

11. F1 hàng REQ và [Action] 1c: chọn REQ thêm.
    - Trích: "các REQ mà một bước, luồng, BR hoặc trường dữ liệu của đặc tả này dùng tới (kể cả REQ Chức năng của use case khác cung cấp dữ liệu ...)".
    - Gặp: không có tiêu chí để biết dừng ở đâu (có thêm REQ-09 thời hạn gói, REQ-17 ngày bắt đầu gói, REQ-42 bán vé hay không).
    - Xử lý: chỉ thêm REQ-10, REQ-43, REQ-46, REQ-51 là các REQ mà một BR hoặc điều kiện kiểm tra trực tiếp dựa vào; đã ghi vào Đề xuất sửa artifact trước cho P02.

12. F10.6 bố cục: nhánh thay thế "lệch sang phải" và trục dọc "cách decision 30".
    - Trích: "nhánh thay thế lệch ngang sang phải trục chính tối thiểu 220 ... các cạnh ra từ decision đi ngang tới một trục dọc cách decision 30 về bên phải".
    - Gặp: action chính rộng 180 nên trục dọc cách decision 30 (tâm decision +50) nằm trong hộp action chính ở các hàng dưới. Hai chuỗi nhánh (bước 3 với decision lồng 3a1; bước 4 với ba nhánh) cùng đặt bên phải thì các cạnh quay lại về M-6 cắt qua cột nhánh. Cửa quay là partition ngoài cùng bên phải nên cạnh từ A-1 sang A-2 và A-7 sang A-8 đi qua toàn bộ partition hệ thống.
    - Xử lý: nhánh của bước 3 ở bên phải, nhánh của bước 4 ở bên trái trục chính; trục dọc đặt ở khoảng trống giữa trục chính và cột nhánh; mọi cạnh vượt partition có điểm uốn. Partition hệ thống rộng 1200. Sơ đồ rộng hơn mức "2-4 partition, mỗi partition tối thiểu 280" dự kiến nhưng vẫn hợp lệ. Không có công cụ dựng ảnh để xem trực quan nên chỉ kiểm bằng script (không chồng node, không cạnh cắt node, khoảng cách tối thiểu 40, toạ độ bội số 10).

13. Format phần A: mục 8a và mục Giả định.
    - Trích: "## 8a. Kịch bản chính (chỉ khi DAY_DU, xem F9)"; "## Giả định (chỉ khi CO_NHAN)" so với C5 "Mục nào không có nội dung thì ghi 'Không có', không xoá mục".
    - Gặp: prompt không nói DAY_DU là giá trị của trường nào; project-profile.md có MUC_CHI_TIET = GON. Mục Giả định vừa "chỉ khi CO_NHAN" vừa phải đủ mục khung C5.
    - Xử lý: bỏ mục 8a (suy MUC_CHI_TIET = GON khác DAY_DU); giữ mục Giả định ghi "Không có (chế độ NGHIEM_NGAT, không dùng mục này)" cho nhất quán với ba đặc tả trước. Target 16 đọc là đạt.

14. F4.2 mục 11, Target 9 với bước 5 và bước 6.
    - Gặp: bước 5 (lưu lượt quẹt) và bước 6 (trả kết quả) không phải bước kiểm tra nên không có luồng thay thế; lỗi hạ tầng (cửa quay không nhận được trả lời trong 1 giây) không được tạo luồng theo F5.5 nhưng REQ-96 nêu ngưỡng 1 giây nên câu hỏi "quá ngưỡng thì sao" là có thật.
    - Xử lý: ghi Q-72 thay vì tạo luồng.

15. Điều kiện hợp lệ và Bắt buộc của dữ liệu cửa quay gửi.
    - Trích F6.1: "Nguồn không nêu thì ghi 'Chưa quy định (Q-nn)' ở chế độ NGHIEM_NGAT".
    - Gặp: trường Chi nhánh của cửa quay thực sự cần (BR-17, BR-19) nhưng nguồn không nói cửa quay có gửi nó hay không. Cột Bắt buộc ghi "Chưa quy định (Q-67)" trong khi bước 4 và 3a1 đã dùng chi nhánh; có chút mâu thuẫn giữa luồng (dùng chi nhánh) và bảng (chưa quy định). Cột Ví dụ yêu cầu giá trị thực tế nhưng định dạng mã QR chưa quy định, nên ví dụ "VF-M-004217" là minh hoạ do người chạy đặt.

16. Ngữ cảnh: đọc phần P00, P01, P02 theo bảng "Phần cần dùng".
    - Gặp: P00 mục Câu hỏi mở dài (Q-01 đến Q-43) và phải đọc để biết Q liên quan; tìm REQ nào "dùng tới" đòi quét thêm nhiều dòng. Không quá tải nhưng tốn công, và việc quyết định Q-nn của P00 nào liên quan UC-018 (Q-18, Q-40, Q-41; còn Q-19, Q-12, Q-03?) là phán đoán. Chỉ dẫn Q-18, Q-40, Q-41, Q-03 trong đặc tả.

## Kết quả tự kiểm Target

- Đạt: 1, 2, 3 (có điều kiện theo vướng mắc 7), 4, 5, 6 (8 bước), 7 (UC-018 không có include, extend), 8, 9, 9a (gói, vé có trạng thái do UC-005, UC-006, UC-017 đặt; đã có kiểm tra và Q-18, Q-40, Q-69; UC-018 không đưa đối tượng sang trạng thái cuối), 10, 11, 13, 14, 15, 16.
- Đạt có điều kiện: 5a (vướng mắc 5, Q-70), 12 (bước 5 và BR-20 suy ra từ REQ-35 và P02, vướng mắc 10), 12a (không có số liệu tính từ BR trong đặc tả này, không áp dụng).
- Không đạt: không có mục nào hoàn toàn không đạt.
