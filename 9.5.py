#Xây dựng phương thức tính A(n,x) theo yêu cầu:
#Cách 1:
n = int(input('Nhập số n : '))
x = int(input('Nhập số x : '))
A = (x**2 +x +1)**n + (x**2 - x +1)**n
print('Đáp số bài toán là : ', A)

#Cách 2
def A1(n,x):
    A1=(x**2 + x +1)**n + (x**2 - x +1)**n
    print('Đáp số bài toán là: ', A1)

#với giá trị n = 4 , x=3
print(A1(4,3))