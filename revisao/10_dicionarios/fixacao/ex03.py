produtos = {"Arroz": 15.98, "Energético": 10.11, "Carne": 45.85}

# Atualizando um preco
produtos["Energético"] = 20.50
print(produtos)

# Acrescentando produto
produtos["Peixe"] = 20.50
print(produtos)

{produto: preco for produto, preco in produtos.items()}

for produto, preco in sorted(produtos.items(), key=lambda x: x[1]):
    print(f"Produto: {produto} R$ {preco:.2f}")
