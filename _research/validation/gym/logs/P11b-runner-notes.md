Model của phiên chạy: Sonnet

# Nhật ký người chạy P11b (lần chạy đầu, sau P11a giai đoạn 1)

Phạm vi: PHAM_VI_SUBSYSTEM = "Tất cả" (SS-01 đến SS-07), TAI_LIEU_GIAO_TIEP = Không có, CHINH_SACH_LOI và YEU_CAU_BO_SUNG theo tham số bước. Đầu ra: gym/design/P11b-system-interfaces.md (file chung), gym/design/P11b-system-interfaces/SS-01 đến SS-07 (7 file), gym/design/diagrams/P11b-subsystem-SS-01 đến SS-07.drawio (7 file, 30 trang). Mã Q, ASM lớn nhất sau lần chạy: Q-102, chưa có ASM (Q-99 là mã người dùng cung cấp và khớp kết quả quét mục Câu hỏi mở của thư mục design).

Cách làm: vì prompt không kèm công cụ sinh .drawio từ bảng mô hình, tôi viết một script ngoài thư mục dự án để sinh đồng thời bảng Node, bảng message và file .drawio từ cùng một dữ liệu (nhằm Target 10), rồi kiểm tra bằng chương trình (XML hợp lệ, toạ độ, chồng lấn, cạnh cắt node). Chưa mở được draw.io để xem bằng mắt.

## Phần A. Vướng mắc theo vị trí trong prompt và Conventions

1. SS-07 không có message P07 nhưng P10 giao trách nhiệm
   - Vị trí: mục 3, "Subsystem không có boundary nguồn ở P08 lấy trách nhiệm từ cột Trách nhiệm của P10 F2 và message P07 tới package đó." và A1, "Interface hoặc operation chỉ phục vụ use case chưa có P04, P07: không định nghĩa chữ ký."
   - Gặp gì: SS-07 Authentication (IF-07) có trách nhiệm ở P10 F2 và P10 F1 nói nó phục vụ UC-005, UC-010, UC-018, nhưng P07 và P04 của bốn use case không có message hay bước xác thực nào tới PKG-21; use case sở hữu việc xác thực (UC-004) chưa có P04, P07. Hai câu của prompt cho hai kết luận trái nhau (lấy trách nhiệm từ P10 F2 và định nghĩa, hay không định nghĩa chữ ký).
   - Xử lý: coi UC-004 là use case phục vụ, ghi IF-07 "Chờ P07 UC-004", F3 chỉ một dòng "// ..." mỗi trách nhiệm, các cột khác "Chờ P07", thêm Đề xuất sửa P04 (chạy P04, P07 cho UC-004 rồi chạy lại P11b). Hệ quả: SS-05 chưa có bước xác thực thiết bị trong sơ đồ hộp trắng. Prompt nên nói rõ câu nào thắng khi P10 F2 đã có trách nhiệm nhưng P07 không có message.

2. Tìm Q cùng nội dung ở những artifact không nằm trong bảng "Phần cần dùng"
   - Vị trí: A5, "Trước khi cấp Q mới, tìm câu hỏi cùng nội dung trong mục Câu hỏi mở của artifact đầu vào (P09, P10, P11a nếu đã có); có rồi thì trích mã cũ." so với bảng mục 3 (P09 chỉ F4, F6, F7; P10 không liệt kê Câu hỏi mở; P11a không có trong mục 2).
   - Gặp gì: muốn trích đúng Q-45, Q-77, Q-96, Q-98 phải đọc mục Câu hỏi mở của P11a (không thuộc đầu vào ở mục 2), của P09 (ngoài F4, F6, F7) và của P04, P07 (nằm trong phạm vi đọc nhưng bảng chỉ cho đọc luồng và message). Tôi đã đọc các mục Câu hỏi mở đó và quét mã Q bằng grep theo C3.
   - Xử lý: đọc thêm mục Câu hỏi mở của P04, P07, P06, P08, P09, P10 và chỉ mục Câu hỏi mở của ba file P11a. Prompt nên thêm "mục Câu hỏi mở" vào cột "Phần cần dùng" của mọi artifact và thêm P11a vào bảng mục 2.

3. Operation vòng đời do P10 giao so với quy tắc A3 và Target 1
   - Vị trí: A3, "Không thêm operation không phục vụ use case nào, trừ operation kỹ thuật cần cho chính sách lỗi (ví dụ tra cứu trạng thái giao dịch) và phải ghi lý do." và Target 1, "mọi interface có ít nhất một operation dùng bởi một UC".
   - Gặp gì: P10 F2 đã giao enableReceiving, disableReceiving, registerScanReceiver (IF-05) và registerMarkHandler, start, stop (IF-06). Chúng không phục vụ riêng bước nào của use case và cũng không thuộc chính sách lỗi, nên A3 không cho phép nhưng bỏ đi thì IF-05 không còn operation nào dùng được.
   - Xử lý: giữ theo P10 F2, ghi UC "(kỹ thuật)", Timeout "-", nêu trong Vấn đề còn mở. Prompt nên cho phép thêm loại "operation vòng đời" hoặc nói rõ nên bỏ chúng.

4. P10 đặt trách nhiệm trùng giữa IF-05 và IF-09
   - Vị trí: A3, "Thiết bị đẩy sự kiện vào hệ thống (máy quét, cảm biến): thiết kế thêm interface theo chiều ngược (listener) do phía hệ thống cung cấp, subsystem thiết bị gọi vào; ghi rõ ai cung cấp, ai dùng."
   - Gặp gì: P10 F2 giao cho IF-05 các trách nhiệm receiveScannedCode, sendEntryResult, openDoor và cũng giao receiveScannedCode, sendEntryResult cho IF-09 (listener). Cửa quay là bên chủ động gọi vào qua API và nhận kết quả trong phản hồi (hồ sơ dự án), nên sendEntryResult và openDoor không là operation của phần mềm gọi ra. Prompt không nói cách xử lý khi P10 đã chia sẵn trách nhiệm chồng nhau.
   - Xử lý: IF-09.decideEntry phủ receiveScannedCode, sendEntryResult (kết quả trả về) và openDoor (cửa quay mở khi phản hồi là cho phép); IF-05 chỉ giữ ba operation vòng đời; thêm Đề xuất sửa P10 (chỉ đổi cấu trúc, không chạy lại P08, P09). // scanQrCode không có operation vì là thao tác vật lý ngoài phần mềm (P10 F2).

5. Quy tắc layer của interface chiều ngược không áp dụng được cho Presentation
   - Vị trí: A2, "interface đặt ở layer của subsystem thiết bị, lớp hiện thực ở layer trên."
   - Gặp gì: SS-05 ở PKG-12 (Presentation), layer cao nhất theo P09 F4 nên không có layer "trên". P10 đặt IF-09 ở PKG-16 (Application) cùng package với lớp hiện thực.
   - Xử lý: giữ nguyên P10 (lời gọi đi xuống, realization trong PKG-16, không đi lên), ghi ở Vấn đề còn mở. Prompt nên có quy tắc riêng cho thiết bị ở layer cao nhất.

6. Xung đột giữa tham số kỹ thuật chọn trong lúc ánh xạ F4 và C7.3: gate và toạ độ bội số của 10
   - Vị trí: F4, "Mỗi message đi qua khung sd ... có một gate riêng, ID '<ID khung>-G<STT>', style ellipse;html=1; kích thước 10 x 10, đặt trên cạnh khung." và "message đầu tiên ở y = 120, hai message cách nhau 40; toạ độ bội số của 10"; C7.3, "toạ độ là bội số của 10".
   - Gặp gì: gate 10 x 10 có tâm trên cạnh khung và ở y của message (y là bội số của 10) thì x, y góc trên trái của gate lệch 5, không thể đồng thời là bội số của 10.
   - Xử lý: đặt tâm gate đúng y của message (x = 15, y = y_message - 5); mọi cell khác theo bội số của 10; ghi vào Target 10 là không đạt trọn vẹn ở riêng gate. Prompt nên nói rõ gate được miễn quy tắc bội số của 10 hoặc dùng quy ước khác (gate nằm bên trong cạnh khung).

7. F4 thiếu thông số bố cục cho sơ đồ có fragment; "hai message cách nhau 40" không đủ chỗ cho fragment liền nhau
   - Vị trí: F4, "Bố cục: lifeline đặt ở y = 40, cách nhau 160 theo trục x, rộng 120; message đầu tiên ở y = 120, hai message cách nhau 40; toạ độ bội số của 10; theo C7.3."
   - Gặp gì: prompt không nêu x của lifeline đầu tiên (tôi cần chỗ cho gate bên trái khung), kích thước khung sd, lề của fragment, lề của fragment lồng nhau, vị trí nhãn của toán hạng thứ hai, hình học của message tự gọi. Với khoảng cách message 40, hai fragment liền nhau (lề mỗi bên 20) sẽ chạm viền; fragment con và đường ngăn toán hạng của fragment cha cũng chạm nhau (đường ngăn nằm ở giữa hai message, cách 20).
   - Xử lý: lifeline đầu ở x = 100, khung sd x = 20; lề fragment ngang 20 cộng 10 cho mỗi mức lồng, lề trên 20 cộng 10 mỗi mức, lề dưới 10 cộng 10 mỗi mức (để viền con không chạm đường ngăn của cha); nhãn toán hạng thứ hai là nhãn của cạnh đường ngăn đặt ngay dưới đường; message tự gọi vẽ vòng rộng 40, cao 20. Để hai fragment không chạm nhau tôi phải chèn thêm message tự gọi thật sự có nghĩa giữa chúng (awaitPaymentResult ở SS01-BB1 và SS06-BB1, startRetryTimer ở SS02-WB1), tức là ép dạng sơ đồ vì quy tắc bố cục. Prompt nên chỉ rõ các thông số trên.

8. Sơ đồ hộp trắng và hộp đen cho interface gọi ngược (IF-08, IF-09, IF-10)
   - Vị trí: A4, "Mỗi operation của interface có ít nhất một sơ đồ, trừ khi operation được hiện thực 1-1 bởi một lớp đơn giản (ghi rõ)." và F4, "Trang 'Hộp trắng - <operation>': khung sd với tên operation; message đến từ gate bên trái khung" và "Trang 'Hộp đen ...': lifeline control của use case, lifeline interface".
   - Gặp gì: với interface gọi ngược, subsystem là bên gọi và Handler là bên hiện thực; không có "message đến từ gate bên trái khung" mà là message đi ra, và phần bên trong cần vẽ là phía subsystem (khi kết quả nhận được từ hệ thống ngoài), không phải phần bên trong Handler (thuộc P12). Ở hộp đen, control vừa là bên hiện thực interface vừa là "control của use case".
   - Xử lý: SS01-WB3 (returnPaymentResult), SS05-WB1 (decideEntry), SS06-WB3 (handleMarkDue) bắt đầu từ tác nhân bên ngoài (hoặc từ thiết bị) và có gate ra khung cho lời gọi interface chiều ngược; hộp đen vẽ cả lifeline interface chiều ngược lẫn lifeline control, nối bằng một message mang tên operation P07 của control (handlePaymentResult, handleEntryRequest, handlePaymentTimeout, handleClassCutoff). Prompt nên có hướng dẫn riêng cho interface gọi ngược.

9. TAI_LIEU_GIAO_TIEP "Không có" nhưng hồ sơ dự án ghi cổng thanh toán có tài liệu và chính sách lỗi cần API tra cứu
   - Vị trí: placeholder TAI_LIEU_GIAO_TIEP, "ghi 'Không có' thì thiết kế ở mức interface, không ánh xạ chi tiết lời gọi ngoài"; A4, "... tới tác nhân hệ thống ngoài hoặc thiết bị"; hồ sơ dự án HE_THONG_NGOAI, "có tài liệu API thanh toán và tra cứu giao dịch".
   - Gặp gì: hồ sơ nói tài liệu API thanh toán và tra cứu có tồn tại nhưng không được đính kèm; sơ đồ hộp trắng buộc phải kết thúc ở tác nhân ngoài nên phải đặt tên lời gọi ngoài (createTransaction, queryTransaction, deliver). CHINH_SACH_LOI yêu cầu tra cứu giao dịch nhưng không biết API tra cứu nhận mã nào.
   - Xử lý: dùng tên lời gọi ngoài chung chung, không ánh xạ trường và địa chỉ; mã tham chiếu giao dịch do phần mềm sinh trước khi gửi, ghi là chưa kiểm chứng với tài liệu. Prompt nên nói cách đặt tên lời gọi ngoài khi không có tài liệu.

10. Thử lại gửi hoá đơn so với quy tắc không thử lại operation có tác dụng phụ tài chính
    - Vị trí: A5, "Thử lại: chỉ tự thử lại operation idempotent hoặc được làm idempotent (khoá idempotency do hệ thống sinh, hệ thống ngoài hỗ trợ theo TAI_LIEU_GIAO_TIEP). Operation có tác dụng phụ tài chính không idempotent thì không tự thử lại" và CHINH_SACH_LOI, "... gửi dữ liệu hoá đơn điện tử thử lại tối đa 3 lần, cách nhau 1 phút."
    - Gặp gì: chính sách đã chốt bắt thử lại gửi hoá đơn (có hệ quả pháp lý/tài chính nếu xuất hai hoá đơn), nhưng "hệ thống ngoài hỗ trợ theo TAI_LIEU_GIAO_TIEP" không kiểm chứng được vì tài liệu là "Không có" và hồ sơ ghi hệ thống hoá đơn chưa có tài liệu API.
    - Xử lý: theo CHINH_SACH_LOI (ưu tiên 2 so với quy tắc bước ở C9): khoá chống trùng là mã tham chiếu giao dịch do hệ thống sinh, thêm Q-100 hỏi bên nhận có loại trùng không, ghi rủi ro ở Vấn đề còn mở. Ranh giới "tác dụng phụ tài chính" cũng chưa rõ cho SMS (tốn tiền mỗi tin) và thông báo đẩy; tôi coi trùng SMS, thông báo đẩy là chấp nhận được và ghi lý do. Prompt nên định nghĩa "tác dụng phụ tài chính" và nói thứ tự thắng giữa CHINH_SACH_LOI và A5.

11. Thử lại cách nhau 1 phút không tương thích với operation đồng bộ
    - Vị trí: CHINH_SACH_LOI "cách nhau 1 phút" và F3 cột "Đồng bộ".
    - Gặp gì: chờ 1 phút giữa các lần thử không thể nằm trong lời gọi đồng bộ của use case. P09 F7 đã nêu gửi thông báo qua tiến trình nền nhưng chỉ cho thông báo; gửi hoá đơn không có hướng dẫn.
    - Xử lý: thông báo đẩy và SMS là bất đồng bộ hoàn toàn; hoá đơn là đồng bộ cho lần gửi đầu rồi thử lại ở nền, kết quả Queued. Hàng chờ thử lại giữ trong bộ nhớ vì PKG-24, PKG-25 chưa phụ thuộc PKG-22 (P10); mất khi tiến trình dừng (ghi theo Q-88). Prompt nên nói rõ lựa chọn khi thử lại kéo dài, và có dùng SS-06 làm kho hàng chờ hay không.

12. A5 buộc mọi loại lỗi không có luồng P04 phải có Q, kể cả lỗi hạ tầng
    - Vị trí: A5, "Nếu P04 không có luồng tương ứng, ghi Đề xuất sửa artifact trước (P04) và Q-nn, không tự tạo hành vi nghiệp vụ." và Target 5.
    - Gặp gì: lỗi ghi CSDL của bộ hẹn giờ, thông điệp cửa quay hỏng, lỗi xử lý lượt quét đều không có luồng P04. Tôi gom thành Q-102 (hẹn giờ) và dùng Q-67, Q-72 cho cửa quay; vẫn còn các hàng như nội dung thông báo rỗng, ngoại lệ do lỗi đầu vào của control không có ý nghĩa nghiệp vụ nhưng bị đòi ánh xạ. Prompt không phân biệt lỗi chương trình với lỗi nghiệp vụ.
    - Xử lý: ánh xạ các lỗi đầu vào sang "Dữ liệu ra 1" hoặc luồng 6a gần nhất kèm giải thích; chỉ cấp Q mới khi hậu quả cho use case là quyết định nghiệp vụ.

13. Kiểu trong chữ ký so với CONG_NGHE
    - Vị trí: A3, "Kiểu trong chữ ký dùng kiểu của ngôn ngữ trong CONG_NGHE khi đã chốt; chưa chốt thì dùng kiểu trung lập (String, Integer, Decimal, Boolean, Date, DateTime, Duration, List<T>)." và F3 ví dụ "authorizePayment(order: FoodOrder, card: PaymentCard): PaymentResult".
    - Gặp gì: CONG_NGHE đã chốt TypeScript nhưng TypeScript không có kiểu ngoại lệ trong chữ ký và các lời gọi I/O là Promise; cột "Lỗi / ngoại lệ" và "Đồng bộ" vẫn cần.
    - Xử lý: dùng string, boolean, Date, void của TypeScript cộng kiểu mô hình, không bọc Promise (để P12), cột Đồng bộ ghi ngữ nghĩa chờ kết quả. Ban đầu tôi dùng tên trung lập, sau đó sửa lại cho đúng quy tắc.

14. Tách file khi dài nhưng C5 vẫn đòi mục kiểm soát ở cuối mỗi artifact
    - Vị trí: Format, "Khi đầu ra dự kiến dài hơn khoảng 100 KB ... tách mỗi subsystem một file ... theo khung C5 ... chứa F1-F7 của subsystem đó" và "Câu hỏi mở, Giả định của mọi subsystem ghi ở file chung"; C5, "Mỗi artifact là file Markdown, mở đầu bằng khối thông tin và kết thúc bằng các mục kiểm soát" và "Mục nào không có nội dung thì ghi 'Không có', không xoá mục."
    - Gặp gì: file con vừa phải theo khung C5 vừa không được chứa Câu hỏi mở, Giả định, Đề xuất, Vấn đề còn mở; hàng "Mã Q, ASM cuối đã cấp" của khối thông tin cũng không rõ ghi gì trong file con.
    - Xử lý: file con có đủ bốn mục kiểm soát, ghi con trỏ về file chung (Giả định ghi "Không có (NGHIEM_NGAT)"); khối thông tin file con ghi Q-102. Tổng đầu ra khoảng 180 KB (file con 162 KB) nên tách là đúng ngưỡng.

15. F5: ai hiện thực interface, và kiểu/ngoại lệ thuộc package khác
    - Vị trí: F5 b, "Quy tắc: subsystem hiện thực interface bằng realization (nét đứt, tam giác rỗng) theo dạng canonical" so với F5 a, cột "Hiện thực IF" (cấp cho lớp); F5 a, "Visibility (public cho interface và cho kiểu dữ liệu, ngoại lệ xuất hiện trong chữ ký interface ...)".
    - Gặp gì: realization vẽ từ subsystem (khung) hay từ lớp Facade; kiểu và ngoại lệ của chữ ký nằm ở package của interface (PKG-16, PKG-22, PKG-23, PKG-24, PKG-25) chứ không nằm trong khung subsystem, nhưng F5 a là "phần tử của subsystem". C3 cũng không nói kiểu dữ liệu, ngoại lệ có mã DC hay không (bảng ghi "DC-xxx Lớp thiết kế").
    - Xử lý: vẽ realization từ lớp Facade tới interface; liệt kê kiểu và ngoại lệ ở F5 a kèm "(PKG-nn)" và cấp mã DC; không vẽ kiểu, ngoại lệ trong class diagram; thêm Đề xuất sửa P10 để thêm chúng vào package. Cần chuẩn hoá trong prompt.

16. Bảng message P07 theo cột "Từ hoặc Đến là boundary nguồn"
    - Vị trí: mục 3, "Dòng bảng message có Từ hoặc Đến là boundary nguồn của subsystem; Câu hỏi mở, Giả định".
    - Gặp gì: các bảng message của P07 dùng mã lifeline (SD1b-L5) trong cột Từ, Đến và bố cục cột khác nhau theo UC (UC-005 có cột ID đầu, UC-015 có ID và y ở cuối); phải đối chiếu bảng Node để biết lifeline nào là boundary nguồn. Với SS-06 các message liên quan là tự gọi của control (startWaitingForPayment, cancelAbsenceMark) không có boundary nguồn nên bộ lọc theo cột không tìm ra; tôi tìm theo tên trách nhiệm trong P10 F2.
    - Xử lý: dò bằng tên message. Prompt nên chỉ cách tìm message tới subsystem không có boundary nguồn.

17. F8 và các bảng tổng hợp thiếu đơn vị dòng
    - Vị trí: F8, "Bảng: | SS | IF | Số operation | UC dùng | Rủi ro chính |."
    - Gặp gì: không nói một dòng cho mỗi subsystem hay mỗi interface; SS-01 có hai interface.
    - Xử lý: một dòng mỗi subsystem, cột Số operation ghi theo từng IF; thêm dòng tổng.

18. YEU_CAU_BO_SUNG: đề xuất sửa artifact trước chờ câu trả lời Q, và đề xuất của P11a giai đoạn 1
    - Vị trí: tham số YEU_CAU_BO_SUNG ("đề xuất chờ câu trả lời Q ...; các đề xuất của P10 cho P08, P09 và của P11a giai đoạn 1 cho P04, P08, P10 chỉ đổi cấu trúc thiết kế nên các bước đó không chạy lại").
    - Gặp gì: không rõ đề xuất mới của P11b chờ Q có được ghi vào mục Đề xuất hay không; và vì phạm vi đọc không cho đọc mục Đề xuất của P11a nên tôi không biết P11a giai đoạn 1 đã đề nghị P10 đổi bảng subsystem hay không. Tôi dùng P10 phiên bản 1.0 đúng như đầu vào.
    - Xử lý: vẫn ghi đề xuất mới (P10 x3, P04 x4), đánh dấu "Chưa áp dụng", không lặp lại các đề xuất cũ của P09, P10 đã ghi. Rủi ro: nếu đề xuất P11a đã đổi P10 thì có thể lệch.

19. Actor ở sơ đồ sequence
    - Vị trí: C7.3 bảng style, "Actor: shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;" và F4 bảng Node "Loại (Lifeline / Actor / Gate / Fragment)".
    - Gặp gì: shape umlActor là hình người, không có đường sống; sơ đồ sequence cần tác nhân có đường thời gian.
    - Xử lý: vẽ tác nhân bằng lifeline có nhãn «actor», Loại "Actor" trong bảng. Prompt nên nói cách vẽ tác nhân trong sequence diagram thiết kế.

20. Khối lượng sơ đồ phải sinh
    - Vị trí: toàn prompt, mục 2 và Target 7, 10.
    - Gặp gì: khối lượng bắt buộc gồm 17 sơ đồ sequence và 13 trang phần tử, phụ thuộc, mỗi trang có bảng Node (tới 37 dòng) và bảng message, cộng bảng .drawio nhất quán; không thể viết tay thuần văn bản mà không sai lệch. Tôi phải viết script sinh; một người chạy bằng chat thuần sẽ không đạt Target 10.
    - Xử lý: sinh bằng script từ một nguồn dữ liệu. Đề nghị prompt kèm công cụ sinh hoặc giảm yêu cầu bảng Node cho sơ đồ sequence (toạ độ x, y, w, h cho lifeline và fragment là phần dư vì suy ra được từ quy tắc bố cục).

## Phần B. Kết quả Target

- Target 1: đạt một phần. Mọi subsystem có interface; SS-07 chỉ có IF-07 ở trạng thái "Chờ P07 UC-004" kèm Đề xuất sửa (A1 cho phép). Mọi interface còn lại có operation dùng bởi UC (IF-05 và phần vòng đời của IF-06 ghi "kỹ thuật", xem mục 3).
- Target 2: đạt. // scanQrCode ngoài phần mềm theo P10 F2; // sendEntryResult, // openDoor được phủ bởi kết quả IF-09.decideEntry và phản hồi SS-05 (xem mục 4). Operation kỹ thuật có lý do: queryPaymentStatus; vòng đời IF-05, IF-06.
- Target 3: đạt. Timeout ghi nguồn CHINH_SACH_LOI, NFR-02 hoặc "Thiết kế: ..."; các operation vòng đời ghi Timeout "-" vì không chờ hệ thống ngoài. Kiểu giá trị trong chữ ký ở layer không cao hơn interface (Domain là layer thấp nhất).
- Target 4: đạt. Chữ ký không có chuỗi JSON, mã HTTP, kiểu giao thức; ngoại lệ đặt tên theo vai trò (PaymentGatewayUnavailable, EntryProcessingFailed).
- Target 5: đạt. Mỗi loại lỗi có luồng P04 hoặc Đề xuất sửa P04 kèm Q (Q-77, Q-14, Q-54, Q-65, Q-67, Q-72, Q-102); một số hàng ánh xạ gần đúng (xem mục 12).
- Target 6: đạt có điều kiện. requestPayment không thử lại; gửi hoá đơn chỉ thử lại với khoá chống trùng và Q-100 chưa trả lời (xem mục 10).
- Target 7: đạt. Hộp đen cho mỗi UC dùng subsystem (UC-005: SS-01, SS-02, SS-06; UC-015: SS-03, SS-04, SS-06; UC-018: SS-05; UC-010 không dùng subsystem nào); hộp trắng cho mọi operation có chữ ký, ngoại trừ operation vòng đời ghi rõ ánh xạ 1-1.
- Target 8: đạt. Client chỉ gọi interface; chỉ interface, kiểu dữ liệu và ngoại lệ thuộc chữ ký là public; phụ thuộc subsystem vào package có lý do (F6).
- Target 9: đạt. SS-05 có IF-09 (listener) và nêu bên cung cấp (DC-EnterBranchHandler) và bên dùng (SS-05 thay mặt cửa quay).
- Target 10: đạt một phần. Bảng và .drawio sinh cùng nguồn; XML hợp lệ (minidom parse thành công cho 7 file); riêng toạ độ của gate không là bội số của 10 (xem mục 6); chưa mở bằng draw.io để xem bố cục bằng mắt.
- Target 11: đạt. Không dùng em dash, mũi tên Unicode (grep trả 0); tiếng Việt, thuật ngữ UML tiếng Anh; mã Q, ASM cấp tiếp từ Q-99.

## Phần C. Điểm không có vướng mắc
- Placeholder: đã thay đủ bốn placeholder (PHAM_VI_SUBSYSTEM, TAI_LIEU_GIAO_TIEP, CHINH_SACH_LOI, YEU_CAU_BO_SUNG) theo tham số bước.
- Không đổi tên, mã, phần tử đã chốt ở bước trước (IF-01 đến IF-10, SS-01 đến SS-07, PKG, DC của P10 giữ nguyên); mã DC mới chỉ cho phần tử bên trong subsystem và kiểu dữ liệu, ngoại lệ trong chữ ký.
