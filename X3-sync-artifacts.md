# X3 - Đồng bộ artifact (Artifact Synchronization)

## 1. Mục đích

Bước này gộp kết quả các phiên chạy song song vào sổ dùng chung, áp các mục "Đề xuất sửa artifact trước" đã đủ điều kiện, và làm mới phiên bản, tham chiếu giữa các artifact. Đây là bước duy nhất được sửa artifact đã chốt của bước khác. Chạy sau mỗi lô song song và trước mỗi lần review toàn bộ.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md, project-profile.md | Có | Luật chung, chế độ giả định |
| Đầu vào | Mọi artifact trong THU_MUC_DAU_RA | Có | Khối thông tin, mục Đề xuất sửa artifact trước, Vấn đề còn mở |
| Đầu vào | Các file *.pending.md | Khi có | Dòng mới của sổ dùng chung từ phiên song song |
| Đầu vào | Báo cáo của tools/check_artifacts.py | Nên có | Danh sách lỗi hình thức cần xử lý |
| Đầu ra | Các artifact đã sửa, phiên bản tăng | Có | Trạng thái đã đồng bộ |
| Đầu ra | _sync-log.md | Có | Nhật ký: áp gì, chờ gì, cần ai quyết |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, các file đầu vào. Khi chạy bằng agent, chỉ đọc khối thông tin và bốn mục kiểm soát của artifact, rồi đọc thêm đúng đoạn cần sửa.
- Có thể chạy nhiều lần. Lần chạy sau đọc _sync-log.md để không xử lý lại.
- Khi chạy bằng chat, AI trả danh sách thay đổi theo từng file để người dùng áp tay.

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| PHAM_VI_DONG_BO | Có | Toàn bộ, hoặc các bước cần đồng bộ |
| QUYET_DINH_DA_CHOT | Tuỳ chọn | Quyết định của người dùng cho các mục Cần người quyết của lần trước |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Quy định riêng của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được hồ sơ dự án, 00-Conventions.md, các artifact trong THU_MUC_DAU_RA và (nếu có) báo cáo kiểm tra tự động, _sync-log.md của lần trước. Tuân thủ 00-Conventions.md, đặc biệt C1, C3, C5, C10. Đây là bước duy nhất được sửa artifact đã chốt của bước khác, và chỉ theo các quy tắc dưới đây.

Phạm vi đồng bộ:
{{PH:PHAM_VI_DONG_BO | Hướng dẫn: "Toàn bộ" hoặc danh sách bước | Ví dụ: "Toàn bộ"; "P04 và sổ BR sau lô UC-003, UC-005, UC-007" (phòng khám); "P07, P08" (quản lý kho)}}

Quyết định đã chốt:
{{PH:QUYET_DINH_DA_CHOT | Hướng dẫn: [TUỲ CHỌN] mỗi dòng một mã SY hoặc Q kèm quyết định; không có thì thay cả khối bằng "Không có" | Ví dụ: "SY-04: hoàn đặt cọc toàn bộ khi khách sạn huỷ phòng" (đặt phòng khách sạn); "Q-31: phí trễ hạn tính theo ngày làm việc" (thư viện)}}

[Role]
Bạn là người quản lý cấu hình tài liệu thiết kế: cẩn thận, không thêm yêu cầu mới, phân biệt rõ sửa cơ học với thay đổi nghiệp vụ.

[Action]
A1. Gộp lô. Với mỗi file *.pending.md: đưa các dòng vào sổ tương ứng, giữ mã đã cấp. Hai dòng cùng nghĩa do hai phiên cấp: giữ mã nhỏ hơn, dòng còn lại đặt trạng thái "Gộp vào <mã>", thay mã trong các artifact đang dẫn. Hai dòng mâu thuẫn: giữ cả hai, tạo SY-nn loại Cần người quyết. Gộp xong thì xoá file pending.
A2. Thu thập mọi dòng "Đề xuất sửa artifact trước" trong phạm vi và các dòng Vấn đề còn mở nhắc tới việc của bước khác. Mỗi dòng cấp một mã SY-nn, trừ dòng đã có trong _sync-log.md.
A3. Phân loại từng SY-nn:
- Áp dụng: sửa cơ học, không đổi ý nghĩa (thay mã bị gộp, bổ sung dẫn chiếu hai chiều, đổi về thuật ngữ đã chốt ở P05, bổ sung REQ vào hàng REQ, đồng bộ theo Q-nn đã trả lời hoặc theo QUYET_DINH_DA_CHOT).
- Cần người quyết: đổi luồng, BR, NFR, tiền điều kiện, tác nhân hoặc phạm vi mà chưa có câu trả lời; hoặc hai đề xuất mâu thuẫn.
- Chờ: phụ thuộc phần tử chưa có (use case chưa đặc tả, bước chưa chạy).
- Không áp: đề xuất sai hoặc đã được giải quyết, ghi lý do.
A4. Áp các mục Áp dụng theo thứ tự pipeline. Mỗi file được sửa tăng phiên bản một lần trong lần chạy này. Xoá dòng đề xuất đã áp khỏi artifact nguồn; dòng Chờ và Cần người quyết giữ nguyên.
A5. Làm mới: cập nhật hàng Đầu vào đã dùng theo phiên bản hiện hành; hàng Mã Q, ASM cuối đã cấp; xoá các câu trong Vấn đề còn mở đã hết đúng; bỏ mọi dấu vết của quá trình chạy. Nếu P09 F11 đã chốt công nghệ mà hồ sơ chưa cập nhật, cập nhật hồ sơ theo khối F11.
A6. Dựa vào bảng phụ thuộc ở mục 5 của README, liệt kê các bước cần rà lại vì nội dung đã đổi. Không tự chạy lại các bước đó.
A7. Nếu có quyền chạy lệnh, chạy tools/check_artifacts.py trên THU_MUC_DAU_RA và xử lý các LOI thuộc phạm vi. Tự kiểm tra theo [Target], rồi xuất kết quả.

[Format]
File _sync-log.md, không theo khung C5, mỗi lần chạy nối thêm một khối:

# Nhật ký đồng bộ - <TEN_HE_THONG>
## Lần <n> - <phạm vi>
| SY | Nguồn (file, mục) | Đích (bước, mã phần tử) | Loại | Nội dung | Kết quả hoặc lý do |

Loại: Áp dụng / Cần người quyết / Chờ / Không áp. Mục "Cần người quyết" đứng đầu khối, nêu câu hỏi, các phương án và đề xuất.
Sau bảng: danh sách file đã sửa kèm phiên bản mới; danh sách bước cần rà lại; khoảng trống trong dải mã do gộp lô.

Đúng: | SY-07 | P07 UC-004, Đề xuất sửa artifact trước | P04 UC-004, Mục 1 hàng REQ | Áp dụng | Thêm REQ-31 (tham chiếu, UC-007) | Đã áp, UC-004 lên 1.3 |
Sai: | SY-07 | P07 | P04 | Áp dụng | Đổi điều kiện hoàn tiền thành 48 giờ | Đã áp | (sai: đổi BR mà không có quyết định; phải là Cần người quyết).

[Target]
1. Không còn file *.pending.md; mọi dòng của chúng đã nằm trong sổ, không mất mã.
2. Mọi đề xuất trong phạm vi có đúng một dòng SY-nn với loại và kết quả.
3. Không có thay đổi về luồng, BR, NFR, tiền điều kiện, tác nhân, phạm vi nào được áp mà thiếu Q-nn đã trả lời hoặc QUYET_DINH_DA_CHOT.
4. Không có yêu cầu, phần tử mới ngoài các đề xuất đã phân loại; không mã nào bị đổi nghĩa hoặc tái sử dụng.
5. Mọi file đã sửa có phiên bản tăng; hàng Đầu vào đã dùng khớp phiên bản hiện hành.
6. Báo cáo kiểm tra tự động không còn LOI trong phạm vi, hoặc LOI còn lại được ghi lý do.
7. Đạt Conventions C2, C6, C8.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này; không dùng thì thay cả khối bằng "Không có" | Ví dụ: "Không tự xoá dòng trong Vấn đề còn mở, chỉ liệt kê."; "Chỉ áp các đề xuất cho P07 trở đi."}}
````

## 5. Ghi chú cho người dùng

- Nhiều mục Cần người quyết: trả lời trong QUYET_DINH_DA_CHOT rồi chạy lại, không cần chạy lại bước nguồn trừ khi thay đổi ảnh hưởng lớn tới luồng hoặc lớp.
- Sửa đổi ở bước sớm vẫn cần rà lại bước sau: X3 chỉ liệt kê, người dùng chạy lại theo bảng phụ thuộc trong README.
- Dùng độc lập: có thể chạy chỉ để làm mới phiên bản và tham chiếu trước khi nộp hoặc bàn giao tài liệu.

## 6. Căn cứ

- ISO/IEC/IEEE 12207, quy trình quản lý cấu hình.
- ISO/IEC/IEEE 29148, tính nhất quán và truy vết của tài liệu yêu cầu.
