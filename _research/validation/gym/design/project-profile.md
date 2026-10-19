# Hồ sơ dự án (project-profile.md)

## 1. Thông tin chung

| Trường | Giá trị |
|---|---|
| TEN_HE_THONG | Hệ thống quản lý chuỗi phòng tập VietFit |
| MO_TA_MOT_CAU | Cho phép hội viên mua gói tập, đặt chỗ lớp nhóm và buổi tập cá nhân trên ứng dụng di động, và giúp nhân viên chuỗi phòng tập VietFit quản lý hội viên, lịch lớp và việc ra vào chi nhánh. |
| TAI_LIEU_NGUON | 1. yeu-cau-phong-tap.md |
| THU_MUC_DAU_RA | ./design/ |

## 2. Chế độ làm việc

| Trường | Giá trị |
|---|---|
| CHE_DO_GIA_DINH | NGHIEM_NGAT |
| NGON_NGU_DAU_RA | Tiếng Việt, giữ thuật ngữ UML tiếng Anh |
| NGON_NGU_TEN_PHAN_TU | Tiếng Anh, PascalCase cho lớp, camelCase cho thuộc tính và phương thức, snake_case cho bảng và cột |
| HAU_TO_TEN_LOP | Boundary người dùng: UI; boundary kênh thông báo: tên kênh, ví dụ PushNotifier, SmsNotifier; boundary hệ thống ngoài: Gateway; boundary thiết bị: Device; control: Handler |
| MUC_CHI_TIET | GON |

## 3. Bối cảnh kỹ thuật [TUỲ CHỌN]

| Trường | Giá trị |
|---|---|
| NEN_TANG | Ứng dụng di động Android và iOS cho hội viên và huấn luyện viên; ứng dụng web chạy trên trình duyệt máy tính cho lễ tân, quản lý chi nhánh và giám đốc chuỗi |
| CONG_NGHE | Ứng dụng di động: React Native (TypeScript); ứng dụng web: React SPA (TypeScript); máy chủ: Node.js với NestJS (TypeScript), giao tiếp REST/JSON; hệ quản trị CSDL: PostgreSQL |
| HE_THONG_NGOAI | Cổng thanh toán trực tuyến của đối tác (API REST, có tài liệu API thanh toán và tra cứu giao dịch); Cổng SMS của nhà mạng (API REST); Dịch vụ thông báo đẩy của nền tảng di động; Hệ thống hoá đơn điện tử của đơn vị cung cấp (API REST, chưa có tài liệu API); Cửa quay có đầu đọc mã QR tại mỗi chi nhánh, do nhà cung cấp thiết bị lắp đặt, gửi mã QR đọc được tới phần mềm qua API và mở cửa theo kết quả trả về |

## 4. Ràng buộc đặc thù của dự án [TUỲ CHỌN]

- Nghiệp vụ hoá đơn điện tử nằm ngoài phạm vi: phần mềm chỉ gửi dữ liệu giao dịch thu tiền sang hệ thống hoá đơn điện tử, không phân tích việc lập, điều chỉnh, huỷ hoá đơn (áp dụng cho mọi bước).
- Việc tính thù lao huấn luyện viên làm ngoài phần mềm; phần mềm chỉ cung cấp báo cáo số buổi tập cá nhân (áp dụng cho mọi bước).
