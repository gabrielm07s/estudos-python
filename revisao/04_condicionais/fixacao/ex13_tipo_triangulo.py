l1, l2, l3 = map(float, input().split())
existe_triangulo = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)

if existe_triangulo:
    if l1 == l2 == l3:
        print("Triângulo Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não existe triângulo com estes valores de lados.")
