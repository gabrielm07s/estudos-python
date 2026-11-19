idade = int(input("Digite a idade: "))
tem_carteira = input("Tem carteira? (S/N) ").lower() == "s"

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
elif idade < 18 and tem_carteira:
    print("É necessário ter 18 anos para ter carteira.")
else:
    print("Não pode dirigir")
