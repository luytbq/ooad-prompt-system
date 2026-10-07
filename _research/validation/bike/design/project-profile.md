# Hồ sơ dự án (project-profile.md)

## 1. Thông tin chung

| Trường | Giá trị |
|---|---|
| TEN_HE_THONG | Hệ thống cho thuê xe đạp công cộng CityBike |
| MO_TA_MOT_CAU | Cho phép người dùng thuê và trả xe đạp tại các trạm công cộng qua ứng dụng di động và giúp nhân viên CityBike vận hành, bảo trì, điều chuyển xe. |
| TAI_LIEU_NGUON | 1. yeu-cau-xe-dap.md |
| THU_MUC_DAU_RA | ./design/ |

## 2. Chế độ làm việc

| Trường | Giá trị |
|---|---|
| CHE_DO_GIA_DINH | NGHIEM_NGAT |
| NGON_NGU_DAU_RA | Tiếng Việt, giữ thuật ngữ UML tiếng Anh |
| NGON_NGU_TEN_PHAN_TU | Tiếng Anh, PascalCase cho lớp, camelCase cho thuộc tính và phương thức, snake_case cho bảng và cột |
| HAU_TO_TEN_LOP | Mặc định |
| MUC_CHI_TIET | DAY_DU |

## 3. Bối cảnh kỹ thuật [TUỲ CHỌN]

| Trường | Giá trị |
|---|---|
| NEN_TANG | Ứng dụng di động (Android, iOS) cho người thuê xe; web cho nhân viên và ban giám đốc (chờ Q-35); back-end máy chủ trung tâm nhân bản được; ụ khoá kết nối qua MQTT broker (theo P09-architecture.md 1.0, F3) |
| CONG_NGHE | Back-end Java 17, Spring Boot 3; CSDL PostgreSQL 16; MQTT broker Eclipse Mosquitto (khi CityBike tự vận hành, Q-36); ứng dụng di động Flutter; web nhân viên React; kiểm thử JUnit 5, Mockito (chọn theo tiêu chí P09-architecture.md F7) |
| HE_THONG_NGOAI | Cổng thanh toán của ngân hàng đối tác (API tạm giữ tiền, thu tiền từ khoản tạm giữ, huỷ tạm giữ, hoàn tiền; chưa có tài liệu API); Ụ khoá có đầu đọc QR và khoá điện, giao tiếp qua MQTT theo quy định của nhà cung cấp thiết bị (chưa có tài liệu giao thức) |

## 4. Ràng buộc đặc thù của dự án [TUỲ CHỌN]

Không có
