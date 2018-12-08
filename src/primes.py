"""
Class for interacting with prime numbers
"""
import math
import pickle

from pathlib import Path
from bitarray import bitarray


class Primes(object):
    cache_location = Path("./prime_cache")

    def __init__(self):
        self.prime_array = bitarray([False, True, True, True, False])
        self.max_prime = 4
        self.load_cache()

    def __iter__(self):
        for x in range(2, self.max_prime + 1):
            if self.is_prime(x):
                yield x

    def load_cache(self) -> None:
        """
        Load cache from disk, if available.
        """
        if self.cache_location.exists():
            with self.cache_location.open("rb") as __f:
                self.prime_array = pickle.load(__f)
                self.max_prime = len(self.prime_array) - 1

    def save_cache(self) -> None:
        """
        Save prime array to disk.
        """
        with self.cache_location.open("wb") as __f:
            pickle.dump(self.prime_array, __f)

    def _generate_prime_array(self, n: int) -> None:
        """
        Populate prime_array with guaranteed correct values <= n.

        :param n: Largest number in array.
        """
        while self.max_prime <= n:
            max_factor = self.max_prime
            _p_n = min(max_factor ** 2, n)
            while self.max_prime <= _p_n:
                if self.max_prime % 2 == 0:
                    self.prime_array.append(True)
                else:
                    self.prime_array.append(False)
                self.max_prime += 1
            for i in self:
                if i == 2:
                    continue
                for j in range(max(math.floor(max_factor / i), 3), math.ceil(_p_n / i) + 1):
                    factor = i * j
                    if factor > self.max_prime:
                        break
                    self.prime_array[factor] = False
        self.save_cache()

    def is_prime(self, n: int) -> bool:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        if n > self.max_prime:
            self._generate_prime_array(n)
        return self.prime_array[n]

