"""
    File: prime_factors.py
    Name: Gabriela Dias

    Project Euler: Problem 3 - Find the largest prime factor of an integer
"""
import math


def is_prime(n: int) -> bool:
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def prime_factors(n: int) -> int:
    assert n > 1, "The integer should be greater than or equal to 1"
    factors: list = []
    for i in range(2, math.floor(math.sqrt(n))+1):
        if is_prime(i):
            if n % i == 0:
                factors.append(i)
                divisor = n//i
                if is_prime(divisor):
                    factors.append(divisor)

    return factors[-1]


print(prime_factors(600851475143))
