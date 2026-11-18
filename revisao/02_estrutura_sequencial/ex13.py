# Tempo em segundos
tempo = int(input('Digite o tempo em segundos: '))

horas = tempo // 3600
resto = tempo % 3600
minutos = resto // 60
resto %= 60
segundos = resto

print(f'{horas:>02}:{minutos:>02}:{segundos:>02}')