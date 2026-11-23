"""
beecrowd 1049 - Animal
https://www.beecrowd.com.br/judge/pt/problems/view/1049
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
