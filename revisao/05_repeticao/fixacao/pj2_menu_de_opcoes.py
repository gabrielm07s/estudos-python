# Menu de Opções
def cabecalho():
    print()
    print("[1] Ver Saldo  [2] Depositar  [3] Sacar  [0] Sair")


saldo = 0.0

while True:
    cabecalho()
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            print(f"Saldo: R$ {saldo:.2f}")
        case 2:
            saldo += float(input("Valor: "))
        case 3:
            valor = float(input("Valor: "))

            if valor <= saldo and valor > 0:
                saldo -= valor
            else:
                print("Saldo insuficiente")
        case 0:
            break
        case _:
            print("Opção Inválida")
