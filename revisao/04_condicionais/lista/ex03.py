# Ler o código e quantidade de um lanche e mostrar o total a pagar
print("=" * 38)
print(f"|| {'QUADRO DE LANCHE':^32} ||")
print("=" * 38)
print(f"|| {'Código':<21} | {'Preço':>8} ||")
print("-" * 38)
print(f"|| {'[1] Sanduíche':<21} | R$ {5.50:>5} ||")
print(f"|| {'[2] Bolo de Chocolate':<21} | R$ {8.50:>5} ||")
print(f"|| {'[3] Batatinha ':<21} | R$ {1.50:>5} ||")
print(f"|| {'[4] Suco':<21} | R$ {2.50:>5} ||")
print("=" * 38)
opcao = int(input("Escolha uma opção: "))
quantidade = int(input("Digite a quantidade: "))

res = None
match opcao:
    case 1:
        res = quantidade * 5.50
    case 2:
        res = quantidade * 8.50
    case 3:
        res = quantidade * 1.50
    case 4:
        res = quantidade * 2.50
    case _:
        print("Opção inválida")

if res is not None:
    print(f"Preço total a pagar: R$ {res:.2f}")
