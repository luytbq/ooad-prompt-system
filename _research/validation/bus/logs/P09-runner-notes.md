# P09 - Nhật ký người chạy - Hệ thống bán vé xe khách SaoViet Bus

Model: Sonnet (tham số model sonnet của công cụ Agent).

Đầu ra: design/P09-architecture.md, design/diagrams/P09-package-layers.drawio, design/diagrams/P09-deployment.drawio. Tham số: RANG_BUOC_KIEN_TRUC, TIEU_CHI_UU_TIEN, YEU_CAU_BO_SUNG = Không có; PHUONG_AN_DA_CHON = Không có (dùng khuyến nghị CN1, trạng thái chờ xác nhận). Kết quả: 8 yêu cầu kiến trúc (F1), 3 phương án mẫu, 3 phương án công nghệ, 4 layer, 21 package (PKG-01 đến PKG-25), 37 phụ thuộc, 8 node deployment, Q-78 đến Q-83, ASM-57, ASM-58.

## 1. Vướng mắc

### 1.1 Thứ tự layer: Domain trên hay dưới Services (mâu thuẫn giữa ví dụ và quy tắc)

- Vị trí: A4 "layer nghiệp vụ hoặc ứng dụng (application logic, domain), layer dịch vụ kỹ thuật (persistence, tích hợp hệ thống ngoài...)"; F5 ví dụ "entity --> lớp miền ở Domain, phần lưu trữ do Persistence đảm nhận; boundary hệ thống --> subsystem ở Services"; A5 "mũi tên phụ thuộc (kể cả realization) không bao giờ đi từ layer dưới lên layer trên"; F4 ví dụ sai "PKG-06 Persistence phụ thuộc PKG-05 Inventory ... (sai: layer dưới phụ thuộc layer trên)".
- Gặp phải: các ví dụ đặt Domain/Application trên Persistence. Nhưng Persistence muốn ánh xạ lớp entity thì phải tham chiếu kiểu của lớp Domain, tức là phụ thuộc đi lên. A5 lại cấm cả realization đi lên, nên cách quen thuộc (interface kho dữ liệu đặt ở Domain, Persistence hiện thực) cũng bị cấm khi Domain nằm trên Services. Prompt cho cách giải ("interface ... đặt ở package cùng layer với lớp hiện thực hoặc thấp hơn") nhưng interface kho dữ liệu trả về kiểu entity nên kiểu entity cũng phải ở layer thấp hơn hoặc bằng.
- Xử lý: đặt thứ tự Presentation, Application, Services, Domain (Domain ở cuối), interface kho dữ liệu nằm ở Domain, Persistence và DeviceStore hiện thực đi xuống; ghi lý do ở F3 và "Vấn đề còn mở". Đề xuất sửa prompt: nêu rõ ở A4/A5 rằng layer miền có thể nằm dưới layer dịch vụ kỹ thuật (hoặc cho phép Persistence phụ thuộc lên Domain như ngoại lệ), và sửa ví dụ F4/F5 cho khớp.

### 1.2 Layer chứa package nhưng quy tắc phụ thuộc chỉ nói về package

- Vị trí: F4 "Mỗi layer là một PKG; package cấp cao bên trong layer là PKG riêng" và cột "Phụ thuộc vào (PKG)"; F6 "một dòng cho mỗi phụ thuộc trong F4".
- Gặp phải: không rõ dòng layer có điền "Phụ thuộc vào" không, và F9 Edge có vẽ cạnh layer-layer không. Nếu vẽ thì cạnh layer đi qua package.
- Xử lý: dòng layer ghi phụ thuộc tổng hợp từ package con, thêm 4 dòng layer vào bảng kiểm F6 (ghi "tổng hợp"), sơ đồ chỉ vẽ cạnh package-package.

### 1.3 Phạm vi "toàn hệ thống" nhưng P08 chỉ phủ 4/18 use case

- Vị trí: [Context] "Phạm vi: toàn hệ thống"; Target 7 "mọi lớp hoạt động trong P08 có layer đích"; F8 "Mọi lớp hoạt động trong P08 thuộc một nhóm".
- Gặp phải: 14 use case (tài khoản, giá vé, báo cáo, lịch chạy, đặt chỗ qua điện thoại, in vé) không có lớp phân tích. Prompt không nói cách đặt package cho nhóm chưa có lớp.
- Xử lý: dựng package theo nhóm chức năng của P02 (AccountService, AccountModel, PricingReportService), ghi rõ "chưa có lớp P08" ở F4, F8 và "Vấn đề còn mở". Prompt nên có câu hướng dẫn cho trường hợp này.

### 1.4 Q hay ASM hay "Thiết kế" cho quyết định kiến trúc thiếu nguồn; xếp hạng ưu tiên

- Vị trí: A1 "Quyết định kiến trúc cần cho cấu trúc mà nguồn không nêu ... được phép đưa ra ở cả hai chế độ ... ghi ở F3 dòng 'Rủi ro còn mở' kèm Q-nn"; C1.7 "Thiết kế: <lý do>"; F1 cột "Mức ưu tiên"; placeholder TIEU_CHI_UU_TIEN "dùng khi P06 không xếp hạng NFR".
- Gặp phải: (a) Chế độ CO_NHAN, prompt vẫn đòi Q-nn cho quyết định (loại client nhân viên, vị trí máy in), trong khi C1.2 CO_NHAN cho phép ASM; hai quy tắc không khớp. (b) Cột "Mức ưu tiên" cần thứ hạng mà P06 và placeholder đều không có; thứ hạng là con số tự đặt hay quyết định thiết kế? A1 cấm "tự đặt ngưỡng" nhưng không nói về thứ hạng. (c) Công nghệ cụ thể (Java, React...) là "Thiết kế" theo C1.7 hay cần nguồn.
- Xử lý: quyết định cấu trúc --> Q-78 đến Q-83 theo A1 (ưu tiên A1 vì là quy tắc riêng của bước, nhưng C9 xếp C1 cao hơn); thứ hạng ưu tiên --> ASM-57; quy mô nhóm --> ASM-58; chọn công nghệ gắn tiêu chí, không cần Q/ASM theo F2.2. Cần làm rõ trong prompt.

### 1.5 Package triển khai trên nhiều node (máy soát vé và máy chủ)

- Vị trí: A4 "Trong mỗi layer, xác định package cấp cao"; F10 "Bảng Node: node ... và artifact triển khai".
- Gặp phải: kiến trúc layer của prompt ngầm giả định một khối triển khai. Ở đề này máy soát vé chạy lại một phần Application (soát vé), Domain và Services (DeviceStore, ScannerIntegration) khi mất sóng, còn máy chủ chạy cùng phần Domain. Prompt không hướng dẫn một package xuất hiện ở hai node, hay layer "Presentation" có chứa logic ứng dụng ở client hay không.
- Xử lý: layer là logical; ghi ở F4 danh sách package chạy trên máy soát vé; artifact "Mô-đun miền dùng chung" ở D-04. Nên thêm hướng dẫn về client có logic cục bộ (offline).

### 1.6 Quy tắc sơ đồ C7.3 với layer chứa package

- Vị trí: C7.3 "cạnh không cắt qua node"; F9 "package con nằm trong layer; mũi tên phụ thuộc đi từ trên xuống".
- Gặp phải: layer là container, cạnh Application --> Domain phải đi qua layer Services; "cắt qua node" có tính container không? Cạnh nhảy 2 layer buộc đi vòng qua lề hoặc cắt qua container. Ngoài ra "nhãn multiplicity" không áp dụng; không rõ kích thước khoảng cách 40 giữa container và package con.
- Xử lý: coi chỉ package là node; 12 cạnh Application --> Domain đi vòng qua lề phải bằng điểm uốn; kiểm tra bằng script (không cạnh cắt package, không đoạn trùng nhau, toạ độ bội 10, khoảng cách giữa package tối thiểu 40). Chưa mở bằng draw.io (không có công cụ hiển thị); nhãn tab của folder chưa kiểm bằng mắt.

### 1.7 Bảng Node F9 và C7.1

- Vị trí: F9a "ID (PKG) | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú"; C7.1 "Khuyến nghị thêm bốn cột x, y, w, h"; F10 không có bảng Edge cụ thể ngoài "đường truyền thông ... có nhãn giao thức".
- Gặp phải: sinh file .drawio tất định cần x,y,w,h nhưng F9 không liệt kê; F10 không chỉ định style cho artifact, execution environment, communication path.
- Xử lý: thêm x,y,w,h và cột Điểm uốn; artifact dùng hình chữ nhật, communication path dùng đường nét liền không mũi tên; node cube theo F10. Nên thêm style artifact vào C7.3.

### 1.8 Cấu trúc F2.1 và F2.2 khi vừa có hai phương án mẫu vừa chưa chốt công nghệ

- Vị trí: A3 "Nếu NEN_TANG hoặc CONG_NGHE là 'Chưa chốt', hoặc có từ 2 phương án khả thi trở lên: lập bảng so sánh"; A2 "Mẫu cho phía giao diện ... chỉ chọn ở A3b".
- Gặp phải: PA2 (Front-end/Back-end) gần như phụ thuộc công nghệ (SPA hay dựng phía máy chủ); PA1 mô tả "giao diện dựng phía máy chủ" đã ngầm chứa công nghệ giao diện, trong khi A2 cấm chọn mẫu giao diện trước công nghệ. Thang trọng số bảng F2.1 chỉ ghi "Trọng số" mà không nêu thang.
- Xử lý: PA mô tả ở mức cấu trúc nhưng PA1 vẫn nhắc cách dựng giao diện; trọng số dùng Cao/Trung bình theo ASM-57; chấp nhận. Cần ví dụ thang trọng số.

### 1.9 Khối F11 và hồ sơ dự án

- Vị trí: mục 3 "sao chép khối trong mục 'Cập nhật hồ sơ dự án' (F11) ... vào project-profile.md mục 3"; F11 khối bảng "Trường | Giá trị" chỉ có NEN_TANG, CONG_NGHE.
- Gặp phải: dán nguyên khối vào mục 3 sẽ trùng tiêu đề bảng và để lại hai dòng cũ "Chưa chốt"; không rõ thay hay thêm.
- Xử lý: ghi "thay hai dòng NEN_TANG và CONG_NGHE hiện có" ngay trên khối.

### 1.10 Ngữ cảnh lớn

- P08 77 KB, P02 55 KB, P06 29 KB, P05 37 KB, P01 16 KB, P03 21 KB. Mục 3 chỉ nói "các file đầu vào" mà không nói mục nào của P02, P03, P05 cần. Tôi chỉ đọc Mục 4 P02, F3, F4, F6 và phần quan hệ của P08, Mục 2 P01, Mục 3 đến 6 P06, tên thuật ngữ P05; P03 chỉ lướt bảng quan hệ. Nên liệt kê mục cần đọc như đã làm ở P05/P06 (README mục 8).
- Mã Q/ASM: phải grep toàn thư mục design để tìm số lớn nhất (Q-77, ASM-56) vì P09 không có artifact cùng bước để đọc; chấp nhận được nhưng tốn công.

### 1.11 Khác

- F4 "Trách nhiệm: một câu, không chứa 'và' nối hai trách nhiệm khác loại": các package cổng/thiết bị dùng chuỗi liệt kê cùng loại; tự đánh giá đạt nhưng tiêu chí khó kiểm.
- F7 yêu cầu bảng giao tiếp ngoài theo ACT trong P01; ACT-10 (Bộ định thời) không phải hệ thống ngoài hay thiết bị nhưng cần package (Scheduling); đã thêm dòng. Máy chủ đối với máy soát vé cũng thêm một dòng (ServerApiClient). Prompt nên nói rõ ACT loại Thời gian có thuộc F7 không.
- Máy in vé (ACT-08) chưa có lớp phân tích nào trong P08 (UC-005 chưa phân tích), nên F5 ánh xạ chỉ nêu theo ACT.

## 2. Kiểm tra theo Target

1. Đạt: F1 có 8 dòng, mỗi dòng có nguồn NFR, REQ, BR hoặc ACT; không có ngưỡng ngoài P06 (thời gian phản hồi ghi Q-22, Q-52); thứ hạng ưu tiên ghi ASM-57.
2. Đạt: F2.1 và F2.2 có bảng so sánh.
3. Đạt: F3 có NFR, phương án loại, hệ quả tiêu cực.
4. Đạt: mỗi PKG có trách nhiệm một câu và đúng một layer (kiểm tra bằng script).
5. Đạt: script kiểm không có phụ thuộc đi lên, không có vòng giữa package; không áp dụng "nhảy layer" vì layered nới lỏng.
6. Đạt: ACT-06 đến ACT-10 có PKG (PKG-15 đến PKG-19), che sau interface. Máy in chưa rõ cách nối: Q-79, Q-57.
7. Đạt: F5 đủ các loại, F8 phủ 24/24 lớp (8 boundary, 5 control, 11 entity). Dòng "boundary kênh thông báo" chỉ ghi tham chiếu vì P08 xếp SMS vào giao diện hệ thống.
8. Đạt: F2.2 có 3 phương án, khuyến nghị CN1, trạng thái "Khuyến nghị - chờ người dùng xác nhận", mẫu giao diện chọn sau (F3), F11 có khối.
9. Đạt một phần: bảng và file khớp nhau (tạo cùng từ một mô hình dữ liệu), XML hợp lệ (kiểm bằng xml.dom.minidom), toạ độ bội 10, không node chồng nhau, không cạnh cắt package, không đoạn trùng; chưa xem bằng draw.io nên chưa kiểm được nhãn và hình dạng tab.
10. Đạt: C2 (không em dash, không mũi tên Unicode), C5 (đủ mục kiểm soát), C6 (không còn khối PH).
