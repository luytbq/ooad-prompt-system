# P03 - Nhật ký người chạy

Bước: P03 (P03-use-case-diagram.md). Placeholder: KIEU_DUONG_ASSOCIATION = Không có (dùng KHONG_MUI_TEN); CACH_PHAN_RA_SO_DO = Không có (dùng THEO_NHOM); YEU_CAU_BO_SUNG = Không có. Đầu vào: P02-usecases.md 1.1 (đã áp dụng UCR-01 đến UCR-04).

Đầu ra: design/P03-usecase-model.md; design/diagrams/P03-usecase-overview.drawio; design/diagrams/P03-usecase-ticket-sales.drawio. Hai file .drawio qua kiểm tra xml.dom.minidom. Bảng Node, Edge và file .drawio được sinh từ cùng một cấu trúc dữ liệu bằng script tạm, rồi đối chiếu lại tự động (ID, toạ độ, nhãn, nguồn, đích, điểm uốn). Bố cục được kiểm bằng phép cắt đoạn thẳng với hình chữ nhật bao (tâm nguồn --> điểm uốn --> tâm đích). Không có công cụ render draw.io trong môi trường nên chưa xem được ảnh thật.

## Vướng mắc

1. Thiếu hướng dẫn cho UC vừa dùng chung vừa có điều kiện.
   - Vị trí: [Action] Bước 3b "Hành vi của UC-B là bắt buộc trong mọi kịch bản thành công của UC-A"; Bước 4a "UC-X được P02 giữ theo điều kiện Q4b ... hoặc là UC mà nguồn mô tả như một lựa chọn thêm trong khi thực hiện UC-Y".
   - Gặp: P02 1.1 (theo UCR-01) giữ UC-003 Thanh toán vé trực tuyến theo Q4 d và Q4 a, dùng lại ở UC-002 và UC-007. P02R Mục 6 còn ghi sẵn "Quan hệ «include» từ UC-002 và UC-007 tới UC-003". Với UC-007, thanh toán chênh lệch chỉ xảy ra khi vé mua trực tuyến và vé mới đắt hơn (ASM-10), nên Bước 3b không thoả. Bước 4a cũng không thoả theo nghĩa chữ: UC-003 không được giữ theo Q4 b, và chênh lệch là điều kiện chứ không phải "lựa chọn thêm" của khách. Prompt không có nhánh cho trường hợp này: bỏ quan hệ thì làm mất liên hệ UC-007 với cổng thanh toán, trái ASM-10.
   - Xử lý: dùng «extend» (RL-28, điểm mở rộng "Thu chênh lệch giá vé"), coi vế hai của 4a thoả một phần. Ghi Vấn đề còn mở và đề xuất sửa P02 (thêm Q4 b cho nhánh UC-007). Đầu vào (P02R) và quy tắc của P03 không khớp nhau.

2. Mâu thuẫn về association của UC Đăng nhập.
   - Vị trí: Bước 8 "UC Đăng nhập giữ theo U-R01 của P02 luôn vẽ trên sơ đồ tổng quát ..., nối mọi tác nhân phải xác thực"; [Context] "Không đổi tên, mã, tác nhân chính hoặc phụ của use case đã chốt"; Bước 2.1 "tạo một association tới mỗi tác nhân chính và mỗi tác nhân phụ ghi trong P02".
   - Gặp: chế độ CO_NHAN, ASM-09 giả định nhân viên phải đăng nhập, nhưng P02 1.1 chỉ ghi ACT-01 cho UC-010 và viết "P03 cần chờ Q-27 hoặc xác nhận ASM-09 trước khi vẽ association". Theo Bước 8 thì ACT-02 đến ACT-05 "phải xác thực" (theo ASM-09) và cần nối; theo [Context] và 2.1 thì không được.
   - Xử lý: giữ theo P02, chỉ nối ACT-01. Ghi Vấn đề còn mở theo C9, nêu việc cần làm khi Q-27 được trả lời.

3. Quy tắc bố cục không thoả đồng thời được.
   - Vị trí: Phần D L-05 "Use case sắp theo trình tự thời gian ... từ trên xuống dưới"; L-06 "UC được include đặt bên phải UC gốc, cùng hàng hoặc giữa các UC gốc dùng chung nó"; L-07 "UC mở rộng đặt bên dưới UC gốc"; Target 10 "include bên phải, extend bên dưới UC gốc".
   - Gặp: UC-003 vừa được UC-002 include vừa mở rộng UC-007, và UC-002 đứng trước UC-007 theo thời gian. Ba quy tắc buộc y(UC-002) < y(UC-007) < y(UC-003) nhưng L-06 lại muốn UC-003 cùng hàng với UC-002 hoặc nằm giữa UC-002 và UC-007.
   - Xử lý: chọn L-05 và L-06, đặt UC-003 giữa UC-002 và UC-007. Target 10 không đạt với RL-28. Ghi Vấn đề còn mở.

4. Số 55 trái với quy tắc bội số của 10.
   - Vị trí: L-12 "cột hai cách cột một 80 và lệch xuống nửa bước dòng (55)"; "Đường từ tác nhân tới UC cột hai có một điểm uốn tại (cạnh trái boundary + 40, tâm dọc của UC đích)"; L-10 và Conventions C7.1, C7.3 "mọi toạ độ là bội số của 10".
   - Gặp: với h = 70 (L-04), tâm dọc UC luôn có đuôi 5, nên cả độ lệch 55 lẫn điểm uốn "tại tâm dọc" đều không thể là bội số của 10.
   - Xử lý: lệch 60; điểm uốn đặt ở y = đỉnh hàng cột một + 90 (giữa khe), lệch 5 so với tâm UC đích. Ghi Vấn đề còn mở.

5. L-12 không nói cách đặt nhiều UC dùng chung giữa hai dải kề nhau.
   - Vị trí: L-12 "Riêng UC chỉ nối tác nhân của hai dải kề nhau có thể đặt ở cột một, giữa hai dải đó; khi đó hành lang giữa hai dải nới thành 150 (UC cao 70, mỗi phía cách 40)".
   - Gặp: UC-007 và UC-008 cùng nối ACT-01, ACT-02; hành lang 150 chỉ chứa một UC, UC-007 còn cao 90 vì có ngăn extension points.
   - Xử lý: đặt cả hai ở cột giữa, đường đi theo hành lang với làn y cách nhau 10. Một chỗ cắt giữa các đường là không tránh được (hai tác nhân cùng nối hai UC).

6. L-12 không nói chỗ đặt UC không nối tác nhân chính nào.
   - Vị trí: L-12 "Dải của một tác nhân chứa các UC mà chỉ tác nhân đó là tác nhân chính"; "bên trái các UC chủ yếu nối tác nhân phụ".
   - Gặp: UC-003 có tác nhân chính "ACT-01 (qua UC-002, UC-007)" nên không nối ACT-01 (Bước 2.2), chỉ nối ACT-06. Prompt chỉ nhắc gián tiếp tới "UC chủ yếu nối tác nhân phụ", không có cột hay quy tắc riêng.
   - Xử lý: đặt UC-003 ở một cột riêng bên phải cột giữa, gần ACT-06.

7. Quy tắc ghi chú cho UC được include, UC mở rộng trên sơ đồ tổng quát còn mơ hồ.
   - Vị trí: Bước 8 phương án hai "UC được include hoặc UC mở rộng không có association ghi '(quan hệ ở sơ đồ <tên>)' ở cột Ghi chú của bảng Node".
   - Gặp: không rõ "không có association" là điều kiện lọc (chỉ ghi cho UC cô lập) hay là mô tả. UC-003 có association với ACT-06. UC gốc (UC-002, UC-007) cũng có quan hệ bị ẩn, nhưng quy tắc không nhắc tới.
   - Xử lý: ghi cho UC-003 và UC-007, không ghi cho UC-002. Đã ghi lý do trong Vấn đề còn mở.

8. Bảng Node tách Stereotype khỏi Nhãn, nhưng file .drawio gộp chung.
   - Vị trí: Phần B Mục 5 "Stereotype: «system», «device» cho tác nhân không phải người nếu dùng"; Phần A "Tác nhân hệ thống ngoài có thể ghi thêm «system» trên tên"; Target 12 "cùng ID, cùng nhãn".
   - Gặp: value của mxCell phải là "«system»<br>Cổng SMS", còn cột Nhãn là "Cổng SMS". Với UC-007, bảng dùng <br> (C8 chỉ nói tới <br>) còn .drawio dùng <hr> theo Phần E. Không rõ "cùng nhãn" có tính phần stereotype và ký hiệu ngăn hay không.
   - Xử lý: hiểu "cùng nhãn" là value bằng stereotype cộng nhãn; khi đối chiếu tự động, bỏ qua khác biệt <hr>/<br>.

9. Không có stereotype cho tác nhân thời gian.
   - Vị trí: Phần A, Phần B Mục 5 chỉ nêu «system», «device».
   - Gặp: ACT-10 Bộ định thời là tác nhân thời gian.
   - Xử lý: để "-". Ghi Vấn đề còn mở.

10. Cột Loại quan hệ của đường nối note không có giá trị trong danh sách.
    - Vị trí: Phần B Mục 1 "Loại: Association / Include / Extend / Generalization"; Mục 5 "đường nối note là RL-nn-N".
    - Gặp: bảng Edge cần giá trị cho RL-28-N.
    - Xử lý: ghi "Note".

11. Cột REQ của association không có hướng dẫn.
    - Vị trí: Phần B Mục 1, các cột; Target 14 chỉ đòi REQ cho include, extend, generalization.
    - Gặp: không rõ association ghi mọi REQ của UC hay chỉ REQ của cặp tác nhân - UC.
    - Xử lý: ghi các REQ nêu riêng cặp tác nhân - UC đó, ví dụ cổng SMS ghi REQ-19, REQ-20.

12. Thứ tự RL của nhiều association trên cùng một UC không được nêu.
    - Vị trí: Phần B Mục 1 "association (theo thứ tự UC)".
    - Xử lý: tác nhân chính trước, tác nhân phụ sau, cùng loại thì theo mã ACT.

13. P02R không có trong thứ tự đọc của khối prompt.
    - Vị trí: Mục 2 liệt kê P02R-review.md (Tuỳ chọn) "Đối chiếu các UCR đã được P02 áp dụng"; Mục 3 "Đính kèm" và [Context] "Đọc theo thứ tự" không có P02R.
    - Gặp: AI chỉ nhận khối prompt sẽ không biết phải đối chiếu P02R, cũng không biết ghi kết quả đối chiếu vào đâu khi UCR đã được áp dụng. Khối prompt chỉ hướng dẫn trường hợp "không áp dụng UCR nào".
    - Xử lý: đã đọc P02R, ghi kết quả đối chiếu vào dòng Đầu vào đã dùng và vào Vấn đề còn mở.

14. Nhãn theo NGON_NGU_TEN_PHAN_TU còn mơ hồ.
    - Vị trí: Phần B Mục 5 "Nhãn: tên tiếng Việt (hoặc theo NGON_NGU_TEN_PHAN_TU của hồ sơ dự án)".
    - Gặp: hồ sơ ghi "Tiếng Anh, PascalCase cho lớp, camelCase cho thuộc tính ..., snake_case cho bảng và cột", không nói tới tác nhân và use case.
    - Xử lý: dùng tên tiếng Việt.

15. Không rõ ngưỡng M > 8 có áp dụng khi N nhỏ không.
    - Vị trí: Bước 8 "N từ 21 đến 40, hoặc M trên 8".
    - Gặp: N = 18, M = 10, trong đó 4 tác nhân phụ chỉ nối 1-3 UC. Phương án hai làm sơ đồ Tổng quát mất include và extend, chỉ vì số tác nhân, và sơ đồ Nhóm Bán vé lặp lại 8 trong 18 UC. Câu chữ rõ nên vẫn áp dụng, nhưng có thể không đúng ý đồ của prompt.
    - Xử lý: theo phương án hai.

16. Mục 7 không có hướng dẫn trình bày.
    - Vị trí: Phần B "Mục 7. Các mục kiểm soát theo Conventions C5".
    - Gặp: không rõ có tạo tiêu đề "## 7." hay không; C5 dùng tiêu đề không đánh số.
    - Xử lý: dùng đúng bốn tiêu đề của C5, không có tiêu đề "7.".

17. Không có công cụ để kiểm bố cục bằng mắt.
    - Vị trí: L-12 gạch cuối "kiểm từng đường: mỗi đoạn thẳng ... không được đi qua hình chữ nhật bao của bất kỳ elip nào".
    - Gặp: sơ đồ Tổng quát có 26 cạnh, 14 cạnh có điểm uốn; kiểm bằng tay rất dễ sót. Prompt không nói cách kiểm.
    - Xử lý: viết script kiểm hình học. Chưa kiểm được nhãn tác nhân (chữ dưới hình người que) có bị đường đè lên hay không.

## Target không đạt

- Target 6: RL-28 chỉ thoả Bước 4a một phần (xem vướng mắc 1).
- Target 10: trên sơ đồ Nhóm Bán vé, UC-003 (UC mở rộng) nằm trên UC-007 (UC gốc) (xem vướng mắc 3).
- Các Target khác đạt. Target 8 đạt với ghi chú: có đường cắt đường (không cắt node) ở sơ đồ Tổng quát; dấu hiệu D-AP15 nhẹ, đã ghi ở Vấn đề còn mở.
