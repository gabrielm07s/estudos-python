"""
beecrowd 1038 - Lanche
https://www.beecrowd.com.br/judge/pt/problems/view/1038
"""

CODIGO, QUANTIDADE = map(int, input().split())


def calcular_preco(VALOR_UNITARIO: float):
    return VALOR_UNITARIO * QUANTIDADE


RES = None
match CODIGO:
    case 1:
        RES = calcular_preco(4.00)
    case 2:
        RES = calcular_preco(4.50)
    case 3:
        RES = calcular_preco(5.00)
    case 4:
        RES = calcular_preco(2.00)
    case 5:
        RES = calcular_preco(1.50)
    case _:
        print("Código inválido")

if RES is not None:
    print(f"Total: R$ {RES:.2f}")
