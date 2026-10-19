Model của phiên chạy: Sonnet

# Nhật ký người chạy P09 - Thiết kế kiến trúc - VietFit (lần chạy đầu)

Đã ghi: design/P09-architecture.md, design/diagrams/P09-package-layers.drawio (XML hợp lệ, 32 node gồm 4 layer, 27 package, 1 note; 54 cạnh). Không tạo diagrams/P09-deployment.drawio (xem mục 2). Q mới Q-88 đến Q-94; chưa có ASM (NGHIEM_NGAT). Kiểm tra bằng script: bảng Node, Edge của F9 khớp file .drawio (id và cạnh), F6 có 54 dòng khớp 54 cạnh, F4 cột Phụ thuộc khớp bảng Edge (trừ 5 package giao diện phía khách, cố ý ghi "-" vì gọi qua mạng), không có cạnh đi lên layer, không có vòng, không có đoạn cạnh cắt node, không có hai đoạn cạnh chồng nhau, mọi điểm uốn là bội số của 10.

Mục Target không đạt: không có. Mục đạt có lưu ý: Target 1 (thước đo của nhiều dòng F1 là "Chưa quy định" kèm Q vì P06 không có NFR bảo mật, sẵn sàng, bảo trì), Target 8 (CN2 chỉ hơn CN1 một điểm). Ghi ở Vấn đề còn mở của artifact.

## Vướng mắc

1. Mục 2 và mục 4, F10: "diagrams/P09-deployment.drawio | (chỉ khi DAY_DU) Khi hệ thống phân tán" và "F10. Deployment diagram (chỉ khi DAY_DU), khi hệ thống có từ hai node thực thi trở lên".
   - Gặp: hồ sơ dự án có MUC_CHI_TIET = GON. Giá trị DAY_DU không được định nghĩa ở prompt, Conventions, README hay hồ sơ (tôi không được đọc mẫu hồ sơ). Hệ thống này rõ ràng phân tán (thiết bị di động, trình duyệt, máy chủ, CSDL).
   - Xử lý: coi GON khác DAY_DU, F10 ghi "Không có" và nêu lý do, không tạo file deployment. Hệ quả: câu ở A4 "F10 ghi artifact chứa package ở mỗi node, và mọi package mà một package trong artifact phụ thuộc phải có trong cùng artifact" không áp dụng được; thông tin node tôi để ở F4 cột Nguồn và F7. Nên nêu rõ ở prompt tập giá trị của MUC_CHI_TIET và điều kiện sinh F10.

2. Mục 3 dòng "Nếu NEN_TANG hoặc CONG_NGHE trong hồ sơ dự án là 'Chưa chốt'" và F11 "Khối chỉ gồm hai dòng bảng ... thay hai dòng NEN_TANG, CONG_NGHE".
   - Gặp: NEN_TANG đã chốt ở mức loại ứng dụng, CONG_NGHE "Chưa chốt". Prompt không nói khi chỉ một trong hai trường chưa chốt thì F11 có ghi lại dòng NEN_TANG không, và câu "Hồ sơ đã chốt cả hai trường thì ghi 'Không cần cập nhật'" không khớp trường hợp này.
   - Xử lý: F11 ghi cả hai dòng, NEN_TANG giữ nguyên giá trị hồ sơ và có câu giải thích.

3. Mục 3 dòng "P10 ... coi các Q-nn liệt kê dưới khối F11 là đã trả lời theo ASM tương ứng" và F11 "Q-nn mà giá trị trên phụ thuộc ... Chấp nhận khối này là chấp nhận phương án đã dùng cho các Q đó."
   - Gặp: chế độ NGHIEM_NGAT không có ASM nên "theo ASM tương ứng" không có nghĩa; Q-76 và Q-94 là câu hỏi về ngưỡng và năng lực đội, chấp nhận công nghệ không "trả lời" được chúng. Cũng không rõ Q nào thì "phụ thuộc" (tôi chọn Q-76, Q-94 vì hai Q này ảnh hưởng điểm so sánh CN1 và CN2).
   - Xử lý: ghi Q-76, Q-94 theo mẫu. Nên làm rõ hệ quả ở NGHIEM_NGAT (Q vẫn mở hay coi là đóng).

4. A1 và Target 1: "Mọi yêu cầu có ý nghĩa kiến trúc truy được về NFR, ràng buộc hoặc tác nhân" và [Context] gắn TIEU_CHI_UU_TIEN.
   - Gặp: P06 chỉ có hai NFR đo được (NFR-01, NFR-02) và không có NFR bảo mật, sẵn sàng, bảo trì; TIEU_CHI_UU_TIEN lại xếp Bảo mật và Sẵn sàng đứng đầu. NGHIEM_NGAT cấm tự đặt ngưỡng nên các dòng bảo mật, sẵn sàng, bảo trì không có nguồn NFR để truy về. Nguồn tôi dùng: chính TIEU_CHI_UU_TIEN, câu "chỉ hội viên đó và huấn luyện viên phụ trách được xem" trong tài liệu nguồn, "Cửa quay hỏi phần mềm", ACT-13/14.
   - Xử lý: ghi thước đo "Chưa quy định (Q-88)" v.v. và sinh 7 Q mới (Q-88 đến Q-94). TIEU_CHI_UU_TIEN không thuộc ba loại nguồn nêu ở Target 1. Nên cho phép "tiêu chí ưu tiên của người dùng" là nguồn hợp lệ, hoặc nói rõ khi P06 thiếu NFR thì A1 phải sinh Q và dừng ở đó.
   - Cùng chỗ: F1 giới hạn 3-10 dòng, tôi dùng đúng 10 dòng phải gộp (NFR-03 với NFR-04, NFR-05 với NFR-06, sáu hệ thống ngoài một dòng).

5. A1 dòng cuối và F3 "Rủi ro còn mở": "Mỗi quyết định như vậy ghi ở F3 dòng 'Rủi ro còn mở' kèm Q-nn ... Ở NGHIEM_NGAT chỉ ghi Q-nn, phần tử phụ thuộc ghi 'chờ Q-nn'".
   - Gặp: không phân biệt được ranh giới giữa "quyết định kiến trúc nguồn không nêu" (được phép đưa ra) và "quyết định thiết kế kỹ thuật" của C1 mục 7 (không cần Q). Ví dụ: client mỏng (không logic cục bộ), một triển khai trung tâm, hai chế độ chạy API và nền, giao dịch khoá dòng cho BR-11, TLS.
   - Xử lý: client mỏng, nơi đặt máy chủ, số node, một hay hai ứng dụng di động, tách tiến trình nền: ghi Q (Q-90, Q-91, Q-92, Q-88). Giao dịch khoá dòng, idempotent, TLS, mỗi mốc một bản chạy: ghi "Thiết kế: ..." không Q. Ranh giới là phán đoán của tôi.

6. F2.1 và F2.2 "Trọng số", "mức đáp ứng (Tốt / Trung bình / Kém)".
   - Gặp: prompt không nói trọng số lấy dạng nào, và cách tổng hợp mức đáp ứng. Tôi tự quy ước trọng số 4, 3, 2, 1 theo thứ tự TIEU_CHI_UU_TIEN và Tốt = 3, Trung bình = 2, Kém = 1. Kết quả F2.2 sát nhau (CN2 31 điểm, CN1 30 điểm), phụ thuộc quy ước; thêm tiêu chí "Phù hợp quy mô và đội" trọng số 1 để phá thế hoà. Đội phát triển không có thông tin nào (sinh Q-94).
   - Xử lý: ghi quy ước ngay dưới bảng, ghi chênh lệch nhỏ và phương án thay thế ở Kết luận và Vấn đề còn mở. Nên cho prompt một công thức chấm mặc định hoặc nói rõ có cần tổng điểm hay không.
   - Cùng chỗ: A2 yêu cầu 2-4 phương án nhưng F2.1 khuyên tránh microservices cho hệ thống nhỏ; tôi vẫn phải đưa PA2 microservices làm phương án so sánh chỉ để loại. Chưa rõ có nên đưa một phương án "chắc chắn bị loại" vào bảng hay không.

7. A4 đoạn "Client có logic nghiệp vụ cục bộ (chạy khi mất kết nối) ... Lời gọi qua mạng giữa hai node ... không là phụ thuộc package: không ghi ở F4, F6, F9".
   - Gặp: đoạn viết cho client có logic cục bộ; hệ thống này dùng client mỏng (gọi API). Prompt không nói client mỏng có áp dụng quy tắc "lời gọi qua mạng không là phụ thuộc" hay không. Nếu áp dụng thì 5 package giao diện phía khách không có cạnh phụ thuộc nào, sơ đồ có 5 package rời; nếu không thì giao diện phụ thuộc vào API (lại vi phạm vì phụ thuộc đi sang package ở node khác).
   - Xử lý: áp dụng quy tắc, ghi "-" ở F4 và đặt một Note trên sơ đồ giải thích.

8. A4/F4 "đặt giao diện người dùng của hai tác nhân khác nhau trong cùng package (P10 A3 sẽ phải tách)" cùng "Mức hợp lý: 3-5 layer; mỗi layer 1-8 package".
   - Gặp: tách theo tác nhân cho 7 tác nhân người cần ít nhất 5 package giao diện (ACT-01 và ACT-02 gộp) cộng 3 package API, đúng 8 package ở Presentation, sát trần. ACT-01 Người quan tâm và ACT-02 Hội viên cùng một ứng dụng nên tôi gộp, ghi ở Vấn đề còn mở. Không rõ Người quan tâm và Hội viên có phải "hai tác nhân khác nhau" theo ý lỗi này không.
   - Cũng: nhóm "Giá và báo cáo" vừa đặt giá vừa báo cáo, "và" trong tên nhóm đụng quy tắc "Trách nhiệm ... không chứa 'và' nối hai trách nhiệm khác loại"; tôi tách PricingService và ReportingService (7 package Application cho 6 nhóm).

9. A5 và F9 "Loại quan hệ (Dependency)" so với A5 "realization đi từ lớp ở layer trên xuống interface".
   - Gặp: bảng Edge của F9 chỉ liệt kê Dependency, nhưng hai cơ chế DIP của tôi (Application hiện thực interface gọi ngược của Scheduling; Persistence hiện thực interface kho của Domain) là realization ở mức lớp. Ở mức package không có ký pháp realization riêng.
   - Xử lý: vẽ thành Dependency đi xuống, ghi chú "hiện thực interface gọi ngược" ở cột Ghi chú và quy tắc V4 ở F6. Nên chỉ rõ ký pháp ở mức package.

10. A7 "ghi Đề xuất sửa P07 thêm entity cho trạng thái chờ".
    - Gặp: tôi không được đọc P07, chỉ có P08 F3 (tên phương thức startWaitingForPayment, handlePaymentTimeout, cancelAbsenceMark, cancelWaitlistTransferMark). Đề xuất dựa trên tên phương thức, chưa kiểm được ngữ cảnh P07. YEU_CAU_BO_SUNG nói đề xuất trước chưa áp dụng vì chờ Q; đề xuất mới của tôi không chờ Q nhưng cũng sẽ chưa được áp dụng; không rõ xếp chung hay riêng.
    - Xử lý: ghi 2 đề xuất P07 và 1 đề xuất P06 (thiếu NFR sẵn sàng, bảo mật). Điều kiện kích hoạt A7 ("nếu kiến trúc không cho giữ trạng thái trong bộ nhớ") do chính kiến trúc tôi chọn quyết định, nên có tính vòng: chọn kiến trúc không giữ trạng thái rồi sinh đề xuất sửa. Prompt chưa nói kiến trúc mặc định có giữ trạng thái hay không.

11. F4 "không có phụ thuộc vòng" so với mô hình P08: AC-E-Member hỏi MembershipPackage (R-12) và ClassBooking (R-19), còn PackageOrder, ClassBooking, EntryScan lại gắn về Member.
    - Gặp: nếu Domain chia theo nhóm chức năng thì phụ thuộc hai chiều giữa package Account và Membership, GroupClass. Prompt không nói P09 hay P10 chịu trách nhiệm giải vòng này (A7 cấm "ánh xạ chi tiết sang lớp thiết kế").
    - Xử lý: P09 chốt chiều phụ thuộc Domain (mọi package phụ thuộc Account), ghi quy tắc V7 và dòng AC-E-Member ở F8 để P10 chuyển hành vi. Không sửa P08 vì chưa phải lỗi.

12. C7.1, C7.3 về sơ đồ nhiều cạnh: sơ đồ có 54 cạnh, 18 cạnh đi từ Application xuống Domain vượt qua cả hàng package Services, 3 cạnh vượt hàng Application.
    - Gặp: C7.1 chỉ hướng dẫn cạnh giữa hai hàng liền kề và cạnh cùng hàng. Cạnh vượt qua một layer không có hướng dẫn; tôi tự dùng hành lang dọc ngoài các hàng node (phải cho cạnh xuống Domain, trái cho cạnh xuống Security) và làn y riêng. Công thức "khoảng cách giữa hai hàng tối thiểu 40 + 10 x số cạnh" làm khoảng cách giữa layer lớn (sơ đồ 1760 x 1580). Phải viết script sinh sơ đồ và kiểm tra cắt node, không thể làm tay.
    - Cũng: cột x, y, w, h trong bảng Node dùng toạ độ tuyệt đối còn file .drawio ghi package con theo toạ độ tương đối của layer chứa (do container); C7.1 không nói dùng loại nào. Tôi ghi tuyệt đối ở bảng và ghi chú ở F9.
    - Hạn chế: không có công cụ vẽ ảnh nên không xem được bố cục; chỉ kiểm bằng hình học (không cạnh cắt node, không chồng đoạn). Đẹp hay không chưa kiểm.

13. F5 dòng bắt buộc "boundary có Loại boundary 'Kênh thông báo' ở P08 F3 ... khi P08 có" và hồ sơ HAU_TO_TEN_LOP "boundary kênh thông báo: tên kênh".
    - Gặp: P08 không có lớp loại này (SMS và push mang Loại "Giao diện hệ thống", hậu tố Gateway). Ghi một dòng "P08 hiện không có". Dòng này gần như rỗng nhưng bắt buộc theo prompt.

14. A4/A6 và F5 cho boundary giao diện thiết bị: cửa quay là thiết bị gọi vào phần mềm (đầu vào), còn A6 nói "mỗi hệ thống ngoài được che sau một interface, sẽ thành subsystem ở P10", F5 ví dụ ánh xạ "boundary hệ thống --> subsystem ở Services".
    - Gặp: với cửa quay (gọi vào) thì "subsystem ở Services" không hợp, điểm vào là REST endpoint ở Presentation phía máy chủ. Tôi đặt vào PKG-12 ExternalApi. Prompt không có ví dụ thiết bị gọi vào. P10/P11b có thể hiểu khác (P11b là giao diện hệ thống/thiết bị).
    - Tương tự cổng thanh toán nếu Q-45 là tự gửi kết quả: cần thêm điểm vào cùng PKG-12. Tôi không vẽ cạnh này (chờ Q-45) và ghi ở F6.

15. Mục 3 bảng "Phần cần dùng" so với F1 "BR-11", "BR-04": P06 chỉ cho dùng mục 2 đến 5, Câu hỏi mở, Giả định; BR nằm ở mục 6. Yêu cầu "không được để số chỗ đã đặt vượt sức chứa" là nguồn quan trọng cho kiến trúc nhưng ở P06 là BR-11. Tôi dẫn BR-11 và BR-04 qua tên xuất hiện trong P08 F3 (được đọc) và câu trong tài liệu nguồn. Nên thêm cột BR vào "Phần cần dùng" của P06 hoặc cho phép trích tài liệu nguồn.

16. Mục 2 liệt kê P03 là "Có" bắt buộc còn mục 3 ghi "Không cần, trừ khi kiểm tra nhóm chức năng". Mục 2 P05 "Không" nhưng [Context] gọi là "(nếu có)". Tôi không đọc P03, lấy nhóm từ P02 Bảng 4a; ghi ở Đầu vào đã dùng.

17. C3 quy tắc cấp Q: "Mã lớn nhất tìm trong mục Câu hỏi mở và Giả định của mọi artifact ... kể cả file không thuộc đầu vào". Phạm vi đọc của lần chạy cấm đọc file khác (P04, P07) nên tôi tin Q-87 do người điều phối cung cấp và không quét lại. P08 ghi Q-87 lớn nhất trước lần chạy nên khớp.

18. C5 "Giả định (chỉ khi CHE_DO_GIA_DINH = CO_NHAN)" so với "Mục nào không có nội dung thì ghi 'Không có', không xoá mục". Hai câu mâu thuẫn nhẹ ở NGHIEM_NGAT. Tôi giữ mục và ghi "Không có (chế độ NGHIEM_NGAT, không dùng mục này)" theo mẫu các artifact trước.

19. Quá tải ngữ cảnh: P02 (74 KB), P08 (63 KB), P06 (36 KB), P05 (35 KB) chỉ cần các phần nhỏ nhưng bảng "Phần cần dùng" gom cả Bảng 4b của P02 (mục 4) và toàn bộ F3 của P08 (23 dòng nhiều chữ). Tôi chỉ dùng Bảng 4a và cột Stereotype, Tên, Loại boundary, Trạng thái ở F3. Nên cho phép "cột AC, Stereotype, Tên, Loại boundary, Trạng thái" nghĩa là chỉ lấy các cột đó (đã ghi), và với P02 chỉ Bảng 4a.

20. Hạng mục không kiểm được: ảnh render của sơ đồ (không có draw.io CLI), tính đúng của các nhận định phi chức năng về Node.js với React Native, NestJS, Flutter (tôi chấm theo hiểu biết chung; prompt cho phép nhưng C1 mục 1 nói không dùng hiểu biết chung để thêm chức năng, còn so sánh công nghệ thì cần hiểu biết chung).
