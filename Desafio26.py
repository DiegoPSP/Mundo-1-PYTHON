frase = str(input("Digite uma frase qualquer: ")).strip()
print(f"A frase digitada possui {frase.lower().count('a')} letras 'A'!")
print(f"A primeira letra 'A' aparece na posição {frase.lower().find('a')} na sua frase!")
print(f"A última letra 'A' aparece na posição {frase.lower().rfind('a')}")
