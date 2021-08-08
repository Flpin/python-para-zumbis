"""5. Faça um Programa que leia três números e mostre o maior e o menor deles."""



n1, n2, n3 = input("Digite três números(entre vírgulas) para saber qual o maior e o menor número: ").split(",")


while True:
    
    if n1 != n2 or n2 != n3:
        maiorNumero = n1
        if (n2 > maiorNumero):
            maiorNumero = n2
        if (n3 > maiorNumero): 
            maiorNumero = n3

        menorNumero = n2

        if (n1 < menorNumero):
            menorNumero = n1
        if (n3 < menorNumero):
            menorNumero = n3
            

        print(f"O maior número é: {maiorNumero}")
        print(f"O menor número é: {menorNumero}")
    break

if n1 == n2 ==n3:
    print("Todos os números são iguais")
   
        










