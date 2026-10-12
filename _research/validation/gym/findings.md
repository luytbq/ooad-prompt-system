# Nhật ký kiểm định hồi quy pipeline trên miền mới - chuỗi phòng tập VietFit

Phạm vi: chạy P00 đến X2 trên đề yeu-cau-phong-tap.md, miền chưa xuất hiện trong ví dụ của bộ prompt và chưa từng được chạy, với bộ prompt sau hai vòng sửa (XK-01 đến XK-93, rồi 13 phát hiện mức Trung của XR). Hồ sơ dự án (design/project-profile.md) chọn các nhánh mà hai lần chạy SaoViet Bus chưa đi qua: NGHIEM_NGAT, MUC_CHI_TIET là GON, HAU_TO_TEN_LOP tự đặt (UI, Handler, Gateway, Device, tên kênh), NEN_TANG đã chốt còn CONG_NGHE "Chưa chốt", có ràng buộc đặc thù giới hạn phạm vi. P04 và P07 chạy cho bốn use case chính, P12 cho một nhóm package lõi.

Cách chạy: mỗi bước do một phiên AI độc lập (model Sonnet) thực hiện, giao việc theo runner-template.md cộng khối "Tham số bước"; phiên chạy chỉ được đọc prompt của bước, 00-Conventions.md, README.md, project-profile.md, đề và các artifact đầu vào mà mục 2, mục 3 của prompt yêu cầu. Các bước chạy tuần tự, mỗi lần một phiên. Nhật ký người chạy ở logs/<BUOC>-runner-notes.md. Sau mỗi giai đoạn, một phiên kiểm định riêng (model mặc định) đối chiếu đầu ra với Target của prompt và với nhật ký người chạy, rồi ghi phát hiện vào bảng dưới đây. Lần này không sửa prompt sản phẩm.

Mức độ:

- Cao: prompt khiến đầu ra sai ở phần cốt lõi (sai tác nhân, sai danh sách UC, sai truy vết, vi phạm Conventions C1), hoặc bước sau không đọc được bảng của bước trước, hoặc không thể hoàn thành bước theo đúng prompt.
- Trung: đầu ra lệch Target hoặc phải sửa tay, chạy lại; hai quy tắc mâu thuẫn buộc AI chọn tuỳ ý và lựa chọn đó ảnh hưởng tới bước sau.
- Thấp: mơ hồ nhỏ, vấn đề trải nghiệm người dùng, không làm sai bước sau.

Ngoài phạm vi: bố cục, định tuyến cạnh và độ dễ đọc của sơ đồ .drawio không phải nhiệm vụ của bộ prompt, nên không ghi vào bảng. Tính hợp lệ của XML và nội dung ngữ nghĩa của sơ đồ (node, cạnh, ký hiệu, khớp bảng mô hình) vẫn thuộc phạm vi.

## 1. Tóm tắt chạy

| Bước | Model | Placeholder đã điền | Đầu ra | Ghi chú |
|---|---|---|---|---|

## 2. Nhật ký phát hiện

Mã phát hiện dùng tiền tố GY.

| ID | Bước/prompt | Vị trí trong prompt (mục, câu trích) | Loại | Mô tả | Đề xuất sửa cụ thể (câu chữ thay thế) | Mức độ |
|---|---|---|---|---|---|---|

## 3. Kiểm định theo giai đoạn

## 4. Tổng kết
