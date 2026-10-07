# P00 - Chuẩn hoá yêu cầu - Hệ thống đặt lịch khám ClinicBook

| Thuộc tính | Giá trị |
|---|---|
| Bước | P00 |
| Phiên bản | 1.0 |
| Đầu vào đã dùng | 00-Conventions.md, project-profile.md, yeu-cau-phong-kham.md |
| Phạm vi | Toàn hệ thống |

## 1. Bối cảnh và mục tiêu nghiệp vụ

Phòng khám đa khoa tư nhân Minh An có 3 chuyên khoa (Nội, Nhi, Da liễu) với khoảng 12 bác sĩ. Hiện nay bệnh nhân đặt lịch qua điện thoại và lễ tân ghi sổ. Cách làm này thường xuyên gây trùng lịch, và bệnh nhân không đến mà không báo. Phòng khám cần một phần mềm web để quản lý việc đặt lịch khám.

Mục tiêu nghiệp vụ:
- Giảm tình trạng trùng lịch khám do ghi sổ (nguồn: đoạn mở đầu, "thường xuyên trùng lịch").
- Giảm tình trạng bệnh nhân không đến mà không báo (nguồn: đoạn mở đầu, "bệnh nhân không đến mà không báo").
- Quản lý việc đặt lịch khám bằng phần mềm web (nguồn: đoạn mở đầu, "Phòng khám cần một phần mềm web để quản lý việc đặt lịch khám").

## 2. Phạm vi

Trong phạm vi:
- Tra cứu chuyên khoa, bác sĩ, lịch trống không cần đăng nhập (REQ-02 đến REQ-05).
- Đăng ký tài khoản bệnh nhân, xác thực số điện thoại bằng OTP (REQ-06 đến REQ-08).
- Đặt lịch khám trực tuyến, xác nhận hoặc từ chối lịch, thông báo SMS (REQ-09 đến REQ-18).
- Hủy lịch hẹn (REQ-19 đến REQ-21).
- Lễ tân đặt lịch hộ, tạo hồ sơ bệnh nhân (REQ-22 đến REQ-25).
- Nhắc lịch tự động (REQ-26).
- Check-in, đánh dấu không đến, khoá tự đặt lịch (REQ-27 đến REQ-30).
- Bác sĩ xem lịch hẹn và ghi kết luận khám (REQ-31 đến REQ-34).
- Lịch làm việc và khoá khung giờ của bác sĩ (REQ-35 đến REQ-37).
- Quản trị danh mục, tài khoản, tham số (REQ-38 đến REQ-41).
- Báo cáo tháng (REQ-42).
- Yêu cầu phi chức năng, ràng buộc và giao tiếp ngoài (REQ-01, REQ-43 đến REQ-46).

Ngoài phạm vi:
- SMS Gateway của nhà mạng: hệ thống khác, hệ thống này chỉ gửi yêu cầu qua API (nguồn: mục 14, "dùng dịch vụ SMS Gateway của nhà mạng qua API có sẵn").

## 3. Các bên liên quan và người dùng

| SH | Bên liên quan | Loại | Quan tâm chính, lợi ích | Tương tác trực tiếp với hệ thống (Có / Không / Chưa rõ) | REQ |
|---|---|---|---|---|---|
| SH-01 | Phòng khám (ban điều hành phòng khám đa khoa) | Chủ sở hữu, người đặt hàng | Giảm trùng lịch, giảm bệnh nhân không đến | Không | REQ-01 |
| SH-02 | Bệnh nhân | Người dùng trực tiếp | Xem lịch trống, đặt và hủy lịch khám, nhận SMS | Có | REQ-02 đến REQ-12, REQ-19, REQ-20, REQ-45 |
| SH-03 | Lễ tân | Người dùng trực tiếp | Xác nhận, từ chối, hủy lịch, đặt lịch hộ, check-in, đánh dấu không đến | Có | REQ-14 đến REQ-17, REQ-21 đến REQ-25, REQ-27, REQ-28, REQ-37 |
| SH-04 | Bác sĩ | Người dùng trực tiếp | Xem lịch hẹn theo ngày, ghi kết luận, đăng ký lịch làm việc, khoá khung giờ | Có | REQ-31 đến REQ-36, REQ-45 |
| SH-05 | SMS Gateway của nhà mạng | Hệ thống hoặc thiết bị ngoài | Nhận yêu cầu gửi SMS | Có | REQ-08, REQ-18, REQ-26, REQ-46 |
| SH-06 | Bệnh nhân đặt lịch qua điện thoại (nhiều người lớn tuổi) | Người hưởng lợi gián tiếp | Có lịch khám mà không cần tự thao tác trên hệ thống | Không | REQ-22, REQ-23 |
| SH-07 | Quản trị viên | Người vận hành, quản trị | Quản lý chuyên khoa, tài khoản nhân viên, tham số | Có | REQ-38 đến REQ-41 |
| SH-08 | Quản lý phòng khám | Người dùng trực tiếp | Xem báo cáo lịch hẹn và tỷ lệ không đến hằng tháng | Có | REQ-42 |

## 4. Danh sách yêu cầu

| REQ | Nội dung chuẩn hoá | Loại | Trích nguồn | Ghi chú |
|---|---|---|---|---|
| REQ-01 | Giải pháp phải là phần mềm web. | Ràng buộc | "Phòng khám cần một phần mềm web để quản lý việc đặt lịch khám." (đoạn mở đầu) | Không có |
| REQ-02 | Bệnh nhân có thể xem danh sách chuyên khoa mà không cần đăng nhập. | Chức năng | "Bệnh nhân có thể xem danh sách chuyên khoa ... mà không cần đăng nhập." (mục 1) | Tách từ cùng câu với REQ-03, REQ-04 |
| REQ-03 | Bệnh nhân có thể xem danh sách bác sĩ theo chuyên khoa mà không cần đăng nhập. | Chức năng | "... danh sách bác sĩ theo chuyên khoa ..." (mục 1) | Tách từ cùng câu với REQ-02 |
| REQ-04 | Bệnh nhân có thể xem lịch trống của từng bác sĩ mà không cần đăng nhập. | Chức năng | "... lịch trống của từng bác sĩ trong 14 ngày tới mà không cần đăng nhập." (mục 1) | Tách từ cùng câu với REQ-02 |
| REQ-05 | Lịch trống của bác sĩ được xem trong phạm vi 14 ngày tới. | Quy tắc nghiệp vụ | "... lịch trống của từng bác sĩ trong 14 ngày tới ..." (mục 1) | Tách từ REQ-04. Q-06 |
| REQ-06 | Bệnh nhân phải có tài khoản để đặt lịch khám. | Quy tắc nghiệp vụ | "Để đặt lịch, bệnh nhân phải có tài khoản." (mục 2) | Không có |
| REQ-07 | Bệnh nhân có thể tự đăng ký tài khoản bằng số điện thoại. | Chức năng | "Bệnh nhân tự đăng ký tài khoản bằng số điện thoại" (mục 2) | Q-13 |
| REQ-08 | Hệ thống gửi mã OTP qua SMS để xác thực số điện thoại khi bệnh nhân đăng ký tài khoản. | Chức năng | "hệ thống gửi mã OTP qua SMS để xác thực số điện thoại." (mục 2) | Kênh gửi là REQ-46. Xếp Chức năng thay vì Giao tiếp ngoài vì câu mô tả hành vi xác thực, không mô tả giao diện với SMS Gateway |
| REQ-09 | Bệnh nhân có thể đặt lịch khám bằng cách chọn chuyên khoa, bác sĩ, ngày, khung giờ còn trống và nhập lý do khám. | Chức năng | "Khi đặt lịch, bệnh nhân chọn chuyên khoa, bác sĩ (...), ngày và khung giờ 30 phút còn trống, nhập lý do khám." (mục 3) | Không có |
| REQ-10 | Bệnh nhân có thể để phòng khám tự phân bác sĩ thay vì tự chọn bác sĩ khi đặt lịch khám. | Chức năng | "bác sĩ (hoặc để phòng khám tự phân bác sĩ)" (mục 3) | Q-01 |
| REQ-11 | Mỗi khung giờ khám dài 30 phút. | Quy tắc nghiệp vụ | "khung giờ 30 phút còn trống" (mục 3) | Q-19 |
| REQ-12 | Mỗi bệnh nhân không được có quá 2 lịch hẹn chưa diễn ra cùng lúc. | Quy tắc nghiệp vụ | "Mỗi bệnh nhân không được có quá 2 lịch hẹn chưa diễn ra cùng lúc." (mục 3) | Q-07 |
| REQ-13 | Lịch hẹn do bệnh nhân vừa đặt có trạng thái "Chờ xác nhận". | Quy tắc nghiệp vụ | "Lịch hẹn vừa đặt ở trạng thái 'Chờ xác nhận'." (mục 4) | Không có |
| REQ-14 | Lễ tân có thể xem các lịch hẹn ở trạng thái "Chờ xác nhận". | Chức năng | "Lễ tân xem các lịch chờ" (mục 4) | Không có |
| REQ-15 | Lễ tân có thể xác nhận lịch hẹn đang chờ xác nhận. | Chức năng | "... và xác nhận hoặc từ chối" (mục 4) | Tách từ cùng câu với REQ-16 |
| REQ-16 | Lễ tân có thể từ chối lịch hẹn đang chờ xác nhận. | Chức năng | "... xác nhận hoặc từ chối (phải ghi lý do từ chối)" (mục 4) | Tách từ cùng câu với REQ-15 |
| REQ-17 | Lễ tân phải ghi lý do khi từ chối lịch hẹn. | Quy tắc nghiệp vụ | "(phải ghi lý do từ chối)" (mục 4) | Tách từ REQ-16 |
| REQ-18 | Hệ thống gửi SMS thông báo cho bệnh nhân khi lịch hẹn được xác nhận hoặc bị từ chối. | Chức năng | "Khi lịch được xác nhận hoặc bị từ chối, hệ thống gửi SMS thông báo cho bệnh nhân." (mục 4) | Q-10. Chưa tách xác nhận và từ chối vì nguồn không phân biệt |
| REQ-19 | Bệnh nhân có thể hủy lịch hẹn của mình. | Chức năng | "Bệnh nhân có thể hủy lịch hẹn của mình" (mục 5) | Không có |
| REQ-20 | Bệnh nhân chỉ được hủy lịch hẹn trước giờ khám ít nhất 4 tiếng. | Quy tắc nghiệp vụ | "... trước giờ khám ít nhất 4 tiếng." (mục 5) | Q-12 |
| REQ-21 | Lễ tân có thể hủy lịch hẹn khi còn dưới 4 tiếng trước giờ khám. | Chức năng | "Sau thời điểm đó chỉ lễ tân mới hủy được." (mục 5) | Q-09 |
| REQ-22 | Lễ tân có thể đặt lịch khám thay cho bệnh nhân gọi điện thoại. | Chức năng | "Lễ tân có thể đặt lịch thay cho bệnh nhân gọi điện" (mục 6) | Không có |
| REQ-23 | Lễ tân có thể tạo hồ sơ bệnh nhân khi bệnh nhân gọi điện chưa có tài khoản. | Chức năng | "nếu bệnh nhân chưa có tài khoản, lễ tân tạo hồ sơ bệnh nhân" (mục 6) | Q-11 |
| REQ-24 | Hồ sơ bệnh nhân do lễ tân tạo gồm họ tên, ngày sinh, số điện thoại. | Dữ liệu | "... hồ sơ bệnh nhân với họ tên, ngày sinh, số điện thoại." (mục 6) | Tách từ REQ-23 |
| REQ-25 | Lịch hẹn do lễ tân đặt được xác nhận ngay khi đặt. | Quy tắc nghiệp vụ | "Lịch do lễ tân đặt được xác nhận ngay." (mục 6) | Q-10 |
| REQ-26 | Vào 18 giờ mỗi ngày, hệ thống tự động gửi SMS nhắc lịch cho các bệnh nhân có lịch hẹn đã xác nhận vào ngày hôm sau. | Chức năng | "Vào 18 giờ mỗi ngày, hệ thống tự động gửi SMS nhắc lịch ..." (mục 7) | Không có |
| REQ-27 | Lễ tân có thể ghi nhận bệnh nhân đã đến phòng khám (check-in). | Chức năng | "Khi bệnh nhân đến phòng khám, lễ tân ghi nhận bệnh nhân đã đến (check-in)." (mục 8) | Q-18 |
| REQ-28 | Lễ tân có thể đánh dấu lịch hẹn là "Không đến". | Chức năng | "lễ tân đánh dấu 'Không đến'" (mục 8) | Không có |
| REQ-29 | Lịch hẹn chỉ được đánh dấu "Không đến" khi đã quá giờ hẹn 30 phút mà bệnh nhân không đến. | Quy tắc nghiệp vụ | "Nếu quá giờ hẹn 30 phút mà bệnh nhân không đến" (mục 8) | Tách từ REQ-28 |
| REQ-30 | Bệnh nhân bị đánh dấu "Không đến" 3 lần trong 6 tháng bị khoá chức năng tự đặt lịch trực tuyến. | Quy tắc nghiệp vụ | "Bệnh nhân bị đánh dấu 'Không đến' 3 lần trong 6 tháng sẽ bị khoá chức năng tự đặt lịch trực tuyến." (mục 8) | Q-04, Q-08 |
| REQ-31 | Bác sĩ có thể xem danh sách lịch hẹn của mình theo ngày. | Chức năng | "Bác sĩ xem danh sách lịch hẹn của mình theo ngày." (mục 9) | Không có |
| REQ-32 | Bác sĩ có thể ghi kết luận khám vào lịch hẹn sau khi khám. | Chức năng | "Sau khi khám, bác sĩ ghi kết luận khám ngắn (...) vào lịch hẹn" (mục 9) | Không có |
| REQ-33 | Kết luận khám gồm chẩn đoán và lời dặn. | Dữ liệu | "kết luận khám ngắn (chẩn đoán, lời dặn)" (mục 9) | Tách từ REQ-32 |
| REQ-34 | Lịch hẹn chuyển sang trạng thái "Đã khám" khi bác sĩ ghi kết luận khám. | Quy tắc nghiệp vụ | "lịch hẹn chuyển sang 'Đã khám'." (mục 9) | Không có |
| REQ-35 | Bác sĩ có thể đăng ký lịch làm việc theo tuần gồm các buổi sáng, chiều trong tuần. | Chức năng | "Bác sĩ đăng ký lịch làm việc theo tuần (các buổi sáng/chiều trong tuần)." (mục 10) | Q-14 |
| REQ-36 | Bác sĩ có thể khoá một số khung giờ đột xuất. | Chức năng | "Bác sĩ có thể khoá một số khung giờ đột xuất" (mục 10) | Không có |
| REQ-37 | Hệ thống báo cho lễ tân khi bác sĩ khoá khung giờ đã có lịch hẹn, để lễ tân liên hệ bệnh nhân đổi lịch. | Chức năng | "nếu khung giờ đó đã có lịch hẹn, hệ thống báo cho lễ tân để liên hệ bệnh nhân đổi lịch." (mục 10) | Q-03, Q-05 |
| REQ-38 | Quản trị viên có thể quản lý chuyên khoa. | Chức năng | "Quản trị viên quản lý chuyên khoa" (mục 11) | Chưa tách thêm, sửa, xoá vì nguồn không phân biệt |
| REQ-39 | Quản trị viên có thể quản lý tài khoản bác sĩ. | Chức năng | "... tài khoản bác sĩ và lễ tân" (mục 11) | Chưa tách thao tác vì nguồn không phân biệt |
| REQ-40 | Quản trị viên có thể quản lý tài khoản lễ tân. | Chức năng | "... tài khoản bác sĩ và lễ tân" (mục 11) | Tách từ cùng câu với REQ-39 |
| REQ-41 | Quản trị viên có thể cấu hình các tham số, gồm số giờ tối thiểu được hủy lịch và số lần không đến tối đa. | Chức năng | "cấu hình các tham số (số giờ tối thiểu được hủy, số lần không đến tối đa)." (mục 11) | Liên quan REQ-20, REQ-30. Q-12 |
| REQ-42 | Quản lý phòng khám có thể xem báo cáo hàng tháng gồm số lịch hẹn theo chuyên khoa, số lịch hẹn theo bác sĩ và tỷ lệ không đến. | Chức năng | "Quản lý phòng khám xem báo cáo hàng tháng: số lịch hẹn theo chuyên khoa, theo bác sĩ, tỷ lệ không đến." (mục 12) | Q-15 |
| REQ-43 | Thao tác đặt lịch có thời gian phản hồi không quá 3 giây khi có 200 người dùng đồng thời. | Phi chức năng | "Hệ thống phải phản hồi thao tác đặt lịch trong không quá 3 giây với 200 người dùng đồng thời." (mục 13) | Q-17 |
| REQ-44 | Giao diện phải "dùng được" trên điện thoại. | Ràng buộc | "Giao diện phải dùng được trên điện thoại." (mục 13) | Q-16 |
| REQ-45 | Dữ liệu kết luận khám chỉ bác sĩ khám và chính bệnh nhân đó được xem. | Phi chức năng | "Dữ liệu kết luận khám chỉ bác sĩ khám và chính bệnh nhân được xem." (mục 13) | Chọn Phi chức năng (bảo mật) vì không rõ là chính sách tổ chức hay yêu cầu chất lượng. Q-02 |
| REQ-46 | Hệ thống trao đổi yêu cầu gửi SMS với SMS Gateway của nhà mạng qua API có sẵn để gửi tin nhắn cho bệnh nhân. | Giao tiếp ngoài | "Việc gửi SMS dùng dịch vụ SMS Gateway của nhà mạng qua API có sẵn." (mục 14) | Dùng cho REQ-08, REQ-18, REQ-26 |

## 5. Vấn đề chất lượng của tài liệu nguồn

| STT | Loại vấn đề | REQ liên quan | Bằng chứng (câu trích) | Hướng xử lý | Q / ASM |
|---|---|---|---|---|---|
| 1 | Mơ hồ | REQ-10 | "để phòng khám tự phân bác sĩ" | Hỏi ai phân và khi nào phân | Q-01 |
| 2 | Thiếu | REQ-45 | "chính bệnh nhân được xem" nhưng không có câu nào nói bệnh nhân xem kết luận khám hoặc lịch hẹn của mình | Hỏi có chức năng bệnh nhân xem không | Q-02 |
| 3 | Thiếu | REQ-37 | "liên hệ bệnh nhân đổi lịch" nhưng nguồn không mô tả chức năng đổi lịch | Hỏi đổi lịch làm trên hệ thống thế nào | Q-03 |
| 4 | Thiếu | REQ-30 | "bị khoá chức năng tự đặt lịch trực tuyến" nhưng không nói khi nào hoặc ai mở khoá | Hỏi cách mở khoá và cách tính 6 tháng | Q-04 |
| 5 | Thiếu | REQ-37 | "hệ thống báo cho lễ tân" không nêu kênh báo | Hỏi kênh báo | Q-05 |
| 6 | Mơ hồ | REQ-05 | "lịch trống ... trong 14 ngày tới" chỉ nói về xem, không nói về giới hạn đặt | Hỏi 14 ngày có là giới hạn đặt lịch không | Q-06 |
| 7 | Mơ hồ | REQ-12 | "lịch hẹn chưa diễn ra" | Hỏi phạm vi trạng thái và có áp dụng cho lễ tân đặt hộ không | Q-07 |
| 8 | Thiếu | REQ-30, REQ-22 | "khoá chức năng tự đặt lịch trực tuyến" | Hỏi lễ tân có được đặt hộ bệnh nhân bị khoá không | Q-08 |
| 9 | Mơ hồ | REQ-21 | "Sau thời điểm đó chỉ lễ tân mới hủy được" | Hỏi lễ tân có hủy được trước mốc 4 tiếng không, có gửi SMS khi hủy không | Q-09 |
| 10 | Mơ hồ | REQ-18, REQ-25 | "Lịch do lễ tân đặt được xác nhận ngay"; "Khi lịch được xác nhận ... hệ thống gửi SMS" | Hỏi lịch lễ tân đặt có gửi SMS xác nhận không | Q-10 |
| 11 | Thiếu | REQ-23, REQ-07 | "lễ tân tạo hồ sơ bệnh nhân" và "Bệnh nhân tự đăng ký tài khoản bằng số điện thoại" | Hỏi quan hệ giữa hồ sơ và tài khoản | Q-11 |
| 12 | Mơ hồ | REQ-41, REQ-20, REQ-30 | "cấu hình các tham số (số giờ tối thiểu được hủy, số lần không đến tối đa)" | Hỏi danh sách tham số là đầy đủ hay ví dụ; 4 tiếng và 3 lần có là giá trị mặc định không | Q-12 |
| 13 | Thiếu | REQ-07 | "Để đặt lịch, bệnh nhân phải có tài khoản"; "mà không cần đăng nhập" | Nguồn nhắc đăng nhập nhưng không nêu cách đăng nhập | Q-13 |
| 14 | Mơ hồ | REQ-35 | "các buổi sáng/chiều trong tuần" | Hỏi giờ của mỗi buổi và cách lặp lại | Q-14 |
| 15 | Mơ hồ | REQ-42 | "tỷ lệ không đến" | Hỏi công thức | Q-15 |
| 16 | Không kiểm chứng được | REQ-44 | "dùng được trên điện thoại" | Hỏi tiêu chí | Q-16 |
| 17 | Mơ hồ | REQ-43 | "phản hồi thao tác đặt lịch trong không quá 3 giây" | Hỏi cách đo | Q-17 |
| 18 | Thiếu | REQ-27, REQ-19 | Nguồn nêu trạng thái "Chờ xác nhận", "Không đến", "Đã khám" nhưng không nêu tên trạng thái sau khi check-in, sau khi hủy, sau khi từ chối | Hỏi tên trạng thái | Q-18 |
| 19 | Mơ hồ | REQ-11, REQ-09 | "khung giờ 30 phút còn trống" | Hỏi một khung giờ nhận mấy bệnh nhân | Q-19 |
| 20 | Không mâu thuẫn, quan hệ tham số | REQ-20, REQ-41 | "trước giờ khám ít nhất 4 tiếng" (mục 5); "số giờ tối thiểu được hủy" (mục 11) | Giữ cả hai REQ; xem Q-12 | Q-12 |

## 6. Ma trận phủ nguồn

| Vị trí trong nguồn | Tóm tắt nội dung | Kết luận (REQ-xx / Ngoài phạm vi / Bối cảnh) |
|---|---|---|
| Đoạn mở đầu, câu 1 | Phòng khám Minh An, 3 chuyên khoa, khoảng 12 bác sĩ | Bối cảnh |
| Đoạn mở đầu, câu 2 | Đặt lịch qua điện thoại, ghi sổ, trùng lịch, không đến | Bối cảnh (mục tiêu nghiệp vụ) |
| Đoạn mở đầu, câu 3 | Cần phần mềm web quản lý đặt lịch | REQ-01 |
| Mục 1 | Xem chuyên khoa, bác sĩ, lịch trống 14 ngày không cần đăng nhập | REQ-02, REQ-03, REQ-04, REQ-05 |
| Mục 2 | Phải có tài khoản; tự đăng ký bằng SĐT; OTP qua SMS | REQ-06, REQ-07, REQ-08 |
| Mục 3 | Đặt lịch: chọn chuyên khoa, bác sĩ hoặc tự phân, ngày, khung 30 phút, lý do; tối đa 2 lịch | REQ-09, REQ-10, REQ-11, REQ-12 |
| Mục 4 | Trạng thái Chờ xác nhận; lễ tân xác nhận, từ chối có lý do; SMS | REQ-13 đến REQ-18 |
| Mục 5 | Bệnh nhân hủy trước 4 tiếng; sau đó chỉ lễ tân | REQ-19, REQ-20, REQ-21 |
| Mục 6, câu 1 | Nhiều người lớn tuổi vẫn gọi điện | Bối cảnh |
| Mục 6, câu 2-3 | Lễ tân đặt hộ, tạo hồ sơ, xác nhận ngay | REQ-22 đến REQ-25 |
| Mục 7 | 18 giờ gửi SMS nhắc lịch hôm sau | REQ-26 |
| Mục 8 | Check-in, đánh dấu Không đến, khoá sau 3 lần/6 tháng | REQ-27 đến REQ-30 |
| Mục 9 | Bác sĩ xem lịch theo ngày, ghi kết luận, chuyển Đã khám | REQ-31 đến REQ-34 |
| Mục 10 | Đăng ký lịch làm việc tuần, khoá khung giờ, báo lễ tân | REQ-35, REQ-36, REQ-37 |
| Mục 11 | Quản trị chuyên khoa, tài khoản bác sĩ, lễ tân, tham số | REQ-38 đến REQ-41 |
| Mục 12 | Báo cáo tháng | REQ-42 |
| Mục 13 | 3 giây / 200 người dùng; dùng trên điện thoại; quyền xem kết luận | REQ-43, REQ-44, REQ-45 |
| Mục 14 | SMS Gateway qua API | REQ-46; phần SMS Gateway là hệ thống khác (Ngoài phạm vi) |

## Câu hỏi mở

| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ |
|---|---|---|---|
| Q-01 | Khi bệnh nhân để phòng khám tự phân bác sĩ, ai phân: hệ thống tự phân ngay lúc đặt, hay lễ tân phân khi xác nhận lịch? | REQ-10; danh sách chức năng của lễ tân; luồng của UC đặt lịch | Mục 3 |
| Q-02 | Bệnh nhân có được xem danh sách lịch hẹn và kết luận khám của mình trên hệ thống không? (Có / Không) | REQ-45; danh sách chức năng của bệnh nhân | Mục 13 |
| Q-03 | Khi bác sĩ khoá khung giờ đã có lịch hẹn, lễ tân đổi lịch trên hệ thống bằng cách nào: đổi khung giờ của lịch hẹn cũ, hay hủy rồi đặt lịch mới? | REQ-37; danh sách chức năng của lễ tân | Mục 10 |
| Q-04 | Bệnh nhân bị khoá tự đặt lịch được mở khoá thế nào (tự động hết 6 tháng / quản trị viên mở / không mở)? "6 tháng" tính theo 6 tháng gần nhất tính tới lần đánh dấu mới nhất? | REQ-30; chức năng quản trị | Mục 8 |
| Q-05 | Hệ thống báo cho lễ tân về khung giờ bị khoá qua kênh nào (thông báo trong hệ thống / SMS / khác)? | REQ-37 | Mục 10 |
| Q-06 | Giới hạn 14 ngày tới có đồng thời là giới hạn ngày được đặt lịch không? Có áp dụng cho lễ tân đặt hộ không? | REQ-05, REQ-09, REQ-22 | Mục 1 |
| Q-07 | "Lịch hẹn chưa diễn ra" có tính lịch "Chờ xác nhận" không? Giới hạn 2 lịch có áp dụng khi lễ tân đặt hộ không? | REQ-12, REQ-22 | Mục 3 |
| Q-08 | Bệnh nhân bị khoá tự đặt lịch có còn được lễ tân đặt lịch hộ không? (Có / Không) | REQ-30, REQ-22 | Mục 8 |
| Q-09 | Lễ tân có được hủy lịch hẹn trước mốc 4 tiếng không? Khi lịch bị hủy, hệ thống có gửi SMS cho bệnh nhân không? | REQ-21 | Mục 5 |
| Q-10 | Lịch hẹn do lễ tân đặt (xác nhận ngay) có gửi SMS xác nhận cho bệnh nhân không? (Có / Không) | REQ-18, REQ-25 | Mục 4, mục 6 |
| Q-11 | Khi bệnh nhân đã có hồ sơ do lễ tân tạo tự đăng ký tài khoản bằng cùng số điện thoại, tài khoản có gắn với hồ sơ cũ không? (Có / Không) | REQ-07, REQ-23 | Mục 2, mục 6 |
| Q-12 | Danh sách tham số cấu hình ở mục 11 là đầy đủ hay ví dụ? 4 tiếng và 3 lần có phải giá trị hiện hành của hai tham số đó không? | REQ-20, REQ-30, REQ-41 | Mục 11 |
| Q-13 | Bệnh nhân đăng nhập bằng gì (số điện thoại và mật khẩu / mã OTP mỗi lần)? | REQ-06, REQ-07 | Mục 1, mục 2 |
| Q-14 | Mỗi buổi sáng, chiều gồm những giờ nào? Lịch làm việc đăng ký cho từng tuần hay lặp lại mọi tuần? | REQ-35 | Mục 10 |
| Q-15 | "Tỷ lệ không đến" tính bằng số lịch "Không đến" chia cho tổng số lịch nào? | REQ-42 | Mục 12 |
| Q-16 | Tiêu chí "dùng được trên điện thoại" là gì (kích thước màn hình tối thiểu, trình duyệt nào)? | REQ-44 | Mục 13 |
| Q-17 | 3 giây đo từ lúc gửi yêu cầu đặt lịch tới lúc nhận kết quả, áp dụng cho bao nhiêu phần trăm yêu cầu? | REQ-43 | Mục 13 |
| Q-18 | Lịch hẹn có trạng thái gì sau khi check-in, sau khi bị hủy, sau khi bị từ chối? | REQ-16, REQ-19, REQ-27 | Mục 4, 5, 8 |
| Q-19 | Mỗi khung giờ 30 phút của một bác sĩ nhận tối đa mấy bệnh nhân? | REQ-09, REQ-11 | Mục 3 |

## Đề xuất sửa artifact trước

Không có

## Vấn đề còn mở

- Số REQ (46) vượt mức tham khảo 15-40 cho tài liệu nguồn khoảng 1 trang. Đã rà lại: không có REQ tách ở mức thao tác hoặc thuộc tính; số lượng do nguồn dày đặc quy tắc nghiệp vụ. Giữ nguyên.
- REQ-08, REQ-18, REQ-26 nhắc tới SMS nhưng được xếp Chức năng thay vì Giao tiếp ngoài (cây F3 câu 1 cho kết luận Giao tiếp ngoài nếu áp dụng đúng thứ tự). Lý do: các câu này mô tả hành vi nghiệp vụ; phần giao tiếp với SMS Gateway đã có REQ-46.
