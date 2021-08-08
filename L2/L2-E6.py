"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê o salário bruto,
quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
Observe que Salário Bruto - Descontos = Salário Líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
"""

salarioHora = float(input("Digite quanto você ganha por hora: ")) 
hora =  float(input("Digite o número de horas trabalhadas no mês: ")) 

salarioMes = (salarioHora * hora) 
impostoDeRenda = (salarioMes * 11) / 100
inss = (salarioMes * 8) / 100
sindicato = (salarioMes * 5) / 100
liquido = (salarioMes - impostoDeRenda - inss - sindicato)

print(f"O seu salário bruto no mês é R${salarioMes}")
print(f"Você pagou R${impostoDeRenda} de imposto de renda")
print(f"Você pagou R${inss} para o INSS")
print(f"Você pagou R${sindicato} para o sindicato")
print(f"O seu salário líquido com todos os descontos é R${liquido:.2f}")
