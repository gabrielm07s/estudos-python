"""
beecrowd 1131 - Grenais
https://www.beecrowd.com.br/judge/pt/problems/view/1131
"""

GRENAIS = 0
VITORIAS_INTER = 0
VITORIAS_GREMIO = 0
EMPATES = 0

while True:
    GOLS_INTER, GOLS_GREMIO = map(int, input().split())
    GRENAIS += 1

    if GOLS_INTER > GOLS_GREMIO:
        VITORIAS_INTER += 1
    elif GOLS_GREMIO > GOLS_INTER:
        VITORIAS_GREMIO += 1
    else:
        EMPATES += 1

    print("Novo grenal (1-sim 2-nao)")
    X = int(input())

    if X == 1:
        continue
    else:
        print(f"{GRENAIS} grenais")
        print(f"Inter:{VITORIAS_INTER}")
        print(f"Gremio:{VITORIAS_GREMIO}")
        print(f"Empates:{EMPATES}")

        if VITORIAS_GREMIO > VITORIAS_INTER:
            print("Gremio venceu mais")
        elif VITORIAS_INTER > VITORIAS_GREMIO:
            print("Inter venceu mais")
        else:
            print("Nao houve vencedor")
        break
