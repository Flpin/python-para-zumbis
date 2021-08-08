"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    nome = input("Digite seu login de usuário: ")
    senha = input("Digite sua se'   nha: ")
    if senha == nome:
        print("ERRO, parece que seu nome e senha são iguais, por favor tente novamente")
    else:
        break
         


        
    
