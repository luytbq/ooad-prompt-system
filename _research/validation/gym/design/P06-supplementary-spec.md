# P06 - Đặc tả bổ sung - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P06 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-phong-tap.md; P00-problem-brief.md (phiên bản 1.0); P01-actors.md (phiên bản 1.0); P02-usecases.md (phiên bản 1.1; Mục 4, Mục 5); P04-uc-specs/UC-005-purchase-or-renew-membership-package.md, UC-010-book-class-spot.md, UC-015-cancel-under-booked-class.md, UC-018-enter-branch.md (phiên bản 1.0; bảng thông tin chung hàng UC và REQ, mục 6 Quy tắc nghiệp vụ, mục 7 Yêu cầu đặc biệt, mục 8 Thông tin bổ sung, Câu hỏi mở, Giả định, Đề xuất sửa artifact trước); P04-uc-specs/_BR-register.md (BR-01 đến BR-20); P05-glossary.md (phiên bản 1.0). Mã Q, ASM lớn nhất được quét thêm (chỉ quét mã) ở các artifact khác trong thư mục đầu ra. MO_HINH_CHAT_LUONG: ISO/IEC 25010. YEU_CAU_BO_SUNG: chỉ bốn use case UC-005, UC-010, UC-015, UC-018 có đặc tả P04; đề xuất sửa P02 trong bốn đặc tả chưa áp dụng (REQ đặc tả đề nghị thêm vào cột REQ của UC chỉ là dữ liệu do use case khác cung cấp; hiển thị mã QR là tiền điều kiện của UC-018 theo phương án (a)); chín đề xuất đổi cách gọi của P05 chưa áp dụng vào P00, P01, P02, P04, dùng thuật ngữ chuẩn của P05. Bản P06 cũ: chưa có |
| Phạm vi | Toàn hệ thống (đặc tả P04 hiện có cho UC-005, UC-010, UC-015, UC-018) |
| Mã Q, ASM cuối đã cấp | Q-80; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## 1. Giới thiệu

Tài liệu này gom yêu cầu chung của Hệ thống quản lý chuỗi phòng tập VietFit: yêu cầu phi chức năng đo được, ràng buộc thiết kế, giao tiếp với hệ thống ngoài và danh sách quy tắc nghiệp vụ hợp nhất. Yêu cầu riêng của một use case nằm ở đặc tả use case đó; tài liệu này chứa yêu cầu chung và danh sách BR chính thức, các đặc tả use case chỉ dẫn mã BR. Lần chạy này dựa trên đặc tả P04 của UC-005, UC-010, UC-015, UC-018; 24 use case còn lại chưa có đặc tả nên NFR và BR của chúng chỉ lấy từ P00 và P02, cần chạy lại khi có đặc tả mới. Sổ BR hiện có BR-01 đến BR-20; BR-21 đến BR-40 cấp mới ở bước này cho các REQ loại Quy tắc nghiệp vụ chưa có BR.

## 2. Yêu cầu chức năng dùng chung

Không có

## 3. Yêu cầu phi chức năng

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-01 | Performance efficiency / P - Performance | Chức năng đặt chỗ lớp nhóm (UC-010) phục vụ được tới 1.500 hội viên đặt chỗ cùng lúc khi mở đặt lớp cho tuần mới lúc 6 giờ sáng thứ Hai. | Kiểm thử tải 1.500 phiên đặt chỗ lớp nhóm đồng thời với dữ liệu mẫu theo quy mô nguồn (4 chi nhánh, khoảng 6.000 hội viên, 40 huấn luyện viên, khoảng 25 lớp nhóm mỗi ngày mỗi chi nhánh). Mức đạt: Chưa đo được (Q-42): nguồn không nêu thời gian phản hồi tối đa cho một lần đặt chỗ và "cùng lúc" là trong khoảng bao nhiêu giây. Cách tính: Chưa quy định (Q-76). Mốc "6 giờ sáng thứ Hai" phụ thuộc Q-11 (cách mở đặt chỗ). | UC-010 | REQ-94, REQ-01, REQ-02, REQ-03, REQ-04 |
| NFR-02 | Performance efficiency / P - Performance | Cửa quay (ACT-12) phản hồi trong vòng 1 giây. | Đo tự động thời gian phản hồi cho mỗi lượt quẹt mã QR tại cửa quay của chi nhánh. Mức đạt: không quá 1 giây. Mốc bắt đầu và mốc kết thúc của phép đo: Chưa quy định (Q-41). Cách tính và mức tải: Chưa quy định (Q-76). Dữ liệu mẫu theo quy mô nguồn (4 chi nhánh, khoảng 6.000 hội viên). | UC-018 | REQ-96, REQ-01, REQ-02 |

## 4. Ràng buộc thiết kế

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-03 | Không tương ứng / + Ràng buộc thiết kế | Ứng dụng di động của hội viên và huấn luyện viên chạy trên hai nền tảng Android và iOS. | Kiểm tra triển khai: ứng dụng di động cài đặt và chạy được trên Android và trên iOS; mức đạt: có hoặc không đối với từng nền tảng. Phiên bản hệ điều hành tối thiểu: Chưa quy định (Q-78). | Toàn hệ thống | REQ-06, REQ-11, REQ-22, REQ-39 |
| NFR-04 | Không tương ứng / + Ràng buộc thiết kế | Ứng dụng web của lễ tân, quản lý chi nhánh và giám đốc chuỗi chạy trên trình duyệt máy tính. | Kiểm tra triển khai: các chức năng của lễ tân, quản lý chi nhánh và giám đốc chuỗi dùng được từ trình duyệt máy tính; mức đạt: có hoặc không. Trình duyệt và phiên bản tối thiểu: Chưa quy định (Q-78). | Toàn hệ thống | REQ-18, REQ-69, REQ-78 |
| NFR-05 | Không tương ứng / + Ràng buộc thiết kế | Phần mềm chỉ gửi dữ liệu giao dịch thu tiền sang hệ thống hoá đơn điện tử và không thực hiện việc lập, điều chỉnh, huỷ hoá đơn điện tử. | Xem xét mã nguồn và danh sách chức năng: có chức năng gửi dữ liệu giao dịch thu tiền và không có chức năng lập, điều chỉnh, huỷ hoá đơn; mức đạt: có hoặc không (ràng buộc đặc thù của hồ sơ dự án, mục 4). | UC-005, UC-007, UC-017, UC-019 | REQ-92 |
| NFR-06 | Không tương ứng / + Ràng buộc thiết kế | Phần mềm không tính thù lao huấn luyện viên và chỉ cung cấp báo cáo số buổi tập cá nhân của từng huấn luyện viên. | Xem xét mã nguồn và danh sách chức năng: không có chức năng tính thù lao; có báo cáo số buổi tập cá nhân của từng huấn luyện viên; mức đạt: có hoặc không (ràng buộc đặc thù của hồ sơ dự án, mục 4). Cách tính số buổi và kỳ báo cáo: Q-34. | UC-028 | REQ-83 |

## 5. Giao tiếp ngoài

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-07 | Compatibility (Interoperability) / + Giao tiếp | Hệ thống gửi thông tin đơn mua tới cổng thanh toán trực tuyến của đối tác (ACT-08) và nhận kết quả thanh toán qua API REST theo tài liệu API thanh toán và tra cứu giao dịch của đối tác. Cổng tự gửi kết quả về hay phần mềm tra cứu: chờ Q-45. Khi cổng không phản hồi: chưa quy định (Q-77). | Kiểm thử tích hợp với cổng thanh toán: thông tin đơn mua được gửi đi và kết quả thanh toán được nhận về qua API theo tài liệu API; mức đạt: có hoặc không. Kết quả thanh toán đến sau khi đơn đã bị huỷ: Q-14. | UC-005 | REQ-14 |
| NFR-08 | Compatibility (Interoperability) / + Giao tiếp | Hệ thống không có kết nối trực tiếp với máy POS của ngân hàng và nhận mã giao dịch POS do lễ tân (ACT-05) nhập tay. | Xem xét mã nguồn và cấu hình triển khai: không có giao tiếp mạng hoặc thiết bị tới máy POS; mã giao dịch POS được nhận từ dữ liệu lễ tân nhập; mức đạt: có hoặc không. Quy tắc định dạng và kiểm tra trùng của mã: Q-55. | UC-005 | REQ-21, REQ-20 |
| NFR-09 | Compatibility (Interoperability) / + Giao tiếp | Hệ thống nhận mã QR đọc được từ cửa quay có đầu đọc mã QR tại mỗi chi nhánh (ACT-12) qua API và trả kết quả cho phép vào để cửa quay mở cửa. Tài liệu API của cửa quay: hồ sơ dự án chưa ghi. Nội dung trao đổi: chờ Q-67. Khi cửa quay không nhận được kết quả: chờ Q-72. | Kiểm thử tích hợp với cửa quay: mã QR đọc được tới phần mềm qua API và kết quả trả về làm cửa quay mở hoặc giữ đóng; mức đạt: có hoặc không. Giao thức và định dạng dữ liệu: Chưa quy định (Q-67). | UC-018 | REQ-40 |
| NFR-10 | Compatibility (Interoperability) / + Giao tiếp | Hệ thống gửi nội dung thông báo tới dịch vụ thông báo đẩy của nền tảng di động (ACT-10) để dịch vụ chuyển thông báo đẩy tới ứng dụng của hội viên. Giao thức và tài liệu API: hồ sơ dự án chưa ghi. Khi dịch vụ không nhận hoặc không gửi được: chờ Q-65, Q-79. | Kiểm thử tích hợp với dịch vụ thông báo đẩy: nội dung thông báo được gửi tới dịch vụ và tới ứng dụng của hội viên thử nghiệm; mức đạt: có hoặc không. | UC-008, UC-011, UC-014, UC-015 | REQ-89 |
| NFR-11 | Compatibility (Interoperability) / + Giao tiếp | Hệ thống gửi nội dung tin nhắn tới cổng SMS của nhà mạng (ACT-09) qua API REST để cổng gửi SMS tới hội viên chưa cài ứng dụng. Khi cổng không nhận hoặc không gửi được: chờ Q-65, Q-79. | Kiểm thử tích hợp với cổng SMS: nội dung tin nhắn được gửi tới cổng và SMS tới số điện thoại của hội viên thử nghiệm; mức đạt: có hoặc không. | UC-008, UC-011, UC-014, UC-015 | REQ-90 |
| NFR-12 | Compatibility (Interoperability) / + Giao tiếp | Hệ thống gửi dữ liệu giao dịch thu tiền tới hệ thống hoá đơn điện tử của đơn vị cung cấp (ACT-11) qua API REST để xuất hoá đơn điện tử. Tài liệu API: hồ sơ dự án ghi chưa có. Các trường dữ liệu: chờ Q-39. Khi hệ thống hoá đơn điện tử không nhận hoặc từ chối: chờ Q-54. | Kiểm thử tích hợp với hệ thống hoá đơn điện tử: dữ liệu của mỗi giao dịch thu tiền được gửi sang và hoá đơn điện tử được xuất; mức đạt: có hoặc không. Phương pháp kiểm thử chi tiết cần tài liệu API: Chưa quy định (Q-39). | UC-005, UC-007, UC-017, UC-019 | REQ-92 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Áp dụng cho UC | REQ | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|
| BR-01 | Mỗi gói tập có thời hạn là 1, 3, 6 hoặc 12 tháng. | Ràng buộc | UC-001, UC-005, UC-026 | REQ-09 | Hiệu lực | UC-001, UC-026 theo P02 Mục 5 |
| BR-02 | Mỗi gói tập thuộc một trong hai loại: áp dụng cho một chi nhánh, hoặc áp dụng cho toàn chuỗi. | Ràng buộc | UC-001, UC-005, UC-026 | REQ-10 | Hiệu lực | UC-001, UC-026 theo P02 Mục 5 |
| BR-03 | Khi hội viên gia hạn lúc gói cũ còn hiệu lực, gói mới bắt đầu ngay sau ngày hết hạn của gói cũ. | Tính toán | UC-005 | REQ-17 | Hiệu lực | Trường hợp gói cũ đã hết hạn, đang bảo lưu hoặc mua gói mới chờ Q-24, Q-52, Q-51 |
| BR-04 | Đơn mua gói tập chưa thanh toán thành công trong 15 phút thì bị huỷ. | Kích hoạt hành động | UC-005 | REQ-15, REQ-16 | Hiệu lực | Áp dụng cho đơn bán tại quầy chờ Q-25 |
| BR-05 | Mọi giao dịch thu tiền phải được xuất hoá đơn điện tử. | Ràng buộc | UC-005, UC-007, UC-017, UC-019 | REQ-91 | Hiệu lực | Phạm vi giao dịch thu tiền chờ Q-37; UC-007, UC-017, UC-019 theo P02 Mục 5 |
| BR-06 | Hội viên chỉ được đặt chỗ lớp nhóm sớm nhất 7 ngày trước giờ học. | Ràng buộc | UC-010 | REQ-23 | Hiệu lực | Mâu thuẫn với BR-07, chờ Q-11; mốc muộn nhất để đặt chờ Q-58; Giữ cả hai BR mâu thuẫn, không chọn bên nào (P06 Action 8d) |
| BR-07 | Đặt chỗ lớp nhóm cho tuần mới mở lúc 6 giờ sáng thứ Hai. | Ràng buộc | UC-010 | REQ-93 | Hiệu lực | Mâu thuẫn với BR-06, chờ Q-11; Giữ cả hai BR mâu thuẫn, không chọn bên nào (P06 Action 8d) |
| BR-08 | Mỗi hội viên được đặt chỗ tối đa 2 lớp nhóm trong một ngày. | Ràng buộc | UC-010 | REQ-24 | Hiệu lực | Cách tính ngày và có tính lớp trong danh sách chờ chờ Q-60 |
| BR-09 | Hội viên bị khoá quyền đặt lớp trong 7 ngày thì không đặt được chỗ lớp nhóm trong thời gian khoá. | Ràng buộc | UC-010, UC-016 | REQ-38 | Hiệu lực | Điều kiện dẫn tới khoá thuộc UC-016; chỗ đã đặt của hội viên bị khoá chờ Q-20; UC-016 theo P02 Mục 5 |
| BR-10 | Sức chứa của mỗi lớp nhóm được xác định theo phòng. | Sự kiện | UC-009, UC-010 | REQ-25 | Hiệu lực | Sức chứa lớp so với sức chứa phòng chờ Q-03; UC-009 theo P02 Mục 5 |
| BR-11 | Số chỗ đã đặt của một lớp nhóm không được vượt sức chứa, kể cả khi nhiều hội viên đặt chỗ cùng lúc. | Ràng buộc | UC-010 | REQ-95, REQ-94 | Hiệu lực | Chỗ giữ riêng cho người đứng đầu danh sách chờ chờ Q-22 |
| BR-12 | Lớp nhóm đã đủ chỗ thì hội viên được vào danh sách chờ của lớp. | Kích hoạt hành động | UC-010 | REQ-26 | Hiệu lực | Tự vào hay hội viên chọn chờ Q-62 |
| BR-13 | Lớp nhóm có dưới 3 người đặt chỗ lúc 2 giờ trước giờ học thì bị huỷ. | Kích hoạt hành động | UC-015 | REQ-73, REQ-74 | Hiệu lực | Việc nhân viên duyệt hoặc gỡ chờ Q-43; chỗ giữ riêng và chỗ của hội viên bị khoá có tính vào số người đặt chỗ hay không chờ Q-22, Q-20 |
| BR-14 | Thông báo cho hội viên gửi qua thông báo đẩy của ứng dụng; hội viên chưa cài ứng dụng thì nhận SMS qua cổng SMS. | Kích hoạt hành động | UC-008, UC-011, UC-014, UC-015 | REQ-87, REQ-88 | Hiệu lực | Cách xác định hội viên chưa cài ứng dụng chờ Q-36; UC-008, UC-011, UC-014 theo P02 Mục 5 |
| BR-15 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên còn hiệu lực. | Ràng buộc | UC-018 | REQ-41 | Hiệu lực | Gói buổi tập cá nhân có tính là gói tập chờ Q-18; hội viên có nhiều gói cùng lúc chờ Q-69 |
| BR-16 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên không đang bảo lưu. | Ràng buộc | UC-018 | REQ-41 | Hiệu lực | Hội viên có nhiều gói cùng lúc chờ Q-69 |
| BR-17 | Cửa quay chỉ mở cho hội viên khi gói tập của hội viên áp dụng cho chi nhánh có cửa quay đó. | Ràng buộc | UC-018 | REQ-41, REQ-10 | Hiệu lực | Cách cửa quay cho biết chi nhánh chờ Q-67; hội viên có nhiều gói cùng lúc chờ Q-69; UC-001, UC-005, UC-026 gắn với REQ-10 ở P02 Mục 5 không thêm vì REQ-10 chỉ là REQ phụ của quy tắc cửa quay này |
| BR-18 | Mã QR trên vé tập một ngày chỉ dùng được trong ngày mua vé. | Ràng buộc | UC-017, UC-018 | REQ-44 | Hiệu lực | Số lần dùng vé trong ngày chờ Q-40; UC-017 theo P02 Mục 5 |
| BR-19 | Mã QR trên vé tập một ngày chỉ dùng được tại chi nhánh đã mua vé. | Ràng buộc | UC-017, UC-018 | REQ-45 | Hiệu lực | Cách cửa quay cho biết chi nhánh chờ Q-67; UC-017 theo P02 Mục 5 |
| BR-20 | Hội viên đặt chỗ lớp nhóm được xem là không vào lớp khi không quẹt vào cửa trong khoảng từ 30 phút trước đến 10 phút sau giờ bắt đầu lớp. | Suy luận | UC-016, UC-018 | REQ-35 | Hiệu lực | UC-016 kiểm tra quy tắc này khi được đặc tả; lượt quẹt bị từ chối có tính hay không chờ Q-71; UC-016 theo P02 Mục 5; Dùng "giờ bắt đầu lớp"; P05 đề xuất đổi thành "giờ học" chờ Q-73 (xem Đề xuất sửa artifact trước) |
| BR-21 | Hội viên đứng đầu danh sách chờ được thông báo có chỗ trống có 30 phút để xác nhận nhận chỗ. | Ràng buộc | UC-012 | REQ-29 | Hiệu lực | Cấp tại P06 từ REQ-29; UC-012 theo P02 Mục 5; chỗ trống giữ riêng trong 30 phút chờ Q-22; số phận hội viên không xác nhận chờ Q-23 |
| BR-22 | Chỗ trong lớp nhóm không được chuyển từ danh sách chờ khi còn dưới 1 giờ trước giờ học. | Ràng buộc | UC-013 | REQ-31 | Hiệu lực | Cấp tại P06 từ REQ-31; UC-013 theo P02 Mục 5 |
| BR-23 | Hội viên chỉ huỷ được chỗ đã đặt chậm nhất 2 giờ trước giờ học. | Ràng buộc | UC-011 | REQ-33 | Hiệu lực | Cấp tại P06 từ REQ-33; UC-011 theo P02 Mục 5 |
| BR-24 | Hội viên có 3 lần vắng mặt trong 30 ngày thì bị khoá quyền đặt lớp. | Kích hoạt hành động | UC-016 | REQ-37 | Hiệu lực | Cấp tại P06 từ REQ-37; UC-016 theo P02 Mục 5; thời gian khoá 7 ngày ở BR-09; chỗ đã đặt của hội viên bị khoá chờ Q-20; đếm lại số lần vắng mặt sau khoá chờ Q-21; hệ thống tự khoá hay có bước nhân viên chờ Q-43 |
| BR-25 | Hội viên có gói từ 3 tháng trở lên được bảo lưu gói. | Ràng buộc | UC-006 | REQ-47 | Hiệu lực | Cấp tại P06 từ REQ-47; UC-006 theo P02 Mục 5; "gói" có gồm gói buổi tập cá nhân hay không chờ Q-17; P05 đề xuất dùng "gói tập" chưa áp dụng nên giữ chữ của REQ |
| BR-26 | Mỗi gói được bảo lưu một lần. | Ràng buộc | UC-006 | REQ-48 | Hiệu lực | Cấp tại P06 từ REQ-48; UC-006 theo P02 Mục 5; "gói" có gồm gói buổi tập cá nhân hay không chờ Q-17 |
| BR-27 | Thời gian bảo lưu của một lần bảo lưu từ 7 đến 30 ngày. | Ràng buộc | UC-006 | REQ-49 | Hiệu lực | Cấp tại P06 từ REQ-49; UC-006 theo P02 Mục 5 |
| BR-28 | Hội viên đăng ký bảo lưu trước ngày bắt đầu bảo lưu ít nhất 1 ngày. | Ràng buộc | UC-006 | REQ-50 | Hiệu lực | Cấp tại P06 từ REQ-50; UC-006 theo P02 Mục 5 |
| BR-29 | Ngày hết hạn của gói được lùi thêm đúng số ngày bảo lưu. | Tính toán | UC-006 | REQ-51 | Hiệu lực | Cấp tại P06 từ REQ-51; UC-006 theo P02 Mục 5; gói đang bảo lưu có tính còn hiệu lực chờ Q-52; "gói" có gồm gói buổi tập cá nhân hay không chờ Q-17 |
| BR-30 | Gói được chuyển nhượng khi còn ít nhất 30 ngày. | Ràng buộc | UC-007 | REQ-53 | Hiệu lực | Cấp tại P06 từ REQ-53; UC-007 theo P02 Mục 5; "gói" có gồm gói buổi tập cá nhân hay không chờ Q-17 |
| BR-31 | Phí chuyển nhượng gói tập là 200.000 đồng. | Tính toán | UC-007 | REQ-55 | Hiệu lực | Cấp tại P06 từ REQ-55; UC-007 theo P02 Mục 5; hình thức thu phí chờ Q-38 |
| BR-32 | Gói buổi tập cá nhân có 10 buổi hoặc 20 buổi. | Ràng buộc | UC-019 | REQ-57 | Hiệu lực | Cấp tại P06 từ REQ-57; UC-019 theo P02 Mục 5 |
| BR-33 | Gói buổi tập cá nhân dùng trong 90 ngày. | Ràng buộc | UC-019 | REQ-58 | Hiệu lực | Cấp tại P06 từ REQ-58; UC-019 theo P02 Mục 5; mốc tính 90 ngày chờ Q-26 |
| BR-34 | Huấn luyện viên xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân trong 12 giờ. | Ràng buộc | UC-021, UC-022 | REQ-61 | Hiệu lực | Cấp tại P06 từ REQ-61; UC-021, UC-022 theo P02 Mục 5; mốc bắt đầu 12 giờ chờ Q-80; xử lý khi từ chối chờ Q-30 |
| BR-35 | Hội viên huỷ buổi tập cá nhân trước 12 giờ thì không bị trừ buổi. | Tính toán | UC-023 | REQ-64 | Hiệu lực | Cấp tại P06 từ REQ-64; UC-023 theo P02 Mục 5; nghĩa của "trước 12 giờ" chờ Q-27; huỷ muộn hơn chờ Q-28; thời điểm trừ buổi chờ Q-29 |
| BR-36 | Một phòng không được xếp hai lớp nhóm trùng giờ. | Ràng buộc | UC-009 | REQ-71 | Hiệu lực | Cấp tại P06 từ REQ-71; UC-009 theo P02 Mục 5; nghĩa của "trùng giờ" chờ Q-32 |
| BR-37 | Một huấn luyện viên không được xếp hai lớp nhóm trùng giờ. | Ràng buộc | UC-009 | REQ-72 | Hiệu lực | Cấp tại P06 từ REQ-72; UC-009 theo P02 Mục 5; nghĩa của "trùng giờ" chờ Q-32 |
| BR-38 | Chương trình khuyến mãi giảm tối đa 20% giá gói. | Ràng buộc | UC-027 | REQ-80 | Hiệu lực | Cấp tại P06 từ REQ-80; UC-027 theo P02 Mục 5; loại hàng áp dụng chờ Q-08; cách áp dụng cho người mua chờ Q-09 |
| BR-39 | Hội viên có gói hết hạn trong 7 ngày tới được nhận thông báo nhắc gia hạn. | Kích hoạt hành động | UC-008 | REQ-85 | Hiệu lực | Cấp tại P06 từ REQ-85; UC-008 theo P02 Mục 5; nhắc mỗi ngày hay một lần, hội viên đã gia hạn còn được nhắc không chờ Q-35 |
| BR-40 | Thông báo nhắc gia hạn được gửi mỗi ngày lúc 8 giờ sáng. | Kích hoạt hành động | UC-008 | REQ-86 | Hiệu lực | Cấp tại P06 từ REQ-86; UC-008 theo P02 Mục 5; nhắc mỗi ngày hay một lần chờ Q-35 |

## 7. Ma trận truy vết

### REQ --> NFR / BR

| REQ | Loại REQ | NFR / BR | Ghi chú |
|---|---|---|---|
| REQ-01 | Dữ liệu | NFR-01, NFR-02 | Điều kiện đo (dữ liệu mẫu) của NFR-01, NFR-02; số liệu quy mô là mô tả hiện trạng trong nguồn, không nêu như yêu cầu dung lượng nên không tạo NFR riêng |
| REQ-02 | Dữ liệu | NFR-01, NFR-02 | Điều kiện đo (dữ liệu mẫu) của NFR-01, NFR-02; không tạo NFR dung lượng riêng vì nguồn không nêu như yêu cầu |
| REQ-03 | Dữ liệu | NFR-01 | Điều kiện đo (dữ liệu mẫu) của NFR-01; không tạo NFR dung lượng riêng vì nguồn không nêu như yêu cầu |
| REQ-04 | Dữ liệu | NFR-01 | Điều kiện đo (dữ liệu mẫu) của NFR-01; không tạo NFR dung lượng riêng vì nguồn không nêu như yêu cầu |
| REQ-09 | Quy tắc nghiệp vụ | BR-01 | - |
| REQ-10 | Quy tắc nghiệp vụ | BR-02, BR-17 | BR-17 dùng REQ-10 làm REQ phụ |
| REQ-14 | Giao tiếp ngoài | NFR-07 | - |
| REQ-16 | Quy tắc nghiệp vụ | BR-04 | - |
| REQ-17 | Quy tắc nghiệp vụ | BR-03 | - |
| REQ-21 | Giao tiếp ngoài | NFR-08 | - |
| REQ-23 | Quy tắc nghiệp vụ | BR-06 | - |
| REQ-24 | Quy tắc nghiệp vụ | BR-08 | - |
| REQ-25 | Quy tắc nghiệp vụ | BR-10 | - |
| REQ-29 | Quy tắc nghiệp vụ | BR-21 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-31 | Quy tắc nghiệp vụ | BR-22 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-33 | Quy tắc nghiệp vụ | BR-23 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-35 | Quy tắc nghiệp vụ | BR-20 | - |
| REQ-37 | Quy tắc nghiệp vụ | BR-24 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-38 | Quy tắc nghiệp vụ | BR-09 | - |
| REQ-40 | Giao tiếp ngoài | NFR-09 | Yêu cầu đặc biệt UC-018 dòng 2 trùng REQ-40, đã gộp vào NFR-09 |
| REQ-44 | Quy tắc nghiệp vụ | BR-18 | - |
| REQ-45 | Quy tắc nghiệp vụ | BR-19 | - |
| REQ-47 | Quy tắc nghiệp vụ | BR-25 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-48 | Quy tắc nghiệp vụ | BR-26 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-49 | Quy tắc nghiệp vụ | BR-27 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-50 | Quy tắc nghiệp vụ | BR-28 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-51 | Quy tắc nghiệp vụ | BR-29 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-53 | Quy tắc nghiệp vụ | BR-30 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-55 | Quy tắc nghiệp vụ | BR-31 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-57 | Quy tắc nghiệp vụ | BR-32 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-58 | Quy tắc nghiệp vụ | BR-33 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-61 | Quy tắc nghiệp vụ | BR-34 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-64 | Quy tắc nghiệp vụ | BR-35 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-71 | Quy tắc nghiệp vụ | BR-36 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-72 | Quy tắc nghiệp vụ | BR-37 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-74 | Quy tắc nghiệp vụ | BR-13 | - |
| REQ-80 | Quy tắc nghiệp vụ | BR-38 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-85 | Quy tắc nghiệp vụ | BR-39 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-86 | Quy tắc nghiệp vụ | BR-40 | BR cấp mới ở P06 vì chưa đặc tả P04 nào dùng tới |
| REQ-87 | Chức năng | BR-14 | Kênh thông báo dùng chung đã phủ bằng BR-14 (P04 UC-015), không lặp ở mục 2; kênh giao tiếp ở NFR-10 |
| REQ-88 | Chức năng | BR-14 | Kênh thông báo dùng chung đã phủ bằng BR-14 (P04 UC-015), không lặp ở mục 2; kênh giao tiếp ở NFR-11 |
| REQ-89 | Giao tiếp ngoài | NFR-10 | - |
| REQ-90 | Giao tiếp ngoài | NFR-11 | - |
| REQ-91 | Quy tắc nghiệp vụ | BR-05 | - |
| REQ-92 | Giao tiếp ngoài | NFR-12, NFR-05 | NFR-05 từ ràng buộc đặc thù của hồ sơ dự án (mục 4) |
| REQ-93 | Quy tắc nghiệp vụ | BR-07 | - |
| REQ-94 | Phi chức năng | NFR-01, BR-11 | Yêu cầu đặc biệt UC-010 dòng 1 thành NFR-01; BR-11 (REQ-95) nên kiểm chứng trong cùng kiểm thử tải |
| REQ-95 | Quy tắc nghiệp vụ | BR-11 | - |
| REQ-96 | Phi chức năng | NFR-02 | Yêu cầu đặc biệt UC-018 dòng 1 thành NFR-02 |

NFR-03 đến NFR-06 lấy từ hồ sơ dự án (NEN_TANG, ràng buộc đặc thù mục 4) và dẫn REQ loại Chức năng làm căn cứ ngữ cảnh (REQ-06, REQ-11, REQ-22, REQ-39, REQ-18, REQ-69, REQ-78, REQ-83); các REQ đó do use case phủ nên không lặp trong bảng trên.

### UC --> NFR / BR

NFR áp dụng toàn hệ thống áp dụng cho mọi use case; dòng đầu liệt kê chúng một lần.

| UC | NFR | BR |
|---|---|---|
| Toàn hệ thống | NFR-03, NFR-04 | - |
| UC-001 Xem giá gói tập | - | BR-01, BR-02 |
| UC-002 Xem lịch lớp nhóm | - | - |
| UC-003 Đăng ký tài khoản hội viên | - | - |
| UC-004 Đăng nhập | - | - |
| UC-005 Mua hoặc gia hạn gói tập | NFR-05, NFR-07, NFR-08, NFR-12 | BR-01, BR-02, BR-03, BR-04, BR-05 |
| UC-006 Bảo lưu gói tập | - | BR-25, BR-26, BR-27, BR-28, BR-29 |
| UC-007 Chuyển nhượng gói tập | NFR-05, NFR-12 | BR-05, BR-30, BR-31 |
| UC-008 Nhắc gia hạn gói tập | NFR-10, NFR-11 | BR-14, BR-39, BR-40 |
| UC-009 Lập lịch lớp nhóm | - | BR-10, BR-36, BR-37 |
| UC-010 Đặt chỗ lớp nhóm | NFR-01 | BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12 |
| UC-011 Huỷ chỗ lớp nhóm | NFR-10, NFR-11 | BR-14, BR-23 |
| UC-012 Nhận chỗ từ danh sách chờ | - | BR-21 |
| UC-013 Chuyển chỗ cho người kế tiếp | - | BR-22 |
| UC-014 Huỷ lớp nhóm vì sự cố | NFR-10, NFR-11 | BR-14 |
| UC-015 Huỷ lớp nhóm ít người đặt | NFR-10, NFR-11 | BR-13, BR-14 |
| UC-016 Ghi nhận vắng mặt lớp nhóm | - | BR-09, BR-20, BR-24 |
| UC-017 Bán vé tập một ngày | NFR-05, NFR-12 | BR-05, BR-18, BR-19 |
| UC-018 Vào chi nhánh | NFR-02, NFR-09 | BR-15, BR-16, BR-17, BR-18, BR-19, BR-20 |
| UC-019 Mua gói buổi tập cá nhân | NFR-05, NFR-12 | BR-05, BR-32, BR-33 |
| UC-020 Đặt buổi tập cá nhân | - | - |
| UC-021 Phản hồi yêu cầu đặt buổi tập | - | BR-34 |
| UC-022 Huỷ yêu cầu đặt buổi quá hạn | - | BR-34 |
| UC-023 Huỷ buổi tập cá nhân | - | BR-35 |
| UC-024 Ghi nhận buổi tập cá nhân | - | - |
| UC-025 Xem chỉ số cơ thể | - | - |
| UC-026 Đặt giá gói tập | - | BR-01, BR-02 |
| UC-027 Đặt chương trình khuyến mãi | - | BR-38 |
| UC-028 Xem báo cáo chuỗi | NFR-06 | - |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-76 | Thời gian phản hồi của đặt chỗ lớp nhóm (NFR-01) và của cửa quay (NFR-02) được tính theo cách nào (trung bình / phân vị 95 / mọi yêu cầu) và đo ở mức tải nào (với cửa quay: số lượt quẹt đồng thời tại một chi nhánh, giờ cao điểm)? (Nêu cách tính và mức tải) | NFR-01, NFR-02; REQ-94, REQ-96 | Mục 10 câu 3 và câu 4: "có thể có tới 1.500 hội viên đặt chỗ cùng lúc", "Cửa quay phải phản hồi trong vòng 1 giây" không nêu cách tính và mức tải của phép đo |
| Q-77 | Khi cổng thanh toán không phản hồi hoặc báo lỗi kỹ thuật lúc hệ thống gửi đơn mua hoặc nhận kết quả thanh toán, đơn mua được xử lý thế nào? (Coi như thanh toán không thành công / Giữ đơn chờ và tra cứu lại kết quả tới hết 15 phút / Khác - nêu rõ) | NFR-07; UC-005 (luồng 9a, 10a); REQ-14, REQ-16 | Mục 2 câu 1 và câu 2: "thanh toán qua cổng thanh toán trực tuyến của đối tác", "chưa thanh toán thành công trong 15 phút thì bị huỷ" không nêu trường hợp cổng không phản hồi |
| Q-78 | Ứng dụng di động cần hỗ trợ từ phiên bản Android và iOS nào, và ứng dụng web cần hỗ trợ những trình duyệt máy tính nào, từ phiên bản nào? (Nêu danh sách và phiên bản tối thiểu) | NFR-03, NFR-04; REQ-06, REQ-11, REQ-18 | project-profile.md, NEN_TANG: "Ứng dụng di động Android và iOS", "trình duyệt máy tính" không nêu phiên bản hay danh sách trình duyệt |
| Q-79 | Cách xử lý ở Q-65 khi dịch vụ thông báo đẩy hoặc cổng SMS không gửi được có áp dụng cho mọi loại thông báo (nhắc gia hạn, báo có chỗ trống, báo huỷ lớp vì sự cố) không? (Áp dụng chung / Từng loại thông báo một cách - nêu rõ) | NFR-10, NFR-11; UC-008, UC-011, UC-014 | Q-65 của P04 UC-015 chỉ hỏi cho thông báo lớp bị huỷ; Mục 10 câu 1 không nêu xử lý khi gửi không được |
| Q-80 | 12 giờ để huấn luyện viên xác nhận hoặc từ chối yêu cầu đặt buổi tập cá nhân tính từ lúc nào? (Từ lúc hội viên gửi yêu cầu / Từ lúc khác - nêu rõ) | BR-34; UC-021, UC-022; REQ-61, REQ-62 | Mục 7 câu 2: "huấn luyện viên xác nhận hoặc từ chối trong 12 giờ" không nêu mốc bắt đầu |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P05 | GL-01 (cột Ghi chú) | Ghi chú dẫn "Các REQ-47 đến REQ-51 chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-25 (REQ-47), BR-26 (REQ-48), BR-27 (REQ-49), BR-28 (REQ-50), BR-29 (REQ-51) |
| P05 | GL-02 (cột Ghi chú) | Ghi chú dẫn "REQ-64, chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-35 |
| P05 | GL-06 (cột Ghi chú) | Ghi chú dẫn "các REQ-52, REQ-53, REQ-55 chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-30 (REQ-53) và BR-31 (REQ-55); REQ-52 loại Chức năng, không có BR |
| P05 | GL-07 (cột Ghi chú) | Ghi chú dẫn "REQ-80, chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-38 |
| P05 | GL-08 (cột Ghi chú) | Ghi chú dẫn "REQ-29 ... REQ-31 chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-21 (REQ-29) và BR-22 (REQ-31) |
| P05 | GL-14 (cột Ghi chú) | Ghi chú dẫn "REQ-57, REQ-58 ... cả hai chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-32 (REQ-57) và BR-33 (REQ-58) |
| P05 | GL-15 (cột Ghi chú) | Ghi chú dẫn "REQ-85, REQ-86 ... cả hai chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-39 (REQ-85) và BR-40 (REQ-86) |
| P05 | GL-23 (cột Ghi chú) | Ghi chú dẫn "REQ-37, chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-24 |
| P05 | GL-26 (cột Ghi chú) | Ghi chú dẫn "REQ-71, REQ-72, chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-36 (REQ-71) và BR-37 (REQ-72) |
| P05 | GL-35 (cột Ghi chú) | Ghi chú dẫn "REQ-71, chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-36 |
| P05 | GL-43 (cột Ghi chú) | Ghi chú dẫn "REQ-61, chưa có BR", nay REQ đó đã có BR ở P06 | Thay bằng BR-34 |
| P04 | UC-018, BR-20 (và sổ BR, dòng BR-20) | P05 đề xuất đổi "giờ bắt đầu lớp" trong nội dung BR-20 thành "giờ học" khi Q-73 trả lời là cùng một thời điểm; P06 giữ nguyên nội dung BR-20 (Hiệu lực), dẫn Q-73 ở Ghi chú | Đổi thành "giờ học của lớp nhóm" khi Q-73 có câu trả lời; BR-20 cấp lần đầu tại P04 UC-018, sau khi đổi cập nhật cả sổ BR và bảng BR của P06 |

## Vấn đề còn mở

Các mục Target đạt. Các điểm cần người dùng lưu ý:

- Mục 2 để trống: REQ-87 và REQ-88 (gửi thông báo qua thông báo đẩy, SMS) theo phép thử F2 gần với chức năng dùng chung, nhưng P04 UC-015 đã xếp thành BR-14 và các bước sau (P05) dẫn BR-14. P06 giữ BR-14 là BR (Hiệu lực), không tạo bản trùng ở mục 2 để không có phần tử vừa là BR vừa là yêu cầu chức năng dùng chung. Nếu người dùng muốn coi kênh thông báo là chức năng dùng chung thì cần chuyển BR-14 sang trạng thái Loại và thêm một dòng ở mục 2, kèm sửa P04 UC-015.
- Chỉ UC-005, UC-010, UC-015, UC-018 có đặc tả P04. BR-21 đến BR-40 cấp từ P00 và P02 mà chưa có đặc tả P04 nào kiểm chứng; câu chữ có thể cần chỉnh khi các use case đó được đặc tả. NFR của các use case còn lại (nếu có Yêu cầu đặc biệt) chưa được thu thập. Cần chạy lại P06 sau khi xong mọi đặc tả P04.
- Cột Áp dụng cho UC của BR-17: REQ-10 là REQ phụ và P02 Mục 5 gắn REQ-10 với UC-001, UC-005, UC-026; ba use case đó không áp dụng quy tắc cửa quay nên không đưa vào, chỉ giữ UC-018 (lý do ghi ở Ghi chú). Các REQ do đặc tả P04 đề nghị thêm vào cột REQ của UC (chưa áp dụng vào P02) không được tính vào cột Áp dụng cho UC.
- BR-25, BR-26, BR-29, BR-30 giữ chữ "gói" của REQ vì phạm vi (gói tập hay cả gói buổi tập cá nhân) chờ Q-17; đề xuất đổi sang "gói tập" của P05 chưa áp dụng.
- NFR-05 và NFR-06 lấy từ ràng buộc đặc thù của hồ sơ dự án; bản chất là ranh giới phạm vi, được xếp ở mục 4 theo F5 vì hồ sơ dự án là nguồn của mục này.
- NFR-01 và NFR-02 chưa đo được đầy đủ (Q-42, Q-41, Q-76). Không có NFR về độ sẵn sàng, bảo mật, sao lưu vì nguồn không nêu và chế độ NGHIEM_NGAT không cho tự thêm.
- GL-04 của P05 ghi "REQ-68, chưa có BR" vẫn đúng: REQ-68 loại Chức năng (UC-025), không tạo BR nên không có đề xuất sửa P05 cho dòng này.
- Không có cặp BR trùng mã, trùng nghĩa hay mâu thuẫn mới. Cặp BR-06 và BR-07 mâu thuẫn đã có Q-11 (P00); giữ cả hai BR và dùng Q-11, không tạo câu hỏi trùng. Không BR nào mâu thuẫn với định nghĩa GL của P05; BR-20 chỉ lệch cách gọi (Q-73).
- Mục Giả định không lập vì chế độ NGHIEM_NGAT.
