lista = [1, 1, 1, 2, 3, 4, 5, 5, 5]
sem_repetidos = []

removidos = 0
for n in lista:
    if n not in sem_repetidos:
        sem_repetidos.append(n)
    else:
        removidos += 1


print(lista)
print(sem_repetidos)
print(f"Removidos: {removidos}")
