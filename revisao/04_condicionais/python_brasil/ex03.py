"""
Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

F - Feminino
M - Masculino
Sexo Inválido.
"""

sexo = input("Digite o sexo: (F/M) ").strip()
sexos = ["F", "M"]

if sexo in sexos:
    print(f"{'M - Masculino' if sexo == 'M' else 'F - Feminino'}")
else:
    print("Sexo inválido")
