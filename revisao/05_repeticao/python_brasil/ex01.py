"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome_usuario = input("Usuário: ")

while True:
    senha = input("Senha: ")

    if senha == nome_usuario:
        print("Erro!")
        continue
    else:
        break
