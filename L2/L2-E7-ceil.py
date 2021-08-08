"""7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Obs. : somente são vendidos um número inteiro de latas."""

#1 litro == 3 M²
#1 tinta == 18L
#1 tinta == 80 reais
#18L == 54m² == 80 reais
#preço = lata * 80

import math

metrosQuadrados = float(input("Digite quantos metros quadrados vão ser pintados: ")) 

lataTinta = (metrosQuadrados / 54)

lata = math.ceil(lataTinta)

print(f"{lata} latas de tinta e o preço a se pagar é R${lata * 80}")





