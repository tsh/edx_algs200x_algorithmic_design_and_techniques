# Uses python3
def calc_fib(n):
    if n < 1:
        return 0
    table = [1,1] + list(range(n-2))
    for i in range(2, n):
        table[i] = table[i-1] + table[i-2]
    return table[n-1]

n = int(input())
print(calc_fib(n))
