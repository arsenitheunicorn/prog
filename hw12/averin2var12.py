import os
import re

def listd():
    li = os.listdir()
    return li

def keine_ziffern(li):
    counter = 0
    for item in li:
        if not re.search('\d', item):
            counter += 1
    print(counter)

def titles(li):
    final = []
    for item in li:
        if item not in final:
            final.append(item)
    print('\n'.join(final))

def main():
    li = listd()
    keine_ziffern(li)
    titles(li)

if __name__ == '__main__':
    main()
    
    
