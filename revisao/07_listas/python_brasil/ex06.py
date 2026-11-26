"""
Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

media_aluno = []

for i in range(10):
    n1, n2, n3, n4 = map(
        float,
        input(f"Digite as notas (1, 2, 3, 4) do {i + 1}º aluno: ").strip().split(),
    )

    media = sum((n1, n2, n3, n4)) / 4.0
    print(f"Média do {i + 1}º aluno: {media:.2f}")

    media_aluno.append(media)
    print()

print(
    f"Número de alunos com média maior ou igual a 7.0: {len([x for x in media_aluno if x >= 7.0])}"
)
