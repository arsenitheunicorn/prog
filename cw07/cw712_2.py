def sloz(n, m):
    x = n + m
    return x
def vych(n, m):
    y = n - m
    return y
def main():
    n = int(input('erste Zahl: '))
    m = int(input('zweite Zahl: '))
    x = sloz(n, m)
    y = vych(x, m)
    print(y)
main()

#лучше было задефать sloz и vych:
def sloz1(n, m):
    return n + m
def vych1(n, m):
    return n - m

#in a more 'python way':
#вместо простого вызова функции:
if __name__ == '__main__':
    main()
