"""Interface de linha de comando da demonstração."""

from __future__ import annotations

import argparse
from random import Random

from .core import Qubit, arithmetic_series_sum, iterative_series_sum, sample_classical_bit


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=10, help="Limite da soma clássica.")
    parser.add_argument("--shots", type=int, default=10_000, help="Quantidade de medições.")
    parser.add_argument("--seed", type=int, default=7, help="Semente pseudoaleatória.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.shots <= 0:
        raise SystemExit("--shots deve ser positivo")

    closed = arithmetic_series_sum(args.n)
    iterative = iterative_series_sum(args.n)
    if closed != iterative:
        raise RuntimeError("a fórmula e a soma iterativa divergiram")

    quantum_rng = Random(args.seed)
    classical_rng = Random(args.seed)
    plus = Qubit.plus()
    quantum_ones = sum(plus.measure(quantum_rng) for _ in range(args.shots))
    classical_ones = sum(sample_classical_bit(classical_rng) for _ in range(args.shots))

    print(f"Soma de 1 a {args.n}: {closed}")
    print(f"Qubit |+>: P(1) experimental = {quantum_ones / args.shots:.4f}")
    print(f"Bit clássico: P(1) experimental = {classical_ones / args.shots:.4f}")
    print("H(H(|0>)) retorna |0>:", Qubit.zero().hadamard().hadamard())


if __name__ == "__main__":
    main()
