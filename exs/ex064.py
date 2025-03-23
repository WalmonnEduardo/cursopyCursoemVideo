n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número [999 para]: '))
    if n != 999:
        s += n
        c += 1
print('O a soma dos {0} números é {1}'.format(c,s))