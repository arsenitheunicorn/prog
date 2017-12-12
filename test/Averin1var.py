#1
with open('Extinct_languages.tsv', 'r', encoding='utf-8') as f:
    te = f.readlines()
for a in te:
    if len(a) > 35:
        print(a)
#2
with open('Extinct_languages.tsv', 'r', encoding='utf-8') as f:
    t = f.readlines()
l = []
for a in t:
    a1 = a.replace('\t', '')
    l.append(a1)
d = 0
b = "Critically endangered"
for st in l:
    p = len(st) - len(b) - 1
    p1 = p + len(b)
    if st[p:p+len(b):] == b:
        d += 1
print(d)
