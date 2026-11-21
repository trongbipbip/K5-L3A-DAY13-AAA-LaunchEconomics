# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Các số tính từ dữ liệu thử nghiệm là `simulated`; đây là chỉ số quan sát trong đợt chạy thử, chưa phải bằng chứng về tác động nhân quả.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | ---: |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0`, chia tổng số yêu cầu | **82,83% (994/1.200) [simulated]** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177) [simulated]** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay = 1`, chia tổng số yêu cầu | **4,25% (51/1.200) [simulated]** |
| Dùng | Tỉ lệ yêu cầu được xem lại | Số yêu cầu có `duoc_xem_lai = 1`, chia tổng số yêu cầu | Theo dõi trong pilot bằng `agent_suggestion_shown` và `staff_review_decision` |
| An toàn | Tỉ lệ hoàn trùng | Số ca có ledger hoàn trùng, chia tổng số yêu cầu | Theo dõi bằng `refund_ledger_write` và `idempotency_key`; ngưỡng dừng là 1 ca trong 3 ngày liên tiếp |

Chỉ số chính trong đợt chạy thử là **82,83% [simulated]**; không viết rằng trợ lý đã nâng chỉ số vì đợt chạy thử chưa có nhóm đối chứng.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in/out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | `giu/sua/bo`, `phut_xem_lai`, `trace_id` | Khi nhân viên giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ cái |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi yêu cầu mở lại |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Khi kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** chỉ số chính dùng `ticket_closed` và `ticket_reopened`; chỉ số bỏ qua dùng `agent_suggestion_shown` và `staff_review_decision`; chỉ số hoàn trùng dùng `refund_ledger_write`; chỉ số làm lại dùng `staff_rework_completed`.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng **51,8%**, lên **6.787 đ [simulated]** | Tỉ lệ làm lại theo tuần vượt 7% | Thu hẹp về `noi_dia`, rà 20 trace làm lại và giới hạn chạy lại | PM trợ lý hoàn phí |
| Tỉ lệ xem lại tăng gấp đôi | CPS tăng **40,7%**, lên **6.292 đ [simulated]** | Tỉ lệ xem lại vượt 50% ở cuối rollout 0,25 | Giảm xem lại theo bậc sau khi kiểm tra chất lượng, không mở bước tiếp theo nếu chưa đạt ngưỡng | Trưởng nhóm CSKH |
| Phải xem lại 100% kéo dài | CPS **11.743–12.415 đ [simulated]**, gần bằng hoặc cao hơn 12.000 đ của nhân viên | Tỉ lệ xem lại vẫn trên 50% sau tuần đầu | Dừng mở rộng, đo phút xem lại thật và điều chỉnh quy trình kiểm tra | Giám đốc vận hành |
