# P06 - Đặc tả bổ sung - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P06 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md (bản hiện có); project-profile.md (bản hiện có); yeu-cau-xe-khach.md (bản hiện có); P00-problem-brief.md 1.0; P01-actors.md 1.0; P02-usecases.md 1.1 (Mục 4, Mục 5); P04-uc-specs/UC-002-book-ticket-online.md 1.0; P04-uc-specs/UC-008-return-ticket.md 1.0; P04-uc-specs/UC-013-cancel-trip.md 1.0; P04-uc-specs/UC-015-check-boarding-ticket.md 1.0; P04-uc-specs/_BR-register.md (BR-01 đến BR-22 trước khi chạy); P05-glossary.md 1.0. Chưa có bản P06 cũ |
| Phạm vi | Toàn hệ thống |

Quy ước trích nguồn theo P00: "Đoạn mở đầu", "Mục n, câu k" chỉ vị trí trong yeu-cau-xe-khach.md. Cách nhóm yêu cầu phi chức năng: FURPS+ (mặc định), cột Nhóm ghi kèm đặc tính ISO/IEC 25010 tương ứng.

## 1. Giới thiệu

Tài liệu này gom các yêu cầu không nằm gọn trong một use case của Hệ thống bán vé xe khách SaoViet Bus: yêu cầu phi chức năng, ràng buộc thiết kế, giao tiếp với hệ thống và thiết bị ngoài, và danh sách quy tắc nghiệp vụ chính thức của toàn hệ thống. Yêu cầu riêng của một use case nằm ở đặc tả use case đó; tài liệu này chứa yêu cầu chung và bảng BR hợp nhất, thay cho bảng BR của từng đặc tả khi có khác biệt. Mã NFR cấp một dãy chung cho Mục 2 đến Mục 5.

## 2. Yêu cầu chức năng dùng chung

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| Không có | | | | | |

## 3. Yêu cầu phi chức năng

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-01 | P - Performance / Performance efficiency | Hệ thống "chịu được" khoảng 2.000 người truy cập cùng lúc vào dịp Tết (ASM-38, ASM-39). | Chưa đo được (Q-22): nguồn không nêu thời gian phản hồi tối đa hay mức đạt. Phần đo được: kiểm thử tải 2.000 phiên truy cập đồng thời (ASM-38) với dữ liệu mẫu theo quy mô của REQ-01, REQ-02 (ASM-40); mức đạt: Chưa quy định (Q-22); cách tính: Chưa quy định (Q-52) | Toàn hệ thống | REQ-66, REQ-01, REQ-02 |
| NFR-02 | R - Reliability / Reliability | Ứng dụng soát vé báo kết quả hợp lệ hoặc không hợp lệ cho mỗi vé được quét khi máy soát vé cầm tay ở vùng mất sóng. | Kiểm thử trên máy soát vé cầm tay không có kết nối mạng, sau khi máy đã nhận danh sách hành khách của chuyến (ASM-33): quét một vé hợp lệ và một vé cho mỗi lý do không hợp lệ (sai chuyến, vé đã huỷ, vé đã soát); mức đạt: máy báo đúng kết quả cho từng vé (có hoặc không). Vé bán sau mốc gửi danh sách: Q-11 | UC-015 | REQ-59 |
| NFR-03 | F - Functionality (bảo mật) / Security | Hệ thống không lưu thông tin thẻ của hành khách (ASM-41). | Xem xét dữ liệu lưu trữ, mã nguồn và nhật ký của sản phẩm; mức đạt: không có dữ liệu thông tin thẻ nào được lưu (có hoặc không); phạm vi "thông tin thẻ": Q-53 | Toàn hệ thống | REQ-68 |

## 4. Ràng buộc thiết kế

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-04 | + Ràng buộc thiết kế / Không tương ứng trực tiếp | Chức năng đặt vé cho hành khách được cung cấp trên website. | Kiểm tra triển khai: hành khách thực hiện được việc đặt vé trên website; mức đạt: có hoặc không | UC-001, UC-002 | REQ-04 |
| NFR-05 | + Ràng buộc thiết kế / Không tương ứng trực tiếp | Chức năng soát vé chạy trên máy soát vé cầm tay Android có đầu quét mã vạch do nhà xe tự trang bị. | Kiểm tra triển khai: ứng dụng soát vé cài đặt và chạy được trên máy soát vé cầm tay Android có đầu quét mã vạch; mức đạt: có hoặc không; model và phiên bản hệ điều hành của máy: Chưa quy định (Q-54) | UC-015 | REQ-56 |

## 5. Giao tiếp ngoài

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-06 | + Giao tiếp / Compatibility | Hệ thống gửi thông tin thanh toán của các chỗ đang giữ tới cổng thanh toán trực tuyến của đối tác (ACT-06) qua API thanh toán và nhận kết quả thanh toán; việc xử lý giao dịch do cổng đảm nhận. | Kiểm thử tích hợp với cổng thanh toán: yêu cầu thanh toán được cổng tiếp nhận và kết quả thanh toán được trả về hệ thống; mức đạt: có hoặc không; giao thức, định dạng dữ liệu, xác thực: Chưa quy định, chưa có tài liệu API (Q-24); hành vi khi cổng không phản hồi: Chưa quy định (Q-55) | UC-003 (được gọi từ UC-002, UC-007) | REQ-15 |
| NFR-07 | + Giao tiếp / Compatibility | Hệ thống gửi yêu cầu hoàn tiền của vé mua trực tuyến tới cổng thanh toán trực tuyến của đối tác (ACT-06) qua API hoàn tiền và nhận kết quả hoàn tiền. | Kiểm thử tích hợp với cổng thanh toán: yêu cầu hoàn tiền được cổng tiếp nhận và kết quả hoàn tiền được trả về hệ thống; mức đạt: có hoặc không; giao thức, định dạng dữ liệu, xác thực: Chưa quy định, chưa có tài liệu API (Q-24); hành vi khi cổng không phản hồi hoặc hoàn không thành công: Chưa quy định (Q-55, Q-37, Q-43) | UC-008, UC-013 | REQ-35 |
| NFR-08 | + Giao tiếp / Compatibility | Hệ thống gửi nội dung tin nhắn (vé của người đi, thông báo huỷ chuyến) tới cổng SMS của nhà mạng (ACT-07) qua API REST; việc chuyển tin nhắn tới thuê bao do cổng đảm nhận. | Kiểm thử tích hợp với cổng SMS: tin nhắn được cổng tiếp nhận để gửi tới số điện thoại người đi; mức đạt: có hoặc không; hành vi khi cổng không nhận hoặc báo lỗi: Chưa quy định (Q-56) | UC-002, UC-013 | REQ-20 |
| NFR-09 | + Giao tiếp / Compatibility | Hệ thống gửi dữ liệu vé, gồm mã vạch thể hiện mã vé, tới máy in vé nhiệt tại quầy (ACT-08) để in vé giấy. | Kiểm thử tích hợp với máy in vé nhiệt: vé giấy được in ra và mã vạch đọc được bằng đầu quét mã vạch (ACT-09) cho đúng mã vé (ASM-34); mức đạt: có hoặc không; kết nối và định dạng dữ liệu in: Chưa quy định (Q-57) | UC-005 | REQ-24 |
| NFR-10 | + Giao tiếp / Compatibility | Ứng dụng soát vé nhận mã vé đọc từ mã vạch trên vé giấy qua đầu quét mã vạch của máy soát vé cầm tay (ACT-09). | Kiểm thử tích hợp trên máy soát vé cầm tay: quét mã vạch của một vé giấy; mức đạt: ứng dụng nhận đúng mã vé (có hoặc không); vé mua trực tuyến không có vé giấy: Q-04, ASM-34; model đầu quét: Chưa quy định (Q-54) | UC-015 | REQ-55, REQ-56 |

## 6. Quy tắc nghiệp vụ

Bảng hợp nhất từ sổ BR và bảng BR của UC-002, UC-008, UC-013, UC-015; BR-23 đến BR-33 cấp mới ở P06 từ các REQ loại Quy tắc nghiệp vụ của P00 chưa có BR. Không có BR bị gộp hoặc loại. Cột Áp dụng cho UC giữ nguyên từ sổ BR hoặc theo ma trận REQ --> UC của P02 (BR mới); UC khác chưa có đặc tả P04 ghi ở Ghi chú.

| BR | Quy tắc | Loại | Áp dụng cho UC | REQ | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|
| BR-01 | Mỗi lần đặt vé trực tuyến được chọn tối đa 5 chỗ. | Ràng buộc | UC-002 | REQ-08 | Hiệu lực | P04 UC-002. Q-09: chưa rõ giới hạn có áp dụng cho bán vé tại quầy và đặt chỗ qua điện thoại (UC-004, UC-005 chờ Q-09). |
| BR-02 | Trên một chuyến, hai vé không được cùng một chỗ. | Ràng buộc | UC-002 | REQ-67 | Hiệu lực | P04 UC-002. Theo P02 còn áp dụng UC-004, UC-005, UC-007 (REQ-67, chưa có P04). Có đề xuất diễn đạt lại (xem Đề xuất sửa artifact trước; Q-36). |
| BR-03 | Một chỗ của chuyến là còn trống khi chỗ đó chưa có vé và không đang được giữ cho một lần đặt chưa hết thời hạn giữ chỗ. | Suy luận | UC-002, UC-008 | REQ-12, REQ-16, REQ-67 | Hiệu lực | P04 UC-002, UC-008. Theo P02 còn áp dụng UC-004, UC-005, UC-007 (REQ-67, chưa có P04). Có đề xuất diễn đạt lại (Q-36, Q-05, ASM-05). |
| BR-04 | Giá vé được đặt theo tuyến và loại xe. | Sự kiện | UC-002 | REQ-52 | Hiệu lực | P04 UC-002. Theo P02 còn áp dụng UC-016 (REQ-52, chưa có P04). Có đề xuất dùng thuật ngữ GL-09. |
| BR-05 | Giá một vé bằng giá vé theo tuyến và loại xe của chuyến nhân với (1 + mức tăng giá lễ Tết theo phần trăm) khi ngày xuất bến của chuyến thuộc khoảng ngày có mức tăng giá áp dụng cho chuyến (ASM-12); ngoài khoảng ngày đó, mức tăng bằng 0%. | Tính toán | UC-002 | REQ-52, REQ-53 | Hiệu lực | P04 UC-002. ASM-12; Q-19, Q-20. Theo P02 còn áp dụng UC-017 (REQ-53, chưa có P04). Giới hạn tối đa của mức tăng ở BR-32. |
| BR-06 | Tổng tiền của một lần đặt vé bằng tổng giá vé của các chỗ đã chọn trong lần đặt đó. | Tính toán | UC-002 | REQ-12, REQ-14 | Hiệu lực | P04 UC-002. Theo P02 còn áp dụng UC-003 (REQ-14, chưa có P04). |
| BR-07 | Các chỗ đã chọn được giữ chờ thanh toán trực tuyến trong 10 phút kể từ khi bắt đầu giữ. | Ràng buộc | UC-002 | REQ-13 | Hiệu lực | P04 UC-002. Q-10 (thanh toán thành công sau khi hết thời hạn giữ chỗ). |
| BR-08 | Khi hết thời hạn giữ chỗ (BR-07) mà chưa thanh toán thành công, các chỗ đang giữ của lần đặt được trả lại trạng thái còn trống cho người khác chọn. | Kích hoạt hành động | UC-002 | REQ-16 | Hiệu lực | P04 UC-002. |
| BR-09 | Khi thanh toán trực tuyến cho các chỗ đang giữ thành công, hệ thống phát hành vé cho các chỗ đó. | Kích hoạt hành động | UC-002 | REQ-17 | Hiệu lực | P04 UC-002. |
| BR-10 | Mỗi chỗ được phát hành thành đúng một vé có một mã vé. | Ràng buộc | UC-002, UC-008, UC-013, UC-015 | REQ-18 | Hiệu lực | P04 UC-002, UC-008, UC-013, UC-015. Theo P02 còn áp dụng UC-005 (REQ-18, chưa có P04). |
| BR-11 | Vé chỉ được trả qua kênh đã mua vé: vé mua trực tuyến do hành khách trả trên website, vé mua tại quầy (gồm vé đặt qua điện thoại đã thanh toán tại quầy) do nhân viên bán vé trả tại quầy (ASM-02). | Ràng buộc | UC-008 | REQ-29, REQ-34, REQ-36 | Hiệu lực | P04 UC-008. ASM-02; Q-02. Có đề xuất sửa cách gọi "vé đặt qua điện thoại". |
| BR-12 | Vé không được trả khi thời gian còn lại trước giờ xuất bến của chuyến dưới 4 giờ. | Ràng buộc | UC-008 | REQ-33 | Hiệu lực | P04 UC-008. Không áp dụng cho vé của chuyến bị huỷ (BR-17; P00 mục 5 dòng 28). Q-39. |
| BR-13 | Vé được trả khi thời gian còn lại trước giờ xuất bến của chuyến từ 24 giờ trở lên được hoàn 90% giá vé. | Tính toán | UC-008 | REQ-31 | Hiệu lực | P04 UC-008. Q-38 (giá vé dùng để tính mức hoàn), Q-39. |
| BR-14 | Vé được trả khi thời gian còn lại trước giờ xuất bến của chuyến từ 4 giờ đến dưới 24 giờ được hoàn 50% giá vé. | Tính toán | UC-008 | REQ-32 | Hiệu lực | P04 UC-008. Q-38, Q-39. |
| BR-15 | Vé mua trực tuyến được hoàn tiền qua cổng thanh toán trực tuyến của đối tác. | Ràng buộc | UC-008, UC-013 (ASM-28) | REQ-34 | Hiệu lực | P04 UC-008; UC-013 áp dụng theo ASM-28 (Q-14). Q-37, Q-43. |
| BR-16 | Vé mua tại quầy được hoàn bằng tiền mặt tại quầy. | Ràng buộc | UC-008, UC-013 (ASM-28) | REQ-36 | Hiệu lực | P04 UC-008; UC-013 áp dụng theo ASM-28 (Q-14). |
| BR-17 | Số tiền hoàn của một vé thuộc chuyến bị nhà xe huỷ bằng 100% giá vé. | Tính toán | UC-013 | REQ-50 | Hiệu lực | P04 UC-013. Q-14, Q-40. |
| BR-18 | Khi chuyến bị huỷ, mọi hành khách đã có vé còn hiệu lực của chuyến được báo việc huỷ chuyến qua SMS (ASM-27). | Kích hoạt hành động | UC-013 | REQ-48 | Hiệu lực | P04 UC-013. ASM-27; Q-15, Q-42. Có đề xuất sửa cách gọi "hành khách". |
| BR-19 | Khi chuyến bị huỷ, mọi hành khách đã có vé còn hiệu lực của chuyến được hoàn tiền theo BR-17 (ASM-27). | Kích hoạt hành động | UC-013 | REQ-49 | Hiệu lực | P04 UC-013. ASM-27; Q-14, Q-15. Có đề xuất sửa cách gọi "hành khách". |
| BR-20 | Khi soát vé lên xe, vé không thuộc chuyến đang soát là vé không hợp lệ với lý do sai chuyến. | Suy luận | UC-015 | REQ-58 | Hiệu lực | P04 UC-015. Q-45. |
| BR-21 | Khi soát vé lên xe, vé đã bị huỷ là vé không hợp lệ với lý do vé đã huỷ. | Suy luận | UC-015 | REQ-58 | Hiệu lực | P04 UC-015. Vé đã huỷ gồm vé đã trả, vé của chuyến bị huỷ, vé cũ sau khi đổi (ASM-20, ASM-26, ASM-36); Q-21, Q-36, Q-47. |
| BR-22 | Khi soát vé lên xe, vé đã được soát trước đó là vé không hợp lệ với lý do vé đã soát. | Suy luận | UC-015 | REQ-58 | Hiệu lực | P04 UC-015. Q-47. |
| BR-23 | Vé bán tại quầy cho khách mua trực tiếp được thanh toán bằng tiền mặt. | Sự kiện | UC-005 | REQ-22 | Hiệu lực | P06; UC theo P02 (chưa có P04). |
| BR-24 | Đặt chỗ qua điện thoại phải được thanh toán tại quầy chậm nhất 60 phút trước giờ xuất bến của chuyến. | Ràng buộc | UC-004, UC-005, UC-006 | REQ-27 | Hiệu lực | P06; UC theo P02 (chưa có P04). Nguồn gọi là "vé đặt qua điện thoại"; dùng thuật ngữ GL-07 (ASM-05, Q-05). |
| BR-25 | Vé chỉ được đổi sang chuyến khác cùng tuyến. | Ràng buộc | UC-007 | REQ-37 | Hiệu lực | P06; UC theo P02 (chưa có P04). |
| BR-26 | Mỗi vé chỉ được đổi một lần. | Ràng buộc | UC-007 | REQ-38 | Hiệu lực | P06; UC theo P02 (chưa có P04). Q-21. |
| BR-27 | Vé chỉ được đổi chậm nhất 4 giờ trước giờ xuất bến. | Ràng buộc | UC-007 | REQ-39 | Hiệu lực | P06; UC theo P02 (chưa có P04). Q-13: giờ xuất bến của chuyến cũ hay chuyến mới. |
| BR-28 | Khi vé mới đắt hơn vé cũ, hành khách trả thêm phần chênh lệch giữa giá vé mới và giá vé cũ. | Tính toán | UC-007, UC-003 | REQ-40 | Hiệu lực | P06; UC theo P02 (chưa có P04). Q-12, Q-28, ASM-10. |
| BR-29 | Một xe không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-012 | REQ-43 | Hiệu lực | P06; UC theo P02 (chưa có P04). ASM-03; Q-17. |
| BR-30 | Một tài xế không được xếp vào hai chuyến có thời gian chạy chồng nhau. | Ràng buộc | UC-012 | REQ-44 | Hiệu lực | P06; UC theo P02 (chưa có P04). ASM-03; Q-16, Q-17. |
| BR-31 | Tài xế không được lái quá 10 giờ trong một ngày. | Ràng buộc | UC-012 | REQ-45 | Hiệu lực | P06; UC theo P02 (chưa có P04). ASM-03; Q-16, Q-17, Q-18. |
| BR-32 | Mức tăng giá lễ Tết theo phần trăm tối đa là 30%. | Ràng buộc | UC-017 | REQ-54 | Hiệu lực | P06; UC theo P02 (chưa có P04). Liên quan BR-05. |
| BR-33 | Danh sách hành khách của chuyến được gửi về máy soát vé cầm tay vào thời điểm 15 phút trước giờ xuất bến của chuyến. | Kích hoạt hành động | UC-014 | REQ-62 | Hiệu lực | P06; UC theo P02 (chưa có P04). Q-11. |

## 7. Ma trận truy vết

REQ --> NFR/BR:

| REQ | Loại REQ | NFR / BR | Ghi chú |
|---|---|---|---|
| REQ-01 | Dữ liệu | NFR-01 | Không phải NFR riêng; dùng làm điều kiện dữ liệu mẫu khi đo (ASM-40) |
| REQ-02 | Dữ liệu | NFR-01 | Như REQ-01 |
| REQ-04 | Ràng buộc | NFR-04 | Không có |
| REQ-08 | Quy tắc nghiệp vụ | BR-01 | Không có |
| REQ-13 | Quy tắc nghiệp vụ | BR-07 | Không có |
| REQ-15 | Giao tiếp ngoài | NFR-06 | Không có |
| REQ-18 | Quy tắc nghiệp vụ | BR-10 | Không có |
| REQ-20 | Giao tiếp ngoài | NFR-08 | Không có |
| REQ-22 | Quy tắc nghiệp vụ | BR-23 | BR cấp mới ở P06 |
| REQ-24 | Giao tiếp ngoài | NFR-09 | Không có |
| REQ-27 | Quy tắc nghiệp vụ | BR-24 | BR cấp mới ở P06 |
| REQ-31 | Quy tắc nghiệp vụ | BR-13 | Không có |
| REQ-32 | Quy tắc nghiệp vụ | BR-14 | Không có |
| REQ-33 | Quy tắc nghiệp vụ | BR-12 | Không có |
| REQ-34 | Quy tắc nghiệp vụ | BR-15 | Không có |
| REQ-35 | Giao tiếp ngoài | NFR-07 | Không có |
| REQ-36 | Quy tắc nghiệp vụ | BR-16 | Không có |
| REQ-37 | Quy tắc nghiệp vụ | BR-25 | BR cấp mới ở P06 |
| REQ-38 | Quy tắc nghiệp vụ | BR-26 | BR cấp mới ở P06 |
| REQ-39 | Quy tắc nghiệp vụ | BR-27 | BR cấp mới ở P06 |
| REQ-40 | Quy tắc nghiệp vụ | BR-28 | BR cấp mới ở P06 |
| REQ-43 | Quy tắc nghiệp vụ | BR-29 | BR cấp mới ở P06 |
| REQ-44 | Quy tắc nghiệp vụ | BR-30 | BR cấp mới ở P06 |
| REQ-45 | Quy tắc nghiệp vụ | BR-31 | BR cấp mới ở P06 |
| REQ-50 | Quy tắc nghiệp vụ | BR-17 | Không có |
| REQ-52 | Quy tắc nghiệp vụ | BR-04, BR-05 | Không có |
| REQ-54 | Quy tắc nghiệp vụ | BR-32 | BR cấp mới ở P06 |
| REQ-56 | Ràng buộc | NFR-05, NFR-10 | Không có |
| REQ-58 | Quy tắc nghiệp vụ | BR-20, BR-21, BR-22 | Không có |
| REQ-59 | Phi chức năng | NFR-02 | Không có |
| REQ-62 | Quy tắc nghiệp vụ | BR-33 | BR cấp mới ở P06 |
| REQ-66 | Phi chức năng | NFR-01 | Không có |
| REQ-67 | Quy tắc nghiệp vụ | BR-02, BR-03 | Không có |
| REQ-68 | Ràng buộc | NFR-03 | Không có |

UC --> NFR/BR (NFR-01 và NFR-03 áp dụng toàn hệ thống nên không lặp ở từng dòng; BR ghi "(P02)" là BR gắn với UC theo ma trận REQ --> UC của P02, UC chưa có đặc tả P04):

| UC | NFR | BR |
|---|---|---|
| UC-001 | NFR-04 | - |
| UC-002 | NFR-04, NFR-08 | BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10 |
| UC-003 | NFR-06 | BR-06 (P02), BR-28 (P02) |
| UC-004 | - | BR-02 (P02), BR-03 (P02), BR-24 (P02) |
| UC-005 | NFR-09 | BR-02 (P02), BR-03 (P02), BR-10 (P02), BR-23 (P02), BR-24 (P02) |
| UC-006 | - | BR-24 (P02) |
| UC-007 | - | BR-02 (P02), BR-03 (P02), BR-25 (P02), BR-26 (P02), BR-27 (P02), BR-28 (P02) |
| UC-008 | NFR-07 | BR-03, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16 |
| UC-009 | - | - |
| UC-010 | - | - |
| UC-011 | - | - |
| UC-012 | - | BR-29 (P02), BR-30 (P02), BR-31 (P02) |
| UC-013 | NFR-07, NFR-08 | BR-10, BR-15, BR-16, BR-17, BR-18, BR-19 |
| UC-014 | - | BR-33 (P02) |
| UC-015 | NFR-02, NFR-05, NFR-10 | BR-10, BR-20, BR-21, BR-22 |
| UC-016 | - | BR-04 (P02) |
| UC-017 | - | BR-05 (P02), BR-32 (P02) |
| UC-018 | - | - |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-51 | Các số liệu quy mô có chữ "khoảng" (2.000 người truy cập cùng lúc, 80 chuyến mỗi ngày, 50 xe giường nằm, 20 xe ghế ngồi) là mức tải tối thiểu hệ thống phải đáp ứng hay giá trị gần đúng; có cần dự phòng thêm bao nhiêu? (Đúng bằng số nêu / Có dự phòng với tỉ lệ do bên liên quan chọn) | NFR-01; ASM-38, ASM-40; P09 | Mục 10, câu 1: "khoảng 2.000 người truy cập cùng lúc"; Đoạn mở đầu, câu 1-2 |
| Q-52 | Thời gian phản hồi tối đa ở Q-22 được tính theo cách nào? (Trung bình / Một tỉ lệ phần trăm các yêu cầu / Mọi yêu cầu) | NFR-01; Q-22; P09 | Mục 10, câu 1: "phải chịu được" (không nêu cách đo) |
| Q-53 | "Thông tin thẻ" gồm những dữ liệu nào, và mã tham chiếu giao dịch do cổng thanh toán cấp (cần cho việc hoàn tiền) có được lưu không? (Mã tham chiếu giao dịch được lưu, không phải thông tin thẻ / Không được lưu bất kỳ dữ liệu nào liên quan tới thẻ hay giao dịch thẻ) | NFR-03; ASM-41; UC-003, UC-008, UC-013; P13 | Mục 10, câu 3: "Hệ thống không lưu thông tin thẻ của hành khách" |
| Q-54 | Máy soát vé cầm tay Android của nhà xe là model nào, chạy phiên bản hệ điều hành nào, và đầu quét mã vạch hỗ trợ loại mã vạch nào? | NFR-05, NFR-10; UC-015; P09, P11b | Mục 8, câu 1; project-profile.md, HE_THONG_NGOAI: "Máy soát vé cầm tay Android có đầu quét mã vạch, do nhà xe tự trang bị" |
| Q-55 | Khi cổng thanh toán không phản hồi kết quả thanh toán hoặc hoàn tiền, hệ thống xử lý lần đặt hoặc yêu cầu hoàn thế nào? (Chờ tới hết thời hạn giữ chỗ rồi trả chỗ / Coi là không thành công ngay / Do nhân viên nhà xe xử lý) | NFR-06, NFR-07; UC-002, UC-008, UC-013; liên quan Q-10, Q-31, Q-37, Q-43 | Mục 3, câu 1-2; project-profile.md, HE_THONG_NGOAI: "chưa có tài liệu API" |
| Q-56 | Khi cổng SMS không nhận hoặc báo lỗi khi gửi tin nhắn vé hoặc tin nhắn báo huỷ chuyến, hệ thống xử lý thế nào? (Gửi lại tự động / Nhân viên nhà xe gửi lại / Hiển thị mã vé cho hành khách trên website) | NFR-08; UC-002, UC-013 | Mục 3, câu 3; Mục 6, câu 4 (không nêu trường hợp gửi lỗi) |
| Q-57 | Máy in vé nhiệt tại quầy là model nào, kết nối với máy của nhân viên bán vé bằng cách nào, và có tài liệu giao tiếp không? | NFR-09; UC-005; P11b | Mục 4, câu 1; project-profile.md, HE_THONG_NGOAI: "Máy in vé nhiệt tại quầy" |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| ASM-38 | Các số liệu có chữ "khoảng" ở REQ-01, REQ-02, REQ-66 được dùng đúng giá trị nguồn nêu làm mức kiểm thử, không cộng dung sai. | Nguồn chỉ nêu "khoảng" mà không cho dung sai; dùng đúng giá trị nguồn để không tự thêm ngưỡng. Chờ Q-51 | NFR-01; ASM-40 |
| ASM-39 | "Chịu được" ở REQ-66 nghĩa là hệ thống xử lý hoàn tất các yêu cầu của 2.000 phiên đồng thời mà không phát sinh lỗi hệ thống; ngưỡng thời gian phản hồi chưa đề xuất con số vì nguồn không có căn cứ. | Mục 10, câu 1 chỉ nêu "chịu được", không có đại lượng đo. Chờ Q-22, Q-52 | NFR-01 |
| ASM-40 | Dữ liệu mẫu khi đo NFR-01 có quy mô theo REQ-01 và REQ-02: 12 tuyến, 3 bến xe, khoảng 80 chuyến mỗi ngày, khoảng 50 xe giường nằm 40 chỗ và 20 xe ghế ngồi 29 chỗ. | Ghi chú của REQ-01 ở P00 nêu số liệu quy mô dùng làm điều kiện dung lượng ở P06; nguồn không nêu điều kiện đo của Mục 10. Chờ Q-51 | NFR-01; REQ-01, REQ-02 |
| ASM-41 | "Thông tin thẻ" gồm số thẻ, tên chủ thẻ, ngày hết hạn và mã xác thực của thẻ; mã tham chiếu giao dịch do cổng thanh toán cấp không phải thông tin thẻ và được phép lưu để phục vụ hoàn tiền. | Nguồn không định nghĩa "thông tin thẻ"; việc hoàn tiền qua cổng (Mục 5, câu 3) cần liên kết tới giao dịch đã thanh toán. Chờ Q-53 | NFR-03; NFR-07 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 (UC-002), sổ BR | BR-02, BR-03 | Hiểu theo nghĩa chữ, "hai vé không được cùng một chỗ" và "chưa có vé" chặn việc bán lại chỗ của vé đã trả hoặc thuộc chuyến bị huỷ (đề xuất của P04 UC-008; ASM-20, ASM-26, Q-36). BR-03 không loại chỗ của đặt chỗ qua điện thoại chưa thanh toán, trái GL-03, GL-11 và ASM-05 (Q-05). P06 giữ nguyên nội dung đã chốt. | Sau khi Q-36 và Q-05 được trả lời, diễn đạt BR-02 là "hai vé còn hiệu lực không được cùng một chỗ" và BR-03 là chỗ "chưa có vé còn hiệu lực và không đang được giữ cho lần đặt chưa hết thời hạn giữ chỗ hoặc đặt chỗ qua điện thoại chưa thanh toán", rồi cập nhật bảng BR ở Mục 6 và sổ BR |
| P04 (UC-002), sổ BR | BR-04 | "Giá vé" ở BR-04 chỉ mức giá đặt theo tuyến và loại xe, trùng tên GL-08 Giá vé (P05) | Dùng thuật ngữ GL-09 "Giá vé theo tuyến và loại xe" |
| P04 (UC-008, UC-013), sổ BR | BR-11 | "vé đặt qua điện thoại đã thanh toán tại quầy" là từ đồng nghĩa không dùng của GL-07 (P05) | Dùng "vé thanh toán tại quầy cho đặt chỗ qua điện thoại" |
| P04 (UC-013), sổ BR | BR-18, BR-19 | "mọi hành khách đã có vé còn hiệu lực" chỉ người đi của vé, không chỉ ACT-01 Hành khách (P05) | Dùng "người đi của mọi vé còn hiệu lực" (GL-26, GL-38) |
| P04 (UC-008), sổ BR | BR-12, BR-13, BR-14 | Phát biểu "Vé không được trả" có thể bị đọc là áp dụng cả vé của chuyến bị huỷ khi còn dưới 4 giờ, trái BR-17 và BR-19; P00 mục 5 dòng 28 và UC-013 mục 8 đã xác định hai nhóm không giao nhau | Ghi rõ phạm vi "Khi hành khách trả vé" ở BR-12 đến BR-14 để loại phạm vi huỷ chuyến |

## Vấn đề còn mở

- Target 4: NFR-01 có ngưỡng 2.000 từ nguồn nhưng nguồn không có mức đạt, thời gian phản hồi và cách tính. Đã ghi "Chưa đo được" kèm Q-22, Q-52 và các ASM-38 đến ASM-40; không tự đặt con số.
- Mục 2 để "Không có": REQ-19 và REQ-48 (gửi SMS) dùng chung kênh cổng SMS nhưng mỗi REQ là bước của một use case riêng (UC-002, UC-013); phần dùng chung đã ghi ở Mục 5 (NFR-08). Nguồn và hồ sơ dự án không có REQ về nhật ký thao tác, phân quyền, đa ngôn ngữ hay định dạng tiền tệ; việc đăng nhập của nhân viên chỉ có ASM-09 và Q-27 ở P02, không có REQ nên không đưa vào.
- Chọn giữa hai quy tắc (C9): P00 xếp REQ-68 loại Ràng buộc, còn F4 xếp NFR dạng có/không "không lưu dữ liệu X" và F3 xếp bảo mật vào nhóm F, trong khi F5 giới hạn Mục 4 ở công nghệ, nền tảng, chuẩn, luật. Đã xếp NFR-03 ở Mục 3 nhóm Security; REQ-68 vẫn nằm trong ma trận truy vết.
- Chọn giữa hai quy tắc (C9): F6 yêu cầu cột lõi giữ nguyên từ sổ BR, đồng thời yêu cầu hợp nhất danh sách UC áp dụng. Đã giữ nguyên Áp dụng cho UC của 22 BR cũ và ghi UC bổ sung theo P02 (REQ-67, REQ-52, REQ-53, REQ-14, REQ-18) ở Ghi chú; ma trận UC --> NFR/BR đánh dấu (P02).
- BR-33 (REQ-62) được P00 xếp loại Quy tắc nghiệp vụ nhưng nội dung là mốc thời gian của một xử lý tự động; đã giữ theo P00 và Target 8, xếp Loại Kích hoạt hành động.
- NFR-07 và NFR-08 gộp các dòng "Yêu cầu đặc biệt" giống nhau của hai đặc tả P04 (UC-008 và UC-013 cho REQ-35; UC-002 và UC-013 cho REQ-20) thành một NFR với cột Áp dụng cho ghi cả hai UC.
- Các đề xuất bổ sung REQ vào P02 Bảng 4b mà P04 UC-002, UC-008, UC-013, UC-015 đã nêu chưa được áp dụng; cột Áp dụng cho UC của BR mới và ma trận UC --> NFR/BR dựa trên P02 1.1 và bảng BR của P04, chưa phản ánh các đề xuất đó.
