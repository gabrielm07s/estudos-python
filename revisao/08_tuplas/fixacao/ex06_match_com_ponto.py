ponto = (0, 0)

match ponto:
    case (0, 0):
        print("Origem")
    case (0, y):
        print("Eixo Y")
    case (x, 0):
        print("Eixo X")
    case (x, y):
        print("Quadrante")
