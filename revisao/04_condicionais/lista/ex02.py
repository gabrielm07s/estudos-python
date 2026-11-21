# Ler um número e dizer se é par, ímpar, positivo ou negativo
n = int(input("Digite um número: "))

par_ou_impar = "Par" if n % 2 == 0 else "Ímpar"
positivo_ou_negativo = "Positivo" if n >= 0 else "Negativo"

print(par_ou_impar + " e " + positivo_ou_negativo)

# if n % 2 == 0:
#     print('Par')
# else:
#     print('Ímpar')
#
# if n >= 0:
#     print('Positivo')
# else:
#     print('Negativo')
