# 00 - Mô-đun xử lý đồng thời

Mô-đun này bổ sung quy tắc cho hệ thống có nhiều người hoặc nhiều tiến trình cùng tác động lên một tài nguyên hữu hạn (phòng khách sạn, tồn kho, chỗ đỗ xe, số dư tài khoản). Đính kèm file này cùng prompt của bước khi trường TRANH_CHAP_TAI_NGUYEN của hồ sơ dự án khác "Không". Trường là "Không", để trống hoặc không có thì bỏ qua toàn bộ mô-đun và không sinh mục nào dưới đây.

Mỗi bước chỉ áp dụng mục ghi tên bước đó. Mục M1 đến M3 ở mức nghiệp vụ và phân tích, không nêu khoá, giao dịch CSDL hay công nghệ (Conventions C1 mục 5).

## M0. Khái niệm

| Khái niệm | Nghĩa |
|---|---|
| Tài nguyên tranh chấp | Dữ liệu mà hai tác nhân hoặc hai tiến trình có thể cùng đọc rồi ghi, và sai thứ tự thì vi phạm quy tắc nghiệp vụ |
| Bất biến | Mệnh đề phải luôn đúng, kể cả dưới tải, ví dụ "một phòng trong một đêm thuộc tối đa một lần đặt" |
| Thao tác nguyên tử | Nhóm bước mà người quan sát thấy hoặc xảy ra trọn vẹn, hoặc không xảy ra |
| Cặp loại trừ | Hai thao tác nguyên tử không được xen kẽ trên cùng tài nguyên, có thể là một thao tác với chính nó |
| Kết cục | Điều mỗi bên nhận được theo từng thứ tự đến của cặp loại trừ |
| Mốc kết thúc | Thời điểm một quá trình được coi là đã kết thúc về nghiệp vụ, khác với lúc dọn dẹp xong |
| Trạng thái dở dang | Trạng thái còn phải có việc tiếp theo mới đúng nghiệp vụ, ví dụ đã huỷ đơn nhưng chưa trả hàng về kho |

## M1. P04: khai báo thao tác nguyên tử

Mục 8 của đặc tả thêm bảng "Thao tác nguyên tử" (không có thì ghi "Không có"):

| Thao tác | Bước | Tài nguyên | Bất biến giữ được | Loại trừ với | Kết cục bên thua | Căn cứ |
|---|---|---|---|---|---|---|
| Giữ phòng | 6 | Phòng trong các đêm đã chọn | Mỗi phòng mỗi đêm tối đa một lần giữ | Chính nó; UC-012 bước 4 (khoá phòng bảo trì) | Báo phòng vừa hết, quay lại bước 3 | BR-07, REQ-19 |

Quy tắc:

1. Kiểm tra rồi hành động trên cùng tài nguyên phải nằm trong cùng một thao tác. Điều kiện kiểm ở bước 5 mà việc ghi ở bước 7 thì gộp hai việc vào một thao tác và ghi rõ, hoặc kiểm lại ở bước ghi.
2. Liệt kê đối thủ ở mọi use case đọc hoặc ghi tài nguyên đó, gồm tác nhân thời gian và mọi kênh (trực tuyến, tại quầy). Đặc tả của cả hai phía phải nhắc nhau. Use case đối thủ chưa đặc tả thì ghi "UC-nnn (chưa đặc tả)". Đối thủ đã đặc tả mà chưa nhắc lại thì thêm dòng Đề xuất sửa artifact trước.
3. Nêu kết cục cho cả hai thứ tự đến khi hai thứ tự cho kết quả khác nhau, kể cả trường hợp sự kiện đến sau khi hết hạn và sự kiện đến trùng.
4. Mỗi quá trình có thời hạn ghi mốc kết thúc của nó, và mọi kiểm tra trên quá trình đó dùng đúng mốc này, không dùng lúc dọn dẹp xong.
5. Mọi trạng thái dở dang có lối ra ghi rõ: use case, tác nhân thời gian hoặc xử lý thủ công nêu trong nguồn. Không có lối ra thì ghi Q-nn.
6. Bên nhận trước thành công là hệ quả của bất biến nên không cần Q-nn. Điều bên thua nhận được mà nguồn không nêu thì áp dụng F5.7 của P04.
7. Hành vi không chia cắt ghi ở bảng này, không cấp BR, trừ khi nguồn nêu nó như một chính sách.

## M2. P06: yêu cầu dưới tải

1. NFR về tải của chức năng có tranh chấp nêu thêm tiêu chí "không vi phạm <các BR là bất biến>"; bất biến giữ dưới mọi mức tải nếu nguồn không có ngoại lệ, không ghi Q-nn cho điều này.
2. Các ngưỡng thời gian nối tiếp nhau trên cùng một chuỗi (hết hạn --> giải phóng --> hiển thị) được cộng lại và nêu tổng ở Tiêu chí đo.
3. Mọi BR là bất biến có tranh chấp phải được một dòng của bảng Thao tác nguyên tử ở P04 bảo vệ. Thiếu thì ghi Đề xuất sửa artifact trước.

## M3. P07: một nơi quyết định

1. Mỗi thao tác nguyên tử của P04 có dòng ở F4 nêu lớp điều phối và các lớp tham gia.
2. Phạm vi của bất biến và đối tượng được dùng làm điểm tuần tự phải khớp: bất biến "mỗi khách tối đa một lần giữ" trải qua mọi suất, nên điểm tuần tự theo từng suất là chưa đủ. Chưa khớp thì ghi vào Vấn đề còn mở để P08 xử lý.
3. Một sự kiện từ tác nhân có đúng một lớp nhận đầu tiên, và một điều kiện như "còn hiệu lực" được định nghĩa ở đúng một lớp, ghi trong bảng 2 của sổ trách nhiệm (P07 F3.5).

## M4. P08: mô hình loại trừ toàn hệ thống

Thêm ba bảng vào P08, ngay sau F4:

- F4a. Đơn vị loại trừ: | EX-nn | Thao tác | UC, bước | Đối tượng theo thứ tự lấy | Chế độ (Độc quyền / Chia sẻ) | Bất biến | BR |
- F4b. Cặp loại trừ: | X-nn | EX A | EX B | Đối tượng giao nhau | Kết cục theo thứ tự đến |
- F4c. Sự kiện theo trạng thái: | Lớp | Trạng thái | Sự kiện | Điều kiện thời gian | Kết quả |

Quy tắc:

1. Một thứ tự lấy toàn cục (hạng) cho mọi lớp có khoá, ghi cạnh F4a. Đơn vị nào lấy ngược hạng phải được sửa hoặc ghi lý do.
2. Không nâng chế độ Chia sẻ thành Độc quyền trên cùng đối tượng trong một đơn vị.
3. Xét mọi cặp đơn vị dùng chung đối tượng, gồm cặp của một đơn vị với chính nó và các thao tác sửa dữ liệu cấu hình (sơ đồ phòng, bảng giá).
4. Hai đơn vị chạy nối tiếp: ghi trạng thái khi dừng giữa hai đơn vị và cách đi tiếp, hoặc gộp lại.
5. Mô hình phải kiểm được mọi tiền điều kiện của đơn vị: "chỗ còn thuộc đúng lần giữ này" cần một liên kết hiện tại, không suy ra được từ quan hệ lịch sử.
6. F4c phủ mọi cặp trạng thái và sự kiện có thể xảy ra, gồm trạng thái còn hiệu lực nhưng đã quá hạn mà tiến trình dọn chưa chạy.

## M5. P09: chọn cơ chế và bảng hỏng

F7 thêm mục "Thiết kế đồng thời": cơ chế cho từng EX, nguồn thời gian duy nhất cho mọi điều kiện thời gian, và "Bảng hỏng": | Tình huống | Hệ quả | Cách phát hiện | Cách hồi phục | EX, NFR liên quan |

Bảng hỏng phải xét đủ, mục nào không áp dụng ghi lý do:

1. Tiến trình dừng giữa hai giao dịch của cùng một nghiệp vụ.
2. Tiến trình dừng sau khi gọi hệ thống ngoài và trước khi ghi kết quả.
3. Sự kiện đến trùng, đến muộn, đến sai thứ tự; sự kiện của lần thử cũ đến khi lần thử mới đang chạy.
4. Giao dịch đã ghi nhưng phản hồi mất, tác nhân bấm lại.
5. Nhiều bản cùng quét một hàng đợi. Hạn nhận việc phải lớn hơn thời gian xử lý tối đa của cả lô đã nhận, và bên xử lý kiểm lại quyền nhận việc ngay trước tác dụng ra bên ngoài.
6. Tiến trình dọn dẹp ở tải đỉnh: thông lượng đủ để đạt NFR, tính bằng số liệu.
7. Nguồn thông báo hoặc hàng đợi mất sự kiện: bên nhận phát hiện được và lấy lại được.

Cấm kết luận "không có deadlock" khi chưa đối chiếu các khoá ngầm của nền tảng đã chọn (khoá do khoá ngoại, khoá khi commit). Tham số thời gian phải cộng lại không vượt NFR, kể cả thời gian chờ kết nối.

## M6. P10 và P11b

1. P10: mỗi EX có đúng một lớp mở giao dịch; chuỗi gọi interface giữ đúng hạng; gói việc theo lô nêu thứ tự khoá trong lô.
2. P11b: lời gọi hệ thống ngoài nằm ngoài giao dịch giữ khoá; tổng thời gian chờ của một lượt nhỏ hơn hạn nhận việc; thao tác tự thử lại tuân theo A5 của P11b.

## M7. P12: ranh giới và lối ra

1. F3 của operation có EX ghi ranh giới từng giao dịch; giữa hai giao dịch ghi một dòng "Nếu dừng tại đây: <trạng thái, ai đi tiếp>" khớp Bảng hỏng.
2. F6: mọi trạng thái trung gian có chuyển trạng thái ra do cơ chế hồi phục, không chỉ có đường thành công. Guard không dùng kết quả của lời gọi ngoài chưa diễn ra ở thời điểm xét guard.
3. Thao tác thử lại phải chạy được khi lần trước đã làm một phần: nêu rõ bước nào bỏ qua và bước nào chạy lại.

## M8. P13: lưới an toàn ở dữ liệu

1. Mỗi bất biến trong F4a có ràng buộc ở F4.4 khi CSDL biểu diễn được, hoặc ghi lý do không có.
2. Bảng ánh xạ EX sang mẫu câu lệnh khoá. Khác P08 về đối tượng, chế độ hoặc thứ tự thì ghi căn cứ ngay tại dòng đó.
3. Câu khoá nhiều dòng sắp theo thứ tự hạng; câu quét theo lô nêu thứ tự lấy khoá.

## M9. X1 và X2

1. X1: đối chiếu chéo M4, M5, M7, M8; mỗi lệch giữa các bước là một phát hiện.
2. X2: mỗi X-nn có ca thử cho từng thứ tự đến khác kết cục; mỗi dòng Bảng hỏng có ca thử hồi phục.
