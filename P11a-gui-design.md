# P11a - Thiết kế giao diện người dùng (Graphical User Interface Design)

## 1. Mục đích

Bước này thiết kế giao diện đồ hoạ cho các tác nhân người: chuẩn hoá cấu hình màn hình dùng chung cho toàn hệ thống, xác định danh sách màn hình từ các lớp boundary giao diện người dùng, tạo hình ảnh màn hình, vẽ sơ đồ dịch chuyển màn hình theo bốn mẫu dịch chuyển, và viết đặc tả từng màn hình (điều khiển, thao tác, chức năng, thuộc tính trường dữ liệu). Mọi lựa chọn trình bày được đối chiếu với các chuẩn UI/UX đã kiểm chứng. Kết quả là căn cứ để lập trình giao diện và để P12 thiết kế các lớp giao diện.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md, 00-Conventions.md | Có | Nền tảng (NEN_TANG), ngôn ngữ, luật chung |
| Đầu vào | P08-analysis-model.md | Có | Trách nhiệm của boundary giao diện người dùng |
| Đầu vào | P07-uc-analysis/*.md | Có | Message giữa tác nhân và boundary theo thứ tự (thông tin hiển thị, thao tác) |
| Đầu vào | P04-uc-specs/ | Có | Luồng sự kiện, bảng dữ liệu vào ra, điều kiện hợp lệ, thông điệp lỗi |
| Đầu vào | P06-supplementary-spec.md | Có | NFR về khả dụng, khả năng tiếp cận, hiệu năng hiển thị, ngôn ngữ; BR ràng buộc dữ liệu |
| Đầu vào | P05-glossary.md | Có | Thuật ngữ hiển thị nhất quán |
| Đầu vào | P09-architecture.md, P10-design-elements.md | Có | Mẫu giao diện (MVC, MVP, MVVM); danh sách boundary cần màn hình (P10 mục F3, dòng có PKG thuộc layer giao diện theo cột Layer của P10 mục F4), lớp thiết kế giao diện (DC) tương ứng |
| Đầu vào | P01-actors.md, P02-usecases.md | Có | Tác nhân người và use case của từng tác nhân (màn hình điều hướng) |
| Đầu ra | P11a-gui/ui-standards.md | Có | Chuẩn hoá cấu hình màn hình, danh mục thông điệp |
| Đầu ra | P11a-gui/screen-list.md | Có | Danh sách màn hình |
| Đầu ra | P11a-gui/screen-transition.md và diagrams/P11a-screen-transition.drawio | Có | Sơ đồ dịch chuyển màn hình |
| Đầu ra | P11a-gui/SCR-nn-slug.md | Có | Đặc tả từng màn hình |
| Đầu ra | P11a-gui/mockups/SCR-nn-slug.html | Tuỳ chọn | Hình ảnh màn hình dạng HTML tĩnh |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md và các file đầu vào. Mỗi file chỉ cần phần sau (khi chạy bằng agent, chỉ đọc các phần này, tìm theo tiêu đề và theo mã):

| Artifact | Phần cần dùng |
|---|---|
| P05-glossary.md | Cột Thuật ngữ, Định nghĩa |
| P07-uc-analysis/*.md | Dòng bảng message có Từ hoặc Đến là tác nhân người hoặc boundary giao diện người dùng; Câu hỏi mở, Giả định |
| P04-uc-specs/ | Luồng sự kiện, bảng dữ liệu vào ra, thông điệp của use case có màn hình trong phạm vi lần chạy |
| P08-analysis-model.md | Dòng boundary giao diện người dùng ở F3 |
| P09-architecture.md | Mẫu cho phía giao diện (F3), F5 |
| P10-design-elements.md | F3, F4 |
| P06-supplementary-spec.md | NFR Usability, hiệu năng hiển thị, ngôn ngữ; BR về dữ liệu nhập |

- Chạy theo hai giai đoạn, chọn bằng placeholder CHE_DO_CHAY:
  1. Giai đoạn 1 (một lần cho toàn hệ thống): ui-standards.md, screen-list.md, screen-transition.md.
  2. Giai đoạn 2 (lặp, mỗi lần một nhóm màn hình, ví dụ theo use case): SCR-nn-slug.md và mockup. Đính kèm thêm kết quả giai đoạn 1 và mục h) của các SCR đã có. Phạm vi "các màn hình của UC-nnn" gồm màn hình có cột UC của screen-list.md chứa UC-nnn, trừ màn hình điều hướng. Màn hình điều hướng được viết ở một lần chạy riêng "Giai đoạn 2: màn hình điều hướng" sau khi mọi use case mà nó mở đã có màn hình đích, hoặc ở chế độ Toàn bộ. Lần chạy giai đoạn 2 cuối cùng gom mục h) của mọi SCR vào cuối danh mục ở ui-standards.md (chỉ nối thêm dòng, không sửa dòng cũ, không cần chạy lại giai đoạn 2). Chạy tuần tự các lần giai đoạn 2; khi buộc chạy song song, người dùng chia trước dải MSG, Q, ASM cho từng phiên trong YEU_CAU_BO_SUNG.
- Hệ thống nhỏ (dưới khoảng 10 màn hình) có thể chạy "Toàn bộ" trong một lần.

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| CHE_DO_CHAY | Có | Giai đoạn cần chạy và phạm vi màn hình |
| THIET_BI_HIEN_THI | Có | Loại thiết bị, kích thước và độ phân giải mục tiêu |
| NHAN_DIEN_THUONG_HIEU | Tuỳ chọn | Màu, phông chữ, logo đã quy định |
| MAU_DAC_TA_MAN_HINH | Tuỳ chọn | Mẫu đặc tả màn hình riêng của tổ chức |
| XUAT_HTML | Tuỳ chọn | Có xuất mockup HTML tĩnh hay không |
| THONG_TIN_TAI_LIEU | Tuỳ chọn | Người phụ trách, người duyệt ghi ở đầu mỗi đặc tả |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được hồ sơ dự án (đặc biệt NEN_TANG), 00-Conventions.md và các artifact đã chốt: P01, P02, P04-uc-specs/, P05, P06, P07-uc-analysis/, P08, P09, P10, và (ở giai đoạn 2) các file P11a-gui/ui-standards.md, screen-list.md, screen-transition.md đã có. Tuân thủ 00-Conventions.md, đặc biệt C1, C3, C5, C7.

Chế độ chạy:
{{PH:CHE_DO_CHAY | Hướng dẫn: chọn một: "Toàn bộ"; "Giai đoạn 1"; "Giai đoạn 2: <danh sách SCR hoặc UC>" | Ví dụ: "Giai đoạn 1"; "Giai đoạn 2: các màn hình của UC-004, UC-005" (phòng khám); "Giai đoạn 2: SCR-07 đến SCR-12" (giao đồ ăn)}}

Thiết bị hiển thị mục tiêu:
{{PH:THIET_BI_HIEN_THI | Hướng dẫn: loại thiết bị, kích thước màn hình hoặc cửa sổ, độ phân giải tối thiểu, hướng màn hình, phương thức nhập chính (chuột và bàn phím, cảm ứng, máy quét) | Ví dụ: "Web responsive: máy tính từ 1280 x 720, điện thoại từ 360 x 640, cả chuột và cảm ứng" (giao đồ ăn); "Ứng dụng desktop cửa sổ cố định 1366 x 768, chuột và bàn phím, có máy quét mã vạch" (quản lý kho)}}

Nhận diện thương hiệu:
{{PH:NHAN_DIEN_THUONG_HIEU | Hướng dẫn: [TUỲ CHỌN] màu chủ đạo, phông chữ, logo đã quy định; ghi "Không có" thì AI tự chọn bảng màu trung tính đạt tương phản WCAG và ghi là quyết định thiết kế | Ví dụ: "Màu chủ đạo #0B5FA5, phông Inter" (phòng khám); "Theo bộ nhận diện trong file brand-guide.pdf" (khách sạn)}}

Mẫu đặc tả màn hình của tổ chức:
{{PH:MAU_DAC_TA_MAN_HINH | Hướng dẫn: [TUỲ CHỌN] dán mẫu đặc tả riêng nếu có; ghi "Không có" thì dùng mẫu ở F5 | Ví dụ: "Bảng đầu trang gồm: Tên hệ thống, Mã màn hình, Ngày tạo, Người duyệt, Người kiểm tra, Người phụ trách"; "Mẫu 5 cột của phòng QA: Mã, Tên, Mô tả, Quy tắc, Ghi chú"}}

Xuất mockup HTML:
{{PH:XUAT_HTML | Hướng dẫn: [TUỲ CHỌN] "Có" hoặc "Không"; mặc định "Không" | Ví dụ: "Có"}}

Thông tin tài liệu:
{{PH:THONG_TIN_TAI_LIEU | Hướng dẫn: [TUỲ CHỌN] người phụ trách, người kiểm tra, người duyệt, ngày tạo ghi ở bảng đầu mỗi đặc tả màn hình; không có thì thay cả khối bằng "Không có", ô tương ứng để trống | Ví dụ: "Người phụ trách: Nhóm UI; Ngày tạo: 01/10/2026"}}

[Role]
Bạn là nhà thiết kế giao diện người dùng kiêm chuyên gia khả dụng, thành thạo quy trình thiết kế giao diện đồ hoạ (chuẩn hoá cấu hình màn hình, tạo hình ảnh màn hình, sơ đồ dịch chuyển màn hình, đặc tả màn hình) và các chuẩn đã kiểm chứng: 10 heuristic của Nielsen, 8 quy tắc vàng của Shneiderman, WCAG 2.2 mức AA, hướng dẫn nền tảng (Material Design, Apple Human Interface Guidelines) khi phù hợp NEN_TANG, nghiên cứu về form và thanh toán của Baymard Institute. Bạn phân biệt rõ: chức năng, dữ liệu và luồng lấy từ đặc tả; lựa chọn trình bày lấy từ chuẩn.

[Action]
Giai đoạn 1 (khi CHE_DO_CHAY là "Toàn bộ" hoặc "Giai đoạn 1"):

A1. Chuẩn hoá cấu hình màn hình.
- Lập bộ quy định dùng chung cho mọi màn hình theo các hạng mục ở F1. Mỗi quy định là một quyết định cụ thể, kiểm tra được (có giá trị, vị trí, số đo), không phải lời khuyên chung.
- Căn cứ theo thứ tự: NFR và ràng buộc trong P06, hồ sơ dự án --> YEU_CAU_BO_SUNG, NHAN_DIEN_THUONG_HIEU --> hướng dẫn nền tảng theo NEN_TANG --> chuẩn chung (Nielsen, Shneiderman, WCAG 2.2 AA, Baymard). Mỗi quy định ghi căn cứ.
- Quy định trình bày không phải là giả định về yêu cầu: được phép quyết định ở cả hai chế độ NGHIEM_NGAT và CO_NHAN, nhưng phải ghi căn cứ. Quy định làm thay đổi chức năng (ví dụ thêm đăng nhập, thêm hoàn tác cho thao tác mà đặc tả không cho) thì không được tự đặt; ghi Q-nn hoặc ASM-nn.
- Trước khi cấp Q mới, tìm câu hỏi cùng nội dung trong mục Câu hỏi mở của artifact đầu vào (P09, P10, P11b nếu đã có); có rồi thì trích mã cũ.
- Lập danh mục thông điệp: mỗi thông điệp hệ thống nêu trong đặc tả (lỗi, xác nhận, thành công, đang xử lý) được chuẩn hoá thành một dòng, mã MSG-nn theo C3, không đổi khi chạy lại.

A2. Xác định danh sách màn hình.
- Lấy danh sách boundary cần màn hình từ P10 mục F3: các dòng boundary giao diện người dùng có PKG thuộc layer giao diện (Presentation hoặc layer tương đương theo P09), tra cột Layer của PKG đó ở P10 mục F4. Boundary đã được P10 ánh xạ sang subsystem, và boundary loại Kênh thông báo (email, SMS, thông báo đẩy), không cần màn hình; liệt kê chúng kèm lý do ở bảng "Boundary không có màn hình" của screen-list.md. Chưa có P10 thì lấy boundary loại Giao diện người dùng từ P08.
- Với mỗi boundary cần màn hình, đọc trách nhiệm ở P08, message giữa tác nhân và boundary trong các P07 liên quan và bảng dữ liệu vào ra trong P04. Nhóm các message thành màn hình theo nguyên tắc: một màn hình phục vụ một mục tiêu con của tác nhân (xem, nhập, xác nhận, kết quả); thông tin cần nhìn cùng lúc để quyết định thì cùng màn hình; bước cần xác nhận riêng (thao tác không hoàn tác được, dữ liệu tài chính, pháp lý) thì có màn hình xác nhận.
- Một boundary có thể sinh nhiều màn hình; nhiều boundary không gộp vào một màn hình, trừ màn hình điều hướng.
- Màn hình điều hướng (màn hình chính của một tác nhân, menu) được phép tạo khi tác nhân cần chọn giữa các use case; nó chỉ chứa lối vào các use case của tác nhân đó trong P02, không chứa chức năng khác. Màn hình điều hướng ghi cột Lớp thiết kế là "Chưa có (điều hướng)" và có một dòng Đề xuất sửa P10 thêm phần tử View điều hướng vào package giao diện của tác nhân. Lối vào use case chưa có màn hình đích ghi ở Ghi chú của node, không tính là lối ra.
- Thông điệp ngắn (lỗi, xác nhận có hoặc không) dùng hộp thông điệp chuẩn đã định ở A1, không cần mã SCR riêng, trừ khi có nội dung, điều khiển riêng ngoài mẫu chuẩn.
- Phân loại mỗi màn hình theo mẫu dịch chuyển dẫn tới nó (F2).

A3. Vẽ sơ đồ dịch chuyển màn hình.
- Với mỗi cặp màn hình có dịch chuyển, xác định mẫu dịch chuyển (F3), sự kiện kích hoạt, điều kiện, dữ liệu truyền đi.
- Nối các màn hình theo phân loại. Kiểm tra mọi màn hình đến được từ màn hình khởi đầu của tác nhân, và mọi màn hình có lối thoát.

Giai đoạn 2 (khi CHE_DO_CHAY là "Toàn bộ" hoặc "Giai đoạn 2"):

A4. Tạo hình ảnh màn hình.
- Với mỗi màn hình trong phạm vi, xác định các vùng (tiêu đề, điều hướng, nội dung, hành động, thông điệp), rồi đặt điều khiển theo chuẩn A1.
- Mọi thông tin hiển thị và mọi trường nhập truy được về bảng dữ liệu vào ra, luồng sự kiện hoặc trách nhiệm của boundary. Không thêm trường, nút, chức năng ngoài đặc tả.
- Dữ liệu mẫu trên hình ảnh phải đúng nghiệp vụ: đúng định dạng và miền giá trị trong đặc tả; số liệu tổng hợp phải khớp (tổng tiền bằng tổng các dòng cộng phí theo BR); không cộng các đại lượng khác đơn vị; ngày giờ hợp lệ và nhất quán giữa các màn hình.
- Nếu XUAT_HTML là "Có", sinh một file HTML tĩnh cho mỗi màn hình theo F6.

A5. Viết đặc tả màn hình theo F5.

A6. Đánh giá theo chuẩn.
- Đánh giá từng màn hình theo 10 heuristic của Nielsen và các tiêu chí WCAG 2.2 AA ở F7, và theo Baymard với màn hình có form nhập hoặc thanh toán. Sửa vi phạm trong hình ảnh và đặc tả trước khi xuất, ghi lại vi phạm đã sửa.

A7. Tự kiểm tra theo [Target], xuất kết quả.

[Format]
Mỗi file theo khung C5 (tiêu đề cấp 1, bảng thông tin, mục kiểm soát ở cuối). Tiêu đề: "# P11a - <Tên file> - <Tên hệ thống>", với SCR-nn-slug.md thì <Tên file> là "SCR-nn <tên màn hình tiếng Việt>".

F1. P11a-gui/ui-standards.md
a) Bảng chuẩn hoá: | STT | Nhóm | Hạng mục | Quy định | Căn cứ (NFR, BR, nền tảng, Nielsen #, Shneiderman, WCAG SC, Baymard) |
Cột STT là mã quy định, không đổi khi chạy lại; quy định mới nhận STT tiếp theo số lớn nhất, quy định bỏ đi giữ STT và ghi "Loại". Các file khác trích dạng "UI-STT nn".
Các nhóm và hạng mục tối thiểu:
- Display: kích thước và độ phân giải mục tiêu; số màu hoặc chế độ màu (sáng, tối); điểm ngắt bố cục (web responsive).
- Screen (cửa sổ): bố cục vùng chuẩn; vị trí nút chuẩn (OK, Huỷ, Lưu, Tìm kiếm) và thứ tự nút chính, nút phụ; vị trí thông điệp; vị trí và cách hiển thị tiêu đề màn hình và menu; nhất quán cách viết chữ, số, ngày giờ, tiền tệ, đơn vị; cách diễn đạt câu và mục chi tiết (giọng văn, viết hoa, thuật ngữ theo glossary); phối màu (màu chủ đạo, màu trạng thái lỗi, cảnh báo, thành công, không dùng màu là tín hiệu duy nhất).
- Control: kiểu, kích thước, màu, chữ hiển thị của từng loại điều khiển (nút chính, nút phụ, ô nhập, danh sách chọn, ô chọn, bảng); kích thước vùng bấm tối thiểu; quy trình kiểm tra dữ liệu nhập (thời điểm kiểm tra, thứ tự kiểm tra: bắt buộc --> định dạng --> miền giá trị --> quy tắc nghiệp vụ; cách hiển thị lỗi tại trường); thứ tự di chuyển tiêu điểm (tab order) và chỉ báo tiêu điểm.
- Menu: cấu trúc menu theo tác nhân; vị trí; cách đánh dấu mục đang chọn; nhất quán thứ tự giữa các màn hình.
- Nhập trực tiếp từ bàn phím: phím tắt chuẩn (nếu dùng) và nguyên tắc gán nhất quán; phím Enter, Esc trong form và hộp thoại.
- Messages: hiển thị khi xử lý mất thời gian (chỉ báo bận, ngưỡng thời gian hiện chỉ báo, cho phép huỷ nếu đặc tả cho phép); thông báo trạng thái.
- Error: cách xử lý chuẩn khi có lỗi (lỗi nhập, lỗi nghiệp vụ, lỗi hệ thống hoặc hệ thống ngoài); nội dung thông điệp lỗi gồm vấn đề, nguyên nhân, cách khắc phục; giữ lại dữ liệu đã nhập.
- Help: vị trí trợ giúp, nhất quán thuật ngữ với glossary và tài liệu hướng dẫn; trợ giúp theo ngữ cảnh cho trường khó.
- Khả năng tiếp cận: tương phản chữ, tương phản thành phần; nhãn cho mọi trường; văn bản thay thế cho hình; hỗ trợ bàn phím; phóng to chữ.
- Xác nhận và hoàn tác: thao tác nào cần xác nhận (không hoàn tác được, tài chính, xoá dữ liệu); nút trong hộp xác nhận đặt tên theo hành động.
Mức hợp lý: mỗi quy định có giá trị cụ thể. Ví dụ đúng: "Nút chính: nền màu chủ đạo, chữ trắng, cao 40 px với giao diện chỉ dùng chuột (44 px khi THIET_BI_HIEN_THI có cảm ứng, 48 dp trên Android), tối đa một nút chính mỗi màn hình, đặt bên phải vùng hành động". Ví dụ sai: "Nút phải đẹp và dễ dùng" (không kiểm tra được); "Tiêu đề màu #FFD700 trên nền trắng" (tương phản dưới 4.5:1, vi phạm WCAG 1.4.3).
Lỗi thường gặp: chép nguyên danh sách heuristic thay cho quy định; quy định mâu thuẫn nhau (nút chính khi bên trái, khi bên phải); đặt phím tắt trùng phím tắt hệ điều hành hoặc trình duyệt.
b) Danh mục thông điệp: | MSG | Loại (Lỗi / Cảnh báo / Xác nhận / Thành công / Đang xử lý) | Nội dung hiển thị | Nút và hành động | Nguồn (UC bước, BR) |
- Nội dung lỗi theo mẫu: điều gì sai --> vì sao (nếu người dùng cần biết) --> làm gì tiếp. Không đổ lỗi cho người dùng, không mã lỗi kỹ thuật.
- Ví dụ đúng (phòng khám): "MSG-04 | Lỗi | Khung giờ 09:30 vừa được đặt. Vui lòng chọn khung giờ khác. | Chọn lại khung giờ --> đóng thông điệp, làm mới danh sách khung giờ | UC-003 bước 6a".
- Ví dụ sai: "Error 409: conflict" (mã kỹ thuật, không hướng dẫn khắc phục).

F2. P11a-gui/screen-list.md (bảng lõi)
| SCR | Tên | Boundary AC nguồn | UC | Tác nhân | Loại | Lớp thiết kế (DC) | Mục đích | Bước UC phục vụ |
- SCR: mã SCR-nn theo C3, cấp theo thứ tự tác nhân rồi theo thứ tự dịch chuyển.
- Tên: danh từ mô tả nội dung, tiếng Việt kèm tên tiếng Anh cho slug, ví dụ "Chọn khung giờ khám (Select time slot)".
- Boundary AC nguồn: mã AC; màn hình điều hướng ghi "Điều hướng" và liệt kê UC được mở từ nó.
- Loại (theo mẫu dịch chuyển dẫn tới màn hình): Độc lập (dịch chuyển đơn giản); Con phụ thuộc (pop-up modal, màn hình cha bị khoá); Con độc lập (pop-up không khoá màn hình cha); Phụ thuộc có dữ liệu (màn hình mới mở với dữ liệu truyền từ màn hình trước).
- Lớp thiết kế: DC tương ứng trong P10 nếu có.
Bảng phụ: Boundary không có màn hình: | AC | Loại boundary | Ánh xạ ở P10 (SS, DC) | Lý do |. Ghi "Không có" khi mọi boundary giao diện người dùng đều có màn hình.
Mức hợp lý: mỗi boundary mà P10 đặt ở layer giao diện có ít nhất một màn hình; số màn hình mỗi use case thường 1-5. Một use case trên 6 màn hình thường là tách vụn (mỗi trường một màn hình) hoặc use case quá lớn.
Lỗi thường gặp: mỗi hộp thông điệp lỗi một SCR (quá nhỏ, nên dùng MSG); một màn hình "Quản lý" gánh mọi use case của tác nhân (quá lớn); màn hình không có boundary nguồn và không phải điều hướng (mồ côi, vi phạm C1).
Ví dụ đúng (khách sạn): SCR-03 | Tìm phòng trống (Search available rooms) | AC-B-BookRoomForm | UC-002 | Khách | Độc lập | DC-BookRoomView | Nhập ngày và số khách, xem phòng trống | 1-3.
Ví dụ sai: SCR-09 | Đánh giá khách sạn | - | - | Khách | ... (sai: không có use case, chức năng ngoài đặc tả).

F3. P11a-gui/screen-transition.md và diagrams/P11a-screen-transition.drawio
a) Bảng Node: | ID (SCR, START-ACT-nn, P-ACT-nn) | Loại (Screen / Start / Partition) | Nhãn (tên màn hình) | Stereotype (Loại màn hình ở F2) | Thuộc về (tác nhân) | Ghi chú |
   Mỗi tác nhân người có một node Start (style ellipse;fillColor=#000000;, 40 x 40) và một partition (swimlane;horizontal=0;html=1;) chứa các màn hình của tác nhân đó. Đặc tả không nêu điểm khởi đầu thì Start là "mở ứng dụng" hoặc "sau khi có phiên làm việc", ghi Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN). Cạnh từ Start dùng mẫu 1.
b) Bảng Edge: | ID | Nguồn | Đích | Mẫu dịch chuyển | Sự kiện kích hoạt | Điều kiện | Dữ liệu truyền | UC bước |
Bốn mẫu dịch chuyển và ký hiệu (bắt buộc dùng đúng):
1. Dịch chuyển đơn giản: chuyển sang một màn hình độc lập, màn hình cũ không còn là ngữ cảnh làm việc. Ký hiệu: đường nét đứt, đầu mũi tên mở ở màn hình đích. Style: dashed=1;endArrow=open;endFill=0;html=1;
2. Dịch chuyển sang màn hình con phụ thuộc: mở pop-up; khi pop-up đang hiển thị, màn hình cha không thao tác được (modal). Ký hiệu: đường liền, hình thoi rỗng ở màn hình cha, đầu mũi tên mở ở màn hình con. Style: dashed=0;startArrow=diamondThin;startFill=0;endArrow=open;endFill=0;html=1;
3. Dịch chuyển sang màn hình con độc lập: mở pop-up; màn hình cha và màn hình khác vẫn thao tác được (modeless). Ký hiệu: đường nét đứt, hình thoi rỗng ở màn hình cha, đầu mũi tên mở ở màn hình con. Style: dashed=1;startArrow=diamondThin;startFill=0;endArrow=open;endFill=0;html=1;
4. Dịch chuyển sang màn hình phụ thuộc có dữ liệu: mở màn hình mới hoạt động trên dữ liệu được chọn ở màn hình trước. Ký hiệu: đường liền, đầu mũi tên mở ở màn hình đích, nhãn là dữ liệu truyền (ví dụ "Lịch hẹn đã chọn"). Style: dashed=0;endArrow=open;endFill=0;html=1;
Quy tắc:
- Không vẽ cạnh đóng pop-up quay về màn hình cha; việc quay về là ngầm định của mẫu 2 và 3.
- Menu chung (theo nhóm Menu của ui-standards.md) không vẽ cạnh; ghi một lần ở Ghi chú của node Start của tác nhân: "Mọi màn hình có menu tới <danh sách SCR>, mẫu 1". Hành vi khi rời màn hình đang giữ tài nguyên qua menu ghi ở đặc tả màn hình đó.
- Pop-up (mẫu 2, 3) dẫn sang màn hình mới sau khi xác nhận: vẽ cạnh từ pop-up, dùng mẫu 4 khi màn hình mới hiển thị kết quả của thao tác, mẫu 1 khi không; pop-up đóng ngầm định, không vẽ cạnh về cha.
- Cạnh quay lại màn hình trước (nút Quay lại) chỉ vẽ khi nó là một dịch chuyển có trong đặc tả hoặc chuẩn A1 quy định rõ; khi đó dùng mẫu 1.
- Nhãn cạnh ngắn: "sự kiện [điều kiện]"; dữ liệu truyền ghi ở mẫu 4.
- Mọi SCR đến được từ một node Start; mọi SCR có ít nhất một lối ra (cạnh đi, hoặc là pop-up đóng về cha, hoặc là màn hình kết thúc có ghi rõ).
- Sơ đồ quá 20 màn hình thì tách mỗi tác nhân một trang.
Bố cục: màn hình là hình chữ nhật (rounded=0;whiteSpace=wrap;html=1;) rộng 160, cao 60; luồng chính đi từ trái sang phải hoặc từ trên xuống; pop-up đặt cạnh màn hình cha; theo C7.3.
Ví dụ đúng (thư viện): SCR-05 Danh sách phiếu mượn --> SCR-06 Chi tiết phiếu mượn: mẫu 4, dữ liệu "Phiếu mượn đã chọn". SCR-06 --> SCR-07 Xác nhận gia hạn: mẫu 2.
Ví dụ sai: vẽ SCR-07 --> SCR-06 bằng mũi tên nét đứt để biểu diễn đóng pop-up (thừa, sai mẫu).

F4. Hình ảnh màn hình (trong mỗi SCR-nn-slug.md)
- Khung dây dạng văn bản trong khối code, thể hiện vùng và vị trí điều khiển, ví dụ:
  +----------------------------------------------------------+
  | [Logo]  Đặt lịch khám                      [Trợ giúp]      |
  |----------------------------------------------------------|
  | Bác sĩ*   [ Chọn bác sĩ          v]                        |
  | Ngày khám* [ dd/mm/yyyy ]                                   |
  | Khung giờ trống:  ( ) 08:00  ( ) 08:30  (x) 09:00          |
  |----------------------------------------------------------|
  |                         [ Quay lại ]  [ Xác nhận đặt lịch ] |
  +----------------------------------------------------------+
- Bảng vùng: | Vùng | Nội dung | Vị trí | Ghi chú |.
- Nếu XUAT_HTML là "Có": ghi đường dẫn mockup.

F5. P11a-gui/SCR-nn-slug.md (đặc tả màn hình, mỗi màn hình một file)
Nếu có MAU_DAC_TA_MAN_HINH thì theo mẫu đó, bổ sung các cột lõi dưới đây nếu mẫu thiếu. Mặc định gồm:
a) Khi có THONG_TIN_TAI_LIEU hoặc MAU_DAC_TA_MAN_HINH: thêm các hàng Ngày tạo, Người duyệt, Người kiểm tra, Người phụ trách vào bảng thông tin C5, giá trị theo THONG_TIN_TAI_LIEU; không lập bảng đầu trang riêng. Không có thì bỏ mục a).
b) Thông tin chung: SCR, UC, bước UC, tác nhân, boundary AC, DC, loại màn hình, màn hình đến từ và đi tới (theo F3).
c) Hình ảnh màn hình (F4).
d) Danh sách chức năng (bảng điều khiển): | STT | Điều khiển (Control) | Loại (nút, ô nhập, danh sách chọn, ô chọn, nút chọn, bảng, vùng hiển thị, liên kết) | Thao tác (Operation: Khởi tạo, Nhấn, Chọn, Nhập, Rời trường, Nhấn đúp, Quét (thiết bị đưa dữ liệu vào), Hết thời gian (sự kiện thời gian trên màn hình), Nhận kết quả (kết quả bất đồng bộ từ hệ thống)) | Chức năng (Function) | Nguồn (UC bước, trách nhiệm boundary, MSG) |
   - Định nghĩa: mỗi dòng là một cặp điều khiển và thao tác, cột Chức năng mô tả hệ thống làm gì khi thao tác xảy ra, kể cả màn hình tiếp theo hoặc thông điệp hiển thị.
   - Quy tắc: thao tác "Khởi tạo" mô tả nội dung hiển thị khi mở màn hình; mỗi nút có dòng "Nhấn"; chức năng nêu kết quả cả khi thành công và khi lỗi (tham chiếu MSG).
   - Ví dụ đúng (giao đồ ăn): | 4 | Nút "Đặt món" | Nút chính | Nhấn | Kiểm tra giỏ không rỗng và địa chỉ đã chọn; hợp lệ thì mở SCR-09 Xác nhận đơn; không hợp lệ thì hiển thị MSG-07 tại trường thiếu | UC-012 bước 5, 5a |.
   - Ví dụ sai: | 4 | Nút "Đặt món" | Nút | Nhấn | Đặt món | (sai: không nêu kết quả, không nêu lỗi, không nguồn).
e) Định nghĩa thuộc tính trường: | Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type: Chữ, Số, Ngày, Giờ, Tiền, Lựa chọn, Logic) | Thuộc tính trường (Field attribute: Nhập / Hiển thị / Chọn; bắt buộc; mặc định; căn lề; màu) | Ràng buộc dữ liệu (định dạng, miền giá trị, quy tắc) | Ghi chú (Remarks) | Nguồn (P04 dữ liệu vào ra STT, BR, GL) |
   - Mọi trường nhập và mọi trường hiển thị có dữ liệu nghiệp vụ đều có dòng.
   - Ràng buộc dữ liệu lấy từ cột "Điều kiện hợp lệ" của bảng dữ liệu vào ra P04 và BR. Trường do tác nhân nhập: độ dài tối đa và miền giá trị mà nguồn không nêu là giá trị nghiệp vụ, ghi Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN). Trường do hệ thống cấp hoặc tính (mã, định danh, số tiền tính từ BR): độ dài là quyết định thiết kế theo Conventions C1.7, ghi "Thiết kế: <lý do>"; P13 dùng lại giá trị này cho cột tương ứng.
   - Cột Số ký tự tối đa ghi "-" cho trường Lựa chọn, Logic và trường Hiển thị có độ dài theo giá trị; trường Ngày, Giờ, Tiền ghi độ dài của định dạng hiển thị (ví dụ dd/MM/yyyy là 10).
   - Ví dụ đúng (quản lý kho): | Số lượng nhập | 6 | Số | Nhập, bắt buộc, căn phải | Số nguyên 1-999999, không vượt số lượng còn lại của dòng đơn mua (BR-08) | Định dạng phân cách hàng nghìn | P04 UC-007 mục 5 Dữ liệu vào 1 STT 1, BR-08 |.
   - Ví dụ sai: | Số lượng | 10 | int | ... (sai: kiểu vật lý, không nguồn cho độ dài).
f) Kiểm tra dữ liệu nhập: | Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |, theo thứ tự chuẩn ở F1.
g) Đánh giá chuẩn (F7) của màn hình này.
h) Thông điệp mới: | MSG | Loại | Nội dung hiển thị | Nút và hành động | Nguồn |. Thông điệp cần cho màn hình mà danh mục ở ui-standards.md chưa có thì cấp MSG-nn ở mục này, nối tiếp số MSG lớn nhất trong ui-standards.md và mọi SCR đã có. Màn hình khác dùng lại thông điệp này trích "MSG-nn (SCR-mm)". Không có thì ghi "Không có".

F6. Mockup HTML (khi XUAT_HTML là "Có")
- Mỗi màn hình một file P11a-gui/mockups/SCR-nn-slug.html, tự đủ (HTML và CSS trong một file, không tải tài nguyên ngoài, không JavaScript bắt buộc).
- Dùng đúng quy định ở ui-standards.md (màu, cỡ chữ, vị trí nút, kích thước điều khiển); có nhãn cho mọi trường (thẻ label gắn với ô nhập); tương phản đạt WCAG AA; điều khiển dùng đúng phần tử ngữ nghĩa (button, input, select, table).
- Dữ liệu mẫu tuân quy tắc đúng nghiệp vụ ở A4. Ảnh minh hoạ dùng khối placeholder có văn bản thay thế.

F7. Đánh giá theo chuẩn
Bảng: | SCR | Tiêu chí | Kết quả (Đạt / Vi phạm đã sửa / Vi phạm còn mở / Không áp dụng) | Bằng chứng | Cách xử lý |
Bảng F7 ghi ở mục g của mỗi SCR-nn-slug.md (giai đoạn 2). Giai đoạn 1 đánh giá ui-standards.md theo từng tiêu chí, cột SCR ghi "Chuẩn hoá", đặt ở cuối ui-standards.md. Lần chạy giai đoạn 2 cuối cùng, hoặc chế độ Toàn bộ, lập bảng tổng hợp ở cuối screen-list.md từ mục g của các SCR.
Bảng của mỗi SCR chỉ ghi dòng Vi phạm đã sửa, Vi phạm còn mở và dòng Đạt có bằng chứng riêng của màn hình (khác quy định chung của ui-standards.md). Khi MUC_CHI_TIET là DAY_DU, thêm một dòng "Các tiêu chí còn lại: Đạt theo ui-standards.md STT ..." thay cho từng dòng.
Tiêu chí:
- Nielsen: 1 Hiển thị trạng thái hệ thống; 2 Khớp giữa hệ thống và thế giới thực; 3 Người dùng kiểm soát và tự do; 4 Nhất quán và theo chuẩn; 5 Ngăn lỗi; 6 Nhận biết thay vì nhớ lại; 7 Linh hoạt và hiệu quả; 8 Thẩm mỹ và tối giản; 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi; 10 Trợ giúp và tài liệu.
- Shneiderman (chỉ đánh giá ở bảng tổng hợp của screen-list.md và bảng của ui-standards.md, không ghi trong từng SCR): nhất quán; khả dụng cho mọi người dùng; phản hồi đầy đủ; hội thoại có điểm kết thúc rõ; ngăn lỗi; hoàn tác dễ dàng; người dùng làm chủ; giảm tải trí nhớ ngắn hạn.
- WCAG 2.2 AA (các tiêu chí thường gặp ở màn hình nghiệp vụ): 1.1.1 Nội dung không phải chữ; 1.3.1 Thông tin và quan hệ; 1.4.1 Không dùng màu làm tín hiệu duy nhất; 1.4.3 Tương phản chữ tối thiểu 4.5:1 (chữ lớn 3:1); 1.4.4 Phóng to chữ 200%; 1.4.10 Reflow (web); 1.4.11 Tương phản thành phần 3:1; 2.1.1 Bàn phím; 2.4.3 Thứ tự tiêu điểm; 2.4.6 Tiêu đề và nhãn; 2.4.7 Tiêu điểm nhìn thấy; 2.4.11 Tiêu điểm không bị che; 2.5.7 Thay thế thao tác kéo; 2.5.8 Vùng bấm tối thiểu 24 x 24 px; 3.2.3 Điều hướng nhất quán; 3.2.4 Định danh nhất quán; 3.2.6 Trợ giúp nhất quán; 3.3.1 Nhận biết lỗi; 3.3.2 Nhãn hoặc hướng dẫn; 3.3.3 Gợi ý sửa lỗi; 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính; 3.3.7 Không bắt nhập lại; 3.3.8 Xác thực dễ tiếp cận; 4.1.3 Thông điệp trạng thái.
- Nền tảng (Material Design chỉ cho màn hình Android, Apple HIG chỉ cho màn hình iOS; màn hình web không ghi hai dòng này): Material Design (vùng chạm tối thiểu 48 dp, mức nhấn mạnh nút, một hành động chính); Apple HIG (vùng chạm tối thiểu 44 pt, điều hướng quay lại theo nền tảng).
- Baymard (màn hình có form nhập, giỏ hàng, thanh toán): form một cột; nhãn đặt trên ô nhập, không dùng placeholder thay nhãn; đánh dấu rõ cả trường bắt buộc và tuỳ chọn; kiểm tra ngay khi rời trường, không báo lỗi khi đang gõ; giữ nguyên dữ liệu đã nhập khi báo lỗi; thông điệp lỗi đặt cạnh trường và nói cụ thể; chấp nhận nhiều định dạng nhập hợp lý (khoảng trắng trong số điện thoại, số thẻ); giảm số trường tới mức đặc tả yêu cầu; hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán.
Lưu ý: chuẩn chỉ quyết định cách trình bày. Nếu một heuristic gợi ý thêm chức năng (ví dụ hoàn tác, lưu nháp, thanh toán không cần tài khoản) mà đặc tả không có, ghi Q-nn hoặc đề xuất sửa P04, không tự thêm.

F8. Mục kiểm soát theo C5 trong mỗi file.

[Target]
1. Mỗi quy định chuẩn hoá có giá trị cụ thể, kiểm tra được, có căn cứ; đủ các nhóm Display, Screen, Control, Menu, Bàn phím, Messages, Error, Help, Khả năng tiếp cận, Xác nhận.
2. Mỗi boundary giao diện người dùng mà P10 mục F3 đặt ở layer giao diện có ít nhất một màn hình; boundary khác (ánh xạ sang subsystem, loại Kênh thông báo) có dòng ở bảng "Boundary không có màn hình" kèm lý do; mỗi màn hình có boundary nguồn hoặc là màn hình điều hướng.
3. Không có trường, nút, chức năng nào không truy được về đặc tả, bảng dữ liệu vào ra, BR hoặc trách nhiệm boundary.
4. Mọi thông điệp trong đặc tả có trong danh mục MSG của ui-standards.md hoặc mục h) của một SCR, và được tham chiếu ở chức năng của điều khiển.
5. Mọi dịch chuyển dùng đúng một trong bốn mẫu, đúng ký hiệu; không vẽ cạnh đóng pop-up; mọi màn hình đến được từ Start và có lối ra.
6. Mỗi màn hình trong phạm vi có hình ảnh, bảng điều khiển, bảng thuộc tính trường, bảng kiểm tra dữ liệu nhập.
7. Ràng buộc dữ liệu của trường khớp P04 và BR; không có độ dài, miền giá trị của trường nhập tự đặt mà không có mã Q hoặc ASM; độ dài của trường do hệ thống cấp có ghi "Thiết kế: <lý do>".
8. Dữ liệu mẫu đúng nghiệp vụ: định dạng đúng, tổng hợp khớp, đơn vị nhất quán.
9. Giai đoạn 1: mọi tiêu chí F7 được đánh giá trên ui-standards.md. Giai đoạn 2: mọi màn hình trong phạm vi được đánh giá theo F7; không còn vi phạm WCAG AA chưa có cách xử lý.
10. Hình ảnh, sơ đồ dịch chuyển, đặc tả, danh sách màn hình nhất quán tên, mã và dịch chuyển.
11. Bảng mô hình và file .drawio khớp nhau, đạt C7.3; mockup HTML (nếu có) theo đúng chuẩn.
12. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này | Ví dụ: "Không dùng phím tắt; mọi màn hình có nút Quay lại."; "Giao diện hỗ trợ tiếng Việt và tiếng Anh."; "Mockup mô phỏng cửa sổ ứng dụng có thanh tiêu đề và nút đóng."}}
````

## 5. Ghi chú cho người dùng

- Nếu đặc tả P04 của use case không có bước hệ thống báo kết quả cho tác nhân người sau khi thành công (hoặc bảng dữ liệu ra ghi "Không có"), màn hình kết quả sẽ không có căn cứ và nhiều vi phạm Nielsen #1 (hiển thị trạng thái hệ thống) chỉ ghi được thành Q. Chạy lại P04 cho use case đó trước khi chạy P11a giai đoạn 2.
- Chạy giai đoạn 1 và rà soát kỹ ui-standards.md trước khi chạy giai đoạn 2; sửa chuẩn sau khi đã có nhiều đặc tả màn hình sẽ phải chạy lại toàn bộ giai đoạn 2.
- Khi AI thêm nút hoặc trường "cho tiện" (ví dụ tìm kiếm nâng cao, đánh giá sao), đó là vi phạm nguồn sự thật. Nếu chức năng đó cần thật, bổ sung vào P04 trước.
- Mockup HTML là hình ảnh tham khảo, không phải mã nguồn giao diện. Nếu cần ảnh chụp để đưa vào tài liệu, mở file HTML trên trình duyệt ở kích thước THIET_BI_HIEN_THI rồi chụp.
- Kiểm tra tương phản màu bằng công cụ đo tỉ lệ tương phản bất kỳ; AI có thể tính sai với màu gần ngưỡng.
- Dùng độc lập: cần tối thiểu đặc tả use case có bảng dữ liệu vào ra và danh sách lớp boundary (hoặc danh sách các tương tác giữa tác nhân và hệ thống). Không có P10 thì bỏ cột DC.

## 6. Căn cứ

- Nielsen J., 10 Usability Heuristics for User Interface Design, Nielsen Norman Group (1994, cập nhật 2020).
- Shneiderman B. và cộng sự, Designing the User Interface, 6th ed. (2016): 8 quy tắc vàng.
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2 (2023), mức AA.
- Google, Material Design 3 guidelines: mức nhấn mạnh nút, kích thước vùng chạm.
- Apple, Human Interface Guidelines: kích thước vùng chạm, điều hướng.
- Baymard Institute, nghiên cứu khả dụng về form, giỏ hàng và thanh toán (checkout usability).
- Galitz W., The Essential Guide to User Interface Design, 3rd ed. (2007): thiết kế màn hình, đặc tả màn hình và thuộc tính trường, thông điệp, trợ giúp.
- Ambler S., The Elements of UML 2.0 Style (2005) và OMG UML 2.5.1: ký pháp sơ đồ.
