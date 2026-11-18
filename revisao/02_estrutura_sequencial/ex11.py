# Conversão de temperatura
temperatura_c = float(input('Temperatura em ºC: '))
temperatura_f = (temperatura_c * 1.8) + 32
temperatura_k = temperatura_c + 273.15

print(f'{temperatura_c:.1f} ºC = {temperatura_f:.1f} ºF = {temperatura_k:.2f} K')