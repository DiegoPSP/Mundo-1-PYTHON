print("VERIFIQUE SE TRÊS RETAS FORMAM  UM TRIÂNGULO!")
reta_X = float(input("Digite a primeiro reta: "))
reta_Y = float(input("Digite a segundo reta: "))
reta_Z = float(input("Digite a terceiro reta: "))

if reta_X + reta_Y > reta_Z and reta_Y + reta_Z > reta_X and reta_Z + reta_X > reta_Y:
    print("O triangulo pode ser formado!")
else:
    print("A soma de duas retas deve ser maiores que a terceira reta.")
    print("Não é possível formar um triângulo!")