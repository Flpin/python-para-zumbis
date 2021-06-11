#N3 Exercicio 3
#1 dia = 24 horas
#24horas = 1440 minutos
#1440minutos = 86400 segundos
"""3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos.
"""

dias = float (input ("Dias: "))
horas = float (input ("Horas: "))
minutos = float (input ("Minutos: "))
segundos = float (input ("Segundos: "))

diasEmSegundos = dias*24*60*60
horasEmSegundos = horas*60*60
minutosEmSegundos = minutos*60
total= diasEmSegundos + horasEmSegundos + minutosEmSegundos + segundos
print(f"O número total em segundos é: {total}")

