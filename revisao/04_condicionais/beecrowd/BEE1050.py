"""
beecrowd 1050 - DDD
https://www.beecrowd.com.br/judge/pt/problems/view/1050
"""

DDD_REGISTRADOS = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte",
}

DDD = int(input())

if DDD in DDD_REGISTRADOS:
    print(DDD_REGISTRADOS[DDD])
else:
    print("DDD nao cadastrado")
