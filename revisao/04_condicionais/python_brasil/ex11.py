"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00
"""

valor_hora = float(input("Valor hora: R$ "))
qtd_horas = int(input("Quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * qtd_horas
INSS = 10
FGTS = 11

if 0 < salario_bruto <= 900:
    IR = 0
elif salario_bruto <= 1500:
    IR = 5
elif salario_bruto <= 2500:
    IR = 10
else:
    IR = 20

valor_IR = salario_bruto * (IR / 100)
valor_FGTS = salario_bruto * (FGTS / 100)
valor_INSS = salario_bruto * (INSS / 100)

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"- IR: R$ {valor_IR:.2f}")
print(f"- INSS: R$ {valor_INSS:.2f}")
print(f"- FGTS: R$ {valor_FGTS:.2f}")
print(f"Total de descontos: R$ {sum((valor_FGTS, valor_IR, valor_INSS)):.2f}")
print(
    f"Salário Líquido: R$ {(salario_bruto - sum((valor_FGTS, valor_IR, valor_INSS))):.2f}"
)
