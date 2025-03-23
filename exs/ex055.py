for i in range(5):
    peso = float(input('Digite o peso da pessoa {}: '.format(i+1)))
    if i == 0:
        min = peso
        max = peso
    else:
        if peso > max:
            max = peso
        if peso < min:
            min = peso
print('O peso máximo é {0} e o mínimo é {1}'.format(max,min))