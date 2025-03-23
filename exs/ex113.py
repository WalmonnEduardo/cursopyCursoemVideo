
while True:
    try:
        i = int(input('Digite um número inteiro: '))
    except:
        print('\033[0;31mErro Digite um número inteiro!\033[m')
    else:
        break
while True:
    try:
        r = float(input('Digite um número real: '))
    except:
        print('\033[0;31mErro Digite um número real!\033[m')
    else:
        break
print(f'O valor inteiro foi {i} e o real foi {r}')