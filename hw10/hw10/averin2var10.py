import re

def seite_öffnen():
    name = input('название html-файла без расширения: ')
    try:
        file = open(name + '.html', 'r', encoding='utf-8')
    except FileNotFoundError:
        print('\nОШИБКА! Файл "' + name + '.html" не найден, запустите заново')
        return '', name
    else:
        return file.read(), name

def teil_finden(file):
    if file:
        utc = re.search(r'>Часовой пояс<[^\n]+\n([^\n]+\n)', file)
        if utc:
            teil = utc.group(1)
        else:
            print('\nНе тот тип карточек! Ничего не найдено.\nПопробуйте заново с другим файлом.')
            teil = ''
        return teil
        
def zeitzone(teil):
    if teil:
        gefunden = re.findall('>([^<>]+)<', teil)
        ergebnis = ''.join(gefunden)
    else:
        ergebnis = ''
    return ergebnis

def txt_machen(ergebnis, seite, name):
    if ergebnis:
        stadt = re.search('<title>([^—]+)\s—\s', seite).group(1) + '\n'
        txt = open(name + '_timezone.txt', 'w', encoding='utf-8')
        stadt += ergebnis + '\n'
        txt.write(stadt)
        txt.close()
    
def main():
    seite, name = seite_öffnen()
    teil = teil_finden(seite)
    ergebnis = zeitzone(teil)
    txt_machen(ergebnis, seite, name)
    
if __name__ == '__main__':
    main()
