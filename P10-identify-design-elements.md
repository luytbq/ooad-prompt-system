# P10 - Xác định phần tử thiết kế (Identify Design Elements)

## 1. Mục đích

Bước này chuyển mô hình phân tích thành các phần tử của mô hình thiết kế: mỗi lớp phân tích được ánh xạ thành một lớp thiết kế, được tách thành nhiều lớp, trở thành package, hoặc trở thành subsystem có interface. Các lớp thiết kế được nhóm vào package theo tiêu chí gắn kết chức năng, đặt trong các layer của P09, với quy tắc visibility và coupling giữa package. Kết quả là khung phần tử thiết kế mà P11a, P11b chi tiết hoá giao diện và P12 thiết kế chi tiết từng lớp.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md, 00-Conventions.md | Có | Luật chung, mã DC, PKG, SS, IF; NEN_TANG, CONG_NGHE đã cập nhật sau P09 |
| Đầu vào | P08-analysis-model.md | Có | Lớp phân tích hợp nhất và quan hệ |
| Đầu vào | P09-architecture.md | Có | Layer, package cấp cao, quy tắc phụ thuộc, bảng ánh xạ stereotype sang layer |
| Đầu vào | P01-actors.md | Có | Tác nhân gắn với boundary (tiêu chí nhóm package) |
| Đầu vào | P02-usecases.md, P03-usecase-model.md | Có | Nhóm chức năng; use case tuỳ chọn (extend) để tách optional và mandatory |
| Đầu vào | P06-supplementary-spec.md | Có | NFR về khả năng thay đổi, bảo mật, thay thế thành phần |
| Đầu vào | P07-uc-analysis/*.md | Không | Tra sequence khi cần đánh giá mức tương tác giữa hai lớp |
| Đầu ra | P10-design-elements.md | Có | Ánh xạ, package, subsystem, interface |
| Đầu ra | diagrams/P10-package-design.drawio | Có | Package diagram chi tiết với phụ thuộc |
| Đầu ra | diagrams/P10-subsystem-context.drawio | Khi có subsystem | Subsystem, interface và lớp dùng chúng |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md và các file đầu vào. Mỗi file chỉ cần phần sau (khi chạy bằng agent, chỉ đọc các mục này, tìm theo tiêu đề):

| Artifact | Phần cần dùng |
|---|---|
| P08-analysis-model.md | F3 (bảng lớp hợp nhất), F4 (bảng quan hệ), Câu hỏi mở, Giả định |
| P09-architecture.md | F4, F5, F6, F7, Câu hỏi mở, Giả định |
| P01-actors.md, P02-usecases.md | Bảng tác nhân; Mục 4 (UC, nhóm chức năng) |
| P06-supplementary-spec.md | NFR về khả năng thay thế, bảo mật, giao tiếp ngoài |
| P03-usecase-model.md, P04-uc-specs/ | Quan hệ extend và use case tuỳ chọn (A3, lớp tuỳ chọn) |

- Chạy một lần cho toàn hệ thống, sau P09 và sau khi đã thay hai dòng NEN_TANG, CONG_NGHE của project-profile.md bằng khối "Cập nhật hồ sơ dự án" của P09 (khi hồ sơ từng ghi "Chưa chốt"). Chạy lại khi P08 hoặc P09 thay đổi.

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| TIEU_CHI_NHOM_PACKAGE | Tuỳ chọn | Tiêu chí nhóm package ưu tiên của dự án (đơn vị cấu hình, phân công nhóm...) |
| KHA_NANG_THAY_DOI_GIAO_DIEN | Tuỳ chọn | Mức độ giao diện người dùng và giao diện hệ thống có thể thay đổi, để quyết định tách hay gộp boundary |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được hồ sơ dự án, 00-Conventions.md và các artifact đã chốt: P01-actors.md, P02-usecases.md, P03-usecase-model.md, P06-supplementary-spec.md, P08-analysis-model.md, P09-architecture.md, (nếu có) P07-uc-analysis/*.md. Tuân thủ 00-Conventions.md, đặc biệt C1, C3, C5, C7.
Phạm vi: toàn hệ thống.

Tiêu chí nhóm package ưu tiên:
{{PH:TIEU_CHI_NHOM_PACKAGE | Hướng dẫn: [TUỲ CHỌN] tiêu chí tổ chức muốn áp dụng thêm cho việc nhóm package; ghi "Không có" thì dùng tiêu chí mặc định ở A3 | Ví dụ: "Mỗi nhóm phát triển sở hữu một package nghiệp vụ: nhóm A đặt lịch, nhóm B hồ sơ bệnh nhân." (phòng khám); "Phân hệ kế toán là đơn vị cấu hình giao riêng cho khách hàng mua thêm." (quản lý kho)}}

Khả năng thay đổi của giao diện:
{{PH:KHA_NANG_THAY_DOI_GIAO_DIEN | Hướng dẫn: [TUỲ CHỌN] nêu giao diện nào dễ thay đổi đáng kể (đổi nền tảng, đổi nhà cung cấp) và giao diện nào ổn định; ghi "Không có" thì suy từ NFR và hồ sơ dự án, không đủ căn cứ thì coi là dễ thay đổi | Ví dụ: "Sẽ có thêm ứng dụng mobile cho khách hàng; giao diện quản trị ổn định." (giao đồ ăn); "Có thể đổi nhà cung cấp cổng SMS." (phòng khám)}}

[Role]
Bạn là kiến trúc sư phần mềm và nhà thiết kế hướng đối tượng, thành thạo hoạt động Identify Design Elements: ánh xạ lớp phân tích sang lớp thiết kế, package, subsystem và interface; tiêu chí nhóm package theo gắn kết chức năng; nguyên tắc package của Martin (REP, CCP, CRP, ADP, SDP); visibility và coupling giữa package; ký pháp UML 2.5.1 cho package, interface, realization.

[Action]
A0. Kiểm tra đầu vào.
- Kiểm tra placeholder theo Conventions C6.
- Đối chiếu mẫu kiến trúc và mẫu cho phía giao diện ở P09 mục F3 với NEN_TANG, CONG_NGHE hiện tại của hồ sơ dự án. Hồ sơ vẫn ghi "Chưa chốt": dùng công nghệ ở P09 mục F11 và ghi vào Vấn đề còn mở "Hồ sơ chưa cập nhật theo P09". Mẫu lệch công nghệ (ví dụ P09 chọn MVC passive cho web render phía máy chủ, hồ sơ chốt SPA): ghi Đề xuất sửa P09 và Q-nn, tiếp tục theo công nghệ trong hồ sơ.

A1. Xác định subsystem ứng viên.
- Xét mọi lớp phân tích hoạt động trong P08. Một lớp (hoặc nhóm lớp) là ứng viên subsystem khi thoả ít nhất một tiêu chí: là boundary giao diện hệ thống ngoài; là boundary giao diện thiết bị; cung cấp dịch vụ phức tạp hoặc tiện ích dùng ở nhiều use case và che giấu được bên trong; có khả năng bị thay thế bằng biến thể khác (đổi nhà cung cấp, đổi thiết bị) theo NFR hoặc KHA_NANG_THAY_DOI_GIAO_DIEN; cần giới hạn truy cập vì lý do bảo mật; đại diện cho sản phẩm có sẵn được dùng lại (thư viện giao tiếp, hỗ trợ truy cập dữ liệu, tiện ích chung).
- Package tích hợp, hạ tầng của P09 không có lớp phân tích nguồn (máy in nối qua phần mềm trung gian, bộ định thời, đồng bộ với máy trạm) cũng được xét: F1 ghi cột Lớp phân tích là "- (ACT-nn hoặc PKG-nn của P09)", F2 ghi AC nguồn "Cơ chế: <mục P09>". Phần hiện thực interface kho dữ liệu (Persistence) không thành subsystem: ghi ở bảng phần tử thiết kế mới do cơ chế kiến trúc (F3); operation của interface kho dữ liệu do P12 thiết kế.
- Boundary loại Kênh thông báo (email, SMS, thông báo đẩy) ánh xạ theo dòng tương ứng ở P09 mục F5; thường thành subsystem gửi thông báo khi kênh đi qua dịch vụ ngoài, không thành lớp giao diện người dùng.
- Lớp "siêu nhân" (một boundary có nhiều trách nhiệm phức tạp) là dấu hiệu nên thành subsystem: trách nhiệm của nó trở thành operation của interface, phần hiện thực chia cho các lớp bên trong.
- Mỗi subsystem: đặt tên theo năng lực cung cấp; xác định interface nó hiện thực (tên bắt đầu bằng chữ I, phản ánh vai trò); liệt kê trách nhiệm (lấy từ trách nhiệm của lớp phân tích nguồn); liệt kê phần tử được che giấu. Chi tiết operation để P11b làm.

A2. Ánh xạ từng lớp phân tích.
- Mặc định ánh xạ 1-1 sang một lớp thiết kế khi lớp đơn giản và đại diện một trừu tượng logic duy nhất.
- Tách thành nhiều lớp khi: lớp chứa hai nhóm trách nhiệm ít liên quan; theo bảng ánh xạ stereotype của P09, một boundary người dùng trở thành nhiều vai trò (ví dụ View và Presenter trong MVP, View và Controller trong MVC); entity cần tách phần hành vi nghiệp vụ và phần lưu trữ theo layer của P09.
- Thành package khi lớp phân tích thực chất là một nhóm khái niệm có nhiều lớp thiết kế.
- Thành subsystem khi đã được chọn ở A1.
- Kết hợp các cách trên khi cần. Mọi lựa chọn khác 1-1 phải ghi lý do.
- Đặt tên lớp thiết kế theo NGON_NGU_TEN_PHAN_TU, mã DC-<Tên>. Lớp thiết kế giữ tên lớp phân tích khi ánh xạ 1-1, trừ khi tên đụng thuật ngữ kỹ thuật của mẫu kiến trúc (ví dụ lớp control phân tích "PlaceOrderController" khi MVC cũng có "Controller"); khi đổi, ghi lý do.
- Không thiết kế thuộc tính, phương thức chi tiết (việc của P12). Chỉ nêu trách nhiệm kế thừa từ lớp phân tích.

A3. Nhóm lớp thiết kế vào package.
- Mỗi package nằm trong một layer của P09 (con của PKG layer hoặc PKG cấp cao ở P09). Cấp mã PKG tiếp theo số lớn nhất của P09.
- Hai lớp gắn kết chức năng (nên cùng package) khi có ít nhất một dấu hiệu: thay đổi hành vi hoặc cấu trúc của lớp này buộc thay đổi lớp kia; bỏ lớp này ảnh hưởng lớp kia; hai đối tượng trao đổi nhiều message hoặc giao tiếp phức tạp (đối chiếu sequence P07); boundary có chức năng trình bày một entity cụ thể; hai lớp cùng tương tác với, hoặc cùng chịu ảnh hưởng khi thay đổi, một tác nhân; hai lớp có quan hệ với nhau; lớp này tạo đối tượng của lớp kia.
- Hai lớp không được cùng package khi: chúng là boundary giao diện người dùng phục vụ hai tác nhân khác nhau (control, entity dùng chung bởi nhiều tác nhân không bị tách vì lý do này; quy tắc tác nhân chỉ áp dụng cho phần tử ở layer giao diện như View, Presenter, Store, ViewModel; phần tiếp nhận yêu cầu ở layer Application nhóm theo nhóm chức năng); một lớp là tuỳ chọn (thuộc tính năng tuỳ chọn, ví dụ use case extend được bán hoặc bật riêng) và lớp kia bắt buộc.
- Package của P09 vi phạm quy tắc tác nhân ở trên thì giữ mã PKG đó làm package cha không chứa phần tử, cấp package con cho từng tác nhân và ghi Đề xuất sửa P09.
- Boundary: nếu giao diện (người dùng hoặc hệ thống) có khả năng thay đổi đáng kể, đặt boundary vào package riêng, tách khỏi lớp nghiệp vụ; nếu giao diện ổn định, có thể đặt boundary cùng package với các lớp gắn kết chức năng với nó. Dùng KHA_NANG_THAY_DOI_GIAO_DIEN; không có thông tin thì coi là dễ thay đổi và tách.
- Kiểu giá trị (tiền, định danh, mã tham chiếu) được interface ở layer dưới dùng trong chữ ký: đặt ở package cùng layer với interface hoặc thấp hơn (ví dụ một package kiểu dữ liệu dùng chung ở layer thấp nhất), để chữ ký interface không kéo layer dưới phụ thuộc layer trên.
- Áp dụng thêm TIEU_CHI_NHOM_PACKAGE nếu có (đơn vị cấu hình, phân công nhóm phát triển, loại người dùng, sản phẩm và dịch vụ có sẵn).
- Khi các tiêu chí mâu thuẫn, ưu tiên: quy tắc layer của P09 --> quy tắc "không được cùng package" --> gắn kết chức năng --> tiêu chí tổ chức. Ghi lựa chọn.

A4. Xác định visibility của phần tử trong package.
- Chỉ lớp public của package được tham chiếu từ ngoài package. Mặc định: lớp được lớp ở package khác dùng là public; lớp chỉ dùng nội bộ là private (package-private).
- Với subsystem: chỉ interface là public; mọi lớp bên trong subsystem không public.

A5. Xác định phụ thuộc giữa package và kiểm tra coupling.
- Suy phụ thuộc package từ quan hệ giữa các lớp thiết kế (kế thừa từ quan hệ ở P08 và từ luồng message ở P07).
- Kiểm tra: không có hai package phụ thuộc lẫn nhau (cross-coupled) và không có vòng phụ thuộc; package ở layer dưới không phụ thuộc package ở layer trên; phụ thuộc không nhảy layer (theo kiểu layered của P09); phụ thuộc tới subsystem đi qua interface.
- Vi phạm thì sửa bằng: chuyển lớp sang package khác; tách package; đảo phụ thuộc theo P09 A5 (layer dưới định nghĩa interface cho việc gọi ngược, layer trên hiện thực nó, realization đi xuống); chuyển interface xuống package cùng layer với lớp hiện thực khi realization đang đi lên; tạo package chung cho phần dùng chung.

A6. Vẽ sơ đồ, tự kiểm tra, xuất kết quả.

[Format]
Xuất file P10-design-elements.md theo khung C5, tiêu đề "# P10 - Phần tử thiết kế - <Tên hệ thống>". Nội dung chính:

F1. Subsystem ứng viên và quyết định
Bảng: | Lớp phân tích (AC) | Tiêu chí thoả (Hệ thống ngoài / Thiết bị / Dịch vụ phức tạp dùng chung / Có thể thay thế / Bảo mật / Sản phẩm có sẵn) | Quyết định (Subsystem / Không) | Lý do |
- Mức hợp lý: mọi boundary giao diện hệ thống ngoài và thiết bị đều thành subsystem, trừ khi có lý do ghi rõ (ví dụ chỉ gửi một thông điệp một chiều rất đơn giản và NFR không yêu cầu thay thế được). Lớp khác chỉ thành subsystem khi có tiêu chí rõ.
- Lỗi thường gặp: biến mọi control thành subsystem (quá lớn, mất lợi ích che giấu); boundary tới cổng thanh toán giữ là lớp thường khiến control phụ thuộc trực tiếp vào chi tiết giao thức (quá nhỏ).
- Ví dụ đúng (giao đồ ăn): AC-B-PaymentGateway --> Subsystem, tiêu chí Hệ thống ngoài, Có thể thay thế (đổi cổng thanh toán). Ví dụ đúng (quản lý kho): AC-B-BarcodeScanner --> Subsystem, tiêu chí Thiết bị.
- Package của P09 chỉ phục vụ use case chưa có P07 (không có lớp hoạt động nào trong P08) thì giữ chỗ ở F4, chưa tạo subsystem, ghi ở Vấn đề còn mở.
- Ví dụ sai: AC-C-BookAppointmentController --> Subsystem vì "có nhiều bước" (sai: độ dài điều phối không phải tiêu chí subsystem).

F2. Bảng subsystem (bảng lõi, P11b đọc bảng này)
| SS | Tên | Interface (IF) | Trách nhiệm | Che giấu phần tử nào | AC nguồn | ACT liên quan | PKG chứa |
- SS: mã SS-nn; IF: mã IF-nn kèm tên, ví dụ "IF-01 IPaymentGateway". Một subsystem có thể hiện thực nhiều interface khi phục vụ các vai trò khác nhau.
- Ngay dưới F2 lập bảng Interface gọi ngược: | IF | Tên | Định nghĩa tại PKG | Subsystem gọi | Lớp hiện thực (DC, PKG) | Trách nhiệm | Nguồn (P09 A5, UC) |. Mỗi chỗ P09 ghi cơ chế gọi ngược và mỗi boundary thiết bị hoặc hệ thống ngoài chỉ đẩy sự kiện vào hệ thống có ít nhất một dòng. Mã IF dùng chung dãy với F2. P11b, P12 đọc cả hai bảng.
- Trách nhiệm: liệt kê theo trách nhiệm của lớp phân tích nguồn, dạng "// tênTráchNhiệm".
- Che giấu phần tử nào: mô tả các lớp bên trong dự kiến (giao thức, chuyển đổi dữ liệu, quản lý kết nối), chưa cần tên cuối cùng.
- Tên interface: phản ánh vai trò trong hệ thống, không phản ánh nhà cung cấp cụ thể (IPaymentGateway, không phải IAcmePayApi), trừ khi YEU_CAU_BO_SUNG yêu cầu.

F3. Bảng ánh xạ lớp phân tích sang phần tử thiết kế (bảng lõi, P12 đọc bảng này)
| AC | Kết quả (Lớp thiết kế DC / Subsystem SS / Package / Tách thành nhiều lớp) | Phần tử thiết kế | PKG | Lý do |
- Mọi lớp hoạt động trong P08 có đúng một dòng. Lớp "Gộp vào" không có dòng.
- Phần tử thiết kế: mã và tên, nhiều phần tử cách nhau bằng thẻ <br>, ví dụ "DC-BookingView<br>DC-BookingPresenter".
- Lý do: bắt buộc khi kết quả khác 1-1; với 1-1 ghi "Lớp đơn giản, một trừu tượng".
Mức hợp lý: phần lớn lớp ánh xạ 1-1; tỷ lệ tách cao bất thường (hơn một nửa) cần kiểm tra lại mô hình phân tích hoặc bảng ánh xạ của P09.
Lỗi thường gặp: thêm lớp thiết kế không truy được về lớp phân tích hay cơ chế kiến trúc (lớp mồ côi); tách entity thành DTO, DAO, Entity, Mapper cho mọi lớp dù P09 không yêu cầu (quá lớn); giữ nguyên boundary người dùng thành một lớp trong khi P09 chọn MVP (bỏ sót vai trò).
Ví dụ đúng (thư viện, P09 chọn layered với MVC passive): AC-B-BorrowBookForm --> Tách thành nhiều lớp: DC-BorrowBookView, DC-BorrowBookRequestHandler, PKG-11 LoanUI, lý do: bảng ánh xạ P09 tách View và phần tiếp nhận yêu cầu. AC-E-Loan --> DC-Loan, PKG-12 Loan, lý do: lớp đơn giản.
Ngoài ra, liệt kê bảng phần tử thiết kế mới do cơ chế kiến trúc (không từ lớp phân tích): | DC hoặc SS | Tên | PKG | Cơ chế (Persistence, Logging, Bảo mật...) | Nguồn (P09 mục, NFR) |.

F4. Bảng package (tiếp nối bảng của P09)
| PKG | Tên | Layer (PKG) | Trách nhiệm | Phần tử chứa (DC, SS, IF) | Tiêu chí nhóm | Phụ thuộc vào (PKG) |
- Tiêu chí nhóm: ghi dấu hiệu gắn kết chức năng hoặc tiêu chí tổ chức đã dùng, ví dụ "cùng tác nhân Lễ tân; View trình bày Appointment".
- Mức hợp lý: package có 2-15 phần tử. Package 1 phần tử chỉ chấp nhận khi là package interface, package subsystem hoặc có lý do thay đổi riêng. Trên 15 phần tử thì kiểm tra có thể tách theo tác nhân hoặc nhóm chức năng.
- Lỗi thường gặp: một package "Common" chứa mọi thứ dùng chung (cohesion thấp, trở thành điểm phụ thuộc của mọi package); đặt boundary của Khách hàng và boundary của Quản trị viên cùng package (vi phạm tiêu chí tác nhân); đặt lớp của tính năng tuỳ chọn cùng package với lớp bắt buộc.

F5. Visibility
Bảng: | PKG | Phần tử | Visibility (public / package-private) | Được dùng bởi (PKG) |
Mọi phần tử được package khác dùng phải public; mọi lớp bên trong subsystem không public.

F6. Kiểm tra coupling giữa package
Bảng: | Phụ thuộc (PKG --> PKG) | Suy ra từ (quan hệ lớp, message) | Cross-coupled | Lower --> Upper | Nhảy layer | Vòng | Kết luận và cách sửa |
Mỗi ô kiểm tra ghi Không hoặc Có. Cột Nhảy layer ghi "Không áp dụng" khi P09 chọn layered nới lỏng; chỉ ghi Có hoặc Không khi P09 chọn nghiêm ngặt. Mọi dòng có "Có" phải có cách sửa đã áp dụng hoặc ghi vào "Vấn đề còn mở".

F7. Package diagram thiết kế
File diagrams/P10-package-design.drawio.
a) Bảng Node: | ID (PKG, SS, IF, DC) | Loại (Layer / Package / Subsystem / Interface / Class; Class chỉ vẽ cho lớp hiện thực interface gọi ngược) | Nhãn | Stereotype («layer», «subsystem», «interface») | Thuộc về | Ghi chú (visibility) |
b) Bảng Edge: | ID | Nguồn | Đích | Loại quan hệ (Dependency / Realization) | Nhãn | Ghi chú |
Quy tắc ngữ nghĩa UML: package là hình thư mục, phụ thuộc là mũi tên nét đứt đầu mở; subsystem vẽ là component có stereotype «subsystem» (style: shape=component;whiteSpace=wrap;html=1; hoặc hình chữ nhật có nhãn «subsystem»); interface vẽ là lớp có stereotype «interface» (dạng canonical) hoặc vòng tròn nhỏ (dạng elided: ellipse;html=1; kích thước 20 x 20); subsystem nối tới interface nó hiện thực bằng realization (nét đứt, tam giác rỗng); package dùng subsystem thì phụ thuộc vào interface, không vào subsystem.
Bố cục: layer xếp chồng từ trên xuống như P09; mũi tên phụ thuộc và realization đều đi xuống hoặc ngang, không đi lên (P09 A5); interface đặt giữa package dùng nó và subsystem hiện thực nó, ở layer không cao hơn subsystem; theo C7.3.

F8. Subsystem context diagram (khi có subsystem)
File diagrams/P10-subsystem-context.drawio, mỗi subsystem một trang: interface (canonical, chưa cần operation chi tiết, có thể ghi trách nhiệm dạng "// ..."), subsystem hiện thực nó, các lớp thiết kế (thường là control) phụ thuộc vào interface. Bảng Node và Edge như F7.

F9. Mục kiểm soát theo C5.

[Target]
1. Mọi lớp phân tích hoạt động trong P08 có đúng một dòng ánh xạ; mọi phần tử thiết kế truy được về lớp phân tích hoặc cơ chế kiến trúc.
2. Mọi ánh xạ khác 1-1 có lý do.
3. Mọi boundary giao diện hệ thống ngoài và thiết bị là subsystem có interface, hoặc có lý do ghi rõ.
4. Mỗi subsystem có ít nhất một interface nó hiện thực; subsystem thiết bị chỉ đẩy sự kiện vào thì interface hiện thực gồm việc bật, tắt và đăng ký bộ nhận, còn sự kiện đi qua interface gọi ngược (bảng dưới F2). Tên interface bắt đầu bằng I và phản ánh vai trò.
5. Mỗi package thuộc đúng một layer của P09; không có hai boundary giao diện người dùng của hai tác nhân khác nhau trong cùng package; không trộn lớp tuỳ chọn với lớp bắt buộc.
6. Không có package cross-coupled, không vòng phụ thuộc, không phụ thuộc hoặc realization từ layer dưới lên trên, không nhảy layer (khi layered nghiêm ngặt).
7. Mọi phụ thuộc tới subsystem đi qua interface; không lớp bên trong subsystem nào public.
8. Không thiết kế thuộc tính, phương thức chi tiết ở bước này.
9. Bảng mô hình và file .drawio khớp nhau, đạt C7.3.
10. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này | Ví dụ: "Mỗi package nghiệp vụ tương ứng một nhóm chức năng trong P02."; "Interface của subsystem đặt chung trong một package ExternalSystemInterfaces ở layer Services."}}
````

## 5. Ghi chú cho người dùng

- Nếu bảng ánh xạ có quá nhiều dòng "Tách thành nhiều lớp", kiểm tra bảng ánh xạ stereotype ở P09 mục F5; nhiều khi nguyên nhân là mẫu kiến trúc chọn quá nặng cho quy mô dự án.
- Nếu kiểm tra coupling liên tục báo vòng phụ thuộc giữa package nghiệp vụ, thường do hai nhóm chức năng dùng chung entity; tách entity dùng chung ra package riêng ở layer phù hợp.
- P11b dựa trên bảng subsystem ở đây. Nếu một hệ thống ngoài không được chọn làm subsystem, P11b sẽ không thiết kế interface cho nó.
- Dùng độc lập: cần bảng lớp phân tích có stereotype và quan hệ, và một mô tả layer (có thể tự viết ngắn thay cho P09).

## 6. Căn cứ

- Kruchten P., The Rational Unified Process: An Introduction, 3rd ed. (2003): hoạt động Identify Design Elements, ánh xạ lớp phân tích sang phần tử thiết kế, subsystem và interface.
- Jacobson I., Booch G., Rumbaugh J., The Unified Software Development Process (1999): subsystem thiết kế, interface, lớp thiết kế truy vết về lớp phân tích.
- Martin R. C., Agile Software Development: Principles, Patterns, and Practices (2002): nguyên tắc gắn kết package (REP, CCP, CRP) và coupling package (ADP, SDP, SAP).
- Larman C., Applying UML and Patterns, 3rd ed. (2004): tổ chức package theo layer, hướng phụ thuộc.
- OMG, Unified Modeling Language 2.5.1 (2017): package, visibility, component, interface, realization.
- Ambler S., The Elements of UML 2.0 Style (2005): quy ước đặt tên interface, bố cục package diagram.
