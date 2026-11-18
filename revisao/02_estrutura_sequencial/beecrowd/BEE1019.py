"""
beecrowd 1019 - Conversão de Tempo
https://www.beecrowd.com.br/judge/pt/problems/view/1019
"""

TIME = int(input())

HOURS = TIME // 3600
REST = TIME % 3600
MINUTES = REST // 60
REST %= 60
SECONDS = REST

print(f"{HOURS}:{MINUTES}:{SECONDS}")
