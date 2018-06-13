import re

def open_bible(title):
    with open(title, 'r', encoding='utf-8') as file:
        f = file.readlines()
        f_clean = [re.sub(r'^[\n\t]*(\S)', r'\1', line) for line in f]
        bible = []
        stih = []
        for number, line in enumerate(f_clean):
            if re.match('<seg ', line):
                stih.append(re.search('id="([^"]+)"', line).group(1))
                bible.append(f_clean[number + 1])
        return bible, stih

def word_length(bib):
    words = 0
    letters = 0
    for line in bib:
        line = re.sub('[.,\n:;?!()]', '', line)
        words += len(line.split(' '))
        letters += len(line) - len(line.split(' ')) + 1
    print(letters / words)

def worddict(bib):
    dicti = {}
    for line in bib:
        line = re.sub('[.,\n:;?!()]', '', line)
        lin = line.lower()
        for word in lin.split(' '):
            if word in dicti:
                dicti[word] += 1
            else:
                dicti[word] = 1
    return dicti

def print_task(d1, d2):
    l1 = sorted(d1, key=d1.get, reverse=True)
    l2 = sorted(d2, key=d2.get, reverse=True)
    for i in range(0, 10):
        print(l1[i], l2[i], sep=':')

def create_strange_file(e, ch, s):
    with open('sto_stihov.txt', 'w', encoding='utf-8') as file:
        for i in range(0, 100):
            l_ch = re.sub('[.,\n:;?!()]', '', ch[i])
            l_e = re.sub('[.,\n:;?!()]', '', e[i])
            line = s[i] + '~~~' + str(round(len(l_ch.split(' ')) / len(l_e.split(' ')), 2)) + '\n'
            file.write(line)

def main():
    eng_bbl, stih = open_bible('English.xml')
    cham_bbl, stih = open_bible('Chamorro-PART.xml')
    word_length(cham_bbl)
    cham_d = worddict(cham_bbl)
    eng_d = worddict(eng_bbl)
    print_task(cham_d, eng_d)
    create_strange_file(eng_bbl, cham_bbl, stih)

if __name__ == '__main__':
    main()
