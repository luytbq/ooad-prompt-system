# Hồ sơ dự án (project-profile.md)

## 1. Thông tin chung

| Trường | Giá trị |
|---|---|
| TEN_HE_THONG | Hệ thống bán vé xe khách SaoViet Bus |
| MO_TA_MOT_CAU | Cho phép hành khách đặt và thanh toán vé xe khách liên tỉnh trực tuyến và giúp nhân viên nhà xe SaoViet bán vé, lập lịch chạy, soát vé. |
| TAI_LIEU_NGUON | 1. yeu-cau-xe-khach.md |
| THU_MUC_DAU_RA | ./design/ |

## 2. Chế độ làm việc

| Trường | Giá trị |
|---|---|
| CHE_DO_GIA_DINH | CO_NHAN |
| NGON_NGU_DAU_RA | Tiếng Việt, giữ thuật ngữ UML tiếng Anh |
| NGON_NGU_TEN_PHAN_TU | Tiếng Anh, PascalCase cho lớp, camelCase cho thuộc tính và phương thức, snake_case cho bảng và cột |
| HAU_TO_TEN_LOP | Mặc định |
| MUC_CHI_TIET | DAY_DU |

## 3. Bối cảnh kỹ thuật [TUỲ CHỌN]

| Trường | Giá trị |
|---|---|
| NEN_TANG | Web (website cho hành khách, giao diện web cho nhân viên nhà xe) và ứng dụng Android cho máy soát vé cầm tay |
| CONG_NGHE | Phía máy chủ: Java 17, Spring Boot (REST); phía giao diện web: React, TypeScript, Redux Toolkit; ứng dụng soát vé: Kotlin, Android, Room (SQLite); hệ quản trị CSDL: PostgreSQL |
| HE_THONG_NGOAI | Cổng thanh toán trực tuyến của đối tác (API thanh toán và hoàn tiền, chưa có tài liệu API); Cổng SMS của nhà mạng (API REST); Máy soát vé cầm tay Android có đầu quét mã vạch, do nhà xe tự trang bị; Máy in vé nhiệt tại quầy |

## 4. Ràng buộc đặc thù của dự án [TUỲ CHỌN]

Không có
