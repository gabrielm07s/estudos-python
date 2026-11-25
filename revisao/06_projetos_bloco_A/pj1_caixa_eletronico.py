import os
import time


def limpar_tela(segundos=2):
    time.sleep(segundos)
    os.system("cls")


def cabecalho():
    print("=" * 38)
    print(f"| {'CAIXA ELETRÔNICO':^34} |")
    print("=" * 38)
    print(f"| {'[1] Saldo':<34} |")
    print(f"| {'[2] Depositar':<34} |")
    print(f"| {'[3] Sacar':<34} |")
    print(f"| {'[0] Sair':<34} |")
    print("=" * 38)


def depositar(valor):
    global saldo

    if valor <= 0:
        print("Valor inválido.")
        return

    saldo += valor
    print("Depósito feito", end=" ")
    exibir_saldo()


def sacar(valor):
    global saldo

    if valor <= 0 or valor > saldo:
        print("Valor inválido")
        return

    contagem_cedulas(valor)
    saldo -= valor
    exibir_saldo()


def contagem_cedulas(valor):
    CEDULAS = (200, 100, 50, 20, 10, 5, 2, 1)

    print("Retire as cédulas:")
    for cedula in CEDULAS:
        qtd, valor = divmod(valor, cedula)

        if qtd:
            print(f"{qtd} x R$ {cedula}")


def exibir_saldo():
    print(f"Saldo: R$ {saldo:.2f}")


saldo = 0.0

while True:
    cabecalho()
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            exibir_saldo()
        case 2:
            valor = float(input("Valor do depósito: R$ "))
            depositar(valor)
        case 3:
            valor = int(input("Valor do saque (inteiro): R$ "))
            sacar(valor)
        case 0:
            break
        case _:
            print("Valor inválido. Tente novamente!")
    limpar_tela()
