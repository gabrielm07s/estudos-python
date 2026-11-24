"""
beecrowd 1160 - Crescimento Populacional
https://www.beecrowd.com.br/judge/pt/problems/view/1160
"""

T = int(input())

for i in range(T):
    ANOS = 0
    PA, PB, G1, G2 = input().split()
    PA, PB, G1, G2 = int(PA), int(PB), float(G1), float(G2)

    while PA <= PB:
        if ANOS > 100:
            break

        PA += int((PA * G1) // 100)
        PB += int((PB * G2) // 100)
        ANOS += 1

    if ANOS > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{ANOS} anos.")
