#nhập dữ liệu đầu vào
can_nang = int(input('Nhập số cân nặng(kg):'))
chieu_cao = float(input('Nhập chiều cao(m):'))
#công thức tính
BMI = can_nang/(chieu_cao*chieu_cao)
print('Chỉ số cơ thể của bạn là :', BMI)
#điều kiện để ra kết quả
if BMI < 18.5:
    print('Bạn khá gầy')
elif BMI >= 25:
    print('Bạn đang trong tình trạng thừa cân')
else:
    print('Cơ thể cân đối')
