dados_turma = [
    {"nome": "Ana", "notas": [8, 9, 10]},
    {"nome": "Bruno", "notas": [6.5, 7.0, 8.5]},
    {"nome": "Carla", "notas": [9.5, 10, 9.0]},
    {"nome": "Daniel", "notas": [5.0, 6.0, 4.5]},
    {"nome": "Eduarda", "notas": [7.5, 8.0, 7.0]},
    {"nome": "Felipe", "notas": [10, 9.5, 10]},
    {"nome": "Gabriela", "notas": [6.0, 5.5, 7.0]},
    {"nome": "Henrique", "notas": [8.5, 8.0, 9.0]},
    {"nome": "Isabela", "notas": [4.0, 5.5, 6.0]},
    {"nome": "João", "notas": [7.0, 7.5, 8.0]},
]

media_alunos = [
    {
        "nome": aluno["nome"],
        "media": round(sum(aluno["notas"]) / len(aluno["notas"]), 2),
    }
    for aluno in dados_turma
]

media_turma = sum([media_aluno["media"] for media_aluno in media_alunos]) / len(
    media_alunos
)
print(f"{media_turma:.2f}")
