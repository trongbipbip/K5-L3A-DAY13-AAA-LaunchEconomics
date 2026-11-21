# Báo cáo cá nhân — 2A202603646 Nguyễn Mạnh Tường

## 1. Thông tin thành viên

- Họ tên: Nguyễn Mạnh Tường
- MSSV: 2A202603646
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
- Nghiệm thu, tính toán độc lập và hoàn thiện toàn bộ bảng độ nhạy CP2 (B1, B2, B3, B4) trong `report/team/bang_chi_phi.md`:
  - B1: 9 kịch bản độ nhạy kiểm tra tính chất tuyến tính đạt chuẩn 100%.
  - B2: Đổi một cặp (token x2 + xem lại x2 = 6.543 đ [+46,3%] [simulated]) và xếp hạng 3 yếu tố nhạy nhất: 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương nhân viên (+23,1%).
  - B3: Khẳng định giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220 đ) thay vì tối ưu cục bộ 1 lần chạy (4.111 đ).
  - B4: Xem lại 100% tốn 11.743 đ (0,98×) đến 12.415 đ (1,03×) [simulated], xác định ngưỡng hòa vốn ≤ 4,8 phút.
- Hỗ trợ Thành viên 4 điền trước Mục 1, Mục 2, Mục 3 và Mục 6 trong `report/team/ho_so_launch_v0.md`.
- Chủ trì thiết kế và hoàn thiện toàn bộ kế hoạch thử nghiệm pilot trong `report/team/pilot_plan.yaml` (CP4):
  - Tính toán 5 bài toán cỡ mẫu D1: Xác định trần lý thuyết của 20 cụm ($c/ICC = 1.000 < 1.251$), chứng minh phương án chia theo nhân viên (20 control vs 20 treatment) với $m \ge 299$ yc/người ($DE = 6,96$) cho MDE = 6 điểm ($n = 859$/nhóm) là phương án tối ưu khả thi duy nhất.
  - Trả lời 5 câu hỏi nhận diện D2: Đối chứng chạy cùng thời gian, bốc thăm ngẫu nhiên phân tầng theo depot, chặn tràn tác động bằng `staff_id`, khai báo trước các tiêu chí và đủ 20 cụm mỗi nhóm.
  - Nêu rõ và minh bạch đánh đổi chấp nhận (power giảm còn 0,64 nếu tác động thực tế chỉ là 5 điểm).
  - Thiết lập 3 quy tắc dừng (Stop Rules) an toàn, chi phí và sử dụng đúng chuẩn 4 vế: NẾU – TRONG – THÌ – KHÔNG THÌ; xác định cơ chế rollback trong 30 phút.

## 4. Bằng chứng

- Script tính toán độc lập từ CSV và log kiểm tra số liệu CP1, CP2, CP4.
- `TEAM.md`: Bảng phân vai 4 roles và nhiệm vụ chi tiết.
- `report/team/bang_chi_phi.md`: Đầy đủ 100% số liệu A1-A4 và B1-B4.
- `report/team/pilot_plan.yaml`: Hoàn thiện 100%, không còn dấu hỏi, cú pháp YAML chuẩn xác.
- `report/team/ho_so_launch_v0.md`: Mục 1, 2, 3, 5, 6 đã cập nhật số liệu chuẩn.
- Các commit kiểm tra và cập nhật tài liệu trên repo `K5-L3A-DAY13-AAA-LaunchEconomics`.

## 5. Công cụ AI đã dùng

- Trợ lý AI (Antigravity): Dùng để viết script kiểm tra số liệu độc lập, đối chiếu rubric và rà soát các quy tắc kiểm duyệt (không dùng từ vận hành chính thức, gắn nhãn `simulated`).
- Tự kiểm tra: Toàn bộ con số đều được tính toán lại trực tiếp từ dữ liệu CSV bằng Python, không sao chép thụ động.

## 6. Tự đánh giá

- Hoàn thành xuất sắc vai trò Người kiểm số ở CP1 (20/20 điểm), CP2 (15/15 điểm) và vai trò Pilot Analyst ở CP4 (15/15 điểm Rubric C4, đạt chuẩn 10/10 điểm Rubric C8).
- Phối hợp và bàn giao kịp thời các dữ liệu đầu vào cho các thành viên khác trong nhóm.
