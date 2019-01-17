import math

from .primes import Primes
primes = Primes()


def prime_factors(n: int) -> list:
    """
    Return the prime factors of n.
    """
    results = []
    max_factor = math.ceil(n/2)
    primes.is_prime(max_factor)

    for x in primes:
        if x > max_factor:
            break
        if n % x == 0:
            results.append(x)

    return results


def divisors(n: int) -> set:
    """
    Return the list of all divisors of a number.
    """
    results = set(prime_factors(n))
    prev_len = 0
    while len(results) > prev_len:
        prev_len = len(results)
        results_iter = list(results)
        for f_1 in results_iter:
            for f_2 in results_iter:
                p = f_1 * f_2
                if p > n:
                    break
                elif n % p == 0:
                    results.add(p)
    results.update({1, n})
    return results


def num_divisors(n: int) -> int:
    return len(divisors(n))


def num_divisors_demo(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


def multiples(n: int, m: int) -> list:
    """
    Return a list of natural numbers, less than m, and multiples of n.

    :return: A list of natural numbers.
    """
    for x in range(0, math.ceil(m/n)):
        yield n*x


