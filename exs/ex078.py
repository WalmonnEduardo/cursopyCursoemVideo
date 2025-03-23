c = 0
nuns = []
while True:
    n = str(input('Digite um número: ')).strip()
    if n.isnumeric():
        nuns.append(int(n))
        c += 1
    if c == 5:
        break
min = min(nuns)
max = max(nuns)
pmin = []
pmax = []
for p,i in enumerate(nuns):
    if i == min:
        pmin.append(p)
    if i == max:
        pmax.append(p)
print(f'O maior valor é {max} e aparece nas posições: {pmax}')
print(f'O menor valor é {min} e aparece nas posições: {pmin}')