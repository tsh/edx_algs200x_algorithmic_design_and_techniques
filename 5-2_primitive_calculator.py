def calculate(n):
    table = [0,1,1,1] + [float('inf')] * (n - 3)
    for i in range(4, n+1):
        num_ops = [table[i-1]+1]
        if i % 2 == 0:
            num_ops.append(table[i//2]+1)
        if i % 3 == 0:
            num_ops.append(table[i//3]+1)
        table[i] = min(num_ops)
    return table[n]

if __name__ == '__main__':
    print(calculate(1))  # 0
    print(calculate(5))  # 3
    print(calculate(96234))  # 14
    print(calculate(98734))