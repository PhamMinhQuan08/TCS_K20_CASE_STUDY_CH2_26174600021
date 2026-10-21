from datetime import datetime 
ma_phien = input()
ma_may = input()
cong_suat_w = float(input())
so_phut = int(input())
don_gia = int(input())

dien_nang_tieu_thu = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_tieu_thu * don_gia
su_dung = (so_phut > 60)
thoi_diem = datetime.now()
thoi_diem_str = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat_w:.2f} W")
print(f"Thoi luong: {so_phut} phut")
print(f"Dien nang: {dien_nang_tieu_thu} kWh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {su_dung}")
print(f"Ghi nhan luc: {thoi_diem_str}")