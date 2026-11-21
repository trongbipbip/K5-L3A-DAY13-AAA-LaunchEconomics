# Báo cáo nhóm

Báo cáo tóm tắt quá trình thực hiện Lab 13. Các số liệu tính từ các cột có hậu tố `_simulated` được ghi nhãn `simulated`.

## 1. Thông tin nhóm

- Tên nhóm: AAA
- Lớp: L3A
- Repo: `K5-L3A-DAY13-AAA-LaunchEconomics`
- Thành viên và vai trò: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá trợ lý hoàn phí LogiX-VN trước khi đề xuất một pilot có kiểm soát. Cách tiếp cận gồm bốn phần: tính chi phí thật từ trace, phân tích độ nhạy kinh tế, phân loại lỗi theo nguyên nhân gốc và thiết kế pilot có nhóm đối chứng, cỡ mẫu cùng luật dừng.

Nhóm ưu tiên các kết luận có thể kiểm tra lại từ `src/lab13.py`, hai file CSV và các bảng trong `report/team/`. Các số giả lập không được dùng như ground truth thực tế.

## 3. Giải pháp

- **CP1 — Chi phí:** Hải Tuấn hoàn thiện `src/lab13.py`; Mạnh Tường kiểm tra độc lập; nhóm điền [bang_chi_phi.md](bang_chi_phi.md).
- **CP2 — Độ nhạy:** nhóm chạy các kịch bản thay đổi giá token, xem lại, làm lại, lương và giới hạn số lần chạy; kết quả được ghi trong [bang_chi_phi.md](bang_chi_phi.md).
- **CP3 — Lỗi:** Phan Văn Diện và Nguyễn Nho Trọng gắn nhãn độc lập 20 ca; nhóm thống nhất nhãn, quy tắc phân biệt và bảng khắc phục trong [bang_loi.md](bang_loi.md).
- **CP4 — Pilot:** Mạnh Tường chủ trì D1/D2 và hoàn thiện [pilot_plan.yaml](pilot_plan.yaml); Hải Tuấn hỗ trợ tính cỡ mẫu và tỉ lệ mở lại.
- **CP5 — Hồ sơ:** nhóm đã hoàn thiện [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md); [phieu_cham.md](phieu_cham.md) chờ thông tin hồ sơ của nhóm được phân công chấm.

## 4. Kết quả

### CP1–CP2

- Ba phép thử A1 đạt: `1,20`, `1,25`, `1,25`.
- Chi phí mỗi việc thành công: **4.472 đ [simulated]**.
- Chi phí toàn hệ thống: **5.865 đ/yêu cầu = 0,49×** chi phí nhân viên [simulated].
- Làm lại là yếu tố nhạy nhất: **+51,8%**; xem lại: **+40,7%**; lương nhân viên: **+23,1%** [simulated].
- Giới hạn 2 lần chạy rẻ nhất cho toàn hệ thống: **6.901.220 đ**; giới hạn 1 lần có CPS thấp nhất nhưng đẩy nhiều việc hơn sang nhân viên.
- `quoc_te` có CPS **22.515 đ = 1,88×** nhân viên, nên được loại khỏi phạm vi pilot ban đầu [simulated].

### CP3–CP4

- CP3 đạt **19/20 = 95%** đồng thuận; đủ 5 loại lỗi và bảng khắc phục có cách phát hiện đo được.
- CP4 chọn chia theo nhân viên: **20 nhân viên nhóm can thiệp + 20 nhân viên đối chứng**.
- Với MDE 6 điểm: **859 yêu cầu mỗi nhóm**, tối thiểu **299 yêu cầu mỗi nhân viên**, hệ số thiết kế **6,96**.
- Tỉ lệ mở lại trong 7 ngày hiện tại: **4,25%** toàn bộ và **3,97%** trong phạm vi `noi_dia + hang_nang` [simulated].
- Kế hoạch có 3 luật dừng về an toàn, chi phí và mức độ sử dụng; có rollback về luồng nhân viên.

Đề xuất trong hồ sơ launch là **Go có điều kiện** cho pilot `noi_dia + hang_nang`; nhóm chưa đưa `quoc_te` vào pilot vì CPS **22.515 đ = 1,88×** nhân viên [simulated].

## 5. Khó khăn và cách xử lý

- **Thiếu thư viện `statsmodels`:** lệnh chạy ban đầu dừng ở D1; nhóm cài bổ sung thư viện rồi chạy lại thành công.
- **Dễ tính thiếu chi phí:** nhóm kiểm tra để tử số gồm mọi lần chạy, kể cả lần lỗi, và mẫu số chỉ gồm việc thành công.
- **Ảnh hưởng của dữ liệu giả lập:** mọi số từ các cột `_simulated` được gắn nhãn trong báo cáo.
- **Phân loại lỗi dễ nhầm:** hai người gắn nhãn độc lập trước khi so sánh; ca 13 được thống nhất là giới hạn hệ thống vì nằm ngoài phạm vi trợ lý.
- **Cỡ mẫu không đủ cho mức chênh 5 điểm:** nhóm ghi rõ đánh đổi sang MDE 6 điểm thay vì che giấu hạn chế.

## 6. Tổng hợp đóng góp

- **Hải Tuấn — Người viết code / Economics Engineer:** viết và chạy mô hình CP1–CP2; hỗ trợ tính D1 và kiểm tra output CP4. Bằng chứng chính: các commit `45b1560`, `ab3a3c8`, `c3663d2`.
- **Nguyễn Mạnh Tường — Người kiểm số / Pilot Analyst:** kiểm tra độc lập CP1–CP2; chủ trì D1, D2, luật dừng và `pilot_plan.yaml`. Bằng chứng chính: các commit `e6fa332`, `a56a328` và báo cáo cá nhân.
- **Phan Văn Diện — Người gắn nhãn lỗi 1 / Error Analyst:** tạo bộ nhãn độc lập thứ nhất cho CP3 và theo dõi điều kiện hoàn thành. Bằng chứng chính: commit `5b6bb0f`.
- **Nguyễn Nho Trọng — Người gắn nhãn lỗi 2 kiêm giữ hồ sơ / Launch Owner:** tạo bộ nhãn độc lập thứ hai, tổng hợp CP3 và cập nhật hồ sơ theo tiến độ. Bằng chứng chính: commit `d47332c` sửa `bang_loi.md`, cùng các commit đồng bộ nhánh của tài khoản `trongbipbip`.

Chi tiết đóng góp cá nhân nằm trong các file `MSSV_HoTen.md` đã đổi tên trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu trong lab là giả lập và đợt chạy thử ban đầu không có nhóm đối chứng; chưa được kết luận tác động nhân quả.
- Phút xem lại và làm lại là dữ liệu `simulated`; pilot cần thay bằng thời gian đo thật.
- Với 40 nhân viên, thiết kế không đủ power 0,80 cho mức chênh 5 điểm; cần tăng số cụm, kéo dài thời gian hoặc chấp nhận MDE lớn hơn.
- `phieu_cham.md` chỉ được hoàn thiện sau khi nhóm nhận hồ sơ của nhóm được phân công chấm; hiện chưa có bằng chứng về nhóm được phân công và điểm chấm nên nhóm không tự bịa kết quả.

## 8. Tài liệu tham khảo

- `README.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `RULES.md` và `SUBMISSION.md` của Lab 13.
- `docs/du_lieu_va_cong_thuc.md`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Google PAIR, *People + AI Guidebook*, chương “Errors + Graceful Failure”.
- Tài liệu `statsmodels` về `NormalIndPower`.
