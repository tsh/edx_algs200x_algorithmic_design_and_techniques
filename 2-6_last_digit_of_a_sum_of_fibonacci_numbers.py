# Uses python3
import sys


def fibonacci_sum_naive(n):
    """ Calculate fibonacci for n + 2"""
    prev, cur = 0, 1
    fib_sum = prev + cur
    sums = [0, fib_sum]
    # patterns repeats after 60 digits
    for i in range(58):
        prev, cur = cur, cur + prev
        fib_sum += cur
        sums.append(fib_sum %10)
    return sums[(n%60)]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))