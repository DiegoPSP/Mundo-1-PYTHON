print('='*20) #Replica o '=' 20 vezes;
nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:^20}!')#Centraliza a escrita dentre 20 espaços;
print(f'Prazer em te conhecer {nome:=^20}!')#Centraliza a escrita dentre 20 espaços colocando o sinal no lugar em branco;

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1 + n2
multiplica = n1 * n2
divide = n1 / n2
divide_inteira = n1 // n2
expoente = n1 ** n2
print(f'A soma é {soma}, o produto é {multiplica} e a divisão é {divide:.3f}')
print(f'Divisão inteira é {divide_inteira} e a potência é {expoente}')
