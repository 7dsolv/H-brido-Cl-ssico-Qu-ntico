# Híbrido Clássico–Quântico

[![Testes](https://github.com/7dsolv/H-brido-Cl-ssico-Qu-ntico/actions/workflows/tests.yml/badge.svg)](https://github.com/7dsolv/H-brido-Cl-ssico-Qu-ntico/actions/workflows/tests.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-6ee7b7)](LICENSE)

Demonstração educacional que compara uma tarefa clássica — a soma de uma progressão aritmética — com a representação mínima de um qubit por vetor de estado e sua medição probabilística.

> [!IMPORTANT]
> O projeto é um simulador clássico. Ele não executa em hardware quântico e não oferece vantagem quântica. Um bit aleatório com distribuição 50/50 reproduz as estatísticas de uma única medição de $|+\rangle$ na base computacional, mas não reproduz fase, interferência ou emaranhamento.

## Executar

Não há dependências externas.

```bash
python -m hybrid_demo --n 10 --shots 10000 --seed 7
```

Executar os testes:

```bash
python -m unittest discover -s tests -v
```

## Parte clássica: soma de uma série

A soma dos primeiros $n$ inteiros não negativos é:

```math
S_n=\sum_{k=1}^{n}k=\frac{n(n+1)}{2}
```

Para $n=10$:

```math
S_{10}=\frac{10(10+1)}{2}=55
```

O projeto calcula o resultado de duas formas — iteração e fórmula fechada — e verifica que ambas coincidem.

## Parte quântica: vetor de estado

Um qubit puro normalizado pode ser escrito como:

```math
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle
```

com a condição:

```math
|\alpha|^2+|\beta|^2=1
```

Na medição pela base computacional:

```math
P(0)=|\alpha|^2,\qquad P(1)=|\beta|^2
```

O estado $|+\rangle$, obtido ao aplicar a porta de Hadamard em $|0\rangle$, é:

```math
|+\rangle=H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt{2}}
```

Por isso, uma medição isolada produz `0` ou `1` com probabilidade igual. A diferença aparece quando preservamos e manipulamos amplitudes. Por exemplo:

```math
H|+\rangle=|0\rangle
```

Essa interferência não pode ser representada por uma moeda clássica que armazena somente probabilidades.

## Comparação

| Propriedade | Bit aleatório clássico | Qubit simulado |
|---|---:|---:|
| Resultado observado | `0` ou `1` | `0` ou `1` |
| Probabilidades | sim | sim |
| Amplitudes complexas | não | sim |
| Fase relativa | não | sim |
| Interferência por Hadamard | não | sim |
| Emaranhamento | não neste modelo | não neste modelo de um qubit |
| Hardware quântico | não | não |

## API

```python
from hybrid_demo import Qubit, arithmetic_series_sum

print(arithmetic_series_sum(10))

plus = Qubit.zero().hadamard()
print(plus.probabilities())
print(plus.hadamard())  # volta a |0>, salvo erro numérico
```

Principais componentes:

- `arithmetic_series_sum(n)`: fórmula fechada;
- `iterative_series_sum(n)`: soma iterativa usada para verificação;
- `Qubit`: estado normalizado de um qubit;
- `Qubit.hadamard()`: aplicação da porta $H$;
- `Qubit.measure()`: amostragem pela regra de Born;
- `sample_classical_bit()`: referência clássica 50/50.

## Limites do simulador

- representa apenas um qubit puro;
- não modela ruído, decoerência ou portas físicas;
- não possui emaranhamento nem circuitos multi-qubit;
- usa números de ponto flutuante e um gerador pseudoaleatório clássico;
- serve para ensino e testes, não para alegar desempenho quântico.

## Contribuir

Forks e pull requests são bem-vindos. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e inclua testes para qualquer nova porta, estado ou cálculo.

## Autor e licença

Criado por **Adilson Oliveira / [7dsolv](https://github.com/7dsolv)**.

Distribuído sob a [Licença MIT](LICENSE).
