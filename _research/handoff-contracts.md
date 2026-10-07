# Hợp đồng giao tiếp giữa các bước (nội bộ)

Các nhánh viết song song phải giữ đúng các bảng lõi dưới đây, vì bước sau ở nhánh khác sẽ đọc chúng. Được thêm cột, thêm mục; không được đổi tên hoặc bỏ cột lõi. Nếu thấy cần đổi, ghi đề xuất vào cuối file notes của nhánh, mục "Đề xuất đổi hợp đồng", người tích hợp sẽ quyết định.

## P00 - P00-problem-brief.md (nhánh B)
- Bảng yêu cầu: | REQ | Nội dung chuẩn hoá | Loại (Chức năng / Phi chức năng / Quy tắc nghiệp vụ / Dữ liệu / Giao tiếp ngoài / Ràng buộc) | Trích nguồn | Ghi chú |
- Mục Phạm vi: Trong phạm vi / Ngoài phạm vi.
- Mục Các bên liên quan và người dùng (stakeholder), chưa phải tác nhân.
- Câu hỏi mở Q-nn, Giả định ASM-nn theo Conventions C5; mã đánh số liên tục toàn dự án, cấp tiếp từ số lớn nhất trong các artifact đầu vào (C3).

## P01 - P01-actors.md (nhánh A)
- Bảng tác nhân: | ACT | Tên (VI) | Tên (EN) | Loại (Người / Hệ thống ngoài / Thiết bị / Thời gian) | Mô tả vai trò | Mục tiêu với hệ thống | Tổng quát hoá từ (ACT cha, nếu có) | REQ |
- Bảng ứng viên tác nhân bị loại: | Ứng viên | Lý do loại | REQ |

## P02 - P02-usecases.md (nhánh A)
- Bảng use case: | UC | Tên (VI) | Tên (EN) | Tác nhân chính (ACT) | Tác nhân phụ (ACT) | Mục tiêu (kết quả có giá trị) | Mô tả ngắn | Sự kiện kích hoạt | Nhóm chức năng | REQ |
- Bảng ứng viên: | CAND | Ứng viên | Kết luận (Giữ thành UC-nnn / Gộp vào UC-nnn / Là bước của UC-nnn / Loại) | Phép thử không đạt | Lý do | REQ |
- Ma trận truy vết REQ chức năng --> UC (mọi REQ chức năng phải được phủ hoặc có lý do).

## P03 - P03-usecase-model.md (nhánh A)
- Bảng quan hệ: | ID | Nguồn | Đích | Loại (Association / Include / Extend / Generalization) | Điều kiện extend / điểm mở rộng | Lý do | REQ |
- Danh sách sơ đồ (tổng quát, phân rã theo nhóm) và file .drawio tương ứng.

## P04 - P04-uc-specs/UC-nnn-<slug>.md (nhánh B)
- Bảng thông tin: Mã UC, Tên, Tác nhân, Mô tả ngắn, Tiền điều kiện, Hậu điều kiện, (các hàng khác theo slide).
- Luồng chính: | STT | Thực hiện bởi | Hành động |, STT là số 1, 2, 3...
- Luồng thay thế / ngoại lệ: | STT (ví dụ 3a, 3a1) | Điều kiện | Thực hiện bởi | Hành động | Quay lại / Kết thúc |
- Dữ liệu vào / ra (nếu slide có): | STT | Trường dữ liệu | Mô tả | Bắt buộc | Điều kiện hợp lệ | Ví dụ |
- Quy tắc nghiệp vụ tham chiếu BR-nn.
- Activity diagram: bảng mô hình + diagrams/P04-activity-UC-nnn.drawio, swimlane theo tác nhân và hệ thống.

- Đã chấp nhận (từ nhánh B): thêm hàng Tác nhân chính/phụ, Sự kiện kích hoạt, Hậu điều kiện thành công và tối thiểu, Quan hệ, Điểm mở rộng; bảng dữ liệu ra có cột Định dạng hiển thị; bảng Node activity có cột Bước UC; sổ BR ở P04-uc-specs/_BR-register.md.

## P05 - P05-glossary.md (nhánh B)
- | GL | Thuật ngữ | Tiếng Anh | Định nghĩa | Từ đồng nghĩa không dùng | Nguồn (REQ / UC) |

## P06 - P06-supplementary-spec.md (nhánh B)
- NFR: | NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
- BR: | BR | Quy tắc | Loại | Áp dụng cho UC | REQ |

## P07 - P07-uc-analysis/UC-nnn-<slug>-analysis.md (nhánh C)
- Lớp phân tích: | AC | Stereotype (boundary / control / entity) | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn |
- Sequence (analysis): | STT | Từ | Đến | Message (tên trách nhiệm, chưa phải chữ ký phương thức) | Bước UC |
- Communication diagram, VOPC (analysis class diagram cho UC).
- Mã AC dùng chung toàn hệ thống: cùng một khái niệm ở hai UC phải cùng mã.

## P08 - P08-analysis-model.md (nhánh C)
- Bảng lớp hợp nhất: | AC | Stereotype | Tên | Trách nhiệm (gộp) | Thuộc tính | Dùng trong UC |
- Bảng quan hệ: | ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn UC |

## P09 - P09-architecture.md (nhánh C)
- Mẫu kiến trúc đã chọn và lý do (đối chiếu NFR); mẫu cho phía giao diện chọn sau khi có công nghệ.
- Khi hồ sơ ghi "Chưa chốt": bảng so sánh phương án công nghệ (F2.2) và mục "Cập nhật hồ sơ dự án" (F11) gồm NEN_TANG, CONG_NGHE để dán vào project-profile.md trước P10.
- | PKG | Tên | Layer | Trách nhiệm | Phụ thuộc vào (PKG) |
- Quy tắc phụ thuộc: không mũi tên dependency hoặc realization đi lên; gọi ngược qua interface do layer dưới định nghĩa, layer trên hiện thực.

## P10 - P10-design-elements.md (nhánh C)
- Ánh xạ: | AC | Kết quả (Lớp thiết kế DC / Subsystem SS / Package / Tách thành nhiều lớp) | Phần tử thiết kế | PKG | Lý do |
- Subsystem: | SS | Tên | Interface (IF) | Trách nhiệm | Che giấu phần tử nào |

## P11a - P11a-gui/ (nhánh C)
- screen-list.md: | SCR | Tên | Boundary AC nguồn | UC | Tác nhân | Loại (chính / pop-up / dependent...) |; danh sách boundary lấy từ P10 F3 (layer giao diện); bảng phụ "Boundary không có màn hình".
- screen-transition.md + diagrams/P11a-screen-transition.drawio
- SCR-nn-<slug>.md: screen spec theo slide (mục điều khiển, thao tác, chức năng).

## P11b - P11b-system-interfaces.md (nhánh C)
- | IF | Tên | Hệ thống/thiết bị | Operation | Tham số vào | Kết quả | Lỗi / ngoại lệ | UC |
- Mã IF-nn do P10, P11b cấp; P12 được cấp IF-nn mới nối tiếp cho interface do cơ chế thiết kế.

## P12 - P12-class-design.md (nhánh D)
- Lớp: | DC | Tên | Stereotype | PKG | Trách nhiệm | Nguồn AC |
- Thuộc tính: | DC | Visibility | Tên | Kiểu | Multiplicity | Mặc định | Ràng buộc |
- Phương thức: | DC | Visibility | Chữ ký | Mô tả | Tiền/hậu điều kiện | Nguồn (message P07 / UC bước) |
- Quan hệ: | ID | Lớp A | Lớp B | Loại | Multiplicity | Điều hướng | Lý do |
- State machine: | ST | Lớp | Trạng thái | Sự kiện | Guard | Hành động | Trạng thái đích |

## P13 - P13-data-model.md (nhánh D)
- Thực thể ER khái niệm, mô hình logic, bảng vật lý: | TBL | Tên bảng | Cột | Kiểu | PK/FK/UNIQUE | NULL | Mặc định | Nguồn DC |
- Kiểm tra chuẩn hoá tới 3NF.

## X1 - X1-design-review.md (nhánh D)
- | RV | Nguyên lý / tiêu chí vi phạm | Phần tử | Bằng chứng | Mức độ | Đề xuất sửa | Bước cần sửa |

## X2 - X2-unit-tests.md (nhánh D)
- | TC | DC.phương thức | Kỹ thuật (phân vùng tương đương / giá trị biên / bảng quyết định / đường đi) | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn (BR / UC bước) |
