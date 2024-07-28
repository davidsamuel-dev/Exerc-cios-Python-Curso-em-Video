# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe o salário deste funcionário: "))

novo_salario = salario + (salario * 0.15)

print(f"O salário R${salario} com aumento de 15% agora pasa a valer R${novo_salario}")