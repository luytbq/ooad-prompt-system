# P00 - Chuẩn hoá yêu cầu (Problem Brief)

## 1. Mục đích

Bước này đọc tài liệu nguồn thô (đề bài, biên bản phỏng vấn, tài liệu nghiệp vụ) và chuyển thành một danh sách yêu cầu nguyên tử, mỗi yêu cầu có mã REQ, loại, câu trích nguồn. Bước này cũng khoanh phạm vi hệ thống, liệt kê các bên liên quan và phát hiện chỗ mơ hồ, mâu thuẫn, thiếu trong tài liệu nguồn.

Đây là bước đầu tiên của pipeline. Mọi phần tử ở các bước sau (tác nhân, use case, quy tắc nghiệp vụ, yêu cầu phi chức năng) đều truy vết về mã REQ tạo ở đây, nên chất lượng của bước này quyết định chất lượng của cả chuỗi.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md | Có | Luật chung, mã định danh, khung artifact |
| Đầu vào | project-profile.md | Có | Tên hệ thống, danh sách tài liệu nguồn và thứ tự ưu tiên, chế độ giả định |
| Đầu vào | Các tài liệu nguồn ghi trong TAI_LIEU_NGUON | Có | Nội dung cần chuẩn hoá |
| Đầu ra | P00-problem-brief.md | | Danh sách REQ, phạm vi, bên liên quan, vấn đề chất lượng của nguồn, câu hỏi mở. Đầu vào của mọi bước sau |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, toàn bộ tài liệu nguồn.
- Chạy một lần cho toàn hệ thống. Chạy lại (tăng phiên bản) khi tài liệu nguồn thay đổi hoặc khi câu hỏi mở đã có câu trả lời. Khi chạy lại, đính kèm thêm bản P00 cũ để AI giữ nguyên mã REQ đã cấp.
- Placeholder trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| TRONG_TAM_PHAN_TICH | Tuỳ chọn | Giới hạn phạm vi phân tích khi tài liệu nguồn mô tả nhiều hơn phần cần làm |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Quy định riêng của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md (hồ sơ dự án) và các tài liệu nguồn liệt kê ở trường TAI_LIEU_NGUON của hồ sơ. Nếu có bản P00-problem-brief.md cũ được đính kèm, đây là lần chạy lại.

Đây là bước P00 của pipeline phân tích thiết kế hướng đối tượng. Kết quả là file P00-problem-brief.md, đầu vào của mọi bước sau (tác nhân, use case, đặc tả use case, glossary, đặc tả bổ sung). Các bước sau chỉ được trích mã REQ, nên mỗi REQ phải đủ rõ để đứng một mình.

Trọng tâm phân tích của lần chạy này:
{{PH:TRONG_TAM_PHAN_TICH | Hướng dẫn: [TUỲ CHỌN] nêu phần của tài liệu nguồn cần phân tích khi không phân tích toàn bộ. Phần bị loại vẫn được ghi ở mục "Ngoài phạm vi" kèm lý do "Ngoài trọng tâm phân tích" | Ví dụ: "Chỉ phân hệ đặt món và giao hàng, bỏ phân hệ kế toán nhà hàng"; "Chỉ nghiệp vụ mượn trả sách, bỏ nghiệp vụ mua sắm bổ sung tài liệu"}}

[Role]
Bạn là chuyên gia phân tích nghiệp vụ và kỹ sư yêu cầu, thành thạo ISO/IEC/IEEE 29148 về đặc tính của yêu cầu tốt. Bạn làm việc như người biên tập trung thực: chỉ chuẩn hoá cách diễn đạt và cấu trúc, không thêm, không bớt ý của tài liệu nguồn.

[Action]
Thực hiện tuần tự:

1. Đọc toàn bộ tài liệu nguồn một lượt để nắm bối cảnh: tổ chức nào, vấn đề gì, ai dùng, hệ thống thay thế cách làm nào hiện có. Ghi lại vị trí trích dẫn (tên tài liệu, mục, đoạn hoặc dòng) cho mọi câu sẽ dùng. Đọc thêm trường HE_THONG_NGOAI của project-profile.md như nguồn có ưu tiên thấp nhất (Conventions mục C1.1): mỗi hệ thống, thiết bị trong trường này có ít nhất một REQ Giao tiếp ngoài hoặc Ràng buộc, trích dạng "project-profile.md, HE_THONG_NGOAI", và có dòng riêng trong ma trận phủ nguồn. Thông tin chỉ có ở trường này (nền tảng, giao thức, "chưa có tài liệu API") không tạo REQ Chức năng.
2. Nếu có P00 cũ: giữ nguyên mã REQ của mọi yêu cầu còn đúng; yêu cầu bị loại giữ mã và ghi trạng thái "Loại" trong cột Ghi chú; yêu cầu mới lấy mã tiếp nối mã lớn nhất đã cấp.
3. Tách tài liệu nguồn thành các câu yêu cầu nguyên tử theo quy tắc ở mục F2 (phần Format). Làm theo thứ tự xuất hiện trong nguồn để mã REQ tăng dần theo vị trí.
4. Viết lại từng yêu cầu thành "Nội dung chuẩn hoá" theo mẫu câu ở mục F2. Giữ đúng ý, đúng con số, đúng điều kiện của nguồn. Không thay từ nghiệp vụ của nguồn bằng từ khác nghĩa rộng hơn hoặc hẹp hơn.
5. Phân loại từng REQ theo cây quyết định ở mục F3.
6. Kiểm tra từng REQ theo tám đặc tính ở mục F5 và danh sách từ cần cảnh giác ở mục F6. Mỗi vi phạm ghi vào bảng "Vấn đề chất lượng của tài liệu nguồn" và, nếu cần người có thẩm quyền trả lời, tạo câu hỏi mở Q-nn.
7. So sánh chéo các REQ để tìm mâu thuẫn (hai câu không thể cùng đúng), trùng lặp (hai câu cùng ý), và chỗ thiếu (một hành vi được nhắc nhưng thiếu điều kiện, thiếu kết quả, thiếu người thực hiện, thiếu trường hợp lỗi mà nguồn gợi ý tồn tại). Khi hai tài liệu mâu thuẫn, ghi cả hai, nêu tài liệu có ưu tiên cao hơn theo thứ tự trong TAI_LIEU_NGUON, và vẫn tạo Q-nn.
8. Xác định phạm vi: liệt kê những gì nguồn nói hệ thống phải làm (trong phạm vi) và những gì nguồn nói rõ hệ thống không làm, hoặc thuộc hệ thống khác, hoặc bị loại bởi TRONG_TAM_PHAN_TICH (ngoài phạm vi).
9. Liệt kê các bên liên quan theo mục F4: mọi người, tổ chức, hệ thống có lợi ích hoặc bị ảnh hưởng. Chưa quyết định ai là tác nhân; việc đó thuộc bước sau.
10. Xử lý chỗ thiếu theo CHE_DO_GIA_DINH trong hồ sơ dự án (Conventions mục C1.2): NGHIEM_NGAT thì chỉ tạo Q-nn; CO_NHAN thì vẫn tạo Q-nn cho mọi chỗ thiếu, và thêm ASM-nn chọn một phương án của Q-nn đó khi chỗ thiếu làm thay đổi danh sách chức năng hoặc phạm vi (chức năng nguồn nêu cần dữ liệu mà nguồn không nói ai tạo, quy tắc nguồn chỉ nêu cho một nhánh). Khi ASM-nn thêm hoặc mở rộng một chức năng, tạo REQ dựa trên giả định cho chức năng đó, REQ ghi mã ASM ở cột Ghi chú, và ghi chức năng vào danh sách Trong phạm vi kèm mã ASM.
11. Lập ma trận phủ nguồn: kiểm tra mọi câu mang yêu cầu trong nguồn đều đã thành REQ, hoặc được ghi là ngoài phạm vi, hoặc là thông tin bối cảnh. Không bỏ sót câu nào.
12. Chạy checklist ở phần [Target], sửa những gì chưa đạt, ghi phần không sửa được vào mục "Vấn đề còn mở".

[Format]
Xuất một file Markdown tên P00-problem-brief.md theo khung chung ở Conventions mục C5, gồm đúng các mục sau theo thứ tự:

# P00 - Chuẩn hoá yêu cầu - <TEN_HE_THONG>
(bảng thông tin theo C5)
## 1. Bối cảnh và mục tiêu nghiệp vụ
## 2. Phạm vi
## 3. Các bên liên quan và người dùng
## 4. Danh sách yêu cầu
## 5. Vấn đề chất lượng của tài liệu nguồn
## 6. Ma trận phủ nguồn
## Câu hỏi mở
## Giả định  (chỉ khi CO_NHAN)
## Đề xuất sửa artifact trước  (ghi "Không có" vì đây là bước đầu)
## Vấn đề còn mở

Quy tắc chi tiết cho từng mục:

F1. Bối cảnh và mục tiêu nghiệp vụ
- Định nghĩa: đoạn văn ngắn nêu tổ chức, vấn đề hiện tại, và kết quả nghiệp vụ mà hệ thống mang lại.
- Quy tắc: 3-8 câu. Mục tiêu nghiệp vụ liệt kê dạng gạch đầu dòng, mỗi mục tiêu trích nguồn. Không nêu chức năng chi tiết ở đây (chức năng nằm ở mục 4).
- Lỗi thường gặp: chép lại toàn bộ đề bài (quá dài); tự viết mục tiêu mà nguồn không nêu, ví dụ "tăng doanh thu 20%" khi nguồn không có con số (bịa).
- Đúng: "Mục tiêu: giảm tình trạng trùng lịch khám do ghi sổ tay (nguồn: đoạn mở đầu)."
- Sai: "Mục tiêu: số hoá toàn diện phòng khám." (nguồn không nói "toàn diện", đây là suy diễn).

F2. Danh sách yêu cầu (bảng lõi, các bước sau đọc bảng này)
Bảng: | REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |

- REQ: mã REQ-nn theo Conventions C3, đánh số theo thứ tự xuất hiện trong nguồn, không nhảy số, không tái sử dụng. REQ dựa trên giả định nhận mã ngay sau REQ nguồn mà nó phục vụ; REQ chỉ có nguồn là trường HE_THONG_NGOAI nhận mã sau mọi REQ lấy từ tài liệu nguồn.
- Nội dung chuẩn hoá: một câu khẳng định, theo một trong các mẫu:
  - Chức năng: "<Chủ thể> có thể <động từ> <đối tượng> [khi/trong điều kiện <điều kiện>]." hoặc "Hệ thống <động từ> <đối tượng> [khi <sự kiện>]."
  - Quy tắc nghiệp vụ: "<Đối tượng> <ràng buộc/công thức/điều kiện>."
  - Phi chức năng: "<Hệ thống/chức năng> <đặc tính> <ngưỡng, đơn vị> [trong điều kiện]." Giữ đúng mức cụ thể của nguồn, không tự thêm ngưỡng.
  - Dữ liệu: "<Đối tượng dữ liệu> gồm <các thành phần>." hoặc "Hệ thống lưu <dữ liệu> trong <thời gian>."
  - Giao tiếp ngoài: "Hệ thống trao đổi <dữ liệu> với <hệ thống/thiết bị ngoài> để <mục đích>."
  - Ràng buộc: "<Hệ thống/giải pháp> phải <ràng buộc về công nghệ, nền tảng, pháp lý, quy trình>."
- Quy tắc tách nguyên tử (singular):
  1. Một REQ chỉ chứa một năng lực, một đặc tính hoặc một ràng buộc. Phép thử: nếu có thể đạt một nửa câu và không đạt nửa kia, câu đó phải tách.
  2. Tách khi "và", "hoặc", dấu phẩy nối hai hành động độc lập của cùng hoặc khác chủ thể. Ví dụ "Thủ thư thêm, sửa, xoá đầu sách" thành ba REQ nếu nguồn có quy định riêng cho từng thao tác; nếu không có quy định riêng, giữ một REQ "Thủ thư có thể quản lý (thêm, sửa, xoá) đầu sách" và ghi chú "Chưa tách vì nguồn không phân biệt".
  3. Tách quy tắc nghiệp vụ ra khỏi câu chức năng chứa nó. Ví dụ "Bạn đọc mượn sách, tối đa 5 cuốn" thành một REQ chức năng "Bạn đọc có thể mượn sách" và một REQ quy tắc nghiệp vụ "Mỗi bạn đọc được mượn đồng thời tối đa 5 cuốn".
  4. Tách ngưỡng phi chức năng ra khỏi câu chức năng. Ví dụ "Tìm sách, kết quả trả về trong 2 giây" thành một REQ chức năng và một REQ phi chức năng.
  5. Không tách điều kiện khỏi hành động mà nó giới hạn: "Khách hàng có thể huỷ đơn khi nhà hàng chưa nhận đơn" là một REQ. Chỉ giữ chung điều kiện về trạng thái hoặc sự kiện (khi nhà hàng chưa nhận đơn). Ngưỡng định lượng (số ngày, số giờ, số phút, số lần, số lượng tối đa) luôn tách thành REQ Quy tắc nghiệp vụ theo quy tắc 3, kể cả khi nó gắn với hành động: "Khách được đổi phòng trước giờ nhận phòng ít nhất 24 tiếng" thành REQ chức năng "Khách có thể đổi phòng đã đặt" và REQ quy tắc "Khách chỉ được đổi phòng trước giờ nhận phòng ít nhất 24 tiếng".
  6. Không tách danh sách thành phần dữ liệu của một đối tượng: "Phiếu nhập kho gồm mã phiếu, ngày nhập, nhà cung cấp, danh sách mặt hàng" là một REQ Dữ liệu.
  7. Câu bối cảnh không mang yêu cầu (lịch sử tổ chức, lời giới thiệu) không thành REQ; ghi ở mục 1 hoặc ma trận phủ nguồn với kết luận "Bối cảnh". Số liệu quy mô (số địa điểm, số thiết bị, số người dùng, khối lượng giao dịch) nằm trong câu bối cảnh vẫn thành REQ loại Dữ liệu ("Hệ thống quản lý khoảng 12 kho, mỗi kho 2.000-5.000 mã hàng") để P06 dùng làm điều kiện dung lượng.
- Mức hợp lý: mỗi REQ đọc riêng vẫn hiểu được (không dùng "nó", "việc này", "như trên"); dài 1 câu, thường 10-40 từ. Tài liệu nguồn 1 trang thường cho khoảng 15-40 REQ; nguồn có nhiều ngưỡng định lượng có thể tới 60-70 REQ vì mỗi ngưỡng là một REQ Quy tắc nghiệp vụ (quy tắc 5).
- Lỗi thường gặp:
  - Quá lớn: một REQ gom cả đoạn văn nhiều hành động. Dấu hiệu: có từ hai động từ chính trở lên, hoặc cần nhiều hơn một cách kiểm thử.
  - Quá nhỏ: tách từng thuộc tính dữ liệu thành REQ riêng, hoặc tách bước thao tác thành REQ ("Bạn đọc nhập mã thẻ", "Bạn đọc nhập mã sách"). Dấu hiệu: REQ không có giá trị nghiệp vụ khi đứng một mình.
  - Diễn giải sai: đổi "tối đa" thành "khoảng", đổi "phải" thành "nên", bỏ mất điều kiện.
  - Thêm ý: viết "Hệ thống gửi email xác nhận" khi nguồn chỉ nói "thông báo cho khách".
  - Viết thành giải pháp: "Hệ thống lưu vào bảng orders" thay vì yêu cầu nghiệp vụ.
- Ví dụ đúng:
  - REQ-05 | Bạn đọc có thể gia hạn phiếu mượn trước ngày hết hạn. | Chức năng | "Bạn đọc được gia hạn sách trước hạn trả" (Mục 2, đoạn 3) | Không có
  - REQ-06 | Mỗi phiếu mượn được gia hạn tối đa 1 lần. | Quy tắc nghiệp vụ | "... và chỉ được gia hạn một lần" (Mục 2, đoạn 3) | Tách từ cùng câu với REQ-05
  - REQ-13 | Khách hàng có thể thanh toán đơn hàng trực tuyến trước khi đơn được chuyển cho nhà hàng. | Chức năng | "Thanh toán online qua cổng thanh toán rồi mới chuyển đơn cho quán" (Đoạn 4) | Kênh: cổng thanh toán (REQ-14). Xem Q-02 về trường hợp thanh toán thất bại
  - REQ-14 | Hệ thống trao đổi thông tin đơn hàng và kết quả thanh toán với cổng thanh toán để thu tiền đơn hàng. | Giao tiếp ngoài | "Thanh toán online qua cổng thanh toán rồi mới chuyển đơn cho quán" (Đoạn 4) | Tách từ cùng câu với REQ-13
- Ví dụ sai:
  - "Thủ kho nhập kho, xuất kho và kiểm kê định kỳ bằng máy quét." (gộp ba chức năng và một ràng buộc thiết bị)
  - "Hệ thống phải nhanh." (không đo được; nguồn nói gì thì giữ nguyên câu đó, nhưng phải có Q-nn hỏi ngưỡng)

- Loại: một trong sáu giá trị Chức năng / Phi chức năng / Quy tắc nghiệp vụ / Dữ liệu / Giao tiếp ngoài / Ràng buộc, chọn theo mục F3.
- Trích nguồn: câu gốc trong ngoặc kép, rút gọn bằng "..." nếu dài, kèm vị trí (tên tài liệu nếu có nhiều tài liệu, mục, đoạn, dòng). Một REQ có thể trích nhiều chỗ, ngăn bằng <br>. REQ dựa trên giả định ghi "Giả định ASM-nn" thay cho câu trích.
- Ghi chú: mã Q-nn, ASM-nn liên quan; quan hệ với REQ khác ("Tách từ cùng câu với REQ-xx", "Mâu thuẫn với REQ-yy", "Trùng REQ-zz"); trạng thái "Loại" khi chạy lại. Không có thì ghi "Không có".

F3. Cây quyết định phân loại
Hỏi theo thứ tự, dừng ở câu trả lời "Có" đầu tiên:
1. Câu chỉ mô tả việc trao đổi với hệ thống, thiết bị, dịch vụ bên ngoài (kênh, dữ liệu, giao thức) mà không nêu hành vi nghiệp vụ? --> Giao tiếp ngoài. Ví dụ: "Việc thanh toán dùng cổng thanh toán của ngân hàng qua API có sẵn", "Đọc mã vạch từ máy quét". Câu nêu hành vi nghiệp vụ và chỉ nhắc hệ thống ngoài như kênh thực hiện thì đi tiếp các câu sau, ghi hệ thống ngoài ở cột Ghi chú. Ví dụ: "Hệ thống gửi email xác nhận cho khách khi đơn được giao" là Chức năng, Ghi chú "Kênh: dịch vụ email ngoài". Mỗi hệ thống, thiết bị ngoài mà nguồn hoặc HE_THONG_NGOAI nêu có một REQ Giao tiếp ngoài riêng; REQ hành vi chỉ ghi kênh ở cột Ghi chú và trỏ tới REQ Giao tiếp ngoài đó, không đổi loại thành Giao tiếp ngoài.
2. Câu giới hạn cách xây dựng giải pháp (công nghệ, nền tảng, ngôn ngữ, chuẩn, luật, hạn chót, ngân sách) mà không mô tả hành vi? --> Ràng buộc. Ví dụ: "Phải chạy trên trình duyệt", "Phải tuân thủ quy định bảo vệ dữ liệu cá nhân". Chỉ câu bắt buộc nền tảng hoặc công nghệ là Ràng buộc; câu về mức dùng được trên một nền tảng đi tiếp câu 3.
3. Câu nêu mức chất lượng của hành vi (nhanh đến đâu, sẵn sàng bao lâu, bảo mật thế nào, dễ dùng thế nào, bao nhiêu người dùng đồng thời)? --> Phi chức năng. Ví dụ: "Trả kết quả tìm kiếm trong 2 giây". Câu về mức dùng được trên một nền tảng ("dùng tốt trên máy tính bảng") là Phi chức năng; chỉ câu bắt buộc nền tảng ("phải chạy trên trình duyệt") là Ràng buộc.
4. Câu nêu chính sách, giới hạn, công thức, điều kiện nghiệp vụ mà tổ chức đặt ra, vẫn đúng kể cả khi làm bằng tay không có phần mềm? --> Quy tắc nghiệp vụ. Ví dụ: "Phí trả sách muộn 5.000 đồng mỗi ngày", "Đơn dưới 100.000 đồng tính phí giao 15.000 đồng".
5. Câu mô tả thông tin cần lưu giữ, thành phần của một đối tượng dữ liệu, thời gian lưu trữ? --> Dữ liệu. Ví dụ: "Hồ sơ bệnh nhân gồm họ tên, ngày sinh, số điện thoại".
6. Câu mô tả việc ai đó làm được gì với hệ thống, hoặc hệ thống tự làm gì khi có sự kiện? --> Chức năng.
Nếu một câu vẫn mang hai loại sau khi đã tách theo F2, câu đó chưa nguyên tử; quay lại F2.
Nhầm lẫn hay gặp: coi quy tắc nghiệp vụ là phi chức năng ("tối đa 5 cuốn" không phải hiệu năng); coi chức năng bảo mật (đăng nhập, phân quyền theo vai trò) là phi chức năng thuần tuý. Quy ước: hành vi người dùng thực hiện được (đăng nhập, đổi mật khẩu) là Chức năng; mức độ bảo vệ (mật khẩu tối thiểu 8 ký tự, khoá sau 5 lần sai) là Quy tắc nghiệp vụ hoặc Phi chức năng tuỳ nguồn nói đó là chính sách tổ chức hay yêu cầu chất lượng; khi không rõ, chọn Phi chức năng và ghi chú. Câu nêu vai trò nào được dùng một chức năng (kể cả "không cần đăng nhập") ghi vào chủ thể hoặc điều kiện của REQ chức năng đó, không tách REQ riêng.

F4. Phạm vi và các bên liên quan
- Phạm vi: hai danh sách "Trong phạm vi" và "Ngoài phạm vi" (thêm danh sách "Chờ Q-nn" khi có mâu thuẫn phạm vi, xem dưới), mỗi dòng một mục, trỏ tới REQ hoặc câu trích. Ngoài phạm vi chỉ gồm điều nguồn nói rõ, hoặc do TRONG_TAM_PHAN_TICH loại, hoặc là hệ thống khác mà hệ thống này chỉ trao đổi dữ liệu. Không tự loại chức năng.
  - Đúng: "Ngoài phạm vi: thanh toán lương cho tài xế (nguồn: 'việc trả lương do phần mềm kế toán hiện có đảm nhiệm')".
  - Sai: "Ngoài phạm vi: báo cáo thống kê" khi nguồn không nói gì về báo cáo (đây là chỗ thiếu, phải thành Q-nn nếu cần hỏi, không phải ngoài phạm vi).
  - Câu nêu phạm vi (thường là câu loại trừ) mâu thuẫn với đoạn mô tả chi tiết của cùng chức năng: không tự chọn bên nào. Tạo Q-nn trích nguyên văn cả hai câu, ghi một dòng "Mâu thuẫn" ở F7, và xếp Q-nn này vào nhóm câu hỏi làm đổi phạm vi ở F9. Ở chế độ NGHIEM_NGAT, thêm danh sách thứ ba "Chờ Q-nn" gồm chức năng đó và các REQ liên quan; cột Ghi chú của các REQ đó ghi "Chờ Q-nn (phạm vi)". Ở chế độ CO_NHAN, tạo ASM-nn nêu lựa chọn (Trong hay Ngoài phạm vi) và lý do, xếp chức năng theo ASM đó, ghi mã ASM cạnh dòng phạm vi, và vẫn giữ Q-nn.
  - Ví dụ (thư viện): "Đoạn 1: 'hệ thống không xử lý việc thu phí thành viên'; Đoạn 6: 'thủ thư ghi nhận phí thành viên hằng năm và in biên lai'" --> Q-nn "Ghi nhận phí thành viên có thuộc phạm vi hệ thống không? (Có / Không)".
- Bảng bên liên quan: | SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống (Có / Không / Chưa rõ) | REQ |
- SH: mã SH-nn theo Conventions C3, cấp theo thứ tự xuất hiện, không đổi khi chạy lại. P01 dẫn mã này khi phân biệt tác nhân với bên liên quan.
  - Loại: Người dùng trực tiếp / Người hưởng lợi gián tiếp / Chủ sở hữu, người đặt hàng / Người vận hành, quản trị / Cơ quan quản lý / Hệ thống hoặc thiết bị ngoài.
  - Bên liên quan khác tác nhân: tác nhân là vai trò tương tác trực tiếp với hệ thống (xác định ở bước sau). Bên liên quan gồm cả người không chạm vào hệ thống, ví dụ chủ phòng khám chỉ đọc báo cáo in ra, cơ quan thuế.
  - Lỗi thường gặp: ghi tên người cụ thể thay vì vai trò ("anh Nam kế toán"); ghi bộ phận của đội phát triển ("lập trình viên"); bỏ sót bên liên quan hệ thống ngoài.

F5. Tám đặc tính kiểm tra từng REQ (theo ISO/IEC/IEEE 29148)
| Đặc tính | Câu hỏi kiểm tra | Dấu hiệu vi phạm |
|---|---|---|
| Cần thiết (necessary) | Bỏ REQ này thì hệ thống có thiếu điều bên liên quan cần không? | REQ do AI thêm, không có câu trích |
| Rõ nghĩa (unambiguous) | Có đúng một cách hiểu không? | Có từ ở mục F6, đại từ không rõ chỉ ai |
| Đầy đủ (complete) | Đủ chủ thể, hành động, đối tượng, điều kiện, ngưỡng chưa? | "Hệ thống thông báo" mà không rõ thông báo cho ai |
| Đơn nhất (singular) | Chỉ một năng lực, một đặc tính? | Hai động từ chính, "và/hoặc" nối hai ý |
| Khả thi (feasible) | Có thể thực hiện trong ràng buộc đã nêu? | "Không bao giờ lỗi", "phản hồi tức thì" |
| Kiểm chứng được (verifiable) | Có thể viết kiểm thử đạt/không đạt? | Không có ngưỡng đo, từ chủ quan |
| Đúng (correct) | Có phản ánh đúng ý nguồn? | Đổi con số, đổi mức bắt buộc |
| Tuân thủ (conforming) | Viết theo mẫu câu F2, đúng mã, đúng loại? | Sai mẫu, thiếu trích nguồn |
Nguồn vi phạm đặc tính thì REQ vẫn giữ đúng ý nguồn (không tự sửa cho "đẹp"), nhưng phải ghi vấn đề ở mục 5 và tạo Q-nn nếu cần người có thẩm quyền quyết định.

F6. Từ và cấu trúc cần cảnh giác
- Chủ quan: dễ dùng, thân thiện, trực quan, đẹp, hiện đại, linh hoạt, mạnh mẽ, hiệu quả. (user-friendly, easy, flexible, efficient)
- Mức độ không định lượng: nhanh, chậm, nhiều, ít, lớn, đáng kể, tối thiểu, tối đa (không kèm số), kịp thời, thường xuyên, định kỳ (không kèm chu kỳ), gần như luôn luôn.
- So sánh, cực cấp không mốc: tốt hơn, nhanh hơn, tốt nhất, tối ưu.
- Kẽ hở: nếu có thể, khi cần thiết, khi phù hợp, tuỳ trường hợp, nếu áp dụng được. (if possible, as appropriate, as applicable)
- Mở, không đóng: v.v., ..., bao gồm nhưng không giới hạn, các thông tin liên quan, và các chức năng khác, hỗ trợ. (etc., including but not limited to, support)
- Tổng thể tuyệt đối: tất cả, mọi, luôn luôn, không bao giờ, 100%, khi nói về độ phủ hoặc độ tin cậy ("sẵn sàng 100%", "mọi khách hàng đều nhận được"). Cần xác nhận có ngoại lệ không. Tỉ lệ hoặc con số nghiệp vụ xác định ("hoàn 100% tiền cọc", "giảm 100% phí giao") và "tối đa", "tối thiểu" có kèm số không thuộc F6, không cần dòng ở mục 5.
- Đại từ, tham chiếu mơ hồ: nó, cái này, việc đó, như trên, thông tin đó, người dùng (khi hệ thống có nhiều vai trò).
- Phủ định kép, câu bị động không có chủ thể: "đơn được duyệt" (ai duyệt?).
- Tham chiếu không đầy đủ: "theo quy định hiện hành", "theo mẫu của phòng" mà không đính kèm.
Cách xử lý: giữ nguyên từ đó trong Nội dung chuẩn hoá nếu nguồn chỉ có vậy, đặt trong ngoặc kép, ghi vấn đề ở mục 5 và tạo Q-nn hỏi giá trị cụ thể. Không tự thay bằng con số (trừ chế độ CO_NHAN với ASM-nn).

F7. Vấn đề chất lượng của tài liệu nguồn
Bảng: | STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
- Loại vấn đề: Mơ hồ / Mâu thuẫn / Thiếu / Không kiểm chứng được / Không khả thi / Trùng lặp.
- Thiếu chỉ ghi khi nguồn gợi ý có điều đó nhưng không nói rõ. Ví dụ: nguồn nói "khách hàng thanh toán online" nhưng không nói điều gì xảy ra khi thanh toán thất bại, trong khi các bước sau cần biết để viết luồng ngoại lệ. Không ghi "Thiếu" cho mọi chức năng mà loại hệ thống này thường có (đó là dùng hiểu biết chung, vi phạm Conventions C1.1).
- Mâu thuẫn phải trích cả hai câu. Ví dụ: "Đoạn 2: 'đặt phòng trước tối đa 30 ngày'; Đoạn 5: 'khách đoàn được đặt trước 90 ngày'". Nếu hai câu hoà giải được bằng điều kiện (khách lẻ và khách đoàn), ghi là "Không mâu thuẫn, tách thành hai REQ có điều kiện" và không tạo Q.

F8. Ma trận phủ nguồn
Bảng: | Vị trí trong nguồn | Tóm tắt nội dung | Kết luận (REQ-xx / Ngoài phạm vi / Bối cảnh) |
Mỗi đoạn hoặc mỗi câu mang ý trong nguồn có ít nhất một dòng. Mục đích: chứng minh không bỏ sót và không thêm.

F9. Câu hỏi mở
Theo Conventions C5: | Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
- Câu hỏi đóng hoặc có phương án, trả lời được trong một câu. Đúng: "Khi số lượng sách còn 0, bạn đọc có được đặt giữ chỗ không? (Có / Không)". Sai: "Hãy mô tả thêm nghiệp vụ mượn sách."
- Cột "Ảnh hưởng tới" ghi REQ và bước bị ảnh hưởng, ví dụ "REQ-07, luồng ngoại lệ của UC đặt món".
- Gom câu hỏi trùng ý. Sắp theo mức ảnh hưởng: câu hỏi làm đổi phạm vi hoặc danh sách chức năng đứng trước.

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Mọi câu mang yêu cầu trong nguồn xuất hiện trong ma trận phủ nguồn với kết luận rõ ràng.
2. Mọi REQ có câu trích nguồn hoặc mã ASM; không có REQ nào không truy được về nguồn.
3. Mọi REQ đạt phép thử đơn nhất ở F2; không có REQ nào chứa hai động từ chính độc lập.
4. Quy tắc nghiệp vụ và ngưỡng phi chức năng đã tách khỏi câu chức năng chứa chúng.
5. Mọi REQ có đúng một loại trong sáu loại, phân loại theo cây F3.
6. Con số, đơn vị, mức bắt buộc trong REQ khớp nguyên văn với nguồn.
7. Mọi từ thuộc F6 xuất hiện trong REQ đã có dòng ở mục 5 và có Q-nn. Ở chế độ CO_NHAN, chỗ thiếu làm thay đổi danh sách chức năng hoặc phạm vi có thêm ASM-nn, và chức năng đó có REQ dựa trên giả định.
8. Không có chức năng, quy tắc, con số nào do AI tự thêm (chế độ NGHIEM_NGAT); mục Giả định không xuất hiện ở chế độ NGHIEM_NGAT.
9. Mục Ngoài phạm vi chỉ gồm điều nguồn nói rõ hoặc do TRONG_TAM_PHAN_TICH loại; chức năng có câu phạm vi mâu thuẫn với mô tả chi tiết nằm ở "Chờ Q-nn" (NGHIEM_NGAT) hoặc có ASM-nn (CO_NHAN), không bị tự xếp Trong hay Ngoài.
10. Bảng bên liên quan ghi vai trò, không ghi tên người; có cả hệ thống, thiết bị ngoài được nhắc trong nguồn.
11. Không có chi tiết công nghệ tự thêm (tên bảng, framework) ngoài những gì nguồn là Ràng buộc.
12. Khi chạy lại: mã REQ cũ được giữ; REQ bị loại vẫn còn dòng với trạng thái "Loại".
13. Định dạng tuân thủ Conventions C2, C5, C8: không em dash, không mũi tên Unicode, mỗi mục trống ghi "Không có".

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này, ưu tiên cao hơn quy tắc mặc định (trừ Conventions C1). Không dùng thì thay cả khối bằng "Không có" | Ví dụ: "Gộp mọi yêu cầu quản lý danh mục (thêm, sửa, xoá, xem) của cùng một đối tượng thành một REQ"; "Tài liệu nguồn có đánh số mục, trích nguồn chỉ cần ghi số mục"; "Thêm loại yêu cầu 'Báo cáo' tách khỏi 'Chức năng'"}}
````

## 5. Ghi chú cho người dùng

- Danh sách REQ quá dài (trên khoảng 80 REQ cho vài trang nguồn): thường do tách quá nhỏ ở mức thao tác hoặc thuộc tính. Nguồn dày ngưỡng định lượng (thời hạn, số tiền, tỷ lệ) cho nhiều REQ Quy tắc nghiệp vụ là bình thường; chỉ gộp khi REQ chức năng hoặc dữ liệu bị tách theo từng thao tác, từng thuộc tính. Thêm vào YEU_CAU_BO_SUNG quy định gộp, rồi chạy lại.
- Có quá nhiều câu hỏi mở: đây là dấu hiệu tốt về chất lượng phân tích, không phải lỗi của AI. Trả lời các câu hỏi ảnh hưởng tới phạm vi trước, bổ sung câu trả lời vào tài liệu nguồn (ví dụ file "tra-loi-cau-hoi.md" đặt cuối danh sách TAI_LIEU_NGUON), rồi chạy lại P00 kèm bản P00 cũ.
- AI tự "làm đẹp" yêu cầu (đổi "khoảng" thành con số, thêm chức năng hay gặp): nhắc lại chế độ NGHIEM_NGAT và yêu cầu đối chiếu cột Trích nguồn.
- Dùng độc lập: bước này dùng được riêng để rà soát chất lượng một tài liệu yêu cầu bất kỳ trước khi ký hợp đồng hoặc ước lượng. Chỉ cần đính kèm Conventions, một hồ sơ dự án tối giản (tên hệ thống, tài liệu nguồn, chế độ giả định) và tài liệu.

## 6. Căn cứ

- ISO/IEC/IEEE 29148:2018, Systems and software engineering - Life cycle processes - Requirements engineering: đặc tính của từng yêu cầu và của tập yêu cầu, tiêu chí ngôn ngữ yêu cầu (các từ mơ hồ cần tránh).
- ISO/IEC/IEEE 12207 (Software requirements analysis process): nội dung chính của mô tả yêu cầu (điều kiện môi trường, yêu cầu chức năng và giao tiếp, định nghĩa dữ liệu, yêu cầu phi chức năng, yêu cầu nghiệm thu).
- K. Wiegers, J. Beatty, Software Requirements, 3rd ed., Microsoft Press, 2013: phân loại yêu cầu, bên liên quan, viết yêu cầu tốt, tách quy tắc nghiệp vụ.
- I. Alexander, R. Stevens, Writing Better Requirements, Addison-Wesley, 2002.
- INCOSE, Guide for Writing Requirements (các quy tắc câu đơn nhất, tránh từ mơ hồ).
