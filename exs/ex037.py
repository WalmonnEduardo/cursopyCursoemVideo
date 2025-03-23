num = int(input('Digite um número inteiro: '))
print('''Escolha uma dessa bases para conversão:
=====================
[ 1 -> Binário      ]
=====================
[ 2 -> Octál        ]
=====================
[ 3 -> Hexadecimal  ]
=====================
''')
esc = int(input('Escolha: '))
if esc == 1:
    print('O número {} converitodo para binário é {}'.format(num,bin(num)[2:]))
elif esc == 2:
    print('O número {} converitodo para octál é {}'.format(num,oct(num)[2:]))
elif esc == 3:
    print('O número {} converitodo para hexadecimal é {}'.format(num,hex(num)[2:].upper()))
else:
    print('Tente novamente!')