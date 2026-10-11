# P05 - Từ điển thuật ngữ - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P05 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-khach.md (tài liệu nguồn duy nhất); P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09); P01-actors.md (phiên bản 1.0, Q-39, ASM-11); P02-usecases.md (phiên bản 1.1, Q-42, ASM-16; Mục 4 và Mục 5); P04-uc-specs/UC-009-book-ticket-online.md (phiên bản 1.0, Q-45, ASM-24); P04-uc-specs/UC-017-cancel-trip.md (phiên bản 1.0, Q-50, ASM-33); P04-uc-specs/_BR-register.md (BR-01 đến BR-11). Chưa có bản P05 cũ. Placeholder NGUON_THUAT_NGU_CHUAN: Không có. YEU_CAU_BO_SUNG: chỉ có hai đặc tả P04 là UC-009 và UC-017, các use case khác trong P02 chưa được đặc tả. Mã Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra: Q-50, ASM-33; lần chạy này không cấp mã Q, ASM mới |
| Phạm vi | Toàn hệ thống; thuật ngữ lần này lấy từ hai đặc tả UC-009, UC-017 và sổ BR |
| Mã Q, ASM cuối đã cấp | Q-50, ASM-33 |

## 1. Giới thiệu

Từ điển này là nơi duy nhất định nghĩa các thuật ngữ nghiệp vụ của Hệ thống bán vé xe khách SaoViet Bus, và là nguồn đặt tên lớp, thuộc tính, bảng dữ liệu ở các bước sau. Phiên bản 1.0 phủ các thuật ngữ dùng trong hai đặc tả UC-009 Đặt vé trực tuyến, UC-017 Huỷ chuyến và sổ BR; thuật ngữ chỉ xuất hiện ở use case chưa có đặc tả P04 được bổ sung khi chạy lại. Mọi artifact dùng cột Thuật ngữ làm cách gọi chính thức; từ ở cột Từ đồng nghĩa không dùng không được dùng trong artifact mới, còn dạng rút gọn ghi ở cột Ghi chú thì được chấp nhận.

## 2. Thuật ngữ

| GL | Thuật ngữ | Tiếng Anh | Định nghĩa | Từ đồng nghĩa không dùng | Nguồn (REQ / UC) | Ghi chú |
|---|---|---|---|---|---|---|
| GL-01 | Chỗ | Seat | Vị trí ngồi hoặc nằm có mã riêng trên sơ đồ chỗ của một loại xe, được bán thành vé cho một chuyến xe. | Không có | REQ-06, REQ-07, REQ-19, REQ-75; UC-009; BR-02, BR-04 | Thành phần: mã chỗ (ví dụ A05). Số chỗ của loại xe: 40 với xe giường nằm, 29 với xe ghế ngồi (REQ-03). Không có hai vé cùng một chỗ trên một chuyến xe (BR-02); mỗi chỗ một mã vé (BR-04). Quan hệ: một Chỗ thuộc một Sơ đồ chỗ (GL-19); trạng thái của chỗ trên một chuyến xe xem Chỗ trống (GL-02) và Giữ chỗ (GL-08) |
| GL-02 | Chỗ trống | Available Seat | Chỗ của một chuyến xe chưa có vé và chưa được giữ chỗ cho lần đặt vé nào. | Không có | REQ-06, REQ-07; UC-009; BR-02 | Chỉ chỗ trống mới chọn được để mua vé (UC-009 Dữ liệu vào 1, BR-02). Cách nói "chỗ còn trống" cùng nghĩa, được chấp nhận |
| GL-03 | Chuyến xe | Trip | Một lần xe khách chạy trên một tuyến xe vào một giờ xuất bến, do một xe và một tài xế đảm nhiệm, nằm trong lịch chạy. | Không có | REQ-02, REQ-47; UC-009, UC-017; BR-05, BR-09, BR-10 | Thành phần: tuyến xe, giờ xuất bến, xe, tài xế (REQ-47), phụ xe (ASM-07, chờ Q-06). Trạng thái: Chưa huỷ, Đã huỷ (UC-017 Dữ liệu ra 1; xem GL-04). Dạng rút gọn "chuyến" được chấp nhận. Nguồn dùng cả "chuyến" và "chuyến xe" ngang nhau; chọn dạng đầy đủ theo tên UC-008 Tra cứu chuyến xe. Chuyến xe dùng sơ đồ chỗ của loại xe (GL-19, GL-14) |
| GL-04 | Chuyến xe đã huỷ | Cancelled Trip | Chuyến xe đã được nhân viên điều hành ghi nhận huỷ và không còn chạy theo lịch chạy. | Không có | REQ-55, REQ-58; UC-017; BR-09, BR-11 | Lý do huỷ chuyến: Xe hỏng, Thời tiết (ASM-25, chờ Q-36). Chuyến xe đã huỷ không được huỷ lại (BR-09). Vé của chuyến xe đã huỷ được hoàn tiền (BR-07, BR-08). Cách nói "chuyến bị huỷ", "chuyến đã bị huỷ" cùng nghĩa, được chấp nhận |
| GL-05 | Giá vé | Fare | Số tiền phải trả cho một vé của một chuyến xe, xác định theo tuyến xe, loại xe của chuyến xe và mức tăng giá nếu có. | Không có | REQ-60, REQ-61; UC-009, UC-017 | Đơn vị: đồng. Giá vé đặt theo tuyến xe và loại xe (REQ-60); mức tăng giá xem Mức tăng giá (GL-16). Giá vé của từng vé được ghi lại khi bán và là căn cứ tính Số tiền hoàn (UC-017 mục 8). Giá vé tính theo ngày xuất bến hay ngày mua chờ Q-24 |
| GL-06 | Giao dịch thanh toán | Payment Transaction | Lần thu tiền vé từ hành khách qua Cổng thanh toán, có mã do Cổng thanh toán cấp và kết quả thành công hoặc không thành công. | Không có | REQ-15, REQ-16, REQ-76; UC-009, UC-017; BR-06 | Kết quả: Thành công, Không thành công. Một giao dịch có thể thu tiền nhiều vé (ASM-32). Giao dịch thành công đến sau Thời hạn giữ chỗ (GL-21) xử lý theo BR-06 (ASM-22, chờ Q-19). Hệ thống không lưu thông tin thẻ (REQ-76) |
| GL-07 | Giờ xuất bến | Departure Time | Ngày giờ một chuyến xe rời bến để bắt đầu chạy theo lịch chạy. | Không có | REQ-47; UC-009, UC-017; BR-05, BR-10 | Mốc để xét ngừng bán vé trực tuyến (BR-05) và để xét huỷ chuyến (BR-10). Các mốc 60 phút (REQ-31, chưa có BR) và 15 phút (REQ-70, chưa có BR) trước giờ xuất bến thuộc UC-007, UC-025 chưa đặc tả |
| GL-08 | Giữ chỗ | Seat Hold | Việc hệ thống dành các chỗ đã chọn của một chuyến xe cho một lần đặt vé trong một thời hạn, không cho lần đặt khác chọn các chỗ đó. | Giữ tạm | REQ-13, REQ-17; UC-009; BR-03 | Thời gian giữ chỗ (GL-20) và thời hạn giữ chỗ (GL-21) theo BR-03; việc giữ chỗ bắt đầu ở bước 5 của UC-009 (ASM-18, chờ Q-18). Cách nói "chỗ đang giữ", "chỗ bị giữ" chỉ chỗ đang trong giữ chỗ, được chấp nhận. Vé đặt qua điện thoại cũng được giữ chỗ đến hạn thanh toán (REQ-31, chưa có BR) |
| GL-09 | Hành khách | Passenger | Người sử dụng dịch vụ vận chuyển của nhà xe bằng cách mua vé xe khách hoặc đi xe theo một vé. | người truy cập | REQ-04; UC-009; ACT-01; BR-01 | Là tên tác nhân ACT-01 khi thao tác trên website, có hoặc không có tài khoản. Hành khách mua tại quầy hoặc đặt qua điện thoại không thao tác trên hệ thống (P01 mục 3). Người đi trên vé xem Người đi (GL-17). Dạng rút gọn "khách" được chấp nhận. Cách gọi "người truy cập" (Mục 10) chỉ người vào website nói chung, P01 đã gộp vào ACT-01 |
| GL-10 | Hoàn tiền | Refund | Việc trả lại cho hành khách một phần hoặc toàn bộ số tiền vé đã thu. | Không có | REQ-40, REQ-57; UC-017; BR-06, BR-07, BR-08 | Trạng thái hoàn tiền của vé đã thanh toán: Chưa hoàn, Đã hoàn (ASM-29, chờ Q-48). Kênh hoàn theo Kênh mua vé (GL-11) của vé (BR-08). Số tiền xem Số tiền hoàn (GL-18). Hoàn một phần số tiền của một giao dịch chờ Q-20 (ASM-32) |
| GL-11 | Kênh mua vé | Purchase Channel | Cách thức hành khách mua và thanh toán một vé, là trực tuyến qua website hoặc tại quầy bán vé. | Không có | REQ-40, REQ-41, REQ-59; UC-017; BR-08 | Giá trị: Trực tuyến (thanh toán qua Cổng thanh toán), Tại quầy (nhân viên bán vé thu tiền mặt). Vé đặt qua điện thoại thuộc kênh Tại quầy khi đã thanh toán tại quầy (UC-017 mục 8). Kênh mua vé quyết định kênh hoàn tiền (BR-08) |
| GL-12 | Lần đặt vé | Booking | Nhóm các chỗ của một chuyến xe mà hành khách chọn mua vé cùng một lúc, được giữ chỗ và thanh toán chung. | Không có | REQ-08, REQ-09; UC-009; BR-01 | Số chỗ tối đa theo BR-01 (luồng bán tại quầy chờ Q-12). Một người đi chung cho cả lần đặt (ASM-19, chờ Q-11). Tổng tiền của lần đặt bằng tổng Giá vé của các vé. Dạng rút gọn "lần đặt" được chấp nhận |
| GL-13 | Lịch chạy | Schedule | Danh sách các chuyến xe của một tuần, mỗi chuyến xe có tuyến xe, giờ xuất bến, xe và tài xế, do nhân viên điều hành lập. | Không có | REQ-46, REQ-47; UC-017 | Lập theo tuần (REQ-46). Mỗi chuyến xe có thêm phụ xe theo ASM-07 (chờ Q-06). Dạng "lịch chạy tuần" (tên UC-016) được chấp nhận |
| GL-14 | Loại xe | Vehicle Type | Phân loại xe theo kiểu bố trí chỗ và số chỗ, mỗi loại xe có một sơ đồ chỗ riêng. | Không có | REQ-03, REQ-49, REQ-60; UC-017 | Giá trị: Xe giường nằm 40 chỗ, Xe ghế ngồi 29 chỗ (REQ-03). Giá vé đặt theo loại xe (REQ-60) |
| GL-15 | Mã vé | Ticket Code | Chuỗi ký tự định danh duy nhất một vé, được gửi cho người đi và được quét khi hành khách lên xe. | Không có | REQ-19, REQ-20, REQ-63; UC-009, UC-017; BR-04 | Mỗi chỗ một mã vé (BR-04). Ví dụ: SV0001. Gửi qua SMS tới số điện thoại người đi (REQ-20) |
| GL-16 | Mức tăng giá | Holiday Surcharge | Tỉ lệ phần trăm cộng thêm vào giá vé cho một khoảng ngày lễ, Tết, do quản lý nhà xe đặt. | Không có | REQ-61, REQ-62; UC-009 | Đơn vị: phần trăm. Mức tối đa theo REQ-62 (chưa có BR). Chỉ ngày lễ, Tết hay bất kỳ khoảng ngày chờ Q-23; áp dụng theo ngày xuất bến hay ngày mua vé chờ Q-24 |
| GL-17 | Người đi | Traveler | Hành khách có họ tên và số điện thoại ghi cho một vé, là người sẽ ngồi hoặc nằm tại chỗ của vé trên chuyến xe. | Không có | REQ-09, REQ-20; UC-009, UC-017; BR-11 | Thành phần: họ tên, số điện thoại nhận mã vé qua SMS (REQ-09); điều kiện hợp lệ chờ Q-44. Một lần đặt vé có một người đi chung (ASM-19, chờ Q-11). Cách nói "hành khách đã có vé", "hành khách của chuyến" (REQ-56, REQ-69, BR-11) chỉ người đi của các vé (ASM-30), được chấp nhận |
| GL-18 | Số tiền hoàn | Refund Amount | Số tiền trả lại cho hành khách ứng với một vé trong một lần hoàn tiền. | Không có | REQ-58; UC-017; BR-07 | Đơn vị: đồng. Chuyến xe đã huỷ: bằng 100% Giá vé của vé đó (BR-07). Trả vé: 90% hoặc 50% giá vé tuỳ thời điểm trả (REQ-37, REQ-38, REQ-39, chưa có BR) |
| GL-19 | Sơ đồ chỗ | Seat Map | Bản bố trí các chỗ của một loại xe, nêu mã và vị trí của từng chỗ. | Không có | REQ-06, REQ-49; UC-009 | Mỗi loại xe có một sơ đồ chỗ. Chỗ trống của một chuyến xe xác định trên sơ đồ chỗ của loại xe (REQ-06). Nhân viên điều hành quản lý sơ đồ chỗ theo ASM-06 (chờ Q-02) |
| GL-20 | Thời gian giữ chỗ | Hold Duration | Khoảng thời gian tính bằng phút mà các chỗ của một lần đặt vé được giữ chỗ để hành khách thanh toán. | Không có | REQ-14; UC-009; BR-03 | Đơn vị: phút. Giá trị theo BR-03. Mốc bắt đầu tính là lúc giữ chỗ (ASM-18, chờ Q-18). Khác Thời hạn giữ chỗ (GL-21), là một thời điểm |
| GL-21 | Thời hạn giữ chỗ | Hold Expiry | Thời điểm việc giữ chỗ hết hiệu lực, bằng thời điểm bắt đầu giữ chỗ cộng thời gian giữ chỗ. | Không có | REQ-17; UC-009; BR-03, BR-06 | Ví dụ: giữ chỗ lúc 20:00 thì thời hạn giữ chỗ là 20:10 (UC-009 mục 8). Hết thời hạn mà chưa thanh toán thành công thì chỗ được trả lại (BR-03). Giao dịch thanh toán thành công đến sau thời hạn xử lý theo BR-06 |
| GL-22 | Tuyến xe | Route | Hành trình cố định giữa một điểm đi và một điểm đến mà nhà xe khai thác, có nhiều chuyến xe chạy theo hành trình đó. | Không có | REQ-01, REQ-47, REQ-60; UC-009, UC-017 | Thành phần: điểm đi, điểm đến; điểm đi, điểm đến là bến xe hay tỉnh, thành chờ Q-10. Nhà xe có 12 tuyến xe xuất phát từ 3 bến xe (REQ-01). Dạng rút gọn "tuyến" được chấp nhận. Nguồn dùng cả "tuyến" và "tuyến xe" ngang nhau; chọn dạng đầy đủ theo tên UC-020 Quản lý danh mục tuyến xe |
| GL-23 | Vé | Ticket | Chứng từ ghi nhận quyền của một người đi được ngồi hoặc nằm tại một chỗ trên một chuyến xe, có mã vé riêng. | Không có | REQ-18, REQ-19; UC-009, UC-017; BR-02, BR-04 | Thành phần: chuyến xe, chỗ, người đi, mã vé, giá vé, kênh mua vé, trạng thái hoàn tiền (ASM-29). Vé mua trực tuyến được phát hành khi thanh toán thành công (REQ-18). Trạng thái nêu trong các artifact: Đã huỷ (GL-24); đã trả, đã đổi (ASM-29; UC-012, UC-014 chưa đặc tả). Phân loại theo kênh mua vé: GL-26, GL-27, GL-28 |
| GL-24 | Vé đã huỷ | Cancelled Ticket | Vé bị hệ thống chấm dứt hiệu lực do chuyến xe của vé đã huỷ hoặc do vé đặt qua điện thoại quá hạn thanh toán. | Không có | REQ-32, REQ-55, REQ-66; UC-017 | Trạng thái vé: Đã huỷ. Vé của chuyến xe đã huỷ chuyển sang Đã huỷ ngay, không chờ hoàn tiền xong (ASM-29, chờ Q-48). Vé đặt qua điện thoại quá hạn thanh toán tự huỷ theo REQ-32 (chưa có BR, UC-007 chưa đặc tả). Vé đã huỷ là vé không hợp lệ khi soát vé (REQ-66, chưa có BR, chờ Q-28). Cách nói "vé bị huỷ" cùng nghĩa, được chấp nhận |
| GL-25 | Vé đang có hiệu lực | Active Ticket | Vé không phải vé đã huỷ, chưa được trả và chưa được đổi sang chuyến xe khác. | Không có | REQ-56; UC-017 | Định nghĩa theo UC-017 mục 8 (ASM-29). Chỉ vé đang có hiệu lực của chuyến xe đã huỷ được chuyển sang Đã huỷ và được báo qua SMS (BR-11, ASM-30). Trả vé, đổi vé: REQ-33, REQ-34 (UC-012, UC-014 chưa đặc tả) |
| GL-26 | Vé đặt qua điện thoại | Phone Reserved Ticket | Vé do nhân viên bán vé ghi nhận khi nhận đặt chỗ của khách qua điện thoại, có chỗ được giữ chỗ cho đến khi khách thanh toán tại quầy. | Không có | REQ-28, REQ-30, REQ-31, REQ-32; UC-017 | Hạn thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến, quá hạn thì tự huỷ (REQ-31, REQ-32, chưa có BR). Vé chưa thanh toán chưa có khoản tiền đã thu nên không có hoàn tiền (UC-017 mục 8). Sau khi thanh toán tại quầy, vé là Vé mua tại quầy (GL-27) |
| GL-27 | Vé mua tại quầy | Counter Ticket | Vé có kênh mua vé là tại quầy, gồm vé bán trực tiếp cho khách tại quầy và vé đặt qua điện thoại đã thanh toán tại quầy. | Không có | REQ-22, REQ-30, REQ-41; UC-017; BR-08 | Hoàn tiền mặt tại quầy (BR-08). Phân loại theo UC-017 mục 8. Dạng rút gọn "vé quầy" được chấp nhận |
| GL-28 | Vé mua trực tuyến | Online Ticket | Vé có kênh mua vé là trực tuyến, được phát hành cho hành khách sau khi thanh toán thành công qua Cổng thanh toán. | Không có | REQ-18, REQ-40; UC-009, UC-017; BR-08 | Hoàn tiền qua Cổng thanh toán (BR-08). Mã vé gửi qua SMS tới số điện thoại người đi (REQ-20). Dạng rút gọn "vé trực tuyến" được chấp nhận |

## 3. Ứng viên không đưa vào

| Ứng viên | Lý do không đưa vào | Nơi xuất hiện |
|---|---|---|
| Họ tên người đi, Số điện thoại người đi (Số điện thoại nhận) | Thuộc tính lẻ, ghi trong Ghi chú của GL-17 Người đi | UC-009 Dữ liệu vào 2, Dữ liệu ra 2; UC-017 Dữ liệu ra 2 |
| Mã chỗ | Thuộc tính lẻ, ghi trong Ghi chú của GL-01 Chỗ | UC-009 Dữ liệu vào 1 |
| Điểm đi, Điểm đến | Thuộc tính lẻ, ghi trong Ghi chú của GL-22 Tuyến xe (nghĩa chờ Q-10) | UC-009 mục 2 bước 2 |
| Lý do huỷ chuyến | Thuộc tính lẻ, ghi trong Ghi chú của GL-04 Chuyến xe đã huỷ | UC-017 Dữ liệu vào 1 |
| Trạng thái hoàn tiền (Chưa hoàn, Đã hoàn) | Tập giá trị ghi trong Ghi chú của GL-10 Hoàn tiền | UC-017 mục 1, mục 8 |
| Tổng tiền | Từ phổ thông dùng đúng nghĩa thông thường (tổng cộng các Giá vé) | UC-009 Dữ liệu ra 1 |
| Chỗ đang giữ, Chỗ bị giữ | Đồng nghĩa của GL-08 Giữ chỗ (chỗ đang trong giữ chỗ) | UC-009 mục 2, mục 3; BR-03 |
| Chỗ còn trống | Đồng nghĩa của GL-02 Chỗ trống | REQ-06; UC-009 mục 3 |
| Giữ tạm | Đồng nghĩa của GL-08 Giữ chỗ | UC-009 mục 2 bước 5, node A-5 |
| Cổng thanh toán, Cổng SMS | Tên tác nhân ACT-06, ACT-07, đã định nghĩa ở P01, không có vai trò gần giống cần phân biệt | UC-009, UC-017 |
| Nhân viên điều hành, Quản lý nhà xe, Phụ xe, Nhân viên bán vé | Tên tác nhân ACT-03, ACT-04, ACT-05, ACT-02, đã định nghĩa ở P01, không có vai trò gần giống cần phân biệt | UC-017, GL-13, GL-16 |
| Xe, Tài xế | Từ phổ thông dùng đúng nghĩa thông thường | UC-017 Dữ liệu ra 1; REQ-47 |
| SMS | Từ phổ thông dùng đúng nghĩa thông thường (tin nhắn qua mạng viễn thông) | UC-009, UC-017 |
| Website | Từ giao diện, kỹ thuật | REQ-04; UC-009 mục 1 |
| Xác thực, phiên làm việc | Thuật ngữ kỹ thuật phần mềm | UC-017 Tiền điều kiện |
| Danh sách hành khách, Gửi danh sách hành khách cho phụ xe | Tên use case UC-025 (đã định nghĩa ở P02) | UC-009 mục 8; UC-017 mục 2, mục 8 |
| Bến xe | Chưa đưa vào lần chạy này: chỉ xuất hiện ở use case chưa có đặc tả P04 (UC-019, UC-020); xét lại khi chạy lại | REQ-01; P02 UC-019 |
| Trả vé, Đổi vé | Chưa đưa vào lần chạy này: chỉ xuất hiện ở use case chưa có đặc tả P04 (UC-012, UC-014, UC-015); xét lại khi chạy lại | REQ-33, REQ-34; UC-009 mục 8 |
| Soát vé, Máy soát vé cầm tay | Chưa đưa vào lần chạy này: chỉ xuất hiện ở use case chưa có đặc tả P04 (UC-026); xét lại khi chạy lại | REQ-63, REQ-64; UC-009 mục 8; UC-017 mục 8 |
| Tài khoản, Mã xác thực | Chưa đưa vào lần chạy này: nghĩa riêng (đăng ký bằng số điện thoại, đăng nhập bằng mã SMS) chỉ xuất hiện ở use case chưa có đặc tả P04 (UC-001, UC-003); xét lại khi chạy lại | REQ-10, REQ-12 |

## Câu hỏi mở

Không có

## Giả định

Không có

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-009 (Mục 2 bước 5; Mục 9 node A-5) | Dùng "Giữ tạm" cho Giữ chỗ (GL-08), trong khi BR-03, luồng 5a và Mục 8 của cùng đặc tả dùng "giữ chỗ" | Đổi "Giữ tạm các chỗ đã chọn" thành "Giữ chỗ cho các chỗ đã chọn" ở bước 5 và ở nhãn node A-5 (bảng Node, bảng đối chiếu và file P04-activity-UC-009.drawio giữ đồng bộ) |

## Vấn đề còn mở

- Phạm vi thuật ngữ: bước 2 của prompt yêu cầu đọc P00, P02 và P04, còn YEU_CAU_BO_SUNG cho biết chỉ có hai đặc tả P04. Theo C9 (yêu cầu bổ sung ưu tiên hơn quy tắc của bước), phiên bản 1.0 chỉ đưa vào thuật ngữ xuất hiện trong UC-009, UC-017 và sổ BR; các ứng viên chỉ xuất hiện ở use case chưa đặc tả được ghi ở mục 3 với lý do "Chưa đưa vào lần chạy này". F5 không liệt kê lý do này; dùng lý do riêng vì không có lý do nào trong F5 phù hợp.
- Thứ tự chữ cái: prompt không nêu cách xếp chữ tiếng Việt có dấu. Bảng xếp theo bảng chữ cái tiếng Việt (a, ă, â, ..., o, ô, ơ, ..., u, ư), bỏ qua dấu thanh khi so sánh, ký tự trắng đứng trước chữ cái.
- Tên chính thức "Chuyến xe", "Tuyến xe": F4 mục 3 (cách gọi nhiều nhất trong nguồn) nghiêng về "chuyến", "tuyến", còn mục 5 (tên use case đã chốt) nghiêng về dạng đầy đủ. Chọn dạng đầy đủ làm chính thức và chấp nhận dạng rút gọn, để không phát sinh đề xuất sửa artifact trước cho các cách gọi đang dùng lẫn nhau.
- GL-09 Hành khách: nguồn dùng "hành khách" cho cả người mua vé ("hành khách nhập họ tên và số điện thoại của người đi", Mục 2) lẫn người đi theo vé ("hành khách đã có vé", Mục 6). Chọn định nghĩa bao quát cả hai, tách Người đi (GL-17) là hành khách ghi trên vé, nên không cần đề xuất sửa các chỗ dùng "hành khách đã có vé", "danh sách hành khách" ở P00, P01, P02, P04.
- Tên tiếng Anh viết dạng Title Case có dấu cách (ví dụ "Phone Reserved Ticket") theo ví dụ của F3; hồ sơ dự án quy định PascalCase cho tên lớp, bước thiết kế sau chuyển dạng.
- Các mục Target còn lại đạt.
