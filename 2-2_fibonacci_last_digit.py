# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n < 1:
        return 0
    table = [1,1] + list(range(n-2))
    for i in range(2, n):
        table[i] = (table[i-1] + table[i-2]) % 10
    return table[n-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
