#Viết hàm trả về phần nguyên của phép chia hai số nguyên
a = int(input('Nhập số nguyên a : '))
b = int(input('Nhập số nguyên b : '))
x = a//b
if b ==0:
    print('Phương trình vô nghiệm')
else:
    print('Phần nguyên của phép chia là : ', x)
        