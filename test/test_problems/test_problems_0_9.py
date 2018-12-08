import math

from src.primes import Primes
from textwrap import dedent
from unittest import TestCase


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


class TestProblem6(TestCase):

    def test_problem_6(self):
        def func(n: int) -> int:
            return sum([x for x in range(1, n + 1)])**2 - sum([x ** 2 for x in range(1, n + 1)])

        self.assertEqual(func(10), 2640)
        print(func(100))


class TestProblem7(TestCase):

    def test_problem_7(self):
        def func(n: int) -> int:
            primes = Primes()
            result = 0
            i = 0
            for p in primes:
                i += 1
                if i == n:
                    return p

        self.assertEqual(func(6), 13)
        print(func(10001))


class TestProblem8(TestCase):
    digit_str = dedent("""
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450""")

    def test_problem_8(self):
        def func(n: int) -> int:
            digits = [int(x) for x in self.digit_str if x != "\n"]
            result = 0
            for i in range(0, len(digits) - n):
                product = 1
                for j in range(i, i+n):
                    product *= digits[j]
                result = max(product, result)
            return result

        self.assertEqual(func(4), 5832)
        print(func(13))


class TestProblem9(TestCase):

    def test_problem_9(self):
        for i in range(1, 1000):
            for j in range(1, 1000):
                if i + j > 1000:
                    break
                k = 1000 - i - j
                if i ** 2 + j ** 2 == k ** 2:
                    print(i * j * k)
                    return




