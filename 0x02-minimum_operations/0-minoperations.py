#!/usr/bin/python3
""" A module with a method that calculates the fewest numb of operations """


def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
