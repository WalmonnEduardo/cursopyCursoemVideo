from lib.interface import *
def arqExiste(arq):
    try:
        a = open(arq,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(arq):
    try:
        a = open(arq,'wt+')
        a.close()
    except:
        cabecalho('Houve um erro ao criar o arquivo','\033[0;31m ')

def lerArq(arq):
    try:
        a = open(arq,'rt')
    except:
        cabecalho('Houve um erro ao ler o arquivo','\033[0;31m ')
    else:
        cabecalho('Pessoas Cadastradas')
        for l in a:
            dado = l.split(':')
            print(f'{dado[0]:<20}:{dado[1].strip():>3} anos')
    finally:
        a.close

def cadastra(arq,nome,idade=0):
    try:
        a = open(arq,'at')
    except:
        cabecalho('Houve um erro na abertura do arquivo')
    else:    
        try:
            a.write(f'{nome}:{idade}\n')
        except:
            cabecalho('Houve um erro na escrita','\033[0;31m ')
        else:
            cabecalho(f'Novo registro {nome} adicionado')
            a.close()