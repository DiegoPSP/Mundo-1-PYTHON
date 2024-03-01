from math import sqrt, floor, ceil

numero = int(input("Digite um número: "))

raiz = sqrt(numero)

print(f"A raiz de {numero} é {raiz}")
print(f"A raíz de {numero} é igual a {ceil(raiz)}")
print(f"A raíz do número {numero} é igual a {floor(raiz)}")
#import math -> importa toda a biblioteca de matemática;
# from math import sqrt, xxx -> importa a função específica deixando o código mais leve;
# sqrt() -> calcula a raíz quadrada de um número;
# floor() -> arredonda o número pra baixo;
# ceil() -> arredonda o número pra cima;