minutos = float(input("Quantos minutos foram usados? "))
if minutos < 200:
    preço = 0.20

elif minutos <= 400:
    preço = 0.18
  
elif minutos >=  800:
    preço = 0.08

else:
    preço = 0.15
print(f"Você gastou R${preço * minutos} de telefone")
