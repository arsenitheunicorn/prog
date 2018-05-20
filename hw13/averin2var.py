import re
import os

def ordner_durchschauen():
    marker = 0
    ordners = []
    for root, dirs, files in os.walk(os.getcwd()):
        di, na = os.path.split(root)
        if re.search('[A-Za-z]', na) == None and re.search('[\s\d]', na) == None and re.search('[.,!]', na) == None:
            ordners.append(na)
    return ordners

def print_da_results(ordn):
    print(len(ordn))

def main():
    ordn = ordner_durchschauen()
    print_da_results(ordn)

if __name__ == '__main__':
    main()
