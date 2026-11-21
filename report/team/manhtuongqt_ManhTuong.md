# Báo cáo cá nhân — ManhTuong-manhtuongqt

## 1. Thông tin thành viên

- Họ tên: Mạnh Tường
- MSSV: (Cập nhật MSSV)
- Email: manhtuongqt@users.noreply.github.com
- Vai trong nhóm: Người kiểm số / Pilot Analyst (Thành viên 2)

## 2. Phần việc phụ trách

- **Giai đoạn CP1 & CP2:** Người kiểm số (Verification). Kiểm tra, tính toán độc lập và đối chiếu chéo số liệu do Người viết code (Thành viên 1) thực hiện trên 2 file dữ liệu gốc `logix_runs.csv` và `logix_requests.csv`. Đảm bảo đáp ứng đầy đủ tiêu chí rubric (sai số $\le 2\%$, gắn nhãn `simulated`, câu trả lời $\le 3$ dòng và có số liệu cụ thể).
- **Giai đoạn CP4:** Pilot Analyst. Chủ trì phân tích cỡ mẫu và hệ số thiết kế (DE) cho thử nghiệm RCT cụm (Cluster Randomized Trial), xác định tính nhận diện (Identifiability), thiết kế 3 quy tắc dừng (Stop Rules) và hoàn thiện `report/team/pilot_plan.yaml`.
- **Giai đoạn CP5 & Gate 2a:** Hỗ trợ Thành viên 4 hoàn thiện Hồ sơ Launch v0, tham gia bảo vệ phương án thử nghiệm pilot trước hội đồng phản biện.

## 3. Đóng góp cụ thể

- Chạy script tính toán độc lập từ dữ liệu gốc, xác nhận kết quả CP1 của Người 1 đạt 100%:
  - Ba phép thử A1 đạt chuẩn ($1,20 \cdot 1,25 \cdot 1,25$).
  - A2: Token (245.585 đ), Tool (84.000 đ), Lần chạy 2 & 3 (93.804 đ), Xem lại (1.780.000 đ [simulated]), Làm lại (2.264.000 đ [simulated]), Tổng (4.373.585 đ), Số việc thành công (978), CPS (4.472 đ [simulated], gấp 16,3 lần hóa đơn token). Chi phí cả hệ thống: 5.865 đ/yc = 0,49× baseline [simulated].
  - A3: Tách 4 loại yêu cầu (`noi_dia` 0,22×, `hang_nang` 0,69×, `quoc_te` 1,88×, `doi_tac` 0,85×). Xác nhận loại `quoc_te` chạy lại không cải thiện tỉ lệ thành công (lần 1: 30%, lần 2: 11,4%, lần 3: 2,2%).
  - A4: Chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (1.185 đ ở 45k yc/tháng, 2.370 đ ở nửa quy mô).
- Nghiệm thu tính hợp lệ của `report/team/bang_chi_phi.md`.
- Hỗ trợ Thành viên 4 điền trước Mục 1 và Mục 3 trong `report/team/ho_so_launch_v0.md`.

## 4. Bằng chứng

- Script tính toán độc lập từ CSV và log kiểm tra số liệu CP1.
- `TEAM.md`: Bảng phân vai 4 roles và nhiệm vụ chi tiết.
- `report/team/ho_so_launch_v0.md`: Mục 1 và Mục 3 đã cập nhật số liệu chuẩn.
- Các commit kiểm tra và cập nhật tài liệu trên repo `K5-L3A-DAY13-AAA-LaunchEconomics`.

## 5. Công cụ AI đã dùng

- Trợ lý AI (Antigravity): Dùng để viết script kiểm tra số liệu độc lập, đối chiếu rubric và rà soát các quy tắc kiểm duyệt (không dùng từ "production", gắn nhãn `simulated`).
- Tự kiểm tra: Toàn bộ con số đều được tính toán lại trực tiếp từ dữ liệu CSV bằng Python, không sao chép thụ động.

## 6. Tự đánh giá

- Hoàn thành xuất sắc vai trò Người kiểm số ở CP1 (xác nhận độ chính xác 100%, bảo toàn 20/20 điểm cho nhóm).
- Phối hợp và bàn giao kịp thời các dữ liệu đầu vào cho các thành viên khác trong nhóm.
