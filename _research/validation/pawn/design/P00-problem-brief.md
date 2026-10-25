# P00 - Chuẩn hoá yêu cầu - Hệ thống quản lý chuỗi cầm đồ Phúc An

| Thuộc tính | Giá trị |
|---|---|
| Bước | P00 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-cam-do.md; bien-ban-hop-bo-sung.md |
| Phạm vi | Toàn hệ thống, trừ nghiệp vụ chốt ca và cảnh báo định mức tiền mặt trong két (mục 8 của yeu-cau-cam-do.md, Ngoài trọng tâm phân tích) |
| Mã Q, ASM cuối đã cấp | Q-35, ASM-08 |

## 1. Bối cảnh và mục tiêu nghiệp vụ

Chuỗi cầm đồ Phúc An có 6 cửa hàng trong thành phố, mỗi ngày lập khoảng 400 hợp đồng mới và có khoảng 600 lượt đóng lãi hoặc chuộc đồ (yeu-cau-cam-do.md, đoạn mở đầu). Hiện hợp đồng viết tay hai liên, hạn hợp đồng theo dõi bằng bảng tính, khách phải tới quầy mới đóng lãi được, và cửa hàng thường để hợp đồng quá hạn mà không báo cho khách. Phúc An cần phần mềm để thay cách làm này.

Mục tiêu nghiệp vụ:
- Có phần mềm quản lý hợp đồng cầm đồ, tài sản cầm cố và tiền mặt tại quầy (nguồn: "Phúc An cần phần mềm quản lý hợp đồng cầm đồ, tài sản cầm cố và tiền mặt tại quầy", yeu-cau-cam-do.md, đoạn mở đầu). Phần nghiệp vụ chốt ca và định mức tiền mặt trong két của mục tiêu này nằm ngoài trọng tâm phân tích của lần chạy này.

## 2. Phạm vi

Trong phạm vi:
- Tiếp nhận khách và hồ sơ khách qua đầu đọc căn cước: REQ-05 đến REQ-09, REQ-91, REQ-92 (ASM-06)
- Định giá tài sản, gợi ý giá tham khảo, giới hạn số tiền cho vay: REQ-10 đến REQ-18, REQ-23 (ASM-05)
- Duyệt khoản vay: REQ-19, REQ-20, REQ-97
- Kiểm tra xe máy trên hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an: REQ-21 đến REQ-25, REQ-104
- Lập hợp đồng cầm đồ, in hợp đồng, nhãn mã vạch cho tài sản cầm cố: REQ-33 đến REQ-38 (ASM-01, ASM-03)
- Giải ngân bằng tiền mặt và chuyển khoản qua cổng chi hộ: REQ-29 đến REQ-32 (ASM-02)
- Đóng lãi gia hạn tại quầy và trên ứng dụng di động, trả bớt gốc, phí trễ hạn: REQ-39 đến REQ-49, REQ-100, REQ-101
- Chuộc đồ, biên nhận, lấy tài sản ra khỏi két: REQ-50 đến REQ-61 (ASM-04)
- Nhắc khách, chuyển chờ thanh lý, báo quản lý cửa hàng: REQ-62 đến REQ-68, REQ-98, REQ-99
- Thanh lý tài sản bằng bán tại quầy hoặc chuyển về bộ phận thanh lý của chuỗi, tính và trả tiền thừa cho khách: REQ-69 đến REQ-74 (ASM-07, ASM-08), REQ-102, REQ-103
- Ứng dụng di động của khách: đăng ký bằng OTP, xem hợp đồng, lịch sử đóng lãi, số tiền chuộc trong ngày: REQ-75 đến REQ-80
- Cấu hình lãi suất, tỉ lệ cho vay, bảng giá; báo cáo; kiểm toán viên xem hợp đồng và nhật ký; nhật ký thay đổi hợp đồng: REQ-15, REQ-16, REQ-28, REQ-81 đến REQ-89
- Tra cứu hợp đồng bằng mã vạch tại quầy và các yêu cầu phi chức năng: REQ-90 đến REQ-95
- Giao tiếp với hệ thống, thiết bị ngoài: REQ-06, REQ-24, REQ-32, REQ-43, REQ-58, REQ-90, REQ-99, REQ-105
- Quy mô và quy tắc vai trò: REQ-01 đến REQ-04, REQ-96

Ngoài phạm vi:
- Nghiệp vụ chốt ca của thủ quỹ: kiểm đếm tiền mặt cuối ca, chốt ca trên phần mềm, quản lý cửa hàng xác nhận chênh lệch từ 200.000 đồng trở lên (yeu-cau-cam-do.md, Mục 8, câu 1). Lý do: Ngoài trọng tâm phân tích.
- Định mức tiền mặt trong két của cửa hàng không vượt 500 triệu đồng và cảnh báo quản lý cửa hàng để nộp bớt về ngân hàng (yeu-cau-cam-do.md, Mục 8, câu 2). Lý do: Ngoài trọng tâm phân tích.
- Chuộc đồ qua ứng dụng di động (nguồn: "Khách không chuộc đồ qua ứng dụng", yeu-cau-cam-do.md, Mục 7, câu 3).
- Việc bán tài sản tại bộ phận thanh lý của chuỗi (nguồn: "Việc bán tài sản ở bộ phận thanh lý của chuỗi làm ngoài phần mềm", bien-ban-hop-bo-sung.md, mục 5). Phần nhập số tiền bán được và tính tiền thừa vẫn trong phạm vi (REQ-102, REQ-103).

Chờ Q-nn: Không có (không có câu nêu phạm vi mâu thuẫn với mô tả chi tiết của cùng chức năng).

## 3. Các bên liên quan và người dùng

| SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống | REQ |
|---|---|---|---|---|---|
| SH-01 | Chuỗi cầm đồ Phúc An | Chủ sở hữu, người đặt hàng | Quản lý hợp đồng cầm đồ, tài sản cầm cố và tiền mặt tại quầy; báo khách khi hợp đồng quá hạn | Chưa rõ | REQ-01, REQ-02, REQ-03 |
| SH-02 | Khách (người cầm đồ) | Người dùng trực tiếp | Cầm đồ, đóng lãi, chuộc đồ; xem hợp đồng và đóng lãi trên ứng dụng di động; nhận tin nhắc | Có (ứng dụng di động) | REQ-09, REQ-39, REQ-42, REQ-50, REQ-75, REQ-78 |
| SH-03 | Nhân viên giao dịch | Người dùng trực tiếp | Đọc thẻ căn cước, in hợp đồng, quét mã vạch lấy tài sản, in biên nhận | Có | REQ-05, REQ-33, REQ-55, REQ-57, REQ-61 |
| SH-04 | Đầu đọc căn cước gắn chip tại quầy | Hệ thống hoặc thiết bị ngoài | Cung cấp họ tên, số căn cước, ngày sinh, địa chỉ từ thẻ | Có | REQ-06 |
| SH-05 | Nhân viên định giá | Người dùng trực tiếp | Chụp ảnh, ghi đặc điểm, nhập giá định giá tài sản | Có | REQ-10, REQ-11, REQ-13 |
| SH-06 | Quản lý chuỗi | Người vận hành, quản trị | Đặt lãi suất, tỉ lệ cho vay, cập nhật bảng giá, xem báo cáo | Có | REQ-15, REQ-28, REQ-81 đến REQ-84 |
| SH-07 | Quản lý cửa hàng | Người dùng trực tiếp | Duyệt khoản vay, nhận báo hợp đồng chờ thanh lý, quyết định thanh lý | Có | REQ-19, REQ-68, REQ-69, REQ-72 |
| SH-08 | Hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an | Hệ thống hoặc thiết bị ngoài | Trả kết quả xe máy có trong danh sách mất cắp hay không | Có | REQ-24 |
| SH-09 | Thủ quỹ | Người dùng trực tiếp | Giải ngân, thu tiền lãi, thu tiền chuộc, ghi nhận trả tiền thừa | Có | REQ-29, REQ-30, REQ-41, REQ-56, REQ-74 |
| SH-10 | Cổng chi hộ của ngân hàng đối tác | Hệ thống hoặc thiết bị ngoài | Thực hiện lệnh chuyển khoản giải ngân | Có | REQ-32 |
| SH-11 | Máy in nhãn mã vạch tại quầy | Hệ thống hoặc thiết bị ngoài | In nhãn mã vạch dán lên tài sản cầm cố | Có | REQ-105 |
| SH-12 | Cổng thanh toán trực tuyến | Hệ thống hoặc thiết bị ngoài | Xử lý thanh toán đóng lãi trên ứng dụng di động | Có | REQ-43 |
| SH-13 | Người được chủ hợp đồng uỷ quyền chuộc đồ | Người hưởng lợi gián tiếp | Chuộc đồ thay chủ hợp đồng bằng giấy uỷ quyền có công chứng | Không | REQ-54, REQ-55 |
| SH-14 | Máy quét mã vạch tại quầy | Hệ thống hoặc thiết bị ngoài | Đọc mã vạch trên nhãn tài sản | Có | REQ-58 |
| SH-15 | Cổng SMS của nhà mạng | Hệ thống hoặc thiết bị ngoài | Chuyển tin nhắn và mã OTP tới khách | Có | REQ-90 |
| SH-16 | Người mua tài sản thanh lý tại quầy | Người hưởng lợi gián tiếp | Mua tài sản thanh lý tại quầy | Không | REQ-69 |
| SH-17 | Bộ phận thanh lý của chuỗi | Người vận hành, quản trị | Nhận tài sản chuyển về và bán ngoài phần mềm | Không | REQ-72, REQ-102 |
| SH-18 | Kiểm toán viên nội bộ | Cơ quan quản lý | Xem mọi hợp đồng và nhật ký thao tác, không sửa được | Có | REQ-85, REQ-86, REQ-87 |
| SH-19 | Dịch vụ thông báo đẩy của nền tảng di động | Hệ thống hoặc thiết bị ngoài | Chuyển tin nhắc tới ứng dụng di động của khách | Có | REQ-99 |
| SH-20 | Kế toán chuỗi | Người dùng trực tiếp | Nhập số tiền bán được của tài sản bán ở bộ phận thanh lý | Có | REQ-102 |

## 4. Danh sách yêu cầu

| REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |
|---|---|---|---|---|
| REQ-01 | Hệ thống phục vụ chuỗi gồm 6 cửa hàng trong thành phố. | Dữ liệu | "Chuỗi cầm đồ Phúc An có 6 cửa hàng trong thành phố" (yeu-cau-cam-do.md, đoạn mở đầu, câu 1) | Quy mô, dùng cho P06 |
| REQ-02 | Hệ thống xử lý khoảng 400 hợp đồng mới mỗi ngày trên toàn chuỗi. | Dữ liệu | "mỗi ngày toàn chuỗi lập khoảng 400 hợp đồng mới" (yeu-cau-cam-do.md, đoạn mở đầu, câu 1) | Quy mô, dùng cho P06 |
| REQ-03 | Hệ thống xử lý khoảng 600 lượt đóng lãi hoặc chuộc đồ mỗi ngày trên toàn chuỗi. | Dữ liệu | "có khoảng 600 lượt đóng lãi hoặc chuộc đồ" (yeu-cau-cam-do.md, đoạn mở đầu, câu 1) | Quy mô, dùng cho P06 |
| REQ-04 | Chuỗi nhận cầm các loại tài sản điện thoại, máy tính xách tay, xe máy, vàng nữ trang. | Quy tắc nghiệp vụ | "Khách đến quầy mang theo tài sản (điện thoại, máy tính xách tay, xe máy, vàng nữ trang)" (yeu-cau-cam-do.md, Mục 1, câu 1) | Q-35 |
| REQ-05 | Nhân viên giao dịch có thể lấy họ tên, số căn cước, ngày sinh và địa chỉ của khách từ thẻ căn cước bằng đầu đọc căn cước gắn chip tại quầy. | Chức năng | "Nhân viên giao dịch đặt thẻ lên đầu đọc căn cước gắn chip tại quầy để lấy họ tên, số căn cước, ngày sinh và địa chỉ" (yeu-cau-cam-do.md, Mục 1, câu 2) | Kênh: đầu đọc căn cước (REQ-06) |
| REQ-06 | Hệ thống trao đổi dữ liệu thẻ căn cước (họ tên, số căn cước, ngày sinh, địa chỉ) với đầu đọc căn cước gắn chip tại quầy để lấy thông tin khách. | Giao tiếp ngoài | "đầu đọc căn cước gắn chip tại quầy" (yeu-cau-cam-do.md, Mục 1, câu 2)<br>project-profile.md, HE_THONG_NGOAI | Tách từ cùng câu với REQ-05. HE_THONG_NGOAI: kết nối USB, có bộ thư viện của nhà sản xuất |
| REQ-07 | Hệ thống tạo hồ sơ khách khi khách chưa có hồ sơ. | Chức năng | "khách mới thì phần mềm tạo hồ sơ khách" (yeu-cau-cam-do.md, Mục 1, câu 2) | Q-19 |
| REQ-08 | Hệ thống mở hồ sơ khách đã có khi khách đã có hồ sơ. | Chức năng | "khách cũ thì mở hồ sơ đã có" (yeu-cau-cam-do.md, Mục 1, câu 2) | Q-19 |
| REQ-09 | Khách dưới 18 tuổi không được cầm đồ. | Quy tắc nghiệp vụ | "Khách dưới 18 tuổi không được cầm đồ." (yeu-cau-cam-do.md, Mục 1, câu 3) | Không có |
| REQ-10 | Nhân viên định giá có thể chụp ảnh tài sản cầm cố. | Chức năng | "Nhân viên định giá kiểm tra tài sản, chụp ảnh" (yeu-cau-cam-do.md, Mục 2, câu 1) | Ảnh tài sản lưu theo REQ-93 |
| REQ-11 | Nhân viên định giá có thể ghi đặc điểm của tài sản cầm cố. | Chức năng | "ghi đặc điểm (hãng, model, số IMEI hoặc số khung, tình trạng)" (yeu-cau-cam-do.md, Mục 2, câu 1) | Tách từ cùng câu với REQ-10 |
| REQ-12 | Đặc điểm tài sản gồm hãng, model, số IMEI hoặc số khung, tình trạng. | Dữ liệu | "ghi đặc điểm (hãng, model, số IMEI hoặc số khung, tình trạng)" (yeu-cau-cam-do.md, Mục 2, câu 1) | Tách từ cùng câu với REQ-11. Danh sách không có số máy, xem REQ-23 và Q-05 |
| REQ-13 | Nhân viên định giá có thể nhập giá định giá của tài sản cầm cố. | Chức năng | "và nhập giá định giá" (yeu-cau-cam-do.md, Mục 2, câu 1) | Tách từ cùng câu với REQ-10 |
| REQ-14 | Hệ thống gợi ý giá tham khảo cho tài sản loại điện thoại và máy tính xách tay theo bảng giá thị trường. | Chức năng | "Với điện thoại và máy tính xách tay, phần mềm gợi ý giá tham khảo theo bảng giá thị trường" (yeu-cau-cam-do.md, Mục 2, câu 2) | Q-13 |
| REQ-15 | Quản lý chuỗi có thể cập nhật bảng giá thị trường dùng để gợi ý giá tham khảo. | Chức năng | "bảng giá thị trường do quản lý chuỗi cập nhật hằng tuần" (yeu-cau-cam-do.md, Mục 2, câu 2)<br>"cập nhật bảng giá tham khảo" (yeu-cau-cam-do.md, Mục 9, câu 1) | Gộp hai chỗ nguồn. Q-13 |
| REQ-16 | Bảng giá thị trường được quản lý chuỗi cập nhật hằng tuần. | Quy tắc nghiệp vụ | "bảng giá thị trường do quản lý chuỗi cập nhật hằng tuần" (yeu-cau-cam-do.md, Mục 2, câu 2) | Tách từ cùng câu với REQ-14 |
| REQ-17 | Số tiền cho vay tối đa bằng 80% giá định giá với vàng nữ trang. | Quy tắc nghiệp vụ | "Số tiền cho vay tối đa bằng 80% giá định giá với vàng nữ trang" (yeu-cau-cam-do.md, Mục 2, câu 3) | Q-10 |
| REQ-18 | Số tiền cho vay tối đa bằng 60% giá định giá với các loại tài sản khác ngoài vàng nữ trang. | Quy tắc nghiệp vụ | "60% với các loại tài sản khác" (yeu-cau-cam-do.md, Mục 2, câu 3) | Tách từ cùng câu với REQ-17. Q-10, Q-35 |
| REQ-19 | Quản lý cửa hàng có thể duyệt khoản vay trên phần mềm. | Chức năng | "phải được quản lý cửa hàng duyệt trên phần mềm trước khi giải ngân" (yeu-cau-cam-do.md, Mục 2, câu 4) | Q-12 |
| REQ-20 | Khoản vay từ 5 triệu đồng trở lên phải được quản lý cửa hàng duyệt trước khi giải ngân. | Quy tắc nghiệp vụ | "Khoản vay từ 5 triệu đồng trở lên phải được quản lý cửa hàng duyệt trên phần mềm trước khi giải ngân." (yeu-cau-cam-do.md, Mục 2, câu 4) | Tách từ cùng câu với REQ-19 theo F2 quy tắc 5 |
| REQ-21 | Xe máy cầm cố phải có giấy đăng ký xe đứng tên khách. | Quy tắc nghiệp vụ | "Xe máy phải có giấy đăng ký xe đứng tên khách" (yeu-cau-cam-do.md, Mục 2, câu 5) | Q-18 |
| REQ-22 | Hệ thống gửi số khung và số máy của xe máy sang hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an trước khi giải ngân. | Chức năng | "trước khi giải ngân, phần mềm gửi số khung, số máy sang hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an" (yeu-cau-cam-do.md, Mục 2, câu 5) | Kênh: REQ-24. Q-05 |
| REQ-23 | Nhân viên định giá có thể ghi số máy của xe máy khi ghi đặc điểm tài sản. | Chức năng | Giả định ASM-05 | Phục vụ REQ-22. Q-05 |
| REQ-24 | Hệ thống trao đổi số khung, số máy và kết quả tra cứu với hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an để kiểm tra xe máy trước khi cầm. | Giao tiếp ngoài | "hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an" (yeu-cau-cam-do.md, Mục 2, câu 5)<br>project-profile.md, HE_THONG_NGOAI | Tách từ cùng câu với REQ-22. HE_THONG_NGOAI: chưa có tài liệu API. Q-21 |
| REQ-25 | Xe máy chỉ được cầm khi kết quả tra cứu phương tiện bị mất cắp là không có trong danh sách. | Quy tắc nghiệp vụ | "chỉ cho cầm khi kết quả là không có trong danh sách" (yeu-cau-cam-do.md, Mục 2, câu 5) | Tách từ cùng câu với REQ-22 |
| REQ-26 | Hợp đồng cầm đồ có kỳ hạn 30 ngày. | Quy tắc nghiệp vụ | "Hợp đồng có kỳ hạn 30 ngày" (yeu-cau-cam-do.md, Mục 3, câu 1) | Không có |
| REQ-27 | Lãi được tính theo ngày trên số tiền gốc còn nợ. | Quy tắc nghiệp vụ | "lãi tính theo ngày trên số tiền gốc còn nợ" (yeu-cau-cam-do.md, Mục 3, câu 1) | Q-24 |
| REQ-28 | Quản lý chuỗi có thể đặt lãi suất cho từng loại tài sản. | Chức năng | "với lãi suất do quản lý chuỗi đặt cho từng loại tài sản" (yeu-cau-cam-do.md, Mục 3, câu 1)<br>"Quản lý chuỗi đặt lãi suất và tỉ lệ cho vay theo loại tài sản" (yeu-cau-cam-do.md, Mục 9, câu 1) | Gộp hai chỗ nguồn. Q-24 |
| REQ-29 | Thủ quỹ có thể giải ngân khoản vay bằng tiền mặt tại quầy. | Chức năng | "Thủ quỹ giải ngân bằng tiền mặt tại quầy" (yeu-cau-cam-do.md, Mục 3, câu 2) | Không có |
| REQ-30 | Thủ quỹ có thể giải ngân khoản vay bằng chuyển khoản vào tài khoản ngân hàng của khách qua cổng chi hộ của ngân hàng đối tác. | Chức năng | "chuyển khoản vào tài khoản ngân hàng của khách qua cổng chi hộ của ngân hàng đối tác" (yeu-cau-cam-do.md, Mục 3, câu 2) | Kênh: REQ-32. Q-14 |
| REQ-31 | Thủ quỹ có thể nhập thông tin tài khoản ngân hàng của khách khi giải ngân bằng chuyển khoản. | Chức năng | Giả định ASM-02 | Phục vụ REQ-30. Q-02 |
| REQ-32 | Hệ thống trao đổi lệnh chi và kết quả chi với cổng chi hộ của ngân hàng đối tác để giải ngân khoản vay bằng chuyển khoản. | Giao tiếp ngoài | "cổng chi hộ của ngân hàng đối tác" (yeu-cau-cam-do.md, Mục 3, câu 2)<br>project-profile.md, HE_THONG_NGOAI | Tách từ cùng câu với REQ-30. HE_THONG_NGOAI: API REST, có tài liệu API chi hộ và tra cứu lệnh chi |
| REQ-33 | Nhân viên giao dịch có thể in hợp đồng cầm đồ để khách ký. | Chức năng | "Nhân viên giao dịch in hợp đồng để khách ký" (yeu-cau-cam-do.md, Mục 3, câu 3) | Không có |
| REQ-34 | Nhân viên giao dịch có thể lập hợp đồng cầm đồ cho tài sản đã định giá. | Chức năng | Giả định ASM-01 | Phục vụ REQ-33. Q-01 |
| REQ-35 | Nhân viên giao dịch có thể nhập số tiền cho vay của hợp đồng cầm đồ. | Chức năng | Giả định ASM-01 | Phục vụ REQ-33. Q-01 |
| REQ-36 | Tài sản cầm cố được dán nhãn mã vạch theo mã hợp đồng. | Quy tắc nghiệp vụ | "tài sản được dán nhãn mã vạch theo mã hợp đồng" (yeu-cau-cam-do.md, Mục 3, câu 3) | Câu bị động không có chủ thể. Q-03 |
| REQ-37 | Nhân viên giao dịch có thể in nhãn mã vạch theo mã hợp đồng cho tài sản cầm cố. | Chức năng | Giả định ASM-03 | Phục vụ REQ-36. Kênh: máy in nhãn (REQ-105). Q-03 |
| REQ-38 | Tài sản cầm cố được cất vào két của cửa hàng. | Quy tắc nghiệp vụ | "rồi cất vào két của cửa hàng" (yeu-cau-cam-do.md, Mục 3, câu 3) | Câu bị động không có chủ thể. Q-23 |
| REQ-39 | Khách có thể đóng lãi để gia hạn hợp đồng cầm đồ. | Chức năng | "Khách đóng lãi để gia hạn hợp đồng thêm 30 ngày" (yeu-cau-cam-do.md, Mục 4, câu 1) | Không có |
| REQ-40 | Mỗi lần gia hạn kéo dài hợp đồng cầm đồ thêm 30 ngày. | Quy tắc nghiệp vụ | "gia hạn hợp đồng thêm 30 ngày" (yeu-cau-cam-do.md, Mục 4, câu 1) | Tách từ cùng câu với REQ-39 |
| REQ-41 | Thủ quỹ có thể thu tiền mặt tại quầy khi khách đóng lãi để gia hạn hợp đồng. | Chức năng | "tại quầy (thủ quỹ thu tiền mặt)" (yeu-cau-cam-do.md, Mục 4, câu 1) | Không có |
| REQ-42 | Khách có thể đóng lãi để gia hạn hợp đồng trên ứng dụng di động của Phúc An qua cổng thanh toán trực tuyến. | Chức năng | "hoặc trên ứng dụng di động của Phúc An qua cổng thanh toán trực tuyến" (yeu-cau-cam-do.md, Mục 4, câu 1)<br>"đóng lãi trực tuyến" (yeu-cau-cam-do.md, Mục 7, câu 2) | Kênh: REQ-43. Gộp hai chỗ nguồn (Trùng lặp). Q-15 |
| REQ-43 | Hệ thống trao đổi thông tin giao dịch và kết quả thanh toán với cổng thanh toán trực tuyến để thu tiền lãi đóng trên ứng dụng di động. | Giao tiếp ngoài | "qua cổng thanh toán trực tuyến" (yeu-cau-cam-do.md, Mục 4, câu 1)<br>project-profile.md, HE_THONG_NGOAI | Tách từ cùng câu với REQ-42. HE_THONG_NGOAI: API REST, có tài liệu API thanh toán và tra cứu giao dịch |
| REQ-44 | Mỗi hợp đồng cầm đồ được gia hạn tối đa 6 lần. | Quy tắc nghiệp vụ | "một hợp đồng được gia hạn tối đa 6 lần" (yeu-cau-cam-do.md, Mục 4, câu 1) | Mâu thuẫn với REQ-101. Q-09 |
| REQ-45 | Khách có thể trả bớt một phần tiền gốc khi đóng lãi tại quầy. | Chức năng | "Khi đóng lãi tại quầy, khách có thể trả bớt một phần tiền gốc." (yeu-cau-cam-do.md, Mục 4, câu 2) | Không có |
| REQ-46 | Hệ thống huỷ giao dịch thanh toán trực tuyến chưa thành công khi quá ngưỡng thời gian ở REQ-47. | Chức năng | "Giao dịch thanh toán trực tuyến chưa thành công trong 10 phút thì bị huỷ." (yeu-cau-cam-do.md, Mục 4, câu 3) | Ngưỡng ở REQ-47. Q-15 |
| REQ-47 | Ngưỡng huỷ giao dịch thanh toán trực tuyến chưa thành công là 10 phút. | Quy tắc nghiệp vụ | "chưa thành công trong 10 phút" (yeu-cau-cam-do.md, Mục 4, câu 3) | Tách từ cùng câu với REQ-46. Q-25 |
| REQ-48 | Phí trễ hạn áp dụng cho khách đóng lãi sau ngày đến hạn quá 3 ngày. | Quy tắc nghiệp vụ | "Khách đóng lãi sau ngày đến hạn quá 3 ngày thì chịu phí trễ hạn" (yeu-cau-cam-do.md, Mục 4, câu 4) | Không có |
| REQ-49 | Phí trễ hạn bằng 1% tiền gốc còn nợ. | Quy tắc nghiệp vụ | "phí trễ hạn bằng 1% tiền gốc còn nợ" (yeu-cau-cam-do.md, Mục 4, câu 4) | Tách từ cùng câu với REQ-48. Làm rõ bởi REQ-100 |
| REQ-50 | Khách có thể chuộc tài sản cầm cố. | Chức năng | "Khách chuộc đồ" (yeu-cau-cam-do.md, Mục 5, câu 1) | Q-11 |
| REQ-51 | Khách chỉ được chuộc đồ tại đúng cửa hàng đã cầm. | Quy tắc nghiệp vụ | "Khách chuộc đồ tại đúng cửa hàng đã cầm" (yeu-cau-cam-do.md, Mục 5, câu 1) | Không có |
| REQ-52 | Khi chuộc đồ, khách phải trả đủ tiền gốc, lãi tính đến ngày chuộc và phí trễ hạn nếu có. | Quy tắc nghiệp vụ | "trả đủ gốc, lãi tính đến ngày chuộc và phí trễ hạn nếu có" (yeu-cau-cam-do.md, Mục 5, câu 1) | Không có |
| REQ-53 | Khi chuộc trước hạn, lãi được tính tối thiểu 10 ngày. | Quy tắc nghiệp vụ | "chuộc trước hạn vẫn tính lãi tối thiểu 10 ngày" (yeu-cau-cam-do.md, Mục 5, câu 1) | Không có |
| REQ-54 | Người chuộc phải là chủ hợp đồng hoặc người được chủ hợp đồng uỷ quyền bằng giấy uỷ quyền có công chứng. | Quy tắc nghiệp vụ | "Người chuộc phải là chủ hợp đồng hoặc người được chủ hợp đồng uỷ quyền bằng giấy uỷ quyền có công chứng" (yeu-cau-cam-do.md, Mục 5, câu 2) | Q-17 |
| REQ-55 | Nhân viên giao dịch có thể đọc thẻ căn cước của người chuộc bằng đầu đọc căn cước. | Chức năng | "nhân viên giao dịch đọc thẻ căn cước của người chuộc bằng đầu đọc" (yeu-cau-cam-do.md, Mục 5, câu 2) | Kênh: đầu đọc căn cước (REQ-06) |
| REQ-56 | Thủ quỹ có thể thu tiền chuộc đồ của khách. | Chức năng | "Thủ quỹ thu tiền" (yeu-cau-cam-do.md, Mục 5, câu 3) | Không có |
| REQ-57 | Nhân viên giao dịch có thể quét mã vạch trên nhãn tài sản để lấy tài sản ra khỏi két. | Chức năng | "nhân viên giao dịch quét mã vạch trên nhãn để lấy tài sản ra khỏi két" (yeu-cau-cam-do.md, Mục 5, câu 3) | Kênh: máy quét mã vạch (REQ-58) |
| REQ-58 | Hệ thống trao đổi dữ liệu mã vạch với máy quét mã vạch tại quầy để đọc mã trên nhãn tài sản. | Giao tiếp ngoài | "quét mã vạch trên nhãn" (yeu-cau-cam-do.md, Mục 5, câu 3)<br>"Tra cứu hợp đồng tại quầy bằng mã vạch" (yeu-cau-cam-do.md, Mục 10, câu 4)<br>project-profile.md, HE_THONG_NGOAI | Tách từ cùng câu với REQ-57 |
| REQ-59 | Khách kiểm tra tài sản khi nhận lại tài sản đã chuộc. | Quy tắc nghiệp vụ | "khách kiểm tra tài sản" (yeu-cau-cam-do.md, Mục 5, câu 3) | Không có |
| REQ-60 | Khách ký biên nhận khi nhận lại tài sản đã chuộc. | Quy tắc nghiệp vụ | "ký biên nhận" (yeu-cau-cam-do.md, Mục 5, câu 3) | Tách từ cùng câu với REQ-59. Q-04 |
| REQ-61 | Nhân viên giao dịch có thể in biên nhận chuộc đồ để khách ký. | Chức năng | Giả định ASM-04 | Phục vụ REQ-60. Q-04 |
| REQ-62 | Hệ thống gửi tin nhắc cho khách có hợp đồng đạt ngưỡng nhắc trước hạn ở REQ-64 lúc 9 giờ sáng mỗi ngày. | Chức năng | "Lúc 9 giờ sáng mỗi ngày, hệ thống gửi tin nhắc cho khách có hợp đồng đến hạn sau 3 ngày" (yeu-cau-cam-do.md, Mục 6, câu 1) | Kênh: cổng SMS (REQ-90), thay bằng thông báo đẩy theo REQ-98 |
| REQ-63 | Hệ thống gửi tin nhắc cho khách có hợp đồng đạt ngưỡng nhắc quá hạn ở REQ-65 lúc 9 giờ sáng mỗi ngày. | Chức năng | "khách có hợp đồng đã quá hạn đúng 7 ngày" (yeu-cau-cam-do.md, Mục 6, câu 1) | Tách từ cùng câu với REQ-62. Kênh như REQ-62 |
| REQ-64 | Ngưỡng nhắc trước hạn là hợp đồng đến hạn sau 3 ngày. | Quy tắc nghiệp vụ | "hợp đồng đến hạn sau 3 ngày" (yeu-cau-cam-do.md, Mục 6, câu 1) | Tách từ cùng câu với REQ-62 |
| REQ-65 | Ngưỡng nhắc quá hạn là hợp đồng đã quá hạn đúng 7 ngày. | Quy tắc nghiệp vụ | "hợp đồng đã quá hạn đúng 7 ngày" (yeu-cau-cam-do.md, Mục 6, câu 1) | Tách từ cùng câu với REQ-63 |
| REQ-66 | Hệ thống chuyển hợp đồng quá hạn đạt ngưỡng ở REQ-67 mà khách chưa đóng lãi hay chuộc sang trạng thái chờ thanh lý lúc 0 giờ mỗi ngày. | Chức năng | "Lúc 0 giờ mỗi ngày, hợp đồng quá hạn 15 ngày mà khách chưa đóng lãi hay chuộc thì hệ thống chuyển sang trạng thái chờ thanh lý" (yeu-cau-cam-do.md, Mục 6, câu 2) | Q-11 |
| REQ-67 | Ngưỡng chuyển sang trạng thái chờ thanh lý là hợp đồng quá hạn 15 ngày. | Quy tắc nghiệp vụ | "hợp đồng quá hạn 15 ngày" (yeu-cau-cam-do.md, Mục 6, câu 2) | Tách từ cùng câu với REQ-66 |
| REQ-68 | Hệ thống báo cho quản lý cửa hàng khi hợp đồng chuyển sang trạng thái chờ thanh lý. | Chức năng | "và báo cho quản lý cửa hàng" (yeu-cau-cam-do.md, Mục 6, câu 2) | Q-22 |
| REQ-69 | Quản lý cửa hàng có thể quyết định thanh lý tài sản của hợp đồng chờ thanh lý bằng cách bán tài sản tại quầy cho người mua. | Chức năng | "Quản lý cửa hàng quyết định thanh lý: bán tài sản tại quầy cho người mua" (yeu-cau-cam-do.md, Mục 6, câu 3) | Không có |
| REQ-70 | Quản lý cửa hàng có thể nhập số tiền bán được khi bán tài sản tại quầy. | Chức năng | Giả định ASM-07 | Phục vụ REQ-69. Q-07 |
| REQ-71 | Hệ thống tính tiền thừa phải trả lại khách từ số tiền bán tài sản tại quầy. | Chức năng | Giả định ASM-07 | Phục vụ REQ-69, cùng cách tính với REQ-103. Q-07 |
| REQ-72 | Quản lý cửa hàng có thể quyết định thanh lý tài sản của hợp đồng chờ thanh lý bằng cách chuyển tài sản về bộ phận thanh lý của chuỗi. | Chức năng | "hoặc chuyển tài sản về bộ phận thanh lý của chuỗi" (yeu-cau-cam-do.md, Mục 6, câu 3) | Tách từ cùng câu với REQ-69 |
| REQ-73 | Tiền bán tài sản vượt quá gốc, lãi và phí thì cửa hàng phải trả lại phần vượt cho khách trong vòng 30 ngày kể từ ngày bán. | Quy tắc nghiệp vụ | "Tiền bán vượt quá gốc, lãi và phí thì cửa hàng phải trả lại cho khách trong vòng 30 ngày kể từ ngày bán." (yeu-cau-cam-do.md, Mục 6, câu 4) | Q-30 |
| REQ-74 | Thủ quỹ có thể ghi nhận việc trả lại tiền thừa cho khách. | Chức năng | Giả định ASM-08 | Phục vụ REQ-73. Q-08 |
| REQ-75 | Khách có thể đăng ký trên ứng dụng di động bằng số điện thoại đã khai trong hợp đồng. | Chức năng | "Khách tải ứng dụng di động và đăng ký bằng số điện thoại đã khai trong hợp đồng" (yeu-cau-cam-do.md, Mục 7, câu 1) | Không có |
| REQ-76 | Hợp đồng cầm đồ ghi số điện thoại do khách khai. | Dữ liệu | "số điện thoại đã khai trong hợp đồng" (yeu-cau-cam-do.md, Mục 7, câu 1) | Tách từ cùng câu với REQ-75 |
| REQ-77 | Hệ thống gửi mã OTP qua SMS để khách xác nhận đăng ký. | Chức năng | "hệ thống gửi mã OTP qua SMS để xác nhận" (yeu-cau-cam-do.md, Mục 7, câu 1) | Kênh: cổng SMS (REQ-90). Q-28 |
| REQ-78 | Khách có thể xem các hợp đồng đang có của mình trên ứng dụng di động. | Chức năng | "Trên ứng dụng, khách xem các hợp đồng đang có" (yeu-cau-cam-do.md, Mục 7, câu 2) | Không có |
| REQ-79 | Khách có thể xem lịch sử đóng lãi trên ứng dụng di động. | Chức năng | "lịch sử đóng lãi" (yeu-cau-cam-do.md, Mục 7, câu 2) | Tách từ cùng câu với REQ-78 |
| REQ-80 | Khách có thể xem số tiền phải trả nếu chuộc trong ngày trên ứng dụng di động. | Chức năng | "số tiền phải trả nếu chuộc trong ngày" (yeu-cau-cam-do.md, Mục 7, câu 2) | Tách từ cùng câu với REQ-78 |
| REQ-81 | Quản lý chuỗi có thể đặt tỉ lệ cho vay theo loại tài sản. | Chức năng | "Quản lý chuỗi đặt lãi suất và tỉ lệ cho vay theo loại tài sản" (yeu-cau-cam-do.md, Mục 9, câu 1) | Q-10 |
| REQ-82 | Quản lý chuỗi có thể xem báo cáo dư nợ theo cửa hàng. | Chức năng | "xem báo cáo dư nợ theo cửa hàng" (yeu-cau-cam-do.md, Mục 9, câu 1) | Không có |
| REQ-83 | Quản lý chuỗi có thể xem báo cáo tỉ lệ hợp đồng quá hạn. | Chức năng | "tỉ lệ hợp đồng quá hạn" (yeu-cau-cam-do.md, Mục 9, câu 1) | Q-34 |
| REQ-84 | Quản lý chuỗi có thể xem báo cáo doanh thu lãi theo tháng. | Chức năng | "doanh thu lãi theo tháng" (yeu-cau-cam-do.md, Mục 9, câu 1) | Q-34 |
| REQ-85 | Kiểm toán viên nội bộ có thể xem mọi hợp đồng. | Chức năng | "Kiểm toán viên nội bộ xem được mọi hợp đồng" (yeu-cau-cam-do.md, Mục 9, câu 2) | Q-33 |
| REQ-86 | Kiểm toán viên nội bộ có thể xem nhật ký thao tác. | Chức năng | "và nhật ký thao tác" (yeu-cau-cam-do.md, Mục 9, câu 2) | Tách từ cùng câu với REQ-85. Q-32 |
| REQ-87 | Kiểm toán viên nội bộ không sửa được dữ liệu nào trong hệ thống. | Quy tắc nghiệp vụ | "nhưng không sửa được gì" (yeu-cau-cam-do.md, Mục 9, câu 2) | Tách từ cùng câu với REQ-85 |
| REQ-88 | Hệ thống ghi nhật ký mọi thay đổi trên hợp đồng về số tiền, kỳ hạn và trạng thái. | Chức năng | "Mọi thay đổi trên hợp đồng (số tiền, kỳ hạn, trạng thái) phải được ghi nhật ký" (yeu-cau-cam-do.md, Mục 9, câu 3) | Q-32 |
| REQ-89 | Mỗi bản ghi nhật ký thay đổi hợp đồng gồm người thực hiện, thời điểm, giá trị cũ và giá trị mới. | Dữ liệu | "gồm người thực hiện, thời điểm, giá trị cũ và giá trị mới" (yeu-cau-cam-do.md, Mục 9, câu 3) | Tách từ cùng câu với REQ-88 |
| REQ-90 | Hệ thống trao đổi tin nhắn gửi khách với cổng SMS của nhà mạng để gửi tin nhắn và mã OTP cho khách. | Giao tiếp ngoài | "Tin nhắn cho khách gửi qua cổng SMS của nhà mạng." (yeu-cau-cam-do.md, Mục 10, câu 1)<br>project-profile.md, HE_THONG_NGOAI | HE_THONG_NGOAI: API REST |
| REQ-91 | Số căn cước và ảnh thẻ căn cước của khách được mã hoá khi lưu trữ. | Phi chức năng | "Số căn cước và ảnh thẻ căn cước của khách phải được mã hoá khi lưu trữ." (yeu-cau-cam-do.md, Mục 10, câu 2) | Q-06 |
| REQ-92 | Nhân viên giao dịch có thể chụp ảnh thẻ căn cước của khách khi tạo hồ sơ khách mới. | Chức năng | Giả định ASM-06 | Phục vụ REQ-91. Q-06 |
| REQ-93 | Hệ thống lưu ảnh tài sản ít nhất 5 năm sau khi hợp đồng kết thúc. | Dữ liệu | "Ảnh tài sản lưu ít nhất 5 năm sau khi hợp đồng kết thúc." (yeu-cau-cam-do.md, Mục 10, câu 3) | Q-29 |
| REQ-94 | Nhân viên tại quầy có thể tra cứu hợp đồng bằng mã vạch. | Chức năng | "Tra cứu hợp đồng tại quầy bằng mã vạch" (yeu-cau-cam-do.md, Mục 10, câu 4) | Kênh: máy quét mã vạch (REQ-58). Q-31 |
| REQ-95 | Tra cứu hợp đồng tại quầy bằng mã vạch trả kết quả trong vòng 2 giây, kể cả giờ cao điểm từ 11 giờ đến 13 giờ. | Phi chức năng | "phải trả kết quả trong vòng 2 giây, kể cả giờ cao điểm từ 11 giờ đến 13 giờ" (yeu-cau-cam-do.md, Mục 10, câu 4) | Tách từ cùng câu với REQ-94 |
| REQ-96 | Một nhân viên có thể đồng thời là nhân viên giao dịch và nhân viên định giá ở cửa hàng nhỏ. | Quy tắc nghiệp vụ | "Ở cửa hàng nhỏ, một nhân viên có thể vừa làm nhân viên giao dịch vừa làm nhân viên định giá" (bien-ban-hop-bo-sung.md, mục 1) | Q-26 |
| REQ-97 | Nhân viên định giá không được duyệt khoản vay của hợp đồng do chính người đó định giá. | Quy tắc nghiệp vụ | "người định giá không được tự duyệt khoản vay của chính hợp đồng mình định giá" (bien-ban-hop-bo-sung.md, mục 1) | Bổ sung cho REQ-19, REQ-20 |
| REQ-98 | Hệ thống gửi tin nhắc qua thông báo đẩy của ứng dụng di động thay cho SMS cho khách đã cài ứng dụng. | Chức năng | "Khách đã cài ứng dụng di động thì nhận tin nhắc qua thông báo đẩy của ứng dụng thay cho SMS" (bien-ban-hop-bo-sung.md, mục 2) | Tin nhắc là tin ở REQ-62, REQ-63; mã OTP vẫn qua SMS. Kênh: REQ-99. Q-27, Q-16 |
| REQ-99 | Hệ thống trao đổi nội dung tin nhắc với dịch vụ thông báo đẩy của nền tảng di động để gửi tin nhắc tới ứng dụng di động của khách. | Giao tiếp ngoài | "thông báo đẩy của ứng dụng" (bien-ban-hop-bo-sung.md, mục 2)<br>project-profile.md, HE_THONG_NGOAI | Tách từ cùng câu với REQ-98 |
| REQ-100 | Phí trễ hạn chỉ tính một lần cho mỗi kỳ hạn, không cộng dồn theo ngày. | Quy tắc nghiệp vụ | "Phí trễ hạn chỉ tính một lần cho mỗi kỳ hạn, không cộng dồn theo ngày." (bien-ban-hop-bo-sung.md, mục 3) | Làm rõ REQ-48, REQ-49 (không mâu thuẫn) |
| REQ-101 | Mỗi hợp đồng cầm đồ được gia hạn tối đa 12 lần. | Quy tắc nghiệp vụ | "Quản lý cửa hàng đề nghị cho gia hạn tối đa 12 lần để giữ khách quen." (bien-ban-hop-bo-sung.md, mục 4) | Mâu thuẫn với REQ-44. Nguồn dùng "đề nghị", chưa rõ đã chốt. Q-09 |
| REQ-102 | Kế toán chuỗi có thể nhập vào phần mềm số tiền bán được của tài sản bán ở bộ phận thanh lý của chuỗi. | Chức năng | "kế toán chuỗi nhập vào phần mềm số tiền bán được" (bien-ban-hop-bo-sung.md, mục 5) | Việc bán ở bộ phận thanh lý là Ngoài phạm vi |
| REQ-103 | Hệ thống tính tiền thừa phải trả lại khách từ số tiền bán được do kế toán chuỗi nhập. | Chức năng | "để phần mềm tính tiền thừa phải trả lại khách" (bien-ban-hop-bo-sung.md, mục 5) | Tách từ cùng câu với REQ-102. Q-30 |
| REQ-104 | Cửa hàng không nhận cầm xe máy khi hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an không phản hồi, cho tới khi tra cứu được. | Quy tắc nghiệp vụ | "Khi hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an không phản hồi, cửa hàng không nhận cầm xe máy cho tới khi tra cứu được." (bien-ban-hop-bo-sung.md, mục 6) | Q-20 |
| REQ-105 | Hệ thống trao đổi dữ liệu nhãn với máy in nhãn mã vạch tại quầy để in nhãn mã vạch dán lên tài sản cầm cố. | Giao tiếp ngoài | project-profile.md, HE_THONG_NGOAI | Chỉ có nguồn là HE_THONG_NGOAI nên xếp sau mọi REQ lấy từ tài liệu nguồn. Mục đích suy từ tên thiết bị và REQ-36. ASM-03 |

## 5. Vấn đề chất lượng của tài liệu nguồn

| STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
|---|---|---|---|---|---|
| 1 | Mâu thuẫn | REQ-44, REQ-101 | yeu-cau-cam-do.md Mục 4: "một hợp đồng được gia hạn tối đa 6 lần"; bien-ban-hop-bo-sung.md mục 4: "Quản lý cửa hàng đề nghị cho gia hạn tối đa 12 lần để giữ khách quen" | Ghi cả hai. Tài liệu ưu tiên cao hơn theo thứ tự TAI_LIEU_NGUON là yeu-cau-cam-do.md (6 lần). Hỏi người có thẩm quyền | Q-09 |
| 2 | Mâu thuẫn | REQ-17, REQ-18, REQ-81 | Mục 2: "Số tiền cho vay tối đa bằng 80% giá định giá với vàng nữ trang và 60% với các loại tài sản khác"; Mục 9: "Quản lý chuỗi đặt lãi suất và tỉ lệ cho vay theo loại tài sản" | Giữ 80%, 60% đúng nguồn; hỏi đây là giá trị cố định hay giá trị ban đầu quản lý chuỗi được đổi | Q-10 |
| 3 | Mâu thuẫn | REQ-12, REQ-22, REQ-23 | Mục 2: "ghi đặc điểm (hãng, model, số IMEI hoặc số khung, tình trạng)"; "phần mềm gửi số khung, số máy sang hệ thống tra cứu" | Đặc điểm không có số máy nhưng bước tra cứu cần số máy. Giữ REQ-12 đúng nguồn, bổ sung REQ-23 theo giả định | Q-05, ASM-05 |
| 4 | Thiếu | REQ-33, REQ-34, REQ-35 | Mục 3: "Nhân viên giao dịch in hợp đồng để khách ký" (nguồn không nói ai lập hợp đồng, ai nhập số tiền cho vay) | Giả định ai lập hợp đồng, chờ xác nhận | Q-01, ASM-01 |
| 5 | Thiếu | REQ-30, REQ-31 | Mục 3: "chuyển khoản vào tài khoản ngân hàng của khách" (nguồn không nói ai nhập thông tin tài khoản) | Giả định thủ quỹ nhập, chờ xác nhận | Q-02, ASM-02 |
| 6 | Mơ hồ | REQ-36, REQ-37, REQ-105 | Mục 3: "tài sản được dán nhãn mã vạch theo mã hợp đồng" (câu bị động, không nói ai tạo nhãn) | Giả định nhân viên giao dịch in nhãn bằng máy in nhãn ở HE_THONG_NGOAI | Q-03, ASM-03 |
| 7 | Thiếu | REQ-60, REQ-61 | Mục 5: "khách kiểm tra tài sản và ký biên nhận" (không nói ai lập, in biên nhận) | Giả định nhân viên giao dịch in biên nhận | Q-04, ASM-04 |
| 8 | Thiếu | REQ-91, REQ-92 | Mục 10: "Số căn cước và ảnh thẻ căn cước của khách phải được mã hoá khi lưu trữ" (không nói ảnh thẻ do ai tạo, lấy từ đâu) | Giả định nhân viên giao dịch chụp ảnh thẻ khi tạo hồ sơ khách mới | Q-06, ASM-06 |
| 9 | Thiếu | REQ-69, REQ-70, REQ-71 | Mục 6: "bán tài sản tại quầy cho người mua"; biên bản mục 5 chỉ nêu việc nhập số tiền bán cho nhánh bộ phận thanh lý | Quy tắc nêu cho một nhánh; giả định nhánh bán tại quầy cũng có nhập số tiền bán và tính tiền thừa | Q-07, ASM-07 |
| 10 | Thiếu | REQ-73, REQ-74 | Mục 6: "cửa hàng phải trả lại cho khách trong vòng 30 ngày" (không nói ai thực hiện, ghi nhận) | Giả định thủ quỹ ghi nhận việc trả | Q-08, ASM-08 |
| 11 | Thiếu | REQ-73, REQ-103 | Mục 6: "Tiền bán vượt quá gốc, lãi và phí" (không nói lãi, phí tính đến ngày nào) | Hỏi mốc tính | Q-30 |
| 12 | Thiếu | REQ-66, REQ-39, REQ-50 | Mục 6: "chuyển sang trạng thái chờ thanh lý" (không nói trong trạng thái này khách còn đóng lãi hoặc chuộc được không) | Hỏi người có thẩm quyền | Q-11 |
| 13 | Thiếu | REQ-19, REQ-20 | Mục 2: "phải được quản lý cửa hàng duyệt" (không nói trường hợp quản lý không duyệt) | Hỏi | Q-12 |
| 14 | Mơ hồ | REQ-14, REQ-15 | Mục 2: "bảng giá thị trường"; Mục 9: "cập nhật bảng giá tham khảo" | Hai tên có thể chỉ cùng một bảng; gộp thành một REQ, hỏi xác nhận | Q-13 |
| 15 | Thiếu | REQ-30, REQ-32 | Mục 3: "qua cổng chi hộ của ngân hàng đối tác" (không nói khi lệnh chi thất bại) | Hỏi | Q-14 |
| 16 | Thiếu | REQ-42, REQ-46 | Mục 4: "Giao dịch thanh toán trực tuyến chưa thành công trong 10 phút thì bị huỷ" (không nói khách có được báo, hợp đồng ra sao) | Hỏi | Q-15 |
| 17 | Mơ hồ | REQ-47 | Mục 4: "chưa thành công trong 10 phút" (không nói mốc bắt đầu tính) | Hỏi mốc | Q-25 |
| 18 | Thiếu | REQ-98 | biên bản mục 2: "nhận tin nhắc qua thông báo đẩy ... thay cho SMS" (không nói khi gửi thông báo đẩy thất bại) | Hỏi | Q-16 |
| 19 | Mơ hồ | REQ-98 | biên bản mục 2: "Khách đã cài ứng dụng di động" | Hỏi điều kiện xác định "đã cài" | Q-27 |
| 20 | Mơ hồ | REQ-96 | biên bản mục 1: "Ở cửa hàng nhỏ" ("nhỏ" thuộc nhóm mức độ không định lượng F6) | Giữ nguyên từ, hỏi tiêu chí | Q-26 |
| 21 | Mơ hồ | REQ-27 | Mục 3: "lãi tính theo ngày trên số tiền gốc còn nợ, với lãi suất do quản lý chuỗi đặt" (không nói đơn vị lãi suất) | Hỏi đơn vị | Q-24 |
| 22 | Thiếu | REQ-07, REQ-08 | Mục 1: "khách mới thì phần mềm tạo hồ sơ khách, khách cũ thì mở hồ sơ đã có" (không nói nhận biết khách cũ bằng gì) | Hỏi | Q-19 |
| 23 | Mơ hồ | REQ-04, REQ-18 | Mục 1: "(điện thoại, máy tính xách tay, xe máy, vàng nữ trang)"; Mục 2: "các loại tài sản khác" | Không rõ danh sách loại tài sản là đóng hay mở | Q-35 |
| 24 | Thiếu | REQ-21 | Mục 2: "Xe máy phải có giấy đăng ký xe đứng tên khách" (không nói phần mềm ghi nhận giấy này thế nào) | Giữ REQ dạng quy tắc, hỏi | Q-18 |
| 25 | Thiếu | REQ-54 | Mục 5: "bằng giấy uỷ quyền có công chứng" (không nói giấy uỷ quyền có được ghi nhận vào phần mềm không) | Hỏi | Q-17 |
| 26 | Không kiểm chứng được | REQ-104 | biên bản mục 6: "không phản hồi" (không nêu ngưỡng thời gian) | Giữ nguyên từ, hỏi ngưỡng | Q-20 |
| 27 | Thiếu | REQ-24 | project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" | Hỏi nguồn tài liệu API | Q-21 |
| 28 | Thiếu | REQ-68 | Mục 6: "và báo cho quản lý cửa hàng" (không nói kênh báo) | Hỏi kênh | Q-22 |
| 29 | Thiếu | REQ-38 | Mục 3: "rồi cất vào két của cửa hàng" (câu bị động, không nói phần mềm có ghi nhận việc cất không) | Hỏi | Q-23 |
| 30 | Không kiểm chứng được | REQ-77 | Mục 7: "hệ thống gửi mã OTP qua SMS để xác nhận" (không nói thời hạn hiệu lực của OTP) | Hỏi | Q-28 |
| 31 | Mơ hồ | REQ-93 | Mục 10: "sau khi hợp đồng kết thúc" (không nói thời điểm kết thúc) | Hỏi | Q-29 |
| 32 | Mơ hồ | REQ-94 | Mục 10: "Tra cứu hợp đồng tại quầy bằng mã vạch" (không nói ai tra cứu) | Dùng "Nhân viên tại quầy", hỏi vai trò | Q-31 |
| 33 | Mơ hồ | REQ-85 | Mục 9: "xem được mọi hợp đồng" (từ tổng thể tuyệt đối F6) | Giữ nguyên "mọi", hỏi có giới hạn nào không | Q-33 |
| 34 | Mơ hồ | REQ-86, REQ-88 | Mục 9: "nhật ký thao tác" và "Mọi thay đổi trên hợp đồng ... phải được ghi nhật ký" (không rõ hai nhật ký có cùng phạm vi; "mọi" là từ F6) | Giữ nguyên, hỏi phạm vi | Q-32 |
| 35 | Mơ hồ | REQ-83, REQ-84 | Mục 9: "tỉ lệ hợp đồng quá hạn, doanh thu lãi theo tháng" (không rõ "theo cửa hàng" có áp dụng cho hai báo cáo này) | Hỏi | Q-34 |
| 36 | Trùng lặp | REQ-42 | Mục 4: "trên ứng dụng di động ... đóng lãi"; Mục 7: "đóng lãi trực tuyến" | Cùng chức năng, gộp vào REQ-42, không tạo Q | Không có |
| 37 | Trùng lặp | REQ-28 | Mục 3: "lãi suất do quản lý chuỗi đặt cho từng loại tài sản"; Mục 9: "Quản lý chuỗi đặt lãi suất ... theo loại tài sản" | Cùng chức năng, gộp vào REQ-28, không tạo Q | Không có |
| 38 | Trùng lặp | REQ-15 | Mục 2: "bảng giá thị trường do quản lý chuỗi cập nhật"; Mục 9: "cập nhật bảng giá tham khảo" | Gộp vào REQ-15 (xem dòng 14) | Q-13 |
| 39 | Mâu thuẫn (hoà giải được) | REQ-48, REQ-49, REQ-100 | Mục 4: "chịu phí trễ hạn bằng 1% tiền gốc còn nợ"; biên bản mục 3: "chỉ tính một lần cho mỗi kỳ hạn, không cộng dồn theo ngày" | Không mâu thuẫn, biên bản làm rõ cách tính; giữ ba REQ | Không có |
| 40 | Mâu thuẫn (hoà giải được) | REQ-62, REQ-63, REQ-90, REQ-98 | Mục 6 và Mục 10: tin nhắn gửi qua cổng SMS; biên bản mục 2: khách đã cài ứng dụng nhận qua thông báo đẩy | Không mâu thuẫn, tách theo điều kiện khách đã cài ứng dụng | Không có |
| 41 | Mâu thuẫn (hoà giải được) | REQ-72, REQ-102 | Mục 6: "chuyển tài sản về bộ phận thanh lý của chuỗi"; biên bản mục 5: "Việc bán tài sản ở bộ phận thanh lý của chuỗi làm ngoài phần mềm" | Không mâu thuẫn, biên bản xác định phần bán nằm ngoài phần mềm | Không có |

## 6. Ma trận phủ nguồn

| Vị trí trong nguồn | Tóm tắt nội dung | Kết luận (REQ-xx / Ngoài phạm vi / Bối cảnh) |
|---|---|---|
| yeu-cau-cam-do.md, đoạn mở đầu, câu 1 | 6 cửa hàng, khoảng 400 hợp đồng mới và 600 lượt đóng lãi hoặc chuộc đồ mỗi ngày | REQ-01, REQ-02, REQ-03 |
| yeu-cau-cam-do.md, đoạn mở đầu, câu 2 | Hợp đồng viết tay hai liên, theo dõi hạn bằng bảng tính, khách phải tới quầy, để quá hạn không báo | Bối cảnh |
| yeu-cau-cam-do.md, đoạn mở đầu, câu 3 | Phúc An cần phần mềm quản lý hợp đồng, tài sản cầm cố và tiền mặt tại quầy | Bối cảnh (mục 1 của artifact); phần chốt ca và định mức két là Ngoài phạm vi (Mục 8) |
| yeu-cau-cam-do.md, Mục 1, câu 1 | Khách mang tài sản bốn loại và thẻ căn cước | REQ-04 |
| yeu-cau-cam-do.md, Mục 1, câu 2 (đọc thẻ) | Đặt thẻ lên đầu đọc để lấy họ tên, số căn cước, ngày sinh, địa chỉ | REQ-05, REQ-06 |
| yeu-cau-cam-do.md, Mục 1, câu 2 (khách mới) | Khách mới thì tạo hồ sơ khách | REQ-07 |
| yeu-cau-cam-do.md, Mục 1, câu 2 (khách cũ) | Khách cũ thì mở hồ sơ đã có | REQ-08 |
| yeu-cau-cam-do.md, Mục 1, câu 3 | Khách dưới 18 tuổi không được cầm đồ | REQ-09 |
| yeu-cau-cam-do.md, Mục 2, câu 1 (kiểm tra) | Nhân viên định giá kiểm tra tài sản | Bối cảnh (thao tác thủ công, không có hành vi phần mềm riêng) |
| yeu-cau-cam-do.md, Mục 2, câu 1 (chụp ảnh, ghi đặc điểm, nhập giá) | Chụp ảnh, ghi đặc điểm, nhập giá định giá | REQ-10, REQ-11, REQ-12, REQ-13, REQ-23 |
| yeu-cau-cam-do.md, Mục 2, câu 2 | Gợi ý giá tham khảo theo bảng giá thị trường quản lý chuỗi cập nhật hằng tuần | REQ-14, REQ-15, REQ-16 |
| yeu-cau-cam-do.md, Mục 2, câu 3 | Cho vay tối đa 80% vàng nữ trang, 60% loại khác | REQ-17, REQ-18 |
| yeu-cau-cam-do.md, Mục 2, câu 4 | Khoản vay từ 5 triệu đồng phải quản lý cửa hàng duyệt | REQ-19, REQ-20 |
| yeu-cau-cam-do.md, Mục 2, câu 5 | Xe máy cần giấy đăng ký đứng tên khách; tra cứu mất cắp trước giải ngân | REQ-21, REQ-22, REQ-23, REQ-24, REQ-25 |
| yeu-cau-cam-do.md, Mục 3, câu 1 | Kỳ hạn 30 ngày, lãi theo ngày trên gốc còn nợ, lãi suất do quản lý chuỗi đặt | REQ-26, REQ-27, REQ-28 |
| yeu-cau-cam-do.md, Mục 3, câu 2 | Thủ quỹ giải ngân tiền mặt hoặc chuyển khoản qua cổng chi hộ | REQ-29, REQ-30, REQ-31, REQ-32 |
| yeu-cau-cam-do.md, Mục 3, câu 3 | In hợp đồng để khách ký; dán nhãn mã vạch; cất vào két | REQ-33, REQ-34, REQ-35, REQ-36, REQ-37, REQ-38 |
| yeu-cau-cam-do.md, Mục 4, câu 1 | Đóng lãi gia hạn 30 ngày tại quầy hoặc trên ứng dụng; tối đa 6 lần | REQ-39, REQ-40, REQ-41, REQ-42, REQ-43, REQ-44 |
| yeu-cau-cam-do.md, Mục 4, câu 2 | Trả bớt một phần gốc khi đóng lãi tại quầy | REQ-45 |
| yeu-cau-cam-do.md, Mục 4, câu 3 | Giao dịch trực tuyến chưa thành công trong 10 phút thì huỷ | REQ-46, REQ-47 |
| yeu-cau-cam-do.md, Mục 4, câu 4 | Đóng lãi sau hạn quá 3 ngày chịu phí trễ hạn 1% gốc còn nợ | REQ-48, REQ-49 |
| yeu-cau-cam-do.md, Mục 5, câu 1 | Chuộc đúng cửa hàng, trả đủ gốc, lãi, phí; lãi tối thiểu 10 ngày khi chuộc trước hạn | REQ-50, REQ-51, REQ-52, REQ-53 |
| yeu-cau-cam-do.md, Mục 5, câu 2 | Người chuộc là chủ hợp đồng hoặc người được uỷ quyền; đọc thẻ căn cước | REQ-54, REQ-55 |
| yeu-cau-cam-do.md, Mục 5, câu 3 | Thủ quỹ thu tiền, quét mã vạch lấy tài sản, khách kiểm tra và ký biên nhận | REQ-56, REQ-57, REQ-58, REQ-59, REQ-60, REQ-61 |
| yeu-cau-cam-do.md, Mục 6, câu 1 | 9 giờ sáng gửi tin nhắc trước hạn 3 ngày và quá hạn đúng 7 ngày | REQ-62, REQ-63, REQ-64, REQ-65 |
| yeu-cau-cam-do.md, Mục 6, câu 2 | 0 giờ chuyển chờ thanh lý khi quá hạn 15 ngày, báo quản lý cửa hàng | REQ-66, REQ-67, REQ-68 |
| yeu-cau-cam-do.md, Mục 6, câu 3 | Quản lý cửa hàng quyết định thanh lý: bán tại quầy hoặc chuyển về bộ phận thanh lý | REQ-69, REQ-70, REQ-71, REQ-72 |
| yeu-cau-cam-do.md, Mục 6, câu 4 | Tiền bán vượt gốc, lãi, phí trả lại khách trong 30 ngày | REQ-73, REQ-74 |
| yeu-cau-cam-do.md, Mục 7, câu 1 | Đăng ký ứng dụng bằng số điện thoại trong hợp đồng, OTP qua SMS | REQ-75, REQ-76, REQ-77 |
| yeu-cau-cam-do.md, Mục 7, câu 2 | Xem hợp đồng, lịch sử đóng lãi, số tiền chuộc trong ngày, đóng lãi trực tuyến | REQ-78, REQ-79, REQ-80, REQ-42 |
| yeu-cau-cam-do.md, Mục 7, câu 3 | Khách không chuộc đồ qua ứng dụng | Ngoài phạm vi |
| yeu-cau-cam-do.md, Mục 8, câu 1 | Kiểm đếm tiền mặt, chốt ca, xác nhận chênh lệch từ 200.000 đồng | Ngoài phạm vi (Ngoài trọng tâm phân tích) |
| yeu-cau-cam-do.md, Mục 8, câu 2 | Tiền mặt trong két không vượt 500 triệu đồng, cảnh báo quản lý cửa hàng | Ngoài phạm vi (Ngoài trọng tâm phân tích) |
| yeu-cau-cam-do.md, Mục 9, câu 1 | Quản lý chuỗi đặt lãi suất, tỉ lệ cho vay, cập nhật bảng giá, xem ba báo cáo | REQ-28, REQ-81, REQ-15, REQ-82, REQ-83, REQ-84 |
| yeu-cau-cam-do.md, Mục 9, câu 2 | Kiểm toán viên xem mọi hợp đồng và nhật ký, không sửa được | REQ-85, REQ-86, REQ-87 |
| yeu-cau-cam-do.md, Mục 9, câu 3 | Ghi nhật ký mọi thay đổi trên hợp đồng, gồm người, thời điểm, giá trị cũ và mới | REQ-88, REQ-89 |
| yeu-cau-cam-do.md, Mục 10, câu 1 | Tin nhắn qua cổng SMS của nhà mạng | REQ-90 |
| yeu-cau-cam-do.md, Mục 10, câu 2 | Mã hoá số căn cước và ảnh thẻ căn cước khi lưu | REQ-91, REQ-92 |
| yeu-cau-cam-do.md, Mục 10, câu 3 | Lưu ảnh tài sản ít nhất 5 năm sau khi hợp đồng kết thúc | REQ-93 |
| yeu-cau-cam-do.md, Mục 10, câu 4 | Tra cứu bằng mã vạch trong 2 giây, kể cả giờ cao điểm | REQ-94, REQ-95, REQ-58 |
| bien-ban-hop-bo-sung.md, mục 1 | Một nhân viên kiêm hai vai trò; người định giá không tự duyệt | REQ-96, REQ-97 |
| bien-ban-hop-bo-sung.md, mục 2 | Khách đã cài ứng dụng nhận tin nhắc qua thông báo đẩy; OTP vẫn qua SMS | REQ-98, REQ-99 |
| bien-ban-hop-bo-sung.md, mục 3 | Phí trễ hạn tính một lần mỗi kỳ hạn | REQ-100 |
| bien-ban-hop-bo-sung.md, mục 4 | Đề nghị gia hạn tối đa 12 lần | REQ-101 |
| bien-ban-hop-bo-sung.md, mục 5 (bán ở bộ phận thanh lý) | Việc bán ở bộ phận thanh lý làm ngoài phần mềm | Ngoài phạm vi |
| bien-ban-hop-bo-sung.md, mục 5 (kế toán nhập) | Kế toán chuỗi nhập số tiền bán được, phần mềm tính tiền thừa | REQ-102, REQ-103 |
| bien-ban-hop-bo-sung.md, mục 6 | Cơ quan công an không phản hồi thì không nhận cầm xe máy | REQ-104 |
| bien-ban-hop-bo-sung.md, đoạn "Thành phần" | Thành phần dự họp | Bối cảnh |
| project-profile.md, HE_THONG_NGOAI (cổng chi hộ) | Cổng chi hộ của ngân hàng đối tác | REQ-32 |
| project-profile.md, HE_THONG_NGOAI (cổng thanh toán) | Cổng thanh toán trực tuyến | REQ-43 |
| project-profile.md, HE_THONG_NGOAI (cổng SMS) | Cổng SMS của nhà mạng | REQ-90 |
| project-profile.md, HE_THONG_NGOAI (thông báo đẩy) | Dịch vụ thông báo đẩy của nền tảng di động | REQ-99 |
| project-profile.md, HE_THONG_NGOAI (tra cứu mất cắp) | Hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an | REQ-24 |
| project-profile.md, HE_THONG_NGOAI (đầu đọc căn cước) | Đầu đọc căn cước gắn chip tại mỗi quầy | REQ-06 |
| project-profile.md, HE_THONG_NGOAI (máy in nhãn) | Máy in nhãn mã vạch tại mỗi quầy | REQ-105 |
| project-profile.md, HE_THONG_NGOAI (máy quét) | Máy quét mã vạch tại mỗi quầy | REQ-58 |
| project-profile.md, mục 4 | Ràng buộc đặc thù: Không có | Không có ràng buộc để ghi |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-01 | Ai lập hợp đồng cầm đồ và nhập số tiền cho vay trên phần mềm? (Nhân viên giao dịch / Vai trò khác, nêu rõ) | REQ-33, REQ-34, REQ-35; use case lập hợp đồng | Mục 3: "Nhân viên giao dịch in hợp đồng để khách ký" |
| Q-02 | Ai nhập thông tin tài khoản ngân hàng của khách khi giải ngân chuyển khoản? (Thủ quỹ / Nhân viên giao dịch / Khác, nêu rõ) | REQ-30, REQ-31, REQ-32; luồng giải ngân | Mục 3: "chuyển khoản vào tài khoản ngân hàng của khách" |
| Q-03 | Ai in nhãn mã vạch cho tài sản và in bằng thiết bị nào? (Nhân viên giao dịch bằng máy in nhãn ở quầy / Khác, nêu rõ) | REQ-36, REQ-37, REQ-105; luồng lập hợp đồng | Mục 3: "tài sản được dán nhãn mã vạch theo mã hợp đồng" |
| Q-04 | Biên nhận chuộc đồ do ai lập hoặc in? (Nhân viên giao dịch in / Khác, nêu rõ) | REQ-60, REQ-61; luồng chuộc đồ | Mục 5: "khách kiểm tra tài sản và ký biên nhận" |
| Q-05 | Số máy của xe máy có được ghi trong đặc điểm tài sản và do nhân viên định giá nhập không? (Có / Không, nêu ai nhập) | REQ-12, REQ-22, REQ-23; luồng định giá xe máy | Mục 2: đặc điểm không có số máy, nhưng bước tra cứu gửi "số khung, số máy" |
| Q-06 | Ảnh thẻ căn cước của khách do ai tạo và lưu khi nào? (Nhân viên giao dịch chụp khi tạo hồ sơ mới / Đầu đọc cung cấp / Khác, nêu rõ) | REQ-91, REQ-92, REQ-05; luồng tạo hồ sơ khách | Mục 10: "ảnh thẻ căn cước của khách phải được mã hoá khi lưu trữ" |
| Q-07 | Khi bán tài sản thanh lý tại quầy, ai nhập số tiền bán được vào phần mềm? (Quản lý cửa hàng / Thủ quỹ / Khác, nêu rõ) | REQ-69, REQ-70, REQ-71; luồng thanh lý | Mục 6: "bán tài sản tại quầy cho người mua"; biên bản mục 5 chỉ nêu nhánh bộ phận thanh lý |
| Q-08 | Ai ghi nhận việc trả lại tiền thừa cho khách? (Thủ quỹ / Khác, nêu rõ) | REQ-73, REQ-74; luồng thanh lý | Mục 6: "cửa hàng phải trả lại cho khách trong vòng 30 ngày" |
| Q-09 | Số lần gia hạn tối đa của một hợp đồng là bao nhiêu? (6 / 12) | REQ-44, REQ-101; luồng gia hạn | Mục 4: "tối đa 6 lần"; biên bản mục 4: "đề nghị cho gia hạn tối đa 12 lần" |
| Q-10 | Tỉ lệ cho vay tối đa 80% (vàng nữ trang) và 60% (loại khác) là giá trị cố định hay giá trị ban đầu mà quản lý chuỗi đổi được? (Cố định / Đổi được) | REQ-17, REQ-18, REQ-81 | Mục 2 và Mục 9 |
| Q-11 | Hợp đồng ở trạng thái chờ thanh lý thì khách còn đóng lãi hoặc chuộc được không? (Có / Không) | REQ-39, REQ-50, REQ-66; luồng đóng lãi, chuộc, thanh lý | Mục 6: "chuyển sang trạng thái chờ thanh lý" |
| Q-12 | Quản lý cửa hàng có thể từ chối khoản vay không? (Có / Không) | REQ-19, REQ-20; luồng duyệt khoản vay | Mục 2: "phải được quản lý cửa hàng duyệt" |
| Q-13 | "Bảng giá thị trường" (Mục 2) và "bảng giá tham khảo" (Mục 9) là cùng một bảng không? (Cùng một bảng / Hai bảng khác nhau) | REQ-14, REQ-15, REQ-16 | Mục 2 và Mục 9 |
| Q-14 | Khi lệnh chi qua cổng chi hộ thất bại, thủ quỹ được thử lại hoặc chuyển sang giải ngân tiền mặt không? (Thử lại / Chuyển tiền mặt / Cả hai / Không) | REQ-30, REQ-32; luồng ngoại lệ của giải ngân | Mục 3: "qua cổng chi hộ của ngân hàng đối tác" |
| Q-15 | Khi giao dịch thanh toán trực tuyến bị huỷ, khách có được báo không? (Có / Không) | REQ-42, REQ-46; luồng ngoại lệ của đóng lãi trực tuyến | Mục 4: "chưa thành công trong 10 phút thì bị huỷ" |
| Q-16 | Khi gửi thông báo đẩy thất bại, hệ thống có gửi SMS thay thế không? (Có / Không) | REQ-98, REQ-99; luồng nhắc khách | biên bản mục 2: "thay cho SMS" |
| Q-17 | Giấy uỷ quyền có công chứng có được ghi nhận vào phần mềm khi chuộc đồ không? (Có, nêu thông tin cần ghi / Không) | REQ-54, REQ-55; luồng chuộc đồ | Mục 5: "bằng giấy uỷ quyền có công chứng" |
| Q-18 | Phần mềm có ghi nhận giấy đăng ký xe của xe máy không? (Có, nêu thông tin cần ghi / Không) | REQ-21; luồng định giá xe máy | Mục 2: "Xe máy phải có giấy đăng ký xe đứng tên khách" |
| Q-19 | Hệ thống nhận biết khách cũ bằng trường nào? (Số căn cước / Số điện thoại / Khác, nêu rõ) | REQ-07, REQ-08; luồng tiếp nhận khách | Mục 1: "khách mới ... khách cũ" |
| Q-20 | Sau bao lâu thì hệ thống tra cứu phương tiện bị mất cắp được coi là không phản hồi? (nêu số giây hoặc phút) | REQ-104, REQ-24 | biên bản mục 6: "không phản hồi" |
| Q-21 | Cơ quan công an có cung cấp tài liệu API tra cứu phương tiện bị mất cắp cho nhóm phát triển không? (Có / Không) | REQ-24; giao tiếp ngoài | project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" |
| Q-22 | Hệ thống báo cho quản lý cửa hàng về hợp đồng chờ thanh lý qua kênh nào? (Trên phần mềm / SMS / Cả hai / Khác, nêu rõ) | REQ-68; luồng chờ thanh lý | Mục 6: "báo cho quản lý cửa hàng" |
| Q-23 | Việc cất tài sản vào két có được ghi nhận trên phần mềm không? (Có, nêu cách ghi / Không) | REQ-38, REQ-57; quản lý tài sản cầm cố | Mục 3: "rồi cất vào két của cửa hàng" |
| Q-24 | Lãi suất do quản lý chuỗi đặt tính theo đơn vị nào? (Phần trăm mỗi ngày / Phần trăm mỗi kỳ hạn 30 ngày / Khác, nêu rõ) | REQ-27, REQ-28; công thức tính lãi | Mục 3: "lãi tính theo ngày ... với lãi suất do quản lý chuỗi đặt" |
| Q-25 | Thời hạn 10 phút của giao dịch thanh toán trực tuyến tính từ thời điểm nào? (Khi khách bắt đầu thanh toán / Khi hệ thống tạo giao dịch / Khác, nêu rõ) | REQ-46, REQ-47 | Mục 4: "chưa thành công trong 10 phút" |
| Q-26 | Cửa hàng nhỏ được định nghĩa thế nào, hoặc mọi cửa hàng đều được một nhân viên kiêm hai vai trò? (Danh sách cửa hàng nhỏ / Mọi cửa hàng) | REQ-96, REQ-97; phân quyền | biên bản mục 1: "Ở cửa hàng nhỏ" |
| Q-27 | Khách được coi là "đã cài ứng dụng" khi nào? (Đã đăng ký thành công bằng OTP / Thiết bị còn nhận được thông báo đẩy / Khác, nêu rõ) | REQ-98, REQ-62, REQ-63 | biên bản mục 2: "Khách đã cài ứng dụng di động" |
| Q-28 | Mã OTP có hiệu lực trong bao lâu? (nêu số phút) | REQ-77; luồng đăng ký ứng dụng | Mục 7: "gửi mã OTP qua SMS để xác nhận" |
| Q-29 | Hợp đồng được coi là "kết thúc" từ thời điểm nào để tính 5 năm lưu ảnh tài sản? (Khi khách chuộc / Khi thanh lý xong / Khi trả xong tiền thừa / Khác, nêu rõ) | REQ-93 | Mục 10: "sau khi hợp đồng kết thúc" |
| Q-30 | Lãi và phí khi tính tiền thừa được tính đến ngày nào? (Ngày bán / Ngày quá hạn 15 ngày / Khác, nêu rõ) | REQ-73, REQ-103, REQ-71 | Mục 6: "Tiền bán vượt quá gốc, lãi và phí" |
| Q-31 | Những vai trò nào được tra cứu hợp đồng bằng mã vạch tại quầy? (Nhân viên giao dịch / Thủ quỹ / Cả hai / Khác, nêu rõ) | REQ-94 | Mục 10: "Tra cứu hợp đồng tại quầy bằng mã vạch" |
| Q-32 | "Nhật ký thao tác" kiểm toán viên xem có cùng phạm vi với nhật ký thay đổi số tiền, kỳ hạn, trạng thái của hợp đồng không? (Cùng phạm vi / Rộng hơn, nêu rõ) | REQ-86, REQ-88, REQ-89 | Mục 9, câu 2 và câu 3 |
| Q-33 | Kiểm toán viên nội bộ xem được hợp đồng của cả 6 cửa hàng ở mọi trạng thái không? (Có / Có giới hạn, nêu rõ) | REQ-85, REQ-87 | Mục 9: "xem được mọi hợp đồng" |
| Q-34 | Báo cáo tỉ lệ hợp đồng quá hạn và doanh thu lãi theo tháng tính theo phạm vi nào? (Toàn chuỗi / Từng cửa hàng / Cả hai) | REQ-83, REQ-84 | Mục 9: "báo cáo dư nợ theo cửa hàng, tỉ lệ hợp đồng quá hạn, doanh thu lãi theo tháng" |
| Q-35 | Chuỗi chỉ nhận cầm bốn loại tài sản điện thoại, máy tính xách tay, xe máy, vàng nữ trang hay còn loại khác? (Chỉ bốn loại / Còn loại khác, nêu rõ) | REQ-04, REQ-18, REQ-28, REQ-81 | Mục 1: danh sách trong ngoặc; Mục 2: "các loại tài sản khác" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-01 | Nhân viên giao dịch lập hợp đồng cầm đồ trên phần mềm cho tài sản đã định giá và nhập số tiền cho vay trong giới hạn ở REQ-17, REQ-18. | Nguồn có hợp đồng in ra và khoảng 400 hợp đồng mới mỗi ngày nhưng không nói ai lập hợp đồng và nhập số tiền cho vay. Chờ Q-01 | REQ-34, REQ-35 |
| ASM-02 | Thủ quỹ nhập thông tin tài khoản ngân hàng của khách khi giải ngân bằng chuyển khoản. | Nguồn cần tài khoản ngân hàng của khách để chuyển khoản nhưng không nói ai nhập. Chờ Q-02 | REQ-31 |
| ASM-03 | Nhân viên giao dịch in nhãn mã vạch theo mã hợp đồng bằng máy in nhãn mã vạch tại quầy. | Nguồn nói tài sản được dán nhãn nhưng không nói ai tạo nhãn; HE_THONG_NGOAI có máy in nhãn. Chờ Q-03 | REQ-37, REQ-105 |
| ASM-04 | Nhân viên giao dịch in biên nhận chuộc đồ để khách ký. | Nguồn nói khách ký biên nhận nhưng không nói ai lập biên nhận. Chờ Q-04 | REQ-61 |
| ASM-05 | Nhân viên định giá ghi số máy của xe máy cùng với các đặc điểm tài sản. | Bước tra cứu mất cắp gửi số máy nhưng danh sách đặc điểm không có số máy. Chờ Q-05 | REQ-23 |
| ASM-06 | Nhân viên giao dịch chụp ảnh thẻ căn cước của khách khi tạo hồ sơ khách mới. | Nguồn yêu cầu mã hoá ảnh thẻ căn cước nhưng không nói ai tạo ảnh. Chờ Q-06 | REQ-92 |
| ASM-07 | Với tài sản bán tại quầy, quản lý cửa hàng nhập số tiền bán được vào phần mềm và phần mềm tính tiền thừa phải trả lại khách như nhánh bộ phận thanh lý. | Biên bản mục 5 chỉ nêu việc nhập số tiền bán và tính tiền thừa cho nhánh bộ phận thanh lý, trong khi quy tắc trả tiền thừa áp dụng cho mọi trường hợp bán. Chờ Q-07 | REQ-70, REQ-71 |
| ASM-08 | Thủ quỹ ghi nhận việc trả lại tiền thừa cho khách. | Nguồn quy định thời hạn 30 ngày để trả tiền thừa nhưng không nói ai thực hiện và ghi nhận. Chờ Q-08 | REQ-74 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Số lượng REQ là 105, vượt mức tham khảo 80 của prompt. Nguyên nhân là nguồn dày ngưỡng định lượng và mỗi ngưỡng tách thành một REQ Quy tắc nghiệp vụ theo F2 quy tắc 5; không gộp thêm.
- Các REQ chức năng REQ-46, REQ-62, REQ-63, REQ-66 dẫn mã REQ quy tắc chứa ngưỡng (F2 quy tắc 5), nên không đọc riêng được hoàn toàn; chấp nhận theo quy tắc đó.
- Mã Q được sắp theo mức ảnh hưởng (Q-01 đến Q-08 gắn ASM, rồi chức năng, rồi giá trị), không theo thứ tự xuất hiện trong nguồn.
- Không có mục Target nào ở trạng thái Không đạt.
