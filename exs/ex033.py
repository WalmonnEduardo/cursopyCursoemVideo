n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2 and n1 > n3 :
    max = n1
if n2 > n1 and n2 > n3:
    max = n2
if n3 > n1 and n3 > n2:
    max = n3
if n1 < n2 and n1 < n3 :
    min = n1
if n2 < n1 and n2 < n3:
    min = n2
if n3 < n1 and n3 < n2:
    min = n3
print("""O maior é {0}
O menor é {1}""".format(max,min))