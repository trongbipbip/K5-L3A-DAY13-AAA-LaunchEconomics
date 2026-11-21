# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Thiếu kiểm tra đầu vào / thao tác không đảo ngược được | ... | ... | ... |
| 2 | Gọi tool sai tham số | ... | ... | ... |
| 3 | Thiết kế sản phẩm / truyền thông kém | ... | ... | ... |
| 4 | Trợ lý xử lý đúng, chuyển người hợp lý | ... | ... | ... |
| 5 | Lỗi logic nghiệp vụ (tính sai tiền) | ... | ... | ... |
| 6 | Hiểu sai ý định / không có đường thoát | ... | ... | ... |
| 7 | Báo thành công giả hoặc bịa căn cứ | ... | ... | ... |
| 8 | Báo thành công giả hoặc bịa căn cứ | ... | ... | ... |
| 9 | Hiểu sai ý định / không có đường thoát | ... | ... | ... |
| 10 | Thiết kế sản phẩm / truyền thông kém | ... | ... | ... |
| 11 | Ngoài khả năng kênh (giọng nói) | ... | ... | ... |
| 12 | Dữ liệu cũ, lỗi âm thầm | ... | ... | ... |
| 13 | Hiểu sai ý định / không có đường thoát | ... | ... | ... |
| 14 | Thiếu kiểm tra đầu vào / thao tác không đảo ngược được | ... | ... | ... |
| 15 | Lỗi logic nghiệp vụ (tính sai tiền) | ... | ... | ... |
| 16 | Thiết kế sản phẩm / truyền thông kém | ... | ... | ... |
| 17 | Dữ liệu cũ, lỗi âm thầm | ... | ... | ... |
| 18 | Thiết kế sản phẩm / truyền thông kém | ... | ... | ... |
| 19 | Trợ lý xử lý đúng, chuyển người hợp lý | ... | ... | ... |
| 20 | Thiếu cơ chế chống trùng | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | Khách khiếu nại mở lại sau 2 ngày. Đối chiếu số tiền hoàn với bảng giá theo trọng lượng khi kiểm mẫu | Bắt buộc truyền trọng lượng và loại hàng vào tool. Thêm bước kiểm tra: hàng trên ngưỡng kg mà dùng giá thường thì chặn lại hoặc chuyển người | Kỹ sư tích hợp tool, kèm nhân viên kiểm mẫu |
| ... | Hệ thống | Tỉ lệ khách nhắn lại cùng đơn sau khi bị từ chối. Đọc mẫu hội thoại bị từ chối theo luồng giao trễ | Phân loại theo nội dung tin nhắn, không chỉ theo mục khách chọn. Nếu mục chọn và nội dung lệch nhau thì hỏi lại hoặc chuyển người | Người thiết kế luồng hội thoại, kèm trưởng nhóm chăm sóc khách hàng |
| ... | Ngữ cảnh | Đối chiếu danh sách "đã báo hoàn" với sổ ghi hoàn tiền. Cảnh báo khi tỉ lệ lỗi 5xx tăng | Chỉ báo thành công khi tool trả mã thành công. Nếu lỗi thì nói thật "đang xử lý" và chuyển nhân viên, kèm cảnh báo tự động | Kỹ sư backend (xử lý lỗi), nhân viên trực xử lý hồ sơ treo |
| ... | Giới hạn hệ thống | Kiểm mẫu định kỳ, so giá trợ lý dùng với bảng giá hiện hành. Cảnh báo khi phiên bản bảng giá trong bộ nhớ đệm khác phiên bản gốc | Xóa hoặc làm mới bộ nhớ đệm mỗi khi bảng giá đổi. Gắn mã phiên bản vào bảng giá và kiểm tra trước mỗi lần tính. Hoàn bù cho 212 đơn | Kỹ sư dữ liệu (đồng bộ bảng giá), tài chính (đối soát) |
| ... | Ngầm | Báo cáo đối soát: một mã đơn có hơn một lệnh hoàn. Cảnh báo khi cùng mã đơn bị hoàn lần hai | Thêm khóa chống trùng (mã đơn + loại hoàn) để lệnh thứ hai bị từ chối. Cho khách thấy trạng thái "đang xử lý" để họ không gửi lại | Kỹ sư backend, tài chính theo dõi đối soát |
