# P11a - SCR-11 Chọn gói tập và người mua - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, Mục 4, BR-01 đến BR-05, BR-38); P07-uc-analysis/UC-005 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); chưa có SCR nào trước lần chạy này nên không có mục h) của SCR khác. Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-102, P11b đã chạy; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-103, Q-104. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-005 (SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14; màn hình điều hướng SCR-02, SCR-10 để lần chạy sau); lần chạy này không phải lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a giai đoạn 1, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-11 (UC-005, ACT-05 Lễ tân, ứng dụng web) |
| Mã Q, ASM cuối đã cấp | Q-104; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-11 Chọn gói tập và người mua (Select package and buyer) |
| UC | UC-005 Mua hoặc gia hạn gói tập |
| Bước UC | 1-3 (bước 1 là yêu cầu nhấn từ SCR-10; bước 2 hiển thị các gói tập; bước 3 chọn gói tập và người mua; bước 4 và 5 do máy chủ xử lý trước khi mở SCR-12) |
| Tác nhân | ACT-05 Lễ tân |
| Boundary AC | AC-B-SellPackageUI |
| DC | DC-SellPackageView (đi cùng DC-SellPackageStore) |
| Loại màn hình | Độc lập |
| Đến từ | SCR-10 (TR-12, mẫu 1); SCR-12 (TR-14, mẫu 1: nút Quay lại) |
| Đi tới | SCR-12 (TR-13, mẫu 4, dữ liệu truyền Gói tập và người mua đã chọn); SCR-10 và các màn hình khác qua menu trái (mẫu 1, ghi ở node START-ACT-05) |

## c) Hình ảnh màn hình

Hình minh hoạ ở trạng thái đã chọn dòng thứ ba và đã nhập người mua. Khi mở màn hình lần đầu không dòng nào được chọn và ô Người mua gói để trống.

```text
+---------------------------------------------------------------------------------------------------------------------+
| [VietFit]                                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------+
| Trang chủ                  | Chọn gói tập và người mua                                                              |
| > Mua hoặc gia hạn gói tập | * Bắt buộc                                                                             |
| Chuyển nhượng gói tập      |                                                                                        |
| Bán vé tập một ngày        | Gói tập *                                                                              |
|                            | +-----+----------+---------------+-------------------+-------------+                   |
|                            | |     | Thời hạn | Loại gói      | Chi nhánh áp dụng |         Giá |                   |
|                            | | ( ) | 1 tháng  | Một chi nhánh | Chi nhánh 2       |   250.000 đ |                   |
|                            | | ( ) | 3 tháng  | Một chi nhánh | Chi nhánh 2       |   650.000 đ |                   |
|                            | | (x) | 6 tháng  | Toàn chuỗi    |                   | 1.200.000 đ |                   |
|                            | | ( ) | 12 tháng | Toàn chuỗi    |                   | 2.100.000 đ |                   |
|                            | +-----+----------+---------------+-------------------+-------------+                   |
|                            |                                                                                        |
|                            | Người mua gói *                                                                        |
|                            | [ Nguyễn Văn An                    ]                                                   |
|                            |                                                                                        |
|                            |                                                          [ Tiếp tục ]                  |
+----------------------------+----------------------------------------------------------------------------------------+
```

Trạng thái lỗi khi nhấn Tiếp tục mà ô Người mua gói trống:

```text
 Người mua gói *
 [                                  ]
 (!) Vui lòng nhập người mua gói.
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit | Trên cùng, cao 56 px, logo trái cách mép 24 px, cao 32 px | UI-STT 11, 12 |
| Menu | Trang chủ, Mua hoặc gia hạn gói tập, Chuyển nhượng gói tập, Bán vé tập một ngày; mục Mua hoặc gia hạn gói tập đang chọn | Trái, rộng 240 px, nền #F4F5F9, mỗi mục cao 44 px | UI-STT 44, 46, 47, 48 |
| Dải thông báo | Không dùng ở màn hình này | - | Lỗi nhập hiện tại trường (UI-STT 58) |
| Tiêu đề màn hình | Chọn gói tập và người mua | Đầu vùng nội dung, 24 px Bold | UI-STT 13 |
| Nội dung | Chú thích * Bắt buộc, nhãn Gói tập, bảng gói, nhãn và ô nhập Người mua gói | Lề 24 px, khoảng cách giữa hai trường 16 px, nhãn cách ô nhập 4 px | UI-STT 11, 30, 32, 34 |
| Hành động | Nút chính Tiếp tục | Cuối nội dung, canh phải, cao 44 px | UI-STT 14, 26. Không có nút phụ |
| Thông điệp | MSG-01 dưới trường lỗi; hộp MSG-10, MSG-11, MSG-12 là lớp phủ modal rộng 480 px | - | UI-STT 54, 58 |

Dữ liệu mẫu: bốn giá gói như SCR-03 (giá 6 tháng Toàn chuỗi 1.200.000 đ theo ví dụ Dữ liệu ra 1 của P04); người mua Nguyễn Văn An theo ví dụ Dữ liệu vào 1 STT 5 của P04.

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Menu trái | Liên kết | Khởi tạo | Hiển thị các mục theo thứ tự: Trang chủ, Mua hoặc gia hạn gói tập (UC-005), Chuyển nhượng gói tập (UC-007), Bán vé tập một ngày (UC-017); đánh dấu mục Mua hoặc gia hạn gói tập đang chọn | UI-STT 44, 46, 47, 48; P02 bảng 4a |
| 3 | Mục menu Trang chủ | Liên kết | Nhấn | Rời màn hình, bỏ dữ liệu đã chọn (đơn chưa tạo), mở SCR-10 (mẫu 1) | UI-STT 46; screen-transition.md node START-ACT-05 |
| 4 | Mục menu Mua hoặc gia hạn gói tập | Liên kết | Nhấn | Ở lại SCR-11, không đổi dữ liệu đã chọn (mục đang chọn) | UI-STT 47 |
| 5 | Mục menu Chuyển nhượng gói tập, Bán vé tập một ngày | Liên kết | Nhấn | Chưa có màn hình đích (UC-007), Chưa có màn hình đích (UC-017); ở lại SCR-11 | UI-STT 44; screen-transition.md node SCR-10 |
| 6 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Chọn gói tập và người mua, sau đó dòng chú thích * Bắt buộc | UI-STT 13, 31 |
| 7 | Bảng gói tập | Bảng | Khởi tạo | Hiển thị mỗi giá gói hiện hành một dòng gồm nút chọn, thời hạn, loại, chi nhánh áp dụng (chỉ với gói Một chi nhánh, nguồn chi nhánh: Q-50) và giá, canh phải ở cột giá. Thứ tự: thời hạn tăng dần, cùng thời hạn thì Một chi nhánh trước Toàn chuỗi. Không dòng nào được chọn sẵn; khi đến từ nút Quay lại của SCR-12 thì giữ dòng và người mua đã chọn. Không có giá gói nào để hiển thị: chưa quy định (Q-103) | UC-005 bước 2, Dữ liệu ra 1 STT 1-4; P08 AC-B-SellPackageUI showPackageOptions; UI-STT 34, 62; Q-50, Q-103 |
| 8 | Dòng của bảng gói tập | Nút chọn | Chọn | Đánh dấu dòng (nền #E8EAF3, thanh trái 4 px, nút chọn đã chọn), bỏ đánh dấu dòng khác, ghi nhận thời hạn và loại của dòng làm Gói tập đã chọn; xoá MSG-01 của bảng nếu đang hiện. Dùng được bằng bàn phím: mũi tên chọn dòng | UC-005 bước 3, Dữ liệu vào 1 STT 1, 2; P08 selectPackage; UI-STT 49 |
| 9 | Ô nhập Người mua gói | Ô nhập | Nhập | Ghi nhận giá trị lễ tân nhập. Cách xác định người mua (nhập hay chọn từ danh sách hội viên) và định dạng: chưa quy định (Q-104) | UC-005 bước 3, Dữ liệu vào 1 STT 5; P08 selectPackage; Q-01, Q-104 |
| 10 | Ô nhập Người mua gói | Ô nhập | Rời trường | Kiểm tra theo mục f); trống thì hiển thị MSG-01 ngay dưới ô nhập; hợp lệ thì xoá lỗi của ô | UI-STT 38, 39; MSG-01 |
| 11 | Nút Tiếp tục | Nút chính | Nhấn | Kiểm tra lại mọi trường theo mục f); trường sai thì hiển thị MSG-01 tại trường và chuyển tiêu điểm tới trường sai đầu tiên theo thứ tự trên màn hình. Hợp lệ thì gửi gói và người mua cho máy chủ; máy chủ xác định ngày bắt đầu (bước 4), tính số tiền phải trả (bước 5), rồi mở SCR-12 với Gói tập và người mua đã chọn (TR-13, mẫu 4). Từ giây thứ 1 hiển thị MSG-10; sự cố hệ thống thì hiển thị MSG-11, mất kết nối thì MSG-12, ở lại SCR-11 và giữ dữ liệu. Nhấn Enter ở ô Người mua gói cũng chạy quy trình này | UC-005 bước 3-6; P08 selectPackage; TR-13; UI-STT 38, 41, 50, 56; MSG-01, MSG-10, MSG-11, MSG-12 |
| 12 | Hộp MSG-11, MSG-12: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-11, giữ nguyên dữ liệu đã chọn | UI-STT 60, 62; MSG-11, MSG-12 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Thời hạn gói | - | Lựa chọn | Hiển thị trong dòng; chọn qua dòng; bắt buộc; không có mặc định; căn trái; chữ #1C1F2A Regular 14 px | Một trong 1, 3, 6, 12 tháng (BR-01) | Hiển thị dạng số nguyên kèm chữ tháng (UI-STT 20) | P04 UC-005 Dữ liệu vào 1 STT 1, Dữ liệu ra 1 STT 1; BR-01 |
| Loại gói | - | Lựa chọn | Hiển thị trong dòng; chọn qua dòng; bắt buộc; không có mặc định; căn trái; chữ #1C1F2A Regular 14 px | Một chi nhánh hoặc Toàn chuỗi (BR-02) | Hiển thị đúng chữ Một chi nhánh hoặc Toàn chuỗi (UI-STT 20) | P04 UC-005 Dữ liệu vào 1 STT 2, Dữ liệu ra 1 STT 2; BR-02 |
| Chi nhánh áp dụng | - | Chữ | Hiển thị trong dòng; bắt buộc: chưa quy định (Q-50); căn trái; chữ #1C1F2A Regular 14 px | Chỉ gói loại Một chi nhánh có giá trị. Ai xác định chi nhánh và có nhập hay chọn ở màn hình này không: chưa quy định (Q-50) | Màn hình chỉ hiển thị giá trị do máy chủ trả; không có điều khiển nhập cho tới khi Q-50 có trả lời | P04 UC-005 Dữ liệu vào 1 STT 3, Dữ liệu ra 1 STT 3; Q-50 |
| Giá gói | 13 | Tiền | Hiển thị trong dòng; căn phải; chữ #1C1F2A Bold 14 px | Số nguyên đồng, phân cách hàng nghìn bằng dấu chấm, kèm dấu cách và chữ đ (UI-STT 19) | Thiết kế: 13 là độ rộng vùng hiển thị tiền (999.999.999 đ), không phải miền giá trị của giá gói. Khuyến mãi không trừ vào giá ở màn hình này (Q-09) | P04 UC-005 Dữ liệu ra 1 STT 4; UI-STT 19 |
| Gói đang có cần gia hạn | Chưa quy định (Q-56) | Chưa quy định (Q-56) | Chưa quy định (Q-56): bắt buộc hay không, nhập hay chọn | Chưa quy định (Q-56) | Không có điều khiển trên hình ảnh cho tới khi Q-56 có trả lời | P04 UC-005 Dữ liệu vào 1 STT 4; Q-56 |
| Người mua gói | Chưa quy định (Q-104) | Chữ (tạm, kiểu chốt theo Q-104) | Nhập; bắt buộc; không có mặc định; căn trái; chữ #1C1F2A Regular 14 px; ô cao 40 px | Chưa quy định định dạng và miền giá trị (Q-01, Q-104). Người mua có tài khoản hội viên hay không: Q-01 | Cột Bắt buộc của P04 ghi Chưa quy định (Q-01); màn hình đặt bắt buộc vì đơn mua ghi nhận một người mua (GL-09) và P07 createOrder nhận người mua. Không chú thích trợ giúp và không placeholder cho tới khi Q-104 có trả lời | P04 UC-005 Dữ liệu vào 1 STT 5; GL-09, GL-19; Q-01, Q-104 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Thời hạn gói, Loại gói (bảng gói tập) | Khi nhấn Tiếp tục. Nhóm dòng chọn một trong nhiều nên không có sự kiện rời trường có nghĩa trước khi người dùng thao tác | (1) Bắt buộc: đã chọn đúng một dòng. (2) Định dạng và miền giá trị: giá trị lấy từ dòng nên luôn thuộc 1, 3, 6, 12 tháng và hai loại gói, không kiểm tra thêm. (3) Quy tắc nghiệp vụ: không có ở màn hình này | MSG-01 (Vui lòng chọn gói tập.) |
| Người mua gói | Khi rời trường và khi nhấn Tiếp tục | (1) Bắt buộc: không để trống. (2) Định dạng và (3) miền giá trị: chưa quy định (Q-104) nên giao diện chưa kiểm tra. (4) Quy tắc nghiệp vụ: người mua có tài khoản hội viên hay không (Q-01), do máy chủ kiểm tra khi nhấn Tiếp tục | MSG-01 (Vui lòng nhập người mua gói.); thông điệp cho lỗi định dạng và lỗi nghiệp vụ: chờ Q-104, Q-01 |
| Chi nhánh áp dụng | Chưa quy định (Q-50) | Chưa quy định (Q-50) | - |
| Gói đang có cần gia hạn | Chưa quy định (Q-56) | Chưa quy định (Q-56) | - |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-11 | Nielsen 6 Nhận biết thay vì nhớ lại (bảng gói) | Vi phạm đã sửa | Áp nguyên UI-STT 33 (hai nhóm nút chọn riêng cho thời hạn và loại gói) thì giá của từng tổ hợp (Dữ liệu ra 1 STT 4) không hiển thị cạnh lựa chọn và có thể chọn tổ hợp chưa có giá gói. Màn hình dùng một bảng, mỗi dòng là một tổ hợp thời hạn và loại kèm giá và nút chọn | Bảng theo UI-STT 34; đề xuất bổ sung ngoại lệ vào UI-STT 33 đã ghi ở SCR-03 |
| SCR-11 | Nielsen 6 Nhận biết thay vì nhớ lại (người mua) | Vi phạm còn mở | Lễ tân phải tự nhập thông tin người mua mà đặc tả chưa nêu thông tin nào dùng để nhận ra người mua và có danh sách để chọn hay không | Q-104, Q-01 |
| SCR-11 | Nielsen 1 Hiển thị trạng thái hệ thống | Vi phạm còn mở | Chưa quy định màn hình khi không có giá gói nào để hiển thị | Q-103 |
| SCR-11 | Nielsen 7 Linh hoạt và hiệu quả | Vi phạm còn mở | Đặc tả có Dữ liệu vào Gói đang có cần gia hạn nhưng chưa quy định cách chỉ định, nên màn hình chưa có điều khiển để lễ tân gia hạn một gói cụ thể | Q-56; không tự thêm điều khiển |
| SCR-11 | Baymard: form một cột, nhãn trên ô nhập, không placeholder thay nhãn | Đạt | Bảng gói rồi ô Người mua gói xếp một cột; nhãn Người mua gói nằm trên ô nhập; ô nhập không có placeholder | - |
| SCR-11 | Baymard: kiểm tra khi rời trường, thông điệp lỗi cạnh trường | Đạt | Ô Người mua gói kiểm tra bắt buộc khi rời trường, MSG-01 ngay dưới ô; nhấn Tiếp tục chuyển tiêu điểm tới trường sai đầu tiên | - |
| SCR-11 | WCAG 1.3.1 Thông tin và quan hệ | Đạt | Bảng gói dùng th cho tiêu đề cột, mỗi dòng có nút chọn gắn nhãn đọc thành thời hạn, loại, giá; menu có aria-current ở mục đang chọn | - |
| SCR-11 | WCAG 1.4.10 Reflow (web) | Đạt | Dưới 1024 px bảng 5 cột cuộn ngang trong khung riêng của bảng, nội dung xếp một cột (UI-STT 3) | - |
| SCR-11 | WCAG 2.1.1 Bàn phím | Đạt | Mũi tên chọn dòng của bảng, Tab tới ô Người mua gói và nút Tiếp tục, Enter ở ô Người mua gói kích hoạt nút chính (UI-STT 49, 50) | - |
| SCR-11 | WCAG 3.2.3 Điều hướng nhất quán | Đạt | Menu có cùng thứ tự các mục với SCR-10, SCR-12, SCR-13, SCR-14 (UI-STT 46, 48) | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-01 (mẫu Vui lòng {chọn hoặc nhập} {tên trường} với tên trường là gói tập hoặc người mua gói), MSG-10, MSG-11, MSG-12.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-104 | Lễ tân xác định người mua gói tại quầy bằng thông tin nào (số điện thoại, họ tên hoặc cả hai) và bằng cách nhập hay chọn từ danh sách hội viên; thông tin đó có độ dài, định dạng gì, và hệ thống phản hồi thế nào khi không tìm thấy người mua? (Nhập số điện thoại / Nhập họ tên rồi chọn từ danh sách / Khác - nêu rõ) | SCR-11 (trường Người mua gói: kiểu điều khiển, độ dài, MSG), SCR-12; P04 UC-005 Dữ liệu vào 1 STT 5 | P04 UC-005 Dữ liệu vào 1 STT 5 "Người mua gói" không nêu bắt buộc và điều kiện hợp lệ (Q-01 chỉ hỏi người mua có tài khoản hay không); P05 GL-19 nêu hội viên đăng ký bằng số điện thoại và họ tên |

Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-01 (người mua tại quầy có tài khoản không), Q-103 (màn hình khi không có giá gói, ghi ở SCR-03), Q-50 (chi nhánh áp dụng), Q-56 (gói đang có cần gia hạn), Q-09 (cách áp dụng khuyến mãi), Q-47 (xác thực của lễ tân), Q-82 (tên gọi mặt hàng được bán).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Không có. Đề xuất sửa UI-STT 33 áp dụng cả cho SCR-11 và đã ghi ở SCR-03; đề xuất bổ sung Người mua gói vào Dữ liệu ra 2 đã ghi ở SCR-04.

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 3, 7: Chi nhánh áp dụng, Gói đang có cần gia hạn và Người mua gói chưa có bắt buộc, điều kiện hợp lệ, độ dài (Q-50, Q-56, Q-01, Q-104). Độ dài và định dạng của Người mua gói ghi Chưa quy định kèm mã Q; chỉ có bắt buộc là quyết định của màn hình (căn cứ GL-09), cần người dùng xác nhận cùng Q-01.
- Target 9: có 4 dòng Vi phạm còn mở (gắn Q-104, Q-01, Q-103, Q-56) đều do đặc tả chưa quy định; không có vi phạm WCAG AA chưa xử lý.
- Thứ tự trường theo UI-STT 32 đặt bảng gói trước ô Người mua gói (theo thứ tự Dữ liệu vào của P04); nếu lễ tân thường chọn người mua trước thì đổi thứ tự cùng lúc với Q-104.
- Menu có hai mục chưa có màn hình đích (UC-007, UC-017) hiển thị theo UI-STT 44 và không thao tác được cho tới khi các use case này được đặc tả.
