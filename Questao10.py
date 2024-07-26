# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27
import math
carteira = float(input("Informe quntos você tem na sua carteira: "))

dolares = carteira / 5.66

print(f"Você pode comprar US$ {round(dolares, 2)}")
