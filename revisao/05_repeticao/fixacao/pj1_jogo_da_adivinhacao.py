import random

numero_secreto = random.randint(1, 20)
# print(numero_secreto)
tentativas = 0

while True:
    numero = int(input("Seu palpite: "))
    tentativas += 1

    if numero < numero_secreto:
        print(" maior")
    elif numero > numero_secreto:
        print(" menor")
    else:
        print(f"Acertou em {tentativas} tentativa(s)!")
        break
