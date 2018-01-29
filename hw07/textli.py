## цифры?? различать дефисы между частями слова и тире

def choose_file():
    fn = input('Введите название файла БЕЗ расширения: ') + '.txt'
    return fn

def read_this_file(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.readlines()
    return text

def destroy_tab(text):
    l = []
    st = ''
    for a in text:
        l.append(a.strip())
    st += ' '.join(l)
    return st

def destroy_punct(st):
    b = ''
    p = '.,><"/?-@!()[]{}:;“”—'
    for a in st:
        d = 0
        for j in p:
            if a != j:
                d += 1
            else:
                d -= 1
        if d == len(p):
            b += a
    return b

def endlich(b):
    fl = b.split(' ')
    return fl

def del_spaces(fl):
    fl1 = []
    for a in fl:
        if a != ' ' and a!= '':
            fl1.append(a)
    return fl1

def final_list(fl1):
    fl2 = []
    for word in fl1:
        word2 = word.lower()
        fl2.append(word2)
    return fl2
    
def main():
    fn = choose_file()
    text = read_this_file(fn)
    st = destroy_tab(text)
    b = destroy_punct(st)
    fl = endlich(b)
    fl1 = del_spaces(fl)
    fl2 = final_list(fl1)
    return fl2

if __name__ == '__main__':
    main()

## ищем текст, и получаем на выходе список слов (без пунктуации и пробелов)
        
