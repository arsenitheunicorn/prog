import textlist

def textli():
    fn = textlist.choose_file()
    text = textlist.read_this_file(fn)
    st = textlist.destroy_tab(text)
    b = textlist.destroy_punct(st)
    fl = textlist.endlich(b)
    fl1 = textlist.del_spaces(fl)
    fl2 = textlist.final_list(fl1)
    return fl2

def dictionary(li):
    d = {}
    for word in li:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def order(d):
    for word in sorted(d, key=d.get, reverse=True):
        print(word, '\t', d[word])

def main():
    li = textli()
    d = dictionary(li)
    order(d)

if __name__ == '__main__':
    main()
