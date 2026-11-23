"""
beecrowd 1037 - Intervalo
https://www.beecrowd.com.br/judge/pt/problems/view/1037
"""

VALOR = float(input())

if VALOR >= 0 and VALOR <= 25:
    print("Intervalo [0,25]")
elif VALOR > 25 and VALOR <= 50:
    print("Intervalo (25,50]")
elif VALOR > 50 and VALOR <= 75:
    print("Intervalo (50,75]")
elif VALOR > 75 and VALOR <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
