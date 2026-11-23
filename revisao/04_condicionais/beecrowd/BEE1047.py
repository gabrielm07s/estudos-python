"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

Exemplo de Entrada	Exemplo de Saída
7 8 9 10
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

7 7 7 7
O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

7 10 8 9
O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
"""

HORA_INICIAL, MINUTO_INICIAL, HORA_FINAL, MINUTO_FINAL = map(int, input().split())

TEMPO_INICIAL = (HORA_INICIAL * 60) + MINUTO_INICIAL
TEMPO_FINAL = (HORA_FINAL * 60) + MINUTO_FINAL
HORA_TOTAL, MINUTO_TOTAL = 0, 0

if TEMPO_INICIAL > TEMPO_FINAL:
    HORA_TOTAL, MINUTO_TOTAL = (
        ((1440 - TEMPO_INICIAL) + TEMPO_FINAL) // 60,
        ((1440 - TEMPO_INICIAL) + TEMPO_FINAL) % 60,
    )
elif TEMPO_FINAL > TEMPO_INICIAL:
    HORA_TOTAL, MINUTO_TOTAL = (
        (TEMPO_FINAL - TEMPO_INICIAL) // 60,
        (TEMPO_FINAL - TEMPO_INICIAL) % 60,
    )
else:
    HORA_TOTAL, MINUTO_TOTAL = (24, 0)

print(f"O JOGO DUROU {HORA_TOTAL} HORA(S) E {MINUTO_TOTAL} MINUTO(S)")
