"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

arquivo_mb = int(input("Tamanho arquivo (MB): "))
velocidade_mbps = int(input("Velocidade (Mbps): "))

tempo_aproximado = ((arquivo_mb * 8) / velocidade_mbps) / 60
print(f"O tempo aproximado de download é: {tempo_aproximado}")
