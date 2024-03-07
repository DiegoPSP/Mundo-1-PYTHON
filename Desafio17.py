from math import sqrt, hypot
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
print(f"A hipotenusa com o cateto oposto sendo {cateto_oposto} e o cateto adjacente sendo {cateto_adjacente} é {hipotenusa:.2f}!")

hipot = hypot(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa é {hipot:.2f}")