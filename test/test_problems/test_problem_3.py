import math

from src.primes import Primes
from unittest import TestCase


def prime_factors(n: int) -> list:
    primes = Primes()
    results = [2] if n % 2 == 0 else []
    max_factor = math.ceil(math.sqrt(n))
    primes.is_prime(max_factor)

    for x in range(3, max_factor+1, 2):
        if x > max_factor:
            break
        if x == 1 or not primes.is_prime(x):
            continue
        if n % x == 0:
            results.append(x)

    return results

class TestProblem3(TestCase):

    def test_prime_factors(self):
        self.assertEqual(prime_factors(13195), [5, 7, 13, 29])

    def test_problem_3(self):
        print(max(prime_factors(600851475143)))
