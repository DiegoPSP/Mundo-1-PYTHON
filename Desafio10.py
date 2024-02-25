carteira = float(input("Digite quanto de dinheiro você tem na carteira:R$ "))
dolar = 3.27
conversão = carteira / dolar
print(f"Com o valor R${carteira}, você pode comprar até US${conversão:.2f} Dólares")