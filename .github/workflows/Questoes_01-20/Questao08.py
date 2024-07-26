# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input("Informe um valor em metros: "))

centimetros =  valor*100
milimetros = valor*1000

print(f"{valor} convertido para centimetros é: {centimetros} e para milimetros é: {milimetros}")