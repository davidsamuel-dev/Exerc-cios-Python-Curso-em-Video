# O mesmo professor do exercício anterior quer sortear a ordem de apresentação 
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
# e mostre a ordem sorteada.

import random

alunos = []
qtd = int(input("Informe quantos alunos irá sortear: "))
for i in range(0, qtd):
    alunos.append(input(f"Informe o nome {i+1}° do aluno: "))

sorteado = random.choice(alunos)

print("O aluno sorteado foi: ", sorteado)
