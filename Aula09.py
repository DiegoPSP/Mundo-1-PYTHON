frase = 'Curso em Vídeo Python '
print(f'\n1-> {frase}')
print(f'2-> {frase[13]}') #Do 2 ao 6: são métodos de cortar uma string "[começo: fim: compasso]";
print(f'3-> {frase[3:13]}')
print(f'4-> {frase[1:15:]}')
print(f'5-> {frase[1:15:2]}')
print(f'6-> {frase[::2]}')
print(f"7-> {frase.count('o')}") #Contador de caracteres de uma string;
print(f'8-> {frase.upper().count('O')}')#.upper() deixa em maiúcolo;
print(f'9-> {len(frase)}')# Retorna o tamanho do argumento;
print(f'10-> {frase.strip()}')#Remove os espaços em branco da frase tem a variação RIGHT e LEFT;
print(f"11-> {frase.replace('Python', 'Android')}")#Altera a string e coloca o valor que deseja;
print(f"12-> {'Curso' in frase}")#Vai fazer uma varredura na frase e procurar o que foi passado, retorna True ou False;
print(f'13-> {frase.find('vídeo')}')#Faz uma busca na string, retorna -1 se não encontrar;
print(f'14-> {frase.lower().find('vídeo')}')#caso encontre, retorna o primeiro índice da string;
print(f'15-> {frase.split()}')#Divide a string e armazena em uma lista fazendo os cortes nos espaços em branco;
print(f"16-> {frase.split()[0]}")
print(f"17-> {frase.split()[2] [4]}\n")