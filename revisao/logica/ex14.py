# Ler três lados de um triângulo e dizer se formam um triângulo e de que tipo
# l1 = float(input('Digite o primeiro lado do triângulo: '))
# l2 = float(input('Digite o segundo lado do triângulo: '))
# l3 = float(input('Digite o terceiro lado do triângulo: '))
lados = input('Digite os três lados do triângulo: ').split()
l1, l2, l3 = [int(x) for x in lados]

existe_triangulo = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l2 + l1)

if existe_triangulo:
    if l1 == l2 == l3:
        print('Triângulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo Isóceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não existe triangulo')