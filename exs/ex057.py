sexo = str(input('Digite seu sexo[F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo[F/M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))