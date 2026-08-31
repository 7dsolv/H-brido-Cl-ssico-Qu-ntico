from random import Random
import unittest

from hybrid_demo import (
    Qubit,
    arithmetic_series_sum,
    iterative_series_sum,
    sample_classical_bit,
)


class ClassicalSeriesTests(unittest.TestCase):
    def test_ten_terms_equal_55(self):
        self.assertEqual(arithmetic_series_sum(10), 55)
        self.assertEqual(iterative_series_sum(10), 55)

    def test_formula_matches_iteration(self):
        for n in range(1_001):
            self.assertEqual(arithmetic_series_sum(n), iterative_series_sum(n))

    def test_invalid_n_is_rejected(self):
        with self.assertRaises(ValueError):
            arithmetic_series_sum(-1)
        with self.assertRaises(TypeError):
            arithmetic_series_sum(1.5)


class QubitTests(unittest.TestCase):
    def test_invalid_state_is_rejected(self):
        with self.assertRaises(ValueError):
            Qubit(1.0, 1.0)

    def test_plus_state_has_equal_probabilities(self):
        probability_zero, probability_one = Qubit.plus().probabilities()
        self.assertAlmostEqual(probability_zero, 0.5)
        self.assertAlmostEqual(probability_one, 0.5)

    def test_hadamard_is_its_own_inverse(self):
        result = Qubit.zero().hadamard().hadamard()
        self.assertAlmostEqual(result.alpha.real, 1.0)
        self.assertAlmostEqual(result.alpha.imag, 0.0)
        self.assertAlmostEqual(abs(result.beta), 0.0)

    def test_measurement_follows_born_probabilities(self):
        rng = Random(2026)
        shots = 20_000
        ones = sum(Qubit.plus().measure(rng) for _ in range(shots))
        self.assertLess(abs(ones / shots - 0.5), 0.02)

    def test_classical_reference_is_balanced(self):
        rng = Random(2026)
        shots = 20_000
        ones = sum(sample_classical_bit(rng) for _ in range(shots))
        self.assertLess(abs(ones / shots - 0.5), 0.02)


if __name__ == "__main__":
    unittest.main()
