import re

def open_text():
    with open ('karenina.xml', 'r', encoding='utf-8') as file:
        text = file.read()
        splited_text = text.split('\n')
    return text, splited_text

def search_count_ana(text):
    amount_ana = re.findall('<ana ', text)
    return len(amount_ana)

def search_count_w(text):
    amount_w = re.findall('<w>', text)
    return len(amount_w)

def counting(a, b):
    print(a / b)

def create_dic(splited_text):
    ed = {}
    for line in splited_text:
        if re.match(r'<w>', line):
            a = re.search('gr="([A-Z]+)[^A-Z]', line)
            res = a.group(1)
            if res in ed:
                ed[res] += 1
            else:
                ed[res] = 1
    return ed

def create_file(ed):
    with open('slovar.txt', 'w', encoding='utf-8') as w:
        for word in sorted(ed, key=ed.get, reverse=True):
            w.write(word + '\t' + str(ed[word]) + '\n')
    

##2 (8 баллов). Составьте частотный словарь всех частей речи в тексте.
##Например: {'APRO': 5, 'S': 277, ...}.
##Распечайте содержимое словаря в отдельный файл
##(на каждой строке "часть речи"<табуляция>"частотность").


def main():
    text, splited = open_text()
    amount_ana = search_count_ana(text)
    amount_w = search_count_w(text)
    counting(amount_ana, amount_w)
    ed = create_dic(splited)
    create_file(ed)

if __name__ == '__main__':
    main()
