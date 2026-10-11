# P06 - Đặc tả bổ sung - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P06 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-khach.md (tài liệu nguồn duy nhất); P00-problem-brief.md (phiên bản 1.0, Q-37, ASM-09); P01-actors.md (phiên bản 1.0, Q-39, ASM-11; Mục 2); P02-usecases.md (phiên bản 1.1, Q-42, ASM-16; Mục 4 và Mục 5); P04-uc-specs/UC-009-book-ticket-online.md (phiên bản 1.0, Q-45, ASM-24); P04-uc-specs/UC-017-cancel-trip.md (phiên bản 1.0, Q-50, ASM-33); P04-uc-specs/_BR-register.md (BR-01 đến BR-11); P05-glossary.md (phiên bản 1.0, Q-50, ASM-33). Chưa có bản P06 cũ. Placeholder MO_HINH_CHAT_LUONG: Không có (dùng FURPS+ mặc định). YEU_CAU_BO_SUNG: chỉ có hai đặc tả P04 là UC-009 và UC-017, các use case khác trong P02 chưa được đặc tả. Mã Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-50, ASM-33; lần chạy này cấp Q-51 đến Q-54, ASM-34 đến ASM-38 |
| Phạm vi | Toàn hệ thống; yêu cầu đặc biệt và BR lần này lấy từ P00, P02 và hai đặc tả UC-009, UC-017 |
| Mã Q, ASM cuối đã cấp | Q-54, ASM-38 |

## 1. Giới thiệu

Tài liệu này gom các yêu cầu không nằm gọn trong một use case của Hệ thống bán vé xe khách SaoViet Bus: yêu cầu phi chức năng đo được, ràng buộc thiết kế, giao tiếp với Cổng thanh toán, Cổng SMS, Máy in vé và máy soát vé cầm tay, cùng bảng quy tắc nghiệp vụ hợp nhất. Yêu cầu riêng của một use case nằm ở đặc tả use case đó; tài liệu này chứa yêu cầu chung và danh sách BR chính thức, còn các đặc tả use case chỉ dẫn mã BR. Phiên bản 1.0 mới có hai đặc tả P04 (UC-009, UC-017), nên các dòng Yêu cầu đặc biệt của những use case còn lại sẽ được bổ sung khi chạy lại. NFR xếp theo FURPS+ kèm đặc tính ISO/IEC 25010 tương ứng.

## 2. Yêu cầu chức năng dùng chung

Không có

## 3. Yêu cầu phi chức năng

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-01 | F - Functionality / Security | Hệ thống không lưu thông tin thẻ của hành khách. | Xem xét mã nguồn, dữ liệu lưu trữ, nhật ký và cấu hình triển khai; mức đạt: không có thông tin thẻ của hành khách ở nơi nào do hệ thống quản lý (đặc tính có hoặc không) | Toàn hệ thống | REQ-76 |
| NFR-02 | F - Functionality / Security | Hành khách hoàn tất UC-009 Đặt vé trực tuyến mà không cần đăng nhập và không cần có tài khoản. | Kiểm thử chức năng với phiên chưa đăng nhập và số điện thoại chưa đăng ký tài khoản: đặt vé trực tuyến hoàn tất tới khi vé được phát hành; mức đạt: có (đặc tính có hoặc không) | UC-009 | REQ-04 |
| NFR-03 | F - Functionality / Security | Hệ thống chỉ cho phép ACT-03 Nhân viên điều hành thực hiện UC-017 Huỷ chuyến; phiên của vai trò khác bị từ chối (ASM-34, chờ Q-51). | Kiểm thử phân quyền: thực hiện huỷ chuyến bằng phiên của từng vai trò nhân viên nhà xe; mức đạt: chỉ phiên của ACT-03 huỷ được chuyến, phiên của vai trò khác bị từ chối (ASM-34, chờ Q-51) | UC-017 | REQ-55 |
| NFR-04 | R - Reliability / Reliability | Khi nhiều yêu cầu cùng chọn một chỗ của một chuyến xe tại cùng thời điểm, hệ thống chỉ cho đúng một yêu cầu giữ được chỗ đó. | Kiểm thử đồng thời: gửi đồng thời nhiều yêu cầu chọn cùng một chỗ của cùng một chuyến xe; mức đạt: đúng một yêu cầu giữ được chỗ, các yêu cầu còn lại nhận phản hồi chỗ không còn trống (UC-009 luồng 4a) | UC-009 | REQ-75 |
| NFR-05 | R - Reliability / Reliability | Mỗi vé mua trực tuyến của chuyến xe đã huỷ được yêu cầu hoàn tiền đúng một lần. | Kiểm tra dữ liệu giao dịch hoàn tiền và kiểm thử tích hợp luồng huỷ chuyến với Cổng thanh toán; đại lượng: số yêu cầu hoàn tiền gửi tới Cổng thanh toán cho mỗi vé; mức đạt: bằng 1; việc tính lần xử lý lại khi hoàn tiền không thành công: Chưa quy định (Q-50) | UC-017 | REQ-58 |
| NFR-06 | R - Reliability / Reliability | Số tiền hoàn cho mỗi vé mua trực tuyến của chuyến xe đã huỷ không vượt số tiền đã thu cho vé đó. | Kiểm tra dữ liệu giao dịch: so số tiền hoàn với số tiền đã thu của từng vé; mức đạt: số tiền hoàn không lớn hơn số tiền đã thu ở mọi vé (đặc tính có hoặc không) | UC-017 | REQ-58 |
| NFR-07 | R - Reliability / Reliability | Ứng dụng soát vé trả kết quả hợp lệ hoặc không hợp lệ đúng cho 100% mã vé có trong danh sách đã nhận khi máy mất kết nối liên tục trong toàn bộ thời gian soát vé của một chuyến xe (ASM-35, chờ Q-31). | Kiểm thử trên máy soát vé cầm tay Android đã nhận danh sách hành khách của chuyến xe: tắt kết nối suốt phiên thử, quét mã vé hợp lệ và các mã vé không hợp lệ theo BR-25; mức đạt: tỉ lệ mã quét có kết quả đúng bằng 100% (ASM-35, chờ Q-31); vé phát sinh sau thời điểm gửi danh sách: Chưa quy định (Q-29) | UC-026 | REQ-67 |
| NFR-08 | P - Performance / Performance efficiency | Website đặt vé trả kết quả cho mỗi yêu cầu tra cứu chuyến xe, xem sơ đồ chỗ và giữ chỗ trong không quá 2 giây ở phân vị 95 khi có 2.000 hành khách truy cập đồng thời trong dịp Tết (ASM-36, chờ Q-34). | Kiểm thử tải 2.000 phiên đồng thời (nguồn nêu "khoảng 2.000") gọi UC-008 Tra cứu chuyến xe và UC-009, không tính thời gian chờ Cổng thanh toán và Cổng SMS; mức đạt: thời gian từ khi gửi yêu cầu tới khi nhận đủ dữ liệu không quá 2 giây ở phân vị 95 (ASM-36, chờ Q-34, Q-52); dữ liệu mẫu: quy mô theo REQ-01, REQ-02, REQ-03 (12 tuyến, 3 bến xe, khoảng 80 chuyến mỗi ngày, khoảng 50 xe giường nằm 40 chỗ và 20 xe ghế ngồi 29 chỗ); số vé đã có, hỗn hợp thao tác của các phiên và khoảng ngày của "dịp Tết": Chưa quy định (Q-34, Q-52) | UC-008, UC-009 | REQ-74, REQ-01, REQ-02, REQ-03 |

## 4. Ràng buộc thiết kế

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-09 | + Ràng buộc thiết kế | Máy soát vé cầm tay mà hệ thống giao tiếp là thiết bị Android có đầu quét mã vạch, do nhà xe tự trang bị; ứng dụng soát vé chạy trên thiết bị đó (ASM-10, chờ Q-38). | Kiểm tra triển khai: ứng dụng soát vé được cài đặt, chạy và quét được mã vạch trên thiết bị Android có đầu quét mã vạch; mức đạt: có (đặc tính có hoặc không) | UC-026 | REQ-77 |

## 5. Giao tiếp ngoài

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-10 | + Giao tiếp / Compatibility | Hệ thống gửi yêu cầu thu tiền vé tới Cổng thanh toán (ACT-06) qua API thanh toán của cổng và nhận từ cổng kết quả thành công hoặc không thành công của từng giao dịch; thông tin thẻ do cổng xử lý và hệ thống không lưu (NFR-01); khi cổng không trả kết quả cho lời gọi, hệ thống coi giao dịch là không thành công theo ASM-37 (chờ Q-53); giao dịch thành công đến sau thời hạn giữ chỗ xử lý theo BR-06 (ASM-22, chờ Q-19). | Kiểm thử tích hợp với Cổng thanh toán: mỗi yêu cầu thu tiền nhận lại một kết quả thành công hoặc không thành công; mức đạt: có (đặc tính có hoặc không); tài liệu API: chưa có (project-profile.md, HE_THONG_NGOAI); cổng có tự gửi thông báo kết quả hay không: Chưa quy định (Q-39, ASM-11) | UC-009, UC-010, UC-014 | REQ-16, REQ-15 |
| NFR-11 | + Giao tiếp / Compatibility | Hệ thống gửi yêu cầu hoàn tiền cho vé mua trực tuyến tới Cổng thanh toán (ACT-06) qua API hoàn tiền của cổng, gồm hoàn một phần số tiền của giao dịch (ASM-32, chờ Q-20), và nhận từ cổng kết quả hoàn tiền của từng vé; khi cổng báo không thành công hoặc không trả kết quả, vé giữ trạng thái hoàn tiền "Chưa hoàn" và việc này được ghi nhận (ASM-33, chờ Q-50). | Kiểm thử tích hợp với Cổng thanh toán: mỗi yêu cầu hoàn tiền, kể cả hoàn một phần số tiền, nhận lại một kết quả hoàn tiền thành công hoặc không thành công; mức đạt: có (đặc tính có hoặc không); tài liệu API: chưa có (project-profile.md, HE_THONG_NGOAI); cơ chế xử lý lại vé chưa hoàn được tiền: Chưa quy định (Q-50) | UC-012, UC-017 | REQ-16, REQ-40, REQ-57 |
| NFR-12 | + Giao tiếp / Compatibility | Hệ thống gửi SMS tới số điện thoại của hành khách qua API REST của Cổng SMS (ACT-07), chiều từ hệ thống tới cổng, gồm SMS mã vé (UC-009, UC-014), SMS thông báo huỷ chuyến (UC-017) và SMS mã xác thực đăng nhập (UC-003, ASM-01); khi SMS không gửi được hoặc cổng không trả kết quả, vé hoặc chuyến đã lưu không bị đảo ngược và việc chưa gửi được được ghi nhận (ASM-20, chờ Q-35 với UC-009; ASM-31, chờ Q-49 với UC-017). | Kiểm thử tích hợp với Cổng SMS: mỗi SMS gửi đi gọi API REST của cổng và nhận lại kết quả của lời gọi; mức đạt: có (đặc tính có hoặc không); cơ chế xử lý lại SMS chưa gửi được: Chưa quy định (Q-49) | UC-003, UC-009, UC-014, UC-017 | REQ-21, REQ-20, REQ-56, REQ-12 |
| NFR-13 | + Giao tiếp / Compatibility | Hệ thống gửi dữ liệu vé tới máy in vé nhiệt tại quầy (ACT-08), chiều từ hệ thống tới máy, để in vé giấy có mã vạch (UC-006, UC-015 theo ASM-14, chờ Q-40). | Kiểm thử tích hợp với máy in vé nhiệt tại quầy: dữ liệu vé gửi đi được in thành vé giấy có mã vạch; mức đạt: có (đặc tính có hoặc không) | UC-004, UC-006, UC-015 | REQ-27, REQ-26 |
| NFR-14 | + Giao tiếp / Compatibility | Hệ thống gửi danh sách hành khách của chuyến xe về máy soát vé cầm tay (không là tác nhân, ASM-10) vào thời điểm theo BR-26 và nhận từ máy kết quả soát vé khi máy có kết nối trở lại; khi máy chưa nhận được danh sách tại thời điểm gửi, hệ thống ghi nhận và gửi lại theo ASM-38 (chờ Q-54); vé phát sinh sau thời điểm gửi danh sách xử lý theo Q-29; nội dung danh sách chờ Q-30. | Kiểm thử tích hợp với máy soát vé cầm tay: danh sách hành khách của chuyến xe xuất hiện trên máy sau khi gửi; kết quả soát vé lưu khi mất kết nối được gửi lại về hệ thống khi máy có kết nối; mức đạt: có (đặc tính có hoặc không) | UC-025, UC-026 | REQ-64, REQ-68, REQ-69 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Áp dụng cho UC | REQ | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|
| BR-01 | Mỗi lần đặt vé, hành khách chọn tối đa 5 chỗ. | Ràng buộc | UC-009 | REQ-08 | Hiệu lực | Luồng bán tại quầy chờ Q-12. Nguồn phát hiện: P04 UC-009 |
| BR-02 | Không được có hai vé cùng một chỗ trên một chuyến. | Ràng buộc | UC-004, UC-005, UC-009, UC-014, UC-015 | REQ-75 | Hiệu lực | UC-004, UC-005, UC-014, UC-015 theo P02 Mục 5 (REQ-75). Tính chất xử lý đồng thời xem NFR-04. Nguồn phát hiện: P04 UC-009 |
| BR-03 | Các chỗ hành khách đã chọn được giữ trong 10 phút để thanh toán, tính từ lúc hệ thống giữ các chỗ đó (ASM-18); hết 10 phút mà chưa thanh toán thành công thì chỗ được trả lại cho người khác. | Ràng buộc | UC-009, UC-010 | REQ-13, REQ-14, REQ-17 | Hiệu lực | UC-009 theo ASM-18 (chờ Q-18); UC-010 theo P02 Mục 5 (REQ-17). Nguồn phát hiện: P04 UC-009 |
| BR-04 | Mỗi chỗ có một mã vé. | Ràng buộc | UC-004, UC-009, UC-017 | REQ-19 | Hiệu lực | UC-004 theo P02 Mục 5 (REQ-19). Nguồn phát hiện: P04 UC-009 |
| BR-05 | Vé của một chuyến chỉ bán trực tuyến cho đến giờ xuất bến; từ giờ xuất bến trở đi không giữ chỗ để bán (ASM-21). | Ràng buộc | UC-009 | REQ-04 | Hiệu lực | UC-009 theo ASM-21 (chờ Q-13); luồng bán tại quầy cũng chờ Q-13. Nguồn phát hiện: P04 UC-009 |
| BR-06 | Giao dịch thanh toán thành công đến sau khi hết thời hạn giữ chỗ và chỗ đã trả lại cho người khác thì không phát hành vé và khoản tiền được hoàn cho hành khách (ASM-22). | Kích hoạt hành động | UC-009, UC-010 | REQ-15, REQ-17 | Hiệu lực | UC-009 theo ASM-22 (chờ Q-19); phần xử lý giao dịch đến sau thuộc UC-010 (UC-010 theo P02 Mục 5, REQ-15, REQ-17). Nguồn phát hiện: P04 UC-009 |
| BR-07 | Số tiền hoàn cho mỗi vé của chuyến bị huỷ bằng 100% giá vé của vé đó. | Tính toán | UC-017, UC-018 | REQ-58 | Hiệu lực | UC-018 theo P02 Mục 5 (REQ-58). Nguồn phát hiện: P04 UC-017 |
| BR-08 | Vé của chuyến bị huỷ được hoàn tiền qua cùng kênh với kênh mua vé: vé mua trực tuyến hoàn qua cổng thanh toán, vé mua tại quầy hoàn tiền mặt tại quầy (ASM-08). | Ràng buộc | UC-017, UC-018 | REQ-57, REQ-59 | Hiệu lực | UC-018 theo P02 Mục 5 (REQ-57, REQ-59); theo ASM-08 (chờ Q-07). Nguồn phát hiện: P04 UC-017 |
| BR-09 | Chuyến đã bị huỷ không được huỷ lại (ASM-26). | Ràng buộc | UC-017 | REQ-55 | Hiệu lực | UC-017 theo ASM-26 (chờ Q-46). Nguồn phát hiện: P04 UC-017 |
| BR-10 | Chuyến từ giờ xuất bến trở đi không được huỷ (ASM-26). | Ràng buộc | UC-017 | REQ-55 | Hiệu lực | UC-017 theo ASM-26 (chờ Q-46). Nguồn phát hiện: P04 UC-017 |
| BR-11 | Khi một chuyến bị huỷ, mọi hành khách đã có vé của chuyến phải được thông báo qua SMS (phạm vi "đã có vé" theo ASM-30). | Kích hoạt hành động | UC-017 | REQ-56 | Hiệu lực | UC-017 theo ASM-30 (chờ Q-25). Nguồn phát hiện: P04 UC-017 |
| BR-12 | Vé đặt qua điện thoại phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến. | Ràng buộc | UC-005, UC-006, UC-007 | REQ-31 | Hiệu lực | Chờ Q-14 (đặt khi còn dưới 60 phút). UC-005, UC-006, UC-007 theo P02 Mục 5 (REQ-31). Mốc của chuyến đã huỷ bị bỏ theo ASM-28 (chờ Q-47). Nguồn phát hiện: P06 |
| BR-13 | Trả vé trước giờ xuất bến từ 24 giờ trở lên được hoàn 90% giá vé. | Tính toán | UC-012 | REQ-37 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-37). Hoàn một phần số tiền của giao dịch chờ Q-20 (ASM-32). Nguồn phát hiện: P06 |
| BR-14 | Trả vé trước giờ xuất bến từ 4 giờ đến dưới 24 giờ được hoàn 50% giá vé. | Tính toán | UC-012 | REQ-38 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-38). Hoàn một phần số tiền của giao dịch chờ Q-20 (ASM-32). Nguồn phát hiện: P06 |
| BR-15 | Vé không được trả khi còn dưới 4 giờ trước giờ xuất bến. | Ràng buộc | UC-012 | REQ-39 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-39). Nguồn phát hiện: P06 |
| BR-16 | Vé mua tại quầy được hoàn tiền mặt tại quầy. | Ràng buộc | UC-012 | REQ-41 | Hiệu lực | UC-012 theo P02 Mục 5 (REQ-41). Câu nguồn bị động, chủ thể thực hiện theo ASM-04 (chờ Q-03). Hoàn tiền của chuyến bị huỷ xem BR-08. Nguồn phát hiện: P06 |
| BR-17 | Mỗi vé chỉ được đổi một lần. | Ràng buộc | UC-014, UC-015 | REQ-42 | Hiệu lực | UC-014, UC-015 theo P02 Mục 5 (REQ-42). Nguồn phát hiện: P06 |
| BR-18 | Vé chỉ được đổi chậm nhất 4 giờ trước giờ xuất bến. | Ràng buộc | UC-014, UC-015 | REQ-43 | Hiệu lực | Giờ xuất bến của chuyến cũ hay chuyến mới chờ Q-21. UC-014, UC-015 theo P02 Mục 5 (REQ-43). Nguồn phát hiện: P06 |
| BR-19 | Hành khách trả thêm phần chênh lệch khi vé mới đắt hơn vé cũ. | Tính toán | UC-010, UC-014, UC-015 | REQ-44 | Hiệu lực | Kênh thanh toán phần chênh lệch chờ Q-22 (ASM-13). UC-010, UC-014, UC-015 theo P02 Mục 5 (REQ-44). Nguồn phát hiện: P06 |
| BR-20 | Hành khách không được hoàn phần chênh lệch khi vé mới rẻ hơn vé cũ (ASM-05). | Ràng buộc | UC-014, UC-015 | REQ-45 | Hiệu lực | Theo ASM-05 (chờ Q-08). UC-014, UC-015 theo P02 Mục 5 (REQ-45). Nguồn phát hiện: P06 |
| BR-21 | Một xe không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-016 | REQ-52 | Hiệu lực | Thời gian chạy của chuyến lấy từ đâu chờ Q-15. UC-016 theo P02 Mục 5 (REQ-52). Nguồn phát hiện: P06 |
| BR-22 | Một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-016 | REQ-53 | Hiệu lực | Tách khỏi BR-21 vì đối tượng khác (xe, tài xế) theo hai REQ riêng. Chờ Q-15. UC-016 theo P02 Mục 5 (REQ-53). Nguồn phát hiện: P06 |
| BR-23 | Một tài xế không được lái quá 10 giờ trong một ngày. | Ràng buộc | UC-016 | REQ-54 | Hiệu lực | Cách tính ngày chờ Q-16; thời gian chạy chờ Q-15. UC-016 theo P02 Mục 5 (REQ-54). Nguồn phát hiện: P06 |
| BR-24 | Mức tăng giá vé cho một khoảng ngày tối đa 30%. | Ràng buộc | UC-024 | REQ-62 | Hiệu lực | Phạm vi khoảng ngày chờ Q-23; ngày áp dụng chờ Q-24. UC-024 theo P02 Mục 5 (REQ-62). Nguồn phát hiện: P06 |
| BR-25 | Mã vé không hợp lệ khi sai chuyến, vé đã huỷ hoặc vé đã soát. | Suy luận | UC-026 | REQ-66 | Hiệu lực | Ba trường hợp đầy đủ hay còn trường hợp khác chờ Q-28. UC-026 theo P02 Mục 5 (REQ-66). Nguồn phát hiện: P06 |
| BR-26 | Danh sách hành khách của chuyến được gửi về máy soát vé vào thời điểm 15 phút trước giờ xuất bến. | Kích hoạt hành động | UC-025 | REQ-70 | Hiệu lực | Nội dung danh sách chờ Q-30; vé phát sinh sau thời điểm gửi chờ Q-29. Mốc của chuyến đã huỷ bị bỏ theo ASM-28 (chờ Q-47). UC-025 theo P02 Mục 5 (REQ-70). Nguồn phát hiện: P06 |

## 7. Ma trận truy vết

NFR-01 áp dụng toàn hệ thống nên không lặp lại ở từng dòng của bảng UC --> NFR/BR.

### 7.1 REQ --> NFR/BR

| REQ | Loại REQ | NFR / BR | Ghi chú |
|---|---|---|---|
| REQ-01 | Dữ liệu | NFR-08 | P02 Mục 5 ghi "Chuyển P06"; dùng làm dữ liệu mẫu của NFR-08, không tạo NFR dung lượng riêng vì nguồn nêu số liệu quy mô, không nêu như một yêu cầu |
| REQ-02 | Dữ liệu | NFR-08 | Như REQ-01 |
| REQ-03 | Dữ liệu | NFR-08 | Như REQ-01 |
| REQ-04 | Chức năng | NFR-02 | NFR từ Yêu cầu đặc biệt của P04 UC-009; REQ cũng được UC-009 phủ |
| REQ-08 | Quy tắc nghiệp vụ | BR-01 | - |
| REQ-14 | Quy tắc nghiệp vụ | BR-03 | - |
| REQ-16 | Giao tiếp ngoài | NFR-10, NFR-11 | - |
| REQ-19 | Quy tắc nghiệp vụ | BR-04 | - |
| REQ-21 | Giao tiếp ngoài | NFR-12 | - |
| REQ-27 | Giao tiếp ngoài | NFR-13 | - |
| REQ-31 | Quy tắc nghiệp vụ | BR-12 | - |
| REQ-37 | Quy tắc nghiệp vụ | BR-13 | - |
| REQ-38 | Quy tắc nghiệp vụ | BR-14 | - |
| REQ-39 | Quy tắc nghiệp vụ | BR-15 | - |
| REQ-41 | Quy tắc nghiệp vụ | BR-16 | - |
| REQ-42 | Quy tắc nghiệp vụ | BR-17 | - |
| REQ-43 | Quy tắc nghiệp vụ | BR-18 | - |
| REQ-44 | Quy tắc nghiệp vụ | BR-19 | - |
| REQ-45 | Quy tắc nghiệp vụ | BR-20 | - |
| REQ-52 | Quy tắc nghiệp vụ | BR-21 | - |
| REQ-53 | Quy tắc nghiệp vụ | BR-22 | - |
| REQ-54 | Quy tắc nghiệp vụ | BR-23 | - |
| REQ-55 | Chức năng | NFR-03 | NFR từ Yêu cầu đặc biệt của P04 UC-017; REQ cũng được UC-017 phủ |
| REQ-58 | Quy tắc nghiệp vụ | BR-07, NFR-05, NFR-06 | NFR-05, NFR-06 từ Yêu cầu đặc biệt của P04 UC-017 |
| REQ-59 | Quy tắc nghiệp vụ | BR-08 | - |
| REQ-62 | Quy tắc nghiệp vụ | BR-24 | - |
| REQ-64 | Giao tiếp ngoài | NFR-14 | Nền tảng của máy soát vé: NFR-09 (REQ-77) |
| REQ-66 | Quy tắc nghiệp vụ | BR-25 | - |
| REQ-67 | Phi chức năng | NFR-07 | - |
| REQ-70 | Quy tắc nghiệp vụ | BR-26 | - |
| REQ-74 | Phi chức năng | NFR-08 | - |
| REQ-75 | Quy tắc nghiệp vụ | BR-02, NFR-04 | NFR-04 từ Yêu cầu đặc biệt của P04 UC-009; NFR-04 đo hành vi đồng thời, BR-02 giữ quy tắc nghiệp vụ |
| REQ-76 | Ràng buộc | NFR-01 | - |
| REQ-77 | Ràng buộc | NFR-09 | - |

### 7.2 UC --> NFR/BR

| UC | NFR | BR |
|---|---|---|
| UC-001 | - | - |
| UC-002 | - | - |
| UC-003 | NFR-12 | - |
| UC-004 | NFR-13 | BR-02, BR-04 |
| UC-005 | - | BR-02, BR-12 |
| UC-006 | NFR-13 | BR-12 |
| UC-007 | - | BR-12 |
| UC-008 | NFR-08 | - |
| UC-009 | NFR-02, NFR-04, NFR-08, NFR-10, NFR-12 | BR-01, BR-02, BR-03, BR-04, BR-05, BR-06 |
| UC-010 | NFR-10 | BR-03, BR-06, BR-19 |
| UC-011 | - | - |
| UC-012 | NFR-11 | BR-13, BR-14, BR-15, BR-16 |
| UC-013 | - | - (UC-013 trạng thái Loại, gộp vào UC-012) |
| UC-014 | NFR-10, NFR-12 | BR-02, BR-17, BR-18, BR-19, BR-20 |
| UC-015 | NFR-13 | BR-02, BR-17, BR-18, BR-19, BR-20 |
| UC-016 | - | BR-21, BR-22, BR-23 |
| UC-017 | NFR-03, NFR-05, NFR-06, NFR-11, NFR-12 | BR-04, BR-07, BR-08, BR-09, BR-10, BR-11 |
| UC-018 | - | BR-07, BR-08 |
| UC-019 | - | - |
| UC-020 | - | - |
| UC-021 | - | - |
| UC-022 | - | - |
| UC-023 | - | - |
| UC-024 | - | BR-24 |
| UC-025 | NFR-14 | BR-26 |
| UC-026 | NFR-07, NFR-09, NFR-14 | BR-25 |
| UC-027 | - | - |
| UC-028 | - | - |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-51 | Ngoài ACT-03 Nhân viên điều hành, vai trò nhân viên nhà xe nào khác (ví dụ ACT-04 Quản lý nhà xe) được huỷ chuyến? (Chỉ nhân viên điều hành / Cả quản lý nhà xe) | NFR-03; UC-017; phân quyền; REQ-55 | Mục 6, câu 4: "nhân viên điều hành huỷ chuyến" không nêu ai khác được hay không được huỷ; P04 UC-017 mục 7 dòng 1 viết "Chỉ nhân viên điều hành được huỷ chuyến" |
| Q-52 | Thời gian phản hồi của website khi có khoảng 2.000 hành khách truy cập đồng thời tính theo cách nào, cho những thao tác nào, và với khối lượng vé đã có là bao nhiêu? (Phân vị 95 cho tra cứu chuyến xe, xem sơ đồ chỗ và giữ chỗ / Trung bình cho mọi thao tác trên website / Nhập tỉ lệ thao tác và số vé đã có) | NFR-08; UC-008, UC-009; REQ-74 | Mục 10, câu 1: "chịu được khoảng 2.000 người truy cập cùng lúc vào dịp Tết" không nêu cách đo |
| Q-53 | Khi Cổng thanh toán không trả kết quả cho lời gọi thu tiền trong thời gian chờ, hệ thống xử lý giao dịch đó thế nào? (Coi là không thành công và cho hành khách thanh toán lại / Coi là chưa rõ kết quả, giữ chỗ đến hết thời hạn giữ chỗ và hỏi lại cổng về giao dịch) | NFR-10; UC-010, UC-009; BR-06; REQ-15, REQ-16 | Mục 3, câu 1 đến câu 3 chỉ nêu thanh toán thành công hoặc chưa thành công; project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" |
| Q-54 | Khi máy soát vé chưa nhận được danh sách hành khách tại thời điểm hệ thống gửi (máy tắt hoặc mất sóng), hệ thống xử lý thế nào? (Gửi lại khi máy có kết nối trở lại cho đến giờ xuất bến / Chỉ ghi nhận máy chưa nhận / Phụ xe tự yêu cầu danh sách trên máy) | NFR-14; UC-025, UC-026; BR-26; REQ-69, REQ-70 | Mục 8, câu 3 và câu 4: nêu gửi danh sách 15 phút trước giờ xuất bến và soát khi mất sóng, không nêu máy không nhận được danh sách |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-34 | Chỉ ACT-03 Nhân viên điều hành được huỷ chuyến; mọi vai trò khác, kể cả ACT-04 Quản lý nhà xe, không có quyền huỷ chuyến. | Chờ Q-51. Nguồn chỉ nêu "nhân viên điều hành huỷ chuyến" (Mục 6, câu 4); P04 UC-017 ghi "Chỉ" ở Yêu cầu đặc biệt mà không có giả định; chọn phương án hạn chế theo đúng vai trò nguồn nêu | NFR-03; UC-017; REQ-55 |
| ASM-35 | Khi máy soát vé mất kết nối liên tục trong toàn bộ thời gian soát vé của một chuyến xe, mọi mã vé có trong danh sách máy đã nhận đều nhận kết quả đúng (mức 100%). | Chờ Q-31. Nguồn nêu "Máy cần soát được cả khi xe ở vùng mất sóng" (Mục 8, câu 3) nhưng không nêu thời gian mất sóng tối đa và mức đạt; chọn phương án "trong phạm vi một chuyến" của Q-31 và mức 100% vì nguồn không cho phép mã nào không soát được. Mức khởi điểm để bên liên quan chốt | NFR-07; UC-026; REQ-67 |
| ASM-36 | Ngưỡng của NFR-08: thời gian phản hồi không quá 2 giây ở phân vị 95 cho tra cứu chuyến xe, xem sơ đồ chỗ và giữ chỗ khi có 2.000 phiên truy cập đồng thời; thời gian chờ Cổng thanh toán và Cổng SMS không tính. | Chờ Q-34, Q-52. Nguồn chỉ nêu "chịu được khoảng 2.000 người truy cập cùng lúc vào dịp Tết" (Mục 10, câu 1), không nêu thời gian phản hồi; mức khởi điểm để bên liên quan chốt, không có căn cứ trong nguồn hoặc artifact trước | NFR-08; UC-008, UC-009; REQ-74 |
| ASM-37 | Khi lời gọi thu tiền không nhận được kết quả từ Cổng thanh toán trong thời gian chờ, hệ thống coi giao dịch là không thành công tại thời điểm đó, không phát hành vé và xử lý như thanh toán không thành công (ASM-12). | Chờ Q-53. Nguồn không nêu cổng không phản hồi; chọn không phát hành vé khi chưa có kết quả thành công để không có vé chưa xác nhận tiền; nếu sau đó có kết quả thành công khi đã quá thời hạn giữ chỗ thì xử lý theo BR-06 (ASM-22) | NFR-10; UC-010, UC-009; REQ-15, REQ-16 |
| ASM-38 | Khi máy soát vé chưa nhận được danh sách hành khách tại thời điểm gửi, hệ thống ghi nhận máy chưa nhận và gửi lại danh sách khi máy có kết nối trở lại, cho đến giờ xuất bến của chuyến xe. | Chờ Q-54. Nguồn không nêu máy không nhận được danh sách; chọn gửi lại để phụ xe còn soát được khi xe ở vùng mất sóng sau đó (Mục 8, câu 3) | NFR-14; UC-025; REQ-69 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-017 (Mục 7 dòng 1) | "Chỉ nhân viên điều hành được huỷ chuyến" không có giả định đi kèm; nguồn nêu "nhân viên điều hành huỷ chuyến" (Mục 6, câu 4), không nêu "chỉ" | Dẫn ASM-34 và Q-51 của P06 ở dòng này, hoặc thêm giả định tương ứng vào mục Giả định của UC-017 |
| P04 | UC-017 (Mục 7 dòng 2; luồng 12a; ASM-33) | "được yêu cầu hoàn tiền đúng một lần" có thể mâu thuẫn với việc xử lý lại khi hoàn tiền không thành công (một phương án của Q-50 là tự thử hoàn lại) | Sau khi Q-50 được trả lời, nêu rõ lần xử lý lại có tính vào "đúng một lần" hay không. NFR-05 giữ nguyên chữ của UC-017 và ghi "Chưa quy định (Q-50)" ở phần tính lần xử lý lại |
| P02 | UC-017, UC-018 (Bảng 4) | Luồng 9a, 12a của UC-017 ghi nhận SMS chưa gửi và vé chưa hoàn tiền để xử lý lại sau, và UC-017 mục 8 giao cơ chế xử lý lại cho P06; chưa có use case nào đảm nhiệm việc này và Q-49, Q-50 chưa được trả lời nên P06 không đặc tả được | Sau khi Q-49, Q-50 được trả lời: nếu chọn "Ghi nhận và báo nhân viên điều hành" thì xem xét thêm use case xử lý lại ở P02; nếu chọn "Tự thử gửi lại" hoặc "Tự thử hoàn lại" thì chạy lại P06 để bổ sung NFR cho phần thử lại (số lần thử và khoảng cách là quyết định thiết kế, Conventions C1 mục 7) |
| P05 | GL-07 | Ghi chú dẫn "REQ-31 (chưa có BR)" và "REQ-70 (chưa có BR)" | Thay bằng BR-12 và BR-26 |
| P05 | GL-08 | Ghi chú dẫn "REQ-31, chưa có BR" | Thay bằng BR-12 |
| P05 | GL-16 | Ghi chú dẫn "REQ-62 (chưa có BR)" | Thay bằng BR-24 |
| P05 | GL-18 | Ghi chú dẫn "REQ-37, REQ-38, REQ-39, chưa có BR" | Thay bằng BR-13, BR-14, BR-15 |
| P05 | GL-24 | Ghi chú dẫn "REQ-66, chưa có BR" và "REQ-32 (chưa có BR...)"; REQ-32 là REQ loại Chức năng nên không có BR | Thay "REQ-66, chưa có BR" bằng BR-25; bỏ cụm "chưa có BR" sau REQ-32 |
| P05 | GL-26 | Ghi chú dẫn "REQ-31, REQ-32, chưa có BR"; REQ-32 là REQ loại Chức năng nên không có BR | Thay REQ-31 bằng BR-12; bỏ cụm "chưa có BR" sau REQ-32 |

## Vấn đề còn mở

- Mục 2 ghi "Không có": P00 không có REQ loại Chức năng nào áp dụng cho nhiều use case mà không thuộc một use case cụ thể. REQ-20 và REQ-56 (gửi SMS) thuộc UC-009, UC-014, UC-017 và được phủ ở NFR-12 như giao tiếp ngoài; REQ-23 (đăng nhập theo vai trò) đã là UC-003 theo P02.
- NFR-03: theo phép thử nhanh ở F2, "Chỉ nhân viên điều hành được huỷ chuyến" có thể là quy tắc nghiệp vụ (còn đúng khi làm bằng tay). Theo Target 2 (mọi dòng Yêu cầu đặc biệt thành NFR) và vì đây là phân quyền trong hệ thống, giữ là NFR nhóm Security, không ghi ở bảng BR. Nếu Q-51 cho thấy đây là chính sách của tổ chức thì chuyển sang BR khi chạy lại.
- NFR-02: "không cần có tài khoản" là đặc tính có hoặc không về quyền truy cập, xếp nhóm Security theo cách P04 UC-009 đã xếp; REQ-04 vẫn là REQ loại Chức năng và do UC-009 phủ.
- NFR-04 và BR-02 cùng gắn REQ-75: BR-02 là bất biến nghiệp vụ "không hai vé cùng một chỗ", NFR-04 đo hành vi khi nhiều yêu cầu đồng thời (đại lượng: số yêu cầu giữ được chỗ). Hai phát biểu đo hai điều khác nhau nên không tính là phần tử vừa NFR vừa BR.
- REQ-01, REQ-02, REQ-03 (loại Dữ liệu, P02 ghi "Chuyển P06") chỉ được dùng làm dữ liệu mẫu của NFR-08. Không tạo NFR nhóm P về dung lượng dữ liệu vì nguồn nêu đây là số liệu quy mô, không nêu như một yêu cầu.
- Không tạo ràng buộc từ NEN_TANG, CONG_NGHE (hồ sơ ghi "Chưa chốt") và RANG_BUOC_DAC_THU (ghi "Không có"). "Qua website" ở REQ-04 vẫn là kênh của REQ loại Chức năng như P00 đã chọn, không tạo ràng buộc nền tảng.
- REQ-77 vừa là Ràng buộc vừa gắn với máy soát vé của REQ-64 (Giao tiếp ngoài). Chọn REQ-77 ở mục 4 (nền tảng thiết bị) và REQ-64 ở mục 5 (trao đổi dữ liệu) để mỗi NFR chỉ một nhóm.
- NFR giao tiếp ở mục 5 gộp giao diện và hành vi khi hệ thống ngoài không phản hồi vào một phát biểu theo F5; "một đại lượng" được hiểu là một đặc tính có hoặc không của giao tiếp đó.
- Hành vi khi SMS mã xác thực đăng nhập (UC-003, ASM-01) không gửi được chưa có Q, ASM riêng vì UC-003 chưa có đặc tả P04; bổ sung khi chạy lại sau khi UC-003 được đặc tả. Q-35 và Q-49 chỉ phủ SMS mã vé và SMS thông báo huỷ chuyến.
- BR-12 và BR-26 nêu mốc theo giờ xuất bến; ASM-28 của P04 UC-017 bỏ các mốc này cho chuyến đã huỷ. Giữ nguyên nội dung hai BR (theo nguồn), ghi ngoại lệ ở Ghi chú và dẫn Q-47.
- NFR-08 dùng "hành khách truy cập" thay cho "người truy cập" của nguồn vì GL-09 liệt "người truy cập" là từ không dùng.
- BR-25 giữ ba điều kiện của REQ-66 trong một câu Suy luận vì nguồn nêu chúng như một định nghĩa vé không hợp lệ.
