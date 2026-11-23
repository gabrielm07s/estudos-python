"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
Entre 9.0 e 10.0         A
Entre 7.5 e 9.0          B
Entre 6.0 e 7.5          C
Entre 4.0 e 6.0          D
Entre 4.0 e zero         E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

n1, n2 = map(float, input().split())

media = (n1 + n2) / 2.0

if 9.0 <= media < 10.0:
    print("Aprovado")
    print("Conceito A")
elif media < 9.0:
    print("Aprovado")
    print("Conceito B")
elif media < 7.5:
    print("Aprovado")
    print("Conceito C")
elif 4.0 < media < 6.0:
    print("Reprovado")
    print("Conceito D")
else:
    print("Reprovado")
    print("Conceito E")
