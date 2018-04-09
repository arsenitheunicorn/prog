import re

def file_oeffnen():
    with open('file.xml', 'r', encoding='utf-8') as file:
        return file.read()

def count_lines(txt):
    haupt = re.search('^(.*?)</teiHeader>', txt, re.DOTALL).group(1).split('\n')
    with open('test2_results.txt', 'w', encoding='utf-8') as res:
        res.write('ЗАДАНИЕ 1:\nЧисло строк заголовка XML = ' + str(len(haupt)) + '\n')

def reinigung(txt):
    txt2 = []
    for line in txt.split('\n'):
        line = re.sub('(^)\s*(\S)', r'\1\2', line)
        txt2.append(line)
    return txt2

def typen_finden(txt):
    types = []
    for line in txt:
        if re.match('<w lemma=', line):
            types.append(re.search('type="([^"]*?)"', line).group(1))
    return types

def woerterbuch(types):
    wb = {}
    for typ in types:
        if typ in wb:
            wb[typ] += 1
        else:
            wb[typ] = 1
    with open('test2_results.txt', 'a', encoding='utf-8') as res:
        res.write('ЗАДАНИЕ 2:\n')
        for word in sorted(wb, key=wb.get, reverse=True):
            res.write(str(wb[word]) + '\t' + word + '\n')

def neutrale_pronomen(txt):
    np = []
    for line in txt:
        if re.match('<w lemma=', line) and re.search('type="f.h', line):
             np.append(re.search('>([^<]*?)<', line).group(1))
    with open('test2_results.txt', 'a', encoding='utf-8') as res:
        res.write('ЗАДАНИЕ 3:\n' + ','.join(np))

def csv_machen(txt):
    csv = ''
    for line in txt:
        if re.match('<w lemma=', line):
            line = re.sub('<w lemma="([^"]*?)" type="([^"]*?)">([^<]*?)</w>', r'\1,\2,\3\n', line)
            csv += line
    with open('test2_results.csv', 'w', encoding='utf-8') as res:
        res.write(csv)


def main():
    txt = file_oeffnen()
    count_lines(txt)
    txt = reinigung(txt)
    types = typen_finden(txt)
    woerterbuch(types)
    neutrale_pronomen(txt)
    csv_machen(txt)

if __name__ == '__main__':
    main()
