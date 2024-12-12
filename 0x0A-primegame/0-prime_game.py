#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of prime game based on rules provided.

    :param x: Number of rounds (int)
    :param nums: List of integers (n) for each round
    :return: Name of the player that won the most rounds or None if tied
    """
    if x < 1 or not nums:
        return None

    # Helper func to determine prime numbers up to a given maximum
    def sieve_of_eratosthenes(max_num):
        primes = [True] * (max_num + 1)
        primes[0] = primes[1] = False  # 0 & 1 are not prime nums
        for i in range(2, int(max_num**0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_num + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    prime_flags = sieve_of_eratosthenes(max_n)

    # Precompute the num of primes up to each num
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime_flags[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine winner for each round
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


# Example usage
if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
