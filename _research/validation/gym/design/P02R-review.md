# P02R - Review danh sách tác nhân và use case - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02R |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md (phiên bản 1.0); P01-actors.md (phiên bản 1.0); P02-usecases.md (phiên bản 1.0); yeu-cau-phong-tap.md. QUY_UOC_DA_CHOT, YEU_CAU_BO_SUNG: Không có |
| Phạm vi | TAC_NHAN, DANH_SACH_UC (toàn hệ thống) |
| Mã Q, ASM cuối đã cấp | Q-49 (không cấp Q mới); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Tóm tắt

- Đối tượng đã review: danh sách tác nhân dạng bảng (P01-actors.md, Mục 2, 14 tác nhân) và danh sách use case dạng bảng (P02-usecases.md phiên bản 1.0, Mục 4, 28 use case). Phạm vi: TAC_NHAN, DANH_SACH_UC. Có tài liệu nguồn: yeu-cau-phong-tap.md và P00-problem-brief.md. Các mục khác của P01 và P02 (ranh giới, ứng viên, sự kiện, ma trận truy vết) chỉ dùng để đối chiếu, không chấm riêng.
- Số phát hiện: Nghiêm trọng 0 / Trung bình 0 / Thấp 3.
- Kết luận: Đạt (không có phát hiện Nghiêm trọng, không quá 3 phát hiện Trung bình).
- Điểm làm tốt:
  - UC-005 Mua gói tập hợp nhất việc mua của hội viên với việc bán tại quầy của lễ tân theo đúng điều kiện loại trừ của U-R10 b, kênh thu tiền khác nhau được xử lý là luồng thay thế (U-R12), đồng thời ghi rõ điều kiện xét lại khi Q-01 được trả lời.
  - UC-018 Vào chi nhánh chọn tác nhân chính là người quét mã (ACT-02, ACT-03) và ACT-12 Cửa quay là tác nhân phụ, nhất quán với U-R18 và với P01; máy POS và ngân hàng được loại đúng lý do A-T2.
  - Các use case do tác nhân thời gian khởi xướng (UC-008, UC-013, UC-015, UC-016, UC-022) đều gắn với mốc hạn cụ thể của nguồn và ghi rõ chỗ phụ thuộc Q-43; ma trận REQ --> UC phủ đủ mọi REQ loại Chức năng và Giao tiếp ngoài.

## 2. Bảng kiểm kê

Đối tượng đã có mã gốc (ACT-nn, UC-nnn), không gán mã tạm.

| Mã tạm | Loại | Tên như trong bản gốc |
|---|---|---|
| Không có, dùng mã gốc | Tác nhân | ACT-01 Người quan tâm |
| Không có, dùng mã gốc | Tác nhân | ACT-02 Hội viên |
| Không có, dùng mã gốc | Tác nhân | ACT-03 Khách vãng lai |
| Không có, dùng mã gốc | Tác nhân | ACT-04 Huấn luyện viên |
| Không có, dùng mã gốc | Tác nhân | ACT-05 Lễ tân |
| Không có, dùng mã gốc | Tác nhân | ACT-06 Quản lý chi nhánh |
| Không có, dùng mã gốc | Tác nhân | ACT-07 Giám đốc chuỗi |
| Không có, dùng mã gốc | Tác nhân | ACT-08 Cổng thanh toán |
| Không có, dùng mã gốc | Tác nhân | ACT-09 Cổng SMS |
| Không có, dùng mã gốc | Tác nhân | ACT-10 Dịch vụ thông báo đẩy |
| Không có, dùng mã gốc | Tác nhân | ACT-11 Hệ thống hoá đơn điện tử |
| Không có, dùng mã gốc | Tác nhân | ACT-12 Cửa quay |
| Không có, dùng mã gốc | Tác nhân | ACT-13 Bộ định thời hằng ngày |
| Không có, dùng mã gốc | Tác nhân | ACT-14 Bộ định thời theo hạn |
| Không có, dùng mã gốc | Use case | UC-001 Xem giá gói tập |
| Không có, dùng mã gốc | Use case | UC-002 Xem lịch lớp nhóm |
| Không có, dùng mã gốc | Use case | UC-003 Đăng ký tài khoản hội viên |
| Không có, dùng mã gốc | Use case | UC-004 Đăng nhập |
| Không có, dùng mã gốc | Use case | UC-005 Mua gói tập |
| Không có, dùng mã gốc | Use case | UC-006 Bảo lưu gói tập |
| Không có, dùng mã gốc | Use case | UC-007 Chuyển nhượng gói tập |
| Không có, dùng mã gốc | Use case | UC-008 Nhắc gia hạn gói tập |
| Không có, dùng mã gốc | Use case | UC-009 Lập lịch lớp nhóm |
| Không có, dùng mã gốc | Use case | UC-010 Đặt chỗ lớp nhóm |
| Không có, dùng mã gốc | Use case | UC-011 Huỷ chỗ lớp nhóm |
| Không có, dùng mã gốc | Use case | UC-012 Nhận chỗ từ danh sách chờ |
| Không có, dùng mã gốc | Use case | UC-013 Chuyển chỗ cho người kế tiếp |
| Không có, dùng mã gốc | Use case | UC-014 Huỷ lớp nhóm vì sự cố |
| Không có, dùng mã gốc | Use case | UC-015 Huỷ lớp nhóm ít người đặt |
| Không có, dùng mã gốc | Use case | UC-016 Ghi nhận vắng mặt lớp nhóm |
| Không có, dùng mã gốc | Use case | UC-017 Bán vé tập một ngày |
| Không có, dùng mã gốc | Use case | UC-018 Vào chi nhánh |
| Không có, dùng mã gốc | Use case | UC-019 Mua gói buổi tập cá nhân |
| Không có, dùng mã gốc | Use case | UC-020 Đặt buổi tập cá nhân |
| Không có, dùng mã gốc | Use case | UC-021 Duyệt yêu cầu đặt buổi tập |
| Không có, dùng mã gốc | Use case | UC-022 Huỷ yêu cầu đặt buổi quá hạn |
| Không có, dùng mã gốc | Use case | UC-023 Huỷ buổi tập cá nhân |
| Không có, dùng mã gốc | Use case | UC-024 Ghi nhận buổi tập cá nhân |
| Không có, dùng mã gốc | Use case | UC-025 Xem chỉ số cơ thể |
| Không có, dùng mã gốc | Use case | UC-026 Đặt giá gói tập |
| Không có, dùng mã gốc | Use case | UC-027 Đặt chương trình khuyến mãi |
| Không có, dùng mã gốc | Use case | UC-028 Xem báo cáo chuỗi |

## 3. Bảng phát hiện

| Mã | Phần tử | Vấn đề | Quy tắc vi phạm | Mức độ | Đề xuất sửa |
|---|---|---|---|---|---|
| UCR-01 | UC-005 Mua gói tập | Tên không cho thấy use case phủ cả gia hạn. Nguồn nêu "Hội viên mua hoặc gia hạn gói tập trên ứng dụng" (Mục 2 câu 1) và P02 gộp gia hạn vào UC-005 (CAND-06, REQ-12, REQ-17), trong khi UC-008 Nhắc gia hạn gói tập dẫn người đọc tới một chức năng gia hạn mà danh sách không có tên nào nói tới. Người tra danh sách theo thuật ngữ nguồn sẽ không thấy gia hạn nằm ở đâu | U-N6, U-N4 | Thấp | Đổi tên UC-005 thành Mua hoặc gia hạn gói tập (EN: Purchase Or Renew Membership Package); giữ nguyên tác nhân, mục tiêu và REQ |
| UCR-02 | UC-011 Huỷ chỗ lớp nhóm; UC-015 Huỷ lớp nhóm ít người đặt; UC-021 Duyệt yêu cầu đặt buổi tập; UC-022 Huỷ yêu cầu đặt buổi quá hạn | Cột Mục tiêu (Bảng 4b) khẳng định kết quả mà nguồn không nêu, hoặc viết cho bên không phải tác nhân chính. UC-011: "chỗ được trả lại cho hội viên đứng đầu danh sách chờ", trong khi nguồn chỉ nêu hệ thống thông báo cho người đó và người đó có 30 phút để xác nhận (Mục 3 câu 4; Q-22 hỏi chỗ có được giữ riêng không). UC-015: "chỗ phòng được giải phóng", nguồn không nêu. UC-021: "Hội viên biết yêu cầu đặt buổi được xác nhận hay bị từ chối" viết cho hội viên, không phải huấn luyện viên là tác nhân chính, và chưa có căn cứ về cách hội viên được báo (Q-15 còn mở). UC-022: "hội viên không bị giữ khung giờ vô thời hạn", nguồn chỉ nêu "quá hạn thì yêu cầu tự huỷ" (Mục 7 câu 2). Cùng một gốc: mục tiêu viết thêm hệ quả suy diễn. Hạ từ Trung bình (mặc định U-T) xuống Thấp: không đổi danh sách use case, tác nhân hay REQ phủ, chỉ sửa câu mục tiêu | U-T5, U-T10 | Thấp | Viết lại Mục tiêu bám nguồn. UC-011: "Hội viên không còn giữ chỗ trong lớp đã huỷ; hội viên đứng đầu danh sách chờ (nếu có) được thông báo có chỗ trống". UC-015: "Những hội viên đã đặt chỗ lớp có dưới 3 người biết lớp đã bị huỷ". UC-021: "Yêu cầu đặt buổi tập cá nhân được huấn luyện viên xác nhận hoặc từ chối". UC-022: "Yêu cầu đặt buổi chưa được huấn luyện viên xác nhận hoặc từ chối trong 12 giờ bị huỷ" |
| UCR-03 | UC-021 Duyệt yêu cầu đặt buổi tập | Thuật ngữ không nhất quán với nguồn và với chính P02. Nguồn dùng "xác nhận hoặc từ chối" (Mục 7 câu 2) và CAND-43 đặt tên "Xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân"; tên trong Bảng 4a đổi sang "Duyệt" mà không ghi lý do, trong khi Q-43 và UC-015, UC-022 dùng "duyệt" với nghĩa khác (bước nhân viên duyệt hoặc gỡ hành động hệ thống tự thực hiện) | U-N4 | Thấp | Đổi tên thành Phản hồi yêu cầu đặt buổi tập (EN: Respond To Training Session Request); giữ nguyên tác nhân chính ACT-04 và mức User-goal |

## 4. Danh sách use case đề xuất sau sửa

| UC | Tên (VI) | Tên (EN) | Tác nhân chính | Tác nhân phụ | Mục tiêu (kết quả có giá trị) | Thay đổi | Mã phát hiện |
|---|---|---|---|---|---|---|---|
| UC-001 | Xem giá gói tập | View Package Prices | ACT-01 | - | Người quan tâm biết được giá và quy cách các gói tập để quyết định có đăng ký hay không. | Giữ | - |
| UC-002 | Xem lịch lớp nhóm | View Class Schedule | ACT-01 | - | Người quan tâm biết được các lớp nhóm đang mở để quyết định có đăng ký hay không. | Giữ | - |
| UC-003 | Đăng ký tài khoản hội viên | Register Member Account | ACT-01 | - | Người quan tâm có tài khoản hội viên để mua gói và đặt lớp. | Giữ | - |
| UC-004 | Đăng nhập | Log In | ACT-02 | - | Hội viên được xác nhận danh tính để dùng các chức năng của tài khoản mình. | Giữ | - |
| UC-005 | Mua hoặc gia hạn gói tập | Purchase Or Renew Membership Package | ACT-02, ACT-05 | ACT-08, ACT-11 | Hội viên có gói tập đã thanh toán và được kích hoạt; khi mua tại quầy, khách có gói tập đã thu tiền. | Đổi tên | UCR-01 |
| UC-006 | Bảo lưu gói tập | Freeze Membership Package | ACT-02 | - | Hội viên có gói được tạm dừng trong thời gian đã đăng ký và ngày hết hạn lùi tương ứng. | Giữ | - |
| UC-007 | Chuyển nhượng gói tập | Transfer Membership Package | ACT-05 | ACT-11 | Người nhận có gói tập chuyển nhượng và VietFit thu phí chuyển nhượng. | Giữ | - |
| UC-008 | Nhắc gia hạn gói tập | Remind Package Renewal | ACT-13 | ACT-09, ACT-10 | Hội viên có gói hết hạn trong 7 ngày tới nhận được lời nhắc gia hạn. | Giữ | - |
| UC-009 | Lập lịch lớp nhóm | Schedule Group Classes | ACT-06 | - | Quản lý chi nhánh có lịch lớp nhóm của tuần đã xếp đủ loại lớp, phòng, huấn luyện viên và giờ, không trùng. | Giữ | - |
| UC-010 | Đặt chỗ lớp nhóm | Book Class Spot | ACT-02 | - | Hội viên có chỗ trong lớp nhóm mong muốn, hoặc có vị trí trong danh sách chờ khi lớp đã đủ chỗ. | Giữ | - |
| UC-011 | Huỷ chỗ lớp nhóm | Cancel Class Booking | ACT-02 | ACT-09, ACT-10 | Hội viên không còn giữ chỗ trong lớp đã huỷ; hội viên đứng đầu danh sách chờ (nếu có) được thông báo có chỗ trống. | Sửa mục tiêu | UCR-02 |
| UC-012 | Nhận chỗ từ danh sách chờ | Claim Waitlist Spot | ACT-02 | - | Hội viên đứng đầu danh sách chờ có chỗ trong lớp vốn đã đủ chỗ. | Giữ | - |
| UC-013 | Chuyển chỗ cho người kế tiếp | Pass Spot To Next Person | ACT-14 | - | Hội viên kế tiếp trong danh sách chờ có cơ hội nhận chỗ khi hội viên trước không xác nhận kịp. | Giữ | - |
| UC-014 | Huỷ lớp nhóm vì sự cố | Cancel Class Due To Incident | ACT-06 | ACT-09, ACT-10 | Mọi người đã đặt chỗ và người trong danh sách chờ của lớp bị huỷ biết lớp đã huỷ. | Giữ | - |
| UC-015 | Huỷ lớp nhóm ít người đặt | Cancel Under-Booked Class | ACT-14 | ACT-09, ACT-10 | Những hội viên đã đặt chỗ lớp có dưới 3 người biết lớp đã bị huỷ. | Sửa mục tiêu | UCR-02 |
| UC-016 | Ghi nhận vắng mặt lớp nhóm | Record Class Absence | ACT-14 | - | Hội viên đặt chỗ mà không vào lớp bị tính vắng mặt, và bị khoá quyền đặt lớp khi đạt ngưỡng. | Giữ | - |
| UC-017 | Bán vé tập một ngày | Sell Day Pass | ACT-05 | ACT-11 | Khách vãng lai có vé tập một ngày có mã QR dùng được trong ngày tại chi nhánh đã mua. | Giữ | - |
| UC-018 | Vào chi nhánh | Enter Branch | ACT-02, ACT-03 | ACT-12 | Hội viên hoặc khách vãng lai hợp lệ đi qua cửa quay vào chi nhánh. | Giữ | - |
| UC-019 | Mua gói buổi tập cá nhân | Purchase Personal Training Package | ACT-02 | ACT-11 | Hội viên có gói buổi tập cá nhân với một huấn luyện viên. | Giữ | - |
| UC-020 | Đặt buổi tập cá nhân | Book Personal Training Session | ACT-02 | - | Hội viên có yêu cầu đặt buổi tập cá nhân vào khung giờ đã chọn, chờ huấn luyện viên phản hồi. | Giữ | - |
| UC-021 | Phản hồi yêu cầu đặt buổi tập | Respond To Training Session Request | ACT-04 | - | Yêu cầu đặt buổi tập cá nhân được huấn luyện viên xác nhận hoặc từ chối. | Đổi tên, Sửa mục tiêu | UCR-02, UCR-03 |
| UC-022 | Huỷ yêu cầu đặt buổi quá hạn | Cancel Expired Session Request | ACT-14 | - | Yêu cầu đặt buổi chưa được huấn luyện viên xác nhận hoặc từ chối trong 12 giờ bị huỷ. | Sửa mục tiêu | UCR-02 |
| UC-023 | Huỷ buổi tập cá nhân | Cancel Personal Training Session | ACT-02 | - | Hội viên huỷ được buổi tập đã đặt và không bị trừ buổi khi huỷ sớm. | Giữ | - |
| UC-024 | Ghi nhận buổi tập cá nhân | Record Training Session | ACT-04 | - | Buổi tập cá nhân và chỉ số cơ thể của hội viên được ghi nhận. | Giữ | - |
| UC-025 | Xem chỉ số cơ thể | View Body Metrics | ACT-02, ACT-04 | - | Hội viên và huấn luyện viên phụ trách xem được chỉ số cơ thể, không ai khác xem được. | Giữ | - |
| UC-026 | Đặt giá gói tập | Set Package Prices | ACT-07 | - | Giám đốc chuỗi có giá các gói được áp dụng trong chuỗi. | Giữ | - |
| UC-027 | Đặt chương trình khuyến mãi | Set Promotion | ACT-07 | - | Giám đốc chuỗi có chương trình khuyến mãi áp dụng trong khoảng ngày đã chọn. | Giữ | - |
| UC-028 | Xem báo cáo chuỗi | View Chain Reports | ACT-07 | - | Giám đốc chuỗi nắm được doanh thu, mức lấp đầy lớp nhóm và số buổi tập cá nhân của từng huấn luyện viên. | Giữ | - |

## 4b. Danh sách tác nhân sau sửa

Không có phát hiện nào về tác nhân; toàn bộ 14 tác nhân được giữ nguyên.

| ACT | Tên | Loại | Tính chất | Thay đổi | Mã phát hiện |
|---|---|---|---|---|---|
| ACT-01 | Người quan tâm | Người | Chính | Giữ | - |
| ACT-02 | Hội viên | Người | Chính | Giữ | - |
| ACT-03 | Khách vãng lai | Người | Chính | Giữ | - |
| ACT-04 | Huấn luyện viên | Người | Chính | Giữ | - |
| ACT-05 | Lễ tân | Người | Chính | Giữ | - |
| ACT-06 | Quản lý chi nhánh | Người | Chính | Giữ | - |
| ACT-07 | Giám đốc chuỗi | Người | Chính | Giữ | - |
| ACT-08 | Cổng thanh toán | Hệ thống ngoài | Phụ | Giữ | - |
| ACT-09 | Cổng SMS | Hệ thống ngoài | Phụ | Giữ | - |
| ACT-10 | Dịch vụ thông báo đẩy | Hệ thống ngoài | Phụ | Giữ | - |
| ACT-11 | Hệ thống hoá đơn điện tử | Hệ thống ngoài | Phụ | Giữ | - |
| ACT-12 | Cửa quay | Thiết bị | Phụ | Giữ | - |
| ACT-13 | Bộ định thời hằng ngày | Thời gian | Chính | Giữ | - |
| ACT-14 | Bộ định thời theo hạn | Thời gian | Chính | Giữ | - |

## 5. Quan hệ đề xuất sau sửa

Không áp dụng (phạm vi review không gồm SO_DO).

## 6. Giới hạn của review

- Không có phần nào của đối tượng không đọc được.
- Các tiêu chí cần nguồn (A-T6, U-T10, U-AP13, U-AP14, U-R16) đã kiểm được vì có tài liệu nguồn và P00. Kết quả: không có tác nhân hoặc use case thừa; mọi REQ loại Chức năng và Giao tiếp ngoài đều có use case phủ.
- U-T4 (size test, luồng chính khoảng 3-15 bước) không kiểm được trực tiếp vì chưa có luồng chính (P04). Với các use case do tác nhân thời gian khởi xướng (UC-013, UC-015, UC-016, UC-022), review dựa trên mô tả ngắn ở Bảng 4b và không kết luận use case quá nhỏ.
- Việc coi hạn 30 phút của danh sách chờ (UC-013) và hạn 12 giờ của huấn luyện viên (UC-022) là use case của tác nhân thời gian, không phải luồng thay thế, được giữ theo U-T6 và U-R13 (lúc hết hạn không còn phiên nào của tác nhân chính đang mở). Đây là lựa chọn mà P02 đã nêu ở mục Vấn đề còn mở; review không coi là lỗi và không cấp Q mới.
- Nhóm tiêu chí D và L (sơ đồ) không chấm vì phạm vi không gồm SO_DO.
- Câu hỏi cần người viết trả lời: Không có.

## Câu hỏi mở

Không có (review không cấp Q-nn mới; các Q-01 đến Q-49 đã có ở P00, P01, P02).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P02 | UC-005, UC-011, UC-015, UC-021, UC-022 | Ba phát hiện mức Thấp UCR-01, UCR-02, UCR-03 (tên và mục tiêu), nội dung chi tiết ở Mục 3 | Nếu áp dụng ít nhất một UCR: chạy lại P02 kèm P02R-review.md, ghi mã UCR áp dụng trong YEU_CAU_BO_SUNG. Không áp dụng: ghi mã và lý do vào Vấn đề còn mở của P02, hoặc vào YEU_CAU_BO_SUNG của P03 |
| P01 | Tất cả tác nhân | Không có phát hiện | Không có |

## Vấn đề còn mở

Không có mục Target nào ở trạng thái Không đạt. Các điểm cần người dùng lưu ý:

- Review không đánh giá lại các Q còn chờ trả lời (Q-01 đến Q-06, Q-11, Q-15, Q-43, Q-45, Q-47); kết quả Đạt chỉ đúng với danh sách hiện tại và phải rà lại khi các Q này được trả lời (có thể thêm use case quản lý danh mục, tài khoản, lịch làm việc huấn luyện viên và tác nhân thời gian theo tuần).
- Mọi phát hiện đều mức Thấp nên không bắt buộc chạy lại P02 trước P03.
