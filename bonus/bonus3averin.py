a = input("Введите слово латиницей: ")
l = list(a)
d = len(a)
v = ['a', 'e', 'i', 'o', 'u', 'y']
for j in v:
    if j == l[0]:
        lv = ''.join(l) + 'yay'
        print(lv)
        l = []
        break
c = []
if l != []:
    for i in enumerate(l):
        for j in v:
            if i[1] == j:
                c.append(i[0])
                break
    if c == []:
        print(a + 'ay')
    else:    
        cc = c[0]
        l1 = l[cc:d]
        l2 = l[:cc]
        lc = ''.join(l1) + ''.join(l2) + 'ay'
        print(lc)
