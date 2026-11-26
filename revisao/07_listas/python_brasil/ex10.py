"""
Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetor_a = []
vetor_b = []

print("VETOR A: ")
for i in range(10):
    vetor_a.append(int(input(f"Digite o {i + 1}º valor: ")))

print("\nVETOR B: ")
for i in range(10):
    vetor_b.append(int(input(f"Digite o {i + 1}º valor: ")))

vetor_c = [] + vetor_a + vetor_b

print("\nVETORES:")
print(f"Vetor A: {vetor_a}")
print(f"Vetor B: {vetor_b}")
print(f"Vetor C: {vetor_c}")
