# P07 - Phân tích use case (Use-Case Analysis)

## 1. Mục đích

Bước này hiện thực hoá (realize) một use case bằng các lớp phân tích: tìm lớp boundary, control, entity từ luồng sự kiện, phân bổ từng bước của use case cho các lớp đó, mô hình hoá tương tác bằng sequence diagram và communication diagram, rồi rút ra VOPC (View Of Participating Classes, sơ đồ lớp phân tích của use case). Kết quả là cầu nối giữa mô hình yêu cầu (P02-P06) và mô hình thiết kế: P08 hợp nhất lớp phân tích của mọi use case, P10 ánh xạ chúng sang phần tử thiết kế, P12 biến trách nhiệm thành phương thức. Bước này chạy lặp, mỗi lần một use case.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md | Có | Chế độ giả định, ngôn ngữ, mức chi tiết |
| Đầu vào | 00-Conventions.md | Có | Luật chung, mã định danh, quy ước sơ đồ |
| Đầu vào | P04-uc-specs/UC-nnn-slug.md của use case đang phân tích | Có | Luồng sự kiện, dữ liệu vào ra, quy tắc nghiệp vụ tham chiếu |
| Đầu vào | P01-actors.md | Có | Phân loại tác nhân (người, hệ thống ngoài, thiết bị, thời gian) để tìm boundary |
| Đầu vào | P03-usecase-model.md | Có | Quan hệ include, extend, generalization của use case |
| Đầu vào | P05-glossary.md | Nên có | Tên khái niệm chuẩn để đặt tên entity và lọc từ đồng nghĩa |
| Đầu vào | P06-supplementary-spec.md | Nên có | BR và NFR áp dụng cho use case |
| Đầu vào | P04-uc-specs của use case được include hoặc extend | Khi có quan hệ | Biết phần hành vi nào thuộc use case khác |
| Đầu vào | P07-uc-analysis/*.md của các use case đã phân tích trước | Khi đã có | Tái dùng mã AC và tên lớp cho cùng khái niệm |
| Đầu vào | P02-usecases.md | Nên có | Mục tiêu và tác nhân của use case để đối chiếu; tìm use case do tác nhân thời gian kích hoạt trên đối tượng mà use case này tạo hoặc thay đổi (A2) |
| Đầu ra | P07-uc-analysis/UC-nnn-slug-analysis.md | Có | Artifact chính của bước |
| Đầu ra | diagrams/P07-sequence-UC-nnn.drawio | Có | Sequence diagram phân tích (mỗi luồng cần vẽ một trang) |
| Đầu ra | diagrams/P07-communication-UC-nnn.drawio | Có | Communication diagram |
| Đầu ra | diagrams/P07-class-UC-nnn.drawio | Có | VOPC |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, các file đầu vào ở bảng trên, và mọi file phân tích P07 đã có (để tái dùng mã AC).
- Chạy lặp: mỗi lần một use case. Thứ tự khuyến nghị: use case được include trước use case gọi nó; use case gốc trước use case extend nó; use case có nhiều entity cốt lõi trước. Thứ tự này giúp lớp dùng chung được đặt mã một lần và tái dùng.
- Sau khi mọi use case trong phạm vi đã chạy xong bước này, chuyển sang P08.
- Chưa có P05 hoặc P06 vẫn chạy được. Hệ quả: tên entity lấy theo thuật ngữ trong P04 và tài liệu nguồn nên có thể phải đổi khi P05 xong; cột GL ghi "-"; khái niệm chưa rõ nghĩa hoặc có thể đồng nghĩa với khái niệm khác thành Q-nn. Chạy lại P07 sau P05, P06 nếu tên hoặc BR thay đổi.

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| UC_ID | Có | Mã và tên use case cần phân tích trong lần chạy này |
| LUONG_CAN_VE | Tuỳ chọn | Giới hạn các luồng thay thế cần vẽ sequence riêng; mặc định vẽ mọi luồng |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được hồ sơ dự án (project-profile.md), bộ quy ước chung (00-Conventions.md) và các artifact đã chốt của các bước trước. Đọc toàn bộ trước khi làm. Tuân thủ mọi quy tắc trong 00-Conventions.md, đặc biệt C1 (nguồn sự thật, chế độ giả định, không sửa artifact trước), C3 (mã định danh), C5 (khung artifact), C7 (sơ đồ).

Use case cần phân tích trong lần chạy này:
{{PH:UC_ID | Hướng dẫn: ghi đúng mã và tên tiếng Việt của use case như trong P02-usecases.md; mỗi lần chạy chỉ một use case | Ví dụ: "UC-004 Hủy lịch hẹn" (phòng khám); "UC-012 Đặt món" (giao đồ ăn); "UC-007 Nhập kho theo phiếu" (quản lý kho)}}

Luồng cần vẽ sequence diagram riêng:
{{PH:LUONG_CAN_VE | Hướng dẫn: [TUỲ CHỌN] liệt kê mã luồng thay thế hoặc ngoại lệ cần vẽ; ghi "Không có" thì vẽ mọi luồng theo quy tắc ở mục A6 | Ví dụ: "Luồng chính, 3a, 5a" (khách sạn); "Chỉ luồng chính và các luồng ngoại lệ về thanh toán" (giao đồ ăn)}}

Đầu vào cần đọc:
- Đặc tả use case đang phân tích trong P04-uc-specs/ (bảng thông tin, luồng chính, luồng thay thế và ngoại lệ, dữ liệu vào ra, BR tham chiếu, activity diagram).
- P01-actors.md để biết loại của từng tác nhân tham gia.
- P03-usecase-model.md để biết use case này include, được include, extend hoặc được extend bởi use case nào.
- P05-glossary.md để lấy tên khái niệm chuẩn.
- P06-supplementary-spec.md để lấy BR, NFR áp dụng cho use case.
- Nếu chưa có P05 hoặc P06: lấy tên khái niệm từ đặc tả P04 và câu trong tài liệu nguồn, cột GL ghi "-"; BR lấy từ sổ P04-uc-specs/_BR-register.md, NFR lấy từ mục Yêu cầu đặc biệt của P04. Khái niệm chưa rõ nghĩa (không biết hai từ có cùng chỉ một thứ hay không) ghi Q-nn. Ghi "Chạy khi chưa có P05/P06" vào Vấn đề còn mở.
- Mọi file P07-uc-analysis/*.md đã có. Từ đó lập "sổ đăng ký AC" gồm mọi mã AC đã cấp, tên, stereotype, trách nhiệm.

[Role]
Bạn là chuyên gia phân tích hướng đối tượng, thành thạo quy trình Use-Case Analysis (hiện thực hoá use case bằng lớp phân tích boundary, control, entity), robustness analysis, các nguyên tắc phân bổ trách nhiệm GRASP (Information Expert, Creator, Controller, Low Coupling, High Cohesion) và ký pháp UML 2.5.1 cho sequence diagram, communication diagram, class diagram. Bạn làm việc ở mức phân tích: mô tả hệ thống làm gì và ai chịu trách nhiệm, không quyết định công nghệ.

[Action]
Làm tuần tự các bước sau. Mỗi bước dùng kết quả của bước trước.

A1. Nắm bối cảnh use case.
- Liệt kê tác nhân chính, tác nhân phụ và loại của từng tác nhân (Người / Hệ thống ngoài / Thiết bị / Thời gian).
- Use case có Tác nhân chính "-" (được include): lấy tác nhân từ use case gọi trong P03; boundary giao diện người dùng của phần hành vi này thuộc use case được include.
- Liệt kê quan hệ include, extend của use case và điểm mở rộng.
- Lập sổ đăng ký AC từ các file P07 đã có. Nếu chưa có file nào, sổ rỗng.
- Use case được include hoặc extend mà chưa có file P07: đặt trước tên và mã control của nó theo quy tắc đặt tên ở F3.3, ghi trạng thái "Tạm - chờ P07 của UC-xxx". Khi chạy P07 cho use case đó phải dùng đúng mã này.

A2. Bổ sung đặc tả use case (supplement the use-case specification).
- Với mỗi bước của luồng chính và luồng thay thế mà hệ thống thực hiện, viết lại ở dạng "hệ thống làm gì bên trong": lấy thông tin gì, từ đâu, kiểm tra điều kiện nào, ghi nhận gì, thông báo cho ai.
- Mô tả bổ sung chỉ làm rõ điều đã có trong đặc tả, BR, glossary. Không thêm chức năng mới. Nếu một bước mơ hồ tới mức không phân bổ được (ví dụ "hệ thống xử lý đơn"), xử lý theo chế độ giả định: NGHIEM_NGAT thì ghi câu hỏi Q-nn; CO_NHAN thì ghi giả định ASM-nn.
- Không nêu công nghệ (không "truy vấn SQL", "gọi REST", "lưu vào bảng").
- Thời hạn nội bộ (ví dụ chờ khách lấy tiền trong thời hạn của BR ở máy ATM) không là tác nhân và không là use case riêng. Control ghi nhận bắt đầu chờ bằng message tự gọi (ví dụ "// startWaitingForCashTaken (BR-04)") và nhận sự kiện hết hạn bằng message tự gọi có nhãn "after(<thời hạn>)", ví dụ "// after(BR-04) handleCashNotTaken"; luồng hết hạn vẽ bằng fragment alt hoặc break theo F5.
- Mốc thời gian phụ thuộc dữ liệu: nếu P02 có use case do tác nhân thời gian kích hoạt tại một mốc tính từ dữ liệu của một đối tượng (ví dụ nhắc bạn đọc khi tới hạn trả sách của phiếu mượn), thì use case tạo ra mốc đó có trách nhiệm đăng ký mốc (hẹn lịch), và use case làm mốc thay đổi hoặc mất hiệu lực (trả sách, gia hạn) có trách nhiệm hẹn lại hoặc huỷ mốc. Ghi bằng message của control ở bước tạo, đổi, kết thúc đối tượng, ví dụ "// scheduleDueReminder (phiếu mượn, hạn trả)", nguồn ghi mã use case do tác nhân thời gian kích hoạt. Mức phân tích không chọn cơ chế lập lịch; P12 thiết kế cơ chế đó.

A3. Tìm lớp boundary.
- Với mỗi cặp (tác nhân, use case) tìm một lớp boundary. Tác nhân người sinh boundary giao diện người dùng; tác nhân hệ thống ngoài sinh boundary giao diện hệ thống; tác nhân thiết bị sinh boundary giao diện thiết bị. Tác nhân thời gian (bộ lập lịch) không cần boundary riêng nếu nó chỉ kích hoạt use case; khi đó ghi rõ control nhận sự kiện kích hoạt.
- Boundary giao diện hệ thống và thiết bị đặt tên theo hệ thống hoặc thiết bị, nên được tái dùng ở mọi use case giao tiếp với cùng hệ thống đó (cùng mã AC). Boundary giao diện người dùng đặt tên theo tương tác của use case, không dùng chung giữa hai use case khác nhau.
- Boundary chỉ mô tả thông tin trao đổi và trách nhiệm giao tiếp, không mô tả bố cục, điều khiển giao diện, giao thức cụ thể.
- Tra sổ đăng ký AC: nếu khái niệm đã có mã thì dùng lại mã và tên, không tạo mã mới.
- Tác nhân chỉ tương tác trong phần hành vi của use case được include hoặc extend (ví dụ cổng thanh toán chỉ xuất hiện trong use case Thanh toán được include) thì boundary của nó thuộc phân tích của use case đó; không tạo lại trong use case đang phân tích.
- Tác nhân phụ là người chỉ nhận thông tin (ví dụ nhà hàng nhận đơn mới) vẫn cần một boundary; control gửi thông tin tới boundary đó. Boundary là giao diện người dùng khi thông tin hiện trên màn hình của hệ thống.
- Tác nhân người chỉ tương tác qua kênh không phải màn hình (email, SMS, thông báo đẩy), hoặc chỉ thao tác vật lý trên thiết bị (đưa thẻ vào máy, đẩy xe qua thanh chắn) và nhận kết quả qua kênh thông báo: boundary của tác nhân đó thuộc loại "Kênh thông báo", đặt tên theo kênh (F3.1). Thao tác vật lý đi vào hệ thống qua boundary thiết bị.

A4. Tìm lớp entity bằng lọc danh từ.
- Gạch chân (liệt kê) mọi danh từ và cụm danh từ trong luồng sự kiện, đặc tả bổ sung, dữ liệu vào ra, BR của use case.
- Loại theo thứ tự và ghi lý do cho từng ứng viên bị loại: trùng lặp hoặc đồng nghĩa (giữ tên theo glossary); mơ hồ (ví dụ "thông tin", "dữ liệu", "hệ thống"); là tác nhân hoặc ngoài phạm vi hệ thống; là khái niệm trong phạm vi nhưng không tham gia hành vi của use case này (chỉ được nhắc tới, không được đọc, ghi hay kiểm tra); là cấu trúc cài đặt (ví dụ "bảng", "file", "danh sách", "form"); là thuộc tính của ứng viên khác (giữ lại để dùng ở A7); là thao tác hoặc sự kiện được mô tả bằng danh từ (ví dụ "việc kiểm tra").
- Ứng viên còn lại là entity nếu hệ thống phải lưu hoặc quản lý thông tin của nó vượt quá một lần thực hiện use case, hoặc nó có hành vi riêng trên dữ liệu của nó.
- Một danh từ chỉ hồ sơ hoặc bản ghi của tác nhân (ví dụ hồ sơ bệnh nhân, tài khoản bạn đọc) có thể là entity dù tác nhân cùng tên đã bị loại; ghi rõ entity biểu diễn thông tin về tác nhân, không phải bản thân tác nhân.
- Tra sổ đăng ký AC và glossary để tái dùng mã.

A5. Tìm lớp control.
- Mặc định một control cho mỗi use case, đặt tên theo use case, chịu trách nhiệm điều phối trình tự, không giữ dữ liệu nghiệp vụ lâu dài.
- Use case chỉ đọc hoặc ghi đơn giản một entity, không có điều phối, về nguyên tắc có thể không cần control. Mặc định vẫn giữ một control tối giản để quy tắc tương tác F6 (boundary không gọi entity) áp dụng thống nhất cho mọi use case. Chỉ bỏ control khi YEU_CAU_BO_SUNG cho phép; khi đó boundary được gọi entity trong riêng use case này và phải ghi lý do trong mục "Vấn đề còn mở".
- Chỉ tách thêm control khi có một phần điều phối lớn dùng lại ở nhiều use case, và phần đó chưa là use case được include.

A6. Phân bổ hành vi cho lớp và mô hình hoá tương tác.
- Với mỗi bước trong đặc tả bổ sung, xác định trách nhiệm cần có và giao cho lớp theo nguyên tắc: hành vi giao tiếp với tác nhân thuộc boundary; hành vi trên dữ liệu mà một entity nắm giữ thuộc entity đó (Information Expert); hành vi điều phối riêng của use case thuộc control (Controller). Khi dữ liệu nằm ở nhiều lớp: giao cho một lớp và thêm quan hệ tới lớp kia; hoặc tạo lớp mới giữ trách nhiệm đó; hoặc giao cho control. Chọn phương án cho coupling thấp nhất và cohesion cao nhất, ghi lý do.
- Lớp tạo ra đối tượng entity mới là lớp chứa hoặc ghi nhận nó, hoặc có dữ liệu khởi tạo nó (Creator).
- Vẽ sequence diagram cho luồng chính. Luồng thay thế ngắn (1-3 message khác biệt) vẽ trong cùng sơ đồ bằng combined fragment alt, opt hoặc break với guard lấy từ điều kiện trong đặc tả; luồng thay thế kết thúc use case dùng break (F5). Luồng dài hoặc làm sơ đồ vượt ngưỡng ở mục F5 thì vẽ trang riêng.
- Kiểm tra từng message theo quy tắc tương tác ở mục F6. Sửa ngay các vi phạm.
- Vẽ communication diagram cùng message và cùng số thứ tự với sequence diagram của luồng chính. Luồng thay thế đã gộp vào sơ đồ đó (chỉ khi DAY_DU): thêm vào communication diagram với cùng số thứ tự.

A7. Mô tả trách nhiệm và thuộc tính.
- Gom mọi message mà một lớp nhận thành danh sách trách nhiệm của lớp đó. Message giống nhau về ý nghĩa gộp thành một trách nhiệm.
- Gán thuộc tính cho entity từ các danh từ bị loại vì "là thuộc tính" ở A4 và từ bảng dữ liệu vào ra của đặc tả. Boundary có thể có thuộc tính là thông tin nó hiển thị hoặc thu nhận. Control thường không có thuộc tính nghiệp vụ.

A8. Lập VOPC.
- Mỗi link trong communication diagram sinh ra ít nhất một quan hệ trong VOPC. Không có quan hệ nào trong VOPC mà không có link hoặc bằng chứng từ đặc tả.
- Ghi multiplicity khi đặc tả hoặc BR nêu rõ; nếu không rõ thì để trống và ghi câu hỏi hoặc giả định, không đoán. Quan hệ cuối cùng được chốt ở P08.

A9. Tự kiểm tra theo [Target], sửa, rồi mới xuất kết quả.

[Format]
Xuất file P07-uc-analysis/UC-nnn-slug-analysis.md theo khung C5 của 00-Conventions.md, tiêu đề "# P07 - Phân tích use case UC-nnn <Tên> - <Tên hệ thống>". Cột "Phạm vi" của bảng thông tin ghi mã use case. Nội dung chính gồm các mục sau, đúng thứ tự.

F1. Bối cảnh use case
Bảng: | Thuộc tính | Giá trị |, gồm: Mã và tên UC; Tác nhân chính (ACT, loại); Tác nhân phụ (ACT, loại); Include (UC); Được include bởi (UC); Extend (UC, điểm mở rộng, điều kiện); Được extend bởi (UC, điểm mở rộng, điều kiện); File P07 đã có được dùng làm sổ đăng ký AC.

F2. Đặc tả bổ sung
Bảng: | Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
- Định nghĩa: bản viết lại các bước hệ thống thực hiện, nói rõ thông tin lấy từ đâu, kiểm tra gì, ghi nhận gì, đủ chi tiết để giao từng việc cho một lớp.
- Quy tắc: STT bước giữ nguyên như P04 (1, 2, 3a, 3a1...). Bước do tác nhân thực hiện chép nguyên, cột bổ sung ghi "Không đổi". Mỗi ô bổ sung tối đa 3 câu.
- Mức hợp lý: đọc cột bổ sung phải trả lời được "ai giữ dữ liệu này" và "điều kiện nào được kiểm tra". Nếu còn động từ chung chung như "xử lý", "quản lý", "cập nhật thông tin" mà không nêu thông tin gì, là chưa đủ.
- Lỗi thường gặp: thêm bước mới không có trong đặc tả (quá lớn); chỉ chép lại nguyên văn (quá nhỏ); nêu công nghệ (nhầm mức trừu tượng).
- Ví dụ đúng (phòng khám): "Hệ thống hiển thị các khung giờ trống" --> "Hệ thống lấy lịch làm việc của bác sĩ đã chọn trong ngày đã chọn, loại các khung giờ đã có lịch hẹn ở trạng thái Đã xác nhận, hiển thị các khung giờ còn lại."
- Ví dụ đúng (thư viện): "Hệ thống ghi nhận mượn sách" --> "Hệ thống tạo phiếu mượn gắn bạn đọc và các bản sách, đặt hạn trả theo BR-03, chuyển trạng thái từng bản sách sang Đang mượn."
- Ví dụ sai: "Hệ thống gọi API /slots và lưu vào bảng appointment" (sai: chi tiết công nghệ). "Hệ thống gửi thêm email khuyến mãi" khi đặc tả không nêu (sai: thêm chức năng).

F3. Tìm lớp phân tích
F3.1 Bảng boundary: | Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary (Giao diện người dùng / Kênh thông báo / Giao diện hệ thống / Giao diện thiết bị) | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
- Định nghĩa: lớp trung gian giữa hệ thống và một thứ bên ngoài (người, hệ thống, thiết bị); phụ thuộc môi trường.
- Quy tắc: một boundary cho mỗi cặp tác nhân và use case. Tên boundary giao diện người dùng dạng <Hành động hoặc đối tượng><Form|Screen|UI> theo hậu tố ghi ở trường HAU_TO_TEN_LOP của hồ sơ dự án (khi trường này là "Mặc định" thì dùng Form và giữ nguyên cho mọi UC); tên boundary hệ thống hoặc thiết bị theo tên hệ thống, thiết bị, kèm hậu tố ghi ở HAU_TO_TEN_LOP (khi "Mặc định" thì không hậu tố, ví dụ PaymentGateway, BarcodeScanner; dự án có thể chọn hậu tố như Boundary, Gateway, Device).
- Boundary kênh thông báo: đặt tên theo kênh và nội dung, không dùng hậu tố của form (Form, Screen, UI) vì không có màn hình, ví dụ OverdueNoticeEmail, GuestSmsNotifier. Hậu tố theo HAU_TO_TEN_LOP nếu hồ sơ quy định riêng cho loại này.
- Tên trùng entity: nếu tên thiết bị hoặc hệ thống ngoài trùng tên một entity (cùng khái niệm vừa là tác nhân vừa là dữ liệu hệ thống quản lý), boundary luôn thêm hậu tố Device (thiết bị) hoặc Gateway (hệ thống ngoài), kể cả khi HAU_TO_TEN_LOP là "Mặc định", và ghi lý do. Ví dụ (bãi đỗ xe): thanh chắn vừa là thiết bị vừa là entity có trạng thái do hệ thống quản lý --> entity ParkingBarrier, boundary ParkingBarrierDevice. Nhờ vậy P10 không có hai lớp thiết kế cùng tên.
- Mức hợp lý: số boundary bằng số tác nhân tham gia (trừ tác nhân thời gian); tác nhân người thao tác vật lý trên thiết bị và nhận kết quả qua kênh thông báo được tính qua boundary kênh thông báo. Nhiều hơn là đang tách boundary theo màn hình (việc của P11a); ít hơn là có tác nhân không được phục vụ.
- Lỗi thường gặp: boundary theo từng màn hình hoặc từng hộp thoại (quá nhỏ); một boundary "MainUI" cho mọi use case (quá lớn); boundary chứa kiểm tra nghiệp vụ như "kiểm tra số dư", "tính phí" (nhầm với control hoặc entity); boundary mang chi tiết công nghệ như "HttpClient", "RestEndpoint", "ReactComponent".
- Ví dụ đúng (giao đồ ăn, UC Đặt món): Khách hàng --> PlaceFoodOrderForm; Cổng thanh toán --> PaymentGateway (tái dùng nếu UC Thanh toán đã tạo).
- Ví dụ đúng (thư viện, UC Nhắc hạn trả): Bạn đọc chỉ nhận thư nhắc --> DueReminderEmail, loại Kênh thông báo.
- Ví dụ sai: DishListScreen, CartPopup, ConfirmDialog là ba boundary riêng cho cùng khách hàng trong cùng UC (sai: tách theo màn hình). ReturnReminderForm cho bạn đọc chỉ nhận email (sai: hậu tố của form cho kênh không có màn hình, P11a sẽ không có màn hình nào cho nó).

F3.2 Bảng lọc danh từ: | STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
Cột Kết luận chỉ nhận một trong các giá trị: Entity (AC-E-...); Loại - trùng hoặc đồng nghĩa với X; Loại - mơ hồ; Loại - là tác nhân hoặc ngoài phạm vi; Loại - cấu trúc cài đặt; Loại - thuộc tính của X; Loại - thao tác hoặc sự kiện; Loại - tham số của quy tắc BR-nn (hằng số, ngưỡng, đơn vị nằm trong một quy tắc); Loại - thuộc phân tích của UC-nnn (khái niệm do use case được include hoặc mở rộng tạo ra và xử lý); Loại - không tham gia hành vi của use case này (khái niệm của UC-nnn), dùng cho khái niệm trong phạm vi chỉ được nhắc tới, ví dụ "kho" trong UC Kiểm kê một ngăn kệ khi luồng không đọc hay ghi gì của kho.
- Mức hợp lý: mọi danh từ trong luồng sự kiện đều xuất hiện trong bảng; mỗi dòng bị loại có lý do cụ thể.
- Lỗi thường gặp: bỏ qua bước lọc và liệt kê entity theo hiểu biết chung (sai C1); giữ "Thông tin đặt phòng" và "Đơn đặt phòng" thành hai entity (trùng); biến "Địa chỉ giao hàng", "Số điện thoại" thành entity khi chúng không có hành vi và định danh riêng (thuộc tính trá hình).
- Ví dụ đúng (khách sạn): "số đêm" --> Loại - thuộc tính của Booking; "hệ thống" --> Loại - mơ hồ; "lễ tân" --> Loại - là tác nhân; "phòng" --> Entity AC-E-Room.
- Ví dụ sai: "danh sách phòng trống" --> Entity RoomList (sai: danh sách là cấu trúc cài đặt, kết quả của một truy vấn trên Room).

F3.3 Bảng control: | Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
- Quy tắc: tên dạng <TênUseCase>Controller hoặc <TênUseCase>Control, theo trường HAU_TO_TEN_LOP của hồ sơ dự án (mặc định Controller), thống nhất toàn dự án.
- Lỗi thường gặp: một control "SystemManager" cho mọi use case (quá lớn); control cho từng bước (quá nhỏ).

F3.4 Bảng lớp phân tích (bảng lõi, bước P08 đọc bảng này):
| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
- AC: theo C3, dạng AC-B-<Tên>, AC-C-<Tên>, AC-E-<Tên>. Cùng khái niệm đã có mã ở use case khác thì dùng lại đúng mã. Không cấp mã mới cho khái niệm đã có.
- Stereotype: boundary, control hoặc entity (chữ thường).
- Tên: danh từ số ít, PascalCase, theo NGON_NGU_TEN_PHAN_TU; entity lấy từ glossary.
- Trách nhiệm: mỗi trách nhiệm một dòng (thẻ <br>), dạng "// tênTráchNhiệm: mô tả ngắn". Tên trách nhiệm là cụm động từ lowerCamelCase, không tham số, không kiểu trả về. Đây là trách nhiệm, chưa phải phương thức. Chỉ ghi trách nhiệm được dùng trong use case này; lớp tái dùng không chép lại trách nhiệm của use case khác (P08 sẽ gộp).
- Thuộc tính chính: tên lowerCamelCase, có thể kèm kiểu khái niệm (Ngày, Giờ, Số tiền, Số lượng, Văn bản, Trạng thái); không kiểu vật lý (varchar, int, BigDecimal).
- Bước UC nguồn: các STT bước làm phát sinh lớp.
- Loại boundary: chỉ ghi cho boundary (Giao diện người dùng / Kênh thông báo / Giao diện hệ thống / Giao diện thiết bị); entity, control ghi "-".
- Mới hoặc tái dùng: "Mới" hoặc "Tái dùng từ UC-nnn". Nếu tái dùng mà bổ sung trách nhiệm, ghi "Tái dùng từ UC-nnn, bổ sung trách nhiệm".
- GL: mã thuật ngữ tương ứng, nếu có.
Mức hợp lý (kiểm tra được):
- Mỗi lớp có ít nhất một trách nhiệm trong use case này.
- Một control có khoảng 2-10 trách nhiệm trong một use case. Trên 10, hoặc control nắm quy tắc tính toán thuộc dữ liệu của entity, là dấu hiệu god control.
- Mỗi entity tham gia use case nên có ít nhất một trách nhiệm hành vi ngoài lưu giữ dữ liệu (kiểm tra, tính toán, chuyển trạng thái trên dữ liệu của nó). Entity chỉ có trách nhiệm dạng "get/set" là entity thiếu trách nhiệm (anemic); ghi nhận nếu đặc tả thật sự không có hành vi nào trên dữ liệu đó.
- Số lớp của một use case thường 4-12. Dưới 4 thì kiểm tra có bỏ sót entity. Trên 12 thì kiểm tra có entity là thuộc tính trá hình hoặc use case quá lớn (đề xuất sửa P02).
Lỗi thường gặp và dấu hiệu:
- God control: control chứa "tính tổng tiền", "kiểm tra còn hạn", "đổi trạng thái đơn" trong khi dữ liệu thuộc entity. Sửa: chuyển cho entity nắm dữ liệu.
- Entity thiếu trách nhiệm: Order chỉ có "// getTotal" trong khi đặc tả có quy tắc tính tổng. Sửa: "// calculateTotal".
- Boundary chứa logic nghiệp vụ: form "// validateCouponRule". Boundary chỉ được kiểm tra hình thức dữ liệu nhập (bắt buộc, định dạng); quy tắc nghiệp vụ thuộc control hoặc entity.
- Lớp mang chi tiết công nghệ: OrderDAO, OrderRepository, OrderDTO, JsonParser, SessionBean ở mức phân tích. Sửa: bỏ, các lớp này chỉ xuất hiện từ P10.
- Message là chữ ký hàm cụ thể: "calculateFee(distance: double): BigDecimal". Sửa: "// calculateDeliveryFee".
- Lớp là thuộc tính trá hình: PhoneNumber, Address, Price thành entity mà không có định danh và hành vi riêng. Sửa: đưa về thuộc tính.
Ví dụ đúng (quản lý kho, UC Nhập kho theo phiếu):
| AC-C-ReceiveGoodsController | control | ReceiveGoodsController | // receiveGoods: điều phối nhập kho<br>// confirmReceipt: chốt phiếu nhập | - | 1-7 | - | Mới | - |
| AC-E-GoodsReceipt | entity | GoodsReceipt | // addLine: thêm dòng hàng<br>// checkQuantityMatchesPurchaseOrder: đối chiếu số lượng với đơn mua | receiptNo, receivedDate, status | 3, 5 | - | Mới | GL-07 |
Ví dụ sai: | AC-E-ReceiptTable | entity | ReceiptTable | lưu phiếu | id int, date varchar | 3 | ... | (sai: tên là cấu trúc cài đặt, kiểu vật lý, trách nhiệm không ở dạng // cụm động từ).

F4. Phân bổ hành vi
Bảng: | Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc (Giao tiếp tác nhân / Information Expert / Controller / Creator / Lớp mới / Giao cho control) | Lý do khi có lựa chọn khác |
- Mọi bước hệ thống thực hiện trong luồng chính và luồng thay thế có ít nhất một dòng.
- Cột "Lý do khi có lựa chọn khác" bắt buộc khi dữ liệu nằm ở nhiều lớp.

F5. Sequence diagram phân tích
Với mỗi sơ đồ (một trang trong diagrams/P07-sequence-UC-nnn.drawio), xuất:
a) Tên sơ đồ và luồng thể hiện (ví dụ "SD1 - Luồng chính và 3a, 5a").
b) Bảng lifeline (bảng Node): | ID | Loại (Actor / Lifeline / Fragment) | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
   - Nhãn lifeline dạng ":TênLớp" (đối tượng vô danh) hoặc "tên:TênLớp" khi cần phân biệt hai đối tượng cùng lớp. Actor đặt bên trái, sau đó boundary của actor, control, các entity, cuối cùng boundary hệ thống ngoài hoặc thiết bị và actor phụ ở bên phải.
   - Fragment: nhãn ghi toán tử (alt, opt, break, loop, ref) và guard trong ngoặc vuông, ví dụ "alt [khung giờ còn trống]". Cột Thuộc về của message nằm trong fragment ghi ID fragment.
   - Luồng thay thế kết thúc use case (cột Quay lại / Kết thúc của P04 ghi "Kết thúc") dùng break: khi guard đúng, các message trong break được thực hiện rồi interaction kết thúc, phần còn lại của luồng chính không chạy. Không dùng opt cho luồng này, vì sau opt luồng chính vẫn tiếp tục.
c) Bảng message (bảng lõi, bảng Edge mở rộng): | STT | Từ | Đến | Message | Loại (Đồng bộ / Trả về / Tự gọi / Tạo) | Fragment | Bước UC |
   - STT: đánh số phân cấp 1, 1.1, 1.1.1: message con được gửi trong khi xử lý message cha. Luồng thay thế trong fragment dùng tiếp số của luồng chính. Message trả về dùng STT của message gọi, ghi thêm "(trả về)" ở cột STT (ví dụ "1.1 (trả về)"); message trả về không xuất hiện trên communication diagram.
   - Message: tên trách nhiệm dạng "// tênTráchNhiệm", có thể ghi dữ liệu truyền đi bằng lời trong ngoặc tròn, ví dụ "// reserveSlot (khung giờ, bệnh nhân)". Message từ actor tới boundary mô tả hành động của actor, cùng dạng tên như các message khác, ví dụ "// selectTimeSlot". Không kiểu dữ liệu, không kiểu trả về.
   - Message trả về chỉ vẽ khi mang dữ liệu có ý nghĩa cho bước sau; ghi dữ liệu trả về, ví dụ "danh sách khung giờ trống".
   - Bước UC: STT bước trong F2. Mọi message phải có bước UC; mọi bước hệ thống phải có ít nhất một message.
Ngưỡng tách sơ đồ: một trang tối đa khoảng 30 message và tối đa 3 fragment ở mức ngoài cùng; vượt ngưỡng thì tách luồng thay thế sang trang riêng, bắt đầu bằng fragment ref tới sơ đồ luồng chính hoặc ghi rõ điểm rẽ nhánh.
Quy tắc ngữ nghĩa UML của sequence diagram:
- Lifeline là đối tượng (instance), không phải lớp; nhãn có dấu hai chấm.
- Message đồng bộ: mũi tên đặc, đầu đặc. Message trả về: nét đứt, đầu mở. Tự gọi: mũi tên quay về chính lifeline.
- Thời gian đi từ trên xuống; không có message đi lên.
- Combined fragment: alt có ít nhất hai toán hạng ngăn bởi đường nét đứt, mỗi toán hạng có guard; opt có một toán hạng; break có một toán hạng, kết thúc interaction bao ngoài sau khi chạy; loop ghi guard hoặc số lần.
- Không vẽ message giữa hai actor. Actor không nhận message từ control hoặc entity.
Xử lý include và extend trong sequence diagram:
- Use case này include use case X: tại bước include, control của use case này gửi một message tới control của X (hoặc dùng fragment ref tên "UC-xxx <tên>"). Không vẽ lại nội bộ của X; nội bộ đó thuộc artifact P07 của X.
- Use case này được extend bởi Y tại điểm mở rộng E: tại vị trí E, vẽ fragment opt với guard là điều kiện extend, bên trong là ref tới "UC-yyy <tên>". Không vẽ nội bộ của Y.
- Use case này là use case extend Y: sơ đồ bắt đầu tại điểm mở rộng; lifeline boundary và control của use case gốc được phép xuất hiện nếu hành vi mở rộng cần chúng, nhưng chỉ vẽ phần hành vi mở rộng.
- Use case được include: phân tích như một use case bình thường với tác nhân là tác nhân của use case gọi; control của nó nhận message từ control của use case gọi.

F6. Quy tắc tương tác giữa các lớp phân tích (kiểm tra trên mọi message và mọi link)
| Từ \ Đến | Actor | Boundary | Control | Entity |
|---|---|---|---|---|
| Actor | Không | Được | Không | Không |
| Boundary | Được (actor của nó) | Không | Được | Không |
| Control | Không | Được | Được | Được |
| Entity | Không | Không | Không | Được, khi có quan hệ cấu trúc |
- Ngoại lệ: tác nhân thời gian --> Control: Được (A3), vì tác nhân thời gian không có boundary riêng; ngoại lệ không áp dụng cho tác nhân khác.
- Actor chỉ trao đổi với boundary, trừ tác nhân thời gian (dòng trên).
- Boundary chỉ trao đổi với actor của nó và với control. Boundary không gọi entity và không gọi boundary khác.
- Control gọi boundary (kể cả boundary hệ thống ngoài), entity, và control của use case được include.
- Entity không gọi boundary, không gọi control. Entity gọi entity khác chỉ khi hai lớp có quan hệ cấu trúc (ví dụ Order hỏi OrderLine để tính tổng).
- Actor phụ là hệ thống ngoài hoặc thiết bị chỉ trao đổi với boundary của nó.
Liệt kê trong artifact bảng: | Vi phạm | Message hoặc link | Cách sửa đã áp dụng |, hoặc ghi "Không có".

F7. Communication diagram
File diagrams/P07-communication-UC-nnn.drawio, phạm vi là luồng chính của sơ đồ SD1.
Communication diagram cho luồng thay thế (chỉ khi DAY_DU): thêm các luồng thay thế đã gộp vào SD1, giữ STT của SD1.
a) Bảng Node: | ID | Loại (Actor / Object) | Nhãn | Stereotype | Thuộc về | Ghi chú |. Nhãn đối tượng giống lifeline ở F5.
b) Bảng Edge (link): | ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT, dạng "1: // ... (-->)", "1.1: // ... (<--)") | Chiều message (Nguồn-->Đích hoặc Đích-->Nguồn) |
- Mỗi cặp đối tượng có trao đổi được nối bằng đúng một link; các message giữa cặp đó ghi trên link, giữ nguyên STT của sequence diagram.
- Communication diagram và phần sequence diagram nó thể hiện tương đương ngữ nghĩa: cùng tập message, cùng STT. Nếu lệch là lỗi.
Quy tắc ngữ nghĩa: link là đường liền không mũi tên; chiều của từng message ghi trong nhãn link bằng "(-->)" (từ Nguồn tới Đích của link) hoặc "(<--)" (ngược lại); không vẽ message trả về. Có thể vẽ thêm mũi tên nhỏ cạnh nhãn cho dễ đọc; mũi tên này có ID dạng <ID link>-A<n> và không cần dòng trong bảng Edge.

F8. VOPC (View Of Participating Classes)
File diagrams/P07-class-UC-nnn.drawio.
a) Bảng Node (lớp): | ID (mã AC) | Loại (Class) | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
   - Ngăn thuộc tính: từ F3.4. Ngăn trách nhiệm: các "// tênTráchNhiệm" của lớp trong use case này.
b) Bảng quan hệ (bảng Edge, P08 đọc bảng này): | ID | Lớp A | Lớp B | Loại (Association / Aggregation / Composition / Generalization / Dependency) | Multiplicity (dạng "A <m> - B <m>", ví dụ "A 1 - B 0..*") | Vai trò | Nguồn (link trong F7 hoặc bước UC, BR) |
   - ID dạng R-UCnnn-nn.
   - Mỗi link trong F7 giữa hai lớp khác nhau sinh một quan hệ. Link actor-boundary không vào VOPC (actor không là lớp trong VOPC), trừ khi dự án yêu cầu vẽ actor.
   - Mức phân tích: association giữa boundary và control, control và entity thường là quan hệ tạm (dùng trong một lần thực hiện); ghi Loại "Association" với ghi chú "tạm thời"; P08 và P12 sẽ quyết định dạng thiết kế.
   - Aggregation, composition, generalization giữa entity chỉ ghi khi đặc tả, BR hoặc glossary cho bằng chứng (ví dụ "đơn gồm nhiều dòng món, dòng món không tồn tại khi đơn bị xoá" --> composition).
Quy tắc ngữ nghĩa UML của class diagram phân tích: lớp vẽ bằng hình chữ nhật ba ngăn với stereotype «boundary», «control», «entity» ở ngăn tên (hoặc biểu tượng boundary, control, entity theo C7); association là đường liền, multiplicity ở hai đầu; composition là hình thoi đặc ở phía lớp toàn thể; aggregation thoi rỗng; generalization tam giác rỗng về phía lớp cha. Không ghi visibility (+, -) và kiểu vật lý ở mức phân tích.

F9. Ma trận truy vết
Bảng: | Bước UC | Message (STT) | Lớp tham gia (AC) |. Mọi bước hệ thống có ít nhất một dòng; mọi message có một bước.

F10. File .drawio
Với mỗi sơ đồ, sinh file theo C7.3: XML không nén, cell id="0" và id="1", ID cell trùng ID trong bảng mô hình, toạ độ bội số 10.
Bố cục riêng:
- Sequence: lifeline đặt ở y=40, cách nhau 160 theo trục x, rộng 120; lifeline của đối tượng được tạo bởi message loại Tạo có đỉnh đặt ngang y của message đó (theo UML 2.5.1), không đặt ở y=40; chiều cao lifeline đủ chứa mọi message; message đầu tiên ở y=120, mỗi message sau cách 40; fragment là hình chữ nhật (style: rounded=0;whiteSpace=wrap;html=1;fillColor=none;verticalAlign=top;align=left;) bao các message của nó, nhãn toán tử ở góc trên trái. Message là edge có sourcePoint và targetPoint nằm trên hai lifeline, nhãn "STT: message".
- Communication: đối tượng là hình chữ nhật (rounded=0;whiteSpace=wrap;html=1;) nhãn gạch chân không bắt buộc, hoặc biểu tượng boundary, control, entity theo C7; actor bên trái; control ở giữa; entity phía dưới; boundary hệ thống ngoài bên phải. Link style endArrow=none;html=1;. Mũi tên chiều message (tuỳ chọn, F7) là edge ngắn (endArrow=block;endFill=1;html=1;) không gắn nguồn đích, đặt cạnh nhãn, ID <ID link>-A<n>.
- VOPC: dùng style Class của C7, edgeStyle=orthogonalEdgeStyle; boundary hàng trên, control hàng giữa, entity hàng dưới; multiplicity và vai trò của bảng quan hệ (dạng "A m - B n") vẽ thành hai nhãn ở hai đầu cạnh theo C7.3, không thành một nhãn giữa cạnh.
Khung XML tối thiểu cho một lifeline và một message:
  <mxCell id="L1" value=":BookAppointmentForm" style="shape=umlLifeline;perimeter=lifelinePerimeter;container=1;collapsible=0;recursiveResize=0;html=1;" vertex="1" parent="1"><mxGeometry x="200" y="40" width="120" height="600" as="geometry"/></mxCell>
  <mxCell id="M1" value="1: // requestBooking" style="endArrow=block;endFill=1;html=1;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="100" y="120" as="sourcePoint"/><mxPoint x="260" y="120" as="targetPoint"/></mxGeometry></mxCell>
Chạy bằng agent có quyền ghi file thì ghi file vào diagrams/; chạy bằng chat thì in nội dung từng file trong một khối code xml riêng, sau bảng mô hình tương ứng.

F11. Các mục kiểm soát theo C5: Câu hỏi mở, Giả định (khi CO_NHAN), Đề xuất sửa artifact trước (ví dụ đặc tả thiếu luồng ngoại lệ cho lỗi hệ thống ngoài, use case quá lớn), Vấn đề còn mở.

[Target]
Tự kiểm tra từng mục, trả lời Đạt hoặc Không đạt; mục Không đạt mà không sửa được thì ghi vào "Vấn đề còn mở".
1. Mọi bước hệ thống trong luồng chính và luồng thay thế của đặc tả có trong F2, F4 và có ít nhất một message.
2. Không có message, trách nhiệm hay lớp nào không truy được về một bước UC, BR hoặc mục dữ liệu của đặc tả.
3. Mỗi tác nhân tương tác trực tiếp trong use case này (trừ tác nhân thời gian và tác nhân chỉ thuộc use case được include hoặc extend) có đúng một boundary.
4. Có một control cho use case; chỉ không có khi YEU_CAU_BO_SUNG cho phép và lý do được ghi rõ.
5. Mọi danh từ trong luồng sự kiện có trong bảng lọc F3.2 với kết luận và lý do.
6. Mọi khái niệm đã có mã AC trong sổ đăng ký được dùng lại đúng mã và tên; không có hai mã cho một khái niệm.
7. Không có vi phạm quy tắc tương tác F6.
8. Không lớp nào mang chi tiết công nghệ; không message nào là chữ ký hàm có kiểu.
9. Không có god control (quá 10 trách nhiệm hoặc giữ quy tắc thuộc dữ liệu của entity); mỗi entity có trách nhiệm hành vi hoặc được ghi nhận lý do.
10. Boundary không chứa quy tắc nghiệp vụ.
11. Include và extend được thể hiện bằng message tới control của use case liên quan hoặc fragment ref/opt, không vẽ lại nội bộ của use case khác.
12. Communication diagram có cùng tập message và cùng STT với phần sequence diagram tương ứng: luồng chính, và luồng thay thế đã gộp (chỉ khi DAY_DU).
13. Mỗi link giữa hai lớp trong communication diagram có quan hệ tương ứng trong VOPC; VOPC không có quan hệ thiếu căn cứ.
14. Bảng mô hình và file .drawio khớp nhau; file .drawio đáp ứng C7.3.
15. Luồng thay thế kết thúc use case dùng break; thời hạn nội bộ dùng message tự gọi "after(...)"; mốc thời gian mà use case do tác nhân thời gian kích hoạt phụ thuộc vào có message hẹn, hẹn lại hoặc huỷ ở use case tạo, đổi, kết thúc mốc.
16. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này, ưu tiên cao hơn quy tắc mặc định (trừ C1) | Ví dụ: "Dùng hậu tố UI cho mọi boundary người dùng, hậu tố Controller cho control."; "Không vẽ communication diagram cho luồng thay thế."; "Vẽ lớp phân tích bằng biểu tượng robustness thay vì hình chữ nhật."}}
````

## 5. Ghi chú cho người dùng

- Chạy use case được include trước. Nếu chạy use case gọi trước, AI sẽ tạo control cho use case được include ở dạng tạm; khi chạy lại use case được include phải dùng đúng mã đó.
- Luôn đính kèm mọi file P07 đã có. Thiếu file, AI có thể cấp mã AC mới cho khái niệm đã có (ví dụ AC-E-Appointment và AC-E-Booking cho cùng lịch hẹn). Nếu đã xảy ra, P08 sẽ phát hiện và gộp, nhưng sửa sớm rẻ hơn.
- Kết quả quá dài khi use case có nhiều luồng thay thế: dùng placeholder LUONG_CAN_VE để chạy thành nhiều lần (luồng chính trước, các luồng thay thế sau) với cùng file đầu ra, tăng phiên bản.
- Nếu AI báo nhiều câu hỏi mở kiểu "bước X không đủ chi tiết để phân bổ", nên quay lại P04 bổ sung đặc tả rồi chạy lại bước này, không nên chuyển sang CO_NHAN chỉ để có kết quả nhanh.
- Dùng độc lập (không chạy cả pipeline): cần tối thiểu một đặc tả use case có luồng sự kiện đánh số và danh sách tác nhân có phân loại. Glossary và supplementary spec có thể thay bằng một đoạn mô tả thuật ngữ và quy tắc trong YEU_CAU_BO_SUNG; khi đó mã GL, BR để trống.

## 6. Căn cứ

- Jacobson I., Booch G., Rumbaugh J., The Unified Software Development Process (1999): khái niệm use-case realization, lớp phân tích boundary, control, entity.
- Kruchten P., The Rational Unified Process: An Introduction, 3rd ed. (2003): hoạt động Use-Case Analysis, bổ sung đặc tả, phân bổ trách nhiệm.
- Rosenberg D., Stephens M., Use Case Driven Object Modeling with UML: Theory and Practice (2007): robustness analysis và quy tắc tương tác giữa actor, boundary, controller, entity.
- Larman C., Applying UML and Patterns, 3rd ed. (2004): GRASP (Information Expert, Creator, Controller, Low Coupling, High Cohesion), lọc danh từ để tìm khái niệm.
- OMG, Unified Modeling Language 2.5.1 (2017): ngữ nghĩa sequence diagram, communication diagram, combined fragment, class diagram.
- Fowler M., UML Distilled, 3rd ed. (2003): cách dùng sequence và communication diagram ở mức khái niệm.
- Ambler S., The Elements of UML 2.0 Style (2005): quy tắc bố cục, đặt tên và độ lớn sơ đồ.
- Wirfs-Brock R., McKean A., Object Design: Roles, Responsibilities, and Collaborations (2003): mô tả trách nhiệm, phát hiện lớp ôm đồm.
