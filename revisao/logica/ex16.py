# Ler N valores e mostrar quantos estão no intervalo [10, 20]
valores_intervalo = 0
n = int(input('Quantos valores deseja ler? '))

i = 0
while i < n:
    num = int(input(f'Digite o {i + 1}º valor: '))

    if num >= 10 and num <= 20:
        valores_intervalo += 1

    i += 1

print(f'Existem {valores_intervalo} números dentro do intervalor [10, 20]')