"""Sorteie 10 inteiros entre 1 e 100 para uma lista
e descubra o maior e o menor valor, sem usar as funções max e min.
"""
x = 1
sorteio = []
maiorNumero = sorteio[0]
menorNumero = sorteio[0]

for i in range(10):sorteio.append(int(input("Digite um número para a sua lista: ")))

for i in range(9):
    if sorteio[x] > maiorNumero: 
        maiorNumero = sorteio[x]
    if sorteio[x] < menorNumero:
        menorNumero = sorteio[x]
    x = x + 1
    
print(f"O maior número da sua lista é: {maiorNumero} e o menor: {menorNumero}")


