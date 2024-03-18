maior = int(input("Digite um número: "))
meio = int(input("Digute outro número: "))
menor = int(input("Digite o mais um número: "))
aux = int
if maior < meio or maior < menor:
    aux = maior
    maior = meio
    meio = aux
    print(f"a1- {maior}\n2- {meio}\n3- {menor}")

if maior < menor:
    aux = maior
    maior = menor
    menor = aux
    print(f"b1- {maior}\n2- {meio}\n3- {menor}")

if meio < menor:
    aux = menor
    menor = meio
    meio = aux
    print(f"c1- {maior}\n2- {meio}\n3- {menor}")

print(f"O maior número é {maior}, o do meio é {meio} e o menor número é {menor}.")
