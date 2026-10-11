# Nhật ký kiểm chứng lại pipeline sau khi sửa prompt - miền bán vé xe khách SaoViet Bus

Phạm vi: chạy lại P00 đến X2 trên cùng đề (yeu-cau-xe-khach.md) và cùng hồ sơ ban đầu (design/project-profile.md: CO_NHAN, DAY_DU, NEN_TANG và CONG_NGHE "Chưa chốt") với bộ prompt đã sửa theo các phát hiện XK-01 đến XK-93 (xem fix-log.md). P04 và P07 chạy cho hai use case đại diện: UC-009 Đặt vé trực tuyến và UC-017 Huỷ chuyến (mã theo P02 của lần chạy này).

Cách chạy: mỗi bước do một phiên AI độc lập (model Sonnet) thực hiện, giao việc theo runner-template.md cộng khối "Tham số bước"; phiên chạy chỉ được đọc prompt của bước, 00-Conventions.md, README.md, project-profile.md, đề và các artifact đầu vào mà mục 2, mục 3 của prompt yêu cầu. Nhật ký người chạy ở logs/<BUOC>-runner-notes.md. Sau mỗi giai đoạn, một phiên kiểm định riêng (model mặc định) đối chiếu đầu ra với Target của prompt và với nhật ký người chạy, rồi ghi phát hiện vào bảng ở mục 2. Các bước chạy tuần tự.

Mức độ:

- Cao: prompt khiến đầu ra sai ở phần cốt lõi (sai tác nhân, sai danh sách UC, sai truy vết, vi phạm Conventions C1), hoặc bước sau không đọc được bảng của bước trước, hoặc không thể hoàn thành bước theo đúng prompt.
- Trung: đầu ra lệch Target hoặc phải sửa tay, chạy lại; hai quy tắc mâu thuẫn buộc AI chọn tuỳ ý và lựa chọn đó ảnh hưởng tới bước sau.
- Thấp: mơ hồ nhỏ, vấn đề trải nghiệm người dùng, không làm sai bước sau.

Ngoài phạm vi: bố cục, định tuyến cạnh và độ dễ đọc của sơ đồ .drawio không phải nhiệm vụ của bộ prompt, nên không ghi vào bảng. Tính hợp lệ của XML và nội dung ngữ nghĩa của sơ đồ (node, cạnh, ký hiệu, khớp bảng mô hình) vẫn thuộc phạm vi.

## 1. Tóm tắt chạy

| Bước | Model | Placeholder đã điền | Đầu ra | Ghi chú |
|---|---|---|---|---|
| P00 | Sonnet | TRONG_TAM_PHAN_TICH, YEU_CAU_BO_SUNG = Không có | P00-problem-brief.md | 77 REQ, 11 SH, Q-01..Q-37, ASM-01..ASM-09; khoảng 24 phút |
| P01 | Sonnet | QUYET_DINH_RANH_GIOI, YEU_CAU_BO_SUNG = Không có | P01-actors.md | 9 ACT, 19 ứng viên loại, Q-38, Q-39, ASM-10, ASM-11; khoảng 15 phút |
| P02 (lần 1) | Sonnet | PHAM_VI_LAN_CHAY, QUY_UOC_DA_CHOT, YEU_CAU_BO_SUNG = Không có | P02-usecases.md | 28 UC (26 User-goal, 2 Subfunction), 66 CAND, 29 EV, Q-40, ASM-12..ASM-14; lần đầu dừng do hết hạn mức, chạy lại bằng phiên mới, khoảng 19 phút |
| P02R | Sonnet | DOI_TUONG_REVIEW = P01, P02; PHAM_VI_REVIEW = TAC_NHAN, DANH_SACH_UC | P02R-review.md | Đạt: 0 Nghiêm trọng, 2 Trung bình, 2 Thấp (UCR-01..UCR-04); Q-41, Q-42, ASM-15, ASM-16. Người điều phối (vai người dùng) chọn áp dụng cả 4 UCR |
| P02 (lần 2, bản 1.1) | Sonnet | YEU_CAU_BO_SUNG = "Áp dụng UCR-01, UCR-02, UCR-03, UCR-04 của P02R-review.md phiên bản 1.0." | P02-usecases.md (ghi đè) | 27 UC hiệu lực, UC-013 Loại (gộp vào UC-012); không cấp mã mới |
| P03 | Sonnet | KIEU_DUONG_ASSOCIATION, CACH_PHAN_RA_SO_DO, YEU_CAU_BO_SUNG = Không có | P03-usecase-model.md; 4 file .drawio | 48 RL (41 association, 6 include, 1 extend), Q-43, ASM-17; khoảng 24 phút |

## 2. Nhật ký phát hiện

| ID | Bước/prompt | Vị trí trong prompt (mục, câu trích) | Loại | Mô tả | Đề xuất sửa cụ thể (câu chữ thay thế) | Mức độ |
|---|---|---|---|---|---|---|
