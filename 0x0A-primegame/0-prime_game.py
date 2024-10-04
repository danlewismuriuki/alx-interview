#!/usr/bin/python3

"""
Determines the winner of a game based on the number of
primes between
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on the number of primes between
    1 and each number in the `nums` list, using the Sieve of Eratosthenes.
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    if max_n < 2:
        return None

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None