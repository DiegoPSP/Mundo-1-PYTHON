from math import cos, sin, tan, radians
angulo = float(input("Digite um ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo {angulo:.2f} possui como SENO {seno:.2f};')
print(f'Como COSSENO {cosseno:.2f};')
print(f'E a TANGENTE {tangente:.2f}.')
