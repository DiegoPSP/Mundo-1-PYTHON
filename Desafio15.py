dias = int(input("Quantos dias você ficou com o carro alugado? "))
kilometros = float(input("Digite quandos KM você percorreu durante esse tempo: "))
aluguel = (dias * 60) + (kilometros * 0.15)
print(f"O valor que você deverá pagar é R${aluguel:.2f}!")
