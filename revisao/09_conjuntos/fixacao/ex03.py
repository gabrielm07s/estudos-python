A = {
    "Lucas Almeida",
    "Mariana Costa",
    "Gabriel Souza",
    "Ana Beatriz Lima",
    "Pedro Henrique Rocha",
    "Juliana Mendes",
    "Rafael Oliveira",
    "Camila Ferreira",
    "Thiago Santos",
    "Larissa Carvalho",
}

B = {
    "Lucas Almeida",
    "Sofia Ribeiro",
    "Mateus Pereira",
    "Mariana Costa",
    "Guilherme Alves",
    "Valentina Gomes",
    "Gabriel Souza",
    "Laura Correia",
    "Pedro Henrique Rocha",
    "Helena Cardoso",
}

print(f"Nas duas turmas: {A.intersection(B)}")
print(f"Todos os alunos: {A.union(B)}")
print(f"Alunos apenas de A: {A - B}")
print(f"Alunos apenas de B: {B - A}")
