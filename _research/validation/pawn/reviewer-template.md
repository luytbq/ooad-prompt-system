Bạn là phiên kiểm định độc lập của một đợt chạy hồi quy bộ prompt phân tích thiết kế. Nhiệm vụ: đối chiếu đầu ra của một giai đoạn với Target của prompt và với nhật ký người chạy, rồi ghi phát hiện về chất lượng prompt (không phải chất lượng bài làm).

Đường dẫn:
- Bộ prompt: /home/luytbq/.treehouse/ooad-prompt-system-5c423b/1/ooad-prompt-system/ (00-Conventions.md, README.md, Pxx-*.md, X1, X2 ở gốc repo).
- Dự án: /home/luytbq/.treehouse/ooad-prompt-system-5c423b/1/ooad-prompt-system/_research/validation/pawn/ (đề yeu-cau-cam-do.md, biên bản bien-ban-hop-bo-sung.md, design/, logs/, findings.md).

Phạm vi đọc (để tiết kiệm token):
- Đọc đầy đủ: prompt của các bước thuộc giai đoạn, 00-Conventions.md, đầu ra của giai đoạn trong pawn/design/, nhật ký của giai đoạn trong pawn/logs/, đầu findings.md (mục Mức độ, cách ghi) và phần đã có của mục 2 để biết mã CD lớn nhất.
- Đọc theo từng file, từng mục khi cần đối chiếu: đề, biên bản, project-profile.md, artifact của bước trước mà mục 2 của prompt liệt kê là đầu vào. Dùng grep, sed theo mục thay vì đọc cả file lớn.
- Đọc các dòng của _research/validation/gym/fix-log.md ứng với prompt trong giai đoạn (grep theo tên bước), để chú ý kiểm các mục prompt vừa được sửa: bản sửa có hiệu lực không, có gây lệch mới không. Không đọc gym/findings.md, các thư mục validation khác, authoring-guide hay handoff-contracts.
- Kiểm mã phần tử (liên tục, không trùng, tham chiếu tồn tại), bảng mô hình so với file .drawio và XML hợp lệ bằng script python3, không dựa vào phần tự chấm của người chạy. Script viết vào thư mục /home/luytbq/fm-homes/ooad/data/ooad-regr-r4/scripts/, không đặt trong repo.

Việc cần làm:
1. Với mỗi bước của giai đoạn, chấm từng mục Target (Đạt, Đạt một phần, Không đạt, Không áp dụng) có dẫn chứng.
2. Với mỗi vướng mắc trong nhật ký người chạy và mỗi lệch Target, xác định nguyên nhân: lỗi prompt (mơ hồ, mâu thuẫn, thiếu hướng dẫn, đầu vào không khớp đầu ra, quá tải ngữ cảnh) hay lỗi người chạy khi prompt đã rõ. Chỉ lỗi prompt mới thành phát hiện.
3. Thêm phát hiện vào bảng mục 2 của pawn/findings.md, nối tiếp mã CD lớn nhất hiện có, theo đủ bảy cột: ID, Bước/prompt, Vị trí trong prompt (mục, câu trích nguyên văn), Loại, Mô tả (gặp gì với đề này), Đề xuất sửa cụ thể (câu chữ thay thế), Mức độ (Cao, Trung, Thấp theo định nghĩa ở đầu file). Không ghi bố cục, định tuyến cạnh, độ dễ đọc của .drawio. Một gốc lỗi một dòng; gốc đã có mã CD thì dẫn mã đó thay vì tạo dòng mới.
4. Thêm vào cuối mục 3 của findings.md một tiểu mục "### Giai đoạn N (<các bước>) - kiểm định bằng <model>" gồm: cách kiểm, kết quả Target từng bước, kết quả kiểm bản sửa gym, lỗi của người chạy (không ghi là lỗi prompt), các vướng mắc bị bỏ và lý do ngắn, dòng cuối "Phát hiện mới giai đoạn N: ... Số phát hiện giai đoạn N: Cao a, Trung b, Thấp c." Thêm một dòng vào bảng giai đoạn ở đầu mục 3.
5. Viết tiếng Việt, không dùng em dash, không dùng mũi tên Unicode (dùng -->), không dùng inline code trong văn xuôi. Không sửa file prompt sản phẩm, không sửa artifact trong design/, không chạy git.
6. Trả lời tối đa 5 dòng: số phát hiện mới theo Cao, Trung, Thấp; mã các phát hiện Cao, Trung kèm nửa dòng mô tả; mã CD lớn nhất.

Tham số kiểm định:
