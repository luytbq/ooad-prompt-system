# P10 - Phần tử thiết kế - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P10 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE đã cập nhật sau P09); P01 1.0; P02 1.0; P03 1.0; P06 1.0; P07 UC-005, UC-007, UC-009, UC-013 1.0; P08 1.0; P09 1.0 |
| Phạm vi | Toàn hệ thống (các lớp hoạt động trong P08) |

Placeholder: TIEU_CHI_NHOM_PACKAGE = Không có; KHA_NANG_THAY_DOI_GIAO_DIEN = Không có (không đủ căn cứ, coi là dễ thay đổi); YEU_CAU_BO_SUNG = Không có.

## F1. Subsystem ứng viên và quyết định

| Lớp phân tích (AC) | Tiêu chí thoả | Quyết định | Lý do |
|---|---|---|---|
| AC-B-PaymentGateway | Hệ thống ngoài; Có thể thay thế; Bảo mật | Subsystem | Che giao thức cổng thanh toán, là nơi duy nhất tiếp xúc dữ liệu thẻ (NFR-04, NFR-06) |
| AC-B-DockDevice | Thiết bị; Có thể thay thế | Subsystem | Che MQTT và định dạng thông điệp của nhà cung cấp (NFR-07); nhận sự kiện từ thiết bị |
| AC-B-ReturnBikeForm | Dịch vụ dùng chung; Có thể thay thế | Subsystem | Kênh là email, có thể là dịch vụ ngoài (Q-19); P09 F8 đặt vào PKG-20 |
| AC-B-RentBikeForm, AC-B-CreateTransferOrderForm | - | Không | Boundary người dùng, ánh xạ theo P09 F5 |
| Control, entity | - | Không | Không thoả tiêu chí |
| (Cơ chế P09) Scheduling | Dịch vụ dùng chung | Subsystem | P09 F4 PKG-21; mốc 60 giây và 24 giờ (BR-06, BR-09) |

## F2. Bảng subsystem

| SS | Tên | Interface (IF) | Trách nhiệm | Che giấu phần tử nào | AC nguồn | ACT liên quan | PKG chứa |
|---|---|---|---|---|---|---|---|
| SS-01 | PaymentGatewaySubsystem | IF-01 IPaymentGateway | // requestHold<br>// requestCancelHold<br>// requestCapture<br>// requestReleaseRemainder<br>// linkCard (UC-002, chưa phân tích) | Gọi API ngân hàng, xác thực với cổng, chuyển đổi mã lỗi, timeout | AC-B-PaymentGateway | ACT-07 | PKG-18 |
| SS-02 | DockCommunicationSubsystem | IF-02 IDockCommandSender (cung cấp)<br>IF-03 IDockEventListener (yêu cầu, Application hiện thực) | // sendUnlockCommand<br>// sendLockCommand<br>// reportBikeRemoved<br>// reportBikeReturned | Kết nối MQTT broker, topic, định dạng thông điệp, xử lý thông điệp trùng | AC-B-DockDevice | ACT-08 | PKG-19 |
| SS-03 | EmailSubsystem | IF-04 IInvoiceSender | // deliverInvoice | Dựng và gửi email | AC-B-ReturnBikeForm | ACT-01 | PKG-20 |
| SS-04 | SchedulerSubsystem | IF-05 IScheduler (cung cấp)<br>IF-06 ITimerListener (yêu cầu, Application hiện thực) | // schedule, // cancel mốc thời gian | Lưu mốc bền vững, quét mốc đến hạn, chống kích hoạt trùng khi nhiều tiến trình | Cơ chế P09 (ACT-09, BR-06) | ACT-09 | PKG-21 |

## F3. Bảng ánh xạ lớp phân tích sang phần tử thiết kế

| AC | Kết quả | Phần tử thiết kế | PKG | Lý do |
|---|---|---|---|---|
| AC-B-RentBikeForm | Tách thành nhiều lớp | DC-RentBikeScreen<br>DC-RentBikeViewModel<br>DC-RentalEndpoint | PKG-05<br>PKG-05<br>PKG-22 | P09 F5: View, ViewModel (MVVM) ở RiderApp và endpoint ở ApiEndpoints |
| AC-B-ReturnBikeForm | Subsystem | SS-03 EmailSubsystem (IF-04) | PKG-20 | F1 |
| AC-B-CreateTransferOrderForm | Tách thành nhiều lớp | DC-CreateTransferOrderPage<br>DC-TransferOrderEndpoint | PKG-06<br>PKG-23 | P09 F5: view ở StaffWeb và endpoint |
| AC-B-PaymentGateway | Subsystem | SS-01 (IF-01) | PKG-18 | F1 |
| AC-B-DockDevice | Subsystem | SS-02 (IF-02, IF-03) | PKG-19 | F1 |
| AC-C-RentBikeController | Lớp thiết kế DC | DC-RentBikeService | PKG-09 | Đổi tên: "Controller" trùng thuật ngữ của MVC và của framework web (P09 F5) |
| AC-C-ReturnBikeController | Lớp thiết kế DC | DC-ReturnBikeService | PKG-09 | Như trên |
| AC-C-RecordLostBikeController | Lớp thiết kế DC | DC-RecordLostBikeService | PKG-09 | Như trên |
| AC-C-CreateTransferOrderController | Lớp thiết kế DC | DC-CreateTransferOrderService | PKG-11 | Như trên |
| AC-E-RiderAccount | Lớp thiết kế DC | DC-RiderAccount | PKG-15 | Lớp đơn giản, một trừu tượng |
| AC-E-Trip | Tách thành nhiều lớp | DC-Trip<br>DC-FareCalculator | PKG-15 | Hai nhóm trách nhiệm: vòng đời chuyến và quy tắc giá (BR-07); quy tắc giá có thể đổi theo bảng giá cước (GL-01, Q-15) mà vòng đời chuyến không đổi |
| AC-E-Dock | Lớp thiết kế DC | DC-Dock | PKG-16 | Lớp đơn giản, một trừu tượng |
| AC-E-Bike | Lớp thiết kế DC | DC-Bike | PKG-16 | Lớp đơn giản, một trừu tượng |
| AC-E-PaymentHold | Lớp thiết kế DC | DC-PaymentHold | PKG-15 | Lớp đơn giản, một trừu tượng |
| AC-E-Station | Lớp thiết kế DC | DC-Station | PKG-16 | Lớp đơn giản, một trừu tượng |
| AC-E-TransferOrder | Lớp thiết kế DC | DC-TransferOrder | PKG-16 | Lớp đơn giản, một trừu tượng |

Phần tử thiết kế mới do cơ chế kiến trúc:

| DC hoặc SS | Tên | PKG | Cơ chế | Nguồn |
|---|---|---|---|---|
| DC-DockEventHandler | DockEventHandler (hiện thực IF-03) | PKG-09 | Callback từ thiết bị | P09 F5, F6 |
| DC-RentalTimerHandler | RentalTimerHandler (hiện thực IF-06) | PKG-09 | Callback từ bộ lập lịch | P09 F5, F6 |
| SS-04 | SchedulerSubsystem | PKG-21 | Lập lịch | P09 F4 |
| IF-07 đến IF-13 | IRiderAccountRepository, ITripRepository, IPaymentHoldRepository, IStationRepository, IDockRepository, IBikeRepository, ITransferOrderRepository | PKG-15, PKG-16 | Persistence (interface kho dữ liệu do Domain định nghĩa) | P09 F5, F6 |
| DC-JpaRiderAccountRepository đến DC-JpaTransferOrderRepository (7 lớp) | Hiện thực IF-07 đến IF-13 | PKG-17 | Persistence | P09 F5; CONG_NGHE |

## F4. Bảng package

| PKG | Tên | Layer (PKG) | Trách nhiệm | Phần tử chứa (DC, SS, IF) | Tiêu chí nhóm | Phụ thuộc vào (PKG) |
|---|---|---|---|---|---|---|
| PKG-05 | RiderApp | PKG-01 | Giao diện di động của người thuê xe. | DC-RentBikeScreen, DC-RentBikeViewModel | Cùng tác nhân ACT-01 | PKG-22 |
| PKG-06 | StaffWeb | PKG-01 | Giao diện của nhân viên. | DC-CreateTransferOrderPage | Cùng nhóm tác nhân nhân viên | PKG-23 |
| PKG-22 | RiderEndpoints | PKG-01 (trong PKG-07) | Tiếp nhận yêu cầu từ RiderApp. | DC-RentalEndpoint | Cùng tác nhân ACT-01; tách khỏi PKG-23 theo tiêu chí tác nhân | PKG-09 |
| PKG-23 | StaffEndpoints | PKG-01 (trong PKG-07) | Tiếp nhận yêu cầu từ StaffWeb. | DC-TransferOrderEndpoint | Cùng tác nhân ACT-04 | PKG-11 |
| PKG-09 | Rental | PKG-02 | Điều phối use case nhóm Thuê trả xe. | DC-RentBikeService, DC-ReturnBikeService, DC-RecordLostBikeService, DC-DockEventHandler, DC-RentalTimerHandler | Tạo và thay đổi cùng Trip, PaymentHold; trao đổi message nhiều (P07) | PKG-15, PKG-16, IF-01, IF-02, IF-04, IF-05 (hiện thực IF-03, IF-06) |
| PKG-11 | Dispatch | PKG-02 | Điều phối use case nhóm Điều phối. | DC-CreateTransferOrderService | Cùng tác nhân ACT-04 | PKG-16, IF-02 (UC-014, chưa phân tích) |
| PKG-15 | RentalDomain | PKG-03 | Quy tắc về tài khoản, chuyến đi, khoản tạm giữ, giá. | DC-RiderAccount, DC-Trip, DC-FareCalculator, DC-PaymentHold, IF-07, IF-08, IF-09 | Có quan hệ R-03, R-13; Trip dùng FareCalculator | PKG-16 |
| PKG-16 | FleetDomain | PKG-03 | Quy tắc về trạm, ụ, xe, lệnh điều chuyển. | DC-Station, DC-Dock, DC-Bike, DC-TransferOrder, IF-10 đến IF-13 | Có quan hệ R-10, R-30, R-31, R-32 | - |
| PKG-17 | Persistence | PKG-04 | Lưu và nạp đối tượng miền. | 7 lớp Jpa*Repository | Cùng cơ chế | PKG-15, PKG-16 (hiện thực interface) |
| PKG-18 | PaymentIntegration | PKG-04 | Giao tiếp cổng thanh toán. | SS-01, IF-01 | Package subsystem | - |
| PKG-19 | DeviceIntegration | PKG-04 | Giao tiếp ụ khoá. | SS-02, IF-02, IF-03 | Package subsystem | - |
| PKG-20 | Notification | PKG-04 | Gửi email. | SS-03, IF-04 | Package subsystem | - |
| PKG-21 | Scheduling | PKG-04 | Lập lịch mốc thời gian. | SS-04, IF-05, IF-06 | Package subsystem | - |

PKG-08, PKG-10, PKG-12, PKG-13, PKG-14 chưa có phần tử (use case chưa phân tích).

## F5. Visibility

| PKG | Phần tử | Visibility | Được dùng bởi (PKG) |
|---|---|---|---|
| PKG-05 | DC-RentBikeScreen | package-private | - |
| PKG-05 | DC-RentBikeViewModel | package-private | - (gọi PKG-22 qua mạng) |
| PKG-06 | DC-CreateTransferOrderPage | package-private | - |
| PKG-22 | DC-RentalEndpoint | public | PKG-05 (qua mạng) |
| PKG-23 | DC-TransferOrderEndpoint | public | PKG-06 (qua mạng) |
| PKG-09 | DC-RentBikeService, DC-ReturnBikeService | public | PKG-22 |
| PKG-09 | DC-RecordLostBikeService, DC-DockEventHandler, DC-RentalTimerHandler | package-private | - (đăng ký với IF-03, IF-06 khi khởi động) |
| PKG-11 | DC-CreateTransferOrderService | public | PKG-23 |
| PKG-15 | DC-RiderAccount, DC-Trip, DC-PaymentHold, IF-07, IF-08, IF-09 | public | PKG-09, PKG-17 |
| PKG-15 | DC-FareCalculator | public | PKG-09 (UC-017 điều chỉnh cước về sau), nội bộ Trip |
| PKG-16 | DC-Station, DC-Dock, DC-Bike, DC-TransferOrder, IF-10 đến IF-13 | public | PKG-09, PKG-11, PKG-15, PKG-17 |
| PKG-17 | 7 lớp Jpa*Repository | package-private | - |
| PKG-18 đến PKG-21 | IF-01 đến IF-06 | public | PKG-09, PKG-11 |
| PKG-18 đến PKG-21 | Lớp bên trong SS-01 đến SS-04 | package-private | - |

## F6. Kiểm tra coupling giữa package

| Phụ thuộc (PKG --> PKG) | Suy ra từ | Cross-coupled | Lower --> Upper | Nhảy layer | Vòng | Kết luận và cách sửa |
|---|---|---|---|---|---|---|
| PKG-05 --> PKG-22 | RentBikeForm P07 message 1.1 | Không | Không | Không | Không | Hợp lệ |
| PKG-06 --> PKG-23 | UC-013 message 2.1 | Không | Không | Không | Không | Hợp lệ |
| PKG-22 --> PKG-09 | R-01 | Không | Không | Không | Không | Hợp lệ |
| PKG-23 --> PKG-11 | R-27 | Không | Không | Không | Không | Hợp lệ |
| PKG-09 --> PKG-15, PKG-16 | R-02, R-04, R-05, R-07, R-09, R-16 đến R-18, R-20, R-22 đến R-26 | Không | Không | Không | Không | Hợp lệ |
| PKG-09 --> IF-01, IF-02, IF-04, IF-05 | R-06, R-08, R-15, R-19, R-24; message tới ReturnBikeForm | Không | Không | Có (nới lỏng, P09 F6) | Không | Hợp lệ theo P09 |
| PKG-19 --> PKG-09 (sự kiện thiết bị) | Message 2.1 UC-005, 1.1 UC-007 | Có (với PKG-09 --> PKG-19) | Có | Không | Có | Sửa: IF-03 IDockEventListener đặt trong PKG-19, PKG-09 hiện thực; phụ thuộc đảo thành PKG-09 --> PKG-19 |
| PKG-21 --> PKG-09 (mốc thời gian) | Message 3 SD2 UC-005, message 1 UC-009 | Có | Có | Không | Có | Sửa: IF-06 ITimerListener trong PKG-21, PKG-09 hiện thực |
| PKG-11 --> PKG-16 | R-28, R-29 | Không | Không | Không | Không | Hợp lệ |
| PKG-15 --> PKG-16 | R-11, R-12, R-21 (Trip --> Bike, Dock) | Có trước khi sửa (PKG-16 --> PKG-15 qua Bike // getOngoingTrip trả về Trip, R-11 hai chiều) | Không | Không | Có trước khi sửa | Sửa: bỏ trách nhiệm // getOngoingTrip khỏi DC-Bike, chuyển thành truy vấn "chuyến đang diễn ra theo xe" của IF-08 ITripRepository; R-11 điều hướng một chiều Trip --> Bike |
| PKG-17 --> PKG-15, PKG-16 | Hiện thực IF-07 đến IF-13 | Không | Có | Không | Không | Ngoại lệ được P09 F6 cho phép |

## F7. Package diagram thiết kế

File diagrams/P10-package-design.drawio.

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú (visibility) |
|---|---|---|---|---|---|
| PKG-01 đến PKG-04 | Package | Presentation, Application, Domain, TechnicalServices | «layer» | - | - |
| PKG-05, PKG-06, PKG-07 | Package | RiderApp, StaffWeb, ApiEndpoints | - | PKG-01 | - |
| PKG-22, PKG-23 | Package | RiderEndpoints, StaffEndpoints | - | PKG-07 | - |
| PKG-09, PKG-11 | Package | Rental, Dispatch | - | PKG-02 | - |
| PKG-15, PKG-16 | Package | RentalDomain, FleetDomain | - | PKG-03 | - |
| PKG-17 đến PKG-21 | Package | Persistence, PaymentIntegration, DeviceIntegration, Notification, Scheduling | - | PKG-04 | - |
| SS-01 đến SS-04 | Subsystem | PaymentGatewaySubsystem, DockCommunicationSubsystem, EmailSubsystem, SchedulerSubsystem | «subsystem» | PKG-18 đến PKG-21 | package-private bên trong |
| IF-01 đến IF-06 | Interface | IPaymentGateway, IDockCommandSender, IDockEventListener, IInvoiceSender, IScheduler, ITimerListener | «interface» | PKG-18 đến PKG-21 | public |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn | Ghi chú |
|---|---|---|---|---|---|
| E-01 | PKG-05 | PKG-22 | Dependency | - | - |
| E-02 | PKG-06 | PKG-23 | Dependency | - | - |
| E-03 | PKG-22 | PKG-09 | Dependency | - | - |
| E-04 | PKG-23 | PKG-11 | Dependency | - | - |
| E-05 | PKG-09 | PKG-15 | Dependency | - | - |
| E-06 | PKG-09 | PKG-16 | Dependency | - | - |
| E-07 | PKG-11 | PKG-16 | Dependency | - | - |
| E-08 | PKG-15 | PKG-16 | Dependency | - | - |
| E-09 | PKG-09 | IF-01 | Dependency | - | - |
| E-10 | PKG-09 | IF-02 | Dependency | - | - |
| E-12 | PKG-09 | IF-04 | Dependency | - | - |
| E-13 | PKG-09 | IF-05 | Dependency | - | - |
| E-14 | PKG-11 | IF-02 | Dependency | - | UC-014 |
| E-15 | SS-01 | IF-01 | Realization | - | - |
| E-16 | SS-02 | IF-02 | Realization | - | - |
| E-17 | SS-03 | IF-04 | Realization | - | - |
| E-18 | SS-04 | IF-05 | Realization | - | - |
| E-19 | SS-02 | IF-03 | Dependency | - | Subsystem gọi listener |
| E-20 | SS-04 | IF-06 | Dependency | - | Subsystem gọi listener |
| E-21 | PKG-09 | IF-03 | Realization | - | DC-DockEventHandler hiện thực |
| E-22 | PKG-09 | IF-06 | Realization | - | DC-RentalTimerHandler hiện thực |
| E-23 | PKG-17 | PKG-03 | Dependency | - | Hiện thực interface kho dữ liệu |

## F8. Subsystem context diagram

File diagrams/P10-subsystem-context.drawio, 4 trang (SS-01 đến SS-04). Mỗi trang: interface dạng canonical với trách nhiệm "// ...", subsystem hiện thực, các DC phụ thuộc; SS-02 và SS-04 có thêm interface yêu cầu (IF-03, IF-06) và DC hiện thực nó.

## Câu hỏi mở

Không có câu hỏi mới. Liên quan: Q-15, Q-19, Q-35, Q-36.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P08 | R-11, AC-E-Bike // getOngoingTrip | Tạo phụ thuộc vòng RentalDomain - FleetDomain | Đổi R-11 thành điều hướng một chiều Trip --> Bike; bỏ // getOngoingTrip khỏi Bike |
| P09 | F3 "web nhân viên (MVC passive)" | CONG_NGHE chọn sau P09 là React (SPA gọi API), không phải MVC passive phía máy chủ | Sửa F3: web nhân viên là SPA theo mẫu component, gọi PKG-07 |

## Vấn đề còn mở

- Tiêu chí A3 "hai lớp liên quan tới hai tác nhân khác nhau không cùng package" chỉ áp dụng cho boundary (tách PKG-22, PKG-23). PKG-09 Rental chứa control của ACT-01 (UC-005, UC-007) và ACT-09 (UC-009); giữ chung theo nhóm chức năng của P09 vì cùng thay đổi Trip, PaymentHold. Áp dụng tiêu chí cho cả control sẽ tách Rental thành 2-3 package cùng phụ thuộc một tập entity.
- DC-DockEventHandler sẽ phải chuyển sự kiện thẻ nhân viên (UC-014) sang PKG-11, tạo phụ thuộc PKG-09 --> PKG-11; chờ P07 của UC-014.
- Tỉ lệ ánh xạ khác 1-1: 4/16 lớp tách hoặc thành subsystem, dưới một nửa.
