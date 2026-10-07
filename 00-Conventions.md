# 00 - Quy ước chung của bộ prompt

File này là luật chung cho mọi bước trong pipeline. Luôn đính kèm file này cùng với prompt của bước đang chạy. Các prompt chỉ ghi phần riêng của bước, phần chung nằm ở đây và không được chép lại.

Người đọc file này gồm hai đối tượng: người dùng (để hiểu cách tổ chức) và AI thực thi prompt (để tuân thủ). Mọi câu trong mục C1 đến C9 là quy tắc bắt buộc với AI.

---

## C1. Nguyên tắc làm việc

1. Nguồn sự thật là tài liệu đầu vào: tài liệu nguồn của dự án (ghi trong hồ sơ dự án), trường HE_THONG_NGOAI của hồ sơ dự án (xếp sau mọi tài liệu nguồn), và các artifact đã chốt của các bước trước. Không dùng hiểu biết chung về một loại hệ thống để thêm chức năng, tác nhân, quy tắc mà nguồn không nêu.
2. Chế độ giả định đọc từ hồ sơ dự án, trường CHE_DO_GIA_DINH:
   - NGHIEM_NGAT: không giả định. Chỗ nào nguồn thiếu hoặc mơ hồ thì ghi vào mục "Câu hỏi mở" (mã Q-nn), không tự điền nội dung.
   - CO_NHAN: được phép giả định khi nguồn thiếu, nhưng mỗi giả định phải có mã ASM-nn, ghi rõ nội dung, lý do, và được liệt kê trong mục "Giả định". Nội dung dựa trên giả định phải trích mã ASM tương ứng.
3. Nhất quán với artifact trước: không đổi tên, không đổi mã, không bỏ phần tử đã chốt ở bước trước. Nếu phát hiện bước trước sai, không tự sửa trong artifact của bước này; ghi vào mục "Đề xuất sửa artifact trước" (bước, mã phần tử, lý do, nội dung đề nghị).
4. Truy vết hai chiều: mọi phần tử tạo ra đều trỏ tới nguồn của nó (mã REQ, UC, BR, NFR... hoặc câu trích tài liệu nguồn). Không có phần tử "mồ côi".
5. Mức trừu tượng đúng bước: phân tích không chứa chi tiết công nghệ (framework, tên bảng, kiểu dữ liệu vật lý, tên màn hình cụ thể); chi tiết đó chỉ xuất hiện từ bước thiết kế trở đi.
6. Tự kiểm tra trước khi trả lời: chạy checklist của bước; mục nào chưa đạt mà không sửa được thì ghi vào mục "Vấn đề còn mở" của artifact, không im lặng bỏ qua.
7. Quyết định thiết kế kỹ thuật: từ P09 trở đi, tham số kỹ thuật không bắt nguồn từ yêu cầu (độ dài cột, timeout kết nối, số lần thử lại, khoảng cách giữa hai lần thử, kích thước pool, kích thước lô, kiểu định danh) là quyết định thiết kế, không phải giả định. AI được chọn giá trị ở cả hai chế độ NGHIEM_NGAT và CO_NHAN, ghi lý do tại chỗ dùng dạng "Thiết kế: <lý do>" (chuẩn, RFC, mặc định của nền tảng, suy từ NFR), không cần Q-nn hay ASM-nn. Chỉ giá trị mang nghĩa nghiệp vụ (hạn mức, thời hạn, giá, phí, ngưỡng mà người dùng cảm nhận được hoặc được nêu trong hợp đồng, quy định) mới theo mục 2: nguồn không nêu thì ghi Q-nn (NGHIEM_NGAT) hoặc ASM-nn (CO_NHAN). Ví dụ: VARCHAR(254) cho email (Thiết kế: độ dài tối đa của địa chỉ theo RFC 5321) là quyết định thiết kế; thời hạn khách phải lấy tiền ở máy ATM là giá trị nghiệp vụ.

## C2. Ngôn ngữ và văn phong

- Ngôn ngữ đầu ra theo trường NGON_NGU_DAU_RA của hồ sơ dự án. Mặc định: tiếng Việt, giữ thuật ngữ UML và thuật ngữ kỹ thuật bằng tiếng Anh khi chưa có từ tiếng Việt thông dụng (use case, actor, include, extend, boundary, control, entity, lifeline, package, subsystem...).
- Tên phần tử mô hình (tác nhân, use case, lớp, thuộc tính, phương thức, bảng) theo trường NGON_NGU_TEN_PHAN_TU. Mặc định: tên lớp, thuộc tính, phương thức, bảng, cột bằng tiếng Anh; tên use case và tác nhân có cả tiếng Việt và tiếng Anh ở hai cột riêng.
- Mỗi câu một ý. Dùng thuật ngữ trong glossary (khi đã có) một cách nhất quán, không dùng từ đồng nghĩa thay thế.
- Không dùng dấu gạch ngang dài (em dash). Dùng dấu gạch nối (-) thay thế.
- Không dùng ký hiệu mũi tên Unicode. Khi cần mũi tên trong văn bản, viết "-->".

## C3. Hệ thống mã định danh

Mã là khoá để các bước sau trỏ tới. Mã đã cấp thì không đổi, không tái sử dụng cho phần tử khác. Phần tử bị loại vẫn giữ mã và ghi trạng thái "Loại".

Phần số trong mã ("nn", "nnn") là số thứ tự có tối thiểu số chữ số như ký hiệu, thêm số 0 ở đầu khi cần (REQ-07, UC-004), và mở rộng thêm chữ số khi vượt giá trị lớn nhất (REQ-99 rồi REQ-100). Các mã đã cấp không đổi độ dài khi dãy mở rộng.

| Mã | Phần tử | Bước tạo | Ví dụ |
|---|---|---|---|
| REQ-nn | Yêu cầu đã chuẩn hoá từ tài liệu nguồn | P00 | REQ-07 |
| SH-nn | Bên liên quan (stakeholder) | P00 | SH-02 |
| Q-nn | Câu hỏi mở | Mọi bước | Q-03 |
| ASM-nn | Giả định (chỉ ở chế độ CO_NHAN) | Mọi bước | ASM-02 |
| ACT-nn | Tác nhân | P01 | ACT-03 |
| EV-nn | Sự kiện kích hoạt (nghiệp vụ, thời gian, hệ thống ngoài) | P02 | EV-07 |
| UC-nnn | Use case | P02 | UC-004 |
| CAND-nn | Ứng viên use case (kể cả bị loại) | P02 | CAND-15 |
| UCR-nn | Phát hiện khi review use case | P02R | UCR-04 |
| RL-nn | Quan hệ trên biểu đồ use case | P03 | RL-12 |
| GL-nn | Thuật ngữ | P05 | GL-12 |
| BR-nn | Quy tắc nghiệp vụ | P04, P06 | BR-05 |
| NFR-nn | Yêu cầu phi chức năng, ràng buộc thiết kế, giao tiếp ngoài (một dãy mã chung) | P06 | NFR-09 |
| AC-xxx | Lớp phân tích | P07, P08 | AC-B-PlaceOrderForm (B/C/E theo stereotype) |
| R-UCnnn-nn / R-nn | Quan hệ giữa lớp (R-UCnnn-nn cục bộ trong một UC ở P07; R-nn toàn hệ thống do P08 cấp, P12 dùng lại và cấp tiếp) | P07, P08, P12 | R-UC004-02, R-11 |
| E-<Ten> / ER-nn | Thực thể và mối quan hệ trong mô hình ER khái niệm | P13 | E-Reader, ER-02 |
| PKG-nn | Package / layer | P09, P10 | PKG-03 |
| SS-nn | Subsystem | P10 | SS-02 |
| IF-nn | Interface (subsystem, hệ thống ngoài, thiết bị, interface do cơ chế thiết kế); lớp thiết kế «interface» dùng chính mã IF-nn, không cấp DC. P12 cấp IF-nn mới nối tiếp số lớn nhất đã có, ghi lý do và đề xuất cập nhật P10 | P10, P11b, P12 | IF-01 |
| SCR-nn | Màn hình | P11a | SCR-06 |
| MSG-nn | Thông điệp giao diện (lỗi, xác nhận, thông tin) | P11a | MSG-14 |
| DC-xxx | Lớp thiết kế | P10, P11b, P12 | DC-OrderController |
| ST-nn | State machine | P12 | ST-01 |
| TBL-nn | Bảng / collection dữ liệu | P13 | TBL-04 |
| TC-nnn | Test case | X2 | TC-015 |
| RV-nn | Phát hiện review | X1 | RV-08 |

Mã Q-nn và ASM-nn đánh số liên tục trong toàn dự án, không đánh lại từ 01 ở mỗi artifact. Lần chạy nào cũng đọc các artifact đầu vào đã có, tìm mã Q và ASM lớn nhất đã thấy, rồi cấp tiếp từ số đó. Bước chạy lặp nhiều lần (P04 cho từng use case, P07 cho từng use case, P12 theo package) đọc thêm mục "Câu hỏi mở" và "Giả định" của các file cùng bước đã có trong thư mục đầu ra và cấp tiếp từ số lớn nhất trong đó. Nhờ vậy khi bước sau trích "Q-07", mã chỉ trỏ tới một câu hỏi duy nhất.

Quy ước tham chiếu trong văn bản: ghi mã kèm tên ở lần đầu trong mỗi mục, ví dụ "UC-004 Hủy lịch hẹn", sau đó có thể chỉ ghi mã.

## C4. Cấu trúc thư mục đầu ra

Gốc thư mục là THU_MUC_DAU_RA trong hồ sơ dự án. Tên file cố định để bước sau tìm được đầu vào.

```text
<THU_MUC_DAU_RA>/
  project-profile.md
  P00-problem-brief.md
  P01-actors.md
  P02-usecases.md
  P02R-review.md  (khi chạy review)
  P03-usecase-model.md
  P04-uc-specs/UC-nnn-<slug>.md  (mỗi lần chạy đọc mục Câu hỏi mở của các đặc tả đã có để cấp tiếp mã Q, ASM theo C3)
  P04-uc-specs/_BR-register.md  (sổ đăng ký mã BR, mỗi lần chạy P04 đọc và cập nhật)
  P05-glossary.md
  P06-supplementary-spec.md
  P07-uc-analysis/UC-nnn-<slug>-analysis.md
  P08-analysis-model.md
  P09-architecture.md
  P10-design-elements.md
  P11a-gui/  (ui-standards.md, screen-list.md, screen-transition.md, SCR-nn-<slug>.md, mockups/ chứa HTML tĩnh tuỳ chọn)
  P11b-system-interfaces.md
  P12-class-design.md  (hoặc P12-class-design/<PKG-nn>[-<PKG-mm>...]-<slug>.md khi chạy theo package; một lần chạy gồm nhiều package thì nối các mã PKG, ví dụ P12-class-design/PKG-05-PKG-06-stock.md)
  P13-data-model.md
  X1-design-review.md
  X2-unit-tests.md
  diagrams/  (mọi file .drawio, tên theo mục C7)
```

slug: tên tiếng Anh viết thường, nối bằng dấu gạch nối, ví dụ UC-004-cancel-appointment.

## C5. Khung chung của mọi artifact

Mỗi artifact là file Markdown, mở đầu bằng khối thông tin và kết thúc bằng các mục kiểm soát:

```text
# <Mã bước> - <Tên artifact> - <Tên hệ thống>

| Thuộc tính | Giá trị |
|---|---|
| Bước | Pxx |
| Phiên bản | 1.0 (tăng khi chạy lại) |
| Đầu vào đã dùng | Danh sách file và phiên bản |
| Phạm vi | Toàn hệ thống, hoặc UC-nnn cụ thể |

... nội dung chính theo đặc tả của bước ...

## Câu hỏi mở
| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |

## Giả định            (chỉ khi CHE_DO_GIA_DINH = CO_NHAN)
| Mã | Giả định | Lý do | Phần tử phụ thuộc |

## Đề xuất sửa artifact trước
| Bước | Mã phần tử | Vấn đề | Đề nghị |

## Vấn đề còn mở
Các mục trong checklist của bước chưa đạt và lý do.
```

Mục nào không có nội dung thì ghi "Không có", không xoá mục.

Không in lại checklist đã đạt vào artifact. Artifact chỉ chứa kết quả, không chứa lời dẫn kiểu "Dưới đây là...".

## C6. Placeholder trong prompt

Prompt được viết chung cho mọi bài toán. Phần phụ thuộc bài toán đặt trong placeholder theo cú pháp:

```text
{{PH:TEN_PLACEHOLDER | Hướng dẫn: cách điền | Ví dụ: một hoặc nhiều ví dụ}}
```

Quy tắc cho người dùng:

- Thay toàn bộ khối từ {{ tới }} bằng nội dung thật. Không để sót phần "Hướng dẫn", "Ví dụ".
- Placeholder có đánh dấu [TUỲ CHỌN] mà không dùng: thay cả khối từ {{ tới }} bằng "Không có", giữ nguyên dòng dẫn phía trên (ví dụ "Trọng tâm phân tích của lần chạy này: Không có"). Không xoá dòng dẫn để khỏi để lại câu treo.
- Placeholder YEU_CAU_BO_SUNG có ở mọi prompt: nơi ghi yêu cầu đặc thù của dự án cho bước đó (quy định riêng của tổ chức, lựa chọn đã chốt, điều cần bỏ qua). Yêu cầu bổ sung có thứ tự ưu tiên cao hơn quy tắc mặc định của bước, trừ các nguyên tắc ở mục C1.
- Thông tin dùng chung cho mọi bước (tên hệ thống, tài liệu nguồn, chế độ giả định, ngôn ngữ...) không điền trong prompt mà điền một lần ở project-profile.md.

Quy tắc cho AI:

- Nếu prompt còn khối {{PH:...}} chưa được thay, dừng lại và liệt kê các placeholder còn thiếu, không tự đoán nội dung, trừ khi placeholder có đánh dấu [TUỲ CHỌN] (khi đó bỏ qua). Placeholder [TUỲ CHỌN] có giá trị "Không có", để trống hoặc bị xoá đều hiểu là không dùng: áp dụng mặc định của bước.

## C7. Quy ước sơ đồ (draw.io)

### C7.1 Hai lớp biểu diễn

Mỗi sơ đồ có hai dạng:

1. Bảng mô hình trong artifact .md: là nguồn chuẩn, bước sau đọc bảng này. Gồm bảng Node và bảng Edge.
2. File .drawio sinh từ bảng mô hình: để xem và đưa vào tài liệu.

Khi sửa sơ đồ: sửa bảng mô hình trước, sau đó sinh lại file .drawio. Không để hai dạng lệch nhau.

Bảng mô hình tối thiểu:

```text
Node: | ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú |
Edge: | ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn (tuỳ chọn) |
```

Mỗi bước có thể thêm cột riêng (ví dụ thứ tự message cho sequence diagram). Khuyến nghị thêm bốn cột x, y, w, h vào bảng Node để file .drawio sinh ra từ bảng một cách tất định và giữ được bố cục khi sinh lại.

Cột Điểm uốn của bảng Edge là tuỳ chọn: danh sách toạ độ tuyệt đối theo thứ tự đi từ nguồn tới đích, dạng "(x1,y1); (x2,y2)", bội số của 10; cạnh đi thẳng hoặc để draw.io tự định tuyến ghi "-". Điền cột này cho cạnh mà định tuyến tự động sẽ cắt qua node (cạnh quay lại, cạnh vượt qua partition hoặc cột khác), để sinh lại file .drawio từ bảng vẫn giữ đường đi. Khi sinh file, mỗi điểm thành một mxPoint trong <Array as="points"> của mxGeometry của cạnh.

Cách tính điểm uốn cho sơ đồ nhiều cạnh (sơ đồ lớp, package, ERD), vì định tuyến tự động của draw.io thường cắt qua node khi có nhiều cạnh:

- Xếp node theo hàng. Cạnh nối hai hàng khác nhau đi trong dải trống giữa hai hàng: đoạn dọc ra khỏi node nguồn, một đoạn ngang trong dải, đoạn dọc vào node đích.
- Mỗi cạnh đi qua một dải dùng một làn y riêng, hai làn cách nhau 10. Cạnh nối hai node cùng hàng đi trong dải phía dưới hàng đó.
- Cổng ra, vào chia đều trên cạnh của node (exitX, exitY, entryX, entryY trong style), hai cạnh không dùng chung một cổng.
- Khoảng cách giữa hai hàng tối thiểu 40 + 10 x số cạnh đi qua dải giữa hai hàng.

### C7.2 Tên file sơ đồ

diagrams/<Mã bước>-<loại>-<phạm vi>.drawio. Danh sách tên chuẩn:

| Bước | Tên file |
|---|---|
| P03 | P03-usecase-overview, P03-usecase-<nhóm> |
| P04 | P04-activity-UC-nnn |
| P07 | P07-sequence-UC-nnn, P07-communication-UC-nnn, P07-class-UC-nnn |
| P08 | P08-class-analysis |
| P09 | P09-package-layers, P09-deployment |
| P10 | P10-package-design, P10-subsystem-context |
| P11a | P11a-screen-transition |
| P11b | P11b-subsystem-SS-nn |
| P12 | P12-class-PKG-nn (hoặc P12-class-<phạm vi> khi vẽ theo UC), P12-state-<DC> |
| P13 | P13-erd-conceptual, P13-erd-logical |
| X2 | X2-cfg-<DC>-<operation> |

### C7.3 Yêu cầu với file .drawio

- XML hợp lệ, mở được bằng draw.io (app.diagrams.net): gốc mxfile --> diagram --> mxGraphModel --> root, có hai cell gốc id="0" và id="1" parent="0".
- Không nén nội dung diagram (không dùng chuỗi base64 deflate), để người dùng và công cụ khác đọc và sửa được.
- ID của mxCell trùng hoặc suy ra được từ ID trong bảng mô hình.
- Mỗi sơ đồ một trang (diagram). Nhiều sơ đồ cùng bước có thể là nhiều trang trong một file khi chúng cùng phạm vi.
- Bố cục: toạ độ là bội số của 10; không có hai node chồng lên nhau; cạnh không cắt qua node; dùng edgeStyle=orthogonalEdgeStyle cho sơ đồ lớp, sơ đồ package, ERD; khoảng cách tối thiểu giữa hai node là 40.
- Multiplicity và tên vai trò của association, aggregation, composition là cell nhãn con của cạnh (style edgeLabel;resizable=0;html=1;align=left;verticalAlign=bottom;), x=-1 ở đầu nguồn, x=1 ở đầu đích. Không ghi chuỗi "A m - B n" của bảng quan hệ làm một nhãn giữa cạnh.
- Ký hiệu theo UML 2.5.1. Style cơ bản:

| Phần tử | Style draw.io |
|---|---|
| Actor | shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1; |
| Use case | ellipse;whiteSpace=wrap;html=1; |
| System boundary (subject) | rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=none; |
| Association (actor - use case) | endArrow=none;html=1; (biến thể có mũi tên: endArrow=open;html=1;, đuôi ở bên khởi xướng, đầu mũi tên mở ở bên nhận (tác nhân chính --> use case; use case --> tác nhân phụ), bật theo lựa chọn ở P03) |
| «include» / «extend» | endArrow=open;dashed=1;html=1; (nhãn «include» hoặc «extend») |
| Generalization | endArrow=block;endFill=0;html=1; |
| Class | swimlane;fontStyle=1;align=center;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;collapsible=0;html=1; (các ngăn thuộc tính, phương thức là cell con, ngăn cách bằng line) |
| Boundary / Control / Entity (icon) | shape=umlBoundary; / ellipse;shape=umlControl; / ellipse;shape=umlEntity; |
| Lifeline | shape=umlLifeline;perimeter=lifelinePerimeter;container=1;collapsible=0;recursiveResize=0;html=1; |
| Message đồng bộ / trả về | endArrow=block;endFill=1;html=1; / endArrow=open;dashed=1;html=1; |
| Association (class) | endArrow=none;html=1; hoặc endArrow=open khi có chiều điều hướng |
| Aggregation / Composition | startArrow=diamondThin;startFill=0; / startArrow=diamondThin;startFill=1; |
| Control flow (activity) | edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=open;endFill=0; (guard trong ngoặc vuông làm nhãn) |
| Đồ thị luồng điều khiển (X2) | quyết định: rhombus;html=1; / khối lệnh: rounded=0;whiteSpace=wrap;html=1; / bắt đầu, kết thúc: style Activity initial / final / cạnh: endArrow=block;endFill=1;html=1; (nhãn Đúng / Sai) |
| Dependency | endArrow=open;dashed=1;html=1; |
| Realization | endArrow=block;endFill=0;dashed=1;html=1; |
| Package | shape=folder;tabWidth=80;tabHeight=20;tabPosition=left;html=1; |
| Subsystem | shape=component;html=1; (nhãn «subsystem») |
| Interface dạng rút gọn (lollipop) | ellipse;html=1; kích thước 20 x 20 |
| Message bất đồng bộ | endArrow=open;endFill=0;html=1; |
| Combined fragment (opt, alt, break, loop, ref) | rounded=0;whiteSpace=wrap;html=1;fillColor=none;align=left;verticalAlign=top; |
| Node (deployment) | shape=cube;whiteSpace=wrap;html=1; |
| Bảng ERD (logic, vật lý) | như Class: swimlane stackLayout, mỗi cột một dòng con |
| Quan hệ ERD chân chim | startArrow=ERmandOne;endArrow=ERzeroToMany;html=1; (dashed=1 cho quan hệ không định danh nếu dự án dùng quy ước đó) |
| Thực thể / thực thể yếu / thuộc tính (Chen) | rounded=0; / shape=ext;double=1; / ellipse; |
| Chuyển trạng thái | endArrow=open;endFill=0;html=1; |
| Dịch chuyển màn hình | theo mục F3 của P11a-gui-design.md |
| Activity initial / final | ellipse;fillColor=#000000; / ellipse;shape=endState;fillColor=#000000; (kích thước 40x40: node 30x30 không căn tâm được với action rộng 180 khi toạ độ là bội số của 10) |
| Action | rounded=1;whiteSpace=wrap;html=1;arcSize=40; |
| Decision / Merge | rhombus;html=1; |
| Fork / Join | shape=line;strokeWidth=4;html=1; (thanh đậm) |
| Swimlane (partition) | swimlane;html=1;startSize=40; (partition dọc); swimlane;horizontal=0;html=1; (partition ngang) |
| State | rounded=1;whiteSpace=wrap;html=1;arcSize=30; |
| Note | shape=note;whiteSpace=wrap;html=1;size=14; |

- Không dùng màu để mang ngữ nghĩa. Màu (nếu có) chỉ để dễ nhìn và phải nhất quán trong toàn bộ dự án.
- Chữ trong sơ đồ dùng dấu « » cho stereotype, ví dụ «include», «entity».

## C8. Quy tắc định dạng Markdown của artifact

- Bảng Markdown chuẩn. Ô nhiều dòng dùng thẻ <br>.
- Mỗi artifact có một tiêu đề cấp 1 duy nhất.
- Không dùng biểu tượng cảm xúc.
- Trích dẫn tài liệu nguồn: đặt trong ngoặc kép, kèm vị trí (mục, đoạn, dòng) nếu tài liệu có.

## C9. Thứ tự ưu tiên khi quy tắc xung đột

1. Nguyên tắc làm việc ở mục C1.
2. Yêu cầu bổ sung (YEU_CAU_BO_SUNG) của người dùng trong prompt đang chạy.
3. Ràng buộc đặc thù trong hồ sơ dự án.
4. Quy tắc riêng của bước (trong prompt).
5. Quy ước chung trong file này (C2 đến C8).

Khi phải chọn giữa hai quy tắc, ghi lại lựa chọn và lý do trong mục "Vấn đề còn mở".
