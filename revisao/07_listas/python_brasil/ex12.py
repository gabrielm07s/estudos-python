"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).
"""

temperatura_media = []

for i in range(12):
    temperatura_media.append(
        float(input(f"Digite a temperatura média do mês {i + 1}: "))
    )

media_anual = sum(temperatura_media) / len(temperatura_media)

meses_acima_media = [
    (indice, temp_mes)
    for (indice, temp_mes) in enumerate(temperatura_media)
    if temp_mes > media_anual
]

for indice, temp_mes in meses_acima_media:
    print(f"Mês: {indice} - {temp_mes} ºC")
