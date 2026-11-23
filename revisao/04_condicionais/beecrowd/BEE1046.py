"""
beecrowd 1046 - Tempo de Jogo
https://www.beecrowd.com.br/judge/pt/problems/view/1046
"""

HORA_INICIAL, HORA_FINAL = map(int, input().split())
TEMPO_TOTAL = 0

if HORA_INICIAL > HORA_FINAL:
    TEMPO_TOTAL = (24 - HORA_INICIAL) + HORA_FINAL
elif HORA_FINAL > HORA_INICIAL:
    TEMPO_TOTAL = HORA_FINAL - HORA_INICIAL
else:
    TEMPO_TOTAL = 24

print(f"O JOGO DUROU {TEMPO_TOTAL} HORA(S)")
