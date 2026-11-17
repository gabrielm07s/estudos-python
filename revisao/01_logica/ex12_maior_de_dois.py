# Lê dois números e msotra o maior (ou "iguais")
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print(f'São iguais')
else: 
    maior = max(n1, n2)
    print(f'O maior entre {n1} e {n2} é: {maior}')