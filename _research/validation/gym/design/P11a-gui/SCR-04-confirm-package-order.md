# P11a - SCR-04 Xác nhận đơn mua - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 2) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE, MUC_CHI_TIET); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Quy tắc nghiệp vụ, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, Mục 4, BR-01 đến BR-05, BR-38); P07-uc-analysis/UC-005 (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4); P11a-gui/ui-standards.md, screen-list.md, screen-transition.md (phiên bản 1.0, giai đoạn 1); chưa có SCR nào trước lần chạy này nên không có mục h) của SCR khác. Mã Q, ASM lớn nhất do người dùng cung cấp trước lần chạy (Q-102, P11b đã chạy; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả; lần chạy này cấp Q-103, Q-104. CHE_DO_CHAY: Giai đoạn 2: các màn hình của UC-005 (SCR-03, SCR-04, SCR-05, SCR-11, SCR-12, SCR-13, SCR-14; màn hình điều hướng SCR-02, SCR-10 để lần chạy sau); lần chạy này không phải lần giai đoạn 2 cuối cùng. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (Ngày tạo để trống vì THONG_TIN_TAI_LIEU không nêu). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất chỉ đổi cấu trúc thiết kế (của P10, P11a giai đoạn 1, P11b) thì các bước đó không chạy lại |
| Phạm vi | SCR-04 (UC-005, ACT-02 Hội viên, ứng dụng di động) |
| Mã Q, ASM cuối đã cấp | Q-104; ASM: chưa cấp (chế độ NGHIEM_NGAT) |
| Ngày tạo |  |
| Người duyệt | Giám đốc vận hành chuỗi |
| Người kiểm tra | Trưởng nhóm thiết kế |
| Người phụ trách | Nhóm phân tích VietFit |

## b) Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| SCR | SCR-04 Xác nhận đơn mua (Confirm package order) |
| UC | UC-005 Mua hoặc gia hạn gói tập |
| Bước UC | 6-7, 9-10, 9a2, 10a (bước 8 tạo đơn chờ thanh toán và bước 11-12 do máy chủ xử lý) |
| Tác nhân | ACT-02 Hội viên |
| Boundary AC | AC-B-PurchaseOrRenewPackageUI |
| DC | DC-PurchaseOrRenewPackageView (đi cùng DC-PurchaseOrRenewPackageStore) |
| Loại màn hình | Phụ thuộc có dữ liệu |
| Đến từ | SCR-03 (TR-04, mẫu 4, dữ liệu Gói tập đã chọn) |
| Đi tới | SCR-05 (TR-06, mẫu 4, dữ liệu Đơn mua đã thanh toán); SCR-03 (TR-05, mẫu 1: nút Quay lại, hoặc nút Chọn lại gói tập của MSG-02); SCR-02 (nút Trang chủ, mẫu 1, ghi ở node START-ACT-02) |

## c) Hình ảnh màn hình

Trạng thái ban đầu:

```text
+--------------------------------------+
| [VietFit]                  [Trang chủ]|
|--------------------------------------|
| Xác nhận đơn mua                     |
|                                      |
| Gói tập        6 tháng, Toàn chuỗi   |
| Ngày bắt đầu              01/12/2026 |
| Số tiền phải trả         1.080.000 đ |
|                                      |
| [          Xác nhận mua            ] |
| [            Quay lại              ] |
+--------------------------------------+
```

Trạng thái chờ kết quả thanh toán (MSG-04 là lớp phủ modal, nền phủ đen 40%, không có nút):

```text
+--------------------------------------+
| [VietFit]                  [Trang chủ]|
|######################################|
|####+----------------------------+####|
|####|          (o) xoay          |####|
|####| Đang chờ kết quả thanh toán|####|
|####+----------------------------+####|
|######################################|
+--------------------------------------+
```

| Vùng | Nội dung | Vị trí | Ghi chú |
|---|---|---|---|
| Thanh tiêu đề | Logo VietFit, nút Trang chủ | Trên cùng, cao 56 dp, logo trái, Trang chủ phải | UI-STT 10, 12, 45 |
| Dải thông báo | Không dùng ở màn hình này | - | Kết quả thanh toán hiển thị bằng hộp thông điệp |
| Tiêu đề màn hình | Xác nhận đơn mua | Đầu vùng nội dung, 20 sp Bold | UI-STT 13 |
| Nội dung | Ba dòng tóm tắt đơn mua: nhãn bên trái, giá trị bên phải | Lề 16 dp, khoảng cách giữa hai dòng 16 dp | UI-STT 10, 76 |
| Hành động | Nút chính Xác nhận mua, nút phụ Quay lại | Cuối nội dung, xếp dọc, rộng 328 dp, cao 48 dp, cách nhau 8 dp | UI-STT 14, 26, 27 |
| Thông điệp | Hộp MSG-02, MSG-03, MSG-04, MSG-10, MSG-11, MSG-12 | Lớp phủ modal giữa màn hình, rộng 312 dp | UI-STT 54, 55 |

Dữ liệu mẫu: gói 6 tháng Toàn chuỗi chọn ở SCR-03 (giá 1.200.000 đ), ngày bắt đầu 01/12/2026 là ngày ngay sau ngày hết hạn 30/11/2026 của gói cũ (BR-03, ví dụ Dữ liệu vào 1 STT 4 của P04), số tiền phải trả 1.080.000 đ theo ví dụ Dữ liệu ra 2 của P04 (giá gói trừ khuyến mãi 10%, trong giới hạn 20% của BR-38).

## d) Danh sách chức năng

| STT | Điều khiển (Control) | Loại | Thao tác (Operation) | Chức năng (Function) | Nguồn |
|---|---|---|---|---|---|
| 1 | Logo VietFit | Vùng hiển thị | Khởi tạo | Hiển thị logo ở góc trên bên trái thanh tiêu đề, văn bản thay thế là VietFit | UI-STT 12, 69 |
| 2 | Nút Trang chủ | Nút | Nhấn | Khi đơn chưa tạo: rời màn hình, bỏ dữ liệu đã chọn, mở SCR-02 (mẫu 1). Khi hộp MSG-04 đang hiển thị: nút không thao tác được vì hộp là modal; việc hội viên rời màn hình trong lúc chờ thanh toán: Q-96 | UI-STT 45; screen-transition.md node START-ACT-02; Q-96 |
| 3 | Nút quay lại của hệ thống (Android) hoặc cử chỉ quay lại (iOS) | Nút | Nhấn | Khi đơn chưa tạo: làm giống nút Quay lại (mở SCR-03 giữ gói đã chọn). Khi hộp MSG-04 đang hiển thị: không có tác dụng vì hộp không có nút; sau khi đơn đã tạo không đưa về màn hình này | UI-STT 15, 51; Q-57 |
| 4 | Tiêu đề màn hình | Vùng hiển thị | Khởi tạo | Hiển thị Xác nhận đơn mua | UI-STT 13 |
| 5 | Dòng Gói tập | Vùng hiển thị | Khởi tạo | Hiển thị thời hạn và loại của gói đã chọn ở SCR-03 | UC-005 bước 6, Dữ liệu ra 2 STT 1 |
| 6 | Dòng Ngày bắt đầu | Vùng hiển thị | Khởi tạo | Hiển thị ngày bắt đầu của gói mới do máy chủ xác định ở bước 4 (BR-03). Ngày bắt đầu khi mua gói mới, gia hạn gói đã hết hạn, gia hạn gói đang bảo lưu: chưa quy định (Q-51, Q-24, Q-52) | UC-005 bước 4, 6, Dữ liệu ra 2 STT 2; BR-03; Q-51, Q-24, Q-52 |
| 7 | Dòng Số tiền phải trả | Vùng hiển thị | Khởi tạo | Hiển thị số tiền phải trả do máy chủ tính ở bước 5 (giá gói trừ mức giảm khuyến mãi áp dụng, cách áp dụng: Q-09) | UC-005 bước 5, 6, Dữ liệu ra 2 STT 3; GL-37; Q-09 |
| 8 | Nút Xác nhận mua | Nút chính | Nhấn | Nhãn chuyển thành Đang xử lý và khoá nhấn lại (UI-STT 41); từ giây thứ 1 hiển thị MSG-10. Máy chủ tạo đơn mua ở trạng thái chờ thanh toán (bước 8) và gửi đơn cho cổng thanh toán (bước 9); khi máy chủ báo đã gửi đơn thì hiển thị MSG-04 và chờ kết quả trong 15 phút (BR-04). Giao diện hội viên thanh toán trên cổng: Q-96. Sự cố hệ thống thì hiển thị MSG-11, mất kết nối thì MSG-12, ở lại SCR-04 | UC-005 bước 7-9; BR-04; UI-STT 41, 56; MSG-04, MSG-10, MSG-11, MSG-12; Q-96 |
| 9 | Nút Quay lại | Nút phụ | Nhấn | Mở SCR-03 và giữ gói đã chọn (TR-05, mẫu 1). Chỉ nhấn được khi đơn chưa tạo; khi MSG-04 hiển thị thì không thao tác được | UC-005 bước 7; UI-STT 15, 62; TR-05 |
| 10 | Hộp MSG-04 (Đang chờ kết quả thanh toán) | Vùng hiển thị | Nhận kết quả | Giao dịch thanh toán thành công trong 15 phút: đóng hộp và mở SCR-05 với Đơn mua đã thanh toán (TR-06, mẫu 4) | UC-005 bước 10, 11, 13; BR-04; TR-06; MSG-04 |
| 11 | Hộp MSG-04 (Đang chờ kết quả thanh toán) | Vùng hiển thị | Nhận kết quả | Cổng thanh toán báo giao dịch không thành công (luồng 10a): đóng hộp MSG-04 và hiển thị MSG-03 | UC-005 luồng 10a; MSG-03; Q-13, Q-53 |
| 12 | Hộp MSG-04 (Đang chờ kết quả thanh toán) | Vùng hiển thị | Nhận kết quả | Máy chủ báo đơn đã bị huỷ vì quá 15 phút (luồng 9a): đóng hộp MSG-04 và hiển thị MSG-02 | UC-005 luồng 9a, 9a1, 9a2; BR-04; MSG-02; Q-25, Q-53 |
| 13 | Hộp MSG-03: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-04. Việc thanh toán lại trên cùng đơn hay tạo đơn mới, và trạng thái của nút Xác nhận mua sau đó: chờ Q-13 | UC-005 luồng 10a; MSG-03; Q-13 |
| 14 | Hộp MSG-02: nút Chọn lại gói tập | Nút chính | Nhấn | Đóng hộp, mở SCR-03 (TR-05, mẫu 1) và không chọn sẵn thẻ nào vì đơn đã bị huỷ | UC-005 luồng 9a2; MSG-02; TR-05 |
| 15 | Hộp MSG-11, MSG-12: nút Đóng | Nút | Nhấn | Đóng hộp, ở lại SCR-04, giữ nguyên dữ liệu đã chọn | UI-STT 60, 62; MSG-11, MSG-12 |

## e) Định nghĩa thuộc tính trường

| Mục (Item name) | Số ký tự tối đa (Number of digits) | Kiểu (Type) | Thuộc tính trường (Field attribute) | Ràng buộc dữ liệu | Ghi chú (Remarks) | Nguồn |
|---|---|---|---|---|---|---|
| Gói tập | - | Chữ | Hiển thị; căn phải; chữ #1C1F2A Regular 16 sp | Thời hạn thuộc 1, 3, 6, 12 tháng (BR-01), loại thuộc Một chi nhánh hoặc Toàn chuỗi (BR-02); dạng "{n} tháng, {loại}" | Gói loại Một chi nhánh thêm tên chi nhánh áp dụng trong ngoặc (UI-STT 76; nguồn chi nhánh: Q-50) | P04 UC-005 Dữ liệu ra 2 STT 1; BR-01, BR-02; UI-STT 76 |
| Ngày bắt đầu | 10 | Ngày | Hiển thị; căn phải; chữ #1C1F2A Regular 16 sp | Định dạng dd/MM/yyyy. Gia hạn khi gói cũ còn hiệu lực: ngay sau ngày hết hạn của gói cũ (BR-03); các nhánh khác chưa quy định (Q-51, Q-24, Q-52) | - | P04 UC-005 Dữ liệu ra 2 STT 2; BR-03 |
| Số tiền phải trả | 13 | Tiền | Hiển thị; căn phải; chữ #1C1F2A Bold 16 sp | Số nguyên đồng, phân cách hàng nghìn bằng dấu chấm, kèm dấu cách và chữ đ | Thiết kế: 13 là độ rộng vùng hiển thị tiền (999.999.999 đ), không phải miền giá trị. Số tiền = giá gói trừ mức giảm khuyến mãi (GL-37), cách áp dụng chờ Q-09 | P04 UC-005 Dữ liệu ra 2 STT 3; GL-37; UI-STT 19 |

## f) Kiểm tra dữ liệu nhập

| Trường | Thời điểm kiểm tra | Kiểm tra | MSG khi lỗi |
|---|---|---|---|
| Không có trường nhập | - | Màn hình chỉ hiển thị tóm tắt đơn mua và hai nút; dữ liệu đã được kiểm tra ở SCR-03. Quy tắc nghiệp vụ liên quan đơn mua do máy chủ kiểm tra khi nhấn Xác nhận mua | Sự cố hệ thống MSG-11; mất kết nối MSG-12 |

## g) Đánh giá chuẩn

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| SCR-04 | Nielsen 5 Ngăn lỗi | Đạt | Màn hình xác nhận riêng cho dữ liệu tài chính (UI-STT 74): tóm tắt, nút Quay lại sửa, nút Xác nhận mua; nút khoá nhấn lại khi đang xử lý để không gửi hai lần cùng một yêu cầu (UI-STT 41) | - |
| SCR-04 | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | Nút đổi sang Đang xử lý, MSG-10 từ giây thứ 1, MSG-04 khi chờ thanh toán, kết quả bằng MSG-02, MSG-03 hoặc SCR-05 | - |
| SCR-04 | Nielsen 3 Người dùng kiểm soát và tự do | Vi phạm còn mở | Khi MSG-04 hiển thị hội viên không có nút nào để huỷ hoặc rời; đặc tả không có thao tác huỷ đơn chưa thanh toán (Q-57) và chưa rõ giao diện thanh toán (Q-96) | Q-57, Q-96; không tự thêm nút huỷ |
| SCR-04 | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Vi phạm còn mở | MSG-03 chưa nêu được việc làm tiếp sau khi giao dịch không thành công vì đặc tả chờ Q-13 | Q-13 |
| SCR-04 | Nielsen 1 Hiển thị trạng thái hệ thống (tóm tắt đơn) | Vi phạm còn mở | Giá gói ở SCR-03 là 1.200.000 đ còn số tiền phải trả là 1.080.000 đ; Dữ liệu ra 2 không có mức giảm khuyến mãi nên chênh lệch không được giải thích trên màn hình | Q-09; đề xuất sửa P04 Dữ liệu ra 2 (mục Đề xuất sửa artifact trước); không tự thêm trường |
| SCR-04 | Baymard: hiển thị tóm tắt đơn và tổng tiền trong bước thanh toán | Đạt | Ba dòng tóm tắt gồm gói tập, ngày bắt đầu, số tiền phải trả, kèm nút Quay lại sửa | - |
| SCR-04 | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | Có tóm tắt để kiểm tra, sửa được bằng Quay lại, xác nhận bằng nút đặt tên theo hành động Xác nhận mua (UI-STT 75) | - |
| SCR-04 | WCAG 3.3.7 Không bắt nhập lại | Đạt | Gói đã chọn ở SCR-03 được chuyển sang và được giữ khi dùng Quay lại | - |
| SCR-04 | WCAG 4.1.3 Thông điệp trạng thái | Đạt | MSG-04 và MSG-10 có vai trò status, được đọc mà không chuyển tiêu điểm (UI-STT 57) | - |
| SCR-04 | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | Khi mở MSG-02 hoặc MSG-03, tiêu điểm vào nút duy nhất của hộp; khi đóng trở về nút Xác nhận mua (UI-STT 52) | - |
| SCR-04 | Material Design (Android): một hành động chính | Đạt | Một nút chính Xác nhận mua ở trên, nút phụ Quay lại ở dưới, cao 48 dp | - |
| SCR-04 | Apple HIG (iOS): điều hướng quay lại theo nền tảng | Đạt | Cử chỉ quay lại làm giống nút Quay lại khi đơn chưa tạo (UI-STT 15) | - |

Tiêu chí không có dòng ở bảng này không có bằng chứng riêng của màn hình, đạt theo ui-standards.md mục 3.

## h) Thông điệp mới

Không có. Màn hình dùng MSG-02, MSG-03, MSG-04, MSG-10, MSG-11, MSG-12 của ui-standards.md.

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi đã cấp ở bước trước và làm đổi màn hình này (không chép lại): Q-96 (giao diện thanh toán trực tuyến), Q-13 (thanh toán lại sau giao dịch không thành công), Q-57 (huỷ đơn chưa thanh toán), Q-25 (cách tính 15 phút), Q-09 (cách áp dụng khuyến mãi), Q-50 (chi nhánh áp dụng), Q-51, Q-24, Q-52 (ngày bắt đầu các nhánh), Q-53 (kênh báo kết quả không thành công), Q-14 (kết quả đến sau khi đơn bị huỷ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-005 Dữ liệu ra 2 (bước 6) | Dữ liệu ra 2 không có mức giảm khuyến mãi nên số tiền phải trả khác giá gói ở bước 2 mà màn hình không giải thích được (Q-09). Dữ liệu ra 2 cũng không có Chi nhánh áp dụng và Người mua gói trong khi UI-STT 76 yêu cầu tóm tắt đơn có hai thông tin này | Khi Q-09 có trả lời, thêm trường mức giảm vào Dữ liệu ra 2; khi Q-50, Q-01 có trả lời, thêm Chi nhánh áp dụng và Người mua gói vào Dữ liệu ra 2. Chưa áp dụng (chờ Q-09, Q-50, Q-01) |

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 3, 4: mọi trường và nút truy được về Dữ liệu ra 2, luồng 7, 9, 9a, 10, 10a; MSG-02, MSG-03, MSG-04 được tham chiếu ở dòng 10 đến 14 của mục d).
- Target 9: 3 dòng Vi phạm còn mở (Nielsen 3 gắn Q-57 và Q-96, Nielsen 9 gắn Q-13, Nielsen 1 gắn Q-09) đều do đặc tả chưa quy định; không có vi phạm WCAG AA chưa xử lý.
- Thao tác Nhận kết quả được dùng cho cả trường hợp quá 15 phút (luồng 9a) vì bộ đếm 15 phút nằm ở máy chủ (BR-04), màn hình không đếm thời gian; giao diện nhận kết quả bằng cách nào (đẩy hay hỏi lại) là quyết định của P12.
- Sau khi đơn đã tạo mà hội viên rời ứng dụng, hành vi khi quay lại chưa quy định (Q-96).
