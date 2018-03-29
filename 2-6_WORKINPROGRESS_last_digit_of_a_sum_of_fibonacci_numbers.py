# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    fibmap= {}

    for i in range(60-1):
        fibmap[i+1] = sum
        previous, current = current, previous + current
        sum += current
    print(fibmap)
    return sum % 10


if __name__ == '__main__':
    input = 63
    n = int(input)
    print(fibonacci_sum_naive(n))
