"""
beecrowd 1040 - Média 3
https://www.beecrowd.com.br/judge/pt/problems/view/1040
"""

N1, N2, N3, N4 = map(float, input().split())

MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 4) + N4) / 10.0
print(f"Media: {MEDIA:.1f}")

if MEDIA >= 7.0:
    print("Aluno aprovado.")
elif MEDIA >= 5 and MEDIA < 7:
    print("Aluno em exame.")

    NOTA_EXAME = float(input())
    print(f"Nota do exame: {NOTA_EXAME:.1f}")

    MEDIA_FINAL = (MEDIA + NOTA_EXAME) / 2.0

    if MEDIA_FINAL >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {MEDIA_FINAL:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {MEDIA_FINAL:.1f}")
elif MEDIA < 5:
    print("Aluno reprovado.")
