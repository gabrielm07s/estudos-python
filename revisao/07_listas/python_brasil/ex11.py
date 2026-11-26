"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""

l_idades = []
l_alturas = []

for i in range(30):
    print(f"Pessoa {i + 1}º: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))

    l_idades.append(idade)
    l_alturas.append(altura)

media_altura = sum(l_alturas) / len(l_alturas)
lista_idades_alturas = list(zip(l_idades, l_alturas))

qtd_alunos = [
    (idade, altura)
    for (idade, altura) in lista_idades_alturas
    if idade > 13 and altura < media_altura
]

print(f"Quantidade de alunos: {len(qtd_alunos)}")
