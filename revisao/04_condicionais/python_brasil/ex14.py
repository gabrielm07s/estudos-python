"""
Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades

12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = int(input("Digite um número inteiro menor que 1000: "))
valor = num

centenas = valor // 100
valor %= 100
dezenas = valor // 10
valor %= 10
unidades = valor

if centenas:
    print(f"{num} = {centenas} centena(s), {dezenas} dezena(s) e {unidades} unidade(s)")
elif dezenas:
    print(f"{num} = {dezenas} dezena(s) e {unidades} unidade(s)")
else:
    print(f"{num} = {unidades} unidade(s)")
