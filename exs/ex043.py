p = float(input('Digite seu peso kg: '))
a = float(input('Altura m: '))
imc = p / (a **2)
print('Se imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')