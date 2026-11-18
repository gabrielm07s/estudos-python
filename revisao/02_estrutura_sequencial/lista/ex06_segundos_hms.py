tempo = int(input())

horas = tempo // 3600
tempo %= 3600
minutos = tempo // 60
tempo %= 60
segundos = tempo

print(f'{horas:>02}:{minutos:>02}:{segundos:>02}')