# P06 - Đặc tả bổ sung (Supplementary Specification)

## 1. Mục đích

Bước này gom mọi yêu cầu không nằm gọn trong một use case: yêu cầu chức năng dùng chung cho nhiều use case, yêu cầu phi chức năng (khả dụng, tin cậy, hiệu năng, khả năng hỗ trợ, bảo mật...), ràng buộc thiết kế, giao tiếp với hệ thống ngoài, và danh sách quy tắc nghiệp vụ hợp nhất của toàn hệ thống. Mỗi yêu cầu phi chức năng được viết thành phát biểu đo được.

Kết quả là căn cứ để chọn kiến trúc, thiết kế giao tiếp hệ thống ngoài, thiết kế dữ liệu và kiểm thử. Bảng BR ở đây là danh sách chính thức; các đặc tả use case chỉ dẫn mã.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | 00-Conventions.md | Có | Luật chung |
| Đầu vào | project-profile.md | Có | Chế độ giả định, bối cảnh kỹ thuật, hệ thống ngoài, ràng buộc đặc thù |
| Đầu vào | Tài liệu nguồn trong TAI_LIEU_NGUON | Có | Câu gốc của NFR, ràng buộc |
| Đầu vào | P00-problem-brief.md | Có | REQ loại Phi chức năng, Quy tắc nghiệp vụ, Giao tiếp ngoài, Ràng buộc, Chức năng dùng chung |
| Đầu vào | P01-actors.md, P02-usecases.md | Có | Tác nhân hệ thống ngoài, mã UC để ghi phạm vi áp dụng; với P02 chỉ cần Mục 4 (bảng use case) và Mục 5 (ma trận REQ --> UC) |
| Đầu vào | P04-uc-specs/*.md | Có | Mục "Yêu cầu đặc biệt", bảng BR của từng use case |
| Đầu vào | P04-uc-specs/_BR-register.md | Có nếu đã tồn tại | Sổ đăng ký BR |
| Đầu vào | P05-glossary.md | Tuỳ chọn | Dùng đúng thuật ngữ |
| Đầu vào | P06-supplementary-spec.md bản cũ | Có khi chạy lại | Giữ mã NFR, BR |
| Đầu ra | P06-supplementary-spec.md | | NFR, ràng buộc, giao tiếp ngoài, BR hợp nhất |
| Đầu ra | P04-uc-specs/_BR-register.md | | Sổ BR đồng bộ với bảng BR hợp nhất (cập nhật trạng thái Gộp, Loại) |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md, tài liệu nguồn, P00, P01, P02 (chỉ cần Mục 4 và Mục 5), mọi đặc tả P04, sổ BR, P05 (nếu có), bản P06 cũ (nếu chạy lại). Không cần P03.
- Chạy một lần cho toàn hệ thống, sau khi đã đặc tả xong các use case. Chạy lại khi thêm đặc tả use case mới hoặc khi NFR trong nguồn thay đổi.
- Placeholder trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| MO_HINH_CHAT_LUONG | Tuỳ chọn | Chọn cách nhóm NFR chính: FURPS+ (mặc định) hay ISO/IEC 25010 |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Quy định riêng của dự án cho bước này |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md, tài liệu nguồn, P00-problem-brief.md, P01-actors.md, P02-usecases.md, các đặc tả P04-uc-specs/UC-nnn-*.md, P04-uc-specs/_BR-register.md (nếu có), và có thể có P05-glossary.md, bản P06 cũ.

Đây là bước P06 của pipeline: đặc tả bổ sung. Kết quả gồm yêu cầu chức năng dùng chung, yêu cầu phi chức năng đo được, ràng buộc thiết kế, giao tiếp ngoài, và bảng quy tắc nghiệp vụ hợp nhất. Bước kiến trúc đọc NFR để chọn mẫu kiến trúc; bước thiết kế giao tiếp hệ thống đọc mục giao tiếp ngoài; bước thiết kế lớp, dữ liệu và kiểm thử đọc bảng BR.

Cách nhóm yêu cầu phi chức năng:
{{PH:MO_HINH_CHAT_LUONG | Hướng dẫn: [TUỲ CHỌN] chọn "FURPS+" (mặc định, cột Nhóm ghi nhóm FURPS+ và đặc tính ISO/IEC 25010 tương ứng) hoặc "ISO/IEC 25010" (cột Nhóm ghi đặc tính ISO trước, FURPS+ sau). Dùng mặc định thì thay cả khối bằng "Không có" | Ví dụ: "FURPS+"; "ISO/IEC 25010, bản 2023"}}

[Role]
Bạn là kỹ sư yêu cầu phụ trách yêu cầu chất lượng và quy tắc nghiệp vụ, thành thạo FURPS+, ISO/IEC 25010 và cách viết yêu cầu phi chức năng định lượng. Bạn không tự đặt ngưỡng thay cho bên liên quan.

[Action]
Thực hiện tuần tự:

1. Nếu có bản P06 cũ: giữ nguyên mã NFR, BR; phần tử bỏ đi giữ mã và ghi trạng thái "Loại"; phần tử mới lấy mã tiếp nối.
2. Thu thập ứng viên NFR: mọi REQ loại Phi chức năng, Ràng buộc, Giao tiếp ngoài trong P00; mọi dòng "Yêu cầu đặc biệt" trong các đặc tả P04; các trường HE_THONG_NGOAI, NEN_TANG, RANG_BUOC_DAC_THU trong hồ sơ dự án (nếu đã chốt).
3. Thu thập yêu cầu chức năng dùng chung: REQ loại Chức năng áp dụng cho nhiều use case mà không phải là một use case (ghi nhật ký thao tác, phân quyền theo vai trò, định dạng tiền tệ thống nhất, gửi thông báo theo một kênh chung, đa ngôn ngữ). Chỉ lấy khi có REQ.
4. Phân loại từng ứng viên theo phép thử ở mục F2 (chức năng, phi chức năng hay quy tắc nghiệp vụ). Ứng viên thực chất là quy tắc nghiệp vụ thì chuyển sang bước 8. Ứng viên thực chất là chức năng riêng của một use case thì ghi vào "Đề xuất sửa artifact trước" cho P02 hoặc P04.
5. Xếp nhóm theo FURPS+ và đối chiếu ISO/IEC 25010 theo bảng ở mục F3.
6. Viết từng NFR thành phát biểu đo được theo F4: đại lượng, ngưỡng, đơn vị, điều kiện đo, phương pháp đo. Nếu nguồn không có ngưỡng: giữ phát biểu định tính theo nguồn, ghi Tiêu chí đo là "Chưa đo được", tạo Q-nn đề nghị bên liên quan chọn ngưỡng (NGHIEM_NGAT) hoặc tạo ASM-nn với ngưỡng đề xuất và lý do (CO_NHAN).
7. Xác định phạm vi áp dụng: toàn hệ thống, hoặc danh sách UC cụ thể. NFR đến từ mục "Yêu cầu đặc biệt" của một đặc tả P04 thì áp dụng cho UC đó.
8. Hợp nhất quy tắc nghiệp vụ theo F6:
   a. Nạp toàn bộ sổ BR và bảng BR của mọi đặc tả P04.
   b. Phát hiện trùng mã (cùng mã, khác nội dung, thường do chạy P04 song song): giữ mã cho quy tắc được cấp trước, cấp mã mới tiếp nối cho quy tắc kia, ghi vào "Đề xuất sửa artifact trước" đặc tả P04 cần đổi mã.
   c. Phát hiện trùng nghĩa (khác mã, cùng nội dung): giữ mã nhỏ hơn ở trạng thái "Hiệu lực", mã lớn hơn chuyển trạng thái "Gộp vào BR-xx"; ghi đề xuất sửa đặc tả P04 đang dùng mã bị gộp.
   d. Phát hiện mâu thuẫn giữa hai BR: giữ cả hai, tạo Q-nn.
   e. Rà mọi REQ loại Quy tắc nghiệp vụ trong P00: REQ nào chưa có BR (vì chưa đặc tả P04 nào dùng tới) thì cấp BR mới tiếp nối; cột "Áp dụng cho UC" lấy các UC gắn với REQ đó trong ma trận truy vết REQ --> UC (Mục 5) của P02, kể cả UC chưa có đặc tả P04. Chỉ ghi "Chưa gắn UC" khi P02 cũng không gắn REQ đó với UC nào, và khi đó thêm Q-nn nếu có thể thiếu use case.
   f. Hợp nhất danh sách UC áp dụng của mỗi BR.
   Không sửa nội dung quy tắc đã chốt; nội dung cần sửa thì ghi đề xuất.
9. Lập mục giao tiếp ngoài và ràng buộc thiết kế theo F5.
10. Cập nhật sổ BR cho khớp bảng BR hợp nhất (trạng thái, UC áp dụng, BR mới) và xuất lại toàn bộ sổ.
11. Chạy checklist ở phần [Target], sửa những gì chưa đạt, ghi phần không sửa được vào mục "Vấn đề còn mở".

[Format]
Xuất hai nội dung. Nếu có quyền ghi file thì ghi thành file; nếu không thì in lần lượt, mỗi nội dung mở đầu bằng một dòng "File: <đường dẫn>".

A. File P06-supplementary-spec.md theo khung C5, gồm đúng các mục sau theo thứ tự:

# P06 - Đặc tả bổ sung - <TEN_HE_THONG>
(bảng thông tin theo C5)
## 1. Giới thiệu
## 2. Yêu cầu chức năng dùng chung
## 3. Yêu cầu phi chức năng
## 4. Ràng buộc thiết kế
## 5. Giao tiếp ngoài
## 6. Quy tắc nghiệp vụ
## 7. Ma trận truy vết
## Câu hỏi mở
## Giả định  (chỉ khi CO_NHAN)
## Đề xuất sửa artifact trước
## Vấn đề còn mở

B. File P04-uc-specs/_BR-register.md đã đồng bộ, cùng mẫu cột như bước đặc tả use case: | BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái |. BR cấp ở bước này ghi "Cấp lần đầu tại" là "P06".

Mục 2, 3, 4, 5 dùng chung một dãy mã NFR-nn (Conventions C3) và cùng mẫu bảng lõi:
| NFR | Nhóm (FURPS+ / ISO 25010) | Phát biểu đo được | Tiêu chí đo | Áp dụng cho (UC / toàn hệ thống) | REQ |
Mã cấp theo thứ tự xuất hiện qua các mục 2, 3, 4, 5. Mục không có phần tử ghi "Không có".

Quy tắc chi tiết:

F1. Giới thiệu
2-4 câu: mục đích, phạm vi, quan hệ với đặc tả use case (yêu cầu riêng của một use case nằm ở đặc tả use case đó; tài liệu này chứa yêu cầu chung và danh sách BR chính thức).

F2. Phân biệt yêu cầu chức năng, phi chức năng, quy tắc nghiệp vụ, ràng buộc
| Loại | Câu hỏi nhận biết | Ví dụ |
|---|---|---|
| Chức năng | Hệ thống làm gì, tác nhân làm được gì? | "Lễ tân có thể huỷ lịch hẹn của bệnh nhân" |
| Phi chức năng | Hệ thống làm việc đó tốt đến mức nào (nhanh, ổn định, an toàn, dễ dùng, dễ sửa)? | "Tìm sách trả kết quả trong không quá 2 giây ở phân vị 95" |
| Quy tắc nghiệp vụ | Tổ chức quy định điều gì, vẫn đúng khi làm bằng tay? | "Bạn đọc mượn tối đa 5 cuốn" |
| Ràng buộc thiết kế | Điều gì giới hạn lựa chọn giải pháp? | "Phải dùng hệ quản trị CSDL mà công ty đã có giấy phép" |
Phép thử nhanh: bỏ phần mềm đi, câu vẫn có nghĩa với nhân viên --> quy tắc nghiệp vụ. Câu chứa đơn vị đo chất lượng (giây, %, giờ, số người dùng đồng thời) --> phi chức năng. Câu nói tới hành động --> chức năng. Câu nói tới công nghệ, nền tảng, chuẩn, luật mà không nói hành vi --> ràng buộc.
Nhầm lẫn hay gặp:
- "Hệ thống phải có chức năng đăng nhập" là chức năng, không phải NFR bảo mật. NFR bảo mật là "Mật khẩu được lưu dưới dạng băm một chiều có muối; không nhân viên nào đọc được mật khẩu gốc".
- "Khoá tài khoản sau 5 lần đăng nhập sai liên tiếp" là quy tắc (chính sách an ninh của tổ chức), có thể xếp BR loại Ràng buộc hoặc NFR nhóm Security; chọn theo cách nguồn trình bày và ghi lý do ở Ghi chú. Không ghi ở cả hai nơi.
- "Giao diện thân thiện" là NFR Usability nhưng chưa đo được.

F3. Nhóm FURPS+ và đối chiếu ISO/IEC 25010
| FURPS+ | Nội dung | Đặc tính ISO/IEC 25010:2011 (tên trong bản 2023 nếu khác) |
|---|---|---|
| F - Functionality (chức năng dùng chung) | Chức năng áp dụng cho nhiều use case: phân quyền, nhật ký, thông báo, in ấn, đa ngôn ngữ; bảo mật | Functional suitability; Security |
| U - Usability | Dễ học, dễ dùng, thời gian đào tạo, hỗ trợ trợ năng, thông báo lỗi, tài liệu trợ giúp | Usability (Interaction capability) |
| R - Reliability | Độ sẵn sàng, thời gian trung bình giữa hai lần hỏng (MTBF), thời gian khôi phục (MTTR), chịu lỗi, sao lưu, độ chính xác của tính toán | Reliability |
| P - Performance | Thời gian phản hồi, thông lượng, số người dùng đồng thời, dung lượng dữ liệu, sử dụng tài nguyên | Performance efficiency |
| S - Supportability | Dễ bảo trì, dễ cấu hình, dễ kiểm thử, dễ cài đặt, khả chuyển, tương thích | Maintainability; Portability (Flexibility); Compatibility |
| + Ràng buộc thiết kế | Công nghệ, nền tảng, ngôn ngữ, kiến trúc bắt buộc | Không tương ứng trực tiếp |
| + Giao tiếp (interface) | Giao tiếp với hệ thống ngoài, thiết bị, giao thức, định dạng dữ liệu | Compatibility (Interoperability) |
| + Cài đặt, vật lý, pháp lý | Yêu cầu triển khai, phần cứng, giấy phép, tuân thủ luật | Safety (bản 2023) khi liên quan an toàn |
Cột Nhóm ghi dạng "P - Performance / Performance efficiency". Khi MO_HINH_CHAT_LUONG là ISO/IEC 25010 thì đảo thứ tự hai tên. Một NFR chỉ thuộc một nhóm; nếu thấy thuộc hai nhóm thì chưa nguyên tử, tách ra.

F4. Phát biểu đo được và tiêu chí đo
- Phát biểu đo được: một câu theo mẫu "<Đối tượng: hệ thống / chức năng / UC> <đại lượng> <so sánh> <ngưỡng> <đơn vị> <điều kiện>." Đối tượng phải cụ thể; đại lượng phải có tên; ngưỡng là con số hoặc tập giá trị lấy từ nguồn.
- Tiêu chí đo: cách kiểm chứng: phương pháp (đo tự động, kiểm thử tải, khảo sát người dùng, kiểm tra mã nguồn, thống kê vận hành), điều kiện đo (tải, dữ liệu mẫu, môi trường, cấu hình), cách tính (trung bình, phân vị 95, tỷ lệ theo tháng), và mức đạt. Tham khảo cách viết Scale / Meter / Must của Planguage.
- Mức hợp lý: đọc xong hai cột, người kiểm thử viết được kịch bản kiểm thử có kết quả đạt hoặc không đạt. Mỗi NFR một đại lượng.
- Mỗi phần của Tiêu chí đo (phương pháp, điều kiện đo, cách tính, mức đạt) chỉ ghi điều nguồn nêu. Nguồn không nêu cách tính hoặc điều kiện đo thì ghi "Chưa quy định (Q-nn)" ở phần đó và tạo câu hỏi mở (CO_NHAN: ASM-nn). Không lấy cách tính, số liệu từ ví dụ trong prompt này.
- NFR dạng có/không (không lưu dữ liệu X, dùng giao thức Y, chạy trên nền tảng Z): Tiêu chí đo là kiểm tra đặc tính đó trên sản phẩm (xem xét mã nguồn, dữ liệu lưu trữ, cấu hình triển khai, kiểm thử tích hợp), mức đạt là đặc tính có hoặc không; không có điều kiện đo và cách tính, không cần Q-nn cho phương pháp.
- Nguồn định tính, không có ngưỡng: giữ nguyên ý nguồn trong ngoặc kép, Tiêu chí đo ghi "Chưa đo được (Q-nn)" và câu hỏi đề xuất đại lượng cần chốt, ví dụ "Dễ dùng: người dùng mới hoàn thành đặt lịch lần đầu không cần hướng dẫn trong bao nhiêu phút?". Không tự điền con số ở chế độ NGHIEM_NGAT.
- Ví dụ đúng:
  | NFR-03 | P - Performance / Performance efficiency | Chức năng tra cứu khung giờ trống trả kết quả trong không quá 2 giây với 150 người dùng đồng thời. | Kiểm thử tải 150 phiên đồng thời gọi chức năng tra cứu khung giờ trống; mức đạt: thời gian từ khi gửi yêu cầu tới khi nhận đủ dữ liệu không quá 2 giây; cách tính và dữ liệu mẫu: Chưa quy định (Q-12) | UC-002, UC-003 | REQ-21 |
  | NFR-07 | R - Reliability / Reliability | Hệ thống sẵn sàng phục vụ ít nhất 99,5% thời gian mỗi tháng, trừ lịch bảo trì đã thông báo trước. | Thống kê giám sát vận hành theo tháng: (tổng phút trong tháng - phút ngừng ngoài kế hoạch) / tổng phút trong tháng | Toàn hệ thống | REQ-30 |
  | NFR-09 | U - Usability / Usability | "Giao diện dùng tốt trên máy tính bảng." | Chưa đo được (Q-07): cần chốt kích thước màn hình tối thiểu và các chức năng phải dùng được | Toàn hệ thống | REQ-22 |
- Ví dụ sai:
  | NFR-01 | Performance | Hệ thống phải nhanh. | Nhanh | Toàn hệ thống | REQ-20 | (không đại lượng, không ngưỡng, tiêu chí lặp lại phát biểu)
  | NFR-02 | Reliability | Hệ thống không bao giờ lỗi. | | | | (không khả thi, không đo được, thiếu truy vết)
  | NFR-05 | Performance | Hệ thống phản hồi trong 1 giây. | Đo | Toàn hệ thống | | (ngưỡng do AI tự thêm, không có REQ; thiếu điều kiện tải, cách tính)
- Lỗi thường gặp: gom nhiều đại lượng vào một NFR ("nhanh và ổn định"); ghi mục tiêu thiết kế thay vì yêu cầu ("dùng cache để tăng tốc" là giải pháp); ghi ngưỡng không có điều kiện ("1 giây" lúc bình thường hay lúc cao điểm?); tách một yêu cầu có hai điều kiện thành hai NFR mâu thuẫn thay vì ghi rõ điều kiện từng ngưỡng.

F5. Ràng buộc thiết kế và giao tiếp ngoài
- Ràng buộc thiết kế (mục 4): chỉ gồm điều nguồn hoặc hồ sơ dự án đã chốt (NEN_TANG, CONG_NGHE, RANG_BUOC_DAC_THU): nền tảng, ngôn ngữ, hệ quản trị dữ liệu, chuẩn bắt buộc, luật. Mỗi ràng buộc ghi lý do nếu nguồn có. Nhóm: "+ Ràng buộc thiết kế". Hồ sơ ghi "Chưa chốt" thì không tạo ràng buộc từ trường đó của hồ sơ; REQ loại Ràng buộc của P00 (ví dụ nguồn yêu cầu có ứng dụng di động cho khách) vẫn thành NFR như mọi REQ khác.
  - Đúng: | NFR-12 | + Ràng buộc thiết kế | Ứng dụng khách chạy trên trình duyệt web, không yêu cầu cài đặt. | Kiểm tra triển khai: truy cập đủ chức năng từ trình duyệt mà không cài thêm phần mềm | Toàn hệ thống | REQ-02 |
  - Sai: "Dùng kiến trúc microservices" khi nguồn không yêu cầu (đây là quyết định thiết kế của bước kiến trúc).
- Giao tiếp ngoài (mục 5): mỗi hệ thống, thiết bị ngoài một hoặc vài NFR, nhóm "+ Giao tiếp / Compatibility". Phát biểu nêu: hệ thống ngoài nào (dẫn mã ACT nếu là tác nhân), dữ liệu trao đổi, chiều trao đổi, giao thức hoặc tài liệu API nếu nguồn có, hành vi khi hệ thống ngoài không phản hồi nếu nguồn có. Không thiết kế chi tiết operation (đó là bước thiết kế giao tiếp hệ thống).
  - Đúng: | NFR-14 | + Giao tiếp / Compatibility | Hệ thống gửi tin nhắn SMS tới bệnh nhân thông qua API có sẵn của nhà cung cấp dịch vụ SMS (ACT-05). | Kiểm thử tích hợp với môi trường thử của nhà cung cấp: tin nhắn được chấp nhận và có mã xác nhận gửi | UC-003, UC-006 | REQ-35 |

F6. Quy tắc nghiệp vụ hợp nhất (mục 6)
Bảng: | BR | Quy tắc | Loại | Áp dụng cho UC | REQ | Trạng thái | Ghi chú |
- Bảng này là danh sách chính thức. Cột lõi BR, Quy tắc, Loại, Áp dụng cho UC, REQ giữ nguyên nội dung từ sổ BR; thêm Trạng thái và Ghi chú.
- Loại: Sự kiện / Ràng buộc / Kích hoạt hành động / Suy luận / Tính toán.
  - Sự kiện: "Mỗi phiếu mượn thuộc về đúng một bạn đọc."
  - Ràng buộc: "Khách hàng chỉ được huỷ đơn khi nhà hàng chưa xác nhận đơn."
  - Kích hoạt hành động: "Khi tồn kho khả dụng của một mặt hàng xuống dưới mức tối thiểu, thông báo cho thủ kho."
  - Suy luận: "Bạn đọc có sách quá hạn trên 30 ngày được coi là bạn đọc bị hạn chế."
  - Tính toán: "Phí trả muộn = số ngày trễ x 5.000 đồng, tối đa bằng giá bìa của sách."
- Trạng thái: Hiệu lực / Gộp vào BR-xx / Loại. Không xoá dòng, không đổi mã (Conventions C3).
- Áp dụng cho UC: hợp nhất từ sổ BR và các đặc tả P04; BR chưa có trong đặc tả P04 nào lấy UC từ ma trận REQ --> UC của P02; chỉ ghi "Chưa gắn UC" khi P02 cũng không gắn.
- Ghi chú: Q-nn, lý do gộp hoặc loại, mâu thuẫn với BR khác, nguồn phát hiện ("P04 UC-003", "P06").
- Phát biểu quy tắc: một câu nguyên tử, có ngưỡng, đơn vị, phạm vi; không chứa hành động giao diện; không chứa cách cài đặt ("kiểm tra bằng trigger").
- Lỗi thường gặp: để hai BR cùng nghĩa cùng "Hiệu lực"; đổi nội dung BR đã chốt để khớp cách hiểu của mình; cấp lại mã đã "Loại"; ghi NFR vào bảng BR.

F7. Ma trận truy vết (mục 7)
Hai bảng:
- REQ --> NFR/BR: | REQ | Loại REQ | NFR / BR | Ghi chú |, gồm mọi REQ loại Phi chức năng, Quy tắc nghiệp vụ, Giao tiếp ngoài, Ràng buộc trong P00. REQ không được phủ phải có lý do ở Ghi chú (ví dụ "Đã phủ bằng UC-004").
- UC --> NFR/BR: | UC | NFR | BR |, gồm mọi UC trong P02.

[Target]
Tự kiểm tra, mỗi câu trả lời Đạt hoặc Không đạt:
1. Mọi REQ loại Phi chức năng, Ràng buộc, Giao tiếp ngoài, Quy tắc nghiệp vụ trong P00 xuất hiện trong ma trận truy vết với NFR, BR hoặc lý do.
2. Mọi dòng "Yêu cầu đặc biệt" của các đặc tả P04 đã thành NFR có cột Áp dụng cho ghi đúng UC.
3. Mọi NFR có đúng một nhóm FURPS+ kèm đặc tính ISO/IEC 25010 tương ứng; mỗi NFR chỉ một đại lượng.
4. Mọi NFR có ngưỡng từ nguồn thì có phát biểu đo được và tiêu chí đo (phương pháp, điều kiện, cách tính); NFR không có ngưỡng thì ghi "Chưa đo được" kèm Q-nn (hoặc ASM-nn khi CO_NHAN).
5. Không có ngưỡng, công nghệ, ràng buộc nào do AI tự thêm ở chế độ NGHIEM_NGAT.
6. Không có phần tử nào vừa là NFR vừa là BR; không có chức năng riêng của một use case nằm trong mục 2.
7. Bảng BR chứa mọi BR của sổ BR và của mọi đặc tả P04; không có hai BR cùng mã khác nội dung; không có hai BR cùng nghĩa cùng trạng thái Hiệu lực.
8. Mọi REQ loại Quy tắc nghiệp vụ trong P00 có BR tương ứng.
9. BR mới có mã tiếp nối mã lớn nhất; không mã nào bị đổi, xoá, dùng lại.
10. Sổ BR xuất lại khớp hoàn toàn với bảng BR hợp nhất (mã, nội dung, trạng thái, UC áp dụng).
11. Mọi thay đổi cần làm ở đặc tả P04 (đổi mã do trùng, thay mã bị gộp) đã ghi ở "Đề xuất sửa artifact trước".
12. Định dạng theo Conventions C2, C5, C8; mục trống ghi "Không có".

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] quy định riêng của dự án cho bước này, ưu tiên cao hơn quy tắc mặc định (trừ Conventions C1). Không dùng thì thay cả khối bằng "Không có" | Ví dụ: "Thời gian phản hồi luôn đo ở phân vị 95"; "Bổ sung mục Yêu cầu pháp lý theo luật bảo vệ dữ liệu cá nhân"; "Khoá tài khoản sau nhiều lần đăng nhập sai luôn xếp vào BR, không xếp NFR"}}
````

## 5. Ghi chú cho người dùng

- Nhiều NFR ở trạng thái "Chưa đo được": đây là tình trạng bình thường với tài liệu yêu cầu thô. Mang các câu hỏi mở tới bên liên quan để chốt ngưỡng; ngưỡng NFR ảnh hưởng trực tiếp tới lựa chọn kiến trúc.
- Bước này có thể đề xuất đổi mã BR trong đặc tả use case (khi trùng mã hoặc gộp). Sửa các đặc tả đó theo mục "Đề xuất sửa artifact trước" trước khi chạy bước phân tích use case.
- Muốn dùng mẫu phân loại khác (ví dụ chỉ ISO/IEC 25010), điền MO_HINH_CHAT_LUONG; bảng lõi không đổi nên bước sau vẫn đọc được.
- Dùng độc lập: bước này dùng được để viết riêng danh sách yêu cầu phi chức năng đo được từ một tài liệu yêu cầu bất kỳ. Khi chưa có đặc tả use case và sổ BR, cột Áp dụng cho ghi "Toàn hệ thống" hoặc tên chức năng theo nguồn, và mọi BR được cấp mã tại bước này.

## 6. Căn cứ

- R. Grady, Practical Software Metrics for Project Management and Process Improvement, Prentice Hall, 1992: mô hình FURPS; phần mở rộng FURPS+ theo Rational Unified Process và C. Larman, Applying UML and Patterns, 3rd ed., 2004 (Supplementary Specification).
- ISO/IEC 25010:2011 và ISO/IEC 25010:2023, Systems and software Quality Requirements and Evaluation (SQuaRE) - Product quality model.
- ISO/IEC/IEEE 29148:2018: đặc tính yêu cầu tốt (kiểm chứng được, khả thi, đơn nhất).
- K. Wiegers, J. Beatty, Software Requirements, 3rd ed., 2013: yêu cầu thuộc tính chất lượng, phân loại quy tắc nghiệp vụ (fact, constraint, action enabler, inference, computation).
- T. Gilb, Competitive Engineering, Butterworth-Heinemann, 2005: Planguage (Scale, Meter, Must, Plan) cho yêu cầu định lượng.
- Business Rules Group, Defining Business Rules - What Are They Really?, 2000.
