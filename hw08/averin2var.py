import random

def tabelle_öffnen():
    wb = {}
    with open('words.csv', 'r', encoding='utf-8') as f:
        fl = f.read()
        flines = fl.splitlines()
        for line in flines:
            massive = line.split(',')
            wb[massive[1]] = massive[0]
    return wb

def funktion(wb):
    word = random.choice(list(wb.keys()))
    check = input(wb[word] + ' ' + '.'*len(word) + '\n')
    if check == word:
        print('Richtig! Gut gemacht! \n)')
    else:
        print("Sorry, you're not a winner! \n(((")
    
def main():
    wb = tabelle_öffnen()
    funktion(wb)

if __name__ == '__main__':
    main()
