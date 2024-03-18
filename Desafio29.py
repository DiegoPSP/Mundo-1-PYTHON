velocidade = float(input("Digite a velocidade que você estava: "))
if velocidade <= 80:
    print("Tenha um Bom dia! Dirija com segurança!")
else:
    print(f"\nVocê estava a {velocidade}km/h e ultrapassou o limite de 80 km/h velocidade permitido!")
    velocidade = (velocidade - 80) * 7
    print(f"Sua multa será no valor de R${velocidade}.")
