# X1 - Review thiết kế (Design Review)

## 1. Mục đích

Bước này đánh giá chéo thiết kế (kiến trúc, phần tử thiết kế, lớp, dữ liệu) theo các tiêu chí đã được kiểm chứng: tính module, mức coupling, mức cohesion, nguyên lý thiết kế hướng đối tượng (SOLID, GRASP và các nguyên lý bổ trợ), nguyên lý package, dấu hiệu thiết kế kém (design smell) và tính nhất quán giữa các artifact. Kết quả là danh sách phát hiện có mức độ, bằng chứng, đề xuất sửa và bước cần chạy lại. Bước này chạy sau P12/P13 trong pipeline, nhưng cũng dùng độc lập được cho thiết kế do người viết hoặc cho mã nguồn có sẵn.

## 2. Đầu vào và đầu ra

| Loại | Artifact | Bắt buộc | Dùng để |
|---|---|---|---|
| Đầu vào | project-profile.md | Có | Chế độ giả định, mức chi tiết, công nghệ |
| Đầu vào | P12-class-design.md (hoặc P12-class-design/*.md) | Có (trừ khi review độc lập) | Lớp, operation, thuộc tính, quan hệ, state machine |
| Đầu vào | P13-data-model.md | Không | Review dữ liệu và nhất quán lớp - bảng |
| Đầu vào | P09-architecture.md, P10-design-elements.md | Không (nên có) | Layer, package, subsystem, interface, quy tắc phụ thuộc |
| Đầu vào | P11b-system-interfaces.md | Không | Interface với hệ thống ngoài |
| Đầu vào | P07-uc-analysis/*.md, P08-analysis-model.md | Không | Kiểm tra truy vết message --> operation |
| Đầu vào | P06-supplementary-spec.md | Không | NFR (khả năng bảo trì, mở rộng, hiệu năng) làm căn cứ mức độ |
| Đầu vào | Thiết kế hoặc mã nguồn do người dùng cung cấp | Có khi review độc lập | Đối tượng review khi không chạy pipeline |
| Đầu ra | X1-design-review.md | Có | Bảng phát hiện và các bảng đánh giá |

## 3. Cách chạy

- Đính kèm: 00-Conventions.md, project-profile.md và các artifact cần review.
- Chạy một lần cho phạm vi đã chọn. Với hệ thống lớn, chạy theo package; mỗi lần ghi phạm vi rõ trong PHAM_VI_REVIEW, các lần chạy sau tiếp tục đánh số RV (không trùng mã).
- Sau khi sửa theo phát hiện, chạy lại X1 với cùng phạm vi; phát hiện cũ giữ mã, cập nhật cột Trạng thái.
- Placeholder cần điền trong prompt:

| Placeholder | Bắt buộc | Ý nghĩa |
|---|---|---|
| PHAM_VI_REVIEW | Có | Artifact, package hoặc lớp cần review |
| NHOM_TIEU_CHI | Tuỳ chọn | Chỉ áp dụng một số nhóm tiêu chí |
| THIET_KE_DOC_LAP | Tuỳ chọn | Mô tả thiết kế hoặc mã nguồn khi review ngoài pipeline |
| MA_RV_BAT_DAU | Tuỳ chọn | Mã RV bắt đầu khi đã có lần review trước |
| YEU_CAU_BO_SUNG | Tuỳ chọn | Yêu cầu đặc thù khác |

## 4. Prompt

````text
[Context]
Bạn nhận được: 00-Conventions.md (luật chung, bắt buộc tuân thủ), project-profile.md và các artifact thiết kế cần review (P12 là chính; P09, P10, P11b, P13, P07, P08, P06 khi có đính kèm).
Phạm vi review:
{{PH:PHAM_VI_REVIEW | Hướng dẫn: liệt kê artifact và phần tử cần review; ghi "Toàn bộ thiết kế" nếu review mọi artifact đính kèm | Ví dụ: "Toàn bộ thiết kế (P09, P10, P12, P13)"; "PKG-04 Xuất nhập kho trong P12 và các bảng liên quan trong P13"; "Chỉ các lớp DC-LoanController, DC-Loan, DC-FineCalculator"}}
Nhóm tiêu chí áp dụng:
{{PH:NHOM_TIEU_CHI | Hướng dẫn: [TUỲ CHỌN] chọn trong: MOD (tính module), CPL (coupling), COH (cohesion), SOLID, GRASP, PRN (nguyên lý bổ trợ), PKP (nguyên lý package), SML (design smell), CNS (nhất quán artifact), DAT (dữ liệu); áp dụng tất cả thì thay cả khối bằng "Không có" | Ví dụ: "CPL, COH, SOLID"; "PKG, CNS"}}
Thiết kế cần review khi dùng độc lập:
{{PH:THIET_KE_DOC_LAP | Hướng dẫn: [TUỲ CHỌN] chỉ dùng khi không review artifact của pipeline: dán hoặc đính kèm class diagram (ảnh, XML draw.io, PlantUML), mô tả lớp, hoặc mã nguồn, kèm mô tả ngắn chức năng hệ thống; review artifact pipeline thì thay cả khối bằng "Không có" | Ví dụ: "File class-diagram.drawio và mô tả: hệ thống đặt phòng khách sạn gồm đặt phòng, nhận phòng, trả phòng"; "Thư mục src/inventory/ (Java) của phân hệ quản lý kho"}}
Mã phát hiện bắt đầu:
{{PH:MA_RV_BAT_DAU | Hướng dẫn: [TUỲ CHỌN] mã RV đầu tiên cho lần chạy này khi đã có file X1 trước đó; đính kèm file X1 cũ để cập nhật trạng thái; lần đầu thì thay cả khối bằng "Không có" (bắt đầu RV-01) | Ví dụ: "RV-23"}}

[Role]
Bạn là chuyên gia review thiết kế phần mềm hướng đối tượng, thành thạo thiết kế module (coupling, cohesion theo Yourdon và Constantine, Myers), SOLID và nguyên lý package (Robert C. Martin), GRASP (Larman), design pattern (Gamma và cộng sự), design smell và refactoring (Fowler), mô hình dữ liệu quan hệ. Bạn review khách quan: mọi kết luận đều có bằng chứng trích từ đầu vào, không phán đoán theo cảm nhận, không phê bình chung chung.

[Action]
Bước 0. Chuẩn bị.
- Kiểm tra placeholder theo Conventions C6.
- Lập danh mục phần tử trong phạm vi: package, subsystem, interface, lớp, operation, quan hệ, bảng. Với review độc lập, gán mã tạm EXT-<Ten> cho mỗi phần tử (lớp, module, bảng) và dùng mã này trong bảng phát hiện.
- Đọc NFR liên quan tới khả năng bảo trì, mở rộng, hiệu năng, bảo mật để làm căn cứ đánh giá mức độ.

Bước 1. Review tính module (MOD).
- Với mỗi package/subsystem: kiểm tra phân rã được (decomposable), ghép lại được qua interface rõ (composable), hiểu được khi xem riêng (understandable), thay đổi nhỏ về yêu cầu chỉ ảnh hưởng ít module (continuity), lỗi một module không lan (protection).
- Phép thử continuity: chọn 2-3 thay đổi yêu cầu có khả năng xảy ra (từ NFR, BR dễ đổi, hệ thống ngoài có thể thay) và đếm số lớp/package phải sửa.

Bước 2. Review coupling (CPL).
- Với mỗi cặp phần tử có quan hệ (association, dependency, lời gọi operation, dữ liệu dùng chung), xác định kênh phụ thuộc và mức coupling theo thang ở [Format] F3.
- Dựa trên chữ ký operation (tham số cờ, tham số là cấu trúc phức hợp), đặc tả method (trường nào của tham số được dùng), thuộc tính public, thuộc tính/đối tượng dùng chung toàn cục, truy cập trực tiếp dữ liệu nội bộ lớp khác.
- Kiểm tra Law of Demeter trên đặc tả method và sequence diagram: chuỗi lời gọi xuyên qua đối tượng trả về.

Bước 3. Review cohesion (COH).
- Với mỗi lớp (và mỗi operation có đặc tả method dài), xác định mức cohesion theo thang ở [Format] F4, dựa trên: câu trách nhiệm, nhóm operation, thuộc tính được operation nào dùng, lý do các phần tử được đặt cùng nhau.

Bước 4. Review nguyên lý (SOLID, GRASP, PRN).
- Áp dụng từng nguyên lý ở [Format] F5 lên phần tử trong phạm vi, ưu tiên các điểm nóng: lớp control, lớp có nhiều quan hệ, cây kế thừa, interface, ranh giới layer, lớp giao tiếp hệ thống ngoài.

Bước 5. Review package (PKP).
- Dựng đồ thị phụ thuộc package từ quan hệ lớp; tìm vòng; kiểm tra chiều layer; tính chỉ số Ca, Ce, I, A, D ở [Format] F6.3 (chỉ khi DAY_DU).

Bước 6. Review design smell (SML), nhất quán (CNS) và dữ liệu (DAT) theo danh mục ở [Format] F5.

Bước 7. Lập bảng phát hiện.
- Mỗi vi phạm là một dòng RV; gộp các biểu hiện của cùng một nguyên nhân gốc vào một dòng và liệt kê các phần tử bị ảnh hưởng.
- Gán mức độ theo định nghĩa ở [Format] F2; ghi độ tin cậy.
- Đề xuất sửa cụ thể (refactoring hoặc thay đổi mô hình), nêu bước pipeline cần chạy lại.
- Khi hai nguyên lý mâu thuẫn (ví dụ Information Expert muốn đặt logic lưu trữ vào entity nhưng High Cohesion muốn tách ra Pure Fabrication), ghi lựa chọn và đánh đổi, không ghi thành hai phát hiện trái chiều.

Bước 8. Tự kiểm tra theo [Target].

[Format]
Đầu ra là file X1-design-review.md theo khung Conventions C5, gồm F1 đến F7 theo thứ tự, sau đó là các mục kiểm soát (Câu hỏi mở, Giả định nếu CO_NHAN, Đề xuất sửa artifact trước, Vấn đề còn mở). Mục "Đề xuất sửa artifact trước" ghi "Xem bảng phát hiện F2" vì toàn bộ đề xuất nằm ở F2.

F1. Phạm vi và phương pháp
Bảng: | Hạng mục | Nội dung |
Gồm: artifact và phiên bản đã review; phần tử trong phạm vi (số package, lớp, bảng); nhóm tiêu chí đã áp dụng; phần không review được và lý do (ví dụ thiếu đặc tả method nên không xác định chắc chắn stamp coupling).

F2. Bảng phát hiện
Cột lõi: | RV | Nguyên lý / tiêu chí vi phạm | Phần tử | Bằng chứng | Mức độ | Đề xuất sửa | Bước cần sửa |
Cột thêm: | Nhóm (MOD / CPL / COH / SOLID / GRASP / PRN / PKP / SML / CNS / DAT) | Độ tin cậy (Chắc chắn / Cần xác nhận) | Trạng thái (Mở / Đã sửa / Chấp nhận có lý do) |
- RV: mã RV-nn theo Conventions C3, tuần tự, không tái sử dụng.
- Nguyên lý / tiêu chí vi phạm: ghi tên chính xác theo danh mục F3-F5, ví dụ "CPL Control coupling", "SOLID DIP", "SML Feature envy", "CNS Operation không có nguồn message".
- Phần tử: mã phần tử (DC, DC.operation, R-nn, PKG, SS, IF, TBL, TBL.cột, EXT-).
- Bằng chứng: trích nguyên văn chữ ký, dòng bảng, hoặc mô tả method; nêu vị trí (artifact, mục, bảng). Phát hiện không có bằng chứng cụ thể thì không ghi.
- Mức độ:
  - Nghiêm trọng: thiết kế không hiện thực đúng yêu cầu hoặc BR; mất toàn vẹn dữ liệu; phụ thuộc vòng giữa layer; content coupling; vi phạm LSP làm hành vi sai khi thay thế.
  - Cao: vi phạm gây thay đổi lan rộng hoặc cản trở thay thế thành phần: common coupling, god class, lớp nghiệp vụ phụ thuộc lớp hiện thực của hệ thống ngoài (DIP), phụ thuộc ngược layer.
  - Trung bình: ảnh hưởng khả năng bảo trì cục bộ: control coupling, stamp coupling không cần thiết, cohesion logical/temporal/procedural, interface quá lớn, điều hướng hai chiều không cần.
  - Thấp: đặt tên, mô tả thiếu, trình bày sơ đồ, vi phạm nhỏ không ảnh hưởng hành vi.
  Có thể nâng một mức khi phần tử nằm trên đường thay đổi mà NFR hoặc BR cho biết là dễ đổi; ghi lý do nâng.
- Đề xuất sửa: hành động cụ thể: tên refactoring (Extract Class, Move Method, Replace Conditional with Polymorphism, Introduce Parameter Object, Extract Interface, Replace Inheritance with Delegation, Hide Delegate...) kèm phần tử đích; hoặc thay đổi mô hình (đổi loại quan hệ, tách bảng).
- Bước cần sửa: mã bước pipeline cần chạy lại sớm nhất (P09, P10, P11b, P12, P13); với review độc lập ghi "Thiết kế đầu vào" hoặc "Mã nguồn".
- Mức hợp lý: một dòng một nguyên nhân gốc; không tách một god class thành năm dòng SRP, cohesion, coupling giống nhau (ghi một dòng, liệt kê các tiêu chí liên quan ở cột Nguyên lý).
- Lỗi thường gặp: phát hiện chung chung không bằng chứng; đề xuất "cải thiện thiết kế" không nói cách; đánh mọi thứ là Nghiêm trọng; review theo khẩu vị (đổi tên theo sở thích); đề xuất pattern không giải quyết vấn đề cụ thể.
- Ví dụ đúng (quản lý kho): | RV-04 | CPL Control coupling; SOLID OCP | DC-StockController.updateStock(action: Integer, item: StockItem) | P12 F2: "action: 1 nhập, 2 xuất, 3 điều chỉnh"; method F3 rẽ nhánh theo action | Trung bình | Tách thành receive(item, qty), issue(item, qty), adjust(item, qty, reason); bên gọi gọi operation đúng nghĩa | P12 | CPL | Chắc chắn | Mở |
- Ví dụ đúng (phòng khám): | RV-07 | SOLID DIP; GRASP Protected Variations | DC-AppointmentService, DC-VendorSmsClient | R-14 association từ DC-AppointmentService tới DC-VendorSmsClient (lớp hiện thực của nhà cung cấp SMS) | Cao | Cho DC-AppointmentService phụ thuộc IF-02 ISmsNotifier; DC-VendorSmsClient hiện thực interface; khởi tạo qua cấu hình | P12 | SOLID | Chắc chắn | Mở |
- Ví dụ sai: | RV-09 | SRP | DC-OrderService | Lớp này quá lớn | Cao | Nên refactor | P12 | Sai: không có bằng chứng (lớp có những trách nhiệm nào, lý do thay đổi nào), đề xuất không cụ thể.

F3. Đánh giá coupling
Bảng: | Phần tử A (phụ thuộc) | Phần tử B (được dùng) | Kênh phụ thuộc (thuộc tính / tham số / biến cục bộ / toàn cục / kế thừa / truy cập trực tiếp dữ liệu) | Mức coupling | Bằng chứng | Chấp nhận (Có / Không: RV) |
- Mỗi cặp có mức khác Data coupling một dòng riêng. Các cặp Data coupling gộp theo phần tử A và kênh: một dòng liệt kê mọi phần tử B ở cột Phần tử B (cách nhau bằng thẻ <br>), ví dụ "DC-LoanService | DC-Loan<br>DC-BookCopy<br>DC-Reader | tham số | Data | ...".
Thang mức coupling (từ chặt, xấu nhất tới lỏng, tốt nhất):
1. Content coupling: module dùng nội dung (dữ liệu, điều khiển) nằm trong ranh giới của module khác: sửa trực tiếp dữ liệu của module khác (thuộc tính public bị lớp khác gán; lớp khác thao tác trực tiếp tập hợp nội bộ được trả về qua getter; dùng reflection đọc/ghi thuộc tính private), nhảy vào giữa thủ tục của module khác. Cách sửa: truy cập qua operation của module sở hữu dữ liệu; không bao giờ sửa điều khiển của module khác.
2. Common coupling: nhiều module cùng đọc/ghi một vùng dữ liệu hoặc cấu trúc dữ liệu toàn cục (biến static có thể thay đổi, singleton giữ trạng thái chung, bảng dùng chung mà nhiều module cùng ghi không qua một chủ sở hữu). Hệ quả: lỗi lan khắp hệ thống, khó biết ai thay đổi dữ liệu, khó dùng lại. Cách sửa: giao dữ liệu cho một module quản lý, module khác gửi yêu cầu tới module đó.
3. Control coupling: một module điều khiển việc module khác làm bằng tham số điều khiển (cờ, mã hành động, mã loại) khiến bên nhận làm những việc khác nhau. Cách sửa: tách thành các operation riêng; dùng đa hình (kế thừa hoặc interface) cho các loại; dùng pattern (Strategy, State, Command) khi phù hợp.
4. Stamp coupling: truyền cấu trúc dữ liệu phức hợp (đối tượng, bản ghi) mà bên nhận chỉ dùng một phần. Hệ quả: bên nhận phải biết cấu trúc, thay đổi cấu trúc ảnh hưởng mọi bên dùng, lộ dữ liệu không cần. Có thể chấp nhận vì hiệu năng hoặc khi đối tượng là một khái niệm trọn vẹn mà bên nhận dùng phần lớn. Cách sửa: chỉ truyền dữ liệu nguyên tố cần thiết.
5. Data coupling: mọi tham số là dữ liệu nguyên tố cần thiết, hoặc cấu trúc dữ liệu mà mọi phần tử đều được dùng; giao tiếp chỉ qua tham số, không qua biến toàn cục. Là mức mong muốn.
Ngoài thang: không có phụ thuộc (tốt nhất khi có thể). External coupling (hai module dùng chung một định dạng hoặc giao thức áp đặt từ bên ngoài, xếp giữa common và control theo Myers) ghi khi phát hiện, đề xuất cô lập bằng adapter.
Law of Demeter ("chỉ nói chuyện với bạn trực tiếp"): trong một method, đối tượng chỉ gửi message tới: chính nó; thuộc tính của nó; tham số của method; đối tượng nó tạo ra; đối tượng trả về từ operation của chính nó; phần tử của tập hợp thuộc các loại trên. Không gửi message tới đối tượng được trả về từ message gửi cho đối tượng khác. Dấu hiệu vi phạm: chuỗi a.getB().getC().doX() trong đặc tả method hoặc sequence diagram. Cách sửa: thêm operation ủy quyền ở bên trực tiếp (Hide Delegate) nêu ý định, ví dụ reservation.getRoom().getRoomType().getBaseRate() --> reservation.quoteBaseRate().
Về getter/setter cho mọi thuộc tính private: không phải content coupling theo nghĩa hẹp (truy cập qua operation), nhưng làm lộ biểu diễn nội bộ và dễ dẫn tới feature envy; ghi thành phát hiện PRN Encapsulation khi bên ngoài dùng getter để tự ra quyết định thay cho đối tượng sở hữu dữ liệu.
Lỗi thường gặp khi đánh giá: coi mọi tham số đối tượng là stamp coupling (chỉ là stamp khi bên nhận dùng một phần nhỏ); không phát hiện common coupling qua singleton hoặc bảng CSDL dùng chung; nhầm control coupling với tham số dữ liệu dạng enumeration mang nghĩa nghiệp vụ (ví dụ paymentMethod được lưu lại, không dùng để rẽ nhánh hành vi của bên nhận thì là data).

F4. Đánh giá cohesion
Bảng: | Phần tử (PKG / DC / DC.operation) | Mức cohesion | Lý do (nhóm phần tử và lý do đặt cùng nhau) | Chấp nhận (Có / Không: RV) |
Thang mức cohesion (từ thấp, xấu nhất tới cao, tốt nhất):
1. Coincidental: các phần tử không liên quan, chỉ tình cờ nằm cùng chỗ. Dấu hiệu: tên lớp chung chung hoặc nối nhiều danh từ bằng "And/With" (CustomerAndReportAndMailUtil); lớp "Utils" chứa hàm của nhiều miền. Sửa: chuyển từng phần sang module chịu trách nhiệm tương ứng.
2. Logical: các phần tử cùng loại việc nhưng độc lập, bên gọi chọn một bằng tham số (ví dụ một lớp xử lý mọi loại nhập liệu: từ bàn phím, tệp, máy quét; một hàm xử lý mọi loại lỗi theo mã lỗi). Thường kéo theo control coupling. Sửa: tách theo từng loại, dùng kế thừa/đa hình (một interface đọc dữ liệu, mỗi nguồn một lớp hiện thực).
3. Temporal: các phần tử được gom vì chạy cùng thời điểm (khởi động, kết thúc, cuối ngày). Sửa: mỗi thành phần tự khởi tạo/dọn dẹp; module thời điểm chỉ gửi thông điệp tới từng thành phần.
4. Procedural: các phần tử được gom vì chạy theo một trình tự, nhưng làm việc trên dữ liệu khác nhau (đọc mã hàng từ CSDL rồi cập nhật phiếu bảo trì). Sửa: để module sở hữu dữ liệu tự làm phần của mình; module điều phối chỉ gọi ở mức trừu tượng.
5. Communicational: các phần tử dùng chung dữ liệu vào hoặc ra nhưng làm việc khác nhau (cập nhật bản ghi rồi ghi nhật ký kiểm toán rồi in bản ghi). Sửa: tách để dùng lại riêng từng việc.
6. Sequential: đầu ra của phần tử này là đầu vào của phần tử sau trong cùng một chuỗi xử lý. Chấp nhận được; nếu chuỗi không tạo thành một chức năng trọn vẹn thì cân nhắc tách.
7. Functional: mọi phần tử cùng hướng tới một trách nhiệm được định nghĩa rõ, và mọi phần tử cần cho trách nhiệm đó đều nằm trong module; tên module nói lên trách nhiệm. Là mức mong muốn.
Cách xác định ở mức lớp: gom operation theo thuộc tính chúng dùng; nếu có hai nhóm operation dùng hai nhóm thuộc tính rời nhau, lớp có ít nhất hai trách nhiệm (cohesion thấp, SRP). Ở mức package: dùng tiêu chí CCP/CRP ở F6.
God class: lớp ôm quá nhiều dữ liệu hoặc chức năng; chỉ giảm coupling bằng cách dồn nhiều module vào một; là anti-pattern, ghi mức Cao.
Ví dụ đúng (khách sạn): | DC-NightAuditJob | Temporal | Gom đóng ngày: tính tiền phòng qua đêm, sao lưu, gửi báo cáo, xoá phiên đăng nhập, cùng chạy lúc 0 giờ | Không: RV-11 |
Ví dụ đúng (thư viện): | DC-FineCalculator | Functional | Mọi operation phục vụ tính tiền phạt quá hạn theo chính sách | Có |

F5. Danh mục nguyên lý, design smell, nhất quán, dữ liệu
Bảng tổng hợp theo nguyên lý: | Nguyên lý | Phần tử đã xét | Kết luận (Đạt / Vi phạm: RV) |
Áp dụng các tiêu chí sau (mỗi tiêu chí: phát biểu, dấu hiệu vi phạm, cách sửa).

SOLID
- SRP (Single Responsibility): một lớp chỉ có một lý do để thay đổi. Dấu hiệu: operation phục vụ các nhóm người dùng/tác nhân khác nhau; một entity vừa chứa dữ liệu nghiệp vụ vừa quyết định thứ tự sắp xếp, định dạng in, lưu trữ. Sửa: Extract Class theo lý do thay đổi.
- OCP (Open/Closed): mở cho mở rộng, đóng cho sửa đổi. Dấu hiệu: switch/if theo mã loại lặp lại ở nhiều nơi; thêm một loại mới phải sửa lớp đã chạy ổn. Sửa: trừu tượng hoá (interface/lớp trừu tượng), đa hình động (ghi đè) hoặc tĩnh (generic).
- LSP (Liskov Substitution): lớp con thay thế được lớp cha mà bên dùng không cần biết. Lớp con không đòi hỏi hơn (không siết tiền điều kiện, chấp nhận mọi tham số lớp cha chấp nhận) và không hứa kém hơn (không làm yếu hậu điều kiện). Dấu hiệu: lớp con ném "không hỗ trợ", ghi đè thành rỗng, bên dùng kiểm tra kiểu cụ thể; kế thừa chỉ để dùng lại hiện thực. Sửa: tách cây kế thừa, dùng composition/delegation.
- ISP (Interface Segregation): bên dùng không bị buộc phụ thuộc vào operation nó không dùng. Dấu hiệu: interface lớn phục vụ nhiều loại bên gọi; lớp hiện thực để trống nhiều operation. Sửa: Extract Interface theo nhóm bên dùng.
- DIP (Dependency Inversion): module mức cao không phụ thuộc module mức thấp, cả hai phụ thuộc trừu tượng; interface được định nghĩa theo nhu cầu của phía mức cao. Về vị trí trong kiến trúc phân lớp, quy tắc của P09 A5 áp dụng: mũi tên phụ thuộc và realization không đi lên, nên interface đặt ở package cùng layer với lớp hiện thực hoặc thấp hơn; khi layer dưới cần gọi ngược lên, layer dưới định nghĩa interface và layer trên hiện thực. Dấu hiệu: lớp nghiệp vụ/control có association tới lớp truy cập CSDL cụ thể, tới SDK của hệ thống ngoài; lớp nghiệp vụ tự khởi tạo lớp hạ tầng bằng new; lớp ở layer dưới hiện thực interface nằm ở layer trên. Sửa: Extract Interface theo nhu cầu của phía nghiệp vụ, đặt interface theo quy tắc vị trí trên, tiêm phụ thuộc (dependency injection).

GRASP
- Information Expert: giao trách nhiệm cho lớp có thông tin cần để thực hiện. Vi phạm: control tự tính tổng đơn bằng cách lấy từng dòng thay vì Order.calculateTotal().
- Creator: lớp B tạo A khi B chứa/gộp A, ghi nhận A, dùng chặt A, hoặc có dữ liệu khởi tạo A. Vi phạm: boundary tạo entity bộ phận thay vì toàn thể tạo.
- Controller: sự kiện hệ thống từ giao diện được nhận bởi lớp control đại diện UC hoặc hệ thống, không bởi boundary. Vi phạm: boundary chứa quy tắc nghiệp vụ; controller phình (bloated) xử lý nhiều UC không liên quan.
- Low Coupling, High Cohesion: xem F3, F4.
- Polymorphism: hành vi thay đổi theo loại được giao cho các loại qua operation đa hình, không rẽ nhánh theo loại.
- Pure Fabrication: lớp không có trong miền, được tạo ra để giữ cohesion cao và coupling thấp (repository, dịch vụ gửi thông báo). Vi phạm ngược: entity tự lưu vào CSDL, tự gửi email.
- Indirection: đặt trung gian để tách hai thành phần (adapter, interface).
- Protected Variations: xác định điểm dễ biến đổi (hệ thống ngoài, chính sách giá, luật tính phí) và bọc bằng interface ổn định.

Nguyên lý bổ trợ (PRN)
- Encapsulation / Information hiding: thuộc tính private, lộ hành vi chứ không lộ dữ liệu ("tell, don't ask").
- Favor composition over inheritance: dùng kế thừa chỉ cho quan hệ "là một loại" thật sự; dùng lại hiện thực bằng composition.
- Program to an interface, not an implementation: kiểu của thuộc tính, tham số là interface hoặc lớp trừu tượng ở ranh giới dễ thay đổi.
- Law of Demeter: xem F3.
- DRY (Don't Repeat Yourself): một tri thức (quy tắc, công thức, ràng buộc) có một nơi biểu diễn duy nhất. Dấu hiệu: cùng BR được kiểm tra ở boundary, control và entity với cách viết khác nhau; cùng công thức ở hai lớp.
- KISS: chọn giải pháp đơn giản nhất đáp ứng yêu cầu. Dấu hiệu: tầng trừu tượng không có biến thể, pattern chồng pattern.
- YAGNI: không thiết kế cho yêu cầu chưa có. Dấu hiệu: interface chỉ có một hiện thực không có lý do thay thế, tham số "để sau này dùng", lớp cha trừu tượng cho một lớp con (speculative generality).

Design smell (SML), phát hiện được từ mô hình thiết kế
- God class / Large class: xem F4.
- Data class: lớp chỉ có thuộc tính và getter/setter, logic dùng dữ liệu của nó nằm ở lớp khác. Sửa: Move Method vào lớp dữ liệu.
- Feature envy: operation dùng dữ liệu của lớp khác nhiều hơn của lớp mình. Sửa: Move Method.
- Shotgun surgery: một thay đổi yêu cầu sửa nhiều lớp. Divergent change: một lớp bị sửa vì nhiều lý do khác nhau. Sửa: gom thứ cùng thay đổi, tách thứ khác lý do thay đổi.
- Long parameter list, Data clumps (nhóm dữ liệu luôn đi cùng nhau nhưng không thành lớp), Primitive obsession (dùng kiểu nguyên thuỷ cho khái niệm có quy tắc riêng như tiền, mã vạch). Sửa: Introduce Parameter Object, Extract Class, Value Object.
- Switch statements theo mã loại. Sửa: Replace Conditional with Polymorphism.
- Message chains, Middle man, Inappropriate intimacy (hai lớp biết quá nhiều về nhau, quan hệ hai chiều không cần). Sửa: Hide Delegate, Remove Middle Man, đổi quan hệ hai chiều thành một chiều.
- Refused bequest (lớp con không dùng phần lớn thứ thừa hưởng), Lazy class (lớp không làm đủ việc để tồn tại), Speculative generality.
- Hidden dependencies (lớp tự lấy phụ thuộc từ nơi toàn cục thay vì khai báo qua constructor), Temporal coupling ẩn (bên gọi phải nhớ gọi các operation theo thứ tự không được khai báo).

Nguyên lý package (PKP)
- Không phụ thuộc vòng giữa package (ADP, Acyclic Dependencies Principle). Sửa: tách package, đảo phụ thuộc bằng interface.
- Package layer dưới không phụ thuộc package layer trên; phụ thuộc không nhảy qua layer trừ khi kiến trúc cho phép.
- Chỉ lớp public của package được tham chiếu từ ngoài package.
- REP (Reuse/Release Equivalence): đơn vị dùng lại là đơn vị phát hành; lớp trong một package dùng lại được cùng nhau.
- CCP (Common Closure): lớp thay đổi cùng lý do nằm cùng package.
- CRP (Common Reuse): lớp không được dùng cùng nhau thì không nằm cùng package (bên dùng một lớp không phải phụ thuộc cả package).
- SDP (Stable Dependencies): phụ thuộc theo chiều ổn định hơn (I của package được phụ thuộc nhỏ hơn I của package phụ thuộc).
- SAP (Stable Abstractions): package càng ổn định càng trừu tượng (D gần 0).

Nhất quán giữa artifact (CNS)
- Mọi message trong P07 có operation ở P12; mọi operation public có nguồn.
- Mọi AC trong P10 có DC hoặc lý do; mọi IF trong P11b có lớp «interface» và lớp hiện thực.
- State machine khớp operation (sự kiện) và thuộc tính (trạng thái); guard khớp BR.
- Multiplicity P12 khớp BR và khớp NULL/FK ở P13; mọi lớp persistent có bảng; mọi cột có nguồn.
- Class diagram khớp bảng lớp, operation, quan hệ.
- Tên dùng đúng glossary.

Dữ liệu (DAT)
- Bảng chưa đạt 3NF mà không có lý do phi chuẩn hoá; phi chuẩn hoá thiếu cơ chế nhất quán.
- Composition không CASCADE; FK sai phía; M:N không có bảng trung gian; thiếu UNIQUE cho khoá nghiệp vụ.
- Kiểu số thực cho tiền; thiếu CHECK cho BR dạng miền giá trị.
- Index không có truy vấn phục vụ, hoặc truy vấn thường xuyên theo NFR không có index.

F6. Phụ thuộc package
F6.1. Bảng phụ thuộc: | PKG nguồn | PKG đích | Quan hệ lớp tạo ra phụ thuộc (R-nn) | Hợp lệ theo layer (Có / Không) |
F6.2. Vòng phụ thuộc: liệt kê từng vòng (PKG-a --> PKG-b --> PKG-a) hoặc "Không có".
F6.3. Chỉ số (chỉ khi DAY_DU): | PKG | Ca (số lớp ngoài package phụ thuộc vào lớp trong package) | Ce (số lớp ngoài package mà lớp trong package phụ thuộc) | I = Ce / (Ca + Ce) | A = số lớp trừu tượng và interface / tổng số lớp | D = abs(A + I - 1) | Nhận xét |
- I gần 0: ổn định (nhiều bên phụ thuộc, nên trừu tượng); I gần 1: không ổn định (dễ đổi, nên cụ thể). D lớn (khoảng từ 0,5 trở lên) cho biết package vừa ổn định vừa cụ thể (khó thay đổi) hoặc vừa không ổn định vừa trừu tượng (trừu tượng thừa); ghi nhận xét, không tự động là vi phạm.

F7. Tổng hợp
- Bảng đếm: | Mức độ | Số phát hiện | Mã RV |
- Thứ tự chạy lại đề xuất: liệt kê bước cần chạy lại theo thứ tự pipeline (bước sớm nhất trước), mỗi bước kèm danh sách RV. Ví dụ: "1. P10: RV-02, RV-05. 2. P12: RV-04, RV-07, RV-09. 3. P13: RV-12."
- Không viết lời khen chung chung; nếu phạm vi không có phát hiện ở một nhóm tiêu chí, ghi "Không phát hiện vi phạm" cho nhóm đó ở F5.

[Target]
Trả lời Đạt/Không đạt cho từng câu, sửa trước khi trả kết quả; mục không đạt còn lại ghi vào "Vấn đề còn mở".
1. Mọi phần tử trong phạm vi đã được xét ở ít nhất một bảng F3, F4 hoặc F5.
2. Mọi cặp phần tử có quan hệ trong phạm vi có mặt ở F3 với mức coupling: cặp có mức khác Data có dòng riêng; cặp Data coupling có thể gộp theo phần tử A và kênh.
3. Mọi lớp trong phạm vi có dòng ở F4 với mức cohesion.
4. Mọi phát hiện có bằng chứng trích từ đầu vào kèm vị trí; không có phát hiện chung chung.
5. Mọi phát hiện có mức độ theo định nghĩa F2 và đề xuất sửa cụ thể có tên hành động.
6. Mọi phát hiện có bước cần sửa; thứ tự chạy lại ở F7 theo thứ tự pipeline.
7. Không có hai phát hiện cho cùng một nguyên nhân gốc; không có hai đề xuất mâu thuẫn nhau.
8. Phát hiện "Cần xác nhận" nêu thông tin còn thiếu để xác nhận.
9. Không đề xuất pattern hoặc trừu tượng mà không nêu vấn đề nó giải quyết (tránh vi phạm KISS, YAGNI ngay trong đề xuất).
10. Bảng phụ thuộc package đầy đủ; vòng phụ thuộc được liệt kê hoặc khẳng định không có.
11. Không sửa trực tiếp artifact đang review; mọi thay đổi nằm trong đề xuất.
12. Đạt Conventions C2, C5, C6.

[Yêu cầu bổ sung]
{{PH:YEU_CAU_BO_SUNG | Hướng dẫn: [TUỲ CHỌN] yêu cầu đặc thù cho lần review; có ưu tiên cao hơn quy tắc mặc định của bước (trừ Conventions C1); không có thì thay cả khối bằng "Không có" | Ví dụ: "Chỉ ghi phát hiện từ mức Trung bình trở lên."; "Bỏ qua tiêu chí DIP với lớp truy cập dữ liệu vì framework đã xử lý."; "Kèm mã nguồn minh hoạ trước và sau cho mỗi đề xuất mức Cao."}}
````

## 5. Ghi chú cho người dùng

- Review quá nhiều phát hiện nhỏ: dùng YEU_CAU_BO_SUNG để lọc mức độ, hoặc giới hạn NHOM_TIEU_CHI.
- Nhiều phát hiện "Cần xác nhận" về stamp coupling hoặc cohesion: P12 thiếu đặc tả method (F3 của P12). Chạy P12 với MUC_CHI_TIET là DAY_DU rồi review lại.
- Sau khi sửa, chạy lại bước ghi ở cột "Bước cần sửa" theo thứ tự F7, sau đó chạy lại X1 với file X1 cũ đính kèm để cập nhật trạng thái.
- Dùng độc lập: điền THIET_KE_DOC_LAP bằng class diagram, mô tả lớp hoặc mã nguồn; AI gán mã EXT- cho phần tử. Với mã nguồn, mức coupling và cohesion được xác định chính xác hơn vì đọc được thân method.
- Nguyên lý là hướng dẫn, không phải luật tuyệt đối: phát hiện có thể được chấp nhận có lý do (ghi Trạng thái "Chấp nhận có lý do"), ví dụ stamp coupling vì hiệu năng.

## 6. Căn cứ

- Stevens W., Myers G., Constantine L., Structured Design, 1974; Yourdon E., Constantine L., Structured Design, 1979: các mức coupling và cohesion.
- Myers G., Composite/Structured Design, 1978: external coupling.
- Meyer B., Object-Oriented Software Construction: tiêu chí module (decomposability, composability, understandability, continuity, protection).
- Martin R. C., Agile Software Development: Principles, Patterns, and Practices; Clean Architecture: SOLID, REP, CCP, CRP, ADP, SDP, SAP và chỉ số I, A, D.
- Larman C., Applying UML and Patterns, 3rd ed.: GRASP.
- Gamma E. và cộng sự, Design Patterns: favor object composition over class inheritance, program to an interface.
- Lieberherr K., Holland I., Assuring Good Style for Object-Oriented Programs, 1989: Law of Demeter.
- Hunt A., Thomas D., The Pragmatic Programmer: DRY.
- Fowler M., Refactoring, 2nd ed.: design smell và refactoring.
- Riel A., Object-Oriented Design Heuristics: god class.
