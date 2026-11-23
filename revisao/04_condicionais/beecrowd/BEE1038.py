"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir,
calcule e mostre o valor da conta a pagar.

1 - Cachorro Quente - 4.00
2 - X-Salada - 4.50
3 - X-Bacon - 5.00
4 - Torrada simples - 2.00
5 - Refrigerante - 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
3 2
Total: R$ 10.00

4 3
Total: R$ 6.00

2 3
Total: R$ 13.50
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
