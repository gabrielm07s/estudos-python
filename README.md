# Estudos de Python

Repositório de estudo de Python (fundamentos até o avançado): aulas dos cursos, listas de exercícios,
revisão por módulo e mini-projetos. Frameworks (Django etc.) ficam em repositórios separados.

## Estrutura

```
cursos/        aulas acompanhadas, na ordem de cada curso
  luiz_otavio/       curso do Luiz Otávio (secao01, secao02, ...): aulaNN.py e exNN.py
  geek_university/   curso da Geek University, uma pasta por assunto
exercicios/    listas de exercícios por tema, numeradas pelo módulo
revisao/       2ª passada por módulo, com o material em PDF e simulados
docs/          documentação por módulo (páginas de revisão em docs/revisao/)
projetos/      mini-projetos (v1 e v2)
```

Os números de `exercicios/` e `revisao/` seguem os módulos do material de revisão. Pastas só aparecem
quando existe conteúdo, então a sequência pode ter "buracos" (por exemplo, não há exercícios de Lógica em `exercicios/`).

| Módulo | Bloco | Exercícios | Revisão |
|---|---|---|---|
| 01 Lógica e Algoritmos | A | | [concluída (18/18)](docs/revisao/01_logica.md) |
| 02 Estrutura Sequencial (com o ambiente) | A | | [exercícios concluídos (68)](docs/revisao/02_estrutura_sequencial.md) |
| 03 Variáveis e Tipos de Dados | A | `03_fundamentos` (19) | [concluída (fixação 8)](docs/revisao/03_variaveis_tipos_de_dados.md) |
| 04 Controle de Fluxo | A | `04_controle_de_fluxo` (condicionais 18, repetição 21) | [exercícios concluídos](docs/revisao/04_controle_de_fluxo.md) |
| 05 Coleções | B | `05_colecoes` (listas 22, tuplas 25, dicionários 25, conjuntos 30) | pendente |
| 06 Comprehensions | B | a criar | pendente |
| 07 Funções | B | `07_funcoes` (19) | pendente |
| 08 Exceções | B | a criar | pendente |

## Convenções

- **Arquivos:** `aulaNN.py` e `exNN.py` nos cursos; em `exercicios/` e `revisao/`, `exNN_descricao.py`
  (minúsculas, sem acento, separado por `_`).
- **Commits em português**, no padrão `tipo(escopo): descrição`, por exemplo
  `feat(secao02/aula10): funções: def` ou `feat(exercicios): exercícios sobre funções`.
  Tipos usados: `feat`, `fix`, `refactor`, `chore`, `docs`.
- **Documentação:** cada módulo de `revisao/` tem uma página em `docs/revisao/` com objetivos, exercícios, armadilhas e
  critério para avançar (espelho das notas no Obsidian). Índice em [`docs/README.md`](docs/README.md).
- **Ruff** formata ao salvar (limite de 79 colunas, veja `.vscode/settings.json`).

## Como rodar

```powershell
python -m venv .venv          # ou: uv venv
.venv\Scripts\activate
python exercicios\07_funcoes\ex01_saudar.py
```

O VS Code recomenda as extensões do `.vscode/extensions.json` (Python, Ruff e o corretor ortográfico com
dicionário em português).

## Próximos passos

Módulos intermediários e avançados de Python (POO, módulos e pacotes, arquivos, testes, tipagem,
concorrência) continuam neste repositório, em novas pastas numeradas depois do módulo 08.
