"""
beecrowd 1061 - Tempo de um Evento
https://www.beecrowd.com.br/judge/pt/problems/view/1061
"""

DIA_INICIO = int(input().split()[-1])
HORA_INICIAL, MINUTO_INICIAL, SEGUNDO_INICIAL = map(int, input().split(" : "))

DIA_FINAL = int(input().split()[-1])
HORA_FINAL, MINUTO_FINAL, SEGUNDO_FINAL = map(int, input().split(" : "))

TEMPO_INICIAL = (
    (DIA_INICIO * 86400)
    + (HORA_INICIAL * 3600)
    + (MINUTO_INICIAL * 60)
    + SEGUNDO_INICIAL
)

TEMPO_FINAL = (
    (DIA_FINAL * 86400)
    + (HORA_FINAL * 3600)
    + (MINUTO_FINAL * 60)
    + SEGUNDO_FINAL
)

DURACAO_TOTAL = TEMPO_FINAL - TEMPO_INICIAL

DIAS_TOTAL = DURACAO_TOTAL // 86400

HORAS_TOTAL = (DURACAO_TOTAL % 86400) // 3600
MINUTOS_TOTAL = ((DURACAO_TOTAL % 86400) % 3600) // 60
SEGUNDO_TOTAL = ((DURACAO_TOTAL % 86400) % 3600) % 60

print(f"{DIAS_TOTAL} dia(s)")
print(f"{HORAS_TOTAL} hora(s)")
print(f"{MINUTOS_TOTAL} minuto(s)")
print(f"{SEGUNDO_TOTAL} segundo(s)")
