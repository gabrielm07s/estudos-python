"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2
questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

perguntas = {
    1: "Telefonou para a vítima?",
    2: "Esteve no local do crime?",
    3: "Mora perto da vítima?",
    4: "Devia para a vítima?",
    5: "Já trabalhou com a vítima?",
}

total_res = 0
for pergunta in perguntas.values():
    res = input(pergunta + " (S/N) ").upper()

    if res == "S":
        total_res += 1

if 0 <= total_res <= 1:
    print("Inocente")
elif total_res == 2:
    print("Suspeita")
elif 3 <= total_res <= 4:
    print("Cúmplice")
elif total_res == 5:
    print("Assassino")
