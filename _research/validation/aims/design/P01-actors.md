# P01 - Xác định tác nhân - Hệ thống thương mại điện tử AIMS

| Thuộc tính | Giá trị |
|---|---|
| Bước | P01 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md 1.0; P00-problem-brief.md 1.0; AIMS-ProblemStatement-VI.md |
| Phạm vi | Toàn hệ thống |

## 1. Ranh giới hệ thống

Hệ thống cần xây dựng là phần mềm AIMS phục vụ khách hàng mua sản phẩm phương tiện truyền thông vật lý và quản trị viên vận hành cửa hàng.

| Thành phần | Trong / Ngoài | Căn cứ (REQ hoặc trích nguồn, Q, ASM) | Hệ quả |
|---|---|---|---|
| Phần mềm AIMS (mọi nền tảng) | Trong | REQ-01 | Là hệ thống cần xây dựng |
| Liên ngân hàng (các API trừ tiền, cộng tiền, reset, xem số dư) | Ngoài | REQ-77, REQ-98 đến REQ-101: "hệ thống sẽ gọi đến một số API được cung cấp sẵn" (L204-205) | Là tác nhân ACT-03 |
| Bộ nhớ thiết bị lưu thông tin mặc định | Trong | REQ-44 | Là thành phần nội bộ, không phải tác nhân |
| Tài khoản khách hàng lưu thông tin mặc định | Trong | REQ-44; Q-02 | Là thành phần nội bộ, không phải tác nhân |
| Kho dữ liệu sản phẩm, đơn hàng, giao dịch, lịch sử thao tác | Trong | REQ-26, REQ-70, REQ-80 | Là thành phần nội bộ, không phải tác nhân |
| Hệ thống gửi email tới hòm thư khách hàng, người dùng | Chưa quyết định | REQ-30, REQ-83; nguồn không nêu là hệ thống bên ngoài | Chờ trả lời Q-07 |

## 2. Bảng tác nhân

| ACT | Tên (VI) | Tên (EN) | Loại | Tính chất | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ | REQ |
|---|---|---|---|---|---|---|---|---|
| ACT-01 | Khách hàng | Customer | Người | Chính | Người mua sản phẩm trên AIMS, không cần tài khoản để đặt hàng và thanh toán. Gộp các cách gọi "khách hàng có đăng nhập", "khách hàng không đăng nhập", "người dùng mới". | Tìm sản phẩm muốn mua<br>Chuẩn bị giỏ hàng<br>Đặt hàng và thanh toán đơn hàng<br>Huỷ đơn hàng đã thanh toán<br>Xem lại lịch sử mua hàng | - | REQ-31 đến REQ-83, REQ-90 đến REQ-93 |
| ACT-02 | Quản trị viên | Administrator | Người | Chính | Người vận hành cửa hàng AIMS. | Quản lý sản phẩm bán<br>Phê duyệt hoặc từ chối đơn hàng chờ xử lý | - | REQ-08 đến REQ-28, REQ-84 đến REQ-89 |
| ACT-03 | Liên ngân hàng | Interbank | Hệ thống ngoài | Phụ | Hệ thống bên ngoài xử lý giao dịch trên thẻ tín dụng giả lập qua các API có sẵn; AIMS gọi tới bằng private token của thẻ. | Cung cấp: trừ tiền trên thẻ<br>Cung cấp: cộng tiền hoàn trả vào thẻ<br>Cung cấp: xem số dư thẻ | - | REQ-77, REQ-97 đến REQ-101 |

## 3. Bên liên quan không phải tác nhân

| Bên liên quan | Lợi ích hoặc mối quan tâm với hệ thống | Tương tác gián tiếp qua (ACT hoặc kênh) | REQ |
|---|---|---|---|
| SH-04 Người dùng được quản trị viên quản lý | Nhận email thông báo về hành động quản trị | Kênh email (chờ Q-07), chức năng chờ Q-01 | REQ-29, REQ-30 |
| SH-05 Văn nghệ sĩ, trí thức | Sản phẩm sáng tạo đến được với người mua | Không có | Không có (bối cảnh L5-9) |
| SH-06 Người nhận hàng | Nhận hàng theo thông tin giao hàng do ACT-01 cung cấp | ACT-01 Khách hàng | REQ-45 |

## 4. Ứng viên tác nhân bị loại

| Ứng viên | Lý do loại | REQ |
|---|---|---|
| Khách hàng có đăng nhập, Khách hàng không đăng nhập | Gộp vào ACT-01 Khách hàng: cùng tập mục tiêu, chỉ khác nơi lưu thông tin mặc định (A-T5); việc có đăng nhập hay không chờ Q-02 | REQ-44, REQ-93 |
| Người dùng mới | Gộp vào ACT-01 Khách hàng: câu L17 nói về khả năng làm quen của người dùng, không phải một vai trò riêng (A-T5) | REQ-03 |
| Hệ thống AIMS | A-T1: là chính hệ thống | REQ-01 |
| Bộ nhớ thiết bị, tài khoản khách hàng | A-T1: kho dữ liệu của chính hệ thống | REQ-44 |
| Hệ thống gửi email | A-T6: nguồn không nêu có hệ thống bên ngoài nào gửi email; chờ Q-07 | REQ-30, REQ-83 |
| Đơn vị vận chuyển | A-T6: nguồn chỉ nêu tên bước vận chuyển, không nêu ai tương tác với hệ thống; chờ Q-03 | REQ-42 |
| Nhóm sinh viên được cấp thẻ ảo, người dùng API reset | A-T4: chỉ phục vụ kiểm thử khi phát triển, không có mục tiêu nghiệp vụ với hệ thống | REQ-100 |
| Ngân hàng phát hành | A-T2: là thuộc tính của thông tin thẻ, không tương tác trực tiếp với hệ thống | REQ-46 |
| Thẻ tín dụng | A-T2: là dữ liệu do khách hàng cung cấp, không phải thiết bị hay hệ thống | REQ-46, REQ-75 |

## Câu hỏi mở

Không có câu hỏi mới. Các câu hỏi ảnh hưởng tới tác nhân đã có ở P00: Q-02 (đăng nhập), Q-03 (vận chuyển), Q-07 (hệ thống gửi email).

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Target 8: REQ-29, REQ-30 (quản lý người dùng) đã gắn ACT-02 nhưng thuộc mục Ngoài phạm vi của P00, chờ Q-01.
- Target 8: REQ-30, REQ-83 (gửi email) chưa có tác nhân phụ tương ứng vì chờ Q-07.
