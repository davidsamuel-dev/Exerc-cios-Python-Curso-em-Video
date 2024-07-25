# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
try:
    num = int(input("Informe um número inteiro: "))
except ValueError:
    print("Informe um número Inteiro")

print(f"Seu antecesssor é: {num - 1}\nE seu sucesor é: {num + 1}")


