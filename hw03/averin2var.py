a = list(input("Введите слово: "))
a1=""
for i,sym in enumerate(a):
    sym=a[i]
    a1+=a1.join(sym)
    print(a1)
