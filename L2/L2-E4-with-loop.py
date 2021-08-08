"""4. Faça um Programa que leia três números e mostre o maior deles."""

while True:
    n1, n2, n3  = input("Digite três números(entre vírgulas) para saber qual o maior número: ").split(",")

    if n1 > n2 and n1 > n3:
        print("O primeiro número é maior")

    elif n2 > n3 and n2 > n1:
        print("O segundo número é maior")

    elif n3 > n2 and n3 > n1:
        print("O terceiro número é maior")

    else:
        print("Os números são iguais")



