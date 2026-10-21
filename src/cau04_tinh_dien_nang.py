cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
#dien_nang_kwh:250*1.5 / 1000 = 0.375 kWh
#chi_phi: 0.375*3000 = 1125 VNĐ
print(dien_nang_kwh)
print(chi_phi)
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(dien_nang_kwh)
print(chi_phi)