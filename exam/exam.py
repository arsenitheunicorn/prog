import re
import os

def open_files():
    liste_der_titeln = os.listdir()
    liste_der_daten = []
    linien = []
    for title in liste_der_titeln:
        if '.xhtml' in title:
            with open(title, 'r', encoding='windows-1251') as file:
                art = file.read()
                lin = art.split('\n')
                liste_der_daten.append(art)
                linien.append(lin)
                file.close()
    return liste_der_daten, linien

def liste_fur_csv(liste):
    tag_liste = ['docid', 'header', 'author', 'created', 'topic', 'tagging']
    csv_liste = []
    for art in liste:
        art_liste = []
        for tag in tag_liste:
            pattern = '<meta content="([^"]*)" name="' + tag + '"'
##            print(pattern)
            result = re.search(pattern, art).group(1)
##            print(result)
            art_liste.append(result)
        csv_liste.append(art_liste)
    return tag_liste, csv_liste

def create_csv(tag, csv):
    with open('auf1.csv', 'w', encoding='utf-8') as table:
        table.write(','.join(tag))
        table.write('\n')
        for art in csv:
            table.write(','.join(art))
            table.write('\n')

def abbr(lines):
    wb = {}
    for art in lines:
        for line in art:
            if re.search('<ana lex="([А-ЯЁ]+)"', line):
                 ab = re.search('<ana lex="([А-ЯЁ]+)"', line).group(1)
                 if len(ab) > 1:
                     if ab in wb:
                         wb[ab] += 1
                     else:
                         wb[ab] = 1
    return wb

def create_tsv(wb):
    with open('auf2.tsv', 'w', encoding='utf-8') as table:
        for line in sorted(wb, key=wb.get, reverse=True):
            kalame = line + '\t' + str(wb[line]) + '\n'
            table.write(kalame)

def bigramms(daten):
    bigr_liste = []
    for art in daten:
        sentences = art.split('<se>')
        for clause in sentences:
            words = clause.split('\n')
            for number, line in enumerate(words):
                if re.search('gr="S,[^"]+?,gen"', line) and number > 0:
                    if re.search('gr="S,', words[number-1]):
##                        point_blank = words[number - 1]
                        bigr = re.search(r'ana>([^<]+?)<', words[number - 1]).group(1) + ' '
                        bigr += re.search(r'ana>([^<]+?)<', line).group(1)
                        bigr += '\t'
                        for word in words:
                            if re.match('<w>', word):
                                bigr += re.search(r'ana>([^<]+?)<', word).group(1)
                                bigr += ' '
                        bigr_liste.append(bigr)
    return bigr_liste

def create_txt(bigr_liste):
    with open('auf3.txt', 'w', encoding='utf-8') as txt:
        txt.write('\n'.join(bigr_liste))

def main():
    daten, lines = open_files()
    tag, csv = liste_fur_csv(daten)
    create_csv(tag, csv)
    wb = abbr(lines)
    create_tsv(wb)
    bigr_liste = bigramms(daten)
    create_txt(bigr_liste)
    
if __name__ == '__main__':
    main()
