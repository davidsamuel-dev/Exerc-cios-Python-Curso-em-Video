# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Informe o preço do produto: "))

print(f"Este produto com 5% de desconto ficará valendo: R${(preco - (preco * 0.05)):.2f}")