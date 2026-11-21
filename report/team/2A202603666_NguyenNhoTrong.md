# Báo cáo cá nhân — Nguyễn Nho Trọng-2A202603666

## 1. Thông tin thành viên

- Họ tên: Nguyễn Nho Trọng
- MSSV: 2A202603666
- Email: ngnhotrong@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ / Launch Owner
- GitHub: trongbipbip

## 2. Phần việc phụ trách

- Giữ và cập nhật hồ sơ launch v0 trong `report/team/ho_so_launch_v0.md` theo tiến độ các checkpoint.
- Thực hiện bộ nhãn độc lập thứ hai cho 20 ca lỗi ở CP3.
- Đối chiếu hai bộ nhãn, ghi nhãn thống nhất, tỉ lệ đồng thuận và bảng khắc phục 5 loại lỗi trong `report/team/bang_loi.md`.
- Rà soát phạm vi pilot, trạng thái bằng chứng và các điều kiện cần đưa vào hồ sơ launch ở CP4–CP5.

## 3. Đóng góp cụ thể

- Hoàn thiện CP3 trong `report/team/bang_loi.md`: điền bộ nhãn độc lập của Người gắn nhãn 2 cho đủ 20 ca.
- So sánh hai bộ nhãn và ghi nhận 19/20 ca trùng, tương đương 95% đồng thuận.
- Thống nhất ca 13 là **Giới hạn hệ thống** vì yêu cầu nằm ngoài phạm vi dữ liệu/sản phẩm của trợ lý.
- Điền bảng khắc phục đủ 5 loại lỗi, gồm cách phát hiện đo được, hành động khắc phục và một role phụ trách.
- Theo dõi hồ sơ launch v0 qua CP1–CP4; các số economics CP1–CP2 và cỡ mẫu CP4 được đối chiếu theo các commit của thành viên phụ trách tương ứng.

## 4. Bằng chứng

- Commit `d47332c` — `CP3`, tác giả `trongbipbip`, ngày 2026-11-21: sửa `report/team/bang_loi.md`.
- `report/team/bang_loi.md`: hai bộ nhãn độc lập, 19/20 = 95% đồng thuận, quy tắc phân biệt ca 13 và bảng khắc phục 5 ca.
- `TEAM.md`: ghi vai trò Người gắn nhãn 2 kiêm giữ hồ sơ / Launch Owner và phạm vi đóng góp của thành viên 4.
- `report/team/ho_so_launch_v0.md`: hồ sơ launch được cập nhật theo các số đã được nhóm nghiệm thu ở CP1–CP4.
- Bằng chứng chạy nhóm: `python lab13.py` in A1 `ĐẠT`, các bảng A2–B4 và D1; D1 cho kết quả 859 yêu cầu mỗi nhóm ở MDE 6 điểm và 299 yêu cầu mỗi nhân viên.

## 5. Công cụ AI đã dùng

- Codex/ChatGPT: dùng để đọc cấu trúc lab, giải thích thứ tự checkpoint, rà soát rubric và kiểm tra tính đầy đủ của hồ sơ.
- Tự kiểm tra bằng cách đối chiếu nội dung file với lịch sử Git, output chạy thật của `python lab13.py` và các điều kiện trong `CHECKPOINTS.md`.
- Không dùng AI để bịa số liệu; các số CP1–CP4 được lấy từ code, dữ liệu CSV và output chạy của nhóm.

## 6. Tự đánh giá

- Hoàn thành phần gắn nhãn độc lập và tổng hợp CP3 với mức đồng thuận 95%, vượt ngưỡng 80% của rubric.
- Hoàn thành vai trò giữ hồ sơ bằng cách theo dõi các số đã nghiệm thu và trạng thái của hồ sơ launch qua các checkpoint.
- Cần tiếp tục hoàn thiện CP5: `chi_so.md`, các rủi ro kinh tế, bảy mục của hồ sơ launch và phiếu duyệt chéo Gate 2a.
