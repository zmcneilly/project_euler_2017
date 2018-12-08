import math

from .primes import Primes

def prime_factors(n: int) -> list:
    """
    Return the prime factors of n.
    """
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


def multiples(n: int, m: int) -> list:
    """
    Return a list of natural numbers, less than m, and multiples of n.

    :return: A list of natural numbers.
    """
    return [n*x for x in range(0, math.ceil(m/n))]


