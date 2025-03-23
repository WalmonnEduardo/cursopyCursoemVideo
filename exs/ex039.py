from datetime import date
ano = int(input('Digite o ano do seu nascimento pequeno gafanhoto: '))
idade = date.today().year - ano
print('Atualmente você meu caro gafanhoto tem {} anos'.format(idade))
if idade == 18:
    print('Chegou seu ano meu gafanhoto de você ser homem e se alistar')
    print('O ano de alistamento é {}'.format(date.today().year))
elif idade < 18:
    print('Ainda falta {} anos para se alistar'.format(18-idade))
    print('O ano de alistamento é {}'.format(date.today().year+(18-idade)))
else:
    print('Você já devia ter se alistado a {} anos atrás'.format(idade-18))
    print('O ano de alistamento é {}'.format(date.today().year-(idade-18)))