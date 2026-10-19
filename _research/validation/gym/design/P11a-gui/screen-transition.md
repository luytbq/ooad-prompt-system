# P11a - Sơ đồ dịch chuyển màn hình - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 1) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; Bảng 4a); P04-uc-specs/UC-005, UC-010, UC-015, UC-018 (phiên bản 1.0; luồng sự kiện, Dữ liệu vào và ra, Câu hỏi mở); P05-glossary.md (phiên bản 1.0; Thuật ngữ, Định nghĩa, Từ đồng nghĩa không dùng); P06-supplementary-spec.md (phiên bản 1.0; Mục 3 đến Mục 6); P07-uc-analysis/ bốn file (phiên bản 1.0; message của tác nhân người và boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (phiên bản 1.0; F3); P09-architecture.md (phiên bản 1.0; F3, F5); P10-design-elements.md (phiên bản 1.0; F3, F4, Đề xuất sửa artifact trước, Vấn đề còn mở). Mã Q, ASM lớn nhất do người dùng cung cấp (Q-94; chưa có ASM), quét lại ở thư mục đầu ra cho cùng kết quả. CHE_DO_CHAY: Giai đoạn 1. THIET_BI_HIEN_THI: ứng dụng di động Android và iOS cho hội viên và huấn luyện viên (điện thoại từ 360 x 640 dp, hướng dọc, cảm ứng), ứng dụng web cho lễ tân, quản lý chi nhánh và giám đốc chuỗi (trình duyệt máy tính từ 1366 x 768, chuột và bàn phím). NHAN_DIEN_THUONG_HIEU: màu chủ đạo #E4572E, màu phụ #29335C, phông Be Vietnam Pro, logo VietFit ở góc trên bên trái. MAU_DAC_TA_MAN_HINH: Không có. XUAT_HTML: Không. THONG_TIN_TAI_LIEU: Người phụ trách: Nhóm phân tích VietFit; Người kiểm tra: Trưởng nhóm thiết kế; Người duyệt: Giám đốc vận hành chuỗi (dùng ở đặc tả màn hình giai đoạn 2). YEU_CAU_BO_SUNG: phạm vi đặc tả và phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; các use case khác của P02 chưa đặc tả, màn hình của chúng chỉ là lối vào trên màn hình điều hướng; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; ba đề xuất của P10 cho P08, P09 chỉ đổi cấu trúc thiết kế nên P08, P09 không chạy lại |
| Phạm vi | Toàn hệ thống (giai đoạn 1): 6 tác nhân người có màn hình, 16 màn hình, 18 dịch chuyển |
| Mã Q, ASM cuối đã cấp | Q-99; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Bảng Node

| ID (SCR, START-ACT-nn, P-ACT-nn) | Loại (Screen / Start / Partition) | Nhãn (tên màn hình) | Stereotype (Loại màn hình ở F2) | Thuộc về (tác nhân) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Người quan tâm (ACT-01) | - | ACT-01 Người quan tâm | Phân vùng chứa các màn hình của ACT-01 | 20 | 20 | 1660 | 120 |
| START-ACT-01 | Start | Bắt đầu: Người quan tâm | - | ACT-01 Người quan tâm | Mở ứng dụng khi chưa có phiên làm việc (Q-99). Tác nhân chỉ có SCR-01 nên không có menu tới màn hình khác. | 100 | 60 | 40 | 40 |
| SCR-01 | Screen | Trang chủ Người quan tâm (Prospect home) | Độc lập | ACT-01 Người quan tâm | Lối vào UC-001, UC-002, UC-003: Chưa có màn hình đích. Màn hình kết thúc của sơ đồ cho tới khi các use case này có màn hình. Lối vào Đăng nhập: Q-99. | 200 | 50 | 160 | 60 |
| P-ACT-02 | Partition | Hội viên (ACT-02) | - | ACT-02 Hội viên | Phân vùng chứa các màn hình của ACT-02 | 20 | 140 | 1660 | 300 |
| START-ACT-02 | Start | Bắt đầu: Hội viên | - | ACT-02 Hội viên | Sau khi có phiên làm việc (tiền điều kiện UC-005, UC-010; Q-99). Mọi màn hình trừ SCR-02 có nút Trang chủ tới SCR-02, mẫu 1. | 100 | 190 | 40 | 40 |
| SCR-02 | Screen | Trang chủ Hội viên (Member home) | Độc lập | ACT-02 Hội viên | Lối vào có màn hình đích: UC-005 --> SCR-03 (TR-03), UC-010 --> SCR-06 (TR-07). Chưa có màn hình đích: UC-006, UC-011, UC-012, UC-018 (mã QR: Q-97), UC-019, UC-020, UC-023, UC-025. UC-004 không là lối vào ở đây (Q-99). | 200 | 180 | 160 | 60 |
| SCR-03 | Screen | Chọn gói tập (Select membership package) | Độc lập | ACT-02 Hội viên | Màn hình thao tác. Lối ra: TR-04. | 520 | 180 | 160 | 60 |
| SCR-04 | Screen | Xác nhận đơn mua (Confirm package order) | Phụ thuộc có dữ liệu | ACT-02 Hội viên | Màn hình xác nhận. Lối ra: TR-05 (Quay lại, chỉ khi đơn chưa tạo; Chọn lại gói tập ở MSG-02), TR-06. Hộp MSG-04 hiển thị khi chờ thanh toán; giao diện thanh toán: Q-96; kết cục MSG-03: Q-13. | 840 | 180 | 160 | 60 |
| SCR-05 | Screen | Gói tập đã kích hoạt (Activated membership package) | Phụ thuộc có dữ liệu | ACT-02 Hội viên | Màn hình kết thúc của UC-005 (hội viên); rời bằng nút Trang chủ. | 1160 | 180 | 160 | 60 |
| SCR-06 | Screen | Chọn lớp nhóm (Select group class) | Độc lập | ACT-02 Hội viên | Màn hình thao tác. MSG-05 đến MSG-08 hiển thị tại màn hình này khi bị từ chối (ở lại SCR-06); MSG-09 là hộp xác nhận modal không phải SCR, dẫn tới SCR-08 ở TR-09. Lối ra: TR-08, TR-09. | 520 | 320 | 160 | 60 |
| SCR-07 | Screen | Chỗ đã đặt (Booked class spot) | Phụ thuộc có dữ liệu | ACT-02 Hội viên | Màn hình kết thúc của UC-010 (đặt chỗ thành công); rời bằng nút Trang chủ. | 840 | 320 | 160 | 60 |
| SCR-08 | Screen | Vị trí trong danh sách chờ (Waitlist position) | Phụ thuộc có dữ liệu | ACT-02 Hội viên | Màn hình kết thúc của UC-010 (vào danh sách chờ); rời bằng nút Trang chủ. | 1160 | 320 | 160 | 60 |
| P-ACT-04 | Partition | Huấn luyện viên (ACT-04) | - | ACT-04 Huấn luyện viên | Phân vùng chứa các màn hình của ACT-04 | 20 | 440 | 1660 | 120 |
| START-ACT-04 | Start | Bắt đầu: Huấn luyện viên | - | ACT-04 Huấn luyện viên | Sau khi có phiên làm việc (Q-47, Q-92). Mọi màn hình có nút Trang chủ tới SCR-09, mẫu 1 (hiện chỉ có SCR-09). | 100 | 470 | 40 | 40 |
| SCR-09 | Screen | Trang chủ Huấn luyện viên (Trainer home) | Độc lập | ACT-04 Huấn luyện viên | Lối vào UC-021, UC-024, UC-025: Chưa có màn hình đích. Màn hình kết thúc của sơ đồ cho tới khi các use case này có màn hình. | 200 | 460 | 160 | 60 |
| P-ACT-05 | Partition | Lễ tân (ACT-05) | - | ACT-05 Lễ tân | Phân vùng chứa các màn hình của ACT-05 | 20 | 560 | 1660 | 140 |
| START-ACT-05 | Start | Bắt đầu: Lễ tân | - | ACT-05 Lễ tân | Sau khi có phiên làm việc (Q-47). Mọi màn hình có menu tới SCR-10, SCR-11, mẫu 1. | 100 | 610 | 40 | 40 |
| SCR-10 | Screen | Trang chủ Lễ tân (Receptionist home) | Độc lập | ACT-05 Lễ tân | Lối vào có màn hình đích: UC-005 --> SCR-11 (TR-12). Chưa có màn hình đích: UC-007, UC-017. | 200 | 600 | 160 | 60 |
| SCR-11 | Screen | Chọn gói tập và người mua (Select package and buyer) | Độc lập | ACT-05 Lễ tân | Màn hình thao tác. Lối ra: TR-13. | 520 | 600 | 160 | 60 |
| SCR-12 | Screen | Xác nhận đơn bán tại quầy (Confirm counter sale order) | Phụ thuộc có dữ liệu | ACT-05 Lễ tân | Màn hình xác nhận. Lối ra: TR-14 (Quay lại, chỉ khi đơn chưa tạo), TR-15. | 840 | 600 | 160 | 60 |
| SCR-13 | Screen | Thu tiền tại quầy (Collect payment at counter) | Phụ thuộc có dữ liệu | ACT-05 Lễ tân | Đơn đã tạo nên không có Quay lại. Lối ra: TR-16. Hình thức thu: Q-98. | 1160 | 600 | 160 | 60 |
| SCR-14 | Screen | Gói tập đã kích hoạt tại quầy (Activated package at counter) | Phụ thuộc có dữ liệu | ACT-05 Lễ tân | Màn hình kết thúc của UC-005 (lễ tân); rời bằng menu. | 1480 | 600 | 160 | 60 |
| P-ACT-06 | Partition | Quản lý chi nhánh (ACT-06) | - | ACT-06 Quản lý chi nhánh | Phân vùng chứa các màn hình của ACT-06 | 20 | 700 | 1660 | 120 |
| START-ACT-06 | Start | Bắt đầu: Quản lý chi nhánh | - | ACT-06 Quản lý chi nhánh | Sau khi có phiên làm việc (Q-47). Mọi màn hình có menu tới SCR-15, mẫu 1. | 100 | 730 | 40 | 40 |
| SCR-15 | Screen | Trang chủ Quản lý chi nhánh (Branch manager home) | Độc lập | ACT-06 Quản lý chi nhánh | Lối vào UC-009, UC-014: Chưa có màn hình đích. Màn hình kết thúc của sơ đồ cho tới khi các use case này có màn hình. | 200 | 720 | 160 | 60 |
| P-ACT-07 | Partition | Giám đốc chuỗi (ACT-07) | - | ACT-07 Giám đốc chuỗi | Phân vùng chứa các màn hình của ACT-07 | 20 | 820 | 1660 | 120 |
| START-ACT-07 | Start | Bắt đầu: Giám đốc chuỗi | - | ACT-07 Giám đốc chuỗi | Sau khi có phiên làm việc (Q-47). Mọi màn hình có menu tới SCR-16, mẫu 1. | 100 | 850 | 40 | 40 |
| SCR-16 | Screen | Trang chủ Giám đốc chuỗi (Chain director home) | Độc lập | ACT-07 Giám đốc chuỗi | Lối vào UC-026, UC-027, UC-028: Chưa có màn hình đích. Màn hình kết thúc của sơ đồ cho tới khi các use case này có màn hình. | 200 | 840 | 160 | 60 |

Toạ độ x, y là toạ độ tuyệt đối trên trang; trong file .drawio, node con của partition dùng toạ độ tương đối với partition. Khách vãng lai (ACT-03) không dùng phần mềm nên không có Start và partition.

## 2. Bảng Edge

| ID | Nguồn | Đích | Mẫu dịch chuyển | Sự kiện kích hoạt | Điều kiện | Dữ liệu truyền | UC bước | Điểm uốn |
|---|---|---|---|---|---|---|---|---|
| TR-01 | START-ACT-01 | SCR-01 | 1 Dịch chuyển đơn giản | Mở ứng dụng | Chưa có phiên làm việc (Q-99) | - | - | - |
| TR-02 | START-ACT-02 | SCR-02 | 1 Dịch chuyển đơn giản | Sau khi có phiên làm việc | Hội viên đã xác thực (tiền điều kiện UC-005, UC-010) | - | UC-005, UC-010 Tiền điều kiện | - |
| TR-03 | SCR-02 | SCR-03 | 1 Dịch chuyển đơn giản | Nhấn mục Mua hoặc gia hạn gói tập | - | - | UC-005 bước 1 | - |
| TR-04 | SCR-03 | SCR-04 | 4 Dịch chuyển sang màn hình phụ thuộc có dữ liệu | Nhấn Tiếp tục | Đã chọn thời hạn và loại gói (thiếu thì MSG-01) | Gói tập đã chọn | UC-005 bước 3, 6 | - |
| TR-05 | SCR-04 | SCR-03 | 1 Dịch chuyển đơn giản | Nhấn Quay lại; hoặc nhấn Chọn lại gói tập trong MSG-02 | Đơn chưa tạo (Quay lại); đơn bị huỷ sau 15 phút (MSG-02) | - | UC-005 bước 7, 9a2 | - |
| TR-06 | SCR-04 | SCR-05 | 4 Dịch chuyển sang màn hình phụ thuộc có dữ liệu | Nhận kết quả | Thanh toán thành công trong 15 phút (BR-04) | Đơn mua đã thanh toán | UC-005 bước 10, 11, 13 | - |
| TR-07 | SCR-02 | SCR-06 | 1 Dịch chuyển đơn giản | Nhấn mục Đặt chỗ lớp nhóm | - | - | UC-010 bước 1 | (280,350) |
| TR-08 | SCR-06 | SCR-07 | 4 Dịch chuyển sang màn hình phụ thuộc có dữ liệu | Nhấn Đặt chỗ | Qua kiểm tra bước 4 đến 7 (không bị khoá, lớp chưa huỷ và trong thời hạn, chưa đủ 2 lớp trong ngày, còn chỗ); lỗi thì MSG-05 đến MSG-08 | Lớp nhóm đã chọn | UC-010 bước 3 đến 9 | - |
| TR-09 | SCR-06 | SCR-08 | 4 Dịch chuyển sang màn hình phụ thuộc có dữ liệu | Nhấn Vào danh sách chờ trong MSG-09 | Lớp đã đủ chỗ (BR-11, BR-12) | Lớp nhóm đã chọn | UC-010 luồng 7a1 đến 7a4 | (600,420); (1240,420) |
| TR-10 | START-ACT-04 | SCR-09 | 1 Dịch chuyển đơn giản | Sau khi có phiên làm việc | Huấn luyện viên đã xác thực (Q-47) | - | - | - |
| TR-11 | START-ACT-05 | SCR-10 | 1 Dịch chuyển đơn giản | Sau khi có phiên làm việc | Lễ tân đã xác thực (Q-47) | - | - | - |
| TR-12 | SCR-10 | SCR-11 | 1 Dịch chuyển đơn giản | Nhấn mục Mua hoặc gia hạn gói tập | - | - | UC-005 bước 1 | - |
| TR-13 | SCR-11 | SCR-12 | 4 Dịch chuyển sang màn hình phụ thuộc có dữ liệu | Nhấn Tiếp tục | Đã chọn thời hạn, loại gói và người mua (thiếu thì MSG-01; người mua: Q-01) | Gói tập và người mua đã chọn | UC-005 bước 3, 6 | - |
| TR-14 | SCR-12 | SCR-11 | 1 Dịch chuyển đơn giản | Nhấn Quay lại | Đơn chưa tạo | - | UC-005 bước 7 | - |
| TR-15 | SCR-12 | SCR-13 | 4 Dịch chuyển sang màn hình phụ thuộc có dữ liệu | Nhấn Xác nhận bán | - | Đơn mua chờ thu tiền | UC-005 bước 7, 8 | - |
| TR-16 | SCR-13 | SCR-14 | 4 Dịch chuyển sang màn hình phụ thuộc có dữ liệu | Nhấn Xác nhận đã thu | Đã thu đủ tiền mặt (8a) hoặc đã nhập mã giao dịch POS (8b; thiếu mã thì MSG-01) | Đơn mua đã thanh toán | UC-005 luồng 8a, 8b, bước 11, 13 | - |
| TR-17 | START-ACT-06 | SCR-15 | 1 Dịch chuyển đơn giản | Sau khi có phiên làm việc | Quản lý chi nhánh đã xác thực (Q-47) | - | - | - |
| TR-18 | START-ACT-07 | SCR-16 | 1 Dịch chuyển đơn giản | Sau khi có phiên làm việc | Giám đốc chuỗi đã xác thực (Q-47) | - | - | - |

Mẫu 2 (pop-up modal) và mẫu 3 (pop-up không khoá) không có cạnh: các hộp thông điệp (MSG-02 đến MSG-09) là hộp thông điệp chuẩn không có mã SCR, việc đóng hộp quay về màn hình cha là ngầm định. Menu chung không vẽ cạnh, ghi ở Ghi chú của node Start. Cạnh TR-05 và TR-14 (Quay lại) vẽ vì ui-standards.md UI-STT 15 quy định rõ.

## 3. Sơ đồ

File diagrams/P11a-screen-transition.drawio, một trang, 16 màn hình trong 6 partition (không quá 20 nên không tách trang). Mẫu 1: nét đứt, đầu mũi tên mở. Mẫu 4: nét liền, đầu mũi tên mở, nhãn kèm dữ liệu truyền.


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-99 | Khi mở ứng dụng di động, người dùng vào màn hình nào: màn hình của Người quan tâm khi chưa đăng nhập, hay màn hình đăng nhập trước; lối vào Đăng nhập (UC-004) đặt ở màn hình nào; và Người quan tâm sau khi đăng ký tài khoản (UC-003) vào màn hình nào? (Mở vào Trang chủ Người quan tâm, lối vào Đăng nhập ở đó / Mở vào màn hình Đăng nhập / Khác - nêu rõ) | START-ACT-01, START-ACT-02, SCR-01, SCR-02, TR-01, TR-02 | P02 bảng 4a: UC-004 Đăng nhập là subfunction của ACT-02, UC-003 của ACT-01; nguồn và đặc tả P04 không nêu điểm khởi đầu của ứng dụng |

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

Các mục Target đạt, với các điểm cần người dùng lưu ý:

- Target 5: 18 cạnh dùng mẫu 1 hoặc mẫu 4, không có cạnh đóng pop-up; mọi SCR đến được từ Start của tác nhân. Lối ra của 4 màn hình điều hướng chưa có màn hình đích (SCR-01, SCR-09, SCR-15, SCR-16) và của các màn hình kết quả (SCR-05, SCR-07, SCR-08, SCR-14) là màn hình kết thúc có ghi rõ ở Ghi chú của node, vì lối vào use case chưa có màn hình đích không tính là lối ra.
- Điểm khởi đầu: đặc tả không nêu điểm khởi đầu nên các Start ghi Sau khi có phiên làm việc (hội viên theo tiền điều kiện UC-005, UC-010; bốn vai trò còn lại chờ Q-47) và Mở ứng dụng cho ACT-01; câu hỏi Q-99 ghi ở mục Câu hỏi mở.
- Các luồng Kết thúc use case (thất bại) của UC-010 (luồng 4a, 7a2a) không có cạnh: hộp thông điệp đóng và người dùng ở lại SCR-06, rời bằng Trang chủ. Luồng 9a2 của UC-005 có cạnh TR-05 (Chọn lại gói tập) vì đơn đã huỷ không dùng tiếp được ở SCR-04.
- TR-06 kết hợp sự kiện người dùng (xác nhận mua) và sự kiện Nhận kết quả của cổng thanh toán; bước thanh toán nằm ngoài ứng dụng chưa rõ giao diện (Q-96) nên không vẽ node riêng.
- Hai cạnh Quay lại (TR-05, TR-14) cùng cặp node với TR-04, TR-13 theo chiều ngược lại, được tách bằng cổng ra, vào khác nhau (exitY, entryY).
- Nếu Q-92 trả lời là hai ứng dụng riêng, partition ACT-04 thuộc ứng dụng khác nhưng sơ đồ không đổi.
