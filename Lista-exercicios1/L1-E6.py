#N6 Exercicio 6
#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
esperada para a viagem. """

distancia = float (input("Qual a distância a percorrer?(Em km): "))
velocm = float (input("Qual a velocidade média do trajeto?(Em km/h):"))
print(f"O tempo de viagem será de: {distancia / velocm:.2f}Horas")
