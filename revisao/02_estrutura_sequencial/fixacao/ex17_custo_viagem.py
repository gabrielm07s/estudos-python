# Ler distância (km) e o consumo (km/L) e o preço do litro, mostrar litros gastos e custo da viagem
distancia = float(input('Distância (km): '))
consumo = float(input('Consumo (km/L): '))
preco_litro = float(input('Preço litro (R$): '))

litros_gastos = distancia / consumo
custo_viagem = preco_litro * litros_gastos

print(f'Litros gastos: {litros_gastos:.2f} L')
print(f'Custo da viagem: R$ {custo_viagem:.2f}')