lista = [1, 2, 3, 4, 5]
k = 2

lista_e = lista[k:] + lista[:k]
print(lista_e)

lista_d = lista[-k:] + lista[:-k]
print(lista_d)
