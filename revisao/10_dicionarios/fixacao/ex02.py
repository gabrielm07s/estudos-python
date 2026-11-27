produtos = {"Arroz": 15.98, "Energético": 10.11, "Carne": 45.85}

# Atualizando um preco
produtos["Energético"] = 20.50
print(produtos)

# Acrescentando produto
produtos["Peixe"] = 20.50
print(produtos)

# Removendo com pop
removido = produtos.pop("Peixe")
print(f"Removido: {removido}, Produtos: {produtos}")
