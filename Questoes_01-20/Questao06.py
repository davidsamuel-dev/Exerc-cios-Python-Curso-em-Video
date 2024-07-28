#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math

num = int(input("Informe um número: "))

dobro = num*2
triplo = num*3
raiz = float(math.sqrt(num))

print(f"""
      Dobro {dobro}
      Triplo {triplo}
      Raiz Quadrada: {round(float(raiz), 2)}
      """)
