# P11a - SCR-03 Chọn gói tập - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, Mục 4, BR-01 đến BR-05, BR-38); P07-uc-analysis/UC-005 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); chưa có SCR nào trước lần chạy này nên không có mục h) của SCR khác. Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-102, P11b đã chạy; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-103, Q-104. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-005 (SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14; màn hình điều hướng SCR-02, SCR-10 để lần chạy sau); lần chạy này không phải lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a giai đoạn 1, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-03 (UC-005, ACT-02 Hội viên, ứng dụng di động) |
| Mã Q, ASM cuối đã cấp | Q-104; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-03 Chọn gói tập (Select membership package) |
| UC | UC-005 Mua hoặc gia hạn gói tập |
| Bước UC | 1-3 (bước 1 là yêu cầu nhấn từ SCR-02; bước 2 hiển thị các gói tập; bước 3 chọn gói tập; bước 4 và 5 do máy chủ xử lý trước khi mở SCR-04) |
| Tác nhân | ACT-02 Hội viên |
| Boundary AC | AC-B-PurchaseOrRenewPackageUI |
| DC | DC-PurchaseOrRenewPackageView (đi cùng DC-PurchaseOrRenewPackageStore) |
| Loại màn hình | Độc lập |
| Đến từ | SCR-02 (TR-03, mẫu 1); SCR-04 (TR-05, mẫu 1: nút Quay lại, hoặc nút Chọn lại gói tập của MSG-02) |
| Đi tới | SCR-04 (TR-04, mẫu 4, dữ liệu truyền Gói tập đã chọn); SCR-02 (nút Trang chủ và nút quay lại của hệ thống, mẫu 1, ghi ở node START-ACT-02) |

## c) Hình ảnh màn hình

Hình minh hoạ ở trạng thái đã chọn thẻ thứ ba. Khi mở màn hình lần đầu không có thẻ nào được chọn.

```text
+--------------------------------------+
| [VietFit]                  [Trang chủ]|
|--------------------------------------|
| Chọn gói tập                         |
| * Bắt buộc                           |
|                                      |
| Chọn gói tập *                       |
| +----------------------------------+ |
| | ( ) 1 tháng             250.000 đ| |
| |     Một chi nhánh - Chi nhánh 2  | |
| +----------------------------------+ |
| | ( ) 3 tháng             650.000 đ| |
| |     Một chi nhánh - Chi nhánh 2  | |
| +----------------------------------+ |
| |[x] 6 tháng            1.200.000 đ| |
| |     Toàn chuỗi                   | |
| +----------------------------------+ |
| | ( ) 12 tháng          2.100.000 đ| |
| |     Toàn chuỗi                   | |
| +----------------------------------+ |
| Gói Toàn chuỗi áp dụng cho cả chuỗi, |
| gói Một chi nhánh chỉ áp dụng cho    |
| một chi nhánh.                       |
|                                      |
| [            Tiếp tục              ] |
+--------------------------------------+
```

Trạng thái lỗi khi nhấn Tiếp tục mà chưa chọn thẻ nào:

```text
| Chọn gói tập *                       |
|  (!) Vui lòng chọn gói tập.          |
| +----------------------------------+ |
| | ( ) 1 tháng             250.000 đ| |
| ...                                  |
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit, nút Trang chủ | Trên cùng, cao 56 dp; logo bên trái cách mép 16 dp, cao 28 dp; Trang chủ bên phải | UI-STT 10, 12, 45 |
| Dải thông báo | Không dùng ở màn hình này | - | Lỗi nhập hiện tại trường (UI-STT 58) |
| Tiêu đề màn hình | Chọn gói tập | Đầu vùng nội dung, 20 sp Bold | UI-STT 13 |
| Nội dung | Dòng chú thích * Bắt buộc, nhãn nhóm, bốn thẻ gói tập, chú thích loại gói | Cuộn dọc, lề trái phải 16 dp, thẻ cách nhau 8 dp, thẻ cao tối thiểu 72 dp | UI-STT 10, 31, 34, 64 |
| Hành động | Nút chính Tiếp tục | Cuối nội dung, rộng 328 dp ở 360 dp, cao 48 dp | UI-STT 14, 26. Không có nút phụ |
| Thông điệp | MSG-01 ngay dưới nhãn nhóm thẻ; hộp MSG-11, MSG-12 là lớp phủ giữa màn hình | - | UI-STT 54, 58 |

Dữ liệu mẫu: bốn giá gói minh hoạ; giá 6 tháng Toàn chuỗi 1.200.000 đ lấy theo ví dụ Dữ liệu ra 1 của P04. Tên Chi nhánh 2 lấy theo ví dụ Dữ liệu vào 1 của P04.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Nút Trang chủ | Nút | Nhấn | Rời màn hình, bỏ thẻ đã chọn, mở SCR-02 (mẫu 1). Chưa có đơn mua nào được tạo nên không có dữ liệu cần giữ | UI-STT 45; screen-transition.md node START-ACT-02 |
| 3 | Nút quay lại của hệ thống (Android) hoặc cử chỉ quay lại (iOS) | Nút | Nhấn | Mở SCR-02 vì màn hình không có nút Quay lại | UI-STT 15 |
| 4 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Chọn gói tập, sau đó dòng chú thích * Bắt buộc | UI-STT 13, 31 |
| 5 | Nhóm thẻ gói tập | Nút chọn | Khởi tạo | Hiển thị mỗi giá gói hiện hành một thẻ gồm thời hạn, loại, chi nhánh áp dụng (chỉ với gói Một chi nhánh, nguồn chi nhánh: Q-50) và giá. Thứ tự: thời hạn tăng dần, cùng thời hạn thì Một chi nhánh trước Toàn chuỗi. Không thẻ nào được chọn sẵn; khi đến từ nút Quay lại của SCR-04 thì giữ thẻ đã chọn, khi đến từ MSG-02 thì không chọn sẵn. Không có giá gói nào để hiển thị: chưa quy định (Q-103) | UC-005 bước 2, Dữ liệu ra 1 STT 1-4; P08 AC-B-PurchaseOrRenewPackageUI showPackageOptions; UI-STT 15, 34, 62; Q-50, Q-103 |
| 6 | Thẻ gói tập | Nút chọn | Chọn | Đánh dấu thẻ (viền 2 px, dấu tích), bỏ đánh dấu thẻ khác, ghi nhận thời hạn và loại của thẻ làm Gói tập đã chọn; xoá MSG-01 nếu đang hiện | UC-005 bước 3, Dữ liệu vào 1 STT 1, 2; P08 selectPackage |
| 7 | Chú thích loại gói | Vùng hiển thị | Khởi tạo | Hiển thị dưới nhóm thẻ: Gói Toàn chuỗi áp dụng cho cả chuỗi, gói Một chi nhánh chỉ áp dụng cho một chi nhánh | UI-STT 64; BR-02 |
| 8 | Nút Tiếp tục | Nút chính | Nhấn | Kiểm tra theo mục f). Chưa chọn thẻ nào thì hiển thị MSG-01 dưới nhãn nhóm thẻ và chuyển tiêu điểm vào nhóm thẻ. Đã chọn thì gửi gói đã chọn cho máy chủ; máy chủ xác định ngày bắt đầu (bước 4), tính số tiền phải trả (bước 5), rồi mở SCR-04 với Gói tập đã chọn (TR-04, mẫu 4). Từ giây thứ 1 hiển thị MSG-10; sự cố hệ thống thì hiển thị MSG-11, mất kết nối thì MSG-12, ở lại SCR-03 và giữ thẻ đã chọn | UC-005 bước 3-6; P08 selectPackage; TR-04; UI-STT 38, 41, 56; MSG-01, MSG-10, MSG-11, MSG-12 |
| 9 | Hộp MSG-11, MSG-12: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-03, giữ nguyên thẻ đã chọn | UI-STT 60, 62; MSG-11, MSG-12 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Thời hạn gói | - | Lựa chọn | Hiển thị trong thẻ; chọn qua thẻ; bắt buộc; không có mặc định; căn trái; chữ #1C1F2A Bold 16 sp | Một trong 1, 3, 6, 12 tháng (BR-01) | Hiển thị dạng số nguyên kèm chữ tháng (UI-STT 20) | P04 UC-005 Dữ liệu vào 1 STT 1, Dữ liệu ra 1 STT 1; BR-01 |
| Loại gói | - | Lựa chọn | Hiển thị trong thẻ; chọn qua thẻ; bắt buộc; không có mặc định; căn trái; chữ #1C1F2A Regular 16 sp | Một chi nhánh hoặc Toàn chuỗi (BR-02) | Hiển thị đúng chữ Một chi nhánh hoặc Toàn chuỗi (UI-STT 20) | P04 UC-005 Dữ liệu vào 1 STT 2, Dữ liệu ra 1 STT 2; BR-02 |
| Chi nhánh áp dụng | - | Chữ | Hiển thị trong thẻ; bắt buộc: chưa quy định (Q-50); căn trái; chữ #1C1F2A Regular 16 sp | Chỉ gói loại Một chi nhánh có giá trị. Ai xác định chi nhánh và có nhập hay chọn ở màn hình này không: chưa quy định (Q-50) | Màn hình chỉ hiển thị giá trị do máy chủ trả; không có điều khiển nhập cho tới khi Q-50 có trả lời | P04 UC-005 Dữ liệu vào 1 STT 3, Dữ liệu ra 1 STT 3; Q-50 |
| Giá gói | 13 | Tiền | Hiển thị trong thẻ; căn phải; chữ #1C1F2A Bold 16 sp | Số nguyên đồng, phân cách hàng nghìn bằng dấu chấm, kèm dấu cách và chữ đ (UI-STT 19) | Thiết kế: 13 là độ rộng vùng hiển thị tiền (999.999.999 đ), chỉ là độ rộng hiển thị, không phải miền giá trị của giá gói. Khuyến mãi không trừ vào giá ở màn hình này (Q-09) | P04 UC-005 Dữ liệu ra 1 STT 4; UI-STT 19 |
| Gói đang có cần gia hạn | Chưa quy định (Q-56) | Chưa quy định (Q-56) | Chưa quy định (Q-56): bắt buộc hay không, nhập hay chọn | Chưa quy định (Q-56) | Không có điều khiển trên hình ảnh cho tới khi Q-56 có trả lời. Không có điều khiển này thì màn hình chưa phân biệt được mua gói mới và gia hạn | P04 UC-005 Dữ liệu vào 1 STT 4; Q-56 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Thời hạn gói, Loại gói (nhóm thẻ gói tập) | Khi nhấn Tiếp tục. Nhóm thẻ chọn một trong nhiều nên không có sự kiện rời trường có nghĩa trước khi người dùng thao tác | (1) Bắt buộc: đã chọn đúng một thẻ. (2) Định dạng và miền giá trị: giá trị lấy từ thẻ nên luôn thuộc 1, 3, 6, 12 tháng và hai loại gói, không kiểm tra thêm. (3) Quy tắc nghiệp vụ: không có ở màn hình này | MSG-01 (Vui lòng chọn gói tập.) |
| Chi nhánh áp dụng | Chưa quy định (Q-50) | Chưa quy định (Q-50) | - |
| Gói đang có cần gia hạn | Chưa quy định (Q-56) | Chưa quy định (Q-56) | - |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-03 | Nielsen 6 Nhận biết thay vì nhớ lại | Vi phạm đã sửa | Áp nguyên UI-STT 33 (hai nhóm nút chọn riêng cho thời hạn và loại gói) thì giá của từng tổ hợp (Dữ liệu ra 1 STT 4) không hiển thị cạnh lựa chọn, người dùng phải nhớ giá và có thể chọn tổ hợp chưa có giá gói. Màn hình dùng một nhóm thẻ chọn, mỗi thẻ là một tổ hợp thời hạn và loại kèm giá | Thẻ chọn theo UI-STT 34; đề xuất bổ sung ngoại lệ vào UI-STT 33 (mục Đề xuất sửa artifact trước) |
| SCR-03 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm nên trạng thái chọn rõ. Chưa quy định màn hình khi không có giá gói nào để hiển thị (Q-103) | Q-103 |
| SCR-03 | Nielsen 5 Ngăn lỗi | Đạt | Chỉ chọn được tổ hợp có trong danh sách giá gói hiện hành; thiếu lựa chọn thì MSG-01 trước khi gửi máy chủ | - |
| SCR-03 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Đặc tả có Dữ liệu vào Gói đang có cần gia hạn nhưng chưa quy định cách chỉ định (Q-56), nên màn hình chưa có điều khiển để hội viên gia hạn một gói cụ thể | Q-56; không tự thêm điều khiển |
| SCR-03 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Nhóm thẻ là nhóm nút chọn (radiogroup) có nhãn Chọn gói tập; mỗi thẻ đọc thành một câu: thời hạn, loại, giá | - |
| SCR-03 | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | Thẻ đang chọn có viền 2 px, dấu tích và chữ đậm; lỗi MSG-01 có biểu tượng và chữ | - |
| SCR-03 | WCAG 2.5.8 Vùng bấm tối thiểu | Đạt | Thẻ cao tối thiểu 72 dp, vùng bấm là cả thẻ, khoảng cách 8 dp | - |
| SCR-03 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Nhóm thẻ có nhãn Chọn gói tập kèm dấu *, chú thích loại gói dưới nhóm | - |
| SCR-03 | Material Design (Android): vùng chạm, một hành động chính | Đạt | Một nút chính Tiếp tục cao 48 dp; thẻ cao tối thiểu 72 dp | - |
| SCR-03 | Apple HIG (iOS): vùng chạm, điều hướng quay lại | Đạt | Vùng chạm lớn hơn 44 pt; cử chỉ quay lại về SCR-02 theo UI-STT 15 | - |
| SCR-03 | Baymard: đánh dấu bắt buộc, thông điệp lỗi cạnh trường | Đạt | Nhãn nhóm có dấu *, đầu màn hình có chú thích * Bắt buộc, MSG-01 đặt ngay dưới nhãn nhóm | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-01 (mẫu Vui lòng chọn {tên trường} với tên trường là gói tập), MSG-10, MSG-11, MSG-12.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-103 | Khi chưa có giá gói hiện hành nào để hiển thị ở bước 2 (giám đốc chuỗi chưa đặt giá ở UC-026), ứng dụng di động và ứng dụng web hiển thị gì và use case kết thúc ra sao? (Hiển thị thông báo chưa có gói tập để mua rồi kết thúc use case - nêu nội dung / Khác - nêu rõ) | SCR-03, SCR-11 (thao tác Khởi tạo của nhóm thẻ và bảng gói); có thể cần thêm MSG và luồng thay thế ở P04 UC-005 | P04 UC-005 bước 2 "Hiển thị các gói tập kèm thời hạn, loại và giá hiện hành" không nêu trường hợp không có gói nào |

Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-50 (chi nhánh áp dụng), Q-56 (gói đang có cần gia hạn), Q-09 (cách áp dụng khuyến mãi vào số tiền), Q-82 (tên gọi mặt hàng được bán ở bước 2, 3: màn hình dùng "gói tập" theo đặc tả).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-005 bước 2, mục 3 (luồng thay thế) | Đặc tả không nêu trường hợp không có giá gói hiện hành (Q-103) | Khi Q-103 có trả lời, thêm luồng thay thế vào P04 UC-005 rồi chạy lại P11a giai đoạn 2 cho SCR-03, SCR-11. Chưa áp dụng (chờ Q-103) |
| P11a (giai đoạn 1) | ui-standards.md UI-STT 33 | Quy định hiển thị thời hạn gói và loại gói bằng nút chọn riêng không hiển thị được giá của từng tổ hợp | Bổ sung ngoại lệ: khi các thuộc tính chọn phải đi kèm giá của tổ hợp thì dùng một nhóm thẻ chọn (di động) hoặc bảng có nút chọn ở mỗi dòng (web). Chỉ đổi cấu trúc trình bày nên giai đoạn 1 không chạy lại; cập nhật khi nối dòng ở lần chạy giai đoạn 2 cuối cùng |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 3, 7: Chi nhánh áp dụng và Gói đang có cần gia hạn là Dữ liệu vào của P04 nhưng chưa quy định bắt buộc, điều kiện hợp lệ và cách nhập (Q-50, Q-56), nên chỉ có dòng ở mục e) và không có điều khiển trên hình ảnh. Khi hai Q này có trả lời cần chạy lại SCR-03 và SCR-11.
- Target 9: có 2 dòng Vi phạm còn mở (Nielsen 1 gắn Q-103, Nielsen 7 gắn Q-56) đều do đặc tả chưa quy định; không có vi phạm WCAG AA chưa xử lý.
- Dữ liệu mẫu có giá 6 tháng Toàn chuỗi 1.200.000 đ nhưng SCR-04 hiển thị số tiền phải trả 1.080.000 đ (khuyến mãi 10%, trong giới hạn 20% của BR-38); chênh lệch này chưa được giải thích trên màn hình (xem mục g) của SCR-04).
- Nhóm thẻ có thể có tối đa 8 thẻ (4 thời hạn nhân 2 loại), vẫn cuộn dọc trong một cột; không có tìm kiếm hay lọc vì đặc tả không có.
