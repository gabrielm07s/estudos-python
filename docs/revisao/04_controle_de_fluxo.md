# 04 Controle de Fluxo

**Status:** exercícios concluídos em 25/11/2026 (condicionais, repetição e 2 mini-projetos). Faltam a lista F/M/D/X sem consulta e o fechamento do Bloco A.
**Bloco:** A · **Anterior:** [03 Variáveis e Tipos de Dados](03_variaveis_tipos_de_dados.md) · **Próximo:** 05 Coleções

## Objetivos
- Decidir com `if`/`elif`/`else` e `match`, combinando condições com `and`, `or` e `not`.
- Repetir com `while` e `for` (`range`, `enumerate`, `zip`), e controlar o laço com `break`, `continue` e `for`/`else`.
- Validar entrada com `while True` e voltar ao menu sem perder o estado.
- Escolher a estrutura certa para cada problema e explicar a escolha.

## Onde estudei
- Python 3 (Luiz Otávio), condicionais e laços.
- Geek University, estruturas de decisão e de repetição.
- Listas externas: beecrowd (Iniciante) e Python Brasil (decisão e repetição).

## Conceitos
| Conceito | Resumo |
|---|---|
| `if`/`elif`/`else` | a ordem das faixas importa: a primeira condição verdadeira vence |
| `match` | compara o **tipo** também: `input()` devolve `str`, então `case 1` não bate com `"1"` |
| `while` | repete enquanto a condição for verdadeira; quem atualiza o contador é você |
| `for` e `range` | `range(inicio, fim, passo)` não inclui o `fim` |
| `break` e `continue` | `break` sai do laço; `continue` volta ao início da próxima volta |
| `for`/`else` | o `else` roda quando o laço terminou sem `break` (ex.: teste de primo) |
| `enumerate` e `zip` | posição junto do item; percorrer duas sequências em paralelo |
| Expressão geradora | `sum(x[1] for x in d.values())` soma sem criar lista (prévia do 06) |
| `max(..., key=)` | escolhe o maior por um critério (`key=lambda x: x[1]`) |

## Exercícios
| Pasta | Conteúdo | Arquivos |
|---|---|---|
| [04_condicionais/fixacao](../../revisao/04_condicionais/fixacao/) | decisão básica | 15 |
| [04_condicionais/lista](../../revisao/04_condicionais/lista/) | lista de revisão | 9 |
| [04_condicionais/beecrowd](../../revisao/04_condicionais/beecrowd/) | problemas 1013 a 1061 | 19 |
| [04_condicionais/python_brasil](../../revisao/04_condicionais/python_brasil/) | lista de decisão (1 a 14 e 19, 23 a 28) | 20 |
| [05_repeticao/fixacao](../../revisao/05_repeticao/fixacao/) | laços, `range`, `enumerate`, `zip` e 3 programas (`pj1` a `pj3`) | 20 |
| [05_repeticao/beecrowd](../../revisao/05_repeticao/beecrowd/) | problemas 1059 a 1165 | 50 |
| [05_repeticao/python_brasil](../../revisao/05_repeticao/python_brasil/) | lista de repetição, 12 dos 14 escolhidos (sem o 42 e o 45) | 12 |

## Mini-projetos do Bloco A
| Projeto | O que treina |
|---|---|
| [pj1_caixa_eletronico](../../revisao/06_projetos_bloco_A/pj1_caixa_eletronico.py) | menu com `match`, funções, saque com cédulas (`divmod`), validar antes de mexer no saldo |
| [pj2_controle_gastos](../../revisao/06_projetos_bloco_A/pj2_controle_gastos.py) | dicionário de categorias, `sum` com expressão geradora, `max` com `key`, barra de `#` |

## Armadilhas (da correção)
- `150 < idade < 0` nunca é verdadeiro. Para "fora do intervalo": `idade < 0 or idade > 150`.
- `letra not in "scvd"` testa substring (`"sc"` passa). Use uma lista ou tupla de letras.
- Cadeia de `elif` com limites trocados: média 10 caiu em "Conceito E". O limite superior da faixa A é inclusivo.
- Caixa eletrônico: o saldo só desce **depois** de validar o saque (inteiro, maior que zero, dentro do saldo). Descontar antes perde dinheiro quando a validação falha.
- `break` ao recusar uma entrada encerra o programa; para voltar ao menu use `continue`.
- `max(lista_de_listas)` compara pelo primeiro item (o nome); para comparar pelo valor use `key=`.
- `"#" * (percentual // 5)` dá `TypeError` quando o resultado é `float`; converta com `int()`.
- Divisão por zero em percentual quando não há gastos: confira o total antes de dividir.
- `for` com limites de relógio: horas `range(24)` e minutos `range(60)`; `range(1, 61)` perde o `00` e cria o `60`.
- Contador de tentativas: some uma vez por palpite e não desfaça no caminho.
- `input()` e `float()` quebram com texto: o tratamento vem no módulo 08 (Exceções).

## Lista de revisão
| Nível | Item | Situação |
|---|---|---|
| F | `if`/`elif`/`else` e um laço com `break` e entrada validada, sem consulta | ⬜ lista F/M/D/X |
| F | diferença entre `while` e `for`, e quando usar `for`/`else` | ⬜ lista F/M/D/X |
| M | `bool()` de `0`, `""`, `[]`, `None` e `"0"` | ⬜ lista F/M/D/X |
| M | 8 métodos de `str` e `f-string` com formatação de número | ⬜ lista F/M/D/X |
| D | caixa eletrônico e jogo da adivinhação sem consulta | ✅ caixa eletrônico · ⬜ adivinhação (`pj1` da fixação) |

## Critério para avançar (plano)
Escrever, sem consulta, um programa com `if`/`elif`/`else`, laço com `break` e entrada validada. Explicar `while` × `for` e o `for`/`else`. Prever `bool()` de `0`, `""`, `[]`, `None` e `"0"`. Usar 8 métodos de `str` e `f-string` com número. Depois: lista integrada do Bloco A (10 exercícios F/M/D) e a lista F/M/D/X do 04.
