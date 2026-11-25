"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
escreva o valor a ser pago pelo cliente.
"""

quantidade_morangos = float(input("Morangos (Kg): "))
quantidade_macas = float(input("Maças (Kg): "))

frutas = {
    "Morango": [2.50, 2.20],
    "Maca": [1.80, 1.50],
}

preco_morango = (
    frutas["Morango"][0 if quantidade_morangos <= 5 else 1] * quantidade_morangos
)
preco_maca = frutas["Maca"][0 if quantidade_macas <= 5 else 1] * quantidade_macas

preco_total = preco_maca + preco_morango

if quantidade_macas + quantidade_morangos > 8 or preco_total > 25.00:
    desconto = 0.10
    preco_total = preco_total * (1 - desconto)

print(f"Preço total: R$ {preco_total:.2f}")
