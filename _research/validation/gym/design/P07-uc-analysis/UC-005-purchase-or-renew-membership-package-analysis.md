# P07 - Phân tích use case UC-005 Mua hoặc gia hạn gói tập - Hệ thống quản lý chuỗi phòng tập VietFit

| Thuộc tính | Giá trị |
|---|---|
| Bước | P07 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md; project-profile.md; P04-uc-specs/UC-005-purchase-or-renew-membership-package.md (phiên bản 1.0; toàn bộ); P01-actors.md (phiên bản 1.0; Mục 2); P02-usecases.md (phiên bản 1.1; dòng UC-005 ở bảng 4a, 4b; các dòng UC có tác nhân thời gian UC-008, UC-013, UC-015, UC-016, UC-022); P03-usecase-model.md (phiên bản 1.0; Mục 1, Mục 2); P05-glossary.md (phiên bản 1.0; các thuật ngữ GL-03, GL-07, GL-09, GL-10, GL-11, GL-12, GL-16, GL-18, GL-19, GL-31, GL-33, GL-37, mục Câu hỏi mở, Đề xuất sửa artifact trước); P06-supplementary-spec.md (phiên bản 1.0; BR-01 đến BR-05, NFR-05, NFR-07, NFR-08, NFR-12, mục Câu hỏi mở); mã Q, ASM quét ở mục Câu hỏi mở, Giả định của P00 đến P06 và các đặc tả P04 (Q-80 lớn nhất, chưa có ASM). File P07 đã có: không có (lần chạy P07 đầu tiên). UC_ID: UC-005 Mua hoặc gia hạn gói tập. LUONG_CAN_VE: Không có. YEU_CAU_BO_SUNG: đề xuất sửa artifact trước của P04, P05, P06 chưa áp dụng và các bước đó không chạy lại; REQ-78, REQ-79 mà đặc tả P04 đề nghị thêm vào cột REQ của P02 chỉ là dữ liệu do UC-026, UC-027 cung cấp; dùng thuật ngữ chuẩn của P05; ghi chú "chưa có BR" ở P05 nay đã có mã BR ở P06 |
| Phạm vi | UC-005 |
| Mã Q, ASM cuối đã cấp | Q-82; ASM: chưa cấp (chế độ NGHIEM_NGAT) |

## F1. Bối cảnh use case

| Thuộc tính | Giá trị |
|---|---|
| Mã và tên UC | UC-005 Mua hoặc gia hạn gói tập (Purchase Or Renew Membership Package) |
| Tác nhân chính (ACT, loại) | ACT-02 Hội viên (Người); ACT-05 Lễ tân (Người) |
| Tác nhân phụ (ACT, loại) | ACT-08 Cổng thanh toán (Hệ thống ngoài); ACT-11 Hệ thống hoá đơn điện tử (Hệ thống ngoài) |
| Include (UC) | Không có |
| Được include bởi (UC) | Không có |
| Extend (UC, điểm mở rộng, điều kiện) | Không có |
| Được extend bởi (UC, điểm mở rộng, điều kiện) | Không có (P03 Mục 2: không có điểm mở rộng) |
| File P07 đã có được dùng làm sổ đăng ký AC | Không có; sổ đăng ký AC rỗng |
| Mốc thời gian phụ thuộc dữ liệu (A2) | Không có message hẹn, hẹn lại hoặc huỷ mốc. UC-008 Nhắc gia hạn gói tập (ACT-13) chạy hằng ngày lúc 8 giờ sáng theo lịch cố định và tự đọc ngày hết hạn của gói, nên đây không phải mốc tính từ dữ liệu của gói (P04 mục 8, F4.2 mục 17 không áp dụng). UC-013, UC-015, UC-016, UC-022 (ACT-14) gắn với lớp nhóm, thông báo nhận chỗ, yêu cầu đặt buổi tập, không gắn với đơn mua hay gói tập do use case này tạo. Thời hạn 15 phút của đơn mua (BR-04) là thời hạn nội bộ, xử lý ở F2 bước 9 và luồng 9a |

## F2. Đặc tả bổ sung

Cột "Mô tả trong đặc tả" chép nguyên văn P04 (kể cả cách gọi "giao dịch thanh toán" ở luồng 10a, từ P05 xếp vào nhóm không dùng); cột bổ sung dùng thuật ngữ chuẩn của P05.

| Bước UC | Thực hiện bởi | Mô tả trong đặc tả | Mô tả bổ sung (hệ thống làm gì bên trong) | Nguồn (BR, GL, REQ) |
|---|---|---|---|---|
| 1 | Hội viên / Lễ tân | Yêu cầu mua hoặc gia hạn gói tập. | Không đổi | REQ-11, REQ-18 |
| 2 | Phần mềm VietFit | Hiển thị các gói tập kèm thời hạn, loại và giá hiện hành (xem Dữ liệu ra 1). | Hệ thống lấy từ mỗi giá gói hiện hành thời hạn (1, 3, 6 hoặc 12 tháng), loại (một chi nhánh hoặc toàn chuỗi), chi nhánh áp dụng (Q-50) và giá hiện hành, rồi hiển thị danh sách các gói. Giá gói do giám đốc chuỗi đặt ở UC-026 nên use case này chỉ đọc. | BR-01, BR-02, GL-10, GL-16, REQ-78, Q-50, Q-82 |
| 3 | Hội viên / Lễ tân | Chọn gói tập cần mua hoặc gia hạn (xem Dữ liệu vào 1). | Không đổi | BR-01, BR-02, REQ-12 |
| 4 | Phần mềm VietFit | Xác định ngày bắt đầu của gói mới (BR-03). | Hệ thống lấy ngày hết hạn của gói cũ mà hội viên gia hạn, rồi đặt ngày bắt đầu của gói mới là ngày ngay sau ngày hết hạn đó khi gói cũ còn hiệu lực. Cách xác định gói cũ chờ Q-56; cách tính ngày hết hạn chờ Q-74. | BR-03, GL-11, GL-16, REQ-17, Q-56, Q-74 |
| 4a | - | Điều kiện: Hội viên mua gói mới, không gia hạn gói nào. Hành động: - (Chờ Q-51) | Đặc tả chưa có hành động nên không phân bổ; ngày bắt đầu của gói mới chờ Q-51. | Q-51 |
| 4b | - | Điều kiện: Hội viên gia hạn khi gói cũ đã hết hạn. Hành động: - (Chờ Q-24) | Đặc tả chưa có hành động nên không phân bổ; ngày bắt đầu chờ Q-24. | Q-24 |
| 4c | - | Điều kiện: Hội viên gia hạn khi gói cũ đang trong thời gian bảo lưu. Hành động: - (Chờ Q-52) | Đặc tả chưa có hành động nên không phân bổ; bảo lưu là khái niệm của UC-006, chỉ được nhắc tới ở đây. | Q-52 |
| 5 | Phần mềm VietFit | Tính số tiền phải trả theo giá gói và chương trình khuyến mãi áp dụng (cách áp dụng khuyến mãi: Q-09). | Hệ thống xác định mức giảm của chương trình khuyến mãi áp dụng cho gói đã chọn, rồi tính số tiền phải trả từ giá của gói trừ mức giảm. Cách áp dụng khuyến mãi chờ Q-09; loại hàng và hiệu lực chờ Q-08, Q-10. | GL-07, GL-10, GL-37, BR-38, REQ-78, REQ-79, Q-08, Q-09, Q-10 |
| 6 | Phần mềm VietFit | Hiển thị tóm tắt đơn mua (xem Dữ liệu ra 2). | Hệ thống hiển thị thời hạn và loại của gói đã chọn, ngày bắt đầu lấy từ bước 4 và số tiền phải trả lấy từ bước 5 để người mua xem lại trước khi xác nhận. | GL-37, Dữ liệu ra 2 |
| 7 | Hội viên / Lễ tân | Xác nhận mua gói tập. | Không đổi | - |
| 8 | Phần mềm VietFit | Tạo đơn mua ở trạng thái chờ thanh toán. | Hệ thống tạo đơn mua gắn người mua, thời hạn và loại của gói đã chọn, ngày bắt đầu và số tiền phải trả, đặt trạng thái chờ thanh toán. Người mua tại quầy có tài khoản hội viên hay không chờ Q-01. | GL-09, GL-19, REQ-13, Q-01 |
| 8a | Lễ tân | Điều kiện: Lễ tân bán gói tại quầy và khách trả bằng tiền mặt. Hành động: Thu tiền mặt của khách và xác nhận đã thu đủ số tiền phải trả. | Không đổi | REQ-19 |
| 8b | Lễ tân | Điều kiện: Lễ tân bán gói tại quầy và khách quẹt thẻ ngân hàng qua máy POS. Hành động: Nhập mã giao dịch in trên hoá đơn POS (xem Dữ liệu vào 2). | Không đổi | REQ-20, REQ-21, GL-31, NFR-08, Q-55 |
| 9 | Phần mềm VietFit | Gửi thông tin đơn mua cho cổng thanh toán và chờ kết quả thanh toán trong thời hạn (BR-04). | Hệ thống chuyển thông tin đơn mua (số tiền phải trả) cho cổng thanh toán và bắt đầu chờ kết quả trong 15 phút theo BR-04. Mốc bắt đầu tính 15 phút chờ Q-25. | BR-04, GL-09, REQ-14, NFR-07, Q-25 |
| 9a | - | Điều kiện: Hết thời hạn (BR-04) mà đơn mua chưa thanh toán thành công. Hành động: Huỷ đơn do hết thời hạn thanh toán. | Control tự nhận sự kiện hết thời hạn mà chính nó đã ghi nhận ở bước 9, rồi chuyển sang 9a1 và 9a2. Hết thời hạn xảy ra trong lúc chờ kết quả giữa bước 9 và bước 10. | BR-04, REQ-15, REQ-16 |
| 9a1 | Phần mềm VietFit | Huỷ đơn mua chưa thanh toán thành công. | Hệ thống chuyển đơn mua chưa thanh toán thành công sang trạng thái đã huỷ, đây là trạng thái cuối của đơn. Xử lý giao dịch đang xử lý tại cổng chờ Q-14. | BR-04, GL-09, Q-14 |
| 9a2 | Phần mềm VietFit | Thông báo cho hội viên đơn mua đã bị huỷ do hết thời hạn thanh toán (kênh thông báo: Q-53). | Hệ thống gửi cho hội viên thông báo đơn mua đã bị huỷ do hết thời hạn thanh toán. Kênh thông báo chờ Q-53. | BR-04, Q-53 |
| 10 | Cổng thanh toán | Thu tiền thanh toán của hội viên và trả về kết quả giao dịch. | Không đổi | REQ-13, REQ-14, NFR-07 |
| 10a | Phần mềm VietFit | Điều kiện: Cổng thanh toán trả về giao dịch không thành công. Hành động: Thông báo cho hội viên giao dịch thanh toán không thành công (kênh thông báo: Q-53). | Hệ thống nhận kết quả giao dịch thu tiền không thành công, không chuyển đơn mua sang đã thanh toán và thông báo cho hội viên. Kết cục sau thông báo chờ Q-13; kênh thông báo chờ Q-53; việc ghi nhận giao dịch không thành công chờ Q-81. | GL-12, REQ-14, Q-13, Q-53, Q-81 |
| 11 | Phần mềm VietFit | Ghi nhận đơn mua đã thanh toán và kích hoạt gói tập. | Hệ thống chuyển đơn mua sang đã thanh toán và ghi nhận giao dịch thu tiền gồm phương thức thu, số tiền, mã giao dịch POS khi có. Hệ thống tạo gói tập mới của hội viên với thời hạn, loại, ngày bắt đầu của đơn, tính ngày hết hạn từ ngày bắt đầu và thời hạn, đặt trạng thái đã kích hoạt. | GL-09, GL-12, GL-16, REQ-91, Q-54, Q-74, Q-75 |
| 12 | Phần mềm VietFit | Gửi dữ liệu giao dịch thu tiền cho hệ thống hoá đơn điện tử (BR-05). | Hệ thống lấy dữ liệu của giao dịch thu tiền vừa ghi nhận và gửi sang hệ thống hoá đơn điện tử. Các trường dữ liệu chờ Q-39; việc lập hoá đơn nằm ngoài phạm vi. | BR-05, GL-12, GL-18, REQ-91, REQ-92, NFR-05, NFR-12, Q-39 |
| 12a | - | Điều kiện: Hệ thống hoá đơn điện tử không nhận hoặc từ chối dữ liệu giao dịch. Hành động: - (Chờ Q-54) | Đặc tả chưa có hành động nên không phân bổ; thứ tự bước 11, bước 12 và cách xử lý chờ Q-54. | Q-54 |
| 13 | Phần mềm VietFit | Hiển thị gói tập đã kích hoạt cho hội viên hoặc lễ tân thực hiện giao dịch (xem Dữ liệu ra 3). | Hệ thống hiển thị thời hạn và loại, ngày bắt đầu và trạng thái của gói tập vừa kích hoạt cho tác nhân đang thao tác. | GL-16, Dữ liệu ra 3 |

## F3. Tìm lớp phân tích

### F3.1 Bảng boundary

| Tác nhân (ACT) | Loại tác nhân | Boundary | Loại boundary | Mới hoặc tái dùng (AC, UC nguồn) | Lý do |
|---|---|---|---|---|---|
| ACT-02 Hội viên | Người | PurchaseOrRenewPackageUI (AC-B-PurchaseOrRenewPackageUI) | Giao diện người dùng | Mới | Hội viên mua hoặc gia hạn trên ứng dụng di động. Tên theo tương tác của use case, hậu tố UI theo HAU_TO_TEN_LOP. |
| ACT-05 Lễ tân | Người | SellPackageUI (AC-B-SellPackageUI) | Giao diện người dùng | Mới | Lễ tân bán gói tại quầy trên ứng dụng web. Hai tác nhân chính dùng chung luồng nhưng mỗi cặp tác nhân và use case có một boundary. |
| ACT-08 Cổng thanh toán | Hệ thống ngoài | PaymentGateway (AC-B-PaymentGateway) | Giao diện hệ thống | Mới | Đặt tên theo hệ thống ngoài, hậu tố Gateway theo HAU_TO_TEN_LOP, để use case khác cùng giao tiếp cổng thanh toán dùng lại mã này. Không trùng tên entity nào. |
| ACT-11 Hệ thống hoá đơn điện tử | Hệ thống ngoài | EInvoiceGateway (AC-B-EInvoiceGateway) | Giao diện hệ thống | Mới | UC-007, UC-017, UC-019 cũng gửi dữ liệu giao dịch thu tiền sang hệ thống này (P02 bảng 4a), P07 của chúng phải dùng lại mã này. Không trùng tên entity nào. |

### F3.2 Bảng lọc danh từ

| STT | Danh từ hoặc cụm danh từ | Vị trí (bước UC, mục dữ liệu, BR) | Kết luận | Lý do |
|---|---|---|---|---|
| 1 | Hội viên (tác nhân) | Bước 1, 3, 7, 13 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-02; tương tác qua AC-B-PurchaseOrRenewPackageUI. |
| 2 | Lễ tân | Bước 1, 3, 7, 8a, 8b, 13 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-05; tương tác qua AC-B-SellPackageUI. |
| 3 | Khách (đến quầy) | Sự kiện kích hoạt, luồng 8a, 8b | Loại - trùng hoặc đồng nghĩa với Member | Khách mua gói tại quầy là người mua gói; có phải hội viên hay không chờ Q-01 (GL-19). |
| 4 | Người mua gói | Dữ liệu vào 1 trường 5 | Loại - trùng hoặc đồng nghĩa với Member | Cùng khái niệm với dòng Khách; chờ Q-01. |
| 5 | Hội viên (hồ sơ người sở hữu gói, người mua của đơn) | Bước 8, 11 | Entity AC-E-Member | Biểu diễn thông tin về hội viên, không phải bản thân tác nhân ACT-02. Hệ thống lưu hồ sơ và quan hệ sở hữu gói vượt quá một lần thực hiện use case (GL-19). |
| 6 | Phần mềm VietFit, hệ thống | Bước 2, 4, 5, 6, 8, 9, 11, 12, 13 | Loại - mơ hồ | Chủ thể của use case, không phải một lớp; trách nhiệm được phân bổ cho các lớp BCE ở F4. |
| 7 | Gói tập (gói mới, gói đã kích hoạt) | Bước 11, 13; Hậu điều kiện; BR-01, BR-02, BR-03 | Entity AC-E-MembershipPackage | Quyền vào tập có thời hạn, ngày bắt đầu, ngày hết hạn, trạng thái, tồn tại lâu hơn một lần thực hiện (GL-16). |
| 8 | Gói cũ, Gói đang có cần gia hạn | Bước 4; BR-03; Dữ liệu vào 1 trường 4 | Loại - trùng hoặc đồng nghĩa với MembershipPackage | Gói cũ là một đối tượng MembershipPackage (lifeline oldPackage); cách xác định gói cũ chờ Q-56 (GL-11). |
| 9 | Gói tập được bán (các gói kèm thời hạn, loại, giá ở bước 2 và 3) | Bước 2, 3 | Loại - trùng hoặc đồng nghĩa với PackagePrice | Mỗi gói được bán là một giá gói gắn thời hạn và loại (GL-10); có cần danh mục gói riêng hay không chờ Q-82. |
| 10 | Giá gói, giá hiện hành | Bước 2, 5; Dữ liệu ra 1 trường 4 | Entity AC-E-PackagePrice | Có định danh nghiệp vụ (thời hạn, loại) và hiệu lực riêng, do UC-026 quản lý, use case này đọc (GL-10, REQ-78). |
| 11 | Danh sách các gói | Bước 2 | Loại - cấu trúc cài đặt | Kết quả truy vấn trên các giá gói, không có định danh nghiệp vụ và vòng đời riêng. |
| 12 | Thời hạn gói (số tháng) | Bước 2, 3; BR-01; Dữ liệu vào 1 trường 1 | Loại - thuộc tính của MembershipPackage | durationMonths; thuộc tính tương ứng ở PackagePrice và PackageOrder. |
| 13 | 1, 3, 6 hoặc 12 tháng | BR-01 | Loại - tham số của quy tắc BR-01 | Giá trị hợp lệ của thời hạn. |
| 14 | Loại gói | Bước 2, 3; BR-02; Dữ liệu vào 1 trường 2 | Loại - thuộc tính của MembershipPackage | packageType. |
| 15 | Một chi nhánh, toàn chuỗi | BR-02 | Loại - tham số của quy tắc BR-02 | Hai giá trị hợp lệ của loại gói. |
| 16 | Chi nhánh, chi nhánh áp dụng | Dữ liệu vào 1 trường 3; Dữ liệu ra 1 trường 3; BR-02 | Loại - thuộc tính của MembershipPackage | appliedBranch, chỉ lưu tham chiếu; use case này không đọc, ghi hay kiểm tra thông tin của chi nhánh. Cách xác định chi nhánh chờ Q-50; người tạo danh mục chi nhánh chờ Q-03 (GL-03). |
| 17 | Chương trình khuyến mãi, khuyến mãi | Bước 5; Dữ liệu ra 1 trường 4 | Entity AC-E-Promotion | Có khoảng ngày và mức giảm riêng, do UC-027 quản lý, use case này đọc để xác định mức giảm (GL-07, BR-38). |
| 18 | Ngày bắt đầu | Bước 4, 6, 13; BR-03; Dữ liệu ra 2 trường 2, Dữ liệu ra 3 trường 2 | Loại - thuộc tính của MembershipPackage | startDate; PackageOrder giữ bản sao startDate của gói sẽ tạo. |
| 19 | Ngày hết hạn | Bước 4; BR-03 | Loại - thuộc tính của MembershipPackage | expiryDate; cách tính ngày hết hạn từ ngày bắt đầu chờ Q-74. |
| 20 | Số tiền phải trả | Bước 5, 6; Dữ liệu ra 2 trường 3 | Loại - thuộc tính của PackageOrder | amountDue (GL-37); tính ở bước 5, lưu vào đơn khi tạo đơn ở bước 8. |
| 21 | Tóm tắt đơn mua | Bước 6; Dữ liệu ra 2 | Loại - dữ liệu trao đổi qua boundary AC-B-PurchaseOrRenewPackageUI | Chỉ để hiển thị, không lưu. |
| 22 | Đơn mua, đơn | Bước 8, 9, 11; BR-04 | Entity AC-E-PackageOrder | Chứng từ có trạng thái và vòng đời (chờ thanh toán, đã thanh toán, đã huỷ), tồn tại lâu hơn một lần thực hiện (GL-09). |
| 23 | Thông tin đơn mua | Bước 9 | Loại - trùng hoặc đồng nghĩa với PackageOrder | Dữ liệu của đơn mua gửi cho cổng thanh toán. |
| 24 | Trạng thái đơn (chờ thanh toán, đã thanh toán, đã huỷ) | Bước 8, 9a1, 11; Hậu điều kiện | Loại - thuộc tính của PackageOrder | status. |
| 25 | Trạng thái gói (đã kích hoạt) | Bước 11, 13; Dữ liệu ra 3 trường 3 | Loại - thuộc tính của MembershipPackage | status; quan hệ giữa các trạng thái của gói chờ Q-75. |
| 26 | Thời hạn thanh toán, 15 phút | Bước 9, 9a; BR-04 | Loại - tham số của quy tắc BR-04 | Hằng số của BR-04; không là tác nhân và không là use case. |
| 27 | Cổng thanh toán | Bước 9, 10 | Loại - là tác nhân hoặc ngoài phạm vi | ACT-08; tương tác qua AC-B-PaymentGateway. |
| 28 | Kết quả thanh toán, kết quả giao dịch | Bước 9, 10, 10a | Loại - dữ liệu trao đổi qua boundary AC-B-PaymentGateway | Không lưu riêng; việc ghi nhận kết quả không thành công chờ Q-81. |
| 29 | Giao dịch thu tiền | Bước 12; BR-05; Hậu điều kiện | Entity AC-E-PaymentTransaction | Có dữ liệu riêng (phương thức thu, số tiền, mã giao dịch POS) cần giữ để gửi hoá đơn điện tử và có thể gửi lại (GL-12, Q-54). |
| 30 | Giao dịch, giao dịch thanh toán | Bước 10, 10a | Loại - trùng hoặc đồng nghĩa với PaymentTransaction | "giao dịch thanh toán" là từ không dùng của Giao dịch thu tiền (GL-12). |
| 31 | Tiền mặt, thẻ ngân hàng | Luồng 8a, 8b | Loại - thuộc tính của PaymentTransaction | paymentMethod. |
| 32 | Máy POS | Luồng 8b | Loại - là tác nhân hoặc ngoài phạm vi | Thiết bị của ngân hàng, không kết nối phần mềm, không là tác nhân (GL-33). |
| 33 | Hoá đơn POS | Luồng 8b | Loại - là tác nhân hoặc ngoài phạm vi | Chứng từ in của máy POS, ngoài phần mềm (GL-33); khác hoá đơn điện tử (GL-18). |
| 34 | Mã giao dịch POS | Luồng 8b; Dữ liệu vào 2 trường 1 | Loại - thuộc tính của PaymentTransaction | posTransactionCode (GL-31); quy tắc định dạng chờ Q-55. |
| 35 | Hệ thống hoá đơn điện tử | Bước 12, 12a | Loại - là tác nhân hoặc ngoài phạm vi | ACT-11; tương tác qua AC-B-EInvoiceGateway. |
| 36 | Hoá đơn điện tử | BR-05; Hậu điều kiện | Loại - là tác nhân hoặc ngoài phạm vi | Do hệ thống ngoài xuất; việc lập, điều chỉnh, huỷ nằm ngoài phạm vi (project-profile.md mục 4, NFR-05). |
| 37 | Dữ liệu giao dịch thu tiền | Bước 12 | Loại - dữ liệu trao đổi qua boundary AC-B-EInvoiceGateway | Lấy từ PaymentTransaction; các trường chờ Q-39. |
| 38 | Thông báo (đơn bị huỷ, giao dịch không thành công) | Luồng 9a2, 10a | Loại - dữ liệu trao đổi qua boundary AC-B-PurchaseOrRenewPackageUI | Nội dung gửi tới hội viên, không lưu; kênh thông báo chờ Q-53. |
| 39 | Bảo lưu, gói đang bảo lưu | Luồng 4c | Loại - không tham gia hành vi của use case này (khái niệm của UC-006) | Chỉ được nhắc tới ở điều kiện của 4c, nội dung chờ Q-52. |
| 40 | Phiên làm việc | Tiền điều kiện | Loại - không tham gia hành vi của use case này (khái niệm của UC-004) | Chỉ là tiền điều kiện, không được đọc, ghi hay kiểm tra ở use case này. |
| 41 | Quầy | Sự kiện kích hoạt; luồng 8a, 8b | Loại - là tác nhân hoặc ngoài phạm vi | Nơi lễ tân làm việc, không là khái niệm dữ liệu. |
| 42 | Gia hạn, mua | Bước 1, 3; Tên use case | Loại - thao tác hoặc sự kiện | Hình thức mua gói (GL-11), không phải đối tượng lưu trữ. |

### F3.3 Bảng control

| Control | Use case điều phối | Mới hoặc tái dùng | Lý do (hoặc lý do không có control) |
|---|---|---|---|
| PurchaseOrRenewPackageHandler (AC-C-PurchaseOrRenewPackageHandler) | UC-005 Mua hoặc gia hạn gói tập | Mới | Một control điều phối luồng của cả hai tác nhân chính; hậu tố Handler theo HAU_TO_TEN_LOP. Không tách control phụ vì không có phần điều phối lớn dùng lại ở nhiều use case. |

### F3.4 Bảng lớp phân tích

| AC | Stereotype | Tên | Trách nhiệm | Thuộc tính chính | Bước UC nguồn | Loại boundary | Mới hoặc tái dùng | GL |
|---|---|---|---|---|---|---|---|---|
| AC-B-PurchaseOrRenewPackageUI | boundary | PurchaseOrRenewPackageUI | // requestPurchaseOrRenewal: nhận yêu cầu mua hoặc gia hạn của hội viên<br>// showPackageOptions: hiển thị các gói tập kèm thời hạn, loại, giá hiện hành<br>// selectPackage: nhận gói đã chọn, kiểm tra hình thức dữ liệu nhập (thời hạn, loại bắt buộc)<br>// showOrderSummary: hiển thị tóm tắt đơn mua (gói, ngày bắt đầu, số tiền phải trả)<br>// confirmPurchase: nhận xác nhận mua của hội viên<br>// showOrderCancelledNotice: thông báo cho hội viên đơn mua bị huỷ do hết thời hạn thanh toán (kênh: Q-53)<br>// showPaymentFailedNotice: thông báo cho hội viên giao dịch thu tiền không thành công (kênh: Q-53)<br>// showActivatedPackage: hiển thị gói tập đã kích hoạt | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew | 1, 2, 3, 6, 7, 9a2, 10a, 13 | Giao diện người dùng | Mới | GL-16 |
| AC-B-SellPackageUI | boundary | SellPackageUI | // requestPackageSale: nhận yêu cầu bán gói tập của lễ tân<br>// showPackageOptions: hiển thị các gói tập kèm thời hạn, loại, giá hiện hành<br>// selectPackage: nhận gói đã chọn và người mua gói, kiểm tra hình thức dữ liệu nhập<br>// showOrderSummary: hiển thị tóm tắt đơn mua cho lễ tân<br>// confirmSale: nhận xác nhận bán của lễ tân<br>// confirmCashCollected: nhận xác nhận lễ tân đã thu đủ tiền mặt (8a)<br>// enterPosTransactionCode: nhận mã giao dịch POS, kiểm tra bắt buộc nhập (8b)<br>// showActivatedPackage: hiển thị gói tập đã kích hoạt cho lễ tân | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew<br>buyer<br>posTransactionCode | 1, 2, 3, 6, 7, 8a, 8b, 13 | Giao diện người dùng | Mới | GL-31 |
| AC-B-PaymentGateway | boundary | PaymentGateway | // requestPayment: chuyển thông tin đơn mua cho cổng thanh toán<br>// returnPaymentResult: nhận kết quả giao dịch từ cổng thanh toán và chuyển cho control | - | 9, 10 | Giao diện hệ thống | Mới | - |
| AC-B-EInvoiceGateway | boundary | EInvoiceGateway | // sendTransactionData: chuyển dữ liệu giao dịch thu tiền cho hệ thống hoá đơn điện tử | - | 12 | Giao diện hệ thống | Mới | GL-18 |
| AC-C-PurchaseOrRenewPackageHandler | control | PurchaseOrRenewPackageHandler | // startPurchase: điều phối hiển thị các gói tập (bước 1-2)<br>// processPackageSelection: điều phối xác định ngày bắt đầu, tính số tiền phải trả, trình tóm tắt đơn mua (bước 3-6)<br>// placeOrder: tạo đơn mua và gửi thông tin đơn cho cổng thanh toán (bước 7-9)<br>// startWaitingForPayment: ghi nhận bắt đầu chờ kết quả thanh toán trong thời hạn BR-04<br>// handlePaymentTimeout: nhận sự kiện hết thời hạn BR-04, huỷ đơn và báo hội viên (9a)<br>// stopWaitingForPayment: dừng chờ thời hạn BR-04 khi đã nhận kết quả<br>// handlePaymentResult: xử lý kết quả giao dịch: thông báo khi không thành công, hoặc ghi nhận đã thanh toán, kích hoạt gói, gửi hoá đơn điện tử, hiển thị gói (bước 10-13, 10a)<br>// confirmCashPayment: xử lý xác nhận đã thu tiền mặt tại quầy rồi tiếp tục bước 11 (8a)<br>// confirmPosPayment: xử lý mã giao dịch POS đã nhập rồi tiếp tục bước 11 (8b) | - | 1-13, 8a, 8b, 9a, 10a | - | Mới | - |
| AC-E-MembershipPackage | entity | MembershipPackage | // calculateRenewalStartDate: xác định ngày bắt đầu của gói mới từ ngày hết hạn của gói cũ (BR-03)<br>// initializePackage: nhận thời hạn, loại, ngày bắt đầu; tính ngày hết hạn (Q-74) và đặt trạng thái đã kích hoạt | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản, Q-50)<br>startDate (Ngày)<br>expiryDate (Ngày)<br>status (Trạng thái) | 4, 11 | - | Mới | GL-16 |
| AC-E-Member | entity | Member | // activatePackage: tạo gói tập mới và gắn cho hội viên sở hữu | - | 11 | - | Mới - chủ sở hữu UC-003 | GL-19 |
| AC-E-PackageOrder | entity | PackageOrder | // createOrder: nhận người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả; đặt trạng thái chờ thanh toán<br>// cancelUnpaidOrder: chuyển đơn chưa thanh toán thành công sang trạng thái đã huỷ khi hết thời hạn BR-04<br>// recordPayment: chuyển đơn sang trạng thái đã thanh toán và ghi nhận giao dịch thu tiền | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản, Q-50)<br>startDate (Ngày)<br>amountDue (Số tiền)<br>status (Trạng thái) | 8, 9a1, 11 | - | Mới | GL-09 |
| AC-E-PaymentTransaction | entity | PaymentTransaction | // createTransaction: nhận phương thức thu, số tiền, mã giao dịch POS (nếu có)<br>// prepareInvoiceData: cung cấp dữ liệu giao dịch thu tiền để gửi hoá đơn điện tử (trường dữ liệu: Q-39) | paymentMethod (Trạng thái)<br>amount (Số tiền)<br>posTransactionCode (Văn bản) | 11, 12 | - | Mới | GL-12, GL-31 |
| AC-E-PackagePrice | entity | PackagePrice | // getPriceInfo: cung cấp thời hạn, loại, chi nhánh áp dụng, giá hiện hành để hiển thị<br>// calculateAmountDue: tính số tiền phải trả từ giá gói và mức giảm áp dụng (Q-09) | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản, Q-50)<br>price (Số tiền) | 2, 5 | - | Mới - chủ sở hữu UC-026 | GL-10, GL-37 |
| AC-E-Promotion | entity | Promotion | // determineApplicableDiscount: xác định mức giảm áp dụng cho gói đã chọn (cách áp dụng: Q-09; loại hàng: Q-08) | validFrom (Ngày)<br>validTo (Ngày)<br>discountRate (Số lượng, tối đa 20% theo BR-38) | 5 | - | Mới - chủ sở hữu UC-027 | GL-07 |

## F4. Phân bổ hành vi

| Bước UC | Trách nhiệm | Lớp nhận (AC) | Nguyên tắc | Lý do khi có lựa chọn khác |
|---|---|---|---|---|
| 1 | // requestPurchaseOrRenewal | AC-B-PurchaseOrRenewPackageUI | Giao tiếp tác nhân | - |
| 1 | // requestPackageSale | AC-B-SellPackageUI | Giao tiếp tác nhân | - |
| 1 | // startPurchase | AC-C-PurchaseOrRenewPackageHandler | Controller | - |
| 2 | // getPriceInfo | AC-E-PackagePrice | Information Expert | Thời hạn, loại, giá hiện hành nằm ở giá gói. Đặc tả, BR, glossary không có đối tượng toàn thể nắm tập giá gói nên control lặp và gửi message tới từng giá gói (A6). |
| 2 | // showPackageOptions | AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI | Giao tiếp tác nhân | - |
| 3 | // selectPackage | AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI | Giao tiếp tác nhân | Boundary chỉ kiểm tra hình thức dữ liệu nhập (thời hạn, loại bắt buộc). |
| 3 | // processPackageSelection | AC-C-PurchaseOrRenewPackageHandler | Controller | - |
| 4 | // calculateRenewalStartDate | AC-E-MembershipPackage | Information Expert | Ngày hết hạn nằm ở gói cũ. Đặt phép tính ở control sẽ làm control nắm quy tắc BR-03 thuộc dữ liệu của gói. |
| 5 | // determineApplicableDiscount | AC-E-Promotion | Information Expert | Khoảng ngày và mức giảm nằm ở chương trình khuyến mãi; control lặp trên tập chương trình (A6). |
| 5 | // calculateAmountDue | AC-E-PackagePrice | Information Expert | Dữ liệu nằm ở hai lớp: giá ở PackagePrice, mức giảm ở Promotion, và đặc tả chưa nêu quan hệ cấu trúc giữa hai lớp (Q-08, Q-09, Q-10). Chọn giao cho PackagePrice nhận mức giảm làm tham số: không thêm quan hệ PackagePrice - Promotion (coupling thấp hơn) và không đặt phép tính ở control (cohesion cao hơn). |
| 6 | // showOrderSummary | AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI | Giao tiếp tác nhân | - |
| 7 | // confirmPurchase | AC-B-PurchaseOrRenewPackageUI | Giao tiếp tác nhân | - |
| 7 | // confirmSale | AC-B-SellPackageUI | Giao tiếp tác nhân | - |
| 7 | // placeOrder | AC-C-PurchaseOrRenewPackageHandler | Controller | - |
| 8 | // createOrder | AC-E-PackageOrder | Creator | Control giữ toàn bộ dữ liệu khởi tạo (người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả) sau các bước 3 đến 6 nên control tạo đơn. Phương án Member tạo đơn buộc Member nhận bốn tham số của đơn, coupling cao hơn. |
| 8a | // confirmCashCollected | AC-B-SellPackageUI | Giao tiếp tác nhân | - |
| 8a | // confirmCashPayment | AC-C-PurchaseOrRenewPackageHandler | Controller | - |
| 8b | // enterPosTransactionCode | AC-B-SellPackageUI | Giao tiếp tác nhân | Boundary chỉ kiểm tra mã bắt buộc nhập; quy tắc mã chờ Q-55. |
| 8b | // confirmPosPayment | AC-C-PurchaseOrRenewPackageHandler | Controller | - |
| 9 | // requestPayment | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 9 | // startWaitingForPayment | AC-C-PurchaseOrRenewPackageHandler | Controller | Thời hạn nội bộ BR-04 do control ghi nhận bằng message tự gọi (A2). |
| 9a | // handlePaymentTimeout | AC-C-PurchaseOrRenewPackageHandler | Controller | Nhận sự kiện hết thời hạn bằng message tự gọi after(BR-04). |
| 9a1 | // cancelUnpaidOrder | AC-E-PackageOrder | Information Expert | Trạng thái đơn nằm ở đơn. |
| 9a2 | // showOrderCancelledNotice | AC-B-PurchaseOrRenewPackageUI | Giao tiếp tác nhân | Kênh thông báo chờ Q-53; tạm gửi tới boundary của hội viên. |
| 10 | // returnPaymentResult | AC-B-PaymentGateway | Giao tiếp tác nhân | - |
| 10 | // handlePaymentResult | AC-C-PurchaseOrRenewPackageHandler | Controller | - |
| 10 | // stopWaitingForPayment | AC-C-PurchaseOrRenewPackageHandler | Controller | - |
| 10a | // showPaymentFailedNotice | AC-B-PurchaseOrRenewPackageUI | Giao tiếp tác nhân | Kênh thông báo chờ Q-53; kết cục chờ Q-13. |
| 11 | // recordPayment | AC-E-PackageOrder | Information Expert | Trạng thái đơn nằm ở đơn. |
| 11 | // createTransaction | AC-E-PaymentTransaction | Creator | Đơn mua ghi nhận thanh toán của chính nó, có phương thức thu và số tiền; đơn và giao dịch có quan hệ cấu trúc. |
| 11 | // activatePackage | AC-E-Member | Creator | Hội viên là lớp ghi nhận các gói tập thuộc về mình (GL-16, GL-19). Phương án control hoặc PackageOrder tạo gói bỏ qua quan hệ sở hữu gói - hội viên. |
| 11 | // initializePackage | AC-E-MembershipPackage | Information Expert | Ngày hết hạn và trạng thái là dữ liệu của gói. |
| 12 | // prepareInvoiceData | AC-E-PaymentTransaction | Information Expert | Dữ liệu giao dịch thu tiền nằm ở giao dịch. |
| 12 | // sendTransactionData | AC-B-EInvoiceGateway | Giao tiếp tác nhân | - |
| 13 | // showActivatedPackage | AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI | Giao tiếp tác nhân | - |

## F5. Sequence diagram phân tích

File diagrams/P07-sequence-UC-005.drawio gồm 4 trang: SD1a, SD1b, SD1c cho luồng chính của Hội viên (luồng chính vượt ngưỡng nên tách theo đoạn bước), SD2 cho biến thể Lễ tân. Luồng 9a và 10a (kết thúc use case) vẽ bằng break ở mức ngoài cùng của SD1b; luồng 8a, 8b vẽ bằng alt trong SD2. Luồng 4a, 4b, 4c, 12a không có hành động trong đặc tả nên không có message. Biến thể Lễ tân dùng cùng STT với luồng chính kèm hậu tố r ở số thứ nhất (1r, 1r.1, 2r...); các message do control khởi phát sau điểm hợp của alt (bước 11 đến 13) đánh số tiếp 6r, 7r, 8r, 9r, 10r.

### SD1a - Luồng chính, bước 1-6 (Hội viên)

a) Sơ đồ SD1a: Luồng chính, bước 1 đến 6, tác nhân chính Hội viên. Trang "SD1a" trong diagrams/P07-sequence-UC-005.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1a-L1 | Actor | Hội viên (ACT-02) | «actor» | - | Tác nhân | 40 | 40 | 120 | 660 |
| SD1a-L2 | Lifeline | :PurchaseOrRenewPackageUI | «boundary» | - | Lớp AC-B-PurchaseOrRenewPackageUI | 200 | 40 | 120 | 660 |
| SD1a-L3 | Lifeline | :PurchaseOrRenewPackageHandler | «control» | - | Lớp AC-C-PurchaseOrRenewPackageHandler | 360 | 40 | 120 | 660 |
| SD1a-L4 | Lifeline | oldPackage:MembershipPackage | «entity» | - | Lớp AC-E-MembershipPackage | 520 | 40 | 120 | 660 |
| SD1a-L5 | Lifeline | :PackagePrice | «entity» | - | Lớp AC-E-PackagePrice | 680 | 40 | 120 | 660 |
| SD1a-L6 | Lifeline | :Promotion | «entity» | - | Lớp AC-E-Promotion | 840 | 40 | 120 | 660 |
| SD1a-F1 | Fragment | loop [mỗi giá gói hiện hành] | - | - | Control lặp vì không có đối tượng toàn thể nắm tập giá gói (A6) | 340 | 170 | 480 | 90 |
| SD1a-F2 | Fragment | loop [mỗi chương trình khuyến mãi đang đặt] | - | - | Control lặp vì không có đối tượng toàn thể nắm tập chương trình khuyến mãi (A6) | 340 | 450 | 640 | 90 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1a-M01 | 1 | SD1a-L1 | SD1a-L2 | // requestPurchaseOrRenewal | Đồng bộ | - | 1 |
| SD1a-M02 | 1.1 | SD1a-L2 | SD1a-L3 | // startPurchase | Đồng bộ | - | 1 |
| SD1a-M03 | 1.1.1 | SD1a-L3 | SD1a-L5 | // getPriceInfo | Đồng bộ | SD1a-F1 | 2 |
| SD1a-M04 | 1.1.1 (trả về) | SD1a-L5 | SD1a-L3 | thời hạn, loại, chi nhánh áp dụng, giá hiện hành | Trả về | SD1a-F1 | 2 |
| SD1a-M05 | 1.1.2 | SD1a-L3 | SD1a-L2 | // showPackageOptions (các gói tập kèm thời hạn, loại, giá hiện hành) | Đồng bộ | - | 2 |
| SD1a-M06 | 2 | SD1a-L1 | SD1a-L2 | // selectPackage (thời hạn, loại, chi nhánh áp dụng, gói cần gia hạn) | Đồng bộ | - | 3 |
| SD1a-M07 | 2.1 | SD1a-L2 | SD1a-L3 | // processPackageSelection (gói đã chọn) | Đồng bộ | - | 3 |
| SD1a-M08 | 2.1.1 | SD1a-L3 | SD1a-L4 | // calculateRenewalStartDate | Đồng bộ | - | 4 |
| SD1a-M09 | 2.1.1 (trả về) | SD1a-L4 | SD1a-L3 | ngày bắt đầu của gói mới | Trả về | - | 4 |
| SD1a-M10 | 2.1.2 | SD1a-L3 | SD1a-L6 | // determineApplicableDiscount (gói đã chọn) | Đồng bộ | SD1a-F2 | 5 |
| SD1a-M11 | 2.1.2 (trả về) | SD1a-L6 | SD1a-L3 | mức giảm áp dụng | Trả về | SD1a-F2 | 5 |
| SD1a-M12 | 2.1.3 | SD1a-L3 | SD1a-L5 | // calculateAmountDue (mức giảm áp dụng) | Đồng bộ | - | 5 |
| SD1a-M13 | 2.1.3 (trả về) | SD1a-L5 | SD1a-L3 | số tiền phải trả | Trả về | - | 5 |
| SD1a-M14 | 2.1.4 | SD1a-L3 | SD1a-L2 | // showOrderSummary (gói đã chọn, ngày bắt đầu, số tiền phải trả) | Đồng bộ | - | 6 |

### SD1b - Luồng chính bước 7-10, luồng 9a, 10a (Hội viên)

a) Sơ đồ SD1b: Luồng chính bước 7 đến 10 và các luồng 9a, 10a, tác nhân chính Hội viên. Trang "SD1b" trong diagrams/P07-sequence-UC-005.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1b-L1 | Actor | Hội viên (ACT-02) | «actor» | - | Tác nhân | 40 | 40 | 120 | 620 |
| SD1b-L2 | Lifeline | :PurchaseOrRenewPackageUI | «boundary» | - | Lớp AC-B-PurchaseOrRenewPackageUI | 200 | 40 | 120 | 620 |
| SD1b-L3 | Lifeline | :PurchaseOrRenewPackageHandler | «control» | - | Lớp AC-C-PurchaseOrRenewPackageHandler | 360 | 40 | 120 | 620 |
| SD1b-L4 | Lifeline | :PackageOrder | «entity» | - | Đối tượng được tạo bởi message loại Tạo; đỉnh lifeline ngang y của message; lớp AC-E-PackageOrder | 520 | 200 | 120 | 460 |
| SD1b-L5 | Lifeline | :PaymentGateway | «boundary» | - | Lớp AC-B-PaymentGateway | 680 | 40 | 120 | 620 |
| SD1b-L6 | Actor | Cổng thanh toán (ACT-08) | «actor» | - | Tác nhân | 840 | 40 | 120 | 620 |
| SD1b-F1 | Fragment | ref SD1a - Luồng chính, bước 1-6 | - | - | - | 180 | 80 | 320 | 30 |
| SD1b-F2 | Fragment | break [hết thời hạn (BR-04) mà đơn mua chưa thanh toán thành công] | - | - | Luồng 9a, kết thúc use case (thất bại). Mốc bắt đầu tính 15 phút chờ Q-25 | 180 | 330 | 480 | 130 |
| SD1b-F3 | Fragment | break [giao dịch không thành công (10a)] | - | - | Luồng 10a. Kết cục sau thông báo chờ Q-13; kênh thông báo chờ Q-53 | 180 | 570 | 320 | 50 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1b-M01 | 3 | SD1b-L1 | SD1b-L2 | // confirmPurchase | Đồng bộ | - | 7 |
| SD1b-M02 | 3.1 | SD1b-L2 | SD1b-L3 | // placeOrder | Đồng bộ | - | 7 |
| SD1b-M03 | 3.1.1 | SD1b-L3 | SD1b-L4 | «create» // createOrder (người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả) | Tạo | - | 8 |
| SD1b-M04 | 3.1.2 | SD1b-L3 | SD1b-L5 | // requestPayment (đơn mua) | Đồng bộ | - | 9 |
| SD1b-M05 | 3.1.2.1 | SD1b-L5 | SD1b-L6 | // collectPayment (đơn mua) | Đồng bộ | - | 10 |
| SD1b-M06 | 3.1.3 | SD1b-L3 | SD1b-L3 | // startWaitingForPayment (BR-04) | Tự gọi | - | 9 |
| SD1b-M07 | 3.1.4 | SD1b-L3 | SD1b-L3 | // after(BR-04) handlePaymentTimeout | Tự gọi | SD1b-F2 | 9a |
| SD1b-M08 | 3.1.4.1 | SD1b-L3 | SD1b-L4 | // cancelUnpaidOrder | Đồng bộ | SD1b-F2 | 9a1 |
| SD1b-M09 | 3.1.4.2 | SD1b-L3 | SD1b-L2 | // showOrderCancelledNotice (kênh thông báo: Q-53) | Đồng bộ | SD1b-F2 | 9a2 |
| SD1b-M10 | 4 | SD1b-L6 | SD1b-L5 | // returnPaymentResult (kết quả giao dịch) | Đồng bộ | - | 10 |
| SD1b-M11 | 4.1 | SD1b-L5 | SD1b-L3 | // handlePaymentResult (kết quả giao dịch) | Đồng bộ | - | 10 |
| SD1b-M12 | 4.1.1 | SD1b-L3 | SD1b-L3 | // stopWaitingForPayment (BR-04) | Tự gọi | - | 10 |
| SD1b-M13 | 4.1.2 | SD1b-L3 | SD1b-L2 | // showPaymentFailedNotice (kênh thông báo: Q-53; kết cục sau thông báo: Q-13) | Đồng bộ | SD1b-F3 | 10a |

### SD1c - Luồng chính, bước 11-13 (Hội viên)

a) Sơ đồ SD1c: Luồng chính bước 11 đến 13, tác nhân chính Hội viên. Trang "SD1c" trong diagrams/P07-sequence-UC-005.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD1c-L1 | Lifeline | :PurchaseOrRenewPackageUI | «boundary» | - | Lớp AC-B-PurchaseOrRenewPackageUI | 40 | 40 | 120 | 460 |
| SD1c-L2 | Lifeline | :PurchaseOrRenewPackageHandler | «control» | - | Lớp AC-C-PurchaseOrRenewPackageHandler | 200 | 40 | 120 | 460 |
| SD1c-L3 | Lifeline | :PackageOrder | «entity» | - | Lớp AC-E-PackageOrder | 360 | 40 | 120 | 460 |
| SD1c-L4 | Lifeline | :PaymentTransaction | «entity» | - | Đối tượng được tạo bởi message loại Tạo; đỉnh lifeline ngang y của message; lớp AC-E-PaymentTransaction | 520 | 160 | 120 | 340 |
| SD1c-L5 | Lifeline | :Member | «entity» | - | Lớp AC-E-Member | 680 | 40 | 120 | 460 |
| SD1c-L6 | Lifeline | newPackage:MembershipPackage | «entity» | - | Đối tượng được tạo bởi message loại Tạo; đỉnh lifeline ngang y của message; lớp AC-E-MembershipPackage | 840 | 240 | 120 | 260 |
| SD1c-L7 | Lifeline | :EInvoiceGateway | «boundary» | - | Lớp AC-B-EInvoiceGateway | 1000 | 40 | 120 | 460 |
| SD1c-L8 | Actor | Hệ thống hoá đơn điện tử (ACT-11) | «actor» | - | Tác nhân | 1160 | 40 | 120 | 460 |
| SD1c-F1 | Fragment | ref SD1b - Luồng chính, bước 7-10 | - | - | - | 20 | 80 | 320 | 30 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD1c-M01 | 4.1.3 | SD1c-L2 | SD1c-L3 | // recordPayment (phương thức thu, số tiền) | Đồng bộ | - | 11 |
| SD1c-M02 | 4.1.3.1 | SD1c-L3 | SD1c-L4 | «create» // createTransaction | Tạo | - | 11 |
| SD1c-M03 | 4.1.4 | SD1c-L2 | SD1c-L5 | // activatePackage (thời hạn, loại, chi nhánh áp dụng, ngày bắt đầu) | Đồng bộ | - | 11 |
| SD1c-M04 | 4.1.4.1 | SD1c-L5 | SD1c-L6 | «create» // initializePackage | Tạo | - | 11 |
| SD1c-M05 | 4.1.5 | SD1c-L2 | SD1c-L4 | // prepareInvoiceData | Đồng bộ | - | 12 |
| SD1c-M06 | 4.1.5 (trả về) | SD1c-L4 | SD1c-L2 | dữ liệu giao dịch thu tiền | Trả về | - | 12 |
| SD1c-M07 | 4.1.6 | SD1c-L2 | SD1c-L7 | // sendTransactionData (dữ liệu giao dịch thu tiền) | Đồng bộ | - | 12 |
| SD1c-M08 | 4.1.6.1 | SD1c-L7 | SD1c-L8 | // receiveTransactionData (dữ liệu giao dịch thu tiền) | Đồng bộ | - | 12 |
| SD1c-M09 | 4.1.7 | SD1c-L2 | SD1c-L1 | // showActivatedPackage (gói tập, ngày bắt đầu, trạng thái gói) | Đồng bộ | - | 13 |

### SD2 - Biến thể Lễ tân: bước 1-8, 8a, 8b, 11-13

a) Sơ đồ SD2: Biến thể của tác nhân chính Lễ tân (ACT-05) dùng chung luồng chính: bước 1 đến 8, luồng 8a, 8b, bước 11 đến 13; bước 9, 10 tham chiếu SD1b. Trang "SD2" trong diagrams/P07-sequence-UC-005.drawio.

b) Bảng lifeline và fragment (bảng Node)

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| SD2-L1 | Actor | Lễ tân (ACT-05) | «actor» | - | Tác nhân | 40 | 40 | 120 | 1450 |
| SD2-L2 | Lifeline | :SellPackageUI | «boundary» | - | Lớp AC-B-SellPackageUI | 200 | 40 | 120 | 1450 |
| SD2-L3 | Lifeline | :PurchaseOrRenewPackageHandler | «control» | - | Lớp AC-C-PurchaseOrRenewPackageHandler | 360 | 40 | 120 | 1450 |
| SD2-L4 | Lifeline | oldPackage:MembershipPackage | «entity» | - | Lớp AC-E-MembershipPackage | 520 | 40 | 120 | 1450 |
| SD2-L5 | Lifeline | :PackagePrice | «entity» | - | Lớp AC-E-PackagePrice | 680 | 40 | 120 | 1450 |
| SD2-L6 | Lifeline | :Promotion | «entity» | - | Lớp AC-E-Promotion | 840 | 40 | 120 | 1450 |
| SD2-L7 | Lifeline | :PackageOrder | «entity» | - | Đối tượng được tạo bởi message loại Tạo; đỉnh lifeline ngang y của message; lớp AC-E-PackageOrder | 1000 | 760 | 120 | 730 |
| SD2-L8 | Lifeline | :PaymentTransaction | «entity» | - | Đối tượng được tạo bởi message loại Tạo; đỉnh lifeline ngang y của message; lớp AC-E-PaymentTransaction | 1160 | 1150 | 120 | 340 |
| SD2-L9 | Lifeline | :Member | «entity» | - | Lớp AC-E-Member | 1320 | 40 | 120 | 1450 |
| SD2-L10 | Lifeline | newPackage:MembershipPackage | «entity» | - | Đối tượng được tạo bởi message loại Tạo; đỉnh lifeline ngang y của message; lớp AC-E-MembershipPackage | 1480 | 1230 | 120 | 260 |
| SD2-L11 | Lifeline | :EInvoiceGateway | «boundary» | - | Lớp AC-B-EInvoiceGateway | 1640 | 40 | 120 | 1450 |
| SD2-L12 | Actor | Hệ thống hoá đơn điện tử (ACT-11) | «actor» | - | Tác nhân | 1800 | 40 | 120 | 1450 |
| SD2-F1 | Fragment | loop [mỗi giá gói hiện hành] | - | - | Control lặp (A6) | 340 | 170 | 480 | 90 |
| SD2-F2 | Fragment | loop [mỗi chương trình khuyến mãi đang đặt] | - | - | Control lặp (A6) | 340 | 450 | 640 | 90 |
| SD2-F4 | Fragment | ref SD1b (bước 9, 10, 9a, 10a) | - | SD2-F3 | - | 340 | 800 | 160 | 40 |
| SD2-F3 | Fragment | alt [khách thanh toán qua cổng thanh toán] | - | - | Ba toán hạng: cổng thanh toán (bước 9, 10), 8a, 8b. Cả ba tiếp tục bước 11 | 20 | 770 | 1120 | 320 |
| SD2-F3-O2 | Fragment | [8a: khách trả bằng tiền mặt] | - | SD2-F3 | Toán hạng thứ hai trở đi của alt; đường ngăn là edge SD2-F3-O2-SEP nét đứt | 20 | 880 | 1120 | 20 |
| SD2-F3-O3 | Fragment | [8b: khách quẹt thẻ qua máy POS] | - | SD2-F3 | Toán hạng thứ hai trở đi của alt; đường ngăn là edge SD2-F3-O3-SEP nét đứt | 20 | 1000 | 1120 | 20 |

c) Bảng message (bảng Edge mở rộng)

| ID | STT | Từ | Đến | Message | Loại | Fragment | Bước UC |
|---|---|---|---|---|---|---|---|
| SD2-M01 | 1r | SD2-L1 | SD2-L2 | // requestPackageSale | Đồng bộ | - | 1 |
| SD2-M02 | 1r.1 | SD2-L2 | SD2-L3 | // startPurchase | Đồng bộ | - | 1 |
| SD2-M03 | 1r.1.1 | SD2-L3 | SD2-L5 | // getPriceInfo | Đồng bộ | SD2-F1 | 2 |
| SD2-M04 | 1r.1.1 (trả về) | SD2-L5 | SD2-L3 | thời hạn, loại, chi nhánh áp dụng, giá hiện hành | Trả về | SD2-F1 | 2 |
| SD2-M05 | 1r.1.2 | SD2-L3 | SD2-L2 | // showPackageOptions (các gói tập kèm thời hạn, loại, giá hiện hành) | Đồng bộ | - | 2 |
| SD2-M06 | 2r | SD2-L1 | SD2-L2 | // selectPackage (thời hạn, loại, chi nhánh áp dụng, gói cần gia hạn, người mua gói) | Đồng bộ | - | 3 |
| SD2-M07 | 2r.1 | SD2-L2 | SD2-L3 | // processPackageSelection (gói đã chọn) | Đồng bộ | - | 3 |
| SD2-M08 | 2r.1.1 | SD2-L3 | SD2-L4 | // calculateRenewalStartDate | Đồng bộ | - | 4 |
| SD2-M09 | 2r.1.1 (trả về) | SD2-L4 | SD2-L3 | ngày bắt đầu của gói mới | Trả về | - | 4 |
| SD2-M10 | 2r.1.2 | SD2-L3 | SD2-L6 | // determineApplicableDiscount (gói đã chọn) | Đồng bộ | SD2-F2 | 5 |
| SD2-M11 | 2r.1.2 (trả về) | SD2-L6 | SD2-L3 | mức giảm áp dụng | Trả về | SD2-F2 | 5 |
| SD2-M12 | 2r.1.3 | SD2-L3 | SD2-L5 | // calculateAmountDue (mức giảm áp dụng) | Đồng bộ | - | 5 |
| SD2-M13 | 2r.1.3 (trả về) | SD2-L5 | SD2-L3 | số tiền phải trả | Trả về | - | 5 |
| SD2-M14 | 2r.1.4 | SD2-L3 | SD2-L2 | // showOrderSummary (gói đã chọn, ngày bắt đầu, số tiền phải trả) | Đồng bộ | - | 6 |
| SD2-M15 | 3r | SD2-L1 | SD2-L2 | // confirmSale | Đồng bộ | - | 7 |
| SD2-M16 | 3r.1 | SD2-L2 | SD2-L3 | // placeOrder | Đồng bộ | - | 7 |
| SD2-M17 | 3r.1.1 | SD2-L3 | SD2-L7 | «create» // createOrder (người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả) | Tạo | - | 8 |
| SD2-M18 | 4r | SD2-L1 | SD2-L2 | // confirmCashCollected | Đồng bộ | SD2-F3-O2 | 8a |
| SD2-M19 | 4r.1 | SD2-L2 | SD2-L3 | // confirmCashPayment | Đồng bộ | SD2-F3-O2 | 8a |
| SD2-M20 | 5r | SD2-L1 | SD2-L2 | // enterPosTransactionCode (mã giao dịch POS) | Đồng bộ | SD2-F3-O3 | 8b |
| SD2-M21 | 5r.1 | SD2-L2 | SD2-L3 | // confirmPosPayment (mã giao dịch POS) | Đồng bộ | SD2-F3-O3 | 8b |
| SD2-M22 | 6r | SD2-L3 | SD2-L7 | // recordPayment (phương thức thu, số tiền, mã giao dịch POS nếu có) | Đồng bộ | - | 11 |
| SD2-M23 | 6r.1 | SD2-L7 | SD2-L8 | «create» // createTransaction | Tạo | - | 11 |
| SD2-M24 | 7r | SD2-L3 | SD2-L9 | // activatePackage (thời hạn, loại, chi nhánh áp dụng, ngày bắt đầu) | Đồng bộ | - | 11 |
| SD2-M25 | 7r.1 | SD2-L9 | SD2-L10 | «create» // initializePackage | Tạo | - | 11 |
| SD2-M26 | 8r | SD2-L3 | SD2-L8 | // prepareInvoiceData | Đồng bộ | - | 12 |
| SD2-M27 | 8r (trả về) | SD2-L8 | SD2-L3 | dữ liệu giao dịch thu tiền | Trả về | - | 12 |
| SD2-M28 | 9r | SD2-L3 | SD2-L11 | // sendTransactionData (dữ liệu giao dịch thu tiền) | Đồng bộ | - | 12 |
| SD2-M29 | 9r.1 | SD2-L11 | SD2-L12 | // receiveTransactionData (dữ liệu giao dịch thu tiền) | Đồng bộ | - | 12 |
| SD2-M30 | 10r | SD2-L3 | SD2-L2 | // showActivatedPackage (gói tập, ngày bắt đầu, trạng thái gói) | Đồng bộ | - | 13 |
## F6. Quy tắc tương tác giữa các lớp phân tích

Đã kiểm tra mọi message ở F5 và mọi link ở F7 theo bảng F6 của prompt.

| Vi phạm | Message hoặc link | Cách sửa đã áp dụng |
|---|---|---|
| Không có | - | - |

## F7. Communication diagram

File diagrams/P07-communication-UC-005.drawio, một trang. Phạm vi là luồng chính (SD1a, SD1b, SD1c) và biến thể của tác nhân chính thứ hai Lễ tân (SD2) giữ STT của trang biến thể. MUC_CHI_TIET của hồ sơ dự án là GON nên không vẽ luồng thay thế 8a, 8b, 9a, 10a; STT giữ nguyên theo sequence diagram nên có khoảng trống (không có 3.1.4, 4.1.2, 4r, 5r). Message của bước 9 và 10 trong biến thể Lễ tân dùng lại link và STT của luồng chính (SD2 tham chiếu SD1b qua ref).

### a) Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về | Ghi chú | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|
| C-ACT02 | Actor | Hội viên (ACT-02) | «actor» | - | Tác nhân | 40 | 60 | 60 | 80 |
| C-ACT05 | Actor | Lễ tân (ACT-05) | «actor» | - | Tác nhân | 40 | 340 | 60 | 80 |
| C-UI | Object | :PurchaseOrRenewPackageUI | «boundary» | - | Lớp AC-B-PurchaseOrRenewPackageUI | 240 | 80 | 240 | 40 |
| C-SELL | Object | :SellPackageUI | «boundary» | - | Lớp AC-B-SellPackageUI | 240 | 360 | 240 | 40 |
| C-CTL | Object | :PurchaseOrRenewPackageHandler | «control» | - | Lớp AC-C-PurchaseOrRenewPackageHandler | 680 | 200 | 320 | 60 |
| C-OLD | Object | oldPackage:MembershipPackage | «entity» | - | Lớp AC-E-MembershipPackage | 40 | 600 | 240 | 40 |
| C-PRICE | Object | :PackagePrice | «entity» | - | Lớp AC-E-PackagePrice | 400 | 600 | 240 | 40 |
| C-PROMO | Object | :Promotion | «entity» | - | Lớp AC-E-Promotion | 760 | 600 | 240 | 40 |
| C-ORDER | Object | :PackageOrder | «entity» | - | Lớp AC-E-PackageOrder | 1120 | 600 | 240 | 40 |
| C-PT | Object | :PaymentTransaction | «entity» | - | Lớp AC-E-PaymentTransaction | 1480 | 600 | 240 | 40 |
| C-MEMBER | Object | :Member | «entity» | - | Lớp AC-E-Member | 1840 | 600 | 240 | 40 |
| C-NEW | Object | newPackage:MembershipPackage | «entity» | - | Lớp AC-E-MembershipPackage | 2200 | 600 | 240 | 40 |
| C-PGW | Object | :PaymentGateway | «boundary» | - | Lớp AC-B-PaymentGateway | 1240 | 60 | 240 | 40 |
| C-EIG | Object | :EInvoiceGateway | «boundary» | - | Lớp AC-B-EInvoiceGateway | 1240 | 220 | 240 | 40 |
| C-ACT08 | Actor | Cổng thanh toán (ACT-08) | «actor» | - | Tác nhân | 1640 | 40 | 60 | 80 |
| C-ACT11 | Actor | Hệ thống hoá đơn điện tử (ACT-11) | «actor» | - | Tác nhân | 1640 | 200 | 60 | 80 |

### b) Bảng Edge (link)

| ID | Nguồn | Đích | Loại (Link) | Nhãn (các message theo STT) | Chiều message |
|---|---|---|---|---|---|
| LK-01 | C-ACT02 | C-UI | Link | 1: // requestPurchaseOrRenewal (-->)<br>2: // selectPackage (thời hạn, loại, chi nhánh áp dụng, gói cần gia hạn) (-->)<br>3: // confirmPurchase (-->) | 1, 2, 3: Nguồn-->Đích |
| LK-02 | C-UI | C-CTL | Link | 1.1: // startPurchase (-->)<br>1.1.2: // showPackageOptions (các gói tập kèm thời hạn, loại, giá hiện hành) (<--)<br>2.1: // processPackageSelection (gói đã chọn) (-->)<br>2.1.4: // showOrderSummary (gói đã chọn, ngày bắt đầu, số tiền phải trả) (<--)<br>3.1: // placeOrder (-->)<br>4.1.7: // showActivatedPackage (gói tập, ngày bắt đầu, trạng thái gói) (<--) | 1.1, 2.1, 3.1: Nguồn-->Đích; 1.1.2, 2.1.4, 4.1.7: Đích-->Nguồn |
| LK-03 | C-CTL | C-PRICE | Link | 1.1.1: // getPriceInfo (-->)<br>2.1.3: // calculateAmountDue (mức giảm áp dụng) (-->)<br>1r.1.1: // getPriceInfo (-->)<br>2r.1.3: // calculateAmountDue (mức giảm áp dụng) (-->) | 1.1.1, 2.1.3, 1r.1.1, 2r.1.3: Nguồn-->Đích |
| LK-04 | C-CTL | C-OLD | Link | 2.1.1: // calculateRenewalStartDate (-->)<br>2r.1.1: // calculateRenewalStartDate (-->) | 2.1.1, 2r.1.1: Nguồn-->Đích |
| LK-05 | C-CTL | C-PROMO | Link | 2.1.2: // determineApplicableDiscount (gói đã chọn) (-->)<br>2r.1.2: // determineApplicableDiscount (gói đã chọn) (-->) | 2.1.2, 2r.1.2: Nguồn-->Đích |
| LK-06 | C-CTL | C-ORDER | Link | 3.1.1: «create» // createOrder (người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả) (-->)<br>4.1.3: // recordPayment (phương thức thu, số tiền) (-->)<br>3r.1.1: «create» // createOrder (người mua, gói đã chọn, ngày bắt đầu, số tiền phải trả) (-->)<br>6r: // recordPayment (phương thức thu, số tiền, mã giao dịch POS nếu có) (-->) | 3.1.1, 4.1.3, 3r.1.1, 6r: Nguồn-->Đích |
| LK-07 | C-CTL | C-PGW | Link | 3.1.2: // requestPayment (đơn mua) (-->)<br>4.1: // handlePaymentResult (kết quả giao dịch) (<--) | 3.1.2: Nguồn-->Đích; 4.1: Đích-->Nguồn |
| LK-08 | C-PGW | C-ACT08 | Link | 3.1.2.1: // collectPayment (đơn mua) (-->)<br>4: // returnPaymentResult (kết quả giao dịch) (<--) | 3.1.2.1: Nguồn-->Đích; 4: Đích-->Nguồn |
| LK-09 | C-CTL | C-CTL | Link tự nối | 3.1.3: // startWaitingForPayment (BR-04) (-->)<br>4.1.1: // stopWaitingForPayment (BR-04) (-->) | 3.1.3, 4.1.1: Nguồn-->Đích |
| LK-10 | C-ORDER | C-PT | Link | 4.1.3.1: «create» // createTransaction (-->)<br>6r.1: «create» // createTransaction (-->) | 4.1.3.1, 6r.1: Nguồn-->Đích |
| LK-11 | C-CTL | C-MEMBER | Link | 4.1.4: // activatePackage (thời hạn, loại, chi nhánh áp dụng, ngày bắt đầu) (-->)<br>7r: // activatePackage (thời hạn, loại, chi nhánh áp dụng, ngày bắt đầu) (-->) | 4.1.4, 7r: Nguồn-->Đích |
| LK-12 | C-MEMBER | C-NEW | Link | 4.1.4.1: «create» // initializePackage (-->)<br>7r.1: «create» // initializePackage (-->) | 4.1.4.1, 7r.1: Nguồn-->Đích |
| LK-13 | C-CTL | C-PT | Link | 4.1.5: // prepareInvoiceData (-->)<br>8r: // prepareInvoiceData (-->) | 4.1.5, 8r: Nguồn-->Đích |
| LK-14 | C-CTL | C-EIG | Link | 4.1.6: // sendTransactionData (dữ liệu giao dịch thu tiền) (-->)<br>9r: // sendTransactionData (dữ liệu giao dịch thu tiền) (-->) | 4.1.6, 9r: Nguồn-->Đích |
| LK-15 | C-EIG | C-ACT11 | Link | 4.1.6.1: // receiveTransactionData (dữ liệu giao dịch thu tiền) (-->)<br>9r.1: // receiveTransactionData (dữ liệu giao dịch thu tiền) (-->) | 4.1.6.1, 9r.1: Nguồn-->Đích |
| LK-16 | C-ACT05 | C-SELL | Link | 1r: // requestPackageSale (-->)<br>2r: // selectPackage (thời hạn, loại, chi nhánh áp dụng, gói cần gia hạn, người mua gói) (-->)<br>3r: // confirmSale (-->) | 1r, 2r, 3r: Nguồn-->Đích |
| LK-17 | C-SELL | C-CTL | Link | 1r.1: // startPurchase (-->)<br>1r.1.2: // showPackageOptions (các gói tập kèm thời hạn, loại, giá hiện hành) (<--)<br>2r.1: // processPackageSelection (gói đã chọn) (-->)<br>2r.1.4: // showOrderSummary (gói đã chọn, ngày bắt đầu, số tiền phải trả) (<--)<br>3r.1: // placeOrder (-->)<br>10r: // showActivatedPackage (gói tập, ngày bắt đầu, trạng thái gói) (<--) | 1r.1, 2r.1, 3r.1: Nguồn-->Đích; 1r.1.2, 2r.1.4, 10r: Đích-->Nguồn |

## F8. VOPC (View Of Participating Classes)

File diagrams/P07-class-UC-005.drawio, một trang.

### a) Bảng Node (lớp)

| ID (mã AC) | Loại | Nhãn (tên lớp) | Stereotype | Thuộc về | Ngăn thuộc tính | Ngăn trách nhiệm | x | y | w | h |
|---|---|---|---|---|---|---|---|---|---|---|
| AC-B-PurchaseOrRenewPackageUI | Class | PurchaseOrRenewPackageUI | «boundary» | - | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew | // requestPurchaseOrRenewal<br>// showPackageOptions<br>// selectPackage<br>// showOrderSummary<br>// confirmPurchase<br>// showOrderCancelledNotice<br>// showPaymentFailedNotice<br>// showActivatedPackage | 360 | 40 | 240 | 310 |
| AC-B-SellPackageUI | Class | SellPackageUI | «boundary» | - | selectedDurationMonths<br>selectedPackageType<br>selectedBranch<br>packageToRenew<br>buyer<br>posTransactionCode | // requestPackageSale<br>// showPackageOptions<br>// selectPackage<br>// showOrderSummary<br>// confirmSale<br>// confirmCashCollected<br>// enterPosTransactionCode<br>// showActivatedPackage | 680 | 40 | 240 | 350 |
| AC-B-PaymentGateway | Class | PaymentGateway | «boundary» | - | - | // requestPayment<br>// returnPaymentResult | 1000 | 40 | 240 | 130 |
| AC-B-EInvoiceGateway | Class | EInvoiceGateway | «boundary» | - | - | // sendTransactionData | 1320 | 40 | 240 | 110 |
| AC-C-PurchaseOrRenewPackageHandler | Class | PurchaseOrRenewPackageHandler | «control» | - | - | // startPurchase<br>// processPackageSelection<br>// placeOrder<br>// startWaitingForPayment<br>// handlePaymentTimeout<br>// stopWaitingForPayment<br>// handlePaymentResult<br>// confirmCashPayment<br>// confirmPosPayment | 780 | 490 | 360 | 270 |
| AC-E-MembershipPackage | Class | MembershipPackage | «entity» | - | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản, Q-50)<br>startDate (Ngày)<br>expiryDate (Ngày)<br>status (Trạng thái) | // calculateRenewalStartDate<br>// initializePackage | 40 | 900 | 240 | 230 |
| AC-E-Member | Class | Member | «entity» | - | - | // activatePackage | 360 | 900 | 240 | 110 |
| AC-E-PackageOrder | Class | PackageOrder | «entity» | - | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản, Q-50)<br>startDate (Ngày)<br>amountDue (Số tiền)<br>status (Trạng thái) | // createOrder<br>// cancelUnpaidOrder<br>// recordPayment | 680 | 900 | 240 | 250 |
| AC-E-PaymentTransaction | Class | PaymentTransaction | «entity» | - | paymentMethod (Trạng thái)<br>amount (Số tiền)<br>posTransactionCode (Văn bản) | // createTransaction<br>// prepareInvoiceData | 1000 | 900 | 240 | 170 |
| AC-E-PackagePrice | Class | PackagePrice | «entity» | - | durationMonths (Số lượng)<br>packageType (Văn bản)<br>appliedBranch (Văn bản, Q-50)<br>price (Số tiền) | // getPriceInfo<br>// calculateAmountDue | 1320 | 900 | 240 | 190 |
| AC-E-Promotion | Class | Promotion | «entity» | - | validFrom (Ngày)<br>validTo (Ngày)<br>discountRate (Số lượng, tối đa 20% theo BR-38) | // determineApplicableDiscount | 1640 | 900 | 240 | 150 |

### b) Bảng quan hệ (bảng Edge)

Quan hệ giữa boundary - control và control - entity ghi Loại Association, mang ghi chú "tạm thời" ở cột Nguồn, multiplicity "-" vì đặc tả không nêu; P08 và P12 quyết định dạng thiết kế. R-UC005-13 không có link trong F7, có bằng chứng từ đặc tả. Link actor - boundary (LK-01, LK-08, LK-15, LK-16) và link tự nối (LK-09) không vào VOPC.

| ID | Lớp A | Lớp B | Loại | Multiplicity | Vai trò | Nguồn |
|---|---|---|---|---|---|---|
| R-UC005-01 | AC-B-PurchaseOrRenewPackageUI | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | Link LK-02 (1.1, 1.1.2, 2.1, 2.1.4, 3.1, 4.1.7); tạm thời |
| R-UC005-02 | AC-B-SellPackageUI | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | Link LK-17 (1r.1, 1r.1.2, 2r.1, 2r.1.4, 3r.1, 10r); tạm thời |
| R-UC005-03 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackageOrder | Association | - | - | Link LK-06 (3.1.1, 4.1.3, 3r.1.1, 6r); tạm thời |
| R-UC005-04 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackagePrice | Association | - | - | Link LK-03 (1.1.1, 2.1.3, 1r.1.1, 2r.1.3); tạm thời |
| R-UC005-05 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Promotion | Association | - | - | Link LK-05 (2.1.2, 2r.1.2); tạm thời |
| R-UC005-06 | AC-C-PurchaseOrRenewPackageHandler | AC-E-MembershipPackage | Association | - | - | Link LK-04 (2.1.1, 2r.1.1; gói cũ, cách xác định gói cũ chờ Q-56); tạm thời |
| R-UC005-07 | AC-B-PaymentGateway | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | Link LK-07 (3.1.2, 4.1); tạm thời |
| R-UC005-08 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Member | Association | - | - | Link LK-11 (4.1.4, 7r); tạm thời |
| R-UC005-09 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PaymentTransaction | Association | - | - | Link LK-13 (4.1.5, 8r); tạm thời |
| R-UC005-10 | AC-B-EInvoiceGateway | AC-C-PurchaseOrRenewPackageHandler | Association | - | - | Link LK-14 (4.1.6, 9r); tạm thời |
| R-UC005-11 | AC-E-PackageOrder | AC-E-PaymentTransaction | Association | A 1 - B ? | - | Link LK-10 (4.1.3.1, 6r.1); GL-09, GL-12; mỗi giao dịch thu tiền thuộc một đơn, số giao dịch của một đơn chờ Q-13, Q-81 |
| R-UC005-12 | AC-E-Member | AC-E-MembershipPackage | Association | A 1 - B ? | - | Link LK-12 (4.1.4.1, 7r.1); GL-16, GL-19; mỗi gói tập thuộc một hội viên, số gói của một hội viên chờ Q-69 |
| R-UC005-13 | AC-E-PackageOrder | AC-E-Member | Association | - | - | Bằng chứng đặc tả, không có link: GL-09 (đơn ghi nhận việc một người mua), Dữ liệu vào 1 trường 5 (Người mua gói), Q-01 |

Điểm uốn của các cạnh trong file .drawio (toạ độ tuyệt đối, theo C7.1):

| ID cạnh | Nguồn | Đích | Điểm uốn |
|---|---|---|---|
| R-UC005-01 | AC-B-PurchaseOrRenewPackageUI | AC-C-PurchaseOrRenewPackageHandler | (480,420); (840,420) |
| R-UC005-02 | AC-B-SellPackageUI | AC-C-PurchaseOrRenewPackageHandler | (800,410); (880,410) |
| R-UC005-03 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackageOrder | (930,800); (800,800) |
| R-UC005-04 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PackagePrice | (1050,820); (1440,820) |
| R-UC005-05 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Promotion | (1110,810); (1760,810) |
| R-UC005-06 | AC-C-PurchaseOrRenewPackageHandler | AC-E-MembershipPackage | (810,780); (160,780) |
| R-UC005-07 | AC-B-PaymentGateway | AC-C-PurchaseOrRenewPackageHandler | (1120,430); (1040,430) |
| R-UC005-08 | AC-C-PurchaseOrRenewPackageHandler | AC-E-Member | (870,790); (480,790) |
| R-UC005-09 | AC-C-PurchaseOrRenewPackageHandler | AC-E-PaymentTransaction | (990,830); (1120,830) |
| R-UC005-10 | AC-B-EInvoiceGateway | AC-C-PurchaseOrRenewPackageHandler | (1440,440); (1080,440) |
| R-UC005-11 | AC-E-PackageOrder | AC-E-PaymentTransaction | - |
| R-UC005-12 | AC-E-Member | AC-E-MembershipPackage | - |
| R-UC005-13 | AC-E-PackageOrder | AC-E-Member | - |

## F9. Ma trận truy vết

Luồng 4a, 4b, 4c, 12a không có hành động trong đặc tả nên không có dòng.

| Bước UC | Message (STT) | Lớp tham gia (AC) |
|---|---|---|
| 1 | 1, 1.1, 1r, 1r.1 | AC-B-PurchaseOrRenewPackageUI, AC-C-PurchaseOrRenewPackageHandler, AC-B-SellPackageUI |
| 2 | 1.1.1, 1.1.2, 1r.1.1, 1r.1.2 | AC-C-PurchaseOrRenewPackageHandler, AC-E-PackagePrice, AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI |
| 3 | 2, 2.1, 2r, 2r.1 | AC-B-PurchaseOrRenewPackageUI, AC-C-PurchaseOrRenewPackageHandler, AC-B-SellPackageUI |
| 4 | 2.1.1, 2r.1.1 | AC-C-PurchaseOrRenewPackageHandler, AC-E-MembershipPackage |
| 5 | 2.1.2, 2.1.3, 2r.1.2, 2r.1.3 | AC-C-PurchaseOrRenewPackageHandler, AC-E-Promotion, AC-E-PackagePrice |
| 6 | 2.1.4, 2r.1.4 | AC-C-PurchaseOrRenewPackageHandler, AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI |
| 7 | 3, 3.1, 3r, 3r.1 | AC-B-PurchaseOrRenewPackageUI, AC-C-PurchaseOrRenewPackageHandler, AC-B-SellPackageUI |
| 8 | 3.1.1, 3r.1.1 | AC-C-PurchaseOrRenewPackageHandler, AC-E-PackageOrder |
| 8a | 4r, 4r.1 | AC-B-SellPackageUI, AC-C-PurchaseOrRenewPackageHandler |
| 8b | 5r, 5r.1 | AC-B-SellPackageUI, AC-C-PurchaseOrRenewPackageHandler |
| 9 | 3.1.2, 3.1.3 | AC-C-PurchaseOrRenewPackageHandler, AC-B-PaymentGateway |
| 9a | 3.1.4 | AC-C-PurchaseOrRenewPackageHandler |
| 9a1 | 3.1.4.1 | AC-C-PurchaseOrRenewPackageHandler, AC-E-PackageOrder |
| 9a2 | 3.1.4.2 | AC-C-PurchaseOrRenewPackageHandler, AC-B-PurchaseOrRenewPackageUI |
| 10 | 3.1.2.1, 4, 4.1, 4.1.1 | AC-B-PaymentGateway, AC-C-PurchaseOrRenewPackageHandler |
| 10a | 4.1.2 | AC-C-PurchaseOrRenewPackageHandler, AC-B-PurchaseOrRenewPackageUI |
| 11 | 4.1.3, 4.1.3.1, 4.1.4, 4.1.4.1, 6r, 6r.1, 7r, 7r.1 | AC-C-PurchaseOrRenewPackageHandler, AC-E-PackageOrder, AC-E-PaymentTransaction, AC-E-Member, AC-E-MembershipPackage |
| 12 | 4.1.5, 4.1.6, 4.1.6.1, 8r, 9r, 9r.1 | AC-C-PurchaseOrRenewPackageHandler, AC-E-PaymentTransaction, AC-B-EInvoiceGateway |
| 13 | 4.1.7, 10r | AC-C-PurchaseOrRenewPackageHandler, AC-B-PurchaseOrRenewPackageUI, AC-B-SellPackageUI |

## F10. File .drawio

| File | Số trang | Nội dung |
|---|---|---|
| diagrams/P07-sequence-UC-005.drawio | 4 | SD1a, SD1b, SD1c, SD2 |
| diagrams/P07-communication-UC-005.drawio | 1 | Luồng chính và biến thể Lễ tân |
| diagrams/P07-class-UC-005.drawio | 1 | VOPC |

ID cell trùng ID trong bảng mô hình; toạ độ là bội số của 10. Sequence: lifeline ở y=40 cách nhau 160, rộng 120; message đầu tiên ở y=120, mỗi message sau cách 40; lifeline của đối tượng được tạo có đỉnh ngang y của message Tạo. Trang bắt đầu bằng fragment ref đặt ở y=80, cao 30, để message đầu vẫn ở y=120.

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-81 | Giao dịch thu tiền không thành công ở cổng thanh toán (luồng 10a) có được hệ thống ghi nhận lại để tra cứu hoặc đối soát không, hay chỉ giao dịch thành công mới được ghi nhận ở bước 11? (Chỉ ghi nhận giao dịch thành công / Ghi nhận cả giao dịch không thành công kèm kết quả / Khác - nêu rõ) | AC-E-PaymentTransaction (thời điểm tạo, thuộc tính kết quả); F2 bước 10a, 11; GL-12; R-UC005-11 | UC-005 bước 10 và luồng 10a chỉ nêu việc thông báo cho hội viên, bước 11 chỉ nêu ghi nhận đơn đã thanh toán; đặc tả không nêu việc lưu giao dịch không thành công |
| Q-82 | Các "gói tập" được hiển thị ở bước 2 và chọn ở bước 3 (có thời hạn, loại, giá) có chính là Giá gói (GL-10) do giám đốc chuỗi đặt, hay là một danh mục gói riêng mà giá gắn vào? (Chỉ có Giá gói, mỗi giá gói là một tổ hợp thời hạn và loại / Có danh mục gói riêng, giá gắn vào danh mục / Khác - nêu rõ) | AC-E-PackagePrice; F2 bước 2, 3, 5; GL-10, GL-16; UC-026 | UC-005 bước 2 "Hiển thị các gói tập kèm thời hạn, loại và giá hiện hành" dùng "gói tập" cho mặt hàng được bán, trong khi GL-16 định nghĩa Gói tập là quyền hội viên có sau khi mua và GL-10 định nghĩa Giá gói là số tiền để mua một gói tập có thời hạn và loại xác định |

Các câu hỏi đã cấp ở bước trước và làm đổi phân tích này (nội dung không chép lại để mỗi mã chỉ trỏ tới một câu hỏi): Q-01, Q-03, Q-08, Q-09, Q-10 (người mua tại quầy, danh mục chi nhánh, phạm vi và cách áp dụng giá, khuyến mãi), Q-13, Q-14, Q-24, Q-25, Q-51, Q-52, Q-56 (thanh toán lại, kết quả đến sau khi huỷ, ngày bắt đầu các nhánh, cách tính 15 phút, cách xác định gói cũ), Q-39, Q-54, Q-55 (hoá đơn điện tử, mã giao dịch POS), Q-50, Q-53, Q-69, Q-74, Q-75 (chi nhánh áp dụng, kênh thông báo, số gói của một hội viên, ngày hết hạn, trạng thái gói).

## Giả định

Không có (chế độ NGHIEM_NGAT, không dùng mục này).

## Đề xuất sửa artifact trước

| Bước | Mã phần tử | Vấn đề | Đề nghị |
|---|---|---|---|
| P05 | GL-16, GL-10 (cột Ghi chú) | P04 UC-005 bước 2 và 3 dùng "gói tập" cho mặt hàng được bán (thời hạn, loại, giá), còn GL-16 định nghĩa Gói tập là quyền hội viên có sau khi mua; P05 chưa có thuật ngữ cho mặt hàng được bán (Q-82) | Khi Q-82 có câu trả lời, bổ sung thuật ngữ hoặc ghi chú vào GL-10 cho mặt hàng được bán, rồi đổi cách gọi tương ứng ở P04 UC-005 bước 2, 3 |

## Vấn đề còn mở

Các mục Target đạt, trừ mục 1 (đạt một phần), với các điểm cần người dùng lưu ý:

- Target 1: luồng 4a, 4b, 4c, 12a trong đặc tả chưa có hành động ("Chờ Q-nn") nên không có dòng F4, F9 và không có message; các luồng đó có dòng ở F2. Khi Q-51, Q-24, Q-52, Q-54 có câu trả lời và P04 bổ sung hành động, chạy lại P07.
- Target 12: MUC_CHI_TIET là GON nên communication diagram chỉ gồm luồng chính và biến thể Lễ tân. Nếu dự án chuyển sang DAY_DU thì thêm 8a, 8b, 9a, 10a.
- Kênh thông báo ở luồng 9a2 và 10a chờ Q-53. Message tạm gửi tới boundary giao diện người dùng của tác nhân đang thao tác, đây chưa phải lựa chọn kênh. Nếu Q-53 chọn thông báo đẩy hoặc SMS thì cần boundary Kênh thông báo (PushNotifier, SmsNotifier theo HAU_TO_TEN_LOP), tác nhân phụ ACT-09, ACT-10 ở UC-005 (P02, P03, P04), rồi chạy lại P07.
- Luồng 9a vẽ là break tại một điểm (giữa bước 9 và bước 10) vì đặc tả đặt 9a ở bước 9 và không ghi hết thời hạn xảy ra "tại bất kỳ bước nào" của một khoảng; nếu Q-25 hoặc Q-13 (thanh toán lại trên cùng đơn) làm thời hạn bao trùm nhiều bước thì chuyển 9a sang trang riêng theo A2.
- Lớp có chủ sở hữu ở use case khác chưa có P07, P07 của use case đó phải dùng lại mã: AC-E-Member (UC-003), AC-E-PackagePrice (UC-026), AC-E-Promotion (UC-027). Lớp do P07 này đặt mã lần đầu và các use case sau phải dùng lại: AC-E-MembershipPackage (UC-006, UC-007, UC-018), AC-E-PaymentTransaction (UC-007, UC-017, UC-019), AC-B-EInvoiceGateway (UC-007, UC-017, UC-019), AC-B-PaymentGateway.
- Tính số tiền phải trả (bước 5) có dữ liệu ở hai lớp không có quan hệ cấu trúc; phương án và lý do ở F4. P08 xem lại khi Q-08, Q-09, Q-10 có câu trả lời.
- Tập giá gói và tập chương trình khuyến mãi được control lặp (A6); việc chọn các phần tử của tập (truy vấn) không vẽ vì đặc tả không nêu.
- Entity Member chỉ có một trách nhiệm (// activatePackage) và không có thuộc tính trong use case này; P08 hợp nhất với các use case khác của hội viên. Thông tin chi nhánh chỉ lưu dạng thuộc tính appliedBranch; P08 quyết định có entity Branch hay không (Q-03, Q-50).
- Bước 9 và 10 của biến thể Lễ tân dùng ref tới SD1b theo nghĩa đặc tả ghi bước 9, 10 chung cho "Hội viên / Lễ tân"; nếu lễ tân chỉ thu tiền mặt hoặc POS thì bỏ toán hạng cổng thanh toán của alt trong SD2.
