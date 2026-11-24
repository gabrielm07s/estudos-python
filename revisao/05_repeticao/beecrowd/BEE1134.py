"""
beecrowd 1134 - Tipo de Combustível
https://www.beecrowd.com.br/judge/pt/problems/view/1134
"""

ALCOOL = 0
GASOLINA = 0
DIESEL = 0

while True:
    opcao = int(input())

    match opcao:
        case 1:
            ALCOOL += 1
        case 2:
            GASOLINA += 1
        case 3:
            DIESEL += 1
        case 4:
            break
        case _:
            continue

print("MUITO OBRIGADO")
print(f"Alcool: {ALCOOL}")
print(f"Gasolina: {GASOLINA}")
print(f"Diesel: {DIESEL}")
