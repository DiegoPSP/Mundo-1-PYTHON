maior = int(input("Digite um número: "))
meio = int(input("Digute outro número: "))
menor = int(input("Digite o mais um número: "))
aux = int
if maior < meio or maior < menor:
    aux = maior
    maior = meio
    meio = aux

if maior < menor:
    aux = maior
    maior = menor
    menor = aux

if meio < menor:
    aux = menor
    menor = meio
    meio = aux
print(f"O maior número é {maior}, o do meio é {meio} e o menor número é {menor}.")
