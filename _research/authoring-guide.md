# Hướng dẫn viết prompt cho bộ prompt-system (nội bộ, dành cho người viết)

File này không thuộc sản phẩm. Mọi file prompt trong prompt-system/ phải theo đúng cấu trúc và quy tắc dưới đây.

## 1. Quy tắc bắt buộc về nội dung sản phẩm

1. Sản phẩm trung lập, chia sẻ cho mọi developer. Tuyệt đối không nhắc tới: bài giảng, slide, giáo viên, giảng viên, môn học, trường, sinh viên, bài tập, AIMS, Interbank, VNPay, tên người, HUST, SoICT, IBM courseware, ITSS. Không dùng ví dụ lấy từ các case study AIMS (media store: CD, LP, DVD, book; rush order; Place order/Pay order/Cancel order/Refund order của AIMS). Không dùng ví dụ "Course Registration System" của IBM (Register for Courses, Close Registration, Student, Registrar, Professor, Course Catalog, Billing System) vì đó là ví dụ đặc trưng của tài liệu gốc.
2. Ví dụ dùng các miền trung lập, luân phiên giữa các miền sau để người đọc thấy tính tổng quát:
   - Phòng khám tư đặt lịch khám (bệnh nhân, lễ tân, bác sĩ, quản trị, cổng SMS).
   - Thư viện (bạn đọc, thủ thư, hệ thống email).
   - Giao đồ ăn (khách hàng, nhà hàng, tài xế, cổng thanh toán).
   - Quản lý kho (thủ kho, kế toán, máy quét mã vạch, hệ thống ERP).
   - Có thể thêm: đặt phòng khách sạn, quản lý bãi đỗ xe, máy ATM.
3. Căn cứ trong sản phẩm chỉ dẫn tài liệu công khai (UML 2.5.1 OMG, Cockburn, Larman, Jacobson, Bittner & Spence, ISO/IEC/IEEE 29148, ISO/IEC 25010, Fowler, Ambler, Martin, Nielsen, Shneiderman, WCAG, Chen, Codd...). Đối chiếu với slide bài giảng thì ghi trong _research/, không ghi trong sản phẩm.
4. Nội dung phải khớp với quy định của slide bài giảng (vì người dùng cần bám slide). Nếu tài liệu ngoài khác slide, sản phẩm theo slide, và ghi chênh lệch trong _research/.
5. Định dạng văn bản của mọi file (cả sản phẩm và _research): không dùng dấu gạch ngang dài (em dash), dùng "-"; không dùng ký hiệu mũi tên Unicode, dùng "-->"; không dùng inline code (cặp dấu backtick trong dòng) trong phần văn xuôi Markdown; hạn chế in đậm, in nghiêng (tối đa 1-2 lần mỗi đoạn). Code block (ba dấu backtick trở lên) thì được dùng.
6. Tiếng Việt có dấu đầy đủ; thuật ngữ UML giữ tiếng Anh.

## 2. Cấu trúc một file prompt

Tên file: Pxx-<slug-tieng-anh>.md, ví dụ P02-identify-use-cases.md. Nội dung theo đúng thứ tự:

```text
# Pxx - <Tên bước tiếng Việt> (<Tên tiếng Anh>)

## 1. Mục đích
2-4 câu: bước này làm gì, tại sao cần, vị trí trong pipeline.

## 2. Đầu vào và đầu ra
Bảng: | Loại | Artifact | Bắt buộc | Dùng để |
Đầu ra ghi đúng tên file theo 00-Conventions mục C4.

## 3. Cách chạy
- Đính kèm: 00-Conventions.md, project-profile.md, các file đầu vào.
- Chạy một lần cho toàn hệ thống hay lặp cho từng phần tử (ví dụ từng UC).
- Placeholder cần điền trong prompt (bảng ngắn: tên, bắt buộc/tuỳ chọn, ý nghĩa).

## 4. Prompt
Một code block duy nhất, fence bốn dấu backtick với nhãn text, để người dùng sao chép nguyên khối.
Bên trong theo khung CRAFT:
  [Context]  - đọc hồ sơ dự án, Conventions, đầu vào nào; phạm vi lần chạy (placeholder nếu lặp).
  [Role]     - vai trò chuyên gia phù hợp.
  [Action]   - quy trình từng bước để đi từ đầu vào tới đầu ra (cách làm, không phải kết quả sẵn).
  [Format]   - đặc tả đầu ra chi tiết từng thành phần (xem mục 3 dưới đây).
  [Target]   - checklist tự kiểm tra, dạng câu có thể trả lời Đạt/Không đạt.
  [Yêu cầu bổ sung] - placeholder YEU_CAU_BO_SUNG [TUỲ CHỌN] luôn ở cuối.
Placeholder đặt đúng chỗ dùng, theo cú pháp {{PH:TEN | Hướng dẫn: ... | Ví dụ: ...}}, ví dụ lấy từ ít nhất hai miền khác nhau. Ngoại lệ: placeholder dạng giá trị (Có/Không, mã bắt đầu) chỉ cần một ví dụ.
Không để phần đặc thù bài toán nằm ngoài placeholder.

## 5. Ghi chú cho người dùng
- Lỗi hay gặp khi dùng bước này và cách xử lý (ví dụ kết quả quá dài, cần chạy lại bước trước).
- Cách dùng bước này độc lập (khi không chạy cả pipeline).

## 6. Căn cứ
Danh sách tài liệu công khai đã dùng để xây dựng quy tắc của bước.
```

## 3. Đặc tả đầu ra trong [Format]: yêu cầu chiều sâu

Với mỗi thành phần của đầu ra (ví dụ mỗi cột, mỗi mục, mỗi loại phần tử sơ đồ), [Format] phải nêu:

1. Định nghĩa: thành phần này là gì.
2. Quy tắc: điều bắt buộc (đặt tên, số lượng, độ dài, cách viết).
3. Mức hợp lý: thế nào là đúng mức, kèm tiêu chí kiểm tra được (phép thử, ngưỡng).
4. Lỗi thường gặp: thế nào là quá nhỏ, quá lớn, nhầm lẫn với khái niệm khác, kèm dấu hiệu nhận biết.
5. Ví dụ đúng và ví dụ sai (kèm lý do sai), lấy từ các miền trung lập.

Ngưỡng định lượng (ví dụ "luồng chính 3-15 bước") phải có lý do hoặc nguồn trong _research/.

Đầu ra phải đủ cấu trúc để bước sau đọc được: bảng có cột cố định, mã định danh theo Conventions mục C3, cột truy vết.

Sơ đồ: đầu ra gồm bảng mô hình Node/Edge trong .md và nội dung file .drawio theo Conventions mục C7. Prompt phải nêu rõ quy tắc ngữ nghĩa UML của sơ đồ đó (ký hiệu, chiều mũi tên, điều cấm) và quy tắc bố cục riêng nếu có.

## 4. File nghiên cứu trong _research/

Mỗi nhánh tạo _research/<nhanh>-notes.md gồm:
- Trích quy định từ slide (tên file slide, số trang) cho từng bước.
- Tóm tắt tài liệu ngoài đã dùng, nêu rõ quy tắc nào lấy từ đâu.
- Chênh lệch giữa slide và tài liệu ngoài, và lựa chọn đã áp dụng.
