s = float(input('Digite seu salário: '))
if s > 1250:
    a = s + (s*0.1)
else:
    a = s + (s*0.15)
print('O seu salário novo será R${:.2f}'.format(a))