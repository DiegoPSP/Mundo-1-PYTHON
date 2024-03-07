from math import floor, ceil

numero = float(input("Digite um número: "))
print(f"A porção inteira arredondando para baixo desse número é {floor(numero)}") 
print(f"A porção inteira arredondando para cima é {ceil(numero)}") 
print(f"O número digitado foi {numero} e a sua porção inteira é {int(numero)}")