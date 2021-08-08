"""soma de números sem repetição definida"""
soma = 0

while True:
    x = int(input("Digite números para que faça a soma deles, digite 0(zero) caso queira ver a soma: "))
    
    if x == 0:
        break

    soma = soma + x
     
print(f"a Soma dos números digitados é {soma}")



"""
média da soma de números sem repetição definida

soma = 0
z = 0

while True:
    x = int(input("Digite números para que faça a soma deles, digite 0(zero) caso queira ver a soma: "))
    
    if x == 0:
        break

    soma = soma + x
    z = z + 1 

print(f"a média dos números digitados é {soma/z:.1f}")
"""
