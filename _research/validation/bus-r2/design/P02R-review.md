# P02R - Review use case - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02R |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09); P01-actors.md (phiên bản 1.0, Q-39, ASM-11); P02-usecases.md (phiên bản 1.0, Q-40, ASM-14); yeu-cau-xe-khach.md. Placeholder QUY_UOC_DA_CHOT, YEU_CAU_BO_SUNG: Không có. Mã Q, ASM cấp tiếp từ Q-40, ASM-14 |
| Phạm vi | TAC_NHAN, DANH_SACH_UC. Toàn hệ thống |
| Mã Q, ASM cuối đã cấp | Q-42, ASM-16 |

## 1. Tóm tắt

- Đối tượng review: P01-actors.md (9 tác nhân ACT-01 đến ACT-09) và P02-usecases.md (28 use case UC-001 đến UC-028), dạng Markdown, đã có mã theo Conventions. Phạm vi: TAC_NHAN, DANH_SACH_UC; không chấm sơ đồ (nhóm D, L). Có tài liệu nguồn: yeu-cau-xe-khach.md và P00-problem-brief.md.
- Số phát hiện: Nghiêm trọng 0 / Trung bình 2 / Thấp 2.
- Kết luận: Đạt.
- Điểm làm tốt:
  - UC-010 Thanh toán vé trực tuyến giữ ở mức Subfunction đúng theo Q4 d (kết quả riêng, cổng thanh toán là tác nhân phụ, thanh toán lại được theo ASM-12) và ghi tác nhân chính kèm "(qua UC-009, UC-014)".
  - Hết 10 phút giữ chỗ được xử lý là luồng thay thế của UC-009 (CAND-41), không thành use case riêng hay tác nhân thời gian; hai tác vụ theo lịch UC-007 và UC-025 đúng U-R07 với tác nhân chính ACT-09.
  - Cách chọn tác nhân qua thiết bị nhất quán: Phụ xe là tác nhân chính của UC-026, máy soát vé không là tác nhân (ASM-10), Máy in vé ACT-08 là tác nhân phụ ở cả UC-004, UC-006, UC-015.

## 2. Bảng kiểm kê

Đối tượng đã có mã theo Conventions nên mọi phần tử dùng mã gốc.

| Mã tạm | Loại | Tên như trong bản gốc |
|---|---|---|
| Không có, dùng mã gốc | Tác nhân | ACT-01 Hành khách |
| Không có, dùng mã gốc | Tác nhân | ACT-02 Nhân viên bán vé |
| Không có, dùng mã gốc | Tác nhân | ACT-03 Nhân viên điều hành |
| Không có, dùng mã gốc | Tác nhân | ACT-04 Quản lý nhà xe |
| Không có, dùng mã gốc | Tác nhân | ACT-05 Phụ xe |
| Không có, dùng mã gốc | Tác nhân | ACT-06 Cổng thanh toán |
| Không có, dùng mã gốc | Tác nhân | ACT-07 Cổng SMS |
| Không có, dùng mã gốc | Tác nhân | ACT-08 Máy in vé |
| Không có, dùng mã gốc | Tác nhân | ACT-09 Bộ định thời |
| Không có, dùng mã gốc | Use case | UC-001 Đăng ký tài khoản |
| Không có, dùng mã gốc | Use case | UC-002 Quản lý tài khoản nhân viên |
| Không có, dùng mã gốc | Use case | UC-003 Đăng nhập |
| Không có, dùng mã gốc | Use case | UC-004 Bán vé tại quầy |
| Không có, dùng mã gốc | Use case | UC-005 Nhận đặt chỗ qua điện thoại |
| Không có, dùng mã gốc | Use case | UC-006 Thu tiền vé đặt qua điện thoại |
| Không có, dùng mã gốc | Use case | UC-007 Huỷ vé đặt chỗ quá hạn |
| Không có, dùng mã gốc | Use case | UC-008 Tra cứu chuyến xe |
| Không có, dùng mã gốc | Use case | UC-009 Đặt vé trực tuyến |
| Không có, dùng mã gốc | Use case | UC-010 Thanh toán vé trực tuyến |
| Không có, dùng mã gốc | Use case | UC-011 Xem lịch sử vé |
| Không có, dùng mã gốc | Use case | UC-012 Trả vé trực tuyến |
| Không có, dùng mã gốc | Use case | UC-013 Trả vé tại quầy |
| Không có, dùng mã gốc | Use case | UC-014 Đổi vé trực tuyến |
| Không có, dùng mã gốc | Use case | UC-015 Đổi vé tại quầy |
| Không có, dùng mã gốc | Use case | UC-016 Lập lịch chạy tuần |
| Không có, dùng mã gốc | Use case | UC-017 Huỷ chuyến |
| Không có, dùng mã gốc | Use case | UC-018 Hoàn tiền mặt chuyến bị huỷ |
| Không có, dùng mã gốc | Use case | UC-019 Quản lý danh mục bến xe |
| Không có, dùng mã gốc | Use case | UC-020 Quản lý danh mục tuyến xe |
| Không có, dùng mã gốc | Use case | UC-021 Quản lý danh mục xe |
| Không có, dùng mã gốc | Use case | UC-022 Quản lý danh mục tài xế |
| Không có, dùng mã gốc | Use case | UC-023 Đặt giá vé |
| Không có, dùng mã gốc | Use case | UC-024 Đặt mức tăng giá ngày lễ |
| Không có, dùng mã gốc | Use case | UC-025 Gửi danh sách hành khách cho phụ xe |
| Không có, dùng mã gốc | Use case | UC-026 Soát vé hành khách lên xe |
| Không có, dùng mã gốc | Use case | UC-027 Xem báo cáo doanh thu |
| Không có, dùng mã gốc | Use case | UC-028 Xem báo cáo tỉ lệ lấp đầy |

## 3. Bảng phát hiện

| Mã | Phần tử | Vấn đề | Quy tắc vi phạm | Mức độ | Đề xuất sửa |
|---|---|---|---|---|---|
| UCR-01 | UC-008 Tra cứu chuyến xe | Mô tả UC-008 (Bảng 4b) nói đây là "phần đầu của các UC đặt, bán, đổi vé (ứng viên include ở P03 cho UC-009, UC-004, UC-005, UC-014, UC-015)", và ASM-03 giao việc chọn chuyến và chỗ ở UC-004, UC-005 cho ACT-02 Nhân viên bán vé, và UC-015 cũng do ACT-02 thực hiện. Nhưng Bảng 4a ghi tác nhân chính của UC-008 chỉ là ACT-01, và P02 Mục 1 không có mục tiêu tìm chuyến nào của ACT-02. Hệ quả: khi P03 include UC-008 vào UC-004, UC-005, UC-015, người thao tác thật (ACT-02) không có đường tới UC-008, hoặc UC-008 bị include bởi use case có tác nhân chính khác. | U-T8, U-T11 | Trung bình | Sửa cột Tác nhân chính của UC-008 thành "ACT-01 Hành khách; ACT-02 Nhân viên bán vé (qua UC-004, UC-005, UC-015)", cùng cách ghi "(qua ...)" đã dùng ở UC-010. Giữ UC-008 là User-goal vì nguồn nêu tìm chuyến không cần tài khoản (Mục 1, câu 3) |
| UCR-02 | UC-012 Trả vé trực tuyến; UC-013 Trả vé tại quầy | Hai use case cùng mục tiêu (trả vé, nhận hoàn theo mức 90%, 50%, 0% của REQ-37, REQ-38, REQ-39) và cùng quy tắc. Khác nhau ở người thao tác (ACT-01 tự làm; ACT-02 làm thay theo ASM-04) và kênh hoàn (cổng thanh toán theo REQ-40; tiền mặt tại quầy theo REQ-41). P02 tách vì "có tác nhân phụ khác (cổng thanh toán)", "đoạn xác thực quyền trả vé của hành khách không có tài khoản (Q-37)", "tra vé của khách, trao tiền mặt" (CAND-06, CAND-11). Theo U-R10 nhánh a, tách chỉ khi luồng của người đại diện có đoạn tương tác riêng từ 2 bước mà luồng người được đại diện không có, hoặc kết quả khác nhau: tác nhân phụ khác không phải điều kiện của a; đoạn xác thực Q-37 thuộc luồng hành khách, không thuộc người đại diện; "tra vé" và "trao tiền mặt" mỗi cái một bước và đều có bước tương ứng ở luồng trực tuyến (chọn vé, nhận hoàn qua cổng); kết quả giống nhau (vé đã trả, hoàn đủ mức). Phần khác biệt còn lại chỉ là kênh hoàn tiền, thuộc nhánh b và là biến thể của cùng một luồng | U-R10, U-R12, U-AP15 | Trung bình | Gộp UC-013 vào UC-012, đổi tên thành "Trả vé" (Return Ticket), tác nhân chính ACT-01 (vé mua trực tuyến) và ACT-02 (vé mua tại quầy), tác nhân phụ ACT-06 (chỉ ở nhánh hoàn qua cổng thanh toán); hoàn tiền mặt tại quầy là luồng thay thế. UC-013 chuyển trạng thái Loại, giữ mã. Khi Q-41 được trả lời "Có, ghi rõ đoạn đó" thì giữ hai use case và bỏ phát hiện này |
| UCR-03 | UC-004, UC-005, UC-006, UC-010, UC-015 | Cột REQ ở Bảng 4b lệch với Ma trận truy vết Mục 5. Mục 5 gán REQ-07 và REQ-09 cho UC-004, UC-005; REQ-19 cho UC-004; REQ-26 cho UC-006, UC-015; nhưng cột REQ của các UC đó không có các REQ này. Ngược lại Bảng 4b UC-010 có REQ-17 trong khi Mục 5 chỉ gán REQ-17 cho UC-009. Mức hạ từ Trung bình xuống Thấp: không đổi tập use case, chỉ làm hai bảng truy vết không khớp nhau | U-T10 | Thấp | Chạy lại P02: thêm REQ-07, REQ-09, REQ-19 vào UC-004; REQ-07, REQ-09 vào UC-005; REQ-26 vào UC-006 và UC-015; ở Mục 5 thêm UC-010 vào dòng REQ-17 (hoặc bỏ REQ-17 khỏi cột REQ của UC-010) |
| UCR-04 | UC-014 Đổi vé trực tuyến | Nguồn nêu đổi sang "vé mới" (Mục 5, câu 4) và quy tắc "mỗi chỗ một mã vé, gửi qua SMS" khi phát hành vé trực tuyến (Mục 3, câu 3; REQ-19, REQ-20). UC-014 tạo vé mới nhưng cột Tác nhân phụ ghi "-", không nói mã vé mới đến tay hành khách bằng cách nào, trong khi UC-009 có ACT-07. Cần xác nhận với nguồn (Q-42). Mức Thấp vì chỉ ảnh hưởng cột tác nhân phụ và chưa có xác nhận từ nguồn | U-R06, U-R08, A-C4 | Thấp | Theo ASM-16: sửa Tác nhân phụ của UC-014 thành "ACT-07 Cổng SMS"; thêm REQ-20, REQ-21 vào cột REQ của UC-014. Khi Q-42 trả lời "Không, giữ mã vé cũ" thì bỏ phát hiện này |

## 4. Danh sách use case đề xuất sau sửa

| UC | Tên (VI) | Tên (EN) | Tác nhân chính | Tác nhân phụ | Mục tiêu (kết quả có giá trị) | Thay đổi | Mã phát hiện |
|---|---|---|---|---|---|---|---|
| UC-001 | Đăng ký tài khoản | Register Account | ACT-01 Hành khách | - | Hành khách có tài khoản gắn với số điện thoại để xem lại lịch sử vé | Giữ | - |
| UC-002 | Quản lý tài khoản nhân viên | Manage Staff Accounts | ACT-04 Quản lý nhà xe | - | Quản lý nhà xe có danh sách tài khoản nhân viên đúng với các vai trò đang làm việc | Giữ | - |
| UC-003 | Đăng nhập | Log In | ACT-01, ACT-02, ACT-03, ACT-04, ACT-05 | ACT-07 Cổng SMS | Người dùng vào được hệ thống với đúng vai trò của mình | Giữ | - |
| UC-004 | Bán vé tại quầy | Sell Ticket At Counter | ACT-02 Nhân viên bán vé | ACT-08 Máy in vé | Khách mua trực tiếp nhận vé giấy có mã vạch cho chỗ đã chọn sau khi trả tiền mặt | Giữ | UCR-03 (chỉ sửa cột REQ) |
| UC-005 | Nhận đặt chỗ qua điện thoại | Take Phone Reservation | ACT-02 | - | Khách gọi điện có chỗ được giữ đến hạn thanh toán tại quầy | Giữ | UCR-03 (chỉ sửa cột REQ) |
| UC-006 | Thu tiền vé đặt qua điện thoại | Collect Payment For Phone Reservation | ACT-02 | ACT-08 | Khách đã đặt chỗ qua điện thoại có vé đã thanh toán tại quầy | Giữ | UCR-03 (chỉ sửa cột REQ) |
| UC-007 | Huỷ vé đặt chỗ quá hạn | Cancel Overdue Reservation | ACT-09 Bộ định thời | - | Chỗ của vé đặt qua điện thoại quá hạn thanh toán được trả lại để người khác đặt | Giữ | - |
| UC-008 | Tra cứu chuyến xe | Search Trips | ACT-01; ACT-02 (qua UC-004, UC-005, UC-015) | - | Hành khách biết các chuyến phù hợp và các chỗ còn trống mà không cần tài khoản | Sửa tác nhân | UCR-01 |
| UC-009 | Đặt vé trực tuyến | Book Ticket Online | ACT-01 | ACT-07 | Hành khách có vé đã phát hành, mỗi chỗ một mã vé, và nhận mã vé qua SMS | Giữ | - |
| UC-010 | Thanh toán vé trực tuyến | Pay Ticket Online | ACT-01 (qua UC-009, UC-014) | ACT-06 Cổng thanh toán | Hành khách có khoản tiền vé đã được cổng thanh toán xác nhận | Giữ | UCR-03 (chỉ sửa cột REQ hoặc Mục 5) |
| UC-011 | Xem lịch sử vé | View Ticket History | ACT-01 | - | Hành khách có tài khoản xem được các vé đã đặt | Giữ | - |
| UC-012 | Trả vé | Return Ticket | ACT-01, ACT-02 | ACT-06 (nhánh hoàn qua cổng thanh toán) | Khách có vé đã trả và nhận lại tiền theo mức hoàn: qua cổng thanh toán với vé mua trực tuyến, bằng tiền mặt tại quầy với vé mua tại quầy | Đổi tên, Sửa tác nhân, Gộp từ UC-013 | UCR-02 |
| UC-013 | Trả vé tại quầy | Return Ticket At Counter | ACT-02 | - | Khách có vé mua tại quầy đã trả vé và nhận lại tiền mặt theo mức hoàn | Loại (gộp vào UC-012) | UCR-02 |
| UC-014 | Đổi vé trực tuyến | Exchange Ticket Online | ACT-01 | ACT-07 Cổng SMS | Hành khách có vé mới ở chuyến khác cùng tuyến thay cho vé cũ | Sửa tác nhân | UCR-04 |
| UC-015 | Đổi vé tại quầy | Exchange Ticket At Counter | ACT-02 | ACT-08 | Khách có vé mua tại quầy có vé mới ở chuyến khác cùng tuyến thay cho vé cũ | Giữ | UCR-03 (chỉ sửa cột REQ) |
| UC-016 | Lập lịch chạy tuần | Create Weekly Schedule | ACT-03 Nhân viên điều hành | - | Nhân viên điều hành có lịch chạy của tuần, mỗi chuyến đủ tuyến, giờ xuất bến, xe, tài xế, phụ xe, không vi phạm ràng buộc | Giữ | - |
| UC-017 | Huỷ chuyến | Cancel Trip | ACT-03 | ACT-06, ACT-07 | Chuyến bị huỷ, hành khách đã có vé được báo và vé trực tuyến được hoàn 100% giá vé | Giữ | - |
| UC-018 | Hoàn tiền mặt chuyến bị huỷ | Refund Cash For Cancelled Trip | ACT-02 | - | Khách có vé mua tại quầy của chuyến bị huỷ nhận lại 100% giá vé bằng tiền mặt | Giữ | - |
| UC-019 | Quản lý danh mục bến xe | Manage Station Catalog | ACT-03 | - | Danh mục bến xe đúng với các bến nhà xe đang khai thác | Giữ | - |
| UC-020 | Quản lý danh mục tuyến xe | Manage Route Catalog | ACT-03 | - | Danh mục tuyến xe đúng với các tuyến nhà xe đang khai thác | Giữ | - |
| UC-021 | Quản lý danh mục xe | Manage Vehicle Catalog | ACT-03 | - | Danh mục xe đúng với đội xe, mỗi xe có loại xe, số chỗ và sơ đồ chỗ | Giữ | - |
| UC-022 | Quản lý danh mục tài xế | Manage Driver Catalog | ACT-03 | - | Danh mục tài xế đúng với các tài xế nhà xe đang có | Giữ | - |
| UC-023 | Đặt giá vé | Set Ticket Fare | ACT-04 | - | Giá vé theo từng tuyến và loại xe do quản lý nhà xe đặt | Giữ | - |
| UC-024 | Đặt mức tăng giá ngày lễ | Set Holiday Surcharge | ACT-04 | - | Giá vé trong khoảng ngày lễ, Tết được tăng đúng mức quản lý đặt | Giữ | - |
| UC-025 | Gửi danh sách hành khách cho phụ xe | Send Passenger List To Attendant | ACT-09 | - | Phụ xe của chuyến có sẵn danh sách hành khách trên máy soát vé trước giờ xuất bến | Giữ | - |
| UC-026 | Soát vé hành khách lên xe | Check Ticket At Boarding | ACT-05 Phụ xe | - | Phụ xe biết mã vé quét được hợp lệ hay không và vé hợp lệ được ghi nhận đã soát | Giữ | - |
| UC-027 | Xem báo cáo doanh thu | View Revenue Report | ACT-04 | - | Quản lý nhà xe biết doanh thu theo ngày hoặc theo tuyến | Giữ | - |
| UC-028 | Xem báo cáo tỉ lệ lấp đầy | View Occupancy Report | ACT-04 | - | Quản lý nhà xe biết tỉ lệ lấp đầy chỗ của từng chuyến | Giữ | - |

Ghi chú: dòng "Giữ" có mã UCR-03 chỉ cần sửa cột REQ ở P02, không đổi tên, tác nhân, mục tiêu.

## 4b. Danh sách tác nhân sau sửa

| ACT | Tên | Loại | Tính chất | Thay đổi | Mã phát hiện |
|---|---|---|---|---|---|
| ACT-01 | Hành khách | Người | Chính | Giữ | - |
| ACT-02 | Nhân viên bán vé | Người | Chính | Giữ | - |
| ACT-03 | Nhân viên điều hành | Người | Chính | Giữ | - |
| ACT-04 | Quản lý nhà xe | Người | Chính | Giữ | - |
| ACT-05 | Phụ xe | Người | Chính | Giữ | - |
| ACT-06 | Cổng thanh toán | Hệ thống ngoài | Phụ | Giữ | - |
| ACT-07 | Cổng SMS | Hệ thống ngoài | Phụ | Giữ | - |
| ACT-08 | Máy in vé | Thiết bị | Phụ | Giữ | - |
| ACT-09 | Bộ định thời | Thời gian | Chính | Giữ | - |

## 5. Quan hệ đề xuất sau sửa

Không áp dụng: phạm vi review không có SO_DO.

## 6. Giới hạn của review

- Không có phần nào không đọc được.
- Tiêu chí nhóm D và L không chấm vì phạm vi không có SO_DO. Mọi ghi chú "ứng viên include ở P03" trong P02 chưa được kiểm.
- UC-014 và UC-015 không bị bắt lỗi U-R10 tách theo kênh vì ASM-14 cho UC-015 một đoạn riêng (thu chênh lệch tiền mặt, in vé giấy mới qua ACT-08). Kết luận này phụ thuộc Q-40: nếu Q-40 trả lời "Không in", đoạn riêng chỉ còn một bước và UC-014, UC-015 phải xét gộp như UCR-02.
- UC-025 được giữ theo U-R07. Nếu Q-38 trả lời máy soát vé có phần mềm riêng (máy là tác nhân hay hệ thống ngoài), tính chất của UC-025 và cách chọn tác nhân của UC-026 cần review lại.
- Câu hỏi cần người viết trả lời: Q-41 và Q-42 (ghi ở mục Câu hỏi mở).

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-41 | Khi nhân viên bán vé trả vé tại quầy cho vé mua tại quầy, luồng có đoạn tương tác riêng từ 2 bước trở lên mà luồng hành khách tự trả vé trực tuyến không có không? (Không có, chỉ khác kênh hoàn tiền / Có, ghi rõ đoạn đó) | UC-012, UC-013; UCR-02 | Mục 5, câu 1 và câu 3; ASM-04 |
| Q-42 | Khi đổi vé trực tuyến, hệ thống có phát hành vé mới với mã vé mới và gửi mã vé mới qua SMS cho người đi không? (Có, gửi SMS như khi đặt vé / Không, giữ mã vé cũ) | UC-014, tác nhân phụ ACT-07; UCR-04 | Mục 5, câu 4 ("vé mới"); Mục 3, câu 3 |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-15 | Luồng trả vé tại quầy chỉ khác luồng trả vé trực tuyến ở người thao tác và kênh hoàn tiền, không có đoạn tương tác riêng từ 2 bước trở lên; trả vé là một use case có hai tác nhân chính. | Chờ Q-41. Nguồn không mô tả luồng trả vé tại quầy ngoài việc hoàn tiền mặt tại quầy (Mục 5, câu 3); chọn phương án gộp theo U-R10 nhánh b | UC-012, UC-013; UCR-02 |
| ASM-16 | Đổi vé trực tuyến thành công phát hành vé mới có mã vé riêng, mã vé mới được gửi qua SMS tới số điện thoại người đi; Cổng SMS là tác nhân phụ của UC-014. | Chờ Q-42. Nguồn nêu "vé mới" khi đổi và việc gửi mã vé qua SMS khi phát hành vé trực tuyến nhưng không nói rõ cho trường hợp đổi vé | UC-014; ACT-07; REQ-19, REQ-20; UCR-04 |

## Đề xuất sửa artifact trước

Không có. Các đề nghị sửa P02 nằm ở Mục 3 theo mã UCR-01 đến UCR-04; P01 không cần sửa.

## Vấn đề còn mở

- Không có mục Target nào ở trạng thái Không đạt.
- Lựa chọn khi hai quy tắc xung đột: P02 tách UC-012 với UC-013 viện U-R12 và tác nhân phụ khác nhau, còn U-R10 nói hai nhánh a, b loại trừ nhau và tác nhân phụ không thuộc điều kiện của a. Review chọn theo U-R10 (UCR-02) vì U-R10 nêu điều kiện cụ thể hơn U-R12 và U-AP15 cùng chiều.
- Lựa chọn khi hai quy tắc xung đột: U-R04 và U-R05 đọc theo nghĩa đen có thể đòi gộp bốn danh mục UC-019 đến UC-022 (cùng tác nhân) và gộp UC-027 với UC-028 (cùng tác nhân, cùng cách xem). Review không bắt lỗi vì mỗi danh mục là một X khác nhau, và gộp báo cáo sẽ buộc tên có "và" (vi phạm U-N7) hoặc tên mơ hồ (U-N3). Người viết có thể xác nhận bằng QUY_UOC_DA_CHOT ở lần review sau.
- Lựa chọn khi hai quy tắc xung đột: tên UC-025 có 5 từ ghép (8 âm tiết); P02 đếm 7 từ và ghi vượt U-N7. Review không bắt lỗi vì U-N7 là "khoảng" và thuộc nhóm heuristic.
