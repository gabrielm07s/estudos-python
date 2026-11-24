"""
beecrowd 1114 - Senha Fixa
https://www.beecrowd.com.br/judge/pt/problems/view/1114
"""

SENHA_CORRETA = 2002

while True:
    SENHA = int(input())

    if SENHA == SENHA_CORRETA:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
