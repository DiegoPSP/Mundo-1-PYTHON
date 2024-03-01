from math import sqrt
cateto_oposto = int(input("Digite o cateto oposto: "))
cateto_adjacente = int(input("Digite o cateto adjacente: "))

hipotenusa = sqrt(cateto_oposto * cateto_oposto + cateto_adjacente * cateto_adjacente)
print(f"A hipotenusa com o cateto oposto sendo {cateto_oposto} e o cateto adjacente sendo {cateto_adjacente} é {hipotenusa}!")