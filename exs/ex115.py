from lib.interface import *
from lib.arquivo import *
arq = 'exs/pessoas.txt'
if  not arqExiste(arq):
    criarArq(arq)
cabecalho('Sistema Arquivo 1.0')
while True:
    cabecalho('Menu principal')
    r = menu(['Listar Pessoas','Cadastrar Pessoas','Sair do Sistema'])
    if r == 1:
        lerArq(arq)
    elif r == 2:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: ')).strip()
        while True:
            try:
                idade = int(input('Idade: '))
            except KeyboardInterrupt:
                print()
                cabecalho('Encerrado a força','\033[0;31m')
                break
            except:
                cabecalho('Digite um valor inteiro','\033[0;31m')
            else:
                break
        if nome == '':
                nome = 'Desconhecido'
            
        cadastra(arq,nome,idade)
    elif r == 3:
        cabecalho('Encerrando','\033[0;31m')
        break
    else:
        cabecalho('Opição inválida','\033[0;31m')