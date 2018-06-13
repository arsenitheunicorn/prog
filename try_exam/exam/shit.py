import re

def datei_öffnen():
    with open('karenina.xml', 'r', encoding='utf-8') as file:
        text = file.read()
        txt = re.sub(r'(\n)\n', r'\1', text)
        lines = txt.split('\n')
    return text, lines

def aufgabe1(text):
    tag_w = re.findall('<w>', text)
    tag_ana = re.findall('<ana', text)
    print(len(tag_ana) / len(tag_w))

def aufgabe2_wb(lines):
    wb = {}
    for line in lines:
        if re.match(r'<w>', line):
            found = re.search('gr="([A-Z]+)[^A-Z]', line).group(1)
            if found in wb:
                wb[found] += 1
            else:
                wb[found] = 1
    return wb

def aufgabe2_dat(wb):
    with open('auf2.txt', 'w', encoding='utf-8') as file:
        for wortart in sorted(wb, key=wb.get, reverse=True):
            file.write(wortart + '\t' + str(wb[wortart]) + '\n')

def aufgabe3_li1(lines):
    körperliste = []
    for number, line in enumerate(lines):
        if re.search('gr="S[^"]+твор[^"]+"', line):
            lineliste = [re.search('/>([А-Яа-яЁё]+)</w>', line).group(1), number]
            körperliste.append(lineliste)
    return körperliste

def aufgabe3_li2(liste1, lines):
    final = []
    for liste in liste1:
        lex_list = []
        start = liste[1] - 3
        stop = liste[1] + 4
        for i in range(start, stop):
            if re.search('/>([А-Яа-яЁё]*)</w>', lines[i]):
                word = re.search('/>([А-Яа-яЁё]*)</w>', lines[i]).group(1)
            else:
                word = '-'
            lex_list.append(word)
        final.append(lex_list)
    return final

def aufgabe3_dat(final):
    with open('auf3.txt', 'w', encoding='utf-8') as file:
        for liste in final:
            außendaten = liste[0] + ' ' + liste[1] + ' ' + liste[2] + '\t' + liste[3] + '\t' + liste[4] + ' ' + liste[5] + ' ' + liste[6] + '\n'
            file.write(außendaten)

            
                      
def main():
    text, lines = datei_öffnen()
    aufgabe1(text)
    wb = aufgabe2_wb(lines)
    aufgabe2_dat(wb)
    liste1 = aufgabe3_li1(lines)
    final = aufgabe3_li2(liste1, lines)
    aufgabe3_dat(final)
    

if __name__ == '__main__':
    main()
