"""Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido"""


while True:
    nota = float(input("Digite sua nota(de 0 a 10): "))
    if nota < 0:
        print("O valor inserido é menor que 0, por favor tente novamente")
    if nota >10:
        print("O valor inserido é maior que 10, por favor tente novamente")



"""
while True:
    nota = float(input("Digite sua nota(de 0 a 10): "))
    if nota < 1 or nota > 10:
        print("O valor pedido é inválido, por favor tente novamente")
"""
