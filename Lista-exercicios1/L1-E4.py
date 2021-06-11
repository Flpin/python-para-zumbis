#N5 Exercicio 5
"""4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário."""

salario = float(input("Digite seu sálario: R$"))
aumento = float(input("Digite o seu aumento do sálario(Em porcentagem): %"))
aumento = aumento/100 * salario
salario = aumento+ salario
print(f"O seu aumento foi de: R${aumento:.2f}")
print(f"O seu novo sálario é de: R${salario:.2f}")
