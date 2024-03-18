velocidade = int(input("Digite a velocidade que você estava: "))
if velocidade <= 80:
    print()
else:
    print(f"\nVocê estava a {velocidade} e ultrapassou o limite de velocidade permitido!")
    velocidade = (velocidade - 80) * 7
    print(f"Sua multa está no valor de R${velocidade},00.")
