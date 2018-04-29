# Uses python3
import sys


def fibonacci_sum_naive(n):
    """ Calculate fibonacci for n + 2"""
    prev, cur = 0, 1
    fibs = [prev, cur]
    for i in range(58):
        prev, cur = cur, cur + prev
        fibs.append(cur % 10)
    print(fibs)
    return fibs[(n%58)+3] - 1


if __name__ == '__main__':
    input = 100
    n = int(input)
    print(fibonacci_sum_naive(n))
    # assert fibonacci_sum_naive(239) == 0
    # assert fibonacci_sum_naive(100) == 5
    # assert fibonacci_sum_naive(3) == 4
