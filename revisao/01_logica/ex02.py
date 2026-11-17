# Descobrir se a pessoa pode votar
idade = int(input('Digite a idade: '))
print(f'Idade: {idade}')

pode_votar = idade >= 16
if pode_votar:
    print('Pode votar')
else:
    print('Não pode votar')