"""
Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

dias_semana = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado",
}

dia = int(input("Digite um dia da semana: "))

if dia in dias_semana:
    print(dias_semana[dia])
