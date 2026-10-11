Model của phiên chạy: Sonnet (claude-sonnet-5-5)

# Nhật ký người chạy P02 - bus-r2

Đầu ra: bus-r2/design/P02-usecases.md (28 UC, 66 CAND, 29 EV, Q-40, ASM-14 lớn nhất). Placeholder PHAM_VI_LAN_CHAY, QUY_UOC_DA_CHOT, YEU_CAU_BO_SUNG: Không có. Đã đọc P02 (đủ 418 dòng), 00-Conventions.md, README.md, project-profile.md, yeu-cau-xe-khach.md, P00, P01. Không đọc file khác trong _research/.

Kiểm tra tự động sau khi ghi: 66 CAND liên tục, mỗi CAND một kết luận đúng sáu dạng, mọi mã UC và CAND được trỏ tới đều tồn tại, 28 UC có đủ ở bảng 4a và 4b, ma trận REQ đủ 77 dòng, không có em dash, mũi tên Unicode hay inline code. Không có mục Target nào ở trạng thái Không đạt, nhưng mục 4 (U-T1 đến U-T12) phần lớn là đánh giá chủ quan cho UC-005, UC-018, UC-025 (xem mục 12).

## Vướng mắc

1. Bước 9.1, chọn quy trình nghiệp vụ chính khi hoà.
   - Câu: "nếu hoà thì chọn tác nhân gắn với mục tiêu nghiệp vụ đầu tiên ở P00 mục 1".
   - Gặp: ACT-01, ACT-02, ACT-03 đều 6 UC User-goal. Mục tiêu đầu tiên của P00 là "Có phần mềm bán vé và quản lý chuyến thay cho cách bán qua điện thoại và quầy", gắn được với cả ACT-02 (quầy, điện thoại) lẫn ACT-03 (quản lý chuyến). Số UC cũng phụ thuộc cách tính (Subfunction có tính không, UC danh mục tách hay gộp).
   - Xử lý: chọn ACT-02, đánh số nhóm Bán vé tại quầy ngay sau nhóm Tài khoản. Ghi ở Vấn đề còn mở.

2. Bước 9.1, nhóm điều kiện tiên quyết.
   - Câu: "Nhóm chứa điều kiện tiên quyết của quy trình đó (đăng ký tài khoản, đăng ký thành viên) đánh số trước nhóm quy trình."
   - Gặp: ví dụ chỉ có đăng ký; đề này đăng ký tài khoản của hành khách là tuỳ chọn, còn điều kiện của ACT-02 là Đăng nhập (tài khoản do ACT-04 cấp). Không rõ Đăng nhập có tính là điều kiện tiên quyết không, và trong nhóm Tài khoản thì Đăng nhập đứng trước hay sau Đăng ký, Quản lý tài khoản nhân viên (quy tắc "việc xảy ra trước đánh số trước" cho đăng ký trước đăng nhập).
   - Xử lý: coi Đăng nhập là điều kiện tiên quyết tự làm của ACT-02, đặt nhóm Tài khoản đầu; trong nhóm đánh số đăng ký, quản lý tài khoản, rồi đăng nhập.

3. Q4 a so với UC User-goal đã có (đoạn chọn chuyến và chỗ).
   - Câu: Q4 a "một đoạn tương tác liền mạch (thường từ 3 bước trở lên) được dùng lặp lại trong từ hai use case User-goal trở lên"; ví dụ "Chọn khung giờ ... được giữ thành UC dùng chung theo Q4 a".
   - Gặp: tìm chuyến, xem sơ đồ, chọn chỗ dùng ở 5 UC (đặt, bán, nhận đặt chỗ, đổi vé hai kênh), thoả Q4 a về hình thức; nhưng phần tìm chuyến và xem sơ đồ đã là UC User-goal Tra cứu chuyến xe (U-R05, U-R17), nên tạo thêm Subfunction sẽ trùng (U-T11).
   - Xử lý: tách ứng viên thành CAND-01 (đã là UC-008) và CAND-35 (chọn chỗ, dưới 3 bước, là bước). Prompt không nói rõ khi đoạn dùng chung trùng một UC User-goal thì làm gì, và không có kết luận "Dùng chung UC-nnn".

4. Q4 d, chế độ CO_NHAN và căn cứ trong nguồn.
   - Câu: Q4 "mọi điều kiện đều có căn cứ trong nguồn"; Q4 d vế ba "có thể thực hiện lại hoặc thất bại độc lập"; Conventions C1.2 "chỗ thiếu làm thay đổi danh sách ... use case phải có ASM-nn chọn một phương án của Q-nn".
   - Gặp: thanh toán trực tuyến khớp gần như đúng ví dụ Q4 d (cổng thanh toán, thất bại), nhưng vế ba chỉ suy ra yếu từ "Hết 10 phút chưa thanh toán thành công" và P00 để Q-17 mở không kèm ASM. Không rõ ASM có được dùng để cấp "căn cứ" cho một điều kiện Q4 không, và có bắt buộc tạo ASM ở mọi Q-nn mà đáp án làm đổi danh sách UC không (ví dụ hoàn tiền thất bại độc lập cũng làm đổi danh sách).
   - Xử lý: tạo ASM-12 (Q-17 phương án có), giữ UC-010 Subfunction; với hoàn tiền qua cổng (CAND-49, CAND-57) không có chỗ dựa trong nguồn nên không tạo ASM và kết luận bước. Quyết định hơi tuỳ ý; hai chỗ tương tự được xử lý khác nhau.

5. Q4 a và b, d lẫn nhau khi cùng một đoạn.
   - Câu: Q4 a "UC gốc chỉ dùng đoạn đó khi một điều kiện đúng thì không được đếm cho Q4 a; xét Q4 b".
   - Gặp: Thanh toán trực tuyến bắt buộc ở UC-009 nhưng có điều kiện ở UC-014 (chỉ khi vé mới đắt hơn). Ví dụ trong prompt chỉ trộn a và b; đề này cần d (UC-009) và b (UC-014). Cột Tác nhân chính "(qua UC-xxx)" cho hai UC gốc cũng chưa có ví dụ trộn.
   - Xử lý: ghi "Q4 d với UC-009; Q4 b với UC-014" ở Mô tả ngắn, tác nhân chính "ACT-01 (qua UC-009, UC-014)".

6. U-R10 và U-R12 mâu thuẫn khi tách trả vé, đổi vé theo kênh.
   - Câu: U-R10 "hai điều kiện loại trừ nhau ... b) Không thoả a: một UC"; U-R12 "Chỉ tách ... khi ... có tác nhân phụ khác nhau".
   - Gặp: trả vé trực tuyến (hành khách, cổng thanh toán) và trả vé tại quầy (nhân viên làm thay, tiền mặt). Đây không phải đại diện cho cùng một đối tượng vé mà là hai tập vé theo ASM-04. U-R10 a đòi "đoạn tương tác riêng từ 2 bước" của người đại diện hoặc "trạng thái kết thúc khác"; nguồn không mô tả được các bước đó, còn U-R12 cho tách chỉ vì tác nhân phụ khác. Hai quy tắc cho kết quả ngược nhau.
   - Xử lý: tách theo U-R12 và U-R10 a (suy ra đoạn tra vé, trao tiền mặt), ghi lựa chọn ở Vấn đề còn mở. Phần "suy ra" vượt nguồn một chút.

7. Cột Kết luận chỉ cho một mã UC, nhưng nhiều bước thuộc nhiều UC.
   - Câu: Kết luận "Là bước của UC-nnn".
   - Gặp: chọn chỗ, nhập thông tin người đi, in vé giấy, tính mức hoàn, ngăn trùng chỗ, trao đổi SMS đều là bước của 2 đến 5 UC.
   - Xử lý: ghi một UC chính ở cột Kết luận, các UC còn lại ở cột Lý do. Không có kết luận chuẩn cho trường hợp này; chọn UC chính là tuỳ ý.

8. U-R07 hết giờ trong phiên: phạm vi "phiên".
   - Câu: "khi tác nhân chính vẫn đang ở phiên của một UC và hệ thống chờ một sự kiện có hạn giờ".
   - Gặp: giữ chỗ 10 phút. Hành khách có thể đóng trình duyệt, khi đó không còn phiên mở nhưng chỗ vẫn phải được trả. Ví dụ khách sạn của prompt tương tự và được xếp luồng thay thế, nên theo đó; nhưng tiêu chí thứ ba của U-R07 tác vụ theo lịch ("mốc rơi vào lúc không còn phiên nào của tác nhân đang mở") lại cho UC thời gian. Hai nhánh chồng lên nhau ở đúng trường hợp này. Thêm nữa, vì thanh toán là UC-010 được include, hết giờ xảy ra trong UC-010 hay UC-009 không được hướng dẫn.
   - Xử lý: theo P01 (không có tác nhân thời gian cho giữ chỗ), kết luận bước của UC-009.

9. Phép thử không đạt khi được U-R ghi đè.
   - Câu: Mục 3 "Phép thử không đạt: ... hoặc "-" khi Giữ"; Target 4 "trừ phép thử bị một quy tắc U-R ... ghi đè".
   - Gặp: UC-007, UC-025 (U-R07), UC-003 (U-R01) không đạt U-T3, U-T5 nhưng kết luận Giữ. Cột có hai hướng dẫn mâu thuẫn ("-" khi Giữ, và ghi mọi phép thử không đạt ở Q5).
   - Xử lý: ghi các phép thử không đạt kèm "(ghi đè bởi U-R07)" thay vì "-".

10. Mục 2, sự kiện không có loại hoặc nguồn phát đơn.
   - Câu: "Nguồn phát (ACT; "-" với sự kiện thời gian trong phiên của một UC)"; "Loại Thiết bị chỉ dùng cho tín hiệu thiết bị tự phát (U-R18)".
   - Gặp: EV-29 "máy có sóng trở lại" là tín hiệu thiết bị nhưng máy không là tác nhân (P01, ASM-10), nên Nguồn phát không có mã ACT; "-" chỉ được định nghĩa cho sự kiện thời gian. EV-05 (đăng nhập) có 5 tác nhân nguồn phát nhưng cột chỉ ghi một ACT. Sự kiện hết 10 phút giữ chỗ (EV-03) có lúc không có người trong phiên.
   - Xử lý: EV-29 Loại Thiết bị, Nguồn phát "-"; EV-05 liệt kê 5 mã trong một ô.

11. Mục 1, tác nhân chính nhưng mục tiêu Summary chung hai tác nhân; Đăng nhập lặp lại.
   - Câu: "Mỗi tác nhân chính ... có ít nhất một dòng."
   - Gặp: mục tiêu Summary "Bán vé cho hành khách" thuộc ACT-01 và ACT-02; Đăng nhập lặp thành một dòng cho mỗi tác nhân. Cột ACT chỉ định nghĩa một mã.
   - Xử lý: ô ACT ghi hai mã cho Summary; lặp dòng Đăng nhập cho 4 tác nhân, cùng CAND-05.

12. Target 4 khó kiểm chứng đủ.
   - Câu: "Mọi UC mức User-goal đạt U-T1 đến U-T12".
   - Gặp: không có hướng dẫn mức bằng chứng. UC-005 (đặt chỗ để lại trạng thái chờ thanh toán, U-T7), UC-018 (hoàn tiền mặt, 3-4 bước, U-T4), UC-025 (chỉ có tác nhân thời gian, U-T3) chỉ đạt nhờ cách đọc dễ tính. Các UC danh mục (UC-019 đến UC-022) U-T4 chỉ dựa vào ASM-06 và không có bước nào nguồn mô tả.
   - Xử lý: ghi Đạt, ghi U-T3 và U-T4 vào cột Phép thử không đạt chỗ có ghi đè.

13. Thao tác của UC Quản lý danh mục khi nguồn không nêu.
   - Câu: U-R04 "Chỉ đưa vào "Quản lý X" những thao tác mà nguồn nêu."
   - Gặp: REQ-48 đến REQ-50 (từ ASM-06) chỉ nói "quản lý", không có thêm, sửa, ngừng dùng. Mô tả ngắn bắt buộc nêu biến thể chính nhưng không có thông tin.
   - Xử lý: ghi "Nguồn chỉ nêu quản lý nên thao tác cụ thể do P04 chốt". Dẫn chiếu sang bước sau trong Mô tả ngắn có thể trái nguyên tắc chỉ mô tả trong phạm vi bước này.

14. Tách bến xe và tuyến xe, loại xe và xe.
   - Câu: U-R04 "Chỉ gộp nhiều loại dữ liệu vào một UC khi ... một loại chỉ là thuộc tính phụ của loại kia."
   - Gặp: "thuộc tính phụ" không có tiêu chí. P00 gộp tuyến và bến trong một REQ-48, nhưng tôi tách (bến được nguồn đếm riêng), còn loại xe và sơ đồ chỗ gộp vào xe. Cách phân xử mang tính cảm tính, có thể cho kết quả khác ở lần chạy khác.
   - Xử lý: như trên, ghi lý do vào cột Lý do.

15. Nhóm chức năng dưới 3 UC.
   - Câu: "Mỗi nhóm thường 3-12 UC; một nhóm chỉ có 1 UC thì cân nhắc nhập vào nhóm gần nhất."
   - Gặp: ba nhóm có 2 UC (Giá vé, Soát vé, Báo cáo); quy tắc chỉ nói về nhóm 1 UC.
   - Xử lý: giữ, giải thích ở Mục 6.

16. Ngữ cảnh lớn.
   - Prompt P02 dài hơn 66 KB, và công cụ đọc file cắt ở 25.000 token nên phải đọc nhiều lần; P00 hơn 51 KB cũng bị cắt. Phần [Format] chứa cả định nghĩa (Phần A đến E), nên khối cần đọc để thực thi gần như là cả file. Không có chỗ nào không thể thoả đồng thời, nhưng độ dài làm khó theo dõi các cross-reference (ví dụ U-R10 ở mục 6, Q4 ở mục 5).

17. Tên UC dài.
   - Câu: U-N7 "thường 2-6 từ".
   - Gặp: UC-025 "Gửi danh sách hành khách cho phụ xe" 7 từ; tên ngắn hơn mất kết quả nghiệp vụ (U-N3). U-N2 yêu cầu tên tác nhân thời gian nêu kết quả nghiệp vụ nhưng kết quả này là dữ liệu cho tác nhân khác.
   - Xử lý: giữ 7 từ, ghi ở Vấn đề còn mở.

18. Tác nhân phụ của UC có include Subfunction.
   - Gặp: UC-009 include UC-010 (gọi cổng thanh toán). Cột Tác nhân phụ của UC-009 chỉ ghi ACT-07 hay cả ACT-06? Prompt chỉ hỏi "trong use case này hệ thống cần gọi tới ai", không nói về phần đã tách. Chọn chỉ ghi ACT-06 ở UC-010 (và nêu trong Mô tả ngắn của UC-009); P03 có thể hiểu khác.

19. U-R01, ASM cho đăng nhập.
   - Câu: "ở CO_NHAN ghi ASM-nn nêu những tác nhân phải đăng nhập".
   - Gặp: ASM-01 (hành khách) và ASM-02 (nhân viên) đã có ở P00. Không rõ phải tạo ASM mới ở P02 hay dùng lại; hướng dẫn Mục 3 cho phép "dùng ASM-nn mà P00, P01 đã ghi". Dùng lại. Phương thức đăng nhập của nhân viên (mật khẩu hay khác) chưa ai hỏi, không ảnh hưởng danh sách UC nên không tạo Q.

20. Mã Q, ASM.
   - Không vướng: Q-39, ASM-11 lấy từ P01 và xác nhận bằng grep trên toàn design/; cấp Q-40, ASM-12 đến ASM-14.
