from random import randint
def luck(nuns):
    for i in range(5):
        nuns.append(randint(1,10))
def sp(nuns):
    print('A soma dos pares da lista ',end='')
    s = 0
    for i in nuns:
        if i % 2 == 0:
            s += i
        print(i,end=' ')
    print(f' a soma dos pares é {s}')
nuns = list()
luck(nuns)
sp(nuns)