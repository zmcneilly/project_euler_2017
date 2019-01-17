import math

from src.factorization import prime_factors, multiples, num_divisors, divisors
from src.fibonacci import fibonacci_sequence
from src.primes import Primes
from textwrap import dedent
from unittest import TestCase


class TestProblem1(TestCase):

    def test_problem_1(self):

        def func(n: list, m: int) -> int:
            results = set()
            for _n in n:
                results.update(multiples(_n, m))
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
                for i in range(10 ** (n - 1), 10 ** n):
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


class TestProblem10(TestCase):

    def test_problem_10(self):
        primes = Primes()

        self.assertEqual(primes.sum_below(10), 17)
        print(primes.sum_below(2000000))


class TestProblem11(TestCase):

    def setUp(self):
        grid_str = """
                      08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
                      49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
                      81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
                      52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
                      22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
                      24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
                      32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
                      67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
                      24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
                      21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
                      78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
                      16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
                      86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
                      19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
                      04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
                      88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
                      04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
                      20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
                      20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
                      01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
        grid_list = [int(x) for x in dedent(grid_str).split()]
        max_index = math.sqrt(len(grid_list))
        max_index = int(max_index) if max_index.is_integer() else self.fail("Oopsie")
        self.grid = [[]]
        for i in range(0, max_index):
            row = []
            for j in range(0, max_index):
                row.append(grid_list.pop(0))
            self.grid.append(row)
        if len(grid_list) > 0:
            self.fail("Huh?")

    def get(self, point: tuple, default: int=1) -> int:
        try:
            result = self.grid[point[0]][point[1]]
        except IndexError:
            result = default
        finally:
            return result

    def test_problem_11(self):
        def product(factors: list) -> float:
            result = 1
            for x in factors:
                result = result * x
            return result


        max_product = 0

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                row = []
                col = []
                diag_right = []
                diag_left = []
                for _x in range(0, 4):
                    row.append(self.get((i, j+_x)))
                    col.append(self.get((i+_x, j)))
                    diag_right.append(self.get((i+_x, j+_x)))
                    diag_left.append(self.get((i-_x, j+_x)))
                max_product = max(max_product, product(row), product(col), product(diag_right), product(diag_left))

        self.assertEqual(max_product, 70600674)


class TestProblem12(TestCase):
    def test_divisors(self):
        self.assertEqual(num_divisors(28), 6)

    def test_divisor_funcs(self):
        for x in range(0, 200):
            if len(divisors(x)) != num_divisors(x):
                self.fail("len({}) != {}".format(divisors(x), num_divisors(x)))

    def triangle_number(self, n):
        return sum([x for x in range(0, n+1)])

    def test_problem_12(self):
        n = 1
        l_1 = num_divisors(n)
        l_2 = num_divisors(n + 1)
        try:
            max_divisors = l_1 * l_2
            _d = max_divisors
            while _d < 500:
                n += 1
                l_1 = l_2
                if n % 2 != 0:
                    l_2 = num_divisors((n + 1) / 2)
                else:
                    l_2 = num_divisors(n + 1)
                _d = l_1 * l_2
                if _d > max_divisors:
                    max_divisors = _d
                    print("{}: {}".format(_d, n))
        finally:
            self.assertEqual(n, 12375)







