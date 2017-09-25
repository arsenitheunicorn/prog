print('введите число a')
print('введите число b')
print('введите число c')
a = int(input())
b = int(input())
c = int(input())
if a * b == c:
    print('a умножить на b равно c')
else:
    print('a умножить на b не равно c')
if a * c + b == 0:
    print('число c является решением уравнения "ax + b = 0"')
else:
    print('число c не является решением уравнения "ax + b = 0"')
