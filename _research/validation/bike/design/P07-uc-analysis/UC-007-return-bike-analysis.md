# P07 - Phân tích use case UC-007 Trả xe - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-007-return-bike.md 1.0; _BR-register.md; P01-actors.md 1.0; P03-usecase-model.md 1.0; P05-glossary.md 1.0; P06-supplementary-spec.md 1.0; P07-uc-analysis/UC-005-rent-bike-analysis.md 1.0 (sổ đăng ký AC) |
| Phạm vi | UC-007 |

Placeholder: UC_ID = "UC-007 Trả xe"; LUONG_CAN_VE = Không có; YEU_CAU_BO_SUNG = Không có.

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-007 Trả xe (Return Bike) |
| Tác nhân chính | ACT-01 Người thuê xe (Người) |
| Tác nhân phụ | ACT-08 Ụ khoá (Thiết bị); ACT-07 Cổng thanh toán (Hệ thống ngoài) |
| Include | Không có |
| Được include bởi | Không có |
| Extend | Không có |
| Được extend bởi | Không có |
| File P07 đã có được dùng làm sổ đăng ký AC | UC-005-rent-bike-analysis.md: AC-B-RentBikeForm, AC-B-PaymentGateway, AC-B-DockDevice, AC-C-RentBikeController, AC-E-RiderAccount, AC-E-Trip, AC-E-Dock, AC-E-Bike, AC-E-PaymentHold |

## F2. Đặc tả bổ sung

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Người thuê xe | Đẩy xe vào một ụ khoá trống ở trạm bất kỳ (BR-08). | Không đổi | BR-08 |
| 2 | Ụ khoá | Nhận diện xe và báo đã nhận xe. | Không đổi | REQ-18 |
| 3 | Hệ thống | Kết thúc chuyến đi của xe. | Hệ thống ghi nhận ụ khoá đang giữ xe, lấy chuyến đang diễn ra của xe, ghi thời điểm kết thúc là lúc nhận báo và ụ khoá trả, chuyển chuyến sang trạng thái đã kết thúc. Trường hợp xe thuộc chuyến đã bị coi là thất lạc chờ Q-04. | GL-04, GL-24 |
| 4 | Hệ thống | Tính cước chuyến đi theo thời lượng (BR-07). | Chuyến đi tính thời lượng từ thời điểm bắt đầu tới thời điểm kết thúc, trừ 30 phút miễn phí, làm tròn lên theo đơn vị 15 phút, nhân 5.000 đồng. Ảnh hưởng của thời gian miễn phí cộng thêm chờ Q-05. | BR-07, GL-05, GL-18 |
| 4a | - | Cước lớn hơn số tiền tạm giữ | Chưa quy định (Q-02); không phân bổ được | BR-05, BR-07 |
| 5 | Hệ thống | Yêu cầu Cổng thanh toán thu cước từ khoản tạm giữ. | Hệ thống lấy khoản tạm giữ của chuyến, gửi yêu cầu thu số tiền bằng cước, ghi số tiền đã thu vào khoản tạm giữ. Cước bằng 0 có gửi yêu cầu thu hay không chờ Q-31. | GL-08, NFR-06 |
| 6 | Hệ thống | Yêu cầu Cổng thanh toán hoàn lại phần tạm giữ còn dư. | Hệ thống gửi yêu cầu cho phần dư (200.000 đồng trừ cước) và ghi khoản tạm giữ đã xử lý xong; dùng API hoàn tiền hay huỷ tạm giữ chờ Q-26. | BR-05, GL-07, GL-08 |
| 7 | Hệ thống | Gửi hoá đơn chuyến đi cho người thuê xe qua email (Q-19). | Chuyến đi lập nội dung hoá đơn (thành phần chờ Q-24) và lấy email từ tài khoản của người thuê xe; hệ thống gửi hoá đơn tới email đó. | GL-06, REQ-24 |

## F3. Tìm lớp phân tích

### F3.1 Boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-01 Người thuê xe | Người | ReturnBikeForm | Giao diện người dùng | Mới (AC-B-ReturnBikeForm) | Cặp ACT-01 - UC-007; người thuê xe chỉ nhận hoá đơn (A3: tác nhân chỉ nhận thông tin vẫn cần boundary). Hậu tố Form theo HAU_TO_TEN_LOP dù kênh là email (Q-19) |
| ACT-08 Ụ khoá | Thiết bị | DockDevice | Giao diện thiết bị | Tái dùng AC-B-DockDevice (UC-005), bổ sung trách nhiệm | Cùng thiết bị |
| ACT-07 Cổng thanh toán | Hệ thống ngoài | PaymentGateway | Giao diện hệ thống | Tái dùng AC-B-PaymentGateway (UC-005), bổ sung trách nhiệm | Cùng hệ thống ngoài |

### F3.2 Lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Người thuê xe | Bước 1 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-01 |
| 2 | Xe | Bước 1, 2, 3 | Entity (AC-E-Bike) | Tái dùng |
| 3 | Ụ khoá, ụ khoá trống | Bước 1, 2 | Entity (AC-E-Dock) | Tái dùng; "trống" là trạng thái (GL-24) |
| 4 | Trạm | Bước 1, BR-08 | Loại - là tác nhân hoặc ngoài phạm vi | Không tham gia hành vi của UC-007 (cùng lý do như UC-005) |
| 5 | Chuyến đi | Bước 3, 4 | Entity (AC-E-Trip) | Tái dùng |
| 6 | Cước | Bước 4, 5 | Loại - thuộc tính của Trip | GL-05: số tiền của một chuyến, không có định danh riêng |
| 7 | Thời lượng | Bước 4 | Loại - thuộc tính của Trip | Suy ra từ thời điểm bắt đầu và kết thúc |
| 8 | 30 phút, 5.000 đồng, 15 phút | BR-07 | Loại - tham số của quy tắc BR-07 | Hằng số của quy tắc; liên hệ với bảng giá cước chờ Q-15 |
| 9 | Cổng thanh toán | Bước 5, 6 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-07 |
| 10 | Khoản tạm giữ, phần tạm giữ còn dư | Bước 5, 6 | Entity (AC-E-PaymentHold) | Tái dùng; "phần dư" là thuộc tính suy ra |
| 11 | Hoá đơn | Bước 7 | Loại - thao tác hoặc sự kiện | Nguồn chỉ nói "gửi hoá đơn"; không nói hệ thống lưu hoặc tra lại hoá đơn. Nếu phải lưu thì thành entity (Q-32) |
| 12 | Email | Bước 7 | Loại - thuộc tính của RiderAccount | REQ-02: tài khoản đăng ký bằng email |
| 13 | Thời điểm kết thúc, ụ khoá trả | Bước 3 (bổ sung) | Loại - thuộc tính của Trip | Hậu điều kiện UC-007 |
| 14 | Hệ thống | Mọi bước | Loại - mơ hồ | - |

### F3.3 Control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do |
|---|---|---|---|
| ReturnBikeController | UC-007 | Mới (AC-C-ReturnBikeController) | Một control cho mỗi use case |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-ReturnBikeForm | boundary | ReturnBikeForm | // deliverInvoice: chuyển hoá đơn tới người thuê xe | invoiceContent<br>recipientEmail | 7 | Giao diện người dùng | Mới | GL-06 |
| AC-B-DockDevice | boundary | DockDevice | // reportBikeReturned: nhận báo ụ đã nhận xe | - | 2 | Giao diện thiết bị | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-23 |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestCapture: gửi yêu cầu thu tiền từ khoản tạm giữ<br>// requestReleaseRemainder: gửi yêu cầu trả lại phần dư | - | 5, 6 | Giao diện hệ thống | Tái dùng từ UC-005, bổ sung trách nhiệm | - |
| AC-C-ReturnBikeController | control | ReturnBikeController | // handleBikeReturned: điều phối kết thúc chuyến, tính cước, thu cước, hoàn dư<br>// sendInvoice: điều phối gửi hoá đơn | - | 2 đến 7 | - | Mới | - |
| AC-E-Dock | entity | Dock | // acceptBike: ghi nhận ụ đang giữ xe | - | 3 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-23 |
| AC-E-Bike | entity | Bike | // getOngoingTrip: cho biết chuyến đang diễn ra của xe | - | 3 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-25 |
| AC-E-Trip | entity | Trip | // endTrip: kết thúc chuyến, ghi thời điểm và ụ trả<br>// calculateFare: tính cước theo BR-07<br>// composeInvoice: lập nội dung hoá đơn | endTime: Giờ<br>fare: Số tiền | 3, 4, 7 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-04, GL-05 |
| AC-E-PaymentHold | entity | PaymentHold | // recordCapture: ghi số tiền đã thu<br>// recordRemainderReleased: ghi phần dư đã trả lại | capturedAmount: Số tiền | 5, 6 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | GL-08 |
| AC-E-RiderAccount | entity | RiderAccount | // getContactEmail: cho biết email nhận hoá đơn | email: Văn bản | 7 | - | Tái dùng từ UC-005, bổ sung trách nhiệm | - |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 2 | // reportBikeReturned | AC-B-DockDevice | Giao tiếp tác nhân | - |
| 2 | // handleBikeReturned | AC-C-ReturnBikeController | Controller | - |
| 3 | // acceptBike | AC-E-Dock | Information Expert | - |
| 3 | // getOngoingTrip | AC-E-Bike | Information Expert | Có thể hỏi Trip theo xe; chọn Bike vì quan hệ Bike - Trip đã có và xe là dữ liệu ụ báo về |
| 3 | // endTrip | AC-E-Trip | Information Expert | - |
| 4 | // calculateFare | AC-E-Trip | Information Expert | Trip giữ thời điểm bắt đầu, kết thúc; tham số BR-07 là hằng số của quy tắc (Q-15 nếu thuộc bảng giá cước) |
| 5 | // requestCapture | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 5 | // recordCapture | AC-E-PaymentHold | Information Expert | - |
| 6 | // requestReleaseRemainder | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 6 | // recordRemainderReleased | AC-E-PaymentHold | Information Expert | - |
| 7 | // composeInvoice | AC-E-Trip | Information Expert | Nội dung hoá đơn nằm ở Trip và RiderAccount; giao Trip vì giữ phần lớn dữ liệu, hỏi RiderAccount qua quan hệ R-UC007-08 |
| 7 | // getContactEmail | AC-E-RiderAccount | Information Expert | - |
| 7 | // sendInvoice, // deliverInvoice | AC-C-ReturnBikeController, AC-B-ReturnBikeForm | Controller; Giao tiếp tác nhân | - |

## F5. Sequence diagram phân tích

### SD1 - Luồng chính

File diagrams/P07-sequence-UC-007.drawio. Tác nhân chính không gửi message: bước 1 là thao tác vật lý trên ụ khoá; tương tác bắt đầu từ ụ khoá (tác nhân phụ). Luồng 4a không có hành động (Q-02), thể hiện bằng note N-4a.

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
|---|---|---|---|---|---|
| A-01 | Actor | Người thuê xe | - | - | ACT-01 |
| L-RTF | Lifeline | :ReturnBikeForm | «boundary» | - | AC-B-ReturnBikeForm |
| L-RTC | Lifeline | :ReturnBikeController | «control» | - | AC-C-ReturnBikeController |
| L-DK | Lifeline | :Dock | «entity» | - | AC-E-Dock |
| L-BK | Lifeline | :Bike | «entity» | - | AC-E-Bike |
| L-TR | Lifeline | :Trip | «entity» | - | AC-E-Trip |
| L-PH | Lifeline | :PaymentHold | «entity» | - | AC-E-PaymentHold |
| L-RA | Lifeline | :RiderAccount | «entity» | - | AC-E-RiderAccount |
| L-PG | Lifeline | :PaymentGateway | «boundary» | - | AC-B-PaymentGateway |
| A-07 | Actor | Cổng thanh toán | - | - | ACT-07 |
| L-DD | Lifeline | :DockDevice | «boundary» | - | AC-B-DockDevice |
| A-08 | Actor | Ụ khoá | - | - | ACT-08 |

| STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|
| 1 | A-08 | L-DD | // reportBikeReturned (ụ khoá, xe) | Bất đồng bộ | - | 2 |
| 1.1 | L-DD | L-RTC | // handleBikeReturned (ụ khoá, xe) | Đồng bộ | - | 2 |
| 1.1.1 | L-RTC | L-DK | // acceptBike (xe) | Đồng bộ | - | 3 |
| 1.1.2 | L-RTC | L-BK | // getOngoingTrip | Đồng bộ | - | 3 |
| 1.1.2 (trả về) | L-BK | L-RTC | chuyến đang diễn ra của xe | Trả về | - | 3 |
| 1.1.3 | L-RTC | L-TR | // endTrip (thời điểm kết thúc, ụ khoá trả) | Đồng bộ | - | 3 |
| 1.1.4 | L-RTC | L-TR | // calculateFare (BR-07) | Đồng bộ | - | 4 |
| 1.1.4 (trả về) | L-TR | L-RTC | cước | Trả về | - | 4 |
| 1.1.5 | L-RTC | L-PG | // requestCapture (cước, khoản tạm giữ) | Đồng bộ | - | 5 |
| 1.1.5.1 | L-PG | A-07 | // captureHold | Đồng bộ | - | 5 |
| 1.1.6 | L-RTC | L-PH | // recordCapture (cước) | Đồng bộ | - | 5 |
| 1.1.7 | L-RTC | L-PG | // requestReleaseRemainder (phần dư, Q-26) | Đồng bộ | - | 6 |
| 1.1.7.1 | L-PG | A-07 | // releaseRemainder | Đồng bộ | - | 6 |
| 1.1.8 | L-RTC | L-PH | // recordRemainderReleased | Đồng bộ | - | 6 |
| 1.1.9 | L-RTC | L-TR | // composeInvoice (Q-24) | Đồng bộ | - | 7 |
| 1.1.9.1 | L-TR | L-RA | // getContactEmail | Đồng bộ | - | 7 |
| 1.1.9 (trả về) | L-TR | L-RTC | nội dung hoá đơn, email | Trả về | - | 7 |
| 1.1.10 | L-RTC | L-RTF | // sendInvoice (nội dung hoá đơn, email) | Đồng bộ | - | 7 |
| 1.1.10.1 | L-RTF | A-01 | // deliverInvoice | Bất đồng bộ | - | 7 |

## F6. Quy tắc tương tác

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-007.drawio.

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú |
|---|---|---|---|---|---|
| A-01 | Actor | Người thuê xe | - | - | - |
| L-RTF | Object | :ReturnBikeForm | «boundary» | - | - |
| L-RTC | Object | :ReturnBikeController | «control» | - | - |
| L-DK | Object | :Dock | «entity» | - | - |
| L-BK | Object | :Bike | «entity» | - | - |
| L-TR | Object | :Trip | «entity» | - | - |
| L-RA | Object | :RiderAccount | «entity» | - | - |
| L-PH | Object | :PaymentHold | «entity» | - | - |
| L-PG | Object | :PaymentGateway | «boundary» | - | - |
| A-07 | Actor | Cổng thanh toán | - | - | - |
| L-DD | Object | :DockDevice | «boundary» | - | - |
| A-08 | Actor | Ụ khoá | - | - | - |

| ID | Nguồn | Đích | Loại | Nhãn | Chiều message |
|---|---|---|---|---|---|
| K01 | A-01 | L-RTF | Link | 1.1.10.1: // deliverInvoice (<--) | Đích-->Nguồn |
| K02 | L-RTF | L-RTC | Link | 1.1.10: // sendInvoice (<--) | Đích-->Nguồn |
| K03 | L-RTC | L-DD | Link | 1.1: // handleBikeReturned (<--) | Đích-->Nguồn |
| K04 | L-DD | A-08 | Link | 1: // reportBikeReturned (<--) | Đích-->Nguồn |
| K05 | L-RTC | L-DK | Link | 1.1.1: // acceptBike (-->) | Nguồn-->Đích |
| K06 | L-RTC | L-BK | Link | 1.1.2: // getOngoingTrip (-->) | Nguồn-->Đích |
| K07 | L-RTC | L-TR | Link | 1.1.3: // endTrip (-->)<br>1.1.4: // calculateFare (-->)<br>1.1.9: // composeInvoice (-->) | Nguồn-->Đích |
| K08 | L-TR | L-RA | Link | 1.1.9.1: // getContactEmail (-->) | Nguồn-->Đích |
| K09 | L-RTC | L-PG | Link | 1.1.5: // requestCapture (-->)<br>1.1.7: // requestReleaseRemainder (-->) | Nguồn-->Đích |
| K10 | L-PG | A-07 | Link | 1.1.5.1: // captureHold (-->)<br>1.1.7.1: // releaseRemainder (-->) | Nguồn-->Đích |
| K11 | L-RTC | L-PH | Link | 1.1.6: // recordCapture (-->)<br>1.1.8: // recordRemainderReleased (-->) | Nguồn-->Đích |

## F8. VOPC

File diagrams/P07-class-UC-007.drawio.

| ID (mã AC) | Loại | Nhãn | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm |
|---|---|---|---|---|---|---|
| AC-B-ReturnBikeForm | Class | ReturnBikeForm | boundary | - | invoiceContent<br>recipientEmail | // deliverInvoice |
| AC-B-PaymentGateway | Class | PaymentGateway | boundary | - | - | // requestCapture<br>// requestReleaseRemainder |
| AC-B-DockDevice | Class | DockDevice | boundary | - | - | // reportBikeReturned |
| AC-C-ReturnBikeController | Class | ReturnBikeController | control | - | - | // handleBikeReturned<br>// sendInvoice |
| AC-E-Dock | Class | Dock | entity | - | - | // acceptBike |
| AC-E-Bike | Class | Bike | entity | - | - | // getOngoingTrip |
| AC-E-Trip | Class | Trip | entity | - | endTime: Giờ<br>fare: Số tiền | // endTrip<br>// calculateFare<br>// composeInvoice |
| AC-E-PaymentHold | Class | PaymentHold | entity | - | capturedAmount: Số tiền | // recordCapture<br>// recordRemainderReleased |
| AC-E-RiderAccount | Class | RiderAccount | entity | - | email: Văn bản | // getContactEmail |

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC007-01 | AC-B-ReturnBikeForm | AC-C-ReturnBikeController | Association | - | - | K02; tạm thời |
| R-UC007-02 | AC-C-ReturnBikeController | AC-B-DockDevice | Association | - | - | K03; tạm thời |
| R-UC007-03 | AC-C-ReturnBikeController | AC-E-Dock | Association | - | - | K05; tạm thời |
| R-UC007-04 | AC-C-ReturnBikeController | AC-E-Bike | Association | - | - | K06; tạm thời |
| R-UC007-05 | AC-C-ReturnBikeController | AC-E-Trip | Association | - | - | K07; tạm thời |
| R-UC007-06 | AC-C-ReturnBikeController | AC-B-PaymentGateway | Association | - | - | K09; tạm thời |
| R-UC007-07 | AC-C-ReturnBikeController | AC-E-PaymentHold | Association | - | - | K11; tạm thời |
| R-UC007-08 | AC-E-Trip | AC-E-RiderAccount | Association | A 0..* - B 1 | - | K08; GL-04 |
| R-UC007-09 | AC-E-Bike | AC-E-Trip | Association | A 1 - B 0..* | - / ongoingTrip | Trả về của 1.1.2; GL-04 "sử dụng một xe"; BR-02 |
| R-UC007-10 | AC-E-Trip | AC-E-Dock | Association | A 0..* - B 0..1 | - / endDock | Bước 3 (bổ sung): ụ khoá trả; GL-04 |
| R-UC007-11 | AC-E-Trip | AC-E-PaymentHold | Association | A 0..1 - B 1 | - | Bước 5 "thu cước từ khoản tạm giữ"; GL-08 |

## F9. Ma trận truy vết

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 2 | 1, 1.1 | AC-B-DockDevice, AC-C-ReturnBikeController |
| 3 | 1.1.1, 1.1.2, 1.1.3 | AC-E-Dock, AC-E-Bike, AC-E-Trip |
| 4 | 1.1.4 | AC-E-Trip |
| 4a | - (note N-4a) | - |
| 5 | 1.1.5, 1.1.5.1, 1.1.6 | AC-B-PaymentGateway, AC-E-PaymentHold |
| 6 | 1.1.7, 1.1.7.1, 1.1.8 | AC-B-PaymentGateway, AC-E-PaymentHold |
| 7 | 1.1.9, 1.1.9.1, 1.1.10, 1.1.10.1 | AC-E-Trip, AC-E-RiderAccount, AC-C-ReturnBikeController, AC-B-ReturnBikeForm |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-31 | Khi cước bằng 0 (chuyến không quá 30 phút), hệ thống có gửi yêu cầu thu 0 đồng hay chỉ trả lại toàn bộ khoản tạm giữ? | UC-007 bước 5, 6 | Mục 4 |
| Q-32 | Hệ thống có phải lưu hoá đơn để tra cứu hoặc gửi lại không? (Có / Không) | Entity Invoice; UC-016 | "gửi hoá đơn qua email" (Mục 4) |

Liên quan từ bước trước: Q-02, Q-04, Q-05, Q-15, Q-19, Q-23, Q-24, Q-26.

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 1: bước 4a có trong F2 nhưng không có message (Q-02); không sửa được khi chưa có câu trả lời.
- Target 3: ACT-01 không tương tác trực tiếp trong luồng; boundary ReturnBikeForm chỉ phục vụ việc nhận hoá đơn. Tên theo quy tắc hậu tố Form dù kênh là email; F3.1 không có dạng tên cho boundary chỉ gửi thông tin ra ngoài.
- AC-E-Bike có trách nhiệm // getOngoingTrip dạng truy vấn (anemic trong UC này); UC-005 đã có trách nhiệm hành vi // checkRentable.
- F2 bước 5 và 6 không có luồng ngoại lệ khi cổng thanh toán lỗi (Q-23).
