a = input('Введите слово: ')
l = []
while a != '':
    l.append(a)
    a = input('Введите еще одно слово: ')
with open('sample_text.txt', 'w', encoding="utf-8") as f:
    for i in enumerate(l):
        if len(i[1]) > 5:
           with open('sample_text.txt', 'a', encoding="utf-8") as f:
               f.write(i[1])
               f.write('\n')
