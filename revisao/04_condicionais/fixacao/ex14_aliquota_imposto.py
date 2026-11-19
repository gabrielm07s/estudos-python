salario = float(input("Salário: R$ "))

if salario < 2000:
    aliquota = 0
elif salario <= 3000:
    aliquota = 8
elif salario <= 4500:
    aliquota = 18
else:
    aliquota = 28

imposto = salario * aliquota / 100
print(f"Aliquota: {aliquota}% | Imposto: R$ {imposto:.2f}")
