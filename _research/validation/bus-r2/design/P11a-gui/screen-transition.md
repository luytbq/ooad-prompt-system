# P11a - screen-transition - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 1) |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (C7.3); project-profile.md; P01-actors.md (Mục 2); P02-usecases.md (Mục 4); P04-uc-specs/UC-009 và UC-017 (luồng sự kiện, thông điệp, tiền điều kiện); P07-uc-analysis/UC-009 và UC-017 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P10-design-elements.md (F3, F4); P11a-gui/ui-standards.md (phiên bản 1.0, UI-STT 8, 11, 34, 49, F1b); P11a-gui/screen-list.md (phiên bản 1.0). Placeholder: CHE_DO_CHAY = Giai đoạn 1; YEU_CAU_BO_SUNG = phạm vi UC-009, UC-017 và màn hình điều hướng cần thiết. Q, ASM lớn nhất quét trước lần chạy: Q-65, ASM-48 |
| Phạm vi | Hai tác nhân người có màn hình trong phạm vi: ACT-01 Hành khách, ACT-03 Nhân viên điều hành |
| Mã Q, ASM cuối đã cấp | Q-68, ASM-50 |

File sơ đồ: diagrams/P11a-screen-transition.drawio (một trang, hai partition). Nhãn của node màn hình trên sơ đồ có ba dòng: «Loại màn hình», ID, nhãn. Cột x, y, w, h của node tính trong partition chứa nó; toạ độ partition và cột Điểm uốn là toạ độ tuyệt đối. ACT-02, ACT-04, ACT-05 chưa có màn hình trong phạm vi nên chưa có node Start và partition; thêm khi các use case của họ vào phạm vi.

## Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| P-ACT-01 | Partition | Hành khách (ACT-01) | - | - | Toạ độ tuyệt đối | 0 | 0 | 1440 | 340 |
| P-ACT-03 | Partition | Nhân viên điều hành (ACT-03) | - | - | Toạ độ tuyệt đối | 0 | 340 | 1440 | 340 |
| START-ACT-01 | Start | - | - | P-ACT-01 | Mở website (ASM-50). Mọi màn hình có menu tới SCR-01, mẫu 1. Rời SCR-03 bằng menu: hành vi với các chỗ đang giữ ghi ở đặc tả SCR-03 | 80 | 110 | 40 | 40 |
| SCR-01 | Screen | Trang chủ hành khách | Độc lập | P-ACT-01 | Màn hình điều hướng. Lối vào mua vé (UC-009) đi qua tra cứu chuyến của UC-008, chưa có màn hình, nối bằng E-02 (ASM-49, Q-66). Lối vào UC-001, UC-003, UC-008, UC-011, UC-012, UC-014 chưa có màn hình đích, không tính là lối ra. Hiển thị MSG-01 khi UC-008 kết thúc mà chưa chọn chuyến và MSG-09 sau khi huỷ yêu cầu mua vé | 240 | 100 | 160 | 60 |
| SCR-02 | Screen | Chọn chỗ | Phụ thuộc có dữ liệu | P-ACT-01 | Nhận "Chuyến đã chọn" từ UC-008 (ASM-49). Luồng 4a: MSG-02 rồi E-05 (quay lại bước 2 qua SCR-01). Luồng 4b: MSG-03 là banner tại SCR-02, không đổi màn hình. Luồng 4c: MSG-04 rồi E-05 | 560 | 100 | 160 | 60 |
| SCR-03 | Screen | Nhập thông tin người đi | Phụ thuộc có dữ liệu | P-ACT-01 | Luồng 7a: lỗi MSG-05, MSG-06 tại trường, không đổi màn hình. Nút "Tiếp tục thanh toán" gọi UC-010 (chưa có màn hình, ASM-49); thanh toán thất bại (8a, MSG-07) hoặc hết thời hạn giữ chỗ (5a, MSG-08) thì E-06 | 880 | 100 | 160 | 60 |
| SCR-04 | Screen | Vé đã phát hành | Phụ thuộc có dữ liệu | P-ACT-01 | Màn hình kết thúc thành công của UC-009; lối ra là nút "Về trang chủ" (E-07) và menu | 1200 | 100 | 160 | 60 |
| START-ACT-03 | Start | - | - | P-ACT-03 | Sau khi có phiên làm việc (tiền điều kiện UC-017, ASM-50). Mọi màn hình có menu tới SCR-05, mẫu 1 | 80 | 110 | 40 | 40 |
| SCR-05 | Screen | Trang chủ điều hành | Độc lập | P-ACT-03 | Màn hình điều hướng. Lối vào UC-016, UC-019, UC-020, UC-021, UC-022 chưa có màn hình đích, không tính là lối ra. Hiển thị MSG-12 sau khi bỏ yêu cầu huỷ chuyến | 240 | 100 | 160 | 60 |
| SCR-06 | Screen | Chọn chuyến cần huỷ | Độc lập | P-ACT-03 | Luồng 4a, 4b: pop-up SCR-07 đóng ngầm định, banner MSG-10, MSG-11 tại SCR-06, không vẽ cạnh | 560 | 100 | 160 | 60 |
| SCR-07 | Screen | Xác nhận huỷ chuyến | Con phụ thuộc | P-ACT-03 | Pop-up modal. Nút "Không huỷ" và phím Esc đóng pop-up, quay về SCR-06 ngầm định, không vẽ cạnh | 880 | 100 | 160 | 60 |
| SCR-08 | Screen | Kết quả huỷ chuyến | Phụ thuộc có dữ liệu | P-ACT-03 | Màn hình kết thúc của UC-017; lối ra là nút "Về trang chủ" (E-13) và menu | 1200 | 100 | 160 | 60 |

## Bảng Edge

| ID | Nguồn | Đích | Mẫu dịch chuyển | Sự kiện kích hoạt | Điều kiện | Dữ liệu truyền | UC bước | Điểm uốn |
|---|---|---|---|---|---|---|---|---|
| E-01 | START-ACT-01 | SCR-01 | 1 | Mở website | - | - | UC-009 bước 1 | - |
| E-02 | SCR-01 | SCR-02 | 4 | Chọn chuyến để mua vé (kết quả của UC-008) | UC-008 trả về chuyến đã chọn | Chuyến đã chọn | UC-009 bước 1 đến 3 | - |
| E-03 | SCR-02 | SCR-03 | 4 | Nhấn "Tiếp tục" | Các chỗ còn trống, không quá 5 chỗ, chuyến chưa đến giờ xuất bến (BR-02, BR-01, BR-05) | Các chỗ đang giữ | UC-009 bước 3 đến 5 | - |
| E-04 | SCR-03 | SCR-04 | 4 | Nhấn "Tiếp tục thanh toán" | Đã nhập họ tên và số điện thoại; UC-010 trả về thanh toán thành công | Các vé đã phát hành | UC-009 bước 6 đến 12 | - |
| E-05 | SCR-02 | SCR-01 | 1 | Nhấn "Tìm lại chuyến" trong MSG-02, đóng MSG-04, hoặc nhấn "Huỷ yêu cầu mua vé" | Luồng 4a, 4c, *a | - | UC-009 bước 4a, 4c, *a | (640,220); (360,220) |
| E-06 | SCR-03 | SCR-01 | 1 | Đóng MSG-07 hoặc MSG-08, hoặc nhấn "Huỷ yêu cầu mua vé" | Luồng 8a, 5a, *a | - | UC-009 bước 8a, 5a, *a | (960,250); (320,250) |
| E-07 | SCR-04 | SCR-01 | 1 | Nhấn "Về trang chủ" | - | - | UC-009 bước 12 | (1280,280); (280,280) |
| E-08 | START-ACT-03 | SCR-05 | 1 | Có phiên làm việc | Nhân viên điều hành đã được xác thực | - | UC-017 tiền điều kiện | - |
| E-09 | SCR-05 | SCR-06 | 1 | Chọn "Huỷ chuyến" | - | - | UC-017 bước 1, 2 | - |
| E-10 | SCR-06 | SCR-07 | 2 | Nhấn "Tiếp tục huỷ chuyến" | Đã chọn chuyến và lý do huỷ | - | UC-017 bước 3 | - |
| E-11 | SCR-07 | SCR-08 | 4 | Nhấn "Xác nhận huỷ chuyến" | Chuyến chưa bị huỷ và chưa đến giờ xuất bến (BR-09, BR-10) | Kết quả huỷ chuyến | UC-017 bước 3 đến 14 | - |
| E-12 | SCR-06 | SCR-05 | 1 | Nhấn "Bỏ yêu cầu huỷ chuyến" | Luồng *a | - | UC-017 bước *a | (640,560); (360,560) |
| E-13 | SCR-08 | SCR-05 | 1 | Nhấn "Về trang chủ" | - | - | UC-017 bước 14 | (1280,590); (320,590) |

Nhãn vẽ trên cạnh: E-01 "mở website"; E-02 "Chuyến đã chọn"; E-03 "Các chỗ đang giữ"; E-04 "Các vé đã phát hành"; E-05 và E-06 "huỷ / thất bại"; E-07 và E-13 "Về trang chủ"; E-08 "có phiên làm việc"; E-09 "chọn Huỷ chuyến"; E-10 "Tiếp tục [đã chọn]"; E-11 "Kết quả huỷ chuyến"; E-12 "bỏ yêu cầu".

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-66 | Sơ đồ chỗ và việc chọn chỗ của UC-009 hiển thị ở đâu, và luồng 4a "Quay lại bước 2" đưa hành khách về đâu? (Sơ đồ chỗ và chọn chỗ cùng một màn hình của UC-009, nhận chuyến đã chọn từ UC-008; 4a đưa về màn hình tra cứu chuyến / Sơ đồ chỗ thuộc màn hình của UC-008 và UC-009 chỉ nhận các chỗ đã chọn; 4a quay lại màn hình tra cứu chuyến) | SCR-01, SCR-02, E-02, E-05; UC-009 bước 2, 3, 4a; UC-008 chưa có P04 | P07 UC-009 F2 bước 2: "Hiển thị sơ đồ chỗ và chỗ trống thuộc phân tích của UC-008" trong khi bước 3 giao việc nhận các chỗ đã chọn cho boundary BookTicketOnlineForm; P04 UC-009 luồng 4a: "Quay lại bước 2" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-49 | SCR-02 hiển thị sơ đồ chỗ và nhận các chỗ hành khách chọn (UC-009 bước 3), nhận "chuyến đã chọn" từ UC-008. UC-008 và UC-010 chưa có màn hình nên sơ đồ nối qua hai use case đó bằng cạnh gộp: E-02 thay cho các màn hình tra cứu chuyến, E-04 thay cho màn hình thanh toán. Luồng 4a "Quay lại bước 2" đưa hành khách về SCR-01 để tìm lại chuyến (E-05). Khi UC-008 và UC-010 có màn hình, tách E-02, E-04, E-05 theo màn hình thật | Chờ Q-66. UC-008 và UC-010 chưa có P04, P07 nên chưa biết màn hình của chúng; chọn cách đọc sát chữ của luồng 4a và phân tích P07 | SCR-01, SCR-02, SCR-03, SCR-04; E-02, E-04, E-05; UC-009 bước 2, 3, 4a, 8 |
| ASM-50 | Điểm khởi đầu của hành khách là mở website (không cần tài khoản, NFR-02); điểm khởi đầu của nhân viên điều hành là sau khi có phiên làm việc. | Chọn điểm khởi đầu mặc định, không cần Q. UC-009 không có tiền điều kiện và đặc tả không nêu cách hành khách vào website; UC-017 nêu tiền điều kiện "đã được xác thực và đang có phiên làm việc" nhưng không nêu màn hình sau đăng nhập | START-ACT-01, START-ACT-03; E-01, E-08 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| Không có | - | - | - |

## Vấn đề còn mở

- Mẫu 1 cho cạnh E-05, E-06, E-07, E-12, E-13 dựa vào chuẩn A1 ở ui-standards.md (UI-STT 49: use case kết thúc đưa người dùng về màn hình điều hướng); các cạnh này không có trong luồng sự kiện của P04 dưới dạng dịch chuyển rõ ràng. Cạnh E-05 và E-06 gộp nhiều sự kiện cùng đích SCR-01 và cùng mẫu 1 vào một cạnh để sơ đồ gọn.
- Bố cục: cạnh quay về SCR-01 và SCR-05 đi trong dải phía dưới hàng màn hình với làn y cách nhau 30. File .drawio sinh bằng chương trình từ cùng dữ liệu với hai bảng trên và đã kiểm tự động (XML hợp lệ, toạ độ là bội số của 10, khoảng cách tối thiểu giữa hai node là 40, cạnh không cắt qua node). Chưa mở bằng draw.io để xem bằng mắt.
- Mọi SCR đến được từ một node Start và có ít nhất một lối ra: SCR-04 và SCR-08 là màn hình kết thúc có ghi rõ ở cột Ghi chú; SCR-07 có lối ra là E-11 và đóng ngầm định về SCR-06.
