# Classificar um triângulo pelos ângulos e pelos lados
l1, l2, l3 = map(float, input().split())
a1, a2, a3 = map(float, input().split())
existe_triangulo = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l2 + l1)

triangulo_retangulo = 90 in (a1, a2, a3)
triangulo_acutangulo = all(a < 90 for a in (a1, a2, a3))
triangulo_obtusangulo = any(90 < a < 180 for a in (a1, a2, a3))

if existe_triangulo:
    if l1 == l2 == l3:
        print("Triângulo Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não existe triângulo")
