"""7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Obs. : somente são vendidos um número inteiro de latas."""

#1 litro == 3 M²
#1 tinta == 18L
#1 tinta == 80 reais
#18L == 54m² == 80 reais
#preço = lata * 80

metrosQuadrados = float(input("Digite quantos metros quadrados vão ser pintados: ")) 

lataTinta = (metrosQuadrados / 54)
    

latasParaComprar = 0
z = -1
x = 0

while True:
    z = z + 1
    x = x + 1
    
    latasParaComprar = latasParaComprar + 1
    preço = latasParaComprar * 80

    if lataTinta > z and lataTinta <= x:
        print(f"Você vai precisar de {latasParaComprar} latas de tinta no custo de R${preço} reais")
        break
        





















"""

metrosQuadrados = float(input("Digite quantos metros quadrados vão ser pintados: ")) 


lataTinta = (metrosQuadrados / 54)


if lataTinta <= 1:
    print("Você vai precisar de 1 1atas de tinta no custo de R$80 reais")
    

else:
    latasParaComprar = 1
    z = 0
    x = 1
    while True:
        z = z + 1
        x = x + 1
        latasParaComprar = latasParaComprar + 1
        preço = latasParaComprar * 80
        if lataTinta > z and lataTinta <= x:
            print(f"Você vai precisar de {latasParaComprar} latas de tinta no custo de R${preço} reais")                 
"""
