# P11b - SS-07 Authentication - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11b |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (HE_THONG_NGOAI); P10-design-elements.md (phiên bản 1.0; F2, bảng Interface gọi ngược, F4, F5); P08-analysis-model.md (phiên bản 1.0; F3 dòng boundary nguồn, entity truyền qua interface); P07-uc-analysis (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; dòng message có boundary nguồn, Câu hỏi mở); P04-uc-specs (UC-005, UC-010, UC-015, UC-018, phiên bản 1.0; luồng thay thế, ngoại lệ có bước của hệ thống ngoài hoặc thiết bị); P06-supplementary-spec.md (phiên bản 1.0; Mục 3, 4, 5); P09-architecture.md (phiên bản 1.0; F4, F6, F7); P11a-gui (mục Câu hỏi mở của screen-list.md, ui-standards.md, screen-transition.md, chỉ để tìm Q cùng nội dung). PHAM_VI_SUBSYSTEM: Tất cả. TAI_LIEU_GIAO_TIEP: Không có. CHINH_SACH_LOI: Timeout 10 giây cho cổng thanh toán, 5 giây cho cổng SMS và dịch vụ thông báo đẩy, 15 giây cho hệ thống hoá đơn điện tử; không tự thử lại yêu cầu thanh toán, khi không biết giao dịch đã thành công hay chưa thì tra cứu qua API tra cứu của cổng trước khi kết luận; SMS, thông báo đẩy và gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút. YEU_CAU_BO_SUNG: phạm vi phân tích hiện có là bốn use case UC-005, UC-010, UC-015, UC-018; đề xuất sửa artifact trước chờ câu trả lời Q chưa áp dụng; đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại. Mã Q, ASM lớn nhất do người dùng cung cấp: Q-99, chưa có ASM |
| Phạm vi | SS-07 Authentication (package PKG-21 Security); lần chạy đầu cho mọi subsystem của P10 F2 |
| Mã Q, ASM cuối đã cấp | Q-102 (Q mới của lần chạy: Q-100 đến Q-102, ghi ở file chung P11b-system-interfaces.md); ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh sử dụng

| UC | Control gọi (AC hoặc DC) | Message trong P07 (STT, tên) | Dữ liệu truyền | Luồng lỗi trong P04 |
|---|---|---|---|---|
| Không có | - | Không có message P07 tới PKG-21 trong UC-005, UC-010, UC-015, UC-018 | - | Không có luồng xác thực trong P04 của bốn use case (cách xác thực của nhân viên: Q-47; yêu cầu bảo mật khác: Q-89) |

- P10 F1 xét SS-07 vì PKG-10, PKG-11, PKG-12 phụ thuộc PKG-21, nhưng P07 của bốn use case không có message xác thực. Use case sở hữu việc xác thực là UC-004 Đăng nhập (và UC-024, UC-025 cho quyền xem chỉ số cơ thể), chưa có P04, P07.

## F2. Interface

| IF | Tên | Vai trò (một câu) | Bên hiện thực (SS; DC khi là interface gọi ngược) | Client (DC, PKG) | Package chứa |
|---|---|---|---|---|---|
| IF-07 | IAuthenticator | Chờ P07 UC-004: xác thực người dùng hoặc thiết bị gọi vào và cho biết định danh, vai trò của người gọi. | SS-07 Authentication | DC-PurchaseOrRenewPackageController, DC-BookClassSpotController (PKG-10); DC-SellPackageController (PKG-11); SS-05 (PKG-12) | PKG-21 Security |

- Trạng thái: Chờ P07 UC-004. Chữ ký operation chưa định nghĩa (A1).

## F3. Operation

| IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC | Tiền điều kiện | Hậu điều kiện | Đồng bộ | Idempotent | Timeout |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IF-07 | IAuthenticator | Người dùng (ACT-01 đến ACT-07), cửa quay (ACT-12) | // authenticateCaller: xác thực người dùng (ACT-01 đến ACT-07) hoặc thiết bị (ACT-12) gọi vào | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 UC-004 | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 |
| IF-07 | IAuthenticator | Người dùng (ACT-01 đến ACT-07) | // identifyCallerRole: cho biết định danh và vai trò của người gọi để Application kiểm tra quyền | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 UC-004 (và UC-024, UC-025 cho quyền xem chỉ số cơ thể) | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 | Chờ P07 |

- Không có sơ đồ sequence: không UC nào đã có P07 gọi SS-07. Cách xác thực chờ Q-47, Q-89.

## F4. Sequence diagram

Không có sơ đồ sequence: SS-07 chưa có operation có chữ ký (Chờ P07 UC-004). File diagrams/P11b-subsystem-SS-07.drawio chỉ có trang "Phụ thuộc".

## F5. Phần tử của subsystem

a) Bảng phần tử

| DC | Tên | Vai trò | Trách nhiệm | Visibility | Hiện thực IF |
|---|---|---|---|---|---|
| - | Không có | - | Chưa thiết kế bên trong vì chữ ký chờ P07 UC-004 | - | IF-07 |

b) Class diagram phần tử: Không có (chưa thiết kế bên trong, Chờ P07 UC-004).

c) Cơ chế kiến trúc áp dụng

| Cơ chế | Nguồn | Cách tích hợp |
|---|---|---|
| Bảo mật dữ liệu | P09 F7 (thông tin xác thực là dữ liệu cần bảo vệ; quy định bảo vệ: Q-89) | Chờ P07 UC-004. |

## F6. Phụ thuộc subsystem

| Subsystem | Phụ thuộc vào (IF, SS, PKG) | Loại (Qua interface / Vào package) | Lý do | Đánh giá (Ưu tiên / Dùng thận trọng) |
|---|---|---|---|---|
| SS-07 | PKG-26 (DC-Member) | Vào package | Tra cứu định danh hội viên (P10 F2, F6 dòng PKG-21 --> PKG-26); chữ ký Chờ P07 UC-004 | Dùng thận trọng |

Trang "Phụ thuộc" (SS07-DP)

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SS-07 | SubsystemBox | SS-07 Authentication | «subsystem» | - | Subsystem đang xét | 40 | 40 | 240 | 60 |
| PKG-26 | Package | PKG-26 Account | - | PKG-04 Domain | Chứa DC-Member | 420 | 40 | 240 | 60 |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| SS07-DP-E1 | SS-07 | PKG-26 | Dependency | «use» | Vào package: tra cứu định danh hội viên (P10 F2, F6); chữ ký chờ P07 UC-004 | - |

## F7. Thiết kế xử lý lỗi và điểm kiểm tra

a) Bảng lỗi

| Operation | Tình huống lỗi | Loại | Phát hiện bằng | Xử lý trong subsystem (thử lại, tra cứu trạng thái, chuyển đổi ngoại lệ) | Kết quả trả cho client | Luồng P04 tương ứng | Q, ASM |
|---|---|---|---|---|---|---|---|
| - | Không có (chưa có operation) | - | - | - | - | - | Q-47, Q-89 |

b) Điểm kiểm tra

| Điểm kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Mỗi interface subsystem cung cấp có quan hệ realization | Không áp dụng | IF-07 chưa có chữ ký và chưa thiết kế phần tử bên trong (Chờ P07 UC-004) |
| Mỗi interface subsystem dùng có quan hệ phụ thuộc | Không áp dụng | SS-07 không dùng interface nào |
| Không phần tử bên trong nào public, trừ kiểu dữ liệu và ngoại lệ thuộc chữ ký interface | Không áp dụng | Chưa có phần tử bên trong |
| Mỗi operation có sơ đồ hộp trắng hoặc ánh xạ 1-1 dễ thấy | Không áp dụng | Chưa có operation có chữ ký |

## Câu hỏi mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).

## Vấn đề còn mở

Ghi ở file chung P11b-system-interfaces.md (Câu hỏi mở, Giả định của mọi subsystem ghi một chỗ).
