import os
import time


def limpar_tela(segundos=2):
    time.sleep(segundos)
    os.system("cls")


def cabecalho():
    print("=" * 22)
    print(f"| {'CONTROLE DE GASTOS':^18} |")
    print("=" * 22)
    print(f"| {'[1] Lançar Gasto':<18} |")
    print(f"| {'[0] Sair':<18} |")
    print("=" * 22)


categorias = {"A": ["alimentacao", 0], "T": ["transporte", 0], "L": ["lazer", 0]}


def exibir_categorias():
    print("\nCategorias: ")
    for chave, valor in categorias.items():
        print(f"[{chave}]{valor[0][1::]}")


def exibir_valores_categorias(total_gasto):
    for categoria, valor in categorias.values():
        percentual = (valor / total_gasto) * 100
        print(
            f"{categoria.title():<12} R$ {valor:^12.2f} {f'{percentual:.1f}%':^12} {'#' * int(percentual // 5):>12}"
        )


total_lancamentos = 0
while True:
    cabecalho()
    opcao = int(input("Opção: "))

    match opcao:
        case 0:
            break
        case 1:
            exibir_categorias()
            letra = input("Digite a categoria: ").upper()
            valor = float(input("Valor do gasto: R$ "))

            if valor <= 0 or letra not in categorias:
                print("Valor inválido")
                limpar_tela()
                continue

            categorias[letra][1] += valor
            total_lancamentos += 1
        case _:
            print("Opção inválida, gasto ignorado!")

    limpar_tela()

total_gastos = sum(x[1] for x in categorias.values())

if total_gastos > 0:
    maior_gasto = max(categorias.values(), key=lambda x: x[1])

    print(f"\n{total_lancamentos} lançamento(s) | total R$ {total_gastos:.2f}")
    exibir_valores_categorias(total_gastos)
    print(f"Maior gasto: R$ {maior_gasto[1]:.2f} ({maior_gasto[0].title()})")
else:
    print("Nenhum gasto lançado")
