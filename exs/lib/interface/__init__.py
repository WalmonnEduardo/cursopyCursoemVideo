def linha(tamanho=42):
    return '='*tamanho


def cabecalho(txt,color='\033[m'):
    print(color,end='')
    print(linha())
    print(txt.center(42))
    print(linha(),end='')
    print('\033[m')

def menu(lista):
    c = 1
    print(linha())
    for item in lista:
        print(f'{c} -> {item}')
        c += 1
    print(linha())
    while True:
        try:
            r = int(input('Escolha uma opição: '))
        except KeyboardInterrupt:
            print()
            cabecalho('Encerrado a força','\033[0;31m')
            break
        except:
            cabecalho('Digite um valor inteiro','\033[0;31m')
        else:
            return r
            break