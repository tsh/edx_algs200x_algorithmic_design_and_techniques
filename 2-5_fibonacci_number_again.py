# Uses python3
"""Compute a Huge Fibonacci Number Modulo m"""
import sys


def get_fibonacci_huge_naive(n, m):
    seq_len = len(fib_m_seq(n, m))
    if seq_len:
        return fib(n % seq_len) % m
    else:
        return fib(n) % m


def fib_m_seq(n, m):
    if n < 1:
        return 0
    # seq begins with 0,1
    table = [0,1]
    for i in range(2, n):
        table.append((table[i-1] + table[i-2]) % m)
        if table[i-1] == 0 and table[i] == 1:  # new seq
            return table[:i-1]
    return []


def fib(n):
    if n < 1:
        return 0
    # seq begins with 0,1
    table = [0,1]
    for i in range(2, n+1):
        table.append((table[i-1] + table[i-2]))
    return table[n]

   
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

