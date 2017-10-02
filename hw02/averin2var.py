s = input('Введите слово: ') 

s1 = "" 

for i,c in enumerate(s): 

    if i % 2 == 0 and (c == "п" or c == "о" or c == "е"): 

        s1+= c 

print(s1)
