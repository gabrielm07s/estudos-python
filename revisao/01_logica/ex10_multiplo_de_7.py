# Ler números até digitar 0 e dizer se algum erá multiplo de 7
num = None
multiplo_de7 = False

while num != 0:
    num = int(input('Digite um número: '))

    if num % 7 == 0 and num != 0:
        multiplo_de7 = True

if multiplo_de7:
    print('Existe múltiplo de 7')
else:
    print('Não existe múltiplo de 7')