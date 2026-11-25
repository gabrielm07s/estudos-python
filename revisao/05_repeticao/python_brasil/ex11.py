"""
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

produtos = {
    100: 1.20,
    101: 1.30,
    102: 1.50,
    103: 1.20,
    104: 1.30,
    105: 1.00,
}

total = 0
while True:
    codigo, quantidade = map(int, input("Código | Quantidade: ").split())
    preco_produto = produtos[codigo] * quantidade
    print(f"Preço produto: R$ {preco_produto:.2f}")

    total += preco_produto

    encerrar = False
    while True:
        opcao = input("Deseja algo mais? (S/N) ").upper()
        if opcao == "N":
            encerrar = True
            break
        elif opcao == "S":
            break
        else:
            print("Opção inválida, tente novamente!")
            continue

    if encerrar:
        break

print(f"\nTotal: R$ {total:.2f}")
