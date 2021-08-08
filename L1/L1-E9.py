#N9 Exercicio 9
"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado."""
km = float(input("Quantos km foram percorridos com o carro? "))
dias = float(input("Por quantos dias o carro foi alugado? "))
print(f"O preço a pagar é: {60 * dias + 0.15 * km:.2f} R$")
