# Phiếu chấm hội đồng Gate 2a — Tự chấm nhóm AAA

Nhóm thực hiện tự đối chiếu hồ sơ của chính nhóm theo rubric Gate 2a và các bằng chứng đã có trong repo.

- Nhóm chấm (hội đồng): **AAA**
- Nhóm được chấm: **AAA — tự chấm theo yêu cầu của giảng viên**

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất **Go có điều kiện** phù hợp: `noi_dia + hang_nang` có CPS 2.696 đ và 8.221 đ; nhóm loại `quoc_te` vì CPS 22.515 đ = 1,88× nhân viên và nêu rủi ro xem lại 100% lên 11.743–12.415 đ. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Các số từ `_simulated` đều ghi `[simulated]`; phạm vi được thu hẹp thành `noi_dia + hang_nang`, loại `quoc_te` và `doi_tac` bằng số liệu CP1. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Pilot có 20 nhân viên can thiệp và 20 đối chứng, MDE 6 điểm, 859 yêu cầu/nhóm, DE 6,96 và tối thiểu 299 yêu cầu/nhân viên; có 3 luật dừng với ngưỡng, thời hạn, owner và rollback 30 phút. |
| **Tổng** | | | | **30 / 30** | Hồ sơ đáp ứng các tiêu chí tự chấm của Gate 2a. |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Nhóm chỉ đề xuất pilot trong `noi_dia + hang_nang`, không mở rộng ngay sang `quoc_te`. Trước khi bắt đầu phải bật đủ event có `trace_id`, đo phút xem lại/làm lại thật sau tuần 1, được chấp nhận MDE 6 điểm và duy trì rollback an toàn.

**Một câu hỏi cho đội trình:** Nếu phải xem lại 100% trong tuần đầu, chi phí mỗi việc thành công có còn thấp hơn nhân viên không?

**Câu trả lời của đội trình:** Không chắc chắn. Kịch bản xem lại 100% cho kết quả 11.743 đ = 0,98× nhân viên với 9 phút làm lại và 12.415 đ = 1,03× với 15,3 phút làm lại [simulated]. Vì vậy pilot phải học tỉ lệ xem lại tối đa có thể chấp nhận và không được mở rộng nếu chi phí vượt ngưỡng.
