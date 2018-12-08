import math
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

