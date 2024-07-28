# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Informe o Km rodado deste carro: "))
dias = int(input("Informe a quantidade de dias pels quais ficou alugado: "))

print(f"O valor total fiicou: R${(km * 0.15) + (dias * 60)}")