TAXA_JUROS = 0.02
montante = 1000
tempo = 12

juros_compostos = montante * ((1 + TAXA_JUROS) ** tempo)
print(f"Juros compostos: {juros_compostos:.2f}")
