lista = [("Gabriel", 10), ("Arthur", 6), ("Guilherme", 4)]

lista_ordenada_desc = sorted(lista, key=lambda x: x[1], reverse=True)
print(lista_ordenada_desc)
