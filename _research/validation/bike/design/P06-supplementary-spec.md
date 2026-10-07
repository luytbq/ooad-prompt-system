# P06 - Đặc tả bổ sung - Hệ thống cho thuê xe đạp công cộng CityBike

| Thuộc tính | Giá trị |
|---|---|
| Bước | P06 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; yeu-cau-xe-dap.md; P00 1.0; P01 1.0; P02 1.0 (Mục 4, Mục 5); P04 UC-005, UC-007, UC-009, UC-013 1.0; _BR-register.md (BR-01 đến BR-10); P05 1.0 |
| Phạm vi | Toàn hệ thống |

Placeholder: MO_HINH_CHAT_LUONG = Không có (FURPS+); YEU_CAU_BO_SUNG = Không có.

## 1. Giới thiệu

Tài liệu này gom các yêu cầu không thuộc riêng một use case của Hệ thống cho thuê xe đạp công cộng CityBike: yêu cầu phi chức năng, ràng buộc thiết kế, giao tiếp với cổng thanh toán và ụ khoá, và danh sách quy tắc nghiệp vụ chính thức. Yêu cầu riêng của một use case nằm ở đặc tả P04 của use case đó; các đặc tả chỉ dẫn mã BR ở đây.

## 2. Yêu cầu chức năng dùng chung

Không có

## 3. Yêu cầu phi chức năng

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-01 | P - Performance / Performance efficiency | Số xe sẵn sàng và số ụ trống trên bản đồ trạm được cập nhật "theo thời gian thực". | Chưa đo được (Q-12): cần chốt độ trễ tối đa giữa thay đổi tại ụ khoá và hiển thị trên bản đồ | UC-004 | REQ-06 |
| NFR-02 | P - Performance / Performance efficiency | Lệnh mở khoá tới ụ khoá trong không quá 2 giây kể từ khi người thuê xe quét mã QR. | Mức đạt: không quá 2 giây; phạm vi thời gian có gồm tạm giữ tiền qua cổng thanh toán: Chưa quy định (Q-13); phương pháp, điều kiện tải, cách tính: Chưa quy định (Q-28) | UC-005 | REQ-58 |
| NFR-03 | P - Performance / Performance efficiency | Hệ thống phục vụ được 1.500 chuyến đi đồng thời. | Chưa đo được (Q-14): cần chốt tiêu chí "phục vụ được" khi có 1.500 chuyến đang diễn ra | Toàn hệ thống | REQ-59 |
| NFR-04 | F - Functionality (Security) / Security | Hệ thống không lưu số thẻ thanh toán. | Mức đạt: không có dữ liệu nào của hệ thống chứa số thẻ thanh toán; phương pháp kiểm chứng: Chưa quy định (Q-29) | UC-002 và toàn hệ thống | REQ-60 |

## 4. Ràng buộc thiết kế

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-05 | + Ràng buộc thiết kế | Người thuê xe sử dụng hệ thống qua ứng dụng di động. | Mức đạt: các UC của ACT-01 thực hiện được từ ứng dụng di động; phương pháp: Chưa quy định (Q-29) | UC-001 đến UC-008 | REQ-01 |

## 5. Giao tiếp ngoài

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-06 | + Giao tiếp / Compatibility (Interoperability) | Hệ thống gọi API của cổng thanh toán của ngân hàng đối tác (ACT-07) để liên kết thẻ, tạm giữ tiền, thu tiền từ khoản tạm giữ, huỷ tạm giữ và hoàn tiền; tài liệu API chưa có (hồ sơ dự án). | Mức đạt: mỗi thao tác trên được cổng thanh toán chấp nhận; phương pháp và môi trường kiểm thử: Chưa quy định (Q-29); hành vi khi cổng không phản hồi: Chưa quy định (Q-08, Q-23) | UC-002, UC-005, UC-007, UC-009, UC-017 | REQ-03, REQ-62 |
| NFR-07 | + Giao tiếp / Compatibility (Interoperability) | Hệ thống trao đổi với ụ khoá (ACT-08) qua giao thức MQTT do nhà cung cấp thiết bị quy định: gửi lệnh mở khoá, lệnh khoá lại; nhận báo xe được rút ra, xe được đưa vào, thao tác bằng thẻ nhân viên; tài liệu giao thức chưa có (hồ sơ dự án). | Mức đạt: các thông điệp trên được trao đổi đúng giao thức của nhà cung cấp; phương pháp: Chưa quy định (Q-29) | UC-005, UC-007, UC-014 | REQ-12, REQ-18, REQ-46, REQ-63 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Áp dụng cho UC | REQ | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|
| BR-01 | Tài khoản chỉ được thuê xe sau khi đã liên kết một thẻ thanh toán. | Ràng buộc | UC-005 | REQ-04 | Hiệu lực | P04 UC-005 |
| BR-02 | Tài khoản chỉ được thuê xe khi không có chuyến đi đang diễn ra. | Ràng buộc | UC-005 | REQ-08 | Hiệu lực | P04 UC-005 |
| BR-03 | Tài khoản chỉ được thuê xe khi không nợ cước. | Ràng buộc | UC-005 | REQ-09 | Hiệu lực | P04 UC-005; Q-02 |
| BR-04 | Xe ở trạng thái "Chờ kiểm tra" không được cho thuê. | Ràng buộc | UC-005, UC-008 | REQ-37 | Hiệu lực | P04 UC-005; UC-008 từ ma trận P02 |
| BR-05 | Số tiền tạm giữ cho mỗi lần thuê xe là 200.000 đồng. | Sự kiện | UC-005, UC-007 | REQ-11 | Hiệu lực | P04 UC-005 |
| BR-06 | Thời hạn chờ rút xe là 60 giây; quá thời hạn mà xe chưa được rút thì ụ khoá bị khoá lại và lệnh tạm giữ bị huỷ. | Kích hoạt hành động | UC-005 | REQ-14, REQ-15, REQ-16 | Hiệu lực | P04 UC-005; Q-10. Nội dung dùng "lệnh tạm giữ", đồng nghĩa không dùng của GL-08 (xem Đề xuất) |
| BR-07 | Cước chuyến đi miễn phí 30 phút đầu, sau đó 5.000 đồng cho mỗi 15 phút hoặc phần lẻ của 15 phút. | Tính toán | UC-007 | REQ-21 | Hiệu lực | P04 UC-007; quan hệ với bảng giá cước Q-15 |
| BR-08 | Người thuê xe được trả xe vào một ụ trống bất kỳ ở bất kỳ trạm nào. | Sự kiện | UC-007 | REQ-17 | Hiệu lực | P04 UC-007 |
| BR-09 | Chuyến đi kéo dài quá 24 giờ thì xe của chuyến bị coi là thất lạc. | Suy luận | UC-009 | REQ-28, REQ-29 | Hiệu lực | P04 UC-009 |
| BR-10 | Khi xe bị coi là thất lạc, toàn bộ số tiền tạm giữ của chuyến bị thu và tài khoản của người thuê xe bị khoá. | Kích hoạt hành động | UC-009 | REQ-30, REQ-31 | Hiệu lực | P04 UC-009 |
| BR-11 | Thời gian miễn phí cộng thêm cho một yêu cầu là 15 phút. | Sự kiện | UC-006 | REQ-26 | Hiệu lực | P06; Q-05 |
| BR-12 | Mỗi chuyến đi chỉ được yêu cầu thêm thời gian miễn phí một lần. | Ràng buộc | UC-006 | REQ-27 | Hiệu lực | P06 |
| BR-13 | Người thuê xe chỉ được báo xe hỏng khi trả xe hoặc trong vòng 10 phút sau khi trả xe. | Ràng buộc | UC-008 | REQ-34 | Hiệu lực | P06 |
| BR-14 | Trạm có dưới 20% số ụ có xe là trạm sắp hết xe. | Suy luận | UC-012 | REQ-42 | Hiệu lực | P06 |
| BR-15 | Trạm có "trên 90%" số ụ có xe là trạm sắp đầy. | Suy luận | UC-012 | REQ-43 | Hiệu lực | P06; Q-11 |
| BR-16 | Mỗi lần điều chỉnh cước phải ghi lý do. | Ràng buộc | UC-017 | REQ-49 | Hiệu lực | P06 |

## 7. Ma trận truy vết

REQ --> NFR/BR

| REQ | Loại REQ | NFR / BR | Ghi chú |
|---|---|---|---|
| REQ-01 | Ràng buộc | NFR-05 | Không có |
| REQ-04 | Quy tắc nghiệp vụ | BR-01 | Không có |
| REQ-06 | Phi chức năng | NFR-01 | Không có |
| REQ-08 | Quy tắc nghiệp vụ | BR-02 | Không có |
| REQ-09 | Quy tắc nghiệp vụ | BR-03 | Không có |
| REQ-11 | Quy tắc nghiệp vụ | BR-05 | Không có |
| REQ-16 | Quy tắc nghiệp vụ | BR-06 | Không có |
| REQ-18 | Giao tiếp ngoài | NFR-07 | Không có |
| REQ-21 | Quy tắc nghiệp vụ | BR-07 | Không có |
| REQ-26 | Quy tắc nghiệp vụ | BR-11 | Không có |
| REQ-27 | Quy tắc nghiệp vụ | BR-12 | Không có |
| REQ-29 | Quy tắc nghiệp vụ | BR-09 | Không có |
| REQ-34 | Quy tắc nghiệp vụ | BR-13 | Không có |
| REQ-37 | Quy tắc nghiệp vụ | BR-04 | Không có |
| REQ-42 | Quy tắc nghiệp vụ | BR-14 | Không có |
| REQ-43 | Quy tắc nghiệp vụ | BR-15 | Không có |
| REQ-49 | Quy tắc nghiệp vụ | BR-16 | Không có |
| REQ-58 | Phi chức năng | NFR-02 | Không có |
| REQ-59 | Phi chức năng | NFR-03 | Không có |
| REQ-60 | Phi chức năng | NFR-04 | Không có |
| REQ-62 | Giao tiếp ngoài | NFR-06 | Không có |
| REQ-63 | Giao tiếp ngoài | NFR-07 | Không có |

UC --> NFR/BR

| UC | NFR | BR |
|---|---|---|
| UC-001 Đăng ký tài khoản | NFR-05 | - |
| UC-002 Liên kết thẻ thanh toán | NFR-04, NFR-05, NFR-06 | - |
| UC-003 Đăng nhập | NFR-05 | - |
| UC-004 Xem bản đồ trạm | NFR-01, NFR-05 | - |
| UC-005 Thuê xe | NFR-02, NFR-05, NFR-06, NFR-07 | BR-01, BR-02, BR-03, BR-04, BR-05, BR-06 |
| UC-006 Xin thêm thời gian miễn phí | NFR-05 | BR-11, BR-12 |
| UC-007 Trả xe | NFR-05, NFR-06, NFR-07 | BR-05, BR-07, BR-08 |
| UC-008 Báo xe hỏng | NFR-05 | BR-04, BR-13 |
| UC-009 Ghi nhận xe thất lạc | NFR-06 | BR-09, BR-10 |
| UC-010 Tra cứu xe chờ kiểm tra | - | - |
| UC-011 Ghi nhận kết quả kiểm tra xe | - | - |
| UC-012 Xem trạm sắp hết xe, sắp đầy | - | BR-14, BR-15 |
| UC-013 Lập lệnh điều chuyển | - | - |
| UC-014 Ghi nhận xe điều chuyển tại ụ | NFR-07 | - |
| UC-015 Theo dõi lệnh điều chuyển | - | - |
| UC-016 Tra cứu lịch sử chuyến đi | - | - |
| UC-017 Điều chỉnh cước | NFR-06 | BR-16 |
| UC-018 Mở khoá tài khoản | - | - |
| UC-019 đến UC-023 (Danh mục) | - | - |
| UC-024 Xem báo cáo hằng tuần | - | - |

NFR-03 áp dụng toàn hệ thống, không liệt kê theo từng UC.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-28 | Ngưỡng 2 giây của lệnh mở khoá được đo trong điều kiện tải nào (ví dụ khi có 1.500 chuyến đồng thời) và tính theo từng lần hay theo tỉ lệ số lần đạt? | NFR-02 | Mục 13 |
| Q-29 | Các yêu cầu không lưu số thẻ, dùng ứng dụng di động, tích hợp cổng thanh toán và ụ khoá được nghiệm thu bằng phương pháp nào (kiểm tra dữ liệu, kiểm thử tích hợp với môi trường thử của đối tác)? | NFR-04 đến NFR-07 | Mục 13, Mục 14 |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | BR-06 (UC-005) | Nội dung dùng "lệnh tạm giữ", đồng nghĩa không dùng theo P05 GL-08 | Sửa nội dung BR-06 thành "... khoá lại và khoản tạm giữ bị huỷ" khi chạy lại P04 UC-005 |

## Vấn đề còn mở

- Nguồn có số liệu quy mô "khoảng 60 trạm, mỗi trạm 10-20 ụ khoá" (đoạn mở đầu), nhưng P00 xếp là bối cảnh nên không có REQ; P06 không tạo NFR dung lượng vì không có REQ để truy vết (C1.1).
- NFR-05: hồ sơ dự án ghi NEN_TANG "Chưa chốt" và F5 nói "Hồ sơ ghi 'Chưa chốt' thì không tạo ràng buộc", nhưng nguồn có REQ-01 loại Ràng buộc về ứng dụng di động. Đã tạo NFR-05 theo nguồn (C1 ưu tiên hơn quy tắc bước).
- Hầu hết Tiêu chí đo có phần "Chưa quy định" vì nguồn không nêu phương pháp, điều kiện đo và cách tính (F4); Q-28, Q-29 gom các phần này.
