ma_may = input("nhap_ma_may: ")
cong_suat_w = int(input("nhập công suất: "))
so_phut_su_dung = int(input("nhập số phút: "))
gia_dien = float(input("nhập giá tiền điện: "))
cong_suat_w= float(cong_suat_w)

dien_nang = float(cong_suat_w)*int(so_phut_su_dung)/60 / 1000
chi_phi = dien_nang * float(gia_dien)
print(f"điện năng: {dien_nang}")
print(f"chi phí: {chi_phi}")



