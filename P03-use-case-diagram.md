# P03 - Mô hình và sơ đồ use case (Use Case Diagram)

## 1. Mục đích

Bước này xây dựng mô hình use case hoàn chỉnh từ danh sách tác nhân (P01) và danh sách use case (P02): xác định quan hệ association giữa tác nhân và use case, quan hệ «include», «extend», generalization giữa các use case và giữa các tác nhân, rồi vẽ sơ đồ use case tổng quát và các sơ đồ phân rã. Mỗi quan hệ phải có lý do và đúng ngữ nghĩa UML; mỗi sơ đồ có bảng mô hình Node/Edge và file .drawio sinh từ bảng đó.

Sơ đồ use case là bản cam kết giữa khách hàng và đội phát triển về phạm vi chức năng. P04 dùng bảng quan hệ để viết điểm gọi include và điểm mở rộng trong đặc tả; các bước phân tích dùng sơ đồ để biết tác nhân nào nối với use case nào.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md | Có | Luật chung, đặc biệt mục C7 về sơ đồ |
| Đầu vào | project-profile.md | Có | Tên hệ thống (nhãn boundary), chế độ giả định |
| Đầu vào | P00-problem-brief.md | Có (khi chạy pipeline) | Truy vết REQ cho quan hệ |
| Đầu vào | P01-actors.md | Có | Tác nhân, loại, tính chất, tổng quát hoá tác nhân |
| Đầu vào | P02-usecases.md | Có | Use case, tác nhân chính và phụ, mức, nhóm chức năng |
| Đầu vào | P02R-review.md | Tuỳ chọn | Đối chiếu các UCR đã được P02 áp dụng hoặc ghi lý do không áp dụng; ghi nhận review khi không UCR nào được áp dụng; không lấy use case trực tiếp từ P02R |
| Đầu ra | P03-usecase-model.md | - | Bảng quan hệ, điểm mở rộng, danh sách sơ đồ, bảng Node/Edge |
| Đầu ra | diagrams/P03-usecase-overview.drawio | - | Sơ đồ tổng quát |
| Đầu ra | diagrams/P03-usecase-<nhóm>.drawio | Khi cần phân rã | Sơ đồ phân rã theo nhóm chức năng hoặc theo tác nhân |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, P00-problem-brief.md, P01-actors.md, P02-usecases.md.
- Chạy một lần cho toàn hệ thống. Chạy lại khi P01 hoặc P02 thay đổi; giữ nguyên mã quan hệ đã cấp.
- Sau P02R mà không áp dụng UCR nào (P02 không chạy lại): ghi vào YEU_CAU_BO_SUNG "Đã review P02R <phiên bản>, không áp dụng UCR-xx, UCR-yy (lý do)"; P03 chép dòng này vào mục Vấn đề còn mở.
- Khi chạy bằng chat (không có quyền ghi file), AI trả nội dung P03-usecase-model.md và nội dung từng file .drawio trong các code block riêng (Mục 6); người dùng lưu thành file theo tên đã ghi. Khi chạy bằng agent có quyền ghi file, XML chỉ nằm trong file .drawio, Mục 6 chỉ ghi đường dẫn.
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| KIEU_DUONG_ASSOCIATION | Tuỳ chọn | Có vẽ đầu mũi tên trên đường nối tác nhân - use case hay không |
| CACH_PHAN_RA_SO_DO | Tuỳ chọn | Phân rã sơ đồ theo nhóm chức năng hay theo tác nhân |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù của dự án cho bước này |

## 4. Prompt

````text
[Context]
Đọc theo thứ tự: 00-Conventions.md (luật chung, đặc biệt mục C7), project-profile.md, P00-problem-brief.md, P01-actors.md, P02-usecases.md.
Chỉ dùng tác nhân có trong P01 và use case có trong P02 Mục 4 (bảng 4a; bỏ qua ứng viên có kết luận khác "Giữ"). Nếu YEU_CAU_BO_SUNG ghi đã review P02R mà không áp dụng UCR nào, chép nguyên dòng đó vào mục Vấn đề còn mở. Không đổi tên, mã, tác nhân chính hoặc phụ của use case đã chốt; nếu thấy P02 hoặc P01 sai, ghi vào "Đề xuất sửa artifact trước".

Kiểu đường association:
{{PH:KIEU_DUONG_ASSOCIATION | Hướng dẫn: [TUỲ CHỌN] chọn một. KHONG_MUI_TEN (mặc định theo Conventions C7): đường liền, không đầu mũi tên. MUI_TEN_KHOI_XUONG: đường liền, đuôi ở bên khởi xướng, đầu mũi tên mở ở bên nhận (tác nhân chính --> use case; use case --> tác nhân phụ). Dùng mặc định thì thay cả khối bằng "Không có" | Ví dụ: "KHONG_MUI_TEN" ; "MUI_TEN_KHOI_XUONG"}}

Cách phân rã sơ đồ khi cần nhiều sơ đồ:
{{PH:CACH_PHAN_RA_SO_DO | Hướng dẫn: [TUỲ CHỌN] chọn một. THEO_NHOM (mặc định): mỗi nhóm chức năng của P02 một sơ đồ. THEO_TAC_NHAN: mỗi tác nhân chính người một sơ đồ, gồm mọi use case của tác nhân đó. Dùng mặc định thì thay cả khối bằng "Không có" | Ví dụ: "THEO_NHOM" (hệ thống kho có các nhóm Nhập kho, Xuất kho, Kiểm kê, Danh mục) ; "THEO_TAC_NHAN" (hệ thống phòng khám cần một sơ đồ riêng cho Bệnh nhân, Lễ tân, Bác sĩ)}}

[Role]
Bạn là chuyên gia mô hình hoá UML, nắm vững ngữ nghĩa chương 18 Use Cases của UML 2.5.1 (subject, actor, association, include, extend, extension point, generalization) và các quy tắc trình bày sơ đồ use case của Ambler. Bạn dùng quan hệ giữa use case một cách tiết kiệm: chỉ khi có lý do rõ ràng, không dùng để vẽ trình tự hay phân rã chức năng. Bạn thành thạo định dạng XML của draw.io.

[Action]
Thực hiện tuần tự các bước sau.

Bước 1. Lập danh sách phần tử.
Liệt kê tác nhân (ACT) và use case (UC) sẽ có trên mô hình, kèm Loại, Tính chất của tác nhân và Mức, Nhóm chức năng của use case, lấy từ P01, P02.

Bước 2. Xác định association giữa tác nhân và use case.
2.1. Với mỗi UC, tạo một association tới mỗi tác nhân chính và mỗi tác nhân phụ ghi trong P02. Association nghĩa là tác nhân và use case trao đổi thông điệp trong toàn bộ cuộc đối thoại, không chỉ một bước.
2.2. Không nối tác nhân chính của UC gốc với UC được include hoặc UC mở rộng (extension) chỉ vì UC gốc gọi tới nó; tác nhân đó đã tương tác qua UC gốc. Chỉ nối tác nhân với UC được include hoặc UC mở rộng khi: (a) đó là tác nhân phụ chỉ tham gia trong phần hành vi này (ví dụ cổng SMS chỉ được gọi trong UC mở rộng gửi tin), hoặc (b) UC đó cũng là mục tiêu mà tác nhân khởi xướng độc lập (P02 ghi tác nhân chính cho nó và có sự kiện kích hoạt riêng). Trường hợp (b) ghi lý do trong cột Lý do. Tác nhân chính mà P02 ghi kèm "(qua UC-xxx)" không thuộc trường hợp (b): không nối.
2.3. Khi có tổng quát hoá tác nhân: nối UC chung với tác nhân cha; tác nhân con kế thừa, không vẽ lại cùng association cho con. Chỉ nối con với UC riêng của con.
2.4. Không bao giờ tạo association giữa hai tác nhân, hoặc giữa hai use case.

Bước 3. Xác định «include».
Ngữ nghĩa: UC gốc (base) gọi tường minh toàn bộ hành vi của UC được include tại một vị trí xác định trong luồng của UC gốc, mỗi lần UC gốc chạy qua vị trí đó. UC gốc không hoàn chỉnh nếu thiếu phần được include. UC được include không đứng một mình: nó chỉ được thực hiện như một phần của UC gốc.
Tạo «include» từ UC-A tới UC-B chỉ khi đồng thời:
  a) UC-B được P02 giữ ở mức Subfunction theo điều kiện Q4a (hành vi dùng chung cho từ hai UC trở lên) hoặc Q4c (tách phần rất lớn để dễ quản lý) hoặc Q4d (mục tiêu con có kết quả riêng, được nguồn mô tả tách bạch, thực hiện lại hoặc thất bại độc lập với UC-A), hoặc UC-B là UC User-goal mà nguồn nêu rõ luôn phải thực hiện như một phần bắt buộc của UC-A.
  b) Hành vi của UC-B là bắt buộc trong mọi kịch bản thành công của UC-A (phép thử: "UC-A có bao giờ đạt mục tiêu mà không cần UC-B không?" Nếu có, không phải include; xem Bước 4).
  c) Có căn cứ trong nguồn.
Không dùng include cho: vẽ trình tự các bước của một quy trình khi phần được tách không thoả Q4a đến Q4d của P02 (phân rã chức năng); UC được P02 tách ra theo Q4 thì được include, kể cả khi nó nằm ở đầu hoặc cuối luồng của UC gốc; xác thực đăng nhập của mọi UC (dùng tiền điều kiện); hành vi chỉ một UC dùng và nhỏ (để nguyên là bước trong UC đó); hành vi tuỳ chọn hoặc có điều kiện.
Không lồng include quá hai tầng (UC-A include UC-B include UC-C là tối đa). Không tạo chu trình include.

Bước 4. Xác định «extend».
Ngữ nghĩa: UC mở rộng (extension) bổ sung hành vi vào UC gốc tại một điểm mở rộng (extension point) có tên trong UC gốc, chỉ khi điều kiện mở rộng đúng. UC gốc hoàn chỉnh và có ý nghĩa khi không có phần mở rộng; UC gốc không biết tới UC mở rộng. Mũi tên đi từ UC mở rộng tới UC gốc.
Tạo «extend» từ UC-X (mở rộng) tới UC-Y (gốc) chỉ khi đồng thời:
  a) UC-X được P02 giữ theo điều kiện Q4b (hành vi tuỳ chọn hoặc ngoại lệ, đủ lớn hoặc là dịch vụ bổ sung), hoặc là UC mà nguồn mô tả như một lựa chọn thêm trong khi thực hiện UC-Y.
  b) UC-Y đạt được mục tiêu của nó trong kịch bản không có UC-X.
  c) Xác định được điều kiện mở rộng (một mệnh đề kiểm chứng được) và tên điểm mở rộng (một vị trí trong luồng của UC-Y, đặt tên theo bước nghiệp vụ, không theo số thứ tự bước).
Không dùng extend cho: lỗi nhỏ, luồng thay thế ngắn (để trong đặc tả UC-Y ở P04); hành vi bắt buộc (dùng include); tuỳ chọn chỉ 1-2 bước.

Bước 5. Xác định generalization.
5.1. Giữa use case: chỉ khi các UC con là các dạng cụ thể của cùng một mục tiêu, thoả phép thử "là một" (UC con là một loại của UC cha, thay được UC cha), UC cha định nghĩa phần chung của luồng, và nguồn mô tả khác biệt đáng kể giữa các dạng (U-R12 của P02). Mũi tên tam giác rỗng từ con tới cha. UC cha có thể trừu tượng (tên in nghiêng) khi không bao giờ được thực hiện trực tiếp.
5.2. Giữa tác nhân: lấy từ cột Tổng quát hoá từ của P01; không tự tạo mới ở bước này (nếu thấy cần, ghi "Đề xuất sửa artifact trước").
5.3. Không dùng generalization để diễn tả "gồm có" hoặc "gọi tới".

Bước 6. Kiểm tra tổng thể quan hệ theo bảng lỗi D-AP ở [Format]. Nguyên tắc tiết kiệm: nếu có thể che mọi UC được include và UC mở rộng mà người đọc vẫn hiểu mục đích chính của hệ thống, mô hình có cấu trúc tốt; nếu che đi thì mất các mục tiêu chính, quan hệ đang bị dùng để phân rã chức năng. Tỷ lệ UC Subfunction trên khoảng 20% tổng số UC là dấu hiệu dùng quan hệ quá mức.

Bước 7. Xử lý use case mới phát sinh.
Nếu phát hiện một hành vi dùng chung hoặc tuỳ chọn cần tách mà P02 chưa có UC tương ứng: không tự thêm vào sơ đồ. Ghi vào bảng "UC đề xuất bổ sung" (mã tạm UC-nnn tiếp theo số lớn nhất của P02, trạng thái "Chờ cập nhật P02") và vào "Đề xuất sửa artifact trước". Chỉ vẽ UC này khi YEU_CAU_BO_SUNG cho phép vẽ UC đề xuất; khi đó ghi chú "(đề xuất)" trong nhãn.

Bước 8. Lập kế hoạch sơ đồ.
Đếm N là tổng số UC sẽ vẽ trên sơ đồ, kể cả UC mức Subfunction và UC Đăng nhập, và M là số tác nhân. Chọn phương án:
  - N không quá 20 và M không quá 8: một sơ đồ tổng quát đầy đủ mọi phần tử và quan hệ. Thêm sơ đồ phân rã chỉ cho nhóm có từ 3 quan hệ include hoặc extend trở lên làm sơ đồ tổng quát rối.
  - N từ 21 đến 40, hoặc M trên 8: sơ đồ tổng quát gồm mọi tác nhân, mọi UC (kể cả Subfunction và Đăng nhập) và mọi association; không vẽ include, extend, generalization giữa UC trên sơ đồ này, UC được include hoặc UC mở rộng không có association ghi "(quan hệ ở sơ đồ <tên>)" ở cột Ghi chú của bảng Node. Sơ đồ phân rã chỉ tạo cho nhóm (hoặc tác nhân, theo CACH_PHAN_RA_SO_DO) có ít nhất một quan hệ include, extend hoặc generalization giữa UC, và vẽ đầy đủ quan hệ của nhóm đó. Nhóm không có quan hệ nào giữa UC không có sơ đồ phân rã, vì nội dung đã nằm đủ trên sơ đồ tổng quát.
  - N trên 40: sơ đồ tổng quát ở mức package: mỗi nhóm chức năng là một package (hình thư mục) bên trong boundary, ghi số UC trong nhãn, tác nhân đặt quanh boundary không có đường nối, kèm bảng "Tác nhân - Nhóm" trong artifact; mỗi nhóm một sơ đồ phân rã.
  - UC Đăng nhập giữ theo U-R01 của P02 luôn vẽ trên sơ đồ tổng quát (khi sơ đồ tổng quát không ở mức package), nối mọi tác nhân phải xác thực, để người đọc thấy vai trò nào phải đăng nhập.
  - Mỗi sơ đồ phân rã nên có không quá khoảng 15 UC; nhóm lớn hơn thì chia nhỏ tiếp.
Các ngưỡng trên là heuristic về khả năng đọc; lệch được nếu có lý do, ghi vào "Vấn đề còn mở".
Trong sơ đồ phân rã, tác nhân và UC thuộc nhóm khác chỉ xuất hiện khi có quan hệ trực tiếp với UC trong nhóm; UC của nhóm khác được ghi chú "(nhóm <tên>)" ở cột Ghi chú của bảng Node.

Bước 9. Bố trí từng sơ đồ theo quy tắc bố cục ở [Format] phần D, tính toạ độ cho mọi node.

Bước 10. Lập bảng Node và bảng Edge cho từng sơ đồ, rồi sinh file .drawio từ đúng hai bảng đó theo Conventions C7 và phần E của [Format].

Bước 11. Chạy checklist [Target]; sửa mục chưa đạt; mục không sửa được ghi "Vấn đề còn mở".

[Format]
Xuất file P03-usecase-model.md theo khung Conventions C5, và nội dung các file .drawio. Không thêm lời dẫn.

=== Phần A. Ký hiệu và ngữ nghĩa bắt buộc ===
| Phần tử / quan hệ | Ký hiệu | Chiều | Quy tắc |
|---|---|---|---|
| Subject (boundary) | Hình chữ nhật, tên hệ thống ở trên cùng | - | Chứa mọi use case; không chứa tác nhân |
| Tác nhân | Hình người que, tên bên dưới | - | Luôn bên ngoài boundary. Tác nhân hệ thống ngoài có thể ghi thêm «system» trên tên; tác nhân thiết bị có thể ghi «device» |
| Use case | Hình elip, tên bên trong | - | Luôn bên trong boundary. UC trừu tượng tên in nghiêng |
| Association | Đường liền | Không chiều; hoặc đuôi ở bên khởi xướng, đầu mũi tên mở ở bên nhận (tác nhân chính --> use case; use case --> tác nhân phụ) khi KIEU_DUONG_ASSOCIATION = MUI_TEN_KHOI_XUONG | Chỉ nối tác nhân với use case. Không nét đứt, không tam giác, không nhãn stereotype |
| «include» | Đường nét đứt, đầu mũi tên mở, nhãn «include» | Từ UC gốc tới UC được include | Bắt buộc, UC gốc không hoàn chỉnh nếu thiếu |
| «extend» | Đường nét đứt, đầu mũi tên mở, nhãn «extend» | Từ UC mở rộng tới UC gốc | Tuỳ chọn, có điều kiện, tại điểm mở rộng có tên |
| Điểm mở rộng | Ngăn "extension points" bên trong elip của UC gốc | - | Mỗi điểm mở rộng một dòng |
| Điều kiện extend | Ghi chú (note) gắn vào đường «extend»: "Condition: {mệnh đề}" và "extension point: <tên>" | - | Bắt buộc có cho mọi extend |
| Generalization | Đường liền, đầu tam giác rỗng | Từ con tới cha | Giữa hai use case hoặc giữa hai tác nhân, không lẫn loại |

Bảng lỗi sơ đồ (dùng ở Bước 6 và checklist; P02R dùng cùng mã):
| Mã | Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|---|
| D-AP01 | Include dùng để vẽ trình tự hoặc phân rã chức năng | Chuỗi UC nối nhau bằng include theo thứ tự thời gian mà từng phần không thoả Q4a đến Q4d của P02 (Chọn phòng --> Nhập thông tin khách --> Xác nhận đặt phòng); UC được include chỉ một UC dùng, nhỏ và không có kết quả riêng. UC được tách theo Q4 không thuộc lỗi này | Gộp về UC gốc, các phần thành bước trong đặc tả |
| D-AP02 | Extend ngược chiều | Mũi tên «extend» đi từ UC gốc tới UC mở rộng | Đảo chiều: từ UC mở rộng tới UC gốc |
| D-AP03 | Include ngược chiều | Mũi tên «include» đi từ UC được include tới UC gốc | Đảo chiều: từ UC gốc tới UC được include |
| D-AP04 | Nhầm include và extend | Hành vi tuỳ chọn vẽ bằng include; hành vi bắt buộc vẽ bằng extend | Áp dụng phép thử Bước 3b |
| D-AP05 | Include lồng quá hai tầng hoặc có chu trình | A include B include C include D; A include B include A | Gộp tầng trong cùng; bỏ chu trình |
| D-AP06 | Association giữa hai tác nhân | Đường nối trực tiếp tác nhân với tác nhân (lễ tân nối bệnh nhân) | Xoá; tương tác giữa người với người nằm ngoài hệ thống. Nếu người đó thao tác hệ thống thì nối họ với UC |
| D-AP07 | Association giữa hai use case | Đường liền không nhãn giữa hai elip | Thay bằng include, extend, generalization nếu đúng ngữ nghĩa, hoặc xoá |
| D-AP08 | Sai ký hiệu trên đường tác nhân - use case | Nét đứt, tam giác, nhãn «include» hoặc «extend», mũi tên hai chiều, đầu mũi tên ở bên khởi xướng | Dùng đường liền theo KIEU_DUONG_ASSOCIATION |
| D-AP09 | Tác nhân trong boundary hoặc use case ngoài boundary | Hình người que nằm trong khung hệ thống | Đưa tác nhân ra ngoài, use case vào trong |
| D-AP10 | Thiếu boundary hoặc boundary không có tên | Không có khung; khung không ghi tên hệ thống | Thêm khung có tên theo TEN_HE_THONG |
| D-AP11 | Tác nhân chính nối với UC được include hoặc UC mở rộng | Tác nhân nối cả UC gốc và UC được include chỉ vì UC gốc gọi tới | Xoá đường nối thừa (Bước 2.2) |
| D-AP12 | Extend thiếu điều kiện hoặc điểm mở rộng | Không có note điều kiện; UC gốc không có ngăn extension points | Bổ sung theo Bước 4c |
| D-AP13 | Generalization sai | Tam giác chỉ về con; con không "là một" cha; dùng generalization cho quan hệ gồm có | Đảo chiều, hoặc đổi sang include, hoặc bỏ |
| D-AP14 | Tác nhân hoặc use case cô lập | Tác nhân không nối UC nào; UC User-goal không nối tác nhân nào (trừ UC được include, UC mở rộng, UC cha trừu tượng) | Nối đúng theo P02, hoặc đề xuất sửa P01, P02 |
| D-AP15 | Mạng nhện | Nhiều đường cắt nhau; một tác nhân nối hàng chục UC trên cùng sơ đồ | Sắp lại bố cục; tổng quát hoá tác nhân; tách sơ đồ |
| D-AP16 | Quá nhiều phần tử trên một sơ đồ | Vượt ngưỡng ở Bước 8 | Tách sơ đồ theo Bước 8 |
| D-AP17 | Quá nhiều quan hệ giữa use case | Tỷ lệ UC Subfunction trên khoảng 20%; che UC được include và UC mở rộng thì mất mục tiêu chính | Gộp lại, chỉ giữ quan hệ có lý do ở Bước 3, 4 |
| D-AP18 | Stereotype sai tên | «uses», «includes», «extends», «call» | Dùng đúng «include», «extend» |
| D-AP19 | Sơ đồ thể hiện luồng màn hình hoặc trình tự | Mũi tên nối UC theo thứ tự thao tác, UC mang tên màn hình | Sơ đồ use case không thể hiện trình tự; trình tự thuộc đặc tả, activity diagram hoặc sơ đồ chuyển màn hình |
| D-AP20 | Thiếu hoặc thừa sơ đồ | Sơ đồ tổng quát thiếu UC (kể cả Đăng nhập) khi N không quá 40; sơ đồ phân rã của nhóm không có include, extend, generalization giữa UC, chỉ lặp lại nội dung sơ đồ tổng quát | Lập lại kế hoạch sơ đồ theo Bước 8 |

Ví dụ đúng và sai về quan hệ (các miền khác nhau):
- Include đúng: "Rút tiền", "Chuyển khoản", "Xem số dư" của máy ATM cùng «include» "Xác thực khách hàng" (đưa thẻ, nhập PIN, kiểm tra, xử lý nhập sai), vì cả ba đều bắt buộc có đoạn tương tác này và đoạn này đủ lớn.
- Include đúng: "Đặt lịch tái khám" (bệnh nhân) và "Đặt lịch tái khám cho bệnh nhân" (điều dưỡng) cùng «include» "Chọn khung giờ khám" (xem lịch làm việc của bác sĩ đã khám lần trước, chọn khung giờ trống, giữ chỗ tạm). "Chọn khung giờ khám" được giữ thành UC Subfunction theo Q4 a của P02 vì hai UC cùng dùng đoạn tương tác này.
- Include đúng: "Đặt món" «include» "Thanh toán đơn" của hệ thống giao đồ ăn, khi nguồn nêu đơn chỉ được ghi nhận sau khi thanh toán thành công, nêu phương thức thanh toán và trường hợp thanh toán bị từ chối. "Thanh toán đơn" được giữ theo Q4d của P02 (kết quả riêng là khoản tiền được xác nhận; thanh toán lại được mà đơn không bị huỷ); cổng thanh toán là tác nhân phụ nối với "Thanh toán đơn", khách hàng chỉ nối với "Đặt món".
- Include sai: "Lập phiếu nhập kho" «include» "Nhập thông tin nhà cung cấp", «include» "Nhập danh sách hàng", «include» "Xác nhận phiếu" (phân rã chức năng, D-AP01).
- Extend đúng: "Nộp phí phạt quá hạn" «extend» "Nhận trả sách", điểm mở rộng "Kiểm tra hạn trả", điều kiện {sách được trả sau hạn}. Nhận trả sách vẫn hoàn chỉnh khi sách trả đúng hạn.
- Extend đúng: "Yêu cầu xe đưa đón" «extend» "Đặt phòng", điểm mở rộng "Chọn dịch vụ kèm theo", điều kiện {khách chọn dịch vụ đưa đón sân bay}.
- Extend sai: "Kiểm tra số dư" «extend» "Rút tiền" (bước bắt buộc, phải là bước trong luồng hoặc include, D-AP04). Mũi tên từ "Đặt món" tới "Áp dụng mã giảm giá" gắn nhãn «extend» (ngược chiều, D-AP02).
- Generalization đúng: "Thanh toán phí gửi xe bằng thẻ" và "Thanh toán phí gửi xe bằng ví điện tử" là con của "Thanh toán phí gửi xe" khi hai cách có luồng và tác nhân phụ khác nhau đáng kể.
- Generalization tác nhân đúng: "Thủ kho" và "Kế toán kho" là con của "Người dùng nội bộ" khi cả hai cùng "Tra cứu tồn kho" và "Xem báo cáo xuất nhập tồn" theo cùng một cách.

=== Phần B. Nội dung P03-usecase-model.md ===

Mục 1. Bảng quan hệ
| ID | Nguồn | Đích | Loại | Điều kiện extend / điểm mở rộng | Lý do | REQ | Sơ đồ |
- ID: RL-nn, đánh số theo thứ tự: association (theo thứ tự UC), include, extend, generalization.
- Nguồn, Đích: mã ACT hoặc UC. Association ghi nguồn là tác nhân, đích là use case. Include: nguồn là UC gốc. Extend: nguồn là UC mở rộng. Generalization: nguồn là con.
- Loại: Association / Include / Extend / Generalization.
- Điều kiện extend / điểm mở rộng: chỉ với Extend, dạng "{điều kiện} tại <tên điểm mở rộng>"; loại khác ghi "-".
- Lý do: với Association ghi "Tác nhân chính" hoặc "Tác nhân phụ: <dịch vụ cung cấp>"; với Include, Extend, Generalization ghi điều kiện ở Bước 3, 4, 5 đã thoả (ví dụ "Dùng chung cho UC-003, UC-004 (Bước 3a)").
- Sơ đồ: tên các sơ đồ thể hiện quan hệ này.

Mục 2. Điểm mở rộng
| UC gốc | Điểm mở rộng | Vị trí trong luồng (mô tả nghiệp vụ) | UC mở rộng | Điều kiện |
Ghi "Không có" nếu không có extend. P04 dùng bảng này để đặt điểm mở rộng trong đặc tả.

Mục 3. UC đề xuất bổ sung (chỉ khi có)
| UC (tạm) | Tên (VI) | Tên (EN) | Lý do | Quan hệ dự kiến | REQ | Trạng thái |

Mục 4. Danh sách sơ đồ
| Sơ đồ | Phạm vi | Tác nhân | Use case | File |
Ví dụ: "Tổng quát | Toàn hệ thống, không vẽ quan hệ giữa UC | ACT-01..ACT-06 | 24 UC (gồm Đăng nhập) | diagrams/P03-usecase-overview.drawio". "Nhóm Đặt lịch | UC-001..UC-006, có 2 include | ACT-01, ACT-02, ACT-05 | 6 | diagrams/P03-usecase-booking.drawio".
Tên file theo Conventions C7.2: diagrams/P03-usecase-overview.drawio cho sơ đồ tổng quát; diagrams/P03-usecase-<slug nhóm hoặc slug tác nhân>.drawio cho sơ đồ phân rã, slug theo Conventions C4.
Khi dùng sơ đồ tổng quát mức package, thêm bảng: | Tác nhân | Nhóm (package) có dùng |.

Mục 5. Bảng mô hình của từng sơ đồ (mỗi sơ đồ một tiểu mục, tên tiểu mục là tên sơ đồ)
Bảng Node:
| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
- ID: mã ACT-nn, UC-nnn; boundary là SYS; package nhóm chức năng là GRP-<slug> (không phải mã PKG của Conventions C3); note là N-nn.
- Loại: Actor / UseCase / Boundary / Package / Note.
- Nhãn: tên tiếng Việt (hoặc theo NGON_NGU_TEN_PHAN_TU của hồ sơ dự án); UC có điểm mở rộng thì nhãn gồm tên và ngăn extension points.
- Stereotype: «system», «device» cho tác nhân không phải người nếu dùng; «abstract» không dùng, UC trừu tượng thể hiện bằng chữ nghiêng và ghi ở Ghi chú.
- Thuộc về: SYS với use case, GRP-... nếu có package; "-" với tác nhân.
- x, y, w, h: toạ độ và kích thước theo phần D, là bội số của 10.
Bảng Edge:
| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
- Điểm uốn: cột tuỳ chọn theo Conventions C7.1; điền khi đường thẳng sẽ cắt qua node (thường ở bố cục dải L-12: đường tới UC cột hai, đường tới UC ở cột giữa), ngược lại ghi "-".
- ID trùng mã RL-nn ở Mục 1; đường nối note là RL-nn-N.
- Nhãn: «include», «extend» hoặc để trống.

Mục 6. Nội dung file .drawio: chỉ có khi chạy bằng chat (không có quyền ghi file), mỗi file một code block, dòng đầu code block là tên file trong chú thích XML. Khi đã ghi được file .drawio, mục này chỉ liệt kê đường dẫn các file, không chép lại XML.

Mục 7. Các mục kiểm soát theo Conventions C5.

=== Phần C. Mức hợp lý (heuristic) ===
- Số quan hệ include cộng extend thường không quá khoảng một phần ba số UC User-goal; nhiều hơn cần xem lại D-AP01, D-AP17.
- Include lồng tối đa hai tầng.
- Sơ đồ vẽ đủ quan hệ giữa UC không quá khoảng 20 UC (đếm mọi UC vẽ trên sơ đồ, kể cả Subfunction, như N ở Bước 8) và 8 tác nhân; sơ đồ phân rã không quá khoảng 15 UC. Sơ đồ tổng quát chỉ vẽ association (Bước 8, phương án thứ hai) được tới khoảng 40 UC.
- Mỗi extend có đúng một điểm mở rộng trong đa số trường hợp; nhiều điểm mở rộng cho một extend chỉ khi nguồn mô tả rõ.

=== Phần D. Quy tắc bố cục ===
L-01 Boundary: góc trên trái tại (200, 40); nhãn tên hệ thống ở trên cùng; kích thước bao mọi UC với lề trong tối thiểu 40.
L-02 Tác nhân chính (kể cả tác nhân thời gian, hệ thống ngoài là chính) đặt bên trái boundary, cột x = 60. Tác nhân chính quan trọng nhất (nhiều UC nhất hoặc gắn với UC khởi đầu quy trình) đặt trên cùng.
L-03 Tác nhân phụ đặt bên phải boundary, cột x = cạnh phải boundary + 80. Tác nhân vừa chính vừa phụ đặt theo vai trò chiếm đa số trên sơ đồ đó. Tác nhân đặt bên phải theo đa số vẫn giữ các association mà nó là tác nhân chính; ghi ngoại lệ này vào Vấn đề còn mở, không tính là vi phạm L-02 và Target 10.
L-04 Kích thước: tác nhân w = 30, h = 60; UC w = 160, h = 70 (tên dài hoặc có ngăn extension points dùng w = 200, h = 90); note w = 200, h = 60.
L-05 Use case sắp theo trình tự thời gian nghiệp vụ từ trên xuống dưới (khi dùng bố cục dải theo L-12, sắp như vậy trong từng dải) (việc xảy ra trước đặt trên), UC chính của nhóm ở góc trên trái của boundary. Khoảng cách dọc giữa hai UC là 40 (bước dòng 110 với h = 70).
L-06 UC được include đặt bên phải UC gốc, cùng hàng hoặc giữa các UC gốc dùng chung nó (cột thứ hai, cách cột UC gốc 80).
L-07 UC mở rộng đặt bên dưới UC gốc (hàng kế tiếp, lệch phải 40 nếu cần tránh đường), note điều kiện đặt cạnh đường «extend».
L-08 UC con của generalization đặt bên dưới UC cha; tác nhân con đặt bên dưới tác nhân cha.
L-09 Mỗi tác nhân đặt ngang tâm dọc của nhóm UC nó nối tới, để đường nối ngắn; sắp thứ tự tác nhân theo thứ tự UC để tránh đường cắt nhau. Nếu vẫn cắt, đổi thứ tự hàng UC trước khi chấp nhận đường cắt.
L-10 Không có hai node chồng nhau; khoảng cách tối thiểu giữa hai node là 40; mọi toạ độ là bội số của 10; không đường nào cắt qua node.
L-11 Không dùng màu để mang ngữ nghĩa (Conventions C7).
L-12 Sơ đồ có trên 12 UC: không xếp mọi UC thành một cột (sơ đồ sẽ quá cao, đường từ tác nhân xa bị kéo dài và cắt qua elip). Bố trí theo dải ngang:
  - Chia boundary thành các dải ngang, mỗi tác nhân chính bên trái một dải theo thứ tự L-02. Dải của một tác nhân chứa các UC mà chỉ tác nhân đó là tác nhân chính, sắp theo trình tự thời gian (L-05). Hai dải liền nhau cách nhau 80 để có hành lang cho đường đi ngang. Tác nhân đặt ngang tâm dọc dải của nó (L-09).
  - Trong một dải dùng tối đa hai cột, cột hai cách cột một 80 và lệch xuống nửa bước dòng (55) so với cột một. Nhờ vậy tâm dọc của mỗi UC cột hai rơi vào khe giữa hai UC cột một, và tâm dọc của mỗi UC cột một rơi vào khe giữa hai UC cột hai. Dải cần hơn hai cột thì tách tác nhân đó ra sơ đồ phân rã hoặc đổi CACH_PHAN_RA_SO_DO.
  - Đường từ tác nhân tới UC cột hai có một điểm uốn tại (cạnh trái boundary + 40, tâm dọc của UC đích), rồi đi ngang qua khe của cột một tới UC đích. Đường từ UC cột một sang tác nhân phụ bên phải đi ngang qua khe của cột hai.
  - UC nối từ hai tác nhân chính trở lên (Đăng nhập, UC dùng chung của nhiều vai trò) đặt ở cột giữa, bên phải mọi dải và bên trái các UC chủ yếu nối tác nhân phụ, căn tâm dọc theo khoảng giữa các tác nhân nó nối. Đường từ mỗi tác nhân tới UC này có điểm uốn: đi xuống hoặc lên tới hành lang giữa hai dải gần nhất tại x = cạnh trái boundary + 20, đi ngang theo hành lang tới cột giữa, rồi tới UC. Riêng UC chỉ nối tác nhân của hai dải kề nhau có thể đặt ở cột một, giữa hai dải đó; khi đó hành lang giữa hai dải nới thành 150 (UC cao 70, mỗi phía cách 40).
  - Chỉ dùng cột theo nhóm chức năng (mỗi nhóm một cột) khi phần lớn UC của các nhóm được nhiều tác nhân chính dùng chung, không tách được theo dải tác nhân; khi đó vẫn áp dụng điểm uốn qua khe như trên.
  - Sau khi đặt toạ độ, kiểm từng đường: mỗi đoạn thẳng (từ nguồn tới điểm uốn đầu, giữa hai điểm uốn, từ điểm uốn cuối tới đích) không được đi qua hình chữ nhật bao của bất kỳ elip nào ngoài hai đầu mút. Đoạn nào vi phạm thì đổi hàng UC hoặc thêm điểm uốn, ghi vào cột Điểm uốn của bảng Edge (Conventions C7.1).

=== Phần E. Quy tắc sinh file .drawio ===
- Cấu trúc theo Conventions C7.3: mxfile, diagram (name là tên sơ đồ), mxGraphModel, root, cell id="0" và cell id="1" parent="0". Không nén nội dung.
- ID của mxCell trùng ID trong bảng Node, Edge.
- Style dùng đúng bảng style của Conventions C7.3, bổ sung:
  - Use case trừu tượng thêm fontStyle=2;. Boundary thêm fontStyle=1; cho tên hệ thống.
  - Association khi KIEU_DUONG_ASSOCIATION = MUI_TEN_KHOI_XUONG: source là bên khởi xướng.
  - Include, Extend: value="«include»" hoặc value="«extend»".
  - Đường nối note: endArrow=none;dashed=1;html=1;
- Use case là cell con của boundary thì toạ độ tính tương đối với boundary; cách đơn giản và được khuyến nghị: mọi node có parent="1" với toạ độ tuyệt đối, boundary vẽ trước để nằm dưới.
- Mọi edge có parent="1", source và target là ID node; đường nối note có target là ID của edge «extend». Nếu công cụ hiển thị không hỗ trợ nối vào cạnh, đặt note sát giữa đường «extend» và bỏ đường nối note, ghi vào Ghi chú của bảng Edge.
- Nhãn có xuống dòng dùng html=1 với thẻ br đã escape trong XML (&lt;br&gt;). Ngăn extension points: tên UC, một đường kẻ (&lt;hr&gt;), dòng "extension points" rồi mỗi điểm một dòng.
- Ký tự đặc biệt trong nhãn (&, <, >, dấu ngoặc kép) phải được escape theo XML.
Khung mẫu (miền thư viện, rút gọn; thay bằng dữ liệu thật):
<mxfile host="app.diagrams.net">
  <diagram id="P03-usecase-overview" name="Tổng quát">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" page="1" pageWidth="1169" pageHeight="827" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="SYS" value="Hệ thống quản lý thư viện" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=none;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="40" width="520" height="330" as="geometry" />
        </mxCell>
        <mxCell id="ACT-01" value="Thủ thư" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="120" width="30" height="60" as="geometry" />
        </mxCell>
        <mxCell id="ACT-03" value="Hệ thống email" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;" vertex="1" parent="1">
          <mxGeometry x="800" y="240" width="30" height="60" as="geometry" />
        </mxCell>
        <mxCell id="UC-004" value="Nhận trả sách&lt;hr&gt;extension points&lt;br&gt;Kiểm tra hạn trả" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="260" y="100" width="200" height="90" as="geometry" />
        </mxCell>
        <mxCell id="UC-005" value="Nộp phí phạt quá hạn" style="ellipse;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="260" width="160" height="70" as="geometry" />
        </mxCell>
        <mxCell id="RL-01" style="endArrow=none;html=1;" edge="1" parent="1" source="ACT-01" target="UC-004">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="RL-02" style="endArrow=none;html=1;" edge="1" parent="1" source="ACT-03" target="UC-005">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="RL-03" value="«extend»" style="endArrow=open;dashed=1;html=1;" edge="1" parent="1" source="UC-005" target="UC-004">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="N-01" value="Condition: {sách được trả sau hạn}&lt;br&gt;extension point: Kiểm tra hạn trả" style="shape=note;whiteSpace=wrap;html=1;size=14;" vertex="1" parent="1">
          <mxGeometry x="500" y="200" width="200" height="60" as="geometry" />
        </mxCell>
        <mxCell id="RL-03-N" style="endArrow=none;dashed=1;html=1;" edge="1" parent="1" source="N-01" target="RL-03">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
(Trong khung mẫu, Hệ thống email là tác nhân phụ của UC mở rộng vì chỉ phần mở rộng gửi biên nhận phí phạt; đó là minh hoạ Bước 2.2a.)

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Mọi tác nhân và use case trên sơ đồ có trong P01, P02 (hoặc ở Mục 3 với nhãn "(đề xuất)" khi được phép); không đổi tên, mã.
2. Mọi UC User-goal nối với tác nhân chính của nó (trực tiếp hoặc qua tác nhân cha); mọi tác nhân phụ trong P02 được nối với UC tương ứng.
3. Không có association giữa hai tác nhân hoặc giữa hai use case.
4. Không có tác nhân chính nào nối với UC được include hoặc UC mở rộng, trừ trường hợp Bước 2.2b có lý do.
5. Mọi include thoả Bước 3a, 3b, 3c, đúng chiều từ UC gốc; không lồng quá hai tầng; không có chu trình.
6. Mọi extend thoả Bước 4a, 4b, 4c, đúng chiều từ UC mở rộng, có điều kiện và điểm mở rộng, có trong bảng Điểm mở rộng.
7. Mọi generalization thoả phép thử "là một", tam giác ở phía cha, không lẫn giữa tác nhân và use case.
8. Không có lỗi D-AP01 đến D-AP20.
9. Tác nhân ở ngoài boundary, use case ở trong; boundary có tên hệ thống.
10. Tác nhân chính bên trái, tác nhân phụ bên phải; UC sắp theo trình tự thời gian từ trên xuống (trong từng dải khi dùng L-12); include bên phải, extend bên dưới UC gốc; sơ đồ trên 12 UC dùng bố cục dải theo L-12; không đường nào cắt qua elip.
11. Số phần tử mỗi sơ đồ trong ngưỡng Bước 8, hoặc có lý do ghi ở "Vấn đề còn mở".
12. Bảng Node, Edge và file .drawio khớp nhau từng phần tử (cùng ID, cùng nhãn, cùng số lượng).
13. File .drawio là XML hợp lệ, có cell 0 và 1, không nén, toạ độ bội số của 10, không có node chồng nhau, khoảng cách tối thiểu 40.
14. Mọi quan hệ include, extend, generalization có lý do và truy vết REQ.
15. Artifact có đủ các mục kiểm soát theo C5.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho bước này; ưu tiên cao hơn quy tắc mặc định của bước (trừ Conventions C1). Không có thì thay cả khối bằng "Không có" | Ví dụ: "Nhãn phần tử trên sơ đồ dùng tên tiếng Anh." ; "Cho phép vẽ UC đề xuất bổ sung với nhãn (đề xuất)." ; "Chỉ cần một sơ đồ tổng quát dù vượt ngưỡng, khổ giấy A3 ngang."}}
````

## 5. Ghi chú cho người dùng

- Sơ đồ rối, nhiều đường cắt: chạy lại với CACH_PHAN_RA_SO_DO khác, hoặc đề xuất tổng quát hoá tác nhân ở P01. Có thể mở file .drawio và dùng Arrange > Layout của draw.io để tinh chỉnh, nhưng sau đó cập nhật lại toạ độ trong bảng Node để hai dạng không lệch nhau.
- Kết quả có quá nhiều include, extend: thường do P02 giữ quá nhiều UC Subfunction. Rà lại P02 theo Q4, hoặc chạy P02R.
- Người review yêu cầu vẽ mũi tên trên đường nối tác nhân - use case: đặt KIEU_DUONG_ASSOCIATION = MUI_TEN_KHOI_XUONG; khi đó đuôi ở bên khởi xướng, đầu mũi tên mở ở bên nhận (tác nhân chính --> use case; use case --> tác nhân phụ). Cả hai kiểu đều hợp lệ trong UML; quan trọng là thống nhất trong mọi sơ đồ.
- Nếu note điều kiện extend không bám vào đường khi mở bằng draw.io, kéo note lại gần đường; nội dung điều kiện vẫn đúng trong bảng quan hệ.
- Dùng độc lập: đính kèm danh sách tác nhân và danh sách use case (có tác nhân chính, phụ) viết theo cột của P01, P02; phần truy vết REQ có thể thay bằng trích dẫn nguồn.

## 6. Căn cứ

- OMG, Unified Modeling Language 2.5.1, chương 18 Use Cases (Include, Extend, ExtensionPoint, condition, Generalization, subject, ràng buộc association của Actor), Annex về ký hiệu.
- Scott W. Ambler, The Elements of UML 2.0 Style, và UML Use Case Diagram Guidelines (agilemodeling.com): tác nhân chính góc trên trái, tác nhân bên ngoài sơ đồ, xếp use case theo trình tự thời gian, include bên phải, extend bên dưới, kế thừa bên dưới, tránh quá hai tầng quan hệ, dùng quan hệ tiết kiệm, không dùng «uses», tác nhân không tương tác với nhau.
- Alistair Cockburn, Writing Effective Use Cases (hạn chế include và extend, điều kiện mở rộng).
- Kurt Bittner, Ian Spence, Use Case Modeling (cấu trúc mô hình, tránh phân rã chức năng bằng include).
- Craig Larman, Applying UML and Patterns, 3rd ed. (quan hệ giữa use case, sơ đồ use case là mục lục của mô hình).
- Susan Lilly, Use Case Pitfalls: Top 10 Problems from Real Projects Using Use Cases, TOOLS 30, 1999 (quan hệ tác nhân - use case kiểu mạng nhện).
- Karl Wiegers, Joy Beatty, Software Requirements, 3rd ed. (lạm dụng include và extend).
