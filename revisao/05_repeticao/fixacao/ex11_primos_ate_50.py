# Números Primos até 50

for numero in range(2, 51):
    for divisores in range(2, numero):
        if numero % divisores == 0:
            break
    else:
        print(numero, end=" ")
print()
