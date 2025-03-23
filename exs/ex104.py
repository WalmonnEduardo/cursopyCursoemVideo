def leiaint(m):
    ok = False
    while not ok:
        n = input(m)
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Escreva um número válido\033[m')
    return f'Você digitou o número {n}'
print(leiaint('Digite um número: '))