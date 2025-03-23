parar = False
s = 0
c = 1
while not parar:
    n = int(input('Digite um número: '))
    s += n
    if c == 1:
        min = n
        max = n
    else:
        if n > max:
            max  = n
        if n < min:
            min = n
    esc = str(input('Deseja continuar[S/F]: ')).strip().upper()[0]
    if esc not in 'S':
        parar = True
    else:
        c += 1
m = s / c
print('Você digitou {0} números, o maior é {1}, o menor é {2} e a média é {3}'.format(c,max,min,m))