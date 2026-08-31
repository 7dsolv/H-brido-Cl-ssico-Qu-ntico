"""Núcleo matemático pequeno e sem dependências externas."""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose, sqrt
from random import Random


def _validate_n(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n deve ser um número inteiro")
    if n < 0:
        raise ValueError("n deve ser não negativo")


def arithmetic_series_sum(n: int) -> int:
    """Retorna 1 + 2 + ... + n pela fórmula fechada."""
    _validate_n(n)
    return n * (n + 1) // 2


def iterative_series_sum(n: int) -> int:
    """Retorna 1 + 2 + ... + n por acumulação."""
    _validate_n(n)
    return sum(range(1, n + 1))


@dataclass(frozen=True, slots=True)
class Qubit:
    """Vetor de estado normalizado de um qubit puro."""

    alpha: complex
    beta: complex

    def __post_init__(self) -> None:
        norm_squared = abs(self.alpha) ** 2 + abs(self.beta) ** 2
        if not isclose(norm_squared, 1.0, rel_tol=1e-12, abs_tol=1e-12):
            raise ValueError("as amplitudes devem satisfazer |alpha|² + |beta|² = 1")

    @classmethod
    def zero(cls) -> "Qubit":
        return cls(1.0 + 0.0j, 0.0 + 0.0j)

    @classmethod
    def one(cls) -> "Qubit":
        return cls(0.0 + 0.0j, 1.0 + 0.0j)

    @classmethod
    def plus(cls) -> "Qubit":
        amplitude = 1.0 / sqrt(2.0)
        return cls(amplitude, amplitude)

    def probabilities(self) -> tuple[float, float]:
        return abs(self.alpha) ** 2, abs(self.beta) ** 2

    def hadamard(self) -> "Qubit":
        """Aplica H = 1/sqrt(2) [[1, 1], [1, -1]]."""
        scale = 1.0 / sqrt(2.0)
        return Qubit(
            scale * (self.alpha + self.beta),
            scale * (self.alpha - self.beta),
        )

    def measure(self, rng: Random | None = None) -> int:
        """Amostra uma medição na base computacional pela regra de Born."""
        generator = rng if rng is not None else Random()
        probability_zero, _ = self.probabilities()
        return 0 if generator.random() < probability_zero else 1


def sample_classical_bit(rng: Random | None = None) -> int:
    """Amostra um bit clássico com P(0) = P(1) = 1/2."""
    generator = rng if rng is not None else Random()
    return generator.randrange(2)
