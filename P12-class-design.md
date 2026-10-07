# P12 - Thiết kế lớp (Class Design)

## 1. Mục đích

Bước này biến các lớp phân tích và phần tử thiết kế đã xác định ở P10 thành lớp thiết kế đủ chi tiết để lập trình: mỗi lớp có trách nhiệm rõ, operation có chữ ký đầy đủ, thuộc tính có kiểu và visibility, quan hệ giữa các lớp được chọn đúng loại, lớp có hành vi phụ thuộc trạng thái có state machine. Trình tự làm việc gồm sáu hoạt động: tạo lớp thiết kế ban đầu, định nghĩa operation và method, định nghĩa quan hệ, định nghĩa trạng thái, định nghĩa thuộc tính, vẽ class diagram. Đầu ra là nguồn cho P13 (mô hình dữ liệu từ lớp persistent), X1 (review thiết kế) và X2 (thiết kế unit test theo phương thức).

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md | Có | Ngôn ngữ đặt tên, công nghệ (kiểu dữ liệu, ngôn ngữ lập trình), chế độ giả định, mức chi tiết |
| Đầu vào | P10-design-elements.md | Có | Bảng ánh xạ AC --> phần tử thiết kế (mục F3, gồm cột PKG), bảng phần tử thiết kế mới do cơ chế kiến trúc, subsystem SS, interface IF, package PKG |
| Đầu vào | P08-analysis-model.md | Có | Trách nhiệm (dạng "// tênTráchNhiệm"), thuộc tính, bảng quan hệ có mã R-nn của lớp phân tích |
| Đầu vào | P07-uc-analysis/*.md | Có | Message trong sequence/communication diagram để suy ra operation |
| Đầu vào | P09-architecture.md | Có | Mẫu kiến trúc đã chọn (mục F3), layer và package (F4), quy tắc ánh xạ stereotype sang layer (F5), quy tắc phụ thuộc (F6) |
| Đầu vào | P11b-system-interfaces.md | Có nếu hệ thống có giao tiếp ngoài | Operation của interface (mục F3, đã có chữ ký), phần tử bên trong subsystem đã được cấp mã DC (mục F5) |
| Đầu vào | P11a-gui/screen-list.md và SCR-nn-*.md | Có nếu có giao diện người dùng | Thiết kế lớp boundary giao diện |
| Đầu vào | P04-uc-specs/*.md | Có | Bước luồng, dữ liệu vào/ra, điều kiện hợp lệ |
| Đầu vào | P06-supplementary-spec.md | Có | BR (tiền/hậu điều kiện, guard), NFR (hiệu năng, bảo mật ảnh hưởng tới tách lớp) |
| Đầu vào | P05-glossary.md | Không | Đặt tên nhất quán |
| Đầu ra | P12-class-design.md (hoặc P12-class-design/<PKG-nn>[-<PKG-mm>...]-<slug>.md khi chạy theo package) | Có | Đặc tả lớp, operation, thuộc tính, quan hệ, state machine |
| Đầu ra | diagrams/P12-class-<PKG hoặc phạm vi>.drawio | Có | Class diagram theo package |
| Đầu ra | diagrams/P12-state-<DC>.drawio | Có nếu có lớp phụ thuộc trạng thái | State machine của từng lớp |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md và các file đầu vào ở bảng trên.
- Hệ thống nhỏ (khoảng dưới 15 lớp thiết kế, tính cả interface và lớp bên trong subsystem): chạy một lần cho toàn hệ thống, đầu ra một file P12-class-design.md.
- Từ khoảng 15-20 lớp trở lên: chạy lặp theo package, mỗi lần tối đa khoảng 15-20 lớp (một package, hoặc nhóm package có quan hệ chặt nếu tổng không vượt ngưỡng). Mỗi lần một file P12-class-design/<PKG-nn>-<slug>.md; lần chạy gồm nhiều package thì nối các mã: P12-class-design/<PKG-nn>-<PKG-mm>-<slug>.md (Conventions C4). Lần chạy sau đính kèm các file P12 đã có để giữ nhất quán tên và quan hệ liên package. Lý do ngưỡng: mỗi lớp sinh trung bình 5-10 dòng qua F2, F5, F7; trên khoảng 20 lớp, đầu ra vượt khả năng duyệt trong một lần đọc và dễ bị cắt.
- Đính kèm tối thiểu cho mỗi lần: P07 của các UC có lớp trong phạm vi (không đính kèm P07 của UC khác), P08, P09, P10, phần P11b của các SS mà phạm vi dùng, SCR của P11a liên quan.
- Khi một lần chạy theo package vẫn quá dài, chia đầu ra thành hai lượt trên cùng file, ghi trong YEU_CAU_BO_SUNG: lượt 1 "Chỉ làm F1, F2, F4, F5, F9" (lớp, operation, ánh xạ message, quan hệ, package); lượt 2 "Làm F3, F6, F7, F8, F10, giữ nguyên F1, F2, F4, F5, F9 của lượt 1" (method, state machine, thuộc tính, sơ đồ, pattern), đính kèm kết quả lượt 1, tăng phiên bản. Lượt 2 được bổ sung vào F2 operation do sự kiện của state machine sinh ra.
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| PHAM_VI_THIET_KE | Có | Toàn hệ thống hay package nào trong lần chạy này |
| QUY_UOC_KIEU_DU_LIEU | Tuỳ chọn | Kiểu dùng cho tiền, ngày giờ, định danh, tập hợp khi dự án đã có quy ước |
| MAU_THIET_KE_DA_CHOT | Tuỳ chọn | Design pattern hoặc framework đã chốt buộc phải dùng |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù khác cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md (hồ sơ dự án) và các artifact đã chốt: P04, P05, P06, P07, P08, P09, P10, P11a, P11b (những file có đính kèm).
Đọc hồ sơ dự án trước để biết: NGON_NGU_TEN_PHAN_TU, CHE_DO_GIA_DINH, MUC_CHI_TIET, CONG_NGHE (ngôn ngữ lập trình và framework quyết định kiểu dữ liệu, cú pháp chữ ký).
Phạm vi lần chạy này:
{{PH:PHAM_VI_THIET_KE | Hướng dẫn: ghi "Toàn hệ thống" hoặc liệt kê mã PKG cần thiết kế trong lần chạy này; nếu chạy theo package, liệt kê thêm file P12 của package khác đã có để tham chiếu | Ví dụ: "Toàn hệ thống"; "PKG-03 Quản lý lịch hẹn (đã có P12-class-design/PKG-02-patient.md)"; "PKG-05 Xuất nhập kho"}}
Quy ước kiểu dữ liệu của dự án:
{{PH:QUY_UOC_KIEU_DU_LIEU | Hướng dẫn: [TUỲ CHỌN] kiểu dùng cho tiền tệ, ngày giờ, định danh, tập hợp, số lượng; dùng mặc định thì thay cả khối bằng "Không có" của ngôn ngữ trong CONG_NGHE | Ví dụ: "Tiền: BigDecimal, làm tròn 0 chữ số thập phân (VND); Ngày giờ: LocalDateTime; Định danh: Long; Tập hợp: List"; "Tiền: decimal; Ngày: DateOnly; Định danh: Guid"}}
Design pattern hoặc framework đã chốt:
{{PH:MAU_THIET_KE_DA_CHOT | Hướng dẫn: [TUỲ CHỌN] pattern hoặc cơ chế bắt buộc dùng do kiến trúc hoặc tổ chức quy định; không có thì thay cả khối bằng "Không có" | Ví dụ: "Truy cập dữ liệu qua Repository, mỗi aggregate một repository"; "Giao tiếp cổng thanh toán qua Adapter đã có trong P11b"}}

[Role]
Bạn là kiến trúc sư phần mềm hướng đối tượng, thành thạo UML 2.5.1, nguyên lý thiết kế (SOLID, GRASP, coupling/cohesion) và design pattern, có kinh nghiệm chuyển mô hình phân tích thành thiết kế lập trình được mà không thêm chức năng ngoài yêu cầu.

[Action]
Làm tuần tự các bước dưới đây. Mỗi bước có thể phát hiện thiếu sót ở bước trước trong cùng artifact; khi đó quay lại sửa trong artifact này. Nếu thiếu sót nằm ở artifact của bước trước (P04 đến P11b), không tự sửa mà ghi vào "Đề xuất sửa artifact trước".

Bước 0. Kiểm tra đầu vào.
- Kiểm tra placeholder theo Conventions C6.
- Lập danh sách phần tử trong phạm vi, từ bốn nguồn: (a) mọi dòng của bảng ánh xạ P10 mục F3 có kết quả là lớp thiết kế (DC) hoặc tách thành nhiều lớp; (b) bảng phần tử thiết kế mới do cơ chế kiến trúc của P10 (persistence, logging, bảo mật...); (c) các lớp bên trong subsystem đã được P11b cấp mã DC (mục F5 của P11b), là lớp thiết kế cần chi tiết hoá như mọi DC khác; (d) mọi interface IF thuộc phạm vi. Subsystem SS mà phạm vi chỉ dùng qua interface thì chỉ cần interface, không chi tiết hoá bên trong.
- Đọc mẫu kiến trúc đã chọn (P09 mục F3) và bảng quy tắc ánh xạ stereotype sang layer (P09 mục F5) để biết mỗi stereotype phân tích trở thành vai trò gì trong mẫu đích.
- Lập danh sách UC có lớp trong phạm vi tham gia (từ cột "Dùng trong UC" của P08).
- Interface IF được dùng trong phạm vi mà P11b chưa có chữ ký (P11b chưa chạy cho SS đó): đặt chữ ký tạm trong một bảng riêng "Chữ ký interface tạm" (IF, operation, lý do, message P07 nguồn), dùng chữ ký tạm trong F2, F4, và ghi Đề xuất sửa artifact trước: chạy P11b cho SS đó. Khi P11b có chữ ký, chạy lại P12 cho phạm vi này.

Bước 1. Tạo lớp thiết kế ban đầu.
1.1. Với mỗi AC ánh xạ sang DC: nếu AC đơn giản và biểu diễn một trừu tượng logic duy nhất thì ánh xạ thẳng thành một DC. Nếu AC phức tạp thì có thể tách thành nhiều lớp, trở thành package, hoặc trở thành subsystem (khi đó P10 phải đã quyết định; nếu P10 chưa quyết định mà bạn thấy cần, ghi đề xuất sửa P10).
1.2. Thiết kế lớp boundary:
- Boundary giao diện người dùng: xác định công cụ/framework giao diện trong CONG_NGHE; phần nào công cụ tự sinh (form, control chuẩn) thì không mô hình hoá chi tiết; mỗi màn hình SCR chính thường có một lớp boundary, các thành phần giao diện dùng lại (hộp thoại xác nhận, bảng phân trang) là lớp riêng dùng chung.
- Boundary với hệ thống/thiết bị ngoài: thường là subsystem có interface IF (từ P10, P11b). Trong phạm vi lớp, mô hình hoá interface IF bằng lớp «interface» và lớp hiện thực (thường là adapter bọc giao thức ngoài). Lớp nghiệp vụ chỉ phụ thuộc vào interface, không phụ thuộc lớp hiện thực.
1.3. Thiết kế lớp entity:
- Entity thường thụ động và persistent. Đánh dấu lớp nào persistent (cần lưu trữ lâu dài) để P13 ánh xạ.
- Nếu một entity có nhiều thuộc tính mà chỉ một phần được dùng thường xuyên và NFR hiệu năng yêu cầu (ví dụ danh sách hàng nghìn bản ghi chỉ cần tên và mã), có thể tách thành lớp chính và lớp dữ liệu phụ nạp muộn (lazy), quan hệ 1 - 0..1. Chỉ tách khi có NFR hoặc lý do đo được, ghi lý do.
- Giá trị có quy tắc hợp lệ riêng (số tiền, khoảng thời gian, địa chỉ, mã vạch) có thể thành lớp giá trị (value object) thay vì kiểu nguyên thuỷ.
- Tập giá trị cố định (trạng thái, loại) thành «enumeration».
1.4. Thiết kế lớp control: với mỗi control, trả lời bốn câu hỏi và ghi kết luận: có thật cần không (control chỉ chuyển tiếp một lời gọi, không điều phối, không có quy tắc thì có thể gộp); có cần tách không (control điều phối nhiều UC khác nhau về tác nhân hoặc lý do thay đổi thì tách); căn cứ quyết định là độ phức tạp, khả năng thay đổi, phân tán và hiệu năng, quản lý giao dịch (transaction). Control thường là nơi đặt ranh giới giao dịch.
1.5. Lớp đã có ở P10 (cơ chế kiến trúc) và P11b (bên trong subsystem) giữ nguyên mã DC, chỉ chi tiết hoá. Lớp mới hoàn toàn (lớp tiện ích, factory, lớp giá trị, entity cho trạng thái chờ do NFR buộc lưu bền) chỉ được thêm khi có lý do thiết kế cụ thể (pattern, NFR, kiến trúc P09); cấp mã DC mới, cột "Nguồn AC" ghi "Thiết kế" kèm lý do. Interface mới do cơ chế thiết kế (interface kho dữ liệu, interface đồng hồ, interface lập lịch) cấp mã IF-nn nối tiếp số IF lớn nhất đã có trong P10, P11b và các file P12 đã đính kèm, ghi lý do và Đề xuất sửa artifact trước: cập nhật P10.
1.5a. Đặt tên và phân biệt control với controller: lớp control của phân tích (điều phối logic một UC) khác "controller" của MVC (thành phần giao diện tiếp nhận yêu cầu người dùng). Đọc P09 mục F3, F5 để biết mẫu kiến trúc; đặt tên lớp theo vai trò trong mẫu đích, không mặc định hậu tố Controller cho mọi lớp control. Ví dụ với layered kết hợp MVC: lớp control phân tích thành lớp dịch vụ ứng dụng (BorrowBookService, IssueStockService), còn hậu tố Controller dành cho lớp tiếp nhận yêu cầu ở Presentation (BorrowBookController). Với kiến trúc không có MVC, lớp control có thể giữ hậu tố Controller. Khi P10 đã đặt tên thì giữ nguyên tên P10, nếu thấy dễ nhầm thì ghi đề xuất sửa P10.
1.6. Mỗi lớp một mục đích: đặt câu "Lớp X chịu trách nhiệm ..." trong một câu không có liên từ "và" nối hai trách nhiệm khác lý do thay đổi. Nếu không viết được, tách lớp.
1.6a. Mốc thời gian đã đăng ký ở P07 (message hẹn, hẹn lại, huỷ mốc cho use case do tác nhân thời gian kích hoạt): thiết kế cơ chế lập lịch tương ứng theo P09 (bộ lập lịch bền vững hoặc quét định kỳ các đối tượng tới mốc). Gồm: interface lập lịch (IF mới nếu P10 chưa có) với operation hẹn, huỷ theo khoá của đối tượng; điểm vào khi tới mốc gọi control của use case do tác nhân thời gian kích hoạt; cách xử lý khi mốc tới lúc đối tượng đã đổi trạng thái (guard trong method). Nguồn ghi message P07 và mã use case do tác nhân thời gian kích hoạt.
1.7. Gán mỗi DC vào đúng một PKG: lấy cột PKG của bảng ánh xạ P10 mục F3 (hoặc bảng phần tử mới do cơ chế kiến trúc, hoặc package chứa subsystem ở P11b); với lớp mới cấp ở bước này, chọn layer theo bảng quy tắc ánh xạ stereotype sang layer ở P09 mục F5, sau đó chọn package trong layer đó theo P09 mục F4 và P10. Kiểm tra theo tiêu chí gom package ở mục [Format] F9. Không tạo PKG mới; nếu cần, ghi đề xuất sửa P09/P10.

Bước 2. Định nghĩa operation và method.
2.1. Duyệt từng sequence/communication diagram ở P07 và danh sách trách nhiệm của P08. Message và trách nhiệm ở đó ghi dạng "// tênTráchNhiệm" (lowerCamelCase, không tham số, không kiểu trả về, dữ liệu truyền đi nếu có ghi bằng lời trong ngoặc). Mỗi message gửi tới một đối tượng trở thành (hoặc được gộp vào) một operation của lớp nhận, có chữ ký đầy đủ: giữ gốc động từ của tên trách nhiệm khi nó đã nêu đúng kết quả, suy tham số từ dữ liệu truyền đi (phần ghi trong ngoặc, thuộc tính và dữ liệu của bước UC), suy kiểu trả về từ message trả về hoặc bước UC tiếp theo. Ví dụ: "// reserveSlot (khung giờ, bệnh nhân)" --> reserveSlot(slot: TimeSlot, patient: Patient): Appointment. Operation của interface IF lấy nguyên chữ ký đã chốt ở P11b mục F3, không đổi. Lập bảng ánh xạ message --> operation (F4).
2.2. Đặt tên operation: theo góc nhìn bên gọi, nêu kết quả chứ không nêu cách làm, nhất quán giữa các lớp (cùng loại việc cùng động từ).
2.3. Định nghĩa chữ ký: tên, tham số (hướng in/out/inout, tên, kiểu), kiểu trả về, visibility, phạm vi (instance hay classifier/static). Với mỗi tham số xem xét: truyền giá trị hay tham chiếu, có bị operation thay đổi không, có tuỳ chọn không, giá trị mặc định, miền giá trị hợp lệ.
2.4. Bổ sung operation không xuất hiện trong message nhưng cần cho lập trình: khởi tạo (constructor/factory), operation quản lý (thêm/bớt phần tử của tập hợp), sao chép, so sánh bằng (equality) khi lớp giá trị hoặc entity cần so sánh. Không thêm getter/setter hàng loạt; chỉ thêm khi có bên gọi cần.
2.5. Viết mô tả: mục đích, ý nghĩa từng tham số, giá trị trả về, ngoại lệ/lỗi và khi nào xảy ra, tiền điều kiện, hậu điều kiện (lấy từ BR, bước UC).
2.6. Với operation có xử lý không hiển nhiên, thiết kế method: thuật toán đặc biệt, đối tượng và operation khác được dùng, cách dùng tham số và thuộc tính, cách dùng quan hệ. Method dùng thời điểm hiện tại (so hạn, tính thời lượng, hết thời hạn) hoặc giá trị ngẫu nhiên: lớp chứa method nhận phụ thuộc đồng hồ hoặc bộ sinh qua constructor (không gọi trực tiếp đồng hồ hệ thống trong method), ghi quan hệ ở F5, để X2 kiểm thử được các giá trị biên thời gian.

Bước 3. Định nghĩa quan hệ.
3.1. Với mỗi cặp lớp có trao đổi message (mỗi link trong communication diagram), xác định vì sao bên gửi "thấy" bên nhận: qua thuộc tính (field) --> association; qua tham số, biến cục bộ, hoặc đối tượng toàn cục --> dependency. Dùng cây quyết định ở [Format] F5.
3.2. Với mỗi association: xét aggregation hoặc composition (quan hệ toàn thể - bộ phận), multiplicity hai đầu, tên vai trò, chiều điều hướng (chỉ giữ chiều mà interaction diagram thực sự dùng).
3.3. Xét generalization: chỉ khi thoả phép thử "là một loại của" và thay thế được (LSP). Xét realization giữa lớp và interface.
3.4. Kiểm tra phụ thuộc giữa package suy ra từ quan hệ lớp: không vòng, không phụ thuộc ngược layer, không nhảy layer (trừ khi P09 cho phép).

Bước 4. Định nghĩa trạng thái.
4.1. Tìm lớp có trạng thái đáng kể: lớp mà cùng một operation cho kết quả khác nhau tuỳ trạng thái, lớp có thuộc tính trạng thái trong phân tích, lớp có BR dạng "chỉ được ... khi ... đang ...". Không làm state machine cho lớp chỉ có một trạng thái tính toán hoặc ánh xạ thẳng tới hiện thực.
4.2. Xác định trạng thái từ giá trị đáng kể của thuộc tính động và từ sự tồn tại/không tồn tại của link.
4.3. Xác định sự kiện từ operation của lớp; xác định chuyển trạng thái, guard, action; thêm entry/do/exit nếu có hành vi gắn với việc vào, ở, ra khỏi trạng thái.
4.4. Ánh xạ ngược: mỗi sự kiện là một operation (thêm nếu thiếu); trạng thái được biểu diễn bằng thuộc tính (thường là enumeration) được đưa vào Bước 5; method của operation phải ghi rõ hành vi theo trạng thái.

Bước 5. Định nghĩa thuộc tính.
5.1. Nguồn thuộc tính: thuộc tính của lớp phân tích; danh từ trong UC/BR không trở thành lớp; thông tin mà mô tả method cần; thuộc tính biểu diễn trạng thái (Bước 4); thông tin lớp phải tự duy trì.
5.2. Với mỗi thuộc tính: tên, kiểu, visibility, multiplicity, giá trị mặc định, ràng buộc, phạm vi (instance/classifier), có phải derived không.
5.3. Thuộc tính trỏ tới lớp khác mà đã có association thì không lặp lại thành thuộc tính trong bảng thuộc tính (association chính là thuộc tính đó); ghi tên vai trò ở association.

Bước 6. Class diagram.
6.1. Vẽ một class diagram cho mỗi package trong phạm vi (thể hiện lớp của package và lớp ngoài package có quan hệ trực tiếp, lớp ngoài chỉ ghi tên). Với package chứa control, lớp ngoài package chỉ vẽ interface được dùng; dependency tới entity của package khác liệt kê ở F5, không vẽ, để sơ đồ không bị hàng chục cạnh. Class diagram tham gia UC (chỉ khi DAY_DU): vẽ thêm cho từng UC phức tạp (các lớp tham gia UC và quan hệ giữa chúng).
6.2. Lập bảng mô hình Node/Edge trước, sinh file .drawio sau, theo Conventions C7 và [Format] F8.

Bước 7. Áp dụng design pattern khi có lý do.
- Chỉ áp dụng pattern khi nhận ra đúng vấn đề mà pattern giải quyết trong chính thiết kế này (xem bảng ở [Format] F10) hoặc khi MAU_THIET_KE_DA_CHOT yêu cầu. Ghi vấn đề, lý do, lớp tham gia, phương án đơn giản hơn đã cân nhắc và vì sao không đủ.
- Không áp dụng pattern "để dự phòng" cho yêu cầu chưa có (vi phạm YAGNI).

Bước 8. Tự kiểm tra theo [Target], sửa những gì sửa được, ghi phần còn lại vào "Vấn đề còn mở".

[Format]
Đầu ra là file P12-class-design.md theo khung Conventions C5, gồm các mục theo thứ tự F1 đến F10, sau đó là các mục kiểm soát (Câu hỏi mở, Giả định nếu CO_NHAN, Đề xuất sửa artifact trước, Vấn đề còn mở). Với chạy theo package, tiêu đề ghi thêm mã PKG.

Quy ước chung cho mọi bảng:
- Mã lớp theo Conventions C3: DC-<TenLop>, ví dụ DC-AppointmentController. Interface giữ mã IF-nn đã cấp ở P10, P11b, không cấp mã DC; interface mới do cơ chế thiết kế cấp IF-nn nối tiếp theo Bước 1.5; bảng F1 ghi IF-nn ở cột DC, Loại "interface", ví dụ IF-02 ISmsNotifier. Tên lớp không chứa tiền tố mã.
- Tên theo NGON_NGU_TEN_PHAN_TU; mặc định PascalCase cho lớp, camelCase cho thuộc tính và operation, UPPER_SNAKE_CASE cho hằng và giá trị enumeration.
- Mã R-nn (quan hệ, nối tiếp dãy mã của P08) và ST-nn (state machine) đánh số liên tục trong toàn hệ thống: khi chạy theo package, tiếp tục từ số lớn nhất trong các file P12 đã đính kèm, không bắt đầu lại từ 01.
- Tham chiếu một operation trong văn bản và ở bước sau: DC-<TenLop>.<tenOperation>, thêm danh sách kiểu tham số khi có overload, ví dụ DC-Stock.reserve(Integer).
- Tham số kỹ thuật (kích thước lô, số lần thử lại nội bộ, kích thước pool, độ chính xác lưu trữ) là quyết định thiết kế theo Conventions C1 mục 7: chọn giá trị và ghi "Thiết kế: <lý do>" ở cột Ràng buộc hoặc Ghi chú, không cần Q, ASM. Giá trị nghiệp vụ (hạn mức, thời hạn, giá, phí, ngưỡng mà người dùng cảm nhận được) và multiplicity phải có nguồn BR, tài liệu nguồn; thiếu thì Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN).
- Kiểu dữ liệu: theo QUY_UOC_KIEU_DU_LIEU nếu có; nếu CONG_NGHE đã chốt ngôn ngữ thì dùng kiểu của ngôn ngữ đó; nếu chưa chốt dùng kiểu trung lập: String, Integer, Long, Decimal, Boolean, Date, DateTime, Duration, List<T>, Set<T>, Map<K,V>, tên lớp hoặc enumeration. Tiền tệ không dùng số thực dấu phẩy động (float/double) vì sai số làm tròn.

F1. Bảng lớp thiết kế
Cột lõi: | DC | Tên | Stereotype | PKG | Trách nhiệm | Nguồn AC |
Cột thêm: | Loại (class / abstract class / interface / enumeration / value object) | Persistent (Có / Không) | Ghi chú thiết kế |
- Định nghĩa: mỗi dòng là một lớp sẽ tồn tại trong mã nguồn (hoặc interface, enumeration).
- Stereotype: «boundary», «control», «entity» giữ từ phân tích; lớp thêm ở thiết kế dùng stereotype mô tả vai trò khi có ích («interface», «enumeration», «utility»), không bắt buộc.
- Trách nhiệm: một câu, bắt đầu bằng động từ, nêu một mục đích duy nhất.
- Nguồn AC: mã AC; nhiều lớp từ một AC thì mỗi lớp ghi cùng AC và ghi "tách từ AC-..." ở Ghi chú; lớp bên trong subsystem do P11b cấp mã ghi "P11b SS-nn"; lớp do cơ chế kiến trúc ở P10 ghi "P10 cơ chế <tên cơ chế>"; lớp thêm ở bước này ghi "Thiết kế: <lý do>". Lớp bên trong subsystem có visibility package (không public), trừ interface.
- Mức hợp lý: câu trách nhiệm không có hai mệnh đề độc lập; số operation public thường không quá khoảng 15-20 và thuộc tính không quá khoảng 10-15 (vượt ngưỡng không tự động là sai, nhưng phải kiểm tra lại mục đích lớp và ghi lý do nếu giữ); lớp chỉ có một operation chuyển tiếp nguyên lời gọi thì xem xét gộp.
- Lỗi thường gặp:
  - Quá lớn (god class): một lớp control xử lý mọi UC của một tác nhân; một entity vừa lưu dữ liệu vừa gửi email vừa xuất báo cáo. Dấu hiệu: tên chung chung (Manager, Handler, Processor, SystemService), câu trách nhiệm có "và".
  - Quá nhỏ: lớp không có hành vi, chỉ bọc một thuộc tính, không có quy tắc hợp lệ riêng; lớp control rỗng chỉ gọi thẳng entity.
  - Nhầm lẫn: giữ lớp phân tích nguyên trạng dù P10 đã quyết định thành subsystem; boundary chứa quy tắc nghiệp vụ; entity phụ thuộc vào lớp giao diện.
- Ví dụ đúng (quản lý kho): | DC-IssueStockController | IssueStockController | «control» | PKG-04 | Điều phối việc lập và xác nhận phiếu xuất kho, là ranh giới giao dịch khi trừ tồn | AC-C-IssueStockController | class | Không | |
- Ví dụ đúng (phòng khám): | DC-Appointment | Appointment | «entity» | PKG-02 | Lưu thông tin một lịch hẹn và kiểm soát vòng đời trạng thái của nó | AC-E-Appointment | class | Có | Có state machine ST-01 |
- Ví dụ sai: | DC-LibraryManager | LibraryManager | «control» | PKG-01 | Quản lý mượn, trả, gia hạn, tìm kiếm sách, gửi email nhắc và thống kê | ... | Sai: nhiều trách nhiệm với nhiều lý do thay đổi (god class); tách theo UC hoặc theo nhóm lý do thay đổi.

F2. Bảng operation
Cột lõi: | DC | Visibility | Chữ ký | Mô tả | Tiền/hậu điều kiện | Nguồn (message P07 / UC bước) |
Cột thêm: | Phạm vi (Instance / Classifier) | Ngoại lệ / lỗi |
- Định nghĩa: operation là dịch vụ mà lớp cung cấp, được gọi qua message. Method là phần hiện thực của operation (xem F3). Một operation có thể có nhiều method ở các lớp con (đa hình).
- Chữ ký theo UML: tenOperation(huong thamSo: Kieu = macDinh, ...): KieuTraVe. Hướng là in (mặc định, có thể bỏ), out, inout. Operation không trả về ghi ": void" hoặc bỏ kiểu trả về, thống nhất một cách trong cả artifact.
- Visibility: + public (bên ngoài gọi được), # protected (lớp con), - private (chỉ nội bộ), ~ package. Mặc định private cho operation hỗ trợ nội bộ; chỉ public những gì có bên gọi ngoài lớp trong interaction diagram.
- Phạm vi: Classifier (static, gạch chân trong sơ đồ) khi operation không cần trạng thái của một đối tượng cụ thể (factory tạo đối tượng, tiện ích thuần tính toán); còn lại là Instance.
- Mô tả: mục đích; ý nghĩa từng tham số; ý nghĩa giá trị trả về; mỗi ngoại lệ kèm điều kiện phát sinh.
- Tiền/hậu điều kiện: trích BR-nn hoặc bước UC; hậu điều kiện nêu trạng thái thay đổi (thuộc tính, link, trạng thái ST).
- Nguồn: "P07 UC-nnn msg <STT> // tênTráchNhiệm" hoặc "P08 AC-...// tênTráchNhiệm" hoặc "P11b IF-nn.<operation>" hoặc "Bổ sung: <lý do>" (khởi tạo, quản lý, equality) hoặc "ST-nn sự kiện <tên>".
- Mức hợp lý:
  - Mỗi message trong interaction diagram của phạm vi được gán cho đúng một operation của lớp nhận (có thể nhiều message cùng gán một operation).
  - Mỗi operation public có ít nhất một nguồn là message, IF, sự kiện ST hoặc lý do bổ sung.
  - Số tham số càng ít càng tốt; từ khoảng 4 tham số trở lên thì xem xét gom thành đối tượng tham số, nhưng chỉ truyền đối tượng khi bên nhận dùng phần lớn dữ liệu của nó; nếu chỉ dùng một hai trường thì truyền trường đó (tránh stamp coupling).
  - Không có tham số cờ (flag) quyết định operation làm việc khác nhau (control coupling); tách thành các operation riêng.
- Lỗi thường gặp:
  - Đặt tên theo cách làm hoặc theo bên nhận: loopThroughItemsAndSum() thay vì calculateTotal().
  - Giữ nguyên tên trách nhiệm phân tích dạng câu: "kiểm tra tồn kho đủ" thay vì hasSufficientStock(quantity: Integer): Boolean.
  - Operation "xử lý tất cả" nhận mã hành động: updateBook(action: Integer, book: Book) với action là thêm/sửa/xoá.
  - Mọi operation đều public; public cả operation chỉ dùng nội bộ.
  - Thiếu ngoại lệ cho luồng thay thế P04 (ví dụ "hết chỗ", "quá hạn mức").
  - Getter/setter cho mọi thuộc tính, kể cả thuộc tính trạng thái chỉ được đổi qua sự kiện.
- Ví dụ đúng (thư viện): | DC-Loan | + | renew(requestDate: Date): Date | Gia hạn phiếu mượn thêm một kỳ; trả về hạn trả mới; ném RenewalLimitExceededException khi đã gia hạn đủ số lần cho phép | Tiền: trạng thái ACTIVE, chưa quá hạn (BR-06). Hậu: dueDate tăng một kỳ, renewCount tăng 1 | P07 UC-007 msg 5 | Instance | RenewalLimitExceededException, LoanOverdueException |
- Ví dụ đúng (giao đồ ăn): | DC-DeliveryFeePolicy | + | calculateFee(distanceKm: Decimal, orderAmount: Decimal): Decimal | Tính phí giao theo khoảng cách và giá trị đơn | Tiền: distanceKm >= 0. Hậu: không đổi trạng thái | P07 UC-004 msg 8 | Instance | InvalidDistanceException |
- Ví dụ sai: | DC-OrderController | + | process(type: Integer, data: Object): Object | Xử lý đơn | | | Sai: tham số cờ, kiểu Object làm mất kiểm tra kiểu, tên không nêu kết quả, không có nguồn.

F3. Bảng thiết kế method (chỉ khi DAY_DU; khi GON vẫn làm cho operation có thuật toán hoặc quy tắc không hiển nhiên)
Cột: | DC.operation | Thuật toán / các bước chính | Đối tượng và operation khác được dùng | Cách dùng thuộc tính, tham số, quan hệ | Hành vi theo trạng thái (nếu có ST) |
- Định nghĩa: method mô tả cách hiện thực operation, đủ để người lập trình không phải đoán.
- Quy tắc: viết theo bước đánh số hoặc giả mã ngắn; nêu rõ ranh giới giao dịch nếu có; nêu quy tắc làm tròn, thứ tự kiểm tra.
- Mức hợp lý: vài bước đến khoảng mười bước; dài hơn là dấu hiệu operation làm quá nhiều việc, cần tách operation private.
- Lỗi thường gặp: chép lại mô tả operation (không thêm thông tin); viết mã nguồn đầy đủ; bỏ qua nhánh lỗi.
- Ví dụ đúng (quản lý kho): | DC-IssueStockController.confirmIssue(issueId: Long) | 1. Nạp phiếu xuất và các dòng. 2. Với mỗi dòng gọi Stock.reserve(quantity) theo thứ tự mã hàng tăng dần để tránh deadlock. 3. Nếu một dòng thiếu tồn thì huỷ toàn bộ giao dịch, trả lỗi kèm danh sách mã hàng thiếu. 4. Đổi trạng thái phiếu sang CONFIRMED | StockIssueRepository.findById, Stock.reserve, StockIssue.confirm | Giao dịch bao trọn bước 1-4 | StockIssue chỉ confirm được ở DRAFT |
- Ví dụ sai: | DC-IssueStockController.confirmIssue | Xác nhận phiếu xuất | | | | Sai: lặp lại tên, không có thông tin cách làm.

F4. Bảng ánh xạ message --> operation
Cột: | UC | STT message (P07) | Từ (AC/DC) | Đến (AC/DC) | Message phân tích (// tênTráchNhiệm) | Operation thiết kế (chữ ký đầy đủ) |
- Mỗi message của P07 trong phạm vi có một dòng. Message tới tác nhân người (hiển thị) ánh xạ tới operation của lớp boundary. Message gửi hệ thống ngoài ánh xạ tới operation của interface IF.
- Lỗi thường gặp: bỏ sót message trả về có dữ liệu (dữ liệu đó phải là kiểu trả về của operation tương ứng); ánh xạ message sang lớp khác lớp nhận mà không ghi lý do.

F5. Bảng quan hệ
Cột lõi: | ID | Lớp A | Lớp B | Loại | Multiplicity | Điều hướng | Lý do |
Cột thêm: | Vai trò (tên role ở đầu A / đầu B) | Căn cứ hiển thị (field / tham số / biến cục bộ / toàn cục) |
- ID: R-nn. Quan hệ có gốc từ bảng quan hệ của P08 giữ nguyên mã R-nn của P08 (kể cả khi đổi loại, ví dụ association thành composition, thì ghi thay đổi ở cột Lý do). Quan hệ mới cấp tiếp từ số lớn nhất đã có trong P08 và các file P12 đã đính kèm. Mã không đổi khi chạy lại.
- Loại: Association, Aggregation, Composition, Dependency, Generalization, Realization.
- Multiplicity: ghi dạng "A <m> - B <m>", trong đó m ở đầu A là số đối tượng A liên kết với một đối tượng B và ngược lại, ví dụ "A 1 - B 0..*" (một A có 0..* B, mỗi B thuộc đúng 1 A). Chỉ có ý nghĩa với association, aggregation, composition; để trống với dependency, generalization, realization.
- Điều hướng: "A --> B", "B --> A" hoặc "Hai chiều".
- Lớp A trong generalization là lớp con, Lớp B là lớp cha; trong realization Lớp A là lớp hiện thực, Lớp B là interface; trong dependency Lớp A là bên phụ thuộc (client), Lớp B là bên được dùng (supplier); trong aggregation/composition Lớp A là toàn thể, Lớp B là bộ phận.

Định nghĩa và quy tắc chọn loại:
- Association: quan hệ cấu trúc, đối tượng của lớp này giữ liên kết lâu dài tới đối tượng lớp kia (hiện thực bằng thuộc tính tham chiếu hoặc tập hợp). Mọi link trong communication diagram trở thành association trừ khi bên nhận được thấy qua tham số, biến cục bộ, hoặc toàn cục.
- Aggregation: association dạng toàn thể - bộ phận ("là một phần của"), bộ phận có thể tồn tại độc lập hoặc dùng chung. Khi phân vân giữa association và aggregation, chọn association.
- Composition: aggregation mạnh: bộ phận chỉ thuộc một toàn thể tại một thời điểm, toàn thể tạo và huỷ bộ phận, bộ phận bị xoá khi toàn thể bị xoá (bộ phận có thể bị toàn thể xoá sớm hơn). Multiplicity phía toàn thể luôn là 1 hoặc 0..1.
- Dependency: quan hệ không cấu trúc, tạm thời: bên nhận được thấy qua tham số của operation, biến cục bộ trong method, hoặc đối tượng toàn cục. Chọn quan hệ nhẹ nhất đủ dùng.
- Generalization: "là một loại của"; lớp con thừa hưởng cấu trúc và hành vi, phải thay thế được lớp cha ở mọi nơi dùng lớp cha (không làm yếu hậu điều kiện, không siết tiền điều kiện). Nếu chỉ muốn dùng lại mã mà không có quan hệ "là một loại", dùng composition hoặc delegation.
- Realization: lớp hiện thực mọi operation của interface.
- Association class (association có thuộc tính riêng, thường là quan hệ nhiều - nhiều như số lượng tồn của một mặt hàng tại một kho, điểm của một độc giả cho một đầu sách): ở mức thiết kế chuyển thành lớp thường có hai association tới hai lớp hai đầu (multiplicity 1 ở phía mỗi lớp đầu), ghi "từ association class, định danh bởi <LớpX> + <LớpY>" ở Ghi chú thiết kế của F1 để P13 dùng khoá ghép.

Cây quyết định association hay dependency (hỏi theo thứ tự):
1. Bên gửi có cần nhớ đối tượng nhận qua nhiều lời gọi, suốt vòng đời của nó không? Có --> association (field).
2. Đối tượng nhận được truyền vào như tham số của operation? --> dependency (parameter).
3. Đối tượng nhận được tạo và chỉ dùng trong một method? --> dependency (local). Nếu việc tạo tốn kém và nhiều đối tượng dùng chung một thể hiện, cân nhắc truyền qua tham số hoặc giữ làm field.
4. Đối tượng nhận là thể hiện dùng chung toàn cục (registry, cấu hình)? --> dependency (global). Hạn chế loại này vì dễ dẫn tới common coupling.

Mức hợp lý và điều hướng:
- Mỗi link trong interaction diagram có một quan hệ tương ứng (association hoặc dependency) giữa hai lớp.
- Điều hướng: chỉ giữ chiều mà interaction diagram cần gửi message. Hai chiều chỉ khi cả hai chiều đều được dùng thường xuyên và số đối tượng hai phía không nhỏ; nếu một chiều hiếm dùng hoặc số đối tượng phía đó nhỏ (có thể tìm bằng truy vấn) thì bỏ chiều đó.
- Multiplicity trả lời hai câu hỏi: quan hệ bắt buộc hay tuỳ chọn (cận dưới 0 hay lớn hơn 0), số đối tượng tối đa liên kết với một đối tượng phía kia. Ký hiệu: 1, 0..1, 0..* (hoặc *), 1..*, khoảng m..n, nhiều khoảng rời như 2, 4..6. Multiplicity phải có căn cứ từ BR hoặc tài liệu nguồn; thiếu căn cứ thì ghi Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN).
- Tên vai trò: đặt khi hai lớp có nhiều association hoặc khi vai trò không hiển nhiên từ tên lớp (ví dụ Doctor đóng vai trò "attendingDoctor" và "referringDoctor").

Lỗi thường gặp:
- Dùng association cho mọi quan hệ, kể cả khi lớp chỉ nhận đối tượng qua tham số.
- Dùng composition cho bộ phận được chia sẻ (một Book thuộc nhiều Loan theo thời gian: không phải composition).
- Dùng generalization để dùng lại mã: Stack kế thừa List, Queue kế thừa ArrayList; hoặc lớp con vô hiệu hoá operation của cha (ném "không hỗ trợ").
- Generalization cho vai trò có thể đổi theo thời gian (một nhân viên kho lúc là thủ kho lúc là kiểm kê viên): dùng association tới lớp vai trò thay vì lớp con.
- Association hai chiều mặc định, gây phụ thuộc vòng giữa package.
- Multiplicity "*" ở mọi đầu, không có căn cứ.
- Controller có association tới boundary (lớp nghiệp vụ biết lớp giao diện): thường là dependency ngược layer, vi phạm quy tắc layer.

Ví dụ đúng:
- Giao đồ ăn: | R-03 | DC-Order | DC-OrderLine | Composition | A 1 - B 1..* | A --> B | Dòng đơn chỉ tồn tại trong một đơn, bị xoá cùng đơn (BR-02) | order / lines | field |
- Thư viện: | R-07 | DC-LoanController | DC-FineCalculator | Dependency | | A --> B | Controller tạo và dùng bộ tính phạt trong một method | | local |
- Khách sạn: | R-11 | DC-Reservation | DC-Room | Association | A 0..* - B 1 | A --> B | Một đặt phòng giữ một phòng; phòng không cần biết danh sách đặt phòng vì tìm qua truy vấn | reservations / room | field |
- Phòng khám: | R-12 | DC-SmsGatewayAdapter | IF-02 | Realization | | A --> B | Adapter hiện thực ISmsNotifier | | |
Ví dụ sai:
- | R-05 | DC-Warehouse | DC-Product | Composition | A 1 - B 0..* | | Kho chứa hàng | Sai: một mặt hàng có thể có tồn ở nhiều kho và không bị huỷ khi xoá kho; quan hệ thực là giữa Warehouse và StockItem (tồn theo kho), Product là association.
- | R-09 | DC-ReferenceBook | DC-LoanableItem | Generalization | | | Tái sử dụng thuộc tính mã, tên sách | Sai: sách tra cứu không được cho mượn, lớp con phải ném lỗi ở checkOut() nên không thay thế được lớp cha (vi phạm LSP); tách lớp cha chung Item, chỉ LoanableItem có checkOut().

F6. State machine
Mỗi lớp có trạng thái đáng kể có một state machine mã ST-nn. Gồm ba bảng và một sơ đồ.

F6.1. Bảng trạng thái: | ST | Lớp | Trạng thái | Mô tả / điều kiện nhận biết (giá trị thuộc tính hoặc link) | entry | do | exit |
F6.2. Bảng chuyển trạng thái (bảng lõi): | ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích |
  Cột thêm: | STT | Operation tương ứng (DC.operation) | Nguồn (BR / UC bước) |
  Mỗi dòng là một chuyển trạng thái. Trạng thái nguồn của chuyển từ pseudo state ghi "(initial)" hoặc "(choice Cn)"; đích là final ghi "(final)".
F6.3. Bảng ánh xạ về mô hình lớp: | ST | Thuộc tính biểu diễn trạng thái | Kiểu (enumeration) | Operation được thêm/sửa |

Định nghĩa và quy tắc:
- State machine là đồ thị có hướng gồm trạng thái (node) nối bằng chuyển trạng thái (cung có hướng), mô tả vòng đời của một đối tượng phản ứng với sự kiện.
- Trạng thái: tình huống trong vòng đời đối tượng mà trong đó đối tượng thoả một điều kiện, thực hiện một hoạt động, hoặc chờ sự kiện. Đặt tên bằng tính từ hoặc phân từ (Draft, Confirmed, Overdue, Đang chờ), không đặt tên bằng động từ hành động.
- Sự kiện: kích hoạt chuyển trạng thái, thường là lời gọi operation của lớp, tín hiệu thời gian (after(24h), when(now > dueDate)) hoặc thay đổi điều kiện.
- Guard: biểu thức logic trong [ ], được đánh giá khi sự kiện xảy ra; chuyển chỉ xảy ra nếu guard đúng. Các guard của cùng sự kiện từ cùng trạng thái phải loại trừ nhau.
- Hành động (action/activity trên chuyển): việc làm ngay khi chuyển, ghi sau dấu "/".
- Nhãn chuyển trạng thái theo cú pháp: su_kien(tham_so) [guard] / hanh_dong.
- entry / hành động khi vào trạng thái; do / hoạt động kéo dài trong trạng thái; exit / hành động khi rời trạng thái.
- Pseudo state: initial (bắt buộc đúng một, là trạng thái khi đối tượng được tạo, cung từ initial không có sự kiện trừ sự kiện tạo); final (tuỳ chọn, có thể nhiều, là kết thúc vòng đời); choice (rẽ nhánh động theo guard; chỉ đoạn vào có sự kiện, các đoạn ra chỉ có guard, phải có nhánh [else] hoặc các guard phủ hết).
- Lớp nào cần state machine: đối tượng có vai trò được làm rõ bằng chuyển trạng thái; UC phức tạp do trạng thái điều khiển. Không cần cho đối tượng ánh xạ thẳng tới hiện thực, không bị điều khiển bởi trạng thái, hoặc chỉ có một trạng thái tính toán.
- Ánh xạ: sự kiện --> operation; trạng thái --> thuộc tính (thường là enumeration); method của operation ghi hành vi theo từng trạng thái (operation gọi ở trạng thái không cho phép thì làm gì: bỏ qua, ném ngoại lệ).

Mức hợp lý:
- Thường 3 đến khoảng 10 trạng thái cho một lớp nghiệp vụ; ít hơn 3 thường không cần state machine; nhiều hơn khoảng 10 thì xem xét trạng thái lồng (composite state) hoặc tách khía cạnh.
- Mọi trạng thái đạt được từ initial; mọi trạng thái không phải cuối có ít nhất một chuyển ra; với mỗi trạng thái, mỗi sự kiện có thể xảy ra đều có xử lý (chuyển, tự chuyển, hoặc ghi rõ "bị từ chối" trong method).
- Mỗi BR dạng "chỉ được X khi đang Y" xuất hiện thành guard hoặc thành việc sự kiện X không có chuyển từ trạng thái khác Y.

Lỗi thường gặp:
- Nhầm state machine với activity diagram: trạng thái đặt tên bằng động từ ("Kiểm tra tồn kho", "Gửi email"), sơ đồ mô tả luồng xử lý thay vì vòng đời đối tượng.
- Nhầm trạng thái của hệ thống/màn hình với trạng thái đối tượng.
- Guard chồng lấn (hai guard cùng đúng) hoặc không phủ hết (không có nhánh else).
- Sự kiện không tương ứng operation nào; trạng thái không có thuộc tính biểu diễn.
- Làm state machine cho lớp chỉ có tạo/xoá (ví dụ danh mục đơn vị tính).

Ví dụ đúng (phòng khám, lớp Appointment, BR: huỷ được nếu còn ít nhất 24 giờ trước giờ khám):
| ST-01 | DC-Appointment | (initial) | create | | / status = BOOKED | Booked |
| ST-01 | DC-Appointment | Booked | cancel(requestTime) | [startTime - requestTime >= 24h] | / release slot | Cancelled |
| ST-01 | DC-Appointment | Booked | checkIn | | | CheckedIn |
| ST-01 | DC-Appointment | Booked | when(now > startTime + 15min) | | / notify reception | NoShow |
| ST-01 | DC-Appointment | CheckedIn | complete | | | Completed |
(Cancelled, NoShow, Completed đều có chuyển tới (final) khi lưu trữ.)
Ví dụ đúng (quản lý kho, lớp StockIssue): Draft --submit--> PendingApproval; PendingApproval --approve [đủ tồn] / trừ tồn--> Confirmed; PendingApproval --approve [thiếu tồn]--> PendingApproval (tự chuyển, trả lỗi); PendingApproval --reject--> Draft.
Ví dụ sai: trạng thái "Nhập thông tin khách" --> "Kiểm tra phòng trống" --> "Lưu đặt phòng": đây là các bước xử lý (activity), không phải trạng thái của đối tượng Reservation.

F6.4. Sơ đồ state machine: bảng mô hình Node/Edge và file diagrams/P12-state-<DC>.drawio.
- Node: | ID | Loại (Initial / State / Choice / Final / Composite state) | Nhãn (tên + các dòng entry/do/exit) | Stereotype | Thuộc về | Ghi chú |
- Edge: | ID | Nguồn | Đích | Loại quan hệ (Transition) | Nhãn (su_kien [guard] / hanh_dong) | Ghi chú |
- ID node: <ST>-S<n> cho trạng thái, <ST>-I cho initial, <ST>-F<n> cho final, <ST>-C<n> cho choice; ID cạnh <ST>-T<STT>.
- Style draw.io: trạng thái theo Conventions C7 (State); initial và final theo C7 (Activity initial / final); choice: rhombus;html=1; chuyển trạng thái: endArrow=open;endFill=0;html=1; (nét liền, đầu mũi tên mở). Không dùng nét đứt cho chuyển trạng thái.
- Bố cục: initial ở trên cùng hoặc bên trái; luồng chính đi từ trên xuống hoặc trái sang phải; trạng thái cuối ở phía cuối luồng.

F7. Bảng thuộc tính
Cột lõi: | DC | Visibility | Tên | Kiểu | Multiplicity | Mặc định | Ràng buộc |
Cột thêm: | Phạm vi (Instance / Classifier) | Derived (Có: công thức / Không) | Nguồn (AC / BR / ST / method) | Mô tả |
- Định nghĩa: thuộc tính là thông tin mà đối tượng sở hữu và duy trì; giá trị của nó quan trọng, không có hành vi riêng.
- Cú pháp UML trong sơ đồ: visibility tenThuocTinh: Kieu[multiplicity] = macDinh {rangBuoc}. Thuộc tính derived có dấu "/" trước tên. Thuộc tính classifier gạch chân.
- Visibility: mặc định private (-); không dùng public cho thuộc tính có thể thay đổi (truy cập qua operation). Hằng (classifier, chỉ đọc) có thể public.
- Kiểu: kiểu cơ bản của ngôn ngữ, kiểu do dự án định nghĩa (enumeration, value object), hoặc lớp. Nếu kiểu là lớp có association thì mô hình hoá bằng association, không lặp trong bảng này.
- Multiplicity: mặc định 1 (bắt buộc, một giá trị); 0..1 nếu tuỳ chọn; tập hợp ghi [0..*] kèm kiểu tập hợp.
- Ràng buộc: miền giá trị, định dạng, duy nhất ({unique}), chỉ đọc ({readOnly}), trích BR hoặc điều kiện hợp lệ ở bảng dữ liệu P04.
- Derived: thuộc tính tính được từ thuộc tính khác. Chỉ lưu giữ (materialize) khi tính lại mỗi lần quá tốn thời gian hoặc khi phải đánh đổi hiệu năng lấy bộ nhớ; khi lưu giữ, ghi rõ công thức và thời điểm cập nhật.
- Nguồn thuộc tính: thuộc tính của AC; danh từ trong UC không thành lớp; thông tin cần cho method; thuộc tính biểu diễn trạng thái; thông tin lớp tự duy trì.
- Mức hợp lý: mỗi thuộc tính được ít nhất một operation dùng hoặc được hiển thị/lưu theo UC; không có thuộc tính trùng nghĩa trong cùng lớp; không có thuộc tính mà giá trị luôn có thể lấy từ lớp liên kết (trừ derived có lý do).
- Lỗi thường gặp:
  - Thuộc tính là khoá ngoại dạng mã thay vì association (thuộc tính customerId: Long trong Order trong khi đã có association Order --> Customer); chỉ chấp nhận khi quan hệ đi qua ranh giới subsystem hoặc aggregate và ghi lý do.
  - Thuộc tính gộp nhiều giá trị trong một chuỗi (address: "số nhà, phường, quận" khi UC cần lọc theo quận).
  - Kiểu số thực cho tiền; kiểu String cho ngày.
  - Thuộc tính thuộc về lớp khác (Loan có readerEmail trong khi Reader đã có email).
  - Thuộc tính trạng thái kiểu Boolean nhiều cờ (isPaid, isShipped, isCancelled) thay vì một enumeration theo state machine.
- Ví dụ đúng (quản lý kho): | DC-StockItem | - | quantityOnHand | Integer | 1 | 0 | {>= 0} | Instance | Không | AC-E-StockItem | Số lượng hiện có của một mặt hàng tại một kho |
- Ví dụ đúng (thư viện): | DC-Loan | - | /isOverdue | Boolean | 1 | | | Instance | Có: today > dueDate và returnDate rỗng | BR-05 | Không lưu, tính khi đọc |
- Ví dụ sai: | DC-Reservation | + | status | String | 1 | "new" | | ... | Sai: public, kiểu String cho trạng thái (phải là enumeration theo ST), giá trị mặc định không có trong tập trạng thái.

F8. Class diagram
- Danh sách sơ đồ: | Sơ đồ | Phạm vi (PKG / UC) | File .drawio | Số lớp |
- Với mỗi sơ đồ, bảng mô hình:
  - Node: | ID | Loại (Class / Interface / Enumeration / Package / Note) | Nhãn (tên lớp) | Stereotype | Thuộc về (PKG) | Ghi chú (lớp ngoài package: "tham chiếu") |
  - Edge: | ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú |
  - ID node trùng mã DC (interface dùng mã IF-nn); ID cạnh trùng mã R-nn; Nguồn của cạnh là Lớp A, Đích là Lớp B theo đúng quy ước vai trò ở F5 (con/cha, hiện thực/interface, client/supplier, toàn thể/bộ phận).
- Nội dung ngăn thuộc tính và ngăn operation của mỗi lớp lấy đúng từ F7, F2 (không thêm, không bớt). Sơ đồ phạm vi UC có thể ẩn thuộc tính và operation không liên quan, ghi "..." ở cuối ngăn.
- Quy tắc ngữ nghĩa UML:
  - Hướng cạnh: generalization và realization đi từ lớp con/lớp hiện thực tới lớp cha/interface, đầu tam giác rỗng ở phía cha/interface. Dependency đi từ client tới supplier, nét đứt đầu mở. Association điều hướng một chiều có đầu mở ở phía được điều hướng tới. Aggregation/composition có hình thoi ở phía toàn thể (rỗng cho aggregation, đặc cho composition).
  - Multiplicity đặt sát đầu cạnh tương ứng; tên vai trò đặt cùng đầu với multiplicity.
  - Tên lớp abstract in nghiêng; thành viên classifier gạch chân; stereotype trong « » phía trên tên lớp.
  - Không vẽ cùng lúc association và dependency giữa cùng một cặp lớp cùng chiều.
- Style draw.io:
  - Lớp: style Class ở Conventions C7; ngăn tên có stereotype: value="«entity»&lt;br&gt;&lt;b&gt;Appointment&lt;/b&gt;" với html=1 (khi đó bỏ fontStyle=1 ở cell cha nếu muốn chỉ in đậm tên). Mỗi ngăn thuộc tính, operation là một cell con style text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1; ; đường ngăn cách là cell con style line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;html=1; . Nhiều thuộc tính trong một ngăn ngăn cách bằng &lt;br&gt;.
  - Lớp abstract: thêm fontStyle=3 (đậm nghiêng) cho tên. Thành viên classifier: bọc bằng &lt;u&gt;...&lt;/u&gt;.
  - Cạnh theo bảng style ở Conventions C7, thêm edgeStyle=orthogonalEdgeStyle; composition: endArrow=none;startArrow=diamondThin;startFill=1;endFill=0; với source là lớp toàn thể; association điều hướng: endArrow=open;endFill=0; multiplicity và vai trò đặt bằng cell nhãn con của cạnh (style edgeLabel;resizable=0;html=1;align=left;verticalAlign=bottom;) với x=-1 (đầu nguồn) hoặc x=1 (đầu đích).
  - Bố cục: lớp cha phía trên lớp con; interface phía trên lớp hiện thực; boundary bên trái, control ở giữa, entity bên phải (hoặc trên xuống theo layer); toạ độ bội số 10, khoảng cách tối thiểu 40.
- Mức hợp lý: một sơ đồ nên đọc được trên một trang; khi vượt khoảng 20-25 lớp hoặc cạnh bắt chéo nhiều, tách theo package hoặc theo UC.
- Lỗi thường gặp: sơ đồ toàn hệ thống quá lớn không đọc được; lớp trong sơ đồ không có trong F1; quan hệ trong sơ đồ không có trong F5; mũi tên generalization vẽ ngược (từ cha tới con); dùng mũi tên tam giác đặc cho generalization.

Khung XML tối thiểu cho một lớp (tham khảo cấu trúc, thay nội dung):
```xml
<mxCell id="DC-StockItem" value="«entity»&lt;br&gt;&lt;b&gt;StockItem&lt;/b&gt;" style="swimlane;fontStyle=0;align=center;childLayout=stackLayout;horizontal=1;startSize=40;horizontalStack=0;resizeParent=1;collapsible=0;html=1;" vertex="1" parent="1">
  <mxGeometry x="400" y="120" width="220" height="130" as="geometry"/>
</mxCell>
<mxCell id="DC-StockItem-attr" value="- quantityOnHand: Integer = 0&lt;br&gt;- reorderLevel: Integer" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="DC-StockItem">
  <mxGeometry y="40" width="220" height="40" as="geometry"/>
</mxCell>
<mxCell id="DC-StockItem-sep" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;html=1;" vertex="1" parent="DC-StockItem">
  <mxGeometry y="80" width="220" height="10" as="geometry"/>
</mxCell>
<mxCell id="DC-StockItem-ops" value="+ reserve(quantity: Integer): void&lt;br&gt;+ isBelowReorderLevel(): Boolean" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;" vertex="1" parent="DC-StockItem">
  <mxGeometry y="90" width="220" height="40" as="geometry"/>
</mxCell>
```

F9. Gán package và kiểm tra phụ thuộc package
Bảng: | PKG | Lớp (DC) | Phụ thuộc vào PKG (suy từ F5) | Hợp lệ theo P09 (Có / Không: lý do) |
- Kiểm tra gán package theo P10 A3; vi phạm ghi đề xuất sửa P10.
- Chỉ lớp public của package được tham chiếu từ ngoài package; lớp chỉ dùng nội bộ đặt visibility package/private.
- Phụ thuộc package: không có phụ thuộc vòng (A dùng B và B dùng A); package layer dưới không phụ thuộc package layer trên, kể cả realization (interface đặt ở layer của lớp hiện thực hoặc thấp hơn, P09 A5); phụ thuộc không nhảy qua layer, trừ khi P09 cho phép. Vi phạm phải được ghi ở "Vấn đề còn mở" kèm cách khắc phục (đảo phụ thuộc bằng interface do layer dưới định nghĩa và layer trên hiện thực, chuyển interface xuống layer dưới, tách package).

F10. Design pattern đã áp dụng
Bảng: | Pattern | Vấn đề trong thiết kế này | Lớp tham gia (vai trò trong pattern) | Lý do chọn | Phương án đơn giản hơn đã xét |
Gợi ý nhận diện (chỉ áp dụng khi dấu hiệu có thật trong thiết kế):

| Dấu hiệu | Pattern cân nhắc |
|---|---|
| Một thuật toán có nhiều biến thể chọn theo loại/cấu hình, lộ ra bằng switch/if theo loại (phí giao theo vùng, cách tính phạt theo loại tài liệu) | Strategy |
| Hành vi của lớp thay đổi rõ rệt theo trạng thái, state machine có nhiều trạng thái và nhiều operation phải kiểm tra trạng thái | State |
| Nhiều đối tượng cần được báo khi một đối tượng thay đổi, bên phát không nên biết bên nhận cụ thể (tồn dưới ngưỡng báo mua hàng và báo quản lý) | Observer |
| Giao diện của hệ thống/thiết bị ngoài không khớp interface hệ thống mong đợi (cổng SMS, cổng thanh toán, máy quét mã vạch) | Adapter |
| Cần một điểm vào đơn giản cho một subsystem phức tạp | Facade |
| Lớp cần tạo đối tượng mà loại cụ thể phụ thuộc cấu hình hoặc dữ liệu | Factory Method / Abstract Factory |
| Các bước của một quy trình cố định, một vài bước khác nhau theo biến thể | Template Method |
| Cấu trúc cây toàn thể - bộ phận xử lý đồng nhất (danh mục lồng nhau, vị trí kho khu - dãy - kệ - ô) | Composite |
| Cần thêm trách nhiệm cho đối tượng một cách linh hoạt mà không tạo bùng nổ lớp con | Decorator |
| Cần đóng gói yêu cầu để xếp hàng, ghi nhật ký, hoàn tác | Command |
| Tách truy cập dữ liệu khỏi logic nghiệp vụ | Repository / Data Mapper |

- Singleton: chỉ dùng khi thật sự cần đúng một thể hiện và không thể truyền qua tham số; ghi rõ rủi ro phụ thuộc toàn cục (common coupling) và khó thay thế khi test.
- Lỗi thường gặp: áp dụng pattern cho biến thể chưa có trong yêu cầu; dùng tên pattern làm tên lớp mà cấu trúc không đúng pattern; tạo interface cho mọi lớp mà chỉ có một hiện thực và không có lý do thay thế (trừ interface với hệ thống ngoài và interface để đảo phụ thuộc layer).
- Nếu không áp dụng pattern nào, ghi "Không có".

[Target]
Trả lời Đạt/Không đạt cho từng câu, sửa trước khi trả kết quả; mục không đạt còn lại ghi vào "Vấn đề còn mở".
Lớp
1. Mọi DC trong P10 (bảng ánh xạ và bảng cơ chế kiến trúc) và mọi DC bên trong subsystem do P11b cấp mã, thuộc phạm vi, đều có trong F1 với đúng mã đã cấp; mọi lớp trong F1 có nguồn (AC, P11b SS-nn, P10 cơ chế, hoặc lý do thiết kế).
1a. Tên lớp phản ánh vai trò trong mẫu kiến trúc của P09; không nhầm lớp control phân tích với controller của MVC.
1b. Mọi quan hệ có gốc ở P08 giữ mã R-nn của P08; quan hệ mới cấp mã tiếp theo.
2. Tên lớp rõ nghĩa, là danh từ, không trùng, dùng thuật ngữ trong glossary.
3. Mỗi lớp có một trừu tượng rõ ràng; câu trách nhiệm không nối hai trách nhiệm khác lý do thay đổi.
4. Thuộc tính và hành vi của mỗi lớp liên quan chức năng với nhau.
5. Generalization chỉ dùng khi thoả "là một loại của" và lớp con thay thế được lớp cha.
6. Vòng đời đầy đủ của đối tượng được mô tả (tạo, thay đổi, huỷ/lưu trữ) cho lớp persistent.
Operation
7. Mọi message trong interaction diagram thuộc phạm vi đã được gán operation (F4 đủ dòng).
8. Mọi operation public có nguồn; không có operation thừa không ai gọi.
9. Tên operation mô tả kết quả theo góc nhìn bên gọi, dễ hiểu, nhất quán.
10. Chữ ký đầy đủ: tham số có hướng (khi khác in), tên, kiểu; kiểu trả về; visibility; không có tham số cờ.
11. Mỗi luồng thay thế/ngoại lệ trong P04 liên quan có ngoại lệ hoặc giá trị trả về tương ứng.
12. Đặc tả method có cho mọi operation không hiển nhiên; method dùng thời điểm hiện tại hoặc giá trị ngẫu nhiên nhận đồng hồ, bộ sinh qua constructor; mốc thời gian đăng ký ở P07 có cơ chế lập lịch (Bước 1.6a).
Quan hệ
13. Mỗi link trong interaction diagram có quan hệ tương ứng; loại association/dependency đúng theo cây quyết định F5.
14. Aggregation/composition đúng ngữ nghĩa toàn thể - bộ phận; composition có multiplicity phía toàn thể 1 hoặc 0..1.
15. Multiplicity có căn cứ; tên vai trò có khi cần.
16. Điều hướng chỉ giữ chiều được dùng.
17. Không có phụ thuộc vòng giữa package; không phụ thuộc hoặc realization ngược layer.
Trạng thái
18. Lớp có BR phụ thuộc trạng thái đều có state machine; lớp không cần thì không vẽ.
19. State machine có đúng một initial; mọi trạng thái đạt được; guard cùng sự kiện loại trừ nhau.
20. Mọi sự kiện ánh xạ tới operation; trạng thái được biểu diễn bằng thuộc tính.
Thuộc tính
21. Mọi thuộc tính có kiểu, visibility; không có thuộc tính public thay đổi được.
22. Mọi thuộc tính cần cho UC hoặc method; không trùng với association.
23. Thuộc tính derived có công thức và lý do nếu được lưu.
Sơ đồ và định dạng
24. Bảng Node/Edge khớp F1, F2, F5, F7; file .drawio khớp bảng, XML hợp lệ, không nén, không chồng node.
25. Pattern áp dụng đều có vấn đề cụ thể và lý do; không có pattern "dự phòng".
26. Không đổi tên, mã phần tử đã chốt ở bước trước; mọi thay đổi đề nghị nằm ở "Đề xuất sửa artifact trước".
27. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho bước thiết kế lớp; có ưu tiên cao hơn quy tắc mặc định của bước (trừ Conventions C1); không có thì thay cả khối bằng "Không có" | Ví dụ: "Mọi entity có thuộc tính createdAt, updatedAt do framework tự điền, không cần liệt kê trong bảng thuộc tính."; "Không vẽ class diagram theo UC, chỉ theo package."; "Operation trả lỗi bằng kiểu Result thay vì ngoại lệ."}}
````

## 5. Ghi chú cho người dùng

- Kết quả quá dài hoặc bị cắt: chạy theo package, từ khoảng 15-20 lớp trở lên; vẫn dài thì chia hai lượt (mục 3). Bắt đầu từ package ở layer thấp (entity, dịch vụ dùng chung) rồi tới layer cao, để lần chạy sau tham chiếu được lớp đã có.
- Thiếu operation hoặc operation không có nguồn: thường do P07 thiếu message hoặc sequence diagram chưa đủ luồng thay thế. Chạy lại P07 cho UC liên quan, sau đó chạy lại P12.
- Multiplicity hoặc guard bị ghi thành câu hỏi mở: tài liệu nguồn không nêu số lượng hoặc điều kiện. Bổ sung tài liệu nguồn hoặc chuyển CHE_DO_GIA_DINH sang CO_NHAN nếu chấp nhận giả định.
- Lớp quá lớn sau khi chạy: yêu cầu AI tách theo lý do thay đổi, rồi chạy X1 để kiểm tra cohesion.
- Dùng độc lập (không chạy các bước trước): đính kèm mô tả lớp phân tích (hoặc danh sách khái niệm và trách nhiệm) và sequence diagram tự vẽ; thay mã AC bằng tên khái niệm; các cột nguồn ghi tên tài liệu đính kèm.
- Sau khi chốt P12, chạy P13 (mô hình dữ liệu cho lớp Persistent = Có), X1 (review), X2 (unit test).

## 6. Căn cứ

- OMG Unified Modeling Language (UML) 2.5.1: Classes (Class, Property, Operation, Association, Generalization, Dependency, Interface Realization), State Machines.
- Booch G., Rumbaugh J., Jacobson I., The Unified Modeling Language User Guide, 2nd ed.
- Fowler M., UML Distilled, 3rd ed.: class diagram, state machine diagram, aggregation và composition.
- Ambler S., The Elements of UML 2.0 Style: quy tắc đặt tên, bố cục class diagram và state machine diagram.
- Larman C., Applying UML and Patterns, 3rd ed.: GRASP (Information Expert, Creator, Controller, Low Coupling, High Cohesion, Pure Fabrication, Indirection, Protected Variations), chuyển từ interaction diagram sang class diagram, visibility (attribute, parameter, local, global).
- Martin R. C., Agile Software Development: Principles, Patterns, and Practices: SRP, OCP, LSP, ISP, DIP; nguyên lý package.
- Gamma E., Helm R., Johnson R., Vlissides J., Design Patterns: Elements of Reusable Object-Oriented Software.
- Fowler M., Patterns of Enterprise Application Architecture: Repository, Data Mapper, Value Object.
- Meyer B., Object-Oriented Software Construction: thiết kế theo hợp đồng (tiền điều kiện, hậu điều kiện).
