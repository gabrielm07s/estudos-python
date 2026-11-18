# Leia uma quantidade de minutos e mostre em horas e minutos (divmod)
tempo_minutos = int(input())

horas, minutos = divmod(tempo_minutos, 60)
print(f'{horas:>02}:{minutos:>02}')