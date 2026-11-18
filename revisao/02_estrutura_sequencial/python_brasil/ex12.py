"""
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes,
usando a seguinte fórmula:

Gigabytes * 1024
"""

arquivo_gb = float(input("GB: "))

arquivo_mb = arquivo_gb * 1024
print(f"Arquivo em MB: {arquivo_mb}")
