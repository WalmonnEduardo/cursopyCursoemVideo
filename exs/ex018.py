from math import cos, sin, tan, radians

ang = float(input('Digite o ângulo: '))
se = sin(radians(ang))
co = cos(radians(ang))
ta = tan(radians(ang))
print('Do ângulo {0:.2f} o seu seno é {1:.2f} o cosseno é {2:.2f} e sua tangente é {3:.2f}'.format(ang,se,co,ta))