# Tabela-verdade de p and not q
print(' p     | q     | p and q | not q')

for p in (True, False):
    for q in (True, False):
        print(f' {p!s:5} | {q!s:5} | {p and q!s:7} | {not q!s:5}')