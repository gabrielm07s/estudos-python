# 02 Estrutura Sequencial (com o ambiente)

**Status:** exercícios concluídos em 18/11/2026. Faltam o aprofundamento teórico e a seção do bootcamp.
**Bloco:** A · **Anterior:** [01 Lógica](01_logica.md)

## Objetivos
- Preparar o ambiente: venv, VS Code, Ruff, REPL, `help()` e `dir()`.
- Ler dados com `input()` e converter com `int()` e `float()`.
- Calcular com operadores, precedência, `//`, `%`, `**` e `divmod`.
- Usar `math` (`pi`, `sqrt`, `ceil`, `floor`).
- Formatar saídas com f-strings e com `sep`/`end` do `print`.

## Onde estudei
- `Material_Python_Fundamentos.pdf`, módulo 02.
- Geek University, `cursos/geek_university/01_introducao_ao_python`.
- Luiz Otávio, `cursos/luiz_otavio/secao01`.
- The Modern Python 3 Bootcamp (Colt Steele): números, operadores, variáveis e strings (pendente).

## Conceitos
| Conceito | Resumo |
|---|---|
| `input()` | sempre devolve `str`; converter antes de calcular |
| `//`, `%`, `divmod` | quociente inteiro e resto; cédulas, dígitos e tempo |
| `math.ceil` | arredonda para cima ("quantas latas comprar") |
| f-string | `f"{v:.2f}"`, `f"{v:,.2f}"` e troca de `,`/`.` para `R$ 1.234,56` |
| `print(sep=, end=)` | separador entre itens e fim da linha |

## Exercícios
| Pasta | Quantidade | Conteúdo |
|---|---|---|
| [fixacao](../../revisao/02_estrutura_sequencial/fixacao/) | 17 | fixação do PDF: desconto, formatação, área, IMC, h:m:s, troco, juros, viagem |
| [lista](../../revisao/02_estrutura_sequencial/lista/) | 12 | soma, salário, média ponderada, distância, cédulas e moedas, BRL, `divmod` |
| [beecrowd](../../revisao/02_estrutura_sequencial/beecrowd/) | 21 | 1000 a 1021, sem o 1013 (pede decisão) |
| [python_brasil](../../revisao/02_estrutura_sequencial/python_brasil/) | 18 | Lista Python Brasil, Estrutura Sequencial completa |

## Armadilhas (erros que corrigi)
- **Python Brasil ex09:** mensagem do `input` dizia °C; o exercício pede °F.
- **ex12 e ex13:** altura e peso são `float`.
- **ex15:** IR, INSS e sindicato formatados com `:.2f`.
- **ex17:** latas de 18 L mais galões de 3,6 L com `ceil(resto / 3.6)`; se forem 5 galões, troca por mais uma lata.
- **ex18:** a conta dá segundos; mostrar em minutos (dividir por 60).
- `0.1 + 0.2 != 0.3`: não comparar `float` com `==`.
- beecrowd exige saída exata, inclusive espaços.

## Critério para avançar
Resolver sem consulta o 1021 (Notas e Moedas) e o ex17 do Python Brasil, e explicar `//`, `%`, `divmod`, `ceil` e a formatação em BRL.
