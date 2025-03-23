from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year-ano
print('O atleta tem {} anos'.format(idade))
if idade < 10:
    print('Mirim')
elif idade < 15:
    print('Infantil')
elif idade < 20:
    print('Junior')
elif idade < 26:
    print('Sênior')
else:
    print('Master')