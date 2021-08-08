l1, l2, l3 = input("Digite 3 valores para três lados de um triângulo(digite separado por vírgulas): ").split( "," )
if l1 == l2 == l3:
    print("É um triangulo Equilátereo")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("É um triangulo Isósceles")
else:   print("É um triangulo Escaleno")
