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


