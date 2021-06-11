#N5 Exercicio 5
"""5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar"""
preço = float(input("Qual o preço da mercadoria?: R$"))
desconto = float(input("Qual o desconto a ser aplicado?(Em porcentagem): %"))
total= print(f"O preço da mercadoria ficou em: R${preço - preço * desconto / 100} e o seu desconto foi de: R$ {preço * desconto / 100}")
