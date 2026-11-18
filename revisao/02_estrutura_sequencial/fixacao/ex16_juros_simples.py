# Juros Simples
capital = float(input('Capital: '))
taxa = float(input('Taxa: '))
meses = int(input('Meses: '))

juros_simples = capital * (taxa / 100) * meses
montante = capital + juros_simples

print(f'Juros simples: R$ {juros_simples:.2f} | Montante: R$ {montante:.2f}')