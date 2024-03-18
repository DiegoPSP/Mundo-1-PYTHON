salario = float(input("Digite seu salário: "))
if salario >= 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)

print(f"Seu novo salário será no valor de R${salario}")