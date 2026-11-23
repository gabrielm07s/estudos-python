"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada	Exemplos de Saída
vertebrado
mamifero
onivoro
homem

vertebrado
ave
carnivoro
aguia

invertebrado
anelideo
onivoro
minhoca
"""

P1 = input().lower()
P2 = input().lower()
P3 = input().lower()

if P1 == "vertebrado":
    if P2 == "ave":
        if P3 == "carnivoro":
            print("aguia")
        elif P3 == "onivoro":
            print("pomba")
    elif P2 == "mamifero":
        if P3 == "onivoro":
            print("homem")
        elif P3 == "herbivoro":
            print("vaca")

if P1 == "invertebrado":
    if P2 == "inseto":
        if P3 == "hematofago":
            print("pulga")
        elif P3 == "herbivoro":
            print("lagarta")
    elif P2 == "anelideo":
        if P3 == "hematofago":
            print("sanguessuga")
        elif P3 == "onivoro":
            print("minhoca")
