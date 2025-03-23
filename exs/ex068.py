from random import randint
c = 0
while True:
    jc = randint(0,10)
    while True:
        esc = str(input('Par ou ímpar[I/P]: ')).strip().upper()[0]
        if esc in 'IP':
            break
    j = int(input('Digite um número: '))
    if (j + jc) % 2 == 0:
        res = 'P'
    else:
        res = 'I'
    if not (esc == res):
        print(f'Você jogou {j} e o computador jogou {jc}, o resultado deu {res}, Você perdeu')
        print('='*20)
        break
    else:
        print(f'Você jogou {j} e o computador jogou {jc}, o resultado deu {res}, Você venceu')
        print('='*20)
    c += 1
print(f'Você teve {c} vitórias consecultivas')