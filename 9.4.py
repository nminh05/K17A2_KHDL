#xây dựng phương thức tính theo yêu cầu
#Cách 1
#Truyền vào tham số n và x
def S(n,x):
    S = (x**2+1)**n
    print('Kết quả bài toán là: ', S)
#Với giá trị n =4 , n= 3
print(S(4,3))

#Cách 2
n = int(input('Nhập số n: '))
x = int(input('Nhập số x: '))
#Công thức xử lí bài toán
S1 = (x**2+1)**n
#In ra kết quả
print('Kết quả là :' , S1)