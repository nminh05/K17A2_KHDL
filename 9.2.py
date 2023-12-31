nam = float(input('Nhập số năm :'))
#công thức tính
tinh_can = nam%10
tinh_chi = nam%12
#lệnh tính can
if nam < 0:
    print('Vui lòng nhập số dương')
if tinh_can ==0:
    tinh_can = 'Canh'
elif tinh_can ==1:
    tinh_can = 'Tân'
elif tinh_can ==2:
    tinh_can = 'Nhâm'
elif tinh_can ==3:
    tinh_can = 'Quý'
elif tinh_can ==4:
    tinh_can = 'Giáp'
elif tinh_can ==5:
    tinh_can = 'Ất'
elif tinh_can ==6:
    tinh_can = 'Bính'
elif tinh_can ==7:
    tinh_can = 'Đinh'
elif tinh_can ==8:
    tinh_can = 'Mậu'
elif tinh_can ==9:
    tinh_can='Kỳ'

#lệnh tính chi
if tinh_chi==0:
    tinh_chi = 'Thân'
elif tinh_chi==1:
    tinh_chi = 'Dậu'
elif tinh_chi==2:
    tinh_chi = 'Tuất'
elif tinh_chi==3:
    tinh_chi = 'Hợi'
elif tinh_chi ==4:
    tinh_chi = 'Tý'
elif tinh_chi ==5:
    tinh_chi = 'Sửu'
elif tinh_chi ==6:
    tinh_chi='Dần'
elif tinh_chi ==7:
    tinh_chi = 'Mão'
elif tinh_chi ==8:
    tinh_chi = 'Thìn'
elif tinh_chi ==9:
    tinh_chi = 'Tỵ'
elif tinh_chi ==10:
    tinh_chi = 'Ngọ'
elif tinh_chi ==11:
    tinh_chi = 'Mùi'

#in ra kết quả
print('Năm', nam, 'lịch âm là năm', tinh_can, tinh_chi)