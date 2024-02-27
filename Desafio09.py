numero = int(input("Digite um numero: "))
limite = int(input("Digite até qual ele deve ser multiplicado: "))

def taboada(numero, limite):
    print(f"\nTABELA DE MULTIPLICAÇÃO DE {numero} até {limite}:\n")
    print('*' * 12)
    for i in range(0, limite + 1):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado:2}")
    print('*' * 12)
taboada(numero, limite)
