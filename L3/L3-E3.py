"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que
a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
"""

#país A = pop. 80000, taxa crescimento anual 3%

#país B = pop. 200000, taxa crescimento anual 1.5%


populaçaoPaísA = 80000
populaçaoPaísB = 200000
ano = 0

while True:
    ano = ano + 1
    
    crescimentoPaísA = populaçaoPaísA * 0.03 
    populaçaoPaísA = populaçaoPaísA + crescimentoPaísA

    crescimentoPaísB = populaçaoPaísB * 0.015 
    populaçaoPaísB = populaçaoPaísB + crescimentoPaísB

    if populaçaoPaísA >= populaçaoPaísB:
        break

print(f"Foi necessário {ano} anos para que a população do país A ultrapassasse a do país B")

    
