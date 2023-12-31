#Kiểm tra một số xem có phải số hoàn hảo không
x = int(input('Nhập số cần kiểm tra : '))
def so_hh(x):
    tong=0
    for i in range(1, x // 2 +1):
        if x % i ==0:
            tong+=i
    if tong==x:
        return True
    else:
        return False
    
#Kiểm tra
if so_hh(x)==True:
    print('Đây là số hoàn hảo')
else:
    print('Đây không phải số hoàn hảo')