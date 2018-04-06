# (исходное, итог, строка)
# N: 0, и; G: а, ов; D: у, ам; A: а, ов; I: ом, ами; Pr: е, ах
# ОСН[иаоуе]?[вмх]?и?
import re

def open_text():
    f = open('vikings.txt', 'r', encoding='utf-8')
    return f.read()

def every_viking_is_a_chipmunk(txt):
    bur = re.sub(r'(\W|^)ви(.?)кинг([иаоуе]?[вмх]?и?)(-|\W|$)', r'\1бурундук\3\4', txt)
    bur = re.sub(r'(\W|^)Ви(.?)кинг([иаоуе]?[вмх]?и?)(-|\W|$)', r'\1Бурундук\3\4', bur)
    return bur

def make_text(txt):
    with open('burunduks.txt', 'w', encoding='utf-8') as f:
        f.write(txt)

def main():
    txt_v = open_text()
    txt_b = every_viking_is_a_chipmunk(txt_v)
    make_text(txt_b)

if __name__ == '__main__':
    main()
