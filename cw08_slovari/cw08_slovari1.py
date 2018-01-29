## тема: Структура данных: Словари
## суть: хранит в себе пары элементов ("ключ" и "значение")
## получать доступ к паре ключ/значение по ключу

## каждый ключ уникален:
## при добавлении пары с ключом, уже имевшимся в словаре, прошлый удаляется

## элементом списка может быть все,
## ключем словаря - только неизменяемый тип данных
## eg: строка (!)
##  s = 'abc'
##  s = 'abcD'
## перезапись
##  l = ['a', 'b', 'c']
##  l[1] = 'd'
## замена

## синтаксис словаря
## d = {}
## d[1] = 'a'
##  где 1 - ключ, 'a' - значение
## d['a'] = 1
##  где 'a' - ключ, 1 - значение
##
## s = d[1]
## кладем "значение" соответствующее ключу 1 в переменную s

## словарь НЕ ХРАНИТ ПОСЛЕДОВАТЕЛЬНОСТЬ
## порядок пар хаотичен
##
## но len() сообщит количество пар ключ-значение
##
## можем обойти словарь циклом for:
## for k in d:
##     v = d[k]
##
## НО словарь нельзя менять в процессе обхода циклом

## задание непустого списка
## d = {'a': 1, 'b': 2}
## 'a', 'b' - ключи, 1, 2 - значения

## функция sorted()
## сортировка по ключу
##
## for k in sorted(d):
##     print(k, d[k])

## сортировка по значению!!!
##
## допустим, в обратном порядке
## допустим, частотный словарь: ключ = слово, частотность = значение
##
## for word in sorted(d, key=d.get, reverse=True):
##     print(d[word])

d = {'ab': 1, 'ba': 2}
if 'c' in d:
    s = d['c']