nome_completo = str(input('Digite seu nome completo:'))
espacos = nome_completo.strip()
primeiro_nome = nome_completo.split()[0]
print(f"O nome com Capslock é {nome_completo.upper()}!")
print(f"O nome sem Capslock é {nome_completo.lower()}!")
print(f"O nome digitado têm {(len(espacos) - nome_completo.count(" "))} caracteres(sem os espaços em branco)!")
print(f"O primeiro nome tem {len(primeiro_nome)} caracteres!")
