nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2
print(f"\nSua primeira nota é {nota1} e a segunda nota é {nota2} e a média delas é {media}.")

if media < 5:
    print("Esse aluno(a) foi REPROVADO!\n")
elif media >= 5 and media < 7:
    print("Esse aluno(a) precisa fazer a prova de RECUPERAÇÃO!\n")
else:
    print("Esse aluno(a) foi APROVADO!\n")