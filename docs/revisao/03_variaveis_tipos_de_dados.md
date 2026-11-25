# 03 Variáveis e Tipos de Dados

**Status:** concluído em 19/11/2026 (fixação, 8 exercícios).
**Bloco:** A · **Anterior:** [02 Estrutura Sequencial](02_estrutura_sequencial.md) · **Próximo:** 04 Controle de Fluxo

## Objetivos
- Explicar variável como nome que aponta para um objeto.
- Usar `int`, `float`, `str`, `bool` e `None` e identificar tipos com `type()`.
- Converter entre tipos (`int()`, `float()`, `str()`) e prever o resultado de `bool()`.
- Manipular texto: métodos, índice, fatiamento e imutabilidade.
- Nomear constantes em MAIÚSCULAS e variáveis em `snake_case` (PEP 8).

## Onde estudei
- `Material_Python_Fundamentos.pdf` (no PDF, este módulo aparece como "Módulo 2 — Variáveis e Tipos de Dados").
- Geek University, seção de variáveis e tipos de dados.
- Luiz Otávio, aulas de tipos e strings.
- The Modern Python 3 Bootcamp (Colt Steele): variáveis, strings e booleanos.

## Conceitos
| Conceito | Resumo |
|---|---|
| `type()` | mostra a classe do valor: `int`, `float`, `str`, `bool`, `NoneType` |
| Conversão | `input()` devolve `str`; `float(x.replace(",", "."))` aceita vírgula decimal |
| `bin()`, `oct()`, `hex()` | mostram um inteiro em base 2, 8 e 16 (`0b`, `0o`, `0x`) |
| Métodos de `str` | `lower`, `title`, `replace`, `isdigit`, `count`, `split`, `strip`... (texto é imutável: o método devolve um novo) |
| Fatiamento | `s[::-1]` inverte a sequência |
| Constante | `TAXA_JUROS = 0.02`: MAIÚSCULAS por convenção (Python não impede de mudar) |
| Potência | `x ** n`; juros compostos: `capital * (1 + i) ** tempo` |

## Exercícios
| Arquivo | Assunto |
|---|---|
| [ex01](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex01_bases_numericas.py) | `bin`, `oct` e `hex` de um inteiro |
| [ex02](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex02_ler_float_virgula.py) | ler número com vírgula e converter para `float` |
| [ex03](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex03_nome_formatado.py) | nome com iniciais maiúsculas (`title`) |
| [ex04](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex04_contar_letra_a.py) | contar a letra "a" com `for` e contador |
| [ex05](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex05_frase_underline_invertida.py) | espaços por `_` e frase invertida (`replace` e `[::-1]`) |
| [ex06](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex06_validar_idade.py) | validar idade com `isdigit` |
| [ex07](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex07_juros_compostos.py) | juros compostos com constante |
| [ex08](../../revisao/03_variaveis_tipos_de_dados/fixacao/ex08_limpar_e_validar_cpf.py) | limpar pontuação do CPF e validar tamanho e dígitos |

## Armadilhas (da correção)
- `"²".isdigit()` é `True`, mas `int("²")` dá `ValueError`. Para validar entrada que vira número, `isdecimal()` é mais seguro. Vale para o `ex06` e o `ex08`.
- `ex06` não mostra nada quando a idade é válida: falta o `else`.
- `ex08` deixa um `print(cpf)` de depuração antes da validação.
- `"maria da silva".title()` dá `Maria Da Silva`: `title()` também capitaliza preposições.
- `ex07`: o valor inicial é o **capital**; **montante** é o resultado (`capital * (1 + i) ** t`).
- `float("abc")` interrompe o programa com `ValueError`: o tratamento vem no módulo 08 (Exceções).
- Contar letras: `frase.count("a")` faz o mesmo que o laço do `ex04`.

## Lista de revisão do PDF (R2)
| Item | Onde praticar | Situação |
|---|---|---|
| R2.7 CPF: limpar e validar tamanho e dígitos | próprio | ✅ `ex08` |
| R2.3 a R2.5 | Exercism (Bools, Numbers, Strings) | ⏸️ adiado por enquanto |
| R2.6, R2.10 e R2.11 | HackerRank, domínio Python | ⏸️ adiado por enquanto |
| R2.1 `type()` de 10 valores | próprio | ⬜ sem arquivo nesta pasta |
| R2.2 nome em maiúsculas, minúsculas, `title` e tamanho sem espaços | Python Brasil: Strings | ⬜ sem arquivo nesta pasta |
| R2.8 | Codewars (8 kyu) | ⬜ não feito |
| R2.9 "R$ 1.234,56" para `float` | próprio | ⬜ sem arquivo nesta pasta |

## Critério para avançar (PDF)
Converter entre tipos sem erro, prever `bool()` em qualquer valor e usar pelo menos 8 métodos de texto sem consulta. Módulo dado como concluído em 19/11/2026.
