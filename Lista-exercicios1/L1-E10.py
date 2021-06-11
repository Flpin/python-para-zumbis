#N10 Exercicio 10
"""Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias."""
cigarro = float(input("Quantos ciggaros você fuma por dia? "))
anos = float(input("Quantos anos você ja fuma? "))
print(f"Você perdeu um total de {cigarro * 365 * anos * 10 / 1440:.2f} dias de vida")
