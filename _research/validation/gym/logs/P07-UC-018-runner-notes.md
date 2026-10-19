Model của phiên chạy: Sonnet

# Nhật ký người chạy - P07 cho UC-018 Vào chi nhánh

Tham số: UC_ID = "UC-018 Vào chi nhánh"; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG theo đề bài (bốn ý: REQ bổ sung chỉ là dữ liệu do use case khác cung cấp, CAND-34 là tiền điều kiện theo phương án (a), dùng thuật ngữ chuẩn P05, ghi chú "chưa có BR" nay đã có BR).

Đầu ra: design/P07-uc-analysis/UC-018-enter-branch-analysis.md; design/diagrams/P07-sequence-UC-018.drawio (5 trang: SD1a, SD1b, SD1c, SD2a, SD2b), P07-communication-UC-018.drawio (1 trang), P07-class-UC-018.drawio (1 trang). Cả ba file .drawio qua kiểm tra xml.dom.minidom; toạ độ là bội số của 10; không có hai node chồng nhau hoặc cách nhau dưới 40 ở communication và VOPC; tập message của communication khớp tập message không trả về, không nằm trong break của sequence.

Kết quả: 6 lớp phân tích (1 boundary, 1 control, 4 entity), 5 quan hệ VOPC, 20 message không kể trả về, 1 câu hỏi mới (Q-86), không có ASM. Mã Q lớn nhất sau lần chạy: Q-86.

## Phạm vi đọc: các chỗ tôi đọc vượt mức cho phép (cần ghi nhận để không hiểu sai chất lượng prompt)

1. Khi liệt kê thư mục logs để kiểm tra thư mục tồn tại, tôi đã in thêm sáu dòng đầu của gym/logs/P07-UC-015-runner-notes.md (dòng "Model của phiên chạy", tiêu đề, dòng Tham số và Đầu ra). Đó là nhật ký của bước khác, không được phép đọc. Nội dung đó không ảnh hưởng quyết định nào của tôi (chỉ là tham số và tên file đầu ra).
2. Để biết bố cục file .drawio và định dạng bảng, tôi đã đọc: các hàng F3.1, F3.2, F3.3, F4 và hai bảng SD1a, SD1b của file P07 UC-005 (prompt mục 3 chỉ cho đọc F1, F3.4, F8 b, Câu hỏi mở, Giả định, Vấn đề còn mở; không cần F2, F5, F7, F9, F10); đầu file P07-sequence-UC-010.drawio, P07-class-UC-015.drawio, P07-communication-UC-015.drawio. Hệ quả: kiểu đặt tên message, cách ghi note, cách vẽ lifeline Actor, cách ghi multiplicity bằng cell nhãn con và cách tách trang chịu ảnh hưởng của các bản trước, nên phần "prompt có đủ hướng dẫn để tự sinh file .drawio đúng định dạng hay không" bị đo lệch (xem mục 14 bên dưới).
3. Tôi đã đọc toàn bộ mục Câu hỏi mở, Vấn đề còn mở của ba file P07 đã có và Mục 2, Mục 4 của P01, P02 (cả bảng 4b của mọi UC để tìm UC có tác nhân thời gian, đúng như prompt cho phép), P05 (các thuật ngữ liên quan và mục Ứng viên không đưa vào), P06 (bảng NFR và BR). Đây là phạm vi cho phép.

## Vướng mắc về prompt và Conventions

1. Mục 3 (bảng "Phần cần dùng") nói P05 chỉ cần "Các thuật ngữ mà đặc tả dùng", P06 chỉ cần "Các BR, NFR có UC_ID ở cột áp dụng". Với P05 chữ "các thuật ngữ mà đặc tả dùng" đủ rõ khi tra theo mã GL, nhưng mục Câu hỏi mở của P05 (có Q-73 đến Q-75 ảnh hưởng UC-018) và mục "Ứng viên không đưa vào" (có "Thời điểm quẹt, mã QR đọc được, chi nhánh của cửa quay" và "Kết quả cho phép vào, lý do không cho phép" ở dạng đã loại) không thuộc "thuật ngữ mà đặc tả dùng". Tôi đọc cả hai mục vì cần cấp mã Q và cần biết khái niệm nào P05 đã loại. Gợi ý: nói rõ P05 mục "Ứng viên không đưa vào" được dùng cho lọc danh từ F3.2.

2. A3 (lớp boundary), F3.1, F6 và Target 3 cùng áp dụng cho UC-018 nhưng không khớp nhau.
   - Trích A3: "tác nhân người chỉ thao tác vật lý trên thiết bị (đưa thẻ vào máy, đẩy xe qua thanh chắn) và nhận kết quả qua kênh thông báo: boundary của tác nhân đó thuộc loại 'Kênh thông báo'".
   - Trích F3.1: "số boundary bằng số tác nhân tham gia (trừ tác nhân thời gian)... ít hơn là có tác nhân không được phục vụ".
   - Trích Target 3: "Mỗi tác nhân tương tác trực tiếp trong use case này ... có đúng một boundary".
   - Trích F6 (ngoại lệ): "tác nhân người thao tác vật lý trên một thiết bị là tác nhân phụ của cùng use case được gửi message tới boundary của thiết bị đó".
   - Với UC-018: hội viên, khách vãng lai chỉ quét mã và đi qua cửa quay; đặc tả không có bước nào báo kết quả cho người (chờ Q-70) nên không có "kênh thông báo"; cửa quay là tác nhân phụ thiết bị. Câu F6 viết "tác nhân người ... là tác nhân phụ", trong khi ở đây người là tác nhân chính, thiết bị là tác nhân phụ.
   - Xử lý: một boundary AC-B-TurnstileDevice (loại Giao diện thiết bị) phục vụ cả ba tác nhân; F3.1 có ba dòng trỏ cùng boundary; không tạo boundary kênh thông báo vì Q-70 chưa trả lời; áp dụng ngoại lệ F6 cho message người --> boundary thiết bị. Số boundary (1) nhỏ hơn số tác nhân (3), ghi giải thích ở F3.1 và Vấn đề còn mở. Mục này khó thoả đồng thời Target 3 theo nghĩa "mỗi tác nhân có đúng một boundary riêng".

3. F6 ngoại lệ thiết bị mô tả đường đi "người --> boundary thiết bị --> control" nhưng không nói ai là chủ thể của bước "thiết bị gửi dữ liệu đọc được". Trích: "rồi boundary thiết bị gửi dữ liệu đọc được tới control". P04 UC-018 bước 2 ghi "Cửa quay" (ACT-12) là bên gửi. Tôi vẽ hai message: người --> boundary (bước 1) và actor ACT-12 --> boundary (bước 2), rồi boundary --> control (2.1). Cách này lặp một thao tác vật lý ở hai lifeline. Prompt không nói nên bỏ message của ACT-12 (chỉ giữ người --> boundary) hay giữ cả hai. Tôi giữ cả hai để mỗi bước P04 có một message đúng cột "Thực hiện bởi".

4. F5 b) và F5 c) không có hướng dẫn cho luồng thay thế vừa là nhánh rẽ vừa chứa luồng kết thúc con.
   - Trích F5 b): "break đặt trực tiếp trong interaction của trang (mức ngoài cùng), không lồng trong toán hạng của alt, opt, loop, par".
   - Trích F5 c): "Luồng 'Quay lại bước K' vẽ bằng alt: toán hạng luồng chính chỉ ghi guard và note 'tiếp tục luồng chính'".
   - Luồng 3a (vé) là nhánh quay lại bước 6 và chứa 3a1a, 3a1b là luồng kết thúc. Nếu vẽ 3a bằng alt thì break 3a1a, 3a1b bị lồng trong alt (cấm); nếu vẽ break ở ngoài cùng thì không còn chỗ cho alt. Prompt chỉ có hướng dẫn "break trước, alt sau" cho cùng một điểm rẽ, không cho nhánh có hai cấp.
   - Xử lý: tách luồng 3a thành trang riêng SD2a, SD2b, mỗi trang có các break ở mức ngoài cùng, kết thúc bằng note "tiếp tục luồng chính từ message 2.1.7". Cách này hợp lệ theo "luồng không gộp được vẽ ở trang riêng" (mục 2 bảng đầu ra) nhưng STT, vị trí rẽ và cách ref tới luồng chính phải tự quyết.

5. Ngưỡng "tối đa 3 fragment ở mức ngoài cùng" (F5) không nói ref, loop có tính hay không, và không nói gì khi luồng chính ít message nhưng nhiều fragment. Trích: "một trang khoảng 30 message không kể message trả về, và tối đa 3 fragment ở mức ngoài cùng". Luồng chính UC-018 chỉ có 13 message nhưng gồm loop đối chiếu hội viên, loop gói tập, ba break (4a, 4b, 4c). Tôi tính ref và loop vào 3 fragment, tách thành SD1a (4 message), SD1b (4 message), SD1c (5 message), mỗi trang rất nhỏ; kết quả 5 trang cho một use case 8 bước, quá chia nhỏ. Gợi ý: cho phép gộp các break cùng điểm rẽ vào một trang hoặc tính ngưỡng theo cả hai tiêu chí (message và fragment) rồi chọn một.

6. A6 và F5 không nói đối chiếu theo khoá (tìm hội viên theo mã QR, tìm vé theo mã QR) có phải vẽ loop hay không.
   - Trích A6: "Trách nhiệm tác động lên một tập đối tượng cùng lớp (huỷ, gom, lọc, tổng hợp) giao cho đối tượng toàn thể nắm tập đó ... Đặc tả, BR, glossary không có đối tượng toàn thể nắm tập thì control lặp và gửi message tới từng phần tử".
   - Tìm hội viên theo mã là phép "lọc" trên tập hội viên mà không có đối tượng toàn thể. Các file P07 trước (đọc ở mục 3 của phần Phạm vi) coi truy vấn chọn phần tử là không vẽ ("việc chọn các phần tử của tập (truy vấn) không vẽ vì đặc tả không nêu"), nhưng prompt không có câu đó. Theo chữ A6 tôi vẽ loop [mỗi hội viên, đến khi mã QR khớp] và loop [mỗi vé]. Đây là nguyên nhân chính khiến vượt ngưỡng ở mục 5. Prompt nên nói rõ truy vấn theo khoá có vẽ hay không.

7. F5 c) quy tắc STT cho luồng trang riêng: "Message ở trang tách riêng dùng STT của message tại điểm rẽ trong trang luồng chính, kèm hậu tố chữ thường theo mã luồng". Luồng 3a và 3b cùng rẽ tại message 2.1.1 (đối chiếu hội viên không khớp), nhưng 3b chỉ biết sau khi 3a đối chiếu vé không khớp. Tôi đặt 3a là 2.1.1a, 2.1.1a.1... và 3b là 2.1.1b; luồng con 3a1a, 3a1b tiếp tục số của 3a (2.1.1a.3, 2.1.1a.5) thay vì hậu tố mới. Prompt không nói luồng con của luồng đã tách đặt STT thế nào. Tự quyết.

8. F7 "biến thể của tác nhân thứ hai" và "Khi DAY_DU". Trích F7: "Use case có nhiều tác nhân chính dùng chung luồng (P02 U-R10 b): biến thể của tác nhân thứ hai vào cùng communication diagram, giữ STT của trang biến thể". Trích: "Communication diagram cho luồng thay thế (chỉ khi DAY_DU)".
   - Prompt không định nghĩa DAY_DU ở đâu; hồ sơ dự án dùng MUC_CHI_TIET = GON. Tôi coi GON khác DAY_DU, theo cách các file P07 trước đã làm, nên không vẽ luồng thay thế kết thúc.
   - Biến thể ACT-03 của UC-018 chỉ khác hội viên ở luồng 3a (một luồng thay thế), nên "biến thể" và "luồng thay thế" trùng nhau; prompt không nói biến thể loại này có thuộc phạm vi GON không. Tôi vẽ phần đạt của luồng 3a (2.1.1a, 2.1.1a.1, 2.1.1a.2, 2.1.1a.4) và link ACT-03 --> boundary với cùng STT 1 như ACT-02. Cần câu hướng dẫn rõ.

9. F2 "Bước do tác nhân thực hiện chép nguyên, cột bổ sung ghi 'Không đổi'" và F9 "mọi message có một bước; mọi bước hệ thống có ít nhất một dòng". Bước 8 (người đi qua cửa quay) là bước của tác nhân nhưng prompt nói tác nhân người --> boundary thiết bị được phép "ở cùng một bước hoặc hai bước liền nhau". Tôi không vẽ message cho bước 8 vì không có phần mềm nào nhận; bước 1 có message vì khởi phát tương tác. Prompt không nói bước cuối của tác nhân có cần message không; Target 1 chỉ đòi bước hệ thống.

10. F2 không có chỗ cho điều kiện của luồng thay thế: bảng chỉ có cột "Mô tả trong đặc tả" nhưng P04 có thêm cột Điều kiện. Tôi gộp "Điều kiện: ... Hành động: ..." vào cột "Mô tả trong đặc tả" (giới hạn "tối đa 3 câu" chỉ áp cho ô bổ sung nên không vi phạm). Đề nghị thêm cột Điều kiện hoặc ghi cách gộp.

11. F3.2 danh sách giá trị cột Kết luận thiếu hai loại gặp ở UC-018:
   - khái niệm là tiền điều kiện/chức năng ngoài luồng không thuộc UC nào cụ thể (mã QR hiển thị trên ứng dụng, CAND-34): tôi dùng "Loại - không tham gia hành vi của use case này (khái niệm của CAND-34, tiền điều kiện theo phương án (a))" dù giá trị chuẩn chỉ nêu "khái niệm của UC-nnn";
   - yêu cầu phi chức năng dạng giá trị ("1 giây"): không có giá trị cho tham số của NFR (chỉ có "tham số của quy tắc BR-nn hoặc ASM-nn"). Tôi không đưa vào bảng, ghi chú dưới bảng.
   - "Hôm nay" (giá trị suy ra từ thời điểm hiện tại): tôi dùng "giá trị suy ra từ thời điểm quẹt", vì giá trị "suy ra từ X" yêu cầu X là entity/thuộc tính; thời điểm hiện tại không phải. Chưa chắc đúng.

12. Mức hợp lý của F3.4 ("Mỗi entity tham gia use case nên có ít nhất một trách nhiệm hành vi ngoài lưu giữ dữ liệu") và "Chỉ ghi trách nhiệm được dùng trong use case này": EntryScan chỉ có // createEntryScan, vì hành vi trên lượt quẹt (BR-20) thuộc UC-016 chưa phân tích. Ghi nhận ở Vấn đề còn mở (Target 9). Không mâu thuẫn nhưng khó thoả: lớp do use case này tạo cho use case khác dùng sẽ luôn mỏng ở lần chạy đầu.

13. F8 b) multiplicity "Ghi multiplicity khi đặc tả hoặc BR nêu rõ; nếu không rõ thì ghi '?' ... và ghi câu hỏi hoặc giả định, không đoán" cộng với định nghĩa "số ở phía A là số đối tượng A ứng với một đối tượng B". Quan hệ Member - EntryScan: phía hội viên (mỗi lượt quẹt thuộc một hội viên) có căn cứ (GL-30, bước 5), phía lượt quẹt (số lượt của một hội viên) không có căn cứ chắc chắn nên tôi ghi "?" và cấp Q-86 mới ("A 1 - B ?"). Cần Q mới chỉ để giải thích dấu "?"; có thể coi là quá chặt, nhưng đúng chữ prompt.

14. F10 và C7: prompt F10 chỉ đưa khung XML cho một lifeline và một message, không nói cách vẽ actor lifeline (participant=umlActor), self-call (điểm uốn), message Tạo (đích là mép trái lifeline), note (shape=note), ngăn thuộc tính và trách nhiệm của lớp VOPC (cell con của swimlane), nhãn multiplicity (C7.3 có nói), link tự nối ở communication, điểm uốn cho cạnh đi qua dải. Do đã xem file .drawio của bản trước (mục 2 của phần Phạm vi), tôi không thể đánh giá một AI chưa xem sẽ tự suy ra được bao nhiêu. Điểm chắc chắn thiếu: kích thước, kiểu của note; cách tính chiều cao lifeline; cách đặt nhãn của link tự nối; cách vẽ ref (prompt chỉ nói "fragment" dùng style chung).

15. Conventions C3: "Mã lớn nhất tìm trong mục Câu hỏi mở và Giả định của mọi artifact đã có trong THU_MUC_DAU_RA, kể cả file không thuộc đầu vào của bước (chỉ quét mã, không cần đọc nội dung)" khớp với mục 3 của prompt ("Mọi artifact trong thư mục đầu ra: Mã ở mục Câu hỏi mở, Giả định"). Không vướng; đề bài đã cho Q lớn nhất là Q-85 và tôi xác nhận bằng quét có ranh giới từ (\bQ-[0-9]+) trên mọi .md trong design/. Chỉ lưu ý: hàng "Mã Q, ASM cuối đã cấp" của khối thông tin chưa nói rõ khi ASM chưa cấp thì ghi gì; tôi ghi "ASM: chưa cấp (chế độ NGHIEM_NGAT)" theo các file trước.

16. A1 yêu cầu ghi "Mới - chủ sở hữu UC-xxx" cho "Entity hoặc boundary hệ thống ngoài mà khái niệm do use case khác (không include, không extend) quản lý, và use case đó chưa có P07". Vé tập một ngày (DayPass) do UC-017 tạo. Tôi ghi "Mới - chủ sở hữu UC-017". Thiết bị cửa quay (boundary) là ACT-12 chỉ UC-018 dùng nên ghi "Mới". Không vướng; nêu để xác nhận cách hiểu.

17. P04 UC-018 và Q-67: đặc tả nói thời điểm quẹt, chi nhánh của cửa quay "chưa quy định" nhưng bước 2 đã liệt kê "Gửi mã QR đọc được và chi nhánh của cửa quay"; thời điểm quẹt chỉ có ở Dữ liệu vào 1 trường 3. Tôi đưa cả ba (mã QR, chi nhánh, thời điểm quẹt) vào message receiveScannedCode và handleEntryRequest, ghi Q-67. Có thể xem là thêm dữ liệu ngoài bước 2, nhưng bước 5 cần thời điểm quẹt nên cần lấy từ đâu đó.

## Mục Target nào không đạt

Tất cả mục Target 1 đến 16 tự đánh giá Đạt, với các điểm nêu ở mục "Vấn đề còn mở" của artifact: Target 1 đạt một phần (luồng 3a1c chưa có hành động, chờ Q-40); Target 3 đạt theo cách hiểu một boundary phục vụ ba tác nhân (mục 2 ở trên); Target 9 EntryScan thiếu hành vi ngoài khởi tạo (mục 12); Target 12 đạt theo GON (mục 8).
