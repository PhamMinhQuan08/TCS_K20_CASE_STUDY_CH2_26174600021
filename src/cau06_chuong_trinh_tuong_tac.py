
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất: "))
so_phut = int(input("Nhập số phút sử dụng: "))
don_gia = float(input("Nhập đơn giá: "))

dien_nang = cong_suat * so_phut / 60 / 1000

chi_phi = dien_nang * don_gia

print("Mã phiên:", ma_phien)
print("Máy:", ma_may)
print("Điện năng:", round(dien_nang, 3))
print("Chi phí:", chi_phi)