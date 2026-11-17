# Ler tempo em segundos e mostrar horas, minutos e segundos
tempo = int(input('Digite o tempo total em segundos: '))

horas = tempo // 3600
tempo %= 3600
minutos = tempo // 60
tempo %= 60
segundos = tempo

print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')