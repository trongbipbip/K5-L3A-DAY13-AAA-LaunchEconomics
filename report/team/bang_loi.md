# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1 (Thành viên 3): Phan Văn Diện · Người gắn nhãn 2 (Thành viên 4): Nguyễn Nho Trọng (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Thiếu kiểm tra đầu vào / thao tác không đảo ngược được | Người dùng nhập sai thông tin tài khoản | Có | Do người dùng |
| 2 | Gọi tool sai tham số | Chọn sai loại hàng khi tra bảng giá | Có | Hệ thống |
| 3 | Thiết kế sản phẩm / truyền thông kém | Kết quả đúng thiết kế nhưng không khớp kỳ vọng nhận tiền của khách | Có | Ngữ cảnh |
| 4 | Trợ lý xử lý đúng, chuyển người hợp lý | Ngoài phạm vi dữ liệu nên không thể xác định trạng thái | Có | Giới hạn hệ thống |
| 5 | Lỗi logic nghiệp vụ (tính sai tiền) | Sai tiền hoàn do dữ liệu mã giảm giá nhưng không ai nhận ra | Có | Ngầm |
| 6 | Hiểu sai ý định / không có đường thoát | Người dùng chọn sai mục, hệ thống không nhận ra ý định thật | Có | Do người dùng |
| 7 | Báo thành công giả hoặc bịa căn cứ | Báo đã hoàn tiền dù ghi sổ cái thất bại | Có | Hệ thống |
| 8 | Báo thành công giả hoặc bịa căn cứ | Hiển thị căn cứ chính sách không tồn tại | Có | Hệ thống |
| 9 | Hiểu sai ý định / không có đường thoát | Không nhận diện mã đơn của sàn và không hướng dẫn thay thế | Có | Do người dùng |
| 10 | Thiết kế sản phẩm / truyền thông kém | Áp dụng đúng chính sách nhưng thông điệp cam kết tạo kỳ vọng trái ngược | Có | Ngữ cảnh |
| 11 | Ngoài khả năng kênh (giọng nói) | Đầu vào âm thanh nằm ngoài khả năng xử lý của hệ thống | Có | Giới hạn hệ thống |
| 12 | Dữ liệu cũ, lỗi âm thầm | Dữ liệu depot thiếu trường làm chi phí tăng âm thầm | Có | Ngầm |
| 13 | Hiểu sai ý định / không có đường thoát | Yêu cầu ngoài phạm vi nhưng không chuyển rõ ràng cho nhân viên | Không | Giới hạn hệ thống |
| 14 | Thiếu kiểm tra đầu vào / thao tác không đảo ngược được | Người dùng xác nhận nhầm khiến yêu cầu bị đóng | Có | Do người dùng |
| 15 | Lỗi logic nghiệp vụ (tính sai tiền) | Tính sai mức hoàn theo chính sách | Có | Hệ thống |
| 16 | Thiết kế sản phẩm / truyền thông kém | Gửi thông báo đúng thiết kế nhưng sai thời điểm với hoàn cảnh khách | Có | Ngữ cảnh |
| 17 | Dữ liệu cũ, lỗi âm thầm | Cache bảng giá cũ gây lệch tiền mà không bị phát hiện | Có | Ngầm |
| 18 | Thiết kế sản phẩm / truyền thông kém | Tính đúng nhưng thiếu cách giải thích khiến khách hiểu sai | Có | Ngữ cảnh |
| 19 | Trợ lý xử lý đúng, chuyển người hợp lý | Dữ liệu quá cũ nên hệ thống không thể tra cứu | Có | Giới hạn hệ thống |
| 20 | Thiếu cơ chế chống trùng | Thiếu khóa chống trùng gây hoàn tiền hai lần | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 13: Nếu yêu cầu nằm ngoài phạm vi dữ liệu hoặc sản phẩm mà trợ lý không thể xử lý, nguyên nhân gốc là **Giới hạn hệ thống**; việc chuyển nhân viên không rõ ràng là phần cần khắc phục.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
