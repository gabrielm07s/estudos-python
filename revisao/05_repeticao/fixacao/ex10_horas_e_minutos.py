# Mostre todas as horas e minutos de um dia (00:00 a 23:59)
# somente com minutos múltiplos de 15

for hora in range(24):
    for minutos in range(60):
        if minutos % 15 == 0:
            print(f"{hora:02d}:{minutos:02d}")
    print()
