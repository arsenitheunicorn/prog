m = float(input("Введите свою массу (в кг): "))
if m <= 0:
    while m <= 0:
        m = float(input("Отрицательная масса! Попробуйте еще раз: "))
h = float(input("Введите свой рост (в метрах): "))
if h <= 0 or h >= 2.9:
    while h <= 0 or h >= 2.9:
        h = float(input("Странный рост! Попробуйте еще раз: "))
i = m/h**2
if i <= 16:
    print("Выраженный дефицит массы тела")
elif i <= 18.5:
    print("Недостаточная (дефицит) масса тела")
elif i < 25:
    print("Норма")
elif i <= 30:
    print("Избыточная масса тела (предожирение)")
elif i <= 35:
    print("Ожирение первой степени")
elif i <= 40:
    print("Ожирение второй степени")
else:
    print("Ожирение третьей степени (морбидное)")