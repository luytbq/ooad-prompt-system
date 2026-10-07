# P02R - Review use case - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02R |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.0 |
| Phạm vi | TAC_NHAN, DANH_SACH_UC (toàn hệ thống); không chấm SO_DO vì P03 chưa chạy |

## Mục 1. Tóm tắt

Đối tượng đã review: danh sách tác nhân P01-actors.md 1.0 (10 tác nhân ACT-01 đến ACT-10) và danh sách use case P02-usecases.md 1.0 (18 use case UC-001 đến UC-018), dạng Markdown theo 00-Conventions.md. Phạm vi: TAC_NHAN, DANH_SACH_UC. Có tài liệu nguồn (yeu-cau-xe-khach.md) và P00-problem-brief.md 1.0 với 68 yêu cầu REQ-01 đến REQ-68.

Số phát hiện theo mức độ: Nghiêm trọng 0 / Trung bình 1 / Thấp 3.

Kết luận: Đạt.

Điểm làm tốt:

- Áp dụng U-R10 nhất quán và có lý do: UC-004 Nhận đặt chỗ qua điện thoại và UC-005 Bán vé tại quầy tách khỏi UC-002 Đặt vé trực tuyến vì kết quả hoặc đoạn tương tác khác, còn UC-007 Đổi vé và UC-008 Trả vé gộp hai tác nhân chính vì cùng mục tiêu và cùng quy tắc.
- Phân biệt đúng hết giờ chờ trong phiên và tác vụ theo lịch: hết 10 phút giữ chỗ là luồng thay thế của UC-002 (CAND-24, U-R07), còn huỷ đặt chỗ qua điện thoại khi đến 60 phút trước giờ xuất bến là UC-006 của ACT-10 Bộ định thời.
- Không tự thêm chức năng nguồn không nêu: cập nhật danh mục tuyến, xe, tài xế (CAND-47 đến CAND-49) chờ Q-03 và hoàn tiền mặt khi huỷ chuyến (CAND-43) chờ Q-14, thay vì thành use case.

Tác nhân đã xét theo nhóm tiêu chí A và không có phát hiện, giữ nguyên: ACT-01 Hành khách, ACT-02 Nhân viên bán vé, ACT-03 Nhân viên điều hành, ACT-04 Quản lý nhà xe, ACT-05 Phụ xe, ACT-06 Cổng thanh toán, ACT-07 Cổng SMS, ACT-08 Máy in vé, ACT-09 Đầu quét mã vạch (điều kiện ở Mục 6), ACT-10 Bộ định thời.

## Mục 2. Bảng kiểm kê

Không có (đối tượng đã có mã ACT-nn và UC-nnn theo Conventions, cột Phần tử dùng mã gốc).

## Mục 3. Bảng phát hiện

| Mã | Phần tử | Vấn đề | Quy tắc vi phạm | Mức độ (Nghiêm trọng / Trung bình / Thấp) | Đề xuất sửa |
|---|---|---|---|---|---|
| UCR-01 | UC-007 Đổi vé; UC-003 Thanh toán vé trực tuyến | UC-003 được giữ làm Subfunction để gói phần thanh toán qua ACT-06 Cổng thanh toán ("Hành khách thanh toán các chỗ đang giữ qua cổng thanh toán trực tuyến của đối tác", P02 Bảng 4b). UC-007 theo ASM-10 cũng thu phần chênh lệch của vé mua trực tuyến qua cổng thanh toán, nhưng nối thẳng ACT-06 làm tác nhân phụ (P02 Bảng 4a) và coi việc trả chênh lệch là bước riêng (CAND-38). Cùng một hành vi thanh toán qua cổng được mô tả ở hai nơi, P04 sẽ viết hai lần đoạn tương tác với cổng thanh toán, P03 sẽ vẽ hai cách nối khác nhau tới ACT-06. Lỗi con: mục tiêu UC-003 gắn cứng vào "các chỗ đang giữ" nên không dùng lại được. | U-T11, U-AP12 | Trung bình | Sửa mục tiêu UC-003 thành "Hành khách có khoản thanh toán trực tuyến được cổng thanh toán xác nhận" (thời hạn giữ chỗ 10 phút để lại ở UC-002); tác nhân chính UC-003 ghi "ACT-01 (qua UC-002, UC-007)"; thêm REQ-40 vào cột REQ của UC-003. Nhánh trả chênh lệch của vé mua trực tuyến trong UC-007 dùng UC-003; cột tác nhân phụ của UC-007 đổi từ "ACT-06" thành "-". Nếu Q-28 được trả lời (b) (mọi chênh lệch trả tại quầy): bỏ ACT-06 khỏi UC-007 và giữ UC-003 như bản gốc. |
| UCR-02 | UC-006 Huỷ vé đặt qua điện thoại quá hạn | Cùng một đối tượng được gọi bằng hai thuật ngữ. UC-004 gọi là "đặt chỗ" với kết quả "chỗ được giữ trên chuyến ... chờ khách thanh toán" (P02 Bảng 4b), tên tiếng Anh của chính UC-006 là "Cancel Overdue Phone Reservation", nhưng tên tiếng Việt và mục tiêu UC-006 dùng "vé đặt qua điện thoại". Theo ASM-05 đây là chỗ được giữ chưa thanh toán, chưa phải vé đã phát hành (REQ-17, REQ-18), nên chữ "vé" dễ làm bước sau coi là vé có trạng thái chưa thanh toán. Nguồn dùng lẫn hai cách gọi (P00 mục 5 dòng 5), nhưng tên use case cần một thuật ngữ. | U-N4 | Thấp | Đổi tên tiếng Việt UC-006 thành "Huỷ đặt chỗ qua điện thoại quá hạn", giữ tên tiếng Anh "Cancel Overdue Phone Reservation"; trong mục tiêu UC-006 thay "vé đặt qua điện thoại" bằng "đặt chỗ qua điện thoại". |
| UCR-03 | UC-012 Lập lịch chạy tuần | Tên "Lập lịch chạy tuần" (Create Weekly Schedule) và mục tiêu "có lịch chạy của tuần gồm các chuyến đã xếp" mô tả kết quả của cả tuần, trong khi ASM-11 cho mỗi lần thực hiện chỉ thêm một hoặc nhiều chuyến (khoảng 560 chuyến mỗi tuần, khó xong trong một phiên). Kết quả một lần thực hiện vì vậy không khớp tên, P04 dễ viết hậu điều kiện "lịch tuần đã lập xong". Không xếp vào U-AP05 vì theo ASM-11 mỗi phiên vẫn kết thúc nhất quán; lệch chỉ ở tên và mục tiêu. | U-N3, U-N6 | Thấp | Đổi tên thành "Xếp chuyến vào lịch chạy tuần" (Schedule Weekly Trips); sửa mục tiêu thành "Các chuyến xếp trong lần làm việc có tuyến, giờ xuất bến, xe và tài xế, được ghi vào lịch chạy của tuần và không vi phạm quy tắc chồng chuyến và giờ lái". Nếu Q-29 được trả lời "Một lần": giữ tên và mục tiêu gốc. |
| UCR-04 | UC-014 Chuẩn bị danh sách soát vé | Tên đưa ra thuật ngữ "danh sách soát vé" không có trong nguồn. Nguồn, P00 (REQ-61) và chính mục tiêu, mô tả của UC-014 đều gọi là "danh sách hành khách của chuyến" ("hệ thống gửi danh sách hành khách của chuyến về máy soát vé", Mục 8, câu 4). Hai tên cho cùng một dữ liệu sẽ sinh hai mục trong glossary. | U-N4 | Thấp | Đổi tên thành "Chuẩn bị danh sách hành khách của chuyến" (Prepare Trip Passenger List). |

## Mục 4. Danh sách use case đề xuất sau sửa

| UC | Tên (VI) | Tên (EN) | Tác nhân chính | Tác nhân phụ | Mục tiêu (kết quả có giá trị) | Thay đổi | Mã phát hiện |
|---|---|---|---|---|---|---|---|
| UC-001 | Tra cứu chuyến xe | Search Trips | ACT-01 Hành khách | - | Hành khách biết các chuyến khớp điểm đi, điểm đến, ngày đi và các chỗ còn trống của chuyến đã chọn. | Giữ | - |
| UC-002 | Đặt vé trực tuyến | Book Ticket Online | ACT-01 | ACT-07 Cổng SMS | Hành khách có vé đã phát hành cho các chỗ đã chọn, mỗi chỗ một mã vé, và người đi nhận được vé qua SMS. | Giữ | - |
| UC-003 | Thanh toán vé trực tuyến | Pay Ticket Online | ACT-01 (qua UC-002, UC-007) | ACT-06 Cổng thanh toán | Hành khách có khoản thanh toán trực tuyến được cổng thanh toán xác nhận. | Đổi mục tiêu và tác nhân chính (dùng chung cho UC-002, UC-007) | UCR-01 |
| UC-004 | Nhận đặt chỗ qua điện thoại | Take Phone Reservation | ACT-02 Nhân viên bán vé | - | Nhân viên bán vé có chỗ được giữ trên chuyến cho khách gọi điện, chờ khách thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến. | Giữ | - |
| UC-005 | Bán vé tại quầy | Sell Ticket At Counter | ACT-02 | ACT-08 Máy in vé | Vé đã được thanh toán tại quầy và in thành vé giấy có mã vạch cho khách. | Giữ | - |
| UC-006 | Huỷ đặt chỗ qua điện thoại quá hạn | Cancel Overdue Phone Reservation | ACT-10 Bộ định thời | - | Chỗ của đặt chỗ qua điện thoại chưa thanh toán trở lại còn trống để bán cho khách khác khi đến 60 phút trước giờ xuất bến. | Đổi tên | UCR-02 |
| UC-007 | Đổi vé | Exchange Ticket | ACT-01, ACT-02 | - (ACT-06 qua UC-003) | Khách có vé trên chuyến khác cùng tuyến thay cho vé cũ, đã trả phần chênh lệch nếu vé mới đắt hơn. | Đổi tác nhân phụ | UCR-01 |
| UC-008 | Trả vé | Return Ticket | ACT-01, ACT-02 | ACT-06 | Khách đã trả vé và nhận lại 90% hoặc 50% giá vé tuỳ thời điểm trả. | Giữ | - |
| UC-009 | Đăng ký tài khoản | Register Account | ACT-01 | - | Hành khách có tài khoản gắn với số điện thoại để xem lại lịch sử vé. | Giữ | - |
| UC-010 | Đăng nhập | Log In | ACT-01 | - | Hành khách được nhận diện là chủ tài khoản để dùng các chức năng cần tài khoản. | Giữ | - |
| UC-011 | Xem lịch sử vé | View Ticket History | ACT-01 | - | Hành khách thấy lại các vé đã mua gắn với tài khoản của mình. | Giữ | - |
| UC-012 | Xếp chuyến vào lịch chạy tuần | Schedule Weekly Trips | ACT-03 Nhân viên điều hành | - | Các chuyến xếp trong lần làm việc có tuyến, giờ xuất bến, xe và tài xế, được ghi vào lịch chạy của tuần và không vi phạm quy tắc chồng chuyến và giờ lái. | Đổi tên | UCR-03 |
| UC-013 | Huỷ chuyến | Cancel Trip | ACT-03 | ACT-06, ACT-07 | Chuyến đã huỷ, mọi hành khách đã có vé được báo qua SMS và được hoàn 100% giá vé. | Giữ | - |
| UC-014 | Chuẩn bị danh sách hành khách của chuyến | Prepare Trip Passenger List | ACT-10 | - | Máy soát vé của chuyến có danh sách hành khách để phụ xe soát vé, kể cả khi mất sóng. | Đổi tên | UCR-04 |
| UC-015 | Soát vé lên xe | Check Boarding Ticket | ACT-05 Phụ xe | ACT-09 Đầu quét mã vạch | Phụ xe biết từng vé hành khách xuất trình là hợp lệ hay không hợp lệ, và kết quả soát được ghi nhận. | Giữ | - |
| UC-016 | Đặt giá vé | Set Ticket Fare | ACT-04 Quản lý nhà xe | - | Quản lý nhà xe có giá vé áp dụng cho từng tuyến và loại xe. | Giữ | - |
| UC-017 | Đặt mức tăng giá lễ Tết | Set Holiday Price Increase | ACT-04 | - | Quản lý nhà xe có mức tăng giá theo phần trăm, tối đa 30%, áp dụng cho một khoảng ngày lễ, Tết. | Giữ | - |
| UC-018 | Xem báo cáo kinh doanh | View Business Reports | ACT-04 | - | Quản lý nhà xe nắm được doanh thu theo ngày, theo tuyến và tỉ lệ lấp đầy chỗ của từng chuyến. | Giữ | - |

Tổng sau sửa: 18 use case (16 User-goal, 2 Subfunction), không thêm, không loại.

## Mục 5. Quan hệ đề xuất sau sửa

Không có (phạm vi không gồm SO_DO).

## Mục 6. Giới hạn của review

- Không chấm sơ đồ: nhóm tiêu chí D và L không kiểm vì P03 chưa chạy. Quan hệ «include» từ UC-002 và UC-007 tới UC-003 nêu ở UCR-01 cần được P03 vẽ và review lại với phạm vi SO_DO.
- ACT-09 Đầu quét mã vạch được giữ theo A-C và U-R18 (thiết bị ngoài ranh giới, có giao tiếp riêng với ứng dụng soát vé), dựa trên ASM-06. Nếu Q-01 hoặc Q-04 cho thấy đầu quét chỉ là bộ phận nhập liệu tích hợp của máy cầm tay, không có giao tiếp riêng, thì theo A-T3 nó là kênh nhập, không phải tác nhân, và UC-015 không có tác nhân phụ.
- UC-014 được giữ theo U-R07 (tác vụ theo lịch có giá trị cho phụ xe), dù theo ASM-01 việc gửi danh sách là trao đổi giữa hai phần nội bộ của hệ thống. Kết luận này phụ thuộc Q-01.
- Câu hỏi cần người viết trả lời: Q-30 (cách giao vé mới khi đổi vé). Câu trả lời quyết định UC-007 có thêm tác nhân phụ ACT-07 hoặc ACT-08 hay không, và luồng của ACT-02 có thêm đoạn in vé giấy (hai bước trở lên) đủ để tách theo U-R10 a như cách đã tách UC-005 khỏi UC-002.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-30 | Khi đổi vé, vé mới được giao cho khách thế nào? (a) Theo kênh mua: vé mua trực tuyến gửi mã vé mới qua SMS, vé mua tại quầy in vé giấy mới có mã vạch tại quầy; (b) Giữ mã vé cũ, chỉ đổi chuyến, không giao vé mới | UC-007 (tác nhân phụ ACT-07, ACT-08; quyết định gộp theo U-R10 b hay tách theo U-R10 a); P04 UC-007 | Mục 5, câu 4: "Mỗi vé chỉ được đổi sang chuyến khác cùng tuyến một lần ... và trả thêm phần chênh lệch nếu vé mới đắt hơn"; Mục 3, câu 3 và Mục 4, câu 1 nêu cách giao vé theo kênh mua nhưng không nhắc tới vé đổi |

## Giả định

Không có

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-003, UC-007 | UCR-01 | Chạy lại P02 kèm file này, ghi UCR-01 vào YEU_CAU_BO_SUNG nếu chọn áp dụng |
| P02 | UC-006 | UCR-02 | Chạy lại P02 kèm file này, ghi UCR-02 vào YEU_CAU_BO_SUNG nếu chọn áp dụng |
| P02 | UC-012 | UCR-03 | Chạy lại P02 kèm file này, ghi UCR-03 vào YEU_CAU_BO_SUNG nếu chọn áp dụng; phụ thuộc Q-29 |
| P02 | UC-014 | UCR-04 | Chạy lại P02 kèm file này, ghi UCR-04 vào YEU_CAU_BO_SUNG nếu chọn áp dụng |

## Vấn đề còn mở

- Chọn giữa hai quy tắc (C9): Phần C mục 2 của prompt chỉ lập Bảng kiểm kê khi đối tượng chưa có mã, còn Conventions C5 yêu cầu không xoá mục. Đã giữ tiêu đề Mục 2 và Mục 5 với nội dung "Không có" kèm lý do.
- Target 8 chỉ cho hai cách ghi nhận phần tử đã xét (có phát hiện hoặc giữ nguyên trong Mục 4), nhưng Mục 4 chỉ chứa use case. Đã liệt kê các tác nhân đã xét không có phát hiện ở cuối Mục 1.
- Cột Thay đổi ở Mục 4 chỉ cho Giữ / Đổi tên / Gộp / Tách / Mới / Loại; UCR-01 sửa mục tiêu và tác nhân của UC-003, sửa tác nhân phụ của UC-007 mà không đổi tên. Đã ghi "Đổi mục tiêu và tác nhân chính" và "Đổi tác nhân phụ", kèm mã phát hiện.
- Phần B không gán mức mặc định cho U-N3, U-N4, U-N6, U-T11. UCR-01 xếp Trung bình theo U-AP12 (trùng lặp); UCR-02 đến UCR-04 xếp Thấp theo nhóm "thuật ngữ chưa nhất quán nhẹ" và "đặt tên chưa chuẩn nhưng không gây hiểu sai".
