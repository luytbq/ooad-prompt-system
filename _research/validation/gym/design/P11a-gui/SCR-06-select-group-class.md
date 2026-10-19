# P11a - SCR-06 Chọn lớp nhóm - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-010 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, BR-06 đến BR-12); P07-uc-analysis/UC-010 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); mục h) của SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14 (đều ghi Không có thông điệp mới). Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-104; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-105. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-010 và các màn hình điều hướng (SCR-01, SCR-02, SCR-06, SCR-07, SCR-08, SCR-09, SCR-10, SCR-15, SCR-16); đây là lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Có. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-06 (UC-010, ACT-02 Hội viên, ứng dụng di động) |
| Mã Q, ASM cuối đã cấp | Q-105; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-06 Chọn lớp nhóm (Select group class) |
| UC | UC-010 Đặt chỗ lớp nhóm |
| Bước UC | 1-3, 4a, 5a, 5b, 6a, 7a1, 7a2 (bước 1 là yêu cầu nhấn từ SCR-02; bước 2 hiển thị lịch lớp nhóm; bước 3 chọn lớp; bước 4 đến 7 do máy chủ kiểm tra và kết quả từ chối hoặc lớp đủ chỗ hiển thị bằng hộp thông điệp tại màn hình này; bước 8 do máy chủ lưu chỗ đã đặt trước khi mở SCR-07) |
| Tác nhân | ACT-02 Hội viên |
| Boundary AC | AC-B-BookClassSpotUI |
| DC | DC-BookClassSpotView (đi cùng DC-BookClassSpotStore) |
| Loại màn hình | Độc lập |
| Đến từ | SCR-02 (TR-07, mẫu 1) |
| Đi tới | SCR-07 (TR-08, mẫu 4, dữ liệu truyền Lớp nhóm đã chọn); SCR-08 (TR-09, mẫu 4, dữ liệu truyền Lớp nhóm đã chọn, qua nút Vào danh sách chờ của hộp MSG-09); SCR-02 (nút Trang chủ và nút quay lại của hệ thống, mẫu 1, ghi ở node START-ACT-02). Các hộp MSG-05 đến MSG-08 đóng rồi ở lại SCR-06 |

## c) Hình ảnh màn hình

Mockup HTML: mockups/SCR-06-select-group-class.html (ba trạng thái: đã chọn một lớp, lỗi MSG-01, hộp MSG-09).

Hình minh hoạ ở trạng thái đã chọn thẻ thứ nhất; lịch có thể dài hơn bốn thẻ và cuộn dọc. Khi mở màn hình lần đầu không có thẻ nào được chọn.

```text
+--------------------------------------+
| [VietFit]                [Trang chủ] |
|--------------------------------------|
|                                      |
| Chọn lớp nhóm                        |
| * Bắt buộc                           |
|                                      |
| Chọn lớp nhóm *                      |
| +----------------------------------+ |
| | Yoga                         (x) | |
| | 26/10/2026 18:00                 | |
| | Phòng 2                          | |
| | Huấn luyện viên Nguyễn Thị Lan   | |
| +----------------------------------+ |
| +----------------------------------+ |
| | Aerobic                      ( ) | |
| | 26/10/2026 19:15                 | |
| | Phòng 1                          | |
| | Huấn luyện viên Trần Văn Hùng    | |
| +----------------------------------+ |
| +----------------------------------+ |
| | Đạp xe trong nhà             ( ) | |
| | 27/10/2026 06:30                 | |
| | Phòng 3                          | |
| | Huấn luyện viên Lê Minh Châu     | |
| +----------------------------------+ |
| +----------------------------------+ |
| | Yoga                         ( ) | |
| | 27/10/2026 18:00                 | |
| | Phòng 2                          | |
| | Huấn luyện viên Nguyễn Thị Lan   | |
| +----------------------------------+ |
|                                      |
| [             Đặt chỗ              ] |
|                                      |
+--------------------------------------+
```

Trạng thái lỗi khi nhấn Đặt chỗ mà chưa chọn thẻ nào:

```text
 Chọn lớp nhóm *
  (!) Vui lòng chọn lớp nhóm.
 +----------------------------------+
 | Yoga                         ( ) |
 | ...                              |
```

Trạng thái hộp xác nhận MSG-09 (lớp Đạp xe trong nhà đã đủ chỗ; nền phủ đen 40%):

```text
+--------------------------------------+
| [VietFit]                [Trang chủ] |
|######################################|
|###+------------------------------+###|
|###| Xác nhận                     |###|
|###| Lớp Đạp xe trong nhà lúc     |###|
|###| 27/10/2026 06:30 đã đủ chỗ.  |###|
|###| Bạn có muốn vào danh sách    |###|
|###| chờ của lớp này không?       |###|
|###| [ Vào danh sách chờ ]        |###|
|###| [ Không vào ]                |###|
|###+------------------------------+###|
|######################################|
+--------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit, nút Trang chủ | Trên cùng, cao 56 dp; logo bên trái cách mép 16 dp, cao 28 dp; Trang chủ bên phải | UI-STT 10, 12, 45 |
| Dải thông báo | Không dùng ở màn hình này | - | Lỗi nhập hiện tại trường (UI-STT 58) |
| Tiêu đề màn hình | Chọn lớp nhóm | Đầu vùng nội dung, 20 sp Bold | UI-STT 13 |
| Nội dung | Dòng chú thích * Bắt buộc, nhãn nhóm Chọn lớp nhóm, các thẻ lớp nhóm | Cuộn dọc, lề trái phải 16 dp, thẻ cách nhau 8 dp, thẻ cao tối thiểu 72 dp | UI-STT 10, 31, 34 |
| Hành động | Nút chính Đặt chỗ | Cuối nội dung, rộng 328 dp ở 360 dp, cao 48 dp | UI-STT 14, 26. Không có nút phụ |
| Thông điệp | MSG-01 ngay dưới nhãn nhóm thẻ; hộp MSG-05 đến MSG-09, MSG-11, MSG-12 là lớp phủ giữa màn hình, rộng 312 dp; MSG-10 là chỉ báo xoay trong vùng nội dung | - | UI-STT 54, 56, 58 |

Dữ liệu mẫu: bốn lớp nhóm trong cùng tuần; lớp Yoga, Phòng 2, Nguyễn Thị Lan, 26/10/2026 18:00 lấy theo ví dụ Dữ liệu ra 1 của P04 (26/10/2026 là thứ Hai). Giờ học định dạng dd/MM/yyyy HH:mm (UI-STT 18). Loại lớp lấy từ ba giá trị nguồn nêu (yoga, aerobic, đạp xe trong nhà; GL-27). Tên phòng và tên huấn luyện viên là giá trị minh hoạ. Lớp Đạp xe trong nhà 27/10/2026 06:30 là lớp đã đủ chỗ trong hộp MSG-09 và là lớp ở SCR-08.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Nút Trang chủ | Nút | Nhấn | Rời màn hình, bỏ thẻ đã chọn, mở SCR-02 (mẫu 1). Chưa lưu chỗ đã đặt nào nên không có dữ liệu cần giữ | UI-STT 45; screen-transition.md node START-ACT-02 |
| 3 | Nút quay lại của hệ thống (Android) hoặc cử chỉ quay lại (iOS) | Nút | Nhấn | Khi không có hộp thông điệp: mở SCR-02 vì màn hình không có nút Quay lại. Khi có hộp thông điệp: đóng hộp theo dòng 8 đến 13 | UI-STT 15, 51 |
| 4 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Chọn lớp nhóm, sau đó dòng chú thích * Bắt buộc | UI-STT 13, 31 |
| 5 | Nhóm thẻ lớp nhóm | Nút chọn | Khởi tạo | Máy chủ trả lịch lớp nhóm; hiển thị mỗi lớp một thẻ gồm loại lớp, giờ học, phòng và huấn luyện viên. Thứ tự: giờ học tăng dần (quyết định trình bày, nguồn không quy định thứ tự). Không thẻ nào được chọn sẵn. Từ giây thứ 1 chưa có dữ liệu thì hiển thị MSG-10; sự cố hệ thống thì MSG-11, mất kết nối thì MSG-12. Phạm vi các lớp trong lịch (chi nhánh, khoảng ngày, lớp đã huỷ hoặc đã đủ chỗ có hiển thị hay không): chưa quy định (Q-83). Lịch không có lớp nào: chưa quy định (Q-105) | UC-010 bước 1-2, Dữ liệu ra 1 STT 1-4; P08 AC-B-BookClassSpotUI showClassSchedule; UI-STT 34, 56; MSG-10, MSG-11, MSG-12; Q-83, Q-105 |
| 6 | Thẻ lớp nhóm | Nút chọn | Chọn | Đánh dấu thẻ (viền 2 px, dấu tích), bỏ đánh dấu thẻ khác, ghi nhận lớp nhóm của thẻ làm Lớp nhóm đã chọn; xoá MSG-01 nếu đang hiện. Dùng được bằng bàn phím hoặc trình đọc màn hình: mũi tên chọn thẻ trong nhóm | UC-010 bước 3; P08 selectClass; UI-STT 34, 49 |
| 7 | Nút Đặt chỗ | Nút chính | Nhấn | Kiểm tra theo mục f). Chưa chọn thẻ nào thì hiển thị MSG-01 dưới nhãn nhóm thẻ và chuyển tiêu điểm vào nhóm thẻ. Đã chọn thì gửi lớp nhóm đã chọn cho máy chủ; máy chủ kiểm tra lần lượt quyền đặt lớp (bước 4), lớp chưa huỷ và thời hạn đặt chỗ (bước 5), số lớp trong ngày (bước 6), chỗ trống (bước 7). Kết quả: bị khoá quyền đặt lớp thì hiển thị MSG-05 (luồng 4a); lớp đã huỷ thì MSG-06 (5a); ngoài thời hạn đặt chỗ thì MSG-07 (5b); đủ số lớp trong ngày thì MSG-08 (6a); lớp đủ chỗ thì MSG-09 (7a1); còn chỗ thì máy chủ lưu chỗ đã đặt (bước 8) rồi mở SCR-07 với Lớp nhóm đã chọn (TR-08, mẫu 4). Từ giây thứ 1 hiển thị MSG-10; sự cố hệ thống thì MSG-11, mất kết nối thì MSG-12, ở lại SCR-06 và giữ thẻ đã chọn. Thứ tự kiểm tra là thứ tự trình bày của P04, nguồn không nêu thứ tự ưu tiên | UC-010 bước 3-9, 4a, 5a, 5b, 6a, 7a1; P08 selectClass, showBookingRejectedNotice, showClassFullNotice; TR-08; BR-06 đến BR-11; UI-STT 26, 38, 41, 56, 59; MSG-01, MSG-05 đến MSG-12 |
| 8 | Hộp MSG-05: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-06, giữ thẻ đã chọn; kết thúc use case (thất bại, luồng 4a) và chỗ đã đặt không đổi. Esc hoặc nút quay lại của hệ thống cùng nghĩa | UC-010 luồng 4a; BR-09; UI-STT 51, 59, 62; MSG-05 |
| 9 | Hộp MSG-06: nút Chọn lớp khác | Nút | Nhấn | Đóng hộp, tải lại lịch lớp nhóm (quay lại bước 2), bỏ thẻ đã chọn vì lớp đã chọn không còn đặt được | UC-010 luồng 5a; UI-STT 59; MSG-06 |
| 10 | Hộp MSG-07, MSG-08: nút Chọn lớp khác | Nút | Nhấn | Đóng hộp, giữ lịch lớp nhóm và thẻ đã chọn (quay lại bước 2); hội viên chọn thẻ khác rồi nhấn Đặt chỗ. Nội dung MSG-07 chờ Q-11, Q-58; cách tính ngày của MSG-08 chờ Q-60 | UC-010 luồng 5b, 6a; BR-06, BR-07, BR-08; UI-STT 59, 62; MSG-07, MSG-08 |
| 11 | Hộp MSG-09: nút Vào danh sách chờ | Nút chính | Nhấn | Gửi yêu cầu vào danh sách chờ của lớp đã chọn cho máy chủ (7a2); máy chủ thêm hội viên vào danh sách chờ (7a3, thứ tự xếp chờ Q-61) rồi mở SCR-08 với Lớp nhóm đã chọn (TR-09, mẫu 4). Từ giây thứ 1 hiển thị MSG-10; sự cố hệ thống thì MSG-11, mất kết nối thì MSG-12: đóng hộp MSG-09, ở lại SCR-06 và giữ thẻ đã chọn. Hộp mở với tiêu điểm ở nút Không vào. Hội viên tự vào hay được chọn vào chờ: Q-62 | UC-010 luồng 7a2, 7a3; BR-12; P08 requestJoinWaitlist; TR-09; UI-STT 52, 56, 74; MSG-09, MSG-10, MSG-11, MSG-12 |
| 12 | Hộp MSG-09: nút Không vào | Nút phụ | Nhấn | Đóng hộp, kết thúc use case (thất bại, luồng 7a2a): ở lại SCR-06, giữ thẻ đã chọn; chỗ đã đặt và danh sách chờ không đổi (hậu điều kiện tối thiểu). Esc hoặc nút quay lại của hệ thống cùng nghĩa | UC-010 luồng 7a2a, Hậu điều kiện tối thiểu; UI-STT 51, 52; MSG-09 |
| 13 | Hộp MSG-11, MSG-12: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-06, giữ nguyên thẻ đã chọn | UI-STT 60, 62; MSG-11, MSG-12 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Loại lớp | - | Chữ | Hiển thị trong thẻ; căn trái; chữ #1C1F2A Bold 16 sp | Văn bản; giá trị nguồn nêu: yoga, aerobic, đạp xe trong nhà (GL-27). Danh sách loại lớp đóng hay mở rộng: Q-04 | Hiển thị viết hoa chữ cái đầu (UI-STT 16); xuống dòng khi dài, không cắt (UI-STT 71) | P04 UC-010 Dữ liệu ra 1 STT 1; GL-27 |
| Phòng | - | Chữ | Hiển thị trong thẻ; căn trái; chữ #1C1F2A Regular 16 sp | Văn bản (tên phòng tập). Phòng thuộc chi nhánh nào: Q-03 | - | P04 UC-010 Dữ liệu ra 1 STT 2; GL-35 |
| Huấn luyện viên | - | Chữ | Hiển thị trong thẻ; căn trái; chữ #1C1F2A Regular 16 sp, nhãn Huấn luyện viên Medium 500 | Văn bản (họ tên) | - | P04 UC-010 Dữ liệu ra 1 STT 3; GL-21 |
| Giờ học | 16 | Ngày, Giờ | Hiển thị trong thẻ; căn trái; chữ #1C1F2A Bold 16 sp | Ngày và giờ bắt đầu của lớp, dạng dd/MM/yyyy HH:mm, giờ 24 (UI-STT 18) | Thiết kế: 16 là độ dài của định dạng hiển thị dd/MM/yyyy HH:mm, không phải miền giá trị. Giờ học và giờ bắt đầu: Q-73 | P04 UC-010 Dữ liệu ra 1 STT 4; GL-13; UI-STT 18 |
| Lớp nhóm đã chọn | - | Lựa chọn | Chọn qua thẻ; bắt buộc; không có mặc định; một lớp duy nhất | Một lớp trong lịch lớp nhóm đang hiển thị; bắt buộc chọn một lớp trước khi nhấn Đặt chỗ | P04 Dữ liệu vào ghi Không có; tính bắt buộc lấy từ P07 selectClass (bắt buộc chọn một lớp), không phải từ cột Bắt buộc của P04 | P04 UC-010 mục 5 Dữ liệu vào, bước 3; P07 AC-B-BookClassSpotUI selectClass |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Lớp nhóm đã chọn (nhóm thẻ lớp nhóm) | Khi nhấn Đặt chỗ. Nhóm thẻ chọn một trong nhiều nên không có sự kiện rời trường có nghĩa trước khi hội viên thao tác | (1) Bắt buộc: đã chọn đúng một thẻ. (2) Định dạng và (3) miền giá trị: giá trị lấy từ thẻ nên luôn là một lớp trong lịch, không kiểm tra thêm. (4) Quy tắc nghiệp vụ do máy chủ kiểm tra sau khi gửi: quyền đặt lớp không bị khoá (BR-09), lớp chưa huỷ và trong thời hạn đặt chỗ (BR-06, BR-07), số lớp trong ngày chưa đạt mức tối đa (BR-08), lớp còn chỗ (BR-10, BR-11) | Bắt buộc: MSG-01 (Vui lòng chọn lớp nhóm.). Quy tắc nghiệp vụ: MSG-05 (BR-09), MSG-06 (lớp đã huỷ), MSG-07 (BR-06, BR-07), MSG-08 (BR-08), MSG-09 (lớp đủ chỗ, BR-11, BR-12) |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-06 | Nielsen 6 Nhận biết thay vì nhớ lại | Vi phạm đã sửa | Áp nguyên UI-STT 33 (trên 5 giá trị thì dùng danh sách chọn, mỗi mục một dòng cao 48 dp) thì loại lớp, phòng, huấn luyện viên và giờ học (Dữ liệu ra 1 STT 1-4) không hiển thị cùng lúc để hội viên so sánh, phải mở từng mục. Màn hình dùng nhóm thẻ chọn, mỗi thẻ là một lớp với đủ bốn thông tin | Thẻ chọn theo UI-STT 34; đề xuất mở rộng ngoại lệ của UI-STT 33 ghi ở mục Đề xuất sửa artifact trước (cùng đề xuất đã ghi ở SCR-03) |
| SCR-06 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm; MSG-10 hiện từ giây thứ 1. Chưa quy định màn hình khi lịch không có lớp nào để hiển thị (Q-105) | Q-105 |
| SCR-06 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Lịch có thể rất dài (khoảng 25 lớp mỗi ngày mỗi chi nhánh, GL-29) mà đặc tả không nêu phạm vi lịch (Q-83) và không có chức năng lọc hay tìm kiếm | Q-83; không tự thêm lọc hay tìm kiếm (UI-STT 37) |
| SCR-06 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | MSG-05, MSG-06, MSG-08 nêu quy tắc và việc làm tiếp theo. Nội dung MSG-07 dựa trên BR-06, còn BR-07 mâu thuẫn BR-06 nên hội viên có thể được báo thời điểm mở đặt chỗ chưa đúng | Q-11, Q-58 |
| SCR-06 | Nielsen 5 Ngăn lỗi | Đạt | Đặt chỗ không phải thao tác tài chính và hoàn tác được bằng UC-011 nên không thêm bước xác nhận (UI-STT 74). Hướng chọn có hai phía (vào danh sách chờ) có hộp xác nhận MSG-09, nút an toàn Không vào nhận tiêu điểm đầu tiên (UI-STT 52) | - |
| SCR-06 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Nhóm thẻ là nhóm nút chọn (radiogroup) có nhãn Chọn lớp nhóm; mỗi thẻ đọc thành một câu: loại lớp, giờ học, phòng, huấn luyện viên | - |
| SCR-06 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm; MSG-01 có biểu tượng lỗi và chữ | - |
| SCR-06 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Hộp MSG-09 giữ tiêu điểm trong hộp, vào nút Không vào; khi đóng, tiêu điểm trở về nút Đặt chỗ đã mở hộp (UI-STT 52) | - |
| SCR-06 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 72 dp, vùng bấm là cả thẻ, khoảng cách 8 dp; nút Đặt chỗ cao 48 dp | - |
| SCR-06 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhóm thẻ có nhãn Chọn lớp nhóm kèm dấu *, đầu màn hình có chú thích * Bắt buộc | - |
| SCR-06 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | MSG-10 có vai trò status; MSG-01 có vai trò alert, đọc không chuyển tiêu điểm; hộp thông điệp là hộp thoại có nhãn tiêu đề | - |
| SCR-06 | Material Design (Android): vùng chạm, một hành động chính | Đạt | Một nút chính Đặt chỗ cao 48 dp; hộp MSG-09 có một nút chính Vào danh sách chờ và một nút phụ Không vào | - |
| SCR-06 | Apple HIG (iOS): vùng chạm, điều hướng quay lại | Đạt | Vùng chạm lớn hơn 44 pt; cử chỉ quay lại về SCR-02 theo UI-STT 15, đóng hộp thông điệp khi hộp đang mở | - |
| SCR-06 | Baymard: đánh dấu bắt buộc, thông điệp lỗi cạnh trường | Đạt | Nhãn nhóm có dấu *, đầu màn hình có chú thích * Bắt buộc, MSG-01 đặt ngay dưới nhãn nhóm; lỗi nghiệp vụ dùng hộp thoại vì không gắn với một trường (UI-STT 54, 59) | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-01 (mẫu Vui lòng chọn {tên trường} với tên trường là lớp nhóm), MSG-05 đến MSG-09, MSG-10, MSG-11, MSG-12 của ui-standards.md.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-105 | Khi lịch lớp nhóm ở bước 2 không có lớp nào để hiển thị, ứng dụng hiển thị gì và use case kết thúc ra sao? (Hiển thị thông báo chưa có lớp nhóm để đặt chỗ rồi kết thúc use case - nêu nội dung / Khác - nêu rõ) | SCR-06 (thao tác Khởi tạo của nhóm thẻ lớp nhóm); có thể cần thêm MSG và luồng thay thế ở P04 UC-010 | P04 UC-010 bước 2 "Hiển thị lịch các lớp nhóm để hội viên chọn lớp" không nêu trường hợp lịch không có lớp nào; Q-83 chỉ hỏi phạm vi của lịch |

Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-83 (phạm vi lịch lớp nhóm), Q-11 và Q-58 (cách mở đặt chỗ, mâu thuẫn BR-06 và BR-07, mốc muộn nhất), Q-59 (đặt trùng cùng lớp), Q-60 (cách tính lớp trong ngày), Q-61 và Q-62 (thứ tự xếp chờ, tự vào hay chọn vào danh sách chờ), Q-12 (điều kiện về gói tập khi đặt chỗ), Q-20 (hội viên bị khoá quyền đặt lớp), Q-22 (chỗ giữ riêng có tính vào chỗ đã đặt), Q-42 (ngưỡng thời gian phản hồi khi 1.500 hội viên đặt cùng lúc), Q-73 (giờ học và giờ bắt đầu), Q-03, Q-04 (danh mục phòng, loại lớp).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-010 bước 2, mục 3 (luồng thay thế) | Đặc tả không nêu trường hợp lịch lớp nhóm không có lớp nào (Q-105) | Khi Q-105 có trả lời, thêm luồng thay thế vào P04 UC-010 rồi chạy lại P11a giai đoạn 2 cho SCR-06. Chưa áp dụng (chờ Q-105) |
| P11a (giai đoạn 1) | ui-standards.md UI-STT 33 | Quy định chọn một trong trên 5 giá trị bằng danh sách chọn không hiển thị được cùng lúc nhiều thông tin của mỗi mục (lịch lớp nhóm: loại lớp, phòng, huấn luyện viên, giờ học). Cùng đề xuất đã ghi ở SCR-03 (nhóm thẻ chọn khi mỗi mục kèm giá) | Mở rộng ngoại lệ đã đề xuất ở SCR-03: khi mỗi mục chọn có nhiều thông tin cần nhìn cùng lúc để quyết định thì dùng nhóm thẻ chọn (di động) hoặc bảng có nút chọn ở mỗi dòng (web). Chỉ đổi cấu trúc trình bày nên giai đoạn 1 không chạy lại. Chưa áp dụng |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 3, 7: mọi trường hiển thị truy được về Dữ liệu ra 1 của P04; P04 ghi Dữ liệu vào là Không có, nên trường Lớp nhóm đã chọn lấy tính bắt buộc từ P07 selectClass và cần người dùng xác nhận. Độ dài của Giờ học (16) là độ dài định dạng hiển thị, ghi Thiết kế; không có độ dài hay miền giá trị tự đặt cho trường nhập.
- Target 9: có 3 dòng Vi phạm còn mở (Nielsen 1 gắn Q-105, Nielsen 7 gắn Q-83, Nielsen 9 gắn Q-11 và Q-58) đều do đặc tả chưa quy định; không có vi phạm WCAG AA chưa xử lý. Các tỉ lệ tương phản dùng lại các cặp màu đã đo ở ui-standards.md, nên đo lại bằng công cụ khi có bản thiết kế thật.
- Dữ liệu mẫu: các lớp mẫu cách giờ học không quá 7 ngày theo BR-06, nhưng BR-07 (tuần mới mở lúc 6 giờ sáng thứ Hai) mâu thuẫn BR-06 (Q-11) nên chưa khẳng định được lớp nào đặt được vào thời điểm nào.
- Màn hình không hiển thị số chỗ còn lại hay nhãn Đã đủ chỗ trên thẻ vì Dữ liệu ra 1 không có các thông tin này; hội viên chỉ biết lớp đủ chỗ ở hộp MSG-09 sau khi nhấn Đặt chỗ.
- Thứ tự thẻ theo giờ học tăng dần là quyết định trình bày (không có trong nguồn), cần người dùng xác nhận cùng Q-83.
