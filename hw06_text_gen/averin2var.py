import random
## размер "стиха" - 101010010, где 1 - ударный слог, 0 - безударный

def voc():
    with open('voc.txt', 'r', encoding='utf-8') as f:
        li = f.read()        
        voc = li.split('\n')
    return random.choice(voc)

def imp_dat():
    with open('imp.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        imp = li.split('\n')
    return random.choice(imp)

def pronoun_dat():
    with open('pr_d.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        pr_d = li.split('\n')
    return random.choice(pr_d)

def adverb():
    with open('adverb.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        adv = li.split('\n')
    return random.choice(adv)

def punct():
    with open('punct.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        punct = li.split('\n')    
    return random.choice(punct)

def number():
    n = input('Укажите число s/pl ')
    return n
        

def word(n):
    a = ''
    if n == 's':
        with open('word_s.txt', 'r', encoding='utf-8') as f:
            li = f.read()
            word_s = li.split('\n')
        a = random.choice(word_s)
    else:
        with open('word_pl.txt', 'r', encoding='utf-8') as f:
            li = f.read()
            word_pl = li.split('\n')
        a = random.choice(word_pl)
    return a

def verb(n):
    a = ''
    if n == 's':
        with open('verb_s.txt', 'r', encoding='utf-8') as f:
            li = f.read()
            verb_s = li.split('\n')
        a = random.choice(verb_s)
    else:
        with open('verb_pl.txt', 'r', encoding='utf-8') as f:
            li = f.read()
            verb_pl = li.split('\n')
        a = random.choice(verb_pl)
    return a

def time():
    with open('time.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        time = li.split('\n')
    return random.choice(time)

def part():
    with open('part.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        part = li.split('\n')
    return random.choice(part)

def anim():
    with open('anim.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        anim = li.split('\n')
    return random.choice(anim)

def verb_anim():
    with open('verb_anim.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        verb = li.split('\n')
    return random.choice(verb)

def place():
    with open('place.txt', 'r', encoding='utf-8') as f:
        li = f.read()
        place = li.split('\n')
    return random.choice(place)

def verse1():
    return voc() + ', ' + imp_dat() + ' ' + pronoun_dat() + ' ' + adverb() + ' и ' + adverb() + punct()

def verse2():
    no = number()
    return word(no) + ' ' + verb(no) + ' ' + time() + ' ' + part() + ' ' + adverb() + punct()

def verse3():
    return anim() + ' ' + adverb() + ' ' + verb_anim() + ' в ' + place() + punct()

def linie():
    r = random.randint(1, 3)
    linie = ''
    if r == 1:
        linie = verse1()
    if r == 2:
        linie = verse2()
    else:
        linie = verse3()
    return linie

def main():
    counter = 0
    lin = '\n'
    while counter != 4:
        counter += 1
        lin += linie()
        lin += '\n'
    print(lin)

if __name__ == '__main__':
    main()
