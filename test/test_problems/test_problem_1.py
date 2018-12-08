import math
from unittest import TestCase


class TestProblem1(TestCase):

    def test_problem_1(self):

        def natural_numbers(n: int, m: int) -> list:
            """
            Return a list of natural numbers, less than m, and multiples of n.

            :return: A list of natural numbers.
            """
            return [n*x for x in range(0, math.ceil(m/n))]

        def func(n: list, m: int) -> int:
            results = set()
            for _n in n:
                results.update(natural_numbers(_n, m))
            return sum(results)

        self.assertEqual(func([3, 5], 10), 23)
        print(func([3, 5], 1000))
