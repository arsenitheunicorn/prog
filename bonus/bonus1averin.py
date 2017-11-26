a = 0
l = []
while a != '':
    a = input('Введите число: ')
    if a != '':
        try:
            a1 = float(a)
            l.append(a1)
        except ValueError:
            print("Это не число!")
    else:
        break
if l == []:
    print("Ничего не было введено!")
else:
    mi = l[0]
    ma = l[0]
    s = 0
    for i in enumerate(l):
        if i[1] <= mi:
            mi = i[1]
        if i[1] >= ma:
            ma = i[1]
        s += i[1]
        c = i[0] + 1
    avs = s/c
    print("Наименьшее число: ", mi)
    print("Набиольшее число: ", ma)
    print("Среднее арифметическое с округлением до тысячных: ", round(avs, 3))
    print(l)
    print(c)
