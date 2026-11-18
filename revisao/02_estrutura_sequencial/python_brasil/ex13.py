"""
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes,
usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
"""

arquivo_gb = float(input("Tamanho do arquivo em GB: "))

arquivo_mb = arquivo_gb * 1024
arquivo_kb = arquivo_gb * (1024**2)

print(f"Tamanho arquivo em MB = {arquivo_mb}")
print(f"Tamanho do arquivo em KB = {arquivo_kb}")
