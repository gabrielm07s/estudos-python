# Leia uma nota e mostre o conceito: A (9 a 10), B (7 a 8.9), C (5 a 6.9) e D (abaixo de 5)
# Rejeitar notas fora de 0 a 10
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida")
elif nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D")
