import math
from unittest import TestCase


class TestProblem4(TestCase):

    def test_problem_4(self):
        def gen_palindromes(n: int) -> int:
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


