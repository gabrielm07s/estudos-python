"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: R$ "))
    estado_civil = input("Estado civil (S/C/V/D): ").lower()

    if (
        (len(nome) < 3)
        or (idade > 150 or idade < 0)
        or (salario < 0)
        or (estado_civil not in ["s", "c", "v", "d"])
    ):
        print("Erro! Tente novamente")
        continue
    else:
        break
