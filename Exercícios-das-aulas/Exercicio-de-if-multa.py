v = float(input("Digite a velocidade do seu carro: "))
if v > 110:
    multa = (v - 110) * 5
    print(f"PARADO!!!\nVocê recebeu uma multa no valor de R${multa:.2f}")
else:
    print("Ta safe irmão, pode passar")

             
