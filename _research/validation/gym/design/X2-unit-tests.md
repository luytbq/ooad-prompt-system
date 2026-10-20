# X2 - Thiết kế unit test - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | X2 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (CHE_DO_GIA_DINH NGHIEM_NGAT, CONG_NGHE TypeScript với NestJS, MUC_CHI_TIET GON); P12-class-design/PKG-15-PKG-29-group-class.md (1.0; F1, F2, F3, F5, F6, F7, Câu hỏi mở, Vấn đề còn mở); P06-supplementary-spec.md (BR-06 đến BR-14); P04-uc-specs/UC-010-book-class-spot.md và UC-015-cancel-under-booked-class.md (1.0; mục 1 đến 8, Câu hỏi mở); P04-uc-specs/_BR-register.md (BR-06 đến BR-14). P13-data-model.md: không dùng. Mã nguồn: chưa có. PHAM_VI_TEST: các phương thức quan trọng của PKG-15 và PKG-29, AI chọn trong giới hạn khoảng 10 operation hoặc 60 TC. MUC_TIEU_PHU: độ phủ nhánh C1. SINH_MA_TEST: Có, Jest (TypeScript, NestJS). MA_TC_BAT_DAU: Không có. YEU_CAU_BO_SUNG: Q lớn nhất hiện có là Q-107 |
| Phạm vi | DC-GroupClass, DC-MemberBookingQuota, DC-BookClassSpotHandler, DC-CancelUnderBookedClassHandler (PKG-15, PKG-29) |
| Mã Q, ASM cuối đã cấp | Q-109; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bảng chọn operation

MUC_CHI_TIET là GON nên không lập sơ đồ CFG .drawio; đồ thị luồng điều khiển ghi bằng bảng node, bảng cạnh ở F2.x.6.

| DC.operation | Tiêu chí | Ưu tiên | Chọn |
|---|---|---|---|
| DC-BookClassSpotHandler.getClassSchedule | điều phối UC (chỉ ủy quyền) | Thấp | Không: chỉ ủy quyền IF-14.findSchedule, không có logic |
| DC-BookClassSpotHandler.bookClass | điều phối UC, BR-08, BR-09, BR-11, rẽ nhánh, kiểm tra hợp lệ | Cao | Có |
| DC-BookClassSpotHandler.joinWaitlist | điều phối UC, BR-12 | Trung bình | Không: vượt giới hạn khoảng 10 operation; kết cục nghiệp vụ chờ Q-106; hành vi thật nằm ở DC-GroupClass.addToWaitlist đã chọn |
| DC-CancelUnderBookedClassHandler.handleMarkDue | điều phối UC, BR-13, nhiều luồng thay thế | Cao | Có |
| DC-CancelUnderBookedClassHandler.onModuleInit | gọi hệ thống ngoài (đăng ký bộ nhận mốc) | Thấp | Không: chỉ đăng ký với IF-06, không có logic |
| DC-CancelUnderBookedClassHandler.cancelAbsenceMark | gọi hệ thống ngoài | Thấp | Không: ủy quyền nguyên lời gọi IF-06.cancelMark; kiểm gián tiếp qua TC-046, TC-054 |
| DC-CancelUnderBookedClassHandler.cancelWaitlistTransferMark | gọi hệ thống ngoài | Thấp | Không: ủy quyền nguyên lời gọi IF-06.cancelMark; kiểm gián tiếp qua TC-046, TC-055 |
| DC-CancelUnderBookedClassHandler.notifyBookedMembers | BR-14, vòng lặp, rẽ nhánh theo kênh, gọi hệ thống ngoài | Cao | Có |
| DC-CancelUnderBookedClassHandler.composeClassCancelledNotice | chuyển đổi, định dạng dữ liệu | Trung bình | Không: câu chữ thông báo chờ Q-66, chỉ có hậu điều kiện nội dung không rỗng, kiểm qua TC-057 |
| DC-GroupClass.GroupClass (constructor) | kiểm tra hợp lệ dữ liệu vào, sự kiện ST-01 (create) | Cao | Có |
| DC-GroupClass.provideClassInfo | chuyển đổi (getter) | Thấp | Không: getter không có logic; được dùng làm oracle ở TC-001, TC-003, TC-035 |
| DC-GroupClass.assessBookability | BR-06, BR-07, rẽ nhánh | Cao | Có |
| DC-GroupClass.hasAvailableSpot | BR-10, BR-11 | Cao | Có |
| DC-GroupClass.reserveSpot | BR-11, sự kiện ST-01 | Cao | Có |
| DC-GroupClass.addToWaitlist | BR-12, sự kiện ST-01 | Cao | Có |
| DC-GroupClass.assessCancellation | BR-13, rẽ nhánh | Cao | Có |
| DC-GroupClass.cancelClass | sự kiện ST-01 | Cao | Có |
| DC-GroupClass.collectBookedMembers | vòng lặp, loại trùng | Cao | Có |
| DC-GroupClass.getStatus | getter | Thấp | Không: getter không có logic; dùng làm công cụ quan sát hậu điều kiện |
| DC-GroupClass.getBookedCount | getter dẫn xuất | Thấp | Không: đếm số phần tử bookings, không có logic; dùng làm công cụ quan sát hậu điều kiện |
| DC-ClassBooking.ClassBooking (constructor) | khởi tạo | Thấp | Không: chỉ gán thuộc tính; kiểm qua TC-003, TC-027 |
| DC-ClassBooking.provideBookedMember | getter | Thấp | Không: getter không có logic; kiểm qua TC-027, TC-028 |
| DC-Waitlist.Waitlist (constructor) | khởi tạo | Thấp | Không: khởi tạo danh sách rỗng, kiểm qua TC-011 |
| DC-Waitlist.addMember | sắp thứ tự, tính vị trí | Trung bình | Không: quy tắc thứ tự chờ Q-61; kiểm gián tiếp qua TC-011, TC-012 (vị trí đứng đầu và vị trí dương) |
| DC-Waitlist.compareWaitOrder | tính toán thứ tự | Trung bình | Không: thân hàm chưa đặc tả được (Q-61) |
| DC-Waitlist.contains | truy vấn | Thấp | Không: truy vấn không có logic |
| DC-MemberBookingQuota.hasReachedDailyLimit | BR-08, tính toán khoảng ngày, gọi kho dữ liệu | Cao | Có |
| IF-14.findSchedule | interface | Thấp | Không: interface, không có hiện thực trong phạm vi; được thay bằng test double |
| IF-14.findByIdForUpdate | interface | Thấp | Không: như trên |
| IF-14.save | interface | Thấp | Không: như trên |
| IF-14.countMemberBookingsBetween | interface | Thấp | Không: như trên |
| IF-14.runInTransaction | interface | Thấp | Không: như trên; hiện thực ở PKG-20 (ngoài phạm vi) |
| IF-16.now | interface | Thấp | Không: interface đồng hồ, được thay bằng stub |

Tổng: 12 operation được chọn (ctor, reserveSpot, hasAvailableSpot, addToWaitlist, cancelClass, assessCancellation, assessBookability, collectBookedMembers của DC-GroupClass; hasReachedDailyLimit; bookClass; handleMarkDue; notifyBookedMembers) với 60 test case, ở mức trần của giới hạn 60 TC.

## F2. Phân tích kỹ thuật cho từng operation

Quy ước chung: hội viên M1, M2, ... là đối tượng DC-Member giả lập (stub) chỉ có getId(); lớp C1 là loại Yoga, phòng Phòng 2, huấn luyện viên Nguyễn Thị Lan, giờ học 18:00 ngày 26/10/2026; thời điểm now = 10:00 ngày 25/10/2026. Mọi điều kiện đầu của DC-GroupClass dựng được bằng operation công khai của P12 (constructor, reserveSpot, addToWaitlist, cancelClass), không cần bộ dựng chỉ có ở test. Hậu điều kiện về danh sách chờ của addToWaitlist không quan sát được qua operation công khai hiện có: các TC dùng operation đề xuất DC-GroupClass.isOnWaitlist(member): boolean (xem Đề xuất sửa artifact trước).

### F2.1 DC-GroupClass.GroupClass (constructor)

F2.1.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | GroupClass(id: string, classType: string, room: string, trainer: string, startTime: Date, capacity: number) | P12 F2 |
| Tiền điều kiện | capacity >= 0 (số nguyên, F7) | P12 F2, F7 |
| Hậu điều kiện | status = SCHEDULED; chưa có chỗ đã đặt và danh sách chờ | P12 F2; ST-01 T1 |
| Ngoại lệ | Không nêu | P12 F2 |
| Điều kiện hợp lệ | capacity: số nguyên không âm; BR-10 sức chứa theo phòng (Q-03) | P12 F7; BR-10 |
| Không áp dụng | F2.1.4 (một điều kiện), F2.1.6 (không có thiết kế method ở P12 F3 và không có mã nguồn: C0, C1 ghi Đo khi có mã nguồn) | |

F2.1.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-01 | capacity | số nguyên >= 0 | Hợp lệ | 40 | P12 F2 tiền điều kiện |
| EC-02 | capacity | số nguyên < 0 | Không hợp lệ | -1 | P12 F2 tiền điều kiện (hành vi không nêu: Q-108, không thiết kế TC) |
| EC-03 | capacity | không phải số nguyên | Không hợp lệ | 2.5 | P12 F7 {số nguyên} (hành vi không nêu: Q-108, không thiết kế TC) |

F2.1.3. Giá trị biên:

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-01 | min của EC-01 | 0 | EC-01 | SCHEDULED, getBookedCount() = 0 |
| BV-02 | ngay ngoài min của EC-01 | -1 | EC-02 | Chưa xác định: chờ Q-108 (không có TC) |

F2.1.5. Chuyển trạng thái:

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| (initial) | create(id, classType, room, trainer, startTime, capacity) | không có guard | Tạo lớp | Scheduled | ST-01 T1 (TC-001, TC-002) |

F2.1.7. Test double: không có phụ thuộc; không cần test double.

### F2.2 DC-GroupClass.reserveSpot

F2.2.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | reserveSpot(member: Member): ClassInfo | P12 F2 |
| Tiền điều kiện | status SCHEDULED; số chỗ đã đặt nhỏ hơn capacity tại lúc gọi | P12 F2; BR-11 |
| Hậu điều kiện | getBookedCount() tăng 1; lớp có thêm chỗ của hội viên; trả DC-ClassInfo | P12 F2; UC-010 bước 8 |
| Ngoại lệ | DC-SpotUnavailableException (đã đủ chỗ); DC-InvalidClassStateException (lớp CANCELLED) | P12 F2 |
| BR | BR-11 số chỗ đã đặt không vượt sức chứa | P06; UC-010 |
| Luồng thay thế | UC-010 7a (đủ chỗ), 5a (lớp đã huỷ) | P04 |
| Không áp dụng | không có | |

F2.2.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-04 | status | SCHEDULED | Hợp lệ | SCHEDULED | P12 F2 |
| EC-05 | status | CANCELLED | Không hợp lệ | CANCELLED | P12 F2 |
| EC-06 | số chỗ đã đặt so với capacity | bookedCount < capacity | Hợp lệ | 0 trên 3 | BR-11 |
| EC-07 | số chỗ đã đặt so với capacity | bookedCount = capacity | Không hợp lệ | 3 trên 3 | BR-11 |
| EC-08 | member | null hoặc không phải hội viên | Không hợp lệ | null | P12 F2 (hành vi không nêu: Q-108, không thiết kế TC) |

Lớp bookedCount > capacity không thể xảy ra vì bất biến BR-11 (N/A).

F2.2.3. Giá trị biên:

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-03 | min của EC-06 | bookedCount 0, capacity 3 | EC-06 | bookedCount = 1 |
| BV-04 | max của EC-06 | bookedCount 2, capacity 3 | EC-06 | bookedCount = 3 |
| BV-05 | min của EC-07 | bookedCount 3, capacity 3 | EC-07 | DC-SpotUnavailableException, bookedCount vẫn 3 |

F2.2.4. Bảng quyết định (căn cứ: P12 F2 ngoại lệ; thứ tự khi cả hai điều kiện sai không được F2 hay P04 nêu nên không gộp):

```text
| Điều kiện / Hành động | R1 | R2 | R3 | R4 |
| C1: lớp đã huỷ | N | N | Y | Y |
| C2: đã đủ chỗ | N | Y | N | Y |
| A1: thêm chỗ, trả ClassInfo | X | - | - | - |
| A2: ném SpotUnavailable | - | X | - | ? (Q-109) |
| A3: ném InvalidClassState | - | - | X | ? (Q-109) |
```
Các quy tắc R1 đến R4 mang mã DT1-R1 đến DT1-R4. DT1-R1: TC-003, TC-004. DT1-R2: TC-005. DT1-R3: TC-006. DT1-R4: TC-007 (chưa xác định).

F2.2.5. Chuyển trạng thái:

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Scheduled | reserveSpot(member) | [bookedCount < capacity] đúng | Thêm chỗ | Scheduled | ST-01 T2 (TC-003, TC-004) |
| Scheduled | reserveSpot(member) | [bookedCount < capacity] sai | Ném DC-SpotUnavailableException | Scheduled | ST-01 từ chối (TC-005) |
| Cancelled | reserveSpot(member) | không có guard | Ném DC-InvalidClassStateException | Cancelled | ST-01 từ chối (TC-006) |

F2.2.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N1 | bắt đầu | bắt đầu |
| N2 | status = CANCELLED? | quyết định |
| N3 | ném DC-InvalidClassStateException | khối lệnh |
| N4 | getBookedCount() >= capacity? | quyết định |
| N5 | ném DC-SpotUnavailableException | khối lệnh |
| N6 | tạo ClassBooking(member), thêm vào bookings, trả provideClassInfo() | khối lệnh |
| N7 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE1 | N1 | N2 |  |
| CE2 | N2 | N3 | Đúng |
| CE3 | N2 | N4 | Sai |
| CE4 | N4 | N5 | Đúng |
| CE5 | N4 | N6 | Sai |
| CE6 | N3 | N7 |  |
| CE7 | N5 | N7 |  |
| CE8 | N6 | N7 |  |

V(G) = E - N + 2 = 8 - 7 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3.

Đường đi cơ sở:

- P1: N1 --> N2 --> N3 --> N7 (TC-006)
- P2: N1 --> N2 --> N4 --> N5 --> N7 (TC-005)
- P3: N1 --> N2 --> N4 --> N6 --> N7 (TC-003)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE1 (N1 --> N2) | TC-003 |
| CE2 (N2 --> N3) | TC-006 |
| CE3 (N2 --> N4) | TC-003, TC-005 |
| CE4 (N4 --> N5) | TC-005 |
| CE5 (N4 --> N6) | TC-003, TC-004 |
| CE6 (N3 --> N7) | TC-006 |
| CE7 (N5 --> N7) | TC-005 |
| CE8 (N6 --> N7) | TC-003, TC-004 |

Độ phủ đạt được: C0 = 3/3 khối lệnh; C1 = 8/8 nhánh.

Vòng lặp: không có.

F2.2.7. Test double: DC-Member (PKG-26, chưa có P12): stub chỉ có getId(), vì P12 PKG-26 chưa chạy; lý do: cô lập khỏi lớp chưa hiện thực.

### F2.3 DC-GroupClass.hasAvailableSpot

F2.3.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | hasAvailableSpot(): boolean | P12 F2 |
| Hậu điều kiện | Trả true khi số chỗ đã đặt còn dưới sức chứa; không đổi dữ liệu | P12 F2; BR-10, BR-11 |
| BR | BR-10, BR-11 (chỗ giữ riêng chưa tính, Q-22) | P06 |
| Luồng thay thế | UC-010 7a (đủ chỗ) | P04 |
| Không áp dụng | F2.3.4 (một điều kiện), F2.3.5 (không phải sự kiện ST), F2.3.6 (không có thiết kế method ở P12 F3 và không có mã nguồn: C0, C1 ghi Đo khi có mã nguồn), F2.3.7 (không có phụ thuộc) | |

F2.3.2. Phân vùng tương đương (theo đầu ra):

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-09 | bookedCount so với capacity | bookedCount < capacity | Hợp lệ (true) | 2 trên 3 | BR-11 |
| EC-10 | bookedCount so với capacity | bookedCount >= capacity | Không hợp lệ (false) | 3 trên 3 | BR-11 |

F2.3.3. Giá trị biên:

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-06 | max của EC-09 | bookedCount 2, capacity 3 | EC-09 | true |
| BV-07 | min của EC-10 | bookedCount 3, capacity 3 | EC-10 | false |
| BV-08 | min của capacity | bookedCount 0, capacity 0 | EC-10 | false |

### F2.4 DC-GroupClass.addToWaitlist

F2.4.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | addToWaitlist(member: Member, now: Date): number | P12 F2 |
| Tiền điều kiện | status SCHEDULED; lớp đã đủ chỗ (bookedCount bằng capacity) | P12 F2; BR-12 |
| Hậu điều kiện | Danh sách chờ chứa hội viên; trả vị trí, 1 là đứng đầu | P12 F2; UC-010 Dữ liệu ra 3 |
| Ngoại lệ | DC-WaitlistNotAllowedException (lớp chưa đủ chỗ, kết cục chờ Q-106); DC-InvalidClassStateException (lớp CANCELLED) | P12 F2 |
| BR | BR-12 | P06 |
| Luồng thay thế | UC-010 7a3, 7a4 | P04 |
| Không áp dụng | không có | |

F2.4.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-11 | status | SCHEDULED | Hợp lệ | SCHEDULED | P12 F2 |
| EC-12 | status | CANCELLED | Không hợp lệ | CANCELLED | P12 F2 |
| EC-13 | số chỗ đã đặt | bookedCount >= capacity (đủ chỗ) | Hợp lệ | 2 trên 2 | BR-12 |
| EC-14 | số chỗ đã đặt | bookedCount < capacity | Không hợp lệ | 1 trên 2 | BR-12; P12 F2 |
| EC-15 | danh sách chờ | chưa có hội viên nào (Waitlist chưa tạo) | Hợp lệ | rỗng | P12 F3 bước 3; Q-84 |
| EC-16 | danh sách chờ | đã có hội viên | Hợp lệ | M3 đã chờ | P12 F3 bước 3 |
| EC-17 | member | null | Không hợp lệ | null | Hành vi không nêu: Q-108, không thiết kế TC |

F2.4.3. Giá trị biên:

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-09 | max của EC-14 | bookedCount 1, capacity 2 | EC-14 | DC-WaitlistNotAllowedException, danh sách chờ không đổi |
| BV-10 | min của EC-13 | bookedCount 2, capacity 2 | EC-13 | Trả vị trí |
| BV-11 | min của vị trí (đầu ra) | hội viên đầu tiên vào danh sách chờ | đầu ra | 1 |

F2.4.4. Bảng quyết định (không gộp: F2 và P04 không nêu thứ tự khi cả hai ngoại lệ cùng áp dụng):

```text
| Điều kiện / Hành động | R1 | R2 | R3 | R4 |
| C1: lớp đã huỷ | N | N | Y | Y |
| C2: lớp đã đủ chỗ | Y | N | Y | N |
| A1: thêm vào danh sách chờ, trả vị trí | X | - | - | - |
| A2: ném WaitlistNotAllowed | - | X | - | ? (Q-109) |
| A3: ném InvalidClassState | - | - | X | ? (Q-109) |
```
Các quy tắc mang mã DT2-R1 đến DT2-R4: TC-011, TC-012; TC-013; TC-014; TC-015 (chưa xác định).

F2.4.5. Chuyển trạng thái:

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Scheduled | addToWaitlist(member, now) | [bookedCount >= capacity] đúng | Thêm mục chờ | Scheduled | ST-01 T3 (TC-011, TC-012) |
| Scheduled | addToWaitlist(member, now) | [bookedCount >= capacity] sai | Ném DC-WaitlistNotAllowedException | Scheduled | ST-01 từ chối (TC-013) |
| Cancelled | addToWaitlist(member, now) | không có guard | Ném DC-InvalidClassStateException | Cancelled | ST-01 từ chối (TC-014) |

F2.4.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N8 | bắt đầu | bắt đầu |
| N9 | status = CANCELLED? | quyết định |
| N10 | ném DC-InvalidClassStateException | khối lệnh |
| N11 | getBookedCount() < capacity? | quyết định |
| N12 | ném DC-WaitlistNotAllowedException | khối lệnh |
| N13 | waitlist chưa có (rỗng)? | quyết định |
| N14 | tạo DC-Waitlist mới | khối lệnh |
| N15 | trả waitlist.addMember(member, now) | khối lệnh |
| N16 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE9 | N8 | N9 |  |
| CE10 | N9 | N10 | Đúng |
| CE11 | N9 | N11 | Sai |
| CE12 | N11 | N12 | Đúng |
| CE13 | N11 | N13 | Sai |
| CE14 | N13 | N14 | Đúng |
| CE15 | N13 | N15 | Sai |
| CE16 | N14 | N15 |  |
| CE17 | N10 | N16 |  |
| CE18 | N12 | N16 |  |
| CE19 | N15 | N16 |  |

V(G) = E - N + 2 = 11 - 9 + 2 = 4; kiểm tra bằng số điểm quyết định nhị phân + 1 = 3 + 1 = 4.

Đường đi cơ sở:

- P1: N8 --> N9 --> N10 --> N16 (TC-014)
- P2: N8 --> N9 --> N11 --> N12 --> N16 (TC-013)
- P3: N8 --> N9 --> N11 --> N13 --> N14 --> N15 --> N16 (TC-011)
- P4: N8 --> N9 --> N11 --> N13 --> N15 --> N16 (TC-012)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE9 (N8 --> N9) | TC-011 |
| CE10 (N9 --> N10) | TC-014 |
| CE11 (N9 --> N11) | TC-011, TC-013 |
| CE12 (N11 --> N12) | TC-013 |
| CE13 (N11 --> N13) | TC-011, TC-012 |
| CE14 (N13 --> N14) | TC-011 |
| CE15 (N13 --> N15) | TC-012 |
| CE16 (N14 --> N15) | TC-011 |
| CE17 (N10 --> N16) | TC-014 |
| CE18 (N12 --> N16) | TC-013 |
| CE19 (N15 --> N16) | TC-011, TC-012 |

Độ phủ đạt được: C0 = 4/4 khối lệnh; C1 = 11/11 nhánh.

Vòng lặp: không có.

F2.4.7. Test double: DC-Member stub (như F2.2.7); DC-Waitlist, DC-WaitlistEntry dùng bản thật vì cùng package và là phần của gốc tập hợp.

### F2.5 DC-GroupClass.cancelClass

F2.5.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | cancelClass(): void | P12 F2 |
| Tiền điều kiện | status SCHEDULED | P12 F2 |
| Hậu điều kiện | status CANCELLED; chỗ đã đặt và danh sách chờ không đổi (Q-63) | P12 F2 |
| Ngoại lệ | DC-InvalidClassStateException (đã CANCELLED) | P12 F2 |
| BR | BR-13 | P06 |
| Luồng thay thế | UC-015 3 (huỷ lớp), 2a | P04 |
| Không áp dụng | F2.5.3 (trạng thái không có thứ tự số), F2.5.4 (một điều kiện), F2.5.6 (không có thiết kế method ở P12 F3 và không có mã nguồn: C0, C1 ghi Đo khi có mã nguồn), F2.5.7 (không có phụ thuộc) | |

F2.5.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-18 | status | SCHEDULED | Hợp lệ | SCHEDULED | P12 F2 |
| EC-19 | status | CANCELLED | Không hợp lệ | CANCELLED | P12 F2 |

F2.5.5. Chuyển trạng thái:

| Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
|---|---|---|---|---|---|
| Scheduled | cancelClass() | không có guard | status = CANCELLED, chỗ và danh sách chờ không đổi | Cancelled | ST-01 T4 (TC-016, TC-017) |
| Cancelled | cancelClass() | không có guard | Ném DC-InvalidClassStateException | Cancelled | ST-01 từ chối (TC-018) |

### F2.6 DC-GroupClass.assessCancellation

F2.6.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | assessCancellation(): CancellationCheck | P12 F2 |
| Hậu điều kiện | ALREADY_CANCELLED khi lớp đã huỷ; ENOUGH_BOOKINGS khi từ 3 người đặt chỗ trở lên; ngược lại CANCELLABLE; không đổi dữ liệu | P12 F2 |
| BR | BR-13 (dưới 3 người đặt chỗ thì huỷ; UNDER_BOOKED_THRESHOLD = 3) | P06; F7 |
| Luồng thay thế | UC-015 2a (đã huỷ), 2b (chưa huỷ và từ 3 người) | P04 |
| Không áp dụng | F2.6.5 (không phải sự kiện ST), F2.6.7 (không có phụ thuộc); cách đếm khi hội viên giữ nhiều chỗ chờ Q-59, chỗ giữ riêng chờ Q-22, chỗ của hội viên bị khoá chờ Q-20 | |

F2.6.2. Phân vùng tương đương (theo đầu ra):

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-20 | status | CANCELLED (bất kể số chỗ) | Không hợp lệ (ALREADY_CANCELLED) | CANCELLED, 3 chỗ | UC-015 2a |
| EC-21 | SCHEDULED, số chỗ đã đặt | 0 đến 2 | Hợp lệ (CANCELLABLE) | 2 | BR-13 |
| EC-22 | SCHEDULED, số chỗ đã đặt | từ 3 trở lên | Không hợp lệ (ENOUGH_BOOKINGS) | 3 | BR-13; UC-015 2b |

F2.6.3. Giá trị biên:

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-12 | min của EC-21 | 0 chỗ | EC-21 | CANCELLABLE |
| BV-13 | max của EC-21 | 2 chỗ | EC-21 | CANCELLABLE |
| BV-14 | min của EC-22 | 3 chỗ | EC-22 | ENOUGH_BOOKINGS |

F2.6.4. Bảng quyết định (căn cứ gộp: P04 UC-015 luồng 2b chỉ áp dụng khi lớp chưa huỷ, nên đã huỷ thì kết quả không phụ thuộc số chỗ):

```text
| Điều kiện / Hành động | R1 | R2 | R3 |
| C1: lớp đã huỷ | N | N | Y |
| C2: từ 3 chỗ trở lên | N | Y | - |
| A1: CANCELLABLE | X | - | - |
| A2: ENOUGH_BOOKINGS | - | X | - |
| A3: ALREADY_CANCELLED | - | - | X |
```
Mã DT3-R1 đến DT3-R3: TC-019, TC-020; TC-021; TC-022.

F2.6.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N17 | bắt đầu | bắt đầu |
| N18 | status = CANCELLED? | quyết định |
| N19 | trả ALREADY_CANCELLED | khối lệnh |
| N20 | n = getBookedCount() | khối lệnh |
| N21 | n < UNDER_BOOKED_THRESHOLD? | quyết định |
| N22 | trả CANCELLABLE | khối lệnh |
| N23 | trả ENOUGH_BOOKINGS | khối lệnh |
| N24 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE20 | N17 | N18 |  |
| CE21 | N18 | N19 | Đúng |
| CE22 | N18 | N20 | Sai |
| CE23 | N20 | N21 |  |
| CE24 | N21 | N22 | Đúng |
| CE25 | N21 | N23 | Sai |
| CE26 | N19 | N24 |  |
| CE27 | N22 | N24 |  |
| CE28 | N23 | N24 |  |

V(G) = E - N + 2 = 9 - 8 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3.

Đường đi cơ sở:

- P1: N17 --> N18 --> N19 --> N24 (TC-022)
- P2: N17 --> N18 --> N20 --> N21 --> N22 --> N24 (TC-019)
- P3: N17 --> N18 --> N20 --> N21 --> N23 --> N24 (TC-021)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE20 (N17 --> N18) | TC-019 |
| CE21 (N18 --> N19) | TC-022 |
| CE22 (N18 --> N20) | TC-019, TC-021 |
| CE23 (N20 --> N21) | TC-019, TC-021 |
| CE24 (N21 --> N22) | TC-019, TC-020 |
| CE25 (N21 --> N23) | TC-021 |
| CE26 (N19 --> N24) | TC-022 |
| CE27 (N22 --> N24) | TC-019, TC-020 |
| CE28 (N23 --> N24) | TC-021 |

Độ phủ đạt được: C0 = 4/4 khối lệnh; C1 = 9/9 nhánh.

Vòng lặp: không có. Điều kiện n < UNDER_BOOKED_THRESHOLD là điều kiện đơn.

### F2.7 DC-GroupClass.assessBookability

F2.7.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | assessBookability(now: Date): Bookability | P12 F2 |
| Hậu điều kiện | CLASS_CANCELLED khi lớp đã huỷ; OUTSIDE_BOOKING_WINDOW khi now ngoài thời hạn đặt chỗ; ngược lại BOOKABLE; không đổi dữ liệu | P12 F2 |
| BR | BR-06 (sớm nhất 7 ngày trước giờ học), BR-07 (tuần mới mở lúc 6 giờ sáng thứ Hai): mâu thuẫn, chờ Q-11; mốc muộn nhất chờ Q-58 | P06 |
| Luồng thay thế | UC-010 5a, 5b | P04 |
| Không áp dụng | F2.7.3 (biên thời hạn chưa xác định được, Q-11, Q-58), F2.7.5 (không phải sự kiện ST), F2.7.7 (không có phụ thuộc) | |

F2.7.2. Phân vùng tương đương (theo đầu ra):

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-23 | status | CANCELLED | Không hợp lệ (CLASS_CANCELLED) | CANCELLED | UC-010 5a |
| EC-24 | SCHEDULED, now so với thời hạn | trong thời hạn | Hợp lệ (BOOKABLE) | chờ Q-11, Q-58 | BR-06, BR-07 |
| EC-25 | SCHEDULED, now so với thời hạn | ngoài thời hạn | Không hợp lệ (OUTSIDE_BOOKING_WINDOW) | chờ Q-11, Q-58 | UC-010 5b |

F2.7.4. Bảng quyết định (căn cứ gộp: P04 UC-010 luồng 5b chỉ áp dụng khi lớp chưa huỷ):

```text
| Điều kiện / Hành động | R1 | R2 | R3 |
| C1: lớp đã huỷ | Y | N | N |
| C2: now ngoài thời hạn | - | N | Y |
| A1: CLASS_CANCELLED | X | - | - |
| A2: BOOKABLE | - | X | - |
| A3: OUTSIDE_BOOKING_WINDOW | - | - | X |
```
Mã DT4-R1 đến DT4-R3: TC-023; TC-024 (chưa xác định); TC-025 (chưa xác định).

F2.7.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N25 | bắt đầu | bắt đầu |
| N26 | status = CANCELLED? | quyết định |
| N27 | trả CLASS_CANCELLED | khối lệnh |
| N28 | now ngoài thời hạn đặt chỗ tính từ startTime? | quyết định |
| N29 | trả OUTSIDE_BOOKING_WINDOW | khối lệnh |
| N30 | trả BOOKABLE | khối lệnh |
| N31 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE29 | N25 | N26 |  |
| CE30 | N26 | N27 | Đúng |
| CE31 | N26 | N28 | Sai |
| CE32 | N28 | N29 | Đúng |
| CE33 | N28 | N30 | Sai |
| CE34 | N27 | N31 |  |
| CE35 | N29 | N31 |  |
| CE36 | N30 | N31 |  |

V(G) = E - N + 2 = 8 - 7 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3.

Đường đi cơ sở:

- P1: N25 --> N26 --> N27 --> N31 (TC-023)
- P2: N25 --> N26 --> N28 --> N29 --> N31 (TC-025)
- P3: N25 --> N26 --> N28 --> N30 --> N31 (TC-024)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE29 (N25 --> N26) | TC-023 (TC chưa xác định, không tính: TC-024, TC-025) |
| CE30 (N26 --> N27) | TC-023 |
| CE31 (N26 --> N28) | Không có (chỉ có TC chưa xác định: TC-024, TC-025) |
| CE32 (N28 --> N29) | Không có (chỉ có TC chưa xác định: TC-025) |
| CE33 (N28 --> N30) | Không có (chỉ có TC chưa xác định: TC-024) |
| CE34 (N27 --> N31) | TC-023 |
| CE35 (N29 --> N31) | Không có (chỉ có TC chưa xác định: TC-025) |
| CE36 (N30 --> N31) | Không có (chỉ có TC chưa xác định: TC-024) |

Độ phủ đạt được: C0 = 1/3 khối lệnh; C1 = 3/8 nhánh. Nhánh chưa phủ: CE31, CE32, CE33, CE35, CE36. Lý do: quy tắc thời hạn đặt chỗ chờ Q-11, Q-58 nên TC-024, TC-025 chưa có kết quả mong đợi.

Vòng lặp: không có.

### F2.8 DC-GroupClass.collectBookedMembers

F2.8.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | collectBookedMembers(): ReadonlyArray<Member> | P12 F2 |
| Hậu điều kiện | Trả các hội viên có chỗ đã đặt, mỗi hội viên một lần; không đổi dữ liệu | P12 F2 |
| BR | Không có BR trực tiếp; phục vụ BR-14 (thông báo mỗi hội viên đã đặt chỗ) | P06 |
| Luồng thay thế | UC-015 5a (không có hội viên) | P04 |
| Không áp dụng | F2.8.3 chỉ có biên kích thước tập hợp (BV-15, BV-16), F2.8.4 (một điều kiện), F2.8.5 (không phải sự kiện ST), F2.8.7 (không có phụ thuộc ngoài DC-ClassBooking cùng package) | |

F2.8.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-26 | số chỗ đã đặt | 0 | Hợp lệ (trả rỗng) | 0 | UC-015 5a |
| EC-27 | số chỗ đã đặt, mỗi chỗ một hội viên khác nhau | từ 1 trở lên | Hợp lệ | 1 | P12 F2 |
| EC-28 | có hội viên giữ nhiều chỗ | có trùng hội viên | Hợp lệ (loại trùng) | M1, M2, M1 | P12 F2, F3 bước 2; Q-59 |

Không có lớp không hợp lệ: toán tử không có tham số và trạng thái nào cũng cho kết quả (kể cả CANCELLED).

F2.8.3. Giá trị biên (kích thước tập hợp):

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-15 | min của số chỗ | 0 chỗ | EC-26 | danh sách rỗng |
| BV-16 | min+1 của số chỗ | 1 chỗ | EC-27 | đúng 1 hội viên |

F2.8.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N32 | bắt đầu | bắt đầu |
| N33 | result = danh sách rỗng | khối lệnh |
| N34 | còn ClassBooking kế tiếp? | quyết định |
| N35 | m = booking.provideBookedMember() | khối lệnh |
| N36 | id của m đã có trong result? | quyết định |
| N37 | thêm m vào result | khối lệnh |
| N38 | trả result | khối lệnh |
| N39 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE37 | N32 | N33 |  |
| CE38 | N33 | N34 |  |
| CE39 | N34 | N35 | Đúng |
| CE40 | N34 | N38 | Sai |
| CE41 | N35 | N36 |  |
| CE42 | N36 | N34 | Đúng |
| CE43 | N36 | N37 | Sai |
| CE44 | N37 | N34 |  |
| CE45 | N38 | N39 |  |

V(G) = E - N + 2 = 9 - 8 + 2 = 3; kiểm tra bằng số điểm quyết định nhị phân + 1 = 2 + 1 = 3.

Đường đi cơ sở:

- P1: N32 --> N33 --> N34 --> N38 --> N39 (TC-026)
- P2: N32 --> N33 --> N34 --> N35 --> N36 --> N37 --> N34 --> N38 --> N39 (TC-027)
- P3: N32 --> N33 --> N34 --> N35 --> N36 --> N34 --> N38 --> N39 (TC-028)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE37 (N32 --> N33) | TC-026 |
| CE38 (N33 --> N34) | TC-026, TC-027, TC-028 |
| CE39 (N34 --> N35) | TC-027, TC-028 |
| CE40 (N34 --> N38) | TC-026, TC-027, TC-028 |
| CE41 (N35 --> N36) | TC-027, TC-028 |
| CE42 (N36 --> N34) | TC-028 |
| CE43 (N36 --> N37) | TC-027, TC-028 |
| CE44 (N37 --> N34) | TC-027, TC-028 |
| CE45 (N38 --> N39) | TC-026, TC-027, TC-028 |

Độ phủ đạt được: C0 = 4/4 khối lệnh; C1 = 9/9 nhánh.

Vòng lặp:

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Duyệt các ClassBooking | bằng capacity của lớp, cấu hình theo phòng (BR-10, Q-03) nên không cố định; n+1 không xảy ra do bất biến BR-11 | 3 | 0, 1, 3; n-1, n, n+1 không áp dụng vì n không cố định | TC-026, TC-027, TC-028 |

### F2.9 DC-MemberBookingQuota.hasReachedDailyLimit

F2.9.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | hasReachedDailyLimit(memberId: string, classStartTime: Date): Promise<boolean> | P12 F2 |
| Hậu điều kiện | Trả true khi số chỗ đã đặt của hội viên thuộc lớp diễn ra cùng ngày với classStartTime đã đạt MAX_BOOKINGS_PER_DAY (= 2); không đổi dữ liệu | P12 F2, F7 |
| BR | BR-08 (tối đa 2 lớp trong một ngày); cách tính ngày và việc tính lớp chờ chờ Q-60; lớp đã huỷ Q-63 | P06 |
| Luồng thay thế | UC-010 6a | P04 |
| Không áp dụng | F2.9.4 (một điều kiện), F2.9.5 (không phải sự kiện ST) | |

F2.9.2. Phân vùng tương đương (theo đầu ra và khoảng ngày):

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-29 | số chỗ đã đặt trong ngày | 0 đến 1 | Hợp lệ (false) | 1 | BR-08 |
| EC-30 | số chỗ đã đặt trong ngày | từ 2 trở lên | Không hợp lệ (true) | 2 | BR-08 |
| EC-31 | classStartTime | mọi thời điểm trong một ngày lịch: khoảng đếm là [00:00 ngày đó, 00:00 ngày kế) | Hợp lệ | 18:00 ngày 26/10/2026 | P12 F2, F3 bước 1 |
| EC-32 | memberId | rỗng hoặc null | Không hợp lệ | rỗng | Hành vi không nêu: Q-108, không thiết kế TC |

F2.9.3. Giá trị biên:

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-17 | min của số chỗ | 0 | EC-29 | false |
| BV-18 | max của EC-29 | 1 | EC-29 | false |
| BV-19 | min của EC-30 (MAX_BOOKINGS_PER_DAY) | 2 | EC-30 | true |
| BV-20 | đầu ngày của EC-31 | classStartTime 00:00 ngày 26/10/2026 | EC-31 | khoảng đếm 00:00 ngày 26/10 đến 00:00 ngày 27/10 |
| BV-21 | cuối ngày của EC-31 | classStartTime 23:59 ngày 26/10/2026 | EC-31 | khoảng đếm 00:00 ngày 26/10 đến 00:00 ngày 27/10 |

F2.9.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N40 | bắt đầu | bắt đầu |
| N41 | from, toExclusive = đầu ngày chứa classStartTime, cộng 1 ngày; n = await IF-14.countMemberBookingsBetween(...); trả n >= MAX_BOOKINGS_PER_DAY | khối lệnh |
| N42 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE46 | N40 | N41 |  |
| CE47 | N41 | N42 |  |

V(G) = E - N + 2 = 2 - 3 + 2 = 1; kiểm tra bằng số điểm quyết định nhị phân + 1 = 0 + 1 = 1.

Đường đi cơ sở:

- P1: N40 --> N41 --> N42 (TC-029)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE46 (N40 --> N41) | TC-029, TC-030, TC-031, TC-032, TC-033, TC-034 |
| CE47 (N41 --> N42) | TC-029, TC-030, TC-031, TC-032, TC-033, TC-034 |

Độ phủ đạt được: C0 = 1/1 khối lệnh; C1 = 2/2 nhánh.

Phép so sánh n >= MAX_BOOKINGS_PER_DAY là biểu thức, không tạo nhánh điều khiển, nên C1 đạt với một TC bất kỳ; các TC biên BV-17 đến BV-19 vẫn giữ để bắt lỗi toán tử so sánh (Bước 4.5). Vòng lặp: không có.

F2.9.7. Test double:

| Phụ thuộc (DC / IF) | Loại | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| IF-14.countMemberBookingsBetween | stub (TC-029 đến TC-031); mock (TC-032 đến TC-034) | Trả số chỗ định sẵn; xác minh gọi đúng 1 lần với (memberId, đầu ngày, đầu ngày kế) | Truy cập CSDL |

### F2.10 DC-BookClassSpotHandler.bookClass

F2.10.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | bookClass(memberId: string, classId: string): Promise<BookClassResult> | P12 F2 |
| Tiền điều kiện | Hội viên đã xác thực | P12 F2; UC-010 |
| Hậu điều kiện | Thành công (BOOKED): lớp có thêm đúng một chỗ của hội viên, không vượt sức chứa. Thất bại: chỗ đã đặt và danh sách chờ không đổi. Mọi kết cục nghiệp vụ trả trong outcome, không ném ngoại lệ | P12 F2; UC-010 hậu điều kiện |
| Ngoại lệ | DC-GroupClassNotFoundException; MemberNotFoundException | P12 F2, F4b |
| BR | BR-06, BR-07 (chờ Q-11, Q-58), BR-08, BR-09, BR-11, BR-12 | P06 |
| Luồng thay thế | UC-010 4a, 5a, 5b, 6a, 7a1; mục 8 (người đến sau đi theo 7a) | P04 |
| Không áp dụng | F2.10.3 (không có đầu vào có thứ tự; biên số chỗ ghi ở BV-22, BV-23), F2.10.5 (không phải sự kiện ST) | |

F2.10.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-33 | hội viên theo memberId | tồn tại | Hợp lệ | M9 | P12 F2 |
| EC-34 | hội viên theo memberId | không tồn tại | Không hợp lệ | IF-11.findById trả null | P12 F2 |
| EC-35 | quyền đặt lớp | không bị khoá | Hợp lệ | isBookingSuspended = false | BR-09 |
| EC-36 | quyền đặt lớp | đang bị khoá | Không hợp lệ (MEMBER_SUSPENDED) | isBookingSuspended = true | BR-09; UC-010 4a |
| EC-37 | lớp theo classId | tồn tại | Hợp lệ | C1 | P12 F2 |
| EC-38 | lớp theo classId | không tồn tại | Không hợp lệ | findByIdForUpdate trả null | P12 F2 |
| EC-39 | trạng thái lớp | chưa huỷ | Hợp lệ | SCHEDULED | UC-010 bước 5 |
| EC-40 | trạng thái lớp | đã huỷ | Không hợp lệ (CLASS_CANCELLED) | CANCELLED | UC-010 5a |
| EC-41 | thời hạn đặt chỗ | trong thời hạn | Hợp lệ | assessBookability = BOOKABLE (ép) | BR-06, BR-07 |
| EC-42 | thời hạn đặt chỗ | ngoài thời hạn | Không hợp lệ (OUTSIDE_BOOKING_WINDOW) | assessBookability = OUTSIDE_BOOKING_WINDOW (ép) | UC-010 5b |
| EC-43 | số lớp đã đặt trong ngày | chưa đạt mức tối đa | Hợp lệ | hasReachedDailyLimit = false | BR-08 |
| EC-44 | số lớp đã đặt trong ngày | đã đạt mức tối đa | Không hợp lệ (DAILY_LIMIT_REACHED) | hasReachedDailyLimit = true | BR-08; UC-010 6a |
| EC-45 | chỗ trống | còn chỗ | Hợp lệ | 2 trên 3 | BR-11 |
| EC-46 | chỗ trống | đã đủ chỗ | Không hợp lệ (CLASS_FULL) | 3 trên 3 | BR-11; UC-010 7a1 |
| EC-47 | lưu chỗ | reserveSpot thành công | Hợp lệ | còn chỗ | UC-010 bước 8 |
| EC-48 | lưu chỗ | reserveSpot ném SpotUnavailable dù hasAvailableSpot đúng | Không hợp lệ (CLASS_FULL) | hasAvailableSpot ép true, lớp đủ chỗ | UC-010 mục 8 |
| EC-49 | memberId, classId | rỗng hoặc null | Không hợp lệ | rỗng | Hành vi không nêu: Q-108, không thiết kế TC |

F2.10.3. Giá trị biên (số chỗ):

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-22 | max của EC-45 | 2 chỗ đã đặt, capacity 3 | EC-45 | BOOKED, bookedCount = 3 |
| BV-23 | min của EC-46 | 3 chỗ đã đặt, capacity 3 | EC-46 | CLASS_FULL, bookedCount vẫn 3 |

F2.10.4. Bảng quyết định. Điều kiện: C1 hội viên bị khoá, C2 lớp đã huỷ, C3 now ngoài thời hạn, C4 đã đủ số lớp trong ngày, C5 lớp đã đủ chỗ (Y là vi phạm). Căn cứ gộp duy nhất: P04 UC-010 luồng 5b chỉ áp dụng khi lớp chưa huỷ, nên C2 = Y thì C3 không quan tâm khi các điều kiện khác đều N. Thứ tự kiểm tra 4, 5, 6, 7 của P04 mục 8 chỉ là thứ tự trình bày, không phải thứ tự ưu tiên, nên các tổ hợp vi phạm từ hai điều kiện trở lên (không thuộc trường hợp gộp trên) chờ Q-109.

```text
| Điều kiện / Hành động | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 | R26 | R27 | R28 | R29 | R30 | R31 |
| C1: hội viên bị khoá | N | Y | N | N | N | N | N | N | N | N | N | N | N | N | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| C2: lớp đã huỷ | N | N | Y | N | N | N | N | N | N | N | Y | Y | Y | Y | Y | Y | N | N | N | N | N | N | N | Y | Y | Y | Y | Y | Y | Y | Y |
| C3: ngoài thời hạn | N | N | - | Y | N | N | N | Y | Y | Y | N | N | N | Y | Y | Y | N | N | N | Y | Y | Y | Y | N | N | N | N | Y | Y | Y | Y |
| C4: đủ số lớp trong ngày | N | N | N | N | Y | N | Y | N | Y | Y | N | Y | Y | N | Y | Y | N | Y | Y | N | N | Y | Y | N | N | Y | Y | N | N | Y | Y |
| C5: lớp đã đủ chỗ | N | N | N | N | N | Y | Y | Y | N | Y | Y | N | Y | Y | N | Y | Y | N | Y | N | Y | N | Y | N | Y | N | Y | N | Y | N | Y |
| A: BOOKED | X | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A: MEMBER_SUSPENDED | - | X | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A: CLASS_CANCELLED | - | - | X | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A: OUTSIDE_BOOKING_WINDOW | - | - | - | X | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A: DAILY_LIMIT_REACHED | - | - | - | - | X | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A: CLASS_FULL | - | - | - | - | - | X | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| A: Chưa xác định (Q-109) | - | - | - | - | - | - | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
```
Quy tắc có TC: DT5-R1 (BOOKED): TC-035; DT5-R2 (MEMBER_SUSPENDED): TC-036; DT5-R3 (CLASS_CANCELLED, gộp C3): TC-039; DT5-R4 (OUTSIDE_BOOKING_WINDOW): TC-040; DT5-R5 (DAILY_LIMIT_REACHED): TC-041; DT5-R6 (CLASS_FULL): TC-042. Chỉ số cột trong bảng: BOOKED = R1, MEMBER_SUSPENDED = R2, CLASS_CANCELLED = R3, OUTSIDE_BOOKING_WINDOW = R4, DAILY_LIMIT_REACHED = R5, CLASS_FULL = R6.
Các quy tắc R7 đến R31 (vi phạm từ hai điều kiện trở lên) chờ Q-109; chỉ hai quy tắc đại diện có dòng TC chưa xác định (TC-044 cho C1 và C2, TC-045 cho C4 và C5), các quy tắc còn lại sinh TC khi Q-109 có đáp án (xem Vấn đề còn mở).

F2.10.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N43 | bắt đầu | bắt đầu |
| N44 | now = IF-16.now(); mở giao dịch; member = await IF-11.findById(memberId) | khối lệnh |
| N45 | member = null? | quyết định |
| N46 | ném MemberNotFoundException | khối lệnh |
| N47 | member.isBookingSuspended(now)? | quyết định |
| N48 | trả MEMBER_SUSPENDED | khối lệnh |
| N49 | lớp = await IF-14.findByIdForUpdate(classId) | khối lệnh |
| N50 | lớp = null? | quyết định |
| N51 | ném DC-GroupClassNotFoundException | khối lệnh |
| N52 | b = lớp.assessBookability(now) | khối lệnh |
| N53 | b = CLASS_CANCELLED? | quyết định |
| N54 | trả CLASS_CANCELLED | khối lệnh |
| N55 | b = OUTSIDE_BOOKING_WINDOW? | quyết định |
| N56 | trả OUTSIDE_BOOKING_WINDOW | khối lệnh |
| N57 | await quota.hasReachedDailyLimit(memberId, startTime)? | quyết định |
| N58 | trả DAILY_LIMIT_REACHED | khối lệnh |
| N59 | không lớp.hasAvailableSpot()? | quyết định |
| N60 | trả CLASS_FULL | khối lệnh |
| N61 | info = lớp.reserveSpot(member) | khối lệnh |
| N62 | reserveSpot ném DC-SpotUnavailableException? | quyết định |
| N63 | trả CLASS_FULL (bắt ngoại lệ) | khối lệnh |
| N64 | reserveSpot ném DC-InvalidClassStateException? | quyết định |
| N65 | để ngoại lệ lan ra | khối lệnh |
| N66 | await IF-14.save(lớp); trả BOOKED kèm info | khối lệnh |
| N67 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE48 | N43 | N44 |  |
| CE49 | N44 | N45 |  |
| CE50 | N45 | N46 | Đúng |
| CE51 | N45 | N47 | Sai |
| CE52 | N47 | N48 | Đúng |
| CE53 | N47 | N49 | Sai |
| CE54 | N49 | N50 |  |
| CE55 | N50 | N51 | Đúng |
| CE56 | N50 | N52 | Sai |
| CE57 | N52 | N53 |  |
| CE58 | N53 | N54 | Đúng |
| CE59 | N53 | N55 | Sai |
| CE60 | N55 | N56 | Đúng |
| CE61 | N55 | N57 | Sai |
| CE62 | N57 | N58 | Đúng |
| CE63 | N57 | N59 | Sai |
| CE64 | N59 | N60 | Đúng |
| CE65 | N59 | N61 | Sai |
| CE66 | N61 | N62 |  |
| CE67 | N62 | N63 | Đúng |
| CE68 | N62 | N64 | Sai |
| CE69 | N64 | N65 | Đúng |
| CE70 | N64 | N66 | Sai |
| CE71 | N46 | N67 |  |
| CE72 | N48 | N67 |  |
| CE73 | N51 | N67 |  |
| CE74 | N54 | N67 |  |
| CE75 | N56 | N67 |  |
| CE76 | N58 | N67 |  |
| CE77 | N60 | N67 |  |
| CE78 | N63 | N67 |  |
| CE79 | N65 | N67 |  |
| CE80 | N66 | N67 |  |

V(G) = E - N + 2 = 33 - 25 + 2 = 10; kiểm tra bằng số điểm quyết định nhị phân + 1 = 9 + 1 = 10.

Đường đi cơ sở:

- P1: N43 --> N44 --> N45 --> N46 --> N67 (TC-037)
- P2: N43 --> N44 --> N45 --> N47 --> N48 --> N67 (TC-036)
- P3: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N51 --> N67 (TC-038)
- P4: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N52 --> N53 --> N54 --> N67 (TC-039)
- P5: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N52 --> N53 --> N55 --> N56 --> N67 (TC-040)
- P6: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N52 --> N53 --> N55 --> N57 --> N58 --> N67 (TC-041)
- P7: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N52 --> N53 --> N55 --> N57 --> N59 --> N60 --> N67 (TC-042)
- P8: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N52 --> N53 --> N55 --> N57 --> N59 --> N61 --> N62 --> N63 --> N67 (TC-043)
- P9: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N52 --> N53 --> N55 --> N57 --> N59 --> N61 --> N62 --> N64 --> N65 --> N67 (chưa có TC)
- P10: N43 --> N44 --> N45 --> N47 --> N49 --> N50 --> N52 --> N53 --> N55 --> N57 --> N59 --> N61 --> N62 --> N64 --> N66 --> N67 (TC-035)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE48 (N43 --> N44) | TC-035, TC-036, TC-037, TC-038, TC-039, TC-040, TC-041, TC-042, TC-043 |
| CE49 (N44 --> N45) | TC-035, TC-036, TC-037, TC-038, TC-039, TC-040, TC-041, TC-042, TC-043 |
| CE50 (N45 --> N46) | TC-037 |
| CE51 (N45 --> N47) | TC-035, TC-036, TC-038, TC-039, TC-040, TC-041, TC-042, TC-043 |
| CE52 (N47 --> N48) | TC-036 |
| CE53 (N47 --> N49) | TC-035, TC-038, TC-039, TC-040, TC-041, TC-042, TC-043 |
| CE54 (N49 --> N50) | TC-035, TC-038, TC-039, TC-040, TC-041, TC-042, TC-043 |
| CE55 (N50 --> N51) | TC-038 |
| CE56 (N50 --> N52) | TC-035, TC-039, TC-040, TC-041, TC-042, TC-043 |
| CE57 (N52 --> N53) | TC-035, TC-039, TC-040, TC-041, TC-042, TC-043 |
| CE58 (N53 --> N54) | TC-039 |
| CE59 (N53 --> N55) | TC-035, TC-040, TC-041, TC-042, TC-043 |
| CE60 (N55 --> N56) | TC-040 |
| CE61 (N55 --> N57) | TC-035, TC-041, TC-042, TC-043 |
| CE62 (N57 --> N58) | TC-041 |
| CE63 (N57 --> N59) | TC-035, TC-042, TC-043 |
| CE64 (N59 --> N60) | TC-042 |
| CE65 (N59 --> N61) | TC-035, TC-043 |
| CE66 (N61 --> N62) | TC-035, TC-043 |
| CE67 (N62 --> N63) | TC-043 |
| CE68 (N62 --> N64) | TC-035 |
| CE69 (N64 --> N65) | Không có |
| CE70 (N64 --> N66) | TC-035 |
| CE71 (N46 --> N67) | TC-037 |
| CE72 (N48 --> N67) | TC-036 |
| CE73 (N51 --> N67) | TC-038 |
| CE74 (N54 --> N67) | TC-039 |
| CE75 (N56 --> N67) | TC-040 |
| CE76 (N58 --> N67) | TC-041 |
| CE77 (N60 --> N67) | TC-042 |
| CE78 (N63 --> N67) | TC-043 |
| CE79 (N65 --> N67) | Không có |
| CE80 (N66 --> N67) | TC-035 |

Độ phủ đạt được: C0 = 13/14 khối lệnh; C1 = 31/33 nhánh. Nhánh chưa phủ: CE69, CE79. Lý do: nhánh D9 (reserveSpot ném DC-InvalidClassStateException) không thể đi tới theo đặc tả vì lớp CANCELLED đã bị chặn ở D4 và dòng lớp bị khoá suốt giao dịch; chỉ đi tới được bằng cách ép assessBookability trả BOOKABLE cho lớp đã huỷ, trái với thiết kế, nên không thiết kế TC.

V(G) = 10, không vượt ngưỡng 10 (ở ngưỡng, không cần tách). Vòng lặp: không có.

F2.10.7. Test double:

| Phụ thuộc (DC / IF) | Loại | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| IF-16 IClock | stub | now() trả 10:00 ngày 25/10/2026 | Thời gian hệ thống |
| IF-11.findById | stub | Trả DC-Member stub (isBookingSuspended theo ca) hoặc null | Truy cập CSDL; PKG-26 chưa có P12 |
| IF-14.findByIdForUpdate | stub | Trả lớp thật hoặc null | Truy cập CSDL |
| IF-14.save | mock | Xác minh gọi/không gọi, tham số là lớp, số lần | Truy cập CSDL |
| IF-14.runInTransaction | fake | Chạy work rồi trả kết quả | Giao dịch CSDL (hiện thực ở PKG-20) |
| DC-MemberBookingQuota | stub | hasReachedDailyLimit trả true/false; xác minh tham số ở TC-041 | Cô lập khỏi kho dữ liệu; đã test riêng ở F2.9 |
| DC-GroupClass.assessBookability, hasAvailableSpot | spy ép giá trị | Ép BOOKABLE / OUTSIDE_BOOKING_WINDOW (quy tắc thời hạn chờ Q-11, Q-58) và hasAvailableSpot = true (dựng tình huống đua ở TC-043) | Tình huống không dựng được bằng trạng thái thật |

### F2.11 DC-CancelUnderBookedClassHandler.handleMarkDue

F2.11.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | handleMarkDue(kind: MarkKind, subjectRef: string, dueAt: Date): Promise<void> | P12 F2 |
| Tiền điều kiện | SS-06 đã giữ quyền xử lý mốc | P12 F2 |
| Hậu điều kiện | Thành công: lớp CANCELLED; mốc AbsenceCheck và WaitlistTransfer của lớp không còn chờ; mỗi hội viên đã đặt chỗ có yêu cầu gửi thông báo. Luồng 2a, 2b, 5a (không có hội viên được thông báo): không đổi dữ liệu thêm. Xử lý lặp lại được | P12 F2; UC-015 hậu điều kiện |
| Ngoại lệ | Lỗi lan ra cho SS-06 (MarkHandlingFailed, Q-102); Error khi kind khác ClassCutoff; MarkStoreUnavailable từ hai operation huỷ mốc | P12 F2 |
| BR | BR-13, BR-14 | P06 |
| Luồng thay thế | UC-015 2a, 2b, 5a, 6a (Q-65) | P04 |
| Không áp dụng | F2.11.2 và F2.11.3: kind và hội viên đã bao gồm trong EC; không có đầu vào có thứ tự ngoài số chỗ (BV-24 đến BV-26); F2.11.5 (không phải sự kiện ST của lớp này; hiệu ứng T4 được kiểm qua TC-046) | |

F2.11.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-50 | kind | ClassCutoff | Hợp lệ | ClassCutoff | P12 F2 |
| EC-51 | kind | khác ClassCutoff | Không hợp lệ (ném Error) | AbsenceCheck | P12 F2 |
| EC-52 | lớp theo subjectRef | tồn tại | Hợp lệ | C1 | P12 F3 bước 2 |
| EC-53 | lớp theo subjectRef | không tồn tại | Không hợp lệ (kết thúc, ghi nhật ký) | findByIdForUpdate trả null | P12 F3 bước 2 |
| EC-54 | lớp chưa huỷ, số chỗ đã đặt | 1 đến 2 | Hợp lệ (huỷ và thông báo) | 2 | BR-13 |
| EC-55 | lớp chưa huỷ, số chỗ đã đặt | từ 3 trở lên | Không hợp lệ (không huỷ, 2b) | 3 | BR-13; UC-015 2b |
| EC-56 | lớp đã huỷ | CANCELLED (bất kể số chỗ) | Không hợp lệ (kết thúc, 2a) | CANCELLED | UC-015 2a |
| EC-57 | lớp chưa huỷ, số chỗ đã đặt | 0 | Hợp lệ (huỷ, không thông báo, 5a) | 0 | UC-015 5a |
| EC-58 | IF-06.cancelMark | thành công cả hai lần | Hợp lệ | không lỗi | P12 F2 |
| EC-59 | IF-06.cancelMark (AbsenceCheck) | ném MarkStoreUnavailable | Không hợp lệ (lỗi lan ra) | MarkStoreUnavailable | P12 F2 (cancelAbsenceMark) |
| EC-60 | IF-06.cancelMark (WaitlistTransfer) | ném MarkStoreUnavailable | Không hợp lệ (lỗi lan ra) | MarkStoreUnavailable | P12 F2 (cancelWaitlistTransferMark) |
| EC-61 | subjectRef | rỗng hoặc null | Không hợp lệ | rỗng | Hành vi không nêu: Q-108, không thiết kế TC |

F2.11.3. Giá trị biên (số chỗ đã đặt):

| BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
|---|---|---|---|---|
| BV-24 | max của EC-54 | 2 chỗ | EC-54 | lớp bị huỷ, thông báo cho 2 hội viên |
| BV-25 | min của EC-55 | 3 chỗ | EC-55 | lớp không bị huỷ |
| BV-26 | min của EC-57 | 0 chỗ | EC-57 | lớp bị huỷ, không thông báo |

F2.11.4. Bảng quyết định. Căn cứ gộp: P12 F3 xếp kiểm tra kind trước khi nạp dữ liệu, lớp không tồn tại thì các điều kiện sau vô nghĩa (N/A), P04 UC-015 luồng 2b chỉ áp dụng khi lớp chưa huỷ (nên C3 = Y thì C4 không quan tâm), và thứ tự C6 trước C7 theo P12 F3 bước 5; F2 và P04 không mâu thuẫn với các thứ tự này.

```text
| Điều kiện / Hành động | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
| C1: kind khác ClassCutoff | Y | N | N | N | N | N | N | N |
| C2: lớp không tồn tại | - | Y | N | N | N | N | N | N |
| C3: lớp đã huỷ | - | N/A | Y | N | N | N | N | N |
| C4: từ 3 chỗ trở lên | - | N/A | - | Y | N | N | N | N |
| C6: huỷ mốc AbsenceCheck ném lỗi | - | N/A | N/A | N/A | Y | N | N | N |
| C7: huỷ mốc WaitlistTransfer ném lỗi | - | N/A | N/A | N/A | - | Y | N | N |
| C5: không có hội viên đã đặt chỗ | - | N/A | N/A | N/A | - | - | Y | N |
| A1: ném Error | X | - | - | - | - | - | - | - |
| A2: kết thúc, không đổi dữ liệu | - | X | X | X | - | - | - | - |
| A3: lỗi lan ra, không thông báo | - | - | - | - | X | X | - | - |
| A4: huỷ lớp và mốc, không thông báo | - | - | - | - | - | - | X | - |
| A5: huỷ lớp và mốc, thông báo từng hội viên | - | - | - | - | - | - | - | X |
```
Mã DT6-R1 đến DT6-R8: TC-050; TC-051; TC-048, TC-052; TC-047; TC-054; TC-055; TC-049; TC-046. Quy tắc DT6-R3 và DT6-R4 đều là A2 nhưng giữ riêng vì khác ghi chú nguồn (2a, 2b). Ngoài bảng: TC-053 (IF-14.save thất bại) kiểm đường lỗi giao dịch.

F2.11.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N68 | bắt đầu | bắt đầu |
| N69 | kind khác ClassCutoff? | quyết định |
| N70 | ném Error | khối lệnh |
| N71 | mở giao dịch; lớp = findByIdForUpdate(subjectRef) | khối lệnh |
| N72 | lớp = null? | quyết định |
| N73 | ghi nhật ký; kết thúc | khối lệnh |
| N74 | check = lớp.assessCancellation() | khối lệnh |
| N75 | check = ALREADY_CANCELLED hoặc ENOUGH_BOOKINGS? | quyết định |
| N76 | kết thúc, không lưu (2a, 2b) | khối lệnh |
| N77 | lớp.cancelClass(); IF-14.save(lớp) | khối lệnh |
| N78 | cancelAbsenceMark(subjectRef) ném MarkStoreUnavailable? | quyết định |
| N79 | lỗi lan ra (hoàn tác giao dịch) | khối lệnh |
| N80 | cancelWaitlistTransferMark(subjectRef) ném MarkStoreUnavailable? | quyết định |
| N81 | lỗi lan ra (hoàn tác giao dịch) | khối lệnh |
| N82 | members = collectBookedMembers(); info = provideClassInfo(); commit | khối lệnh |
| N83 | members rỗng? | quyết định |
| N84 | kết thúc (5a) | khối lệnh |
| N85 | notifyBookedMembers(members, info) | khối lệnh |
| N86 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE81 | N68 | N69 |  |
| CE82 | N69 | N70 | Đúng |
| CE83 | N69 | N71 | Sai |
| CE84 | N71 | N72 |  |
| CE85 | N72 | N73 | Đúng |
| CE86 | N72 | N74 | Sai |
| CE87 | N74 | N75 |  |
| CE88 | N75 | N76 | Đúng |
| CE89 | N75 | N77 | Sai |
| CE90 | N77 | N78 |  |
| CE91 | N78 | N79 | Đúng |
| CE92 | N78 | N80 | Sai |
| CE93 | N80 | N81 | Đúng |
| CE94 | N80 | N82 | Sai |
| CE95 | N82 | N83 |  |
| CE96 | N83 | N84 | Đúng |
| CE97 | N83 | N85 | Sai |
| CE98 | N70 | N86 |  |
| CE99 | N73 | N86 |  |
| CE100 | N76 | N86 |  |
| CE101 | N79 | N86 |  |
| CE102 | N81 | N86 |  |
| CE103 | N84 | N86 |  |
| CE104 | N85 | N86 |  |

V(G) = E - N + 2 = 24 - 19 + 2 = 7; kiểm tra bằng số điểm quyết định nhị phân + 1 = 6 + 1 = 7.

Đường đi cơ sở:

- P1: N68 --> N69 --> N70 --> N86 (TC-050)
- P2: N68 --> N69 --> N71 --> N72 --> N73 --> N86 (TC-051)
- P3: N68 --> N69 --> N71 --> N72 --> N74 --> N75 --> N76 --> N86 (TC-047, TC-048)
- P4: N68 --> N69 --> N71 --> N72 --> N74 --> N75 --> N77 --> N78 --> N79 --> N86 (TC-054)
- P5: N68 --> N69 --> N71 --> N72 --> N74 --> N75 --> N77 --> N78 --> N80 --> N81 --> N86 (TC-055)
- P6: N68 --> N69 --> N71 --> N72 --> N74 --> N75 --> N77 --> N78 --> N80 --> N82 --> N83 --> N84 --> N86 (TC-049)
- P7: N68 --> N69 --> N71 --> N72 --> N74 --> N75 --> N77 --> N78 --> N80 --> N82 --> N83 --> N85 --> N86 (TC-046)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE81 (N68 --> N69) | TC-046, TC-047, TC-048, TC-049, TC-050, TC-051, TC-052, TC-053, TC-054, TC-055 |
| CE82 (N69 --> N70) | TC-050 |
| CE83 (N69 --> N71) | TC-046, TC-047, TC-048, TC-049, TC-051, TC-052, TC-053, TC-054, TC-055 |
| CE84 (N71 --> N72) | TC-046, TC-047, TC-048, TC-049, TC-051, TC-052, TC-053, TC-054, TC-055 |
| CE85 (N72 --> N73) | TC-051 |
| CE86 (N72 --> N74) | TC-046, TC-047, TC-048, TC-049, TC-052, TC-053, TC-054, TC-055 |
| CE87 (N74 --> N75) | TC-046, TC-047, TC-048, TC-049, TC-052, TC-053, TC-054, TC-055 |
| CE88 (N75 --> N76) | TC-047, TC-048, TC-052 |
| CE89 (N75 --> N77) | TC-046, TC-049, TC-052, TC-053, TC-054, TC-055 |
| CE90 (N77 --> N78) | TC-046, TC-049, TC-052, TC-053, TC-054, TC-055 |
| CE91 (N78 --> N79) | TC-054 |
| CE92 (N78 --> N80) | TC-046, TC-049, TC-052, TC-055 |
| CE93 (N80 --> N81) | TC-055 |
| CE94 (N80 --> N82) | TC-046, TC-049, TC-052 |
| CE95 (N82 --> N83) | TC-046, TC-049, TC-052 |
| CE96 (N83 --> N84) | TC-049 |
| CE97 (N83 --> N85) | TC-046, TC-052 |
| CE98 (N70 --> N86) | TC-050 |
| CE99 (N73 --> N86) | TC-051 |
| CE100 (N76 --> N86) | TC-047, TC-048, TC-052 |
| CE101 (N79 --> N86) | TC-054 |
| CE102 (N81 --> N86) | TC-055 |
| CE103 (N84 --> N86) | TC-049 |
| CE104 (N85 --> N86) | TC-046, TC-052 |

Độ phủ đạt được: C0 = 11/11 khối lệnh; C1 = 24/24 nhánh.

Điều kiện ghép D3 (ALREADY_CANCELLED hoặc ENOUGH_BOOKINGS) hiện thực BR-13: mỗi điều kiện con nhận cả đúng và sai nhờ TC-048 (lớp đã huỷ) và TC-047 (3 chỗ). Vòng lặp: không có (vòng gửi thông báo nằm ở notifyBookedMembers).

F2.11.7. Test double:

| Phụ thuộc (DC / IF) | Loại | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| IF-14.findByIdForUpdate | stub | Trả lớp thật hoặc null | Truy cập CSDL |
| IF-14.save | mock | Xác minh gọi với lớp; ghi sự kiện để kiểm thứ tự; TC-053 cho từ chối | Truy cập CSDL |
| IF-14.runInTransaction | fake | Chạy work, ghi sự kiện commit sau khi work xong, work lỗi thì lỗi lan ra | Giao dịch CSDL (PKG-20) |
| IF-06.cancelMark | mock | Xác minh (loại mốc, mã lớp); TC-054, TC-055 cho từ chối MarkStoreUnavailable | Hệ thống hẹn giờ (SS-06) |
| IF-03.sendPushNotification, IF-04.sendSms | mock | Xác minh người nhận, số lần và gọi sau commit | Hệ thống ngoài |
| IF-16 IClock | stub | now() trả giá trị cố định (handleMarkDue chỉ ghi dueAt nhật ký) | Thời gian hệ thống |
| DC-Member (PKG-26) | stub | getId, determineNotificationChannel, getPhoneNumber | Lớp chưa có P12 |

### F2.12 DC-CancelUnderBookedClassHandler.notifyBookedMembers

F2.12.1. Cơ sở kiểm thử:

| Mục | Nội dung | Nguồn |
|---|---|---|
| Chữ ký | notifyBookedMembers(members: ReadonlyArray<Member>, info: ClassInfo): Promise<void> (private) | P12 F2 |
| Tiền điều kiện | Lớp đã CANCELLED và giao dịch đã commit | P12 F2 |
| Hậu điều kiện | Mỗi hội viên có yêu cầu gửi trong hàng chờ gửi nền của SS-03 hoặc SS-04, trừ hội viên bị từ chối đầu vào | P12 F2 |
| Ngoại lệ | Không nêu ngoại lệ ra ngoài; InvalidNotificationContent, InvalidPhoneNumber được bắt, ghi nhật ký, bỏ qua (kết cục chờ Q-65) | P12 F2, F3 |
| BR | BR-14 (thông báo đẩy; chưa cài ứng dụng thì SMS) | P06 |
| Luồng thay thế | UC-015 6a (Q-65), 5a | P04 |
| Không áp dụng | F2.12.3 (không có đầu vào có thứ tự; kích thước danh sách ghi ở vòng lặp), F2.12.5 (không phải sự kiện ST) | |

F2.12.2. Phân vùng tương đương:

| EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
|---|---|---|---|---|---|
| EC-62 | members | rỗng | Hợp lệ (không gửi) | danh sách rỗng | UC-015 5a |
| EC-63 | kênh của hội viên | thông báo đẩy | Hợp lệ | M1 | BR-14 |
| EC-64 | kênh của hội viên | SMS | Hợp lệ | M2, số 0900000002 | BR-14 |
| EC-65 | kết quả IF-03 | từ chối InvalidNotificationContent | Không hợp lệ (bỏ qua hội viên) | M1 | P12 F2, F3 bước 5 |
| EC-66 | kết quả IF-04 | từ chối InvalidPhoneNumber | Không hợp lệ (bỏ qua hội viên) | M1 số invalid | P12 F2, F3 bước 5 |
| EC-67 | kết quả cổng | lỗi khác (cổng không gửi được) | Không hợp lệ (kết cục chờ Q-65) | lỗi cổng | UC-015 6a; Q-65 |

F2.12.4. Bảng quyết định (cho từng hội viên; không gộp vì F2 liệt kê rõ từng cặp):

```text
| Điều kiện / Hành động | R1 | R2 | R3 | R4 |
| C1: kênh là thông báo đẩy | Y | Y | N | N |
| C2: cổng từ chối đầu vào | N | Y | N | Y |
| A1: gửi qua IF-03 | X | X | - | - |
| A2: gửi qua IF-04 | - | - | X | X |
| A3: ghi nhật ký, bỏ qua hội viên | - | X | - | X |
```
Mã DT7-R1 đến DT7-R4 lần lượt do TC-057, TC-058, TC-057, TC-059 phủ. Lỗi khác của cổng (EC-67) ngoài bảng: TC-060 chờ Q-65.

F2.12.6. Hộp trắng (thiết kế method P12 F3):

Bảng node:

| N | Nội dung (lệnh hoặc điều kiện) | Loại |
|---|---|---|
| N87 | bắt đầu | bắt đầu |
| N88 | content = composeClassCancelledNotice(info) | khối lệnh |
| N89 | còn hội viên kế tiếp? | quyết định |
| N90 | channel = member.determineNotificationChannel() | khối lệnh |
| N91 | channel = thông báo đẩy? | quyết định |
| N92 | IF-03.sendPushNotification(member, content) | khối lệnh |
| N93 | IF-04.sendSms(member.getPhoneNumber(), content) | khối lệnh |
| N94 | cổng ném InvalidNotificationContent hoặc InvalidPhoneNumber? | quyết định |
| N95 | ghi nhật ký mã hội viên | khối lệnh |
| N96 | kết thúc | kết thúc |

Bảng cạnh:

| CE | Từ N | Tới N | Nhãn |
|---|---|---|---|
| CE105 | N87 | N88 |  |
| CE106 | N88 | N89 |  |
| CE107 | N89 | N90 | Đúng |
| CE108 | N89 | N96 | Sai |
| CE109 | N90 | N91 |  |
| CE110 | N91 | N92 | Đúng |
| CE111 | N91 | N93 | Sai |
| CE112 | N92 | N94 |  |
| CE113 | N93 | N94 |  |
| CE114 | N94 | N95 | Đúng |
| CE115 | N94 | N89 | Sai |
| CE116 | N95 | N89 |  |

V(G) = E - N + 2 = 12 - 10 + 2 = 4; kiểm tra bằng số điểm quyết định nhị phân + 1 = 3 + 1 = 4.

Đường đi cơ sở:

- P1: N87 --> N88 --> N89 --> N96 (TC-056)
- P2: N87 --> N88 --> N89 --> N90 --> N91 --> N92 --> N94 --> N89 --> N96 (TC-057)
- P3: N87 --> N88 --> N89 --> N90 --> N91 --> N93 --> N94 --> N89 --> N96 (TC-057)
- P4: N87 --> N88 --> N89 --> N90 --> N91 --> N92 --> N94 --> N95 --> N89 --> N96 (TC-058)

Bảng phủ nhánh:

| Nhánh (CE) | TC phủ |
|---|---|
| CE105 (N87 --> N88) | TC-056, TC-057, TC-058, TC-059 |
| CE106 (N88 --> N89) | TC-056, TC-057, TC-058, TC-059 |
| CE107 (N89 --> N90) | TC-057, TC-058, TC-059 |
| CE108 (N89 --> N96) | TC-056, TC-057, TC-058, TC-059 |
| CE109 (N90 --> N91) | TC-057, TC-058, TC-059 |
| CE110 (N91 --> N92) | TC-057, TC-058 |
| CE111 (N91 --> N93) | TC-057, TC-059 |
| CE112 (N92 --> N94) | TC-057, TC-058 |
| CE113 (N93 --> N94) | TC-057, TC-059 |
| CE114 (N94 --> N95) | TC-058, TC-059 |
| CE115 (N94 --> N89) | TC-057 |
| CE116 (N95 --> N89) | TC-058, TC-059 |

Độ phủ đạt được: C0 = 5/5 khối lệnh; C1 = 12/12 nhánh.

Nhánh lỗi khác của cổng (không phải Invalid*) không có ở P12 F2 nên không tạo nhánh theo Bước 4.1; kết cục chờ Q-65 (TC-060).

Vòng lặp:

| Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
|---|---|---|---|---|
| Duyệt danh sách hội viên | không xác định (số hội viên đặt chỗ tối đa bằng capacity của lớp, chưa cố định, Q-03) | 2 | 0, 2; 1 và n-1, n, n+1 không kiểm (xem Vấn đề còn mở) | TC-056, TC-057, TC-058, TC-059 |

F2.12.7. Test double:

| Phụ thuộc (DC / IF) | Loại | Hành vi giả lập hoặc điều cần xác minh | Lý do |
|---|---|---|---|
| IF-03.sendPushNotification | mock | Xác minh người nhận, nội dung; từ chối InvalidNotificationContent ở TC-058 | Hệ thống ngoài |
| IF-04.sendSms | mock | Xác minh số điện thoại, nội dung; từ chối InvalidPhoneNumber ở TC-059 | Hệ thống ngoài |
| DC-Member (PKG-26) | stub | determineNotificationChannel (PUSH hoặc SMS), getPhoneNumber | Lớp chưa có P12 |
| DC-NotificationContent (PKG-24) | dùng thật qua composeClassCancelledNotice | Kiểm body không rỗng | Kiểu giá trị đơn giản |

Operation private: test truy cập qua cú pháp dấu ngoặc vuông của TypeScript (handler['notifyBookedMembers']) để không đổi visibility theo P12.

## F3. Bảng test case

| TC | DC.operation | Kỹ thuật | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn (BR / UC bước) | Phủ | Test double | Ưu tiên |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | DC-GroupClass.GroupClass | phân vùng tương đương | Chưa có đối tượng lớp | id C1, classType Yoga, room Phòng 2, trainer Nguyễn Thị Lan, startTime 18:00 26/10/2026, capacity 40 | Không ngoại lệ; getStatus() = SCHEDULED; getBookedCount() = 0; provideClassInfo() trả classId C1, classType Yoga, room Phòng 2, trainer Nguyễn Thị Lan, startTime 18:00 26/10/2026 | P12 F2 hậu điều kiện; ST-01 T1; BR-10 | EC-01, T1 | Không | Cao |
| TC-002 | DC-GroupClass.GroupClass | giá trị biên | Chưa có đối tượng lớp | như TC-001 nhưng capacity = 0 | Không ngoại lệ; getStatus() = SCHEDULED; getBookedCount() = 0 | P12 F2 tiền điều kiện capacity >= 0; BR-10 | BV-01, EC-01, T1 | Không | Cao |
| TC-003 | DC-GroupClass.reserveSpot | bảng quyết định | lớp C1 (loại Yoga, phòng Phòng 2, huấn luyện viên Nguyễn Thị Lan, giờ học 18:00 ngày 26/10/2026), capacity 3, status SCHEDULED, chưa có chỗ đã đặt | member = hội viên M1 | Không ngoại lệ; trả DC-ClassInfo bằng provideClassInfo() của lớp; getBookedCount() = 1; collectBookedMembers() chứa đúng M1 | BR-11; UC-010 bước 8; P12 F2 hậu điều kiện | DT1-R1, EC-04, EC-06, BV-03, T2 | Không | Cao |
| TC-004 | DC-GroupClass.reserveSpot | giá trị biên | capacity 3, status SCHEDULED, đã có chỗ của M1, M2 (còn đúng 1 chỗ) | member = M3 | Không ngoại lệ; getBookedCount() = 3 | BR-11; UC-010 bước 7, 8 | BV-04, EC-06, DT1-R1 | Không | Cao |
| TC-005 | DC-GroupClass.reserveSpot | giá trị biên | capacity 3, status SCHEDULED, đã có chỗ của M1, M2, M3 (đủ chỗ) | member = M4 | Ném DC-SpotUnavailableException; getBookedCount() = 3; collectBookedMembers() không chứa M4 | BR-11; UC-010 bước 7a; P12 F2 ngoại lệ | BV-05, EC-07, DT1-R2, từ chối ST-01 | Không | Cao |
| TC-006 | DC-GroupClass.reserveSpot | chuyển trạng thái | capacity 3, đã có chỗ của M1, lớp đã cancelClass() (status CANCELLED) | member = M2 | Ném DC-InvalidClassStateException; getStatus() = CANCELLED; getBookedCount() = 1 | P12 F2 ngoại lệ; ST-01 từ chối; UC-010 5a | EC-05, DT1-R3, từ chối ST-01 | Không | Cao |
| TC-007 | DC-GroupClass.reserveSpot | bảng quyết định | capacity 3, đã có chỗ của M1, M2, M3, lớp đã huỷ | member = M4 | Chưa xác định: chờ Q-109 | P12 F2 ngoại lệ | DT1-R4 | Không | Trung bình |
| TC-008 | DC-GroupClass.hasAvailableSpot | giá trị biên | capacity 3, đã có chỗ của M1, M2 | Không có tham số | Trả true; getBookedCount() = 2 | BR-10, BR-11; UC-010 bước 7 | BV-06, EC-09 | Không | Cao |
| TC-009 | DC-GroupClass.hasAvailableSpot | giá trị biên | capacity 3, đã có chỗ của M1, M2, M3 | Không có tham số | Trả false; getBookedCount() = 3 | BR-11; UC-010 bước 7a | BV-07, EC-10 | Không | Cao |
| TC-010 | DC-GroupClass.hasAvailableSpot | giá trị biên | capacity 0, chưa có chỗ đã đặt | Không có tham số | Trả false; getBookedCount() = 0 | BR-10, BR-11 | BV-08, EC-10 | Không | Trung bình |
| TC-011 | DC-GroupClass.addToWaitlist | bảng quyết định | capacity 2, đã có chỗ của M1, M2 (đủ chỗ), status SCHEDULED, chưa có ai trong danh sách chờ | member = M3, now = 10:00 ngày 25/10/2026 | Trả 1; isOnWaitlist(M3) = true (operation đề xuất, xem Đề xuất sửa artifact trước); getBookedCount() = 2 | BR-12; UC-010 bước 7a3, 7a4 (vị trí 1 là đứng đầu) | DT2-R1, EC-11, EC-13, EC-15, BV-10, BV-11, T3 | Không | Cao |
| TC-012 | DC-GroupClass.addToWaitlist | phân vùng tương đương | capacity 2, đủ chỗ (M1, M2), M3 đã trong danh sách chờ | member = M4, now = 10:00 ngày 25/10/2026 | Trả số nguyên dương từ 1 đến 2 (giá trị chính xác chờ Q-61); isOnWaitlist(M3) = true và isOnWaitlist(M4) = true | BR-12; UC-010 Dữ liệu ra 3 (số nguyên dương); Q-61 | EC-16 | Không | Cao |
| TC-013 | DC-GroupClass.addToWaitlist | chuyển trạng thái | capacity 2, đã có chỗ của M1 (còn 1 chỗ), status SCHEDULED | member = M3, now = 10:00 ngày 25/10/2026 | Ném DC-WaitlistNotAllowedException (kết cục nghiệp vụ có thể đổi theo Q-106); isOnWaitlist(M3) = false; getBookedCount() = 1 | P12 F2 ngoại lệ; ST-01 từ chối; Q-106 | DT2-R2, EC-14, BV-09, từ chối ST-01 | Không | Cao |
| TC-014 | DC-GroupClass.addToWaitlist | chuyển trạng thái | capacity 2, đã có chỗ của M1, M2, lớp đã huỷ | member = M3, now = 10:00 ngày 25/10/2026 | Ném DC-InvalidClassStateException; isOnWaitlist(M3) = false; getStatus() = CANCELLED | P12 F2 ngoại lệ; ST-01 từ chối | DT2-R3, EC-12, từ chối ST-01 | Không | Cao |
| TC-015 | DC-GroupClass.addToWaitlist | bảng quyết định | capacity 2, đã có chỗ của M1, lớp đã huỷ | member = M3, now = 10:00 ngày 25/10/2026 | Chưa xác định: chờ Q-109 | P12 F2 ngoại lệ | DT2-R4 | Không | Trung bình |
| TC-016 | DC-GroupClass.cancelClass | chuyển trạng thái | capacity 3, status SCHEDULED, chưa có chỗ đã đặt | Không có tham số | Không ngoại lệ; getStatus() = CANCELLED; getBookedCount() = 0 | BR-13; UC-015 bước 3; ST-01 T4 | EC-18, T4 | Không | Cao |
| TC-017 | DC-GroupClass.cancelClass | chuyển trạng thái | capacity 2, đã có chỗ của M1, M2, M3 trong danh sách chờ, status SCHEDULED | Không có tham số | Không ngoại lệ; getStatus() = CANCELLED; getBookedCount() = 2; collectBookedMembers() = M1, M2; isOnWaitlist(M3) = true | P12 F2 hậu điều kiện (chỗ đã đặt và danh sách chờ không đổi); Q-63 | T4 | Không | Trung bình |
| TC-018 | DC-GroupClass.cancelClass | chuyển trạng thái | capacity 3, lớp đã huỷ | Không có tham số | Ném DC-InvalidClassStateException; getStatus() = CANCELLED | P12 F2 ngoại lệ; ST-01 từ chối; UC-015 luồng 2a | EC-19, từ chối ST-01 | Không | Cao |
| TC-019 | DC-GroupClass.assessCancellation | giá trị biên | capacity 5, status SCHEDULED, chưa có chỗ đã đặt | Không có tham số | Trả CANCELLABLE; getStatus() = SCHEDULED | BR-13; UC-015 bước 2, 3 | BV-12, EC-21, DT3-R1 | Không | Cao |
| TC-020 | DC-GroupClass.assessCancellation | giá trị biên | capacity 5, status SCHEDULED, chỗ đã đặt của M1, M2 | Không có tham số | Trả CANCELLABLE; getStatus() = SCHEDULED | BR-13 (dưới 3 người); UC-015 ví dụ 0, 1, 2 người | BV-13, EC-21, DT3-R1 | Không | Cao |
| TC-021 | DC-GroupClass.assessCancellation | giá trị biên | capacity 5, status SCHEDULED, chỗ đã đặt của M1, M2, M3 | Không có tham số | Trả ENOUGH_BOOKINGS; getStatus() = SCHEDULED | BR-13; UC-015 luồng 2b | BV-14, EC-22, DT3-R2 | Không | Cao |
| TC-022 | DC-GroupClass.assessCancellation | bảng quyết định | capacity 5, chỗ đã đặt của M1, M2, M3, lớp đã huỷ | Không có tham số | Trả ALREADY_CANCELLED; getStatus() = CANCELLED; getBookedCount() = 3 | UC-015 luồng 2a và 2b (2b chỉ áp dụng khi lớp chưa huỷ) | EC-20, DT3-R3 | Không | Cao |
| TC-023 | DC-GroupClass.assessBookability | phân vùng tương đương | capacity 5, lớp đã huỷ, giờ học 18:00 ngày 26/10/2026 | now = 10:00 ngày 25/10/2026 | Trả CLASS_CANCELLED | UC-010 luồng 5a; P12 F2 | EC-23, DT4-R1 | Không | Cao |
| TC-024 | DC-GroupClass.assessBookability | phân vùng tương đương | capacity 5, status SCHEDULED, giờ học 18:00 ngày 26/10/2026 | now trong thời hạn đặt chỗ (giá trị cụ thể chờ Q-11, Q-58) | Chưa xác định: chờ Q-11, Q-58 | BR-06, BR-07; UC-010 bước 5 | EC-24, DT4-R2 | Không | Cao |
| TC-025 | DC-GroupClass.assessBookability | giá trị biên | capacity 5, status SCHEDULED, giờ học 18:00 ngày 26/10/2026 | now ngoài thời hạn đặt chỗ (biên cụ thể chờ Q-11, Q-58) | Chưa xác định: chờ Q-11, Q-58 | BR-06, BR-07; UC-010 luồng 5b | EC-25, DT4-R3 | Không | Cao |
| TC-026 | DC-GroupClass.collectBookedMembers | giá trị biên | capacity 5, chưa có chỗ đã đặt | Không có tham số | Trả danh sách rỗng | UC-015 luồng 5a; P12 F2 | BV-15, EC-26 | Không | Cao |
| TC-027 | DC-GroupClass.collectBookedMembers | giá trị biên | capacity 5, chỗ đã đặt của M1 | Không có tham số | Trả đúng một hội viên M1 | UC-015 bước 5; P12 F2 | BV-16, EC-27 | Không | Cao |
| TC-028 | DC-GroupClass.collectBookedMembers | phân vùng tương đương | capacity 5, ba chỗ đã đặt: M1, M2, M1 (M1 giữ hai chỗ, đặt trùng chờ Q-59) | Không có tham số | Trả hai hội viên M1 và M2 (mỗi hội viên một lần, không xét thứ tự); getBookedCount() = 3 | P12 F2 (mỗi hội viên một lần); UC-015 bước 5, 6; Q-59 | EC-28 | Không | Cao |
| TC-029 | DC-MemberBookingQuota.hasReachedDailyLimit | giá trị biên | IF-14.countMemberBookingsBetween trả 0 | memberId M1, classStartTime 18:00 ngày 26/10/2026 | Trả false | BR-08 (tối đa 2 lớp); UC-010 bước 6 | BV-17, EC-29 | stub IF-14 | Cao |
| TC-030 | DC-MemberBookingQuota.hasReachedDailyLimit | giá trị biên | IF-14.countMemberBookingsBetween trả 1 | memberId M1, classStartTime 18:00 ngày 26/10/2026 | Trả false | BR-08; UC-010 bước 6 | BV-18, EC-29 | stub IF-14 | Cao |
| TC-031 | DC-MemberBookingQuota.hasReachedDailyLimit | giá trị biên | IF-14.countMemberBookingsBetween trả 2 | memberId M1, classStartTime 18:00 ngày 26/10/2026 | Trả true | BR-08; UC-010 luồng 6a | BV-19, EC-30 | stub IF-14 | Cao |
| TC-032 | DC-MemberBookingQuota.hasReachedDailyLimit | phân vùng tương đương | IF-14.countMemberBookingsBetween trả 0 | memberId M1, classStartTime 18:00 ngày 26/10/2026 | Gọi IF-14.countMemberBookingsBetween đúng 1 lần với (M1, 00:00 ngày 26/10/2026, 00:00 ngày 27/10/2026) | P12 F2 (cùng ngày với classStartTime); Q-60 | EC-31 | mock IF-14 | Cao |
| TC-033 | DC-MemberBookingQuota.hasReachedDailyLimit | giá trị biên | IF-14.countMemberBookingsBetween trả 0 | memberId M1, classStartTime 00:00 ngày 26/10/2026 | Gọi IF-14.countMemberBookingsBetween đúng 1 lần với (M1, 00:00 ngày 26/10/2026, 00:00 ngày 27/10/2026) | P12 F2 (cùng ngày với classStartTime); Q-60 | BV-20, EC-31 | mock IF-14 | Cao |
| TC-034 | DC-MemberBookingQuota.hasReachedDailyLimit | giá trị biên | IF-14.countMemberBookingsBetween trả 0 | memberId M1, classStartTime 23:59 ngày 26/10/2026 | Gọi IF-14.countMemberBookingsBetween đúng 1 lần với (M1, 00:00 ngày 26/10/2026, 00:00 ngày 27/10/2026) | P12 F2 (cùng ngày với classStartTime); Q-60 | BV-21, EC-31 | mock IF-14 | Cao |
| TC-035 | DC-BookClassSpotHandler.bookClass | use case | IF-11.findById trả hội viên M9 không bị khoá; lớp C1 capacity 3 đã có chỗ của M1, M2 (còn 1 chỗ), assessBookability được ép trả BOOKABLE; DC-MemberBookingQuota trả false | memberId M9, classId C1 | Trả DC-BookClassResult có outcome BOOKED và classInfo bằng provideClassInfo() của lớp; getBookedCount() = 3; IF-14.save gọi đúng 1 lần với lớp C1; IF-14.runInTransaction gọi đúng 1 lần | UC-010 bước 3 đến 9; BR-11; P12 F3 | DT5-R1, BV-22, EC-33, EC-35, EC-37, EC-39, EC-41, EC-43, EC-45, EC-47, CE (luồng chính) | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub | Cao |
| TC-036 | DC-BookClassSpotHandler.bookClass | use case | IF-11.findById trả hội viên M9 có isBookingSuspended = true; lớp C1 capacity 3 đã có chỗ của M1 | memberId M9, classId C1 | Trả outcome MEMBER_SUSPENDED, classInfo = null; IF-14.save không được gọi; getBookedCount() = 1 | BR-09; UC-010 luồng 4a | DT5-R2, EC-36 | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub | Cao |
| TC-037 | DC-BookClassSpotHandler.bookClass | use case | IF-11.findById trả null | memberId M9, classId C1 | Ném MemberNotFoundException; IF-14.save không được gọi | P12 F2 ngoại lệ; UC-010 tiền điều kiện | EC-34 | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub | Trung bình |
| TC-038 | DC-BookClassSpotHandler.bookClass | use case | IF-11.findById trả hội viên M9; IF-14.findByIdForUpdate trả null | memberId M9, classId C404 | Ném DC-GroupClassNotFoundException; IF-14.save không được gọi | P12 F2 ngoại lệ | EC-38 | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub | Trung bình |
| TC-039 | DC-BookClassSpotHandler.bookClass | use case | Hội viên M9 không bị khoá; lớp C1 capacity 3 đã có chỗ của M1, lớp đã huỷ | memberId M9, classId C1 | Trả outcome CLASS_CANCELLED, classInfo = null; IF-14.save không được gọi; getBookedCount() = 1 | UC-010 luồng 5a | DT5-R3, EC-40 | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub | Cao |
| TC-040 | DC-BookClassSpotHandler.bookClass | use case | Hội viên M9 không bị khoá; lớp C1 capacity 3 đã có chỗ của M1, assessBookability được ép trả OUTSIDE_BOOKING_WINDOW | memberId M9, classId C1 | Trả outcome OUTSIDE_BOOKING_WINDOW, classInfo = null; IF-14.save không được gọi; getBookedCount() = 1 | BR-06, BR-07; UC-010 luồng 5b (ánh xạ kết quả; quy tắc thời hạn chờ Q-11, Q-58) | DT5-R4, EC-42 | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub; spy assessBookability | Cao |
| TC-041 | DC-BookClassSpotHandler.bookClass | use case | Hội viên M9 không bị khoá; lớp C1 capacity 3 đã có chỗ của M1, assessBookability được ép trả BOOKABLE; DC-MemberBookingQuota.hasReachedDailyLimit trả true | memberId M9, classId C1 | Trả outcome DAILY_LIMIT_REACHED, classInfo = null; hasReachedDailyLimit được gọi với (M9, 18:00 ngày 26/10/2026); IF-14.save không được gọi; getBookedCount() = 1 | BR-08; UC-010 luồng 6a | DT5-R5, EC-44 | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub; spy assessBookability | Cao |
| TC-042 | DC-BookClassSpotHandler.bookClass | use case | Hội viên M9 không bị khoá; lớp C1 capacity 3 đã có chỗ của M1, M2, M3 (đủ chỗ), assessBookability được ép trả BOOKABLE; DC-MemberBookingQuota trả false | memberId M9, classId C1 | Trả outcome CLASS_FULL, classInfo = null; IF-14.save không được gọi; getBookedCount() = 3 | BR-11, BR-12; UC-010 luồng 7a1 | DT5-R6, EC-46, BV-23 | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub; spy assessBookability | Cao |
| TC-043 | DC-BookClassSpotHandler.bookClass | use case | Như TC-042 nhưng hasAvailableSpot được ép trả true (chỗ cuối bị lấy giữa lúc kiểm tra và lúc lưu) | memberId M9, classId C1 | reserveSpot ném SpotUnavailableException; trả outcome CLASS_FULL; IF-14.save không được gọi; getBookedCount() = 3 | BR-11; UC-010 mục 8 (người đến sau đi theo luồng 7a) | EC-48, CE (nhánh bắt SpotUnavailable) | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub; spy assessBookability, hasAvailableSpot | Cao |
| TC-044 | DC-BookClassSpotHandler.bookClass | bảng quyết định | Hội viên M9 bị khoá quyền đặt lớp và lớp C1 đã huỷ | memberId M9, classId C1 | Chưa xác định: chờ Q-109 | UC-010 mục 8 (không nêu thứ tự ưu tiên) | DT5 (đại diện R7 đến R31) | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub | Trung bình |
| TC-045 | DC-BookClassSpotHandler.bookClass | bảng quyết định | Hội viên M9 đã đủ số lớp trong ngày và lớp C1 đã đủ chỗ | memberId M9, classId C1 | Chưa xác định: chờ Q-109 | UC-010 mục 8 (không nêu thứ tự ưu tiên) | DT5 (đại diện R7 đến R31) | IF-16 stub (now = 10:00 ngày 25/10/2026), IF-11 stub, IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake chạy work), DC-MemberBookingQuota stub | Trung bình |
| TC-046 | DC-CancelUnderBookedClassHandler.handleMarkDue | use case | Lớp C1 capacity 5, status SCHEDULED, chỗ đã đặt của M1 (kênh thông báo đẩy) và M2 (kênh SMS, số 0900000002); IF-06.cancelMark thành công | kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Hoàn tất không lỗi; getStatus() = CANCELLED; IF-14.save gọi với lớp C1; IF-06.cancelMark gọi với (AbsenceCheck, C1) và (WaitlistTransfer, C1); IF-03.sendPushNotification gọi với (M1, nội dung); IF-04.sendSms gọi với (0900000002, nội dung); mọi lời gọi gửi xảy ra sau commit | BR-13, BR-14; UC-015 bước 1 đến 7; P12 F3 | DT6-R8, EC-50, EC-52, EC-54, EC-58, BV-24, T4 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Cao |
| TC-047 | DC-CancelUnderBookedClassHandler.handleMarkDue | use case | Lớp C1 capacity 5, status SCHEDULED, chỗ đã đặt của M1, M2, M3 | kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Hoàn tất không lỗi; getStatus() = SCHEDULED; IF-14.save, IF-06.cancelMark, IF-03.sendPushNotification, IF-04.sendSms không được gọi | BR-13; UC-015 luồng 2b | DT6-R4, EC-55, BV-25 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Cao |
| TC-048 | DC-CancelUnderBookedClassHandler.handleMarkDue | use case | Lớp C1 capacity 5, chỗ đã đặt của M1, lớp đã huỷ | kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Hoàn tất không lỗi; getStatus() = CANCELLED; IF-14.save, IF-06.cancelMark, IF-03.sendPushNotification, IF-04.sendSms không được gọi | UC-015 luồng 2a; P12 F2 (xử lý lặp lại được) | DT6-R3, EC-56 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Cao |
| TC-049 | DC-CancelUnderBookedClassHandler.handleMarkDue | use case | Lớp C1 capacity 5, status SCHEDULED, chưa có chỗ đã đặt | kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Hoàn tất không lỗi; getStatus() = CANCELLED; IF-14.save gọi với lớp C1; IF-06.cancelMark gọi đúng 2 lần; IF-03.sendPushNotification và IF-04.sendSms không được gọi | BR-13; UC-015 luồng 5a | DT6-R7, EC-57, BV-26 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Cao |
| TC-050 | DC-CancelUnderBookedClassHandler.handleMarkDue | phân vùng tương đương | Không có lớp nào được nạp | kind AbsenceCheck, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Ném Error; IF-14.runInTransaction và IF-14.save không được gọi | P12 F2 ngoại lệ (Error khi kind khác ClassCutoff) | DT6-R1, EC-51 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Trung bình |
| TC-051 | DC-CancelUnderBookedClassHandler.handleMarkDue | phân vùng tương đương | IF-14.findByIdForUpdate trả null | kind ClassCutoff, subjectRef C404, dueAt 16:00 ngày 26/10/2026 | Hoàn tất không lỗi; IF-14.save, IF-06.cancelMark, IF-03.sendPushNotification, IF-04.sendSms không được gọi | P12 F3 bước 2 (null thì ghi nhật ký rồi kết thúc) | DT6-R2, EC-53 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Trung bình |
| TC-052 | DC-CancelUnderBookedClassHandler.handleMarkDue | use case | Lớp C1 capacity 5, status SCHEDULED, chỗ đã đặt của M1, M2 (cùng kênh thông báo đẩy); handleMarkDue đã được gọi một lần thành công | Gọi lần hai: kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Lần hai hoàn tất không lỗi; tổng IF-14.save = 1 lần, IF-06.cancelMark = 2 lần, IF-03.sendPushNotification = 2 lần (không gửi lại) | P12 F2 (xử lý lặp lại được); UC-015 luồng 2a | DT6-R3, EC-56, T4 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Cao |
| TC-053 | DC-CancelUnderBookedClassHandler.handleMarkDue | đường đi | Lớp C1 capacity 5, chỗ đã đặt của M1; IF-14.save bị từ chối với Error db down | kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Bị từ chối với Error db down; IF-06.cancelMark, IF-03.sendPushNotification, IF-04.sendSms không được gọi | P12 F3 (ranh giới giao dịch, gửi sau commit); P12 F2 (lỗi lan ra cho SS-06) | CE (đường lỗi giao dịch) | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Trung bình |
| TC-054 | DC-CancelUnderBookedClassHandler.handleMarkDue | đường đi | Lớp C1 capacity 5, chỗ đã đặt của M1; IF-06.cancelMark bị từ chối với MarkStoreUnavailable ở lần gọi đầu (AbsenceCheck) | kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Bị từ chối với MarkStoreUnavailable; IF-06.cancelMark gọi đúng 1 lần; IF-03.sendPushNotification và IF-04.sendSms không được gọi | P12 F2 ngoại lệ (cancelAbsenceMark; lỗi lan ra cho SS-06, Q-102) | DT6-R5, EC-59 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Trung bình |
| TC-055 | DC-CancelUnderBookedClassHandler.handleMarkDue | đường đi | Lớp C1 capacity 5, chỗ đã đặt của M1; IF-06.cancelMark thành công ở lần đầu, bị từ chối với MarkStoreUnavailable ở lần hai (WaitlistTransfer) | kind ClassCutoff, subjectRef C1, dueAt 16:00 ngày 26/10/2026 | Bị từ chối với MarkStoreUnavailable; IF-06.cancelMark gọi đúng 2 lần; IF-03.sendPushNotification và IF-04.sendSms không được gọi | P12 F2 ngoại lệ (cancelWaitlistTransferMark; lỗi lan ra cho SS-06, Q-102) | DT6-R6, EC-60 | IF-14 mock (findByIdForUpdate stub, save mock, runInTransaction fake ghi sự kiện commit), IF-06 mock, IF-03 mock, IF-04 mock, IF-16 stub | Trung bình |
| TC-056 | DC-CancelUnderBookedClassHandler.notifyBookedMembers | giá trị biên | Không có | members = danh sách rỗng, info của lớp C1 | Hoàn tất không lỗi; IF-03.sendPushNotification và IF-04.sendSms không được gọi | UC-015 luồng 5a; bước 7 (lặp cho mọi hội viên) | BV-27, EC-62 | IF-03 mock, IF-04 mock, DC-Member stub | Trung bình |
| TC-057 | DC-CancelUnderBookedClassHandler.notifyBookedMembers | bảng quyết định | M1 có kênh thông báo đẩy; M2 có kênh SMS, số 0900000002; cổng nhận thành công | members = M1, M2; info của lớp C1 | IF-03.sendPushNotification gọi đúng 1 lần với (M1, nội dung); IF-04.sendSms gọi đúng 1 lần với (0900000002, cùng nội dung); nội dung có body không rỗng | BR-14; UC-015 bước 6, 7; Dữ liệu ra 1 | DT7-R1, DT7-R3, EC-63, EC-64, BV-28 | IF-03 mock, IF-04 mock, DC-Member stub | Cao |
| TC-058 | DC-CancelUnderBookedClassHandler.notifyBookedMembers | bảng quyết định | M1, M2 cùng kênh thông báo đẩy; IF-03 từ chối lần đầu với InvalidNotificationContent | members = M1, M2; info của lớp C1 | Hoàn tất không lỗi; IF-03.sendPushNotification gọi 2 lần, lần sau cùng với M2 | P12 F2 (bỏ qua hội viên bị từ chối đầu vào, không chặn hội viên khác); Q-65 | DT7-R2, EC-65 | IF-03 mock, IF-04 mock, DC-Member stub | Trung bình |
| TC-059 | DC-CancelUnderBookedClassHandler.notifyBookedMembers | bảng quyết định | M1 (số invalid), M2 (số 0900000002) cùng kênh SMS; IF-04 từ chối lần đầu với InvalidPhoneNumber | members = M1, M2; info của lớp C1 | Hoàn tất không lỗi; IF-04.sendSms gọi 2 lần, lần sau cùng với 0900000002 | P12 F2 (như TC-058); Q-65 | DT7-R4, EC-66 | IF-03 mock, IF-04 mock, DC-Member stub | Trung bình |
| TC-060 | DC-CancelUnderBookedClassHandler.notifyBookedMembers | phân vùng tương đương | M1 có kênh thông báo đẩy; IF-03 từ chối với lỗi khác InvalidNotificationContent | members = M1; info của lớp C1 | Chưa xác định: chờ Q-65 | UC-015 luồng 6a | EC-67 | IF-03 mock, IF-04 mock, DC-Member stub | Trung bình |

## F4. Ma trận phủ

| Mục cần phủ | TC phủ | Đạt |
|---|---|---|
| EC-01 | TC-001, TC-002 | Có |
| EC-02 | Không có | Không: hành vi chờ Q-108 |
| EC-03 | Không có | Không: hành vi chờ Q-108 |
| EC-04 | TC-003 | Có |
| EC-05 | TC-006 | Có |
| EC-06 | TC-003, TC-004 | Có |
| EC-07 | TC-005 | Có |
| EC-08 | Không có | Không: hành vi chờ Q-108 |
| EC-09 | TC-008 | Có |
| EC-10 | TC-009, TC-010 | Có |
| EC-11 | TC-011 | Có |
| EC-12 | TC-014 | Có |
| EC-13 | TC-011 | Có |
| EC-14 | TC-013 | Có |
| EC-15 | TC-011 | Có |
| EC-16 | TC-012 | Có |
| EC-17 | Không có | Không: hành vi chờ Q-108 |
| EC-18 | TC-016 | Có |
| EC-19 | TC-018 | Có |
| EC-20 | TC-022 | Có |
| EC-21 | TC-019, TC-020 | Có |
| EC-22 | TC-021 | Có |
| EC-23 | TC-023 | Có |
| EC-24 | Không có | Không: chờ Q-11, Q-58 (TC-024 chưa xác định) |
| EC-25 | Không có | Không: chờ Q-11, Q-58 (TC-025 chưa xác định) |
| EC-26 | TC-026 | Có |
| EC-27 | TC-027 | Có |
| EC-28 | TC-028 | Có |
| EC-29 | TC-029, TC-030 | Có |
| EC-30 | TC-031 | Có |
| EC-31 | TC-032, TC-033, TC-034 | Có |
| EC-32 | Không có | Không: hành vi chờ Q-108 |
| EC-33 | TC-035 | Có |
| EC-34 | TC-037 | Có |
| EC-35 | TC-035 | Có |
| EC-36 | TC-036 | Có |
| EC-37 | TC-035 | Có |
| EC-38 | TC-038 | Có |
| EC-39 | TC-035 | Có |
| EC-40 | TC-039 | Có |
| EC-41 | TC-035 | Có |
| EC-42 | TC-040 | Có |
| EC-43 | TC-035 | Có |
| EC-44 | TC-041 | Có |
| EC-45 | TC-035 | Có |
| EC-46 | TC-042 | Có |
| EC-47 | TC-035 | Có |
| EC-48 | TC-043 | Có |
| EC-49 | Không có | Không: hành vi chờ Q-108 |
| EC-50 | TC-046 | Có |
| EC-51 | TC-050 | Có |
| EC-52 | TC-046 | Có |
| EC-53 | TC-051 | Có |
| EC-54 | TC-046 | Có |
| EC-55 | TC-047 | Có |
| EC-56 | TC-048, TC-052 | Có |
| EC-57 | TC-049 | Có |
| EC-58 | TC-046 | Có |
| EC-59 | TC-054 | Có |
| EC-60 | TC-055 | Có |
| EC-61 | Không có | Không: hành vi chờ Q-108 |
| EC-62 | TC-056 | Có |
| EC-63 | TC-057 | Có |
| EC-64 | TC-057 | Có |
| EC-65 | TC-058 | Có |
| EC-66 | TC-059 | Có |
| EC-67 | Không có | Không: chờ Q-65 (TC-060 chưa xác định) |
| BV-01 | TC-002 | Có |
| BV-02 | Không có | Không: hành vi chờ Q-108 |
| BV-03 | TC-003 | Có |
| BV-04 | TC-004 | Có |
| BV-05 | TC-005 | Có |
| BV-06 | TC-008 | Có |
| BV-07 | TC-009 | Có |
| BV-08 | TC-010 | Có |
| BV-09 | TC-013 | Có |
| BV-10 | TC-011 | Có |
| BV-11 | TC-011 | Có |
| BV-12 | TC-019 | Có |
| BV-13 | TC-020 | Có |
| BV-14 | TC-021 | Có |
| BV-15 | TC-026 | Có |
| BV-16 | TC-027 | Có |
| BV-17 | TC-029 | Có |
| BV-18 | TC-030 | Có |
| BV-19 | TC-031 | Có |
| BV-20 | TC-033 | Có |
| BV-21 | TC-034 | Có |
| BV-22 | TC-035 | Có |
| BV-23 | TC-042 | Có |
| BV-24 | TC-046 | Có |
| BV-25 | TC-047 | Có |
| BV-26 | TC-049 | Có |
| BV-27 | TC-056 | Có |
| BV-28 | TC-057 | Có |

Bảng quyết định và chuyển trạng thái:

| Mục cần phủ | TC phủ | Đạt |
|---|---|---|
| DT1-R1 đến DT1-R3 | TC-003, TC-004; TC-005; TC-006 | Có |
| DT1-R4 | TC-007 | Không: chưa xác định, chờ Q-109 |
| DT2-R1 đến DT2-R3 | TC-011, TC-012; TC-013; TC-014 | Có |
| DT2-R4 | TC-015 | Không: chưa xác định, chờ Q-109 |
| DT3-R1 đến DT3-R3 | TC-019, TC-020; TC-021; TC-022 | Có |
| DT4-R1 | TC-023 | Có |
| DT4-R2, DT4-R3 | TC-024, TC-025 | Không: chưa xác định, chờ Q-11, Q-58 |
| DT5-R1 đến DT5-R6 | TC-035; TC-036; TC-039; TC-040; TC-041; TC-042 | Có |
| DT5-R7 đến DT5-R31 | TC-044, TC-045 (đại diện) | Không: chờ Q-109 |
| DT6-R1 đến DT6-R8 | TC-050; TC-051; TC-048, TC-052; TC-047; TC-054; TC-055; TC-049; TC-046 | Có |
| DT7-R1 đến DT7-R4 | TC-057; TC-058; TC-057; TC-059 | Có |
| ST-01 T1 (create) | TC-001, TC-002 | Có |
| ST-01 T2 (reserveSpot) | TC-003, TC-004 | Có |
| ST-01 T3 (addToWaitlist) | TC-011, TC-012 | Có |
| ST-01 T4 (cancelClass) | TC-016, TC-017, TC-046, TC-049 | Có |
| ST-01 từ chối: Scheduled reserveSpot đủ chỗ | TC-005 | Có |
| ST-01 từ chối: Scheduled addToWaitlist chưa đủ chỗ | TC-013 | Có |
| ST-01 từ chối: Cancelled reserveSpot, addToWaitlist, cancelClass | TC-006; TC-014; TC-018 | Có |

Quy tắc nghiệp vụ và luồng thay thế P04:

| Mục cần phủ | TC phủ | Đạt |
|---|---|---|
| BR-06, BR-07 (thời hạn đặt chỗ) | TC-023, TC-040 (ánh xạ kết quả); TC-024, TC-025 chưa xác định | Không: quy tắc mâu thuẫn, chờ Q-11, Q-58; kiểm thử lại ở mức unit khi chốt, và ở mức tích hợp cho cơ chế mở đặt chỗ theo tuần |
| BR-08 (tối đa 2 lớp mỗi ngày) | TC-029 đến TC-034, TC-041 | Có |
| BR-09 (khoá quyền đặt lớp) | TC-036 | Có (điều kiện khoá do DC-Member quyết định, ngoài phạm vi) |
| BR-10 (sức chứa theo phòng) | TC-001, TC-002, TC-008 đến TC-010 | Có (việc xác định sức chứa theo phòng ở UC-009, ngoài phạm vi) |
| BR-11 (không vượt sức chứa) | TC-003 đến TC-005, TC-042, TC-043 | Không đủ: đặt chỗ đồng thời thật cần kiểm thử tích hợp có CSDL và khoá dòng (PKG-20) |
| BR-12 (vào danh sách chờ khi đủ chỗ) | TC-011 đến TC-014 | Có (joinWaitlist không chọn, xem F1) |
| BR-13 (dưới 3 người thì huỷ) | TC-019 đến TC-022, TC-046 đến TC-049 | Có |
| BR-14 (thông báo đẩy hoặc SMS) | TC-046, TC-057 | Có (cách xác định hội viên chưa cài ứng dụng ở DC-Member, Q-36) |
| UC-010 luồng chính (bước 3 đến 9) | TC-035 | Có |
| UC-010 4a | TC-036 | Có |
| UC-010 5a | TC-023, TC-039 | Có |
| UC-010 5b | TC-040 | Có (ánh xạ kết quả) |
| UC-010 6a | TC-041 | Có |
| UC-010 7a, 7a1 | TC-042, TC-043 | Có |
| UC-010 7a2 đến 7a4 | TC-011, TC-012 | Có (mức entity; mức handler joinWaitlist không chọn) |
| UC-010 7a2a | Không có | Không: hội viên không yêu cầu, không có bước hệ thống; thuộc giao diện |
| UC-015 luồng chính (bước 1 đến 7) | TC-046 | Có |
| UC-015 2a | TC-022, TC-048, TC-052 | Có |
| UC-015 2b | TC-021, TC-047 | Có |
| UC-015 5a | TC-049, TC-056 | Có |
| UC-015 6a | TC-058, TC-059, TC-060 | Không đủ: kết cục khi gửi không được chờ Q-65 (TC-060 chưa xác định) |
| UC-015 bước 4 (huỷ mốc) | TC-046, TC-054, TC-055 | Có |

Tóm tắt độ phủ so với MUC_TIEU_PHU (C1 cho mọi phương thức được chọn):

| Phương thức | V(G) | C0 | C1 | Đạt mục tiêu C1 |
|---|---|---|---|---|
| reserveSpot | 3 | 3/3 khối lệnh | 8/8 nhánh | Có |
| addToWaitlist | 4 | 4/4 khối lệnh | 11/11 nhánh | Có |
| assessCancellation | 3 | 4/4 khối lệnh | 9/9 nhánh | Có |
| assessBookability | 3 | 1/3 khối lệnh | 3/8 nhánh | Không: nhánh CE31, CE32, CE33, CE35, CE36 chưa phủ (lý do ở F2) |
| collectBookedMembers | 3 | 4/4 khối lệnh | 9/9 nhánh | Có |
| hasReachedDailyLimit | 1 | 1/1 khối lệnh | 2/2 nhánh | Có |
| bookClass | 10 | 13/14 khối lệnh | 31/33 nhánh | Không: nhánh CE69, CE79 chưa phủ (lý do ở F2) |
| handleMarkDue | 7 | 11/11 khối lệnh | 24/24 nhánh | Có |
| notifyBookedMembers | 4 | 5/5 khối lệnh | 12/12 nhánh | Có |
| GroupClass (constructor) | - | Đo khi có mã nguồn | Đo khi có mã nguồn | Mọi EC, BV và chuyển trạng thái đều có TC |
| hasAvailableSpot | - | Đo khi có mã nguồn | Đo khi có mã nguồn | Mọi EC, BV và chuyển trạng thái đều có TC |
| cancelClass | - | Đo khi có mã nguồn | Đo khi có mã nguồn | Mọi EC, BV và chuyển trạng thái đều có TC |

## F5. Khung mã test

Jest 29 với ts-jest, TypeScript, NestJS; đường dẫn import theo cấu trúc thư mục giả định src/group-class, src/member, src/scheduler, src/notification và có thể đổi theo cấu trúc dự án thật. Mỗi TC một test; TC chờ Q dùng it.skip kèm mã Q. Các test của DC-GroupClass dùng isOnWaitlist(member) theo đề xuất sửa P12.

F5.1. group-class.spec.ts (TC-001 đến TC-028)

```typescript
import {
  Bookability,
  CancellationCheck,
  GroupClass,
  GroupClassStatus,
  InvalidClassStateException,
  SpotUnavailableException,
  WaitlistNotAllowedException,
} from '../group-class';
import { Member } from '../../member/member';

const START = new Date(2026, 9, 26, 18, 0, 0, 0);
const NOW = new Date(2026, 9, 25, 10, 0, 0, 0);

const member = (id: string): Member => ({ getId: () => id }) as unknown as Member;

const newClass = (capacity: number): GroupClass =>
  new GroupClass('C1', 'Yoga', 'Phòng 2', 'Nguyễn Thị Lan', START, capacity);

const book = (c: GroupClass, ...ids: string[]): void => {
  ids.forEach((id) => c.reserveSpot(member(id)));
};

const bookedIds = (c: GroupClass): string[] =>
  c.collectBookedMembers().map((m) => m.getId()).sort();

describe('GroupClass', () => {
  describe('constructor', () => {
    it('TC-001 constructor_validCapacity_startsScheduledWithoutBookings', () => {
      const c = newClass(40);
      expect(c.getStatus()).toBe(GroupClassStatus.SCHEDULED);
      expect(c.getBookedCount()).toBe(0);
      expect(c.provideClassInfo()).toEqual({
        classId: 'C1', classType: 'Yoga', room: 'Phòng 2',
        trainer: 'Nguyễn Thị Lan', startTime: START,
      });
    });

    it('TC-002 constructor_zeroCapacity_startsScheduledWithoutBookings', () => {
      const c = newClass(0);
      expect(c.getStatus()).toBe(GroupClassStatus.SCHEDULED);
      expect(c.getBookedCount()).toBe(0);
    });
  });

  describe('reserveSpot', () => {
    it('TC-003 reserveSpot_emptyClass_addsBookingAndReturnsClassInfo', () => {
      const c = newClass(3);
      const info = c.reserveSpot(member('M1'));
      expect(info).toEqual(c.provideClassInfo());
      expect(c.getBookedCount()).toBe(1);
      expect(bookedIds(c)).toEqual(['M1']);
    });

    it('TC-004 reserveSpot_lastFreeSpot_fillsClass', () => {
      const c = newClass(3);
      book(c, 'M1', 'M2');
      c.reserveSpot(member('M3'));
      expect(c.getBookedCount()).toBe(3);
    });

    it('TC-005 reserveSpot_classFull_throwsSpotUnavailable', () => {
      const c = newClass(3);
      book(c, 'M1', 'M2', 'M3');
      expect(() => c.reserveSpot(member('M4'))).toThrow(SpotUnavailableException);
      expect(c.getBookedCount()).toBe(3);
      expect(bookedIds(c)).not.toContain('M4');
    });

    it('TC-006 reserveSpot_cancelledClassWithFreeSpot_throwsInvalidClassState', () => {
      const c = newClass(3);
      book(c, 'M1');
      c.cancelClass();
      expect(() => c.reserveSpot(member('M2'))).toThrow(InvalidClassStateException);
      expect(c.getStatus()).toBe(GroupClassStatus.CANCELLED);
      expect(c.getBookedCount()).toBe(1);
    });

    it.skip('TC-007 reserveSpot_cancelledAndFull_exceptionTypeUndefined (chờ Q-109)', () => {});
  });

  describe('hasAvailableSpot', () => {
    it.each([
      { id: 'TC-008', capacity: 3, booked: ['M1', 'M2'], expected: true },
      { id: 'TC-009', capacity: 3, booked: ['M1', 'M2', 'M3'], expected: false },
      { id: 'TC-010', capacity: 0, booked: [] as string[], expected: false },
    ])('$id hasAvailableSpot_capacity$capacity_returns$expected', ({ capacity, booked, expected }) => {
      const c = newClass(capacity);
      book(c, ...booked);
      expect(c.hasAvailableSpot()).toBe(expected);
      expect(c.getBookedCount()).toBe(booked.length);
    });
  });

  describe('addToWaitlist', () => {
    it('TC-011 addToWaitlist_fullClassEmptyWaitlist_returnsPositionOne', () => {
      const c = newClass(2);
      book(c, 'M1', 'M2');
      const m3 = member('M3');
      expect(c.addToWaitlist(m3, NOW)).toBe(1);
      expect(c.isOnWaitlist(m3)).toBe(true);
    });

    it('TC-012 addToWaitlist_secondMember_returnsPositivePositionAndKeepsBoth', () => {
      const c = newClass(2);
      book(c, 'M1', 'M2');
      const m3 = member('M3');
      const m4 = member('M4');
      c.addToWaitlist(m3, NOW);
      const position = c.addToWaitlist(m4, NOW);
      expect(Number.isInteger(position)).toBe(true);
      expect(position).toBeGreaterThanOrEqual(1);
      expect(position).toBeLessThanOrEqual(2);
      expect(c.isOnWaitlist(m3)).toBe(true);
      expect(c.isOnWaitlist(m4)).toBe(true);
    });

    it('TC-013 addToWaitlist_classNotFull_throwsWaitlistNotAllowed', () => {
      const c = newClass(2);
      book(c, 'M1');
      const m3 = member('M3');
      expect(() => c.addToWaitlist(m3, NOW)).toThrow(WaitlistNotAllowedException);
      expect(c.isOnWaitlist(m3)).toBe(false);
      expect(c.getBookedCount()).toBe(1);
    });

    it('TC-014 addToWaitlist_cancelledFullClass_throwsInvalidClassState', () => {
      const c = newClass(2);
      book(c, 'M1', 'M2');
      c.cancelClass();
      const m3 = member('M3');
      expect(() => c.addToWaitlist(m3, NOW)).toThrow(InvalidClassStateException);
      expect(c.isOnWaitlist(m3)).toBe(false);
    });

    it.skip('TC-015 addToWaitlist_cancelledAndNotFull_exceptionTypeUndefined (chờ Q-109)', () => {});
  });

  describe('cancelClass', () => {
    it('TC-016 cancelClass_scheduledWithoutBookings_becomesCancelled', () => {
      const c = newClass(3);
      c.cancelClass();
      expect(c.getStatus()).toBe(GroupClassStatus.CANCELLED);
      expect(c.getBookedCount()).toBe(0);
    });

    it('TC-017 cancelClass_withBookingsAndWaitlist_keepsBookingsAndWaitlist', () => {
      const c = newClass(2);
      book(c, 'M1', 'M2');
      const m3 = member('M3');
      c.addToWaitlist(m3, NOW);
      c.cancelClass();
      expect(c.getStatus()).toBe(GroupClassStatus.CANCELLED);
      expect(c.getBookedCount()).toBe(2);
      expect(bookedIds(c)).toEqual(['M1', 'M2']);
      expect(c.isOnWaitlist(m3)).toBe(true);
    });

    it('TC-018 cancelClass_alreadyCancelled_throwsInvalidClassState', () => {
      const c = newClass(3);
      c.cancelClass();
      expect(() => c.cancelClass()).toThrow(InvalidClassStateException);
      expect(c.getStatus()).toBe(GroupClassStatus.CANCELLED);
    });
  });

  describe('assessCancellation', () => {
    it.each([
      { id: 'TC-019', booked: [] as string[], expected: CancellationCheck.CANCELLABLE },
      { id: 'TC-020', booked: ['M1', 'M2'], expected: CancellationCheck.CANCELLABLE },
      { id: 'TC-021', booked: ['M1', 'M2', 'M3'], expected: CancellationCheck.ENOUGH_BOOKINGS },
    ])('$id assessCancellation_scheduledWith$booked.length Bookings_returns$expected', ({ booked, expected }) => {
      const c = newClass(5);
      book(c, ...booked);
      expect(c.assessCancellation()).toBe(expected);
      expect(c.getStatus()).toBe(GroupClassStatus.SCHEDULED);
    });

    it('TC-022 assessCancellation_cancelledClassWithThreeBookings_returnsAlreadyCancelled', () => {
      const c = newClass(5);
      book(c, 'M1', 'M2', 'M3');
      c.cancelClass();
      expect(c.assessCancellation()).toBe(CancellationCheck.ALREADY_CANCELLED);
      expect(c.getStatus()).toBe(GroupClassStatus.CANCELLED);
    });
  });

  describe('assessBookability', () => {
    it('TC-023 assessBookability_cancelledClass_returnsClassCancelled', () => {
      const c = newClass(5);
      c.cancelClass();
      expect(c.assessBookability(NOW)).toBe(Bookability.CLASS_CANCELLED);
    });

    it.skip('TC-024 assessBookability_scheduledWithinBookingWindow_returnsBookable (chờ Q-11, Q-58)', () => {});
    it.skip('TC-025 assessBookability_scheduledOutsideBookingWindow_returnsOutsideWindow (chờ Q-11, Q-58)', () => {});
  });

  describe('collectBookedMembers', () => {
    it('TC-026 collectBookedMembers_noBookings_returnsEmpty', () => {
      expect(newClass(5).collectBookedMembers()).toEqual([]);
    });

    it('TC-027 collectBookedMembers_oneBooking_returnsThatMember', () => {
      const c = newClass(5);
      book(c, 'M1');
      expect(bookedIds(c)).toEqual(['M1']);
    });

    it('TC-028 collectBookedMembers_memberHoldsTwoBookings_returnsMemberOnce', () => {
      const c = newClass(5);
      book(c, 'M1', 'M2', 'M1');
      expect(c.getBookedCount()).toBe(3);
      expect(bookedIds(c)).toEqual(['M1', 'M2']);
    });
  });
});
```

F5.2. member-booking-quota.spec.ts (TC-029 đến TC-034)

```typescript
import { MemberBookingQuota } from '../member-booking-quota';
import { IGroupClassRepository } from '../group-class-repository';

describe('MemberBookingQuota.hasReachedDailyLimit', () => {
  let count: jest.Mock;
  let quota: MemberBookingQuota;

  beforeEach(() => {
    count = jest.fn();
    quota = new MemberBookingQuota({ countMemberBookingsBetween: count } as unknown as IGroupClassRepository);
  });

  it.each([
    { id: 'TC-029', existing: 0, expected: false },
    { id: 'TC-030', existing: 1, expected: false },
    { id: 'TC-031', existing: 2, expected: true },
  ])('$id hasReachedDailyLimit_$existing existingBookings_returns$expected', async ({ existing, expected }) => {
    count.mockResolvedValue(existing);
    await expect(quota.hasReachedDailyLimit('M1', new Date(2026, 9, 26, 18, 0))).resolves.toBe(expected);
  });

  it.each([
    { id: 'TC-032', start: new Date(2026, 9, 26, 18, 0, 0, 0) },
    { id: 'TC-033', start: new Date(2026, 9, 26, 0, 0, 0, 0) },
    { id: 'TC-034', start: new Date(2026, 9, 26, 23, 59, 0, 0) },
  ])('$id hasReachedDailyLimit_classStartInSameDay_countsFromMidnightToNextMidnight', async ({ start }) => {
    count.mockResolvedValue(0);
    await quota.hasReachedDailyLimit('M1', start);
    expect(count).toHaveBeenCalledTimes(1);
    expect(count).toHaveBeenCalledWith('M1', new Date(2026, 9, 26, 0, 0, 0, 0), new Date(2026, 9, 27, 0, 0, 0, 0));
  });
});
```

F5.3. book-class-spot-handler.spec.ts (TC-035 đến TC-045)

```typescript
import {
  Bookability,
  BookingOutcome,
  GroupClass,
  GroupClassNotFoundException,
  GroupClassStatus,
} from '../group-class';
import { BookClassSpotHandler } from '../book-class-spot-handler';
import { MemberNotFoundException } from '../../member/member-not-found.exception';
import { Member } from '../../member/member';

const START = new Date(2026, 9, 26, 18, 0, 0, 0);
const NOW = new Date(2026, 9, 25, 10, 0, 0, 0);

const member = (id: string, suspended = false): Member =>
  ({ getId: () => id, isBookingSuspended: () => suspended }) as unknown as Member;

const newClass = (capacity: number, bookedBy: string[] = []): GroupClass => {
  const c = new GroupClass('C1', 'Yoga', 'Phòng 2', 'Nguyễn Thị Lan', START, capacity);
  bookedBy.forEach((id) => c.reserveSpot(member(id)));
  return c;
};

describe('BookClassSpotHandler.bookClass', () => {
  let accounts: { findById: jest.Mock };
  let quota: { hasReachedDailyLimit: jest.Mock };
  let repository: {
    findByIdForUpdate: jest.Mock;
    save: jest.Mock;
    runInTransaction: jest.Mock;
  };
  let handler: BookClassSpotHandler;

  const arrange = (c: GroupClass | null, m: Member | null = member('M9')): void => {
    accounts.findById.mockResolvedValue(m);
    repository.findByIdForUpdate.mockResolvedValue(c);
  };
  const forceBookable = (c: GroupClass, result = Bookability.BOOKABLE): void => {
    jest.spyOn(c, 'assessBookability').mockReturnValue(result);
  };

  beforeEach(() => {
    accounts = { findById: jest.fn() };
    quota = { hasReachedDailyLimit: jest.fn().mockResolvedValue(false) };
    repository = {
      findByIdForUpdate: jest.fn(),
      save: jest.fn().mockResolvedValue(undefined),
      runInTransaction: jest.fn((work: () => Promise<unknown>) => work()),
    };
    handler = new BookClassSpotHandler(
      repository as never, accounts as never, quota as never, { now: () => NOW },
    );
  });

  it('TC-035 bookClass_lastFreeSpot_returnsBookedAndSavesClass', async () => {
    const c = newClass(3, ['M1', 'M2']);
    forceBookable(c);
    arrange(c);
    const result = await handler.bookClass('M9', 'C1');
    expect(result.outcome).toBe(BookingOutcome.BOOKED);
    expect(result.classInfo).toEqual(c.provideClassInfo());
    expect(c.getBookedCount()).toBe(3);
    expect(repository.save).toHaveBeenCalledTimes(1);
    expect(repository.save).toHaveBeenCalledWith(c);
    expect(repository.runInTransaction).toHaveBeenCalledTimes(1);
  });

  it('TC-036 bookClass_memberSuspended_returnsMemberSuspendedWithoutSaving', async () => {
    const c = newClass(3, ['M1']);
    forceBookable(c);
    arrange(c, member('M9', true));
    const result = await handler.bookClass('M9', 'C1');
    expect(result.outcome).toBe(BookingOutcome.MEMBER_SUSPENDED);
    expect(result.classInfo).toBeNull();
    expect(repository.save).not.toHaveBeenCalled();
    expect(c.getBookedCount()).toBe(1);
  });

  it('TC-037 bookClass_memberNotFound_throwsMemberNotFound', async () => {
    arrange(newClass(3), null);
    await expect(handler.bookClass('M9', 'C1')).rejects.toBeInstanceOf(MemberNotFoundException);
    expect(repository.save).not.toHaveBeenCalled();
  });

  it('TC-038 bookClass_classNotFound_throwsGroupClassNotFound', async () => {
    arrange(null);
    await expect(handler.bookClass('M9', 'C404')).rejects.toBeInstanceOf(GroupClassNotFoundException);
    expect(repository.save).not.toHaveBeenCalled();
  });

  it('TC-039 bookClass_cancelledClass_returnsClassCancelledWithoutSaving', async () => {
    const c = newClass(3, ['M1']);
    c.cancelClass();
    arrange(c);
    const result = await handler.bookClass('M9', 'C1');
    expect(result.outcome).toBe(BookingOutcome.CLASS_CANCELLED);
    expect(result.classInfo).toBeNull();
    expect(repository.save).not.toHaveBeenCalled();
    expect(c.getBookedCount()).toBe(1);
  });

  it('TC-040 bookClass_outsideBookingWindow_returnsOutsideWindowWithoutSaving', async () => {
    const c = newClass(3, ['M1']);
    forceBookable(c, Bookability.OUTSIDE_BOOKING_WINDOW);
    arrange(c);
    const result = await handler.bookClass('M9', 'C1');
    expect(result.outcome).toBe(BookingOutcome.OUTSIDE_BOOKING_WINDOW);
    expect(repository.save).not.toHaveBeenCalled();
    expect(c.getBookedCount()).toBe(1);
  });

  it('TC-041 bookClass_dailyLimitReached_returnsDailyLimitReachedWithoutSaving', async () => {
    const c = newClass(3, ['M1']);
    forceBookable(c);
    arrange(c);
    quota.hasReachedDailyLimit.mockResolvedValue(true);
    const result = await handler.bookClass('M9', 'C1');
    expect(result.outcome).toBe(BookingOutcome.DAILY_LIMIT_REACHED);
    expect(quota.hasReachedDailyLimit).toHaveBeenCalledWith('M9', START);
    expect(repository.save).not.toHaveBeenCalled();
    expect(c.getBookedCount()).toBe(1);
  });

  it('TC-042 bookClass_classFull_returnsClassFullWithoutSaving', async () => {
    const c = newClass(3, ['M1', 'M2', 'M3']);
    forceBookable(c);
    arrange(c);
    const result = await handler.bookClass('M9', 'C1');
    expect(result.outcome).toBe(BookingOutcome.CLASS_FULL);
    expect(repository.save).not.toHaveBeenCalled();
    expect(c.getBookedCount()).toBe(3);
  });

  it('TC-043 bookClass_spotTakenBetweenCheckAndReserve_returnsClassFull', async () => {
    const c = newClass(3, ['M1', 'M2', 'M3']);
    forceBookable(c);
    jest.spyOn(c, 'hasAvailableSpot').mockReturnValue(true);
    arrange(c);
    const result = await handler.bookClass('M9', 'C1');
    expect(result.outcome).toBe(BookingOutcome.CLASS_FULL);
    expect(repository.save).not.toHaveBeenCalled();
    expect(c.getBookedCount()).toBe(3);
  });

  it.skip('TC-044 bookClass_suspendedAndCancelled_outcomeUndefined (chờ Q-109)', () => {});
  it.skip('TC-045 bookClass_dailyLimitAndFull_outcomeUndefined (chờ Q-109)', () => {});
});
```

F5.4. cancel-under-booked-class-handler.spec.ts (TC-046 đến TC-060)

```typescript
import { GroupClass, GroupClassStatus } from '../group-class';
import { CancelUnderBookedClassHandler } from '../cancel-under-booked-class-handler';
import { MarkKind } from '../../scheduler/mark-kind';
import { NotificationChannel } from '../../member/notification-channel';
import { InvalidNotificationContent } from '../../notification/invalid-notification-content';
import { InvalidPhoneNumber } from '../../notification/invalid-phone-number';
import { Member } from '../../member/member';

const START = new Date(2026, 9, 26, 18, 0, 0, 0);
const DUE = new Date(2026, 9, 26, 16, 0, 0, 0);

const member = (id: string, channel = NotificationChannel.PUSH, phone = `090000000${id.slice(1)}`): Member =>
  ({
    getId: () => id,
    determineNotificationChannel: () => channel,
    getPhoneNumber: () => phone,
  }) as unknown as Member;

const newClass = (capacity: number, bookedBy: Member[] = []): GroupClass => {
  const c = new GroupClass('C1', 'Yoga', 'Phòng 2', 'Nguyễn Thị Lan', START, capacity);
  bookedBy.forEach((m) => c.reserveSpot(m));
  return c;
};

describe('CancelUnderBookedClassHandler', () => {
  let events: string[];
  let repository: { findByIdForUpdate: jest.Mock; save: jest.Mock; runInTransaction: jest.Mock };
  let scheduler: { cancelMark: jest.Mock };
  let push: { sendPushNotification: jest.Mock };
  let sms: { sendSms: jest.Mock };
  let handler: CancelUnderBookedClassHandler;

  beforeEach(() => {
    events = [];
    repository = {
      findByIdForUpdate: jest.fn(),
      save: jest.fn(async () => { events.push('save'); }),
      runInTransaction: jest.fn(async (work: () => Promise<unknown>) => {
        const result = await work();
        events.push('commit');
        return result;
      }),
    };
    scheduler = { cancelMark: jest.fn(async () => { events.push('cancelMark'); }) };
    push = { sendPushNotification: jest.fn(async () => { events.push('push'); }) };
    sms = { sendSms: jest.fn(async () => { events.push('sms'); }) };
    handler = new CancelUnderBookedClassHandler(
      repository as never, scheduler as never, push as never, sms as never, { now: () => DUE },
    );
  });

  describe('handleMarkDue', () => {
    it('TC-046 handleMarkDue_underBookedClass_cancelsClassAndMarksThenNotifiesAfterCommit', async () => {
      const m1 = member('M1');
      const m2 = member('M2', NotificationChannel.SMS, '0900000002');
      const c = newClass(5, [m1, m2]);
      repository.findByIdForUpdate.mockResolvedValue(c);
      await handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE);
      expect(c.getStatus()).toBe(GroupClassStatus.CANCELLED);
      expect(repository.save).toHaveBeenCalledWith(c);
      expect(scheduler.cancelMark).toHaveBeenCalledWith(MarkKind.AbsenceCheck, 'C1');
      expect(scheduler.cancelMark).toHaveBeenCalledWith(MarkKind.WaitlistTransfer, 'C1');
      expect(push.sendPushNotification).toHaveBeenCalledWith(m1, expect.anything());
      expect(sms.sendSms).toHaveBeenCalledWith('0900000002', expect.anything());
      expect(events.indexOf('commit')).toBeLessThan(events.indexOf('push'));
      expect(events.indexOf('commit')).toBeLessThan(events.indexOf('sms'));
    });

    it('TC-047 handleMarkDue_threeBookings_doesNotCancel', async () => {
      const c = newClass(5, [member('M1'), member('M2'), member('M3')]);
      repository.findByIdForUpdate.mockResolvedValue(c);
      await expect(handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE)).resolves.toBeUndefined();
      expect(c.getStatus()).toBe(GroupClassStatus.SCHEDULED);
      expect(repository.save).not.toHaveBeenCalled();
      expect(scheduler.cancelMark).not.toHaveBeenCalled();
      expect(push.sendPushNotification).not.toHaveBeenCalled();
      expect(sms.sendSms).not.toHaveBeenCalled();
    });

    it('TC-048 handleMarkDue_alreadyCancelledClass_doesNothing', async () => {
      const c = newClass(5, [member('M1')]);
      c.cancelClass();
      repository.findByIdForUpdate.mockResolvedValue(c);
      await expect(handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE)).resolves.toBeUndefined();
      expect(repository.save).not.toHaveBeenCalled();
      expect(scheduler.cancelMark).not.toHaveBeenCalled();
      expect(push.sendPushNotification).not.toHaveBeenCalled();
    });

    it('TC-049 handleMarkDue_noBookings_cancelsClassWithoutNotifications', async () => {
      const c = newClass(5);
      repository.findByIdForUpdate.mockResolvedValue(c);
      await handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE);
      expect(c.getStatus()).toBe(GroupClassStatus.CANCELLED);
      expect(repository.save).toHaveBeenCalledWith(c);
      expect(scheduler.cancelMark).toHaveBeenCalledTimes(2);
      expect(push.sendPushNotification).not.toHaveBeenCalled();
      expect(sms.sendSms).not.toHaveBeenCalled();
    });

    it('TC-050 handleMarkDue_kindNotClassCutoff_throwsErrorWithoutTouchingData', async () => {
      await expect(handler.handleMarkDue(MarkKind.AbsenceCheck, 'C1', DUE)).rejects.toThrow(Error);
      expect(repository.runInTransaction).not.toHaveBeenCalled();
      expect(repository.save).not.toHaveBeenCalled();
    });

    it('TC-051 handleMarkDue_classNotFound_doesNothing', async () => {
      repository.findByIdForUpdate.mockResolvedValue(null);
      await expect(handler.handleMarkDue(MarkKind.ClassCutoff, 'C404', DUE)).resolves.toBeUndefined();
      expect(repository.save).not.toHaveBeenCalled();
      expect(scheduler.cancelMark).not.toHaveBeenCalled();
      expect(push.sendPushNotification).not.toHaveBeenCalled();
    });

    it('TC-052 handleMarkDue_redeliveredAfterCancel_doesNotNotifyAgain', async () => {
      const c = newClass(5, [member('M1'), member('M2')]);
      repository.findByIdForUpdate.mockResolvedValue(c);
      await handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE);
      await handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE);
      expect(repository.save).toHaveBeenCalledTimes(1);
      expect(scheduler.cancelMark).toHaveBeenCalledTimes(2);
      expect(push.sendPushNotification).toHaveBeenCalledTimes(2);
    });

    it('TC-053 handleMarkDue_saveFails_propagatesErrorWithoutMarksOrNotifications', async () => {
      const c = newClass(5, [member('M1')]);
      repository.findByIdForUpdate.mockResolvedValue(c);
      repository.save.mockRejectedValue(new Error('db down'));
      await expect(handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE)).rejects.toThrow('db down');
      expect(scheduler.cancelMark).not.toHaveBeenCalled();
      expect(push.sendPushNotification).not.toHaveBeenCalled();
    });

    it('TC-054 handleMarkDue_absenceMarkCancelFails_propagatesErrorWithoutNotifications', async () => {
      const c = newClass(5, [member('M1')]);
      repository.findByIdForUpdate.mockResolvedValue(c);
      scheduler.cancelMark.mockRejectedValueOnce(new Error('MarkStoreUnavailable'));
      await expect(handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE)).rejects.toThrow('MarkStoreUnavailable');
      expect(scheduler.cancelMark).toHaveBeenCalledTimes(1);
      expect(push.sendPushNotification).not.toHaveBeenCalled();
    });

    it('TC-055 handleMarkDue_waitlistTransferMarkCancelFails_propagatesErrorWithoutNotifications', async () => {
      const c = newClass(5, [member('M1')]);
      repository.findByIdForUpdate.mockResolvedValue(c);
      scheduler.cancelMark
        .mockResolvedValueOnce(undefined)
        .mockRejectedValueOnce(new Error('MarkStoreUnavailable'));
      await expect(handler.handleMarkDue(MarkKind.ClassCutoff, 'C1', DUE)).rejects.toThrow('MarkStoreUnavailable');
      expect(scheduler.cancelMark).toHaveBeenCalledTimes(2);
      expect(push.sendPushNotification).not.toHaveBeenCalled();
    });
  });

  describe('notifyBookedMembers', () => {
    const info = { classId: 'C1', classType: 'Yoga', room: 'Phòng 2', trainer: 'Nguyễn Thị Lan', startTime: START };
    const notify = (members: Member[]): Promise<void> => handler['notifyBookedMembers'](members, info);

    it('TC-056 notifyBookedMembers_noMembers_sendsNothing', async () => {
      await expect(notify([])).resolves.toBeUndefined();
      expect(push.sendPushNotification).not.toHaveBeenCalled();
      expect(sms.sendSms).not.toHaveBeenCalled();
    });

    it('TC-057 notifyBookedMembers_pushAndSmsMembers_usesChannelOfEachMember', async () => {
      const m1 = member('M1');
      const m2 = member('M2', NotificationChannel.SMS, '0900000002');
      await notify([m1, m2]);
      expect(push.sendPushNotification).toHaveBeenCalledTimes(1);
      expect(sms.sendSms).toHaveBeenCalledTimes(1);
      const content = push.sendPushNotification.mock.calls[0][1];
      expect(push.sendPushNotification).toHaveBeenCalledWith(m1, content);
      expect(sms.sendSms).toHaveBeenCalledWith('0900000002', content);
      expect(content.body.length).toBeGreaterThan(0);
    });

    it('TC-058 notifyBookedMembers_pushRejectedAsInvalidContent_skipsMemberAndContinues', async () => {
      const m1 = member('M1');
      const m2 = member('M2');
      push.sendPushNotification.mockRejectedValueOnce(new InvalidNotificationContent());
      await expect(notify([m1, m2])).resolves.toBeUndefined();
      expect(push.sendPushNotification).toHaveBeenCalledTimes(2);
      expect(push.sendPushNotification).toHaveBeenLastCalledWith(m2, expect.anything());
    });

    it('TC-059 notifyBookedMembers_smsRejectedAsInvalidPhone_skipsMemberAndContinues', async () => {
      const m1 = member('M1', NotificationChannel.SMS, 'invalid');
      const m2 = member('M2', NotificationChannel.SMS, '0900000002');
      sms.sendSms.mockRejectedValueOnce(new InvalidPhoneNumber());
      await expect(notify([m1, m2])).resolves.toBeUndefined();
      expect(sms.sendSms).toHaveBeenCalledTimes(2);
      expect(sms.sendSms).toHaveBeenLastCalledWith('0900000002', expect.anything());
    });

    it.skip('TC-060 notifyBookedMembers_gatewayFailsWithOtherError_outcomeUndefined (chờ Q-65)', () => {});
  });
});
```


## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-108 | Khi đầu vào vi phạm tiền điều kiện mà thiết kế không nêu hành vi (sức chứa âm hoặc không phải số nguyên khi tạo lớp; hội viên null khi đặt chỗ hoặc vào danh sách chờ; mã hội viên, mã lớp hoặc subjectRef rỗng hoặc null) thì hệ thống xử lý thế nào? (Ném ngoại lệ đầu vào không hợp lệ, nêu tên ngoại lệ / Coi như không tìm thấy / Khác - nêu rõ) | EC-02, EC-03, EC-08, EC-17, EC-32, EC-49, EC-61; BV-02; P12 F2 của GroupClass, reserveSpot, addToWaitlist, hasReachedDailyLimit, bookClass, handleMarkDue | P12 F2 chỉ nêu tiền điều kiện (capacity >= 0, member không rỗng) không nêu hành vi khi vi phạm |
| Q-109 | Khi một yêu cầu vi phạm đồng thời từ hai điều kiện trở lên thì hệ thống báo điều kiện nào? Gồm: đặt chỗ vào lớp đã huỷ và đã đủ chỗ (ném ngoại lệ nào); vào danh sách chờ khi lớp đã huỷ và chưa đủ chỗ (ném ngoại lệ nào); bookClass khi hội viên bị khoá, lớp đã huỷ, ngoài thời hạn, đủ số lớp trong ngày, lớp đủ chỗ cùng xảy ra (báo outcome nào). (Theo thứ tự kiểm tra 4, 5, 6, 7 của P04 mục 8 / Theo thứ tự ưu tiên khác - nêu rõ) | DT1-R4, DT2-R4, DT5-R7 đến DT5-R31; TC-007, TC-015, TC-044, TC-045 | UC-010 mục 8 nêu thứ tự các bước kiểm tra chỉ là thứ tự trình bày, nguồn không nêu thứ tự ưu tiên; P12 F2 liệt kê ngoại lệ không nêu thứ tự |

Các Q đã có làm đổi kết quả mong đợi của bộ test (nội dung không chép lại): Q-11, Q-58 (thời hạn đặt chỗ: TC-024, TC-025); Q-59 (đặt trùng: TC-028); Q-60 (cách tính ngày: TC-032 đến TC-034); Q-61 (thứ tự chờ: TC-012); Q-63 (chỗ khi lớp huỷ: TC-017); Q-65 (gửi không được: TC-060); Q-102 (lỗi cơ chế hẹn giờ: TC-054, TC-055); Q-106 (kết cục vào danh sách chờ không hợp lệ: TC-013).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P12 | DC-GroupClass (F2, F7) | Hậu điều kiện của addToWaitlist (danh sách chờ chứa hội viên) và các ca lỗi (danh sách chờ không đổi) không quan sát được qua operation công khai; DC-Waitlist.contains là public nhưng DC-GroupClass không cho truy cập waitlist | Thêm operation DC-GroupClass.isOnWaitlist(member: Member): boolean (truy vấn, không đổi dữ liệu), ánh xạ tới DC-Waitlist.contains; TC-011 đến TC-015, TC-017 dùng operation này |
| P12 | DC-CancelUnderBookedClassHandler.handleMarkDue, notifyBookedMembers (F2, F3, F5) | F3 ghi "ghi nhật ký" ở các nhánh lớp không tồn tại và hội viên bị từ chối đầu vào nhưng F5 không có phụ thuộc nhật ký (logger) và F2 không nêu hậu điều kiện này nên không kiểm được | Thêm phụ thuộc ILogger vào F5 của hai handler (hoặc ghi rõ nhật ký là mối quan tâm ngoài phạm vi test) |
| P12 | DC-CancelUnderBookedClassHandler.handleMarkDue (F2) | Nhánh lớp không tồn tại (kết thúc, ghi nhật ký) chỉ có ở F3 bước 2, F2 không nêu | Bổ sung vào hậu điều kiện của F2: lớp không còn thì kết thúc không đổi dữ liệu |
| P12 | DC-GroupClass.GroupClass, hasAvailableSpot, cancelClass (F3) | Không có thiết kế method nên không dựng được CFG và đo C0, C1 | Bổ sung dòng F3 cho ba operation này nếu muốn đo độ phủ ở mức thiết kế; nếu không, đo khi có mã nguồn |
| P12 | Tất cả operation nhận Member (PKG-26 chưa có P12) | Test dùng DC-Member stub với getId, isBookingSuspended, determineNotificationChannel, getPhoneNumber theo F4b | Đối chiếu F4b khi P12 PKG-26 chạy; chạy lại X2 nếu chữ ký khác |

## Vấn đề còn mở

Kết quả tự kiểm tra theo [Target]; các mục đạt không in lại. Các mục chưa đạt hoặc đạt một phần:

- Target 3 đạt một phần: biên thời hạn đặt chỗ (BR-06, BR-07) của assessBookability chưa có giá trị biên vì Q-11, Q-58 (TC-024, TC-025 chưa xác định).
- Target 4 đạt một phần: bảng quyết định DT5 của bookClass có 31 quy tắc; 25 quy tắc vi phạm từ hai điều kiện trở lên (DT5-R7 đến DT5-R31) kết quả chờ Q-109, chỉ hai quy tắc đại diện có dòng TC (TC-044, TC-045). Sinh thêm TC cho từng quy tắc khi Q-109 có đáp án (một bảng thứ tự ưu tiên giải quyết cả 25 quy tắc), đồng thời giữ tổng số TC trong giới hạn 60 của lần chạy này.
- Target 6 đạt một phần: BR-06, BR-07 (Q-11, Q-58), BR-11 phần đặt chỗ đồng thời thật (cần kiểm thử tích hợp có CSDL), UC-015 6a (Q-65), UC-010 7a2a (giao diện); lý do và mức kiểm thử phù hợp ghi ở F4.
- Target 7 đạt, trừ bảy TC ghi Chưa xác định (TC-007, TC-015, TC-024, TC-025, TC-044, TC-045, TC-060), theo F3.
- Target 9 đạt một phần: C1 chưa đạt 100% ở assessBookability (nhánh thời hạn, chờ Q-11, Q-58) và bookClass (nhánh D9 không thể đi tới theo đặc tả); ba operation không có F3 (constructor, hasAvailableSpot, cancelClass) ghi Đo khi có mã nguồn. V(G) lớn nhất là 10 (bookClass), không vượt ngưỡng.
- Target 10 đạt một phần: vòng duyệt hội viên của notifyBookedMembers kiểm 0 và 2 lần, chưa kiểm đúng 1 lần; n không xác định (capacity chưa cố định) nên n-1, n, n+1 không áp dụng. Vòng của collectBookedMembers kiểm 0, 1, 3.
- Target 12 đạt, trừ TC-058 và TC-059 mỗi TC có hai hội viên nhưng chỉ một giá trị không hợp lệ (hội viên đầu), hội viên sau là hợp lệ để chứng minh không bị chặn.
- Giới hạn lần chạy: 12 operation và 60 TC, ở mức trần; DC-BookClassSpotHandler.joinWaitlist không chọn (F1) và nên đưa vào lần chạy kế tiếp sau khi Q-106 có đáp án.
- Khung mã F5 chưa được biên dịch hoặc chạy vì chưa có mã nguồn thật của PKG-15, PKG-29; tên kiểu, đường dẫn import và chữ ký constructor của handler (thứ tự tham số tiêm) là giả định theo F5 của P12.
- Không lập sơ đồ CFG .drawio vì MUC_CHI_TIET của hồ sơ là GON.
