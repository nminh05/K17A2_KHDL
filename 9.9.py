import math
r = float(input('Nhập bán kính r :'))
a = float(input('Nhập chiều dài cạnh a:'))
b = float(input('Nhập chiều rộng cạnh b:'))
pi = math.pi
if a < 0:
    print('Vui lòng nhập cạnh a dương')
if b < 0:
    print('Vui lòng nhập cạnh b dương')
if r <0:
    print('Vui lòng nhập bán kính dương')

#hình tròn
#Chu vi
C = 2*pi*r
print('Chu vi hình trong là :', C)

#Diện tích
P = pi*r**2
print('Diện tích hình trong là :', P)

#hình chữ nhật
#Chu vi
C1 = (a + b)*2
print('Chu vi hình chữ nhật là :', C1)

#Diện tích
P1 = a * b 
print('Diện tích hình chữ nhật là :', P1)
