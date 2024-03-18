from datetime import date
ano = int(input("Digite um ano qualquer ou coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 and ano % 100 == 0 or ano % 4 == 0:
    print(f"O ano {ano} É um ano bissexto e em fevereiro terá 29 dias!")
else:
    print(f"O ano {ano} NÃO é um ano bissexto e em fevereiro terá 28 dias!")