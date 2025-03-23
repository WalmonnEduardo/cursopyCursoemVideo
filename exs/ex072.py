nuns = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número: '))
    if -1 < n < 21:
        break
print(f'O número que você digitou é {nuns[n]}')