# Faça um menu com match / case (Saldo / Depósito / Saque)
import os
import time


def limpar_tela(segundos=2):
    time.sleep(segundos)
    os.system("cls")


def cabecalho():
    print("=" * 28)
    print(f"|| {'MENU DE AÇÕES':^22} ||")
    print("=" * 28)
    print(f"|| {'[1] Saldo':<22} ||")
    print(f"|| {'[2] Depósito':<22} ||")
    print(f"|| {'[3] Saque':<22} ||")
    print(f"|| {'[4] Sair':<22} ||")
    print("=" * 28)


def exibir_saldo():
    print(f"Saldo: R$ {saldo:.2f}")
    limpar_tela()


def deposito(valor: float):
    global saldo

    if valor > 0 and valor:
        saldo += valor

    return exibir_saldo()


def saque(valor: float):
    global saldo

    if valor > 0 and valor <= saldo:
        saldo -= valor

    return exibir_saldo()


saldo = 0
while True:
    cabecalho()
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            exibir_saldo()
        case 2:
            valor = float(input("Digite o valor de depósito: R$ "))
            deposito(valor)
        case 3:
            valor = float(input("Digite o valor de saque: R$ "))
            saque(valor)
        case 4:
            break
        case _:
            print("Opção inválida")
