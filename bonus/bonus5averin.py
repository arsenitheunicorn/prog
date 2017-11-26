a = input('Введите слово латиницей: ')
l = list(a)
s = []
v = ['a', 'e', 'i', 'o', 'u', 'y', ' ', '.', ',', '!', '?', '-']
for i in enumerate(l):
    s.append(i[1] + 'aig')
    for j in enumerate(v):
        if i[1] == j[1]:
             s.insert(i[0], i[1])
             s.remove(i[1] + 'aig')
s1 = ''.join(s)
print(s1)
