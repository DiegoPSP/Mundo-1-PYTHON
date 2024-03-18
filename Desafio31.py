distancia = float(input("Digite a distância em Kilometros que você vai fazer: "))
if distancia <= 200:
    distancia = distancia * 0.50
    print(f"Sua passagem ficou no valor de R${distancia}!")
else:
    distancia = distancia * 0.45
    print(f"Sua passagem ficou no valor de R${distancia}!")
