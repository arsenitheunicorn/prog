a = input('Введите слово кириллицей: ')
l = list(a)
s = []
v = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
for i in enumerate(l):
    s.append(i[1])
    for j in enumerate(v):
        if i[1] == j[1]:
            s.append('с')
            s.append(i[1])
s1 = ''.join(s)
print(s1)
