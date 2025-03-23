v = float(input('Digite a sua velocidade: '))
if v > 80:
    p = (v-80)*7
    print('Você foi multado em R${0:.2f} por exceder a velocidade de 80km/h'.format(p))
else:
    print('Você está dentro do limite de velocidade')
print('Digija com cuidado')