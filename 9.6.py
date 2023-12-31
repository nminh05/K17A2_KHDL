#Xây dựng hàm kiểm tra số nguyên tố
x = int(input('Nhập số cần kiểm tra : '))
import math
def kiem_tra_so_nguyen_to(x):
    can = (int)(math.sqrt(x))
    if x < 2:
        return False
    for i in range(2, can+1):
        if x%i==0:
            return False
        else:
            return True
        
#Kiểm tra 
if kiem_tra_so_nguyen_to(x)==True:
    print(x,' là số nguyên tố')
else:
    print(x,' không là số nguyên tố')