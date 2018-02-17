import random

def tabelle_öffnen():
    wb = {}
    keys = []
    with open('words.csv', 'r', encoding='utf-8') as f:
        fl = f.read()
        flines = fl.splitlines()
        for line in flines:
            massive = line.split(',')
            wb[massive[1]] = massive[0]
            keys.append(massive[1])
    return wb, keys

def funktion(wb, keys):
    word = random.choice(keys)
    check = input(wb[word] + ' ' + '.'*len(word) + '\n')
    if check == word:
        print('Richtig! Gut gemacht! \n)')
    else:
        print("Sorry, you're not a winner! \n(((")
    
def main():
    wb, keys = tabelle_öffnen()
    funktion(wb, keys)

if __name__ == '__main__':
    main()
