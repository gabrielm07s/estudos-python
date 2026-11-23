"""
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês.
O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar.
Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss.
Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplo de Entrada	Exemplo de Saída
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)
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
    (DIA_FINAL * 86400) + (HORA_FINAL * 3600) + (MINUTO_FINAL * 60) + SEGUNDO_FINAL
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
