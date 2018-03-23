import re

def text_öffnen():
    name = input('Введите название текста БЕЗ расширения: ')
    name += '.txt'
    file = open(name, 'r', encoding='utf-8')
    tex = file.read()
    text = tex.lower()
    return text

def liste_der_wf():
    wortforme = ['йти', 'шедши', 'йденн?[аоуы]?[^ш]*', 'ш[её]л', 'шл[ао]', 'йд[яуиеё][мтш]?[еь]?']
    wf = []
    for form in wortforme:
        form2 = "\s(на" + form + 'с?[ья]?)\W'
        wf.append(form2)
    return wf

def finden(wf, text):
    found = []
    for form in wf:
        form_found = re.findall(form, text)
        for wort in form_found:
            found.append(wort)
    return found

def nur_ein_wort(found):
    ergebnis = []
    for wort in found:
        if wort not in ergebnis:
            ergebnis.append(wort)
    print(ergebnis)

def main():
    text = text_öffnen()
    wf = liste_der_wf()
    found = finden(wf, text)
    nur_ein_wort(found)

if __name__ == '__main__':
    main()
    
# найти
# нашедши
# найденн?[аоуы]?[^ш]*
# наш[её]л
# нашл[ао]
# найд[яуиеё][мтш]?[еь]?
#
#
