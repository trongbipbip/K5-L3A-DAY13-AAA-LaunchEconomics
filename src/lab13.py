"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i chỉ xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i=1..k
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Tử số: MỌI lần chạy, kể cả lần lỗi. Nhớ chia 1.000 trước khi nhân giá token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print(f'  E[lần chạy] p=0,8 k=2: {so_lan_chay_ky_vong(0.8, 2):.2f} · k=∞: {so_lan_chay_ky_vong(0.8):.2f}'
          f' · hệ số chi phí k=3: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    # ---- A2 ----
    print('\n=== A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated) ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    print(f"Số lần gọi tool: {runs['tool_calls'].sum():,} · phút xem lại: {reqs['phut_xem_lai_simulated'].sum():,}"
          f" · phút làm lại: {reqs['phut_lam_lai_simulated'].sum():,}")
    print(f"cps / hoá đơn mỗi yêu cầu = {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong']:6.1%}")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu (cộng {khong_tc} ca không thành công × 12.000 đ): '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× baseline [simulated]')

    # ---- A3 ----
    print('\n=== A3 · Theo loại yêu cầu (cps: simulated) ===')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'lan/yc':>7s} {'cps':>9s} {'×12000':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        print(f"{loai:10s} {len(r):6d} {kq['thanh_cong'] / len(r):9.1%} {r['so_lan_chay'].mean():7.2f}"
              f" {kq['cps']:9,.0f} {kq['cps'] / BASELINE:7.2f}")
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử
    ok = runs.merge(reqs[['request_id', 'loai']]).assign(ok=lambda d: d['status'] == 'ok')
    print('\nTỉ lệ ok theo lần thử (attempt):')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---- A4 ----
    print('\n=== A4 · Chi phí cố định 40 triệu đ/tháng, phạm vi noi_dia + hang_nang [simulated] ===')
    CO_DINH = 40_000_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    print(f"Phạm vi: {len(pham_vi)} yêu cầu, {kq_pv['thanh_cong']} thành công, tổng {kq_pv['tong']:,.0f} đ,"
          f" cps {kq_pv['cps']:,.0f} đ")
    for nhan, kl in [('45.000 yc/tháng', 45_000), ('Một nửa khối lượng', 22_500)]:
        tc_thang = kl * kq_pv['thanh_cong'] / len(reqs)
        cd = CO_DINH / tc_thang
        print(f"{nhan:20s} thành công/tháng {tc_thang:>8,.0f} · cố định/việc {cd:>6,.0f} đ"
              f" · cps + cố định {kq_pv['cps'] + cd:>6,.0f} đ = {(kq_pv['cps'] + cd) / BASELINE:.2f}×")

    # ---- B1 · Đổi từng yếu tố ----
    print('\n=== B1 · Độ nhạy: đổi từng yếu tố (cps: simulated) ===')
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f"{'Gốc (A2)':25s} {goc:8,.0f}")
    thay_doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = (cps / goc - 1) * 100
        print(f'{ten:25s} {cps:8,.0f} {thay_doi[ten]:+6.1f}%')
    # Tự kiểm tra: "giảm một nửa" = −½ mức tăng của "gấp đôi"
    for gap_doi, giam_nua in [('Giá token gấp đôi', 'Giá token giảm một nửa'),
                              ('Xem lại gấp đôi', 'Xem lại giảm một nửa'),
                              ('Làm lại gấp đôi', 'Làm lại giảm một nửa')]:
        assert abs(thay_doi[giam_nua] + thay_doi[gap_doi] / 2) < 1e-6, f'{giam_nua} phải bằng −½ × {gap_doi}'
    print('Tự kiểm tra "giảm một nửa = −½ gấp đôi": ĐẠT')

    # ---- B2 · Đổi một cặp và xếp hạng ----
    print('\n=== B2 · Đổi một cặp: giá token gấp đôi + xem lại gấp đôi [simulated] ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Xem lại gấp đôi']
    print(f'cps {cps_cap:,.0f} đ ({(cps_cap / goc - 1) * 100:+.1f}%) · tổng hai tác động riêng {tong_rieng:+.1f}%')
    yeu_to = {  # so sánh theo cùng mức đổi: gấp đôi (lương chỉ có kịch bản +25%)
        'Số ca làm lại': abs(thay_doi['Làm lại gấp đôi']),
        'Tỉ lệ xem lại': abs(thay_doi['Xem lại gấp đôi']),
        'Lương nhân viên (+25%)': abs(thay_doi['Lương tăng 25%']),
        'Giá token': abs(thay_doi['Giá token gấp đôi']),
        'Giới hạn số lần chạy': abs(thay_doi['Chỉ 1 lần chạy']),
    }
    print('Xếp hạng yếu tố theo |thay đổi|:')
    for i, (ten, v) in enumerate(sorted(yeu_to.items(), key=lambda x: -x[1]), 1):
        print(f'  {i}. {ten:25s} {v:5.1f}%')

    # ---- B3 · Giới hạn chạy lại và chi phí cả hệ thống ----
    print('\n=== B3 · Giới hạn số lần chạy: chi phí cả hệ thống [simulated] ===')
    print(f"{'Giới hạn':9s} {'Tổng trợ lý':>13s} {'Không TC':>9s} {'Cả hệ thống':>13s} {'cps':>7s}")
    b3 = {}
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        b3[k] = (kq['tong'] + khong_tc * BASELINE, kq['cps'])
        print(f"{k} lần     {kq['tong']:13,.0f} {khong_tc:9d} {b3[k][0]:13,.0f} {kq['cps']:7,.0f}")
    k_he_thong = min(b3, key=lambda k: b3[k][0])
    k_cps = min(b3, key=lambda k: b3[k][1])
    print(f'Rẻ nhất cho công ty: {k_he_thong} lần · cps thấp nhất: {k_cps} lần')

    # ---- B4 · Xem lại 100% cho noi_dia + hang_nang ----
    print('\n=== B4 · Xem lại 100%, phạm vi noi_dia + hang_nang [simulated] ===')
    PHUT_XEM_LAI, PHUT_LAM_LAI = 5, 9
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    tc_pv = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    tien_xem = co_ok * PHUT_XEM_LAI * LUONG_PHUT
    tien_may = kq_pv['token'] + kq_pv['tool']
    # Trung bình phút làm lại trên TOÀN BỘ ca lam_lai (không chỉ phạm vi), theo hướng dẫn
    tb_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'{len(pham_vi)} yêu cầu · có ≥1 lần ok: {co_ok} → xem lại {tien_xem:,.0f} đ · token + tool {tien_may:,.0f} đ'
          f' · thành công {tc_pv}')
    for nhan, phut in [(f'{PHUT_LAM_LAI} phút/ca (đề)', PHUT_LAM_LAI),
                       (f'{tb_lam_lai:.1f} phút/ca (TB dữ liệu)', tb_lam_lai)]:
        tien_lam = so_lam_lai * phut * LUONG_PHUT
        tong_b4 = tien_xem + tien_lam + tien_may
        cps_b4 = tong_b4 / tc_pv
        # Hoà vốn: số phút xem lại tối đa để cps = BASELINE
        hoa_von = (BASELINE * tc_pv - tien_lam - tien_may) / (co_ok * LUONG_PHUT)
        print(f'  Làm lại {nhan:24s}: {so_lam_lai} ca → {tien_lam:,.0f} đ · tổng {tong_b4:,.0f} đ'
              f' · cps {cps_b4:,.0f} đ = {cps_b4 / BASELINE:.2f}× · hoà vốn ≤ {hoa_von:.1f} phút/lần xem')

    # ---- D1 · Cỡ mẫu theo ba cách chia ----
    from statistics import NormalDist
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    def co_mau(p1, p2, alpha=0.05, power=0.8):
        """Số yêu cầu mỗi nhóm để thấy chênh p1 → p2 (kiểm định hai tỉ lệ, hai phía)."""
        za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    def he_so_thiet_ke(m, icc):
        return 1 + (m - 1) * icc

    P0, ICC, SO_NV = 0.70, 0.02, 40
    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    n_a = co_mau(P0, P0 + 0.05)
    print(f'a) Chia theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm')

    m_b = 75
    de_b = he_so_thiet_ke(m_b, ICC)
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / m_b)
    print(f'b) Theo nhân viên, m = {m_b}: DE = {de_b:.2f} → {n_b:,} mỗi nhóm → {nv_b} người/nhóm,'
          f' tổng {2 * nv_b} {">" if 2 * nv_b > SO_NV else "≤"} {SO_NV}:'
          f' {"KHÔNG đủ người" if 2 * nv_b > SO_NV else "đủ người"}')

    for nhan, c in [('c) 20 nhân viên mỗi nhóm', 20), ('d) 6 depot mỗi nhóm', 6)]:
        tran = c / ICC   # n_hiệu dụng = c·m / DE < c / ICC khi m → ∞
        print(f'{nhan}: n hiệu dụng tối đa = {c} / {ICC} = {tran:,.0f}'
              f' {"<" if tran < n_a else "≥"} {n_a:,}: {"KHÔNG đạt" if tran < n_a else "đạt"}')

    n_e = co_mau(P0, P0 + 0.06)
    c_e = 20
    # c·m / (1 + (m−1)·ICC) ≥ n  ⇔  m·(c − n·ICC) ≥ n·(1 − ICC)
    m_e = math.ceil(n_e * (1 - ICC) / (c_e - n_e * ICC))
    print(f'e) Mức chênh 6 điểm ({n_e:,} mỗi nhóm), {c_e} người/nhóm: m ≥ {m_e} yêu cầu mỗi người'
          f' (DE {he_so_thiet_ke(m_e, ICC):.2f}, n hiệu dụng {c_e * m_e / he_so_thiet_ke(m_e, ICC):,.0f})')

    # Power thật nếu thiết kế cho 6 điểm nhưng tác động thật chỉ 5 điểm
    es5 = proportion_effectsize(P0 + 0.05, P0)
    power_5 = NormalIndPower().power(effect_size=es5, nobs1=n_e, alpha=0.05, ratio=1.0)
    print(f'Đánh đổi: thiết kế cho 6 điểm (n = {n_e}) mà tác động thật 5 điểm → power ≈ {power_5:.2f}')
    n_sm = NormalIndPower().solve_power(effect_size=es5, alpha=0.05, power=0.8, ratio=1.0)
    print(f'(Đối chiếu statsmodels, chia theo yêu cầu, +5 điểm: {math.ceil(n_sm):,} mỗi nhóm)')

    # ---- D3 · Tỉ lệ mở lại hiện tại (trước khi đặt luật an toàn) ----
    print('\n=== D3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại ===')
    mo_lai = reqs['mo_lai_trong_7_ngay']
    print(f'Toàn bộ: {mo_lai.mean():.2%} ({mo_lai.sum()}/{len(reqs)})')
    mo_lai_pv = pham_vi['mo_lai_trong_7_ngay']
    print(f'Phạm vi noi_dia + hang_nang: {mo_lai_pv.mean():.2%} ({mo_lai_pv.sum()}/{len(pham_vi)})')
    print(reqs.groupby('loai')['mo_lai_trong_7_ngay'].mean().map('{:.2%}'.format).to_string())
