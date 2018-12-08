import math

from src.primes import Primes
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


def fibonacci_sequence(n: int) -> list:
    """
    Return a list of the fibonacci sequence, with all values <= n.

    :return: A list of ints.
    :rtype: list[int]
    """

    sequence = [1, 2]
    while sequence[-1] <= n:
        index = len(sequence)
        sequence.append(sequence[index - 1] + sequence[index - 2])
    while sequence[-1] > n:
        sequence.pop()
    return sequence


class TestProblem2(TestCase):

    def test_problem_2(self):
        self.assertEqual(fibonacci_sequence(89), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

        total = 0
        for x in fibonacci_sequence(4000000):
            if x % 2 == 0:
                total += x

        print(total)

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(89), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


def prime_factors(n: int) -> list:
    primes = Primes()
    results = [2] if n % 2 == 0 else []
    max_factor = math.ceil(math.sqrt(n))
    primes.is_prime(max_factor)

    for x in primes:
        if x > max_factor:
            break
        if n % x == 0:
            results.append(x)

    return results


class TestProblem3(TestCase):

    def test_prime_factors(self):
        self.assertEqual(prime_factors(13195), [5, 7, 13, 29])

    def test_problem_3(self):
        print(max(prime_factors(600851475143)))


class TestProblem4(TestCase):

    def test_problem_4(self):
        def gen_palindromes(n: int) -> list:
            """
            Generates palindromes of length `n`
            """
            if n % 2 != 0:
                n = n - 1
                spacer = True
            else:
                spacer = False
            for x in range(10 ** (int(n / 2) - 1), 10 ** int(n / 2)):
                x_str = str(x)
                if not spacer:
                    yield int("{}{}".format(x_str, x_str[::-1]))
                else:
                    for y in range(10 ** (n - 2), 10 ** (n - 1)):
                        yield int("{}{}{}".format(x_str, y, x_str[::-1]))

        def func(n: int) -> int:
            """
            Finds the largest palindrome that's the product of n-digit numbers.
            """
            m = 0
            for x in range(0, n):
                m *= 10
                m += 9
            max_product = m ** 2
            pal_len = math.ceil(math.log10(max_product))

            results = []
            for pal in gen_palindromes(pal_len):
                for i in range(10 ** (n - 1), 10 ** (n)):
                    j = pal / i
                    if j.is_integer() and len(str(int(j))) == n:
                        results.append(pal)
                        break
            return max(results)

        self.assertEqual(func(2), 9009)
        print(func(3))


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

