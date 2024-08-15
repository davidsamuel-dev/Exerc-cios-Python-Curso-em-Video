# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

alunos = []
qtd = int(input("Informe quantos alunos irá sortear: "))
for i in range(0, qtd):
    alunos.append(input(f"Informe o nome {i+1}° do aluno: "))

print(alunos)

