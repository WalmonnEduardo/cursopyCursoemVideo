from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Teceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolha = choice(lista)
print('O aluno escolhido foi {}'.format(escolha))