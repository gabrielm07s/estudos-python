cpf = input("Digite o CPF: ").replace("-", "").replace(".", "")

print(cpf)
if cpf.isdigit() and len(cpf) == 11:
    print("CPF pronto para validar")
else:
    print("CPF inválido")
