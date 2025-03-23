s = 0
mm = 0
for i in range(4):
    print('---------- {}° PESSOA ----------'.format(i+1))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: '))
    s += idade
    if i == 0 and sexo in 'Mm':
        mi = idade
        nv = nome
    if sexo in 'Mm' and idade > mi:
        mi = idade
        nv = nome
    if sexo in 'Ff' and idade < 20:
        mm += 1
m = s/4
print('A média das idades é {0}, o homem mais velho é {1} e sua idade é {2} e tem {3} mulheres menores de 20 anos'.format(m,nv,mi,mm))