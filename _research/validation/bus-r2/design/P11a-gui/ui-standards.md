# P11a - ui-standards - Hệ thống bán vé xe khách SaoViet Bus

| Thuộc tính | Giá trị |
|---|---|
| Bước | P11a (giai đoạn 1) |
| Phiên bản | 1.1 (giai đoạn 1 phiên bản 1.0; nối MSG-15, MSG-16 từ giai đoạn 2) |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md (NEN_TANG, CONG_NGHE đã chốt); P01-actors.md (Mục 2); P02-usecases.md (Mục 4); P04-uc-specs/UC-009-book-ticket-online.md và UC-017-cancel-trip.md (luồng sự kiện, bảng dữ liệu vào ra, thông điệp, Câu hỏi mở, Giả định); P05-glossary.md (Thuật ngữ, Định nghĩa); P06-supplementary-spec.md (NFR, BR); P07-uc-analysis/UC-009 và UC-017 (message với boundary giao diện người dùng, Câu hỏi mở, Giả định); P08-analysis-model.md (F3, dòng boundary giao diện người dùng); P09-architecture.md (F3, F5); P10-design-elements.md (F3, F4). Placeholder: CHE_DO_CHAY = Giai đoạn 1; THIET_BI_HIEN_THI = website cho hành khách dùng được trên máy tính và điện thoại (responsive, có cảm ứng), phần mềm web cho nhân viên nhà xe trên máy tính bàn tại quầy và văn phòng, ứng dụng Android trên máy soát vé cầm tay; NHAN_DIEN_THUONG_HIEU = Không có (bảng màu trung tính đạt WCAG, ghi là quyết định thiết kế ở UI-STT 16); MAU_DAC_TA_MAN_HINH = Không có; XUAT_HTML = Không; THONG_TIN_TAI_LIEU = Không có; YEU_CAU_BO_SUNG = phạm vi UC-009, UC-017 và màn hình điều hướng cần thiết. Q, ASM lớn nhất quét từ mọi artifact trong thư mục đầu ra trước lần chạy: Q-65, ASM-48; lần chạy này cấp Q-66 đến Q-68 và ASM-49, ASM-50 |
| Phạm vi | Toàn hệ thống (quy định dùng chung); thông điệp lấy từ UC-009, UC-017 |
| Mã Q, ASM cuối đã cấp | Q-72, ASM-54 (giai đoạn 2 cấp Q-70 đến Q-72, ASM-52 đến ASM-54, ghi ở SCR-03 và SCR-06) |

## F1a. Bảng chuẩn hoá

Giá trị ghi "Thiết kế" là quyết định trình bày theo Conventions C1 mục 7, không phải giả định về yêu cầu. Các giá trị tương phản màu đã tính theo công thức độ chói tương đối của WCAG.

| STT | Nhóm | Hạng mục | Quy định | Căn cứ |
|---|---|---|---|---|
| 1 | Display | Website hành khách | Trình duyệt web trên máy tính từ 1280 x 720 px và điện thoại từ 360 x 640 px (hướng dọc, dùng được cả hướng ngang). Nhập bằng chuột, bàn phím và cảm ứng | THIET_BI_HIEN_THI; NEN_TANG; WCAG 1.4.10 |
| 2 | Display | Phần mềm nhân viên nhà xe (ACT-02, ACT-03, ACT-04) | Trình duyệt web trên máy tính bàn từ 1280 x 720 px. Nhập bằng chuột và bàn phím, không yêu cầu cảm ứng, không thiết kế cho điện thoại. Thiết kế: nguồn không nêu cỡ màn hình tại quầy và văn phòng, dùng cùng ngưỡng với website để một bộ quy định phục vụ cả hai | THIET_BI_HIEN_THI; ASM-45 (P09); C1 mục 7 |
| 3 | Display | Ứng dụng Android trên máy soát vé (ACT-05) | Android gốc, hướng dọc, kích thước tính bằng dp và co giãn từ 360 x 640 dp. Nhập bằng đầu quét tích hợp và cảm ứng. Mẫu máy chưa biết nên chưa cố định kích thước máy (ASM-10, Q-38); chưa có màn hình trong phạm vi lần chạy này | THIET_BI_HIEN_THI; NFR-09; Material Design |
| 4 | Display | Chế độ màu | Chỉ có chế độ sáng (nền sáng, chữ tối); chưa có chế độ tối. Thiết kế: nguồn không yêu cầu chế độ tối, một bảng màu giúp kiểm tra tương phản đầy đủ | C1 mục 7; WCAG 1.4.3, 1.4.11 |
| 5 | Display | Điểm ngắt bố cục (web) | Dưới 600 px là bố cục điện thoại: một cột, nội dung rộng 100% trừ lề 16 px mỗi bên. Từ 600 px là bố cục máy tính: một cột nội dung tối đa 1120 px, căn giữa, lề 24 px. Nội dung không cuộn ngang ở độ rộng 320 px | WCAG 1.4.10; Material Design (lớp cửa sổ compact dưới 600 dp) |
| 6 | Screen | Phông chữ và cỡ chữ | Phông Roboto, dự phòng "Segoe UI", Arial, sans-serif (phông hệ thống, không tải tài nguyên ngoài). Chữ nội dung 16 px, dòng cao 24 px; nhãn trường 14 px đậm; chú thích và gợi ý 14 px; tiêu đề màn hình 24 px đậm (20 px khi dưới 600 px). Dùng đơn vị rem để phóng to được. Android dùng Roboto 16 sp | WCAG 1.4.4; Material Design (typography); C1 mục 7 |
| 7 | Screen | Bố cục vùng chuẩn (web) | Từ trên xuống: (1) thanh trên cao 56 px; (2) tiêu đề màn hình; (3) vùng thông điệp (banner); (4) vùng nội dung một cột; (5) vùng hành động ở cuối nội dung, ngăn bằng đường kẻ 1 px #D5DAE0. Vùng hành động không cố định ở mép màn hình (không sticky) để không che điều khiển đang có tiêu điểm | Nielsen #4, #8; Shneiderman (nhất quán); WCAG 2.4.11 |
| 8 | Screen | Vị trí nút (từ 600 px) | Nút phụ nằm bên trái nút chính, cách nhau 16 px, cả hai căn phải trong vùng hành động; thứ tự trái --> phải: nút phụ ("Quay lại", "Huỷ yêu cầu mua vé", "Bỏ yêu cầu huỷ chuyến"), nút chính. Nút "Tìm kiếm" (nếu có) là nút chính, đặt bên phải cuối vùng bộ lọc. Nút "Lưu" (nếu có) là nút chính. Hộp thông điệp và hộp xác nhận cũng căn phải theo thứ tự này | Nielsen #3, #4; Shneiderman (nhất quán); Material Design (một hành động chính) |
| 9 | Screen | Vị trí nút (điện thoại dưới 600 px và Android) | Nút xếp dọc, rộng 100% vùng nội dung, nút chính ở trên, nút phụ ở dưới, cách nhau 12 px. Thiết kế: ngón cái chạm dễ hơn khi nút rộng toàn chiều ngang | Material Design; Apple HIG (vùng chạm); WCAG 2.5.8 |
| 10 | Screen | Nhãn nút | Nhãn bắt đầu bằng động từ, nêu đúng hành động, tối đa 5 từ (ví dụ "Tiếp tục", "Quay lại", "Huỷ yêu cầu mua vé", "Xác nhận huỷ chuyến", "Về trang chủ", "Đóng"). Không dùng "OK", "Có", "Không" đứng một mình. Chỉ chữ cái đầu viết hoa | Nielsen #2, #4; WCAG 2.4.6, 3.2.4 |
| 11 | Screen | Vị trí thông điệp | Ba nơi, mỗi tình huống dùng đúng một nơi: (a) lỗi theo trường ngay dưới trường; (b) banner ngay dưới tiêu đề màn hình, trên vùng nội dung, cho từ chối mà người dùng quay lại sửa và cho kết quả hiển thị ở màn hình đích; (c) hộp thông điệp modal ở giữa màn hình cho use case kết thúc thất bại và cho xác nhận | Baymard; Nielsen #1, #9; WCAG 3.3.1, 4.1.3 |
| 12 | Screen | Tiêu đề màn hình và tiêu đề trang | Mỗi màn hình có đúng một tiêu đề cấp 1, là phần tiếng Việt của tên màn hình ở screen-list.md. Tiêu đề trang của trình duyệt là "<Tên màn hình> - SaoViet Bus". Ngôn ngữ trang khai báo là tiếng Việt (vi) | WCAG 2.4.6, 3.1.1; Nielsen #1 |
| 13 | Screen | Chữ, số, ngày giờ, tiền tệ, đơn vị | Ngày dd/MM/yyyy; giờ HH:mm theo 24 giờ; ngày giờ "dd/MM/yyyy HH:mm". Tiền là số nguyên, phân cách hàng nghìn bằng dấu chấm, sau số có dấu cách và "đ" (250.000 đ), căn phải trong bảng. Tổng tiền chỉ cộng các khoản cùng đơn vị đồng. Tuyến ghi "Điểm đi - Điểm đến" (Hà Nội - Vinh). Số đếm là số nguyên kèm danh từ ("5 vé"). Mã vé và mã chỗ hiển thị đúng như hệ thống cấp (SV0001, A05), không đổi chữ hoa thường | P04 UC-009 Dữ liệu ra 1 dòng 2, 5, 6; P04 UC-017 Dữ liệu ra 1, 3, 4; Nielsen #2, #4 |
| 14 | Screen | Diễn đạt câu và mục chi tiết | Tiếng Việt có dấu, mỗi câu một ý, tối đa 20 từ. Xưng "bạn" với hành khách, không xưng hô với nhân viên nhà xe. Chữ hoa chỉ ở đầu câu và tên riêng. Mục chi tiết chỉ đọc gồm nhãn 14 px đậm ở trên và giá trị 16 px ở dưới. Giao diện chỉ có tiếng Việt vì nguồn và P05 bằng tiếng Việt, P06 không có NFR về ngôn ngữ giao diện (Thiết kế) | C2; Nielsen #2; C1 mục 7 |
| 15 | Screen | Thuật ngữ | Dùng đúng thuật ngữ P05: "chuyến xe" (chấp nhận "chuyến"), "chỗ", "chỗ trống", "giữ chỗ", "thời hạn giữ chỗ", "lần đặt vé", "mã vé", "người đi", "tuyến xe", "giờ xuất bến", "hoàn tiền", "chuyến xe đã huỷ". Không dùng "người truy cập" thay "hành khách" (GL-09) và "giữ tạm" thay "giữ chỗ" (GL-08) | GL-01, GL-02, GL-03, GL-04, GL-08, GL-09, GL-10, GL-12, GL-15, GL-17, GL-21, GL-22; C2 |
| 16 | Screen | Bảng màu | Chủ đạo #1F4E8C; nền trang #FFFFFF; nền vùng phụ #F3F5F7; chữ chính #1F2933; chữ phụ #52606D; viền ô nhập #6B7280; đường kẻ #D5DAE0; lỗi #B3261E trên nền #FDECEA; thành công #1B6E3C trên nền #E7F5EC; cảnh báo chữ #7A4A00 trên nền #FFF4D6; thông tin dùng màu chủ đạo trên nền #E8F0FA. Tương phản đã tính: chữ chính trên trắng 14,76:1; chữ phụ trên trắng 6,46:1 và trên #F3F5F7 5,91:1; trắng trên chủ đạo 8,31:1; lỗi trên trắng 6,54:1 và trên nền lỗi 5,72:1; thành công trên trắng 6,28:1 và trên nền thành công 5,59:1; cảnh báo 6,83:1; chủ đạo trên #E8F0FA 7,23:1; viền ô nhập trên trắng 4,83:1. NHAN_DIEN_THUONG_HIEU là Không có nên bảng màu này là quyết định thiết kế | NHAN_DIEN_THUONG_HIEU = Không có; WCAG 1.4.3, 1.4.11 |
| 17 | Screen | Màu trạng thái | Lỗi, cảnh báo, thành công, thông tin luôn có biểu tượng riêng và tiền tố chữ ("Lỗi:", "Cảnh báo:", "Thành công:", "Thông tin:"). Không dùng màu làm tín hiệu duy nhất cho trạng thái, trường bắt buộc, chỗ đã chọn hay liên kết | WCAG 1.4.1; Nielsen #9 |
| 18 | Control | Nút chính | Nền #1F4E8C, chữ trắng 16 px đậm; cao 44 px với website hành khách (có cảm ứng), 40 px với phần mềm nhân viên (chỉ chuột), 48 dp trên Android; rộng tối thiểu 96 px, đệm ngang 24 px, bo góc 4 px; khi di chuột nền đổi sang #163A6B (trắng trên #163A6B 11,34:1). Tối đa một nút chính mỗi màn hình, đặt bên phải vùng hành động | Material Design (một hành động chính, 48 dp); Apple HIG (44 pt); WCAG 2.5.8; Shneiderman (nhất quán) |
| 19 | Control | Nút phụ | Nền trắng, viền 1 px #1F4E8C, chữ #1F4E8C 16 px đậm; cùng chiều cao và chiều rộng tối thiểu với nút chính; tối đa hai nút phụ mỗi vùng hành động | Material Design (mức nhấn mạnh); Nielsen #4 |
| 20 | Control | Nút nguy hiểm | Nền #B3261E, chữ trắng 16 px đậm (6,54:1); kích thước như nút chính. Chỉ dùng làm nút chính của màn hình xác nhận thao tác không hoàn tác | Nielsen #5; WCAG 1.4.3; Material Design |
| 21 | Control | Trạng thái nút | Nút vô hiệu: nền #D5DAE0, chữ #52606D (4,59:1), khai báo aria-disabled. Chỉ vô hiệu nút chính khi đang xử lý (UI-STT 44) hoặc khi một trường lựa chọn bắt buộc chưa được chọn. Không vô hiệu nút chính vì trường nhập chữ còn thiếu, để người dùng nhận được lỗi cụ thể tại trường | Nielsen #5, #9; Baymard; WCAG 3.3.1 |
| 22 | Control | Ô nhập chữ, số, điện thoại | Mọi form một cột. Nhãn 14 px đậm đặt phía trên ô, luôn hiển thị, gắn với ô bằng thuộc tính for. Ô cao 44 px (website) hoặc 40 px (nhân viên), rộng 100% trên điện thoại và rộng theo số ký tự tối đa nhưng không quá 480 px trên máy tính; viền 1 px #6B7280, bo góc 4 px, chữ 16 px. Placeholder chỉ để ví dụ định dạng (màu #6B7280), không thay nhãn. Sau nhãn ghi "(bắt buộc)" hoặc "(tuỳ chọn)" bằng chữ 14 px thường, không chỉ dùng dấu sao. Ô số điện thoại gợi bàn phím số | Baymard; WCAG 1.3.1, 3.3.2; Nielsen #6 |
| 23 | Control | Nút chọn và danh sách chọn | Từ 2 đến 5 lựa chọn loại trừ nhau dùng nút chọn (radio) hiển thị đủ các lựa chọn, ví dụ lý do huỷ chuyến; từ 6 lựa chọn trở lên dùng danh sách chọn. Không chọn sẵn lựa chọn bắt buộc có hệ quả nghiệp vụ. Cao 44 px (website) hoặc 40 px (nhân viên) | Nielsen #5, #6; WCAG 3.3.2 |
| 24 | Control | Ô chọn (checkbox) | Hộp 24 x 24 px, nhãn bên phải hộp; vùng bấm gồm cả hộp và nhãn, cao tối thiểu 44 px (website) hoặc 40 px (nhân viên) | WCAG 2.5.8, 1.3.1 |
| 25 | Control | Bảng | Dòng tiêu đề nền #F3F5F7 chữ đậm 16 px; dòng dữ liệu cao tối thiểu 44 px (40 px với phần mềm nhân viên), kẻ ngang 1 px #D5DAE0. Cột chữ căn trái; cột số và tiền căn phải. Bảng liệt kê chuyến sắp theo giờ xuất bến tăng dần. Chọn một dòng bằng nút chọn ở cột đầu, không chỉ tô màu dòng. Từ 21 dòng trở lên phân trang 20 dòng mỗi trang. Dưới 600 px mỗi dòng thành một thẻ, nhãn cột đứng trước giá trị | WCAG 1.3.1, 1.4.1, 1.4.10; Nielsen #6, #7 |
| 26 | Control | Sơ đồ chỗ | Bố cục theo sơ đồ chỗ của loại xe (GL-19). Mỗi chỗ là ô 44 x 44 px, cách nhau 8 px, ghi mã chỗ (A05). Ba trạng thái: Trống (nền trắng, viền 2 px chủ đạo); Đã chọn (nền chủ đạo, chữ trắng, kèm biểu tượng dấu tick); Không chọn được (nền #D5DAE0, viền 1 px #6B7280, chữ #52606D, kèm biểu tượng gạch chéo). Chú giải ba trạng thái đặt dưới sơ đồ. Mỗi ô có tên đọc được cho trình đọc màn hình, ví dụ "Chỗ A05, trống" | GL-01, GL-02, GL-19; WCAG 1.4.1, 1.4.11, 2.5.8; Nielsen #1 |
| 27 | Control | Vùng bấm tối thiểu | Mọi điều khiển bấm được có vùng bấm tối thiểu 44 x 44 px với cảm ứng, cao 40 px với chuột, 48 dp trên Android; khoảng cách giữa hai vùng bấm liền kề tối thiểu 8 px; không có vùng bấm nhỏ hơn 24 x 24 px | WCAG 2.5.8; Material Design (48 dp); Apple HIG (44 pt) |
| 28 | Control | Thời điểm kiểm tra dữ liệu nhập | Kiểm tra từng trường khi người dùng rời trường, không báo lỗi khi đang gõ. Khi nhấn nút chính, kiểm tra lại mọi trường rồi mới gửi. Quy tắc nghiệp vụ cần dữ liệu của hệ thống do hệ thống kiểm tra sau khi gửi và trả bằng thông điệp MSG | Baymard; Nielsen #5, #9; WCAG 3.3.1, 3.3.3 |
| 29 | Control | Thứ tự kiểm tra | Với mỗi trường: bắt buộc --> định dạng --> miền giá trị --> quy tắc nghiệp vụ. Dừng ở lỗi đầu tiên của trường và chỉ hiện một lỗi mỗi trường | Chuẩn F1 của P11a; Nielsen #9 |
| 30 | Control | Hiển thị lỗi tại trường | Ngay dưới ô nhập, chữ #B3261E 14 px, có biểu tượng lỗi và tiền tố "Lỗi:"; viền ô đổi sang 2 px #B3261E; gắn với ô bằng aria-describedby. Lỗi mất ngay khi trường hợp lệ | Baymard; WCAG 1.4.1, 3.3.1; Nielsen #9 |
| 31 | Control | Dữ liệu nhập linh hoạt | Số điện thoại chấp nhận khoảng trắng, dấu chấm và dấu gạch ngang giữa các chữ số; hệ thống bỏ các ký tự đó trước khi kiểm tra. Điều kiện hợp lệ của họ tên và số điện thoại người đi theo Q-44 (UC-009), chưa quy định | Baymard; Q-44 |
| 32 | Control | Thứ tự di chuyển tiêu điểm | Thứ tự Tab theo thứ tự đọc: thanh trên, vùng thông điệp, vùng nội dung từ trên xuống và từ trái sang phải, vùng hành động từ trái sang phải. Không dùng tabindex dương. Khi mở màn hình có form, tiêu điểm đặt ở trường nhập đầu tiên; màn hình khác đặt ở tiêu đề màn hình | WCAG 2.4.3, 2.1.1 |
| 33 | Control | Chỉ báo tiêu điểm | Viền ngoài 3 px #1F4E8C cách điều khiển 2 px, luôn nhìn thấy, không tắt outline (#1F4E8C trên trắng 8,31:1). Vùng cuộn có lề cuộn 72 px để thanh trên không che điều khiển đang có tiêu điểm | WCAG 2.4.7, 2.4.11, 1.4.11 |
| 34 | Menu | Cấu trúc menu theo tác nhân | Mỗi tác nhân có một thanh trên (UI-STT 7) với tên hệ thống "SaoViet Bus" bên trái và mục "Trang chủ" bên phải; "Trang chủ" dẫn tới màn hình điều hướng của tác nhân đó. Menu chung không liệt kê use case; lối vào use case nằm ở màn hình điều hướng | Nielsen #6, #8; Shneiderman (nhất quán); P09 F5 |
| 35 | Menu | Vị trí menu | Thanh trên nằm trên cùng mọi màn hình, cùng vị trí và cùng kích thước ở cả điện thoại và máy tính; trên điện thoại chỉ có một mục nên không dùng menu thu gọn | WCAG 3.2.3; Nielsen #4 |
| 36 | Menu | Đánh dấu mục đang chọn | Khi đang ở màn hình điều hướng, mục "Trang chủ" có gạch chân 3 px màu chủ đạo và thuộc tính aria-current; ở màn hình khác không có mục nào được đánh dấu | Nielsen #1; WCAG 1.4.1, 4.1.3 |
| 37 | Menu | Nhất quán thứ tự và hành vi rời màn hình | Thứ tự và tên mục giống nhau ở mọi màn hình của cùng tác nhân. Hành vi khi rời màn hình đang giữ tài nguyên (đang giữ chỗ) bằng menu được ghi ở đặc tả màn hình đó | WCAG 3.2.3; Shneiderman (nhất quán); Nielsen #3 |
| 38 | Bàn phím | Phím tắt | Không định nghĩa phím tắt riêng và không dùng accesskey. Thiết kế: nguồn không yêu cầu, phím tắt dễ trùng với phím của trình duyệt, hệ điều hành và trình đọc màn hình | C1 mục 7; WCAG 2.1.4 |
| 39 | Bàn phím | Phím Enter | Trong form, Enter ở ô nhập một dòng kích hoạt nút chính của form. Enter trên nút đang có tiêu điểm kích hoạt nút đó. Trong màn hình xác nhận thao tác không hoàn tác, tiêu điểm đầu ở nút an toàn nên Enter không kích hoạt thao tác nguy hiểm | Nielsen #5, #7; WCAG 2.1.1 |
| 40 | Bàn phím | Phím Esc | Esc đóng hộp thông điệp và màn hình pop-up, tương đương nhấn nút phụ hoặc nút "Đóng" của hộp đó, không bao giờ kích hoạt nút nguy hiểm. Esc ở màn hình thường không có tác dụng | Nielsen #3; WCAG 2.1.1 |
| 41 | Bàn phím | Phím trong nhóm điều khiển và sơ đồ chỗ | Nút chọn: mũi tên di chuyển giữa các lựa chọn, Space chọn. Sơ đồ chỗ: Tab vào lưới một lần (một điểm dừng), mũi tên di chuyển giữa các chỗ theo bố cục, Space chọn hoặc bỏ chọn chỗ. Ô chọn: Space đổi trạng thái | WCAG 2.1.1, 2.4.3; Nielsen #7 |
| 42 | Bàn phím | Phím vật lý trên máy soát vé | Phím quét vật lý của máy chỉ kích hoạt đầu quét, không gán chức năng khác. Phím Back theo hướng dẫn nền tảng Android, quay lại màn hình trước. Mẫu máy chưa biết (Q-38) nên chưa quy định thêm | Material Design; NFR-09; Q-38 |
| 43 | Messages | Chỉ báo xử lý | Khi một xử lý kéo dài quá 1 giây, hiện chỉ báo xoay 24 px kèm chữ MSG-13 ngay cạnh nút vừa nhấn; quá 10 giây thêm câu "Việc này mất lâu hơn thường lệ" vào cùng dòng. Mốc 1 giây và 10 giây theo ngưỡng thời gian phản hồi của Nielsen; NFR-08 đặt mục tiêu 2 giây ở phân vị 95 cho tra cứu, xem sơ đồ chỗ và giữ chỗ | Nielsen #1; NFR-08; Shneiderman (phản hồi đầy đủ) |
| 44 | Messages | Chống gửi lặp và huỷ khi đang xử lý | Trong lúc xử lý, vô hiệu nút chính vừa nhấn để không gửi hai lần (NFR-04 chỉ một yêu cầu giữ được chỗ, NFR-05 hoàn tiền đúng một lần). Không hiện nút huỷ khi đang xử lý, trừ khi đặc tả có luồng huỷ ở bước đó; đặc tả UC-017 không cho huỷ giữa bước 4 và bước 14 | NFR-04, NFR-05; Nielsen #5; UC-017 luồng *a |
| 45 | Messages | Thông báo trạng thái | Thông báo kết quả (thành công, đã huỷ, đang xử lý) khai báo role status và không chiếm tiêu điểm; thông báo lỗi khai báo role alert. Trình đọc màn hình đọc được mà tiêu điểm vẫn ở điều khiển đang dùng | WCAG 4.1.3; Nielsen #1 |
| 46 | Messages | Thời hạn giữ chỗ | Mọi màn hình hiển thị trong thời hạn giữ chỗ (BR-03) ghi thời hạn giữ chỗ dạng "Chỗ được giữ đến HH:mm" kèm thời gian còn lại mm:ss, cập nhật mỗi giây cho mắt nhìn; trình đọc màn hình chỉ được thông báo ở các mốc còn 5 phút, 1 phút và 30 giây. Thời hạn do nghiệp vụ quy định (BR-03) nên không cho kéo dài; đây là trường hợp ngoại lệ thiết yếu của WCAG 2.2.1 | BR-03; GL-21; Nielsen #1; WCAG 2.2.1, 4.1.3 |
| 47 | Messages | Hộp thông điệp modal | Rộng tối đa 480 px, ở giữa màn hình, nền phía sau phủ #1F2933 độ mờ 60%. Gồm biểu tượng và tiền tố loại, nội dung thông điệp, vùng nút căn phải theo UI-STT 8. Khi mở, tiêu điểm vào nút đầu tiên của hộp (nút an toàn với hộp xác nhận), giữ tiêu điểm trong hộp, khi đóng trả tiêu điểm về điều khiển đã mở hộp | Nielsen #1, #9; WCAG 2.1.1, 2.4.3, 4.1.3 |
| 48 | Messages | Banner | Rộng bằng vùng nội dung, nền theo loại (UI-STT 16), viền trái 4 px màu loại, biểu tượng và tiền tố loại, nút đóng "x" vùng bấm 44 px. Không chặn thao tác; mất khi người dùng đóng hoặc đã thao tác lại và gửi. Mỗi lúc chỉ một banner, banner mới thay banner cũ | Nielsen #1, #9; WCAG 1.4.1, 4.1.3 |
| 49 | Messages | Kết thúc use case | Use case kết thúc thất bại có nội dung cần người dùng đọc: hộp thông điệp modal có một nút đưa về màn hình điều hướng của tác nhân. Use case kết thúc bằng bỏ yêu cầu hoặc huỷ: về màn hình điều hướng kèm banner thành công. Use case kết thúc thành công: màn hình kết quả có nút "Về trang chủ". Từ chối mà đặc tả cho quay lại bước trước: ở lại màn hình hiện tại kèm banner | Shneiderman (hội thoại có điểm kết thúc rõ); Nielsen #1, #3 |
| 50 | Error | Phân loại và xử lý lỗi | Ba loại: lỗi nhập (xử lý tại trường, UI-STT 30); lỗi nghiệp vụ (BR bị vi phạm, hiển thị bằng banner hoặc hộp thông điệp theo UI-STT 11 và 49); lỗi hệ thống hoặc hệ thống ngoài (UI-STT 53). Mỗi lỗi có một MSG trong danh mục F1b | Nielsen #9; WCAG 3.3.1 |
| 51 | Error | Nội dung thông điệp lỗi | Theo mẫu: điều gì sai --> vì sao (khi người dùng cần biết) --> làm gì tiếp. Không đổ lỗi cho người dùng, không dùng mã lỗi kỹ thuật, không viết hoa toàn bộ, câu mở đầu hướng dẫn bằng "Vui lòng" | Nielsen #9; WCAG 3.3.3 |
| 52 | Error | Giữ dữ liệu đã nhập | Khi có lỗi, giữ nguyên mọi dữ liệu và lựa chọn đã nhập (họ tên, số điện thoại, chỗ đã chọn, chuyến và lý do đã chọn); người dùng không phải nhập lại. Màn hình của hệ thống không có trường thông tin thẻ (NFR-01) | Baymard; WCAG 3.3.7; NFR-01 |
| 53 | Error | Lỗi hệ thống hoặc hệ thống ngoài | Hiển thị MSG-14 bằng hộp thông điệp modal chỉ có nút "Đóng", ở lại màn hình hiện tại, không có nút thử lại. Lý do: thao tác tài chính (thanh toán, hoàn tiền) phải gửi đúng một lần (NFR-05); gửi lại thủ công sẽ được các kiểm tra BR-02, BR-09 của hệ thống chặn. Kết quả lỗi của Cổng SMS và Cổng thanh toán hiển thị theo luồng thay thế của đặc tả, không hiển thị thông tin kỹ thuật | NFR-05, NFR-10, NFR-11, NFR-12; Nielsen #9 |
| 54 | Error | Tóm tắt lỗi form | Khi nhấn nút chính mà có từ hai trường lỗi trở lên, hiện banner "Có <n> trường cần sửa" và đưa tiêu điểm tới trường lỗi đầu tiên; có một lỗi thì chỉ đưa tiêu điểm tới trường đó | WCAG 3.3.1, 2.4.3; Baymard |
| 55 | Help | Trợ giúp theo ngữ cảnh | Trường có định dạng hoặc giới hạn có dòng gợi ý 14 px màu chữ phụ ngay dưới nhãn, ví dụ "Ví dụ: 0912345678", "Chọn tối đa 5 chỗ" (BR-01). Nội dung gợi ý chỉ lặp lại quy tắc có trong đặc tả hoặc BR, không đặt quy tắc mới | Nielsen #6, #10; WCAG 3.3.2; BR-01 |
| 56 | Help | Trang trợ giúp | Chưa có trang trợ giúp riêng, liên kết "Trợ giúp" hay tài liệu hướng dẫn vì đặc tả không có chức năng này; không thêm khi chưa có câu trả lời Q-68. Thuật ngữ trong gợi ý và thông điệp theo UI-STT 15 | Q-68; Nielsen #10; WCAG 3.2.6 |
| 57 | Khả năng tiếp cận | Tương phản chữ | Chữ thường tối thiểu 4,5:1 so với nền, chữ lớn (từ 24 px, hoặc từ 18,66 px đậm) tối thiểu 3:1; mọi cặp màu trong UI-STT 16 đã đạt. Chữ trên ảnh nền hoặc nền chuyển sắc không dùng | WCAG 1.4.3 |
| 58 | Khả năng tiếp cận | Tương phản thành phần | Viền ô nhập, viền chỗ trống, biểu tượng trạng thái và chỉ báo tiêu điểm tối thiểu 3:1 so với nền liền kề (viền ô nhập 4,83:1; viền chủ đạo trên trắng 8,31:1) | WCAG 1.4.11 |
| 59 | Khả năng tiếp cận | Nhãn cho mọi trường | Mọi ô nhập, danh sách chọn, nút chọn, ô chọn có nhãn nhìn thấy gắn bằng for hoặc bao bọc; nhóm nút chọn có nhãn nhóm (fieldset, legend). Nút chỉ có biểu tượng có tên đọc được | WCAG 1.3.1, 2.4.6, 3.3.2 |
| 60 | Khả năng tiếp cận | Văn bản thay thế | Hình mang thông tin có văn bản thay thế mô tả nội dung; hình trang trí có alt rỗng. Sơ đồ chỗ có mô tả văn bản của từng ô (UI-STT 26) và chú giải bằng chữ | WCAG 1.1.1 |
| 61 | Khả năng tiếp cận | Hỗ trợ bàn phím | Mọi chức năng dùng được chỉ bằng bàn phím; thứ tự và phím theo UI-STT 32, 39, 40, 41; không có bẫy bàn phím; không chức năng nào chỉ dùng được bằng thao tác kéo thả | WCAG 2.1.1, 2.5.7 |
| 62 | Khả năng tiếp cận | Phóng to chữ và reflow | Phóng to chữ 200% không mất nội dung hoặc chức năng; không đặt chiều cao cố định cho khối chứa chữ; ở độ rộng 320 px nội dung không cuộn ngang (bảng chuyển thành thẻ theo UI-STT 25, sơ đồ chỗ được phép cuộn ngang vì là nội dung hai chiều) | WCAG 1.4.4, 1.4.10 |
| 63 | Khả năng tiếp cận | Cấu trúc ngữ nghĩa | Dùng vùng header, main; một tiêu đề cấp 1 mỗi trang, tiêu đề cấp dưới không nhảy cấp; bảng dùng th có scope; thông báo dùng role theo UI-STT 45; dùng đúng phần tử button, input, select, table | WCAG 1.3.1, 4.1.3 |
| 64 | Khả năng tiếp cận | Chuyển động | Không có nội dung nhấp nháy; chỉ báo xoay và hiệu ứng mở hộp tắt khi người dùng bật giảm chuyển động của hệ điều hành | WCAG 2.3.1; Nielsen #8 |
| 65 | Xác nhận | Thao tác cần xác nhận | Thao tác không hoàn tác, thao tác tài chính, thao tác xoá dữ liệu phải qua màn hình xác nhận riêng trước khi gửi. Trong phạm vi lần chạy: huỷ chuyến (UC-017: huỷ vé, gửi SMS, hoàn tiền không đảo ngược được). Thanh toán vé (UC-010) xác nhận bằng màn hình thanh toán của chính UC-010 | Nielsen #5; Shneiderman (ngăn lỗi); WCAG 3.3.4; UC-017 BR-07, BR-08, BR-11 |
| 66 | Xác nhận | Màn hình xác nhận | Là pop-up modal (mẫu dịch chuyển 2), nêu lại đối tượng (tuyến, giờ xuất bến) và lý do, nêu hệ quả bằng chữ lấy từ BR. Tiêu điểm đầu ở nút an toàn; nút nguy hiểm đứng bên phải theo UI-STT 8; Esc là nút an toàn | Nielsen #5; Shneiderman (ngăn lỗi); WCAG 3.3.4 |
| 67 | Xác nhận | Nhãn nút trong màn hình xác nhận | Nút đặt tên theo hành động và đối tượng: "Xác nhận huỷ chuyến" (nguy hiểm), "Không huỷ" (an toàn). Không dùng "OK", "Có", "Không" | Nielsen #2, #5; WCAG 2.4.6 |
| 68 | Xác nhận | Hoàn tác | Không thêm thao tác hoàn tác cho chức năng mà đặc tả không có: huỷ chuyến đã xác nhận không có chức năng khôi phục. Thay vào đó ngăn lỗi bằng xác nhận (UI-STT 65, 66) và lối thoát trước khi gửi (nút "Quay lại", "Bỏ yêu cầu huỷ chuyến", "Huỷ yêu cầu mua vé") | Nielsen #3, #5; Shneiderman (hoàn tác); C1 mục 1 |
| 69 | Xác nhận | Tóm tắt trước thanh toán | Bước ngay trước khi chuyển sang thanh toán hiển thị tóm tắt lần đặt (tuyến, giờ xuất bến, các chỗ, giá vé từng chỗ, tổng tiền) nếu bảng dữ liệu của bước đó trong P04 có các dữ liệu này. Dữ liệu chưa có thì ghi Q ở đặc tả màn hình, không tự thêm | Baymard; WCAG 3.3.4; Nielsen #6 |

## F1b. Danh mục thông điệp

| MSG | Loại (Lỗi / Cảnh báo / Xác nhận / Thành công / Đang xử lý) | Nội dung hiển thị | Nút và hành động | Nguồn (UC bước, BR) |
|---|---|---|---|---|
| MSG-01 | Lỗi | Chưa chọn được chuyến để mua vé. Vui lòng tìm và chọn một chuyến, rồi mua vé lại. | Banner tại SCR-01; nút đóng "x" | UC-009 bước 2a |
| MSG-02 | Lỗi | Chỗ <mã chỗ> không còn trống vì vừa được người khác đặt. Vui lòng tìm lại chuyến và chọn chỗ khác. | Hộp modal; nút "Tìm lại chuyến" --> đóng hộp, về SCR-01 (quay lại bước 2) | UC-009 bước 4a, BR-02 |
| MSG-03 | Lỗi | Mỗi lần đặt chỉ chọn tối đa 5 chỗ. Vui lòng bỏ bớt chỗ đã chọn. | Banner tại SCR-02, giữ nguyên các chỗ đã chọn; nút đóng "x" | UC-009 bước 4b, BR-01 |
| MSG-04 | Lỗi | Chuyến này đã đến giờ xuất bến nên không bán được vé. Vui lòng chọn chuyến khác. | Hộp modal; nút "Về trang chủ" --> đóng hộp, về SCR-01 | UC-009 bước 4c, BR-05 |
| MSG-05 | Lỗi | Vui lòng nhập họ tên người đi. | Lỗi tại trường "Họ tên người đi", tiêu điểm vào trường | UC-009 bước 7a |
| MSG-06 | Lỗi | Vui lòng nhập số điện thoại người đi. | Lỗi tại trường "Số điện thoại người đi", tiêu điểm vào trường | UC-009 bước 7a |
| MSG-07 | Lỗi | Thanh toán không thành công nên các chỗ đã giữ được trả lại. Vui lòng đặt vé lại nếu bạn vẫn muốn đi chuyến này. | Hộp modal; nút "Về trang chủ" --> đóng hộp, về SCR-01 | UC-009 bước 8a |
| MSG-08 | Lỗi | Đã hết thời hạn giữ chỗ nên các chỗ được trả lại cho người khác. Vui lòng đặt vé lại. | Hộp modal; nút "Về trang chủ" --> đóng hộp, về SCR-01 | UC-009 bước 5a, BR-03 |
| MSG-09 | Thành công | Đã huỷ yêu cầu mua vé. | Banner tại SCR-01; nút đóng "x" | UC-009 bước *a |
| MSG-10 | Lỗi | Chuyến <tuyến, giờ xuất bến> đã bị huỷ trước đó nên không huỷ lại được. Vui lòng chọn chuyến khác. | Banner tại SCR-06, danh sách chuyến được làm mới, giữ nguyên lý do đã chọn; nút đóng "x" | UC-017 bước 4a, BR-09 |
| MSG-11 | Lỗi | Chuyến <tuyến, giờ xuất bến> đã đến giờ xuất bến nên không huỷ được. Vui lòng chọn chuyến khác. | Banner tại SCR-06, danh sách chuyến được làm mới, giữ nguyên lý do đã chọn; nút đóng "x" | UC-017 bước 4b, BR-10 |
| MSG-12 | Thành công | Đã bỏ yêu cầu huỷ chuyến. Chuyến và vé không thay đổi. | Banner tại SCR-05; nút đóng "x" | UC-017 bước *a |
| MSG-13 | Đang xử lý | Đang xử lý yêu cầu. Vui lòng chờ và không đóng trang. | Chỉ báo xoay cạnh nút vừa nhấn; không có nút huỷ (UI-STT 44) | UI-STT 43, 44; UC-009 bước 4 đến 12; UC-017 bước 4 đến 14 |
| MSG-14 | Lỗi | Hệ thống tạm thời chưa xử lý được yêu cầu. Thông tin đã nhập vẫn được giữ lại. Vui lòng thử lại sau ít phút. | Hộp modal; nút "Đóng" --> đóng hộp, ở lại màn hình hiện tại | UI-STT 53 |
| MSG-15 | Lỗi | Có <n> trường cần sửa. Vui lòng kiểm tra các trường được đánh dấu lỗi. | Banner tại SCR-03 khi nhấn nút chính mà có từ hai trường lỗi; tiêu điểm vào trường lỗi đầu tiên; nút đóng "x" | UC-009 bước 7a; UI-STT 54 (SCR-03 mục h) |
| MSG-16 | Cảnh báo | Chỗ của bạn chỉ còn được giữ <5 phút / 1 phút / 30 giây>. Vui lòng hoàn tất thanh toán. | Thông báo role status cho trình đọc màn hình tại ba mốc; không có nút và không chiếm tiêu điểm | BR-03; UC-009 bước 5; UI-STT 46 (SCR-03 mục h) |

Các mục h) của SCR giai đoạn 2 nối thêm dòng vào cuối danh mục này, không sửa dòng cũ. Mã MSG lớn nhất hiện có: MSG-16 (MSG-15, MSG-16 nối từ mục h của SCR-03; các SCR-02, SCR-04, SCR-06, SCR-07, SCR-08 không có thông điệp mới).

## F7. Đánh giá chuẩn (giai đoạn 1)

| SCR | Tiêu chí | Kết quả | Bằng chứng | Cách xử lý |
|---|---|---|---|---|
| Chuẩn hoá | Nielsen 1 Hiển thị trạng thái hệ thống | Đạt | UI-STT 43, 45, 46, 48 | - |
| Chuẩn hoá | Nielsen 2 Khớp giữa hệ thống và thế giới thực | Đạt | UI-STT 13, 14, 15 | - |
| Chuẩn hoá | Nielsen 3 Người dùng kiểm soát và tự do | Đạt | UI-STT 8, 40, 49, 68 | - |
| Chuẩn hoá | Nielsen 4 Nhất quán và theo chuẩn | Đạt | UI-STT 7, 8, 10, 18, 35, 37 | - |
| Chuẩn hoá | Nielsen 5 Ngăn lỗi | Đạt | UI-STT 21, 23, 44, 65, 66 | - |
| Chuẩn hoá | Nielsen 6 Nhận biết thay vì nhớ lại | Đạt | UI-STT 22, 25, 46, 55 | - |
| Chuẩn hoá | Nielsen 7 Linh hoạt và hiệu quả | Đạt | UI-STT 31, 39, 41; không dùng phím tắt riêng (UI-STT 38) nên người dùng thành thạo chỉ có Enter, Tab và mũi tên | Ghi nhận đánh đổi ở UI-STT 38 |
| Chuẩn hoá | Nielsen 8 Thẩm mỹ và tối giản | Đạt | UI-STT 7, 16, 18, 22 (một cột, một nút chính) | - |
| Chuẩn hoá | Nielsen 9 Giúp nhận biết, chẩn đoán, khắc phục lỗi | Đạt | UI-STT 30, 50, 51, 53, 54; F1b | - |
| Chuẩn hoá | Nielsen 10 Trợ giúp và tài liệu | Vi phạm còn mở | Có gợi ý theo ngữ cảnh (UI-STT 55) nhưng chưa có trang trợ giúp hay tài liệu (UI-STT 56) | Q-68; không tự thêm chức năng |
| Chuẩn hoá | Shneiderman: nhất quán | Đạt | UI-STT 7, 8, 10, 18, 34, 37 | - |
| Chuẩn hoá | Shneiderman: khả dụng cho mọi người dùng | Đạt | UI-STT 1, 2, 3, 57 đến 64 | - |
| Chuẩn hoá | Shneiderman: phản hồi đầy đủ | Đạt | UI-STT 43, 45, 48, 49 | - |
| Chuẩn hoá | Shneiderman: hội thoại có điểm kết thúc rõ | Đạt | UI-STT 49 | - |
| Chuẩn hoá | Shneiderman: ngăn lỗi | Đạt | UI-STT 21, 23, 28, 65, 66 | - |
| Chuẩn hoá | Shneiderman: hoàn tác dễ dàng | Đạt | UI-STT 68: thay hoàn tác bằng xác nhận và lối thoát, vì đặc tả không có chức năng hoàn tác | Không thêm chức năng |
| Chuẩn hoá | Shneiderman: người dùng làm chủ | Đạt | UI-STT 8, 40, 49 | - |
| Chuẩn hoá | Shneiderman: giảm tải trí nhớ ngắn hạn | Đạt | UI-STT 22, 25, 46, 69 | - |
| Chuẩn hoá | WCAG 1.1.1 Nội dung không phải chữ | Đạt | UI-STT 60 | - |
| Chuẩn hoá | WCAG 1.3.1 Thông tin và quan hệ | Đạt | UI-STT 22, 24, 25, 59, 63 | - |
| Chuẩn hoá | WCAG 1.4.1 Không dùng màu làm tín hiệu duy nhất | Đạt | UI-STT 17, 26, 30 | - |
| Chuẩn hoá | WCAG 1.4.3 Tương phản chữ tối thiểu | Đạt | UI-STT 16, 57 (mọi cặp màu từ 4,59:1) | - |
| Chuẩn hoá | WCAG 1.4.4 Phóng to chữ 200% | Đạt | UI-STT 6, 62 | - |
| Chuẩn hoá | WCAG 1.4.10 Reflow | Đạt | UI-STT 5, 25, 62 | - |
| Chuẩn hoá | WCAG 1.4.11 Tương phản thành phần | Đạt | UI-STT 16, 33, 58 | - |
| Chuẩn hoá | WCAG 2.1.1 Bàn phím | Đạt | UI-STT 41, 61 | - |
| Chuẩn hoá | WCAG 2.4.3 Thứ tự tiêu điểm | Đạt | UI-STT 32, 47 | - |
| Chuẩn hoá | WCAG 2.4.6 Tiêu đề và nhãn | Đạt | UI-STT 10, 12, 59 | - |
| Chuẩn hoá | WCAG 2.4.7 Tiêu điểm nhìn thấy | Đạt | UI-STT 33 | - |
| Chuẩn hoá | WCAG 2.4.11 Tiêu điểm không bị che | Đạt | UI-STT 7, 33 | - |
| Chuẩn hoá | WCAG 2.5.7 Thay thế thao tác kéo | Không áp dụng | Không có thao tác kéo thả; chọn chỗ bằng bấm (UI-STT 26, 61) | - |
| Chuẩn hoá | WCAG 2.5.8 Vùng bấm tối thiểu 24 x 24 px | Đạt | UI-STT 18, 27 (tối thiểu 40 px chiều cao) | - |
| Chuẩn hoá | WCAG 3.2.3 Điều hướng nhất quán | Đạt | UI-STT 34, 35, 37 | - |
| Chuẩn hoá | WCAG 3.2.4 Định danh nhất quán | Đạt | UI-STT 10, 15 | - |
| Chuẩn hoá | WCAG 3.2.6 Trợ giúp nhất quán | Không áp dụng | Chưa có cơ chế trợ giúp lặp lại ở các trang (UI-STT 56) | Xét lại khi Q-68 có câu trả lời |
| Chuẩn hoá | WCAG 3.3.1 Nhận biết lỗi | Đạt | UI-STT 28, 30, 54 | - |
| Chuẩn hoá | WCAG 3.3.2 Nhãn hoặc hướng dẫn | Đạt | UI-STT 22, 55, 59 | - |
| Chuẩn hoá | WCAG 3.3.3 Gợi ý sửa lỗi | Đạt | UI-STT 28, 51 | - |
| Chuẩn hoá | WCAG 3.3.4 Ngăn lỗi với dữ liệu pháp lý, tài chính | Đạt | UI-STT 65, 66, 69 | - |
| Chuẩn hoá | WCAG 3.3.7 Không bắt nhập lại | Đạt | UI-STT 31, 52 | - |
| Chuẩn hoá | WCAG 3.3.8 Xác thực dễ tiếp cận | Không áp dụng | Phạm vi lần chạy không có màn hình xác thực (UC-003 chưa có màn hình) | Lập quy định khi UC-003 vào phạm vi |
| Chuẩn hoá | WCAG 4.1.3 Thông điệp trạng thái | Đạt | UI-STT 45, 47, 48 | - |
| Chuẩn hoá | WCAG 2.2.1 Điều chỉnh thời gian (thêm vì có thời hạn giữ chỗ BR-03) | Đạt | UI-STT 46: thời hạn do nghiệp vụ quy định, thuộc ngoại lệ thiết yếu, có hiển thị thời gian còn lại | - |
| Chuẩn hoá | Nền tảng: Material Design (vùng chạm 48 dp, một hành động chính) | Đạt | UI-STT 3, 9, 18, 27 (chỉ áp dụng cho ứng dụng Android, chưa có màn hình trong phạm vi) | Đánh giá lại ở màn hình đầu tiên của ACT-05 |
| Chuẩn hoá | Nền tảng: Apple HIG | Không áp dụng | Hệ thống không có ứng dụng iOS | - |
| Chuẩn hoá | Baymard: form một cột | Đạt | UI-STT 22 | - |
| Chuẩn hoá | Baymard: nhãn trên ô nhập, không dùng placeholder thay nhãn | Đạt | UI-STT 22, 59 | - |
| Chuẩn hoá | Baymard: đánh dấu cả trường bắt buộc và tuỳ chọn | Đạt | UI-STT 22 | - |
| Chuẩn hoá | Baymard: kiểm tra khi rời trường, không báo lỗi khi đang gõ | Đạt | UI-STT 28 | - |
| Chuẩn hoá | Baymard: giữ nguyên dữ liệu đã nhập khi báo lỗi | Đạt | UI-STT 52 | - |
| Chuẩn hoá | Baymard: thông điệp lỗi cạnh trường và cụ thể | Đạt | UI-STT 30, 51 | - |
| Chuẩn hoá | Baymard: chấp nhận nhiều định dạng nhập hợp lý | Đạt | UI-STT 31 | - |
| Chuẩn hoá | Baymard: giảm số trường tới mức đặc tả yêu cầu | Đạt | UI-STT 55 (gợi ý không thêm trường), mọi trường nhập lấy từ bảng Dữ liệu vào của P04 (kiểm ở giai đoạn 2) | - |
| Chuẩn hoá | Baymard: tóm tắt đơn và tổng tiền ở bước thanh toán | Đạt | UI-STT 69 | Kiểm ở đặc tả SCR-03 giai đoạn 2 |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-68 | Hệ thống có trang trợ giúp hoặc tài liệu hướng dẫn sử dụng cho hành khách và nhân viên nhà xe (liên kết "Trợ giúp" ở thanh trên) không? (Không có, chỉ gợi ý theo ngữ cảnh tại trường / Có trang hướng dẫn riêng cho từng loại người dùng) | UI-STT 55, 56; F7 Nielsen 10, WCAG 3.2.6 | yeu-cau-xe-khach.md không nêu trợ giúp hay hướng dẫn sử dụng; P06 không có NFR về trợ giúp |

## Giả định

| Mã | Giả định | Lý do | Phần tử phụ thuộc |
|---|---|---|---|
| Không có | - | - | - |

ASM-49 và ASM-50 của lần chạy này ghi ở screen-transition.md.

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P06 | Mục 3 (NFR) | P06 không có NFR về khả dụng, khả năng tiếp cận, ngôn ngữ giao diện và thiết bị hiển thị, nên ui-standards tự đặt mức WCAG 2.2 AA, giao diện tiếng Việt, thiết bị ở UI-STT 1 đến 5, 14, 57 đến 64 như quyết định thiết kế | Nếu cần ràng buộc, bổ sung NFR nhóm Usability (khả năng tiếp cận WCAG 2.2 AA, ngôn ngữ giao diện, thiết bị) khi chạy lại P06 |

## Vấn đề còn mở

- Nielsen 10 ở F7 là Vi phạm còn mở, chờ Q-68; không có vi phạm WCAG AA nào chưa có cách xử lý.
- Hai quy định phục vụ ứng dụng Android (UI-STT 3, 42) và Material Design ở F7 chưa kiểm được trên màn hình thật vì ACT-05 chưa có màn hình trong phạm vi lần chạy.
- UI-STT 25 (phân trang 20 dòng) và UI-STT 46 (đếm ngược mỗi giây) là quyết định trình bày; số dòng mỗi trang là tham số thiết kế, không phải ngưỡng nghiệp vụ.
- Cặp màu tính tương phản bằng công thức WCAG, chưa kiểm bằng công cụ đo ngoài; các cặp gần ngưỡng (nút vô hiệu 4,59:1, viền ô nhập 4,83:1) nên đo lại khi dựng giao diện.
- Danh mục MSG cần được người duyệt đọc lại câu chữ tiếng Việt trước khi giai đoạn 2 trích dẫn.
