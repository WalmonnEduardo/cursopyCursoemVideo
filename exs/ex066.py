c = s = 0
while True:
    n = int(input('Digite um número[999 para]:'))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foi {c} números e a soma é  {s}')