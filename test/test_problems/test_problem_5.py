from unittest import TestCase
from src.primes import Primes


class TestProblem5(TestCase):

    def test_problem_5(self):
        def func(n: int) -> int:
            primes = Primes()
            i = 1

            primes.is_prime(n)
            m = 1
            for p in primes:
                if p <= n:
                    m *= p
                else:
                    break

            match = False
            while not match:
                match = True
                num = m * i
                for j in range(n, 2, -1):
                    if num % j != 0:
                        match = False
                        i += 1
                        break
            return i * m

        self.assertEqual(func(10), 2520)
        print(func(20))

