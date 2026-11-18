print(f'[{3.14159:010.2f}]')

valor_formatado = f'{1234567.891:,.2f}'.replace('.', 'x').replace(',', '.').replace('x', ',')
print(f'[{valor_formatado}]')