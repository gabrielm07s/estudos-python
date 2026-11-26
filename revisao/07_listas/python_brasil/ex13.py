"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

l_notas = []
while True:
    nota = float(input())

    if nota == -1:
        break

    l_notas.append(nota)

print(f"Total de valores lidos: {len(l_notas)}")
print(f"Valores na ordem informada: {l_notas}")
l_notas_inversa = l_notas[::-1]
print(f"Valores na ordem inversa do que foram informados: {l_notas_inversa}")
print(f"Soma dos valores: {sum(l_notas):.2f}")
print(f"Média dos valores: {sum(l_notas) / len(l_notas):.2f}")
print(
    f"Valores acima da média: {[x for x in l_notas if x > sum(l_notas) / len(l_notas)]}"
)
print(f"Valores abaixo de sete: {[x for x in l_notas if x < 7]}")
print("Encerrado")
