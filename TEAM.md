# Team

## Thông tin nhóm

- Tên nhóm: AAA
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-AAA-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/trongbipbip/K5-L3A-DAY13-AAA-LaunchEconomics, nhánh main

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Hải Tuấn | | vuhaituan100903@gmail.com | ha1tuan | Người viết code / Economics Engineer |
|   2 | Mạnh Tường | | manhtuongqt@users.noreply.github.com | manhtuongqt | Người kiểm số / Pilot Analyst |
|   3 | Thành viên 3 | | | | Người gắn nhãn lỗi 1 / Error Analyst |
|   4 | Nguyễn Nho Trọng | | | trongbipbip | Người gắn nhãn lỗi 2 kiêm giữ hồ sơ / Launch Owner |

Bốn vai của lab:

- **Người viết code (Thành viên 1):** viết và chạy `src/lab13.py` (CP1-A, CP2-B).
- **Người kiểm số (Thành viên 2 - manhtuongqt):** tính tay đối chiếu các số A2/A3/B1; kiểm tra output code; làm CP4-D1, D2 và chủ trì `pilot_plan.yaml`. Đã kiểm số độc lập CP1: ĐẠT 100%.
- **Người gắn nhãn 1 (Thành viên 3):** đọc 20 ca lỗi, theo dõi điều kiện "Xong khi"; gắn nhãn độc lập ở CP3 (Bộ 1 trong `bang_loi.md`).
- **Người gắn nhãn 2, kiêm giữ hồ sơ (Thành viên 4):** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn độc lập ở CP3 (Bộ 2 trong `bang_loi.md`); tổng hợp CP5.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## ManhTuong-manhtuongqt

### Phần việc phụ trách

- **Người kiểm số (Verification):** Chạy tính toán độc lập, đối chiếu và nghiệm thu toàn bộ mô hình chi phí CP1 (A1, A2, A3, A4) và bảng độ nhạy CP2 (B1, B2, B3, B4).
- **Pilot Analyst:** Chủ trì tính toán cỡ mẫu thử nghiệm RCT cụm (CP4-D1), xác định tính nhận diện tách biệt tác động (CP4-D2), thiết kế 3 luật dừng và hoàn thiện `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Chạy script tính toán độc lập từ 2 file CSV gốc (`logix_runs.csv` và `logix_requests.csv`), kiểm tra chéo toàn bộ kết quả của Người 1: Xác nhận A1 đạt 3/3 phép thử, A2 khớp 100% (CPS 4.472 đ gấp 16,3 lần hóa đơn, giờ nhân viên chiếm 92,5%), A3 và A4 chuẩn xác.
- Nghiệm thu tính hợp lệ của `report/team/bang_chi_phi.md`: Kiểm tra gắn nhãn `simulated`, đảm bảo câu trả lời $\le 3$ dòng và có số liệu cụ thể.
- Hỗ trợ điền trước các con số kinh tế của CP1 (Mục 1 và Mục 3) vào `report/team/ho_so_launch_v0.md` để Launch Owner (Thành viên 4) theo dõi và hoàn thiện hồ sơ.

### Bằng chứng

- Script kiểm số độc lập từ dữ liệu gốc trong repo.
- Các số liệu đã nghiệm thu trong `report/team/bang_chi_phi.md`.
- Mục 1 và Mục 3 đã cập nhật trong `report/team/ho_so_launch_v0.md`.
