"""
    Project Euler - Problem 2 - Even Fibonacci numbers
"""


def fibonacci(n: int) -> int:
    """ Fibonacci recursive function. Receives a hyperparameter n, return the n fibonacci number. """
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_with_memo(n: int, fib_dict: dict) -> int:
    """ Fibonacci recursive function with memoization. """
    if n in fib_dict:
        return fib_dict[n]
    fib_dict[n] = fibonacci_with_memo(n - 1, fib_dict) + fibonacci_with_memo(n - 2, fib_dict)
    return fib_dict[n]


def fibonacci_with_generator():
    previous_num, after_num = 1, 2
    while True:
        yield previous_num
        previous_num, after_num = after_num, previous_num + after_num


fib_sum: int = 0

for i, value in enumerate(fibonacci_with_generator()):
    if value % 2 == 0:
        fib_sum += value

    if value >= 4e6:
        break

print(fib_sum)