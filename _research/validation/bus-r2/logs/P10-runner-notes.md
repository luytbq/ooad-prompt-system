Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy - P10 - bus-r2

Đầu ra: design/P10-design-elements.md, design/diagrams/P10-package-design.drawio (1 trang), design/diagrams/P10-subsystem-context.drawio (2 trang). Cả hai file .drawio đã qua kiểm tra XML bằng xml.dom.minidom; bố cục (toạ độ bội số 10, điểm uốn bội số 10, khoảng cách tối thiểu 40, cạnh không cắt node) kiểm bằng chương trình. Chưa mở bằng draw.io.

Phạm vi đọc: prompt P10, 00-Conventions.md, README.md, project-profile.md, yeu-cau-xe-khach.md; P08 (F3, F4, Câu hỏi mở, Giả định, Vấn đề còn mở); P09 (F3 đến F7, F11, Câu hỏi mở, Giả định, Đề xuất, Vấn đề còn mở); P01 bảng tác nhân; P02 Mục 4; P06 Mục 3 đến 5; P03 Mục 1, 2. Không đọc P07, P04-uc-specs. Mã Q, ASM lớn nhất quét được: Q-65, ASM-48 (chỉ P09); P10 không cấp Q, ASM mới.

Mục Target không đạt: không có. Target 9 mới kiểm bằng chương trình, chưa xem bằng mắt (ghi ở Vấn đề còn mở của artifact).

## Vướng mắc

1. Mục 4, A1, hai câu nói ngược nhau về package hạ tầng không có lớp nguồn.
   - Câu A1: "Package tích hợp, hạ tầng của P09 không có lớp phân tích nguồn (máy in nối qua phần mềm trung gian, bộ định thời, đồng bộ với máy trạm) cũng được xét". Câu F1: "Package của P09 chỉ phục vụ use case chưa có P07 (không có lớp hoạt động nào trong P08) thì giữ chỗ ở F4, chưa tạo subsystem".
   - Gặp: PKG-23 TicketPrinting, PKG-26 BoardingSyncClient, PKG-24 Security thuộc cả hai câu (hạ tầng, không lớp nguồn, và chỉ phục vụ UC chưa có P07). Bộ định thời PKG-11 cũng thuộc cả hai nhưng có phục vụ UC-009 (handleHoldExpiry).
   - Xử lý: coi câu F1 là quy tắc quyết định (giữ chỗ, ghi ở F1 và Vấn đề còn mở); chỉ xét sâu package hạ tầng phục vụ UC đã có P07 (PKG-11, PKG-20). Prompt nên nói rõ câu A1 chỉ áp dụng khi use case phục vụ đã có P07.

2. Mục 4, F3: "Mọi lớp hoạt động trong P08 có đúng một dòng."
   - Gặp: P08 F3 có cột Trạng thái với hai giá trị "Hoạt động" và "Tạm (chờ P07 của UC-008/UC-010)". Không rõ "lớp hoạt động" có gồm lớp "Tạm" không.
   - Xử lý: ánh xạ cả hai control tạm (đủ 14 dòng) vì P09 F5 đã gán chúng vào PKG-13 và P08 F4 có quan hệ R-02, R-03; ghi "Tạm" ở lý do và Vấn đề còn mở. Prompt nên định nghĩa "lớp hoạt động" là lớp không bị gộp, hoặc nêu cách xử lý lớp tạm.

3. Mục 4, A2: "Lớp thiết kế giữ tên lớp phân tích khi ánh xạ 1-1, trừ khi tên đụng thuật ngữ kỹ thuật của mẫu kiến trúc".
   - Gặp: cả bốn control phân tích đặt tên XController, trong khi P09 F5 chọn MVC passive và còn lưu ý riêng rằng "controller" của MVC khác lớp control phân tích. Hệ quả là phải đổi tên cả 4 lớp 1-1 (thành XService), và ví dụ F3 của thư viện lại đặt phần Controller của MVC tên RequestHandler. Không nơi nào nói tên chuẩn cho lớp Application.
   - Xử lý: Application: XService; MVC controller: XRequestHandler (theo ví dụ F3). Ghi lý do ở từng dòng. Prompt nên gợi ý một hậu tố mặc định cho lớp control khi mẫu giao diện là MVC.

4. Mục 4, A2/F3: view model.
   - Gặp: P09 F3 nói "dữ liệu đưa cho view là view model do Application cấp" và QT-4 cấm Presentation phụ thuộc Domain, nhưng P10 không nói view model là phần tử thiết kế nào, có thuộc "tách thành nhiều lớp" của boundary không, và có phải "lớp mồ côi" không.
   - Xử lý: tạo DC-BookTicketOnlineViewModel, DC-CancelTripViewModel ở PKG-13, PKG-16, ghi ở bảng phần tử mới do cơ chế kiến trúc, nguồn P09 F3, QT-4 và thuộc tính boundary. Prompt nên nêu rõ nơi ghi view model.

5. Mục 4, A3: "Kiểu giá trị (tiền, định danh, mã tham chiếu) ... đặt ở package cùng layer với interface hoặc thấp hơn (ví dụ một package kiểu dữ liệu dùng chung ở layer thấp nhất)".
   - Gặp: IF-01, IF-02 ở Services dùng tiền, mã vé, mã giao dịch, số điện thoại; P09 không có package kiểu giá trị. Không rõ mã DC cho kiểu giá trị có cần lớp phân tích nguồn không (Target 1: "mọi phần tử thiết kế truy được về lớp phân tích hoặc cơ chế kiến trúc"), và đặt vào package P09 sẵn có hay cấp PKG mới. Cũng không rõ phụ thuộc mới tới package mới của các package giữ chỗ có phải ghi không.
   - Xử lý: cấp PKG-31 ValueTypes (Domain) gồm 4 kiểu, nguồn là thuộc tính kiểu "Số tiền", "Văn bản" của P08 và quy tắc A3; thêm phụ thuộc tới PKG-31 cho PKG-12, PKG-15 (giữ chỗ) vì chúng phụ thuộc IF-01, IF-02; ghi một dòng Đề xuất sửa P09. Chọn cách này thay vì gom vào Operations để tránh Operations thành điểm phụ thuộc chung.

6. Mục 4, F2: "Mỗi chỗ P09 ghi cơ chế gọi ngược và mỗi boundary thiết bị hoặc hệ thống ngoài chỉ đẩy sự kiện vào hệ thống có ít nhất một dòng."
   - Gặp: P09 QT-8 ghi không có gọi ngược; hai hệ thống ngoài đều do hệ thống gọi (ASM-11, NFR-12); thiết bị chưa thành subsystem. Bảng gọi ngược rỗng, prompt không nói cách trình bày bảng rỗng; mục C5 chỉ nói mục không có nội dung thì ghi "Không có".
   - Xử lý: một dòng "Không có" kèm đoạn lý do ngay dưới bảng.

7. Mục 4, F7: "Class chỉ vẽ cho lớp hiện thực interface gọi ngược".
   - Gặp: không nói interface kho dữ liệu (IF-03 đến IF-08) có vẽ không, và realization từ package PKG-20 tới interface/package không phải ký pháp UML chuẩn (realization nối classifier). Số cạnh tăng nhiều nếu vẽ đủ 6 interface.
   - Xử lý: không vẽ IF-03 đến IF-08; vẽ realization từ PKG-20 tới package chứa, nhãn ghi mã IF; ghi chú ở F7. Package giữ chỗ cũng không vẽ (mục 4 không nói có vẽ không). Prompt nên nêu hai điều này.

8. Conventions C3 và C7: không có mã cho node/edge của sơ đồ P10.
   - Gặp: F7, F8 yêu cầu bảng Node, Edge với ID nhưng C3 không cấp tiền tố cho cạnh; "E-<Ten>" đã dành cho thực thể ER (P13). Layer dùng lại PKG-01 đến PKG-04.
   - Xử lý: cạnh sơ đồ package ED-nn, cạnh sơ đồ context CE-nn (ID chỉ có nghĩa trong file sơ đồ, không nằm trong C3).

9. Conventions C7.1/C7.3 so với interface lollipop 20 x 20.
   - Gặp: điểm uốn bội số của 10 nhưng interface rộng 20 chỉ có 3 giá trị x bội 10 trên đỉnh (hai cạnh dùng chung một cổng bị cấm: "hai cạnh không dùng chung một cổng"), nên không đủ cổng cho 2 cạnh đi xuống + 1 realization. Nhãn của lollipop cũng tràn ngoài hình.
   - Xử lý: một cạnh vào đỉnh (đoạn thẳng, không điểm uốn), cạnh thứ hai vào cạnh phải qua một điểm uốn, realization vào cạnh trái; nhãn đặt dưới hình (verticalLabelPosition=bottom).

10. Mục 4, F6: bảng kiểm tra coupling.
    - Gặp: không nói bảng gồm phụ thuộc của package giữ chỗ không. P09 F6 đã có 58 dòng.
    - Xử lý: F6 chỉ liệt kê phụ thuộc của package có phần tử và phụ thuộc mới; kiểm toàn đồ thị (67 phụ thuộc) bằng chương trình và ghi kết quả dưới bảng.

11. Mục 4, A3: "Mỗi package nằm trong một layer của P09 (con của PKG layer hoặc PKG cấp cao ở P09). Cấp mã PKG tiếp theo số lớn nhất của P09."
    - Gặp: P09 đã có 26 package cấp dưới layer theo nhóm chức năng và tác nhân; chưa rõ lớp thiết kế mới đặt thẳng vào package P09 (cách chọn) hay phải tạo package con mới. Ví dụ F3 (PKG-11 LoanUI) gợi ý dùng package P09 sẵn có.
    - Xử lý: đặt thẳng vào package P09 sẵn có; chỉ cấp mã mới (PKG-31) khi P09 thiếu chỗ. Prompt nên nói điều này.

12. Mục 3 (bảng "Phần cần dùng"): "P03-usecase-model.md, P04-uc-specs/ | Quan hệ extend và use case tuỳ chọn (A3, lớp tuỳ chọn)".
    - Gặp: bảng không nói đọc phần nào của P04-uc-specs, còn mục 2 ghi P04 không có trong đầu vào. Chỉ có một quan hệ extend (UC-010 --> UC-014, điều kiện "vé mới đắt hơn"), là điều kiện luồng chứ không phải tính năng tuỳ chọn bán riêng, nên không có lớp tuỳ chọn.
    - Xử lý: đọc P03 Mục 1, 2; không đọc P04; ghi PKG-13 "UC-010 là include bắt buộc của UC-009, không phải lớp tuỳ chọn". Prompt nên phân biệt extend "điều kiện luồng" với "tính năng tuỳ chọn".

13. Mục 4, F1: bảng tiêu chí.
    - Gặp: cột "Tiêu chí thoả" chỉ có 6 giá trị cố định, không có chỗ cho bộ định thời nội bộ (tác nhân thời gian); và "Sản phẩm có sẵn" trùng với Persistence nhưng A1 lại bảo Persistence "không thành subsystem".
    - Xử lý: ghi "-" cho bộ định thời, ghi "Sản phẩm có sẵn" nhưng quyết định "Không" cho Persistence kèm lý do theo A1.

14. Mục 4, F1: "Mức hợp lý ... mọi boundary giao diện hệ thống ngoài và thiết bị đều thành subsystem".
    - Gặp: thiết bị (máy in, máy soát vé) chưa có lớp nguồn nên không thành subsystem lần này, trong khi Target 3 và README chỉ nói P11b thiết kế interface cho subsystem có ở P10. Hậu quả: P11b hiện chỉ có 2 subsystem.
    - Xử lý: giữ chỗ và ghi Vấn đề còn mở (nêu cần chạy lại P10 khi P08 phủ UC-004, UC-025, UC-026).

15. Mục 4, A2 và dữ liệu P08/P09: trách nhiệm chờ thanh toán và "huỷ mốc" của hai control.
    - Gặp: P08 gán startWaitingForPaymentResult, stopWaitingForPaymentResult cho control, nhưng P09 F5 nói control không giữ bộ đếm trong bộ nhớ. Tương tự cancelOverdueReservationMark, cancelPassengerListMark (ASM-28) của CancelTripController mâu thuẫn với PKG-11 đọc trạng thái chuyến từ dữ liệu bền (P09 F7). Prompt cấm thiết kế operation chi tiết nên không quyết ở P10.
    - Xử lý: giữ trách nhiệm kế thừa, ghi lý do ở F3 và Vấn đề còn mở cho P12.

16. Mục 4, A0: "Hồ sơ vẫn ghi 'Chưa chốt' ... Mẫu lệch công nghệ ... ghi Đề xuất sửa P09".
    - Gặp: hồ sơ đã cập nhật, không lệch; không có việc cho A0. Các Q-38, Q-62 đến Q-65 của P09 vẫn mở dù hồ sơ coi như chốt; README nói P10 không xét trạng thái "chờ xác nhận" nhưng không nói các Q liên quan có coi là đã đóng không.
    - Xử lý: không thêm Q, không đóng Q; ghi một câu ở đầu artifact rằng P10 kế thừa các Q, ASM đó.

17. Mục 4, Format: các mục F2 ("Trách nhiệm") và AC-B-PaymentGateway.
    - Gặp: NFR-10 (thu tiền) và NFR-12 (SMS mã xác thực) cho thấy hai subsystem còn năng lực chưa có trách nhiệm trong AC (UC-010, UC-003 chưa có P07). Quy tắc "lấy từ trách nhiệm của lớp phân tích nguồn" không cho thêm.
    - Xử lý: chỉ liệt kê trách nhiệm từ AC; thêm ghi chú dưới F2 nêu hai năng lực còn thiếu.

Không có hiện tượng quá tải ngữ cảnh: P09 dài nhưng chỉ cần F3 đến F7, F11 và phần kiểm soát; P08 F3 có dòng rất dài nhưng đọc được.
