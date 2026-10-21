ma_may = input("Nhập mã máy: ")
cong_suat_w = int(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

#cau07_chuan_doan_loi.py", line 6 print(f"Điện năng: {dien_nang:.3f} kWh" SyntaxError: '(' was never closed
#Nguyen nhan la do thieu ngoac o print cuoi cung

#cau07_chuan_doan_loi.py", line 4, in <module> dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000 TypeError: unsupported operand type(s) for /: 'str' and 'int'
#Nguyen nhan do cong_suat_w dang nhan gia tri str khong the nhan vs so phut la int

#cau07_chuan_doan_loi.py", line 6, in <module> print(f"Điện năng: {dien_nang:.3f} kWh") NameError: name 'dien_nang' is not defined. Did you mean: 'dien_nang_kwh'?
#Nguyen nhan do dien_nang chua duoc khai bao