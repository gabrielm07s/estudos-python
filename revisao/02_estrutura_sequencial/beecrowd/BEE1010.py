"""
beecrowd 1010 - Cálculo Simples
https://www.beecrowd.com.br/judge/pt/problems/view/1010
"""

CODE_1, QUANTITY_1, UNIT_VALUE_1 = map(float, input().split())
CODE_2, QUANTITY_2, UNIT_VALUE_2 = map(float, input().split())

TOTAL = (QUANTITY_1 * UNIT_VALUE_1) + (QUANTITY_2 * UNIT_VALUE_2)
print(f"VALOR A PAGAR: R$ {TOTAL:.2f}")
