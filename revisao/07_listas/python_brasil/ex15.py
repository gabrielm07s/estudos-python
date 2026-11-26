"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe
o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

l_atleta = []
l_saltos = []
l_media_saltos = []

while True:
    atleta = input("Atleta: ")

    if not atleta:
        break

    salto_1 = float(input("\nPrimeiro Salto: "))
    salto_2 = float(input("Segundo Salto: "))
    salto_3 = float(input("Terceiro Salto: "))
    salto_4 = float(input("Quarto Salto: "))
    salto_5 = float(input("Quinto Salto: "))

    media_saltos = sum((salto_1, salto_2, salto_3, salto_4, salto_5)) / 5.0

    l_atleta.append(atleta)
    l_saltos.append([salto_1, salto_2, salto_3, salto_4, salto_5])
    l_media_saltos.append(media_saltos)
    print()

dados_atleta = zip(l_atleta, l_saltos, l_media_saltos)

print("\nResultado final: ")
for dados in dados_atleta:
    atleta, saltos, media_saltos = dados
    saltos_formatado = " - ".join(map(str, saltos))
    print(f"Atleta: {atleta}")
    print(f"Saltos: {saltos_formatado}")
    print(f"Média de saltos: {media_saltos:.1f}")
