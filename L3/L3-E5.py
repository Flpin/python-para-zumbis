"""Dados dois números inteiros positivos,
determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
"""
n1, n2 = input("Digite dois números(entre vírgulas) para saber qual o máximo divisor comum entre eles: ").split(",")

n1 = int(n1) 
n2 = int(n2) 

while n2 != 0:
      n1, n2 = n2, n1 % n2

print(f"O máximo divisor comum é {n1}")

