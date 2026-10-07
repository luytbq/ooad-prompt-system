# Sổ đăng ký quy tắc nghiệp vụ - Hệ thống cho thuê xe đạp công cộng CityBike

| BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái |
|---|---|---|---|---|---|---|
| BR-01 | Tài khoản chỉ được thuê xe sau khi đã liên kết một thẻ thanh toán. | Ràng buộc | UC-005 | REQ-04 | P04 UC-005 | Hiệu lực |
| BR-02 | Tài khoản chỉ được thuê xe khi không có chuyến đi đang diễn ra. | Ràng buộc | UC-005 | REQ-08 | P04 UC-005 | Hiệu lực |
| BR-03 | Tài khoản chỉ được thuê xe khi không nợ cước. | Ràng buộc | UC-005 | REQ-09 | P04 UC-005 | Hiệu lực |
| BR-04 | Xe ở trạng thái "Chờ kiểm tra" không được cho thuê. | Ràng buộc | UC-005, UC-008 | REQ-37 | P04 UC-005 | Hiệu lực |
| BR-05 | Số tiền tạm giữ cho mỗi lần thuê xe là 200.000 đồng. | Sự kiện | UC-005, UC-007 | REQ-11 | P04 UC-005 | Hiệu lực |
| BR-06 | Thời hạn chờ rút xe là 60 giây; quá thời hạn mà xe chưa được rút thì ụ khoá bị khoá lại và lệnh tạm giữ bị huỷ. | Kích hoạt hành động | UC-005 | REQ-14, REQ-15, REQ-16 | P04 UC-005 | Hiệu lực |
| BR-07 | Cước chuyến đi miễn phí 30 phút đầu, sau đó 5.000 đồng cho mỗi 15 phút hoặc phần lẻ của 15 phút. | Tính toán | UC-007 | REQ-21 | P04 UC-007 | Hiệu lực |
| BR-08 | Người thuê xe được trả xe vào một ụ trống bất kỳ ở bất kỳ trạm nào. | Sự kiện | UC-007 | REQ-17 | P04 UC-007 | Hiệu lực |
| BR-09 | Chuyến đi kéo dài quá 24 giờ thì xe của chuyến bị coi là thất lạc. | Suy luận | UC-009 | REQ-28, REQ-29 | P04 UC-009 | Hiệu lực |
| BR-10 | Khi xe bị coi là thất lạc, toàn bộ số tiền tạm giữ của chuyến bị thu và tài khoản của người thuê xe bị khoá. | Kích hoạt hành động | UC-009 | REQ-30, REQ-31 | P04 UC-009 | Hiệu lực |
| BR-11 | Thời gian miễn phí cộng thêm cho một yêu cầu là 15 phút. | Sự kiện | UC-006 | REQ-26 | P06 | Hiệu lực |
| BR-12 | Mỗi chuyến đi chỉ được yêu cầu thêm thời gian miễn phí một lần. | Ràng buộc | UC-006 | REQ-27 | P06 | Hiệu lực |
| BR-13 | Người thuê xe chỉ được báo xe hỏng khi trả xe hoặc trong vòng 10 phút sau khi trả xe. | Ràng buộc | UC-008 | REQ-34 | P06 | Hiệu lực |
| BR-14 | Trạm có dưới 20% số ụ có xe là trạm sắp hết xe. | Suy luận | UC-012 | REQ-42 | P06 | Hiệu lực |
| BR-15 | Trạm có "trên 90%" số ụ có xe là trạm sắp đầy. | Suy luận | UC-012 | REQ-43 | P06 | Hiệu lực |
| BR-16 | Mỗi lần điều chỉnh cước phải ghi lý do. | Ràng buộc | UC-017 | REQ-49 | P06 | Hiệu lực |
