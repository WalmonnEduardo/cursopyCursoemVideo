n = 0
c = 0
for i in range(1,501):
    if i%3 == 0 and i%2 == 1:
        n += i
        c += 1
print("A soma de todos os {} números dá {}".format(c,n))