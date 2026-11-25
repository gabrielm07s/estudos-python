lista_nomes = []

while True:
    nome = input().strip().lower()

    if nome == "fim":
        break

    lista_nomes.append(nome)

print(f"Lista de nomes: {[x.title() for x in lista_nomes]}")
print(f"O nome 'Ana' apareceram: {lista_nomes.count('ana')}")

if "ana" in lista_nomes:
    posicao = lista_nomes.index("ana")
    print(f"A posição em que apareceu primeiro foi: {posicao}")
else:
    print("O nome Ana não apareceu na lista")
