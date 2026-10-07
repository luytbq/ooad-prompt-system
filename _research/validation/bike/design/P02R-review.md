# P02R - Review use case - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P02R |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.0; yeu-cau-xe-dap.md |
| Phạm vi | TAC_NHAN, DANH_SACH_UC |

## Mục 1. Tóm tắt

- Đối tượng: P01-actors.md (9 tác nhân) và P02-usecases.md (24 use case) của CityBike; có tài liệu nguồn và P00. Phạm vi: TAC_NHAN, DANH_SACH_UC.
- Số phát hiện: Nghiêm trọng 0 / Trung bình 2 / Thấp 3.
- Kết luận: Đạt.
- Điểm làm tốt:
  - CAND-04 "Thuê xe và trả xe" và CAND-19 "Điều chuyển xe giữa các trạm" được nhận diện là summary và tách đúng theo phiên (UC-005, UC-007; UC-013, UC-014, UC-015).
  - Các việc hệ thống làm (tạm giữ tiền, tính cước, gửi hoá đơn, đánh dấu "Chờ kiểm tra") đều là bước của UC gây ra, không thành UC riêng (CAND-31 đến CAND-38).
  - Tác vụ quá 24 giờ thành UC-009 với ACT-09 Bộ định thời, tên theo kết quả nghiệp vụ "Ghi nhận xe thất lạc".

## Mục 2. Bảng kiểm kê

Không có (đối tượng đã có mã ACT, UC).

## Mục 3. Bảng phát hiện

| Mã | Phần tử | Vấn đề | Quy tắc vi phạm | Mức độ | Đề xuất sửa |
|---|---|---|---|---|---|
| UCR-01 | UC-007 Trả xe, ACT-08 Ụ khoá | ACT-08 ghi ở cột Tác nhân phụ, nhưng trong UC-007 hệ thống không gọi ụ khoá; ụ khoá tự gửi sự kiện "đã nhận xe" (EV-07) khi người thuê xe đẩy xe vào. Theo A-C, tác nhân phụ là bên hệ thống gọi tới | A-C | Trung bình | Giữ ACT-01 là tác nhân chính (bên khởi xướng để đạt mục tiêu của mình). Giữ ACT-08 trong cột Tác nhân phụ và ghi trong Mô tả ngắn: "ụ khoá là thiết bị trung gian báo sự kiện người thuê xe đẩy xe vào". Áp dụng cùng cách ghi cho UC-005 (ụ báo xe được rút ra) |
| UCR-02 | UC-014 Ghi nhận xe điều chuyển tại ụ | Tác nhân chính là ACT-08, trong khi UC-007 cùng dạng (người thao tác trên ụ, ụ báo sự kiện) lại lấy người làm tác nhân chính. Hai UC cùng cơ chế dùng hai cách chọn tác nhân | A-C, A-T2 | Trung bình | Giữ ACT-08 là tác nhân chính cho tới khi Q-07 được trả lời; ghi trong Mô tả ngắn "tác nhân chính xét lại theo Q-07". Khi Q-07 có câu trả lời, đổi tác nhân chính sang vai trò nhân viên được nêu và ACT-08 thành tác nhân phụ như UC-007 |
| UCR-03 | UC-018 Mở khoá tài khoản | "Mở khoá" dùng cho cả tài khoản (UC-018) và ụ khoá (bước của UC-005); dễ nhầm khi đọc tên | U-N4, U-N6 | Thấp | Giữ tên theo nguồn; phân biệt hai thuật ngữ ở P05 |
| UCR-04 | UC-012 Xem trạm sắp hết xe, sắp đầy | Tên liệt kê hai điều kiện bằng dấu phẩy | U-N7 | Thấp | Đổi tên thành "Xem trạm sắp hết xe hoặc sắp đầy" |
| UCR-05 | UC-003 Đăng nhập, ACT-06 Ban giám đốc | Nguồn không nói ban giám đốc có tài khoản; nối ACT-06 với UC-003 chưa có căn cứ trực tiếp | U-T10 | Thấp | Giữ, ghi trong Mô tả ngắn "danh sách tác nhân phải đăng nhập chờ Q-01" |

## Mục 4. Danh sách use case đề xuất sau sửa

| UC | Tên (VI) | Tên (EN) | Tác nhân chính | Tác nhân phụ | Mục tiêu (kết quả có giá trị) | Thay đổi | Mã phát hiện |
|---|---|---|---|---|---|---|---|
| UC-001 | Đăng ký tài khoản | Register Account | ACT-01 | - | Có tài khoản | Giữ | - |
| UC-002 | Liên kết thẻ thanh toán | Link Payment Card | ACT-01 | ACT-07 | Tài khoản đủ điều kiện thuê | Giữ | - |
| UC-003 | Đăng nhập | Log In | ACT-01 đến ACT-06 | - | Được xác thực | Giữ (ghi chú Q-01) | UCR-05 |
| UC-004 | Xem bản đồ trạm | View Station Map | ACT-01 | - | Biết số xe, số ụ trống | Giữ | - |
| UC-005 | Thuê xe | Rent Bike | ACT-01 | ACT-07, ACT-08 | Chuyến đi bắt đầu | Giữ (ghi chú vai trò ụ khoá) | UCR-01 |
| UC-006 | Xin thêm thời gian miễn phí | Request Extra Free Time | ACT-01 | - | Thêm 15 phút miễn phí | Giữ | - |
| UC-007 | Trả xe | Return Bike | ACT-01 | ACT-08, ACT-07 | Chuyến kết thúc, cước được thu | Giữ (ghi chú vai trò ụ khoá) | UCR-01 |
| UC-008 | Báo xe hỏng | Report Damaged Bike | ACT-01 | - | Xe hỏng bị chặn cho thuê | Giữ | - |
| UC-009 | Ghi nhận xe thất lạc | Record Lost Bike | ACT-09 | ACT-07 | Thu tạm giữ, khoá tài khoản | Giữ | - |
| UC-010 | Tra cứu xe chờ kiểm tra | Look Up Bikes Awaiting Inspection | ACT-03 | - | Biết xe chờ kiểm tra | Giữ | - |
| UC-011 | Ghi nhận kết quả kiểm tra xe | Record Bike Inspection Result | ACT-03 | - | Xe có kết quả và trạng thái mới | Giữ | - |
| UC-012 | Xem trạm sắp hết xe hoặc sắp đầy | View Low Or Full Stations | ACT-04 | - | Biết trạm cần điều chuyển | Đổi tên | UCR-04 |
| UC-013 | Lập lệnh điều chuyển | Create Transfer Order | ACT-04 | - | Có lệnh điều chuyển | Giữ | - |
| UC-014 | Ghi nhận xe điều chuyển tại ụ | Record Transfer At Dock | ACT-08 | - | Lệnh điều chuyển phản ánh đúng xe đã lấy, đưa | Giữ (ghi chú Q-07) | UCR-02 |
| UC-015 | Theo dõi lệnh điều chuyển | Track Transfer Order | ACT-04 | - | Biết tiến độ lệnh | Giữ | - |
| UC-016 | Tra cứu lịch sử chuyến đi | Look Up Trip History | ACT-02 | - | Có thông tin chuyến | Giữ | - |
| UC-017 | Điều chỉnh cước | Adjust Fare | ACT-02 | ACT-07 | Cước được hoàn, có lý do | Giữ | - |
| UC-018 | Mở khoá tài khoản | Unlock Account | ACT-02 | - | Tài khoản dùng lại được | Giữ | UCR-03 (P05) |
| UC-019 đến UC-023 | Quản lý trạm, ụ khoá, xe, tài khoản nhân viên, bảng giá cước | Manage ... | ACT-05 | - | Danh mục đúng thực tế | Giữ | - |
| UC-024 | Xem báo cáo hằng tuần | View Weekly Report | ACT-06 | - | Có số liệu tuần | Giữ | - |

## Mục 5. Quan hệ đề xuất sau sửa

Không có (phạm vi không gồm SO_DO).

## Mục 6. Giới hạn của review

- REQ-32 (Q-03) và nợ cước (Q-02) chưa được phủ do chờ câu hỏi mở; không tính là U-AP14.
- Quan hệ giữa UC-008 Báo xe hỏng và UC-007 Trả xe ("báo xe hỏng ngay khi trả xe") thuộc phạm vi SO_DO, chưa chấm.

## Câu hỏi mở

Không có

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Bộ tiêu chí A-C chỉ có hai loại "tác nhân chính" và "tác nhân phụ (hệ thống gọi tới)". Thiết bị trung gian báo sự kiện thay cho người thao tác (ụ khoá trong UC-005, UC-007, UC-014) không thuộc loại nào; UCR-01, UCR-02 là cách xử lý tạm.
