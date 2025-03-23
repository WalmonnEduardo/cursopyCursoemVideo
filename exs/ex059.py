fim = False
pn = int(input('Digite o primeiro número: '))
sn = int(input('Digite o segundo número: '))
while not fim:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair
    ''')
    esc = int(input('Escolha: '))
    print('='*20)
    if esc == 1:
        print('{0} + {1} = {2}'.format(pn,sn,pn+sn))
    elif esc == 2:
        print('{0} x {1} = {2}'.format(pn,sn,pn*sn))
    elif esc == 3:
        if pn > sn:
            print(pn)
        else:
            print(sn)
    elif esc == 4:
        pn = int(input('Digite o primeiro número: '))
        sn = int(input('Digite o segundo número: '))
    elif esc == 5:
        fim = True
        print('Finalizando...')
    else:
        print('Opção errada.')
    print('='*20)
print('Fim')