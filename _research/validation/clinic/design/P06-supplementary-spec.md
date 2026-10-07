# P06 - Đặc tả bổ sung - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P06 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, yeu-cau-phong-kham.md, P00 1.0, P01 1.0, P02 1.0, P04-uc-specs/UC-004, UC-005, UC-008 (1.0), P04-uc-specs/_BR-register.md, P05-glossary.md 1.0 |
| Phạm vi | Toàn hệ thống |

## 1. Giới thiệu

Tài liệu này chứa các yêu cầu không thuộc riêng một use case của Hệ thống đặt lịch khám ClinicBook: yêu cầu phi chức năng, ràng buộc thiết kế, giao tiếp với SMS Gateway và danh sách quy tắc nghiệp vụ chính thức. Yêu cầu riêng của một use case nằm trong đặc tả use case đó; các đặc tả use case chỉ dẫn mã NFR và BR ở đây.

## 2. Yêu cầu chức năng dùng chung

Không có

## 3. Yêu cầu phi chức năng

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-01 | P - Performance / Performance efficiency | Thao tác đặt lịch có thời gian phản hồi không quá 3 giây khi có 200 người dùng đồng thời. | Kiểm thử tải với 200 phiên đồng thời thực hiện đặt lịch; đo thời gian từ khi gửi yêu cầu đặt lịch tới khi nhận kết quả. Cách tính (trung bình, phân vị) chưa quy định (Q-17) | UC-004, UC-005 | REQ-43 |
| NFR-02 | F - Functionality / Security | Kết luận khám của một lịch hẹn chỉ bác sĩ khám lịch hẹn đó và bệnh nhân của lịch hẹn đó xem được. | Kiểm thử phân quyền: với mỗi vai trò khác (bệnh nhân khác, bác sĩ khác, lễ tân, quản trị viên, quản lý phòng khám), yêu cầu xem kết luận khám bị từ chối; hai vai trò được phép xem được | UC-016, UC-017 | REQ-45 |
| NFR-03 | U - Usability / Usability | "Giao diện dùng được trên điện thoại." | Chưa đo được (Q-16): cần chốt kích thước màn hình tối thiểu, trình duyệt và các chức năng phải dùng được trên điện thoại | Toàn hệ thống | REQ-44 |

## 4. Ràng buộc thiết kế

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-04 | + Ràng buộc thiết kế | Hệ thống là phần mềm web, người dùng truy cập qua trình duyệt. | Kiểm tra triển khai: truy cập được mọi chức năng từ trình duyệt | Toàn hệ thống | REQ-01; hồ sơ dự án NEN_TANG "Web app responsive" |

## 5. Giao tiếp ngoài

| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
|---|---|---|---|---|---|
| NFR-05 | + Giao tiếp / Compatibility | Hệ thống gửi yêu cầu gửi tin SMS (mã OTP, thông báo kết quả duyệt lịch hẹn, nhắc lịch) tới ACT-06 Cổng SMS qua API có sẵn của nhà mạng; chiều trao đổi từ hệ thống tới Cổng SMS. | Kiểm thử tích hợp với Cổng SMS: yêu cầu gửi được Cổng SMS chấp nhận. Tài liệu API chưa có (hồ sơ dự án); hành vi khi Cổng SMS không phản hồi chưa quy định (Q-29, Q-32) | UC-002, UC-007, UC-008 | REQ-46 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Áp dụng cho UC | REQ | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|
| BR-01 | Bệnh nhân phải có tài khoản để tự đặt lịch khám. | Ràng buộc | UC-004 | REQ-06 | Hiệu lực | P04 UC-004 |
| BR-02 | Mỗi bệnh nhân không được có quá 2 lịch hẹn chưa diễn ra cùng lúc. | Ràng buộc | UC-004 | REQ-12 | Hiệu lực | P04 UC-004. Q-07 |
| BR-03 | Lịch hẹn do bệnh nhân tự đặt có trạng thái ban đầu "Chờ xác nhận". | Kích hoạt hành động | UC-004 | REQ-13 | Hiệu lực | P04 UC-004 |
| BR-04 | Bệnh nhân bị đánh dấu "Không đến" 3 lần trong 6 tháng bị khoá chức năng tự đặt lịch trực tuyến. | Suy luận | UC-004 | REQ-30 | Hiệu lực | P04 UC-004. Ngưỡng 3 lần là tham số cấu hình được (REQ-41, Q-12); Q-04 |
| BR-05 | Lịch hẹn do lễ tân đặt có trạng thái ban đầu "Đã xác nhận". | Kích hoạt hành động | UC-005 | REQ-25 | Hiệu lực | P04 UC-005 |
| BR-06 | Lúc 18 giờ mỗi ngày, mỗi lịch hẹn ở trạng thái "Đã xác nhận" có ngày khám là ngày hôm sau được nhắc lịch bằng SMS. | Kích hoạt hành động | UC-008 | REQ-26 | Hiệu lực | P04 UC-008 |
| BR-07 | Lịch trống của bác sĩ được xem trong phạm vi 14 ngày tới. | Ràng buộc | Chưa gắn UC | REQ-05 | Hiệu lực | P06. P02 gắn REQ-05 với UC-001. Q-06 |
| BR-08 | Mỗi khung giờ dài 30 phút. | Sự kiện | Chưa gắn UC | REQ-11 | Hiệu lực | P06. P02 gắn với UC-006 |
| BR-09 | Lễ tân phải ghi lý do khi từ chối lịch hẹn. | Ràng buộc | Chưa gắn UC | REQ-17 | Hiệu lực | P06. P02 gắn với UC-007 |
| BR-10 | Bệnh nhân chỉ được tự hủy lịch hẹn khi còn ít nhất 4 tiếng trước giờ khám. | Ràng buộc | Chưa gắn UC | REQ-20 | Hiệu lực | P06. P02 gắn với UC-009. Ngưỡng là tham số cấu hình được (REQ-41, Q-12) |
| BR-11 | Lịch hẹn chỉ được đánh dấu "Không đến" khi đã quá giờ hẹn 30 phút mà bệnh nhân chưa đến. | Ràng buộc | Chưa gắn UC | REQ-29 | Hiệu lực | P06. P02 gắn với UC-012 |
| BR-12 | Khi bác sĩ ghi kết luận khám, lịch hẹn chuyển sang trạng thái "Đã khám". | Kích hoạt hành động | Chưa gắn UC | REQ-34 | Hiệu lực | P06. P02 gắn với UC-016 |

## 7. Ma trận truy vết

REQ --> NFR/BR

| REQ | Loại REQ | NFR / BR | Ghi chú |
|---|---|---|---|
| REQ-01 | Ràng buộc | NFR-04 | Không có |
| REQ-05 | Quy tắc nghiệp vụ | BR-07 | Không có |
| REQ-06 | Quy tắc nghiệp vụ | BR-01 | Không có |
| REQ-11 | Quy tắc nghiệp vụ | BR-08 | Không có |
| REQ-12 | Quy tắc nghiệp vụ | BR-02 | Không có |
| REQ-13 | Quy tắc nghiệp vụ | BR-03 | Không có |
| REQ-17 | Quy tắc nghiệp vụ | BR-09 | Không có |
| REQ-20 | Quy tắc nghiệp vụ | BR-10 | Không có |
| REQ-25 | Quy tắc nghiệp vụ | BR-05 | Không có |
| REQ-29 | Quy tắc nghiệp vụ | BR-11 | Không có |
| REQ-30 | Quy tắc nghiệp vụ | BR-04 | Không có |
| REQ-34 | Quy tắc nghiệp vụ | BR-12 | Không có |
| REQ-43 | Phi chức năng | NFR-01 | Không có |
| REQ-44 | Ràng buộc | NFR-03 | P00 xếp Ràng buộc; theo F2 bước này, câu nêu mức dùng được (chất lượng) nên xếp Usability |
| REQ-45 | Phi chức năng | NFR-02 | Không có |
| REQ-46 | Giao tiếp ngoài | NFR-05 | Không có |

UC --> NFR/BR

| UC | NFR | BR |
|---|---|---|
| UC-001 | NFR-03, NFR-04 | BR-07 |
| UC-002 | NFR-03, NFR-04, NFR-05 | - |
| UC-003 | NFR-03, NFR-04 | - |
| UC-004 | NFR-01, NFR-03, NFR-04 | BR-01, BR-02, BR-03, BR-04 |
| UC-005 | NFR-01, NFR-03, NFR-04 | BR-05 |
| UC-006 | NFR-03, NFR-04 | BR-08 |
| UC-007 | NFR-03, NFR-04, NFR-05 | BR-09 |
| UC-008 | NFR-05 | BR-06 |
| UC-009 | NFR-03, NFR-04 | BR-10 |
| UC-010 | NFR-03, NFR-04 | - |
| UC-011 | NFR-03, NFR-04 | - |
| UC-012 | NFR-03, NFR-04 | BR-04, BR-11 |
| UC-013 | NFR-03, NFR-04 | - |
| UC-014 | NFR-03, NFR-04 | - |
| UC-015 | NFR-03, NFR-04 | - |
| UC-016 | NFR-02, NFR-03, NFR-04 | BR-12 |
| UC-017 | NFR-02, NFR-03, NFR-04 | - |
| UC-018 | NFR-03, NFR-04 | - |
| UC-019 | NFR-03, NFR-04 | - |
| UC-020 | NFR-03, NFR-04 | BR-04, BR-10 |
| UC-021 | NFR-03, NFR-04 | - |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-32 | Nhà mạng cung cấp tài liệu API của SMS Gateway khi nào, và API có trả kết quả gửi (thành công, thất bại) cho từng tin không? | NFR-05; bước thiết kế giao tiếp hệ thống | REQ-46; hồ sơ dự án HE_THONG_NGOAI |

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P04 | UC-004 | Yêu cầu đặc biệt chỉ gắn NFR (REQ-43) với UC-004, trong khi nguồn nói "thao tác đặt lịch" chung | Thêm dòng Yêu cầu đặc biệt REQ-43 vào UC-005 khi đặc tả lại |
| P00 | REQ-44 | Xếp Ràng buộc, nhưng nội dung là mức dùng được | Đổi loại thành Phi chức năng khi chạy lại P00 |

## Vấn đề còn mở

- Mới có ba đặc tả P04; BR-07 đến BR-12 ghi "Chưa gắn UC" theo F6 dù P02 đã gắn REQ tương ứng với UC. Cần chạy lại P06 khi có đủ đặc tả.
- NFR-01 chưa có cách tính (trung bình hay phân vị): F4 yêu cầu nêu cách tính, nhưng chế độ NGHIEM_NGAT không cho tự chọn; đã để Q-17.
