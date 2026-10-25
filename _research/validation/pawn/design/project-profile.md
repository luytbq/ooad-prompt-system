# Hồ sơ dự án (project-profile.md)

## 1. Thông tin chung

| Trường | Giá trị |
|---|---|
| TEN_HE_THONG | Hệ thống quản lý chuỗi cầm đồ Phúc An |
| MO_TA_MOT_CAU | Giúp nhân viên chuỗi cửa hàng cầm đồ Phúc An lập và theo dõi hợp đồng cầm đồ, quản lý tài sản cầm cố và tiền mặt tại quầy, và cho khách xem hợp đồng, đóng lãi trên ứng dụng di động. |
| TAI_LIEU_NGUON | 1. yeu-cau-cam-do.md; 2. bien-ban-hop-bo-sung.md |
| THU_MUC_DAU_RA | ./design/ |

## 2. Chế độ làm việc

| Trường | Giá trị |
|---|---|
| CHE_DO_GIA_DINH | CO_NHAN |
| NGON_NGU_DAU_RA | Tiếng Việt, giữ thuật ngữ UML tiếng Anh |
| NGON_NGU_TEN_PHAN_TU | Tiếng Anh, PascalCase cho lớp, camelCase cho thuộc tính và phương thức, snake_case cho bảng và cột |
| HAU_TO_TEN_LOP | Boundary người dùng: Form; boundary kênh thông báo (SMS, thông báo đẩy): tên kênh, ví dụ SmsNotifier, PushNotifier; boundary hệ thống ngoài: Gateway; boundary thiết bị: Device; control: Controller |
| MUC_CHI_TIET | DAY_DU |

## 3. Bối cảnh kỹ thuật [TUỲ CHỌN]

| Trường | Giá trị |
|---|---|
| NEN_TANG | Chưa chốt |
| CONG_NGHE | Chưa chốt |
| HE_THONG_NGOAI | Cổng chi hộ của ngân hàng đối tác (API REST, có tài liệu API chi hộ và tra cứu lệnh chi); Cổng thanh toán trực tuyến (API REST, có tài liệu API thanh toán và tra cứu giao dịch); Cổng SMS của nhà mạng (API REST); Dịch vụ thông báo đẩy của nền tảng di động; Hệ thống tra cứu phương tiện bị mất cắp của cơ quan công an (chưa có tài liệu API); Đầu đọc căn cước gắn chip tại mỗi quầy (kết nối USB, có bộ thư viện của nhà sản xuất); Máy in nhãn mã vạch và máy quét mã vạch tại mỗi quầy |

## 4. Ràng buộc đặc thù của dự án [TUỲ CHỌN]

Không có
