# Uses python3
import sys


def fibonacci_sum_naive(n):
    """ Calculate fibonacci for n + 2"""
    cur, prev = 0, 1

    for i in range(n+2):
        prev, cur = cur, cur + prev
    fib_sum = cur - 1
    return fib_sum % 10


if __name__ == '__main__':
    input = 63
    n = int(input)
    print(fibonacci_sum_naive(n))
