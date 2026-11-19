ano = int(input("Digite um ano: "))
ano_bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if ano_bissexto:
    print(f"O ano {ano} É um ano BISSEXTO")
else:
    print(f"O ano {ano} NÃO É um ano BISSEXTO")
