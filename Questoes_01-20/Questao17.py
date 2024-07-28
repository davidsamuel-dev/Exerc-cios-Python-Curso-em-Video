# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt

c_o = float(input("Informee o comprimento do cateto oposto: "))
c_a = float(input("Informee o comprimento do cateto adjacente: "))

hi = c_o**2 + c_a**2

print(f"A hipotenusa é: {sqrt(hi)} ")
