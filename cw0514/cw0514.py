## 14 May
## модуль os
import os
## функция __
## если вложенные каталоги
## только в циклах

##for root, dirs, files in os.walk(path):
##    for fl in files:
##        if not fl.endswith('.txt'):
##            continue
##        f = open(root, os.sep, fl)

## где root |str| - путь папки, где мы есть
## dirs |list| - список тех директорий, которые лежат в root (если папок нет - список пуст)
## files |list| - -||-, но с файлами
## path - путь главного каталога
## os.sep - разделитель (соответственно ОС)
## .endswith(str) & .startswith(str)
## задача: посчитать директории с буквой 'r', файлы с буквой 'd'. Если двойное попадание: выдать на экран.
def my_path():
    path = input('введите ПОЛНЫЙ ПУТЬ до корневой директории: ')
    return path

def rcounter(root, counters):
    if 'r' in root:
        if 'rcount' in counters:
            counters['rcount'] += 1
        else:
            counters['rcount'] = 1
        return True, counters
    else:
        return False, counters

def dcounter(files, counters):
    if 'd' in files:
        if 'dcount' in counters:
            counters['dcount'] += 1
        else:
            counters['dcount'] = 1
        return True, counters
    else:
        return False, counters

def parsing(path):
    counters = {}
    for root, dirs, files in os.walk(path):
        rc, counters = rcounter(root, counters)
        for fl in files:
            dc, counters = dcounter(fl, counters)
            if rc and dc:
                print(root + os.sep + fl + '\n')
    return counters

def print_da_results(counters):
    for counter in sorted(counters, key=counters.get, reverse=True):
        print(counter, '\t', counters[counter])

def main():
    path = my_path()
    counters = parsing(path)
    print_da_results(counters)

if __name__ == '__main__':
    main()
