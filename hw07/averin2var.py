import textli

def textlist():
    file_list = textli.main()
    return file_list

def woerterbuch(a):
    d = {}
    for word in a:
        if word[len(word)-4: len(word):] == 'ness':
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d

def zahl(d):
    zahl = 0
    for word in d:
        zahl += d[word]
    print('всего слов на -ness: ', zahl)

def frec(d):
    a = ''
    for word in sorted(d, key=d.get, reverse=True):
        if a == '':
            print('самое частотное - ', word, '(', d[word], ')')
            a += word

def main():
    file_list = textlist()
    d = woerterbuch(file_list)
    zahl(d)
    frec(d)

if __name__ == '__main__':
    main()
