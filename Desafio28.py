from random import randint

pense = randint(0, 5)
print('\nEu pensei em um número, tente adivinhá-lo!')
chance = int(input("Digite um número de 0 a 5: "))

if chance == pense:
    print(f"\nVocê acertou! Eu pensei em {pense} e você digitou {chance}")
else:
    print(f"\nVocê errou! Você digitou {chance} e eu pensei em {pense}")
print('\nFIM DA BRINCADEIRA!\n') 