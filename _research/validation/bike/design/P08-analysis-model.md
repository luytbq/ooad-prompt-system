# P08 - Mô hình phân tích hợp nhất - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P08 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P01-actors.md 1.0; P02-usecases.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis UC-005, UC-007, UC-009, UC-013 1.0; P04-uc-specs (tra câu gốc) |
| Phạm vi | Toàn hệ thống (mô hình chỉ gồm 4 use case đã có P07) |

Placeholder: CACH_CHIA_VIEW = Không có (mặc định F5: 16 lớp hoạt động, một trang); YEU_CAU_BO_SUNG = Không có.

## F1. Độ phủ use case

| UC | Tên | File P07 | Trạng thái |
|---|---|---|---|
| UC-001 | Đăng ký tài khoản | - | Chưa phân tích |
| UC-002 | Liên kết thẻ thanh toán | - | Chưa phân tích |
| UC-003 | Đăng nhập | - | Chưa phân tích |
| UC-004 | Xem bản đồ trạm | - | Chưa phân tích |
| UC-005 | Thuê xe | P07-uc-analysis/UC-005-rent-bike-analysis.md | Đã phân tích |
| UC-006 | Xin thêm thời gian miễn phí | - | Chưa phân tích |
| UC-007 | Trả xe | P07-uc-analysis/UC-007-return-bike-analysis.md | Đã phân tích |
| UC-008 | Báo xe hỏng | - | Chưa phân tích |
| UC-009 | Ghi nhận xe thất lạc | P07-uc-analysis/UC-009-record-lost-bike-analysis.md | Đã phân tích |
| UC-010 đến UC-012 | Tra cứu xe chờ kiểm tra; Ghi nhận kết quả kiểm tra xe; Xem trạm sắp hết xe, sắp đầy | - | Chưa phân tích |
| UC-013 | Lập lệnh điều chuyển | P07-uc-analysis/UC-013-create-transfer-order-analysis.md | Đã phân tích |
| UC-014 đến UC-024 | (11 use case còn lại) | - | Chưa phân tích |

## F2. Nhật ký hợp nhất

| STT | Lớp gốc (AC, tên) | UC nguồn | Tình huống | Kết quả | Bằng chứng |
|---|---|---|---|---|---|
| 1 | AC-B-RentBikeForm | UC-005 | Giữ nguyên | Giữ | Boundary người dùng riêng của UC-005 |
| 2 | AC-B-ReturnBikeForm | UC-007 | Giữ nguyên | Giữ | Boundary người dùng riêng của UC-007 |
| 3 | AC-B-CreateTransferOrderForm | UC-013 | Giữ nguyên | Giữ | - |
| 4 | AC-B-PaymentGateway | UC-005, UC-007, UC-009 | Boundary hệ thống trùng | Giữ (P07 đã dùng chung mã); hợp 4 trách nhiệm | ACT-07 |
| 5 | AC-B-DockDevice | UC-005, UC-007 | Boundary hệ thống trùng | Giữ (P07 đã dùng chung mã); hợp 4 trách nhiệm | ACT-08 |
| 6 | AC-C-RentBikeController | UC-005 | Giữ nguyên | Giữ | - |
| 7 | AC-C-ReturnBikeController | UC-007 | Giữ nguyên | Giữ | - |
| 8 | AC-C-RecordLostBikeController | UC-009 | Giữ nguyên | Giữ | - |
| 9 | AC-C-CreateTransferOrderController | UC-013 | Giữ nguyên | Giữ | - |
| 10 | AC-E-RiderAccount | UC-005, UC-007, UC-009 | Giữ nguyên | Giữ; hợp thuộc tính | GL-13, GL-12, GL-14, GL-15 |
| 11 | AC-E-Trip | UC-005, UC-007, UC-009 | Giữ nguyên | Giữ; hợp 6 trách nhiệm | GL-04 |
| 12 | AC-E-Dock | UC-005, UC-007 | Giữ nguyên | Giữ | GL-23 |
| 13 | AC-E-Bike | UC-005, UC-007, UC-009 | Giữ nguyên | Giữ | GL-25 |
| 14 | AC-E-PaymentHold | UC-005, UC-007, UC-009 | Giữ nguyên | Giữ | GL-08 |
| 15 | AC-E-Station | UC-013 | Giữ nguyên | Giữ | GL-19 |
| 16 | AC-E-TransferOrder | UC-013 | Giữ nguyên | Giữ; đổi tên trách nhiệm "// createTransferOrder" thành "// initializeTransferOrder" để phân biệt với trách nhiệm cùng tên của control | GL-09 |

Đổi tên trách nhiệm: AC-E-TransferOrder "// createTransferOrder" --> "// initializeTransferOrder" (cùng tên, khác ý nghĩa với trách nhiệm điều phối của AC-C-CreateTransferOrderController). Không có cặp đồng nghĩa, đồng âm nào giữa các lớp.

## F3. Bảng lớp hợp nhất

| AC | Stereotype | Tên | Trách nhiệm (gộp) | Thuộc tính | Dùng trong UC | Loại boundary | Trạng thái |
|---|---|---|---|---|---|---|---|
| AC-B-RentBikeForm | boundary | RentBikeForm | // scanDockQrCode: nhận mã QR (UC-005)<br>// showRentalRejected: báo từ chối thuê (UC-005) | dockQrCode | UC-005 | Giao diện người dùng | Hoạt động |
| AC-B-ReturnBikeForm | boundary | ReturnBikeForm | // deliverInvoice: chuyển hoá đơn tới người thuê xe (UC-007) | invoiceContent, recipientEmail | UC-007 | Giao diện người dùng | Hoạt động |
| AC-B-CreateTransferOrderForm | boundary | CreateTransferOrderForm | // requestCreateTransferOrder: nhận yêu cầu lập lệnh (UC-013)<br>// specifyTransfer: nhận trạm, xe (UC-013) | fromStation, toStation, requestedBikes | UC-013 | Giao diện người dùng | Hoạt động |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestHold: yêu cầu tạm giữ (UC-005)<br>// requestCancelHold: yêu cầu huỷ tạm giữ (UC-005)<br>// requestCapture: yêu cầu thu từ khoản tạm giữ (UC-007, UC-009)<br>// requestReleaseRemainder: yêu cầu trả lại phần dư (UC-007) | - | UC-005, UC-007, UC-009 | Giao diện hệ thống | Hoạt động |
| AC-B-DockDevice | boundary | DockDevice | // sendUnlockCommand (UC-005)<br>// sendLockCommand (UC-005)<br>// reportBikeRemoved (UC-005)<br>// reportBikeReturned (UC-007) | - | UC-005, UC-007 | Giao diện thiết bị | Hoạt động |
| AC-C-RentBikeController | control | RentBikeController | // requestRental, // rejectRental, // startRemovalWait, // handleBikeRemoved, // handleRemovalTimeout (UC-005) | - | UC-005 | - | Hoạt động |
| AC-C-ReturnBikeController | control | ReturnBikeController | // handleBikeReturned, // sendInvoice (UC-007) | - | UC-007 | - | Hoạt động |
| AC-C-RecordLostBikeController | control | RecordLostBikeController | // notifyTripDurationReached (UC-009) | - | UC-009 | - | Hoạt động |
| AC-C-CreateTransferOrderController | control | CreateTransferOrderController | // createTransferOrder (UC-013) | - | UC-013 | - | Hoạt động |
| AC-E-RiderAccount | entity | RiderAccount | // checkRentalEligibility: kiểm tra BR-01, BR-02, BR-03 (UC-005)<br>// getContactEmail (UC-007)<br>// lock: khoá tài khoản theo BR-10 (UC-009) | email: Văn bản; cardReference: Văn bản; outstandingFare: Số tiền; accountStatus: Trạng thái | UC-005, UC-007, UC-009 | - | Hoạt động |
| AC-E-Trip | entity | Trip | // isOngoing (UC-005)<br>// startTrip (UC-005)<br>// endTrip (UC-007)<br>// calculateFare: BR-07 (UC-007)<br>// composeInvoice (UC-007)<br>// checkExceedsMaxDuration: BR-09 (UC-009) | startTime: Giờ; endTime: Giờ; fare: Số tiền; status: Trạng thái | UC-005, UC-007, UC-009 | - | Hoạt động |
| AC-E-Dock | entity | Dock | // findDockByQrCode (UC-005)<br>// releaseBike (UC-005)<br>// acceptBike (UC-007) | qrCode: Văn bản | UC-005, UC-007 | - | Hoạt động |
| AC-E-Bike | entity | Bike | // checkRentable: BR-04 (UC-005)<br>// getOngoingTrip (UC-007)<br>// markLost (UC-009) | status: Trạng thái | UC-005, UC-007, UC-009 | - | Hoạt động |
| AC-E-PaymentHold | entity | PaymentHold | // recordHold (UC-005)<br>// markCancelled (UC-005)<br>// recordCapture (UC-007, UC-009)<br>// recordRemainderReleased (UC-007) | holdReference: Văn bản; amount: Số tiền; capturedAmount: Số tiền; status: Trạng thái | UC-005, UC-007, UC-009 | - | Hoạt động |
| AC-E-Station | entity | Station | // findStation (UC-013) | name: Văn bản | UC-013 | - | Hoạt động |
| AC-E-TransferOrder | entity | TransferOrder | // initializeTransferOrder (UC-013) | status: Trạng thái; requestedBikes (Q-25) | UC-013 | - | Hoạt động |

## F4. Bảng quan hệ

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn UC | Bằng chứng | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| R-01 | AC-B-RentBikeForm | AC-C-RentBikeController | Association | - | - | UC-005 | tạm thời | R-UC005-01 |
| R-02 | AC-C-RentBikeController | AC-E-RiderAccount | Association | - | - | UC-005 | tạm thời | R-UC005-02 |
| R-03 | AC-E-RiderAccount | AC-E-Trip | Association | A 1 - B 0..* | rider / trips | UC-005, UC-007, UC-009 | GL-04; BR-02 | R-UC005-03, R-UC007-08, R-UC009-08 |
| R-04 | AC-C-RentBikeController | AC-E-Dock | Association | - | - | UC-005 | tạm thời | R-UC005-04 |
| R-05 | AC-C-RentBikeController | AC-E-Bike | Association | - | - | UC-005 | tạm thời | R-UC005-05 |
| R-06 | AC-C-RentBikeController | AC-B-PaymentGateway | Association | - | - | UC-005 | tạm thời | R-UC005-06 |
| R-07 | AC-C-RentBikeController | AC-E-PaymentHold | Association | - | - | UC-005 | tạm thời | R-UC005-07 |
| R-08 | AC-C-RentBikeController | AC-B-DockDevice | Association | - | - | UC-005 | tạm thời | R-UC005-08 |
| R-09 | AC-C-RentBikeController | AC-E-Trip | Association | - | - | UC-005 | tạm thời | R-UC005-09 |
| R-10 | AC-E-Dock | AC-E-Bike | Association | A 0..1 - B 0..1 | dock / dockedBike | UC-005, UC-007 | GL-23, GL-24 | R-UC005-10 |
| R-11 | AC-E-Trip | AC-E-Bike | Association | A 0..* - B 1 | trips / bike | UC-005, UC-007, UC-009 | GL-04 | R-UC005-11, R-UC007-09, R-UC009-06 |
| R-12 | AC-E-Trip | AC-E-Dock | Association | A 0..* - B 1 | - / startDock | UC-005 | GL-04 | R-UC005-12 |
| R-13 | AC-E-Trip | AC-E-PaymentHold | Association | A 0..1 - B 1 | trip / hold | UC-005, UC-007, UC-009 | GL-08 | R-UC005-13, R-UC007-11, R-UC009-07 |
| R-14 | AC-B-ReturnBikeForm | AC-C-ReturnBikeController | Association | - | - | UC-007 | tạm thời | R-UC007-01 |
| R-15 | AC-C-ReturnBikeController | AC-B-DockDevice | Association | - | - | UC-007 | tạm thời | R-UC007-02 |
| R-16 | AC-C-ReturnBikeController | AC-E-Dock | Association | - | - | UC-007 | tạm thời | R-UC007-03 |
| R-17 | AC-C-ReturnBikeController | AC-E-Bike | Association | - | - | UC-007 | tạm thời | R-UC007-04 |
| R-18 | AC-C-ReturnBikeController | AC-E-Trip | Association | - | - | UC-007 | tạm thời | R-UC007-05 |
| R-19 | AC-C-ReturnBikeController | AC-B-PaymentGateway | Association | - | - | UC-007 | tạm thời | R-UC007-06 |
| R-20 | AC-C-ReturnBikeController | AC-E-PaymentHold | Association | - | - | UC-007 | tạm thời | R-UC007-07 |
| R-21 | AC-E-Trip | AC-E-Dock | Association | A 0..* - B 0..1 | - / endDock | UC-007 | GL-04 | R-UC007-10 |
| R-22 | AC-C-RecordLostBikeController | AC-E-Trip | Association | - | - | UC-009 | tạm thời | R-UC009-01 |
| R-23 | AC-C-RecordLostBikeController | AC-E-Bike | Association | - | - | UC-009 | tạm thời | R-UC009-02 |
| R-24 | AC-C-RecordLostBikeController | AC-B-PaymentGateway | Association | - | - | UC-009 | tạm thời | R-UC009-03 |
| R-25 | AC-C-RecordLostBikeController | AC-E-PaymentHold | Association | - | - | UC-009 | tạm thời | R-UC009-04 |
| R-26 | AC-C-RecordLostBikeController | AC-E-RiderAccount | Association | - | - | UC-009 | tạm thời | R-UC009-05 |
| R-27 | AC-B-CreateTransferOrderForm | AC-C-CreateTransferOrderController | Association | - | - | UC-013 | tạm thời | R-UC013-01 |
| R-28 | AC-C-CreateTransferOrderController | AC-E-Station | Association | - | - | UC-013 | tạm thời | R-UC013-02 |
| R-29 | AC-C-CreateTransferOrderController | AC-E-TransferOrder | Association | - | - | UC-013 | tạm thời | R-UC013-03 |
| R-30 | AC-E-TransferOrder | AC-E-Station | Association | A 0..* - B 1 | - / fromStation | UC-013 | GL-09 | R-UC013-04 |
| R-31 | AC-E-TransferOrder | AC-E-Station | Association | A 0..* - B 1 | - / toStation | UC-013 | GL-09 | R-UC013-05 |
| R-32 | AC-E-Station | AC-E-Dock | Association | A 1 - B 1..* | station / docks | - | Mới ở P08; GL-19 "Địa điểm đặt một nhóm ụ khoá"; đoạn mở đầu nguồn | - |

## F5. Analysis class diagram tổng thể

File diagrams/P08-class-analysis.drawio, một trang V1 (16 lớp hoạt động, dưới ngưỡng 20).

| ID (mã AC) | Loại | Nhãn | Stereotype | Thuộc về (view) | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-RentBikeForm | Class | RentBikeForm | boundary | V1 | dockQrCode | // scanDockQrCode<br>// showRentalRejected |
| AC-B-ReturnBikeForm | Class | ReturnBikeForm | boundary | V1 | invoiceContent<br>recipientEmail | // deliverInvoice |
| AC-B-PaymentGateway | Class | PaymentGateway | boundary | V1 | - | // requestHold<br>// requestCancelHold<br>// requestCapture<br>// requestReleaseRemainder |
| AC-B-DockDevice | Class | DockDevice | boundary | V1 | - | // sendUnlockCommand<br>// sendLockCommand<br>// reportBikeRemoved<br>// reportBikeReturned |
| AC-B-CreateTransferOrderForm | Class | CreateTransferOrderForm | boundary | V1 | fromStation<br>toStation<br>requestedBikes | // requestCreateTransferOrder<br>// specifyTransfer |
| AC-C-RentBikeController | Class | RentBikeController | control | V1 | - | // requestRental<br>// rejectRental<br>// startRemovalWait<br>// handleBikeRemoved<br>// handleRemovalTimeout |
| AC-C-ReturnBikeController | Class | ReturnBikeController | control | V1 | - | // handleBikeReturned<br>// sendInvoice |
| AC-C-RecordLostBikeController | Class | RecordLostBikeController | control | V1 | - | // notifyTripDurationReached |
| AC-C-CreateTransferOrderController | Class | CreateTransferOrderController | control | V1 | - | // createTransferOrder |
| AC-E-RiderAccount | Class | RiderAccount | entity | V1 | email: Văn bản<br>cardReference: Văn bản<br>outstandingFare: Số tiền<br>accountStatus: Trạng thái | // checkRentalEligibility<br>// getContactEmail<br>// lock |
| AC-E-Trip | Class | Trip | entity | V1 | startTime: Giờ<br>endTime: Giờ<br>fare: Số tiền<br>status: Trạng thái | // isOngoing<br>// startTrip<br>// endTrip<br>// calculateFare<br>// composeInvoice<br>// checkExceedsMaxDuration |
| AC-E-Dock | Class | Dock | entity | V1 | qrCode: Văn bản | // findDockByQrCode<br>// releaseBike<br>// acceptBike |
| AC-E-Bike | Class | Bike | entity | V1 | status: Trạng thái | // checkRentable<br>// getOngoingTrip<br>// markLost |
| AC-E-PaymentHold | Class | PaymentHold | entity | V1 | holdReference: Văn bản<br>amount: Số tiền<br>capturedAmount: Số tiền<br>status: Trạng thái | // recordHold<br>// markCancelled<br>// recordCapture<br>// recordRemainderReleased |
| AC-E-Station | Class | Station | entity | V1 | name: Văn bản | // findStation |
| AC-E-TransferOrder | Class | TransferOrder | entity | V1 | status: Trạng thái<br>requestedBikes (Q-25) | // initializeTransferOrder |

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Thuộc về (view) |
|---|---|---|---|---|---|
| R-01 | AC-B-RentBikeForm | AC-C-RentBikeController | Association | - | V1 |
| R-02 | AC-C-RentBikeController | AC-E-RiderAccount | Association | - | V1 |
| R-03 | AC-E-RiderAccount | AC-E-Trip | Association | A 1 - B 0..* | V1 |
| R-04 | AC-C-RentBikeController | AC-E-Dock | Association | - | V1 |
| R-05 | AC-C-RentBikeController | AC-E-Bike | Association | - | V1 |
| R-06 | AC-C-RentBikeController | AC-B-PaymentGateway | Association | - | V1 |
| R-07 | AC-C-RentBikeController | AC-E-PaymentHold | Association | - | V1 |
| R-08 | AC-C-RentBikeController | AC-B-DockDevice | Association | - | V1 |
| R-09 | AC-C-RentBikeController | AC-E-Trip | Association | - | V1 |
| R-10 | AC-E-Dock | AC-E-Bike | Association | A 0..1 - B 0..1 | V1 |
| R-11 | AC-E-Trip | AC-E-Bike | Association | A 0..* - B 1 | V1 |
| R-12 | AC-E-Trip | AC-E-Dock | Association | A 0..* - B 1 | V1 |
| R-13 | AC-E-Trip | AC-E-PaymentHold | Association | A 0..1 - B 1 | V1 |
| R-14 | AC-B-ReturnBikeForm | AC-C-ReturnBikeController | Association | - | V1 |
| R-15 | AC-C-ReturnBikeController | AC-B-DockDevice | Association | - | V1 |
| R-16 | AC-C-ReturnBikeController | AC-E-Dock | Association | - | V1 |
| R-17 | AC-C-ReturnBikeController | AC-E-Bike | Association | - | V1 |
| R-18 | AC-C-ReturnBikeController | AC-E-Trip | Association | - | V1 |
| R-19 | AC-C-ReturnBikeController | AC-B-PaymentGateway | Association | - | V1 |
| R-20 | AC-C-ReturnBikeController | AC-E-PaymentHold | Association | - | V1 |
| R-21 | AC-E-Trip | AC-E-Dock | Association | A 0..* - B 0..1 | V1 |
| R-22 | AC-C-RecordLostBikeController | AC-E-Trip | Association | - | V1 |
| R-23 | AC-C-RecordLostBikeController | AC-E-Bike | Association | - | V1 |
| R-24 | AC-C-RecordLostBikeController | AC-B-PaymentGateway | Association | - | V1 |
| R-25 | AC-C-RecordLostBikeController | AC-E-PaymentHold | Association | - | V1 |
| R-26 | AC-C-RecordLostBikeController | AC-E-RiderAccount | Association | - | V1 |
| R-27 | AC-B-CreateTransferOrderForm | AC-C-CreateTransferOrderController | Association | - | V1 |
| R-28 | AC-C-CreateTransferOrderController | AC-E-Station | Association | - | V1 |
| R-29 | AC-C-CreateTransferOrderController | AC-E-TransferOrder | Association | - | V1 |
| R-30 | AC-E-TransferOrder | AC-E-Station | Association | A 0..* - B 1 | V1 |
| R-31 | AC-E-TransferOrder | AC-E-Station | Association | A 0..* - B 1 | V1 |
| R-32 | AC-E-Station | AC-E-Dock | Association | A 1 - B 1..* | V1 |

## F6. Rà soát lớp phân tích

| AC | Tên phản ánh đúng vai trò | Một khái niệm duy nhất | Trách nhiệm gắn kết | Cung cấp đủ hành vi cần | Yêu cầu đặc thù (BR, NFR) đã gắn | Ghi chú |
|---|---|---|---|---|---|---|
| AC-B-RentBikeForm | Đạt | Đạt | Đạt | Đạt | Đạt (NFR-05) | - |
| AC-B-ReturnBikeForm | Không đạt: kênh là email, hậu tố Form gây hiểu nhầm | Đạt | Đạt | Đạt | Đạt | Chờ Q-19 |
| AC-B-CreateTransferOrderForm | Đạt | Đạt | Đạt | Đạt | Đạt | - |
| AC-B-PaymentGateway | Đạt | Đạt | Đạt | Đạt | Đạt (NFR-06) | Hành vi lỗi chờ Q-23 |
| AC-B-DockDevice | Đạt | Đạt | Đạt | Đạt | Đạt (NFR-02, NFR-07) | - |
| AC-C-RentBikeController | Đạt | Đạt | Đạt | Đạt | Đạt (BR-05, BR-06) | - |
| AC-C-ReturnBikeController | Đạt | Đạt | Đạt | Không đạt: 4a chưa xử lý | Đạt | Q-02 |
| AC-C-RecordLostBikeController | Đạt | Đạt | Đạt | Đạt | Đạt (BR-10) | - |
| AC-C-CreateTransferOrderController | Đạt | Đạt | Đạt | Đạt | - | - |
| AC-E-RiderAccount | Đạt | Đạt | Đạt | Đạt | Đạt (BR-01, BR-02, BR-03, BR-10, NFR-04) | - |
| AC-E-Trip | Đạt | Đạt | Không đạt: composeInvoice là việc trình bày hoá đơn, khác nhóm trách nhiệm vòng đời chuyến và tính cước | Đạt | Đạt (BR-07, BR-09) | Xem Vấn đề còn mở |
| AC-E-Dock | Đạt | Đạt | Đạt | Đạt | Đạt | - |
| AC-E-Bike | Đạt | Đạt | Đạt | Đạt | Đạt (BR-04) | Giá trị trạng thái chờ Q-27 |
| AC-E-PaymentHold | Đạt | Đạt | Đạt | Đạt | Đạt (BR-05) | - |
| AC-E-Station | Đạt | Đạt | Đạt | Không đạt: chỉ có truy vấn | Không đạt: BR-14, BR-15 chưa gắn vì UC-012 chưa phân tích | Vấn đề còn mở |
| AC-E-TransferOrder | Đạt | Đạt | Đạt | Đạt | - | Q-09, Q-25 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-34 | Một ụ khoá có luôn thuộc đúng một trạm và mỗi trạm có ít nhất một ụ không? (Có / Không) | R-32 multiplicity | Đoạn mở đầu "mỗi trạm có từ 10 đến 20 ụ khoá" |

Liên quan: Q-04 (Trip.status có giá trị cho xe thất lạc không), Q-25, Q-27.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P07 | UC-013, AC-E-TransferOrder | Trách nhiệm "// createTransferOrder" trùng tên với control | Đổi thành "// initializeTransferOrder" khi chạy lại P07 UC-013 |

## Vấn đề còn mở

- 20 trên 24 use case chưa có P07 (F1). Mô hình hợp nhất chỉ phản ánh 4 use case; Station, Dock thiếu trách nhiệm của UC-004, UC-012, UC-019, UC-020.
- R-32 Station - Dock được thêm ở P08 dựa trên GL-19, không có trong VOPC nào; multiplicity "1 - 1..*" dựa trên đoạn mở đầu nguồn, chờ Q-34.
- AC-E-Trip có 6 trách nhiệm; // composeInvoice có thể tách sang lớp khác nếu Q-32 xác nhận hoá đơn phải lưu.
- Sơ đồ một trang có 32 quan hệ, trong đó 22 là association tạm thời giữa control và lớp khác; các đường cắt nhau nhiều (xem Target 9, C7.3 "cạnh không cắt qua node" không bảo đảm được khi sinh tự động).
