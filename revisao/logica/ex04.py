# Verificar se um ano é bissexto
ano = int(input('Digite o ano: '))
ano_bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

if ano_bissexto:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} NÃO é Bissexto')