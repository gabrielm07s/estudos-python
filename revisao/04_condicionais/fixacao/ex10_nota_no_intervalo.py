nota = input("Digite uma nota: ")

try:
    nota = int(nota)
except ValueError:
    print("É permitido apenas valores númericos")
    raise

if 0 <= nota <= 10:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")
