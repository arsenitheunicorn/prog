#1
def say_hello():
    print('!سلام')
def say_hi(a):
    print('oh hi', a)
say_hello()
a = input('username: ')
say_hi('mark')

#2
n = 7
m = 8
def say_numbers(n, m):
    n = 9
    m = 10
    print(n)
    print(m)

say_numbers(5, 6) #обрати внимание сюда. переменные внутри функции и переменные вне её -- это разные переменные, даже если они имеют одинаковое название

print(n)
print(m)

#3

def saysum(n, m):
    x = n + m
saysum(5, 6)
#print(x) #будет еррор, так как х не существует вне функции

def saysum2(n, m):
    x = n + m
    return x
x = saysum2(5, 6) #вместо х можем задать любую переменную: y, z etc

print(x)

#есть тип данных None (это просто НИЧЕГО).
#например, если фунцкция ничего не возвращает:

z = saysum(5, 7)
print(z)



