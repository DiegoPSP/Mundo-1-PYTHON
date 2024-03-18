ano = int(input("Digite um ano qualquer: "))
if ano % 4 == 0:
    print(f"O ano {ano} É um ano bissexto e em fevereiro terá 29 dias!")
else:
    print(f"O ano {ano} NÃO é um ano bissexto e em fevereiro terá 28 dias!")