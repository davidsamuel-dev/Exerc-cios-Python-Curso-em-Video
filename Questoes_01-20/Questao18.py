# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
# cosseno e tangente desse ângulo.
import math

angulo = float(input("Infrme o valor de um angulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"seno: {sen:.2f}\ncossseno: {cos:.2f}\ntangene: {tan:.2f} ")