import re

def öffnen_file():
    with open('grgrus.html', 'r', encoding='utf-8') as file:
        html = file.read()
    return html

def familie(html):
    dze = re.findall('>[А-Яа-яЁё ]+?дзе</a>', html)
    shv = re.findall('>[А-Яа-яЁё ]+?швили</a>', html)
    if len(dze) > len(shv):
        k = round(len(dze)/len(shv), 2)
        print('Людей с фамилией на -дзе в ', k, ' раз больше, чем на -швили')
    elif len(dze) < len(shv):
        k = round(len(shv)/len(dze), 2)
        print('Людей с фамилией на -дзе в ', k, ' раз меньше, чем на -швили')
    else:
        print("Людей на -дзе столько же, сколько на -швили")
    return dze, shv

def beria(html):
    ija = re.findall('>[А-Я][а-яё]+ [А-Я][а-яё]+ [А-Я][а-яё]+?ия</a>', html)
    print('Людей с фамилией на -ия: ', len(ija))
    return ija

def find_galaktions(html, dze, shv):
    dze.extend(shv)
    gal = []
    for name in dze:
        name_l = name.split( )
        if len(name_l[0]) > 7:
            gal.append(name)
    return gal

def change(html, gal):
    for name in gal:
        galak = re.sub('>[А-Я][а-яё]+ ', '>Галактион ', name)
        html = html.replace(name, galak)
    with open('galak.html', 'w', encoding='utf-8') as file:
        file.write(html)
    

def main():
    html = öffnen_file()
    dze, shv = familie(html)
    ija = beria(html)
    names = find_galaktions(html, dze, shv)
    change(html, names)
    
if __name__ == '__main__':
    main()
