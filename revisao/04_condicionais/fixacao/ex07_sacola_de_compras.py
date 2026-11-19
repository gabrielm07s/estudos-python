import os
import time


def limpar_tela(segundos=3):
    time.sleep(segundos)
    os.system("cls")


def cabecalho():
    print("=================================")
    print("||        COMPRAS DO MÊS       ||")
    print("=================================")
    print("|| [1] Adicionar Produto       ||")
    print("|| [2] Listar Sacola           ||")
    print("|| [3] Buscar Produto          ||")
    print("|| [4] Remover Produto         ||")
    print("|| [5] Finalizar Compra        ||")
    print("|| [0] Sair                    ||")
    print("=================================")


def adicionar_produto(
    nome_produto: str,
    qtd_produto: int,
    preco_produto: float,
):

    sacola.append({nome_produto: (qtd_produto, preco_produto)})
    print("\nProduto adicionado com sucesso")
    limpar_tela()


def listar_sacola():
    print("\nSacola:")

    if not sacola:
        print("A sacola está vazia")
        limpar_tela()
        return

    for item in sacola:
        for nome, valor in item.items():
            qtd, preco = valor
            print(f"  • {nome.title()} ({qtd}) -- R$ {preco:.2f}")

    input("\nAperte enter para fechar a sacola....")
    limpar_tela()


def buscar_produto(nome_produto: str):
    for item in sacola:
        for nome in item:
            if nome.lower() == nome_produto:
                return item
    return None


def remover_produto(nome_produto: str):
    produto_encontrado = buscar_produto(nome_produto)

    if produto_encontrado is None:
        print("Produto não encontrado.")
        limpar_tela()
        return

    sacola.remove(produto_encontrado)

    print("Produto removido.")
    limpar_tela()


def finalizar_compra():
    preco_total = 0
    for item in sacola:
        for valor in item.values():
            preco_total += valor[0] * valor[1]

    return preco_total


sacola = []
while True:
    cabecalho()
    opcao = input("Escolha uma opção: ").strip().lower()

    match opcao:
        case "1" | "um":
            nome_produto = input("\nNome produto: ")
            qtd_produto = int(input("Quantidade do produto: "))
            preco_produto = float(input("Preço do produto: "))

            adicionar_produto(nome_produto, qtd_produto, preco_produto)
        case "2" | "dois":
            listar_sacola()
        case "3" | "três" | "tres":
            nome_produto = input("\nNome do produto: ").strip().lower()
            produto_encontrado = buscar_produto(nome_produto)

            if produto_encontrado is None:
                print(f"O produto {nome_produto} não foi encontrado.")
            else:
                for nome, (qtd, preco) in produto_encontrado.items():
                    print(
                        f"Produto encontrado: {nome.title()} ({qtd}) -- R$ {preco:.2f}"
                    )
            limpar_tela()
        case "4" | "quatro":
            nome_produto = input("\nNome do produto: ").strip().lower()
            remover_produto(nome_produto)
        case "5" | "cinco":
            preco_total = finalizar_compra()
            print(f"\nPreço total: R$ {preco_total:.2f}")
            break
        case "0" | "zero":
            break
        case _:
            print("Opção inválida, tente novamente!")
            limpar_tela()
