lista_palavras = ["Oi", "Abracadabra", "Alakazam", "Putz", "Legal", "Ai"]

nova_lista = sorted(
    lista_palavras, key=lambda palavra: (len(palavra), palavra.lower())
)
print(nova_lista)
