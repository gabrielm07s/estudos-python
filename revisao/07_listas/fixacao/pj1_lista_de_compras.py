import os
import time

lista_compras = []


def limpar_tela(segundos=2):
    time.sleep(segundos)
    os.system("cls")


def cabecalho():
    print("=" * 20)
    print(f"| {'LISTA DE COMPRAS':^16} |")
    print("=" * 20)
    print(f"| {'[1] Adicionar':<16} |")
    print(f"| {'[2] Remover':<16} |")
    print(f"| {'[3] Listar':<16} |")
    print(f"| {'[0] Sair':<16} |")
    print("=" * 20)


def adicionar(produto):
    if produto.lower() in lista_compras:
        print("Esse item já está na lista")
        return

    lista_compras.insert(0, produto)


def remover(produto):
    if produto.lower() in lista_compras:
        lista_compras.remove(produto.lower())
    else:
        print("Este produto não está na lista.")
        return


def listar():
    if not lista_compras:
        print("Lista de compras vazia")
    else:
        for indice, produto in enumerate(lista_compras):
            print(f"{indice + 1}. {produto.lower()}")


while True:
    cabecalho()
    opcao = int(input("Opção: "))

    match opcao:
        case 0:
            break
        case 1:
            produto = input("Item: ").strip().lower()
            adicionar(produto)
        case 2:
            produto = input("Remover qual item? ").strip().lower()
            remover(produto)
        case 3:
            listar()
        case _:
            print("Opção inválida. Tente novamente!")
    limpar_tela()
