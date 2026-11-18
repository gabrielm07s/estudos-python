# Leia o preço e a quantidade de um produto e mostre o total no formato R$ 1.234,56
preco = float(input())
quantidade = int(input())

total = preco * quantidade
total_formatado = f'{total:,.2f}'.replace('.', 'x').replace(',', '.').replace('x', ',')
print(f'Preço total: R$ {total_formatado}')