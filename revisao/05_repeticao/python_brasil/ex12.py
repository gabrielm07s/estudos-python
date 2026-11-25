"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1, 2, 3, 4  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.
"""

candidatura = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

while True:
    print("[1] Candidato A")
    print("[2] Candidato B")
    print("[3] Candidato C")
    print("[4] Candidato D")
    print("[5] Voto Nulo")
    print("[6] Voto em Branco")
    print("[0] Sair")

    opcao = int(input("Digite a opção: "))

    match opcao:
        case 0:
            break
        case 1 | 2 | 3 | 4 | 5 | 6:
            candidatura[opcao] += 1
        case _:
            print("Opção inválida, favor tentar novamente!")
            continue

total_votos = sum(candidatura.values())

print(f"CANDIDATO A: {candidatura[1]}")
print(f"CANDIDATO B: {candidatura[2]}")
print(f"CANDIDATO C: {candidatura[3]}")
print(f"CANDIDATO D: {candidatura[4]}")
print(f"Total de votos nulos: {candidatura[5]}")
print(f"Total de votos brancos: {candidatura[6]}")

if total_votos > 0:
    percentual_nulos = (candidatura[5] / total_votos) * 100
    percentual_brancos = (candidatura[6] / total_votos) * 100
    print(f"Percentagem de votos nulos: {percentual_nulos:.2f}%")
    print(f"Percentagem de votos em branco: {percentual_brancos:.2f}%")
else:
    print("Nenhum voto computado")
