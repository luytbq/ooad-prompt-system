# X2 - Thiết kế unit test (Unit Test Design)

## 1. Mục đích

Bước này thiết kế bộ test case mức đơn vị (unit: phương thức, lớp) cho các phương thức quan trọng của thiết kế lớp P12. Test case được suy ra có hệ thống bằng kỹ thuật hộp đen (phân vùng tương đương, phân tích giá trị biên, bảng quyết định, kiểm thử theo use case, chuyển trạng thái) từ đặc tả, sau đó bổ sung bằng kỹ thuật hộp trắng (độ phủ lệnh C0, độ phủ nhánh C1, đường đi cơ sở, vòng lặp) từ thiết kế method hoặc mã nguồn. Nguồn test là quy tắc nghiệp vụ, luồng thay thế của đặc tả use case và đặc tả phương thức. Tuỳ chọn sinh khung mã test theo ngôn ngữ của dự án.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md | Có | Ngôn ngữ lập trình, framework test (CONG_NGHE), chế độ giả định |
| Đầu vào | P12-class-design.md (hoặc P12-class-design/*.md) | Có | Chữ ký, tiền/hậu điều kiện, ngoại lệ, thiết kế method, state machine, quan hệ (để xác định phụ thuộc cần giả lập) |
| Đầu vào | P06-supplementary-spec.md | Có | BR (miền giá trị, điều kiện, công thức) |
| Đầu vào | P04-uc-specs/*.md | Có | Luồng chính, luồng thay thế/ngoại lệ, bảng dữ liệu vào/ra với điều kiện hợp lệ |
| Đầu vào | P13-data-model.md | Không | Ràng buộc dữ liệu (độ dài, NULL, CHECK) để bổ sung biên |
| Đầu vào | Mã nguồn của phương thức | Không | Kỹ thuật hộp trắng chính xác hơn thiết kế method |
| Đầu ra | X2-unit-tests.md | Có | Phân tích kỹ thuật, bảng test case, ma trận phủ, khung mã test (tuỳ chọn) |
| Đầu ra | diagrams/X2-cfg-<DC>-<operation>.drawio | (chỉ khi DAY_DU) Khi có phân tích hộp trắng | Đồ thị luồng điều khiển |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md và các file đầu vào ở bảng trên.
- Chạy theo nhóm lớp (một package hoặc vài lớp liên quan) để kết quả không quá dài; lần chạy sau đính kèm X2 đã có để tiếp tục đánh số TC.
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| PHAM_VI_TEST | Có | Lớp/phương thức cần thiết kế test, hoặc để AI chọn trong một package |
| MUC_TIEU_PHU | Tuỳ chọn | Mục tiêu độ phủ hộp trắng |
| SINH_MA_TEST | Tuỳ chọn | Có sinh khung mã test hay không, framework nào |
| MA_TC_BAT_DAU | Tuỳ chọn | Mã TC bắt đầu khi đã có lần chạy trước |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù khác |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md và các artifact: P12 (bắt buộc), P06, P04, P13 (nếu có), mã nguồn (nếu có).
Đọc hồ sơ dự án để biết CONG_NGHE (ngôn ngữ, framework test), CHE_DO_GIA_DINH, MUC_CHI_TIET.
Phạm vi thiết kế test:
{{PH:PHAM_VI_TEST | Hướng dẫn: liệt kê DC.operation cần test, hoặc ghi mã PKG/DC để AI tự chọn phương thức theo tiêu chí ở Bước 1 | Ví dụ: "DC-StockItem.issue, DC-IssueStockController.confirmIssue"; "Tự chọn trong PKG-02 Mượn trả"; "Mọi operation public của DC-Appointment"}}
Mục tiêu độ phủ hộp trắng:
{{PH:MUC_TIEU_PHU | Hướng dẫn: [TUỲ CHỌN] mức độ phủ cần đạt cho phương thức được chọn; dùng mặc định thì thay cả khối bằng "Không có" (100% C1 cho phương thức ưu tiên Cao, 100% C0 cho phương thức còn lại) | Ví dụ: "100% C1 cho mọi phương thức được chọn"; "100% C0, riêng phương thức tính tiền 100% C1 và đường đi cơ sở"}}
Sinh khung mã test:
{{PH:SINH_MA_TEST | Hướng dẫn: [TUỲ CHỌN] "Có" kèm framework test; chỉ cần thiết kế thì thay cả khối bằng "Không có" | Ví dụ: "Có, Java 17 + JUnit 5 + Mockito"; "Có, Python 3.12 + pytest + unittest.mock"; "Có, C# + xUnit + Moq"}}
Mã test case bắt đầu:
{{PH:MA_TC_BAT_DAU | Hướng dẫn: [TUỲ CHỌN] mã TC đầu tiên cho lần chạy này khi đã có X2 trước đó; lần đầu thì thay cả khối bằng "Không có" (bắt đầu TC-001) | Ví dụ: "TC-048"}}

[Role]
Bạn là kỹ sư kiểm thử phần mềm, thành thạo thiết kế test case hộp đen và hộp trắng (Myers, ISTQB), kiểm thử đơn vị với test double (stub, driver, mock, fake), và framework xUnit. Bạn suy ra kết quả mong đợi từ đặc tả, không từ hiện thực.

[Action]
Bước 0. Kiểm tra đầu vào.
- Kiểm tra placeholder theo Conventions C6.
- Nếu phương thức trong phạm vi thiếu tiền/hậu điều kiện hoặc ngoại lệ ở P12, ghi vào "Đề xuất sửa artifact trước" và dùng BR/P04 để thiết kế; chỗ không suy ra được kết quả mong đợi thì ghi Q (NGHIEM_NGAT) hoặc ASM (CO_NHAN).

Bước 1. Chọn phương thức cần test.
- Ưu tiên Cao: phương thức hiện thực BR (tính toán, kiểm tra điều kiện, giới hạn); phương thức có nhiều nhánh; phương thức là sự kiện của state machine; phương thức kiểm tra hợp lệ dữ liệu vào; phương thức điều phối luồng UC có nhiều luồng thay thế.
- Ưu tiên Trung bình: phương thức chuyển đổi, định dạng dữ liệu; phương thức gọi hệ thống ngoài qua interface (test với test double).
- Không cần unit test riêng: getter/setter không có logic, phương thức chỉ ủy quyền nguyên lời gọi, phương thức sinh tự động bởi framework; ghi lý do.

Bước 2. Thu thập cơ sở kiểm thử cho từng phương thức: chữ ký, tiền điều kiện, hậu điều kiện, ngoại lệ (P12 F2); thiết kế method (P12 F3); BR liên quan (P06); luồng thay thế/ngoại lệ liên quan (P04); điều kiện hợp lệ của trường dữ liệu (P04, P13); chuyển trạng thái (P12 F6) nếu phương thức là sự kiện.

Bước 3. Kỹ thuật hộp đen (luôn làm trước).
3.1. Phân vùng tương đương: với mỗi điều kiện đầu vào (tham số, trạng thái đối tượng, dữ liệu liên quan), chia miền thành các lớp mà mọi giá trị trong một lớp được kỳ vọng cho cùng kết quả. Luôn có cả lớp hợp lệ và lớp không hợp lệ (sai kiểu, ngoài miền, rỗng, null). Xét cả phân vùng theo đầu ra (mỗi kết quả khác nhau là một vùng).
3.2. Phân tích giá trị biên: với mỗi lớp có thứ tự, lấy giá trị ngay tại biên và ngay ngoài biên (min-1, min, max, max+1; thêm giá trị ngay trong biên min+1, max-1 khi phương thức có rủi ro cao). Biên có thể là biên của đầu vào, của đầu ra, của kích thước tập hợp, của thời gian.
3.3. Bảng quyết định: khi kết quả phụ thuộc tổ hợp của nhiều điều kiện. Liệt kê điều kiện (hàng), mọi tổ hợp (cột quy tắc, 2^n với n điều kiện nhị phân), hành động (hàng). Đánh dấu tổ hợp không thể xảy ra là N/A; gộp quy tắc có hành động giống nhau bằng giá trị "-" (không quan tâm) chỉ khi đặc tả cho biết thứ tự kiểm tra. Mỗi quy tắc còn lại ít nhất một test case.
3.4. Chuyển trạng thái (khi phương thức là sự kiện của state machine): mỗi chuyển hợp lệ một test case; với các cặp (trạng thái, sự kiện) không có chuyển, thiết kế test case kiểm tra phương thức từ chối đúng như đặc tả; mỗi guard xét cả đúng và sai, kèm giá trị biên của guard.
3.5. Theo use case (với phương thức điều phối của lớp control): một kịch bản cho luồng chính, một kịch bản cho mỗi luồng thay thế/ngoại lệ, và các tổ hợp luồng thay thế hợp lý; nếu luồng có vòng lặp (nhập lại khi sai), thêm kịch bản lặp. Đặc tả P04 có mục 8a Kịch bản chính thì lấy danh sách đó làm điểm xuất phát, rồi bổ sung các luồng còn thiếu.
3.6. Kết quả mong đợi (oracle): suy ra từ đặc tả; ghi giá trị cụ thể (giá trị trả về, ngoại lệ, trạng thái đối tượng sau, tương tác với phụ thuộc). Với trường hợp lỗi, kiểm tra cả việc trạng thái không bị thay đổi. Khi đặc tả không nói kết quả cho một tổ hợp (ví dụ hai điều kiện cùng sai thì báo lỗi nào), không tự quyết: ghi Q/ASM.

Bước 4. Kỹ thuật hộp trắng (khi có thiết kế method hoặc mã nguồn).
4.1. Dựng đồ thị luồng điều khiển (CFG): node là khối lệnh tuần tự hoặc điểm quyết định; cạnh là luồng điều khiển; nhánh đúng/sai ghi nhãn.
4.2. Tính độ phức tạp cyclomatic V(G) = E - N + 2 (E số cạnh, N số node của một đồ thị liên thông), hoặc số điểm quyết định nhị phân + 1. V(G) là số đường đi cơ sở độc lập và là cận trên số test case cần để phủ mọi nhánh. V(G) lớn hơn 10 là dấu hiệu phương thức quá phức tạp: ghi đề xuất tách phương thức cho P12.
4.3. Kiểm tra độ phủ của bộ test hộp đen: C0 (tỷ lệ lệnh được thực thi) và C1 (tỷ lệ nhánh được đi qua). Thêm test case cho lệnh/nhánh chưa phủ, trong phạm vi đặc tả ngoài. Với điều kiện ghép (A và B, A hoặc B), C1 không bảo đảm mỗi điều kiện con nhận cả đúng và sai; nếu điều kiện ghép hiện thực BR, thêm test case để mỗi điều kiện con nhận cả hai giá trị.
4.4. Vòng lặp: với vòng lặp đơn có số lần tối đa n và số lần điển hình m (m < n), kiểm thử: bỏ qua vòng (0 lần), 1 lần, m lần, n-1, n, n+1 lần (n+1 là trường hợp không hợp lệ nếu đặc tả giới hạn). Vòng lồng: cố định vòng ngoài ở số lần điển hình, kiểm thử vòng trong như vòng đơn; sau đó cố định vòng trong ở số lần điển hình, kiểm thử vòng ngoài như vòng đơn.
4.5. Không bỏ test case hộp đen khi một test case hộp trắng đã phủ cùng nhánh: độ phủ 100% không phát hiện được chức năng bị thiếu hoặc sai điều kiện so sánh tại biên (ví dụ viết > thay vì >=), nên các test case biên vẫn cần.

Bước 5. Test double.
- Xác định phụ thuộc của phương thức (quan hệ association/dependency ở P12, interface IF) cần thay thế để test cô lập: truy cập CSDL, hệ thống ngoài, thời gian hệ thống, sinh số ngẫu nhiên, lớp chưa hiện thực.
- Chọn loại: stub (trả giá trị định sẵn cho phương thức được test gọi xuống), driver (chương trình gọi đơn vị được test khi thành phần gọi thật chưa có), mock (kiểm tra phương thức được test đã gọi phụ thuộc đúng cách, đúng tham số, đúng số lần), fake (hiện thực đơn giản chạy được, ví dụ kho dữ liệu trong bộ nhớ).
- Thời gian hiện tại và giá trị ngẫu nhiên phải được tiêm vào (tham số hoặc đối tượng đồng hồ giả lập) để kết quả lặp lại được.

Bước 6. Lập bảng test case, ma trận phủ; nếu SINH_MA_TEST là "Có", sinh khung mã test.

Bước 7. Tự kiểm tra theo [Target].

[Format]
Đầu ra là file X2-unit-tests.md theo khung Conventions C5 gồm F1 đến F5 theo thứ tự, sau đó là các mục kiểm soát (Câu hỏi mở, Giả định nếu CO_NHAN, Đề xuất sửa artifact trước, Vấn đề còn mở).

Quy ước mã: TC-nnn theo Conventions C3. Mã nội bộ trong file: lớp tương đương EC-nn, giá trị biên BV-nn, quy tắc bảng quyết định DT<k>-Q<n> (bảng thứ k, quy tắc n), node đồ thị luồng điều khiển N<n>, cạnh CE<n>; mã nội bộ đánh số liên tục trong cả file để không trùng.

F1. Bảng chọn operation
Cột: | DC.operation | Tiêu chí (BR / rẽ nhánh / tính toán / sự kiện ST / kiểm tra hợp lệ / điều phối UC / gọi hệ thống ngoài) | Ưu tiên (Cao / Trung bình / Thấp) | Chọn (Có / Không: lý do) |
- Lỗi thường gặp: chọn mọi getter/setter (tốn công, ít giá trị); bỏ phương thức hiện thực BR chỉ vì ngắn.

F2. Phân tích kỹ thuật cho từng operation (mỗi operation một tiểu mục "F2.x DC.operation")
F2.x.1. Cơ sở kiểm thử: | Mục (chữ ký / tiền điều kiện / hậu điều kiện / ngoại lệ / BR / luồng thay thế / điều kiện hợp lệ) | Nội dung | Nguồn |
F2.x.2. Phân vùng tương đương: | EC | Điều kiện | Lớp tương đương | Hợp lệ / Không hợp lệ | Giá trị đại diện | Nguồn |
- Quy tắc: mỗi điều kiện có ít nhất một lớp hợp lệ và một lớp không hợp lệ (trừ khi kiểu dữ liệu làm cho lớp không hợp lệ không thể xảy ra, ghi lý do). Lớp phải rời nhau và phủ hết miền.
- Lỗi thường gặp: chỉ có lớp hợp lệ (bỏ quên giá trị âm, vượt tối đa, null); lớp chồng lấn; chia lớp theo cảm tính không theo BR.
F2.x.3. Giá trị biên: | BV | Biên (của EC nào) | Giá trị kiểm thử | Kỳ vọng thuộc lớp | Kết quả mong đợi |
- Lỗi thường gặp: chỉ lấy giá trị giữa lớp; lấy biên sai phía với phép so sánh của BR (BR "từ 200.000 đồng" thì biên là 199.999 và 200.000).
F2.x.4. Bảng quyết định (khi có từ hai điều kiện ảnh hưởng tổ hợp):
```text
| Điều kiện / Hành động | Q1 | Q2 | Q3 | ... |
| C1: <điều kiện> | Y | Y | N | ... |
| C2: <điều kiện> | Y | N | Y | ... |
| A1: <hành động> | X | - | - | ... |
| A2: <hành động> | - | X | X | ... |
```
Y/N cho điều kiện, X cho hành động được thực hiện, "-" cho không thực hiện (ở hàng hành động) hoặc không quan tâm (ở hàng điều kiện, chỉ sau khi gộp có căn cứ), N/A cho quy tắc không thể xảy ra.
F2.x.5. Chuyển trạng thái (khi phương thức là sự kiện): | Trạng thái đầu | Sự kiện (tham số) | Guard đúng/sai | Kết quả mong đợi | Trạng thái sau | ST nguồn |
F2.x.6. Hộp trắng (khi có thiết kế method hoặc mã nguồn):
- Bảng node: | N | Nội dung (lệnh hoặc điều kiện) | Loại (khối lệnh / quyết định / bắt đầu / kết thúc) |
- Bảng cạnh: | CE | Từ N | Tới N | Nhãn (Đúng / Sai / rỗng) |
- V(G) và cách tính; danh sách đường đi cơ sở (chuỗi node).
- Bảng phủ: | Nhánh (CE) hoặc lệnh (N) | TC phủ |; tỷ lệ C0, C1 đạt được.
- Vòng lặp: | Vòng | n (tối đa) | m (điển hình) | Số lần kiểm thử (0, 1, m, n-1, n, n+1) | TC |
- Sơ đồ CFG (chỉ khi DAY_DU): theo Conventions C7 trong file diagrams/X2-cfg-<DC>-<operation>.drawio (style theo dòng "Đồ thị luồng điều khiển (X2)" của bảng C7.3; cạnh có nhãn Đúng/Sai; ID cell trùng N, CE).
F2.x.7. Test double: | Phụ thuộc (DC / IF) | Loại (stub / driver / mock / fake) | Hành vi giả lập hoặc điều cần xác minh | Lý do |

F3. Bảng test case
Cột lõi: | TC | DC.operation | Kỹ thuật (phân vùng tương đương / giá trị biên / bảng quyết định / chuyển trạng thái / use case / đường đi) | Điều kiện đầu | Dữ liệu vào | Kết quả mong đợi | Nguồn (BR / UC bước) |
Cột thêm: | Phủ (EC, BV, DT-Q, chuyển trạng thái, nhánh CE) | Test double | Ưu tiên |
- Định nghĩa: một test case là một tập điều kiện đầu, dữ liệu vào và kết quả mong đợi để xác định đơn vị được test có đáp ứng đặc tả không.
- Điều kiện đầu: trạng thái đối tượng và dữ liệu cần có trước khi gọi (giá trị thuộc tính, trạng thái ST, dữ liệu mà stub trả về, thời điểm giả lập).
- Dữ liệu vào: giá trị cụ thể của từng tham số.
- Kết quả mong đợi: giá trị trả về cụ thể, hoặc ngoại lệ cụ thể; trạng thái đối tượng sau (thuộc tính, trạng thái ST); tương tác với mock (gọi gì, bao nhiêu lần). Với ca lỗi, ghi rõ trạng thái không đổi.
- Nguồn: BR-nn, UC-nnn bước (ví dụ UC-004 3a), ST-nn chuyển, P12 hậu điều kiện.
- Mức hợp lý: mỗi test case kiểm tra một hành vi; các test case độc lập, không phụ thuộc thứ tự chạy, không dùng chung trạng thái có thể thay đổi; mỗi lớp tương đương, giá trị biên, quy tắc bảng quyết định, chuyển trạng thái, nhánh trong mục tiêu phủ đều có ít nhất một test case; một test case có thể phủ nhiều lớp hợp lệ nhưng chỉ nên chứa một giá trị không hợp lệ (để biết lỗi do đâu).
- Lỗi thường gặp: kết quả mong đợi mơ hồ ("thành công", "hiển thị đúng", "báo lỗi"); lấy kết quả mong đợi bằng cách chạy mã; test case gộp nhiều giá trị không hợp lệ; thiếu kiểm tra trạng thái sau; phụ thuộc thời gian thực hoặc dữ liệu CSDL thật.

Ví dụ đúng (quản lý kho, DC-StockItem.issue(quantity: Integer), BR-08: số lượng xuất là số nguyên từ 1 tới tồn hiện có; điều kiện đầu quantityOnHand = 50):
| EC-01 | quantity | quantity < 1 | Không hợp lệ | -5 | BR-08 |
| EC-02 | quantity | 1 <= quantity <= quantityOnHand | Hợp lệ | 20 | BR-08 |
| EC-03 | quantity | quantity > quantityOnHand | Không hợp lệ | 80 | BR-08 |
| BV-01 | min của EC-02 | 0 | EC-01 | InvalidQuantityException, quantityOnHand vẫn 50 |
| BV-02 | min của EC-02 | 1 | EC-02 | quantityOnHand = 49 |
| BV-03 | max của EC-02 | 50 | EC-02 | quantityOnHand = 0 |
| BV-04 | max của EC-02 | 51 | EC-03 | InsufficientStockException, quantityOnHand vẫn 50 |
Test case:
| TC-001 | DC-StockItem.issue | giá trị biên | quantityOnHand = 50 | quantity = 0 | Ném InvalidQuantityException; quantityOnHand = 50 | BR-08 | BV-01, EC-01 | | Cao |
| TC-002 | DC-StockItem.issue | giá trị biên | quantityOnHand = 50 | quantity = 1 | Không ngoại lệ; quantityOnHand = 49 | BR-08 | BV-02, EC-02 | | Cao |
| TC-003 | DC-StockItem.issue | giá trị biên | quantityOnHand = 50 | quantity = 50 | Không ngoại lệ; quantityOnHand = 0 | BR-08 | BV-03, EC-02 | | Cao |
| TC-004 | DC-StockItem.issue | giá trị biên | quantityOnHand = 50 | quantity = 51 | Ném InsufficientStockException; quantityOnHand = 50 | BR-08, UC-006 4a | BV-04, EC-03 | | Cao |
Ví dụ đúng (thư viện, DC-LoanPolicy.checkEligibility(reader), bảng quyết định với C1 thẻ còn hạn, C2 số sách đang mượn < 5, C3 không có sách quá hạn; A1 cho mượn, A2 từ chối): 8 quy tắc; chỉ Q1 (Y, Y, Y) cho A1; các quy tắc còn lại cho A2. Nếu đặc tả không nói lý do từ chối nào được báo khi nhiều điều kiện cùng sai, ghi Q "Khi thẻ hết hạn và đang có sách quá hạn, thông báo lý do nào?" thay vì tự chọn.
Ví dụ đúng (phòng khám, DC-Appointment.cancel(requestTime), guard [startTime - requestTime >= 24h], startTime = 10:00 ngày 15): chuyển trạng thái Booked --> Cancelled với requestTime = 10:00 ngày 14 (đúng 24 giờ, được huỷ); requestTime = 10:01 ngày 14 (còn 23 giờ 59 phút, từ chối, trạng thái vẫn Booked); gọi cancel khi trạng thái Completed (từ chối theo đặc tả, trạng thái không đổi).
Ví dụ đúng (giao đồ ăn, BR: miễn phí giao khi giá trị đơn từ 200.000 đồng): giá trị biên 199.999 (tính phí) và 200.000 (miễn phí).
Ví dụ sai: | TC-010 | DC-StockItem.issue | | | quantity hợp lệ | Thành công | | Sai: không có điều kiện đầu, dữ liệu không cụ thể, kết quả mơ hồ, không có nguồn.
Ví dụ hộp trắng (khách sạn, DC-RateCalculator.quote(nights, isMember, season) có ba điểm quyết định: if nights > 7, if isMember, if season = HIGH): V(G) = 3 + 1 = 4, cần tối đa 4 đường đi cơ sở; kiểm tra các test case hộp đen đã phủ đủ 6 nhánh chưa, thêm test case cho nhánh còn thiếu.

F4. Ma trận phủ
Cột: | Mục cần phủ (EC / BV / DT-Q / chuyển trạng thái / nhánh CE / BR / luồng thay thế P04) | TC phủ | Đạt (Có / Không: lý do) |
- Mọi BR và luồng thay thế P04 liên quan tới phương thức trong phạm vi phải xuất hiện; mục không phủ bằng unit test (ví dụ cần kiểm thử tích hợp hoặc giao diện) ghi lý do và mức kiểm thử phù hợp.
- Tóm tắt độ phủ C0, C1 đạt được so với MUC_TIEU_PHU cho từng phương thức.

F5. Khung mã test (chỉ khi SINH_MA_TEST là "Có")
- Một lớp test cho mỗi lớp được test, tên theo quy ước framework (ví dụ StockItemTest; test_stock_item.py).
- Mỗi test case một phương thức test, tên nêu hành vi được kiểm tra, dạng <phuongThuc>_<dieuKien>_<ketQua>, ví dụ issue_quantityExceedsOnHand_throwsInsufficientStock; ghi mã TC trong chú thích hoặc tên hiển thị.
- Cấu trúc Arrange - Act - Assert (chuẩn bị điều kiện đầu, gọi phương thức, kiểm tra kết quả); chuẩn bị đối tượng mới trong phương thức khởi tạo test (setUp, @BeforeEach, fixture) để các test độc lập.
- Dùng test tham số hoá (parameterized test) cho nhóm test case chỉ khác dữ liệu (lớp tương đương, giá trị biên).
- Kiểm tra ngoại lệ bằng cơ chế của framework (assertThrows, pytest.raises), không dùng try/catch tự viết.
- Mỗi test chỉ kiểm tra một hành vi; số assert vừa đủ cho hành vi đó; có thông điệp mô tả khi assert thất bại nếu framework hỗ trợ.
- Test double theo F2.x.7 bằng thư viện đã chọn; không truy cập CSDL, mạng, đồng hồ hệ thống thật.
- Thân test có đủ Arrange - Act - Assert theo bảng F3; phần chưa xác định (do Q/ASM) đánh dấu bằng lệnh bỏ qua test của framework kèm mã Q.
Ví dụ khung (JUnit 5):
```java
class StockItemTest {
    private StockItem item;

    @BeforeEach
    void setUp() {
        item = new StockItem(50);
    }

    @Test
    @DisplayName("TC-004 issue: quantity vượt tồn thì ném InsufficientStockException và giữ nguyên tồn")
    void issue_quantityExceedsOnHand_throwsInsufficientStock() {
        assertThrows(InsufficientStockException.class, () -> item.issue(51));
        assertEquals(50, item.getQuantityOnHand());
    }

    @ParameterizedTest(name = "TC-002, TC-003: issue({0}) thì tồn còn {1}")
    @CsvSource({"1, 49", "50, 0"})
    void issue_validQuantity_decreasesOnHand(int quantity, int expectedOnHand) {
        item.issue(quantity);
        assertEquals(expectedOnHand, item.getQuantityOnHand());
    }
}
```

[Target]
Trả lời Đạt/Không đạt cho từng câu, sửa trước khi trả kết quả; mục không đạt còn lại ghi vào "Vấn đề còn mở".
1. Mọi phương thức trong phạm vi có dòng ở F1 với quyết định chọn và lý do.
2. Mọi phương thức được chọn có phân vùng tương đương gồm cả lớp hợp lệ và không hợp lệ, lớp rời nhau và phủ hết miền.
3. Mọi lớp có thứ tự có giá trị biên tại và ngay ngoài biên, đúng phía với phép so sánh của BR.
4. Mọi tổ hợp điều kiện ảnh hưởng kết quả có bảng quyết định; quy tắc N/A và quy tắc gộp có căn cứ.
5. Mọi phương thức là sự kiện của state machine có test cho chuyển hợp lệ, guard đúng/sai và sự kiện ở trạng thái không cho phép.
6. Mọi BR và luồng thay thế P04 liên quan có test case hoặc lý do ở F4.
7. Mọi test case có điều kiện đầu, dữ liệu vào cụ thể, kết quả mong đợi cụ thể (gồm trạng thái sau), nguồn.
8. Kết quả mong đợi lấy từ đặc tả; chỗ đặc tả không nói có Q/ASM, không tự quyết.
9. Mục tiêu độ phủ C0/C1 đạt hoặc có lý do; V(G) được tính khi có thiết kế method; V(G) > 10 có đề xuất tách.
10. Vòng lặp có test 0, 1, m, n-1, n, n+1 khi áp dụng.
11. Phụ thuộc ngoài (CSDL, hệ thống ngoài, thời gian, ngẫu nhiên) được thay bằng test double phù hợp.
12. Test case độc lập, mỗi test case một hành vi, chỉ một giá trị không hợp lệ.
13. Khung mã (nếu có) khớp F3: cùng số test case, cùng dữ liệu, cùng kết quả mong đợi.
14. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho bước thiết kế unit test; có ưu tiên cao hơn quy tắc mặc định của bước (trừ Conventions C1); không có thì thay cả khối bằng "Không có" | Ví dụ: "Chỉ thiết kế hộp đen, chưa có mã nguồn."; "Tên phương thức test viết theo dạng should_<ketQua>_when_<dieuKien>."; "Bỏ qua lớp boundary giao diện, sẽ kiểm thử bằng công cụ UI riêng."}}
````

## 5. Ghi chú cho người dùng

- Nhiều câu hỏi mở về kết quả mong đợi: đặc tả chưa đủ (thường ở tổ hợp nhiều điều kiện sai hoặc giá trị biên). Đây là giá trị của bước này: bổ sung BR ở P06 hoặc luồng thay thế ở P04, sau đó chạy lại.
- Chưa có mã nguồn: chạy với thiết kế method ở P12 (hộp trắng mức thiết kế); khi có mã, chạy lại bước 4 với mã nguồn đính kèm để cập nhật CFG và độ phủ.
- Kết quả quá dài: thu hẹp PHAM_VI_TEST, hoặc ghi trong YEU_CAU_BO_SUNG chỉ làm phương thức ưu tiên Cao.
- Kiểm thử tích hợp và hồi quy không thuộc bước này: bộ unit test sinh ra nên được chạy lại tự động mỗi khi mã thay đổi (kiểm thử hồi quy); kiểm thử tích hợp dùng stub (tích hợp từ trên xuống) hoặc driver (tích hợp từ dưới lên) theo tài liệu kế hoạch kiểm thử riêng.
- Dùng độc lập: đính kèm đặc tả phương thức (chữ ký, mô tả, quy tắc) hoặc mã nguồn; thay mã DC bằng tên lớp, nguồn ghi tên tài liệu.

## 6. Căn cứ

- Myers G., Badgett T., Sandler C., The Art of Software Testing, 3rd ed.: phân vùng tương đương, phân tích giá trị biên, bảng quyết định, độ phủ lệnh, nhánh, điều kiện.
- ISTQB Certified Tester Foundation Level Syllabus: kỹ thuật hộp đen (phân vùng tương đương, giá trị biên, bảng quyết định, chuyển trạng thái), hộp trắng (statement coverage, branch coverage).
- McCabe T. J., A Complexity Measure, IEEE Transactions on Software Engineering, 1976: độ phức tạp cyclomatic, đường đi cơ sở, ngưỡng 10.
- Beizer B., Software Testing Techniques, 2nd ed.: kiểm thử vòng lặp.
- Meszaros G., xUnit Test Patterns: test double (dummy, stub, spy, mock, fake), cấu trúc test bốn pha.
- Beck K., Test-Driven Development: By Example; tài liệu JUnit 5, pytest.
- IEEE 829 / ISO/IEC/IEEE 29119-3: tài liệu đặc tả test case.
