import re

def datei_lesen():
    title = input('Введите название txt-файла без расширения: ') + '.txt'
    with open(title, 'r', encoding='utf-8') as txt:
        text = txt.read()
    text = re.sub(r'[!?\n]', '\.', text)
    text = re.sub('\.\.\.', '\.', text)
    sntncs = text.split('.')
    sntnc = [re.sub(r'[,:;"«—»\\]', '', satz) for satz in sntncs]
    sntn = [re.sub(r'^(\s)*(\S)', r'\2', satz) for satz in sntnc]
    snt = [satz for satz in sntn if satz]
    return snt

def lange_sätze(snt):
    lange = [satz.split(' ') for satz in snt if len(satz.split(' ')) > 10]
    lange_up = [word for sntnc in lange for word in sntnc if re.match(r'^[А-ЯЁ]', word)]
    return lange_up

def form_machen(lng):
    ##int(math.sqrt(len(lng)))
    for word in enumerate(lng):
        space = str(len(word[1]) + 8) + '}'
        if word[0] % 3 == 0:
            form = '{:<' + space
        if word[0] % 3 == 1:
            form = '{:^' + space
        if word[0] % 3 == 2:
            form = '{:>' + space
        print(form.format(word[1]))
        

def main():
    snt = datei_lesen()
    lng = lange_sätze(snt)
    form_machen(lng)

if __name__ == '__main__':
    main()
