# Calcular preco final de um produto com 10% de desconto
preco = float(input('Digite o preço do produto: '))
desconto = 10

preco_final = preco * (1 - (desconto / 100))
print(f'R$ {preco_final:.2f}')