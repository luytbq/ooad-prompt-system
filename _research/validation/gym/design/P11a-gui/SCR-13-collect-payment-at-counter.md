# P11a - SCR-13 Thu tiền tại quầy - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, Mục 4, BR-01 đến BR-05, BR-38); P07-uc-analysis/UC-005 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); chưa có SCR nào trước lần chạy này nên không có mục h) của SCR khác. Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-102, P11b đã chạy; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-103, Q-104. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-005 (SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14; màn hình điều hướng SCR-02, SCR-10 để lần chạy sau); lần chạy này không phải lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a giai đoạn 1, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-13 (UC-005, ACT-05 Lễ tân, ứng dụng web) |
| Mã Q, ASM cuối đã cấp | Q-104; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-13 Thu tiền tại quầy (Collect payment at counter) |
| UC | UC-005 Mua hoặc gia hạn gói tập |
| Bước UC | 8a, 8b (bước 11 ghi nhận đã thanh toán, kích hoạt gói và bước 12 gửi hoá đơn điện tử do máy chủ xử lý sau khi nhấn Xác nhận đã thu) |
| Tác nhân | ACT-05 Lễ tân |
| Boundary AC | AC-B-SellPackageUI |
| DC | DC-SellPackageView (đi cùng DC-SellPackageStore) |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-12 (TR-15, mẫu 4, dữ liệu Đơn mua chờ thu tiền) |
| Đi tới | SCR-14 (TR-16, mẫu 4, dữ liệu Đơn mua đã thanh toán); SCR-10, SCR-11 và các màn hình khác qua menu trái (mẫu 1, ghi ở node START-ACT-05). Không có nút Quay lại vì đơn đã tạo |

## c) Hình ảnh màn hình

Hình minh hoạ ở trạng thái đã chọn Thẻ ngân hàng qua máy POS và đã nhập mã. Khi mở màn hình lần đầu chưa chọn hình thức thu và chưa hiện ô Mã giao dịch POS.

```text
+---------------------------------------------------------------------------------------------------------------------+
| [VietFit]                                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------+
| Trang chủ                  | Thu tiền tại quầy                                                                      |
| > Mua hoặc gia hạn gói tập | * Bắt buộc                                                                             |
| Chuyển nhượng gói tập      |                                                                                        |
| Bán vé tập một ngày        | Gói tập                  6 tháng, Toàn chuỗi                                           |
|                            | Số tiền phải trả         1.080.000 đ                                                   |
|                            |                                                                                        |
|                            | Hình thức thu *                                                                        |
|                            |   ( ) Tiền mặt        (x) Thẻ ngân hàng qua máy POS                                    |
|                            |                                                                                        |
|                            | Mã giao dịch POS *                                                                     |
|                            | [ 004217              ]                                                                |
|                            | Nhập mã in trên hoá đơn POS.                                                           |
|                            |                                                                                        |
|                            |                                    [ Xác nhận đã thu 1.080.000 đ ]                     |
+----------------------------+----------------------------------------------------------------------------------------+
```

Trạng thái đã chọn Tiền mặt (không có ô Mã giao dịch POS):

```text
 Hình thức thu *
   (x) Tiền mặt        ( ) Thẻ ngân hàng qua máy POS

                                    [ Xác nhận đã thu 1.080.000 đ ]
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit | Trên cùng, cao 56 px, logo trái cách mép 24 px, cao 32 px | UI-STT 11, 12 |
| Menu | Trang chủ, Mua hoặc gia hạn gói tập, Chuyển nhượng gói tập, Bán vé tập một ngày; mục Mua hoặc gia hạn gói tập đang chọn | Trái, rộng 240 px, nền #F4F5F9, mỗi mục cao 44 px | UI-STT 44, 46, 47, 48 |
| Dải thông báo | Không dùng ở màn hình này | - | - |
| Tiêu đề màn hình | Thu tiền tại quầy | Đầu vùng nội dung, 24 px Bold | UI-STT 13 |
| Nội dung | Chú thích * Bắt buộc, hai dòng tóm tắt (gói tập, số tiền phải trả), nhóm nút chọn Hình thức thu, ô Mã giao dịch POS (chỉ khi chọn Thẻ ngân hàng qua máy POS) | Lề 24 px, khoảng cách giữa hai trường 16 px, nhãn cách ô nhập 4 px | UI-STT 11, 30, 31, 32, 64 |
| Hành động | Nút chính Xác nhận đã thu kèm số tiền | Cuối nội dung, canh phải, cao 44 px | UI-STT 14, 26, 75. Không có nút phụ |
| Thông điệp | MSG-01 dưới trường lỗi; hộp MSG-10, MSG-11, MSG-12 là lớp phủ modal rộng 480 px | - | UI-STT 54, 58 |

Dữ liệu mẫu nhất quán với SCR-12: gói 6 tháng Toàn chuỗi, số tiền phải trả 1.080.000 đ; mã giao dịch POS 004217 theo ví dụ Dữ liệu vào 2 của P04.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Menu trái | Liên kết | Khởi tạo | Hiển thị các mục theo thứ tự: Trang chủ, Mua hoặc gia hạn gói tập (UC-005), Chuyển nhượng gói tập (UC-007), Bán vé tập một ngày (UC-017); đánh dấu mục Mua hoặc gia hạn gói tập đang chọn | UI-STT 44, 46, 47, 48; P02 bảng 4a |
| 3 | Mục menu Trang chủ, Mua hoặc gia hạn gói tập | Liên kết | Nhấn | Rời màn hình và mở SCR-10 hoặc SCR-11 trống (mẫu 1). Đơn đã tạo ở trạng thái chờ thanh toán được giữ nguyên, màn hình không huỷ đơn vì đặc tả không có thao tác huỷ (Q-57); đơn bán tại quầy có hết hạn sau 15 phút hay không: Q-25 | UI-STT 46; screen-transition.md node START-ACT-05; Q-25, Q-57 |
| 4 | Mục menu Chuyển nhượng gói tập, Bán vé tập một ngày | Liên kết | Nhấn | Chưa có màn hình đích (UC-007), Chưa có màn hình đích (UC-017); ở lại SCR-13 | UI-STT 44; screen-transition.md node SCR-10 |
| 5 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Thu tiền tại quầy, sau đó dòng chú thích * Bắt buộc | UI-STT 13, 31 |
| 6 | Dòng Gói tập | Vùng hiển thị | Khởi tạo | Hiển thị thời hạn và loại của gói trong đơn đã tạo | UC-005 bước 8a, Dữ liệu ra 2 STT 1 |
| 7 | Dòng Số tiền phải trả | Vùng hiển thị | Khởi tạo | Hiển thị số tiền lễ tân phải thu của khách | UC-005 luồng 8a, Dữ liệu ra 2 STT 3; GL-37 |
| 8 | Nhóm nút chọn Hình thức thu | Nút chọn | Khởi tạo | Hiển thị hai nút chọn Tiền mặt và Thẻ ngân hàng qua máy POS, không chọn sẵn nút nào. Hình thức thu qua cổng thanh toán tại quầy: Q-98 | UC-005 luồng 8a, 8b; P08 confirmCashCollected, enterPosTransactionCode; UI-STT 33; Q-98 |
| 9 | Nút chọn Tiền mặt | Nút chọn | Chọn | Ẩn ô Mã giao dịch POS (nếu đang hiện) và xoá lỗi của ô; khách trả bằng tiền mặt (luồng 8a) | UC-005 luồng 8a |
| 10 | Nút chọn Thẻ ngân hàng qua máy POS | Nút chọn | Chọn | Hiển thị ô Mã giao dịch POS ngay dưới nhóm, không tự chuyển tiêu điểm vào ô; khách quẹt thẻ qua máy POS (luồng 8b) | UC-005 luồng 8b; GL-33; WCAG 3.2.2 |
| 11 | Ô nhập Mã giao dịch POS | Ô nhập | Nhập | Ghi nhận mã lễ tân nhập, cắt khoảng trắng đầu và cuối khi rời trường. Quy tắc định dạng và kiểm tra trùng: chưa quy định (Q-55) | UC-005 luồng 8b, Dữ liệu vào 2 STT 1; NFR-08; UI-STT 40; Q-55 |
| 12 | Ô nhập Mã giao dịch POS | Ô nhập | Rời trường | Kiểm tra theo mục f); trống thì hiển thị MSG-01 ngay dưới ô; hợp lệ thì xoá lỗi của ô | UI-STT 38, 39; MSG-01 |
| 13 | Nút Xác nhận đã thu | Nút chính | Nhấn | Kiểm tra lại mọi trường theo mục f); chưa chọn hình thức thu hoặc thiếu mã thì hiển thị MSG-01 tại trường và chuyển tiêu điểm tới trường sai đầu tiên. Hợp lệ thì gửi hình thức thu (và mã giao dịch POS nếu có) cho máy chủ; nhãn nút chuyển thành Đang xử lý và khoá nhấn lại (UI-STT 41), từ giây thứ 1 hiển thị MSG-10. Máy chủ ghi nhận đơn đã thanh toán và kích hoạt gói (bước 11), gửi dữ liệu giao dịch sang hệ thống hoá đơn điện tử (bước 12), rồi mở SCR-14 với Đơn mua đã thanh toán (TR-16, mẫu 4). Kết cục khi hệ thống hoá đơn điện tử không nhận dữ liệu: chờ Q-54. Sự cố hệ thống thì hiển thị MSG-11, mất kết nối thì MSG-12, ở lại SCR-13 và giữ dữ liệu. Nhấn Enter ở ô Mã giao dịch POS cũng chạy quy trình này | UC-005 luồng 8a, 8b, bước 11-13; TR-16; UI-STT 38, 41, 50, 56, 75; MSG-01, MSG-10, MSG-11, MSG-12; Q-54 |
| 14 | Hộp MSG-11, MSG-12: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-13, giữ nguyên hình thức thu và mã đã nhập | UI-STT 60, 62; MSG-11, MSG-12 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Gói tập | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Regular 14 px | Dạng "{n} tháng, {loại}"; thời hạn thuộc 1, 3, 6, 12 tháng (BR-01), loại thuộc Một chi nhánh hoặc Toàn chuỗi (BR-02) | Gói loại Một chi nhánh thêm tên chi nhánh áp dụng trong ngoặc (nguồn chi nhánh: Q-50) | P04 UC-005 Dữ liệu ra 2 STT 1; BR-01, BR-02 |
| Số tiền phải trả | 13 | Tiền | Hiển thị; căn phải; chữ #1C1F2A Bold 14 px | Số nguyên đồng, phân cách hàng nghìn bằng dấu chấm, kèm dấu cách và chữ đ | Thiết kế: 13 là độ rộng vùng hiển thị tiền (999.999.999 đ), không phải miền giá trị. Cùng giá trị đã hiển thị ở SCR-12 | P04 UC-005 Dữ liệu ra 2 STT 3; GL-37; UI-STT 19 |
| Hình thức thu | - | Lựa chọn | Chọn; bắt buộc; không có mặc định; căn trái; chữ #1C1F2A Regular 14 px | Một trong hai giá trị: Tiền mặt, Thẻ ngân hàng qua máy POS. Có thêm hình thức qua cổng thanh toán hay không: Q-98 | Cột Bắt buộc của P04 không có trường này; hình thức thu là điều kiện chọn luồng 8a hoặc 8b nên màn hình đặt bắt buộc và không có mặc định | P04 UC-005 luồng 8a, 8b (cột Điều kiện); P07 AC-E-PaymentTransaction paymentMethod; Q-98 |
| Mã giao dịch POS | Chưa quy định (Q-55) | Chữ | Nhập; bắt buộc khi Hình thức thu là Thẻ ngân hàng qua máy POS, không hiển thị ở hình thức khác; căn trái; chữ #1C1F2A Regular 14 px; ô cao 40 px | Bắt buộc nhập (Dữ liệu vào 2 STT 1: Có). Định dạng, độ dài, kiểm tra trùng: chưa quy định (Q-55) | Cắt khoảng trắng đầu và cuối, không đổi ký tự khác (UI-STT 40). Chú thích dưới ô: Nhập mã in trên hoá đơn POS. Không placeholder | P04 UC-005 Dữ liệu vào 2 STT 1; GL-31; NFR-08; Q-55 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Hình thức thu | Khi nhấn Xác nhận đã thu. Nhóm nút chọn một trong nhiều nên không có sự kiện rời trường có nghĩa trước khi người dùng thao tác | (1) Bắt buộc: đã chọn một nút. (2) Định dạng, miền giá trị: giá trị lấy từ nút chọn nên luôn thuộc hai giá trị hợp lệ. (3) Quy tắc nghiệp vụ: không có ở màn hình này | MSG-01 (Vui lòng chọn hình thức thu.) |
| Mã giao dịch POS (khi Hình thức thu là Thẻ ngân hàng qua máy POS) | Khi rời trường và khi nhấn Xác nhận đã thu | (1) Bắt buộc: không để trống sau khi cắt khoảng trắng. (2) Định dạng và (3) miền giá trị: chưa quy định (Q-55) nên giao diện chưa kiểm tra. (4) Quy tắc nghiệp vụ (kiểm tra trùng với mã đã nhập): chưa quy định (Q-55) | MSG-01 (Vui lòng nhập mã giao dịch POS.); thông điệp cho lỗi định dạng và trùng mã: chờ Q-55 |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-13 | Nielsen 5 Ngăn lỗi (mã giao dịch POS) | Vi phạm còn mở | Chưa quy định định dạng và kiểm tra trùng của mã giao dịch POS, nên giao diện không ngăn được nhập sai hoặc nhập trùng mã | Q-55 |
| SCR-13 | Nielsen 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | Đơn đã tạo nên không có nút Quay lại, và không có thao tác huỷ đơn chưa thu tiền; lễ tân chỉ rời bằng menu để lại đơn chờ thanh toán | Q-57, Q-25; không tự thêm nút huỷ |
| SCR-13 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | Chưa có thông điệp khi hệ thống hoá đơn điện tử không nhận dữ liệu giao dịch sau khi lễ tân xác nhận đã thu | Q-54 |
| SCR-13 | Nielsen 2 Khớp giữa hệ thống và thế giới thực | Đạt | Hai lựa chọn gọi là Tiền mặt và Thẻ ngân hàng qua máy POS, đúng thuật ngữ P05 (Giao dịch thu tiền GL-12, Máy POS GL-33) | - |
| SCR-13 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Số tiền phải trả, hình thức thu và mã hiển thị trên cùng màn hình trước khi nhấn; không chọn sẵn hình thức thu; nhãn nút chính có số tiền (UI-STT 75) | - |
| SCR-13 | WCAG 3.2.2 Khi nhập liệu (ngoài danh sách F7) | Đạt | Chọn Thẻ ngân hàng qua máy POS chỉ hiện thêm ô mã bên dưới, không tự chuyển tiêu điểm hay chuyển màn hình | - |
| SCR-13 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Nhóm nút chọn Hình thức thu có nhãn nhóm (fieldset, legend); ô Mã giao dịch POS gắn nhãn bằng for và id và gắn chú thích bằng aria-describedby | - |
| SCR-13 | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | Ô mã có nhãn Mã giao dịch POS kèm dấu * và chú thích Nhập mã in trên hoá đơn POS (nội dung theo GL-31) | - |
| SCR-13 | Baymard: nhãn trên ô nhập, không placeholder; chấp nhận nhiều định dạng nhập | Đạt | Nhãn đặt trên ô, không có placeholder; mã được cắt khoảng trắng đầu cuối nên mã dán từ hoá đơn không bị từ chối vì khoảng trắng (UI-STT 40) | - |
| SCR-13 | Baymard: kiểm tra khi rời trường, giữ dữ liệu khi báo lỗi | Đạt | Ô mã kiểm tra bắt buộc khi rời trường; MSG-11, MSG-12 giữ hình thức thu và mã đã nhập | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-01 (mẫu Vui lòng {chọn hoặc nhập} {tên trường} với tên trường là hình thức thu hoặc mã giao dịch POS), MSG-10, MSG-11, MSG-12.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-55 (quy tắc mã giao dịch POS), Q-98 (hình thức thu qua cổng thanh toán tại quầy), Q-54 (hệ thống hoá đơn điện tử không nhận dữ liệu), Q-57 (huỷ đơn chưa thanh toán), Q-25 (15 phút có áp dụng cho đơn bán tại quầy không), Q-39 (dữ liệu hoá đơn điện tử).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-005 luồng 8a, 8b; Dữ liệu vào (bước 8) | Hình thức thu (tiền mặt hoặc thẻ qua máy POS) là điều kiện chọn luồng 8a hay 8b nhưng không là Dữ liệu vào của đặc tả, trong khi lễ tân phải chọn trên màn hình | Khi Q-98 có trả lời, thêm Dữ liệu vào Hình thức thu (Bắt buộc: Có; Điều kiện hợp lệ: các hình thức được phép) ở bước 8. Chưa áp dụng (chờ Q-98) |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 3: trường Hình thức thu truy được về điều kiện của luồng 8a, 8b và thuộc tính paymentMethod của P07, không có dòng riêng ở Dữ liệu vào của P04; xem Đề xuất sửa artifact trước.
- Target 7: độ dài và định dạng của Mã giao dịch POS ghi Chưa quy định kèm Q-55; không có giá trị tự đặt.
- Target 9: có 3 dòng Vi phạm còn mở (Nielsen 5 gắn Q-55, Nielsen 3 gắn Q-57 và Q-25, Nielsen 9 gắn Q-54) đều do đặc tả chưa quy định; không có vi phạm WCAG AA chưa xử lý.
- Nhãn nút chính Xác nhận đã thu kèm số tiền dài hơn 4 từ nếu tính cả số tiền; coi số tiền là một thành phần theo ví dụ của UI-STT 75, phần động từ cộng đối tượng vẫn là 4 từ (UI-STT 29).
- Nếu Q-98 trả lời lễ tân cũng bán qua cổng thanh toán thì SCR-13 cần thêm hình thức thu và luồng chờ kết quả như SCR-04.
